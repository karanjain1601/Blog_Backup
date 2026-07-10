---
title: "MoCo — Momentum Contrast and Dynamic Queue"
slug: "moco-momentum-contrast"
description: "MoCo (He et al. 2020) achieves contrastive self-supervised learning without large batch sizes by maintaining a queue of consistent negative keys updated via an exponential moving average momentum encoder, decoupling the number of negatives from GPU memory."
tags: ["deep-learning", "self-supervised-learning", "contrastive-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9DbyAoTW9tZW50dW0gQ29udHJhc3QsIEhlIGV0IGFsLiAyMDIwKSBhZGRyZXNzZXMgdGhlIGZ1bmRhbWVudGFsIGJvdHRsZW5lY2sgb2YgU2ltQ0xSOiB0aGUgcmVxdWlyZW1lbnQgZm9yIGVub3Jtb3VzIGJhdGNoIHNpemVzIHRvIGhhdmUgZW5vdWdoIG5lZ2F0aXZlcy4gTW9DbyBkZWNvdXBsZXMgdGhlIG51bWJlciBvZiBuZWdhdGl2ZXMgZnJvbSB0aGUgYmF0Y2ggc2l6ZSBieSBtYWludGFpbmluZyBhIGR5bmFtaWMgcXVldWUgb2YgZW5jb2RlZCBrZXlzIGZyb20gcGFzdCBtaW5pLWJhdGNoZXMuIEEgbW9tZW50dW0gZW5jb2RlciAodXBkYXRlZCBieSBFTUEsIG5vdCBncmFkaWVudCkgZW5zdXJlcyB0aGUga2V5cyBpbiB0aGUgcXVldWUgcmVtYWluIGNvbnNpc3RlbnQgZXZlbiBhcyB0aGUgbW9kZWwgZXZvbHZlcyBkdXJpbmcgdHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW90aXZhdGlvbiDigJQgVGhlIERpY3Rpb25hcnkgUGVyc3BlY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnRyYXN0aXZlIGxlYXJuaW5nIGNhbiBiZSB2aWV3ZWQgYXMgdHJhaW5pbmcgYSBkeW5hbWljIGRpY3Rpb25hcnkgbG9vay11cC4gRWFjaCBlbmNvZGVkIHF1ZXJ5IHEgbXVzdCBtYXRjaCBpdHMgcG9zaXRpdmUga2V5IGvigoogKGZyb20gdGhlIHNhbWUgaW1hZ2UsIGRpZmZlcmVudCBhdWdtZW50YXRpb24pIGFuZCBiZSBkaXNzaW1pbGFyIGZyb20gYWxsIG5lZ2F0aXZlIGtleXMgSyA9IHtr4oKBLCBr4oKCLCDigKYsIGtLfS4gVG8gbWFrZSB0aGUgbG9zcyBpbmZvcm1hdGl2ZSwgSyBtdXN0IGJlIGxhcmdlICh0ZW5zIG9mIHRob3VzYW5kcykuIEJ1dCBjb21wdXRpbmcgZ3JhZGllbnRzIHRocm91Z2ggSyBlbmNvZGluZ3MgcGVyIHN0ZXAgaXMgcHJvaGliaXRpdmVseSBleHBlbnNpdmUuIE1vQ28gc3RvcmVzIGtleXMgaW4gYSBGSUZPIHF1ZXVlIGFuZCBvbmx5IGVuY29kZXMgdGhlIGN1cnJlbnQgbWluaS1iYXRjaFx1MDAyN3Mga2V5cyB3aXRoIGdyYWRpZW50OyBvbGQga2V5cyBpbiB0aGUgcXVldWUgYXJlIHJldXNlZCB3aXRob3V0IHJlLWVuY29kaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vbWVudHVtIEVuY29kZXIg4oCUIEVNQSBVcGRhdGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrZXkgZW5jb2RlciDOuF9rIGlzIG5vdCB1cGRhdGVkIGJ5IGdyYWRpZW50LiBJbnN0ZWFkIGl0IHRyYWNrcyB0aGUgcXVlcnkgZW5jb2RlciDOuF9xIHZpYSBleHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZTogzrhfayDihpAgbcK3zrhfayArICgxLW0pwrfOuF9xIHdoZXJlIG0gPSAwLjk5OSAodmVyeSBzbG93IHVwZGF0ZSkuIFRoaXMgZW5zdXJlcyB0aGF0IHRoZSBrZXlzIGVucXVldWVkIG92ZXIgdGhlIHBhc3QgZmV3IHRob3VzYW5kIHN0ZXBzIHdlcmUgcHJvZHVjZWQgYnkgYW4gZW5jb2RlciB0aGF0IGNoYW5nZWQgdmVyeSBzbG93bHksIHNvIHRoZXkgYXJlIG11dHVhbGx5IGNvbnNpc3RlbnQuIElmIHRoZSBrZXkgZW5jb2RlciB3ZXJlIHVwZGF0ZWQgcmFwaWRseSBieSBncmFkaWVudCwgb2xkZXIgcXVldWUgZW50cmllcyB3b3VsZCBiZSBlbmNvZGVkIGJ5IGEgdmVyeSBkaWZmZXJlbnQgbW9kZWwsIG1ha2luZyB0aGUgbmVnYXRpdmVzIGluY29uc2lzdGVudCBhbmQgZGVncmFkaW5nIHRoZSBsb3NzIHNpZ25hbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBjb3B5XG5cbmRlZiBidWlsZF9tb21lbnR1bV9lbmNvZGVyKHF1ZXJ5X2VuY29kZXIsIG1vbWVudHVtPTAuOTk5KTpcbiAgICBcIlwiXCJDcmVhdGUga2V5IGVuY29kZXIgYXMgRU1BIGNvcHkgb2YgcXVlcnkgZW5jb2Rlci5cIlwiXCJcbiAgICBrZXlfZW5jb2RlciA9IGNvcHkuZGVlcGNvcHkocXVlcnlfZW5jb2RlcilcbiAgICAjIEtleSBlbmNvZGVyIG5vdCB1cGRhdGVkIGJ5IGdyYWRpZW50XG4gICAgZm9yIHAgaW4ga2V5X2VuY29kZXIucGFyYW1ldGVycygpOlxuICAgICAgICBwLnJlcXVpcmVzX2dyYWRfKEZhbHNlKVxuICAgIHJldHVybiBrZXlfZW5jb2RlclxuXG5AdG9yY2gubm9fZ3JhZCgpXG5kZWYgbW9tZW50dW1fdXBkYXRlKHF1ZXJ5X2VuY29kZXIsIGtleV9lbmNvZGVyLCBtb21lbnR1bT0wLjk5OSk6XG4gICAgXCJcIlwiRU1BIHVwZGF0ZTogzrhfayA9IG0gKiDOuF9rICsgKDEtbSkgKiDOuF9xXCJcIlwiXG4gICAgZm9yIHFfcGFyYW0sIGtfcGFyYW0gaW4gemlwKHF1ZXJ5X2VuY29kZXIucGFyYW1ldGVycygpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBrZXlfZW5jb2Rlci5wYXJhbWV0ZXJzKCkpOlxuICAgICAgICBrX3BhcmFtLmRhdGEgPSBtb21lbnR1bSAqIGtfcGFyYW0uZGF0YSArICgxLjAgLSBtb21lbnR1bSkgKiBxX3BhcmFtLmRhdGFcblxuIyBEZW1vOiBzaG93IHNsb3cgZHJpZnQgb2Yga2V5IGVuY29kZXJcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxudG9yY2gubWFudWFsX3NlZWQoMClcbnFfZW5jID0gbm4uTGluZWFyKDY0LCA2NClcbmtfZW5jID0gYnVpbGRfbW9tZW50dW1fZW5jb2RlcihxX2VuYylcblxuIyBTaW11bGF0ZSBvbmUgZ3JhZGllbnQgc3RlcCBvbiBxdWVyeSBlbmNvZGVyXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5TR0QocV9lbmMucGFyYW1ldGVycygpLCBscj0wLjEpXG5sb3NzID0gcV9lbmModG9yY2gucmFuZG4oOCwgNjQpKS5tZWFuKClcbmxvc3MuYmFja3dhcmQoKVxub3B0aW1pemVyLnN0ZXAoKVxuXG4jIEVNQSB1cGRhdGVcbm1vbWVudHVtX3VwZGF0ZShxX2VuYywga19lbmMsIG1vbWVudHVtPTAuOTk5KVxuXG4jIE1lYXN1cmUgZHJpZnRcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIGRpZmYgPSBzdW0oKHFwIC0ga3ApLm5vcm0oKS5pdGVtKClcbiAgICAgICAgICAgICAgIGZvciBxcCwga3AgaW4gemlwKHFfZW5jLnBhcmFtZXRlcnMoKSwga19lbmMucGFyYW1ldGVycygpKSlcbnByaW50KGZcdTAwMjdQYXJhbWV0ZXIgZHJpZnQgYWZ0ZXIgMSBzdGVwIChtb21lbnR1bT0wLjk5OSk6IHtkaWZmOi42Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFF1ZXVlIE1hbmFnZW1lbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBxdWV1ZSBzdG9yZXMgSyBlbmNvZGVkIGtleXMgKEsgPSA2NTUzNiBieSBkZWZhdWx0KS4gQWZ0ZXIgZWFjaCBtaW5pLWJhdGNoIG9mIHNpemUgTiwgTiBuZXcga2V5cyBhcmUgZW5xdWV1ZWQgYW5kIHRoZSBvbGRlc3QgTiBrZXlzIGFyZSBkZXF1ZXVlZCAoRklGTykuIEltcG9ydGFudGx5LCBrZXlzIGFyZSBlbnF1ZXVlZCBhcy1pcyBmcm9tIHRoZSBrZXkgZW5jb2RlciBvdXRwdXQ7IHRoZXkgYXJlIG5vdCBiYWNrcHJvcGFnYXRlZCB0aHJvdWdoLiBUaGUgcXVldWUgaXMgc3RvcmVkIG9uIEdQVSBhcyBhIGZpeGVkLXNpemUgYnVmZmVyLiBCZWNhdXNlIHF1ZXVlIGtleXMgY29tZSBmcm9tIG1hbnkgcGFzdCBtaW5pLWJhdGNoZXMgKHdpdGggdGhlIHNsb3dseS1kcmlmdGluZyBrZXkgZW5jb2RlciksIHRoZXkgYXJlIGRpdmVyc2UgYW5kIGNvbnNpc3RlbnQg4oCUIHVubGlrZSBTaW1DTFJcdTAwMjdzIGluLWJhdGNoIG5lZ2F0aXZlcywgd2hpY2ggdmFyeSBtaW5pLWJhdGNoIHRvIG1pbmktYmF0Y2guIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBNb0NvUXVldWU6XG4gICAgXCJcIlwiRklGTyBxdWV1ZSBvZiBlbmNvZGVkIGtleXMgZm9yIE1vQ28uXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGZlYXRfZGltPTEyOCwgcXVldWVfc2l6ZT02NTUzNiwgZGV2aWNlPVx1MDAyN2N1ZGFcdTAwMjcpOlxuICAgICAgICBzZWxmLnF1ZXVlX3NpemUgPSBxdWV1ZV9zaXplXG4gICAgICAgICMgSW5pdGlhbGlzZSB3aXRoIHJhbmRvbSB1bml0IHZlY3RvcnNcbiAgICAgICAgc2VsZi5xdWV1ZSA9IEYubm9ybWFsaXplKFxuICAgICAgICAgICAgdG9yY2gucmFuZG4oZmVhdF9kaW0sIHF1ZXVlX3NpemUsIGRldmljZT1kZXZpY2UpLCBkaW09MFxuICAgICAgICApXG4gICAgICAgIHNlbGYucHRyID0gMCAgIyBwb2ludGVyIHRvIGN1cnJlbnQgd3JpdGUgcG9zaXRpb25cblxuICAgIEB0b3JjaC5ub19ncmFkKClcbiAgICBkZWYgZW5xdWV1ZV9kZXF1ZXVlKHNlbGYsIGtleXMpOlxuICAgICAgICBcIlwiXCJFbnF1ZXVlIG5ldyBrZXlzIGFuZCBkZXF1ZXVlIG9sZGVzdC4ga2V5czogKE4sIEQpIG5vcm1hbGlzZWQuXCJcIlwiXG4gICAgICAgIE4gPSBrZXlzLnNpemUoMClcbiAgICAgICAgYXNzZXJ0IHNlbGYucXVldWVfc2l6ZSAlIE4gPT0gMCwgXHUwMDI3cXVldWVfc2l6ZSBtdXN0IGJlIGRpdmlzaWJsZSBieSBiYXRjaCBzaXplXHUwMDI3XG4gICAgICAgICMgV3JpdGUgbmV3IGtleXMgYXQgY3VycmVudCBwb2ludGVyIHBvc2l0aW9uXG4gICAgICAgIHNlbGYucXVldWVbOiwgc2VsZi5wdHI6c2VsZi5wdHIgKyBOXSA9IGtleXMuVCAgIyAoRCwgTilcbiAgICAgICAgc2VsZi5wdHIgPSAoc2VsZi5wdHIgKyBOKSAlIHNlbGYucXVldWVfc2l6ZVxuXG4gICAgZGVmIGdldF9rZXlzKHNlbGYpOlxuICAgICAgICBcIlwiXCJSZXR1cm4gYWxsIGtleXMgaW4gcXVldWUgYXMgKEQsIEspIHRlbnNvci5cIlwiXCJcbiAgICAgICAgcmV0dXJuIHNlbGYucXVldWUuY2xvbmUoKS5kZXRhY2goKVxuXG4jIERlbW9cbnF1ZXVlID0gTW9Db1F1ZXVlKGZlYXRfZGltPTEyOCwgcXVldWVfc2l6ZT00MDk2LCBkZXZpY2U9XHUwMDI3Y3B1XHUwMDI3KVxucHJpbnQoXHUwMDI3UXVldWUgc2hhcGU6XHUwMDI3LCBxdWV1ZS5nZXRfa2V5cygpLnNoYXBlKVxuYmF0Y2hfa2V5cyA9IEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKDY0LCAxMjgpLCBkaW09MSlcbnF1ZXVlLmVucXVldWVfZGVxdWV1ZShiYXRjaF9rZXlzKVxucHJpbnQoXHUwMDI3QWZ0ZXIgZW5xdWV1ZSAocHRyIHNob3VsZCBiZSA2NCk6XHUwMDI3LCBxdWV1ZS5wdHIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9DbyBUcmFpbmluZyBMb29wIGFuZCBJbmZvTkNFIExvc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBJbmZvTkNFIGxvc3MgZm9yIE1vQ286IEwgPSAtbG9nWyBleHAoccK3a+KCii/PhCkgLyAoZXhwKHHCt2vigoovz4QpICsgzqPhtaIgZXhwKHHCt2vhtaIvz4QpKSBdIHdoZXJlIHEgaXMgdGhlIHF1ZXJ5IGVtYmVkZGluZyAoZnJvbSB0aGUgcXVlcnkgZW5jb2RlciB3aXRoIGdyYWRpZW50KSwga+KCiiBpcyB0aGUgcG9zaXRpdmUga2V5IChmcm9tIHRoZSBrZXkgZW5jb2Rlciwgbm8gZ3JhZGllbnQpLCBhbmQge2vhtaJ9IGFyZSB0aGUgbmVnYXRpdmUga2V5cyBmcm9tIHRoZSBxdWV1ZS4gVGhlIGxvc3MgcmVkdWNlcyB0byBhIEsrMS13YXkgc29mdG1heCBjbGFzc2lmaWNhdGlvbiB3aGVyZSB0aGUgcG9zaXRpdmUgcGFpciBpcyB0aGUgY29ycmVjdCBjbGFzcy4gVGhlIHF1ZXJ5IGVuY29kZXIgaXMgdXBkYXRlZCBieSBncmFkaWVudDsgdGhlIGtleSBlbmNvZGVyIGlzIHVwZGF0ZWQgYnkgRU1BIGFmdGVyIGVhY2ggc3RlcDsgdGhlIHBvc2l0aXZlIGtleSBpcyBlbnF1ZXVlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCB0b3JjaHZpc2lvbi5tb2RlbHMgYXMgbW9kZWxzXG5pbXBvcnQgY29weVxuXG5jbGFzcyBNb0NvKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGJhc2VfZW5jb2RlciwgZmVhdF9kaW09MTI4LCBxdWV1ZV9zaXplPTY1NTM2LFxuICAgICAgICAgICAgICAgICBtb21lbnR1bT0wLjk5OSwgdGVtcGVyYXR1cmU9MC4wNyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm0gPSBtb21lbnR1bVxuICAgICAgICBzZWxmLlQgPSB0ZW1wZXJhdHVyZVxuICAgICAgICAjIFF1ZXJ5IGVuY29kZXJcbiAgICAgICAgc2VsZi5lbmNvZGVyX3EgPSBiYXNlX2VuY29kZXIod2VpZ2h0cz1Ob25lKVxuICAgICAgICBzZWxmLmVuY29kZXJfcS5mYyA9IG5uLkxpbmVhcihzZWxmLmVuY29kZXJfcS5mYy5pbl9mZWF0dXJlcywgZmVhdF9kaW0pXG4gICAgICAgICMgS2V5IGVuY29kZXIgKEVNQSBjb3B5KVxuICAgICAgICBzZWxmLmVuY29kZXJfayA9IGNvcHkuZGVlcGNvcHkoc2VsZi5lbmNvZGVyX3EpXG4gICAgICAgIGZvciBwIGluIHNlbGYuZW5jb2Rlcl9rLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgICAgIHAucmVxdWlyZXNfZ3JhZF8oRmFsc2UpXG4gICAgICAgICMgUXVldWVcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3cXVldWVcdTAwMjcsXG4gICAgICAgICAgICBGLm5vcm1hbGl6ZSh0b3JjaC5yYW5kbihmZWF0X2RpbSwgcXVldWVfc2l6ZSksIGRpbT0wKSlcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3cXVldWVfcHRyXHUwMDI3LCB0b3JjaC56ZXJvcygxLCBkdHlwZT10b3JjaC5sb25nKSlcbiAgICAgICAgc2VsZi5xdWV1ZV9zaXplID0gcXVldWVfc2l6ZVxuXG4gICAgQHRvcmNoLm5vX2dyYWQoKVxuICAgIGRlZiBfbW9tZW50dW1fdXBkYXRlKHNlbGYpOlxuICAgICAgICBmb3IgcSwgayBpbiB6aXAoc2VsZi5lbmNvZGVyX3EucGFyYW1ldGVycygpLCBzZWxmLmVuY29kZXJfay5wYXJhbWV0ZXJzKCkpOlxuICAgICAgICAgICAgay5kYXRhID0gc2VsZi5tICogay5kYXRhICsgKDEgLSBzZWxmLm0pICogcS5kYXRhXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIF9kZXF1ZXVlX2VucXVldWUoc2VsZiwga2V5cyk6XG4gICAgICAgIE4gPSBrZXlzLnNpemUoMClcbiAgICAgICAgcHRyID0gaW50KHNlbGYucXVldWVfcHRyKVxuICAgICAgICBzZWxmLnF1ZXVlWzosIHB0cjpwdHIgKyBOXSA9IGtleXMuVFxuICAgICAgICBzZWxmLnF1ZXVlX3B0clswXSA9IChwdHIgKyBOKSAlIHNlbGYucXVldWVfc2l6ZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeF9xLCB4X2spOlxuICAgICAgICBxID0gRi5ub3JtYWxpemUoc2VsZi5lbmNvZGVyX3EoeF9xKSwgZGltPTEpICAgICAgICAjIChOLCBDKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIHNlbGYuX21vbWVudHVtX3VwZGF0ZSgpXG4gICAgICAgICAgICBrID0gRi5ub3JtYWxpemUoc2VsZi5lbmNvZGVyX2soeF9rKSwgZGltPTEpICAgICMgKE4sIEMpXG4gICAgICAgIGxfcG9zID0gKHEgKiBrKS5zdW0oZGltPTEsIGtlZXBkaW09VHJ1ZSkgLyBzZWxmLlQgICMgKE4sIDEpXG4gICAgICAgIGxfbmVnID0gKHEgQCBzZWxmLnF1ZXVlLmNsb25lKCkpIC8gc2VsZi5UICAgICAgICAgICAjIChOLCBLKVxuICAgICAgICBsb2dpdHMgPSB0b3JjaC5jYXQoW2xfcG9zLCBsX25lZ10sIGRpbT0xKSAgICAgICAgICAgIyAoTiwgMStLKVxuICAgICAgICBsYWJlbHMgPSB0b3JjaC56ZXJvcyhsb2dpdHMuc2l6ZSgwKSwgZHR5cGU9dG9yY2gubG9uZywgZGV2aWNlPXEuZGV2aWNlKVxuICAgICAgICBzZWxmLl9kZXF1ZXVlX2VucXVldWUoaylcbiAgICAgICAgcmV0dXJuIEYuY3Jvc3NfZW50cm9weShsb2dpdHMsIGxhYmVscylcblxucHJpbnQoXHUwMDI3TW9DbyBtb2RlbCBkZWZpbmVkLiBQb3NpdGl2ZSBpcyBjbGFzcyAwIGluICgxK0spLXdheSBzb2Z0bWF4Llx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb0NvIHYyIEltcHJvdmVtZW50cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9DbyB2MiAoQ2hlbiBldCBhbC4gMjAyMCkgaXMgYSBzaW1wbGUgYnV0IGltcGFjdGZ1bCB1cGRhdGU6ICgxKSByZXBsYWNlIHRoZSBsaW5lYXIgcHJvamVjdGlvbiBoZWFkIHdpdGggYSAyLWxheWVyIE1MUCAobGlrZSBTaW1DTFIpLCBhbmQgKDIpIGFkb3B0IHN0cm9uZ2VyIGF1Z21lbnRhdGlvbiAoR2F1c3NpYW4gYmx1ciArIHN0cm9uZ2VyIGNvbG9yIGppdHRlcikuIFRoZXNlIHR3byBjaGFuZ2VzLCB3aXRob3V0IGFueSBvdGhlciBtb2RpZmljYXRpb24gdG8gdGhlIHF1ZXVlIG9yIG1vbWVudHVtIG1lY2hhbmlzbSwgYnJvdWdodCBNb0NvIHdpdGhpbiB+MSUgb2YgU2ltQ0xSIHYxIHVzaW5nIGEgYmF0Y2ggc2l6ZSBvZiBqdXN0IDI1NiDigJQgMTbDlyBzbWFsbGVyLiBUaGlzIGRlbW9uc3RyYXRlZCB0aGF0IHRoZSBNb0NvIGZyYW1ld29yayB3YXMgbm90IHRoZSBib3R0bGVuZWNrOyB0aGUgbWlzc2luZyBpbmdyZWRpZW50cyB3ZXJlIHRoZSBNTFAgaGVhZCBhbmQgYXVnbWVudGF0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNodmlzaW9uLm1vZGVscyBhcyBtb2RlbHNcbmZyb20gdG9yY2h2aXNpb24gaW1wb3J0IHRyYW5zZm9ybXNcblxuZGVmIGJ1aWxkX21vY29fdjJfZW5jb2RlcihmZWF0X2RpbT0xMjgpOlxuICAgIFwiXCJcIlJlc05ldC01MCB3aXRoIDItbGF5ZXIgTUxQIHByb2plY3Rpb24gaGVhZCAoTW9DbyB2MikuXCJcIlwiXG4gICAgYmFzZSA9IG1vZGVscy5yZXNuZXQ1MCh3ZWlnaHRzPU5vbmUpXG4gICAgaGlkZGVuX2RpbSA9IGJhc2UuZmMuaW5fZmVhdHVyZXMgICMgMjA0OFxuICAgIGJhc2UuZmMgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICBubi5MaW5lYXIoaGlkZGVuX2RpbSwgaGlkZGVuX2RpbSksXG4gICAgICAgIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgbm4uTGluZWFyKGhpZGRlbl9kaW0sIGZlYXRfZGltKSxcbiAgICApXG4gICAgcmV0dXJuIGJhc2VcblxuZGVmIG1vY29fdjJfYXVnbWVudGF0aW9uKGltYWdlX3NpemU9MjI0KTpcbiAgICBcIlwiXCJTdHJvbmdlciBhdWdtZW50YXRpb24gbWF0Y2hpbmcgU2ltQ0xSIChNb0NvIHYyKS5cIlwiXCJcbiAgICByZXR1cm4gdHJhbnNmb3Jtcy5Db21wb3NlKFtcbiAgICAgICAgdHJhbnNmb3Jtcy5SYW5kb21SZXNpemVkQ3JvcChpbWFnZV9zaXplLCBzY2FsZT0oMC4yLCAxLjApKSxcbiAgICAgICAgdHJhbnNmb3Jtcy5SYW5kb21BcHBseShbXG4gICAgICAgICAgICB0cmFuc2Zvcm1zLkNvbG9ySml0dGVyKDAuNCwgMC40LCAwLjQsIDAuMSlcbiAgICAgICAgXSwgcD0wLjgpLFxuICAgICAgICB0cmFuc2Zvcm1zLlJhbmRvbUdyYXlzY2FsZShwPTAuMiksXG4gICAgICAgIHRyYW5zZm9ybXMuUmFuZG9tQXBwbHkoW1xuICAgICAgICAgICAgdHJhbnNmb3Jtcy5HYXVzc2lhbkJsdXIoa2VybmVsX3NpemU9MjMpXG4gICAgICAgIF0sIHA9MC41KSxcbiAgICAgICAgdHJhbnNmb3Jtcy5SYW5kb21Ib3Jpem9udGFsRmxpcCgpLFxuICAgICAgICB0cmFuc2Zvcm1zLlRvVGVuc29yKCksXG4gICAgICAgIHRyYW5zZm9ybXMuTm9ybWFsaXplKFswLjQ4NSwgMC40NTYsIDAuNDA2XSwgWzAuMjI5LCAwLjIyNCwgMC4yMjVdKSxcbiAgICBdKVxuXG5lbmMgPSBidWlsZF9tb2NvX3YyX2VuY29kZXIoKVxucGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBlbmMucGFyYW1ldGVycygpKSAvLyAxXzAwMF8wMDBcbnByaW50KGZcdTAwMjdNb0NvIHYyIGVuY29kZXIgcGFyYW1ldGVyczoge3BhcmFtc31NXHUwMDI3KVxucHJpbnQoXHUwMDI3S2V5IGNoYW5nZTogTUxQIGhlYWQgKyBHYXVzc2lhbiBibHVyIGF1Z21lbnRhdGlvbi5cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJXaHkgTW9tZW50dW0gPSAwLjk5OSBJcyBDcml0aWNhbCIsImNvbnRlbnQiOiJJZiBtb21lbnR1bSBpcyB0b28gbG93IChlLmcuIDAuOSksIHRoZSBrZXkgZW5jb2RlciB1cGRhdGVzIHJhcGlkbHkgYW5kIG9sZGVyIHF1ZXVlIGVudHJpZXMgYXJlIGVuY29kZWQgYnkgYSB2ZXJ5IGRpZmZlcmVudCBtb2RlbCwgbWFraW5nIHRoZSBuZWdhdGl2ZXMgaW5jb25zaXN0ZW50IOKAlCB0aGUgbG9zcyBiZWNvbWVzIG5vaXN5LiBJZiBtb21lbnR1bSBpcyB0b28gaGlnaCAoY2xvc2UgdG8gMSksIHRoZSBrZXkgZW5jb2RlciBiYXJlbHkgbGVhcm5zIGZyb20gdGhlIHF1ZXJ5IGVuY29kZXIsIGFuZCBjb252ZXJnZW5jZSBzbG93cy4gRW1waXJpY2FsbHkgbSA9IDAuOTk5IHByb3ZpZGVzIHRoZSBiZXN0IGJhbGFuY2UgYmV0d2VlbiBrZXkgY29uc2lzdGVuY3kgYW5kIGxlYXJuaW5nIHNpZ25hbC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb0NvIHYzIGFuZCBWaXNpb24gVHJhbnNmb3JtZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb0NvIHYzIChDaGVuIGV0IGFsLiAyMDIxKSBhZGFwdHMgdGhlIGZyYW1ld29yayB0byBWaXNpb24gVHJhbnNmb3JtZXJzIChWaVQpLiBUaGUgcXVldWUgaXMgYWJhbmRvbmVkOiB3aXRoIFZpVC1CIGFuZCBhIGJhdGNoIHNpemUgb2YgNDA5Niwgc3VmZmljaWVudCBuZWdhdGl2ZXMgZXhpc3QgaW4tYmF0Y2ggKGxpa2UgU2ltQ0xSKS4gQSBzdG9wLWdyYWRpZW50IGlzIGFkZGVkIG9uIHRoZSBrZXkgcGF0aCAoc2ltaWxhciB0byBCWU9MKS4gVGhlIHByb2plY3Rpb24gaGVhZCBiZWNvbWVzIGEgMy1sYXllciBNTFAuIE1vQ28gdjMgd2l0aCBWaVQtQi8xNiBhY2hpZXZlcyA4My4yJSB0b3AtMSBvbiBJbWFnZU5ldCBsaW5lYXIgZXZhbCDigJQgc3VycGFzc2luZyBzdXBlcnZpc2VkIFJlc05ldC01MCAoNzYuMSUpIHdpdGhvdXQgYW55IGxhYmVscy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbInYxOiBSZXNOZXQgKyBxdWV1ZSg2NTUzNikgKyBtb21lbnR1bSBlbmNvZGVyICsgbGluZWFyIHByb2plY3Rpb24gKyBJbmZvTkNFLiIsInYyOiB2MSArIE1MUCBwcm9qZWN0aW9uIGhlYWQgKyBzdHJvbmdlciBhdWdtZW50YXRpb24g4oCUIG1hdGNoZXMgU2ltQ0xSIGF0IDI1NiBiYXRjaC4iLCJ2MzogVmlUIGJhY2tib25lICsgbm8gcXVldWUgKyBzdG9wLWdyYWRpZW50IG9uIGtleSBwYXRoICsgMy1sYXllciBNTFAgaGVhZC4iLCJNb21lbnR1bSBtID0gMC45OTkgKHYxL3YyKSwgbSA9IDAuOTkgKHYzIHdpdGggVmlUIOKAlCBmYXN0ZXIgZHJpZnQgYWNjZXB0YWJsZSkuIiwidjMgdHJhaW5pbmcgdHJpY2s6IGZyZWV6ZSBwYXRjaCBwcm9qZWN0aW9uIGxheWVyIGZvciBmaXJzdCBmZXcgZXBvY2hzIHRvIHN0YWJpbGlzZSBWaVQuIl19LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJWZXJzaW9uIiwiUXVldWUiLCJCYXRjaCBTaXplIiwiQmFja2JvbmUiLCJBdWdtZW50YXRpb24iLCJMaW5lYXIgRXZhbCBUb3AtMSJdLCJyb3dzIjpbWyJNb0NvIHYxIiwiNjUgNTM2IiwiMjU2IiwiUmVzTmV0LTUwIiwiU3RhbmRhcmQiLCI2MC42JSJdLFsiTW9DbyB2MiIsIjY1IDUzNiIsIjI1NiIsIlJlc05ldC01MCIsIlNpbUNMUi1zdHlsZSIsIjcxLjElIl0sWyJNb0NvIHYzIiwiTm9uZSIsIjQwOTYiLCJWaVQtQi8xNiIsIlNpbUNMUi1zdHlsZSIsIjgzLjIlIl0sWyJTaW1DTFIgdjEgKHJlZikiLCJOb25lIiwiNDA5NiIsIlJlc05ldC01MCIsIlNpbUNMUi1zdHlsZSIsIjY5LjMlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXN1bHRzIGFuZCBEb3duc3RyZWFtIEV2YWx1YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vQ28gdjEgYWNoaWV2ZXMgNjAuNiUgdG9wLTEgbGluZWFyIGV2YWx1YXRpb24gb24gSW1hZ2VOZXQgd2l0aCBSZXNOZXQtNTAg4oCUIHNpZ25pZmljYW50bHkgYmVsb3cgc3VwZXJ2aXNlZCAoNzYuMSUpIGJ1dCB3aXRoIHplcm8gbGFiZWxzLiBNb0NvIHYyIGNsb3NlcyB0aGUgZ2FwIHRvIDcxLjElIHB1cmVseSBieSBhZGRpbmcgTUxQIGhlYWQgYW5kIGF1Z21lbnRhdGlvbi4gRm9yIHNlbWktc3VwZXJ2aXNlZCBhbmQgZmluZS10dW5pbmcgdGFza3MsIE1vQ28gcmVwcmVzZW50YXRpb25zIHRyYW5zZmVyIHdlbGw6IG9uIFBBU0NBTCBWT0MgZGV0ZWN0aW9uLCBNb0NvIHByZS10cmFpbmluZyBtYXRjaGVzIHN1cGVydmlzZWQgcHJlLXRyYWluaW5nIHdpdGhpbiAwLjUgQVAuIFRoaXMgZGVtb25zdHJhdGVzIHRoYXQgcXVldWUtYmFzZWQgY29udHJhc3RpdmUgbGVhcm5pbmcgcHJvZHVjZXMgYnJvYWRseSB1c2VmdWwgcmVwcmVzZW50YXRpb25zIHRoYXQgdHJhbnNmZXIgYWNyb3NzIHRhc2tzIGFuZCBkb21haW5zIHdpdGhvdXQgcmVxdWlyaW5nIHRoZSBtYXNzaXZlIGJhdGNoIHNpemVzIG9mIFNpbUNMUi4ifV0="
---
# MoCo — Momentum Contrast and Dynamic Queue

MoCo (Momentum Contrast, He et al. 2020) addresses the fundamental bottleneck of SimCLR: the requirement for enormous batch sizes to have enough negatives. MoCo decouples the number of negatives from the batch size by maintaining a dynamic queue of encoded keys from past mini-batches. A momentum encoder (updated by EMA, not gradient) ensures the keys in the queue remain consistent even as the model evolves during training.

## Motivation — The Dictionary Perspective

Contrastive learning can be viewed as training a dynamic dictionary look-up. Each encoded query q must match its positive key k₊ (from the same image, different augmentation) and be dissimilar from all negative keys K = {k₁, k₂, …, kK}. To make the loss informative, K must be large (tens of thousands). But computing gradients through K encodings per step is prohibitively expensive. MoCo stores keys in a FIFO queue and only encodes the current mini-batch's keys with gradient; old keys in the queue are reused without re-encoding.

## Momentum Encoder — EMA Update

The key encoder θ_k is not updated by gradient. Instead it tracks the query encoder θ_q via exponential moving average: θ_k ← m·θ_k + (1-m)·θ_q where m = 0.999 (very slow update). This ensures that the keys enqueued over the past few thousand steps were produced by an encoder that changed very slowly, so they are mutually consistent. If the key encoder were updated rapidly by gradient, older queue entries would be encoded by a very different model, making the negatives inconsistent and degrading the loss signal.

```python
import torch
import torch.nn as nn
import copy

def build_momentum_encoder(query_encoder, momentum=0.999):
    """Create key encoder as EMA copy of query encoder."""
    key_encoder = copy.deepcopy(query_encoder)
    # Key encoder not updated by gradient
    for p in key_encoder.parameters():
        p.requires_grad_(False)
    return key_encoder

@torch.no_grad()
def momentum_update(query_encoder, key_encoder, momentum=0.999):
    """EMA update: θ_k = m * θ_k + (1-m) * θ_q"""
    for q_param, k_param in zip(query_encoder.parameters(),
                                key_encoder.parameters()):
        k_param.data = momentum * k_param.data + (1.0 - momentum) * q_param.data

# Demo: show slow drift of key encoder
import torch.nn.functional as F

torch.manual_seed(0)
q_enc = nn.Linear(64, 64)
k_enc = build_momentum_encoder(q_enc)

# Simulate one gradient step on query encoder
optimizer = torch.optim.SGD(q_enc.parameters(), lr=0.1)
loss = q_enc(torch.randn(8, 64)).mean()
loss.backward()
optimizer.step()

# EMA update
momentum_update(q_enc, k_enc, momentum=0.999)

# Measure drift
with torch.no_grad():
    diff = sum((qp - kp).norm().item()
               for qp, kp in zip(q_enc.parameters(), k_enc.parameters()))
print(f'Parameter drift after 1 step (momentum=0.999): {diff:.6f}')
```

## Key Queue Management

The queue stores K encoded keys (K = 65536 by default). After each mini-batch of size N, N new keys are enqueued and the oldest N keys are dequeued (FIFO). Importantly, keys are enqueued as-is from the key encoder output; they are not backpropagated through. The queue is stored on GPU as a fixed-size buffer. Because queue keys come from many past mini-batches (with the slowly-drifting key encoder), they are diverse and consistent — unlike SimCLR's in-batch negatives, which vary mini-batch to mini-batch.

```python
import torch
import torch.nn.functional as F

class MoCoQueue:
    """FIFO queue of encoded keys for MoCo."""
    def __init__(self, feat_dim=128, queue_size=65536, device='cuda'):
        self.queue_size = queue_size
        # Initialise with random unit vectors
        self.queue = F.normalize(
            torch.randn(feat_dim, queue_size, device=device), dim=0
        )
        self.ptr = 0  # pointer to current write position

    @torch.no_grad()
    def enqueue_dequeue(self, keys):
        """Enqueue new keys and dequeue oldest. keys: (N, D) normalised."""
        N = keys.size(0)
        assert self.queue_size % N == 0, 'queue_size must be divisible by batch size'
        # Write new keys at current pointer position
        self.queue[:, self.ptr:self.ptr + N] = keys.T  # (D, N)
        self.ptr = (self.ptr + N) % self.queue_size

    def get_keys(self):
        """Return all keys in queue as (D, K) tensor."""
        return self.queue.clone().detach()

# Demo
queue = MoCoQueue(feat_dim=128, queue_size=4096, device='cpu')
print('Queue shape:', queue.get_keys().shape)
batch_keys = F.normalize(torch.randn(64, 128), dim=1)
queue.enqueue_dequeue(batch_keys)
print('After enqueue (ptr should be 64):', queue.ptr)
```

## MoCo Training Loop and InfoNCE Loss

The InfoNCE loss for MoCo: L = -log[ exp(q·k₊/τ) / (exp(q·k₊/τ) + Σᵢ exp(q·kᵢ/τ)) ] where q is the query embedding (from the query encoder with gradient), k₊ is the positive key (from the key encoder, no gradient), and {kᵢ} are the negative keys from the queue. The loss reduces to a K+1-way softmax classification where the positive pair is the correct class. The query encoder is updated by gradient; the key encoder is updated by EMA after each step; the positive key is enqueued.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import copy

class MoCo(nn.Module):
    def __init__(self, base_encoder, feat_dim=128, queue_size=65536,
                 momentum=0.999, temperature=0.07):
        super().__init__()
        self.m = momentum
        self.T = temperature
        # Query encoder
        self.encoder_q = base_encoder(weights=None)
        self.encoder_q.fc = nn.Linear(self.encoder_q.fc.in_features, feat_dim)
        # Key encoder (EMA copy)
        self.encoder_k = copy.deepcopy(self.encoder_q)
        for p in self.encoder_k.parameters():
            p.requires_grad_(False)
        # Queue
        self.register_buffer('queue',
            F.normalize(torch.randn(feat_dim, queue_size), dim=0))
        self.register_buffer('queue_ptr', torch.zeros(1, dtype=torch.long))
        self.queue_size = queue_size

    @torch.no_grad()
    def _momentum_update(self):
        for q, k in zip(self.encoder_q.parameters(), self.encoder_k.parameters()):
            k.data = self.m * k.data + (1 - self.m) * q.data

    @torch.no_grad()
    def _dequeue_enqueue(self, keys):
        N = keys.size(0)
        ptr = int(self.queue_ptr)
        self.queue[:, ptr:ptr + N] = keys.T
        self.queue_ptr[0] = (ptr + N) % self.queue_size

    def forward(self, x_q, x_k):
        q = F.normalize(self.encoder_q(x_q), dim=1)        # (N, C)
        with torch.no_grad():
            self._momentum_update()
            k = F.normalize(self.encoder_k(x_k), dim=1)    # (N, C)
        l_pos = (q * k).sum(dim=1, keepdim=True) / self.T  # (N, 1)
        l_neg = (q @ self.queue.clone()) / self.T           # (N, K)
        logits = torch.cat([l_pos, l_neg], dim=1)           # (N, 1+K)
        labels = torch.zeros(logits.size(0), dtype=torch.long, device=q.device)
        self._dequeue_enqueue(k)
        return F.cross_entropy(logits, labels)

print('MoCo model defined. Positive is class 0 in (1+K)-way softmax.')
```

## MoCo v2 Improvements

MoCo v2 (Chen et al. 2020) is a simple but impactful update: (1) replace the linear projection head with a 2-layer MLP (like SimCLR), and (2) adopt stronger augmentation (Gaussian blur + stronger color jitter). These two changes, without any other modification to the queue or momentum mechanism, brought MoCo within ~1% of SimCLR v1 using a batch size of just 256 — 16× smaller. This demonstrated that the MoCo framework was not the bottleneck; the missing ingredients were the MLP head and augmentation.

```python
import torch
import torch.nn as nn
import torchvision.models as models
from torchvision import transforms

def build_moco_v2_encoder(feat_dim=128):
    """ResNet-50 with 2-layer MLP projection head (MoCo v2)."""
    base = models.resnet50(weights=None)
    hidden_dim = base.fc.in_features  # 2048
    base.fc = nn.Sequential(
        nn.Linear(hidden_dim, hidden_dim),
        nn.ReLU(inplace=True),
        nn.Linear(hidden_dim, feat_dim),
    )
    return base

def moco_v2_augmentation(image_size=224):
    """Stronger augmentation matching SimCLR (MoCo v2)."""
    return transforms.Compose([
        transforms.RandomResizedCrop(image_size, scale=(0.2, 1.0)),
        transforms.RandomApply([
            transforms.ColorJitter(0.4, 0.4, 0.4, 0.1)
        ], p=0.8),
        transforms.RandomGrayscale(p=0.2),
        transforms.RandomApply([
            transforms.GaussianBlur(kernel_size=23)
        ], p=0.5),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])

enc = build_moco_v2_encoder()
params = sum(p.numel() for p in enc.parameters()) // 1_000_000
print(f'MoCo v2 encoder parameters: {params}M')
print('Key change: MLP head + Gaussian blur augmentation.')
```

> **Why Momentum = 0.999 Is Critical**: If momentum is too low (e.g. 0.9), the key encoder updates rapidly and older queue entries are encoded by a very different model, making the negatives inconsistent — the loss becomes noisy. If momentum is too high (close to 1), the key encoder barely learns from the query encoder, and convergence slows. Empirically m = 0.999 provides the best balance between key consistency and learning signal.

## MoCo v3 and Vision Transformers

MoCo v3 (Chen et al. 2021) adapts the framework to Vision Transformers (ViT). The queue is abandoned: with ViT-B and a batch size of 4096, sufficient negatives exist in-batch (like SimCLR). A stop-gradient is added on the key path (similar to BYOL). The projection head becomes a 3-layer MLP. MoCo v3 with ViT-B/16 achieves 83.2% top-1 on ImageNet linear eval — surpassing supervised ResNet-50 (76.1%) without any labels.

- v1: ResNet + queue(65536) + momentum encoder + linear projection + InfoNCE.
- v2: v1 + MLP projection head + stronger augmentation — matches SimCLR at 256 batch.
- v3: ViT backbone + no queue + stop-gradient on key path + 3-layer MLP head.
- Momentum m = 0.999 (v1/v2), m = 0.99 (v3 with ViT — faster drift acceptable).
- v3 training trick: freeze patch projection layer for first few epochs to stabilise ViT.

| Version | Queue | Batch Size | Backbone | Augmentation | Linear Eval Top-1 |
| --- | --- | --- | --- | --- | --- |
| MoCo v1 | 65 536 | 256 | ResNet-50 | Standard | 60.6% |
| MoCo v2 | 65 536 | 256 | ResNet-50 | SimCLR-style | 71.1% |
| MoCo v3 | None | 4096 | ViT-B/16 | SimCLR-style | 83.2% |
| SimCLR v1 (ref) | None | 4096 | ResNet-50 | SimCLR-style | 69.3% |

## Results and Downstream Evaluation

MoCo v1 achieves 60.6% top-1 linear evaluation on ImageNet with ResNet-50 — significantly below supervised (76.1%) but with zero labels. MoCo v2 closes the gap to 71.1% purely by adding MLP head and augmentation. For semi-supervised and fine-tuning tasks, MoCo representations transfer well: on PASCAL VOC detection, MoCo pre-training matches supervised pre-training within 0.5 AP. This demonstrates that queue-based contrastive learning produces broadly useful representations that transfer across tasks and domains without requiring the massive batch sizes of SimCLR.

