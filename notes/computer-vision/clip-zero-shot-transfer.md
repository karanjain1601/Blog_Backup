---
title: "CLIP Zero-Shot Transfer: Contrastive Image-Language Pretraining"
slug: "clip-zero-shot-transfer"
description: ""
tags: ["clip", "zero-shot", "contrastive-learning", "vision-language", "openai"]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDTElQIChDb250cmFzdGl2ZSBMYW5ndWFnZS1JbWFnZSBQcmV0cmFpbmluZykgaXMgYSBtb2RlbCB0cmFpbmVkIGJ5IE9wZW5BSSBvbiA0MDAgbWlsbGlvbiBpbWFnZS10ZXh0IHBhaXJzIHNjcmFwZWQgZnJvbSB0aGUgaW50ZXJuZXQuIFVubGlrZSBzdXBlcnZpc2VkIG1vZGVscyB0cmFpbmVkIG9uIGZpeGVkIGxhYmVsIHNldHMsIENMSVAgbGVhcm5zIGEgc2hhcmVkIGVtYmVkZGluZyBzcGFjZSBmb3IgaW1hZ2VzIGFuZCB0ZXh0LCBlbmFibGluZyB6ZXJvLXNob3QgdHJhbnNmZXIgdG8gYXJiaXRyYXJ5IGRvd25zdHJlYW0gdGFza3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2V5IGluc2lnaHQgaXMgbmF0dXJhbCBsYW5ndWFnZSBzdXBlcnZpc2lvbjogaW5zdGVhZCBvZiBwcmVkaWN0aW5nIGRpc2NyZXRlIGxhYmVscywgdGhlIG1vZGVsIGxlYXJucyB0byBhc3NvY2lhdGUgaW1hZ2VzIHdpdGggZnJlZS1mb3JtIHRleHQgZGVzY3JpcHRpb25zLiBBdCBpbmZlcmVuY2UgdGltZSwgY2xhc3MgbmFtZXMgYXJlIGVtYmVkZGVkIGFzIHRleHQgYW5kIGNvbXBhcmVkIGFnYWluc3QgaW1hZ2UgZW1iZWRkaW5ncyDigJQgbm8gdGFzay1zcGVjaWZpYyBmaW5lLXR1bmluZyByZXF1aXJlZC4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJjb250ZW50IjoiQ0xJUFx1MDAyN3MgemVyby1zaG90IHRyYW5zZmVyIHdvcmtzIGJlY2F1c2UgaXQgbGVhcm5zIHZpc3VhbCBjb25jZXB0cyBmcm9tIG5hdHVyYWwgbGFuZ3VhZ2Ugc3VwZXJ2aXNpb24gcmF0aGVyIHRoYW4gZml4ZWQgbGFiZWwgc2V0cy4gVGhlIGtleSBpcyB0aGUgY29udHJhc3RpdmUgb2JqZWN0aXZlIOKAlCBpdCBwdXNoZXMgbWF0Y2hpbmcgcGFpcnMgdG9nZXRoZXIgYW5kIHVubWF0Y2hlZCBwYWlycyBhcGFydCBpbiBhIHNoYXJlZCBlbWJlZGRpbmcgc3BhY2UuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDTElQIHVzZXMgdHdvIGVuY29kZXJzOiBhIFZpc2lvbiBUcmFuc2Zvcm1lciAoVmlUKSBvciBSZXNOZXQgZm9yIGltYWdlcywgYW5kIGEgVHJhbnNmb3JtZXIgZm9yIHRleHQuIEJvdGggZW5jb2RlcnMgcHJvamVjdCB0aGVpciBpbnB1dHMgaW50byBhIHNoYXJlZCA1MTItZGltZW5zaW9uYWwgZW1iZWRkaW5nIHNwYWNlLiBUaGUgdHJhaW5pbmcgc2lnbmFsIGNvbWVzIGVudGlyZWx5IGZyb20gd2hldGhlciBhbiBpbWFnZSBhbmQgdGV4dCB3ZXJlIG9yaWdpbmFsbHkgcGFpcmVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbnRyYXN0aXZlIFByZXRyYWluaW5nIE9iamVjdGl2ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvbnRyYXN0aXZlIGxvc3Mgb3BlcmF0ZXMgb24gYSBiYXRjaCBvZiBOIGltYWdlLXRleHQgcGFpcnMuIEZvciBlYWNoIGJhdGNoLCBDTElQIGNvbXB1dGVzIGFuIE7Dl04gc2ltaWxhcml0eSBtYXRyaXggYmV0d2VlbiBhbGwgaW1hZ2UgYW5kIHRleHQgZW1iZWRkaW5ncy4gVGhlIGRpYWdvbmFsIGVudHJpZXMgYXJlIHBvc2l0aXZlIHBhaXJzOyBhbGwgb2ZmLWRpYWdvbmFsIGVudHJpZXMgYXJlIG5lZ2F0aXZlcy4gVGhlIGxvc3MgbWF4aW1pemVzIGRpYWdvbmFsIHNpbWlsYXJpdHkgd2hpbGUgbWluaW1pemluZyBvZmYtZGlhZ29uYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgY2xpcF9sb3NzKGltYWdlX2ZlYXR1cmVzLCB0ZXh0X2ZlYXR1cmVzLCB0ZW1wZXJhdHVyZSk6XG4gICAgIyBOb3JtYWxpemUgZW1iZWRkaW5nc1xuICAgIGltYWdlX2ZlYXR1cmVzID0gRi5ub3JtYWxpemUoaW1hZ2VfZmVhdHVyZXMsIGRpbT0tMSlcbiAgICB0ZXh0X2ZlYXR1cmVzID0gRi5ub3JtYWxpemUodGV4dF9mZWF0dXJlcywgZGltPS0xKVxuICAgICMgU2NhbGVkIGNvc2luZSBzaW1pbGFyaXR5XG4gICAgbG9naXRzID0gaW1hZ2VfZmVhdHVyZXMgQCB0ZXh0X2ZlYXR1cmVzLlQgKiB0ZW1wZXJhdHVyZVxuICAgIEIgPSBsb2dpdHMuc2hhcGVbMF1cbiAgICBsYWJlbHMgPSB0b3JjaC5hcmFuZ2UoQiwgZGV2aWNlPWxvZ2l0cy5kZXZpY2UpXG4gICAgbG9zc19pID0gRi5jcm9zc19lbnRyb3B5KGxvZ2l0cywgbGFiZWxzKVxuICAgIGxvc3NfdCA9IEYuY3Jvc3NfZW50cm9weShsb2dpdHMuVCwgbGFiZWxzKVxuICAgIHJldHVybiAobG9zc19pICsgbG9zc190KSAvIDIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0ZW1wZXJhdHVyZSBwYXJhbWV0ZXIgKGxlYXJuZWQsIGluaXRpYWxpemVkIHRvIDAuMDcpIHNjYWxlcyB0aGUgbG9naXRzIGJlZm9yZSBzb2Z0bWF4LiBBIGxvd2VyIHRlbXBlcmF0dXJlIG1ha2VzIHRoZSBkaXN0cmlidXRpb24gcGVha2llciwgd2hpY2ggaXMgaW1wb3J0YW50IGVhcmx5IGluIHRyYWluaW5nLiBDTElQIHVzZXMgYSBzeW1tZXRyaWMgbG9zczogaXQgY2xhc3NpZmllcyBib3RoIGltYWdlcyBnaXZlbiB0ZXh0cywgYW5kIHRleHRzIGdpdmVuIGltYWdlcywgYXZlcmFnaW5nIGJvdGggY3Jvc3MtZW50cm9weSB0ZXJtcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJaZXJvLVNob3QgQ2xhc3NpZmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ilplcm8tc2hvdCBjbGFzc2lmaWNhdGlvbiB3aXRoIENMSVAgcmVxdWlyZXMgbm8gbGFiZWxlZCBleGFtcGxlcy4gQXQgaW5mZXJlbmNlIHRpbWUsIGNsYXNzIG5hbWVzIGFyZSB3cmFwcGVkIGluIGEgcHJvbXB0IHRlbXBsYXRlIChlLmcuLCBcdTAwMjdhIHBob3RvIG9mIGEge2NsYXNzfVx1MDAyNyksIGVuY29kZWQgYnkgdGhlIHRleHQgZW5jb2RlciwgYW5kIGNvbXBhcmVkIHRvIHRoZSBpbWFnZSBlbWJlZGRpbmcuIFRoZSBjbGFzcyB3aXRoIHRoZSBoaWdoZXN0IGNvc2luZSBzaW1pbGFyaXR5IGlzIHRoZSBwcmVkaWN0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgY2xpcFxuaW1wb3J0IHRvcmNoXG5cbmRlZiB6ZXJvX3Nob3RfY2xhc3NpZnkoaW1hZ2UsIGNsYXNzZXMsIG1vZGVsLCBwcmVwcm9jZXNzLCBkZXZpY2UpOlxuICAgIHRlbXBsYXRlcyA9IFtcImEgcGhvdG8gb2YgYSB7fS5cIi5mb3JtYXQoYykgZm9yIGMgaW4gY2xhc3Nlc11cbiAgICB0b2tlbnMgPSBjbGlwLnRva2VuaXplKHRlbXBsYXRlcykudG8oZGV2aWNlKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBpbWFnZV9mZWF0ID0gbW9kZWwuZW5jb2RlX2ltYWdlKHByZXByb2Nlc3MoaW1hZ2UpLnVuc3F1ZWV6ZSgwKS50byhkZXZpY2UpKVxuICAgICAgICB0ZXh0X2ZlYXQgPSBtb2RlbC5lbmNvZGVfdGV4dCh0b2tlbnMpXG4gICAgICAgIGltYWdlX2ZlYXQgPSBpbWFnZV9mZWF0IC8gaW1hZ2VfZmVhdC5ub3JtKGRpbT0tMSwga2VlcGRpbT1UcnVlKVxuICAgICAgICB0ZXh0X2ZlYXQgPSB0ZXh0X2ZlYXQgLyB0ZXh0X2ZlYXQubm9ybShkaW09LTEsIGtlZXBkaW09VHJ1ZSlcbiAgICAgICAgc2NvcmVzID0gKGltYWdlX2ZlYXQgQCB0ZXh0X2ZlYXQuVCkuc3F1ZWV6ZSgwKVxuICAgIHJldHVybiBzY29yZXMuYXJnbWF4KC0xKS5pdGVtKCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoaXMgYXBwcm9hY2ggdHJhbnNmZXJzIHRvIGFueSB0YXNrIGV4cHJlc3NpYmxlIGFzIGEgY2xhc3NpZmljYXRpb24gcHJvYmxlbSB3aXRoIG5hbWVkIGNhdGVnb3JpZXMuIENMSVAgYWNoaWV2ZXMgNzYuMiUgemVyby1zaG90IGFjY3VyYWN5IG9uIEltYWdlTmV0LTFLIHdpdGggVmlULUwvMTRAMzM2cHgg4oCUIG1hdGNoaW5nIHN1cGVydmlzZWQgUmVzTmV0LTUwIHBlcmZvcm1hbmNlIGZyb20gMjAxOSwgYnV0IHdpdGhvdXQgZXZlciBzZWVpbmcgSW1hZ2VOZXQgbGFiZWxzIGR1cmluZyB0cmFpbmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW5lYXIgUHJvYmUgdnMgWmVyby1TaG90In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMaW5lYXIgcHJvYmluZyBmcmVlemVzIHRoZSBwcmV0cmFpbmVkIGltYWdlIGVuY29kZXIgYW5kIHRyYWlucyBvbmx5IGEgbGluZWFyIGNsYXNzaWZpY2F0aW9uIGhlYWQgb24gbGFiZWxlZCBmZWF0dXJlcy4gVGhpcyByZXF1aXJlcyBsYWJlbGVkIGRhdGEgYnV0IHNpZ25pZmljYW50bHkgb3V0cGVyZm9ybXMgemVyby1zaG90IENMSVAgb24gbW9zdCBiZW5jaG1hcmtzLiBUaGUgY29tcGFyaXNvbiByZXZlYWxzIGhvdyBtdWNoIHRhc2stc3BlY2lmaWMgaW5mb3JtYXRpb24gZXhpc3RzIGluIENMSVBcdTAwMjdzIGZyb3plbiBmZWF0dXJlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGNsaXBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBMb2dpc3RpY1JlZ3Jlc3Npb25cblxuZGVmIGxpbmVhcl9wcm9iZSh0cmFpbl9sb2FkZXIsIHRlc3RfbG9hZGVyLCBtb2RlbCwgZGV2aWNlKTpcbiAgICBtb2RlbC5ldmFsKClcbiAgICBkZWYgZXh0cmFjdChsb2FkZXIpOlxuICAgICAgICBmZWF0cywgbGFiZWxzID0gW10sIFtdXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgZm9yIGltZ3MsIGxibHMgaW4gbG9hZGVyOlxuICAgICAgICAgICAgICAgIGYgPSBtb2RlbC5lbmNvZGVfaW1hZ2UoaW1ncy50byhkZXZpY2UpKVxuICAgICAgICAgICAgICAgIGZlYXRzLmFwcGVuZChmLmNwdSgpLm51bXB5KCkpXG4gICAgICAgICAgICAgICAgbGFiZWxzLmFwcGVuZChsYmxzLm51bXB5KCkpXG4gICAgICAgIHJldHVybiBucC5jb25jYXRlbmF0ZShmZWF0cyksIG5wLmNvbmNhdGVuYXRlKGxhYmVscylcbiAgICBYX3RyYWluLCB5X3RyYWluID0gZXh0cmFjdCh0cmFpbl9sb2FkZXIpXG4gICAgWF90ZXN0LCB5X3Rlc3QgPSBleHRyYWN0KHRlc3RfbG9hZGVyKVxuICAgIGNsZiA9IExvZ2lzdGljUmVncmVzc2lvbihtYXhfaXRlcj0xMDAwKS5maXQoWF90cmFpbiwgeV90cmFpbilcbiAgICByZXR1cm4gY2xmLnNjb3JlKFhfdGVzdCwgeV90ZXN0KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGluZWFyIHByb2Jpbmcgd2l0aCBDTElQIFZpVC1CLzMyIGFjaGlldmVzIDg0LjIlIG9uIEltYWdlTmV0IHZzIDYzLjIlIHplcm8tc2hvdCDigJQgYSBnYXAgb2YgMjEgcG9pbnRzLiBUaGlzIGdhcCBuYXJyb3dzIGF0IGxhcmdlciBtb2RlbCBzY2FsZXMuIE9uIHNwZWNpYWxpemVkIGRhdGFzZXRzIGxpa2UgRXVyb1NBVCAoc2F0ZWxsaXRlIGltYWdlcnkpIGFuZCBNTklTVCAoaGFuZHdyaXR0ZW4gZGlnaXRzKSwgemVyby1zaG90IHVuZGVycGVyZm9ybXMgc2lnbmlmaWNhbnRseSwgcmV2ZWFsaW5nIGRvbWFpbiBnYXBzIGluIHRyYWluaW5nIGRhdGEuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiVmlUIFZhcmlhbnQiLCJQYXJhbXMgKE0pIiwiSU4tMUsgWmVyby1TaG90ICUiLCJJTi0xSyBMaW5lYXIgUHJvYmUgJSIsIlRyYWluaW5nIERhdGEiXSwicm93cyI6W1siQ0xJUCIsIlZpVC1CLzMyIiwiMTUxIiwiNjMuMiIsIjg0LjIiLCI0MDBNIFdJVCJdLFsiQ0xJUCIsIlZpVC1CLzE2IiwiMTUwIiwiNjguMyIsIjg2LjMiLCI0MDBNIFdJVCJdLFsiQ0xJUCIsIlZpVC1MLzE0IiwiNDI4IiwiNzUuNSIsIjg3LjgiLCI0MDBNIFdJVCJdLFsiQ0xJUCIsIlZpVC1MLzE0QDMzNnB4IiwiNDI4IiwiNzYuMiIsIjg4LjMiLCI0MDBNIFdJVCJdLFsiT3BlbkNMSVAiLCJWaVQtSC8xNCIsIjk4NiIsIjc4LjAiLCI4OS4zIiwiTEFJT04tMkIiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByb21wdCBFbmdpbmVlcmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNob2ljZSBvZiB0ZXh0IHByb21wdCBzaWduaWZpY2FudGx5IGFmZmVjdHMgemVyby1zaG90IGFjY3VyYWN5LiBVc2luZyBcdTAwMjdhIHBob3RvIG9mIGEge2NsYXNzfVx1MDAyNyBvdXRwZXJmb3JtcyB1c2luZyB0aGUgcmF3IGNsYXNzIG5hbWUgYnkgYWJvdXQgMS4zJSBvbiBJbWFnZU5ldC4gTW9yZSBlbGFib3JhdGUgcHJvbXB0IGVuc2VtYmxlcyDigJQgYXZlcmFnaW5nIGVtYmVkZGluZ3MgYWNyb3NzIDgwIGRpdmVyc2UgdGVtcGxhdGVzIOKAlCB5aWVsZCBhbiBhZGRpdGlvbmFsIDMuNSUgaW1wcm92ZW1lbnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltYWdlbmV0X3RlbXBsYXRlcyA9IFtcbiAgICBcImEgcGhvdG8gb2YgYSB7fS5cIixcbiAgICBcImEgYmx1cnJ5IHBob3RvIG9mIGEge30uXCIsXG4gICAgXCJhIGJsYWNrIGFuZCB3aGl0ZSBwaG90byBvZiBhIHt9LlwiLFxuICAgIFwiYSBsb3cgY29udHJhc3QgcGhvdG8gb2YgYSB7fS5cIixcbiAgICBcImEgaGlnaCBjb250cmFzdCBwaG90byBvZiBhIHt9LlwiLFxuICAgIFwiYSBiYWQgcGhvdG8gb2YgYSB7fS5cIixcbiAgICBcImEgZ29vZCBwaG90byBvZiBhIHt9LlwiLFxuICAgIFwiYSByZW5kZXJpbmcgb2YgYSB7fS5cIixcbl1cblxuZGVmIGVuc2VtYmxlX3RleHRfZmVhdHVyZXMoY2xhc3NlcywgbW9kZWwsIHRlbXBsYXRlcywgZGV2aWNlKTpcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgY2xhc3NfZmVhdHMgPSBbXVxuICAgICAgICBmb3IgY2xzIGluIGNsYXNzZXM6XG4gICAgICAgICAgICB0b2tlbnMgPSBjbGlwLnRva2VuaXplKFt0LmZvcm1hdChjbHMpIGZvciB0IGluIHRlbXBsYXRlc10pLnRvKGRldmljZSlcbiAgICAgICAgICAgIGZlYXRzID0gbW9kZWwuZW5jb2RlX3RleHQodG9rZW5zKVxuICAgICAgICAgICAgZmVhdHMgPSBmZWF0cyAvIGZlYXRzLm5vcm0oZGltPS0xLCBrZWVwZGltPVRydWUpXG4gICAgICAgICAgICBjbGFzc19mZWF0cy5hcHBlbmQoZmVhdHMubWVhbigwKSlcbiAgICByZXR1cm4gdG9yY2guc3RhY2soY2xhc3NfZmVhdHMpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb250ZXh0IG1hdHRlcnMgYmV5b25kIGp1c3QgdGhlIGNsYXNzIG5hbWUuIFByb21wdHMgbGlrZSBcdTAwMjdhIHBob3RvIG9mIGEge2NsYXNzfSwgYSB0eXBlIG9mIHBldFx1MDAyNyBmb3IgZmluZS1ncmFpbmVkIGFuaW1hbCBjbGFzc2lmaWNhdGlvbiBvciBcdTAwMjdhIGNlbnRlcmVkIHNhdGVsbGl0ZSBwaG90byBvZiB7fVx1MDAyNyBmb3IgRXVyb1NBVCBzdWJzdGFudGlhbGx5IGltcHJvdmUgYWNjdXJhY3kuIERvbWFpbi1zcGVjaWZpYyBwcm9tcHQgZW5naW5lZXJpbmcgY2FuIGNsb3NlIG11Y2ggb2YgdGhlIGdhcCB0byBzdXBlcnZpc2VkIGJhc2VsaW5lcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDTElQIGRlbW9uc3RyYXRlZCB0aGF0IHdlYi1zY2FsZSBpbWFnZS10ZXh0IGRhdGEsIGNvbWJpbmVkIHdpdGggYSBjb250cmFzdGl2ZSBvYmplY3RpdmUsIHByb2R1Y2VzIHBvd2VyZnVsIHZpc3VhbCByZXByZXNlbnRhdGlvbnMgd2l0aG91dCB0YXNrLXNwZWNpZmljIHN1cGVydmlzaW9uLiBUaGUgbW9kZWxcdTAwMjdzIGdlbmVyYWxpdHkgaXMgaXRzIGRlZmluaW5nIHByb3BlcnR5OiBhIHNpbmdsZSB0cmFpbmVkIG1vZGVsIHRyYW5zZmVycyBjb21wZXRpdGl2ZWx5IGFjcm9zcyBkb3plbnMgb2YgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxpbWl0YXRpb25zIHJlbWFpbjogQ0xJUCBzdHJ1Z2dsZXMgd2l0aCBhYnN0cmFjdCByZWFzb25pbmcsIGNvdW50aW5nIG9iamVjdHMsIGFuZCBmaW5lLWdyYWluZWQgc3BhdGlhbCByZWxhdGlvbnNoaXBzLiBJdHMgemVyby1zaG90IHBlcmZvcm1hbmNlIG9uIGhpZ2hseSBzcGVjaWFsaXplZCBkb21haW5zIChtZWRpY2FsIGltYWdpbmcsIHNhdGVsbGl0ZSBpbWFnZXJ5KSBsYWdzIHN1cGVydmlzZWQgbW9kZWxzLiBQcm9tcHQgZW5naW5lZXJpbmcgcmVxdWlyZXMgZG9tYWluIGV4cGVydGlzZSB0byBicmlkZ2UgdGhlc2UgZ2FwcyBlZmZlY3RpdmVseS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNMSVAgYmVjYW1lIHRoZSBkZSBmYWN0byB2aXN1YWwgZW5jb2RlciBiYWNrYm9uZSBmb3Igc3Vic2VxdWVudCBtdWx0aW1vZGFsIG1vZGVscyBpbmNsdWRpbmcgREFMTC1FLCBTdGFibGUgRGlmZnVzaW9uLCBMTGFWQSwgYW5kIEJMSVAtMi4gSXRzIGNvbnRyYXN0aXZlIHByZXRyYWluaW5nIHBhcmFkaWdtIGluZmx1ZW5jZWQgdGhlIGJyb2FkZXIgZmllbGQgb2Ygc2VsZi1zdXBlcnZpc2VkIGFuZCB3ZWFrbHkgc3VwZXJ2aXNlZCByZXByZXNlbnRhdGlvbiBsZWFybmluZy4ifV0="
---
# CLIP Zero-Shot Transfer: Contrastive Image-Language Pretraining

## Overview

CLIP (Contrastive Language-Image Pretraining) is a model trained by OpenAI on 400 million image-text pairs scraped from the internet. Unlike supervised models trained on fixed label sets, CLIP learns a shared embedding space for images and text, enabling zero-shot transfer to arbitrary downstream tasks.

The key insight is natural language supervision: instead of predicting discrete labels, the model learns to associate images with free-form text descriptions. At inference time, class names are embedded as text and compared against image embeddings — no task-specific fine-tuning required.

> **info**: CLIP's zero-shot transfer works because it learns visual concepts from natural language supervision rather than fixed label sets. The key is the contrastive objective — it pushes matching pairs together and unmatched pairs apart in a shared embedding space.

CLIP uses two encoders: a Vision Transformer (ViT) or ResNet for images, and a Transformer for text. Both encoders project their inputs into a shared 512-dimensional embedding space. The training signal comes entirely from whether an image and text were originally paired.

## Contrastive Pretraining Objective

The contrastive loss operates on a batch of N image-text pairs. For each batch, CLIP computes an N×N similarity matrix between all image and text embeddings. The diagonal entries are positive pairs; all off-diagonal entries are negatives. The loss maximizes diagonal similarity while minimizing off-diagonal.

```python
import torch
import torch.nn.functional as F

def clip_loss(image_features, text_features, temperature):
    # Normalize embeddings
    image_features = F.normalize(image_features, dim=-1)
    text_features = F.normalize(text_features, dim=-1)
    # Scaled cosine similarity
    logits = image_features @ text_features.T * temperature
    B = logits.shape[0]
    labels = torch.arange(B, device=logits.device)
    loss_i = F.cross_entropy(logits, labels)
    loss_t = F.cross_entropy(logits.T, labels)
    return (loss_i + loss_t) / 2
```

The temperature parameter (learned, initialized to 0.07) scales the logits before softmax. A lower temperature makes the distribution peakier, which is important early in training. CLIP uses a symmetric loss: it classifies both images given texts, and texts given images, averaging both cross-entropy terms.

## Zero-Shot Classification

Zero-shot classification with CLIP requires no labeled examples. At inference time, class names are wrapped in a prompt template (e.g., 'a photo of a {class}'), encoded by the text encoder, and compared to the image embedding. The class with the highest cosine similarity is the prediction.

```python
import clip
import torch

def zero_shot_classify(image, classes, model, preprocess, device):
    templates = ["a photo of a {}.".format(c) for c in classes]
    tokens = clip.tokenize(templates).to(device)
    with torch.no_grad():
        image_feat = model.encode_image(preprocess(image).unsqueeze(0).to(device))
        text_feat = model.encode_text(tokens)
        image_feat = image_feat / image_feat.norm(dim=-1, keepdim=True)
        text_feat = text_feat / text_feat.norm(dim=-1, keepdim=True)
        scores = (image_feat @ text_feat.T).squeeze(0)
    return scores.argmax(-1).item()
```

This approach transfers to any task expressible as a classification problem with named categories. CLIP achieves 76.2% zero-shot accuracy on ImageNet-1K with ViT-L/14@336px — matching supervised ResNet-50 performance from 2019, but without ever seeing ImageNet labels during training.

## Linear Probe vs Zero-Shot

Linear probing freezes the pretrained image encoder and trains only a linear classification head on labeled features. This requires labeled data but significantly outperforms zero-shot CLIP on most benchmarks. The comparison reveals how much task-specific information exists in CLIP's frozen features.

```python
import clip
import torch
import numpy as np
from sklearn.linear_model import LogisticRegression

def linear_probe(train_loader, test_loader, model, device):
    model.eval()
    def extract(loader):
        feats, labels = [], []
        with torch.no_grad():
            for imgs, lbls in loader:
                f = model.encode_image(imgs.to(device))
                feats.append(f.cpu().numpy())
                labels.append(lbls.numpy())
        return np.concatenate(feats), np.concatenate(labels)
    X_train, y_train = extract(train_loader)
    X_test, y_test = extract(test_loader)
    clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    return clf.score(X_test, y_test)
```

Linear probing with CLIP ViT-B/32 achieves 84.2% on ImageNet vs 63.2% zero-shot — a gap of 21 points. This gap narrows at larger model scales. On specialized datasets like EuroSAT (satellite imagery) and MNIST (handwritten digits), zero-shot underperforms significantly, revealing domain gaps in training data.

| Model | ViT Variant | Params (M) | IN-1K Zero-Shot % | IN-1K Linear Probe % | Training Data |
| --- | --- | --- | --- | --- | --- |
| CLIP | ViT-B/32 | 151 | 63.2 | 84.2 | 400M WIT |
| CLIP | ViT-B/16 | 150 | 68.3 | 86.3 | 400M WIT |
| CLIP | ViT-L/14 | 428 | 75.5 | 87.8 | 400M WIT |
| CLIP | ViT-L/14@336px | 428 | 76.2 | 88.3 | 400M WIT |
| OpenCLIP | ViT-H/14 | 986 | 78.0 | 89.3 | LAION-2B |

## Prompt Engineering

The choice of text prompt significantly affects zero-shot accuracy. Using 'a photo of a {class}' outperforms using the raw class name by about 1.3% on ImageNet. More elaborate prompt ensembles — averaging embeddings across 80 diverse templates — yield an additional 3.5% improvement.

```python
imagenet_templates = [
    "a photo of a {}.",
    "a blurry photo of a {}.",
    "a black and white photo of a {}.",
    "a low contrast photo of a {}.",
    "a high contrast photo of a {}.",
    "a bad photo of a {}.",
    "a good photo of a {}.",
    "a rendering of a {}.",
]

def ensemble_text_features(classes, model, templates, device):
    with torch.no_grad():
        class_feats = []
        for cls in classes:
            tokens = clip.tokenize([t.format(cls) for t in templates]).to(device)
            feats = model.encode_text(tokens)
            feats = feats / feats.norm(dim=-1, keepdim=True)
            class_feats.append(feats.mean(0))
    return torch.stack(class_feats)
```

Context matters beyond just the class name. Prompts like 'a photo of a {class}, a type of pet' for fine-grained animal classification or 'a centered satellite photo of {}' for EuroSAT substantially improve accuracy. Domain-specific prompt engineering can close much of the gap to supervised baselines.

## Key Takeaways

CLIP demonstrated that web-scale image-text data, combined with a contrastive objective, produces powerful visual representations without task-specific supervision. The model's generality is its defining property: a single trained model transfers competitively across dozens of benchmarks.

Limitations remain: CLIP struggles with abstract reasoning, counting objects, and fine-grained spatial relationships. Its zero-shot performance on highly specialized domains (medical imaging, satellite imagery) lags supervised models. Prompt engineering requires domain expertise to bridge these gaps effectively.

CLIP became the de facto visual encoder backbone for subsequent multimodal models including DALL-E, Stable Diffusion, LLaVA, and BLIP-2. Its contrastive pretraining paradigm influenced the broader field of self-supervised and weakly supervised representation learning.

