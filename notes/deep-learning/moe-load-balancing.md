---
title: "MoE Load Balancing"
slug: "moe-load-balancing"
description: "Techniques to prevent expert collapse where a few experts receive nearly all tokens — covering auxiliary losses, expert choice routing, and Z-loss regularization."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gYSBNaXh0dXJlLW9mLUV4cGVydHMgbW9kZWwsIHRoZSByb3V0ZXIgaXMgYSBzbWFsbCBsZWFybmVkIG5ldHdvcmsgdGhhdCBtYXBzIGVhY2ggdG9rZW4gdG8gYSBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb24gb3ZlciBleHBlcnRzLiBMZWZ0IHVuY29uc3RyYWluZWQsIHRoZSByb3V0ZXIgcXVpY2tseSBjb2xsYXBzZXM6IGEgZmV3IGV4cGVydHMgY29uc2lzdGVudGx5IHdpbiB0aGUgc29mdG1heCBjb21wZXRpdGlvbiwgcmVjZWl2ZSB0aGUgbW9zdCB0b2tlbnMsIGFjY3VtdWxhdGUgdGhlIG1vc3QgZ3JhZGllbnQgc2lnbmFsLCBhbmQgYmVjb21lIGV2ZW4gYmV0dGVyIOKAlCB3aGlsZSB0aGUgcmVtYWluaW5nIGV4cGVydHMgc3RhcnZlLiBUaGlzIGZhaWx1cmUgbW9kZSwgY2FsbGVkIGV4cGVydCBjb2xsYXBzZSwgaXMgb25lIG9mIHRoZSBjZW50cmFsIHRyYWluaW5nIGNoYWxsZW5nZXMgaW4gTW9FIGFyY2hpdGVjdHVyZXMuIEFkZHJlc3NpbmcgaXQgcmVxdWlyZXMgZXhwbGljaXQgcmVndWxhcmlzYXRpb24gaW4gdGhlIGxvc3MgZnVuY3Rpb24sIGFsdGVybmF0aXZlIHJvdXRpbmcgc3RyYXRlZ2llcyB0aGF0IHJlbW92ZSB0aGUgY29tcGV0aXRpdmUgZHluYW1pYywgYW5kIGNhcmVmdWwgbW9uaXRvcmluZyB0aHJvdWdob3V0IHRyYWluaW5nLiBUaGlzIG5vdGUgY292ZXJzIHRoZSBmdWxsIHRvb2xraXQ6IGF1eGlsaWFyeSBsb3NzLCBleHBlcnQgY2hvaWNlIHJvdXRpbmcsIFotbG9zcywgYW5kIGNhcGFjaXR5IGZhY3RvcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxvYWQgYmFsYW5jaW5nIGluIE1vRSB0cmFpbmluZyBpcyB0aGUgcHJvYmxlbSBvZiBlbnN1cmluZyBlYWNoIGV4cGVydCBwcm9jZXNzZXMgYXBwcm94aW1hdGVseSAxL04gb2YgYWxsIHRva2VucyB0aHJvdWdob3V0IHRyYWluaW5nLCB3aGlsZSBzdGlsbCBhbGxvd2luZyB0aGUgcm91dGVyIHRvIGRldmVsb3AgbWVhbmluZ2Z1bCBzcGVjaWFsaXNhdGlvbi4gUGVyZmVjdCBiYWxhbmNlIChlYWNoIGV4cGVydCBzZWVzIGV4YWN0bHkgMS9OIHRva2Vucykgd291bGQgcmVxdWlyZSBhIGNvbWJpbmF0b3JpYWwgYXNzaWdubWVudCB0aGF0IGlnbm9yZXMgdG9rZW4tZXhwZXJ0IGFmZmluaXR5OyBwdXJlIGFmZmluaXR5IHJvdXRpbmcgKGVhY2ggdG9rZW4gYWx3YXlzIGdvZXMgdG8gaXRzIG1vc3QgcHJlZmVycmVkIGV4cGVydCkgY29sbGFwc2VzLiBHb29kIGxvYWQgYmFsYW5jaW5nIG1ldGhvZHMgZmluZCBhIG1pZGRsZSBncm91bmQ6IHRoZXkgYWxsb3cgdGhlIHJvdXRlciB0byBwcmVmZXIgY2VydGFpbiBleHBlcnRzIGZvciBjZXJ0YWluIHRva2VucyB3aGlsZSBhZGRpbmcgc29mdCByZWd1bGFyaXNhdGlvbiB0aGF0IGRpc2NvdXJhZ2VzIGV4dHJlbWUgaW1iYWxhbmNlLiBUaGUgbWFpbiBhcHByb2FjaGVzIGFyZTogKDEpIGF1eGlsaWFyeSBsb3NzIG9uIHRoZSByb3V0aW5nIGRpc3RyaWJ1dGlvbiwgKDIpIGV4cGVydCBjaG9pY2Ugcm91dGluZyB3aGVyZSBleHBlcnRzIHNlbGVjdCB0b2tlbnMgcmF0aGVyIHRoYW4gdG9rZW5zIHNlbGVjdGluZyBleHBlcnRzLCAoMykgWi1sb3NzIHRvIHByZXZlbnQgcm91dGVyIGxvZ2l0IGV4cGxvc2lvbiwgYW5kICg0KSBjYXBhY2l0eSBmYWN0b3JzIHdpdGggdG9rZW4gZHJvcHBpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXhwZXJ0IENvbGxhcHNlIFByb2JsZW0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV4cGVydCBjb2xsYXBzZSBvY2N1cnMgYmVjYXVzZSB0aGUgc29mdG1heCByb3V0ZXIgaXMgYSB3aW5uZXItdGFrZXMtYWxsIGZ1bmN0aW9uIGluIGV4cGVjdGF0aW9uLiBJZiBleHBlcnQgMCBoYXBwZW5zIHRvIGJlIGluaXRpYWxpc2VkIHdpdGggc2xpZ2h0bHkgbGFyZ2VyIHdlaWdodHMsIGl0IHJlY2VpdmVzIHNsaWdodGx5IGhpZ2hlciBsb2dpdHMgZm9yIG1hbnkgdG9rZW5zLCBnZXRzIHJvdXRlZCBtb3JlIHRva2VucywgcmVjZWl2ZXMgbW9yZSBncmFkaWVudCwgaW1wcm92ZXMgZmFzdGVyLCBhbmQgd2lucyBhbiBldmVyLWxhcmdlciBzaGFyZSBvZiB0b2tlbnMuIFRoaXMgY3JlYXRlcyBhIHJpY2gtZ2V0LXJpY2hlciBkeW5hbWljIHRoYXQgaXMgcmVpbmZvcmNlZCBhdCBldmVyeSBncmFkaWVudCBzdGVwLiBPbmNlIGFuIGV4cGVydCBkb21pbmF0ZXMg4oCUIHJlY2VpdmluZyBtb3JlIHRoYW4gNTAlIG9mIHRva2VucyDigJQgdGhlIG90aGVyIGV4cGVydHMgcmVjZWl2ZSBzbyBsaXR0bGUgZ3JhZGllbnQgdGhhdCB0aGVpciB3ZWlnaHRzIGJhcmVseSBjaGFuZ2UsIGVmZmVjdGl2ZWx5IGZyZWV6aW5nIHRoZW0uIFJlY292ZXJ5IGZyb20gc2V2ZXJlIGNvbGxhcHNlIGlzIGRpZmZpY3VsdCBiZWNhdXNlIHRoZSBkb21pbmFudCBleHBlcnQgaGFzIGFscmVhZHkgY29udmVyZ2VkIHRvIGEgbG9jYWwgb3B0aW11bSwgYW5kIHRoZSBhdXhpbGlhcnkgbG9zcyBtdXN0IHB1c2ggc3Ryb25nbHkgZW5vdWdoIGFnYWluc3QgaXQgdG8gb3ZlcmNvbWUgdGhpcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlJvdXRlciBsb2dpdHMgZm9yIHRoZSBkb21pbmFudCBleHBlcnQgZ3JvdyBtb25vdG9uaWNhbGx5IHdoaWxlIG90aGVycyBkZWNheSIsIkF1eGlsaWFyeSBsb3NzIGJlY29tZXMgaW5lZmZlY3RpdmUgb25jZSBjb2xsYXBzZSBpcyBzZXZlcmUgKGdyYWRpZW50IGZsb3cgdG8gb3RoZXIgZXhwZXJ0cyBpcyBuZWFyIHplcm8pIiwiVHJhaW5pbmcgbG9zcyBtYXkgc3RpbGwgZGVjcmVhc2UgZXZlbiBkdXJpbmcgY29sbGFwc2Ug4oCUIHRoZSBMTSBvYmplY3RpdmUgZG9lcyBub3QgZGV0ZWN0IGl0IiwiRXhwZXJ0IHV0aWxpc2F0aW9uIGVudHJvcHkgZHJvcHMgZnJvbSBsb2coTikgdG8gbmVhciAwIG92ZXIgaHVuZHJlZHMgb2Ygc3RlcHMiLCJSZWNvdmVyeSByZXF1aXJlcyBlaXRoZXIgdmVyeSBzdHJvbmcgYWxwaGEgb3IgYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzIHRvIHRoZSByb3V0ZXIiLCJQcmV2ZW50aW9uIChzdHJvbmcgYWxwaGEgZnJvbSBzdGVwIDEpIGlzIGZhciBlYXNpZXIgdGhhbiBjdXJlIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1eGlsaWFyeSBMb2FkIEJhbGFuY2luZyBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc3RhbmRhcmQgYXV4aWxpYXJ5IGxvc3MgKEdTaGFyZCwgU3dpdGNoIFRyYW5zZm9ybWVyKSBhZGRzIGEgZGlmZmVyZW50aWFibGUgcGVuYWx0eSBmb3IgZXhwZXJ0IGltYmFsYW5jZSB0byB0aGUgdHJhaW5pbmcgb2JqZWN0aXZlLiBJdCBjb21wdXRlcyB0d28gcGVyLWV4cGVydCBxdWFudGl0aWVzOiBmX2ksIHRoZSBmcmFjdGlvbiBvZiB0b2tlbnMgZGlzcGF0Y2hlZCB0byBleHBlcnQgaSAoYmFzZWQgb24gdGhlIGRpc2NyZXRlIHRvcC1LIHNlbGVjdGlvbiksIGFuZCBQX2ksIHRoZSBtZWFuIHJvdXRpbmcgcHJvYmFiaWxpdHkgZm9yIGV4cGVydCBpICh0aGUgc29mdG1heCBvdXRwdXQsIHdoaWNoIGlzIGRpZmZlcmVudGlhYmxlKS4gVGhlIHByb2R1Y3QgZl9pICogUF9pIGlzIGhpZ2ggd2hlbiBleHBlcnQgaSBib3RoIHJlY2VpdmVzIG1hbnkgdG9rZW5zIGFuZCBoYXMgaGlnaCByb3V0aW5nIHByb2JhYmlsaXR5IOKAlCBib3RoIGNvbmRpdGlvbnMgdHJ1ZSBmb3IgdGhlIGRvbWluYW50IGV4cGVydC4gVGhlIGF1eGlsaWFyeSBsb3NzIGlzIE4gKiBzdW1faShmX2kgKiBQX2kpLCBzY2FsZWQgYnkgYSBjb2VmZmljaWVudCBhbHBoYSAodHlwaWNhbGx5IDFlLTIpLiBOb3RlIHRoYXQgZl9pIGlzIG5vdCBkaWZmZXJlbnRpYWJsZSAoaXQgaXMgYmFzZWQgb24gYXJnbWF4KSwgYnV0IFBfaSBpcyBkaWZmZXJlbnRpYWJsZSwgc28gZ3JhZGllbnRzIGZsb3cgYmFjayB0aHJvdWdoIFBfaSB0byB0aGUgcm91dGVyIHdlaWdodHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgZ3NoYXJkX2F1eGlsaWFyeV9sb3NzKHJvdXRlcl9sb2dpdHM6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgbl9leHBlcnRzOiBpbnQsIHRvcF9rOiBpbnQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgIGFscGhhOiBmbG9hdCA9IDFlLTIpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIkF1eGlsaWFyeSBsb2FkLWJhbGFuY2luZyBsb3NzIGZyb20gR1NoYXJkIGFuZCBTd2l0Y2ggVHJhbnNmb3JtZXIuXG4gICAgcm91dGVyX2xvZ2l0czogKGJhdGNoKnNlcSwgbl9leHBlcnRzKSDigJQgcmF3IHJvdXRlciBvdXRwdXRzIGJlZm9yZSBzb2Z0bWF4LlwiXCJcIlxuICAgIHByb2JzICAgPSBGLnNvZnRtYXgocm91dGVyX2xvZ2l0cywgZGltPS0xKSAgICAgICAgICAgICAgIyAoTiwgRSkgZGlmZmVyZW50aWFibGVcbiAgICAjIERpc3BhdGNoIGluZGljZXMgKG5vdCBkaWZmZXJlbnRpYWJsZSlcbiAgICBfLCBpZHggID0gdG9yY2gudG9wayhwcm9icy5kZXRhY2goKSwgdG9wX2ssIGRpbT0tMSkgICAgIyAoTiwgdG9wX2spXG4gICAgIyBmX2k6IGZyYWN0aW9uIG9mIHRva2VucyBkaXNwYXRjaGVkIHRvIGV4cGVydCBpIChub24tZGlmZmVyZW50aWFibGUpXG4gICAgb25laG90ICA9IEYub25lX2hvdChpZHhbOiwgMF0sIG5fZXhwZXJ0cykuZmxvYXQoKSAgICAgICMgdXNlIHRvcC0xIGZvciBmX2lcbiAgICBmX2kgICAgID0gb25laG90Lm1lYW4oZGltPTApICAgICAgICAgICAgICAgICAgICAgICAgICAgIyAoRSwpXG4gICAgIyBQX2k6IG1lYW4gcm91dGluZyBwcm9iYWJpbGl0eSAoZGlmZmVyZW50aWFibGUpXG4gICAgUF9pICAgICA9IHByb2JzLm1lYW4oZGltPTApICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKEUsKVxuICAgIGF1eCAgICAgPSBuX2V4cGVydHMgKiAoZl9pICogUF9pKS5zdW0oKVxuICAgIHJldHVybiBhbHBoYSAqIGF1eFxuXG4jIE9ic2VydmUgYXV4X2xvc3MgdW5kZXIgZGlmZmVyZW50IHJvdXRpbmcgZGlzdHJpYnV0aW9uc1xuZm9yIG5hbWUsIGxvZ2l0X2ZuIGluIFtcbiAgICAoXCJ1bmlmb3JtXCIsICBsYW1iZGE6IHRvcmNoLnplcm9zKDY0LCA4KSksXG4gICAgKFwiYmFsYW5jZWRcIiwgbGFtYmRhOiB0b3JjaC5yYW5kbig2NCwgOCkgKiAwLjUpLFxuICAgIChcImNvbGxhcHNlXCIsIGxhbWJkYTogdG9yY2guY2F0KFt0b3JjaC5mdWxsKCg2NCwxKSw1LjApLCB0b3JjaC56ZXJvcyg2NCw3KV0sIC0xKSksXG5dOlxuICAgIEwgPSBnc2hhcmRfYXV4aWxpYXJ5X2xvc3MobG9naXRfZm4oKSwgbl9leHBlcnRzPTgsIHRvcF9rPTIsIGFscGhhPTEuMClcbiAgICBwcmludChmXCJ7bmFtZTpcdTAwM2UxMH06IHJhd19hdXggPSB7TC5pdGVtKCk6LjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4cGVydCBDaG9pY2UgUm91dGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXhwZXJ0IGNob2ljZSByb3V0aW5nIChaaG91IGV0IGFsLiwgMjAyMikgaW52ZXJ0cyB0aGUgcm91dGluZyBkaXJlY3Rpb246IGluc3RlYWQgb2YgZWFjaCB0b2tlbiBzZWxlY3RpbmcgaXRzIHRvcC1LIGV4cGVydHMsIGVhY2ggZXhwZXJ0IHNlbGVjdHMgaXRzIHRvcC1DIHRva2VucyBmcm9tIHRoZSBiYXRjaC4gV2l0aCBhIGNhcGFjaXR5IEMgPSAoYmF0Y2hfc2l6ZSAqIHNlcV9sZW4gKiBLKSAvIE4gdG9rZW5zIHBlciBleHBlcnQsIGV2ZXJ5IGV4cGVydCBwcm9jZXNzZXMgZXhhY3RseSB0aGUgc2FtZSBudW1iZXIgb2YgdG9rZW5zIOKAlCBsb2FkIGJhbGFuY2UgaXMgZ3VhcmFudGVlZCBieSBjb25zdHJ1Y3Rpb24uIFRoZSBzZWxlY3Rpb24gaXMgZG9uZSBwZXIgZXhwZXJ0IGluZGVwZW5kZW50bHk6IGV4cGVydCBpIHNjb3JlcyBhbGwgYmF0Y2ggdG9rZW5zIHdpdGggaXRzIG93biByb3V0aW5nIGhlYWQgYW5kIHRha2VzIHRoZSB0b3AtQy4gQSB0b2tlbiBtYXkgYmUgc2VsZWN0ZWQgYnkgbXVsdGlwbGUgZXhwZXJ0cyAobGlrZSB0b3AtSykgb3IgYnkgbm9uZSAodW5saWtlIHRva2VuLWNob2ljZSByb3V0aW5nLCB3aGVyZSBldmVyeSB0b2tlbiBpcyBndWFyYW50ZWVkIHRvIGJlIHByb2Nlc3NlZCkuIFRoZSBtZXRob2QgZWxpbWluYXRlcyB0aGUgbmVlZCBmb3IgYXV4aWxpYXJ5IGxvc3MgZW50aXJlbHkgYW5kIHJlbW92ZXMgdGhlIGNhcGFjaXR5LWZhY3Rvci1hbmQtZHJvcCBwcm9ibGVtLCBidXQgcmVxdWlyZXMgYSBkaWZmZXJlbnQgaW1wbGVtZW50YXRpb24gb2YgdGhlIGRpc3BhdGNoIG1lY2hhbmlzbS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBleHBlcnRfY2hvaWNlX3JvdXRpbmcoeDogdG9yY2guVGVuc29yLCBXX3JvdXRlcjogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICBuX2V4cGVydHM6IGludCwgY2FwYWNpdHlfZmFjdG9yOiBmbG9hdCA9IDEuMCkgLVx1MDAzZSB0dXBsZTpcbiAgICBcIlwiXCJFeHBlcnQgY2hvaWNlOiBlYWNoIGV4cGVydCBzZWxlY3RzIHRvcC1DIHRva2Vucy5cbiAgICB4OiAoTiwgRCkgIFdfcm91dGVyOiAoRCwgRSlcbiAgICBSZXR1cm5zOiAoZXhwZXJ0X291dHB1dHMgcGxhY2Vob2xkZXIsIHRva2VuX2Fzc2lnbm1lbnRzIGRpY3QpXCJcIlwiXG4gICAgTiwgRCA9IHguc2hhcGVcbiAgICAjIENhcGFjaXR5OiBlYWNoIGV4cGVydCBwcm9jZXNzZXMgY2FwYWNpdHlfZmFjdG9yICogTiAvIG5fZXhwZXJ0cyB0b2tlbnNcbiAgICBDID0gbWF4KDEsIGludChjYXBhY2l0eV9mYWN0b3IgKiBOIC8gbl9leHBlcnRzKSlcbiAgICBzY29yZXMgPSB4IEAgV19yb3V0ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKE4sIEUpXG4gICAgc2NvcmVzID0gRi5zb2Z0bWF4KHNjb3JlcywgZGltPTApICAgICAgICAgICAgICAgICAgICAgICAjIHNvZnRtYXggb3ZlciB0b2tlbnNcbiAgICAjIEVhY2ggZXhwZXJ0IHNlbGVjdHMgaXRzIHRvcC1DIHRva2Vuc1xuICAgIHRvcF9zY29yZXMsIHRvcF9pbmRpY2VzID0gdG9yY2gudG9wayhzY29yZXMsIEMsIGRpbT0wKSAjIChDLCBFKVxuICAgIGFzc2lnbm1lbnRzID0ge31cbiAgICBmb3IgZSBpbiByYW5nZShuX2V4cGVydHMpOlxuICAgICAgICB0b2tlbl9pZHMgPSB0b3BfaW5kaWNlc1s6LCBlXSAgICAgICAgICAgICAgICAgICAgICAgIyAoQywpIHRva2VuIGluZGljZXNcbiAgICAgICAgd2VpZ2h0cyAgID0gdG9wX3Njb3Jlc1s6LCBlXSAgICAgICAgICAgICAgICAgICAgICAgICMgKEMsKSByb3V0aW5nIHdlaWdodHNcbiAgICAgICAgYXNzaWdubWVudHNbZV0gPSAodG9rZW5faWRzLCB3ZWlnaHRzKVxuICAgICMgRXZlcnkgZXhwZXJ0IHByb2Nlc3NlcyBleGFjdGx5IEMgdG9rZW5zIOKAlCBsb2FkIGJhbGFuY2UgZ3VhcmFudGVlZFxuICAgIHJldHVybiBhc3NpZ25tZW50cywgQ1xuXG5OLCBELCBFID0gMTI4LCAyNTYsIDhcbmFzc2lnbiwgY2FwID0gZXhwZXJ0X2Nob2ljZV9yb3V0aW5nKHRvcmNoLnJhbmRuKE4sIEQpLCB0b3JjaC5yYW5kbihELCBFKSwgRSlcbmZvciBlLCAoaWRzLCB3dHMpIGluIGFzc2lnbi5pdGVtcygpOlxuICAgIHByaW50KGZcIkV4cGVydCB7ZX06IHtsZW4oaWRzKX0gdG9rZW5zLCBtZWFuX3dlaWdodD17d3RzLm1lYW4oKTouM2Z9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiWi1Mb3NzIGZvciBSb3V0ZXIgU3RhYmlsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJaLWxvc3MgKFpvcGggZXQgYWwuLCAyMDIyLCBmcm9tIHRoZSBTVC1Nb0UgcGFwZXIpIGFkZHJlc3NlcyBhIGRpZmZlcmVudCBpbnN0YWJpbGl0eTogcm91dGVyIGxvZ2l0IGV4cGxvc2lvbi4gRHVyaW5nIHRyYWluaW5nLCB0aGUgcm91dGVyIGxvZ2l0cyBjYW4gZ3JvdyB0byB2ZXJ5IGxhcmdlIG1hZ25pdHVkZXMgKMKxMzAgb3IgbW9yZSksIGNhdXNpbmcgdGhlIHNvZnRtYXggdG8gc2F0dXJhdGUg4oCUIG9uZSBleHBlcnQgZ2V0cyBwcm9iYWJpbGl0eSB+MS4wIGFuZCBhbGwgb3RoZXJzIGdldCB+MC4wLiBUaGlzIHNhdHVyYXRpb24gbWFrZXMgdGhlIGF1eGlsaWFyeSBsb3NzIGFsbW9zdCB6ZXJvIChzaW5jZSB0aGUgc29mdG1heCBncmFkaWVudCB2YW5pc2hlcyBhdCBzYXR1cmF0aW9uKSwgcHJldmVudHMgdGhlIGF1eGlsaWFyeSBsb3NzIGZyb20gZG9pbmcgaXRzIGpvYiwgYW5kIGluIHByYWN0aWNlIGxlYWRzIHRvIHRyYWluaW5nIGluc3RhYmlsaXR5IG9yIE5hTnMgYXQgbGFyZ2Ugc2NhbGUuIFotbG9zcyBwZW5hbGlzZXMgbGFyZ2Ugcm91dGVyIGxvZ2l0cyBkaXJlY3RseTogTF96ID0gKDEvTikgKiBzdW1faSBsb2coc3VtX2ogZXhwKGhfaWopKV4yLCB3aGVyZSBoX2lqIGFyZSB0aGUgbG9naXRzIGZvciB0b2tlbiBpLiBUaGlzIGlzIHRoZSBzcXVhcmVkIGxvZy1zdW0tZXhwIG9mIHRoZSBsb2dpdHMg4oCUIHplcm8gd2hlbiBsb2dpdHMgYXJlIG5lYXIgemVybywgbGFyZ2Ugd2hlbiBsb2dpdHMgYXJlIGxhcmdlIGluIG1hZ25pdHVkZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiB6X2xvc3Mocm91dGVyX2xvZ2l0czogdG9yY2guVGVuc29yLCBjb2VmZjogZmxvYXQgPSAxZS0zKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJaLWxvc3M6IHBlbmFsaXNlIGxhcmdlIHJvdXRlciBsb2dpdHMgdG8gcHJldmVudCBzb2Z0bWF4IHNhdHVyYXRpb24uXG4gICAgcm91dGVyX2xvZ2l0czogKGJhdGNoKnNlcSwgbl9leHBlcnRzKSByYXcgbG9naXRzIChiZWZvcmUgc29mdG1heCkuXG4gICAgUmV0dXJucyBhIHNjYWxhciBsb3NzIHRvIGFkZCB0byB0aGUgdG90YWwgdHJhaW5pbmcgbG9zcy5cIlwiXCJcbiAgICAjIGxvZyhzdW0oZXhwKGgpKSkgPSBsb2dzdW1leHAgYWNyb3NzIGV4cGVydHMgZm9yIGVhY2ggdG9rZW5cbiAgICBsb2dfeiA9IHRvcmNoLmxvZ3N1bWV4cChyb3V0ZXJfbG9naXRzLCBkaW09LTEpICAgICAgICAgICMgKE4sKVxuICAgIHJldHVybiBjb2VmZiAqIChsb2dfeiAqKiAyKS5tZWFuKClcblxuZGVmIHJvdXRlcl9zdGFiaWxpdHlfY2hlY2sobG9naXRzOiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJDaGVjayByb3V0ZXIgbG9naXQgaGVhbHRoOiBsYXJnZSBtYWduaXR1ZGVzIGluZGljYXRlIGltcGVuZGluZyBjb2xsYXBzZS5cIlwiXCJcbiAgICBhYnNfbWF4ICA9IGxvZ2l0cy5hYnMoKS5tYXgoKS5pdGVtKClcbiAgICBwcm9icyAgICA9IEYuc29mdG1heChsb2dpdHMsIGRpbT0tMSlcbiAgICBlbnRyb3B5ICA9IC0ocHJvYnMgKiAocHJvYnMgKyAxZS05KS5sb2coKSkuc3VtKC0xKS5tZWFuKCkuaXRlbSgpXG4gICAgbWF4X3Byb2IgPSBwcm9icy5tYXgoLTEpLnZhbHVlcy5tZWFuKCkuaXRlbSgpXG4gICAgcmV0dXJuIHtcImFic19tYXhfbG9naXRcIjogYWJzX21heCwgXCJtZWFuX2VudHJvcHlcIjogZW50cm9weSxcbiAgICAgICAgICAgIFwibWVhbl9tYXhfcHJvYlwiOiBtYXhfcHJvYiwgXCJ6X2xvc3NcIjogel9sb3NzKGxvZ2l0cywgMS4wKS5pdGVtKCl9XG5cbmZvciBuYW1lLCBsb2dpdHMgaW4gW1xuICAgIChcImhlYWx0aHlcIiwgIHRvcmNoLnJhbmRuKDMyLCA4KSAqIDEuMCksXG4gICAgKFwibW9kZXJhdGVcIiwgdG9yY2gucmFuZG4oMzIsIDgpICogNS4wKSxcbiAgICAoXCJleHBsb2RlZFwiLCB0b3JjaC5yYW5kbigzMiwgOCkgKiAyMC4wKSxcbl06XG4gICAgcyA9IHJvdXRlcl9zdGFiaWxpdHlfY2hlY2sobG9naXRzKVxuICAgIHByaW50KGZcIntuYW1lOlx1MDAzZTEwfTogbWF4X2xvZ2l0PXtzW1x1MDAyN2Fic19tYXhfbG9naXRcdTAwMjddOi4xZn0gIGVudHJvcHk9e3NbXHUwMDI3bWVhbl9lbnRyb3B5XHUwMDI3XTouM2Z9ICB6X2xvc3M9e3NbXHUwMDI3el9sb3NzXHUwMDI3XTouMmZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2FwYWNpdHkgRmFjdG9yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDYXBhY2l0eSBmYWN0b3IgaXMgYSBoYXJkd2FyZS1sZXZlbCBsb2FkLWJhbGFuY2luZyBtZWNoYW5pc20gdXNlZCBpbiBib3RoIEdTaGFyZCBhbmQgU3dpdGNoIFRyYW5zZm9ybWVyLiBFYWNoIGV4cGVydCBpcyBhbGxvY2F0ZWQgYSBmaXhlZCBidWZmZXIgb2Ygc2l6ZSBDID0gY2FwYWNpdHlfZmFjdG9yICogKGJhdGNoX3Rva2VucyAvIG5fZXhwZXJ0cykgdG9rZW5zLiBJZiBtb3JlIHRoYW4gQyB0b2tlbnMgYXJlIHJvdXRlZCB0byBhbiBleHBlcnQsIHRoZSBvdmVyZmxvdyB0b2tlbnMgYXJlIGRyb3BwZWQgKHRoZWlyIHJlcHJlc2VudGF0aW9uIHBhc3NlcyB0aHJvdWdoIHVuY2hhbmdlZCwgb3IgaXMgemVyby1wYWRkZWQpLiBUaGUgY2FwYWNpdHkgZmFjdG9yIGlzIHR5cGljYWxseSBzZXQgdG8gMS4w4oCTMS4yNTogMS4wIG1lYW5zIHBlcmZlY3QgYmFsYW5jZSB3aXRoIHplcm8gc2xhY2ssIGNhdXNpbmcgZnJlcXVlbnQgZHJvcHBpbmcgdW5sZXNzIGxvYWQgaXMgcGVyZmVjdGx5IGJhbGFuY2VkOyAxLjI1IHByb3ZpZGVzIGEgMjUlIGJ1ZmZlciB0aGF0IGFic29yYnMgbWlsZCBpbWJhbGFuY2Ugd2l0aG91dCBkcm9wcGluZy4gRHVyaW5nIHRyYWluaW5nLCBkcm9wcGVkIHRva2VucyBzdGlsbCBjb250cmlidXRlIHRvIHRoZSBMTSBsb3NzICh0aGVpciB0YXJnZXQgbGFiZWxzIGFyZSB1bmNoYW5nZWQpIGJ1dCBkbyBub3QgcGFzcyB0aHJvdWdoIHRoZSBleHBlcnQsIHdlYWtlbmluZyB0aGVpciBncmFkaWVudC4gVGhlIGNhcGFjaXR5IGZhY3RvciBpcyB1c3VhbGx5IHJlZHVjZWQgb3ZlciB0cmFpbmluZyBhcyB0aGUgcm91dGVyIGxlYXJucyB0byBiYWxhbmNlIGl0c2VsZi4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiTG9hZCBiYWxhbmNlIHF1YWxpdHkiLCJBY2N1cmFjeSBpbXBhY3QiLCJFeHRyYSBjb21wdXRlIiwiTm90ZXMiXSwicm93cyI6W1siTm8gYmFsYW5jaW5nIiwiUG9vciAoY29sbGFwc2UpIiwiU2V2ZXJlICgtMyB0byAtNSBQUEwpIiwiTm9uZSIsIkZhaWxzIHdpdGhvdXQgcmVndWxhcmlzYXRpb24iXSxbIkF1eGlsaWFyeSBsb3NzIChhbHBoYT0xZS0yKSIsIkdvb2QiLCJNaW5pbWFsICh+MC4xIFBQTCkiLCJOZWdsaWdpYmxlIiwiU3RhbmRhcmQgY2hvaWNlOyBTd2l0Y2gvR1NoYXJkIl0sWyJFeHBlcnQgY2hvaWNlIHJvdXRpbmciLCJQZXJmZWN0IChndWFyYW50ZWVkKSIsIk5vbmUgdG8gc2xpZ2h0IGdhaW4iLCJNb2RlcmF0ZSAoc29mdG1heCBvdmVyIHRva2VucykiLCJObyBhdXggbG9zcyBuZWVkZWQ7IGRpZmZlcmVudCBkaXNwYXRjaCBsb2dpYyJdLFsiWi1sb3NzIChjb2VmZj0xZS0zKSIsIkdvb2QgKHByZXZlbnRzIGV4cGxvc2lvbikiLCJNaW5pbWFsIiwiTmVnbGlnaWJsZSIsIlVzZWQgYWxvbmdzaWRlIGF1eCBsb3NzIGluIFNULU1vRSJdLFsiVG9rZW4gZHJvcHBpbmcgKGNhcD0xLjApIiwiR29vZCAoYm91bmRlZCkiLCJTbGlnaHQgKC0wLjIgdG8gLTAuNSBQUEwpIiwiTmVnbGlnaWJsZSIsIkRyb3BzIG92ZXJmbG93IHRva2VuczsgaGFyZHdhcmUgZWZmaWNpZW50Il0sWyJCdWZmZXIgdG9rZW5zIiwiTW9kZXJhdGUiLCJOZWdsaWdpYmxlIiwiU21hbGwgbWVtb3J5IiwiT3ZlcmZsb3cgdG9rZW5zIGhlbGQgaW4gc2hhcmVkIGJ1ZmZlciJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9uaXRvcmluZyBFeHBlcnQgVXRpbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vbml0b3JpbmcgZXhwZXJ0IHV0aWxpc2F0aW9uIHRocm91Z2hvdXQgdHJhaW5pbmcgaXMgZXNzZW50aWFsIGJlY2F1c2UgdGhlIExNIGxvc3MgaXMgbm90IGEgcmVsaWFibGUgaW5kaWNhdG9yIG9mIGxvYWQgY29sbGFwc2Ug4oCUIGEgbW9kZWwgY2FuIHByb2R1Y2UgZ29vZCBwZXJwbGV4aXR5IHdpdGggb25seSAy4oCTMyBhY3RpdmUgZXhwZXJ0cy4gVGhlIGtleSBtZXRyaWNzIGFyZTogbm9ybWFsaXNlZCBlbnRyb3B5IG9mIHRoZSBleHBlcnQgdXRpbGlzYXRpb24gZGlzdHJpYnV0aW9uICgxLjAgPSBwZXJmZWN0bHkgYmFsYW5jZWQsIDAuMCA9IGZ1bGwgY29sbGFwc2UpOyBjb2VmZmljaWVudCBvZiB2YXJpYXRpb24gKENWKSBvZiBwZXItZXhwZXJ0IHRva2VuIGNvdW50cyAodGFyZ2V0IFx1MDAzYyAwLjMpOyBhbmQgZnJhY3Rpb24gb2YgdG9rZW5zIGRyb3BwZWQgZHVlIHRvIGNhcGFjaXR5IG92ZXJmbG93ICh0YXJnZXQgXHUwMDNjIDUlKS4gVGhlc2Ugc2hvdWxkIGJlIGxvZ2dlZCBldmVyeSAxMDDigJM1MDAgdHJhaW5pbmcgc3RlcHMuIElmIG5vcm1hbGlzZWQgZW50cm9weSBkcm9wcyBiZWxvdyAwLjcgb3IgQ1YgZXhjZWVkcyAwLjUsIGluY3JlYXNlIGFscGhhIG9yIGluc3BlY3QgdGhlIHJvdXRlciBsb2dpdHMgZm9yIHNhdHVyYXRpb24uIEEgdXNlZnVsIGRpYWdub3N0aWMgaXMgdG8gcGxvdCB0aGUgcGVyLWV4cGVydCB0b2tlbiBmcmFjdGlvbiBhcyBhIHN0YWNrZWQgYmFyIGNoYXJ0IG92ZXIgdHJhaW5pbmcg4oCUIHZpc3VhbCBjb2xsYXBzZSBpcyBpbW1lZGlhdGVseSBvYnZpb3VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVxdWVcblxuY2xhc3MgRXhwZXJ0TG9hZE1vbml0b3I6XG4gICAgXCJcIlwiTW9uaXRvciBwZXItZXhwZXJ0IHRva2VuIGxvYWQgb3ZlciBhIHNsaWRpbmcgd2luZG93IG9mIGJhdGNoZXMuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fZXhwZXJ0czogaW50LCB3aW5kb3c6IGludCA9IDUwMCk6XG4gICAgICAgIHNlbGYubl9leHBlcnRzID0gbl9leHBlcnRzXG4gICAgICAgIHNlbGYuaGlzdG9yeSAgID0gZGVxdWUobWF4bGVuPXdpbmRvdylcblxuICAgIGRlZiByZWNvcmQoc2VsZiwgZXhwZXJ0X2luZGljZXM6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSBkaWN0OlxuICAgICAgICBcIlwiXCJleHBlcnRfaW5kaWNlczogKE4sIHRvcF9rKS4gUmVjb3JkcyBsb2FkIGFuZCByZXR1cm5zIGN1cnJlbnQgc3RhdHMuXCJcIlwiXG4gICAgICAgIGNvdW50cyA9IHRvcmNoLnplcm9zKHNlbGYubl9leHBlcnRzKVxuICAgICAgICBmb3IgZSBpbiByYW5nZShzZWxmLm5fZXhwZXJ0cyk6XG4gICAgICAgICAgICBjb3VudHNbZV0gPSAoZXhwZXJ0X2luZGljZXMgPT0gZSkuc3VtKCkuZmxvYXQoKVxuICAgICAgICBsb2FkID0gY291bnRzIC8gY291bnRzLnN1bSgpXG4gICAgICAgIHNlbGYuaGlzdG9yeS5hcHBlbmQobG9hZC5udW1weSgpKVxuICAgICAgICAjIENvbXB1dGUgc3RhdHMgb3ZlciBoaXN0b3J5IHdpbmRvd1xuICAgICAgICBoaXN0ICA9IG5wLnN0YWNrKHNlbGYuaGlzdG9yeSkgICAgICAgICAgICAgICAgICAgICAjIChXLCBFKVxuICAgICAgICBtZWFuICA9IGhpc3QubWVhbihheGlzPTApXG4gICAgICAgIGN2ICAgID0gbWVhbi5zdGQoKSAvIChtZWFuLm1lYW4oKSArIDFlLTkpXG4gICAgICAgIGVudCAgID0gLShtZWFuICogbnAubG9nKG1lYW4gKyAxZS05KSkuc3VtKClcbiAgICAgICAgbWF4X2UgPSBucC5sb2coc2VsZi5uX2V4cGVydHMpXG4gICAgICAgIHN0YXRzID0ge1wiY3ZcIjogY3YsIFwibm9ybV9lbnRyb3B5XCI6IGVudCAvIG1heF9lLFxuICAgICAgICAgICAgICAgICBcIm1heF9sb2FkXCI6IG1lYW4ubWF4KCksIFwibWluX2xvYWRcIjogbWVhbi5taW4oKX1cbiAgICAgICAgaWYgY3YgXHUwMDNlIDAuNTpcbiAgICAgICAgICAgIHByaW50KGZcIiAgQUxFUlQ6IENWPXtjdjouM2Z9IFx1MDAzZSAwLjUg4oCUIHBvc3NpYmxlIGV4cGVydCBjb2xsYXBzZVwiKVxuICAgICAgICByZXR1cm4gc3RhdHNcblxubW9uaXRvciA9IEV4cGVydExvYWRNb25pdG9yKG5fZXhwZXJ0cz04LCB3aW5kb3c9MTAwKVxuZm9yIHN0ZXAgaW4gcmFuZ2UoNTApOlxuICAgIGlkeCA9IHRvcmNoLnJhbmRpbnQoMCwgOCwgKDY0LCAyKSlcbiAgICBpZiBzdGVwICUgMTAgPT0gMDpcbiAgICAgICAgcyA9IG1vbml0b3IucmVjb3JkKGlkeClcbiAgICAgICAgcHJpbnQoZlwic3RlcCB7c3RlcDpcdTAwM2UzfTogbm9ybV9lbnRyb3B5PXtzW1x1MDAyN25vcm1fZW50cm9weVx1MDAyN106LjNmfSAgY3Y9e3NbXHUwMDI3Y3ZcdTAwMjddOi4zZn1cIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkV4cGVydCBDb2xsYXBzZSBpcyBOb3QgU2VsZi1Db3JyZWN0aW5nIiwiY29udGVudCI6IkV4cGVydCBjb2xsYXBzZSBpcyBhIHRyYWluaW5nIGZhaWx1cmUgbW9kZSwgbm90IGEgY29udmVyZ2VuY2UgaXNzdWUg4oCUIG9uY2UgYSBmZXcgZXhwZXJ0cyBkb21pbmF0ZSwgZ3JhZGllbnQgc2lnbmFsIHN0b3BzIGZsb3dpbmcgdG8gb3RoZXJzLCBtYWtpbmcgcmVjb3ZlcnkgZGlmZmljdWx0IHdpdGhvdXQgc3Ryb25nIGF1eGlsaWFyeSBsb3NzZXMgZnJvbSB0aGUgc3RhcnQuIE1vbml0b3Igbm9ybWFsaXNlZCBlbnRyb3B5IGV2ZXJ5IDEwMCBzdGVwczsgaWYgaXQgZHJvcHMgYmVsb3cgMC43LCBpbmNyZWFzZSBhbHBoYSBpbW1lZGlhdGVseS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMb2FkIGJhbGFuY2luZyBpcyBhIGZpcnN0LWNsYXNzIGNvbmNlcm4gaW4gTW9FIHRyYWluaW5nLCBub3QgYW4gYWZ0ZXJ0aG91Z2h0LiBUaGUgYXV4aWxpYXJ5IGxvc3MgKGFscGhhIH4gMWUtMikgaXMgdGhlIHN0YW5kYXJkIHByZXZlbnRpb24gbWVjaGFuaXNtIGFuZCBtdXN0IGJlIGFwcGxpZWQgZnJvbSB0aGUgZmlyc3QgdHJhaW5pbmcgc3RlcC4gWi1sb3NzIChjb2VmZiB+IDFlLTMpIHNob3VsZCBiZSBhZGRlZCBhbG9uZ3NpZGUgdGhlIGF1eGlsaWFyeSBsb3NzIGF0IGxhcmdlIHNjYWxlIHRvIHByZXZlbnQgcm91dGVyIGxvZ2l0IGV4cGxvc2lvbi4gRXhwZXJ0IGNob2ljZSByb3V0aW5nIGNvbXBsZXRlbHkgZWxpbWluYXRlcyB0aGUgbG9hZC1pbWJhbGFuY2UgcHJvYmxlbSBhdCB0aGUgY29zdCBvZiBhIGRpZmZlcmVudCBkaXNwYXRjaCBpbXBsZW1lbnRhdGlvbi4gQ2FwYWNpdHkgZmFjdG9yIHdpdGggdG9rZW4gZHJvcHBpbmcgaXMgYSBoYXJkd2FyZS1lZmZpY2llbmN5IHRvb2wsIG5vdCBhIGJhbGFuY2luZyBzb2x1dGlvbiDigJQgaXQgY2FwcyBkYW1hZ2UgZnJvbSBpbWJhbGFuY2UgYnV0IGRvZXMgbm90IHByZXZlbnQgaXQuIE1vbml0b3Igbm9ybWFsaXNlZCBlbnRyb3B5IGFuZCBDViB0aHJvdWdob3V0IHRyYWluaW5nLCBhbmQgYWxlcnQgd2hlbiBlbnRyb3B5IGRyb3BzIGJlbG93IDAuNy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFwcGx5IGF1eGlsaWFyeSBsb2FkLWJhbGFuY2luZyBsb3NzIGZyb20gc3RlcCAxIHdpdGggYWxwaGEgfiAxZS0yIChTd2l0Y2gvR1NoYXJkIGZvcm11bGEpIiwiQWRkIFotbG9zcyAoY29lZmYgfiAxZS0zKSBhdCBsYXJnZSBzY2FsZSB0byBwcmV2ZW50IHJvdXRlciBsb2dpdCBzYXR1cmF0aW9uIiwiRXhwZXJ0IGNob2ljZSByb3V0aW5nIGd1YXJhbnRlZXMgbG9hZCBiYWxhbmNlIGJ5IGNvbnN0cnVjdGlvbjsgbm8gYXV4IGxvc3MgbmVlZGVkIiwiQ2FwYWNpdHkgZmFjdG9yIDEuMOKAkzEuMjUgY2FwcyB0b2tlbnMgcGVyIGV4cGVydDsgb3ZlcmZsb3cgdG9rZW5zIGFyZSBkcm9wcGVkIiwiTW9uaXRvciBub3JtYWxpc2VkIGVudHJvcHkgKHRhcmdldCBcdTAwM2UgMC44KSBhbmQgQ1YgKHRhcmdldCBcdTAwM2MgMC4zKSBldmVyeSAxMDAgc3RlcHMiLCJSZWNvdmVyeSBmcm9tIGNvbGxhcHNlIGlzIGhhcmQg4oCUIHByZXZlbnRpb24gd2l0aCBzdHJvbmcgYWxwaGEgZnJvbSBzdGVwIDEgaXMgZXNzZW50aWFsIl19XQ=="
---
# MoE Load Balancing

In a Mixture-of-Experts model, the router is a small learned network that maps each token to a probability distribution over experts. Left unconstrained, the router quickly collapses: a few experts consistently win the softmax competition, receive the most tokens, accumulate the most gradient signal, and become even better — while the remaining experts starve. This failure mode, called expert collapse, is one of the central training challenges in MoE architectures. Addressing it requires explicit regularisation in the loss function, alternative routing strategies that remove the competitive dynamic, and careful monitoring throughout training. This note covers the full toolkit: auxiliary loss, expert choice routing, Z-loss, and capacity factors.

## Overview

Load balancing in MoE training is the problem of ensuring each expert processes approximately 1/N of all tokens throughout training, while still allowing the router to develop meaningful specialisation. Perfect balance (each expert sees exactly 1/N tokens) would require a combinatorial assignment that ignores token-expert affinity; pure affinity routing (each token always goes to its most preferred expert) collapses. Good load balancing methods find a middle ground: they allow the router to prefer certain experts for certain tokens while adding soft regularisation that discourages extreme imbalance. The main approaches are: (1) auxiliary loss on the routing distribution, (2) expert choice routing where experts select tokens rather than tokens selecting experts, (3) Z-loss to prevent router logit explosion, and (4) capacity factors with token dropping.

## Expert Collapse Problem

Expert collapse occurs because the softmax router is a winner-takes-all function in expectation. If expert 0 happens to be initialised with slightly larger weights, it receives slightly higher logits for many tokens, gets routed more tokens, receives more gradient, improves faster, and wins an ever-larger share of tokens. This creates a rich-get-richer dynamic that is reinforced at every gradient step. Once an expert dominates — receiving more than 50% of tokens — the other experts receive so little gradient that their weights barely change, effectively freezing them. Recovery from severe collapse is difficult because the dominant expert has already converged to a local optimum, and the auxiliary loss must push strongly enough against it to overcome this.

- Router logits for the dominant expert grow monotonically while others decay
- Auxiliary loss becomes ineffective once collapse is severe (gradient flow to other experts is near zero)
- Training loss may still decrease even during collapse — the LM objective does not detect it
- Expert utilisation entropy drops from log(N) to near 0 over hundreds of steps
- Recovery requires either very strong alpha or architectural changes to the router
- Prevention (strong alpha from step 1) is far easier than cure

## Auxiliary Load Balancing Loss

The standard auxiliary loss (GShard, Switch Transformer) adds a differentiable penalty for expert imbalance to the training objective. It computes two per-expert quantities: f_i, the fraction of tokens dispatched to expert i (based on the discrete top-K selection), and P_i, the mean routing probability for expert i (the softmax output, which is differentiable). The product f_i * P_i is high when expert i both receives many tokens and has high routing probability — both conditions true for the dominant expert. The auxiliary loss is N * sum_i(f_i * P_i), scaled by a coefficient alpha (typically 1e-2). Note that f_i is not differentiable (it is based on argmax), but P_i is differentiable, so gradients flow back through P_i to the router weights.

```python
import torch
import torch.nn.functional as F

def gshard_auxiliary_loss(router_logits: torch.Tensor,
                          n_experts: int, top_k: int,
                          alpha: float = 1e-2) -> torch.Tensor:
    """Auxiliary load-balancing loss from GShard and Switch Transformer.
    router_logits: (batch*seq, n_experts) — raw router outputs before softmax."""
    probs   = F.softmax(router_logits, dim=-1)              # (N, E) differentiable
    # Dispatch indices (not differentiable)
    _, idx  = torch.topk(probs.detach(), top_k, dim=-1)    # (N, top_k)
    # f_i: fraction of tokens dispatched to expert i (non-differentiable)
    onehot  = F.one_hot(idx[:, 0], n_experts).float()      # use top-1 for f_i
    f_i     = onehot.mean(dim=0)                           # (E,)
    # P_i: mean routing probability (differentiable)
    P_i     = probs.mean(dim=0)                            # (E,)
    aux     = n_experts * (f_i * P_i).sum()
    return alpha * aux

# Observe aux_loss under different routing distributions
for name, logit_fn in [
    ("uniform",  lambda: torch.zeros(64, 8)),
    ("balanced", lambda: torch.randn(64, 8) * 0.5),
    ("collapse", lambda: torch.cat([torch.full((64,1),5.0), torch.zeros(64,7)], -1)),
]:
    L = gshard_auxiliary_loss(logit_fn(), n_experts=8, top_k=2, alpha=1.0)
    print(f"{name:>10}: raw_aux = {L.item():.4f}")
```

## Expert Choice Routing

Expert choice routing (Zhou et al., 2022) inverts the routing direction: instead of each token selecting its top-K experts, each expert selects its top-C tokens from the batch. With a capacity C = (batch_size * seq_len * K) / N tokens per expert, every expert processes exactly the same number of tokens — load balance is guaranteed by construction. The selection is done per expert independently: expert i scores all batch tokens with its own routing head and takes the top-C. A token may be selected by multiple experts (like top-K) or by none (unlike token-choice routing, where every token is guaranteed to be processed). The method eliminates the need for auxiliary loss entirely and removes the capacity-factor-and-drop problem, but requires a different implementation of the dispatch mechanism.

```python
import torch
import torch.nn.functional as F

def expert_choice_routing(x: torch.Tensor, W_router: torch.Tensor,
                          n_experts: int, capacity_factor: float = 1.0) -> tuple:
    """Expert choice: each expert selects top-C tokens.
    x: (N, D)  W_router: (D, E)
    Returns: (expert_outputs placeholder, token_assignments dict)"""
    N, D = x.shape
    # Capacity: each expert processes capacity_factor * N / n_experts tokens
    C = max(1, int(capacity_factor * N / n_experts))
    scores = x @ W_router                                   # (N, E)
    scores = F.softmax(scores, dim=0)                       # softmax over tokens
    # Each expert selects its top-C tokens
    top_scores, top_indices = torch.topk(scores, C, dim=0) # (C, E)
    assignments = {}
    for e in range(n_experts):
        token_ids = top_indices[:, e]                       # (C,) token indices
        weights   = top_scores[:, e]                        # (C,) routing weights
        assignments[e] = (token_ids, weights)
    # Every expert processes exactly C tokens — load balance guaranteed
    return assignments, C

N, D, E = 128, 256, 8
assign, cap = expert_choice_routing(torch.randn(N, D), torch.randn(D, E), E)
for e, (ids, wts) in assign.items():
    print(f"Expert {e}: {len(ids)} tokens, mean_weight={wts.mean():.3f}")
```

## Z-Loss for Router Stability

Z-loss (Zoph et al., 2022, from the ST-MoE paper) addresses a different instability: router logit explosion. During training, the router logits can grow to very large magnitudes (±30 or more), causing the softmax to saturate — one expert gets probability ~1.0 and all others get ~0.0. This saturation makes the auxiliary loss almost zero (since the softmax gradient vanishes at saturation), prevents the auxiliary loss from doing its job, and in practice leads to training instability or NaNs at large scale. Z-loss penalises large router logits directly: L_z = (1/N) * sum_i log(sum_j exp(h_ij))^2, where h_ij are the logits for token i. This is the squared log-sum-exp of the logits — zero when logits are near zero, large when logits are large in magnitude.

```python
import torch
import torch.nn.functional as F

def z_loss(router_logits: torch.Tensor, coeff: float = 1e-3) -> torch.Tensor:
    """Z-loss: penalise large router logits to prevent softmax saturation.
    router_logits: (batch*seq, n_experts) raw logits (before softmax).
    Returns a scalar loss to add to the total training loss."""
    # log(sum(exp(h))) = logsumexp across experts for each token
    log_z = torch.logsumexp(router_logits, dim=-1)          # (N,)
    return coeff * (log_z ** 2).mean()

def router_stability_check(logits: torch.Tensor) -> dict:
    """Check router logit health: large magnitudes indicate impending collapse."""
    abs_max  = logits.abs().max().item()
    probs    = F.softmax(logits, dim=-1)
    entropy  = -(probs * (probs + 1e-9).log()).sum(-1).mean().item()
    max_prob = probs.max(-1).values.mean().item()
    return {"abs_max_logit": abs_max, "mean_entropy": entropy,
            "mean_max_prob": max_prob, "z_loss": z_loss(logits, 1.0).item()}

for name, logits in [
    ("healthy",  torch.randn(32, 8) * 1.0),
    ("moderate", torch.randn(32, 8) * 5.0),
    ("exploded", torch.randn(32, 8) * 20.0),
]:
    s = router_stability_check(logits)
    print(f"{name:>10}: max_logit={s['abs_max_logit']:.1f}  entropy={s['mean_entropy']:.3f}  z_loss={s['z_loss']:.2f}")
```

## Capacity Factor

Capacity factor is a hardware-level load-balancing mechanism used in both GShard and Switch Transformer. Each expert is allocated a fixed buffer of size C = capacity_factor * (batch_tokens / n_experts) tokens. If more than C tokens are routed to an expert, the overflow tokens are dropped (their representation passes through unchanged, or is zero-padded). The capacity factor is typically set to 1.0–1.25: 1.0 means perfect balance with zero slack, causing frequent dropping unless load is perfectly balanced; 1.25 provides a 25% buffer that absorbs mild imbalance without dropping. During training, dropped tokens still contribute to the LM loss (their target labels are unchanged) but do not pass through the expert, weakening their gradient. The capacity factor is usually reduced over training as the router learns to balance itself.

| Method | Load balance quality | Accuracy impact | Extra compute | Notes |
| --- | --- | --- | --- | --- |
| No balancing | Poor (collapse) | Severe (-3 to -5 PPL) | None | Fails without regularisation |
| Auxiliary loss (alpha=1e-2) | Good | Minimal (~0.1 PPL) | Negligible | Standard choice; Switch/GShard |
| Expert choice routing | Perfect (guaranteed) | None to slight gain | Moderate (softmax over tokens) | No aux loss needed; different dispatch logic |
| Z-loss (coeff=1e-3) | Good (prevents explosion) | Minimal | Negligible | Used alongside aux loss in ST-MoE |
| Token dropping (cap=1.0) | Good (bounded) | Slight (-0.2 to -0.5 PPL) | Negligible | Drops overflow tokens; hardware efficient |
| Buffer tokens | Moderate | Negligible | Small memory | Overflow tokens held in shared buffer |

## Monitoring Expert Utilization

Monitoring expert utilisation throughout training is essential because the LM loss is not a reliable indicator of load collapse — a model can produce good perplexity with only 2–3 active experts. The key metrics are: normalised entropy of the expert utilisation distribution (1.0 = perfectly balanced, 0.0 = full collapse); coefficient of variation (CV) of per-expert token counts (target < 0.3); and fraction of tokens dropped due to capacity overflow (target < 5%). These should be logged every 100–500 training steps. If normalised entropy drops below 0.7 or CV exceeds 0.5, increase alpha or inspect the router logits for saturation. A useful diagnostic is to plot the per-expert token fraction as a stacked bar chart over training — visual collapse is immediately obvious.

```python
import torch
import numpy as np
from collections import deque

class ExpertLoadMonitor:
    """Monitor per-expert token load over a sliding window of batches."""
    def __init__(self, n_experts: int, window: int = 500):
        self.n_experts = n_experts
        self.history   = deque(maxlen=window)

    def record(self, expert_indices: torch.Tensor) -> dict:
        """expert_indices: (N, top_k). Records load and returns current stats."""
        counts = torch.zeros(self.n_experts)
        for e in range(self.n_experts):
            counts[e] = (expert_indices == e).sum().float()
        load = counts / counts.sum()
        self.history.append(load.numpy())
        # Compute stats over history window
        hist  = np.stack(self.history)                     # (W, E)
        mean  = hist.mean(axis=0)
        cv    = mean.std() / (mean.mean() + 1e-9)
        ent   = -(mean * np.log(mean + 1e-9)).sum()
        max_e = np.log(self.n_experts)
        stats = {"cv": cv, "norm_entropy": ent / max_e,
                 "max_load": mean.max(), "min_load": mean.min()}
        if cv > 0.5:
            print(f"  ALERT: CV={cv:.3f} > 0.5 — possible expert collapse")
        return stats

monitor = ExpertLoadMonitor(n_experts=8, window=100)
for step in range(50):
    idx = torch.randint(0, 8, (64, 2))
    if step % 10 == 0:
        s = monitor.record(idx)
        print(f"step {step:>3}: norm_entropy={s['norm_entropy']:.3f}  cv={s['cv']:.3f}")
```

> **Expert Collapse is Not Self-Correcting**: Expert collapse is a training failure mode, not a convergence issue — once a few experts dominate, gradient signal stops flowing to others, making recovery difficult without strong auxiliary losses from the start. Monitor normalised entropy every 100 steps; if it drops below 0.7, increase alpha immediately.

## Key Takeaways

Load balancing is a first-class concern in MoE training, not an afterthought. The auxiliary loss (alpha ~ 1e-2) is the standard prevention mechanism and must be applied from the first training step. Z-loss (coeff ~ 1e-3) should be added alongside the auxiliary loss at large scale to prevent router logit explosion. Expert choice routing completely eliminates the load-imbalance problem at the cost of a different dispatch implementation. Capacity factor with token dropping is a hardware-efficiency tool, not a balancing solution — it caps damage from imbalance but does not prevent it. Monitor normalised entropy and CV throughout training, and alert when entropy drops below 0.7.

- Apply auxiliary load-balancing loss from step 1 with alpha ~ 1e-2 (Switch/GShard formula)
- Add Z-loss (coeff ~ 1e-3) at large scale to prevent router logit saturation
- Expert choice routing guarantees load balance by construction; no aux loss needed
- Capacity factor 1.0–1.25 caps tokens per expert; overflow tokens are dropped
- Monitor normalised entropy (target > 0.8) and CV (target < 0.3) every 100 steps
- Recovery from collapse is hard — prevention with strong alpha from step 1 is essential

