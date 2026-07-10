---
title: "Deformable Convolutions — Learned Geometric Offsets"
slug: "deformable-convolutions"
description: "Deformable convolutions (Dai et al. 2017): learn spatial offset Δpₙ per kernel position enabling flexible sampling beyond fixed grids. Covers DCNv1 (offsets), DCNv2 (modulation scalars), bilinear interpolation, visualization of sampling patterns, DCNv3, and use in object detection."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgY29udm9sdXRpb25zIGFwcGx5IGEgZml4ZWQga8OXayBncmlkIG9mIGtlcm5lbCB3ZWlnaHRzIHRvIGVhY2ggc3BhdGlhbCBsb2NhdGlvbiDigJQgdGhlIHNhbXBsaW5nIHBhdHRlcm4gbmV2ZXIgYWRhcHRzIHRvIHRoZSBjb250ZW50IG9mIHRoZSBpbWFnZS4gRGVmb3JtYWJsZSBDb252b2x1dGlvbnMgKERhaSBldCBhbC4sIElDQ1YgMjAxNykgYnJlYWsgdGhpcyBjb25zdHJhaW50IGJ5IGxlYXJuaW5nIDJEIHNwYXRpYWwgb2Zmc2V0cyDOlHDigpkgZm9yIGVhY2ggb2YgdGhlIGvCsiBrZXJuZWwgcG9zaXRpb25zLiBUaGUgY29udm9sdXRpb24gdGhlbiBzYW1wbGVzIGF0IHBlcnR1cmJlZCBsb2NhdGlvbnMgeCArIHDigpkgKyDOlHDigpkgdXNpbmcgYmlsaW5lYXIgaW50ZXJwb2xhdGlvbiBmb3IgZnJhY3Rpb25hbCBjb29yZGluYXRlcy4gVGhlIG9mZnNldHMgYXJlIGxlYXJuZWQgYnkgYW4gYWRkaXRpb25hbCBsaWdodHdlaWdodCBjb252b2x1dGlvbmFsIGJyYW5jaCwgbWFraW5nIHRoZSBvcGVyYXRpb24gZW5kLXRvLWVuZCBkaWZmZXJlbnRpYWJsZS4gRGVmb3JtYWJsZSBjb252b2x1dGlvbnMgZHJhbWF0aWNhbGx5IGltcHJvdmUgZGV0ZWN0aW9uIGFuZCBzZWdtZW50YXRpb24gb2Ygb2JqZWN0cyB3aXRoIGFyYml0cmFyeSBzaGFwZXMgYW5kIHNpemVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbWl0YXRpb25zIG9mIFN0YW5kYXJkIENvbnZvbHV0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBrw5drIGNvbnZvbHV0aW9uIHNhbXBsZXMga8KyIGZpeGVkIHJlbGF0aXZlIHBvc2l0aW9uczogcOKCmSDiiIggeygtMSwtMSksICgtMSwwKSwgLi4uLCAoMSwxKX0gZm9yIGs9My4gVGhlc2UgcG9zaXRpb25zIGFyZSBmaXhlZCByZWdhcmRsZXNzIG9mIHRoZSBpbnB1dCDigJQgdGhlIHNhbWUgZ3JpZCBpcyBhcHBsaWVkIHRvIGEgdGhpbiB2ZXJ0aWNhbCBsaW5lLCBhIGxhcmdlIGNpcmNsZSwgYW5kIGEgZGlhZ29uYWwgZWRnZS4gVGhpcyBmaXhlZCByZWNlcHRpdmUgZmllbGQgaXMgcG9vcmx5IHN1aXRlZCB0byBvYmplY3RzIHRoYXQgdmFyeSBpbiBzY2FsZSwgYXNwZWN0IHJhdGlvLCBhbmQgb3JpZW50YXRpb24uIFBvb2xpbmcgYW5kIGxhcmdlIHN0cmlkZXMgcHJvdmlkZSBzb21lIHNjYWxlIGludmFyaWFuY2UsIGJ1dCB0aGV5IGNhbm5vdCBhZGFwdCB0aGUgc2FtcGxpbmcgZ2VvbWV0cnkgdG8gbWF0Y2ggb2JqZWN0IHNoYXBlLiBBdWdtZW50YXRpb24gKHJhbmRvbSByb3RhdGlvbiwgc2NhbGluZykgaGVscHMgdHJhaW5pbmcgYnV0IGRvZXMgbm90IGdpdmUgdGhlIG5ldHdvcmsgdGhlIGFiaWxpdHkgdG8gZHluYW1pY2FsbHkgYWRqdXN0IGl0cyBmZWF0dXJlIGV4dHJhY3Rpb24gcGF0dGVybiBhdCBpbmZlcmVuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVmb3JtYWJsZSBDb252b2x1dGlvbiB2MSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRENOdjEgYWRkcyBhIHBhcmFsbGVsIG9mZnNldC1nZW5lcmF0aW5nIGNvbnYgYnJhbmNoIHRoYXQgdGFrZXMgdGhlIGlucHV0IGZlYXR1cmUgbWFwIGFuZCBvdXRwdXRzIDLDl2vCsiBjaGFubmVscyDigJQgdHdvIGNoYW5uZWxzICjOlHgsIM6UeSkgZm9yIGVhY2ggb2YgdGhlIGvCsiBrZXJuZWwgcG9zaXRpb25zLiBUaGVzZSBvZmZzZXRzIGFyZSBhZGRlZCB0byB0aGUgc3RhbmRhcmQgZ3JpZCBwb3NpdGlvbnMsIGFuZCB0aGUgZmVhdHVyZSBtYXAgaXMgc2FtcGxlZCBhdCB0aGUgcmVzdWx0aW5nIGZyYWN0aW9uYWwgbG9jYXRpb25zIHVzaW5nIGJpbGluZWFyIGludGVycG9sYXRpb246IHkocCkgPSDOo+KCmSB3KHDigpkpIMK3IHgocCArIHDigpkgKyDOlHDigpkpLiBUaGUgYmlsaW5lYXIgaW50ZXJwb2xhdGlvbiBtYWtlcyB0aGUgb3BlcmF0aW9uIGRpZmZlcmVudGlhYmxlIHdpdGggcmVzcGVjdCB0byDOlHDigpksIGFsbG93aW5nIGdyYWRpZW50cyB0byBmbG93IHRocm91Z2ggdGhlIHNhbXBsaW5nIGxvY2F0aW9ucyBkdXJpbmcgYmFja3Byb3BhZ2F0aW9uLiBUaGUgb2Zmc2V0IGNvbnYgYnJhbmNoIGlzIGluaXRpYWxpemVkIHdpdGggemVybyB3ZWlnaHRzIHNvIHRoYXQgZGVmb3JtYWJsZSBjb252IHN0YXJ0cyBhcyBzdGFuZGFyZCBjb252IGF0IHRoZSBiZWdpbm5pbmcgb2YgdHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVmb3JtYWJsZSBDb252b2x1dGlvbiB2MiDigJQgTW9kdWxhdGlvbiBTY2FsYXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEQ052MiAoWmh1IGV0IGFsLiwgQ1ZQUiAyMDE5KSBleHRlbmRzIERDTnYxIGJ5IGFkZGl0aW9uYWxseSBsZWFybmluZyBhIG1vZHVsYXRpb24gc2NhbGFyIG3igpkg4oiIICgwLCAxKSBmb3IgZWFjaCBvZiB0aGUga8KyIHNhbXBsaW5nIHBvc2l0aW9ucy4gVGhlIG1vZHVsYXRlZCBzYW1wbGluZyBiZWNvbWVzOiB5KHApID0gzqPigpkgdyhw4oKZKSDCtyBt4oKZIMK3IHgocCArIHDigpkgKyDOlHDigpkpLiBUaGUgbW9kdWxhdGlvbiBzY2FsYXJzIGFjdCBhcyBhdHRlbnRpb24gd2VpZ2h0cyBvdmVyIHRoZSBzYW1wbGluZyBwb3NpdGlvbnMg4oCUIHRoZSBuZXR3b3JrIGNhbiBlZmZlY3RpdmVseSB6ZXJvIG91dCBpcnJlbGV2YW50IHNhbXBsaW5nIGxvY2F0aW9ucyB3aGlsZSBhbXBsaWZ5aW5nIGltcG9ydGFudCBvbmVzLiBUaGUgY29tYmluZWQgb2Zmc2V0K21vZHVsYXRpb24gYnJhbmNoIG91dHB1dHMgM8OXa8KyIGNoYW5uZWxzOiAyw5drwrIgZm9yICjOlHgsIM6UeSkgb2Zmc2V0cyBhbmQga8KyIGZvciBt4oKZIHNjYWxhcnMgKHBhc3NlZCB0aHJvdWdoIFNpZ21vaWQgdG8ga2VlcCBpbiAoMCwxKSkuIERDTnYyIHNpZ25pZmljYW50bHkgb3V0cGVyZm9ybXMgRENOdjEgb24gZGV0ZWN0aW9uIGJlY2F1c2UgaXQgY2FuIGlnbm9yZSBiYWNrZ3JvdW5kIHNhbXBsZXMgdGhhdCBmYWxsIG91dHNpZGUgdGhlIG9iamVjdCBib3VuZGFyeS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkRDTnYyID0gRGVmb3JtYWJsZSArIEFtcGxpdHVkZSBNb2R1bGF0aW9uIiwiY29udGVudCI6IkRDTnYyIGNvbWJpbmVzIHNwYXRpYWwgZGVmb3JtYXRpb24gKHdoZXJlIHRvIHNhbXBsZSkgd2l0aCBhbXBsaXR1ZGUgbW9kdWxhdGlvbiAoaG93IG11Y2ggdG8gd2VpZ2h0IGVhY2ggc2FtcGxlKS4gVGhpcyBnaXZlcyBpdCB0d28gZGVncmVlcyBvZiBmcmVlZG9tIHZlcnN1cyBzdGFuZGFyZCBjb252IChmaXhlZCBsb2NhdGlvbiwgZml4ZWQgd2VpZ2h0KSBhbmQgRENOdjEgKGZyZWUgbG9jYXRpb24sIGZpeGVkIHVuaXQgd2VpZ2h0KS4gVGhlIG1vZHVsYXRpb24gZWZmZWN0aXZlbHkgbWFrZXMgdGhlIHNhbXBsaW5nIHBhdHRlcm4gc3BhcnNlIGFuZCBvYmplY3QtYWRhcHRpdmU6IGZvciBhIGNhciwgdGhlIG5ldHdvcmsgbGVhcm5zIHRvIHNhbXBsZSB3aGVlbCBhbmQgd2luZG93IHBvc2l0aW9ucyB3aXRoIGhpZ2ggd2VpZ2h0IGFuZCBiYWNrZ3JvdW5kIHdpdGggbmVhci16ZXJvIHdlaWdodC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIEV4YW1wbGVzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIE9mZnNldEdlbmVyYXRvcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkxlYXJuIHBlci1wb3NpdGlvbiAyRCBvZmZzZXRzIGZvciBhIGsgeCBrIGRlZm9ybWFibGUgY29udiBrZXJuZWwuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBrZXJuZWxfc2l6ZT0zKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuayA9IGtlcm5lbF9zaXplXG4gICAgICAgIG5fb2Zmc2V0cyA9IDIgKiBrZXJuZWxfc2l6ZSAqIGtlcm5lbF9zaXplICAjIChkeCwgZHkpIHBlciBwb3NpdGlvblxuICAgICAgICBzZWxmLm9mZnNldF9jb252ID0gbm4uQ29udjJkKGluX2NoLCBuX29mZnNldHMsIGtlcm5lbF9zaXplPTMsIHBhZGRpbmc9MSlcbiAgICAgICAgIyBaZXJvLWluaXQ6IGRlZm9ybWFibGUgY29udiBzdGFydHMgYXMgc3RhbmRhcmQgY29udlxuICAgICAgICBubi5pbml0Lnplcm9zXyhzZWxmLm9mZnNldF9jb252LndlaWdodClcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5vZmZzZXRfY29udi5iaWFzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG9mZnNldHMgPSBzZWxmLm9mZnNldF9jb252KHgpICAgIyAoQiwgMiprXjIsIEgsIFcpXG4gICAgICAgIHJldHVybiBvZmZzZXRzXG5cbiMgRGVtb25zdHJhdGUgb2Zmc2V0IHNoYXBlc1xuZ2VuID0gT2Zmc2V0R2VuZXJhdG9yKGluX2NoPTY0LCBrZXJuZWxfc2l6ZT0zKVxueCA9IHRvcmNoLnJhbmRuKDIsIDY0LCAyOCwgMjgpXG5vZmZzZXRzID0gZ2VuKHgpXG5wcmludChmXCJJbnB1dCBmZWF0dXJlIG1hcDoge3guc2hhcGV9XCIpXG5wcmludChmXCJPZmZzZXRzIHNoYXBlOiAgICAge29mZnNldHMuc2hhcGV9ICAoMiAqIDMqMyA9IDE4IGNoYW5uZWxzKVwiKVxucHJpbnQoZlwiSW50ZXJwcmV0YXRpb246ICAgIG9mZnNldFtiLCAybiwgICBoLCB3XSA9IGRlbHRhX3ggZm9yIHBvc2l0aW9uIG4gYXQgKGgsdylcIilcbnByaW50KGZcIiAgICAgICAgICAgICAgICAgICBvZmZzZXRbYiwgMm4rMSwgaCwgd10gPSBkZWx0YV95IGZvciBwb3NpdGlvbiBuIGF0IChoLHcpXCIpXG5wcmludChmXCJaZXJvLWluaXQgbWVhbnM6IGF0IHN0YXJ0IG9mIHRyYWluaW5nLCBhbGwgb2Zmc2V0cz0wIC1cdTAwM2Ugc3RhbmRhcmQgY29udlwiKVxucHJpbnQoZlwiUGFyYW1zIGluIG9mZnNldCBicmFuY2g6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIGdlbi5wYXJhbWV0ZXJzKCkpOix9XCIpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNodmlzaW9uLm9wcyBpbXBvcnQgRGVmb3JtQ29udjJkXG5cbmNsYXNzIERDTnYyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiRGVmb3JtYWJsZSBDb252IHYyOiBvZmZzZXRzICsgbW9kdWxhdGlvbiBzY2FsYXJzIHZpYSB0b3JjaHZpc2lvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2gsIG91dF9jaCwga2VybmVsX3NpemU9Mywgc3RyaWRlPTEsIHBhZGRpbmc9MSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBrMiA9IGtlcm5lbF9zaXplICoga2VybmVsX3NpemVcbiAgICAgICAgIyBCcmFuY2g6IHByZWRpY3QgMiprXjIgb2Zmc2V0cyArIGteMiBtb2R1bGF0aW9uIHNjYWxhcnNcbiAgICAgICAgc2VsZi5vZmZzZXRfbWFzayA9IG5uLkNvbnYyZChpbl9jaCwgMyAqIGsyLCAzLCBzdHJpZGU9MSwgcGFkZGluZz0xKVxuICAgICAgICBzZWxmLmRjbiA9IERlZm9ybUNvbnYyZChpbl9jaCwgb3V0X2NoLCBrZXJuZWxfc2l6ZSwgc3RyaWRlPXN0cmlkZSwgcGFkZGluZz1wYWRkaW5nKVxuICAgICAgICBubi5pbml0Lnplcm9zXyhzZWxmLm9mZnNldF9tYXNrLndlaWdodClcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5vZmZzZXRfbWFzay5iaWFzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG9tID0gc2VsZi5vZmZzZXRfbWFzayh4KSAgICAgICAgICAjIChCLCAzKmteMiwgSCwgVylcbiAgICAgICAgazIgPSBvbS5zaGFwZVsxXSAvLyAzXG4gICAgICAgIG9mZnNldCA9IG9tWzosIDoyKmsyXSAgICAgICAgICAgICAjIHNwYXRpYWwgb2Zmc2V0cyAoZHgsIGR5KSBwZXIgcG9zaXRpb25cbiAgICAgICAgbWFzayAgID0gdG9yY2guc2lnbW9pZChvbVs6LCAyKmsyOl0pICAjIG1vZHVsYXRpb24gaW4gKDAsIDEpXG4gICAgICAgIHJldHVybiBzZWxmLmRjbih4LCBvZmZzZXQsIG1hc2spXG5cbmRjbiA9IERDTnYyKDY0LCAxMjgsIGtlcm5lbF9zaXplPTMsIHBhZGRpbmc9MSlcbnggPSB0b3JjaC5yYW5kbigyLCA2NCwgMjgsIDI4KVxub3V0ID0gZGNuKHgpXG5wcmludChmXCJJbnB1dDogIHt4LnNoYXBlfVwiKVxucHJpbnQoZlwiT3V0cHV0OiB7b3V0LnNoYXBlfVwiKVxucHJpbnQoZlwiT2Zmc2V0K21hc2sgY29udiBwYXJhbXM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIGRjbi5vZmZzZXRfbWFzay5wYXJhbWV0ZXJzKCkpOix9XCIpXG5wcmludChmXCJEQ04ga2VybmVsIHBhcmFtczogICAgICAge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gZGNuLmRjbi5wYXJhbWV0ZXJzKCkpOix9XCIpXG5wcmludChcIm1hc2s9c2lnbW9pZChsb2dpdCkgaW4gKDAsMSkgLVx1MDAzZSBhdHRlbmRzIHRvIHJlbGV2YW50IHNhbXBsaW5nIHBvc2l0aW9uc1wiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdHBsb3RsaWJcbm1hdHBsb3RsaWIudXNlKFx1MDAyN0FnZ1x1MDAyNylcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgdmlzdWFsaXplX29mZnNldHMob2Zmc2V0cywga2VybmVsX3NpemU9MywgbG9jPSgxNCwgMTQpLCBzYXZlX3BhdGg9XHUwMDI3ZGVmb3JtX29mZnNldHMucG5nXHUwMDI3KTpcbiAgICBcIlwiXCJWaXN1YWxpemUgd2hlcmUgYSBkZWZvcm1hYmxlIGNvbnYgc2FtcGxlcyB2cyBzdGFuZGFyZCBjb252IGF0IGEgZ2l2ZW4gbG9jYXRpb24uXCJcIlwiXG4gICAgayA9IGtlcm5lbF9zaXplXG4gICAgciA9IGsgLy8gMlxuICAgICMgU3RhbmRhcmQgZ3JpZCBwb3NpdGlvbnMgcmVsYXRpdmUgdG8gY2VudGVyXG4gICAgZ3ksIGd4ID0gbnAubWVzaGdyaWQocmFuZ2UoLXIsIHIrMSksIHJhbmdlKC1yLCByKzEpLCBpbmRleGluZz1cdTAwMjdpalx1MDAyNylcbiAgICBiYXNlX3ksIGJhc2VfeCA9IGd5LnJhdmVsKCksIGd4LnJhdmVsKClcblxuICAgICMgTGVhcm5lZCBvZmZzZXRzIGF0IHRoZSBxdWVyeSBsb2NhdGlvblxuICAgIGsyID0gayAqIGtcbiAgICBkeSA9IG9mZnNldHNbMCwgOmsyLCAgbG9jWzBdLCBsb2NbMV1dLmRldGFjaCgpLm51bXB5KClcbiAgICBkeCA9IG9mZnNldHNbMCwgazI6LCBsb2NbMF0sIGxvY1sxXV0uZGV0YWNoKCkubnVtcHkoKVxuXG4gICAgc2FtcGxlX3kgPSBsb2NbMF0gKyBiYXNlX3kgKyBkeVxuICAgIHNhbXBsZV94ID0gbG9jWzFdICsgYmFzZV94ICsgZHhcblxuICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oNSwgNSkpXG4gICAgcGx0LnNjYXR0ZXIobG9jWzFdICsgYmFzZV94LCBsb2NbMF0gKyBiYXNlX3ksIGM9XHUwMDI3Ymx1ZVx1MDAyNywgcz0xMDAsXG4gICAgICAgICAgICAgICAgbGFiZWw9XHUwMDI3U3RhbmRhcmQgY29udlx1MDAyNywgbWFya2VyPVx1MDAyN3NcdTAwMjcsIHpvcmRlcj0zKVxuICAgIHBsdC5zY2F0dGVyKHNhbXBsZV94LCBzYW1wbGVfeSwgYz1cdTAwMjdyZWRcdTAwMjcsIHM9MTAwLFxuICAgICAgICAgICAgICAgIGxhYmVsPVx1MDAyN0RlZm9ybWFibGUgY29udlx1MDAyNywgbWFya2VyPVx1MDAyN29cdTAwMjcsIHpvcmRlcj0zKVxuICAgIGZvciBieCwgYnksIHN4LCBzeSBpbiB6aXAobG9jWzFdK2Jhc2VfeCwgbG9jWzBdK2Jhc2VfeSwgc2FtcGxlX3gsIHNhbXBsZV95KTpcbiAgICAgICAgcGx0LmFycm93KGJ4LCBieSwgc3gtYngsIHN5LWJ5LCBjb2xvcj1cdTAwMjdncmF5XHUwMDI3LCBoZWFkX3dpZHRoPTAuMywgYWxwaGE9MC41KVxuICAgIHBsdC5sZWdlbmQoKVxuICAgIHBsdC50aXRsZShcdTAwMjdTYW1wbGluZyBsb2NhdGlvbnM6IHN0YW5kYXJkIChibHVlKSB2cyBkZWZvcm1hYmxlIChyZWQpXHUwMDI3KVxuICAgIHBsdC5zYXZlZmlnKHNhdmVfcGF0aCwgZHBpPTEwMCwgYmJveF9pbmNoZXM9XHUwMDI3dGlnaHRcdTAwMjcpXG4gICAgcGx0LmNsb3NlKClcbiAgICBwcmludChmXHUwMDI3U2F2ZWQge3NhdmVfcGF0aH1cdTAwMjcpXG5cbiMgU2ltdWxhdGUgdHJhaW5lZCBvZmZzZXRzIChub24temVybyA9IGRlZm9ybWF0aW9uIGZyb20gc3RhbmRhcmQgZ3JpZClcbm9mZnNldHMgPSB0b3JjaC5yYW5kbigxLCAxOCwgMjgsIDI4KSAqIDIuNVxudmlzdWFsaXplX29mZnNldHMob2Zmc2V0cywga2VybmVsX3NpemU9MywgbG9jPSgxNCwgMTQpKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuZnJvbSB0b3JjaHZpc2lvbi5vcHMgaW1wb3J0IERlZm9ybUNvbnYyZFxuXG5jbGFzcyBTdGRDb252QmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2gsIG91dF9jaCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmNvbnYgPSBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMywgcGFkZGluZz0xKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gRi5yZWx1KHNlbGYuY29udih4KSlcblxuY2xhc3MgRGVmb3JtQ29udkJsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBvdXRfY2gpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5vZmZzZXQgPSBubi5Db252MmQoaW5fY2gsIDE4LCAzLCBwYWRkaW5nPTEpICAjIDIqMyozPTE4XG4gICAgICAgIHNlbGYuZGNuICAgID0gRGVmb3JtQ29udjJkKGluX2NoLCBvdXRfY2gsIDMsIHBhZGRpbmc9MSlcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5vZmZzZXQud2VpZ2h0KVxuICAgICAgICBubi5pbml0Lnplcm9zXyhzZWxmLm9mZnNldC5iaWFzKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gRi5yZWx1KHNlbGYuZGNuKHgsIHNlbGYub2Zmc2V0KHgpKSlcblxuIyBUZXN0IG9uIHJvdGF0ZWQgZmVhdHVyZSBtYXA6IGRvZXMgZGVmb3JtYWJsZSBjb252IGFkYXB0IGJldHRlcj9cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG54ID0gdG9yY2gucmFuZG4oMSwgMywgMzIsIDMyKVxueF9yb3QgPSB0b3JjaC5yb3Q5MCh4LCBrPTEsIGRpbXM9WzIsIDNdKVxuXG5zdGQgICA9IFN0ZENvbnZCbG9jaygzLCA2NClcbmRlZm9ybSA9IERlZm9ybUNvbnZCbG9jaygzLCA2NClcblxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgZGlmZl9zdGQgICA9IChzdGQoeCkgLSBzdGQoeF9yb3QpKS5hYnMoKS5tZWFuKCkuaXRlbSgpXG4gICAgZGlmZl9kZWZvcm0gPSAoZGVmb3JtKHgpIC0gZGVmb3JtKHhfcm90KSkuYWJzKCkubWVhbigpLml0ZW0oKVxuXG5wcmludChmXCJTdGFuZGFyZCBjb252IHJlc3BvbnNlIGRpZmYgKDkwLWRlZyByb3RhdGlvbik6IHtkaWZmX3N0ZDouNGZ9XCIpXG5wcmludChmXCJEZWZvcm1hYmxlIGNvbnYgcmVzcG9uc2UgZGlmZjogICAgICAgICAgICAgICAgICB7ZGlmZl9kZWZvcm06LjRmfVwiKVxucHJpbnQoXCJBZnRlciB0cmFpbmluZywgZGVmb3JtYWJsZSBjb252IGxlYXJucyBvZmZzZXRzIHRoYXQgY29tcGVuc2F0ZSBmb3Igcm90YXRpb25cIilcbnByaW50KFwiYW5kIG90aGVyIGdlb21ldHJpYyB0cmFuc2Zvcm1zIChzY2FsZSwgc2hlYXIpIHdpdGhvdXQgZXhwbGljaXQgYXVnbWVudGF0aW9uXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRENOdjMgYW5kIEVmZmljaWVuY3kgSW1wcm92ZW1lbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEQ052MyAoSW50ZXJuSW1hZ2UsIENWUFIgMjAyMykgaW50cm9kdWNlcyBncm91cGVkIGRlZm9ybWFibGUgY29udm9sdXRpb246IGluc3RlYWQgb2YgbGVhcm5pbmcgb25lIHNldCBvZiBvZmZzZXRzIGFuZCBtb2R1bGF0aW9ucyBmb3IgYWxsIGNoYW5uZWxzLCBpdCB1c2VzIEcgZ3JvdXBzIGVhY2ggd2l0aCB0aGVpciBvd24gb2Zmc2V0cyBhbmQgbW9kdWxhdGlvbnMsIHNpbWlsYXIgdG8gZ3JvdXBlZCBjb252b2x1dGlvbiBvciBtdWx0aS1oZWFkIGF0dGVudGlvbi4gVGhlIG91dHB1dCBpcyB0aGUgc3VtIGFjcm9zcyBncm91cHMuIERDTnYzIGFsc28gc2VwYXJhdGVzIHRoZSBzcGF0aWFsIGFnZ3JlZ2F0aW9uIChkZWZvcm1hYmxlIHNhbXBsaW5nKSBmcm9tIHRoZSBjaGFubmVsIHByb2plY3Rpb24sIHJlZHVjaW5nIHBhcmFtZXRlciBjb3VudC4gSW50ZXJuSW1hZ2UtSCB3aXRoIERDTnYzIGFjaGlldmVzIDg5LjYlIG9uIEltYWdlTmV0IGFuZCA2NS40IGJveCBBUCBvbiBDT0NPLCBzZXR0aW5nIG5ldyBzdGF0ZS1vZi10aGUtYXJ0IGZvciBDTk4tYmFzZWQgYXJjaGl0ZWN0dXJlcyBhdCB0aGUgdGltZSBvZiBwdWJsaWNhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcHBsaWNhdGlvbnMgaW4gT2JqZWN0IERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVmb3JtYWJsZSBjb252b2x1dGlvbnMgYXJlIHBhcnRpY3VsYXJseSBwb3dlcmZ1bCBpbiBkZXRlY3Rpb24gYmFja2JvbmVzIGJlY2F1c2Ugb2JqZWN0cyB2YXJ5IGluIHNjYWxlIGFuZCBhc3BlY3QgcmF0aW8uIFJlcGxhY2luZyBzdGFuZGFyZCAzw5czIGNvbnZzIGluIFJlc05ldCBzdGFnZSAzIGFuZCA0IHdpdGggRENOdjIgY29uc2lzdGVudGx5IGFkZHMgKzLigJM0JSBBUCBvbiBDT0NPIHdpdGhvdXQgYW55IG90aGVyIGNoYW5nZS4gTWFzayBSLUNOTiB3aXRoIERDTnYyIGltcHJvdmVzIGJvdGggYm94IEFQIGFuZCBtYXNrIEFQLiBUaGUgb2Zmc2V0IHBhdHRlcm5zIGxlYXJuZWQgYnkgZGV0ZWN0aW9uIG5ldHdvcmtzIGFyZSBpbnRlcnByZXRhYmxlOiBmb3IgYSBjYXIsIG9mZnNldHMgY2x1c3RlciBhcm91bmQgd2hlZWwgcG9zaXRpb25zOyBmb3IgYSBwZXJzb24sIHRoZXkgY2x1c3RlciBhcm91bmQgam9pbnRzIGFuZCB0b3Jzby4gVGhpcyBnZW9tZXRyaWMgYWRhcHRpdml0eSByZXBsYWNlcyB0aGUgbmVlZCBmb3IgZXhwbGljaXQgbXVsdGktc2NhbGUgZmVhdHVyZSBhZ2dyZWdhdGlvbiBpbiBzb21lIGRlc2lnbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udm9sdXRpb24gVmFyaWFudCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlZhcmlhbnQiLCJTYW1wbGluZyBQYXR0ZXJuIiwiRXh0cmEgUGFyYW1zIChrPTMpIiwiQmlsaW5lYXIgSW50ZXJwIiwiR2VvbWV0cmljIEZsZXhpYmlsaXR5IiwiQmVzdCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJTdGFuZGFyZCBDb252IiwiRml4ZWQgM8OXMyBncmlkIiwiTm9uZSIsIk5vIiwiTm9uZSDigJQgcmlnaWQiLCJHZW5lcmFsIGZlYXR1cmUgZXh0cmFjdGlvbiJdLFsiRGVmb3JtYWJsZSBDb252IHYxIiwiTGVhcm5lZCBvZmZzZXRzIM6UcOKCmSBwZXIgcG9zaXRpb24iLCIyw5drwrIgcGVyIGxheWVyIiwiWWVzIiwiSGlnaCDigJQgZnJlZSBvZmZzZXRzIiwiU2hhcGUtYWRhcHRpdmUgZGV0ZWN0aW9uIl0sWyJEZWZvcm1hYmxlIENvbnYgdjIiLCJPZmZzZXRzICsgbW9kdWxhdGlvbiBt4oKZIOKIiCAoMCwxKSIsIjPDl2vCsiBwZXIgbGF5ZXIiLCJZZXMiLCJIaWdoICsgYW1wbGl0dWRlIGNvbnRyb2wiLCJEZXRlY3Rpb24sIHNlZ21lbnRhdGlvbiJdLFsiRGVmb3JtYWJsZSBDb252IHYzIiwiR3JvdXBlZCBvZmZzZXRzICsgbW9kdWxhdGlvbiIsIjPDl2vCsi9HIHBlciBncm91cCIsIlllcyIsIkhpZ2ggKyBjaGFubmVsIGdyb3VwaW5nIiwiRWZmaWNpZW50IGxhcmdlLXNjYWxlIGJhY2tib25lIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbXBsZW1lbnRhdGlvbiBOb3RlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiB1c2luZyBkZWZvcm1hYmxlIGNvbnZvbHV0aW9ucyBpbiBwcmFjdGljZSwga2VlcCB0aGVzZSBwb2ludHMgaW4gbWluZDogKDEpIFplcm8taW5pdGlhbGl6ZSB0aGUgb2Zmc2V0IGJyYW5jaCB3ZWlnaHRzIGFuZCBiaWFzZXMgc28gdHJhaW5pbmcgc3RhcnRzIGZyb20gYSBzdGFuZGFyZCBjb252IGFuZCBkZWZvcm1hdGlvbnMgYXJlIGxlYXJuZWQgZ3JhZHVhbGx5OyAoMikgQ2xpcCBvZmZzZXRzIHRvIGEgcmVhc29uYWJsZSByYW5nZSAodHlwaWNhbGx5IMKxKGstMSkpIHRvIHByZXZlbnQgc2FtcGxpbmcgb3V0c2lkZSB0aGUgZmVhdHVyZSBtYXAg4oCUIHRvcmNodmlzaW9uXHUwMDI3cyBEZWZvcm1Db252MmQgaGFuZGxlcyBib3JkZXIgcGFkZGluZyBhdXRvbWF0aWNhbGx5OyAoMykgVXNlIERDTnYyICh3aXRoIG1vZHVsYXRpb24pIG92ZXIgRENOdjEgaW4gYWxsIGRldGVjdGlvbiBzY2VuYXJpb3Mg4oCUIHRoZSBtb2R1bGF0aW9uIHByb3ZpZGVzIG1lYW5pbmdmdWwgYWNjdXJhY3kgZ2FpbnMgd2l0aCBtaW5pbWFsIG92ZXJoZWFkOyAoNCkgUGxhY2UgZGVmb3JtYWJsZSBjb252b2x1dGlvbnMgaW4gdGhlIGRlZXBlciBzdGFnZXMgKHN0YWdlIDMsIDQgaW4gUmVzTmV0KSB3aGVyZSBzZW1hbnRpYyBmZWF0dXJlcyBiZW5lZml0IG1vc3QgZnJvbSBzaGFwZSBhZGFwdGF0aW9uOyAoNSkgTGVhcm5pbmcgcmF0ZSBmb3IgdGhlIG9mZnNldCBicmFuY2ggbWF5IG5lZWQgdHVuaW5nIOKAlCBzdGFydGluZyB3aXRoIGEgbG93ZXIgTFIgZm9yIG9mZnNldHMgKDAuMcOXIGJhY2tib25lIExSKSBjYW4gaW1wcm92ZSBzdGFiaWxpdHkuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJEQ052MTogb2Zmc2V0IM6UcOKCmSBwZXIga2VybmVsIHBvc2l0aW9uOyBiaWxpbmVhciBpbnRlcnBvbGF0aW9uIGF0IHAgKyBw4oKZICsgzpRw4oKZLiIsIkRDTnYyOiBvZmZzZXQgKyBtb2R1bGF0aW9uIG3igpkg4oiIICgwLDEpOyBlZmZlY3RpdmVseSBzcGFyc2UgYXR0ZW50aW9uIG92ZXIgc2FtcGxpbmcgZ3JpZC4iLCJEQ052MzogZ3JvdXBlZCBvZmZzZXRzOyBzaGFyZWQgb2Zmc2V0IHBlciBncm91cCBvZiBjaGFubmVsczsgdXNlZCBpbiBJbnRlcm5JbWFnZS4iLCJaZXJvLWluaXQgb2Zmc2V0czogZGVmb3JtYWJsZSBjb252IGRlZ3JhZGVzIHRvIHN0YW5kYXJkIGNvbnYgYXQgaW5pdGlhbGl6YXRpb24uIiwiUHJhY3RpY2FsIGdhaW46ICsyLTQgQVAgb24gQ09DTyBieSByZXBsYWNpbmcgc3RhbmRhcmQgM8OXMyBpbiBSZXNOZXQgc3RhZ2VzIDMtNC4iLCJ0b3JjaHZpc2lvbi5vcHMuRGVmb3JtQ29udjJkOiB0YWtlcyAoeCwgb2Zmc2V0KSBvciAoeCwgb2Zmc2V0LCBtYXNrKSBmb3IgRENOdjIuIl19XQ=="
---
# Deformable Convolutions — Learned Geometric Offsets

Standard convolutions apply a fixed k×k grid of kernel weights to each spatial location — the sampling pattern never adapts to the content of the image. Deformable Convolutions (Dai et al., ICCV 2017) break this constraint by learning 2D spatial offsets Δpₙ for each of the k² kernel positions. The convolution then samples at perturbed locations x + pₙ + Δpₙ using bilinear interpolation for fractional coordinates. The offsets are learned by an additional lightweight convolutional branch, making the operation end-to-end differentiable. Deformable convolutions dramatically improve detection and segmentation of objects with arbitrary shapes and sizes.

## Limitations of Standard Convolutions

A k×k convolution samples k² fixed relative positions: pₙ ∈ {(-1,-1), (-1,0), ..., (1,1)} for k=3. These positions are fixed regardless of the input — the same grid is applied to a thin vertical line, a large circle, and a diagonal edge. This fixed receptive field is poorly suited to objects that vary in scale, aspect ratio, and orientation. Pooling and large strides provide some scale invariance, but they cannot adapt the sampling geometry to match object shape. Augmentation (random rotation, scaling) helps training but does not give the network the ability to dynamically adjust its feature extraction pattern at inference.

## Deformable Convolution v1

DCNv1 adds a parallel offset-generating conv branch that takes the input feature map and outputs 2×k² channels — two channels (Δx, Δy) for each of the k² kernel positions. These offsets are added to the standard grid positions, and the feature map is sampled at the resulting fractional locations using bilinear interpolation: y(p) = Σₙ w(pₙ) · x(p + pₙ + Δpₙ). The bilinear interpolation makes the operation differentiable with respect to Δpₙ, allowing gradients to flow through the sampling locations during backpropagation. The offset conv branch is initialized with zero weights so that deformable conv starts as standard conv at the beginning of training.

## Deformable Convolution v2 — Modulation Scalars

DCNv2 (Zhu et al., CVPR 2019) extends DCNv1 by additionally learning a modulation scalar mₙ ∈ (0, 1) for each of the k² sampling positions. The modulated sampling becomes: y(p) = Σₙ w(pₙ) · mₙ · x(p + pₙ + Δpₙ). The modulation scalars act as attention weights over the sampling positions — the network can effectively zero out irrelevant sampling locations while amplifying important ones. The combined offset+modulation branch outputs 3×k² channels: 2×k² for (Δx, Δy) offsets and k² for mₙ scalars (passed through Sigmoid to keep in (0,1)). DCNv2 significantly outperforms DCNv1 on detection because it can ignore background samples that fall outside the object boundary.

> **DCNv2 = Deformable + Amplitude Modulation**: DCNv2 combines spatial deformation (where to sample) with amplitude modulation (how much to weight each sample). This gives it two degrees of freedom versus standard conv (fixed location, fixed weight) and DCNv1 (free location, fixed unit weight). The modulation effectively makes the sampling pattern sparse and object-adaptive: for a car, the network learns to sample wheel and window positions with high weight and background with near-zero weight.

## Code Examples

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class OffsetGenerator(nn.Module):
    """Learn per-position 2D offsets for a k x k deformable conv kernel."""
    def __init__(self, in_ch, kernel_size=3):
        super().__init__()
        self.k = kernel_size
        n_offsets = 2 * kernel_size * kernel_size  # (dx, dy) per position
        self.offset_conv = nn.Conv2d(in_ch, n_offsets, kernel_size=3, padding=1)
        # Zero-init: deformable conv starts as standard conv
        nn.init.zeros_(self.offset_conv.weight)
        nn.init.zeros_(self.offset_conv.bias)

    def forward(self, x):
        offsets = self.offset_conv(x)   # (B, 2*k^2, H, W)
        return offsets

# Demonstrate offset shapes
gen = OffsetGenerator(in_ch=64, kernel_size=3)
x = torch.randn(2, 64, 28, 28)
offsets = gen(x)
print(f"Input feature map: {x.shape}")
print(f"Offsets shape:     {offsets.shape}  (2 * 3*3 = 18 channels)")
print(f"Interpretation:    offset[b, 2n,   h, w] = delta_x for position n at (h,w)")
print(f"                   offset[b, 2n+1, h, w] = delta_y for position n at (h,w)")
print(f"Zero-init means: at start of training, all offsets=0 -> standard conv")
print(f"Params in offset branch: {sum(p.numel() for p in gen.parameters()):,}")
```

```python
import torch
import torch.nn as nn
from torchvision.ops import DeformConv2d

class DCNv2(nn.Module):
    """Deformable Conv v2: offsets + modulation scalars via torchvision."""
    def __init__(self, in_ch, out_ch, kernel_size=3, stride=1, padding=1):
        super().__init__()
        k2 = kernel_size * kernel_size
        # Branch: predict 2*k^2 offsets + k^2 modulation scalars
        self.offset_mask = nn.Conv2d(in_ch, 3 * k2, 3, stride=1, padding=1)
        self.dcn = DeformConv2d(in_ch, out_ch, kernel_size, stride=stride, padding=padding)
        nn.init.zeros_(self.offset_mask.weight)
        nn.init.zeros_(self.offset_mask.bias)

    def forward(self, x):
        om = self.offset_mask(x)          # (B, 3*k^2, H, W)
        k2 = om.shape[1] // 3
        offset = om[:, :2*k2]             # spatial offsets (dx, dy) per position
        mask   = torch.sigmoid(om[:, 2*k2:])  # modulation in (0, 1)
        return self.dcn(x, offset, mask)

dcn = DCNv2(64, 128, kernel_size=3, padding=1)
x = torch.randn(2, 64, 28, 28)
out = dcn(x)
print(f"Input:  {x.shape}")
print(f"Output: {out.shape}")
print(f"Offset+mask conv params: {sum(p.numel() for p in dcn.offset_mask.parameters()):,}")
print(f"DCN kernel params:       {sum(p.numel() for p in dcn.dcn.parameters()):,}")
print("mask=sigmoid(logit) in (0,1) -> attends to relevant sampling positions")
```

```python
import torch
import torch.nn as nn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def visualize_offsets(offsets, kernel_size=3, loc=(14, 14), save_path='deform_offsets.png'):
    """Visualize where a deformable conv samples vs standard conv at a given location."""
    k = kernel_size
    r = k // 2
    # Standard grid positions relative to center
    gy, gx = np.meshgrid(range(-r, r+1), range(-r, r+1), indexing='ij')
    base_y, base_x = gy.ravel(), gx.ravel()

    # Learned offsets at the query location
    k2 = k * k
    dy = offsets[0, :k2,  loc[0], loc[1]].detach().numpy()
    dx = offsets[0, k2:, loc[0], loc[1]].detach().numpy()

    sample_y = loc[0] + base_y + dy
    sample_x = loc[1] + base_x + dx

    plt.figure(figsize=(5, 5))
    plt.scatter(loc[1] + base_x, loc[0] + base_y, c='blue', s=100,
                label='Standard conv', marker='s', zorder=3)
    plt.scatter(sample_x, sample_y, c='red', s=100,
                label='Deformable conv', marker='o', zorder=3)
    for bx, by, sx, sy in zip(loc[1]+base_x, loc[0]+base_y, sample_x, sample_y):
        plt.arrow(bx, by, sx-bx, sy-by, color='gray', head_width=0.3, alpha=0.5)
    plt.legend()
    plt.title('Sampling locations: standard (blue) vs deformable (red)')
    plt.savefig(save_path, dpi=100, bbox_inches='tight')
    plt.close()
    print(f'Saved {save_path}')

# Simulate trained offsets (non-zero = deformation from standard grid)
offsets = torch.randn(1, 18, 28, 28) * 2.5
visualize_offsets(offsets, kernel_size=3, loc=(14, 14))
```

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.ops import DeformConv2d

class StdConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.conv = nn.Conv2d(in_ch, out_ch, 3, padding=1)
    def forward(self, x):
        return F.relu(self.conv(x))

class DeformConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.offset = nn.Conv2d(in_ch, 18, 3, padding=1)  # 2*3*3=18
        self.dcn    = DeformConv2d(in_ch, out_ch, 3, padding=1)
        nn.init.zeros_(self.offset.weight)
        nn.init.zeros_(self.offset.bias)
    def forward(self, x):
        return F.relu(self.dcn(x, self.offset(x)))

# Test on rotated feature map: does deformable conv adapt better?
torch.manual_seed(0)
x = torch.randn(1, 3, 32, 32)
x_rot = torch.rot90(x, k=1, dims=[2, 3])

std   = StdConvBlock(3, 64)
deform = DeformConvBlock(3, 64)

with torch.no_grad():
    diff_std   = (std(x) - std(x_rot)).abs().mean().item()
    diff_deform = (deform(x) - deform(x_rot)).abs().mean().item()

print(f"Standard conv response diff (90-deg rotation): {diff_std:.4f}")
print(f"Deformable conv response diff:                  {diff_deform:.4f}")
print("After training, deformable conv learns offsets that compensate for rotation")
print("and other geometric transforms (scale, shear) without explicit augmentation")
```

## DCNv3 and Efficiency Improvements

DCNv3 (InternImage, CVPR 2023) introduces grouped deformable convolution: instead of learning one set of offsets and modulations for all channels, it uses G groups each with their own offsets and modulations, similar to grouped convolution or multi-head attention. The output is the sum across groups. DCNv3 also separates the spatial aggregation (deformable sampling) from the channel projection, reducing parameter count. InternImage-H with DCNv3 achieves 89.6% on ImageNet and 65.4 box AP on COCO, setting new state-of-the-art for CNN-based architectures at the time of publication.

## Applications in Object Detection

Deformable convolutions are particularly powerful in detection backbones because objects vary in scale and aspect ratio. Replacing standard 3×3 convs in ResNet stage 3 and 4 with DCNv2 consistently adds +2–4% AP on COCO without any other change. Mask R-CNN with DCNv2 improves both box AP and mask AP. The offset patterns learned by detection networks are interpretable: for a car, offsets cluster around wheel positions; for a person, they cluster around joints and torso. This geometric adaptivity replaces the need for explicit multi-scale feature aggregation in some designs.

## Convolution Variant Comparison

| Variant | Sampling Pattern | Extra Params (k=3) | Bilinear Interp | Geometric Flexibility | Best Use Case |
| --- | --- | --- | --- | --- | --- |
| Standard Conv | Fixed 3×3 grid | None | No | None — rigid | General feature extraction |
| Deformable Conv v1 | Learned offsets Δpₙ per position | 2×k² per layer | Yes | High — free offsets | Shape-adaptive detection |
| Deformable Conv v2 | Offsets + modulation mₙ ∈ (0,1) | 3×k² per layer | Yes | High + amplitude control | Detection, segmentation |
| Deformable Conv v3 | Grouped offsets + modulation | 3×k²/G per group | Yes | High + channel grouping | Efficient large-scale backbone |

## Implementation Notes

When using deformable convolutions in practice, keep these points in mind: (1) Zero-initialize the offset branch weights and biases so training starts from a standard conv and deformations are learned gradually; (2) Clip offsets to a reasonable range (typically ±(k-1)) to prevent sampling outside the feature map — torchvision's DeformConv2d handles border padding automatically; (3) Use DCNv2 (with modulation) over DCNv1 in all detection scenarios — the modulation provides meaningful accuracy gains with minimal overhead; (4) Place deformable convolutions in the deeper stages (stage 3, 4 in ResNet) where semantic features benefit most from shape adaptation; (5) Learning rate for the offset branch may need tuning — starting with a lower LR for offsets (0.1× backbone LR) can improve stability.

- DCNv1: offset Δpₙ per kernel position; bilinear interpolation at p + pₙ + Δpₙ.
- DCNv2: offset + modulation mₙ ∈ (0,1); effectively sparse attention over sampling grid.
- DCNv3: grouped offsets; shared offset per group of channels; used in InternImage.
- Zero-init offsets: deformable conv degrades to standard conv at initialization.
- Practical gain: +2-4 AP on COCO by replacing standard 3×3 in ResNet stages 3-4.
- torchvision.ops.DeformConv2d: takes (x, offset) or (x, offset, mask) for DCNv2.

