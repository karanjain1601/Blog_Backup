---
title: "Deformable Attention: Efficient Sparse Cross-Attention in Vision"
slug: "cross-attention-deformable"
description: "How deformable attention replaces O(N^2) full attention with O(N*K) sparse sampling, enabling transformer-based detection and segmentation at high resolution."
tags: ["vision-transformer", "deformable-attention", "detection", "segmentation", "detr"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBzZWxmLWF0dGVudGlvbiBpbiB2aXNpb24gdHJhbnNmb3JtZXJzIGF0dGVuZHMgdG8gYWxsIHNwYXRpYWwgcG9zaXRpb25zLCBnaXZpbmcgTygoSFcpXjIpIGNvbXBsZXhpdHkuIEZvciBhbiA4MDB4MTIwMCBkZXRlY3Rpb24gaW1hZ2UgcHJvY2Vzc2VkIGF0IHN0cmlkZSA4LCB0aGlzIHByb2R1Y2VzIDEyMCwwMDAgdG9rZW5zIOKAlCBtYWtpbmcgZnVsbCBhdHRlbnRpb24gY29tcHV0YXRpb25hbGx5IGluZmVhc2libGUuIERlZm9ybWFibGUgYXR0ZW50aW9uIHJlcGxhY2VzIHRoZSBmdWxsIGF0dGVudGlvbiBtYXAgd2l0aCBhIHNwYXJzZSBzZXQgb2YgSyBsZWFybmVkIHNhbXBsaW5nIHBvaW50cyBwZXIgcXVlcnksIHJlZHVjaW5nIGNvbXBsZXhpdHkgdG8gTyhIVyAqIEspIHdoZXJlIEsgaXMgdHlwaWNhbGx5IDTigJM4LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBpZGVhOiBpbnN0ZWFkIG9mIGNvbXB1dGluZyBzaW1pbGFyaXR5IHNjb3JlcyB0byBhbGwgb3RoZXIgdG9rZW5zLCBlYWNoIHF1ZXJ5IHByZWRpY3RzIHdoZXJlIHRvIGxvb2sg4oCUIGEgc2V0IG9mIHJlZmVyZW5jZSBwb2ludCBvZmZzZXRzIHNhbXBsZWQgZnJvbSB0aGUgZmVhdHVyZSBtYXAgdmlhIGJpbGluZWFyIGludGVycG9sYXRpb24uIFRoZSBhdHRlbmRlZCB2YWx1ZSBpcyBhIHdlaWdodGVkIHN1bSBvZiBmZWF0dXJlcyBhdCB0aG9zZSBLIHBvc2l0aW9ucy4gVGhpcyBpcyBhcmNoaXRlY3R1cmFsbHkgc2ltaWxhciB0byBkZWZvcm1hYmxlIGNvbnZvbHV0aW9uIGJ1dCBvcGVyYXRlcyB3aXRoaW4gdGhlIHRyYW5zZm9ybWVyIGF0dGVudGlvbiBmcmFtZXdvcmsuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJXYXJuaW5nIiwiY29udGVudCI6IkRlZm9ybWFibGUgYXR0ZW50aW9uIG9mZnNldHMgYXJlIGxlYXJuZWQgdmlhIGEgbGluZWFyIGxheWVyIHdpdGggc2lnbW9pZCBhY3RpdmF0aW9uIOKAlCBpZiByZWZlcmVuY2UgcG9pbnRzIGNvbGxhcHNlIHRvIGEgc21hbGwgcmVnaW9uIGR1cmluZyBlYXJseSB0cmFpbmluZywgZ3JhZGllbnRzIHZhbmlzaC4gVXNlIHNtYWxsIGluaXQgc3RkICgwLjAxKSBmb3IgdGhlIG9mZnNldCBwcmVkaWN0aW9uIGhlYWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUXVhZHJhdGljIEF0dGVudGlvbiBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGdWxsIHNlbGYtYXR0ZW50aW9uIHJlcXVpcmVzIGNvbXB1dGluZyBhbiBOw5dOIHNpbWlsYXJpdHkgbWF0cml4IHdoZXJlIE4gaXMgdGhlIG51bWJlciBvZiBzcGF0aWFsIHRva2Vucy4gRm9yIFZpVC1CIGF0IDIyNHB4IHRoaXMgaXMgMTk2w5cxOTYgPSAzOCw0MTYgb3BlcmF0aW9ucyBwZXIgaGVhZCBwZXIgbGF5ZXIg4oCUIHRyYWN0YWJsZS4gQnV0IG9iamVjdCBkZXRlY3Rpb24gYW5kIHNlZ21lbnRhdGlvbiB0eXBpY2FsbHkgb3BlcmF0ZSBhdCBtdWNoIGhpZ2hlciByZXNvbHV0aW9uIG9yIG11bHRpLXNjYWxlIGZlYXR1cmUgcHlyYW1pZHMgd2hlcmUgdGhlIHRvdGFsIHRva2VuIGNvdW50IG1ha2VzIHRoZSBuYWl2ZSBmb3JtdWxhdGlvbiBpbXByYWN0aWNhbCBmb3IgYW55IHJlYWwtdGltZSBvciBiYXRjaCB3b3JrbG9hZC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldpbmRvdyBhdHRlbnRpb24gKFN3aW4gVHJhbnNmb3JtZXIpIHJlZHVjZXMgY29tcGxleGl0eSB0byBPKEhXICogV14yKSB3aGVyZSBXIGlzIHdpbmRvdyBzaXplLCBidXQgbG9jYWwgd2luZG93cyBsYWNrIGdsb2JhbCByZWNlcHRpdmUgZmllbGRzIGFuZCByZXF1aXJlIGFkZGl0aW9uYWwgY3Jvc3Mtd2luZG93IGNvbW11bmljYXRpb24gbWVjaGFuaXNtcy4gRGVmb3JtYWJsZSBhdHRlbnRpb24gcHJvdmlkZXMgZ2xvYmFsIHJlY2VwdGl2ZSBmaWVsZCB3aXRoIHNwYXJzZSBjb3N0LCB3aXRob3V0IG5lZWRpbmcgdGhlIHNoaWZ0ZWQtd2luZG93IG1hY2hpbmVyeSBvciBtdWx0aXBsZSBwYXNzZXMgdGhyb3VnaCB0aGUgZmVhdHVyZSBweXJhbWlkLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BhcnNlIGF0dGVudGlvbiBtZXRob2RzIHByZWRhdGUgZGVmb3JtYWJsZSBhdHRlbnRpb24g4oCUIExvbmdmb3JtZXIgdXNlcyBmaXhlZCBzdHJpZGUgcGF0dGVybnMsIEJpZ0JpcmQgdXNlcyByYW5kb20gKyBzbGlkaW5nIHdpbmRvdyArIGdsb2JhbCB0b2tlbnMuIERlZm9ybWFibGUgYXR0ZW50aW9uIGRpZmZlcnMgaW4gdGhhdCB0aGUgc3BhcnNpdHkgcGF0dGVybiBpcyBpbnB1dC1kZXBlbmRlbnQgYW5kIGxlYXJuZWQ6IGRpZmZlcmVudCBpbWFnZXMgeWllbGQgZGlmZmVyZW50IHF1ZXJ5IHNhbXBsaW5nIGxvY2F0aW9ucy4gVGhpcyBjb250ZW50LWFkYXB0aXZlIHNwYXJzaXR5IGlzIGVzcGVjaWFsbHkgZWZmZWN0aXZlIGZvciBkZXRlY3Rpb24gd2hlcmUgYXR0ZW50aW9uIG5lZWRzIHRvIGZvY3VzIG9uIG9iamVjdCBib3VuZGFyaWVzIGFuZCBrZXlwb2ludHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVmb3JtYWJsZSBTYW1wbGluZyBQb2ludHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVhY2ggcXVlcnkgcSBhdCBwb3NpdGlvbiBwIGdlbmVyYXRlcyBLIG9mZnNldCB2ZWN0b3JzIHZpYSBhIGxpbmVhciBwcm9qZWN0aW9uLiBUaGVzZSBvZmZzZXRzIGFyZSBhZGRlZCB0byB0aGUgcmVmZXJlbmNlIHBvaW50IChub3JtYWxpemVkIHRvIFswLDFdKSBhbmQgdXNlZCB0byBzYW1wbGUgZmVhdHVyZSB2YWx1ZXMgdmlhIGJpbGluZWFyIGludGVycG9sYXRpb24uIFRoZSBhdHRlbmRlZCBvdXRwdXQgaXMgdGhlIHdlaWdodGVkIHN1bSBvZiBzYW1wbGVkIGZlYXR1cmVzLCB3aGVyZSB3ZWlnaHRzIGFyZSBwcm9kdWNlZCBieSBhIHNlY29uZCBsaW5lYXIgaGVhZCBhbmQgbm9ybWFsaXplZCB2aWEgc29mdG1heCBhY3Jvc3MgdGhlIEsgcG9pbnRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIERlZm9ybWFibGUgYXR0ZW50aW9uOiBwcmVkaWN0IEsgcmVmZXJlbmNlIG9mZnNldHMsIHNhbXBsZSB3aXRoIGdyaWRfc2FtcGxlXG5pbXBvcnQgdG9yY2gsIHRvcmNoLm5uIGFzIG5uLCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgRGVmb3JtYWJsZUF0dGVudGlvbihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW0sIEs9NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLksgPSBLXG4gICAgICAgIHNlbGYub2Zmc2V0X3Byb2ogPSBubi5MaW5lYXIoZGltLCAyICogSykgICMgKGR4LCBkeSkgcGVyIHBvaW50XG4gICAgICAgIHNlbGYuYXR0bl9wcm9qICA9IG5uLkxpbmVhcihkaW0sIEspXG4gICAgICAgIHNlbGYudmFsdWVfcHJvaiA9IG5uLkxpbmVhcihkaW0sIGRpbSlcbiAgICAgICAgbm4uaW5pdC5ub3JtYWxfKHNlbGYub2Zmc2V0X3Byb2oud2VpZ2h0LCBzdGQ9MC4wMSlcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5vZmZzZXRfcHJvai5iaWFzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgcXVlcnksIHZhbHVlX21hcCwgcmVmX3BvaW50cyk6XG4gICAgICAgICMgcXVlcnk6IChCLE5xLEQpOyB2YWx1ZV9tYXA6IChCLEQsSCxXKTsgcmVmX3BvaW50czogKEIsTnEsMikgaW4gWzAsMV1cbiAgICAgICAgb2Zmc2V0cyA9IHNlbGYub2Zmc2V0X3Byb2oocXVlcnkpLnZpZXcoLTEsIHF1ZXJ5LnNoYXBlWzFdLCBzZWxmLkssIDIpLnRhbmgoKSAqIDAuNVxuICAgICAgICBwdHMgPSAocmVmX3BvaW50cy51bnNxdWVlemUoMikgKyBvZmZzZXRzKS5jbGFtcCgwLCAxKSAqIDIgLSAxICAjIHRvIFstMSwxXVxuICAgICAgICB2ID0gc2VsZi52YWx1ZV9wcm9qKHZhbHVlX21hcC5mbGF0dGVuKDIpLnRyYW5zcG9zZSgxLCAyKSlcbiAgICAgICAgdl9tYXAgPSB2LnZpZXcodmFsdWVfbWFwLnNoYXBlWzBdLCAqdmFsdWVfbWFwLnNoYXBlWzI6XSwgLTEpLnBlcm11dGUoMCwzLDEsMilcbiAgICAgICAgc2FtcGxlZCA9IEYuZ3JpZF9zYW1wbGUodl9tYXAsIHB0cy52aWV3KHZfbWFwLnNoYXBlWzBdLC0xLDEsMiksIGFsaWduX2Nvcm5lcnM9VHJ1ZSlcbiAgICAgICAgc2FtcGxlZCA9IHNhbXBsZWQuc3F1ZWV6ZSgtMSkudmlldyh2X21hcC5zaGFwZVswXSwgLTEsIHF1ZXJ5LnNoYXBlWzFdLCBzZWxmLkspLnBlcm11dGUoMCwyLDMsMSlcbiAgICAgICAgd2VpZ2h0cyA9IHNlbGYuYXR0bl9wcm9qKHF1ZXJ5KS5zb2Z0bWF4KC0xKS51bnNxdWVlemUoLTEpXG4gICAgICAgIHJldHVybiAoc2FtcGxlZCAqIHdlaWdodHMpLnN1bShkaW09MikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvZmZzZXQgaGVhZCBpbml0aWFsaXphdGlvbiBpcyBjcml0aWNhbC4gU21hbGwgc3RkICgwLjAxKSBlbnN1cmVzIG9mZnNldHMgc3RhcnQgbmVhciB6ZXJvLCBzbyB0aGUgbW9kZWwgaW5pdGlhbGx5IGF0dGVuZHMgdG8gdGhlIHJlZmVyZW5jZSBwb2ludCBuZWlnaGJvcmhvb2QuIElmIG9mZnNldHMgYXJlIGluaXRpYWxpemVkIHdpdGggZGVmYXVsdCBzdGQgKDAuMDIrKSwgc2FtcGxpbmcgcG9pbnRzIHNjYXR0ZXIgYWNyb3NzIHRoZSBmZWF0dXJlIG1hcCwgcHJvZHVjaW5nIG5vaXN5IGdyYWRpZW50cyB0aGF0IHN0YWxsIGVhcmx5IHRyYWluaW5nLiBUaGUgdGFuaCBhY3RpdmF0aW9uIGJvdW5kcyBvZmZzZXRzIHRvIMKxMC41IG9mIHRoZSBmZWF0dXJlIG1hcCBleHRlbnQgdG8gcHJldmVudCBydW5hd2F5IHNhbXBsaW5nIGxvY2F0aW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1TY2FsZSBEZWZvcm1hYmxlIEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGktc2NhbGUgZGVmb3JtYWJsZSBhdHRlbnRpb24gZXh0ZW5kcyB0aGUgc2luZ2xlLXNjYWxlIHZlcnNpb24gYnkgYXR0ZW5kaW5nIGFjcm9zcyBmZWF0dXJlIHB5cmFtaWQgbGV2ZWxzIHNpbXVsdGFuZW91c2x5LiBHaXZlbiBMIGZlYXR1cmUgbWFwcyBbUDMsIFA0LCBQNSwgUDZdIHdpdGggc3RyaWRlcyBbOCwgMTYsIDMyLCA2NF0sIGVhY2ggcXVlcnkgZ2VuZXJhdGVzIEsgc2FtcGxpbmcgcG9pbnRzIHBlciBsZXZlbCDigJQgdG90YWwgS8OXTCA9IDMyIHNhbXBsZXMgZm9yIEs9NCwgTD00LiBBIGxldmVsIGVtYmVkZGluZyBkaXN0aW5ndWlzaGVzIHdoaWNoIHB5cmFtaWQgbGV2ZWwgZWFjaCBzYW1wbGUgcG9pbnQgYmVsb25ncyB0by4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBNdWx0aS1zY2FsZSBkZWZvcm1hYmxlIGF0dGVudGlvbjogc2FtcGxlIGFjcm9zcyBbUDMsUDQsUDUsUDZdIGZlYXR1cmUgbWFwc1xuaW1wb3J0IHRvcmNoLCB0b3JjaC5ubiBhcyBubiwgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIE1TRGVmb3JtQXR0bihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW0sIG5fbGV2ZWxzPTQsIEs9NCwgbl9oZWFkcz04KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuSyA9IEs7IHNlbGYuTCA9IG5fbGV2ZWxzOyBzZWxmLkggPSBuX2hlYWRzXG4gICAgICAgIHNlbGYub2Zmc2V0X3Byb2ogPSBubi5MaW5lYXIoZGltLCBuX2hlYWRzICogbl9sZXZlbHMgKiBLICogMilcbiAgICAgICAgc2VsZi5hdHRuX3Byb2ogICA9IG5uLkxpbmVhcihkaW0sIG5faGVhZHMgKiBuX2xldmVscyAqIEspXG4gICAgICAgIHNlbGYudmFsdWVfcHJvaiAgPSBubi5MaW5lYXIoZGltLCBkaW0pXG4gICAgICAgIHNlbGYub3V0X3Byb2ogICAgPSBubi5MaW5lYXIoZGltLCBkaW0pXG4gICAgICAgIHNlbGYubGV2ZWxfZW1iZWQgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mobl9sZXZlbHMsIGRpbSkpXG4gICAgICAgIG5uLmluaXQubm9ybWFsXyhzZWxmLm9mZnNldF9wcm9qLndlaWdodCwgc3RkPTAuMDEpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBxdWVyeSwgdmFsdWVfbGlzdCwgcmVmX3BvaW50cyk6XG4gICAgICAgIEIsIE5xLCBEID0gcXVlcnkuc2hhcGVcbiAgICAgICAgb2Zmc2V0cyA9IHNlbGYub2Zmc2V0X3Byb2oocXVlcnkpLnZpZXcoQiwgTnEsIHNlbGYuSCwgc2VsZi5MLCBzZWxmLkssIDIpXG4gICAgICAgIGF0dG5fdyAgPSBzZWxmLmF0dG5fcHJvaihxdWVyeSkudmlldyhCLCBOcSwgc2VsZi5ILCBzZWxmLkwgKiBzZWxmLkspLnNvZnRtYXgoLTEpXG4gICAgICAgIGF0dG5fdyAgPSBhdHRuX3cudmlldyhCLCBOcSwgc2VsZi5ILCBzZWxmLkwsIHNlbGYuSylcbiAgICAgICAgIyBzYW1wbGUgZnJvbSBlYWNoIGxldmVsIGFuZCBhY2N1bXVsYXRlIChkZXRhaWxzIGluIF9zYW1wbGVfbGV2ZWwpXG4gICAgICAgIHJldHVybiBzZWxmLm91dF9wcm9qKHNlbGYuX2FnZ3JlZ2F0ZSh2YWx1ZV9saXN0LCByZWZfcG9pbnRzLCBvZmZzZXRzLCBhdHRuX3cpKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGktc2NhbGUgc2FtcGxpbmcgZ2l2ZXMgZWFjaCBxdWVyeSBhY2Nlc3MgdG8gYm90aCBmaW5lLWdyYWluZWQgKFAzLCBzdHJpZGUtOCkgZmVhdHVyZXMgZm9yIHByZWNpc2UgbG9jYWxpemF0aW9uIGFuZCBjb2Fyc2UgKFA2LCBzdHJpZGUtNjQpIGZlYXR1cmVzIGZvciBzZW1hbnRpYyBjb250ZXh0IOKAlCBhbGwgd2l0aGluIGEgc2luZ2xlIGF0dGVudGlvbiBvcGVyYXRpb24uIFRoaXMgcmVwbGFjZXMgZXhwbGljaXQgRlBOIHRvcC1kb3duIGZ1c2lvbiB3aXRoIGltcGxpY2l0IHNjYWxlLWF3YXJlIGF0dGVudGlvbiwgcmVkdWNpbmcgdGhlIG51bWJlciBvZiBhcmNoaXRlY3R1cmFsIGNvbXBvbmVudHMgbmVlZGVkLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGxldmVsIGVtYmVkZGluZyBhbGxvd3MgdGhlIG9mZnNldCBwcmVkaWN0aW9uIGhlYWQgdG8gc3BlY2lhbGl6ZSBwZXIgc2NhbGUuIEluIHByYWN0aWNlLCBtb2RlbHMgbGVhcm4gdG8gdXNlIGhpZ2gtcmVzb2x1dGlvbiBsZXZlbHMgZm9yIGVkZ2UtYWxpZ25lZCBzYW1wbGluZyBhbmQgbG93LXJlc29sdXRpb24gbGV2ZWxzIGZvciBvYmplY3QtY2F0ZWdvcnkgY29udGV4dC4gVGhpcyBlbWVyZ2VudCBzcGVjaWFsaXphdGlvbiBpcyB2aXNpYmxlIHdoZW4gdmlzdWFsaXppbmcgdGhlIGRpc3RyaWJ1dGlvbiBvZiBzYW1wbGluZyBwb2ludHMgcGVyIGxldmVsIGFjcm9zcyBkaWZmZXJlbnQgcXVlcnkgdHlwZXMgaW4gdHJhaW5lZCBEZWZvcm1hYmxlIERFVFIgbW9kZWxzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFwcGxpY2F0aW9ucyBpbiBEZXRlY3Rpb24gYW5kIFNlZ21lbnRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVmb3JtYWJsZSBERVRSIHJlcGxhY2VzIHN0YW5kYXJkIERFVFJcdTAwMjdzIGF0dGVudGlvbiB3aXRoIG11bHRpLXNjYWxlIGRlZm9ybWFibGUgYXR0ZW50aW9uIGluIGJvdGggZW5jb2RlciBhbmQgZGVjb2Rlci4gVGhlIGVuY29kZXIgYXBwbGllcyBkZWZvcm1hYmxlIHNlbGYtYXR0ZW50aW9uIHRvIGZsYXR0ZW5lZCBtdWx0aS1zY2FsZSBmZWF0dXJlcywgcmVwbGFjaW5nIE8oTl4yKSBhdHRlbnRpb24uIFRoZSBkZWNvZGVyIGFwcGxpZXMgZGVmb3JtYWJsZSBjcm9zcy1hdHRlbnRpb24gZnJvbSBvYmplY3QgcXVlcmllcyB0byBlbmNvZGVyIG91dHB1dCwgdXNpbmcgZWFjaCBxdWVyeVx1MDAyN3MgcHJlZGljdGVkIHJlZmVyZW5jZSBwb2ludCBhcyB0aGUgYW5jaG9yIGZvciBzYW1wbGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBEZWZvcm1hYmxlIERFVFI6IGVuY29kZXIgdXNlcyBkZWZvcm1hYmxlIHNlbGYtYXR0bjsgZGVjb2RlciB1c2VzIGNyb3NzLWF0dG5cbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBEZWZvcm1hYmxlREVUUihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBiYWNrYm9uZSwgZF9tb2RlbD0yNTYsIGVuY19sYXllcnM9NiwgZGVjX2xheWVycz02KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmFja2JvbmUgICA9IGJhY2tib25lXG4gICAgICAgIHNlbGYuaW5wdXRfcHJvaiA9IG5uLk1vZHVsZUxpc3QoXG4gICAgICAgICAgICBbbm4uQ29udjJkKGMsIGRfbW9kZWwsIDEpIGZvciBjIGluIFs1MTIsIDEwMjQsIDIwNDhdXSlcbiAgICAgICAgc2VsZi5lbmNvZGVyICAgID0gbm4uTW9kdWxlTGlzdChcbiAgICAgICAgICAgIFtEZWZvcm1hYmxlRW5jb2RlckxheWVyKGRfbW9kZWwsIG5fbGV2ZWxzPTQsIEs9NCkgZm9yIF8gaW4gcmFuZ2UoZW5jX2xheWVycyldKVxuICAgICAgICBzZWxmLmRlY29kZXIgICAgPSBubi5Nb2R1bGVMaXN0KFxuICAgICAgICAgICAgW0RlZm9ybWFibGVEZWNvZGVyTGF5ZXIoZF9tb2RlbCwgbl9sZXZlbHM9NCwgSz00KSBmb3IgXyBpbiByYW5nZShkZWNfbGF5ZXJzKV0pXG4gICAgICAgIHNlbGYucXVlcnlfZW1iZWQgPSBubi5FbWJlZGRpbmcoMzAwLCBkX21vZGVsICogMikgICMgY29udGVudCArIHBvc1xuICAgICAgICBzZWxmLmNsYXNzX2hlYWQgID0gbm4uTGluZWFyKGRfbW9kZWwsIDkxKVxuICAgICAgICBzZWxmLmJib3hfaGVhZCAgID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsKSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoZF9tb2RlbCwgNCkpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6IiMgUHJvZmlsZSBzdGFuZGFyZCB2cyBkZWZvcm1hYmxlIGF0dGVudGlvbjogRkxPUHMgYW5kIGxhdGVuY3kgb24gODAweDEyMDAgaW1hZ2VcbkgsIFcsIEQsIEsgPSAxMDAsIDE1MCwgMjU2LCA0ICAjIHN0cmlkZS04IGZlYXR1cmUgbWFwIG9mIDgwMHgxMjAwXG5OID0gSCAqIFcgICMgMTUsMDAwIHRva2Vuc1xuXG5zdGRfZmxvcHMgICA9IDIgKiBOICogTiAqIEQgICAgIyBRS15UICsgQVY6IE8oTl4yICogRClcbmRlZm9ybV9mbG9wcyA9IDIgKiBOICogSyAqIEQgICMgTyhOICogSyAqIEQpXG5cbnByaW50KGZcdTAwMjdTdGFuZGFyZCBhdHRlbnRpb24gOiB7c3RkX2Zsb3BzIC8gMWU5Oi4xZn0gR0ZMT1BzXHUwMDI3KVxucHJpbnQoZlx1MDAyN0RlZm9ybWFibGUgKEs9e0t9KSAgOiB7ZGVmb3JtX2Zsb3BzIC8gMWU2Oi4xZn0gTUZMT1BzXHUwMDI3KVxucHJpbnQoZlx1MDAyN0ZMT1AgcmVkdWN0aW9uICAgICAgOiB7c3RkX2Zsb3BzIC8gZGVmb3JtX2Zsb3BzOi4wZn14XHUwMDI3KVxuXG4jIENvbmNlcHR1YWwgbGF0ZW5jeSBvbiBBMTAwIChzaW5nbGUtYmF0Y2gsIGVuY29kZXIgb25seSlcbmZvciBsYWJlbCwgbXMgaW4gWyhcdTAwMjdTdGFuZGFyZCA4MDB4MTIwMFx1MDAyNywgMjg0MCksIChcdTAwMjdEZWZvcm1hYmxlIEs9NFx1MDAyNywgNDcpLCAoXHUwMDI3RGVmb3JtYWJsZSBLPThcdTAwMjcsIDg5KV06XG4gICAgcHJpbnQoZlx1MDAyN3tsYWJlbH06IH57bXN9IG1zXHUwMDI3KSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJBdHRlbnRpb24gVHlwZSIsIkNvbXBsZXhpdHkiLCJLZXlzIHBlciBRdWVyeSIsIk1lbW9yeSAoR0IpIiwiQ09DTyBBUCJdLCJyb3dzIjpbWyJTdGFuZGFyZCIsIk8oKEhXKV4yKSIsIkhXID0gMTUwMDAiLCIxMi40IiwiNDIuMCJdLFsiRGVmb3JtYWJsZSBLPTQiLCJPKEhXICogSykiLCI0IiwiMS4xIiwiNDQuNSJdLFsiRGVmb3JtYWJsZSBLPTgiLCJPKEhXICogSykiLCI4IiwiMS40IiwiNDUuMSJdLFsiV2luZG93IChTd2luKSIsIk8oSFcgKiBXXjIpIiwiNDkgKDd4NyB3aW5kb3cpIiwiMi4zIiwiNDguMyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVmb3JtYWJsZSBhdHRlbnRpb24gc29sdmVzIHRoZSBxdWFkcmF0aWMgYm90dGxlbmVjayBieSBtYWtpbmcgYXR0ZW50aW9uIHNwYXJzZSBhbmQgY29udGVudC1hZGFwdGl2ZS4gVGhlIGNvcmUgdHJhZGVvZmYgaXMgdGhhdCBlYWNoIHF1ZXJ5IG9ubHkgYXR0ZW5kcyB0byBLIGxvY2F0aW9ucyBpbnN0ZWFkIG9mIGFsbCBOLCBzbyB0aGUgbW9kZWwgbXVzdCBsZWFybiB0byBwcmVkaWN0IGdvb2Qgc2FtcGxpbmcgbG9jYXRpb25zLiBUaGlzIHJlcXVpcmVzIGNhcmVmdWwgaW5pdGlhbGl6YXRpb24gYW5kIHNvbWV0aW1lcyBzbG93ZXIgZWFybHkgdHJhaW5pbmcgY29udmVyZ2VuY2UsIGJ1dCB0aGUgYXN5bXB0b3RpYyBzcGVlZCBnYWlucyBtYWtlIGl0IHRoZSBkZWZhdWx0IGNob2ljZSBmb3IgaGlnaC1yZXNvbHV0aW9uIHZpc2lvbiB0YXNrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtdWx0aS1zY2FsZSB2YXJpYW50IGlzIHBhcnRpY3VsYXJseSBwb3dlcmZ1bCBmb3IgZGV0ZWN0aW9uIGJlY2F1c2UgaXQgYWxsb3dzIGEgc2luZ2xlIGF0dGVudGlvbiBvcGVyYXRpb24gdG8gc2ltdWx0YW5lb3VzbHkgZ2F0aGVyIGV2aWRlbmNlIGZyb20gbXVsdGlwbGUgc2NhbGVzIG9mIHRoZSBmZWF0dXJlIHB5cmFtaWQuIFRoaXMgcmVwbGFjZXMgZXhwbGljaXQgRlBOIHRvcC1kb3duIGZ1c2lvbiB3aXRoIGltcGxpY2l0IHNjYWxlLWF3YXJlIGF0dGVudGlvbiwgcmVkdWNpbmcgdGhlIG51bWJlciBvZiBhcmNoaXRlY3R1cmFsIGNvbXBvbmVudHMgbmVlZGVkIHdoaWxlIGFjaGlldmluZyBjb21wZXRpdGl2ZSBhY2N1cmFjeSB3aXRoIG11Y2ggbG93ZXIgY29tcHV0YXRpb25hbCBjb3N0IGFjcm9zcyBiZW5jaG1hcmsgZGF0YXNldHMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgaW1wbGVtZW50YXRpb24sIHRoZSBtb3N0IGNyaXRpY2FsIHByYWN0aWNhbCBjb25zaWRlcmF0aW9uIGlzIHRoZSBvZmZzZXQgaGVhZCBpbml0aWFsaXphdGlvbjogdXNlIHN0ZD0wLjAxIGFuZCB6ZXJvIGJpYXMgc28gZWFybHkgdHJhaW5pbmcgc3RhcnRzIHdpdGggbmVhci16ZXJvIG9mZnNldHMuIEFkZGl0aW9uYWxseSwgY2xhbXAgc2FtcGxpbmcgcG9pbnRzIHRvIFswLDFdIGJlZm9yZSBiaWxpbmVhciBpbnRlcnBvbGF0aW9uIHRvIHByZXZlbnQgb3V0LW9mLWJvdW5kcyBzYW1wbGluZyB0aGF0IHByb2R1Y2VzIHplcm8gZ3JhZGllbnRzLiBUaGVzZSB0d28gaW1wbGVtZW50YXRpb24gZGV0YWlscyBzZXBhcmF0ZSBzdGFibGUgZnJvbSB1bnN0YWJsZSB0cmFpbmluZyBydW5zIGluIG5lYXJseSBldmVyeSByZXBvcnRlZCBEZWZvcm1hYmxlIERFVFIgcmVwcm9kdWN0aW9uLiJ9XQ=="
---
# Deformable Attention: Efficient Sparse Cross-Attention in Vision

## Overview

Standard self-attention in vision transformers attends to all spatial positions, giving O((HW)^2) complexity. For an 800x1200 detection image processed at stride 8, this produces 120,000 tokens — making full attention computationally infeasible. Deformable attention replaces the full attention map with a sparse set of K learned sampling points per query, reducing complexity to O(HW * K) where K is typically 4–8.

The key idea: instead of computing similarity scores to all other tokens, each query predicts where to look — a set of reference point offsets sampled from the feature map via bilinear interpolation. The attended value is a weighted sum of features at those K positions. This is architecturally similar to deformable convolution but operates within the transformer attention framework.

> **Warning**: Deformable attention offsets are learned via a linear layer with sigmoid activation — if reference points collapse to a small region during early training, gradients vanish. Use small init std (0.01) for the offset prediction head.

## Quadratic Attention Problem

Full self-attention requires computing an N×N similarity matrix where N is the number of spatial tokens. For ViT-B at 224px this is 196×196 = 38,416 operations per head per layer — tractable. But object detection and segmentation typically operate at much higher resolution or multi-scale feature pyramids where the total token count makes the naive formulation impractical for any real-time or batch workload.

Window attention (Swin Transformer) reduces complexity to O(HW * W^2) where W is window size, but local windows lack global receptive fields and require additional cross-window communication mechanisms. Deformable attention provides global receptive field with sparse cost, without needing the shifted-window machinery or multiple passes through the feature pyramid.

Sparse attention methods predate deformable attention — Longformer uses fixed stride patterns, BigBird uses random + sliding window + global tokens. Deformable attention differs in that the sparsity pattern is input-dependent and learned: different images yield different query sampling locations. This content-adaptive sparsity is especially effective for detection where attention needs to focus on object boundaries and keypoints.

## Deformable Sampling Points

Each query q at position p generates K offset vectors via a linear projection. These offsets are added to the reference point (normalized to [0,1]) and used to sample feature values via bilinear interpolation. The attended output is the weighted sum of sampled features, where weights are produced by a second linear head and normalized via softmax across the K points.

```python
# Deformable attention: predict K reference offsets, sample with grid_sample
import torch, torch.nn as nn, torch.nn.functional as F

class DeformableAttention(nn.Module):
    def __init__(self, dim, K=4):
        super().__init__()
        self.K = K
        self.offset_proj = nn.Linear(dim, 2 * K)  # (dx, dy) per point
        self.attn_proj  = nn.Linear(dim, K)
        self.value_proj = nn.Linear(dim, dim)
        nn.init.normal_(self.offset_proj.weight, std=0.01)
        nn.init.zeros_(self.offset_proj.bias)

    def forward(self, query, value_map, ref_points):
        # query: (B,Nq,D); value_map: (B,D,H,W); ref_points: (B,Nq,2) in [0,1]
        offsets = self.offset_proj(query).view(-1, query.shape[1], self.K, 2).tanh() * 0.5
        pts = (ref_points.unsqueeze(2) + offsets).clamp(0, 1) * 2 - 1  # to [-1,1]
        v = self.value_proj(value_map.flatten(2).transpose(1, 2))
        v_map = v.view(value_map.shape[0], *value_map.shape[2:], -1).permute(0,3,1,2)
        sampled = F.grid_sample(v_map, pts.view(v_map.shape[0],-1,1,2), align_corners=True)
        sampled = sampled.squeeze(-1).view(v_map.shape[0], -1, query.shape[1], self.K).permute(0,2,3,1)
        weights = self.attn_proj(query).softmax(-1).unsqueeze(-1)
        return (sampled * weights).sum(dim=2)
```

The offset head initialization is critical. Small std (0.01) ensures offsets start near zero, so the model initially attends to the reference point neighborhood. If offsets are initialized with default std (0.02+), sampling points scatter across the feature map, producing noisy gradients that stall early training. The tanh activation bounds offsets to ±0.5 of the feature map extent to prevent runaway sampling locations.

## Multi-Scale Deformable Attention

Multi-scale deformable attention extends the single-scale version by attending across feature pyramid levels simultaneously. Given L feature maps [P3, P4, P5, P6] with strides [8, 16, 32, 64], each query generates K sampling points per level — total K×L = 32 samples for K=4, L=4. A level embedding distinguishes which pyramid level each sample point belongs to.

```python
# Multi-scale deformable attention: sample across [P3,P4,P5,P6] feature maps
import torch, torch.nn as nn, torch.nn.functional as F

class MSDeformAttn(nn.Module):
    def __init__(self, dim, n_levels=4, K=4, n_heads=8):
        super().__init__()
        self.K = K; self.L = n_levels; self.H = n_heads
        self.offset_proj = nn.Linear(dim, n_heads * n_levels * K * 2)
        self.attn_proj   = nn.Linear(dim, n_heads * n_levels * K)
        self.value_proj  = nn.Linear(dim, dim)
        self.out_proj    = nn.Linear(dim, dim)
        self.level_embed = nn.Parameter(torch.zeros(n_levels, dim))
        nn.init.normal_(self.offset_proj.weight, std=0.01)

    def forward(self, query, value_list, ref_points):
        B, Nq, D = query.shape
        offsets = self.offset_proj(query).view(B, Nq, self.H, self.L, self.K, 2)
        attn_w  = self.attn_proj(query).view(B, Nq, self.H, self.L * self.K).softmax(-1)
        attn_w  = attn_w.view(B, Nq, self.H, self.L, self.K)
        # sample from each level and accumulate (details in _sample_level)
        return self.out_proj(self._aggregate(value_list, ref_points, offsets, attn_w))
```

Multi-scale sampling gives each query access to both fine-grained (P3, stride-8) features for precise localization and coarse (P6, stride-64) features for semantic context — all within a single attention operation. This replaces explicit FPN top-down fusion with implicit scale-aware attention, reducing the number of architectural components needed.

The level embedding allows the offset prediction head to specialize per scale. In practice, models learn to use high-resolution levels for edge-aligned sampling and low-resolution levels for object-category context. This emergent specialization is visible when visualizing the distribution of sampling points per level across different query types in trained Deformable DETR models.

## Applications in Detection and Segmentation

Deformable DETR replaces standard DETR's attention with multi-scale deformable attention in both encoder and decoder. The encoder applies deformable self-attention to flattened multi-scale features, replacing O(N^2) attention. The decoder applies deformable cross-attention from object queries to encoder output, using each query's predicted reference point as the anchor for sampling.

```python
# Deformable DETR: encoder uses deformable self-attn; decoder uses cross-attn
import torch.nn as nn

class DeformableDETR(nn.Module):
    def __init__(self, backbone, d_model=256, enc_layers=6, dec_layers=6):
        super().__init__()
        self.backbone   = backbone
        self.input_proj = nn.ModuleList(
            [nn.Conv2d(c, d_model, 1) for c in [512, 1024, 2048]])
        self.encoder    = nn.ModuleList(
            [DeformableEncoderLayer(d_model, n_levels=4, K=4) for _ in range(enc_layers)])
        self.decoder    = nn.ModuleList(
            [DeformableDecoderLayer(d_model, n_levels=4, K=4) for _ in range(dec_layers)])
        self.query_embed = nn.Embedding(300, d_model * 2)  # content + pos
        self.class_head  = nn.Linear(d_model, 91)
        self.bbox_head   = nn.Sequential(
            nn.Linear(d_model, d_model), nn.ReLU(), nn.Linear(d_model, 4))
```

```python
# Profile standard vs deformable attention: FLOPs and latency on 800x1200 image
H, W, D, K = 100, 150, 256, 4  # stride-8 feature map of 800x1200
N = H * W  # 15,000 tokens

std_flops   = 2 * N * N * D    # QK^T + AV: O(N^2 * D)
deform_flops = 2 * N * K * D  # O(N * K * D)

print(f'Standard attention : {std_flops / 1e9:.1f} GFLOPs')
print(f'Deformable (K={K})  : {deform_flops / 1e6:.1f} MFLOPs')
print(f'FLOP reduction      : {std_flops / deform_flops:.0f}x')

# Conceptual latency on A100 (single-batch, encoder only)
for label, ms in [('Standard 800x1200', 2840), ('Deformable K=4', 47), ('Deformable K=8', 89)]:
    print(f'{label}: ~{ms} ms')
```

| Attention Type | Complexity | Keys per Query | Memory (GB) | COCO AP |
| --- | --- | --- | --- | --- |
| Standard | O((HW)^2) | HW = 15000 | 12.4 | 42.0 |
| Deformable K=4 | O(HW * K) | 4 | 1.1 | 44.5 |
| Deformable K=8 | O(HW * K) | 8 | 1.4 | 45.1 |
| Window (Swin) | O(HW * W^2) | 49 (7x7 window) | 2.3 | 48.3 |

## Key Takeaways

Deformable attention solves the quadratic bottleneck by making attention sparse and content-adaptive. The core tradeoff is that each query only attends to K locations instead of all N, so the model must learn to predict good sampling locations. This requires careful initialization and sometimes slower early training convergence, but the asymptotic speed gains make it the default choice for high-resolution vision tasks.

The multi-scale variant is particularly powerful for detection because it allows a single attention operation to simultaneously gather evidence from multiple scales of the feature pyramid. This replaces explicit FPN top-down fusion with implicit scale-aware attention, reducing the number of architectural components needed while achieving competitive accuracy with much lower computational cost across benchmark datasets.

For implementation, the most critical practical consideration is the offset head initialization: use std=0.01 and zero bias so early training starts with near-zero offsets. Additionally, clamp sampling points to [0,1] before bilinear interpolation to prevent out-of-bounds sampling that produces zero gradients. These two implementation details separate stable from unstable training runs in nearly every reported Deformable DETR reproduction.

