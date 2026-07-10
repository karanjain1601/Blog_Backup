---
title: "Best-of-N Sampling"
slug: "best-of-n-sampling"
description: "Generating N candidate solutions and selecting the best using a reward model, majority vote, or verifier — a simple but powerful test-time compute scaling strategy with strong empirical results."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVzdC1vZi1OIChCb04pIHNhbXBsaW5nIGlzIHRoZSBzaW1wbGVzdCBhbmQgbW9zdCB3aWRlbHkgZGVwbG95ZWQgdGVzdC10aW1lIGNvbXB1dGUgc2NhbGluZyBzdHJhdGVneTogZ2VuZXJhdGUgTiBjYW5kaWRhdGUgc29sdXRpb25zIGZvciBhIHByb2JsZW0gYW5kIHNlbGVjdCB0aGUgYmVzdCBvbmUgdXNpbmcgYSByZXdhcmQgbW9kZWwsIG1ham9yaXR5IHZvdGUsIG9yIHZlcmlmaWVyLiBVbmxpa2UgYmVhbSBzZWFyY2ggKHdoaWNoIHBydW5lcyB0aGUgc2VhcmNoIHNwYWNlIGR1cmluZyBnZW5lcmF0aW9uKSBvciBNQ1RTICh3aGljaCBidWlsZHMgYSByZWFzb25pbmcgdHJlZSksIEJvTiBnZW5lcmF0ZXMgYWxsIE4gY2FuZGlkYXRlcyBpbmRlcGVuZGVudGx5IGFuZCBzZWxlY3RzIHBvc3QtaG9jLiBUaGlzIGRlY291cGxpbmcgb2YgZ2VuZXJhdGlvbiBhbmQgc2VsZWN0aW9uIG1ha2VzIEJvTiB0cml2aWFsbHkgcGFyYWxsZWxpc2FibGUg4oCUIGFsbCBOIGNhbmRpZGF0ZXMgY2FuIGJlIGdlbmVyYXRlZCBzaW11bHRhbmVvdXNseSBvbiBOIEdQVXMgb3IgdmlhIGJhdGNoZWQgQVBJIGNhbGxzIOKAlCBhbmQgcm9idXN0IHRvIGNvcnJlbGF0aW9uIGJldHdlZW4gY2FuZGlkYXRlcyAoc2luY2UgZWFjaCBpcyBzYW1wbGVkIGluZGVwZW5kZW50bHkpLiBEZXNwaXRlIGl0cyBzaW1wbGljaXR5LCBCb04gYWNoaWV2ZXMgcmVtYXJrYWJseSBzdHJvbmcgZW1waXJpY2FsIHJlc3VsdHM6IG9uIE1BVEgsIEJvTiB3aXRoIE49NjQgYW5kIGEgZ29vZCBPUk0gYWNoaWV2ZXMgNzIlIGFjY3VyYWN5IGZvciBhIDdCLXBhcmFtZXRlciBtb2RlbCB0aGF0IGFjaGlldmVzIG9ubHkgMzIlIHdpdGggZ3JlZWR5IGRlY29kaW5nLiBUaGUgYWNjdXJhY3ktY29tcHV0ZSBjdXJ2ZSBmb2xsb3dzIGFuIGFwcHJveGltYXRlIHBvd2VyIGxhdyBpbiBOLCBtYWtpbmcgaXQgc3RyYWlnaHRmb3J3YXJkIHRvIGVzdGltYXRlIHRoZSBOIHJlcXVpcmVkIHRvIGhpdCBhIHRhcmdldCBhY2N1cmFjeSBnaXZlbiBhIGNvc3QgYnVkZ2V0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQm9OIHBpcGVsaW5lIGhhcyB0aHJlZSBjb21wb25lbnRzOiBhIGdlbmVyYXRvciBMTE0gdGhhdCBwcm9kdWNlcyBkaXZlcnNlIGNhbmRpZGF0ZSBzb2x1dGlvbnMsIGEgc2VsZWN0aW9uIG1lY2hhbmlzbSB0aGF0IHNjb3JlcyBhbmQgcmFua3MgY2FuZGlkYXRlcywgYW5kIChvcHRpb25hbGx5KSBhIHZlcmlmaWVyIHRoYXQgcHJvdmlkZXMgZ3JvdW5kLXRydXRoIGNvcnJlY3RuZXNzIGxhYmVscyBmb3IgZXZhbHVhdGlvbi4gVGhlIGdlbmVyYXRvciBtdXN0IHByb2R1Y2Ugc3VmZmljaWVudGx5IGRpdmVyc2UgY2FuZGlkYXRlcyB0byBjb3ZlciB0aGUgc3BhY2Ugb2YgcG9zc2libGUgY29ycmVjdCBzb2x1dGlvbnMg4oCUIGRpdmVyc2l0eSBpcyBwcmltYXJpbHkgY29udHJvbGxlZCBieSB0ZW1wZXJhdHVyZSAoaGlnaGVyIFQgPSBtb3JlIGRpdmVyc2UgYnV0IGxvd2VyIGF2ZXJhZ2UgcXVhbGl0eSkuIFRoZSBzZWxlY3Rpb24gbWVjaGFuaXNtIGNhbiBiZSBhbiBPUk0gKHNjYWxhciBzY29yZSBwZXIgc29sdXRpb24pLCBhIG1ham9yaXR5IHZvdGUgb3ZlciBleHRyYWN0ZWQgZmluYWwgYW5zd2VycywgYSB3ZWlnaHRlZCBtYWpvcml0eSB2b3RlIChPUk0td2VpZ2h0ZWQgcGVyIGNhbmRpZGF0ZSksIG9yIGEgbGVhcm5lZCB2ZXJpZmllci4gQm9OIGFjY3VyYWN5IG1vbm90b25pY2FsbHkgaW1wcm92ZXMgd2l0aCBOIGZvciBhbnkgc2VsZWN0aW9uIG1lY2hhbmlzbSB0aGF0IGlzIGJldHRlciB0aGFuIHJhbmRvbSwgd2l0aCB0aGUgaW1wcm92ZW1lbnQgcmF0ZSBkZXBlbmRpbmcgb24gc2VsZWN0aW9uIHF1YWxpdHkuIFRoZSBvcmFjbGUgcGFzc0BOIHJhdGUg4oCUIHRoZSBwcm9iYWJpbGl0eSB0aGF0IGF0IGxlYXN0IG9uZSBvZiBOIHNvbHV0aW9ucyBpcyBjb3JyZWN0IOKAlCBzZXRzIGFuIHVwcGVyIGJvdW5kIG9uIEJvTiBhY2N1cmFjeTsgYSBwZXJmZWN0IHNlbGVjdG9yIHdvdWxkIGFjaGlldmUgdGhpcyBib3VuZC4gUHJhY3RpY2FsIHNlbGVjdG9ycyB0eXBpY2FsbHkgY2FwdHVyZSA3MC04NSUgb2YgdGhlIG9yYWNsZSBib3VuZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHZW5lcmF0aW9uIERpdmVyc2l0eSB2aWEgVGVtcGVyYXR1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRlbXBlcmF0dXJlIGNvbnRyb2xzIHRoZSB0cmFkZS1vZmYgYmV0d2VlbiBkaXZlcnNpdHkgYW5kIHF1YWxpdHkgaW4gdGhlIGdlbmVyYXRlZCBzb2x1dGlvbiBwb29sLiBBdCBUPTAgKGdyZWVkeSksIGFsbCBOIHNvbHV0aW9ucyBhcmUgaWRlbnRpY2FsIOKAlCBkaXZlcnNpdHkgaXMgemVybyBhbmQgQm9OIGNvbGxhcHNlcyB0byBhIHNpbmdsZS1zYW1wbGUgZXZhbHVhdGlvbi4gQXMgVCBpbmNyZWFzZXMsIHNvbHV0aW9ucyBiZWNvbWUgbW9yZSB2YXJpZWQ6IHRoZSBtb2RlbCBleHBsb3JlcyBkaWZmZXJlbnQgcHJvYmxlbS1zb2x2aW5nIGFwcHJvYWNoZXMsIHVzZXMgZGlmZmVyZW50IGludGVybWVkaWF0ZSBzdGVwcywgYW5kIGFycml2ZXMgYXQgZGlmZmVyZW50IGZpbmFsIGFuc3dlcnMgKGluY2x1ZGluZyBib3RoIGNvcnJlY3QgYW5kIGluY29ycmVjdCBvbmVzKS4gVGhlIG9wdGltYWwgdGVtcGVyYXR1cmUgZm9yIEJvTiBpcyBwcm9ibGVtLWRlcGVuZGVudDogZm9yIG5lYXItZGV0ZXJtaW5pc3RpYyBwcm9ibGVtcyB3aGVyZSB0aGUgbW9kZWwgdXN1YWxseSBrbm93cyB0aGUgYW5zd2VyIChsb3ctZGlmZmljdWx0eSksIFQ9MC42LTAuOCBwcmVzZXJ2ZXMgcXVhbGl0eSB3aGlsZSBhZGRpbmcgZGl2ZXJzaXR5LiBGb3IgaGFyZCBwcm9ibGVtcyB3aGVyZSB0aGUgbW9kZWwgcmFyZWx5IGdldHMgZ3JlZWR5IGFuc3dlcnMgY29ycmVjdCwgVD0wLjgtMS4yIGlzIGJldHRlciBiZWNhdXNlIGRpdmVyc2l0eSBpcyBtb3JlIGltcG9ydGFudCB0aGFuIHBlci1zYW1wbGUgcXVhbGl0eS4gQSBjb21tb24gaGV1cmlzdGljIGlzIHRvIHVzZSBUPTEuMCBmb3IgQm9OIGdlbmVyYXRpb24gYWNyb3NzIGFsbCBwcm9ibGVtcywgc2luY2UgaXQgcHJvdmlkZXMgc3Ryb25nIGRpdmVyc2l0eSB3aXRob3V0IGV4Y2Vzc2l2ZSBkZWdyYWRhdGlvbiBpbiBzb2x1dGlvbiBxdWFsaXR5LiBTb21lIGltcGxlbWVudGF0aW9ucyB1c2UgdGVtcGVyYXR1cmUgYW5uZWFsaW5nOiBzdGFydCBhdCBUPTEuMCBmb3IgdGhlIGZpcnN0IE4vMiBzYW1wbGVzIGFuZCBUPTAuNyBmb3IgdGhlIHNlY29uZCBoYWxmLCBjb21iaW5pbmcgaGlnaC1kaXZlcnNpdHkgYW5kIGhpZ2gtcXVhbGl0eSBzYW1wbGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IHRpbWVcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBUdXBsZSwgT3B0aW9uYWxcbmZyb20gZGF0YWNsYXNzZXMgaW1wb3J0IGRhdGFjbGFzcywgZmllbGRcbmZyb20gb3BlbmFpIGltcG9ydCBBc3luY09wZW5BSVxuXG5hY2xpZW50ID0gQXN5bmNPcGVuQUkoKVxuXG5AZGF0YWNsYXNzXG5jbGFzcyBCb25TYW1wbGU6XG4gICAgc29sdXRpb246IHN0clxuICAgIG9ybV9zY29yZTogZmxvYXQgPSAwLjBcbiAgICBpc19jb3JyZWN0OiBPcHRpb25hbFtib29sXSA9IE5vbmVcblxuYXN5bmMgZGVmIGdlbmVyYXRlX2NhbmRpZGF0ZShwcm9ibGVtOiBzdHIsIG1vZGVsOiBzdHIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGVtcGVyYXR1cmU6IGZsb2F0KSAtXHUwMDNlIHN0cjpcbiAgICByZXNwID0gYXdhaXQgYWNsaWVudC5jaGF0LmNvbXBsZXRpb25zLmNyZWF0ZShcbiAgICAgICAgbW9kZWw9bW9kZWwsIHRlbXBlcmF0dXJlPXRlbXBlcmF0dXJlLFxuICAgICAgICBtZXNzYWdlcz1be1wicm9sZVwiOiBcInVzZXJcIixcbiAgICAgICAgICAgICAgICAgICBcImNvbnRlbnRcIjogZlwiU29sdmUgc3RlcCBieSBzdGVwOiB7cHJvYmxlbX1cIn1dXG4gICAgKVxuICAgIHJldHVybiByZXNwLmNob2ljZXNbMF0ubWVzc2FnZS5jb250ZW50XG5cbmFzeW5jIGRlZiBiZXN0X29mX24ocHJvYmxlbTogc3RyLCBuOiBpbnQgPSA2NCxcbiAgICAgICAgICAgICAgICAgICAgIHRlbXBlcmF0dXJlOiBmbG9hdCA9IDEuMCxcbiAgICAgICAgICAgICAgICAgICAgIG1vZGVsOiBzdHIgPSBcImdwdC00by1taW5pXCIpIC1cdTAwM2UgTGlzdFtCb25TYW1wbGVdOlxuICAgICMgR2VuZXJhdGUgbiBjYW5kaWRhdGVzIGluIHBhcmFsbGVsOyByZXR1cm4gdW5zb3J0ZWQgbGlzdC5cbiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICBzb2x1dGlvbnMgPSBhd2FpdCBhc3luY2lvLmdhdGhlcihcbiAgICAgICAgKltnZW5lcmF0ZV9jYW5kaWRhdGUocHJvYmxlbSwgbW9kZWwsIHRlbXBlcmF0dXJlKSBmb3IgXyBpbiByYW5nZShuKV1cbiAgICApXG4gICAgZWxhcHNlZCA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgIHNhbXBsZXMgPSBbQm9uU2FtcGxlKHNvbHV0aW9uPXMpIGZvciBzIGluIHNvbHV0aW9uc11cbiAgICBwcmludChmXCJHZW5lcmF0ZWQge259IGNhbmRpZGF0ZXMgaW4ge2VsYXBzZWQ6LjJmfXMgKHtlbGFwc2VkL24qMTAwMDouMGZ9bXMgZWFjaClcIilcbiAgICByZXR1cm4gc2FtcGxlcyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlbGVjdGlvbiBTdHJhdGVnaWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaHJlZSBtYWluIHNlbGVjdGlvbiBzdHJhdGVnaWVzIGFyZSB1c2VkIGluIHByYWN0aWNlLCBlYWNoIHdpdGggZGlmZmVyZW50IGFjY3VyYWN5LWNvc3QgdHJhZGUtb2Zmcy4gT1JNIHNlbGVjdGlvbiBzY29yZXMgZWFjaCBjYW5kaWRhdGUgd2l0aCBhIHRyYWluZWQgcmV3YXJkIG1vZGVsIGFuZCByZXR1cm5zIHRoZSBjYW5kaWRhdGUgd2l0aCB0aGUgaGlnaGVzdCBzY29yZTsgdGhpcyByZXF1aXJlcyBhIHByZS10cmFpbmVkIE9STSBidXQgYWNoaWV2ZXMgdGhlIGJlc3QgYWNjdXJhY3kuIE1ham9yaXR5IHZvdGUgKHNlbGYtY29uc2lzdGVuY3kpIGV4dHJhY3RzIHRoZSBmaW5hbCBhbnN3ZXIgZnJvbSBlYWNoIGNhbmRpZGF0ZSwgY29tcHV0ZXMgdGhlIHBsdXJhbGl0eSBhbnN3ZXIsIGFuZCByZXR1cm5zIGFueSBjYW5kaWRhdGUgdGhhdCBwcm9kdWNlZCB0aGF0IGFuc3dlcjsgdGhpcyByZXF1aXJlcyBubyBhZGRpdGlvbmFsIG1vZGVsIGJ1dCBpcyBsaW1pdGVkIHRvIHByb2JsZW1zIHdpdGggZGlzY3JldGUgZmluYWwgYW5zd2VycyAobnVtYmVycywgbXVsdGlwbGUgY2hvaWNlKS4gV2VpZ2h0ZWQgbWFqb3JpdHkgdm90ZSBjb21iaW5lcyBib3RoOiBlYWNoIGNhbmRpZGF0ZVx1MDAyN3Mgdm90ZSBpcyB3ZWlnaHRlZCBieSBpdHMgT1JNIHNjb3JlLCBzbyBjYW5kaWRhdGVzIHRoYXQgYXJlIGJvdGggcG9wdWxhciAobWFueSBhZ3JlZSkgYW5kIGhpZ2gtc2NvcmluZyAoT1JNIGNvbmZpZGVudCkgcmVjZWl2ZSBleHRyYSB3ZWlnaHQuIFdlaWdodGVkIG1ham9yaXR5IHZvdGUgY29uc2lzdGVudGx5IG91dHBlcmZvcm1zIGJvdGggdW53ZWlnaHRlZCBtYWpvcml0eSB2b3RlIGFuZCBwbGFpbiBPUk0gc2VsZWN0aW9uIG9uIG1hdGhlbWF0aWNhbCBiZW5jaG1hcmtzLCBwYXJ0aWN1bGFybHkgYXQgc21hbGwgTiAoNC04KSB3aGVyZSB0aGUgT1JNIHNpZ25hbCBhbmQgdGhlIGRpdmVyc2l0eSBzaWduYWwgYXJlIGJvdGggbm9pc3kuIFRoZSBwZXJmb3JtYW5jZSBnYXAgbmFycm93cyBhdCBsYXJnZSBOICg2NCspIHdoZXJlIGJvdGggbWV0aG9kcyBhcHByb2FjaCB0aGUgb3JhY2xlIHBhc3NATiBib3VuZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYWpvcml0eSBWb3RlIChTZWxmLUNvbnNpc3RlbmN5KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWFqb3JpdHkgdm90ZSwgaW50cm9kdWNlZCBhcyBTZWxmLUNvbnNpc3RlbmN5IGJ5IFdhbmcgZXQgYWwuICgyMDIyKSwgaXMgdGhlIHNpbXBsZXN0IE9STS1mcmVlIHNlbGVjdGlvbiBzdHJhdGVneSBmb3IgQm9OLiBFYWNoIG9mIHRoZSBOIGNhbmRpZGF0ZXMgaXMgZGVjb2RlZCBpbmRlcGVuZGVudGx5ICh0eXBpY2FsbHkgYXQgdGVtcGVyYXR1cmUgMC41LTEuMCksIHRoZSBmaW5hbCBhbnN3ZXIgaXMgZXh0cmFjdGVkICh2aWEgcmVnZXggb3IgbW9kZWwtYmFzZWQgZXh0cmFjdGlvbiksIGFuZCB0aGUgcGx1cmFsaXR5IGFuc3dlciBpcyByZXR1cm5lZC4gU2VsZi1jb25zaXN0ZW5jeSBpcyByZW1hcmthYmx5IGVmZmVjdGl2ZTogb24gR1NNOEssIG1ham9yaXR5IHZvdGUgd2l0aCBOPTQwIHNhbXBsZXMgb2YgQ2hhaW4tb2YtVGhvdWdodCByZWFzb25pbmcgYWNoaWV2ZXMgNzQlIGFjY3VyYWN5IHZlcnN1cyA1NiUgZm9yIGEgc2luZ2xlIENvVCBzYW1wbGUsIGEgMTgtcG9pbnQgaW1wcm92ZW1lbnQgd2l0aCB6ZXJvIGFkZGl0aW9uYWwgbW9kZWwgdHJhaW5pbmcuIFRoZSBrZXkgaW50dWl0aW9uIGlzIHRoYXQgY29ycmVjdCByZWFzb25pbmcgcGF0aHMgdGVuZCB0byBjb252ZXJnZSBvbiB0aGUgc2FtZSBmaW5hbCBhbnN3ZXIgd2hpbGUgaW5jb3JyZWN0IHBhdGhzIG1ha2UgZGl2ZXJzZSBlcnJvcnMuIE1ham9yaXR5IHZvdGUgYW1wbGlmaWVzIHRoaXMgc2lnbmFsIGJ5IGNvdW50aW5nIHZvdGVzLiBJdHMgbWFpbiBsaW1pdGF0aW9uIGlzIHRoYXQgaXQgcmVxdWlyZXMgYSBkaXNjcmV0ZSBmaW5hbCBhbnN3ZXIgdG8gYmUgZXh0cmFjdGFibGUg4oCUIG9wZW4tZW5kZWQgZ2VuZXJhdGlvbiB0YXNrcywgY29kZSBnZW5lcmF0aW9uLCBhbmQgZXNzYXkgd3JpdGluZyBjYW5ub3QgdXNlIG5haXZlIG1ham9yaXR5IHZvdGUgd2l0aG91dCBhZGRpdGlvbmFsIHN0cnVjdHVyZS4gRm9yIGNvZGUsIG1ham9yaXR5IHZvdGUgY2FuIGJlIGFwcGxpZWQgb3ZlciB0ZXN0LXBhc3Npbmcgb3V0Y29tZXMgcmF0aGVyIHRoYW4gc3RyaW5nIGVxdWFsaXR5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXJcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBPcHRpb25hbCwgVHVwbGVcblxuZGVmIGV4dHJhY3RfZmluYWxfYW5zd2VyKHRleHQ6IHN0cikgLVx1MDAzZSBPcHRpb25hbFtzdHJdOlxuICAgICMgVHJ5IGNvbW1vbiBwYXR0ZXJuczogYm94ZWQgYW5zd2VyLCBcIj0gWFwiIGF0IGVuZCwgbGFzdCBudW1iZXIuXG4gICAgYm94ZWQgPSByZS5zZWFyY2goclwiXFxcXGJveGVkXFx7KFtefV0rKVxcfVwiLCB0ZXh0KVxuICAgIGlmIGJveGVkOlxuICAgICAgICByZXR1cm4gYm94ZWQuZ3JvdXAoMSkuc3RyaXAoKVxuICAgIGVxX2VuZCA9IHJlLnNlYXJjaChyXCI9XFxzKihbXFxkLi8tXSspXFxzKiRcIiwgdGV4dC5zdHJpcCgpKVxuICAgIGlmIGVxX2VuZDpcbiAgICAgICAgcmV0dXJuIGVxX2VuZC5ncm91cCgxKS5zdHJpcCgpXG4gICAgbnVtcyA9IHJlLmZpbmRhbGwoclwiWy0rXT9cXGQqXFwuP1xcZCtcIiwgdGV4dC5yZXBsYWNlKFwiLFwiLCBcIlwiKSlcbiAgICByZXR1cm4gbnVtc1stMV0gaWYgbnVtcyBlbHNlIE5vbmVcblxuZGVmIG1ham9yaXR5X3ZvdGUoc29sdXRpb25zOiBMaXN0W3N0cl0sXG4gICAgICAgICAgICAgICAgICBvcm1fc2NvcmVzOiBPcHRpb25hbFtMaXN0W2Zsb2F0XV0gPSBOb25lKSAtXHUwMDNlIFR1cGxlW3N0ciwgc3RyXTpcbiAgICAjIEV4dHJhY3QgYW5zd2VycywgY29tcHV0ZSBwbHVyYWxpdHk7IGJyZWFrIHRpZXMgdXNpbmcgT1JNIHNjb3JlLlxuICAgIGFuc3dlcnMgPSBbZXh0cmFjdF9maW5hbF9hbnN3ZXIocykgb3IgXCJcIiBmb3IgcyBpbiBzb2x1dGlvbnNdXG4gICAgY291bnRzICA9IENvdW50ZXIoYSBmb3IgYSBpbiBhbnN3ZXJzIGlmIGEpXG4gICAgaWYgbm90IGNvdW50czpcbiAgICAgICAgcmV0dXJuIHNvbHV0aW9uc1swXSwgXCJmYWxsYmFja1wiXG4gICAgcGx1cmFsaXR5X2Fuc3dlciA9IGNvdW50cy5tb3N0X2NvbW1vbigxKVswXVswXVxuICAgIGNhbmRpZGF0ZXMgPSBbKHMsIHNjKSBmb3IgcywgYSwgc2MgaW5cbiAgICAgICAgICAgICAgICAgIHppcChzb2x1dGlvbnMsIGFuc3dlcnMsIG9ybV9zY29yZXMgb3IgWzAuMF0qbGVuKHNvbHV0aW9ucykpXG4gICAgICAgICAgICAgICAgICBpZiBhID09IHBsdXJhbGl0eV9hbnN3ZXJdXG4gICAgaWYgb3JtX3Njb3JlczpcbiAgICAgICAgYmVzdCA9IG1heChjYW5kaWRhdGVzLCBrZXk9bGFtYmRhIHg6IHhbMV0pXG4gICAgZWxzZTpcbiAgICAgICAgYmVzdCA9IGNhbmRpZGF0ZXNbMF1cbiAgICB2b3RlX3BjdCA9IGNvdW50c1twbHVyYWxpdHlfYW5zd2VyXSAvIGxlbihhbnN3ZXJzKSAqIDEwMFxuICAgIHByaW50KGZcIlBsdXJhbGl0eSBhbnN3ZXI6IHtwbHVyYWxpdHlfYW5zd2VyfSAoe3ZvdGVfcGN0Oi4xZn0lIG9mIHtsZW4oYW5zd2Vycyl9IHZvdGVzKVwiKVxuICAgIHJldHVybiBiZXN0WzBdLCBwbHVyYWxpdHlfYW5zd2VyIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmV3YXJkIE1vZGVsIFNlbGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT1JNLWJhc2VkIHNlbGVjdGlvbiBzY29yZXMgZWFjaCBvZiB0aGUgTiBjYW5kaWRhdGVzIHdpdGggYSByZXdhcmQgbW9kZWwgYW5kIHJldHVybnMgdGhlIGhpZ2hlc3Qtc2NvcmluZyBjYW5kaWRhdGUuIFRoaXMgYXBwcm9hY2ggcmVxdWlyZXMgYSBwcmUtdHJhaW5lZCBPUk0gYnV0IGNhcHR1cmVzIGluZm9ybWF0aW9uIHRoYXQgbWFqb3JpdHkgdm90ZSBtaXNzZXM6IGEgdW5pcXVlbHkgY29ycmVjdCBzb2x1dGlvbiB0aGF0IG5vIG90aGVyIGNhbmRpZGF0ZSBhZ3JlZXMgd2l0aCB3aWxsIGJlIHNlbGVjdGVkIGJ5IHRoZSBPUk0gaWYgaXQgc2NvcmVzIGhpZ2gsIGJ1dCBpZ25vcmVkIGJ5IG1ham9yaXR5IHZvdGUuIE9STSBzZWxlY3Rpb24gaXMgc3RyaWN0bHkgYmV0dGVyIHRoYW4gbWFqb3JpdHkgdm90ZSB3aGVuIHRoZSBPUk0gaXMgd2VsbC1jYWxpYnJhdGVkIChBVVJPQyBcdTAwM2UgMC44MCkgYW5kIE4gaXMgbGFyZ2UgZW5vdWdoIHRoYXQgZGl2ZXJzaXR5IGlzIG5vdCB0aGUgbGltaXRpbmcgZmFjdG9yLiBUaGUgT1JNIHNjb3Jpbmcgc3RlcCBhZGRzIGxhdGVuY3kgcHJvcG9ydGlvbmFsIHRvIE4gKGVhY2ggY2FuZGlkYXRlIG11c3QgYmUgc2NvcmVkKSwgYnV0IHRoaXMgaXMgb2Z0ZW4gYWNjZXB0YWJsZSBzaW5jZSB0aGUgZ2VuZXJhdGlvbiBzdGVwICh3aGljaCBhbHNvIHJ1bnMgTiB0aW1lcykgZG9taW5hdGVzIGxhdGVuY3kuIFdoZW4gdXNpbmcgYSBsYXJnZSBPUk0gKGUuZy4sIGEgMTNCLXBhcmFtZXRlciByZXdhcmQgbW9kZWwgdG8gc2NvcmUgYSA3QiBnZW5lcmF0b3IpLCB0aGUgT1JNIHNjb3Jpbmcgc3RlcCBjYW4gdGFrZSBhcyBsb25nIGFzIGdlbmVyYXRpb24g4oCUIGEgMTNCIE9STSBzY29yaW5nIDY0IGNhbmRpZGF0ZXMgbWF5IHRha2UgMTI4IHNlY29uZHMgb24gYSBzaW5nbGUgQTEwMC4gUXVhbnRpc2luZyB0aGUgT1JNIHRvIDQtYml0IG9yIHVzaW5nIGEgc21hbGxlciBPUk0gKDNCLTdCKSBjYW4gcmVkdWNlIHRoaXMgdG8gMjAtNDAgc2Vjb25kcyB3aXRoIG1pbmltYWwgYWNjdXJhY3kgbG9zcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTiBzYW1wbGVzIiwiVGVtcGVyYXR1cmUiLCJTZWxlY3Rpb24iLCJNQVRIIGFjY3VyYWN5IiwiQ29zdCAoMWsgcXVlcmllcykiLCJOb3RlcyJdLCJyb3dzIjpbWyJOPTEiLCIwLjAgKGdyZWVkeSkiLCLigJQiLCIzMiUiLCIkMC40MCIsIkJhc2VsaW5lOiBzaW5nbGUgZ3JlZWR5IHNhbXBsZSJdLFsiTj00IiwiMC44IiwiTWFqb3JpdHkgdm90ZSIsIjQ2JSIsIiQxLjYwIiwiU2ltcGxlIHZvdGU7IG5vIE9STSBuZWVkZWQiXSxbIk49MTYiLCIxLjAiLCJPUk0gc2VsZWN0aW9uIiwiNjElIiwiJDYuNDAiLCJTdHJvbmcgT1JNIHJlcXVpcmVkOyBnb29kIGFjY3VyYWN5Il0sWyJOPTY0IiwiMS4wIiwiT1JNIHNlbGVjdGlvbiIsIjcyJSIsIiQyNS42MCIsIk5lYXItc2F0dXJhdGluZyBmb3IgN0IgbW9kZWwiXSxbIk49MjU2IiwiMS4wIiwiT1JNIHNlbGVjdGlvbiIsIjc3JSIsIiQxMDIuNDAiLCJEaW1pbmlzaGluZyByZXR1cm5zOyBleHBlbnNpdmUiXSxbIk9yYWNsZSBOPTY0IiwiMS4wIiwiUGVyZmVjdCB2ZXJpZmllciIsIjg0JSIsIuKAlCIsIlVwcGVyIGJvdW5kOiBhbnktb2YtNjQgY29ycmVjdCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2VpZ2h0ZWQgTWFqb3JpdHkgVm90ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2VpZ2h0ZWQgbWFqb3JpdHkgdm90ZSAoV01WKSBjb21iaW5lcyBPUk0gc2NvcmVzIGFuZCBwbHVyYWxpdHkgdm90aW5nIGludG8gYSBzaW5nbGUgc2VsZWN0aW9uIGNyaXRlcmlvbi4gRm9yIGVhY2ggdW5pcXVlIGV4dHJhY3RlZCBhbnN3ZXIgYSwgV01WIGNvbXB1dGVzIGEgd2VpZ2h0IFcoYSkgPSBzdW0gb2YgZXhwKE9STV9zY29yZV9pKSBmb3IgYWxsIGNhbmRpZGF0ZXMgaSB3aG9zZSBleHRyYWN0ZWQgYW5zd2VyIGVxdWFscyBhLiBUaGUgYW5zd2VyIHdpdGggdGhlIGhpZ2hlc3QgdG90YWwgd2VpZ2h0IGlzIHNlbGVjdGVkLCBhbmQgYW55IGNhbmRpZGF0ZSB3aXRoIHRoYXQgYW5zd2VyIGlzIHJldHVybmVkICh0eXBpY2FsbHkgdGhlIGhpZ2hlc3QtT1JNLXNjb3Jpbmcgb25lKS4gV01WIG91dHBlcmZvcm1zIGJvdGggdW53ZWlnaHRlZCBtYWpvcml0eSB2b3RlIGFuZCBwbGFpbiBPUk0gc2VsZWN0aW9uIGF0IHNtYWxsIE4gKDQtMTYpIGJlY2F1c2UgaXQgZXhwbG9pdHMgdHdvIGNvbXBsZW1lbnRhcnkgc2lnbmFsczogdGhlIE9STSBzaWduYWwgKHdoaWNoIGNhbmRpZGF0ZSBpcyBpbmRpdmlkdWFsbHkgbW9zdCBwbGF1c2libGUpIGFuZCB0aGUgYWdyZWVtZW50IHNpZ25hbCAod2hpY2ggYW5zd2VyIGlzIG1vc3Qgcm9idXN0bHkgcmVhY2hlZCBieSBkaWZmZXJlbnQgcmVhc29uaW5nIHBhdGhzKS4gQXQgTj00LCBXTVYgdHlwaWNhbGx5IG91dHBlcmZvcm1zIHBsYWluIE9STSBzZWxlY3Rpb24gYnkgMi00IHBlcmNlbnRhZ2UgcG9pbnRzIG9uIE1BVEguIEF0IE49NjQsIHRoZSBkaWZmZXJlbmNlIG5hcnJvd3MgdG8gMC41LTEuNSBwb2ludHMuIFdNViBhZGRzIG5lZ2xpZ2libGUgbGF0ZW5jeSBiZXlvbmQgT1JNIHNjb3JpbmcgYW5kIGlzIHN0cmFpZ2h0Zm9yd2FyZCB0byBpbXBsZW1lbnQ7IGl0IHNob3VsZCBiZSB0aGUgZGVmYXVsdCBzZWxlY3Rpb24gc3RyYXRlZ3kgZm9yIGFueSBCb04gc3lzdGVtIHRoYXQgYWxyZWFkeSBoYXMgYW4gT1JNLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbWF0aFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVmYXVsdGRpY3RcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBUdXBsZSwgT3B0aW9uYWxcblxuZGVmIHdlaWdodGVkX21ham9yaXR5X3ZvdGUoc29sdXRpb25zOiBMaXN0W3N0cl0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgb3JtX3Njb3JlczogTGlzdFtmbG9hdF0pIC1cdTAwM2UgVHVwbGVbc3RyLCBzdHIsIGZsb2F0XTpcbiAgICAjIFdNVjogd2VpZ2h0IGVhY2ggYW5zd2VyIGJ5IHN1bSBvZiBleHAoT1JNIHNjb3JlKSBvZiBhZ3JlZWluZyBjYW5kaWRhdGVzLlxuICAgIGFuc3dlcnMgPSBbZXh0cmFjdF9maW5hbF9hbnN3ZXIocykgb3IgXCJcIiBmb3IgcyBpbiBzb2x1dGlvbnNdXG4gICAgd2VpZ2h0X21hcDogZGljdCA9IGRlZmF1bHRkaWN0KGZsb2F0KVxuICAgIHNjb3JlX21hcDogIGRpY3QgPSBkZWZhdWx0ZGljdChsaXN0KVxuICAgIGZvciBzLCBhLCBzYyBpbiB6aXAoc29sdXRpb25zLCBhbnN3ZXJzLCBvcm1fc2NvcmVzKTpcbiAgICAgICAgaWYgYTpcbiAgICAgICAgICAgIHdlaWdodF9tYXBbYV0gKz0gbWF0aC5leHAoc2MpICAgICAgICAjIGV4cG9uZW50aWFsIHdlaWdodGluZ1xuICAgICAgICAgICAgc2NvcmVfbWFwW2FdLmFwcGVuZCgoc2MsIHMpKVxuICAgIGlmIG5vdCB3ZWlnaHRfbWFwOlxuICAgICAgICByZXR1cm4gc29sdXRpb25zWzBdLCBcIlwiLCBvcm1fc2NvcmVzWzBdXG4gICAgYmVzdF9hbnMgID0gbWF4KHdlaWdodF9tYXAsIGtleT1sYW1iZGEgYTogd2VpZ2h0X21hcFthXSlcbiAgICBiZXN0X3NvbCAgPSBtYXgoc2NvcmVfbWFwW2Jlc3RfYW5zXSwga2V5PWxhbWJkYSB4OiB4WzBdKVsxXVxuICAgIHRvdGFsX3cgICA9IHN1bSh3ZWlnaHRfbWFwLnZhbHVlcygpKVxuICAgIGNvbmYgICAgICA9IHdlaWdodF9tYXBbYmVzdF9hbnNdIC8gdG90YWxfd1xuICAgIHByaW50KGZcIldNViB3aW5uZXI6IHtiZXN0X2Fuc30gIGNvbmZpZGVuY2U6IHtjb25mOi4zZn1cIilcbiAgICByZXR1cm4gYmVzdF9zb2wsIGJlc3RfYW5zLCBjb25mXG5cbmRlZiBjb21wYXJlX3NlbGVjdGlvbl9tZXRob2RzKHNvbHV0aW9uczogTGlzdFtzdHJdLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9ybV9zY29yZXM6IExpc3RbZmxvYXRdKSAtXHUwMDNlIE5vbmU6XG4gICAgIyBDb21wYXJlIE9STS1vbmx5LCBtYWpvcml0eSB2b3RlLCBhbmQgV01WIG9uIHRoZSBzYW1lIGNhbmRpZGF0ZSBwb29sLlxuICAgIG9ybV9iZXN0ICA9IHNvbHV0aW9uc1ttYXgocmFuZ2UobGVuKHNvbHV0aW9ucykpLCBrZXk9bGFtYmRhIGk6IG9ybV9zY29yZXNbaV0pXVxuICAgIG12X3NvbCwgbXZfYW5zID0gbWFqb3JpdHlfdm90ZShzb2x1dGlvbnMsIE5vbmUpXG4gICAgd21fc29sLCB3bV9hbnMsIHdtX2NvbmYgPSB3ZWlnaHRlZF9tYWpvcml0eV92b3RlKHNvbHV0aW9ucywgb3JtX3Njb3JlcylcbiAgICBwcmludChmXCJPUk0gYmVzdCBhbnN3ZXIgOiB7ZXh0cmFjdF9maW5hbF9hbnN3ZXIob3JtX2Jlc3QpfVwiKVxuICAgIHByaW50KGZcIk1ham9yaXR5IHZvdGUgICA6IHttdl9hbnN9XCIpXG4gICAgcHJpbnQoZlwiV2VpZ2h0ZWQgTVYgICAgIDoge3dtX2Fuc30gKGNvbmY9e3dtX2NvbmY6LjNmfSlcIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQWNjdXJhY3ktQ29zdCBTd2VldCBTcG90IiwiY29udGVudCI6IkJlc3Qtb2YtNCB3aXRoIGEgbGlnaHR3ZWlnaHQgT1JNIHR5cGljYWxseSBhY2hpZXZlcyA4MC05MCUgb2YgdGhlIGdhaW4gb2YgYmVzdC1vZi02NCBhdCAxLzE2IHRoZSBjb3N0IOKAlCBhbHdheXMgYmVuY2htYXJrIHRoZSBhY2N1cmFjeS1jb3N0IGN1cnZlIGJlZm9yZSBjb21taXR0aW5nIHRvIGEgbGFyZ2UgTi4gRm9yIG1vc3QgcHJvZHVjdGlvbiB1c2UgY2FzZXMsIE49OCB0byBOPTE2IHdpdGggT1JNIHNlbGVjdGlvbiBwcm92aWRlcyBhbiBleGNlbGxlbnQgYWNjdXJhY3ktY29zdCB0cmFkZS1vZmY6IDYtMTIgcGVyY2VudGFnZSBwb2ludHMgb2YgTUFUSCBhY2N1cmFjeSBpbXByb3ZlbWVudCBvdmVyIGdyZWVkeSBhdCA4LTE2eCB0aGUgaW5mZXJlbmNlIGNvc3QuIFJlc2VydmUgTj02NCsgZm9yIG9mZmxpbmUgYmF0Y2ggZXZhbHVhdGlvbiBvciBoaWdoLXZhbHVlIHF1ZXJpZXMgd2hlcmUgbGF0ZW5jeSBpcyBub3QgYSBjb25zdHJhaW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNjYWxpbmcgTGF3cyBmb3IgQmVzdC1vZi1OIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQm9OIGFjY3VyYWN5LWNvbXB1dGUgcmVsYXRpb25zaGlwIGZvbGxvd3MgYW4gYXBwcm94aW1hdGUgcG93ZXIgbGF3OiBhY2N1cmFjeShOKSDiiYggb3JhY2xlX3Bhc3NfcmF0ZSAtIChvcmFjbGVfcGFzc19yYXRlIC0gcGFzc0AxKSAqIE5eey1hbHBoYX0sIHdoZXJlIGFscGhhIGRlcGVuZHMgb24gdGhlIHNlbGVjdG9yIHF1YWxpdHkgYW5kIHRoZSBwcm9ibGVtIGRpZmZpY3VsdHkgZGlzdHJpYnV0aW9uLiBGb3IgYSB3ZWxsLWNhbGlicmF0ZWQgT1JNIG9uIE1BVEgsIGFscGhhIOKJiCAwLjMtMC41LCBtZWFuaW5nIGFjY3VyYWN5IHNjYWxlcyByb3VnaGx5IGFzIHRoZSBzcXVhcmUgcm9vdCBvZiB0aGUgbnVtYmVyIG9mIHNhbXBsZXMg4oCUIGRvdWJsaW5nIE4gZnJvbSAxNiB0byAzMiBnaXZlcyByb3VnaGx5IHRoZSBzYW1lIGFjY3VyYWN5IGdhaW4gYXMgdGhlIGp1bXAgZnJvbSA4IHRvIDE2LiBUaGlzIHN1Yi1saW5lYXIgc2NhbGluZyBtZWFucyB0aGF0IHRoZSBtYXJnaW5hbCB2YWx1ZSBvZiBhZGRpdGlvbmFsIHNhbXBsZXMgZGVjcmVhc2VzIHJhcGlkbHkuIEEgdXNlZnVsIHJ1bGUgb2YgdGh1bWI6IDgwJSBvZiB0aGUgZ2FwIGJldHdlZW4gcGFzc0AxIGFuZCBvcmFjbGUgcGFzc0BOIGlzIGNhcHR1cmVkIGJ5IE4g4omIIChvcmFjbGVfcGFzc19yYXRlIC8gKDEtcGFzc0AxKSleezEvYWxwaGF9LiBGb3IgYSBtb2RlbCB3aXRoIDMyJSBwYXNzQDEgYW5kIDg0JSBvcmFjbGUgcGFzc0A2NCwgcmVhY2hpbmcgOTAlIG9mIHRoZSBvcmFjbGUgcmVxdWlyZXMgTiDiiYggMzIuIEZpdHRpbmcgdGhlIHBvd2VyIGxhdyBvbiBhIHNtYWxsIHZhbGlkYXRpb24gc2V0IChOPTEsMiw0LDgsMTYsMzIpIGFuZCBleHRyYXBvbGF0aW5nIHRvIGxhcmdlciBOIGlzIGFuIGVmZmVjdGl2ZSB3YXkgdG8gZXN0aW1hdGUgdGhlIE4gbmVlZGVkIHRvIGhpdCBhIHRhcmdldCBhY2N1cmFjeSB3aXRob3V0IHJ1bm5pbmcgdGhlIGZ1bGwgYmVuY2htYXJrLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IGN1cnZlX2ZpdFxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3QsIFR1cGxlXG5cbmRlZiBwb3dlcl9sYXdfZml0KG5fdmFsdWVzOiBMaXN0W2ludF0sXG4gICAgICAgICAgICAgICAgICBhY2N1cmFjaWVzOiBMaXN0W2Zsb2F0XSkgLVx1MDAzZSBUdXBsZVtmbG9hdCwgZmxvYXQsIGZsb2F0XTpcbiAgICAjIEZpdCBhY2N1cmFjeShOKSA9IG9yYWNsZSAtIChvcmFjbGUgLSBiYXNlKSAqIE5eKC1hbHBoYSlcbiAgICAjIFJldHVybnMgKG9yYWNsZV9yYXRlLCBiYXNlX3JhdGUsIGFscGhhKVxuICAgIG5fYXJyID0gbnAuYXJyYXkobl92YWx1ZXMsIGR0eXBlPWZsb2F0KVxuICAgIGFfYXJyID0gbnAuYXJyYXkoYWNjdXJhY2llcywgZHR5cGU9ZmxvYXQpXG4gICAgZGVmIG1vZGVsKG4sIG9yYWNsZSwgYmFzZSwgYWxwaGEpOlxuICAgICAgICByZXR1cm4gb3JhY2xlIC0gKG9yYWNsZSAtIGJhc2UpICogbioqKC1hbHBoYSlcbiAgICBwMCA9ICgwLjg0LCBhX2FyclswXSwgMC40KVxuICAgIHBvcHQsIF8gPSBjdXJ2ZV9maXQobW9kZWwsIG5fYXJyLCBhX2FyciwgcDA9cDAsIG1heGZldj01MDAwKVxuICAgIG9yYWNsZSwgYmFzZSwgYWxwaGEgPSBwb3B0XG4gICAgcHJpbnQoZlwiRml0dGVkIHBvd2VyIGxhdzogb3JhY2xlPXtvcmFjbGU6LjNmfSAgYmFzZT17YmFzZTouM2Z9ICBhbHBoYT17YWxwaGE6LjNmfVwiKVxuICAgIHJldHVybiBvcmFjbGUsIGJhc2UsIGFscGhhXG5cbmRlZiBvcHRpbWFsX24odGFyZ2V0X2FjYzogZmxvYXQsIGNvc3RfcGVyX3NhbXBsZTogZmxvYXQsXG4gICAgICAgICAgICAgICBvcmFjbGU6IGZsb2F0LCBiYXNlOiBmbG9hdCwgYWxwaGE6IGZsb2F0KSAtXHUwMDNlIGludDpcbiAgICAjIEZpbmQgc21hbGxlc3QgTiBhY2hpZXZpbmcgdGFyZ2V0X2FjYyBhbmQgZXN0aW1hdGUgY29zdC5cbiAgICBuID0gMVxuICAgIHdoaWxlIFRydWU6XG4gICAgICAgIGFjYyA9IG9yYWNsZSAtIChvcmFjbGUgLSBiYXNlKSAqIChuICoqICgtYWxwaGEpKVxuICAgICAgICBpZiBhY2MgXHUwMDNlPSB0YXJnZXRfYWNjIG9yIG4gXHUwMDNlIDEwMjQ6XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBuICo9IDJcbiAgICBjb3N0ID0gbiAqIGNvc3RfcGVyX3NhbXBsZVxuICAgIHByaW50KGZcIk49e259IGFjaGlldmVzIGFjYz17b3JhY2xlLShvcmFjbGUtYmFzZSkqbioqKC1hbHBoYSk6LjNmfSBjb3N0PSR7Y29zdDouNGZ9XCIpXG4gICAgcmV0dXJuIG5cblxuIyBFbXBpcmljYWwgTUFUSCBhY2N1cmFjeSBmb3IgTGxhbWEtMi03QiArIE9STSBhY3Jvc3MgTiB2YWx1ZXNcbm5fdmFsdWVzICAgPSBbMSwgMiwgNCwgOCwgMTYsIDMyLCA2NCwgMTI4XVxuYWNjdXJhY2llcyA9IFswLjMyLCAwLjQxLCAwLjUxLCAwLjU5LCAwLjY1LCAwLjcwLCAwLjcyLCAwLjc0XVxub3JhY2xlLCBiYXNlLCBhbHBoYSA9IHBvd2VyX2xhd19maXQobl92YWx1ZXMsIGFjY3VyYWNpZXMpXG5vcHRpbWFsX24odGFyZ2V0X2FjYz0wLjcwLCBjb3N0X3Blcl9zYW1wbGU9MC4wMDA0LCBvcmFjbGU9b3JhY2xlLFxuICAgICAgICAgIGJhc2U9YmFzZSwgYWxwaGE9YWxwaGEpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVzdC1vZi1OIHNhbXBsaW5nIGlzIHRoZSBtb3N0IHByYWN0aWNhbCBlbnRyeSBwb2ludCBmb3IgdGVzdC10aW1lIGNvbXB1dGUgc2NhbGluZyBkdWUgdG8gaXRzIHNpbXBsaWNpdHksIHBhcmFsbGVsaXNhYmlsaXR5LCBhbmQgc3Ryb25nIGVtcGlyaWNhbCByZXN1bHRzLiBUaGUgdGhyZWUgc2VsZWN0aW9uIHN0cmF0ZWdpZXMg4oCUIE9STSBzZWxlY3Rpb24sIG1ham9yaXR5IHZvdGUsIGFuZCB3ZWlnaHRlZCBtYWpvcml0eSB2b3RlIOKAlCBjb3ZlciBhIGJyb2FkIHJhbmdlIG9mIGRlcGxveW1lbnQgc2NlbmFyaW9zLCBmcm9tIHplcm8tYWRkaXRpb25hbC1tb2RlbCAobWFqb3JpdHkgdm90ZSkgdG8gZnVsbCBPUk0gKFdNVikuIFRoZSBhY2N1cmFjeS1jb21wdXRlIGN1cnZlIGZvbGxvd3MgYSBwb3dlciBsYXcgd2l0aCBkaW1pbmlzaGluZyByZXR1cm5zOyBhbHdheXMgYmVuY2htYXJrIE49MSw0LDE2LDY0IGFuZCBmaXQgdGhlIGN1cnZlIGJlZm9yZSBkZWNpZGluZyBvbiBhIHByb2R1Y3Rpb24gTi4gRm9yIG1vc3QgYXBwbGljYXRpb25zLCBOPTgtMTYgd2l0aCBPUk0gc2VsZWN0aW9uIGNhcHR1cmVzIHRoZSBidWxrIG9mIHRoZSBhY2N1cmFjeSBnYWluIGF0IGEgbWFuYWdlYWJsZSBjb3N0LiBXZWlnaHRlZCBtYWpvcml0eSB2b3RlIGlzIHRoZSByZWNvbW1lbmRlZCBkZWZhdWx0IHdoZW4gYW4gT1JNIGlzIGF2YWlsYWJsZSwgc2luY2UgaXQgZXhwbG9pdHMgYm90aCB0aGUgaW5kaXZpZHVhbCBxdWFsaXR5IHNpZ25hbCBhbmQgdGhlIHNvbHV0aW9uIGFncmVlbWVudCBzaWduYWwgYXQgbm8gYWRkaXRpb25hbCBsYXRlbmN5IGNvc3QuIEJleW9uZCBOPTY0LCBNQ1RTIGFuZCBvdGhlciBzdHJ1Y3R1cmVkIHNlYXJjaCBtZXRob2RzIGJlZ2luIHRvIG91dHBlcmZvcm0gZmxhdCBCb04gYXQgZXF1aXZhbGVudCB0b2tlbiBidWRnZXRzIGJ5IHVzaW5nIHRoZSBjb21wdXRlIG1vcmUgZWZmaWNpZW50bHkgdGhyb3VnaCBhZGFwdGl2ZSBleHBsb3JhdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdlbmVyYXRlIE4gY2FuZGlkYXRlcyBpbiBwYXJhbGxlbCBhdCB0ZW1wZXJhdHVyZSAxLjA7IHNjb3JlIHdpdGggT1JNOyByZXR1cm4gdGhlIGhpZ2hlc3Qtc2NvcmluZyBzb2x1dGlvbiIsIk1ham9yaXR5IHZvdGUgKHNlbGYtY29uc2lzdGVuY3kpIG5lZWRzIG5vIE9STTogcmV0dXJuIHRoZSBwbHVyYWxpdHkgZmluYWwgYW5zd2VyIGFjcm9zcyBOIHNhbXBsZXMiLCJXZWlnaHRlZCBtYWpvcml0eSB2b3RlOiBXKGEpID0gc3VtIG9mIGV4cChPUk1fc2NvcmUpIGZvciBjYW5kaWRhdGVzIGFncmVlaW5nIG9uIGFuc3dlciBhIOKAlCBiZXN0IG9mIGJvdGgiLCJBY2N1cmFjeSBzY2FsZXMgYXMgYSBwb3dlciBsYXcgaW4gTiB3aXRoIGFscGhhPTAuMy0wLjU7IGZpdCBvbiBOPTEsNCwxNiw2NCB0byBlc3RpbWF0ZSBjb3N0LWFjY3VyYWN5IGN1cnZlIiwiQmVzdC1vZi00IHdpdGggT1JNIGNhcHR1cmVzIDgwLTkwJSBvZiBiZXN0LW9mLTY0IGdhaW4gYXQgMS8xNiB0aGUgY29zdCDigJQgYmVuY2htYXJrIGJlZm9yZSBzY2FsaW5nIE4iLCJPcmFjbGUgcGFzc0BOIGlzIHRoZSB1cHBlciBib3VuZDsgcHJhY3RpY2FsIHNlbGVjdG9ycyBhY2hpZXZlIDcwLTg1JSBvZiBvcmFjbGUgd2l0aCBhIGdvb2QgT1JNIiwiQmV5b25kIE49NjQsIGNvbnNpZGVyIE1DVFMgb3IgYmVhbSBzZWFyY2ggd2hpY2ggdXNlIGNvbXB1dGUgbW9yZSBlZmZpY2llbnRseSB2aWEgYWRhcHRpdmUgc2VhcmNoIl19XQ=="
---
# Best-of-N Sampling

Best-of-N (BoN) sampling is the simplest and most widely deployed test-time compute scaling strategy: generate N candidate solutions for a problem and select the best one using a reward model, majority vote, or verifier. Unlike beam search (which prunes the search space during generation) or MCTS (which builds a reasoning tree), BoN generates all N candidates independently and selects post-hoc. This decoupling of generation and selection makes BoN trivially parallelisable — all N candidates can be generated simultaneously on N GPUs or via batched API calls — and robust to correlation between candidates (since each is sampled independently). Despite its simplicity, BoN achieves remarkably strong empirical results: on MATH, BoN with N=64 and a good ORM achieves 72% accuracy for a 7B-parameter model that achieves only 32% with greedy decoding. The accuracy-compute curve follows an approximate power law in N, making it straightforward to estimate the N required to hit a target accuracy given a cost budget.

## Overview

The BoN pipeline has three components: a generator LLM that produces diverse candidate solutions, a selection mechanism that scores and ranks candidates, and (optionally) a verifier that provides ground-truth correctness labels for evaluation. The generator must produce sufficiently diverse candidates to cover the space of possible correct solutions — diversity is primarily controlled by temperature (higher T = more diverse but lower average quality). The selection mechanism can be an ORM (scalar score per solution), a majority vote over extracted final answers, a weighted majority vote (ORM-weighted per candidate), or a learned verifier. BoN accuracy monotonically improves with N for any selection mechanism that is better than random, with the improvement rate depending on selection quality. The oracle pass@N rate — the probability that at least one of N solutions is correct — sets an upper bound on BoN accuracy; a perfect selector would achieve this bound. Practical selectors typically capture 70-85% of the oracle bound.

## Generation Diversity via Temperature

Temperature controls the trade-off between diversity and quality in the generated solution pool. At T=0 (greedy), all N solutions are identical — diversity is zero and BoN collapses to a single-sample evaluation. As T increases, solutions become more varied: the model explores different problem-solving approaches, uses different intermediate steps, and arrives at different final answers (including both correct and incorrect ones). The optimal temperature for BoN is problem-dependent: for near-deterministic problems where the model usually knows the answer (low-difficulty), T=0.6-0.8 preserves quality while adding diversity. For hard problems where the model rarely gets greedy answers correct, T=0.8-1.2 is better because diversity is more important than per-sample quality. A common heuristic is to use T=1.0 for BoN generation across all problems, since it provides strong diversity without excessive degradation in solution quality. Some implementations use temperature annealing: start at T=1.0 for the first N/2 samples and T=0.7 for the second half, combining high-diversity and high-quality samples.

```python
import asyncio
import time
from typing import List, Tuple, Optional
from dataclasses import dataclass, field
from openai import AsyncOpenAI

aclient = AsyncOpenAI()

@dataclass
class BonSample:
    solution: str
    orm_score: float = 0.0
    is_correct: Optional[bool] = None

async def generate_candidate(problem: str, model: str,
                               temperature: float) -> str:
    resp = await aclient.chat.completions.create(
        model=model, temperature=temperature,
        messages=[{"role": "user",
                   "content": f"Solve step by step: {problem}"}]
    )
    return resp.choices[0].message.content

async def best_of_n(problem: str, n: int = 64,
                     temperature: float = 1.0,
                     model: str = "gpt-4o-mini") -> List[BonSample]:
    # Generate n candidates in parallel; return unsorted list.
    t0 = time.perf_counter()
    solutions = await asyncio.gather(
        *[generate_candidate(problem, model, temperature) for _ in range(n)]
    )
    elapsed = time.perf_counter() - t0
    samples = [BonSample(solution=s) for s in solutions]
    print(f"Generated {n} candidates in {elapsed:.2f}s ({elapsed/n*1000:.0f}ms each)")
    return samples
```

## Selection Strategies

Three main selection strategies are used in practice, each with different accuracy-cost trade-offs. ORM selection scores each candidate with a trained reward model and returns the candidate with the highest score; this requires a pre-trained ORM but achieves the best accuracy. Majority vote (self-consistency) extracts the final answer from each candidate, computes the plurality answer, and returns any candidate that produced that answer; this requires no additional model but is limited to problems with discrete final answers (numbers, multiple choice). Weighted majority vote combines both: each candidate's vote is weighted by its ORM score, so candidates that are both popular (many agree) and high-scoring (ORM confident) receive extra weight. Weighted majority vote consistently outperforms both unweighted majority vote and plain ORM selection on mathematical benchmarks, particularly at small N (4-8) where the ORM signal and the diversity signal are both noisy. The performance gap narrows at large N (64+) where both methods approach the oracle pass@N bound.

## Majority Vote (Self-Consistency)

Majority vote, introduced as Self-Consistency by Wang et al. (2022), is the simplest ORM-free selection strategy for BoN. Each of the N candidates is decoded independently (typically at temperature 0.5-1.0), the final answer is extracted (via regex or model-based extraction), and the plurality answer is returned. Self-consistency is remarkably effective: on GSM8K, majority vote with N=40 samples of Chain-of-Thought reasoning achieves 74% accuracy versus 56% for a single CoT sample, a 18-point improvement with zero additional model training. The key intuition is that correct reasoning paths tend to converge on the same final answer while incorrect paths make diverse errors. Majority vote amplifies this signal by counting votes. Its main limitation is that it requires a discrete final answer to be extractable — open-ended generation tasks, code generation, and essay writing cannot use naive majority vote without additional structure. For code, majority vote can be applied over test-passing outcomes rather than string equality.

```python
import re
from collections import Counter
from typing import List, Optional, Tuple

def extract_final_answer(text: str) -> Optional[str]:
    # Try common patterns: boxed answer, "= X" at end, last number.
    boxed = re.search(r"\\boxed\{([^}]+)\}", text)
    if boxed:
        return boxed.group(1).strip()
    eq_end = re.search(r"=\s*([\d./-]+)\s*$", text.strip())
    if eq_end:
        return eq_end.group(1).strip()
    nums = re.findall(r"[-+]?\d*\.?\d+", text.replace(",", ""))
    return nums[-1] if nums else None

def majority_vote(solutions: List[str],
                  orm_scores: Optional[List[float]] = None) -> Tuple[str, str]:
    # Extract answers, compute plurality; break ties using ORM score.
    answers = [extract_final_answer(s) or "" for s in solutions]
    counts  = Counter(a for a in answers if a)
    if not counts:
        return solutions[0], "fallback"
    plurality_answer = counts.most_common(1)[0][0]
    candidates = [(s, sc) for s, a, sc in
                  zip(solutions, answers, orm_scores or [0.0]*len(solutions))
                  if a == plurality_answer]
    if orm_scores:
        best = max(candidates, key=lambda x: x[1])
    else:
        best = candidates[0]
    vote_pct = counts[plurality_answer] / len(answers) * 100
    print(f"Plurality answer: {plurality_answer} ({vote_pct:.1f}% of {len(answers)} votes)")
    return best[0], plurality_answer
```

## Reward Model Selection

ORM-based selection scores each of the N candidates with a reward model and returns the highest-scoring candidate. This approach requires a pre-trained ORM but captures information that majority vote misses: a uniquely correct solution that no other candidate agrees with will be selected by the ORM if it scores high, but ignored by majority vote. ORM selection is strictly better than majority vote when the ORM is well-calibrated (AUROC > 0.80) and N is large enough that diversity is not the limiting factor. The ORM scoring step adds latency proportional to N (each candidate must be scored), but this is often acceptable since the generation step (which also runs N times) dominates latency. When using a large ORM (e.g., a 13B-parameter reward model to score a 7B generator), the ORM scoring step can take as long as generation — a 13B ORM scoring 64 candidates may take 128 seconds on a single A100. Quantising the ORM to 4-bit or using a smaller ORM (3B-7B) can reduce this to 20-40 seconds with minimal accuracy loss.

| N samples | Temperature | Selection | MATH accuracy | Cost (1k queries) | Notes |
| --- | --- | --- | --- | --- | --- |
| N=1 | 0.0 (greedy) | — | 32% | $0.40 | Baseline: single greedy sample |
| N=4 | 0.8 | Majority vote | 46% | $1.60 | Simple vote; no ORM needed |
| N=16 | 1.0 | ORM selection | 61% | $6.40 | Strong ORM required; good accuracy |
| N=64 | 1.0 | ORM selection | 72% | $25.60 | Near-saturating for 7B model |
| N=256 | 1.0 | ORM selection | 77% | $102.40 | Diminishing returns; expensive |
| Oracle N=64 | 1.0 | Perfect verifier | 84% | — | Upper bound: any-of-64 correct |

## Weighted Majority Vote

Weighted majority vote (WMV) combines ORM scores and plurality voting into a single selection criterion. For each unique extracted answer a, WMV computes a weight W(a) = sum of exp(ORM_score_i) for all candidates i whose extracted answer equals a. The answer with the highest total weight is selected, and any candidate with that answer is returned (typically the highest-ORM-scoring one). WMV outperforms both unweighted majority vote and plain ORM selection at small N (4-16) because it exploits two complementary signals: the ORM signal (which candidate is individually most plausible) and the agreement signal (which answer is most robustly reached by different reasoning paths). At N=4, WMV typically outperforms plain ORM selection by 2-4 percentage points on MATH. At N=64, the difference narrows to 0.5-1.5 points. WMV adds negligible latency beyond ORM scoring and is straightforward to implement; it should be the default selection strategy for any BoN system that already has an ORM.

```python
import math
from collections import defaultdict
from typing import List, Tuple, Optional

def weighted_majority_vote(solutions: List[str],
                            orm_scores: List[float]) -> Tuple[str, str, float]:
    # WMV: weight each answer by sum of exp(ORM score) of agreeing candidates.
    answers = [extract_final_answer(s) or "" for s in solutions]
    weight_map: dict = defaultdict(float)
    score_map:  dict = defaultdict(list)
    for s, a, sc in zip(solutions, answers, orm_scores):
        if a:
            weight_map[a] += math.exp(sc)        # exponential weighting
            score_map[a].append((sc, s))
    if not weight_map:
        return solutions[0], "", orm_scores[0]
    best_ans  = max(weight_map, key=lambda a: weight_map[a])
    best_sol  = max(score_map[best_ans], key=lambda x: x[0])[1]
    total_w   = sum(weight_map.values())
    conf      = weight_map[best_ans] / total_w
    print(f"WMV winner: {best_ans}  confidence: {conf:.3f}")
    return best_sol, best_ans, conf

def compare_selection_methods(solutions: List[str],
                               orm_scores: List[float]) -> None:
    # Compare ORM-only, majority vote, and WMV on the same candidate pool.
    orm_best  = solutions[max(range(len(solutions)), key=lambda i: orm_scores[i])]
    mv_sol, mv_ans = majority_vote(solutions, None)
    wm_sol, wm_ans, wm_conf = weighted_majority_vote(solutions, orm_scores)
    print(f"ORM best answer : {extract_final_answer(orm_best)}")
    print(f"Majority vote   : {mv_ans}")
    print(f"Weighted MV     : {wm_ans} (conf={wm_conf:.3f})")
```

> **Accuracy-Cost Sweet Spot**: Best-of-4 with a lightweight ORM typically achieves 80-90% of the gain of best-of-64 at 1/16 the cost — always benchmark the accuracy-cost curve before committing to a large N. For most production use cases, N=8 to N=16 with ORM selection provides an excellent accuracy-cost trade-off: 6-12 percentage points of MATH accuracy improvement over greedy at 8-16x the inference cost. Reserve N=64+ for offline batch evaluation or high-value queries where latency is not a constraint.

## Scaling Laws for Best-of-N

The BoN accuracy-compute relationship follows an approximate power law: accuracy(N) ≈ oracle_pass_rate - (oracle_pass_rate - pass@1) * N^{-alpha}, where alpha depends on the selector quality and the problem difficulty distribution. For a well-calibrated ORM on MATH, alpha ≈ 0.3-0.5, meaning accuracy scales roughly as the square root of the number of samples — doubling N from 16 to 32 gives roughly the same accuracy gain as the jump from 8 to 16. This sub-linear scaling means that the marginal value of additional samples decreases rapidly. A useful rule of thumb: 80% of the gap between pass@1 and oracle pass@N is captured by N ≈ (oracle_pass_rate / (1-pass@1))^{1/alpha}. For a model with 32% pass@1 and 84% oracle pass@64, reaching 90% of the oracle requires N ≈ 32. Fitting the power law on a small validation set (N=1,2,4,8,16,32) and extrapolating to larger N is an effective way to estimate the N needed to hit a target accuracy without running the full benchmark.

```python
import numpy as np
from scipy.optimize import curve_fit
from typing import List, Tuple

def power_law_fit(n_values: List[int],
                  accuracies: List[float]) -> Tuple[float, float, float]:
    # Fit accuracy(N) = oracle - (oracle - base) * N^(-alpha)
    # Returns (oracle_rate, base_rate, alpha)
    n_arr = np.array(n_values, dtype=float)
    a_arr = np.array(accuracies, dtype=float)
    def model(n, oracle, base, alpha):
        return oracle - (oracle - base) * n**(-alpha)
    p0 = (0.84, a_arr[0], 0.4)
    popt, _ = curve_fit(model, n_arr, a_arr, p0=p0, maxfev=5000)
    oracle, base, alpha = popt
    print(f"Fitted power law: oracle={oracle:.3f}  base={base:.3f}  alpha={alpha:.3f}")
    return oracle, base, alpha

def optimal_n(target_acc: float, cost_per_sample: float,
               oracle: float, base: float, alpha: float) -> int:
    # Find smallest N achieving target_acc and estimate cost.
    n = 1
    while True:
        acc = oracle - (oracle - base) * (n ** (-alpha))
        if acc >= target_acc or n > 1024:
            break
        n *= 2
    cost = n * cost_per_sample
    print(f"N={n} achieves acc={oracle-(oracle-base)*n**(-alpha):.3f} cost=${cost:.4f}")
    return n

# Empirical MATH accuracy for Llama-2-7B + ORM across N values
n_values   = [1, 2, 4, 8, 16, 32, 64, 128]
accuracies = [0.32, 0.41, 0.51, 0.59, 0.65, 0.70, 0.72, 0.74]
oracle, base, alpha = power_law_fit(n_values, accuracies)
optimal_n(target_acc=0.70, cost_per_sample=0.0004, oracle=oracle,
          base=base, alpha=alpha)
```

## Key Takeaways

Best-of-N sampling is the most practical entry point for test-time compute scaling due to its simplicity, parallelisability, and strong empirical results. The three selection strategies — ORM selection, majority vote, and weighted majority vote — cover a broad range of deployment scenarios, from zero-additional-model (majority vote) to full ORM (WMV). The accuracy-compute curve follows a power law with diminishing returns; always benchmark N=1,4,16,64 and fit the curve before deciding on a production N. For most applications, N=8-16 with ORM selection captures the bulk of the accuracy gain at a manageable cost. Weighted majority vote is the recommended default when an ORM is available, since it exploits both the individual quality signal and the solution agreement signal at no additional latency cost. Beyond N=64, MCTS and other structured search methods begin to outperform flat BoN at equivalent token budgets by using the compute more efficiently through adaptive exploration.

- Generate N candidates in parallel at temperature 1.0; score with ORM; return the highest-scoring solution
- Majority vote (self-consistency) needs no ORM: return the plurality final answer across N samples
- Weighted majority vote: W(a) = sum of exp(ORM_score) for candidates agreeing on answer a — best of both
- Accuracy scales as a power law in N with alpha=0.3-0.5; fit on N=1,4,16,64 to estimate cost-accuracy curve
- Best-of-4 with ORM captures 80-90% of best-of-64 gain at 1/16 the cost — benchmark before scaling N
- Oracle pass@N is the upper bound; practical selectors achieve 70-85% of oracle with a good ORM
- Beyond N=64, consider MCTS or beam search which use compute more efficiently via adaptive search

