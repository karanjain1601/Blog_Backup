---
title: "Rejection Sampling Fine-Tuning — Generate Many, Keep Best for SFT"
slug: "rejection-sampling-finetuning"
description: "Rejection sampling fine-tuning (ReST/RST-EM) generates N candidate completions per prompt from the current policy, scores them with a reward model, filters to the top-K by reward, and fine-tunes on the filtered dataset — an EM-style self-improvement loop simpler and more stable than PPO."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVqZWN0aW9uIHNhbXBsaW5nIGZpbmUtdHVuaW5nIChSZVNULCBHdWxjZWhyZSBldCBhbC4gMjAyMzsgUlNULUVNLCBEb25nIGV0IGFsLiAyMDIzKSBpcyBhbiBhbGlnbm1lbnQgdGVjaG5pcXVlIHRoYXQgZnJhbWVzIHBvbGljeSBpbXByb3ZlbWVudCBhcyBhbiBFTSBhbGdvcml0aG0uIEluIHRoZSBFLXN0ZXAsIHRoZSBjdXJyZW50IHBvbGljeSBnZW5lcmF0ZXMgTiBjYW5kaWRhdGUgY29tcGxldGlvbnMgcGVyIHByb21wdCBhbmQgYSByZXdhcmQgbW9kZWwgc2NvcmVzIHRoZW0uIEluIHRoZSBNLXN0ZXAsIHRoZSB0b3AtSyBjb21wbGV0aW9ucyBhcmUga2VwdCBhbmQgdGhlIHBvbGljeSBpcyBmaW5lLXR1bmVkIHZpYSBzdGFuZGFyZCBTRlQgb24gdGhlc2UgZmlsdGVyZWQgKHByb21wdCwgY29tcGxldGlvbikgcGFpcnMuIFRoZSBwcm9jZXNzIHJlcGVhdHMgZm9yIG11bHRpcGxlIHJvdW5kcywgcHJvZ3Jlc3NpdmVseSBtb3ZpbmcgdGhlIHBvbGljeSBkaXN0cmlidXRpb24gdG93YXJkIGhpZ2hlci1yZXdhcmQgb3V0cHV0cyB3aXRob3V0IHRoZSBjb21wbGV4aXR5IGFuZCBpbnN0YWJpbGl0eSBvZiBQUE8uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIFJlU1QgQWxnb3JpdGhtIOKAlCBFTSBmb3IgQWxpZ25tZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgRU0gZnJhbWluZyBpcyBuYXR1cmFsOiBpbiB0aGUgRS1zdGVwLCB0aGUgcG9saWN5IGFjdHMgYXMgdGhlIHByb3Bvc2FsIGRpc3RyaWJ1dGlvbiB0byBnZW5lcmF0ZSBkaXZlcnNlIGNhbmRpZGF0ZSBjb21wbGV0aW9uczsgaW4gdGhlIE0tc3RlcCwgc3VwZXJ2aXNlZCBmaW5lLXR1bmluZyBvbiBmaWx0ZXJlZCBkYXRhIG1vdmVzIHRoZSBwb2xpY3kgdG93YXJkIHRoZSBoaWdoLXJld2FyZCByZWdpb24uIFVubGlrZSBQUE8sIHdoaWNoIHJlcXVpcmVzIG9ubGluZSByb2xsb3V0cywgaW1wb3J0YW5jZSBzYW1wbGluZyBjb3JyZWN0aW9ucywgYW5kIGEgdmFsdWUgZnVuY3Rpb24sIFJlU1Qgb25seSBuZWVkczogKDEpIGJhdGNoIGluZmVyZW5jZSBmb3IgZ2VuZXJhdGlvbiwgKDIpIGEgcmV3YXJkIG1vZGVsIGZvciBzY29yaW5nLCBhbmQgKDMpIHN0YW5kYXJkIFNGVCB0cmFpbmluZy4gVGhpcyBtYWtlcyBpdCBzaWduaWZpY2FudGx5IHNpbXBsZXIgdG8gaW1wbGVtZW50IGFuZCBtb3JlIHN0YWJsZSB0byB0cmFpbi4gTExhTUEtMlx1MDAyN3MgZmluYWwgYWxpZ25tZW50IHN0YWdlIHVzZXMgcmVqZWN0aW9uIHNhbXBsaW5nLCBhcyBkb2VzIEdlbWluaVx1MDAyN3MgUkxIRiBwaXBlbGluZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFLVN0ZXAg4oCUIEdlbmVyYXRpbmcgRGl2ZXJzZSBDb21wbGV0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGl2ZXJzaXR5IGluIHRoZSBFLXN0ZXAgaXMgY3JpdGljYWw6IHNhbXBsaW5nIGF0IGhpZ2ggdGVtcGVyYXR1cmUgKDAuOOKAkzEuMCkgc3ByZWFkcyB0aGUgZGlzdHJpYnV0aW9uIHRvIGV4cGxvcmUgdGhlIHJlc3BvbnNlIHNwYWNlLiBUaGUgbnVtYmVyIG9mIHNhbXBsZXMgTiBwZXIgcHJvbXB0ICh0eXBpY2FsbHkgMTDigJMxMDApIGNvbnRyb2xzIHRoZSBleHBsb3JhdGlvbi1leHBsb2l0YXRpb24gdHJhZGVvZmYuIFdpdGggTj0xIHRoZXJlIGlzIG5vIHNlbGVjdGlvbiBwcmVzc3VyZTsgd2l0aCBOPTEwMCwgdGhlIHJld2FyZCBtb2RlbCBjYW4gaWRlbnRpZnkgaGlnaC1xdWFsaXR5IGNvbXBsZXRpb25zIGV2ZW4gaWYgb25seSAxJSBvZiBzYW1wbGVzIGFyZSBleGNlbGxlbnQuIEJhdGNoIGdlbmVyYXRpb24gaXMgZW1iYXJyYXNzaW5nbHkgcGFyYWxsZWxpemFibGUgYWNyb3NzIHByb21wdHMsIG1ha2luZyBsYXJnZSBOIGNvbXB1dGF0aW9uYWxseSBmZWFzaWJsZSB3aXRoIHZMTE0gb3Igb3RoZXIgaGlnaC10aHJvdWdocHV0IGluZmVyZW5jZSBlbmdpbmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplclxuZnJvbSB0eXBpbmcgaW1wb3J0IE9wdGlvbmFsXG5cbmRlZiBiYXRjaF9nZW5lcmF0ZV9jb21wbGV0aW9ucyhcbiAgICBtb2RlbDogQXV0b01vZGVsRm9yQ2F1c2FsTE0sXG4gICAgdG9rZW5pemVyOiBBdXRvVG9rZW5pemVyLFxuICAgIHByb21wdHM6IGxpc3QsXG4gICAgbl9zYW1wbGVzOiBpbnQgPSA4LFxuICAgIHRlbXBlcmF0dXJlOiBmbG9hdCA9IDAuOSxcbiAgICBtYXhfbmV3X3Rva2VuczogaW50ID0gMjU2LFxuKSAtXHUwMDNlIGxpc3Q6XG4gICAgIyBHZW5lcmF0ZSBOIGNvbXBsZXRpb25zIHBlciBwcm9tcHQgYXQgaGlnaCB0ZW1wZXJhdHVyZSBmb3IgZGl2ZXJzaXR5XG4gICAgYWxsX2NvbXBsZXRpb25zID0gW11cbiAgICBmb3IgcHJvbXB0IGluIHByb21wdHM6XG4gICAgICAgIGlucHV0cyA9IHRva2VuaXplcihwcm9tcHQsIHJldHVybl90ZW5zb3JzPVx1MDAyN3B0XHUwMDI3KS50byhtb2RlbC5kZXZpY2UpXG4gICAgICAgIGNvbXBsZXRpb25zID0gW11cbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9zYW1wbGVzKTpcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIG91dHB1dF9pZHMgPSBtb2RlbC5nZW5lcmF0ZShcbiAgICAgICAgICAgICAgICAgICAgKippbnB1dHMsXG4gICAgICAgICAgICAgICAgICAgIG1heF9uZXdfdG9rZW5zPW1heF9uZXdfdG9rZW5zLFxuICAgICAgICAgICAgICAgICAgICBkb19zYW1wbGU9VHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgdGVtcGVyYXR1cmU9dGVtcGVyYXR1cmUsXG4gICAgICAgICAgICAgICAgICAgIHBhZF90b2tlbl9pZD10b2tlbml6ZXIuZW9zX3Rva2VuX2lkLFxuICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgIGdlbl9pZHMgPSBvdXRwdXRfaWRzWzBdW2lucHV0c1tcdTAwMjdpbnB1dF9pZHNcdTAwMjddLnNoYXBlWzFdOl1cbiAgICAgICAgICAgIGNvbXBsZXRpb25zLmFwcGVuZCh0b2tlbml6ZXIuZGVjb2RlKGdlbl9pZHMsIHNraXBfc3BlY2lhbF90b2tlbnM9VHJ1ZSkpXG4gICAgICAgIGFsbF9jb21wbGV0aW9ucy5hcHBlbmQoY29tcGxldGlvbnMpXG4gICAgcmV0dXJuIGFsbF9jb21wbGV0aW9uc1xuXG5kZWYgc2NvcmVfY29tcGxldGlvbnMocmV3YXJkX21vZGVsLCB0b2tlbml6ZXIsIHByb21wdHM6IGxpc3QsIGNvbXBsZXRpb25zX3Blcl9wcm9tcHQ6IGxpc3QpIC1cdTAwM2UgbGlzdDpcbiAgICAjIFNjb3JlIGVhY2ggY29tcGxldGlvbiB3aXRoIHJld2FyZCBtb2RlbCwgcmV0dXJuIHJld2FyZCBsaXN0c1xuICAgIHNjb3JlcyA9IFtdXG4gICAgZm9yIHByb21wdCwgY29tcGxldGlvbnMgaW4gemlwKHByb21wdHMsIGNvbXBsZXRpb25zX3Blcl9wcm9tcHQpOlxuICAgICAgICBwcm9tcHRfc2NvcmVzID0gW11cbiAgICAgICAgZm9yIGNvbXBsZXRpb24gaW4gY29tcGxldGlvbnM6XG4gICAgICAgICAgICBlbmMgPSB0b2tlbml6ZXIocHJvbXB0ICsgY29tcGxldGlvbiwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJ1bmNhdGlvbj1UcnVlLCBtYXhfbGVuZ3RoPTUxMikudG8ocmV3YXJkX21vZGVsLmRldmljZSlcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIHJld2FyZCA9IHJld2FyZF9tb2RlbCgqKmVuYykubG9naXRzLnNxdWVlemUoKS5pdGVtKClcbiAgICAgICAgICAgIHByb21wdF9zY29yZXMuYXBwZW5kKHJld2FyZClcbiAgICAgICAgc2NvcmVzLmFwcGVuZChwcm9tcHRfc2NvcmVzKVxuICAgIHJldHVybiBzY29yZXNcblxucHJpbnQoXHUwMDI3UmVTVCBFLXN0ZXA6IE49OCBzYW1wbGVzIHBlciBwcm9tcHQgYXQgdGVtcGVyYXR1cmU9MC45IGZvciBkaXZlcnNpdHlcdTAwMjcpXG5wcmludChcdTAwMjdTY29yZSBhbGwgY29tcGxldGlvbnMgd2l0aCByZXdhcmQgbW9kZWwsIHRoZW4ga2VlcCB0b3AtSyBmb3IgTS1zdGVwXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik0tU3RlcCDigJQgVG9wLUsgU2VsZWN0aW9uIGFuZCBGaW5lLVR1bmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIE0tc3RlcCBmaWx0ZXJzIGNvbXBsZXRpb25zIHRvIGEgaGlnaC1yZXdhcmQgc3Vic2V0IGFuZCBydW5zIFNGVCBvbiB0aGUgcmVzdWx0LiBUd28gc2VsZWN0aW9uIHN0cmF0ZWdpZXMgZXhpc3Q6IHRvcC1LIChrZWVwIHRoZSBLIGhpZ2hlc3Qtc2NvcmluZyBjb21wbGV0aW9ucyBwZXIgcHJvbXB0KSBhbmQgdGhyZXNob2xkLWJhc2VkIChrZWVwIGFsbCBjb21wbGV0aW9ucyBhYm92ZSBhIHJld2FyZCB0aHJlc2hvbGQpLiBUb3AtSyBndWFyYW50ZWVzIGV4YWN0bHkgSyB0cmFpbmluZyBleGFtcGxlcyBwZXIgcHJvbXB0LCBtYWludGFpbmluZyBkYXRhc2V0IGJhbGFuY2UuIFRocmVzaG9sZC1iYXNlZCBzZWxlY3Rpb24gZGlzY2FyZHMgYWxsIGNvbXBsZXRpb25zIGlmIG5vbmUgZXhjZWVkIHRoZSB0aHJlc2hvbGQsIHByb2R1Y2luZyBzcGFyc2VyIGJ1dCBoaWdoZXItcXVhbGl0eSB0cmFpbmluZyBkYXRhLiBBIGh5YnJpZCBhcHByb2FjaCDigJQgdG9wLUsgYW1vbmcgY29tcGxldGlvbnMgYWJvdmUgYSBtaW5pbXVtIHRocmVzaG9sZCDigJQgY29tYmluZXMgYm90aCBiZW5lZml0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIGRhdGFzZXRzIGltcG9ydCBEYXRhc2V0XG5mcm9tIHR5cGluZyBpbXBvcnQgT3B0aW9uYWxcblxuZGVmIHNlbGVjdF90b3Bfa19jb21wbGV0aW9ucyhcbiAgICBwcm9tcHRzOiBsaXN0LFxuICAgIGNvbXBsZXRpb25zOiBsaXN0LFxuICAgIHNjb3JlczogbGlzdCxcbiAgICB0b3BfazogaW50ID0gMixcbiAgICBzY29yZV90aHJlc2hvbGQ6IE9wdGlvbmFsW2Zsb2F0XSA9IE5vbmUsXG4pIC1cdTAwM2UgdHVwbGU6XG4gICAgIyBGaWx0ZXIgY29tcGxldGlvbnM6IGtlZXAgdG9wLUsgcGVyIHByb21wdCwgb3B0aW9uYWxseSBhYm92ZSB0aHJlc2hvbGRcbiAgICBzZWxlY3RlZF9wcm9tcHRzLCBzZWxlY3RlZF9jb21wbGV0aW9ucyA9IFtdLCBbXVxuICAgIGZvciBwcm9tcHQsIGNvbXBfbGlzdCwgc2NvcmVfbGlzdCBpbiB6aXAocHJvbXB0cywgY29tcGxldGlvbnMsIHNjb3Jlcyk6XG4gICAgICAgIHBhaXJlZCA9IHNvcnRlZCh6aXAoc2NvcmVfbGlzdCwgY29tcF9saXN0KSwgcmV2ZXJzZT1UcnVlKVxuICAgICAgICBrZXB0ID0gWyhzLCBjKSBmb3IgcywgYyBpbiBwYWlyZWRbOnRvcF9rXVxuICAgICAgICAgICAgICAgIGlmIHNjb3JlX3RocmVzaG9sZCBpcyBOb25lIG9yIHMgXHUwMDNlPSBzY29yZV90aHJlc2hvbGRdXG4gICAgICAgIGZvciBzY29yZSwgY29tcGxldGlvbiBpbiBrZXB0OlxuICAgICAgICAgICAgc2VsZWN0ZWRfcHJvbXB0cy5hcHBlbmQocHJvbXB0KVxuICAgICAgICAgICAgc2VsZWN0ZWRfY29tcGxldGlvbnMuYXBwZW5kKGNvbXBsZXRpb24pXG4gICAgcmV0dXJuIHNlbGVjdGVkX3Byb21wdHMsIHNlbGVjdGVkX2NvbXBsZXRpb25zXG5cbmRlZiBidWlsZF9zZnRfZGF0YXNldChwcm9tcHRzOiBsaXN0LCBjb21wbGV0aW9uczogbGlzdCkgLVx1MDAzZSBEYXRhc2V0OlxuICAgICMgQ3JlYXRlIEh1Z2dpbmdGYWNlIGRhdGFzZXQgZnJvbSBmaWx0ZXJlZCAocHJvbXB0LCBjb21wbGV0aW9uKSBwYWlyc1xuICAgIHJldHVybiBEYXRhc2V0LmZyb21fZGljdCh7XG4gICAgICAgIFx1MDAyN3Byb21wdFx1MDAyNzogcHJvbXB0cyxcbiAgICAgICAgXHUwMDI3Y29tcGxldGlvblx1MDAyNzogY29tcGxldGlvbnMsXG4gICAgICAgIFx1MDAyN3RleHRcdTAwMjc6IFtwICsgYyBmb3IgcCwgYyBpbiB6aXAocHJvbXB0cywgY29tcGxldGlvbnMpXSxcbiAgICB9KVxuXG4jIEV4YW1wbGUgd2l0aCBtb2NrIGRhdGFcbnNhbXBsZV9wcm9tcHRzID0gW1x1MDAyN0V4cGxhaW4gZ3JhZGllbnQgZGVzY2VudDpcdTAwMjcsIFx1MDAyN1doYXQgaXMgYXR0ZW50aW9uIGluIHRyYW5zZm9ybWVyczpcdTAwMjddXG5zYW1wbGVfY29tcGxldGlvbnMgPSBbW1x1MDAyN0dvb2QgQTFcdTAwMjcsIFx1MDAyN1Bvb3IgQTFcdTAwMjcsIFx1MDAyN09LIEExXHUwMDI3XSwgW1x1MDAyN0dyZWF0IEEyXHUwMDI3LCBcdTAwMjdQb29yIEEyXHUwMDI3LCBcdTAwMjdNZWRpdW0gQTJcdTAwMjddXVxuc2FtcGxlX3Njb3JlcyA9IFtbMC44LCAwLjMsIDAuNV0sIFswLjksIDAuMiwgMC42XV1cbnNlbF9wLCBzZWxfYyA9IHNlbGVjdF90b3Bfa19jb21wbGV0aW9ucyhzYW1wbGVfcHJvbXB0cywgc2FtcGxlX2NvbXBsZXRpb25zLCBzYW1wbGVfc2NvcmVzLCB0b3Bfaz0xKVxuZGF0YXNldCA9IGJ1aWxkX3NmdF9kYXRhc2V0KHNlbF9wLCBzZWxfYylcbnByaW50KGZcdTAwMjdTZWxlY3RlZCB7bGVuKGRhdGFzZXQpfSBwYWlycyBmcm9tIHtzdW0obGVuKGMpIGZvciBjIGluIHNhbXBsZV9jb21wbGV0aW9ucyl9IHRvdGFsXHUwMDI3KVxucHJpbnQoXHUwMDI3TS1zdGVwOiBmaW5lLXR1bmUgcG9saWN5IG9uIGZpbHRlcmVkIFNGVCBkYXRhc2V0IGZvciAxLTMgZXBvY2hzXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikl0ZXJhdGl2ZSBTZWxmLUltcHJvdmVtZW50IExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJ1bm5pbmcgbXVsdGlwbGUgcm91bmRzIG9mIFJlU1QgcHJvZ3Jlc3NpdmVseSBpbXByb3ZlcyB0aGUgcG9saWN5LiBFYXJseSByb3VuZHMgaW1wcm92ZSBwZXJmb3JtYW5jZSBvbiBlYXN5IHByb21wdHMgd2hlcmUgdGhlIGluaXRpYWwgcG9saWN5IGFscmVhZHkgZ2VuZXJhdGVzIG5lYXItY29ycmVjdCBvdXRwdXRzLiBMYXRlciByb3VuZHMgdGFyZ2V0IGhhcmRlciBwcm9tcHRzIGFzIHRoZSBwb2xpY3kgaW1wcm92ZXMuIFRoZSBFTS1saWtlIGR5bmFtaWNzIG1lYW4gdGhlIHByb2Nlc3MgY29udmVyZ2VzOiBvbmNlIHRoZSBwb2xpY3kgY29uc2lzdGVudGx5IGdlbmVyYXRlcyBoaWdoLXJld2FyZCBjb21wbGV0aW9ucywgdGhlIGZpbHRlcmVkIGRhdGFzZXQgc3RvcHMgY2hhbmdpbmcgYW5kIGZ1cnRoZXIgZmluZS10dW5pbmcgeWllbGRzIGRpbWluaXNoaW5nIHJldHVybnMuIFR5cGljYWwgc2V0dXBzIHJ1biAz4oCTNSByb3VuZHMgd2l0aCBOIGRlY3JlYXNpbmcgYWNyb3NzIHJvdW5kcyAobW9yZSBleHBsb3JhdGlvbiBlYXJseSwgbW9yZSBleHBsb2l0YXRpb24gbGF0ZXIpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcbmZyb20gdHlwaW5nIGltcG9ydCBDYWxsYWJsZVxuXG5AZGF0YWNsYXNzXG5jbGFzcyBSZVNUQ29uZmlnOlxuICAgIG5fcm91bmRzOiBpbnQgPSAzXG4gICAgbl9zYW1wbGVzX3Blcl9wcm9tcHQ6IGludCA9IDE2XG4gICAgdG9wX2s6IGludCA9IDRcbiAgICB0ZW1wZXJhdHVyZTogZmxvYXQgPSAwLjlcbiAgICByZXdhcmRfdGhyZXNob2xkOiBmbG9hdCA9IDAuNVxuXG5kZWYgcmVzdF9lbV9sb29wKFxuICAgIG1vZGVsLFxuICAgIHRva2VuaXplcixcbiAgICByZXdhcmRfbW9kZWwsXG4gICAgcHJvbXB0czogbGlzdCxcbiAgICBjb25maWc6IFJlU1RDb25maWcsXG4gICAgZmluZXR1bmVfZm46IENhbGxhYmxlLFxuKSAtXHUwMDNlIGxpc3Q6XG4gICAgIyBSdW4gZnVsbCBFLXN0ZXAgLyBNLXN0ZXAgbG9vcCBmb3IgY29uZmlnLm5fcm91bmRzXG4gICAgaGlzdG9yeSA9IFtdXG4gICAgZm9yIHJvdW5kX2lkeCBpbiByYW5nZShjb25maWcubl9yb3VuZHMpOlxuICAgICAgICBwcmludChmXHUwMDI3Um91bmQge3JvdW5kX2lkeCsxfS97Y29uZmlnLm5fcm91bmRzfTogRS1zdGVwIOKAlCBnZW5lcmF0aW5nIHtjb25maWcubl9zYW1wbGVzX3Blcl9wcm9tcHR9IHNhbXBsZXMvcHJvbXB0XHUwMDI3KVxuICAgICAgICBjb21wbGV0aW9ucyA9IGJhdGNoX2dlbmVyYXRlX2NvbXBsZXRpb25zKG1vZGVsLCB0b2tlbml6ZXIsIHByb21wdHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29uZmlnLm5fc2FtcGxlc19wZXJfcHJvbXB0LCBjb25maWcudGVtcGVyYXR1cmUpXG4gICAgICAgIHNjb3JlcyA9IHNjb3JlX2NvbXBsZXRpb25zKHJld2FyZF9tb2RlbCwgdG9rZW5pemVyLCBwcm9tcHRzLCBjb21wbGV0aW9ucylcbiAgICAgICAgc2VsX3AsIHNlbF9jID0gc2VsZWN0X3RvcF9rX2NvbXBsZXRpb25zKHByb21wdHMsIGNvbXBsZXRpb25zLCBzY29yZXMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29uZmlnLnRvcF9rLCBjb25maWcucmV3YXJkX3RocmVzaG9sZClcbiAgICAgICAgYXZnX3Jld2FyZCA9IHN1bShzdW0ocykvbGVuKHMpIGZvciBzIGluIHNjb3JlcykgLyBsZW4oc2NvcmVzKVxuICAgICAgICBwcmludChmXHUwMDI3Um91bmQge3JvdW5kX2lkeCsxfTogTS1zdGVwIOKAlCBmaW5lLXR1bmluZyBvbiB7bGVuKHNlbF9wKX0gcGFpcnMgKGF2ZyByZXdhcmQ9e2F2Z19yZXdhcmQ6LjNmfSlcdTAwMjcpXG4gICAgICAgIGRhdGFzZXQgPSBidWlsZF9zZnRfZGF0YXNldChzZWxfcCwgc2VsX2MpXG4gICAgICAgIGZpbmV0dW5lX2ZuKG1vZGVsLCBkYXRhc2V0KVxuICAgICAgICBoaXN0b3J5LmFwcGVuZCh7XHUwMDI3cm91bmRcdTAwMjc6IHJvdW5kX2lkeCsxLCBcdTAwMjduX3BhaXJzXHUwMDI3OiBsZW4oc2VsX3ApLCBcdTAwMjdhdmdfcmV3YXJkXHUwMDI3OiBhdmdfcmV3YXJkfSlcbiAgICByZXR1cm4gaGlzdG9yeVxuXG5jb25maWcgPSBSZVNUQ29uZmlnKG5fcm91bmRzPTMsIG5fc2FtcGxlc19wZXJfcHJvbXB0PTE2LCB0b3Bfaz00KVxucHJpbnQoXHUwMDI3UmVTVC1FTSBjb252ZXJnZXMgd2hlbiBwb2xpY3kgY29uc2lzdGVudGx5IGdlbmVyYXRlcyBoaWdoLXJld2FyZCBjb21wbGV0aW9uc1x1MDAyNylcbnByaW50KFx1MDAyN1JvdW5kIDE6IGVhc3kgcHJvbXB0cyBpbXByb3ZlOyBSb3VuZCAzKzogaGFyZCBwcm9tcHRzIHRhcmdldGVkIGJ5IGJldHRlciBwb2xpY3lcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmVzdC1vZi1OIENvbXB1dGUgQW5hbHlzaXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJlc3Qtb2YtTiAoQm9OKSBzYW1wbGluZyDigJQgZ2VuZXJhdGUgTiBjb21wbGV0aW9ucyBhbmQgcmV0dXJuIHRoZSBoaWdoZXN0LXNjb3Jpbmcgb25lIOKAlCBpcyBhIHNpbXBsZSBiYXNlbGluZSB0aGF0IHByb3ZpZGVzIHVzZWZ1bCBjb21wdXRlLXF1YWxpdHkgdHJhZGVvZmZzLiBUaGUgZXhwZWN0ZWQgbWF4aW11bSByZXdhcmQgb2YgTiBpLmkuZC4gR2F1c3NpYW4gc2FtcGxlcyBzY2FsZXMgYXMgzrwgKyDPg8K3zqbigbvCuShOLyhOKzEpKSwgd2hlcmUgzqbigbvCuSBpcyB0aGUgaW52ZXJzZSBDREYuIEJvTiB3aXRoIE49NjQgb2Z0ZW4gbWF0Y2hlcyBQUE8tdHJhaW5lZCBtb2RlbHMgYXQgMUIgcGFyYW1ldGVyIHNjYWxlLCBidXQgYXQgdGhlIGNvc3Qgb2YgTiBpbmZlcmVuY2UgcGFzc2VzIHBlciBwcm9tcHQuIFJlU1QgYW1vcnRpemVzIEJvTlx1MDAyN3MgcXVhbGl0eSBnYWluIGludG8gdGhlIG1vZGVsIHdlaWdodHMgc28gdGhhdCBpbmZlcmVuY2UgY29zdCByZW1haW5zIDEgcGFzcyBwZXIgcHJvbXB0IOKAlCB0aGUga2V5IHByYWN0aWNhbCBhZHZhbnRhZ2Ugb3ZlciBwdXJlIEJvTiBpbmZlcmVuY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybVxuXG5kZWYgZXhwZWN0ZWRfbWF4X3Jld2FyZChtdTogZmxvYXQsIHNpZ21hOiBmbG9hdCwgbl92YWx1ZXM6IGxpc3QpIC1cdTAwM2UgbGlzdDpcbiAgICAjIEV4cGVjdGVkIG1heGltdW0gb2YgTiBpLmkuZC4gR2F1c3NpYW4gcmV3YXJkczogbXUgKyBzaWdtYSAqIFBoaV4tMShOLyhOKzEpKVxuICAgIHJldHVybiBbbXUgKyBzaWdtYSAqIG5vcm0ucHBmKG4gLyAobiArIDEpKSBmb3IgbiBpbiBuX3ZhbHVlc11cblxuZGVmIGJvbl92c19wcG9fYW5hbHlzaXMobl92YWx1ZXM6IGxpc3QsIHBwb19yZXdhcmQ6IGZsb2F0LCBtdT0wLjAsIHNpZ21hPTEuMCkgLVx1MDAzZSBOb25lOlxuICAgICMgQ29tcGFyZSBCZXN0LW9mLU4gZXhwZWN0ZWQgcmV3YXJkIHZzIFBQTyBiYXNlbGluZSByZXdhcmRcbiAgICBib25fcmV3YXJkcyA9IGV4cGVjdGVkX21heF9yZXdhcmQobXUsIHNpZ21hLCBuX3ZhbHVlcylcbiAgICBwcmludChmXHUwMDI3e1wiTlwiOlx1MDAzZTZ9ICB7XCJCb04gRVtSXVwiOiBcdTAwM2UxMn0gIHtcInZzIFBQT1wiOlx1MDAzZTEwfSAge1wiSW5mZXJlbmNlIE5GRVwiOlx1MDAzZTE1fVx1MDAyNylcbiAgICBwcmludChcdTAwMjctXHUwMDI3ICogNTApXG4gICAgZm9yIG4sIHIgaW4gemlwKG5fdmFsdWVzLCBib25fcmV3YXJkcyk6XG4gICAgICAgIGRlbHRhID0gciAtIHBwb19yZXdhcmRcbiAgICAgICAgc2lnbiA9IFx1MDAyNytcdTAwMjcgaWYgZGVsdGEgXHUwMDNlPSAwIGVsc2UgXHUwMDI3XHUwMDI3XG4gICAgICAgIHByaW50KGZcdTAwMjd7bjpcdTAwM2U2fSAge3I6XHUwMDNlMTIuNGZ9ICB7c2lnbn17ZGVsdGE6XHUwMDNlOS40Zn0gIHtuOlx1MDAzZTE1fVx1MDAyNylcblxubl92YWx1ZXMgPSBbMSwgNCwgOCwgMTYsIDMyLCA2NCwgMTI4XVxucHBvX2VxdWl2YWxlbnQgPSAxLjE1ICAjIHR5cGljYWwgUFBPIHJld2FyZCBhdCBjb252ZXJnZW5jZSAoc3RkIEdhdXNzaWFuIHNjYWxlKVxuYm9uX3ZzX3Bwb19hbmFseXNpcyhuX3ZhbHVlcywgcHBvX2VxdWl2YWxlbnQsIG11PTAuMCwgc2lnbWE9MS4wKVxucHJpbnQoKVxucHJpbnQoXHUwMDI3UmVTVCBhbW9ydGl6ZXMgQm9OIHF1YWxpdHkgaW50byB3ZWlnaHRzOiBpbmZlcmVuY2UgY29zdCA9IDEgcGFzcyAobm90IE4pXHUwMDI3KVxucHJpbnQoXHUwMDI3UFBPIHJlYWNoZXMgc2ltaWxhciBxdWFsaXR5IGJ1dCByZXF1aXJlcyBvbmxpbmUgUkwgaW5mcmFzdHJ1Y3R1cmVcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tYmluaW5nIFJlamVjdGlvbiBTYW1wbGluZyB3aXRoIERQTyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHNhbWUgTiBzYW1wbGVzIGdlbmVyYXRlZCBwZXIgcHJvbXB0IGNhbiBiZSB1c2VkIHRvIGNyZWF0ZSAoYmVzdCwgd29yc3QpIERQTyBwcmVmZXJlbmNlIHBhaXJzIHJhdGhlciB0aGFuIG9ubHkga2VlcGluZyB0aGUgYmVzdCBmb3IgU0ZULiBUaGlzIGh5YnJpZCBhcHByb2FjaCDigJQgc29tZXRpbWVzIGNhbGxlZCBSZWplY3Rpb24gU2FtcGxpbmcgRFBPIOKAlCB1c2VzIHRoZSBoaWdoZXN0LXNjb3JpbmcgY29tcGxldGlvbiBhcyB0aGUgY2hvc2VuIHJlc3BvbnNlIGFuZCB0aGUgbG93ZXN0LXNjb3JpbmcgYXMgdGhlIHJlamVjdGVkIHJlc3BvbnNlLiBCZWNhdXNlIGJvdGggY29tcGxldGlvbnMgY29tZSBmcm9tIHRoZSBjdXJyZW50IHBvbGljeSwgdGhlIHByZWZlcmVuY2UgcGFpcnMgYXJlIG9uLXBvbGljeSB3aXRoIHJlc3BlY3QgdG8gdGhlIGN1cnJlbnQgbW9kZWxcdTAwMjdzIGRpc3RyaWJ1dGlvbiwgd2hpY2ggaXMgbW9yZSBpbmZvcm1hdGl2ZSB0aGFuIHN0YXRpYyBodW1hbiBsYWJlbHMgZnJvbSB0aGUgb3JpZ2luYWwgU0ZUIG1vZGVsLiBDb21iaW5pbmcgcmVqZWN0aW9uIHNhbXBsaW5nIHdpdGggRFBPIHByb3ZpZGVzIHRoZSBiZXN0IG9mIGJvdGg6IGRpdmVyc2UgZXhwbG9yYXRpb24gZnJvbSBzYW1wbGluZyBhbmQgY29udHJhc3RpdmUgcHJlZmVyZW5jZSBsZWFybmluZyBmcm9tIERQTy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmFyaWFudCIsIk4gU2FtcGxlcyIsIlNlbGVjdGlvbiBTdHJhdGVneSIsIlJvdW5kcyIsIlJld2FyZCBNb2RlbCBUeXBlIl0sInJvd3MiOltbIlJlU1QgKEd1bGNlaHJlIDIwMjMpIiwiMTDigJM2NCIsIlRocmVzaG9sZDoga2VlcCBhYm92ZSBSX21pbiIsIjHigJMzIiwiVHJhaW5lZCBSTSAoTE0taGVhZCBvbiByZXdhcmQpIl0sWyJSU1QtRU0gKERvbmcgMjAyMykiLCIxNuKAkzY0IiwiVG9wLUsgcGVyIHByb21wdCIsIjPigJM1IiwiVHJhaW5lZCBSTSBvciB2ZXJpZmllciJdLFsiTExhTUEtMiBSU1QiLCIyMOKAkzEwMCIsIlRvcC0xIChzaW5nbGUgYmVzdCkiLCIxIiwiSHVtYW4gcHJlZmVyZW5jZSBSTSJdLFsiU1RhUiAoWmVsaWttYW4gMjAyMikiLCJTZWxmLWNvbnNpc3RlbmN5IG1ham9yaXR5IHZvdGUiLCJDb3JyZWN0IGZpbmFsIGFuc3dlciBmaWx0ZXIiLCJNdWx0aXBsZSIsIkdyb3VuZCB0cnV0aCB2ZXJpZmllciJdLFsiU2VsZi1QbGF5IEZpbmUtVHVuaW5nIiwiVmFyaWFibGUiLCJDdXJyZW50IHZzIHByZXZpb3VzIG1vZGVsIHdpbnMiLCJJdGVyYXRpdmUiLCJMTS1hcy1qdWRnZSBvciB0cmFpbmVkIFJNIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgQ29uc2lkZXJhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJld2FyZCBoYWNraW5nIGlzIHRoZSBwcmltYXJ5IGZhaWx1cmUgbW9kZTogaWYgdGhlIHJld2FyZCBtb2RlbCBoYXMgYmxpbmQgc3BvdHMsIHRoZSBwb2xpY3kgbGVhcm5zIHRvIGV4cGxvaXQgdGhlbSByYXRoZXIgdGhhbiBnZW51aW5lbHkgaW1wcm92ZS4gTW9uaXRvcmluZyByZXdhcmQgbW9kZWwgY29ycmVsYXRpb24gd2l0aCBodW1hbiBwcmVmZXJlbmNlcyBhY3Jvc3MgdHJhaW5pbmcgcm91bmRzIGlzIGVzc2VudGlhbC4gVGhlIHJld2FyZCB0aHJlc2hvbGQgc2hvdWxkIGluY3JlYXNlIGFjcm9zcyByb3VuZHMgYXMgdGhlIHBvbGljeSBpbXByb3ZlcyDigJQga2VlcGluZyBhbiBhYnNvbHV0ZSB0aHJlc2hvbGQgbGVhZHMgdG8gYWxsIGNvbXBsZXRpb25zIHBhc3NpbmcgaW4gbGF0ZXIgcm91bmRzLCBjb2xsYXBzaW5nIHRvIHN0YW5kYXJkIFNGVC4gVXNpbmcgYSBzZXBhcmF0ZSBoZWxkLW91dCBzZXQgdG8gdHJhY2sgaHVtYW4gZXZhbCB3aW4gcmF0ZSAobm90IGp1c3QgUk0gc2NvcmUpIGNhdGNoZXMgcmV3YXJkIGhhY2tpbmcgYmVmb3JlIGl0IGRlZ3JhZGVzIGh1bWFuLXBlcmNlaXZlZCBxdWFsaXR5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIHRlbXBlcmF0dXJlIDAuOOKAkzEuMCBmb3IgRS1zdGVwIGdlbmVyYXRpb24g4oCUIGxvd2VyIHRlbXBlcmF0dXJlcyByZWR1Y2UgZGl2ZXJzaXR5IGFuZCBsaW1pdCBzZWxlY3Rpb24gcHJlc3N1cmUuIiwiTj0xNuKAkzMyIGlzIG9mdGVuIHN1ZmZpY2llbnQ7IGJleW9uZCBOPTY0IHRoZSBtYXJnaW5hbCBpbXByb3ZlbWVudCBwZXIgYWRkaXRpb25hbCBzYW1wbGUgZGltaW5pc2hlcyBzaGFycGx5LiIsIkluY3JlYXNlIHJld2FyZCB0aHJlc2hvbGQgYWNyb3NzIHJvdW5kcyB0byBtYWludGFpbiBzZWxlY3Rpb24gcHJlc3N1cmUgYXMgdGhlIHBvbGljeSBpbXByb3Zlcy4iLCJNb25pdG9yIFJNIHNjb3JlIHZzIGh1bWFuIHdpbiByYXRlIGNvcnJlbGF0aW9uIOKAlCBkaXZlcmdlbmNlIHNpZ25hbHMgcmV3YXJkIGhhY2tpbmcuIiwiVXNlIHZMTE0gb3IgU0dMYW5nIGZvciBFLXN0ZXAgZ2VuZXJhdGlvbjogYmF0Y2hlZCBzYW1wbGluZyB3aXRoIE4gY29tcGxldGlvbnMgcGVyIHByb21wdCBpcyBtZW1vcnktZWZmaWNpZW50LiJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQ29tYmluaW5nIFJlamVjdGlvbiBTYW1wbGluZyB3aXRoIERQTyIsImNvbnRlbnQiOiJDb21iaW5pbmcgcmVqZWN0aW9uIHNhbXBsaW5nIHdpdGggRFBPIHByb3ZpZGVzIHRoZSBiZXN0IG9mIGJvdGg6IHVzZSB0aGUgc2FtZSBOIHNhbXBsZXMgdG8gY3JlYXRlIChiZXN0LCB3b3JzdCkgRFBPIHBhaXJzIOKAlCB0aGlzIGdlbmVyYXRlcyBkaXZlcnNlIHByZWZlcmVuY2UgcGFpcnMgYWxpZ25lZCB3aXRoIHRoZSBjdXJyZW50IHBvbGljeVx1MDAyN3Mgb3V0cHV0IGRpc3RyaWJ1dGlvbiwgd2hpY2ggaXMgbW9yZSBvbi1wb2xpY3kgdGhhbiBzdGF0aWMgaHVtYW4gbGFiZWxzIGFuZCB0cmFpbnMgZmFzdGVyIHRoYW4gUFBPIHdoaWxlIG1haW50YWluaW5nIERQT1x1MDAyN3Mgc2ltcGxpY2l0eS4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Rejection Sampling Fine-Tuning — Generate Many, Keep Best for SFT

Rejection sampling fine-tuning (ReST, Gulcehre et al. 2023; RST-EM, Dong et al. 2023) is an alignment technique that frames policy improvement as an EM algorithm. In the E-step, the current policy generates N candidate completions per prompt and a reward model scores them. In the M-step, the top-K completions are kept and the policy is fine-tuned via standard SFT on these filtered (prompt, completion) pairs. The process repeats for multiple rounds, progressively moving the policy distribution toward higher-reward outputs without the complexity and instability of PPO.

## The ReST Algorithm — EM for Alignment

The EM framing is natural: in the E-step, the policy acts as the proposal distribution to generate diverse candidate completions; in the M-step, supervised fine-tuning on filtered data moves the policy toward the high-reward region. Unlike PPO, which requires online rollouts, importance sampling corrections, and a value function, ReST only needs: (1) batch inference for generation, (2) a reward model for scoring, and (3) standard SFT training. This makes it significantly simpler to implement and more stable to train. LLaMA-2's final alignment stage uses rejection sampling, as does Gemini's RLHF pipeline.

## E-Step — Generating Diverse Completions

Diversity in the E-step is critical: sampling at high temperature (0.8–1.0) spreads the distribution to explore the response space. The number of samples N per prompt (typically 10–100) controls the exploration-exploitation tradeoff. With N=1 there is no selection pressure; with N=100, the reward model can identify high-quality completions even if only 1% of samples are excellent. Batch generation is embarrassingly parallelizable across prompts, making large N computationally feasible with vLLM or other high-throughput inference engines.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Optional

def batch_generate_completions(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    prompts: list,
    n_samples: int = 8,
    temperature: float = 0.9,
    max_new_tokens: int = 256,
) -> list:
    # Generate N completions per prompt at high temperature for diversity
    all_completions = []
    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
        completions = []
        for _ in range(n_samples):
            with torch.no_grad():
                output_ids = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=True,
                    temperature=temperature,
                    pad_token_id=tokenizer.eos_token_id,
                )
            gen_ids = output_ids[0][inputs['input_ids'].shape[1]:]
            completions.append(tokenizer.decode(gen_ids, skip_special_tokens=True))
        all_completions.append(completions)
    return all_completions

def score_completions(reward_model, tokenizer, prompts: list, completions_per_prompt: list) -> list:
    # Score each completion with reward model, return reward lists
    scores = []
    for prompt, completions in zip(prompts, completions_per_prompt):
        prompt_scores = []
        for completion in completions:
            enc = tokenizer(prompt + completion, return_tensors='pt',
                            truncation=True, max_length=512).to(reward_model.device)
            with torch.no_grad():
                reward = reward_model(**enc).logits.squeeze().item()
            prompt_scores.append(reward)
        scores.append(prompt_scores)
    return scores

print('ReST E-step: N=8 samples per prompt at temperature=0.9 for diversity')
print('Score all completions with reward model, then keep top-K for M-step')
```

## M-Step — Top-K Selection and Fine-Tuning

The M-step filters completions to a high-reward subset and runs SFT on the result. Two selection strategies exist: top-K (keep the K highest-scoring completions per prompt) and threshold-based (keep all completions above a reward threshold). Top-K guarantees exactly K training examples per prompt, maintaining dataset balance. Threshold-based selection discards all completions if none exceed the threshold, producing sparser but higher-quality training data. A hybrid approach — top-K among completions above a minimum threshold — combines both benefits.

```python
import torch
from datasets import Dataset
from typing import Optional

def select_top_k_completions(
    prompts: list,
    completions: list,
    scores: list,
    top_k: int = 2,
    score_threshold: Optional[float] = None,
) -> tuple:
    # Filter completions: keep top-K per prompt, optionally above threshold
    selected_prompts, selected_completions = [], []
    for prompt, comp_list, score_list in zip(prompts, completions, scores):
        paired = sorted(zip(score_list, comp_list), reverse=True)
        kept = [(s, c) for s, c in paired[:top_k]
                if score_threshold is None or s >= score_threshold]
        for score, completion in kept:
            selected_prompts.append(prompt)
            selected_completions.append(completion)
    return selected_prompts, selected_completions

def build_sft_dataset(prompts: list, completions: list) -> Dataset:
    # Create HuggingFace dataset from filtered (prompt, completion) pairs
    return Dataset.from_dict({
        'prompt': prompts,
        'completion': completions,
        'text': [p + c for p, c in zip(prompts, completions)],
    })

# Example with mock data
sample_prompts = ['Explain gradient descent:', 'What is attention in transformers:']
sample_completions = [['Good A1', 'Poor A1', 'OK A1'], ['Great A2', 'Poor A2', 'Medium A2']]
sample_scores = [[0.8, 0.3, 0.5], [0.9, 0.2, 0.6]]
sel_p, sel_c = select_top_k_completions(sample_prompts, sample_completions, sample_scores, top_k=1)
dataset = build_sft_dataset(sel_p, sel_c)
print(f'Selected {len(dataset)} pairs from {sum(len(c) for c in sample_completions)} total')
print('M-step: fine-tune policy on filtered SFT dataset for 1-3 epochs')
```

## Iterative Self-Improvement Loop

Running multiple rounds of ReST progressively improves the policy. Early rounds improve performance on easy prompts where the initial policy already generates near-correct outputs. Later rounds target harder prompts as the policy improves. The EM-like dynamics mean the process converges: once the policy consistently generates high-reward completions, the filtered dataset stops changing and further fine-tuning yields diminishing returns. Typical setups run 3–5 rounds with N decreasing across rounds (more exploration early, more exploitation later).

```python
from dataclasses import dataclass
from typing import Callable

@dataclass
class ReSTConfig:
    n_rounds: int = 3
    n_samples_per_prompt: int = 16
    top_k: int = 4
    temperature: float = 0.9
    reward_threshold: float = 0.5

def rest_em_loop(
    model,
    tokenizer,
    reward_model,
    prompts: list,
    config: ReSTConfig,
    finetune_fn: Callable,
) -> list:
    # Run full E-step / M-step loop for config.n_rounds
    history = []
    for round_idx in range(config.n_rounds):
        print(f'Round {round_idx+1}/{config.n_rounds}: E-step — generating {config.n_samples_per_prompt} samples/prompt')
        completions = batch_generate_completions(model, tokenizer, prompts,
                                                 config.n_samples_per_prompt, config.temperature)
        scores = score_completions(reward_model, tokenizer, prompts, completions)
        sel_p, sel_c = select_top_k_completions(prompts, completions, scores,
                                                 config.top_k, config.reward_threshold)
        avg_reward = sum(sum(s)/len(s) for s in scores) / len(scores)
        print(f'Round {round_idx+1}: M-step — fine-tuning on {len(sel_p)} pairs (avg reward={avg_reward:.3f})')
        dataset = build_sft_dataset(sel_p, sel_c)
        finetune_fn(model, dataset)
        history.append({'round': round_idx+1, 'n_pairs': len(sel_p), 'avg_reward': avg_reward})
    return history

config = ReSTConfig(n_rounds=3, n_samples_per_prompt=16, top_k=4)
print('ReST-EM converges when policy consistently generates high-reward completions')
print('Round 1: easy prompts improve; Round 3+: hard prompts targeted by better policy')
```

## Best-of-N Compute Analysis

Best-of-N (BoN) sampling — generate N completions and return the highest-scoring one — is a simple baseline that provides useful compute-quality tradeoffs. The expected maximum reward of N i.i.d. Gaussian samples scales as μ + σ·Φ⁻¹(N/(N+1)), where Φ⁻¹ is the inverse CDF. BoN with N=64 often matches PPO-trained models at 1B parameter scale, but at the cost of N inference passes per prompt. ReST amortizes BoN's quality gain into the model weights so that inference cost remains 1 pass per prompt — the key practical advantage over pure BoN inference.

```python
import numpy as np
from scipy.stats import norm

def expected_max_reward(mu: float, sigma: float, n_values: list) -> list:
    # Expected maximum of N i.i.d. Gaussian rewards: mu + sigma * Phi^-1(N/(N+1))
    return [mu + sigma * norm.ppf(n / (n + 1)) for n in n_values]

def bon_vs_ppo_analysis(n_values: list, ppo_reward: float, mu=0.0, sigma=1.0) -> None:
    # Compare Best-of-N expected reward vs PPO baseline reward
    bon_rewards = expected_max_reward(mu, sigma, n_values)
    print(f'{"N":>6}  {"BoN E[R]": >12}  {"vs PPO":>10}  {"Inference NFE":>15}')
    print('-' * 50)
    for n, r in zip(n_values, bon_rewards):
        delta = r - ppo_reward
        sign = '+' if delta >= 0 else ''
        print(f'{n:>6}  {r:>12.4f}  {sign}{delta:>9.4f}  {n:>15}')

n_values = [1, 4, 8, 16, 32, 64, 128]
ppo_equivalent = 1.15  # typical PPO reward at convergence (std Gaussian scale)
bon_vs_ppo_analysis(n_values, ppo_equivalent, mu=0.0, sigma=1.0)
print()
print('ReST amortizes BoN quality into weights: inference cost = 1 pass (not N)')
print('PPO reaches similar quality but requires online RL infrastructure')
```

## Combining Rejection Sampling with DPO

The same N samples generated per prompt can be used to create (best, worst) DPO preference pairs rather than only keeping the best for SFT. This hybrid approach — sometimes called Rejection Sampling DPO — uses the highest-scoring completion as the chosen response and the lowest-scoring as the rejected response. Because both completions come from the current policy, the preference pairs are on-policy with respect to the current model's distribution, which is more informative than static human labels from the original SFT model. Combining rejection sampling with DPO provides the best of both: diverse exploration from sampling and contrastive preference learning from DPO.

| Variant | N Samples | Selection Strategy | Rounds | Reward Model Type |
| --- | --- | --- | --- | --- |
| ReST (Gulcehre 2023) | 10–64 | Threshold: keep above R_min | 1–3 | Trained RM (LM-head on reward) |
| RST-EM (Dong 2023) | 16–64 | Top-K per prompt | 3–5 | Trained RM or verifier |
| LLaMA-2 RST | 20–100 | Top-1 (single best) | 1 | Human preference RM |
| STaR (Zelikman 2022) | Self-consistency majority vote | Correct final answer filter | Multiple | Ground truth verifier |
| Self-Play Fine-Tuning | Variable | Current vs previous model wins | Iterative | LM-as-judge or trained RM |

## Practical Considerations

Reward hacking is the primary failure mode: if the reward model has blind spots, the policy learns to exploit them rather than genuinely improve. Monitoring reward model correlation with human preferences across training rounds is essential. The reward threshold should increase across rounds as the policy improves — keeping an absolute threshold leads to all completions passing in later rounds, collapsing to standard SFT. Using a separate held-out set to track human eval win rate (not just RM score) catches reward hacking before it degrades human-perceived quality.

- Use temperature 0.8–1.0 for E-step generation — lower temperatures reduce diversity and limit selection pressure.
- N=16–32 is often sufficient; beyond N=64 the marginal improvement per additional sample diminishes sharply.
- Increase reward threshold across rounds to maintain selection pressure as the policy improves.
- Monitor RM score vs human win rate correlation — divergence signals reward hacking.
- Use vLLM or SGLang for E-step generation: batched sampling with N completions per prompt is memory-efficient.

> **Combining Rejection Sampling with DPO**: Combining rejection sampling with DPO provides the best of both: use the same N samples to create (best, worst) DPO pairs — this generates diverse preference pairs aligned with the current policy's output distribution, which is more on-policy than static human labels and trains faster than PPO while maintaining DPO's simplicity.

---

