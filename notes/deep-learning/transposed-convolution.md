---
title: "Transposed Convolution — Upsampling and Checkerboard Artifacts"
slug: "transposed-convolution"
description: "Understand transposed convolution as learnable upsampling, diagnose and fix checkerboard artifacts, and compare pixel shuffle and bilinear resize alternatives."
tags: ["deep-learning", "cnns"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW5jb2Rlci1kZWNvZGVyIGFyY2hpdGVjdHVyZXMg4oCUIFUtTmV0IGZvciBzZWdtZW50YXRpb24sIERDR0FOIGFuZCBTdHlsZUdBTiBnZW5lcmF0b3JzLCBzdXBlci1yZXNvbHV0aW9uIG5ldHdvcmtzIOKAlCBuZWVkIHRvIGluY3JlYXNlIHNwYXRpYWwgcmVzb2x1dGlvbiBpbiB0aGUgZGVjb2Rlci4gVHJhbnNwb3NlZCBjb252b2x1dGlvbiAoYWxzbyBjYWxsZWQgZGVjb252b2x1dGlvbiBvciBmcmFjdGlvbmFsbHktc3RyaWRlZCBjb252b2x1dGlvbikgaXMgdGhlIGxlYXJuYWJsZSBhbHRlcm5hdGl2ZSB0byBmaXhlZCB1cHNhbXBsaW5nIGxpa2UgYmlsaW5lYXIgb3IgbmVhcmVzdC1uZWlnaGJvdXIgaW50ZXJwb2xhdGlvbi4gSG93ZXZlciwgdHJhbnNwb3NlZCBjb252IGlzIG5vdG9yaW91cyBmb3IgcHJvZHVjaW5nIGNoZWNrZXJib2FyZCBhcnRpZmFjdHMg4oCUIHBlcmlvZGljIGFtcGxpdHVkZSBwYXR0ZXJucyBjYXVzZWQgYnkgdW5ldmVuIGtlcm5lbCBvdmVybGFwLiBVbmRlcnN0YW5kaW5nIHdoeSB0aGlzIGhhcHBlbnMgYW5kIGhvdyB0byBhdm9pZCBpdCBpcyBlc3NlbnRpYWwgZm9yIGFueW9uZSBidWlsZGluZyBnZW5lcmF0aXZlIG9yIGRlbnNlLXByZWRpY3Rpb24gbW9kZWxzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYW5zcG9zZWQgQ29udm9sdXRpb24gTWVjaGFuaWNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHRyYW5zcG9zZWQgY29udiB3aXRoIHN0cmlkZSBzIGluc2VydHMgcy0xIHplcm9zIGJldHdlZW4gZWFjaCBpbnB1dCBlbGVtZW50IGFsb25nIGVhY2ggc3BhdGlhbCBheGlzLCB0aGVuIGFwcGxpZXMgYSBzdGFuZGFyZCBjb252b2x1dGlvbi4gVGhpcyBpcyB0aGUgdHJhbnNwb3NlIG9mIHRoZSBmb3J3YXJkIGNvbnZvbHV0aW9uIG9wZXJhdG9yIGluIGl0cyBtYXRyaXggZm9ybS4gSWYgZm9yd2FyZCBjb252IGlzIHkgPSBDeCwgdHJhbnNwb3NlZCBjb252IGNvbXB1dGVzIHjMgiA9IEPhtYB5LiBUaGUgb3V0cHV0IHNpemUgaXM6IEhfb3V0ID0gKEhfaW4gLSAxKcK3cyAtIDJwICsgay4gRm9yIEhfaW49NCwgaz00LCBzPTIsIHA9MTogSF9vdXQgPSAoNC0xKcK3MiAtIDIgKyA0ID0gOCDigJQgZXhhY3RseSBkb3VibGluZy4gVGhpcyBpcyB0aGUgc3RhbmRhcmQgY29uZmlndXJhdGlvbiBpbiBEQ0dBTiBhbmQgVS1OZXQgZGVjb2RlcnMuIFRoZSBsZWFybmFibGUgd2VpZ2h0cyBnaXZlIHRoZSBuZXR3b3JrIGZyZWVkb20gdG8gbGVhcm4gdGhlIGJlc3QgdXBzYW1wbGluZyBmaWx0ZXIgZm9yIHRoZSB0YXNrLCB1bmxpa2UgZml4ZWQgYmlsaW5lYXIgaW50ZXJwb2xhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiB0cmFuc3Bvc2VkX2NvbnYxZF9zY3JhdGNoKHgsIGtlcm5lbCwgc3RyaWRlPTIpOlxuICAgIFwiXCJcIjFEIHRyYW5zcG9zZWQgY29udjogaW5zZXJ0IHplcm9zIHRoZW4gY29udm9sdmUgKG5vIHBhZGRpbmcpLlwiXCJcIlxuICAgICMgU3RlcCAxOiBpbnNlcnQgKHN0cmlkZS0xKSB6ZXJvcyBiZXR3ZWVuIGVsZW1lbnRzXG4gICAgeF91cCA9IG5wLnplcm9zKCh4LnNoYXBlWzBdIC0gMSkgKiBzdHJpZGUgKyB4LnNoYXBlWzBdIC1cbiAgICAgICAgICAgICAgICAgICAgKHguc2hhcGVbMF0gLSAxKSAqIChzdHJpZGUgLSAxKSlcbiAgICAjIFNpbXBsZXI6IHVzZSBucCByZXBlYXQgdHJpY2tcbiAgICBleHBhbmRlZCA9IG5wLnplcm9zKCh4LnNoYXBlWzBdIC0gMSkgKiBzdHJpZGUgKyAxKVxuICAgIGV4cGFuZGVkWzo6c3RyaWRlXSA9IHhcbiAgICAjIFN0ZXAgMjogY29udm9sdmUgKGNyb3NzLWNvcnJlbGF0ZSkgd2l0aCBrZXJuZWwgKG5vIGZsaXAgZm9yIENOTilcbiAgICBrID0gbGVuKGtlcm5lbClcbiAgICBvdXRfbGVuID0gbGVuKGV4cGFuZGVkKSArIGsgLSAxXG4gICAgb3V0cHV0ID0gbnAuemVyb3Mob3V0X2xlbilcbiAgICBmb3IgaSBpbiByYW5nZShsZW4oZXhwYW5kZWQpKTpcbiAgICAgICAgb3V0cHV0W2k6aStrXSArPSBleHBhbmRlZFtpXSAqIGtlcm5lbFxuICAgIHJldHVybiBvdXRwdXRcblxueCA9IG5wLmFycmF5KFsxLjAsIDIuMCwgMy4wLCA0LjBdKVxua2VybmVsID0gbnAuYXJyYXkoWzEuMCwgMi4wLCAxLjBdKVxub3V0ID0gdHJhbnNwb3NlZF9jb252MWRfc2NyYXRjaCh4LCBrZXJuZWwsIHN0cmlkZT0yKVxucHJpbnQoZlx1MDAyN0lucHV0IGxlbmd0aDogIHtsZW4oeCl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0tlcm5lbCBsZW5ndGg6IHtsZW4oa2VybmVsKX1cdTAwMjcpXG5wcmludChmXHUwMDI3T3V0cHV0IGxlbmd0aDoge2xlbihvdXQpfSAgKGV4cGVjdGVkOiAoNC0xKSoyKzEgKyAzLTEgPSA5KVx1MDAyNylcbnByaW50KGZcdTAwMjdPdXRwdXQgdmFsdWVzOiB7b3V0fVx1MDAyNylcbnByaW50KFx1MDAyN1plcm8gaW5zZXJ0aW9uIGRvdWJsZXMgc3BhY2luZzsga2VybmVsIGJsZW5kcyBhZGphY2VudCBlbGVtZW50cy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hlY2tlcmJvYXJkIEFydGlmYWN0cyBhbmQgVGhlaXIgQ2F1c2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNoZWNrZXJib2FyZCBhcnRpZmFjdHMgYXJpc2Ugd2hlbiBrZXJuZWxfc2l6ZSBpcyBub3QgZGl2aXNpYmxlIGJ5IHN0cmlkZS4gV2l0aCBrPTMsIHM9Mjogc29tZSBvdXRwdXQgcGl4ZWxzIHJlY2VpdmUgY29udHJpYnV0aW9ucyBmcm9tIDIgaW5wdXQgcGl4ZWxzIHdoaWxlIG90aGVycyByZWNlaXZlIGZyb20gb25seSAxIOKAlCBhIHN5c3RlbWF0aWMgYW1wbGl0dWRlIGltYmFsYW5jZSB0aGF0IHJlcGVhdHMgd2l0aCBwZXJpb2Qgcy4gVGhlIHJlc3VsdCBpcyBhIHNwYXRpYWxseSBwZXJpb2RpYyBpbnRlbnNpdHkgcGF0dGVybiB2aXNpYmxlIGluIEdBTi1nZW5lcmF0ZWQgaW1hZ2VzIGFuZCBzZWdtZW50YXRpb24gbWFza3MuIE9kZW5hIGV0IGFsLiAoMjAxNikgZG9jdW1lbnRlZCB0aGlzIGluIFx1MDAyN0RlY29udm9sdXRpb24gYW5kIENoZWNrZXJib2FyZCBBcnRpZmFjdHNcdTAwMjcgYW5kIHNob3dlZCB0aGF0IGFueSBrIG5vdCBkaXZpc2libGUgYnkgcyBwcm9kdWNlcyBvdmVybGFwIGltYmFsYW5jZS4gT2RkIGs9NCB3aXRoIHM9MiBpcyBkaXZpc2libGU7IGs9MyB3aXRoIHM9MiBpcyBub3QuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG92ZXJsYXBfcGF0dGVybihrLCBzLCBzaXplPTgpOlxuICAgIFwiXCJcIkNvdW50IGhvdyBtYW55IGlucHV0IHBpeGVscyBjb250cmlidXRlIHRvIGVhY2ggb3V0cHV0IHBvc2l0aW9uLlwiXCJcIlxuICAgICMgVXNlIGEgb25lcyBpbnB1dCB0byBjb3VudCBvdmVybGFwc1xuICAgIHggPSB0b3JjaC5vbmVzKDEsIDEsIHNpemUsIHNpemUpXG4gICAgY29udl90ID0gbm4uQ29udlRyYW5zcG9zZTJkKDEsIDEsIGssIHN0cmlkZT1zLCBwYWRkaW5nPTAsIGJpYXM9RmFsc2UpXG4gICAgbm4uaW5pdC5vbmVzXyhjb252X3Qud2VpZ2h0KVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBvdXQgPSBjb252X3QoeClcbiAgICByZXR1cm4gb3V0WzAsIDBdLm51bXB5KClcblxucHJpbnQoXHUwMDI3T3ZlcmxhcCBjb3VudHMg4oCUIGs9NCBzPTIgKGRpdmlzaWJsZSwgdW5pZm9ybSk6XHUwMDI3KVxub3cgPSBvdmVybGFwX3BhdHRlcm4oNCwgMiwgc2l6ZT00KVxucHJpbnQob3dbOjgsIDo4XS5hc3R5cGUoaW50KSlcblxucHJpbnQoXHUwMDI3XFxuT3ZlcmxhcCBjb3VudHMg4oCUIGs9MyBzPTIgKE5PVCBkaXZpc2libGUsIGNoZWNrZXJib2FyZCk6XHUwMDI3KVxub3cgPSBvdmVybGFwX3BhdHRlcm4oMywgMiwgc2l6ZT00KVxucHJpbnQob3dbOjgsIDo4XS5hc3R5cGUoaW50KSlcblxucHJpbnQoXHUwMDI3XFxuRml4OiByZXNpemUgdGhlbiBjb252IChubyB0cmFuc3Bvc2VkIGNvbnYgYXQgYWxsKTpcdTAwMjcpXG5kZWYgdXBzYW1wbGVfcmVzaXplX2NvbnYoeF9pbiwgQ19pbiwgQ19vdXQpOlxuICAgIHhfdXAgPSBGLmludGVycG9sYXRlKHhfaW4sIHNjYWxlX2ZhY3Rvcj0yLCBtb2RlPVx1MDAyN2JpbGluZWFyXHUwMDI3LCBhbGlnbl9jb3JuZXJzPUZhbHNlKVxuICAgIGNvbnYgPSBubi5Db252MmQoQ19pbiwgQ19vdXQsIDMsIHBhZGRpbmc9MSlcbiAgICByZXR1cm4gY29udih4X3VwKVxuXG5wcmludChcdTAwMjdCaWxpbmVhciArIGNvbnYgPSB1bmlmb3JtIG92ZXJsYXAgYnkgY29uc3RydWN0aW9uLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVLU5ldCBEZWNvZGVyIOKAlCBUcmFuc3Bvc2VkIENvbnYgdnMgQmlsaW5lYXIrQ29udiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG9yaWdpbmFsIFUtTmV0IHVzZWQgdHJhbnNwb3NlZCBjb252IGluIHRoZSBkZWNvZGVyLiBNb2Rlcm4gc2VnbWVudGF0aW9uIG1vZGVscyBvZnRlbiByZXBsYWNlIGl0IHdpdGggYmlsaW5lYXIgdXBzYW1wbGluZyBmb2xsb3dlZCBieSBhIDPDlzMgY29udiwgd2hpY2ggYXZvaWRzIGNoZWNrZXJib2FyZCBhcnRpZmFjdHMgd2l0aCBtaW5pbWFsIGFjY3VyYWN5IGxvc3MuIFRoZSB0cmFkZW9mZjogdHJhbnNwb3NlZCBjb252IGlzIGZ1bGx5IGxlYXJuYWJsZSAoY2FuIGxlYXJuIG5vbi1zeW1tZXRyaWMgdXBzYW1wbGluZyksIHdoaWxlIGJpbGluZWFyK2NvbnYgZml4ZXMgdGhlIHVwc2FtcGxpbmcgdG8gYmlsaW5lYXIgYnV0IGxldHMgdGhlIGNvbnYgcmVmaW5lIGZlYXR1cmVzLiBGb3IgdGFza3Mgd2hlcmUgZmluZS1ncmFpbmVkIGRldGFpbCBtYXR0ZXJzIChlLmcuLCBjZWxsIGJvdW5kYXJ5IHNlZ21lbnRhdGlvbiksIHRyYW5zcG9zZWQgY29udiB3aXRoIGNhcmVmdWwgaW5pdGlhbGlzYXRpb24gKGJpbGluZWFyIGluaXQpIGNhbiBvdXRwZXJmb3JtIGZpeGVkIGJpbGluZWFyIHVwc2FtcGxpbmcuIEluIHByYWN0aWNlLCB0aGUgY2hvaWNlIGlzIG9mdGVuIGhhcmR3YXJlLWFuZC1sYXRlbmN5LWRyaXZlbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgVU5ldERlY29kZXIobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJDb21wYXJlIHRyYW5zcG9zZWQgY29udiB2cyBiaWxpbmVhcitjb252IGRlY29kZXIgYmxvY2tzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBDX2luLCBDX291dCwgbW9kZT1cdTAwMjd0cmFuc3Bvc2VcdTAwMjcpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5tb2RlID0gbW9kZVxuICAgICAgICBpZiBtb2RlID09IFx1MDAyN3RyYW5zcG9zZVx1MDAyNzpcbiAgICAgICAgICAgIHNlbGYudXAgPSBubi5Db252VHJhbnNwb3NlMmQoQ19pbiwgQ19vdXQsIGtlcm5lbF9zaXplPTIsIHN0cmlkZT0yKVxuICAgICAgICBlbHNlOiAgIyBiaWxpbmVhciArIGNvbnZcbiAgICAgICAgICAgIHNlbGYudXAgICA9IG5uLlVwc2FtcGxlKHNjYWxlX2ZhY3Rvcj0yLCBtb2RlPVx1MDAyN2JpbGluZWFyXHUwMDI3LCBhbGlnbl9jb3JuZXJzPUZhbHNlKVxuICAgICAgICAgICAgc2VsZi5jb252ID0gbm4uQ29udjJkKENfaW4sIENfb3V0LCAzLCBwYWRkaW5nPTEpXG4gICAgICAgIHNlbGYucmVmaW5lID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChDX291dCAqIDIsIENfb3V0LCAzLCBwYWRkaW5nPTEpLCAgIyBhZnRlciBza2lwIGNvbmNhdFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQoQ19vdXQpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcbiAgICAgICAgKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgc2tpcCk6XG4gICAgICAgIHggPSBzZWxmLnVwKHgpIGlmIHNlbGYubW9kZSA9PSBcdTAwMjd0cmFuc3Bvc2VcdTAwMjcgZWxzZSBzZWxmLmNvbnYoc2VsZi51cCh4KSlcbiAgICAgICAgeCA9IHRvcmNoLmNhdChbeCwgc2tpcF0sIGRpbT0xKVxuICAgICAgICByZXR1cm4gc2VsZi5yZWZpbmUoeClcblxuZm9yIG1vZGUgaW4gW1x1MDAyN3RyYW5zcG9zZVx1MDAyNywgXHUwMDI3YmlsaW5lYXJcdTAwMjddOlxuICAgIGRlYyA9IFVOZXREZWNvZGVyKDI1NiwgMTI4LCBtb2RlPW1vZGUpXG4gICAgeCA9IHRvcmNoLnJhbmRuKDIsIDI1NiwgMTQsIDE0KVxuICAgIHNraXAgPSB0b3JjaC5yYW5kbigyLCAxMjgsIDI4LCAyOClcbiAgICBvdXQgPSBkZWMoeCwgc2tpcClcbiAgICBwID0gc3VtKHEubnVtZWwoKSBmb3IgcSBpbiBkZWMucGFyYW1ldGVycygpKVxuICAgIHByaW50KGZcdTAwMjd7bW9kZTpcdTAwM2MxMn06IG91dHB1dD17dHVwbGUob3V0LnNoYXBlKX0sIHBhcmFtcz17cDosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQaXhlbCBTaHVmZmxlIOKAlCBTdWItUGl4ZWwgQ29udm9sdXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBpeGVsIHNodWZmbGUgKHN1Yi1waXhlbCBjb252b2x1dGlvbiwgU2hpIGV0IGFsLiAyMDE2KSBpcyBhbiBlbGVnYW50IGFsdGVybmF0aXZlIGZvciBzdXBlci1yZXNvbHV0aW9uLiBJbnN0ZWFkIG9mIGluc2VydGluZyB6ZXJvcyBhbmQgZmlsdGVyaW5nLCBpdCBhcHBsaWVzIGEgc3RhbmRhcmQgY29udiBpbiB0aGUgbG93LXJlc29sdXRpb24gc3BhY2UgdG8gcHJvZHVjZSBDw5dywrLDl0jDl1cgZmVhdHVyZXMsIHRoZW4gcmVhcnJhbmdlcyAoc2h1ZmZsZXMpIHRoZSBywrIgY2hhbm5lbHMgaW50byBhIHNwYXRpYWwgcsOXciBncmlkOiBvdXRwdXQgaXMgQ8OXKEjCt3Ipw5coV8K3cikuIFRoZSBjb21wdXRhdGlvbiBoYXBwZW5zIGVudGlyZWx5IGF0IGxvdyByZXNvbHV0aW9uIOKAlCBmYXIgY2hlYXBlciB0aGFuIG9wZXJhdGluZyBhdCBoaWdoIHJlc29sdXRpb24g4oCUIGFuZCB0aGUgdXBzYW1wbGluZyBpcyBmdWxseSBsZWFybmVkLiBFU1BDTiB1c2VkIHRoaXMgZm9yIHJlYWwtdGltZSB2aWRlbyBzdXBlci1yZXNvbHV0aW9uLiBUaGUga2V5IHByb3BlcnR5OiBubyBjaGVja2VyYm9hcmQgYXJ0aWZhY3RzIHdoZW4gdGhlIHByZWNlZGluZyBjb252IGlzIGluaXRpYWxpc2VkIGNvcnJlY3RseSAoSUNOUiBpbml0aWFsaXNhdGlvbikuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFBpeGVsU2h1ZmZsZVVwc2FtcGxlKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU3ViLXBpeGVsIGNvbnZvbHV0aW9uIGZvciAyeCB1cHNhbXBsaW5nLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBDX2luLCBDX291dCwgc2NhbGVfZmFjdG9yPTIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgIyBDb252IHByb2R1Y2VzIENfb3V0ICogcl4yIGNoYW5uZWxzIGF0IGxvdyByZXNvbHV0aW9uXG4gICAgICAgIHNlbGYuY29udiA9IG5uLkNvbnYyZChDX2luLCBDX291dCAqIHNjYWxlX2ZhY3RvcioqMiwga2VybmVsX3NpemU9MywgcGFkZGluZz0xKVxuICAgICAgICBzZWxmLnBzICAgPSBubi5QaXhlbFNodWZmbGUoc2NhbGVfZmFjdG9yKSAgIyByZWFycmFuZ2VzIHRvIHNwYXRpYWxcbiAgICAgICAgc2VsZi5faW5pdF93ZWlnaHRzKENfb3V0LCBzY2FsZV9mYWN0b3IpXG5cbiAgICBkZWYgX2luaXRfd2VpZ2h0cyhzZWxmLCBDX291dCwgcik6XG4gICAgICAgIFwiXCJcIklDTlIgaW5pdDogdGlsZSBDX291dCBmaWx0ZXJzIHRvIGF2b2lkIGNoZWNrZXJib2FyZCBhdCBpbml0LlwiXCJcIlxuICAgICAgICBrZXJuZWwgPSBzZWxmLmNvbnYud2VpZ2h0LmRhdGEuY2xvbmUoKVs6Q19vdXRdXG4gICAgICAgIGZvciBpIGluIHJhbmdlKHIgKiByKTpcbiAgICAgICAgICAgIHNlbGYuY29udi53ZWlnaHQuZGF0YVtpKkNfb3V0OihpKzEpKkNfb3V0XSA9IGtlcm5lbFxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLnBzKHNlbGYuY29udih4KSlcblxuIyBDb21wYXJlIHRyYW5zcG9zZWQgY29udiB2cyBwaXhlbCBzaHVmZmxlXG5DX2luLCBDX291dCwgciA9IDY0LCAzMiwgMlxudHJhbnNwID0gbm4uQ29udlRyYW5zcG9zZTJkKENfaW4sIENfb3V0LCBrZXJuZWxfc2l6ZT0yLCBzdHJpZGU9MiwgYmlhcz1GYWxzZSlcbnBpeHNodSA9IFBpeGVsU2h1ZmZsZVVwc2FtcGxlKENfaW4sIENfb3V0LCBzY2FsZV9mYWN0b3I9cilcblxueCA9IHRvcmNoLnJhbmRuKDIsIENfaW4sIDE0LCAxNClcbnByaW50KGZcdTAwMjdUcmFuc3Bvc2VkIGNvbnYgb3V0cHV0OiB7dHVwbGUodHJhbnNwKHgpLnNoYXBlKX1cdTAwMjcpXG5wcmludChmXHUwMDI3UGl4ZWwgc2h1ZmZsZSBvdXRwdXQ6ICAge3R1cGxlKHBpeHNodSh4KS5zaGFwZSl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1RyYW5zcG9zZWQgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiB0cmFuc3AucGFyYW1ldGVycygpKTosfVx1MDAyNylcbnByaW50KGZcdTAwMjdQaXhlbFNodWZmbGUgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBwaXhzaHUucGFyYW1ldGVycygpKTosfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkFsd2F5cyBDaGVjayBLZXJuZWwgRGl2aXNpYmlsaXR5IiwiY29udGVudCI6IlRoZSBzaW5nbGUgbW9zdCBjb21tb24gY2F1c2Ugb2YgY2hlY2tlcmJvYXJkIGFydGlmYWN0cyBpbiBHQU4gZ2VuZXJhdG9ycyBpcyB1c2luZyBrZXJuZWxfc2l6ZT0zIHdpdGggc3RyaWRlPTIgaW4gQ29udlRyYW5zcG9zZTJkLiBUaGUgZml4IGlzIGVpdGhlcjogKDEpIHVzZSBrZXJuZWxfc2l6ZT00IHdpdGggc3RyaWRlPTIgKGRpdmlzaWJsZSksICgyKSByZXBsYWNlIHdpdGggVXBzYW1wbGUoc2NhbGVfZmFjdG9yPTIpICsgQ29udjJkKDN4MyksIG9yICgzKSB1c2UgUGl4ZWxTaHVmZmxlLiBJZiB5b3VyIEdBTiBvdXRwdXRzIGhhdmUgYSBmYWludCBncmlkIHBhdHRlcm4sIHRoaXMgaXMgYWxtb3N0IGNlcnRhaW5seSB0aGUgY3VscHJpdC4gQ2hlY2sgZXZlcnkgQ29udlRyYW5zcG9zZTJkIGluIHlvdXIgZGVjb2RlcjogaXMgayAlIHMgPT0gMD8ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVcHNhbXBsaW5nIE1ldGhvZHMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWFjaCB1cHNhbXBsaW5nIG1ldGhvZCBjYXJyaWVzIGRpZmZlcmVudCB0cmFkZW9mZnMgaW4gbGVhcm5hYmlsaXR5LCBhcnRpZmFjdCByaXNrLCBtZW1vcnksIGFuZCBjb21wdXRhdGlvbmFsIGNvc3QuIE5lYXJlc3QtbmVpZ2hib3VyIGlzIGZhc3Rlc3QgYnV0IHByb2R1Y2VzIGJsb2NreSBvdXRwdXRzIHdpdGggc2hhcnAgdHJhbnNpdGlvbnMuIEJpbGluZWFyIGlzIHNtb290aGVyIGJ1dCBhbHNvIGZpeGVkLiBUcmFuc3Bvc2VkIGNvbnYgaXMgZnVsbHkgbGVhcm5hYmxlIGJ1dCBhcnRpZmFjdC1wcm9uZS4gUGl4ZWwgc2h1ZmZsZSBsZWFybnMgdXBzYW1wbGluZyBhdCBsb3cgcmVzb2x1dGlvbiDigJQgdGhlIG1vc3QgY29tcHV0ZS1lZmZpY2llbnQgbGVhcm5hYmxlIG9wdGlvbi4gSW4gcHJhY3RpY2UsIHNlZ21lbnRhdGlvbiBtb2RlbHMgKGxpa2UgRGVlcExhYlYzKykgdXNlIGJpbGluZWFyIHVwc2FtcGxpbmcgdGhyb3VnaG91dCB0aGUgZGVjb2RlciBmb3Igc2ltcGxpY2l0eSwgd2hpbGUgc3VwZXItcmVzb2x1dGlvbiBtb2RlbHMgZXhjbHVzaXZlbHkgdXNlIHBpeGVsIHNodWZmbGUuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkxlYXJuYWJsZSIsIkNoZWNrZXJib2FyZCBSaXNrIiwiTWVtb3J5IFVzZSIsIk1haW4gVXNlIENhc2UiLCJBcnRpZmFjdCBGaXgiXSwicm93cyI6W1siTmVhcmVzdCBuZWlnaGJvdXIiLCJObyIsIk5vbmUiLCJMb3ciLCJTaW1wbGUgYmFzZWxpbmVzLCBxdWljayBwcm90b3R5cGluZyIsIk4vQSJdLFsiQmlsaW5lYXIgdXBzYW1wbGUiLCJObyIsIk5vbmUiLCJMb3ciLCJTZWdtZW50YXRpb24gZGVjb2RlcnMgKERlZXBMYWIpIiwiTi9BIl0sWyJUcmFuc3Bvc2VkIGNvbnYiLCJZZXMiLCJIaWdoIChpZiBrJXPiiaAwKSIsIk1lZGl1bSIsIlUtTmV0LCBEQ0dBTiwgVkFFIGRlY29kZXJzIiwiVXNlIGslcz09MCBvciBzd2l0Y2ggbWV0aG9kIl0sWyJCaWxpbmVhciArIENvbnYiLCJQYXJ0aWFsIChjb252KSIsIk5vbmUiLCJNZWRpdW0iLCJNb2Rlcm4gc2VnbWVudGF0aW9uIGRlY29kZXJzIiwiTi9BIOKAlCBpbmhlcmVudGx5IHNhZmUiXSxbIlBpeGVsIFNodWZmbGUiLCJZZXMiLCJMb3cgKHdpdGggSUNOUiBpbml0KSIsIkxvdyAod29ya3MgYXQgTFIpIiwiU3VwZXItcmVzb2x1dGlvbiAoRVNQQ04sIEVTUkdBTikiLCJJQ05SIGluaXRpYWxpc2F0aW9uIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIm91dHB1dF9wYWRkaW5nIGluIENvbnZUcmFuc3Bvc2UyZCBhZGRzIGV4dHJhIHJvd3MvY29scyB0byByZXNvbHZlIGFtYmlndWl0eSB3aGVuIHN0cmlkZSBcdTAwM2UgMS4iLCJJQ05SIChJbml0aWFsaXNhdGlvbiB2aWEgQ29udm9sdXRpb25hbCBOZXVyYWwgbmV0d29yayBSZWFycmFuZ2VtZW50KSBpbml0IGZvciBwaXhlbCBzaHVmZmxlIGF2b2lkcyBlYXJseS10cmFpbmluZyBjaGVja2VyYm9hcmQuIiwiUHJvZ3Jlc3NpdmUgZ3Jvd2luZyBHQU5zIChQcm9HQU4pIGFkZCB0cmFuc3Bvc2VkIGNvbnYgbGF5ZXJzIGdyYWR1YWxseSBkdXJpbmcgdHJhaW5pbmcgdG8gc3RhYmlsaXNlLiIsIkluIHNlZ21lbnRhdGlvbiwgQVNQUCAoQXRyb3VzIFNwYXRpYWwgUHlyYW1pZCBQb29saW5nKSBhdm9pZHMgdHJhbnNwb3NlZCBjb252IGVudGlyZWx5IGJ5IHVzaW5nIGRpbGF0ZWQgY29udnMuIiwibm4uVXBzYW1wbGUgd2l0aCBhbGlnbl9jb3JuZXJzPVRydWUgdnMgRmFsc2UgZ2l2ZXMgZGlmZmVyZW50IHJlc3VsdHMg4oCUIEZhbHNlIGlzIHJlY29tbWVuZGVkIGZvciBtb3N0IHRhc2tzLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgRGVjb2RlciBEZXNpZ24gUGF0dGVybnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vZGVybiBlbmNvZGVyLWRlY29kZXIgYXJjaGl0ZWN0dXJlcyBoYXZlIGNvbnZlcmdlZCBvbiBhIGZldyByZWxpYWJsZSBkZWNvZGVyIHBhdHRlcm5zLiBGUE4gKEZlYXR1cmUgUHlyYW1pZCBOZXR3b3JrKSB1c2VzIHRvcC1kb3duIGxhdGVyYWwgY29ubmVjdGlvbnMgd2l0aCBuZWFyZXN0LW5laWdoYm91ciB1cHNhbXBsaW5nICsgMcOXMSBjb252IGZvciBjaGFubmVsIG1hdGNoaW5nLCB0aGVuIDPDlzMgY29udiBmb3Igc21vb3RoaW5nLiBUaGlzIGF2b2lkcyB0cmFuc3Bvc2VkIGNvbnYgZW50aXJlbHkgYW5kIGlzIHJvYnVzdCB0byBjaGVja2VyYm9hcmQgYXJ0aWZhY3RzLiBVLU5ldCB2YXJpYW50cyBmb3IgbWVkaWNhbCBpbWFnaW5nIG9mdGVuIGtlZXAgdHJhbnNwb3NlZCBjb252IGJlY2F1c2UgaGlnaC1mcmVxdWVuY3kgZGV0YWlsIHByZXNlcnZhdGlvbiBpcyBjcml0aWNhbCBhbmQgYXJ0aWZhY3QtZnJlZSBiaWxpbmVhciB1cHNhbXBsaW5nIGRpc2NhcmRzIHNvbWUgbGVhcm5lZCBzaGFycG5lc3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgR0FOIGdlbmVyYXRvcnMsIHRoZSBjb21tdW5pdHkgaGFzIGxhcmdlbHkgbW92ZWQgYXdheSBmcm9tIHRyYW5zcG9zZWQgY29udiBpbiBmYXZvdXIgb2YgcmVzaXplK2NvbnYgKFN0eWxlR0FOMiB1c2VzIG1vZHVsYXRlZCBjb252KSBvciBwaXhlbCBzaHVmZmxlIChFU1JHQU4pLiBUaGUgY2hlY2tlcmJvYXJkIGFydGlmYWN0IGlzIHBhcnRpY3VsYXJseSB2aXNpYmxlIGluIEdBTiBvdXRwdXRzIGJlY2F1c2UgdGhlIGRpc2NyaW1pbmF0b3IgaXMgc3BlY2lmaWNhbGx5IHRyYWluZWQgdG8gZGlzdGluZ3Vpc2ggcmVhbCBmcm9tIGdlbmVyYXRlZCBpbWFnZXMg4oCUIGFueSBzeXN0ZW1hdGljIHBhdHRlcm4gaXMgaW1tZWRpYXRlbHkgcGVuYWxpc2VkLiBTdGFibGUgRGlmZnVzaW9uXHUwMDI3cyBWQUUgZGVjb2RlciB1c2VzIG5lYXJlc3QtbmVpZ2hib3VyIHVwc2FtcGxpbmcgZm9sbG93ZWQgYnkgUmVzTmV0IGJsb2NrcywgYXZvaWRpbmcgdHJhbnNwb3NlZCBjb252IGNvbXBsZXRlbHkuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTZWdGb3JtZXIgZGVjb2Rlcjogc2ltcGxlIE1MUCArIGJpbGluZWFyIHVwc2FtcGxlIOKAlCBubyB0cmFuc3Bvc2VkIGNvbnYsIHN0YXRlLW9mLXRoZS1hcnQgc2VnbWVudGF0aW9uLiIsIkVTUkdBTiBnZW5lcmF0b3I6IHBpeGVsIHNodWZmbGUgKFJSREIgYmxvY2tzKSBmb3Igc3VwZXItcmVzb2x1dGlvbiB3aXRoIG5vIGNoZWNrZXJib2FyZCBhcnRpZmFjdHMuIiwib3V0cHV0X3BhZGRpbmcgcGFyYW1ldGVyIGluIENvbnZUcmFuc3Bvc2UyZCBpcyBuZWVkZWQgd2hlbiBpbnB1dCBzaXplIGlzIGFtYmlndW91cyBnaXZlbiBzdHJpZGUuIiwiQ29udlRyYW5zcG9zZTFkIGFuZCBDb252VHJhbnNwb3NlM2QgZm9sbG93IHRoZSBzYW1lIG1lY2hhbmljcyDigJQgc2FtZSBjaGVja2VyYm9hcmQgcmlzayBhcHBsaWVzLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Transposed Convolution — Upsampling and Checkerboard Artifacts

Encoder-decoder architectures — U-Net for segmentation, DCGAN and StyleGAN generators, super-resolution networks — need to increase spatial resolution in the decoder. Transposed convolution (also called deconvolution or fractionally-strided convolution) is the learnable alternative to fixed upsampling like bilinear or nearest-neighbour interpolation. However, transposed conv is notorious for producing checkerboard artifacts — periodic amplitude patterns caused by uneven kernel overlap. Understanding why this happens and how to avoid it is essential for anyone building generative or dense-prediction models.

## Transposed Convolution Mechanics

A transposed conv with stride s inserts s-1 zeros between each input element along each spatial axis, then applies a standard convolution. This is the transpose of the forward convolution operator in its matrix form. If forward conv is y = Cx, transposed conv computes x̂ = Cᵀy. The output size is: H_out = (H_in - 1)·s - 2p + k. For H_in=4, k=4, s=2, p=1: H_out = (4-1)·2 - 2 + 4 = 8 — exactly doubling. This is the standard configuration in DCGAN and U-Net decoders. The learnable weights give the network freedom to learn the best upsampling filter for the task, unlike fixed bilinear interpolation.

```python
import numpy as np

def transposed_conv1d_scratch(x, kernel, stride=2):
    """1D transposed conv: insert zeros then convolve (no padding)."""
    # Step 1: insert (stride-1) zeros between elements
    x_up = np.zeros((x.shape[0] - 1) * stride + x.shape[0] -
                    (x.shape[0] - 1) * (stride - 1))
    # Simpler: use np repeat trick
    expanded = np.zeros((x.shape[0] - 1) * stride + 1)
    expanded[::stride] = x
    # Step 2: convolve (cross-correlate) with kernel (no flip for CNN)
    k = len(kernel)
    out_len = len(expanded) + k - 1
    output = np.zeros(out_len)
    for i in range(len(expanded)):
        output[i:i+k] += expanded[i] * kernel
    return output

x = np.array([1.0, 2.0, 3.0, 4.0])
kernel = np.array([1.0, 2.0, 1.0])
out = transposed_conv1d_scratch(x, kernel, stride=2)
print(f'Input length:  {len(x)}')
print(f'Kernel length: {len(kernel)}')
print(f'Output length: {len(out)}  (expected: (4-1)*2+1 + 3-1 = 9)')
print(f'Output values: {out}')
print('Zero insertion doubles spacing; kernel blends adjacent elements.')
```

## Checkerboard Artifacts and Their Cause

Checkerboard artifacts arise when kernel_size is not divisible by stride. With k=3, s=2: some output pixels receive contributions from 2 input pixels while others receive from only 1 — a systematic amplitude imbalance that repeats with period s. The result is a spatially periodic intensity pattern visible in GAN-generated images and segmentation masks. Odena et al. (2016) documented this in 'Deconvolution and Checkerboard Artifacts' and showed that any k not divisible by s produces overlap imbalance. Odd k=4 with s=2 is divisible; k=3 with s=2 is not.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

def overlap_pattern(k, s, size=8):
    """Count how many input pixels contribute to each output position."""
    # Use a ones input to count overlaps
    x = torch.ones(1, 1, size, size)
    conv_t = nn.ConvTranspose2d(1, 1, k, stride=s, padding=0, bias=False)
    nn.init.ones_(conv_t.weight)
    with torch.no_grad():
        out = conv_t(x)
    return out[0, 0].numpy()

print('Overlap counts — k=4 s=2 (divisible, uniform):')
ow = overlap_pattern(4, 2, size=4)
print(ow[:8, :8].astype(int))

print('\nOverlap counts — k=3 s=2 (NOT divisible, checkerboard):')
ow = overlap_pattern(3, 2, size=4)
print(ow[:8, :8].astype(int))

print('\nFix: resize then conv (no transposed conv at all):')
def upsample_resize_conv(x_in, C_in, C_out):
    x_up = F.interpolate(x_in, scale_factor=2, mode='bilinear', align_corners=False)
    conv = nn.Conv2d(C_in, C_out, 3, padding=1)
    return conv(x_up)

print('Bilinear + conv = uniform overlap by construction.')
```

## U-Net Decoder — Transposed Conv vs Bilinear+Conv

The original U-Net used transposed conv in the decoder. Modern segmentation models often replace it with bilinear upsampling followed by a 3×3 conv, which avoids checkerboard artifacts with minimal accuracy loss. The tradeoff: transposed conv is fully learnable (can learn non-symmetric upsampling), while bilinear+conv fixes the upsampling to bilinear but lets the conv refine features. For tasks where fine-grained detail matters (e.g., cell boundary segmentation), transposed conv with careful initialisation (bilinear init) can outperform fixed bilinear upsampling. In practice, the choice is often hardware-and-latency-driven.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class UNetDecoder(nn.Module):
    """Compare transposed conv vs bilinear+conv decoder blocks."""
    def __init__(self, C_in, C_out, mode='transpose'):
        super().__init__()
        self.mode = mode
        if mode == 'transpose':
            self.up = nn.ConvTranspose2d(C_in, C_out, kernel_size=2, stride=2)
        else:  # bilinear + conv
            self.up   = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False)
            self.conv = nn.Conv2d(C_in, C_out, 3, padding=1)
        self.refine = nn.Sequential(
            nn.Conv2d(C_out * 2, C_out, 3, padding=1),  # after skip concat
            nn.BatchNorm2d(C_out), nn.ReLU(inplace=True)
        )

    def forward(self, x, skip):
        x = self.up(x) if self.mode == 'transpose' else self.conv(self.up(x))
        x = torch.cat([x, skip], dim=1)
        return self.refine(x)

for mode in ['transpose', 'bilinear']:
    dec = UNetDecoder(256, 128, mode=mode)
    x = torch.randn(2, 256, 14, 14)
    skip = torch.randn(2, 128, 28, 28)
    out = dec(x, skip)
    p = sum(q.numel() for q in dec.parameters())
    print(f'{mode:<12}: output={tuple(out.shape)}, params={p:,}')
```

## Pixel Shuffle — Sub-Pixel Convolution

Pixel shuffle (sub-pixel convolution, Shi et al. 2016) is an elegant alternative for super-resolution. Instead of inserting zeros and filtering, it applies a standard conv in the low-resolution space to produce C×r²×H×W features, then rearranges (shuffles) the r² channels into a spatial r×r grid: output is C×(H·r)×(W·r). The computation happens entirely at low resolution — far cheaper than operating at high resolution — and the upsampling is fully learned. ESPCN used this for real-time video super-resolution. The key property: no checkerboard artifacts when the preceding conv is initialised correctly (ICNR initialisation).

```python
import torch
import torch.nn as nn

class PixelShuffleUpsample(nn.Module):
    """Sub-pixel convolution for 2x upsampling."""
    def __init__(self, C_in, C_out, scale_factor=2):
        super().__init__()
        # Conv produces C_out * r^2 channels at low resolution
        self.conv = nn.Conv2d(C_in, C_out * scale_factor**2, kernel_size=3, padding=1)
        self.ps   = nn.PixelShuffle(scale_factor)  # rearranges to spatial
        self._init_weights(C_out, scale_factor)

    def _init_weights(self, C_out, r):
        """ICNR init: tile C_out filters to avoid checkerboard at init."""
        kernel = self.conv.weight.data.clone()[:C_out]
        for i in range(r * r):
            self.conv.weight.data[i*C_out:(i+1)*C_out] = kernel

    def forward(self, x):
        return self.ps(self.conv(x))

# Compare transposed conv vs pixel shuffle
C_in, C_out, r = 64, 32, 2
transp = nn.ConvTranspose2d(C_in, C_out, kernel_size=2, stride=2, bias=False)
pixshu = PixelShuffleUpsample(C_in, C_out, scale_factor=r)

x = torch.randn(2, C_in, 14, 14)
print(f'Transposed conv output: {tuple(transp(x).shape)}')
print(f'Pixel shuffle output:   {tuple(pixshu(x).shape)}')
print(f'Transposed params: {sum(p.numel() for p in transp.parameters()):,}')
print(f'PixelShuffle params: {sum(p.numel() for p in pixshu.parameters()):,}')
```

> **Always Check Kernel Divisibility**: The single most common cause of checkerboard artifacts in GAN generators is using kernel_size=3 with stride=2 in ConvTranspose2d. The fix is either: (1) use kernel_size=4 with stride=2 (divisible), (2) replace with Upsample(scale_factor=2) + Conv2d(3x3), or (3) use PixelShuffle. If your GAN outputs have a faint grid pattern, this is almost certainly the culprit. Check every ConvTranspose2d in your decoder: is k % s == 0?

## Upsampling Methods Comparison

Each upsampling method carries different tradeoffs in learnability, artifact risk, memory, and computational cost. Nearest-neighbour is fastest but produces blocky outputs with sharp transitions. Bilinear is smoother but also fixed. Transposed conv is fully learnable but artifact-prone. Pixel shuffle learns upsampling at low resolution — the most compute-efficient learnable option. In practice, segmentation models (like DeepLabV3+) use bilinear upsampling throughout the decoder for simplicity, while super-resolution models exclusively use pixel shuffle.

| Method | Learnable | Checkerboard Risk | Memory Use | Main Use Case | Artifact Fix |
| --- | --- | --- | --- | --- | --- |
| Nearest neighbour | No | None | Low | Simple baselines, quick prototyping | N/A |
| Bilinear upsample | No | None | Low | Segmentation decoders (DeepLab) | N/A |
| Transposed conv | Yes | High (if k%s≠0) | Medium | U-Net, DCGAN, VAE decoders | Use k%s==0 or switch method |
| Bilinear + Conv | Partial (conv) | None | Medium | Modern segmentation decoders | N/A — inherently safe |
| Pixel Shuffle | Yes | Low (with ICNR init) | Low (works at LR) | Super-resolution (ESPCN, ESRGAN) | ICNR initialisation |

- output_padding in ConvTranspose2d adds extra rows/cols to resolve ambiguity when stride > 1.
- ICNR (Initialisation via Convolutional Neural network Rearrangement) init for pixel shuffle avoids early-training checkerboard.
- Progressive growing GANs (ProGAN) add transposed conv layers gradually during training to stabilise.
- In segmentation, ASPP (Atrous Spatial Pyramid Pooling) avoids transposed conv entirely by using dilated convs.
- nn.Upsample with align_corners=True vs False gives different results — False is recommended for most tasks.

## Practical Decoder Design Patterns

Modern encoder-decoder architectures have converged on a few reliable decoder patterns. FPN (Feature Pyramid Network) uses top-down lateral connections with nearest-neighbour upsampling + 1×1 conv for channel matching, then 3×3 conv for smoothing. This avoids transposed conv entirely and is robust to checkerboard artifacts. U-Net variants for medical imaging often keep transposed conv because high-frequency detail preservation is critical and artifact-free bilinear upsampling discards some learned sharpness.

For GAN generators, the community has largely moved away from transposed conv in favour of resize+conv (StyleGAN2 uses modulated conv) or pixel shuffle (ESRGAN). The checkerboard artifact is particularly visible in GAN outputs because the discriminator is specifically trained to distinguish real from generated images — any systematic pattern is immediately penalised. Stable Diffusion's VAE decoder uses nearest-neighbour upsampling followed by ResNet blocks, avoiding transposed conv completely.

- SegFormer decoder: simple MLP + bilinear upsample — no transposed conv, state-of-the-art segmentation.
- ESRGAN generator: pixel shuffle (RRDB blocks) for super-resolution with no checkerboard artifacts.
- output_padding parameter in ConvTranspose2d is needed when input size is ambiguous given stride.
- ConvTranspose1d and ConvTranspose3d follow the same mechanics — same checkerboard risk applies.

---

