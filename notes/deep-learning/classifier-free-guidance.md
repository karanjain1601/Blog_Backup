---
title: "Classifier-Free Guidance — CFG and the Quality-Diversity Trade-off"
slug: "classifier-free-guidance"
description: "Implement classifier-free guidance training with conditioning dropout, build the CFG inference formula, sweep the guidance scale w from 1 to 15, apply CFG to text-to-image with CLIP embeddings, and compare CFG against classifier guidance and PAG."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2xhc3NpZmllci1mcmVlIGd1aWRhbmNlIChIbyBcdTAwMjYgU2FsaW1hbnMgMjAyMikgYWNoaWV2ZXMgY2xhc3MtY29uZGl0aW9uYWwgcXVhbGl0eSBlcXVpdmFsZW50IHRvIGNsYXNzaWZpZXIgZ3VpZGFuY2Ug4oCUIHdpdGhvdXQgYSBzZXBhcmF0ZWx5IHRyYWluZWQgY2xhc3NpZmllci4gVGhlIGtleSBpbnNpZ2h0OiB0cmFpbiBhIHNpbmdsZSBkaWZmdXNpb24gbW9kZWwgdG8gYmUgYm90aCB1bmNvbmRpdGlvbmFsIChjb25kaXRpb24gYyByZXBsYWNlZCBieSBudWxsIHRva2VuIOKIhSkgYW5kIGNvbmRpdGlvbmFsIChjb25kaXRpb24gYyBwcm92aWRlZCksIGJ5IHJhbmRvbWx5IGRyb3BwaW5nIHRoZSBjb25kaXRpb25pbmcgZHVyaW5nIHRyYWluaW5nLiBBdCBpbmZlcmVuY2UsIGNvbWJpbmUgYm90aCBwcmVkaWN0aW9ucyB0byBleHRyYXBvbGF0ZSBpbiB0aGUgZGlyZWN0aW9uIG9mIHRoZSBjb25kaXRpb24sIGFtcGxpZnlpbmcgdGhlIGNsYXNzIHNpZ25hbCB3aXRob3V0IGFueSBjbGFzc2lmaWVyIGdyYWRpZW50IGNvbXB1dGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vdGl2YXRpb24g4oCUIEF2b2lkaW5nIHRoZSBTZXBhcmF0ZSBDbGFzc2lmaWVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFzc2lmaWVyIGd1aWRhbmNlIHJlcXVpcmVzICgxKSBhIHNlcGFyYXRlbHkgdHJhaW5lZCBub2lzeSBjbGFzc2lmaWVyIHBfz4YoeXx4X3QpIHRyYWluZWQgYXQgYWxsIG5vaXNlIGxldmVscywgKDIpIGdyYWRpZW50IGNvbXB1dGF0aW9uIHRocm91Z2ggdGhpcyBjbGFzc2lmaWVyIGF0IGV2ZXJ5IGRlbm9pc2luZyBzdGVwLCBhbmQgKDMpIGNhcmVmdWwgdHVuaW5nIHRvIGF2b2lkIGNsYXNzaWZpZXIgZ3JhZGllbnQgaW5zdGFiaWxpdHkgYXQgaGlnaCBub2lzZSBsZXZlbHMuIFRoZXNlIGNvc3RzIGFkZCB+NTAlIGluZmVyZW5jZSBjb21wdXRlIGFuZCBzaWduaWZpY2FudCB0cmFpbmluZyBjb21wbGV4aXR5LiBDbGFzc2lmaWVyLWZyZWUgZ3VpZGFuY2UgZWxpbWluYXRlcyB0aGUgY2xhc3NpZmllciBlbnRpcmVseTogdGhlIGd1aWRhbmNlIHNpZ25hbCBpcyBkZXJpdmVkIGZyb20gdGhlIGRpZmZlcmVuY2UgYmV0d2VlbiBjb25kaXRpb25hbCBhbmQgdW5jb25kaXRpb25hbCBwcmVkaWN0aW9ucyBvZiB0aGUgc2FtZSBuZXR3b3JrLCB3aGljaCBpcyBhIGNoZWFwIGV4dHJhIGZvcndhcmQgcGFzcyByYXRoZXIgdGhhbiBhbiBleHBlbnNpdmUgZ3JhZGllbnQgY29tcHV0YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ0ZHIFRyYWluaW5nIOKAlCBDb25kaXRpb25hbCBhbmQgVW5jb25kaXRpb25hbCBUb2dldGhlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ0ZHIHRyYWluaW5nIG1vZGlmaWVzIHRoZSBzdGFuZGFyZCBkaWZmdXNpb24gdHJhaW5pbmcgbG9vcCBieSByYW5kb21seSByZXBsYWNpbmcgdGhlIGNvbmRpdGlvbiBjIHdpdGggYSBudWxsIHRva2VuIOKIhSB3aXRoIHByb2JhYmlsaXR5IHBfdW5jb25kICh0eXBpY2FsbHkgMC4x4oCTMC4yKS4gVGhlIG5ldHdvcmsgbGVhcm5zIGJvdGggcCh4X3R8YykgKGNvbmRpdGlvbmFsIGRlbm9pc2luZykgYW5kIHAoeF90fOKIhSkgKHVuY29uZGl0aW9uYWwgZGVub2lzaW5nKSBmcm9tIHRoZSBzYW1lIHdlaWdodHMuIEF0IGluZmVyZW5jZSB0aW1lLCBib3RoIHRoZSBjb25kaXRpb25hbCBwcmVkaWN0aW9uIM61X864KHhfdCx0LGMpIGFuZCB1bmNvbmRpdGlvbmFsIHByZWRpY3Rpb24gzrVfzrgoeF90LHQs4oiFKSBhcmUgY29tcHV0ZWQgaW4gYSBzaW5nbGUgZm9yd2FyZCBwYXNzIChvciB0d28gZm9yd2FyZCBwYXNzZXMgaWYgYmF0Y2hlZCBzZXBhcmF0ZWx5KSwgYW5kIGNvbWJpbmVkIHdpdGggdGhlIGd1aWRhbmNlIGZvcm11bGEuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIENGR0RpZmZ1c2lvbk1vZGVsKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRhdGFfZGltPTMyLCBjb25kX2RpbT0xNiwgaGlkZGVuPTEyOCwgVD0xMDAwKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubnVsbF9jb25kID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKGNvbmRfZGltKSkgICMgbGVhcm5lZCBudWxsIHRva2VuXG4gICAgICAgIHNlbGYudGltZV9lbWJlZCA9IG5uLkVtYmVkZGluZyhULCAxNilcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGRhdGFfZGltICsgY29uZF9kaW0gKyAxNiwgaGlkZGVuKSwgbm4uU2lMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuKSwgbm4uU2lMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgZGF0YV9kaW0pXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4X3QsIHQsIGNvbmQpOlxuICAgICAgICB0X2VtYiA9IHNlbGYudGltZV9lbWJlZCh0KVxuICAgICAgICBoID0gdG9yY2guY2F0KFt4X3QsIGNvbmQsIHRfZW1iXSwgZGltPS0xKVxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoaClcblxuZGVmIGNmZ190cmFpbl9zdGVwKG1vZGVsLCB4MCwgY29uZCwgYWxwaGFfYmFyLCBwX3VuY29uZD0wLjE1KTpcbiAgICBcIlwiXCJDRkcgdHJhaW5pbmc6IHJhbmRvbWx5IGRyb3AgY29uZGl0aW9uaW5nIHdpdGggcHJvYmFiaWxpdHkgcF91bmNvbmQuXCJcIlwiXG4gICAgQiA9IHgwLnNpemUoMClcbiAgICBUID0gbGVuKGFscGhhX2JhcilcbiAgICB0ID0gdG9yY2gucmFuZGludCgwLCBULCAoQiwpKVxuICAgIGVwcyA9IHRvcmNoLnJhbmRuX2xpa2UoeDApXG4gICAgYWIgPSBhbHBoYV9iYXJbdF0udW5zcXVlZXplKDEpXG4gICAgeF90ID0gdG9yY2guc3FydChhYikgKiB4MCArIHRvcmNoLnNxcnQoMSAtIGFiKSAqIGVwc1xuICAgICMgRHJvcCBjb25kaXRpb24gd2l0aCBwcm9iYWJpbGl0eSBwX3VuY29uZFxuICAgIGRyb3BfbWFzayA9IHRvcmNoLnJhbmQoQikgXHUwMDNjIHBfdW5jb25kXG4gICAgY29uZF91c2VkID0gY29uZC5jbG9uZSgpXG4gICAgY29uZF91c2VkW2Ryb3BfbWFza10gPSBtb2RlbC5udWxsX2NvbmQudW5zcXVlZXplKDApLmV4cGFuZChkcm9wX21hc2suc3VtKCksIC0xKVxuICAgIGVwc19wcmVkID0gbW9kZWwoeF90LCB0LCBjb25kX3VzZWQpXG4gICAgcmV0dXJuIEYubXNlX2xvc3MoZXBzX3ByZWQsIGVwcylcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmFscGhhX2JhciA9IHRvcmNoLmN1bXByb2QoMSAtIHRvcmNoLmxpbnNwYWNlKDFlLTQsIDAuMDIsIDEwMDApLCBkaW09MClcbm1vZGVsID0gQ0ZHRGlmZnVzaW9uTW9kZWwoKVxub3B0ID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5kYXRhID0gdG9yY2gucmFuZG4oNDAwLCAzMilcbmNvbmRzID0gdG9yY2gucmFuZG4oNDAwLCAxNilcbmZvciBzdGVwIGluIHJhbmdlKDIwMCk6XG4gICAgaWR4ID0gdG9yY2gucmFuZGludCgwLCA0MDAsICgzMiwpKVxuICAgIGxvc3MgPSBjZmdfdHJhaW5fc3RlcChtb2RlbCwgZGF0YVtpZHhdLCBjb25kc1tpZHhdLCBhbHBoYV9iYXIpXG4gICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbiAgICBpZiBzdGVwICUgMTAwID09IDA6XG4gICAgICAgIHByaW50KGZcdTAwMjdTdGVwIHtzdGVwfTogQ0ZHIHRyYWluaW5nIGxvc3MgPSB7bG9zcy5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDRkcgSW5mZXJlbmNlIEZvcm11bGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF0IGluZmVyZW5jZSwgdGhlIENGRyBlcHNpbG9uIGlzOiDOtcyDID0gzrVfzrgoeF90LHQs4oiFKSArIHfCtyjOtV/OuCh4X3QsdCxjKSDiiJIgzrVfzrgoeF90LHQs4oiFKSksIHdoZXJlIHcgaXMgdGhlIGd1aWRhbmNlIHNjYWxlLiBBdCB3PTAgdGhpcyBpcyB1bmNvbmRpdGlvbmFsOyBhdCB3PTEgaXQgaXMgcHVyZWx5IGNvbmRpdGlvbmFsOyBhdCB3IFx1MDAzZSAxIHRoZSBndWlkYW5jZSBleHRyYXBvbGF0ZXMgYmV5b25kIHRoZSBjb25kaXRpb25hbCBkaXN0cmlidXRpb24gdG93YXJkIGhpZ2gtcHJvYmFiaWxpdHkgbW9kZXMgZm9yIGNsYXNzIGMuIE1lY2hhbmljYWxseSwgQ0ZHIHN0ZWVycyB0aGUgc2NvcmUgaW4gdGhlIGRpcmVjdGlvbiB0aGF0IGluY3JlYXNlcyBwKGN8eF90KSDigJQgaXQgcGVyZm9ybXMgYXBwcm94aW1hdGUgY2xhc3NpZmllciBndWlkYW5jZSBpbXBsaWNpdGx5LCB3aXRob3V0IGEgcmVhbCBjbGFzc2lmaWVyLiBUaGUgZWZmZWN0aXZlIGltcGxpY2l0IGNsYXNzaWZpZXIgZ3JhZGllbnQgaXM6IHPCt+KIhyBsb2cgcChjfHhfdCkg4omIICh34oiSMSnCt1vOtV9jb25kIOKIkiDOtV91bmNvbmRdL+KImigx4oiS4b6xX3QpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuQHRvcmNoLm5vX2dyYWQoKVxuZGVmIGNmZ19zYW1wbGluZyhtb2RlbCwgY29uZCwgYWxwaGFfYmFyLCB0aW1lc3RlcHMsIHc9Ny4wLCBkYXRhX2RpbT0zMiwgQj00KTpcbiAgICBcIlwiXCJDRkcgaW5mZXJlbmNlOiBjb21iaW5lIGNvbmRpdGlvbmFsIGFuZCB1bmNvbmRpdGlvbmFsIHByZWRpY3Rpb25zLlwiXCJcIlxuICAgIG51bGxfY29uZCA9IG1vZGVsLm51bGxfY29uZC51bnNxdWVlemUoMCkuZXhwYW5kKEIsIC0xKVxuICAgIHggPSB0b3JjaC5yYW5kbihCLCBkYXRhX2RpbSlcbiAgICBmb3IgaSBpbiByYW5nZShsZW4odGltZXN0ZXBzKSAtIDEpOlxuICAgICAgICB0ID0gdGltZXN0ZXBzW2ldXG4gICAgICAgIHRfcHJldiA9IHRpbWVzdGVwc1tpICsgMV1cbiAgICAgICAgYWJfdCA9IGFscGhhX2Jhclt0XVxuICAgICAgICBhYl9wID0gYWxwaGFfYmFyW3RfcHJldl1cbiAgICAgICAgdF9iYXRjaCA9IHRvcmNoLmZ1bGwoKEIsKSwgdCwgZHR5cGU9dG9yY2gubG9uZylcbiAgICAgICAgIyBUd28gZm9yd2FyZCBwYXNzZXMgKG9yIG9uZSB3aXRoIGRvdWJsZWQgYmF0Y2gpXG4gICAgICAgIGVwc19jb25kICAgPSBtb2RlbCh4LCB0X2JhdGNoLCBjb25kLmV4cGFuZChCLCAtMSkpXG4gICAgICAgIGVwc191bmNvbmQgPSBtb2RlbCh4LCB0X2JhdGNoLCBudWxsX2NvbmQpXG4gICAgICAgICMgQ0ZHIGNvbWJpbmF0aW9uXG4gICAgICAgIGVwc19jZmcgPSBlcHNfdW5jb25kICsgdyAqIChlcHNfY29uZCAtIGVwc191bmNvbmQpXG4gICAgICAgICMgRERJTS1zdHlsZSB1cGRhdGVcbiAgICAgICAgeDAgPSAoeCAtIHRvcmNoLnNxcnQoMSAtIGFiX3QpICogZXBzX2NmZykgLyB0b3JjaC5zcXJ0KGFiX3QpXG4gICAgICAgIHgwID0geDAuY2xhbXAoLTEsIDEpXG4gICAgICAgIHggPSB0b3JjaC5zcXJ0KGFiX3ApICogeDAgKyB0b3JjaC5zcXJ0KDEgLSBhYl9wKSAqIGVwc19jZmdcbiAgICByZXR1cm4geFxuXG5hbHBoYV9iYXIgPSB0b3JjaC5jdW1wcm9kKDEgLSB0b3JjaC5saW5zcGFjZSgxZS00LCAwLjAyLCAxMDAwKSwgZGltPTApXG50aW1lc3RlcHMgPSBsaXN0KHJhbmdlKDAsIDEwMDAsIDIwKSlbOjotMV1cbmNvbmQgPSB0b3JjaC5yYW5kbigxLCAxNilcbmZvciB3IGluIFsxLjAsIDMuMCwgNy41XTpcbiAgICBvdXQgPSBjZmdfc2FtcGxpbmcobW9kZWwsIGNvbmQsIGFscGhhX2JhciwgdGltZXN0ZXBzLCB3PXcpXG4gICAgcHJpbnQoZlx1MDAyN3c9e3c6NC4xZn06IG91dHB1dCBub3JtPXtvdXQubm9ybSgpOi4zZn0sIHN0ZD17b3V0LnN0ZCgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3VpZGFuY2UgU2NhbGUgYW5kIHRoZSBRdWFsaXR5LURpdmVyc2l0eSBUcmFkZS1vZmYifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBndWlkYW5jZSBzY2FsZSB3IGRyaXZlcyBhIHByZWNpc2lvbi1yZWNhbGwgdHJhZGUtb2ZmLiBMb3cgdyAoMOKAkzIpOiBoaWdoIGRpdmVyc2l0eSwgbG93ZXIgY2xhc3MgZmlkZWxpdHkuIE9wdGltYWwgdyAoN+KAkzEwIGZvciB0ZXh0LXRvLWltYWdlLCB+M+KAkzUgZm9yIGNsYXNzLWNvbmRpdGlvbmFsIEltYWdlTmV0KTogYmVzdCBGSUQuIEhpZ2ggdyAoXHUwMDNlMTIpOiBtb2RlIGNvbGxhcHNlLCBvdmVyLXNhdHVyYXRlZCBjb2xvcnMsIHVubmF0dXJhbCBzaGFycG5lc3MuIFRoZSBtZWNoYW5pc20gaXMgbW9kZS1zZWVraW5nOiBDRkcgZXh0cmFwb2xhdGVzIGluIHRoZSBkaXJlY3Rpb24gdGhhdCBtYXhpbWl6ZXMgcChjfHgpLCBwdXNoaW5nIHNhbXBsZXMgdG93YXJkIGhpZ2gtZGVuc2l0eSBjbGFzcyBtb2RlcyBhdCB0aGUgY29zdCBvZiBtYXJnaW5hbCBkaXZlcnNpdHkuIFNEWEwgbW9kZWxzIHVzZSBhIGRlZmF1bHQgdz03LjU7IFN0YWJsZSBEaWZmdXNpb24gWEwgdXNlcyB3PTUuMCB3aXRoIHJlc2NhbGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGd1aWRhbmNlX3NjYWxlX3N3ZWVwKG1vZGVsLCBjb25kLCBhbHBoYV9iYXIsIHRpbWVzdGVwcywgZGF0YV9kaW09MzIsIEI9MTYpOlxuICAgIFwiXCJcIlN3ZWVwIGd1aWRhbmNlIHNjYWxlIGFuZCBtZWFzdXJlIHByb3h5IGRpdmVyc2l0eSAoc3RkKSBhbmQgc2hhcnBuZXNzLlwiXCJcIlxuICAgIG51bGxfY29uZCA9IG1vZGVsLm51bGxfY29uZC51bnNxdWVlemUoMCkuZXhwYW5kKEIsIC0xKVxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciB3IGluIFswLjAsIDEuMCwgMy4wLCA1LjAsIDcuNSwgMTAuMCwgMTUuMF06XG4gICAgICAgIHRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuICAgICAgICB4ID0gdG9yY2gucmFuZG4oQiwgZGF0YV9kaW0pXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKHRpbWVzdGVwcykgLSAxKTpcbiAgICAgICAgICAgICAgICB0LCB0X3AgPSB0aW1lc3RlcHNbaV0sIHRpbWVzdGVwc1tpKzFdXG4gICAgICAgICAgICAgICAgYWJfdCwgYWJfcCA9IGFscGhhX2Jhclt0XSwgYWxwaGFfYmFyW3RfcF1cbiAgICAgICAgICAgICAgICB0X2IgPSB0b3JjaC5mdWxsKChCLCksIHQsIGR0eXBlPXRvcmNoLmxvbmcpXG4gICAgICAgICAgICAgICAgZXBzX2MgPSBtb2RlbCh4LCB0X2IsIGNvbmQuZXhwYW5kKEIsIC0xKSlcbiAgICAgICAgICAgICAgICBlcHNfdSA9IG1vZGVsKHgsIHRfYiwgbnVsbF9jb25kKVxuICAgICAgICAgICAgICAgIGVwcyA9IGVwc191ICsgdyAqIChlcHNfYyAtIGVwc191KVxuICAgICAgICAgICAgICAgIHgwID0gKHggLSB0b3JjaC5zcXJ0KDEgLSBhYl90KSplcHMpIC8gdG9yY2guc3FydChhYl90KVxuICAgICAgICAgICAgICAgIHggPSB0b3JjaC5zcXJ0KGFiX3ApKngwLmNsYW1wKC0xLDEpICsgdG9yY2guc3FydCgxLWFiX3ApKmVwc1xuICAgICAgICBkaXZlcnNpdHkgPSB4LnN0ZChkaW09MCkubWVhbigpLml0ZW0oKSAgICMgYWNyb3NzIHNhbXBsZXNcbiAgICAgICAgc2hhcnBuZXNzID0geC5hYnMoKS5tZWFuKCkuaXRlbSgpICAgICAgICAgIyBwcm94eSBmb3Igc2lnbmFsIHN0cmVuZ3RoXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKCh3LCBkaXZlcnNpdHksIHNoYXJwbmVzcykpXG4gICAgICAgIHByaW50KGZcdTAwMjd3PXt3OjUuMWZ9OiBkaXZlcnNpdHkoc3RkKT17ZGl2ZXJzaXR5Oi40Zn0gIHNoYXJwbmVzcz17c2hhcnBuZXNzOi40Zn1cdTAwMjcpXG4gICAgcmV0dXJuIHJlc3VsdHNcblxuY29uZCA9IHRvcmNoLnJhbmRuKDEsIDE2KVxudGltZXN0ZXBzID0gbGlzdChyYW5nZSgwLCAxMDAwLCA1MCkpWzo6LTFdXG5ndWlkYW5jZV9zY2FsZV9zd2VlcChtb2RlbCwgY29uZCwgYWxwaGFfYmFyLCB0aW1lc3RlcHMpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGV4dC10by1JbWFnZSB3aXRoIENMSVAgRW1iZWRkaW5ncyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gdGV4dC10by1pbWFnZSBtb2RlbHMsIHRoZSBjb25kaXRpb24gYyBpcyBhIENMSVAgdGV4dCBlbWJlZGRpbmcgKGUuZy4gNzY4LWRpbSBmb3IgQ0xJUCBWaVQtTC8xNCkuIFRoZSBkaWZmdXNpb24gbW9kZWwgcmVjZWl2ZXMgdGhlIHRleHQgZW1iZWRkaW5nIHZpYSBjcm9zcy1hdHRlbnRpb24gaW4gdGhlIFUtTmV0LCBub3QgY29uY2F0ZW5hdGlvbi4gQ0ZHIGlzIGFwcGxpZWQgaWRlbnRpY2FsbHk6IM61zIMgPSDOtV/OuCh4X3QsdCziiIUpICsgd8K3KM61X864KHhfdCx0LENMSVAodGV4dCkpIOKIkiDOtV/OuCh4X3QsdCziiIUpKSwgd2hlcmUg4oiFIGlzIHRoZSBDTElQIGVtYmVkZGluZyBvZiB0aGUgZW1wdHkgc3RyaW5nLiBHdWlkYW5jZSBzY2FsZSB3PTfigJM5IGlzIHR5cGljYWwgZm9yIFN0YWJsZSBEaWZmdXNpb24uIENMSVAgZW1iZWRkaW5ncyBhcmUgbm9ybWFsaXplZCB0byB1bml0IG5vcm0gYmVmb3JlIGluamVjdGlvbiwgYW5kIHRoZSBjcm9zcy1hdHRlbnRpb24ga2V5cy92YWx1ZXMgYXJlIGRlcml2ZWQgZnJvbSB0aGUgQ0xJUCBmZWF0dXJlcyB2aWEgbGVhcm5lZCBsaW5lYXIgcHJvamVjdGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIENyb3NzQXR0ZW50aW9uQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTaW5nbGUgY3Jvc3MtYXR0ZW50aW9uIGxheWVyOiBxdWVyaWVzIGZyb20gaW1hZ2UsIGtleXMvdmFsdWVzIGZyb20gdGV4dC5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW1nX2RpbT02NCwgdGV4dF9kaW09MzIsIG5faGVhZHM9NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5faGVhZHMgPSBuX2hlYWRzXG4gICAgICAgIHNlbGYuaGVhZF9kaW0gPSBpbWdfZGltIC8vIG5faGVhZHNcbiAgICAgICAgc2VsZi50b19xID0gbm4uTGluZWFyKGltZ19kaW0sIGltZ19kaW0sIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYudG9fayA9IG5uLkxpbmVhcih0ZXh0X2RpbSwgaW1nX2RpbSwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi50b192ID0gbm4uTGluZWFyKHRleHRfZGltLCBpbWdfZGltLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnRvX291dCA9IG5uLkxpbmVhcihpbWdfZGltLCBpbWdfZGltKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgdGV4dF9lbWIpOlxuICAgICAgICBCLCBTLCBEID0geC5zaGFwZVxuICAgICAgICBUID0gdGV4dF9lbWIuc2hhcGVbMV1cbiAgICAgICAgUSA9IHNlbGYudG9fcSh4KS52aWV3KEIsIFMsIHNlbGYubl9oZWFkcywgc2VsZi5oZWFkX2RpbSkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIEsgPSBzZWxmLnRvX2sodGV4dF9lbWIpLnZpZXcoQiwgVCwgc2VsZi5uX2hlYWRzLCBzZWxmLmhlYWRfZGltKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgViA9IHNlbGYudG9fdih0ZXh0X2VtYikudmlldyhCLCBULCBzZWxmLm5faGVhZHMsIHNlbGYuaGVhZF9kaW0pLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICBzY2FsZSA9IHNlbGYuaGVhZF9kaW0gKiogLTAuNVxuICAgICAgICBhdHRuID0gKFEgQCBLLnRyYW5zcG9zZSgtMiwgLTEpKSAqIHNjYWxlXG4gICAgICAgIGF0dG4gPSBGLnNvZnRtYXgoYXR0biwgZGltPS0xKSAgIyAoQiwgbl9oZWFkcywgUywgVClcbiAgICAgICAgb3V0ID0gKGF0dG4gQCBWKS50cmFuc3Bvc2UoMSwgMikucmVzaGFwZShCLCBTLCBEKVxuICAgICAgICByZXR1cm4gc2VsZi50b19vdXQob3V0KVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuQiwgUyA9IDIsIDE2ICAjIGJhdGNoLCBzcGF0aWFsIHRva2Vuc1xuaW1nX2ZlYXQgPSB0b3JjaC5yYW5kbihCLCBTLCA2NCkgICMgaW1hZ2UgbGF0ZW50IHRva2Vuc1xubnVsbF90ZXh0ID0gdG9yY2guemVyb3MoQiwgOCwgMzIpICAjIG51bGwgdGV4dCAoZW1wdHkgcHJvbXB0KVxudGV4dF9lbWIgPSB0b3JjaC5yYW5kbihCLCA4LCAzMikgICMgQ0xJUCB0ZXh0IGVtYmVkZGluZ1xuYXR0biA9IENyb3NzQXR0ZW50aW9uQmxvY2soaW1nX2RpbT02NCwgdGV4dF9kaW09MzIpXG5vdXRfY29uZCA9IGF0dG4oaW1nX2ZlYXQsIHRleHRfZW1iKVxub3V0X3VuY29uZCA9IGF0dG4oaW1nX2ZlYXQsIG51bGxfdGV4dClcbmVwc19jZmcgPSBvdXRfdW5jb25kICsgNy41ICogKG91dF9jb25kIC0gb3V0X3VuY29uZClcbnByaW50KGZcdTAwMjdDb25kaXRpb25hbCBvdXRwdXQgbm9ybTogICB7b3V0X2NvbmQubm9ybSgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3VW5jb25kaXRpb25hbCBvdXRwdXQgbm9ybToge291dF91bmNvbmQubm9ybSgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3Q0ZHIG91dHB1dCBub3JtICh3PTcuNSk6ICAge2Vwc19jZmcubm9ybSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUEFHIGFuZCBHdWlkYW5jZSBWYXJpYW50cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGVydHVyYmVkIEF0dGVudGlvbiBHdWlkYW5jZSAoUEFHLCAyMDI0KSByZXBsYWNlcyB0aGUgbnVsbCBjb25kaXRpb24g4oiFIHdpdGggaWRlbnRpdHkgc2VsZi1hdHRlbnRpb24gbWFwcyDigJQgaW5zdGVhZCBvZiBkcm9wcGluZyB0aGUgY29uZGl0aW9uLCBpdCBkZWdyYWRlcyBhdHRlbnRpb24gcHJvY2Vzc2luZy4gVGhpcyBwcm9kdWNlcyBhIGRpZmZlcmVudCBraW5kIG9mIHN0cnVjdHVyYWwgZ3VpZGFuY2UgdGhhdCBpbXByb3ZlcyBmaW5lLWdyYWluZWQgZGV0YWlsIHdpdGhvdXQgb3Zlci1zYXR1cmF0aW5nIGNvbG9ycy4gU0RYTCBndWlkYW5jZSByZXNjYWxpbmcgKEJhc2lsZSBldCBhbC4gMjAyMykgYWRkcmVzc2VzIHRoZSBjb2xvciBhcnRpZmFjdCBwcm9ibGVtIGF0IHcgXHUwMDNlIDc6IHRoZSBDRkcgb3V0cHV0IGhhcyBhIGxhcmdlciBzdGFuZGFyZCBkZXZpYXRpb24gdGhhbiB0aGUgY29uZGl0aW9uYWwgb3V0cHV0LCBzbyByZXNjYWxpbmcgzrVfY2ZnIGJ5IHN0ZCjOtV9jb25kKS9zdGQozrVfY2ZnKSBiZWZvcmUgdGhlIGRlbm9pc2luZyBzdGVwIHByZXZlbnRzIG92ZXItc2F0dXJhdGlvbi4gTmVnYXRpdmUgcHJvbXB0cyBhcmUgYW5vdGhlciBwcmFjdGljYWwgQ0ZHIGV4dGVuc2lvbjogcmVwbGFjZSDiiIUgd2l0aCBDTElQKG5lZ2F0aXZlX3Byb21wdCkgdG8gYWN0aXZlbHkgc3RlZXIgYXdheSBmcm9tIHVuZGVzaXJhYmxlIGF0dHJpYnV0ZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiBvZiBHdWlkYW5jZSBNZXRob2RzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkNsYXNzaWZpZXIgbmVlZGVkIiwiR3VpZGFuY2UgZm9ybXVsYSIsIk9wdGltYWwgdyIsIkFydGlmYWN0cyBhdCBoaWdoIHciLCJJbnZlcnNpb24gc3VwcG9ydCJdLCJyb3dzIjpbWyJObyBndWlkYW5jZSAodz0xKSIsIk5vIiwizrVfzrgoeF90LCB0LCBjKSIsIk4vQSIsIk5vbmUiLCJZZXMgKERESU0pIl0sWyJDbGFzc2lmaWVyIGd1aWRhbmNlIiwiWWVzIOKAlCBub2lzeSBwX8+GKHl8eF90KSIsIs61X864IOKIkiBzwrfiiJooMeKIkuG+sSnCt+KIhyBsb2cgcF/Phih5fHhfdCkiLCJzPTPigJM1IChJbWFnZU5ldCkiLCJOb2lzeSBhdCBoaWdoIHMiLCJObyDigJQgc3RvY2hhc3RpYyJdLFsiQ0ZHIChIbyBcdTAwMjYgU2FsaW1hbnMgMjAyMikiLCJObyDigJQgam9pbnQgdHJhaW5pbmciLCLOtV91bmNvbmQgKyB3wrcozrVfY29uZOKIks61X3VuY29uZCkiLCJ3PTfigJMxMCAodGV4dC10by1pbWFnZSkiLCJDb2xvciBzYXR1cmF0aW9uLCBzaGFycG5lc3MiLCJZZXMg4oCUIHdpdGggbnVsbCBjb25kIl0sWyJQQUcgKDIwMjQpIiwiTm8iLCLOtV9pZGVudGl0eV9hdHRuICsgd8K3KM61X2NvbmTiiJLOtV9pZGVudGl0eV9hdHRuKSIsInc9M+KAkzUiLCJGZXdlciBhcnRpZmFjdHMgdGhhbiBDRkciLCJZZXMiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJHdWlkYW5jZSBTY2FsZSBUdW5pbmcgUnVsZSBvZiBUaHVtYiIsImNvbnRlbnQiOiJTdGFydCB3aXRoIHc9Ny41IGZvciB0ZXh0LXRvLWltYWdlIHRhc2tzLiBJZiBzYW1wbGVzIGFyZSBvdmVyLXNhdHVyYXRlZCBvciBoYXZlIHVubmF0dXJhbCBlZGdlcywgcmVkdWNlIHRvIHc9NS4wIGFuZCB0cnkgZ3VpZGFuY2UgcmVzY2FsaW5nLiBJZiBzZW1hbnRpYyBhbGlnbm1lbnQgdG8gdGhlIHByb21wdCBpcyBwb29yLCBpbmNyZWFzZSB0byB3PTEw4oCTMTIuIEZvciBjbGFzcy1jb25kaXRpb25hbCBJbWFnZU5ldCBtb2RlbHMsIG9wdGltYWwgRklEIGlzIHVzdWFsbHkgYXQgdz0z4oCTNS4gQWx3YXlzIHZhbGlkYXRlIG9uIGEgaGVsZC1vdXQgcHJvbXB0IHNldCDigJQgdGhlIG9wdGltYWwgdyB2YXJpZXMgYWNyb3NzIG1vZGVsIGZhbWlsaWVzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQ0ZHIHRyYWlucyBvbmUgbmV0d29yayBmb3IgYm90aCBjb25kaXRpb25hbCBhbmQgdW5jb25kaXRpb25hbCBnZW5lcmF0aW9uIHZpYSBjb25kaXRpb24gZHJvcG91dCAocD0wLjHigJMwLjIpLiIsIkluZmVyZW5jZSBmb3JtdWxhOiDOtV9jZmcgPSDOtV91bmNvbmQgKyB3wrcozrVfY29uZCDiiJIgzrVfdW5jb25kKSDigJQganVzdCB0d28gZm9yd2FyZCBwYXNzZXMuIiwidz0wOiB1bmNvbmRpdGlvbmFsOyB3PTE6IGNvbmRpdGlvbmFsOyB3XHUwMDNlMTogZXh0cmFwb2xhdGVkIHRvd2FyZCBoaWdoLWNsYXNzLXByb2JhYmlsaXR5IG1vZGVzLiIsIk9wdGltYWwgdyBmb3IgdGV4dC10by1pbWFnZSBpcyA34oCTMTA7IGZvciBjbGFzcy1jb25kaXRpb25hbCBJbWFnZU5ldCwgM+KAkzUuIiwiTmVnYXRpdmUgcHJvbXB0cyByZXBsYWNlIOKIhSB3aXRoIENMSVAobmVnYXRpdmUgdGV4dCksIGFjdGl2ZWx5IHN0ZWVyaW5nIGF3YXkgZnJvbSB1bmRlc2lyZWQgYXR0cmlidXRlcy4iLCJHdWlkYW5jZSByZXNjYWxpbmcgKHN0ZCBub3JtYWxpemF0aW9uKSBmaXhlcyB0aGUgY29sb3Igc2F0dXJhdGlvbiBhcnRpZmFjdHMgc2VlbiBhdCBoaWdoIGd1aWRhbmNlIHNjYWxlcy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Classifier-Free Guidance — CFG and the Quality-Diversity Trade-off

Classifier-free guidance (Ho & Salimans 2022) achieves class-conditional quality equivalent to classifier guidance — without a separately trained classifier. The key insight: train a single diffusion model to be both unconditional (condition c replaced by null token ∅) and conditional (condition c provided), by randomly dropping the conditioning during training. At inference, combine both predictions to extrapolate in the direction of the condition, amplifying the class signal without any classifier gradient computation.

## Motivation — Avoiding the Separate Classifier

Classifier guidance requires (1) a separately trained noisy classifier p_φ(y|x_t) trained at all noise levels, (2) gradient computation through this classifier at every denoising step, and (3) careful tuning to avoid classifier gradient instability at high noise levels. These costs add ~50% inference compute and significant training complexity. Classifier-free guidance eliminates the classifier entirely: the guidance signal is derived from the difference between conditional and unconditional predictions of the same network, which is a cheap extra forward pass rather than an expensive gradient computation.

## CFG Training — Conditional and Unconditional Together

CFG training modifies the standard diffusion training loop by randomly replacing the condition c with a null token ∅ with probability p_uncond (typically 0.1–0.2). The network learns both p(x_t|c) (conditional denoising) and p(x_t|∅) (unconditional denoising) from the same weights. At inference time, both the conditional prediction ε_θ(x_t,t,c) and unconditional prediction ε_θ(x_t,t,∅) are computed in a single forward pass (or two forward passes if batched separately), and combined with the guidance formula.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CFGDiffusionModel(nn.Module):
    def __init__(self, data_dim=32, cond_dim=16, hidden=128, T=1000):
        super().__init__()
        self.null_cond = nn.Parameter(torch.zeros(cond_dim))  # learned null token
        self.time_embed = nn.Embedding(T, 16)
        self.net = nn.Sequential(
            nn.Linear(data_dim + cond_dim + 16, hidden), nn.SiLU(),
            nn.Linear(hidden, hidden), nn.SiLU(),
            nn.Linear(hidden, data_dim)
        )
    def forward(self, x_t, t, cond):
        t_emb = self.time_embed(t)
        h = torch.cat([x_t, cond, t_emb], dim=-1)
        return self.net(h)

def cfg_train_step(model, x0, cond, alpha_bar, p_uncond=0.15):
    """CFG training: randomly drop conditioning with probability p_uncond."""
    B = x0.size(0)
    T = len(alpha_bar)
    t = torch.randint(0, T, (B,))
    eps = torch.randn_like(x0)
    ab = alpha_bar[t].unsqueeze(1)
    x_t = torch.sqrt(ab) * x0 + torch.sqrt(1 - ab) * eps
    # Drop condition with probability p_uncond
    drop_mask = torch.rand(B) < p_uncond
    cond_used = cond.clone()
    cond_used[drop_mask] = model.null_cond.unsqueeze(0).expand(drop_mask.sum(), -1)
    eps_pred = model(x_t, t, cond_used)
    return F.mse_loss(eps_pred, eps)

torch.manual_seed(0)
alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
model = CFGDiffusionModel()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
data = torch.randn(400, 32)
conds = torch.randn(400, 16)
for step in range(200):
    idx = torch.randint(0, 400, (32,))
    loss = cfg_train_step(model, data[idx], conds[idx], alpha_bar)
    opt.zero_grad(); loss.backward(); opt.step()
    if step % 100 == 0:
        print(f'Step {step}: CFG training loss = {loss.item():.4f}')
```

## CFG Inference Formula

At inference, the CFG epsilon is: ε̃ = ε_θ(x_t,t,∅) + w·(ε_θ(x_t,t,c) − ε_θ(x_t,t,∅)), where w is the guidance scale. At w=0 this is unconditional; at w=1 it is purely conditional; at w > 1 the guidance extrapolates beyond the conditional distribution toward high-probability modes for class c. Mechanically, CFG steers the score in the direction that increases p(c|x_t) — it performs approximate classifier guidance implicitly, without a real classifier. The effective implicit classifier gradient is: s·∇ log p(c|x_t) ≈ (w−1)·[ε_cond − ε_uncond]/√(1−ᾱ_t).

```python
import torch

@torch.no_grad()
def cfg_sampling(model, cond, alpha_bar, timesteps, w=7.0, data_dim=32, B=4):
    """CFG inference: combine conditional and unconditional predictions."""
    null_cond = model.null_cond.unsqueeze(0).expand(B, -1)
    x = torch.randn(B, data_dim)
    for i in range(len(timesteps) - 1):
        t = timesteps[i]
        t_prev = timesteps[i + 1]
        ab_t = alpha_bar[t]
        ab_p = alpha_bar[t_prev]
        t_batch = torch.full((B,), t, dtype=torch.long)
        # Two forward passes (or one with doubled batch)
        eps_cond   = model(x, t_batch, cond.expand(B, -1))
        eps_uncond = model(x, t_batch, null_cond)
        # CFG combination
        eps_cfg = eps_uncond + w * (eps_cond - eps_uncond)
        # DDIM-style update
        x0 = (x - torch.sqrt(1 - ab_t) * eps_cfg) / torch.sqrt(ab_t)
        x0 = x0.clamp(-1, 1)
        x = torch.sqrt(ab_p) * x0 + torch.sqrt(1 - ab_p) * eps_cfg
    return x

alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
timesteps = list(range(0, 1000, 20))[::-1]
cond = torch.randn(1, 16)
for w in [1.0, 3.0, 7.5]:
    out = cfg_sampling(model, cond, alpha_bar, timesteps, w=w)
    print(f'w={w:4.1f}: output norm={out.norm():.3f}, std={out.std():.4f}')
```

## Guidance Scale and the Quality-Diversity Trade-off

The guidance scale w drives a precision-recall trade-off. Low w (0–2): high diversity, lower class fidelity. Optimal w (7–10 for text-to-image, ~3–5 for class-conditional ImageNet): best FID. High w (>12): mode collapse, over-saturated colors, unnatural sharpness. The mechanism is mode-seeking: CFG extrapolates in the direction that maximizes p(c|x), pushing samples toward high-density class modes at the cost of marginal diversity. SDXL models use a default w=7.5; Stable Diffusion XL uses w=5.0 with rescaling.

```python
import torch
import numpy as np

def guidance_scale_sweep(model, cond, alpha_bar, timesteps, data_dim=32, B=16):
    """Sweep guidance scale and measure proxy diversity (std) and sharpness."""
    null_cond = model.null_cond.unsqueeze(0).expand(B, -1)
    results = []
    for w in [0.0, 1.0, 3.0, 5.0, 7.5, 10.0, 15.0]:
        torch.manual_seed(42)
        x = torch.randn(B, data_dim)
        with torch.no_grad():
            for i in range(len(timesteps) - 1):
                t, t_p = timesteps[i], timesteps[i+1]
                ab_t, ab_p = alpha_bar[t], alpha_bar[t_p]
                t_b = torch.full((B,), t, dtype=torch.long)
                eps_c = model(x, t_b, cond.expand(B, -1))
                eps_u = model(x, t_b, null_cond)
                eps = eps_u + w * (eps_c - eps_u)
                x0 = (x - torch.sqrt(1 - ab_t)*eps) / torch.sqrt(ab_t)
                x = torch.sqrt(ab_p)*x0.clamp(-1,1) + torch.sqrt(1-ab_p)*eps
        diversity = x.std(dim=0).mean().item()   # across samples
        sharpness = x.abs().mean().item()         # proxy for signal strength
        results.append((w, diversity, sharpness))
        print(f'w={w:5.1f}: diversity(std)={diversity:.4f}  sharpness={sharpness:.4f}')
    return results

cond = torch.randn(1, 16)
timesteps = list(range(0, 1000, 50))[::-1]
guidance_scale_sweep(model, cond, alpha_bar, timesteps)
```

## Text-to-Image with CLIP Embeddings

In text-to-image models, the condition c is a CLIP text embedding (e.g. 768-dim for CLIP ViT-L/14). The diffusion model receives the text embedding via cross-attention in the U-Net, not concatenation. CFG is applied identically: ε̃ = ε_θ(x_t,t,∅) + w·(ε_θ(x_t,t,CLIP(text)) − ε_θ(x_t,t,∅)), where ∅ is the CLIP embedding of the empty string. Guidance scale w=7–9 is typical for Stable Diffusion. CLIP embeddings are normalized to unit norm before injection, and the cross-attention keys/values are derived from the CLIP features via learned linear projections.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CrossAttentionBlock(nn.Module):
    """Single cross-attention layer: queries from image, keys/values from text."""
    def __init__(self, img_dim=64, text_dim=32, n_heads=4):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = img_dim // n_heads
        self.to_q = nn.Linear(img_dim, img_dim, bias=False)
        self.to_k = nn.Linear(text_dim, img_dim, bias=False)
        self.to_v = nn.Linear(text_dim, img_dim, bias=False)
        self.to_out = nn.Linear(img_dim, img_dim)

    def forward(self, x, text_emb):
        B, S, D = x.shape
        T = text_emb.shape[1]
        Q = self.to_q(x).view(B, S, self.n_heads, self.head_dim).transpose(1, 2)
        K = self.to_k(text_emb).view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        V = self.to_v(text_emb).view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        scale = self.head_dim ** -0.5
        attn = (Q @ K.transpose(-2, -1)) * scale
        attn = F.softmax(attn, dim=-1)  # (B, n_heads, S, T)
        out = (attn @ V).transpose(1, 2).reshape(B, S, D)
        return self.to_out(out)

torch.manual_seed(0)
B, S = 2, 16  # batch, spatial tokens
img_feat = torch.randn(B, S, 64)  # image latent tokens
null_text = torch.zeros(B, 8, 32)  # null text (empty prompt)
text_emb = torch.randn(B, 8, 32)  # CLIP text embedding
attn = CrossAttentionBlock(img_dim=64, text_dim=32)
out_cond = attn(img_feat, text_emb)
out_uncond = attn(img_feat, null_text)
eps_cfg = out_uncond + 7.5 * (out_cond - out_uncond)
print(f'Conditional output norm:   {out_cond.norm():.4f}')
print(f'Unconditional output norm: {out_uncond.norm():.4f}')
print(f'CFG output norm (w=7.5):   {eps_cfg.norm():.4f}')
```

## PAG and Guidance Variants

Perturbed Attention Guidance (PAG, 2024) replaces the null condition ∅ with identity self-attention maps — instead of dropping the condition, it degrades attention processing. This produces a different kind of structural guidance that improves fine-grained detail without over-saturating colors. SDXL guidance rescaling (Basile et al. 2023) addresses the color artifact problem at w > 7: the CFG output has a larger standard deviation than the conditional output, so rescaling ε_cfg by std(ε_cond)/std(ε_cfg) before the denoising step prevents over-saturation. Negative prompts are another practical CFG extension: replace ∅ with CLIP(negative_prompt) to actively steer away from undesirable attributes.

## Comparison of Guidance Methods

| Method | Classifier needed | Guidance formula | Optimal w | Artifacts at high w | Inversion support |
| --- | --- | --- | --- | --- | --- |
| No guidance (w=1) | No | ε_θ(x_t, t, c) | N/A | None | Yes (DDIM) |
| Classifier guidance | Yes — noisy p_φ(y|x_t) | ε_θ − s·√(1−ᾱ)·∇ log p_φ(y|x_t) | s=3–5 (ImageNet) | Noisy at high s | No — stochastic |
| CFG (Ho & Salimans 2022) | No — joint training | ε_uncond + w·(ε_cond−ε_uncond) | w=7–10 (text-to-image) | Color saturation, sharpness | Yes — with null cond |
| PAG (2024) | No | ε_identity_attn + w·(ε_cond−ε_identity_attn) | w=3–5 | Fewer artifacts than CFG | Yes |

> **Guidance Scale Tuning Rule of Thumb**: Start with w=7.5 for text-to-image tasks. If samples are over-saturated or have unnatural edges, reduce to w=5.0 and try guidance rescaling. If semantic alignment to the prompt is poor, increase to w=10–12. For class-conditional ImageNet models, optimal FID is usually at w=3–5. Always validate on a held-out prompt set — the optimal w varies across model families.

- CFG trains one network for both conditional and unconditional generation via condition dropout (p=0.1–0.2).
- Inference formula: ε_cfg = ε_uncond + w·(ε_cond − ε_uncond) — just two forward passes.
- w=0: unconditional; w=1: conditional; w>1: extrapolated toward high-class-probability modes.
- Optimal w for text-to-image is 7–10; for class-conditional ImageNet, 3–5.
- Negative prompts replace ∅ with CLIP(negative text), actively steering away from undesired attributes.
- Guidance rescaling (std normalization) fixes the color saturation artifacts seen at high guidance scales.

---

