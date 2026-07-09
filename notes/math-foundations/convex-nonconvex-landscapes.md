---
title: "Convex vs Non-Convex Loss Landscapes"
slug: "convex-nonconvex-landscapes"
description: "Rigorous treatment of convex function theory, loss landscape geometry for neural networks, saddle point prevalence in high dimensions, mode connectivity, and the neural tangent kernel regime."
tags: ["optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIGdlb21ldHJ5IG9mIGEgbG9zcyBmdW5jdGlvbiBkZXRlcm1pbmVzIHdoZXRoZXIgZ3JhZGllbnQgZGVzY2VudCBjYW4gZmluZCBnb29kIHNvbHV0aW9ucyBlZmZpY2llbnRseS4gQ29udmV4IGxhbmRzY2FwZXMgaGF2ZSBleGFjdGx5IG9uZSBiYXNpbiBjb250YWluaW5nIHRoZSBnbG9iYWwgbWluaW11bSwgc28gYW55IGRlc2NlbnQgYWxnb3JpdGhtIHdpdGggc3VmZmljaWVudCBzdGVwIHNpemUgZXZlbnR1YWxseSBjb252ZXJnZXMuIE5vbi1jb252ZXggbGFuZHNjYXBlcyDigJQgY2hhcmFjdGVyaXN0aWMgb2YgbmV1cmFsIG5ldHdvcmtzIOKAlCBjb250YWluIG11bHRpcGxlIGJhc2lucywgc2FkZGxlIHBvaW50cywgcmlkZ2VzLCBhbmQgcGxhdGVhdXMuIFVuZGVyc3RhbmRpbmcgdGhpcyBnZW9tZXRyeSBndWlkZXMgYXJjaGl0ZWN0dXJlIGRlc2lnbiwgb3B0aW1pemVyIGNob2ljZSwgYW5kIHRyYWluaW5nIHN0cmF0ZWdpZXMuIFRoaXMgbm90ZSBidWlsZHMgcmlnb3JvdXMgaW50dWl0aW9uIGZyb20gY29udmV4IGZ1bmN0aW9uIHRoZW9yeSB0aHJvdWdoIHRoZSBwcmFjdGljYWwgaW1wbGljYXRpb25zIGZvciBtb2Rlcm4gZGVlcCBsZWFybmluZywgY292ZXJpbmcgdGhlIHByZXZhbGVuY2Ugb2Ygc2FkZGxlIHBvaW50cyBwcmVkaWN0ZWQgYnkgcmFuZG9tIG1hdHJpeCB0aGVvcnksIGxvc3MgbGFuZHNjYXBlIHZpc3VhbGl6YXRpb24sIG1vZGUgY29ubmVjdGl2aXR5LCBhbmQgdGhlIE5ldXJhbCBUYW5nZW50IEtlcm5lbCByZWdpbWUuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29udmV4IEZ1bmN0aW9uczogRGVmaW5pdGlvbnMgYW5kIFByb3BlcnRpZXMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJBIGZ1bmN0aW9uIGY6IFJebiDihpIgUiBpcyBjb252ZXggaWYgZm9yIGFsbCB4LCB5IGluIGl0cyBkb21haW4gYW5kIGFsbCDOuyDiiIggWzAsMV06IGYozrt4ICsgKDEtzrspeSkg4omkIM67Zih4KSArICgxLc67KWYoeSkuIFRoZSBjaG9yZCBjb25uZWN0aW5nIGFueSB0d28gcG9pbnRzIG9uIHRoZSBncmFwaCBsaWVzIGFib3ZlIG9yIG9uIHRoZSBncmFwaC4gU3RyaWN0IGNvbnZleGl0eSByZXF1aXJlcyBzdHJpY3QgaW5lcXVhbGl0eSBmb3IgeCDiiaAgeSwgZ3VhcmFudGVlaW5nIGEgdW5pcXVlIGdsb2JhbCBtaW5pbXVtLiDOvC1zdHJvbmdseSBjb252ZXggKM68ID4gMCkgbWVhbnMgZih5KSDiiaUgZih4KSArIOKIh2YoeCnhtYAoeeKIkngpICsgKM68LzIp4oCWeeKIknjigJbCsiDigJQgdGhlIGZ1bmN0aW9uIGlzIGxvd2VyLWJvdW5kZWQgYnkgYSBxdWFkcmF0aWMuIEVxdWl2YWxlbnQgSGVzc2lhbiBjb25kaXRpb246IEgg4om9IDAgKFBTRCkgZm9yIGNvbnZleCwgSCDiibsgMCAoUEQpIGZvciBzdHJpY3RseSBjb252ZXgsIEgg4om9IM68SSBmb3Igzrwtc3Ryb25nbHkgY29udmV4LiBMb2dpc3RpYyByZWdyZXNzaW9uIHdpdGggbG9nLWxvc3MgSVMgY29udmV4OiB0aGUgbG9nLXN1bS1leHAgaXMgY29udmV4LCBjb21wb3NpdGlvbiB3aXRoIGEgbGluZWFyIGZ1bmN0aW9uIHByZXNlcnZlcyBjb252ZXhpdHkuIE5ldXJhbCBuZXR3b3JrcyBhcmUgTk9UIGNvbnZleDogdGhlIGNvbXBvc2l0aW9uIGYoV3gpIHdpdGggbm9uLWxpbmVhciBhY3RpdmF0aW9uIGYgYnJlYWtzIHRoZSBjb252ZXhpdHktcHJlc2VydmluZyBjb21wb3NpdGlvbiBydWxlICh3aGljaCByZXF1aXJlcyBmIHRvIGJlIGNvbnZleCBhbmQgbm9uLWRlY3JlYXNpbmcsIGJ1dCBSZUxVIGFwcGxpZWQgdG8gYSBsaW5lYXIgbGF5ZXIgbWFrZXMgdGhlIGNvbXBvc2l0ZSBub24tY29udmV4IHdoZW4gbGF5ZXJzIGFyZSBzdGFja2VkKS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBMb2dpc3RpY1JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuXG5kZWYgY2hlY2tfY29udmV4aXR5X251bWVyaWNhbGx5KGYsIG5fc2FtcGxlcz01MDAsIG5fZGltPTUsIHRvbD0xZS02KTpcbiAgICBcIlwiXCJTYW1wbGUgcGFpcnMgKHgsIHkpIGFuZCBjaGVjayBmKM67eCsoMS3Ouyl5KSA8PSDOu2YoeCkrKDEtzrspZih5KS5cIlwiXCJcbiAgICB2aW9sYXRpb25zID0gMFxuICAgIGZvciBfIGluIHJhbmdlKG5fc2FtcGxlcyk6XG4gICAgICAgIHggPSBucC5yYW5kb20ucmFuZG4obl9kaW0pXG4gICAgICAgIHkgPSBucC5yYW5kb20ucmFuZG4obl9kaW0pXG4gICAgICAgIGxhbSA9IG5wLnJhbmRvbS51bmlmb3JtKDAuMDEsIDAuOTkpXG4gICAgICAgIGxocyA9IGYobGFtICogeCArICgxIC0gbGFtKSAqIHkpXG4gICAgICAgIHJocyA9IGxhbSAqIGYoeCkgKyAoMSAtIGxhbSkgKiBmKHkpXG4gICAgICAgIGlmIGxocyA+IHJocyArIHRvbDpcbiAgICAgICAgICAgIHZpb2xhdGlvbnMgKz0gMVxuICAgIHJldHVybiB2aW9sYXRpb25zLCBuX3NhbXBsZXNcblxuIyBMb2dpc3RpYyBsb3NzIChjb252ZXgpXG5kZWYgbG9naXN0aWNfbG9zcyhwYXJhbXMsIFgsIHkpOlxuICAgIHcsIGIgPSBwYXJhbXNbOi0xXSwgcGFyYW1zWy0xXVxuICAgIGxvZ2l0cyA9IFggQCB3ICsgYlxuICAgIHJldHVybiBucC5tZWFuKG5wLmxvZygxICsgbnAuZXhwKC15ICogbG9naXRzKSkpXG5cblgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKG5fc2FtcGxlcz01MCwgbl9mZWF0dXJlcz00LCByYW5kb21fc3RhdGU9MClcbnkgPSAyICogeSAtIDEgICMgey0xLCArMX1cbmZfbG9naXN0aWMgPSBsYW1iZGEgcDogbG9naXN0aWNfbG9zcyhwLCBYLCB5KVxudmlvbCwgdG90YWwgPSBjaGVja19jb252ZXhpdHlfbnVtZXJpY2FsbHkoZl9sb2dpc3RpYywgbl9kaW09NSlcbnByaW50KGZcIkxvZ2lzdGljIGxvc3MgdmlvbGF0aW9uczoge3Zpb2x9L3t0b3RhbH0gKGV4cGVjdGVkIDApXCIpXG5cbiMgU2ltcGxlIDItbGF5ZXIgTk4gbG9zcyAobm9uLWNvbnZleClcbmRlZiBubl9sb3NzKHBhcmFtcyk6XG4gICAgVzEgPSBwYXJhbXNbOjhdLnJlc2hhcGUoMiwgNClcbiAgICBXMiA9IHBhcmFtc1s4OjEwXVxuICAgIGggPSBucC5tYXhpbXVtKDAsIFggQCBXMS5UKSAgIyBSZUxVXG4gICAgb3V0ID0gaCBAIFcyXG4gICAgcmV0dXJuIG5wLm1lYW4oKG91dCAtIHkpICoqIDIpXG5cbnZpb2wyLCB0b3RhbDIgPSBjaGVja19jb252ZXhpdHlfbnVtZXJpY2FsbHkobm5fbG9zcywgbl9kaW09MTApXG5wcmludChmXCJOTiBsb3NzIHZpb2xhdGlvbnM6IHt2aW9sMn0ve3RvdGFsMn0gKGV4cGVjdGVkID4gMClcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJTYWRkbGUgUG9pbnRzIGluIEhpZ2ggRGltZW5zaW9ucyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBpbmRleCBvZiBhIHNhZGRsZSBwb2ludCBpcyB0aGUgZnJhY3Rpb24gb2YgbmVnYXRpdmUgSGVzc2lhbiBlaWdlbnZhbHVlcyBhdCB0aGF0IGNyaXRpY2FsIHBvaW50LiBSYW5kb20gbWF0cml4IHRoZW9yeSAoV2lnbmVyIHNlbWljaXJjbGUgbGF3KSBwcmVkaWN0cyB0aGF0IGZvciBhIHJhbmRvbSBuw5duIHN5bW1ldHJpYyBtYXRyaXgsIGFwcHJveGltYXRlbHkgaGFsZiB0aGUgZWlnZW52YWx1ZXMgYXJlIG5lZ2F0aXZlLiBUaGlzIG1lYW5zIHRoYXQgYXQgYSByYW5kb20gY3JpdGljYWwgcG9pbnQgaW4gaGlnaC1kaW1lbnNpb25hbCBub24tY29udmV4IGxhbmRzY2FwZXMsIHJvdWdobHkgaGFsZiB0aGUgY3VydmF0dXJlIGRpcmVjdGlvbnMgcG9pbnQgZG93bndhcmQg4oCUIGkuZS4sIG1vc3QgY3JpdGljYWwgcG9pbnRzIGFyZSBzYWRkbGUgcG9pbnRzLCBub3QgbG9jYWwgbWluaW1hLiBEYXVwaGluIGV0IGFsLiAoMjAxNCkgc2hvd2VkIGVtcGlyaWNhbGx5IHRoYXQgaW4gZGVlcCBuZXR3b3JrcywgY3JpdGljYWwgcG9pbnRzIGVuY291bnRlcmVkIGR1cmluZyB0cmFpbmluZyBoYXZlIGxvc3MgY2xvc2UgdG8gdGhlIGdsb2JhbCBtaW5pbXVtLCBjb250cmFkaWN0aW5nIHRoZSBmZWFyIG9mICdiYWQgbG9jYWwgbWluaW1hLicgSW5zdGVhZCwgc2FkZGxlIHBvaW50cyBkb21pbmF0ZTogdGhlIGdyYWRpZW50IG5vcm0gaXMgbmVhciB6ZXJvIChHRCBzdGFsbHMpIGJ1dCBsb3NzIGlzIGFib3ZlIHRoZSBnbG9iYWwgbWluaW11bS4gVGhyZWUgZXNjYXBlIG1lY2hhbmlzbXM6ICgxKSBTR0QncyBncmFkaWVudCBub2lzZSBmcm9tIG1pbmktYmF0Y2hpbmcgcGVydHVyYnMgdGhlIHRyYWplY3Rvcnkgb2ZmIHRoZSBzYWRkbGU7ICgyKSBOZWdhdGl2ZSBjdXJ2YXR1cmUgZXhwbG9pdGF0aW9uIChDYXJtb24gZXQgYWwuKTogZm9sbG93IHRoZSBtb3N0IG5lZ2F0aXZlIGVpZ2VudmVjdG9yIGRpcmVjdGlvbjsgKDMpIFBlcnR1cmJhdGlvbi10aGVuLXJlc3RhcnQgKEdlIGV0IGFsLiAyMDE1KTogYWRkIHJhbmRvbSBub2lzZSB0byB3ZWlnaHRzIHdoZW4gZ3JhZGllbnQgbm9ybSA8IHRocmVzaG9sZC4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYlxubWF0cGxvdGxpYi51c2UoJ0FnZycpXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbiMgRnVuY3Rpb24gd2l0aCBhIGtub3duIHNhZGRsZSBhdCBvcmlnaW46IGYoeCx5KSA9IHheMiAtIHleMlxuZGVmIGYoeHkpOiByZXR1cm4geHlbMF0qKjIgLSB4eVsxXSoqMlxuZGVmIGdyYWRfZih4eSk6IHJldHVybiBucC5hcnJheShbMip4eVswXSwgLTIqeHlbMV1dKVxuXG5kZWYgZ3JhZGllbnRfZGVzY2VudChzdGFydCwgbHI9MC4wNSwgc3RlcHM9MjAwLCBub2lzZT0wLjApOlxuICAgIHBhdGggPSBbc3RhcnQuY29weSgpXVxuICAgIHh5ID0gc3RhcnQuY29weSgpXG4gICAgZm9yIF8gaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICBnID0gZ3JhZF9mKHh5KVxuICAgICAgICB4eSA9IHh5IC0gbHIgKiBnICsgbm9pc2UgKiBucC5yYW5kb20ucmFuZG4oMilcbiAgICAgICAgcGF0aC5hcHBlbmQoeHkuY29weSgpKVxuICAgIHJldHVybiBucC5hcnJheShwYXRoKVxuXG4jIEdEIGZyb20gbmVhciBzYWRkbGU6IHN0YXJ0IGF0IFswLjAxLCAwLjFdIChzbGlnaHQgb2Zmc2V0KVxubnAucmFuZG9tLnNlZWQoNDIpXG5zdGFydF9uZWFyX3NhZGRsZSA9IG5wLmFycmF5KFswLjAxLCAwLjFdKVxuXG5wYXRoX2dkID0gZ3JhZGllbnRfZGVzY2VudChzdGFydF9uZWFyX3NhZGRsZSwgbHI9MC4wNSwgbm9pc2U9MC4wKVxucGF0aF9zZ2QgPSBncmFkaWVudF9kZXNjZW50KHN0YXJ0X25lYXJfc2FkZGxlLCBscj0wLjA1LCBub2lzZT0wLjAyKVxuXG5wcmludChcIkdEIG5lYXIgc2FkZGxlIOKAlCBmaW5hbCBwb3NpdGlvbjpcIiwgcGF0aF9nZFstMV0ucm91bmQoNCkpXG5wcmludChcIkdEIGdyYWRpZW50IG5vcm0gaGlzdG9yeSAoZmlyc3QgMTApOlwiLFxuICAgICAgW3JvdW5kKG5wLmxpbmFsZy5ub3JtKGdyYWRfZihwKSksIDQpIGZvciBwIGluIHBhdGhfZ2RbOjEwXV0pXG5wcmludChcIlNHRCAod2l0aCBub2lzZSkgZmluYWwgcG9zaXRpb246XCIsIHBhdGhfc2dkWy0xXS5yb3VuZCg0KSlcbnByaW50KFwiU0dEIGVzY2FwZWQgc2FkZGxlIGluIHktZGlyZWN0aW9uOlwiLCBhYnMocGF0aF9zZ2RbLTFdWzFdKSA+IDEuMCkifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJMb3NzIExhbmRzY2FwZSBvZiBOZXVyYWwgTmV0d29ya3MifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJHb29kZmVsbG93IGV0IGFsLiAoMjAxNSkgc2hvd2VkIHRoYXQgbGluZWFybHkgaW50ZXJwb2xhdGluZyBiZXR3ZWVuIGluaXRpYWwgYW5kIGZpbmFsIHdlaWdodHMgdHlwaWNhbGx5IHByb2R1Y2VzIGEgcGF0aCBvZiBtb25vdG9uaWNhbGx5IGRlY3JlYXNpbmcgbG9zcywgc3VnZ2VzdGluZyBsb2NhbCBtaW5pbWEgZm91bmQgYnkgR0QgYXJlIGNsb3NlIHRvIHRoZSBpbml0aWFsaXphdGlvbidzIGJhc2luLiBMaSBldCBhbC4gKDIwMTgpIGludHJvZHVjZWQgZmlsdGVyIG5vcm1hbGl6YXRpb24gZm9yIGxvc3MgdmlzdWFsaXphdGlvbjogcHJvamVjdCB0aGUgbG9zcyBzdXJmYWNlIG9udG8gMkQgdXNpbmcgdHdvIHJhbmRvbSBkaXJlY3Rpb25zIGluIHdlaWdodCBzcGFjZSAobm9ybWFsaXplZCB0byBoYXZlIHRoZSBzYW1lIGxheWVyLXdpc2Ugc2NhbGUgYXMgdGhlIHdlaWdodHMpLCByZXZlYWxpbmcgc2hhcnAgY2xpZmZzIHZzIHNtb290aCB2YWxsZXlzLiBGbGF0IHJlZ2lvbnMgKHNoYWxsb3dlciBsYW5kc2NhcGUpIGNvcnJlbGF0ZSB3aXRoIGJldHRlciBnZW5lcmFsaXphdGlvbiAoZmxhdCBtaW5pbWEgaHlwb3RoZXNpcykuIFRoZSBiZW5pZ24gbGFuZHNjYXBlIGh5cG90aGVzaXMgKEhhZWZmZWxlIGFuZCBWaWRhbCwgZXh0ZW5kZWQgYnkgRHUgZXQgYWwuKTogZm9yIG92ZXItcGFyYW1ldGVyaXplZCBuZXR3b3JrcyB3aXRoIHNwZWNpZmljIGFyY2hpdGVjdHVyZSBjb25kaXRpb25zLCBhbGwgbG9jYWwgbWluaW1hIG9mIHRoZSB0cmFpbmluZyBsb3NzIGFjaGlldmUgemVybyB0cmFpbmluZyBlcnJvciwgYW5kIHRoZWlyIGxvc3MgdmFsdWVzIGFyZSBlcXVhbC4gVGhpcyBtZWFucyBvdmVyLXBhcmFtZXRlcml6YXRpb24g4oCUIGFkZGluZyBtb3JlIHBhcmFtZXRlcnMgdGhhbiBzdHJpY3RseSBuZWVkZWQg4oCUIGZ1bmRhbWVudGFsbHkgY2hhbmdlcyB0aGUgdG9wb2xvZ3kgb2YgdGhlIGxvc3MgbGFuZHNjYXBlIGZyb20gb25lIHdpdGggYmFkIGxvY2FsIG1pbmltYSB0byBvbmUgd2hlcmUgYW55IGxvY2FsIG1pbmltdW0gaXMgZWZmZWN0aXZlbHkgZ2xvYmFsLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliXG5tYXRwbG90bGliLnVzZSgnQWdnJylcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9tb29uc1xuXG5kZWYgc2ltcGxlX2xvc3Mod2VpZ2h0cywgWCwgeSk6XG4gICAgXCJcIlwiMi1sYXllciBuZXR3b3JrIGxvc3MgZm9yIGludGVycG9sYXRpb24gZGVtby5cIlwiXCJcbiAgICBuX2luLCBuX2ggPSBYLnNoYXBlWzFdLCA0XG4gICAgVzEgPSB3ZWlnaHRzWzpuX2luKm5faF0ucmVzaGFwZShuX2gsIG5faW4pXG4gICAgYjEgPSB3ZWlnaHRzW25faW4qbl9oOm5faW4qbl9oK25faF1cbiAgICBXMiA9IHdlaWdodHNbbl9pbipuX2grbl9oOm5faW4qbl9oK25faCtuX2hdXG4gICAgYjIgPSB3ZWlnaHRzWy0xXVxuICAgIGggPSBucC5tYXhpbXVtKDAsIFggQCBXMS5UICsgYjEpXG4gICAgb3V0ID0gaCBAIFcyICsgYjJcbiAgICByZXR1cm4gbnAubWVhbigob3V0IC0geSkqKjIpXG5cblgsIHkgPSBtYWtlX21vb25zKG5fc2FtcGxlcz0xMDAsIG5vaXNlPTAuMSwgcmFuZG9tX3N0YXRlPTApXG5uX3BhcmFtcyA9IFguc2hhcGVbMV0gKiA0ICsgNCArIDQgKyAxXG5ucC5yYW5kb20uc2VlZCgwKVxud19pbml0ID0gbnAucmFuZG9tLnJhbmRuKG5fcGFyYW1zKSAqIDAuMVxud19maW5hbCA9IG5wLnJhbmRvbS5yYW5kbihuX3BhcmFtcykgKiAwLjUgICMgc2ltdWxhdGUgdHJhaW5lZCB3ZWlnaHRzXG5cbiMgSW50ZXJwb2xhdGUgYmV0d2VlbiBpbml0IGFuZCBmaW5hbFxuYWxwaGFzID0gbnAubGluc3BhY2UoMCwgMSwgNTApXG5sb3NzZXMgPSBbc2ltcGxlX2xvc3MoKDEtYSkqd19pbml0ICsgYSp3X2ZpbmFsLCBYLCB5KSBmb3IgYSBpbiBhbHBoYXNdXG5cbnByaW50KFwiTG9zcyBhdCBhbHBoYT0wIChpbml0KTpcIiwgcm91bmQobG9zc2VzWzBdLCA0KSlcbnByaW50KFwiTG9zcyBhdCBhbHBoYT0xIChmaW5hbCk6XCIsIHJvdW5kKGxvc3Nlc1stMV0sIDQpKVxucHJpbnQoXCJMb2NhbCBtYXggb24gcGF0aD9cIiwgYW55KGxvc3Nlc1tpXSA+IGxvc3Nlc1tpLTFdIGFuZCBsb3NzZXNbaV0gPiBsb3NzZXNbaSsxXVxuICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgbGVuKGxvc3NlcyktMSkpKVxucHJpbnQoXCJNb25vdG9uZSBkZWNyZWFzZT9cIiwgYWxsKGxvc3Nlc1tpXSA+PSBsb3NzZXNbaSsxXSBmb3IgaSBpbiByYW5nZShsZW4obG9zc2VzKS0xKSkpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTW9kZSBDb25uZWN0aXZpdHkifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJHYXJpcG92IGV0IGFsLiAoMjAxOCkgYW5kIERyYXhsZXIgZXQgYWwuICgyMDE4KSBkaXNjb3ZlcmVkIHRoYXQgdHdvIGxvY2FsIG1pbmltYSBmb3VuZCBieSBpbmRlcGVuZGVudCBTR0QgcnVucyBhcmUgdHlwaWNhbGx5IGNvbm5lY3RlZCBieSBhIGxvdy1sb3NzIGN1cnZlZCBwYXRoIHRocm91Z2ggd2VpZ2h0IHNwYWNlIOKAlCBkZXNwaXRlIHRoZSBzdHJhaWdodCBsaW5lIGJldHdlZW4gdGhlbSBjcm9zc2luZyBhIGxvc3MgYmFycmllci4gVGhlIGN1cnZlZCBwYXRoIGNhbiBiZSBwYXJhbWV0ZXJpemVkIGFzIGEgQmV6aWVyIGN1cnZlIM+GKHQpID0gKDEtdCnCss644oKBICsgMnQoMS10Kc64X21pZCArIHTCss644oKCIHdpdGggb25lIHRyYWluYWJsZSBtaWRwb2ludCDOuF9taWQuIE1vZGUgY29ubmVjdGl2aXR5IGltcGxpZXMgdGhlIGxvc3MgbGFuZHNjYXBlIGhhcyBhIGNvbm5lY3RlZCAndmFsbGV5JyBzdHJ1Y3R1cmUgcmF0aGVyIHRoYW4gaXNvbGF0ZWQgbWluaW1hLCB3aGljaCBoYXMgcHJvZm91bmQgaW1wbGljYXRpb25zIGZvciBtb2RlbCBtZXJnaW5nIGFuZCBlbnNlbWJsZSBtZXRob2RzLiBMaW5lYXIgTW9kZSBDb25uZWN0aXZpdHkgKExNQyk6IGlmIHRoZSBzdHJhaWdodC1saW5lIHBhdGggYmV0d2VlbiB0d28gc29sdXRpb25zIGFsc28gaGFzIGxvdyBsb3NzIChubyBiYXJyaWVyKSwgdGhlIG1vZGVscyBjYW4gYmUgbGluZWFybHkgaW50ZXJwb2xhdGVkIHdpdGhvdXQgcGVyZm9ybWFuY2UgZGVncmFkYXRpb24uIExNQyBpcyB0aGUgdGhlb3JldGljYWwgZm91bmRhdGlvbiBmb3IgU3RvY2hhc3RpYyBXZWlnaHQgQXZlcmFnaW5nIChTV0EsIEl6bWFpbG92IGV0IGFsLiAyMDE4KSDigJQgYXZlcmFnaW5nIG11bHRpcGxlIGNoZWNrcG9pbnRzIGZyb20gbGF0ZSBpbiB0cmFpbmluZyBwcm9kdWNlcyBhIG1vZGVsIGF0IHRoZSBmbGF0IGNlbnRlciBvZiBhIHdpZGUgdmFsbGV5LiBJdCBpcyBhbHNvIHRoZSBiYXNpcyBmb3IgbW9kZWwgbWVyZ2luZyB0ZWNobmlxdWVzIHdoZXJlIGluZGVwZW5kZW50bHkgZmluZS10dW5lZCBtb2RlbHMgYXJlIG1lcmdlZCBieSBzaW1wbGUgd2VpZ2h0IGF2ZXJhZ2luZyB3aGVuIHRoZXkgYXJlIGluaXRpYWxpemVkIGZyb20gdGhlIHNhbWUgcHJlLXRyYWluZWQgY2hlY2twb2ludC4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNTCBDb25uZWN0aW9uczogTlRLIFJlZ2ltZSBhbmQgQ29udmV4IFByb3hpZXMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJBdCBpbmZpbml0ZSB3aWR0aCwgbmV1cmFsIG5ldHdvcmtzIHRyYWluZWQgd2l0aCBncmFkaWVudCBkZXNjZW50IGJlaGF2ZSBsaWtlIGtlcm5lbCBtZXRob2RzIGdvdmVybmVkIGJ5IHRoZSBOZXVyYWwgVGFuZ2VudCBLZXJuZWwgSyh4LCB4JykgPSDOo+G1oiAo4oiCZih4KS/iiILOuOG1oiko4oiCZih4Jykv4oiCzrjhtaIpLiBJbiB0aGUgTlRLIHJlZ2ltZSwgdGhlIGtlcm5lbCBzdGF5cyBjb25zdGFudCB0aHJvdWdob3V0IHRyYWluaW5nIChwYXJhbWV0ZXJzIGJhcmVseSBtb3ZlIHJlbGF0aXZlIHRvIGluaXRpYWxpemF0aW9uKSwgYW5kIHRoZSBsb3NzIGxhbmRzY2FwZSBpcyBlZmZlY3RpdmVseSBjb252ZXggaW4gZnVuY3Rpb24gc3BhY2Ug4oCUIGdyYWRpZW50IGRlc2NlbnQgcHJvdmFibHkgY29udmVyZ2VzIHRvIGEgZ2xvYmFsIG1pbmltdW0uIEhvd2V2ZXIsIHRoZSBOVEsgcmVnaW1lIHJlcXVpcmVzIGltcHJhY3RpY2FsbHkgbGFyZ2Ugd2lkdGggYW5kIHZlcnkgc21hbGwgbGVhcm5pbmcgcmF0ZXM7IHByYWN0aWNhbCBuZXR3b3JrcyBvcGVyYXRlIGluIHRoZSAnZmVhdHVyZSBsZWFybmluZycgcmVnaW1lIHdoZXJlIHJlcHJlc2VudGF0aW9ucyBldm9sdmUsIGRlcGFydGluZyBmcm9tIE5USyBwcmVkaWN0aW9ucy4gVGhlIHByYWN0aWNhbCB0YWtlYXdheSBmcm9tIE5USyB0aGVvcnk6IG92ZXItcGFyYW1ldGVyaXphdGlvbiBoZWxwcy4gTW9yZSBwYXJhbWV0ZXJzIHJlbGF0aXZlIHRvIGRhdGEgbWFrZXMgdGhlIGxhbmRzY2FwZSBtb3JlIGJlbmlnbiwgcmVkdWNpbmcgdGhlIHByb2JhYmlsaXR5IG9mIGJhZCBsb2NhbCBtaW5pbWEuIFRoaXMgZW1waXJpY2FsbHkgZXhwbGFpbnMgd2h5IHdpZGVyIG5ldHdvcmtzIHRyYWluIG1vcmUgcmVsaWFibHkgdGhhbiBuYXJyb3cgb25lcywgd2h5IExMTXMgYXJlIG92ZXItcGFyYW1ldGVyaXplZCBieSBkZXNpZ24sIGFuZCB3aHkgdGhlICdkb3VibGUgZGVzY2VudCcgcGhlbm9tZW5vbiBvY2N1cnMg4oCUIGFkZGluZyBwYXJhbWV0ZXJzIHBhc3QgdGhlIGludGVycG9sYXRpb24gdGhyZXNob2xkIGNhbiBpbXByb3ZlIHJhdGhlciB0aGFuIGh1cnQgZ2VuZXJhbGl6YXRpb24uIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZ2Rfd2l0aF9wZXJ0dXJiYXRpb24oZiwgZ3JhZF9mLCB4MCwgbHI9MC4wMiwgc3RlcHM9MzAwLFxuICAgICAgICAgICAgICAgICAgICAgICAgICBub2lzZV9zY2FsZT0wLjAsIG5vaXNlX3N0YXJ0PTE1MCk6XG4gICAgXCJcIlwiUnVuIEdELCBvcHRpb25hbGx5IGFkZGluZyBub2lzZSBhZnRlciBub2lzZV9zdGFydCBzdGVwcy5cIlwiXCJcbiAgICB4ID0geDAuY29weSgpXG4gICAgaGlzdG9yeSA9IHsnbG9zcyc6IFtdLCAnZ3JhZF9ub3JtJzogW10sICd4JzogW119XG4gICAgZm9yIHN0ZXAgaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICBsb3NzID0gZih4KVxuICAgICAgICBnID0gZ3JhZF9mKHgpXG4gICAgICAgIG5vaXNlID0gMC4wXG4gICAgICAgIGlmIG5vaXNlX3NjYWxlID4gMCBhbmQgc3RlcCA+PSBub2lzZV9zdGFydDpcbiAgICAgICAgICAgIG5vaXNlID0gbm9pc2Vfc2NhbGUgKiBucC5yYW5kb20ucmFuZG4oKnguc2hhcGUpXG4gICAgICAgIHggPSB4IC0gbHIgKiBnICsgbm9pc2VcbiAgICAgICAgaGlzdG9yeVsnbG9zcyddLmFwcGVuZChsb3NzKVxuICAgICAgICBoaXN0b3J5WydncmFkX25vcm0nXS5hcHBlbmQobnAubGluYWxnLm5vcm0oZykpXG4gICAgICAgIGhpc3RvcnlbJ3gnXS5hcHBlbmQoeC5jb3B5KCkpXG4gICAgcmV0dXJuIGhpc3RvcnlcblxuIyBTYWRkbGU6IGYoeCx5KSA9IHheMiAtIHleMlxuZjJkID0gbGFtYmRhIHh5OiB4eVswXSoqMiAtIHh5WzFdKioyXG5ncmFkMmQgPSBsYW1iZGEgeHk6IG5wLmFycmF5KFsyKnh5WzBdLCAtMip4eVsxXV0pXG5cbm5wLnJhbmRvbS5zZWVkKDcpXG5zdGFydCA9IG5wLmFycmF5KFswLjA1LCAwLjAyXSlcblxuaGlzdF9nZCA9IGdkX3dpdGhfcGVydHVyYmF0aW9uKGYyZCwgZ3JhZDJkLCBzdGFydCwgbHI9MC4wNSwgbm9pc2Vfc2NhbGU9MC4wKVxuaGlzdF9ub2lzeSA9IGdkX3dpdGhfcGVydHVyYmF0aW9uKGYyZCwgZ3JhZDJkLCBzdGFydCwgbHI9MC4wNSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5vaXNlX3NjYWxlPTAuMSwgbm9pc2Vfc3RhcnQ9NTApXG5cbnByaW50KFwiR0Q6IGZpbmFsIGdyYWRfbm9ybSA9XCIsIHJvdW5kKGhpc3RfZ2RbJ2dyYWRfbm9ybSddWy0xXSwgNSkpXG5wcmludChcIkdEOiBmaW5hbCB4ID1cIiwgbnAucm91bmQoaGlzdF9nZFsneCddWy0xXSwgNCkpXG5wcmludChcIk5vaXN5IEdEOiBmaW5hbCBncmFkX25vcm0gPVwiLCByb3VuZChoaXN0X25vaXN5WydncmFkX25vcm0nXVstMV0sIDUpKVxucHJpbnQoXCJOb2lzeSBHRDogZmluYWwgeCA9XCIsIG5wLnJvdW5kKGhpc3Rfbm9pc3lbJ3gnXVstMV0sIDQpKVxucHJpbnQoXCJHRCBzdGFsbGVkIGF0IHNhZGRsZTpcIiwgaGlzdF9nZFsnZ3JhZF9ub3JtJ11bLTFdIDwgMC4wMSlcbnByaW50KFwiTm9pc3kgR0QgZXNjYXBlZDpcIiwgYWJzKGhpc3Rfbm9pc3lbJ3gnXVstMV1bMV0pID4gMC41KSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkltcGxlbWVudGF0aW9uIFBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhyZWUgY3JpdGljYWwgcGl0ZmFsbHMgd2hlbiByZWFzb25pbmcgYWJvdXQgbG9zcyBsYW5kc2NhcGVzIGluIHByYWN0aWNlLiBGaXJzdCwgZ3JhZGllbnQgdmFuaXNoaW5nIG5lYXIgc2FkZGxlIHBvaW50czogdGhlIGdyYWRpZW50IG5vcm0gYXBwcm9hY2hlcyB6ZXJvIGF0IHNhZGRsZSBwb2ludHMganVzdCBhcyBpdCBkb2VzIGF0IG1pbmltYSDigJQgbW9uaXRvcmluZyBvbmx5IGxvc3MgZ2l2ZXMgbm8gc2lnbmFsIGFib3V0IHdoaWNoIHlvdSBoYXZlIHJlYWNoZWQuIEFsd2F5cyBsb2cg4oCW4oiHTOKAliBhbmQgbG9zcyBzZXBhcmF0ZWx5OyBhIHBsYXRlYXUgaW4gYm90aCBzaWduYWxzIGEgc2FkZGxlLCBub3QgY29udmVyZ2VuY2UuIFNlY29uZCwgbGVhcm5pbmcgcmF0ZSBjaG9pY2UgaW4gbm9uLWNvbnZleCBsYW5kc2NhcGVzOiB0b28gbGFyZ2UgYSBsZWFybmluZyByYXRlIGNhdXNlcyBvc2NpbGxhdGlvbiBhY3Jvc3Mgc2hhcnAgcmlkZ2VzICh6aWd6YWcgaW4gdGhlIGxvc3MgY3VydmUpOyB0b28gc21hbGwgYSByYXRlIGNhdXNlcyB0aGUgdHJhamVjdG9yeSB0byBzdGFsbCBpbiB0aGUgZmlyc3QgbG9jYWwgYmFzaW4gaXQgZmluZHMuIFRoZSBvcHRpbWFsIExSIGZvciBub24tY29udmV4IHByb2JsZW1zIGlzIHR5cGljYWxseSBmb3VuZCB2aWEgd2FybXVwLXRoZW4tZGVjYXkgc2NoZWR1bGVzIHRoYXQgc3RhcnQgY29uc2VydmF0aXZlbHkgYW5kIGluY3JlYXNlIGJyaWVmbHkuIFRoaXJkLCBzaW5nbGUgcmFuZG9tIHJlc3RhcnQgaXMgaW5zdWZmaWNpZW50OiBmb3IgaGlnaGx5IG5vbi1jb252ZXggb2JqZWN0aXZlcywgYWx3YXlzIHJ1biBhdCBsZWFzdCAzLTUgcmFuZG9tIHJlc3RhcnRzIHdpdGggZGlmZmVyZW50IHJhbmRvbSBzZWVkcyBhbmQgc2VsZWN0IHRoZSBjaGVja3BvaW50IHdpdGggYmVzdCB2YWxpZGF0aW9uIGxvc3MsIHNpbmNlIGRpZmZlcmVudCBzZWVkcyBmaW5kIGRpZmZlcmVudCBiYXNpbnMgd2l0aCBkaWZmZXJlbnQgZ2VuZXJhbGl6YXRpb24gcHJvcGVydGllcy4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQcmFjdGljYWwgR3VpZGFuY2UifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJGb3IgbmV1cmFsIG5ldHdvcmsgdHJhaW5pbmcgb24gbm9uLWNvbnZleCBsYW5kc2NhcGVzLCBhcHBseSB0aGVzZSBldmlkZW5jZS1iYXNlZCBzdHJhdGVnaWVzLiBVc2UgbGVhcm5pbmcgcmF0ZSB3YXJtdXAgZm9yIHRoZSBmaXJzdCA1LTEwJSBvZiB0cmFpbmluZyBzdGVwczogdGhpcyBwcmV2ZW50cyBlYXJseSBsYXJnZSBzdGVwcyB0aGF0IGNvdWxkIHB1c2ggdGhlIG1vZGVsIGludG8gYSBiYWQgYmFzaW4gZnJvbSB3aGljaCBlc2NhcGUgaXMgZGlmZmljdWx0LiBNb25pdG9yIOKAluKIh0zigJYgKGdyYWRpZW50IG5vcm0pIGV2ZXJ5IDEwMCBzdGVwcyDigJQgYSBoZWFsdGh5IHRyYWluaW5nIHJ1biBzaG93cyBncmFkdWFsbHkgZGVjcmVhc2luZyBncmFkaWVudCBub3JtOyBwZXJzaXN0ZW50IGxhcmdlIGdyYWRpZW50IG5vcm0gaW5kaWNhdGVzIHRoZSBtb2RlbCBpcyBub3QgY29udmVyZ2luZywgd2hpbGUgc3VkZGVuIHNwaWtlcyBpbmRpY2F0ZSBpbnN0YWJpbGl0eS4gVXNlIFNXQSAoU3RvY2hhc3RpYyBXZWlnaHQgQXZlcmFnaW5nKSBieSBhdmVyYWdpbmcgY2hlY2twb2ludHMgZnJvbSB0aGUgbGFzdCAyMCUgb2YgdHJhaW5pbmc6IHRoaXMgbW92ZXMgdGhlIGVmZmVjdGl2ZSBwYXJhbWV0ZXIgdmVjdG9yIHRvd2FyZCB0aGUgZmxhdCBjZW50ZXIgb2YgdGhlIGxvc3MgYmFzaW4sIGltcHJvdmluZyBib3RoIGdlbmVyYWxpemF0aW9uIGFuZCBjYWxpYnJhdGlvbiB3aXRob3V0IGFueSBhZGRpdGlvbmFsIHRyYWluaW5nIGNvc3QuIEZvciB0YXNrcyB3aXRoIGtub3duIGNvbnZleCBwcm94aWVzIChsb2dpc3RpYyByZWdyZXNzaW9uLCBsaW5lYXIgU1ZNKSwgcHJlZmVyIHRoZSBjb252ZXggZm9ybXVsYXRpb24gdW5sZXNzIHlvdSBoYXZlIHN0cm9uZyByZWFzb25zIHRvIHVzZSBhIG5ldXJhbCBuZXR3b3JrIOKAlCBjb252ZXggcHJvYmxlbXMgaGF2ZSBwcm92YWJsZSBnbG9iYWwgY29udmVyZ2VuY2UgZ3VhcmFudGVlcyBhbmQgbm8gc2FkZGxlIHBvaW50cy4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidGl0bGUiOiAiV2FybmluZyIsICJjb250ZW50IjogIkEgZGVjcmVhc2luZyB0cmFpbmluZyBsb3NzIGRvZXMgTk9UIG1lYW4geW91IGFyZSBuZWFyIGEgZ29vZCBtaW5pbXVtIOKAlCB5b3UgY291bGQgYmUgYXBwcm9hY2hpbmcgYSBzYWRkbGUgcG9pbnQgd2hlcmUgbG9zcyBpcyBzdGlsbCBkZWNyZWFzaW5nIGJ1dCBncmFkaWVudCBpcyBjb2xsYXBzaW5nIHRvd2FyZCB6ZXJvLiBNb25pdG9yIOKAluKIh0zigJYgc2VwYXJhdGVseSBmcm9tIGxvc3MgYXQgZXZlcnkgY2hlY2twb2ludC4gQSBzYWRkbGUgbWFuaWZlc3RzIGFzOiBsb3NzIHN0aWxsIGRlY3JlYXNpbmcgYnV0IGdyYWRpZW50IG5vcm0gYWxzbyBkZWNyZWFzaW5nIHRvd2FyZCB6ZXJvIHdoaWxlIHZhbGlkYXRpb24gbG9zcyBwbGF0ZWF1cy4gSWYgeW91IHNlZSB0aGlzIHBhdHRlcm4gYmVmb3JlIGV4cGVjdGVkIGNvbnZlcmdlbmNlLCBhZGQgZ3JhZGllbnQgbm9pc2Ugb3IgcmVkdWNlIHRoZSBsZWFybmluZyByYXRlIHRlbXBvcmFyaWx5IHRvIGVzY2FwZS4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIkZ1bmN0aW9uIENsYXNzIiwgIkRlZmluaXRpb24iLCAiR2xvYmFsIE1pbiBHdWFyYW50ZWUiLCAiR0QgQ29udmVyZ2VuY2UgUmF0ZSIsICJFeGFtcGxlIExvc3MiXSwgInJvd3MiOiBbWyJDb252ZXgiLCAiZijOu3grKDEtzrspeSkg4omkIM67Zih4KSsoMS3OuylmKHkpIiwgIkFueSBsb2NhbCBtaW4gaXMgZ2xvYmFsIiwgIk8oMS90KSIsICJMb2ctbG9zcywgSGluZ2UgbG9zcyJdLCBbIlN0cmljdGx5IENvbnZleCIsICJTdHJpY3QgaW5lcXVhbGl0eSBmb3IgeOKJoHkiLCAiVW5pcXVlIGdsb2JhbCBtaW4iLCAiTygxL3QpIiwgIlNxdWFyZWQgbG9zcyB3aXRoIEwyIHJlZyJdLCBbIlN0cm9uZ2x5IENvbnZleCAozrwpIiwgIkgg4om9IM68SSwgzrwgPiAwIiwgIlVuaXF1ZSBnbG9iYWwgbWluIiwgIkxpbmVhciBPKM+B4bWXKSwgz4E8MSIsICJSaWRnZSByZWdyZXNzaW9uIl0sIFsiTm9uLWNvbnZleCBQTCoiLCAiwr3igJbiiIdm4oCWwrIg4omlIM68KGbiiJJmKikiLCAiTm90IGd1YXJhbnRlZWQgKFBMIGdpdmVzIGxpbmVhciByYXRlKSIsICJMaW5lYXIgdW5kZXIgUEwiLCAiU29tZSBvdmVyLXBhcmFtIE5OcyJdLCBbIkdlbmVyYWwgTm9uLWNvbnZleCIsICJObyBjb25kaXRpb24iLCAiTm8gZ3VhcmFudGVlIiwgIk8oMS/iiJp0KSB0byBzdGF0aW9uYXJ5IiwgIkRlZXAgbmV0d29yayBsb3NzZXMiXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAiaXRlbXMiOiBbIkNvbnZleCBmdW5jdGlvbnMgc2F0aXNmeSBmKM67eCsoMS3Ouyl5KSDiiaQgzrtmKHgpKygxLc67KWYoeSk7IHN0cm9uZ2x5IGNvbnZleCBhZGRzIGEgcXVhZHJhdGljIGxvd2VyIGJvdW5kIHdpdGggcGFyYW1ldGVyIM68LCBndWFyYW50ZWVpbmcgbGluZWFyIGNvbnZlcmdlbmNlIG9mIEdELiIsICJMb2dpc3RpYyByZWdyZXNzaW9uIHdpdGggbG9nLWxvc3MgaXMgY29udmV4IChncmFkaWVudCBhbGlnbm1lbnQgcHJvcGVydHkgaG9sZHMpOyBuZXVyYWwgbmV0d29ya3MgYXJlIG5vdCBjb252ZXggYmVjYXVzZSBub24tbGluZWFyIGFjdGl2YXRpb25zIGJyZWFrIHRoZSBjb21wb3NpdGlvbiBydWxlLiIsICJJbiBoaWdoIGRpbWVuc2lvbnMsIHJhbmRvbSBtYXRyaXggdGhlb3J5IHByZWRpY3RzIHRoYXQgbW9zdCBjcml0aWNhbCBwb2ludHMgYXJlIHNhZGRsZSBwb2ludHMgKHJvdWdobHkgaGFsZiBvZiBIZXNzaWFuIGVpZ2VudmFsdWVzIGFyZSBuZWdhdGl2ZSksIG5vdCBsb2NhbCBtaW5pbWEg4oCUICdiYWQgbG9jYWwgbWluaW1hJyBhcmUgcmFyZS4iLCAiU2FkZGxlIHBvaW50cyBzdGFsbCBncmFkaWVudCBkZXNjZW50IChncmFkaWVudCDihpIgMCkgYnV0IFNHRCdzIG1pbmktYmF0Y2ggbm9pc2UgbmF0dXJhbGx5IHBlcnR1cmJzIHRoZSB0cmFqZWN0b3J5OyBpZiBTR0Qgc3RhbGxzLCBhZGQgZXhwbGljaXQgcGVydHVyYmF0aW9uIG5vaXNlLiIsICJNb2RlIGNvbm5lY3Rpdml0eTogdHdvIGluZGVwZW5kZW50bHkgdHJhaW5lZCBtaW5pbWEgYXJlIHR5cGljYWxseSBjb25uZWN0ZWQgYnkgYSBsb3ctbG9zcyBjdXJ2ZWQgcGF0aCAoQmV6aWVyIGN1cnZlKSwgaW1wbHlpbmcgYSB2YWxsZXkgc3RydWN0dXJlIHJhdGhlciB0aGFuIGlzb2xhdGVkIGJhc2lucy4iLCAiTGluZWFyIE1vZGUgQ29ubmVjdGl2aXR5IGVuYWJsZXMgbW9kZWwgbWVyZ2luZyBhbmQgU1dBOiBtb2RlbHMgZnJvbSB0aGUgc2FtZSBwcmUtdHJhaW5lZCBjaGVja3BvaW50IGNhbiBiZSBsaW5lYXJseSBpbnRlcnBvbGF0ZWQgd2l0aG91dCBsb3NzIGJhcnJpZXIuIiwgIlRoZSBOVEsgcmVnaW1lIChpbmZpbml0ZSB3aWR0aCkgZ2l2ZXMgYSBjb252ZXggbG9zcyBsYW5kc2NhcGU7IHByYWN0aWNhbCB0YWtlYXdheSBpcyB0aGF0IG92ZXItcGFyYW1ldGVyaXphdGlvbiByZWR1Y2VzIHRoZSBwcm9iYWJpbGl0eSBvZiBiYWQgbG9jYWwgbWluaW1hLiJdfV0="
---

# Convex vs Non-Convex Loss Landscapes

The geometry of a loss function determines whether gradient descent can find good solutions efficiently. Convex landscapes have exactly one basin containing the global minimum, so any descent algorithm with sufficient step size eventually converges. Non-convex landscapes — characteristic of neural networks — contain multiple basins, saddle points, ridges, and plateaus. Understanding this geometry guides architecture design, optimizer choice, and training strategies. This note builds rigorous intuition from convex function theory through the practical implications for modern deep learning, covering the prevalence of saddle points predicted by random matrix theory, loss landscape visualization, mode connectivity, and the Neural Tangent Kernel regime.

## Convex Functions: Definitions and Properties

A function f: R^n → R is convex if for all x, y in its domain and all λ ∈ [0,1]: f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y). The chord connecting any two points on the graph lies above or on the graph. Strict convexity requires strict inequality for x ≠ y, guaranteeing a unique global minimum. μ-strongly convex (μ > 0) means f(y) ≥ f(x) + ∇f(x)ᵀ(y−x) + (μ/2)‖y−x‖² — the function is lower-bounded by a quadratic. Equivalent Hessian condition: H ≽ 0 (PSD) for convex, H ≻ 0 (PD) for strictly convex, H ≽ μI for μ-strongly convex. Logistic regression with log-loss IS convex: the log-sum-exp is convex, composition with a linear function preserves convexity. Neural networks are NOT convex: the composition f(Wx) with non-linear activation f breaks the convexity-preserving composition rule (which requires f to be convex and non-decreasing, but ReLU applied to a linear layer makes the composite non-convex when layers are stacked).

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

def check_convexity_numerically(f, n_samples=500, n_dim=5, tol=1e-6):
    """Sample pairs (x, y) and check f(λx+(1-λ)y) <= λf(x)+(1-λ)f(y)."""
    violations = 0
    for _ in range(n_samples):
        x = np.random.randn(n_dim)
        y = np.random.randn(n_dim)
        lam = np.random.uniform(0.01, 0.99)
        lhs = f(lam * x + (1 - lam) * y)
        rhs = lam * f(x) + (1 - lam) * f(y)
        if lhs > rhs + tol:
            violations += 1
    return violations, n_samples

# Logistic loss (convex)
def logistic_loss(params, X, y):
    w, b = params[:-1], params[-1]
    logits = X @ w + b
    return np.mean(np.log(1 + np.exp(-y * logits)))

X, y = make_classification(n_samples=50, n_features=4, random_state=0)
y = 2 * y - 1  # {-1, +1}
f_logistic = lambda p: logistic_loss(p, X, y)
viol, total = check_convexity_numerically(f_logistic, n_dim=5)
print(f"Logistic loss violations: {viol}/{total} (expected 0)")

# Simple 2-layer NN loss (non-convex)
def nn_loss(params):
    W1 = params[:8].reshape(2, 4)
    W2 = params[8:10]
    h = np.maximum(0, X @ W1.T)  # ReLU
    out = h @ W2
    return np.mean((out - y) ** 2)

viol2, total2 = check_convexity_numerically(nn_loss, n_dim=10)
print(f"NN loss violations: {viol2}/{total2} (expected > 0)")
```

## Saddle Points in High Dimensions

The index of a saddle point is the fraction of negative Hessian eigenvalues at that critical point. Random matrix theory (Wigner semicircle law) predicts that for a random n×n symmetric matrix, approximately half the eigenvalues are negative. This means that at a random critical point in high-dimensional non-convex landscapes, roughly half the curvature directions point downward — i.e., most critical points are saddle points, not local minima. Dauphin et al. (2014) showed empirically that in deep networks, critical points encountered during training have loss close to the global minimum, contradicting the fear of 'bad local minima.' Instead, saddle points dominate: the gradient norm is near zero (GD stalls) but loss is above the global minimum. Three escape mechanisms: (1) SGD's gradient noise from mini-batching perturbs the trajectory off the saddle; (2) Negative curvature exploitation (Carmon et al.): follow the most negative eigenvector direction; (3) Perturbation-then-restart (Ge et al. 2015): add random noise to weights when gradient norm < threshold.

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Function with a known saddle at origin: f(x,y) = x^2 - y^2
def f(xy): return xy[0]**2 - xy[1]**2
def grad_f(xy): return np.array([2*xy[0], -2*xy[1]])

def gradient_descent(start, lr=0.05, steps=200, noise=0.0):
    path = [start.copy()]
    xy = start.copy()
    for _ in range(steps):
        g = grad_f(xy)
        xy = xy - lr * g + noise * np.random.randn(2)
        path.append(xy.copy())
    return np.array(path)

# GD from near saddle: start at [0.01, 0.1] (slight offset)
np.random.seed(42)
start_near_saddle = np.array([0.01, 0.1])

path_gd = gradient_descent(start_near_saddle, lr=0.05, noise=0.0)
path_sgd = gradient_descent(start_near_saddle, lr=0.05, noise=0.02)

print("GD near saddle — final position:", path_gd[-1].round(4))
print("GD gradient norm history (first 10):",
      [round(np.linalg.norm(grad_f(p)), 4) for p in path_gd[:10]])
print("SGD (with noise) final position:", path_sgd[-1].round(4))
print("SGD escaped saddle in y-direction:", abs(path_sgd[-1][1]) > 1.0)
```

## Loss Landscape of Neural Networks

Goodfellow et al. (2015) showed that linearly interpolating between initial and final weights typically produces a path of monotonically decreasing loss, suggesting local minima found by GD are close to the initialization's basin. Li et al. (2018) introduced filter normalization for loss visualization: project the loss surface onto 2D using two random directions in weight space (normalized to have the same layer-wise scale as the weights), revealing sharp cliffs vs smooth valleys. Flat regions (shallower landscape) correlate with better generalization (flat minima hypothesis). The benign landscape hypothesis (Haeffele and Vidal, extended by Du et al.): for over-parameterized networks with specific architecture conditions, all local minima of the training loss achieve zero training error, and their loss values are equal. This means over-parameterization — adding more parameters than strictly needed — fundamentally changes the topology of the loss landscape from one with bad local minima to one where any local minimum is effectively global.

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

def simple_loss(weights, X, y):
    """2-layer network loss for interpolation demo."""
    n_in, n_h = X.shape[1], 4
    W1 = weights[:n_in*n_h].reshape(n_h, n_in)
    b1 = weights[n_in*n_h:n_in*n_h+n_h]
    W2 = weights[n_in*n_h+n_h:n_in*n_h+n_h+n_h]
    b2 = weights[-1]
    h = np.maximum(0, X @ W1.T + b1)
    out = h @ W2 + b2
    return np.mean((out - y)**2)

X, y = make_moons(n_samples=100, noise=0.1, random_state=0)
n_params = X.shape[1] * 4 + 4 + 4 + 1
np.random.seed(0)
w_init = np.random.randn(n_params) * 0.1
w_final = np.random.randn(n_params) * 0.5  # simulate trained weights

# Interpolate between init and final
alphas = np.linspace(0, 1, 50)
losses = [simple_loss((1-a)*w_init + a*w_final, X, y) for a in alphas]

print("Loss at alpha=0 (init):", round(losses[0], 4))
print("Loss at alpha=1 (final):", round(losses[-1], 4))
print("Local max on path?", any(losses[i] > losses[i-1] and losses[i] > losses[i+1]
      for i in range(1, len(losses)-1)))
print("Monotone decrease?", all(losses[i] >= losses[i+1] for i in range(len(losses)-1)))
```

## Mode Connectivity

Garipov et al. (2018) and Draxler et al. (2018) discovered that two local minima found by independent SGD runs are typically connected by a low-loss curved path through weight space — despite the straight line between them crossing a loss barrier. The curved path can be parameterized as a Bezier curve φ(t) = (1-t)²θ₁ + 2t(1-t)θ_mid + t²θ₂ with one trainable midpoint θ_mid. Mode connectivity implies the loss landscape has a connected 'valley' structure rather than isolated minima, which has profound implications for model merging and ensemble methods. Linear Mode Connectivity (LMC): if the straight-line path between two solutions also has low loss (no barrier), the models can be linearly interpolated without performance degradation. LMC is the theoretical foundation for Stochastic Weight Averaging (SWA, Izmailov et al. 2018) — averaging multiple checkpoints from late in training produces a model at the flat center of a wide valley. It is also the basis for model merging techniques where independently fine-tuned models are merged by simple weight averaging when they are initialized from the same pre-trained checkpoint.

## ML Connections: NTK Regime and Convex Proxies

At infinite width, neural networks trained with gradient descent behave like kernel methods governed by the Neural Tangent Kernel K(x, x') = Σᵢ (∂f(x)/∂θᵢ)(∂f(x')/∂θᵢ). In the NTK regime, the kernel stays constant throughout training (parameters barely move relative to initialization), and the loss landscape is effectively convex in function space — gradient descent provably converges to a global minimum. However, the NTK regime requires impractically large width and very small learning rates; practical networks operate in the 'feature learning' regime where representations evolve, departing from NTK predictions. The practical takeaway from NTK theory: over-parameterization helps. More parameters relative to data makes the landscape more benign, reducing the probability of bad local minima. This empirically explains why wider networks train more reliably than narrow ones, why LLMs are over-parameterized by design, and why the 'double descent' phenomenon occurs — adding parameters past the interpolation threshold can improve rather than hurt generalization.

```python
import numpy as np

def gd_with_perturbation(f, grad_f, x0, lr=0.02, steps=300,
                          noise_scale=0.0, noise_start=150):
    """Run GD, optionally adding noise after noise_start steps."""
    x = x0.copy()
    history = {'loss': [], 'grad_norm': [], 'x': []}
    for step in range(steps):
        loss = f(x)
        g = grad_f(x)
        noise = 0.0
        if noise_scale > 0 and step >= noise_start:
            noise = noise_scale * np.random.randn(*x.shape)
        x = x - lr * g + noise
        history['loss'].append(loss)
        history['grad_norm'].append(np.linalg.norm(g))
        history['x'].append(x.copy())
    return history

# Saddle: f(x,y) = x^2 - y^2
f2d = lambda xy: xy[0]**2 - xy[1]**2
grad2d = lambda xy: np.array([2*xy[0], -2*xy[1]])

np.random.seed(7)
start = np.array([0.05, 0.02])

hist_gd = gd_with_perturbation(f2d, grad2d, start, lr=0.05, noise_scale=0.0)
hist_noisy = gd_with_perturbation(f2d, grad2d, start, lr=0.05,
                                    noise_scale=0.1, noise_start=50)

print("GD: final grad_norm =", round(hist_gd['grad_norm'][-1], 5))
print("GD: final x =", np.round(hist_gd['x'][-1], 4))
print("Noisy GD: final grad_norm =", round(hist_noisy['grad_norm'][-1], 5))
print("Noisy GD: final x =", np.round(hist_noisy['x'][-1], 4))
print("GD stalled at saddle:", hist_gd['grad_norm'][-1] < 0.01)
print("Noisy GD escaped:", abs(hist_noisy['x'][-1][1]) > 0.5)
```

## Implementation Pitfalls

Three critical pitfalls when reasoning about loss landscapes in practice. First, gradient vanishing near saddle points: the gradient norm approaches zero at saddle points just as it does at minima — monitoring only loss gives no signal about which you have reached. Always log ‖∇L‖ and loss separately; a plateau in both signals a saddle, not convergence. Second, learning rate choice in non-convex landscapes: too large a learning rate causes oscillation across sharp ridges (zigzag in the loss curve); too small a rate causes the trajectory to stall in the first local basin it finds. The optimal LR for non-convex problems is typically found via warmup-then-decay schedules that start conservatively and increase briefly. Third, single random restart is insufficient: for highly non-convex objectives, always run at least 3-5 random restarts with different random seeds and select the checkpoint with best validation loss, since different seeds find different basins with different generalization properties.

## Practical Guidance

For neural network training on non-convex landscapes, apply these evidence-based strategies. Use learning rate warmup for the first 5-10% of training steps: this prevents early large steps that could push the model into a bad basin from which escape is difficult. Monitor ‖∇L‖ (gradient norm) every 100 steps — a healthy training run shows gradually decreasing gradient norm; persistent large gradient norm indicates the model is not converging, while sudden spikes indicate instability. Use SWA (Stochastic Weight Averaging) by averaging checkpoints from the last 20% of training: this moves the effective parameter vector toward the flat center of the loss basin, improving both generalization and calibration without any additional training cost. For tasks with known convex proxies (logistic regression, linear SVM), prefer the convex formulation unless you have strong reasons to use a neural network — convex problems have provable global convergence guarantees and no saddle points.

> **Warning**: A decreasing training loss does NOT mean you are near a good minimum — you could be approaching a saddle point where loss is still decreasing but gradient is collapsing toward zero. Monitor ‖∇L‖ separately from loss at every checkpoint. A saddle manifests as: loss still decreasing but gradient norm also decreasing toward zero while validation loss plateaus. If you see this pattern before expected convergence, add gradient noise or reduce the learning rate temporarily to escape.

| Function Class | Definition | Global Min Guarantee | GD Convergence Rate | Example Loss |
|---|---|---|---|---|
| Convex | f(λx+(1-λ)y) ≤ λf(x)+(1-λ)f(y) | Any local min is global | O(1/t) | Log-loss, Hinge loss |
| Strictly Convex | Strict inequality for x≠y | Unique global min | O(1/t) | Squared loss with L2 reg |
| Strongly Convex (μ) | H ≽ μI, μ > 0 | Unique global min | Linear O(ρᵗ), ρ<1 | Ridge regression |
| Non-convex PL* | ½‖∇f‖² ≥ μ(f−f*) | Not guaranteed (PL gives linear rate) | Linear under PL | Some over-param NNs |
| General Non-convex | No condition | No guarantee | O(1/√t) to stationary | Deep network losses |

---

## Key Takeaways

- Convex functions satisfy f(λx+(1-λ)y) ≤ λf(x)+(1-λ)f(y); strongly convex adds a quadratic lower bound with parameter μ, guaranteeing linear convergence of GD.
- Logistic regression with log-loss is convex (gradient alignment property holds); neural networks are not convex because non-linear activations break the composition rule.
- In high dimensions, random matrix theory predicts that most critical points are saddle points (roughly half of Hessian eigenvalues are negative), not local minima — 'bad local minima' are rare.
- Saddle points stall gradient descent (gradient → 0) but SGD's mini-batch noise naturally perturbs the trajectory; if SGD stalls, add explicit perturbation noise.
- Mode connectivity: two independently trained minima are typically connected by a low-loss curved path (Bezier curve), implying a valley structure rather than isolated basins.
- Linear Mode Connectivity enables model merging and SWA: models from the same pre-trained checkpoint can be linearly interpolated without loss barrier.
- The NTK regime (infinite width) gives a convex loss landscape; practical takeaway is that over-parameterization reduces the probability of bad local minima.

