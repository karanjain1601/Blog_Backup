---
title: "Backpropagation Through Time (BPTT) — Unrolling and Gradient Computation"
slug: "backprop-through-time"
description: "Derive BPTT by unrolling the RNN computational graph, compute gradient products across timesteps, visualise vanishing and exploding gradients, implement full vs truncated BPTT, and apply gradient clipping."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFja3Byb3BhZ2F0aW9uIFRocm91Z2ggVGltZSAoQlBUVCkgaXMgdGhlIGFsZ29yaXRobSB1c2VkIHRvIHRyYWluIFJOTnMuIFRoZSBrZXkgaWRlYSBpcyB0byB1bnJvbGwgdGhlIFJOTiBmb3IgVCBzdGVwcywgY3JlYXRpbmcgYSBkZWVwIGZlZWRmb3J3YXJkIGNvbXB1dGF0aW9uYWwgZ3JhcGggd2l0aCBzaGFyZWQgd2VpZ2h0cy4gU3RhbmRhcmQgYmFja3Byb3BhZ2F0aW9uIGlzIHRoZW4gYXBwbGllZCB0byB0aGlzIHVucm9sbGVkIGdyYXBoLiBUaGUgZ3JhZGllbnQgb2YgdGhlIGxvc3Mgd2l0aCByZXNwZWN0IHRvIHRoZSByZWN1cnJlbnQgd2VpZ2h0IG1hdHJpeCBX4oKV4oKVIGFjY3VtdWxhdGVzIGNvbnRyaWJ1dGlvbnMgZnJvbSBldmVyeSB0aW1lc3RlcDogZEwvZFfigpXigpUgPSDOo+KCnCBkTOKCnC9kV+KCleKClS4gRWFjaCB0ZXJtIGludm9sdmVzIGEgcHJvZHVjdCBvZiBKYWNvYmlhbnMg4oiCaOKCnC/iiIJo4oKc4oKL4oKBID0gV+KCleKCleG1gCDCtyBkaWFnKHRhbmhcdTAwMjcoaOKCnCkpLCB3aGljaCBjYXVzZXMgZ3JhZGllbnRzIHRvIGVpdGhlciB2YW5pc2ggKGlmIOKAllfigpXigpXigJZcdTAwM2MxKSBvciBleHBsb2RlIChpZiDigJZX4oKV4oKV4oCWXHUwMDNlMSkgZXhwb25lbnRpYWxseSB3aXRoIFQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVW5yb2xsaW5nIHRoZSBDb21wdXRhdGlvbmFsIEdyYXBoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVbnJvbGxpbmcgY3JlYXRlcyBUIGNvcGllcyBvZiB0aGUgUk5OIGNlbGwgc2hhcmluZyB0aGUgc2FtZSB3ZWlnaHRzLiBUaGUgY29tcHV0YXRpb25hbCBncmFwaCBoYXMgVCBub2RlcyBmb3IgaGlkZGVuIHN0YXRlcyBo4oKALCBo4oKBLCAuLi4sIGjigpzigovigoEgYW5kIFQgbm9kZXMgZm9yIG91dHB1dHMgeeKCgCwgLi4uLCB54oKc4oKL4oKBLiBBbGwgZWRnZXMgZnJvbSBo4oKc4oKL4oKBIHRvIGjigpwgcGFzcyB0aHJvdWdoIHRoZSBzYW1lIFfigpXigpUuIER1cmluZyBmb3J3YXJkIHBhc3MsIGFsbCBUIGhpZGRlbiBzdGF0ZXMgbXVzdCBiZSBjb21wdXRlZCBzZXF1ZW50aWFsbHkgYW5kIHN0b3JlZCBpbiBtZW1vcnkgZm9yIHRoZSBiYWNrd2FyZCBwYXNzIOKAlCB0aGlzIGdpdmVzIE8oVMK3SCkgbWVtb3J5IHJlcXVpcmVtZW50LiBUaGUgYmFja3dhcmQgcGFzcyB0aGVuIHRyYXZlcnNlcyB0aGUgZ3JhcGggaW4gcmV2ZXJzZTogZnJvbSB0aGUgZmluYWwgbG9zcyBiYWNrIHRocm91Z2ggZXZlcnkgaGlkZGVuIHN0YXRlIHRvIHRoZSBmaXJzdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuVCwgSSwgSCwgTyA9IDEwLCA0LCA4LCAyXG5cbiMgSW5pdGlhbGl6ZSB3ZWlnaHRzXG5XeGggPSBucC5yYW5kb20ucmFuZG4oSCwgSSkgKiAwLjFcbldoaCA9IG5wLnJhbmRvbS5yYW5kbihILCBIKSAqIDAuMVxuV2h5ID0gbnAucmFuZG9tLnJhbmRuKE8sIEgpICogMC4xXG5iaCAgPSBucC56ZXJvcygoSCwgMSkpXG5ieSAgPSBucC56ZXJvcygoTywgMSkpXG54cyAgPSBbbnAucmFuZG9tLnJhbmRuKEksIDEpIGZvciBfIGluIHJhbmdlKFQpXVxuXG4jIEZvcndhcmQgcGFzcyAtLSBzdG9yZSBhbGwgaGlkZGVuIHN0YXRlcyAobmVlZGVkIGZvciBiYWNrd2FyZClcbmhzICA9IHstMTogbnAuemVyb3MoKEgsIDEpKX1cbnJhdyA9IHt9XG5mb3IgdCBpbiByYW5nZShUKTpcbiAgICByYXdbdF0gPSBXeGggQCB4c1t0XSArIFdoaCBAIGhzW3QtMV0gKyBiaFxuICAgIGhzW3RdICA9IG5wLnRhbmgocmF3W3RdKVxub3V0ID0gV2h5IEAgaHNbVC0xXSArIGJ5XG5cbiMgQmFja3dhcmQgcGFzcyB0aHJvdWdoIHRpbWUgLS0gdW5yb2xsIGFsbCBUIHN0ZXBzXG5keSAgID0gb3V0IC0gbnAub25lcygoTywgMSkpICAgIyBncmFkaWVudCBvZiBNU0UgbG9zc1xuZFdoeSA9IGR5IEAgaHNbVC0xXS5UXG5kV3hoID0gbnAuemVyb3NfbGlrZShXeGgpXG5kV2hoID0gbnAuemVyb3NfbGlrZShXaGgpXG5kYmggID0gbnAuemVyb3NfbGlrZShiaClcbmRoICAgPSBXaHkuVCBAIGR5XG5ncmFkX25vcm1zID0gW11cblxuZm9yIHQgaW4gcmV2ZXJzZWQocmFuZ2UoVCkpOlxuICAgIGR0YW5oID0gKDEgLSBoc1t0XSoqMikgKiBkaCAgICMgYmFja3Byb3AgdGhyb3VnaCB0YW5oXG4gICAgZFdoaCArPSBkdGFuaCBAIGhzW3QtMV0uVCAgICAgIyBhY2N1bXVsYXRlIFdoaCBncmFkaWVudFxuICAgIGRXeGggKz0gZHRhbmggQCB4c1t0XS5UXG4gICAgZGJoICArPSBkdGFuaFxuICAgIGdyYWRfbm9ybXMuYXBwZW5kKGZsb2F0KG5wLmxpbmFsZy5ub3JtKGRoKSkpXG4gICAgZGggICAgPSBXaGguVCBAIGR0YW5oICAgICAgICAgICMgcHJvcGFnYXRlIHRocm91Z2ggV2hoXG5cbnByaW50KFx1MDAyN0JQVFQgZ3JhZGllbnQgbm9ybXMgZmxvd2luZyBiYWNrIHRocm91Z2ggdGltZSAobGF0ZXN0IHRvIGVhcmxpZXN0KTpcdTAwMjcpXG5mb3IgaSwgbiBpbiBlbnVtZXJhdGUoZ3JhZF9ub3Jtcyk6XG4gICAgcHJpbnQoZlx1MDAyNyAgc3RlcCB7VC0xLWk6MmR9OiB7bjouNmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IEZsb3cgVGhyb3VnaCBUaW1lIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZ3JhZGllbnQgb2YgdGhlIGxvc3MgYXQgc3RlcCBUIHdpdGggcmVzcGVjdCB0byB0aGUgaGlkZGVuIHN0YXRlIGF0IHN0ZXAgayBpczogZEzigpwvZGjigpYgPSAoZEzigpwvZGjigpwpIMK3IM6g4rG84oKM4oKW4oKK4oKB4bWAICjiiIJo4rG8L+KIgmjisbzigovigoEpLiBFYWNoIGZhY3RvciDiiIJo4rG8L+KIgmjisbzigovigoEgPSBX4oKV4oKV4bWAIMK3IGRpYWcoMSAtIGjisbzCsikuIElmIHRoZSBsYXJnZXN0IHNpbmd1bGFyIHZhbHVlIM+DX21heChX4oKV4oKVKSBcdTAwM2MgMSwgdGhlbiDigJbiiIJo4rG8L+KIgmjisbzigovigoHigJYgXHUwMDNjIDEgYW5kIHRoZSBwcm9kdWN0IGRlY2F5cyBleHBvbmVudGlhbGx5IHdpdGggVC1rLiBJZiDPg19tYXggXHUwMDNlIDEsIHRoZSBwcm9kdWN0IGdyb3dzIGV4cG9uZW50aWFsbHkuIFRoZSB0YW5oIHNhdHVyYXRpb24gZmFjdG9yICgxLWjisbzCsikg4oiIIFswLDFdIGZ1cnRoZXIgcmVkdWNlcyBncmFkaWVudCBtYWduaXR1ZGUsIG1ha2luZyB2YW5pc2hpbmcgbW9yZSBsaWtlbHkgdGhhbiBleHBsb2RpbmcgaW4gcHJhY3RpY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5ucC5yYW5kb20uc2VlZCgwKVxuVCwgSCwgSSA9IDMwLCAxNiwgNFxuXG5kZWYgZ3JhZGllbnRfbm9ybV9wcm9maWxlKFdoaF9zY2FsZSwgVD0zMCwgSD0xNiwgST00KTpcbiAgICBucC5yYW5kb20uc2VlZCgwKVxuICAgIFd4aCA9IG5wLnJhbmRvbS5yYW5kbihILCBJKSAqIDAuMVxuICAgIFdoaCA9IG5wLnJhbmRvbS5yYW5kbihILCBIKSAqIFdoaF9zY2FsZSAvIG5wLnNxcnQoSClcbiAgICBiaCAgPSBucC56ZXJvcygoSCwgMSkpXG4gICAgeHMgID0gW25wLnJhbmRvbS5yYW5kbihJLCAxKSBmb3IgXyBpbiByYW5nZShUKV1cbiAgICBocyAgPSB7LTE6IG5wLnplcm9zKChILCAxKSl9XG4gICAgZm9yIHQgaW4gcmFuZ2UoVCk6XG4gICAgICAgIGhzW3RdID0gbnAudGFuaChXeGggQCB4c1t0XSArIFdoaCBAIGhzW3QtMV0gKyBiaClcbiAgICBkaCA9IG5wLm9uZXMoKEgsIDEpKSAvIEhcbiAgICBub3JtcyA9IHt9XG4gICAgZm9yIHQgaW4gcmV2ZXJzZWQocmFuZ2UoVCkpOlxuICAgICAgICBub3Jtc1t0XSA9IGZsb2F0KG5wLmxpbmFsZy5ub3JtKGRoKSlcbiAgICAgICAgZHRhbmggICAgPSAoMSAtIGhzW3RdKioyKSAqIGRoXG4gICAgICAgIGRoICAgICAgID0gV2hoLlQgQCBkdGFuaFxuICAgIHJldHVybiBbbm9ybXNbdF0gZm9yIHQgaW4gcmFuZ2UoVCldXG5cbnByaW50KGZcdTAwMjdHcmFkaWVudCBtYWduaXR1ZGUgYXQgc2VsZWN0ZWQgdGltZXN0ZXBzIChsb3NzIGF0IHQ9e1QtMX0pOlx1MDAyNylcbnByaW50KGZcdTAwMjd7XCJTY2FsZVwiOlx1MDAzZTh9IHtcInQ9VC0xXCI6XHUwMDNlMTB9IHtcInQ9VC8yXCI6XHUwMDNlMTB9IHtcInQ9MFwiOlx1MDAzZTEwfSB7XCJSZWdpbWVcIjpcdTAwM2UxMn1cdTAwMjcpXG5mb3Igc2NhbGUsIGxhYmVsIGluIFsoMC41LCBcdTAwMjd2YW5pc2hpbmdcdTAwMjcpLCAoMS4wLCBcdTAwMjdtYXJnaW5hbFx1MDAyNyksICgyLjAsIFx1MDAyN2V4cGxvZGluZ1x1MDAyNyldOlxuICAgIG5vcm1zID0gZ3JhZGllbnRfbm9ybV9wcm9maWxlKHNjYWxlKVxuICAgIHRfaGFsZiA9IFQgLy8gMlxuICAgIHByaW50KGZcdTAwMjd7c2NhbGU6XHUwMDNlOC4xZn0ge25vcm1zW1QtMV06XHUwMDNlMTAuNGV9IHtub3Jtc1t0X2hhbGZdOlx1MDAzZTEwLjRlfSBcdTAwMjdcbiAgICAgICAgICBmXHUwMDI3e25vcm1zWzBdOlx1MDAzZTEwLjRlfSB7bGFiZWw6XHUwMDNlMTJ9XHUwMDI3KVxucHJpbnQoXHUwMDI3UmF0aW8gbm9ybXNbMF0vbm9ybXNbVC0xXSBzaG93cyBleHBvbmVudGlhbCBjaGFuZ2UgYWNyb3NzIFQgc3RlcHMuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IFZhbmlzaGluZyBhbmQgRXhwbG9kaW5nIEFuYWx5c2lzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWYW5pc2hpbmcgZ3JhZGllbnQ6IHdoZW4g4oCWV+KCleKCleKAliBcdTAwM2MgMSwgZ3JhZGllbnRzIGFwcHJvYWNoaW5nIGZyb20gZmFyLWF3YXkgdGltZXN0ZXBzIGJlY29tZSBuZWdsaWdpYmx5IHNtYWxsLiBUaGUgd2VpZ2h0IHVwZGF0ZSBkTC9kV+KCleKClSA9IM6j4oKcIGRM4oKcL2RX4oKV4oKVIGlzIGRvbWluYXRlZCBieSByZWNlbnQgdGltZXN0ZXBzOyB0aGUgbW9kZWwgY2Fubm90IGxlYXJuIGRlcGVuZGVuY2llcyBsb25nZXIgdGhhbiB+MTDigJMyMCBzdGVwcyB3aXRoIHJhbmRvbSBpbml0aWFsaXNhdGlvbi4gRXhwbG9kaW5nIGdyYWRpZW50OiB3aGVuIOKAllfigpXigpXigJYgXHUwMDNlIDEsIGdyYWRpZW50cyBibG93IHVwLCBjYXVzaW5nIE5hTiBsb3NzZXMuIEdyYWRpZW50IGNsaXBwaW5nIOKAlCBzY2FsaW5nIHRoZSBncmFkaWVudCB3aGVuIOKAlmfigJYgXHUwMDNlIHRocmVzaG9sZCDigJQgaXMgdGhlIHN0YW5kYXJkIGZpeCBmb3IgZXhwbG9zaW9ucy4gQ2xpcHBpbmcgZG9lcyBub3QgZml4IHZhbmlzaGluZyBncmFkaWVudHM7IHRoYXQgcmVxdWlyZXMgYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzIChMU1RNL0dSVSkgb3IgY2FyZWZ1bCBpbml0aWFsaXNhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGdWxsIEJQVFQgdnMgVHJ1bmNhdGVkIEJQVFQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZ1bGwgQlBUVCB1bnJvbGxzIHRoZSBlbnRpcmUgc2VxdWVuY2Ugb2YgVCBzdGVwcy4gRm9yIFQ9MTAwMCBhbmQgSD01MTIsIHN0b3JpbmcgYWxsIGhpZGRlbiBzdGF0ZXMgcmVxdWlyZXMgMTAwMMOXNTEyw5c0IGJ5dGVzIOKJiCAyIE1CIHBlciBzZXF1ZW5jZSAocGVyIGJhdGNoIGVsZW1lbnQpLiBNb3JlIGltcG9ydGFudGx5LCB0aGUgYmFja3dhcmQgcGFzcyBpcyBhbHNvIHNlcXVlbnRpYWwgb3ZlciBUIHN0ZXBzLiBUcnVuY2F0ZWQgQlBUVCAoVEJQVFQpIGxpbWl0cyB0aGUgYmFja3dhcmQgcGFzcyB0byB0aGUgbGFzdCBrIHN0ZXBzOiB0aGUgc2VxdWVuY2UgaXMgc3BsaXQgaW50byBjaHVua3Mgb2Ygc2l6ZSBrLCB0aGUgaGlkZGVuIHN0YXRlIGlzIGNhcnJpZWQgZm9yd2FyZCAod2l0aG91dCBncmFkaWVudCkgZnJvbSBvbmUgY2h1bmsgdG8gdGhlIG5leHQsIGFuZCBiYWNrcHJvcGFnYXRpb24gb25seSBnb2VzIGsgc3RlcHMgYmFjay4gVGhpcyByZWR1Y2VzIG1lbW9yeSB0byBPKGvCt0gpIGFuZCBlbmFibGVzIGFwcHJveGltYXRlIGJ1dCBwcmFjdGljYWwgdHJhaW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5ucC5yYW5kb20uc2VlZCg3KVxuVCwgSSwgSCA9IDQwLCA0LCA4XG5XaGhfc2NhbGUgPSAwLjUgICAjIHZhbmlzaGluZyByZWdpbWUgZm9yIGNsZWFyIGRlbW9uc3RyYXRpb25cblxuV3hoID0gbnAucmFuZG9tLnJhbmRuKEgsIEkpICogMC4xXG5XaGggPSBucC5yYW5kb20ucmFuZG4oSCwgSCkgKiBXaGhfc2NhbGUgLyBucC5zcXJ0KEgpXG5iaCAgPSBucC56ZXJvcygoSCwgMSkpXG54cyAgPSBbbnAucmFuZG9tLnJhbmRuKEksIDEpIGZvciBfIGluIHJhbmdlKFQpXVxuXG5kZWYgZm9yd2FyZF9hbGwoeHMsIGgwKTpcbiAgICBocyA9IHstMTogaDB9XG4gICAgZm9yIHQsIHggaW4gZW51bWVyYXRlKHhzKTpcbiAgICAgICAgaHNbdF0gPSBucC50YW5oKFd4aCBAIHggKyBXaGggQCBoc1t0LTFdICsgYmgpXG4gICAgcmV0dXJuIGhzXG5cbmRlZiBicHR0X2dyYWRpZW50KHhzLCBocywga19iYWNrKTpcbiAgICBkaCA9IG5wLm9uZXMoKEgsIDEpKSAvIEg7IGRXID0gbnAuemVyb3NfbGlrZShXaGgpXG4gICAgVF9jaHVuayA9IGxlbih4cylcbiAgICBmb3IgdCBpbiByZXZlcnNlZChyYW5nZShtYXgoMCwgVF9jaHVuayAtIGtfYmFjayksIFRfY2h1bmspKTpcbiAgICAgICAgZHQgPSAoMSAtIGhzW3RdKioyKSAqIGRoXG4gICAgICAgIGRXICs9IGR0IEAgaHNbdC0xXS5UXG4gICAgICAgIGRoICA9IFdoaC5UIEAgZHRcbiAgICByZXR1cm4gZFdcblxuaHNfZnVsbCA9IGZvcndhcmRfYWxsKHhzLCBucC56ZXJvcygoSCwgMSkpKVxuZFdfZnVsbCA9IGJwdHRfZ3JhZGllbnQoeHMsIGhzX2Z1bGwsIFQpICAgIyBmdWxsIEJQVFRcblxucHJpbnQoZlx1MDAyN0Z1bGwgQlBUVCAoaz17VH0pOiBkV2hoIG5vcm0gPSB7bnAubGluYWxnLm5vcm0oZFdfZnVsbCk6LjZmfVx1MDAyNylcbmZvciBrIGluIFs1LCAxMCwgMjAsIFRdOlxuICAgIGRXX2sgPSBicHR0X2dyYWRpZW50KHhzLCBoc19mdWxsLCBrKVxuICAgIGNvcyAgPSBucC5kb3QoZFdfZnVsbC5yYXZlbCgpLCBkV19rLnJhdmVsKCkpIC8gKFxuICAgICAgICAgICAgICAgbnAubGluYWxnLm5vcm0oZFdfZnVsbCkgKiBucC5saW5hbGcubm9ybShkV19rKSArIDFlLTkpXG4gICAgcHJpbnQoZlx1MDAyNyAgVHJ1bmNhdGVkIGs9e2s6MmR9OiBjb3NpbmUgc2ltaWxhcml0eT17Y29zOi40Zn0sIG5vcm09e25wLmxpbmFsZy5ub3JtKGRXX2spOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGV0YWNoaW5nIEhpZGRlbiBTdGF0ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gUHlUb3JjaCwgaC5kZXRhY2goKSBjcmVhdGVzIGEgbmV3IHRlbnNvciB0aGF0IHNoYXJlcyB0aGUgc2FtZSBkYXRhIGJ1dCBoYXMgbm8gZ3JhZGllbnQgdHJhY2tpbmcuIFdoZW4gcGFzc2VkIGFzIHRoZSBpbml0aWFsIHN0YXRlIHRvIHRoZSBuZXh0IGNodW5rLCBncmFkaWVudHMgZnJvbSB0aGF0IGNodW5rIGNhbm5vdCBmbG93IGJhY2sgdGhyb3VnaCB0aGUgZGV0YWNoZWQgdGVuc29yIGludG8gdGhlIHByZXZpb3VzIGNodW5rXHUwMDI3cyBjb21wdXRhdGlvbiBncmFwaC4gVGhpcyBpcyBlc3NlbnRpYWwgZm9yIG1lbW9yeS1lZmZpY2llbnQgdHJhaW5pbmcgb2YgbG9uZyBzZXF1ZW5jZXM6IHdpdGhvdXQgZGV0YWNoLCB0aGUgYmFja3dhcmQgcGFzcyB3b3VsZCBuZWVkIHRvIHRyYXZlcnNlIHRoZSBlbnRpcmUgYWNjdW11bGF0ZWQgZ3JhcGgsIGRlZmVhdGluZyB0aGUgcHVycG9zZSBvZiBjaHVua2luZy4gVGhlIHBhdHRlcm4gaXM6IGggPSBoLmRldGFjaCgpIGJlZm9yZSBlYWNoIGNodW5rXHUwMDI3cyBmb3J3YXJkIHBhc3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuVCwgY2h1bmssIEksIEgsIE8sIEIgPSAxMDAsIDIwLCA4LCAzMiwgNCwgNFxuXG5ybm4gPSBubi5STk4oSSwgSCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbmZjICA9IG5uLkxpbmVhcihILCBPKVxub3B0ID0gdG9yY2gub3B0aW0uQWRhbShsaXN0KHJubi5wYXJhbWV0ZXJzKCkpICsgbGlzdChmYy5wYXJhbWV0ZXJzKCkpLCBscj0xZS0zKVxueCAgID0gdG9yY2gucmFuZG4oQiwgVCwgSSlcbnkgICA9IHRvcmNoLnJhbmRuKEIsIFQsIE8pXG5cbnRvdGFsX2xvc3MgPSAwLjBcbmggPSB0b3JjaC56ZXJvcygxLCBCLCBIKVxuZm9yIHN0YXJ0IGluIHJhbmdlKDAsIFQsIGNodW5rKTpcbiAgICB4YyAgID0geFs6LCBzdGFydDpzdGFydCArIGNodW5rLCA6XVxuICAgIHljICAgPSB5WzosIHN0YXJ0OnN0YXJ0ICsgY2h1bmssIDpdXG4gICAgaF9pbiA9IGguZGV0YWNoKCkgICAgICAgICAgIyBzdG9wIGdyYWRpZW50IGZyb20gZmxvd2luZyBpbnRvIHByZXYgY2h1bmtcbiAgICBvcHQuemVyb19ncmFkKClcbiAgICBvdXQsIGggPSBybm4oeGMsIGhfaW4pXG4gICAgbG9zcyA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MoZmMob3V0KSwgeWMpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgdG9yY2gubm4udXRpbHMuY2xpcF9ncmFkX25vcm1fKHJubi5wYXJhbWV0ZXJzKCksIG1heF9ub3JtPTEuMClcbiAgICBvcHQuc3RlcCgpXG4gICAgdG90YWxfbG9zcyArPSBsb3NzLml0ZW0oKVxuXG5uX2NodW5rcyA9IFQgLy8gY2h1bmtcbnByaW50KGZcdTAwMjdUQlBUVCB0cmFpbmluZzoge25fY2h1bmtzfSBjaHVua3MgeCB7Y2h1bmt9IHN0ZXBzXHUwMDI3KVxucHJpbnQoZlx1MDAyN0F2ZyBjaHVuayBsb3NzOiB7dG90YWxfbG9zcyAvIG5fY2h1bmtzOi42Zn1cdTAwMjcpXG5wcmludChcdTAwMjdoLmRldGFjaCgpIGJyZWFrcyBncmFkaWVudCBncmFwaCAtLSBtZW1vcnkgaXMgTyhjaHVuayAqIEgpIHBlciBzdGVwLlx1MDAyNylcbnByaW50KGZcdTAwMjdTYXZpbmdzIHZzIGZ1bGwgQlBUVDoge1QgLy8gY2h1bmt9eCBsZXNzIGdyYXBoIG5vZGVzIHRvIHN0b3JlLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcnkgUmVxdWlyZW1lbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGdWxsIEJQVFQgbXVzdCBzdG9yZSBhbGwgVCBoaWRkZW4gc3RhdGVzIGZvciB0aGUgYmFja3dhcmQgcGFzczogTyhUwrdIwrdCwrc0KSBieXRlcyAoZmxvYXQzMikuIEZvciBUPTEwMDAsIEg9NTEyLCBCPTMyOiAxMDAww5c1MTLDlzMyw5c0IOKJiCA2NCBNQiBwZXIgbGF5ZXIuIFRydW5jYXRlZCBCUFRUIHdpdGggY2h1bmsgayBzdG9yZXMgb25seSBrIGhpZGRlbiBzdGF0ZXM6IE8oa8K3SMK3QsK3NCkgYnl0ZXMuIEFkZGl0aW9uYWxseSwgc3RvcmluZyByYXcgcHJlLWFjdGl2YXRpb24gdmFsdWVzIGZvciBiYWNrcHJvcGFnYXRpbmcgdGhyb3VnaCB0YW5oIGRvdWJsZXMgdGhpcyBlc3RpbWF0ZS4gR3JhZGllbnQgY2hlY2twb2ludGluZyBjYW4gdHJhZGUgcmVjb21wdXRhdGlvbiBmb3IgbWVtb3J5LCBzdG9yaW5nIG9ubHkgZXZlcnkg4oiaVCBoaWRkZW4gc3RhdGUgYW5kIHJlY29tcHV0aW5nIHRoZSByZXN0IGR1cmluZyBiYWNrd2FyZCDigJQgcmVkdWNpbmcgbWVtb3J5IHRvIE8o4oiaVMK3SCkgYXQgdGhlIGNvc3Qgb2YgfjEuNXggZm9yd2FyZCBwYXNzZXMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJHcmFkaWVudCBDbGlwcGluZyBJcyBFc3NlbnRpYWwiLCJjb250ZW50IjoiQWx3YXlzIGFwcGx5IGdyYWRpZW50IGNsaXBwaW5nIHdoZW4gdHJhaW5pbmcgUk5Ocy4gVGhlIHN0YW5kYXJkIHRocmVzaG9sZCBpcyBtYXhfbm9ybT0xLjAgdG8gNS4wICh1c2UgdG9yY2gubm4udXRpbHMuY2xpcF9ncmFkX25vcm1fKS4gV2l0aG91dCBjbGlwcGluZywgYSBzaW5nbGUgc3RlcCB3aXRoIOKAllfigpXigpXigJZcdTAwM2UxIGNhbiBjYXVzZSBleHBsb3NpdmUgZ3JhZGllbnQgZ3Jvd3RoLCByZXN1bHRpbmcgaW4gTmFOIHBhcmFtZXRlcnMuIENsaXBwaW5nIGRvZXMgbm90IHByZXZlbnQgdmFuaXNoaW5nIGdyYWRpZW50cyDigJQgZm9yIHRoYXQsIHVzZSBMU1RNL0dSVSBhcmNoaXRlY3R1cmVzIG9yIGdyYWRpZW50IGhpZ2h3YXkgY29ubmVjdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgQ2xpcHBpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdyYWRpZW50IGNsaXBwaW5nIHJlc2NhbGVzIHRoZSBncmFkaWVudCB2ZWN0b3Igd2hlbiBpdHMgbm9ybSBleGNlZWRzIGEgdGhyZXNob2xkOiBpZiDigJZn4oCWIFx1MDAzZSDOuCwgc2V0IGcg4oaQIGfCtyjOuC/igJZn4oCWKS4gVGhpcyBwcmVzZXJ2ZXMgZ3JhZGllbnQgZGlyZWN0aW9uIHdoaWxlIGJvdW5kaW5nIGl0cyBtYWduaXR1ZGUuIFRoZSB0aHJlc2hvbGQgzrggaXMgYSBoeXBlcnBhcmFtZXRlciB0eXBpY2FsbHkgc2V0IGJldHdlZW4gMS4wIGFuZCAxMC4wOyBsb3dlciB2YWx1ZXMgYXJlIHNhZmVyIGJ1dCBtYXkgc2xvdyBjb252ZXJnZW5jZS4gR2xvYmFsIGNsaXBwaW5nIChhY3Jvc3MgYWxsIHBhcmFtZXRlcnMpIGlzIHByZWZlcnJlZCBvdmVyIHBlci1wYXJhbWV0ZXIgY2xpcHBpbmcuIE1vbml0b3JpbmcgdGhlIGZyYWN0aW9uIG9mIHN0ZXBzIHdoZXJlIGNsaXBwaW5nIGFjdGl2YXRlcyBpcyB1c2VmdWwgZGlhZ25vc3RpY3M6IFx1MDAzZTUwJSBhY3RpdmF0aW9uIHN1Z2dlc3RzIHRoZSB0aHJlc2hvbGQgaXMgdG9vIGxvdzsgMCUgbWVhbnMgaXQgbWF5IGJlIHRvbyBoaWdoIG9yIGdyYWRpZW50cyBhcmUgd2VsbC1iZWhhdmVkLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJNZW1vcnkiLCJHcmFkaWVudCBRdWFsaXR5IiwiUGFyYWxsZWxpemFibGUiLCJMb25nLVJhbmdlIENhcHR1cmUiXSwicm93cyI6W1siRnVsbCBCUFRUIiwiTyhUwrdIwrdCKSDigJQgc3RvcmVzIGFsbCBoaWRkZW4gc3RhdGVzIiwiRXhhY3QgZ3JhZGllbnQiLCJObyDigJQgc2VxdWVudGlhbCB1bnJvbGwgb3ZlciBUIiwiWWVzIOKAlCBncmFkaWVudCBmbG93cyBmcm9tIHQ9VCB0byB0PTAiXSxbIlRydW5jYXRlZCBCUFRUIChrKSIsIk8oa8K3SMK3Qikg4oCUIG9ubHkgayBzdGF0ZXMiLCJBcHByb3hpbWF0aW9uIOKAlCBsb2NhbCBncmFkaWVudCBvbmx5IiwiTm8g4oCUIHN0aWxsIHNlcXVlbnRpYWwiLCJPbmx5IHdpdGhpbiBrIHN0ZXBzOyBubyBzaWduYWwgZm9yIGxhZyBcdTAwM2UgayJdLFsiUmVhbC1UaW1lIFJlY3VycmVudCBMZWFybmluZyIsIk8oSMKyKSBwZXIgc3RlcCDigJQgb25saW5lIiwiRXhhY3QgYnV0IG9ubGluZSAocGVyLXN0ZXApIiwiWWVzIOKAlCBvbmUgc3RlcCBhdCBhIHRpbWUiLCJZZXMg4oCUIEjCsiBwYXJhbWV0ZXIgZ3JhZGllbnRzIHBlciBzdGVwIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZ1bGwgQlBUVDogZXhhY3QgZ3JhZGllbnRzIGJ1dCBPKFQpIG1lbW9yeSBhbmQgdGltZTsgaW5mZWFzaWJsZSBmb3IgVCBcdTAwM2UgYSBmZXcgaHVuZHJlZC4iLCJUcnVuY2F0ZWQgQlBUVDogc3RhbmRhcmQgaW4gcHJhY3RpY2U7IGNodW5rIHNpemVzIG9mIDM14oCTMjU2IGFyZSBjb21tb247IGdyYWRpZW50IGlzIGJpYXNlZCBmb3IgbG9uZyBsYWdzLiIsIkdyYWRpZW50IGNoZWNrcG9pbnRpbmc6IE8oc3FydChUKSkgbWVtb3J5LCAxLjV4IGNvbXB1dGU7IHVzZWZ1bCB3aGVuIFQgaXMgbGFyZ2UgYnV0IG5vdCBleHRyZW1lLiIsIlJUUkw6IG9ubGluZSBsZWFybmluZyB3aXRoIGV4YWN0IGdyYWRpZW50cyBidXQgTyhIXjQpIGNvbXB1dGUgcGVyIHN0ZXAg4oCUIG9ubHkgcHJhY3RpY2FsIGZvciB0aW55IEguIiwiR3JhZGllbnQgY2xpcHBpbmcgKG1heF9ub3JtPTEtNSk6IHByZXZlbnRzIGV4cGxvc2lvbnM7IG1hbmRhdG9yeSBmb3Igc3RhYmxlIFJOTiB0cmFpbmluZy4iLCJPcnRob2dvbmFsIFdoaCBpbml0OiBzcGVjdHJhbCByYWRpdXMgPSAxIGF0IGluaXRpYWxpc2F0aW9uOyBkZWxheXMgdmFuaXNoaW5nIGdyYWRpZW50IG9uc2V0LiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Backpropagation Through Time (BPTT) — Unrolling and Gradient Computation

Backpropagation Through Time (BPTT) is the algorithm used to train RNNs. The key idea is to unroll the RNN for T steps, creating a deep feedforward computational graph with shared weights. Standard backpropagation is then applied to this unrolled graph. The gradient of the loss with respect to the recurrent weight matrix Wₕₕ accumulates contributions from every timestep: dL/dWₕₕ = Σₜ dLₜ/dWₕₕ. Each term involves a product of Jacobians ∂hₜ/∂hₜ₋₁ = Wₕₕᵀ · diag(tanh'(hₜ)), which causes gradients to either vanish (if ‖Wₕₕ‖<1) or explode (if ‖Wₕₕ‖>1) exponentially with T.

## Unrolling the Computational Graph

Unrolling creates T copies of the RNN cell sharing the same weights. The computational graph has T nodes for hidden states h₀, h₁, ..., hₜ₋₁ and T nodes for outputs y₀, ..., yₜ₋₁. All edges from hₜ₋₁ to hₜ pass through the same Wₕₕ. During forward pass, all T hidden states must be computed sequentially and stored in memory for the backward pass — this gives O(T·H) memory requirement. The backward pass then traverses the graph in reverse: from the final loss back through every hidden state to the first.

```python
import numpy as np

np.random.seed(42)
T, I, H, O = 10, 4, 8, 2

# Initialize weights
Wxh = np.random.randn(H, I) * 0.1
Whh = np.random.randn(H, H) * 0.1
Why = np.random.randn(O, H) * 0.1
bh  = np.zeros((H, 1))
by  = np.zeros((O, 1))
xs  = [np.random.randn(I, 1) for _ in range(T)]

# Forward pass -- store all hidden states (needed for backward)
hs  = {-1: np.zeros((H, 1))}
raw = {}
for t in range(T):
    raw[t] = Wxh @ xs[t] + Whh @ hs[t-1] + bh
    hs[t]  = np.tanh(raw[t])
out = Why @ hs[T-1] + by

# Backward pass through time -- unroll all T steps
dy   = out - np.ones((O, 1))   # gradient of MSE loss
dWhy = dy @ hs[T-1].T
dWxh = np.zeros_like(Wxh)
dWhh = np.zeros_like(Whh)
dbh  = np.zeros_like(bh)
dh   = Why.T @ dy
grad_norms = []

for t in reversed(range(T)):
    dtanh = (1 - hs[t]**2) * dh   # backprop through tanh
    dWhh += dtanh @ hs[t-1].T     # accumulate Whh gradient
    dWxh += dtanh @ xs[t].T
    dbh  += dtanh
    grad_norms.append(float(np.linalg.norm(dh)))
    dh    = Whh.T @ dtanh          # propagate through Whh

print('BPTT gradient norms flowing back through time (latest to earliest):')
for i, n in enumerate(grad_norms):
    print(f'  step {T-1-i:2d}: {n:.6f}')
```

## Gradient Flow Through Time

The gradient of the loss at step T with respect to the hidden state at step k is: dLₜ/dhₖ = (dLₜ/dhₜ) · Πⱼ₌ₖ₊₁ᵀ (∂hⱼ/∂hⱼ₋₁). Each factor ∂hⱼ/∂hⱼ₋₁ = Wₕₕᵀ · diag(1 - hⱼ²). If the largest singular value σ_max(Wₕₕ) < 1, then ‖∂hⱼ/∂hⱼ₋₁‖ < 1 and the product decays exponentially with T-k. If σ_max > 1, the product grows exponentially. The tanh saturation factor (1-hⱼ²) ∈ [0,1] further reduces gradient magnitude, making vanishing more likely than exploding in practice.

```python
import numpy as np

np.random.seed(0)
T, H, I = 30, 16, 4

def gradient_norm_profile(Whh_scale, T=30, H=16, I=4):
    np.random.seed(0)
    Wxh = np.random.randn(H, I) * 0.1
    Whh = np.random.randn(H, H) * Whh_scale / np.sqrt(H)
    bh  = np.zeros((H, 1))
    xs  = [np.random.randn(I, 1) for _ in range(T)]
    hs  = {-1: np.zeros((H, 1))}
    for t in range(T):
        hs[t] = np.tanh(Wxh @ xs[t] + Whh @ hs[t-1] + bh)
    dh = np.ones((H, 1)) / H
    norms = {}
    for t in reversed(range(T)):
        norms[t] = float(np.linalg.norm(dh))
        dtanh    = (1 - hs[t]**2) * dh
        dh       = Whh.T @ dtanh
    return [norms[t] for t in range(T)]

print(f'Gradient magnitude at selected timesteps (loss at t={T-1}):')
print(f'{"Scale":>8} {"t=T-1":>10} {"t=T/2":>10} {"t=0":>10} {"Regime":>12}')
for scale, label in [(0.5, 'vanishing'), (1.0, 'marginal'), (2.0, 'exploding')]:
    norms = gradient_norm_profile(scale)
    t_half = T // 2
    print(f'{scale:>8.1f} {norms[T-1]:>10.4e} {norms[t_half]:>10.4e} '
          f'{norms[0]:>10.4e} {label:>12}')
print('Ratio norms[0]/norms[T-1] shows exponential change across T steps.')
```

## Gradient Vanishing and Exploding Analysis

Vanishing gradient: when ‖Wₕₕ‖ < 1, gradients approaching from far-away timesteps become negligibly small. The weight update dL/dWₕₕ = Σₜ dLₜ/dWₕₕ is dominated by recent timesteps; the model cannot learn dependencies longer than ~10–20 steps with random initialisation. Exploding gradient: when ‖Wₕₕ‖ > 1, gradients blow up, causing NaN losses. Gradient clipping — scaling the gradient when ‖g‖ > threshold — is the standard fix for explosions. Clipping does not fix vanishing gradients; that requires architectural changes (LSTM/GRU) or careful initialisation.

## Full BPTT vs Truncated BPTT

Full BPTT unrolls the entire sequence of T steps. For T=1000 and H=512, storing all hidden states requires 1000×512×4 bytes ≈ 2 MB per sequence (per batch element). More importantly, the backward pass is also sequential over T steps. Truncated BPTT (TBPTT) limits the backward pass to the last k steps: the sequence is split into chunks of size k, the hidden state is carried forward (without gradient) from one chunk to the next, and backpropagation only goes k steps back. This reduces memory to O(k·H) and enables approximate but practical training.

```python
import numpy as np

np.random.seed(7)
T, I, H = 40, 4, 8
Whh_scale = 0.5   # vanishing regime for clear demonstration

Wxh = np.random.randn(H, I) * 0.1
Whh = np.random.randn(H, H) * Whh_scale / np.sqrt(H)
bh  = np.zeros((H, 1))
xs  = [np.random.randn(I, 1) for _ in range(T)]

def forward_all(xs, h0):
    hs = {-1: h0}
    for t, x in enumerate(xs):
        hs[t] = np.tanh(Wxh @ x + Whh @ hs[t-1] + bh)
    return hs

def bptt_gradient(xs, hs, k_back):
    dh = np.ones((H, 1)) / H; dW = np.zeros_like(Whh)
    T_chunk = len(xs)
    for t in reversed(range(max(0, T_chunk - k_back), T_chunk)):
        dt = (1 - hs[t]**2) * dh
        dW += dt @ hs[t-1].T
        dh  = Whh.T @ dt
    return dW

hs_full = forward_all(xs, np.zeros((H, 1)))
dW_full = bptt_gradient(xs, hs_full, T)   # full BPTT

print(f'Full BPTT (k={T}): dWhh norm = {np.linalg.norm(dW_full):.6f}')
for k in [5, 10, 20, T]:
    dW_k = bptt_gradient(xs, hs_full, k)
    cos  = np.dot(dW_full.ravel(), dW_k.ravel()) / (
               np.linalg.norm(dW_full) * np.linalg.norm(dW_k) + 1e-9)
    print(f'  Truncated k={k:2d}: cosine similarity={cos:.4f}, norm={np.linalg.norm(dW_k):.4f}')
```

## Detaching Hidden State

In PyTorch, h.detach() creates a new tensor that shares the same data but has no gradient tracking. When passed as the initial state to the next chunk, gradients from that chunk cannot flow back through the detached tensor into the previous chunk's computation graph. This is essential for memory-efficient training of long sequences: without detach, the backward pass would need to traverse the entire accumulated graph, defeating the purpose of chunking. The pattern is: h = h.detach() before each chunk's forward pass.

```python
import torch
import torch.nn as nn

torch.manual_seed(42)
T, chunk, I, H, O, B = 100, 20, 8, 32, 4, 4

rnn = nn.RNN(I, H, batch_first=True)
fc  = nn.Linear(H, O)
opt = torch.optim.Adam(list(rnn.parameters()) + list(fc.parameters()), lr=1e-3)
x   = torch.randn(B, T, I)
y   = torch.randn(B, T, O)

total_loss = 0.0
h = torch.zeros(1, B, H)
for start in range(0, T, chunk):
    xc   = x[:, start:start + chunk, :]
    yc   = y[:, start:start + chunk, :]
    h_in = h.detach()          # stop gradient from flowing into prev chunk
    opt.zero_grad()
    out, h = rnn(xc, h_in)
    loss = nn.functional.mse_loss(fc(out), yc)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(rnn.parameters(), max_norm=1.0)
    opt.step()
    total_loss += loss.item()

n_chunks = T // chunk
print(f'TBPTT training: {n_chunks} chunks x {chunk} steps')
print(f'Avg chunk loss: {total_loss / n_chunks:.6f}')
print('h.detach() breaks gradient graph -- memory is O(chunk * H) per step.')
print(f'Savings vs full BPTT: {T // chunk}x less graph nodes to store.')
```

## Memory Requirements

Full BPTT must store all T hidden states for the backward pass: O(T·H·B·4) bytes (float32). For T=1000, H=512, B=32: 1000×512×32×4 ≈ 64 MB per layer. Truncated BPTT with chunk k stores only k hidden states: O(k·H·B·4) bytes. Additionally, storing raw pre-activation values for backpropagating through tanh doubles this estimate. Gradient checkpointing can trade recomputation for memory, storing only every √T hidden state and recomputing the rest during backward — reducing memory to O(√T·H) at the cost of ~1.5x forward passes.

> **Gradient Clipping Is Essential**: Always apply gradient clipping when training RNNs. The standard threshold is max_norm=1.0 to 5.0 (use torch.nn.utils.clip_grad_norm_). Without clipping, a single step with ‖Wₕₕ‖>1 can cause explosive gradient growth, resulting in NaN parameters. Clipping does not prevent vanishing gradients — for that, use LSTM/GRU architectures or gradient highway connections.

## Gradient Clipping

Gradient clipping rescales the gradient vector when its norm exceeds a threshold: if ‖g‖ > θ, set g ← g·(θ/‖g‖). This preserves gradient direction while bounding its magnitude. The threshold θ is a hyperparameter typically set between 1.0 and 10.0; lower values are safer but may slow convergence. Global clipping (across all parameters) is preferred over per-parameter clipping. Monitoring the fraction of steps where clipping activates is useful diagnostics: >50% activation suggests the threshold is too low; 0% means it may be too high or gradients are well-behaved.

| Method | Memory | Gradient Quality | Parallelizable | Long-Range Capture |
| --- | --- | --- | --- | --- |
| Full BPTT | O(T·H·B) — stores all hidden states | Exact gradient | No — sequential unroll over T | Yes — gradient flows from t=T to t=0 |
| Truncated BPTT (k) | O(k·H·B) — only k states | Approximation — local gradient only | No — still sequential | Only within k steps; no signal for lag > k |
| Real-Time Recurrent Learning | O(H²) per step — online | Exact but online (per-step) | Yes — one step at a time | Yes — H² parameter gradients per step |

- Full BPTT: exact gradients but O(T) memory and time; infeasible for T > a few hundred.
- Truncated BPTT: standard in practice; chunk sizes of 35–256 are common; gradient is biased for long lags.
- Gradient checkpointing: O(sqrt(T)) memory, 1.5x compute; useful when T is large but not extreme.
- RTRL: online learning with exact gradients but O(H^4) compute per step — only practical for tiny H.
- Gradient clipping (max_norm=1-5): prevents explosions; mandatory for stable RNN training.
- Orthogonal Whh init: spectral radius = 1 at initialisation; delays vanishing gradient onset.

---

