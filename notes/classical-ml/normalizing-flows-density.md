---
title: "Normalizing Flows — Exact Likelihood and Change of Variables"
slug: "normalizing-flows-density"
description: "Explore normalizing flows for exact likelihood computation: the change-of-variables formula, RealNVP coupling layers, autoregressive flows MAF and IAF, and using −log p(x) as a principled anomaly score that avoids the approximation errors of VAEs and KDE."
tags: ["anomaly-detection", "density-estimation", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm9ybWFsaXppbmcgZmxvd3MgYXJlIGdlbmVyYXRpdmUgbW9kZWxzIHRoYXQgbGVhcm4gYSBiaWplY3RpdmUgdHJhbnNmb3JtYXRpb24gVCBiZXR3ZWVuIGEgc2ltcGxlIGJhc2UgZGlzdHJpYnV0aW9uIChHYXVzc2lhbikgYW5kIHRoZSBjb21wbGV4IGRhdGEgZGlzdHJpYnV0aW9uLiBCZWNhdXNlIFQgaXMgaW52ZXJ0aWJsZSBhbmQgaGFzIGEgdHJhY3RhYmxlIEphY29iaWFuIGRldGVybWluYW50LCB0aGUgbW9kZWwgY2FuIGNvbXB1dGUgdGhlIGV4YWN0IGxvZy1saWtlbGlob29kIG9mIGFueSBkYXRhIHBvaW50IOKAlCBubyBFTEJPIGFwcHJveGltYXRpb24sIG5vIGtlcm5lbCBiYW5kd2lkdGggdHVuaW5nLiBUaGUgbG9nLWxpa2VsaWhvb2QgaXMgdGhlcmVmb3JlIGEgcHJpbmNpcGxlZCBhbm9tYWx5IHNjb3JlIHdpdGggc3Ryb25nIHRoZW9yZXRpY2FsIG1vdGl2YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hhbmdlIG9mIFZhcmlhYmxlcyBhbmQgRXhhY3QgTGlrZWxpaG9vZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSWYgeiA9IFTigbvCuSh4KSB3aGVyZSB6IH4gcF9aIChzdGFuZGFyZCBHYXVzc2lhbikgYW5kIFQgaXMgYSBiaWplY3Rpb24sIHRoZW4gYnkgdGhlIGNoYW5nZS1vZi12YXJpYWJsZXMgZm9ybXVsYTogbG9nIHBfWCh4KSA9IGxvZyBwX1ooVOKBu8K5KHgpKSArIGxvZyB8ZGV0IEpfe1TigbvCuX0oeCl8LiBUaGUgZmlyc3QgdGVybSBpcyB0aGUgbG9nLXByb2JhYmlsaXR5IG9mIHRoZSBsYXRlbnQgY29kZSB1bmRlciB0aGUgcHJpb3I7IHRoZSBzZWNvbmQgdGVybSBpcyB0aGUgbG9nIGFic29sdXRlIEphY29iaWFuIGRldGVybWluYW50IHRoYXQgYWNjb3VudHMgZm9yIHRoZSB2b2x1bWUgY2hhbmdlIG9mIHRoZSB0cmFuc2Zvcm1hdGlvbi4gVG8gdHJhaW4gYSBmbG93IHdlIG1heGltaXNlIM6j4bWiIGxvZyBwX1goeOG1oikgZGlyZWN0bHkg4oCUIG5vIHZhcmlhdGlvbmFsIGJvdW5kIG5lZWRlZC4gQXQgaW5mZXJlbmNlIHRoZSBhbm9tYWx5IHNjb3JlIGlzIOKIkmxvZyBwX1goeCkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuY2xhc3MgQWZmaW5lRmxvdzFEKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3U2ltcGxlIDFEIG5vcm1hbGl6aW5nIGZsb3c6IHggPSBleHAocykqeiArIHQsIHBhcmFtZXRlcmlzZWQgYnkgKHMsdCkuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fbGF5ZXJzPTQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5sb2dfcyA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcyhuX2xheWVycykpXG4gICAgICAgIHNlbGYudCAgICAgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mobl9sYXllcnMpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeik6XG4gICAgICAgIGxvZ19kZXQgPSAwLjBcbiAgICAgICAgeCA9IHpcbiAgICAgICAgZm9yIGxzLCB0IGluIHppcChzZWxmLmxvZ19zLCBzZWxmLnQpOlxuICAgICAgICAgICAgeCA9IHRvcmNoLmV4cChscykgKiB4ICsgdFxuICAgICAgICAgICAgbG9nX2RldCArPSBsc1xuICAgICAgICByZXR1cm4geCwgbG9nX2RldFxuXG4gICAgZGVmIGludmVyc2Uoc2VsZiwgeCk6XG4gICAgICAgIHogPSB4XG4gICAgICAgIGZvciBscywgdCBpbiB6aXAocmV2ZXJzZWQobGlzdChzZWxmLmxvZ19zKSksXG4gICAgICAgICAgICAgICAgICAgICAgICAgcmV2ZXJzZWQobGlzdChzZWxmLnQpKSk6XG4gICAgICAgICAgICB6ID0gKHogLSB0KSAqIHRvcmNoLmV4cCgtbHMpXG4gICAgICAgIHJldHVybiB6XG5cbiAgICBkZWYgbG9nX3Byb2Ioc2VsZiwgeCk6XG4gICAgICAgIHogPSBzZWxmLmludmVyc2UoeClcbiAgICAgICAgbG9nX3B6ID0gLTAuNSAqICh6ICoqIDIgKyBucC5sb2coMiAqIG5wLnBpKSlcbiAgICAgICAgbG9nX2RldCA9IHNlbGYubG9nX3Muc3VtKClcbiAgICAgICAgcmV0dXJuIGxvZ19weiAtIGxvZ19kZXQgICMgbG9nIHBfWCh4KVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuZmxvdyA9IEFmZmluZUZsb3cxRCgpXG5vcHQgPSB0b3JjaC5vcHRpbS5BZGFtKGZsb3cucGFyYW1ldGVycygpLCBscj0wLjA1KVxuWF90ciA9IHRvcmNoLnJhbmRuKDUwMCkgKiAyICsgMSAgIyBzaGlmdGVkIEdhdXNzaWFuXG5mb3Igc3RlcCBpbiByYW5nZSgzMDApOlxuICAgIG9wdC56ZXJvX2dyYWQoKVxuICAgIGxvc3MgPSAtZmxvdy5sb2dfcHJvYihYX3RyKS5tZWFuKClcbiAgICBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbnByaW50KGZcdTAwMjdGaW5hbCBOTEw6IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvdXBsaW5nIExheWVyczogUmVhbE5WUCBBcmNoaXRlY3R1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlYWxOVlAgKERpbmggZXQgYWwuLCAyMDE3KSB1c2VzIGFmZmluZSBjb3VwbGluZyBsYXllcnMgdG8gYnVpbGQgYW4gZXhwcmVzc2l2ZSBiaWplY3Rpb24gd2l0aCB0cmFjdGFibGUgSmFjb2JpYW4uIEluIGVhY2ggbGF5ZXIsIHRoZSBpbnB1dCB4IGlzIHNwbGl0IGludG8gKHhfYSwgeF9iKS4gVGhlIG91dHB1dCBpczogeFx1MDAyN19hID0geF9hICh1bmNoYW5nZWQpLCB4XHUwMDI3X2IgPSB4X2Ig4oqZIGV4cChzKHhfYSkpICsgdCh4X2EpIHdoZXJlIHMgYW5kIHQgYXJlIGFyYml0cmFyeSBuZXVyYWwgbmV0d29ya3MuIFRoZSBKYWNvYmlhbiBpcyBsb3dlci10cmlhbmd1bGFyIHdpdGggZGlhZ29uYWwgZXhwKHMoeF9hKSksIHNvIGRldCBKID0gZXhwKM6jIHMoeF9hKSkg4oCUIGNvbXB1dGVkIGluIE8oZCkgd2l0aG91dCBhbnkgbWF0cml4IGludmVyc2lvbi4gU3RhY2tpbmcgY291cGxpbmcgbGF5ZXJzIHdpdGggYWx0ZXJuYXRpbmcgbWFza3MgY3JlYXRlcyBhIHVuaXZlcnNhbCBkZW5zaXR5IGVzdGltYXRvci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuXG5jbGFzcyBDb3VwbGluZ0xheWVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGQsIG1hc2spOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5tYXNrID0gbWFza1xuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKGQsIDY0KSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5uLkxpbmVhcig2NCwgNjQpLCBubi5SZUxVKCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbm4uTGluZWFyKDY0LCBkICogMikpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHhfbWFza2VkID0geCAqIHNlbGYubWFza1xuICAgICAgICBzdCA9IHNlbGYubmV0KHhfbWFza2VkKVxuICAgICAgICBzLCB0ID0gc3QuY2h1bmsoMiwgZGltPS0xKVxuICAgICAgICBzID0gdG9yY2gudGFuaChzKSAqICgxIC0gc2VsZi5tYXNrKVxuICAgICAgICB0ID0gdCAqICgxIC0gc2VsZi5tYXNrKVxuICAgICAgICB5ID0geF9tYXNrZWQgKyAoMSAtIHNlbGYubWFzaykgKiAoeCAqIHRvcmNoLmV4cChzKSArIHQpXG4gICAgICAgIGxvZ19kZXQgPSBzLnN1bShkaW09LTEpXG4gICAgICAgIHJldHVybiB5LCBsb2dfZGV0XG4gICAgZGVmIGludmVyc2Uoc2VsZiwgeSk6XG4gICAgICAgIHlfbWFza2VkID0geSAqIHNlbGYubWFza1xuICAgICAgICBzdCA9IHNlbGYubmV0KHlfbWFza2VkKVxuICAgICAgICBzLCB0ID0gc3QuY2h1bmsoMiwgZGltPS0xKVxuICAgICAgICBzID0gdG9yY2gudGFuaChzKSAqICgxIC0gc2VsZi5tYXNrKVxuICAgICAgICB0ID0gdCAqICgxIC0gc2VsZi5tYXNrKVxuICAgICAgICByZXR1cm4geV9tYXNrZWQgKyAoMSAtIHNlbGYubWFzaykgKiAoKHkgLSB0KSAqIHRvcmNoLmV4cCgtcykpXG5cbmQgPSAyXG5tYXNrX2EgPSB0b3JjaC50ZW5zb3IoWzEuLCAwLl0pXG5tYXNrX2IgPSB0b3JjaC50ZW5zb3IoWzAuLCAxLl0pXG5sYXllcnMgPSBbQ291cGxpbmdMYXllcihkLCBtYXNrX2EpLCBDb3VwbGluZ0xheWVyKGQsIG1hc2tfYildICogM1xucHJpbnQoZlx1MDAyN1JlYWxOVlAgd2l0aCB7bGVuKGxheWVycyl9IGNvdXBsaW5nIGxheWVycyBvbiBkPXtkfVx1MDAyNylcblhfMmQgPSB0b3JjaC5yYW5kbigyMDAsIGQpXG5sb2dfZGV0X3RvdGFsID0gMC4wXG54ID0gWF8yZFxuZm9yIGxheWVyIGluIGxheWVyczpcbiAgICB4LCBsZCA9IGxheWVyKHgpXG4gICAgbG9nX2RldF90b3RhbCArPSBsZFxucHJpbnQoZlx1MDAyN01lYW4gbG9nfGRldCBKfDoge2xvZ19kZXRfdG90YWwubWVhbigpLml0ZW0oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1dG9yZWdyZXNzaXZlIEZsb3dzOiBNQUYgYW5kIElBRiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWFza2VkIEF1dG9yZWdyZXNzaXZlIEZsb3cgKE1BRikgc2V0cyBlYWNoIG91dHB1dCB44bWiID0gz4PhtaIoeF97XHUwMDNjaX0pwrd64bWiICsgzrzhtaIoeF97XHUwMDNjaX0pIHdoZXJlIM68IGFuZCDPgyBhcmUgY29tcHV0ZWQgYnkgYSBNQURFIG5ldHdvcmsuIFRoZSBKYWNvYmlhbiBpcyB0cmlhbmd1bGFyIChkZXQgSiA9IM6g4bWiIM+D4bWiKSDigJQgdHJhY3RhYmxlLiBEZW5zaXR5IGV2YWx1YXRpb24gKGZvcndhcmQgcGFzcyB0aHJvdWdoIE1BREUpIGlzIE8oZCk7IHNhbXBsaW5nIGlzIE8oZMKyKSBiZWNhdXNlIGVhY2ggZGltZW5zaW9uIGRlcGVuZHMgb24gdGhlIHByZXZpb3VzIG9uZXMsIHJlcXVpcmluZyBzZXF1ZW50aWFsIGdlbmVyYXRpb24uIEludmVyc2UgQXV0b3JlZ3Jlc3NpdmUgRmxvdyAoSUFGKSBzd2FwcyB0aGUgcm9sZXM6IHNhbXBsaW5nIGlzIE8oZCksIGRlbnNpdHkgZXZhbHVhdGlvbiBpcyBPKGTCsikuIENob29zZSBNQUYgZm9yIGFub21hbHkgZGV0ZWN0aW9uIChmYXN0IHNjb3JpbmcpLCBJQUYgZm9yIGdlbmVyYXRpb24gdGFza3MuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJNQUY6IGRlbnNpdHkgZXZhbHVhdGlvbiBPKGQpLCBzYW1wbGluZyBPKGTCsikg4oCUIHByZWZlcnJlZCBmb3IgYW5vbWFseSBkZXRlY3Rpb24gc2NvcmluZy4iLCJJQUY6IHNhbXBsaW5nIE8oZCksIGRlbnNpdHkgZXZhbHVhdGlvbiBPKGTCsikg4oCUIHByZWZlcnJlZCBmb3IgZ2VuZXJhdGlvbjsgdXNlZCBpbiB2YXJpYXRpb25hbCBpbmZlcmVuY2UuIiwiR2xvdzogMcOXMSBpbnZlcnRpYmxlIGNvbnZvbHV0aW9ucyArIGFjdG5vcm0gKyBhZmZpbmUgY291cGxpbmcgZm9yIGltYWdlIGZsb3dzOyBPKGQgbG9nIGQpIEphY29iaWFuIHZpYSBMVSBkZWNvbXBvc2l0aW9uLiIsIkZGSk9SRDogY29udGludW91cyBub3JtYWxpemluZyBmbG93IHZpYSBPREU7IGV4YWN0IGxvZy1kZXQgYnV0IHJlcXVpcmVzIE9ERSBzb2x2ZXIg4oCUIHZlcnkgZmxleGlibGUuIiwiTklDRTogYWRkaXRpdmUgY291cGxpbmcgKHM9MSkg4oCUIG5vIGxvZy1kZXQgdGVybTsgc2ltcGxlciBidXQgbGVzcyBleHByZXNzaXZlIHRoYW4gUmVhbE5WUC4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTm9ybWFsaXppbmcgRmxvd3MgZm9yIEFub21hbHkgRGV0ZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZmxvdyBhbm9tYWx5IHNjb3JlIOKIkmxvZyBwX1goeCkgaXMgZXhhY3Qg4oCUIG5vdCBhIGJvdW5kIOKAlCBhbmQgaW5oZXJpdHMgdGhlIGV4cHJlc3NpdmUgcG93ZXIgb2YgdGhlIGJpamVjdGl2ZSBuZXR3b3JrLiBUcmFpbmluZyBpcyBzdHJhaWdodGZvcndhcmQ6IG1pbmltaXNlIHRoZSBOTEwgb24gY2xlYW4gdHJhaW5pbmcgZGF0YS4gQXQgdGVzdCB0aW1lLCBmbGFnIHBvaW50cyB3aXRoIOKIkmxvZyBwX1goeCkgYWJvdmUgdGhlICgx4oiSzrEpIHF1YW50aWxlIG9mIHRyYWluaW5nIHNjb3Jlcy4gRmxvdy1iYXNlZCBkZXRlY3RvcnMgZXhjZWwgd2hlbiB0aGUgbm9ybWFsIGRhdGEgZGlzdHJpYnV0aW9uIGlzIGNvbXBsZXggKG11bHRpbW9kYWwsIG5vbi1HYXVzc2lhbikgYW5kIGEgbGFyZ2UgdHJhaW5pbmcgc2V0IGlzIGF2YWlsYWJsZSB0byBqdXN0aWZ5IHRoZSBuZXVyYWwgbmV0d29yayBjb21wbGV4aXR5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuXG5jbGFzcyBTaW1wbGVGbG93KG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3TWluaW1hbCBmbG93OiB0d28gY291cGxpbmcgbGF5ZXJzIG9uIDJEIGRhdGEgZm9yIGFub21hbHkgZGV0ZWN0aW9uLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIG0wID0gdG9yY2gudGVuc29yKFsxLiwgMC5dKVxuICAgICAgICBtMSA9IHRvcmNoLnRlbnNvcihbMC4sIDEuXSlcbiAgICAgICAgc2VsZi5sMCA9IENvdXBsaW5nTGF5ZXIoMiwgbTApXG4gICAgICAgIHNlbGYubDEgPSBDb3VwbGluZ0xheWVyKDIsIG0xKVxuXG4gICAgZGVmIGxvZ19wcm9iKHNlbGYsIHgpOlxuICAgICAgICB6LCBsZCA9IHNlbGYubDAoeClcbiAgICAgICAgeiwgbGQyID0gc2VsZi5sMSh6KVxuICAgICAgICBsb2dfcHogPSAtMC41ICogKHogKiogMikuc3VtKGRpbT0tMSkgLSBucC5sb2coMiAqIG5wLnBpKVxuICAgICAgICByZXR1cm4gbG9nX3B6ICsgbGQgKyBsZDJcblxubnAucmFuZG9tLnNlZWQoNylcbnRvcmNoLm1hbnVhbF9zZWVkKDcpXG5mbG93MiA9IFNpbXBsZUZsb3coKVxub3B0ID0gdG9yY2gub3B0aW0uQWRhbShmbG93Mi5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5YX3RyID0gdG9yY2gudGVuc29yKG5wLnJhbmRvbS5yYW5kbig2MDAsIDIpLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuZm9yIF8gaW4gcmFuZ2UoMzAwKTpcbiAgICBvcHQuemVyb19ncmFkKClcbiAgICAoLWZsb3cyLmxvZ19wcm9iKFhfdHIpLm1lYW4oKSkuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuXG5YX24gPSB0b3JjaC50ZW5zb3IobnAucmFuZG9tLnJhbmRuKDEwMCwgMiksIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG5YX2EgPSB0b3JjaC50ZW5zb3IobnAucmFuZG9tLnJhbmRuKDMwLCAyKSowLjMgKyA0LCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuWF9hbGwgPSB0b3JjaC5jYXQoW1hfbiwgWF9hXSlcbnkgPSBucC5hcnJheShbMF0qMTAwICsgWzFdKjMwKVxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgc2NvcmVzID0gLWZsb3cyLmxvZ19wcm9iKFhfYWxsKS5udW1weSgpXG5wcmludChmXHUwMDI3RmxvdyBBVVJPQzoge3JvY19hdWNfc2NvcmUoeSwgc2NvcmVzKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmluZyBGbG93LUJhc2VkIHZzIEFsdGVybmF0aXZlIERlbnNpdHkgRXN0aW1hdG9ycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR01NIGFuZCBLREUgc2VydmUgYXMgZmFzdCBwYXJhbWV0cmljIGFuZCBub24tcGFyYW1ldHJpYyBiYXNlbGluZXMgcmVzcGVjdGl2ZWx5LiBHTU0gaXMgZmFzdCB0byB0cmFpbiBhbmQgaGFuZGxlcyBlbGxpcHRpY2FsIGNsdXN0ZXJzIHdlbGw7IEtERSBhZGFwdHMgdG8gYXJiaXRyYXJ5IHNoYXBlcyBidXQgZGVncmFkZXMgaW4gaGlnaCBkaW1lbnNpb25zLiBUaGUgbm9ybWFsaXppbmcgZmxvdyB0eXBpY2FsbHkgYWNoaWV2ZXMgdGhlIGJlc3Qgc2VwYXJhdGlvbiB3aGVuIHRoZSBub3JtYWwgZGF0YSBkaXN0cmlidXRpb24gaXMgZ2VudWluZWx5IGNvbXBsZXggYW5kIG11bHRpbW9kYWwuIE9uIHNpbXBsZXIgZGlzdHJpYnV0aW9ucyAodW5pbW9kYWwgR2F1c3NpYW4pLCBHTU0gYW5kIEtERSBtYXRjaCBvciBiZWF0IHRoZSBmbG93IHdoaWxlIHRyYWluaW5nIGluIGEgZnJhY3Rpb24gb2YgdGhlIHRpbWUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLm5laWdoYm9ycyBpbXBvcnQgS2VybmVsRGVuc2l0eVxuZnJvbSBza2xlYXJuLm1peHR1cmUgaW1wb3J0IEdhdXNzaWFuTWl4dHVyZVxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IHJvY19hdWNfc2NvcmVcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IEdyaWRTZWFyY2hDVlxuXG5ucC5yYW5kb20uc2VlZCgxMClcblhfdHJhaW4gPSBucC52c3RhY2soW25wLnJhbmRvbS5yYW5kbig0MDAsIDIpLFxuICAgICAgICAgICAgICAgICAgICAgIG5wLnJhbmRvbS5yYW5kbigxMDAsIDIpICogMC41ICsgWzMsIDNdXSlcblhfbl90ZXN0ID0gbnAudnN0YWNrKFtucC5yYW5kb20ucmFuZG4oODAsIDIpLFxuICAgICAgICAgICAgICAgICAgICAgICBucC5yYW5kb20ucmFuZG4oMjAsIDIpICogMC41ICsgWzMsIDNdXSlcblhfYV90ZXN0ID0gbnAucmFuZG9tLnVuaWZvcm0oLTUsIDgsICgyNSwgMikpXG5YX3RlID0gbnAudnN0YWNrKFtYX25fdGVzdCwgWF9hX3Rlc3RdKVxueV90ZSA9IG5wLmFycmF5KFswXSoxMDAgKyBbMV0qMjUpXG5cbiMgR01NXG5nbW0gPSBHYXVzc2lhbk1peHR1cmUobl9jb21wb25lbnRzPTMsIG5faW5pdD01LCByYW5kb21fc3RhdGU9MCkuZml0KFhfdHJhaW4pXG5zX2dtbSA9IC1nbW0uc2NvcmVfc2FtcGxlcyhYX3RlKVxuXG4jIEtERVxuYndzID0gbnAubG9nc3BhY2UoLTEsIDEsIDE1KVxua2RlID0gR3JpZFNlYXJjaENWKEtlcm5lbERlbnNpdHkoKSwge1x1MDAyN2JhbmR3aWR0aFx1MDAyNzogYndzfSwgY3Y9MykuZml0KFhfdHJhaW4pXG5zX2tkZSA9IC1rZGUuYmVzdF9lc3RpbWF0b3JfLnNjb3JlX3NhbXBsZXMoWF90ZSlcblxucHJpbnQoZlx1MDAyN0dNTSAgQVVST0M6IHtyb2NfYXVjX3Njb3JlKHlfdGUsIHNfZ21tKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0tERSAgQVVST0M6IHtyb2NfYXVjX3Njb3JlKHlfdGUsIHNfa2RlKTouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3Tm90ZTogZmxvdyBBVVJPQyBmcm9tIHByZXZpb3VzIGNlbGw7IHR5cGljYWxseSBoaWdoZXN0IG9uIGNvbXBsZXggZGVuc2l0aWVzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIaWdoLURpbWVuc2lvbmFsIENoYWxsZW5nZXMgYW5kIFByYWN0aWNhbCBHdWlkYW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm9ybWFsaXppbmcgZmxvd3MgZmFjZSB0d28gY29tcGV0aW5nIGNvbnN0cmFpbnRzIGluIGhpZ2ggZGltZW5zaW9uczogdGhlIGJpamVjdGl2ZSBuZXR3b3JrIG11c3QgYmUgZXhwcmVzc2l2ZSBlbm91Z2ggdG8gbW9kZWwgY29tcGxleCBkaXN0cmlidXRpb25zLCB5ZXQgcmVtYWluIGludmVydGlibGUgd2l0aCBhIHRyYWN0YWJsZSBKYWNvYmlhbi4gQ291cGxpbmcgbGF5ZXJzIGFkZHJlc3MgdGhpcyB2aWEgdHJpYW5ndWxhciBzdHJ1Y3R1cmUsIGJ1dCByZXF1aXJlIG1hbnkgbGF5ZXJzIGZvciBoaWdoIGV4cHJlc3NpdmVuZXNzLiBQcmFjdGljYWwgcmVjb21tZW5kYXRpb25zOiB1c2UgUmVhbE5WUCB3aXRoIGF0IGxlYXN0IDggY291cGxpbmcgbGF5ZXJzIGZvciBkXHUwMDNlMjA7IGFwcGx5IG11bHRpLXNjYWxlIGFyY2hpdGVjdHVyZXMgKHNxdWVlemUtYW5kLXNwbGl0KSBmb3IgaW1hZ2UgZGF0YTsgdXNlIGJhdGNoIG5vcm1hbGlzYXRpb24gYmV0d2VlbiBsYXllcnMgdG8gc3RhYmlsaXNlIHRyYWluaW5nOyBtb25pdG9yIE5MTCBvbiBhIHZhbGlkYXRpb24gc2V0IGFuZCBzdG9wIGVhcmx5IGlmIGl0IGJlZ2lucyByaXNpbmcuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJGbG93IHZzIFZBRSBmb3IgQW5vbWFseSBEZXRlY3Rpb24iLCJjb250ZW50IjoiRmxvd3MgcHJvdmlkZSBleGFjdCBsaWtlbGlob29kcyBidXQgcmVxdWlyZSBsYXJnZSBkYXRhc2V0cyAodGhvdXNhbmRzIG9mIG5vcm1hbCBleGFtcGxlcykgdG8gdHJhaW4gYSByZWxpYWJsZSBiaWplY3Rpb24uIFZBRXMgYXJlIGZhc3RlciB0byB0cmFpbiBhbmQgd29yayB3aXRoIHNtYWxsZXIgZGF0YXNldHMsIGJ1dCB0aGVpciBFTEJPIGlzIGEgbG93ZXIgYm91bmQuIEZvciB0YWJ1bGFyIGFub21hbHkgZGV0ZWN0aW9uIHdpdGggXHUwMDNjNUsgbm9ybWFsIHNhbXBsZXMsIGEgR01NIG9yIEtERSBpcyBvZnRlbiBhcyBhY2N1cmF0ZSBhcyBhIGZsb3cgYW5kIHRyYWlucyBpbiBzZWNvbmRzLiBSZXNlcnZlIGZsb3dzIGZvciBpbWFnZSBvciBoaWdoLWNvbXBsZXhpdHkgc3RydWN0dXJlZCBkYXRhIHdoZXJlIGV4YWN0IGxpa2VsaWhvb2RzIG1hdHRlci4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiRXhhY3QgTGlrZWxpaG9vZCIsIkludmVydGlibGUiLCJMYXRlbnQgU3BhY2UiLCJBbm9tYWx5IFNjb3JlIiwiQ29tcHV0YXRpb25hbCBDb3N0Il0sInJvd3MiOltbIk5vcm1hbGl6aW5nIEZsb3ciLCJZZXMiLCJZZXMgKGJpamVjdGlvbikiLCJTdHJ1Y3R1cmVkIHByaW9yIiwi4oiSbG9nIHBfZmxvdyh4KSIsIkhpZ2gg4oCUIGRlZXAgYmlqZWN0aW9uIl0sWyJWQUUiLCJObyAoRUxCTykiLCJObyIsIlN0b2NoYXN0aWMgZW5jb2RlciIsIuKIkkVMQk8gb3IgSVdBRSIsIk1lZGl1bSDigJQgZW5jb2RlcitkZWNvZGVyIl0sWyJHTU0iLCJZZXMiLCJObyIsIkRpc2NyZXRlIG1peHR1cmUiLCLiiJJsb2cgcF9HTU0oeCkiLCJMb3cg4oCUIEVNIGFsZ29yaXRobSJdLFsiS0RFIiwiWWVzIChhc3ltcHRvdGljKSIsIk5vIiwiTm9uZSIsIuKIkmxvZyBwzIIoeCkiLCJMb3cgZml0LCBPKG4pIHF1ZXJ5Il1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNob29zZSBub3JtYWxpemluZyBmbG93cyB3aGVuIHlvdSBuZWVkIGV4YWN0IGxpa2VsaWhvb2RzLCBoYXZlIHN1ZmZpY2llbnQgZGF0YSB0byB0cmFpbiBhIGRlZXAgYmlqZWN0aXZlIG5ldHdvcmssIGFuZCB0aGUgZGF0YSBkaXN0cmlidXRpb24gaXMgZ2VudWluZWx5IGNvbXBsZXguIEZvciBtb3N0IGluZHVzdHJpYWwgYW5vbWFseSBkZXRlY3Rpb24gdGFza3Mgb24gdGFidWxhciBkYXRhLCBhIHdlbGwtdHVuZWQgR01NIG9yIEtERSBwcm92aWRlcyBjb21wZXRpdGl2ZSBwZXJmb3JtYW5jZSBhdCBhIGZyYWN0aW9uIG9mIHRoZSBlbmdpbmVlcmluZyBjb3N0LiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Normalizing Flows — Exact Likelihood and Change of Variables

Normalizing flows are generative models that learn a bijective transformation T between a simple base distribution (Gaussian) and the complex data distribution. Because T is invertible and has a tractable Jacobian determinant, the model can compute the exact log-likelihood of any data point — no ELBO approximation, no kernel bandwidth tuning. The log-likelihood is therefore a principled anomaly score with strong theoretical motivation.

## Change of Variables and Exact Likelihood

If z = T⁻¹(x) where z ~ p_Z (standard Gaussian) and T is a bijection, then by the change-of-variables formula: log p_X(x) = log p_Z(T⁻¹(x)) + log |det J_{T⁻¹}(x)|. The first term is the log-probability of the latent code under the prior; the second term is the log absolute Jacobian determinant that accounts for the volume change of the transformation. To train a flow we maximise Σᵢ log p_X(xᵢ) directly — no variational bound needed. At inference the anomaly score is −log p_X(x).

```python
import torch
import torch.nn as nn
import numpy as np

class AffineFlow1D(nn.Module):
    '''Simple 1D normalizing flow: x = exp(s)*z + t, parameterised by (s,t).'''
    def __init__(self, n_layers=4):
        super().__init__()
        self.log_s = nn.Parameter(torch.zeros(n_layers))
        self.t     = nn.Parameter(torch.zeros(n_layers))

    def forward(self, z):
        log_det = 0.0
        x = z
        for ls, t in zip(self.log_s, self.t):
            x = torch.exp(ls) * x + t
            log_det += ls
        return x, log_det

    def inverse(self, x):
        z = x
        for ls, t in zip(reversed(list(self.log_s)),
                         reversed(list(self.t))):
            z = (z - t) * torch.exp(-ls)
        return z

    def log_prob(self, x):
        z = self.inverse(x)
        log_pz = -0.5 * (z ** 2 + np.log(2 * np.pi))
        log_det = self.log_s.sum()
        return log_pz - log_det  # log p_X(x)

torch.manual_seed(0)
flow = AffineFlow1D()
opt = torch.optim.Adam(flow.parameters(), lr=0.05)
X_tr = torch.randn(500) * 2 + 1  # shifted Gaussian
for step in range(300):
    opt.zero_grad()
    loss = -flow.log_prob(X_tr).mean()
    loss.backward(); opt.step()
print(f'Final NLL: {loss.item():.4f}')
```

## Coupling Layers: RealNVP Architecture

RealNVP (Dinh et al., 2017) uses affine coupling layers to build an expressive bijection with tractable Jacobian. In each layer, the input x is split into (x_a, x_b). The output is: x'_a = x_a (unchanged), x'_b = x_b ⊙ exp(s(x_a)) + t(x_a) where s and t are arbitrary neural networks. The Jacobian is lower-triangular with diagonal exp(s(x_a)), so det J = exp(Σ s(x_a)) — computed in O(d) without any matrix inversion. Stacking coupling layers with alternating masks creates a universal density estimator.

```python
import torch
import torch.nn as nn
import numpy as np

class CouplingLayer(nn.Module):
    def __init__(self, d, mask):
        super().__init__()
        self.mask = mask
        self.net = nn.Sequential(nn.Linear(d, 64), nn.ReLU(),
                                  nn.Linear(64, 64), nn.ReLU(),
                                  nn.Linear(64, d * 2))
    def forward(self, x):
        x_masked = x * self.mask
        st = self.net(x_masked)
        s, t = st.chunk(2, dim=-1)
        s = torch.tanh(s) * (1 - self.mask)
        t = t * (1 - self.mask)
        y = x_masked + (1 - self.mask) * (x * torch.exp(s) + t)
        log_det = s.sum(dim=-1)
        return y, log_det
    def inverse(self, y):
        y_masked = y * self.mask
        st = self.net(y_masked)
        s, t = st.chunk(2, dim=-1)
        s = torch.tanh(s) * (1 - self.mask)
        t = t * (1 - self.mask)
        return y_masked + (1 - self.mask) * ((y - t) * torch.exp(-s))

d = 2
mask_a = torch.tensor([1., 0.])
mask_b = torch.tensor([0., 1.])
layers = [CouplingLayer(d, mask_a), CouplingLayer(d, mask_b)] * 3
print(f'RealNVP with {len(layers)} coupling layers on d={d}')
X_2d = torch.randn(200, d)
log_det_total = 0.0
x = X_2d
for layer in layers:
    x, ld = layer(x)
    log_det_total += ld
print(f'Mean log|det J|: {log_det_total.mean().item():.4f}')
```

## Autoregressive Flows: MAF and IAF

Masked Autoregressive Flow (MAF) sets each output xᵢ = σᵢ(x_{<i})·zᵢ + μᵢ(x_{<i}) where μ and σ are computed by a MADE network. The Jacobian is triangular (det J = Πᵢ σᵢ) — tractable. Density evaluation (forward pass through MADE) is O(d); sampling is O(d²) because each dimension depends on the previous ones, requiring sequential generation. Inverse Autoregressive Flow (IAF) swaps the roles: sampling is O(d), density evaluation is O(d²). Choose MAF for anomaly detection (fast scoring), IAF for generation tasks.

- MAF: density evaluation O(d), sampling O(d²) — preferred for anomaly detection scoring.
- IAF: sampling O(d), density evaluation O(d²) — preferred for generation; used in variational inference.
- Glow: 1×1 invertible convolutions + actnorm + affine coupling for image flows; O(d log d) Jacobian via LU decomposition.
- FFJORD: continuous normalizing flow via ODE; exact log-det but requires ODE solver — very flexible.
- NICE: additive coupling (s=1) — no log-det term; simpler but less expressive than RealNVP.

## Normalizing Flows for Anomaly Detection

The flow anomaly score −log p_X(x) is exact — not a bound — and inherits the expressive power of the bijective network. Training is straightforward: minimise the NLL on clean training data. At test time, flag points with −log p_X(x) above the (1−α) quantile of training scores. Flow-based detectors excel when the normal data distribution is complex (multimodal, non-Gaussian) and a large training set is available to justify the neural network complexity.

```python
import torch
import torch.nn as nn
import numpy as np
from sklearn.metrics import roc_auc_score

class SimpleFlow(nn.Module):
    '''Minimal flow: two coupling layers on 2D data for anomaly detection.'''
    def __init__(self):
        super().__init__()
        m0 = torch.tensor([1., 0.])
        m1 = torch.tensor([0., 1.])
        self.l0 = CouplingLayer(2, m0)
        self.l1 = CouplingLayer(2, m1)

    def log_prob(self, x):
        z, ld = self.l0(x)
        z, ld2 = self.l1(z)
        log_pz = -0.5 * (z ** 2).sum(dim=-1) - np.log(2 * np.pi)
        return log_pz + ld + ld2

np.random.seed(7)
torch.manual_seed(7)
flow2 = SimpleFlow()
opt = torch.optim.Adam(flow2.parameters(), lr=1e-3)
X_tr = torch.tensor(np.random.randn(600, 2), dtype=torch.float32)
for _ in range(300):
    opt.zero_grad()
    (-flow2.log_prob(X_tr).mean()).backward(); opt.step()

X_n = torch.tensor(np.random.randn(100, 2), dtype=torch.float32)
X_a = torch.tensor(np.random.randn(30, 2)*0.3 + 4, dtype=torch.float32)
X_all = torch.cat([X_n, X_a])
y = np.array([0]*100 + [1]*30)
with torch.no_grad():
    scores = -flow2.log_prob(X_all).numpy()
print(f'Flow AUROC: {roc_auc_score(y, scores):.4f}')
```

## Comparing Flow-Based vs Alternative Density Estimators

GMM and KDE serve as fast parametric and non-parametric baselines respectively. GMM is fast to train and handles elliptical clusters well; KDE adapts to arbitrary shapes but degrades in high dimensions. The normalizing flow typically achieves the best separation when the normal data distribution is genuinely complex and multimodal. On simpler distributions (unimodal Gaussian), GMM and KDE match or beat the flow while training in a fraction of the time.

```python
import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.mixture import GaussianMixture
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV

np.random.seed(10)
X_train = np.vstack([np.random.randn(400, 2),
                      np.random.randn(100, 2) * 0.5 + [3, 3]])
X_n_test = np.vstack([np.random.randn(80, 2),
                       np.random.randn(20, 2) * 0.5 + [3, 3]])
X_a_test = np.random.uniform(-5, 8, (25, 2))
X_te = np.vstack([X_n_test, X_a_test])
y_te = np.array([0]*100 + [1]*25)

# GMM
gmm = GaussianMixture(n_components=3, n_init=5, random_state=0).fit(X_train)
s_gmm = -gmm.score_samples(X_te)

# KDE
bws = np.logspace(-1, 1, 15)
kde = GridSearchCV(KernelDensity(), {'bandwidth': bws}, cv=3).fit(X_train)
s_kde = -kde.best_estimator_.score_samples(X_te)

print(f'GMM  AUROC: {roc_auc_score(y_te, s_gmm):.4f}')
print(f'KDE  AUROC: {roc_auc_score(y_te, s_kde):.4f}')
print('Note: flow AUROC from previous cell; typically highest on complex densities.')
```

## High-Dimensional Challenges and Practical Guidance

Normalizing flows face two competing constraints in high dimensions: the bijective network must be expressive enough to model complex distributions, yet remain invertible with a tractable Jacobian. Coupling layers address this via triangular structure, but require many layers for high expressiveness. Practical recommendations: use RealNVP with at least 8 coupling layers for d>20; apply multi-scale architectures (squeeze-and-split) for image data; use batch normalisation between layers to stabilise training; monitor NLL on a validation set and stop early if it begins rising.

> **Flow vs VAE for Anomaly Detection**: Flows provide exact likelihoods but require large datasets (thousands of normal examples) to train a reliable bijection. VAEs are faster to train and work with smaller datasets, but their ELBO is a lower bound. For tabular anomaly detection with <5K normal samples, a GMM or KDE is often as accurate as a flow and trains in seconds. Reserve flows for image or high-complexity structured data where exact likelihoods matter.

| Method | Exact Likelihood | Invertible | Latent Space | Anomaly Score | Computational Cost |
| --- | --- | --- | --- | --- | --- |
| Normalizing Flow | Yes | Yes (bijection) | Structured prior | −log p_flow(x) | High — deep bijection |
| VAE | No (ELBO) | No | Stochastic encoder | −ELBO or IWAE | Medium — encoder+decoder |
| GMM | Yes | No | Discrete mixture | −log p_GMM(x) | Low — EM algorithm |
| KDE | Yes (asymptotic) | No | None | −log p̂(x) | Low fit, O(n) query |

Choose normalizing flows when you need exact likelihoods, have sufficient data to train a deep bijective network, and the data distribution is genuinely complex. For most industrial anomaly detection tasks on tabular data, a well-tuned GMM or KDE provides competitive performance at a fraction of the engineering cost.

---

