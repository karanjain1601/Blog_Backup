---
title: "RMSNorm — Simplified Layer Norm in LLaMA and Gemma"
slug: "rmsnorm"
description: "Derive RMSNorm by removing mean subtraction from LN, benchmark its speed advantage, implement LLaMA-style pre-norm transformer blocks, and verify when RMSNorm equals LN."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUk1TTm9ybSAoWmhhbmcgXHUwMDI2IFNlbm5yaWNoIDIwMTkpIHNpbXBsaWZpZXMgTGF5ZXIgTm9ybWFsaXphdGlvbiBieSByZW1vdmluZyB0aGUgbWVhbiBzdWJ0cmFjdGlvbiBzdGVwLCBrZWVwaW5nIG9ubHkgdGhlIHJvb3QtbWVhbi1zcXVhcmUgc2NhbGluZy4gVGhlIGludHVpdGlvbiDigJQgY2FsbGVkIHRoZSByZS1jZW50ZXJpbmcgaHlwb3RoZXNpcyDigJQgaXMgdGhhdCBtZWFuIHN1YnRyYWN0aW9uIGFkZHMgY29tcHV0ZSB3aXRob3V0IG1lYW5pbmdmdWwgYmVuZWZpdCBpbiBwcmFjdGljZSwgc2luY2UgdGhlIHNjYWxlIGFuZCBzaGlmdCBwYXJhbWV0ZXJzIM6zIGFuZCDOsiBjYW4gYWJzb3JiIGFueSBjZW50ZXJpbmcuIFJNU05vcm0gYWNoaWV2ZXMgMTDigJMxNSUgZmFzdGVyIGZvcndhcmQgYW5kIGJhY2t3YXJkIHBhc3NlcyB0aGFuIExheWVyTm9ybSBhbmQgaGFzIGJlY29tZSB0aGUgZGVmYXVsdCBub3JtYWxpemF0aW9uIGluIHZpcnR1YWxseSBhbGwgbW9kZXJuIGxhcmdlIGxhbmd1YWdlIG1vZGVscy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSTVNOb3JtIEZvcm11bGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJNU05vcm0gY29tcHV0ZXM6IFJNUyh4KSA9IOKImigoMS9uKSDOo+G1oiB44bWiwrIpIOKAlCB0aGUgcm9vdCBtZWFuIHNxdWFyZSBvZiB0aGUgaW5wdXQgKG5vIG1lYW4gc3VidHJhY3Rpb24pLiB4zILhtaIgPSB44bWiIC8gUk1TKHgpIOKAlCBkaXZpZGUgZWFjaCBlbGVtZW50IGJ5IHRoZSBSTVMuIHnhtaIgPSDOs+G1oiDCtyB4zILhtaIg4oCUIGFwcGx5IGEgbGVhcm5lZCBzY2FsZSDOsyAobm8gYmlhcyDOsikuIFRoZSBrZXkgZGlmZmVyZW5jZSBmcm9tIExheWVyTm9ybTogbm8gbWVhbiBjb21wdXRhdGlvbiwgbm8gc3VidHJhY3Rpb24sIG5vIM6yIHBhcmFtZXRlci4gVGhpcyByZW1vdmVzIHRoZSByZS1jZW50ZXJpbmcgb3BlcmF0aW9uIGVudGlyZWx5LCBrZWVwaW5nIG9ubHkgcmUtc2NhbGluZy4gVGhlIGdyYWRpZW50IGlzIGFsc28gc2ltcGxlcjog4oiCTC/iiIJ44bWiID0gKDEvUk1TKSDCtyBb4oiCTC/iiILFt+G1oiDCtyDOs+G1oiDiiJIgeMyC4bWiIMK3ICgxL24pIM6j4rG8IOKIgkwv4oiCxbfisbwgwrcgzrPisbwgwrcgeMyC4rG8XS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgcm1zbm9ybV9udW1weSh4LCBnYW1tYSwgZXBzPTFlLTYpOlxuICAgICMgUk1TIG92ZXIgdGhlIGxhc3QgZGltZW5zaW9uIChmZWF0dXJlIGRpbSlcbiAgICBybXMgPSBucC5zcXJ0KG5wLm1lYW4oeCAqKiAyLCBheGlzPS0xLCBrZWVwZGltcz1UcnVlKSArIGVwcylcbiAgICByZXR1cm4gZ2FtbWEgKiAoeCAvIHJtcylcblxuY2xhc3MgUk1TTm9ybShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW0sIGVwcz0xZS02KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZXBzID0gZXBzXG4gICAgICAgIHNlbGYud2VpZ2h0ID0gbm4uUGFyYW1ldGVyKHRvcmNoLm9uZXMoZGltKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcm1zID0geC5wb3coMikubWVhbihkaW09LTEsIGtlZXBkaW09VHJ1ZSkuYWRkKHNlbGYuZXBzKS5zcXJ0KClcbiAgICAgICAgcmV0dXJuIHNlbGYud2VpZ2h0ICogKHggLyBybXMpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuQiwgVCwgQyA9IDIsIDEwLCA2NFxueF9ucCA9IG5wLnJhbmRvbS5yYW5kbihCLCBULCBDKS5hc3R5cGUobnAuZmxvYXQzMilcbmdhbW1hX25wID0gbnAub25lcyhDLCBkdHlwZT1ucC5mbG9hdDMyKVxub3V0X25wID0gcm1zbm9ybV9udW1weSh4X25wLCBnYW1tYV9ucClcblxueF90b3JjaCA9IHRvcmNoLnRlbnNvcih4X25wKVxucm1zX3RvcmNoID0gUk1TTm9ybShDKVxub3V0X3RvcmNoID0gcm1zX3RvcmNoKHhfdG9yY2gpLmRldGFjaCgpLm51bXB5KClcblxucHJpbnQoZlx1MDAyN01heCBkaWZmIG51bXB5IHZzIFB5VG9yY2g6IHtucC5hYnMob3V0X25wIC0gb3V0X3RvcmNoKS5tYXgoKTouMmV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JNUyBvZiBvdXRwdXQgKHNob3VsZCB+MSk6IHtucC5zcXJ0KG5wLm1lYW4ob3V0X25wKioyLCBheGlzPS0xKSkubWVhbigpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3TWVhbiBvZiBvdXRwdXQgKG5vdCBmb3JjZWQgdG8gMCk6IHtvdXRfbnAubWVhbihheGlzPS0xKS5tZWFuKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb3RpdmF0aW9uIOKAlCBXaHkgUmVtb3ZlIE1lYW4gU3VidHJhY3Rpb24/In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcmUtY2VudGVyaW5nIGh5cG90aGVzaXMgc3RhdGVzIHRoYXQgdGhlIGxlYXJuZWQgYmlhcyDOsiBpbiBMYXllck5vcm0gY2FuIGFic29yYiBhbnkgY29uc3RhbnQgc2hpZnQsIG1ha2luZyBleHBsaWNpdCBtZWFuIHN1YnRyYWN0aW9uIHJlZHVuZGFudC4gRW1waXJpY2FsbHksIHJlbW92aW5nIG1lYW4gY29tcHV0YXRpb24gc2F2ZXMgbWVtb3J5IGJhbmR3aWR0aCBhbmQgYXJpdGhtZXRpYzogZm9yIGEgZmVhdHVyZSB2ZWN0b3Igb2YgZGltZW5zaW9uIGQsIExheWVyTm9ybSByZXF1aXJlcyB0d28gcGFzc2VzIChvbmUgZm9yIG1lYW4sIG9uZSBmb3IgdmFyaWFuY2UpOyBSTVNOb3JtIHJlcXVpcmVzIG9uZSBwYXNzICh2YXJpYW5jZSBhcm91bmQgemVybykuIFRoaXMgdHJhbnNsYXRlcyB0byBhcHByb3hpbWF0ZWx5IDEw4oCTMTUlIHdhbGwtY2xvY2sgc3BlZWR1cCBvbiBsYXJnZSB0ZW5zb3JzLCB3aGljaCBjb21wb3VuZHMgc2lnbmlmaWNhbnRseSBhY3Jvc3MgdGhvdXNhbmRzIG9mIHRyYW5zZm9ybWVyIGJsb2NrcyBpbiBMTE0gdHJhaW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdGltZVxuXG5kZXZpY2UgPSBcdTAwMjdjdWRhXHUwMDI3IGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcdTAwMjdjcHVcdTAwMjdcblxuY2xhc3MgUk1TTm9ybShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW0sIGVwcz0xZS02KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZXBzID0gZXBzXG4gICAgICAgIHNlbGYud2VpZ2h0ID0gbm4uUGFyYW1ldGVyKHRvcmNoLm9uZXMoZGltKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcm1zID0geC5wb3coMikubWVhbigtMSwga2VlcGRpbT1UcnVlKS5hZGQoc2VsZi5lcHMpLnNxcnQoKVxuICAgICAgICByZXR1cm4gc2VsZi53ZWlnaHQgKiAoeCAvIHJtcylcblxuQiwgVCwgQyA9IDMyLCAyMDQ4LCA0MDk2XG54ID0gdG9yY2gucmFuZG4oQiwgVCwgQywgZGV2aWNlPWRldmljZSlcbmxuID0gbm4uTGF5ZXJOb3JtKEMpLnRvKGRldmljZSlcbnJtcyA9IFJNU05vcm0oQykudG8oZGV2aWNlKVxuXG5kZWYgYmVuY2htYXJrKGZuLCB4LCBuPTUwKTpcbiAgICBmb3IgXyBpbiByYW5nZSg1KTogICMgd2FybXVwXG4gICAgICAgIGZuKHgpXG4gICAgaWYgZGV2aWNlID09IFx1MDAyN2N1ZGFcdTAwMjc6XG4gICAgICAgIHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGZvciBfIGluIHJhbmdlKG4pOlxuICAgICAgICBmbih4KVxuICAgIGlmIGRldmljZSA9PSBcdTAwMjdjdWRhXHUwMDI3OlxuICAgICAgICB0b3JjaC5jdWRhLnN5bmNocm9uaXplKClcbiAgICByZXR1cm4gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MCkgLyBuICogMTAwMFxuXG5sbl9tcyA9IGJlbmNobWFyayhsbiwgeClcbnJtc19tcyA9IGJlbmNobWFyayhybXMsIHgpXG5wcmludChmXHUwMDI3TGF5ZXJOb3JtIDoge2xuX21zOi4zZn0gbXNcdTAwMjcpXG5wcmludChmXHUwMDI3Uk1TTm9ybSAgIDoge3Jtc19tczouM2Z9IG1zXHUwMDI3KVxucHJpbnQoZlx1MDAyN1NwZWVkdXAgICA6IHtsbl9tcy9ybXNfbXM6LjJmfXhcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUk1TTm9ybSBpbiBNb2Rlcm4gTExNcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUk1TTm9ybSBoYXMgYmVjb21lIHRoZSBkZWZhdWx0IG5vcm1hbGl6YXRpb24gZm9yIG5lYXJseSBhbGwgb3Blbi13ZWlnaHQgTExNczogTExhTUEgMS8yLzMsIEdlbW1hIDEvMiwgTWlzdHJhbCwgTWl4dHJhbCwgRmFsY29uLCBRd2VuLCBhbmQgUGhpIGFsbCB1c2UgUk1TTm9ybSB3aXRoIFByZS1Ob3JtIHBsYWNlbWVudC4gVGhlIHN0YW5kYXJkIHBsYWNlbWVudCBpcyBiZWZvcmUgdGhlIGF0dGVudGlvbiBzdWJsYXllciBhbmQgYmVmb3JlIHRoZSBmZWVkLWZvcndhcmQgc3VibGF5ZXIg4oCUIHR3byBSTVNOb3JtIG9wZXJhdGlvbnMgcGVyIHRyYW5zZm9ybWVyIGJsb2NrLiBUaGUgZmluYWwgaGlkZGVuIHN0YXRlIGJlZm9yZSB0aGUgbGFuZ3VhZ2UgbW9kZWwgaGVhZCByZWNlaXZlcyBvbmUgYWRkaXRpb25hbCBSTVNOb3JtLiBMTGFNQSB1c2VzIM61PTFlLTU7IEdlbW1hIHVzZXMgzrU9MWUtNi4gVGhlIHdlaWdodCDOsyBpcyBpbml0aWFsaXplZCB0byAxLjAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFJNU05vcm0obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltLCBlcHM9MWUtNSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVwcyA9IGVwc1xuICAgICAgICBzZWxmLndlaWdodCA9IG5uLlBhcmFtZXRlcih0b3JjaC5vbmVzKGRpbSkpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJtcyA9IHgucG93KDIpLm1lYW4oLTEsIGtlZXBkaW09VHJ1ZSkuYWRkKHNlbGYuZXBzKS5zcXJ0KClcbiAgICAgICAgcmV0dXJuIHNlbGYud2VpZ2h0ICogKHggLyBybXMpXG5cbmNsYXNzIExMYU1BQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgbmhlYWQsIGRpbV9mZik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmF0dG4gPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oZF9tb2RlbCwgbmhlYWQsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZmYgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGRfbW9kZWwsIGRpbV9mZiwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5TaUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoZGltX2ZmLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICApXG4gICAgICAgIHNlbGYucm1zMSA9IFJNU05vcm0oZF9tb2RlbCkgICMgYmVmb3JlIGF0dGVudGlvblxuICAgICAgICBzZWxmLnJtczIgPSBSTVNOb3JtKGRfbW9kZWwpICAjIGJlZm9yZSBmZWVkLWZvcndhcmRcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgbjEgPSBzZWxmLnJtczEoeClcbiAgICAgICAgeCA9IHggKyBzZWxmLmF0dG4objEsIG4xLCBuMSlbMF1cbiAgICAgICAgeCA9IHggKyBzZWxmLmZmKHNlbGYucm1zMih4KSlcbiAgICAgICAgcmV0dXJuIHhcblxuZF9tb2RlbCwgbmhlYWQsIGRpbV9mZiA9IDEyOCwgNCwgNTEyXG5ibG9jayA9IExMYU1BQmxvY2soZF9tb2RlbCwgbmhlYWQsIGRpbV9mZilcbnggPSB0b3JjaC5yYW5kbigyLCAzMiwgZF9tb2RlbClcbm91dCA9IGJsb2NrKHgpXG5wcmludChmXHUwMDI3SW5wdXQgIG5vcm06IHt4Lm5vcm0oZGltPS0xKS5tZWFuKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdPdXRwdXQgbm9ybToge291dC5ub3JtKGRpbT0tMSkubWVhbigpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3UGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBibG9jay5wYXJhbWV0ZXJzKCkpOix9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUHJlLU5vcm0gUGxhY2VtZW50IGluIExMYU1BIiwiY29udGVudCI6IkluIExMYU1BLXN0eWxlIG1vZGVscywgUk1TTm9ybSBpcyBhcHBsaWVkIGJlZm9yZSBhdHRlbnRpb24gKGlucHV0X2xheWVybm9ybSkgYW5kIGJlZm9yZSB0aGUgZmVlZC1mb3J3YXJkIG5ldHdvcmsgKHBvc3RfYXR0ZW50aW9uX2xheWVybm9ybSkuIEEgZmluYWwgUk1TTm9ybSBpcyBhcHBsaWVkIHRvIHRoZSBsYXN0IGhpZGRlbiBzdGF0ZSBiZWZvcmUgdGhlIHVuZW1iZWRkaW5nIGxheWVyLiBObyBub3JtYWxpemF0aW9uIGlzIGFwcGxpZWQgdG8gdGhlIGVtYmVkZGluZyB0YWJsZSBvdXRwdXQgaXRzZWxmIGluIExMYU1BICh1bmxpa2UgQkVSVCkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2hlbiBEb2VzIE1lYW4gU3VidHJhY3Rpb24gTWF0dGVyPyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSWYgdGhlIGlucHV0IHRvIGEgbm9ybWFsaXphdGlvbiBsYXllciBoYXMgYSBzaWduaWZpY2FudCBub24temVybyBtZWFuIHNoaWZ0IChlLmcuLCBmcm9tIGEgYmlhc2VkIHJlc2lkdWFsIGFjY3VtdWxhdGlvbiksIExOXHUwMDI3cyBtZWFuIHN1YnRyYWN0aW9uIGNvcnJlY3RzIGl0IHdoaWxlIFJNU05vcm0gbGVhdmVzIHRoZSBzaGlmdCBmb3IgzrMgYW5kIM6yIHRvIGhhbmRsZS4gSW4gcHJhY3RpY2UsIHByZS1ub3JtIHBsYWNlbWVudCBtZWFucyB0aGUgcmVzaWR1YWwgc3RyZWFtIGlzIHJlLW5vcm1hbGl6ZWQgZnJlcXVlbnRseSwgYW5kIHRoZSBtZWFuIHNoaWZ0IGFjY3VtdWxhdGVzIHZlcnkgc2xvd2x5LiBFbXBpcmljYWwgcmVzdWx0cyBhY3Jvc3MgTExhTUEsIEdlbW1hLCBhbmQgTWlzdHJhbCB0cmFpbmluZyBzaG93IHRoYXQgUk1TTm9ybSBtYXRjaGVzIExOIHBlcnBsZXhpdHkgdG8gd2l0aGluIDAuMeKAkzAuNSUgb24gc3RhbmRhcmQgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgUk1TTm9ybShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW0sIGVwcz0xZS02KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYud2VpZ2h0ID0gbm4uUGFyYW1ldGVyKHRvcmNoLm9uZXMoZGltKSlcbiAgICAgICAgc2VsZi5lcHMgPSBlcHNcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYud2VpZ2h0ICogeCAvIHgucG93KDIpLm1lYW4oLTEsIGtlZXBkaW09VHJ1ZSkuYWRkKHNlbGYuZXBzKS5zcXJ0KClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmRpbSA9IDI1NlxuXG4jIENhc2UgMTogemVyby1tZWFuIGlucHV0IOKAlCBSTVNOb3JtIGFuZCBMTiBzaG91bGQgYWdyZWVcbnhfemVyb21lYW4gPSB0b3JjaC5yYW5kbigxNiwgZGltKSAgIyBzdGFuZGFyZCBub3JtYWwgaXMgemVyby1tZWFuXG5sbiA9IG5uLkxheWVyTm9ybShkaW0pXG5ybXMgPSBSTVNOb3JtKGRpbSlcbm91dF9sbiAgPSBsbih4X3plcm9tZWFuKVxub3V0X3JtcyA9IHJtcyh4X3plcm9tZWFuKVxuZGlmZl96ZXJvbWVhbiA9IChvdXRfbG4gLSBvdXRfcm1zKS5hYnMoKS5tZWFuKCkuaXRlbSgpXG5cbiMgQ2FzZSAyOiBzaGlmdGVkIGlucHV0IOKAlCBMTiBjb3JyZWN0cyBzaGlmdCwgUk1TTm9ybSBkb2VzIG5vdFxueF9zaGlmdGVkID0geF96ZXJvbWVhbiArIDUuMCAgIyBhZGQgY29uc3RhbnQgc2hpZnRcbm91dF9sbjIgID0gbG4oeF9zaGlmdGVkKVxub3V0X3JtczIgPSBybXMoeF9zaGlmdGVkKVxuZGlmZl9zaGlmdGVkID0gKG91dF9sbjIgLSBvdXRfcm1zMikuYWJzKCkubWVhbigpLml0ZW0oKVxuXG5wcmludChmXHUwMDI3WmVyby1tZWFuIGlucHV0ICDigJQgTE4gdnMgUk1TTm9ybSBtZWFuIGFicyBkaWZmOiB7ZGlmZl96ZXJvbWVhbjouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1NoaWZ0ZWQgaW5wdXQgKCs1KSDigJQgTE4gdnMgUk1TTm9ybSBtZWFuIGFicyBkaWZmOiB7ZGlmZl9zaGlmdGVkOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdSTVNOb3JtIG1hdGNoZXMgTE4gY2xvc2VseSBmb3IgemVyby1tZWFuIGlucHV0cyAodHlwaWNhbCBhZnRlciBub3JtYWxpemF0aW9uKS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgYW5kIE51bWVyaWNhbCBQcm9wZXJ0aWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgUk1TTm9ybSBiYWNrd2FyZCBwYXNzIGlzIHNpbXBsZXIgdGhhbiBMYXllck5vcm06IHRoZXJlIGlzIG5vIGNlbnRlcmluZyB0ZXJtIGluIHRoZSBncmFkaWVudC4gVGhlIGdyYWRpZW50IOKIgkwv4oiCeCBoYXMgdGhlIGZvcm0gKM6z4bWiL1JNUykgwrcgW+KIgkwv4oiCxbfhtaIg4oiSIHjMguG1oiDCtyBtZWFuKOKIgkwv4oiCxbfisbwgwrcgeMyC4rG8KV0g4oCUIGEgc2luZ2xlIGRvdC1wcm9kdWN0IGNvcnJlY3Rpb24gaW5zdGVhZCBvZiBMYXllck5vcm1cdTAwMjdzIHR3byBjb3JyZWN0aW9uIHRlcm1zLiBUaGUgzrUgdmFsdWUgbWF0dGVyczogTExhTUEgdXNlcyAxZS01LCBHZW1tYSB1c2VzIDFlLTYuIFRvbyBzbWFsbCBhbiDOtSBjYXVzZXMgTmFOIHdoZW4gaW5wdXRzIGhhdmUgbmVhci16ZXJvIG1hZ25pdHVkZTsgdG9vIGxhcmdlIGJpYXNlcyB0aGUgbm9ybWFsaXphdGlvbi4gSW4gYmZsb2F0MTYgdHJhaW5pbmcsIM61IGlzIHNvbWV0aW1lcyBpbmNyZWFzZWQgdG8gMWUtNSBvciBoaWdoZXIgZm9yIG51bWVyaWNhbCBzYWZldHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW1wbGVtZW50YXRpb24gRGV0YWlscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRnVzZWQgUk1TTm9ybSBrZXJuZWxzIChhdmFpbGFibGUgaW4gRmxhc2hBdHRlbnRpb24gYW5kIEFwZXgpIGNvbXB1dGUgdGhlIG5vcm1hbGl6YXRpb24gaW4gYSBzaW5nbGUgR1BVIGtlcm5lbCBwYXNzLCBlbGltaW5hdGluZyB0aGUgbWVtb3J5IGJhbmR3aWR0aCBib3R0bGVuZWNrIG9mIHJlYWRpbmcgeCB0d2ljZS4gVGhlIHdlaWdodCDOsyBpcyB0eXBpY2FsbHkgc3RvcmVkIGluIGZwMzIgZXZlbiB3aGVuIHRoZSBhY3RpdmF0aW9ucyBhcmUgaW4gYmYxNiwgdG8gbWFpbnRhaW4gcHJlY2lzaW9uIGluIHRoZSBzY2FsZSBwYXJhbWV0ZXJzLiBIdWdnaW5nIEZhY2UgVHJhbnNmb3JtZXJzIGltcGxlbWVudHMgTGxhbWFSTVNOb3JtIHdpdGggYW4gdXBjYXN0IHRvIGZwMzIgZm9yIHRoZSBub3JtYWxpemF0aW9uIGNvbXB1dGF0aW9uLCBkb3duY2FzdCBiYWNrIHRvIHRoZSBhY3RpdmF0aW9uIGR0eXBlIGZvciBvdXRwdXQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJObyDOsiBwYXJhbWV0ZXI6IFJNU05vcm0gaGFzIG9ubHkgzrMgKHNjYWxlKSwgbm90IM6yIChzaGlmdCkg4oCUIHRoaXMgc2F2ZXMgcGFyYW1ldGVycyBhbmQgc2xpZ2h0bHkgc2ltcGxpZmllcyB0aGUgY29tcHV0YXRpb24gZ3JhcGguIiwiRnVzZWQga2VybmVsczogdXNlIGFwZXgubm9ybWFsaXphdGlvbi5GdXNlZFJNU05vcm0gb3IgZmxhc2hfYXR0bi5vcHMucm1zX25vcm0gZm9yIG1heGltdW0gdGhyb3VnaHB1dC4iLCJVcGNhc3QgdG8gZnAzMjogdGhlIHBvdy9tZWFuL3NxcnQgc2VxdWVuY2UgaXMgbnVtZXJpY2FsbHkgc2FmZXIgaW4gZnAzMiBldmVuIHdoZW4gYWN0aXZhdGlvbnMgYXJlIGJmMTYuIiwizrUgdHVuaW5nOiBpbmNyZWFzZSDOtSB0byAxZS01IGlmIHlvdSBzZWUgTmFOIGxvc3NlcyBpbiB0aGUgZmlyc3QgZmV3IHN0ZXBzIG9mIHRyYWluaW5nIHdpdGggYmYxNiBwcmVjaXNpb24uIiwiSW5pdGlhbGl6YXRpb246IM6zIGluaXRpYWxpemVkIHRvIDEuMCAob25lcyksIHdoaWNoIG1lYW5zIHRoZSBsYXllciBpcyBhbiBpZGVudGl0eSBtYXAgYXQgaW5pdGlhbGl6YXRpb24uIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxOIHZzIFJNU05vcm0gdnMgQk4gQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIkxheWVyTm9ybSIsIlJNU05vcm0iLCJCYXRjaE5vcm0iXSwicm93cyI6W1siRm9ybXVsYSIsInjMgj0oeOKIks68KS/PgywgeT3Os3jMgivOsiIsInjMgj14L1JNUyh4KSwgeT3Os3jMgiIsInjMgj0oeOKIks68X0IpL8+DX0IsIHk9zrN4zIIrzrIiXSxbIk1lYW4gc3VidHJhY3Rpb24iLCJZZXMiLCJObyIsIlllcyAob3ZlciBiYXRjaCkiXSxbIkxlYXJuYWJsZSBwYXJhbXMiLCLOsyBhbmQgzrIgcGVyIGZlYXR1cmUiLCLOsyBwZXIgZmVhdHVyZSBvbmx5IiwizrMgYW5kIM6yIHBlciBmZWF0dXJlIl0sWyJDb21wdXRlIGNvc3QgKHJlbGF0aXZlKSIsIjEuMMOXIiwifjAuODXigJMwLjkww5ciLCIxLjDDlyAoKyBydW5uaW5nIHN0YXRzKSJdLFsiQmF0Y2ggZGVwZW5kZW5jZSIsIk5vbmUiLCJOb25lIiwiWWVzIOKAlCB0cmFpbi9ldmFsIGdhcCJdLFsiVXNlZCBpbiIsIkJFUlQsIFQ1LCBHUFQtMiAoZWFybHkpIiwiTExhTUEsIEdlbW1hLCBNaXN0cmFsLCBGYWxjb24iLCJSZXNOZXQsIEVmZmljaWVudE5ldCwgVkdHIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBuZXcgVHJhbnNmb3JtZXItYmFzZWQgbW9kZWxzLCBSTVNOb3JtIGlzIHRoZSByZWNvbW1lbmRlZCBkZWZhdWx0LiBJdCBkZWxpdmVycyB0aGUgc2FtZSBlbXBpcmljYWwgcGVyZm9ybWFuY2UgYXMgTGF5ZXJOb3JtIHdpdGggbG93ZXIgY29tcHV0ZSBjb3N0LiBMYXllck5vcm0gcmVtYWlucyBhcHByb3ByaWF0ZSB3aGVuIGxvYWRpbmcgcHJldHJhaW5lZCBjaGVja3BvaW50cyB0aGF0IHVzZWQgaXQgKEJFUlQsIFQ1LCBlYXJseSBHUFQtMikuIEJhdGNoTm9ybSBpcyBpbmFwcHJvcHJpYXRlIGZvciBhdXRvcmVncmVzc2l2ZSBsYW5ndWFnZSBtb2RlbHMgYW5kIHNlcXVlbmNlIG1vZGVscyB3aXRoIHZhcmlhYmxlIGxlbmd0aHMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# RMSNorm — Simplified Layer Norm in LLaMA and Gemma

RMSNorm (Zhang & Sennrich 2019) simplifies Layer Normalization by removing the mean subtraction step, keeping only the root-mean-square scaling. The intuition — called the re-centering hypothesis — is that mean subtraction adds compute without meaningful benefit in practice, since the scale and shift parameters γ and β can absorb any centering. RMSNorm achieves 10–15% faster forward and backward passes than LayerNorm and has become the default normalization in virtually all modern large language models.

## RMSNorm Formula

RMSNorm computes: RMS(x) = √((1/n) Σᵢ xᵢ²) — the root mean square of the input (no mean subtraction). x̂ᵢ = xᵢ / RMS(x) — divide each element by the RMS. yᵢ = γᵢ · x̂ᵢ — apply a learned scale γ (no bias β). The key difference from LayerNorm: no mean computation, no subtraction, no β parameter. This removes the re-centering operation entirely, keeping only re-scaling. The gradient is also simpler: ∂L/∂xᵢ = (1/RMS) · [∂L/∂ŷᵢ · γᵢ − x̂ᵢ · (1/n) Σⱼ ∂L/∂ŷⱼ · γⱼ · x̂ⱼ].

```python
import numpy as np
import torch
import torch.nn as nn

def rmsnorm_numpy(x, gamma, eps=1e-6):
    # RMS over the last dimension (feature dim)
    rms = np.sqrt(np.mean(x ** 2, axis=-1, keepdims=True) + eps)
    return gamma * (x / rms)

class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x):
        rms = x.pow(2).mean(dim=-1, keepdim=True).add(self.eps).sqrt()
        return self.weight * (x / rms)

np.random.seed(42)
B, T, C = 2, 10, 64
x_np = np.random.randn(B, T, C).astype(np.float32)
gamma_np = np.ones(C, dtype=np.float32)
out_np = rmsnorm_numpy(x_np, gamma_np)

x_torch = torch.tensor(x_np)
rms_torch = RMSNorm(C)
out_torch = rms_torch(x_torch).detach().numpy()

print(f'Max diff numpy vs PyTorch: {np.abs(out_np - out_torch).max():.2e}')
print(f'RMS of output (should ~1): {np.sqrt(np.mean(out_np**2, axis=-1)).mean():.4f}')
print(f'Mean of output (not forced to 0): {out_np.mean(axis=-1).mean():.4f}')
```

## Motivation — Why Remove Mean Subtraction?

The re-centering hypothesis states that the learned bias β in LayerNorm can absorb any constant shift, making explicit mean subtraction redundant. Empirically, removing mean computation saves memory bandwidth and arithmetic: for a feature vector of dimension d, LayerNorm requires two passes (one for mean, one for variance); RMSNorm requires one pass (variance around zero). This translates to approximately 10–15% wall-clock speedup on large tensors, which compounds significantly across thousands of transformer blocks in LLM training.

```python
import torch
import torch.nn as nn
import time

device = 'cuda' if torch.cuda.is_available() else 'cpu'

class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x):
        rms = x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt()
        return self.weight * (x / rms)

B, T, C = 32, 2048, 4096
x = torch.randn(B, T, C, device=device)
ln = nn.LayerNorm(C).to(device)
rms = RMSNorm(C).to(device)

def benchmark(fn, x, n=50):
    for _ in range(5):  # warmup
        fn(x)
    if device == 'cuda':
        torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(n):
        fn(x)
    if device == 'cuda':
        torch.cuda.synchronize()
    return (time.perf_counter() - t0) / n * 1000

ln_ms = benchmark(ln, x)
rms_ms = benchmark(rms, x)
print(f'LayerNorm : {ln_ms:.3f} ms')
print(f'RMSNorm   : {rms_ms:.3f} ms')
print(f'Speedup   : {ln_ms/rms_ms:.2f}x')
```

## RMSNorm in Modern LLMs

RMSNorm has become the default normalization for nearly all open-weight LLMs: LLaMA 1/2/3, Gemma 1/2, Mistral, Mixtral, Falcon, Qwen, and Phi all use RMSNorm with Pre-Norm placement. The standard placement is before the attention sublayer and before the feed-forward sublayer — two RMSNorm operations per transformer block. The final hidden state before the language model head receives one additional RMSNorm. LLaMA uses ε=1e-5; Gemma uses ε=1e-6. The weight γ is initialized to 1.0.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x):
        rms = x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt()
        return self.weight * (x / rms)

class LLaMABlock(nn.Module):
    def __init__(self, d_model, nhead, dim_ff):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, nhead, batch_first=True)
        self.ff = nn.Sequential(
            nn.Linear(d_model, dim_ff, bias=False),
            nn.SiLU(),
            nn.Linear(dim_ff, d_model, bias=False)
        )
        self.rms1 = RMSNorm(d_model)  # before attention
        self.rms2 = RMSNorm(d_model)  # before feed-forward
    def forward(self, x):
        n1 = self.rms1(x)
        x = x + self.attn(n1, n1, n1)[0]
        x = x + self.ff(self.rms2(x))
        return x

d_model, nhead, dim_ff = 128, 4, 512
block = LLaMABlock(d_model, nhead, dim_ff)
x = torch.randn(2, 32, d_model)
out = block(x)
print(f'Input  norm: {x.norm(dim=-1).mean():.4f}')
print(f'Output norm: {out.norm(dim=-1).mean():.4f}')
print(f'Params: {sum(p.numel() for p in block.parameters()):,}')
```

> **Pre-Norm Placement in LLaMA**: In LLaMA-style models, RMSNorm is applied before attention (input_layernorm) and before the feed-forward network (post_attention_layernorm). A final RMSNorm is applied to the last hidden state before the unembedding layer. No normalization is applied to the embedding table output itself in LLaMA (unlike BERT).

## When Does Mean Subtraction Matter?

If the input to a normalization layer has a significant non-zero mean shift (e.g., from a biased residual accumulation), LN's mean subtraction corrects it while RMSNorm leaves the shift for γ and β to handle. In practice, pre-norm placement means the residual stream is re-normalized frequently, and the mean shift accumulates very slowly. Empirical results across LLaMA, Gemma, and Mistral training show that RMSNorm matches LN perplexity to within 0.1–0.5% on standard benchmarks.

```python
import torch
import torch.nn as nn

class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-6):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(dim))
        self.eps = eps
    def forward(self, x):
        return self.weight * x / x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt()

torch.manual_seed(0)
dim = 256

# Case 1: zero-mean input — RMSNorm and LN should agree
x_zeromean = torch.randn(16, dim)  # standard normal is zero-mean
ln = nn.LayerNorm(dim)
rms = RMSNorm(dim)
out_ln  = ln(x_zeromean)
out_rms = rms(x_zeromean)
diff_zeromean = (out_ln - out_rms).abs().mean().item()

# Case 2: shifted input — LN corrects shift, RMSNorm does not
x_shifted = x_zeromean + 5.0  # add constant shift
out_ln2  = ln(x_shifted)
out_rms2 = rms(x_shifted)
diff_shifted = (out_ln2 - out_rms2).abs().mean().item()

print(f'Zero-mean input  — LN vs RMSNorm mean abs diff: {diff_zeromean:.4f}')
print(f'Shifted input (+5) — LN vs RMSNorm mean abs diff: {diff_shifted:.4f}')
print('RMSNorm matches LN closely for zero-mean inputs (typical after normalization).')
```

## Gradient and Numerical Properties

The RMSNorm backward pass is simpler than LayerNorm: there is no centering term in the gradient. The gradient ∂L/∂x has the form (γᵢ/RMS) · [∂L/∂ŷᵢ − x̂ᵢ · mean(∂L/∂ŷⱼ · x̂ⱼ)] — a single dot-product correction instead of LayerNorm's two correction terms. The ε value matters: LLaMA uses 1e-5, Gemma uses 1e-6. Too small an ε causes NaN when inputs have near-zero magnitude; too large biases the normalization. In bfloat16 training, ε is sometimes increased to 1e-5 or higher for numerical safety.

## Implementation Details

Fused RMSNorm kernels (available in FlashAttention and Apex) compute the normalization in a single GPU kernel pass, eliminating the memory bandwidth bottleneck of reading x twice. The weight γ is typically stored in fp32 even when the activations are in bf16, to maintain precision in the scale parameters. Hugging Face Transformers implements LlamaRMSNorm with an upcast to fp32 for the normalization computation, downcast back to the activation dtype for output.

- No β parameter: RMSNorm has only γ (scale), not β (shift) — this saves parameters and slightly simplifies the computation graph.
- Fused kernels: use apex.normalization.FusedRMSNorm or flash_attn.ops.rms_norm for maximum throughput.
- Upcast to fp32: the pow/mean/sqrt sequence is numerically safer in fp32 even when activations are bf16.
- ε tuning: increase ε to 1e-5 if you see NaN losses in the first few steps of training with bf16 precision.
- Initialization: γ initialized to 1.0 (ones), which means the layer is an identity map at initialization.

## LN vs RMSNorm vs BN Comparison

| Property | LayerNorm | RMSNorm | BatchNorm |
| --- | --- | --- | --- |
| Formula | x̂=(x−μ)/σ, y=γx̂+β | x̂=x/RMS(x), y=γx̂ | x̂=(x−μ_B)/σ_B, y=γx̂+β |
| Mean subtraction | Yes | No | Yes (over batch) |
| Learnable params | γ and β per feature | γ per feature only | γ and β per feature |
| Compute cost (relative) | 1.0× | ~0.85–0.90× | 1.0× (+ running stats) |
| Batch dependence | None | None | Yes — train/eval gap |
| Used in | BERT, T5, GPT-2 (early) | LLaMA, Gemma, Mistral, Falcon | ResNet, EfficientNet, VGG |

For new Transformer-based models, RMSNorm is the recommended default. It delivers the same empirical performance as LayerNorm with lower compute cost. LayerNorm remains appropriate when loading pretrained checkpoints that used it (BERT, T5, early GPT-2). BatchNorm is inappropriate for autoregressive language models and sequence models with variable lengths.

---

