---
title: "Image Representation in Deep Learning"
slug: "image-representation"
description: "How digital images are stored as tensors — channels, dtypes, memory layout, PIL vs OpenCV conventions, and the NumPy/PyTorch array formats used in vision pipelines."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImgyIiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaWdpdGFsIGltYWdlcyBhcmUgbXVsdGktZGltZW5zaW9uYWwgYXJyYXlzIG9mIHBpeGVsIHZhbHVlcy4gSW4gZGVlcCBsZWFybmluZyBwaXBlbGluZXMsIGltYWdlcyBtb3ZlIHRocm91Z2ggc2V2ZXJhbCByZXByZXNlbnRhdGlvbnM6IHJhdyBmaWxlcyBvbiBkaXNrLCBQSUwgSW1hZ2Ugb2JqZWN0cywgTnVtUHkgYXJyYXlzLCBhbmQgUHlUb3JjaCB0ZW5zb3JzLiBFYWNoIGZvcm1hdCBoYXMgZGlmZmVyZW50IGF4aXMgb3JkZXJpbmcsIGR0eXBlLCBhbmQgdmFsdWUgcmFuZ2VzLiBVbmRlcnN0YW5kaW5nIHRoZXNlIGNvbnZlbnRpb25zIHByZXZlbnRzIHN1YnRsZSBidWdzIGluIHByZXByb2Nlc3NpbmcgYW5kIG1vZGVsIGluZmVyZW5jZSBwaXBlbGluZXMuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiUGl4ZWwgQXJyYXlzIGFuZCBDaGFubmVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBncmF5c2NhbGUgaW1hZ2UgaXMgYSAyRCBhcnJheSBvZiBzaGFwZSAoSCwgVykuIEEgY29sb3IgaW1hZ2UgYWRkcyBhIGNoYW5uZWwgZGltZW5zaW9uIGdpdmluZyBzaGFwZSAoSCwgVywgQykg4oCUIGhlaWdodCwgd2lkdGgsIGNoYW5uZWxzLiBUaGlzIEhXQyBsYXlvdXQgaXMgdXNlZCBieSBQSUwsIE51bVB5LCBhbmQgT3BlbkNWLiBQeVRvcmNoIHVzZXMgQ0hXIGxheW91dCB3aGVyZSBjaGFubmVscyBjb21lIGZpcnN0LiBDb252ZXJ0aW5nIGJldHdlZW4gdGhlc2UgbGF5b3V0cyBpcyBhIGNvbW1vbiBzb3VyY2Ugb2Ygc2hhcGUgbWlzbWF0Y2ggZXJyb3JzIGluIHZpc2lvbiBjb2RlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIFBJTCBpbXBvcnQgSW1hZ2VcbmltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5cbmltZyA9IEltYWdlLm9wZW4oXHUwMDI3c2FtcGxlLmpwZ1x1MDAyNykuY29udmVydChcdTAwMjdSR0JcdTAwMjcpXG5hcnIgPSBucC5hcnJheShpbWcpICAgICAgICAgICMgSFdDLCB1aW50OCwgWzAsIDI1NV1cbnByaW50KFx1MDAyN051bVB5IEhXQyBzaGFwZTpcdTAwMjcsIGFyci5zaGFwZSlcblxudGVuc29yID0gdG9yY2guZnJvbV9udW1weShhcnIpLnBlcm11dGUoMiwgMCwgMSkgICMgQ0hXXG50ZW5zb3IgPSB0ZW5zb3IuZmxvYXQoKSAvIDI1NS4wICAgICAgICAgICAgICAgICAgICMgZmxvYXQzMiBbMCwgMV1cbnByaW50KFx1MDAyN1RlbnNvciBDSFcgc2hhcGU6XHUwMDI3LCB0ZW5zb3Iuc2hhcGUpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBSR0IgaW1hZ2VzIGhhdmUgMyBjaGFubmVscy4gR3JheXNjYWxlIGhhcyAxLiBSR0JBIGltYWdlcyBoYXZlIDQgY2hhbm5lbHMgaW5jbHVkaW5nIGFscGhhIHRyYW5zcGFyZW5jeS4gVGhlIGNoYW5uZWwgZGltZW5zaW9uIHJlcHJlc2VudHMgc3BlY3RyYWwgaW5mb3JtYXRpb24gYXQgZWFjaCBwaXhlbCBsb2NhdGlvbi4gQ2hhbm5lbCBvcmRlcmluZyDigJQgd2hldGhlciBSR0Igb3IgQkdSIOKAlCBkZXRlcm1pbmVzIGhvdyBjb2xvciBpbmZvcm1hdGlvbiBpcyBpbnRlcnByZXRlZCBieSB0aGUgbW9kZWwuIEFsd2F5cyB2ZXJpZnkgY2hhbm5lbCBvcmRlciB3aGVuIGludGVncmF0aW5nIG11bHRpcGxlIGxpYnJhcmllcyBpbiBvbmUgcGlwZWxpbmUuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiSW1hZ2UgRHR5cGVzIGFuZCBWYWx1ZSBSYW5nZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkltYWdlcyBhcmUgc3RvcmVkIGluIGRpZmZlcmVudCBudW1lcmljIGZvcm1hdHMgZGVwZW5kaW5nIG9uIHRoZSBzb3VyY2UuIFJhdyBwaXhlbCBkYXRhIGZyb20gY2FtZXJhcyBpcyB0eXBpY2FsbHkgdWludDggd2l0aCB2YWx1ZXMgMOKAkzI1NS4gRGVlcCBsZWFybmluZyBtb2RlbHMgZXhwZWN0IGZsb2F0MzIgaW5wdXRzIG5vcm1hbGl6ZWQgdG8gWzAsIDFdIG9yIFstMSwgMV0uIENvbnZlcnRpbmcgYmV0d2VlbiB0aGVzZSByYW5nZXMgaXMgYSBjcml0aWNhbCBwcmVwcm9jZXNzaW5nIHN0ZXAg4oCUIGZhaWxpbmcgdG8gc2NhbGUgY2FuIGNhdXNlIE5hTiBncmFkaWVudHMgb3IgdmVyeSBzbG93IGNvbnZlcmdlbmNlIGR1cmluZyB0cmFpbmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGN2MlxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmltZ19iZ3IgPSBjdjIuaW1yZWFkKFx1MDAyN3NhbXBsZS5qcGdcdTAwMjcpICAgICAgICAgICAgICAjIEhXQyB1aW50OCBCR1JcbmltZ19yZ2IgPSBjdjIuY3Z0Q29sb3IoaW1nX2JnciwgY3YyLkNPTE9SX0JHUjJSR0IpICAjIGNvbnZlcnQgdG8gUkdCXG5cbmltZ19mbG9hdCA9IGltZ19yZ2IuYXN0eXBlKG5wLmZsb2F0MzIpIC8gMjU1LjAgICMgdWludDgg4oaSIGZsb2F0MzIgWzAsIDFdXG5wcmludChcdTAwMjdmbG9hdDMyIHJhbmdlOlx1MDAyNywgaW1nX2Zsb2F0Lm1pbigpLCBpbWdfZmxvYXQubWF4KCkpXG5cbmltZ191aW50OCA9IChpbWdfZmxvYXQgKiAyNTUuMCkuY2xpcCgwLCAyNTUpLmFzdHlwZShucC51aW50OClcbnByaW50KFx1MDAyN3VpbnQ4IHJhbmdlOlx1MDAyNywgaW1nX3VpbnQ4Lm1pbigpLCBpbWdfdWludDgubWF4KCkpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGbG9hdDE2IGlzIHNvbWV0aW1lcyB1c2VkIGluIG1peGVkLXByZWNpc2lvbiB0cmFpbmluZyB0byByZWR1Y2UgR1BVIG1lbW9yeS4gQmUgY2FyZWZ1bCB3aGVuIGNvbnZlcnRpbmc6IGRpdmlkaW5nIHVpbnQ4IGJ5IDI1NS4wIGdpdmVzIGZsb2F0NjQgaW4gTnVtUHkgYnkgZGVmYXVsdCDigJQgZXhwbGljaXRseSBjYXN0IHRvIGZsb2F0MzIgdG8gYXZvaWQgZG91YmxpbmcgbWVtb3J5IHVzYWdlLiBQeVRvcmNoXHUwMDI3cyB0ZW5zb3IuZmxvYXQoKSBjb252ZXJ0cyB0byBmbG9hdDMyLiBVc2luZyAuaGFsZigpIGdpdmVzIGZsb2F0MTYgZm9yIGluZmVyZW5jZSBvbiBzdXBwb3J0ZWQgaGFyZHdhcmUgYWNjZWxlcmF0b3JzLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IlBJTCB2cyBPcGVuQ1YgQ29udmVudGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBJTCAoUGlsbG93KSBhbmQgT3BlbkNWIGFyZSB0aGUgdHdvIGRvbWluYW50IGltYWdlIEkvTyBsaWJyYXJpZXMgaW4gUHl0aG9uLiBQSUwgcmV0dXJucyBpbWFnZXMgaW4gUkdCIG9yZGVyIGFuZCB1c2VzIHRoZSBIV0MgTnVtUHkgY29udmVudGlvbi4gT3BlbkNWIGxvYWRzIGltYWdlcyBhcyBOdW1QeSBhcnJheXMgaW4gQkdSIG9yZGVyIOKAlCB0aGUgYmx1ZSBhbmQgcmVkIGNoYW5uZWxzIGFyZSBzd2FwcGVkLiBUaGlzIGRpZmZlcmVuY2UgaXMgaW52aXNpYmxlIHRvIHRoZSBleWUgYnV0IGNhdXNlcyBtb2RlbCBwcmVkaWN0aW9ucyB0byBkZWdyYWRlIHdoZW4gY2hhbm5lbHMgYXJlIG1pc21hdGNoZWQgYXQgaW5mZXJlbmNlIHRpbWUuIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRUeXBlIjoid2FybmluZyIsImNvbnRlbnQiOiJPcGVuQ1YgbG9hZHMgaW1hZ2VzIGFzIEJHUiBieSBkZWZhdWx0IOKAlCBhbHdheXMgY29udmVydCB0byBSR0IgYmVmb3JlIHBhc3NpbmcgdG8gUHlUb3JjaC9URiBtb2RlbHMgb3IgeW91ciBjaGFubmVsIG9yZGVyIHdpbGwgYmUgd3JvbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIHVzaW5nIHRvcmNodmlzaW9uIG9yIEtlcmFzLCBpbWFnZXMgbXVzdCBiZSBpbiBSR0IgZm9ybWF0LiBBbHdheXMgdmVyaWZ5IHlvdXIgbG9hZGluZyBjb252ZW50aW9uLiBBIHF1aWNrIHNhbml0eSBjaGVjazogZGlzcGxheSBhIGtub3duIHJlZCBvYmplY3Qg4oCUIGlmIGl0IGFwcGVhcnMgYmx1ZSwgeW91ciBjaGFubmVscyBhcmUgc3dhcHBlZC4gRml4IHdpdGggY3YyLmN2dENvbG9yKGltZywgY3YyLkNPTE9SX0JHUjJSR0IpLiBQeVRvcmNoXHUwMDI3cyBUb1RlbnNvciB0cmFuc2Zvcm0gYWxzbyBub3JtYWxpemVzIHVpbnQ4IHRvIGZsb2F0MzIgaW4gWzAsIDFdIGF1dG9tYXRpY2FsbHkgd2hlbiBhcHBsaWVkIHRvIGEgUElMIGltYWdlLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IkJhdGNoZWQgSW1hZ2UgVGVuc29ycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRHVyaW5nIHRyYWluaW5nLCBpbWFnZXMgYXJlIHByb2Nlc3NlZCBpbiBtaW5pLWJhdGNoZXMgdG8gbGV2ZXJhZ2UgR1BVIHBhcmFsbGVsaXNtLiBQeVRvcmNoIGNvbGxhdGVzIGluZGl2aWR1YWwgdGVuc29ycyBvZiBzaGFwZSAoQywgSCwgVykgaW50byBhIGJhdGNoIHRlbnNvciBvZiBzaGFwZSAoQiwgQywgSCwgVykgd2hlcmUgQiBpcyB0aGUgYmF0Y2ggc2l6ZS4gQWxsIGltYWdlcyBpbiBhIGJhdGNoIG11c3QgaGF2ZSB0aGUgc2FtZSBzcGF0aWFsIGRpbWVuc2lvbnMsIHdoaWNoIGlzIHdoeSByZXNpemluZyBpcyBhIHN0YW5kYXJkIHByZXByb2Nlc3Npbmcgc3RlcCBiZWZvcmUgYmF0Y2hpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSBQSUwgaW1wb3J0IEltYWdlXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGxvYWRfdGVuc29yKHBhdGgpOlxuICAgIGltZyA9IEltYWdlLm9wZW4ocGF0aCkuY29udmVydChcdTAwMjdSR0JcdTAwMjcpLnJlc2l6ZSgoMjI0LCAyMjQpKVxuICAgIGFyciA9IG5wLmFycmF5KGltZywgZHR5cGU9bnAuZmxvYXQzMikgLyAyNTUuMFxuICAgIHJldHVybiB0b3JjaC5mcm9tX251bXB5KGFycikucGVybXV0ZSgyLCAwLCAxKSAgIyBDSFdcblxudGVuc29ycyA9IFtsb2FkX3RlbnNvcihmXHUwMDI3aW1nX3tpfS5qcGdcdTAwMjcpIGZvciBpIGluIHJhbmdlKDQpXVxuYmF0Y2ggPSB0b3JjaC5zdGFjayh0ZW5zb3JzKSAgICMgW0IsIEMsIEgsIFddXG5wcmludChcdTAwMjdCYXRjaCBzaGFwZTpcdTAwMjcsIGJhdGNoLnNoYXBlKSAgIyB0b3JjaC5TaXplKFs0LCAzLCAyMjQsIDIyNF0pIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUZW5zb3JGbG93IGFuZCBLZXJhcyB1c2UgdGhlIE5IV0MgY29udmVudGlvbiBieSBkZWZhdWx0IOKAlCBiYXRjaCBOLCBoZWlnaHQsIHdpZHRoLCBjaGFubmVscyDigJQgd2hpbGUgUHlUb3JjaCB1c2VzIE5DSFcuIFdoZW4gcG9ydGluZyBtb2RlbHMgYmV0d2VlbiBmcmFtZXdvcmtzLCByZXNoYXBpbmcgYmF0Y2ggdGVuc29ycyBpcyByZXF1aXJlZC4gdG9yY2guVGVuc29yLnBlcm11dGUoKSByZW9yZGVycyBheGVzIHdpdGhvdXQgY29weWluZyBkYXRhLiBudW1weS50cmFuc3Bvc2UoKSBkb2VzIHRoZSBzYW1lIGZvciBOdW1QeSBhcnJheXMgd2l0aG91dCBhbGxvY2F0aW5nIGFkZGl0aW9uYWwgbWVtb3J5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc2hvd190ZW5zb3IodGVuc29yKTpcbiAgICAjIHRlbnNvcjogQ0hXIGZsb2F0MzIgWzAsIDFdXG4gICAgaW1nID0gdGVuc29yLnBlcm11dGUoMSwgMiwgMCkubnVtcHkoKSAgIyBDSFcg4oaSIEhXQ1xuICAgIGltZyA9IG5wLmNsaXAoaW1nLCAwLCAxKVxuICAgIHBsdC5pbXNob3coaW1nKVxuICAgIHBsdC5heGlzKFx1MDAyN29mZlx1MDAyNylcbiAgICBwbHQuc2hvdygpXG5cbnNob3dfdGVuc29yKGJhdGNoWzBdKSAgIyBzaG93IGZpcnN0IGltYWdlIGluIGJhdGNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGRpc3BsYXlpbmcgdGVuc29ycyB3aXRoIG1hdHBsb3RsaWIsIHJldmVyc2UgdGhlIHByZXByb2Nlc3Npbmc6IG1vdmUgdGhlIGNoYW5uZWwgYXhpcyBiYWNrIHRvIEhXQyBvcmRlciBhbmQgY2xhbXAgdG8gWzAsIDFdLiBtYXRwbG90bGliXHUwMDI3cyBpbXNob3cgZXhwZWN0cyAoSCwgVywgMykgZm9yIFJHQiBvciAoSCwgVykgZm9yIGdyYXlzY2FsZS4gRm9yZ2V0dGluZyB0byBjbGFtcCBmbG9hdCB2YWx1ZXMgdG8gWzAsIDFdIGJlZm9yZSBkaXNwbGF5IGNhdXNlcyBjb2xvciBhcnRpZmFjdHMgYW5kIGluY29ycmVjdCByZW5kZXJpbmcsIGVzcGVjaWFsbHkgYWZ0ZXIgbm9ybWFsaXphdGlvbiB3aXRoIG5lZ2F0aXZlIHZhbHVlcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRm9ybWF0IiwiTGlicmFyeSIsIlNoYXBlIiwiVmFsdWUgUmFuZ2UiLCJDaGFubmVsIE9yZGVyIl0sInJvd3MiOltbIlBJTCBJbWFnZSIsIlBpbGxvdyIsIkhXQyIsIjDigJMyNTUgKHVpbnQ4KSIsIlJHQiJdLFsiT3BlbkNWIGFycmF5IiwiY3YyIiwiSFdDIiwiMOKAkzI1NSAodWludDgpIiwiQkdSIl0sWyJOdW1QeSBhcnJheSIsIm51bXB5IiwiSFdDIiwiYW55IGR0eXBlIiwiZGVwZW5kcyBvbiBzb3VyY2UiXSxbIlB5VG9yY2ggdGVuc29yIiwidG9yY2giLCJDSFciLCIwLjDigJMxLjAgKGZsb2F0MzIpIiwiUkdCIl0sWyJUZW5zb3JGbG93IHRlbnNvciIsInRmL2tlcmFzIiwiSFdDIiwiMC4w4oCTMS4wIChmbG9hdDMyKSIsIlJHQiJdXX0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWx3YXlzIHRyYWNrIHlvdXIgaW1hZ2UgZm9ybWF0OiBzaGFwZSwgZHR5cGUsIGNoYW5uZWwgb3JkZXIsIGFuZCB2YWx1ZSByYW5nZS4gVGhlIG1vc3QgY29tbW9uIGJ1Z3MgY29tZSBmcm9tIG1peGluZyBQSUwgUkdCIHdpdGggT3BlbkNWIEJHUiwgb3IgZm9yZ2V0dGluZyB0byBjb252ZXJ0IHRvIGZsb2F0MzIgYmVmb3JlIG5vcm1hbGl6aW5nLiBXcml0ZSBhIHNtYWxsIGhlbHBlciBmdW5jdGlvbiB0aGF0IHByaW50cyB0aGVzZSBwcm9wZXJ0aWVzIOKAlCBpdCB3aWxsIHNhdmUgaG91cnMgb2YgZGVidWdnaW5nIGR1cmluZyBkYXRhc2V0IHByZXByb2Nlc3NpbmcgYW5kIHBpcGVsaW5lIGludGVncmF0aW9uIHdvcmsuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQeVRvcmNoIGV4cGVjdHMgQ0hXIGZsb2F0MzIgdGVuc29ycyBpbiBbMCwgMV0gb3Igbm9ybWFsaXplZCB3aXRoIG1lYW4vc3RkLiBQSUwgdXNlcyBIV0MgdWludDguIE9wZW5DViB1c2VzIEhXQyB1aW50OCBpbiBCR1IuIEtlZXAgYSBtZW50YWwgbWFwIG9mIHdoYXQgZm9ybWF0IHlvdXIgZGF0YSBpcyBpbiBhdCBlYWNoIHN0YWdlOiBsb2FkaW5nIOKGkiBhdWdtZW50YXRpb24g4oaSIG5vcm1hbGl6YXRpb24g4oaSIGJhdGNoaW5nIOKGkiBtb2RlbCBpbnB1dC4gRXhwbGljaXQgc2hhcGUgYXNzZXJ0aW9ucyBhZnRlciBlYWNoIHN0ZXAgYXJlIGludmFsdWFibGUgZm9yIGNhdGNoaW5nIGVycm9ycyBlYXJseSBpbiB0aGUgcGlwZWxpbmUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEb2N1bWVudCBmb3JtYXQgYXNzdW1wdGlvbnMgaW4geW91ciBkYXRhIGxvYWRlciBhbmQgbW9kZWwgY29kZS4gV2hlbiBzaGFyaW5nIG1vZGVscyBvciBkYXRhc2V0cywgaW5jbHVkZSB0aGUgZXhwZWN0ZWQgaW5wdXQgZm9ybWF0IGluIHRoZSBSRUFETUUgb3IgbW9kZWwgY2FyZC4gTWFueSBzaWxlbnQgYWNjdXJhY3kgcmVncmVzc2lvbnMgaW4gcHJvZHVjdGlvbiBhcmUgY2F1c2VkIGJ5IGEgbWlzbWF0Y2ggYmV0d2VlbiB0cmFpbmluZyBhbmQgaW5mZXJlbmNlIHByZXByb2Nlc3Npbmcg4oCUIHZhbGlkYXRlIGVuZC10by1lbmQgd2l0aCBhIGtub3duIHNhbXBsZSBiZWZvcmUgZGVwbG95aW5nIGFueSB2aXNpb24gbW9kZWwuIn1d"
---
# Image Representation in Deep Learning

Digital images are multi-dimensional arrays of pixel values. In deep learning pipelines, images move through several representations: raw files on disk, PIL Image objects, NumPy arrays, and PyTorch tensors. Each format has different axis ordering, dtype, and value ranges. Understanding these conventions prevents subtle bugs in preprocessing and model inference pipelines.

A grayscale image is a 2D array of shape (H, W). A color image adds a channel dimension giving shape (H, W, C) — height, width, channels. This HWC layout is used by PIL, NumPy, and OpenCV. PyTorch uses CHW layout where channels come first. Converting between these layouts is a common source of shape mismatch errors in vision code.

```python
from PIL import Image
import numpy as np
import torch

img = Image.open('sample.jpg').convert('RGB')
arr = np.array(img)          # HWC, uint8, [0, 255]
print('NumPy HWC shape:', arr.shape)

tensor = torch.from_numpy(arr).permute(2, 0, 1)  # CHW
tensor = tensor.float() / 255.0                   # float32 [0, 1]
print('Tensor CHW shape:', tensor.shape)
```

Standard RGB images have 3 channels. Grayscale has 1. RGBA images have 4 channels including alpha transparency. The channel dimension represents spectral information at each pixel location. Channel ordering — whether RGB or BGR — determines how color information is interpreted by the model. Always verify channel order when integrating multiple libraries in one pipeline.

Images are stored in different numeric formats depending on the source. Raw pixel data from cameras is typically uint8 with values 0–255. Deep learning models expect float32 inputs normalized to [0, 1] or [-1, 1]. Converting between these ranges is a critical preprocessing step — failing to scale can cause NaN gradients or very slow convergence during training.

```python
import cv2
import numpy as np

img_bgr = cv2.imread('sample.jpg')              # HWC uint8 BGR
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)  # convert to RGB

img_float = img_rgb.astype(np.float32) / 255.0  # uint8 → float32 [0, 1]
print('float32 range:', img_float.min(), img_float.max())

img_uint8 = (img_float * 255.0).clip(0, 255).astype(np.uint8)
print('uint8 range:', img_uint8.min(), img_uint8.max())
```

Float16 is sometimes used in mixed-precision training to reduce GPU memory. Be careful when converting: dividing uint8 by 255.0 gives float64 in NumPy by default — explicitly cast to float32 to avoid doubling memory usage. PyTorch's tensor.float() converts to float32. Using .half() gives float16 for inference on supported hardware accelerators.

PIL (Pillow) and OpenCV are the two dominant image I/O libraries in Python. PIL returns images in RGB order and uses the HWC NumPy convention. OpenCV loads images as NumPy arrays in BGR order — the blue and red channels are swapped. This difference is invisible to the eye but causes model predictions to degrade when channels are mismatched at inference time.

> ****: OpenCV loads images as BGR by default — always convert to RGB before passing to PyTorch/TF models or your channel order will be wrong.

When using torchvision or Keras, images must be in RGB format. Always verify your loading convention. A quick sanity check: display a known red object — if it appears blue, your channels are swapped. Fix with cv2.cvtColor(img, cv2.COLOR_BGR2RGB). PyTorch's ToTensor transform also normalizes uint8 to float32 in [0, 1] automatically when applied to a PIL image.

During training, images are processed in mini-batches to leverage GPU parallelism. PyTorch collates individual tensors of shape (C, H, W) into a batch tensor of shape (B, C, H, W) where B is the batch size. All images in a batch must have the same spatial dimensions, which is why resizing is a standard preprocessing step before batching.

```python
import torch
from PIL import Image
import numpy as np

def load_tensor(path):
    img = Image.open(path).convert('RGB').resize((224, 224))
    arr = np.array(img, dtype=np.float32) / 255.0
    return torch.from_numpy(arr).permute(2, 0, 1)  # CHW

tensors = [load_tensor(f'img_{i}.jpg') for i in range(4)]
batch = torch.stack(tensors)   # [B, C, H, W]
print('Batch shape:', batch.shape)  # torch.Size([4, 3, 224, 224])
```

TensorFlow and Keras use the NHWC convention by default — batch N, height, width, channels — while PyTorch uses NCHW. When porting models between frameworks, reshaping batch tensors is required. torch.Tensor.permute() reorders axes without copying data. numpy.transpose() does the same for NumPy arrays without allocating additional memory.

```python
import torch
import matplotlib.pyplot as plt
import numpy as np

def show_tensor(tensor):
    # tensor: CHW float32 [0, 1]
    img = tensor.permute(1, 2, 0).numpy()  # CHW → HWC
    img = np.clip(img, 0, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

show_tensor(batch[0])  # show first image in batch
```

When displaying tensors with matplotlib, reverse the preprocessing: move the channel axis back to HWC order and clamp to [0, 1]. matplotlib's imshow expects (H, W, 3) for RGB or (H, W) for grayscale. Forgetting to clamp float values to [0, 1] before display causes color artifacts and incorrect rendering, especially after normalization with negative values.

| Format | Library | Shape | Value Range | Channel Order |
| --- | --- | --- | --- | --- |
| PIL Image | Pillow | HWC | 0–255 (uint8) | RGB |
| OpenCV array | cv2 | HWC | 0–255 (uint8) | BGR |
| NumPy array | numpy | HWC | any dtype | depends on source |
| PyTorch tensor | torch | CHW | 0.0–1.0 (float32) | RGB |
| TensorFlow tensor | tf/keras | HWC | 0.0–1.0 (float32) | RGB |

Always track your image format: shape, dtype, channel order, and value range. The most common bugs come from mixing PIL RGB with OpenCV BGR, or forgetting to convert to float32 before normalizing. Write a small helper function that prints these properties — it will save hours of debugging during dataset preprocessing and pipeline integration work.

PyTorch expects CHW float32 tensors in [0, 1] or normalized with mean/std. PIL uses HWC uint8. OpenCV uses HWC uint8 in BGR. Keep a mental map of what format your data is in at each stage: loading → augmentation → normalization → batching → model input. Explicit shape assertions after each step are invaluable for catching errors early in the pipeline.

Document format assumptions in your data loader and model code. When sharing models or datasets, include the expected input format in the README or model card. Many silent accuracy regressions in production are caused by a mismatch between training and inference preprocessing — validate end-to-end with a known sample before deploying any vision model.

