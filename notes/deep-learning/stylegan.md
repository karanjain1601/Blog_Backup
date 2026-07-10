---
title: "StyleGAN — Style-Based Generator and Adaptive Instance Norm"
slug: "stylegan"
description: "StyleGAN (Karras 2019) introduces a mapping network that disentangles the latent space, style injection via AdaIN at each resolution block, and per-pixel stochastic noise, enabling unprecedented control over coarse pose/shape and fine texture/colour attributes in high-resolution face synthesis."
tags: ["deep-learning", "generative-models", "gans"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3R5bGVHQU4gKEthcnJhcyBldCBhbC4gMjAxOSwgTlZJRElBKSBmdW5kYW1lbnRhbGx5IHJldGhpbmtzIHRoZSBnZW5lcmF0b3IgYXJjaGl0ZWN0dXJlIG9mIEdBTnMuIFJhdGhlciB0aGFuIGZlZWRpbmcgYSBsYXRlbnQgdmVjdG9yIHogZGlyZWN0bHkgaW50byBhIGNvbnZvbHV0aW9uYWwgc3RhY2ssIFN0eWxlR0FOIHNlcGFyYXRlcyB0d28gY29uY2VybnM6IGEgbWFwcGluZyBuZXR3b3JrIHRyYW5zZm9ybXMgeiBpbnRvIGFuIGludGVybWVkaWF0ZSBsYXRlbnQgdywgYW5kIHcgaXMgdGhlbiBpbmplY3RlZCBpbnRvIGV2ZXJ5IGxheWVyIG9mIGEgc3ludGhlc2lzIG5ldHdvcmsgdmlhIEFkYXB0aXZlIEluc3RhbmNlIE5vcm1hbGlzYXRpb24gKEFkYUlOKS4gVGhpcyBzZXBhcmF0aW9uIGRpc2VudGFuZ2xlcyB0aGUgbGF0ZW50IHNwYWNlIOKAlCBpbiBXIHNwYWNlLCBpbmRpdmlkdWFsIGRpbWVuc2lvbnMgY29udHJvbCBzZW1hbnRpY2FsbHkgY29oZXJlbnQgYXR0cmlidXRlcyAocG9zZSwgYWdlLCBoYWlyIGNvbG91cikgd2l0aG91dCB0aGUgZW50YW5nbGVkIGNvcnJlbGF0aW9ucyBzZWVuIGluIFogc3BhY2UuIFRoZSByZXN1bHQgaXMgYSBnZW5lcmF0b3IgdGhhdCBzdXBwb3J0cyBpbnR1aXRpdmUgc3R5bGUgbWl4aW5nLCBzdG9jaGFzdGljIGZpbmUtZGV0YWlsIGNvbnRyb2wsIGFuZCBzdGF0ZS1vZi10aGUtYXJ0IGltYWdlIHF1YWxpdHkgYXQgMTAyNHgxMDI0IHJlc29sdXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWFwcGluZyBOZXR3b3JrOiBaIFNwYWNlIHRvIFcgU3BhY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtYXBwaW5nIG5ldHdvcmsgZjogWiDihpIgVyBpcyBhbiA4LWxheWVyIGZ1bGx5LWNvbm5lY3RlZCBNTFAgd2l0aCBMZWFreVJlTFUgYWN0aXZhdGlvbnMuIFRoZSBpbnB1dCB6IH4gTigwLCBJKSBpcyBmaXJzdCBwaXhlbC1ub3JtYWxpc2VkLCB0aGVuIHRyYW5zZm9ybWVkIGludG8gdyDiiIggUl41MTIuIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IFogaXMgY29uc3RyYWluZWQgdG8gZm9sbG93IGEgc3RhbmRhcmQgR2F1c3NpYW4gcHJpb3IsIHdoaWNoIGZvcmNlcyB0aGUgZ2VuZXJhdG9yIHRvIHdhcnAgYW5kIGVudGFuZ2xlIGF0dHJpYnV0ZXMgdG8gZml0IHRoaXMgZml4ZWQgZGlzdHJpYnV0aW9uLiBXIGhhcyBubyBzdWNoIGZpeGVkIHByaW9yIOKAlCBpdCBpcyBsZWFybmVkIGFuZCBjYW4gdGFrZSB3aGF0ZXZlciBzaGFwZSBiZXN0IHJlcHJlc2VudHMgdGhlIGRhdGEgbWFuaWZvbGQuIFRoaXMgaXMgd2h5IFcgaXMgbW9yZSBkaXNlbnRhbmdsZWQ6IGRpcmVjdGlvbnMgaW4gVyBjb3JyZXNwb25kIG1vcmUgY2xlYW5seSB0byBpbmRpdmlkdWFsIHNlbWFudGljIGF0dHJpYnV0ZXMuIFRoZSBkaXNlbnRhbmdsZW1lbnQgaXMgbWVhc3VyZWQgYnkgdGhlIFBlcmNlcHR1YWwgUGF0aCBMZW5ndGggKFBQTCkgbWV0cmljIOKAlCBzaG9ydGVyLCBzbW9vdGhlciBwYXRocyB0aHJvdWdoIFcgc3BhY2UgaW5kaWNhdGUgYmV0dGVyIGRpc2VudGFuZ2xlbWVudC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlogc3BhY2UgZW50YW5nbGVtZW50OiBjaGFuZ2luZyBvbmUgZGltZW5zaW9uIG9mIHogYWZmZWN0cyBtdWx0aXBsZSBhdHRyaWJ1dGVzIHNpbXVsdGFuZW91c2x5IGJlY2F1c2UgdGhlIHByaW9yIGlzIGZpeGVkIEdhdXNzaWFuLiIsIlcgc3BhY2UgZGlzZW50YW5nbGVtZW50OiBXIGlzIGxlYXJuZWQsIHNvIGl0cyBnZW9tZXRyeSBjYW4gbWF0Y2ggdGhlIHRydWUgZGF0YSBtYW5pZm9sZCDigJQgb25lIGRpcmVjdGlvbiDiiYggb25lIGF0dHJpYnV0ZS4iLCJUcnVuY2F0aW9uIHRyaWNrOiBzYW1wbGUgdyBmcm9tIGEgdHJ1bmNhdGVkIGRpc3RyaWJ1dGlvbiAofHx3IC0gd19hdmd8fCBcdTAwM2MgcHNpKSB0byB0cmFkZSBkaXZlcnNpdHkgZm9yIHF1YWxpdHk7IHBzaT0wLjcgaXMgdHlwaWNhbC4iLCJTdHlsZSB0cmFuc2ZlcjogZ2l2ZW4gdHdvIGltYWdlcywgaW52ZXJ0IHRvIHcxIGFuZCB3MiwgdGhlbiB1c2UgdzEgZm9yIGNvYXJzZSBsYXllcnMgYW5kIHcyIGZvciBmaW5lIGxheWVycyB0byB0cmFuc2ZlciBmaW5lLWdyYWluZWQgdGV4dHVyZS4iLCJQUEwgbWVhc3VyZXMgdGhlIGF2ZXJhZ2UgcGVyY2VwdHVhbCBjaGFuZ2UgcGVyIHVuaXQgc3RlcCBpbiBXIOKAlCBsb3dlciBQUEwgbWVhbnMgVyBpcyBtb3JlIGxpbmVhcmx5IG9yZ2FuaXNlZCB3aXRoIHJlc3BlY3QgdG8gcGVyY2VwdGlvbi4iXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIE1hcHBpbmdOZXR3b3JrKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU3R5bGVHQU4gbWFwcGluZyBuZXR3b3JrOiB6IC1cdTAwM2UgdyB2aWEgOC1sYXllciBNTFAgd2l0aCBMZWFreVJlTFUuXG5cbiAgICBJbnB1dCB6IGlzIHBpeGVsLW5vcm1hbGlzZWQgYmVmb3JlIG1hcHBpbmcuXG4gICAgT3V0cHV0IHcgaXMgdGhlIGRpc2VudGFuZ2xlZCBpbnRlcm1lZGlhdGUgbGF0ZW50IHVzZWQgZm9yIHN0eWxlIGluamVjdGlvbi5cbiAgICBcIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgel9kaW09NTEyLCB3X2RpbT01MTIsIG5fbGF5ZXJzPTgsIGxyX211bD0wLjAxKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGxheWVycyA9IFtdXG4gICAgICAgIGZvciBpIGluIHJhbmdlKG5fbGF5ZXJzKTpcbiAgICAgICAgICAgIGluX2RpbSAgPSB6X2RpbSBpZiBpID09IDAgZWxzZSB3X2RpbVxuICAgICAgICAgICAgbGluZWFyICA9IG5uLkxpbmVhcihpbl9kaW0sIHdfZGltKVxuICAgICAgICAgICAgIyBMZWFybmluZyByYXRlIG11bHRpcGxpZXI6IHNjYWxlIHdlaWdodHMgZG93biwgc2NhbGUgZ3JhZGllbnRzIHVwXG4gICAgICAgICAgICBubi5pbml0Lm5vcm1hbF8obGluZWFyLndlaWdodCwgc3RkPTEuMCAvIGxyX211bClcbiAgICAgICAgICAgIG5uLmluaXQuemVyb3NfKGxpbmVhci5iaWFzKVxuICAgICAgICAgICAgbGF5ZXJzICs9IFtsaW5lYXIsIG5uLkxlYWt5UmVMVSgwLjIpXVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoKmxheWVycylcbiAgICAgICAgc2VsZi5scl9tdWwgPSBscl9tdWxcblxuICAgIGRlZiBwaXhlbF9ub3JtKHNlbGYsIHopOlxuICAgICAgICByZXR1cm4geiAvICh6LnBvdygyKS5tZWFuKGRpbT0xLCBrZWVwZGltPVRydWUpLnNxcnQoKSArIDFlLTgpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB6KTpcbiAgICAgICAgeiA9IHNlbGYucGl4ZWxfbm9ybSh6KVxuICAgICAgICB3ID0gc2VsZi5uZXQoeikgKiBzZWxmLmxyX211bFxuICAgICAgICByZXR1cm4gd1xuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubWFwcGluZyA9IE1hcHBpbmdOZXR3b3JrKHpfZGltPTUxMiwgd19kaW09NTEyLCBuX2xheWVycz04KVxueiA9IHRvcmNoLnJhbmRuKDQsIDUxMilcbncgPSBtYXBwaW5nKHopXG5wcmludChmXHUwMDI3eiBzaGFwZToge3ouc2hhcGV9IC1cdTAwM2UgdyBzaGFwZToge3cuc2hhcGV9XHUwMDI3KSAgIyAoNCwgNTEyKSAtXHUwMDNlICg0LCA1MTIpXG5wcmludChmXHUwMDI3dyBtZWFuOiB7dy5tZWFuKCk6LjRmfSAgc3RkOiB7dy5zdGQoKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFkYXB0aXZlIEluc3RhbmNlIE5vcm1hbGlzYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0eWxlIGluamVjdGlvbiBpbiBTdHlsZUdBTiB1c2VzIEFkYXB0aXZlIEluc3RhbmNlIE5vcm1hbGlzYXRpb24gKEFkYUlOKS4gQXQgZWFjaCBjb252b2x1dGlvbmFsIGxheWVyIGluIHRoZSBzeW50aGVzaXMgbmV0d29yaywgdGhlIGZlYXR1cmUgbWFwIHggaXMgZmlyc3QgaW5zdGFuY2Utbm9ybWFsaXNlZCAoemVybyBtZWFuLCB1bml0IHZhcmlhbmNlIHBlciBzcGF0aWFsIG1hcCBwZXIgY2hhbm5lbCksIHRoZW4gcmVzY2FsZWQgYW5kIHNoaWZ0ZWQgYnkgc3R5bGUgcGFyYW1ldGVycyBkZXJpdmVkIGZyb20gdzogQWRhSU4oeCwgeSkgPSB5X3MgwrcgKHggLSDOvCh4KSkgLyDPgyh4KSArIHlfYiwgd2hlcmUgKHlfcywgeV9iKSA9IEEodykgaXMgYW4gYWZmaW5lIHRyYW5zZm9ybSBvZiB0aGUgdyB2ZWN0b3IgKGEgbGVhcm5lZCBsaW5lYXIgbGF5ZXIpLiBFYWNoIHJlc29sdXRpb24gYmxvY2sgdXNlcyBpdHMgb3duIGFmZmluZSBsYXllciwgc28gdGhlIHN0eWxlIHBhcmFtZXRlcnMgZGlmZmVyIGF0IGV2ZXJ5IGxldmVsLiBUaGlzIGlzIGZ1bmRhbWVudGFsbHkgZGlmZmVyZW50IGZyb20gY29uZGl0aW9uaW5nIHZpYSBjb25jYXRlbmF0aW9uIOKAlCBBZGFJTiBpbmplY3RzIHN0eWxlIGJ5IGNvbnRyb2xsaW5nIHRoZSBzdGF0aXN0aWNhbCBtb21lbnRzIG9mIGVhY2ggZmVhdHVyZSBtYXAsIGEgbXVjaCBtb3JlIGV4cHJlc3NpdmUgZm9ybSBvZiBjb25kaXRpb25pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIEFkYUlOKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiQWRhcHRpdmUgSW5zdGFuY2UgTm9ybWFsaXNhdGlvbjogbm9ybWFsaXNlIHgsIHRoZW4gc2NhbGUrc2hpZnQgZnJvbSB3LlxuXG4gICAgQWRhSU4oeCwgdykgPSB5X3MgKiAoeCAtIG1lYW4oeCkpIC8gc3RkKHgpICsgeV9iXG4gICAgd2hlcmUgKHlfcywgeV9iKSA9IGFmZmluZSh3KSwgZWFjaCB3aXRoIHNoYXBlIChCLCBDKS5cbiAgICBJbnN0YW5jZSBub3JtIGlzIHBlci1zYW1wbGUgcGVyLWNoYW5uZWwgb3ZlciBzcGF0aWFsIGRpbXMuXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fY2hhbm5lbHMsIHdfZGltPTUxMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmluc3RhbmNlX25vcm0gPSBubi5JbnN0YW5jZU5vcm0yZChuX2NoYW5uZWxzLCBhZmZpbmU9RmFsc2UpXG4gICAgICAgICMgQWZmaW5lIHByb2plY3Rpb246IHcgLVx1MDAzZSAoc2NhbGUsIGJpYXMpIHBlciBjaGFubmVsXG4gICAgICAgIHNlbGYuYWZmaW5lID0gbm4uTGluZWFyKHdfZGltLCBuX2NoYW5uZWxzICogMilcbiAgICAgICAgbm4uaW5pdC5vbmVzXyhzZWxmLmFmZmluZS53ZWlnaHRbOm5fY2hhbm5lbHNdKSAgICMgaW5pdCBzY2FsZSB0byAxXG4gICAgICAgIG5uLmluaXQuemVyb3NfKHNlbGYuYWZmaW5lLndlaWdodFtuX2NoYW5uZWxzOl0pICAjIGluaXQgYmlhcyB0byAwXG4gICAgICAgIG5uLmluaXQuemVyb3NfKHNlbGYuYWZmaW5lLmJpYXMpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCB3KTpcbiAgICAgICAgIyB4OiAoQiwgQywgSCwgVyksIHc6IChCLCB3X2RpbSlcbiAgICAgICAgc3R5bGUgPSBzZWxmLmFmZmluZSh3KSAgICAgICAgICAgICAgICAgICAgICMgKEIsIDIqQylcbiAgICAgICAgeV9zLCB5X2IgPSBzdHlsZS5jaHVuaygyLCBkaW09MSkgICAgICAgICAgICMgZWFjaCAoQiwgQylcbiAgICAgICAgeV9zID0geV9zLnVuc3F1ZWV6ZSgtMSkudW5zcXVlZXplKC0xKSAgICAgICMgKEIsIEMsIDEsIDEpXG4gICAgICAgIHlfYiA9IHlfYi51bnNxdWVlemUoLTEpLnVuc3F1ZWV6ZSgtMSkgICAgICAjIChCLCBDLCAxLCAxKVxuICAgICAgICB4X25vcm0gPSBzZWxmLmluc3RhbmNlX25vcm0oeCkgICAgICAgICAgICAgIyB6ZXJvIG1lYW4sIHVuaXQgdmFyIHBlciAoQiwgQywgSCwgVylcbiAgICAgICAgcmV0dXJuIHlfcyAqIHhfbm9ybSArIHlfYiAgICAgICAgICAgICAgICAgICMgc3R5bGUtY29uZGl0aW9uZWQgZmVhdHVyZXNcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmFkYWluID0gQWRhSU4obl9jaGFubmVscz0yNTYsIHdfZGltPTUxMilcbnggPSB0b3JjaC5yYW5kbigyLCAyNTYsIDE2LCAxNikgICMgZmVhdHVyZSBtYXAgYXQgMTZ4MTYgcmVzb2x1dGlvblxudyA9IHRvcmNoLnJhbmRuKDIsIDUxMikgICAgICAgICAgICMgdyB2ZWN0b3IgZnJvbSBtYXBwaW5nIG5ldHdvcmtcbm91dCA9IGFkYWluKHgsIHcpXG5wcmludChmXHUwMDI3QWRhSU4gaW5wdXQ6ICBtZWFuPXt4Lm1lYW4oKTouNGZ9ICBzdGQ9e3guc3RkKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdBZGFJTiBvdXRwdXQ6IG1lYW49e291dC5tZWFuKCk6LjRmfSAgc3RkPXtvdXQuc3RkKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdPdXRwdXQgc2hhcGU6IHtvdXQuc2hhcGV9XHUwMDI3KSAgIyAoMiwgMjU2LCAxNiwgMTYpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RvY2hhc3RpYyBOb2lzZSBJbmplY3Rpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgTm9pc2VJbmplY3Rpb24obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJQZXItcGl4ZWwgR2F1c3NpYW4gbm9pc2Ugd2l0aCBsZWFybmFibGUgcGVyLWNoYW5uZWwgYW1wbGl0dWRlIEIuXG5cbiAgICB4X291dCA9IHggKyBCICogbm9pc2UgIHdoZXJlIG5vaXNlIH4gTigwLCBJKSBzYW1wbGVkIGZyZXNoIGVhY2ggZm9yd2FyZCBwYXNzLlxuICAgIEIgaXMgYSBsZWFybmFibGUgc2NhbGFyIHBlciBjaGFubmVsLCBpbml0aWFsaXNlZCB0byB6ZXJvIChubyBub2lzZSBhdCBzdGFydCkuXG4gICAgQ2FwdHVyZXMgc3RvY2hhc3RpYyB2YXJpYXRpb246IGhhaXIgc3RyYW5kIHBsYWNlbWVudCwgZnJlY2tsZXMsIHBvcmUgZGV0YWlsLlxuICAgIFRoaXMgdmFyaWF0aW9uIGlzIE5PVCBlbmNvZGVkIGluIHcg4oCUIGl0IGlzIGluZGVwZW5kZW50IHBlciBpbWFnZSBnZW5lcmF0aW9uLlxuICAgIFwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2NoYW5uZWxzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuQiA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcygxLCBuX2NoYW5uZWxzLCAxLCAxKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIG5vaXNlPU5vbmUpOlxuICAgICAgICBCX3ZhbCwgQywgSCwgVyA9IHguc2hhcGVcbiAgICAgICAgaWYgbm9pc2UgaXMgTm9uZTpcbiAgICAgICAgICAgIG5vaXNlID0gdG9yY2gucmFuZG4oQl92YWwsIDEsIEgsIFcsIGRldmljZT14LmRldmljZSlcbiAgICAgICAgcmV0dXJuIHggKyBzZWxmLkIgKiBub2lzZVxuXG5jbGFzcyBTdHlsZUNvbnZCbG9jayhubi5Nb2R1bGUpOlxuICAgIFwiXCJcIk9uZSBTdHlsZUdBTiBzeW50aGVzaXMgYmxvY2s6IENvbnYgLVx1MDAzZSBOb2lzZUluamVjdGlvbiAtXHUwMDNlIEFkYUlOIC1cdTAwM2UgQWN0aXZhdGlvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2gsIG91dF9jaCwgd19kaW09NTEyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuY29udiAgPSBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMywgcGFkZGluZz0xKVxuICAgICAgICBzZWxmLm5vaXNlID0gTm9pc2VJbmplY3Rpb24ob3V0X2NoKVxuICAgICAgICBzZWxmLmFkYWluID0gQWRhSU4ob3V0X2NoLCB3X2RpbSlcbiAgICAgICAgc2VsZi5hY3QgICA9IG5uLkxlYWt5UmVMVSgwLjIpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCB3LCBub2lzZT1Ob25lKTpcbiAgICAgICAgeCA9IHNlbGYuY29udih4KVxuICAgICAgICB4ID0gc2VsZi5ub2lzZSh4LCBub2lzZSlcbiAgICAgICAgeCA9IHNlbGYuYWRhaW4oeCwgdylcbiAgICAgICAgcmV0dXJuIHNlbGYuYWN0KHgpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5ibG9jayA9IFN0eWxlQ29udkJsb2NrKGluX2NoPTI1Niwgb3V0X2NoPTI1Niwgd19kaW09NTEyKVxueCA9IHRvcmNoLnJhbmRuKDIsIDI1NiwgMTYsIDE2KVxudyA9IHRvcmNoLnJhbmRuKDIsIDUxMilcbm91dDEgPSBibG9jayh4LCB3KVxub3V0MiA9IGJsb2NrKHgsIHcpICAjIGRpZmZlcmVudCBub2lzZSBlYWNoIGNhbGxcbnByaW50KGZcdTAwMjdPdXRwdXQgc2hhcGU6IHtvdXQxLnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdNYXggZGlmZiBiZXR3ZWVuIHR3byBydW5zIChkaWZmZXJlbnQgbm9pc2UpOiB7KG91dDEgLSBvdXQyKS5hYnMoKS5tYXgoKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0eWxlIE1peGluZyBhbmQgQ29hcnNlIHZzIEZpbmUgQ29udHJvbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3R5bGVHQU5cdTAwMjdzIHN5bnRoZXNpcyBuZXR3b3JrIG1hcHMgcmVzb2x1dGlvbiB0byBzZW1hbnRpYyBjb250ZW50OiBjb2Fyc2UgbGF5ZXJzICg0LTE2cHgpIGNvbnRyb2wgaGlnaC1sZXZlbCBhdHRyaWJ1dGVzIGxpa2UgcG9zZSwgZmFjZSBzaGFwZSwgYW5kIGhhaXIgc3R5bGU7IGZpbmUgbGF5ZXJzICg2NC0xMDI0cHgpIGNvbnRyb2wgY29sb3VyIHBhbGV0dGUsIHNraW4gdGV4dHVyZSwgYW5kIG1pY3Jvc3RydWN0dXJlIGRldGFpbHMuIFN0eWxlIG1peGluZyBleHBsb2l0cyB0aGlzIGJ5IHNhbXBsaW5nIHR3byBpbmRlcGVuZGVudCB3IHZlY3RvcnMgYW5kIHVzaW5nIHfigoEgZm9yIGNvYXJzZSBsYXllcnMgYW5kIHfigoIgZm9yIGZpbmUgbGF5ZXJzLiBUaGUgcmVzdWx0IGlzIGFuIGltYWdlIHRoYXQgaGFzIHRoZSBwb3NlIGFuZCBzaGFwZSBvZiB34oKBIGJ1dCB0aGUgY29sb3VyIGFuZCB0ZXh0dXJlIG9mIHfigoIuIFRoaXMgaXMgYWxzbyB1c2VkIGFzIGEgcmVndWxhcmlzYXRpb24gdGVjaG5pcXVlIGR1cmluZyB0cmFpbmluZzogd2l0aCBwcm9iYWJpbGl0eSAwLjksIGEgcmFuZG9tIG1peGluZyBwb2ludCBpcyBjaG9zZW4gc28gdGhlIGdlbmVyYXRvciBjYW5ub3QgdXNlIGZlYXR1cmUgY29ycmVsYXRpb25zIGFjcm9zcyBsYXllcnMgdG8gY2hlYXQgdGhlIExpcHNjaGl0eiBjb25zdHJhaW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3RcblxuY2xhc3MgU3R5bGVHQU5TeW50aGVzaXNOZXR3b3JrKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU2ltcGxpZmllZCBTdHlsZUdBTiBzeW50aGVzaXMgbmV0d29yayB3aXRoIHN0eWxlLW1peGluZyBzdXBwb3J0LlxuXG4gICAgQ29hcnNlIHJlc29sdXRpb25zICg0LTE2cHgpOiAgcG9zZSwgZmFjZSBzaGFwZSwgaGFpciBzdHlsZS5cbiAgICBGaW5lICAgcmVzb2x1dGlvbnMgKDMyLTEwMjRweCk6IGNvbG91ciBwYWxldHRlLCBtaWNyb3N0cnVjdHVyZSwgdGV4dHVyZXMuXG4gICAgU3R5bGUgbWl4aW5nOiB1c2UgdzEgZm9yIGNvYXJzZSBsYXllcnMsIHcyIGZvciBmaW5lIGxheWVycy5cbiAgICBcIlwiXCJcbiAgICBSRVNPTFVUSU9OUyA9IFs0LCA4LCAxNiwgMzIsIDY0XVxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHdfZGltPTUxMiwgY2hhbm5lbHM9Tm9uZSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBpZiBjaGFubmVscyBpcyBOb25lOlxuICAgICAgICAgICAgY2hhbm5lbHMgPSB7NDogNTEyLCA4OiA1MTIsIDE2OiAyNTYsIDMyOiAxMjgsIDY0OiA2NH1cbiAgICAgICAgc2VsZi5jb25zdCA9IG5uLlBhcmFtZXRlcih0b3JjaC5yYW5kbigxLCBjaGFubmVsc1s0XSwgNCwgNCkpXG4gICAgICAgIHNlbGYuYmxvY2tzID0gbm4uTW9kdWxlRGljdCgpXG4gICAgICAgIHByZXZfY2ggPSBjaGFubmVsc1s0XVxuICAgICAgICBmb3IgcmVzIGluIHNlbGYuUkVTT0xVVElPTlM6XG4gICAgICAgICAgICBjaCA9IGNoYW5uZWxzW3Jlc11cbiAgICAgICAgICAgIHNlbGYuYmxvY2tzW2ZcdTAwMjdjb252X3tyZXN9YVx1MDAyN10gPSBTdHlsZUNvbnZCbG9jayhwcmV2X2NoLCBjaCwgd19kaW0pXG4gICAgICAgICAgICBzZWxmLmJsb2Nrc1tmXHUwMDI3Y29udl97cmVzfWJcdTAwMjddID0gU3R5bGVDb252QmxvY2soY2gsIGNoLCB3X2RpbSlcbiAgICAgICAgICAgIHByZXZfY2ggPSBjaFxuICAgICAgICBzZWxmLnRvX3JnYiA9IG5uLkNvbnYyZChjaGFubmVsc1s2NF0sIDMsIDEpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB3czogTGlzdFt0b3JjaC5UZW5zb3JdLCBtaXhpbmdfY3V0b2ZmOiBpbnQgPSBOb25lKTpcbiAgICAgICAgXCJcIlwid3M6IGxpc3Qgb2YgdyB2ZWN0b3JzLiBJZiBtaXhpbmdfY3V0b2ZmIHNldCwgd3NbMF0gZm9yIGNvYXJzZSwgd3NbMV0gZm9yIGZpbmUuXCJcIlwiXG4gICAgICAgIEIgPSB3c1swXS5zaXplKDApXG4gICAgICAgIHggPSBzZWxmLmNvbnN0LmV4cGFuZChCLCAtMSwgLTEsIC0xKVxuICAgICAgICBsYXllcl9pZHggPSAwXG4gICAgICAgIGZvciBpLCByZXMgaW4gZW51bWVyYXRlKHNlbGYuUkVTT0xVVElPTlMpOlxuICAgICAgICAgICAgdyA9IHdzWzBdIGlmIChtaXhpbmdfY3V0b2ZmIGlzIE5vbmUgb3IgbGF5ZXJfaWR4IFx1MDAzYyBtaXhpbmdfY3V0b2ZmKSBlbHNlIHdzWzFdXG4gICAgICAgICAgICBpZiByZXMgXHUwMDNlIDQ6XG4gICAgICAgICAgICAgICAgeCA9IG5uLmZ1bmN0aW9uYWwuaW50ZXJwb2xhdGUoeCwgc2NhbGVfZmFjdG9yPTIsIG1vZGU9XHUwMDI3YmlsaW5lYXJcdTAwMjcsIGFsaWduX2Nvcm5lcnM9RmFsc2UpXG4gICAgICAgICAgICB4ID0gc2VsZi5ibG9ja3NbZlx1MDAyN2NvbnZfe3Jlc31hXHUwMDI3XSh4LCB3KVxuICAgICAgICAgICAgeCA9IHNlbGYuYmxvY2tzW2ZcdTAwMjdjb252X3tyZXN9Ylx1MDAyN10oeCwgdylcbiAgICAgICAgICAgIGxheWVyX2lkeCArPSAyXG4gICAgICAgIHJldHVybiBzZWxmLnRvX3JnYih4KVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubmV0ID0gU3R5bGVHQU5TeW50aGVzaXNOZXR3b3JrKClcbncxID0gdG9yY2gucmFuZG4oMiwgNTEyKSAgIyBjb2Fyc2Ugc3R5bGU6IGNvbnRyb2xzIHBvc2UsIHNoYXBlXG53MiA9IHRvcmNoLnJhbmRuKDIsIDUxMikgICMgZmluZSBzdHlsZTogICBjb250cm9scyBjb2xvdXIsIHRleHR1cmVcbmltZ193MSAgPSBuZXQoW3cxXSlcbnByaW50KGZcdTAwMjdTaW5nbGUgc3R5bGUgb3V0cHV0OiB7aW1nX3cxLnNoYXBlfVx1MDAyNykgICMgKDIsIDMsIDY0LCA2NClcbmltZ19taXggPSBuZXQoW3cxLCB3Ml0sIG1peGluZ19jdXRvZmY9NClcbnByaW50KGZcdTAwMjdNaXhlZCBzdHlsZSBvdXRwdXQ6ICB7aW1nX21peC5zaGFwZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3R5bGVHQU4yIEltcHJvdmVtZW50cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3R5bGVHQU4yIChLYXJyYXMgZXQgYWwuIDIwMjApIGFkZHJlc3NlZCB0d28gbWFpbiBhcnRpZmFjdHMgZnJvbSBTdHlsZUdBTjEuIEZpcnN0LCBcdTAwMjd3YXRlciBkcm9wbGV0XHUwMDI3IGFydGlmYWN0cyBhcHBlYXJpbmcgYXQgZml4ZWQgcGl4ZWwgcG9zaXRpb25zIHdlcmUgdHJhY2VkIHRvIEFkYUlOOiBpbnN0YW5jZSBub3JtYWxpc2F0aW9uIGFsbG93cyB0aGUgZ2VuZXJhdG9yIHRvIGhpZGUgaW5mb3JtYXRpb24gaW4gZmVhdHVyZSBtYXAgc3RhdGlzdGljcyByYXRoZXIgdGhhbiBzcGF0aWFsIGNvbnRlbnQuIFN0eWxlR0FOMiByZXBsYWNlcyBBZGFJTiB3aXRoIHdlaWdodCBkZW1vZHVsYXRpb24g4oCUIGluc3RlYWQgb2Ygbm9ybWFsaXNpbmcgdGhlIGZlYXR1cmUgbWFwLCBpdCBub3JtYWxpc2VzIHRoZSBjb252b2x1dGlvbiB3ZWlnaHRzIGJhc2VkIG9uIHRoZSBleHBlY3RlZCB1bml0LXN0YW5kYXJkLWRldmlhdGlvbiBpbnB1dCwgZWxpbWluYXRpbmcgdGhlIGFydGlmYWN0IHdoaWxlIHByZXNlcnZpbmcgc3R5bGUgaW5qZWN0aW9uLiBTZWNvbmQsIHByb2dyZXNzaXZlIGdyb3dpbmcgaW50cm9kdWNlZCBwaGFzZSBhcnRpZmFjdHMgYXQgcmVzb2x1dGlvbiBib3VuZGFyaWVzLiBTdHlsZUdBTjIgdHJhaW5zIGF0IGZ1bGwgcmVzb2x1dGlvbiBmcm9tIHRoZSBzdGFydCB1c2luZyBza2lwIGNvbm5lY3Rpb25zIHRvIGEgc2VyaWVzIG9mIFJHQiBvdXRwdXRzIHRoYXQgYXJlIHN1bW1lZCBkdXJpbmcgdHJhaW5pbmcuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJXZWlnaHQgZGVtb2R1bGF0aW9uOiBzY2FsZSBjb252IHdlaWdodHMgYnkgdy1kZXJpdmVkIHN0eWxlIChtb2R1bGF0aW9uKSwgdGhlbiBkaXZpZGUgZWFjaCBvdXRwdXQgYnkgdGhlIGV4cGVjdGVkIHN0ZCAoZGVtb2R1bGF0aW9uKSDigJQgYXZvaWRzIG9wZXJhdGluZyBvbiBmZWF0dXJlIHN0YXRpc3RpY3MuIiwiTm8gcHJvZ3Jlc3NpdmUgZ3Jvd2luZzogU3R5bGVHQU4yIHRyYWlucyBhdCBmdWxsIHJlc29sdXRpb24gd2l0aCBNU0ctc3R5bGUgc2tpcCBjb25uZWN0aW9ucyDigJQgc2ltcGxlciBhbmQgYXZvaWRzIHBoYXNlLXRyYW5zaXRpb24gYXJ0aWZhY3RzLiIsIlBhdGggbGVuZ3RoIHJlZ3VsYXJpc2F0aW9uIChsYXp5LCBldmVyeSAxNiBzdGVwcyk6IGVuY291cmFnZSB8fEpeVCBhfHwgdG8gYmUgY29uc3RhbnQgZm9yIHJhbmRvbSBhIH4gTigwLEkpLCBzbW9vdGhpbmcgdGhlIFctc3BhY2UgZ2VvbWV0cnkuIiwiUjEgZ3JhZGllbnQgcGVuYWx0eSByZXBsYWNlcyBXR0FOLUdQOiBzaW1wbGVyLCBjb21wYXRpYmxlIHdpdGggQmF0Y2hOb3JtIGluIGdlbmVyYXRvciwgc3RhbmRhcmQgZm9yIGFsbCBHQU4gc3RhYmlsaXNhdGlvbi4iLCJGSUQgaW1wcm92ZW1lbnQ6IEZGSFEgMTAyNHB4IEZJRCBkcm9wcyBmcm9tIDQuNDAgKFN0eWxlR0FOKSB0byAyLjg0IChTdHlsZUdBTjIpIHdpdGggdGhlIHNhbWUgdHJhaW5pbmcgZGF0YS4iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlcrIFNwYWNlIGZvciBHQU4gSW52ZXJzaW9uIiwiY29udGVudCI6IlN0eWxlR0FOXHUwMDI3cyBXIHNwYWNlIGhhcyBhIHNpbmdsZSB3IHZlY3RvciBicm9hZGNhc3QgdG8gYWxsIGxheWVycy4gVysgc3BhY2UgZXh0ZW5kcyB0aGlzIHRvIGEgc2VwYXJhdGUgd19pIHBlciBsYXllciAoMTggdmVjdG9ycyBmb3IgU3R5bGVHQU4gYXQgMTAyNHB4KSwgZ2l2aW5nIG1vcmUgZGVncmVlcyBvZiBmcmVlZG9tIGZvciBHQU4gaW52ZXJzaW9uIOKAlCBlbmNvZGluZyBhIHJlYWwgcGhvdG8gYmFjayBpbnRvIGEgbGF0ZW50LiBXKyBpcyB1c2VkIGJ5IGU0ZSBhbmQgUFRJIGVuY29kZXJzLiBFZGl0cyBpbiBXIHNwYWNlIGdlbmVyYWxpc2UgYmV0dGVyIChzYW1lIGRpcmVjdGlvbiBmb3IgYWxsIGxheWVycyk7IGVkaXRzIGluIFcrIGFsbG93IGxheWVyLXNwZWNpZmljIGFkanVzdG1lbnRzIGJ1dCBhcmUgbGVzcyBzZW1hbnRpY2FsbHkgY29oZXJlbnQuIEZvciBhdHRyaWJ1dGUgZWRpdGluZyAoYWdlLCBzbWlsZSksIHdvcmsgaW4gVzsgZm9yIGZhaXRoZnVsIHJlY29uc3RydWN0aW9uIG9mIHNwZWNpZmljIGlkZW50aXRpZXMsIHVzZSBXKy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcm9ncmVzc2l2ZSBHcm93aW5nIGFuZCBUcmFpbmluZyBTdGFiaWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJvdGggU3R5bGVHQU4gYW5kIGl0cyBwcmVkZWNlc3NvciBQcm9ncmVzc2l2ZUdBTiAoS2FycmFzIGV0IGFsLiAyMDE4KSBncm93IHRoZSBnZW5lcmF0b3IgYW5kIGRpc2NyaW1pbmF0b3IgcmVzb2x1dGlvbiBpbmNyZW1lbnRhbGx5IOKAlCBzdGFydGluZyBhdCA0eDQgYW5kIGRvdWJsaW5nIGV2ZXJ5IGZldyBodW5kcmVkIGtpbWcgdW50aWwgcmVhY2hpbmcgdGhlIHRhcmdldCByZXNvbHV0aW9uLiBOZXcgbGF5ZXJzIGFyZSBmYWRlZCBpbiB3aXRoIGEgbGluZWFyIGFscGhhIGJsZW5kaW5nIHNjaGVkdWxlIHRvIGF2b2lkIHN1ZGRlbiBjYXBhY2l0eSBqdW1wcy4gVGhpcyB0ZWNobmlxdWUgZHJhbWF0aWNhbGx5IHJlZHVjZXMgdHJhaW5pbmcgdGltZSBmb3IgaGlnaC1yZXNvbHV0aW9uIHN5bnRoZXNpcyAoMTAyNHgxMDI0KSBiZWNhdXNlIG1vc3QgdHJhaW5pbmcgaXRlcmF0aW9ucyBhcmUgc3BlbnQgYXQgbG93ZXIgcmVzb2x1dGlvbnMgd2hlcmUgY29tcHV0ZSBpcyBjaGVhcC4gU3R5bGVHQU4xIGluaGVyaXRlZCBwcm9ncmVzc2l2ZSBncm93aW5nIGRpcmVjdGx5OyBTdHlsZUdBTjIgYWJhbmRvbmVkIGl0IGluIGZhdm91ciBvZiBza2lwLWNvbm5lY3Rpb24gYXJjaGl0ZWN0dXJlcyB0aGF0IHRyYWluIGF0IGZ1bGwgcmVzb2x1dGlvbiBmcm9tIHRoZSBzdGFydCwgdHJhZGluZyBzaW1wbGljaXR5IGZvciB0aGUgZWxpbWluYXRpb24gb2YgcGhhc2UgYXJ0aWZhY3RzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFyY2hpdGVjdHVyZSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiS2V5IElubm92YXRpb24iLCJGSUQgYXQgMTAyNHB4IiwiQXJ0aWZhY3RzIiwiVHJhaW5pbmcgQ29zdCJdLCJyb3dzIjpbWyJEQ0dBTiIsIkRlZXAgY29udiBnZW5lcmF0b3IvZGlzY3JpbWluYXRvciwgQk4sIG5vIEZDIGxheWVycyIsIn4zNSAoMjU2cHgpIiwiQ2hlY2tlcmJvYXJkICh0cmFuc3Bvc2UgY29udiksIG1vZGUgY29sbGFwc2UiLCJMb3cg4oCUIGhvdXJzIG9uIDEgR1BVIl0sWyJQcm9ncmVzc2l2ZUdBTiIsIkdyb3cgcmVzb2x1dGlvbiA0LVx1MDAzZTEwMjQgcHJvZ3Jlc3NpdmVseSwgZmFkZS1pbiBsYXllcnMiLCI4LjA0IiwiUGhhc2UgdHJhbnNpdGlvbiBhcnRpZmFjdHMgYXQgcmVzb2x1dGlvbiBib3VuZGFyaWVzIiwiSGlnaCDigJQgZGF5cyBvbiA4IEdQVXMiXSxbIlN0eWxlR0FOIiwiTWFwcGluZyBuZXQgKyBBZGFJTiBzdHlsZSBpbmplY3Rpb24gKyBub2lzZSArIHByb2cgZ3JvdyIsIjQuNDAiLCJXYXRlciBkcm9wbGV0IGFydGlmYWN0cyAoQWRhSU4gc3RhdGlzdGljcyksIHBoYXNlIGFydGlmYWN0cyIsIlZlcnkgaGlnaCDigJQgd2Vla3Mgb24gOCBHUFVzIl0sWyJTdHlsZUdBTjIiLCJXZWlnaHQgZGVtb2R1bGF0aW9uLCBubyBwcm9ncmVzc2l2ZSBncm93LCBwYXRoIGxlbmd0aCByZWcsIFIxIiwiMi44NCIsIlNpZ25pZmljYW50bHkgcmVkdWNlZCDigJQgbm8gZHJvcGxldHMsIG5vIHBoYXNlIGFydGlmYWN0cyIsIlZlcnkgaGlnaCDigJQgd2Vla3Mgb24gOCBHUFVzIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRoZSBtYXBwaW5nIG5ldHdvcmsgdXNlcyBscl9tdWw9MC4wMSDigJQgdGhlIGxlYXJuaW5nIHJhdGUgbXVsdGlwbGllciBzY2FsZXMgd2VpZ2h0cyBkb3duIGF0IGluaXQgYW5kIGdyYWRpZW50cyB1cCBkdXJpbmcgb3B0aW1pc2F0aW9uLCBzdGFiaWxpc2luZyB0aGUgTUxQIHRyYWluaW5nLiIsIkVhY2ggcmVzb2x1dGlvbiBibG9jayBpbiB0aGUgc3ludGhlc2lzIG5ldHdvcmsgaGFzIGl0cyBvd24gYWZmaW5lIGxheWVyIEEodyksIGdpdmluZyAxOCBpbmRlcGVuZGVudCBzdHlsZSB2ZWN0b3JzIGF0IDEwMjRweCByZXNvbHV0aW9uICgyIHBlciByZXNvbHV0aW9uIGZyb20gNHB4IHRvIDEwMjRweCkuIiwiU3RvY2hhc3RpYyBub2lzZSBhbXBsaXR1ZGUgQiBpcyBpbml0aWFsaXNlZCB0byB6ZXJvLCBzbyBub2lzZSBoYXMgbm8gZWZmZWN0IGF0IHRyYWluaW5nIHN0YXJ0IOKAlCBpdCBpcyBsZWFybmVkIGdyYWR1YWxseSBhcyB0aGUgZ2VuZXJhdG9yIHJlZmluZXMgZmluZSBkZXRhaWxzLiIsIlN0eWxlIG1peGluZyByZWd1bGFyaXNhdGlvbjogZHVyaW5nIHRyYWluaW5nLCBzb21lIHNhbXBsZXMgdXNlIHR3byBkaWZmZXJlbnQgdyB2ZWN0b3JzIChjb2Fyc2UvZmluZSBzcGxpdCBhdCBhIHJhbmRvbSBsYXllcikgdG8gcHJldmVudCBjcm9zcy1sYXllciBkZXBlbmRlbmNpZXMuIiwiU3R5bGVHQU4yIHdlaWdodCBkZW1vZHVsYXRpb24gaXMgaW1wbGVtZW50ZWQgYXMgYSBmdXNlZCBsYXllciB0aGF0IGNvbWJpbmVzIG1vZHVsYXRpb24sIGNvbnZvbHV0aW9uLCBhbmQgZGVtb2R1bGF0aW9uIGluIGEgc2luZ2xlIGVmZmljaWVudCBDVURBIGtlcm5lbC4iLCJQUEwgKFBlcmNlcHR1YWwgUGF0aCBMZW5ndGgpIG1lYXN1cmVzIFctc3BhY2UgZGlzZW50YW5nbGVtZW50OiBsb3dlciBQUEwgbWVhbnMgdHJhdmVyc2FscyBiZXR3ZWVuIHcgdmVjdG9ycyBwcm9kdWNlIHNtb290aGVyLCBtb3JlIHByZWRpY3RhYmxlIGltYWdlIGNoYW5nZXMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# StyleGAN — Style-Based Generator and Adaptive Instance Norm

StyleGAN (Karras et al. 2019, NVIDIA) fundamentally rethinks the generator architecture of GANs. Rather than feeding a latent vector z directly into a convolutional stack, StyleGAN separates two concerns: a mapping network transforms z into an intermediate latent w, and w is then injected into every layer of a synthesis network via Adaptive Instance Normalisation (AdaIN). This separation disentangles the latent space — in W space, individual dimensions control semantically coherent attributes (pose, age, hair colour) without the entangled correlations seen in Z space. The result is a generator that supports intuitive style mixing, stochastic fine-detail control, and state-of-the-art image quality at 1024x1024 resolution.

## Mapping Network: Z Space to W Space

The mapping network f: Z → W is an 8-layer fully-connected MLP with LeakyReLU activations. The input z ~ N(0, I) is first pixel-normalised, then transformed into w ∈ R^512. The key insight is that Z is constrained to follow a standard Gaussian prior, which forces the generator to warp and entangle attributes to fit this fixed distribution. W has no such fixed prior — it is learned and can take whatever shape best represents the data manifold. This is why W is more disentangled: directions in W correspond more cleanly to individual semantic attributes. The disentanglement is measured by the Perceptual Path Length (PPL) metric — shorter, smoother paths through W space indicate better disentanglement.

- Z space entanglement: changing one dimension of z affects multiple attributes simultaneously because the prior is fixed Gaussian.
- W space disentanglement: W is learned, so its geometry can match the true data manifold — one direction ≈ one attribute.
- Truncation trick: sample w from a truncated distribution (||w - w_avg|| < psi) to trade diversity for quality; psi=0.7 is typical.
- Style transfer: given two images, invert to w1 and w2, then use w1 for coarse layers and w2 for fine layers to transfer fine-grained texture.
- PPL measures the average perceptual change per unit step in W — lower PPL means W is more linearly organised with respect to perception.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MappingNetwork(nn.Module):
    """StyleGAN mapping network: z -> w via 8-layer MLP with LeakyReLU.

    Input z is pixel-normalised before mapping.
    Output w is the disentangled intermediate latent used for style injection.
    """
    def __init__(self, z_dim=512, w_dim=512, n_layers=8, lr_mul=0.01):
        super().__init__()
        layers = []
        for i in range(n_layers):
            in_dim  = z_dim if i == 0 else w_dim
            linear  = nn.Linear(in_dim, w_dim)
            # Learning rate multiplier: scale weights down, scale gradients up
            nn.init.normal_(linear.weight, std=1.0 / lr_mul)
            nn.init.zeros_(linear.bias)
            layers += [linear, nn.LeakyReLU(0.2)]
        self.net = nn.Sequential(*layers)
        self.lr_mul = lr_mul

    def pixel_norm(self, z):
        return z / (z.pow(2).mean(dim=1, keepdim=True).sqrt() + 1e-8)

    def forward(self, z):
        z = self.pixel_norm(z)
        w = self.net(z) * self.lr_mul
        return w

torch.manual_seed(0)
mapping = MappingNetwork(z_dim=512, w_dim=512, n_layers=8)
z = torch.randn(4, 512)
w = mapping(z)
print(f'z shape: {z.shape} -> w shape: {w.shape}')  # (4, 512) -> (4, 512)
print(f'w mean: {w.mean():.4f}  std: {w.std():.4f}')
```

## Adaptive Instance Normalisation

Style injection in StyleGAN uses Adaptive Instance Normalisation (AdaIN). At each convolutional layer in the synthesis network, the feature map x is first instance-normalised (zero mean, unit variance per spatial map per channel), then rescaled and shifted by style parameters derived from w: AdaIN(x, y) = y_s · (x - μ(x)) / σ(x) + y_b, where (y_s, y_b) = A(w) is an affine transform of the w vector (a learned linear layer). Each resolution block uses its own affine layer, so the style parameters differ at every level. This is fundamentally different from conditioning via concatenation — AdaIN injects style by controlling the statistical moments of each feature map, a much more expressive form of conditioning.

```python
import torch
import torch.nn as nn

class AdaIN(nn.Module):
    """Adaptive Instance Normalisation: normalise x, then scale+shift from w.

    AdaIN(x, w) = y_s * (x - mean(x)) / std(x) + y_b
    where (y_s, y_b) = affine(w), each with shape (B, C).
    Instance norm is per-sample per-channel over spatial dims.
    """
    def __init__(self, n_channels, w_dim=512):
        super().__init__()
        self.instance_norm = nn.InstanceNorm2d(n_channels, affine=False)
        # Affine projection: w -> (scale, bias) per channel
        self.affine = nn.Linear(w_dim, n_channels * 2)
        nn.init.ones_(self.affine.weight[:n_channels])   # init scale to 1
        nn.init.zeros_(self.affine.weight[n_channels:])  # init bias to 0
        nn.init.zeros_(self.affine.bias)

    def forward(self, x, w):
        # x: (B, C, H, W), w: (B, w_dim)
        style = self.affine(w)                     # (B, 2*C)
        y_s, y_b = style.chunk(2, dim=1)           # each (B, C)
        y_s = y_s.unsqueeze(-1).unsqueeze(-1)      # (B, C, 1, 1)
        y_b = y_b.unsqueeze(-1).unsqueeze(-1)      # (B, C, 1, 1)
        x_norm = self.instance_norm(x)             # zero mean, unit var per (B, C, H, W)
        return y_s * x_norm + y_b                  # style-conditioned features

torch.manual_seed(0)
adain = AdaIN(n_channels=256, w_dim=512)
x = torch.randn(2, 256, 16, 16)  # feature map at 16x16 resolution
w = torch.randn(2, 512)           # w vector from mapping network
out = adain(x, w)
print(f'AdaIN input:  mean={x.mean():.4f}  std={x.std():.4f}')
print(f'AdaIN output: mean={out.mean():.4f}  std={out.std():.4f}')
print(f'Output shape: {out.shape}')  # (2, 256, 16, 16)
```

## Stochastic Noise Injection

```python
import torch
import torch.nn as nn

class NoiseInjection(nn.Module):
    """Per-pixel Gaussian noise with learnable per-channel amplitude B.

    x_out = x + B * noise  where noise ~ N(0, I) sampled fresh each forward pass.
    B is a learnable scalar per channel, initialised to zero (no noise at start).
    Captures stochastic variation: hair strand placement, freckles, pore detail.
    This variation is NOT encoded in w — it is independent per image generation.
    """
    def __init__(self, n_channels):
        super().__init__()
        self.B = nn.Parameter(torch.zeros(1, n_channels, 1, 1))

    def forward(self, x, noise=None):
        B_val, C, H, W = x.shape
        if noise is None:
            noise = torch.randn(B_val, 1, H, W, device=x.device)
        return x + self.B * noise

class StyleConvBlock(nn.Module):
    """One StyleGAN synthesis block: Conv -> NoiseInjection -> AdaIN -> Activation."""
    def __init__(self, in_ch, out_ch, w_dim=512):
        super().__init__()
        self.conv  = nn.Conv2d(in_ch, out_ch, 3, padding=1)
        self.noise = NoiseInjection(out_ch)
        self.adain = AdaIN(out_ch, w_dim)
        self.act   = nn.LeakyReLU(0.2)

    def forward(self, x, w, noise=None):
        x = self.conv(x)
        x = self.noise(x, noise)
        x = self.adain(x, w)
        return self.act(x)

torch.manual_seed(0)
block = StyleConvBlock(in_ch=256, out_ch=256, w_dim=512)
x = torch.randn(2, 256, 16, 16)
w = torch.randn(2, 512)
out1 = block(x, w)
out2 = block(x, w)  # different noise each call
print(f'Output shape: {out1.shape}')
print(f'Max diff between two runs (different noise): {(out1 - out2).abs().max():.4f}')
```

## Style Mixing and Coarse vs Fine Control

StyleGAN's synthesis network maps resolution to semantic content: coarse layers (4-16px) control high-level attributes like pose, face shape, and hair style; fine layers (64-1024px) control colour palette, skin texture, and microstructure details. Style mixing exploits this by sampling two independent w vectors and using w₁ for coarse layers and w₂ for fine layers. The result is an image that has the pose and shape of w₁ but the colour and texture of w₂. This is also used as a regularisation technique during training: with probability 0.9, a random mixing point is chosen so the generator cannot use feature correlations across layers to cheat the Lipschitz constraint.

```python
import torch
import torch.nn as nn
from typing import List

class StyleGANSynthesisNetwork(nn.Module):
    """Simplified StyleGAN synthesis network with style-mixing support.

    Coarse resolutions (4-16px):  pose, face shape, hair style.
    Fine   resolutions (32-1024px): colour palette, microstructure, textures.
    Style mixing: use w1 for coarse layers, w2 for fine layers.
    """
    RESOLUTIONS = [4, 8, 16, 32, 64]

    def __init__(self, w_dim=512, channels=None):
        super().__init__()
        if channels is None:
            channels = {4: 512, 8: 512, 16: 256, 32: 128, 64: 64}
        self.const = nn.Parameter(torch.randn(1, channels[4], 4, 4))
        self.blocks = nn.ModuleDict()
        prev_ch = channels[4]
        for res in self.RESOLUTIONS:
            ch = channels[res]
            self.blocks[f'conv_{res}a'] = StyleConvBlock(prev_ch, ch, w_dim)
            self.blocks[f'conv_{res}b'] = StyleConvBlock(ch, ch, w_dim)
            prev_ch = ch
        self.to_rgb = nn.Conv2d(channels[64], 3, 1)

    def forward(self, ws: List[torch.Tensor], mixing_cutoff: int = None):
        """ws: list of w vectors. If mixing_cutoff set, ws[0] for coarse, ws[1] for fine."""
        B = ws[0].size(0)
        x = self.const.expand(B, -1, -1, -1)
        layer_idx = 0
        for i, res in enumerate(self.RESOLUTIONS):
            w = ws[0] if (mixing_cutoff is None or layer_idx < mixing_cutoff) else ws[1]
            if res > 4:
                x = nn.functional.interpolate(x, scale_factor=2, mode='bilinear', align_corners=False)
            x = self.blocks[f'conv_{res}a'](x, w)
            x = self.blocks[f'conv_{res}b'](x, w)
            layer_idx += 2
        return self.to_rgb(x)

torch.manual_seed(0)
net = StyleGANSynthesisNetwork()
w1 = torch.randn(2, 512)  # coarse style: controls pose, shape
w2 = torch.randn(2, 512)  # fine style:   controls colour, texture
img_w1  = net([w1])
print(f'Single style output: {img_w1.shape}')  # (2, 3, 64, 64)
img_mix = net([w1, w2], mixing_cutoff=4)
print(f'Mixed style output:  {img_mix.shape}')
```

## StyleGAN2 Improvements

StyleGAN2 (Karras et al. 2020) addressed two main artifacts from StyleGAN1. First, 'water droplet' artifacts appearing at fixed pixel positions were traced to AdaIN: instance normalisation allows the generator to hide information in feature map statistics rather than spatial content. StyleGAN2 replaces AdaIN with weight demodulation — instead of normalising the feature map, it normalises the convolution weights based on the expected unit-standard-deviation input, eliminating the artifact while preserving style injection. Second, progressive growing introduced phase artifacts at resolution boundaries. StyleGAN2 trains at full resolution from the start using skip connections to a series of RGB outputs that are summed during training.

- Weight demodulation: scale conv weights by w-derived style (modulation), then divide each output by the expected std (demodulation) — avoids operating on feature statistics.
- No progressive growing: StyleGAN2 trains at full resolution with MSG-style skip connections — simpler and avoids phase-transition artifacts.
- Path length regularisation (lazy, every 16 steps): encourage ||J^T a|| to be constant for random a ~ N(0,I), smoothing the W-space geometry.
- R1 gradient penalty replaces WGAN-GP: simpler, compatible with BatchNorm in generator, standard for all GAN stabilisation.
- FID improvement: FFHQ 1024px FID drops from 4.40 (StyleGAN) to 2.84 (StyleGAN2) with the same training data.

> **W+ Space for GAN Inversion**: StyleGAN's W space has a single w vector broadcast to all layers. W+ space extends this to a separate w_i per layer (18 vectors for StyleGAN at 1024px), giving more degrees of freedom for GAN inversion — encoding a real photo back into a latent. W+ is used by e4e and PTI encoders. Edits in W space generalise better (same direction for all layers); edits in W+ allow layer-specific adjustments but are less semantically coherent. For attribute editing (age, smile), work in W; for faithful reconstruction of specific identities, use W+.

## Progressive Growing and Training Stability

Both StyleGAN and its predecessor ProgressiveGAN (Karras et al. 2018) grow the generator and discriminator resolution incrementally — starting at 4x4 and doubling every few hundred kimg until reaching the target resolution. New layers are faded in with a linear alpha blending schedule to avoid sudden capacity jumps. This technique dramatically reduces training time for high-resolution synthesis (1024x1024) because most training iterations are spent at lower resolutions where compute is cheap. StyleGAN1 inherited progressive growing directly; StyleGAN2 abandoned it in favour of skip-connection architectures that train at full resolution from the start, trading simplicity for the elimination of phase artifacts.

## Architecture Comparison

| Model | Key Innovation | FID at 1024px | Artifacts | Training Cost |
| --- | --- | --- | --- | --- |
| DCGAN | Deep conv generator/discriminator, BN, no FC layers | ~35 (256px) | Checkerboard (transpose conv), mode collapse | Low — hours on 1 GPU |
| ProgressiveGAN | Grow resolution 4->1024 progressively, fade-in layers | 8.04 | Phase transition artifacts at resolution boundaries | High — days on 8 GPUs |
| StyleGAN | Mapping net + AdaIN style injection + noise + prog grow | 4.40 | Water droplet artifacts (AdaIN statistics), phase artifacts | Very high — weeks on 8 GPUs |
| StyleGAN2 | Weight demodulation, no progressive grow, path length reg, R1 | 2.84 | Significantly reduced — no droplets, no phase artifacts | Very high — weeks on 8 GPUs |

- The mapping network uses lr_mul=0.01 — the learning rate multiplier scales weights down at init and gradients up during optimisation, stabilising the MLP training.
- Each resolution block in the synthesis network has its own affine layer A(w), giving 18 independent style vectors at 1024px resolution (2 per resolution from 4px to 1024px).
- Stochastic noise amplitude B is initialised to zero, so noise has no effect at training start — it is learned gradually as the generator refines fine details.
- Style mixing regularisation: during training, some samples use two different w vectors (coarse/fine split at a random layer) to prevent cross-layer dependencies.
- StyleGAN2 weight demodulation is implemented as a fused layer that combines modulation, convolution, and demodulation in a single efficient CUDA kernel.
- PPL (Perceptual Path Length) measures W-space disentanglement: lower PPL means traversals between w vectors produce smoother, more predictable image changes.

---

