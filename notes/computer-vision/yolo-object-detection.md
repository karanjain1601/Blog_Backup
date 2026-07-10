---
title: "YOLO: Real-Time Single-Stage Detection"
slug: "yolo-object-detection"
description: "YOLO's grid-based detection paradigm — from YOLOv1's unified detection to YOLOv8's decoupled head — covering objectness scores, multi-scale grids, and the YOLOv5/v8 training pipeline."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJZT0xPIChZb3UgT25seSBMb29rIE9uY2UpIHJlZGVmaW5lZCByZWFsLXRpbWUgb2JqZWN0IGRldGVjdGlvbiBieSBmcmFtaW5nIGl0IGFzIGEgc2luZ2xlIHJlZ3Jlc3Npb24gcHJvYmxlbS4gSW5zdGVhZCBvZiBwcm9wb3NpbmcgcmVnaW9ucyB0aGVuIGNsYXNzaWZ5aW5nIHRoZW0sIFlPTE8gZGl2aWRlcyB0aGUgaW1hZ2UgaW50byBhIGdyaWQgYW5kIHByZWRpY3RzIGJvdW5kaW5nIGJveGVzIGFuZCBjbGFzcyBwcm9iYWJpbGl0aWVzIGZvciBlYWNoIGNlbGwgaW4gb25lIGZvcndhcmQgcGFzcy4gVGhpcyB1bmlmaWVkIGFwcHJvYWNoIGVuYWJsZXMgZGV0ZWN0aW9uIGF0IDMw4oCTMTAwKyBGUFMgd2l0aCBjb21wZXRpdGl2ZSBhY2N1cmFjeS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNpbmNlIHRoZSBvcmlnaW5hbCAyMDE2IHBhcGVyLCBZT0xPIGhhcyBldm9sdmVkIHRocm91Z2ggbmluZSBtYWpvciB2ZXJzaW9ucy4gRWFjaCB2ZXJzaW9uIGltcHJvdmVkIGFjY3VyYWN5LCB0cmFpbmluZyBzdGFiaWxpdHksIGFuZCBkZXBsb3ltZW50IGZsZXhpYmlsaXR5IHdoaWxlIHByZXNlcnZpbmcgdGhlIGNvcmUgc2luZ2xlLXN0YWdlLCByZWFsLXRpbWUgcGhpbG9zb3BoeS4gVG9kYXksIFlPTE92OCBhbmQgWU9MT3Y5IGZyb20gVWx0cmFseXRpY3MgYXJlIHRoZSBtb3N0IHdpZGVseSBkZXBsb3llZCBkZXRlY3Rpb24gbW9kZWxzIGluIHByb2R1Y3Rpb24gY29tcHV0ZXIgdmlzaW9uIHN5c3RlbXMgZ2xvYmFsbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JpZC1CYXNlZCBQcmVkaWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJZT0xPdjEgZGl2aWRlcyB0aGUgaW5wdXQgaW1hZ2UgaW50byBhbiBTw5dTIGdyaWQgKGRlZmF1bHQgN8OXNykuIEVhY2ggZ3JpZCBjZWxsIHByZWRpY3RzIEIgYm91bmRpbmcgYm94ZXMgKGVhY2ggd2l0aCB4LCB5LCB3LCBoLCBjb25maWRlbmNlKSBhbmQgQyBjbGFzcyBwcm9iYWJpbGl0aWVzLiBUaGUgbmV0d29yayBvdXRwdXRzIGEgdGVuc29yIG9mIHNoYXBlIFtTLCBTLCBCw5c1K0NdLiBUaGUgY2VsbCB0aGF0IGNvbnRhaW5zIGFuIG9iamVjdFx1MDAyN3MgY2VudGVyIGlzIHJlc3BvbnNpYmxlIGZvciBwcmVkaWN0aW5nIHRoYXQgb2JqZWN0LiBCb3ggY29vcmRpbmF0ZXMgYXJlIG5vcm1hbGl6ZWQgcmVsYXRpdmUgdG8gdGhlIGNlbGxcdTAwMjdzIHBvc2l0aW9uIGFuZCBzaXplLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGRlY29kZV95b2xvdjFfb3V0cHV0KG91dHB1dCwgUz03LCBCPTIsIEM9ODAsIGltZ19zaXplPTQ0OCk6XG4gICAgXCJcIlwiXG4gICAgb3V0cHV0OiBbYmF0Y2gsIFMsIFMsIEIqNSArIENdXG4gICAgUmV0dXJucyBib3hlcyBpbiBbeDEsIHkxLCB4MiwgeTJdIGZvcm1hdC5cbiAgICBcIlwiXCJcbiAgICBjZWxsX3NpemUgPSBpbWdfc2l6ZSAvIFNcbiAgICBib3hlcyA9IG91dHB1dFsuLi4sIDpCKjVdLnJlc2hhcGUoKm91dHB1dC5zaGFwZVs6M10sIEIsIDUpXG4gICAgIyBjeCwgY3kgYXJlIG9mZnNldHMgd2l0aGluIGNlbGwgLVx1MDAzZSBjb252ZXJ0IHRvIGltYWdlIGNvb3Jkc1xuICAgIGdyaWRfeSwgZ3JpZF94ID0gdG9yY2gubWVzaGdyaWQodG9yY2guYXJhbmdlKFMpLCB0b3JjaC5hcmFuZ2UoUyksIGluZGV4aW5nPVx1MDAyN2lqXHUwMDI3KVxuICAgIGJveGVzWy4uLiwgMF0gPSAoYm94ZXNbLi4uLCAwXSArIGdyaWRfeC51bnNxdWVlemUoLTEpKSAqIGNlbGxfc2l6ZVxuICAgIGJveGVzWy4uLiwgMV0gPSAoYm94ZXNbLi4uLCAxXSArIGdyaWRfeS51bnNxdWVlemUoLTEpKSAqIGNlbGxfc2l6ZVxuICAgIGJveGVzWy4uLiwgMl0gPSBib3hlc1suLi4sIDJdICogaW1nX3NpemUgICMgd2lkdGhcbiAgICBib3hlc1suLi4sIDNdID0gYm94ZXNbLi4uLCAzXSAqIGltZ19zaXplICAjIGhlaWdodFxuICAgIHJldHVybiBib3hlcywgb3V0cHV0Wy4uLiwgQio1Ol0gICMgYm94ZXMsIGNsYXNzX3Byb2JzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktU2NhbGUgRGV0ZWN0aW9uIGluIFlPTE92MysifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IllPTE92MiBpbnRyb2R1Y2VkIGFuY2hvciBib3hlcyAobGVhcm5lZCBjbHVzdGVyIGNlbnRyb2lkcyBmcm9tIENPQ08gYW5ub3RhdGlvbnMpIHRvIGltcHJvdmUgYm91bmRpbmcgYm94IHByZWRpY3Rpb24gc3RhYmlsaXR5LiBZT0xPdjMgZXh0ZW5kZWQgdGhpcyB0byB0aHJlZSBkZXRlY3Rpb24gc2NhbGVzIHVzaW5nIGEgRlBOLWxpa2UgZmVhdHVyZSBweXJhbWlkIGZyb20gaXRzIERhcmtuZXQtNTMgYmFja2JvbmUuIEVhY2ggc2NhbGUgdXNlcyAzIGFuY2hvcnMsIGdpdmluZyA5IGFuY2hvcnMgdG90YWwsIHR1bmVkIHRvIGRpZmZlcmVudCBvYmplY3Qgc2l6ZXMuIFRoaXMgbXVsdGktc2NhbGUgYXBwcm9hY2ggZHJhbWF0aWNhbGx5IGltcHJvdmVkIHNtYWxsIG9iamVjdCBkZXRlY3Rpb24gb3ZlciB2MSBhbmQgdjIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgZGVjb2RlX3lvbG92M19wcmVkaWN0aW9ucyhyYXcsIGFuY2hvcnMsIG51bV9jbGFzc2VzLCBpbnB1dF9zaXplKTpcbiAgICBcIlwiXCJcbiAgICByYXc6IFtCLCBudW1fYW5jaG9ycyooNStDKSwgSCwgV11cbiAgICBhbmNob3JzOiBsaXN0IG9mIChwdywgcGgpIGZvciB0aGlzIHNjYWxlXG4gICAgXCJcIlwiXG4gICAgQiwgXywgSCwgVyA9IHJhdy5zaGFwZVxuICAgIG5hID0gbGVuKGFuY2hvcnMpXG4gICAgcHJlZCA9IHJhdy52aWV3KEIsIG5hLCA1ICsgbnVtX2NsYXNzZXMsIEgsIFcpLnBlcm11dGUoMCwxLDMsNCwyKVxuICAgICMgU2lnbW9pZCBmb3IgY2VudGVyIG9mZnNldHMgYW5kIG9iamVjdG5lc3MvY2xhc3Mgc2NvcmVzXG4gICAgcHJlZFsuLi4sIDoyXSA9IHRvcmNoLnNpZ21vaWQocHJlZFsuLi4sIDoyXSkgICAjIGN4LCBjeVxuICAgIHByZWRbLi4uLCA0Ol0gPSB0b3JjaC5zaWdtb2lkKHByZWRbLi4uLCA0Ol0pICAgIyBvYmogKyBjbHNcbiAgICAjIEV4cG9uZW50aWFsIGZvciB3aWR0aC9oZWlnaHQgKHJlbGF0aXZlIHRvIGFuY2hvcilcbiAgICBwdyA9IHRvcmNoLnRlbnNvcihbYVswXSBmb3IgYSBpbiBhbmNob3JzXSkudmlldygxLG5hLDEsMSlcbiAgICBwaCA9IHRvcmNoLnRlbnNvcihbYVsxXSBmb3IgYSBpbiBhbmNob3JzXSkudmlldygxLG5hLDEsMSlcbiAgICBwcmVkWy4uLiwgMl0gPSB0b3JjaC5leHAocHJlZFsuLi4sIDJdKSAqIHB3XG4gICAgcHJlZFsuLi4sIDNdID0gdG9yY2guZXhwKHByZWRbLi4uLCAzXSkgKiBwaFxuICAgIHJldHVybiBwcmVkIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVjb3VwbGVkIEhlYWQgaW4gWU9MT3Y4In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcmlvciBZT0xPIHZlcnNpb25zIHVzZWQgYSBjb3VwbGVkIGRldGVjdGlvbiBoZWFkOiB0aGUgc2FtZSBmZWF0dXJlcyBwcmVkaWN0ZWQgb2JqZWN0bmVzcywgY2xhc3Mgc2NvcmVzLCBhbmQgYm94IGNvb3JkaW5hdGVzIHRvZ2V0aGVyLiBZT0xPdjggYWRvcHRzIGEgZGVjb3VwbGVkIGhlYWQgKHBpb25lZXJlZCBieSBZT0xPWCkgd2l0aCBzZXBhcmF0ZSBicmFuY2hlcyBmb3IgY2xhc3NpZmljYXRpb24gYW5kIHJlZ3Jlc3Npb24uIFRoaXMgcmVkdWNlcyB0YXNrIGludGVyZmVyZW5jZSBhbmQgaW1wcm92ZXMgY29udmVyZ2VuY2UuIFlPTE92OCBhbHNvIGRyb3BzIG9iamVjdG5lc3Mgc2NvcmVzIGVudGlyZWx5LCB1c2luZyBvbmx5IGNsYXNzIGNvbmZpZGVuY2UgYW5kIGJveCBxdWFsaXR5LCBmb2xsb3dpbmcgdGhlIHRyZW5kIGluIGFuY2hvci1mcmVlIGRldGVjdG9ycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSB1bHRyYWx5dGljcyBpbXBvcnQgWU9MT1xuaW1wb3J0IGN2MlxuXG4jIExvYWQgcHJldHJhaW5lZCBZT0xPdjggbmFubyBtb2RlbFxubW9kZWwgPSBZT0xPKFx1MDAyN3lvbG92OG4ucHRcdTAwMjcpXG5cbiMgUnVuIGluZmVyZW5jZSDigJQgcmV0dXJucyBSZXN1bHRzIG9iamVjdFxucmVzdWx0cyA9IG1vZGVsKFx1MDAyN2ltYWdlLmpwZ1x1MDAyNywgY29uZj0wLjI1LCBpb3U9MC40NSlcblxuZm9yIHIgaW4gcmVzdWx0czpcbiAgICBib3hlcyA9IHIuYm94ZXMueHl4eSAgICAjIFtOLCA0XSBhYnNvbHV0ZSBwaXhlbCBjb29yZHNcbiAgICBzY29yZXMgPSByLmJveGVzLmNvbmYgICAjIFtOXSBjb25maWRlbmNlIHNjb3Jlc1xuICAgIGNsYXNzZXMgPSByLmJveGVzLmNscyAgICMgW05dIGNsYXNzIGluZGljZXNcbiAgICBhbm5vdGF0ZWQgPSByLnBsb3QoKSAgICAjIG51bXB5IGFycmF5IHdpdGggYm94ZXMgZHJhd25cbiAgICBjdjIuaW13cml0ZShcdTAwMjdvdXRwdXQuanBnXHUwMDI3LCBhbm5vdGF0ZWQpIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRfdHlwZSI6InRpcCIsImNvbnRlbnQiOiJZT0xPdjggZnJvbSBVbHRyYWx5dGljcyBpcyB0aGUgZWFzaWVzdCBwcm9kdWN0aW9uIHN0YXJ0aW5nIHBvaW50IOKAlCBpdCBpbmNsdWRlcyBhIFB5dGhvbiBBUEksIE9OTlggZXhwb3J0LCBhbmQgc3VwcG9ydHMgZGV0ZWN0aW9uLCBzZWdtZW50YXRpb24sIHBvc2UsIGFuZCBjbGFzc2lmaWNhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyBQaXBlbGluZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiWU9MT3Y1IGFuZCB2OCB0cmFpbmluZyBwaXBlbGluZXMgaW5jbHVkZSBtb3NhaWMgYXVnbWVudGF0aW9uICg0LWltYWdlIGNvbGxhZ2UpLCBjb3B5LXBhc3RlLCBtaXh1cCwgYW5kIHJhbmRvbSBwZXJzcGVjdGl2ZSB0cmFuc2Zvcm1hdGlvbnMuIE1vc2FpYyBpcyBlc3BlY2lhbGx5IGltcGFjdGZ1bCBmb3Igc21hbGwgb2JqZWN0IGRldGVjdGlvbiBiZWNhdXNlIGl0IGZvcmNlcyB0aGUgbW9kZWwgdG8gZGV0ZWN0IG9iamVjdHMgaW4gZGl2ZXJzZSBjb250ZXh0cyBhbmQgYXQgc21hbGxlciBlZmZlY3RpdmUgc2NhbGVzLiBUaGVzZSBhdWdtZW50YXRpb25zIGFyZSBhcHBsaWVkIG9ubGluZSBkdXJpbmcgdHJhaW5pbmcsIHJlcXVpcmluZyBubyBwcmUtZ2VuZXJhdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsb3NzIGZ1bmN0aW9uIGNvbWJpbmVzIHRocmVlIHRlcm1zOiBiaW5hcnkgY3Jvc3MtZW50cm9weSBmb3IgY2xhc3NpZmljYXRpb24sIGJpbmFyeSBjcm9zcy1lbnRyb3B5IGZvciBvYmplY3RuZXNzICh2NSkgb3IgY2xhc3MgcXVhbGl0eSAodjgpLCBhbmQgQ0lvVSBsb3NzIGZvciBib3ggcmVncmVzc2lvbi4gQ0lvVSAoQ29tcGxldGUgSW9VKSBwZW5hbGl6ZXMgZGlzdGFuY2UgYmV0d2VlbiBjZW50ZXJzLCBhc3BlY3QgcmF0aW8gbWlzbWF0Y2gsIGFuZCBvdmVybGFwIOKAlCBtYWtpbmcgaXQgZmFyIG1vcmUgaW5mb3JtYXRpdmUgdGhhbiBMMSBvciBNU0UgbG9zcyBmb3IgYm94IHJlZ3Jlc3Npb24sIGVzcGVjaWFsbHkgZm9yIGVsb25nYXRlZCBvYmplY3RzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGNpb3VfbG9zcyhwcmVkX2JveGVzLCB0YXJnZXRfYm94ZXMsIGVwcz0xZS03KTpcbiAgICBcIlwiXCJDSW9VIGxvc3MgZm9yIFlPTE8gYm94IHJlZ3Jlc3Npb24uIEJveGVzIGluIFtjeCxjeSx3LGhdIGZvcm1hdC5cIlwiXCJcbiAgICAjIENvbXB1dGUgSW9VXG4gICAgYjFfeDEsIGIxX3kxID0gcHJlZF9ib3hlc1s6LDBdLXByZWRfYm94ZXNbOiwyXS8yLCBwcmVkX2JveGVzWzosMV0tcHJlZF9ib3hlc1s6LDNdLzJcbiAgICBiMV94MiwgYjFfeTIgPSBwcmVkX2JveGVzWzosMF0rcHJlZF9ib3hlc1s6LDJdLzIsIHByZWRfYm94ZXNbOiwxXStwcmVkX2JveGVzWzosM10vMlxuICAgIGIyX3gxLCBiMl95MSA9IHRhcmdldF9ib3hlc1s6LDBdLXRhcmdldF9ib3hlc1s6LDJdLzIsIHRhcmdldF9ib3hlc1s6LDFdLXRhcmdldF9ib3hlc1s6LDNdLzJcbiAgICBiMl94MiwgYjJfeTIgPSB0YXJnZXRfYm94ZXNbOiwwXSt0YXJnZXRfYm94ZXNbOiwyXS8yLCB0YXJnZXRfYm94ZXNbOiwxXSt0YXJnZXRfYm94ZXNbOiwzXS8yXG4gICAgaW50ZXIgPSAodG9yY2gubWluKGIxX3gyLGIyX3gyKS10b3JjaC5tYXgoYjFfeDEsYjJfeDEpKS5jbGFtcCgwKSAqIFxcXG4gICAgICAgICAgICAodG9yY2gubWluKGIxX3kyLGIyX3kyKS10b3JjaC5tYXgoYjFfeTEsYjJfeTEpKS5jbGFtcCgwKVxuICAgIHVuaW9uID0gcHJlZF9ib3hlc1s6LDJdKnByZWRfYm94ZXNbOiwzXSArIHRhcmdldF9ib3hlc1s6LDJdKnRhcmdldF9ib3hlc1s6LDNdIC0gaW50ZXIgKyBlcHNcbiAgICBpb3UgPSBpbnRlciAvIHVuaW9uXG4gICAgcmV0dXJuICgxIC0gaW91KS5tZWFuKCkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmVyc2lvbiIsIm1BUCAoQ09DTykiLCJTcGVlZCAoRlBTKSIsIklucHV0IFNpemUiLCJLZXkgSW5ub3ZhdGlvbiJdLCJyb3dzIjpbWyJZT0xPdjEiLCI2My40IChWT0MpIiwiNDUiLCI0NDjDlzQ0OCIsIlVuaWZpZWQgZGV0ZWN0aW9uIGFzIHJlZ3Jlc3Npb24iXSxbIllPTE92MyIsIjU1LjMiLCIyMCIsIjYwOMOXNjA4IiwiTXVsdGktc2NhbGUgcHJlZGljdGlvbiwgRGFya25ldC01MyJdLFsiWU9MT3Y1IiwiNTYuOCIsIjE0MCAobmFubykiLCI2NDDDlzY0MCIsIk1vc2FpYyBhdWdtZW50YXRpb24sIGF1dG8tYW5jaG9yIl0sWyJZT0xPdjciLCI1Ni44IiwiMTYxIiwiNjQww5c2NDAiLCJFLUVMQU4sIGF1eGlsaWFyeSB0cmFpbmluZyBoZWFkcyJdLFsiWU9MT3Y4IiwiNTMuOSAobmFubzogMzcuMykiLCIyMDArIiwiNjQww5c2NDAiLCJEZWNvdXBsZWQgaGVhZCwgYW5jaG9yLWZyZWUiXSxbIllPTE92OSIsIjU1LjYiLCJ+MTAwIiwiNjQww5c2NDAiLCJQcm9ncmFtbWFibGUgZ3JhZGllbnQgaW5mb3JtYXRpb24iXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IllPTE9cdTAwMjdzIGV2b2x1dGlvbiByZWZsZWN0cyB0aGUgYnJvYWRlciB0cmVuZHMgaW4gZGV0ZWN0aW9uOiBmcm9tIGhhbmQtY3JhZnRlZCBhbmNob3JzIHRvIGFuY2hvci1mcmVlIGRlc2lnbnMsIGZyb20gc2luZ2xlLXNjYWxlIHRvIG11bHRpLXNjYWxlIHB5cmFtaWRzLCBmcm9tIGNvdXBsZWQgdG8gZGVjb3VwbGVkIGhlYWRzLiBUaGUgY29uc3RhbnQgYWNyb3NzIGFsbCB2ZXJzaW9ucyBpcyB0aGUgZW1waGFzaXMgb24gaW5mZXJlbmNlIHNwZWVkIHRocm91Z2ggYSBmdWxseSBjb252b2x1dGlvbmFsLCBzaW5nbGUtcGFzcyBkZXNpZ24uIEZvciBhcHBsaWNhdGlvbnMgcmVxdWlyaW5nIHJlYWwtdGltZSBwZXJmb3JtYW5jZSBvbiBlZGdlIGhhcmR3YXJlLCBZT0xPIHJlbWFpbnMgdGhlIGRvbWluYW50IHByYWN0aWNhbCBjaG9pY2UuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGNob29zaW5nIGEgWU9MTyB2YXJpYW50OiB1c2UgWU9MT3Y4biBvciBZT0xPdjhzIGZvciBlZGdlIGRlcGxveW1lbnQgKEpldHNvbiwgbW9iaWxlKSwgWU9MT3Y4bSBvciBsIGZvciBzZXJ2ZXItc2lkZSBiYWxhbmNlZCBhY2N1cmFjeS9zcGVlZCwgYW5kIFlPTE92OHggb3IgWU9MT3Y5IGZvciBtYXhpbXVtIGFjY3VyYWN5LiBBbHdheXMgZmluZS10dW5lIG9uIHlvdXIgZG9tYWluIGRhdGEg4oCUIENPQ08gcHJldHJhaW5lZCB3ZWlnaHRzIHRyYW5zZmVyIHdlbGwgYnV0IGRvbWFpbiBnYXAgaXMgcmVhbCBmb3Igc3BlY2lhbGl6ZWQgb2JqZWN0cyBsaWtlIG1lZGljYWwgZGV2aWNlcywgc2F0ZWxsaXRlIGltYWdlcnksIG9yIG1pY3Jvc2NvcHkuIn1d"
---
# YOLO: Real-Time Single-Stage Detection

## Overview

YOLO (You Only Look Once) redefined real-time object detection by framing it as a single regression problem. Instead of proposing regions then classifying them, YOLO divides the image into a grid and predicts bounding boxes and class probabilities for each cell in one forward pass. This unified approach enables detection at 30–100+ FPS with competitive accuracy.

Since the original 2016 paper, YOLO has evolved through nine major versions. Each version improved accuracy, training stability, and deployment flexibility while preserving the core single-stage, real-time philosophy. Today, YOLOv8 and YOLOv9 from Ultralytics are the most widely deployed detection models in production computer vision systems globally.

## Grid-Based Prediction

YOLOv1 divides the input image into an S×S grid (default 7×7). Each grid cell predicts B bounding boxes (each with x, y, w, h, confidence) and C class probabilities. The network outputs a tensor of shape [S, S, B×5+C]. The cell that contains an object's center is responsible for predicting that object. Box coordinates are normalized relative to the cell's position and size.

```python
import torch

def decode_yolov1_output(output, S=7, B=2, C=80, img_size=448):
    """
    output: [batch, S, S, B*5 + C]
    Returns boxes in [x1, y1, x2, y2] format.
    """
    cell_size = img_size / S
    boxes = output[..., :B*5].reshape(*output.shape[:3], B, 5)
    # cx, cy are offsets within cell -> convert to image coords
    grid_y, grid_x = torch.meshgrid(torch.arange(S), torch.arange(S), indexing='ij')
    boxes[..., 0] = (boxes[..., 0] + grid_x.unsqueeze(-1)) * cell_size
    boxes[..., 1] = (boxes[..., 1] + grid_y.unsqueeze(-1)) * cell_size
    boxes[..., 2] = boxes[..., 2] * img_size  # width
    boxes[..., 3] = boxes[..., 3] * img_size  # height
    return boxes, output[..., B*5:]  # boxes, class_probs
```

## Multi-Scale Detection in YOLOv3+

YOLOv2 introduced anchor boxes (learned cluster centroids from COCO annotations) to improve bounding box prediction stability. YOLOv3 extended this to three detection scales using a FPN-like feature pyramid from its Darknet-53 backbone. Each scale uses 3 anchors, giving 9 anchors total, tuned to different object sizes. This multi-scale approach dramatically improved small object detection over v1 and v2.

```python
import torch
import torch.nn.functional as F

def decode_yolov3_predictions(raw, anchors, num_classes, input_size):
    """
    raw: [B, num_anchors*(5+C), H, W]
    anchors: list of (pw, ph) for this scale
    """
    B, _, H, W = raw.shape
    na = len(anchors)
    pred = raw.view(B, na, 5 + num_classes, H, W).permute(0,1,3,4,2)
    # Sigmoid for center offsets and objectness/class scores
    pred[..., :2] = torch.sigmoid(pred[..., :2])   # cx, cy
    pred[..., 4:] = torch.sigmoid(pred[..., 4:])   # obj + cls
    # Exponential for width/height (relative to anchor)
    pw = torch.tensor([a[0] for a in anchors]).view(1,na,1,1)
    ph = torch.tensor([a[1] for a in anchors]).view(1,na,1,1)
    pred[..., 2] = torch.exp(pred[..., 2]) * pw
    pred[..., 3] = torch.exp(pred[..., 3]) * ph
    return pred
```

## Decoupled Head in YOLOv8

Prior YOLO versions used a coupled detection head: the same features predicted objectness, class scores, and box coordinates together. YOLOv8 adopts a decoupled head (pioneered by YOLOX) with separate branches for classification and regression. This reduces task interference and improves convergence. YOLOv8 also drops objectness scores entirely, using only class confidence and box quality, following the trend in anchor-free detectors.

```python
from ultralytics import YOLO
import cv2

# Load pretrained YOLOv8 nano model
model = YOLO('yolov8n.pt')

# Run inference — returns Results object
results = model('image.jpg', conf=0.25, iou=0.45)

for r in results:
    boxes = r.boxes.xyxy    # [N, 4] absolute pixel coords
    scores = r.boxes.conf   # [N] confidence scores
    classes = r.boxes.cls   # [N] class indices
    annotated = r.plot()    # numpy array with boxes drawn
    cv2.imwrite('output.jpg', annotated)
```

> ****: YOLOv8 from Ultralytics is the easiest production starting point — it includes a Python API, ONNX export, and supports detection, segmentation, pose, and classification.

## Training Pipeline

YOLOv5 and v8 training pipelines include mosaic augmentation (4-image collage), copy-paste, mixup, and random perspective transformations. Mosaic is especially impactful for small object detection because it forces the model to detect objects in diverse contexts and at smaller effective scales. These augmentations are applied online during training, requiring no pre-generation.

The loss function combines three terms: binary cross-entropy for classification, binary cross-entropy for objectness (v5) or class quality (v8), and CIoU loss for box regression. CIoU (Complete IoU) penalizes distance between centers, aspect ratio mismatch, and overlap — making it far more informative than L1 or MSE loss for box regression, especially for elongated objects.

```python
import torch
import torch.nn.functional as F

def ciou_loss(pred_boxes, target_boxes, eps=1e-7):
    """CIoU loss for YOLO box regression. Boxes in [cx,cy,w,h] format."""
    # Compute IoU
    b1_x1, b1_y1 = pred_boxes[:,0]-pred_boxes[:,2]/2, pred_boxes[:,1]-pred_boxes[:,3]/2
    b1_x2, b1_y2 = pred_boxes[:,0]+pred_boxes[:,2]/2, pred_boxes[:,1]+pred_boxes[:,3]/2
    b2_x1, b2_y1 = target_boxes[:,0]-target_boxes[:,2]/2, target_boxes[:,1]-target_boxes[:,3]/2
    b2_x2, b2_y2 = target_boxes[:,0]+target_boxes[:,2]/2, target_boxes[:,1]+target_boxes[:,3]/2
    inter = (torch.min(b1_x2,b2_x2)-torch.max(b1_x1,b2_x1)).clamp(0) * \
            (torch.min(b1_y2,b2_y2)-torch.max(b1_y1,b2_y1)).clamp(0)
    union = pred_boxes[:,2]*pred_boxes[:,3] + target_boxes[:,2]*target_boxes[:,3] - inter + eps
    iou = inter / union
    return (1 - iou).mean()
```

| Version | mAP (COCO) | Speed (FPS) | Input Size | Key Innovation |
| --- | --- | --- | --- | --- |
| YOLOv1 | 63.4 (VOC) | 45 | 448×448 | Unified detection as regression |
| YOLOv3 | 55.3 | 20 | 608×608 | Multi-scale prediction, Darknet-53 |
| YOLOv5 | 56.8 | 140 (nano) | 640×640 | Mosaic augmentation, auto-anchor |
| YOLOv7 | 56.8 | 161 | 640×640 | E-ELAN, auxiliary training heads |
| YOLOv8 | 53.9 (nano: 37.3) | 200+ | 640×640 | Decoupled head, anchor-free |
| YOLOv9 | 55.6 | ~100 | 640×640 | Programmable gradient information |

## Key Takeaways

YOLO's evolution reflects the broader trends in detection: from hand-crafted anchors to anchor-free designs, from single-scale to multi-scale pyramids, from coupled to decoupled heads. The constant across all versions is the emphasis on inference speed through a fully convolutional, single-pass design. For applications requiring real-time performance on edge hardware, YOLO remains the dominant practical choice.

When choosing a YOLO variant: use YOLOv8n or YOLOv8s for edge deployment (Jetson, mobile), YOLOv8m or l for server-side balanced accuracy/speed, and YOLOv8x or YOLOv9 for maximum accuracy. Always fine-tune on your domain data — COCO pretrained weights transfer well but domain gap is real for specialized objects like medical devices, satellite imagery, or microscopy.

