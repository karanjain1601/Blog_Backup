---
title: "RealNVP — Affine Coupling Layers for Image Flows"
slug: "realnvp"
description: "RealNVP (Dinh et al. 2016) extends NICE with affine coupling layers y2 = x2 * exp(s(x1)) + t(x1), alternating checkerboard and channel-wise masks, a multi-scale architecture that factors out half the channels at each scale, and achieves competitive bits-per-dim on CIFAR-10 and CelebA."
tags: ["deep-learning", "generative-models", "gans", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVhbE5WUCAoUmVhbC12YWx1ZWQgTm9uLVZvbHVtZSBQcmVzZXJ2aW5nIHRyYW5zZm9ybWF0aW9ucywgRGluaCBldCBhbC4gMjAxNikgaXMgdGhlIGZpcnN0IG5vcm1hbGl6aW5nIGZsb3cgdG8gYWNoaWV2ZSBoaWdoLXF1YWxpdHkgaW1hZ2UgZ2VuZXJhdGlvbiBhdCBtb2RlcmF0ZSByZXNvbHV0aW9uLiBJdCBleHRlbmRzIE5JQ0VcdTAwMjdzIGFkZGl0aXZlIGNvdXBsaW5nIHdpdGggYWZmaW5lIGNvdXBsaW5nIOKAlCBhZGRpbmcgYSBsZWFybmVkIHNjYWxlIGZhY3RvciBleHAocyh44oKBKSkgdGhhdCBtYWtlcyB0aGUgbWFwcGluZyBub24tdm9sdW1lLXByZXNlcnZpbmcgYW5kIHN0cmljdGx5IG1vcmUgZXhwcmVzc2l2ZS4gVGhlIGFmZmluZSBjb3VwbGluZyBsYXllciwgY29tYmluZWQgd2l0aCBhbHRlcm5hdGluZyBjaGVja2VyYm9hcmQgYW5kIGNoYW5uZWwtd2lzZSBtYXNrcyBhbmQgYSBtdWx0aS1zY2FsZSBhcmNoaXRlY3R1cmUgdGhhdCBwcm9ncmVzc2l2ZWx5IGZhY3RvcnMgb3V0IGRpbWVuc2lvbnMsIGFsbG93ZWQgUmVhbE5WUCB0byBhY2hpZXZlIDMuNDkgYml0cy9kaW0gb24gQ0lGQVItMTAgYW5kIGdlbmVyYXRlIHJlY29nbmlzYWJsZSBmYWNlIGltYWdlcyBvbiBDZWxlYkEgNjTDlzY0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFmZmluZSBDb3VwbGluZyBMYXllciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW4gYWZmaW5lIGNvdXBsaW5nIGxheWVyIHNwbGl0cyB0aGUgaW5wdXQgeCBpbnRvIHR3byBoYWx2ZXMgW3jigoEsIHjigoJdLiBUaGUgZmlyc3QgaGFsZiBwYXNzZXMgdGhyb3VnaCB1bmNoYW5nZWQ6IHnigoEgPSB44oKBLiBUaGUgc2Vjb25kIGhhbGYgaXMgdHJhbnNmb3JtZWQgYnkgYSBsZWFybmVkIHNjYWxlIGFuZCBzaGlmdDogeeKCgiA9IHjigoIg4oqZIGV4cChzKHjigoEpKSArIHQoeOKCgSksIHdoZXJlIHMgYW5kIHQgYXJlIHRoZSBvdXRwdXRzIG9mIGFyYml0cmFyeSBuZXVyYWwgbmV0d29ya3MgdGFraW5nIHjigoEgYXMgaW5wdXQuIFRoZSBKYWNvYmlhbiBpcyBsb3dlci10cmlhbmd1bGFyIHdpdGggZXhwKHMoeOKCgSkpIG9uIHRoZSBkaWFnb25hbCBlbnRyaWVzIGNvcnJlc3BvbmRpbmcgdG8geOKCgi4gVGh1cyBsb2d8ZGV0IEp8ID0gzqPhtaIgc+G1oih44oKBKSDigJQgdGhlIHN1bSBvZiBsb2ctc2NhbGVzLiBJbnZlcnNpb24gaXM6IHjigoIgPSAoeeKCgiDiiJIgdCh54oKBKSkg4oqZIGV4cCjiiJJzKHnigoEpKSwgY29tcHV0ZWQgaW4gYSBzaW5nbGUgZm9yd2FyZCBwYXNzIHRocm91Z2ggdGhlIHNhbWUgcyBhbmQgdCBuZXR3b3Jrcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgQWZmaW5lQ291cGxpbmcobm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdSZWFsTlZQIGFmZmluZSBjb3VwbGluZzogeTIgPSB4MiAqIGV4cChzKHgxKSkgKyB0KHgxKS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCwgaGlkZGVuPTEyOCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBkMSA9IGQgLy8gMjsgc2VsZi5kMSA9IGQxXG4gICAgICAgIHNlbGYuc3QgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGQxLCBoaWRkZW4pLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCBoaWRkZW4pLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCAoZCAtIGQxKSAqIDIpKSAgIyBvdXRwdXRzIFtzOyB0XSBjb25jYXRlbmF0ZWRcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICB4MSwgeDIgPSB4WzosIDpzZWxmLmQxXSwgeFs6LCBzZWxmLmQxOl1cbiAgICAgICAgc3QgPSBzZWxmLnN0KHgxKTsgcywgdCA9IHN0LmNodW5rKDIsIGRpbT0xKVxuICAgICAgICBzICA9IHRvcmNoLnRhbmgocykgICAgICAgICAgIyBib3VuZCBzIGZvciBudW1lcmljYWwgc3RhYmlsaXR5XG4gICAgICAgIHkxID0geDEgICAgICAgICAgICAgICAgICAgICAjIGlkZW50aXR5IHBhc3N0aHJvdWdoXG4gICAgICAgIHkyID0geDIgKiB0b3JjaC5leHAocykgKyB0ICMgYWZmaW5lIHRyYW5zZm9ybVxuICAgICAgICBsb2dfZGV0ID0gcy5zdW0oZGltPTEpICAgICAgIyBzdW0gb2YgbG9nLXNjYWxlc1xuICAgICAgICByZXR1cm4gdG9yY2guY2F0KFt5MSwgeTJdLCBkaW09MSksIGxvZ19kZXRcblxuICAgIGRlZiBpbnZlcnNlKHNlbGYsIHkpOlxuICAgICAgICB5MSwgeTIgPSB5WzosIDpzZWxmLmQxXSwgeVs6LCBzZWxmLmQxOl1cbiAgICAgICAgc3QgPSBzZWxmLnN0KHkxKTsgcywgdCA9IHN0LmNodW5rKDIsIGRpbT0xKVxuICAgICAgICBzICA9IHRvcmNoLnRhbmgocylcbiAgICAgICAgeDIgPSAoeTIgLSB0KSAqIHRvcmNoLmV4cCgtcykgICAjIGludmVydCBhZmZpbmVcbiAgICAgICAgcmV0dXJuIHRvcmNoLmNhdChbeTEsIHgyXSwgZGltPTEpXG5cbmxheWVyID0gQWZmaW5lQ291cGxpbmcoZD04KVxueCA9IHRvcmNoLnJhbmRuKDQsIDgpXG55LCBsZCA9IGxheWVyKHgpXG5wcmludChcdTAwMjdsb2d8ZGV0IEp8Olx1MDAyNywgbGQudG9saXN0KCkpXG5wcmludChcdTAwMjdSZWNvbnN0cnVjdGlvbiBlcnJvcjpcdTAwMjcsICh4IC0gbGF5ZXIuaW52ZXJzZSh5KSkuYWJzKCkubWF4KCkuaXRlbSgpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFsdGVybmF0aW5nIENoZWNrZXJib2FyZCBhbmQgQ2hhbm5lbCBNYXNrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBzaW5nbGUgY291cGxpbmcgbGF5ZXIgb25seSB0cmFuc2Zvcm1zIGhhbGYgb2YgdGhlIGRpbWVuc2lvbnMuIFRvIGFsbG93IGFsbCBkaW1lbnNpb25zIHRvIGludGVyYWN0LCBSZWFsTlZQIGFsdGVybmF0ZXMgYmV0d2VlbiBkaWZmZXJlbnQgbWFza3MuIEZvciAyRCBpbWFnZXMsIGl0IHVzZXMgY2hlY2tlcmJvYXJkIG1hc2tzOiBwaXhlbHMgYXQgcG9zaXRpb25zIHdoZXJlIChpK2opIGlzIGV2ZW4gZm9ybSBncm91cCBBOyBvdGhlcnMgZm9ybSBncm91cCBCLiBTdWNjZXNzaXZlIGNvdXBsaW5nIGxheWVycyBhbHRlcm5hdGUgYmV0d2VlbiBBLW1hc2tlZCBhbmQgQi1tYXNrZWQsIGVuc3VyaW5nIGV2ZXJ5IHBpeGVsIGlzIHRyYW5zZm9ybWVkIGluIGFsdGVybmF0ZSBsYXllcnMuIEFmdGVyIHRocmVlIGNoZWNrZXJib2FyZC1tYXNrZWQgbGF5ZXJzLCB0aGUgc3BhdGlhbCBkaW1lbnNpb25zIGFyZSByZXNoYXBlZCB0byBjaGFubmVsLXdpc2Ugc3BsaXRzLCBhbmQgdGhlIHBhdHRlcm4gc3dpdGNoZXMgdG8gY2hhbm5lbC13aXNlIGFsdGVybmF0aW9uIGZvciBkZWVwZXIgbGF5ZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGNoZWNrZXJib2FyZF9tYXNrKGgsIHcsIHN0YXJ0PTAsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0NoZWNrZXJib2FyZCBzcGF0aWFsIG1hc2s6IDEgYXQgKGksaikgd2hlcmUgKGkraitzdGFydCkgaXMgZXZlbi5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICByb3dzID0gdG9yY2guYXJhbmdlKGgsIGRldmljZT1kZXZpY2UpLnVuc3F1ZWV6ZSgxKSAgIyAoSCwxKVxuICAgIGNvbHMgPSB0b3JjaC5hcmFuZ2UodywgZGV2aWNlPWRldmljZSkudW5zcXVlZXplKDApICAjICgxLFcpXG4gICAgcmV0dXJuICgocm93cyArIGNvbHMgKyBzdGFydCkgJSAyKS5mbG9hdCgpICAgICAgICAgICAjIChILFcpXG5cbmRlZiBhcHBseV9tYXNrX2NvdXBsaW5nKHgsIG1hc2ssIGNvdXBsaW5nX2ZuKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdBcHBseSBjb3VwbGluZyBsYXllciB3aXRoIGdpdmVuIHNwYXRpYWwgbWFzay5cbiAgICB4OiAoQixDLEgsVyk7IG1hc2s6IChILFcpIGJpbmFyeSBtYXNrLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIG1hc2sgPSBtYXNrLnVuc3F1ZWV6ZSgwKS51bnNxdWVlemUoMCkgICAjICgxLDEsSCxXKSBicm9hZGNhc3RcbiAgICB4X3Bhc3MgID0geCAqIG1hc2sgICAgICAgICAgICAgICAgICAgICAgIyBtYXNrZWQgKHBhc3N0aHJvdWdoKSBwYXJ0XG4gICAgeF90cmFucyA9IHggKiAoMSAtIG1hc2spICAgICAgICAgICAgICAgIyBwYXJ0IHRvIGJlIHRyYW5zZm9ybWVkXG4gICAgcmV0dXJuIHhfcGFzcywgeF90cmFuc1xuXG5tYXNrX2EgPSBjaGVja2VyYm9hcmRfbWFzayg0LCA0LCBzdGFydD0wKVxubWFza19iID0gY2hlY2tlcmJvYXJkX21hc2soNCwgNCwgc3RhcnQ9MSlcbnByaW50KFx1MDAyN01hc2sgQTpcXG5cdTAwMjcsIG1hc2tfYS5udW1weSgpKVxucHJpbnQoXHUwMDI3Q29tcGxlbWVudCBjaGVjazpcdTAwMjcsIChtYXNrX2EgKyBtYXNrX2IgPT0gMSkuYWxsKCkuaXRlbSgpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik11bHRpLVNjYWxlIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVhbE5WUCBpbnRyb2R1Y2VzIGEgbXVsdGktc2NhbGUgYXJjaGl0ZWN0dXJlIHRvIHByb2dyZXNzaXZlbHkgY29tcHJlc3MgdGhlIHJlcHJlc2VudGF0aW9uLiBBZnRlciBldmVyeSB0d28gY291cGxpbmcgbGF5ZXJzIGF0IGEgZ2l2ZW4gc3BhdGlhbCBzY2FsZSwgaGFsZiBvZiB0aGUgY2hhbm5lbHMgYXJlIGZhY3RvcmVkIG91dCAocGFzc2VkIGRpcmVjdGx5IHRvIHRoZSBwcmlvcikgYW5kIHRoZSBzcGF0aWFsIGRpbWVuc2lvbnMgYXJlIHNxdWVlemVkICgyw5cyIGJsb2NrcyByZXNoYXBlZCB0byA0w5cgY2hhbm5lbHMpLiBUaGUgcmVtYWluaW5nIGhhbGYgaXMgcHJvY2Vzc2VkIGF0IHRoZSBuZXh0IHNjYWxlIHdpdGggYWRkaXRpb25hbCBjb3VwbGluZyBsYXllcnMuIFRoaXMgaXMgdGhlIFx1MDAyN3NxdWVlemluZ1x1MDAyNyBvcGVyYXRpb246IChCLEMsSCxXKSDihpIgKEIsNEMsSC8yLFcvMikuIFRoaXMgcmVkdWNlcyBtZW1vcnksIGFsbG93cyBncmFkaWVudHMgdG8gcmVhY2ggZWFybHkgbGF5ZXJzIGVmZmljaWVudGx5LCBhbmQgZ2l2ZXMgdGhlIG1vZGVsIGEgY29hcnNlLXRvLWZpbmUgZ2VuZXJhdGl2ZSBzdHJ1Y3R1cmUgc2ltaWxhciB0byBMYXBsYWNpYW4gcHlyYW1pZHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE11bHRpU2NhbGVGbG93KG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3UmVhbE5WUCBtdWx0aS1zY2FsZTogZmFjdG9yIG91dCBoYWxmIGNoYW5uZWxzIGF0IGVhY2ggc2NhbGUuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGQ9MTYsIG5fc2NhbGVzPTMsIGhpZGRlbj02NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmNvdXBsaW5ncyA9IG5uLk1vZHVsZUxpc3QoKVxuICAgICAgICBjdXJfZCA9IGRcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9zY2FsZXMpOlxuICAgICAgICAgICAgIyBUd28gY291cGxpbmcgbGF5ZXJzIHBlciBzY2FsZSAoYWx0ZXJuYXRpbmcgbWFza3MpXG4gICAgICAgICAgICBzZWxmLmNvdXBsaW5ncy5hcHBlbmQoQWZmaW5lQ291cGxpbmcoY3VyX2QsIGhpZGRlbj1oaWRkZW4pKVxuICAgICAgICAgICAgc2VsZi5jb3VwbGluZ3MuYXBwZW5kKEFmZmluZUNvdXBsaW5nKGN1cl9kLCBoaWRkZW49aGlkZGVuKSlcbiAgICAgICAgICAgIGN1cl9kID0gY3VyX2QgLy8gMiAgICMgZmFjdG9yIG91dCBoYWxmIGRpbWVuc2lvbnNcbiAgICAgICAgc2VsZi5uX3NjYWxlcyA9IG5fc2NhbGVzXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgel9wYXJ0cywgbG9nX2RldCA9IFtdLCB0b3JjaC56ZXJvcyh4LnNpemUoMCkpXG4gICAgICAgIGggPSB4XG4gICAgICAgIGlkeCA9IDBcbiAgICAgICAgZm9yIHNjYWxlIGluIHJhbmdlKHNlbGYubl9zY2FsZXMpOlxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2UoMik6ICAgIyB0d28gY291cGxpbmdzIHBlciBzY2FsZVxuICAgICAgICAgICAgICAgIGgsIGxkID0gc2VsZi5jb3VwbGluZ3NbaWR4XShoKTsgbG9nX2RldCArPSBsZDsgaWR4ICs9IDFcbiAgICAgICAgICAgIHNwbGl0ID0gaC5zaXplKDEpIC8vIDJcbiAgICAgICAgICAgIHpfcGFydHMuYXBwZW5kKGhbOiwgOnNwbGl0XSlcbiAgICAgICAgICAgIGggPSBoWzosIHNwbGl0Ol0gICAgICMgY29udGludWUgd2l0aCByZW1haW5pbmcgZGltc1xuICAgICAgICB6X3BhcnRzLmFwcGVuZChoKVxuICAgICAgICByZXR1cm4gdG9yY2guY2F0KHpfcGFydHMsIGRpbT0xKSwgbG9nX2RldFxuXG5mbG93ID0gTXVsdGlTY2FsZUZsb3coZD0xNiwgbl9zY2FsZXM9MywgaGlkZGVuPTMyKVxueCA9IHRvcmNoLnJhbmRuKDQsIDE2KVxueiwgbGQgPSBmbG93KHgpXG5wcmludChcdTAwMjd6IHNoYXBlOiB7fSAgbG9nX2RldCBtZWFuOiB7Oi4zZn1cdTAwMjcuZm9ybWF0KHouc2hhcGUsIGxkLm1lYW4oKS5pdGVtKCkpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxvZy1EZXRlcm1pbmFudCBhbmQgVHJhaW5pbmcgT2JqZWN0aXZlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmFpbmluZyBSZWFsTlZQIG1heGltaXNlcyBsb2cgcF9YKHgpID0gbG9nIHBfWih6KSArIM6jIGxvZ3xkZXQgSuKClnwgPSBsb2cgTih6OzAsSSkgKyDOo+KCliDOo+G1oiBz4oKW4bWiKHjigoEpLiBUaGUgbG9nLWRldGVybWluYW50IHRlcm0gzqMgc+G1oih44oKBKSBpcyBjb21wdXRlZCBieSBzdW1taW5nIGxvZy1zY2FsZXMgZnJvbSBldmVyeSBhZmZpbmUgY291cGxpbmcgbGF5ZXIuIFRhbmggaXMgYXBwbGllZCB0byBzIHRvIGJvdW5kIHRoZSBsb2ctc2NhbGVzIOKAlCBwcmV2ZW50aW5nIGV4cChzKSBmcm9tIGJlY29taW5nIHRvbyBsYXJnZSBvciB0b28gc21hbGwuIERlZXAgUmVzTmV0IGFyY2hpdGVjdHVyZXMgYXJlIHVzZWQgZm9yIHRoZSBzIGFuZCB0IG5ldHdvcmtzIHdpdGhpbiBlYWNoIGNvdXBsaW5nIGxheWVyLiBCYXRjaCBub3JtYWxpc2F0aW9uIGlzIGFwcGxpZWQgYmV0d2VlbiBjb3VwbGluZyBsYXllcnMgaW4gdGhlIG9yaWdpbmFsIHBhcGVyOyBsYXRlciB3b3JrcyBwcmVmZXIgQWN0Tm9ybSAoZGF0YS1kZXBlbmRlbnQgaW5pdGlhbGlzYXRpb24gdG8gdW5pdCBhY3RpdmF0aW9uIHN0YXRpc3RpY3MpLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiQ291cGxpbmcgdnMgQXV0b3JlZ3Jlc3NpdmU6IFBhcmFsbGVsaXNtIFRyYWRlLW9mZiIsImNvbnRlbnQiOiJBZmZpbmUgY291cGxpbmcgKFJlYWxOVlApOiBib3RoIGZvcndhcmQgKGRlbnNpdHkgZXZhbHVhdGlvbikgYW5kIGludmVyc2UgKHNhbXBsaW5nKSBydW4gaW4gcGFyYWxsZWwg4oCUIGFsbCBkaW1lbnNpb25zIGNvbXB1dGVkIHNpbXVsdGFuZW91c2x5IHBlciBsYXllci4gQXV0b3JlZ3Jlc3NpdmUgKE1BRik6IGZvcndhcmQgcGFzcyBpcyBwYXJhbGxlbCAoZXZhbHVhdGUgYWxsIHPhtaIgc2ltdWx0YW5lb3VzbHkgdmlhIE1BREUpLCBidXQgaW52ZXJzaW9uIHJlcXVpcmVzIGQgc2VxdWVudGlhbCBwYXNzZXMuIElBRiByZXZlcnNlcyB0aGlzLiBGb3IgZ2VuZXJhdGl2ZSBhcHBsaWNhdGlvbnMgKGZhc3Qgc2FtcGxpbmcpLCBSZWFsTlZQL0dsb3dcdTAwMjdzIGNvdXBsaW5nIGxheWVycyBhcmUgcHJlZmVyYWJsZS4gRm9yIGRlbnNpdHkgZXN0aW1hdGlvbiBhcHBsaWNhdGlvbnMsIE1BRlx1MDAyN3MgcGFyYWxsZWwgZm9yd2FyZCBwYXNzIGlzIGZpbmUuIEdsb3cgKEtpbmdtYSBcdTAwMjYgRGhhcml3YWwgMjAxOCkgYWRkcyAxw5cxIGludmVydGlibGUgY29udm9sdXRpb25zIHRvIFJlYWxOVlAgZm9yIGZ1bGwgbWl4aW5nLCBhY2hpZXZpbmcgMy4zNSBiaXRzL2RpbSBvbiBDSUZBUi0xMC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTYW1wbGUgR2VuZXJhdGlvbiBmcm9tIFJlYWxOVlAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIGdlbmVyYXRlIGEgbmV3IGltYWdlOiBzYW1wbGUgeiB+IE4oMCxJKSBhdCB0aGUgc2FtZSBkaW1lbnNpb25hbGl0eSBhcyB4LCB0aGVuIGFwcGx5IHRoZSBpbnZlcnNlIG9mIGVhY2ggY291cGxpbmcgbGF5ZXIgaW4gcmV2ZXJzZSBvcmRlci4gRm9yIGFmZmluZSBjb3VwbGluZywgdGhlIGludmVyc2UgeOKCgiA9ICh54oKCIOKIkiB0KHnigoEpKSDiipkgZXhwKOKIknMoeeKCgSkpIGlzIGFuYWx5dGljYWxseSBleGFjdCBhbmQgcmVxdWlyZXMgb25lIGZvcndhcmQgcGFzcyB0aHJvdWdoIHRoZSBzLHQgbmV0d29ya3MgKG5vdCBhIHNlcGFyYXRlIGludmVyc2lvbiBuZXR3b3JrKS4gQWxsIGRpbWVuc2lvbnMgYXJlIGNvbXB1dGVkIGluIHBhcmFsbGVsLiBGb3IgbXVsdGktc2NhbGUgbW9kZWxzLCB0aGUgZmFjdG9yZWQtb3V0IHogcGFydHMgYXJlIG1hcHBlZCBiYWNrIHRocm91Z2ggdGhlaXIgcmVzcGVjdGl2ZSBpbnZlcnNlIHNjYWxlcy4gUmVkdWNpbmcgdGhlIHRlbXBlcmF0dXJlIChzY2FsaW5nIHogYnkgz4QgXHUwMDNjIDEpIGdpdmVzIHNoYXJwZXIgYnV0IGxlc3MgZGl2ZXJzZSBzYW1wbGVzIOKAlCBhbmFsb2dvdXMgdG8gdGhlIHRydW5jYXRpb24gdHJpY2sgaW4gQmlnR0FOLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIHJlYWxudnBfZ2VuZXJhdGUoZmxvdywgbj04LCB0ZW1wZXJhdHVyZT0xLjApOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0dlbmVyYXRlIHNhbXBsZXM6IHogfiBOKDAsSSkqdGVtcCwgYXBwbHkgaW52ZXJzZSBjb3VwbGluZ3MuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZmxvdy5ldmFsKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgeiA9IHRvcmNoLnJhbmRuKG4sIDE2KSAqIHRlbXBlcmF0dXJlICAjIHNjYWxlIGJ5IHRlbXAgZm9yIHF1YWxpdHlcbiAgICAgICAgIyBJbnZlcnQgbXVsdGktc2NhbGUgZmxvd1xuICAgICAgICB6X3BhcnRzID0gdG9yY2guc3BsaXQoeiwgWzIsIDIsIDQsIDhdLCBkaW09MSlcbiAgICAgICAgaCA9IHpfcGFydHNbLTFdICAgICAgICAgICAjIHN0YXJ0IGZyb20gZmluYWwgKHNtYWxsZXN0KSBwYXJ0XG4gICAgICAgIGZvciBzY2FsZSBpbiByYW5nZShmbG93Lm5fc2NhbGVzIC0gMSwgLTEsIC0xKTpcbiAgICAgICAgICAgIGggPSB0b3JjaC5jYXQoW3pfcGFydHNbc2NhbGVdLCBoXSwgZGltPTEpXG4gICAgICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCAtMSwgLTEpOiAgIyByZXZlcnNlIHR3byBjb3VwbGluZ3MgcGVyIHNjYWxlXG4gICAgICAgICAgICAgICAgaWR4ID0gc2NhbGUgKiAyICsgaVxuICAgICAgICAgICAgICAgIGggPSBmbG93LmNvdXBsaW5nc1tpZHhdLmludmVyc2UoaClcbiAgICAgICAgc2FtcGxlcyA9IGhcbiAgICBwcmludChcdTAwMjdHZW5lcmF0ZWQge30gc2FtcGxlcywgc2hhcGU6IHt9XHUwMDI3LmZvcm1hdChuLCBzYW1wbGVzLnNoYXBlKSlcbiAgICBwcmludChcdTAwMjcgIG1lYW49ezouNGZ9ICBzdGQ9ezouNGZ9XHUwMDI3LmZvcm1hdChcbiAgICAgICAgICBzYW1wbGVzLm1lYW4oKS5pdGVtKCksIHNhbXBsZXMuc3RkKCkuaXRlbSgpKSlcbiAgICByZXR1cm4gc2FtcGxlc1xuXG5mbG93ID0gTXVsdGlTY2FsZUZsb3coZD0xNiwgbl9zY2FsZXM9MywgaGlkZGVuPTMyKVxuc2FtcGxlcyA9IHJlYWxudnBfZ2VuZXJhdGUoZmxvdywgbj04LCB0ZW1wZXJhdHVyZT0wLjgpXG5wcmludChcdTAwMjdUZW1wZXJhdHVyZSAwLjg6IHNoYXJwZXIgKGxlc3MgZGl2ZXJzZSkgdGhhbiBmdWxsLXRlbXBlcmF0dXJlIHNhbXBsaW5nLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCaXRzLVBlci1EaW0gRXZhbHVhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQml0cy1wZXItZGltIChCUEQpIGlzIHRoZSBzdGFuZGFyZCBtZXRyaWMgZm9yIG5vcm1hbGl6aW5nIGZsb3dzIG9uIGltYWdlIGJlbmNobWFya3M6IEJQRCA9IOKIkmxvZ+KCgiBwKHgpIC8gRCB3aGVyZSBEIGlzIHRoZSBudW1iZXIgb2YgcGl4ZWxzw5djaGFubmVscy4gTG93ZXIgQlBEIG1lYW5zIGhpZ2hlciBsaWtlbGlob29kLiBSZWFsTlZQIGFjaGlldmVzIDMuNDkgQlBEIG9uIENJRkFSLTEwLiBHbG93IGFjaGlldmVzIDMuMzUuIEEgdW5pZm9ybSBkaXN0cmlidXRpb24gb3ZlciBbMCwyNTVdIGdpdmVzIDguMCBCUEQuIEEgbW9kZWwgYWNoaWV2aW5nIDAgQlBEIHdvdWxkIG1lbW9yaXNlIHRoZSBkYXRhLiBCUEQgaXMgZGlyZWN0bHkgY29tcGFyYWJsZSBhY3Jvc3MgZmxvdyBtb2RlbHMgYnV0IGluY29tcGFyYWJsZSB0byBHQU5zICh3aGljaCBoYXZlIG5vIGxpa2VsaWhvb2QpLiBGb3IgVkFFcywgdGhlIHJlcG9ydGVkIHZhbHVlIGlzIHR5cGljYWxseSB0aGUgRUxCTy1kZXJpdmVkIEJQRCDigJQgYSBwZXNzaW1pc3RpYyAoaGlnaGVyKSBlc3RpbWF0ZSBvZiB0aGUgdHJ1ZSBCUEQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyIzLjQ5IEJQRDogUmVhbE5WUCBvbiBDSUZBUi0xMCAoMjAxNikg4oCUIGZpcnN0IGZsb3cgdG8gd29yayBvbiBuYXR1cmFsIGltYWdlcyIsIjMuMzUgQlBEOiBHbG93IG9uIENJRkFSLTEwICgyMDE4KSDigJQgYWRkcyAxeDEgaW52ZXJ0aWJsZSBjb252IGZvciBmdWxsIG1peGluZyIsIjIuOTggQlBEOiBGbG93KysgKDIwMTkpIOKAlCB2YXJpYXRpb25hbCBkZXF1YW50aXphdGlvbiBhbmQgbG9naXN0aWMgbWl4dHVyZSBjb3VwbGluZyIsIjguMDAgQlBEOiBVbmlmb3JtIGJhc2VsaW5lIChubyBjb21wcmVzc2lvbiBhdCBhbGwpIiwiVGVtcGVyYXR1cmUgc2FtcGxpbmc6IG11bHRpcGx5IHogYnkgdGF1XHUwMDNjMSBmb3Igc2hhcnBlciBpbWFnZXMsIHRhdVx1MDAzZTEgZm9yIG1vcmUgZGl2ZXJzaXR5IiwiQWN0Tm9ybTogZGF0YS1kZXBlbmRlbnQgaW5pdGlhbGlzYXRpb24gb2Ygbm9ybWFsaXNhdGlvbiBzY2FsZStiaWFzLCByZXBsYWNlcyBiYXRjaCBub3JtIGluIEdsb3ciXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTklDRSB2cyBSZWFsTlZQIHZzIE1BRiB2cyBHbG93IENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJDb3VwbGluZyBUeXBlIiwiUGFyYWxsZWwgU2FtcGxpbmciLCJQYXJhbGxlbCBUcmFpbmluZyIsImxvZy1kZXQgQ29zdCIsIkV4cHJlc3Npdml0eSJdLCJyb3dzIjpbWyJOSUNFICgyMDE0KSIsIkFkZGl0aXZlOiB5Mj14MittKHgxKSIsIlllcyIsIlllcyIsIlplcm8gKHZvbHVtZSBwcmVzZXJ2aW5nKSIsIkxvdyJdLFsiUmVhbE5WUCAoMjAxNikiLCJBZmZpbmU6IHkyPXgyKmV4cChzKSt0IiwiWWVzIiwiWWVzIiwiTyhkKSBzdW0gb2YgbG9nLXNjYWxlcyIsIk1lZGl1bSJdLFsiTUFGICgyMDE3KSIsIkF1dG9yZWdyZXNzaXZlIGFmZmluZSIsIk5vIChzZXF1ZW50aWFsIGQgc3RlcHMpIiwiWWVzIChNQURFKSIsIk8oZCkgZGlhZ29uYWwiLCJIaWdoIl0sWyJHbG93ICgyMDE4KSIsIkFmZmluZSArIDF4MSBpbnZlcnRpYmxlIGNvbnYiLCJZZXMiLCJZZXMiLCJPKGQpICsgTyhDXjMpIHBlciAxeDEiLCJIaWdoIl1dfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# RealNVP — Affine Coupling Layers for Image Flows

RealNVP (Real-valued Non-Volume Preserving transformations, Dinh et al. 2016) is the first normalizing flow to achieve high-quality image generation at moderate resolution. It extends NICE's additive coupling with affine coupling — adding a learned scale factor exp(s(x₁)) that makes the mapping non-volume-preserving and strictly more expressive. The affine coupling layer, combined with alternating checkerboard and channel-wise masks and a multi-scale architecture that progressively factors out dimensions, allowed RealNVP to achieve 3.49 bits/dim on CIFAR-10 and generate recognisable face images on CelebA 64×64.

## Affine Coupling Layer

An affine coupling layer splits the input x into two halves [x₁, x₂]. The first half passes through unchanged: y₁ = x₁. The second half is transformed by a learned scale and shift: y₂ = x₂ ⊙ exp(s(x₁)) + t(x₁), where s and t are the outputs of arbitrary neural networks taking x₁ as input. The Jacobian is lower-triangular with exp(s(x₁)) on the diagonal entries corresponding to x₂. Thus log|det J| = Σᵢ sᵢ(x₁) — the sum of log-scales. Inversion is: x₂ = (y₂ − t(y₁)) ⊙ exp(−s(y₁)), computed in a single forward pass through the same s and t networks.

```python
import torch
import torch.nn as nn

class AffineCoupling(nn.Module):
    '''RealNVP affine coupling: y2 = x2 * exp(s(x1)) + t(x1).'''
    def __init__(self, d, hidden=128):
        super().__init__()
        d1 = d // 2; self.d1 = d1
        self.st = nn.Sequential(
            nn.Linear(d1, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
            nn.Linear(hidden, (d - d1) * 2))  # outputs [s; t] concatenated

    def forward(self, x):
        x1, x2 = x[:, :self.d1], x[:, self.d1:]
        st = self.st(x1); s, t = st.chunk(2, dim=1)
        s  = torch.tanh(s)          # bound s for numerical stability
        y1 = x1                     # identity passthrough
        y2 = x2 * torch.exp(s) + t # affine transform
        log_det = s.sum(dim=1)      # sum of log-scales
        return torch.cat([y1, y2], dim=1), log_det

    def inverse(self, y):
        y1, y2 = y[:, :self.d1], y[:, self.d1:]
        st = self.st(y1); s, t = st.chunk(2, dim=1)
        s  = torch.tanh(s)
        x2 = (y2 - t) * torch.exp(-s)   # invert affine
        return torch.cat([y1, x2], dim=1)

layer = AffineCoupling(d=8)
x = torch.randn(4, 8)
y, ld = layer(x)
print('log|det J|:', ld.tolist())
print('Reconstruction error:', (x - layer.inverse(y)).abs().max().item())
```

## Alternating Checkerboard and Channel Masks

A single coupling layer only transforms half of the dimensions. To allow all dimensions to interact, RealNVP alternates between different masks. For 2D images, it uses checkerboard masks: pixels at positions where (i+j) is even form group A; others form group B. Successive coupling layers alternate between A-masked and B-masked, ensuring every pixel is transformed in alternate layers. After three checkerboard-masked layers, the spatial dimensions are reshaped to channel-wise splits, and the pattern switches to channel-wise alternation for deeper layers.

```python
import torch

def checkerboard_mask(h, w, start=0, device='cpu'):
    '''Checkerboard spatial mask: 1 at (i,j) where (i+j+start) is even.'''
    rows = torch.arange(h, device=device).unsqueeze(1)  # (H,1)
    cols = torch.arange(w, device=device).unsqueeze(0)  # (1,W)
    return ((rows + cols + start) % 2).float()           # (H,W)

def apply_mask_coupling(x, mask, coupling_fn):
    '''Apply coupling layer with given spatial mask.
    x: (B,C,H,W); mask: (H,W) binary mask.'''
    mask = mask.unsqueeze(0).unsqueeze(0)   # (1,1,H,W) broadcast
    x_pass  = x * mask                      # masked (passthrough) part
    x_trans = x * (1 - mask)               # part to be transformed
    return x_pass, x_trans

mask_a = checkerboard_mask(4, 4, start=0)
mask_b = checkerboard_mask(4, 4, start=1)
print('Mask A:\n', mask_a.numpy())
print('Complement check:', (mask_a + mask_b == 1).all().item())
```

## Multi-Scale Architecture

RealNVP introduces a multi-scale architecture to progressively compress the representation. After every two coupling layers at a given spatial scale, half of the channels are factored out (passed directly to the prior) and the spatial dimensions are squeezed (2×2 blocks reshaped to 4× channels). The remaining half is processed at the next scale with additional coupling layers. This is the 'squeezing' operation: (B,C,H,W) → (B,4C,H/2,W/2). This reduces memory, allows gradients to reach early layers efficiently, and gives the model a coarse-to-fine generative structure similar to Laplacian pyramids.

```python
import torch
import torch.nn as nn

class MultiScaleFlow(nn.Module):
    '''RealNVP multi-scale: factor out half channels at each scale.'''
    def __init__(self, d=16, n_scales=3, hidden=64):
        super().__init__()
        self.couplings = nn.ModuleList()
        cur_d = d
        for _ in range(n_scales):
            # Two coupling layers per scale (alternating masks)
            self.couplings.append(AffineCoupling(cur_d, hidden=hidden))
            self.couplings.append(AffineCoupling(cur_d, hidden=hidden))
            cur_d = cur_d // 2   # factor out half dimensions
        self.n_scales = n_scales

    def forward(self, x):
        z_parts, log_det = [], torch.zeros(x.size(0))
        h = x
        idx = 0
        for scale in range(self.n_scales):
            for _ in range(2):   # two couplings per scale
                h, ld = self.couplings[idx](h); log_det += ld; idx += 1
            split = h.size(1) // 2
            z_parts.append(h[:, :split])
            h = h[:, split:]     # continue with remaining dims
        z_parts.append(h)
        return torch.cat(z_parts, dim=1), log_det

flow = MultiScaleFlow(d=16, n_scales=3, hidden=32)
x = torch.randn(4, 16)
z, ld = flow(x)
print('z shape: {}  log_det mean: {:.3f}'.format(z.shape, ld.mean().item()))
```

## Log-Determinant and Training Objective

Training RealNVP maximises log p_X(x) = log p_Z(z) + Σ log|det Jₖ| = log N(z;0,I) + Σₖ Σᵢ sₖᵢ(x₁). The log-determinant term Σ sᵢ(x₁) is computed by summing log-scales from every affine coupling layer. Tanh is applied to s to bound the log-scales — preventing exp(s) from becoming too large or too small. Deep ResNet architectures are used for the s and t networks within each coupling layer. Batch normalisation is applied between coupling layers in the original paper; later works prefer ActNorm (data-dependent initialisation to unit activation statistics).

> **Coupling vs Autoregressive: Parallelism Trade-off**: Affine coupling (RealNVP): both forward (density evaluation) and inverse (sampling) run in parallel — all dimensions computed simultaneously per layer. Autoregressive (MAF): forward pass is parallel (evaluate all sᵢ simultaneously via MADE), but inversion requires d sequential passes. IAF reverses this. For generative applications (fast sampling), RealNVP/Glow's coupling layers are preferable. For density estimation applications, MAF's parallel forward pass is fine. Glow (Kingma & Dhariwal 2018) adds 1×1 invertible convolutions to RealNVP for full mixing, achieving 3.35 bits/dim on CIFAR-10.

## Sample Generation from RealNVP

To generate a new image: sample z ~ N(0,I) at the same dimensionality as x, then apply the inverse of each coupling layer in reverse order. For affine coupling, the inverse x₂ = (y₂ − t(y₁)) ⊙ exp(−s(y₁)) is analytically exact and requires one forward pass through the s,t networks (not a separate inversion network). All dimensions are computed in parallel. For multi-scale models, the factored-out z parts are mapped back through their respective inverse scales. Reducing the temperature (scaling z by τ < 1) gives sharper but less diverse samples — analogous to the truncation trick in BigGAN.

```python
import torch

def realnvp_generate(flow, n=8, temperature=1.0):
    '''Generate samples: z ~ N(0,I)*temp, apply inverse couplings.'''
    flow.eval()
    with torch.no_grad():
        z = torch.randn(n, 16) * temperature  # scale by temp for quality
        # Invert multi-scale flow
        z_parts = torch.split(z, [2, 2, 4, 8], dim=1)
        h = z_parts[-1]           # start from final (smallest) part
        for scale in range(flow.n_scales - 1, -1, -1):
            h = torch.cat([z_parts[scale], h], dim=1)
            for i in range(1, -1, -1):  # reverse two couplings per scale
                idx = scale * 2 + i
                h = flow.couplings[idx].inverse(h)
        samples = h
    print('Generated {} samples, shape: {}'.format(n, samples.shape))
    print('  mean={:.4f}  std={:.4f}'.format(
          samples.mean().item(), samples.std().item()))
    return samples

flow = MultiScaleFlow(d=16, n_scales=3, hidden=32)
samples = realnvp_generate(flow, n=8, temperature=0.8)
print('Temperature 0.8: sharper (less diverse) than full-temperature sampling.')
```

## Bits-Per-Dim Evaluation

Bits-per-dim (BPD) is the standard metric for normalizing flows on image benchmarks: BPD = −log₂ p(x) / D where D is the number of pixels×channels. Lower BPD means higher likelihood. RealNVP achieves 3.49 BPD on CIFAR-10. Glow achieves 3.35. A uniform distribution over [0,255] gives 8.0 BPD. A model achieving 0 BPD would memorise the data. BPD is directly comparable across flow models but incomparable to GANs (which have no likelihood). For VAEs, the reported value is typically the ELBO-derived BPD — a pessimistic (higher) estimate of the true BPD.

- 3.49 BPD: RealNVP on CIFAR-10 (2016) — first flow to work on natural images
- 3.35 BPD: Glow on CIFAR-10 (2018) — adds 1x1 invertible conv for full mixing
- 2.98 BPD: Flow++ (2019) — variational dequantization and logistic mixture coupling
- 8.00 BPD: Uniform baseline (no compression at all)
- Temperature sampling: multiply z by tau<1 for sharper images, tau>1 for more diversity
- ActNorm: data-dependent initialisation of normalisation scale+bias, replaces batch norm in Glow

## NICE vs RealNVP vs MAF vs Glow Comparison

| Model | Coupling Type | Parallel Sampling | Parallel Training | log-det Cost | Expressivity |
| --- | --- | --- | --- | --- | --- |
| NICE (2014) | Additive: y2=x2+m(x1) | Yes | Yes | Zero (volume preserving) | Low |
| RealNVP (2016) | Affine: y2=x2*exp(s)+t | Yes | Yes | O(d) sum of log-scales | Medium |
| MAF (2017) | Autoregressive affine | No (sequential d steps) | Yes (MADE) | O(d) diagonal | High |
| Glow (2018) | Affine + 1x1 invertible conv | Yes | Yes | O(d) + O(C^3) per 1x1 | High |

---

