---
title: "Temporal Convolutional Networks (TCN) — Dilated Causal Convolutions"
slug: "temporal-convolutional-networks"
description: "Build TCN architectures using causal and dilated convolutions to achieve exponentially growing receptive fields without sequential computation, and compare training dynamics and accuracy against LSTM baselines."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGVtcG9yYWwgQ29udm9sdXRpb25hbCBOZXR3b3JrcyAoVENOKSBhY2hpZXZlIGxvbmctcmFuZ2UgdGVtcG9yYWwgbW9kZWxsaW5nIHRocm91Z2ggdHdvIGtleSBtb2RpZmljYXRpb25zIHRvIHN0YW5kYXJkIGNvbnZvbHV0aW9uczogY2F1c2FsIHBhZGRpbmcgKGVuc3VyaW5nIG91dHB1dCBhdCB0aW1lIHQgZGVwZW5kcyBvbmx5IG9uIGlucHV0cyBhdCB0LCB0LTEsIC4uLikgYW5kIGRpbGF0aW9uIChleHBhbmRpbmcgdGhlIHJlY2VwdGl2ZSBmaWVsZCBleHBvbmVudGlhbGx5IGJ5IHNraXBwaW5nIHBvc2l0aW9ucyBpbiB0aGUgaW5wdXQpLiBDb21iaW5lZCB3aXRoIHJlc2lkdWFsIGNvbm5lY3Rpb25zIGFuZCB3ZWlnaHQgbm9ybWFsaXNhdGlvbiwgVENOcyBtYXRjaCBvciBvdXRwZXJmb3JtIExTVE1zIG9uIG1hbnkgc2VxdWVuY2UgbW9kZWxsaW5nIGJlbmNobWFya3Mgd2hpbGUgYmVpbmcgZnVsbHkgcGFyYWxsZWxpc2FibGUgYWNyb3NzIHRpbWUg4oCUIGEga2V5IHRyYWluaW5nLWVmZmljaWVuY3kgYWR2YW50YWdlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRocmVlIGRlc2lnbiByZXF1aXJlbWVudHMgZm9yIHNlcXVlbmNlIG1vZGVscyB1c2VkIGluIGZvcmVjYXN0aW5nIGFyZTogKDEpIGNhdXNhbGl0eSDigJQgbm8gaW5mb3JtYXRpb24gZnJvbSBmdXR1cmUgdGltZXN0ZXBzIHNob3VsZCBpbmZsdWVuY2UgdGhlIG91dHB1dCBhdCB0aW1lIHQ7ICgyKSBsb25nIHJlY2VwdGl2ZSBmaWVsZCDigJQgdGhlIG1vZGVsIG11c3QgYmUgYWJsZSB0byBhdHRlbmQgdG8gcGF0dGVybnMgdGhhdCBoYXBwZW5lZCBtYW55IHN0ZXBzIGluIHRoZSBwYXN0LCBzdWNoIGFzIHNlYXNvbmFsIGN5Y2xlczsgKDMpIHN0YWJsZSBncmFkaWVudCBmbG93IOKAlCB2ZXJ5IGRlZXAgbmV0d29ya3Mgc2hvdWxkIG5vdCBzdWZmZXIgZnJvbSB2YW5pc2hpbmcgb3IgZXhwbG9kaW5nIGdyYWRpZW50cyB0aGF0IHByZXZlbnQgY29udmVyZ2VuY2UuIFRDTiBzYXRpc2ZpZXMgYWxsIHRocmVlIHRocm91Z2ggY2F1c2FsIHBhZGRpbmcsIGV4cG9uZW50aWFsbHkgZ3Jvd2luZyBkaWxhdGlvbiwgYW5kIHJlc2lkdWFsIHNob3J0Y3V0cyByZXNwZWN0aXZlbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2F1c2FsIENvbnZvbHV0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBzdGFuZGFyZCAxRCBjb252b2x1dGlvbiB3aXRoIGtlcm5lbCBzaXplIGsgYW5kIHBhZGRpbmcgKGstMSkvMiBpcyBub3QgY2F1c2FsIOKAlCBpdCB1c2VzIGZ1dHVyZSBpbnB1dHMgYXQgcG9zaXRpb24gdCsoay0xKS8yLiBDYXVzYWwgY29udm9sdXRpb24gcGFkcyAoay0xKSB6ZXJvcyB0byB0aGUgbGVmdCBvZiB0aGUgaW5wdXQgKHBhc3Qgc2lkZSkgYW5kIHplcm8gdG8gdGhlIHJpZ2h0LCBzbyB0aGUgb3V0cHV0IGF0IHBvc2l0aW9uIHQgdXNlcyBvbmx5IGlucHV0cyBhdCBwb3NpdGlvbnMgdCwgdC0xLCAuLi4sIHQtKGstMSkuIFdpdGggc3RyaWRlIDEsIGlucHV0IGFuZCBvdXRwdXQgbGVuZ3RoIGFyZSBlcXVhbC4gQ2F1c2FsIGNvbnZvbHV0aW9ucyBhcmUgYSBwcmVyZXF1aXNpdGUgZm9yIGF1dG9yZWdyZXNzaXZlIGZvcmVjYXN0aW5nOiB0aGUgbW9kZWwgY2Fubm90IHBlZWsgYXQgdGhlIGZ1dHVyZSBkdXJpbmcgdHJhaW5pbmcgb3IgaW5mZXJlbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBDYXVzYWxDb252MWQobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJcbiAgICBDYXVzYWwgMUQgY29udm9sdXRpb246IHBhZHMgKGtlcm5lbF9zaXplLTEpKmRpbGF0aW9uIHplcm9zIG9uIHRoZSBsZWZ0LlxuICAgIE91dHB1dCBhdCBwb3NpdGlvbiB0IGRlcGVuZHMgb25seSBvbiBpbnB1dHMgYXQgdCwgdC0xLCAuLi5cbiAgICBcIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2hhbm5lbHMsIG91dF9jaGFubmVscywga2VybmVsX3NpemUsIGRpbGF0aW9uPTEpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5wYWRkaW5nID0gKGtlcm5lbF9zaXplIC0gMSkgKiBkaWxhdGlvblxuICAgICAgICBzZWxmLmNvbnYgPSBubi5Db252MWQoXG4gICAgICAgICAgICBpbl9jaGFubmVscywgb3V0X2NoYW5uZWxzLCBrZXJuZWxfc2l6ZSxcbiAgICAgICAgICAgIGRpbGF0aW9uPWRpbGF0aW9uLCBwYWRkaW5nPXNlbGYucGFkZGluZ1xuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgIyB4OiAoYmF0Y2gsIGNoYW5uZWxzLCB0aW1lKVxuICAgICAgICBvdXQgPSBzZWxmLmNvbnYoeClcbiAgICAgICAgIyBSZW1vdmUgcmlnaHQgcGFkZGluZyB0byByZXN0b3JlIG9yaWdpbmFsIHRpbWUgZGltZW5zaW9uXG4gICAgICAgIHJldHVybiBvdXRbOiwgOiwgOi1zZWxmLnBhZGRpbmddIGlmIHNlbGYucGFkZGluZyBcdTAwM2UgMCBlbHNlIG91dFxuXG4jIFZlcmlmeSBjYXVzYWxpdHk6IG91dHB1dCBhdCB0IHNob3VsZCBub3QgZGVwZW5kIG9uIGZ1dHVyZSBpbnB1dHNcbmJhdGNoLCBDLCBUID0gMiwgMSwgMjBcbnggPSB0b3JjaC5yYW5kbihiYXRjaCwgQywgVClcbmNhdXNhbCA9IENhdXNhbENvbnYxZCgxLCAxLCBrZXJuZWxfc2l6ZT0zLCBkaWxhdGlvbj0yKVxub3V0ID0gY2F1c2FsKHgpXG5wcmludChmXHUwMDI3SW5wdXQgIHNoYXBlOiB7eC5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3T3V0cHV0IHNoYXBlOiB7b3V0LnNoYXBlfSAgKG11c3QgbWF0Y2ggaW5wdXQgdGltZSBkaW0pXHUwMDI3KVxuYXNzZXJ0IG91dC5zaGFwZVsyXSA9PSBULCBcdTAwMjdDYXVzYWwgY29udiBtdXN0IHByZXNlcnZlIHNlcXVlbmNlIGxlbmd0aFx1MDAyN1xucHJpbnQoXHUwMDI3Q2F1c2FsaXR5IGNoZWNrIHBhc3NlZC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGlsYXRlZCBDb252b2x1dGlvbnMgYW5kIFJlY2VwdGl2ZSBGaWVsZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlsYXRlZCBjb252b2x1dGlvbiBhcHBsaWVzIHRoZSBrZXJuZWwgd2l0aCBhIHN0ZXAgb2YgZCAoZGlsYXRpb24gcmF0ZSkgYmV0d2VlbiBrZXJuZWwgcG9zaXRpb25zLiBBIGtlcm5lbCBvZiBzaXplIGsgd2l0aCBkaWxhdGlvbiBkIGhhcyBhbiBlZmZlY3RpdmUgcmVjZXB0aXZlIGZpZWxkIG9mIGTCtyhrLTEpKzEgcGVyIGxheWVyLiBTdGFja2luZyBMIGxheWVycyB3aXRoIGRvdWJsaW5nIGRpbGF0aW9ucyBkPTEsMiw0LC4uLiwyXihMLTEpIGFuZCBrZXJuZWwgc2l6ZSBrIGdpdmVzIHRvdGFsIHJlY2VwdGl2ZSBmaWVsZDogKGstMSnCtygyXkwgLSAxKSArIDEuIFdpdGggaz0zLCBMPTgsIHRoZSByZWNlcHRpdmUgZmllbGQgaXMgNTExIHRpbWUgc3RlcHMg4oCUIGVub3VnaCBmb3IgbW9zdCBwcmFjdGljYWwgc2VyaWVzIOKAlCB1c2luZyBvbmx5IDjCtzI9MTYgY29udm9sdXRpb25hbCBvcGVyYXRpb25zLiBUaGlzIGV4cG9uZW50aWFsIGdyb3d0aCBpcyB0aGUga2V5IGFkdmFudGFnZSBvdmVyIHZhbmlsbGEgY29udm9sdXRpb25zIHRoYXQgbmVlZCBMIGxheWVycyBmb3IgcmVjZXB0aXZlIGZpZWxkIEzCtyhrLTEpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgcmVjZXB0aXZlX2ZpZWxkKGtlcm5lbF9zaXplLCBkaWxhdGlvbnMpOlxuICAgIFwiXCJcIkNvbXB1dGUgVENOIHJlY2VwdGl2ZSBmaWVsZCBmb3IgYSBzdGFjayBvZiBkaWxhdGVkIGNhdXNhbCBjb252cy5cIlwiXCJcbiAgICByZiA9IDFcbiAgICBmb3IgZCBpbiBkaWxhdGlvbnM6XG4gICAgICAgIHJmICs9IChrZXJuZWxfc2l6ZSAtIDEpICogZFxuICAgIHJldHVybiByZlxuXG4jIEV4YW1wbGU6IDMgYmxvY2tzLCBlYWNoIHdpdGggZGlsYXRpb25zIFsxLDIsNCw4XVxua2VybmVsX3NpemUgPSAzXG5kaWxhdGlvbnMgPSBbMSwgMiwgNCwgOF0gKiAzICAjIDMgcmVwZWF0ZWQgYmxvY2tzXG5yZiA9IHJlY2VwdGl2ZV9maWVsZChrZXJuZWxfc2l6ZSwgZGlsYXRpb25zKVxucHJpbnQoZlx1MDAyN0tlcm5lbCBzaXplOiB7a2VybmVsX3NpemV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0RpbGF0aW9uczogICB7ZGlsYXRpb25zfVx1MDAyNylcbnByaW50KGZcdTAwMjdSZWNlcHRpdmUgZmllbGQ6IHtyZn0gdGltZSBzdGVwc1x1MDAyNylcblxuIyBTaG93IFJGIGdyb3d0aCBwZXIgYmxvY2tcbmZvciBuX2xheWVycyBpbiBbMSwgMiwgNCwgOCwgMTJdOlxuICAgIGRfbGlzdCA9IGRpbGF0aW9uc1s6bl9sYXllcnNdXG4gICAgcHJpbnQoZlx1MDAyNyAge25fbGF5ZXJzOjJkfSBsYXllcnMg4oaSIFJGID0ge3JlY2VwdGl2ZV9maWVsZChrZXJuZWxfc2l6ZSwgZF9saXN0KTo0ZH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVENOIFJlc2lkdWFsIEJsb2NrIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWFjaCBUQ04gcmVzaWR1YWwgYmxvY2sgY29uc2lzdHMgb2YgdHdvIGNhdXNhbCBkaWxhdGVkIGNvbnZvbHV0aW9ucyB3aXRoIHdlaWdodCBub3JtYWxpc2F0aW9uIGFuZCBkcm9wb3V0LCBmb2xsb3dlZCBieSBhIHNraXAgY29ubmVjdGlvbjogb3V0cHV0ID0gYWN0aXZhdGlvbihXZWlnaHROb3JtKENhdXNhbENvbnYpIOKGkiBSZUxVIOKGkiBEcm9wb3V0IOKGkiBXZWlnaHROb3JtKENhdXNhbENvbnYpIOKGkiBSZUxVIOKGkiBEcm9wb3V0KSArIHNraXAuIFRoZSBza2lwIGNvbm5lY3Rpb24gdXNlcyBhIDHDlzEgY29udm9sdXRpb24gaWYgdGhlIGNoYW5uZWwgZGltZW5zaW9uIGNoYW5nZXMsIG90aGVyd2lzZSBhbiBpZGVudGl0eSBtYXAuIFJlc2lkdWFsIGNvbm5lY3Rpb25zIHByZXZlbnQgdmFuaXNoaW5nIGdyYWRpZW50cyBpbiBkZWVwIG5ldHdvcmtzICh1cCB0byAzMCsgbGF5ZXJzKSBhbmQgYWxsb3cgdGhlIG5ldHdvcmsgdG8gbGVhcm4gc21hbGwgaW5jcmVtZW50YWwgcmVmaW5lbWVudHMgb3ZlciBlYWNoIGJsb2NrLiBNdWx0aXBsZSBibG9ja3Mgd2l0aCBpbmNyZWFzaW5nIGRpbGF0aW9uIHJhdGVzIGFyZSBzdGFja2VkIHRvIGFjaGlldmUgdGhlIGRlc2lyZWQgcmVjZXB0aXZlIGZpZWxkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBUQ05CbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgb3V0X2NoLCBrZXJuZWxfc2l6ZSwgZGlsYXRpb24sIGRyb3BvdXQ9MC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHBhZCA9IChrZXJuZWxfc2l6ZSAtIDEpICogZGlsYXRpb25cbiAgICAgICAgc2VsZi5jb252MSA9IG5uLnV0aWxzLndlaWdodF9ub3JtKG5uLkNvbnYxZChcbiAgICAgICAgICAgIGluX2NoLCBvdXRfY2gsIGtlcm5lbF9zaXplLCBkaWxhdGlvbj1kaWxhdGlvbiwgcGFkZGluZz1wYWQpKVxuICAgICAgICBzZWxmLmNvbnYyID0gbm4udXRpbHMud2VpZ2h0X25vcm0obm4uQ29udjFkKFxuICAgICAgICAgICAgb3V0X2NoLCBvdXRfY2gsIGtlcm5lbF9zaXplLCBkaWxhdGlvbj1kaWxhdGlvbiwgcGFkZGluZz1wYWQpKVxuICAgICAgICBzZWxmLnJlbHUgICAgPSBubi5SZUxVKClcbiAgICAgICAgc2VsZi5kcm9wb3V0ID0gbm4uRHJvcG91dChkcm9wb3V0KVxuICAgICAgICBzZWxmLnNraXAgICAgPSBubi5Db252MWQoaW5fY2gsIG91dF9jaCwgMSkgaWYgaW5fY2ggIT0gb3V0X2NoIGVsc2Ugbm4uSWRlbnRpdHkoKVxuICAgICAgICBzZWxmLnBhZCAgICAgPSBwYWRcblxuICAgIGRlZiBfY2F1c2FsX3RyaW0oc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiB4WzosIDosIDotc2VsZi5wYWRdIGlmIHNlbGYucGFkIFx1MDAzZSAwIGVsc2UgeFxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG91dCA9IHNlbGYuZHJvcG91dChzZWxmLnJlbHUoc2VsZi5fY2F1c2FsX3RyaW0oc2VsZi5jb252MSh4KSkpKVxuICAgICAgICBvdXQgPSBzZWxmLmRyb3BvdXQoc2VsZi5yZWx1KHNlbGYuX2NhdXNhbF90cmltKHNlbGYuY29udjIob3V0KSkpKVxuICAgICAgICByZXR1cm4gc2VsZi5yZWx1KG91dCArIHNlbGYuc2tpcCh4KSlcblxuY2xhc3MgVENOKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBuX2ZpbHRlcnMsIGtlcm5lbF9zaXplLCBuX2Jsb2NrcywgZHJvcG91dD0wLjEpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgbGF5ZXJzID0gW11cbiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uobl9ibG9ja3MpOlxuICAgICAgICAgICAgZGlsYXRpb24gPSAyICoqIGlcbiAgICAgICAgICAgIGNfaW4gID0gaW5fY2ggaWYgaSA9PSAwIGVsc2Ugbl9maWx0ZXJzXG4gICAgICAgICAgICBsYXllcnMuYXBwZW5kKFRDTkJsb2NrKGNfaW4sIG5fZmlsdGVycywga2VybmVsX3NpemUsIGRpbGF0aW9uLCBkcm9wb3V0KSlcbiAgICAgICAgc2VsZi5uZXQgICAgPSBubi5TZXF1ZW50aWFsKCpsYXllcnMpXG4gICAgICAgIHNlbGYubGluZWFyID0gbm4uTGluZWFyKG5fZmlsdGVycywgMSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICAjIHg6IChiYXRjaCwgZmVhdHVyZXMsIHRpbWUpXG4gICAgICAgIG91dCA9IHNlbGYubmV0KHgpICAgIyAoYmF0Y2gsIG5fZmlsdGVycywgdGltZSlcbiAgICAgICAgcmV0dXJuIHNlbGYubGluZWFyKG91dC50cmFuc3Bvc2UoMSwgMikpICAjIChiYXRjaCwgdGltZSwgMSlcblxubW9kZWwgPSBUQ04oaW5fY2g9MSwgbl9maWx0ZXJzPTMyLCBrZXJuZWxfc2l6ZT0zLCBuX2Jsb2Nrcz02KVxucHJpbnQobW9kZWwpXG50b3RhbF9wYXJhbXMgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSlcbnByaW50KGZcdTAwMjdUb3RhbCBwYXJhbWV0ZXJzOiB7dG90YWxfcGFyYW1zOix9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlY2VwdGl2ZSBGaWVsZCBDYWxjdWxhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVmb3JlIGJ1aWxkaW5nIGEgVENOLCBkZXRlcm1pbmUgdGhlIG1pbmltdW0gcmVjZXB0aXZlIGZpZWxkIG5lZWRlZCB0byBjYXB0dXJlIHRoZSBzZXJpZXNcdTAwMjcgbG9uZ2VzdCByZWxldmFudCBkZXBlbmRlbmN5LiBGb3IgaG91cmx5IGRhdGEgd2l0aCB3ZWVrbHkgc2Vhc29uYWxpdHksIHRoZSByZWNlcHRpdmUgZmllbGQgbXVzdCBjb3ZlciAxNjggdGltZSBzdGVwcyAoNyBkYXlzIMOXIDI0IGhvdXJzKS4gRm9yIGRhaWx5IGRhdGEgd2l0aCBhbm51YWwgc2Vhc29uYWxpdHksIGl0IG11c3QgY292ZXIgMzY1IHN0ZXBzLiBDaG9vc2UgdGhlIG1pbmltdW0gbnVtYmVyIG9mIGJsb2NrcyB0aGF0IGFjaGlldmVzIHRoaXMgUkYgd2l0aCB5b3VyIGNob3NlbiBrZXJuZWwgc2l6ZS4gT3Zlci1wcm92aXNpb25pbmcgdGhlIFJGIHdhc3RlcyBwYXJhbWV0ZXJzIGFuZCBtYXkgcmVxdWlyZSBtb3JlIGRhdGE7IHVuZGVyLXByb3Zpc2lvbmluZyBwcmV2ZW50cyB0aGUgbW9kZWwgZnJvbSBjYXB0dXJpbmcgbG9uZy1yYW5nZSBzZWFzb25hbCBwYXR0ZXJucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgcGFuZGFzIGFzIHBkXG5cbmRlZiB0Y25fcmVjZXB0aXZlX2ZpZWxkKGtlcm5lbF9zaXplLCBuX2Jsb2Nrcywgbl9sYXllcnNfcGVyX2Jsb2NrPTEpOlxuICAgIFwiXCJcIlJlY2VwdGl2ZSBmaWVsZCBmb3IgVENOIHdpdGggZG91YmxpbmcgZGlsYXRpb25zIG92ZXIgbl9ibG9ja3MuXCJcIlwiXG4gICAgZGlsYXRpb25zID0gWzIqKmkgZm9yIGIgaW4gcmFuZ2Uobl9ibG9ja3MpIGZvciBpIGluIHJhbmdlKG5fbGF5ZXJzX3Blcl9ibG9jayldXG4gICAgcmYgPSAxICsgc3VtKChrZXJuZWxfc2l6ZSAtIDEpICogZCBmb3IgZCBpbiBkaWxhdGlvbnMpXG4gICAgcmV0dXJuIHJmLCBkaWxhdGlvbnNcblxucm93cyA9IFtdXG5mb3IgayBpbiBbMiwgMywgNF06XG4gICAgZm9yIG5iIGluIFs0LCA2LCA4LCAxMF06XG4gICAgICAgIHJmLCBfID0gdGNuX3JlY2VwdGl2ZV9maWVsZChrLCBuYilcbiAgICAgICAgcm93cy5hcHBlbmQoe1x1MDAyN2tlcm5lbFx1MDAyNzogaywgXHUwMDI3YmxvY2tzXHUwMDI3OiBuYiwgXHUwMDI3UkZcdTAwMjc6IHJmLCBcdTAwMjdSRl9rXHUwMDI3OiByZiAvLyAxMDAwfSlcblxuZGYgPSBwZC5EYXRhRnJhbWUocm93cylcbnByaW50KGRmLnBpdm90X3RhYmxlKHZhbHVlcz1cdTAwMjdSRlx1MDAyNywgaW5kZXg9XHUwMDI3a2VybmVsXHUwMDI3LCBjb2x1bW5zPVx1MDAyN2Jsb2Nrc1x1MDAyNykudG9fc3RyaW5nKCkpXG5cbiMgUHJhY3RpY2FsIHJlY29tbWVuZGF0aW9uXG50YXJnZXRfcmYgPSAxNjggICMgZS5nLiwgd2Vla2x5IGhvdXJseSBwYXR0ZXJuXG5mb3IgayBpbiBbMiwgM106XG4gICAgZm9yIG5iIGluIHJhbmdlKDEsIDE1KTpcbiAgICAgICAgcmYsIF8gPSB0Y25fcmVjZXB0aXZlX2ZpZWxkKGssIG5iKVxuICAgICAgICBpZiByZiBcdTAwM2U9IHRhcmdldF9yZjpcbiAgICAgICAgICAgIHByaW50KGZcdTAwMjdrZXJuZWw9e2t9LCBibG9ja3M9e25ifSDihpIgUkY9e3JmfSBcdTAwM2U9IHt0YXJnZXRfcmZ9XHUwMDI3KTsgYnJlYWsifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiVENOIHZzIExTVE06IFdoZW4gdG8gUHJlZmVyIEVhY2giLCJjb250ZW50IjoiVENOIGlzIHByZWZlcnJlZCB3aGVuOiAoMSkgdHJhaW5pbmcgZGF0YSBpcyBsYXJnZSAocGFyYWxsZWwgdHJhaW5pbmcgb3ZlciB0aW1lIGlzIGEgc2lnbmlmaWNhbnQgc3BlZWR1cCksICgyKSB0aGUgcmVxdWlyZWQgcmVjZXB0aXZlIGZpZWxkIGlzIGtub3duIGFuZCBmaXhlZCAoZGlsYXRpb25zIGdpdmUgZXhwbGljaXQgY29udHJvbCksICgzKSBncmFkaWVudCBmbG93IG5lZWRzIHRvIGJlIHN0YWJsZSAobm8gTFNUTSBnYXRpbmcgaXNzdWVzKS4gTFNUTSBpcyBwcmVmZXJyZWQgd2hlbjogKDEpIHZhcmlhYmxlLWxlbmd0aCBzZXF1ZW5jZXMgd2l0aG91dCBwYWRkaW5nLCAoMikgc3Ryb25nIHNlcXVlbnRpYWwgaW5kdWN0aXZlIGJpYXMgaXMgZGVzaXJlZCwgKDMpIHRoZSBtb2RlbCBtdXN0IHByb2R1Y2UgYSBoaWRkZW4gc3RhdGUgZm9yIGRvd25zdHJlYW0gdGFza3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmFpbmluZyBhIFRDTiBvbiB0aW1lLXNlcmllcyBkYXRhIGZvbGxvd3MgYSBzbGlkaW5nLXdpbmRvdyBhcHByb2FjaDogY3JlYXRlIGlucHV0LW91dHB1dCBwYWlycyAoeOKCnOKCi0w6dCwgeeKCnOKCiuKCgTp04oKKSCkgd2hlcmUgTCA9IGlucHV0IHdpbmRvdyBsZW5ndGgg4omlIHJlY2VwdGl2ZSBmaWVsZCBhbmQgSCA9IGZvcmVjYXN0IGhvcml6b24uIEZvciBtdWx0aS1zdGVwIG91dHB1dCwgdGhlIFRDTiBoZWFkIG1hcHMgdGhlIGxhc3QgdGltZSBzdGVwXHUwMDI3cyBmZWF0dXJlIHZlY3RvciB0byBIIHZhbHVlcyAoTUlNTykuIFVzZSBBZGFtIHdpdGggbGVhcm5pbmcgcmF0ZSAxZS0zIGFuZCBjb3NpbmUgYW5uZWFsaW5nLiBEcm9wb3V0IHJhdGUgMC4x4oCTMC4yIGJldHdlZW4gdGhlIHR3byBjb252b2x1dGlvbnMgcGVyIGJsb2NrLiBXZWlnaHQgbm9ybWFsaXNhdGlvbiBpcyBwcmVmZXJyZWQgb3ZlciBiYXRjaCBub3JtYWxpc2F0aW9uIGJlY2F1c2UgaXQgaXMgY29tcGF0aWJsZSB3aXRoIHZhcmlhYmxlIHNlcXVlbmNlIGxlbmd0aHMgYW5kIHNtYWxsIGJhdGNoIHNpemVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFyY2hpdGVjdHVyZSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiVENOIiwiTFNUTSIsIlRyYW5zZm9ybWVyIl0sInJvd3MiOltbIlBhcmFsbGVsaXNhYmxlIG92ZXIgdGltZSIsIlllcyDigJQgZnVsbHkgcGFyYWxsZWwiLCJObyDigJQgc2VxdWVudGlhbCBoaWRkZW4gc3RhdGUiLCJZZXMg4oCUIGF0dGVudGlvbiBpcyBwYXJhbGxlbCJdLFsiUmVjZXB0aXZlIGZpZWxkIiwiRXhwb25lbnRpYWwgaW4gZGVwdGggKGV4cGxpY2l0KSIsIlRoZW9yZXRpY2FsbHkgaW5maW5pdGUgKHByYWN0aWNhbCB+NTAtMjAwKSIsIkZ1bGwgc2VxdWVuY2UgKE8oTMKyKSBtZW1vcnkpIl0sWyJHcmFkaWVudCBwYXRoIGxlbmd0aCIsIlNob3J0IOKAlCByZXNpZHVhbCBzaG9ydGN1dHMiLCJHYXRlZCDigJQgdmFuaXNoaW5nIGdyYWRpZW50IG1pdGlnYXRlZCIsIkNvbnN0YW50IOKAlCBhdHRlbnRpb24gc2hvcnRjdXRzIl0sWyJNZW1vcnkgcGVyIHNlcXVlbmNlIiwiTyhMKSDigJQgbm8gaGlkZGVuIHN0YXRlIiwiTyhMwrdkKSDigJQgaGlkZGVuIHN0YXRlcyBmb3IgYWxsIHQiLCJPKEzCsikg4oCUIGF0dGVudGlvbiBtYXRyaXgiXSxbIlBvc2l0aW9uYWwgaW5mb3JtYXRpb24iLCJJbXBsaWNpdCB2aWEgY2F1c2FsIHBhZGRpbmcgb3JkZXIiLCJJbXBsaWNpdCB2aWEgcmVjdXJyZW5jZSIsIkV4cGxpY2l0IHBvc2l0aW9uYWwgZW5jb2RpbmcgbmVlZGVkIl0sWyJQYXJhbWV0ZXIgY291bnQgKGVxdWFsIFJGKSIsIk1vZGVyYXRlIOKAlCBjb252b2x1dGlvbmFsIHdlaWdodHMiLCJNb2RlcmF0ZSDigJQgZ2F0ZSB3ZWlnaHRzIiwiSGlnaCDigJQgUSxLLFYgcHJvamVjdGlvbnMgcGVyIGxheWVyIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVzZSBkaWxhdGlvbiByYXRlcyBbMSwgMiwgNCwgOCwgMTYsIDMyXSAoZG91YmxpbmcpIGZvciBleHBvbmVudGlhbCByZWNlcHRpdmUgZmllbGQgZ3Jvd3RoIHdpdGggbWluaW1hbCBsYXllcnMuIiwiV2VpZ2h0IG5vcm1hbGlzYXRpb24gKG5vdCBiYXRjaCBub3JtYWxpc2F0aW9uKSBpcyBzdGFuZGFyZCBmb3IgVENOIGJlY2F1c2UgaXQgaXMgY29tcGF0aWJsZSB3aXRoIHZhcmlhYmxlLWxlbmd0aCBzZXF1ZW5jZXMuIiwiRHJvcG91dCBiZXR3ZWVuIHRoZSB0d28gY29udm9sdXRpb25zIGluIGVhY2ggYmxvY2sgKG5vdCBhZnRlciByZXNpZHVhbCBhZGRpdGlvbikgaXMgdGhlIHN0YW5kYXJkIFRDTiByZWd1bGFyaXNhdGlvbi4iLCJGb3IgbXVsdGktc3RlcCBmb3JlY2FzdGluZyB3aXRoIFRDTiwgdXNlIGEgTUlNTyBvdXRwdXQgaGVhZDogbGluZWFyIGxheWVyIG1hcHBpbmcgdGhlIGxhc3QgdGltZSBzdGVwXHUwMDI3cyBmZWF0dXJlcyB0byBIIGZ1dHVyZSB2YWx1ZXMuIiwiVENOIG91dHBlcmZvcm1zIExTVE0gb24gdGFza3MgcmVxdWlyaW5nIHZlcnkgbG9uZyBjb250ZXh0IChob3VycyBvZiBhdWRpbywgbW9udGhzIG9mIGhvdXJseSBzZW5zb3IgZGF0YSkgZHVlIHRvIGV4cGxpY2l0IHJlY2VwdGl2ZSBmaWVsZCBjb250cm9sLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRDTiBoYXMgYmVlbiBzdWNjZXNzZnVsbHkgYXBwbGllZCB0byBsb2FkIGZvcmVjYXN0aW5nIChlbGVjdHJpY2l0eSBkZW1hbmQpLCBhbm9tYWx5IGRldGVjdGlvbiBpbiBpbmR1c3RyaWFsIHNlbnNvciBkYXRhLCBhbmQgZmluYW5jaWFsIHZvbGF0aWxpdHkgcHJlZGljdGlvbi4gVGhlIFRlbXBvcmFsIEZ1c2lvbiBUcmFuc2Zvcm1lciAoTGltIGV0IGFsLiwgMjAyMSkgY29tYmluZXMgaWRlYXMgZnJvbSBUQ04gKGdhdGluZywgc2tpcCBjb25uZWN0aW9ucykgd2l0aCBhdHRlbnRpb24gbWVjaGFuaXNtcyBhbmQgdmFyaWFibGUgc2VsZWN0aW9uIG5ldHdvcmtzIGZvciBpbnRlcnByZXRhYmxlIG11bHRpLWhvcml6b24gZm9yZWNhc3Rpbmcgb24gdGFidWxhciB0aW1lIHNlcmllcyDigJQgYSBwcmFjdGljYWwgYXJjaGl0ZWN0dXJlIHRoYXQgYnJpZGdlcyBUQ04gYW5kIFRyYW5zZm9ybWVyIHBhcmFkaWdtcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gcG9ydGluZyBhbiBMU1RNIGJhc2VsaW5lIHRvIGEgVENOOiAoMSkgcmVwbGFjZSB0aGUgTFNUTSBjZWxsIHdpdGggYSBzdGFjayBvZiBUQ05CbG9ja3M7ICgyKSBzZXQgdGhlIHJlY2VwdGl2ZSBmaWVsZCB0byBhdCBsZWFzdCA0w5cgdGhlIGxvbmdlc3Qgc2Vhc29uYWwgcGVyaW9kOyAoMykgcmVwbGFjZSB0aGUgTFNUTSBoaWRkZW4gc3RhdGUgb3V0cHV0IHdpdGggdGhlIFRDTlx1MDAyN3MgbGFzdCB0aW1lLXN0ZXAgZmVhdHVyZSB2ZWN0b3IgZm9yIHRoZSBwcmVkaWN0aW9uIGhlYWQ7ICg0KSB0dW5lIGRyb3BvdXQgaW4gWzAuMDUsIDAuMl0gYW5kIG51bWJlciBvZiBmaWx0ZXJzIGluIFszMiwgMTI4XS4gVXN1YWxseSwgNuKAkzggYmxvY2tzIHdpdGggZG91YmxpbmcgZGlsYXRpb25zIGFuZCBrZXJuZWwgc2l6ZSAzIG9yIDQgYXJlIHN1ZmZpY2llbnQgZm9yIGRhaWx5IG9yIGhvdXJseSBzZXJpZXMgdXAgdG8gMSB5ZWFyIG9mIGNvbnRleHQuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Temporal Convolutional Networks (TCN) — Dilated Causal Convolutions

Temporal Convolutional Networks (TCN) achieve long-range temporal modelling through two key modifications to standard convolutions: causal padding (ensuring output at time t depends only on inputs at t, t-1, ...) and dilation (expanding the receptive field exponentially by skipping positions in the input). Combined with residual connections and weight normalisation, TCNs match or outperform LSTMs on many sequence modelling benchmarks while being fully parallelisable across time — a key training-efficiency advantage.

The three design requirements for sequence models used in forecasting are: (1) causality — no information from future timesteps should influence the output at time t; (2) long receptive field — the model must be able to attend to patterns that happened many steps in the past, such as seasonal cycles; (3) stable gradient flow — very deep networks should not suffer from vanishing or exploding gradients that prevent convergence. TCN satisfies all three through causal padding, exponentially growing dilation, and residual shortcuts respectively.

## Causal Convolutions

A standard 1D convolution with kernel size k and padding (k-1)/2 is not causal — it uses future inputs at position t+(k-1)/2. Causal convolution pads (k-1) zeros to the left of the input (past side) and zero to the right, so the output at position t uses only inputs at positions t, t-1, ..., t-(k-1). With stride 1, input and output length are equal. Causal convolutions are a prerequisite for autoregressive forecasting: the model cannot peek at the future during training or inference.

```python
import torch
import torch.nn as nn

class CausalConv1d(nn.Module):
    """
    Causal 1D convolution: pads (kernel_size-1)*dilation zeros on the left.
    Output at position t depends only on inputs at t, t-1, ...
    """
    def __init__(self, in_channels, out_channels, kernel_size, dilation=1):
        super().__init__()
        self.padding = (kernel_size - 1) * dilation
        self.conv = nn.Conv1d(
            in_channels, out_channels, kernel_size,
            dilation=dilation, padding=self.padding
        )

    def forward(self, x):
        # x: (batch, channels, time)
        out = self.conv(x)
        # Remove right padding to restore original time dimension
        return out[:, :, :-self.padding] if self.padding > 0 else out

# Verify causality: output at t should not depend on future inputs
batch, C, T = 2, 1, 20
x = torch.randn(batch, C, T)
causal = CausalConv1d(1, 1, kernel_size=3, dilation=2)
out = causal(x)
print(f'Input  shape: {x.shape}')
print(f'Output shape: {out.shape}  (must match input time dim)')
assert out.shape[2] == T, 'Causal conv must preserve sequence length'
print('Causality check passed.')
```

## Dilated Convolutions and Receptive Field

Dilated convolution applies the kernel with a step of d (dilation rate) between kernel positions. A kernel of size k with dilation d has an effective receptive field of d·(k-1)+1 per layer. Stacking L layers with doubling dilations d=1,2,4,...,2^(L-1) and kernel size k gives total receptive field: (k-1)·(2^L - 1) + 1. With k=3, L=8, the receptive field is 511 time steps — enough for most practical series — using only 8·2=16 convolutional operations. This exponential growth is the key advantage over vanilla convolutions that need L layers for receptive field L·(k-1).

```python
import torch
import torch.nn as nn

def receptive_field(kernel_size, dilations):
    """Compute TCN receptive field for a stack of dilated causal convs."""
    rf = 1
    for d in dilations:
        rf += (kernel_size - 1) * d
    return rf

# Example: 3 blocks, each with dilations [1,2,4,8]
kernel_size = 3
dilations = [1, 2, 4, 8] * 3  # 3 repeated blocks
rf = receptive_field(kernel_size, dilations)
print(f'Kernel size: {kernel_size}')
print(f'Dilations:   {dilations}')
print(f'Receptive field: {rf} time steps')

# Show RF growth per block
for n_layers in [1, 2, 4, 8, 12]:
    d_list = dilations[:n_layers]
    print(f'  {n_layers:2d} layers → RF = {receptive_field(kernel_size, d_list):4d}')
```

## TCN Residual Block Architecture

Each TCN residual block consists of two causal dilated convolutions with weight normalisation and dropout, followed by a skip connection: output = activation(WeightNorm(CausalConv) → ReLU → Dropout → WeightNorm(CausalConv) → ReLU → Dropout) + skip. The skip connection uses a 1×1 convolution if the channel dimension changes, otherwise an identity map. Residual connections prevent vanishing gradients in deep networks (up to 30+ layers) and allow the network to learn small incremental refinements over each block. Multiple blocks with increasing dilation rates are stacked to achieve the desired receptive field.

```python
import torch
import torch.nn as nn

class TCNBlock(nn.Module):
    def __init__(self, in_ch, out_ch, kernel_size, dilation, dropout=0.1):
        super().__init__()
        pad = (kernel_size - 1) * dilation
        self.conv1 = nn.utils.weight_norm(nn.Conv1d(
            in_ch, out_ch, kernel_size, dilation=dilation, padding=pad))
        self.conv2 = nn.utils.weight_norm(nn.Conv1d(
            out_ch, out_ch, kernel_size, dilation=dilation, padding=pad))
        self.relu    = nn.ReLU()
        self.dropout = nn.Dropout(dropout)
        self.skip    = nn.Conv1d(in_ch, out_ch, 1) if in_ch != out_ch else nn.Identity()
        self.pad     = pad

    def _causal_trim(self, x):
        return x[:, :, :-self.pad] if self.pad > 0 else x

    def forward(self, x):
        out = self.dropout(self.relu(self._causal_trim(self.conv1(x))))
        out = self.dropout(self.relu(self._causal_trim(self.conv2(out))))
        return self.relu(out + self.skip(x))

class TCN(nn.Module):
    def __init__(self, in_ch, n_filters, kernel_size, n_blocks, dropout=0.1):
        super().__init__()
        layers = []
        for i in range(n_blocks):
            dilation = 2 ** i
            c_in  = in_ch if i == 0 else n_filters
            layers.append(TCNBlock(c_in, n_filters, kernel_size, dilation, dropout))
        self.net    = nn.Sequential(*layers)
        self.linear = nn.Linear(n_filters, 1)

    def forward(self, x):
        # x: (batch, features, time)
        out = self.net(x)   # (batch, n_filters, time)
        return self.linear(out.transpose(1, 2))  # (batch, time, 1)

model = TCN(in_ch=1, n_filters=32, kernel_size=3, n_blocks=6)
print(model)
total_params = sum(p.numel() for p in model.parameters())
print(f'Total parameters: {total_params:,}')
```

## Receptive Field Calculation

Before building a TCN, determine the minimum receptive field needed to capture the series' longest relevant dependency. For hourly data with weekly seasonality, the receptive field must cover 168 time steps (7 days × 24 hours). For daily data with annual seasonality, it must cover 365 steps. Choose the minimum number of blocks that achieves this RF with your chosen kernel size. Over-provisioning the RF wastes parameters and may require more data; under-provisioning prevents the model from capturing long-range seasonal patterns.

```python
import numpy as np
import pandas as pd

def tcn_receptive_field(kernel_size, n_blocks, n_layers_per_block=1):
    """Receptive field for TCN with doubling dilations over n_blocks."""
    dilations = [2**i for b in range(n_blocks) for i in range(n_layers_per_block)]
    rf = 1 + sum((kernel_size - 1) * d for d in dilations)
    return rf, dilations

rows = []
for k in [2, 3, 4]:
    for nb in [4, 6, 8, 10]:
        rf, _ = tcn_receptive_field(k, nb)
        rows.append({'kernel': k, 'blocks': nb, 'RF': rf, 'RF_k': rf // 1000})

df = pd.DataFrame(rows)
print(df.pivot_table(values='RF', index='kernel', columns='blocks').to_string())

# Practical recommendation
target_rf = 168  # e.g., weekly hourly pattern
for k in [2, 3]:
    for nb in range(1, 15):
        rf, _ = tcn_receptive_field(k, nb)
        if rf >= target_rf:
            print(f'kernel={k}, blocks={nb} → RF={rf} >= {target_rf}'); break
```

> **TCN vs LSTM: When to Prefer Each**: TCN is preferred when: (1) training data is large (parallel training over time is a significant speedup), (2) the required receptive field is known and fixed (dilations give explicit control), (3) gradient flow needs to be stable (no LSTM gating issues). LSTM is preferred when: (1) variable-length sequences without padding, (2) strong sequential inductive bias is desired, (3) the model must produce a hidden state for downstream tasks.

Training a TCN on time-series data follows a sliding-window approach: create input-output pairs (xₜ₋L:t, yₜ₊₁:t₊H) where L = input window length ≥ receptive field and H = forecast horizon. For multi-step output, the TCN head maps the last time step's feature vector to H values (MIMO). Use Adam with learning rate 1e-3 and cosine annealing. Dropout rate 0.1–0.2 between the two convolutions per block. Weight normalisation is preferred over batch normalisation because it is compatible with variable sequence lengths and small batch sizes.

## Architecture Comparison

| Property | TCN | LSTM | Transformer |
| --- | --- | --- | --- |
| Parallelisable over time | Yes — fully parallel | No — sequential hidden state | Yes — attention is parallel |
| Receptive field | Exponential in depth (explicit) | Theoretically infinite (practical ~50-200) | Full sequence (O(L²) memory) |
| Gradient path length | Short — residual shortcuts | Gated — vanishing gradient mitigated | Constant — attention shortcuts |
| Memory per sequence | O(L) — no hidden state | O(L·d) — hidden states for all t | O(L²) — attention matrix |
| Positional information | Implicit via causal padding order | Implicit via recurrence | Explicit positional encoding needed |
| Parameter count (equal RF) | Moderate — convolutional weights | Moderate — gate weights | High — Q,K,V projections per layer |

- Use dilation rates [1, 2, 4, 8, 16, 32] (doubling) for exponential receptive field growth with minimal layers.
- Weight normalisation (not batch normalisation) is standard for TCN because it is compatible with variable-length sequences.
- Dropout between the two convolutions in each block (not after residual addition) is the standard TCN regularisation.
- For multi-step forecasting with TCN, use a MIMO output head: linear layer mapping the last time step's features to H future values.
- TCN outperforms LSTM on tasks requiring very long context (hours of audio, months of hourly sensor data) due to explicit receptive field control.

TCN has been successfully applied to load forecasting (electricity demand), anomaly detection in industrial sensor data, and financial volatility prediction. The Temporal Fusion Transformer (Lim et al., 2021) combines ideas from TCN (gating, skip connections) with attention mechanisms and variable selection networks for interpretable multi-horizon forecasting on tabular time series — a practical architecture that bridges TCN and Transformer paradigms.

When porting an LSTM baseline to a TCN: (1) replace the LSTM cell with a stack of TCNBlocks; (2) set the receptive field to at least 4× the longest seasonal period; (3) replace the LSTM hidden state output with the TCN's last time-step feature vector for the prediction head; (4) tune dropout in [0.05, 0.2] and number of filters in [32, 128]. Usually, 6–8 blocks with doubling dilations and kernel size 3 or 4 are sufficient for daily or hourly series up to 1 year of context.

---

