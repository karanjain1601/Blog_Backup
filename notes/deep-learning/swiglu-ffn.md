---
title: "SwiGLU — Gated Linear Units and LLaMA FFN"
slug: "swiglu-ffn"
description: "SwiGLU and the GLU family of gated FFN activations — how SiLU gates improve Transformer FFN quality, parameter equivalence with the 3-matrix design, and full LLaMA block integration."
tags: ["deep-learning", "transformers"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGZlZWQtZm9yd2FyZCBzdWItbGF5ZXIgaGFzIGJlZW4gYSBxdWlldCBzb3VyY2Ugb2YgY29uc2lzdGVudCBpbXByb3ZlbWVudCBpbiBUcmFuc2Zvcm1lciBkZXNpZ24uIE5vYW0gU2hhemVlclx1MDAyN3MgMjAyMCBwYXBlciBcdTAwMjdHTFUgVmFyaWFudHMgSW1wcm92ZSBUcmFuc2Zvcm1lcnNcdTAwMjcgaW50cm9kdWNlZCBhIGZhbWlseSBvZiBnYXRlZCBmZWVkLWZvcndhcmQgbGF5ZXJzIHdoZXJlIG9uZSBsaW5lYXIgcHJvamVjdGlvbiBhY3RzIGFzIGEgbXVsdGlwbGljYXRpdmUgZ2F0ZSBvbiBhbm90aGVyLiBTd2lHTFUg4oCUIHRoZSB2YXJpYW50IHVzaW5nIHRoZSBTaUxVIChTd2lzaCkgYWN0aXZhdGlvbiBhcyB0aGUgZ2F0ZSDigJQgaGFzIGJlY29tZSB0aGUgc3RhbmRhcmQgRkZOIGluIG1vc3QgZnJvbnRpZXIgTExNcywgaW5jbHVkaW5nIExMYU1BIDEvMi8zLCBNaXN0cmFsLCBQYUxNLCBhbmQgR2VtbWEuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR2F0ZWQgTGluZWFyIFVuaXRzIOKAlCBUaGUgR0xVIEZhbWlseSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBHYXRlZCBMaW5lYXIgVW5pdCAoR0xVKSwgaW50cm9kdWNlZCBieSBEYXVwaGluIGV0IGFsLiAoMjAxNyksIHNwbGl0cyBhIGxpbmVhciBwcm9qZWN0aW9uIGludG8gdHdvIGhhbHZlcyBhbmQgbXVsdGlwbGllcyB0aGVtIGVsZW1lbnQtd2lzZTogR0xVKHgsIFcsIFYsIGIsIGMpID0gz4MoeFcgKyBiKSDiipkgKHhWICsgYykuIFRoZSBzaWdtb2lkLWdhdGVkIGJyYW5jaCBhY3RzIGFzIGFuIGluZm9ybWF0aW9uIGdhdGUg4oCUIGl0IGNvbnRyb2xzIGhvdyBtdWNoIG9mIHRoZSB2YWx1ZSBicmFuY2ggcGFzc2VzIHRocm91Z2ggdG8gdGhlIG5leHQgbGF5ZXIuIFNoYXplZXIgKDIwMjApIGV4cGxvcmVkIHJlcGxhY2luZyB0aGUgc2lnbW9pZCBnYXRlIHdpdGggb3RoZXIgbm9uLWxpbmVhcml0aWVzLCBmaW5kaW5nIHRoYXQgc21vb3RoIGFjdGl2YXRpb25zIChHRUxVLCBTaUxVKSBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybWVkIGJvdGggR0xVIGFuZCBSZUxVLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiR0xVIChEYXVwaGluIDIwMTcpOiDPgyh4Vykg4oqZIHhWIOKAlCBzaWdtb2lkIGdhdGUsIHNwbGl0cyBwcm9qZWN0aW9uIGluIHR3byIsIlJlR0xVIChTaGF6ZWVyIDIwMjApOiBSZUxVKHhXKSDiipkgeFYg4oCUIFJlTFUgZ2F0ZSwgY29tcGV0aXRpdmUgd2l0aCBHRUxVIiwiR0VHTFUgKFNoYXplZXIgMjAyMCk6IEdFTFUoeFcpIOKKmSB4ViDigJQgc3Ryb25nIGFjcm9zcyBiZW5jaG1hcmtzIiwiU3dpR0xVIChTaGF6ZWVyIDIwMjApOiBTaUxVKHhXKSDiipkgeFYg4oCUIGJlc3QgcmVwb3J0ZWQ7IFNpTFUgPSB4wrfPgyh4KSIsIkFsbCBnYXRlZCB2YXJpYW50cyB1c2UgYSB0aGlyZCBkb3duLXByb2plY3Rpb24gbWF0cml4IFczIHRvIHJldHVybiB0byBkX21vZGVsIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IEdhdGluZyBJbXByb3ZlcyBRdWFsaXR5IiwiY29udGVudCI6IlRoZSBnYXRlIHByb3ZpZGVzIGR5bmFtaWMgZmVhdHVyZSBzZWxlY3Rpb246IGl0IGFsbG93cyB0aGUgbmV0d29yayB0byBzdXBwcmVzcyBpcnJlbGV2YW50IGRpbWVuc2lvbnMgdG9rZW4tYnktdG9rZW4sIHNpbWlsYXIgdG8gTFNUTSBmb3JnZXQgZ2F0ZXMuIFNpTFUgaXMgc21vb3RoLCBub24tc2F0dXJhdGluZyBmb3IgcG9zaXRpdmUgdmFsdWVzLCBhbmQgaGFzIGEgc21hbGwgbmVnYXRpdmUgcmVnaW9uIOKAlCB0aGVzZSBwcm9wZXJ0aWVzIGNvbWJpbmUgdG8gZ2l2ZSByaWNoZXIgZ3JhZGllbnRzIHRoYW4gUmVMVSBhbmQgbG93ZXIgdmFyaWFuY2UgdGhhbiBzaWdtb2lkIGdhdGVzLiBFbXBpcmljYWxseSBHRUdMVSBhbmQgU3dpR0xVIGltcHJvdmUgcGVycGxleGl0eSBieSAxLTMlIGF0IHRoZSBzYW1lIEZMT1BzIGJ1ZGdldC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTd2lHTFUg4oCUIFNpTFUgR2F0ZSB3aXRoIFBhcmFtZXRlciBBZGp1c3RtZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTd2lHTFUgaXMgZGVmaW5lZCBhcyBGRk5fU3dpR0xVKHgpID0gKFNpTFUoeFfigoEpIOKKmSB4V+KCgikgV+KCgyB3aGVyZSBTaUxVKHgpID0geCDCtyDPgyh4KS4gVGhyZWUgd2VpZ2h0IG1hdHJpY2VzIHJlcGxhY2UgdGhlIHN0YW5kYXJkIHR3bywgc28gdGhlIGhpZGRlbiBkaW1lbnNpb24gbXVzdCBiZSByZWR1Y2VkIHRvIHByZXNlcnZlIHRoZSBwYXJhbWV0ZXIgYnVkZ2V0OiBpbnN0ZWFkIG9mIGRfZmYgPSA0wrdkX21vZGVsIHdpdGggdHdvIG1hdHJpY2VzICgywrdkwrdkX2ZmID0gOGTCsiksIFN3aUdMVSB1c2VzIGRfZmYgPSA4ZC8zIHdpdGggdGhyZWUgbWF0cmljZXMgKDPCt2TCtyg4ZC8zKSA9IDhkwrIpLiBMTGFNQSByb3VuZHMgOC8zIHRvIHRoZSBuZWFyZXN0IG11bHRpcGxlIG9mIDI1NiBmb3IgaGFyZHdhcmUgZWZmaWNpZW5jeSwgdHlwaWNhbGx5IGRfZmYg4omIIDExLDAwOCBmb3IgZF9tb2RlbCA9IDQsMDk2LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBHYXRlcyBJbXByb3ZlIEZGTiBRdWFsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBGRk4gYWN0aXZhdGlvbnMgKFJlTFUsIEdFTFUpIGFwcGx5IGEgZml4ZWQgbm9uLWxpbmVhcml0eSB0byBldmVyeSBuZXVyb24gaW5kZXBlbmRlbnRseSBvZiB0aGUgaW5wdXQgdmFsdWUuIEdhdGVkIHZhcmlhbnRzIG1ha2UgdGhlIGVmZmVjdGl2ZSBhY3RpdmF0aW9uICppbnB1dC1kZXBlbmRlbnQqOiBTaUxVKHhX4oKBKSDiipkgeFfigoIgbWVhbnMgZGlmZmVyZW50IHRva2VucyBhY3RpdmF0ZSBkaWZmZXJlbnQgc3Vic2V0cyBvZiBmZWF0dXJlcy4gVGhpcyBkeW5hbWljIHNlbGVjdGlvbiBhbGxvd3MgdGhlIEZGTiB0byBzcGVjaWFsaXNlIGRpZmZlcmVudCBuZXVyb25zIGZvciBkaWZmZXJlbnQgaW5wdXQgcGF0dGVybnMsIGluY3JlYXNpbmcgZXhwcmVzc2l2aXR5IHdpdGhvdXQgaW5jcmVhc2luZyBGTE9Qcy4gVGhlIGdhdGUgYWxzbyBwcm92aWRlcyBhIG5hdHVyYWwgbWVjaGFuaXNtIGZvciB0aGUgbW9kZWwgdG8gcm91dGUgaW5mb3JtYXRpb24g4oCUIGZlYXR1cmVzIHdpdGggbG93IGdhdGUgYWN0aXZhdGlvbiBhcmUgZWZmZWN0aXZlbHkgemVyb2VkIG91dC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIFN3aUdMVSBGRk4gZnJvbSBTY3JhdGNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGNsZWFuIFN3aUdMVSBpbXBsZW1lbnRhdGlvbiB3aXRoIHRoZSA4LzMgaGlkZGVuIGRpbWVuc2lvbiBzY2FsaW5nLiBDb25maXJtcyBvdXRwdXQgc2hhcGUgYW5kIHBhcmFtZXRlciBjb3VudCByZWxhdGl2ZSB0byBhIHN0YW5kYXJkIDItbWF0cml4IEZGTi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgU3dpR0xVKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU3dpR0xVIGZyb20gXHUwMDI3R0xVIFZhcmlhbnRzIEltcHJvdmUgVHJhbnNmb3JtZXJzXHUwMDI3IChTaGF6ZWVyLCAyMDIwKS5cbiAgICBGRk4oeCkgPSAoU2lMVSh4IEAgV19nYXRlKSAqICh4IEAgV191cCkpIEAgV19kb3duXG4gICAgSGlkZGVuIGRpbSA9IDgvMyAqIGRfbW9kZWwgdG8ga2VlcCBwYXJhbSBjb3VudCBlcXVhbCB0byAyLW1hdHJpeCBGRk4uXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgZmFjdG9yOiBmbG9hdCA9IDgvMyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBkX2hpZGRlbiAgICAgICA9IGludChkX21vZGVsICogZmFjdG9yKVxuICAgICAgICBzZWxmLmdhdGVfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBkX2hpZGRlbiwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi51cF9wcm9qICAgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9oaWRkZW4sIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuZG93bl9wcm9qID0gbm4uTGluZWFyKGRfaGlkZGVuLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgZ2F0ZSA9IEYuc2lsdShzZWxmLmdhdGVfcHJvaih4KSkgICAjIFNpTFUoeFdfZ2F0ZSlcbiAgICAgICAgdXAgICA9IHNlbGYudXBfcHJvaih4KSAgICAgICAgICAgICAjIHhXX3VwIChubyBhY3RpdmF0aW9uKVxuICAgICAgICByZXR1cm4gc2VsZi5kb3duX3Byb2ooZ2F0ZSAqIHVwKSAgICMgKGdhdGUg4oqZIHVwKSBAIFdfZG93blxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuZF9tb2RlbCA9IDUxMlxuZmZuICAgICA9IFN3aUdMVShkX21vZGVsKVxueCAgICAgICA9IHRvcmNoLnJhbmRuKDIsIDEwLCBkX21vZGVsKVxub3V0ICAgICA9IGZmbih4KVxucF9zd2kgICA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gZmZuLnBhcmFtZXRlcnMoKSlcbnBfc3RkICAgPSAyICogZF9tb2RlbCAqICg0ICogZF9tb2RlbCkgICAgIyBzdGFuZGFyZCAyLW1hdHJpeCBwYXJhbSBjb3VudFxucHJpbnQoZlx1MDAyN1N3aUdMVSBvdXRwdXQ6IHtvdXQuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1N3aUdMVSBwYXJhbXM6IHtwX3N3aTosfVx1MDAyNylcbnByaW50KGZcdTAwMjdTdGFuZGFyZCBwYXJhbXMgKGRfZmY9NGQpOiB7cF9zdGQ6LH1cdTAwMjcpXG5wcmludChmXHUwMDI3UmF0aW86IHtwX3N3aS9wX3N0ZDouNGZ9ICAoc2hvdWxkIGJlIH4xLjAg4oCUIHBhcmFtLWVxdWl2YWxlbnQpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMiDigJQgR0xVIFZhcmlhbnRzIFNpZGUgYnkgU2lkZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSB1bmlmaWVkIGltcGxlbWVudGF0aW9uIG9mIHRoZSBHTFUgZmFtaWx5IHVzaW5nIGEgc3BsaXQtcHJvamVjdGlvbiBhcHByb2FjaCwgbWFraW5nIGl0IGVhc3kgdG8gc3dhcCBnYXRlIGFjdGl2YXRpb25zIGFuZCBjb21wYXJlIG91dHB1dHMgb24gdGhlIHNhbWUgaW5wdXQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEdhdGVkRkZOKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiVW5pZmllZCBHTFUtZmFtaWx5IEZGTjogZ2F0ZSBhY3RpdmF0aW9uIGlzIGNvbmZpZ3VyYWJsZS5cIlwiXCJcbiAgICBHQVRFUyA9IHtcbiAgICAgICAgXHUwMDI3Z2x1XHUwMDI3OiAgICB0b3JjaC5zaWdtb2lkLFxuICAgICAgICBcdTAwMjdyZWdsdVx1MDAyNzogIEYucmVsdSxcbiAgICAgICAgXHUwMDI3Z2VnbHVcdTAwMjc6ICBGLmdlbHUsXG4gICAgICAgIFx1MDAyN3N3aWdsdVx1MDAyNzogRi5zaWx1LFxuICAgIH1cblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsOiBpbnQsIGRfZmY6IGludCwgdmFyaWFudDogc3RyID0gXHUwMDI3c3dpZ2x1XHUwMDI3KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGlmIHZhcmlhbnQgbm90IGluIHNlbGYuR0FURVM6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcdTAwMjdVbmtub3duIHZhcmlhbnQ6IHt2YXJpYW50fS4gQ2hvb3NlOiB7bGlzdChzZWxmLkdBVEVTKX1cdTAwMjcpXG4gICAgICAgIHNlbGYudmFyaWFudCA9IHZhcmlhbnRcbiAgICAgICAgc2VsZi5nYXRlX2ZuICA9IHNlbGYuR0FURVNbdmFyaWFudF1cbiAgICAgICAgc2VsZi51cCAgID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfZmYgKiAyLCBiaWFzPUZhbHNlKSAgIyBnYXRlICsgdmFsdWVcbiAgICAgICAgc2VsZi5kb3duID0gbm4uTGluZWFyKGRfZmYsICAgZF9tb2RlbCwgICBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgZ2F0ZSwgdmFsdWUgPSBzZWxmLnVwKHgpLmNodW5rKDIsIGRpbT0tMSlcbiAgICAgICAgcmV0dXJuIHNlbGYuZG93bihzZWxmLmdhdGVfZm4oZ2F0ZSkgKiB2YWx1ZSlcblxuIyBDb21wYXJlIGFsbCB2YXJpYW50cyBvbiBpZGVudGljYWwgd2VpZ2h0cyBhbmQgaW5wdXRcbmRfbW9kZWwsIGRfZmYgPSAyNTYsIDUxMlxueCA9IHRvcmNoLnJhbmRuKDIsIDgsIGRfbW9kZWwpXG5mb3IgdmFyaWFudCBpbiAoXHUwMDI3Z2x1XHUwMDI3LCBcdTAwMjdyZWdsdVx1MDAyNywgXHUwMDI3Z2VnbHVcdTAwMjcsIFx1MDAyN3N3aWdsdVx1MDAyNyk6XG4gICAgdG9yY2gubWFudWFsX3NlZWQoMClcbiAgICBmZm4gICAgPSBHYXRlZEZGTihkX21vZGVsLCBkX2ZmLCB2YXJpYW50KVxuICAgIG91dCAgICA9IGZmbih4KVxuICAgIHBhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gZmZuLnBhcmFtZXRlcnMoKSlcbiAgICBwcmludChmXHUwMDI3e3ZhcmlhbnQudXBwZXIoKTo4fTogb3V0PXt0dXBsZShvdXQuc2hhcGUpfSwgcGFyYW1zPXtwYXJhbXM6LH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAzIOKAlCBQYXJhbWV0ZXIgRXF1aXZhbGVuY2UgVmVyaWZpY2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcm92aW5nIHRoYXQgYSBTd2lHTFUgRkZOIHdpdGggZF9mZiA9IDJkLzMgw5cgb3JpZ2luYWwgaGFzIHRoZSBzYW1lIHBhcmFtZXRlciBjb3VudCBhcyBhIHN0YW5kYXJkIDItbWF0cml4IEZGTiB3aXRoIGRfZmYgPSA0IMOXIGRfbW9kZWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFN0YW5kYXJkRkZOKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiVHdvLW1hdHJpeCBGRk46IDIgKiBkX21vZGVsICogZF9mZiBwYXJhbWV0ZXJzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkLCBkX2ZmKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZmMxID0gbm4uTGluZWFyKGQsIGRfZmYsICBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmZjMiA9IG5uLkxpbmVhcihkX2ZmLCBkLCAgYmlhcz1GYWxzZSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYuZmMyKEYuZ2VsdShzZWxmLmZjMSh4KSkpXG5cbmNsYXNzIFN3aUdMVUZGTihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlRocmVlLW1hdHJpeCBTd2lHTFU6IDMgKiBkX21vZGVsICogZF9oaWRkZW4gcGFyYW1ldGVycy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCwgZF9oaWRkZW4pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5XMSA9IG5uLkxpbmVhcihkLCBkX2hpZGRlbiwgICBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLlcyID0gbm4uTGluZWFyKGQsIGRfaGlkZGVuLCAgIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuVzMgPSBubi5MaW5lYXIoZF9oaWRkZW4sIGQsICAgYmlhcz1GYWxzZSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYuVzMoRi5zaWx1KHNlbGYuVzEoeCkpICogc2VsZi5XMih4KSlcblxuZF9tb2RlbCAgID0gNTEyXG5kX3N0ZF9mZiAgPSA0ICogZF9tb2RlbCAgICAgICAgICAjIHN0YW5kYXJkIGRfZmYgPSAyMDQ4XG5kX3N3aV9mZiAgPSBpbnQoZF9zdGRfZmYgKiAyLzMpICAjIFN3aUdMVSBkX2ZmID0gMTM2NVxuXG5zdGQgPSBTdGFuZGFyZEZGTihkX21vZGVsLCBkX3N0ZF9mZilcbnN3aSA9IFN3aUdMVUZGTihkX21vZGVsLCBkX3N3aV9mZilcbnBfc3RkID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBzdGQucGFyYW1ldGVycygpKVxucF9zd2kgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIHN3aS5wYXJhbWV0ZXJzKCkpXG5cbnByaW50KGZcdTAwMjdTdGFuZGFyZCBGRk4gICgyIG1hdHMsIGRfZmY9e2Rfc3RkX2ZmfSk6IHtwX3N0ZDosfSBwYXJhbXNcdTAwMjcpXG5wcmludChmXHUwMDI3U3dpR0xVIEZGTiAgICAoMyBtYXRzLCBkX2ZmPXtkX3N3aV9mZn0pOiB7cF9zd2k6LH0gcGFyYW1zXHUwMDI3KVxucHJpbnQoZlx1MDAyN1JhdGlvOiB7cF9zd2kvcF9zdGQ6LjRmfSAgKGNsb3NlIHRvIDEuMDAwIOKAlCBwYXJhbWV0ZXItZXF1aXZhbGVudClcdTAwMjcpXG5wcmludChmXHUwMDI3Rm9ybXVsYSBjaGVjayDigJQgMyBtYXRzOiAzKntkX21vZGVsfSp7ZF9zd2lfZmZ9ID0gezMqZF9tb2RlbCpkX3N3aV9mZjosfVx1MDAyNylcbnByaW50KGZcdTAwMjdGb3JtdWxhIGNoZWNrIOKAlCAyIG1hdHM6IDIqe2RfbW9kZWx9KntkX3N0ZF9mZn0gPSB7MipkX21vZGVsKmRfc3RkX2ZmOix9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgNCDigJQgU3dpR0xVIGluIGEgRnVsbCBMTGFNQS1TdHlsZSBCbG9jayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBjb21wbGV0ZSBMTGFNQS1zdHlsZSBkZWNvZGVyIGJsb2NrIHVzaW5nIFJNU05vcm0gKGluc3RlYWQgb2YgTGF5ZXJOb3JtKSwgU3dpR0xVIEZGTiwgYW5kIHByZS1ub3JtIGxheW91dCDigJQgdGhlIGJ1aWxkaW5nIGJsb2NrIHVzZWQgaW4gTExhTUEgMS8yLzMgYW5kIE1pc3RyYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFJNU05vcm0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJSb290IE1lYW4gU3F1YXJlIExheWVyIE5vcm1hbGlzYXRpb24gKExMYU1BLCBNaXN0cmFsKS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZDogaW50LCBlcHM6IGZsb2F0ID0gMWUtNik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLndlaWdodCA9IG5uLlBhcmFtZXRlcih0b3JjaC5vbmVzKGQpKVxuICAgICAgICBzZWxmLmVwcyAgICA9IGVwc1xuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIHJtcyA9IHgucG93KDIpLm1lYW4oLTEsIGtlZXBkaW09VHJ1ZSkuYWRkKHNlbGYuZXBzKS5zcXJ0KClcbiAgICAgICAgcmV0dXJuIHNlbGYud2VpZ2h0ICogeCAvIHJtc1xuXG5jbGFzcyBTd2lHTFVGRk4obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZDogaW50LCBkX2ZmOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5nYXRlID0gbm4uTGluZWFyKGQsIGRfZmYsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYudXAgICA9IG5uLkxpbmVhcihkLCBkX2ZmLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmRvd24gPSBubi5MaW5lYXIoZF9mZiwgZCwgYmlhcz1GYWxzZSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYuZG93bihGLnNpbHUoc2VsZi5nYXRlKHgpKSAqIHNlbGYudXAoeCkpXG5cbmNsYXNzIExMYU1BQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJMTGFNQS1zdHlsZSBibG9jazogUk1TTm9ybSArIE1IQSArIFN3aUdMVSwgcHJlLW5vcm0gbGF5b3V0LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsOiBpbnQgPSAyNTYsIG5faGVhZHM6IGludCA9IDgsIGRfZmY6IGludCA9IE5vbmUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgZF9mZiAgICAgICAgICAgPSBkX2ZmIG9yIGludChkX21vZGVsICogOCAvIDMpXG4gICAgICAgIHNlbGYuYXR0bl9ub3JtID0gUk1TTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmZmbl9ub3JtICA9IFJNU05vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5hdHRuID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsIGJhdGNoX2ZpcnN0PVRydWUsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuZmZuICA9IFN3aUdMVUZGTihkX21vZGVsLCBkX2ZmKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgbiA9IHNlbGYuYXR0bl9ub3JtKHgpXG4gICAgICAgIHggPSB4ICsgc2VsZi5hdHRuKG4sIG4sIG4pWzBdICAgICAgIyBwcmUtbm9ybSBhdHRlbnRpb25cbiAgICAgICAgeCA9IHggKyBzZWxmLmZmbihzZWxmLmZmbl9ub3JtKHgpKSAjIHByZS1ub3JtIFN3aUdMVSBGRk5cbiAgICAgICAgcmV0dXJuIHhcblxuYmxvY2sgID0gTExhTUFCbG9jayhkX21vZGVsPTI1Niwgbl9oZWFkcz04KVxueCAgICAgID0gdG9yY2gucmFuZG4oMiwgMTYsIDI1Nilcbm91dCAgICA9IGJsb2NrKHgpXG5wYXJhbXMgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIGJsb2NrLnBhcmFtZXRlcnMoKSlcbnByaW50KGZcdTAwMjdMTGFNQSBibG9jayBvdXRwdXQ6IHtvdXQuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1BhcmFtZXRlcnM6IHtwYXJhbXM6LH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRkZOIEFjdGl2YXRpb24gVmFyaWFudHMgQ29tcGFyZWQifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmFyaWFudCIsIkdhdGUgQWN0aXZhdGlvbiIsIkZvcm11bGEgKHNpbXBsaWZpZWQpIiwiVXNlZCBJbiIsIlF1YWxpdHkgUmFuayJdLCJyb3dzIjpbWyJTdGFuZGFyZCBSZUxVIiwiTm9uZSIsIlJlTFUoeFcxKSBAIFcyIiwiT3JpZ2luYWwgVHJhbnNmb3JtZXIsIEJFUlQiLCJCYXNlbGluZSJdLFsiU3RhbmRhcmQgR0VMVSIsIk5vbmUiLCJHRUxVKHhXMSkgQCBXMiIsIkdQVC0yLCBSb0JFUlRhLCBEaXN0aWxCRVJUIiwiQmV0dGVyIHRoYW4gUmVMVSJdLFsiR0xVIChzaWdtb2lkKSIsIlNpZ21vaWQgz4MiLCIoz4MoeFcpIOKKmSB4VikgQCBXMiIsIkRhdXBoaW4gZXQgYWwuICgyMDE3KSwgTE0gdGFza3MiLCJNb2RlcmF0ZSBnYWluIl0sWyJSZUdMVSIsIlJlTFUiLCIoUmVMVSh4Vykg4oqZIHhWKSBAIFcyIiwiU2hhemVlciAyMDIwIGFibGF0aW9ucyIsIkNvbXBldGl0aXZlIl0sWyJHRUdMVSIsIkdFTFUiLCIoR0VMVSh4Vykg4oqZIHhWKSBAIFcyIiwiVDUgdmFyaWFudHMsIHNvbWUgQkVSVCBtb2RlbHMiLCJTdHJvbmciXSxbIlN3aUdMVSIsIlNpTFUgKFN3aXNoKSIsIihTaUxVKHhXKSDiipkgeFYpIEAgVzIiLCJMTGFNQSAxLzIvMywgTWlzdHJhbCwgUGFMTSwgR2VtbWEiLCJCZXN0IHJlcG9ydGVkIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN3aUdMVSByZXByZXNlbnRzIG9uZSBvZiB0aGUgY2xlYXJlc3Qgd2lucyBpbiBtb2Rlcm4gTExNIGRlc2lnbjogYSBvbmUtbGluZSBjaGFuZ2UgdG8gdGhlIEZGTiBhY3RpdmF0aW9uIHRoYXQgY29uc2lzdGVudGx5IGltcHJvdmVzIHBlcnBsZXhpdHkgYXQgaWRlbnRpY2FsIGNvbXB1dGUuIFRoZSAzLW1hdHJpeCBkZXNpZ24gd2l0aCB0aGUgMi8zIGhpZGRlbi1kaW1lbnNpb24gYWRqdXN0bWVudCBrZWVwcyBGTE9QIGFuZCBwYXJhbWV0ZXIgY291bnRzIGVxdWl2YWxlbnQgdG8gYSBzdGFuZGFyZCBGRk4sIHNvIHRoZXJlIGlzIG5vIGNvc3QgdG8gc3dpdGNoaW5nLiBGb3IgYW55IG5ldyBUcmFuc2Zvcm1lciBwcm9qZWN0IHVzaW5nIExMYU1BLWZhbWlseSBhcmNoaXRlY3R1cmUgYXMgYSByZWZlcmVuY2UsIFN3aUdMVSB3aXRoIFJNU05vcm0gc2hvdWxkIGJlIHRoZSBzdGFydGluZyBwb2ludCBmb3IgdGhlIEZGTiBzdWItbGF5ZXIuIn1d"
---
# SwiGLU — Gated Linear Units and LLaMA FFN

The feed-forward sub-layer has been a quiet source of consistent improvement in Transformer design. Noam Shazeer's 2020 paper 'GLU Variants Improve Transformers' introduced a family of gated feed-forward layers where one linear projection acts as a multiplicative gate on another. SwiGLU — the variant using the SiLU (Swish) activation as the gate — has become the standard FFN in most frontier LLMs, including LLaMA 1/2/3, Mistral, PaLM, and Gemma.

## Gated Linear Units — The GLU Family

A Gated Linear Unit (GLU), introduced by Dauphin et al. (2017), splits a linear projection into two halves and multiplies them element-wise: GLU(x, W, V, b, c) = σ(xW + b) ⊙ (xV + c). The sigmoid-gated branch acts as an information gate — it controls how much of the value branch passes through to the next layer. Shazeer (2020) explored replacing the sigmoid gate with other non-linearities, finding that smooth activations (GELU, SiLU) consistently outperformed both GLU and ReLU.

- GLU (Dauphin 2017): σ(xW) ⊙ xV — sigmoid gate, splits projection in two
- ReGLU (Shazeer 2020): ReLU(xW) ⊙ xV — ReLU gate, competitive with GELU
- GEGLU (Shazeer 2020): GELU(xW) ⊙ xV — strong across benchmarks
- SwiGLU (Shazeer 2020): SiLU(xW) ⊙ xV — best reported; SiLU = x·σ(x)
- All gated variants use a third down-projection matrix W3 to return to d_model

> **Why Gating Improves Quality**: The gate provides dynamic feature selection: it allows the network to suppress irrelevant dimensions token-by-token, similar to LSTM forget gates. SiLU is smooth, non-saturating for positive values, and has a small negative region — these properties combine to give richer gradients than ReLU and lower variance than sigmoid gates. Empirically GEGLU and SwiGLU improve perplexity by 1-3% at the same FLOPs budget.

## SwiGLU — SiLU Gate with Parameter Adjustment

SwiGLU is defined as FFN_SwiGLU(x) = (SiLU(xW₁) ⊙ xW₂) W₃ where SiLU(x) = x · σ(x). Three weight matrices replace the standard two, so the hidden dimension must be reduced to preserve the parameter budget: instead of d_ff = 4·d_model with two matrices (2·d·d_ff = 8d²), SwiGLU uses d_ff = 8d/3 with three matrices (3·d·(8d/3) = 8d²). LLaMA rounds 8/3 to the nearest multiple of 256 for hardware efficiency, typically d_ff ≈ 11,008 for d_model = 4,096.

## Why Gates Improve FFN Quality

Standard FFN activations (ReLU, GELU) apply a fixed non-linearity to every neuron independently of the input value. Gated variants make the effective activation *input-dependent*: SiLU(xW₁) ⊙ xW₂ means different tokens activate different subsets of features. This dynamic selection allows the FFN to specialise different neurons for different input patterns, increasing expressivity without increasing FLOPs. The gate also provides a natural mechanism for the model to route information — features with low gate activation are effectively zeroed out.

## Code 1 — SwiGLU FFN from Scratch

A clean SwiGLU implementation with the 8/3 hidden dimension scaling. Confirms output shape and parameter count relative to a standard 2-matrix FFN.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SwiGLU(nn.Module):
    """SwiGLU from 'GLU Variants Improve Transformers' (Shazeer, 2020).
    FFN(x) = (SiLU(x @ W_gate) * (x @ W_up)) @ W_down
    Hidden dim = 8/3 * d_model to keep param count equal to 2-matrix FFN.
    """
    def __init__(self, d_model: int, factor: float = 8/3):
        super().__init__()
        d_hidden       = int(d_model * factor)
        self.gate_proj = nn.Linear(d_model, d_hidden, bias=False)
        self.up_proj   = nn.Linear(d_model, d_hidden, bias=False)
        self.down_proj = nn.Linear(d_hidden, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        gate = F.silu(self.gate_proj(x))   # SiLU(xW_gate)
        up   = self.up_proj(x)             # xW_up (no activation)
        return self.down_proj(gate * up)   # (gate ⊙ up) @ W_down

torch.manual_seed(0)
d_model = 512
ffn     = SwiGLU(d_model)
x       = torch.randn(2, 10, d_model)
out     = ffn(x)
p_swi   = sum(p.numel() for p in ffn.parameters())
p_std   = 2 * d_model * (4 * d_model)    # standard 2-matrix param count
print(f'SwiGLU output: {out.shape}')
print(f'SwiGLU params: {p_swi:,}')
print(f'Standard params (d_ff=4d): {p_std:,}')
print(f'Ratio: {p_swi/p_std:.4f}  (should be ~1.0 — param-equivalent)')
```

## Code 2 — GLU Variants Side by Side

A unified implementation of the GLU family using a split-projection approach, making it easy to swap gate activations and compare outputs on the same input.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GatedFFN(nn.Module):
    """Unified GLU-family FFN: gate activation is configurable."""
    GATES = {
        'glu':    torch.sigmoid,
        'reglu':  F.relu,
        'geglu':  F.gelu,
        'swiglu': F.silu,
    }

    def __init__(self, d_model: int, d_ff: int, variant: str = 'swiglu'):
        super().__init__()
        if variant not in self.GATES:
            raise ValueError(f'Unknown variant: {variant}. Choose: {list(self.GATES)}')
        self.variant = variant
        self.gate_fn  = self.GATES[variant]
        self.up   = nn.Linear(d_model, d_ff * 2, bias=False)  # gate + value
        self.down = nn.Linear(d_ff,   d_model,   bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        gate, value = self.up(x).chunk(2, dim=-1)
        return self.down(self.gate_fn(gate) * value)

# Compare all variants on identical weights and input
d_model, d_ff = 256, 512
x = torch.randn(2, 8, d_model)
for variant in ('glu', 'reglu', 'geglu', 'swiglu'):
    torch.manual_seed(0)
    ffn    = GatedFFN(d_model, d_ff, variant)
    out    = ffn(x)
    params = sum(p.numel() for p in ffn.parameters())
    print(f'{variant.upper():8}: out={tuple(out.shape)}, params={params:,}')
```

## Code 3 — Parameter Equivalence Verification

Proving that a SwiGLU FFN with d_ff = 2d/3 × original has the same parameter count as a standard 2-matrix FFN with d_ff = 4 × d_model.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class StandardFFN(nn.Module):
    """Two-matrix FFN: 2 * d_model * d_ff parameters."""
    def __init__(self, d, d_ff):
        super().__init__()
        self.fc1 = nn.Linear(d, d_ff,  bias=False)
        self.fc2 = nn.Linear(d_ff, d,  bias=False)
    def forward(self, x): return self.fc2(F.gelu(self.fc1(x)))

class SwiGLUFFN(nn.Module):
    """Three-matrix SwiGLU: 3 * d_model * d_hidden parameters."""
    def __init__(self, d, d_hidden):
        super().__init__()
        self.W1 = nn.Linear(d, d_hidden,   bias=False)
        self.W2 = nn.Linear(d, d_hidden,   bias=False)
        self.W3 = nn.Linear(d_hidden, d,   bias=False)
    def forward(self, x): return self.W3(F.silu(self.W1(x)) * self.W2(x))

d_model   = 512
d_std_ff  = 4 * d_model          # standard d_ff = 2048
d_swi_ff  = int(d_std_ff * 2/3)  # SwiGLU d_ff = 1365

std = StandardFFN(d_model, d_std_ff)
swi = SwiGLUFFN(d_model, d_swi_ff)
p_std = sum(p.numel() for p in std.parameters())
p_swi = sum(p.numel() for p in swi.parameters())

print(f'Standard FFN  (2 mats, d_ff={d_std_ff}): {p_std:,} params')
print(f'SwiGLU FFN    (3 mats, d_ff={d_swi_ff}): {p_swi:,} params')
print(f'Ratio: {p_swi/p_std:.4f}  (close to 1.000 — parameter-equivalent)')
print(f'Formula check — 3 mats: 3*{d_model}*{d_swi_ff} = {3*d_model*d_swi_ff:,}')
print(f'Formula check — 2 mats: 2*{d_model}*{d_std_ff} = {2*d_model*d_std_ff:,}')
```

## Code 4 — SwiGLU in a Full LLaMA-Style Block

A complete LLaMA-style decoder block using RMSNorm (instead of LayerNorm), SwiGLU FFN, and pre-norm layout — the building block used in LLaMA 1/2/3 and Mistral.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalisation (LLaMA, Mistral)."""
    def __init__(self, d: int, eps: float = 1e-6):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(d))
        self.eps    = eps
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rms = x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt()
        return self.weight * x / rms

class SwiGLUFFN(nn.Module):
    def __init__(self, d: int, d_ff: int):
        super().__init__()
        self.gate = nn.Linear(d, d_ff, bias=False)
        self.up   = nn.Linear(d, d_ff, bias=False)
        self.down = nn.Linear(d_ff, d, bias=False)
    def forward(self, x): return self.down(F.silu(self.gate(x)) * self.up(x))

class LLaMABlock(nn.Module):
    """LLaMA-style block: RMSNorm + MHA + SwiGLU, pre-norm layout."""
    def __init__(self, d_model: int = 256, n_heads: int = 8, d_ff: int = None):
        super().__init__()
        d_ff           = d_ff or int(d_model * 8 / 3)
        self.attn_norm = RMSNorm(d_model)
        self.ffn_norm  = RMSNorm(d_model)
        self.attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True, bias=False)
        self.ffn  = SwiGLUFFN(d_model, d_ff)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        n = self.attn_norm(x)
        x = x + self.attn(n, n, n)[0]      # pre-norm attention
        x = x + self.ffn(self.ffn_norm(x)) # pre-norm SwiGLU FFN
        return x

block  = LLaMABlock(d_model=256, n_heads=8)
x      = torch.randn(2, 16, 256)
out    = block(x)
params = sum(p.numel() for p in block.parameters())
print(f'LLaMA block output: {out.shape}')
print(f'Parameters: {params:,}')
```

## FFN Activation Variants Compared

| Variant | Gate Activation | Formula (simplified) | Used In | Quality Rank |
| --- | --- | --- | --- | --- |
| Standard ReLU | None | ReLU(xW1) @ W2 | Original Transformer, BERT | Baseline |
| Standard GELU | None | GELU(xW1) @ W2 | GPT-2, RoBERTa, DistilBERT | Better than ReLU |
| GLU (sigmoid) | Sigmoid σ | (σ(xW) ⊙ xV) @ W2 | Dauphin et al. (2017), LM tasks | Moderate gain |
| ReGLU | ReLU | (ReLU(xW) ⊙ xV) @ W2 | Shazeer 2020 ablations | Competitive |
| GEGLU | GELU | (GELU(xW) ⊙ xV) @ W2 | T5 variants, some BERT models | Strong |
| SwiGLU | SiLU (Swish) | (SiLU(xW) ⊙ xV) @ W2 | LLaMA 1/2/3, Mistral, PaLM, Gemma | Best reported |

SwiGLU represents one of the clearest wins in modern LLM design: a one-line change to the FFN activation that consistently improves perplexity at identical compute. The 3-matrix design with the 2/3 hidden-dimension adjustment keeps FLOP and parameter counts equivalent to a standard FFN, so there is no cost to switching. For any new Transformer project using LLaMA-family architecture as a reference, SwiGLU with RMSNorm should be the starting point for the FFN sub-layer.

