---
title: "Adapter Merging — TIES, DARE, and Model Soup for Combining Fine-Tuned Models"
slug: "adapter-merging"
description: "Combine multiple fine-tuned models or adapters without additional training. Covers model soup weight averaging, TIES merging (trim, elect, disjoint merge), DARE random delta dropping, SLERP spherical interpolation, and LoRA merging in weight space."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9kZWwgbWVyZ2luZyBjb21iaW5lcyB0aGUgY2FwYWJpbGl0aWVzIG9mIG11bHRpcGxlIGZpbmUtdHVuZWQgbW9kZWxzIOKAlCBvciBhZGFwdGVycyDigJQgaW50byBhIHNpbmdsZSBtb2RlbCB3aXRob3V0IGFueSBhZGRpdGlvbmFsIHRyYWluaW5nLiBJbnN0ZWFkIG9mIG11bHRpLXRhc2sgdHJhaW5pbmcgZnJvbSBzY3JhdGNoLCB5b3Ugc3RhcnQgd2l0aCB0YXNrLXNwZWNpZmljIGZpbmUtdHVuZXMgYW5kIG1lcmdlIHRoZWlyIHdlaWdodHMuIFRoZSByZXN1bHRpbmcgbW9kZWwgaW5oZXJpdHMgY2FwYWJpbGl0aWVzIGZyb20gYWxsIHNvdXJjZSBtb2RlbHMgd2hpbGUgcmVxdWlyaW5nIG9ubHkgYSBzaW5nbGUgaW5mZXJlbmNlIGRlcGxveW1lbnQuIE1lcmdpbmcgaXMgZXNwZWNpYWxseSB1c2VmdWwgd2l0aCBMb1JBIGFkYXB0ZXJzOiB5b3UgY2FuIGZpbmUtdHVuZSBkb3plbnMgb2Ygc3BlY2lhbGl6YXRpb25zIGNoZWFwbHkgYW5kIG1lcmdlIHRoZSBiZXN0IHN1YnNldCBvbiBkZW1hbmQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IE1lcmdlIE1vZGVscyBJbnN0ZWFkIG9mIFRyYWluaW5nIE11bHRpLVRhc2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik11bHRpLXRhc2sgdHJhaW5pbmcgcmVxdWlyZXMgYWxsIHRhc2sgZGF0YSBzaW11bHRhbmVvdXNseSwgY2FyZWZ1bCBsb3NzIGJhbGFuY2luZywgYW5kIGlzIHByb25lIHRvIHRhc2sgaW50ZXJmZXJlbmNlIOKAlCB3aGVyZSBsZWFybmluZyBvbmUgdGFzayBkZWdyYWRlcyBhbm90aGVyLiBNZXJnaW5nIGF2b2lkcyB0aGVzZSBwcm9ibGVtczogZWFjaCBtb2RlbCBpcyB0cmFpbmVkIGluZGVwZW5kZW50bHkgdG8gaXRzIG9wdGltdW0sIHRoZW4gY29tYmluZWQuIFRoZSBtZXJnZWQgbW9kZWwgaXMgYWxzbyBlYXN5IHRvIHVwZGF0ZTogc3dhcCBvbmUgdGFza1x1MDAyN3MgZmluZS10dW5lIGZvciBhIG5ld2VyIHZlcnNpb24gYW5kIHJlLW1lcmdlIHJhdGhlciB0aGFuIHJlLXJ1bm5pbmcgdGhlIGVudGlyZSBtdWx0aS10YXNrIHBpcGVsaW5lLiBXZWlnaHQgaW50ZXJwb2xhdGlvbiDOuF9tZXJnZWQgPSDOoyDOseG1os644bWiIGlzIHRoZSBzaW1wbGVzdCBmb3JtLCB3aXRoIM6jIM6x4bWiID0gMSBlbnN1cmluZyB0aGUgbWVyZ2VkIG1vZGVsIHN0YXlzIGluIHRoZSBzYW1lIHdlaWdodCBtYWduaXR1ZGUgcmVnaW1lIGFzIHRoZSBvcmlnaW5hbHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9kZWwgU291cCDigJQgV2VpZ2h0IEF2ZXJhZ2luZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9kZWwgc291cCAoV29ydHNtYW4gZXQgYWwuLCAyMDIyKSBhdmVyYWdlcyB0aGUgd2VpZ2h0cyBvZiBtb2RlbHMgZmluZS10dW5lZCBmcm9tIHRoZSBzYW1lIHByZXRyYWluZWQgYmFzZSwgdHlwaWNhbGx5IHdpdGggZGlmZmVyZW50IGh5cGVycGFyYW1ldGVycyBvciBkYXRhIGF1Z21lbnRhdGlvbiBzZWVkcy4gVGhlIGF2ZXJhZ2Ugb3V0cGVyZm9ybXMgYW55IGluZGl2aWR1YWwgbW9kZWwgb24gdGhlIGhlbGQtb3V0IGV2YWx1YXRpb24sIGJlY2F1c2UgZGlmZmVyZW50IGZpbmUtdHVuZXMgZXhwbG9yZSBkaWZmZXJlbnQgbG9zcyBiYXNpbiByZWdpb25zIGFuZCB0aGVpciBhdmVyYWdlIGxhbmRzIGluIGEgZmxhdHRlciwgaGlnaGVyLWFjY3VyYWN5IGJhc2luLiBUaGUga2V5IGNvbnN0cmFpbnQgaXMgdGhhdCBhbGwgbW9kZWxzIG11c3QgYmUgZmluZS10dW5lZCBmcm9tIHRoZSBzYW1lIHByZXRyYWluZWQgY2hlY2twb2ludCDigJQgYXZlcmFnaW5nIHdlaWdodHMgZnJvbSBkaWZmZXJlbnQgaW5pdGlhbGl6YXRpb25zIHByb2R1Y2VzIGluY29oZXJlbnQgcmVzdWx0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBPcmRlcmVkRGljdFxuXG5kZWYgbW9kZWxfc291cChiYXNlX3N0YXRlX2RpY3QsIGZpbmV0dW5lZF9zdGF0ZV9kaWN0cywgd2VpZ2h0cz1Ob25lKTpcbiAgICBcIlwiXCJBdmVyYWdlIHdlaWdodHMgZnJvbSBtdWx0aXBsZSBmaW5lLXR1bmVkIG1vZGVscyAobW9kZWwgc291cCkuXCJcIlwiXG4gICAgbiA9IGxlbihmaW5ldHVuZWRfc3RhdGVfZGljdHMpXG4gICAgaWYgd2VpZ2h0cyBpcyBOb25lOlxuICAgICAgICB3ZWlnaHRzID0gWzEuMCAvIG5dICogblxuICAgIGFzc2VydCBhYnMoc3VtKHdlaWdodHMpIC0gMS4wKSBcdTAwM2MgMWUtNiwgXCJXZWlnaHRzIG11c3Qgc3VtIHRvIDFcIlxuICAgIHNvdXAgPSBPcmRlcmVkRGljdCgpXG4gICAgZm9yIGtleSBpbiBiYXNlX3N0YXRlX2RpY3Q6XG4gICAgICAgIHNvdXBba2V5XSA9IHN1bShcbiAgICAgICAgICAgIHcgKiBzZFtrZXldLmZsb2F0KCkgZm9yIHcsIHNkIGluIHppcCh3ZWlnaHRzLCBmaW5ldHVuZWRfc3RhdGVfZGljdHMpXG4gICAgICAgIClcbiAgICByZXR1cm4gc291cFxuXG4jIERlbW86IHNpbXVsYXRlIDMgZmluZS10dW5lZCBjaGVja3BvaW50cyBmcm9tIHNhbWUgcHJldHJhaW5lZCBiYXNlXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbmJhc2UgPSB7XCJlbmMud1wiOiB0b3JjaC56ZXJvcyg0LCA0KSwgXCJoZWFkLndcIjogdG9yY2guemVyb3MoNCl9XG5mdF9tb2RlbHMgPSBbXG4gICAge1wiZW5jLndcIjogYmFzZVtcImVuYy53XCJdICsgdG9yY2gucmFuZG4oNCwgNCkgKiAwLjEsXG4gICAgIFwiaGVhZC53XCI6IGJhc2VbXCJoZWFkLndcIl0gKyB0b3JjaC5yYW5kbig0KSAqIDAuMX1cbiAgICBmb3IgXyBpbiByYW5nZSgzKVxuXVxuc291cF9zZCA9IG1vZGVsX3NvdXAoYmFzZSwgZnRfbW9kZWxzKVxucHJpbnQoZlwiU291cCB3ZWlnaHQgbm9ybSAoZW5jKToge3NvdXBfc2RbXHUwMDI3ZW5jLndcdTAwMjddLm5vcm0oKTouNGZ9XCIpXG5mb3IgaSwgZnQgaW4gZW51bWVyYXRlKGZ0X21vZGVscyk6XG4gICAgcHJpbnQoZlwiTW9kZWwge2krMX0gd2VpZ2h0IG5vcm06IHtmdFtcdTAwMjdlbmMud1x1MDAyN10ubm9ybSgpOi40Zn1cIilcbnByaW50KFwiU291cCBhdmVyYWdlcyBhY3Jvc3MgYWxsIGZpbmUtdHVuZWQgY2hlY2twb2ludHMg4oCUIGxhbmRzIGluIGEgZmxhdHRlciBsb3NzIGJhc2luLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRJRVMgTWVyZ2luZyDigJQgVHJpbSwgRWxlY3QsIERpc2pvaW50IE1lcmdlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW1wbGUgd2VpZ2h0IGF2ZXJhZ2luZyBmYWlscyB3aGVuIG1vZGVscyBhcmUgZmluZS10dW5lZCBvbiB2ZXJ5IGRpZmZlcmVudCB0YXNrcywgYmVjYXVzZSBvcHBvc2luZyB3ZWlnaHQgdXBkYXRlcyBjYW5jZWwgZWFjaCBvdGhlciBvdXQg4oCUIGEgd2VpZ2h0IHB1c2hlZCBwb3NpdGl2ZSBieSB0YXNrIEEgYW5kIG5lZ2F0aXZlIGJ5IHRhc2sgQiBhdmVyYWdlcyB0byBuZWFyIHplcm8sIGxvc2luZyBib3RoIGNhcGFiaWxpdGllcy4gVElFUyBtZXJnaW5nIChZYWRhdiBldCBhbC4sIDIwMjMpIHNvbHZlcyB0aGlzIHdpdGggdGhyZWUgc3RlcHM6ICgxKSBUcmltIOKAlCBzZXQgdGFzayB2ZWN0b3IgZGVsdGFzIHdpdGggc21hbGwgbWFnbml0dWRlIHRvIHplcm8sIGtlZXBpbmcgb25seSB0aGUgdG9wLWslIGJ5IG1hZ25pdHVkZTsgKDIpIEVsZWN0IOKAlCBmb3IgZWFjaCBwYXJhbWV0ZXIsIGRldGVybWluZSB0aGUgZG9taW5hbnQgc2lnbiBhY3Jvc3MgYWxsIHRhc2sgdmVjdG9ycyBieSBtYWpvcml0eSB2b3RlOyAoMykgRGlzam9pbnQgTWVyZ2Ug4oCUIGF2ZXJhZ2Ugb25seSB0aGUgcGFyYW1ldGVycyB3aG9zZSBzaWduIGFncmVlcyB3aXRoIHRoZSBlbGVjdGVkIHNpZ24sIGV4Y2x1ZGluZyBjb25mbGljdGluZyB1cGRhdGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IE9yZGVyZWREaWN0XG5cbmRlZiB0aWVzX21lcmdlKHRhc2tfdmVjdG9ycywgYmFzZV9zdGF0ZV9kaWN0LCB0b3Bfaz0wLjIsIHNjYWxlPTEuMCk6XG4gICAgXCJcIlwiVElFUyBtZXJnaW5nOiBUcmltLCBFbGVjdCwgRGlzam9pbnQgTWVyZ2Ugb3ZlciB0YXNrIHZlY3RvciBkZWx0YXMuXCJcIlwiXG4gICAgbWVyZ2VkID0gT3JkZXJlZERpY3QoKVxuICAgIGZvciBrZXkgaW4gYmFzZV9zdGF0ZV9kaWN0OlxuICAgICAgICBkZWx0YXMgPSB0b3JjaC5zdGFjayhbdHZba2V5XS5mbG9hdCgpIGZvciB0diBpbiB0YXNrX3ZlY3RvcnNdLCBkaW09MCkgICMgKG4sIC4uLilcbiAgICAgICAgIyBTdGVwIDE6IFRyaW0g4oCUIHplcm8gb3V0IHNtYWxsIGRlbHRhcywga2VlcCB0b3AtayUgYnkgbWFnbml0dWRlXG4gICAgICAgIHRocmVzaG9sZCA9IGRlbHRhcy5hYnMoKS5xdWFudGlsZSgxLjAgLSB0b3BfaywgZGltPTAsIGtlZXBkaW09VHJ1ZSlcbiAgICAgICAgdHJpbW1lZCA9IHRvcmNoLndoZXJlKGRlbHRhcy5hYnMoKSBcdTAwM2U9IHRocmVzaG9sZCwgZGVsdGFzLCB0b3JjaC56ZXJvc19saWtlKGRlbHRhcykpXG4gICAgICAgICMgU3RlcCAyOiBFbGVjdCDigJQgbWFqb3JpdHkgdm90ZSBvbiBzaWduIHBlciBwYXJhbWV0ZXJcbiAgICAgICAgc2lnbl9zdW0gPSB0cmltbWVkLnNpZ24oKS5zdW0oZGltPTApXG4gICAgICAgIGVsZWN0ZWRfc2lnbiA9IHRvcmNoLndoZXJlKHNpZ25fc3VtIFx1MDAzZT0gMCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdG9yY2gub25lc19saWtlKHNpZ25fc3VtKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLXRvcmNoLm9uZXNfbGlrZShzaWduX3N1bSkpXG4gICAgICAgICMgU3RlcCAzOiBEaXNqb2ludCBNZXJnZSDigJQgYXZlcmFnZSBvbmx5IHBhcmFtZXRlcnMgdGhhdCBhZ3JlZSB3aXRoIGVsZWN0ZWQgc2lnblxuICAgICAgICBhZ3JlZSA9ICh0cmltbWVkLnNpZ24oKSA9PSBlbGVjdGVkX3NpZ24udW5zcXVlZXplKDApKSB8ICh0cmltbWVkID09IDApXG4gICAgICAgIGFncmVlZCA9IHRyaW1tZWQgKiBhZ3JlZS5mbG9hdCgpXG4gICAgICAgIG5fYWdyZWUgPSBhZ3JlZS5mbG9hdCgpLnN1bShkaW09MCkuY2xhbXAobWluPTEpXG4gICAgICAgIG1lcmdlZFtrZXldID0gYmFzZV9zdGF0ZV9kaWN0W2tleV0uZmxvYXQoKSArIHNjYWxlICogYWdyZWVkLnN1bShkaW09MCkgLyBuX2FncmVlXG4gICAgcmV0dXJuIG1lcmdlZFxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuYmFzZSA9IHtcIndcIjogdG9yY2guemVyb3MoNil9XG50dnMgPSBbe1wid1wiOiB0b3JjaC50ZW5zb3IoWzAuNSwgLTAuMywgMC4yLCAtMC4xLCAwLjQsIDAuMF0pfSxcbiAgICAgICB7XCJ3XCI6IHRvcmNoLnRlbnNvcihbLTAuMiwgMC40LCAwLjMsIDAuMiwgLTAuMSwgMC41XSl9LFxuICAgICAgIHtcIndcIjogdG9yY2gudGVuc29yKFswLjMsIDAuMSwgLTAuMiwgMC40LCAwLjMsIC0wLjJdKX1dXG5yZXN1bHQgPSB0aWVzX21lcmdlKHR2cywgYmFzZSwgdG9wX2s9MC41KVxucHJpbnQoZlwiVElFUyBtZXJnZWQ6IHtbcm91bmQodiwzKSBmb3IgdiBpbiByZXN1bHRbXHUwMDI3d1x1MDAyN10udG9saXN0KCldfVwiKVxucHJpbnQoXCJTaWduIGNvbmZsaWN0cyByZXNvbHZlZDsgZGVzdHJ1Y3RpdmUgaW50ZXJmZXJlbmNlIGVsaW1pbmF0ZWQuXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiREFSRSDigJQgUmFuZG9tIERlbHRhIERyb3BwaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEQVJFIChZdSBldCBhbC4sIDIwMjMpIGFkZHJlc3NlcyBpbnRlci1tb2RlbCBpbnRlcmZlcmVuY2UgYnkgcmFuZG9tbHkgZHJvcHBpbmcgdGFzayB2ZWN0b3IgZGVsdGFzIGJlZm9yZSBtZXJnaW5nIOKAlCBhbmFsb2dvdXMgdG8gZHJvcG91dCBhcHBsaWVkIHRvIHdlaWdodCBkaWZmZXJlbmNlcyByYXRoZXIgdGhhbiBhY3RpdmF0aW9ucy4gRWFjaCBkZWx0YSBlbGVtZW50IGlzIGRyb3BwZWQgaW5kZXBlbmRlbnRseSB3aXRoIHByb2JhYmlsaXR5IHAsIGFuZCBzdXJ2aXZpbmcgZWxlbWVudHMgYXJlIHJlc2NhbGVkIGJ5IDEvKDEtcCkgdG8gbWFpbnRhaW4gdGhlIGV4cGVjdGVkIG1hZ25pdHVkZS4gVGhpcyBzdG9jaGFzdGljIHBydW5pbmcgcmVkdWNlcyB0aGUgbnVtYmVyIG9mIGNvbmZsaWN0cyBiZXR3ZWVuIHRhc2sgdmVjdG9ycywgZXNwZWNpYWxseSBmb3IgcGFyYW1ldGVycyB3aGVyZSB0d28gbW9kZWxzIGxlYXJuZWQgb3Bwb3NpbmcgdXBkYXRlcy4gREFSRSBjYW4gYmUgY29tYmluZWQgd2l0aCBUSUVTIGZvciBmdXJ0aGVyIGltcHJvdmVtZW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IE9yZGVyZWREaWN0XG5cbmRlZiBkYXJlX21lcmdlKHRhc2tfdmVjdG9ycywgYmFzZV9zdGF0ZV9kaWN0LCBkcm9wX3JhdGU9MC41LCBzY2FsZT0xLjAsIHNlZWQ9NDIpOlxuICAgIFwiXCJcIkRBUkU6IHJhbmRvbWx5IGRyb3AgdGFzayB2ZWN0b3IgZGVsdGFzLCByZXNjYWxlLCBhcHBseSB0byBiYXNlIG1vZGVsLlwiXCJcIlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgbWVyZ2VkID0gT3JkZXJlZERpY3QoKVxuICAgIGZvciBrZXkgaW4gYmFzZV9zdGF0ZV9kaWN0OlxuICAgICAgICBkZWx0YXMgPSB0b3JjaC5zdGFjayhbdHZba2V5XS5mbG9hdCgpIGZvciB0diBpbiB0YXNrX3ZlY3RvcnNdLCBkaW09MClcbiAgICAgICAgIyBSYW5kb21seSBkcm9wIGVhY2ggZGVsdGEgZWxlbWVudCB3aXRoIHByb2JhYmlsaXR5IGRyb3BfcmF0ZVxuICAgICAgICBrZWVwX21hc2sgPSAodG9yY2gucmFuZF9saWtlKGRlbHRhcykgXHUwMDNlIGRyb3BfcmF0ZSkuZmxvYXQoKVxuICAgICAgICAjIFJlc2NhbGUgdG8gbWFpbnRhaW4gZXhwZWN0ZWQgbWFnbml0dWRlXG4gICAgICAgIHJlc2NhbGVkID0gZGVsdGFzICoga2VlcF9tYXNrIC8gKDEuMCAtIGRyb3BfcmF0ZSArIDFlLTgpXG4gICAgICAgIG1lcmdlZFtrZXldID0gYmFzZV9zdGF0ZV9kaWN0W2tleV0uZmxvYXQoKSArIHNjYWxlICogcmVzY2FsZWQubWVhbihkaW09MClcbiAgICByZXR1cm4gbWVyZ2VkXG5cbmJhc2UgPSB7XCJ3XCI6IHRvcmNoLnplcm9zKDgpfVxudHZzID0gW1xuICAgIHtcIndcIjogdG9yY2gudGVuc29yKFswLjQsIC0wLjMsIDAuNSwgLTAuMiwgMC4xLCAwLjYsIC0wLjQsIDAuM10pfSxcbiAgICB7XCJ3XCI6IHRvcmNoLnRlbnNvcihbLTAuMiwgMC41LCAtMC4zLCAwLjQsIC0wLjUsIDAuMiwgMC4zLCAtMC4xXSl9LFxuXVxuZm9yIGRyb3AgaW4gWzAuMCwgMC4zLCAwLjUsIDAuN106XG4gICAgcmVzdWx0ID0gZGFyZV9tZXJnZSh0dnMsIGJhc2UsIGRyb3BfcmF0ZT1kcm9wKVxuICAgIHByaW50KGZcImRyb3BfcmF0ZT17ZHJvcDouMWZ9OiBtZXJnZWQgbm9ybT17cmVzdWx0W1x1MDAyN3dcdTAwMjddLm5vcm0oKTouNGZ9ICBcIlxuICAgICAgICAgIGZcInZhbHVlcz17W3JvdW5kKHYsMikgZm9yIHYgaW4gcmVzdWx0W1x1MDAyN3dcdTAwMjddLnRvbGlzdCgpXX1cIilcbnByaW50KFwiREFSRSByZWR1Y2VzIGludGVyZmVyZW5jZTsgaGlnaGVyIGRyb3BfcmF0ZSBtZWFucyBtb3JlIHJlZ3VsYXJpemF0aW9uLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNMRVJQIOKAlCBTcGhlcmljYWwgTGluZWFyIEludGVycG9sYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxpbmVhciBpbnRlcnBvbGF0aW9uIGJldHdlZW4gdHdvIG1vZGVsIHdlaWdodCBzZXRzIChMRVJQKSB0cmF2ZWxzIGluIGEgc3RyYWlnaHQgbGluZSB0aHJvdWdoIHBhcmFtZXRlciBzcGFjZSwgcG90ZW50aWFsbHkgcGFzc2luZyB0aHJvdWdoIGxvdy1xdWFsaXR5IHJlZ2lvbnMgbmVhciB0aGUgY2VudGVyLiBTTEVSUCAoU3BoZXJpY2FsIExpbmVhciBJbnRlcnBvbGF0aW9uKSBpbnRlcnBvbGF0ZXMgYWxvbmcgdGhlIGdlb2Rlc2ljIG9uIHRoZSB1bml0IHNwaGVyZTogaXQgbWFpbnRhaW5zIGNvbnN0YW50IGFuZ3VsYXIgdmVsb2NpdHkgYW5kIGNvbnN0YW50IG1hZ25pdHVkZSBhbG9uZyB0aGUgaW50ZXJwb2xhdGlvbiBwYXRoLiBGb3IgdHdvIG1vZGVscyDOuOKCgSBhbmQgzrjigoIgd2l0aCBhbmdsZSDPiSBiZXR3ZWVuIHRoZW0sIFNMRVJQIGF0IGludGVycG9sYXRpb24gcGFyYW1ldGVyIHQgcmV0dXJucyBzaW4oKDEtdCnPiSkvc2luKM+JKSDCtyDOuOKCgSArIHNpbih0z4kpL3NpbijPiSkgwrcgzrjigoIuIFdoZW4gz4kg4omIIDAgKG5lYXJseSBwYXJhbGxlbCksIFNMRVJQIGRlZ2VuZXJhdGVzIHRvIExFUlAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgT3JkZXJlZERpY3RcblxuZGVmIHNsZXJwKHRoZXRhMSwgdGhldGEyLCB0PTAuNSk6XG4gICAgXCJcIlwiU3BoZXJpY2FsIExpbmVhciBJbnRlcnBvbGF0aW9uIGJldHdlZW4gdHdvIG1vZGVsIHdlaWdodCBzZXRzLlwiXCJcIlxuICAgIG1lcmdlZCA9IE9yZGVyZWREaWN0KClcbiAgICBmb3Iga2V5IGluIHRoZXRhMTpcbiAgICAgICAgdjAgPSB0aGV0YTFba2V5XS5mbG9hdCgpLmZsYXR0ZW4oKVxuICAgICAgICB2MSA9IHRoZXRhMltrZXldLmZsb2F0KCkuZmxhdHRlbigpXG4gICAgICAgIHYwX25vcm0gPSB2MCAvICh2MC5ub3JtKCkgKyAxZS04KVxuICAgICAgICB2MV9ub3JtID0gdjEgLyAodjEubm9ybSgpICsgMWUtOClcbiAgICAgICAgZG90ID0gdG9yY2guY2xhbXAoKHYwX25vcm0gKiB2MV9ub3JtKS5zdW0oKSwgLTEuMCwgMS4wKVxuICAgICAgICBvbWVnYSA9IHRvcmNoLmFjb3MoZG90KVxuICAgICAgICBpZiBvbWVnYS5hYnMoKSBcdTAwM2MgMWUtNjpcbiAgICAgICAgICAgICMgVmVjdG9ycyBuZWFybHkgcGFyYWxsZWw6IGZhbGwgYmFjayB0byBsaW5lYXIgaW50ZXJwb2xhdGlvblxuICAgICAgICAgICAgbWVyZ2VkW2tleV0gPSAoKDEgLSB0KSAqIHRoZXRhMVtrZXldLmZsb2F0KCkgKyB0ICogdGhldGEyW2tleV0uZmxvYXQoKSlcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIHMgPSB0b3JjaC5zaW4ob21lZ2EpXG4gICAgICAgICAgICBtZXJnZWRba2V5XSA9IChcbiAgICAgICAgICAgICAgICAodG9yY2guc2luKCgxIC0gdCkgKiBvbWVnYSkgLyBzKSAqIHYwICtcbiAgICAgICAgICAgICAgICAodG9yY2guc2luKHQgKiBvbWVnYSkgLyBzKSAqIHYxXG4gICAgICAgICAgICApLnJlc2hhcGUodGhldGExW2tleV0uc2hhcGUpXG4gICAgcmV0dXJuIG1lcmdlZFxuXG50b3JjaC5tYW51YWxfc2VlZCgxKVxubTEgPSB7XCJlbmNcIjogdG9yY2gucmFuZG4oNCwgNCksIFwiaGVhZFwiOiB0b3JjaC5yYW5kbigyLCA0KX1cbm0yID0ge1wiZW5jXCI6IHRvcmNoLnJhbmRuKDQsIDQpLCBcImhlYWRcIjogdG9yY2gucmFuZG4oMiwgNCl9XG5mb3IgdF92YWwgaW4gWzAuMCwgMC4yNSwgMC41LCAwLjc1LCAxLjBdOlxuICAgIGJsZW5kZWQgPSBzbGVycChtMSwgbTIsIHQ9dF92YWwpXG4gICAgZW5jX25vcm0gPSBibGVuZGVkW1wiZW5jXCJdLm5vcm0oKS5pdGVtKClcbiAgICBwcmludChmXCJ0PXt0X3ZhbH06IGVuY19ub3JtPXtlbmNfbm9ybTouNGZ9XCIpXG5wcmludChcIlNMRVJQIHRyYWNlcyBjb25zdGFudC1zcGVlZCBwYXRoIG9uIHVuaXQgc3BoZXJlOyBMRVJQIGN1dHMgdGhyb3VnaCBjZW50ZXIuXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9SQSBNZXJnaW5nIGluIFdlaWdodCBTcGFjZSB2cyBBZGFwdGVyIFNwYWNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMb1JBIGFkYXB0ZXJzIGNhbiBiZSBtZXJnZWQgYXQgdHdvIGxldmVscy4gSW4gYWRhcHRlciBzcGFjZSwgdGhlIExvUkEgbWF0cmljZXMgQSBhbmQgQiBhcmUgYXZlcmFnZWQgb3IgY29tYmluZWQgYmVmb3JlIGNvbXB1dGluZyB0aGUgdXBkYXRlIM6UIFcgPSBCQS4gSW4gd2VpZ2h0IHNwYWNlLCBlYWNoIGFkYXB0ZXJcdTAwMjdzIGZ1bGwgd2VpZ2h0IHVwZGF0ZSDOlCBX4bWiID0gQuG1okHhtaIgaXMgY29tcHV0ZWQgZmlyc3QsIHRoZW4gdGhlIGZ1bGwtcmFuayB1cGRhdGVzIGFyZSBtZXJnZWQgKGUuZy4sIHZpYSBUSUVTIG9yIERBUkUpLiBXZWlnaHQtc3BhY2UgbWVyZ2luZyBpcyBtb3JlIGZsZXhpYmxlIOKAlCB5b3UgY2FuIGFwcGx5IGFueSBtZXJnaW5nIGFsZ29yaXRobSDigJQgYnV0IGxvc2VzIHRoZSBsb3ctcmFuayBzdHJ1Y3R1cmUuIEFkYXB0ZXItc3BhY2UgbWVyZ2luZyBwcmVzZXJ2ZXMgbG93IHJhbmsgYnV0IGlzIGxpbWl0ZWQgdG8gbWV0aG9kcyB0aGF0IG9wZXJhdGUgb24gdGhlIGZhY3RvcmVkIG1hdHJpY2VzLiBGb3IgdGFzayBhcml0aG1ldGljIGFuZCBUSUVTL0RBUkUsIHdlaWdodC1zcGFjZSBtZXJnaW5nIGlzIHN0YW5kYXJkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBHdWlkZWxpbmVzIGFuZCBNZXRob2QgQ29tcGFyaXNvbiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTW9kZWwgc291cDogdXNlIHdoZW4gbWVyZ2luZyBjaGVja3BvaW50cyBmcm9tIHRoZSBzYW1lIHRyYWluaW5nIHJ1biB3aXRoIGRpZmZlcmVudCBoeXBlcnBhcmFtZXRlcnMgb3IgZGF0YSBzZWVkcy4iLCJUSUVTOiBwcmVmZXJyZWQgd2hlbiBtZXJnaW5nIG1vZGVscyBmaW5lLXR1bmVkIG9uIHZlcnkgZGlmZmVyZW50IHRhc2tzIOKAlCBzaWduIGNvbmZsaWN0IHJlc29sdXRpb24gcHJldmVudHMgZGVzdHJ1Y3RpdmUgaW50ZXJmZXJlbmNlLiIsIkRBUkU6IGFkZCB3aGVuIG1lcmdpbmcgbWFueSBtb2RlbHMgKDQrKTsgdGhlIHJhbmRvbSBkcm9wcGluZyByZWR1Y2VzIHBhaXJ3aXNlIGludGVyZmVyZW5jZSB3aXRob3V0IG5lZWRpbmcgZXhwbGljaXQgc2lnbiByZXNvbHV0aW9uLiIsIlNMRVJQOiBiZXN0IGZvciBtZXJnaW5nIGV4YWN0bHkgdHdvIG1vZGVscyB3aGVuIG1hZ25pdHVkZSBwcmVzZXJ2YXRpb24gbWF0dGVycyAoZS5nLiwgaW5zdHJ1Y3Rpb24tdHVuZWQgKyBEUE8tdHVuZWQgdmVyc2lvbnMpLiIsIlRhc2sgYXJpdGhtZXRpYzogdXNlIHdoZW4geW91IHdhbnQgYWRkaXRpdmUgY29tcG9zaXRpb24g4oCUIGVhY2ggdGFzayB2ZWN0b3IgY29udHJpYnV0ZXMgaW5kZXBlbmRlbnRseSB3aXRoIGEgdHVuYWJsZSBzY2FsZSDOuy4iLCJBbGwgbWV0aG9kcyByZXF1aXJlIGZpbmUtdHVuaW5nIGZyb20gdGhlIHNhbWUgcHJldHJhaW5lZCBiYXNlIHRvIGF2b2lkIGNhdGFzdHJvcGhpYyBpbnRlcmZlcmVuY2UgZnJvbSBtaXNtYXRjaGVkIGZlYXR1cmUgc3BhY2VzLiJdfSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQ29uZmxpY3QgUmVzb2x1dGlvbiIsIlBhcmFtZXRlciBDb3VudCIsIlF1YWxpdHkgdnMgSW5kaXZpZHVhbCIsIkNvbXB1dGUgQ29zdCIsIkJlc3QgRm9yIl0sInJvd3MiOltbIk1vZGVsIFNvdXAiLCJOb25lIChzaW1wbGUgYXZlcmFnZSkiLCJTYW1lIGFzIG9uZSBtb2RlbCIsIkJldHRlciAoZmxhdHRlciBiYXNpbikiLCJUcml2aWFsIOKAlCBvbmUgcGFzcyIsIlNhbWUtdGFzayBoeXBlcnBhcmFtZXRlciBlbnNlbWJsaW5nIl0sWyJUYXNrIEFyaXRobWV0aWMiLCJOb25lIChhZGRpdGl2ZSkiLCJTYW1lIGFzIG9uZSBtb2RlbCIsIkNvbXBhcmFibGUgYXQgbG93IHNjYWxlIiwiVHJpdmlhbCDigJQgdmVjdG9yIGFkZCIsIkFkZGl0aXZlIG11bHRpLXRhc2sgY29tcG9zaXRpb24iXSxbIlRJRVMiLCJTaWduIG1ham9yaXR5IHZvdGUgcGVyIHBhcmFtIiwiU2FtZSBhcyBvbmUgbW9kZWwiLCJCZXR0ZXIgdGhhbiBzb3VwIGZvciBjcm9zcy10YXNrIiwiTG93IOKAlCBvbmUgdHJpbW1pbmcgcGFzcyIsIkRpZmZlcmVudC10YXNrIG1lcmdpbmcsIHVwIHRvIH44IG1vZGVscyJdLFsiREFSRSIsIlN0b2NoYXN0aWMgZHJvcCArIHJlc2NhbGUiLCJTYW1lIGFzIG9uZSBtb2RlbCIsIkdvb2QgZm9yIG1hbnkgbW9kZWxzIiwiTG93IOKAlCByYW5kb20gbWFzayIsIk1lcmdpbmcgNCsgbW9kZWxzLCBoaWdoIGludGVyZmVyZW5jZSJdLFsiU0xFUlAiLCJOb25lIChnZW9kZXNpYyBwYXRoKSIsIlNhbWUgYXMgb25lIG1vZGVsIiwiQmVzdCBmb3IgMi1tb2RlbCBibGVuZCIsIkxvdyDigJQgcGVyLWxheWVyIHRyaWciLCJUd28tbW9kZWwgaW50ZXJwb2xhdGlvbiwgbWFnbml0dWRlLXNlbnNpdGl2ZSJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlRJRVMgT3V0cGVyZm9ybXMgU2ltcGxlIEF2ZXJhZ2luZyBmb3IgQ3Jvc3MtVGFzayBNZXJnaW5nIiwiY29udGVudCI6IlRJRVMgbWVyZ2luZyBvdXRwZXJmb3JtcyBzaW1wbGUgd2VpZ2h0IGF2ZXJhZ2luZyB3aGVuIG1lcmdpbmcgbW9kZWxzIGZpbmUtdHVuZWQgb24gdmVyeSBkaWZmZXJlbnQgdGFza3Mg4oCUIHRoZSBzaWduIGNvbmZsaWN0IHJlc29sdXRpb24gc3RlcCBwcmV2ZW50cyBkZXN0cnVjdGl2ZSBpbnRlcmZlcmVuY2UgYmV0d2VlbiBvcHBvc2luZyB3ZWlnaHQgdXBkYXRlcyB0aGF0IGRlZ3JhZGUgYm90aCB0YXNrcy4gVXNlIHRvcC1rPTAuMiAoa2VlcCAyMCUgb2YgZGVsdGFzKSBhcyBhIHN0YXJ0aW5nIHBvaW50OyBsYXJnZXIgayByZXRhaW5zIG1vcmUgdGFzayBzaWduYWwgYnV0IGluY3JlYXNlcyBpbnRlcmZlcmVuY2UuIEZvciBMb1JBIG1lcmdpbmcsIG1lcmdlIGluIHdlaWdodCBzcGFjZSAoY29tcHV0ZSBCQSBmaXJzdCkgc28gVElFUyBjYW4gc2VlIHRoZSBmdWxsLXJhbmsgdXBkYXRlcy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Adapter Merging — TIES, DARE, and Model Soup for Combining Fine-Tuned Models

Model merging combines the capabilities of multiple fine-tuned models — or adapters — into a single model without any additional training. Instead of multi-task training from scratch, you start with task-specific fine-tunes and merge their weights. The resulting model inherits capabilities from all source models while requiring only a single inference deployment. Merging is especially useful with LoRA adapters: you can fine-tune dozens of specializations cheaply and merge the best subset on demand.

## Why Merge Models Instead of Training Multi-Task

Multi-task training requires all task data simultaneously, careful loss balancing, and is prone to task interference — where learning one task degrades another. Merging avoids these problems: each model is trained independently to its optimum, then combined. The merged model is also easy to update: swap one task's fine-tune for a newer version and re-merge rather than re-running the entire multi-task pipeline. Weight interpolation θ_merged = Σ αᵢθᵢ is the simplest form, with Σ αᵢ = 1 ensuring the merged model stays in the same weight magnitude regime as the originals.

## Model Soup — Weight Averaging

Model soup (Wortsman et al., 2022) averages the weights of models fine-tuned from the same pretrained base, typically with different hyperparameters or data augmentation seeds. The average outperforms any individual model on the held-out evaluation, because different fine-tunes explore different loss basin regions and their average lands in a flatter, higher-accuracy basin. The key constraint is that all models must be fine-tuned from the same pretrained checkpoint — averaging weights from different initializations produces incoherent results.

```python
import torch
from collections import OrderedDict

def model_soup(base_state_dict, finetuned_state_dicts, weights=None):
    """Average weights from multiple fine-tuned models (model soup)."""
    n = len(finetuned_state_dicts)
    if weights is None:
        weights = [1.0 / n] * n
    assert abs(sum(weights) - 1.0) < 1e-6, "Weights must sum to 1"
    soup = OrderedDict()
    for key in base_state_dict:
        soup[key] = sum(
            w * sd[key].float() for w, sd in zip(weights, finetuned_state_dicts)
        )
    return soup

# Demo: simulate 3 fine-tuned checkpoints from same pretrained base
torch.manual_seed(42)
base = {"enc.w": torch.zeros(4, 4), "head.w": torch.zeros(4)}
ft_models = [
    {"enc.w": base["enc.w"] + torch.randn(4, 4) * 0.1,
     "head.w": base["head.w"] + torch.randn(4) * 0.1}
    for _ in range(3)
]
soup_sd = model_soup(base, ft_models)
print(f"Soup weight norm (enc): {soup_sd['enc.w'].norm():.4f}")
for i, ft in enumerate(ft_models):
    print(f"Model {i+1} weight norm: {ft['enc.w'].norm():.4f}")
print("Soup averages across all fine-tuned checkpoints — lands in a flatter loss basin.")
```

## TIES Merging — Trim, Elect, Disjoint Merge

Simple weight averaging fails when models are fine-tuned on very different tasks, because opposing weight updates cancel each other out — a weight pushed positive by task A and negative by task B averages to near zero, losing both capabilities. TIES merging (Yadav et al., 2023) solves this with three steps: (1) Trim — set task vector deltas with small magnitude to zero, keeping only the top-k% by magnitude; (2) Elect — for each parameter, determine the dominant sign across all task vectors by majority vote; (3) Disjoint Merge — average only the parameters whose sign agrees with the elected sign, excluding conflicting updates.

```python
import torch
from collections import OrderedDict

def ties_merge(task_vectors, base_state_dict, top_k=0.2, scale=1.0):
    """TIES merging: Trim, Elect, Disjoint Merge over task vector deltas."""
    merged = OrderedDict()
    for key in base_state_dict:
        deltas = torch.stack([tv[key].float() for tv in task_vectors], dim=0)  # (n, ...)
        # Step 1: Trim — zero out small deltas, keep top-k% by magnitude
        threshold = deltas.abs().quantile(1.0 - top_k, dim=0, keepdim=True)
        trimmed = torch.where(deltas.abs() >= threshold, deltas, torch.zeros_like(deltas))
        # Step 2: Elect — majority vote on sign per parameter
        sign_sum = trimmed.sign().sum(dim=0)
        elected_sign = torch.where(sign_sum >= 0,
                                   torch.ones_like(sign_sum),
                                   -torch.ones_like(sign_sum))
        # Step 3: Disjoint Merge — average only parameters that agree with elected sign
        agree = (trimmed.sign() == elected_sign.unsqueeze(0)) | (trimmed == 0)
        agreed = trimmed * agree.float()
        n_agree = agree.float().sum(dim=0).clamp(min=1)
        merged[key] = base_state_dict[key].float() + scale * agreed.sum(dim=0) / n_agree
    return merged

torch.manual_seed(0)
base = {"w": torch.zeros(6)}
tvs = [{"w": torch.tensor([0.5, -0.3, 0.2, -0.1, 0.4, 0.0])},
       {"w": torch.tensor([-0.2, 0.4, 0.3, 0.2, -0.1, 0.5])},
       {"w": torch.tensor([0.3, 0.1, -0.2, 0.4, 0.3, -0.2])}]
result = ties_merge(tvs, base, top_k=0.5)
print(f"TIES merged: {[round(v,3) for v in result['w'].tolist()]}")
print("Sign conflicts resolved; destructive interference eliminated.")
```

## DARE — Random Delta Dropping

DARE (Yu et al., 2023) addresses inter-model interference by randomly dropping task vector deltas before merging — analogous to dropout applied to weight differences rather than activations. Each delta element is dropped independently with probability p, and surviving elements are rescaled by 1/(1-p) to maintain the expected magnitude. This stochastic pruning reduces the number of conflicts between task vectors, especially for parameters where two models learned opposing updates. DARE can be combined with TIES for further improvement.

```python
import torch
from collections import OrderedDict

def dare_merge(task_vectors, base_state_dict, drop_rate=0.5, scale=1.0, seed=42):
    """DARE: randomly drop task vector deltas, rescale, apply to base model."""
    torch.manual_seed(seed)
    merged = OrderedDict()
    for key in base_state_dict:
        deltas = torch.stack([tv[key].float() for tv in task_vectors], dim=0)
        # Randomly drop each delta element with probability drop_rate
        keep_mask = (torch.rand_like(deltas) > drop_rate).float()
        # Rescale to maintain expected magnitude
        rescaled = deltas * keep_mask / (1.0 - drop_rate + 1e-8)
        merged[key] = base_state_dict[key].float() + scale * rescaled.mean(dim=0)
    return merged

base = {"w": torch.zeros(8)}
tvs = [
    {"w": torch.tensor([0.4, -0.3, 0.5, -0.2, 0.1, 0.6, -0.4, 0.3])},
    {"w": torch.tensor([-0.2, 0.5, -0.3, 0.4, -0.5, 0.2, 0.3, -0.1])},
]
for drop in [0.0, 0.3, 0.5, 0.7]:
    result = dare_merge(tvs, base, drop_rate=drop)
    print(f"drop_rate={drop:.1f}: merged norm={result['w'].norm():.4f}  "
          f"values={[round(v,2) for v in result['w'].tolist()]}")
print("DARE reduces interference; higher drop_rate means more regularization.")
```

## SLERP — Spherical Linear Interpolation

Linear interpolation between two model weight sets (LERP) travels in a straight line through parameter space, potentially passing through low-quality regions near the center. SLERP (Spherical Linear Interpolation) interpolates along the geodesic on the unit sphere: it maintains constant angular velocity and constant magnitude along the interpolation path. For two models θ₁ and θ₂ with angle ω between them, SLERP at interpolation parameter t returns sin((1-t)ω)/sin(ω) · θ₁ + sin(tω)/sin(ω) · θ₂. When ω ≈ 0 (nearly parallel), SLERP degenerates to LERP.

```python
import torch
from collections import OrderedDict

def slerp(theta1, theta2, t=0.5):
    """Spherical Linear Interpolation between two model weight sets."""
    merged = OrderedDict()
    for key in theta1:
        v0 = theta1[key].float().flatten()
        v1 = theta2[key].float().flatten()
        v0_norm = v0 / (v0.norm() + 1e-8)
        v1_norm = v1 / (v1.norm() + 1e-8)
        dot = torch.clamp((v0_norm * v1_norm).sum(), -1.0, 1.0)
        omega = torch.acos(dot)
        if omega.abs() < 1e-6:
            # Vectors nearly parallel: fall back to linear interpolation
            merged[key] = ((1 - t) * theta1[key].float() + t * theta2[key].float())
        else:
            s = torch.sin(omega)
            merged[key] = (
                (torch.sin((1 - t) * omega) / s) * v0 +
                (torch.sin(t * omega) / s) * v1
            ).reshape(theta1[key].shape)
    return merged

torch.manual_seed(1)
m1 = {"enc": torch.randn(4, 4), "head": torch.randn(2, 4)}
m2 = {"enc": torch.randn(4, 4), "head": torch.randn(2, 4)}
for t_val in [0.0, 0.25, 0.5, 0.75, 1.0]:
    blended = slerp(m1, m2, t=t_val)
    enc_norm = blended["enc"].norm().item()
    print(f"t={t_val}: enc_norm={enc_norm:.4f}")
print("SLERP traces constant-speed path on unit sphere; LERP cuts through center.")
```

## LoRA Merging in Weight Space vs Adapter Space

LoRA adapters can be merged at two levels. In adapter space, the LoRA matrices A and B are averaged or combined before computing the update Δ W = BA. In weight space, each adapter's full weight update Δ Wᵢ = BᵢAᵢ is computed first, then the full-rank updates are merged (e.g., via TIES or DARE). Weight-space merging is more flexible — you can apply any merging algorithm — but loses the low-rank structure. Adapter-space merging preserves low rank but is limited to methods that operate on the factored matrices. For task arithmetic and TIES/DARE, weight-space merging is standard.

## Practical Guidelines and Method Comparison

- Model soup: use when merging checkpoints from the same training run with different hyperparameters or data seeds.
- TIES: preferred when merging models fine-tuned on very different tasks — sign conflict resolution prevents destructive interference.
- DARE: add when merging many models (4+); the random dropping reduces pairwise interference without needing explicit sign resolution.
- SLERP: best for merging exactly two models when magnitude preservation matters (e.g., instruction-tuned + DPO-tuned versions).
- Task arithmetic: use when you want additive composition — each task vector contributes independently with a tunable scale λ.
- All methods require fine-tuning from the same pretrained base to avoid catastrophic interference from mismatched feature spaces.

| Method | Conflict Resolution | Parameter Count | Quality vs Individual | Compute Cost | Best For |
| --- | --- | --- | --- | --- | --- |
| Model Soup | None (simple average) | Same as one model | Better (flatter basin) | Trivial — one pass | Same-task hyperparameter ensembling |
| Task Arithmetic | None (additive) | Same as one model | Comparable at low scale | Trivial — vector add | Additive multi-task composition |
| TIES | Sign majority vote per param | Same as one model | Better than soup for cross-task | Low — one trimming pass | Different-task merging, up to ~8 models |
| DARE | Stochastic drop + rescale | Same as one model | Good for many models | Low — random mask | Merging 4+ models, high interference |
| SLERP | None (geodesic path) | Same as one model | Best for 2-model blend | Low — per-layer trig | Two-model interpolation, magnitude-sensitive |

> **TIES Outperforms Simple Averaging for Cross-Task Merging**: TIES merging outperforms simple weight averaging when merging models fine-tuned on very different tasks — the sign conflict resolution step prevents destructive interference between opposing weight updates that degrade both tasks. Use top-k=0.2 (keep 20% of deltas) as a starting point; larger k retains more task signal but increases interference. For LoRA merging, merge in weight space (compute BA first) so TIES can see the full-rank updates.

---

