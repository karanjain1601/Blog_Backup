---
title: "FCOS: Anchor-Free Object Detection"
slug: "fcos-anchor-free-detection"
description: "FCOS detects objects per pixel without anchors — predicting (l,r,t,b) distances to box edges, centerness scores to suppress off-center predictions, and multi-level features from FPN."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImgyIiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGQ09TIChGdWxseSBDb252b2x1dGlvbmFsIE9uZS1TdGFnZSBkZXRlY3RvcikgZWxpbWluYXRlcyB0aGUgYW5jaG9yIGh5cGVycGFyYW1ldGVycyB0aGF0IHBsYWd1ZSBSZXRpbmFOZXQgYW5kIEZhc3RlciBSLUNOTi4gRWFjaCBGUE4gbG9jYXRpb24gaW5kZXBlbmRlbnRseSBwcmVkaWN0cyB3aGV0aGVyIGl0IGZhbGxzIGluc2lkZSBhIGdyb3VuZC10cnV0aCBib3ggYW5kLCBpZiBzbywgcmVncmVzc2VzIHRoZSBkaXN0YW5jZXMgdG8gYWxsIGZvdXIgYm94IGVkZ2VzLiBUaGlzIHBlci1waXhlbCBmb3JtdWxhdGlvbiByZW1vdmVzIE5NUyBzZW5zaXRpdml0eSB0byBhbmNob3Igc2l6ZSBhbmQgYXNwZWN0IHJhdGlvLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBpbnNpZ2h0IGlzIHRoYXQgYW55IHBvaW50IGluc2lkZSBhIGdyb3VuZC10cnV0aCBib3VuZGluZyBib3ggaXMgYSB2YWxpZCBwb3NpdGl2ZSBzYW1wbGUuIEZDT1MgYXNzaWducyBlYWNoIEZQTiBsZXZlbCBhIHNpemUgcmFuZ2Ugc28gc21hbGwgb2JqZWN0cyBhcmUgZGV0ZWN0ZWQgb24gaGlnaC1yZXNvbHV0aW9uIGxldmVscyBhbmQgbGFyZ2Ugb2JqZWN0cyBvbiBsb3ctcmVzb2x1dGlvbiBsZXZlbHMsIHByZXZlbnRpbmcgc2NhbGUgYW1iaWd1aXR5IGFjcm9zcyBsZXZlbHMuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiUGVyLVBvaW50IEJveCBSZWdyZXNzaW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZXZlcnkgc3BhdGlhbCBsb2NhdGlvbiAoeCwgeSkgb24gYW4gRlBOIGZlYXR1cmUgbWFwLCBGQ09TIHJlZ3Jlc3NlcyBmb3VyIGRpc3RhbmNlczogbCAobGVmdCksIHIgKHJpZ2h0KSwgdCAodG9wKSwgYiAoYm90dG9tKSDigJQgdGhlIGRpc3RhbmNlIGZyb20gdGhlIHBvaW50IHRvIGVhY2ggZWRnZSBvZiB0aGUgYXNzaWduZWQgZ3JvdW5kLXRydXRoIGJveC4gVGhlIGZpbmFsIGJveCBpcyByZWNvdmVyZWQgYXMgKHjiiJJsLCB54oiSdCwgeCtyLCB5K2IpLCBtYWtpbmcgdGhlIHJlZ3Jlc3Npb24gdGFyZ2V0IGFsd2F5cyBwb3NpdGl2ZSBhbmQgYm91bmRlZCBieSBvYmplY3Qgc2l6ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGNvbXB1dGVfZmNvc190YXJnZXRzKGxvY2F0aW9ucywgZ3RfYm94ZXMsIHNpemVfcmFuZ2UpOlxuICAgICMgbG9jYXRpb25zOiAoTiwyKSB4LHkgb24gRlBOIGxldmVsXG4gICAgIyBndF9ib3hlczogKE0sNCkgeDEseTEseDIseTJcbiAgICB4cywgeXMgPSBsb2NhdGlvbnNbOiwgMF0sIGxvY2F0aW9uc1s6LCAxXVxuICAgIGwgPSB4c1s6LCBOb25lXSAtIGd0X2JveGVzW05vbmUsIDosIDBdICAjIChOLE0pXG4gICAgdCA9IHlzWzosIE5vbmVdIC0gZ3RfYm94ZXNbTm9uZSwgOiwgMV1cbiAgICByID0gZ3RfYm94ZXNbTm9uZSwgOiwgMl0gLSB4c1s6LCBOb25lXVxuICAgIGIgPSBndF9ib3hlc1tOb25lLCA6LCAzXSAtIHlzWzosIE5vbmVdXG4gICAgbHRyYiA9IHRvcmNoLnN0YWNrKFtsLCB0LCByLCBiXSwgZGltPS0xKSAgIyAoTixNLDQpXG4gICAgaW5zaWRlID0gbHRyYi5taW4oLTEpLnZhbHVlcyBcdTAwM2UgMFxuICAgIG1heF9yZWcgPSBsdHJiLm1heCgtMSkudmFsdWVzXG4gICAgaW5fcmFuZ2UgPSAobWF4X3JlZyBcdTAwM2U9IHNpemVfcmFuZ2VbMF0pIFx1MDAyNiAobWF4X3JlZyBcdTAwM2M9IHNpemVfcmFuZ2VbMV0pXG4gICAgcmV0dXJuIGx0cmIsIGluc2lkZSBcdTAwMjYgaW5fcmFuZ2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gYSBsb2NhdGlvbiBmYWxscyBpbnNpZGUgbXVsdGlwbGUgZ3JvdW5kLXRydXRoIGJveGVzLCBGQ09TIGFzc2lnbnMgaXQgdG8gdGhlIHNtYWxsZXN0IGJveCBieSBhcmVhLiBUaGlzIGhldXJpc3RpYyBoYW5kbGVzIGNyb3dkZWQgc2NlbmVzIHJlYXNvbmFibHkgd2VsbCBidXQgaXMgbGVzcyBwcmluY2lwbGVkIHRoYW4gbGF0ZXIgbWV0aG9kcyBsaWtlIEFUU1MsIHdoaWNoIHVzZSBzdGF0aXN0aWNhbCBvdmVybGFwIHRvIGRldGVybWluZSBwb3NpdGl2ZSBzYW1wbGVzIGFkYXB0aXZlbHkuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiQ2VudGVybmVzcyBTY29yZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBwYXJhbGxlbCBicmFuY2ggcHJlZGljdHMgYSBjZW50ZXJuZXNzIHNjb3JlIGZvciBlYWNoIHBvc2l0aXZlIGxvY2F0aW9uLiBDZW50ZXJuZXNzIGlzIDEgYXQgdGhlIGJveCBjZW50ZXIgYW5kIGZhbGxzIG9mZiB0b3dhcmQgZWRnZXMsIGFjdGluZyBhcyBzb2Z0IHN1cHByZXNzaW9uIG9mIGxvdy1xdWFsaXR5IHByZWRpY3Rpb25zIHdpdGhvdXQgcmVxdWlyaW5nIGFkZGl0aW9uYWwgTk1TIHR1bmluZy4gQXQgaW5mZXJlbmNlLCBjbGFzc2lmaWNhdGlvbiBjb25maWRlbmNlIGlzIG11bHRpcGxpZWQgYnkgY2VudGVybmVzcyB0byByYW5rIHByb3Bvc2Fscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGNlbnRlcm5lc3NfdGFyZ2V0KGx0cmIpOlxuICAgIFwiXCJcIlxuICAgIGx0cmI6IChOLCA0KSB0ZW5zb3Igb2YgKGwsIHQsIHIsIGIpIGRpc3RhbmNlc1xuICAgIFJldHVybnMgY2VudGVybmVzcyBpbiBbMCwgMV0sIHBlYWtzIGF0IGJveCBjZW50ZXIuXG4gICAgXCJcIlwiXG4gICAgbCwgdCwgciwgYiA9IGx0cmIudW5iaW5kKC0xKVxuICAgIGNlbnRlcm5lc3MgPSB0b3JjaC5zcXJ0KFxuICAgICAgICAodG9yY2gubWluaW11bShsLCByKSAvIHRvcmNoLm1heGltdW0obCwgcikuY2xhbXAobWluPTFlLTYpKSAqXG4gICAgICAgICh0b3JjaC5taW5pbXVtKHQsIGIpIC8gdG9yY2gubWF4aW11bSh0LCBiKS5jbGFtcChtaW49MWUtNikpXG4gICAgKVxuICAgIHJldHVybiBjZW50ZXJuZXNzICAjIDEuMCBhdCBjZW50ZXIsIDAgYXQgY29ybmVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2VudGVybmVzcyByYW5nZXMgZnJvbSAwIHRvIDEuIEF0IHRoZSBleGFjdCBjZW50ZXIgb2YgYSBib3gsIG1pbihsLHIpPW1heChsLHIpIGFuZCBtaW4odCxiKT1tYXgodCxiKSwgc28gYm90aCByYXRpb3MgZXF1YWwgMSBhbmQgY2VudGVybmVzcyBlcXVhbHMgMS4gTmVhciBjb3JuZXJzLCByYXRpb3MgYXBwcm9hY2ggMC4gVGhpcyBlbGVnYW50IGZvcm11bGF0aW9uIHJlcXVpcmVzIG5vIGFkZGl0aW9uYWwgaHlwZXJwYXJhbWV0ZXJzIGFuZCBnZW5lcmFsaXNlcyBhY3Jvc3Mgb2JqZWN0IHNoYXBlcy4ifSx7InR5cGUiOiJoMiIsImNvbnRlbnQiOiJUYXJnZXQgQXNzaWdubWVudCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRkNPUyBhc3NpZ25zIEZQTiBsZXZlbHMgYnkgb2JqZWN0IHNpemU6IFAzIGhhbmRsZXMgb2JqZWN0cyB3aXRoIG1heChsLHIsdCxiKSBpbiBbMCw2NF0sIFA0IGluIFs2NCwxMjhdLCBQNSBpbiBbMTI4LDI1Nl0sIFA2IGluIFsyNTYsNTEyXSwgUDcgaW4gWzUxMiziiJ5dLiBBbnkgbG9jYXRpb24gd2hvc2UgbWF4IHJlZ3Jlc3Npb24gdGFyZ2V0IGZhbGxzIG91dHNpZGUgdGhlIGxldmVsXHUwMDI3cyByYW5nZSBpcyB0cmVhdGVkIGFzIGJhY2tncm91bmQuIFRoaXMgaGllcmFyY2hpY2FsIGFzc2lnbm1lbnQgc2VwYXJhdGVzIHNjYWxlIHNlbnNpdGl2aXR5IGNsZWFubHkuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRldGVjdG9yIiwiQW5jaG9ycyIsIkFzc2lnbm1lbnQgc3RyYXRlZ3kiLCJBbWJpZ3VpdHkgaGFuZGxpbmciLCJDT0NPIG1BUCJdLCJyb3dzIjpbWyJGYXN0ZXIgUi1DTk4iLCJNdWx0aS1zY2FsZSBhbmNob3JzIiwiSW9VIHdpdGggYW5jaG9ycyDiiaUgMC43IiwiU3VwcHJlc3NlZCBieSBOTVMiLCIzNy45Il0sWyJSZXRpbmFOZXQiLCJNdWx0aS1zY2FsZSBhbmNob3JzIiwiSW9VIHdpdGggYW5jaG9ycyDiiaUgMC41IiwiRm9jYWwgbG9zcyIsIjM5LjEiXSxbIkZDT1MiLCJOb25lIiwiUG9pbnQtaW4tYm94ICsgc2l6ZSByYW5nZSIsIkNlbnRlcm5lc3MgYnJhbmNoIiwiNDIuMSJdLFsiQVRTUyIsIk9uZSBwZXIgbG9jYXRpb24iLCJBZGFwdGl2ZSB0b3BrIGJ5IHN0ZChJb1UpIiwiQ2VudGVybmVzcyBicmFuY2giLCI0My42Il0sWyJHRkwiLCJOb25lIiwiQVRTUy1zdHlsZSBhZGFwdGl2ZSIsIlF1YWxpdHkgZm9jYWwgbG9zcyIsIjQ1LjAiXV19LHsidHlwZSI6ImgyIiwiY29udGVudCI6IkZDT1MgVHJhaW5pbmcgTG9zcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRkNPUyBvcHRpbWlzZXMgdGhyZWUgbG9zc2VzIGpvaW50bHk6IGZvY2FsIGxvc3Mgb24gdGhlIGNsYXNzaWZpY2F0aW9uIGJyYW5jaCAoaGFuZGxlcyBjbGFzcyBpbWJhbGFuY2Ugd2l0aG91dCBoYXJkIG1pbmluZyksIElvVSBsb3NzIG9uIHRoZSBib3ggcmVncmVzc2lvbiBicmFuY2ggKHNjYWxlLWludmFyaWFudCBhbmQgZGlyZWN0bHkgb3B0aW1pc2VzIHRoZSBmaW5hbCBtZXRyaWMpLCBhbmQgYmluYXJ5IGNyb3NzLWVudHJvcHkgb24gdGhlIGNlbnRlcm5lc3MgYnJhbmNoLiBPbmx5IHBvc2l0aXZlIGxvY2F0aW9ucyBjb250cmlidXRlIHRvIHJlZ3Jlc3Npb24gYW5kIGNlbnRlcm5lc3MgbG9zcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmZyb20gdG9yY2h2aXNpb24ub3BzIGltcG9ydCBzaWdtb2lkX2ZvY2FsX2xvc3MsIGJveF9pb3VcblxuZGVmIGZjb3NfbG9zcyhjbHNfcHJlZCwgcmVnX3ByZWQsIGN0cl9wcmVkLCBjbHNfdGd0LCBsdHJiX3RndCwgY3RyX3RndCwgcG9zX21hc2spOlxuICAgICMgQ2xhc3NpZmljYXRpb246IGZvY2FsIGxvc3Mgb3ZlciBhbGwgbG9jYXRpb25zXG4gICAgY2xzX2xvc3MgPSBzaWdtb2lkX2ZvY2FsX2xvc3MoY2xzX3ByZWQsIGNsc190Z3QsIHJlZHVjdGlvbj1cdTAwMjdzdW1cdTAwMjcpXG4gICAgaWYgcG9zX21hc2suc3VtKCkgPT0gMDpcbiAgICAgICAgcmV0dXJuIGNsc19sb3NzLCBjbHNfcHJlZC5uZXdfdGVuc29yKDAuKSwgY2xzX3ByZWQubmV3X3RlbnNvcigwLilcbiAgICAjIElvVSBsb3NzIG9uIHBvc2l0aXZlcyBvbmx5XG4gICAgcmVnX2xvc3MgPSAoMSAtIGJveF9pb3VfZnJvbV9sdHJiKHJlZ19wcmVkW3Bvc19tYXNrXSwgbHRyYl90Z3RbcG9zX21hc2tdKSkubWVhbigpXG4gICAgIyBDZW50ZXJuZXNzIEJDRSBvbiBwb3NpdGl2ZXNcbiAgICBjdHJfbG9zcyA9IEYuYmluYXJ5X2Nyb3NzX2VudHJvcHlfd2l0aF9sb2dpdHMoY3RyX3ByZWRbcG9zX21hc2tdLCBjdHJfdGd0W3Bvc19tYXNrXSlcbiAgICByZXR1cm4gY2xzX2xvc3MgLyBwb3NfbWFzay5zdW0oKSwgcmVnX2xvc3MsIGN0cl9sb3NzIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRUeXBlIjoiaW5mbyIsImNvbnRlbnQiOiJDZW50ZXJuZXNzIGlzIHRoZSBrZXkgdHJpY2s6IGl0IGRvd24td2VpZ2h0cyBwcmVkaWN0aW9ucyBmYXIgZnJvbSBvYmplY3QgY2VudGVycywgZWZmZWN0aXZlbHkgYWN0aW5nIGxpa2UgTk1TIHN1cHByZXNzaW9uIHdpdGhvdXQgcmVxdWlyaW5nIGFuY2hvciBkZXNpZ24uIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgZGVjb2RlX2Zjb3Nfb3V0cHV0KGNlbnRlcnMsIGx0cmIpOlxuICAgIFwiXCJcIlxuICAgIFJlY292ZXIgYm91bmRpbmcgYm94ZXMgZnJvbSBGQ09TIG91dHB1dHMuXG4gICAgY2VudGVyczogKE4sIDIpIOKAlCAoY3gsIGN5KSBwaXhlbCBjb29yZHMgb24gb3JpZ2luYWwgaW1hZ2VcbiAgICBsdHJiOiAgICAoTiwgNCkg4oCUIHByZWRpY3RlZCAobCwgdCwgciwgYikgZGlzdGFuY2VzXG4gICAgUmV0dXJuczogKE4sIDQpIGJveGVzIGFzICh4MSwgeTEsIHgyLCB5MilcbiAgICBcIlwiXCJcbiAgICBjeCwgY3kgPSBjZW50ZXJzWzosIDBdLCBjZW50ZXJzWzosIDFdXG4gICAgbCwgdCwgciwgYiA9IGx0cmJbOiwgMF0sIGx0cmJbOiwgMV0sIGx0cmJbOiwgMl0sIGx0cmJbOiwgM11cbiAgICB4MSA9IGN4IC0gbFxuICAgIHkxID0gY3kgLSB0XG4gICAgeDIgPSBjeCArIHJcbiAgICB5MiA9IGN5ICsgYlxuICAgIHJldHVybiB0b3JjaC5zdGFjayhbeDEsIHkxLCB4MiwgeTJdLCBkaW09LTEpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGQ09TIHNob3dlZCB0aGF0IGFuY2hvci1mcmVlIGRldGVjdGlvbiBtYXRjaGVzIG9yIGV4Y2VlZHMgYW5jaG9yLWJhc2VkIG1ldGhvZHMgd2l0aCBzaW1wbGVyIGltcGxlbWVudGF0aW9uLiBJdHMgcGVyLXBvaW50IHJlZ3Jlc3Npb24sIEZQTiBsZXZlbCBhc3NpZ25tZW50LCBhbmQgY2VudGVybmVzcyB0cmljayBiZWNhbWUgYSB0ZW1wbGF0ZSBmb3Igc3Vic2VxdWVudCBkZXRlY3RvcnMgaW5jbHVkaW5nIEFUU1MgYW5kIEdGTCwgd2hpY2ggcmVmaW5lZCB0aGUgYXNzaWdubWVudCBzdHJhdGVneSB3aGlsZSByZXRhaW5pbmcgdGhlIGFuY2hvci1mcmVlIHJlZ3Jlc3Npb24gaGVhZC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByYWN0aWNhbCB0aXBzOiB1c2UgR04gKEdyb3VwIE5vcm0pIG9uIHRoZSBkZXRlY3Rpb24gaGVhZCByYXRoZXIgdGhhbiBCTiBmb3Igc3RhYmxlIHRyYWluaW5nIGFjcm9zcyB2YXJ5aW5nIGJhdGNoIHNpemVzLiBFeHBvbmVudGlhbCBhY3RpdmF0aW9uIG9uIHRoZSByZWdyZXNzaW9uIG91dHB1dCBlbnN1cmVzIHBvc2l0aXZlIGRpc3RhbmNlIHByZWRpY3Rpb25zLiBDZW50ZXJuZXNzLXdlaWdodGVkIElvVSBsb3NzIChtdWx0aXBseSBJb1UgbG9zcyBieSBjZW50ZXJuZXNzIHRhcmdldCkgcHJvdmlkZXMgYSBtYXJnaW5hbCBidXQgY29uc2lzdGVudCBpbXByb3ZlbWVudCBvdmVyIHBsYWluIElvVSBsb3NzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRkNPUyBpcyBhdmFpbGFibGUgaW4gdG9yY2h2aXNpb24gKHRvcmNodmlzaW9uLm1vZGVscy5kZXRlY3Rpb24uZmNvc19yZXNuZXQ1MF9mcG4pIGFuZCBpbiBNTURldGVjdGlvbi4gQm90aCBwcm92aWRlIHByZXRyYWluZWQgQ09DTyB3ZWlnaHRzLiBNTURldGVjdGlvblx1MDAyN3MgY29uZmlnIGFsbG93cyBzd2FwcGluZyB0aGUgYmFja2JvbmUgdG8gU3dpbiBUcmFuc2Zvcm1lciBvciBDb252TmVYdCBmb3IgaGlnaGVyIGFjY3VyYWN5IGF0IG1vZGVzdCBpbmZlcmVuY2UgY29zdC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtYWluIHdlYWtuZXNzIG9mIHZhbmlsbGEgRkNPUyBpcyBhbWJpZ3VpdHkgd2hlbiBvYmplY3RzIGhlYXZpbHkgb3ZlcmxhcCDigJQgdHdvIG9iamVjdHMgb2YgZGlmZmVyZW50IHNpemVzIHNoYXJpbmcgdGhlIHNhbWUgY2VudGVyIHBpeGVsIGNhbm5vdCBib3RoIGJlIHBvc2l0aXZlIG9uIGFueSBzaW5nbGUgRlBOIGxldmVsLiBBVFNTIGFkZHJlc3NlcyB0aGlzIGJ5IGFkYXB0aXZlIHN0YXRpc3RpY2FsIHRocmVzaG9sZGluZyByYXRoZXIgdGhhbiBmaXhlZCBzaXplIHJhbmdlcywgeWllbGRpbmcgKzEtMiBtQVAgd2l0aG91dCBhZGRpdGlvbmFsIGNvbXB1dGUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZGVwbG95bWVudCwgRkNPUyBleHBvcnRzIGNsZWFubHkgdG8gT05OWCBhbmQgVGVuc29yUlQuIFRoZSB0aHJlZSBvdXRwdXQgaGVhZHMgKGNsYXNzaWZpY2F0aW9uLCByZWdyZXNzaW9uLCBjZW50ZXJuZXNzKSBkZWNvZGUgaW5kZXBlbmRlbnRseSBwZXIgbG9jYXRpb24gYW5kIGFyZSBhbWVuYWJsZSB0byBJTlQ4IHF1YW50aXNhdGlvbi4gUG9zdC1wcm9jZXNzaW5nIChjZW50ZXJuZXNzLXdlaWdodGVkIHNjb3JlICsgTk1TKSBydW5zIGVmZmljaWVudGx5IG9uIENQVSBmb3IgYmF0Y2ggc2l6ZSAxIGluZmVyZW5jZSBwaXBlbGluZXMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGZpbmUtdHVuaW5nIEZDT1Mgb24gYSBjdXN0b20gZGF0YXNldDogZnJlZXplIHRoZSBGUE4gYmFja2JvbmUgZm9yIHRoZSBmaXJzdCBmZXcgZXBvY2hzLCB1c2UgYSB3YXJtLXVwIExSIHNjaGVkdWxlLCBhbmQgbW9uaXRvciBjZW50ZXJuZXNzIGxvc3Mgc2VwYXJhdGVseSDigJQgaWYgaXQgZGl2ZXJnZXMgZWFybHkgaXQgaW5kaWNhdGVzIHRoZSBwb3NpdGl2ZS9uZWdhdGl2ZSBhc3NpZ25tZW50IGlzIG1pc2NvbmZpZ3VyZWQgZm9yIHlvdXIgb2JqZWN0IHNpemVzLiJ9XQ=="
---
# FCOS: Anchor-Free Object Detection

FCOS (Fully Convolutional One-Stage detector) eliminates the anchor hyperparameters that plague RetinaNet and Faster R-CNN. Each FPN location independently predicts whether it falls inside a ground-truth box and, if so, regresses the distances to all four box edges. This per-pixel formulation removes NMS sensitivity to anchor size and aspect ratio.

The key insight is that any point inside a ground-truth bounding box is a valid positive sample. FCOS assigns each FPN level a size range so small objects are detected on high-resolution levels and large objects on low-resolution levels, preventing scale ambiguity across levels.

For every spatial location (x, y) on an FPN feature map, FCOS regresses four distances: l (left), r (right), t (top), b (bottom) — the distance from the point to each edge of the assigned ground-truth box. The final box is recovered as (x−l, y−t, x+r, y+b), making the regression target always positive and bounded by object size.

```
import torch

def compute_fcos_targets(locations, gt_boxes, size_range):
    # locations: (N,2) x,y on FPN level
    # gt_boxes: (M,4) x1,y1,x2,y2
    xs, ys = locations[:, 0], locations[:, 1]
    l = xs[:, None] - gt_boxes[None, :, 0]  # (N,M)
    t = ys[:, None] - gt_boxes[None, :, 1]
    r = gt_boxes[None, :, 2] - xs[:, None]
    b = gt_boxes[None, :, 3] - ys[:, None]
    ltrb = torch.stack([l, t, r, b], dim=-1)  # (N,M,4)
    inside = ltrb.min(-1).values > 0
    max_reg = ltrb.max(-1).values
    in_range = (max_reg >= size_range[0]) & (max_reg <= size_range[1])
    return ltrb, inside & in_range
```

When a location falls inside multiple ground-truth boxes, FCOS assigns it to the smallest box by area. This heuristic handles crowded scenes reasonably well but is less principled than later methods like ATSS, which use statistical overlap to determine positive samples adaptively.

A parallel branch predicts a centerness score for each positive location. Centerness is 1 at the box center and falls off toward edges, acting as soft suppression of low-quality predictions without requiring additional NMS tuning. At inference, classification confidence is multiplied by centerness to rank proposals.

```
import torch

def centerness_target(ltrb):
    """
    ltrb: (N, 4) tensor of (l, t, r, b) distances
    Returns centerness in [0, 1], peaks at box center.
    """
    l, t, r, b = ltrb.unbind(-1)
    centerness = torch.sqrt(
        (torch.minimum(l, r) / torch.maximum(l, r).clamp(min=1e-6)) *
        (torch.minimum(t, b) / torch.maximum(t, b).clamp(min=1e-6))
    )
    return centerness  # 1.0 at center, 0 at corners
```

Centerness ranges from 0 to 1. At the exact center of a box, min(l,r)=max(l,r) and min(t,b)=max(t,b), so both ratios equal 1 and centerness equals 1. Near corners, ratios approach 0. This elegant formulation requires no additional hyperparameters and generalises across object shapes.

FCOS assigns FPN levels by object size: P3 handles objects with max(l,r,t,b) in [0,64], P4 in [64,128], P5 in [128,256], P6 in [256,512], P7 in [512,∞]. Any location whose max regression target falls outside the level's range is treated as background. This hierarchical assignment separates scale sensitivity cleanly.

| Detector | Anchors | Assignment strategy | Ambiguity handling | COCO mAP |
| --- | --- | --- | --- | --- |
| Faster R-CNN | Multi-scale anchors | IoU with anchors ≥ 0.7 | Suppressed by NMS | 37.9 |
| RetinaNet | Multi-scale anchors | IoU with anchors ≥ 0.5 | Focal loss | 39.1 |
| FCOS | None | Point-in-box + size range | Centerness branch | 42.1 |
| ATSS | One per location | Adaptive topk by std(IoU) | Centerness branch | 43.6 |
| GFL | None | ATSS-style adaptive | Quality focal loss | 45.0 |

FCOS optimises three losses jointly: focal loss on the classification branch (handles class imbalance without hard mining), IoU loss on the box regression branch (scale-invariant and directly optimises the final metric), and binary cross-entropy on the centerness branch. Only positive locations contribute to regression and centerness loss.

```
import torch
import torch.nn.functional as F
from torchvision.ops import sigmoid_focal_loss, box_iou

def fcos_loss(cls_pred, reg_pred, ctr_pred, cls_tgt, ltrb_tgt, ctr_tgt, pos_mask):
    # Classification: focal loss over all locations
    cls_loss = sigmoid_focal_loss(cls_pred, cls_tgt, reduction='sum')
    if pos_mask.sum() == 0:
        return cls_loss, cls_pred.new_tensor(0.), cls_pred.new_tensor(0.)
    # IoU loss on positives only
    reg_loss = (1 - box_iou_from_ltrb(reg_pred[pos_mask], ltrb_tgt[pos_mask])).mean()
    # Centerness BCE on positives
    ctr_loss = F.binary_cross_entropy_with_logits(ctr_pred[pos_mask], ctr_tgt[pos_mask])
    return cls_loss / pos_mask.sum(), reg_loss, ctr_loss
```

> ****: Centerness is the key trick: it down-weights predictions far from object centers, effectively acting like NMS suppression without requiring anchor design.

```
import torch

def decode_fcos_output(centers, ltrb):
    """
    Recover bounding boxes from FCOS outputs.
    centers: (N, 2) — (cx, cy) pixel coords on original image
    ltrb:    (N, 4) — predicted (l, t, r, b) distances
    Returns: (N, 4) boxes as (x1, y1, x2, y2)
    """
    cx, cy = centers[:, 0], centers[:, 1]
    l, t, r, b = ltrb[:, 0], ltrb[:, 1], ltrb[:, 2], ltrb[:, 3]
    x1 = cx - l
    y1 = cy - t
    x2 = cx + r
    y2 = cy + b
    return torch.stack([x1, y1, x2, y2], dim=-1)
```

FCOS showed that anchor-free detection matches or exceeds anchor-based methods with simpler implementation. Its per-point regression, FPN level assignment, and centerness trick became a template for subsequent detectors including ATSS and GFL, which refined the assignment strategy while retaining the anchor-free regression head.

Practical tips: use GN (Group Norm) on the detection head rather than BN for stable training across varying batch sizes. Exponential activation on the regression output ensures positive distance predictions. Centerness-weighted IoU loss (multiply IoU loss by centerness target) provides a marginal but consistent improvement over plain IoU loss.

FCOS is available in torchvision (torchvision.models.detection.fcos_resnet50_fpn) and in MMDetection. Both provide pretrained COCO weights. MMDetection's config allows swapping the backbone to Swin Transformer or ConvNeXt for higher accuracy at modest inference cost.

The main weakness of vanilla FCOS is ambiguity when objects heavily overlap — two objects of different sizes sharing the same center pixel cannot both be positive on any single FPN level. ATSS addresses this by adaptive statistical thresholding rather than fixed size ranges, yielding +1-2 mAP without additional compute.

For deployment, FCOS exports cleanly to ONNX and TensorRT. The three output heads (classification, regression, centerness) decode independently per location and are amenable to INT8 quantisation. Post-processing (centerness-weighted score + NMS) runs efficiently on CPU for batch size 1 inference pipelines.

When fine-tuning FCOS on a custom dataset: freeze the FPN backbone for the first few epochs, use a warm-up LR schedule, and monitor centerness loss separately — if it diverges early it indicates the positive/negative assignment is misconfigured for your object sizes.

