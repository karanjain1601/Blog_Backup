---
title: "Normalizing Flows — Change of Variables and Exact Likelihood"
slug: "normalizing-flows-basics"
description: "Normalizing flows learn a bijective mapping f: X <-> Z where Z~N(0,I), enabling exact likelihood computation via the change of variables formula log p_X(x) = log p_Z(f(x)) + log|det J_f(x)|. Covers coupling layers, NICE, autoregressive flows, and the comparison with VAE, GAN, and diffusion."
tags: ["deep-learning", "generative-models", "gans", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBub3JtYWxpemluZyBmbG93IGlzIGEgZ2VuZXJhdGl2ZSBtb2RlbCB0aGF0IGxlYXJucyBhIGJpamVjdGl2ZSAoaW52ZXJ0aWJsZSkgZnVuY3Rpb24gZjogWCDihpQgWiwgd2hlcmUgWiBmb2xsb3dzIGEgc2ltcGxlIGJhc2UgZGlzdHJpYnV0aW9uIHN1Y2ggYXMgTigwLEkpLiBUaGUgbmFtZSBjb21lcyBmcm9tIHRoZSBpZGVhIHRoYXQgdGhlIHRyYW5zZm9ybWF0aW9uIFx1MDAyN25vcm1hbGlzZXNcdTAwMjcgdGhlIGNvbXBsZXggZGF0YSBkaXN0cmlidXRpb24gaW50byBhIEdhdXNzaWFuLiBGbG93cyBvZmZlciBhIHByb3BlcnR5IHVuaXF1ZSBhbW9uZyBkZWVwIGdlbmVyYXRpdmUgbW9kZWxzOiBleGFjdCBsb2ctbGlrZWxpaG9vZCBjb21wdXRhdGlvbi4gVW5saWtlIFZBRXMgKGxvd2VyIGJvdW5kKSBhbmQgR0FOcyAoaW1wbGljaXQgZGlzdHJpYnV0aW9uKSwgZmxvd3MgZ2l2ZSB0aGUgZXhhY3QgbG9nIHAoeCkgdmlhIHRoZSBjaGFuZ2Ugb2YgdmFyaWFibGVzIGZvcm11bGEsIGVuYWJsaW5nIGRpcmVjdCBtYXhpbXVtIGxpa2VsaWhvb2QgdHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hhbmdlIG9mIFZhcmlhYmxlcyBGb3JtdWxhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJZiBaIH4gcF9aIGFuZCB4ID0gZuKBu8K5KHopIHdoZXJlIGYgaXMgYmlqZWN0aXZlLCB0aGVuIHRoZSBkZW5zaXR5IG9mIFggc2F0aXNmaWVzOiBwX1goeCkgPSBwX1ooZih4KSkgfGRldCBKX2YoeCl8LiBUYWtpbmcgbG9nczogbG9nIHBfWCh4KSA9IGxvZyBwX1ooZih4KSkgKyBsb2d8ZGV0IEpfZih4KXwuIFRoZSBmaXJzdCB0ZXJtIGlzIHRoZSBsb2ctbGlrZWxpaG9vZCB1bmRlciB0aGUgc2ltcGxlIGJhc2UgZGlzdHJpYnV0aW9uLiBUaGUgc2Vjb25kIHRlcm0gaXMgdGhlIGxvZyBhYnNvbHV0ZSBKYWNvYmlhbiBkZXRlcm1pbmFudCBvZiBmIOKAlCBpdCBhY2NvdW50cyBmb3IgaG93IGYgc3RyZXRjaGVzIG9yIGNvbXByZXNzZXMgdm9sdW1lLiBUcmFpbmluZyBtYXhpbWlzZXMgRV94W2xvZyBwX1goeCldIG92ZXIgdGhlIGRhdGFzZXQuIFRoZSBjaGFsbGVuZ2U6IGZvciBhIGdlbmVyYWwgbmV1cmFsIG5ldHdvcmssIGNvbXB1dGluZyBkZXQgSl9mIGNvc3RzIE8oZMKzKSBmb3IgYSBkLWRpbWVuc2lvbmFsIGlucHV0IOKAlCBwcm9oaWJpdGl2ZSBmb3IgaW1hZ2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY2hhbmdlX29mX3ZhcmlhYmxlc19kZW1vKCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3MUQ6IFogfiBOKDAsMSksIHggPSBmXnstMX0oeikgPSB6XjMuIFZlcmlmeSBwX1ggaW50ZWdyYXRlcyB0byAxLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIHogPSB0b3JjaC5saW5zcGFjZSgtMi41LCAyLjUsIDEwMDApXG4gICAgeCA9IHogKiogMyAgICAgICAgICAgICAgIyBmb3J3YXJkIG1hcDogeiAtXHUwMDNlIHhcbiAgICAjIENoYW5nZSBvZiB2YXJpYWJsZXM6IHBfWCh4KSA9IHBfWih6KSAvIHxkZi9kenxcbiAgICAjIGRmL2R6ID0gM3peMiwgc28gcF9YID0gcF9aKHopIC8gKDN6XjIpXG4gICAgcHogID0gdG9yY2guZXhwKC0wLjUgKiB6KioyKSAvICgyICogdG9yY2gucGkpICoqIDAuNVxuICAgIGphYyA9ICgzICogeioqMikuY2xhbXAobWluPTFlLTYpXG4gICAgcHggID0gcHogLyBqYWNcbiAgICAjIE51bWVyaWNhbCBpbnRlZ3JhdGlvbiB0byB2ZXJpZnkgcF9YIGludGVncmF0ZXMgdG8gMVxuICAgIGR4ICA9ICh4WzE6XSAtIHhbOi0xXSkuYWJzKClcbiAgICBweF9taWQgPSAocHhbMTpdICsgcHhbOi0xXSkgLyAyXG4gICAgaW50ZWdyYWwgPSAocHhfbWlkICogZHgpLnN1bSgpLml0ZW0oKVxuICAgIHByaW50KFx1MDAyN0ludGVncmFsIG9mIHBfWCAoc2hvdWxkIGJlIH4xKTogezouNGZ9XHUwMDI3LmZvcm1hdChpbnRlZ3JhbCkpXG4gICAgIyBMb2ctbGlrZWxpaG9vZCBhdCBzcGVjaWZpYyB4IHZhbHVlc1xuICAgIGZvciB4aSBpbiBbLTguMCwgMC4wMDEsIDguMF06XG4gICAgICAgIHppICA9IG5wLnNpZ24oeGkpICogYWJzKHhpKSAqKiAoMS4wLzMpXG4gICAgICAgIHB6aSA9IG5wLmV4cCgtMC41ICogemkqKjIpIC8gbnAuc3FydCgyICogbnAucGkpXG4gICAgICAgIHB4aSA9IHB6aSAvICgzICogemkqKjIgKyAxZS04KVxuICAgICAgICBwcmludChcdTAwMjcgIHg9ezo1LjFmfSAgej17Oi4zZn0gIGxvZyBwX1g9ezouM2Z9XHUwMDI3LmZvcm1hdChcbiAgICAgICAgICAgICAgeGksIHppLCBucC5sb2cocHhpICsgMWUtMzApKSlcblxuY2hhbmdlX29mX3ZhcmlhYmxlc19kZW1vKCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFjdGFibGUgSmFjb2JpYW4gRGV0ZXJtaW5hbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2V5IGNvbXB1dGF0aW9uYWwgY2hhbGxlbmdlIGlzIGNvbXB1dGluZyBsb2d8ZGV0IEpfZnwuIEZvciBhIGdlbmVyYWwgaW52ZXJ0aWJsZSBuZXVyYWwgbmV0d29yaywgdGhpcyBpcyBPKGTCsykuIFRoZSBzb2x1dGlvbiBpcyB0byBkZXNpZ24gZiB3aXRoIGEgdHJpYW5ndWxhciBKYWNvYmlhbiwgd2hvc2UgZGV0ZXJtaW5hbnQgaXMganVzdCB0aGUgcHJvZHVjdCBvZiBkaWFnb25hbCBlbnRyaWVzIOKAlCBPKGQpLiBBIGxvd2VyLXRyaWFuZ3VsYXIgSmFjb2JpYW4gYXJpc2VzIGZyb20gYXV0b3JlZ3Jlc3NpdmUgbW9kZWxzOiB4X2kgPSBmKHhfe1x1MDAzY2l9LCB6X2kpLCBzbyDiiIJ4X2kv4oiCel9qID0gMCBmb3IgaiBcdTAwM2UgaS4gQW4gdXBwZXItdHJpYW5ndWxhciBKYWNvYmlhbiBhcmlzZXMgZnJvbSBjb3VwbGluZyBsYXllcnMuIEJvdGggZW5hYmxlIE8oZCkgbG9nLWRldGVybWluYW50IGNvbXB1dGF0aW9uLiBUaGlzIHN0cnVjdHVyYWwgY29uc3RyYWludCBvbiB0aGUgSmFjb2JpYW4gaXMgdGhlIGNvcmUgZGVzaWduIHByaW5jaXBsZSBiZWhpbmQgYWxsIHByYWN0aWNhbCBmbG93IGFyY2hpdGVjdHVyZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ291cGxpbmcgTGF5ZXJzOiBOSUNFIGFuZCBSZWFsTlZQIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOSUNFIChEaW5oIGV0IGFsLiAyMDE0KSBpbnRyb2R1Y2VzIGFkZGl0aXZlIGNvdXBsaW5nIGxheWVyczogc3BsaXQgeCBpbnRvIFt44oKBLCB44oKCXSwgcGFzcyB44oKBIHRocm91Z2ggdW5jaGFuZ2VkLCBhbmQgY29tcHV0ZSB54oKCID0geOKCgiArIG0oeOKCgSkgd2hlcmUgbSBpcyBhbiBhcmJpdHJhcnkgbmV1cmFsIG5ldHdvcmsuIFRoZSBKYWNvYmlhbiBpcyBsb3dlci10cmlhbmd1bGFyIHdpdGggMXMgb24gdGhlIGRpYWdvbmFsLCBzbyBsb2d8ZGV0IEp8ID0gMC4gSW52ZXJzaW9uIGlzIHRyaXZpYWw6IHjigoIgPSB54oKCIOKIkiBtKHnigoEpLiBSZWFsTlZQIGV4dGVuZHMgdGhpcyB0byBhZmZpbmUgY291cGxpbmc6IHnigoIgPSB44oKCIOKKmSBleHAocyh44oKBKSkgKyB0KHjigoEpLiBUaGUgSmFjb2JpYW4gZGlhZ29uYWwgaXMgZXhwKHMoeOKCgSkpLCBnaXZpbmcgbG9nfGRldCBKfCA9IM6j4bWiIHPhtaIoeOKCgSkuIEJvdGggcyBhbmQgdCBhcmUgdW5yZXN0cmljdGVkIG5ldXJhbCBuZXR3b3Jrczsgb25seSB0aGUgY291cGxpbmcgc3RydWN0dXJlIG11c3QgYmUgcHJlc2VydmVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBBZGRpdGl2ZUNvdXBsaW5nKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3TklDRSAoRGluaCAyMDE0KTogeTIgPSB4MiArIG0oeDEpLCB5MSA9IHgxLiBsb2d8ZGV0IEp8ID0gMC5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCwgaGlkZGVuPTY0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGQxID0gZCAvLyAyXG4gICAgICAgIHNlbGYuZDEgPSBkMVxuICAgICAgICBzZWxmLm0gID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkMSwgaGlkZGVuKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgZCAtIGQxKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICB4MSwgeDIgID0geFs6LCA6c2VsZi5kMV0sIHhbOiwgc2VsZi5kMTpdXG4gICAgICAgIHkyICAgICAgID0geDIgKyBzZWxmLm0oeDEpICAgICAgICAgICAgICAjIHRyYW5zbGF0ZSBvbmx5XG4gICAgICAgIGxvZ19kZXQgID0gdG9yY2guemVyb3MoeC5zaXplKDApKSAgICAgICAjIHVuaXQtdm9sdW1lIG1hcFxuICAgICAgICByZXR1cm4gdG9yY2guY2F0KFt4MSwgeTJdLCBkaW09MSksIGxvZ19kZXRcblxuICAgIGRlZiBpbnZlcnNlKHNlbGYsIHkpOlxuICAgICAgICB5MSwgeTIgPSB5WzosIDpzZWxmLmQxXSwgeVs6LCBzZWxmLmQxOl1cbiAgICAgICAgeDIgICAgID0geTIgLSBzZWxmLm0oeTEpICAgICAgICAgICAgICAgIyB0cml2aWFsIGludmVyc2lvblxuICAgICAgICByZXR1cm4gdG9yY2guY2F0KFt5MSwgeDJdLCBkaW09MSlcblxubGF5ZXIgPSBBZGRpdGl2ZUNvdXBsaW5nKGQ9OClcbnggPSB0b3JjaC5yYW5kbig0LCA4KVxueSwgbGQgPSBsYXllcih4KVxueF9yZWMgPSBsYXllci5pbnZlcnNlKHkpXG5wcmludChcdTAwMjdSZWNvbnN0cnVjdGlvbiBlcnJvcjpcdTAwMjcsICh4IC0geF9yZWMpLmFicygpLm1heCgpLml0ZW0oKSlcbnByaW50KFx1MDAyN2xvZ3xkZXQgSnw6XHUwMDI3LCBsZC50b2xpc3QoKSkgICMgc2hvdWxkIGJlIFswLDAsMCwwXSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4YWN0IExvZy1MaWtlbGlob29kIENvbXB1dGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIG5vcm1hbGl6aW5nIGZsb3cgc3RhY2tzIEsgY291cGxpbmcgbGF5ZXJzOiBsb2cgcF9YKHgpID0gbG9nIHBfWih6X0spICsgzqPigpYgbG9nfGRldCBKX2bigpYoeuKCluKCi+KCgSl8LCB3aGVyZSB64oKAID0geCBhbmQgel9LIGlzIHRoZSBmaW5hbCBsYXRlbnQuIFRoZSBzdW0gb2YgbG9nLWRldGVybWluYW50cyBhY2N1bXVsYXRlcyBhY3Jvc3MgbGF5ZXJzLiBUcmFpbmluZyBkaXJlY3RseSBtYXhpbWlzZXMgdGhpcyBleGFjdCBsb2ctbGlrZWxpaG9vZCDigJQgbm8gdmFyaWF0aW9uYWwgYm91bmQsIG5vIHNjb3JlIG1hdGNoaW5nLCBubyBhZHZlcnNhcmlhbCB0cmFpbmluZy4gVGhlIGV4YWN0IGxpa2VsaWhvb2QgYWxzbyBlbmFibGVzIGRpcmVjdCBjb21wYXJpc29uIGJldHdlZW4gbW9kZWxzIGluIG5hdHMgb3IgYml0cy1wZXItZGltIChCUEQgPSDiiJJsb2figoIgcCh4KSAvIEQgZm9yIEQtZGltZW5zaW9uYWwgeCksIHVubGlrZSBHQU5zIHdoZXJlIGxpa2VsaWhvb2QgaXMgdW5hdmFpbGFibGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2guZGlzdHJpYnV0aW9ucyBhcyBkaXN0XG5cbmNsYXNzIFNpbXBsZU5JQ0VGbG93KG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGQ9OCwgbl9sYXllcnM9NCwgaGlkZGVuPTY0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubGF5ZXJzID0gbm4uTW9kdWxlTGlzdChcbiAgICAgICAgICAgIFtBZGRpdGl2ZUNvdXBsaW5nKGQsIGhpZGRlbj1oaWRkZW4pIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKV0pXG4gICAgICAgIHNlbGYucHJpb3IgID0gZGlzdC5NdWx0aXZhcmlhdGVOb3JtYWwoXG4gICAgICAgICAgICB0b3JjaC56ZXJvcyhkKSwgdG9yY2guZXllKGQpKVxuXG4gICAgZGVmIGxvZ19wcm9iKHNlbGYsIHgpOlxuICAgICAgICB6LCBsb2dfZGV0ID0geCwgdG9yY2guemVyb3MoeC5zaXplKDApKVxuICAgICAgICBmb3IgbGF5ZXIgaW4gc2VsZi5sYXllcnM6XG4gICAgICAgICAgICB6LCBsZCA9IGxheWVyKHopXG4gICAgICAgICAgICBsb2dfZGV0ID0gbG9nX2RldCArIGxkXG4gICAgICAgIHJldHVybiBzZWxmLnByaW9yLmxvZ19wcm9iKHopICsgbG9nX2RldCAgICMgZXhhY3QgbG9nIHAoeClcblxuICAgIGRlZiBzYW1wbGUoc2VsZiwgbik6XG4gICAgICAgIHogPSBzZWxmLnByaW9yLnNhbXBsZSgobiwpKVxuICAgICAgICBmb3IgbGF5ZXIgaW4gcmV2ZXJzZWQoc2VsZi5sYXllcnMpOlxuICAgICAgICAgICAgeiA9IGxheWVyLmludmVyc2UoeilcbiAgICAgICAgcmV0dXJuIHpcblxuZmxvdyA9IFNpbXBsZU5JQ0VGbG93KGQ9OCwgbl9sYXllcnM9NClcbnggPSB0b3JjaC5yYW5kbigxNiwgOClcbmxvZ19weCA9IGZsb3cubG9nX3Byb2IoeClcbnByaW50KFx1MDAyN01lYW4gbG9nIHAoeCk6IHs6LjNmfSAgKE5JQ0U6IGxvZ19kZXQgYWx3YXlzIDAsIHNvID0gbG9nIHBfWih6KSlcdTAwMjcuZm9ybWF0KFxuICAgICAgbG9nX3B4Lm1lYW4oKS5pdGVtKCkpKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiRXhhY3QgTGlrZWxpaG9vZCB2cyBMb3dlciBCb3VuZCB2cyBJbXBsaWNpdCIsImNvbnRlbnQiOiJWQUVzIG1heGltaXNlIHRoZSBFTEJPID0gRVtsb2cgcCh4fHopXSAtIEtMKHEoenx4KSB8fCBwKHopKSwgYSBsb3dlciBib3VuZCBvbiBsb2cgcCh4KS4gVGhlIGdhcCBiZXR3ZWVuIEVMQk8gYW5kIHRydWUgbG9nIHAoeCkgY2FuIGJlIGxhcmdlLiBHQU5zIGhhdmUgbm8gbGlrZWxpaG9vZCBhdCBhbGwg4oCUIHRoZSBtb2RlbCBpcyBpbXBsaWNpdCBhbmQgbGlrZWxpaG9vZCBjYW5ub3QgYmUgY29tcHV0ZWQuIEZsb3dzIGNvbXB1dGUgbG9nIHAoeCkgZXhhY3RseSB2aWEgdGhlIGNoYW5nZSBvZiB2YXJpYWJsZXMgZm9ybXVsYS4gVGhpcyBtYWtlcyBmbG93cyB1bmlxdWVseSBzdWl0ZWQgZm9yIGRlbnNpdHkgZXN0aW1hdGlvbiB0YXNrcywgYW5vbWFseSBkZXRlY3Rpb24sIGFuZCBhbnkgYXBwbGljYXRpb24gcmVxdWlyaW5nIGNhbGlicmF0ZWQgcHJvYmFiaWxpdGllcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBdXRvcmVncmVzc2l2ZSBGbG93czogTUFGIGFuZCBJQUYifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1hc2tlZCBBdXRvcmVncmVzc2l2ZSBGbG93IChNQUYsIFBhcGFtYWthcmlvcyAyMDE3KSB1c2VzIGFuIGF1dG9yZWdyZXNzaXZlIG1vZGVsIHRvIGRlZmluZSB0aGUgc2NhbGUtYW5kLXNoaWZ0IHBhcmFtZXRlcnM6IHjhtaIgPSB64bWiIMK3IGV4cChz4bWiKHhfe1x1MDAzY2l9KSkgKyB04bWiKHhfe1x1MDAzY2l9KS4gVGhlIEphY29iaWFuIGlzIGxvd2VyLXRyaWFuZ3VsYXIgc28gbG9nfGRldCBKfCA9IM6jIHPhtaIuIE1BRiBhbGxvd3MgcGFyYWxsZWwgZGVuc2l0eSBldmFsdWF0aW9uIChhbGwgc+G1oiBjYW4gYmUgY29tcHV0ZWQgaW4gb25lIGZvcndhcmQgcGFzcyBvZiBhIE1BREUgbmV0d29yaykgYnV0IHJlcXVpcmVzIHNlcXVlbnRpYWwgc2FtcGxpbmcuIEludmVyc2UgQXV0b3JlZ3Jlc3NpdmUgRmxvdyAoSUFGKSByZXZlcnNlcyB0aGlzOiBzYW1wbGluZyBpcyBwYXJhbGxlbCBidXQgZGVuc2l0eSBldmFsdWF0aW9uIGlzIHNlcXVlbnRpYWwuIE1BRiBpcyBiZXR0ZXIgZm9yIGRlbnNpdHkgZXN0aW1hdGlvbjsgSUFGIGlzIGJldHRlciBmb3IgZmFzdCBzYW1wbGluZyAoYXMgaW4gVkFFIGRlY29kZXJzKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHZW5lcmF0aXZlIFNhbXBsaW5nIHZpYSBJbnZlcnNpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIGdlbmVyYXRlIG5ldyBzYW1wbGVzIGZyb20gYSBmbG93OiAoMSkgc2FtcGxlIHogfiBwX1ogPSBOKDAsSSkgKHRyaXZpYWxseSBmYXN0KTsgKDIpIGFwcGx5IHRoZSBpbnZlcnNlIGbigbvCuSB0byBvYnRhaW4geCA9IGbigbvCuSh6KS4gRm9yIGNvdXBsaW5nIGxheWVycywgdGhlIGludmVyc2UgaXMgYW5hbHl0aWNhbGx5IHRyYWN0YWJsZSBhbmQgZmFzdCDigJQgTyhkKSBwZXIgbGF5ZXIsIGFuZCBhbGwgZGltZW5zaW9ucyBjYW4gYmUgY29tcHV0ZWQgaW4gcGFyYWxsZWwuIEZvciBhdXRvcmVncmVzc2l2ZSBmbG93cyAoTUFGKSwgaW52ZXJzaW9uIHJlcXVpcmVzIGQgc2VxdWVudGlhbCBzdGVwcyDigJQgb25lIHBlciBkaW1lbnNpb24uIFRoaXMgc2VxdWVudGlhbCBkZXBlbmRlbmN5IG1ha2VzIGF1dG9yZWdyZXNzaXZlIGZsb3dzIHNsb3dlciBhdCBnZW5lcmF0aW9uOyBjb3VwbGluZy1sYXllciBmbG93cyAoUmVhbE5WUCwgR2xvdykgYXJlIHByZWZlcnJlZCB3aGVuIGZhc3Qgc2FtcGxpbmcgbWF0dGVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBmbG93X3NhbXBsZV9hbmRfZXZhbHVhdGUoZmxvdywgbl9zYW1wbGVzPTE2KTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdHZW5lcmF0ZSBzYW1wbGVzIHZpYSBpbnZlcnNpb247IGNvbXB1dGUgdGhlaXIgbG9nLWxpa2VsaWhvb2RzLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGZsb3cuZXZhbCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHNhbXBsZXMgPSBmbG93LnNhbXBsZShuX3NhbXBsZXMpXG4gICAgICAgIGxvZ19weCAgPSBmbG93LmxvZ19wcm9iKHNhbXBsZXMpXG4gICAgcHJpbnQoXHUwMDI3U2FtcGxlcyBzaGFwZSA6IHt9XHUwMDI3LmZvcm1hdChzYW1wbGVzLnNoYXBlKSlcbiAgICBwcmludChcdTAwMjdTYW1wbGUgbWVhbiAgIDogezouNGZ9XHUwMDI3LmZvcm1hdChzYW1wbGVzLm1lYW4oKS5pdGVtKCkpKVxuICAgIHByaW50KFx1MDAyN1NhbXBsZSBzdGQgICAgOiB7Oi40Zn1cdTAwMjcuZm9ybWF0KHNhbXBsZXMuc3RkKCkuaXRlbSgpKSlcbiAgICBwcmludChcdTAwMjdNZWFuIGxvZyBwKHgpIDogezouM2Z9XHUwMDI3LmZvcm1hdChsb2dfcHgubWVhbigpLml0ZW0oKSkpXG4gICAgcHJpbnQoXHUwMDI3QlBEIChiaXRzL2RpbSk6IHs6LjNmfVx1MDAyNy5mb3JtYXQoLWxvZ19weC5tZWFuKCkuaXRlbSgpIC8gKDggKiAwLjY5MzEpKSlcbiAgICByZXR1cm4gc2FtcGxlc1xuXG5mbG93ID0gU2ltcGxlTklDRUZsb3coZD04LCBuX2xheWVycz00KVxuc2FtcGxlcyA9IGZsb3dfc2FtcGxlX2FuZF9ldmFsdWF0ZShmbG93KVxucHJpbnQoXHUwMDI3Rmxvd3M6IGV4YWN0IGxpa2VsaWhvb2QgKyBPKGQpIHBhcmFsbGVsIHNhbXBsaW5nIHZpYSBjb3VwbGluZyBpbnZlcnNpb24uXHUwMDI3KSJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRXhhY3QgbG9nLWxpa2VsaWhvb2Q6IGxvZyBwX1goeCkgPSBsb2cgcF9aKGYoeCkpICsgbG9nfGRldCBKX2YoeCl8IOKAlCBubyBib3VuZCwgbm8gYXBwcm94aW1hdGlvbi4iLCJDb3VwbGluZyBsYXllcnM6IHRyaWFuZ3VsYXIgSmFjb2JpYW4gd2l0aCBPKGQpIGRldGVybWluYW50OyBwYXJhbGxlbCBmb3J3YXJkIGFuZCBpbnZlcnNlLiIsIkFkZGl0aXZlIGNvdXBsaW5nIChOSUNFKTogbG9nfGRldCBKfCA9IDA7IHZvbHVtZS1wcmVzZXJ2aW5nOyBsaW1pdGVkIGV4cHJlc3Npdml0eS4iLCJBZmZpbmUgY291cGxpbmcgKFJlYWxOVlApOiBsb2d8ZGV0IEp8ID0gc3VtIG9mIGxvZy1zY2FsZXM7IG1vcmUgZXhwcmVzc2l2ZS4iLCJNQUY6IHBhcmFsbGVsIGRlbnNpdHkgZXN0aW1hdGlvbiwgc2VxdWVudGlhbCBzYW1wbGluZyDigJQgYmVzdCBmb3IgZGVuc2l0eSBlc3RpbWF0aW9uIHRhc2tzLiIsIklBRjogcGFyYWxsZWwgc2FtcGxpbmcsIHNlcXVlbnRpYWwgZGVuc2l0eSDigJQgdXNlZCBpbiBWQUUgZGVjb2RlcnMgZm9yIGZhc3QgZ2VuZXJhdGlvbi4iLCJHbG93OiAxeDEgaW52ZXJ0aWJsZSBjb252b2x1dGlvbnMgKyBhZmZpbmUgY291cGxpbmcgZm9yIGhpZ2gtcmVzb2x1dGlvbiBpbWFnZSBzeW50aGVzaXMuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb246IFZBRSB2cyBHQU4gdnMgRmxvdyB2cyBEaWZmdXNpb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJWQUUiLCJHQU4iLCJOb3JtYWxpemluZyBGbG93IiwiRGlmZnVzaW9uIl0sInJvd3MiOltbIkV4YWN0IGxpa2VsaWhvb2QiLCJObyAoRUxCTyBsb3dlciBib3VuZCkiLCJObyAoaW1wbGljaXQpIiwiWWVzIChjaGFuZ2Ugb2YgdmFycykiLCJObyAoYnV0IHRyYWN0YWJsZSBib3VuZCkiXSxbIlNhbXBsZSBxdWFsaXR5IiwiTWVkaXVtIiwiSGlnaCIsIk1lZGl1bSIsIlZlcnkgaGlnaCJdLFsiVHJhaW5pbmcgc3RhYmlsaXR5IiwiU3RhYmxlIiwiVW5zdGFibGUgKGFkdmVyc2FyaWFsKSIsIlN0YWJsZSAoTUxFKSIsIlN0YWJsZSJdLFsiU2FtcGxlIHNwZWVkIiwiRmFzdCAoMS1zdGVwIGRlY29kZSkiLCJGYXN0ICgxLXN0ZXAgRykiLCJGYXN0IChjb3VwbGluZyBpbnZlcnNlKSIsIlNsb3cgKG1hbnkgZGVub2lzaW5nIHN0ZXBzKSJdLFsiTGF0ZW50IHNwYWNlIiwiWWVzLCBzdHJ1Y3R1cmVkIiwiUGFydGlhbCAoeikiLCJZZXMsIGV4YWN0IGludmVyc2UiLCJOb2lzZSBzZXF1ZW5jZSJdXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Normalizing Flows — Change of Variables and Exact Likelihood

A normalizing flow is a generative model that learns a bijective (invertible) function f: X ↔ Z, where Z follows a simple base distribution such as N(0,I). The name comes from the idea that the transformation 'normalises' the complex data distribution into a Gaussian. Flows offer a property unique among deep generative models: exact log-likelihood computation. Unlike VAEs (lower bound) and GANs (implicit distribution), flows give the exact log p(x) via the change of variables formula, enabling direct maximum likelihood training.

## Change of Variables Formula

If Z ~ p_Z and x = f⁻¹(z) where f is bijective, then the density of X satisfies: p_X(x) = p_Z(f(x)) |det J_f(x)|. Taking logs: log p_X(x) = log p_Z(f(x)) + log|det J_f(x)|. The first term is the log-likelihood under the simple base distribution. The second term is the log absolute Jacobian determinant of f — it accounts for how f stretches or compresses volume. Training maximises E_x[log p_X(x)] over the dataset. The challenge: for a general neural network, computing det J_f costs O(d³) for a d-dimensional input — prohibitive for images.

```python
import torch
import numpy as np

def change_of_variables_demo():
    '''1D: Z ~ N(0,1), x = f^{-1}(z) = z^3. Verify p_X integrates to 1.'''
    z = torch.linspace(-2.5, 2.5, 1000)
    x = z ** 3              # forward map: z -> x
    # Change of variables: p_X(x) = p_Z(z) / |df/dz|
    # df/dz = 3z^2, so p_X = p_Z(z) / (3z^2)
    pz  = torch.exp(-0.5 * z**2) / (2 * torch.pi) ** 0.5
    jac = (3 * z**2).clamp(min=1e-6)
    px  = pz / jac
    # Numerical integration to verify p_X integrates to 1
    dx  = (x[1:] - x[:-1]).abs()
    px_mid = (px[1:] + px[:-1]) / 2
    integral = (px_mid * dx).sum().item()
    print('Integral of p_X (should be ~1): {:.4f}'.format(integral))
    # Log-likelihood at specific x values
    for xi in [-8.0, 0.001, 8.0]:
        zi  = np.sign(xi) * abs(xi) ** (1.0/3)
        pzi = np.exp(-0.5 * zi**2) / np.sqrt(2 * np.pi)
        pxi = pzi / (3 * zi**2 + 1e-8)
        print('  x={:5.1f}  z={:.3f}  log p_X={:.3f}'.format(
              xi, zi, np.log(pxi + 1e-30)))

change_of_variables_demo()
```

## Tractable Jacobian Determinants

The key computational challenge is computing log|det J_f|. For a general invertible neural network, this is O(d³). The solution is to design f with a triangular Jacobian, whose determinant is just the product of diagonal entries — O(d). A lower-triangular Jacobian arises from autoregressive models: x_i = f(x_{<i}, z_i), so ∂x_i/∂z_j = 0 for j > i. An upper-triangular Jacobian arises from coupling layers. Both enable O(d) log-determinant computation. This structural constraint on the Jacobian is the core design principle behind all practical flow architectures.

## Coupling Layers: NICE and RealNVP

NICE (Dinh et al. 2014) introduces additive coupling layers: split x into [x₁, x₂], pass x₁ through unchanged, and compute y₂ = x₂ + m(x₁) where m is an arbitrary neural network. The Jacobian is lower-triangular with 1s on the diagonal, so log|det J| = 0. Inversion is trivial: x₂ = y₂ − m(y₁). RealNVP extends this to affine coupling: y₂ = x₂ ⊙ exp(s(x₁)) + t(x₁). The Jacobian diagonal is exp(s(x₁)), giving log|det J| = Σᵢ sᵢ(x₁). Both s and t are unrestricted neural networks; only the coupling structure must be preserved.

```python
import torch
import torch.nn as nn

class AdditiveCoupling(nn.Module):
    '''NICE (Dinh 2014): y2 = x2 + m(x1), y1 = x1. log|det J| = 0.'''
    def __init__(self, d, hidden=64):
        super().__init__()
        d1 = d // 2
        self.d1 = d1
        self.m  = nn.Sequential(
            nn.Linear(d1, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
            nn.Linear(hidden, d - d1))

    def forward(self, x):
        x1, x2  = x[:, :self.d1], x[:, self.d1:]
        y2       = x2 + self.m(x1)              # translate only
        log_det  = torch.zeros(x.size(0))       # unit-volume map
        return torch.cat([x1, y2], dim=1), log_det

    def inverse(self, y):
        y1, y2 = y[:, :self.d1], y[:, self.d1:]
        x2     = y2 - self.m(y1)               # trivial inversion
        return torch.cat([y1, x2], dim=1)

layer = AdditiveCoupling(d=8)
x = torch.randn(4, 8)
y, ld = layer(x)
x_rec = layer.inverse(y)
print('Reconstruction error:', (x - x_rec).abs().max().item())
print('log|det J|:', ld.tolist())  # should be [0,0,0,0]
```

## Exact Log-Likelihood Computation

A normalizing flow stacks K coupling layers: log p_X(x) = log p_Z(z_K) + Σₖ log|det J_fₖ(zₖ₋₁)|, where z₀ = x and z_K is the final latent. The sum of log-determinants accumulates across layers. Training directly maximises this exact log-likelihood — no variational bound, no score matching, no adversarial training. The exact likelihood also enables direct comparison between models in nats or bits-per-dim (BPD = −log₂ p(x) / D for D-dimensional x), unlike GANs where likelihood is unavailable.

```python
import torch
import torch.nn as nn
import torch.distributions as dist

class SimpleNICEFlow(nn.Module):
    def __init__(self, d=8, n_layers=4, hidden=64):
        super().__init__()
        self.layers = nn.ModuleList(
            [AdditiveCoupling(d, hidden=hidden) for _ in range(n_layers)])
        self.prior  = dist.MultivariateNormal(
            torch.zeros(d), torch.eye(d))

    def log_prob(self, x):
        z, log_det = x, torch.zeros(x.size(0))
        for layer in self.layers:
            z, ld = layer(z)
            log_det = log_det + ld
        return self.prior.log_prob(z) + log_det   # exact log p(x)

    def sample(self, n):
        z = self.prior.sample((n,))
        for layer in reversed(self.layers):
            z = layer.inverse(z)
        return z

flow = SimpleNICEFlow(d=8, n_layers=4)
x = torch.randn(16, 8)
log_px = flow.log_prob(x)
print('Mean log p(x): {:.3f}  (NICE: log_det always 0, so = log p_Z(z))'.format(
      log_px.mean().item()))
```

> **Exact Likelihood vs Lower Bound vs Implicit**: VAEs maximise the ELBO = E[log p(x|z)] - KL(q(z|x) || p(z)), a lower bound on log p(x). The gap between ELBO and true log p(x) can be large. GANs have no likelihood at all — the model is implicit and likelihood cannot be computed. Flows compute log p(x) exactly via the change of variables formula. This makes flows uniquely suited for density estimation tasks, anomaly detection, and any application requiring calibrated probabilities.

## Autoregressive Flows: MAF and IAF

Masked Autoregressive Flow (MAF, Papamakarios 2017) uses an autoregressive model to define the scale-and-shift parameters: xᵢ = zᵢ · exp(sᵢ(x_{<i})) + tᵢ(x_{<i}). The Jacobian is lower-triangular so log|det J| = Σ sᵢ. MAF allows parallel density evaluation (all sᵢ can be computed in one forward pass of a MADE network) but requires sequential sampling. Inverse Autoregressive Flow (IAF) reverses this: sampling is parallel but density evaluation is sequential. MAF is better for density estimation; IAF is better for fast sampling (as in VAE decoders).

## Generative Sampling via Inversion

To generate new samples from a flow: (1) sample z ~ p_Z = N(0,I) (trivially fast); (2) apply the inverse f⁻¹ to obtain x = f⁻¹(z). For coupling layers, the inverse is analytically tractable and fast — O(d) per layer, and all dimensions can be computed in parallel. For autoregressive flows (MAF), inversion requires d sequential steps — one per dimension. This sequential dependency makes autoregressive flows slower at generation; coupling-layer flows (RealNVP, Glow) are preferred when fast sampling matters.

```python
import torch

def flow_sample_and_evaluate(flow, n_samples=16):
    '''Generate samples via inversion; compute their log-likelihoods.'''
    flow.eval()
    with torch.no_grad():
        samples = flow.sample(n_samples)
        log_px  = flow.log_prob(samples)
    print('Samples shape : {}'.format(samples.shape))
    print('Sample mean   : {:.4f}'.format(samples.mean().item()))
    print('Sample std    : {:.4f}'.format(samples.std().item()))
    print('Mean log p(x) : {:.3f}'.format(log_px.mean().item()))
    print('BPD (bits/dim): {:.3f}'.format(-log_px.mean().item() / (8 * 0.6931)))
    return samples

flow = SimpleNICEFlow(d=8, n_layers=4)
samples = flow_sample_and_evaluate(flow)
print('Flows: exact likelihood + O(d) parallel sampling via coupling inversion.')
```

- Exact log-likelihood: log p_X(x) = log p_Z(f(x)) + log|det J_f(x)| — no bound, no approximation.
- Coupling layers: triangular Jacobian with O(d) determinant; parallel forward and inverse.
- Additive coupling (NICE): log|det J| = 0; volume-preserving; limited expressivity.
- Affine coupling (RealNVP): log|det J| = sum of log-scales; more expressive.
- MAF: parallel density estimation, sequential sampling — best for density estimation tasks.
- IAF: parallel sampling, sequential density — used in VAE decoders for fast generation.
- Glow: 1x1 invertible convolutions + affine coupling for high-resolution image synthesis.

## Comparison: VAE vs GAN vs Flow vs Diffusion

| Property | VAE | GAN | Normalizing Flow | Diffusion |
| --- | --- | --- | --- | --- |
| Exact likelihood | No (ELBO lower bound) | No (implicit) | Yes (change of vars) | No (but tractable bound) |
| Sample quality | Medium | High | Medium | Very high |
| Training stability | Stable | Unstable (adversarial) | Stable (MLE) | Stable |
| Sample speed | Fast (1-step decode) | Fast (1-step G) | Fast (coupling inverse) | Slow (many denoising steps) |
| Latent space | Yes, structured | Partial (z) | Yes, exact inverse | Noise sequence |

---

