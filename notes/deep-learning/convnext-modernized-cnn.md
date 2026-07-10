---
title: "ConvNeXt — Modernized CNN Matching ViT Performance"
slug: "convnext-modernized-cnn"
description: "ConvNeXt (Liu et al. 2022): systematically modernize ResNet-50 using Swin Transformer design choices, step by step. Covers patchify stem, inverted bottleneck, depthwise 7×7, LayerNorm, GELU, ConvNeXt V2 with FCMAE, and the conclusion that training recipe + architecture together explain Transformer gains."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udk5lWHQgKExpdSBldCBhbC4sIENWUFIgMjAyMikgYXNrZWQ6IGNhbiBhIHB1cmVseSBjb252b2x1dGlvbmFsIG5ldHdvcmsgbWF0Y2ggU3dpbiBUcmFuc2Zvcm1lciBhY2N1cmFjeSBpZiB3ZSBhZG9wdCB0aGUgc2FtZSBtb2Rlcm4gZGVzaWduIHByaW5jaXBsZXM/IFRoZSBhbnN3ZXIgaXMgeWVzLiBTdGFydGluZyBmcm9tIFJlc05ldC01MCwgdGhlIHBhcGVyIGFwcGxpZXMgc2l4IHRhcmdldGVkIGNoYW5nZXMg4oCUIGFsbCBpbnNwaXJlZCBieSB0aGUgU3dpbiBUcmFuc2Zvcm1lciDigJQgYW5kIHJlY292ZXJzIGEgQ05OIHRoYXQgbWF0Y2hlcyBvciBleGNlZWRzIFN3aW4tVCBhdCBldmVyeSBzY2FsZS4gVGhpcyByZXN1bHQgaGFzIGltcG9ydGFudCBpbXBsaWNhdGlvbnM6IHRoZSBnYWlucyBvZiBWaXNpb24gVHJhbnNmb3JtZXJzIGNvbWUgcGFydGx5IGZyb20gdHJhaW5pbmcgcmVjaXBlIGFuZCBkZXNpZ24gY2hvaWNlcywgbm90IHB1cmVseSBmcm9tIGF0dGVudGlvbiBtZWNoYW5pc21zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vdGl2YXRpb24g4oCUIFRyYW5zZm9ybWVycyB2cyBDTk5zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCeSAyMDIxLCBTd2luIFRyYW5zZm9ybWVyIGhhZCBzdXJwYXNzZWQgUmVzTmV0cyBvbiBJbWFnZU5ldCwgQ09DTywgYW5kIEFERTIwSyB3aXRoIGhpZXJhcmNoaWNhbCBhdHRlbnRpb24gYW5kIHNoaWZ0ZWQgd2luZG93cy4gVGhlIGNvbW1vbiBpbnRlcnByZXRhdGlvbiB3YXMgdGhhdCBzZWxmLWF0dGVudGlvbiBpcyBpbmhlcmVudGx5IHN1cGVyaW9yIHRvIGNvbnZvbHV0aW9uLiBDb252TmVYdCBjaGFsbGVuZ2VzIHRoaXMgaW50ZXJwcmV0YXRpb24gYnkgYXNraW5nIHdoZXRoZXIgdGhlIGFjY3VyYWN5IGdhcCBleGlzdHMgYmVjYXVzZSBvZiBhdHRlbnRpb24sIG9yIGJlY2F1c2Ugb2YgdGhlIG1hbnkgb3RoZXIgZGVzaWduIGRpZmZlcmVuY2VzOiB0cmFpbmluZyByZWNpcGUgKEFkYW1XLCBjb3NpbmUgc2NoZWR1bGUsIGV4dGVuc2l2ZSBhdWdtZW50YXRpb24pLCBtYWNybyBzdHJ1Y3R1cmUgKHN0YWdlIHJhdGlvcywgc3RlbXMsIGRvd25zYW1wbGluZyksIGFuZCBtaWNybyBkZXNpZ24gKG5vcm1hbGl6YXRpb24sIGFjdGl2YXRpb25zLCBrZXJuZWwgc2l6ZSkuIFRoZSBtb2Rlcm5pemF0aW9uIHJvYWRtYXAgYW5zd2VycyB0aGlzIHF1ZXN0aW9uIHN5c3RlbWF0aWNhbGx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBNb2Rlcm5pemF0aW9uIFJvYWQgTWFwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcGFwZXIgc3RhcnRzIHdpdGggUmVzTmV0LTUwICg3Ni4xJSB0b3AtMSkgYW5kIGFkZHMgU3dpbi1pbnNwaXJlZCBjaGFuZ2VzIG9uZSBhdCBhIHRpbWUsIG1lYXN1cmluZyBhY2N1cmFjeSBhZnRlciBlYWNoLiBUaGUgb3JkZXIgaXM6ICgxKSB0cmFpbmluZyByZWNpcGUgKEFkYW1XLCBjb3NpbmUgc2NoZWR1bGUsIE1peHVwLCBDdXRNaXgsIFJhbmRBdWdtZW50LCBMYWJlbCBTbW9vdGhpbmcpIC1cdTAwM2UgNzguOCU7IHRoZW4gYXJjaGl0ZWN0dXJlIGNoYW5nZXMgc3RhcnRpbmcgZnJvbSBtYWNybyBkZXNpZ24gZG93biB0byBtaWNybyBkZXNpZ24uIEVhY2ggc3RlcCBpcyBhYmxhdGVkIGluZGVwZW5kZW50bHksIG1ha2luZyB0aGUgcGFwZXIgYW4gdW51c3VhbGx5IGNsZWFuIGFuYWx5c2lzIG9mIHdoYXQgZHJpdmVzIGFjY3VyYWN5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjp0cnVlLCJpdGVtcyI6WyJQYXRjaGlmeSBzdGVtOiByZXBsYWNlIDfDlzcrTWF4UG9vbCB3aXRoIDTDlzQgc3RyaWRlLTQgQ29udiAobGlrZSBWaVQpIOKAlCBmZXdlciBmb3J3YXJkIHBhc3NlcywgbGVzcyBhZ2dyZXNzaXZlIHNwYXRpYWwgZG93bnNhbXBsaW5nIGF0IHRoZSBzdGFydC4iLCJTdGFnZSByYXRpbyAzOjM6OTozOiBtaXJyb3IgU3dpbi1UIGJsb2NrIGRpc3RyaWJ1dGlvbiAoZmV3ZXIgYmxvY2tzIGluIGVhcmx5IHN0YWdlcywgbW9yZSBpbiBzdGFnZSAzKS4iLCJSZXNOZVh0LWlmeTogcmVwbGFjZSAzw5czIGNvbnYgd2l0aCBkZXB0aHdpc2UgM8OXMyBjb252ICsgaW5jcmVhc2UgY2hhbm5lbCB3aWR0aCAoaW52ZXJ0ZWQgYm90dGxlbmVjayBzdHlsZSkuIiwiSW52ZXJ0ZWQgYm90dGxlbmVjazogZXhwYW5kIGNoYW5uZWxzIDTDlyBpbiB0aGUgbWlkZGxlIGxheWVyIChsaWtlIFRyYW5zZm9ybWVyIE1MUCkgcmF0aGVyIHRoYW4gY29tcHJlc3NpbmcuIiwiTGFyZ2VyIGtlcm5lbDogaW5jcmVhc2UgZGVwdGh3aXNlIGNvbnYgZnJvbSAzw5czIHRvIDfDlzcgKGxpa2UgU3dpblx1MDAyN3MgN8OXNyBhdHRlbnRpb24gd2luZG93KS4iLCJNaWNybyBkZXNpZ246IHJlcGxhY2UgQmF0Y2hOb3JtIHdpdGggTGF5ZXJOb3JtLCByZXBsYWNlIFJlTFUgd2l0aCBHRUxVLCByZWR1Y2UgYWN0aXZhdGlvbnMgdG8gb25lIHBlciBibG9jaywgc2VwYXJhdGUgZG93bnNhbXBsaW5nIGxheWVycyBiZXR3ZWVuIHN0YWdlcy4iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJUcmFpbmluZyBSZWNpcGUgdnMgQXJjaGl0ZWN0dXJlIiwiY29udGVudCI6IlNpbXBseSBhcHBseWluZyBBZGFtVyArIGNvc2luZSBzY2hlZHVsZSArIG1vZGVybiBhdWdtZW50YXRpb24gKE1peHVwLCBDdXRNaXgsIFJhbmRBdWdtZW50LCBMYWJlbCBTbW9vdGhpbmcpIHRvIFJlc05ldC01MCByYWlzZXMgYWNjdXJhY3kgZnJvbSA3Ni4xJSB0byA3OC44JSDigJQgYSAyLjclIGdhaW4gd2l0aCB6ZXJvIGFyY2hpdGVjdHVyYWwgY2hhbmdlLiBUaGlzIHJlc3VsdCByZXZlYWxzIHRoYXQgYSBsYXJnZSBmcmFjdGlvbiBvZiB0aGUgVHJhbnNmb3JtZXIgYWNjdXJhY3kgYWR2YW50YWdlIGlzIGF0dHJpYnV0YWJsZSB0byB0cmFpbmluZyByZWNpcGUsIG5vdCBhcmNoaXRlY3R1cmUuIFRoZSByZW1haW5pbmcgYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzIGFkZCBhIGZ1cnRoZXIgMy4zJSBvbiB0b3AuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udk5lWHQgQmxvY2sgRGVzaWduIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQ29udk5lWHQgYmxvY2sgaXMgc3RydWN0dXJhbGx5IHNpbWlsYXIgdG8gYSBUcmFuc2Zvcm1lciBibG9jazogZGVwdGh3aXNlIDfDlzcgY29udiAoYW5hbG9nb3VzIHRvIGF0dGVudGlvbiBvdmVyIGEgN8OXNyB3aW5kb3cpIGZvbGxvd2VkIGJ5IGEgNMOXIGludmVydGVkIGJvdHRsZW5lY2sgTUxQIChwb2ludHdpc2UgZXhwYW5kIC1cdTAwM2UgR0VMVSAtXHUwMDNlIHBvaW50d2lzZSBjb250cmFjdCkuIE5vcm1hbGl6YXRpb24gdXNlcyBMYXllck5vcm0gYXBwbGllZCBvbiB0aGUgY2hhbm5lbCBheGlzIChhZnRlciBwZXJtdXRpbmcgdG8gQiwgSCwgVywgQykuIFRoZXJlIGlzIG9uZSBHRUxVIGFjdGl2YXRpb24gcGVyIGJsb2NrIChub3Qgb25lIHBlciBsaW5lYXIgbGF5ZXIgYXMgaW4gUmVzTmV0KS4gQSBsYXllciBzY2FsZSBwYXJhbWV0ZXIgzrMgKGluaXRpYWxpemVkIHRvIDFlLTYpIGlzIG9wdGlvbmFsbHkgYXBwbGllZCBiZWZvcmUgdGhlIHJlc2lkdWFsIGFkZGl0aW9uLiBUaGUgZGVwdGh3aXNlIGNvbnYgb3BlcmF0ZXMgYWNyb3NzIHRoZSBzcGF0aWFsIGRpbWVuc2lvbnMgd2hpbGUgdGhlIHBvaW50d2lzZSBsYXllcnMgbWl4IGNoYW5uZWxzIOKAlCBleGFjdGx5IGFzIGluIFRyYW5zZm9ybWVycyB3aGVyZSBhdHRlbnRpb24gbWl4ZXMgcG9zaXRpb25zIGFuZCBNTFAgbWl4ZXMgY2hhbm5lbHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSBFeGFtcGxlcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBDb252TmVYdEJsb2NrKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiQ29udk5lWHQgYmxvY2s6IGRlcHRod2lzZSA3eDcgLVx1MDAzZSBMTiAtXHUwMDNlIHBvaW50d2lzZSBleHBhbmQgLVx1MDAzZSBHRUxVIC1cdTAwM2UgcG9pbnR3aXNlIHByb2plY3QuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbSwgbWxwX3JhdGlvPTQsIGxheWVyX3NjYWxlX2luaXQ9MWUtNik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmR3Y29udiAgPSBubi5Db252MmQoZGltLCBkaW0sIGtlcm5lbF9zaXplPTcsIHBhZGRpbmc9MywgZ3JvdXBzPWRpbSlcbiAgICAgICAgc2VsZi5ub3JtICAgID0gbm4uTGF5ZXJOb3JtKGRpbSwgZXBzPTFlLTYpXG4gICAgICAgIHNlbGYucHdjb252MSA9IG5uLkxpbmVhcihkaW0sIG1scF9yYXRpbyAqIGRpbSlcbiAgICAgICAgc2VsZi5hY3QgICAgID0gbm4uR0VMVSgpXG4gICAgICAgIHNlbGYucHdjb252MiA9IG5uLkxpbmVhcihtbHBfcmF0aW8gKiBkaW0sIGRpbSlcbiAgICAgICAgc2VsZi5nYW1tYSAgID0gbm4uUGFyYW1ldGVyKGxheWVyX3NjYWxlX2luaXQgKiB0b3JjaC5vbmVzKGRpbSkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmVzaWR1YWwgPSB4XG4gICAgICAgIHggPSBzZWxmLmR3Y29udih4KSAgICAgICAgICAgICAgICMgKEIsIEMsIEgsIFcpIC0tIGRlcHRod2lzZSBzcGF0aWFsIG1peGluZ1xuICAgICAgICB4ID0geC5wZXJtdXRlKDAsIDIsIDMsIDEpICAgICAgICMgKEIsIEgsIFcsIEMpIGZvciBMYXllck5vcm1cbiAgICAgICAgeCA9IHNlbGYubm9ybSh4KVxuICAgICAgICB4ID0gc2VsZi5wd2NvbnYxKHgpICAgICAgICAgICAgICAjIGV4cGFuZDogQyAtXHUwMDNlIDRDXG4gICAgICAgIHggPSBzZWxmLmFjdCh4KSAgICAgICAgICAgICAgICAgICMgc2luZ2xlIEdFTFUgKG5vdCBvbmUgcGVyIGxheWVyKVxuICAgICAgICB4ID0gc2VsZi5wd2NvbnYyKHgpICAgICAgICAgICAgICAjIGNvbnRyYWN0OiA0QyAtXHUwMDNlIENcbiAgICAgICAgeCA9IHNlbGYuZ2FtbWEgKiB4XG4gICAgICAgIHggPSB4LnBlcm11dGUoMCwgMywgMSwgMikgICAgICAgIyBiYWNrIHRvIChCLCBDLCBILCBXKVxuICAgICAgICByZXR1cm4gcmVzaWR1YWwgKyB4XG5cbmJsb2NrID0gQ29udk5lWHRCbG9jayhkaW09OTYpXG54ID0gdG9yY2gucmFuZG4oMiwgOTYsIDU2LCA1NilcbnByaW50KGZcIklucHV0OiAge3guc2hhcGV9XCIpXG5wcmludChmXCJPdXRwdXQ6IHtibG9jayh4KS5zaGFwZX1cIilcbnByaW50KGZcIlBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gYmxvY2sucGFyYW1ldGVycygpKTosfVwiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBQYXRjaGlmeVN0ZW0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJSZXBsYWNlIDd4NytNYXhQb29sIHdpdGggYSBzaW5nbGUgNHg0IHN0cmlkZS00IGNvbnYgKGxpa2UgVmlUIHBhdGNoaWZ5KS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2g9Mywgb3V0X2NoPTk2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucHJvaiA9IG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCBrZXJuZWxfc2l6ZT00LCBzdHJpZGU9NClcbiAgICAgICAgc2VsZi5ub3JtID0gbm4uTGF5ZXJOb3JtKG91dF9jaCwgZXBzPTFlLTYpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgeCA9IHNlbGYucHJvaih4KSAgICAgICAgICAgICAgICAgIyAoQiwgQywgSC80LCBXLzQpXG4gICAgICAgIHggPSB4LnBlcm11dGUoMCwgMiwgMywgMSkgICAgICAgIyAoQiwgSC80LCBXLzQsIEMpXG4gICAgICAgIHggPSBzZWxmLm5vcm0oeClcbiAgICAgICAgcmV0dXJuIHgucGVybXV0ZSgwLCAzLCAxLCAyKSAgICAjIChCLCBDLCBILzQsIFcvNClcblxuY2xhc3MgRG93bnNhbXBsZUxheWVyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU2VwYXJhdGUgZG93bnNhbXBsaW5nIGJldHdlZW4gc3RhZ2VzOiBMTiAtXHUwMDNlIDJ4MiBzdHJpZGUtMiBjb252LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgb3V0X2NoKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubm9ybSA9IG5uLkxheWVyTm9ybShpbl9jaCwgZXBzPTFlLTYpXG4gICAgICAgIHNlbGYuY29udiA9IG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCBrZXJuZWxfc2l6ZT0yLCBzdHJpZGU9MilcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICB4ID0geC5wZXJtdXRlKDAsIDIsIDMsIDEpXG4gICAgICAgIHggPSBzZWxmLm5vcm0oeClcbiAgICAgICAgeCA9IHgucGVybXV0ZSgwLCAzLCAxLCAyKVxuICAgICAgICByZXR1cm4gc2VsZi5jb252KHgpXG5cbnN0ZW0gPSBQYXRjaGlmeVN0ZW0oMywgOTYpXG5kb3duID0gRG93bnNhbXBsZUxheWVyKDk2LCAxOTIpXG54ID0gdG9yY2gucmFuZG4oMiwgMywgMjI0LCAyMjQpXG5oID0gc3RlbSh4KVxucHJpbnQoZlwiQWZ0ZXIgcGF0Y2hpZnkgc3RlbToge2guc2hhcGV9XCIpICAgIyAoMiwgOTYsIDU2LCA1NilcbnByaW50KGZcIkFmdGVyIGRvd25zYW1wbGU6ICAgIHtkb3duKGgpLnNoYXBlfVwiKSAgIyAoMiwgMTkyLCAyOCwgMjgpXG5wcmludChcIk5vIE1heFBvb2w6IHNtb290aGVyIHNwYXRpYWwgZG93bnNhbXBsaW5nIHZzIFJlc05ldCBzdGVtXCIpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgbW9kZWxzXG5cbmNvbnZuZXh0ID0gbW9kZWxzLmNvbnZuZXh0X3Rpbnkod2VpZ2h0cz1tb2RlbHMuQ29udk5lWHRfVGlueV9XZWlnaHRzLklNQUdFTkVUMUtfVjEpXG5zd2luX3QgICA9IG1vZGVscy5zd2luX3Qod2VpZ2h0cz1tb2RlbHMuU3dpbl9UX1dlaWdodHMuSU1BR0VORVQxS19WMSlcblxuZGVmIGNvdW50X3BhcmFtcyhtb2RlbCk6XG4gICAgcmV0dXJuIHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKSAvIDFlNlxuXG5tb2RlbHNfaW5mbyA9IFtcbiAgICAoXHUwMDI3Q29udk5lWHQtVGlueVx1MDAyNywgY29udm5leHQsIDgyLjEpLFxuICAgIChcdTAwMjdTd2luLVRcdTAwMjcsICAgICAgICBzd2luX3QsICAgODEuMyksXG5dXG5cbnByaW50KGZcIntcdTAwMjdNb2RlbFx1MDAyNzpcdTAwM2MyMH0ge1x1MDAyN1BhcmFtcyAoTSlcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdPZmZpY2lhbCBUb3AtMVx1MDAyNzpcdTAwM2UxNX0ge1x1MDAyN0F0dGVudGlvbj9cdTAwMjc6XHUwMDNlMTJ9XCIpXG5wcmludChcdTAwMjctXHUwMDI3ICogNjIpXG5mb3IgbmFtZSwgbSwgYWNjIGluIG1vZGVsc19pbmZvOlxuICAgIHByaW50KGZcIntuYW1lOlx1MDAzYzIwfSB7Y291bnRfcGFyYW1zKG0pOlx1MDAzZTEyLjFmfSB7YWNjOlx1MDAzZTE0LjFmfSUge1x1MDAyN05vXHUwMDI3IGlmIFx1MDAyN0NvbnZOZVh0XHUwMDI3IGluIG5hbWUgZWxzZSBcdTAwMjdZZXNcdTAwMjc6XHUwMDNlMTJ9XCIpXG5cbnByaW50KClcbnggPSB0b3JjaC5yYW5kbigxLCAzLCAyMjQsIDIyNClcbmNvbnZuZXh0LmV2YWwoKTsgc3dpbl90LmV2YWwoKVxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgXyA9IGNvbnZuZXh0KHgpXG5wcmludChcIkNvbnZOZVh0LVRpbnkgbWF0Y2hlcyBTd2luLVQgd2l0aCBubyBzZWxmLWF0dGVudGlvbiwgc2ltcGxlciBpbmR1Y3RpdmUgYmlhc1wiKVxucHJpbnQoXCJLZXk6IFRyYW5zZm9ybWVyIGFkdmFudGFnZXMgY29tZSBmcm9tIHRyYWluaW5nIHJlY2lwZSArIGRlc2lnbiwgbm90IGF0dGVudGlvbiBhbG9uZVwiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIEFibGF0aW9uOiBhY2N1cmFjeSBnYWlucyBmcm9tIGVhY2ggQ29udk5lWHQgbW9kZXJuaXphdGlvbiBzdGVwXG4jIFJlcHJvZHVjZWQgZnJvbSBUYWJsZSAxIGluIFx1MDAyN0EgQ29udk5ldCBmb3IgdGhlIDIwMjBzXHUwMDI3IChMaXUgZXQgYWwuLCAyMDIyKVxuc3RlcHMgPSBbXG4gICAgKFwiQmFzZWxpbmUgUmVzTmV0LTUwXCIsICAgICAgICAgICAgICAgICAgICAgICA3Ni4xKSxcbiAgICAoXCIrIE1vZGVybiB0cmFpbmluZyByZWNpcGUgKEFkYW1XLCBhdWdzKVwiLCAgIDc4LjgpLFxuICAgIChcIisgU3RhZ2UgcmF0aW8gMzozOjk6M1wiLCAgICAgICAgICAgICAgICAgICAgNzkuNCksXG4gICAgKFwiKyBQYXRjaGlmeSBzdGVtICg0eDQgczQpXCIsICAgICAgICAgICAgICAgICA3OS41KSxcbiAgICAoXCIrIERlcHRod2lzZSArIGludmVydGVkIGJvdHRsZW5lY2tcIiwgICAgICAgIDgwLjYpLFxuICAgIChcIisgTGFyZ2Uga2VybmVsIDd4NyBkZXB0aHdpc2VcIiwgICAgICAgICAgICAgODAuNiksXG4gICAgKFwiKyBMTiwgR0VMVSwgb25lIGFjdGl2YXRpb24vYmxvY2tcIiwgICAgICAgICA4MS4zKSxcbiAgICAoXCIrIFNlcGFyYXRlIGRvd25zYW1wbGluZyBsYXllcnNcIiwgICAgICAgICAgIDgyLjEpLFxuXVxuXG5wcmludChmXCJ7XHUwMDI3TW9kZXJuaXphdGlvbiBTdGVwXHUwMDI3Olx1MDAzYzQ1fSB7XHUwMDI3VG9wLTFcdTAwMjc6XHUwMDNlNn0ge1x1MDAyN0RlbHRhXHUwMDI3Olx1MDAzZTd9XCIpXG5wcmludChcdTAwMjctXHUwMDI3ICogNjIpXG5wcmV2ID0gTm9uZVxuZm9yIG5hbWUsIGFjYyBpbiBzdGVwczpcbiAgICBkZWx0YSA9IGZcIit7YWNjIC0gcHJldjouMWZ9JVwiIGlmIHByZXYgaXMgbm90IE5vbmUgZWxzZSBcImJhc2VcIlxuICAgIHByaW50KGZcIntuYW1lOlx1MDAzYzQ1fSB7YWNjOlx1MDAzZTUuMWZ9JSB7ZGVsdGE6XHUwMDNlN31cIilcbiAgICBwcmV2ID0gYWNjXG5cbnRvdGFsX2dhaW4gPSBzdGVwc1stMV1bMV0gLSBzdGVwc1swXVsxXVxucHJpbnQoZlwiXFxuVG90YWwgZ2FpbjogK3t0b3RhbF9nYWluOi4xZn0lIChSZXNOZXQtNTAgLVx1MDAzZSBDb252TmVYdC1UKVwiKVxucHJpbnQoXCJUcmFpbmluZyByZWNpcGUgYWxvbmU6ICsyLjclOyBhcmNoaXRlY3R1cmUgY2hhbmdlczogKzMuMyVcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb252TmVYdCBWMiDigJQgRkNNQUUgYW5kIEdSTiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udk5lWHQgVjIgKFdvbyBldCBhbC4sIDIwMjMpIGFkZHMgdHdvIGFkdmFuY2VzOiAoMSkgRkNNQUUgKEZ1bGx5IENvbnZvbHV0aW9uYWwgTWFza2VkIEF1dG9lbmNvZGVyKSBwcmV0cmFpbmluZyDigJQgYSBtYXNrZWQgYXV0b2VuY29kZXIgd2hlcmUgdGhlIGVuY29kZXIgaXMgYSBDb252TmVYdCBiYWNrYm9uZSBhbmQgdGhlIGRlY29kZXIgcmVjb25zdHJ1Y3RzIG1hc2tlZCBwYXRjaGVzLCBzaW1pbGFyIHRvIE1BRSBidXQgZm9yIENOTnM7ICgyKSBHUk4gKEdsb2JhbCBSZXNwb25zZSBOb3JtYWxpemF0aW9uKSDigJQgYSBuZXcgbm9ybWFsaXphdGlvbiBsYXllciBpbnNlcnRlZCBpbiB0aGUgcG9pbnR3aXNlIE1MUCB0aGF0IG5vcm1hbGl6ZXMgYWNyb3NzIHRoZSBzcGF0aWFsIGRpbWVuc2lvbiAobm90IGNoYW5uZWxzKSwgcHJldmVudGluZyBmZWF0dXJlIGNvbGxhcHNlIGluIHRoZSBtYXNrZWQgYXV0b2VuY29kZXIgc2V0dGluZy4gQ29udk5lWHQgVjItSCBhY2hpZXZlcyA4OC45JSBvbiBJbWFnZU5ldCB3aXRoIEZDTUFFIHByZXRyYWluaW5nLCBjb21wZXRpdGl2ZSB3aXRoIHRoZSBiZXN0IFZpVCB2YXJpYW50cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXNOZXQgTW9kZXJuaXphdGlvbiBTdGVwcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDaGFuZ2UiLCJDdW11bGF0aXZlIFRvcC0xICglKSIsIkRlbHRhIiwiSW5zcGlyZWQgYnkiXSwicm93cyI6W1siQmFzZWxpbmUgUmVzTmV0LTUwIiwiNzYuMSIsIuKAlCIsIkhlIGV0IGFsLiAyMDE2Il0sWyJNb2Rlcm4gdHJhaW5pbmcgcmVjaXBlIiwiNzguOCIsIisyLjclIiwiRGVpVCB0cmFpbmluZyBzdHJhdGVneSJdLFsiU3RhZ2UgcmF0aW8gMzozOjk6MyIsIjc5LjQiLCIrMC42JSIsIlN3aW4tVCBzdGFnZSBkaXN0cmlidXRpb24iXSxbIlBhdGNoaWZ5IHN0ZW0gNMOXNCBzNCIsIjc5LjUiLCIrMC4xJSIsIlZpVCBub24tb3ZlcmxhcHBpbmcgcGF0Y2hlcyJdLFsiRGVwdGh3aXNlICsgaW52ZXJ0ZWQgYm90dGxlbmVjayIsIjgwLjYiLCIrMS4xJSIsIk1vYmlsZU5ldFYyIC8gU3dpbiBNTFAiXSxbIjfDlzcgZGVwdGh3aXNlIGNvbnYiLCI4MC42IiwiKzAuMCUiLCJTd2luIDfDlzcgYXR0ZW50aW9uIHdpbmRvdyJdLFsiTE4gKyBHRUxVICsgMSBhY3RpdmF0aW9uL2Jsb2NrIiwiODEuMyIsIiswLjclIiwiVHJhbnNmb3JtZXIgbWljcm8gZGVzaWduIl0sWyJTZXBhcmF0ZSBkb3duc2FtcGxpbmcgbGF5ZXJzIiwiODIuMSIsIiswLjglIiwiU3dpbiBwYXRjaCBtZXJnaW5nIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb252TmVYdCB2cyBWaXNpb24gVHJhbnNmb3JtZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnZOZVh0IGhhcyBhIHNpbXBsZXIgaW5kdWN0aXZlIGJpYXMgdGhhbiBTd2luIFRyYW5zZm9ybWVyOiB0cmFuc2xhdGlvbiBlcXVpdmFyaWFuY2UgZnJvbSBjb252b2x1dGlvbiwgYnV0IG5vIHNoaWZ0ZWQtd2luZG93IHBhcnRpdGlvbmluZyBvciByZWxhdGl2ZSBwb3NpdGlvbiBlbmNvZGluZ3MuIEluZmVyZW5jZSBpcyBmYXN0ZXIgYXQgaGlnaCByZXNvbHV0aW9uIGJlY2F1c2UgY29udm9sdXRpb24gc2NhbGVzIGFzIE8oSFcpIHdoaWxlIHdpbmRvd2VkIGF0dGVudGlvbiBzY2FsZXMgYXMgTyhIVyDDlyB3aW5kb3dfc2l6ZcKyKS4gQ29udk5lWHQgaXMgYWxzbyBlYXNpZXIgdG8gaW1wbGVtZW50IChubyBjdXN0b20gQ1VEQSBrZXJuZWxzIGZvciBzaGlmdGVkIHdpbmRvd3MpLiBTd2luIFRyYW5zZm9ybWVyIGhhcyBzbGlnaHRseSBzdHJvbmdlciBwZXJmb3JtYW5jZSBvbiBkZW5zZSBwcmVkaWN0aW9uIHRhc2tzIChkZXRlY3Rpb24sIHNlZ21lbnRhdGlvbikgYmVjYXVzZSBpdHMgaGllcmFyY2hpY2FsIGF0dGVudGlvbiBjYXB0dXJlcyBsb25nZXItcmFuZ2UgZGVwZW5kZW5jaWVzLiBGb3IgbW9zdCBwcmFjdGljYWwgYXBwbGljYXRpb25zLCBDb252TmVYdCBpcyB0aGUgc2ltcGxlciBhbmQgbW9yZSBkZXBsb3lhYmxlIGNob2ljZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb252TmVYdCBkZW1vbnN0cmF0ZXMgdGhhdCB0aGUgZ2FwIGJldHdlZW4gVHJhbnNmb3JtZXJzIGFuZCBDTk5zIGluIHRoZSAyMDIwLTIwMjIgcGVyaW9kIHdhcyBsYXJnZWx5IGEgZ2FwIGluIHRyYWluaW5nIHJlY2lwZSBhbmQgZGVzaWduIHBoaWxvc29waHksIG5vdCBhIGZ1bmRhbWVudGFsIGxpbWl0YXRpb24gb2YgdGhlIGNvbnZvbHV0aW9uIG9wZXJhdGlvbi4gQSBjYXJlZnVsbHkgZGVzaWduZWQgQ05OLCB0cmFpbmVkIHdpdGggbW9kZXJuIHRlY2huaXF1ZXMsIG1hdGNoZXMgU3dpbiBUcmFuc2Zvcm1lciBhdCBldmVyeSBzY2FsZS4gVGhlIGNob2ljZSBiZXR3ZWVuIENvbnZOZVh0IGFuZCBhIFZpVC1iYXNlZCBtb2RlbCBzaG91bGQgYmUgZHJpdmVuIGJ5IGRlcGxveW1lbnQgY29uc3RyYWludHMgKENvbnZOZVh0IGlzIHNpbXBsZXIgYW5kIGZhc3RlciksIHByZXRyYWluaW5nIGF2YWlsYWJpbGl0eSwgYW5kIHdoZXRoZXIgdGhlIHNwZWNpZmljIHRhc2sgYmVuZWZpdHMgZnJvbSBnbG9iYWwgYXR0ZW50aW9uICh2ZXJ5IGxvbmctcmFuZ2UgZGVwZW5kZW5jaWVzKSBvciBsb2NhbCBjb252b2x1dGlvbiAobG9jYWwgdGV4dHVyZSBhbmQgc3RydWN0dXJlKS4ifV0="
---
# ConvNeXt — Modernized CNN Matching ViT Performance

ConvNeXt (Liu et al., CVPR 2022) asked: can a purely convolutional network match Swin Transformer accuracy if we adopt the same modern design principles? The answer is yes. Starting from ResNet-50, the paper applies six targeted changes — all inspired by the Swin Transformer — and recovers a CNN that matches or exceeds Swin-T at every scale. This result has important implications: the gains of Vision Transformers come partly from training recipe and design choices, not purely from attention mechanisms.

## Motivation — Transformers vs CNNs

By 2021, Swin Transformer had surpassed ResNets on ImageNet, COCO, and ADE20K with hierarchical attention and shifted windows. The common interpretation was that self-attention is inherently superior to convolution. ConvNeXt challenges this interpretation by asking whether the accuracy gap exists because of attention, or because of the many other design differences: training recipe (AdamW, cosine schedule, extensive augmentation), macro structure (stage ratios, stems, downsampling), and micro design (normalization, activations, kernel size). The modernization roadmap answers this question systematically.

## The Modernization Road Map

The paper starts with ResNet-50 (76.1% top-1) and adds Swin-inspired changes one at a time, measuring accuracy after each. The order is: (1) training recipe (AdamW, cosine schedule, Mixup, CutMix, RandAugment, Label Smoothing) -> 78.8%; then architecture changes starting from macro design down to micro design. Each step is ablated independently, making the paper an unusually clean analysis of what drives accuracy.

1. Patchify stem: replace 7×7+MaxPool with 4×4 stride-4 Conv (like ViT) — fewer forward passes, less aggressive spatial downsampling at the start.
2. Stage ratio 3:3:9:3: mirror Swin-T block distribution (fewer blocks in early stages, more in stage 3).
3. ResNeXt-ify: replace 3×3 conv with depthwise 3×3 conv + increase channel width (inverted bottleneck style).
4. Inverted bottleneck: expand channels 4× in the middle layer (like Transformer MLP) rather than compressing.
5. Larger kernel: increase depthwise conv from 3×3 to 7×7 (like Swin's 7×7 attention window).
6. Micro design: replace BatchNorm with LayerNorm, replace ReLU with GELU, reduce activations to one per block, separate downsampling layers between stages.

> **Training Recipe vs Architecture**: Simply applying AdamW + cosine schedule + modern augmentation (Mixup, CutMix, RandAugment, Label Smoothing) to ResNet-50 raises accuracy from 76.1% to 78.8% — a 2.7% gain with zero architectural change. This result reveals that a large fraction of the Transformer accuracy advantage is attributable to training recipe, not architecture. The remaining architectural changes add a further 3.3% on top.

## ConvNeXt Block Design

The ConvNeXt block is structurally similar to a Transformer block: depthwise 7×7 conv (analogous to attention over a 7×7 window) followed by a 4× inverted bottleneck MLP (pointwise expand -> GELU -> pointwise contract). Normalization uses LayerNorm applied on the channel axis (after permuting to B, H, W, C). There is one GELU activation per block (not one per linear layer as in ResNet). A layer scale parameter γ (initialized to 1e-6) is optionally applied before the residual addition. The depthwise conv operates across the spatial dimensions while the pointwise layers mix channels — exactly as in Transformers where attention mixes positions and MLP mixes channels.

## Code Examples

```python
import torch
import torch.nn as nn

class ConvNeXtBlock(nn.Module):
    """ConvNeXt block: depthwise 7x7 -> LN -> pointwise expand -> GELU -> pointwise project."""
    def __init__(self, dim, mlp_ratio=4, layer_scale_init=1e-6):
        super().__init__()
        self.dwconv  = nn.Conv2d(dim, dim, kernel_size=7, padding=3, groups=dim)
        self.norm    = nn.LayerNorm(dim, eps=1e-6)
        self.pwconv1 = nn.Linear(dim, mlp_ratio * dim)
        self.act     = nn.GELU()
        self.pwconv2 = nn.Linear(mlp_ratio * dim, dim)
        self.gamma   = nn.Parameter(layer_scale_init * torch.ones(dim))

    def forward(self, x):
        residual = x
        x = self.dwconv(x)               # (B, C, H, W) -- depthwise spatial mixing
        x = x.permute(0, 2, 3, 1)       # (B, H, W, C) for LayerNorm
        x = self.norm(x)
        x = self.pwconv1(x)              # expand: C -> 4C
        x = self.act(x)                  # single GELU (not one per layer)
        x = self.pwconv2(x)              # contract: 4C -> C
        x = self.gamma * x
        x = x.permute(0, 3, 1, 2)       # back to (B, C, H, W)
        return residual + x

block = ConvNeXtBlock(dim=96)
x = torch.randn(2, 96, 56, 56)
print(f"Input:  {x.shape}")
print(f"Output: {block(x).shape}")
print(f"Params: {sum(p.numel() for p in block.parameters()):,}")
```

```python
import torch
import torch.nn as nn

class PatchifyStem(nn.Module):
    """Replace 7x7+MaxPool with a single 4x4 stride-4 conv (like ViT patchify)."""
    def __init__(self, in_ch=3, out_ch=96):
        super().__init__()
        self.proj = nn.Conv2d(in_ch, out_ch, kernel_size=4, stride=4)
        self.norm = nn.LayerNorm(out_ch, eps=1e-6)

    def forward(self, x):
        x = self.proj(x)                 # (B, C, H/4, W/4)
        x = x.permute(0, 2, 3, 1)       # (B, H/4, W/4, C)
        x = self.norm(x)
        return x.permute(0, 3, 1, 2)    # (B, C, H/4, W/4)

class DownsampleLayer(nn.Module):
    """Separate downsampling between stages: LN -> 2x2 stride-2 conv."""
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.norm = nn.LayerNorm(in_ch, eps=1e-6)
        self.conv = nn.Conv2d(in_ch, out_ch, kernel_size=2, stride=2)

    def forward(self, x):
        x = x.permute(0, 2, 3, 1)
        x = self.norm(x)
        x = x.permute(0, 3, 1, 2)
        return self.conv(x)

stem = PatchifyStem(3, 96)
down = DownsampleLayer(96, 192)
x = torch.randn(2, 3, 224, 224)
h = stem(x)
print(f"After patchify stem: {h.shape}")   # (2, 96, 56, 56)
print(f"After downsample:    {down(h).shape}")  # (2, 192, 28, 28)
print("No MaxPool: smoother spatial downsampling vs ResNet stem")
```

```python
import torch
from torchvision import models

convnext = models.convnext_tiny(weights=models.ConvNeXt_Tiny_Weights.IMAGENET1K_V1)
swin_t   = models.swin_t(weights=models.Swin_T_Weights.IMAGENET1K_V1)

def count_params(model):
    return sum(p.numel() for p in model.parameters()) / 1e6

models_info = [
    ('ConvNeXt-Tiny', convnext, 82.1),
    ('Swin-T',        swin_t,   81.3),
]

print(f"{'Model':<20} {'Params (M)':>12} {'Official Top-1':>15} {'Attention?':>12}")
print('-' * 62)
for name, m, acc in models_info:
    print(f"{name:<20} {count_params(m):>12.1f} {acc:>14.1f}% {'No' if 'ConvNeXt' in name else 'Yes':>12}")

print()
x = torch.randn(1, 3, 224, 224)
convnext.eval(); swin_t.eval()
with torch.no_grad():
    _ = convnext(x)
print("ConvNeXt-Tiny matches Swin-T with no self-attention, simpler inductive bias")
print("Key: Transformer advantages come from training recipe + design, not attention alone")
```

```python
# Ablation: accuracy gains from each ConvNeXt modernization step
# Reproduced from Table 1 in 'A ConvNet for the 2020s' (Liu et al., 2022)
steps = [
    ("Baseline ResNet-50",                       76.1),
    ("+ Modern training recipe (AdamW, augs)",   78.8),
    ("+ Stage ratio 3:3:9:3",                    79.4),
    ("+ Patchify stem (4x4 s4)",                 79.5),
    ("+ Depthwise + inverted bottleneck",        80.6),
    ("+ Large kernel 7x7 depthwise",             80.6),
    ("+ LN, GELU, one activation/block",         81.3),
    ("+ Separate downsampling layers",           82.1),
]

print(f"{'Modernization Step':<45} {'Top-1':>6} {'Delta':>7}")
print('-' * 62)
prev = None
for name, acc in steps:
    delta = f"+{acc - prev:.1f}%" if prev is not None else "base"
    print(f"{name:<45} {acc:>5.1f}% {delta:>7}")
    prev = acc

total_gain = steps[-1][1] - steps[0][1]
print(f"\nTotal gain: +{total_gain:.1f}% (ResNet-50 -> ConvNeXt-T)")
print("Training recipe alone: +2.7%; architecture changes: +3.3%")
```

## ConvNeXt V2 — FCMAE and GRN

ConvNeXt V2 (Woo et al., 2023) adds two advances: (1) FCMAE (Fully Convolutional Masked Autoencoder) pretraining — a masked autoencoder where the encoder is a ConvNeXt backbone and the decoder reconstructs masked patches, similar to MAE but for CNNs; (2) GRN (Global Response Normalization) — a new normalization layer inserted in the pointwise MLP that normalizes across the spatial dimension (not channels), preventing feature collapse in the masked autoencoder setting. ConvNeXt V2-H achieves 88.9% on ImageNet with FCMAE pretraining, competitive with the best ViT variants.

## ResNet Modernization Steps

| Change | Cumulative Top-1 (%) | Delta | Inspired by |
| --- | --- | --- | --- |
| Baseline ResNet-50 | 76.1 | — | He et al. 2016 |
| Modern training recipe | 78.8 | +2.7% | DeiT training strategy |
| Stage ratio 3:3:9:3 | 79.4 | +0.6% | Swin-T stage distribution |
| Patchify stem 4×4 s4 | 79.5 | +0.1% | ViT non-overlapping patches |
| Depthwise + inverted bottleneck | 80.6 | +1.1% | MobileNetV2 / Swin MLP |
| 7×7 depthwise conv | 80.6 | +0.0% | Swin 7×7 attention window |
| LN + GELU + 1 activation/block | 81.3 | +0.7% | Transformer micro design |
| Separate downsampling layers | 82.1 | +0.8% | Swin patch merging |

## ConvNeXt vs Vision Transformer

ConvNeXt has a simpler inductive bias than Swin Transformer: translation equivariance from convolution, but no shifted-window partitioning or relative position encodings. Inference is faster at high resolution because convolution scales as O(HW) while windowed attention scales as O(HW × window_size²). ConvNeXt is also easier to implement (no custom CUDA kernels for shifted windows). Swin Transformer has slightly stronger performance on dense prediction tasks (detection, segmentation) because its hierarchical attention captures longer-range dependencies. For most practical applications, ConvNeXt is the simpler and more deployable choice.

## Key Takeaways

ConvNeXt demonstrates that the gap between Transformers and CNNs in the 2020-2022 period was largely a gap in training recipe and design philosophy, not a fundamental limitation of the convolution operation. A carefully designed CNN, trained with modern techniques, matches Swin Transformer at every scale. The choice between ConvNeXt and a ViT-based model should be driven by deployment constraints (ConvNeXt is simpler and faster), pretraining availability, and whether the specific task benefits from global attention (very long-range dependencies) or local convolution (local texture and structure).

