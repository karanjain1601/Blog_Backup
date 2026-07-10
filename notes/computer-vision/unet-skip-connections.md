---
title: "U-Net: Encoder-Decoder with Skip Connections"
slug: "unet-skip-connections"
description: "U-Net architecture for dense prediction — symmetric encoder-decoder, skip connections that concatenate high-resolution features, and applications in medical image segmentation."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVLU5ldCAoUm9ubmViZXJnZXIgZXQgYWwuLCAyMDE1KSB3YXMgZGVzaWduZWQgZm9yIGJpb21lZGljYWwgaW1hZ2Ugc2VnbWVudGF0aW9uIHdoZXJlIGxhYmVsbGVkIGRhdGEgaXMgc2NhcmNlLiBJdHMgc3ltbWV0cmljIGVuY29kZXItZGVjb2RlciB3aXRoIHNraXAgY29ubmVjdGlvbnMgYWxsb3dzIHRoZSBuZXR3b3JrIHRvIGNvbWJpbmUgZGVlcCBzZW1hbnRpYyBmZWF0dXJlcyB3aXRoIGhpZ2gtcmVzb2x1dGlvbiBzcGF0aWFsIGRldGFpbC4gVHJhaW5lZCB3aXRoIGFnZ3Jlc3NpdmUgYXVnbWVudGF0aW9uLCBVLU5ldCBhY2hpZXZlcyBzdHJvbmcgcmVzdWx0cyBldmVuIHdpdGggYSBmZXcgZG96ZW4gdHJhaW5pbmcgaW1hZ2VzIOKAlCBtYWtpbmcgaXQgdGhlIGRvbWluYW50IGFyY2hpdGVjdHVyZSBpbiBtZWRpY2FsIGltYWdpbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbmFtZSBjb21lcyBmcm9tIGl0cyBVLXNoYXBlZCBhcmNoaXRlY3R1cmU6IHRoZSBlbmNvZGVyIGNvbnRyYWN0cyB0aGUgc3BhdGlhbCBkaW1lbnNpb25zIHdoaWxlIGluY3JlYXNpbmcgY2hhbm5lbHM7IHRoZSBkZWNvZGVyIG1pcnJvcnMgdGhpcyBwYXRoLCBleHBhbmRpbmcgYmFjayB0byBpbnB1dCByZXNvbHV0aW9uLiBFYWNoIGxldmVsIG9mIHRoZSBlbmNvZGVyIGNvbm5lY3RzIGRpcmVjdGx5IHRvIHRoZSBjb3JyZXNwb25kaW5nIGRlY29kZXIgbGV2ZWwgdmlhIGEgc2tpcCBjb25uZWN0aW9uIHRoYXQgY29uY2F0ZW5hdGVzIGZlYXR1cmUgbWFwcywgcHJlc2VydmluZyBmaW5lLWdyYWluZWQgc3BhdGlhbCBpbmZvcm1hdGlvbiB0aHJvdWdob3V0IHRoZSB1cHNhbXBsaW5nIHBhdGguIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRW5jb2RlciBQYXRoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZW5jb2RlciBmb2xsb3dzIGEgc3RhbmRhcmQgQ05OIHBhdHRlcm46IHJlcGVhdGVkIGJsb2NrcyBvZiB0d28gM8OXMyBjb252b2x1dGlvbnMgKGVhY2ggZm9sbG93ZWQgYnkgYmF0Y2ggbm9ybWFsaXNhdGlvbiBhbmQgUmVMVSksIHRoZW4gMsOXMiBtYXggcG9vbGluZyB3aXRoIHN0cmlkZSAyLiBFYWNoIHBvb2xpbmcgc3RlcCBoYWx2ZXMgdGhlIHNwYXRpYWwgZGltZW5zaW9ucyBhbmQgZG91YmxlcyB0aGUgY2hhbm5lbHMsIHByb2dyZXNzaXZlbHkgYnVpbGRpbmcgdXAgYW4gYWJzdHJhY3Qgc2VtYW50aWMgcmVwcmVzZW50YXRpb24uIFRoZSBmaW5hbCBlbmNvZGVyIG91dHB1dCDigJQgdGhlIGJvdHRsZW5lY2sg4oCUIGNhcHR1cmVzIHRoZSBtb3N0IGNvbXByZXNzZWQsIHNlbWFudGljYWxseSByaWNoIGZlYXR1cmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgRW5jb2RlckJsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBvdXRfY2gpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5jb252ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAzLCBwYWRkaW5nPTEpLCBubi5CYXRjaE5vcm0yZChvdXRfY2gpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQob3V0X2NoLCBvdXRfY2gsIDMsIHBhZGRpbmc9MSksIG5uLkJhdGNoTm9ybTJkKG91dF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuICAgICAgICApXG4gICAgICAgIHNlbGYucG9vbCA9IG5uLk1heFBvb2wyZCgyKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGZlYXR1cmVzID0gc2VsZi5jb252KHgpICAgIyBzYXZlIGZvciBza2lwIGNvbm5lY3Rpb25cbiAgICAgICAgcmV0dXJuIHNlbGYucG9vbChmZWF0dXJlcyksIGZlYXR1cmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcmUtdHJhaW5lZCBlbmNvZGVycyAoUmVzTmV0LCBFZmZpY2llbnROZXQpIGFyZSBvZnRlbiB1c2VkIGFzIGRyb3AtaW4gcmVwbGFjZW1lbnRzIGZvciB0aGUgaGFuZC1kZXNpZ25lZCBlbmNvZGVyLiBUaGlzIHRyYW5zZmVyIGxlYXJuaW5nIGZyb20gSW1hZ2VOZXQgcHJvdmlkZXMgYSBzdHJvbmcgaW5pdGlhbGlzYXRpb24sIHJlZHVjaW5nIHRyYWluaW5nIHRpbWUgYW5kIGRhdGEgcmVxdWlyZW1lbnRzLiBMaWJyYXJpZXMgbGlrZSBzZWdtZW50YXRpb24tbW9kZWxzLXB5dG9yY2ggbWFrZSBpdCBlYXN5IHRvIHN3YXAgZW5jb2RlcnMgd2hpbGUga2VlcGluZyB0aGUgVS1OZXQgZGVjb2RlciBzdHJ1Y3R1cmUgYW5kIHNraXAgY29ubmVjdGlvbiB3aXJpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVjb2RlciBQYXRoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZGVjb2RlciBtaXJyb3JzIHRoZSBlbmNvZGVyOiBhdCBlYWNoIGxldmVsLCB0aGUgZmVhdHVyZSBtYXAgaXMgdXBzYW1wbGVkIGJ5IDLDlyAoYmlsaW5lYXIgaW50ZXJwb2xhdGlvbiBvciB0cmFuc3Bvc2VkIGNvbnZvbHV0aW9uKSwgY29uY2F0ZW5hdGVkIHdpdGggdGhlIGNvcnJlc3BvbmRpbmcgZW5jb2RlciBza2lwIGZlYXR1cmVzLCB0aGVuIHByb2Nlc3NlZCBieSB0d28gM8OXMyBjb252LUJOLVJlTFUgYmxvY2tzLiBUaGlzIHByb2dyZXNzaXZlbHkgcmVmaW5lcyB0aGUgY29hcnNlIGJvdHRsZW5lY2sgcmVwcmVzZW50YXRpb24gaW50byBhIGZ1bGwtcmVzb2x1dGlvbiBzZWdtZW50YXRpb24gbWFwIHdpdGggZmluZSBib3VuZGFyeSBkZXRhaWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIERlY29kZXJCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgc2tpcF9jaCwgb3V0X2NoKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYudXAgPSBubi5VcHNhbXBsZShzY2FsZV9mYWN0b3I9MiwgbW9kZT1cdTAwMjdiaWxpbmVhclx1MDAyNywgYWxpZ25fY29ybmVycz1UcnVlKVxuICAgICAgICBzZWxmLmNvbnYgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoICsgc2tpcF9jaCwgb3V0X2NoLCAzLCBwYWRkaW5nPTEpLCBubi5CYXRjaE5vcm0yZChvdXRfY2gpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQob3V0X2NoLCBvdXRfY2gsIDMsIHBhZGRpbmc9MSksIG5uLkJhdGNoTm9ybTJkKG91dF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBza2lwKTpcbiAgICAgICAgeCA9IHNlbGYudXAoeClcbiAgICAgICAgcmV0dXJuIHNlbGYuY29udih0b3JjaC5jYXQoW3gsIHNraXBdLCBkaW09MSkpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmFuc3Bvc2VkIGNvbnZvbHV0aW9ucyAoc29tZXRpbWVzIGNhbGxlZCBkZWNvbnZvbHV0aW9ucykgYXJlIGFuIGFsdGVybmF0aXZlIHRvIGJpbGluZWFyIHVwc2FtcGxpbmcuIFRoZXkgYXJlIGxlYXJuYWJsZSwgYnV0IGNhbiBpbnRyb2R1Y2UgY2hlY2tlcmJvYXJkIGFydGVmYWN0cyBpZiBub3QgY2FyZWZ1bGx5IGluaXRpYWxpc2VkLiBJbiBwcmFjdGljZSwgYmlsaW5lYXIgdXBzYW1wbGluZyBmb2xsb3dlZCBieSBhIHJlZ3VsYXIgY29udm9sdXRpb24gdGVuZHMgdG8gcHJvZHVjZSBjbGVhbmVyIHJlc3VsdHMgYW5kIGlzIHByZWZlcnJlZCBpbiBtb3N0IG1vZGVybiBVLU5ldCBpbXBsZW1lbnRhdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2tpcCBDb25uZWN0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2tpcCBjb25uZWN0aW9ucyBhcmUgdGhlIGRlZmluaW5nIGZlYXR1cmUgb2YgVS1OZXQuIFRoZXkgZGlyZWN0bHkgcm91dGUgZmVhdHVyZSBtYXBzIGZyb20gdGhlIGVuY29kZXIgdG8gdGhlIGNvcnJlc3BvbmRpbmcgZGVjb2RlciBsZXZlbCwgYnlwYXNzaW5nIHRoZSBib3R0bGVuZWNrLiBUaGlzIGdpdmVzIHRoZSBkZWNvZGVyIGFjY2VzcyB0byBib3RoIGNvYXJzZSBzZW1hbnRpYyBjb250ZXh0IChmcm9tIHRoZSBkZWVwIGJvdHRsZW5lY2spIGFuZCBwcmVjaXNlIHNwYXRpYWwgZGV0YWlsIChmcm9tIHRoZSBzaGFsbG93IGVuY29kZXIgZmVhdHVyZXMpLiBXaXRob3V0IHNraXAgY29ubmVjdGlvbnMsIGZpbmUgc3RydWN0dXJlcyBsaWtlIGNlbGwgYm91bmRhcmllcyBvciB2ZXNzZWwgZWRnZXMgdGVuZCB0byBibHVyIG91dC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgVU5ldChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaD0xLCBudW1fY2xhc3Nlcz0yKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jMSA9IEVuY29kZXJCbG9jayhpbl9jaCwgNjQpXG4gICAgICAgIHNlbGYuZW5jMiA9IEVuY29kZXJCbG9jayg2NCwgMTI4KVxuICAgICAgICBzZWxmLmVuYzMgPSBFbmNvZGVyQmxvY2soMTI4LCAyNTYpXG4gICAgICAgIHNlbGYuZW5jNCA9IEVuY29kZXJCbG9jaygyNTYsIDUxMilcbiAgICAgICAgc2VsZi5ib3R0bGVuZWNrID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZCg1MTIsIDEwMjQsIDMsIHBhZGRpbmc9MSksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZCgxMDI0LCAxMDI0LCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcbiAgICAgICAgKVxuICAgICAgICBzZWxmLmRlYzQgPSBEZWNvZGVyQmxvY2soMTAyNCwgNTEyLCA1MTIpXG4gICAgICAgIHNlbGYuZGVjMyA9IERlY29kZXJCbG9jayg1MTIsIDI1NiwgMjU2KVxuICAgICAgICBzZWxmLmRlYzIgPSBEZWNvZGVyQmxvY2soMjU2LCAxMjgsIDEyOClcbiAgICAgICAgc2VsZi5kZWMxID0gRGVjb2RlckJsb2NrKDEyOCwgNjQsIDY0KVxuICAgICAgICBzZWxmLmhlYWQgPSBubi5Db252MmQoNjQsIG51bV9jbGFzc2VzLCAxKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVS1OZXQrKyBuZXN0cyBkZW5zZSBza2lwIGNvbm5lY3Rpb25zIGJldHdlZW4gZW5jb2RlciBhbmQgZGVjb2RlciBub2RlcywgY3JlYXRpbmcgYW4gZW5zZW1ibGUgb2YgVS1OZXRzIG9mIHZhcnlpbmcgZGVwdGhzLiBUaGlzIGhlbHBzIHdoZW4gdGhlIG9wdGltYWwgZGVwdGggaXMgdW5rbm93biwgYXMgaW50ZXJtZWRpYXRlIHByZWRpY3Rpb25zIGNhbiBiZSB1c2VkIGZvciBkZWVwIHN1cGVydmlzaW9uLiBUaGUgZG93bnNpZGUgaXMgaW5jcmVhc2VkIHBhcmFtZXRlciBjb3VudCBhbmQgbWVtb3J5LCBidXQgdGhlIGltcHJvdmVtZW50IGluIG1Jb1Ugb24gbWVkaWNhbCBpbWFnaW5nIGJlbmNobWFya3MgaXMgY29uc2lzdGVudCBhY3Jvc3MgZGF0YXNldHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVS1OZXQgZm9yIE1lZGljYWwgSW1hZ2luZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWVkaWNhbCBpbWFnZSBzZWdtZW50YXRpb24gcHJlc2VudHMgdW5pcXVlIGNoYWxsZW5nZXM6IDNEIHZvbHVtZXMgKENUL01SSSksIGhpZ2ggY2xhc3MgaW1iYWxhbmNlIChzbWFsbCBsZXNpb25zIGluIGxhcmdlIGJhY2tncm91bmRzKSwgbGltaXRlZCBsYWJlbGxlZCBkYXRhLCBhbmQgZG9tYWluIHNoaWZ0IGJldHdlZW4gc2Nhbm5lcnMgb3IgaW5zdGl0dXRpb25zLiBVLU5ldCBhZGRyZXNzZXMgdGhlc2UgdGhyb3VnaCBhZ2dyZXNzaXZlIGF1Z21lbnRhdGlvbiAoZWxhc3RpYyBkZWZvcm1hdGlvbiwgcm90YXRpb24sIGZsaXBwaW5nKSBhbmQgbG9zcyBmdW5jdGlvbnMgdGhhdCBoYW5kbGUgaW1iYWxhbmNlLCBzdWNoIGFzIERpY2UgbG9zcyBvciBhIHdlaWdodGVkIGNvbWJpbmF0aW9uIG9mIERpY2UgYW5kIGJpbmFyeSBjcm9zcy1lbnRyb3B5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGRpY2VfbG9zcyhwcmVkLCB0YXJnZXQsIHNtb290aD0xLjApOlxuICAgICMgcHJlZDogKEIsIEMsIEgsIFcpIGxvZ2l0czsgdGFyZ2V0OiAoQiwgSCwgVykgbG9uZ1xuICAgIHByZWQgPSB0b3JjaC5zb2Z0bWF4KHByZWQsIGRpbT0xKVxuICAgIHRhcmdldF9vaCA9IEYub25lX2hvdCh0YXJnZXQsIHByZWQuc2hhcGVbMV0pLnBlcm11dGUoMCwzLDEsMikuZmxvYXQoKVxuICAgIGludGVyID0gKHByZWQgKiB0YXJnZXRfb2gpLnN1bShkaW09KDIsIDMpKVxuICAgIHVuaW9uID0gcHJlZC5zdW0oZGltPSgyLCAzKSkgKyB0YXJnZXRfb2guc3VtKGRpbT0oMiwgMykpXG4gICAgZGljZSA9ICgyICogaW50ZXIgKyBzbW9vdGgpIC8gKHVuaW9uICsgc21vb3RoKVxuICAgIHJldHVybiAxIC0gZGljZS5tZWFuKClcblxuZGVmIGNvbWJpbmVkX2xvc3MocHJlZCwgdGFyZ2V0KTpcbiAgICByZXR1cm4gZGljZV9sb3NzKHByZWQsIHRhcmdldCkgKyBGLmNyb3NzX2VudHJvcHkocHJlZCwgdGFyZ2V0KSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJVLU5ldCB2YXJpYW50IiwiU2tpcCBjb25uZWN0aW9uIiwiS2V5IGNoYW5nZSIsIkFwcGxpY2F0aW9uIl0sInJvd3MiOltbIlUtTmV0IG9yaWdpbmFsIiwiQ29uY2F0ZW5hdGlvbiIsIlN5bW1ldHJpYyBlbmNvZGVyLWRlY29kZXIiLCJCaW9tZWRpY2FsIHNlZ21lbnRhdGlvbiJdLFsiVS1OZXQrKyIsIkRlbnNlIG5lc3RlZCIsIlN1Yi1uZXR3b3JrcyBvZiB2YXJ5aW5nIGRlcHRoIiwiTXVsdGktb3JnYW4sIHBhdGhvbG9neSJdLFsiQXR0ZW50aW9uIFUtTmV0IiwiQXR0ZW50aW9uIGdhdGVzIG9uIHNraXAiLCJTdXBwcmVzcyBpcnJlbGV2YW50IGZlYXR1cmVzIiwiUHJvc3RhdGUsIENUIG9yZ2FucyJdLFsiUmVzaWR1YWwgVS1OZXQiLCJSZXNpZHVhbCArIHNraXAiLCJSZXNOZXQgYmxvY2tzIGluIGVuY29kZXIiLCJSZXRpbmFsIHZlc3NlbHMsIGRlcm1vc2NvcHkiXSxbIm5uVS1OZXQiLCJDb25jYXRlbmF0aW9uIiwiQXV0by1jb25maWcgZm9yIGFueSBkYXRhc2V0IiwiTWVkaWNhbCBpbWFnaW5nIGNvbXBldGl0aW9ucyJdXX0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRfdHlwZSI6InRpcCIsImNvbnRlbnQiOiJublUtTmV0IGF1dG9tYXRpY2FsbHkgY29uZmlndXJlcyBVLU5ldCBoeXBlcnBhcmFtZXRlcnMgKHBhdGNoIHNpemUsIGJhdGNoIHNpemUsIGF1Z21lbnRhdGlvbikgZm9yIGFueSBtZWRpY2FsIGltYWdpbmcgZGF0YXNldCDigJQgaXRcdTAwMjdzIHRoZSBnby10byBiYXNlbGluZSBiZWZvcmUgY3VzdG9tIGFyY2hpdGVjdHVyZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVS1OZXRcdTAwMjdzIGVsZWdhbmNlIGxpZXMgaW4gaXRzIHN5bW1ldHJpYyBzdHJ1Y3R1cmUgYW5kIHNraXAgY29ubmVjdGlvbnMsIHdoaWNoIGNvbWJpbmUgdGhlIGJlc3Qgb2YgYm90aCB3b3JsZHM6IHNlbWFudGljIGRlcHRoIGZyb20gdGhlIGVuY29kZXIgYm90dGxlbmVjayBhbmQgc3BhdGlhbCBwcmVjaXNpb24gZnJvbSBlYXJseSBlbmNvZGVyIGZlYXR1cmVzLiBUaGVzZSBwcm9wZXJ0aWVzIG1ha2UgaXQgbmVhci11bml2ZXJzYWxseSBhcHBsaWNhYmxlIGluIG1lZGljYWwgaW1hZ2luZywgcmVtb3RlIHNlbnNpbmcsIGFuZCBhbnkgZG9tYWluIHJlcXVpcmluZyBwcmVjaXNlIGJvdW5kYXJ5IGRlbGluZWF0aW9uIHdpdGggbGltaXRlZCB0cmFpbmluZyBkYXRhLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiBzdGFydGluZyBhIG5ldyBzZWdtZW50YXRpb24gcHJvamVjdCwgdHJ5IG5uVS1OZXQgZmlyc3Qg4oCUIGl0IGhhbmRsZXMgcHJlcHJvY2Vzc2luZywgYXVnbWVudGF0aW9uLCBhbmQgaHlwZXJwYXJhbWV0ZXIgc2VsZWN0aW9uIGF1dG9tYXRpY2FsbHkgYW5kIHNlcnZlcyBhcyBhIHN0cm9uZyBiYXNlbGluZS4gRm9yIG5hdHVyYWwgaW1hZ2VzLCBjb21iaW5lIGEgcHJldHJhaW5lZCBFZmZpY2llbnROZXQgb3IgUmVzTmV0IGVuY29kZXIgd2l0aCBhIFUtTmV0IGRlY29kZXIgdXNpbmcgc2VnbWVudGF0aW9uLW1vZGVscy1weXRvcmNoLiBBbHdheXMgdXNlIERpY2UgbG9zcyBvciBjb21iaW5lZCBEaWNlICsgQ0UgdG8gaGFuZGxlIGNsYXNzIGltYmFsYW5jZSByb2J1c3RseS4ifV0="
---
# U-Net: Encoder-Decoder with Skip Connections

## Overview

U-Net (Ronneberger et al., 2015) was designed for biomedical image segmentation where labelled data is scarce. Its symmetric encoder-decoder with skip connections allows the network to combine deep semantic features with high-resolution spatial detail. Trained with aggressive augmentation, U-Net achieves strong results even with a few dozen training images — making it the dominant architecture in medical imaging.

The name comes from its U-shaped architecture: the encoder contracts the spatial dimensions while increasing channels; the decoder mirrors this path, expanding back to input resolution. Each level of the encoder connects directly to the corresponding decoder level via a skip connection that concatenates feature maps, preserving fine-grained spatial information throughout the upsampling path.

## Encoder Path

The encoder follows a standard CNN pattern: repeated blocks of two 3×3 convolutions (each followed by batch normalisation and ReLU), then 2×2 max pooling with stride 2. Each pooling step halves the spatial dimensions and doubles the channels, progressively building up an abstract semantic representation. The final encoder output — the bottleneck — captures the most compressed, semantically rich features.

```python
import torch.nn as nn

class EncoderBlock(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1), nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1), nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True)
        )
        self.pool = nn.MaxPool2d(2)

    def forward(self, x):
        features = self.conv(x)   # save for skip connection
        return self.pool(features), features
```

Pre-trained encoders (ResNet, EfficientNet) are often used as drop-in replacements for the hand-designed encoder. This transfer learning from ImageNet provides a strong initialisation, reducing training time and data requirements. Libraries like segmentation-models-pytorch make it easy to swap encoders while keeping the U-Net decoder structure and skip connection wiring.

## Decoder Path

The decoder mirrors the encoder: at each level, the feature map is upsampled by 2× (bilinear interpolation or transposed convolution), concatenated with the corresponding encoder skip features, then processed by two 3×3 conv-BN-ReLU blocks. This progressively refines the coarse bottleneck representation into a full-resolution segmentation map with fine boundary detail.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DecoderBlock(nn.Module):
    def __init__(self, in_ch, skip_ch, out_ch):
        super().__init__()
        self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch + skip_ch, out_ch, 3, padding=1), nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1), nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True)
        )

    def forward(self, x, skip):
        x = self.up(x)
        return self.conv(torch.cat([x, skip], dim=1))
```

Transposed convolutions (sometimes called deconvolutions) are an alternative to bilinear upsampling. They are learnable, but can introduce checkerboard artefacts if not carefully initialised. In practice, bilinear upsampling followed by a regular convolution tends to produce cleaner results and is preferred in most modern U-Net implementations.

## Skip Connections

Skip connections are the defining feature of U-Net. They directly route feature maps from the encoder to the corresponding decoder level, bypassing the bottleneck. This gives the decoder access to both coarse semantic context (from the deep bottleneck) and precise spatial detail (from the shallow encoder features). Without skip connections, fine structures like cell boundaries or vessel edges tend to blur out.

```python
import torch
import torch.nn as nn

class UNet(nn.Module):
    def __init__(self, in_ch=1, num_classes=2):
        super().__init__()
        self.enc1 = EncoderBlock(in_ch, 64)
        self.enc2 = EncoderBlock(64, 128)
        self.enc3 = EncoderBlock(128, 256)
        self.enc4 = EncoderBlock(256, 512)
        self.bottleneck = nn.Sequential(
            nn.Conv2d(512, 1024, 3, padding=1), nn.ReLU(inplace=True),
            nn.Conv2d(1024, 1024, 3, padding=1), nn.ReLU(inplace=True)
        )
        self.dec4 = DecoderBlock(1024, 512, 512)
        self.dec3 = DecoderBlock(512, 256, 256)
        self.dec2 = DecoderBlock(256, 128, 128)
        self.dec1 = DecoderBlock(128, 64, 64)
        self.head = nn.Conv2d(64, num_classes, 1)
```

U-Net++ nests dense skip connections between encoder and decoder nodes, creating an ensemble of U-Nets of varying depths. This helps when the optimal depth is unknown, as intermediate predictions can be used for deep supervision. The downside is increased parameter count and memory, but the improvement in mIoU on medical imaging benchmarks is consistent across datasets.

## U-Net for Medical Imaging

Medical image segmentation presents unique challenges: 3D volumes (CT/MRI), high class imbalance (small lesions in large backgrounds), limited labelled data, and domain shift between scanners or institutions. U-Net addresses these through aggressive augmentation (elastic deformation, rotation, flipping) and loss functions that handle imbalance, such as Dice loss or a weighted combination of Dice and binary cross-entropy.

```python
import torch
import torch.nn.functional as F

def dice_loss(pred, target, smooth=1.0):
    # pred: (B, C, H, W) logits; target: (B, H, W) long
    pred = torch.softmax(pred, dim=1)
    target_oh = F.one_hot(target, pred.shape[1]).permute(0,3,1,2).float()
    inter = (pred * target_oh).sum(dim=(2, 3))
    union = pred.sum(dim=(2, 3)) + target_oh.sum(dim=(2, 3))
    dice = (2 * inter + smooth) / (union + smooth)
    return 1 - dice.mean()

def combined_loss(pred, target):
    return dice_loss(pred, target) + F.cross_entropy(pred, target)
```

| U-Net variant | Skip connection | Key change | Application |
| --- | --- | --- | --- |
| U-Net original | Concatenation | Symmetric encoder-decoder | Biomedical segmentation |
| U-Net++ | Dense nested | Sub-networks of varying depth | Multi-organ, pathology |
| Attention U-Net | Attention gates on skip | Suppress irrelevant features | Prostate, CT organs |
| Residual U-Net | Residual + skip | ResNet blocks in encoder | Retinal vessels, dermoscopy |
| nnU-Net | Concatenation | Auto-config for any dataset | Medical imaging competitions |

> ****: nnU-Net automatically configures U-Net hyperparameters (patch size, batch size, augmentation) for any medical imaging dataset — it's the go-to baseline before custom architectures.

## Key Takeaways

U-Net's elegance lies in its symmetric structure and skip connections, which combine the best of both worlds: semantic depth from the encoder bottleneck and spatial precision from early encoder features. These properties make it near-universally applicable in medical imaging, remote sensing, and any domain requiring precise boundary delineation with limited training data.

When starting a new segmentation project, try nnU-Net first — it handles preprocessing, augmentation, and hyperparameter selection automatically and serves as a strong baseline. For natural images, combine a pretrained EfficientNet or ResNet encoder with a U-Net decoder using segmentation-models-pytorch. Always use Dice loss or combined Dice + CE to handle class imbalance robustly.

