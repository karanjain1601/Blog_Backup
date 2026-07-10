---
title: "Group Norm and Instance Norm — Small Batch Alternatives"
slug: "group-norm-instance-norm"
description: "Implement GroupNorm and InstanceNorm from scratch, demonstrate BN failure at small batch sizes, apply IN for style transfer, and compare all normalization methods across tasks."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT2JqZWN0IGRldGVjdGlvbiBhbmQgc2VnbWVudGF0aW9uIG1vZGVscyBvZnRlbiB0cmFpbiB3aXRoIHZlcnkgc21hbGwgYmF0Y2ggc2l6ZXMgKDHigJM0IGltYWdlcyBwZXIgR1BVKSBiZWNhdXNlIGhpZ2gtcmVzb2x1dGlvbiBpbWFnZXMgY29uc3VtZSBzaWduaWZpY2FudCBtZW1vcnkuIEJhdGNoIE5vcm1hbGl6YXRpb25cdTAwMjdzIHN0YXRpc3RpY3MgYmVjb21lIHVucmVsaWFibGUgYXQgdGhlc2Ugc21hbGwgYmF0Y2ggc2l6ZXMsIGNhdXNpbmcgdHJhaW5pbmcgaW5zdGFiaWxpdHkgYW5kIHBvb3IgcGVyZm9ybWFuY2UuIEdyb3VwIE5vcm1hbGl6YXRpb24gKFd1IFx1MDAyNiBIZSAyMDE4KSBhbmQgSW5zdGFuY2UgTm9ybWFsaXphdGlvbiAoVWx5YW5vdiBldCBhbC4gMjAxNikgc29sdmUgdGhpcyBieSBub3JtYWxpemluZyB3aXRob3V0IHJlbHlpbmcgb24gdGhlIGJhdGNoIGRpbWVuc2lvbiDigJQgR04gZm9yIGdlbmVyYWwgc21hbGwtYmF0Y2ggdHJhaW5pbmcsIElOIHNwZWNpZmljYWxseSBmb3Igc3R5bGUgdHJhbnNmZXIgdGFza3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JvdXAgTm9ybWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR3JvdXBOb3JtIGRpdmlkZXMgdGhlIEMgY2hhbm5lbHMgaW50byBHIGdyb3VwcyBhbmQgbm9ybWFsaXplcyB3aXRoaW4gZWFjaCBncm91cCBpbmRlcGVuZGVudGx5LiBGb3IgYW4gaW5wdXQgeCDiiIgg4oSdXihCw5dDw5dIw5dXKSwgdGhlIGNoYW5uZWxzIGFyZSByZXNoYXBlZCB0byAoQiwgRywgQy9HLCBILCBXKSBhbmQgbm9ybWFsaXphdGlvbiBpcyBjb21wdXRlZCBvdmVyIHRoZSAoQy9HLCBILCBXKSBkaW1lbnNpb25zIGZvciBlYWNoIGdyb3VwLiBTcGVjaWFsIGNhc2VzOiBHTiB3aXRoIEc9MSBub3JtYWxpemVzIG92ZXIgYWxsIGNoYW5uZWxzIHBlciBzYW1wbGUsIHdoaWNoIGVxdWFscyBMYXllck5vcm0gZm9yIGltYWdlIGlucHV0cy4gR04gd2l0aCBHPUMgbm9ybWFsaXplcyBlYWNoIGNoYW5uZWwgaW5kZXBlbmRlbnRseSBwZXIgc2FtcGxlLCB3aGljaCBlcXVhbHMgSW5zdGFuY2VOb3JtLiBUaGUgRz0zMiBkZWZhdWx0IHdvcmtzIHdlbGwgYWNyb3NzIGRldGVjdGlvbiwgc2VnbWVudGF0aW9uLCBhbmQgdmlkZW8gdGFza3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGdyb3VwX25vcm1fbnVtcHkoeCwgbnVtX2dyb3VwcywgZ2FtbWEsIGJldGEsIGVwcz0xZS01KTpcbiAgICAjIHg6IChCLCBDLCBILCBXKVxuICAgIEIsIEMsIEgsIFcgPSB4LnNoYXBlXG4gICAgYXNzZXJ0IEMgJSBudW1fZ3JvdXBzID09IDBcbiAgICBHID0gbnVtX2dyb3Vwc1xuICAgIHhfciA9IHgucmVzaGFwZShCLCBHLCBDIC8vIEcsIEgsIFcpXG4gICAgIyBNZWFuIGFuZCB2YXIgb3ZlciAoQy9HLCBILCBXKSBheGVzIHBlciAoQiwgRylcbiAgICBtZWFuID0geF9yLm1lYW4oYXhpcz0oMiwgMywgNCksIGtlZXBkaW1zPVRydWUpXG4gICAgdmFyICA9IHhfci52YXIoYXhpcz0oMiwgMywgNCksIGtlZXBkaW1zPVRydWUsIGRkb2Y9MClcbiAgICB4X2hhdCA9ICh4X3IgLSBtZWFuKSAvIG5wLnNxcnQodmFyICsgZXBzKVxuICAgIHhfaGF0ID0geF9oYXQucmVzaGFwZShCLCBDLCBILCBXKVxuICAgICMgZ2FtbWEsIGJldGE6IChDLCkgLVx1MDAzZSBicm9hZGNhc3Qgb3ZlciAoQiwgSCwgVylcbiAgICByZXR1cm4gZ2FtbWFbTm9uZSwgOiwgTm9uZSwgTm9uZV0gKiB4X2hhdCArIGJldGFbTm9uZSwgOiwgTm9uZSwgTm9uZV1cblxuQiwgQywgSCwgVyA9IDIsIDE2LCA4LCA4XG5udW1fZ3JvdXBzID0gNFxueF9ucCA9IG5wLnJhbmRvbS5yYW5kbihCLCBDLCBILCBXKS5hc3R5cGUobnAuZmxvYXQzMilcbmdhbW1hX25wID0gbnAub25lcyhDLCBkdHlwZT1ucC5mbG9hdDMyKVxuYmV0YV9ucCAgPSBucC56ZXJvcyhDLCBkdHlwZT1ucC5mbG9hdDMyKVxub3V0X3NjcmF0Y2ggPSBncm91cF9ub3JtX251bXB5KHhfbnAsIG51bV9ncm91cHMsIGdhbW1hX25wLCBiZXRhX25wKVxuXG5nbiA9IG5uLkdyb3VwTm9ybShudW1fZ3JvdXBzLCBDKVxub3V0X3RvcmNoID0gZ24odG9yY2gudGVuc29yKHhfbnApKS5kZXRhY2goKS5udW1weSgpXG5wcmludChmXHUwMDI3TWF4IGRpZmYgc2NyYXRjaCB2cyBQeVRvcmNoIEdyb3VwTm9ybToge25wLmFicyhvdXRfc2NyYXRjaCAtIG91dF90b3JjaCkubWF4KCk6LjJlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnN0YW5jZSBOb3JtYWxpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbnN0YW5jZU5vcm0gbm9ybWFsaXplcyBlYWNoIHNhbXBsZSBhbmQgZWFjaCBjaGFubmVsIGluZGVwZW5kZW50bHkgb3ZlciB0aGUgc3BhdGlhbCBkaW1lbnNpb25zIChILCBXKS4gSXQgY29tcGxldGVseSByZW1vdmVzIHRoZSBwZXItaW5zdGFuY2UgcGVyLWNoYW5uZWwgbWVhbiBhbmQgdmFyaWFuY2Ug4oCUIG5vcm1hbGl6aW5nIHRoZSBzdHlsZSBzdGF0aXN0aWNzLiBUaGlzIG1ha2VzIElOIGlkZWFsIGZvciBzdHlsZSB0cmFuc2ZlcjogZ2l2ZW4gY29udGVudCBpbWFnZSBDIGFuZCBzdHlsZSBpbWFnZSBTLCBub3JtYWxpemluZyB0aGUgZmVhdHVyZSBhY3RpdmF0aW9ucyBvZiBDIHRvIG1hdGNoIHRoZSBzdGF0aXN0aWNzIG9mIFMgKEFkYXB0aXZlIElOIC8gQWRhSU4pIHRyYW5zZmVycyB0aGUgc3R5bGUuIEN5Y2xlR0FOLCBTdHlsZUdBTiwgYW5kIGFyYml0cmFyeSBuZXVyYWwgc3R5bGUgdHJhbnNmZXIgYWxsIHVzZSBJTiBvciBpdHMgdmFyaWFudHMuIElOIGlzIGVxdWl2YWxlbnQgdG8gR04gd2l0aCBHPUMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGFkYXB0aXZlX2luc3RhbmNlX25vcm0oY29udGVudF9mZWF0LCBzdHlsZV9mZWF0LCBlcHM9MWUtNSk6XG4gICAgIyBBbGlnbiBjb250ZW50IGZlYXR1cmUgc3RhdGlzdGljcyB0byBtYXRjaCBzdHlsZSBmZWF0dXJlIHN0YXRpc3RpY3NcbiAgICAjIGNvbnRlbnRfZmVhdCwgc3R5bGVfZmVhdDogKEIsIEMsIEgsIFcpXG4gICAgQiwgQywgSCwgVyA9IGNvbnRlbnRfZmVhdC5zaGFwZVxuICAgICMgQ29tcHV0ZSBjb250ZW50IHN0YXRpc3RpY3NcbiAgICBjX21lYW4gPSBjb250ZW50X2ZlYXQubWVhbihkaW09KDIsIDMpLCBrZWVwZGltPVRydWUpXG4gICAgY19zdGQgID0gY29udGVudF9mZWF0LnN0ZChkaW09KDIsIDMpLCBrZWVwZGltPVRydWUpICsgZXBzXG4gICAgIyBDb21wdXRlIHN0eWxlIHN0YXRpc3RpY3NcbiAgICBzX21lYW4gPSBzdHlsZV9mZWF0Lm1lYW4oZGltPSgyLCAzKSwga2VlcGRpbT1UcnVlKVxuICAgIHNfc3RkICA9IHN0eWxlX2ZlYXQuc3RkKGRpbT0oMiwgMyksIGtlZXBkaW09VHJ1ZSkgKyBlcHNcbiAgICAjIE5vcm1hbGl6ZSBjb250ZW50IHRoZW4gcmVzY2FsZSB3aXRoIHN0eWxlIHN0YXRpc3RpY3NcbiAgICBub3JtYWxpemVkID0gKGNvbnRlbnRfZmVhdCAtIGNfbWVhbikgLyBjX3N0ZFxuICAgIHJldHVybiBzX3N0ZCAqIG5vcm1hbGl6ZWQgKyBzX21lYW5cblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIEMsIEgsIFcgPSAyLCA2NCwgMTYsIDE2XG5jb250ZW50ID0gdG9yY2gucmFuZG4oQiwgQywgSCwgVylcbnN0eWxlICAgPSB0b3JjaC5yYW5kbihCLCBDLCBILCBXKSAqIDIuNSArIDEuMCAgIyBkaWZmZXJlbnQgc2NhbGUgYW5kIHNoaWZ0XG5hZGFpbl9vdXQgPSBhZGFwdGl2ZV9pbnN0YW5jZV9ub3JtKGNvbnRlbnQsIHN0eWxlKVxuXG5wcmludChmXHUwMDI3Q29udGVudCBtZWFuOiB7Y29udGVudC5tZWFuKCgyLDMpKS5tZWFuKCk6LjNmfSwgc3RkOiB7Y29udGVudC5zdGQoKDIsMykpLm1lYW4oKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1N0eWxlICAgbWVhbjoge3N0eWxlLm1lYW4oKDIsMykpLm1lYW4oKTouM2Z9LCBzdGQ6IHtzdHlsZS5zdGQoKDIsMykpLm1lYW4oKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0FkYUlOICAgbWVhbjoge2FkYWluX291dC5tZWFuKCgyLDMpKS5tZWFuKCk6LjNmfSwgc3RkOiB7YWRhaW5fb3V0LnN0ZCgoMiwzKSkubWVhbigpOi4zZn1cdTAwMjcpXG5wcmludChcdTAwMjdBZGFJTiBvdXRwdXQgc3RhdGlzdGljcyBtYXRjaCBzdHlsZSDigJQgY29udGVudCBzdHJ1Y3R1cmUgcHJlc2VydmVkLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHTiB2cyBCTiBhdCBEaWZmZXJlbnQgQmF0Y2ggU2l6ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ild1IFx1MDAyNiBIZSAoMjAxOCkgc2hvd2VkIHRoYXQgR3JvdXBOb3JtIHNpZ25pZmljYW50bHkgb3V0cGVyZm9ybXMgQmF0Y2hOb3JtIG9uIENPQ08gb2JqZWN0IGRldGVjdGlvbiBhdCBzbWFsbCBiYXRjaCBzaXplcy4gQXQgYmF0Y2hfc2l6ZT0yIHBlciBHUFUsIEdOIGFjaGlldmVzIDM0LjggQVAgdnMgQk5cdTAwMjdzIDMxLjMgQVAgb24gTWFzayBSLUNOTiB3aXRoIFJlc05ldC01MCBGUE4uIFRoZSBwZXJmb3JtYW5jZSBnYXAgY2xvc2VzIGFzIGJhdGNoIHNpemUgaW5jcmVhc2VzOiBhdCBiYXRjaF9zaXplPTMyLCBCTiBtYXRjaGVzIG9yIHNsaWdodGx5IHN1cnBhc3NlcyBHTi4gRm9yIG1vZGVybiBHUFUgbWVtb3J5IGNvbnN0cmFpbnRzIChoaWdoLXJlc29sdXRpb24gaW5wdXRzLCBsYXJnZSBtb2RlbHMpLCBHTiBvciBMTiBpcyBwcmVmZXJyZWQgb3ZlciBCTiBpbiBkZXRlY3Rpb24vc2VnbWVudGF0aW9uIHBpcGVsaW5lcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbm9ybV9zdGF0cyhvdXRfdGVuc29yKTpcbiAgICBtID0gb3V0X3RlbnNvci5tZWFuKCkuaXRlbSgpXG4gICAgcyA9IG91dF90ZW5zb3Iuc3RkKCkuaXRlbSgpXG4gICAgcmV0dXJuIGZcdTAwMjdtZWFuPXttOi4zZn0sIHN0ZD17czouM2Z9XHUwMDI3XG5cbkMsIEgsIFcgPSAzMiwgMTYsIDE2XG5ub3JtX2xheWVycyA9IHtcbiAgICBcdTAwMjdHcm91cE5vcm0oRz04KVx1MDAyNzogbm4uR3JvdXBOb3JtKDgsIEMpLFxuICAgIFx1MDAyN0luc3RhbmNlTm9ybVx1MDAyNyA6IG5uLkluc3RhbmNlTm9ybTJkKEMsIGFmZmluZT1UcnVlKSxcbiAgICBcdTAwMjdMYXllck5vcm1cdTAwMjcgICAgOiBubi5Hcm91cE5vcm0oMSwgQyksICAjIEdOKEc9MSkgPT0gTE4gZm9yIGltYWdlc1xufVxuXG5wcmludChmXHUwMDI3e1wiXCI6IFx1MDAzYzIwfSB7XCJiYXRjaD0xXCI6IFx1MDAzYzI1fSB7XCJiYXRjaD00XCI6IFx1MDAzYzI1fSB7XCJiYXRjaD0xNlwifVx1MDAyNylcbmZvciBuYW1lLCBsYXllciBpbiBub3JtX2xheWVycy5pdGVtcygpOlxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciBicyBpbiBbMSwgNCwgMTZdOlxuICAgICAgICB4ID0gdG9yY2gucmFuZG4oYnMsIEMsIEgsIFcpXG4gICAgICAgIG91dCA9IGxheWVyKHgpXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKG5vcm1fc3RhdHMob3V0KSlcbiAgICBwcmludChmXHUwMDI3e25hbWU6IFx1MDAzYzIwfSB7cmVzdWx0c1swXTogXHUwMDNjMjV9IHtyZXN1bHRzWzFdOiBcdTAwM2MyNX0ge3Jlc3VsdHNbMl19XHUwMDI3KVxuXG5wcmludChcdTAwMjdcXG5CTiBzdGF0cyBmb3IgY29tcGFyaXNvbjpcdTAwMjcpXG5ibiA9IG5uLkJhdGNoTm9ybTJkKEMpXG5mb3IgYnMgaW4gWzEsIDQsIDE2XTpcbiAgICB4ID0gdG9yY2gucmFuZG4oYnMsIEMsIEgsIFcpXG4gICAgdHJ5OlxuICAgICAgICBvdXQgPSBibih4KVxuICAgICAgICBwcmludChmXHUwMDI3ICBCYXRjaE5vcm0gYmF0Y2g9e2JzfToge25vcm1fc3RhdHMob3V0KX1cdTAwMjcpXG4gICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOlxuICAgICAgICBwcmludChmXHUwMDI3ICBCYXRjaE5vcm0gYmF0Y2g9e2JzfTogRVJST1JcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJHcm91cE5vcm0gZm9yIFNtYWxsIEJhdGNoIERldGVjdGlvbiBhbmQgU2VnbWVudGF0aW9uIiwiY29udGVudCI6IldoZW4gdHJhaW5pbmcgTWFzayBSLUNOTiwgREVUUiwgb3IgU2VnRm9ybWVyIHdpdGggYmF0Y2hfc2l6ZSBcdTAwM2M9IDQgcGVyIEdQVSwgYWx3YXlzIHJlcGxhY2UgQmF0Y2hOb3JtIHdpdGggR3JvdXBOb3JtIChHPTMyIG9yIEc9MTYpLiBCTiBhdCBzbWFsbCBiYXRjaCBzaXplcyBwcm9kdWNlcyBub2lzeSBzdGF0aXN0aWNzIHRoYXQgZGVzdGFiaWxpemUgdHJhaW5pbmcuIEZyZWV6ZSBCTiAodmlhIFN5bmNCYXRjaE5vcm0gb3IgQmF0Y2hOb3JtIGZyb3plbj1UcnVlKSBpcyBhbm90aGVyIG9wdGlvbiB3aGVuIHVzaW5nIHByZXRyYWluZWQgYmFja2JvbmVzLCBidXQgdHJhaW5pbmcgbmV3IEJOIGxheWVycyBhdCBzbWFsbCBiYXRjaCBpcyBub3QgcmVjb21tZW5kZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVsYXRpb25zaGlwIEJldHdlZW4gTm9ybWFsaXphdGlvbiBNZXRob2RzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGwgZm91ciBub3JtYWxpemF0aW9ucyBzaGFyZSB0aGUgc2FtZSBjb21wdXRhdGlvbiBzdHJ1Y3R1cmUgYnV0IGRpZmZlciBpbiB3aGljaCBkaW1lbnNpb25zIHRoZXkgbm9ybWFsaXplIG92ZXIuIEZvciBhIDREIHRlbnNvciAoQiwgQywgSCwgVyk6IEJhdGNoTm9ybSBub3JtYWxpemVzIG92ZXIgKEIsIEgsIFcpIHBlciBjaGFubmVsIOKAlCBzdGF0aXN0aWNzIGRlcGVuZCBvbiBhbGwgc2FtcGxlcyBhbmQgYWxsIHNwYXRpYWwgcG9zaXRpb25zIGZvciBlYWNoIGNoYW5uZWwuIExheWVyTm9ybSBub3JtYWxpemVzIG92ZXIgKEMsIEgsIFcpIHBlciBzYW1wbGUg4oCUIHN0YXRpc3RpY3MgZGVwZW5kIG9uIGFsbCBjaGFubmVscyBhbmQgc3BhdGlhbCBwb3NpdGlvbnMgcGVyIHNhbXBsZS4gR3JvdXBOb3JtIG5vcm1hbGl6ZXMgb3ZlciAoQy9HLCBILCBXKSBwZXIgKHNhbXBsZSwgZ3JvdXApLiBJbnN0YW5jZU5vcm0gbm9ybWFsaXplcyBvdmVyIChILCBXKSBwZXIgKHNhbXBsZSwgY2hhbm5lbCkuIFRoaXMgdW5pZnlpbmcgdmlldyBtYWtlcyBpdCBlYXN5IHRvIHN3aXRjaCBiZXR3ZWVuIG5vcm1hbGl6YXRpb25zIGluIGNvZGUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHTihHPTEpID0gTGF5ZXJOb3JtIGZvciBpbWFnZSB0ZW5zb3JzIChub3JtYWxpemUgb3ZlciBhbGwgQywgSCwgVyBwZXIgc2FtcGxlKS4iLCJHTihHPUMpID0gSW5zdGFuY2VOb3JtIChub3JtYWxpemUgb3ZlciBILCBXIHBlciBzYW1wbGUgcGVyIGNoYW5uZWwpLiIsIkJOIHdpdGggYmF0Y2hfc2l6ZT0xIGFuZCBzcGF0aWFsIGNvbGxhcHNlID0gSW5zdGFuY2VOb3JtIChudW1lcmljYWxseSBlcXVpdmFsZW50IGJ1dCBkaWZmZXJlbnQgQVBJKS4iLCJBbGwgbm9ybWFsaXphdGlvbnMgc2hhcmUgdGhlIHNhbWUgYWZmaW5lIHRyYW5zZm9ybTogeSA9IM6zeMyCICsgzrIgd2l0aCBsZWFybmVkIHBlci1jaGFubmVsIM6zLCDOsi4iLCJTeW5jQmF0Y2hOb3JtOiBhbGxyZWR1Y2UgYmF0Y2ggc3RhdGlzdGljcyBhY3Jvc3MgR1BVcyDigJQgYWxsb3dzIGVmZmVjdGl2ZSBiYXRjaCBub3JtYWxpemF0aW9uIGV2ZW4gYXQgc21hbGwgcGVyLWRldmljZSBiYXRjaCBzaXplcyBpbiBkaXN0cmlidXRlZCB0cmFpbmluZy4iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDaG9vc2luZyB0aGUgbnVtYmVyIG9mIGdyb3VwcyBHIGluIEdyb3VwTm9ybSByZXF1aXJlcyBhIHRyYWRlb2ZmOiBmZXdlciBncm91cHMgKHNtYWxsIEcpIG1lYW5zIGxhcmdlciBncm91cCBzaXplIGFuZCBtb3JlIHN0YWJsZSBzdGF0aXN0aWNzLCBidXQgbGVzcyBmaW5lLWdyYWluZWQgbm9ybWFsaXphdGlvbi4gTW9yZSBncm91cHMgKGxhcmdlIEcpIGdpdmVzIGZpbmVyLWdyYWluZWQgbm9ybWFsaXphdGlvbiBidXQgc21hbGxlciBwZXItZ3JvdXAgc3RhdGlzdGljcy4gRz0zMiBpcyB0aGUgc3RhbmRhcmQgZm9yIGRldGVjdGlvbiBhbmQgc2VnbWVudGF0aW9uIG1vZGVscy4gRm9yIG5hcnJvdyBsYXllcnMgd2l0aCBmZXdlciB0aGFuIDMyIGNoYW5uZWxzLCB1c2UgRz00IG9yIEc9OC4gVGhlIGdyb3VwIHNpemUgQy9HIHNob3VsZCBhbHdheXMgYmUgYXQgbGVhc3QgOCB0byBtYWludGFpbiByZWxpYWJsZSB3aXRoaW4tZ3JvdXAgc3RhdGlzdGljcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCZW5jaG1hcms6IENsYXNzaWZpY2F0aW9uIHZzIERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGJlbmNobWFyayBiZWxvdyBtZWFzdXJlcyBmb3J3YXJkLXBhc3Mgd2FsbC1jbG9jayB0aW1lIGFjcm9zcyBub3JtYWxpemF0aW9uIG1ldGhvZHMgYXQgZGlmZmVyZW50IGJhdGNoIHNpemVzIG9uIGEgKEIsIDY0LCAzMiwgMzIpIGZlYXR1cmUgbWFwLiBHTiwgTE4sIGFuZCBJTiBhcmUgYmF0Y2gtc2l6ZSBpbmRlcGVuZGVudCDigJQgdGhlaXIgY29zdCBzY2FsZXMgbGluZWFybHkgd2l0aCBpbnB1dCBzaXplIHJlZ2FyZGxlc3Mgb2YgYmF0Y2guIEJOIGFkZHMgb3ZlcmhlYWQgZm9yIHJ1bm5pbmctc3RhdCB1cGRhdGVzIGR1cmluZyB0cmFpbmluZy4gT24gR1BVIHdpdGggZnVzZWQga2VybmVscyAoY3VETk4pLCBCTiBiZW5lZml0cyBmcm9tIGhpZ2hseSBvcHRpbWl6ZWQgQ1VEQSBjb2RlIHBhdGhzIGF0IGxhcmdlIGJhdGNoIHNpemVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRpbWVcblxuQywgSCwgVyA9IDY0LCAzMiwgMzJcbm5vcm1fY29uZmlncyA9IFtcbiAgICAoXHUwMDI3QmF0Y2hOb3JtMmRcdTAwMjcsIG5uLkJhdGNoTm9ybTJkKEMpKSxcbiAgICAoXHUwMDI3R3JvdXBOb3JtKEc9MzIpXHUwMDI3LCBubi5Hcm91cE5vcm0oMzIsIEMpKSxcbiAgICAoXHUwMDI3R3JvdXBOb3JtKEc9MS9MTilcdTAwMjcsIG5uLkdyb3VwTm9ybSgxLCBDKSksXG4gICAgKFx1MDAyN0luc3RhbmNlTm9ybTJkXHUwMDI3LCBubi5JbnN0YW5jZU5vcm0yZChDLCBhZmZpbmU9VHJ1ZSkpLFxuXVxuXG5wcmludChcdTAwMjc9PT0gVGhyb3VnaHB1dCBiZW5jaG1hcmsgKGZvcndhcmQgcGFzcyBvbmx5LCBtcyBwZXIgY2FsbCkgPT09XHUwMDI3KVxuZm9yIGJhdGNoX3NpemUgaW4gWzIsIDgsIDMyXTpcbiAgICBwcmludChmXHUwMDI3XFxuICBiYXRjaF9zaXplPXtiYXRjaF9zaXplfTpcdTAwMjcpXG4gICAgeCA9IHRvcmNoLnJhbmRuKGJhdGNoX3NpemUsIEMsIEgsIFcpXG4gICAgZm9yIG5hbWUsIGxheWVyIGluIG5vcm1fY29uZmlnczpcbiAgICAgICAgdGltZXMgPSBbXVxuICAgICAgICBmb3IgXyBpbiByYW5nZSgyMDApOlxuICAgICAgICAgICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgICAgICAgICBfID0gbGF5ZXIoeClcbiAgICAgICAgICAgIHRpbWVzLmFwcGVuZCgodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAqIDEwMDApXG4gICAgICAgIGF2ZyA9IHN1bSh0aW1lc1syMDpdKSAvIGxlbih0aW1lc1syMDpdKSAgIyBza2lwIHdhcm11cFxuICAgICAgICBwcmludChmXHUwMDI3ICAgIHtuYW1lOlx1MDAzYzI1fToge2F2ZzouM2Z9IG1zXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5vcm1hbGl6YXRpb24gTWV0aG9kcyBSZWZlcmVuY2UgVGFibGUifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiTm9ybWFsaXplcyBPdmVyIiwiQmF0Y2ggRGVwZW5kZW50IiwiVHJhaW4vRXZhbCBHYXAiLCJUeXBpY2FsIFVzZSBDYXNlIl0sInJvd3MiOltbIkJhdGNoTm9ybSIsIihCLCBILCBXKSBwZXIgY2hhbm5lbCIsIlllcyIsIlllcyIsIkltYWdlIGNsYXNzaWZpY2F0aW9uLCBsYXJnZSBiYXRjaCAo4omlMTYpIl0sWyJMYXllck5vcm0iLCIoQywgSCwgVykgcGVyIHNhbXBsZSIsIk5vIiwiTm8iLCJUcmFuc2Zvcm1lcnMsIE5MUCwgQkVSVCwgVDUiXSxbIkdyb3VwTm9ybSIsIihDL0csIEgsIFcpIHBlciAoQiwgRykiLCJObyIsIk5vIiwiT2JqZWN0IGRldGVjdGlvbiwgc2VnbWVudGF0aW9uLCBzbWFsbCBiYXRjaCJdLFsiSW5zdGFuY2VOb3JtIiwiKEgsIFcpIHBlciAoQiwgQykiLCJObyIsIk5vIiwiU3R5bGUgdHJhbnNmZXIsIEN5Y2xlR0FOLCBpbWFnZS10by1pbWFnZSJdLFsiUk1TTm9ybSIsIkZlYXR1cmUgZGltIHBlciBzYW1wbGUgKG5vIG1lYW4pIiwiTm8iLCJObyIsIkxMTSBwcmUtdHJhaW5pbmcsIExMYU1BLCBHZW1tYSwgTWlzdHJhbCJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHcm91cE5vcm0gd2l0aCBHPTMyIGlzIHRoZSByZWNvbW1lbmRlZCBkZWZhdWx0IGZvciBhbnkgdmlzaW9uIHRhc2sgd2hlcmUgYmF0Y2ggc2l6ZSBwZXIgR1BVIGlzIDggb3IgZmV3ZXIuIEZvciBjbGFzc2lmaWNhdGlvbiB3aXRoIGxhcmdlIGJhdGNoZXMgKOKJpTMyKSwgQmF0Y2hOb3JtIHJlbWFpbnMgY29tcGV0aXRpdmUuIEluc3RhbmNlIE5vcm1hbGl6YXRpb24gaXMgc3BlY2lhbGl6ZWQgZm9yIHN0eWxlIHRyYW5zZmVyIGFuZCBzaG91bGQgbm90IGJlIHVzZWQgYXMgYSBnZW5lcmFsLXB1cnBvc2UgcmVwbGFjZW1lbnQgZm9yIEJOIG9yIEdOIOKAlCByZW1vdmluZyBwZXItaW5zdGFuY2Ugc3RhdGlzdGljcyBhbHNvIHJlbW92ZXMgZGlzY3JpbWluYXRpdmUgaW5mb3JtYXRpb24gdGhhdCBjbGFzc2lmaWNhdGlvbiB0YXNrcyByZWx5IG9uLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Group Norm and Instance Norm — Small Batch Alternatives

Object detection and segmentation models often train with very small batch sizes (1–4 images per GPU) because high-resolution images consume significant memory. Batch Normalization's statistics become unreliable at these small batch sizes, causing training instability and poor performance. Group Normalization (Wu & He 2018) and Instance Normalization (Ulyanov et al. 2016) solve this by normalizing without relying on the batch dimension — GN for general small-batch training, IN specifically for style transfer tasks.

## Group Normalization

GroupNorm divides the C channels into G groups and normalizes within each group independently. For an input x ∈ ℝ^(B×C×H×W), the channels are reshaped to (B, G, C/G, H, W) and normalization is computed over the (C/G, H, W) dimensions for each group. Special cases: GN with G=1 normalizes over all channels per sample, which equals LayerNorm for image inputs. GN with G=C normalizes each channel independently per sample, which equals InstanceNorm. The G=32 default works well across detection, segmentation, and video tasks.

```python
import numpy as np
import torch
import torch.nn as nn

def group_norm_numpy(x, num_groups, gamma, beta, eps=1e-5):
    # x: (B, C, H, W)
    B, C, H, W = x.shape
    assert C % num_groups == 0
    G = num_groups
    x_r = x.reshape(B, G, C // G, H, W)
    # Mean and var over (C/G, H, W) axes per (B, G)
    mean = x_r.mean(axis=(2, 3, 4), keepdims=True)
    var  = x_r.var(axis=(2, 3, 4), keepdims=True, ddof=0)
    x_hat = (x_r - mean) / np.sqrt(var + eps)
    x_hat = x_hat.reshape(B, C, H, W)
    # gamma, beta: (C,) -> broadcast over (B, H, W)
    return gamma[None, :, None, None] * x_hat + beta[None, :, None, None]

B, C, H, W = 2, 16, 8, 8
num_groups = 4
x_np = np.random.randn(B, C, H, W).astype(np.float32)
gamma_np = np.ones(C, dtype=np.float32)
beta_np  = np.zeros(C, dtype=np.float32)
out_scratch = group_norm_numpy(x_np, num_groups, gamma_np, beta_np)

gn = nn.GroupNorm(num_groups, C)
out_torch = gn(torch.tensor(x_np)).detach().numpy()
print(f'Max diff scratch vs PyTorch GroupNorm: {np.abs(out_scratch - out_torch).max():.2e}')
```

## Instance Normalization

InstanceNorm normalizes each sample and each channel independently over the spatial dimensions (H, W). It completely removes the per-instance per-channel mean and variance — normalizing the style statistics. This makes IN ideal for style transfer: given content image C and style image S, normalizing the feature activations of C to match the statistics of S (Adaptive IN / AdaIN) transfers the style. CycleGAN, StyleGAN, and arbitrary neural style transfer all use IN or its variants. IN is equivalent to GN with G=C.

```python
import torch
import torch.nn as nn
import numpy as np

def adaptive_instance_norm(content_feat, style_feat, eps=1e-5):
    # Align content feature statistics to match style feature statistics
    # content_feat, style_feat: (B, C, H, W)
    B, C, H, W = content_feat.shape
    # Compute content statistics
    c_mean = content_feat.mean(dim=(2, 3), keepdim=True)
    c_std  = content_feat.std(dim=(2, 3), keepdim=True) + eps
    # Compute style statistics
    s_mean = style_feat.mean(dim=(2, 3), keepdim=True)
    s_std  = style_feat.std(dim=(2, 3), keepdim=True) + eps
    # Normalize content then rescale with style statistics
    normalized = (content_feat - c_mean) / c_std
    return s_std * normalized + s_mean

torch.manual_seed(0)
B, C, H, W = 2, 64, 16, 16
content = torch.randn(B, C, H, W)
style   = torch.randn(B, C, H, W) * 2.5 + 1.0  # different scale and shift
adain_out = adaptive_instance_norm(content, style)

print(f'Content mean: {content.mean((2,3)).mean():.3f}, std: {content.std((2,3)).mean():.3f}')
print(f'Style   mean: {style.mean((2,3)).mean():.3f}, std: {style.std((2,3)).mean():.3f}')
print(f'AdaIN   mean: {adain_out.mean((2,3)).mean():.3f}, std: {adain_out.std((2,3)).mean():.3f}')
print('AdaIN output statistics match style — content structure preserved.')
```

## GN vs BN at Different Batch Sizes

Wu & He (2018) showed that GroupNorm significantly outperforms BatchNorm on COCO object detection at small batch sizes. At batch_size=2 per GPU, GN achieves 34.8 AP vs BN's 31.3 AP on Mask R-CNN with ResNet-50 FPN. The performance gap closes as batch size increases: at batch_size=32, BN matches or slightly surpasses GN. For modern GPU memory constraints (high-resolution inputs, large models), GN or LN is preferred over BN in detection/segmentation pipelines.

```python
import torch
import torch.nn as nn
import numpy as np

def norm_stats(out_tensor):
    m = out_tensor.mean().item()
    s = out_tensor.std().item()
    return f'mean={m:.3f}, std={s:.3f}'

C, H, W = 32, 16, 16
norm_layers = {
    'GroupNorm(G=8)': nn.GroupNorm(8, C),
    'InstanceNorm' : nn.InstanceNorm2d(C, affine=True),
    'LayerNorm'    : nn.GroupNorm(1, C),  # GN(G=1) == LN for images
}

print(f'{"": <20} {"batch=1": <25} {"batch=4": <25} {"batch=16"}')
for name, layer in norm_layers.items():
    results = []
    for bs in [1, 4, 16]:
        x = torch.randn(bs, C, H, W)
        out = layer(x)
        results.append(norm_stats(out))
    print(f'{name: <20} {results[0]: <25} {results[1]: <25} {results[2]}')

print('\nBN stats for comparison:')
bn = nn.BatchNorm2d(C)
for bs in [1, 4, 16]:
    x = torch.randn(bs, C, H, W)
    try:
        out = bn(x)
        print(f'  BatchNorm batch={bs}: {norm_stats(out)}')
    except Exception as e:
        print(f'  BatchNorm batch={bs}: ERROR')
```

> **GroupNorm for Small Batch Detection and Segmentation**: When training Mask R-CNN, DETR, or SegFormer with batch_size <= 4 per GPU, always replace BatchNorm with GroupNorm (G=32 or G=16). BN at small batch sizes produces noisy statistics that destabilize training. Freeze BN (via SyncBatchNorm or BatchNorm frozen=True) is another option when using pretrained backbones, but training new BN layers at small batch is not recommended.

## Relationship Between Normalization Methods

All four normalizations share the same computation structure but differ in which dimensions they normalize over. For a 4D tensor (B, C, H, W): BatchNorm normalizes over (B, H, W) per channel — statistics depend on all samples and all spatial positions for each channel. LayerNorm normalizes over (C, H, W) per sample — statistics depend on all channels and spatial positions per sample. GroupNorm normalizes over (C/G, H, W) per (sample, group). InstanceNorm normalizes over (H, W) per (sample, channel). This unifying view makes it easy to switch between normalizations in code.

- GN(G=1) = LayerNorm for image tensors (normalize over all C, H, W per sample).
- GN(G=C) = InstanceNorm (normalize over H, W per sample per channel).
- BN with batch_size=1 and spatial collapse = InstanceNorm (numerically equivalent but different API).
- All normalizations share the same affine transform: y = γx̂ + β with learned per-channel γ, β.
- SyncBatchNorm: allreduce batch statistics across GPUs — allows effective batch normalization even at small per-device batch sizes in distributed training.

Choosing the number of groups G in GroupNorm requires a tradeoff: fewer groups (small G) means larger group size and more stable statistics, but less fine-grained normalization. More groups (large G) gives finer-grained normalization but smaller per-group statistics. G=32 is the standard for detection and segmentation models. For narrow layers with fewer than 32 channels, use G=4 or G=8. The group size C/G should always be at least 8 to maintain reliable within-group statistics.

## Benchmark: Classification vs Detection

The benchmark below measures forward-pass wall-clock time across normalization methods at different batch sizes on a (B, 64, 32, 32) feature map. GN, LN, and IN are batch-size independent — their cost scales linearly with input size regardless of batch. BN adds overhead for running-stat updates during training. On GPU with fused kernels (cuDNN), BN benefits from highly optimized CUDA code paths at large batch sizes.

```python
import torch
import torch.nn as nn
import time

C, H, W = 64, 32, 32
norm_configs = [
    ('BatchNorm2d', nn.BatchNorm2d(C)),
    ('GroupNorm(G=32)', nn.GroupNorm(32, C)),
    ('GroupNorm(G=1/LN)', nn.GroupNorm(1, C)),
    ('InstanceNorm2d', nn.InstanceNorm2d(C, affine=True)),
]

print('=== Throughput benchmark (forward pass only, ms per call) ===')
for batch_size in [2, 8, 32]:
    print(f'\n  batch_size={batch_size}:')
    x = torch.randn(batch_size, C, H, W)
    for name, layer in norm_configs:
        times = []
        for _ in range(200):
            t0 = time.perf_counter()
            _ = layer(x)
            times.append((time.perf_counter() - t0) * 1000)
        avg = sum(times[20:]) / len(times[20:])  # skip warmup
        print(f'    {name:<25}: {avg:.3f} ms')
```

## Normalization Methods Reference Table

| Method | Normalizes Over | Batch Dependent | Train/Eval Gap | Typical Use Case |
| --- | --- | --- | --- | --- |
| BatchNorm | (B, H, W) per channel | Yes | Yes | Image classification, large batch (≥16) |
| LayerNorm | (C, H, W) per sample | No | No | Transformers, NLP, BERT, T5 |
| GroupNorm | (C/G, H, W) per (B, G) | No | No | Object detection, segmentation, small batch |
| InstanceNorm | (H, W) per (B, C) | No | No | Style transfer, CycleGAN, image-to-image |
| RMSNorm | Feature dim per sample (no mean) | No | No | LLM pre-training, LLaMA, Gemma, Mistral |

GroupNorm with G=32 is the recommended default for any vision task where batch size per GPU is 8 or fewer. For classification with large batches (≥32), BatchNorm remains competitive. Instance Normalization is specialized for style transfer and should not be used as a general-purpose replacement for BN or GN — removing per-instance statistics also removes discriminative information that classification tasks rely on.

---

