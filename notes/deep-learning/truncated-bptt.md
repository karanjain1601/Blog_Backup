---
title: "Truncated BPTT — Practical Approximation for Long Sequences"
slug: "truncated-bptt"
description: "Implement TBPTT(k1,k2), compare gradient quality across chunk sizes, train a character-level language model with TBPTT, and profile memory usage versus full BPTT."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRnVsbCBCUFRUIHRocm91Z2ggVD0xMDAwIHN0ZXBzIHJlcXVpcmVzIE8oVMK3SCkgbWVtb3J5IHRvIHN0b3JlIGFsbCBhY3RpdmF0aW9ucyBhbmQgcnVucyBUIHNlcXVlbnRpYWwgYmFja3dhcmQgcGFzc2VzLiBUcnVuY2F0ZWQgQlBUVCAoVEJQVFQpIGFwcHJveGltYXRlcyB0aGlzIGJ5IGxpbWl0aW5nIGJhY2twcm9wYWdhdGlvbiB0byBr4oKCIHN0ZXBzIHdoaWxlIHRoZSBmb3J3YXJkIHBhc3MgY2FuIHJ1biBr4oKBIOKJpSBr4oKCIHN0ZXBzIGJlZm9yZSBlYWNoIHVwZGF0ZS4gVGhlIG1vc3QgY29tbW9uIGZvcm0gaXMgVEJQVFQoayxrKSB3aGVyZSBrIGlzIHRoZSBjaHVuayBzaXplIOKAlCBmb3J3YXJkIGFuZCBiYWNrd2FyZCBib3RoIHNwYW4gayBzdGVwcy4gVGhlIGhpZGRlbiBzdGF0ZSBpcyBjYXJyaWVkIGJldHdlZW4gY2h1bmtzIChhbGxvd2luZyBsb25nLXJhbmdlIGluZm9ybWF0aW9uIHRvIHByb3BhZ2F0ZSBmb3J3YXJkKSBidXQgdGhlIGdyYWRpZW50IGlzIGRldGFjaGVkIChwcmV2ZW50aW5nIGdyYWRpZW50IGZsb3cgYmV5b25kIHRoZSBjdXJyZW50IGNodW5rKS4gVGhpcyBpcyB3aHkgVEJQVFQgbGVhcm5zIHNob3J0LXJhbmdlIGdyYWRpZW50cyBhY2N1cmF0ZWx5IGJ1dCBjYW5ub3QgZGlyZWN0bHkgdXBkYXRlIHdlaWdodHMgYmFzZWQgb24gZGVwZW5kZW5jaWVzIGxvbmdlciB0aGFuIGsgc3RlcHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRnVsbCBCUFRUIE1lbW9yeSBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBzZXF1ZW5jZSBvZiBsZW5ndGggVD0xMDAwLCBiYXRjaCBzaXplIEI9MzIsIGhpZGRlbiBzaXplIEg9NTEyOiBmdWxsIEJQVFQgcmVxdWlyZXMgc3RvcmluZyAxMDAww5czMsOXNTEyw5c0IGJ5dGVzIOKJiCA2NCBNQiBvZiBoaWRkZW4gc3RhdGVzIHBlciBsYXllciwgcGx1cyBtYXRjaGluZyBidWZmZXJzIGZvciB0YW5oIGlucHV0cy4gV2l0aCBtdWx0aXBsZSBsYXllcnMsIHRoZSBtZW1vcnkgcmVxdWlyZW1lbnQgZ3Jvd3MgcHJvcG9ydGlvbmFsbHkuIE1vcmUgY3JpdGljYWxseSwgdGhlIGJhY2t3YXJkIGdyYXBoIGNvbnRhaW5zIFTDl0jDl0gg4omIIDI2MiBtaWxsaW9uIG5vZGVzLCBtYWtpbmcgZWFjaCBzdGVwIG9mIHRoZSBiYWNrd2FyZCBwYXNzIHNsb3cuIEdyYWRpZW50IGNoZWNrcG9pbnRpbmcgY2FuIGhhbHZlIHRoZSBtZW1vcnkgcmVxdWlyZW1lbnQgYXQgNTAlIGV4dHJhIGNvbXB1dGUgY29zdCwgYnV0IFRCUFRUIHJlbWFpbnMgdGhlIHN0YW5kYXJkIGZvciBSTk4gdHJhaW5pbmcgYmVjYXVzZSBpdCBpcyBzaW1wbGVyIGFuZCBtb3JlIHByZWRpY3RhYmxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRCUFRUKGvigoEsa+KCgikgRm9ybXVsYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRCUFRUKGvigoEsa+KCgikgZ2VuZXJhbGlzZXMgdGhlIGNvbW1vbiBjaHVua2VkIGZvcm06IGvigoEgaXMgdGhlIGZvcndhcmQgc3RyaWRlIChob3cgbWFueSBzdGVwcyB0byBhZHZhbmNlIGJlZm9yZSBlYWNoIHVwZGF0ZSkgYW5kIGvigoIgaXMgdGhlIGJhY2twcm9wYWdhdGlvbiBkZXB0aCAoa+KCgiDiiaQga+KCgSkuIFdoZW4ga+KCgSBcdTAwM2Uga+KCgiwgdGhlIGZpcnN0IGvigoEta+KCgiBzdGVwcyBvZiBlYWNoIHN0cmlkZSBhcmUgcnVuIHdpdGhvdXQgZ3JhZGllbnQgdHJhY2tpbmcsIHRoZW4gZ3JhZGllbnQgaXMgdHJhY2tlZCBmb3IgdGhlIGxhc3Qga+KCgiBzdGVwcy4gTW9zdCBpbXBsZW1lbnRhdGlvbnMgdXNlIGvigoEgPSBr4oKCID0gY2h1bmtfc2l6ZSAoUGVubiBUcmVlYmFuayB1c2VzIDM1LCB3b3JkLWxldmVsIG1vZGVscyBvZnRlbiAxMjjigJMyNTYpLiBUaGUgZGV0YWNoZWQgaGlkZGVuIHN0YXRlIGguZGV0YWNoKCkgY2FycmllcyBmb3J3YXJkLXBhc3MgaW5mb3JtYXRpb24gKGxldHRpbmcgdGhlIG1vZGVsIGNvbmRpdGlvbiBvbiBkaXN0YW50IGhpc3RvcnkpIHdpdGhvdXQgY3JlYXRpbmcgZ3JhZGllbnQgcGF0aHMgaW50byB0aG9zZSBkaXN0YW50IHN0ZXBzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuVCwgQiwgSSwgSCwgTyA9IDIwMCwgOCwgMTYsIDY0LCA4XG5rMSwgazIgPSAxMDAsIDIwICAjIGZvcndhcmQgazEgc3RlcHMsIGJhY2twcm9wIHRocm91Z2ggazIgc3RlcHMgKGsyIFx1MDAzYyBrMSlcblxucm5uID0gbm4uUk5OKEksIEgsIGJhdGNoX2ZpcnN0PVRydWUpXG5mYyAgPSBubi5MaW5lYXIoSCwgTylcbm9wdCA9IHRvcmNoLm9wdGltLkFkYW0obGlzdChybm4ucGFyYW1ldGVycygpKSArIGxpc3QoZmMucGFyYW1ldGVycygpKSwgbHI9M2UtNClcbnggICA9IHRvcmNoLnJhbmRuKEIsIFQsIEkpXG55ICAgPSB0b3JjaC5yYW5kbihCLCBULCBPKVxuXG5oID0gdG9yY2guemVyb3MoMSwgQiwgSClcbnRvdGFsX2xvc3MsIG5fdXBkYXRlcyA9IDAuMCwgMFxuXG5mb3Igc3RhcnQgaW4gcmFuZ2UoMCwgVCAtIGsyLCBrMSk6XG4gICAgIyBSdW4gazEgLSBrMiBzdGVwcyBmb3J3YXJkIHdpdGhvdXQgZ3JhZGllbnQgdG8gYWR2YW5jZSBoaWRkZW4gc3RhdGVcbiAgICBub19ncmFkX2VuZCA9IG1pbihzdGFydCArIGsxIC0gazIsIFQpXG4gICAgaWYgbm9fZ3JhZF9lbmQgXHUwMDNlIHN0YXJ0OlxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIF8sIGggPSBybm4oeFs6LCBzdGFydDpub19ncmFkX2VuZCwgOl0sIGgpXG4gICAgICAgIGggPSBoLmRldGFjaCgpXG4gICAgIyBCYWNrcHJvcCB0aHJvdWdoIG9ubHkgdGhlIGxhc3QgazIgc3RlcHNcbiAgICBid2Rfc3RhcnQgPSBtaW4oc3RhcnQgKyBrMSAtIGsyLCBUIC0gazIpXG4gICAgYndkX2VuZCAgID0gbWluKGJ3ZF9zdGFydCArIGsyLCBUKVxuICAgIG9wdC56ZXJvX2dyYWQoKVxuICAgIG91dCwgaF9uZXcgPSBybm4oeFs6LCBid2Rfc3RhcnQ6YndkX2VuZCwgOl0sIGguZGV0YWNoKCkpXG4gICAgbG9zcyA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MoZmMob3V0KSwgeVs6LCBid2Rfc3RhcnQ6YndkX2VuZCwgOl0pXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgdG9yY2gubm4udXRpbHMuY2xpcF9ncmFkX25vcm1fKHJubi5wYXJhbWV0ZXJzKCksIDEuMClcbiAgICBvcHQuc3RlcCgpXG4gICAgaCA9IGhfbmV3LmRldGFjaCgpXG4gICAgdG90YWxfbG9zcyArPSBsb3NzLml0ZW0oKTsgbl91cGRhdGVzICs9IDFcblxucHJpbnQoZlx1MDAyN1RCUFRUKGsxPXtrMX0sIGsyPXtrMn0pIG92ZXIgVD17VH1cdTAwMjcpXG5wcmludChmXHUwMDI3VXBkYXRlczoge25fdXBkYXRlc30sIGF2ZyBsb3NzOiB7dG90YWxfbG9zcyAvIG1heChuX3VwZGF0ZXMsIDEpOi42Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3R3JhZGllbnQgZmxvd3Mgb25seSB0aHJvdWdoIGxhc3QgazI9e2syfSBzdGVwcyBwZXIgdXBkYXRlLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcmFkaWVudCBRdWFsaXR5IHZzIENodW5rIFNpemUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFzIGNodW5rIHNpemUga+KCgiBpbmNyZWFzZXMsIHRoZSBUQlBUVCBncmFkaWVudCBiZWNvbWVzIGEgYmV0dGVyIGFwcHJveGltYXRpb24gb2YgdGhlIGZ1bGwgQlBUVCBncmFkaWVudC4gVGhlIGNvc2luZSBzaW1pbGFyaXR5IGJldHdlZW4gdGhlIHRydW5jYXRlZCBhbmQgZnVsbCBncmFkaWVudCB2ZWN0b3JzIG1lYXN1cmVzIGdyYWRpZW50IGRpcmVjdGlvbiBxdWFsaXR5LiBGb3IgZGVwZW5kZW5jaWVzIHRoYXQgZGVjYXkgZXhwb25lbnRpYWxseSAoYXMgd2l0aCBhIHdlbGwtYmVoYXZlZCBSTk4pLCBr4oKCPTIwIG1heSBjYXB0dXJlIDkwJSsgb2YgdGhlIHVzZWZ1bCBncmFkaWVudCBzaWduYWwuIEZvciB0YXNrcyB3aXRoIGxvbmctcmFuZ2UgZGVwZW5kZW5jaWVzIChlLmcuLCBtYXRjaGluZyBwYXJlbnRoZXNlcyA1MCBzdGVwcyBhcGFydCksIHNtYWxsIGvigoIgd2lsbCBmYWlsIHRvIGxlYXJuIHRoZSB0YXNrLiBUaGUgcHJhY3RpY2FsIHJ1bGU6IGvigoIgc2hvdWxkIGJlIGF0IGxlYXN0IGFzIGxhcmdlIGFzIHRoZSBsb25nZXN0IGRlcGVuZGVuY3kgeW91IG5lZWQgdG8gbGVhcm4uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5ucC5yYW5kb20uc2VlZCg3KVxuVCwgSSwgSCA9IDYwLCA0LCA4XG5XaGhfc2NhbGUgPSAwLjUgICMgc3RhYmxlIHZhbmlzaGluZyByZWdpbWVcblxuV3hoID0gbnAucmFuZG9tLnJhbmRuKEgsIEkpICogMC4xXG5XaGggPSBucC5yYW5kb20ucmFuZG4oSCwgSCkgKiBXaGhfc2NhbGUgLyBucC5zcXJ0KEgpXG5iaCAgPSBucC56ZXJvcygoSCwgMSkpXG54cyAgPSBbbnAucmFuZG9tLnJhbmRuKEksIDEpIGZvciBfIGluIHJhbmdlKFQpXVxuXG5kZWYgZm9yd2FyZF9jaHVuayh4c19saXN0LCBoMCk6XG4gICAgaHMgPSB7LTE6IGgwfVxuICAgIGZvciB0LCB4IGluIGVudW1lcmF0ZSh4c19saXN0KTpcbiAgICAgICAgaHNbdF0gPSBucC50YW5oKFd4aCBAIHggKyBXaGggQCBoc1t0LTFdICsgYmgpXG4gICAgcmV0dXJuIGhzXG5cbmRlZiBncmFkX1doaCh4c19saXN0LCBocywgV2hoKTpcbiAgICBkaCA9IG5wLm9uZXMoKEgsIDEpKSAvIEg7IGRXID0gbnAuemVyb3NfbGlrZShXaGgpXG4gICAgZm9yIHQgaW4gcmV2ZXJzZWQocmFuZ2UobGVuKHhzX2xpc3QpKSk6XG4gICAgICAgIGR0ID0gKDEgLSBoc1t0XSoqMikgKiBkaFxuICAgICAgICBkVyArPSBkdCBAIGhzW3QtMV0uVDsgZGggPSBXaGguVCBAIGR0XG4gICAgcmV0dXJuIGRXXG5cbiMgRnVsbCBCUFRUIHJlZmVyZW5jZSBncmFkaWVudFxuaHNfZnVsbCA9IGZvcndhcmRfY2h1bmsoeHMsIG5wLnplcm9zKChILCAxKSkpXG5kV19yZWYgID0gZ3JhZF9XaGgoeHMsIGhzX2Z1bGwsIFdoaClcblxucHJpbnQoZlx1MDAyN0NodW5rICBDb3NpbmUgU2ltaWxhcml0eSAgZFdoaCBOb3JtICBOb3RlXHUwMDI3KVxuZm9yIGNodW5rIGluIFs1LCAxMCwgMjAsIDQwLCA2MF06XG4gICAgZFdfdGJwdHQgPSBucC56ZXJvc19saWtlKFdoaCk7IGhfY2FycnkgPSBucC56ZXJvcygoSCwgMSkpXG4gICAgZm9yIHMgaW4gcmFuZ2UoMCwgVCwgY2h1bmspOlxuICAgICAgICB4YyA9IHhzW3M6cyArIGNodW5rXVxuICAgICAgICBoYyA9IGZvcndhcmRfY2h1bmsoeGMsIGhfY2FycnkpXG4gICAgICAgIGRXX3RicHR0ICs9IGdyYWRfV2hoKHhjLCBoYywgV2hoKVxuICAgICAgICBoX2NhcnJ5ID0gaGNbbGVuKHhjKSAtIDFdLmNvcHkoKVxuICAgIGNvcyA9IChucC5kb3QoZFdfcmVmLnJhdmVsKCksIGRXX3RicHR0LnJhdmVsKCkpIC9cbiAgICAgICAgICAgKG5wLmxpbmFsZy5ub3JtKGRXX3JlZikgKiBucC5saW5hbGcubm9ybShkV190YnB0dCkgKyAxZS05KSlcbiAgICBub3RlID0gXHUwMDI3IChmdWxsIEJQVFQpXHUwMDI3IGlmIGNodW5rID09IFQgZWxzZSBcdTAwMjdcdTAwMjdcbiAgICBwcmludChmXHUwMDI3e2NodW5rOlx1MDAzZTV9ICB7Y29zOlx1MDAzZTE4LjZmfSAge25wLmxpbmFsZy5ub3JtKGRXX3RicHR0KTpcdTAwM2U5LjRmfXtub3RlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYW5ndWFnZSBNb2RlbCBUcmFpbmluZyB3aXRoIFRCUFRUIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDaGFyYWN0ZXItbGV2ZWwgbGFuZ3VhZ2UgbW9kZWxzIGFyZSB0cmFpbmVkIGJ5IHByZWRpY3RpbmcgdGhlIG5leHQgY2hhcmFjdGVyIGdpdmVuIGFsbCBwcmV2aW91cyBjaGFyYWN0ZXJzLiBUaGUgc3RhbmRhcmQgVEJQVFQgaW1wbGVtZW50YXRpb246ICgxKSB0b2tlbmlzZSB0ZXh0IGludG8gaW50ZWdlcnMsICgyKSBjaHVuayB0aGUgdG9rZW4gc2VxdWVuY2UgaW50byBibG9ja3Mgb2Ygc2l6ZSBrLCAoMykgZm9yIGVhY2ggYmxvY2sgcnVuIGEgZm9yd2FyZCBwYXNzIGFuZCBiYWNrd2FyZCBwYXNzLCAoNCkgY2FycnkgdGhlIGhpZGRlbiBzdGF0ZSBiZXR3ZWVuIGJsb2NrcyB3aXRoIGguZGV0YWNoKCkuIFRoaXMgaXMgdGhlIGV4YWN0IHNldHVwIHVzZWQgaW4gTWlrb2xvdiAoMjAxMCkgYW5kIEthcnBhdGh5XHUwMDI3cyBjaGFyLXJubi4gQ2h1bmsgc2l6ZSAzNSBtYXRjaGVzIHRoZSBQZW5uIFRyZWViYW5rIGJlbmNobWFyazsgbW9kZXJuIGltcGxlbWVudGF0aW9ucyBvZnRlbiB1c2UgMTI44oCTMjU2LiBMb3NzIGlzIGNyb3NzLWVudHJvcHkgb3ZlciB0aGUgdm9jYWJ1bGFyeTsgcGVycGxleGl0eSA9IGV4cChjcm9zcy1lbnRyb3B5KSBpcyB0aGUgc3RhbmRhcmQgZXZhbHVhdGlvbiBtZXRyaWMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxudGV4dCAgPSBcdTAwMjd0aGUgcXVpY2sgYnJvd24gZm94IGp1bXBzIG92ZXIgdGhlIGxhenkgZG9nIFx1MDAyNyAqIDQwXG5jaGFycyA9IHNvcnRlZChzZXQodGV4dCkpXG5jMmkgICA9IHtjOiBpIGZvciBpLCBjIGluIGVudW1lcmF0ZShjaGFycyl9XG52b2NhYiA9IGxlbihjaGFycylcbmRhdGEgID0gdG9yY2gudGVuc29yKFtjMmlbY10gZm9yIGMgaW4gdGV4dF0sIGR0eXBlPXRvcmNoLmxvbmcpXG5UX2RhdGEsIGNodW5rLCBILCBCID0gbGVuKGRhdGEpIC0gMSwgMzUsIDY0LCAxXG5cbmVtYiA9IG5uLkVtYmVkZGluZyh2b2NhYiwgSClcbnJubiA9IG5uLlJOTihILCBILCBiYXRjaF9maXJzdD1UcnVlKVxuZmMgID0gbm4uTGluZWFyKEgsIHZvY2FiKVxucGFyYW1zID0gbGlzdChlbWIucGFyYW1ldGVycygpKSArIGxpc3Qocm5uLnBhcmFtZXRlcnMoKSkgKyBsaXN0KGZjLnBhcmFtZXRlcnMoKSlcbm9wdCAgICA9IHRvcmNoLm9wdGltLkFkYW0ocGFyYW1zLCBscj0xZS0zKVxuaCA9IHRvcmNoLnplcm9zKDEsIEIsIEgpXG50b3RhbF9sb3NzLCBuX3N0ZXBzID0gMC4wLCAwXG5cbmZvciBzdGFydCBpbiByYW5nZSgwLCBUX2RhdGEgLSBjaHVuaywgY2h1bmspOlxuICAgIHhjID0gZGF0YVtzdGFydDpzdGFydCArIGNodW5rXS51bnNxdWVlemUoMCkgICAgICAgICAgIyAoMSwgY2h1bmspXG4gICAgeWMgPSBkYXRhW3N0YXJ0ICsgMTpzdGFydCArIGNodW5rICsgMV0udW5zcXVlZXplKDApICAjICgxLCBjaHVuaylcbiAgICBoICA9IGguZGV0YWNoKClcbiAgICBlbWJlZF94YyAgICA9IGVtYih4YykgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKDEsIGNodW5rLCBIKVxuICAgIGhpZGRlbl9vdXQsIGggPSBybm4oZW1iZWRfeGMsIGgpICAgICAgICAgICAgICAgICAgICAgIyAoMSwgY2h1bmssIEgpXG4gICAgbG9naXRzICAgICAgPSBmYyhoaWRkZW5fb3V0KS52aWV3KC0xLCB2b2NhYikgICAgICAgICAjIChjaHVuaywgdm9jYWIpXG4gICAgbG9zcyAgICAgICAgPSBubi5mdW5jdGlvbmFsLmNyb3NzX2VudHJvcHkobG9naXRzLCB5Yy52aWV3KC0xKSlcbiAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKVxuICAgIHRvcmNoLm5uLnV0aWxzLmNsaXBfZ3JhZF9ub3JtXyhybm4ucGFyYW1ldGVycygpLCA1LjApXG4gICAgb3B0LnN0ZXAoKVxuICAgIHRvdGFsX2xvc3MgKz0gbG9zcy5pdGVtKCk7IG5fc3RlcHMgKz0gMVxuXG5hdmdfY2UgPSB0b3RhbF9sb3NzIC8gbl9zdGVwc1xucHJpbnQoZlx1MDAyN0NoYXIgTE06IHZvY2FiPXt2b2NhYn0sIGNodW5rPXtjaHVua30gKFBUQi1zdHlsZSBUQlBUVClcdTAwMjcpXG5wcmludChmXHUwMDI3U3RlcHM6IHtuX3N0ZXBzfSwgYXZnIGNyb3NzLWVudHJvcHk6IHthdmdfY2U6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdQZXJwbGV4aXR5OiB7dG9yY2guZXhwKHRvcmNoLnRlbnNvcihhdmdfY2UpKS5pdGVtKCk6LjJmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcnkgUHJvZmlsaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbWVtb3J5IGFkdmFudGFnZSBvZiBUQlBUVCBvdmVyIGZ1bGwgQlBUVCBzY2FsZXMgbGluZWFybHkgd2l0aCBUL2suIEZvciBUPTEwMDAgYW5kIGs9MzUsIFRCUFRUIHN0b3JlcyAyOHggZmV3ZXIgaGlkZGVuIHN0YXRlIHRlbnNvcnMuIFByb2ZpbGluZyB3aXRoIHRvcmNoLmN1ZGEubWVtb3J5X2FsbG9jYXRlZCgpIG9yIHRyYWNlbWFsbG9jIGNvbmZpcm1zIHRoaXMgdGhlb3JldGljYWwgcmF0aW8uIFRoZSBhdXRvZ3JhZCBncmFwaCBkZXB0aCBpcyBhbHNvIHByb3BvcnRpb25hbCB0byB0aGUgY2h1bmsgc2l6ZSwgd2hpY2ggYWZmZWN0cyBiYWNrd2FyZCBwYXNzIHRpbWUuIExhcmdlciBjaHVua3MgZ2l2ZSBiZXR0ZXIgZ3JhZGllbnQgcXVhbGl0eSBhdCB0aGUgY29zdCBvZiBtb3JlIG1lbW9yeSBhbmQgc2xvd2VyIGJhY2t3YXJkIHBhc3NlcyDigJQgdGhlIGZ1bmRhbWVudGFsIHRyYWRlLW9mZiBpbiBjaHVuayBzaXplIHNlbGVjdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxudG9yY2gubWFudWFsX3NlZWQoMSlcbkksIEgsIEIgPSAxNiwgNjQsIDRcbnJubiA9IG5uLlJOTihJLCBILCBiYXRjaF9maXJzdD1UcnVlKVxuXG5kZWYgY291bnRfZ3JhcGhfbm9kZXMobG9zc190ZW5zb3IpOlxuICAgIHZpc2l0ZWQsIHN0YWNrID0gc2V0KCksIFtsb3NzX3RlbnNvci5ncmFkX2ZuXVxuICAgIHdoaWxlIHN0YWNrOlxuICAgICAgICBuID0gc3RhY2sucG9wKClcbiAgICAgICAgaWYgbiBpcyBOb25lIG9yIGlkKG4pIGluIHZpc2l0ZWQ6XG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICB2aXNpdGVkLmFkZChpZChuKSlcbiAgICAgICAgc3RhY2suZXh0ZW5kKGMgZm9yIGMsIF8gaW4gKG4ubmV4dF9mdW5jdGlvbnMgb3IgW10pKVxuICAgIHJldHVybiBsZW4odmlzaXRlZClcblxucHJpbnQoZlx1MDAyN3tcIlRcIjpcdTAwM2U2fSB7XCJDaHVua1wiOlx1MDAzZTd9IHtcIk1ldGhvZFwiOlx1MDAzYzIwfSB7XCJBY3QuIE1lbSBNQlwiOlx1MDAzZTEyfSB7XCJHcmFwaCBub2Rlc1wiOlx1MDAzZTEyfVx1MDAyNylcbmJ5dGVzX3Blcl9mbG9hdCA9IDRcbmZvciBUIGluIFs1MCwgMTAwLCAyMDBdOlxuICAgIHggPSB0b3JjaC5yYW5kbihCLCBULCBJKVxuICAgIG91dF9mdWxsLCBfID0gcm5uKHgsIHRvcmNoLnplcm9zKDEsIEIsIEgpKVxuICAgIG5vZGVzX2Z1bGwgID0gY291bnRfZ3JhcGhfbm9kZXMob3V0X2Z1bGwuc3VtKCkpXG4gICAgZnVsbF9tYiAgICAgPSBUICogSCAqIEIgKiBieXRlc19wZXJfZmxvYXQgLyAxZTZcbiAgICBwcmludChmXHUwMDI3e1Q6XHUwMDNlNn0ge1Q6XHUwMDNlN30ge1wiRnVsbCBCUFRUXCI6XHUwMDNjMjB9IHtmdWxsX21iOlx1MDAzZTEyLjRmfSB7bm9kZXNfZnVsbDpcdTAwM2UxMn1cdTAwMjcpXG4gICAgZm9yIGNodW5rIGluIFsxMCwgMjVdOlxuICAgICAgICBpZiBjaHVuayBcdTAwM2U9IFQ6XG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICBvdXRfYywgXyA9IHJubih4WzosIDpjaHVuaywgOl0sIHRvcmNoLnplcm9zKDEsIEIsIEgpKVxuICAgICAgICBub2Rlc19jICA9IGNvdW50X2dyYXBoX25vZGVzKG91dF9jLnN1bSgpKVxuICAgICAgICBtYl9jICAgICA9IGNodW5rICogSCAqIEIgKiBieXRlc19wZXJfZmxvYXQgLyAxZTZcbiAgICAgICAgcmF0aW8gICAgPSBmdWxsX21iIC8gbWJfY1xuICAgICAgICBwcmludChmXHUwMDI3e1Q6XHUwMDNlNn0ge2NodW5rOlx1MDAzZTd9IHtmXCJUQlBUVCBrPXtjaHVua31cIjpcdTAwM2MyMH0ge21iX2M6XHUwMDNlMTIuNGZ9IFx1MDAyN1xuICAgICAgICAgICAgICBmXHUwMDI3e25vZGVzX2M6XHUwMDNlMTJ9ICAoe3JhdGlvOi4xZn14IGxlc3MgbWVtKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgQ2h1bmsgU2l6ZSBTZWxlY3Rpb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQ2h1bmsgU2l6ZSIsIkdyYWRpZW50IFF1YWxpdHkiLCJNZW1vcnkgcGVyIENodW5rIiwiRGVwZW5kZW5jaWVzIENhcHR1cmVkIiwiVHlwaWNhbCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyIxMCIsIlBvb3Ig4oCUIHZlcnkgbG9jYWwgZ3JhZGllbnQgb25seSIsIlZlcnkgbG93IOKAlCBPKDEwwrdIwrdCKSIsIlVwIHRvIDEwIHN0ZXBzIiwiU2ltcGxlIHBhdHRlcm4gcmVwZXRpdGlvbiwgc2hvcnQtbGFnIHRhc2tzIl0sWyIzNSIsIk1vZGVyYXRlIOKAlCBQVEIgc3RhbmRhcmQiLCJMb3cg4oCUIE8oMzXCt0jCt0IpIiwiVXAgdG8gMzUgc3RlcHMiLCJDaGFyYWN0ZXItbGV2ZWwgTE0sIFBlbm4gVHJlZWJhbmsgd29yZC1sZXZlbCBMTSJdLFsiMTAwIiwiR29vZCDigJQgY2FwdHVyZXMgbWVkaXVtLXJhbmdlIHBhdHRlcm5zIiwiTW9kZXJhdGUg4oCUIE8oMTAwwrdIwrdCKSIsIlVwIHRvIDEwMCBzdGVwcyIsIldvcmQtbGV2ZWwgTE0sIG1hY2hpbmUgdHJhbnNsYXRpb24gc2VxdWVuY2VzIl0sWyIyNTYiLCJOZWFyLWZ1bGwgQlBUVCBxdWFsaXR5IiwiSGlnaCDigJQgTygyNTbCt0jCt0IpIiwiVXAgdG8gMjU2IHN0ZXBzIiwiTG9uZyBkb2N1bWVudHMsIG1vZGVybiBMU1RNL0dSVSB0cmFpbmluZyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhZGUtb2ZmcyBhbmQgTGltaXRhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRCUFRUIGludHJvZHVjZXMgYSBzeXN0ZW1hdGljIGJpYXM6IHdlaWdodHMgYXJlIHVwZGF0ZWQgYmFzZWQgb24gbG9jYWwgZ3JhZGllbnQgc2lnbmFscyBvbmx5LCBzbyBsb25nLXJhbmdlIHBhdHRlcm5zIGFyZSBsZWFybmVkIGluZGlyZWN0bHkgKHZpYSB0aGUgaGlkZGVuIHN0YXRlIGNhcnJ5aW5nIGluZm9ybWF0aW9uIGZvcndhcmQpIHJhdGhlciB0aGFuIGRpcmVjdGx5IHZpYSBncmFkaWVudC4gRm9yIHRhc2tzIHdpdGggZGVwZW5kZW5jaWVzIHNob3J0ZXIgdGhhbiBrLCBUQlBUVCBpcyBhcyBnb29kIGFzIGZ1bGwgQlBUVC4gRm9yIHRhc2tzIHdoZXJlIHRoZSBjcml0aWNhbCBzaWduYWwgYXJyaXZlcyBcdTAwM2VrIHN0ZXBzIGJlZm9yZSB0aGUgb3V0cHV0LCBUQlBUVCBtYXkgZmFpbCB0byBsZWFybiBldmVuIGlmIHRoZSBoaWRkZW4gc3RhdGUgY29udGFpbnMgdGhlIGluZm9ybWF0aW9uIOKAlCBiZWNhdXNlIHRoZSBncmFkaWVudCBjYW5ub3QgY3JlZGl0LWFzc2lnbiBiYWNrIHRvIHdoZXJlIHRoZSBpbmZvcm1hdGlvbiB3YXMgZW5jb2RlZC4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiUnVsZSBvZiBUaHVtYiBmb3IgQ2h1bmsgU2l6ZSIsImNvbnRlbnQiOiJTZXQgY2h1bmsgc2l6ZSB0byBhdCBsZWFzdCAy4oCTM3ggdGhlIGxvbmdlc3QgZGVwZW5kZW5jeSB5b3UgbmVlZCB0byBsZWFybi4gSWYgeW91XHUwMDI3cmUgdW5zdXJlLCBwcm9maWxlIGdyYWRpZW50IGNvc2luZSBzaW1pbGFyaXR5IGJldHdlZW4gVEJQVFQgYW5kIGEgc2hvcnQgZnVsbC1CUFRUIHJ1biBvbiBhIHNtYWxsIG1vZGVsLiBVc2UgZ3JhZGllbnQgY2hlY2twb2ludGluZyBpZiB5b3Ugd2FudCBmdWxsIEJQVFQgcXVhbGl0eSB3aXRoIGFjY2VwdGFibGUgbWVtb3J5OiBzdG9yZSBldmVyeSBzcXJ0KFQpIGhpZGRlbiBzdGF0ZSBhbmQgcmVjb21wdXRlIHRoZSByZXN0IGR1cmluZyBiYWNrd2FyZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRCUFRUKGssayk6IG1vc3QgY29tbW9uIGZvcm0g4oCUIGZvcndhcmQgYW5kIGJhY2t3YXJkIGJvdGggc3BhbiBrIHN0ZXBzIHBlciBjaHVuay4iLCJUQlBUVChrMSxrMikgd2l0aCBrMVx1MDAzZWsyOiBydW4gazEgc3RlcHMgYmVmb3JlIGVhY2ggdXBkYXRlOyBiYWNrcHJvcCBvbmx5IGsyIHN0ZXBzIGJhY2suIiwiQ2FycnkgaC5kZXRhY2goKSBmb3J3YXJkOiBoaWRkZW4gc3RhdGUgY2FycmllcyBsb25nLXJhbmdlIGluZm87IGdyYWRpZW50IGlzIGxvY2FsIG9ubHkuIiwiQ2h1bmsgc2l6ZSAzNTogUFRCIGxhbmd1YWdlIG1vZGVsIGJlbmNobWFyayBzdGFuZGFyZCBzaW5jZSBNaWtvbG92ICgyMDEwKS4iLCJHcmFkaWVudCBjbGlwcGluZyAobWF4X25vcm09MS01KTogbWFuZGF0b3J5IGFsb25nc2lkZSBUQlBUVCB0byBwcmV2ZW50IGV4cGxvc2lvbnMuIiwiR3JhZGllbnQgcXVhbGl0eSBtb25pdG9yaW5nOiBtZWFzdXJlIGNvc2luZSBzaW1pbGFyaXR5IG9mIFRCUFRUIHZzIGZ1bGwgQlBUVCBvbiBhIHNtYWxsIGhlbGQtb3V0IHRhc2suIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Truncated BPTT — Practical Approximation for Long Sequences

Full BPTT through T=1000 steps requires O(T·H) memory to store all activations and runs T sequential backward passes. Truncated BPTT (TBPTT) approximates this by limiting backpropagation to k₂ steps while the forward pass can run k₁ ≥ k₂ steps before each update. The most common form is TBPTT(k,k) where k is the chunk size — forward and backward both span k steps. The hidden state is carried between chunks (allowing long-range information to propagate forward) but the gradient is detached (preventing gradient flow beyond the current chunk). This is why TBPTT learns short-range gradients accurately but cannot directly update weights based on dependencies longer than k steps.

## Full BPTT Memory Problem

For a sequence of length T=1000, batch size B=32, hidden size H=512: full BPTT requires storing 1000×32×512×4 bytes ≈ 64 MB of hidden states per layer, plus matching buffers for tanh inputs. With multiple layers, the memory requirement grows proportionally. More critically, the backward graph contains T×H×H ≈ 262 million nodes, making each step of the backward pass slow. Gradient checkpointing can halve the memory requirement at 50% extra compute cost, but TBPTT remains the standard for RNN training because it is simpler and more predictable.

## TBPTT(k₁,k₂) Formulation

TBPTT(k₁,k₂) generalises the common chunked form: k₁ is the forward stride (how many steps to advance before each update) and k₂ is the backpropagation depth (k₂ ≤ k₁). When k₁ > k₂, the first k₁-k₂ steps of each stride are run without gradient tracking, then gradient is tracked for the last k₂ steps. Most implementations use k₁ = k₂ = chunk_size (Penn Treebank uses 35, word-level models often 128–256). The detached hidden state h.detach() carries forward-pass information (letting the model condition on distant history) without creating gradient paths into those distant steps.

```python
import torch
import torch.nn as nn

torch.manual_seed(0)
T, B, I, H, O = 200, 8, 16, 64, 8
k1, k2 = 100, 20  # forward k1 steps, backprop through k2 steps (k2 < k1)

rnn = nn.RNN(I, H, batch_first=True)
fc  = nn.Linear(H, O)
opt = torch.optim.Adam(list(rnn.parameters()) + list(fc.parameters()), lr=3e-4)
x   = torch.randn(B, T, I)
y   = torch.randn(B, T, O)

h = torch.zeros(1, B, H)
total_loss, n_updates = 0.0, 0

for start in range(0, T - k2, k1):
    # Run k1 - k2 steps forward without gradient to advance hidden state
    no_grad_end = min(start + k1 - k2, T)
    if no_grad_end > start:
        with torch.no_grad():
            _, h = rnn(x[:, start:no_grad_end, :], h)
        h = h.detach()
    # Backprop through only the last k2 steps
    bwd_start = min(start + k1 - k2, T - k2)
    bwd_end   = min(bwd_start + k2, T)
    opt.zero_grad()
    out, h_new = rnn(x[:, bwd_start:bwd_end, :], h.detach())
    loss = nn.functional.mse_loss(fc(out), y[:, bwd_start:bwd_end, :])
    loss.backward()
    torch.nn.utils.clip_grad_norm_(rnn.parameters(), 1.0)
    opt.step()
    h = h_new.detach()
    total_loss += loss.item(); n_updates += 1

print(f'TBPTT(k1={k1}, k2={k2}) over T={T}')
print(f'Updates: {n_updates}, avg loss: {total_loss / max(n_updates, 1):.6f}')
print(f'Gradient flows only through last k2={k2} steps per update.')
```

## Gradient Quality vs Chunk Size

As chunk size k₂ increases, the TBPTT gradient becomes a better approximation of the full BPTT gradient. The cosine similarity between the truncated and full gradient vectors measures gradient direction quality. For dependencies that decay exponentially (as with a well-behaved RNN), k₂=20 may capture 90%+ of the useful gradient signal. For tasks with long-range dependencies (e.g., matching parentheses 50 steps apart), small k₂ will fail to learn the task. The practical rule: k₂ should be at least as large as the longest dependency you need to learn.

```python
import numpy as np

np.random.seed(7)
T, I, H = 60, 4, 8
Whh_scale = 0.5  # stable vanishing regime

Wxh = np.random.randn(H, I) * 0.1
Whh = np.random.randn(H, H) * Whh_scale / np.sqrt(H)
bh  = np.zeros((H, 1))
xs  = [np.random.randn(I, 1) for _ in range(T)]

def forward_chunk(xs_list, h0):
    hs = {-1: h0}
    for t, x in enumerate(xs_list):
        hs[t] = np.tanh(Wxh @ x + Whh @ hs[t-1] + bh)
    return hs

def grad_Whh(xs_list, hs, Whh):
    dh = np.ones((H, 1)) / H; dW = np.zeros_like(Whh)
    for t in reversed(range(len(xs_list))):
        dt = (1 - hs[t]**2) * dh
        dW += dt @ hs[t-1].T; dh = Whh.T @ dt
    return dW

# Full BPTT reference gradient
hs_full = forward_chunk(xs, np.zeros((H, 1)))
dW_ref  = grad_Whh(xs, hs_full, Whh)

print(f'Chunk  Cosine Similarity  dWhh Norm  Note')
for chunk in [5, 10, 20, 40, 60]:
    dW_tbptt = np.zeros_like(Whh); h_carry = np.zeros((H, 1))
    for s in range(0, T, chunk):
        xc = xs[s:s + chunk]
        hc = forward_chunk(xc, h_carry)
        dW_tbptt += grad_Whh(xc, hc, Whh)
        h_carry = hc[len(xc) - 1].copy()
    cos = (np.dot(dW_ref.ravel(), dW_tbptt.ravel()) /
           (np.linalg.norm(dW_ref) * np.linalg.norm(dW_tbptt) + 1e-9))
    note = ' (full BPTT)' if chunk == T else ''
    print(f'{chunk:>5}  {cos:>18.6f}  {np.linalg.norm(dW_tbptt):>9.4f}{note}')
```

## Language Model Training with TBPTT

Character-level language models are trained by predicting the next character given all previous characters. The standard TBPTT implementation: (1) tokenise text into integers, (2) chunk the token sequence into blocks of size k, (3) for each block run a forward pass and backward pass, (4) carry the hidden state between blocks with h.detach(). This is the exact setup used in Mikolov (2010) and Karpathy's char-rnn. Chunk size 35 matches the Penn Treebank benchmark; modern implementations often use 128–256. Loss is cross-entropy over the vocabulary; perplexity = exp(cross-entropy) is the standard evaluation metric.

```python
import torch
import torch.nn as nn

torch.manual_seed(42)
text  = 'the quick brown fox jumps over the lazy dog ' * 40
chars = sorted(set(text))
c2i   = {c: i for i, c in enumerate(chars)}
vocab = len(chars)
data  = torch.tensor([c2i[c] for c in text], dtype=torch.long)
T_data, chunk, H, B = len(data) - 1, 35, 64, 1

emb = nn.Embedding(vocab, H)
rnn = nn.RNN(H, H, batch_first=True)
fc  = nn.Linear(H, vocab)
params = list(emb.parameters()) + list(rnn.parameters()) + list(fc.parameters())
opt    = torch.optim.Adam(params, lr=1e-3)
h = torch.zeros(1, B, H)
total_loss, n_steps = 0.0, 0

for start in range(0, T_data - chunk, chunk):
    xc = data[start:start + chunk].unsqueeze(0)          # (1, chunk)
    yc = data[start + 1:start + chunk + 1].unsqueeze(0)  # (1, chunk)
    h  = h.detach()
    embed_xc    = emb(xc)                                # (1, chunk, H)
    hidden_out, h = rnn(embed_xc, h)                     # (1, chunk, H)
    logits      = fc(hidden_out).view(-1, vocab)         # (chunk, vocab)
    loss        = nn.functional.cross_entropy(logits, yc.view(-1))
    opt.zero_grad(); loss.backward()
    torch.nn.utils.clip_grad_norm_(rnn.parameters(), 5.0)
    opt.step()
    total_loss += loss.item(); n_steps += 1

avg_ce = total_loss / n_steps
print(f'Char LM: vocab={vocab}, chunk={chunk} (PTB-style TBPTT)')
print(f'Steps: {n_steps}, avg cross-entropy: {avg_ce:.4f}')
print(f'Perplexity: {torch.exp(torch.tensor(avg_ce)).item():.2f}')
```

## Memory Profiling

The memory advantage of TBPTT over full BPTT scales linearly with T/k. For T=1000 and k=35, TBPTT stores 28x fewer hidden state tensors. Profiling with torch.cuda.memory_allocated() or tracemalloc confirms this theoretical ratio. The autograd graph depth is also proportional to the chunk size, which affects backward pass time. Larger chunks give better gradient quality at the cost of more memory and slower backward passes — the fundamental trade-off in chunk size selection.

```python
import torch
import torch.nn as nn

torch.manual_seed(1)
I, H, B = 16, 64, 4
rnn = nn.RNN(I, H, batch_first=True)

def count_graph_nodes(loss_tensor):
    visited, stack = set(), [loss_tensor.grad_fn]
    while stack:
        n = stack.pop()
        if n is None or id(n) in visited:
            continue
        visited.add(id(n))
        stack.extend(c for c, _ in (n.next_functions or []))
    return len(visited)

print(f'{"T":>6} {"Chunk":>7} {"Method":<20} {"Act. Mem MB":>12} {"Graph nodes":>12}')
bytes_per_float = 4
for T in [50, 100, 200]:
    x = torch.randn(B, T, I)
    out_full, _ = rnn(x, torch.zeros(1, B, H))
    nodes_full  = count_graph_nodes(out_full.sum())
    full_mb     = T * H * B * bytes_per_float / 1e6
    print(f'{T:>6} {T:>7} {"Full BPTT":<20} {full_mb:>12.4f} {nodes_full:>12}')
    for chunk in [10, 25]:
        if chunk >= T:
            continue
        out_c, _ = rnn(x[:, :chunk, :], torch.zeros(1, B, H))
        nodes_c  = count_graph_nodes(out_c.sum())
        mb_c     = chunk * H * B * bytes_per_float / 1e6
        ratio    = full_mb / mb_c
        print(f'{T:>6} {chunk:>7} {f"TBPTT k={chunk}":<20} {mb_c:>12.4f} '
              f'{nodes_c:>12}  ({ratio:.1f}x less mem)')
```

## Practical Chunk Size Selection

| Chunk Size | Gradient Quality | Memory per Chunk | Dependencies Captured | Typical Use Case |
| --- | --- | --- | --- | --- |
| 10 | Poor — very local gradient only | Very low — O(10·H·B) | Up to 10 steps | Simple pattern repetition, short-lag tasks |
| 35 | Moderate — PTB standard | Low — O(35·H·B) | Up to 35 steps | Character-level LM, Penn Treebank word-level LM |
| 100 | Good — captures medium-range patterns | Moderate — O(100·H·B) | Up to 100 steps | Word-level LM, machine translation sequences |
| 256 | Near-full BPTT quality | High — O(256·H·B) | Up to 256 steps | Long documents, modern LSTM/GRU training |

## Trade-offs and Limitations

TBPTT introduces a systematic bias: weights are updated based on local gradient signals only, so long-range patterns are learned indirectly (via the hidden state carrying information forward) rather than directly via gradient. For tasks with dependencies shorter than k, TBPTT is as good as full BPTT. For tasks where the critical signal arrives >k steps before the output, TBPTT may fail to learn even if the hidden state contains the information — because the gradient cannot credit-assign back to where the information was encoded.

> **Rule of Thumb for Chunk Size**: Set chunk size to at least 2–3x the longest dependency you need to learn. If you're unsure, profile gradient cosine similarity between TBPTT and a short full-BPTT run on a small model. Use gradient checkpointing if you want full BPTT quality with acceptable memory: store every sqrt(T) hidden state and recompute the rest during backward.

- TBPTT(k,k): most common form — forward and backward both span k steps per chunk.
- TBPTT(k1,k2) with k1>k2: run k1 steps before each update; backprop only k2 steps back.
- Carry h.detach() forward: hidden state carries long-range info; gradient is local only.
- Chunk size 35: PTB language model benchmark standard since Mikolov (2010).
- Gradient clipping (max_norm=1-5): mandatory alongside TBPTT to prevent explosions.
- Gradient quality monitoring: measure cosine similarity of TBPTT vs full BPTT on a small held-out task.

---

