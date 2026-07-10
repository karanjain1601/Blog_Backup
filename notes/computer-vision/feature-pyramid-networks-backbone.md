---
title: "Feature Pyramid Networks: Multi-Scale Backbone Features"
slug: "feature-pyramid-networks-backbone"
description: "FPN builds a top-down pathway with lateral connections to produce rich multi-scale feature maps for detection — better than single-scale features or image pyramids."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmVhdHVyZSBQeXJhbWlkIE5ldHdvcmtzIChGUE4pLCBpbnRyb2R1Y2VkIGJ5IExpbiBldCBhbC4gKDIwMTcpLCBzb2x2ZSBhIGNvcmUgY2hhbGxlbmdlIGluIG9iamVjdCBkZXRlY3Rpb246IG9iamVjdHMgYXBwZWFyIGF0IHZhc3RseSBkaWZmZXJlbnQgc2NhbGVzLCBzbyBhIHNpbmdsZS1yZXNvbHV0aW9uIGZlYXR1cmUgbWFwIGNhbm5vdCBoYW5kbGUgdGhlbSBhbGwgd2VsbC4gRlBOIGFkZHMgYSB0b3AtZG93biBwYXRod2F5IG92ZXIgYSBzdGFuZGFyZCBDTk4gYmFja2JvbmUgdG8gcHJvZHVjZSBhIGZlYXR1cmUgcHlyYW1pZCB3aXRoIHN0cm9uZyBzZW1hbnRpY3MgYXQgZXZlcnkgc2NhbGUg4oCUIHdpdGhvdXQgdGhlIGNvc3Qgb2YgcHJvY2Vzc2luZyBtdWx0aXBsZSBpbWFnZSBzaXplcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVmb3JlIEZQTiwgZGV0ZWN0b3JzIGVpdGhlciByYW4gb24gYSBzaW5nbGUgZmVhdHVyZSBtYXAgKGZhc3QgYnV0IHNjYWxlLWxpbWl0ZWQpIG9yIHVzZWQgaW1hZ2UgcHlyYW1pZHMgYXQgaW5mZXJlbmNlIChhY2N1cmF0ZSBidXQgMTB4IHNsb3dlcikuIEZQTiBrZWVwcyBhIHNpbmdsZS1zY2FsZSBpbnB1dCwgZXh0cmFjdHMgbXVsdGktc2NhbGUgZmVhdHVyZSBtYXBzIGZyb20gYmFja2JvbmUgc3RhZ2VzLCB0aGVuIGVucmljaGVzIHRoZW0gdG9wLWRvd24g4oCUIHN0cmlraW5nIGEgYmFsYW5jZSBiZXR3ZWVuIGFjY3VyYWN5IGFuZCBzcGVlZCB0aGF0IG1hZGUgaXQgdGhlIGRlZmF1bHQgYmFja2JvbmUgZm9yIHR3by1zdGFnZSBhbmQgc2luZ2xlLXN0YWdlIGRldGVjdG9ycyBhbGlrZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZQTiBpcyBiYWNrYm9uZS1hZ25vc3RpYy4gSXQgYXR0YWNoZXMgdG8gYW55IENOTiB0aGF0IHByb2R1Y2VzIGhpZXJhcmNoaWNhbCBmZWF0dXJlcyDigJQgUmVzTmV0LCBWR0csIEVmZmljaWVudE5ldCwgb3IgYSBWaXNpb24gVHJhbnNmb3JtZXIgd2l0aCBwYXRjaCB0b2tlbnMuIFRoZSByZXN1bHRpbmcgcHlyYW1pZCBsZXZlbHMgUDPigJNQNyBjb3JyZXNwb25kIHRvIGJhY2tib25lIHN0YWdlcyBDM+KAk0M1IHBsdXMgZXh0cmEgcG9vbGluZyBzdGFnZXMuIEVhY2ggbGV2ZWwgUF9rIGhhcyBhIGZpeGVkIGNoYW5uZWwgd2lkdGggKHR5cGljYWxseSAyNTYpLCBtYWtpbmcgZG93bnN0cmVhbSBkZXRlY3Rpb24gaGVhZHMgc2ltcGxlIGFuZCB1bmlmb3JtIGFjcm9zcyBhbGwgc2NhbGVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJvdHRvbS1VcCBhbmQgVG9wLURvd24gUGF0aHdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBib3R0b20tdXAgcGF0aHdheSBpcyBzaW1wbHkgdGhlIGZvcndhcmQgcGFzcyBvZiB0aGUgYmFja2JvbmUuIEZlYXR1cmUgbWFwcyBzaHJpbmsgc3BhdGlhbGx5IGJ5IDJ4IGF0IGVhY2ggc3RhZ2UgYnV0IGdyb3cgcmljaGVyIHNlbWFudGljYWxseS4gVHlwaWNhbCBvdXRwdXQgc3RyaWRlcyBhcmUgOCwgMTYsIGFuZCAzMiBwaXhlbHMgZm9yIEMzLCBDNCwgYW5kIEM1IHJlc3BlY3RpdmVseS4gVGhlIHRvcC1kb3duIHBhdGh3YXkgc3RhcnRzIGZyb20gdGhlIGRlZXBlc3QsIG1vc3Qgc2VtYW50aWMgZmVhdHVyZSBtYXAgQzUgYW5kIHByb2dyZXNzaXZlbHkgdXBzYW1wbGVzIGl0LCBtZXJnaW5nIHdpdGggc2hhbGxvd2VyLCBoaWdoZXItcmVzb2x1dGlvbiBiYWNrYm9uZSBmZWF0dXJlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2h2aXNpb24ubW9kZWxzIGFzIG1vZGVsc1xuXG5jbGFzcyBGUE5CYWNrYm9uZShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBvdXRfY2hhbm5lbHM9MjU2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGJhY2tib25lID0gbW9kZWxzLnJlc25ldDUwKHByZXRyYWluZWQ9VHJ1ZSlcbiAgICAgICAgc2VsZi5jMyA9IG5uLlNlcXVlbnRpYWwoYmFja2JvbmUubGF5ZXIxLCBiYWNrYm9uZS5sYXllcjIpICAjIHN0cmlkZSA4XG4gICAgICAgIHNlbGYuYzQgPSBiYWNrYm9uZS5sYXllcjMgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgc3RyaWRlIDE2XG4gICAgICAgIHNlbGYuYzUgPSBiYWNrYm9uZS5sYXllcjQgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgc3RyaWRlIDMyXG4gICAgICAgIHNlbGYubGF0ZXJhbHMgPSBubi5Nb2R1bGVMaXN0KFtcbiAgICAgICAgICAgIG5uLkNvbnYyZCg1MTIsICBvdXRfY2hhbm5lbHMsIDEpLCAgIyBsYXRlcmFsIGZvciBDM1xuICAgICAgICAgICAgbm4uQ29udjJkKDEwMjQsIG91dF9jaGFubmVscywgMSksICAjIGxhdGVyYWwgZm9yIEM0XG4gICAgICAgICAgICBubi5Db252MmQoMjA0OCwgb3V0X2NoYW5uZWxzLCAxKSwgICMgbGF0ZXJhbCBmb3IgQzVcbiAgICAgICAgXSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsYXRlcmFsIGNvbm5lY3Rpb25zIHRha2UgQzMsIEM0LCBDNSBhbmQgcHJvamVjdCBlYWNoIHRvIGEgY29tbW9uIGNoYW5uZWwgd2lkdGgg4oCUIDI1NiBieSBkZWZhdWx0IOKAlCB1c2luZyAxeDEgY29udm9sdXRpb25zLiBUaGlzIG1ha2VzIGNoYW5uZWwgZGltZW5zaW9ucyB1bmlmb3JtIGJlZm9yZSB0aGUgdG9wLWRvd24gbWVyZ2Ugc3RlcC4gR3JhZGllbnRzIGZsb3cgdGhyb3VnaCB0aGUgbGF0ZXJhbCBjb252b2x1dGlvbnMgZHVyaW5nIHRyYWluaW5nLCBhbGxvd2luZyB0aGUgRlBOIGhlYWQgdG8gYWRhcHQgdGhlIGJhY2tib25lIGZlYXR1cmVzIHdpdGhvdXQgcmVxdWlyaW5nIGZ1bGwgYmFja2JvbmUgZmluZS10dW5pbmcgd2hlbiB0cmFuc2Zlci1sZWFybmluZyB0byBhIG5ldyBkZXRlY3Rpb24gZGF0YXNldC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgdG9wX2Rvd25fcGF0aHdheShzZWxmLCBjMywgYzQsIGM1KTpcbiAgICBwNSA9IHNlbGYubGF0ZXJhbHNbMl0oYzUpXG4gICAgcDQgPSBzZWxmLmxhdGVyYWxzWzFdKGM0KSArIEYuaW50ZXJwb2xhdGUocDUsIHNjYWxlX2ZhY3Rvcj0yLCBtb2RlPVx1MDAyN25lYXJlc3RcdTAwMjcpXG4gICAgcDMgPSBzZWxmLmxhdGVyYWxzWzBdKGMzKSArIEYuaW50ZXJwb2xhdGUocDQsIHNjYWxlX2ZhY3Rvcj0yLCBtb2RlPVx1MDAyN25lYXJlc3RcdTAwMjcpXG4gICAgIyAzeDMgc21vb3RoZXIgcmVtb3ZlcyBuZWFyZXN0LW5laWdoYm91ciBhbGlhc2luZyBhZnRlciBlYWNoIG1lcmdlXG4gICAgcDUgPSBzZWxmLnNtb290aGVyc1syXShwNSlcbiAgICBwNCA9IHNlbGYuc21vb3RoZXJzWzFdKHA0KVxuICAgIHAzID0gc2VsZi5zbW9vdGhlcnNbMF0ocDMpXG4gICAgcmV0dXJuIHAzLCBwNCwgcDUifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXRlcmFsIENvbm5lY3Rpb25zIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRfdHlwZSI6ImluZm8iLCJjb250ZW50IjoiRlBOXHUwMDI3cyBrZXkgaW5ub3ZhdGlvbiBpcyBsYXRlcmFsIGNvbm5lY3Rpb25zIOKAlCAxeDEgY29udnMgdGhhdCBhbGlnbiBjaGFubmVsIGRpbWVuc2lvbnMgYmVmb3JlIGFkZGl0aW9uLiBXaXRob3V0IHRoZW0sIHRoZSB0b3AtZG93biBwYXRod2F5IHdvdWxkIG92ZXJ3cml0ZSBzZW1hbnRpY3Mgd2l0aCBwb3NpdGlvbmFsIG5vaXNlIGZyb20gdGhlIGhpZ2gtcmVzIGZlYXR1cmUgbWFwcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgM3gzIGNvbnZvbHV0aW9uIGZvbGxvd3MgZWFjaCBtZXJnZSB0byBzbW9vdGggYWxpYXNpbmcgYXJ0aWZhY3RzIGludHJvZHVjZWQgYnkgbmVhcmVzdC1uZWlnaGJvciB1cHNhbXBsaW5nLiBUaGVzZSBzbW9vdGhlcnMgYWxzbyBoZWxwIHRoZSBuZXR3b3JrIGJsZW5kIHRvcC1kb3duIGFuZCBsYXRlcmFsIHNpZ25hbHMgb3B0aW1hbGx5IHJhdGhlciB0aGFuIHJlbHlpbmcgb24gYSBmaXhlZCA1MC81MCBhZGRpdGlvbi4gSW4gcHJhY3RpY2UsIG9taXR0aW5nIHRoZSAzeDMgc21vb3RoZXIgcmVkdWNlcyBBUCBieSAwLjPigJMwLjUgcG9pbnRzIG9uIENPQ08g4oCUIGEgc21hbGwgYnV0IGNvbnNpc3RlbnQgYW5kIHJlcHJvZHVjaWJsZSBkZWdyYWRhdGlvbiBhY3Jvc3MgZGV0ZWN0aW9uIGJlbmNobWFya3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcHlyYW1pZCBsZXZlbHMgYWxsIHNoYXJlIDI1Ni1jaGFubmVsIG91dHB1dCBidXQgZW5jb2RlIGZlYXR1cmVzIGF0IGRpZmZlcmVudCBzcGF0aWFsIHJlc29sdXRpb25zIGFuZCBzZW1hbnRpYyBhYnN0cmFjdGlvbiBsZXZlbHMuIFAzIGlzIGhpZ2hlc3QgcmVzb2x1dGlvbiAoc3RyaWRlIDgpIGFuZCBiZXN0IGZvciBzbWFsbCBvYmplY3RzOyBQNSBpcyBsb3dlc3QgcmVzb2x1dGlvbiAoc3RyaWRlIDMyKSBidXQgcmljaGVzdCBzZW1hbnRpY2FsbHksIGhhbmRsaW5nIGxhcmdlIG9iamVjdHMgd2VsbC4gVGhpcyBjb21wbGVtZW50YXJpdHkgaXMgdGhlIGNvcmUgcmVhc29uIEZQTiBvdXRwZXJmb3JtcyBib3RoIHNpbmdsZS1zY2FsZSBmZWF0dXJlIG1hcHMgYW5kIG5haXZlIGltYWdlLXB5cmFtaWQgYXBwcm9hY2hlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGUE4gaW4gRGV0ZWN0aW9uIEhlYWRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGYXN0ZXIgUi1DTk4gd2l0aCBGUE4gYXNzaWducyBlYWNoIHJlZ2lvbiBwcm9wb3NhbCB0byBleGFjdGx5IG9uZSBweXJhbWlkIGxldmVsIGJhc2VkIG9uIHRoZSBwcm9wb3NhbFx1MDAyN3MgYXJlYS4gU21hbGwgcHJvcG9zYWxzIG1hcCB0byBoaWdoLXJlc29sdXRpb24gbGV2ZWxzIChQMyksIGxhcmdlIG9uZXMgdG8gY29hcnNlciBsZXZlbHMgKFA1KS4gVGhlIGRldGVjdGlvbiBoZWFkIOKAlCB0d28gRkMgbGF5ZXJzIGZvciBjbGFzc2lmaWNhdGlvbiBhbmQgcmVncmVzc2lvbiDigJQgaXMgc2hhcmVkIGFjcm9zcyBhbGwgbGV2ZWxzLCBzbyB0aGUgbmV0d29yayBsZWFybnMgb25lIHVuaXZlcnNhbCBoZWFkIHRoYXQgZ2VuZXJhbGl6ZXMgYWNyb3NzIHNjYWxlcyB3aXRob3V0IHJlcXVpcmluZyBwZXItbGV2ZWwgc3BlY2lhbGl6YXRpb24uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkxldmVsIiwiU3RyaWRlIiwiRmVhdHVyZSBTY2FsZSIsIlR5cGljYWwgQW5jaG9ycyIsIk9iamVjdHMgRGV0ZWN0ZWQiXSwicm93cyI6W1siUDMiLCI4IiwiMzLCsiIsIjMywrIiLCJUaW55Il0sWyJQNCIsIjE2IiwiNjTCsiIsIjY0wrIiLCJTbWFsbCJdLFsiUDUiLCIzMiIsIjEyOMKyIiwiMTI4wrIiLCJNZWRpdW0iXSxbIlA2IiwiNjQiLCIyNTbCsiIsIjI1NsKyIiwiTGFyZ2UiXSxbIlA3IiwiMTI4IiwiNTEywrIiLCI1MTLCsiIsIkh1Z2UiXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbWF0aFxuXG5kZWYgYXNzaWduX2Zwbl9sZXZlbChib3hfdywgYm94X2gsIGswPTQsIHMwPTIyNCk6XG4gICAgXCJcIlwiQXNzaWduIGEgUm9JIHRvIGFuIEZQTiBsZXZlbC5cbiAgICBMaW4gZXQgYWwuICgyMDE3KSBFcS4gMTogayA9IGZsb29yKGswICsgbG9nMihzcXJ0KHdoKSAvIHMwKSlcbiAgICBrMD00IG1hcHMgUDQgdG8gdGhlIGNhbm9uaWNhbCAyMjR4MjI0IHJlZmVyZW5jZSBzaXplLlxuICAgIFwiXCJcIlxuICAgIGFyZWEgPSBib3hfdyAqIGJveF9oXG4gICAgayA9IG1hdGguZmxvb3IoazAgKyBtYXRoLmxvZzIobWF0aC5zcXJ0KGFyZWEpIC8gczApKVxuICAgIGsgPSBtYXgoMiwgbWluKGssIDUpKSAgIyBjbGFtcCB0byB2YWxpZCBGUE4gbGV2ZWxzIFtQMiwgUDVdXG4gICAgcmV0dXJuIGtcblxuIyA1Nng1NiBwcm9wb3NhbCAgLVx1MDAzZSBQMyAoc21hbGwpLCAgNDQ4eDQ0OCAtXHUwMDNlIFA1IChsYXJnZSlcbnByaW50KGFzc2lnbl9mcG5fbGV2ZWwoNTYsIDU2KSkgICAgIyAtXHUwMDNlIDNcbnByaW50KGFzc2lnbl9mcG5fbGV2ZWwoNDQ4LCA0NDgpKSAgIyAtXHUwMDNlIDUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJldGluYU5ldCB1c2VzIEZQTiBsZXZlbHMgUDPigJNQNywgd2hlcmUgUDYgYW5kIFA3IGFyZSBwcm9kdWNlZCBieSBzdHJpZGVkIGNvbnZvbHV0aW9ucyBvbiB0b3Agb2YgQzUgcmF0aGVyIHRoYW4gYmFja2JvbmUgc3RhZ2VzLiBSZXRpbmFOZXQgYXR0YWNoZXMgYSBib3ggcmVncmVzc2lvbiBzdWJuZXR3b3JrIGFuZCBhIGNsYXNzaWZpY2F0aW9uIHN1Ym5ldHdvcmsg4oCUIGVhY2ggYSBzdGFjayBvZiBmb3VyIDN4MyBjb252b2x1dGlvbnMg4oCUIHRvIGV2ZXJ5IEZQTiBsZXZlbCwgYWNoaWV2aW5nIHN0YXRlLW9mLXRoZS1hcnQgb25lLXN0YWdlIGFjY3VyYWN5IHdoaWxlIHJlbWFpbmluZyBmdWxseSBjb252b2x1dGlvbmFsLCBhbmNob3ItYmFzZWQsIGFuZCBmcmVlIG9mIHJlZ2lvbiBwcm9wb3NhbCBzdGFnZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUEFOZXQgYW5kIEJpRlBOIEV4dGVuc2lvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZQTlx1MDAyN3MgdG9wLWRvd24gcGF0aCBjcmVhdGVzIG9uZS1kaXJlY3Rpb25hbCBpbmZvcm1hdGlvbiBmbG93OiBzZW1hbnRpY3MgcHJvcGFnYXRlIGZyb20gZGVlcCB0byBzaGFsbG93LCBidXQgZmluZSBzcGF0aWFsIGRldGFpbCBkb2VzIG5vdCBwcm9wYWdhdGUgdXB3YXJkLiBQQU5ldCBmaXhlcyB0aGlzIGJ5IGFkZGluZyBhIGJvdHRvbS11cCBwYXRoIGF1Z21lbnRhdGlvbiBzdGVwIGFmdGVyIEZQTiBwcm9kdWNlcyBQM+KAk1A1LiBBIHNlY29uZCBsYXRlcmFsLWZ1c2Ugc2VxdWVuY2UgcHJvcGFnYXRlcyBsb3ctbGV2ZWwgZGV0YWlsIGJhY2sgdXAgdG8gUDUsIGZvcm1pbmcgYSB0d28tcGF0aCBmZWF0dXJlIHB5cmFtaWQgdGhhdCBjb25zaXN0ZW50bHkgaW1wcm92ZXMgbWFzayBhbmQgYm94IEFQIG9uIENPQ08uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImNsYXNzIFBBTmV0QXVnbWVudGF0aW9uKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNoYW5uZWxzPTI1Nik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICAjIFN0cmlkZWQgY29udnMgZHJpdmUgdGhlIGJvdHRvbS11cCBhdWdtZW50YXRpb24gcGF0aFxuICAgICAgICBzZWxmLnBhX2xhdGVyYWxzID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBubi5Db252MmQoY2hhbm5lbHMsIGNoYW5uZWxzLCAzLCBzdHJpZGU9MiwgcGFkZGluZz0xKSwgICMgUDMtXHUwMDNlTjRcbiAgICAgICAgICAgIG5uLkNvbnYyZChjaGFubmVscywgY2hhbm5lbHMsIDMsIHN0cmlkZT0yLCBwYWRkaW5nPTEpLCAgIyBONC1cdTAwM2VONVxuICAgICAgICBdKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgcDMsIHA0LCBwNSk6XG4gICAgICAgIG4zID0gcDNcbiAgICAgICAgbjQgPSBwNCArIHNlbGYucGFfbGF0ZXJhbHNbMF0objMpICAjIGZ1c2UgUDQgKyBkb3duc2FtcGxlZCBOM1xuICAgICAgICBuNSA9IHA1ICsgc2VsZi5wYV9sYXRlcmFsc1sxXShuNCkgICMgZnVzZSBQNSArIGRvd25zYW1wbGVkIE40XG4gICAgICAgIHJldHVybiBuMywgbjQsIG41In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCaUZQTiwgZnJvbSBFZmZpY2llbnREZXQsIG1ha2VzIGZ1c2lvbiB3ZWlnaHRlZCBhbmQgbGVhcm5hYmxlLiBFYWNoIG5vZGUgcmVjZWl2ZXMgYSBzb2Z0bWF4LW5vcm1hbGl6ZWQgd2VpZ2h0IHBlciBpbnB1dCBlZGdlIHNvIHRoZSBuZXR3b3JrIGNvbnRyb2xzIGhvdyBtdWNoIG9mIGVhY2ggc2NhbGUgdG8gYmxlbmQuIFNpbmdsZS1pbnB1dCBub2RlcyBhcmUgcHJ1bmVkIHNpbmNlIHRoZXkgYWRkIG5vIGNyb3NzLXNjYWxlIGZ1c2lvbiB2YWx1ZS4gVGhlIGJpZGlyZWN0aW9uYWwgZnVzaW9uIGJsb2NrIHJlcGVhdHMgbXVsdGlwbGUgdGltZXMgZm9yIGV4dHJhIHJlcHJlc2VudGF0aW9uYWwgY2FwYWNpdHksIHNjYWxpbmcgY2xlYW5seSBhbG9uZ3NpZGUgdGhlIEVmZmljaWVudE5ldCBjb21wb3VuZC1zY2FsaW5nIGNvZWZmaWNpZW50LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTkFTLUZQTiB1c2VzIG5ldXJhbCBhcmNoaXRlY3R1cmUgc2VhcmNoIHRvIGRpc2NvdmVyIGNyb3NzLXNjYWxlIGNvbm5lY3Rpb24gdG9wb2xvZ2llcywgc29tZXRpbWVzIG91dHBlcmZvcm1pbmcgUEFOZXQgYW5kIEJpRlBOIGJ5IHdpZGUgbWFyZ2lucy4gRGVzcGl0ZSB0aGlzLCBoYW5kLWRlc2lnbmVkIHB5cmFtaWRzIGRvbWluYXRlIHByb2R1Y3Rpb246IHRoZXkgYXJlIGludGVycHJldGFibGUsIGluZmVyZW5jZS1wcmVkaWN0YWJsZSwgYW5kIGVhc2llciB0byBxdWFudGl6ZSBmb3IgZWRnZSBoYXJkd2FyZSDigJQgcHJvcGVydGllcyB0aGF0IG1hdHRlciBpbiBhdXRvbm9tb3VzIGRyaXZpbmcgYW5kIG1vYmlsZSB2aXNpb24gd2hlcmUgbGF0ZW5jeSBhbmQgb24tZGV2aWNlIGRlcGxveW1lbnQgYXJlIGhhcmQgY29uc3RyYWludHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRlBOIHRyYW5zZm9ybWVkIG11bHRpLXNjYWxlIGRldGVjdGlvbiBmcm9tIGFuIGV4cGVuc2l2ZSBwcmVwcm9jZXNzaW5nIHN0ZXAgKGltYWdlIHB5cmFtaWRzKSBpbnRvIGFuIGVmZmljaWVudCBhcmNoaXRlY3R1cmFsIGNvbXBvbmVudC4gVGhlIGNvcmUgaW5zaWdodCDigJQgbWVyZ2UgdG9wLWRvd24gc2VtYW50aWNzIHdpdGggYm90dG9tLXVwIHJlc29sdXRpb24gdmlhIGxhdGVyYWwgMXgxIGNvbnZvbHV0aW9ucyDigJQgaXMgcmVtYXJrYWJseSBzaW1wbGUgeWV0IHBvd2VyZnVsLiBGUE4gYmVjYW1lIHRoZSBiYWNrYm9uZSBvZiBNYXNrIFItQ05OLCBSZXRpbmFOZXQsIGFuZCBDYXNjYWRlIFJDTk4sIGFuZCBpdHMgZGVzY2VuZGFudHMgKFBBTmV0LCBCaUZQTikgcmVtYWluIGNvbXBldGl0aXZlIGFjcm9zcyBhbGwgZGV0ZWN0aW9uIGJlbmNobWFya3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaHJlZSBjb21tb24gRlBOIHBpdGZhbGxzOiAoMSkgc2tpcHBpbmcgdGhlIDN4MyBzbW9vdGhlciBhZnRlciBsYXRlcmFsIG1lcmdlIGNhdXNlcyBhbGlhc2luZyBhbmQgaHVydHMgc21hbGwtb2JqZWN0IEFQOyAoMikgYmlsaW5lYXIgdXBzYW1wbGluZyBpbnN0ZWFkIG9mIG5lYXJlc3QtbmVpZ2hib3IgaW50cm9kdWNlcyBjb29yZGluYXRlIG1pc2FsaWdubWVudCBpbiBmdXNlZCBtYXBzOyAoMykgdW4tZnJvemVuIGJhY2tib25lIEJOIHdpdGggc21hbGwgYmF0Y2ggc2l6ZXMgcHJvZHVjZXMgbm9pc3kgY3Jvc3Mtc2NhbGUgZ3JhZGllbnRzLiBWaXN1YWxpemluZyBlYWNoIHB5cmFtaWQgbGV2ZWxcdTAwMjdzIGFjdGl2YXRpb24gbWFwcyBzZXBhcmF0ZWx5IGlzIHRoZSBmYXN0ZXN0IGRpYWdub3N0aWMgZm9yIGFsbCB0aHJlZSBpc3N1ZXMuIn1d"
---
# Feature Pyramid Networks: Multi-Scale Backbone Features

Feature Pyramid Networks (FPN), introduced by Lin et al. (2017), solve a core challenge in object detection: objects appear at vastly different scales, so a single-resolution feature map cannot handle them all well. FPN adds a top-down pathway over a standard CNN backbone to produce a feature pyramid with strong semantics at every scale — without the cost of processing multiple image sizes.

## Overview

Before FPN, detectors either ran on a single feature map (fast but scale-limited) or used image pyramids at inference (accurate but 10x slower). FPN keeps a single-scale input, extracts multi-scale feature maps from backbone stages, then enriches them top-down — striking a balance between accuracy and speed that made it the default backbone for two-stage and single-stage detectors alike.

FPN is backbone-agnostic. It attaches to any CNN that produces hierarchical features — ResNet, VGG, EfficientNet, or a Vision Transformer with patch tokens. The resulting pyramid levels P3–P7 correspond to backbone stages C3–C5 plus extra pooling stages. Each level P_k has a fixed channel width (typically 256), making downstream detection heads simple and uniform across all scales.

## Bottom-Up and Top-Down Pathways

The bottom-up pathway is simply the forward pass of the backbone. Feature maps shrink spatially by 2x at each stage but grow richer semantically. Typical output strides are 8, 16, and 32 pixels for C3, C4, and C5 respectively. The top-down pathway starts from the deepest, most semantic feature map C5 and progressively upsamples it, merging with shallower, higher-resolution backbone features.

```python
import torch.nn as nn
import torchvision.models as models

class FPNBackbone(nn.Module):
    def __init__(self, out_channels=256):
        super().__init__()
        backbone = models.resnet50(pretrained=True)
        self.c3 = nn.Sequential(backbone.layer1, backbone.layer2)  # stride 8
        self.c4 = backbone.layer3                                   # stride 16
        self.c5 = backbone.layer4                                   # stride 32
        self.laterals = nn.ModuleList([
            nn.Conv2d(512,  out_channels, 1),  # lateral for C3
            nn.Conv2d(1024, out_channels, 1),  # lateral for C4
            nn.Conv2d(2048, out_channels, 1),  # lateral for C5
        ])
```

The lateral connections take C3, C4, C5 and project each to a common channel width — 256 by default — using 1x1 convolutions. This makes channel dimensions uniform before the top-down merge step. Gradients flow through the lateral convolutions during training, allowing the FPN head to adapt the backbone features without requiring full backbone fine-tuning when transfer-learning to a new detection dataset.

```python
import torch.nn.functional as F

def top_down_pathway(self, c3, c4, c5):
    p5 = self.laterals[2](c5)
    p4 = self.laterals[1](c4) + F.interpolate(p5, scale_factor=2, mode='nearest')
    p3 = self.laterals[0](c3) + F.interpolate(p4, scale_factor=2, mode='nearest')
    # 3x3 smoother removes nearest-neighbour aliasing after each merge
    p5 = self.smoothers[2](p5)
    p4 = self.smoothers[1](p4)
    p3 = self.smoothers[0](p3)
    return p3, p4, p5
```

## Lateral Connections

> ****: FPN's key innovation is lateral connections — 1x1 convs that align channel dimensions before addition. Without them, the top-down pathway would overwrite semantics with positional noise from the high-res feature maps.

A 3x3 convolution follows each merge to smooth aliasing artifacts introduced by nearest-neighbor upsampling. These smoothers also help the network blend top-down and lateral signals optimally rather than relying on a fixed 50/50 addition. In practice, omitting the 3x3 smoother reduces AP by 0.3–0.5 points on COCO — a small but consistent and reproducible degradation across detection benchmarks.

The pyramid levels all share 256-channel output but encode features at different spatial resolutions and semantic abstraction levels. P3 is highest resolution (stride 8) and best for small objects; P5 is lowest resolution (stride 32) but richest semantically, handling large objects well. This complementarity is the core reason FPN outperforms both single-scale feature maps and naive image-pyramid approaches.

## FPN in Detection Heads

Faster R-CNN with FPN assigns each region proposal to exactly one pyramid level based on the proposal's area. Small proposals map to high-resolution levels (P3), large ones to coarser levels (P5). The detection head — two FC layers for classification and regression — is shared across all levels, so the network learns one universal head that generalizes across scales without requiring per-level specialization.

| Level | Stride | Feature Scale | Typical Anchors | Objects Detected |
| --- | --- | --- | --- | --- |
| P3 | 8 | 32² | 32² | Tiny |
| P4 | 16 | 64² | 64² | Small |
| P5 | 32 | 128² | 128² | Medium |
| P6 | 64 | 256² | 256² | Large |
| P7 | 128 | 512² | 512² | Huge |

```python
import math

def assign_fpn_level(box_w, box_h, k0=4, s0=224):
    """Assign a RoI to an FPN level.
    Lin et al. (2017) Eq. 1: k = floor(k0 + log2(sqrt(wh) / s0))
    k0=4 maps P4 to the canonical 224x224 reference size.
    """
    area = box_w * box_h
    k = math.floor(k0 + math.log2(math.sqrt(area) / s0))
    k = max(2, min(k, 5))  # clamp to valid FPN levels [P2, P5]
    return k

# 56x56 proposal  -> P3 (small),  448x448 -> P5 (large)
print(assign_fpn_level(56, 56))    # -> 3
print(assign_fpn_level(448, 448))  # -> 5
```

RetinaNet uses FPN levels P3–P7, where P6 and P7 are produced by strided convolutions on top of C5 rather than backbone stages. RetinaNet attaches a box regression subnetwork and a classification subnetwork — each a stack of four 3x3 convolutions — to every FPN level, achieving state-of-the-art one-stage accuracy while remaining fully convolutional, anchor-based, and free of region proposal stages.

## PANet and BiFPN Extensions

FPN's top-down path creates one-directional information flow: semantics propagate from deep to shallow, but fine spatial detail does not propagate upward. PANet fixes this by adding a bottom-up path augmentation step after FPN produces P3–P5. A second lateral-fuse sequence propagates low-level detail back up to P5, forming a two-path feature pyramid that consistently improves mask and box AP on COCO.

```python
class PANetAugmentation(nn.Module):
    def __init__(self, channels=256):
        super().__init__()
        # Strided convs drive the bottom-up augmentation path
        self.pa_laterals = nn.ModuleList([
            nn.Conv2d(channels, channels, 3, stride=2, padding=1),  # P3->N4
            nn.Conv2d(channels, channels, 3, stride=2, padding=1),  # N4->N5
        ])

    def forward(self, p3, p4, p5):
        n3 = p3
        n4 = p4 + self.pa_laterals[0](n3)  # fuse P4 + downsampled N3
        n5 = p5 + self.pa_laterals[1](n4)  # fuse P5 + downsampled N4
        return n3, n4, n5
```

BiFPN, from EfficientDet, makes fusion weighted and learnable. Each node receives a softmax-normalized weight per input edge so the network controls how much of each scale to blend. Single-input nodes are pruned since they add no cross-scale fusion value. The bidirectional fusion block repeats multiple times for extra representational capacity, scaling cleanly alongside the EfficientNet compound-scaling coefficient.

NAS-FPN uses neural architecture search to discover cross-scale connection topologies, sometimes outperforming PANet and BiFPN by wide margins. Despite this, hand-designed pyramids dominate production: they are interpretable, inference-predictable, and easier to quantize for edge hardware — properties that matter in autonomous driving and mobile vision where latency and on-device deployment are hard constraints.

## Key Takeaways

FPN transformed multi-scale detection from an expensive preprocessing step (image pyramids) into an efficient architectural component. The core insight — merge top-down semantics with bottom-up resolution via lateral 1x1 convolutions — is remarkably simple yet powerful. FPN became the backbone of Mask R-CNN, RetinaNet, and Cascade RCNN, and its descendants (PANet, BiFPN) remain competitive across all detection benchmarks.

Three common FPN pitfalls: (1) skipping the 3x3 smoother after lateral merge causes aliasing and hurts small-object AP; (2) bilinear upsampling instead of nearest-neighbor introduces coordinate misalignment in fused maps; (3) un-frozen backbone BN with small batch sizes produces noisy cross-scale gradients. Visualizing each pyramid level's activation maps separately is the fastest diagnostic for all three issues.

