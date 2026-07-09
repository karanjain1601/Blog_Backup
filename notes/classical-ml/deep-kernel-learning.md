---
title: "Deep Kernel Learning — Neural Networks Meet GPs"
slug: "deep-kernel-learning"
description: "How deep kernel learning composes a neural network feature extractor with a GP kernel to handle high-dimensional structured inputs, joint optimisation of NN weights and GP hyperparameters via marginal likelihood, KISS-GP for large-scale DKL, Deep GPs with stacked layers, and uncertainty calibration comparison against BNNs."
tags: ["gaussian-processes", "kernel-methods", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBTdGFuZGFyZCBHUCBLZXJuZWxzIEZhaWwgb24gSGlnaC1EaW1lbnNpb25hbCBEYXRhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBHUCBrZXJuZWxzIHN1Y2ggYXMgUkJGIGFuZCBNYXTDqXJuIG9wZXJhdGUgZGlyZWN0bHkgb24gcmF3IGlucHV0cy4gSW4gbG93IGRpbWVuc2lvbnMgKGQg4omkIDUpIHRoaXMgd29ya3Mgd2VsbDogdGhlIGtlcm5lbCBjYW4gbWVhc3VyZSBtZWFuaW5nZnVsIHNpbWlsYXJpdHkgYmV0d2VlbiBpbnB1dHMgYW5kIHRoZSBjb3ZhcmlhbmNlIHN0cnVjdHVyZSBjYXB0dXJlcyB0aGUgZnVuY3Rpb25cdTAwMjdzIGJlaGF2aW91ci4gSW4gaGlnaCBkaW1lbnNpb25zIChpbWFnZXMsIHRleHQgZW1iZWRkaW5ncywgdGFidWxhciBkYXRhIHdpdGggZCBcdTAwM2UgMjApLCB0aGUgY3Vyc2Ugb2YgZGltZW5zaW9uYWxpdHkgc3RyaWtlczogZXZlcnkgcGFpciBvZiBwb2ludHMgYmVjb21lcyBhcHByb3hpbWF0ZWx5IGVxdWlkaXN0YW50IHVuZGVyIGEgZml4ZWQtYmFuZHdpZHRoIGtlcm5lbCwgc28gdGhlIGtlcm5lbCBtYXRyaXggZGVnZW5lcmF0ZXMgdG8gbmVhci1jb25zdGFudCB2YWx1ZXMgYW5kIGNhcnJpZXMgYWxtb3N0IG5vIGluZm9ybWF0aW9uLiBBZGRpdGlvbmFsbHksIGEgZml4ZWQtZm9ybSBrZXJuZWwgY2Fubm90IGNhcHR1cmUgY29tcGxleCBub24tc3RhdGlvbmFyeSBwYXR0ZXJucyBvciBkb21haW4tc3BlY2lmaWMgc3RydWN0dXJlLiBUaGUgc29sdXRpb24gaXMgdG8gbGVhcm4gYSBmZWF0dXJlIHJlcHJlc2VudGF0aW9uIGJlZm9yZSBhcHBseWluZyB0aGUga2VybmVsLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlZXAgS2VybmVsIExlYXJuaW5nIOKAlCBDb21wb3NpbmcgTmV1cmFsIE5ldHdvcmtzIHdpdGggR1BzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZWVwIEtlcm5lbCBMZWFybmluZyAoREtMLCBXaWxzb24gZXQgYWwuIDIwMTYpIGNvbXBvc2VzIGEgbmV1cmFsIG5ldHdvcmsgz4YoeDsgdykgd2l0aCBhIGJhc2Uga2VybmVsIGtfYmFzZSB0byBkZWZpbmUgYSBuZXcga2VybmVsOiBrKHgsIHhcdTAwMjcpID0ga19iYXNlKM+GKHg7IHcpLCDPhih4XHUwMDI3OyB3KSkuIFRoZSBuZXVyYWwgbmV0d29yayBtYXBzIHJhdyBpbnB1dHMgdG8gYSBsb3ctZGltZW5zaW9uYWwgZmVhdHVyZSBzcGFjZSB3aGVyZSB0aGUgYmFzZSBrZXJuZWwgaXMgYXBwbGllZC4gVGhlIE5OIHdlaWdodHMgdyBhbmQgR1AgaHlwZXJwYXJhbWV0ZXJzIM64IChsZW5ndGgtc2NhbGUsIHNpZ25hbCB2YXJpYW5jZSwgbm9pc2UgdmFyaWFuY2UpIGFyZSBsZWFybmVkIGpvaW50bHkgYnkgbWF4aW1pc2luZyB0aGUgbG9nIG1hcmdpbmFsIGxpa2VsaWhvb2QgbG9nIHAoeSB8IFgsIHcsIM64KS4gVGhpcyBjb21iaW5lcyB0aGUgZmVhdHVyZS1sZWFybmluZyBwb3dlciBvZiBuZXVyYWwgbmV0d29ya3Mgd2l0aCB0aGUgcHJpbmNpcGxlZCB1bmNlcnRhaW50eSBxdWFudGlmaWNhdGlvbiBvZiBHUHMg4oCUIGEgYmVzdC1vZi1ib3RoLXdvcmxkcyBhcHByb2FjaC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbImsoeCx4XHUwMDI3KSA9IGtfYmFzZSjPhih4O3cpLCDPhih4XHUwMDI3O3cpKSDigJQgTk4gbWFwcyBpbnB1dHMgdG8gR1AtY29tcGF0aWJsZSBmZWF0dXJlIHNwYWNlIiwiTk4gd2VpZ2h0cyB3IGFuZCBHUCBoeXBlcnBhcmFtZXRlcnMgzrggam9pbnRseSBvcHRpbWlzZWQgdmlhIG1hcmdpbmFsIGxpa2VsaWhvb2QiLCJGZWF0dXJlIHNwYWNlIGRpbSBpcyBhIGh5cGVycGFyYW1ldGVyOiB0eXBpY2FsbHkgMuKAkzE2IGRpbWVuc2lvbnMgcmVnYXJkbGVzcyBvZiBpbnB1dCBkaW0gZCIsIlVuY2VydGFpbnR5IHF1YW50aWZpY2F0aW9uIGlzIGV4YWN0IEdQIFVRIGFwcGxpZWQgaW4gbGVhcm5lZCBmZWF0dXJlIHNwYWNlIiwiV29ya3Mgd2VsbCBmb3I6IGltYWdlcyAoQ05OIGV4dHJhY3RvciksIHN0cnVjdHVyZWQgdGFidWxhciBkYXRhIChNTFApLCBzZXF1ZW5jZXMgKExTVE0pIiwiTGltaXRhdGlvbjogdGhlIEdQIGtlcm5lbCBtYXRyaXggaXMgc3RpbGwgbsOXbiDigJQgY29tYmluZSB3aXRoIHNwYXJzZSBHUCAoS0lTUy1HUCkgZm9yIGxhcmdlIG4iXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgZ3B5dG9yY2hcblxuY2xhc3MgRmVhdHVyZU5ldChubi5TZXF1ZW50aWFsKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9pbik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9pbiwgNjQpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoNjQsIDMyKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDMyLCA4KSlcblxuY2xhc3MgREtMTW9kZWwoZ3B5dG9yY2gubW9kZWxzLkV4YWN0R1ApOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0cmFpbl94LCB0cmFpbl95LCBsaWtlbGlob29kLCBkX2luKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyh0cmFpbl94LCB0cmFpbl95LCBsaWtlbGlob29kKVxuICAgICAgICBzZWxmLm1lYW5fbW9kdWxlID0gZ3B5dG9yY2gubWVhbnMuQ29uc3RhbnRNZWFuKClcbiAgICAgICAgc2VsZi5jb3Zhcl9tb2R1bGUgPSBncHl0b3JjaC5rZXJuZWxzLlNjYWxlS2VybmVsKGdweXRvcmNoLmtlcm5lbHMuUkJGS2VybmVsKCkpXG4gICAgICAgIHNlbGYuZmVhdHVyZV9uZXQgPSBGZWF0dXJlTmV0KGRfaW4pXG4gICAgICAgIHNlbGYuc2NhbGVyID0gZ3B5dG9yY2gudXRpbHMuZ3JpZC5TY2FsZVRvQm91bmRzKC0xLiwgMS4pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgeiA9IHNlbGYuc2NhbGVyKHNlbGYuZmVhdHVyZV9uZXQoeCkpICAgICMgZF9pbiAtXHUwMDNlIDgtZGltIGJvdW5kZWQgZmVhdHVyZXNcbiAgICAgICAgcmV0dXJuIGdweXRvcmNoLmRpc3RyaWJ1dGlvbnMuTXVsdGl2YXJpYXRlTm9ybWFsKFxuICAgICAgICAgICAgc2VsZi5tZWFuX21vZHVsZSh6KSwgc2VsZi5jb3Zhcl9tb2R1bGUoeikpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5uLCBkID0gNTAwLCAyMFxudHJhaW5feCA9IHRvcmNoLnJhbmRuKG4sIGQpXG50cmFpbl95ID0gdG9yY2guc2luKHRyYWluX3hbOiwgMF0pICsgMC4yICogdG9yY2gucmFuZG4obikgICMgb25seSAxc3QgZmVhdHVyZSBtYXR0ZXJzXG5saWtlbGlob29kID0gZ3B5dG9yY2gubGlrZWxpaG9vZHMuR2F1c3NpYW5MaWtlbGlob29kKClcbm1vZGVsID0gREtMTW9kZWwodHJhaW5feCwgdHJhaW5feSwgbGlrZWxpaG9vZCwgZClcbm1vZGVsLnRyYWluKCk7IGxpa2VsaWhvb2QudHJhaW4oKVxub3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTAuMDEpXG5tbGwgPSBncHl0b3JjaC5tbGxzLkV4YWN0TWFyZ2luYWxMb2dMaWtlbGlob29kKGxpa2VsaWhvb2QsIG1vZGVsKVxuZm9yIGkgaW4gcmFuZ2UoMTUwKTpcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzID0gLW1sbChtb2RlbCh0cmFpbl94KSwgdHJhaW5feSlcbiAgICBsb3NzLmJhY2t3YXJkKCk7IG9wdGltaXplci5zdGVwKClcbiAgICBpZiAoaSArIDEpICUgNTAgPT0gMDpcbiAgICAgICAgcHJpbnQoZlx1MDAyN0l0ZXIge2krMX06IGxvc3M9e2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdES0w6IDIwLWRpbSBpbnB1dCAtXHUwMDNlIDgtZGltIGZlYXR1cmUgc3BhY2UgdmlhIE1MUCwgR1AgaGFuZGxlcyBVUSBvbiB0b3BcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlVzZSBhIExvdyBMZWFybmluZyBSYXRlIGFuZCBQcmV0cmFpbiB0aGUgTk4iLCJjb250ZW50IjoiREtMIG9wdGltaXNhdGlvbiBjYW4gYmUgdW5zdGFibGUgd2hlbiBOTiB3ZWlnaHRzIGFuZCBHUCBoeXBlcnBhcmFtZXRlcnMgYXJlIHRyYWluZWQgc2ltdWx0YW5lb3VzbHkgZnJvbSBzY3JhdGNoLiBBIHByYWN0aWNhbCByZWNpcGU6ICgxKSBwcmV0cmFpbiB0aGUgTk4gb24gdGhlIHJlZ3Jlc3Npb24gdGFzayBhbG9uZSBmb3IgNTDigJMxMDAgZXBvY2hzLCAoMikgdGhlbiBqb2ludGx5IGZpbmUtdHVuZSBOTiArIEdQIGh5cGVycGFyYW1ldGVycyB3aXRoIGEgc21hbGwgbGVhcm5pbmcgcmF0ZSAoMWUtMyBvciBsb3dlcikuIFRoaXMgcHJldmVudHMgdGhlIE5OIGZyb20gY29sbGFwc2luZyBhbGwgaW5wdXRzIHRvIGEgc2luZ2xlIHBvaW50IGluIGZlYXR1cmUgc3BhY2UgYmVmb3JlIHRoZSBHUCBoeXBlcnBhcmFtZXRlcnMgaGF2ZSBhZGFwdGVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRLTCB2cyBTdGFuZGFyZCBHUCBvbiBIaWdoLURpbWVuc2lvbmFsIFJlZ3Jlc3Npb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBiZW5lZml0IG9mIERLTCBvdmVyIGEgc3RhbmRhcmQgUkJGIEdQIGJlY29tZXMgbW9zdCB2aXNpYmxlIGFzIGlucHV0IGRpbWVuc2lvbmFsaXR5IGdyb3dzLiBBIHN0YW5kYXJkIEdQIHdpdGggUkJGIGtlcm5lbCBvbiBkID0gNTAgcmF3IGZlYXR1cmVzIG11c3QgdXNlIGEgc2luZ2xlIHNoYXJlZCBsZW5ndGgtc2NhbGUgYWNyb3NzIGFsbCBkaW1lbnNpb25zIChvciBhIHNlcGFyYXRlIGxlbmd0aC1zY2FsZSBwZXIgZGltZW5zaW9uIHdpdGggQVJELCBzdGlsbCBsaW5lYXIgaW4gZCkuIEl0IGNhbm5vdCBsZWFybiB0aGF0IG9ubHkgYSBoYW5kZnVsIG9mIGZlYXR1cmVzIGFyZSByZWxldmFudC4gREtMXHUwMDI3cyBOTiBhY3RzIGFzIGEgbGVhcm5lZCBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb246IGFmdGVyIHRyYWluaW5nLCB0aGUgOC1kaW1lbnNpb25hbCBmZWF0dXJlIHNwYWNlIGNvbmNlbnRyYXRlcyBvbiB0aGUgZmV3IGRpcmVjdGlvbnMgdGhhdCBhY3R1YWxseSBwcmVkaWN0IHksIGxlYXZpbmcgaXJyZWxldmFudCBmZWF0dXJlcyBpZ25vcmVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IGdweXRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gc2tsZWFybi5nYXVzc2lhbl9wcm9jZXNzIGltcG9ydCBHYXVzc2lhblByb2Nlc3NSZWdyZXNzb3JcbmZyb20gc2tsZWFybi5nYXVzc2lhbl9wcm9jZXNzLmtlcm5lbHMgaW1wb3J0IFJCRiwgV2hpdGVLZXJuZWxcblxubnAucmFuZG9tLnNlZWQoNDIpOyB0b3JjaC5tYW51YWxfc2VlZCg0MilcbmQgPSA1MFxuWF90ciA9IG5wLnJhbmRvbS5yYW5kbigzMDAsIGQpXG55X3RyID0gbnAuc2luKFhfdHJbOiwgMF0pICsgMC4xNSAqIG5wLnJhbmRvbS5yYW5kbigzMDApICAjIG9ubHkgZGltIDAgbWF0dGVyc1xuWF90ZSA9IG5wLnJhbmRvbS5yYW5kbigxMDAsIGQpXG55X3RlID0gbnAuc2luKFhfdGVbOiwgMF0pXG5cbiMgU3RhbmRhcmQgR1Agd2l0aCBBUkQtUkJGIG9uIHJhdyA1MC1kaW0gaW5wdXRcbmtlcm5lbCA9IFJCRihsZW5ndGhfc2NhbGU9bnAub25lcyhkKSkgKyBXaGl0ZUtlcm5lbChub2lzZV9sZXZlbD0wLjEpXG5ncCA9IEdhdXNzaWFuUHJvY2Vzc1JlZ3Jlc3NvcihrZXJuZWw9a2VybmVsLCBuX3Jlc3RhcnRzX29wdGltaXplcj0xKVxuZ3AuZml0KFhfdHIsIHlfdHIpXG5tdV9ncCA9IGdwLnByZWRpY3QoWF90ZSlcbnJtc2VfZ3AgPSBucC5zcXJ0KG5wLm1lYW4oKG11X2dwIC0geV90ZSkqKjIpKVxuXG4jIERLTCBwcm94eTogTUxQIGxlYXJucyB0byBpZ25vcmUgaXJyZWxldmFudCBkaW1zXG50cmFpbl94X3QgPSB0b3JjaC50ZW5zb3IoWF90ciwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnRyYWluX3lfdCA9IHRvcmNoLnRlbnNvcih5X3RyLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxudGVzdF94X3QgID0gdG9yY2gudGVuc29yKFhfdGUsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG5uZXQgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkLCA2NCksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDY0LCAzMiksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDMyLCAxKSlcbm9wdCA9IHRvcmNoLm9wdGltLkFkYW0obmV0LnBhcmFtZXRlcnMoKSwgbHI9MC4wMSlcbmZvciBfIGluIHJhbmdlKDMwMCk6XG4gICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgbG9zcyA9IG5uLk1TRUxvc3MoKShuZXQodHJhaW5feF90KS5zcXVlZXplKCksIHRyYWluX3lfdClcbiAgICBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIG11X2RrbCA9IG5ldCh0ZXN0X3hfdCkuc3F1ZWV6ZSgpLm51bXB5KClcbnJtc2VfZGtsID0gbnAuc3FydChucC5tZWFuKChtdV9ka2wgLSB5X3RlKSoqMikpXG5wcmludChmXHUwMDI3U3RhbmRhcmQgQVJELVJCRiBHUCBSTVNFIChkPTUwKToge3Jtc2VfZ3A6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdES0wtc3R5bGUgTk4gUk1TRSAgICAgIChkPTUwKToge3Jtc2VfZGtsOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdES0wgbGVhcm5zIHRvIGF0dGVuZCB0byBkaW0gMCBvbmx5OyBzdGFuZGFyZCBHUCB3YXN0ZXMgY2FwYWNpdHkgb24gNDkgbm9pc2UgZGltc1x1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLSVNTLUdQOiBTdHJ1Y3R1cmVkIEtlcm5lbCBJbnRlcnBvbGF0aW9uIGZvciBMYXJnZS1TY2FsZSBES0wifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IktJU1MtR1AgKFN0cnVjdHVyZWQgS2VybmVsIEludGVycG9sYXRpb24sIFdpbHNvbiBcdTAwMjYgTmlja2lzY2ggMjAxNSkgZW5hYmxlcyBES0wgdG8gc2NhbGUgYmV5b25kIHRoZSBuw5duIGtlcm5lbCBtYXRyaXggYm90dGxlbmVjay4gQWZ0ZXIgdGhlIE5OIG1hcHMgaW5wdXRzIHRvIGZlYXR1cmUgc3BhY2UsIEtJU1MtR1AgYXBwcm94aW1hdGVzIGtlcm5lbCBldmFsdWF0aW9ucyB1c2luZyBpbnRlcnBvbGF0aW9uIG9uIGEgc3RydWN0dXJlZCBncmlkIG9mIGluZHVjaW5nIHBvaW50czogayjPhih44bWiKSwgz4YoeOKxvCkpIOKJiCB34bWi4bWAIEtfZ3JpZCB34rG8IHdoZXJlIHfhtaIgYXJlIHNwYXJzZSBpbnRlcnBvbGF0aW9uIHdlaWdodHMgYW5kIEtfZ3JpZCBoYXMgYSBLcm9uZWNrZXIgKG9yIFRvZXBsaXR6KSBzdHJ1Y3R1cmUgZW5hYmxpbmcgZmFzdCBtYXRyaXgtdmVjdG9yIHByb2R1Y3RzLiBUaGlzIHJlZHVjZXMgY29zdCB0byBPKG4gKyBtIGxvZyBtKSBwZXIgY29uanVnYXRlIGdyYWRpZW50IGl0ZXJhdGlvbi4gR1B5VG9yY2hcdTAwMjdzIEdyaWRJbnRlcnBvbGF0aW9uS2VybmVsIGltcGxlbWVudHMgS0lTUy1HUCBhbmQgaXMgdGhlIHJlY29tbWVuZGVkIGNob2ljZSB3aGVuIGNvbWJpbmluZyBES0wgd2l0aCBsYXJnZSBuIChcdTAwM2UgMTAsMDAwKS4gVGhlIGtleSBoeXBlcnBhcmFtZXRlciBpcyB0aGUgZ3JpZCBzaXplIOKAlCB0eXBpY2FsbHkgMTAw4oCTMSwwMDAgcG9pbnRzIHBlciBmZWF0dXJlIGRpbWVuc2lvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZWVwIEdQczogU3RhY2tpbmcgR1AgTGF5ZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIERlZXAgR1AgKERhbWlhbm91IFx1MDAyNiBMYXdyZW5jZSAyMDEzKSBzdGFja3MgbXVsdGlwbGUgR1AgbGF5ZXJzIHdoZXJlIGVhY2ggbGF5ZXJcdTAwMjdzIG91dHB1dCBiZWNvbWVzIHRoZSBuZXh0IGxheWVyXHUwMDI3cyBpbnB1dC4gRm9ybWFsbHksIGjCuSA9IGbCuSh4KSwgaMKyID0gZsKyKGjCuSksIOKApiwgeSA9IGbhtLgoaOG0uOKBu8K5KSB3aGVyZSBlYWNoIGbLoSBpcyBhIEdQLiBUaGlzIGluZHVjZXMgYSBoaWVyYXJjaGljYWwgcHJpb3IgdGhhdCBjYW4gcmVwcmVzZW50IG5vbi1zdGF0aW9uYXJ5IGZ1bmN0aW9ucyBhbmQgY29tcGxleCBjb21wb3NpdGlvbmFsIHN0cnVjdHVyZSB1bmFjaGlldmFibGUgd2l0aCBhIHNpbmdsZSBHUC4gSG93ZXZlciwgdGhlIGludHJhY3RhYmxlIG1hcmdpbmFsaXNhdGlvbiBvdmVyIGFsbCBoaWRkZW4gbGF5ZXJzIHJlcXVpcmVzIHZhcmlhdGlvbmFsIGluZmVyZW5jZS4gVGhlIGRvdWJseS1zdG9jaGFzdGljIHZhcmlhdGlvbmFsIGluZmVyZW5jZSAoRFNWSSkgbWV0aG9kIChTYWxpbWJlbmkgXHUwMDI2IERlaXNlbnJvdGggMjAxNykgZHJhd3Mgc2FtcGxlcyBmcm9tIGVhY2ggbGF5ZXJcdTAwMjdzIHZhcmlhdGlvbmFsIHBvc3RlcmlvciBhbmQgcHJvcGFnYXRlcyB0aGVtIGZvcndhcmQg4oCUIGVhY2ggZm9yd2FyZCBwYXNzIHJlcXVpcmVzIE1vbnRlIENhcmxvIHNhbXBsZXMgdGhyb3VnaCBhbGwgaW50ZXJtZWRpYXRlIGxheWVycywgbWFraW5nIHRyYWluaW5nIHN0b2NoYXN0aWMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IGdweXRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBEZWVwIEdQOiB0d28gc3RhY2tlZCBBcHByb3hpbWF0ZUdQIGxheWVycyAoMS1kaW0gaW5wdXQgLVx1MDAzZSAzLWRpbSBoaWRkZW4gLVx1MDAzZSAxLWRpbSBvdXRwdXQpXG5jbGFzcyBIaWRkZW5MYXllcihncHl0b3JjaC5tb2RlbHMuQXBwcm94aW1hdGVHUCk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBpbmR1Y2luZyA9IHRvcmNoLmxpbnNwYWNlKC0zLCAzLCAyNSkudW5zcXVlZXplKC0xKVxuICAgICAgICB2ZCA9IGdweXRvcmNoLnZhcmlhdGlvbmFsLkNob2xlc2t5VmFyaWF0aW9uYWxEaXN0cmlidXRpb24oXG4gICAgICAgICAgICAyNSwgYmF0Y2hfc2hhcGU9dG9yY2guU2l6ZShbM10pKSAgICAgICAgICAjIDMgb3V0cHV0IGRpbWVuc2lvbnNcbiAgICAgICAgdnMgPSBncHl0b3JjaC52YXJpYXRpb25hbC5WYXJpYXRpb25hbFN0cmF0ZWd5KFxuICAgICAgICAgICAgc2VsZiwgaW5kdWNpbmcsIHZkLCBsZWFybl9pbmR1Y2luZ19sb2NhdGlvbnM9VHJ1ZSlcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyh2cylcbiAgICAgICAgc2VsZi5tZWFuX21vZHVsZSAgPSBncHl0b3JjaC5tZWFucy5Db25zdGFudE1lYW4oYmF0Y2hfc2hhcGU9dG9yY2guU2l6ZShbM10pKVxuICAgICAgICBzZWxmLmNvdmFyX21vZHVsZSA9IGdweXRvcmNoLmtlcm5lbHMuU2NhbGVLZXJuZWwoXG4gICAgICAgICAgICBncHl0b3JjaC5rZXJuZWxzLlJCRktlcm5lbChiYXRjaF9zaGFwZT10b3JjaC5TaXplKFszXSkpLFxuICAgICAgICAgICAgYmF0Y2hfc2hhcGU9dG9yY2guU2l6ZShbM10pKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBncHl0b3JjaC5kaXN0cmlidXRpb25zLk11bHRpdmFyaWF0ZU5vcm1hbChcbiAgICAgICAgICAgIHNlbGYubWVhbl9tb2R1bGUoeCksIHNlbGYuY292YXJfbW9kdWxlKHgpKVxuXG5jbGFzcyBPdXRwdXRMYXllcihncHl0b3JjaC5tb2RlbHMuQXBwcm94aW1hdGVHUCk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBpbmR1Y2luZyA9IHRvcmNoLnJhbmRuKDI1LCAzKSAgICAgICAgICAgICAgICMgMy1kaW0gaW5wdXQgZnJvbSBoaWRkZW4gbGF5ZXJcbiAgICAgICAgdmQgPSBncHl0b3JjaC52YXJpYXRpb25hbC5DaG9sZXNreVZhcmlhdGlvbmFsRGlzdHJpYnV0aW9uKDI1KVxuICAgICAgICB2cyA9IGdweXRvcmNoLnZhcmlhdGlvbmFsLlZhcmlhdGlvbmFsU3RyYXRlZ3koXG4gICAgICAgICAgICBzZWxmLCBpbmR1Y2luZywgdmQsIGxlYXJuX2luZHVjaW5nX2xvY2F0aW9ucz1UcnVlKVxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHZzKVxuICAgICAgICBzZWxmLm1lYW5fbW9kdWxlICA9IGdweXRvcmNoLm1lYW5zLkNvbnN0YW50TWVhbigpXG4gICAgICAgIHNlbGYuY292YXJfbW9kdWxlID0gZ3B5dG9yY2gua2VybmVscy5TY2FsZUtlcm5lbChncHl0b3JjaC5rZXJuZWxzLlJCRktlcm5lbCgpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBncHl0b3JjaC5kaXN0cmlidXRpb25zLk11bHRpdmFyaWF0ZU5vcm1hbChcbiAgICAgICAgICAgIHNlbGYubWVhbl9tb2R1bGUoeCksIHNlbGYuY292YXJfbW9kdWxlKHgpKVxuXG50b3JjaC5tYW51YWxfc2VlZCgxKVxuaGlkZGVuID0gSGlkZGVuTGF5ZXIoKTsgb3V0cHV0X2dwID0gT3V0cHV0TGF5ZXIoKVxucHJpbnQoXHUwMDI3RGVlcCBHUCBhcmNoaXRlY3R1cmU6IEhpZGRlbkxheWVyKDEtXHUwMDNlMykgKyBPdXRwdXRMYXllcigzLVx1MDAzZTEpXHUwMDI3KVxucHJpbnQoXHUwMDI3RUxCTyA9IEVfcVtsb2cgcCh5fGZfTCldIC0gS0xbcSh1MSl8fHAodTEpXSAtIEtMW3EodTIpfHxwKHUyKV1cdTAwMjcpXG5wcmludChcdTAwMjdUcmFpbmluZzogZG91Ymx5LXN0b2NoYXN0aWMg4oCUIHNhbXBsZSBoMSBmcm9tIHEodTEpLCBmZWVkIHRvIHEodTIpXHUwMDI3KVxucHJpbnQoXHUwMDI3Q2FwdHVyZXMgbm9uLXN0YXRpb25hcnkgYW5kIGNvbXBvc2l0aW9uYWwgc3RydWN0dXJlIGJleW9uZCBzaW5nbGUtbGF5ZXIgR1BcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiREtMIHZzIEJheWVzaWFuIE5ldXJhbCBOZXR3b3JrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQm90aCBES0wgYW5kIEJheWVzaWFuIE5ldXJhbCBOZXR3b3JrcyAoQk5OcykgYWltIHRvIHByb3ZpZGUgdW5jZXJ0YWludHkgcXVhbnRpZmljYXRpb24gb24gdG9wIG9mIG5ldXJhbCBuZXR3b3JrIGZlYXR1cmUgbGVhcm5pbmcsIGJ1dCB0aGV5IHVzZSB2ZXJ5IGRpZmZlcmVudCBhcHByb3hpbWF0aW9ucy4gREtMIHJlcGxhY2VzIHRoZSBmaW5hbCBsYXllciB3aXRoIGFuIGV4YWN0IEdQIHBvc3RlcmlvciDigJQgdGhlIHVuY2VydGFpbnR5IGlzIEdQLWNhbGlicmF0ZWQgZ2l2ZW4gdGhlIGxlYXJuZWQgZmVhdHVyZXMsIGJ1dCB0aGUgZmVhdHVyZSBleHRyYWN0b3Igd2VpZ2h0cyB3IGFyZSB0cmVhdGVkIGFzIHBvaW50IGVzdGltYXRlcyAobm8gdW5jZXJ0YWludHkgb24gdykuIEJOTnMgbWFpbnRhaW4gYSBkaXN0cmlidXRpb24gb3ZlciBhbGwgd2VpZ2h0cyB2aWEgdmFyaWF0aW9uYWwgaW5mZXJlbmNlIChtZWFuLWZpZWxkKSwgZHJvcG91dCAoTUMgRHJvcG91dCksIG9yIEhhbWlsdG9uaWFuIE1vbnRlIENhcmxvIOKAlCB3ZWlnaHQgdW5jZXJ0YWludHkgcHJvcGFnYXRlcyB0byBwcmVkaWN0aW9ucyBidXQgdGhlIGFwcHJveGltYXRpb24gcXVhbGl0eSBkZXBlbmRzIGhlYXZpbHkgb24gdGhlIHZhcmlhdGlvbmFsIGZhbWlseSBjaG9zZW4uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkZlYXR1cmUgTGVhcm5pbmciLCJVUSBRdWFsaXR5IiwiVHJhaW5pbmcgQ29zdCIsIkludGVycHJldGFiaWxpdHkiLCJTY2FsYWJpbGl0eSIsIktleSBMaW1pdGF0aW9uIl0sInJvd3MiOltbIlN0YW5kYXJkIEdQIiwiTm9uZSDigJQgdXNlcyByYXcgaW5wdXRzIiwiRXhhY3QgKGdpdmVuIGtlcm5lbCkiLCJPKG7CsykiLCJIaWdoIOKAlCBrZXJuZWwgaXMgZXhwbGljaXQiLCJQb29yIGZvciBuXHUwMDNlNWsgb3IgZFx1MDAzZTEwIiwiRml4ZWQtZm9ybSBrZXJuZWwgZmFpbHMgaW4gaGlnaCBkaW1zIl0sWyJES0wiLCJOTiAocG9pbnQgZXN0aW1hdGUgd2VpZ2h0cykiLCJHUC1leGFjdCBpbiBmZWF0dXJlIHNwYWNlIiwiTyhuwrMpICsgTk4gYmFja3Byb3AiLCJNZWRpdW0g4oCUIGZlYXR1cmUgc3BhY2UgbGVhcm5lZCIsIkdvb2Qgd2l0aCBLSVNTLUdQIiwiUG9pbnQtZXN0aW1hdGUgTk4gd2VpZ2h0czsgbm8gdyB1bmNlcnRhaW50eSJdLFsiRGVlcCBHUCIsIkhpZXJhcmNoaWNhbCBHUCBsYXllcnMiLCJWYXJpYXRpb25hbCBhcHByb3hpbWF0aW9uIiwiTyhubcKyTCkgcGVyIHNhbXBsZSIsIkxvdyDigJQgYmxhY2stYm94IGNvbXBvc2l0aW9uIiwiTW9kZXJhdGUgd2l0aCBzcGFyc2UgbGF5ZXJzIiwiRG91Ymx5LXN0b2NoYXN0aWMgdHJhaW5pbmc7IGNvbXBsZXggdG8gdHVuZSJdLFsiQk5OIChNQyBEcm9wb3V0KSIsIkZ1bGwgTk4gKHdlaWdodCBkaXN0cmlidXRpb24pIiwiQXBwcm94aW1hdGUg4oCUIGRyb3BvdXQgcHJveHkiLCJTYW1lIGFzIE5OICsgaW5mZXJlbmNlIHNhbXBsZXMiLCJMb3cg4oCUIGFsbCB3ZWlnaHRzIHVuY2VydGFpbiIsIlNhbWUgYXMgTk4iLCJNQyBEcm9wb3V0IGlzIGEgcG9vciBhcHByb3hpbWF0aW9uIHRvIHRydWUgcG9zdGVyaW9yIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVbmNlcnRhaW50eSBDYWxpYnJhdGlvbiBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDYWxpYnJhdGlvbiBtZWFzdXJlcyB3aGV0aGVyIHByZWRpY3RlZCB1bmNlcnRhaW50eSBpbnRlcnZhbHMgYWN0dWFsbHkgY29udGFpbiB0aGUgdHJ1ZSB2YWx1ZXMgYXQgdGhlIHN0YXRlZCByYXRlIOKAlCBhIDk1JSBjcmVkaWJsZSBpbnRlcnZhbCBzaG91bGQgY292ZXIgdGhlIHRydXRoIDk1JSBvZiB0aGUgdGltZS4gU3RhbmRhcmQgR1BzIGFyZSB3ZWxsLWNhbGlicmF0ZWQgd2hlbiB0aGUga2VybmVsIGFuZCBub2lzZSBhcmUgY29ycmVjdGx5IHNwZWNpZmllZC4gREtMIGluaGVyaXRzIEdQIGNhbGlicmF0aW9uIGluIHRoZSBsZWFybmVkIGZlYXR1cmUgc3BhY2UgYnV0IGNhbiBiZSBtaXNjYWxpYnJhdGVkIGlmIHRoZSBOTiBmZWF0dXJlcyBhcmUgb3ZlcmZpdC4gTUMgRHJvcG91dCAoYSBjb21tb24gQk5OIHByb3h5KSB0ZW5kcyB0byB1bmRlcmVzdGltYXRlIHVuY2VydGFpbnR5IGJlY2F1c2UgZHJvcG91dCB2YXJpYW5jZSBpcyBub3QgYSBwcm9wZXIgQmF5ZXNpYW4gcG9zdGVyaW9yLiBUaGUgY292ZXJhZ2UgbWV0cmljIOKAlCBmcmFjdGlvbiBvZiB0ZXN0IHBvaW50cyB3aGVyZSB0aGUgdHJ1dGggZmFsbHMgd2l0aGluIMKxMs+DIOKAlCBpcyB0aGUgbW9zdCBkaXJlY3QgY2FsaWJyYXRpb24gZGlhZ25vc3RpYy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZ2F1c3NpYW5fcHJvY2VzcyBpbXBvcnQgR2F1c3NpYW5Qcm9jZXNzUmVncmVzc29yXG5mcm9tIHNrbGVhcm4uZ2F1c3NpYW5fcHJvY2Vzcy5rZXJuZWxzIGltcG9ydCBSQkYsIFdoaXRlS2VybmVsXG5mcm9tIHNrbGVhcm4ubmV1cmFsX25ldHdvcmsgaW1wb3J0IE1MUFJlZ3Jlc3NvclxuXG5ucC5yYW5kb20uc2VlZCgwKVxuWF90ciA9IG5wLnJhbmRvbS51bmlmb3JtKC00LCA0LCAoMTUwLCAxKSlcbnlfdHIgPSBucC5zaW4oWF90ci5yYXZlbCgpKSArIDAuMiAqIG5wLnJhbmRvbS5yYW5kbigxNTApXG5YX3RlID0gbnAubGluc3BhY2UoLTYsIDYsIDIwMCkucmVzaGFwZSgtMSwgMSlcbnlfdGUgPSBucC5zaW4oWF90ZS5yYXZlbCgpKVxuXG4jIFN0YW5kYXJkIEdQIOKAlCB3ZWxsLWNhbGlicmF0ZWQgYnkgZGVzaWduXG5ncCA9IEdhdXNzaWFuUHJvY2Vzc1JlZ3Jlc3NvcihrZXJuZWw9UkJGKCkgKyBXaGl0ZUtlcm5lbCgpLCBuX3Jlc3RhcnRzX29wdGltaXplcj0zKVxuZ3AuZml0KFhfdHIsIHlfdHIpXG5tdV9ncCwgc3RkX2dwID0gZ3AucHJlZGljdChYX3RlLCByZXR1cm5fc3RkPVRydWUpXG5jb3ZfZ3AgPSBucC5tZWFuKG5wLmFicyh5X3RlIC0gbXVfZ3ApIFx1MDAzYyAyICogc3RkX2dwKVxuXG4jIE1DIERyb3BvdXQgcHJveHk6IE1MUCB3aXRoIG5vaXNlIGFkZGVkIGF0IGluZmVyZW5jZSB0byBzaW11bGF0ZSBVUVxubWxwID0gTUxQUmVncmVzc29yKGhpZGRlbl9sYXllcl9zaXplcz0oNjQsIDY0KSwgbWF4X2l0ZXI9NjAwLCByYW5kb21fc3RhdGU9MClcbm1scC5maXQoWF90ciwgeV90cilcbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZygxKVxucHJlZHNfbWMgPSBucC5hcnJheShbbWxwLnByZWRpY3QoWF90ZSkgKyAwLjE1ICogcm5nLnN0YW5kYXJkX25vcm1hbCgyMDApIGZvciBfIGluIHJhbmdlKDIwMCldKVxubXVfYm5uLCBzdGRfYm5uID0gcHJlZHNfbWMubWVhbihheGlzPTApLCBwcmVkc19tYy5zdGQoYXhpcz0wKVxuY292X2JubiA9IG5wLm1lYW4obnAuYWJzKHlfdGUgLSBtdV9ibm4pIFx1MDAzYyAyICogc3RkX2JubilcblxucHJpbnQoZlx1MDAyN1N0YW5kYXJkIEdQICA5NSUtYmFuZCBjb3ZlcmFnZToge2Nvdl9ncDouMiV9ICAodGFyZ2V0IDk1JSlcdTAwMjcpXG5wcmludChmXHUwMDI3TUMgRHJvcG91dCAgIDk1JS1iYW5kIGNvdmVyYWdlOiB7Y292X2JubjouMiV9XHUwMDI3KVxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDEsIDIsIGZpZ3NpemU9KDEzLCA0KSwgc2hhcmV5PVRydWUpXG5mb3IgYXgsIG11LCBzdGQsIGxhYmVsIGluIHppcChheGVzLCBbbXVfZ3AsIG11X2Jubl0sIFtzdGRfZ3AsIHN0ZF9ibm5dLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFtcdTAwMjdTdGFuZGFyZCBHUCAod2VsbC1jYWxpYnJhdGVkKVx1MDAyNywgXHUwMDI3TUMgRHJvcG91dCAvIEJOTiBwcm94eVx1MDAyN10pOlxuICAgIGF4LmZpbGxfYmV0d2VlbihYX3RlLnJhdmVsKCksIG11IC0gMipzdGQsIG11ICsgMipzdGQsIGFscGhhPTAuMjUpXG4gICAgYXgucGxvdChYX3RlLnJhdmVsKCksIG11LCBsdz0yKTsgYXgucGxvdChYX3RlLnJhdmVsKCksIHlfdGUsIFx1MDAyN2stLVx1MDAyNywgbHc9MSwgYWxwaGE9MC43KVxuICAgIGF4LnNjYXR0ZXIoWF90ci5yYXZlbCgpLCB5X3RyLCBzPTIwLCBjPVx1MDAyN3JcdTAwMjcsIHpvcmRlcj01KTsgYXguc2V0X3RpdGxlKGxhYmVsKVxucGx0LnN1cHRpdGxlKFx1MDAyN0NhbGlicmF0aW9uOiBkb2VzIMKxMs+DIGNvbnRhaW4gOTUlIG9mIHRlc3QgcG9pbnRzP1x1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIEdQIGtlcm5lbHMgYXBwbGllZCB0byByYXcgaGlnaC1kaW1lbnNpb25hbCBpbnB1dHMgZGVncmFkZSBhcyBldmVyeSBwYWlyIG9mIHBvaW50cyBiZWNvbWVzIGVxdWlkaXN0YW50LiBEZWVwIEtlcm5lbCBMZWFybmluZyBmaXhlcyB0aGlzIGJ5IGNvbXBvc2luZyBhIG5ldXJhbCBuZXR3b3JrIM+GKHg7IHcpIHdpdGggYSBiYXNlIGtlcm5lbDogayh4LCB4XHUwMDI3KSA9IGtfYmFzZSjPhih4O3cpLCDPhih4XHUwMDI3O3cpKS4gTk4gd2VpZ2h0cyBhbmQgR1AgaHlwZXJwYXJhbWV0ZXJzIGFyZSBqb2ludGx5IG9wdGltaXNlZCB2aWEgbG9nIG1hcmdpbmFsIGxpa2VsaWhvb2QuIERLTCBkZWxpdmVycyBHUC1jYWxpYnJhdGVkIHVuY2VydGFpbnR5IGluIGEgbGVhcm5lZCBmZWF0dXJlIHNwYWNlLiBLSVNTLUdQIG1ha2VzIERLTCBzY2FsYWJsZSB0byBsYXJnZSBuIHZpYSBzdHJ1Y3R1cmVkIGtlcm5lbCBpbnRlcnBvbGF0aW9uLiBEZWVwIEdQcyBzdGFjayBtdWx0aXBsZSBHUCBsYXllcnMgZm9yIGNvbXBvc2l0aW9uYWwgcHJpb3JzIGJ1dCByZXF1aXJlIGRvdWJseS1zdG9jaGFzdGljIHZhcmlhdGlvbmFsIGluZmVyZW5jZS4gQ29tcGFyZWQgd2l0aCBCTk5zLCBES0wgZ2l2ZXMgYmV0dGVyLWNhbGlicmF0ZWQgdW5jZXJ0YWludHkgYnV0IHRyZWF0cyBmZWF0dXJlIGV4dHJhY3RvciB3ZWlnaHRzIGFzIHBvaW50IGVzdGltYXRlcyDigJQgYSB0cmFkZS1vZmYgd29ydGggdW5kZXJzdGFuZGluZyB3aGVuIGNob29zaW5nIGJldHdlZW4gdGhlIHR3by4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkRLTCBrZXJuZWw6IGsoeCx4XHUwMDI3KSA9IGtfYmFzZSjPhih4O3cpLCDPhih4XHUwMDI3O3cpKSDigJQgTk4gbWFwcyBpbnB1dHMgdG8gR1AtY29tcGF0aWJsZSBzcGFjZSIsIkpvaW50IG9wdGltaXNhdGlvbjogTk4gd2VpZ2h0cyB3ICsgR1AgaHlwZXJwYXJhbWV0ZXJzIM64IHZpYSBsb2cgbWFyZ2luYWwgbGlrZWxpaG9vZCIsIlByZXRyYWluIE5OIGJlZm9yZSBqb2ludCB0dW5pbmcgdG8gYXZvaWQgZmVhdHVyZS1zcGFjZSBjb2xsYXBzZSIsIktJU1MtR1A6IHN0cnVjdHVyZWQga2VybmVsIGludGVycG9sYXRpb24gcmVkdWNlcyBES0wgdG8gTyhuICsgbSBsb2cgbSkgcGVyIENHIHN0ZXAiLCJEZWVwIEdQOiBoaWVyYXJjaGljYWwgcHJpb3IgdmlhIHN0YWNrZWQgR1AgbGF5ZXJzIOKAlCBEU1ZJIGZvciB0cmFpbmluZywgY2FwdHVyZXMgbm9uLXN0YXRpb25hcml0eSIsIkRLTCB2cyBCTk46IERLTCBoYXMgR1AtZXhhY3QgVVEgaW4gZmVhdHVyZSBzcGFjZTsgQk5OIGhhcyBmdWxsIHdlaWdodCB1bmNlcnRhaW50eSBidXQgd29yc2UgY2FsaWJyYXRpb24iLCJDYWxpYnJhdGlvbiBtZXRyaWM6IDk1JS1iYW5kIGNvdmVyYWdlIOKAlCBHUCB0eXBpY2FsbHkgbmVhciA5NSUsIE1DIERyb3BvdXQgb2Z0ZW4gdW5kZXItY292ZXJzIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Deep Kernel Learning — Neural Networks Meet GPs

## Why Standard GP Kernels Fail on High-Dimensional Data

Standard GP kernels such as RBF and Matérn operate directly on raw inputs. In low dimensions (d ≤ 5) this works well: the kernel can measure meaningful similarity between inputs and the covariance structure captures the function's behaviour. In high dimensions (images, text embeddings, tabular data with d > 20), the curse of dimensionality strikes: every pair of points becomes approximately equidistant under a fixed-bandwidth kernel, so the kernel matrix degenerates to near-constant values and carries almost no information. Additionally, a fixed-form kernel cannot capture complex non-stationary patterns or domain-specific structure. The solution is to learn a feature representation before applying the kernel.

## Deep Kernel Learning — Composing Neural Networks with GPs

Deep Kernel Learning (DKL, Wilson et al. 2016) composes a neural network φ(x; w) with a base kernel k_base to define a new kernel: k(x, x') = k_base(φ(x; w), φ(x'; w)). The neural network maps raw inputs to a low-dimensional feature space where the base kernel is applied. The NN weights w and GP hyperparameters θ (length-scale, signal variance, noise variance) are learned jointly by maximising the log marginal likelihood log p(y | X, w, θ). This combines the feature-learning power of neural networks with the principled uncertainty quantification of GPs — a best-of-both-worlds approach.

- k(x,x') = k_base(φ(x;w), φ(x';w)) — NN maps inputs to GP-compatible feature space
- NN weights w and GP hyperparameters θ jointly optimised via marginal likelihood
- Feature space dim is a hyperparameter: typically 2–16 dimensions regardless of input dim d
- Uncertainty quantification is exact GP UQ applied in learned feature space
- Works well for: images (CNN extractor), structured tabular data (MLP), sequences (LSTM)
- Limitation: the GP kernel matrix is still n×n — combine with sparse GP (KISS-GP) for large n

```python
import torch
import torch.nn as nn
import gpytorch

class FeatureNet(nn.Sequential):
    def __init__(self, d_in):
        super().__init__(
            nn.Linear(d_in, 64), nn.ReLU(),
            nn.Linear(64, 32), nn.ReLU(),
            nn.Linear(32, 8))

class DKLModel(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood, d_in):
        super().__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ConstantMean()
        self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())
        self.feature_net = FeatureNet(d_in)
        self.scaler = gpytorch.utils.grid.ScaleToBounds(-1., 1.)

    def forward(self, x):
        z = self.scaler(self.feature_net(x))    # d_in -> 8-dim bounded features
        return gpytorch.distributions.MultivariateNormal(
            self.mean_module(z), self.covar_module(z))

torch.manual_seed(0)
n, d = 500, 20
train_x = torch.randn(n, d)
train_y = torch.sin(train_x[:, 0]) + 0.2 * torch.randn(n)  # only 1st feature matters
likelihood = gpytorch.likelihoods.GaussianLikelihood()
model = DKLModel(train_x, train_y, likelihood, d)
model.train(); likelihood.train()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
for i in range(150):
    optimizer.zero_grad()
    loss = -mll(model(train_x), train_y)
    loss.backward(); optimizer.step()
    if (i + 1) % 50 == 0:
        print(f'Iter {i+1}: loss={loss.item():.4f}')
print('DKL: 20-dim input -> 8-dim feature space via MLP, GP handles UQ on top')
```

> **Use a Low Learning Rate and Pretrain the NN**: DKL optimisation can be unstable when NN weights and GP hyperparameters are trained simultaneously from scratch. A practical recipe: (1) pretrain the NN on the regression task alone for 50–100 epochs, (2) then jointly fine-tune NN + GP hyperparameters with a small learning rate (1e-3 or lower). This prevents the NN from collapsing all inputs to a single point in feature space before the GP hyperparameters have adapted.

## DKL vs Standard GP on High-Dimensional Regression

The benefit of DKL over a standard RBF GP becomes most visible as input dimensionality grows. A standard GP with RBF kernel on d = 50 raw features must use a single shared length-scale across all dimensions (or a separate length-scale per dimension with ARD, still linear in d). It cannot learn that only a handful of features are relevant. DKL's NN acts as a learned dimensionality reduction: after training, the 8-dimensional feature space concentrates on the few directions that actually predict y, leaving irrelevant features ignored.

```python
import numpy as np
import torch
import gpytorch
import torch.nn as nn
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

np.random.seed(42); torch.manual_seed(42)
d = 50
X_tr = np.random.randn(300, d)
y_tr = np.sin(X_tr[:, 0]) + 0.15 * np.random.randn(300)  # only dim 0 matters
X_te = np.random.randn(100, d)
y_te = np.sin(X_te[:, 0])

# Standard GP with ARD-RBF on raw 50-dim input
kernel = RBF(length_scale=np.ones(d)) + WhiteKernel(noise_level=0.1)
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=1)
gp.fit(X_tr, y_tr)
mu_gp = gp.predict(X_te)
rmse_gp = np.sqrt(np.mean((mu_gp - y_te)**2))

# DKL proxy: MLP learns to ignore irrelevant dims
train_x_t = torch.tensor(X_tr, dtype=torch.float32)
train_y_t = torch.tensor(y_tr, dtype=torch.float32)
test_x_t  = torch.tensor(X_te, dtype=torch.float32)
net = nn.Sequential(nn.Linear(d, 64), nn.ReLU(), nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 1))
opt = torch.optim.Adam(net.parameters(), lr=0.01)
for _ in range(300):
    opt.zero_grad()
    loss = nn.MSELoss()(net(train_x_t).squeeze(), train_y_t)
    loss.backward(); opt.step()
with torch.no_grad():
    mu_dkl = net(test_x_t).squeeze().numpy()
rmse_dkl = np.sqrt(np.mean((mu_dkl - y_te)**2))
print(f'Standard ARD-RBF GP RMSE (d=50): {rmse_gp:.4f}')
print(f'DKL-style NN RMSE      (d=50): {rmse_dkl:.4f}')
print('DKL learns to attend to dim 0 only; standard GP wastes capacity on 49 noise dims')
```

## KISS-GP: Structured Kernel Interpolation for Large-Scale DKL

KISS-GP (Structured Kernel Interpolation, Wilson & Nickisch 2015) enables DKL to scale beyond the n×n kernel matrix bottleneck. After the NN maps inputs to feature space, KISS-GP approximates kernel evaluations using interpolation on a structured grid of inducing points: k(φ(xᵢ), φ(xⱼ)) ≈ wᵢᵀ K_grid wⱼ where wᵢ are sparse interpolation weights and K_grid has a Kronecker (or Toeplitz) structure enabling fast matrix-vector products. This reduces cost to O(n + m log m) per conjugate gradient iteration. GPyTorch's GridInterpolationKernel implements KISS-GP and is the recommended choice when combining DKL with large n (> 10,000). The key hyperparameter is the grid size — typically 100–1,000 points per feature dimension.

## Deep GPs: Stacking GP Layers

A Deep GP (Damianou & Lawrence 2013) stacks multiple GP layers where each layer's output becomes the next layer's input. Formally, h¹ = f¹(x), h² = f²(h¹), …, y = fᴸ(hᴸ⁻¹) where each fˡ is a GP. This induces a hierarchical prior that can represent non-stationary functions and complex compositional structure unachievable with a single GP. However, the intractable marginalisation over all hidden layers requires variational inference. The doubly-stochastic variational inference (DSVI) method (Salimbeni & Deisenroth 2017) draws samples from each layer's variational posterior and propagates them forward — each forward pass requires Monte Carlo samples through all intermediate layers, making training stochastic.

```python
import torch
import gpytorch
import numpy as np

# Deep GP: two stacked ApproximateGP layers (1-dim input -> 3-dim hidden -> 1-dim output)
class HiddenLayer(gpytorch.models.ApproximateGP):
    def __init__(self):
        inducing = torch.linspace(-3, 3, 25).unsqueeze(-1)
        vd = gpytorch.variational.CholeskyVariationalDistribution(
            25, batch_shape=torch.Size([3]))          # 3 output dimensions
        vs = gpytorch.variational.VariationalStrategy(
            self, inducing, vd, learn_inducing_locations=True)
        super().__init__(vs)
        self.mean_module  = gpytorch.means.ConstantMean(batch_shape=torch.Size([3]))
        self.covar_module = gpytorch.kernels.ScaleKernel(
            gpytorch.kernels.RBFKernel(batch_shape=torch.Size([3])),
            batch_shape=torch.Size([3]))

    def forward(self, x):
        return gpytorch.distributions.MultivariateNormal(
            self.mean_module(x), self.covar_module(x))

class OutputLayer(gpytorch.models.ApproximateGP):
    def __init__(self):
        inducing = torch.randn(25, 3)               # 3-dim input from hidden layer
        vd = gpytorch.variational.CholeskyVariationalDistribution(25)
        vs = gpytorch.variational.VariationalStrategy(
            self, inducing, vd, learn_inducing_locations=True)
        super().__init__(vs)
        self.mean_module  = gpytorch.means.ConstantMean()
        self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())

    def forward(self, x):
        return gpytorch.distributions.MultivariateNormal(
            self.mean_module(x), self.covar_module(x))

torch.manual_seed(1)
hidden = HiddenLayer(); output_gp = OutputLayer()
print('Deep GP architecture: HiddenLayer(1->3) + OutputLayer(3->1)')
print('ELBO = E_q[log p(y|f_L)] - KL[q(u1)||p(u1)] - KL[q(u2)||p(u2)]')
print('Training: doubly-stochastic — sample h1 from q(u1), feed to q(u2)')
print('Captures non-stationary and compositional structure beyond single-layer GP')
```

## DKL vs Bayesian Neural Networks

Both DKL and Bayesian Neural Networks (BNNs) aim to provide uncertainty quantification on top of neural network feature learning, but they use very different approximations. DKL replaces the final layer with an exact GP posterior — the uncertainty is GP-calibrated given the learned features, but the feature extractor weights w are treated as point estimates (no uncertainty on w). BNNs maintain a distribution over all weights via variational inference (mean-field), dropout (MC Dropout), or Hamiltonian Monte Carlo — weight uncertainty propagates to predictions but the approximation quality depends heavily on the variational family chosen.

| Method | Feature Learning | UQ Quality | Training Cost | Interpretability | Scalability | Key Limitation |
| --- | --- | --- | --- | --- | --- | --- |
| Standard GP | None — uses raw inputs | Exact (given kernel) | O(n³) | High — kernel is explicit | Poor for n>5k or d>10 | Fixed-form kernel fails in high dims |
| DKL | NN (point estimate weights) | GP-exact in feature space | O(n³) + NN backprop | Medium — feature space learned | Good with KISS-GP | Point-estimate NN weights; no w uncertainty |
| Deep GP | Hierarchical GP layers | Variational approximation | O(nm²L) per sample | Low — black-box composition | Moderate with sparse layers | Doubly-stochastic training; complex to tune |
| BNN (MC Dropout) | Full NN (weight distribution) | Approximate — dropout proxy | Same as NN + inference samples | Low — all weights uncertain | Same as NN | MC Dropout is a poor approximation to true posterior |

## Uncertainty Calibration Comparison

Calibration measures whether predicted uncertainty intervals actually contain the true values at the stated rate — a 95% credible interval should cover the truth 95% of the time. Standard GPs are well-calibrated when the kernel and noise are correctly specified. DKL inherits GP calibration in the learned feature space but can be miscalibrated if the NN features are overfit. MC Dropout (a common BNN proxy) tends to underestimate uncertainty because dropout variance is not a proper Bayesian posterior. The coverage metric — fraction of test points where the truth falls within ±2σ — is the most direct calibration diagnostic.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.neural_network import MLPRegressor

np.random.seed(0)
X_tr = np.random.uniform(-4, 4, (150, 1))
y_tr = np.sin(X_tr.ravel()) + 0.2 * np.random.randn(150)
X_te = np.linspace(-6, 6, 200).reshape(-1, 1)
y_te = np.sin(X_te.ravel())

# Standard GP — well-calibrated by design
gp = GaussianProcessRegressor(kernel=RBF() + WhiteKernel(), n_restarts_optimizer=3)
gp.fit(X_tr, y_tr)
mu_gp, std_gp = gp.predict(X_te, return_std=True)
cov_gp = np.mean(np.abs(y_te - mu_gp) < 2 * std_gp)

# MC Dropout proxy: MLP with noise added at inference to simulate UQ
mlp = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=600, random_state=0)
mlp.fit(X_tr, y_tr)
rng = np.random.default_rng(1)
preds_mc = np.array([mlp.predict(X_te) + 0.15 * rng.standard_normal(200) for _ in range(200)])
mu_bnn, std_bnn = preds_mc.mean(axis=0), preds_mc.std(axis=0)
cov_bnn = np.mean(np.abs(y_te - mu_bnn) < 2 * std_bnn)

print(f'Standard GP  95%-band coverage: {cov_gp:.2%}  (target 95%)')
print(f'MC Dropout   95%-band coverage: {cov_bnn:.2%}')
fig, axes = plt.subplots(1, 2, figsize=(13, 4), sharey=True)
for ax, mu, std, label in zip(axes, [mu_gp, mu_bnn], [std_gp, std_bnn],
                               ['Standard GP (well-calibrated)', 'MC Dropout / BNN proxy']):
    ax.fill_between(X_te.ravel(), mu - 2*std, mu + 2*std, alpha=0.25)
    ax.plot(X_te.ravel(), mu, lw=2); ax.plot(X_te.ravel(), y_te, 'k--', lw=1, alpha=0.7)
    ax.scatter(X_tr.ravel(), y_tr, s=20, c='r', zorder=5); ax.set_title(label)
plt.suptitle('Calibration: does ±2σ contain 95% of test points?')
plt.tight_layout(); plt.show()
```

## Key Takeaways

Standard GP kernels applied to raw high-dimensional inputs degrade as every pair of points becomes equidistant. Deep Kernel Learning fixes this by composing a neural network φ(x; w) with a base kernel: k(x, x') = k_base(φ(x;w), φ(x';w)). NN weights and GP hyperparameters are jointly optimised via log marginal likelihood. DKL delivers GP-calibrated uncertainty in a learned feature space. KISS-GP makes DKL scalable to large n via structured kernel interpolation. Deep GPs stack multiple GP layers for compositional priors but require doubly-stochastic variational inference. Compared with BNNs, DKL gives better-calibrated uncertainty but treats feature extractor weights as point estimates — a trade-off worth understanding when choosing between the two.

- DKL kernel: k(x,x') = k_base(φ(x;w), φ(x';w)) — NN maps inputs to GP-compatible space
- Joint optimisation: NN weights w + GP hyperparameters θ via log marginal likelihood
- Pretrain NN before joint tuning to avoid feature-space collapse
- KISS-GP: structured kernel interpolation reduces DKL to O(n + m log m) per CG step
- Deep GP: hierarchical prior via stacked GP layers — DSVI for training, captures non-stationarity
- DKL vs BNN: DKL has GP-exact UQ in feature space; BNN has full weight uncertainty but worse calibration
- Calibration metric: 95%-band coverage — GP typically near 95%, MC Dropout often under-covers

---

