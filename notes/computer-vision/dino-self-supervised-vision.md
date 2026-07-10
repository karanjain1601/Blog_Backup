---
title: "DINO: Self-Supervised Vision with Self-Distillation"
slug: "dino-self-supervised-vision"
description: "DINO trains ViT via self-distillation with no labels — student network matches teacher (EMA) predictions on differently augmented views, with centering and sharpening to prevent collapse."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJESU5PIChTZWxmLURJc3RpbGxhdGlvbiB3aXRoIE5PIGxhYmVscykgcHJldHJhaW5zIFZpc2lvbiBUcmFuc2Zvcm1lcnMgd2l0aG91dCBhbnkgbGFiZWxlZCBkYXRhLiBBIHN0dWRlbnQgbmV0d29yayBpcyB0cmFpbmVkIHRvIG1hdGNoIHRoZSBvdXRwdXQgZGlzdHJpYnV0aW9uIG9mIGEgdGVhY2hlciBuZXR3b3JrIHRoYXQgaXMgdXBkYXRlZCBhcyBhbiBleHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZSAoRU1BKSBvZiB0aGUgc3R1ZGVudCB3ZWlnaHRzLiBCb3RoIG5ldHdvcmtzIHNoYXJlIHRoZSBzYW1lIGFyY2hpdGVjdHVyZSBidXQgYXJlIGZlZCBkaWZmZXJlbnRseSBhdWdtZW50ZWQgdmlld3Mgb2YgdGhlIHNhbWUgaW1hZ2UuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJESU5PIHByb2R1Y2VzIGZlYXR1cmVzIHRoYXQgZ2VuZXJhbGl6ZSByZW1hcmthYmx5IHdlbGwg4oCUIHRoZSBDTFMgdG9rZW5cdTAwMjdzIHNlbGYtYXR0ZW50aW9uIG1hcHMgc2VnbWVudCBvYmplY3RzIHdpdGhvdXQgYW55IHN1cGVydmlzaW9uLiBJdCBicmlkZ2VzIHRoZSBnYXAgYmV0d2VlbiBzZWxmLXN1cGVydmlzZWQgYW5kIHN1cGVydmlzZWQgVmlUIHBlcmZvcm1hbmNlLCBhY2hpZXZpbmcgODAuMSUgdG9wLTEgb24gSW1hZ2VOZXQgd2l0aCBhIGxpbmVhciBwcm9iZSB1c2luZyBWaVQtQi8xNi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTZWxmLURpc3RpbGxhdGlvbiBPYmplY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjb3JlIGxvc3MgaXMgYSBjcm9zcy1lbnRyb3B5IGJldHdlZW4gdGhlIHN0dWRlbnRcdTAwMjdzIHNoYXJwZW5lZCBzb2Z0bWF4IG91dHB1dCBhbmQgdGhlIHRlYWNoZXJcdTAwMjdzIGNlbnRlcmVkLWFuZC1zaGFycGVuZWQgc29mdG1heCBvdXRwdXQuIFRoZSB0ZWFjaGVyIHRlbXBlcmF0dXJlIM+EX3QgaXMgbG93ZXIgdGhhbiB0aGUgc3R1ZGVudCB0ZW1wZXJhdHVyZSDPhF9zLCBwcm9kdWNpbmcgc2hhcnBlciAobW9yZSBjb25maWRlbnQpIHRlYWNoZXIgZGlzdHJpYnV0aW9ucyB0aGF0IGd1aWRlIHRoZSBzdHVkZW50LiBObyBleHBsaWNpdCBuZWdhdGl2ZSBwYWlycyBhcmUgbmVlZGVkIOKAlCBjb2xsYXBzZSBpcyBhdm9pZGVkIHZpYSBjZW50ZXJpbmcgYW5kIEVNQS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBkaW5vX2xvc3Moc3R1ZGVudF9vdXQsIHRlYWNoZXJfb3V0LCBzdHVkZW50X3RlbXA9MC4xLCB0ZWFjaGVyX3RlbXA9MC4wNCwgY2VudGVyPU5vbmUpOlxuICAgICMgY2VudGVyIGFuZCBzaGFycGVuIHRlYWNoZXIgb3V0cHV0XG4gICAgdGVhY2hlcl9vdXQgPSAodGVhY2hlcl9vdXQgLSBjZW50ZXIpIC8gdGVhY2hlcl90ZW1wXG4gICAgdGVhY2hlcl9wcm9icyA9IEYuc29mdG1heCh0ZWFjaGVyX291dCwgZGltPS0xKS5kZXRhY2goKVxuICAgICMgc2hhcnBlbiBzdHVkZW50XG4gICAgc3R1ZGVudF9sb2dfcHJvYnMgPSBGLmxvZ19zb2Z0bWF4KHN0dWRlbnRfb3V0IC8gc3R1ZGVudF90ZW1wLCBkaW09LTEpXG4gICAgIyBjcm9zcy1lbnRyb3B5IGxvc3NcbiAgICBsb3NzID0gLSh0ZWFjaGVyX3Byb2JzICogc3R1ZGVudF9sb2dfcHJvYnMpLnN1bShkaW09LTEpLm1lYW4oKVxuICAgIHJldHVybiBsb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc3R1ZGVudCBpcyB1cGRhdGVkIHZpYSBncmFkaWVudCBkZXNjZW50IHdoaWxlIHRoZSB0ZWFjaGVyIGlzIHVwZGF0ZWQgYXMgYW4gRU1BIG9mIHRoZSBzdHVkZW50OiDOuF90IOKGkCBtwrfOuF90ICsgKDEtbSnCt864X3MsIHdpdGggbSB0eXBpY2FsbHkgMC45OTYgcmFtcGVkIHVwIHRvIDEuMCBvdmVyIHRyYWluaW5nLiBUaGlzIHNsb3ctbW92aW5nIHRlYWNoZXIgcHJvdmlkZXMgc3RhYmxlIHRhcmdldHMgYW5kIHByZXZlbnRzIHJlcHJlc2VudGF0aW9uIGNvbGxhcHNlIHdpdGhvdXQgbmVlZGluZyBuZWdhdGl2ZSBwYWlycyBvciBzdG9wLWdyYWRpZW50IHRyaWNrcyBhbG9uZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDZW50ZXJpbmcgYW5kIFNoYXJwZW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRJTk8gcHJldmVudHMgdHdvIGRpc3RpbmN0IGNvbGxhcHNlIG1vZGVzLiBTaGFycGVuaW5nIChsb3cgdGVhY2hlciB0ZW1wZXJhdHVyZSkgYXZvaWRzIHVuaWZvcm0gY29sbGFwc2Ugd2hlcmUgYWxsIG91dHB1dHMgYXJlIGVxdWFsLiBDZW50ZXJpbmcgc3VidHJhY3RzIGEgcnVubmluZyBtZWFuIGZyb20gdGVhY2hlciBsb2dpdHMgdG8gcHJldmVudCBkb21pbmFudC1kaW1lbnNpb24gY29sbGFwc2Ugd2hlcmUgb25lIG5ldXJvbiBhbHdheXMgZmlyZXMuIFRvZ2V0aGVyIHRoZXkgZm9ybSBhIG1pbmltYWwsIGVsZWdhbnQgc3RhYmlsaXphdGlvbiBtZWNoYW5pc20gdGhhdCByZXF1aXJlcyBubyBjb250cmFzdGl2ZSBuZWdhdGl2ZXMgb3Igc3BlY2lhbGl6ZWQgYXJjaGl0ZWN0dXJlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmNsYXNzIERJTk9DZW50ZXJpbmc6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG91dF9kaW0sIG1vbWVudHVtPTAuOSk6XG4gICAgICAgIHNlbGYuY2VudGVyID0gdG9yY2guemVyb3MoMSwgb3V0X2RpbSlcbiAgICAgICAgc2VsZi5tb21lbnR1bSA9IG1vbWVudHVtXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIHVwZGF0ZShzZWxmLCB0ZWFjaGVyX291dHB1dHMpOlxuICAgICAgICAjIHRlYWNoZXJfb3V0cHV0czogW0IsIERdIGJhdGNoIG9mIHRlYWNoZXIgbG9naXRzXG4gICAgICAgIGJhdGNoX21lYW4gPSB0ZWFjaGVyX291dHB1dHMubWVhbihkaW09MCwga2VlcGRpbT1UcnVlKVxuICAgICAgICBzZWxmLmNlbnRlciA9IHNlbGYubW9tZW50dW0gKiBzZWxmLmNlbnRlciArICgxIC0gc2VsZi5tb21lbnR1bSkgKiBiYXRjaF9tZWFuXG5cbiAgICBkZWYgYXBwbHkoc2VsZiwgdGVhY2hlcl9vdXRwdXRzKTpcbiAgICAgICAgcmV0dXJuIHRlYWNoZXJfb3V0cHV0cyAtIHNlbGYuY2VudGVyIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktQ3JvcCBTdHJhdGVneSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElOTyB1c2VzIGEgbXVsdGktY3JvcCBhdWdtZW50YXRpb24gc3RyYXRlZ3k6IHR3byBnbG9iYWwgdmlld3MgYXQgMjI0w5cyMjQgcGl4ZWxzIGFuZCBzaXggbG9jYWwgdmlld3MgYXQgOTbDlzk2IHBpeGVscy4gVGhlIHN0dWRlbnQgbmV0d29yayBwcm9jZXNzZXMgYWxsIDggY3JvcHMgYW5kIGlzIHRyYWluZWQgdG8gbWF0Y2ggdGhlIHRlYWNoZXIgb24gZWFjaC4gVGhlIHRlYWNoZXIgb25seSBzZWVzIHRoZSB0d28gZ2xvYmFsIHZpZXdzLCBlbnN1cmluZyBpdCBoYXMgZnVsbCBjb250ZXh0LiBUaGlzIGxvY2FsLXRvLWdsb2JhbCBjb3JyZXNwb25kZW5jZSBmb3JjZXMgdGhlIHN0dWRlbnQgdG8gbGVhcm4gaW52YXJpYW5jZXMgYXQgbXVsdGlwbGUgc2NhbGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2h2aXNpb24udHJhbnNmb3JtcyBhcyBUXG5cbmRlZiBidWlsZF9tdWx0aWNyb3BfdHJhbnNmb3JtKGdsb2JhbF9zaXplPTIyNCwgbG9jYWxfc2l6ZT05Niwgbl9sb2NhbD02KTpcbiAgICBnbG9iYWxfdHJhbnNmb3JtID0gVC5Db21wb3NlKFtcbiAgICAgICAgVC5SYW5kb21SZXNpemVkQ3JvcChnbG9iYWxfc2l6ZSwgc2NhbGU9KDAuNCwgMS4wKSksXG4gICAgICAgIFQuUmFuZG9tSG9yaXpvbnRhbEZsaXAoKSxcbiAgICAgICAgVC5Db2xvckppdHRlcigwLjQsIDAuNCwgMC4yLCAwLjEpLFxuICAgICAgICBULlJhbmRvbUdyYXlzY2FsZShwPTAuMiksXG4gICAgICAgIFQuVG9UZW5zb3IoKSxcbiAgICAgICAgVC5Ob3JtYWxpemUoKDAuNDg1LCAwLjQ1NiwgMC40MDYpLCAoMC4yMjksIDAuMjI0LCAwLjIyNSkpLFxuICAgIF0pXG4gICAgbG9jYWxfdHJhbnNmb3JtID0gVC5Db21wb3NlKFtcbiAgICAgICAgVC5SYW5kb21SZXNpemVkQ3JvcChsb2NhbF9zaXplLCBzY2FsZT0oMC4wNSwgMC40KSksXG4gICAgICAgIFQuUmFuZG9tSG9yaXpvbnRhbEZsaXAoKSxcbiAgICAgICAgVC5Db2xvckppdHRlcigwLjQsIDAuNCwgMC4yLCAwLjEpLFxuICAgICAgICBULlRvVGVuc29yKCksXG4gICAgICAgIFQuTm9ybWFsaXplKCgwLjQ4NSwgMC40NTYsIDAuNDA2KSwgKDAuMjI5LCAwLjIyNCwgMC4yMjUpKSxcbiAgICBdKVxuICAgIHJldHVybiBnbG9iYWxfdHJhbnNmb3JtLCBsb2NhbF90cmFuc2Zvcm0sIG5fbG9jYWwifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJESU5PIEZlYXR1cmVzIGZvciBEb3duc3RyZWFtIFRhc2tzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJESU5PIGZlYXR1cmVzIHRyYW5zZmVyIHN0cm9uZ2x5IHRvIGxpbmVhciBwcm9iaW5nLCBrLU5OIGNsYXNzaWZpY2F0aW9uLCBhbmQgZGVuc2UgcHJlZGljdGlvbiB0YXNrcy4gVGhlIENMUyB0b2tlbiBmcm9tIGEgZnJvemVuIERJTk8gVmlUIGFjaGlldmVzIGNvbXBldGl0aXZlIGstTk4gYWNjdXJhY3kgd2l0aG91dCBhbnkgZmluZS10dW5pbmcuIFBhdGNoIHRva2VucyByZXRhaW4gc3BhdGlhbCBpbmZvcm1hdGlvbiB1c2VmdWwgZm9yIGRldGVjdGlvbiBhbmQgc2VnbWVudGF0aW9uLiBESU5PdjIgZXh0ZW5kcyB0aGlzIHdpdGggY3VyYXRlZCBkYXRhIGFuZCBkaXN0aWxsYXRpb24sIGZ1cnRoZXIgY2xvc2luZyB0aGUgZ2FwIHdpdGggZnVsbHkgc3VwZXJ2aXNlZCB0cmFpbmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHNrbGVhcm4ubmVpZ2hib3JzIGltcG9ydCBLTmVpZ2hib3JzQ2xhc3NpZmllclxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBrbm5fZXZhbChtb2RlbCwgdHJhaW5fbG9hZGVyLCB2YWxfbG9hZGVyLCBrPTIwKTpcbiAgICBtb2RlbC5ldmFsKClcbiAgICB0cmFpbl9mZWF0cywgdHJhaW5fbGFiZWxzID0gW10sIFtdXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZvciBpbWdzLCBsYWJlbHMgaW4gdHJhaW5fbG9hZGVyOlxuICAgICAgICAgICAgIyBleHRyYWN0IENMUyB0b2tlblxuICAgICAgICAgICAgZmVhdHMgPSBtb2RlbChpbWdzKVs6LCAwXSAgIyBbQiwgRF1cbiAgICAgICAgICAgIHRyYWluX2ZlYXRzLmFwcGVuZChmZWF0cy5jcHUoKS5udW1weSgpKVxuICAgICAgICAgICAgdHJhaW5fbGFiZWxzLmFwcGVuZChsYWJlbHMubnVtcHkoKSlcbiAgICBYX3RyYWluID0gbnAuY29uY2F0ZW5hdGUodHJhaW5fZmVhdHMpXG4gICAgeV90cmFpbiA9IG5wLmNvbmNhdGVuYXRlKHRyYWluX2xhYmVscylcbiAgICBrbm4gPSBLTmVpZ2hib3JzQ2xhc3NpZmllcihuX25laWdoYm9ycz1rLCBtZXRyaWM9XHUwMDI3Y29zaW5lXHUwMDI3KVxuICAgIGtubi5maXQoWF90cmFpbiwgeV90cmFpbilcbiAgICByZXR1cm4ga25uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiTGluZWFyIEFjYyAoJSkiLCJrLU5OIEFjYyAoJSkiLCJCYWNrYm9uZSIsIlByZXRyYWluIERhdGEiXSwicm93cyI6W1siRElOTy1TLzE2IiwiNzcuMCIsIjc0LjUiLCJWaVQtUy8xNiIsIkltYWdlTmV0LTFrIl0sWyJESU5PLUIvMTYiLCI4MC4xIiwiNzcuNCIsIlZpVC1CLzE2IiwiSW1hZ2VOZXQtMWsiXSxbIkRJTk8tQi84IiwiODMuOCIsIjgwLjEiLCJWaVQtQi84IiwiSW1hZ2VOZXQtMWsiXSxbIkRJTk92Mi1CIiwiODYuMiIsIjgzLjAiLCJWaVQtQi8xNCIsIkxWRC0xNDJNIl0sWyJESU5PdjItTCIsIjg4LjMiLCI4NS41IiwiVmlULUwvMTQiLCJMVkQtMTQyTSJdLFsiTUFFLUIiLCI2OC4wIiwi4oCUIiwiVmlULUIvMTYiLCJJbWFnZU5ldC0xayJdXX0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRfdHlwZSI6ImluZm8iLCJjb250ZW50IjoiRElOT1x1MDAyN3MgYXR0ZW50aW9uIG1hcHMgc3VycHJpc2luZ2x5IHNlZ21lbnQgb2JqZWN0cyB3aXRob3V0IGFueSBzZWdtZW50YXRpb24gc3VwZXJ2aXNpb24g4oCUIHRoZSBDTFMgdG9rZW4gYXR0ZW5kcyB0byBzZW1hbnRpY2FsbHkgbWVhbmluZ2Z1bCBmb3JlZ3JvdW5kIHJlZ2lvbnMsIGVtZXJnaW5nIGZyb20gdGhlIHNlbGYtc3VwZXJ2aXNlZCBvYmplY3RpdmUgYWxvbmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElOTyBkZW1vbnN0cmF0ZXMgdGhhdCBzZWxmLWRpc3RpbGxhdGlvbiB3aXRoIGNhcmVmdWwgY29sbGFwc2UgcHJldmVudGlvbiDigJQgY2VudGVyaW5nIGFuZCBzaGFycGVuaW5nIOKAlCBpcyBzdWZmaWNpZW50IHRvIGxlYXJuIHJpY2ggdmlzdWFsIHJlcHJlc2VudGF0aW9ucy4gVGhlIEVNQSB0ZWFjaGVyIHByb3ZpZGVzIHN0YWJsZSB0YXJnZXRzIHdpdGhvdXQgcmVxdWlyaW5nIGxhcmdlIGJhdGNoIHNpemVzIG9yIG1lbW9yeSBiYW5rcy4gTXVsdGktY3JvcCBhdWdtZW50YXRpb24gZWZmaWNpZW50bHkgc2NhbGVzIHRoZSBudW1iZXIgb2Ygdmlld3MuIERJTk8gYW5kIERJTk92MiByZW1haW4gZm91bmRhdGlvbmFsIGJhc2VsaW5lcyBmb3Igc2VsZi1zdXBlcnZpc2VkIHZpc3VhbCBwcmV0cmFpbmluZyBpbiAyMDI1LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS2V5IGRlc2lnbiBjaG9pY2VzOiAoMSkgRU1BIHRlYWNoZXIgYXZvaWRzIG1vZGUgY29sbGFwc2UgbW9yZSByb2J1c3RseSB0aGFuIHN0b3AtZ3JhZGllbnQgYWxvbmUsICgyKSBjZW50ZXJpbmcgYW5kIHNoYXJwZW5pbmcgdG9nZXRoZXIgYWRkcmVzcyBib3RoIGNvbGxhcHNlIGZhaWx1cmUgbW9kZXMsICgzKSBtdWx0aS1jcm9wIGltcHJvdmVzIGRhdGEgZWZmaWNpZW5jeSwgKDQpIG5vIG5lZ2F0aXZlIHBhaXJzIHNpbXBsaWZpZXMgdGhlIHRyYWluaW5nIHBpcGVsaW5lLiBESU5PIGZlYXR1cmVzIGV4Y2VsIGVzcGVjaWFsbHkgYXQgay1OTiB0YXNrcywgcmV2ZWFsaW5nIHRoZSBxdWFsaXR5IG9mIHRoZSBsZWFybmVkIGVtYmVkZGluZyBzcGFjZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRJTk92MiBzY2FsZXMgRElOTyB3aXRoIGN1cmF0ZWQsIGRpdmVyc2UgcHJldHJhaW5pbmcgZGF0YSBhbmQga25vd2xlZGdlIGRpc3RpbGxhdGlvbiBmcm9tIGEgbGFyZ2UgdGVhY2hlciwgYWNoaWV2aW5nIHN1cGVydmlzZWQtbGV2ZWwgcGVyZm9ybWFuY2Ugb24gbWFueSBiZW5jaG1hcmtzIHdpdGhvdXQgZmluZS10dW5pbmcuIEZvciBwcmFjdGl0aW9uZXJzLCBmcm96ZW4gRElOT3YyIGZlYXR1cmVzIHdpdGggYSBzaW1wbGUgay1OTiBvciBsaW5lYXIgaGVhZCBhcmUgYSBzdHJvbmcgYW5kIGZhc3QgYmFzZWxpbmUgZm9yIGFueSB2aXN1YWwgcmVjb2duaXRpb24gdGFzay4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlY29tbWVuZGVkIHN0YXJ0aW5nIHBvaW50OiB1c2UgdGhlIG9mZmljaWFsIERJTk8gVmlULUIvMTYgd2VpZ2h0cyBmcm9tIEZhY2Vib29rIFJlc2VhcmNoIGZvciBsaW5lYXIgcHJvYmluZyBvciBmZWF0dXJlIGV4dHJhY3Rpb24uIEZvciBwcm9kdWN0aW9uIHVzZSBjYXNlcywgRElOT3YyIFZpVC1MLzE0IHByb3ZpZGVzIHRoZSBiZXN0IGFjY3VyYWN5LXRocm91Z2hwdXQgdHJhZGVvZmYgaW4gdGhlIERJTk8gZmFtaWx5IGFuZCBpcyBhdmFpbGFibGUgdmlhIEh1Z2dpbmdGYWNlIEh1YiB3aXRoIHN0YW5kYXJkIFZpVCBpbnRlcmZhY2UgY29tcGF0aWJpbGl0eS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbW1vbiBwaXRmYWxsczogdXNpbmcgdG9vLWhpZ2ggdGVhY2hlciB0ZW1wZXJhdHVyZSAo4omlMC4xKSByZWR1Y2VzIHNoYXJwZW5pbmcgZWZmZWN0aXZlbmVzczsgbm90IHJhbXBpbmcgRU1BIG1vbWVudHVtIGZyb20gMC45OTYgdG8gMS4wIGRlc3RhYmlsaXplcyBsYXRlIHRyYWluaW5nOyBza2lwcGluZyBjZW50ZXJpbmcgd2l0aCBzbWFsbCBiYXRjaGVzIGxlYWRzIHRvIGRpbWVuc2lvbiBjb2xsYXBzZS4gQWx3YXlzIG1vbml0b3IgdGhlIHRlYWNoZXIgb3V0cHV0IGVudHJvcHkgZHVyaW5nIHRyYWluaW5nIOKAlCBhIHN1ZGRlbiBzcGlrZSBvciBjb2xsYXBzZSBpbmRpY2F0ZXMgaW5zdGFiaWxpdHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXNlYXJjaCBleHRlbnNpb25zOiBESU5PIGhhcyBiZWVuIGFkYXB0ZWQgdG8gdmlkZW8gKFZpZGVvRElOTyksIGF1ZGlvLXZpc3VhbCBsZWFybmluZywgYW5kIHBvaW50IGNsb3Vkcy4gVGhlIHNlbGYtZGlzdGlsbGF0aW9uIHBhcmFkaWdtIGFsc28gaW5zcGlyZWQgSS1KRVBBLCB3aGljaCBvcGVyYXRlcyBpbiBsYXRlbnQgc3BhY2UgcmF0aGVyIHRoYW4gcGl4ZWwgc3BhY2UuIENvbWJpbmluZyBESU5PIHdpdGggbWFza2VkIGltYWdlIG1vZGVsaW5nIChlLmcuLCBpQk9UKSB5aWVsZHMgZnVydGhlciBnYWlucyBieSBhZGRpbmcgYSBwYXRjaC1sZXZlbCBvYmplY3RpdmUgYWxvbmdzaWRlIHRoZSBnbG9iYWwgQ0xTIGRpc3RpbGxhdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV2YWx1YXRpb24gcHJvdG9jb2w6IGxpbmVhciBwcm9iaW5nIChmcmVlemUgYmFja2JvbmUsIHRyYWluIGxpbmVhciBoZWFkKSBtZWFzdXJlcyBmZWF0dXJlIHF1YWxpdHkgZm9yIGNsYXNzaWZpY2F0aW9uLiBrLU5OIGV2YWx1YXRpb24gKG5vIHRyYWluaW5nIGF0IGFsbCkgbWVhc3VyZXMgdGhlIGludHJpbnNpYyBzdHJ1Y3R1cmUgb2YgdGhlIGVtYmVkZGluZyBzcGFjZS4gU2VnbWVudGF0aW9uIHRyYW5zZmVyIChEQVZJUywgUGFzY2FsIFZPQykgbWVhc3VyZXMgc3BhdGlhbCBmZWF0dXJlIHF1YWxpdHkuIERJTk8gY29uc2lzdGVudGx5IGV4Y2VscyBvbiB0aGUgbGF0dGVyIHR3bywgbWFraW5nIGl0IGVzcGVjaWFsbHkgdXNlZnVsIGZvciBkZW5zZSB0YXNrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbXB1dGUgcmVxdWlyZW1lbnRzOiBESU5PIFZpVC1CLzE2IHByZXRyYWlucyBpbiB+MyBkYXlzIG9uIDE2IEExMDAgR1BVcyBmb3IgODAwIGVwb2NocyBvbiBJbWFnZU5ldC0xay4gVGhlIG11bHRpLWNyb3Agc3RyYXRlZ3kgaW5jcmVhc2VzIGNvbXB1dGUgYnkgfjLDlyBjb21wYXJlZCB0byBzaW5nbGUtY3JvcCBidXQgeWllbGRzIHNpZ25pZmljYW50IGFjY3VyYWN5IGdhaW5zLiBESU5PdjIgcmVxdWlyZXMgc3Vic3RhbnRpYWxseSBtb3JlIGNvbXB1dGUgYW5kIGRhdGEgYnV0IHNoaXBzIHByZXRyYWluZWQgd2VpZ2h0cywgc28gcHJhY3RpdGlvbmVycyBjYW4gdXNlIGl0IG91dCBvZiB0aGUgYm94LiJ9XQ=="
---
# DINO: Self-Supervised Vision with Self-Distillation

## Overview

DINO (Self-DIstillation with NO labels) pretrains Vision Transformers without any labeled data. A student network is trained to match the output distribution of a teacher network that is updated as an exponential moving average (EMA) of the student weights. Both networks share the same architecture but are fed differently augmented views of the same image.

DINO produces features that generalize remarkably well — the CLS token's self-attention maps segment objects without any supervision. It bridges the gap between self-supervised and supervised ViT performance, achieving 80.1% top-1 on ImageNet with a linear probe using ViT-B/16.

## Self-Distillation Objective

The core loss is a cross-entropy between the student's sharpened softmax output and the teacher's centered-and-sharpened softmax output. The teacher temperature τ_t is lower than the student temperature τ_s, producing sharper (more confident) teacher distributions that guide the student. No explicit negative pairs are needed — collapse is avoided via centering and EMA.

```python
import torch
import torch.nn.functional as F

def dino_loss(student_out, teacher_out, student_temp=0.1, teacher_temp=0.04, center=None):
    # center and sharpen teacher output
    teacher_out = (teacher_out - center) / teacher_temp
    teacher_probs = F.softmax(teacher_out, dim=-1).detach()
    # sharpen student
    student_log_probs = F.log_softmax(student_out / student_temp, dim=-1)
    # cross-entropy loss
    loss = -(teacher_probs * student_log_probs).sum(dim=-1).mean()
    return loss
```

The student is updated via gradient descent while the teacher is updated as an EMA of the student: θ_t ← m·θ_t + (1-m)·θ_s, with m typically 0.996 ramped up to 1.0 over training. This slow-moving teacher provides stable targets and prevents representation collapse without needing negative pairs or stop-gradient tricks alone.

## Centering and Sharpening

DINO prevents two distinct collapse modes. Sharpening (low teacher temperature) avoids uniform collapse where all outputs are equal. Centering subtracts a running mean from teacher logits to prevent dominant-dimension collapse where one neuron always fires. Together they form a minimal, elegant stabilization mechanism that requires no contrastive negatives or specialized architectures.

```python
import torch

class DINOCentering:
    def __init__(self, out_dim, momentum=0.9):
        self.center = torch.zeros(1, out_dim)
        self.momentum = momentum

    @torch.no_grad()
    def update(self, teacher_outputs):
        # teacher_outputs: [B, D] batch of teacher logits
        batch_mean = teacher_outputs.mean(dim=0, keepdim=True)
        self.center = self.momentum * self.center + (1 - self.momentum) * batch_mean

    def apply(self, teacher_outputs):
        return teacher_outputs - self.center
```

## Multi-Crop Strategy

DINO uses a multi-crop augmentation strategy: two global views at 224×224 pixels and six local views at 96×96 pixels. The student network processes all 8 crops and is trained to match the teacher on each. The teacher only sees the two global views, ensuring it has full context. This local-to-global correspondence forces the student to learn invariances at multiple scales.

```python
import torchvision.transforms as T

def build_multicrop_transform(global_size=224, local_size=96, n_local=6):
    global_transform = T.Compose([
        T.RandomResizedCrop(global_size, scale=(0.4, 1.0)),
        T.RandomHorizontalFlip(),
        T.ColorJitter(0.4, 0.4, 0.2, 0.1),
        T.RandomGrayscale(p=0.2),
        T.ToTensor(),
        T.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    local_transform = T.Compose([
        T.RandomResizedCrop(local_size, scale=(0.05, 0.4)),
        T.RandomHorizontalFlip(),
        T.ColorJitter(0.4, 0.4, 0.2, 0.1),
        T.ToTensor(),
        T.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    return global_transform, local_transform, n_local
```

## DINO Features for Downstream Tasks

DINO features transfer strongly to linear probing, k-NN classification, and dense prediction tasks. The CLS token from a frozen DINO ViT achieves competitive k-NN accuracy without any fine-tuning. Patch tokens retain spatial information useful for detection and segmentation. DINOv2 extends this with curated data and distillation, further closing the gap with fully supervised training.

```python
import torch
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def knn_eval(model, train_loader, val_loader, k=20):
    model.eval()
    train_feats, train_labels = [], []
    with torch.no_grad():
        for imgs, labels in train_loader:
            # extract CLS token
            feats = model(imgs)[:, 0]  # [B, D]
            train_feats.append(feats.cpu().numpy())
            train_labels.append(labels.numpy())
    X_train = np.concatenate(train_feats)
    y_train = np.concatenate(train_labels)
    knn = KNeighborsClassifier(n_neighbors=k, metric='cosine')
    knn.fit(X_train, y_train)
    return knn
```

| Model | Linear Acc (%) | k-NN Acc (%) | Backbone | Pretrain Data |
| --- | --- | --- | --- | --- |
| DINO-S/16 | 77.0 | 74.5 | ViT-S/16 | ImageNet-1k |
| DINO-B/16 | 80.1 | 77.4 | ViT-B/16 | ImageNet-1k |
| DINO-B/8 | 83.8 | 80.1 | ViT-B/8 | ImageNet-1k |
| DINOv2-B | 86.2 | 83.0 | ViT-B/14 | LVD-142M |
| DINOv2-L | 88.3 | 85.5 | ViT-L/14 | LVD-142M |
| MAE-B | 68.0 | — | ViT-B/16 | ImageNet-1k |

> ****: DINO's attention maps surprisingly segment objects without any segmentation supervision — the CLS token attends to semantically meaningful foreground regions, emerging from the self-supervised objective alone.

## Key Takeaways

DINO demonstrates that self-distillation with careful collapse prevention — centering and sharpening — is sufficient to learn rich visual representations. The EMA teacher provides stable targets without requiring large batch sizes or memory banks. Multi-crop augmentation efficiently scales the number of views. DINO and DINOv2 remain foundational baselines for self-supervised visual pretraining in 2025.

Key design choices: (1) EMA teacher avoids mode collapse more robustly than stop-gradient alone, (2) centering and sharpening together address both collapse failure modes, (3) multi-crop improves data efficiency, (4) no negative pairs simplifies the training pipeline. DINO features excel especially at k-NN tasks, revealing the quality of the learned embedding space.

DINOv2 scales DINO with curated, diverse pretraining data and knowledge distillation from a large teacher, achieving supervised-level performance on many benchmarks without fine-tuning. For practitioners, frozen DINOv2 features with a simple k-NN or linear head are a strong and fast baseline for any visual recognition task.

Recommended starting point: use the official DINO ViT-B/16 weights from Facebook Research for linear probing or feature extraction. For production use cases, DINOv2 ViT-L/14 provides the best accuracy-throughput tradeoff in the DINO family and is available via HuggingFace Hub with standard ViT interface compatibility.

Common pitfalls: using too-high teacher temperature (≥0.1) reduces sharpening effectiveness; not ramping EMA momentum from 0.996 to 1.0 destabilizes late training; skipping centering with small batches leads to dimension collapse. Always monitor the teacher output entropy during training — a sudden spike or collapse indicates instability.

Research extensions: DINO has been adapted to video (VideoDINO), audio-visual learning, and point clouds. The self-distillation paradigm also inspired I-JEPA, which operates in latent space rather than pixel space. Combining DINO with masked image modeling (e.g., iBOT) yields further gains by adding a patch-level objective alongside the global CLS distillation.

Evaluation protocol: linear probing (freeze backbone, train linear head) measures feature quality for classification. k-NN evaluation (no training at all) measures the intrinsic structure of the embedding space. Segmentation transfer (DAVIS, Pascal VOC) measures spatial feature quality. DINO consistently excels on the latter two, making it especially useful for dense tasks.

Compute requirements: DINO ViT-B/16 pretrains in ~3 days on 16 A100 GPUs for 800 epochs on ImageNet-1k. The multi-crop strategy increases compute by ~2× compared to single-crop but yields significant accuracy gains. DINOv2 requires substantially more compute and data but ships pretrained weights, so practitioners can use it out of the box.

