---
title: "DistilBERT and TinyBERT — BERT Compression via Distillation"
slug: "distilbert-tinybert"
description: "DistilBERT distills BERT-base into a 6-layer model using MLM, cosine, and soft-CE losses. TinyBERT extends this with layer-wise attention and hidden state distillation in two stages. Covers every-other-layer mapping, attention matrix transfer, two-stage distillation, and comparison on GLUE."
tags: ["deep-learning", "model-compression", "pruning", "quantization"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkVSVC1iYXNlIGhhcyAxMTBNIHBhcmFtZXRlcnMsIDEyIGxheWVycywgYW5kIGEgNzY4LWRpbWVuc2lvbmFsIGhpZGRlbiBzdGF0ZS4gRm9yIG1hbnkgcHJvZHVjdGlvbiB1c2UgY2FzZXMgaXQgaXMgdG9vIGxhcmdlOiB0b28gc2xvdyBmb3IgcmVhbC10aW1lIGluZmVyZW5jZSwgdG9vIGV4cGVuc2l2ZSB0byBzZXJ2ZSBhdCBzY2FsZSwgYW5kIHRvbyBtZW1vcnktaW50ZW5zaXZlIGZvciBvbi1kZXZpY2UgZGVwbG95bWVudC4gRGlzdGlsQkVSVCBhbmQgVGlueUJFUlQgY29tcHJlc3MgQkVSVCB2aWEga25vd2xlZGdlIGRpc3RpbGxhdGlvbiDigJQgdHJhaW5pbmcgYSBzbWFsbGVyIHN0dWRlbnQgbW9kZWwgdG8gbWltaWMgdGhlIGxhcmdlciB0ZWFjaGVyIOKAlCByZXRhaW5pbmcgOTbigJM5NyUgb2YgQkVSVFx1MDAyN3MgR0xVRSBzY29yZSBhdCA0MOKAkzYwJSBvZiBpdHMgc2l6ZSBhbmQgbGF0ZW5jeS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEaXN0aWxCRVJUIOKAlCBUYXNrLUFnbm9zdGljIFByZXRyYWluaW5nIERpc3RpbGxhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlzdGlsQkVSVCAoU2FuaCBldCBhbC4gMjAxOSkgZGlzdGlsbHMgQkVSVC1iYXNlIGR1cmluZyBwcmV0cmFpbmluZywgbm90IGZpbmUtdHVuaW5nLiBUaGUgc3R1ZGVudCBoYXMgNiBsYXllcnMgKGhhbGYgb2YgQkVSVC1iYXNlXHUwMDI3cyAxMiksIHNhbWUgaGlkZGVuIGRpbSAoNzY4KSBhbmQgaGVhZCBjb3VudCAoMTIpLCBidXQgbm8gdG9rZW4tdHlwZSBlbWJlZGRpbmdzIGFuZCBubyBwb29sZXIuIFRoZSB0ZWFjaGVyIGlzIEJFUlQtYmFzZSB0cmFpbmVkIG9uIHRoZSBzYW1lIE1MTSBjb3JwdXMuIFRocmVlIGxvc3MgdGVybXMgYXJlIGNvbWJpbmVkOiAoMSkgTF9NTE0g4oCUIHN0dWRlbnRcdTAwMjdzIG1hc2tlZCBsYW5ndWFnZSBtb2RlbCBsb3NzIG9uIHRydWUgbGFiZWxzOyAoMikgTF9jb3Mg4oCUIGNvc2luZSBzaW1pbGFyaXR5IGJldHdlZW4gc3R1ZGVudCBhbmQgdGVhY2hlciBoaWRkZW4gc3RhdGVzIGF0IHRoZSBsYXN0IGxheWVyOyAoMykgTF9DRSDigJQgY3Jvc3MtZW50cm9weSBvZiBzdHVkZW50IG91dHB1dHMgYWdhaW5zdCB0ZWFjaGVyXHUwMDI3cyBzb2Z0IHByb2JhYmlsaXR5IGRpc3RyaWJ1dGlvbiB3aXRoIHRlbXBlcmF0dXJlIFQ9NC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGRpc3RpbGJlcnRfZGlzdGlsbGF0aW9uX2xvc3MoXG4gICAgc3R1ZGVudF9sb2dpdHM6IHRvcmNoLlRlbnNvciwgICAgIyAoQiwgc2VxX2xlbiwgdm9jYWJfc2l6ZSlcbiAgICB0ZWFjaGVyX2xvZ2l0czogdG9yY2guVGVuc29yLCAgICAjIChCLCBzZXFfbGVuLCB2b2NhYl9zaXplKVxuICAgIHN0dWRlbnRfaGlkZGVuOiB0b3JjaC5UZW5zb3IsICAgICMgKEIsIHNlcV9sZW4sIGhpZGRlbilcbiAgICB0ZWFjaGVyX2hpZGRlbjogdG9yY2guVGVuc29yLCAgICAjIChCLCBzZXFfbGVuLCBoaWRkZW4pXG4gICAgdHJ1ZV9sYWJlbHM6IHRvcmNoLlRlbnNvciwgICAgICAgIyAoQiwgc2VxX2xlbikg4oCUIC0xMDAgZm9yIG5vbi1tYXNrZWQgdG9rZW5zXG4gICAgdGVtcGVyYXR1cmU6IGZsb2F0ID0gNC4wLFxuICAgIGFscGhhX21sbTogZmxvYXQgPSAwLjMzLFxuICAgIGFscGhhX2NvczogZmxvYXQgPSAwLjMzLFxuICAgIGFscGhhX2tkOiBmbG9hdCA9IDAuMzQsXG4pIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlRocmVlLWNvbXBvbmVudCBEaXN0aWxCRVJUIGRpc3RpbGxhdGlvbiBsb3NzLlwiXCJcIlxuICAgICMgMS4gTUxNIGxvc3MgKHN0dWRlbnQgdnMgdHJ1ZSBsYWJlbHMpXG4gICAgbWxtX2xvc3MgPSBGLmNyb3NzX2VudHJvcHkoXG4gICAgICAgIHN0dWRlbnRfbG9naXRzLnZpZXcoLTEsIHN0dWRlbnRfbG9naXRzLnNpemUoLTEpKSxcbiAgICAgICAgdHJ1ZV9sYWJlbHMudmlldygtMSksXG4gICAgICAgIGlnbm9yZV9pbmRleD0tMTAwXG4gICAgKVxuXG4gICAgIyAyLiBDb3NpbmUgc2ltaWxhcml0eSBsb3NzIG9uIGhpZGRlbiBzdGF0ZXNcbiAgICAjIENvc2luZSBkaXN0YW5jZSA9IDEgLSBjb3NpbmVfc2ltaWxhcml0eSwgbWluaW1pc2UgdGhpc1xuICAgIGNvc19sb3NzID0gKDEgLSBGLmNvc2luZV9zaW1pbGFyaXR5KHN0dWRlbnRfaGlkZGVuLCB0ZWFjaGVyX2hpZGRlbiwgZGltPS0xKSkubWVhbigpXG5cbiAgICAjIDMuIFNvZnQgY3Jvc3MtZW50cm9weSAoS0QpIGF0IHRlbXBlcmF0dXJlIFRcbiAgICBUID0gdGVtcGVyYXR1cmVcbiAgICBzb2Z0X3RlYWNoZXIgPSBGLnNvZnRtYXgodGVhY2hlcl9sb2dpdHMgLyBULCBkaW09LTEpXG4gICAgbG9nX3NvZnRfc3R1ZGVudCA9IEYubG9nX3NvZnRtYXgoc3R1ZGVudF9sb2dpdHMgLyBULCBkaW09LTEpXG4gICAgIyBPbmx5IGNvbXB1dGUgb24gbWFza2VkIHBvc2l0aW9ucyAod2hlcmUgdHJ1ZV9sYWJlbHMgIT0gLTEwMClcbiAgICBtYXNrID0gKHRydWVfbGFiZWxzICE9IC0xMDApLnVuc3F1ZWV6ZSgtMSkuZXhwYW5kX2FzKHNvZnRfdGVhY2hlcilcbiAgICBrZF9sb3NzID0gRi5rbF9kaXYobG9nX3NvZnRfc3R1ZGVudFttYXNrXS52aWV3KC0xLCBzb2Z0X3RlYWNoZXIuc2l6ZSgtMSkpLFxuICAgICAgICAgICAgICAgICAgICAgICAgc29mdF90ZWFjaGVyW21hc2tdLnZpZXcoLTEsIHNvZnRfdGVhY2hlci5zaXplKC0xKSksXG4gICAgICAgICAgICAgICAgICAgICAgICByZWR1Y3Rpb249XHUwMDI3YmF0Y2htZWFuXHUwMDI3KSAqIChUICoqIDIpXG5cbiAgICB0b3RhbCA9IGFscGhhX21sbSAqIG1sbV9sb3NzICsgYWxwaGFfY29zICogY29zX2xvc3MgKyBhbHBoYV9rZCAqIGtkX2xvc3NcbiAgICByZXR1cm4gdG90YWwsIHtcdTAwMjdtbG1cdTAwMjc6IG1sbV9sb3NzLml0ZW0oKSwgXHUwMDI3Y29zXHUwMDI3OiBjb3NfbG9zcy5pdGVtKCksIFx1MDAyN2tkXHUwMDI3OiBrZF9sb3NzLml0ZW0oKX0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFdmVyeS1PdGhlci1MYXllciBNYXBwaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaXN0aWxCRVJUIGluaXRpYWxpemVzIHN0dWRlbnQgbGF5ZXIgaSBmcm9tIHRlYWNoZXIgbGF5ZXIgMmkgKGV2ZXJ5IG90aGVyIHRlYWNoZXIgbGF5ZXIpLiBXaXRoIDYgc3R1ZGVudCBsYXllcnM6IHN0dWRlbnRbMF0g4oaQIHRlYWNoZXJbMV0sIHN0dWRlbnRbMV0g4oaQIHRlYWNoZXJbM10sIC4uLiwgc3R1ZGVudFs1XSDihpAgdGVhY2hlclsxMV0uIFRoaXMgaW5pdGlhbGl6YXRpb24gZ2l2ZXMgdGhlIHN0dWRlbnQgYSBzdHJvbmcgc3RhcnRpbmcgcG9pbnQgYW5kIGlzIHBhcnRpYWxseSByZXNwb25zaWJsZSBmb3IgRGlzdGlsQkVSVFx1MDAyN3MgZWZmaWNpZW5jeSDigJQgdGhlIHByZS10cmFpbmluZyBkaXN0aWxsYXRpb24gaXMgc2hvcnQgYmVjYXVzZSBtb3N0IG9mIHRoZSBrbm93bGVkZ2UgaXMgYWxyZWFkeSBwcmVzZW50IGluIHRoZSBpbml0aWFsaXplZCB3ZWlnaHRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEJlcnRNb2RlbCwgQmVydENvbmZpZ1xuXG5kZWYgaW5pdGlhbGl6ZV9kaXN0aWxiZXJ0X2Zyb21fYmVydCh0ZWFjaGVyX2JlcnQ6IEJlcnRNb2RlbCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5fc3R1ZGVudF9sYXllcnM6IGludCA9IDYpIC1cdTAwM2Ugbm4uTW9kdWxlTGlzdDpcbiAgICBcIlwiXCJcbiAgICBDb3B5IGV2ZXJ5LW90aGVyIHRlYWNoZXIgbGF5ZXIgaW50byBzdHVkZW50LlxuICAgIFRlYWNoZXI6IDEyIGxheWVycy4gU3R1ZGVudDogNiBsYXllcnMuXG4gICAgTWFwcGluZzogc3R1ZGVudFtpXSBcdTAwM2MtIHRlYWNoZXJbMippICsgMV0gKDEtaW5kZXhlZCB0ZWFjaGVyIGxheWVycykuXG4gICAgXCJcIlwiXG4gICAgdGVhY2hlcl9sYXllcnMgPSB0ZWFjaGVyX2JlcnQuZW5jb2Rlci5sYXllciAgIyBNb2R1bGVMaXN0IG9mIDEyIEJlcnRMYXllclxuICAgIHN0dWRlbnRfbGF5ZXJzID0gbm4uTW9kdWxlTGlzdCgpXG5cbiAgICBmb3IgaSBpbiByYW5nZShuX3N0dWRlbnRfbGF5ZXJzKTpcbiAgICAgICAgdGVhY2hlcl9pZHggPSAyICogaSArIDEgICMgMSwgMywgNSwgNywgOSwgMTFcbiAgICAgICAgaWYgdGVhY2hlcl9pZHggXHUwMDNlPSBsZW4odGVhY2hlcl9sYXllcnMpOlxuICAgICAgICAgICAgdGVhY2hlcl9pZHggPSBsZW4odGVhY2hlcl9sYXllcnMpIC0gMVxuICAgICAgICAjIERlZXAgY29weSB0aGUgdGVhY2hlciBsYXllclx1MDAyN3Mgc3RhdGUgZGljdCBpbnRvIGEgbmV3IGxheWVyXG4gICAgICAgIGltcG9ydCBjb3B5XG4gICAgICAgIHN0dWRlbnRfbGF5ZXIgPSBjb3B5LmRlZXBjb3B5KHRlYWNoZXJfbGF5ZXJzW3RlYWNoZXJfaWR4XSlcbiAgICAgICAgc3R1ZGVudF9sYXllcnMuYXBwZW5kKHN0dWRlbnRfbGF5ZXIpXG4gICAgICAgIHByaW50KGZcdTAwMjdTdHVkZW50IGxheWVyIHtpfSBcdTAwM2MtIFRlYWNoZXIgbGF5ZXIge3RlYWNoZXJfaWR4fVx1MDAyNylcblxuICAgIHJldHVybiBzdHVkZW50X2xheWVyc1xuXG4jIERlbW8gd2l0aCBhIHRpbnkgQkVSVCBjb25maWcgKGF2b2lkcyBkb3dubG9hZGluZyBmdWxsIG1vZGVsKVxuY29uZmlnID0gQmVydENvbmZpZyhudW1faGlkZGVuX2xheWVycz0xMiwgaGlkZGVuX3NpemU9MTI4LFxuICAgICAgICAgICAgICAgICAgICBudW1fYXR0ZW50aW9uX2hlYWRzPTQsIGludGVybWVkaWF0ZV9zaXplPTUxMilcbnRpbnlfYmVydCA9IEJlcnRNb2RlbChjb25maWcpXG5zdHVkZW50X2xheWVycyA9IGluaXRpYWxpemVfZGlzdGlsYmVydF9mcm9tX2JlcnQodGlueV9iZXJ0LCBuX3N0dWRlbnRfbGF5ZXJzPTYpXG5wcmludChmXHUwMDI3XFxuU3R1ZGVudCBoYXMge2xlbihzdHVkZW50X2xheWVycyl9IGxheWVycyBpbml0aWFsaXplZCBmcm9tIGV2ZXJ5LW90aGVyIHRlYWNoZXIgbGF5ZXIuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRpbnlCRVJUIOKAlCBMYXllci1XaXNlIEF0dGVudGlvbiBhbmQgSGlkZGVuIERpc3RpbGxhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGlueUJFUlQgKEppYW8gZXQgYWwuIDIwMjApIGFwcGxpZXMgZGlzdGlsbGF0aW9uIGF0IGV2ZXJ5IGxheWVyLCBub3QganVzdCB0aGUgZmluYWwgb3V0cHV0LiBUaGUgc3R1ZGVudCAoNCBvciA2IGxheWVycywgMzEyIG9yIDc2OCBoaWRkZW4gZGltKSBsZWFybnMgZnJvbTogKDEpIGVtYmVkZGluZyBsYXllciBvdXRwdXRzLCAoMikgYXR0ZW50aW9uIG1hdHJpY2VzIEFfcyDiiYggQV90IChNU0UgYmV0d2VlbiBzdHVkZW50IGFuZCB0ZWFjaGVyIGF0dGVudGlvbiB3ZWlnaHQgbWF0cmljZXMgYXQgZWFjaCBoZWFkKSwgKDMpIGhpZGRlbiBzdGF0ZXMgSF9zIMK3IFdfaCDiiYggSF90IChNU0UgYWZ0ZXIgcHJvamVjdGluZyBzdHVkZW50IGhpZGRlbiBzdGF0ZXMgdG8gdGVhY2hlclx1MDAyN3MgZGltZW5zaW9uKSwgYW5kICg0KSBwcmVkaWN0aW9uIGxheWVyIG91dHB1dHMuIEEgbGluZWFyIG1hcHBpbmcgV19oIG9mIHNoYXBlIChkX3N0dWRlbnQsIGRfdGVhY2hlcikgaXMgaW50cm9kdWNlZCB0byBicmlkZ2UgZGltZW5zaW9uIG1pc21hdGNoZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFRpbnlCRVJUTGF5ZXJMb3NzKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiVGlueUJFUlQgaW50ZXJtZWRpYXRlIGxheWVyIGRpc3RpbGxhdGlvbjogYXR0ZW50aW9uICsgaGlkZGVuIHN0YXRlLlwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHN0dWRlbnRfZGltOiBpbnQgPSAzMTIsIHRlYWNoZXJfZGltOiBpbnQgPSA3NjgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgIyBMZWFybmFibGUgbGluZWFyIG1hcHBpbmcgZnJvbSBzdHVkZW50IHRvIHRlYWNoZXIgZGltZW5zaW9uXG4gICAgICAgIHNlbGYuaGlkZGVuX21hcHBpbmcgPSBubi5MaW5lYXIoc3R1ZGVudF9kaW0sIHRlYWNoZXJfZGltLCBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGF0dGVudGlvbl9sb3NzKFxuICAgICAgICBzZWxmLFxuICAgICAgICBzdHVkZW50X2F0dG46IHRvcmNoLlRlbnNvciwgICMgKEIsIEhfcywgc2VxLCBzZXEpXG4gICAgICAgIHRlYWNoZXJfYXR0bjogdG9yY2guVGVuc29yLCAgIyAoQiwgSF90LCBzZXEsIHNlcSlcbiAgICApIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBcIlwiXCJNU0UgYmV0d2VlbiBzdHVkZW50IGFuZCB0ZWFjaGVyIGF0dGVudGlvbiBtYXRyaWNlcyAoaGVhZC1hdmVyYWdlZCkuXCJcIlwiXG4gICAgICAgICMgSWYgc3R1ZGVudCBoYXMgZmV3ZXIgaGVhZHMsIGF2ZXJhZ2UgdGVhY2hlciBoZWFkcyB0byBtYXRjaFxuICAgICAgICBIX3MsIEhfdCA9IHN0dWRlbnRfYXR0bi5zaGFwZVsxXSwgdGVhY2hlcl9hdHRuLnNoYXBlWzFdXG4gICAgICAgIGlmIEhfdCAhPSBIX3M6XG4gICAgICAgICAgICB0ZWFjaGVyX2F0dG4gPSB0ZWFjaGVyX2F0dG4udmlldyhcbiAgICAgICAgICAgICAgICB0ZWFjaGVyX2F0dG4uc2hhcGVbMF0sIEhfcywgSF90IC8vIEhfcywgKnRlYWNoZXJfYXR0bi5zaGFwZVsyOl1cbiAgICAgICAgICAgICkubWVhbihkaW09MilcbiAgICAgICAgcmV0dXJuIEYubXNlX2xvc3Moc3R1ZGVudF9hdHRuLCB0ZWFjaGVyX2F0dG4pXG5cbiAgICBkZWYgaGlkZGVuX2xvc3MoXG4gICAgICAgIHNlbGYsXG4gICAgICAgIHN0dWRlbnRfaGlkZGVuOiB0b3JjaC5UZW5zb3IsICAjIChCLCBzZXEsIGRfc3R1ZGVudClcbiAgICAgICAgdGVhY2hlcl9oaWRkZW46IHRvcmNoLlRlbnNvciwgICMgKEIsIHNlcSwgZF90ZWFjaGVyKVxuICAgICkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIFwiXCJcIk1TRSBiZXR3ZWVuIHByb2plY3RlZCBzdHVkZW50IGhpZGRlbiBzdGF0ZXMgYW5kIHRlYWNoZXIgaGlkZGVuIHN0YXRlcy5cIlwiXCJcbiAgICAgICAgcHJvamVjdGVkID0gc2VsZi5oaWRkZW5fbWFwcGluZyhzdHVkZW50X2hpZGRlbikgICMgKEIsIHNlcSwgZF90ZWFjaGVyKVxuICAgICAgICByZXR1cm4gRi5tc2VfbG9zcyhwcm9qZWN0ZWQsIHRlYWNoZXJfaGlkZGVuKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgc3R1ZGVudF9hdHRuLCB0ZWFjaGVyX2F0dG4sIHN0dWRlbnRfaGlkZGVuLCB0ZWFjaGVyX2hpZGRlbik6XG4gICAgICAgIGF0dG5fbCA9IHNlbGYuYXR0ZW50aW9uX2xvc3Moc3R1ZGVudF9hdHRuLCB0ZWFjaGVyX2F0dG4pXG4gICAgICAgIGhpZGRlbl9sID0gc2VsZi5oaWRkZW5fbG9zcyhzdHVkZW50X2hpZGRlbiwgdGVhY2hlcl9oaWRkZW4pXG4gICAgICAgIHJldHVybiBhdHRuX2wgKyBoaWRkZW5fbCwge1x1MDAyN2F0dG5cdTAwMjc6IGF0dG5fbC5pdGVtKCksIFx1MDAyN2hpZGRlblx1MDAyNzogaGlkZGVuX2wuaXRlbSgpfVxuXG4jIERlbW9cbkIsIHNlcSwgSF9zLCBIX3QsIGRfcywgZF90ID0gMiwgMzIsIDQsIDEyLCAzMTIsIDc2OFxubG9zc19mbiA9IFRpbnlCRVJUTGF5ZXJMb3NzKGRfcywgZF90KVxuc3R1ZGVudF9hdHRuID0gdG9yY2gucmFuZG4oQiwgSF9zLCBzZXEsIHNlcSkuc29mdG1heCgtMSlcbnRlYWNoZXJfYXR0biA9IHRvcmNoLnJhbmRuKEIsIEhfdCwgc2VxLCBzZXEpLnNvZnRtYXgoLTEpXG5zdHVkZW50X2ggPSB0b3JjaC5yYW5kbihCLCBzZXEsIGRfcylcbnRlYWNoZXJfaCA9IHRvcmNoLnJhbmRuKEIsIHNlcSwgZF90KVxudG90YWwsIHBhcnRzID0gbG9zc19mbihzdHVkZW50X2F0dG4sIHRlYWNoZXJfYXR0biwgc3R1ZGVudF9oLCB0ZWFjaGVyX2gpXG5wcmludChmXHUwMDI3VG90YWwgbGF5ZXIgbG9zczoge3RvdGFsLml0ZW0oKTouNGZ9ICBhdHRuPXtwYXJ0c1tcImF0dG5cIl06LjRmfSAgaGlkZGVuPXtwYXJ0c1tcImhpZGRlblwiXTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlR3by1TdGFnZSBEaXN0aWxsYXRpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIHR3b19zdGFnZV90aW55YmVydF90cmFpbmluZyhzdHVkZW50LCB0ZWFjaGVyLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBnZW5lcmFsX2xvYWRlciwgdGFza19sb2FkZXIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyaXRlcmlvbl90YXNrLCBsYXllcl9sb3NzX2ZuLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBnZW5lcmFsX2Vwb2Nocz0zLCB0YXNrX2Vwb2Nocz0xMCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbHI9NWUtNSk6XG4gICAgXCJcIlwiXG4gICAgVGlueUJFUlQgdHdvLXN0YWdlIHRyYWluaW5nOlxuICAgIFN0YWdlIDEgKEdlbmVyYWwgRGlzdGlsbGF0aW9uKTogdHJhaW4gb24gTUxNIGNvcnB1cyB3aXRoIGxheWVyLXdpc2UgS0QgZnJvbSBCRVJULlxuICAgIFN0YWdlIDIgKFRhc2stU3BlY2lmaWMgRGlzdGlsbGF0aW9uKTogZmluZS10dW5lIHdpdGggdGFzayBsb3NzICsgbGF5ZXIgS0QgZnJvbSBmaW5lLXR1bmVkIHRlYWNoZXIuXG4gICAgXCJcIlwiXG4gICAgb3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbVcoc3R1ZGVudC5wYXJhbWV0ZXJzKCksIGxyPWxyKVxuXG4gICAgIyBTdGFnZSAxOiBHZW5lcmFsIGRpc3RpbGxhdGlvbiBvbiB1bmxhYmVsZWQgdGV4dFxuICAgIHByaW50KFx1MDAyNz09PSBTdGFnZSAxOiBHZW5lcmFsIERpc3RpbGxhdGlvbiA9PT1cdTAwMjcpXG4gICAgZm9yIGVwb2NoIGluIHJhbmdlKGdlbmVyYWxfZXBvY2hzKTpcbiAgICAgICAgdG90YWxfbG9zcyA9IDAuMFxuICAgICAgICBmb3IgYmF0Y2ggaW4gZ2VuZXJhbF9sb2FkZXI6XG4gICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgICAgICMgR2V0IHRlYWNoZXIgaW50ZXJtZWRpYXRlIHJlcHJlc2VudGF0aW9uc1xuICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICAgICAgdGVhY2hlcl9vdXRwdXRzID0gdGVhY2hlcigqKmJhdGNoLCBvdXRwdXRfYXR0ZW50aW9ucz1UcnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0X2hpZGRlbl9zdGF0ZXM9VHJ1ZSlcbiAgICAgICAgICAgIHN0dWRlbnRfb3V0cHV0cyA9IHN0dWRlbnQoKipiYXRjaCwgb3V0cHV0X2F0dGVudGlvbnM9VHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0X2hpZGRlbl9zdGF0ZXM9VHJ1ZSlcbiAgICAgICAgICAgICMgTGF5ZXItd2lzZSBkaXN0aWxsYXRpb24gbG9zc1xuICAgICAgICAgICAgbG9zcyA9IHN1bShcbiAgICAgICAgICAgICAgICBsYXllcl9sb3NzX2ZuKFxuICAgICAgICAgICAgICAgICAgICBzX2F0dG4sIHRfYXR0biwgc19oLCB0X2hcbiAgICAgICAgICAgICAgICApWzBdXG4gICAgICAgICAgICAgICAgZm9yIHNfYXR0biwgdF9hdHRuLCBzX2gsIHRfaCBpbiB6aXAoXG4gICAgICAgICAgICAgICAgICAgIHN0dWRlbnRfb3V0cHV0cy5hdHRlbnRpb25zLFxuICAgICAgICAgICAgICAgICAgICB0ZWFjaGVyX291dHB1dHMuYXR0ZW50aW9uc1sxOjoyXSwgICMgZXZlcnktb3RoZXIgdGVhY2hlciBsYXllclxuICAgICAgICAgICAgICAgICAgICBzdHVkZW50X291dHB1dHMuaGlkZGVuX3N0YXRlc1sxOl0sXG4gICAgICAgICAgICAgICAgICAgIHRlYWNoZXJfb3V0cHV0cy5oaWRkZW5fc3RhdGVzWzI6OjJdLFxuICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgIClcbiAgICAgICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICAgICAgb3B0aW1pemVyLnN0ZXAoKVxuICAgICAgICAgICAgdG90YWxfbG9zcyArPSBsb3NzLml0ZW0oKVxuICAgICAgICBwcmludChmXHUwMDI3ICBFcG9jaCB7ZXBvY2grMX06IGF2Z19sb3NzPXt0b3RhbF9sb3NzL21heCgxLGxlbihnZW5lcmFsX2xvYWRlcikpOi40Zn1cdTAwMjcpXG5cbiAgICBwcmludChcdTAwMjc9PT0gU3RhZ2UgMjogVGFzay1TcGVjaWZpYyBEaXN0aWxsYXRpb24gPT09XHUwMDI3KVxuICAgICMgU3RhZ2UgMiBvbWl0dGVkIGZvciBicmV2aXR5IOKAlCB1c2VzIHRhc2sgbG9zcyArIEtEIGZyb20gdGFzay1maW5lLXR1bmVkIHRlYWNoZXJcbiAgICBwcmludChcdTAwMjdTdGFnZSAyOiBmaW5lLXR1bmUgc3R1ZGVudCBvbiB0YXNrIHdpdGggbGF5ZXIgS0QgZnJvbSB0YXNrLWZpbmUtdHVuZWQgQkVSVCB0ZWFjaGVyLlx1MDAyNylcblxucHJpbnQoXHUwMDI3VHdvLXN0YWdlIFRpbnlCRVJUOiBnZW5lcmFsIC1cdTAwM2UgdGFzay1zcGVjaWZpYyBkaXN0aWxsYXRpb24gcGlwZWxpbmUgZGVmaW5lZC5cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJXaHkgVHdvLVN0YWdlIERpc3RpbGxhdGlvbiBXb3JrcyBCZXR0ZXIiLCJjb250ZW50IjoiSW4gc2luZ2xlLXN0YWdlIGRpc3RpbGxhdGlvbiwgdGhlIHN0dWRlbnQgaXMgZGlzdGlsbGVkIGRpcmVjdGx5IG9uIHRoZSB0YXNrIHdpdGggYSBzbWFsbCBkYXRhc2V0LiBUaGUgc3R1ZGVudCBuZXZlciBzZWVzIHRoZSBicmVhZHRoIG9mIGxpbmd1aXN0aWMgcGF0dGVybnMgdGhhdCBCRVJUIGxlYXJuZWQgZnJvbSBiaWxsaW9ucyBvZiB0b2tlbnMuIEdlbmVyYWwgZGlzdGlsbGF0aW9uIGZpcnN0IGdpdmVzIHRoZSBzdHVkZW50IGdlbmVyYWwgbGFuZ3VhZ2UgdW5kZXJzdGFuZGluZyBmcm9tIHVubGFiZWxlZCB0ZXh0LCB0aGVuIHRhc2stc3BlY2lmaWMgZGlzdGlsbGF0aW9uIGZpbmUtdHVuZXMgaXQgZm9yIHRoZSB0YXNrLiBUaGlzIHR3by1zdGFnZSBhcHByb2FjaCBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybXMgc2luZ2xlLXN0YWdlIG9uIEdMVUUgYnkgMeKAkzIgcG9pbnRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBhdGllbnQgS25vd2xlZGdlIERpc3RpbGxhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGF0aWVudCBLRCAoU3VuIGV0IGFsLiAyMDE5KSBkaXN0aWxscyBmcm9tIG11bHRpcGxlIHRlYWNoZXIgbGF5ZXJzIHNpbXVsdGFuZW91c2x5IHJhdGhlciB0aGFuIGp1c3QgdGhlIGZpbmFsIGxheWVyLiBUaGUgc3R1ZGVudCBpcyB0cmFpbmVkIHRvIG1hdGNoIHRoZSBvdXRwdXQgb2YgdGVhY2hlciBsYXllcnMgMywgNiwgOSwgYW5kIDEyIChmb3IgUEtELXNraXApIG9yIGFsbCBsYXllcnMgKGZvciBQS0QtbGFzdCkuIFRoaXMgcGF0aWVudCBhcHByb2FjaCBwcmV2ZW50cyB0aGUgc3R1ZGVudCBmcm9tIG92ZXJmaXR0aW5nIHRvIHRoZSBmaW5hbCB0ZWFjaGVyIGxheWVyIHRvbyBlYXJseS4gVGhlIGxvc3MgY29tYmluZXMgdGFzayBjcm9zcy1lbnRyb3B5IHdpdGggTVNFIG9uIG5vcm1hbGl6ZWQgaGlkZGVuIHN0YXRlcyBhdCBlYWNoIHBhdGllbnQgbGF5ZXIsIHByb3ZpZGluZyBhIGRlbnNlciBzdXBlcnZpc29yeSBzaWduYWwgdGhyb3VnaG91dCB0cmFpbmluZy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkRpc3RpbEJFUlQ6IHRhc2stYWdub3N0aWMgZGlzdGlsbGF0aW9uIGR1cmluZyBwcmV0cmFpbmluZzsgNiBsYXllcnM7IE1MTSArIGNvc2luZSArIHNvZnQtQ0UgbG9zc2VzLiIsIlRpbnlCRVJUOiB0YXNrLXNwZWNpZmljICsgZ2VuZXJhbCBkaXN0aWxsYXRpb247IDQgb3IgNiBsYXllcnM7IGVtYmVkZGluZyArIGF0dGVudGlvbiArIGhpZGRlbiArIHByZWRpY3Rpb24gbG9zc2VzLiIsIlBhdGllbnQgS0Q6IG11bHRpLWxheWVyIHRlYWNoZXIgc3VwZXJ2aXNpb247IGF2b2lkcyBwcmVtYXR1cmUgY29udmVyZ2VuY2UgdG8gZmluYWwgbGF5ZXIgcmVwcmVzZW50YXRpb24uIiwiTGF5ZXIgbWFwcGluZzogc3R1ZGVudFtpXSDihpAgdGVhY2hlclsyaV0gZm9yIGV2ZXJ5LW90aGVyIGluaXQ7IFRpbnlCRVJUIGxlYXJucyBhIGxpbmVhciBwcm9qZWN0aW9uIFdfaC4iLCJUZW1wZXJhdHVyZSBUPTQgaW4gc29mdCBjcm9zcy1lbnRyb3B5OiBmbGF0dGVyIHRlYWNoZXIgZGlzdHJpYnV0aW9uIHJldmVhbHMgbW9yZSBjbGFzcyByZWxhdGlvbnNoaXAgaW5mb3JtYXRpb24uIiwiT24gR0xVRSBNTkxJLW06IERpc3RpbEJFUlQg4omIIDgyLjIsIFRpbnlCRVJULTQg4omIIDgyLjUsIEJFUlQtYmFzZSDiiYggODQuNiDigJQgVGlueUJFUlQtNCBhdCAxNC41TSBwYXJhbXMuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJFUlQgQ29tcHJlc3Npb24gTW9kZWwgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIlBhcmFtcyIsIkxheWVycyIsIkdMVUUgU2NvcmUiLCJJbmZlcmVuY2UgU3BlZWQgdnMgQkVSVCIsIkRpc3RpbGxhdGlvbiBUeXBlIl0sInJvd3MiOltbIkJFUlQtYmFzZSIsIjExME0iLCIxMiIsIjc5LjYiLCIxw5cgKGJhc2VsaW5lKSIsIk4vQSAodGVhY2hlcikiXSxbIkRpc3RpbEJFUlQiLCI2Nk0iLCI2IiwiNzcuMCAofjk3JSkiLCIxLjbDlyIsIlRhc2stYWdub3N0aWMgcHJldHJhaW5pbmcgS0QiXSxbIlRpbnlCRVJULTRMIiwiMTQuNU0iLCI0IiwiNzUuNSAofjk1JSkiLCIyLjXDlyIsIkdlbmVyYWwgKyB0YXNrLXNwZWNpZmljLCBsYXllci13aXNlIl0sWyJUaW55QkVSVC02TCIsIjY3TSIsIjYiLCI3OS40ICh+OTklKSIsIjEuOMOXIiwiR2VuZXJhbCArIHRhc2stc3BlY2lmaWMsIGxheWVyLXdpc2UiXSxbIkFMQkVSVC1iYXNlIiwiMTJNIiwiMTIgKHNoYXJlZCkiLCI3Ni4xICh+OTYlKSIsIn4xw5cgKHBhcmFtIHNoYXJpbmcsIG5vdCBmYXN0ZXIpIiwiTm9uZSAod2VpZ2h0IHNoYXJpbmcgb25seSkiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRhc2stU3BlY2lmaWMgRGlzdGlsbGF0aW9uIEZpbmUtVHVuaW5nIERldGFpbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIFRpbnlCRVJUXHUwMDI3cyB0YXNrLXNwZWNpZmljIHN0YWdlLCB0aGUgdGVhY2hlciBpcyBhIGZpbmUtdHVuZWQgQkVSVCAobm90IHRoZSBvcmlnaW5hbCBwcmUtdHJhaW5lZCBCRVJUKS4gRGF0YSBhdWdtZW50YXRpb24gaXMgYXBwbGllZDogdGhlIHRyYWluaW5nIHNldCBpcyBleHBhbmRlZCB3aXRoIHdvcmQgc3Vic3RpdHV0aW9ucyB1c2luZyBhIGxhbmd1YWdlIG1vZGVsLCB0cmlwbGluZyB0aGUgbnVtYmVyIG9mIHRyYWluaW5nIGV4YW1wbGVzLiBUaGlzIGF1Z21lbnRlZCBkYXRhIGlzIGZlZCB0byBib3RoIHRlYWNoZXIgYW5kIHN0dWRlbnQsIGFuZCB0aGUgc3R1ZGVudCBtYXRjaGVzIHRoZSB0ZWFjaGVyXHUwMDI3cyBpbnRlcm1lZGlhdGUgcmVwcmVzZW50YXRpb25zIGFjcm9zcyBhbGwgbGF5ZXJzIHNpbXVsdGFuZW91c2x5LiBUaGUgY29tYmluZWQgYXVnbWVudGF0aW9uICsgbGF5ZXItd2lzZSBLRCBpcyB3aGF0IGdpdmVzIFRpbnlCRVJULTRMIHN1Y2ggaGlnaCBHTFVFIHNjb3JlcyBhdCBvbmx5IDE0LjVNIHBhcmFtZXRlcnMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaXN0aWxCRVJUXHUwMDI3cyBzaW1wbGljaXR5IGlzIGl0cyBtYWluIGFkdmFudGFnZTogbm8gbGF5ZXItbWFwcGluZyBtYXRyaXgsIG5vIGF0dGVudGlvbiB0cmFuc2Zlciwgbm8gZGF0YSBhdWdtZW50YXRpb24g4oCUIGp1c3QgdGhyZWUgcHJldHJhaW5pbmcgbG9zc2VzIGFwcGxpZWQgb3ZlciB0aGUgc2FtZSBNTE0gZGF0YXNldCBhcyBCRVJULiBUaGlzIG1ha2VzIERpc3RpbEJFUlQgc3RyYWlnaHRmb3J3YXJkIHRvIHJlcHJvZHVjZSBhbmQgZXh0ZW5kIHRvIGRvbWFpbi1zcGVjaWZpYyBjb3Jwb3JhIChlLmcuLCBkaXN0aWxsaW5nIEJpb0JFUlQgaW50byBhIHNtYWxsZXIgYmlvbWVkaWNhbCBtb2RlbCkuIFRoZSBtYWluIGxpbWl0YXRpb24gaXMgdGhhdCB0YXNrLWFnbm9zdGljIGRpc3RpbGxhdGlvbiBpcyBsZXNzIGVmZmVjdGl2ZSB0aGFuIHRhc2stc3BlY2lmaWM6IERpc3RpbEJFUlQgZmluZS10dW5lZCBvbiBHTFVFIGNvbnNpc3RlbnRseSBsYWdzIFRpbnlCRVJULTZMIGJ5IDLigJMzIHBvaW50cyBkZXNwaXRlIGhhdmluZyBzaW1pbGFyIHNpemUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUZW1wZXJhdHVyZSBUPTQgaW4gc29mdCBDRTogdGVhY2hlciBkaXN0cmlidXRpb24gYXQgVD00IHJldmVhbHMgcmFua2luZyBpbmZvcm1hdGlvbiBiZXR3ZWVuIG5vbi10YXJnZXQgY2xhc3Nlcy4iLCJDb3NpbmUgbG9zcyBpbiBEaXN0aWxCRVJUOiBlbnN1cmVzIHN0dWRlbnQgaGlkZGVuIHNwYWNlIGlzIGFsaWduZWQgd2l0aCB0ZWFjaGVyLCBwcmV2ZW50aW5nIHJlcHJlc2VudGF0aW9uIGNvbGxhcHNlLiIsIlRpbnlCRVJUIGxheWVyIG1hcHBpbmcgbWF0cml4IFdfaDogaW5pdGlhbGl6ZWQgdG8gcmFuZG9tIG9ydGhvZ29uYWwgbWF0cml4IGZvciBzdGFibGUgZWFybHktdHJhaW5pbmcgZ3JhZGllbnQgZmxvdy4iLCJEYXRhIGF1Z21lbnRhdGlvbiBmb3IgdGFzay1zcGVjaWZpYyBzdGFnZTogbWFza2VkIExNIHdvcmQgcmVwbGFjZW1lbnQgdXNpbmcgQkVSVC1iYXNlIGFzIGF1Z21lbnRhdGlvbiBtb2RlbC4iLCJHcmFkaWVudCBjb25mbGljdHM6IGxheWVyLXdpc2UgbG9zc2VzIGF0IGRpZmZlcmVudCBsYXllcnMgbWF5IGNvbmZsaWN0IOKAlCB3ZWlnaHQgdGhlbSBpbnZlcnNlbHkgYnkgbGF5ZXIgaW5kZXguIiwiVGlueSBzdHVkZW50LCBsYXJnZSB0ZWFjaGVyIGdhcDogXHUwMDNlNMOXIHNpemUgZGlmZmVyZW5jZSBjYXVzZXMgYXR0ZW50aW9uIG1pc21hdGNoIOKAlCB1c2UgaW50ZXJtZWRpYXRlIHRlYWNoZXIgZm9yIHZlcnkgc21hbGwgc3R1ZGVudHMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# DistilBERT and TinyBERT — BERT Compression via Distillation

BERT-base has 110M parameters, 12 layers, and a 768-dimensional hidden state. For many production use cases it is too large: too slow for real-time inference, too expensive to serve at scale, and too memory-intensive for on-device deployment. DistilBERT and TinyBERT compress BERT via knowledge distillation — training a smaller student model to mimic the larger teacher — retaining 96–97% of BERT's GLUE score at 40–60% of its size and latency.

## DistilBERT — Task-Agnostic Pretraining Distillation

DistilBERT (Sanh et al. 2019) distills BERT-base during pretraining, not fine-tuning. The student has 6 layers (half of BERT-base's 12), same hidden dim (768) and head count (12), but no token-type embeddings and no pooler. The teacher is BERT-base trained on the same MLM corpus. Three loss terms are combined: (1) L_MLM — student's masked language model loss on true labels; (2) L_cos — cosine similarity between student and teacher hidden states at the last layer; (3) L_CE — cross-entropy of student outputs against teacher's soft probability distribution with temperature T=4.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def distilbert_distillation_loss(
    student_logits: torch.Tensor,    # (B, seq_len, vocab_size)
    teacher_logits: torch.Tensor,    # (B, seq_len, vocab_size)
    student_hidden: torch.Tensor,    # (B, seq_len, hidden)
    teacher_hidden: torch.Tensor,    # (B, seq_len, hidden)
    true_labels: torch.Tensor,       # (B, seq_len) — -100 for non-masked tokens
    temperature: float = 4.0,
    alpha_mlm: float = 0.33,
    alpha_cos: float = 0.33,
    alpha_kd: float = 0.34,
) -> torch.Tensor:
    """Three-component DistilBERT distillation loss."""
    # 1. MLM loss (student vs true labels)
    mlm_loss = F.cross_entropy(
        student_logits.view(-1, student_logits.size(-1)),
        true_labels.view(-1),
        ignore_index=-100
    )

    # 2. Cosine similarity loss on hidden states
    # Cosine distance = 1 - cosine_similarity, minimise this
    cos_loss = (1 - F.cosine_similarity(student_hidden, teacher_hidden, dim=-1)).mean()

    # 3. Soft cross-entropy (KD) at temperature T
    T = temperature
    soft_teacher = F.softmax(teacher_logits / T, dim=-1)
    log_soft_student = F.log_softmax(student_logits / T, dim=-1)
    # Only compute on masked positions (where true_labels != -100)
    mask = (true_labels != -100).unsqueeze(-1).expand_as(soft_teacher)
    kd_loss = F.kl_div(log_soft_student[mask].view(-1, soft_teacher.size(-1)),
                        soft_teacher[mask].view(-1, soft_teacher.size(-1)),
                        reduction='batchmean') * (T ** 2)

    total = alpha_mlm * mlm_loss + alpha_cos * cos_loss + alpha_kd * kd_loss
    return total, {'mlm': mlm_loss.item(), 'cos': cos_loss.item(), 'kd': kd_loss.item()}
```

## Every-Other-Layer Mapping

DistilBERT initializes student layer i from teacher layer 2i (every other teacher layer). With 6 student layers: student[0] ← teacher[1], student[1] ← teacher[3], ..., student[5] ← teacher[11]. This initialization gives the student a strong starting point and is partially responsible for DistilBERT's efficiency — the pre-training distillation is short because most of the knowledge is already present in the initialized weights.

```python
import torch
import torch.nn as nn
from transformers import BertModel, BertConfig

def initialize_distilbert_from_bert(teacher_bert: BertModel,
                                    n_student_layers: int = 6) -> nn.ModuleList:
    """
    Copy every-other teacher layer into student.
    Teacher: 12 layers. Student: 6 layers.
    Mapping: student[i] <- teacher[2*i + 1] (1-indexed teacher layers).
    """
    teacher_layers = teacher_bert.encoder.layer  # ModuleList of 12 BertLayer
    student_layers = nn.ModuleList()

    for i in range(n_student_layers):
        teacher_idx = 2 * i + 1  # 1, 3, 5, 7, 9, 11
        if teacher_idx >= len(teacher_layers):
            teacher_idx = len(teacher_layers) - 1
        # Deep copy the teacher layer's state dict into a new layer
        import copy
        student_layer = copy.deepcopy(teacher_layers[teacher_idx])
        student_layers.append(student_layer)
        print(f'Student layer {i} <- Teacher layer {teacher_idx}')

    return student_layers

# Demo with a tiny BERT config (avoids downloading full model)
config = BertConfig(num_hidden_layers=12, hidden_size=128,
                    num_attention_heads=4, intermediate_size=512)
tiny_bert = BertModel(config)
student_layers = initialize_distilbert_from_bert(tiny_bert, n_student_layers=6)
print(f'\nStudent has {len(student_layers)} layers initialized from every-other teacher layer.')
```

## TinyBERT — Layer-Wise Attention and Hidden Distillation

TinyBERT (Jiao et al. 2020) applies distillation at every layer, not just the final output. The student (4 or 6 layers, 312 or 768 hidden dim) learns from: (1) embedding layer outputs, (2) attention matrices A_s ≈ A_t (MSE between student and teacher attention weight matrices at each head), (3) hidden states H_s · W_h ≈ H_t (MSE after projecting student hidden states to teacher's dimension), and (4) prediction layer outputs. A linear mapping W_h of shape (d_student, d_teacher) is introduced to bridge dimension mismatches.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TinyBERTLayerLoss(nn.Module):
    """TinyBERT intermediate layer distillation: attention + hidden state."""

    def __init__(self, student_dim: int = 312, teacher_dim: int = 768):
        super().__init__()
        # Learnable linear mapping from student to teacher dimension
        self.hidden_mapping = nn.Linear(student_dim, teacher_dim, bias=False)

    def attention_loss(
        self,
        student_attn: torch.Tensor,  # (B, H_s, seq, seq)
        teacher_attn: torch.Tensor,  # (B, H_t, seq, seq)
    ) -> torch.Tensor:
        """MSE between student and teacher attention matrices (head-averaged)."""
        # If student has fewer heads, average teacher heads to match
        H_s, H_t = student_attn.shape[1], teacher_attn.shape[1]
        if H_t != H_s:
            teacher_attn = teacher_attn.view(
                teacher_attn.shape[0], H_s, H_t // H_s, *teacher_attn.shape[2:]
            ).mean(dim=2)
        return F.mse_loss(student_attn, teacher_attn)

    def hidden_loss(
        self,
        student_hidden: torch.Tensor,  # (B, seq, d_student)
        teacher_hidden: torch.Tensor,  # (B, seq, d_teacher)
    ) -> torch.Tensor:
        """MSE between projected student hidden states and teacher hidden states."""
        projected = self.hidden_mapping(student_hidden)  # (B, seq, d_teacher)
        return F.mse_loss(projected, teacher_hidden)

    def forward(self, student_attn, teacher_attn, student_hidden, teacher_hidden):
        attn_l = self.attention_loss(student_attn, teacher_attn)
        hidden_l = self.hidden_loss(student_hidden, teacher_hidden)
        return attn_l + hidden_l, {'attn': attn_l.item(), 'hidden': hidden_l.item()}

# Demo
B, seq, H_s, H_t, d_s, d_t = 2, 32, 4, 12, 312, 768
loss_fn = TinyBERTLayerLoss(d_s, d_t)
student_attn = torch.randn(B, H_s, seq, seq).softmax(-1)
teacher_attn = torch.randn(B, H_t, seq, seq).softmax(-1)
student_h = torch.randn(B, seq, d_s)
teacher_h = torch.randn(B, seq, d_t)
total, parts = loss_fn(student_attn, teacher_attn, student_h, teacher_h)
print(f'Total layer loss: {total.item():.4f}  attn={parts["attn"]:.4f}  hidden={parts["hidden"]:.4f}')
```

## Two-Stage Distillation

```python
import torch
import torch.nn as nn

def two_stage_tinybert_training(student, teacher,
                                general_loader, task_loader,
                                criterion_task, layer_loss_fn,
                                general_epochs=3, task_epochs=10,
                                lr=5e-5):
    """
    TinyBERT two-stage training:
    Stage 1 (General Distillation): train on MLM corpus with layer-wise KD from BERT.
    Stage 2 (Task-Specific Distillation): fine-tune with task loss + layer KD from fine-tuned teacher.
    """
    optimizer = torch.optim.AdamW(student.parameters(), lr=lr)

    # Stage 1: General distillation on unlabeled text
    print('=== Stage 1: General Distillation ===')
    for epoch in range(general_epochs):
        total_loss = 0.0
        for batch in general_loader:
            optimizer.zero_grad()
            # Get teacher intermediate representations
            with torch.no_grad():
                teacher_outputs = teacher(**batch, output_attentions=True,
                                          output_hidden_states=True)
            student_outputs = student(**batch, output_attentions=True,
                                      output_hidden_states=True)
            # Layer-wise distillation loss
            loss = sum(
                layer_loss_fn(
                    s_attn, t_attn, s_h, t_h
                )[0]
                for s_attn, t_attn, s_h, t_h in zip(
                    student_outputs.attentions,
                    teacher_outputs.attentions[1::2],  # every-other teacher layer
                    student_outputs.hidden_states[1:],
                    teacher_outputs.hidden_states[2::2],
                )
            )
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f'  Epoch {epoch+1}: avg_loss={total_loss/max(1,len(general_loader)):.4f}')

    print('=== Stage 2: Task-Specific Distillation ===')
    # Stage 2 omitted for brevity — uses task loss + KD from task-fine-tuned teacher
    print('Stage 2: fine-tune student on task with layer KD from task-fine-tuned BERT teacher.')

print('Two-stage TinyBERT: general -> task-specific distillation pipeline defined.')
```

> **Why Two-Stage Distillation Works Better**: In single-stage distillation, the student is distilled directly on the task with a small dataset. The student never sees the breadth of linguistic patterns that BERT learned from billions of tokens. General distillation first gives the student general language understanding from unlabeled text, then task-specific distillation fine-tunes it for the task. This two-stage approach consistently outperforms single-stage on GLUE by 1–2 points.

## Patient Knowledge Distillation

Patient KD (Sun et al. 2019) distills from multiple teacher layers simultaneously rather than just the final layer. The student is trained to match the output of teacher layers 3, 6, 9, and 12 (for PKD-skip) or all layers (for PKD-last). This patient approach prevents the student from overfitting to the final teacher layer too early. The loss combines task cross-entropy with MSE on normalized hidden states at each patient layer, providing a denser supervisory signal throughout training.

- DistilBERT: task-agnostic distillation during pretraining; 6 layers; MLM + cosine + soft-CE losses.
- TinyBERT: task-specific + general distillation; 4 or 6 layers; embedding + attention + hidden + prediction losses.
- Patient KD: multi-layer teacher supervision; avoids premature convergence to final layer representation.
- Layer mapping: student[i] ← teacher[2i] for every-other init; TinyBERT learns a linear projection W_h.
- Temperature T=4 in soft cross-entropy: flatter teacher distribution reveals more class relationship information.
- On GLUE MNLI-m: DistilBERT ≈ 82.2, TinyBERT-4 ≈ 82.5, BERT-base ≈ 84.6 — TinyBERT-4 at 14.5M params.

## BERT Compression Model Comparison

| Model | Params | Layers | GLUE Score | Inference Speed vs BERT | Distillation Type |
| --- | --- | --- | --- | --- | --- |
| BERT-base | 110M | 12 | 79.6 | 1× (baseline) | N/A (teacher) |
| DistilBERT | 66M | 6 | 77.0 (~97%) | 1.6× | Task-agnostic pretraining KD |
| TinyBERT-4L | 14.5M | 4 | 75.5 (~95%) | 2.5× | General + task-specific, layer-wise |
| TinyBERT-6L | 67M | 6 | 79.4 (~99%) | 1.8× | General + task-specific, layer-wise |
| ALBERT-base | 12M | 12 (shared) | 76.1 (~96%) | ~1× (param sharing, not faster) | None (weight sharing only) |

## Task-Specific Distillation Fine-Tuning Details

In TinyBERT's task-specific stage, the teacher is a fine-tuned BERT (not the original pre-trained BERT). Data augmentation is applied: the training set is expanded with word substitutions using a language model, tripling the number of training examples. This augmented data is fed to both teacher and student, and the student matches the teacher's intermediate representations across all layers simultaneously. The combined augmentation + layer-wise KD is what gives TinyBERT-4L such high GLUE scores at only 14.5M parameters.

DistilBERT's simplicity is its main advantage: no layer-mapping matrix, no attention transfer, no data augmentation — just three pretraining losses applied over the same MLM dataset as BERT. This makes DistilBERT straightforward to reproduce and extend to domain-specific corpora (e.g., distilling BioBERT into a smaller biomedical model). The main limitation is that task-agnostic distillation is less effective than task-specific: DistilBERT fine-tuned on GLUE consistently lags TinyBERT-6L by 2–3 points despite having similar size.

- Temperature T=4 in soft CE: teacher distribution at T=4 reveals ranking information between non-target classes.
- Cosine loss in DistilBERT: ensures student hidden space is aligned with teacher, preventing representation collapse.
- TinyBERT layer mapping matrix W_h: initialized to random orthogonal matrix for stable early-training gradient flow.
- Data augmentation for task-specific stage: masked LM word replacement using BERT-base as augmentation model.
- Gradient conflicts: layer-wise losses at different layers may conflict — weight them inversely by layer index.
- Tiny student, large teacher gap: >4× size difference causes attention mismatch — use intermediate teacher for very small students.

---

