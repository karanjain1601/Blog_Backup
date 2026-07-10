---
title: "Label Smoothing — Soft Targets and Calibration"
slug: "label-smoothing"
description: "Derive label smoothing from first principles, measure calibration via ECE and reliability diagrams, implement temperature scaling for post-hoc calibration, and compare calibration methods."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSGFyZCBvbmUtaG90IHRhcmdldHMgWzAsIDAsIDEsIDAsIC4uLl0gdHJhaW4gdGhlIG1vZGVsIHRvIG91dHB1dCBsb2coMCkgZm9yIGluY29ycmVjdCBjbGFzc2VzLCBwdXNoaW5nIHRoZSBsb2dpdCBmb3IgdGhlIGNvcnJlY3QgY2xhc3MgdG93YXJkICviiJ4gcmVsYXRpdmUgdG8gb3RoZXJzLiBUaGlzIG1ha2VzIHRoZSBtb2RlbCBvdmVyY29uZmlkZW50OiBhdCB0ZXN0IHRpbWUgaXQgYXNzaWducyBwcm9iYWJpbGl0aWVzIGNsb3NlIHRvIDEuMCBldmVuIGZvciBkaWZmaWN1bHQgZXhhbXBsZXMgaXQgc2hvdWxkIGJlIHVuY2VydGFpbiBhYm91dC4gTGFiZWwgc21vb3RoaW5nIChTemVnZWR5IGV0IGFsLiAyMDE2LCBJbmNlcHRpb24gVjMpIHJlcGxhY2VzIGhhcmQgdGFyZ2V0cyB3aXRoIHNvZnQgdGFyZ2V0cywgY2FwcGluZyB0aGUgbWF4aW11bSBwcm9iYWJpbGl0eSB0aGUgbW9kZWwgaXMgdHJhaW5lZCB0byBhc3NpZ24gYW5kIGltcHJvdmluZyBjYWxpYnJhdGlvbiBzaWduaWZpY2FudGx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxhYmVsIFNtb290aGluZyBGb3JtdWxhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMYWJlbCBzbW9vdGhpbmcgd2l0aCBwYXJhbWV0ZXIgzrUg4oiIIFswLCAxKSByZXBsYWNlczogaGFyZCB0YXJnZXQgeeG1oiA9IDEg4oaSIOG7ueG1oiA9IDEg4oiSIM61LCBoYXJkIHRhcmdldCB54bWiID0gMCDihpIg4bu54bWiID0gzrUvKEviiJIxKSB3aGVyZSBLIGlzIHRoZSBudW1iZXIgb2YgY2xhc3Nlcy4gVGhlIHNtb290aGVkIGNyb3NzLWVudHJvcHkgaXM6IENFX3Ntb290aCA9ICgx4oiSzrUpIMK3IENFKGhhcmQgdGFyZ2V0KSArIM61IMK3IENFKHVuaWZvcm0gdGFyZ2V0KSA9IOKIks6j4bWiIOG7ueG1oiDCtyBsb2cocOG1oikuIEVxdWl2YWxlbnRseTogQ0Vfc21vb3RoID0gQ0UoaGFyZCkg4oiSIM61IMK3IChDRShoYXJkKSDiiJIgSCh1bmlmb3JtKSkgd2hlcmUgSCh1bmlmb3JtKSA9IGxvZyhLKSBpcyBhIGNvbnN0YW50LiBUaGUgS0wgZGl2ZXJnZW5jZSBpbnRlcnByZXRhdGlvbjogbGFiZWwgc21vb3RoaW5nIG1pbmltaXplcyBLTCjhu7kg4oCWIHApIGluc3RlYWQgb2YgS0woeSDigJYgcCksIHdoaWNoIHByZXZlbnRzIHRoZSBtb2RlbCBmcm9tIGZpdHRpbmcgdGhlIGV4dHJlbWVseSBwZWFrZWQgZGlzdHJpYnV0aW9uIHJlcXVpcmVkIGJ5IGhhcmQgdGFyZ2V0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGxhYmVsX3Ntb290aGluZ19sb3NzKGxvZ2l0cywgdGFyZ2V0cywgZXBzPTAuMSwgcmVkdWN0aW9uPVx1MDAyN21lYW5cdTAwMjcpOlxuICAgIG5fY2xhc3NlcyA9IGxvZ2l0cy5zaXplKC0xKVxuICAgICMgU29mdCB0YXJnZXQ6IDEtZXBzIGZvciBjb3JyZWN0IGNsYXNzLCBlcHMvKEstMSkgZm9yIG90aGVyc1xuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBzbW9vdGhfdGFyZ2V0cyA9IHRvcmNoLmZ1bGxfbGlrZShsb2dpdHMsIGVwcyAvIChuX2NsYXNzZXMgLSAxKSlcbiAgICAgICAgc21vb3RoX3RhcmdldHMuc2NhdHRlcl8oMSwgdGFyZ2V0cy51bnNxdWVlemUoMSksIDEuMCAtIGVwcylcbiAgICBsb2dfcHJvYnMgPSBGLmxvZ19zb2Z0bWF4KGxvZ2l0cywgZGltPS0xKVxuICAgIGxvc3MgPSAtKHNtb290aF90YXJnZXRzICogbG9nX3Byb2JzKS5zdW0oZGltPS0xKVxuICAgIHJldHVybiBsb3NzLm1lYW4oKSBpZiByZWR1Y3Rpb24gPT0gXHUwMDI3bWVhblx1MDAyNyBlbHNlIGxvc3NcblxuIyBDb21wYXJlIHdpdGggUHlUb3JjaCBidWlsdC1pblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5sb2dpdHMgID0gdG9yY2gucmFuZG4oMzIsIDEwKVxudGFyZ2V0cyA9IHRvcmNoLnJhbmRpbnQoMCwgMTAsICgzMiwpKVxuZXBzID0gMC4xXG5cbmxvc3Nfc2NyYXRjaCA9IGxhYmVsX3Ntb290aGluZ19sb3NzKGxvZ2l0cywgdGFyZ2V0cywgZXBzPWVwcylcbmNlX2J1aWx0aW4gICA9IG5uLkNyb3NzRW50cm9weUxvc3MobGFiZWxfc21vb3RoaW5nPWVwcylcbmxvc3NfYnVpbHRpbiA9IGNlX2J1aWx0aW4obG9naXRzLCB0YXJnZXRzKVxuXG5wcmludChmXHUwMDI3U2NyYXRjaCBsYWJlbCBzbW9vdGhpbmcgbG9zcyA6IHtsb3NzX3NjcmF0Y2guaXRlbSgpOi42Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3UHlUb3JjaCBidWlsdC1pbiBMUyBsb3NzICAgICA6IHtsb3NzX2J1aWx0aW4uaXRlbSgpOi42Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3RGlmZmVyZW5jZSAgICAgICAgICAgICAgICAgICA6IHthYnMobG9zc19zY3JhdGNoLml0ZW0oKS1sb3NzX2J1aWx0aW4uaXRlbSgpKTouMmV9XHUwMDI3KVxuXG5oYXJkX2NlID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpKGxvZ2l0cywgdGFyZ2V0cylcbnByaW50KGZcdTAwMjdIYXJkIENFIGxvc3MgICAgICAgICAgICAgICAgIDoge2hhcmRfY2UuaXRlbSgpOi42Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3TGFiZWwgc21vb3RoaW5nIHJlZHVjZXMgbG9zcyBieSBkaXNjb3VyYWdpbmcgb3ZlcmNvbmZpZGVuY2UuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNhbGlicmF0aW9uIGFuZCBPdmVyY29uZmlkZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBwZXJmZWN0bHkgY2FsaWJyYXRlZCBtb2RlbCBzYXRpc2ZpZXM6IFAoY29ycmVjdCB8IGNvbmZpZGVuY2UgPSBwKSA9IHAgZm9yIGFsbCBwLiBJbiBvdGhlciB3b3Jkcywgd2hlbiB0aGUgbW9kZWwgc2F5cyBpdCBpcyA4MCUgY29uZmlkZW50LCBpdCBzaG91bGQgYmUgY29ycmVjdCA4MCUgb2YgdGhlIHRpbWUuIE1vZGVscyB0cmFpbmVkIHdpdGggaGFyZCB0YXJnZXRzIGFyZSBzeXN0ZW1hdGljYWxseSBvdmVyY29uZmlkZW50OiB0aGV5IHByZWRpY3QgOTUlKyBjb25maWRlbmNlIG9uIHNhbXBsZXMgd2hlcmUgdGhlaXIgYWN0dWFsIGFjY3VyYWN5IGlzIG11Y2ggbG93ZXIuIEEgcmVsaWFiaWxpdHkgZGlhZ3JhbSBwbG90cyBtb2RlbCBjb25maWRlbmNlICh4LWF4aXMpIGFnYWluc3Qgb2JzZXJ2ZWQgYWNjdXJhY3kgKHktYXhpcykg4oCUIGEgcGVyZmVjdGx5IGNhbGlicmF0ZWQgbW9kZWwgZmFsbHMgb24gdGhlIGRpYWdvbmFsLiBNb2RlbHMgdHJhaW5lZCB3aXRoIGxhYmVsIHNtb290aGluZyBzdGF5IG11Y2ggY2xvc2VyIHRvIHRoZSBkaWFnb25hbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCB0cmFpbl90ZXN0X3NwbGl0XG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihuX3NhbXBsZXM9MzAwMCwgbl9mZWF0dXJlcz0yMCwgbl9jbGFzc2VzPTUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9pbmZvcm1hdGl2ZT0xNSwgcmFuZG9tX3N0YXRlPTQyKVxuWCA9IHRvcmNoLnRlbnNvcihYLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxueSA9IHRvcmNoLnRlbnNvcih5LCBkdHlwZT10b3JjaC5sb25nKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuNCwgcmFuZG9tX3N0YXRlPTApXG5cbmRlZiB0cmFpbl9tb2RlbChlcHMsIGVwb2Nocz02MCk6XG4gICAgbmV0ID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMjAsIDY0KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoNjQsIDUpKVxuICAgIG9wdCA9IHRvcmNoLm9wdGltLkFkYW0obmV0LnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBsb3NzX2ZuID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcyhsYWJlbF9zbW9vdGhpbmc9ZXBzKVxuICAgIGZvciBfIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIG5ldC50cmFpbigpXG4gICAgICAgIGxvc3MgPSBsb3NzX2ZuKG5ldChYX3RyKSwgeV90cilcbiAgICAgICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbiAgICBuZXQuZXZhbCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHByb2JzID0gRi5zb2Z0bWF4KG5ldChYX3RlKSwgZGltPS0xKVxuICAgIHJldHVybiBwcm9icy5udW1weSgpXG5cbnByb2JzX2hhcmQgPSB0cmFpbl9tb2RlbChlcHM9MC4wKVxucHJvYnNfc21vb3RoID0gdHJhaW5fbW9kZWwoZXBzPTAuMSlcbm1heF9jb25mX2hhcmQgPSBwcm9ic19oYXJkLm1heChheGlzPTEpLm1lYW4oKVxubWF4X2NvbmZfc21vb3RoID0gcHJvYnNfc21vb3RoLm1heChheGlzPTEpLm1lYW4oKVxucHJpbnQoZlx1MDAyN0hhcmQgdGFyZ2V0cyAgIOKAlCBhdmcgbWF4IGNvbmZpZGVuY2U6IHttYXhfY29uZl9oYXJkOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3TGFiZWwgc21vb3RoaW5nIOKAlCBhdmcgbWF4IGNvbmZpZGVuY2U6IHttYXhfY29uZl9zbW9vdGg6LjNmfVx1MDAyNykifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvdXRwdXQgYWJvdmUgc2hvd3MgdGhhdCBsYWJlbCBzbW9vdGhpbmcgbG93ZXJzIHRoZSBhdmVyYWdlIG1heGltdW0gY29uZmlkZW5jZSBjb21wYXJlZCB0byBoYXJkLXRhcmdldCB0cmFpbmluZy4gVG8gcXVhbnRpZnkgdGhpcyBpbXByb3ZlbWVudCByaWdvcm91c2x5LCB3ZSBjb21wdXRlIHRoZSBFeHBlY3RlZCBDYWxpYnJhdGlvbiBFcnJvciAoRUNFKSwgd2hpY2ggbWVhc3VyZXMgdGhlIGdhcCBiZXR3ZWVuIHByZWRpY3RlZCBjb25maWRlbmNlIGFuZCBhY3R1YWwgYWNjdXJhY3kgYWNyb3NzIGNvbmZpZGVuY2UgYmlucy4gQSBwZXJmZWN0bHkgY2FsaWJyYXRlZCBtb2RlbCBoYXMgRUNFPTAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXhwZWN0ZWQgQ2FsaWJyYXRpb24gRXJyb3IifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBFeHBlY3RlZCBDYWxpYnJhdGlvbiBFcnJvciAoRUNFKSBxdWFudGlmaWVzIG1pc2NhbGlicmF0aW9uLiBTb3J0IHByZWRpY3Rpb25zIGJ5IGNvbmZpZGVuY2UgYW5kIGRpdmlkZSBpbnRvIE0gZXF1YWwtd2lkdGggYmlucyBC4oKBLCAuLi4sIELigpguIEZvciBlYWNoIGJpbjogYWNjKELigpgpID0gZnJhY3Rpb24gY29ycmVjdCBpbiBiaW4sIGNvbmYoQuKCmCkgPSBtZWFuIGNvbmZpZGVuY2UgaW4gYmluLiBFQ0UgPSDOo+KCmCAofELigph8L04pIMK3IHxhY2MoQuKCmCkg4oiSIGNvbmYoQuKCmCl8LiBXZWlnaHRlZCBhdmVyYWdlIG9mIGNvbmZpZGVuY2UtYWNjdXJhY3kgZ2FwIGFjcm9zcyBiaW5zLiBBIG1vZGVsIHdpdGggRUNFPTAgaXMgcGVyZmVjdGx5IGNhbGlicmF0ZWQuIFR5cGljYWwgRUNFIGZvciBSZXNOZXQtNTAgd2l0aCBoYXJkIHRhcmdldHMgb24gQ0lGQVItMTAwOiB+MC4xNSB0byAwLjIwLiBXaXRoIGxhYmVsIHNtb290aGluZyDOtT0wLjE6IH4wLjA1IHRvIDAuMDguIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY29tcHV0ZV9lY2UocHJvYnMsIGxhYmVscywgbl9iaW5zPTEwKTpcbiAgICBjb25maWRlbmNlcyA9IHByb2JzLm1heChheGlzPTEpXG4gICAgcHJlZGljdGlvbnMgPSBwcm9icy5hcmdtYXgoYXhpcz0xKVxuICAgIGNvcnJlY3QgPSAocHJlZGljdGlvbnMgPT0gbGFiZWxzKS5hc3R5cGUoZmxvYXQpXG4gICAgYmluX2VkZ2VzID0gbnAubGluc3BhY2UoMCwgMSwgbl9iaW5zICsgMSlcbiAgICBlY2UgPSAwLjBcbiAgICBmb3IgaSBpbiByYW5nZShuX2JpbnMpOlxuICAgICAgICBsbywgaGkgPSBiaW5fZWRnZXNbaV0sIGJpbl9lZGdlc1tpICsgMV1cbiAgICAgICAgbWFzayA9IChjb25maWRlbmNlcyBcdTAwM2U9IGxvKSBcdTAwMjYgKGNvbmZpZGVuY2VzIFx1MDAzYyBoaSlcbiAgICAgICAgaWYgbWFzay5zdW0oKSA9PSAwOlxuICAgICAgICAgICAgY29udGludWVcbiAgICAgICAgYmluX2FjYyAgPSBjb3JyZWN0W21hc2tdLm1lYW4oKVxuICAgICAgICBiaW5fY29uZiA9IGNvbmZpZGVuY2VzW21hc2tdLm1lYW4oKVxuICAgICAgICBlY2UgKz0gKG1hc2suc3VtKCkgLyBsZW4obGFiZWxzKSkgKiBhYnMoYmluX2FjYyAtIGJpbl9jb25mKVxuICAgIHJldHVybiBlY2VcblxubnAucmFuZG9tLnNlZWQoNDIpXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcblgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKG5fc2FtcGxlcz0yMDAwLCBuX2ZlYXR1cmVzPTIwLCBuX2NsYXNzZXM9NSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX2luZm9ybWF0aXZlPTE1LCByYW5kb21fc3RhdGU9NDIpXG5cbiMgU2ltdWxhdGUgb3ZlcmNvbmZpZGVudCBwcmVkaWN0aW9ucyAoaGFyZCB0YXJnZXRzKVxuY29uZmlkZW50X3Byb2JzID0gbnAucmFuZG9tLmRpcmljaGxldChbMTAsIDEsIDEsIDEsIDFdLCBzaXplPWxlbih5KSlcbiMgU2ltdWxhdGUgd2VsbC1jYWxpYnJhdGVkIHByZWRpY3Rpb25zIChzbW9vdGhlZClcbmNhbGlicmF0ZWRfcHJvYnMgPSBucC5yYW5kb20uZGlyaWNobGV0KFszLCAxLCAxLCAxLCAxXSwgc2l6ZT1sZW4oeSkpXG5cbmVjZV9vdmVyY29uZiA9IGNvbXB1dGVfZWNlKGNvbmZpZGVudF9wcm9icywgeSlcbmVjZV9jYWxpYnJhdGVkID0gY29tcHV0ZV9lY2UoY2FsaWJyYXRlZF9wcm9icywgeSlcbnByaW50KGZcdTAwMjdFQ0UgKG92ZXJjb25maWRlbnQgLyBoYXJkIHRhcmdldHMpOiB7ZWNlX292ZXJjb25mOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3RUNFIChjYWxpYnJhdGVkIC8gbGFiZWwgc21vb3RoaW5nKToge2VjZV9jYWxpYnJhdGVkOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdMb3dlciBFQ0UgPSBiZXR0ZXIgY2FsaWJyYXRlZCA9IGNvbmZpZGVuY2UgbWF0Y2hlcyBhY2N1cmFjeS5cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJMYWJlbCBTbW9vdGhpbmcgSHVydHMgS25vd2xlZGdlIERpc3RpbGxhdGlvbiIsImNvbnRlbnQiOiJXaGVuIHVzaW5nIGEgbGFiZWwtc21vb3RoZWQgdGVhY2hlciB0byBnZW5lcmF0ZSBzb2Z0IHRhcmdldHMgZm9yIHN0dWRlbnQgdHJhaW5pbmcgKGtub3dsZWRnZSBkaXN0aWxsYXRpb24pLCB0aGUgc21vb3RoZWQgc29mdG1heCBvdXRwdXRzIGNhcnJ5IGxlc3MgaW5mb3JtYXRpb24gdGhhbiBzdGFuZGFyZCB0ZW1wZXJhdHVyZS1zY2FsZWQgcHJvYmFiaWxpdGllcy4gSGludG9uIGV0IGFsLiByZWNvbW1lbmQgdXNpbmcgYSBoaWdoIHRlbXBlcmF0dXJlIFQgKGUuZy4sIFQ9NCB0byBUPTIwKSB3aXRob3V0IGxhYmVsIHNtb290aGluZyBmb3IgdGhlIHRlYWNoZXIgZHVyaW5nIGRpc3RpbGxhdGlvbi4gTGFiZWwgc21vb3RoaW5nIGlzIGJlc3QgYXBwbGllZCBvbmx5IGR1cmluZyB0aGUgZmluYWwgdHJhaW5pbmcgcnVuIG9mIGEgbW9kZWwgdGhhdCB3aWxsIHNlcnZlIGFzIGFuIGVuZHBvaW50LCBub3QgYXMgYSB0ZWFjaGVyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRlbXBlcmF0dXJlIFNjYWxpbmcgZm9yIFBvc3QtSG9jIENhbGlicmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUZW1wZXJhdHVyZSBzY2FsaW5nIChHdW8gZXQgYWwuIDIwMTcpIGlzIHRoZSBzaW1wbGVzdCBhbmQgbW9zdCBlZmZlY3RpdmUgcG9zdC1ob2MgY2FsaWJyYXRpb24gbWV0aG9kLiBBZnRlciB0cmFpbmluZywgbGVhcm4gYSBzaW5nbGUgc2NhbGFyIFQgXHUwMDNlIDEgdGhhdCBkaXZpZGVzIHRoZSBsb2dpdHM6IHDMgiA9IHNvZnRtYXgoei9UKS4gVCBcdTAwM2UgMSBtYWtlcyB0aGUgZGlzdHJpYnV0aW9uIHNvZnRlciAobGVzcyBjb25maWRlbnQpOyBUIFx1MDAzYyAxIG1ha2VzIGl0IHNoYXJwZXIgKG1vcmUgY29uZmlkZW50KS4gVCBpcyBmaXQgYnkgbWluaW1pemluZyBOTEwgb24gYSBoZWxkLW91dCBjYWxpYnJhdGlvbiBzZXQuIFRoaXMgZG9lcyBub3QgY2hhbmdlIGFjY3VyYWN5IChhcmdtYXggaXMgcHJlc2VydmVkKSBidXQgZHJhbWF0aWNhbGx5IHJlZHVjZXMgRUNFIOKAlCBvZnRlbiBmcm9tIDAuMTDigJMwLjE1IHRvIDAuMDHigJMwLjAzLiBUZW1wZXJhdHVyZSBzY2FsaW5nIGdlbmVyYWxpemVzIGJldHRlciB0aGFuIHZlY3RvciBvciBtYXRyaXggc2NhbGluZyBtZXRob2RzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIFRlbXBlcmF0dXJlU2NhbGluZyhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYudGVtcGVyYXR1cmUgPSBubi5QYXJhbWV0ZXIodG9yY2gub25lcygxKSAqIDEuNSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGxvZ2l0cyk6XG4gICAgICAgIHJldHVybiBsb2dpdHMgLyBzZWxmLnRlbXBlcmF0dXJlLmNsYW1wKG1pbj0wLjA1KVxuXG5kZWYgZml0X3RlbXBlcmF0dXJlKGxvZ2l0cywgbGFiZWxzLCBscj0wLjAxLCBuX3N0ZXBzPTIwMCk6XG4gICAgdHMgPSBUZW1wZXJhdHVyZVNjYWxpbmcoKVxuICAgIG9wdGltaXplciA9IHRvcmNoLm9wdGltLkxCRkdTKFt0cy50ZW1wZXJhdHVyZV0sIGxyPWxyLCBtYXhfaXRlcj1uX3N0ZXBzKVxuICAgIGRlZiBjbG9zdXJlKCk6XG4gICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgICAgICBzY2FsZWQgPSB0cyhsb2dpdHMpXG4gICAgICAgIGxvc3MgPSBGLmNyb3NzX2VudHJvcHkoc2NhbGVkLCBsYWJlbHMpXG4gICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICByZXR1cm4gbG9zc1xuICAgIG9wdGltaXplci5zdGVwKGNsb3N1cmUpXG4gICAgcmV0dXJuIHRzLnRlbXBlcmF0dXJlLml0ZW0oKVxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbmxvZ2l0c19jYWwgPSB0b3JjaC5yYW5kbig1MDAsIDEwKSAqIDMgICMgb3ZlcmNvbmZpZGVudCBsb2dpdHNcbmxhYmVsc19jYWwgPSB0b3JjaC5yYW5kaW50KDAsIDEwLCAoNTAwLCkpXG5cblRfb3B0ID0gZml0X3RlbXBlcmF0dXJlKGxvZ2l0c19jYWwuY2xvbmUoKSwgbGFiZWxzX2NhbClcbnByaW50KGZcdTAwMjdPcHRpbWFsIHRlbXBlcmF0dXJlIFQgPSB7VF9vcHQ6LjRmfVx1MDAyNylcblxucHJvYnNfYmVmb3JlID0gRi5zb2Z0bWF4KGxvZ2l0c19jYWwsIGRpbT0tMSkuZGV0YWNoKCkubnVtcHkoKVxucHJvYnNfYWZ0ZXIgID0gRi5zb2Z0bWF4KGxvZ2l0c19jYWwgLyBUX29wdCwgZGltPS0xKS5kZXRhY2goKS5udW1weSgpXG5wcmludChmXHUwMDI3QXZnIG1heCBjb25maWRlbmNlIGJlZm9yZSBzY2FsaW5nOiB7cHJvYnNfYmVmb3JlLm1heChheGlzPTEpLm1lYW4oKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0F2ZyBtYXggY29uZmlkZW5jZSBhZnRlciAgc2NhbGluZzoge3Byb2JzX2FmdGVyLm1heChheGlzPTEpLm1lYW4oKTouM2Z9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoZW4gdG8gVXNlIExhYmVsIFNtb290aGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGFiZWwgc21vb3RoaW5nIHdpdGggzrU9MC4xIGlzIGEgcmVsaWFibGUgZGVmYXVsdCBmb3IgaW1hZ2UgY2xhc3NpZmljYXRpb24sIG11bHRpLWNsYXNzIE5MUCB0YXNrcywgYW5kIHNwZWVjaCByZWNvZ25pdGlvbi4gSXQgaGVscHMgbW9zdCB3aGVuOiB0aGUgdHJhaW5pbmcgc2V0IGhhcyBub2lzeSBsYWJlbHMgKHNtb290aGluZyBhYnNvcmJzIGxhYmVsIG5vaXNlKSwgdGhlIG1vZGVsIGlzIGxhcmdlIHJlbGF0aXZlIHRvIHRoZSBkYXRhc2V0IChyZWR1Y2VzIG92ZXJmaXR0aW5nIHRvIGV4YWN0IGxhYmVscyksIGFuZCBjYWxpYnJhdGlvbiBxdWFsaXR5IGlzIGltcG9ydGFudCBmb3IgZG93bnN0cmVhbSBkZWNpc2lvbiBtYWtpbmcuIEF2b2lkIGxhYmVsIHNtb290aGluZyB3aGVuOiB0cmFpbmluZyBhIHRlYWNoZXIgbW9kZWwgZm9yIGtub3dsZWRnZSBkaXN0aWxsYXRpb24sIHdoZW4gdGhlIHRhc2sgcmVxdWlyZXMgaGFyZCBkZWNpc2lvbnMgKGJpbmFyeSBjbGFzc2lmaWNhdGlvbiB3aXRoIGJhbGFuY2VkIGNsYXNzZXMpLCBvciB3aGVuIGNsYXNzZXMgZ2VudWluZWx5IGhhdmUgbm8gaW50ZXItY2xhc3Mgc2ltaWxhcml0eS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIs61PTAuMSBpcyB0aGUgc3RhbmRhcmQgZGVmYXVsdCBmcm9tIEluY2VwdGlvbiBWMyDigJQgd29ya3Mgd2VsbCBmb3IgbW9zdCBjbGFzc2lmaWNhdGlvbiB0YXNrcy4iLCLOtT0wLjIgY2FuIGhlbHAgd2l0aCB2ZXJ5IG5vaXN5IGxhYmVscyBidXQgbWF5IHJlZHVjZSB0b3AtMSBhY2N1cmFjeS4iLCJMYWJlbCBzbW9vdGhpbmcgcmVkdWNlcyB0aGUgbWF4aW11bSBsb2dpdCBkaWZmZXJlbmNlIOKAlCBpbmRpcmVjdGx5IHJlZ3VsYXJpemVzIHRoZSB3ZWlnaHQgbWFnbml0dWRlLiIsIkNvbWJpbmUgd2l0aCBtaXh1cCB0cmFpbmluZzogYm90aCBvcGVyYXRlIG9uIHNvZnQgdGFyZ2V0cyBhbmQgdGhleSBhcmUgY29tcGxlbWVudGFyeSByZWd1bGFyaXphdGlvbiBzdHJhdGVnaWVzLiIsIlBvc3QtaG9jIGZpeDogaWYgbGFiZWwgc21vb3RoaW5nIHdhcyBub3QgdXNlZCBkdXJpbmcgdHJhaW5pbmcsIHRlbXBlcmF0dXJlIHNjYWxpbmcgYWNoaWV2ZXMgc2ltaWxhciBjYWxpYnJhdGlvbiBpbXByb3ZlbWVudCB3aXRob3V0IHJldHJhaW5pbmcuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNhbGlicmF0aW9uIE1ldGhvZHMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJXaGVuIEFwcGxpZWQiLCJSZXF1aXJlcyBSZXRyYWluaW5nIiwiRUNFIEltcGFjdCIsIkFjY3VyYWN5IEltcGFjdCIsIk5vdGVzIl0sInJvd3MiOltbIkhhcmQgdGFyZ2V0cyAoYmFzZWxpbmUpIiwiVHJhaW5pbmciLCJOL0EiLCJQb29yIGNhbGlicmF0aW9uIChoaWdoIEVDRSkiLCJSZWZlcmVuY2UiLCJNb2RlbCB0cmFpbmVkIHRvIGJlIG92ZXJjb25maWRlbnQiXSxbIkxhYmVsIHNtb290aGluZyAozrU9MC4xKSIsIlRyYWluaW5nIiwiWWVzIOKAlCB0cmFpbiBmcm9tIHNjcmF0Y2giLCJHb29kIOKAlCByZWR1Y2VzIEVDRSA0MOKAkzYwJSIsIk5ldXRyYWwgdG8gKzAuMSUiLCJTdGFuZGFyZCBkZWZhdWx0IGZvciBjbGFzc2lmaWNhdGlvbiJdLFsiVGVtcGVyYXR1cmUgc2NhbGluZyIsIlBvc3QtaG9jIG9uIGNhbGlicmF0aW9uIHNldCIsIk5vIiwiRXhjZWxsZW50IOKAlCByZWR1Y2VzIEVDRSA3MOKAkzkwJSIsIlplcm8gY2hhbmdlIiwiQmVzdCBzaW5nbGUtcGFyYW1ldGVyIHBvc3QtaG9jIG1ldGhvZCJdLFsiTWl4dXAgKM6xPTAuMikiLCJUcmFpbmluZyIsIlllcyIsIkdvb2Qg4oCUIGludGVycG9sYXRlZCB0YXJnZXRzIiwiKzAuNeKAkzEuMCUgdG9wLTEiLCJBbHNvIGltcHJvdmVzIGFjY3VyYWN5OyBzb2Z0IGJvdW5kYXJpZXMiXSxbIkRpcmljaGxldCBjYWxpYnJhdGlvbiIsIlBvc3QtaG9jIiwiTm8iLCJHb29kIOKAlCBmbGV4aWJsZSIsIlplcm8gY2hhbmdlIiwiTW9yZSBwYXJhbWV0ZXJzIHRoYW4gdGVtcCBzY2FsaW5nOyBjYW4gb3ZlcmZpdCJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgbW9zdCBwcm9kdWN0aW9uIG1vZGVscywgdGhlIHJlY29tbWVuZGVkIHN0cmF0ZWd5IGlzOiB0cmFpbiB3aXRoIGxhYmVsIHNtb290aGluZyDOtT0wLjEsIHRoZW4gYXBwbHkgdGVtcGVyYXR1cmUgc2NhbGluZyBvbiBhIGhlbGQtb3V0IGNhbGlicmF0aW9uIHNldC4gVGhpcyB0d28tc3RlcCBhcHByb2FjaCBjb21iaW5lcyB0aGUgdHJhaW5pbmctdGltZSByZWd1bGFyaXphdGlvbiBiZW5lZml0cyBvZiBsYWJlbCBzbW9vdGhpbmcgd2l0aCB0aGUgcG9zdC1ob2MgRUNFIHJlZHVjdGlvbiBvZiB0ZW1wZXJhdHVyZSBzY2FsaW5nLCBhY2hpZXZpbmcgY2FsaWJyYXRpb24gY2xvc2UgdG8gdGhlIHRoZW9yZXRpY2FsIG9wdGltdW0gd2l0aCBtaW5pbWFsIGVuZ2luZWVyaW5nIGVmZm9ydC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Label Smoothing — Soft Targets and Calibration

Hard one-hot targets [0, 0, 1, 0, ...] train the model to output log(0) for incorrect classes, pushing the logit for the correct class toward +∞ relative to others. This makes the model overconfident: at test time it assigns probabilities close to 1.0 even for difficult examples it should be uncertain about. Label smoothing (Szegedy et al. 2016, Inception V3) replaces hard targets with soft targets, capping the maximum probability the model is trained to assign and improving calibration significantly.

## Label Smoothing Formula

Label smoothing with parameter ε ∈ [0, 1) replaces: hard target yᵢ = 1 → ỹᵢ = 1 − ε, hard target yᵢ = 0 → ỹᵢ = ε/(K−1) where K is the number of classes. The smoothed cross-entropy is: CE_smooth = (1−ε) · CE(hard target) + ε · CE(uniform target) = −Σᵢ ỹᵢ · log(pᵢ). Equivalently: CE_smooth = CE(hard) − ε · (CE(hard) − H(uniform)) where H(uniform) = log(K) is a constant. The KL divergence interpretation: label smoothing minimizes KL(ỹ ‖ p) instead of KL(y ‖ p), which prevents the model from fitting the extremely peaked distribution required by hard targets.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def label_smoothing_loss(logits, targets, eps=0.1, reduction='mean'):
    n_classes = logits.size(-1)
    # Soft target: 1-eps for correct class, eps/(K-1) for others
    with torch.no_grad():
        smooth_targets = torch.full_like(logits, eps / (n_classes - 1))
        smooth_targets.scatter_(1, targets.unsqueeze(1), 1.0 - eps)
    log_probs = F.log_softmax(logits, dim=-1)
    loss = -(smooth_targets * log_probs).sum(dim=-1)
    return loss.mean() if reduction == 'mean' else loss

# Compare with PyTorch built-in
torch.manual_seed(42)
logits  = torch.randn(32, 10)
targets = torch.randint(0, 10, (32,))
eps = 0.1

loss_scratch = label_smoothing_loss(logits, targets, eps=eps)
ce_builtin   = nn.CrossEntropyLoss(label_smoothing=eps)
loss_builtin = ce_builtin(logits, targets)

print(f'Scratch label smoothing loss : {loss_scratch.item():.6f}')
print(f'PyTorch built-in LS loss     : {loss_builtin.item():.6f}')
print(f'Difference                   : {abs(loss_scratch.item()-loss_builtin.item()):.2e}')

hard_ce = nn.CrossEntropyLoss()(logits, targets)
print(f'Hard CE loss                 : {hard_ce.item():.6f}')
print(f'Label smoothing reduces loss by discouraging overconfidence.')
```

## Calibration and Overconfidence

A perfectly calibrated model satisfies: P(correct | confidence = p) = p for all p. In other words, when the model says it is 80% confident, it should be correct 80% of the time. Models trained with hard targets are systematically overconfident: they predict 95%+ confidence on samples where their actual accuracy is much lower. A reliability diagram plots model confidence (x-axis) against observed accuracy (y-axis) — a perfectly calibrated model falls on the diagonal. Models trained with label smoothing stay much closer to the diagonal.

```python
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

np.random.seed(42)
torch.manual_seed(42)
X, y = make_classification(n_samples=3000, n_features=20, n_classes=5,
                            n_informative=15, random_state=42)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.4, random_state=0)

def train_model(eps, epochs=60):
    net = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Linear(64, 5))
    opt = torch.optim.Adam(net.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss(label_smoothing=eps)
    for _ in range(epochs):
        net.train()
        loss = loss_fn(net(X_tr), y_tr)
        opt.zero_grad(); loss.backward(); opt.step()
    net.eval()
    with torch.no_grad():
        probs = F.softmax(net(X_te), dim=-1)
    return probs.numpy()

probs_hard = train_model(eps=0.0)
probs_smooth = train_model(eps=0.1)
max_conf_hard = probs_hard.max(axis=1).mean()
max_conf_smooth = probs_smooth.max(axis=1).mean()
print(f'Hard targets   — avg max confidence: {max_conf_hard:.3f}')
print(f'Label smoothing — avg max confidence: {max_conf_smooth:.3f}')
```

The output above shows that label smoothing lowers the average maximum confidence compared to hard-target training. To quantify this improvement rigorously, we compute the Expected Calibration Error (ECE), which measures the gap between predicted confidence and actual accuracy across confidence bins. A perfectly calibrated model has ECE=0.

## Expected Calibration Error

The Expected Calibration Error (ECE) quantifies miscalibration. Sort predictions by confidence and divide into M equal-width bins B₁, ..., Bₘ. For each bin: acc(Bₘ) = fraction correct in bin, conf(Bₘ) = mean confidence in bin. ECE = Σₘ (|Bₘ|/N) · |acc(Bₘ) − conf(Bₘ)|. Weighted average of confidence-accuracy gap across bins. A model with ECE=0 is perfectly calibrated. Typical ECE for ResNet-50 with hard targets on CIFAR-100: ~0.15 to 0.20. With label smoothing ε=0.1: ~0.05 to 0.08.

```python
import numpy as np

def compute_ece(probs, labels, n_bins=10):
    confidences = probs.max(axis=1)
    predictions = probs.argmax(axis=1)
    correct = (predictions == labels).astype(float)
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        mask = (confidences >= lo) & (confidences < hi)
        if mask.sum() == 0:
            continue
        bin_acc  = correct[mask].mean()
        bin_conf = confidences[mask].mean()
        ece += (mask.sum() / len(labels)) * abs(bin_acc - bin_conf)
    return ece

np.random.seed(42)
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
X, y = make_classification(n_samples=2000, n_features=20, n_classes=5,
                            n_informative=15, random_state=42)

# Simulate overconfident predictions (hard targets)
confident_probs = np.random.dirichlet([10, 1, 1, 1, 1], size=len(y))
# Simulate well-calibrated predictions (smoothed)
calibrated_probs = np.random.dirichlet([3, 1, 1, 1, 1], size=len(y))

ece_overconf = compute_ece(confident_probs, y)
ece_calibrated = compute_ece(calibrated_probs, y)
print(f'ECE (overconfident / hard targets): {ece_overconf:.4f}')
print(f'ECE (calibrated / label smoothing): {ece_calibrated:.4f}')
print('Lower ECE = better calibrated = confidence matches accuracy.')
```

> **Label Smoothing Hurts Knowledge Distillation**: When using a label-smoothed teacher to generate soft targets for student training (knowledge distillation), the smoothed softmax outputs carry less information than standard temperature-scaled probabilities. Hinton et al. recommend using a high temperature T (e.g., T=4 to T=20) without label smoothing for the teacher during distillation. Label smoothing is best applied only during the final training run of a model that will serve as an endpoint, not as a teacher.

## Temperature Scaling for Post-Hoc Calibration

Temperature scaling (Guo et al. 2017) is the simplest and most effective post-hoc calibration method. After training, learn a single scalar T > 1 that divides the logits: p̂ = softmax(z/T). T > 1 makes the distribution softer (less confident); T < 1 makes it sharper (more confident). T is fit by minimizing NLL on a held-out calibration set. This does not change accuracy (argmax is preserved) but dramatically reduces ECE — often from 0.10–0.15 to 0.01–0.03. Temperature scaling generalizes better than vector or matrix scaling methods.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class TemperatureScaling(nn.Module):
    def __init__(self):
        super().__init__()
        self.temperature = nn.Parameter(torch.ones(1) * 1.5)

    def forward(self, logits):
        return logits / self.temperature.clamp(min=0.05)

def fit_temperature(logits, labels, lr=0.01, n_steps=200):
    ts = TemperatureScaling()
    optimizer = torch.optim.LBFGS([ts.temperature], lr=lr, max_iter=n_steps)
    def closure():
        optimizer.zero_grad()
        scaled = ts(logits)
        loss = F.cross_entropy(scaled, labels)
        loss.backward()
        return loss
    optimizer.step(closure)
    return ts.temperature.item()

torch.manual_seed(42)
logits_cal = torch.randn(500, 10) * 3  # overconfident logits
labels_cal = torch.randint(0, 10, (500,))

T_opt = fit_temperature(logits_cal.clone(), labels_cal)
print(f'Optimal temperature T = {T_opt:.4f}')

probs_before = F.softmax(logits_cal, dim=-1).detach().numpy()
probs_after  = F.softmax(logits_cal / T_opt, dim=-1).detach().numpy()
print(f'Avg max confidence before scaling: {probs_before.max(axis=1).mean():.3f}')
print(f'Avg max confidence after  scaling: {probs_after.max(axis=1).mean():.3f}')
```

## When to Use Label Smoothing

Label smoothing with ε=0.1 is a reliable default for image classification, multi-class NLP tasks, and speech recognition. It helps most when: the training set has noisy labels (smoothing absorbs label noise), the model is large relative to the dataset (reduces overfitting to exact labels), and calibration quality is important for downstream decision making. Avoid label smoothing when: training a teacher model for knowledge distillation, when the task requires hard decisions (binary classification with balanced classes), or when classes genuinely have no inter-class similarity.

- ε=0.1 is the standard default from Inception V3 — works well for most classification tasks.
- ε=0.2 can help with very noisy labels but may reduce top-1 accuracy.
- Label smoothing reduces the maximum logit difference — indirectly regularizes the weight magnitude.
- Combine with mixup training: both operate on soft targets and they are complementary regularization strategies.
- Post-hoc fix: if label smoothing was not used during training, temperature scaling achieves similar calibration improvement without retraining.

## Calibration Methods Comparison

| Method | When Applied | Requires Retraining | ECE Impact | Accuracy Impact | Notes |
| --- | --- | --- | --- | --- | --- |
| Hard targets (baseline) | Training | N/A | Poor calibration (high ECE) | Reference | Model trained to be overconfident |
| Label smoothing (ε=0.1) | Training | Yes — train from scratch | Good — reduces ECE 40–60% | Neutral to +0.1% | Standard default for classification |
| Temperature scaling | Post-hoc on calibration set | No | Excellent — reduces ECE 70–90% | Zero change | Best single-parameter post-hoc method |
| Mixup (α=0.2) | Training | Yes | Good — interpolated targets | +0.5–1.0% top-1 | Also improves accuracy; soft boundaries |
| Dirichlet calibration | Post-hoc | No | Good — flexible | Zero change | More parameters than temp scaling; can overfit |

For most production models, the recommended strategy is: train with label smoothing ε=0.1, then apply temperature scaling on a held-out calibration set. This two-step approach combines the training-time regularization benefits of label smoothing with the post-hoc ECE reduction of temperature scaling, achieving calibration close to the theoretical optimum with minimal engineering effort.

---

