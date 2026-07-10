---
title: "DINO — Self-Distillation Without Labels"
slug: "dino-self-distillation"
description: "How DINO (Caron et al. 2021) uses a student-teacher self-distillation framework with EMA weight updates, multi-crop training, centering and sharpening for collapse prevention, and emergent attention-based segmentation."
tags: ["deep-learning", "self-supervised-learning", "masked-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElOTyAoU2VsZi1ESXN0aWxsYXRpb24gd2l0aCBOTyBsYWJlbHMpIGJ5IENhcm9uIGV0IGFsLiAoMjAyMSkgc2hvd2VkIHRoYXQgc2VsZi1zdXBlcnZpc2VkIFZpVCBmZWF0dXJlcyB0cmFpbmVkIHdpdGgga25vd2xlZGdlIGRpc3RpbGxhdGlvbiBiZXR3ZWVuIGEgc3R1ZGVudCBhbmQgYW4gRU1BIHRlYWNoZXIgZGV2ZWxvcCBlbWVyZ2VudCBwcm9wZXJ0aWVzIGFic2VudCBpbiBzdXBlcnZpc2VkIG1vZGVscyDigJQgbW9zdCBzdHJpa2luZ2x5LCBhdHRlbnRpb24gbWFwcyB0aGF0IGFsaWduIHByZWNpc2VseSB3aXRoIHNlbWFudGljIG9iamVjdCBib3VuZGFyaWVzIHdpdGhvdXQgZXZlciBzZWVpbmcgYSBzZWdtZW50YXRpb24gbGFiZWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VsZi1EaXN0aWxsYXRpb24gQ29uY2VwdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElOTyB1c2VzIGEgc3R1ZGVudC10ZWFjaGVyIGZyYW1ld29yayB3aGVyZSBib3RoIG5ldHdvcmtzIHNoYXJlIHRoZSBzYW1lIFZpVCBhcmNoaXRlY3R1cmUuIFRoZSB0ZWFjaGVyIGlzIGFuIGV4cG9uZW50aWFsIG1vdmluZyBhdmVyYWdlIChFTUEpIG9mIHRoZSBzdHVkZW50XHUwMDI3cyB3ZWlnaHRzIOKAlCBpdCBuZXZlciByZWNlaXZlcyBncmFkaWVudHMgZGlyZWN0bHkuIFRoZSBzdHVkZW50IGlzIHRyYWluZWQgdG8gcHJlZGljdCB0aGUgdGVhY2hlclx1MDAyN3Mgb3V0cHV0IGRpc3RyaWJ1dGlvbiBmb3IgZGlmZmVyZW50IGF1Z21lbnRlZCB2aWV3cyBvZiB0aGUgc2FtZSBpbWFnZS4gQmVjYXVzZSB0aGUgdGVhY2hlciBpcyBhIHNtb290aGVkIHZlcnNpb24gb2YgdGhlIHN0dWRlbnQsIHRoaXMgaXMgY2FsbGVkIHNlbGYtZGlzdGlsbGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRlYWNoZXIgRU1BIFVwZGF0ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRlYWNoZXJcdTAwMjdzIHBhcmFtZXRlcnMgYXJlIHVwZGF0ZWQgdmlhIEVNQSB3aXRoIGEgbW9tZW50dW0gY29lZmZpY2llbnQgbSB0aGF0IGlzIGFubmVhbGVkIGZyb20gMC45OTYgdG93YXJkIDEuMCBkdXJpbmcgdHJhaW5pbmcgdXNpbmcgYSBjb3NpbmUgc2NoZWR1bGUuIEhpZ2hlciBtb21lbnR1bSAobSDihpIgMS4wKSBtZWFucyB0aGUgdGVhY2hlciBjaGFuZ2VzIG1vcmUgc2xvd2x5IOKAlCBwcm92aWRpbmcgYSBzdGFibGUgdHJhaW5pbmcgdGFyZ2V0LiBUaGUgc3R1ZGVudCBpcyB1cGRhdGVkIHZpYSBzdGFuZGFyZCBncmFkaWVudCBkZXNjZW50OyB0aGUgdGVhY2hlciByZWNlaXZlcyBubyBncmFkaWVudCBzaWduYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBjb3B5XG5cbmNsYXNzIERJTk9UZWFjaGVyVXBkYXRlcjpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgc3R1ZGVudCwgdGVhY2hlciwgYmFzZV9tb21lbnR1bT0wLjk5Nik6XG4gICAgICAgIHNlbGYuc3R1ZGVudCAgICAgICA9IHN0dWRlbnRcbiAgICAgICAgc2VsZi50ZWFjaGVyICAgICAgID0gdGVhY2hlclxuICAgICAgICBzZWxmLmJhc2VfbW9tZW50dW0gPSBiYXNlX21vbWVudHVtXG4gICAgICAgICMgSW5pdGlhbGl6ZSB0ZWFjaGVyIGZyb20gc3R1ZGVudCB3ZWlnaHRzOyBkaXNhYmxlIGdyYWRpZW50c1xuICAgICAgICBzZWxmLnRlYWNoZXIubG9hZF9zdGF0ZV9kaWN0KHN0dWRlbnQuc3RhdGVfZGljdCgpKVxuICAgICAgICBmb3IgcCBpbiBzZWxmLnRlYWNoZXIucGFyYW1ldGVycygpOlxuICAgICAgICAgICAgcC5yZXF1aXJlc19ncmFkXyhGYWxzZSlcblxuICAgIGRlZiB1cGRhdGUoc2VsZiwgZXBvY2gsIG1heF9lcG9jaHMpOlxuICAgICAgICAjIE1vbWVudHVtIGluY3JlYXNlcyBmcm9tIGJhc2VfbW9tZW50dW0gdG8gMS4wIHZpYSBjb3NpbmUgc2NoZWR1bGVcbiAgICAgICAgbSA9IDEuMCAtICgxLjAgLSBzZWxmLmJhc2VfbW9tZW50dW0pICogKFxuICAgICAgICAgICAgbnAuY29zKG5wLnBpICogZXBvY2ggLyBtYXhfZXBvY2hzKSArIDEuMFxuICAgICAgICApIC8gMi4wXG5cbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICBmb3Igc19wLCB0X3AgaW4gemlwKFxuICAgICAgICAgICAgICAgIHNlbGYuc3R1ZGVudC5wYXJhbWV0ZXJzKCksIHNlbGYudGVhY2hlci5wYXJhbWV0ZXJzKClcbiAgICAgICAgICAgICk6XG4gICAgICAgICAgICAgICAgdF9wLmRhdGEubXVsXyhtKS5hZGRfKCgxLjAgLSBtKSAqIHNfcC5kYXRhKVxuXG4gICAgQHRvcmNoLm5vX2dyYWQoKVxuICAgIGRlZiBoYXJkX2NvcHkoc2VsZik6XG4gICAgICAgICMgQ29weSBzdHVkZW50IHdlaWdodHMgZGlyZWN0bHkgdG8gdGVhY2hlciAodXNlZCBhdCBpbml0aWFsaXphdGlvbilcbiAgICAgICAgZm9yIHNfcCwgdF9wIGluIHppcChcbiAgICAgICAgICAgIHNlbGYuc3R1ZGVudC5wYXJhbWV0ZXJzKCksIHNlbGYudGVhY2hlci5wYXJhbWV0ZXJzKClcbiAgICAgICAgKTpcbiAgICAgICAgICAgIHRfcC5kYXRhLmNvcHlfKHNfcC5kYXRhKVxuXG4jIEV4YW1wbGU6IHVwZGF0ZSB0ZWFjaGVyIGFmdGVyIGVhY2ggb3B0aW1pemVyIHN0ZXBcbiMgdXBkYXRlciA9IERJTk9UZWFjaGVyVXBkYXRlcihzdHVkZW50LCB0ZWFjaGVyKVxuIyBmb3IgZXBvY2ggaW4gcmFuZ2UobWF4X2Vwb2Nocyk6XG4jICAgICAuLi4gdHJhaW4gc3R1ZGVudCAuLi5cbiMgICAgIHVwZGF0ZXIudXBkYXRlKGVwb2NoLCBtYXhfZXBvY2hzKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNlbnRlcmluZyBhbmQgU2hhcnBlbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aG91dCBhbnkgY29sbGFwc2UgcHJldmVudGlvbiwgc2VsZi1kaXN0aWxsYXRpb24gcXVpY2tseSBjb2xsYXBzZXMgdG8gYSB0cml2aWFsIHNvbHV0aW9uIHdoZXJlIGJvdGggc3R1ZGVudCBhbmQgdGVhY2hlciBvdXRwdXQgYSBjb25zdGFudCBkaXN0cmlidXRpb24uIERJTk8gdXNlcyB0d28gY29tcGxlbWVudGFyeSBtZWNoYW5pc21zOiBjZW50ZXJpbmcgKHN1YnRyYWN0IGEgcnVubmluZyBtZWFuIGZyb20gdGVhY2hlciBsb2dpdHMgdG8gcHJldmVudCBvbmUgZGltZW5zaW9uIGZyb20gZG9taW5hdGluZykgYW5kIHNoYXJwZW5pbmcgKGxvdyB0ZW1wZXJhdHVyZSBvbiB0aGUgdGVhY2hlciB0byBwcm9kdWNlIHBlYWtlZCBkaXN0cmlidXRpb25zIHRoYXQgY2FycnkgYSBtZWFuaW5nZnVsIHRyYWluaW5nIHNpZ25hbCkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIERJTk9IZWFkKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2RpbSwgb3V0X2RpbT02NTUzNiwgY2VudGVyX21vbWVudHVtPTAuOSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm1scCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoaW5fZGltLCAyMDQ4KSwgbm4uR0VMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDIwNDgsIDIwNDgpLCBubi5HRUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoMjA0OCwgb3V0X2RpbSwgYmlhcz1GYWxzZSlcbiAgICAgICAgKVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdjZW50ZXJcdTAwMjcsIHRvcmNoLnplcm9zKDEsIG91dF9kaW0pKVxuICAgICAgICBzZWxmLmNlbnRlcl9tb21lbnR1bSA9IGNlbnRlcl9tb21lbnR1bVxuXG4gICAgQHRvcmNoLm5vX2dyYWQoKVxuICAgIGRlZiB1cGRhdGVfY2VudGVyKHNlbGYsIHRlYWNoZXJfb3V0cHV0KTpcbiAgICAgICAgIyBFTUEgdXBkYXRlOiBzdWJ0cmFjdCBydW5uaW5nIG1lYW4gdG8gcHJldmVudCBtb2RlIGNvbGxhcHNlXG4gICAgICAgIGJhdGNoX2NlbnRlciA9IHRlYWNoZXJfb3V0cHV0Lm1lYW4oZGltPTAsIGtlZXBkaW09VHJ1ZSlcbiAgICAgICAgc2VsZi5jZW50ZXIgPSAoXG4gICAgICAgICAgICBzZWxmLmNlbnRlciAqIHNlbGYuY2VudGVyX21vbWVudHVtXG4gICAgICAgICAgICArIGJhdGNoX2NlbnRlciAqICgxIC0gc2VsZi5jZW50ZXJfbW9tZW50dW0pXG4gICAgICAgIClcblxuICAgIGRlZiB0ZWFjaGVyX3NvZnRtYXgoc2VsZiwgeCwgdGVtcD0wLjA0KTpcbiAgICAgICAgIyBTdWJ0cmFjdCBjZW50ZXIsIGFwcGx5IGxvdyB0ZW1wZXJhdHVyZSAtXHUwMDNlIHNoYXJwIHBlYWtlZCBkaXN0cmlidXRpb25cbiAgICAgICAgcmV0dXJuIEYuc29mdG1heCgoeCAtIHNlbGYuY2VudGVyKSAvIHRlbXAsIGRpbT0tMSlcblxuICAgIGRlZiBzdHVkZW50X2xvZ19zb2Z0bWF4KHNlbGYsIHgsIHRlbXA9MC4xKTpcbiAgICAgICAgIyBIaWdoZXIgdGVtcGVyYXR1cmUgZm9yIHN0dWRlbnQgLVx1MDAzZSBzb2Z0ZXIgZGlzdHJpYnV0aW9uXG4gICAgICAgIHJldHVybiBGLmxvZ19zb2Z0bWF4KHggLyB0ZW1wLCBkaW09LTEpXG5cbiAgICBkZWYgZGlub19sb3NzKHNlbGYsIHN0dWRlbnRfb3V0LCB0ZWFjaGVyX291dCk6XG4gICAgICAgICMgQ3Jvc3MtZW50cm9weSBIKHRlYWNoZXJfc2hhcnAsIHN0dWRlbnQpOiBzdHVkZW50IHByZWRpY3RzIHRlYWNoZXJcbiAgICAgICAgdF9wcm9icyAgPSBzZWxmLnRlYWNoZXJfc29mdG1heCh0ZWFjaGVyX291dClcbiAgICAgICAgc19sb2dwICAgPSBzZWxmLnN0dWRlbnRfbG9nX3NvZnRtYXgoc3R1ZGVudF9vdXQpXG4gICAgICAgIHJldHVybiAtKHRfcHJvYnMgKiBzX2xvZ3ApLnN1bShkaW09LTEpLm1lYW4oKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQ29sbGFwc2UgUHJldmVudGlvbiBpcyBDcml0aWNhbCIsImNvbnRlbnQiOiJXaXRob3V0IGNlbnRlcmluZyArIHNoYXJwZW5pbmcsIERJTk8gY29sbGFwc2VzIHdpdGhpbiB0aGUgZmlyc3QgZmV3IHRob3VzYW5kIGl0ZXJhdGlvbnM6IHRoZSB0ZWFjaGVyIG91dHB1dHMgYSB1bmlmb3JtIGRpc3RyaWJ1dGlvbiAoYWxsIGltYWdlcyBtYXAgdG8gdGhlIHNhbWUgcmVwcmVzZW50YXRpb24pLiBDZW50ZXJpbmcgcHJldmVudHMgYW55IHNpbmdsZSBkaW1lbnNpb24gZnJvbSBkb21pbmF0aW5nLiBTaGFycGVuaW5nIChsb3cgdGVhY2hlciB0ZW1wZXJhdHVyZSDPhF90ID0gMC4wNCkgZW5zdXJlcyB0aGUgdGVhY2hlciBvdXRwdXRzIHBlYWtlZCBkaXN0cmlidXRpb25zLCBnaXZpbmcgdGhlIHN0dWRlbnQgYSBtZWFuaW5nZnVsIHRhcmdldCB0byBtYXRjaC4gQm90aCBhcmUgcmVxdWlyZWQg4oCUIGNlbnRlcmluZyBhbG9uZSBzdGlsbCBhbGxvd3MgY29sbGFwc2UgdG8gYSB1bmlmb3JtIGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1Dcm9wIFRyYWluaW5nIFN0cmF0ZWd5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJESU5PIHVzZXMgYSBtdWx0aS1jcm9wIGF1Z21lbnRhdGlvbiBzdHJhdGVneTogZ2VuZXJhdGUgMiBnbG9iYWwgY3JvcHMgKFx1MDAzZTUwJSBvZiBpbWFnZSBhcmVhKSBhbmQgNuKAkzggbG9jYWwgY3JvcHMgKFx1MDAzYzUwJSBhcmVhKS4gVGhlIHRlYWNoZXIgc2VlcyBvbmx5IHRoZSAyIGdsb2JhbCBjcm9wczsgdGhlIHN0dWRlbnQgc2VlcyBhbGwgY3JvcHMuIFRoZSBsb3NzIGlzIGNvbXB1dGVkIGFzIHRoZSBjcm9zcy1lbnRyb3B5IGZyb20gZWFjaCBzdHVkZW50IG91dHB1dCB0byBlYWNoIHRlYWNoZXIgb3V0cHV0IChsb2NhbOKGkmdsb2JhbCBtYXRjaGluZykuIFRoaXMgdGVhY2hlcyB0aGUgc3R1ZGVudCB0byBwcmVkaWN0IGdsb2JhbCBjb250ZXh0IGZyb20gbG9jYWwgdmlld3MsIGZvcmNpbmcgc2VtYW50aWMgZmVhdHVyZSBsZWFybmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaHZpc2lvbi50cmFuc2Zvcm1zIGFzIFRcblxuY2xhc3MgTXVsdGlDcm9wV3JhcHBlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBiYWNrYm9uZSwgaGVhZCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmJhY2tib25lID0gYmFja2JvbmVcbiAgICAgICAgc2VsZi5oZWFkICAgICA9IGhlYWRcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGNyb3BzKTpcbiAgICAgICAgIyBCYXRjaCBhbGwgY3JvcHMgdG9nZXRoZXIgZm9yIGEgc2luZ2xlIGVmZmljaWVudCBmb3J3YXJkIHBhc3NcbiAgICAgICAgYWxsX2Nyb3BzID0gdG9yY2guY2F0KGNyb3BzLCBkaW09MCkgICAgICAgICAgICMgW3N1bShCKSwgQywgSCwgV11cbiAgICAgICAgZmVhdHVyZXMgID0gc2VsZi5iYWNrYm9uZShhbGxfY3JvcHMpICAgICAgICAgICMgW3N1bShCKSwgRF1cbiAgICAgICAgb3V0cHV0ICAgID0gc2VsZi5oZWFkLm1scChmZWF0dXJlcykgICAgICAgICAgICMgW3N1bShCKSwgb3V0X2RpbV1cbiAgICAgICAgIyBTcGxpdCBiYWNrIGludG8gcGVyLWNyb3AgY2h1bmtzXG4gICAgICAgIHJldHVybiBvdXRwdXQuc3BsaXQoW2Muc2hhcGVbMF0gZm9yIGMgaW4gY3JvcHNdLCBkaW09MClcblxuZGVmIGRpbm9fdHJhaW5fc3RlcChzdHVkZW50X25ldCwgdGVhY2hlcl9uZXQsIGhlYWQsIG9wdGltaXplcixcbiAgICAgICAgICAgICAgICAgICAgIGdsb2JhbF9jcm9wcywgbG9jYWxfY3JvcHMpOlxuICAgICMgVGVhY2hlciBmb3J3YXJkIG9uIGdsb2JhbCBjcm9wcyBvbmx5IChubyBncmFkaWVudHMpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHRfb3V0cyA9IFt0ZWFjaGVyX25ldChnYykgZm9yIGdjIGluIGdsb2JhbF9jcm9wc11cblxuICAgICMgU3R1ZGVudCBmb3J3YXJkIG9uIEFMTCBjcm9wcyAoZ2xvYmFsICsgbG9jYWwpXG4gICAgYWxsX2Nyb3BzID0gZ2xvYmFsX2Nyb3BzICsgbG9jYWxfY3JvcHNcbiAgICBzX291dHMgICAgPSBbc3R1ZGVudF9uZXQoYykgZm9yIGMgaW4gYWxsX2Nyb3BzXVxuXG4gICAgIyBMb3NzOiBlYWNoIHN0dWRlbnQgY3JvcCBwcmVkaWN0cyBlYWNoIHRlYWNoZXIgY3JvcFx1MDAyN3MgZGlzdHJpYnV0aW9uXG4gICAgbG9zcyAgID0gdG9yY2gudGVuc29yKDAuMClcbiAgICBuX3BhaXJzID0gMFxuICAgIGZvciBzX291dCBpbiBzX291dHM6XG4gICAgICAgIGZvciB0X291dCBpbiB0X291dHM6XG4gICAgICAgICAgICBsb3NzID0gbG9zcyArIGhlYWQuZGlub19sb3NzKHNfb3V0LCB0X291dClcbiAgICAgICAgICAgIG5fcGFpcnMgKz0gMVxuICAgIGxvc3MgPSBsb3NzIC8gbl9wYWlyc1xuXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgbm4udXRpbHMuY2xpcF9ncmFkX25vcm1fKHN0dWRlbnRfbmV0LnBhcmFtZXRlcnMoKSwgMy4wKVxuICAgIG9wdGltaXplci5zdGVwKClcbiAgICBoZWFkLnVwZGF0ZV9jZW50ZXIodG9yY2guY2F0KHRfb3V0cykuZGV0YWNoKCkpXG4gICAgcmV0dXJuIGxvc3MuaXRlbSgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRElOTyBBdHRlbnRpb24gTWFwcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1vc3Qgc3RyaWtpbmcgZW1lcmdlbnQgcHJvcGVydHkgb2YgRElOTy1wcmV0cmFpbmVkIFZpVHMgaXMgdGhhdCB0aGUgc2VsZi1hdHRlbnRpb24gbWFwcyBpbiB0aGUgbGFzdCB0cmFuc2Zvcm1lciBibG9jayBhbGlnbiBjbG9zZWx5IHdpdGggc2VtYW50aWMgb2JqZWN0IG1hc2tzIOKAlCBkZXNwaXRlIG5vIHNlZ21lbnRhdGlvbiBzdXBlcnZpc2lvbi4gRWFjaCBhdHRlbnRpb24gaGVhZCBhdHRlbmRzIHRvIGRpZmZlcmVudCBvYmplY3QgcGFydHMuIEJ5IHRocmVzaG9sZGluZyB0aGUgQ0xTLXRvLXBhdGNoIGF0dGVudGlvbiwgb25lIG9idGFpbnMgbmVhci1ncm91bmQtdHJ1dGggb2JqZWN0IG1hc2tzIGZyb20gYSBtb2RlbCB0cmFpbmVkIG9ubHkgd2l0aCBpbWFnZS1sZXZlbCBzZWxmLXN1cGVydmlzaW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgZXh0cmFjdF9kaW5vX2F0dGVudGlvbihtb2RlbCwgaW1nLCBwYXRjaF9zaXplPTgsIHRocmVzaG9sZF9wY3Q9NjApOlxuICAgICMgRXh0cmFjdCBDTFMtXHUwMDNlcGF0Y2ggc2VsZi1hdHRlbnRpb24gZnJvbSB0aGUgbGFzdCBWaVQgYmxvY2tcbiAgICBtb2RlbC5ldmFsKClcbiAgICBhdHRuX3N0b3JlID0ge31cblxuICAgIGRlZiBob29rX2ZuKG1vZHVsZSwgaW5wLCBvdXQpOlxuICAgICAgICAjIE11bHRpaGVhZEF0dGVudGlvbiByZXR1cm5zIChvdXRwdXQsIGF0dG5fd2VpZ2h0cykgd2hlbiBuZWVkX3dlaWdodHM9VHJ1ZVxuICAgICAgICBhdHRuX3N0b3JlW1x1MDAyN2F0dG5cdTAwMjddID0gb3V0WzFdXG5cbiAgICBoYW5kbGUgPSBtb2RlbC5ibG9ja3NbLTFdLmF0dG4ucmVnaXN0ZXJfZm9yd2FyZF9ob29rKGhvb2tfZm4pXG5cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgXyA9IG1vZGVsKGltZy51bnNxdWVlemUoMCkpXG4gICAgaGFuZGxlLnJlbW92ZSgpXG5cbiAgICAjIGF0dG46IFsxLCBudW1faGVhZHMsIE4rMSwgTisxXSAtXHUwMDNlIENMUyByb3cgLVx1MDAzZSBbbnVtX2hlYWRzLCBOXVxuICAgIGF0dG4gPSBhdHRuX3N0b3JlW1x1MDAyN2F0dG5cdTAwMjddWzAsIDosIDAsIDE6XSAgIyByZW1vdmUgY2xzLXRvLWNsc1xuICAgIGggPSB3ID0gaW50KGF0dG4uc2hhcGVbLTFdICoqIDAuNSlcbiAgICBhdHRuID0gYXR0bi5yZXNoYXBlKC0xLCAxLCBoLCB3KSAgICAgICAgIyBbbnVtX2hlYWRzLCAxLCBoLCB3XVxuXG4gICAgIyBVcHNhbXBsZSB0byBvcmlnaW5hbCBpbWFnZSByZXNvbHV0aW9uXG4gICAgaW1nX2gsIGltZ193ID0gaW1nLnNoYXBlWy0yXSwgaW1nLnNoYXBlWy0xXVxuICAgIGF0dG5fdXAgPSBGLmludGVycG9sYXRlKGF0dG4sIHNpemU9KGltZ19oLCBpbWdfdyksIG1vZGU9XHUwMDI3YmlsaW5lYXJcdTAwMjcsIGFsaWduX2Nvcm5lcnM9RmFsc2UpXG4gICAgYXR0bl91cCA9IGF0dG5fdXAuc3F1ZWV6ZSgxKS5jcHUoKS5udW1weSgpICAjIFtudW1faGVhZHMsIEgsIFddXG5cbiAgICAjIFRocmVzaG9sZCBlYWNoIGhlYWQgdG8gZ2V0IGJpbmFyeSBmb3JlZ3JvdW5kIG1hc2tzXG4gICAgbWFza3MgPSBucC5zdGFjayhbXG4gICAgICAgIGEgXHUwMDNlIG5wLnBlcmNlbnRpbGUoYSwgdGhyZXNob2xkX3BjdCkgZm9yIGEgaW4gYXR0bl91cFxuICAgIF0pXG4gICAgcmV0dXJuIGF0dG5fdXAsIG1hc2tzICAgIyAocmF3IGF0dGVudGlvbiwgYmluYXJ5IG1hc2tzKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV2YWx1YXRpb24g4oCUIGstTk4gQ2xhc3NpZmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRJTk8gZmVhdHVyZXMgYXJlIHJlbWFya2FibHkgZ29vZCBmb3Igay1uZWFyZXN0LW5laWdoYm9yIChrLU5OKSBjbGFzc2lmaWNhdGlvbiDigJQgbm8gbGluZWFyIGxheWVyIG9yIGZpbmUtdHVuaW5nIHJlcXVpcmVkLiBGZWF0dXJlcyBhcmUgZXh0cmFjdGVkIGZyb20gdGhlIGZyb3plbiBiYWNrYm9uZSwgTDItbm9ybWFsaXplZCwgYW5kIHRoZSBsYWJlbCBvZiB0aGUgaz0yMCBuZWFyZXN0IHRyYWluaW5nIG5laWdoYm9ycyBpcyB1c2VkIGZvciBwcmVkaWN0aW9uLiBESU5PIFZpVC1TLzggYWNoaWV2ZXMgNzQuNSUgdG9wLTEgay1OTiBhY2N1cmFjeSBvbiBJbWFnZU5ldCBlbnRpcmVseSB3aXRob3V0IGxhYmVscywgcml2YWxpbmcgc3VwZXJ2aXNlZCBtb2RlbHMgZnJvbSBhIGZldyB5ZWFycyBwcmlvci4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkRJTk8gVmlULVMvODogNzQuNSUgay1OTiB0b3AtMSBvbiBJbWFnZU5ldCAobm8gbGFiZWxzLCBubyBsaW5lYXIgbGF5ZXIpIiwiRElOTyBWaVQtQi84OiA3Ny4zJSBrLU5OIHRvcC0xIOKAlCBzdHJvbmcgZW5vdWdoIGZvciBtYW55IHJldHJpZXZhbCBhcHBsaWNhdGlvbnMiLCJrLU5OIHByb2JlIGlzIGEgZGlyZWN0IG1lYXN1cmUgb2YgZmVhdHVyZSBxdWFsaXR5OiBubyBsZWFybmVkIGNsYXNzaWZpZXIgY2FuIGNvbXBlbnNhdGUgZm9yIGJhZCBmZWF0dXJlcyIsIkZlYXR1cmVzIGFyZSBMMi1ub3JtYWxpemVkIGJlZm9yZSBrLU5OIHNlYXJjaDsgY29zaW5lIHNpbWlsYXJpdHkgdXNlZCBhcyB0aGUgZGlzdGFuY2UgbWV0cmljIiwiRElOT3YyICgyMDIzKSBzY2FsZXMgdGhpcyB0byA4Ni4xJSBrLU5OIHRvcC0xIHdpdGggY3VyYXRlZCBkYXRhIGFuZCBsYXJnZXIgbW9kZWxzIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRJTk8gdnMgQ29udHJhc3RpdmUgTWV0aG9kcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElOTyBiZWxvbmdzIHRvIHRoZSBzZWxmLWRpc3RpbGxhdGlvbiBmYW1pbHkgKGFsb25nIHdpdGggQllPTCBhbmQgRU1BLWJhc2VkIG1ldGhvZHMpIHJhdGhlciB0aGFuIGNvbnRyYXN0aXZlIGxlYXJuaW5nIChTaW1DTFIsIE1vQ28pLiBDb250cmFzdGl2ZSBtZXRob2RzIHJlcXVpcmUgZXhwbGljaXQgbmVnYXRpdmUgcGFpcnMgdG8gcHJldmVudCBjb2xsYXBzZTsgZGlzdGlsbGF0aW9uLWJhc2VkIG1ldGhvZHMgcmVseSBvbiBhcmNoaXRlY3R1cmFsIGFzeW1tZXRyeSBhbmQgY2VudGVyL3NoYXJwZW4gbWVjaGFuaXNtcyBpbnN0ZWFkLiBUaGUgdGFibGUgY29tcGFyZXMgRElOTyB3aXRoIHR3byBzdHJvbmcgY29udHJhc3RpdmUgYmFzZWxpbmVzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJCYWNrYm9uZSIsIk11bHRpLWNyb3AiLCJUZWFjaGVyIEVNQSIsImstTk4gVG9wLTEiLCJBdHRlbnRpb24gTWFwIFF1YWxpdHkiXSwicm93cyI6W1siRElOTyIsIlZpVC1TLzgiLCJZZXMgKDJHICsgNkwpIiwiWWVzIChtPTAuOTk24oaSMS4wKSIsIjc0LjUlIiwiRXhjZWxsZW50IChzZW1hbnRpYyBzZWdtZW50YXRpb24pIl0sWyJNb0NvIHYzIiwiVmlULUIvMTYiLCJObyAoMiB2aWV3cykiLCJObyAobW9tZW50dW0gZW5jb2RlciBzZXBhcmF0ZSkiLCI3My4yJSIsIk1vZGVyYXRlIChjbGFzcy1sZXZlbCkiXSxbIlNpbUNMUiB2MiIsIlJlc05ldC0xNTIiLCJObyAoMiB2aWV3cykiLCJObyIsIjYzLjAlIiwiUG9vciAodGV4dHVyZS1iaWFzZWQpIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGcm9tIERJTk8gdG8gRElOT3YyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJESU5PdjIgKE9xdWFiIGV0IGFsLiAyMDIzKSBzY2FsZXMgRElOTyBieSBjdXJhdGluZyBhIGxhcmdlIDE0Mk0taW1hZ2UgZGF0YXNldCAoTFZELTE0Mk0pIGZyb20gdGhlIGludGVybmV0LCBjb21iaW5pbmcgRElOT1x1MDAyN3Mgc2VsZi1kaXN0aWxsYXRpb24gbG9zcyB3aXRoIGEgcGF0Y2gtbGV2ZWwgbWFza2VkIGltYWdlIG1vZGVsaW5nIGxvc3MgKHNpbWlsYXIgdG8gaUJPVCksIGFuZCB0cmFpbmluZyBsYXJnZXIgbW9kZWxzIChWaVQtZy8xNCkuIFRoZSByZXN1bHQgaXMgYSB1bml2ZXJzYWwgdmlzdWFsIGZlYXR1cmUgZXh0cmFjdG9yOiBESU5PdjIgVmlULWcgYWNoaWV2ZXMgODYuNSUgbGluZWFyIHByb2Jpbmcgb24gSW1hZ2VOZXQgYW5kIDg2LjElIGstTk4sIG1hdGNoaW5nIG1hbnkgc3VwZXJ2aXNlZCBtb2RlbHMgb24gZGVuc2UgcHJlZGljdGlvbiB0YXNrcyB3aXRob3V0IGFueSBmaW5lLXR1bmluZy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBESU5PIGxpbmVhZ2Ug4oCUIERJTk8g4oaSIERJTk92MiDigJQgZGVtb25zdHJhdGVzIHRoYXQgc2VsZi1zdXBlcnZpc2VkIHZpc3VhbCBwcmUtdHJhaW5pbmcgY2FuIHByb2R1Y2UgZ2VuZXJhbC1wdXJwb3NlIGZlYXR1cmVzIHRoYXQgdHJhbnNmZXIgZWZmZWN0aXZlbHkgYWNyb3NzIGRlcHRoIGVzdGltYXRpb24sIHNlbWFudGljIHNlZ21lbnRhdGlvbiwgYW5kIGltYWdlIHJldHJpZXZhbCB3aXRob3V0IHRhc2stc3BlY2lmaWMgZmluZS10dW5pbmcsIHJlcHJlc2VudGluZyBhIHNpZ25pZmljYW50IHN0ZXAgdG93YXJkIGZvdW5kYXRpb24gbW9kZWxzIGZvciB2aXNpb24uIn1d"
---
# DINO — Self-Distillation Without Labels

DINO (Self-DIstillation with NO labels) by Caron et al. (2021) showed that self-supervised ViT features trained with knowledge distillation between a student and an EMA teacher develop emergent properties absent in supervised models — most strikingly, attention maps that align precisely with semantic object boundaries without ever seeing a segmentation label.

## Self-Distillation Concept

DINO uses a student-teacher framework where both networks share the same ViT architecture. The teacher is an exponential moving average (EMA) of the student's weights — it never receives gradients directly. The student is trained to predict the teacher's output distribution for different augmented views of the same image. Because the teacher is a smoothed version of the student, this is called self-distillation.

## Teacher EMA Update

The teacher's parameters are updated via EMA with a momentum coefficient m that is annealed from 0.996 toward 1.0 during training using a cosine schedule. Higher momentum (m → 1.0) means the teacher changes more slowly — providing a stable training target. The student is updated via standard gradient descent; the teacher receives no gradient signal.

```python
import torch
import torch.nn as nn
import numpy as np
import copy

class DINOTeacherUpdater:
    def __init__(self, student, teacher, base_momentum=0.996):
        self.student       = student
        self.teacher       = teacher
        self.base_momentum = base_momentum
        # Initialize teacher from student weights; disable gradients
        self.teacher.load_state_dict(student.state_dict())
        for p in self.teacher.parameters():
            p.requires_grad_(False)

    def update(self, epoch, max_epochs):
        # Momentum increases from base_momentum to 1.0 via cosine schedule
        m = 1.0 - (1.0 - self.base_momentum) * (
            np.cos(np.pi * epoch / max_epochs) + 1.0
        ) / 2.0

        with torch.no_grad():
            for s_p, t_p in zip(
                self.student.parameters(), self.teacher.parameters()
            ):
                t_p.data.mul_(m).add_((1.0 - m) * s_p.data)

    @torch.no_grad()
    def hard_copy(self):
        # Copy student weights directly to teacher (used at initialization)
        for s_p, t_p in zip(
            self.student.parameters(), self.teacher.parameters()
        ):
            t_p.data.copy_(s_p.data)

# Example: update teacher after each optimizer step
# updater = DINOTeacherUpdater(student, teacher)
# for epoch in range(max_epochs):
#     ... train student ...
#     updater.update(epoch, max_epochs)
```

## Centering and Sharpening

Without any collapse prevention, self-distillation quickly collapses to a trivial solution where both student and teacher output a constant distribution. DINO uses two complementary mechanisms: centering (subtract a running mean from teacher logits to prevent one dimension from dominating) and sharpening (low temperature on the teacher to produce peaked distributions that carry a meaningful training signal).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DINOHead(nn.Module):
    def __init__(self, in_dim, out_dim=65536, center_momentum=0.9):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(in_dim, 2048), nn.GELU(),
            nn.Linear(2048, 2048), nn.GELU(),
            nn.Linear(2048, out_dim, bias=False)
        )
        self.register_buffer('center', torch.zeros(1, out_dim))
        self.center_momentum = center_momentum

    @torch.no_grad()
    def update_center(self, teacher_output):
        # EMA update: subtract running mean to prevent mode collapse
        batch_center = teacher_output.mean(dim=0, keepdim=True)
        self.center = (
            self.center * self.center_momentum
            + batch_center * (1 - self.center_momentum)
        )

    def teacher_softmax(self, x, temp=0.04):
        # Subtract center, apply low temperature -> sharp peaked distribution
        return F.softmax((x - self.center) / temp, dim=-1)

    def student_log_softmax(self, x, temp=0.1):
        # Higher temperature for student -> softer distribution
        return F.log_softmax(x / temp, dim=-1)

    def dino_loss(self, student_out, teacher_out):
        # Cross-entropy H(teacher_sharp, student): student predicts teacher
        t_probs  = self.teacher_softmax(teacher_out)
        s_logp   = self.student_log_softmax(student_out)
        return -(t_probs * s_logp).sum(dim=-1).mean()
```

> **Collapse Prevention is Critical**: Without centering + sharpening, DINO collapses within the first few thousand iterations: the teacher outputs a uniform distribution (all images map to the same representation). Centering prevents any single dimension from dominating. Sharpening (low teacher temperature τ_t = 0.04) ensures the teacher outputs peaked distributions, giving the student a meaningful target to match. Both are required — centering alone still allows collapse to a uniform distribution.

## Multi-Crop Training Strategy

DINO uses a multi-crop augmentation strategy: generate 2 global crops (>50% of image area) and 6–8 local crops (<50% area). The teacher sees only the 2 global crops; the student sees all crops. The loss is computed as the cross-entropy from each student output to each teacher output (local→global matching). This teaches the student to predict global context from local views, forcing semantic feature learning.

```python
import torch
import torch.nn as nn
import torchvision.transforms as T

class MultiCropWrapper(nn.Module):
    def __init__(self, backbone, head):
        super().__init__()
        self.backbone = backbone
        self.head     = head

    def forward(self, crops):
        # Batch all crops together for a single efficient forward pass
        all_crops = torch.cat(crops, dim=0)           # [sum(B), C, H, W]
        features  = self.backbone(all_crops)          # [sum(B), D]
        output    = self.head.mlp(features)           # [sum(B), out_dim]
        # Split back into per-crop chunks
        return output.split([c.shape[0] for c in crops], dim=0)

def dino_train_step(student_net, teacher_net, head, optimizer,
                     global_crops, local_crops):
    # Teacher forward on global crops only (no gradients)
    with torch.no_grad():
        t_outs = [teacher_net(gc) for gc in global_crops]

    # Student forward on ALL crops (global + local)
    all_crops = global_crops + local_crops
    s_outs    = [student_net(c) for c in all_crops]

    # Loss: each student crop predicts each teacher crop's distribution
    loss   = torch.tensor(0.0)
    n_pairs = 0
    for s_out in s_outs:
        for t_out in t_outs:
            loss = loss + head.dino_loss(s_out, t_out)
            n_pairs += 1
    loss = loss / n_pairs

    optimizer.zero_grad()
    loss.backward()
    nn.utils.clip_grad_norm_(student_net.parameters(), 3.0)
    optimizer.step()
    head.update_center(torch.cat(t_outs).detach())
    return loss.item()
```

## DINO Attention Maps

The most striking emergent property of DINO-pretrained ViTs is that the self-attention maps in the last transformer block align closely with semantic object masks — despite no segmentation supervision. Each attention head attends to different object parts. By thresholding the CLS-to-patch attention, one obtains near-ground-truth object masks from a model trained only with image-level self-supervision.

```python
import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

def extract_dino_attention(model, img, patch_size=8, threshold_pct=60):
    # Extract CLS->patch self-attention from the last ViT block
    model.eval()
    attn_store = {}

    def hook_fn(module, inp, out):
        # MultiheadAttention returns (output, attn_weights) when need_weights=True
        attn_store['attn'] = out[1]

    handle = model.blocks[-1].attn.register_forward_hook(hook_fn)

    with torch.no_grad():
        _ = model(img.unsqueeze(0))
    handle.remove()

    # attn: [1, num_heads, N+1, N+1] -> CLS row -> [num_heads, N]
    attn = attn_store['attn'][0, :, 0, 1:]  # remove cls-to-cls
    h = w = int(attn.shape[-1] ** 0.5)
    attn = attn.reshape(-1, 1, h, w)        # [num_heads, 1, h, w]

    # Upsample to original image resolution
    img_h, img_w = img.shape[-2], img.shape[-1]
    attn_up = F.interpolate(attn, size=(img_h, img_w), mode='bilinear', align_corners=False)
    attn_up = attn_up.squeeze(1).cpu().numpy()  # [num_heads, H, W]

    # Threshold each head to get binary foreground masks
    masks = np.stack([
        a > np.percentile(a, threshold_pct) for a in attn_up
    ])
    return attn_up, masks   # (raw attention, binary masks)
```

## Evaluation — k-NN Classification

DINO features are remarkably good for k-nearest-neighbor (k-NN) classification — no linear layer or fine-tuning required. Features are extracted from the frozen backbone, L2-normalized, and the label of the k=20 nearest training neighbors is used for prediction. DINO ViT-S/8 achieves 74.5% top-1 k-NN accuracy on ImageNet entirely without labels, rivaling supervised models from a few years prior.

- DINO ViT-S/8: 74.5% k-NN top-1 on ImageNet (no labels, no linear layer)
- DINO ViT-B/8: 77.3% k-NN top-1 — strong enough for many retrieval applications
- k-NN probe is a direct measure of feature quality: no learned classifier can compensate for bad features
- Features are L2-normalized before k-NN search; cosine similarity used as the distance metric
- DINOv2 (2023) scales this to 86.1% k-NN top-1 with curated data and larger models

## DINO vs Contrastive Methods

DINO belongs to the self-distillation family (along with BYOL and EMA-based methods) rather than contrastive learning (SimCLR, MoCo). Contrastive methods require explicit negative pairs to prevent collapse; distillation-based methods rely on architectural asymmetry and center/sharpen mechanisms instead. The table compares DINO with two strong contrastive baselines.

| Method | Backbone | Multi-crop | Teacher EMA | k-NN Top-1 | Attention Map Quality |
| --- | --- | --- | --- | --- | --- |
| DINO | ViT-S/8 | Yes (2G + 6L) | Yes (m=0.996→1.0) | 74.5% | Excellent (semantic segmentation) |
| MoCo v3 | ViT-B/16 | No (2 views) | No (momentum encoder separate) | 73.2% | Moderate (class-level) |
| SimCLR v2 | ResNet-152 | No (2 views) | No | 63.0% | Poor (texture-biased) |

## From DINO to DINOv2

DINOv2 (Oquab et al. 2023) scales DINO by curating a large 142M-image dataset (LVD-142M) from the internet, combining DINO's self-distillation loss with a patch-level masked image modeling loss (similar to iBOT), and training larger models (ViT-g/14). The result is a universal visual feature extractor: DINOv2 ViT-g achieves 86.5% linear probing on ImageNet and 86.1% k-NN, matching many supervised models on dense prediction tasks without any fine-tuning.

The DINO lineage — DINO → DINOv2 — demonstrates that self-supervised visual pre-training can produce general-purpose features that transfer effectively across depth estimation, semantic segmentation, and image retrieval without task-specific fine-tuning, representing a significant step toward foundation models for vision.

