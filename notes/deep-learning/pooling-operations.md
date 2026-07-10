---
title: "Pooling Operations — Max, Average, Global, and Adaptive"
slug: "pooling-operations"
description: "Compare pooling variants from max and average to global average pooling, adaptive pooling, and spatial pyramid pooling, with gradient flow and classification head analysis."
tags: ["deep-learning", "cnns"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUG9vbGluZyBhZ2dyZWdhdGVzIHNwYXRpYWwgaW5mb3JtYXRpb24sIHJlZHVjZXMgZmVhdHVyZSBtYXAgc2l6ZSwgYW5kIGludHJvZHVjZXMgYSBkZWdyZWUgb2Ygc3BhdGlhbCBpbnZhcmlhbmNlLiBUaGUgY2hvaWNlIG9mIHBvb2xpbmcgc3RyYXRlZ3kgaGFzIGRvd25zdHJlYW0gZWZmZWN0cyBvbiBwYXJhbWV0ZXIgY291bnQsIGdyYWRpZW50IGZsb3csIHNwYXRpYWwgaW52YXJpYW5jZSwgYW5kIHRoZSBhYmlsaXR5IHRvIGhhbmRsZSB2YXJpYWJsZS1zaXplIGlucHV0cy4gR2xvYmFsIGF2ZXJhZ2UgcG9vbGluZyAoR0FQKSByZXBsYWNlZCB0aGUgZnVsbHktY29ubmVjdGVkIGNsYXNzaWZpZXIgaW4gbW9kZXJuIG5ldHdvcmtzLCBjdXR0aW5nIG1pbGxpb25zIG9mIHBhcmFtZXRlcnMuIEFkYXB0aXZlIHBvb2xpbmcgZW5hYmxlcyBiYXRjaCBpbmZlcmVuY2Ugb24gaW1hZ2VzIG9mIGRpZmZlcmVudCBzaXplcy4gVW5kZXJzdGFuZGluZyB3aGVuIHRvIHBvb2wsIGhvdyBtdWNoLCBhbmQgd2hpY2ggdmFyaWFudCBkZXRlcm1pbmVzIHdoZXRoZXIgYSBtb2RlbCBpcyBjb21wYWN0IGFuZCBnZW5lcmFsaXNlcyB3ZWxsIG9yIGlzIG92ZXJwYXJhbWV0ZXJpc2VkIGFuZCBicml0dGxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1heCBQb29saW5nIHZzIEF2ZXJhZ2UgUG9vbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWF4IHBvb2xpbmcgc2VsZWN0cyB0aGUgbWF4aW11bSBhY3RpdmF0aW9uIGluIGVhY2ggd2luZG93OiBpdCBpcyBhIGhhcmQgc2VsZWN0b3IsIGRldGVjdGluZyB3aGV0aGVyIGEgZmVhdHVyZSBpcyBwcmVzZW50IGFueXdoZXJlIGluIHRoZSByZWdpb24gKGZlYXR1cmUgZGV0ZWN0aXZlbmVzcykuIEF2ZXJhZ2UgcG9vbGluZyBjb21wdXRlcyB0aGUgbWVhbjogaXQgaW50ZWdyYXRlcyBldmlkZW5jZSBhY3Jvc3MgdGhlIHJlZ2lvbiAoc21vb3RoZXIsIGxlc3Mgc2Vuc2l0aXZlIHRvIGV4YWN0IGxvY2F0aW9uKS4gTWF4IHBvb2xpbmcgaGFzIHN0cm9uZ2VyIHNwYXRpYWwgaW52YXJpYW5jZSDigJQgYSBzaGlmdGVkIGZlYXR1cmUgc3RpbGwgcHJvZHVjZXMgdGhlIHNhbWUgbWF4LiBBdmVyYWdlIHBvb2xpbmcgZGlzY2FyZHMgdGhlIHBlYWsgbWFnbml0dWRlLiBGb3IgZWFybHkgbGF5ZXJzIGRldGVjdGluZyBlZGdlIGFuZCB0ZXh0dXJlIGZlYXR1cmVzLCBtYXggcG9vbGluZyBpcyBzdGFuZGFyZC4gRm9yIHRoZSBmaW5hbCBnbG9iYWwgcG9vbGluZyBiZWZvcmUgdGhlIGNsYXNzaWZpZXIsIGF2ZXJhZ2UgcG9vbGluZyBpcyBwcmVmZXJyZWQgYmVjYXVzZSBpdCB1c2VzIGluZm9ybWF0aW9uIGZyb20gYWxsIHNwYXRpYWwgbG9jYXRpb25zIHJhdGhlciB0aGFuIGp1c3Qgb25lIHBlYWsuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxubnAucmFuZG9tLnNlZWQoNDIpXG4jIFNpbXVsYXRlIGEgZmVhdHVyZSBtYXAgd2l0aCBhIHNoYXJwIGFjdGl2YXRpb24gcGVha1xuZmVhdCA9IHRvcmNoLnplcm9zKDEsIDEsIDgsIDgpXG5mZWF0WzAsIDAsIDMsIDRdID0gNS4wICAgIyBzaGFycCBwZWFrXG5mZWF0WzAsIDAsIDosIDpdICs9IHRvcmNoLnJhbmRuKDgsIDgpICogMC4xICAjIG5vaXNlXG5cbm1heF9wb29sID0gbm4uTWF4UG9vbDJkKDIsIHN0cmlkZT0yKVxuYXZnX3Bvb2wgPSBubi5BdmdQb29sMmQoMiwgc3RyaWRlPTIpXG5cbm1heF9vdXQgPSBtYXhfcG9vbChmZWF0KVxuYXZnX291dCA9IGF2Z19wb29sKGZlYXQpXG5cbnByaW50KFx1MDAyN0lucHV0IGZlYXR1cmUgbWFwICg4eDgpOlx1MDAyNylcbnByaW50KGZlYXRbMCwwXS5udW1weSgpLnJvdW5kKDIpKVxucHJpbnQoXHUwMDI3XFxuQWZ0ZXIgTWF4UG9vbDJkKDIsMikg4oCUIDR4NDpcdTAwMjcpXG5wcmludChtYXhfb3V0WzAsMF0uZGV0YWNoKCkubnVtcHkoKS5yb3VuZCgyKSlcbnByaW50KFx1MDAyN1xcbkFmdGVyIEF2Z1Bvb2wyZCgyLDIpIOKAlCA0eDQ6XHUwMDI3KVxucHJpbnQoYXZnX291dFswLDBdLmRldGFjaCgpLm51bXB5KCkucm91bmQoMikpXG5wcmludChcdTAwMjdcXG5NYXggcG9vbCBwcmVzZXJ2ZXMgcGVhayBtYWduaXR1ZGU7IGF2ZyBwb29sIHNwcmVhZHMgaXQuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikdsb2JhbCBBdmVyYWdlIFBvb2xpbmcg4oCUIFJlcGxhY2luZyB0aGUgQ2xhc3NpZmllciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2xvYmFsIEF2ZXJhZ2UgUG9vbGluZyAoR0FQKSBjb2xsYXBzZXMgdGhlIGVudGlyZSBIw5dXIHNwYXRpYWwgbWFwIGZvciBlYWNoIGNoYW5uZWwgaW50byBhIHNpbmdsZSBzY2FsYXIgYnkgYXZlcmFnaW5nLiBGb3IgYSBmZWF0dXJlIG1hcCBvZiBzaGFwZSAoTiwgQywgSCwgVyksIEdBUCBwcm9kdWNlcyAoTiwgQykuIEEgZmluYWwgbGluZWFyIGxheWVyIHRoZW4gbWFwcyBD4oaSbnVtX2NsYXNzZXMuIFRoaXMgcmVwbGFjZXMgdGhlIHRyYWRpdGlvbmFsIGZsYXR0ZW4gKyBGQyBhcHByb2FjaDogZm9yIEFsZXhOZXRcdTAwMjdzIDbDlzbDlzI1NiBmaW5hbCBjb252LCB0aGUgRkMgbGF5ZXJzIGhhZCAyNTbDlzbDlzbDlzQwOTYg4omIIDM3LjdNIHBhcmFtZXRlcnMuIEdBUCB1c2VzIDAgZXh0cmEgcGFyYW1ldGVycyBmb3IgdGhlIHNwYXRpYWwgYWdncmVnYXRpb24gc3RlcCBhbmQgb25seSBDw5dudW1fY2xhc3NlcyBmb3IgdGhlIGZpbmFsIGxheWVyLiBMaW4gZXQgYWwuICgyMDEzLCBOZXR3b3JrIGluIE5ldHdvcmspIGludHJvZHVjZWQgR0FQOyBpdCBiZWNhbWUgdW5pdmVyc2FsIHdpdGggUmVzTmV0LiBHQVAgYWxzbyBhY3RzIGFzIGEgc3RydWN0dXJhbCByZWd1bGFyaXNlcjogZWFjaCBjaGFubmVsIG11c3QgcHJvZHVjZSBhIGNsYXNzLWRpc2NyaW1pbmF0aXZlIGFjdGl2YXRpb24gbWFwIGF2ZXJhZ2VkIG92ZXIgdGhlIHdob2xlIHNwYXRpYWwgZXh0ZW50IOKAlCB0aGlzIGlzIHRoZSBiYXNpcyBmb3IgY2xhc3MgYWN0aXZhdGlvbiBtYXBzIChDQU0pLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBSZXNOZXRIZWFkX0ZDKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiVHJhZGl0aW9uYWw6IGZsYXR0ZW4gKyB0d28gRkMgbGF5ZXJzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBDPTUxMiwgSD03LCBXPTcsIG51bV9jbGFzc2VzPTEwMDApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5mYzEgPSBubi5MaW5lYXIoQyAqIEggKiBXLCA0MDk2KVxuICAgICAgICBzZWxmLmZjMiA9IG5uLkxpbmVhcig0MDk2LCBudW1fY2xhc3NlcylcbiAgICAgICAgc2VsZi5kcm9wID0gbm4uRHJvcG91dCgwLjUpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHggPSB4LmZsYXR0ZW4oMSlcbiAgICAgICAgcmV0dXJuIHNlbGYuZmMyKHNlbGYuZHJvcCh0b3JjaC5yZWx1KHNlbGYuZmMxKHgpKSkpXG5cbmNsYXNzIFJlc05ldEhlYWRfR0FQKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTW9kZXJuOiBnbG9iYWwgYXZlcmFnZSBwb29sICsgc2luZ2xlIGxpbmVhci5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgQz01MTIsIG51bV9jbGFzc2VzPTEwMDApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5nYXAgPSBubi5BZGFwdGl2ZUF2Z1Bvb2wyZCgxKVxuICAgICAgICBzZWxmLmZjICA9IG5uLkxpbmVhcihDLCBudW1fY2xhc3NlcylcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYuZmMoc2VsZi5nYXAoeCkuc3F1ZWV6ZSgtMSkuc3F1ZWV6ZSgtMSkpXG5cbmZjX2hlYWQgID0gUmVzTmV0SGVhZF9GQygpXG5nYXBfaGVhZCA9IFJlc05ldEhlYWRfR0FQKClcblxucF9mYyAgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIGZjX2hlYWQucGFyYW1ldGVycygpKVxucF9nYXAgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIGdhcF9oZWFkLnBhcmFtZXRlcnMoKSlcbnByaW50KGZcdTAwMjdGQyBoZWFkIHBhcmFtczogIHtwX2ZjOix9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0dBUCBoZWFkIHBhcmFtczoge3BfZ2FwOix9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JlZHVjdGlvbjoge3BfZmMvcF9nYXA6LjFmfXggZmV3ZXIgcGFyYW1ldGVyc1x1MDAyNylcblxueCA9IHRvcmNoLnJhbmRuKDIsIDUxMiwgNywgNylcbnByaW50KGZcdTAwMjdcXG5GQyAgb3V0cHV0OiB7dHVwbGUoZmNfaGVhZCh4KS5zaGFwZSl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0dBUCBvdXRwdXQ6IHt0dXBsZShnYXBfaGVhZCh4KS5zaGFwZSl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFkYXB0aXZlIFBvb2xpbmcg4oCUIFZhcmlhYmxlIElucHV0IFNpemVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJubi5BZGFwdGl2ZUF2Z1Bvb2wyZChvdXRwdXRfc2l6ZSkgYW5kIG5uLkFkYXB0aXZlTWF4UG9vbDJkKG91dHB1dF9zaXplKSBwcm9kdWNlIGEgZml4ZWQgb3V0cHV0IHNpemUgcmVnYXJkbGVzcyBvZiB0aGUgaW5wdXQgc3BhdGlhbCBkaW1lbnNpb25zLiBUaGUgcG9vbCB3aW5kb3cgYW5kIHN0cmlkZSBhcmUgY29tcHV0ZWQgYXV0b21hdGljYWxseTogc3RyaWRlID0g4oyKSF9pbiAvIEhfb3V04oyLLCBrZXJuZWwgPSBIX2luIC0gKEhfb3V0IC0gMSnCt3N0cmlkZS4gVGhpcyBlbmFibGVzIGEgbmV0d29yayB0cmFpbmVkIG9uIG9uZSBpbWFnZSBzaXplIHRvIGJlIGV2YWx1YXRlZCBvbiBhbnkgb3RoZXIgc2l6ZSDigJQgY3JpdGljYWwgZm9yIGZ1bGx5LWNvbnZvbHV0aW9uYWwgZXZhbHVhdGlvbiwgdGVzdC10aW1lIGF1Z21lbnRhdGlvbiB3aXRoIGRpZmZlcmVudCBjcm9wIHNpemVzLCBhbmQgaW5mZXJlbmNlIG9uIHZhcmlhYmxlLXJlc29sdXRpb24gaW5wdXRzIChkb2N1bWVudHMsIG1lZGljYWwgc2NhbnMpLiB0b3JjaHZpc2lvbiBtb2RlbHMgdXNlIEFkYXB0aXZlQXZnUG9vbDJkKDEpIGFzIHRoZWlyIGZpbmFsIHBvb2wsIG1ha2luZyB0aGVtIHJlc29sdXRpb24tYWdub3N0aWMgZnJvbSB0aGUgaGVhZCBvbndhcmRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5wb29sID0gbm4uQWRhcHRpdmVBdmdQb29sMmQoKDcsIDcpKVxuXG5wcmludChmXHUwMDI3e1x1MDAyN0lucHV0IHNoYXBlXHUwMDI3Olx1MDAzYzIwfSB7XHUwMDI3T3V0cHV0IHNoYXBlXHUwMDI3Olx1MDAzYzIwfSB7XHUwMDI3UG9vbCB3aW5kb3cgKGFwcHJveC4pXHUwMDI3fVx1MDAyNylcbmZvciBILCBXIGluIFsoNyw3KSwgKDE0LDE0KSwgKDI4LDI4KSwgKDU2LDU2KSwgKDIyNCwyMjQpLCAoMTEyLDg1KV06XG4gICAgeCA9IHRvcmNoLnJhbmRuKDEsIDUxMiwgSCwgVylcbiAgICBvdXQgPSBwb29sKHgpXG4gICAgc3RyaWRlX2ggPSBIIC8vIDdcbiAgICBrZXJuZWxfaCA9IEggLSAoNy0xKSpzdHJpZGVfaFxuICAgIHByaW50KGZcdTAwMjcoMSw1MTIse0h9LHtXfSl7XCJcIjpcdTAwM2N7bWF4KDAsOC1sZW4oc3RyKEgpKS1sZW4oc3RyKFcpKSl9fSAtXHUwMDNlIHt0dXBsZShvdXQuc2hhcGUpIXM6XHUwMDNjMjB9IH57a2VybmVsX2h9eHtrZXJuZWxfaH1cdTAwMjcpXG5cbiMgR2xvYmFsIGFkYXB0aXZlIHBvb2w6IG91dHB1dCBzaXplID0gKDEsMSlcbmdhcDEgPSBubi5BZGFwdGl2ZUF2Z1Bvb2wyZCgxKVxuZm9yIEggaW4gWzcsIDE0LCAyOF06XG4gICAgeCA9IHRvcmNoLnJhbmRuKDIsIDI1NiwgSCwgSClcbiAgICBvdXQgPSBnYXAxKHgpLnNoYXBlXG4gICAgcHJpbnQoZlx1MDAyN0dsb2JhbDogKDIsMjU2LHtIfSx7SH0pIC1cdTAwM2Uge291dH0gIChhbHdheXMgKDIsMjU2LDEsMSkpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwYXRpYWwgUHlyYW1pZCBQb29saW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTcGF0aWFsIFB5cmFtaWQgUG9vbGluZyAoU1BQLCBIZSBldCBhbC4gMjAxNSkgcG9vbHMgZmVhdHVyZSBtYXBzIGF0IG11bHRpcGxlIHNjYWxlcyDigJQgZS5nLiwgMcOXMSwgMsOXMiwgNMOXNCDigJQgYW5kIGNvbmNhdGVuYXRlcyB0aGUgcmVzdWx0cy4gVGhpcyBhbGxvd3MgYSBuZXR3b3JrIHRvIGhhbmRsZSBhcmJpdHJhcnkgaW5wdXQgc2l6ZXMgYW5kIGNhcHR1cmVzIG11bHRpLXNjYWxlIGNvbnRleHQgaW4gYSBzaW5nbGUgcGFzcy4gRm9yIGEgQy1jaGFubmVsIGlucHV0LCBTUFAgcHJvZHVjZXMgQ8OXKDErNCsxNikgPSAyMUMgZmVhdHVyZXMgKGZvciB0aHJlZSBweXJhbWlkIGxldmVscykuIFNQUC1OZXQgd2FzIHRoZSBmaXJzdCB0byBhcHBseSB0aGlzIGluIENOTiBjbGFzc2lmaWNhdGlvbiwgbWFraW5nIGRldGVjdGlvbiBuZXR3b3JrcyB0aGF0IHJlc2l6ZSBpbnB1dHMgYXZvaWRhYmxlLiBZT0xPXHUwMDI3cyBTUFAgbW9kdWxlICh0aHJlZSBwYXJhbGxlbCBtYXgtcG9vbHMgd2l0aCBrZXJuZWwgNSwgOSwgMTMgYW5kIHNhbWUgcGFkZGluZywgdGhlbiBjb25jYXQpIGNhcHR1cmVzIG11bHRpLXNjYWxlIGNvbnRleHQgaW4gdGhlIGJhY2tib25lIHdpdGhvdXQgc3BhdGlhbCBweXJhbWlkIGxldmVscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgU3BhdGlhbFB5cmFtaWRQb29saW5nKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTXVsdGktc2NhbGUgcG9vbGluZzogcG9vbHMgdG8gZWFjaCBsZXZlbCB0aGVuIGNvbmNhdGVuYXRlcy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbGV2ZWxzPSgxLCAyLCA0KSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBvb2xzID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBubi5BZGFwdGl2ZU1heFBvb2wyZChsZXZlbCkgZm9yIGxldmVsIGluIGxldmVsc1xuICAgICAgICBdKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgICMgeDogKE4sIEMsIEgsIFcpXG4gICAgICAgIHBhcnRzID0gW3Bvb2woeCkuZmxhdHRlbigyKSBmb3IgcG9vbCBpbiBzZWxmLnBvb2xzXSAgIyBlYWNoOiAoTixDLGxldmVsXjIpXG4gICAgICAgIHJldHVybiB0b3JjaC5jYXQocGFydHMsIGRpbT0yKS5mbGF0dGVuKDEpICAgICAgICAgICAgICMgKE4sIEMqKDErNCsxNisuLi4pKVxuXG4gICAgZGVmIG91dF9mZWF0dXJlcyhzZWxmLCBDLCBsZXZlbHM9KDEsMiw0KSk6XG4gICAgICAgIHJldHVybiBDICogc3VtKGwqbCBmb3IgbCBpbiBsZXZlbHMpXG5cbnNwcCA9IFNwYXRpYWxQeXJhbWlkUG9vbGluZyhsZXZlbHM9KDEsIDIsIDQpKVxuQyA9IDUxMlxuIyBTYW1lIG5ldHdvcmsgb3V0cHV0IHdpdGggZGlmZmVyZW50IGlucHV0IHNpemVzXG5mb3IgSCBpbiBbNywgMTQsIDE5LCAyOF06XG4gICAgeCA9IHRvcmNoLnJhbmRuKDIsIEMsIEgsIEgpXG4gICAgb3V0ID0gc3BwKHgpXG4gICAgcHJpbnQoZlx1MDAyN0lucHV0ICgyLHtDfSx7SH0se0h9KSAtXHUwMDNlIFNQUCBvdXRwdXQge3R1cGxlKG91dC5zaGFwZSl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1xcbk91dHB1dCBkaW0gYWx3YXlzOiB7Q30gKiAoMSs0KzE2KSA9IHtDKjIxfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiU3RyaWRlZCBDb252IGFzIGEgUG9vbGluZyBBbHRlcm5hdGl2ZSIsImNvbnRlbnQiOiJBIDPDlzMgY29udiB3aXRoIHN0cmlkZSAyIGFjaGlldmVzIHRoZSBzYW1lIHNwYXRpYWwgZG93bnNhbXBsaW5nIGFzIGEgMsOXMiBtYXggcG9vbCBidXQgd2l0aCBsZWFybmFibGUgd2VpZ2h0cywgbm8gaW5mb3JtYXRpb24gYm90dGxlbmVjayBmcm9tIHRoZSBoYXJkLW1heCBvcGVyYXRpb24sIGFuZCBiZXR0ZXIgZ3JhZGllbnQgZmxvdy4gUmVzTmV0XHUwMDI3cyBkZXNpZ24gcmVwbGFjZWQgdGhlIGVhcmx5IHBvb2xpbmcgbGF5ZXJzIHdpdGggc3RyaWRlZCBjb252b2x1dGlvbnMsIGVuYWJsaW5nIGdyYWRpZW50cyB0byBmbG93IHRocm91Z2ggdGhlIHNwYXRpYWwgZG93bnNhbXBsaW5nIHN0ZXAgd2l0aG91dCB0aGUgZGVhZC1ncmFkaWVudCBwcm9ibGVtIG9mIG1heCBwb29sXHUwMDI3cyBoYXJkIHNlbGVjdGlvbi4gRm9yIG1vZGVybiBhcmNoaXRlY3R1cmVzLCBzdHJpZGVkIGNvbnYgKG9yIHN0cmlkZWQgZGVwdGh3aXNlIGNvbnYgaW4gTW9iaWxlTmV0KSBpcyBnZW5lcmFsbHkgcHJlZmVycmVkIG92ZXIgbWF4IHBvb2xpbmcgZm9yIGRvd25zYW1wbGluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcmFkaWVudCBGbG93IFRocm91Z2ggUG9vbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWF4IHBvb2xpbmcgaGFzIGEgc3dpdGNoIG1lY2hhbmlzbTogZHVyaW5nIHRoZSBiYWNrd2FyZCBwYXNzLCBncmFkaWVudCBmbG93cyBvbmx5IHRvIHRoZSBtYXhpbXVtIGVsZW1lbnQgaW4gZWFjaCB3aW5kb3csIHdoaWxlIGFsbCBvdGhlciBlbGVtZW50cyByZWNlaXZlIHplcm8gZ3JhZGllbnQuIFRoaXMgY2FuIGxlYWQgdG8gc3BhcnNlIGdyYWRpZW50cyBpbiBlYXJseSBsYXllcnMgaWYgbWF4IHBvb2xpbmcgaXMgYXBwbGllZCBhZ2dyZXNzaXZlbHkuIEF2ZXJhZ2UgcG9vbGluZyBkaXN0cmlidXRlcyBncmFkaWVudCBlcXVhbGx5IGFjcm9zcyBhbGwgd2luZG93IGVsZW1lbnRzLiBHbG9iYWwgYXZlcmFnZSBwb29saW5nIGRpc3RyaWJ1dGVzIGdyYWRpZW50IGFjcm9zcyB0aGUgZW50aXJlIEjDl1cgZmVhdHVyZSBtYXAg4oCUIHRoZSBzbW9vdGhlc3Qgb3B0aW9uLCBlbnN1cmluZyBhbGwgc3BhdGlhbCBsb2NhdGlvbnMgcmVjZWl2ZSB0cmFpbmluZyBzaWduYWwuIFN0cmlkZWQgY29udiBoYXMgdGhlIG1vc3QgZmxleGlibGUgZ3JhZGllbnQgcm91dGluZyBiZWNhdXNlIHRoZSAzw5czIGtlcm5lbCB3ZWlnaHRzIGFyZSBsZWFybmVkLiBXaGVuIGRpYWdub3NpbmcgdmFuaXNoaW5nIGdyYWRpZW50cyBpbiBlYXJseSBsYXllcnMsIGNoZWNrIHdoZXRoZXIgYWdncmVzc2l2ZSBtYXggcG9vbGluZyBpcyBibG9ja2luZyBncmFkaWVudCBmbG93LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQb29saW5nIFR5cGUiLCJTcGF0aWFsIEludmFyaWFuY2UiLCJHcmFkaWVudCBGbG93IiwiUGFyYW1zIiwiSGFuZGxlcyBWYXJpYWJsZSBTaXplIiwiVHlwaWNhbCBVc2UiXSwicm93cyI6W1siTWF4IHBvb2wgMsOXMiBzMiIsIkhpZ2ggKGhhcmQgc2VsZWN0KSIsIlNwYXJzZSAobWF4IG9ubHkpIiwiMCIsIk5vIChmaXhlZCBzdHJpZGUpIiwiRWFybHkgQ05OIGxheWVycyAoVkdHLCBBbGV4TmV0KSJdLFsiQXZlcmFnZSBwb29sIDLDlzIgczIiLCJNZWRpdW0gKHNtb290aCkiLCJEZW5zZSAoZXF1YWwpIiwiMCIsIk5vIiwiUmFyZSDigJQgZ2xvYmFsIGF2ZyBwcmVmZXJyZWQiXSxbIkdsb2JhbCBhdmcgcG9vbCIsIkZ1bGwgc3BhdGlhbCBhdmciLCJGdWxseSBkaXN0cmlidXRlZCIsIjAiLCJZZXMgKGNvbGxhcHNlcyBhbnkgSHhXKSIsIkZpbmFsIHBvb2wgYmVmb3JlIGNsYXNzaWZpZXIiXSxbIkFkYXB0aXZlIGF2ZyBwb29sIiwiQ29uZmlndXJhYmxlIiwiRGlzdHJpYnV0ZWQiLCIwIiwiWWVzIiwiVHJhbnNmZXIgbGVhcm5pbmcsIHZhcmlhYmxlIHJlcyJdLFsiU3BhdGlhbCBweXJhbWlkIiwiTXVsdGktc2NhbGUiLCJEaXN0cmlidXRlZCIsIjAiLCJZZXMiLCJEZXRlY3Rpb24gKFNQUC1OZXQsIFlPTE8pIl0sWyJTdHJpZGVkIGNvbnYgM8OXMyBzMiIsIkxlYXJuZWQiLCJGdWxsICh2aWEgY29udikiLCJrwrLDl0PDl0MiLCJObyIsIk1vZGVybiBSZXNOZXQsIE1vYmlsZU5ldCJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJGLm1heF9wb29sMmQoeCwga2VybmVsX3NpemU9MikgYW5kIG5uLk1heFBvb2wyZCgyKSBhcmUgZXF1aXZhbGVudDsgdXNlIHRoZSBtb2R1bGUgZm9yIG5uLlNlcXVlbnRpYWwuIiwiR2xvYmFsIG1heCBwb29saW5nIChub3QgYXZlcmFnZSkgaXMgdXNlZCBpbiBUZXh0Q05OOiB0YWtlcyB0aGUgbW9zdCBhY3RpdmF0ZWQgZmVhdHVyZSBwZXIgZmlsdGVyIGFjcm9zcyBhbGwgcG9zaXRpb25zLiIsIlJPSSBwb29saW5nIChGYXN0IFItQ05OKSBpcyBhZGFwdGl2ZSBtYXggcG9vbCBhcHBsaWVkIHRvIHJlZ2lvbiBwcm9wb3NhbHMgb2YgdmFyaWFibGUgc2l6ZS4iLCJST0kgYWxpZ24gKE1hc2sgUi1DTk4pIGZpeGVzIHRoZSBxdWFudGlzYXRpb24gZXJyb3Igb2YgUk9JIHBvb2xpbmcgdXNpbmcgYmlsaW5lYXIgaW50ZXJwb2xhdGlvbi4iLCJGb3IgMUQgaW5wdXRzICh0aW1lIHNlcmllcyksIG5uLkFkYXB0aXZlQXZnUG9vbDFkKDEpIGlzIHRoZSBHQVAgZXF1aXZhbGVudCDigJQgY29sbGFwc2VzIHRoZSBzZXF1ZW5jZSB0byBvbmUgdmFsdWUgcGVyIGNoYW5uZWwuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF0dGVudGlvbiBQb29saW5nIGFuZCBMZWFybmVkIEFnZ3JlZ2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdHRlbnRpb24gcG9vbGluZyBnZW5lcmFsaXNlcyBhdmVyYWdlIHBvb2xpbmcgYnkgYXNzaWduaW5nIGxlYXJuZWQgd2VpZ2h0cyB0byBlYWNoIHNwYXRpYWwgbG9jYXRpb24gYmVmb3JlIGFnZ3JlZ2F0aW5nLiBHaXZlbiBmZWF0dXJlIG1hcCBGIOKIiCDihJ3htpzLo+G0tMuj4bWCLCBhdHRlbnRpb24gcG9vbGluZyBjb21wdXRlcyBhIHdlaWdodCBtYXAgQSA9IHNvZnRtYXgoV2YoRikpIGFuZCByZXR1cm5zIM6j4bWi4rG8IEHhtaLisbwgwrcgRuG1ouKxvC4gVGhpcyBpcyB1c2VkIGluIENMSVBcdTAwMjdzIGltYWdlIGVuY29kZXIgKG11bHRpLWhlYWQgYXR0ZW50aW9uIHBvb2xpbmcgb3ZlciBWaVQgcGF0Y2ggdG9rZW5zKSwgaW4gRElOTyBzZWxmLXN1cGVydmlzZWQgZmVhdHVyZXMgKGF0dGVudGlvbiBmcm9tIFtDTFNdIHRva2VuKSwgYW5kIGluIG1lZGljYWwgaW1hZ2luZyBtb2RlbHMgd2hlcmUgZ2xvYmFsIGF2ZXJhZ2UgcG9vbGluZyBsb3NlcyBsb2NhbGlzZWQgcGF0aG9sb2d5IHNpZ25hbHMuIFRoZSBvdXRwdXQgaXMgc3RpbGwgYSBzaW5nbGUgdmVjdG9yIHBlciBzYW1wbGUg4oCUIHNhbWUgc2hhcGUgYXMgR0FQIOKAlCBidXQgd2l0aCBzcGF0aWFsbHkgYWRhcHRpdmUgd2VpZ2h0aW5nLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3F1ZWV6ZS1hbmQtRXhjaXRhdGlvbiAoU0UpIG5ldHdvcmtzIGFwcGx5IGEgc29mdCBjaGFubmVsLXdpc2UgYXR0ZW50aW9uIGFmdGVyIHBvb2xpbmc6IEdBUCDihpIgRkMg4oaSIFJlTFUg4oaSIEZDIOKGkiBTaWdtb2lkIHByb2R1Y2VzIGEgcGVyLWNoYW5uZWwgd2VpZ2h0IHZlY3RvciB0aGF0IHJlc2NhbGVzIHRoZSBmZWF0dXJlIG1hcC4gVGhpcyByZWNhbGlicmF0ZXMgY2hhbm5lbCBpbXBvcnRhbmNlIGdsb2JhbGx5IHVzaW5nIG9ubHkgMsOXQ8KyL3IgcGFyYW1ldGVycyAociBpcyB0aGUgcmVkdWN0aW9uIHJhdGlvLCB0eXBpY2FsbHkgMTYpLiBTRSBibG9ja3MgYWRkIH4yJSBleHRyYSBwYXJhbWV0ZXJzIGJ1dCBjb25zaXN0ZW50bHkgaW1wcm92ZSBhY2N1cmFjeSBieSB+MC414oCTMSUgdG9wLTEgb24gSW1hZ2VOZXQuIEVmZmljaWVudE5ldCBpbmNvcnBvcmF0ZXMgU0UgYmxvY2tzIGluIGV2ZXJ5IE1CQ29udiBsYXllci4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdlTSAoR2VuZXJhbGlzZWQgTWVhbiBQb29saW5nKTogRnBvb2wgPSAoMS9uIM6jIGbhtZYpXigxL3ApIOKAlCBnZW5lcmFsaXNlcyBhdmcgKHA9MSkgYW5kIG1heCAocOKGkuKInikgcG9vbGluZyBmb3IgcmV0cmlldmFsLiIsIk5ldFZMQUQ6IHNvZnQtYXNzaWdubWVudCBvZiBmZWF0dXJlcyB0byBjbHVzdGVyIGNlbnRyZXMgZm9sbG93ZWQgYnkgcmVzaWR1YWwgYWdncmVnYXRpb24g4oCUIGRpZmZlcmVudGlhYmxlIFZMQUQgcG9vbGluZy4iLCJQb3dlciBBdmVyYWdlIFBvb2xpbmcgKFBBUCk6IGxlYXJuYWJsZSBwZXItY2hhbm5lbCBwIGV4cG9uZW50IGZvciByZXRyaWV2YWwgYW5kIHBsYWNlIHJlY29nbml0aW9uIHRhc2tzLiIsIlNlY29uZC1vcmRlciBwb29saW5nIChpU1FSVC1DT1YpOiBjb3ZhcmlhbmNlIG1hdHJpeCBvZiBzcGF0aWFsIGZlYXR1cmVzIGluc3RlYWQgb2YgZmlyc3Qtb3JkZXIgbWVhbiDigJQgY2FwdHVyZXMgZmVhdHVyZSBjb3JyZWxhdGlvbnMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Pooling Operations — Max, Average, Global, and Adaptive

Pooling aggregates spatial information, reduces feature map size, and introduces a degree of spatial invariance. The choice of pooling strategy has downstream effects on parameter count, gradient flow, spatial invariance, and the ability to handle variable-size inputs. Global average pooling (GAP) replaced the fully-connected classifier in modern networks, cutting millions of parameters. Adaptive pooling enables batch inference on images of different sizes. Understanding when to pool, how much, and which variant determines whether a model is compact and generalises well or is overparameterised and brittle.

## Max Pooling vs Average Pooling

Max pooling selects the maximum activation in each window: it is a hard selector, detecting whether a feature is present anywhere in the region (feature detectiveness). Average pooling computes the mean: it integrates evidence across the region (smoother, less sensitive to exact location). Max pooling has stronger spatial invariance — a shifted feature still produces the same max. Average pooling discards the peak magnitude. For early layers detecting edge and texture features, max pooling is standard. For the final global pooling before the classifier, average pooling is preferred because it uses information from all spatial locations rather than just one peak.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

np.random.seed(42)
# Simulate a feature map with a sharp activation peak
feat = torch.zeros(1, 1, 8, 8)
feat[0, 0, 3, 4] = 5.0   # sharp peak
feat[0, 0, :, :] += torch.randn(8, 8) * 0.1  # noise

max_pool = nn.MaxPool2d(2, stride=2)
avg_pool = nn.AvgPool2d(2, stride=2)

max_out = max_pool(feat)
avg_out = avg_pool(feat)

print('Input feature map (8x8):')
print(feat[0,0].numpy().round(2))
print('\nAfter MaxPool2d(2,2) — 4x4:')
print(max_out[0,0].detach().numpy().round(2))
print('\nAfter AvgPool2d(2,2) — 4x4:')
print(avg_out[0,0].detach().numpy().round(2))
print('\nMax pool preserves peak magnitude; avg pool spreads it.')
```

## Global Average Pooling — Replacing the Classifier

Global Average Pooling (GAP) collapses the entire H×W spatial map for each channel into a single scalar by averaging. For a feature map of shape (N, C, H, W), GAP produces (N, C). A final linear layer then maps C→num_classes. This replaces the traditional flatten + FC approach: for AlexNet's 6×6×256 final conv, the FC layers had 256×6×6×4096 ≈ 37.7M parameters. GAP uses 0 extra parameters for the spatial aggregation step and only C×num_classes for the final layer. Lin et al. (2013, Network in Network) introduced GAP; it became universal with ResNet. GAP also acts as a structural regulariser: each channel must produce a class-discriminative activation map averaged over the whole spatial extent — this is the basis for class activation maps (CAM).

```python
import torch
import torch.nn as nn

class ResNetHead_FC(nn.Module):
    """Traditional: flatten + two FC layers."""
    def __init__(self, C=512, H=7, W=7, num_classes=1000):
        super().__init__()
        self.fc1 = nn.Linear(C * H * W, 4096)
        self.fc2 = nn.Linear(4096, num_classes)
        self.drop = nn.Dropout(0.5)
    def forward(self, x):
        x = x.flatten(1)
        return self.fc2(self.drop(torch.relu(self.fc1(x))))

class ResNetHead_GAP(nn.Module):
    """Modern: global average pool + single linear."""
    def __init__(self, C=512, num_classes=1000):
        super().__init__()
        self.gap = nn.AdaptiveAvgPool2d(1)
        self.fc  = nn.Linear(C, num_classes)
    def forward(self, x):
        return self.fc(self.gap(x).squeeze(-1).squeeze(-1))

fc_head  = ResNetHead_FC()
gap_head = ResNetHead_GAP()

p_fc  = sum(p.numel() for p in fc_head.parameters())
p_gap = sum(p.numel() for p in gap_head.parameters())
print(f'FC head params:  {p_fc:,}')
print(f'GAP head params: {p_gap:,}')
print(f'Reduction: {p_fc/p_gap:.1f}x fewer parameters')

x = torch.randn(2, 512, 7, 7)
print(f'\nFC  output: {tuple(fc_head(x).shape)}')
print(f'GAP output: {tuple(gap_head(x).shape)}')
```

## Adaptive Pooling — Variable Input Sizes

nn.AdaptiveAvgPool2d(output_size) and nn.AdaptiveMaxPool2d(output_size) produce a fixed output size regardless of the input spatial dimensions. The pool window and stride are computed automatically: stride = ⌊H_in / H_out⌋, kernel = H_in - (H_out - 1)·stride. This enables a network trained on one image size to be evaluated on any other size — critical for fully-convolutional evaluation, test-time augmentation with different crop sizes, and inference on variable-resolution inputs (documents, medical scans). torchvision models use AdaptiveAvgPool2d(1) as their final pool, making them resolution-agnostic from the head onwards.

```python
import torch
import torch.nn as nn

pool = nn.AdaptiveAvgPool2d((7, 7))

print(f'{'Input shape':<20} {'Output shape':<20} {'Pool window (approx.)'}')
for H, W in [(7,7), (14,14), (28,28), (56,56), (224,224), (112,85)]:
    x = torch.randn(1, 512, H, W)
    out = pool(x)
    stride_h = H // 7
    kernel_h = H - (7-1)*stride_h
    print(f'(1,512,{H},{W}){"":<{max(0,8-len(str(H))-len(str(W)))}} -> {tuple(out.shape)!s:<20} ~{kernel_h}x{kernel_h}')

# Global adaptive pool: output size = (1,1)
gap1 = nn.AdaptiveAvgPool2d(1)
for H in [7, 14, 28]:
    x = torch.randn(2, 256, H, H)
    out = gap1(x).shape
    print(f'Global: (2,256,{H},{H}) -> {out}  (always (2,256,1,1))')
```

## Spatial Pyramid Pooling

Spatial Pyramid Pooling (SPP, He et al. 2015) pools feature maps at multiple scales — e.g., 1×1, 2×2, 4×4 — and concatenates the results. This allows a network to handle arbitrary input sizes and captures multi-scale context in a single pass. For a C-channel input, SPP produces C×(1+4+16) = 21C features (for three pyramid levels). SPP-Net was the first to apply this in CNN classification, making detection networks that resize inputs avoidable. YOLO's SPP module (three parallel max-pools with kernel 5, 9, 13 and same padding, then concat) captures multi-scale context in the backbone without spatial pyramid levels.

```python
import torch
import torch.nn as nn

class SpatialPyramidPooling(nn.Module):
    """Multi-scale pooling: pools to each level then concatenates."""
    def __init__(self, levels=(1, 2, 4)):
        super().__init__()
        self.pools = nn.ModuleList([
            nn.AdaptiveMaxPool2d(level) for level in levels
        ])

    def forward(self, x):
        # x: (N, C, H, W)
        parts = [pool(x).flatten(2) for pool in self.pools]  # each: (N,C,level^2)
        return torch.cat(parts, dim=2).flatten(1)             # (N, C*(1+4+16+...))

    def out_features(self, C, levels=(1,2,4)):
        return C * sum(l*l for l in levels)

spp = SpatialPyramidPooling(levels=(1, 2, 4))
C = 512
# Same network output with different input sizes
for H in [7, 14, 19, 28]:
    x = torch.randn(2, C, H, H)
    out = spp(x)
    print(f'Input (2,{C},{H},{H}) -> SPP output {tuple(out.shape)}')
print(f'\nOutput dim always: {C} * (1+4+16) = {C*21}')
```

> **Strided Conv as a Pooling Alternative**: A 3×3 conv with stride 2 achieves the same spatial downsampling as a 2×2 max pool but with learnable weights, no information bottleneck from the hard-max operation, and better gradient flow. ResNet's design replaced the early pooling layers with strided convolutions, enabling gradients to flow through the spatial downsampling step without the dead-gradient problem of max pool's hard selection. For modern architectures, strided conv (or strided depthwise conv in MobileNet) is generally preferred over max pooling for downsampling.

## Gradient Flow Through Pooling

Max pooling has a switch mechanism: during the backward pass, gradient flows only to the maximum element in each window, while all other elements receive zero gradient. This can lead to sparse gradients in early layers if max pooling is applied aggressively. Average pooling distributes gradient equally across all window elements. Global average pooling distributes gradient across the entire H×W feature map — the smoothest option, ensuring all spatial locations receive training signal. Strided conv has the most flexible gradient routing because the 3×3 kernel weights are learned. When diagnosing vanishing gradients in early layers, check whether aggressive max pooling is blocking gradient flow.

| Pooling Type | Spatial Invariance | Gradient Flow | Params | Handles Variable Size | Typical Use |
| --- | --- | --- | --- | --- | --- |
| Max pool 2×2 s2 | High (hard select) | Sparse (max only) | 0 | No (fixed stride) | Early CNN layers (VGG, AlexNet) |
| Average pool 2×2 s2 | Medium (smooth) | Dense (equal) | 0 | No | Rare — global avg preferred |
| Global avg pool | Full spatial avg | Fully distributed | 0 | Yes (collapses any HxW) | Final pool before classifier |
| Adaptive avg pool | Configurable | Distributed | 0 | Yes | Transfer learning, variable res |
| Spatial pyramid | Multi-scale | Distributed | 0 | Yes | Detection (SPP-Net, YOLO) |
| Strided conv 3×3 s2 | Learned | Full (via conv) | k²×C×C | No | Modern ResNet, MobileNet |

- F.max_pool2d(x, kernel_size=2) and nn.MaxPool2d(2) are equivalent; use the module for nn.Sequential.
- Global max pooling (not average) is used in TextCNN: takes the most activated feature per filter across all positions.
- ROI pooling (Fast R-CNN) is adaptive max pool applied to region proposals of variable size.
- ROI align (Mask R-CNN) fixes the quantisation error of ROI pooling using bilinear interpolation.
- For 1D inputs (time series), nn.AdaptiveAvgPool1d(1) is the GAP equivalent — collapses the sequence to one value per channel.

## Attention Pooling and Learned Aggregation

Attention pooling generalises average pooling by assigning learned weights to each spatial location before aggregating. Given feature map F ∈ ℝᶜˣᴴˣᵂ, attention pooling computes a weight map A = softmax(Wf(F)) and returns Σᵢⱼ Aᵢⱼ · Fᵢⱼ. This is used in CLIP's image encoder (multi-head attention pooling over ViT patch tokens), in DINO self-supervised features (attention from [CLS] token), and in medical imaging models where global average pooling loses localised pathology signals. The output is still a single vector per sample — same shape as GAP — but with spatially adaptive weighting.

Squeeze-and-Excitation (SE) networks apply a soft channel-wise attention after pooling: GAP → FC → ReLU → FC → Sigmoid produces a per-channel weight vector that rescales the feature map. This recalibrates channel importance globally using only 2×C²/r parameters (r is the reduction ratio, typically 16). SE blocks add ~2% extra parameters but consistently improve accuracy by ~0.5–1% top-1 on ImageNet. EfficientNet incorporates SE blocks in every MBConv layer.

- GeM (Generalised Mean Pooling): Fpool = (1/n Σ fᵖ)^(1/p) — generalises avg (p=1) and max (p→∞) pooling for retrieval.
- NetVLAD: soft-assignment of features to cluster centres followed by residual aggregation — differentiable VLAD pooling.
- Power Average Pooling (PAP): learnable per-channel p exponent for retrieval and place recognition tasks.
- Second-order pooling (iSQRT-COV): covariance matrix of spatial features instead of first-order mean — captures feature correlations.

---

