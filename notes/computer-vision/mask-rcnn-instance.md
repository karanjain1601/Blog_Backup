---
title: "Mask R-CNN: Instance Segmentation"
slug: "mask-rcnn-instance"
description: "Mask R-CNN extends Faster R-CNN with a parallel mask prediction head — RoI Align, FCN-based mask branch, multi-task training loss, and applications to COCO instance segmentation."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNYXNrIFItQ05OIGV4dGVuZHMgRmFzdGVyIFItQ05OIGJ5IGFkZGluZyBhIHRoaXJkIHBhcmFsbGVsIGJyYW5jaCB0aGF0IHByZWRpY3RzIGEgc2VnbWVudGF0aW9uIG1hc2sgZm9yIGVhY2ggZGV0ZWN0ZWQgb2JqZWN0LiBUaGUgbW9kZWwgdXNlcyBhIFJlc05ldC1GUE4gYmFja2JvbmUgZm9yIG11bHRpLXNjYWxlIGZlYXR1cmVzLCBhIFJlZ2lvbiBQcm9wb3NhbCBOZXR3b3JrIGZvciBjYW5kaWRhdGUgYm94ZXMsIGFuZCBzZXBhcmF0ZSBoZWFkcyBmb3IgY2xhc3MgcHJlZGljdGlvbiwgYm91bmRpbmcgYm94IHJlZ3Jlc3Npb24sIGFuZCBiaW5hcnkgbWFzayBvdXRwdXQuIEl0IGFjaGlldmVzIHN0YXRlLW9mLXRoZS1hcnQgaW5zdGFuY2Ugc2VnbWVudGF0aW9uIG9uIENPQ08gd2l0aCBwcmFjdGljYWwgaW5mZXJlbmNlIHNwZWVkLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsImNvbnRlbnQiOiJNYXNrIFItQ05OIHByZWRpY3RzIG1hc2tzIGluZGVwZW5kZW50bHkgcGVyIGNsYXNzIOKAlCBpdCBkb2VzIE5PVCB1c2UgdGhlIHByZWRpY3RlZCBjbGFzcyB0byBwaWNrIHRoZSBtYXNrIGF0IHRyYWluaW5nIHRpbWUuIFRoaXMgYXZvaWRzIGNvbXBldGl0aW9uIGJldHdlZW4gY2xhc3NlcyBpbiB0aGUgbWFzayBoZWFkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJvSSBBbGlnbiBmb3IgUHJlY2lzZSBBbGlnbm1lbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJvSSBQb29saW5nIHF1YW50aXplcyByZWdpb24gY29vcmRpbmF0ZXMgdG8gaW50ZWdlcnMsIGNyZWF0aW5nIHNwYXRpYWwgbWlzYWxpZ25tZW50IHRoYXQgZGVncmFkZXMgbWFzayBhY2N1cmFjeS4gUm9JIEFsaWduIHJlbW92ZXMgcXVhbnRpemF0aW9uIGJ5IHNhbXBsaW5nIGZlYXR1cmVzIGF0IGV4YWN0IGZsb2F0aW5nLXBvaW50IHBvc2l0aW9ucyB1c2luZyBiaWxpbmVhciBpbnRlcnBvbGF0aW9uLiBBIGZpeGVkIHNhbXBsaW5nIGdyaWQgcGVyIG91dHB1dCBjZWxsIGlzIGNvbXB1dGVkIGZyb20gdGhlIGZlYXR1cmUgbWFwIHdpdGhvdXQgcm91bmRpbmcsIHByZXNlcnZpbmcgc3BhdGlhbCBhY2N1cmFjeSB0aGF0IGlzIGVzc2VudGlhbCBmb3IgdGhlIGRvd25zdHJlYW0gMjh4MjggbWFzayBicmFuY2guIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNodmlzaW9uLm9wcyBhcyBvcHNcblxuZGVmIGRlbW9fcm9pX2FsaWduKGZlYXR1cmVfbWFwLCBib3hlcyk6XG4gICAgXCJcIlwiUm9JIEFsaWduOiBiaWxpbmVhciBzYW1wbGluZyBhdCBleGFjdCBjb29yZHMsIG5vIHF1YW50aXphdGlvbiBlcnJvci5cIlwiXCJcbiAgICAjIGZlYXR1cmVfbWFwOiBbQiwgQywgSCwgV107IGJveGVzOiBbTiwgNV0gKGJhdGNoX2lkeCwgeDEsIHkxLCB4MiwgeTIpXG4gICAgYWxpZ25lZCA9IG9wcy5yb2lfYWxpZ24oXG4gICAgICAgIGZlYXR1cmVfbWFwLFxuICAgICAgICBib3hlcyxcbiAgICAgICAgb3V0cHV0X3NpemU9KDE0LCAxNCksXG4gICAgICAgIHNwYXRpYWxfc2NhbGU9MS4wIC8gMTYuMCxcbiAgICAgICAgc2FtcGxpbmdfcmF0aW89MixcbiAgICAgICAgYWxpZ25lZD1UcnVlXG4gICAgKVxuICAgIHJldHVybiBhbGlnbmVkICAjIFtOLCBDLCAxNCwgMTRdIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBwcmFjdGljZSwgUm9JIEFsaWduIGRpdmlkZXMgZWFjaCBvdXRwdXQgY2VsbCBpbnRvIGEgMngyIG9yIDR4NCBzdWItZ3JpZCBhbmQgc2FtcGxlcyBmb3VyIGJpbGluZWFyIGludGVycG9sYXRpb24gcG9pbnRzIHBlciBzdWItY2VsbCwgdGhlbiBhdmVyYWdlcyB3aXRoaW4gZWFjaCBjZWxsLiBUaGUgaW1wcm92ZW1lbnQgb3ZlciBSb0kgUG9vbGluZyBpcyBtb3N0IHByb25vdW5jZWQgZm9yIG1hc2sgcXVhbGl0eSDigJQgTWFzayBSLUNOTlx1MDAyN3MgcGFwZXIgcmVwb3J0cyBhIDMtcG9pbnQgbWFzayBBUCBnYWluIGZyb20gc3dpdGNoaW5nIHRvIFJvSSBBbGlnbiwgZXNwZWNpYWxseSBmb3Igc21hbGwgb3IgdGhpbiBvYmplY3RzIHN1Y2ggYXMgcG9sZXMgYW5kIHdpcmVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1hc2sgSGVhZCBBcmNoaXRlY3R1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtYXNrIGhlYWQgaXMgYSBzbWFsbCBmdWxseSBjb252b2x1dGlvbmFsIG5ldHdvcmsgYXBwbGllZCBpbmRlcGVuZGVudGx5IHRvIGVhY2ggUm9JIGZlYXR1cmUuIEl0IGNvbnNpc3RzIG9mIGZvdXIgM3gzIGNvbnZvbHV0aW9uYWwgbGF5ZXJzIHdpdGggMjU2IGNoYW5uZWxzIGFuZCBSZUxVIGFjdGl2YXRpb25zLCBmb2xsb3dlZCBieSBhIHRyYW5zcG9zZWQgY29udm9sdXRpb24gdG8gdXBzYW1wbGUgZnJvbSAxNHgxNCB0byAyOHgyOCwgYW5kIGEgMXgxIGNvbnYgd2l0aCBzaWdtb2lkIGFjdGl2YXRpb24uIE9uZSAyOHgyOCBiaW5hcnkgbWFzayBpcyBwcmVkaWN0ZWQgcGVyIGNsYXNzIHdpdGhvdXQgY2xhc3MgY29tcGV0aXRpb24gaW4gdGhlIGhlYWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBNYXNrSGVhZChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIjR4IGNvbnYzeDMgLVx1MDAzZSBkZWNvbnYgLVx1MDAzZSAxeDE7IG91dHB1dDogW04sIG51bV9jbGFzc2VzLCAyOCwgMjhdLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBudW1fY2xhc3Nlcz04MCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmNvbnZzID0gbm4uU2VxdWVudGlhbCgqW1xuICAgICAgICAgICAgbm4uU2VxdWVudGlhbChubi5Db252MmQoMjU2LCAyNTYsIDMsIHBhZGRpbmc9MSksIG5uLlJlTFUoKSlcbiAgICAgICAgICAgIGZvciBfIGluIHJhbmdlKDQpXSlcbiAgICAgICAgc2VsZi5kZWNvbnYgPSBubi5Db252VHJhbnNwb3NlMmQoMjU2LCAyNTYsIDIsIHN0cmlkZT0yKVxuICAgICAgICBzZWxmLm91dCA9IG5uLkNvbnYyZCgyNTYsIG51bV9jbGFzc2VzLCAxKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICB4ID0gc2VsZi5jb252cyh4KVxuICAgICAgICB4ID0gbm4uZnVuY3Rpb25hbC5yZWx1KHNlbGYuZGVjb252KHgpKVxuICAgICAgICByZXR1cm4gc2VsZi5vdXQoeCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSAyOHgyOCByZXNvbHV0aW9uIGJhbGFuY2VzIHNwYXRpYWwgZGV0YWlsIGFnYWluc3QgY29tcHV0ZSBjb3N0LiBBdCBpbmZlcmVuY2UsIHRoZSB0b3Atc2NvcmluZyBjbGFzcyBzZWxlY3RzIHdoaWNoIG9mIHRoZSBDIHByZWRpY3RlZCBtYXNrcyB0byB1c2U7IHRoZSBjaG9zZW4gbWFzayBpcyByZXNpemVkIGJhY2sgdG8gdGhlIGJvdW5kaW5nIGJveCBkaW1lbnNpb25zIHVzaW5nIGJpbGluZWFyIGludGVycG9sYXRpb24gYW5kIHBhc3RlZCBpbnRvIHRoZSBmdWxsIGltYWdlIGNhbnZhcy4gTWFzayBwcmVkaWN0aW9uIGFuZCBjbGFzc2lmaWNhdGlvbiByZW1haW4gZnVsbHkgZGVjb3VwbGVkIHRocm91Z2hvdXQgdHJhaW5pbmcgYW5kIGluZmVyZW5jZSwgcHJldmVudGluZyBjcm9zcy1jbGFzcyBncmFkaWVudCBpbnRlcmZlcmVuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktdGFzayBUcmFpbmluZyBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNYXNrIFItQ05OIG9wdGltaXplcyB0aHJlZSBsb3NzZXMgam9pbnRseTogY3Jvc3MtZW50cm9weSBjbGFzc2lmaWNhdGlvbiBsb3NzLCBzbW9vdGgtTDEgYm91bmRpbmcgYm94IHJlZ3Jlc3Npb24gbG9zcywgYW5kIGJpbmFyeSBjcm9zcy1lbnRyb3B5IG1hc2sgbG9zcy4gVGhlIHRvdGFsIGxvc3MgaXMgdGhlaXIgdW53ZWlnaHRlZCBzdW0uIE9ubHkgcG9zaXRpdmUgUm9JcyDigJQgdGhvc2UgbWF0Y2hlZCB0byBhIGdyb3VuZC10cnV0aCBvYmplY3QgYnkgSW9VIHRocmVzaG9sZCDigJQgY29udHJpYnV0ZSB0byB0aGUgbWFzayBsb3NzLiBOZWdhdGl2ZSBSb0lzIGNvbnRyaWJ1dGUgb25seSB0byBjbGFzc2lmaWNhdGlvbiBhbmQgYm94IHJlZ3Jlc3Npb24gbG9zc2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIG1hc2tfbG9zcyhwcmVkX21hc2tzLCBndF9tYXNrcywgZ3RfbGFiZWxzLCBwb3NfaWR4KTpcbiAgICBcIlwiXCJCQ0UgbWFzayBsb3NzIG9uIEdUIGNsYXNzIGNoYW5uZWwgb25seSwgYXZlcmFnZWQgb3ZlciBwb3NpdGl2ZSBSb0lzLlwiXCJcIlxuICAgIHBvc19wcmVkID0gcHJlZF9tYXNrc1twb3NfaWR4XSAgICAgICAjIFtQLCBDLCAyOCwgMjhdXG4gICAgcG9zX2d0ICAgPSBndF9tYXNrc1twb3NfaWR4XSAgICAgICAgICMgW1AsIDI4LCAyOF0gYmluYXJ5IGZsb2F0XG4gICAgcG9zX2NscyAgPSBndF9sYWJlbHNbcG9zX2lkeF0gICAgICAgICMgW1BdIEdUIGNsYXNzIGluZGljZXNcbiAgICAjIFNlbGVjdCBwcmVkaWN0ZWQgbWFzayBhdCB0aGUgZ3JvdW5kLXRydXRoIGNsYXNzIGNoYW5uZWxcbiAgICBzZWwgPSBwb3NfY2xzLnZpZXcoLTEsIDEsIDEsIDEpLmV4cGFuZCgtMSwgMSwgMjgsIDI4KVxuICAgIGNob3NlbiA9IHBvc19wcmVkLmdhdGhlcigxLCBzZWwpLnNxdWVlemUoMSkgICMgW1AsIDI4LCAyOF1cbiAgICByZXR1cm4gRi5iaW5hcnlfY3Jvc3NfZW50cm9weV93aXRoX2xvZ2l0cyhjaG9zZW4sIHBvc19ndC5mbG9hdCgpKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGJpbmFyeSBjcm9zcy1lbnRyb3B5IG1hc2sgbG9zcyBpcyBhdmVyYWdlZCBvdmVyIGFsbCBwaXhlbHMgaW4gdGhlIDI4eDI4IHByZWRpY3Rpb24gZm9yIGVhY2ggcG9zaXRpdmUgUm9JLiBDcnVjaWFsbHksIHRoZSBsb3NzIGlzIGNvbXB1dGVkIG9ubHkgb24gdGhlIG1hc2sgY2hhbm5lbCBjb3JyZXNwb25kaW5nIHRvIHRoZSBncm91bmQtdHJ1dGggY2xhc3MsIG5vdCB0aGUgcHJlZGljdGVkIGNsYXNzLiBUaGlzIGRlc2lnbiBjaG9pY2UgcHJldmVudHMgZ3JhZGllbnQgaW50ZXJmZXJlbmNlIGJldHdlZW4gY2xhc3MgbWFza3MsIGFsbG93aW5nIGVhY2ggY2hhbm5lbCB0byBzcGVjaWFsaXplIHdpdGhvdXQgY29tcGV0aW5nIHdpdGggb3RoZXJzIGR1cmluZyBiYWNrcHJvcGFnYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUnVubmluZyBNYXNrIFItQ05OIHdpdGggdG9yY2h2aXNpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0b3JjaHZpc2lvbiBsaWJyYXJ5IHNoaXBzIE1hc2sgUi1DTk4gd2l0aCBhIFJlc05ldC01MC1GUE4gYmFja2JvbmUgcHJldHJhaW5lZCBvbiBDT0NPLCBhdmFpbGFibGUgdmlhIGEgc2luZ2xlIG1vZGVsIGZhY3RvcnkgY2FsbC4gVGhlIHByZXRyYWluZWQgbW9kZWwgYWNoaWV2ZXMgMzcuOSBib3ggQVAgYW5kIDM0LjYgbWFzayBBUCBvbiBDT0NPIG1pbml2YWwuIEZvciBpbmZlcmVuY2UsIGltYWdlcyBhcmUgcGFzc2VkIGFzIGEgbGlzdCBvZiB0ZW5zb3JzOyB0aGUgbW9kZWwgcmV0dXJucyBib3hlcywgbGFiZWxzLCBzY29yZXMsIGFuZCBiaW5hcnkgbWFza3MgYXQgMjh4MjggcmVzb2x1dGlvbiBhbHJlYWR5IHJlc2l6ZWQgdG8gZWFjaCBkZXRlY3RlZCBib3guIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaHZpc2lvbi5tb2RlbHMuZGV0ZWN0aW9uIGltcG9ydCBtYXNrcmNubl9yZXNuZXQ1MF9mcG4sIE1hc2tSQ05OX1Jlc05ldDUwX0ZQTl9XZWlnaHRzXG5pbXBvcnQgdG9yY2h2aXNpb24udHJhbnNmb3Jtcy5mdW5jdGlvbmFsIGFzIFRGXG5cbm1vZGVsID0gbWFza3Jjbm5fcmVzbmV0NTBfZnBuKHdlaWdodHM9TWFza1JDTk5fUmVzTmV0NTBfRlBOX1dlaWdodHMuREVGQVVMVClcbm1vZGVsLmV2YWwoKVxuXG5pbWdfdGVuc29yID0gVEYudG9fdGVuc29yKGltYWdlX3BpbCkudW5zcXVlZXplKDApXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBwcmVkcyA9IG1vZGVsKGltZ190ZW5zb3IpWzBdXG5cbm1hc2tzICA9IHByZWRzW1wibWFza3NcIl1bOiwgMF0gXHUwMDNlIDAuNVxuc2NvcmVzID0gcHJlZHNbXCJzY29yZXNcIl1cbmxhYmVscyA9IHByZWRzW1wibGFiZWxzXCJdXG5wcmludChmXCJ7KHNjb3JlcyBcdTAwM2UgMC45KS5zdW0oKX0gaGlnaC1jb25maWRlbmNlIGRldGVjdGlvbnNcIikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBjdXN0b20gZGF0YXNldCBmaW5lLXR1bmluZywgcmVwbGFjZSB0aGUgYm94IHByZWRpY3RvciBhbmQgbWFzayBwcmVkaWN0b3IgaGVhZHMgd2l0aCBuZXcgb25lcyBtYXRjaGluZyB0aGUgbnVtYmVyIG9mIHRhcmdldCBjbGFzc2VzLiBGcmVlemUgYmFja2JvbmUgbGF5ZXJzIGR1cmluZyBpbml0aWFsIHRyYWluaW5nIHRoZW4gdW5mcmVlemUgZm9yIGZpbmUtdHVuaW5nLiBUaGUgZGVmYXVsdCBhbmNob3IgZ2VuZXJhdG9yIGFuZCBOTVMgdGhyZXNob2xkcyB3b3JrIHdlbGwgZm9yIG1vc3QgZGF0YXNldHMsIGJ1dCBhZGp1c3RpbmcgdGhlIG1pbmltdW0gc2NvcmUgdGhyZXNob2xkIGF0IGluZmVyZW5jZSBzaWduaWZpY2FudGx5IGFmZmVjdHMgdGhlIG51bWJlciBvZiByZXR1cm5lZCBpbnN0YW5jZXMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiQVAgKGJveCkiLCJBUCAobWFzaykiLCJCYWNrYm9uZSIsIkZQUyIsIlllYXIiXSwicm93cyI6W1siTWFzayBSLUNOTiIsIjM4LjIiLCIzNC43IiwiUmVzTmV0LTUwLUZQTiIsIjguOCIsIjIwMTciXSxbIlBBTmV0IiwiNDIuMCIsIjM3LjUiLCJSZXNOZXQtNTAtRlBOIiwiNC43IiwiMjAxOCJdLFsiSFRDIiwiNDQuOSIsIjM4LjQiLCJSZXNOZXQtNTAtRlBOIiwiMi4zIiwiMjAxOSJdLFsiU09MT3YyIiwiMzkuNyIsIjM1LjUiLCJSZXNOZXQtNTAtRlBOIiwiMTguMCIsIjIwMjAiXSxbIlF1ZXJ5SW5zdCIsIjQ0LjUiLCIzOS43IiwiUmVzTmV0LTUwLUZQTiIsIjEwLjAiLCIyMDIxIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNYXNrIFItQ05OXHUwMDI3cyBrZXkgaW5zaWdodCBpcyB0aGF0IGluc3RhbmNlIHNlZ21lbnRhdGlvbiBjYW4gYmUgZGVjb21wb3NlZCBpbnRvIGRldGVjdGlvbiBhbmQgc2VnbWVudGF0aW9uIGFzIHBhcmFsbGVsIHRhc2tzIHNoYXJpbmcgYSBiYWNrYm9uZS4gVGhlIEZQTiBiYWNrYm9uZSBwcm92aWRlcyBtdWx0aS1zY2FsZSBmZWF0dXJlcyBlbmFibGluZyBkZXRlY3Rpb24gYWNyb3NzIHNjYWxlcy4gVGhpcyB0d28tc3RhZ2UgYXBwcm9hY2gg4oCUIGZpcnN0IGRldGVjdCB0aGVuIHNlZ21lbnQg4oCUIHByb2R1Y2VzIGhpZ2gtcXVhbGl0eSBtYXNrcyBieSBmb2N1c2luZyB0aGUgbWFzayBoZWFkIG9uIGFscmVhZHktbG9jYWxpemVkIHJlZ2lvbnMgcmF0aGVyIHRoYW4gZnVsbCBpbWFnZXMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSb0kgQWxpZ24gaXMgYSBjcml0aWNhbCBjb250cmlidXRpb24g4oCUIHRoZSBzaGlmdCBmcm9tIHF1YW50aXplZCBSb0kgUG9vbGluZyB0byBiaWxpbmVhci1pbnRlcnBvbGF0ZWQgc2FtcGxpbmcgbWF5IHNlZW0gbWlub3IgYnV0IHlpZWxkcyBzaWduaWZpY2FudCBtYXNrIHF1YWxpdHkgaW1wcm92ZW1lbnRzLiBTcGF0aWFsIG1pc2FsaWdubWVudCBvZiBldmVuIG9uZSBwaXhlbCBhdCB0aGUgZmVhdHVyZSBsZXZlbCB0cmFuc2xhdGVzIHRvIHZpc2libGUgYXJ0aWZhY3RzIGluIHRoZSB1cHNhbXBsZWQgMjh4MjggbWFzaywgZXNwZWNpYWxseSBmb3Igc21hbGwgb3IgdGhpbiBvYmplY3RzIHN1Y2ggYXMgcG9sZXMsIHdpcmVzLCBvciBwZWRlc3RyaWFuIGxpbWJzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGktdGFzayB0cmFpbmluZyB3aXRoIGEgam9pbnQgbG9zcyBpcyBjcnVjaWFsIGZvciBwZXJmb3JtYW5jZS4gVGhlIG1hc2sgaGVhZCBiZW5lZml0cyBmcm9tIHRoZSBvYmplY3QgbG9jYWxpemF0aW9uIHNpZ25hbCBwcm92aWRlZCBieSB0aGUgYm94IGhlYWQsIGFuZCB0aGUgYm94IGhlYWQgaW1wcm92ZXMgZnJvbSBhZGRpdGlvbmFsIHN1cGVydmlzaW9uLiBKb2ludGx5IHRyYWluaW5nIGFsbCB0aHJlZSB0YXNrcyBwcm9kdWNlcyBiZXR0ZXIgc2hhcmVkIHJlcHJlc2VudGF0aW9ucyB0aGFuIGFueSBzaW5nbGUtdGFzayBtb2RlbCwgc2hvd2luZyB0aGF0IGNvbXBsZW1lbnRhcnkgdmlzaW9uIG9iamVjdGl2ZXMgcmVndWxhcml6ZSBmZWF0dXJlcyBlZmZlY3RpdmVseS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1hc2sgUi1DTk4gcmVtYWlucyBhIHN0cm9uZyBiYXNlbGluZSBmb3IgaW5zdGFuY2Ugc2VnbWVudGF0aW9uIGRlc3BpdGUgYmVpbmcgcHVibGlzaGVkIGluIDIwMTcuIFN1YnNlcXVlbnQgYWR2YW5jZXMgbGlrZSBQQU5ldCwgSFRDLCBTT0xPdjIsIGFuZCBRdWVyeUluc3QgaW1wcm92ZSBBUCBieSA1IHRvIDE1IHBvaW50cyBidXQgc2hhcmUgaXRzIGNvcmUgZGVzaWduIHByaW5jaXBsZXMuIFVuZGVyc3RhbmRpbmcgTWFzayBSLUNOTiBpcyBlc3NlbnRpYWwgZm9yIHJlYWRpbmcgbW9kZXJuIGluc3RhbmNlIHNlZ21lbnRhdGlvbiBsaXRlcmF0dXJlIGFuZCBhZGFwdGluZyBtb2RlbHMgdG8gZG9tYWluLXNwZWNpZmljIGFwcGxpY2F0aW9ucy4ifV0="
---
# Mask R-CNN: Instance Segmentation

## Overview

Mask R-CNN extends Faster R-CNN by adding a third parallel branch that predicts a segmentation mask for each detected object. The model uses a ResNet-FPN backbone for multi-scale features, a Region Proposal Network for candidate boxes, and separate heads for class prediction, bounding box regression, and binary mask output. It achieves state-of-the-art instance segmentation on COCO with practical inference speed.

> **warning**: Mask R-CNN predicts masks independently per class — it does NOT use the predicted class to pick the mask at training time. This avoids competition between classes in the mask head.

## RoI Align for Precise Alignment

RoI Pooling quantizes region coordinates to integers, creating spatial misalignment that degrades mask accuracy. RoI Align removes quantization by sampling features at exact floating-point positions using bilinear interpolation. A fixed sampling grid per output cell is computed from the feature map without rounding, preserving spatial accuracy that is essential for the downstream 28x28 mask branch.

```python
import torch
import torchvision.ops as ops

def demo_roi_align(feature_map, boxes):
    """RoI Align: bilinear sampling at exact coords, no quantization error."""
    # feature_map: [B, C, H, W]; boxes: [N, 5] (batch_idx, x1, y1, x2, y2)
    aligned = ops.roi_align(
        feature_map,
        boxes,
        output_size=(14, 14),
        spatial_scale=1.0 / 16.0,
        sampling_ratio=2,
        aligned=True
    )
    return aligned  # [N, C, 14, 14]
```

In practice, RoI Align divides each output cell into a 2x2 or 4x4 sub-grid and samples four bilinear interpolation points per sub-cell, then averages within each cell. The improvement over RoI Pooling is most pronounced for mask quality — Mask R-CNN's paper reports a 3-point mask AP gain from switching to RoI Align, especially for small or thin objects such as poles and wires.

## Mask Head Architecture

The mask head is a small fully convolutional network applied independently to each RoI feature. It consists of four 3x3 convolutional layers with 256 channels and ReLU activations, followed by a transposed convolution to upsample from 14x14 to 28x28, and a 1x1 conv with sigmoid activation. One 28x28 binary mask is predicted per class without class competition in the head.

```python
import torch.nn as nn

class MaskHead(nn.Module):
    """4x conv3x3 -> deconv -> 1x1; output: [N, num_classes, 28, 28]."""
    def __init__(self, num_classes=80):
        super().__init__()
        self.convs = nn.Sequential(*[
            nn.Sequential(nn.Conv2d(256, 256, 3, padding=1), nn.ReLU())
            for _ in range(4)])
        self.deconv = nn.ConvTranspose2d(256, 256, 2, stride=2)
        self.out = nn.Conv2d(256, num_classes, 1)
    def forward(self, x):
        x = self.convs(x)
        x = nn.functional.relu(self.deconv(x))
        return self.out(x)
```

The 28x28 resolution balances spatial detail against compute cost. At inference, the top-scoring class selects which of the C predicted masks to use; the chosen mask is resized back to the bounding box dimensions using bilinear interpolation and pasted into the full image canvas. Mask prediction and classification remain fully decoupled throughout training and inference, preventing cross-class gradient interference.

## Multi-task Training Loss

Mask R-CNN optimizes three losses jointly: cross-entropy classification loss, smooth-L1 bounding box regression loss, and binary cross-entropy mask loss. The total loss is their unweighted sum. Only positive RoIs — those matched to a ground-truth object by IoU threshold — contribute to the mask loss. Negative RoIs contribute only to classification and box regression losses.

```python
import torch
import torch.nn.functional as F

def mask_loss(pred_masks, gt_masks, gt_labels, pos_idx):
    """BCE mask loss on GT class channel only, averaged over positive RoIs."""
    pos_pred = pred_masks[pos_idx]       # [P, C, 28, 28]
    pos_gt   = gt_masks[pos_idx]         # [P, 28, 28] binary float
    pos_cls  = gt_labels[pos_idx]        # [P] GT class indices
    # Select predicted mask at the ground-truth class channel
    sel = pos_cls.view(-1, 1, 1, 1).expand(-1, 1, 28, 28)
    chosen = pos_pred.gather(1, sel).squeeze(1)  # [P, 28, 28]
    return F.binary_cross_entropy_with_logits(chosen, pos_gt.float())
```

The binary cross-entropy mask loss is averaged over all pixels in the 28x28 prediction for each positive RoI. Crucially, the loss is computed only on the mask channel corresponding to the ground-truth class, not the predicted class. This design choice prevents gradient interference between class masks, allowing each channel to specialize without competing with others during backpropagation.

## Running Mask R-CNN with torchvision

The torchvision library ships Mask R-CNN with a ResNet-50-FPN backbone pretrained on COCO, available via a single model factory call. The pretrained model achieves 37.9 box AP and 34.6 mask AP on COCO minival. For inference, images are passed as a list of tensors; the model returns boxes, labels, scores, and binary masks at 28x28 resolution already resized to each detected box.

```python
import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights
import torchvision.transforms.functional as TF

model = maskrcnn_resnet50_fpn(weights=MaskRCNN_ResNet50_FPN_Weights.DEFAULT)
model.eval()

img_tensor = TF.to_tensor(image_pil).unsqueeze(0)
with torch.no_grad():
    preds = model(img_tensor)[0]

masks  = preds["masks"][:, 0] > 0.5
scores = preds["scores"]
labels = preds["labels"]
print(f"{(scores > 0.9).sum()} high-confidence detections")
```

For custom dataset fine-tuning, replace the box predictor and mask predictor heads with new ones matching the number of target classes. Freeze backbone layers during initial training then unfreeze for fine-tuning. The default anchor generator and NMS thresholds work well for most datasets, but adjusting the minimum score threshold at inference significantly affects the number of returned instances.

| Model | AP (box) | AP (mask) | Backbone | FPS | Year |
| --- | --- | --- | --- | --- | --- |
| Mask R-CNN | 38.2 | 34.7 | ResNet-50-FPN | 8.8 | 2017 |
| PANet | 42.0 | 37.5 | ResNet-50-FPN | 4.7 | 2018 |
| HTC | 44.9 | 38.4 | ResNet-50-FPN | 2.3 | 2019 |
| SOLOv2 | 39.7 | 35.5 | ResNet-50-FPN | 18.0 | 2020 |
| QueryInst | 44.5 | 39.7 | ResNet-50-FPN | 10.0 | 2021 |

## Key Takeaways

Mask R-CNN's key insight is that instance segmentation can be decomposed into detection and segmentation as parallel tasks sharing a backbone. The FPN backbone provides multi-scale features enabling detection across scales. This two-stage approach — first detect then segment — produces high-quality masks by focusing the mask head on already-localized regions rather than full images.

RoI Align is a critical contribution — the shift from quantized RoI Pooling to bilinear-interpolated sampling may seem minor but yields significant mask quality improvements. Spatial misalignment of even one pixel at the feature level translates to visible artifacts in the upsampled 28x28 mask, especially for small or thin objects such as poles, wires, or pedestrian limbs.

Multi-task training with a joint loss is crucial for performance. The mask head benefits from the object localization signal provided by the box head, and the box head improves from additional supervision. Jointly training all three tasks produces better shared representations than any single-task model, showing that complementary vision objectives regularize features effectively.

Mask R-CNN remains a strong baseline for instance segmentation despite being published in 2017. Subsequent advances like PANet, HTC, SOLOv2, and QueryInst improve AP by 5 to 15 points but share its core design principles. Understanding Mask R-CNN is essential for reading modern instance segmentation literature and adapting models to domain-specific applications.

