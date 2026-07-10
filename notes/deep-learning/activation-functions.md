---
title: "Activation Functions — ReLU, GELU, SiLU, and Friends"
slug: "activation-functions"
description: "Compare sigmoid, tanh, ReLU, Leaky ReLU, ELU, GELU, SiLU, and Mish — their mathematical forms, saturation behaviour, gradient properties, and when to use each in practice."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWN0aXZhdGlvbiBmdW5jdGlvbnMgYXJlIHRoZSBub24tbGluZWFyaXRpZXMgdGhhdCBnaXZlIG5ldXJhbCBuZXR3b3JrcyB0aGVpciBleHByZXNzaXZlIHBvd2VyLiBUaGUgY2hvaWNlIG9mIGFjdGl2YXRpb24gYWZmZWN0cyBncmFkaWVudCBmbG93LCB0cmFpbmluZyBzcGVlZCwgYW5kIG1vZGVsIHF1YWxpdHkuIEVhcmx5IG5ldHdvcmtzIHVzZWQgc2lnbW9pZCBhbmQgdGFuaDsgbW9kZXJuIENOTnMgZGVmYXVsdCB0byBSZUxVOyBUcmFuc2Zvcm1lcnMgYW5kIGxhcmdlIGxhbmd1YWdlIG1vZGVscyByZWx5IG9uIEdFTFUgYW5kIFNpTFUuIFVuZGVyc3RhbmRpbmcgZWFjaCBmdW5jdGlvblx1MDAyN3MgcHJvcGVydGllcyDigJQgc2F0dXJhdGlvbiwgemVyby1jZW50ZXJpbmcsIGRpZmZlcmVudGlhYmlsaXR5LCBhbmQgc3RvY2hhc3RpYyBpbnRlcnByZXRhdGlvbiDigJQgZ3VpZGVzIHdoaWNoIHRvIHJlYWNoIGZvciBpbiBhIG5ldyBhcmNoaXRlY3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2xhc3NpY2FsIEFjdGl2YXRpb25zOiBTaWdtb2lkIGFuZCBUYW5oIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaWdtb2lkIM+DKHgpID0gMS8oMStl4oG7y6MpIG1hcHMgdG8gKDAsMSkg4oCUIHVzZWZ1bCBmb3IgcHJvYmFiaWxpdGllcyBidXQgc2F0dXJhdGVzIGZvciB8eHwgXHUwMDNlIDQ6IGdyYWRpZW50IM+DXHUwMDI3KHgpID0gz4MoeCkoMS3Pgyh4KSkgaXMgYXQgbW9zdCAwLjI1IGFuZCBjb2xsYXBzZXMgdG8gbmVhciB6ZXJvIGZhciBmcm9tIHRoZSBvcmlnaW4uIE5vbi16ZXJvLWNlbnRlcmVkOiBvdXRwdXRzIGFsd2F5cyBwb3NpdGl2ZSwgc28gZ3JhZGllbnRzIG9uIFcgYXJlIGFsbC1wb3NpdGl2ZSBvciBhbGwtbmVnYXRpdmUg4oCUIHppZy16YWcgZ3JhZGllbnQgdXBkYXRlcy4gVGFuaCh4KSA9IChly6MtZeKBu8ujKS8oZcujK2XigbvLoykgbWFwcyB0byAoLTEsMSksIHplcm8tY2VudGVyZWQsIGRlcml2YXRpdmUgMS10YW5owrIoeCkgcGVha3MgYXQgMS4wIOKAlCBiZXR0ZXIgZ3JhZGllbnQgdGhhbiBzaWdtb2lkIGJ1dCBzdGlsbCBzYXR1cmF0ZXMuIEJvdGggYXJlIGxhcmdlbHkgcmVwbGFjZWQgYnkgUmVMVSB2YXJpYW50cyBpbiBoaWRkZW4gbGF5ZXJzOyBzaWdtb2lkIHN1cnZpdmVzIGluIG91dHB1dCBsYXllcnMgZm9yIGJpbmFyeSBjbGFzc2lmaWNhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZUxVIGFuZCBpdHMgVmFyaWFudHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlTFU6IGEgPSBtYXgoMCwgeCkuIE5vbi1zYXR1cmF0aW5nIGZvciB4IFx1MDAzZSAwLCBzcGFyc2UgKOKJiDUwJSB6ZXJvIGFjdGl2YXRpb25zKSwgY29tcHV0YXRpb25hbGx5IHRyaXZpYWwuIFByb2JsZW1zOiAoMSkgZGVhZCBuZXVyb25zIOKAlCBpZiB6IFx1MDAzYyAwIGZvciBhbGwgaW5wdXRzLCBncmFkaWVudCBpcyB6ZXJvIGFuZCB3ZWlnaHRzIG5ldmVyIHVwZGF0ZTsgKDIpIG5vdCB6ZXJvLWNlbnRlcmVkOyAoMykgbm90IGRpZmZlcmVudGlhYmxlIGF0IDAgKHN1YmdyYWRpZW50IDAgaXMgdXNlZCkuIExlYWt5IFJlTFU6IG1heCjOsXgsIHgpIHdpdGggzrE9MC4wMSDigJQgbm9uLXplcm8gZ3JhZGllbnQgZXZlcnl3aGVyZS4gUFJlTFU6IHNhbWUgYnV0IM6xIGlzIGEgbGVhcm5lZCBwYXJhbWV0ZXIgcGVyIGNoYW5uZWwuIEVMVTogeCBmb3IgeFx1MDAzZTAsIM6xKGXLoy0xKSBmb3IgeOKJpDAg4oCUIHNtb290aCBuZWdhdGl2ZSBzaWRlLCB6ZXJvLW1lYW4gb3V0cHV0cywgYnV0IHNsb3dlciBkdWUgdG8gZXhwLiBTRUxVIGlzIGEgc2NhbGVkIEVMVSBkZXNpZ25lZCBmb3Igc2VsZi1ub3JtYWxpc2luZyBuZXR3b3Jrcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb2Rlcm4gQWN0aXZhdGlvbnM6IEdFTFUsIFNpTFUsIGFuZCBNaXNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHRUxVIChHYXVzc2lhbiBFcnJvciBMaW5lYXIgVW5pdCk6IHggwrcgzqYoeCkgd2hlcmUgzqYgaXMgdGhlIENERiBvZiBOKDAsMSkuIFN0b2NoYXN0aWMgaW50ZXJwcmV0YXRpb246IHN0b2NoYXN0aWNhbGx5IHplcm8tZ2F0ZXMgeCB3aXRoIHByb2JhYmlsaXR5IM6mKHgpLiBTbW9vdGggZXZlcnl3aGVyZSwgbm9uLW1vbm90b25lIChzbWFsbCBuZWdhdGl2ZSBkaXAgYXJvdW5kIHg9LTAuMSkuIFVzZWQgaW4gQkVSVCwgR1BULTIvMywgVmlULiBBcHByb3hpbWF0ZWQgYXMgMC41eCgxK3Rhbmgo4oiaKDIvz4ApKHgrMC4wNDQ3MTV4wrMpKSkuIFNpTFUvU3dpc2g6IHjCt8+DKHgpIOKAlCBzaW1pbGFyIHNoYXBlIHRvIEdFTFUsIHVzZWQgaW4gRWZmaWNpZW50TmV0LCBNb2JpbGVOZXRWMywgTExhTUEuIE1pc2g6IHjCt3Rhbmgoc29mdHBsdXMoeCkpIOKAlCBzbW9vdGgsIG5vbi1tb25vdG9uZSwgc2xpZ2h0IHBlcmZvcm1hbmNlIGdhaW5zIHJlcG9ydGVkIG92ZXIgU3dpc2guIEFsbCB0aHJlZSBvdXRwZXJmb3JtIFJlTFUgb24gbGFuZ3VhZ2UgbW9kZWxzIGJlY2F1c2UgdGhlaXIgc21vb3RoLCBub24temVybyBuZWdhdGl2ZSBzaWRlIGhlbHBzIGdyYWRpZW50IGZsb3cuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbiMgSW1wbGVtZW50IGFsbCBhY3RpdmF0aW9ucyBmcm9tIHNjcmF0Y2hcbmRlZiBzaWdtb2lkKHgpOiAgcmV0dXJuIDEgLyAoMSArIG5wLmV4cCgtbnAuY2xpcCh4LCAtNTAwLCA1MDApKSlcbmRlZiB0YW5oX2ZuKHgpOiAgcmV0dXJuIG5wLnRhbmgoeClcbmRlZiByZWx1KHgpOiAgICAgcmV0dXJuIG5wLm1heGltdW0oMCwgeClcbmRlZiBsZWFreV9yZWx1KHgsIGFscGhhPTAuMDEpOiByZXR1cm4gbnAud2hlcmUoeCBcdTAwM2UgMCwgeCwgYWxwaGEgKiB4KVxuZGVmIGVsdSh4LCBhbHBoYT0xLjApOiByZXR1cm4gbnAud2hlcmUoeCBcdTAwM2UgMCwgeCwgYWxwaGEgKiAobnAuZXhwKG5wLmNsaXAoeCwtNTAsMCkpIC0gMSkpXG5cbmRlZiBnZWx1KHgpOlxuICAgICMgRXhhY3QgR0VMVSB2aWEgc3RhbmRhcmQgbm9ybWFsIENERlxuICAgIHJldHVybiB4ICogMC41ICogKDEgKyBucC52ZWN0b3JpemUobGFtYmRhIHY6IGZsb2F0KHRvcmNoLmVyZih0b3JjaC50ZW5zb3IodiAvIG5wLnNxcnQoMikpKSkpKHgpKVxuXG5kZWYgc2lsdSh4KTogIHJldHVybiB4ICogc2lnbW9pZCh4KSAgIyBTd2lzaFxuZGVmIG1pc2goeCk6ICByZXR1cm4geCAqIG5wLnRhbmgobnAubG9nMXAobnAuZXhwKG5wLmNsaXAoeCwgLTUwLCA1MCkpKSlcblxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG5mbnMgPSB7XG4gICAgXHUwMDI3c2lnbW9pZFx1MDAyNzogc2lnbW9pZCwgXHUwMDI3dGFuaFx1MDAyNzogdGFuaF9mbiwgXHUwMDI3cmVsdVx1MDAyNzogcmVsdSxcbiAgICBcdTAwMjdsZWFreV9yZWx1XHUwMDI3OiBsZWFreV9yZWx1LCBcdTAwMjdlbHVcdTAwMjc6IGVsdSwgXHUwMDI3Z2VsdVx1MDAyNzogZ2VsdSxcbiAgICBcdTAwMjdzaWx1XHUwMDI3OiBzaWx1LCBcdTAwMjdtaXNoXHUwMDI3OiBtaXNoXG59XG5wcmludChmXHUwMDI3e1wiQWN0aXZhdGlvblwiOlx1MDAzZTEyfSAge1wibWluXCI6XHUwMDNlN30gIHtcIm1heFwiOlx1MDAzZTd9ICB7XCJhdF94PS0zXCI6XHUwMDNlOX0gIHtcImF0X3g9MFwiOlx1MDAzZTd9ICB7XCJhdF94PTNcIjpcdTAwM2U3fVx1MDAyNylcbmZvciBuYW1lLCBmbiBpbiBmbnMuaXRlbXMoKTpcbiAgICB5ID0gZm4oeClcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNlMTJ9ICB7eS5taW4oKTpcdTAwM2U3LjNmfSAge3kubWF4KCk6XHUwMDNlNy4zZn0gIFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjd7Zm4obnAuYXJyYXkoWy0zLjBdKSlbMF06XHUwMDNlOS40Zn0gIFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjd7Zm4obnAuYXJyYXkoWzAuMF0pKVswXTpcdTAwM2U3LjRmfSAgXHUwMDI3XG4gICAgICAgICAgZlx1MDAyN3tmbihucC5hcnJheShbMy4wXSkpWzBdOlx1MDAzZTcuNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIENvbXBhcmlzb24gb24gTU5JU1QifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgZGF0YXNldHMsIHRyYW5zZm9ybXNcbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YUxvYWRlclxuXG5kZWYgbWFrZV9tb2RlbChhY3RfbmFtZSk6XG4gICAgYWN0cyA9IHtcbiAgICAgICAgXHUwMDI3cmVsdVx1MDAyNzogICAgICAgbm4uUmVMVSgpLFxuICAgICAgICBcdTAwMjdsZWFreV9yZWx1XHUwMDI3OiBubi5MZWFreVJlTFUoMC4wMSksXG4gICAgICAgIFx1MDAyN2VsdVx1MDAyNzogICAgICAgIG5uLkVMVSgpLFxuICAgICAgICBcdTAwMjdnZWx1XHUwMDI3OiAgICAgICBubi5HRUxVKCksXG4gICAgICAgIFx1MDAyN3NpbHVcdTAwMjc6ICAgICAgIG5uLlNpTFUoKSxcbiAgICAgICAgXHUwMDI3dGFuaFx1MDAyNzogICAgICAgbm4uVGFuaCgpLFxuICAgIH1cbiAgICBhY3QgPSBhY3RzW2FjdF9uYW1lXVxuICAgIHJldHVybiBubi5TZXF1ZW50aWFsKFxuICAgICAgICBubi5GbGF0dGVuKCksXG4gICAgICAgIG5uLkxpbmVhcig3ODQsIDI1NiksIGFjdCxcbiAgICAgICAgbm4uTGluZWFyKDI1NiwgMTI4KSwgYWN0LFxuICAgICAgICBubi5MaW5lYXIoMTI4LCAxMClcbiAgICApXG5cbnRyYW5zZm9ybSA9IHRyYW5zZm9ybXMuQ29tcG9zZShbdHJhbnNmb3Jtcy5Ub1RlbnNvcigpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJhbnNmb3Jtcy5Ob3JtYWxpemUoKDAuMTMwNywpLCAoMC4zMDgxLCkpXSlcbnRyYWluX2RzID0gZGF0YXNldHMuTU5JU1QoXHUwMDI3Llx1MDAyNywgdHJhaW49VHJ1ZSwgIGRvd25sb2FkPVRydWUsIHRyYW5zZm9ybT10cmFuc2Zvcm0pXG50ZXN0X2RzICA9IGRhdGFzZXRzLk1OSVNUKFx1MDAyNy5cdTAwMjcsIHRyYWluPUZhbHNlLCBkb3dubG9hZD1UcnVlLCB0cmFuc2Zvcm09dHJhbnNmb3JtKVxudHJhaW5fbGQgPSBEYXRhTG9hZGVyKHRyYWluX2RzLCBiYXRjaF9zaXplPTI1Niwgc2h1ZmZsZT1UcnVlKVxudGVzdF9sZCAgPSBEYXRhTG9hZGVyKHRlc3RfZHMsICBiYXRjaF9zaXplPTUxMilcblxucmVzdWx0cyA9IHt9XG5mb3IgYWN0X25hbWUgaW4gW1x1MDAyN3JlbHVcdTAwMjcsIFx1MDAyN2dlbHVcdTAwMjcsIFx1MDAyN3NpbHVcdTAwMjcsIFx1MDAyN2VsdVx1MDAyNywgXHUwMDI3dGFuaFx1MDAyN106XG4gICAgbW9kZWwgPSBtYWtlX21vZGVsKGFjdF9uYW1lKVxuICAgIG9wdCAgID0gb3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG4gICAgbG9zc19mbiA9IG5uLkNyb3NzRW50cm9weUxvc3MoKVxuICAgIGZvciBlcG9jaCBpbiByYW5nZSgzKTpcbiAgICAgICAgbW9kZWwudHJhaW4oKVxuICAgICAgICBmb3IgeGIsIHliIGluIHRyYWluX2xkOlxuICAgICAgICAgICAgbG9zcyA9IGxvc3NfZm4obW9kZWwoeGIpLCB5YilcbiAgICAgICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgbW9kZWwuZXZhbCgpXG4gICAgY29ycmVjdCA9IHN1bSgobW9kZWwoeGIpLmFyZ21heCgxKSA9PSB5Yikuc3VtKCkuaXRlbSgpIGZvciB4YiwgeWIgaW4gdGVzdF9sZClcbiAgICByZXN1bHRzW2FjdF9uYW1lXSA9IGNvcnJlY3QgLyBsZW4odGVzdF9kcykgKiAxMDBcbiAgICBwcmludChmXHUwMDI3e2FjdF9uYW1lOlx1MDAzZTEyfToge3Jlc3VsdHNbYWN0X25hbWVdOi4yZn0lIGFjY3VyYWN5ICgzIGVwb2NocylcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJXaHkgR0VMVSBCZWF0cyBSZUxVIGluIExhbmd1YWdlIE1vZGVscyIsImNvbnRlbnQiOiJHRUxVXHUwMDI3cyBzbW9vdGgsIHByb2JhYmlsaXN0aWMgZ2F0aW5nIGhlbHBzIGluIFRyYW5zZm9ybWVyIGFyY2hpdGVjdHVyZXMgYmVjYXVzZSBhdHRlbnRpb24gc2NvcmVzIGNhbiBiZSBuZWdhdGl2ZSBhbmQgc21hbGw7IFJlTFVcdTAwMjdzIGhhcmQgemVyby1nYXRlIGRlc3Ryb3lzIHRoaXMgaW5mb3JtYXRpb24uIEdFTFUgYWxsb3dzIGEgc29mdCwgc21vb3RoIHBhc3MtdGhyb3VnaCBuZWFyIHplcm8sIHdoaWNoIGVtcGlyaWNhbGx5IGltcHJvdmVzIGNvbnZlcmdlbmNlLiBCRVJUICgyMDE4KSByZXBsYWNlZCBSZUxVIHdpdGggR0VMVSBhbmQgaXQgaGFzIGJlZW4gdGhlIGRlZmF1bHQgZm9yIGxhcmdlIGxhbmd1YWdlIG1vZGVscyBldmVyIHNpbmNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IEZsb3cgaW4gRGVlcCBOZXR3b3JrcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBtZWFzdXJlX2dyYWRfZmxvdyhhY3RfbW9kdWxlLCBkZXB0aD0yMCwgd2lkdGg9MTI4LCBtPTY0LCBzZWVkPTApOlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgbGF5ZXJzID0gW11cbiAgICBmb3IgaSBpbiByYW5nZShkZXB0aCk6XG4gICAgICAgIGxheWVycy5hcHBlbmQobm4uTGluZWFyKHdpZHRoLCB3aWR0aCkpXG4gICAgICAgIGxheWVycy5hcHBlbmQoYWN0X21vZHVsZSgpIGlmIGNhbGxhYmxlKGFjdF9tb2R1bGUpIGVsc2UgdHlwZShhY3RfbW9kdWxlKSgpKVxuICAgIG1vZGVsID0gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuICAgICMgWGF2aWVyIGluaXQgZm9yIGZhaXIgY29tcGFyaXNvblxuICAgIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgaWYgcC5kaW0oKSBcdTAwM2U9IDI6XG4gICAgICAgICAgICBubi5pbml0Lnhhdmllcl91bmlmb3JtXyhwKVxuICAgIHggPSB0b3JjaC5yYW5kbihtLCB3aWR0aCwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxuICAgIG91dCA9IG1vZGVsKHgpXG4gICAgb3V0LnN1bSgpLmJhY2t3YXJkKClcbiAgICAjIENvbGxlY3QgZ3JhZGllbnQgbm9ybXMgcGVyIGxpbmVhciBsYXllclxuICAgIG5vcm1zID0gW11cbiAgICBmb3IgbW9kIGluIG1vZGVsLm1vZHVsZXMoKTpcbiAgICAgICAgaWYgaXNpbnN0YW5jZShtb2QsIG5uLkxpbmVhcikgYW5kIG1vZC53ZWlnaHQuZ3JhZCBpcyBub3QgTm9uZTpcbiAgICAgICAgICAgIG5vcm1zLmFwcGVuZChtb2Qud2VpZ2h0LmdyYWQubm9ybSgpLml0ZW0oKSlcbiAgICByZXR1cm4gbm9ybXNcblxuZm9yIGFjdF9uYW1lLCBhY3RfY2xzIGluIFsoXHUwMDI3UmVMVVx1MDAyNywgbm4uUmVMVSksIChcdTAwMjdHRUxVXHUwMDI3LCBubi5HRUxVKSwgKFx1MDAyN1RhbmhcdTAwMjcsIG5uLlRhbmgpXTpcbiAgICBub3JtcyA9IG1lYXN1cmVfZ3JhZF9mbG93KGFjdF9jbHMsIGRlcHRoPTEwKVxuICAgIHJhdGlvID0gbm9ybXNbMF0gLyAobm9ybXNbLTFdICsgMWUtMTApXG4gICAgcHJpbnQoZlx1MDAyN3thY3RfbmFtZTpcdTAwM2U2fTogZmlyc3QtbGF5ZXItZ3JhZD17bm9ybXNbMF06LjRmfSAgbGFzdC1sYXllci1ncmFkPXtub3Jtc1stMV06LjRmfSAgXHUwMDI3XG4gICAgICAgICAgZlx1MDAyN3JhdGlvPXtyYXRpbzouMWZ9ICB2YW5pc2hpbmc9e3JhdGlvIFx1MDAzZSAxMDB9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFjdGl2YXRpb24gRnVuY3Rpb24gUmVmZXJlbmNlIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRpbWVcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgYmVuY2htYXJrX2FjdGl2YXRpb24oZm4sIHgsIG49MTAwMCk6XG4gICAgIyBXYXJtdXBcbiAgICBmb3IgXyBpbiByYW5nZSgxMCk6IGZuKHgpXG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgZm9yIF8gaW4gcmFuZ2Uobik6IGZuKHgpXG4gICAgcmV0dXJuICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApIC8gbiAqIDFlNiAgIyBtaWNyb3NlY29uZHNcblxueCA9IHRvcmNoLnJhbmRuKDUxMiwgMTAyNClcbmFjdHMgPSB7XG4gICAgXHUwMDI3UmVMVVx1MDAyNzogICAgICAgdG9yY2gubm4uZnVuY3Rpb25hbC5yZWx1LFxuICAgIFx1MDAyN0xlYWt5UmVMVVx1MDAyNzogIGxhbWJkYSB6OiB0b3JjaC5ubi5mdW5jdGlvbmFsLmxlYWt5X3JlbHUoeiwgMC4wMSksXG4gICAgXHUwMDI3RUxVXHUwMDI3OiAgICAgICAgdG9yY2gubm4uZnVuY3Rpb25hbC5lbHUsXG4gICAgXHUwMDI3R0VMVVx1MDAyNzogICAgICAgdG9yY2gubm4uZnVuY3Rpb25hbC5nZWx1LFxuICAgIFx1MDAyN1NpTFVcdTAwMjc6ICAgICAgIHRvcmNoLm5uLmZ1bmN0aW9uYWwuc2lsdSxcbiAgICBcdTAwMjdUYW5oXHUwMDI3OiAgICAgICB0b3JjaC50YW5oLFxuICAgIFx1MDAyN1NpZ21vaWRcdTAwMjc6ICAgIHRvcmNoLnNpZ21vaWQsXG59XG5wcmludChmXHUwMDI3e1wiQWN0aXZhdGlvblwiOlx1MDAzZTEyfSAge1widXMvY2FsbFwiOlx1MDAzZTEwfSAge1wicmVsYXRpdmVcIjpcdTAwM2UxMH1cdTAwMjcpXG5iYXNlbGluZSA9IE5vbmVcbmZvciBuYW1lLCBmbiBpbiBhY3RzLml0ZW1zKCk6XG4gICAgdCA9IGJlbmNobWFya19hY3RpdmF0aW9uKGZuLCB4KVxuICAgIGlmIGJhc2VsaW5lIGlzIE5vbmU6IGJhc2VsaW5lID0gdFxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2UxMn0gIHt0Olx1MDAzZTEwLjJmfSAge3QvYmFzZWxpbmU6XHUwMDNlMTAuMmZ9eFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBY3RpdmF0aW9uIENvbXBhcmlzb24gVGFibGUifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQWN0aXZhdGlvbiIsIlNhdHVyYXRlcyIsIlplcm8tQ2VudGVyZWQiLCJEaWZmZXJlbnRpYWJsZSBhdCAwIiwiVHlwaWNhbCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJTaWdtb2lkIiwiWWVzIOKAlCBib3RoIHRhaWxzIiwiTm8gKG91dHB1dHMgMCB0byAxKSIsIlllcyIsIk91dHB1dCBsYXllciBiaW5hcnkgY2xhc3NpZmljYXRpb24iXSxbIlRhbmgiLCJZZXMg4oCUIGJvdGggdGFpbHMiLCJZZXMgKG91dHB1dHMgLTEgdG8gMSkiLCJZZXMiLCJSTk5zL0xTVE1zLCB6ZXJvLWNlbnRlcmVkIGFsdGVybmF0aXZlIHRvIHNpZ21vaWQiXSxbIlJlTFUiLCJObyAocG9zaXRpdmUgc2lkZSkiLCJObyAob3V0cHV0cyDiiaUgMCkiLCJObyAoc3ViZ3JhZGllbnQ9MCkiLCJEZWZhdWx0IGZvciBDTk5zOyBmYXN0IGFuZCBzcGFyc2UiXSxbIkxlYWt5IFJlTFUiLCJObyIsIk5vIiwiTm8gKHN1YmdyYWRpZW50Pc6xKSIsIlJlcGxhY2UgUmVMVSB3aGVuIGRlYWQgbmV1cm9ucyBhcmUgYSBjb25jZXJuIl0sWyJFTFUiLCJTb2Z0IG5lZ2F0aXZlIHNhdHVyYXRpb24iLCJBcHByb3hpbWF0ZWx5IHllcyIsIlllcyIsIkRlZXAgbmV0d29ya3MgbmVlZGluZyBzbW9vdGggbmVnYXRpdmUgc2lkZSJdLFsiR0VMVSIsIk5vIiwiQXBwcm94aW1hdGVseSB5ZXMiLCJZZXMiLCJUcmFuc2Zvcm1lcnMsIEJFUlQsIEdQVCDigJQgZGVmYXVsdCBmb3IgTExNcyJdLFsiU2lMVS9Td2lzaCIsIk5vIiwiQXBwcm94aW1hdGVseSB5ZXMiLCJZZXMiLCJFZmZpY2llbnROZXQsIExMYU1BLCBNb2JpbGVOZXRWMyJdLFsiTWlzaCIsIk5vIiwiQXBwcm94aW1hdGVseSB5ZXMiLCJZZXMiLCJBbHRlcm5hdGl2ZSB0byBTd2lzaDsgc2xpZ2h0bHkgc21vb3RoZXIiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNob29zaW5nIHRoZSBSaWdodCBBY3RpdmF0aW9uIGluIFByYWN0aWNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgY29udm9sdXRpb25hbCBuZXVyYWwgbmV0d29ya3MgcHJvY2Vzc2luZyBpbWFnZXMsIFJlTFUgcmVtYWlucyB0aGUgZGVmYXVsdDogaXQgaXMgZmFzdCwgcHJvZHVjZXMgc3BhcnNlIGFjdGl2YXRpb25zIHRoYXQgYXJlIGJlbmVmaWNpYWwgZm9yIGZlYXR1cmUgZGV0ZWN0aW9uLCBhbmQgd29ya3Mgd2VsbCB3aXRoIEhlIGluaXRpYWxpc2F0aW9uLiBGb3IgVHJhbnNmb3JtZXIgYXJjaGl0ZWN0dXJlcyBhbmQgbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzLCBHRUxVIGlzIHRoZSBzdGFuZGFyZCBjaG9pY2Ug4oCUIGl0IHdhcyBhZG9wdGVkIGJ5IEJFUlQgaW4gMjAxOCBhbmQgaGFzIHJlbWFpbmVkIGRvbWluYW50LiBTaUxVIChTd2lzaCkgaXMgcHJlZmVycmVkIGluIEVmZmljaWVudE5ldCwgTExhTUEsIGFuZCBvdGhlciBlZmZpY2llbmN5LWZvY3VzZWQgYXJjaGl0ZWN0dXJlczsgaXRzIHNtb290aCBub24tbW9ub3RvbmUgc2hhcGUgaGVscHMgZ3JhZGllbnQgZmxvdyBpbiB2ZXJ5IGRlZXAgc3RhY2tzLiBUYW5oIGlzIHN0aWxsIHVzZWQgaW4gTFNUTSBnYXRlcywgd2hlcmUgYm91bmRlZCBvdXRwdXQgaXMgcmVxdWlyZWQuIFNpZ21vaWQgc3Vydml2ZXMgb25seSBpbiBvdXRwdXQgbGF5ZXJzIGZvciBiaW5hcnkgY2xhc3NpZmljYXRpb24gYW5kIGluIGdhdGluZyBtZWNoYW5pc21zLiBNaXNoIGFuZCBvdGhlciBuZXdlciBhY3RpdmF0aW9ucyBvZmZlciBtYXJnaW5hbCBnYWlucyBhdCBoaWdoZXIgY29tcHV0ZSBjb3N0IGFuZCBhcmUgcmFyZWx5IHdvcnRoIHRoZSBjb21wbGV4aXR5IGluIHByb2R1Y3Rpb24uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlF1aWNrIERlZmF1bHQgUnVsZXMiLCJjb250ZW50IjoiQ05OIGhpZGRlbiBsYXllcnM6IFJlTFUgKyBIZSBpbml0LiBUcmFuc2Zvcm1lciBGRk4gbGF5ZXJzOiBHRUxVIG9yIFNpTFUuIFJOTi9MU1RNIGdhdGVzOiB0YW5oIChoaWRkZW4gc3RhdGUpICsgc2lnbW9pZCAoZ2F0ZXMpLiBPdXRwdXQgbGF5ZXIg4oCUIGJpbmFyeSBjbGFzc2lmaWNhdGlvbjogc2lnbW9pZC4gT3V0cHV0IGxheWVyIOKAlCBtdWx0aS1jbGFzczogbm8gYWN0aXZhdGlvbiAocmF3IGxvZ2l0cyBpbnRvIENyb3NzRW50cm9weUxvc3MpLiBJZiBSZUxVIHByb2R1Y2VzIGRlYWQgbmV1cm9ucywgc3dpdGNoIHRvIExlYWt5IFJlTFUgYmVmb3JlIHRyeWluZyBhbnl0aGluZyBtb3JlIGV4b3RpYy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlJlTFU6IGRlZmF1bHQgZm9yIENOTnM7IGZhc3QsIHNwYXJzZSwgd29ya3Mgd2l0aCBIZSBpbml0OyByaXNrcyBkZWFkIG5ldXJvbnMgYXQgaGlnaCBMUi4iLCJHRUxVOiBzdGFuZGFyZCBpbiBUcmFuc2Zvcm1lcnMgKEJFUlQsIEdQVCwgVmlUKTsgc21vb3RoLCBub24tbW9ub3RvbmU7IHNsaWdodGx5IHNsb3dlciB0aGFuIFJlTFUuIiwiU2lMVS9Td2lzaDogdXNlZCBpbiBMTGFNQSwgRWZmaWNpZW50TmV0OyBwcmFjdGljYWxseSBpbnRlcmNoYW5nZWFibGUgd2l0aCBHRUxVIG9uIG1vc3QgdGFza3MuIiwiTGVha3kgUmVMVTogZHJvcC1pbiBSZUxVIHJlcGxhY2VtZW50IHdoZW4gZGVhZCBuZXVyb25zIGFyZSBvYnNlcnZlZDsgdmlydHVhbGx5IG5vIGV4dHJhIGNvc3QuIiwiVGFuaDogTFNUTS9HUlUgZ2F0ZXMsIG91dHB1dCBib3VuZGVkIHRvICgtMSwxKTsgc2F0dXJhdGVzIGluIGRlZXAgZmVlZGZvcndhcmQgbmV0d29ya3MuIiwiU2lnbW9pZDogYmluYXJ5IG91dHB1dCBoZWFkcyBvbmx5OyBub24temVyby1jZW50ZXJlZCBhbmQgc2F0dXJhdGluZyDigJQgYXZvaWQgaW4gaGlkZGVuIGxheWVycy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Activation Functions — ReLU, GELU, SiLU, and Friends

Activation functions are the non-linearities that give neural networks their expressive power. The choice of activation affects gradient flow, training speed, and model quality. Early networks used sigmoid and tanh; modern CNNs default to ReLU; Transformers and large language models rely on GELU and SiLU. Understanding each function's properties — saturation, zero-centering, differentiability, and stochastic interpretation — guides which to reach for in a new architecture.

## Classical Activations: Sigmoid and Tanh

Sigmoid σ(x) = 1/(1+e⁻ˣ) maps to (0,1) — useful for probabilities but saturates for |x| > 4: gradient σ'(x) = σ(x)(1-σ(x)) is at most 0.25 and collapses to near zero far from the origin. Non-zero-centered: outputs always positive, so gradients on W are all-positive or all-negative — zig-zag gradient updates. Tanh(x) = (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) maps to (-1,1), zero-centered, derivative 1-tanh²(x) peaks at 1.0 — better gradient than sigmoid but still saturates. Both are largely replaced by ReLU variants in hidden layers; sigmoid survives in output layers for binary classification.

## ReLU and its Variants

ReLU: a = max(0, x). Non-saturating for x > 0, sparse (≈50% zero activations), computationally trivial. Problems: (1) dead neurons — if z < 0 for all inputs, gradient is zero and weights never update; (2) not zero-centered; (3) not differentiable at 0 (subgradient 0 is used). Leaky ReLU: max(αx, x) with α=0.01 — non-zero gradient everywhere. PReLU: same but α is a learned parameter per channel. ELU: x for x>0, α(eˣ-1) for x≤0 — smooth negative side, zero-mean outputs, but slower due to exp. SELU is a scaled ELU designed for self-normalising networks.

## Modern Activations: GELU, SiLU, and Mish

GELU (Gaussian Error Linear Unit): x · Φ(x) where Φ is the CDF of N(0,1). Stochastic interpretation: stochastically zero-gates x with probability Φ(x). Smooth everywhere, non-monotone (small negative dip around x=-0.1). Used in BERT, GPT-2/3, ViT. Approximated as 0.5x(1+tanh(√(2/π)(x+0.044715x³))). SiLU/Swish: x·σ(x) — similar shape to GELU, used in EfficientNet, MobileNetV3, LLaMA. Mish: x·tanh(softplus(x)) — smooth, non-monotone, slight performance gains reported over Swish. All three outperform ReLU on language models because their smooth, non-zero negative side helps gradient flow.

```python
import numpy as np
import torch
import torch.nn.functional as F

# Implement all activations from scratch
def sigmoid(x):  return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
def tanh_fn(x):  return np.tanh(x)
def relu(x):     return np.maximum(0, x)
def leaky_relu(x, alpha=0.01): return np.where(x > 0, x, alpha * x)
def elu(x, alpha=1.0): return np.where(x > 0, x, alpha * (np.exp(np.clip(x,-50,0)) - 1))

def gelu(x):
    # Exact GELU via standard normal CDF
    return x * 0.5 * (1 + np.vectorize(lambda v: float(torch.erf(torch.tensor(v / np.sqrt(2)))))(x))

def silu(x):  return x * sigmoid(x)  # Swish
def mish(x):  return x * np.tanh(np.log1p(np.exp(np.clip(x, -50, 50))))

x = np.linspace(-4, 4, 200)
fns = {
    'sigmoid': sigmoid, 'tanh': tanh_fn, 'relu': relu,
    'leaky_relu': leaky_relu, 'elu': elu, 'gelu': gelu,
    'silu': silu, 'mish': mish
}
print(f'{"Activation":>12}  {"min":>7}  {"max":>7}  {"at_x=-3":>9}  {"at_x=0":>7}  {"at_x=3":>7}')
for name, fn in fns.items():
    y = fn(x)
    print(f'{name:>12}  {y.min():>7.3f}  {y.max():>7.3f}  '
          f'{fn(np.array([-3.0]))[0]:>9.4f}  '
          f'{fn(np.array([0.0]))[0]:>7.4f}  '
          f'{fn(np.array([3.0]))[0]:>7.4f}')
```

## Training Comparison on MNIST

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def make_model(act_name):
    acts = {
        'relu':       nn.ReLU(),
        'leaky_relu': nn.LeakyReLU(0.01),
        'elu':        nn.ELU(),
        'gelu':       nn.GELU(),
        'silu':       nn.SiLU(),
        'tanh':       nn.Tanh(),
    }
    act = acts[act_name]
    return nn.Sequential(
        nn.Flatten(),
        nn.Linear(784, 256), act,
        nn.Linear(256, 128), act,
        nn.Linear(128, 10)
    )

transform = transforms.Compose([transforms.ToTensor(),
                                 transforms.Normalize((0.1307,), (0.3081,))])
train_ds = datasets.MNIST('.', train=True,  download=True, transform=transform)
test_ds  = datasets.MNIST('.', train=False, download=True, transform=transform)
train_ld = DataLoader(train_ds, batch_size=256, shuffle=True)
test_ld  = DataLoader(test_ds,  batch_size=512)

results = {}
for act_name in ['relu', 'gelu', 'silu', 'elu', 'tanh']:
    model = make_model(act_name)
    opt   = optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    for epoch in range(3):
        model.train()
        for xb, yb in train_ld:
            loss = loss_fn(model(xb), yb)
            opt.zero_grad(); loss.backward(); opt.step()
    model.eval()
    correct = sum((model(xb).argmax(1) == yb).sum().item() for xb, yb in test_ld)
    results[act_name] = correct / len(test_ds) * 100
    print(f'{act_name:>12}: {results[act_name]:.2f}% accuracy (3 epochs)')
```

> **Why GELU Beats ReLU in Language Models**: GELU's smooth, probabilistic gating helps in Transformer architectures because attention scores can be negative and small; ReLU's hard zero-gate destroys this information. GELU allows a soft, smooth pass-through near zero, which empirically improves convergence. BERT (2018) replaced ReLU with GELU and it has been the default for large language models ever since.

## Gradient Flow in Deep Networks

```python
import torch
import torch.nn as nn
import numpy as np

def measure_grad_flow(act_module, depth=20, width=128, m=64, seed=0):
    torch.manual_seed(seed)
    layers = []
    for i in range(depth):
        layers.append(nn.Linear(width, width))
        layers.append(act_module() if callable(act_module) else type(act_module)())
    model = nn.Sequential(*layers)
    # Xavier init for fair comparison
    for p in model.parameters():
        if p.dim() >= 2:
            nn.init.xavier_uniform_(p)
    x = torch.randn(m, width, requires_grad=True)
    out = model(x)
    out.sum().backward()
    # Collect gradient norms per linear layer
    norms = []
    for mod in model.modules():
        if isinstance(mod, nn.Linear) and mod.weight.grad is not None:
            norms.append(mod.weight.grad.norm().item())
    return norms

for act_name, act_cls in [('ReLU', nn.ReLU), ('GELU', nn.GELU), ('Tanh', nn.Tanh)]:
    norms = measure_grad_flow(act_cls, depth=10)
    ratio = norms[0] / (norms[-1] + 1e-10)
    print(f'{act_name:>6}: first-layer-grad={norms[0]:.4f}  last-layer-grad={norms[-1]:.4f}  '
          f'ratio={ratio:.1f}  vanishing={ratio > 100}')
```

## Activation Function Reference

```python
import torch
import time
import numpy as np

def benchmark_activation(fn, x, n=1000):
    # Warmup
    for _ in range(10): fn(x)
    t0 = time.perf_counter()
    for _ in range(n): fn(x)
    return (time.perf_counter() - t0) / n * 1e6  # microseconds

x = torch.randn(512, 1024)
acts = {
    'ReLU':       torch.nn.functional.relu,
    'LeakyReLU':  lambda z: torch.nn.functional.leaky_relu(z, 0.01),
    'ELU':        torch.nn.functional.elu,
    'GELU':       torch.nn.functional.gelu,
    'SiLU':       torch.nn.functional.silu,
    'Tanh':       torch.tanh,
    'Sigmoid':    torch.sigmoid,
}
print(f'{"Activation":>12}  {"us/call":>10}  {"relative":>10}')
baseline = None
for name, fn in acts.items():
    t = benchmark_activation(fn, x)
    if baseline is None: baseline = t
    print(f'{name:>12}  {t:>10.2f}  {t/baseline:>10.2f}x')
```

## Activation Comparison Table

| Activation | Saturates | Zero-Centered | Differentiable at 0 | Typical Use Case |
| --- | --- | --- | --- | --- |
| Sigmoid | Yes — both tails | No (outputs 0 to 1) | Yes | Output layer binary classification |
| Tanh | Yes — both tails | Yes (outputs -1 to 1) | Yes | RNNs/LSTMs, zero-centered alternative to sigmoid |
| ReLU | No (positive side) | No (outputs ≥ 0) | No (subgradient=0) | Default for CNNs; fast and sparse |
| Leaky ReLU | No | No | No (subgradient=α) | Replace ReLU when dead neurons are a concern |
| ELU | Soft negative saturation | Approximately yes | Yes | Deep networks needing smooth negative side |
| GELU | No | Approximately yes | Yes | Transformers, BERT, GPT — default for LLMs |
| SiLU/Swish | No | Approximately yes | Yes | EfficientNet, LLaMA, MobileNetV3 |
| Mish | No | Approximately yes | Yes | Alternative to Swish; slightly smoother |

## Choosing the Right Activation in Practice

For convolutional neural networks processing images, ReLU remains the default: it is fast, produces sparse activations that are beneficial for feature detection, and works well with He initialisation. For Transformer architectures and large language models, GELU is the standard choice — it was adopted by BERT in 2018 and has remained dominant. SiLU (Swish) is preferred in EfficientNet, LLaMA, and other efficiency-focused architectures; its smooth non-monotone shape helps gradient flow in very deep stacks. Tanh is still used in LSTM gates, where bounded output is required. Sigmoid survives only in output layers for binary classification and in gating mechanisms. Mish and other newer activations offer marginal gains at higher compute cost and are rarely worth the complexity in production.

> **Quick Default Rules**: CNN hidden layers: ReLU + He init. Transformer FFN layers: GELU or SiLU. RNN/LSTM gates: tanh (hidden state) + sigmoid (gates). Output layer — binary classification: sigmoid. Output layer — multi-class: no activation (raw logits into CrossEntropyLoss). If ReLU produces dead neurons, switch to Leaky ReLU before trying anything more exotic.

- ReLU: default for CNNs; fast, sparse, works with He init; risks dead neurons at high LR.
- GELU: standard in Transformers (BERT, GPT, ViT); smooth, non-monotone; slightly slower than ReLU.
- SiLU/Swish: used in LLaMA, EfficientNet; practically interchangeable with GELU on most tasks.
- Leaky ReLU: drop-in ReLU replacement when dead neurons are observed; virtually no extra cost.
- Tanh: LSTM/GRU gates, output bounded to (-1,1); saturates in deep feedforward networks.
- Sigmoid: binary output heads only; non-zero-centered and saturating — avoid in hidden layers.

---

