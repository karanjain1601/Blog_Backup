---
title: "Faster R-CNN: Two-Stage Object Detection"
slug: "faster-rcnn-two-stage"
description: "The Faster R-CNN architecture — Region Proposal Network (RPN), RoI Align, two-stage pipeline, and how to use torchvision's pretrained detection models."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGYXN0ZXIgUi1DTk4gaXMgdGhlIGNhbm9uaWNhbCB0d28tc3RhZ2Ugb2JqZWN0IGRldGVjdG9yLCBpbnRyb2R1Y2luZyB0aGUgUmVnaW9uIFByb3Bvc2FsIE5ldHdvcmsgKFJQTikgdG8gcmVwbGFjZSB0aGUgc2xvdyBzZWxlY3RpdmUgc2VhcmNoIGFsZ29yaXRobSB1c2VkIGluIFItQ05OIGFuZCBGYXN0IFItQ05OLiBUaGUgc2hhcmVkIGNvbnZvbHV0aW9uYWwgYmFja2JvbmUgZXh0cmFjdHMgZmVhdHVyZXMgdXNlZCBieSBib3RoIHRoZSBSUE4gYW5kIHRoZSBkZXRlY3Rpb24gaGVhZCwgZHJhbWF0aWNhbGx5IHJlZHVjaW5nIGluZmVyZW5jZSB0aW1lIGNvbXBhcmVkIHRvIHByZWRlY2Vzc29ycyB3aGlsZSBtYWludGFpbmluZyBoaWdoIGFjY3VyYWN5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHR3by1zdGFnZSBwaXBlbGluZSBzZXBhcmF0ZXMgbG9jYWxpemF0aW9uIGludG8gY29hcnNlIHJlZ2lvbiBwcm9wb3NhbCAoUlBOKSBhbmQgZmluZS1ncmFpbmVkIGNsYXNzaWZpY2F0aW9uIHBsdXMgcmVmaW5lbWVudCAoZGV0ZWN0aW9uIGhlYWQpLiBUaGlzIGRlY291cGxpbmcgbGV0cyB0aGUgbW9kZWwgZm9jdXMgY29tcHV0ZSBvbiBwcm9taXNpbmcgcmVnaW9ucyByYXRoZXIgdGhhbiBldmFsdWF0aW5nIGV2ZXJ5IHNwYXRpYWwgbG9jYXRpb24gYXQgZXZlcnkgc2NhbGUuIEZhc3RlciBSLUNOTiBhY2hpZXZlZCByb3VnaGx5IDUgRlBTIG9uIGEgR1BVIGluIDIwMTUsIHdoaWNoIHdhcyBzdGF0ZS1vZi10aGUtYXJ0IGF0IHRoZSB0aW1lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlZ2lvbiBQcm9wb3NhbCBOZXR3b3JrIChSUE4pIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgUlBOIHNsaWRlcyBhIHNtYWxsIG5ldHdvcmsgb3ZlciB0aGUgZmVhdHVyZSBtYXAsIGF0IGVhY2ggbG9jYXRpb24gY2xhc3NpZnlpbmcgYW5jaG9ycyBhcyBvYmplY3QgdnMuIGJhY2tncm91bmQgYW5kIHJlZ3Jlc3NpbmcgYm94IG9mZnNldHMuIEl0IG91dHB1dHMgb2JqZWN0bmVzcyBzY29yZXMgYW5kIGJvdW5kaW5nIGJveCBkZWx0YXMgZm9yIGVhY2ggYW5jaG9yLiBUaGUgdG9wLWsgcHJvcG9zYWxzIHJhbmtlZCBieSBvYmplY3RuZXNzIGFmdGVyIE5NUyBhcmUgcGFzc2VkIHRvIHRoZSBkZXRlY3Rpb24gaGVhZCDigJQgdHlwaWNhbGx5IDIwMDAgZHVyaW5nIHRyYWluaW5nIGFuZCAxMDAwIGF0IGluZmVyZW5jZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBSUE4gc2hhcmVzIHRoZSBiYWNrYm9uZSB3aXRoIHRoZSBkZXRlY3Rpb24gaGVhZCDigJQgdGhpcyBpcyB0aGUga2V5IGluc2lnaHQgb2YgRmFzdGVyIFItQ05OLiBCb3RoIG5ldHdvcmtzIGFyZSB0cmFpbmVkIGpvaW50bHkuIFRoZSBSUE4gbG9zcyBjb21iaW5lcyBiaW5hcnkgY3Jvc3MtZW50cm9weSBmb3Igb2JqZWN0bmVzcyBjbGFzc2lmaWNhdGlvbiBhbmQgU21vb3RoIEwxIGZvciBib3ggcmVncmVzc2lvbiwgc3VtbWVkIG92ZXIgYWxsIHBvc2l0aXZlIGFuZCBzYW1wbGVkIG5lZ2F0aXZlIGFuY2hvcnMgaW4gdGhlIG1pbmktYmF0Y2guIFBvc2l0aXZlIGFuY2hvcnMgdXNlIElvVSBcdTAwM2U9IDAuNyB3aXRoIGFueSBHVCBib3guIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFJQTihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaGFubmVscywgbnVtX2FuY2hvcnM9OSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmNvbnYgPSBubi5Db252MmQoaW5fY2hhbm5lbHMsIDI1NiwgMywgcGFkZGluZz0xKVxuICAgICAgICBzZWxmLmNscyAgPSBubi5Db252MmQoMjU2LCBudW1fYW5jaG9ycyAqIDIsIDEpXG4gICAgICAgIHNlbGYucmVnICA9IG5uLkNvbnYyZCgyNTYsIG51bV9hbmNob3JzICogNCwgMSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGZlYXQpOlxuICAgICAgICB4ID0gdG9yY2gucmVsdShzZWxmLmNvbnYoZmVhdCkpXG4gICAgICAgIGNsc19sb2dpdHMgID0gc2VsZi5jbHMoeCkgICAjIFtCLCAyKkEsIEgsIFddXG4gICAgICAgIGJib3hfZGVsdGFzID0gc2VsZi5yZWcoeCkgICAjIFtCLCA0KkEsIEgsIFddXG4gICAgICAgIHJldHVybiBjbHNfbG9naXRzLCBiYm94X2RlbHRhcyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJvSSBQb29saW5nIHZzIFJvSSBBbGlnbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUm9JIFBvb2xpbmcgZXh0cmFjdHMgZml4ZWQtc2l6ZSBmZWF0dXJlIG1hcHMgZnJvbSB2YXJpYWJsZS1zaXplIHByb3Bvc2FscyBieSBxdWFudGl6aW5nIHByb3Bvc2FsIGJvdW5kYXJpZXMgdG8gdGhlIG5lYXJlc3QgZmVhdHVyZSBtYXAgY2VsbC4gVGhpcyBkb3VibGUgcXVhbnRpemF0aW9uIOKAlCBvbmNlIHdoZW4gcHJvamVjdGluZyB0aGUgcHJvcG9zYWwgdG8gdGhlIGZlYXR1cmUgbWFwLCBhZ2FpbiB3aGVuIGRpdmlkaW5nIGludG8gZ3JpZCBjZWxscyDigJQgaW50cm9kdWNlcyBtaXNhbGlnbm1lbnQgZXJyb3JzIHRoYXQgaHVydCBhY2N1cmFjeSBvbiB0YXNrcyByZXF1aXJpbmcgcHJlY2lzZSBsb2NhbGl6YXRpb24gbGlrZSBpbnN0YW5jZSBzZWdtZW50YXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSb0kgQWxpZ24gZWxpbWluYXRlcyBxdWFudGl6YXRpb24gYnkgdXNpbmcgYmlsaW5lYXIgaW50ZXJwb2xhdGlvbiB0byBzYW1wbGUgZXhhY3RseSBhdCBmcmFjdGlvbmFsIGZlYXR1cmUgbWFwIGNvb3JkaW5hdGVzLiBFYWNoIGdyaWQgY2VsbCBzYW1wbGVzIDQgcG9pbnRzIHVzaW5nIGJpbGluZWFyIHdlaWdodHMuIFRoaXMgcHJlc2VydmVzIHNwYXRpYWwgYWxpZ25tZW50IGJldHdlZW4gaW5wdXQgaW1hZ2UgcmVnaW9ucyBhbmQgZXh0cmFjdGVkIGZlYXR1cmVzLCB3aGljaCBpcyBjcml0aWNhbCBmb3IgaW5zdGFuY2Ugc2VnbWVudGF0aW9uIGFuZCBhbHNvIG1lYXN1cmFibHkgaW1wcm92ZXMgYm94IGRldGVjdGlvbiBtQVAgaW4gcHJhY3RpY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaHZpc2lvbi5vcHMgaW1wb3J0IHJvaV9hbGlnblxuXG4jIGZlYXR1cmVzOiBbQiwgQywgSCwgV107IHByb3Bvc2FsczogW0ssIDVdIChiYXRjaF9pZHgsIHgxLCB5MSwgeDIsIHkyKVxuZmVhdHVyZXMgPSB0b3JjaC5yYW5kbigyLCAyNTYsIDMyLCAzMilcbnByb3Bvc2FscyA9IHRvcmNoLnRlbnNvcihbXG4gICAgWzAsIDEwLjAsIDIwLjAsIDUwLjAsIDgwLjBdLFxuICAgIFsxLCAgNS4wLCAgNS4wLCA2MC4wLCA2MC4wXVxuXSlcblxuIyBzcGF0aWFsX3NjYWxlIG1hcHMgaW1hZ2UgY29vcmRzIHRvIGZlYXR1cmUgbWFwIGNvb3JkcyAoMS9zdHJpZGUpXG5wb29sZWQgPSByb2lfYWxpZ24oZmVhdHVyZXMsIHByb3Bvc2Fscywgb3V0cHV0X3NpemU9KDcsIDcpLFxuICAgICAgICAgICAgICAgICAgIHNwYXRpYWxfc2NhbGU9MS4wLzMyLCBzYW1wbGluZ19yYXRpbz0yKVxucHJpbnQocG9vbGVkLnNoYXBlKSAgIyBbMiwgMjU2LCA3LCA3XSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsImNvbnRlbnQiOiJSb0kgQWxpZ24gZml4ZWQgdGhlIHF1YW50aXphdGlvbiBlcnJvciBpbiBSb0kgUG9vbGluZyBieSB1c2luZyBiaWxpbmVhciBpbnRlcnBvbGF0aW9uIOKAlCB0aGlzIGltcHJvdmVkIE1hc2sgUi1DTk5cdTAwMjdzIGluc3RhbmNlIHNlZ21lbnRhdGlvbiBxdWFsaXR5IHNpZ25pZmljYW50bHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHdvLVN0YWdlIERldGVjdGlvbiBIZWFkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2Vjb25kIHN0YWdlIHRha2VzIFJvSS1hbGlnbmVkIGZlYXR1cmVzIG9mIHNoYXBlIFtLLCBDLCA3LCA3XSBmb3IgdGhlIHRvcC1LIHByb3Bvc2FscywgZmxhdHRlbnMgdGhlbSwgYW5kIHBhc3NlcyB0aGVtIHRocm91Z2ggdHdvIGZ1bGx5IGNvbm5lY3RlZCBsYXllcnMuIFRoZSBvdXRwdXQgYnJhbmNoZXMgaW50byBhIGNsYXNzaWZpY2F0aW9uIGhlYWQgKEsrMSBzb2Z0bWF4IG92ZXIgb2JqZWN0IGNsYXNzZXMgcGx1cyBiYWNrZ3JvdW5kKSBhbmQgYSByZWdyZXNzaW9uIGhlYWQgKDQgdGltZXMgSyBib3ggb2Zmc2V0cyBmb3IgY2xhc3Mtc3BlY2lmaWMgcmVmaW5lbWVudCBvZiB0aGUgY29hcnNlIFJQTiBwcm9wb3NhbHMpLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2FzY2FkZSBSLUNOTiBleHRlbmRzIHRoaXMgaWRlYSBieSBzdGFja2luZyBtdWx0aXBsZSBkZXRlY3Rpb24gaGVhZHMgd2l0aCBwcm9ncmVzc2l2ZWx5IGhpZ2hlciBJb1UgdGhyZXNob2xkcyAoMC41LCAwLjYsIDAuNykuIEVhY2ggc3RhZ2UgcmVmaW5lcyB0aGUgcHJvcG9zYWxzIGZyb20gdGhlIHByZXZpb3VzIHN0YWdlLiBUaGlzIGltcHJvdmVzIHByZWNpc2lvbiBhdCBoaWdoIElvVSB0aHJlc2hvbGRzIHdpdGhvdXQgc2FjcmlmaWNpbmcgcmVjYWxsLCBvdXRwZXJmb3JtaW5nIHN0YW5kYXJkIEZhc3RlciBSLUNOTiBvbiBDT0NPIGVzcGVjaWFsbHkgYXQgc3RyaWN0IElvVSB0aHJlc2hvbGRzIGxpa2UgQVA3NS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgRGV0ZWN0aW9uSGVhZChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9kaW0sIG51bV9jbGFzc2VzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZmMxID0gbm4uTGluZWFyKGluX2RpbSwgMTAyNClcbiAgICAgICAgc2VsZi5mYzIgPSBubi5MaW5lYXIoMTAyNCwgMTAyNClcbiAgICAgICAgc2VsZi5jbHNfc2NvcmUgPSBubi5MaW5lYXIoMTAyNCwgbnVtX2NsYXNzZXMgKyAxKVxuICAgICAgICBzZWxmLmJib3hfcHJlZCA9IG5uLkxpbmVhcigxMDI0LCBudW1fY2xhc3NlcyAqIDQpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCByb2lfZmVhdHMpOlxuICAgICAgICB4ID0gdG9yY2gucmVsdShzZWxmLmZjMShyb2lfZmVhdHMuZmxhdHRlbigxKSkpXG4gICAgICAgIHggPSB0b3JjaC5yZWx1KHNlbGYuZmMyKHgpKVxuICAgICAgICByZXR1cm4gc2VsZi5jbHNfc2NvcmUoeCksIHNlbGYuYmJveF9wcmVkKHgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhaW5pbmcgdGhlIEZ1bGwgUGlwZWxpbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZhc3RlciBSLUNOTiBpcyB0cmFpbmVkIGVuZC10by1lbmQgYnkgc3VtbWluZyBmb3VyIGxvc3NlczogUlBOIGNsYXNzaWZpY2F0aW9uIChvYmplY3RuZXNzKSwgUlBOIHJlZ3Jlc3Npb24gKGJveCBvZmZzZXRzKSwgZGV0ZWN0aW9uIGhlYWQgY2xhc3NpZmljYXRpb24gKGNsYXNzIHNjb3JlcyksIGFuZCBkZXRlY3Rpb24gaGVhZCByZWdyZXNzaW9uIChyZWZpbmVkIGJveCBvZmZzZXRzKS4gVGhlIGJhY2tib25lIGFuZCBSUE4gc2hhcmUgZ3JhZGllbnRzIGZyb20gYm90aCBzdGFnZXMuIFB5VG9yY2hcdTAwMjdzIHRvcmNodmlzaW9uIGltcGxlbWVudGF0aW9uIGhhbmRsZXMgdGhpcyB3aXRoIGEgR2VuZXJhbGl6ZWRSQ05OIHdyYXBwZXIgY2xhc3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNaW5pLWJhdGNoIGNvbnN0cnVjdGlvbiBzYW1wbGVzIDI1NiBhbmNob3JzIGZvciB0aGUgUlBOIHN0YWdlICh1cCB0byAxMjggcG9zaXRpdmUpIGFuZCA1MTIgUm9JcyBmb3IgdGhlIGRldGVjdGlvbiBzdGFnZSAodXAgdG8gMjUlIHBvc2l0aXZlKS4gRHVyaW5nIHRyYWluaW5nLCBncm91bmQtdHJ1dGggYm94ZXMgYXJlIGFkZGVkIHRvIHRoZSBSb0kgcG9vbCB0byBlbnN1cmUgdGhlIGRldGVjdGlvbiBoZWFkIGFsd2F5cyBzZWVzIHBvc2l0aXZlIGV4YW1wbGVzIGV2ZW4gaWYgdGhlIFJQTiBtaXNzZXMgc29tZSBvYmplY3RzIGVhcmx5IGluIHRyYWluaW5nIOKAlCBhIHRlY2huaXF1ZSBjYWxsZWQgR1QgYm94IHNhbXBsaW5nLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGF0YSBhdWdtZW50YXRpb24gZm9yIGRldGVjdGlvbiBpbmNsdWRlcyBob3Jpem9udGFsIGZsaXBwaW5nLCByYW5kb20gY3JvcHBpbmcsIG11bHRpLXNjYWxlIHRyYWluaW5nLCBhbmQgY29sb3Igaml0dGVyLiBUaGUgYmFja2JvbmUgaXMgdHlwaWNhbGx5IGluaXRpYWxpemVkIGZyb20gSW1hZ2VOZXQgcHJlLXRyYWluZWQgd2VpZ2h0cywgYW5kIHRoZSBsZWFybmluZyByYXRlIGZvciB0aGUgYmFja2JvbmUgaXMgb2Z0ZW4gc2V0IGxvd2VyIHRoYW4gZGV0ZWN0aW9uLXNwZWNpZmljIGxheWVycyB0byBwcmV2ZW50IGRlc3Ryb3lpbmcgbGVhcm5lZCByZXByZXNlbnRhdGlvbnMgZHVyaW5nIHRoZSBlYXJseSBzdGFnZXMgb2YgZmluZS10dW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmFzdGVyIFItQ05OIGVzdGFibGlzaGVkIHRoZSB0ZW1wbGF0ZSB0aGF0IG1vc3Qgc3Vic2VxdWVudCB0d28tc3RhZ2UgZGV0ZWN0b3JzIGZvbGxvdzogc2hhcmVkIGJhY2tib25lIHBsdXMgcHJvcG9zYWwgbmV0d29yayBwbHVzIFJvSSBmZWF0dXJlIGV4dHJhY3Rpb24gcGx1cyBjbGFzc2lmaWNhdGlvbiBhbmQgcmVncmVzc2lvbiBoZWFkLiBVbmRlcnN0YW5kaW5nIHRoaXMgYXJjaGl0ZWN0dXJlIGNsYXJpZmllcyB0aGUgZGVzaWduIGNob2ljZXMgaW4gbGF0ZXIgbW9kZWxzIGxpa2UgTWFzayBSLUNOTiwgQ2FzY2FkZSBSLUNOTiwgYW5kIFNwYXJzZSBSLUNOTiwgd2hpY2ggYWxsIGJ1aWxkIG9uIHRoZSBzYW1lIGZ1bmRhbWVudGFsIHN0cnVjdHVyZS4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJQcm9wb3NhbCBNZXRob2QiLCJTcGVlZCAoRlBTKSIsIm1BUCAoVk9DL0NPQ08pIiwiWWVhciJdLCJyb3dzIjpbWyJSLUNOTiIsIlNlbGVjdGl2ZSBTZWFyY2giLCJ+MC4wMiIsIjU4LjUgKFZPQykiLCIyMDE0Il0sWyJGYXN0IFItQ05OIiwiU2VsZWN0aXZlIFNlYXJjaCIsIn4yIiwiNzAuMCAoVk9DKSIsIjIwMTUiXSxbIkZhc3RlciBSLUNOTiIsIlJQTiIsIn41IiwiNzMuMiAoVk9DKSIsIjIwMTUiXSxbIkNhc2NhZGUgUi1DTk4iLCJSUE4gKGNhc2NhZGVkKSIsIn43IiwiNDIuOCAoQ09DTykiLCIyMDE4Il0sWyJTcGFyc2UgUi1DTk4iLCJMZWFybmVkIHF1ZXJpZXMiLCJ+MjIiLCI0NS4wIChDT0NPKSIsIjIwMjEiXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdG9yY2h2aXNpb24ubW9kZWxzLmRldGVjdGlvbiBpbXBvcnQgZmFzdGVycmNubl9yZXNuZXQ1MF9mcG5cbmZyb20gdG9yY2h2aXNpb24udHJhbnNmb3Jtcy5mdW5jdGlvbmFsIGltcG9ydCB0b190ZW5zb3JcbmZyb20gUElMIGltcG9ydCBJbWFnZVxuXG5tb2RlbCA9IGZhc3RlcnJjbm5fcmVzbmV0NTBfZnBuKHByZXRyYWluZWQ9VHJ1ZSlcbm1vZGVsLmV2YWwoKVxuXG5pbWcgPSB0b190ZW5zb3IoSW1hZ2Uub3BlbihcdTAwMjdpbWFnZS5qcGdcdTAwMjcpKSAgIyBbMywgSCwgV10gZmxvYXQzMlxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgcHJlZHMgPSBtb2RlbChbaW1nXSlbMF1cblxucHJpbnQocHJlZHNbXHUwMDI3Ym94ZXNcdTAwMjddLnNoYXBlKSAgICMgW04sIDRdIHh5eHlcbnByaW50KHByZWRzW1x1MDAyN2xhYmVsc1x1MDAyN10uc2hhcGUpICAjIFtOXVxucHJpbnQocHJlZHNbXHUwMDI3c2NvcmVzXHUwMDI3XS5zaGFwZSkgICMgW05dIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZmluZS10dW5pbmcgb24gYSBjdXN0b20gZGF0YXNldCwgcmVwbGFjZSB0aGUgY2xhc3NpZmljYXRpb24gYW5kIHJlZ3Jlc3Npb24gaGVhZHMgYnkgc3BlY2lmeWluZyBudW1fY2xhc3NlcyBpbiB0aGUgdG9yY2h2aXNpb24gY29uc3RydWN0b3IuIEtlZXAgdGhlIGJhY2tib25lIGFuZCBGUE4gZnJvemVuIGZvciB0aGUgZmlyc3QgZmV3IGVwb2NocyB0byBzdGFiaWxpemUgdHJhaW5pbmcsIHRoZW4gdW5mcmVlemUgZm9yIGVuZC10by1lbmQgZmluZS10dW5pbmcuIFVzZSBhIGJhdGNoIHNpemUgb2YgMS0yIGltYWdlcyB3aXRoIG11bHRpcGxlIGNyb3BzIHBlciBpbWFnZSB0byBtYWludGFpbiBlZmZlY3RpdmUgbWluaS1iYXRjaCBkaXZlcnNpdHkuIn1d"
---
# Faster R-CNN: Two-Stage Object Detection

## Overview

Faster R-CNN is the canonical two-stage object detector, introducing the Region Proposal Network (RPN) to replace the slow selective search algorithm used in R-CNN and Fast R-CNN. The shared convolutional backbone extracts features used by both the RPN and the detection head, dramatically reducing inference time compared to predecessors while maintaining high accuracy.

The two-stage pipeline separates localization into coarse region proposal (RPN) and fine-grained classification plus refinement (detection head). This decoupling lets the model focus compute on promising regions rather than evaluating every spatial location at every scale. Faster R-CNN achieved roughly 5 FPS on a GPU in 2015, which was state-of-the-art at the time.

## Region Proposal Network (RPN)

The RPN slides a small network over the feature map, at each location classifying anchors as object vs. background and regressing box offsets. It outputs objectness scores and bounding box deltas for each anchor. The top-k proposals ranked by objectness after NMS are passed to the detection head — typically 2000 during training and 1000 at inference.

The RPN shares the backbone with the detection head — this is the key insight of Faster R-CNN. Both networks are trained jointly. The RPN loss combines binary cross-entropy for objectness classification and Smooth L1 for box regression, summed over all positive and sampled negative anchors in the mini-batch. Positive anchors use IoU >= 0.7 with any GT box.

```python
import torch
import torch.nn as nn

class RPN(nn.Module):
    def __init__(self, in_channels, num_anchors=9):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, 256, 3, padding=1)
        self.cls  = nn.Conv2d(256, num_anchors * 2, 1)
        self.reg  = nn.Conv2d(256, num_anchors * 4, 1)

    def forward(self, feat):
        x = torch.relu(self.conv(feat))
        cls_logits  = self.cls(x)   # [B, 2*A, H, W]
        bbox_deltas = self.reg(x)   # [B, 4*A, H, W]
        return cls_logits, bbox_deltas
```

## RoI Pooling vs RoI Align

RoI Pooling extracts fixed-size feature maps from variable-size proposals by quantizing proposal boundaries to the nearest feature map cell. This double quantization — once when projecting the proposal to the feature map, again when dividing into grid cells — introduces misalignment errors that hurt accuracy on tasks requiring precise localization like instance segmentation.

RoI Align eliminates quantization by using bilinear interpolation to sample exactly at fractional feature map coordinates. Each grid cell samples 4 points using bilinear weights. This preserves spatial alignment between input image regions and extracted features, which is critical for instance segmentation and also measurably improves box detection mAP in practice.

```python
import torch
from torchvision.ops import roi_align

# features: [B, C, H, W]; proposals: [K, 5] (batch_idx, x1, y1, x2, y2)
features = torch.randn(2, 256, 32, 32)
proposals = torch.tensor([
    [0, 10.0, 20.0, 50.0, 80.0],
    [1,  5.0,  5.0, 60.0, 60.0]
])

# spatial_scale maps image coords to feature map coords (1/stride)
pooled = roi_align(features, proposals, output_size=(7, 7),
                   spatial_scale=1.0/32, sampling_ratio=2)
print(pooled.shape)  # [2, 256, 7, 7]
```

> **info**: RoI Align fixed the quantization error in RoI Pooling by using bilinear interpolation — this improved Mask R-CNN's instance segmentation quality significantly.

## Two-Stage Detection Head

The second stage takes RoI-aligned features of shape [K, C, 7, 7] for the top-K proposals, flattens them, and passes them through two fully connected layers. The output branches into a classification head (K+1 softmax over object classes plus background) and a regression head (4 times K box offsets for class-specific refinement of the coarse RPN proposals).

Cascade R-CNN extends this idea by stacking multiple detection heads with progressively higher IoU thresholds (0.5, 0.6, 0.7). Each stage refines the proposals from the previous stage. This improves precision at high IoU thresholds without sacrificing recall, outperforming standard Faster R-CNN on COCO especially at strict IoU thresholds like AP75.

```python
import torch
import torch.nn as nn

class DetectionHead(nn.Module):
    def __init__(self, in_dim, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(in_dim, 1024)
        self.fc2 = nn.Linear(1024, 1024)
        self.cls_score = nn.Linear(1024, num_classes + 1)
        self.bbox_pred = nn.Linear(1024, num_classes * 4)

    def forward(self, roi_feats):
        x = torch.relu(self.fc1(roi_feats.flatten(1)))
        x = torch.relu(self.fc2(x))
        return self.cls_score(x), self.bbox_pred(x)
```

## Training the Full Pipeline

Faster R-CNN is trained end-to-end by summing four losses: RPN classification (objectness), RPN regression (box offsets), detection head classification (class scores), and detection head regression (refined box offsets). The backbone and RPN share gradients from both stages. PyTorch's torchvision implementation handles this with a GeneralizedRCNN wrapper class.

Mini-batch construction samples 256 anchors for the RPN stage (up to 128 positive) and 512 RoIs for the detection stage (up to 25% positive). During training, ground-truth boxes are added to the RoI pool to ensure the detection head always sees positive examples even if the RPN misses some objects early in training — a technique called GT box sampling.

Data augmentation for detection includes horizontal flipping, random cropping, multi-scale training, and color jitter. The backbone is typically initialized from ImageNet pre-trained weights, and the learning rate for the backbone is often set lower than detection-specific layers to prevent destroying learned representations during the early stages of fine-tuning.

## Key Takeaways

Faster R-CNN established the template that most subsequent two-stage detectors follow: shared backbone plus proposal network plus RoI feature extraction plus classification and regression head. Understanding this architecture clarifies the design choices in later models like Mask R-CNN, Cascade R-CNN, and Sparse R-CNN, which all build on the same fundamental structure.

| Model | Proposal Method | Speed (FPS) | mAP (VOC/COCO) | Year |
| --- | --- | --- | --- | --- |
| R-CNN | Selective Search | ~0.02 | 58.5 (VOC) | 2014 |
| Fast R-CNN | Selective Search | ~2 | 70.0 (VOC) | 2015 |
| Faster R-CNN | RPN | ~5 | 73.2 (VOC) | 2015 |
| Cascade R-CNN | RPN (cascaded) | ~7 | 42.8 (COCO) | 2018 |
| Sparse R-CNN | Learned queries | ~22 | 45.0 (COCO) | 2021 |

```python
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms.functional import to_tensor
from PIL import Image

model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

img = to_tensor(Image.open('image.jpg'))  # [3, H, W] float32
with torch.no_grad():
    preds = model([img])[0]

print(preds['boxes'].shape)   # [N, 4] xyxy
print(preds['labels'].shape)  # [N]
print(preds['scores'].shape)  # [N]
```

For fine-tuning on a custom dataset, replace the classification and regression heads by specifying num_classes in the torchvision constructor. Keep the backbone and FPN frozen for the first few epochs to stabilize training, then unfreeze for end-to-end fine-tuning. Use a batch size of 1-2 images with multiple crops per image to maintain effective mini-batch diversity.

