---
title: "Universal Approximation Theorem — Statements and Limitations"
slug: "universal-approximation-theorem"
description: "Survey UAT variants from Cybenko to depth-separation results, empirically demonstrate width vs depth tradeoffs on function approximation tasks, and understand what UAT guarantees and critically what it does not."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFVuaXZlcnNhbCBBcHByb3hpbWF0aW9uIFRoZW9yZW0gKFVBVCkgaXMgdGhlIHRoZW9yZXRpY2FsIGZvdW5kYXRpb24gZm9yIHdoeSBuZXVyYWwgbmV0d29ya3MgY2FuLCBpbiBwcmluY2lwbGUsIHJlcHJlc2VudCBhbnkgZnVuY3Rpb24uIEN5YmVua28gKDE5ODkpIHByb3ZlZCB0aGF0IGEgc2luZ2xlIGhpZGRlbiBsYXllciB3aXRoIHNpZ21vaWQgYWN0aXZhdGlvbnMgYW5kIGVub3VnaCBuZXVyb25zIGNhbiBhcHByb3hpbWF0ZSBhbnkgY29udGludW91cyBmdW5jdGlvbiBvbiBhIGNvbXBhY3Qgc3Vic2V0IG9mIOKEneKBvyB0byBhcmJpdHJhcnkgYWNjdXJhY3kuIFRoaXMgcmVzdWx0IGlzIGNvbWZvcnRpbmcgYnV0IGRhbmdlcm91c2x5IGVhc3kgdG8gbWlzaW50ZXJwcmV0IOKAlCBpdCBpcyBhIHB1cmUgZXhpc3RlbmNlIHJlc3VsdCB0aGF0IHNheXMgbm90aGluZyBhYm91dCBob3cgdG8gZmluZCB0aGUgd2VpZ2h0cywgaG93IG1hbnkgbmV1cm9ucyBhcmUgcmVxdWlyZWQsIG9yIGhvdyBtYW55IHRyYWluaW5nIGV4YW1wbGVzIGFyZSBuZWVkZWQgdG8gZ2VuZXJhbGl6ZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBVQVQgaGFzIHNwYXduZWQgYSBmYW1pbHkgb2YgaW5jcmVhc2luZ2x5IHByZWNpc2UgcmVzdWx0czogSG9ybmlrICgxOTkxKSBnZW5lcmFsaXplZCB0byBhcmJpdHJhcnkgc3F1YXNoaW5nIGFjdGl2YXRpb25zLCBCYXJyb24gKDE5OTMpIGdhdmUgYSBjb25zdHJ1Y3RpdmUgZGltZW5zaW9uLWZyZWUgYm91bmQsIGFuZCBUZWxnYXJza3kgKDIwMTYpIHByb3ZlZCBleHBvbmVudGlhbCBkZXB0aC1zZXBhcmF0aW9uIHJlc3VsdHMuIEVhY2ggYWRkcmVzc2VzIGRpZmZlcmVudCBhc3BlY3RzIG9mIHdoYXQgbmV0d29ya3MgY2FuIHJlcHJlc2VudCBhbmQgYXQgd2hhdCBjb3N0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkN5YmVua28gMTk4OSBhbmQgSG9ybmlrIDE5OTEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkN5YmVua29cdTAwMjdzIHRoZW9yZW06IEZvciBhbnkgY29udGludW91cyBmOiBbMCwxXeKBvyDihpIg4oSdIGFuZCBhbnkgzrUgXHUwMDNlIDAsIHRoZXJlIGV4aXN0IHdlaWdodHMgVywgYmlhc2VzIGIsIGFuZCBvdXRwdXQgd2VpZ2h0cyB2IHN1Y2ggdGhhdCB8zqPisbwgduKxvCDPgyhX4rG84bWAeCArIGLisbwpIOKIkiBmKHgpfCBcdTAwM2MgzrUgZm9yIGFsbCB4IOKIiCBbMCwxXeKBvywgd2hlcmUgz4MgaXMgYW55IGNvbnRpbnVvdXMgc2lnbW9pZGFsIGZ1bmN0aW9uLiBIb3JuaWsgKDE5OTEpIGdlbmVyYWxpemVkIHRvIGFyYml0cmFyeSBzcXVhc2hpbmcgZnVuY3Rpb25zIGFuZCBtdWx0aS1vdXRwdXQgbmV0d29ya3MuIExlc2hubyAoMTk5Mykgc2hvd2VkIHRoZSByZXN1bHQgaG9sZHMgZm9yIGFueSBub24tcG9seW5vbWlhbCBhY3RpdmF0aW9uLiBBbGwgcHJvb2ZzIGFyZSBub24tY29uc3RydWN0aXZlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSB3b3JkIGlzIGV4aXN0ZW5jZSDigJQgdGhlIHRoZW9yZW0gcHJvdmVzIHN1Y2ggd2VpZ2h0cyBleGlzdCBidXQgcHJvdmlkZXMgbm8gYWxnb3JpdGhtIHRvIGZpbmQgdGhlbS4gVGhlIHJlcXVpcmVkIG51bWJlciBvZiBuZXVyb25zIG1heSBiZSBleHBvbmVudGlhbCBpbiB0aGUgaW5wdXQgZGltZW5zaW9uIGZvciBzb21lIGZ1bmN0aW9ucy4gVGhlIHRoZW9yZW0gYWxzbyBzYXlzIG5vdGhpbmcgYWJvdXQgdGhlIHNhbXBsZSBjb21wbGV4aXR5IG9mIGxlYXJuaW5nIGZyb20gZmluaXRlIGRhdGEsIG5vciBhYm91dCB3aGV0aGVyIGdyYWRpZW50IGRlc2NlbnQgd2lsbCBjb252ZXJnZSB0byB0aGUgYXBwcm94aW1hdGluZyB3ZWlnaHRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLm9wdGltIGltcG9ydCBBZGFtXG5cbmRlZiBhcHByb3hpbWF0ZV9mdW5jdGlvbihuX2hpZGRlbiwgbl9zdGVwcz0zMDAwLCBzZWVkPTApOlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgWCA9IHRvcmNoLmxpbnNwYWNlKC1ucC5waSwgbnAucGksIDUwMCkudW5zcXVlZXplKDEpXG4gICAgeSA9IHRvcmNoLnNpbigzKlguc3F1ZWV6ZSgpKSAqIHRvcmNoLmNvcyhYLnNxdWVlemUoKSkgKyBYLnNxdWVlemUoKSoqMiAvIDRcbiAgICBtb2RlbCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDEsIG5faGlkZGVuKSwgbm4uU2lnbW9pZCgpLCBubi5MaW5lYXIobl9oaWRkZW4sIDEpKVxuICAgIG9wdCA9IEFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0yKVxuICAgIGZvciBfIGluIHJhbmdlKG5fc3RlcHMpOlxuICAgICAgICBsb3NzID0gKChtb2RlbChYKS5zcXVlZXplKCkgLSB5KSoqMikubWVhbigpXG4gICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHJldHVybiAoKG1vZGVsKFgpLnNxdWVlemUoKSAtIHkpKioyKS5tZWFuKCkuaXRlbSgpXG5cbnByaW50KGZcdTAwMjd7XCJXaWR0aFwiOlx1MDAzZTZ9IHwge1wiRmluYWwgTVNFXCI6XHUwMDNlMTB9XHUwMDI3KVxuZm9yIHcgaW4gWzIsIDEwLCA1MCwgMjAwLCAxMDAwXTpcbiAgICBwcmludChmXHUwMDI3e3c6XHUwMDNlNn0gfCB7YXBwcm94aW1hdGVfZnVuY3Rpb24odyk6XHUwMDNlMTAuNmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlcHRoIEFkdmFudGFnZSDigJQgV2lkdGggdnMgRGVwdGgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBVQVQgZ3VhcmFudGVlcyBhIHNpbmdsZSBoaWRkZW4gbGF5ZXIgc3VmZmljZXMsIGJ1dCBtYXkgcmVxdWlyZSBleHBvbmVudGlhbGx5IG1hbnkgbmV1cm9ucy4gRGVwdGggc2VwYXJhdGlvbiByZXN1bHRzIChUZWxnYXJza3kgMjAxNikgc2hvdyB0aGF0IGZ1bmN0aW9ucyByZXByZXNlbnRhYmxlIGJ5IGRlcHRoLWsgbmV0d29ya3Mgd2l0aCBPKG4pIG5ldXJvbnMgcmVxdWlyZSDOqSgyXm4pIG5ldXJvbnMgaW4gYSBkZXB0aC0oa+KIkjEpIG5ldHdvcmsuIFByYWN0aWNhbGx5OiBhIGRlZXAgbmFycm93IG5ldHdvcmsgb2Z0ZW4gb3V0cGVyZm9ybXMgYSB3aWRlIHNoYWxsb3cgbmV0d29yayBhdCB0aGUgc2FtZSBwYXJhbWV0ZXIgY291bnQgYmVjYXVzZSBkZXB0aCBlbmFibGVzIGNvbXBvc2luZyBzaW1wbGVyIHRyYW5zZm9ybWF0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2gub3B0aW0gaW1wb3J0IEFkYW1cbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgYnVpbGRfbmV0KGRlcHRoLCB3aWR0aCwgZF9pbj0xKTpcbiAgICBsYXllcnMgPSBbbm4uTGluZWFyKGRfaW4sIHdpZHRoKSwgbm4uUmVMVSgpXVxuICAgIGZvciBfIGluIHJhbmdlKGRlcHRoIC0gMSk6IGxheWVycyArPSBbbm4uTGluZWFyKHdpZHRoLCB3aWR0aCksIG5uLlJlTFUoKV1cbiAgICBsYXllcnMuYXBwZW5kKG5uLkxpbmVhcih3aWR0aCwgMSkpXG4gICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwoKmxheWVycylcblxuZGVmIHRyYWluX21zZShtb2RlbCwgWCwgeSwgc3RlcHM9MjAwMCk6XG4gICAgb3B0ID0gQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG4gICAgZm9yIF8gaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICBsb3NzID0gKChtb2RlbChYKS5zcXVlZXplKCkgLSB5KSoqMikubWVhbigpXG4gICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6IHJldHVybiAoKG1vZGVsKFgpLnNxdWVlemUoKS15KSoqMikubWVhbigpLml0ZW0oKVxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcblggPSB0b3JjaC5saW5zcGFjZSgwLCAyKm5wLnBpLCA0MDApLnVuc3F1ZWV6ZSgxKVxueSA9IHRvcmNoLnNpbig1Klguc3F1ZWV6ZSgpKSAqIHRvcmNoLmNvcygzKlguc3F1ZWV6ZSgpKVxuWF90ciwgeV90ciA9IFhbOjMwMF0sIHlbOjMwMF1cbnByaW50KGZcdTAwMjd7XCJDb25maWdcIjoyMn0gfCBQYXJhbXMgfCBUZXN0IE1TRVx1MDAyNylcbmZvciBkZXB0aCwgd2lkdGggaW4gWygxLCA0MDApLCAoMywgNjQpLCAoNiwgMjQpXTpcbiAgICBtb2RlbCA9IGJ1aWxkX25ldChkZXB0aCwgd2lkdGgpXG4gICAgcGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpXG4gICAgbXNlID0gdHJhaW5fbXNlKG1vZGVsLCBYX3RyLCB5X3RyKVxuICAgIHByaW50KGZcdTAwMjdkZXB0aD17ZGVwdGh9IHdpZHRoPXt3aWR0aDozZH0gICAgICAgfCB7cGFyYW1zOjZkfSB8IHttc2U6LjZmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVQVQgRG9lcyBOb3QgR3VhcmFudGVlIExlYXJuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVQVQgZ3VhcmFudGVlcyB0aGUgZXhpc3RlbmNlIG9mIHdlaWdodHMgdGhhdCBhcHByb3hpbWF0ZSBhbnkgdGFyZ2V0IGZ1bmN0aW9uLCBidXQgZ3JhZGllbnQgZGVzY2VudCBpcyBub3QgZ3VhcmFudGVlZCB0byBmaW5kIHRoZW0uIEZvciBoaWdobHkgb3NjaWxsYXRvcnkgZnVuY3Rpb25zLCB0aGUgbG9zcyBsYW5kc2NhcGUgaGFzIGV4cG9uZW50aWFsbHkgbWFueSBsb2NhbCBtaW5pbWEgYW5kIHNhZGRsZSBwb2ludHMuIEV2ZW4gd2l0aCBzdWZmaWNpZW50IGNhcGFjaXR5LCBTR0QgbWF5IGNvbnZlcmdlIHRvIGEgcG9vciBzb2x1dGlvbiwgbm90IHRoZSBhcHByb3hpbWF0aW5nIHdlaWdodHMgdGhlIHRoZW9yZW0gZ3VhcmFudGVlcyBleGlzdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2gub3B0aW0gaW1wb3J0IEFkYW1cbmltcG9ydCBudW1weSBhcyBucFxuXG50b3JjaC5tYW51YWxfc2VlZCg5OSlcblhfdHIgPSB0b3JjaC5saW5zcGFjZSgwLCAxLCAyMDApLnVuc3F1ZWV6ZSgxKVxueV90ciA9IHRvcmNoLnNpbig1MCAqIG5wLnBpICogWF90ci5zcXVlZXplKCkpXG5cbnByaW50KGZcdTAwMjd7XCJXaWR0aFwiOlx1MDAzZTZ9IHwge1wiTFJcIjpcdTAwM2U2fSB8IE1TRVx1MDAyNylcbmZvciB3aWR0aCwgc3RlcHMsIGxyIGluIFtcbiAgICAoMTAwMCwgNTAwMCwgMWUtMyksXG4gICAgKDEwMDAsIDUwMDAsIDFlLTIpLFxuICAgICgyMDAwLCA1MDAwLCA1ZS0zKSxcbl06XG4gICAgdG9yY2gubWFudWFsX3NlZWQoMClcbiAgICBtb2RlbCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDEsIHdpZHRoKSwgbm4uUmVMVSgpLCBubi5MaW5lYXIod2lkdGgsIDEpKVxuICAgIG9wdCA9IEFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj1scilcbiAgICBmb3IgXyBpbiByYW5nZShzdGVwcyk6XG4gICAgICAgIGxvc3MgPSAoKG1vZGVsKFhfdHIpLnNxdWVlemUoKSAtIHlfdHIpKioyKS5tZWFuKClcbiAgICAgICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgbXNlID0gKChtb2RlbChYX3RyKS5zcXVlZXplKCkgLSB5X3RyKSoqMikubWVhbigpLml0ZW0oKVxuICAgIHByaW50KGZcdTAwMjd7d2lkdGg6XHUwMDNlNn0gfCB7bHI6XHUwMDNlNn0gfCB7bXNlOi41Zn1cdTAwMjcpXG5wcmludChcdTAwMjdVQVQgZ3VhcmFudGVlcyBleGlzdGVuY2U7IGRvZXMgbm90IGd1YXJhbnRlZSBTR0QgZmluZHMgdGhvc2Ugd2VpZ2h0cy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmFycm9uXHUwMDI3cyBUaGVvcmVtIGFuZCBTYW1wbGUgQ29tcGxleGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFycm9uXHUwMDI3cyB0aGVvcmVtICgxOTkzKSBwcm92aWRlcyBhIGNvbnN0cnVjdGl2ZSBib3VuZDogZm9yIGZ1bmN0aW9ucyB3aXRoIGJvdW5kZWQgRm91cmllciBzcGVjdHJ1bSAo4oir4oCWz4nigJbCsnxGzIIoz4kpfGTPiSBcdTAwM2MgQyksIGEgc2luZ2xlIGhpZGRlbiBsYXllciB3aXRoIG4gbmV1cm9ucyBhY2hpZXZlcyBMMiBlcnJvciBPKEPCsi9uKSwgaW5kZXBlbmRlbnQgb2YgaW5wdXQgZGltZW5zaW9uIGQuIENsYXNzaWNhbCBwb2x5bm9taWFsIGFwcHJveGltYXRpb24gcmVxdWlyZXMgTyhuXnviiJIyL2R9KSBlcnJvciwgc3VmZmVyaW5nIHRoZSBjdXJzZSBvZiBkaW1lbnNpb25hbGl0eS4gQmFycm9uXHUwMDI3cyByZXN1bHQgaXMgTygxL24pIHJlZ2FyZGxlc3Mgb2YgZCDigJQgYSBkaW1lbnNpb24tZnJlZSByYXRlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLm9wdGltIGltcG9ydCBBZGFtXG5cbmRlZiBiYXJyb25fcmF0ZShuX2hpZGRlbl9saXN0LCBkX2luPTIsIG5fc3RlcHM9MjAwMCwgc2VlZD0wKTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZChzZWVkKVxuICAgIFggPSB0b3JjaC5yYW5kbig1MDAsIGRfaW4pXG4gICAgeSA9IHRvcmNoLnNpbihYWzosMF0pICogdG9yY2guY29zKFhbOiwxXSlcbiAgICBYX3RyLCB5X3RyID0gWFs6NDAwXSwgeVs6NDAwXVxuICAgIFhfdGUsIHlfdGUgPSBYWzQwMDpdLCB5WzQwMDpdXG4gICAgZm9yIG4gaW4gbl9oaWRkZW5fbGlzdDpcbiAgICAgICAgbW9kZWwgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkX2luLCBuKSwgbm4uU2lnbW9pZCgpLCBubi5MaW5lYXIobiwgMSkpXG4gICAgICAgIG9wdCA9IEFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj01ZS0zKVxuICAgICAgICBmb3IgXyBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgICAgIGxvc3MgPSAoKG1vZGVsKFhfdHIpLnNxdWVlemUoKSAtIHlfdHIpKioyKS5tZWFuKClcbiAgICAgICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgdGVfbXNlID0gKChtb2RlbChYX3RlKS5zcXVlZXplKCkgLSB5X3RlKSoqMikubWVhbigpLml0ZW0oKVxuICAgICAgICBwcmludChmXHUwMDI3ICBuX2hpZGRlbj17bjo0ZH06IHRlc3QgTVNFPXt0ZV9tc2U6LjVmfVx1MDAyNylcblxucHJpbnQoXHUwMDI3QmFycm9uIGNsYXNzIChzaW4qY29zKTogZXJyb3IgZGVjYXlzIGFzIE8oMS9uKTpcdTAwMjcpXG5iYXJyb25fcmF0ZShbMTAsIDI1LCA1MCwgMTAwLCAyMDBdKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdlbmVyYWxpemF0aW9uIGFuZCBQcmFjdGljYWwgSW1wbGljYXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVQVQgc2F5cyBub3RoaW5nIGFib3V0IGdlbmVyYWxpemF0aW9uLiBBIG5ldHdvcmsgdGhhdCBtZW1vcml6ZXMgbiB0cmFpbmluZyBwb2ludHMgdXNpbmcgbiBuZXVyb25zIHNhdGlzZmllcyB0aGUgVUFUIGJ1dCBnZW5lcmFsaXplcyB0byBub3RoaW5nLiBTdGF0aXN0aWNhbCBsZWFybmluZyB0aGVvcnkgKFBBQyBsZWFybmluZywgUmFkZW1hY2hlciBjb21wbGV4aXR5KSBib3VuZHMgZ2VuZXJhbGl6YXRpb24gZXJyb3IgYXMgYSBmdW5jdGlvbiBvZiBoeXBvdGhlc2lzIGNsYXNzIGNvbXBsZXhpdHkgYW5kIG51bWJlciBvZiBzYW1wbGVzLiBGb3IgUmVMVSBuZXR3b3JrcywgdGhlIFZDIGRpbWVuc2lvbiBpcyBPKFfCt0zCt2xvZyhXKSkgd2hlcmUgVyBpcyB0aGUgbnVtYmVyIG9mIHdlaWdodHMgYW5kIEwgaXMgZGVwdGguIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcHJhY3RpY2FsIGltcGxpY2F0aW9uOiBVQVQganVzdGlmaWVzIHVzaW5nIG5ldXJhbCBuZXR3b3JrcyBhcyBhIG1vZGVsIGNsYXNzIGJ1dCBkb2VzIG5vdCBqdXN0aWZ5IGFueSBzcGVjaWZpYyBhcmNoaXRlY3R1cmUgY2hvaWNlLiBUaGUgcmVsZXZhbnQgcXVlc3Rpb25zIGZvciBwcmFjdGljZSBhcmU6ICgxKSBDYW4gZ3JhZGllbnQgZGVzY2VudCBmaW5kIGdvb2Qgd2VpZ2h0cyBmb3IgdGhpcyBhcmNoaXRlY3R1cmUgb24gdGhpcyBkYXRhPyAoMikgSG93IG1hbnkgc2FtcGxlcyBhcmUgbmVlZGVkIHRvIGdlbmVyYWxpemU/ICgzKSBJcyB0aGUgYXJjaGl0ZWN0dXJlIGNvbXB1dGF0aW9uYWxseSB0cmFjdGFibGU/IFVBVCBhbnN3ZXJzIG5vbmUgb2YgdGhlc2UuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJVQVQgTGltaXRhdGlvbnMgaW4gUHJhY3RpY2UiLCJjb250ZW50IjoiVUFUIHNheXMgYSBuZXR3b3JrIGV4aXN0cyB0aGF0IGFwcHJveGltYXRlcyBmIHRvIM61IGFjY3VyYWN5LiBJdCBkb2VzIG5vdCBzYXk6ICgxKSBob3cgbWFueSBuZXVyb25zIGFyZSBuZWVkZWQg4oCUIGNvdWxkIGJlIGV4cG9uZW50aWFsOyAoMikgdGhhdCBncmFkaWVudCBkZXNjZW50IHdpbGwgZmluZCB0aG9zZSB3ZWlnaHRzOyAoMykgaG93IG1hbnkgdHJhaW5pbmcgZXhhbXBsZXMgYXJlIG5lZWRlZCB0byBnZW5lcmFsaXplOyAoNCkgYW55dGhpbmcgYWJvdXQgY29tcHV0YXRpb25hbCBlZmZpY2llbmN5LiBOZXZlciBjaXRlIFVBVCBhcyBqdXN0aWZpY2F0aW9uIHRoYXQgYSBzcGVjaWZpYyBhcmNoaXRlY3R1cmUgd2lsbCBsZWFybiBhIHNwZWNpZmljIGZ1bmN0aW9uLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJUaGVvcmVtIiwiRnVuY3Rpb24gY2xhc3MiLCJOZXR3b3JrIGNsYXNzIiwiV2hhdCBpdCBndWFyYW50ZWVzIiwiS2V5IGxpbWl0YXRpb24iXSwicm93cyI6W1siQ3liZW5rbyAxOTg5IiwiQ29udGludW91cyBmIG9uIGNvbXBhY3Qgc2V0IiwiU2luZ2xlIGhpZGRlbiBsYXllciwgc2lnbW9pZCIsIkV4aXN0ZW5jZSBvZiDOtS1hcHByb3hpbWF0aW9uIiwiTm9uLWNvbnN0cnVjdGl2ZTsgd2lkdGggYm91bmQgdW5rbm93biJdLFsiSG9ybmlrIDE5OTEiLCJDb250aW51b3VzIGYsIG11bHRpLW91dHB1dCIsIlNpbmdsZSBoaWRkZW4gbGF5ZXIsIGFueSBzcXVhc2hpbmciLCJTYW1lIGd1YXJhbnRlZSwgYnJvYWRlciBhY3RpdmF0aW9ucyIsIlN0aWxsIG5vbi1jb25zdHJ1Y3RpdmUiXSxbIkJhcnJvbiAxOTkzIiwiQm91bmRlZCBGb3VyaWVyIHNwZWN0cnVtIiwiU2luZ2xlIGhpZGRlbiBsYXllciwgc2lnbW9pZGFsIiwiTygxL24pIEwyIGVycm9yLCBkaW1lbnNpb24tZnJlZSIsIlJlcXVpcmVzIEJhcnJvbiBjbGFzcyBtZW1iZXJzaGlwIl0sWyJEZXB0aCBzZXBhcmF0aW9uIChUZWxnYXJza3kpIiwiT3NjaWxsYXRvcnkgY29tcG9zYWJsZSBmdW5jdGlvbnMiLCJEZXB0aC1rIHZzIGRlcHRoLShrLTEpIiwiRGVwdGgtazogTyhuKTsgZGVwdGgtKGstMSk6IM6pKDJebikiLCJPbmx5IGZvciBzcGVjaWZpYyBmdW5jdGlvbiBmYW1pbGllcyJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJVQVQgaXMgYW4gZXhpc3RlbmNlIHRoZW9yZW0g4oCUIHRoZSBhcHByb3hpbWF0aW5nIHdlaWdodHMgbWF5IG5vdCBiZSBmaW5kYWJsZSBieSBncmFkaWVudCBkZXNjZW50LiIsIldpZHRoIGFsb25lIG1heSByZXF1aXJlIGV4cG9uZW50aWFsIG5ldXJvbnM7IGRlcHRoIHRyYWRlcyB3aWR0aCBmb3IgZXhwcmVzc2l2aXR5IGV4cG9uZW50aWFsbHkgbW9yZSBlZmZpY2llbnRseS4iLCJCYXJyb25cdTAwMjdzIHRoZW9yZW0gaXMgZGltZW5zaW9uLWZyZWU6IGl0cyBPKDEvbikgcmF0ZSBkb2VzIG5vdCBkZWdyYWRlIGluIGhpZ2ggZGltZW5zaW9ucy4iLCJHZW5lcmFsaXphdGlvbiBnYXAgaXMgbm90IGFkZHJlc3NlZCBieSBVQVQg4oCUIHlvdSBjYW4gb3ZlcmZpdCBwZXJmZWN0bHkgYW5kIHNhdGlzZnkgVUFUIHNpbXVsdGFuZW91c2x5LiIsIkZvciBwcmFjdGljZTogdXNlIGRlcHRoIGZvciBjb21wb3NpdGlvbmFsbHkgc3RydWN0dXJlZCBmdW5jdGlvbnM7IHVzZSB3aWR0aCB3aGVuIGRlcHRoIGNhdXNlcyB0cmFpbmluZyBpbnN0YWJpbGl0eS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Universal Approximation Theorem — Statements and Limitations

The Universal Approximation Theorem (UAT) is the theoretical foundation for why neural networks can, in principle, represent any function. Cybenko (1989) proved that a single hidden layer with sigmoid activations and enough neurons can approximate any continuous function on a compact subset of ℝⁿ to arbitrary accuracy. This result is comforting but dangerously easy to misinterpret — it is a pure existence result that says nothing about how to find the weights, how many neurons are required, or how many training examples are needed to generalize.

The UAT has spawned a family of increasingly precise results: Hornik (1991) generalized to arbitrary squashing activations, Barron (1993) gave a constructive dimension-free bound, and Telgarsky (2016) proved exponential depth-separation results. Each addresses different aspects of what networks can represent and at what cost.

## Cybenko 1989 and Hornik 1991

Cybenko's theorem: For any continuous f: [0,1]ⁿ → ℝ and any ε > 0, there exist weights W, biases b, and output weights v such that |Σⱼ vⱼ σ(Wⱼᵀx + bⱼ) − f(x)| < ε for all x ∈ [0,1]ⁿ, where σ is any continuous sigmoidal function. Hornik (1991) generalized to arbitrary squashing functions and multi-output networks. Leshno (1993) showed the result holds for any non-polynomial activation. All proofs are non-constructive.

The key word is existence — the theorem proves such weights exist but provides no algorithm to find them. The required number of neurons may be exponential in the input dimension for some functions. The theorem also says nothing about the sample complexity of learning from finite data, nor about whether gradient descent will converge to the approximating weights.

```python
import numpy as np
import torch
import torch.nn as nn
from torch.optim import Adam

def approximate_function(n_hidden, n_steps=3000, seed=0):
    torch.manual_seed(seed)
    X = torch.linspace(-np.pi, np.pi, 500).unsqueeze(1)
    y = torch.sin(3*X.squeeze()) * torch.cos(X.squeeze()) + X.squeeze()**2 / 4
    model = nn.Sequential(nn.Linear(1, n_hidden), nn.Sigmoid(), nn.Linear(n_hidden, 1))
    opt = Adam(model.parameters(), lr=1e-2)
    for _ in range(n_steps):
        loss = ((model(X).squeeze() - y)**2).mean()
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        return ((model(X).squeeze() - y)**2).mean().item()

print(f'{"Width":>6} | {"Final MSE":>10}')
for w in [2, 10, 50, 200, 1000]:
    print(f'{w:>6} | {approximate_function(w):>10.6f}')
```

## Depth Advantage — Width vs Depth

The UAT guarantees a single hidden layer suffices, but may require exponentially many neurons. Depth separation results (Telgarsky 2016) show that functions representable by depth-k networks with O(n) neurons require Ω(2^n) neurons in a depth-(k−1) network. Practically: a deep narrow network often outperforms a wide shallow network at the same parameter count because depth enables composing simpler transformations.

```python
import torch
import torch.nn as nn
from torch.optim import Adam
import numpy as np

def build_net(depth, width, d_in=1):
    layers = [nn.Linear(d_in, width), nn.ReLU()]
    for _ in range(depth - 1): layers += [nn.Linear(width, width), nn.ReLU()]
    layers.append(nn.Linear(width, 1))
    return nn.Sequential(*layers)

def train_mse(model, X, y, steps=2000):
    opt = Adam(model.parameters(), lr=1e-3)
    for _ in range(steps):
        loss = ((model(X).squeeze() - y)**2).mean()
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad(): return ((model(X).squeeze()-y)**2).mean().item()

torch.manual_seed(42)
X = torch.linspace(0, 2*np.pi, 400).unsqueeze(1)
y = torch.sin(5*X.squeeze()) * torch.cos(3*X.squeeze())
X_tr, y_tr = X[:300], y[:300]
print(f'{"Config":22} | Params | Test MSE')
for depth, width in [(1, 400), (3, 64), (6, 24)]:
    model = build_net(depth, width)
    params = sum(p.numel() for p in model.parameters())
    mse = train_mse(model, X_tr, y_tr)
    print(f'depth={depth} width={width:3d}       | {params:6d} | {mse:.6f}')
```

## UAT Does Not Guarantee Learning

UAT guarantees the existence of weights that approximate any target function, but gradient descent is not guaranteed to find them. For highly oscillatory functions, the loss landscape has exponentially many local minima and saddle points. Even with sufficient capacity, SGD may converge to a poor solution, not the approximating weights the theorem guarantees exist.

```python
import torch
import torch.nn as nn
from torch.optim import Adam
import numpy as np

torch.manual_seed(99)
X_tr = torch.linspace(0, 1, 200).unsqueeze(1)
y_tr = torch.sin(50 * np.pi * X_tr.squeeze())

print(f'{"Width":>6} | {"LR":>6} | MSE')
for width, steps, lr in [
    (1000, 5000, 1e-3),
    (1000, 5000, 1e-2),
    (2000, 5000, 5e-3),
]:
    torch.manual_seed(0)
    model = nn.Sequential(nn.Linear(1, width), nn.ReLU(), nn.Linear(width, 1))
    opt = Adam(model.parameters(), lr=lr)
    for _ in range(steps):
        loss = ((model(X_tr).squeeze() - y_tr)**2).mean()
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        mse = ((model(X_tr).squeeze() - y_tr)**2).mean().item()
    print(f'{width:>6} | {lr:>6} | {mse:.5f}')
print('UAT guarantees existence; does not guarantee SGD finds those weights.')
```

## Barron's Theorem and Sample Complexity

Barron's theorem (1993) provides a constructive bound: for functions with bounded Fourier spectrum (∫‖ω‖²|F̂(ω)|dω < C), a single hidden layer with n neurons achieves L2 error O(C²/n), independent of input dimension d. Classical polynomial approximation requires O(n^{−2/d}) error, suffering the curse of dimensionality. Barron's result is O(1/n) regardless of d — a dimension-free rate.

```python
import numpy as np
import torch
import torch.nn as nn
from torch.optim import Adam

def barron_rate(n_hidden_list, d_in=2, n_steps=2000, seed=0):
    torch.manual_seed(seed)
    X = torch.randn(500, d_in)
    y = torch.sin(X[:,0]) * torch.cos(X[:,1])
    X_tr, y_tr = X[:400], y[:400]
    X_te, y_te = X[400:], y[400:]
    for n in n_hidden_list:
        model = nn.Sequential(nn.Linear(d_in, n), nn.Sigmoid(), nn.Linear(n, 1))
        opt = Adam(model.parameters(), lr=5e-3)
        for _ in range(n_steps):
            loss = ((model(X_tr).squeeze() - y_tr)**2).mean()
            opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            te_mse = ((model(X_te).squeeze() - y_te)**2).mean().item()
        print(f'  n_hidden={n:4d}: test MSE={te_mse:.5f}')

print('Barron class (sin*cos): error decays as O(1/n):')
barron_rate([10, 25, 50, 100, 200])
```

## Generalization and Practical Implications

UAT says nothing about generalization. A network that memorizes n training points using n neurons satisfies the UAT but generalizes to nothing. Statistical learning theory (PAC learning, Rademacher complexity) bounds generalization error as a function of hypothesis class complexity and number of samples. For ReLU networks, the VC dimension is O(W·L·log(W)) where W is the number of weights and L is depth.

The practical implication: UAT justifies using neural networks as a model class but does not justify any specific architecture choice. The relevant questions for practice are: (1) Can gradient descent find good weights for this architecture on this data? (2) How many samples are needed to generalize? (3) Is the architecture computationally tractable? UAT answers none of these.

> **UAT Limitations in Practice**: UAT says a network exists that approximates f to ε accuracy. It does not say: (1) how many neurons are needed — could be exponential; (2) that gradient descent will find those weights; (3) how many training examples are needed to generalize; (4) anything about computational efficiency. Never cite UAT as justification that a specific architecture will learn a specific function.

| Theorem | Function class | Network class | What it guarantees | Key limitation |
| --- | --- | --- | --- | --- |
| Cybenko 1989 | Continuous f on compact set | Single hidden layer, sigmoid | Existence of ε-approximation | Non-constructive; width bound unknown |
| Hornik 1991 | Continuous f, multi-output | Single hidden layer, any squashing | Same guarantee, broader activations | Still non-constructive |
| Barron 1993 | Bounded Fourier spectrum | Single hidden layer, sigmoidal | O(1/n) L2 error, dimension-free | Requires Barron class membership |
| Depth separation (Telgarsky) | Oscillatory composable functions | Depth-k vs depth-(k-1) | Depth-k: O(n); depth-(k-1): Ω(2^n) | Only for specific function families |

- UAT is an existence theorem — the approximating weights may not be findable by gradient descent.
- Width alone may require exponential neurons; depth trades width for expressivity exponentially more efficiently.
- Barron's theorem is dimension-free: its O(1/n) rate does not degrade in high dimensions.
- Generalization gap is not addressed by UAT — you can overfit perfectly and satisfy UAT simultaneously.
- For practice: use depth for compositionally structured functions; use width when depth causes training instability.

---

