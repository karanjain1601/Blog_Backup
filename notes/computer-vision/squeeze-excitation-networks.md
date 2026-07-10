---
title: "Squeeze-and-Excitation Networks"
slug: "squeeze-excitation-networks"
description: "Channel attention via global average pooling (squeeze) and two FC layers (excitation) — how SE blocks recalibrate channel-wise feature responses and improve accuracy with minimal parameter overhead."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImgyIiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTcXVlZXplLWFuZC1FeGNpdGF0aW9uIChTRSkgTmV0d29ya3MsIGludHJvZHVjZWQgYnkgSHUgZXQgYWwuIGF0IENWUFIgMjAxOCwgd29uIHRoZSBJbWFnZU5ldCBJTFNWUkMgY2xhc3NpZmljYXRpb24gY2hhbGxlbmdlLiBUaGUgY29yZSBpZGVhIGlzIGNoYW5uZWwgYXR0ZW50aW9uOiBsZWFybiB3aGljaCBmZWF0dXJlIGNoYW5uZWxzIGFyZSBtb3N0IGluZm9ybWF0aXZlIGZvciBhIGdpdmVuIGlucHV0IGFuZCByZWNhbGlicmF0ZSB0aGVpciByZXNwb25zZXMgYWNjb3JkaW5nbHkuIFRoaXMgaXMgYWNoaWV2ZWQgdGhyb3VnaCBhIGxpZ2h0d2VpZ2h0IGdhdGluZyBtZWNoYW5pc20gdGhhdCBhZGRzIG1pbmltYWwgcGFyYW1ldGVycy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIENOTnMgdHJlYXQgYWxsIGNoYW5uZWxzIGVxdWFsbHkgd2hlbiBjb21iaW5pbmcgZmVhdHVyZSBtYXBzLiBTRSBibG9ja3MgYWRkcmVzcyB0aGlzIGJ5IGV4cGxpY2l0bHkgbW9kZWxpbmcgY2hhbm5lbCBpbnRlcmRlcGVuZGVuY2llcy4gR2l2ZW4gYSBmZWF0dXJlIG1hcCBvZiBzaGFwZSAoSCwgVywgQyksIFNFIGJsb2NrcyBwcm9kdWNlIGEgdmVjdG9yIG9mIEMgd2VpZ2h0cyDigJQgb25lIHBlciBjaGFubmVsIOKAlCB0aGF0IGFtcGxpZnkgdXNlZnVsIGZlYXR1cmVzIGFuZCBzdXBwcmVzcyBsZXNzIHJlbGV2YW50IG9uZXMsIGltcHJvdmluZyByZXByZXNlbnRhdGlvbmFsIHBvd2VyIHdpdGhvdXQgY2hhbmdpbmcgc3BhdGlhbCByZXNvbHV0aW9uLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IlNxdWVlemU6IEdsb2JhbCBDb250ZXh0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc3F1ZWV6ZSBvcGVyYXRpb24gY29tcHJlc3NlcyBzcGF0aWFsIGluZm9ybWF0aW9uIGludG8gYSBjaGFubmVsIGRlc2NyaXB0b3IuIEdsb2JhbCBBdmVyYWdlIFBvb2xpbmcgKEdBUCkgYWdncmVnYXRlcyBlYWNoIGNoYW5uZWxcdTAwMjdzIGZlYXR1cmUgbWFwIGludG8gYSBzaW5nbGUgc2NhbGFyIGJ5IGF2ZXJhZ2luZyBvdmVyIGFsbCBIw5dXIHNwYXRpYWwgcG9zaXRpb25zLiBUaGUgcmVzdWx0IGlzIGEgdmVjdG9yIHog4oiIIOKEnV5DLCB3aGVyZSB6X2MgPSAoMS9Iw5dXKSDOoyB1X2MoaSxqKS4gVGhpcyBnaXZlcyB0aGUgbmV0d29yayBhIGdsb2JhbCB2aWV3IG9mIGVhY2ggY2hhbm5lbFx1MDAyN3MgYWN0aXZhdGlvbiBkaXN0cmlidXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHQVAgaXMgY2hvc2VuIG92ZXIgbW9yZSBjb21wbGV4IHBvb2xpbmcgc3RyYXRlZ2llcyBiZWNhdXNlIGl0IGlzIGRpZmZlcmVudGlhYmxlLCBjb21wdXRhdGlvbmFsbHkgZnJlZSwgYW5kIGNhcHR1cmVzIGhvbGlzdGljIGNoYW5uZWwtbGV2ZWwgc3RhdGlzdGljcy4gSXQgYWxsb3dzIHRoZSBzdWJzZXF1ZW50IGV4Y2l0YXRpb24gbW9kdWxlIHRvIHJlYXNvbiBhYm91dCBjaGFubmVsIHJlbGF0aW9uc2hpcHMgaW4gYSBwb3NpdGlvbi1hZ25vc3RpYyBtYW5uZXIsIGZvY3VzaW5nIG9uIHdoYXQgaXMgcHJlc2VudCByYXRoZXIgdGhhbiB3aGVyZSBpdCBhcHBlYXJzIGluIHRoZSBzcGF0aWFsIGRpbWVuc2lvbnMgb2YgdGhlIGZlYXR1cmUgbWFwLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IkV4Y2l0YXRpb246IENoYW5uZWwgUmVjYWxpYnJhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGV4Y2l0YXRpb24gb3BlcmF0aW9uIHRyYW5zZm9ybXMgdGhlIHNxdWVlemVkIGRlc2NyaXB0b3IgeiBpbnRvIGNoYW5uZWwgd2VpZ2h0cyBzIOKIiCBbMCwxXV5DLiBUd28gZnVsbHkgY29ubmVjdGVkIGxheWVycyBmb3JtIGEgYm90dGxlbmVjazogeiBpcyBwcm9qZWN0ZWQgZG93biBmcm9tIEMgdG8gQy9yIG5ldXJvbnMgKHIgaXMgdGhlIHJlZHVjdGlvbiByYXRpbyksIHRoZW4gYmFjayB1cCB0byBDIG5ldXJvbnMuIEEgc2lnbW9pZCBhY3RpdmF0aW9uIGVuc3VyZXMgZWFjaCB3ZWlnaHQgbGllcyBpbiBbMCwxXSwgZW5hYmxpbmcgc29mdCwgZGlmZmVyZW50aWFibGUgY2hhbm5lbCBzZWxlY3Rpb24gdGhhdCByZWNhbGlicmF0ZXMgZmVhdHVyZSByZXNwb25zZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaC5ubiBhcyBublxuY2xhc3MgU0VCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjaGFubmVscywgcmVkdWN0aW9uPTE2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucG9vbCA9IG5uLkFkYXB0aXZlQXZnUG9vbDJkKDEpXG4gICAgICAgIHNlbGYuZmMgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGNoYW5uZWxzLCBjaGFubmVscyAvLyByZWR1Y3Rpb24sIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGNoYW5uZWxzIC8vIHJlZHVjdGlvbiwgY2hhbm5lbHMsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uU2lnbW9pZCgpXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgYiwgYyA9IHguc2hhcGVbOjJdXG4gICAgICAgIHMgPSBzZWxmLmZjKHNlbGYucG9vbCh4KS52aWV3KGIsIGMpKS52aWV3KGIsIGMsIDEsIDEpXG4gICAgICAgIHJldHVybiB4ICogcyJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IlNFIEJsb2NrIEltcGxlbWVudGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcmVkdWN0aW9uIHJhdGlvIHIgY29udHJvbHMgdGhlIGJvdHRsZW5lY2sgc2l6ZSwgdHJhZGluZyBvZmYgYWNjdXJhY3kgYWdhaW5zdCBwYXJhbWV0ZXIgZWZmaWNpZW5jeS4gQSBzbWFsbGVyIHIgKGUuZy4sIHI9NCkgZW5hYmxlcyByaWNoZXIgY2hhbm5lbCBpbnRlcmFjdGlvbnMgYnV0IGFkZHMgbW9yZSBwYXJhbWV0ZXJzOyBhIGxhcmdlciByIChlLmcuLCByPTMyKSBpcyBtb3JlIGZydWdhbCBidXQgbWF5IGxvc2UgcmVwcmVzZW50YXRpb25hbCBjYXBhY2l0eS4gVGhlIG9yaWdpbmFsIHBhcGVyIHJlY29tbWVuZHMgcj0xNiBhcyBhIGRlZmF1bHQsIGJhbGFuY2luZyBhY2N1cmFjeSBnYWlucyBhbmQgY29tcHV0YXRpb25hbCBvdmVyaGVhZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiY2xhc3MgU0VSZXNCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjaGFubmVscywgcmVkdWN0aW9uPTE2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuY29udjEgPSBubi5Db252MmQoY2hhbm5lbHMsIGNoYW5uZWxzLCAzLCBwYWRkaW5nPTEpXG4gICAgICAgIHNlbGYuYm4xICAgPSBubi5CYXRjaE5vcm0yZChjaGFubmVscylcbiAgICAgICAgc2VsZi5jb252MiA9IG5uLkNvbnYyZChjaGFubmVscywgY2hhbm5lbHMsIDMsIHBhZGRpbmc9MSlcbiAgICAgICAgc2VsZi5ibjIgICA9IG5uLkJhdGNoTm9ybTJkKGNoYW5uZWxzKVxuICAgICAgICBzZWxmLnNlICAgID0gU0VCbG9jayhjaGFubmVscywgcmVkdWN0aW9uKVxuICAgICAgICBzZWxmLnJlbHUgID0gbm4uUmVMVShpbnBsYWNlPVRydWUpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG91dCA9IHNlbGYucmVsdShzZWxmLmJuMShzZWxmLmNvbnYxKHgpKSlcbiAgICAgICAgb3V0ID0gc2VsZi5ibjIoc2VsZi5jb252MihvdXQpKVxuICAgICAgICBvdXQgPSBzZWxmLnNlKG91dCkgICAgICAgICAgIyByZWNhbGlicmF0ZSBjaGFubmVsc1xuICAgICAgICByZXR1cm4gc2VsZi5yZWx1KG91dCArIHgpICAjIGFkZCBza2lwIGNvbm5lY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNFIGJsb2NrcyBpbnRlZ3JhdGUgc2VhbWxlc3NseSBpbnRvIGV4aXN0aW5nIGFyY2hpdGVjdHVyZXMgYXMgZHJvcC1pbiBtb2R1bGVzLiBJbiBSZXNOZXRzLCB0aGUgU0UgYmxvY2sgaXMgaW5zZXJ0ZWQgYWZ0ZXIgdGhlIHNlY29uZCBjb252b2x1dGlvbiBhbmQgYmVmb3JlIHRoZSByZXNpZHVhbCBhZGRpdGlvbi4gSW4gVkdHLXN0eWxlIG5ldHdvcmtzIGl0IGZvbGxvd3MgZWFjaCBjb252b2x1dGlvbmFsIGJsb2NrLiBQbGFjZW1lbnQgYmVmb3JlIHRoZSBza2lwIGNvbm5lY3Rpb24gZW5zdXJlcyByZWNhbGlicmF0aW9uIGhhcHBlbnMgb24gdHJhbnNmb3JtZWQgZmVhdHVyZXMsIHByZXNlcnZpbmcgdGhlIGlkZW50aXR5IHNob3J0Y3V0XHUwMDI3cyBncmFkaWVudCBmbG93LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJkZWYgc3dlZXBfcmVkdWN0aW9uX3JhdGlvcyh2YWxfbG9hZGVyLCByYXRpb3M9WzQsIDgsIDE2LCAzMl0pOlxuICAgIHJlc3VsdHMgPSB7fVxuICAgIGZvciByIGluIHJhdGlvczpcbiAgICAgICAgbW9kZWwgPSBTRVJlc05ldDUwKHJlZHVjdGlvbj1yKS5jdWRhKClcbiAgICAgICAgcGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpXG4gICAgICAgIGFjYyA9IGV2YWx1YXRlKG1vZGVsLCB2YWxfbG9hZGVyKVxuICAgICAgICByZXN1bHRzW3JdID0ge1xuICAgICAgICAgICAgXCJwYXJhbXNfTVwiOiBwYXJhbXMgLyAxZTYsXG4gICAgICAgICAgICBcInRvcDFfYWNjXCI6IGFjY1xuICAgICAgICB9XG4gICAgICAgIHByaW50KGZcInI9e3J9OiB7cGFyYW1zLzFlNjouMWZ9TSBwYXJhbXMsIHthY2M6LjJmfSUgdG9wLTFcIilcbiAgICByZXR1cm4gcmVzdWx0cyJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IkludGVncmF0aW9uIGFuZCBPdmVyaGVhZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU0UgYmxvY2tzIGFyZSBjb21wdXRhdGlvbmFsbHkgZWZmaWNpZW50OiB0aGUgc3F1ZWV6ZSBvcGVyYXRpb24gKEdBUCkgaXMgcGFyYW1ldGVyLWZyZWUsIGFuZCB0aGUgdHdvIEZDIGxheWVycyBhZGQgb25seSAyKEPCsi9yKSBwYXJhbWV0ZXJzIHBlciBibG9jay4gRm9yIGEgUmVzTmV0LTUwIHdpdGggfjI1TSBwYXJhbWV0ZXJzLCBhZGRpbmcgU0UgYmxvY2tzIHdpdGggcj0xNiBpbmNyZWFzZXMgcGFyYW1ldGVyIGNvdW50IGJ5IGFib3V0IDIuNU0gKH4xMCUpLCB5ZXQgY29uc2lzdGVudGx5IGRlbGl2ZXJzIDHigJMyJSB0b3AtMSBhY2N1cmFjeSBnYWlucyBvbiBJbWFnZU5ldCDigJQgYSBoaWdobHkgZmF2b3JhYmxlIHRyYWRlLW9mZi4ifSx7InR5cGUiOiJ0YWJsZSIsImNvbnRlbnQiOiJ8IE1vZGVsIHwgU0UgUmF0aW8gfCBFeHRyYSBQYXJhbXMgJSB8IFRvcC0xIEdhaW4gfCBGTE9QcyBPdmVyaGVhZCB8XG58LS0tfC0tLXwtLS18LS0tfC0tLXxcbnwgU0UtUmVzTmV0LTUwIHI9NCB8IDQgfCAxOS4zJSB8ICsxLjglIHwgXHUwMDNjMC4xJSB8XG58IFNFLVJlc05ldC01MCByPTggfCA4IHwgOS43JSB8ICsxLjclIHwgXHUwMDNjMC4xJSB8XG58IFNFLVJlc05ldC01MCByPTE2IHwgMTYgfCA0LjklIHwgKzEuNiUgfCBcdTAwM2MwLjElIHxcbnwgU0UtUmVzTmV0LTUwIHI9MzIgfCAzMiB8IDIuNSUgfCArMS4zJSB8IFx1MDAzYzAuMSUgfFxufCBFZmZpY2llbnROZXQgU0UgfCA0IHwgMi4xJSB8ICswLjQlIHwgXHUwMDNjMC4xJSB8XG58IE1vYmlsZU5ldFYzIFNFIHwgNCB8IDMuMiUgfCArMS4wJSB8IFx1MDAzYzAuMSUgfCJ9LHsidHlwZSI6ImNhbGxvdXQiLCJjYWxsb3V0VHlwZSI6ImluZm8iLCJjb250ZW50IjoiU0UgYmxvY2tzIGFkZCBvbmx5IH4yJSBleHRyYSBwYXJhbWV0ZXJzIGJ1dCBjb25zaXN0ZW50bHkgeWllbGQgMeKAkzIlIHRvcC0xIGFjY3VyYWN5IGdhaW5zIOKAlCB0aGV5IGFyZSBub3cgc3RhbmRhcmQgaW4gRWZmaWNpZW50TmV0LCBNb2JpbGVOZXRWMywgYW5kIFJlZ05ldCBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRkxPUHMgb3ZlcmhlYWQgZnJvbSBTRSBibG9ja3MgaXMgbmVnbGlnaWJsZSBiZWNhdXNlIHRoZSBGQyBsYXllcnMgb3BlcmF0ZSBvbiB0aGUgY2hhbm5lbCB2ZWN0b3IgKEMgdmFsdWVzKSByYXRoZXIgdGhhbiBmdWxsIGZlYXR1cmUgbWFwcyAoSMOXV8OXQyB2YWx1ZXMpLiBGb3IgYSAxNMOXMTTDlzUxMiBmZWF0dXJlIG1hcCwgR0FQIHJlZHVjZXMgc3BhdGlhbCBkaW1lbnNpb25zIGVudGlyZWx5LCBzbyBzdWJzZXF1ZW50IEZDIGxheWVycyBwcm9jZXNzIG9ubHkgNTEyIHZhbHVlcyDigJQgb3JkZXJzIG9mIG1hZ25pdHVkZSBjaGVhcGVyIHRoYW4gdGhlIHNwYXRpYWwgY29udm9sdXRpb24gb3BlcmF0aW9ucyB0aGV5IGFjY29tcGFueS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoLCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmRlZiB2aXN1YWxpemVfc2Vfd2VpZ2h0cyhtb2RlbCwgeCk6XG4gICAgd2VpZ2h0cyA9IHt9XG4gICAgZGVmIGhvb2sobmFtZSk6XG4gICAgICAgIGRlZiBmbihtLCBpbnAsIG91dCk6XG4gICAgICAgICAgICB3ZWlnaHRzW25hbWVdID0gb3V0LmRldGFjaCgpLnNxdWVlemUoKS5jcHUoKVxuICAgICAgICByZXR1cm4gZm5cbiAgICBmb3IgbmFtZSwgbSBpbiBtb2RlbC5uYW1lZF9tb2R1bGVzKCk6XG4gICAgICAgIGlmIGlzaW5zdGFuY2UobSwgU0VCbG9jayk6XG4gICAgICAgICAgICBtLmZjLnJlZ2lzdGVyX2ZvcndhcmRfaG9vayhob29rKG5hbWUpKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBtb2RlbCh4KVxuICAgIGZvciBuYW1lLCB3IGluIHdlaWdodHMuaXRlbXMoKTpcbiAgICAgICAgcGx0LmJhcihyYW5nZShsZW4odykpLCB3Lm51bXB5KCkpXG4gICAgICAgIHBsdC50aXRsZShmXCJTRSB3ZWlnaHRzOiB7bmFtZX1cIik7IHBsdC5zaG93KCkifSx7InR5cGUiOiJoMiIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTRSBOZXR3b3JrcyBkZW1vbnN0cmF0ZSB0aGF0IGV4cGxpY2l0IGNoYW5uZWwgYXR0ZW50aW9uIGlzIGEgcG93ZXJmdWwgYW5kIGdlbmVyYWwgdGVjaG5pcXVlIGZvciBpbXByb3ZpbmcgQ05OIHBlcmZvcm1hbmNlLiBUaGUgc3F1ZWV6ZS1leGNpdGF0aW9uIHBhcmFkaWdtIOKAlCBhZ2dyZWdhdGUgZ2xvYmFsIGNvbnRleHQsIGxlYXJuIGNoYW5uZWwgd2VpZ2h0cywgcmVjYWxpYnJhdGUg4oCUIGlzIGludHVpdGl2ZSBhbmQgZWZmZWN0aXZlLiBUaGUgb3JpZ2luYWwgU0UtUmVzTmV0LTE1NCBhY2hpZXZlZCAyLjI1MSUgdG9wLTUgZXJyb3Igb24gSW1hZ2VOZXQsIHdpbm5pbmcgdGhlIElMU1ZSQyAyMDE3IGNsYXNzaWZpY2F0aW9uIGNoYWxsZW5nZSBvdXRyaWdodC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSByZWR1Y3Rpb24gcmF0aW8gciBvZmZlcnMgYSBkaXJlY3Qga25vYiBmb3IgdGhlIGFjY3VyYWN5LWVmZmljaWVuY3kgdHJhZGUtb2ZmLiBQcmFjdGl0aW9uZXJzIHNob3VsZCBiZW5jaG1hcmsgcj04IGFuZCByPTE2IGZpcnN0OyByPTQgaXMgd29ydGggZXhwbG9yaW5nIHdoZW4gYWNjdXJhY3kgaXMgdGhlIHByaW9yaXR5IGFuZCBjb21wdXRlIGJ1ZGdldCBhbGxvd3MuIFNFIGJsb2NrcyBhcmUgcGFydGljdWxhcmx5IGJlbmVmaWNpYWwgaW4gZGVwdGh3aXNlLXNlcGFyYWJsZSBhcmNoaXRlY3R1cmVzIHN1Y2ggYXMgTW9iaWxlTmV0cywgd2hlcmUgY2hhbm5lbCBtaXhpbmcgaXMgbGltaXRlZCBieSB0aGUgZmFjdG9yZWQgY29udm9sdXRpb24gZGVzaWduLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU0UgTmV0d29ya3MgaW5zcGlyZWQgc3Vic2VxdWVudCBhdHRlbnRpb24gbWVjaGFuaXNtczogQ0JBTSBleHRlbmRzIGNoYW5uZWwgYXR0ZW50aW9uIHdpdGggc3BhdGlhbCBhdHRlbnRpb247IEVDQS1OZXQgcmVwbGFjZXMgRkMgbGF5ZXJzIHdpdGggMUQgY29udm9sdXRpb24gb3ZlciBhZGphY2VudCBjaGFubmVscyBmb3IgbG93ZXIgb3ZlcmhlYWQ7IEdFLU5ldHMgdXNlIGdhdGhlci1leGNpdGUgdG8gY2FwdHVyZSBzcGF0aWFsIGNvbnRleHQgYXQgbXVsdGlwbGUgc2NhbGVzLiBEZXNwaXRlIHRoZXNlIGFkdmFuY2VzLCBTRSBibG9ja3MgcmVtYWluIGEgZ28tdG8gY2hvaWNlIGR1ZSB0byB0aGVpciBzaW1wbGljaXR5IGFuZCBzdHJvbmcgZW1waXJpY2FsIHJlc3VsdHMuIn1d"
---
# Squeeze-and-Excitation Networks

Squeeze-and-Excitation (SE) Networks, introduced by Hu et al. at CVPR 2018, won the ImageNet ILSVRC classification challenge. The core idea is channel attention: learn which feature channels are most informative for a given input and recalibrate their responses accordingly. This is achieved through a lightweight gating mechanism that adds minimal parameters.

Standard CNNs treat all channels equally when combining feature maps. SE blocks address this by explicitly modeling channel interdependencies. Given a feature map of shape (H, W, C), SE blocks produce a vector of C weights — one per channel — that amplify useful features and suppress less relevant ones, improving representational power without changing spatial resolution.

The squeeze operation compresses spatial information into a channel descriptor. Global Average Pooling (GAP) aggregates each channel's feature map into a single scalar by averaging over all H×W spatial positions. The result is a vector z ∈ ℝ^C, where z_c = (1/H×W) Σ u_c(i,j). This gives the network a global view of each channel's activation distribution.

GAP is chosen over more complex pooling strategies because it is differentiable, computationally free, and captures holistic channel-level statistics. It allows the subsequent excitation module to reason about channel relationships in a position-agnostic manner, focusing on what is present rather than where it appears in the spatial dimensions of the feature map.

The excitation operation transforms the squeezed descriptor z into channel weights s ∈ [0,1]^C. Two fully connected layers form a bottleneck: z is projected down from C to C/r neurons (r is the reduction ratio), then back up to C neurons. A sigmoid activation ensures each weight lies in [0,1], enabling soft, differentiable channel selection that recalibrates feature responses.

```python
import torch.nn as nn
class SEBlock(nn.Module):
    def __init__(self, channels, reduction=16):
        super().__init__()
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channels, channels // reduction, bias=False),
            nn.ReLU(),
            nn.Linear(channels // reduction, channels, bias=False),
            nn.Sigmoid()
        )
    def forward(self, x):
        b, c = x.shape[:2]
        s = self.fc(self.pool(x).view(b, c)).view(b, c, 1, 1)
        return x * s
```

The reduction ratio r controls the bottleneck size, trading off accuracy against parameter efficiency. A smaller r (e.g., r=4) enables richer channel interactions but adds more parameters; a larger r (e.g., r=32) is more frugal but may lose representational capacity. The original paper recommends r=16 as a default, balancing accuracy gains and computational overhead.

```python
class SEResBlock(nn.Module):
    def __init__(self, channels, reduction=16):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1   = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2   = nn.BatchNorm2d(channels)
        self.se    = SEBlock(channels, reduction)
        self.relu  = nn.ReLU(inplace=True)
    def forward(self, x):
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out = self.se(out)          # recalibrate channels
        return self.relu(out + x)  # add skip connection
```

SE blocks integrate seamlessly into existing architectures as drop-in modules. In ResNets, the SE block is inserted after the second convolution and before the residual addition. In VGG-style networks it follows each convolutional block. Placement before the skip connection ensures recalibration happens on transformed features, preserving the identity shortcut's gradient flow.

```python
def sweep_reduction_ratios(val_loader, ratios=[4, 8, 16, 32]):
    results = {}
    for r in ratios:
        model = SEResNet50(reduction=r).cuda()
        params = sum(p.numel() for p in model.parameters())
        acc = evaluate(model, val_loader)
        results[r] = {
            "params_M": params / 1e6,
            "top1_acc": acc
        }
        print(f"r={r}: {params/1e6:.1f}M params, {acc:.2f}% top-1")
    return results
```

SE blocks are computationally efficient: the squeeze operation (GAP) is parameter-free, and the two FC layers add only 2(C²/r) parameters per block. For a ResNet-50 with ~25M parameters, adding SE blocks with r=16 increases parameter count by about 2.5M (~10%), yet consistently delivers 1–2% top-1 accuracy gains on ImageNet — a highly favorable trade-off.

|  |
| --- |

> ****: SE blocks add only ~2% extra parameters but consistently yield 1–2% top-1 accuracy gains — they are now standard in EfficientNet, MobileNetV3, and RegNet architectures.

FLOPs overhead from SE blocks is negligible because the FC layers operate on the channel vector (C values) rather than full feature maps (H×W×C values). For a 14×14×512 feature map, GAP reduces spatial dimensions entirely, so subsequent FC layers process only 512 values — orders of magnitude cheaper than the spatial convolution operations they accompany.

```python
import torch, matplotlib.pyplot as plt
def visualize_se_weights(model, x):
    weights = {}
    def hook(name):
        def fn(m, inp, out):
            weights[name] = out.detach().squeeze().cpu()
        return fn
    for name, m in model.named_modules():
        if isinstance(m, SEBlock):
            m.fc.register_forward_hook(hook(name))
    with torch.no_grad():
        model(x)
    for name, w in weights.items():
        plt.bar(range(len(w)), w.numpy())
        plt.title(f"SE weights: {name}"); plt.show()
```

SE Networks demonstrate that explicit channel attention is a powerful and general technique for improving CNN performance. The squeeze-excitation paradigm — aggregate global context, learn channel weights, recalibrate — is intuitive and effective. The original SE-ResNet-154 achieved 2.251% top-5 error on ImageNet, winning the ILSVRC 2017 classification challenge outright.

The reduction ratio r offers a direct knob for the accuracy-efficiency trade-off. Practitioners should benchmark r=8 and r=16 first; r=4 is worth exploring when accuracy is the priority and compute budget allows. SE blocks are particularly beneficial in depthwise-separable architectures such as MobileNets, where channel mixing is limited by the factored convolution design.

SE Networks inspired subsequent attention mechanisms: CBAM extends channel attention with spatial attention; ECA-Net replaces FC layers with 1D convolution over adjacent channels for lower overhead; GE-Nets use gather-excite to capture spatial context at multiple scales. Despite these advances, SE blocks remain a go-to choice due to their simplicity and strong empirical results.

