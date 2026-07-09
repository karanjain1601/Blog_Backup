---
title: "PyTorch Internals — Strides, Contiguous Memory, and Dispatch"
slug: "pytorch-internals"
description: "Under the hood of PyTorch: tensor storage layout, strides, non-contiguous tensors, the dispatcher, custom autograd Functions, TorchScript, and torch.fx."
tags: ["pytorch", "tools", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9zdCBQeVRvcmNoIHVzZXJzIG5ldmVyIG5lZWQgdG8gdGhpbmsgYWJvdXQgdGVuc29yIHN0cmlkZXMgb3IgdGhlIGRpc3BhdGNoZXIg4oCUIHVudGlsIHBlcmZvcm1hbmNlIGRlZ3JhZGVzIHVuZXhwZWN0ZWRseSBvciBhIGN1c3RvbSBDVURBIGtlcm5lbCBtdXN0IGJlIGludGVncmF0ZWQuIFVuZGVyc3RhbmRpbmcgaG93IFB5VG9yY2ggc3RvcmVzIHRlbnNvcnMgaW4gbWVtb3J5LCByb3V0ZXMgb3BlcmF0aW9ucyB0byBiYWNrZW5kcywgYW5kIHRyYWNlcyBjb21wdXRhdGlvbiBncmFwaHMgaXMgZXNzZW50aWFsIGZvciBvcHRpbWl6aW5nIGFuZCBleHRlbmRpbmcgdGhlIGZyYW1ld29yay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW5zb3IgU3RvcmFnZTogU3RyaWRlcyBhbmQgQ29udGlndWl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBQeVRvcmNoIHRlbnNvciBpcyBub3QganVzdCBkYXRhIOKAlCBpdCBpcyBhIHZpZXcgaW50byBhIGNvbnRpZ3VvdXMgbWVtb3J5IGJsb2NrIGRlZmluZWQgYnk6IHN0b3JhZ2UgKHJhdyBtZW1vcnkpLCBvZmZzZXQgKHN0YXJ0IHBvc2l0aW9uKSwgc2hhcGUgKHNpemUgcGVyIGRpbWVuc2lvbiksIGFuZCBzdHJpZGVzIChzdGVwIHNpemUgaW4gbWVtb3J5IHRvIGFkdmFuY2Ugb25lIGVsZW1lbnQgYWxvbmcgZWFjaCBkaW1lbnNpb24pLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQ29udGlndW91cyB0ZW5zb3I6IHN0cmlkZXNbaV0gPSBwcm9kdWN0IG9mIHNoYXBlW2krMTpdIOKAlCBlbGVtZW50cyBzdG9yZWQgaW4gcm93LW1ham9yIChDKSBvcmRlciIsIkFmdGVyIHRyYW5zcG9zZTogc3RyaWRlcyBzd2FwIOKAlCB0aGUgZGF0YSBpcyB0aGUgc2FtZSwgYnV0IHRoZSB2aWV3IGlzIGRpZmZlcmVudCAobm9uLWNvbnRpZ3VvdXMpIiwiQWZ0ZXIgbmFycm93L3NsaWNlOiBzdHJpZGVzIHVuY2hhbmdlZCwgb2Zmc2V0IHNoaWZ0cyDigJQgYW5vdGhlciBub24tY29udGlndW91cyB2aWV3IiwiLmlzX2NvbnRpZ3VvdXMoKSByZXR1cm5zIFRydWUgb25seSBpZiBzdHJpZGVzIG1hdGNoIHRoZSBleHBlY3RlZCBDLW9yZGVyIGxheW91dCIsIi5jb250aWd1b3VzKCkgZm9yY2VzIGEgY29weSB0byBhIG5ldyBjb250aWd1b3VzIGFsbG9jYXRpb24g4oCUIG5lZWRlZCBiZWZvcmUgb3BlcmF0aW9ucyB0aGF0IHJlcXVpcmUgY29udGlndW91cyBpbnB1dCIsInZpZXcoKSByZXF1aXJlcyBjb250aWd1b3VzIGlucHV0OyByZXNoYXBlKCkgdXNlcyB2aWV3IGlmIHBvc3NpYmxlLCBvdGhlcndpc2UgY29waWVzIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0cmlkZXMgaW4gUHJhY3RpY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVuZGVyc3RhbmRpbmcgc3RyaWRlcyBoZWxwcyBkaWFnbm9zZSB3aHkgY2VydGFpbiBvcGVyYXRpb25zIGFyZSBzbG93IChub24tY29udGlndW91cyBtZW1vcnkgYWNjZXNzKSBhbmQgd2hlbiByZXNoYXBlIHZzIGNvbnRpZ3VvdXMrdmlldyBpcyBuZWVkZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG4jIENvbnRpZ3VvdXMgdGVuc29yOiBzaGFwZSAoMywgNClcbnggPSB0b3JjaC5hcmFuZ2UoMTIpLnJlc2hhcGUoMywgNClcbnByaW50KGZcdTAwMjdTaGFwZTogICAgICAgICAge3guc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1N0cmlkZXM6ICAgICAgICB7eC5zdHJpZGUoKX1cdTAwMjcpICAgIyAoNCwgMSkg4oCUIHJvdy1tYWpvclxucHJpbnQoZlx1MDAyN0lzIGNvbnRpZ3VvdXM6ICB7eC5pc19jb250aWd1b3VzKCl9XHUwMDI3KVxuXG4jIFRyYW5zcG9zZTogc2FtZSBkYXRhLCBzd2FwcGVkIHN0cmlkZXNcbnhfdCA9IHguVFxucHJpbnQoZlx1MDAyN1xcblRyYW5zcG9zZWQgc3RyaWRlczoge3hfdC5zdHJpZGUoKX1cdTAwMjcpICAjICgxLCA0KSDigJQgbm9uLWNvbnRpZ3VvdXNcbnByaW50KGZcdTAwMjdJcyBjb250aWd1b3VzOiAgICAgIHt4X3QuaXNfY29udGlndW91cygpfVx1MDAyNylcblxuIyB2aWV3KCkgZmFpbHMgb24gbm9uLWNvbnRpZ3VvdXMgdGVuc29yXG50cnk6XG4gICAgeF90LnZpZXcoNiwgMilcbmV4Y2VwdCBSdW50aW1lRXJyb3IgYXMgZTpcbiAgICBwcmludChmXHUwMDI3XFxudmlldygpIGVycm9yOiB7ZX1cdTAwMjcpXG5cbiMgY29udGlndW91cygpIGNyZWF0ZXMgYSBjb3B5IHdpdGggY29ycmVjdCBzdHJpZGVzXG54X3RfY29udGlnID0geF90LmNvbnRpZ3VvdXMoKVxucHJpbnQoZlx1MDAyN1xcbkFmdGVyIGNvbnRpZ3VvdXMoKSwgc3RyaWRlczoge3hfdF9jb250aWcuc3RyaWRlKCl9XHUwMDI3KVxueF90X2NvbnRpZy52aWV3KDYsIDIpICAjIG5vdyB3b3Jrc1xuXG4jIHJlc2hhcGUoKSA9IHZpZXcgaWYgY29udGlndW91cywgZWxzZSBjb3B5XG54X3Jlc2hhcGVkID0geF90LnJlc2hhcGUoNiwgMilcbnByaW50KGZcdTAwMjd4X3Jlc2hhcGVkIHNoYXJlcyBzdG9yYWdlOiB7eF9yZXNoYXBlZC5zdG9yYWdlKCkuZGF0YV9wdHIoKSA9PSB4X3Quc3RvcmFnZSgpLmRhdGFfcHRyKCl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkN1c3RvbSBBdXRvZ3JhZCBGdW5jdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gYSBudW1lcmljYWxseSBzdGFibGUgb3IgZnVzZWQgb3BlcmF0aW9uIGlzIG5lZWRlZCB0aGF0IGF1dG9ncmFkIGNhbm5vdCBoYW5kbGUgYXV0b21hdGljYWxseSwgdG9yY2guYXV0b2dyYWQuRnVuY3Rpb24gbGV0cyB5b3UgZGVmaW5lIGJvdGggdGhlIGZvcndhcmQgY29tcHV0YXRpb24gYW5kIHRoZSBleGFjdCBiYWNrd2FyZCAoZ3JhZGllbnQpIGZvcm11bGEuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaC5hdXRvZ3JhZCBpbXBvcnQgRnVuY3Rpb25cblxuY2xhc3MgU3RhYmxlU2lnbW9pZChGdW5jdGlvbik6XG4gICAgXCJcIlwiTnVtZXJpY2FsbHkgc3RhYmxlIHNpZ21vaWQgd2l0aCBzYXZlZCBvdXRwdXQgZm9yIGJhY2t3YXJkLlwiXCJcIlxuXG4gICAgQHN0YXRpY21ldGhvZFxuICAgIGRlZiBmb3J3YXJkKGN0eCwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgIyBOdW1lcmljYWxseSBzdGFibGU6IHVzZSBuZWdhdGl2ZSBleHBvbmVudGlhbCBmb3IgcG9zaXRpdmUgeFxuICAgICAgICBzaWcgPSB0b3JjaC53aGVyZSh4IFx1MDAzZT0gMCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgMSAvICgxICsgdG9yY2guZXhwKC14KSksXG4gICAgICAgICAgICAgICAgICAgICAgICAgIHRvcmNoLmV4cCh4KSAvICgxICsgdG9yY2guZXhwKHgpKSlcbiAgICAgICAgY3R4LnNhdmVfZm9yX2JhY2t3YXJkKHNpZykgICMgc2F2ZSBvdXRwdXQgZm9yIGJhY2t3YXJkIHBhc3NcbiAgICAgICAgcmV0dXJuIHNpZ1xuXG4gICAgQHN0YXRpY21ldGhvZFxuICAgIGRlZiBiYWNrd2FyZChjdHgsIGdyYWRfb3V0cHV0OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBzaWcsID0gY3R4LnNhdmVkX3RlbnNvcnNcbiAgICAgICAgIyBkL2R4IHNpZ21vaWQoeCkgPSBzaWdtb2lkKHgpICogKDEgLSBzaWdtb2lkKHgpKVxuICAgICAgICByZXR1cm4gZ3JhZF9vdXRwdXQgKiBzaWcgKiAoMSAtIHNpZylcblxuIyBSZWdpc3RlciBhcyBhIGNhbGxhYmxlIGZ1bmN0aW9uXG5zdGFibGVfc2lnbW9pZCA9IFN0YWJsZVNpZ21vaWQuYXBwbHlcblxuIyBUZXN0OiBjb21wYXJlIHdpdGggdG9yY2guc2lnbW9pZFxueCA9IHRvcmNoLnJhbmRuKDUsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbm91dF9jdXN0b20gPSBzdGFibGVfc2lnbW9pZCh4KVxub3V0X2N1c3RvbS5zdW0oKS5iYWNrd2FyZCgpXG5wcmludChcdTAwMjdDdXN0b20gZ3JhZGllbnQ6XHUwMDI3LCB4LmdyYWQpXG5cbngyID0geC5kZXRhY2goKS5jbG9uZSgpLnJlcXVpcmVzX2dyYWRfKFRydWUpXG50b3JjaC5zaWdtb2lkKHgyKS5zdW0oKS5iYWNrd2FyZCgpXG5wcmludChcdTAwMjdUb3JjaCBncmFkaWVudDogXHUwMDI3LCB4Mi5ncmFkKVxucHJpbnQoXHUwMDI3TWF0Y2g6XHUwMDI3LCB0b3JjaC5hbGxjbG9zZSh4LmdyYWQsIHgyLmdyYWQsIGF0b2w9MWUtNikpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVG9yY2hTY3JpcHQg4oCUIFRyYWNpbmcgdnMgU2NyaXB0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUb3JjaFNjcmlwdCBjb21waWxlcyBQeXRob24gY29kZSB0byBhIHBvcnRhYmxlIElSIChpbnRlcm1lZGlhdGUgcmVwcmVzZW50YXRpb24pIHRoYXQgY2FuIGJlIHNlcmlhbGl6ZWQsIG9wdGltaXplZCwgYW5kIGRlcGxveWVkIHdpdGhvdXQgYSBQeXRob24gaW50ZXJwcmV0ZXIg4oCUIGVzc2VudGlhbCBmb3IgbW9iaWxlIGFuZCBDKysgc2VydmluZy4gVHdvIG1vZGVzOiB0cmFjZSAocmVjb3JkcyBvcGVyYXRpb25zIG9uIGEgc2FtcGxlIGlucHV0KSBhbmQgc2NyaXB0IChhbmFseXplcyBQeXRob24gc291cmNlIGNvZGUgc3RhdGljYWxseSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFNpbXBsZU5ldChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW06IGludCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmZjID0gbm4uTGluZWFyKGRpbSwgZGltKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgcmV0dXJuIHRvcmNoLnJlbHUoc2VsZi5mYyh4KSlcblxubW9kZWwgPSBTaW1wbGVOZXQoNjQpXG5tb2RlbC5ldmFsKClcblxuIyBNZXRob2QgMTogdG9yY2guaml0LnRyYWNlIOKAlCByZWNvcmRzIG9wZXJhdGlvbnMgb24gYSBzYW1wbGUgaW5wdXRcbnNhbXBsZSA9IHRvcmNoLnJhbmRuKDEsIDY0KVxudHJhY2VkID0gdG9yY2guaml0LnRyYWNlKG1vZGVsLCBzYW1wbGUpXG50cmFjZWQuc2F2ZShcdTAwMjdtb2RlbF90cmFjZWQucHRcdTAwMjcpICAjIHBvcnRhYmxlIHNlcmlhbGl6ZWQgbW9kZWxcbnByaW50KFx1MDAyN1RyYWNlZCBvdXRwdXQ6XHUwMDI3LCB0cmFjZWQoc2FtcGxlKS5zaGFwZSlcblxuIyBNZXRob2QgMjogdG9yY2guaml0LnNjcmlwdCDigJQgYW5hbHl6ZXMgUHl0aG9uIEFTVCwgc3VwcG9ydHMgY29udHJvbCBmbG93XG5AdG9yY2guaml0LnNjcmlwdFxuZGVmIGNvbmRpdGlvbmFsX29wKHg6IHRvcmNoLlRlbnNvciwgZmxhZzogYm9vbCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgaWYgZmxhZzogICMgY29udHJvbCBmbG93IHByZXNlcnZlZCBpbiBzY3JpcHRlZCBJUlxuICAgICAgICByZXR1cm4gdG9yY2gucmVsdSh4KVxuICAgIGVsc2U6XG4gICAgICAgIHJldHVybiB0b3JjaC5zaWdtb2lkKHgpXG5cbnByaW50KFx1MDAyN1NjcmlwdCB3aXRoIGZsYWc9VHJ1ZTogXHUwMDI3LCBjb25kaXRpb25hbF9vcCh0b3JjaC5yYW5kbigzKSwgVHJ1ZSkpXG5wcmludChcdTAwMjdTY3JpcHQgd2l0aCBmbGFnPUZhbHNlOlx1MDAyNywgY29uZGl0aW9uYWxfb3AodG9yY2gucmFuZG4oMyksIEZhbHNlKSlcblxuIyBMb2FkIGFuZCBydW4gdHJhY2VkIG1vZGVsIGluIGEgbmV3IHNlc3Npb24gKG5vIG1vZGVsIGRlZmluaXRpb24gbmVlZGVkKVxubG9hZGVkID0gdG9yY2guaml0LmxvYWQoXHUwMDI3bW9kZWxfdHJhY2VkLnB0XHUwMDI3KVxucHJpbnQoXHUwMDI3TG9hZGVkIG1vZGVsIG91dHB1dDpcdTAwMjcsIGxvYWRlZChzYW1wbGUpLnNoYXBlKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6InRvcmNoLmZ4IOKAlCBHcmFwaCBDYXB0dXJlIGFuZCBNYW5pcHVsYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6InRvcmNoLmZ4IGNhcHR1cmVzIHRoZSBzeW1ib2xpYyBleGVjdXRpb24gdHJhY2Ugb2YgYSBubi5Nb2R1bGUgYXMgYW4gZXhwbGljaXQgZ3JhcGggKEZYIElSKS4gVGhpcyBncmFwaCBjYW4gYmUgaW5zcGVjdGVkLCB0cmFuc2Zvcm1lZCwgYW5kIGNvbXBpbGVkIOKAlCB0aGUgZm91bmRhdGlvbiBmb3IgdG9yY2guY29tcGlsZVx1MDAyN3MgRHluYW1vIHRyYWNpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2guZnggYXMgZnhcblxuY2xhc3MgU21hbGxOZXQobm4uTW9kdWxlKTpcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICB4ID0gdG9yY2gucmVsdSh4KVxuICAgICAgICB4ID0geCAqIDIuMFxuICAgICAgICByZXR1cm4geC5zdW0oZGltPS0xKVxuXG5tb2RlbCA9IFNtYWxsTmV0KClcblxuIyBDYXB0dXJlIHRoZSBGWCBncmFwaCBieSBzeW1ib2xpYyB0cmFjaW5nXG5ncmFwaF9tb2R1bGUgPSBmeC5zeW1ib2xpY190cmFjZShtb2RlbClcblxucHJpbnQoXHUwMDI3PT09IEZYIEdyYXBoIE5vZGVzID09PVx1MDAyNylcbmZvciBub2RlIGluIGdyYXBoX21vZHVsZS5ncmFwaC5ub2RlczpcbiAgICBwcmludChmXHUwMDI3ICB7bm9kZS5vcDpcdTAwM2MxNX0ge25vZGUubmFtZTpcdTAwM2MyMH0gdGFyZ2V0PXtub2RlLnRhcmdldH1cdTAwMjcpXG5cbiMgRXhhbXBsZSB0cmFuc2Zvcm1hdGlvbjogcmVwbGFjZSByZWx1IHdpdGggZ2VsdVxuZm9yIG5vZGUgaW4gZ3JhcGhfbW9kdWxlLmdyYXBoLm5vZGVzOlxuICAgIGlmIG5vZGUub3AgPT0gXHUwMDI3Y2FsbF9mdW5jdGlvblx1MDAyNyBhbmQgbm9kZS50YXJnZXQgPT0gdG9yY2gucmVsdTpcbiAgICAgICAgbm9kZS50YXJnZXQgPSB0b3JjaC5ubi5mdW5jdGlvbmFsLmdlbHVcbiAgICAgICAgcHJpbnQoZlx1MDAyN1xcblJlcGxhY2VkIHJlbHUgLVx1MDAzZSBnZWx1IGluIG5vZGU6IHtub2RlLm5hbWV9XHUwMDI3KVxuXG5ncmFwaF9tb2R1bGUucmVjb21waWxlKCkgICMgcmVnZW5lcmF0ZSBQeXRob24gY29kZSBmcm9tIG1vZGlmaWVkIGdyYXBoXG54X3Rlc3QgPSB0b3JjaC5yYW5kbig0LCA4KVxub3V0ID0gZ3JhcGhfbW9kdWxlKHhfdGVzdClcbnByaW50KGZcdTAwMjdPdXRwdXQgYWZ0ZXIgdHJhbnNmb3JtYXRpb246IHtvdXQuc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW5zb3IgT3BlcmF0aW9uczogVmlld3MgdnMgQ29waWVzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk9wZXJhdGlvbiIsIkNvcGllcyBEYXRhIiwiU3RyaWRlIENoYW5nZSIsIlJlcXVpcmVzIENvbnRpZ3VvdXMiLCJXaGVuIHRvIFVzZSJdLCJyb3dzIjpbWyJ2aWV3KHNoYXBlKSIsIk5vIOKAlCB6ZXJvLWNvcHkiLCJZZXMgKHJlY29tcHV0ZWQpIiwiWWVzIiwiUmVzaGFwZSBjb250aWd1b3VzIHRlbnNvcnMgZWZmaWNpZW50bHkiXSxbInJlc2hhcGUoc2hhcGUpIiwiT25seSBpZiBuZWVkZWQiLCJZZXMiLCJObyAoY29waWVzIGlmIG5lZWRlZCkiLCJHZW5lcmFsIHJlc2hhcGUg4oCUIHByZWZlciBvdmVyIHZpZXciXSxbInRyYW5zcG9zZShkMCwgZDEpIiwiTm8g4oCUIHplcm8tY29weSIsIlllcyAoc3dhcHBlZCkiLCJObyIsIlN3YXAgdHdvIGRpbWVuc2lvbnM7IGNoZWNrIGNvbnRpZ3VpdHkgYWZ0ZXIiXSxbInBlcm11dGUoZGltcykiLCJObyDigJQgemVyby1jb3B5IiwiWWVzIChyZW9yZGVyZWQpIiwiTm8iLCJBcmJpdHJhcnkgZGltZW5zaW9uIHJlb3JkZXJpbmciXSxbImNvbnRpZ3VvdXMoKSIsIlllcyBpZiBuZWVkZWQiLCJSZXNldCB0byBDLW9yZGVyIiwiTi9BIiwiQmVmb3JlIHZpZXcoKSBvciBrZXJuZWwgcmVxdWlyaW5nIGNvbnRpZyBpbnB1dCJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJOb24tQ29udGlndW91cyBUZW5zb3JzIGFuZCBLZXJuZWwgUGVyZm9ybWFuY2UiLCJjb250ZW50IjoiQ1VEQSBrZXJuZWxzIGFzc3VtZSBjb250aWd1b3VzIG1lbW9yeSBmb3IgbWF4aW11bSB0aHJvdWdocHV0LiBPcGVyYXRpbmcgb24gYSBub24tY29udGlndW91cyB0ZW5zb3IgKGUuZy4sIGFmdGVyIHRyYW5zcG9zZSkgZm9yY2VzIFB5VG9yY2ggdG8gZWl0aGVyIGNvcHkgdGhlIHRlbnNvciBmaXJzdCBvciB1c2UgYSBzbG93ZXIgZ2VuZXJpYyBrZXJuZWwuIFByb2ZpbGUgd2l0aCB0b3JjaC5wcm9maWxlciBpZiB5b3Ugb2JzZXJ2ZSB1bmV4cGVjdGVkIHNsb3dkb3ducyDigJQgYSBzaW5nbGUgLmNvbnRpZ3VvdXMoKSBjYWxsIGJlZm9yZSBhIGNvbXB1dGUtaGVhdnkgb3BlcmF0aW9uIG9mdGVuIHJlc29sdmVzIGl0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRlbnNvcnMgYXJlIChzdG9yYWdlLCBvZmZzZXQsIHNoYXBlLCBzdHJpZGVzKSDigJQgdHJhbnNwb3NlIGFuZCBzbGljZSBjcmVhdGUgbm9uLWNvbnRpZ3VvdXMgdmlld3Mgd2l0aG91dCBjb3B5aW5nIiwiLmNvbnRpZ3VvdXMoKSBmb3JjZXMgYSBjb3B5IHRvIEMtb3JkZXIgbWVtb3J5IOKAlCByZXF1aXJlZCBiZWZvcmUgdmlldygpIGFuZCBtYW55IENVREEga2VybmVscyIsIkN1c3RvbSBhdXRvZ3JhZCBGdW5jdGlvbnM6IGRlZmluZSBmb3J3YXJkICsgYmFja3dhcmQgZXhwbGljaXRseSB3aXRoIGN0eC5zYXZlX2Zvcl9iYWNrd2FyZCIsIlRvcmNoU2NyaXB0IHRyYWNlIHJlY29yZHMgb3BlcmF0aW9ucyBvbiBhIHNhbXBsZTsgc2NyaXB0IHBhcnNlcyBQeXRob24gQVNUIOKAlCBzY3JpcHQgc3VwcG9ydHMgY29udHJvbCBmbG93LCB0cmFjZSBkb2VzIG5vdCIsInRvcmNoLmZ4IGNhcHR1cmVzIHRoZSBleGVjdXRpb24gZ3JhcGggYXMgYW4gZWRpdGFibGUgSVIg4oCUIGZvdW5kYXRpb24gZm9yIGNvbXBpbGUtdGltZSBvcHRpbWl6YXRpb25zIl19XQ=="
---
# PyTorch Internals — Strides, Contiguous Memory, and Dispatch

Most PyTorch users never need to think about tensor strides or the dispatcher — until performance degrades unexpectedly or a custom CUDA kernel must be integrated. Understanding how PyTorch stores tensors in memory, routes operations to backends, and traces computation graphs is essential for optimizing and extending the framework.

## Tensor Storage: Strides and Contiguity

A PyTorch tensor is not just data — it is a view into a contiguous memory block defined by: storage (raw memory), offset (start position), shape (size per dimension), and strides (step size in memory to advance one element along each dimension).

- Contiguous tensor: strides[i] = product of shape[i+1:] — elements stored in row-major (C) order
- After transpose: strides swap — the data is the same, but the view is different (non-contiguous)
- After narrow/slice: strides unchanged, offset shifts — another non-contiguous view
- .is_contiguous() returns True only if strides match the expected C-order layout
- .contiguous() forces a copy to a new contiguous allocation — needed before operations that require contiguous input
- view() requires contiguous input; reshape() uses view if possible, otherwise copies

## Strides in Practice

Understanding strides helps diagnose why certain operations are slow (non-contiguous memory access) and when reshape vs contiguous+view is needed.

```python
import torch

# Contiguous tensor: shape (3, 4)
x = torch.arange(12).reshape(3, 4)
print(f'Shape:          {x.shape}')
print(f'Strides:        {x.stride()}')   # (4, 1) — row-major
print(f'Is contiguous:  {x.is_contiguous()}')

# Transpose: same data, swapped strides
x_t = x.T
print(f'\nTransposed strides: {x_t.stride()}')  # (1, 4) — non-contiguous
print(f'Is contiguous:      {x_t.is_contiguous()}')

# view() fails on non-contiguous tensor
try:
    x_t.view(6, 2)
except RuntimeError as e:
    print(f'\nview() error: {e}')

# contiguous() creates a copy with correct strides
x_t_contig = x_t.contiguous()
print(f'\nAfter contiguous(), strides: {x_t_contig.stride()}')
x_t_contig.view(6, 2)  # now works

# reshape() = view if contiguous, else copy
x_reshaped = x_t.reshape(6, 2)
print(f'x_reshaped shares storage: {x_reshaped.storage().data_ptr() == x_t.storage().data_ptr()}')
```

## Custom Autograd Functions

When a numerically stable or fused operation is needed that autograd cannot handle automatically, torch.autograd.Function lets you define both the forward computation and the exact backward (gradient) formula.

```python
import torch
from torch.autograd import Function

class StableSigmoid(Function):
    """Numerically stable sigmoid with saved output for backward."""

    @staticmethod
    def forward(ctx, x: torch.Tensor) -> torch.Tensor:
        # Numerically stable: use negative exponential for positive x
        sig = torch.where(x >= 0,
                          1 / (1 + torch.exp(-x)),
                          torch.exp(x) / (1 + torch.exp(x)))
        ctx.save_for_backward(sig)  # save output for backward pass
        return sig

    @staticmethod
    def backward(ctx, grad_output: torch.Tensor) -> torch.Tensor:
        sig, = ctx.saved_tensors
        # d/dx sigmoid(x) = sigmoid(x) * (1 - sigmoid(x))
        return grad_output * sig * (1 - sig)

# Register as a callable function
stable_sigmoid = StableSigmoid.apply

# Test: compare with torch.sigmoid
x = torch.randn(5, requires_grad=True)
out_custom = stable_sigmoid(x)
out_custom.sum().backward()
print('Custom gradient:', x.grad)

x2 = x.detach().clone().requires_grad_(True)
torch.sigmoid(x2).sum().backward()
print('Torch gradient: ', x2.grad)
print('Match:', torch.allclose(x.grad, x2.grad, atol=1e-6))
```

## TorchScript — Tracing vs Scripting

TorchScript compiles Python code to a portable IR (intermediate representation) that can be serialized, optimized, and deployed without a Python interpreter — essential for mobile and C++ serving. Two modes: trace (records operations on a sample input) and script (analyzes Python source code statically).

```python
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.fc = nn.Linear(dim, dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.relu(self.fc(x))

model = SimpleNet(64)
model.eval()

# Method 1: torch.jit.trace — records operations on a sample input
sample = torch.randn(1, 64)
traced = torch.jit.trace(model, sample)
traced.save('model_traced.pt')  # portable serialized model
print('Traced output:', traced(sample).shape)

# Method 2: torch.jit.script — analyzes Python AST, supports control flow
@torch.jit.script
def conditional_op(x: torch.Tensor, flag: bool) -> torch.Tensor:
    if flag:  # control flow preserved in scripted IR
        return torch.relu(x)
    else:
        return torch.sigmoid(x)

print('Script with flag=True: ', conditional_op(torch.randn(3), True))
print('Script with flag=False:', conditional_op(torch.randn(3), False))

# Load and run traced model in a new session (no model definition needed)
loaded = torch.jit.load('model_traced.pt')
print('Loaded model output:', loaded(sample).shape)
```

## torch.fx — Graph Capture and Manipulation

torch.fx captures the symbolic execution trace of a nn.Module as an explicit graph (FX IR). This graph can be inspected, transformed, and compiled — the foundation for torch.compile's Dynamo tracing.

```python
import torch
import torch.nn as nn
import torch.fx as fx

class SmallNet(nn.Module):
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(x)
        x = x * 2.0
        return x.sum(dim=-1)

model = SmallNet()

# Capture the FX graph by symbolic tracing
graph_module = fx.symbolic_trace(model)

print('=== FX Graph Nodes ===')
for node in graph_module.graph.nodes:
    print(f'  {node.op:<15} {node.name:<20} target={node.target}')

# Example transformation: replace relu with gelu
for node in graph_module.graph.nodes:
    if node.op == 'call_function' and node.target == torch.relu:
        node.target = torch.nn.functional.gelu
        print(f'\nReplaced relu -> gelu in node: {node.name}')

graph_module.recompile()  # regenerate Python code from modified graph
x_test = torch.randn(4, 8)
out = graph_module(x_test)
print(f'Output after transformation: {out.shape}')
```

---

## Tensor Operations: Views vs Copies

| Operation | Copies Data | Stride Change | Requires Contiguous | When to Use |
| --- | --- | --- | --- | --- |
| view(shape) | No — zero-copy | Yes (recomputed) | Yes | Reshape contiguous tensors efficiently |
| reshape(shape) | Only if needed | Yes | No (copies if needed) | General reshape — prefer over view |
| transpose(d0, d1) | No — zero-copy | Yes (swapped) | No | Swap two dimensions; check contiguity after |
| permute(dims) | No — zero-copy | Yes (reordered) | No | Arbitrary dimension reordering |
| contiguous() | Yes if needed | Reset to C-order | N/A | Before view() or kernel requiring contig input |

> **Non-Contiguous Tensors and Kernel Performance**: CUDA kernels assume contiguous memory for maximum throughput. Operating on a non-contiguous tensor (e.g., after transpose) forces PyTorch to either copy the tensor first or use a slower generic kernel. Profile with torch.profiler if you observe unexpected slowdowns — a single .contiguous() call before a compute-heavy operation often resolves it.

## Key Takeaways

- Tensors are (storage, offset, shape, strides) — transpose and slice create non-contiguous views without copying
- .contiguous() forces a copy to C-order memory — required before view() and many CUDA kernels
- Custom autograd Functions: define forward + backward explicitly with ctx.save_for_backward
- TorchScript trace records operations on a sample; script parses Python AST — script supports control flow, trace does not
- torch.fx captures the execution graph as an editable IR — foundation for compile-time optimizations

