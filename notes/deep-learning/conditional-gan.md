---
title: "Conditional GAN (cGAN) — Class-Conditional and Projection Discriminator"
slug: "conditional-gan"
description: "Condition both generator G(z,y) and discriminator D(x,y) on class label y; derive the projection discriminator D(x,y)=phi(x)^T V_y + psi(phi(x)); implement class-conditional BatchNorm as used in BigGAN; and apply the truncation trick to trade sample quality for diversity."
tags: ["deep-learning", "generative-models", "gans", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBjb25kaXRpb25hbCBHQU4gKGNHQU4pIGV4dGVuZHMgdGhlIHZhbmlsbGEgR0FOIGJ5IHN1cHBseWluZyBib3RoIHRoZSBnZW5lcmF0b3IgRyBhbmQgZGlzY3JpbWluYXRvciBEIHdpdGggYSBjb25kaXRpb25pbmcgc2lnbmFsIHkg4oCUIHR5cGljYWxseSBhIGNsYXNzIGxhYmVsLiBUaGUgZ2VuZXJhdG9yIGxlYXJucyBHOiAoeix5KSDihpIgeCwgcHJvZHVjaW5nIGltYWdlcyBiZWxvbmdpbmcgdG8gY2xhc3MgeS4gVGhlIGRpc2NyaW1pbmF0b3IgbGVhcm5zIHRvIGRpc3Rpbmd1aXNoIHJlYWwgKHgseSkgcGFpcnMgZnJvbSBmYWtlIG9uZXMuIENvbmRpdGlvbmluZyBlbmFibGVzIGNsYXNzLXNwZWNpZmljIGdlbmVyYXRpb24sIHJlZHVjZXMgd2l0aGluLWNsYXNzIHNhbXBsZSBkaXZlcnNpdHksIGFuZCBhbGxvd3MgY29udHJvbGxhYmxlIHN5bnRoZXNpcyDigJQgdGhlIGZvdW5kYXRpb24gZm9yIGxhcmdlLXNjYWxlIG1vZGVscyBzdWNoIGFzIEJpZ0dBTiBhbmQgbW9kZXJuIHRleHQtY29uZGl0aW9uYWwgZGlmZnVzaW9uIG1vZGVscy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25kaXRpb25pbmcgR2VuZXJhdG9yIGFuZCBEaXNjcmltaW5hdG9yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2ltcGxlc3Qgc3RyYXRlZ3kgZW1iZWRzIHkgaW50byBhIGRlbnNlIHZlY3RvciB2aWEgYSBsZWFybmVkIG5uLkVtYmVkZGluZywgdGhlbiBjb25jYXRlbmF0ZXMgaXQgdG8gdGhlIG5vaXNlIHZlY3RvciB6IGJlZm9yZSBmZWVkaW5nIEcuIEZvciBELCB0aGUgbGFiZWwgZW1iZWRkaW5nIGlzIGNvbmNhdGVuYXRlZCB0byB0aGUgZmxhdHRlbmVkIGltYWdlLiBFbWJlZGRpbmcgZGltZW5zaW9uICg1MOKAkzI1NikgaXMgYSBoeXBlcnBhcmFtZXRlci4gVGhlIG9iamVjdGl2ZSByZW1haW5zIHRoZSBzdGFuZGFyZCBHQU4gbG9zcyDigJQgQkNFIG9yIGhpbmdlIOKAlCB3aXRoIHRoZSBwYWlyICh4LHkpIGFzIGlucHV0IHJhdGhlciB0aGFuIHggYWxvbmUuIFRoaXMgYXBwcm9hY2ggaXMgY2FsbGVkIGxhYmVsIGNvbmNhdGVuYXRpb24gY29uZGl0aW9uaW5nIGFuZCBzZXJ2ZXMgYXMgdGhlIGJhc2VsaW5lIGFnYWluc3Qgd2hpY2ggcHJvamVjdGlvbiBkaXNjcmltaW5hdG9ycyBhcmUgY29tcGFyZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIENvbmRpdGlvbmFsR2VuZXJhdG9yKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHpfZGltPTEwMCwgbl9jbGFzc2VzPTEwLCBpbWdfZGltPTc4NCwgZW1iZWRfZGltPTUwKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubGFiZWxfZW1iZWQgPSBubi5FbWJlZGRpbmcobl9jbGFzc2VzLCBlbWJlZF9kaW0pXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcih6X2RpbSArIGVtYmVkX2RpbSwgMjU2KSwgbm4uTGVha3lSZUxVKDAuMiksXG4gICAgICAgICAgICBubi5MaW5lYXIoMjU2LCA1MTIpLCBubi5MZWFreVJlTFUoMC4yKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcig1MTIsIGltZ19kaW0pLCBubi5UYW5oKCkpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeiwgbGFiZWxzKTpcbiAgICAgICAgcmV0dXJuIHNlbGYubmV0KHRvcmNoLmNhdChbeiwgc2VsZi5sYWJlbF9lbWJlZChsYWJlbHMpXSwgMSkpXG5cbmNsYXNzIENvbmRpdGlvbmFsRGlzY3JpbWluYXRvcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2NsYXNzZXM9MTAsIGltZ19kaW09Nzg0LCBlbWJlZF9kaW09NTApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5sYWJlbF9lbWJlZCA9IG5uLkVtYmVkZGluZyhuX2NsYXNzZXMsIGVtYmVkX2RpbSlcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGltZ19kaW0gKyBlbWJlZF9kaW0sIDUxMiksIG5uLkxlYWt5UmVMVSgwLjIpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDUxMiwgMjU2KSwgbm4uTGVha3lSZUxVKDAuMiksXG4gICAgICAgICAgICBubi5MaW5lYXIoMjU2LCAxKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBsYWJlbHMpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQodG9yY2guY2F0KFt4LCBzZWxmLmxhYmVsX2VtYmVkKGxhYmVscyldLCAxKSlcblxudG9yY2gubWFudWFsX3NlZWQoMClcbkcsIEQgPSBDb25kaXRpb25hbEdlbmVyYXRvcigpLCBDb25kaXRpb25hbERpc2NyaW1pbmF0b3IoKVxueiA9IHRvcmNoLnJhbmRuKDgsIDEwMClcbmxhYmVscyA9IHRvcmNoLnJhbmRpbnQoMCwgMTAsICg4LCkpXG5mYWtlID0gRyh6LCBsYWJlbHMpXG5zY29yZSA9IEQoZmFrZS5kZXRhY2goKSwgbGFiZWxzKVxucHJpbnQoXHUwMDI3RmFrZSBzaGFwZTpcdTAwMjcsIGZha2Uuc2hhcGUsIFx1MDAyN3wgU2NvcmUgc2hhcGU6XHUwMDI3LCBzY29yZS5zaGFwZSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcm9qZWN0aW9uIERpc2NyaW1pbmF0b3IgKE1peWF0byAyMDE4KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uY2F0ZW5hdGluZyB0aGUgbGFiZWwgZW1iZWRkaW5nIHRvIERcdTAwMjdzIGlucHV0IHRyZWF0cyB4IGFuZCB5IHN5bW1ldHJpY2FsbHksIGlnbm9yaW5nIHRoZWlyIGRpZmZlcmVudCBzdGF0aXN0aWNhbCByb2xlcy4gVGhlIHByb2plY3Rpb24gZGlzY3JpbWluYXRvciAoTWl5YXRvIFx1MDAyNiBLb3lhbWEgMjAxOCkgY29tcHV0ZXMgRCh4LHkpID0gz4YoeCnhtYBWX3kgKyDPiCjPhih4KSksIHdoZXJlIM+GIGlzIGEgZGVlcCBmZWF0dXJlIGV4dHJhY3RvciwgViBpcyB0aGUgbGFiZWwgZW1iZWRkaW5nIG1hdHJpeCwgYW5kIM+IIGlzIGFuIHVuY29uZGl0aW9uYWwgbGluZWFyIGhlYWQuIFRoZSBpbm5lciBwcm9kdWN0IM+GKHgp4bWAVl95IGRpcmVjdGx5IHNjb3JlcyBob3cgd2VsbCBpbWFnZSBmZWF0dXJlcyBhbGlnbiB3aXRoIHRoZSBjbGFzcyBlbWJlZGRpbmcg4oCUIGEgcHJpbmNpcGxlZCBmYWN0b3Jpc2F0aW9uIGdyb3VuZGVkIGluIHRoZSB0aGVvcnkgb2YgZW5lcmd5LWJhc2VkIG1vZGVscyB0aGF0IGVtcGlyaWNhbGx5IGFjaGlldmVzIGxvd2VyIEZJRCB0aGFuIGNvbmNhdGVuYXRpb24gY29uZGl0aW9uaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBQcm9qZWN0aW9uRGlzY3JpbWluYXRvcihubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN01peWF0byBcdTAwMjYgS295YW1hIDIwMTg6IEQoeCx5KSA9IHBoaSh4KV5UIFZfeSArIHBzaShwaGkoeCkpLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBmZWF0dXJlX2RpbT0yNTYsIG5fY2xhc3Nlcz0xMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBoaSA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoNzg0LCA1MTIpLCBubi5MZWFreVJlTFUoMC4yKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcig1MTIsIGZlYXR1cmVfZGltKSwgbm4uTGVha3lSZUxVKDAuMikpXG4gICAgICAgIHNlbGYuViAgID0gbm4uRW1iZWRkaW5nKG5fY2xhc3NlcywgZmVhdHVyZV9kaW0pICAjIGxhYmVsIG1hdHJpeFxuICAgICAgICBzZWxmLnBzaSA9IG5uLkxpbmVhcihmZWF0dXJlX2RpbSwgMSkgICAgICAgICAgICAgIyB1bmNvbmRpdGlvbmFsIGhlYWRcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIGxhYmVscyk6XG4gICAgICAgIGggICA9IHNlbGYucGhpKHgpICAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIGZlYXR1cmVfZGltKVxuICAgICAgICB2X3kgPSBzZWxmLlYobGFiZWxzKSAgICAgICAgICAgICAgICAgICAgICAjIChCLCBmZWF0dXJlX2RpbSlcbiAgICAgICAgcHJvaiAgID0gKGggKiB2X3kpLnN1bSgxLCBrZWVwZGltPVRydWUpICAjIGlubmVyIHByb2R1Y3QgKEIsIDEpXG4gICAgICAgIHVuY29uZCA9IHNlbGYucHNpKGgpICAgICAgICAgICAgICAgICAgICAgICMgYmlhcyB0ZXJtICAgIChCLCAxKVxuICAgICAgICByZXR1cm4gcHJvaiArIHVuY29uZFxuXG50b3JjaC5tYW51YWxfc2VlZCgxKVxuRF9wcm9qID0gUHJvamVjdGlvbkRpc2NyaW1pbmF0b3IoKVxueCA9IHRvcmNoLnJhbmRuKDgsIDc4NClcbmxhYmVscyA9IHRvcmNoLnJhbmRpbnQoMCwgMTAsICg4LCkpXG5vdXQgPSBEX3Byb2ooeCwgbGFiZWxzKVxucHJpbnQoXHUwMDI3UHJvamVjdGlvbiBEIG91dHB1dCBzaGFwZTpcdTAwMjcsIG91dC5zaGFwZSkgICMgKDgsIDEpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2xhc3MtQ29uZGl0aW9uYWwgQmF0Y2ggTm9ybWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2xhc3MtY29uZGl0aW9uYWwgQmF0Y2hOb3JtIChjQk4pIHVzZXMgYSBzZXBhcmF0ZSAozrNfeSwgzrJfeSkgcGFpciBmb3IgZWFjaCBjbGFzcyB5IGluc3RlYWQgb2YgZ2xvYmFsIM6zIGFuZCDOsi4gRmVhdHVyZXMgYXJlIG5vcm1hbGlzZWQgYWNyb3NzIHRoZSBiYXRjaCBhcyB1c3VhbCwgYnV0IHRoZSBhZmZpbmUgdHJhbnNmb3JtIGlzIGNsYXNzLXNwZWNpZmljOiBoID0gzrNfeSDCtyBCTihoKSArIM6yX3kuIEJpZ0dBTiBhcHBsaWVzIGNCTiB0aHJvdWdob3V0IHRoZSBnZW5lcmF0b3IsIGFsbG93aW5nIHRoZSBuZXR3b3JrIHRvIG1vZHVsYXRlIGFjdGl2YXRpb25zIGF0IGV2ZXJ5IGxheWVyIGJhc2VkIG9uIGNsYXNzIGlkZW50aXR5LiBJbiBCaWdHQU4sIM6zX3kgYW5kIM6yX3kgYXJlIGxpbmVhciBwcm9qZWN0aW9ucyBvZiBhIHNoYXJlZCBjbGFzcyBlbWJlZGRpbmcgcmF0aGVyIHRoYW4gZGlyZWN0IGxvb2t1cHMsIG1ha2luZyB0aGUgY29uZGl0aW9uaW5nIHBhcmFtZXRyaWNhbGx5IGVmZmljaWVudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgQ29uZGl0aW9uYWxCYXRjaE5vcm0obm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdTZXBhcmF0ZSBnYW1tYS9iZXRhIHBlciBjbGFzcywgYXMgdXNlZCBpbiBCaWdHQU4gZ2VuZXJhdG9yLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBudW1fZmVhdHVyZXMsIG5fY2xhc3Nlcz0xMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmJuICAgID0gbm4uQmF0Y2hOb3JtMWQobnVtX2ZlYXR1cmVzLCBhZmZpbmU9RmFsc2UpXG4gICAgICAgIHNlbGYuZ2FtbWEgPSBubi5FbWJlZGRpbmcobl9jbGFzc2VzLCBudW1fZmVhdHVyZXMpXG4gICAgICAgIHNlbGYuYmV0YSAgPSBubi5FbWJlZGRpbmcobl9jbGFzc2VzLCBudW1fZmVhdHVyZXMpXG4gICAgICAgIG5uLmluaXQub25lc18oc2VsZi5nYW1tYS53ZWlnaHQpXG4gICAgICAgIG5uLmluaXQuemVyb3NfKHNlbGYuYmV0YS53ZWlnaHQpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBsYWJlbHMpOlxuICAgICAgICBvdXQgPSBzZWxmLmJuKHgpXG4gICAgICAgIGcgICA9IHNlbGYuZ2FtbWEobGFiZWxzKSAgIyAoQiwgbnVtX2ZlYXR1cmVzKVxuICAgICAgICBiICAgPSBzZWxmLmJldGEobGFiZWxzKSAgICMgKEIsIG51bV9mZWF0dXJlcylcbiAgICAgICAgcmV0dXJuIGcgKiBvdXQgKyBiXG5cbmNibiA9IENvbmRpdGlvbmFsQmF0Y2hOb3JtKDY0LCAxMClcbnggICA9IHRvcmNoLnJhbmRuKDE2LCA2NClcbnkwICA9IGNibih4LCB0b3JjaC56ZXJvcygxNiwgZHR5cGU9dG9yY2gubG9uZykpICAjIGNsYXNzIDBcbnkxICA9IGNibih4LCB0b3JjaC5vbmVzKDE2LCAgZHR5cGU9dG9yY2gubG9uZykpICAjIGNsYXNzIDFcbmRpZmYgPSAoeTAgLSB5MSkuYWJzKCkubWVhbigpLml0ZW0oKVxucHJpbnQoXHUwMDI3Q2xhc3MtMCB2cyBjbGFzcy0xIG91dHB1dCBkaWZmOlx1MDAyNywgcm91bmQoZGlmZiwgNCksIFx1MDAyNyhleHBlY3QgXHUwMDNlIDApXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJpZ0dBTjogTGFyZ2UtU2NhbGUgQ29uZGl0aW9uYWwgR2VuZXJhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmlnR0FOIChCcm9jayBldCBhbC4gMjAxOCkgc2NhbGVzIGNvbmRpdGlvbmFsIEdBTnMgdG8gSW1hZ2VOZXQgNTEyw5c1MTIgdXNpbmcgYmF0Y2ggc2l6ZSAyMDQ4LCBjaGFubmVsIG11bHRpcGxpZXIgw5c0LCBzZWxmLWF0dGVudGlvbiBhdCA2NMOXNjQgcmVzb2x1dGlvbiwgc3BlY3RyYWwgbm9ybWFsaXNhdGlvbiBvbiBELCBhbmQgb3J0aG9nb25hbCByZWd1bGFyaXNhdGlvbiBvbiB3ZWlnaHRzLiBDbGFzcy1jb25kaXRpb25hbCBCYXRjaE5vcm0gaXMgYXBwbGllZCBhdCBldmVyeSByZXNpZHVhbCBibG9jayBpbiBHLCB3aXRoIM6zX3kgYW5kIM6yX3kgY29tcHV0ZWQgZnJvbSBhIHNoYXJlZCBjbGFzcyBlbWJlZGRpbmcgY29uY2F0ZW5hdGVkIHRvIHouIEJpZ0dBTiBhY2hpZXZlcyBGSUQgfjcgb24gSW1hZ2VOZXQgMTI4w5cxMjggdmVyc3VzIH4yOCBmb3IgdGhlIHByaW9yIGJlc3Qg4oCUIGRlbW9uc3RyYXRpbmcgdGhhdCBzY2FsZSBhbmQgd2VsbC1kZXNpZ25lZCBjb25kaXRpb25pbmcgdG9nZXRoZXIgY2xvc2UgbXVjaCBvZiB0aGUgcmVhbGlzbSBnYXAuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJCaWdHQU4gVHJ1bmNhdGlvbiBhbmQgQ2xhc3MgTGVha2FnZSIsImNvbnRlbnQiOiJCaWdHQU4gdXNlcyB0cnVuY2F0ZWQgTm9ybWFsIHNhbXBsaW5nIGF0IHRlc3QgdGltZSAodHJ1bmNhdGlvbiB0cmljaykgYW5kIG9ic2VydmVzIGEgdHJhZGUtb2ZmOiBzbWFsbGVyIHRydW5jYXRpb24gdGhyZXNob2xkIGdpdmVzIHNoYXJwZXIgYnV0IGxlc3MgZGl2ZXJzZSBpbWFnZXMuIEEga25vd24gZmFpbHVyZSBtb2RlIGlzIGNsYXNzIGxlYWthZ2Ug4oCUIGdlbmVyYXRpbmcgZmVhdHVyZXMgZnJvbSBuZWFyYnkgY2xhc3NlcyDigJQgd2hpY2ggd29yc2VucyBhdCBoaWdoIHRydW5jYXRpb24uIEJpZ0dBTiBtaXRpZ2F0ZXMgdGhpcyBieSB0cmFpbmluZyB3aXRoIG9ydGhvZ29uYWwgcmVndWxhcmlzYXRpb24gdGhhdCBrZWVwcyB3ZWlnaHRzIG9uIHRoZSB1bml0IHNwaGVyZSwgcmVkdWNpbmcgbW9kZSBjb2xsYXBzZSBhbmQgbGVha2FnZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcnVuY2F0aW9uIFRyaWNrOiBRdWFsaXR5IHZzIERpdmVyc2l0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRydW5jYXRpb24gdHJpY2sgc2FtcGxlcyB6IGZyb20gYSB0cnVuY2F0ZWQgTm9ybWFsOiByZWplY3Qgc2FtcGxlcyB3aXRoIOKAlnrigJYv4oiaZCBcdTAwM2Ugz4QgYW5kIHJlc2FtcGxlLiBTbWFsbCDPhCBjb25zdHJhaW5zIHogdG8gYSBoaWdoLWRlbnNpdHkgcmVnaW9uIG9mIE4oMCxJKSwgc28gRyBtYXBzIGl0IHRvIGhpZ2gtcXVhbGl0eSB0eXBpY2FsIGltYWdlcy4gTGFyZ2Ugz4QgYWxsb3dzIHJhcmUgeiB2YWx1ZXMsIGluY3JlYXNpbmcgZGl2ZXJzaXR5IGJ1dCByaXNraW5nIGFydGVmYWN0cy4gVGhlIEZJROKAk0lTIHRyYWRlLW9mZiBhcyDPhCB2YXJpZXMgdHJhY2VzIGEgUGFyZXRvIGZyb250aWVyLiBUcnVuY2F0aW9uIGlzIGEgdGVzdC10aW1lIHRlY2huaXF1ZTsgRyBpcyB0cmFpbmVkIHdpdGhvdXQgaXQsIHRoZW4gdHJ1bmNhdGlvbiBpcyBhcHBsaWVkIG9ubHkgZHVyaW5nIGV2YWx1YXRpb24gb3IgZ2VuZXJhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHRydW5jYXRlZF9zYW1wbGUoRywgbl9jbGFzc2VzPTEwLCBuX3NhbXBsZXM9OCxcbiAgICAgICAgICAgICAgICAgICAgIHpfZGltPTEwMCwgdGhyZXNob2xkcz0oMC4zLCAwLjcsIDEuMCwgMS41KSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3U2FtcGxlIHogZnJvbSB0cnVuY2F0ZWQgTm9ybWFsOyByZXBvcnQgZGl2ZXJzaXR5IHBlciB0aHJlc2hvbGQuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgRy5ldmFsKClcbiAgICBmb3IgdGF1IGluIHRocmVzaG9sZHM6XG4gICAgICAgIHBvb2wgID0gdG9yY2gucmFuZG4obl9zYW1wbGVzICogMjAwLCB6X2RpbSlcbiAgICAgICAgbm9ybXMgPSBwb29sLm5vcm0oZGltPTEpIC8gbnAuc3FydCh6X2RpbSlcbiAgICAgICAgb2sgPSBwb29sW25vcm1zIFx1MDAzYyB0YXVdXG4gICAgICAgIG9rID0gb2tbOm5fc2FtcGxlc10gaWYgbGVuKG9rKSBcdTAwM2U9IG5fc2FtcGxlcyBlbHNlIHBvb2xbOm5fc2FtcGxlc11cbiAgICAgICAgbGJsID0gdG9yY2gucmFuZGludCgwLCBuX2NsYXNzZXMsIChsZW4ob2spLCkpXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgZmFrZSA9IEcob2ssIGxibClcbiAgICAgICAgcHJpbnQoXHUwMDI3dGF1PXs6LjFmfSAgYWNjZXB0ZWQ9e30gIGZha2Vfc3RkPXs6LjRmfVx1MDAyNy5mb3JtYXQoXG4gICAgICAgICAgICAgIHRhdSwgbGVuKG9rKSwgZmFrZS5zdGQoKS5pdGVtKCkpKVxuXG5HX2RlbW8gPSBDb25kaXRpb25hbEdlbmVyYXRvcigpXG50cnVuY2F0ZWRfc2FtcGxlKEdfZGVtbylcbnByaW50KFx1MDAyN0xvd2VyIHRhdTogZmV3ZXIgb3V0bGllciB6IC1cdTAwM2UgaGlnaGVyIHF1YWxpdHksIGxvd2VyIGRpdmVyc2l0eVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZXh0IGFuZCBDcm9zcy1BdHRlbnRpb24gQ29uZGl0aW9uaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb2Rlcm4gdGV4dC1jb25kaXRpb25hbCBnZW5lcmF0aW9uIHJlcGxhY2VzIHRoZSBjbGFzcyBlbWJlZGRpbmcgd2l0aCBhIHJpY2ggdGV4dCBlbmNvZGVyLiBDTElQIGVuY29kZXMgYSB0ZXh0IHByb21wdCBpbnRvIGEgNTEyLWQgdmVjdG9yIHRoYXQgc2VydmVzIGFzIHRoZSBjb25kaXRpb25pbmcgc2lnbmFsIOKAlCBwYXNzZWQgdG8gRyB2aWEgcHJvamVjdGlvbiBvciBjcm9zcy1hdHRlbnRpb24uIEluIGNyb3NzLWF0dGVudGlvbiBjb25kaXRpb25pbmcgKExETS9TdGFibGUgRGlmZnVzaW9uKSwgcXVlcmllcyBjb21lIGZyb20gc3BhdGlhbCBpbWFnZSBmZWF0dXJlcyBhbmQga2V5cy92YWx1ZXMgZnJvbSB0aGUgdGV4dCBlbWJlZGRpbmcsIGFsbG93aW5nIHRoZSBtb2RlbCB0byBhdHRlbmQgdG8gc3BlY2lmaWMgd29yZHMgZm9yIHNwZWNpZmljIHJlZ2lvbnMuIENMSVAgY29uZGl0aW9uaW5nIGFsc28gZW5hYmxlcyB6ZXJvLXNob3QgZ2VuZXJhdGlvbjogZGVzY3JpYmUgYW55IGNvbmNlcHQgaW4gdGV4dCBhbmQgZ2VuZXJhdGUgc2FtcGxlcyB3aXRob3V0IGNsYXNzLXNwZWNpZmljIHRyYWluaW5nIGRhdGEuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMYWJlbCBjb25jYXRlbmF0aW9uOiBlbWJlZCB5LCBjb25jYXRlbmF0ZSB0byB6IGFuZCBEIGlucHV0IOKAlCBzaW1wbGVzdCBhcHByb2FjaCBmb3Igc21hbGwgbl9jbGFzc2VzLiIsIlByb2plY3Rpb24gRDogRCh4LHkpPXBoaSh4KV5UIFZfeSArIHBzaShwaGkoeCkpIOKAlCBwcmluY2lwbGVkIGlubmVyLXByb2R1Y3QgZmFjdG9yaXNhdGlvbiwgYmV0dGVyIEZJRC4iLCJDbGFzcy1jb25kaXRpb25hbCBCTjogcGVyLWNsYXNzIGdhbW1hL2JldGEgYXQgZXZlcnkgbGF5ZXIg4oCUIEJpZ0dBTiBhcHByb2FjaCBmb3IgbGFyZ2Utc2NhbGUgZ2VuZXJhdGlvbi4iLCJUcnVuY2F0aW9uIHRyaWNrOiBzYW1wbGUgeiBmcm9tIHRydW5jYXRlZCBOb3JtYWwgYXQgdGVzdCB0aW1lIOKAlCB0cmFkZXMgZGl2ZXJzaXR5IGZvciBxdWFsaXR5LiIsIkNMSVAgY29uZGl0aW9uaW5nOiB0ZXh0IGVtYmVkZGluZyBhcyB5IOKAlCBlbmFibGVzIG9wZW4tdm9jYWJ1bGFyeSB6ZXJvLXNob3QgZ2VuZXJhdGlvbi4iLCJDcm9zcy1hdHRlbnRpb246IGF0dGVuZCBvdmVyIHRleHQgdG9rZW5zIGF0IGVhY2ggc3BhdGlhbCBzY2FsZSDigJQgU3RhYmxlIERpZmZ1c2lvbiAvIExETSBhcmNoaXRlY3R1cmUuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuY29uZGl0aW9uYWwgdnMgQ29uZGl0aW9uYWwgR0FOIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXNwZWN0IiwiVW5jb25kaXRpb25hbCBHQU4iLCJjR0FOIChjb25jYXQpIiwiUHJvamVjdGlvbiBEIiwiQmlnR0FOIl0sInJvd3MiOltbIkxhYmVsIGlucHV0IiwiTm9uZSIsImNvbmNhdCB0byB6IGFuZCBEIGlucHV0IiwiaW5uZXIgcHJvZHVjdCBpbiBEIG9ubHkiLCJjQk4gKyBzaGFyZWQgY2xhc3MgZW1iZWQiXSxbIkNvbnRyb2xzIGNsYXNzIiwiTm8iLCJZZXMiLCJZZXMiLCJZZXMiXSxbIkJOIGNvbmRpdGlvbmluZyIsIlN0YW5kYXJkIEJOIiwiU3RhbmRhcmQgQk4iLCJTdGFuZGFyZCBCTiIsIkNsYXNzLWNvbmRpdGlvbmFsIEJOIl0sWyJGSUQgQ0lGQVItMTAgKGFwcHJveCkiLCIyMOKAkzMwIiwiMTLigJMxOCIsIjnigJMxNCIsIjfigJM5Il0sWyJTdHJlbmd0aHMiLCJTaW1wbGUgYmFzZWxpbmUiLCJFYXN5IHRvIGltcGxlbWVudCIsIlByaW5jaXBsZWQsIGJldHRlciBGSUQiLCJTT1RBIHF1YWxpdHkgYXQgc2NhbGUiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHByb2plY3Rpb24gZGlzY3JpbWluYXRvciBhbmQgY2xhc3MtY29uZGl0aW9uYWwgQmF0Y2hOb3JtIGFyZSBjb21wbGVtZW50YXJ5OiB0aGUgZm9ybWVyIGltcHJvdmVzIGhvdyBEIHVzZXMgdGhlIGxhYmVsLCB3aGlsZSB0aGUgbGF0dGVyIGltcHJvdmVzIGhvdyBHIHVzZXMgaXQuIENvbWJpbmVkIGluIEJpZ0dBTiwgdGhleSBhY2hpZXZlIHN1YnN0YW50aWFsbHkgYmV0dGVyIGNsYXNzLWNvbmRpdGlvbmFsIEZJRCB0aGFuIG5haXZlIGNvbmNhdGVuYXRpb24sIHNldHRpbmcgdGhlIHN0YW5kYXJkIGZvciBsYXJnZS1zY2FsZSBjb25kaXRpb25hbCBpbWFnZSBzeW50aGVzaXMgYmVmb3JlIHRoZSBkaWZmdXNpb24gZXJhLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Conditional GAN (cGAN) — Class-Conditional and Projection Discriminator

A conditional GAN (cGAN) extends the vanilla GAN by supplying both the generator G and discriminator D with a conditioning signal y — typically a class label. The generator learns G: (z,y) → x, producing images belonging to class y. The discriminator learns to distinguish real (x,y) pairs from fake ones. Conditioning enables class-specific generation, reduces within-class sample diversity, and allows controllable synthesis — the foundation for large-scale models such as BigGAN and modern text-conditional diffusion models.

## Conditioning Generator and Discriminator

The simplest strategy embeds y into a dense vector via a learned nn.Embedding, then concatenates it to the noise vector z before feeding G. For D, the label embedding is concatenated to the flattened image. Embedding dimension (50–256) is a hyperparameter. The objective remains the standard GAN loss — BCE or hinge — with the pair (x,y) as input rather than x alone. This approach is called label concatenation conditioning and serves as the baseline against which projection discriminators are compared.

```python
import torch
import torch.nn as nn

class ConditionalGenerator(nn.Module):
    def __init__(self, z_dim=100, n_classes=10, img_dim=784, embed_dim=50):
        super().__init__()
        self.label_embed = nn.Embedding(n_classes, embed_dim)
        self.net = nn.Sequential(
            nn.Linear(z_dim + embed_dim, 256), nn.LeakyReLU(0.2),
            nn.Linear(256, 512), nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim), nn.Tanh())
    def forward(self, z, labels):
        return self.net(torch.cat([z, self.label_embed(labels)], 1))

class ConditionalDiscriminator(nn.Module):
    def __init__(self, n_classes=10, img_dim=784, embed_dim=50):
        super().__init__()
        self.label_embed = nn.Embedding(n_classes, embed_dim)
        self.net = nn.Sequential(
            nn.Linear(img_dim + embed_dim, 512), nn.LeakyReLU(0.2),
            nn.Linear(512, 256), nn.LeakyReLU(0.2),
            nn.Linear(256, 1))
    def forward(self, x, labels):
        return self.net(torch.cat([x, self.label_embed(labels)], 1))

torch.manual_seed(0)
G, D = ConditionalGenerator(), ConditionalDiscriminator()
z = torch.randn(8, 100)
labels = torch.randint(0, 10, (8,))
fake = G(z, labels)
score = D(fake.detach(), labels)
print('Fake shape:', fake.shape, '| Score shape:', score.shape)
```

## Projection Discriminator (Miyato 2018)

Concatenating the label embedding to D's input treats x and y symmetrically, ignoring their different statistical roles. The projection discriminator (Miyato & Koyama 2018) computes D(x,y) = φ(x)ᵀV_y + ψ(φ(x)), where φ is a deep feature extractor, V is the label embedding matrix, and ψ is an unconditional linear head. The inner product φ(x)ᵀV_y directly scores how well image features align with the class embedding — a principled factorisation grounded in the theory of energy-based models that empirically achieves lower FID than concatenation conditioning.

```python
import torch
import torch.nn as nn

class ProjectionDiscriminator(nn.Module):
    '''Miyato & Koyama 2018: D(x,y) = phi(x)^T V_y + psi(phi(x)).'''
    def __init__(self, feature_dim=256, n_classes=10):
        super().__init__()
        self.phi = nn.Sequential(
            nn.Linear(784, 512), nn.LeakyReLU(0.2),
            nn.Linear(512, feature_dim), nn.LeakyReLU(0.2))
        self.V   = nn.Embedding(n_classes, feature_dim)  # label matrix
        self.psi = nn.Linear(feature_dim, 1)             # unconditional head

    def forward(self, x, labels):
        h   = self.phi(x)                         # (B, feature_dim)
        v_y = self.V(labels)                      # (B, feature_dim)
        proj   = (h * v_y).sum(1, keepdim=True)  # inner product (B, 1)
        uncond = self.psi(h)                      # bias term    (B, 1)
        return proj + uncond

torch.manual_seed(1)
D_proj = ProjectionDiscriminator()
x = torch.randn(8, 784)
labels = torch.randint(0, 10, (8,))
out = D_proj(x, labels)
print('Projection D output shape:', out.shape)  # (8, 1)
```

## Class-Conditional Batch Normalization

Class-conditional BatchNorm (cBN) uses a separate (γ_y, β_y) pair for each class y instead of global γ and β. Features are normalised across the batch as usual, but the affine transform is class-specific: h = γ_y · BN(h) + β_y. BigGAN applies cBN throughout the generator, allowing the network to modulate activations at every layer based on class identity. In BigGAN, γ_y and β_y are linear projections of a shared class embedding rather than direct lookups, making the conditioning parametrically efficient.

```python
import torch
import torch.nn as nn

class ConditionalBatchNorm(nn.Module):
    '''Separate gamma/beta per class, as used in BigGAN generator.'''
    def __init__(self, num_features, n_classes=10):
        super().__init__()
        self.bn    = nn.BatchNorm1d(num_features, affine=False)
        self.gamma = nn.Embedding(n_classes, num_features)
        self.beta  = nn.Embedding(n_classes, num_features)
        nn.init.ones_(self.gamma.weight)
        nn.init.zeros_(self.beta.weight)

    def forward(self, x, labels):
        out = self.bn(x)
        g   = self.gamma(labels)  # (B, num_features)
        b   = self.beta(labels)   # (B, num_features)
        return g * out + b

cbn = ConditionalBatchNorm(64, 10)
x   = torch.randn(16, 64)
y0  = cbn(x, torch.zeros(16, dtype=torch.long))  # class 0
y1  = cbn(x, torch.ones(16,  dtype=torch.long))  # class 1
diff = (y0 - y1).abs().mean().item()
print('Class-0 vs class-1 output diff:', round(diff, 4), '(expect > 0)')
```

## BigGAN: Large-Scale Conditional Generation

BigGAN (Brock et al. 2018) scales conditional GANs to ImageNet 512×512 using batch size 2048, channel multiplier ×4, self-attention at 64×64 resolution, spectral normalisation on D, and orthogonal regularisation on weights. Class-conditional BatchNorm is applied at every residual block in G, with γ_y and β_y computed from a shared class embedding concatenated to z. BigGAN achieves FID ~7 on ImageNet 128×128 versus ~28 for the prior best — demonstrating that scale and well-designed conditioning together close much of the realism gap.

> **BigGAN Truncation and Class Leakage**: BigGAN uses truncated Normal sampling at test time (truncation trick) and observes a trade-off: smaller truncation threshold gives sharper but less diverse images. A known failure mode is class leakage — generating features from nearby classes — which worsens at high truncation. BigGAN mitigates this by training with orthogonal regularisation that keeps weights on the unit sphere, reducing mode collapse and leakage.

## Truncation Trick: Quality vs Diversity

The truncation trick samples z from a truncated Normal: reject samples with ‖z‖/√d > τ and resample. Small τ constrains z to a high-density region of N(0,I), so G maps it to high-quality typical images. Large τ allows rare z values, increasing diversity but risking artefacts. The FID–IS trade-off as τ varies traces a Pareto frontier. Truncation is a test-time technique; G is trained without it, then truncation is applied only during evaluation or generation.

```python
import torch
import numpy as np

def truncated_sample(G, n_classes=10, n_samples=8,
                     z_dim=100, thresholds=(0.3, 0.7, 1.0, 1.5)):
    '''Sample z from truncated Normal; report diversity per threshold.'''
    G.eval()
    for tau in thresholds:
        pool  = torch.randn(n_samples * 200, z_dim)
        norms = pool.norm(dim=1) / np.sqrt(z_dim)
        ok = pool[norms < tau]
        ok = ok[:n_samples] if len(ok) >= n_samples else pool[:n_samples]
        lbl = torch.randint(0, n_classes, (len(ok),))
        with torch.no_grad():
            fake = G(ok, lbl)
        print('tau={:.1f}  accepted={}  fake_std={:.4f}'.format(
              tau, len(ok), fake.std().item()))

G_demo = ConditionalGenerator()
truncated_sample(G_demo)
print('Lower tau: fewer outlier z -> higher quality, lower diversity')
```

## Text and Cross-Attention Conditioning

Modern text-conditional generation replaces the class embedding with a rich text encoder. CLIP encodes a text prompt into a 512-d vector that serves as the conditioning signal — passed to G via projection or cross-attention. In cross-attention conditioning (LDM/Stable Diffusion), queries come from spatial image features and keys/values from the text embedding, allowing the model to attend to specific words for specific regions. CLIP conditioning also enables zero-shot generation: describe any concept in text and generate samples without class-specific training data.

- Label concatenation: embed y, concatenate to z and D input — simplest approach for small n_classes.
- Projection D: D(x,y)=phi(x)^T V_y + psi(phi(x)) — principled inner-product factorisation, better FID.
- Class-conditional BN: per-class gamma/beta at every layer — BigGAN approach for large-scale generation.
- Truncation trick: sample z from truncated Normal at test time — trades diversity for quality.
- CLIP conditioning: text embedding as y — enables open-vocabulary zero-shot generation.
- Cross-attention: attend over text tokens at each spatial scale — Stable Diffusion / LDM architecture.

## Unconditional vs Conditional GAN Comparison

| Aspect | Unconditional GAN | cGAN (concat) | Projection D | BigGAN |
| --- | --- | --- | --- | --- |
| Label input | None | concat to z and D input | inner product in D only | cBN + shared class embed |
| Controls class | No | Yes | Yes | Yes |
| BN conditioning | Standard BN | Standard BN | Standard BN | Class-conditional BN |
| FID CIFAR-10 (approx) | 20–30 | 12–18 | 9–14 | 7–9 |
| Strengths | Simple baseline | Easy to implement | Principled, better FID | SOTA quality at scale |

The projection discriminator and class-conditional BatchNorm are complementary: the former improves how D uses the label, while the latter improves how G uses it. Combined in BigGAN, they achieve substantially better class-conditional FID than naive concatenation, setting the standard for large-scale conditional image synthesis before the diffusion era.

---

