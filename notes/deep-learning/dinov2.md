---
title: "DINOv2 — Curated Data and Improved SSL for Universal Features"
slug: "dinov2"
description: "DINOv2 (Oquab et al. 2023) scales DINO with a carefully curated 142M-image dataset, adds iBOT masked image modeling and SwAV regularization, and produces frozen features that achieve state-of-the-art performance on depth estimation, segmentation, and classification via simple linear probes."
tags: ["deep-learning", "self-supervised-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElOT3YyIChPcXVhYiBldCBhbC4gMjAyMykgYXNrZWQgYSBzaW1wbGUgcXVlc3Rpb246IHdoYXQgaGFwcGVucyB0byBzZWxmLXN1cGVydmlzZWQgdmlzdWFsIGZlYXR1cmVzIHdoZW4geW91IGZpeCB0aGUgZGF0YSBhbmQgdHJhaW5pbmcgcmVjaXBlIHJhdGhlciB0aGFuIGp1c3Qgc2NhbGluZyB0aGUgbW9kZWw/IFRoZSBhbnN3ZXIgd2FzIHN0cmlraW5nIOKAlCBmcm96ZW4gRElOT3YyIGZlYXR1cmVzIG91dHBlcmZvcm0gc3VwZXJ2aXNlZCBWaVQtTCBvbiBkZXB0aCBlc3RpbWF0aW9uIGFuZCBtYXRjaCBpdCBvbiBzZWdtZW50YXRpb24gdXNpbmcgbm90aGluZyBtb3JlIHRoYW4gYSBzaW5nbGUgbGluZWFyIGxheWVyLiBUaGUga2V5IGlubm92YXRpb25zIGFyZSBhIGN1cmF0ZWQgMTQyTS1pbWFnZSBkYXRhc2V0IChMVkQtMTQyTSksIHRoZSBjb21iaW5hdGlvbiBvZiBESU5PICsgaUJPVCArIFN3QVYgb2JqZWN0aXZlcywgYW5kIGNhcmVmdWwgc3RhYmlsaXNhdGlvbiB0cmlja3MgdGhhdCBhbGxvdyB0cmFpbmluZyBWaVQtZyAoMUIgcGFyYW1ldGVycykgdG8gY29tcGxldGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEYXRhc2V0IEN1cmF0aW9uIOKAlCBMVkQtMTQyTSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJpb3Igc2VsZi1zdXBlcnZpc2VkIG1ldGhvZHMgdHJhaW5lZCBvbiBJbWFnZU5ldC0xSyAoMS4yOE0gaW1hZ2VzKSBvciB1bmN1cmF0ZWQgaW50ZXJuZXQgY3Jhd2xzLiBESU5PdjIgcHJvcG9zZXMgYSBtaWRkbGUgcGF0aDogaGFydmVzdCBpbWFnZXMgZnJvbSB0aGUgaW50ZXJuZXQsIHRoZW4gYWdncmVzc2l2ZWx5IGZpbHRlciBmb3IgcXVhbGl0eSBhbmQgZGl2ZXJzaXR5LiBTdGFydGluZyBmcm9tIDEuMkIgY2FuZGlkYXRlIGltYWdlcywgdGhlIHBpcGVsaW5lIGFwcGxpZXM6ICgxKSBkZWR1cGxpY2F0aW9uIOKAlCByZW1vdmUgbmVhci1kdXBsaWNhdGVzIHVzaW5nIGNvcHktZGV0ZWN0aW9uIGhhc2hpbmc7ICgyKSByZXRyaWV2YWwtYmFzZWQgY3VyYXRpb24g4oCUIHVzZSBJbWFnZU5ldC0yMksgYXMgc2VlZHMsIHJldHJpZXZlIG5lYXJlc3QgbmVpZ2hib3VycyBmcm9tIHRoZSB3ZWIgcG9vbCB1c2luZyBhIHByZXRyYWluZWQgU1NMIG1vZGVsLCB0aGVuIHRocmVzaG9sZCBieSBzaW1pbGFyaXR5OyAoMykgbGVha2FnZSBwcmV2ZW50aW9uIOKAlCBkZWR1cGxpY2F0ZSBhZ2FpbnN0IGRvd25zdHJlYW0gdGVzdCBzZXRzIChJbWFnZU5ldCB2YWwsIEFERTIwSywgZXRjLikgdG8gZW5zdXJlIGZhaXIgZXZhbHVhdGlvbi4gVGhlIHJlc3VsdCBpcyBMVkQtMTQyTTogMTQyTSBoaWdoLXF1YWxpdHksIGRpdmVyc2UsIG5vbi1sZWFraW5nIGltYWdlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBub3JtYWxpemVcblxuXG5kZWYgZXh0cmFjdF9mZWF0dXJlc19mb3JfZGVkdXAobW9kZWwsIGRhdGFsb2FkZXIsIGRldmljZT1cdTAwMjdjdWRhXHUwMDI3KTpcbiAgICBcIlwiXCJFeHRyYWN0IEwyLW5vcm1hbGlzZWQgZW1iZWRkaW5ncyBmb3IgbmVhci1kdXBsaWNhdGUgZGV0ZWN0aW9uLlwiXCJcIlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIGFsbF9mZWF0cywgYWxsX2lkcyA9IFtdLCBbXVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgaW1ncywgaWRzIGluIGRhdGFsb2FkZXI6XG4gICAgICAgICAgICBmZWF0cyA9IG1vZGVsKGltZ3MudG8oZGV2aWNlKSkgICAgICAgICMgKEIsIEQpXG4gICAgICAgICAgICBmZWF0cyA9IEYubm9ybWFsaXplKGZlYXRzLCBkaW09MSkgICAgICMgdW5pdCBzcGhlcmVcbiAgICAgICAgICAgIGFsbF9mZWF0cy5hcHBlbmQoZmVhdHMuY3B1KCkubnVtcHkoKSlcbiAgICAgICAgICAgIGFsbF9pZHMuZXh0ZW5kKGlkcylcbiAgICByZXR1cm4gbnAudnN0YWNrKGFsbF9mZWF0cyksIGFsbF9pZHNcblxuXG5kZWYgbmVhcl9kdXBsaWNhdGVfcmVtb3ZhbChmZWF0dXJlcywgaWRzLCB0aHJlc2hvbGQ9MC45NSk6XG4gICAgXCJcIlwiUmVtb3ZlIG5lYXItZHVwbGljYXRlczogY29zaW5lLXNpbWlsYXJpdHkgXHUwMDNlIHRocmVzaG9sZC5cbiAgICBSZXR1cm5zIGxpc3Qgb2YgcmV0YWluZWQgaW1hZ2UgaWRzLlxuICAgIFN0cmF0ZWd5OiBncmVlZHkg4oCUIGtlZXAgZmlyc3Qgb2NjdXJyZW5jZSwgcmVtb3ZlIGxhdGVyIGR1cGxpY2F0ZXMuXG4gICAgXCJcIlwiXG4gICAgZmVhdHVyZXMgPSBub3JtYWxpemUoZmVhdHVyZXMsIGF4aXM9MSkgICMgZW5zdXJlIHVuaXQgbm9ybVxuICAgIG4gPSBsZW4oZmVhdHVyZXMpXG4gICAgcmVtb3ZlZCA9IHNldCgpXG4gICAgcmV0YWluZWQgPSBbXVxuICAgIGZvciBpIGluIHJhbmdlKG4pOlxuICAgICAgICBpZiBpIGluIHJlbW92ZWQ6XG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICByZXRhaW5lZC5hcHBlbmQoaWRzW2ldKVxuICAgICAgICAjIFZlY3RvcmlzZWQgY29zaW5lIHNpbWlsYXJpdHk6IGZlYXRfaSBkb3QgYWxsX2pcbiAgICAgICAgc2ltcyA9IGZlYXR1cmVzW2ldIEAgZmVhdHVyZXNbaSsxOl0uVCAgICMgKG4taS0xLClcbiAgICAgICAgZHVwX29mZnNldHMgPSBucC53aGVyZShzaW1zIFx1MDAzZSB0aHJlc2hvbGQpWzBdXG4gICAgICAgIGZvciBvZmYgaW4gZHVwX29mZnNldHM6XG4gICAgICAgICAgICByZW1vdmVkLmFkZChpICsgMSArIG9mZilcbiAgICByZXR1cm4gcmV0YWluZWRcblxuXG5kZWYgcXVhbGl0eV9maWx0ZXIoc2NvcmVzLCBpZHMsIG1pbl9zY29yZT0wLjUpOlxuICAgIFwiXCJcIktlZXAgaW1hZ2VzIHdob3NlIGFlc3RoZXRpYy9xdWFsaXR5IHNjb3JlIGV4Y2VlZHMgdGhyZXNob2xkLlwiXCJcIlxuICAgIHJldHVybiBbaWRfIGZvciBpZF8sIHMgaW4gemlwKGlkcywgc2NvcmVzKSBpZiBzIFx1MDAzZT0gbWluX3Njb3JlXVxuXG5cbnByaW50KFx1MDAyN1BpcGVsaW5lOiBleHRyYWN0IC1cdTAwM2UgZGVkdXAgKGNvc2luZSBcdTAwM2UgMC45NSkgLVx1MDAzZSBxdWFsaXR5IGZpbHRlciAtXHUwMDNlIExWRC0xNDJNXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6ImlCT1Qg4oCUIE1hc2tlZCBJbWFnZSBNb2RlbGluZyB3aXRoIE9ubGluZSBUb2tlbml6ZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIERJTk8gcHJlZGljdHMgZ2xvYmFsIENMUyB0b2tlbiByZXByZXNlbnRhdGlvbnMgYWNyb3NzIGF1Z21lbnRlZCB2aWV3cy4gaUJPVCAoSW1hZ2UgQkVSVCBwcmUtdHJhaW5pbmcgd2l0aCBPbmxpbmUgVG9rZW5pemVyLCBaaG91IGV0IGFsLiAyMDIyKSBleHRlbmRzIHRoaXMgdG8gcGF0Y2gtbGV2ZWwgdG9rZW5zLiBUaGUgdGVhY2hlciBuZXR3b3JrIGdlbmVyYXRlcyBwYXRjaC1sZXZlbCB0b2tlbiB0YXJnZXRzIGR5bmFtaWNhbGx5IOKAlCB0aGVyZSBpcyBubyBmaXhlZCBkaXNjcmV0ZSB0b2tlbml6ZXIgKHVubGlrZSBCRWlULCB3aGljaCB1c2VzIGEgcHJldHJhaW5lZCBkVkFFKS4gTWFza2VkIHBhdGNoZXMgaW4gdGhlIHN0dWRlbnQgdmlldyBtdXN0IG1hdGNoIHRoZSBjb3JyZXNwb25kaW5nIHRlYWNoZXIgcGF0Y2ggdG9rZW5zLiBESU5PdjIgYWRvcHRzIGlCT1RcdTAwMjdzIG1hc2tpbmcgYXMgYW4gYWRkaXRpb25hbCBvYmplY3RpdmUgYWxvbmdzaWRlIHRoZSBnbG9iYWwgRElOTyBsb3NzOiBMX3RvdGFsID0gTF9ESU5PICsgzrvCt0xfaUJPVCArIM68wrdMX1N3QVYuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cblxuZGVmIGlib3RfbG9zcyhzdHVkZW50X3BhdGNoX3Rva2VucywgdGVhY2hlcl9wYXRjaF90b2tlbnMsIG1hc2ssIHRlbXBfcz0wLjEsIHRlbXBfdD0wLjA0KTpcbiAgICBcIlwiXCJpQk9UIG1hc2tlZCBpbWFnZSBtb2RlbGluZyBsb3NzLlxuICAgIHN0dWRlbnRfcGF0Y2hfdG9rZW5zOiAoQiwgTiwgRCkg4oCUIHN0dWRlbnQgVmlUIHBhdGNoIG91dHB1dHNcbiAgICB0ZWFjaGVyX3BhdGNoX3Rva2VuczogKEIsIE4sIEQpIOKAlCB0ZWFjaGVyIFZpVCBwYXRjaCBvdXRwdXRzIChzdG9wLWdyYWQpXG4gICAgbWFzazogKEIsIE4pIGJvb2wg4oCUIFRydWUgZm9yIG1hc2tlZCBwb3NpdGlvbnMgdG8gcHJlZGljdFxuICAgIFwiXCJcIlxuICAgICMgU29mdG1heC1iYXNlZCBjcm9zcy1lbnRyb3B5IGluIHRva2VuIHByb2JhYmlsaXR5IHNwYWNlXG4gICAgIyBUZWFjaGVyIHByb3ZpZGVzIHNvZnQgdGFyZ2V0cyAoc2hhcnBlbmVkKTsgc3R1ZGVudCBwcmVkaWN0cyBmcm9tIGNvbnRleHRcbiAgICBzID0gc3R1ZGVudF9wYXRjaF90b2tlbnNbbWFza10gICAjIChNLCBEKSDigJQgbWFza2VkIHBvc2l0aW9ucyBvbmx5XG4gICAgdCA9IHRlYWNoZXJfcGF0Y2hfdG9rZW5zW21hc2tdICAgIyAoTSwgRClcblxuICAgICMgQ29tcHV0ZSBzb2Z0IHRhcmdldHMgZnJvbSB0ZWFjaGVyIChzaW5raG9ybi1ub3JtYWxpc2VkIG9yIHNpbXBsZSBzb2Z0bWF4KVxuICAgIHRfcHJvYnMgPSBGLnNvZnRtYXgodCAvIHRlbXBfdCwgZGltPS0xKS5kZXRhY2goKSAgICMgKE0sIEQpIHNvZnQgdGFyZ2V0c1xuICAgIHNfbG9nX3Byb2JzID0gRi5sb2dfc29mdG1heChzIC8gdGVtcF9zLCBkaW09LTEpICAgICMgKE0sIEQpXG5cbiAgICBsb3NzID0gLSh0X3Byb2JzICogc19sb2dfcHJvYnMpLnN1bShkaW09LTEpLm1lYW4oKVxuICAgIHJldHVybiBsb3NzXG5cblxuZGVmIHJhbmRvbV9ibG9ja19tYXNrKEIsIE5fcGF0Y2hlcywgbWFza19yYXRpbz0wLjE1LCBkZXZpY2U9XHUwMDI3Y3B1XHUwMDI3KTpcbiAgICBcIlwiXCJTYW1wbGUgYSByYW5kb20gbWFzayBmb3IgaUJPVDogbWFza19yYXRpbyBmcmFjdGlvbiBvZiBwYXRjaCB0b2tlbnMuXCJcIlwiXG4gICAgbnVtX21hc2sgPSBpbnQoTl9wYXRjaGVzICogbWFza19yYXRpbylcbiAgICBtYXNrcyA9IHRvcmNoLnplcm9zKEIsIE5fcGF0Y2hlcywgZHR5cGU9dG9yY2guYm9vbCwgZGV2aWNlPWRldmljZSlcbiAgICBmb3IgaSBpbiByYW5nZShCKTpcbiAgICAgICAgaWR4ID0gdG9yY2gucmFuZHBlcm0oTl9wYXRjaGVzLCBkZXZpY2U9ZGV2aWNlKVs6bnVtX21hc2tdXG4gICAgICAgIG1hc2tzW2ksIGlkeF0gPSBUcnVlXG4gICAgcmV0dXJuIG1hc2tzXG5cblxuIyBEZW1vOiByYW5kb20gbWFza2VkIHBhdGNoZXMsIHJhbmRvbSB0b2tlbiB2ZWN0b3JzXG5CLCBOLCBEID0gNCwgMTk2LCA3NjggICAjIFZpVC1COiAxNHgxND0xOTYgcGF0Y2hlcywgZGltPTc2OFxuc3R1ZGVudF90b2sgPSB0b3JjaC5yYW5kbihCLCBOLCBEKVxudGVhY2hlcl90b2sgPSB0b3JjaC5yYW5kbihCLCBOLCBEKVxubWFzayA9IHJhbmRvbV9ibG9ja19tYXNrKEIsIE4sIG1hc2tfcmF0aW89MC4xNSlcbmxvc3MgPSBpYm90X2xvc3Moc3R1ZGVudF90b2ssIHRlYWNoZXJfdG9rLCBtYXNrKVxucHJpbnQoZlx1MDAyN2lCT1QgbG9zczoge2xvc3MuaXRlbSgpOi40Zn0gIHwgIG1hc2tlZCBwYXRjaGVzOiB7bWFzay5zdW0oKS5pdGVtKCl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIE9iamVjdGl2ZXMg4oCUIERJTk8gKyBpQk9UICsgU3dBViBSZWd1bGFyaXplciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElOT3YyIGNvbWJpbmVzIHRocmVlIGNvbXBsZW1lbnRhcnkgc2VsZi1zdXBlcnZpc2VkIG9iamVjdGl2ZXMuIERJTk8gcHJvdmlkZXMgZ2xvYmFsIHZpZXcgY29uc2lzdGVuY3k6IHRoZSBzdHVkZW50XHUwMDI3cyBDTFMgdG9rZW4gbXVzdCBtYXRjaCB0aGUgdGVhY2hlclx1MDAyN3MgQ0xTIHRva2VuIGFjcm9zcyBkaWZmZXJlbnQgYXVnbWVudGVkIHZpZXdzLiBpQk9UIHByb3ZpZGVzIGxvY2FsIHBhdGNoLWxldmVsIHByZWRpY3Rpb246IHN0dWRlbnQgcGF0Y2hlcyBhdCBtYXNrZWQgcG9zaXRpb25zIG11c3QgcHJlZGljdCB0ZWFjaGVyIHBhdGNoIHRva2Vucy4gVGhlIFN3QVYgcmVndWxhcml6ZXIgKENhcm9uIGV0IGFsLiAyMDIwKSB1c2VzIG9ubGluZSBjbHVzdGVyaW5nIHRvIGVuc3VyZSB0aGF0IHRoZSBmZWF0dXJlIHNwYWNlIHJlbWFpbnMgdW5pZm9ybWx5IHNwcmVhZCDigJQgcHJldmVudGluZyBmZWF0dXJlIGNvbGxhcHNlIHdpdGhvdXQgcmVseWluZyBvbiB0aGUgYmF0Y2ggY29udHJhc3RpdmUgdGVybS4gVGhlIHRocmVlIGxvc3NlcyBhcmUgd2VpZ2h0ZWQgYW5kIHN1bW1lZDogTCA9IExfRElOTyArIDAuNcK3TF9pQk9UICsgMC4xwrdMX1N3QVYuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhaW5pbmcgU2NhbGUgYW5kIEluZnJhc3RydWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJESU5PdjItVmlULWcgaGFzIDEuMSBiaWxsaW9uIHBhcmFtZXRlcnMgYW5kIHdhcyB0cmFpbmVkIGZvciA1MDBLIGl0ZXJhdGlvbnMgb24gTFZELTE0Mk0gdXNpbmcgNjQgQTEwMCBHUFVzIG92ZXIgYXBwcm94aW1hdGVseSAxNSBkYXlzLiBTdGFiaWxpdHkgYXQgdGhpcyBzY2FsZSByZXF1aXJlZCBzZXZlcmFsIHRlY2huaXF1ZXM6IHN0b2NoYXN0aWMgZGVwdGggKGRyb3AgcGF0aCksIGZyZWV6aW5nIHBhdGNoIHByb2plY3Rpb24gZm9yIHRoZSBmaXJzdCBmZXcgdGhvdXNhbmQgc3RlcHMsIGdyYWRpZW50IGNsaXBwaW5nLCBhbmQgU2hhbXBvby9BZGFtVyB3aXRoIHNwZWNpZmljIGxlYXJuaW5nIHJhdGUgYW5kIHdlaWdodCBkZWNheSBzY2hlZHVsZXMgcGVyIHBhcmFtZXRlciBncm91cCAoaGlnaGVyIHdlaWdodCBkZWNheSBmb3IgYXR0ZW50aW9uIHBhcmFtZXRlcnMpLiBGbGFzaCBBdHRlbnRpb24gMiB3YXMgdXNlZCB0aHJvdWdob3V0IHRvIGZpdCB0aGUgVmlULWcgc2VxdWVuY2UgbGVuZ3RoIGluIG1lbW9yeS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlZpVC1TL0IvTC9nIGJhY2tib25lcyB0cmFpbmVkIOKAlCBWaVQtZyAoMUIpIGlzIHRoZSBmbGFnc2hpcCBtb2RlbC4iLCJBZGFtVyB3aXRoIM6y4oKBPTAuOSwgzrLigoI9MC45NSwgcGVhayBMUj0wLjAwMSwgd2VpZ2h0IGRlY2F5PTAuMDQg4oaSIDAuNCAoY29zaW5lKS4iLCJTdG9jaGFzdGljIGRlcHRoIHJhdGU9MC40IGZvciBWaVQtZyB0byByZWd1bGFyaXplIHRoZSBkZWVwIG5ldHdvcmsuIiwiRU1BIG1vbWVudHVtIHNjaGVkdWxlOiAwLjk5NCDihpIgMS4wIChjb3NpbmUgb3ZlciB0cmFpbmluZykg4oCUIHRlYWNoZXIgdHJhY2tzIHN0dWRlbnQuIiwiNjTDlyBBMTAwIDgwR0IsIH4xNSBkYXlzIHdhbGwtY2xvY2s7IFZpVC1MIHRyYWlucyBpbiB+MyBkYXlzIG9uIHNhbWUgaGFyZHdhcmUuIiwiRmxhc2ggQXR0ZW50aW9uIDIgZW5hYmxlcyBWaVQtZyBhdCBiYXRjaCBzaXplIDMwNzIgd2l0aG91dCBncmFkaWVudCBjaGVja3BvaW50aW5nLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW5lYXIgUHJvYmUgRXZhbHVhdGlvbiDigJQgRnJvemVuIFVuaXZlcnNhbCBGZWF0dXJlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRlZmluaW5nIGNsYWltIG9mIERJTk92MiBpcyB0aGF0IGl0cyBmZWF0dXJlcyBhcmUgXHUwMDI3dW5pdmVyc2FsXHUwMDI3IOKAlCBhIHNpbmdsZSBmcm96ZW4gYmFja2JvbmUgd2l0aCBhIHRhc2stc3BlY2lmaWMgbGluZWFyIGxheWVyIGFjaGlldmVzIHN0cm9uZyBwZXJmb3JtYW5jZSBhY3Jvc3MgZGl2ZXJzZSBkZW5zZSBwcmVkaWN0aW9uIHRhc2tzLiBUaGlzIGlzIGV2YWx1YXRlZCB3aXRoIGEgZnJvemVuIGxpbmVhciBwcm9iZTogZnJlZXplIHRoZSBiYWNrYm9uZSBlbnRpcmVseSwgZXh0cmFjdCBDTFMgb3IgcGF0Y2ggZmVhdHVyZXMsIHRyYWluIGEgbGluZWFyIGxheWVyIHdpdGggYSBzdGFuZGFyZCBvcHRpbWl6ZXIuIERJTk92Mi1WaVQtTCBhY2hpZXZlcyA4Ni41JSBJbWFnZU5ldCB0b3AtMSBsaW5lYXIgcHJvYmUg4oCUIDQlIGFib3ZlIE1BRS1WaVQtTCBhbmQgd2l0aGluIDElIG9mIHN1cGVydmlzZWQgVmlULUwuIE9uIGRlcHRoIGVzdGltYXRpb24gYW5kIEFERTIwSyBzZWdtZW50YXRpb24gdGhlIG1hcmdpbiBvdmVyIE1BRSBhbmQgQ0xJUCBpcyBldmVuIGxhcmdlci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YUxvYWRlclxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgZGF0YXNldHMsIHRyYW5zZm9ybXNcblxuXG5kZWYgYnVpbGRfbGluZWFyX3Byb2JlKGZlYXRfZGltOiBpbnQsIG51bV9jbGFzc2VzOiBpbnQgPSAxMDAwKSAtXHUwMDNlIG5uLk1vZHVsZTpcbiAgICByZXR1cm4gbm4uU2VxdWVudGlhbChcbiAgICAgICAgbm4uQmF0Y2hOb3JtMWQoZmVhdF9kaW0sIGFmZmluZT1GYWxzZSwgZXBzPTFlLTYpLFxuICAgICAgICBubi5MaW5lYXIoZmVhdF9kaW0sIG51bV9jbGFzc2VzKSxcbiAgICApXG5cblxuZGVmIHJ1bl9saW5lYXJfcHJvYmUoYmFja2JvbmUsIHByb2JlLCB0cmFpbl9sb2FkZXIsIHZhbF9sb2FkZXIsXG4gICAgICAgICAgICAgICAgICAgICBlcG9jaHM9MjAsIGxyPTAuMSwgZGV2aWNlPVx1MDAyN2N1ZGFcdTAwMjcpOlxuICAgIFwiXCJcIkZyZWV6ZSBiYWNrYm9uZTsgdHJhaW4gbGluZWFyIHByb2JlIG9ubHkuXCJcIlwiXG4gICAgYmFja2JvbmUuZXZhbCgpXG4gICAgZm9yIHAgaW4gYmFja2JvbmUucGFyYW1ldGVycygpOlxuICAgICAgICBwLnJlcXVpcmVzX2dyYWRfKEZhbHNlKVxuXG4gICAgb3B0aW1pemVyID0gdG9yY2gub3B0aW0uU0dEKHByb2JlLnBhcmFtZXRlcnMoKSwgbHI9bHIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1vbWVudHVtPTAuOSwgd2VpZ2h0X2RlY2F5PTAuMClcbiAgICBzY2hlZHVsZXIgPSB0b3JjaC5vcHRpbS5scl9zY2hlZHVsZXIuQ29zaW5lQW5uZWFsaW5nTFIob3B0aW1pemVyLCBlcG9jaHMpXG4gICAgY3JpdGVyaW9uID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpXG5cbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgcHJvYmUudHJhaW4oKVxuICAgICAgICBmb3IgaW1ncywgbGFiZWxzIGluIHRyYWluX2xvYWRlcjpcbiAgICAgICAgICAgIGltZ3MsIGxhYmVscyA9IGltZ3MudG8oZGV2aWNlKSwgbGFiZWxzLnRvKGRldmljZSlcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIGZlYXRzID0gYmFja2JvbmUoaW1ncykgICMgKEIsIGZlYXRfZGltKSDigJQgQ0xTIHRva2VuXG4gICAgICAgICAgICBsb3NzID0gY3JpdGVyaW9uKHByb2JlKGZlYXRzKSwgbGFiZWxzKVxuICAgICAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgc2NoZWR1bGVyLnN0ZXAoKVxuXG4gICAgIyBWYWxpZGF0aW9uXG4gICAgcHJvYmUuZXZhbCgpXG4gICAgY29ycmVjdCA9IHRvdGFsID0gMFxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgaW1ncywgbGFiZWxzIGluIHZhbF9sb2FkZXI6XG4gICAgICAgICAgICBpbWdzLCBsYWJlbHMgPSBpbWdzLnRvKGRldmljZSksIGxhYmVscy50byhkZXZpY2UpXG4gICAgICAgICAgICBwcmVkcyA9IHByb2JlKGJhY2tib25lKGltZ3MpKS5hcmdtYXgoMSlcbiAgICAgICAgICAgIGNvcnJlY3QgKz0gKHByZWRzID09IGxhYmVscykuc3VtKCkuaXRlbSgpXG4gICAgICAgICAgICB0b3RhbCArPSBsYWJlbHMuc2l6ZSgwKVxuICAgIHJldHVybiBjb3JyZWN0IC8gdG90YWxcblxuXG5wcmludChcdTAwMjdESU5PdjIgbGluZWFyIHByb2JlOiBmcmVlemUgYmFja2JvbmUsIEJhdGNoTm9ybSArIExpbmVhciBoZWFkIG9ubHkuXHUwMDI3KVxucHJpbnQoXHUwMDI3RElOT3YyLVZpVC1MIGFjaGlldmVzIH44Ni41JSB0b3AtMSB3aXRoIHRoaXMgc2ltcGxlIHByb3RvY29sLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZXB0aCBFc3RpbWF0aW9uIHdpdGggRnJvemVuIERJTk92MiBGZWF0dXJlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9ub2N1bGFyIGRlcHRoIGVzdGltYXRpb24gaXMgb25lIG9mIHRoZSBtb3N0IGRlbWFuZGluZyBkZW5zZSBwcmVkaWN0aW9uIHRhc2tzIGJlY2F1c2UgaXQgcmVxdWlyZXMgYm90aCBsb2NhbCBzcGF0aWFsIGFjY3VyYWN5IGFuZCBnbG9iYWwgc2NlbmUgdW5kZXJzdGFuZGluZy4gRElOT3YyIHBhdGNoIGZlYXR1cmVzICgxNMOXMTQgc3BhdGlhbCBncmlkIGZvciBhIDIyNMOXMjI0IGltYWdlKSBjYW4gYmUgZmVkIGRpcmVjdGx5IGludG8gYSBzaW5nbGUgbGluZWFyIGxheWVyIHRyYWluZWQgdG8gcHJlZGljdCBhIGRlbnNlIGRlcHRoIG1hcC4gVGhpcyBpcyBhIHJlbWFya2FibGUgZGVtb25zdHJhdGlvbiBvZiBmZWF0dXJlIHF1YWxpdHk6IG5vIHRhc2stc3BlY2lmaWMgZW5jb2RlciB0cmFpbmluZywgbm8gZGVjb2RlciwganVzdCBhIGxpbmVhciBtYXAgZnJvbSBmcm96ZW4gcGF0Y2ggdG9rZW5zIHRvIGRlcHRoIHZhbHVlcy4gRElOT3YyLVZpVC1MIHdpdGggdGhpcyBwcm90b2NvbCBvdXRwZXJmb3JtcyBtYW55IHNwZWNpYWxpemVkIGRlcHRoIG5ldHdvcmtzIGZpbmUtdHVuZWQgZW5kLXRvLWVuZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuXG5jbGFzcyBESU5PdjJEZXB0aExpbmVhcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlNpbmdsZSBsaW5lYXIgbGF5ZXIgZGVwdGggZXN0aW1hdG9yIG9uIGZyb3plbiBESU5PdjIgcGF0Y2ggdG9rZW5zLlwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGJhY2tib25lLCBwYXRjaF9kaW06IGludCA9IDEwMjQsIG91dHB1dF9oOiBpbnQgPSAxNCxcbiAgICAgICAgICAgICAgICAgb3V0cHV0X3c6IGludCA9IDE0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmFja2JvbmUgPSBiYWNrYm9uZVxuICAgICAgICBzZWxmLm91dHB1dF9oID0gb3V0cHV0X2hcbiAgICAgICAgc2VsZi5vdXRwdXRfdyA9IG91dHB1dF93XG4gICAgICAgICMgRnJlZXplIGJhY2tib25lXG4gICAgICAgIGZvciBwIGluIHNlbGYuYmFja2JvbmUucGFyYW1ldGVycygpOlxuICAgICAgICAgICAgcC5yZXF1aXJlc19ncmFkXyhGYWxzZSlcbiAgICAgICAgIyBPbmUgbGluZWFyIGxheWVyOiBwYXRjaF9kaW0gLVx1MDAzZSAxIGRlcHRoIHZhbHVlIHBlciBwYXRjaFxuICAgICAgICBzZWxmLmRlcHRoX2hlYWQgPSBubi5MaW5lYXIocGF0Y2hfZGltLCAxKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgXCJcIlwieDogKEIsIDMsIEgsIFcpIC1cdTAwM2UgZGVwdGg6IChCLCAxLCBIX291dCwgV19vdXQpLlwiXCJcIlxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgICMgRElOT3YyIHJldHVybnMgZGljdCB3aXRoIFx1MDAyN3hfbm9ybV9wYXRjaHRva2Vuc1x1MDAyNzogKEIsIE5fcGF0Y2hlcywgRClcbiAgICAgICAgICAgIG91dCA9IHNlbGYuYmFja2JvbmUuZm9yd2FyZF9mZWF0dXJlcyh4KVxuICAgICAgICAgICAgcGF0Y2hfdG9rZW5zID0gb3V0W1x1MDAyN3hfbm9ybV9wYXRjaHRva2Vuc1x1MDAyN10gICAjIChCLCAxOTYsIDEwMjQpIGZvciBWaVQtTFxuICAgICAgICBkZXB0aCA9IHNlbGYuZGVwdGhfaGVhZChwYXRjaF90b2tlbnMpICAgICAgICAgICAjIChCLCAxOTYsIDEpXG4gICAgICAgIEIsIE4sIF8gPSBkZXB0aC5zaGFwZVxuICAgICAgICBkZXB0aCA9IGRlcHRoLnZpZXcoQiwgc2VsZi5vdXRwdXRfaCwgc2VsZi5vdXRwdXRfdywgMSlcbiAgICAgICAgZGVwdGggPSBkZXB0aC5wZXJtdXRlKDAsIDMsIDEsIDIpICAgICAgICAgICAgICAgIyAoQiwgMSwgSCwgVylcbiAgICAgICAgIyBVcHNhbXBsZSB0byBpbnB1dCByZXNvbHV0aW9uXG4gICAgICAgIGRlcHRoID0gRi5pbnRlcnBvbGF0ZShkZXB0aCwgc2NhbGVfZmFjdG9yPTE2LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbW9kZT1cdTAwMjdiaWxpbmVhclx1MDAyNywgYWxpZ25fY29ybmVycz1GYWxzZSlcbiAgICAgICAgcmV0dXJuIGRlcHRoXG5cblxucHJpbnQoXHUwMDI3RElOT3YyIGRlcHRoIHByb2JlOiBzaW5nbGUgbm4uTGluZWFyIG9uIHBhdGNoIHRva2VucyAtXHUwMDNlIGJpbGluZWFyIHVwc2FtcGxlLlx1MDAyNylcbnByaW50KFx1MDAyN1ZpVC1MIHBhdGNoIHRva2VuczogKEIsIDE5NiwgMTAyNCkgZm9yIDIyNHgyMjQgaW5wdXQgd2l0aCAxNHgxNCBwYXRjaGVzLlx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Imluc2lnaHQiLCJ0aXRsZSI6IldoeSBESU5PdjIgQmVhdHMgTUFFIG9uIEZyb3plbiBFdmFsdWF0aW9uIiwiY29udGVudCI6Ik1BRSBpcyBvcHRpbWlzZWQgdG8gcmVjb25zdHJ1Y3QgcGl4ZWwgdmFsdWVzIGZyb20gdmlzaWJsZSBwYXRjaGVzIOKAlCBpdCBuZXZlciBzZWVzIGEgZGlzY3JpbWluYXRpdmUgc2lnbmFsLiBJdHMgZmVhdHVyZXMgcmVxdWlyZSBmaW5lLXR1bmluZyB0byByZWFjaCBjb21wZXRpdGl2ZSBhY2N1cmFjeS4gRElOT3YyIGNvbWJpbmVzIERJTk8gKGdsb2JhbCBkaXNjcmltaW5hdGl2ZSkgKyBpQk9UIChwYXRjaCBkaXNjcmltaW5hdGl2ZSkgKyBTd0FWIChjbHVzdGVyIHJlZ3VsYXJpc2F0aW9uKSwgZW5zdXJpbmcgdGhlIGZyb3plbiByZXByZXNlbnRhdGlvbiBpcyBib3RoIHNwYXRpYWxseSByaWNoIGFuZCBnbG9iYWxseSBzZW1hbnRpYy4gT24gbGluZWFyIHByb2JlLCBESU5PdjItVmlULUwgZXhjZWVkcyBNQUUtVmlULUwgYnkgfjQlIG9uIEltYWdlTmV0IGFuZCBieSBsYXJnZXIgbWFyZ2lucyBvbiBkZW5zZSB0YXNrcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJESU5PdjIgdnMgUHJpb3IgTWV0aG9kcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJQcmV0cmFpbmluZyBPYmouIiwiRGF0YSIsImstTk4gVG9wLTEiLCJEZXB0aCBSTVNFICjihpMpIiwiU2VnLiBtSW9VIiwiQ2xhc3NpZmljYXRpb24gTGluZWFyIl0sInJvd3MiOltbIk1BRSBWaVQtTCIsIlBpeGVsIHJlY29uc3RydWN0aW9uIiwiSW1hZ2VOZXQtMUsiLCI1Ni41JSIsIjAuMzM5IiwiNDUuNCIsIjc1LjglIl0sWyJDTElQIFZpVC1MIiwiSW1hZ2UtdGV4dCBjb250cmFzdGl2ZSIsIkxBSU9OLTJCIiwiNzUuMyUiLCIwLjMxMiIsIjQ4LjEiLCI4NS40JSJdLFsiU3VwZXJ2aXNlZCBWaVQtTCIsIkNyb3NzLWVudHJvcHkiLCJJbWFnZU5ldC0yMksiLCLigJQiLCIwLjI5NCIsIjUzLjIiLCI4Ny4zJSJdLFsiRElOT3YyIFZpVC1MIiwiRElOTytpQk9UK1N3QVYiLCJMVkQtMTQyTSIsIjgxLjElIiwiMC4yNzEiLCI1My4wIiwiODYuNSUiXSxbIkRJTk92MiBWaVQtZyIsIkRJTk8raUJPVCtTd0FWIiwiTFZELTE0Mk0iLCI4My41JSIsIjAuMjU4IiwiNTQuOSIsIjg3LjElIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRJTk92Mi1WaVQtZyBzdXJwYXNzZXMgc3VwZXJ2aXNlZCBWaVQtTCBvbiBkZXB0aCBhbmQgbmVhcmx5IG1hdGNoZXMgaXQgb24gc2VnbWVudGF0aW9uIOKAlCB1c2luZyBvbmx5IGZyb3plbiBmZWF0dXJlcyBhbmQgYSBsaW5lYXIgaGVhZC4gVGhpcyByZXByZXNlbnRzIGEgcXVhbGl0YXRpdmUgc2hpZnQ6IGZvciBkZXBsb3ltZW50IHNjZW5hcmlvcyB3aGVyZSBmaW5lLXR1bmluZyBpcyBleHBlbnNpdmUsIERJTk92MiBwcm92aWRlcyBhIHBsdWctYW5kLXBsYXkgZmVhdHVyZSBleHRyYWN0b3IgY29tcGV0aXRpdmUgd2l0aCBzdXBlcnZpc2VkIHByZXRyYWluaW5nLiBJdHMgcHJpbWFyeSBsaW1pdGF0aW9uIGlzIHRyYWluaW5nIGNvbXB1dGU6IDY0IEExMDBzIGZvciAxNSBkYXlzIGlzIGJleW9uZCBtb3N0IHJlc2VhcmNoIGxhYnMsIHRob3VnaCBzbWFsbGVyIERJTk92MiB2YXJpYW50cyAoVmlULVMsIFZpVC1CKSBhcmUgcHJhY3RpY2FsIHRvIGRpc3RpbCBvciBmaW5lLXR1bmUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJESU5PdjIgVmlULVMvQi9ML2cgYXJlIG9wZW4tc291cmNlZCBvbiBIdWdnaW5nRmFjZSDigJQgdXNlIHRvcmNoLmh1Yi5sb2FkKFx1MDAyN2ZhY2Vib29rcmVzZWFyY2gvZGlub3YyXHUwMDI3LCBcdTAwMjdkaW5vdjJfdml0bDE0XHUwMDI3KS4iLCJmb3J3YXJkX2ZlYXR1cmVzKCkgcmV0dXJucyBib3RoIENMUyB0b2tlbiBhbmQgcGF0Y2ggdG9rZW5zIOKAlCB1c2UgcGF0Y2ggdG9rZW5zIGZvciBkZW5zZSB0YXNrcy4iLCJESU5PdjIgZmVhdHVyZXMgZ2VuZXJhbGl6ZSB0byBtZWRpY2FsIGltYWdpbmcgYW5kIHNhdGVsbGl0ZSBpbWFnZXJ5IHdpdGhvdXQgYW55IGRvbWFpbi1zcGVjaWZpYyBmaW5lLXR1bmluZy4iLCJJbmZlcmlvciB0byBmaW5lLXR1bmVkIHN1cGVydmlzZWQgbW9kZWxzIG9uIHNvbWUgdGFza3Mg4oCUIGZyb3plbiBldmFsdWF0aW9uIGlzIG5vdCB0aGUgZW5kIGdhbWUuIiwiTFZELTE0Mk0gY3VyYXRpb24gY29kZSBpcyBvcGVuLXNvdXJjZTsgdGhlIGN1cmF0ZWQgZGF0YXNldCBpdHNlbGYgaXMgbm90IGRpc3RyaWJ1dGVkIGR1ZSB0byBsaWNlbnNpbmcuIl19XQ=="
---
# DINOv2 — Curated Data and Improved SSL for Universal Features

DINOv2 (Oquab et al. 2023) asked a simple question: what happens to self-supervised visual features when you fix the data and training recipe rather than just scaling the model? The answer was striking — frozen DINOv2 features outperform supervised ViT-L on depth estimation and match it on segmentation using nothing more than a single linear layer. The key innovations are a curated 142M-image dataset (LVD-142M), the combination of DINO + iBOT + SwAV objectives, and careful stabilisation tricks that allow training ViT-g (1B parameters) to completion.

## Dataset Curation — LVD-142M

Prior self-supervised methods trained on ImageNet-1K (1.28M images) or uncurated internet crawls. DINOv2 proposes a middle path: harvest images from the internet, then aggressively filter for quality and diversity. Starting from 1.2B candidate images, the pipeline applies: (1) deduplication — remove near-duplicates using copy-detection hashing; (2) retrieval-based curation — use ImageNet-22K as seeds, retrieve nearest neighbours from the web pool using a pretrained SSL model, then threshold by similarity; (3) leakage prevention — deduplicate against downstream test sets (ImageNet val, ADE20K, etc.) to ensure fair evaluation. The result is LVD-142M: 142M high-quality, diverse, non-leaking images.

```python
import torch
import torch.nn.functional as F
import numpy as np
from sklearn.preprocessing import normalize


def extract_features_for_dedup(model, dataloader, device='cuda'):
    """Extract L2-normalised embeddings for near-duplicate detection."""
    model.eval()
    all_feats, all_ids = [], []
    with torch.no_grad():
        for imgs, ids in dataloader:
            feats = model(imgs.to(device))        # (B, D)
            feats = F.normalize(feats, dim=1)     # unit sphere
            all_feats.append(feats.cpu().numpy())
            all_ids.extend(ids)
    return np.vstack(all_feats), all_ids


def near_duplicate_removal(features, ids, threshold=0.95):
    """Remove near-duplicates: cosine-similarity > threshold.
    Returns list of retained image ids.
    Strategy: greedy — keep first occurrence, remove later duplicates.
    """
    features = normalize(features, axis=1)  # ensure unit norm
    n = len(features)
    removed = set()
    retained = []
    for i in range(n):
        if i in removed:
            continue
        retained.append(ids[i])
        # Vectorised cosine similarity: feat_i dot all_j
        sims = features[i] @ features[i+1:].T   # (n-i-1,)
        dup_offsets = np.where(sims > threshold)[0]
        for off in dup_offsets:
            removed.add(i + 1 + off)
    return retained


def quality_filter(scores, ids, min_score=0.5):
    """Keep images whose aesthetic/quality score exceeds threshold."""
    return [id_ for id_, s in zip(ids, scores) if s >= min_score]


print('Pipeline: extract -> dedup (cosine > 0.95) -> quality filter -> LVD-142M')
```

## iBOT — Masked Image Modeling with Online Tokenizer

Standard DINO predicts global CLS token representations across augmented views. iBOT (Image BERT pre-training with Online Tokenizer, Zhou et al. 2022) extends this to patch-level tokens. The teacher network generates patch-level token targets dynamically — there is no fixed discrete tokenizer (unlike BEiT, which uses a pretrained dVAE). Masked patches in the student view must match the corresponding teacher patch tokens. DINOv2 adopts iBOT's masking as an additional objective alongside the global DINO loss: L_total = L_DINO + λ·L_iBOT + μ·L_SwAV.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


def ibot_loss(student_patch_tokens, teacher_patch_tokens, mask, temp_s=0.1, temp_t=0.04):
    """iBOT masked image modeling loss.
    student_patch_tokens: (B, N, D) — student ViT patch outputs
    teacher_patch_tokens: (B, N, D) — teacher ViT patch outputs (stop-grad)
    mask: (B, N) bool — True for masked positions to predict
    """
    # Softmax-based cross-entropy in token probability space
    # Teacher provides soft targets (sharpened); student predicts from context
    s = student_patch_tokens[mask]   # (M, D) — masked positions only
    t = teacher_patch_tokens[mask]   # (M, D)

    # Compute soft targets from teacher (sinkhorn-normalised or simple softmax)
    t_probs = F.softmax(t / temp_t, dim=-1).detach()   # (M, D) soft targets
    s_log_probs = F.log_softmax(s / temp_s, dim=-1)    # (M, D)

    loss = -(t_probs * s_log_probs).sum(dim=-1).mean()
    return loss


def random_block_mask(B, N_patches, mask_ratio=0.15, device='cpu'):
    """Sample a random mask for iBOT: mask_ratio fraction of patch tokens."""
    num_mask = int(N_patches * mask_ratio)
    masks = torch.zeros(B, N_patches, dtype=torch.bool, device=device)
    for i in range(B):
        idx = torch.randperm(N_patches, device=device)[:num_mask]
        masks[i, idx] = True
    return masks


# Demo: random masked patches, random token vectors
B, N, D = 4, 196, 768   # ViT-B: 14x14=196 patches, dim=768
student_tok = torch.randn(B, N, D)
teacher_tok = torch.randn(B, N, D)
mask = random_block_mask(B, N, mask_ratio=0.15)
loss = ibot_loss(student_tok, teacher_tok, mask)
print(f'iBOT loss: {loss.item():.4f}  |  masked patches: {mask.sum().item()}')
```

## Training Objectives — DINO + iBOT + SwAV Regularizer

DINOv2 combines three complementary self-supervised objectives. DINO provides global view consistency: the student's CLS token must match the teacher's CLS token across different augmented views. iBOT provides local patch-level prediction: student patches at masked positions must predict teacher patch tokens. The SwAV regularizer (Caron et al. 2020) uses online clustering to ensure that the feature space remains uniformly spread — preventing feature collapse without relying on the batch contrastive term. The three losses are weighted and summed: L = L_DINO + 0.5·L_iBOT + 0.1·L_SwAV.

## Training Scale and Infrastructure

DINOv2-ViT-g has 1.1 billion parameters and was trained for 500K iterations on LVD-142M using 64 A100 GPUs over approximately 15 days. Stability at this scale required several techniques: stochastic depth (drop path), freezing patch projection for the first few thousand steps, gradient clipping, and Shampoo/AdamW with specific learning rate and weight decay schedules per parameter group (higher weight decay for attention parameters). Flash Attention 2 was used throughout to fit the ViT-g sequence length in memory.

- ViT-S/B/L/g backbones trained — ViT-g (1B) is the flagship model.
- AdamW with β₁=0.9, β₂=0.95, peak LR=0.001, weight decay=0.04 → 0.4 (cosine).
- Stochastic depth rate=0.4 for ViT-g to regularize the deep network.
- EMA momentum schedule: 0.994 → 1.0 (cosine over training) — teacher tracks student.
- 64× A100 80GB, ~15 days wall-clock; ViT-L trains in ~3 days on same hardware.
- Flash Attention 2 enables ViT-g at batch size 3072 without gradient checkpointing.

## Linear Probe Evaluation — Frozen Universal Features

The defining claim of DINOv2 is that its features are 'universal' — a single frozen backbone with a task-specific linear layer achieves strong performance across diverse dense prediction tasks. This is evaluated with a frozen linear probe: freeze the backbone entirely, extract CLS or patch features, train a linear layer with a standard optimizer. DINOv2-ViT-L achieves 86.5% ImageNet top-1 linear probe — 4% above MAE-ViT-L and within 1% of supervised ViT-L. On depth estimation and ADE20K segmentation the margin over MAE and CLIP is even larger.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


def build_linear_probe(feat_dim: int, num_classes: int = 1000) -> nn.Module:
    return nn.Sequential(
        nn.BatchNorm1d(feat_dim, affine=False, eps=1e-6),
        nn.Linear(feat_dim, num_classes),
    )


def run_linear_probe(backbone, probe, train_loader, val_loader,
                     epochs=20, lr=0.1, device='cuda'):
    """Freeze backbone; train linear probe only."""
    backbone.eval()
    for p in backbone.parameters():
        p.requires_grad_(False)

    optimizer = torch.optim.SGD(probe.parameters(), lr=lr,
                                momentum=0.9, weight_decay=0.0)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, epochs)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        probe.train()
        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            with torch.no_grad():
                feats = backbone(imgs)  # (B, feat_dim) — CLS token
            loss = criterion(probe(feats), labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        scheduler.step()

    # Validation
    probe.eval()
    correct = total = 0
    with torch.no_grad():
        for imgs, labels in val_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            preds = probe(backbone(imgs)).argmax(1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    return correct / total


print('DINOv2 linear probe: freeze backbone, BatchNorm + Linear head only.')
print('DINOv2-ViT-L achieves ~86.5% top-1 with this simple protocol.')
```

## Depth Estimation with Frozen DINOv2 Features

Monocular depth estimation is one of the most demanding dense prediction tasks because it requires both local spatial accuracy and global scene understanding. DINOv2 patch features (14×14 spatial grid for a 224×224 image) can be fed directly into a single linear layer trained to predict a dense depth map. This is a remarkable demonstration of feature quality: no task-specific encoder training, no decoder, just a linear map from frozen patch tokens to depth values. DINOv2-ViT-L with this protocol outperforms many specialized depth networks fine-tuned end-to-end.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class DINOv2DepthLinear(nn.Module):
    """Single linear layer depth estimator on frozen DINOv2 patch tokens."""

    def __init__(self, backbone, patch_dim: int = 1024, output_h: int = 14,
                 output_w: int = 14):
        super().__init__()
        self.backbone = backbone
        self.output_h = output_h
        self.output_w = output_w
        # Freeze backbone
        for p in self.backbone.parameters():
            p.requires_grad_(False)
        # One linear layer: patch_dim -> 1 depth value per patch
        self.depth_head = nn.Linear(patch_dim, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (B, 3, H, W) -> depth: (B, 1, H_out, W_out)."""
        with torch.no_grad():
            # DINOv2 returns dict with 'x_norm_patchtokens': (B, N_patches, D)
            out = self.backbone.forward_features(x)
            patch_tokens = out['x_norm_patchtokens']   # (B, 196, 1024) for ViT-L
        depth = self.depth_head(patch_tokens)           # (B, 196, 1)
        B, N, _ = depth.shape
        depth = depth.view(B, self.output_h, self.output_w, 1)
        depth = depth.permute(0, 3, 1, 2)               # (B, 1, H, W)
        # Upsample to input resolution
        depth = F.interpolate(depth, scale_factor=16,
                              mode='bilinear', align_corners=False)
        return depth


print('DINOv2 depth probe: single nn.Linear on patch tokens -> bilinear upsample.')
print('ViT-L patch tokens: (B, 196, 1024) for 224x224 input with 14x14 patches.')
```

> **Why DINOv2 Beats MAE on Frozen Evaluation**: MAE is optimised to reconstruct pixel values from visible patches — it never sees a discriminative signal. Its features require fine-tuning to reach competitive accuracy. DINOv2 combines DINO (global discriminative) + iBOT (patch discriminative) + SwAV (cluster regularisation), ensuring the frozen representation is both spatially rich and globally semantic. On linear probe, DINOv2-ViT-L exceeds MAE-ViT-L by ~4% on ImageNet and by larger margins on dense tasks.

## DINOv2 vs Prior Methods

| Method | Pretraining Obj. | Data | k-NN Top-1 | Depth RMSE (↓) | Seg. mIoU | Classification Linear |
| --- | --- | --- | --- | --- | --- | --- |
| MAE ViT-L | Pixel reconstruction | ImageNet-1K | 56.5% | 0.339 | 45.4 | 75.8% |
| CLIP ViT-L | Image-text contrastive | LAION-2B | 75.3% | 0.312 | 48.1 | 85.4% |
| Supervised ViT-L | Cross-entropy | ImageNet-22K | — | 0.294 | 53.2 | 87.3% |
| DINOv2 ViT-L | DINO+iBOT+SwAV | LVD-142M | 81.1% | 0.271 | 53.0 | 86.5% |
| DINOv2 ViT-g | DINO+iBOT+SwAV | LVD-142M | 83.5% | 0.258 | 54.9 | 87.1% |

DINOv2-ViT-g surpasses supervised ViT-L on depth and nearly matches it on segmentation — using only frozen features and a linear head. This represents a qualitative shift: for deployment scenarios where fine-tuning is expensive, DINOv2 provides a plug-and-play feature extractor competitive with supervised pretraining. Its primary limitation is training compute: 64 A100s for 15 days is beyond most research labs, though smaller DINOv2 variants (ViT-S, ViT-B) are practical to distil or fine-tune.

- DINOv2 ViT-S/B/L/g are open-sourced on HuggingFace — use torch.hub.load('facebookresearch/dinov2', 'dinov2_vitl14').
- forward_features() returns both CLS token and patch tokens — use patch tokens for dense tasks.
- DINOv2 features generalize to medical imaging and satellite imagery without any domain-specific fine-tuning.
- Inferior to fine-tuned supervised models on some tasks — frozen evaluation is not the end game.
- LVD-142M curation code is open-source; the curated dataset itself is not distributed due to licensing.

