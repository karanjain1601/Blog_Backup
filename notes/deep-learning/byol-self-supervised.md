---
title: "BYOL — Bootstrap Your Own Latent Without Negatives"
slug: "byol-self-supervised"
description: "BYOL (Grill et al. 2020) eliminates the need for negative samples in self-supervised learning by using an asymmetric online-target architecture where only the online network has a predictor and the target network is an EMA copy, with stop-gradient preventing collapse."
tags: ["deep-learning", "self-supervised-learning", "contrastive-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQllPTCAoQm9vdHN0cmFwIFlvdXIgT3duIExhdGVudCwgR3JpbGwgZXQgYWwuIDIwMjApIHdhcyBhIGxhbmRtYXJrIHJlc3VsdCBiZWNhdXNlIGl0IGFjaGlldmVkIHN0YXRlLW9mLXRoZS1hcnQgc2VsZi1zdXBlcnZpc2VkIHJlcHJlc2VudGF0aW9uIGxlYXJuaW5nIHdpdGhvdXQgYW55IG5lZ2F0aXZlIHNhbXBsZXMuIFRoZSBjb252ZW50aW9uYWwgd2lzZG9tIHdhcyB0aGF0IG5lZ2F0aXZlcyBhcmUgZXNzZW50aWFsIHRvIHByZXZlbnQgY29sbGFwc2Ug4oCUIGEgZGVnZW5lcmF0ZSBzb2x1dGlvbiB3aGVyZSB0aGUgZW5jb2RlciBtYXBzIGFsbCBpbnB1dHMgdG8gdGhlIHNhbWUgY29uc3RhbnQuIEJZT0wgc2hvd3MgdGhhdCBhbiBhc3ltbWV0cmljIGFyY2hpdGVjdHVyZSBjb21iaW5lZCB3aXRoIGFuIEVNQSB0YXJnZXQgbmV0d29yayBhbmQgc3RvcC1ncmFkaWVudCBpcyBzdWZmaWNpZW50IHRvIGF2b2lkIGNvbGxhcHNlIGFuZCBsZWFybiB1c2VmdWwgcmVwcmVzZW50YXRpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5vIE5lZ2F0aXZlcyDigJQgQXN5bW1ldHJpYyBBcmNoaXRlY3R1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJZT0wgdXNlcyB0d28gbmV0d29ya3M6IHRoZSBvbmxpbmUgbmV0d29yayAozrgpIGFuZCB0aGUgdGFyZ2V0IG5ldHdvcmsgKM6+KS4gVGhlIG9ubGluZSBuZXR3b3JrIGNvbXByaXNlcyBhbiBlbmNvZGVyIGZfzrgsIGEgcHJvamVjdG9yIGdfzrgsIGFuZCBhIHByZWRpY3RvciBxX864LiBUaGUgdGFyZ2V0IG5ldHdvcmsgaGFzIGVuY29kZXIgZl/OviBhbmQgcHJvamVjdG9yIGdfzr4sIGJ1dCBubyBwcmVkaWN0b3IuIEJvdGggbmV0d29ya3MgcHJvY2VzcyBkaWZmZXJlbnQgYXVnbWVudGVkIHZpZXdzIG9mIHRoZSBzYW1lIGltYWdlLiBUaGUgb25saW5lIG5ldHdvcmsgcHJlZGljdHMgdGhlIHRhcmdldFx1MDAyN3MgcHJvamVjdGlvbiwgYW5kIHRoZSBsb3NzIGlzIHRoZSBNU0UgYmV0d2VlbiBMMi1ub3JtYWxpc2VkIGVtYmVkZGluZ3MuIFRoZSBhc3ltbWV0cnkgKHByZWRpY3RvciBvbmx5IG9uIHRoZSBvbmxpbmUgc2lkZSkgYW5kIHRoZSBtb3ZpbmcgdGFyZ2V0IHByZXZlbnQgY29sbGFwc2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT25saW5lIGFuZCBUYXJnZXQgTmV0d29ya3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBpbWFnZSB4LCBhdWdtZW50IHRvIHByb2R1Y2Ugdmlld3MgdiBhbmQgdlx1MDAyNy4gT25saW5lOiB6X864ID0gZ1/OuChmX864KHYpKSwgcF/OuCA9IHFfzrgoel/OuCkuIFRhcmdldDogel/OviA9IGdfzr4oZl/Ovih2XHUwMDI3KSkuIExvc3M6IEwgPSAyIC0gMiDCtyAocF/OuCAvIOKAlnBfzrjigJYpIMK3ICh6X86+IC8g4oCWel/OvuKAlikgd2hpY2ggaXMgTVNFIG9mIG5vcm1hbGlzZWQgdmVjdG9ycy4gQnkgc3ltbWV0cnksIGNvbXB1dGUgbG9zcyBpbiBib3RoIGRpcmVjdGlvbnMgKHN3YXAgdiBhbmQgdlx1MDAyNykgYW5kIGF2ZXJhZ2UuIFRoZSB0YXJnZXQgbmV0d29yayBwYXJhbWV0ZXJzIM6+IGFyZSB1cGRhdGVkIGJ5IEVNQTogzr4g4oaQIM+EwrfOviArICgxLc+EKcK3zrggd2hlcmUgz4Qgc3RhcnRzIGF0IDAuOTk2IGFuZCBpcyBhbm5lYWxlZCB0byAxIGZvbGxvd2luZyBhIGNvc2luZSBzY2hlZHVsZS4gT25seSDOuCBpcyB1cGRhdGVkIGJ5IGdyYWRpZW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IHRvcmNodmlzaW9uLm1vZGVscyBhcyBtb2RlbHNcbmltcG9ydCBjb3B5XG5cbmRlZiBidWlsZF9tbHAoaW5fZGltLCBoaWRkZW5fZGltLCBvdXRfZGltKTpcbiAgICByZXR1cm4gbm4uU2VxdWVudGlhbChcbiAgICAgICAgbm4uTGluZWFyKGluX2RpbSwgaGlkZGVuX2RpbSksXG4gICAgICAgIG5uLkJhdGNoTm9ybTFkKGhpZGRlbl9kaW0pLFxuICAgICAgICBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgIG5uLkxpbmVhcihoaWRkZW5fZGltLCBvdXRfZGltKSxcbiAgICApXG5cbmNsYXNzIEJZT0wobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmFja2JvbmVfZm49bW9kZWxzLnJlc25ldDUwLCBmZWF0X2RpbT0yNTYsXG4gICAgICAgICAgICAgICAgIHByb2pfaGlkZGVuPTQwOTYsIHByZWRfaGlkZGVuPTQwOTYsIG1vbWVudHVtPTAuOTk2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubW9tZW50dW0gPSBtb21lbnR1bVxuICAgICAgICBiYXNlID0gYmFja2JvbmVfZm4od2VpZ2h0cz1Ob25lKVxuICAgICAgICBiYWNrYm9uZV9kaW0gPSBiYXNlLmZjLmluX2ZlYXR1cmVzXG4gICAgICAgICMgT25saW5lIG5ldHdvcms6IGVuY29kZXIgKyBwcm9qZWN0b3IgKyBwcmVkaWN0b3JcbiAgICAgICAgc2VsZi5vbmxpbmVfZW5jb2RlciA9IG5uLlNlcXVlbnRpYWwoKmxpc3QoYmFzZS5jaGlsZHJlbigpKVs6LTFdKVxuICAgICAgICBzZWxmLm9ubGluZV9wcm9qZWN0b3IgPSBidWlsZF9tbHAoYmFja2JvbmVfZGltLCBwcm9qX2hpZGRlbiwgZmVhdF9kaW0pXG4gICAgICAgIHNlbGYucHJlZGljdG9yID0gYnVpbGRfbWxwKGZlYXRfZGltLCBwcmVkX2hpZGRlbiwgZmVhdF9kaW0pXG4gICAgICAgICMgVGFyZ2V0IG5ldHdvcms6IGVuY29kZXIgKyBwcm9qZWN0b3Igb25seSAobm8gcHJlZGljdG9yKVxuICAgICAgICBzZWxmLnRhcmdldF9lbmNvZGVyID0gY29weS5kZWVwY29weShzZWxmLm9ubGluZV9lbmNvZGVyKVxuICAgICAgICBzZWxmLnRhcmdldF9wcm9qZWN0b3IgPSBjb3B5LmRlZXBjb3B5KHNlbGYub25saW5lX3Byb2plY3RvcilcbiAgICAgICAgZm9yIHAgaW4gbGlzdChzZWxmLnRhcmdldF9lbmNvZGVyLnBhcmFtZXRlcnMoKSkgKyBcXFxuICAgICAgICAgICAgICAgICBsaXN0KHNlbGYudGFyZ2V0X3Byb2plY3Rvci5wYXJhbWV0ZXJzKCkpOlxuICAgICAgICAgICAgcC5yZXF1aXJlc19ncmFkXyhGYWxzZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHYxLCB2Mik6XG4gICAgICAgICMgT25saW5lIHBhdGg6IHZpZXcgMVxuICAgICAgICBoMSA9IHNlbGYub25saW5lX2VuY29kZXIodjEpLmZsYXR0ZW4oMSlcbiAgICAgICAgejEgPSBzZWxmLm9ubGluZV9wcm9qZWN0b3IoaDEpXG4gICAgICAgIHAxID0gc2VsZi5wcmVkaWN0b3IoejEpXG4gICAgICAgICMgT25saW5lIHBhdGg6IHZpZXcgMlxuICAgICAgICBoMiA9IHNlbGYub25saW5lX2VuY29kZXIodjIpLmZsYXR0ZW4oMSlcbiAgICAgICAgejIgPSBzZWxmLm9ubGluZV9wcm9qZWN0b3IoaDIpXG4gICAgICAgIHAyID0gc2VsZi5wcmVkaWN0b3IoejIpXG4gICAgICAgICMgVGFyZ2V0IHBhdGggKG5vIGdyYWRpZW50KVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIHp0MSA9IHNlbGYudGFyZ2V0X3Byb2plY3RvcihzZWxmLnRhcmdldF9lbmNvZGVyKHYxKS5mbGF0dGVuKDEpKVxuICAgICAgICAgICAgenQyID0gc2VsZi50YXJnZXRfcHJvamVjdG9yKHNlbGYudGFyZ2V0X2VuY29kZXIodjIpLmZsYXR0ZW4oMSkpXG4gICAgICAgIHJldHVybiBwMSwgcDIsIHp0MS5kZXRhY2goKSwgenQyLmRldGFjaCgpXG5cbmJ5b2wgPSBCWU9MKClcbnByaW50KFx1MDAyN09ubGluZSBwYXJhbXM6XHUwMDI3LCBzdW0ocC5udW1lbCgpIGZvciBwIGluIGJ5b2wucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZCkgLy8gMV8wMDBfMDAwLCBcdTAwMjdNXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJZT0wgTG9zcyDigJQgTVNFIEJldHdlZW4gTm9ybWFsaXNlZCBQcmVkaWN0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEJZT0wgbG9zcyBpcyB0aGUgbWVhbiBzcXVhcmVkIGVycm9yIGJldHdlZW4gTDItbm9ybWFsaXNlZCB2ZWN0b3JzOiBMID0g4oCWcSh6zrgoeCkpIC8g4oCWcSh6zrgoeCkp4oCWIC0ges6+KHhcdTAwMjcpIC8g4oCWes6+KHhcdTAwMjcp4oCW4oCWwrIgPSAyIC0gMsK3Y29zX3NpbS4gVGhpcyBjYW4gYWxzbyBiZSB3cml0dGVuIGFzIDIoMSAtIGNvc19zaW1pbGFyaXR5KS4gVGhlIHN5bW1ldHJpc2VkIGxvc3MgYXZlcmFnZXMgYWNyb3NzIGJvdGggb3JkZXJpbmdzOiBMX3RvdGFsID0gwr1MKHDigoEsIHp04oKCKSArIMK9TChw4oKCLCB6dOKCgSkuIEJlY2F1c2UgYWxsIHRlcm1zIGFyZSBNU0UgcmF0aGVyIHRoYW4gYSBzb2Z0bWF4IG92ZXIgbmVnYXRpdmVzLCB0aGVyZSBpcyBubyBleHBsaWNpdCByZXB1bHNpb24gYmV0d2VlbiBkaWZmZXJlbnQgaW1hZ2VzIOKAlCBjb2xsYXBzZSBwcmV2ZW50aW9uIGNvbWVzIGVudGlyZWx5IGZyb20gdGhlIGFyY2hpdGVjdHVyYWwgYXN5bW1ldHJ5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGJ5b2xfbG9zcyhwLCB6KTpcbiAgICBcIlwiXCJCWU9MIHJlZ3Jlc3Npb24gbG9zczogMiAtIDIgKiBjb3NpbmVfc2ltaWxhcml0eSBiZXR3ZWVuIG5vcm1hbGlzZWQgdmVjdG9ycy5cbiAgICBwOiBvbmxpbmUgcHJlZGljdGlvbiAgKE4sIEQpIOKAlCByZXF1aXJlcyBncmFkXG4gICAgejogdGFyZ2V0IHByb2plY3Rpb24gKE4sIEQpIOKAlCBkZXRhY2hlZCwgbm8gZ3JhZFxuICAgIFwiXCJcIlxuICAgIHBfbm9ybSA9IEYubm9ybWFsaXplKHAsIGRpbT0xKVxuICAgIHpfbm9ybSA9IEYubm9ybWFsaXplKHosIGRpbT0xKVxuICAgICMgRXF1aXZhbGVudCB0byBNU0Ugb2YgdW5pdCB2ZWN0b3JzOiDigJZwLXrigJbCsiA9IDIgLSAyIHDCt3pcbiAgICByZXR1cm4gMiAtIDIgKiAocF9ub3JtICogel9ub3JtKS5zdW0oZGltPTEpLm1lYW4oKVxuXG5kZWYgYnlvbF9zeW1tZXRyaWNfbG9zcyhwMSwgcDIsIHp0MSwgenQyKTpcbiAgICBcIlwiXCJTeW1tZXRyaXNlZCBCWU9MIGxvc3Mgb3ZlciBib3RoIGF1Z21lbnRhdGlvbiBvcmRlcmluZ3MuXCJcIlwiXG4gICAgcmV0dXJuIDAuNSAqIGJ5b2xfbG9zcyhwMSwgenQyKSArIDAuNSAqIGJ5b2xfbG9zcyhwMiwgenQxKVxuXG4jIFZlcmlmeTogcGVyZmVjdCBhZ3JlZW1lbnQg4oaSIGxvc3MgPSAwXG50b3JjaC5tYW51YWxfc2VlZCgwKVxucCA9IEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKDMyLCAyNTYpLCBkaW09MSlcbmxvc3NfcGVyZmVjdCA9IGJ5b2xfbG9zcyhwLCBwKVxubG9zc19yYW5kb20gID0gYnlvbF9sb3NzKHAsIEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKDMyLCAyNTYpLCBkaW09MSkpXG5wcmludChmXHUwMDI3TG9zcyAocGVyZmVjdCBhZ3JlZW1lbnQpOiB7bG9zc19wZXJmZWN0Oi42Zn0gIChleHBlY3RlZCB+MClcdTAwMjcpXG5wcmludChmXHUwMDI3TG9zcyAocmFuZG9tIHZlY3RvcnMpOiAgICB7bG9zc19yYW5kb206LjRmfSAgICAoZXhwZWN0ZWQgfjIpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVNQSBUYXJnZXQgVXBkYXRlIFNjaGVkdWxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVbmxpa2UgTW9Db1x1MDAyN3MgZml4ZWQgbW9tZW50dW0gKDAuOTk5KSwgQllPTCB1c2VzIGEgY29zaW5lIHNjaGVkdWxlIGZvciDPhDogz4QodCkgPSAxIC0gKDEgLSDPhF9iYXNlKSDCtyAoY29zKM+AdC9UKSArIDEpIC8gMiB3aGVyZSDPhF9iYXNlID0gMC45OTYsIHQgaXMgdGhlIGN1cnJlbnQgc3RlcCwgYW5kIFQgaXMgdGhlIHRvdGFsIG51bWJlciBvZiBzdGVwcy4gVGhpcyBtZWFucyDPhCBzdGFydHMgYXQgMC45OTYgYW5kIGFwcHJvYWNoZXMgMS4wIGJ5IHRoZSBlbmQgb2YgdHJhaW5pbmcuIFRoZSBlZmZlY3QgaXMgdGhhdCBpbiBlYXJseSB0cmFpbmluZyB0aGUgdGFyZ2V0IHVwZGF0ZXMgbW9yZSByYXBpZGx5IChmYXN0ZXIgbGVhcm5pbmcpLCBhbmQgYnkgdGhlIGVuZCBvZiB0cmFpbmluZyB0aGUgdGFyZ2V0IGNoYW5nZXMgZXh0cmVtZWx5IHNsb3dseSAoc3RhYmxlLCBjb25zaXN0ZW50IHRhcmdldCBmb3IgdGhlIG9ubGluZSBuZXR3b3JrIHRvIGNvbnZlcmdlIHRvKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBtYXRoXG5pbXBvcnQgY29weVxuXG5kZWYgY29zaW5lX21vbWVudHVtX3NjaGVkdWxlKHN0ZXAsIHRvdGFsX3N0ZXBzLCB0YXVfYmFzZT0wLjk5Nik6XG4gICAgXCJcIlwiQllPTCBjb3NpbmUgYW5uZWFsaW5nIGZvciBFTUEgbW9tZW50dW0uXCJcIlwiXG4gICAgcmV0dXJuIDEgLSAoMSAtIHRhdV9iYXNlKSAqIChtYXRoLmNvcyhtYXRoLnBpICogc3RlcCAvIHRvdGFsX3N0ZXBzKSArIDEpIC8gMlxuXG5AdG9yY2gubm9fZ3JhZCgpXG5kZWYgdXBkYXRlX3RhcmdldF9uZXR3b3JrKG9ubGluZV9uZXQsIHRhcmdldF9uZXQsIHRhdSk6XG4gICAgXCJcIlwiRU1BIHVwZGF0ZSBvZiB0YXJnZXQgbmV0d29yayBwYXJhbWV0ZXJzLlwiXCJcIlxuICAgIGZvciBvbmxpbmVfcCwgdGFyZ2V0X3AgaW4gemlwKG9ubGluZV9uZXQucGFyYW1ldGVycygpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0YXJnZXRfbmV0LnBhcmFtZXRlcnMoKSk6XG4gICAgICAgIHRhcmdldF9wLmRhdGEgPSB0YXUgKiB0YXJnZXRfcC5kYXRhICsgKDEgLSB0YXUpICogb25saW5lX3AuZGF0YVxuXG4jIFZpc3VhbGlzZSBtb21lbnR1bSBzY2hlZHVsZSBvdmVyIDEwMDAgZXBvY2hzXG50b3RhbF9zdGVwcyA9IDEwMDBcbnRhdV92YWx1ZXMgPSBbY29zaW5lX21vbWVudHVtX3NjaGVkdWxlKHQsIHRvdGFsX3N0ZXBzKSBmb3IgdCBpbiByYW5nZSh0b3RhbF9zdGVwcyldXG5wcmludChmXHUwMDI3TW9tZW50dW0gYXQgc3RlcCAgICAwOiB7dGF1X3ZhbHVlc1swXTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01vbWVudHVtIGF0IHN0ZXAgIDI1MDoge3RhdV92YWx1ZXNbMjUwXTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01vbWVudHVtIGF0IHN0ZXAgIDUwMDoge3RhdV92YWx1ZXNbNTAwXTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01vbWVudHVtIGF0IHN0ZXAgIDk5OToge3RhdV92YWx1ZXNbOTk5XTouNmZ9XHUwMDI3KVxuIyBWZXJpZnkgbW9ub3RvbmljYWxseSBpbmNyZWFzaW5nXG5hc3NlcnQgYWxsKHRhdV92YWx1ZXNbaV0gXHUwMDNjPSB0YXVfdmFsdWVzW2krMV0gZm9yIGkgaW4gcmFuZ2UoOTk5KSlcbnByaW50KFx1MDAyN01vbWVudHVtIHNjaGVkdWxlIGlzIG1vbm90b25pY2FsbHkgaW5jcmVhc2luZzogVHJ1ZVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2xsYXBzZSBQcmV2ZW50aW9uIOKAlCBXaHkgSXQgV29ya3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgY29uc3RhbnQgb3V0cHV0IHogPSBjIGZvciBhbGwgaW5wdXRzIHdvdWxkIHRyaXZpYWxseSBtaW5pbWlzZSBhIG5haXZlIE1TRSBsb3NzIGJldHdlZW4gdHdvIHZpZXdzIG9mIHRoZSBzYW1lIGltYWdlLiBCWU9MIGF2b2lkcyB0aGlzIHRocm91Z2ggdGhyZWUgbWVjaGFuaXNtczogKDEpIFN0b3AtZ3JhZGllbnQgb24gdGhlIHRhcmdldCDigJQgdGhlIHRhcmdldCBuZXR3b3JrIGRvZXMgbm90IHByb3BhZ2F0ZSBncmFkaWVudHMsIHNvIHRoZSBvbmxpbmUgbmV0d29yayBjYW5ub3QgY28tYWRhcHQgd2l0aCB0aGUgdGFyZ2V0IHRvIGZpbmQgYSBqb2ludCBjb2xsYXBzZTsgKDIpIEVNQSB0YXJnZXQg4oCUIHRoZSB0YXJnZXQgZXZvbHZlcyBzbG93bHksIHByb3ZpZGluZyBhIHN0YWJsZSBidXQgbW92aW5nIHJlZ3Jlc3Npb24gdGFyZ2V0IHRoYXQgdGhlIG9ubGluZSBuZXR3b3JrIG11c3QgY29udGludW91c2x5IGltcHJvdmUgdG8gbWF0Y2g7ICgzKSBQcmVkaWN0b3IgcV/OuCDigJQgdGhlIGFzeW1tZXRyaWMgcHJlZGljdG9yIGNhbm5vdCBiZSBzYXRpc2ZpZWQgYnkgYSBjb25zdGFudCBtYXBwaW5nLCBmb3JjaW5nIHRoZSBvbmxpbmUgbmV0d29yayB0byBsZWFybiBzdHJ1Y3R1cmUuIEJhdGNoIE5vcm1hbGlzYXRpb24gYWxzbyBwbGF5cyBhIHN1YnRsZSByb2xlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgc2ltdWxhdGVfY29sbGFwc2UodXNlX3N0b3BfZ3JhZGllbnQ9VHJ1ZSwgc3RlcHM9MjAwLCBzZWVkPTQyKTpcbiAgICBcIlwiXCJEZW1vbnN0cmF0ZSBjb2xsYXBzZSByaXNrIGluIGEgc2ltcGxpZmllZCBCWU9MIHNldHRpbmcuXCJcIlwiXG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICBvbmxpbmUgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcigxNiwgMzIpLCBubi5SZUxVKCksIG5uLkxpbmVhcigzMiwgMTYpKVxuICAgIHRhcmdldCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDE2LCAzMiksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDMyLCAxNikpXG4gICAgIyBJbml0aWFsaXNlIHRhcmdldCA9IG9ubGluZVxuICAgIHRhcmdldC5sb2FkX3N0YXRlX2RpY3Qob25saW5lLnN0YXRlX2RpY3QoKSlcbiAgICBmb3IgcCBpbiB0YXJnZXQucGFyYW1ldGVycygpOlxuICAgICAgICBwLnJlcXVpcmVzX2dyYWRfKEZhbHNlKVxuICAgIG9wdGltaXplciA9IHRvcmNoLm9wdGltLkFkYW0ob25saW5lLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBjb2xsYXBzZV9tZXRyaWMgPSBbXVxuICAgIGZvciBzdGVwIGluIHJhbmdlKHN0ZXBzKTpcbiAgICAgICAgeCA9IHRvcmNoLnJhbmRuKDY0LCAxNilcbiAgICAgICAgcF9vdXQgPSBGLm5vcm1hbGl6ZShvbmxpbmUoeCksIGRpbT0xKVxuICAgICAgICB0X291dCA9IHRhcmdldCh4KVxuICAgICAgICBpZiB1c2Vfc3RvcF9ncmFkaWVudDpcbiAgICAgICAgICAgIHRfb3V0ID0gdF9vdXQuZGV0YWNoKClcbiAgICAgICAgbG9zcyA9ICgyIC0gMiAqIChwX291dCAqIEYubm9ybWFsaXplKHRfb3V0LCBkaW09MSkpLnN1bSgxKSkubWVhbigpXG4gICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgICMgRU1BIHVwZGF0ZSBvbmx5IGlmIHN0b3AtZ3JhZGllbnQgaXMgdXNlZFxuICAgICAgICBpZiB1c2Vfc3RvcF9ncmFkaWVudDpcbiAgICAgICAgICAgIHRhdSA9IDAuOTlcbiAgICAgICAgICAgIGZvciBvcCwgdHAgaW4gemlwKG9ubGluZS5wYXJhbWV0ZXJzKCksIHRhcmdldC5wYXJhbWV0ZXJzKCkpOlxuICAgICAgICAgICAgICAgIHRwLmRhdGEgPSB0YXUgKiB0cC5kYXRhICsgKDEtdGF1KSAqIG9wLmRhdGFcbiAgICAgICAgIyBDb2xsYXBzZSBtZXRyaWM6IHN0ZCBvZiBvdXRwdXRzIChzaG91bGQgc3RheSBcdTAwM2UgMClcbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICBzdGQgPSBGLm5vcm1hbGl6ZShvbmxpbmUoeCksIGRpbT0xKS5zdGQoMCkubWVhbigpLml0ZW0oKVxuICAgICAgICBjb2xsYXBzZV9tZXRyaWMuYXBwZW5kKHN0ZClcbiAgICByZXR1cm4gY29sbGFwc2VfbWV0cmljXG5cbnNnX21ldHJpY3MgICA9IHNpbXVsYXRlX2NvbGxhcHNlKHVzZV9zdG9wX2dyYWRpZW50PVRydWUpXG5ub3NnX21ldHJpY3MgPSBzaW11bGF0ZV9jb2xsYXBzZSh1c2Vfc3RvcF9ncmFkaWVudD1GYWxzZSlcbnByaW50KGZcdTAwMjdXaXRoIHN0b3AtZ3JhZGllbnQ6IGZpbmFsIG91dHB1dCBzdGQgPSB7c2dfbWV0cmljc1stMV06LjRmfSAgIChubyBjb2xsYXBzZSlcdTAwMjcpXG5wcmludChmXHUwMDI3Tm8gIHN0b3AtZ3JhZGllbnQ6ICBmaW5hbCBvdXRwdXQgc3RkID0ge25vc2dfbWV0cmljc1stMV06LjZmfSAgKGNvbGxhcHNlZClcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJCYXRjaCBOb3JtYWxpc2F0aW9uIGFuZCBDb2xsYXBzZSIsImNvbnRlbnQiOiJCWU9MIHJlbGllcyBzdWJ0bHkgb24gQmF0Y2ggTm9ybWFsaXNhdGlvbiAoQk4pIGluIHRoZSBwcm9qZWN0b3IgYW5kIHByZWRpY3Rvci4gQk4gbm9ybWFsaXNlcyBhY3RpdmF0aW9ucyBhY3Jvc3MgdGhlIGJhdGNoIGRpbWVuc2lvbiwgcHJldmVudGluZyB0aGUgbmV0d29yayBmcm9tIG91dHB1dHRpbmcgYSBjb25zdGFudCB2ZWN0b3IgKHNpbmNlIEJOIHdvdWxkIHplcm8tY2VudHJlIGFuZCBzY2FsZSBhbnkgY29uc3RhbnQgdG8gcHJvZHVjZSB2YXJpYW5jZSkuIEFuIGFibGF0aW9uIHJlbW92aW5nIEJOIGZyb20gdGhlIHByb2plY3RvciBhbmQgcHJlZGljdG9yIHNpZ25pZmljYW50bHkgaW5jcmVhc2VzIGNvbGxhcHNlIHByb2JhYmlsaXR5LiBXaGVuIGltcGxlbWVudGluZyBCWU9MIHdpdGhvdXQgQk4gKGUuZy4gd2l0aCBsYXllciBub3JtKSwgYWRkaXRpb25hbCBzdGFiaWxpc2F0aW9uIHRlY2huaXF1ZXMgbWF5IGJlIG5lZWRlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyBEZXRhaWxzIGFuZCBBdWdtZW50YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJZT0wgdXNlcyB0aGUgc2FtZSBhdWdtZW50YXRpb24gcGlwZWxpbmUgYXMgU2ltQ0xSOiByYW5kb20gcmVzaXplZCBjcm9wLCBob3Jpem9udGFsIGZsaXAsIGNvbG9yIGppdHRlciwgZ3JheXNjYWxlLCBhbmQgR2F1c3NpYW4gYmx1ci4gQW4gYWRkaXRpb25hbCBzb2xhcmlzYXRpb24gYXVnbWVudGF0aW9uIChpbnZlcnQgcGl4ZWwgdmFsdWVzIGFib3ZlIGEgdGhyZXNob2xkKSBpcyB1c2VkIHdpdGggMjAlIHByb2JhYmlsaXR5LiBFbmNvZGVyOiBSZXNOZXQtNTAgKG9yIGxhcmdlcikuIFByb2plY3RvcjogMi1sYXllciBNTFAgKDIwNDgg4oaSIDQwOTYg4oaSIDI1NikuIFByZWRpY3RvcjogMi1sYXllciBNTFAgKDI1NiDihpIgNDA5NiDihpIgMjU2KS4gVHJhaW5lZCBmb3IgMTAwMCBlcG9jaHMgd2l0aCBMQVJTIG9wdGltaXplciwgYmFzZSBMUiA9IDAuMiDDlyBiYXRjaF9zaXplLzI1Niwgd2VpZ2h0IGRlY2F5ID0gMS41ZS02LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiz4RfYmFzZSA9IDAuOTk2LCBhbm5lYWxlZCB0byAxLjAgdmlhIGNvc2luZSBzY2hlZHVsZSBvdmVyIHRyYWluaW5nLiIsIlByb2plY3RvciBoaWRkZW4gZGltIDQwOTYg4oCUIG11Y2ggbGFyZ2VyIHRoYW4gU2ltQ0xSXHUwMDI3cyBwcm9qZWN0aW9uIGhlYWQuIiwiUHJlZGljdG9yIGlzIGFsc28gYSAyLWxheWVyIE1MUCB3aXRoIHRoZSBzYW1lIGRpbWVuc2lvbnMgYXMgdGhlIHByb2plY3Rvci4iLCJObyBzeW1tZXRyaWMgbG9zcyBpbiBvcmlnaW5hbCBwYXBlciwgYnV0IHN5bW1ldHJpc2luZyBpbXByb3ZlcyBzdGFiaWxpdHkuIiwiU29sYXJpc2F0aW9uIGF1Z21lbnRhdGlvbjogUmFuZG9tU29sYXJpemUodGhyZXNob2xkPTEyOCwgcD0wLjIpIOKAlCB1bmlxdWUgdG8gQllPTC4iXX0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIk5lZ2F0aXZlcyIsIkVNQSBUYXJnZXQiLCJQcmVkaWN0b3IiLCJDb2xsYXBzZSBNZWNoYW5pc20iLCJMaW5lYXIgRXZhbCBUb3AtMSJdLCJyb3dzIjpbWyJTaW1DTFIiLCJZZXMgKGluLWJhdGNoKSIsIk5vIiwiTm8iLCJDb250cmFzdGl2ZSByZXB1bHNpb24iLCI2OS4zJSJdLFsiTW9DbyB2MiIsIlllcyAocXVldWUpIiwiWWVzIiwiTm8iLCJDb250cmFzdGl2ZSByZXB1bHNpb24gKyBxdWV1ZSIsIjcxLjElIl0sWyJCWU9MIiwiTm8iLCJZZXMiLCJZZXMiLCJBc3ltbWV0cnkgKyBFTUEgKyBCTiIsIjc0LjMlIl0sWyJTaW1TaWFtIiwiTm8iLCJObyIsIlllcyIsIlN0b3AtZ3JhZGllbnQgb25seSIsIjcxLjMlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXN1bHRzIGFuZCBJbXBhY3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJZT0wgYWNoaWV2ZXMgNzQuMyUgdG9wLTEgb24gSW1hZ2VOZXQgd2l0aCBSZXNOZXQtNTAg4oCUIGF0IHRoZSB0aW1lIG9mIHB1YmxpY2F0aW9uLCB0aGUgaGlnaGVzdCBzZWxmLXN1cGVydmlzZWQgbGluZWFyIGV2YWx1YXRpb24gYWNjdXJhY3ksIHN1cnBhc3NpbmcgYm90aCBTaW1DTFIgdjEgKDY5LjMlKSBhbmQgTW9DbyB2MiAoNzEuMSUpLiBPbiBzZW1pLXN1cGVydmlzZWQgYmVuY2htYXJrcyAoMSUgb2YgbGFiZWxzKSwgQllPTCB3aXRoIGEgZmluZS10dW5lZCBsaW5lYXIgaGVhZCBhY2hpZXZlcyA1My4yJSB0b3AtNSwgY2xvc2UgdG8gc3VwZXJ2aXNlZCAoNjMuMCUpLiBUaGUga2V5IHByYWN0aWNhbCBpbXBhY3Q6IEJZT0wgZW5hYmxlcyBoaWdoLXF1YWxpdHkgc2VsZi1zdXBlcnZpc2VkIHByZS10cmFpbmluZyB3aXRob3V0IGFueSBuZWVkIGZvciBuZWdhdGl2ZSBzYW1wbGluZyBzdHJhdGVnaWVzLCBoYXJkIG5lZ2F0aXZlIG1pbmluZywgb3IgY3VzdG9tIGRpc3RyaWJ1dGVkIGJhdGNoIG1hbmFnZW1lbnQuIn1d"
---
# BYOL — Bootstrap Your Own Latent Without Negatives

BYOL (Bootstrap Your Own Latent, Grill et al. 2020) was a landmark result because it achieved state-of-the-art self-supervised representation learning without any negative samples. The conventional wisdom was that negatives are essential to prevent collapse — a degenerate solution where the encoder maps all inputs to the same constant. BYOL shows that an asymmetric architecture combined with an EMA target network and stop-gradient is sufficient to avoid collapse and learn useful representations.

## No Negatives — Asymmetric Architecture

BYOL uses two networks: the online network (θ) and the target network (ξ). The online network comprises an encoder f_θ, a projector g_θ, and a predictor q_θ. The target network has encoder f_ξ and projector g_ξ, but no predictor. Both networks process different augmented views of the same image. The online network predicts the target's projection, and the loss is the MSE between L2-normalised embeddings. The asymmetry (predictor only on the online side) and the moving target prevent collapse.

## Online and Target Networks

For image x, augment to produce views v and v'. Online: z_θ = g_θ(f_θ(v)), p_θ = q_θ(z_θ). Target: z_ξ = g_ξ(f_ξ(v')). Loss: L = 2 - 2 · (p_θ / ‖p_θ‖) · (z_ξ / ‖z_ξ‖) which is MSE of normalised vectors. By symmetry, compute loss in both directions (swap v and v') and average. The target network parameters ξ are updated by EMA: ξ ← τ·ξ + (1-τ)·θ where τ starts at 0.996 and is annealed to 1 following a cosine schedule. Only θ is updated by gradient.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import copy

def build_mlp(in_dim, hidden_dim, out_dim):
    return nn.Sequential(
        nn.Linear(in_dim, hidden_dim),
        nn.BatchNorm1d(hidden_dim),
        nn.ReLU(inplace=True),
        nn.Linear(hidden_dim, out_dim),
    )

class BYOL(nn.Module):
    def __init__(self, backbone_fn=models.resnet50, feat_dim=256,
                 proj_hidden=4096, pred_hidden=4096, momentum=0.996):
        super().__init__()
        self.momentum = momentum
        base = backbone_fn(weights=None)
        backbone_dim = base.fc.in_features
        # Online network: encoder + projector + predictor
        self.online_encoder = nn.Sequential(*list(base.children())[:-1])
        self.online_projector = build_mlp(backbone_dim, proj_hidden, feat_dim)
        self.predictor = build_mlp(feat_dim, pred_hidden, feat_dim)
        # Target network: encoder + projector only (no predictor)
        self.target_encoder = copy.deepcopy(self.online_encoder)
        self.target_projector = copy.deepcopy(self.online_projector)
        for p in list(self.target_encoder.parameters()) + \
                 list(self.target_projector.parameters()):
            p.requires_grad_(False)

    def forward(self, v1, v2):
        # Online path: view 1
        h1 = self.online_encoder(v1).flatten(1)
        z1 = self.online_projector(h1)
        p1 = self.predictor(z1)
        # Online path: view 2
        h2 = self.online_encoder(v2).flatten(1)
        z2 = self.online_projector(h2)
        p2 = self.predictor(z2)
        # Target path (no gradient)
        with torch.no_grad():
            zt1 = self.target_projector(self.target_encoder(v1).flatten(1))
            zt2 = self.target_projector(self.target_encoder(v2).flatten(1))
        return p1, p2, zt1.detach(), zt2.detach()

byol = BYOL()
print('Online params:', sum(p.numel() for p in byol.parameters() if p.requires_grad) // 1_000_000, 'M')
```

## BYOL Loss — MSE Between Normalised Predictions

The BYOL loss is the mean squared error between L2-normalised vectors: L = ‖q(zθ(x)) / ‖q(zθ(x))‖ - zξ(x') / ‖zξ(x')‖‖² = 2 - 2·cos_sim. This can also be written as 2(1 - cos_similarity). The symmetrised loss averages across both orderings: L_total = ½L(p₁, zt₂) + ½L(p₂, zt₁). Because all terms are MSE rather than a softmax over negatives, there is no explicit repulsion between different images — collapse prevention comes entirely from the architectural asymmetry.

```python
import torch
import torch.nn.functional as F

def byol_loss(p, z):
    """BYOL regression loss: 2 - 2 * cosine_similarity between normalised vectors.
    p: online prediction  (N, D) — requires grad
    z: target projection (N, D) — detached, no grad
    """
    p_norm = F.normalize(p, dim=1)
    z_norm = F.normalize(z, dim=1)
    # Equivalent to MSE of unit vectors: ‖p-z‖² = 2 - 2 p·z
    return 2 - 2 * (p_norm * z_norm).sum(dim=1).mean()

def byol_symmetric_loss(p1, p2, zt1, zt2):
    """Symmetrised BYOL loss over both augmentation orderings."""
    return 0.5 * byol_loss(p1, zt2) + 0.5 * byol_loss(p2, zt1)

# Verify: perfect agreement → loss = 0
torch.manual_seed(0)
p = F.normalize(torch.randn(32, 256), dim=1)
loss_perfect = byol_loss(p, p)
loss_random  = byol_loss(p, F.normalize(torch.randn(32, 256), dim=1))
print(f'Loss (perfect agreement): {loss_perfect:.6f}  (expected ~0)')
print(f'Loss (random vectors):    {loss_random:.4f}    (expected ~2)')
```

## EMA Target Update Schedule

Unlike MoCo's fixed momentum (0.999), BYOL uses a cosine schedule for τ: τ(t) = 1 - (1 - τ_base) · (cos(πt/T) + 1) / 2 where τ_base = 0.996, t is the current step, and T is the total number of steps. This means τ starts at 0.996 and approaches 1.0 by the end of training. The effect is that in early training the target updates more rapidly (faster learning), and by the end of training the target changes extremely slowly (stable, consistent target for the online network to converge to).

```python
import torch
import torch.nn as nn
import math
import copy

def cosine_momentum_schedule(step, total_steps, tau_base=0.996):
    """BYOL cosine annealing for EMA momentum."""
    return 1 - (1 - tau_base) * (math.cos(math.pi * step / total_steps) + 1) / 2

@torch.no_grad()
def update_target_network(online_net, target_net, tau):
    """EMA update of target network parameters."""
    for online_p, target_p in zip(online_net.parameters(),
                                   target_net.parameters()):
        target_p.data = tau * target_p.data + (1 - tau) * online_p.data

# Visualise momentum schedule over 1000 epochs
total_steps = 1000
tau_values = [cosine_momentum_schedule(t, total_steps) for t in range(total_steps)]
print(f'Momentum at step    0: {tau_values[0]:.4f}')
print(f'Momentum at step  250: {tau_values[250]:.4f}')
print(f'Momentum at step  500: {tau_values[500]:.4f}')
print(f'Momentum at step  999: {tau_values[999]:.6f}')
# Verify monotonically increasing
assert all(tau_values[i] <= tau_values[i+1] for i in range(999))
print('Momentum schedule is monotonically increasing: True')
```

## Collapse Prevention — Why It Works

A constant output z = c for all inputs would trivially minimise a naive MSE loss between two views of the same image. BYOL avoids this through three mechanisms: (1) Stop-gradient on the target — the target network does not propagate gradients, so the online network cannot co-adapt with the target to find a joint collapse; (2) EMA target — the target evolves slowly, providing a stable but moving regression target that the online network must continuously improve to match; (3) Predictor q_θ — the asymmetric predictor cannot be satisfied by a constant mapping, forcing the online network to learn structure. Batch Normalisation also plays a subtle role.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def simulate_collapse(use_stop_gradient=True, steps=200, seed=42):
    """Demonstrate collapse risk in a simplified BYOL setting."""
    torch.manual_seed(seed)
    online = nn.Sequential(nn.Linear(16, 32), nn.ReLU(), nn.Linear(32, 16))
    target = nn.Sequential(nn.Linear(16, 32), nn.ReLU(), nn.Linear(32, 16))
    # Initialise target = online
    target.load_state_dict(online.state_dict())
    for p in target.parameters():
        p.requires_grad_(False)
    optimizer = torch.optim.Adam(online.parameters(), lr=1e-3)
    collapse_metric = []
    for step in range(steps):
        x = torch.randn(64, 16)
        p_out = F.normalize(online(x), dim=1)
        t_out = target(x)
        if use_stop_gradient:
            t_out = t_out.detach()
        loss = (2 - 2 * (p_out * F.normalize(t_out, dim=1)).sum(1)).mean()
        optimizer.zero_grad(); loss.backward(); optimizer.step()
        # EMA update only if stop-gradient is used
        if use_stop_gradient:
            tau = 0.99
            for op, tp in zip(online.parameters(), target.parameters()):
                tp.data = tau * tp.data + (1-tau) * op.data
        # Collapse metric: std of outputs (should stay > 0)
        with torch.no_grad():
            std = F.normalize(online(x), dim=1).std(0).mean().item()
        collapse_metric.append(std)
    return collapse_metric

sg_metrics   = simulate_collapse(use_stop_gradient=True)
nosg_metrics = simulate_collapse(use_stop_gradient=False)
print(f'With stop-gradient: final output std = {sg_metrics[-1]:.4f}   (no collapse)')
print(f'No  stop-gradient:  final output std = {nosg_metrics[-1]:.6f}  (collapsed)')
```

> **Batch Normalisation and Collapse**: BYOL relies subtly on Batch Normalisation (BN) in the projector and predictor. BN normalises activations across the batch dimension, preventing the network from outputting a constant vector (since BN would zero-centre and scale any constant to produce variance). An ablation removing BN from the projector and predictor significantly increases collapse probability. When implementing BYOL without BN (e.g. with layer norm), additional stabilisation techniques may be needed.

## Training Details and Augmentation

BYOL uses the same augmentation pipeline as SimCLR: random resized crop, horizontal flip, color jitter, grayscale, and Gaussian blur. An additional solarisation augmentation (invert pixel values above a threshold) is used with 20% probability. Encoder: ResNet-50 (or larger). Projector: 2-layer MLP (2048 → 4096 → 256). Predictor: 2-layer MLP (256 → 4096 → 256). Trained for 1000 epochs with LARS optimizer, base LR = 0.2 × batch_size/256, weight decay = 1.5e-6.

- τ_base = 0.996, annealed to 1.0 via cosine schedule over training.
- Projector hidden dim 4096 — much larger than SimCLR's projection head.
- Predictor is also a 2-layer MLP with the same dimensions as the projector.
- No symmetric loss in original paper, but symmetrising improves stability.
- Solarisation augmentation: RandomSolarize(threshold=128, p=0.2) — unique to BYOL.

| Method | Negatives | EMA Target | Predictor | Collapse Mechanism | Linear Eval Top-1 |
| --- | --- | --- | --- | --- | --- |
| SimCLR | Yes (in-batch) | No | No | Contrastive repulsion | 69.3% |
| MoCo v2 | Yes (queue) | Yes | No | Contrastive repulsion + queue | 71.1% |
| BYOL | No | Yes | Yes | Asymmetry + EMA + BN | 74.3% |
| SimSiam | No | No | Yes | Stop-gradient only | 71.3% |

## Results and Impact

BYOL achieves 74.3% top-1 on ImageNet with ResNet-50 — at the time of publication, the highest self-supervised linear evaluation accuracy, surpassing both SimCLR v1 (69.3%) and MoCo v2 (71.1%). On semi-supervised benchmarks (1% of labels), BYOL with a fine-tuned linear head achieves 53.2% top-5, close to supervised (63.0%). The key practical impact: BYOL enables high-quality self-supervised pre-training without any need for negative sampling strategies, hard negative mining, or custom distributed batch management.

