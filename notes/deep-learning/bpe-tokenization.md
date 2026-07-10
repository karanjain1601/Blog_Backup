---
title: "BPE — Byte-Pair Encoding and LLM Vocabulary Construction"
slug: "bpe-tokenization"
description: "How BPE builds LLM vocabularies by iteratively merging frequent character pairs, covering the merge algorithm, pre-tokenization, fertility analysis, and HuggingFace integration."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQnl0ZS1QYWlyIEVuY29kaW5nIChCUEUpIGlzIHRoZSB0b2tlbml6YXRpb24gYWxnb3JpdGhtIHVzZWQgYnkgR1BULTIsIEdQVC0zLCBhbmQgR1BULTQuIE9yaWdpbmFsbHkgYSBsb3NzbGVzcyBkYXRhLWNvbXByZXNzaW9uIHRlY2huaXF1ZSwgQlBFIHdhcyBhZGFwdGVkIGZvciBOTFAgYnkgU2VubnJpY2ggZXQgYWwuICgyMDE2KSB0byBoYW5kbGUgb3BlbiB2b2NhYnVsYXJpZXMgaW4gbmV1cmFsIG1hY2hpbmUgdHJhbnNsYXRpb24gd2l0aG91dCBvdXQtb2Ytdm9jYWJ1bGFyeSB0b2tlbnMuIFRoZSBhbGdvcml0aG0gc3RhcnRzIHdpdGggYSB2b2NhYnVsYXJ5IG9mIGluZGl2aWR1YWwgY2hhcmFjdGVycyAob3IgYnl0ZXMpLCB0aGVuIGl0ZXJhdGl2ZWx5IG1lcmdlcyB0aGUgbW9zdCBmcmVxdWVudCBhZGphY2VudCBzeW1ib2wgcGFpciB1bnRpbCB0aGUgdm9jYWJ1bGFyeSByZWFjaGVzIGEgdGFyZ2V0IHNpemUgVi4gVGhlIHJlc3VsdCBpcyBhIHNldCBvZiBzdWJ3b3JkIHVuaXRzIHJhbmdpbmcgZnJvbSBzaW5nbGUgY2hhcmFjdGVycyB0byBjb21wbGV0ZSBjb21tb24gd29yZHMsIHdpdGggcmFyZSB3b3JkcyBzcGxpdCBpbnRvIHRoZWlyIG1vc3QgZnJlcXVlbnQgY29uc3RpdHVlbnQgcGllY2VzLiBCZWNhdXNlIGV2ZXJ5IHBvc3NpYmxlIGJ5dGUgaXMgaW4gdGhlIGluaXRpYWwgdm9jYWJ1bGFyeSwgYnl0ZS1sZXZlbCBCUEUgZ3VhcmFudGVlcyB0aGF0IGFueSBpbnB1dCB0ZXh0IGNhbiBiZSBlbmNvZGVkIHdpdGhvdXQgYW4gW1VOS10gdG9rZW4uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW50cm9kdWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXb3JkLWxldmVsIHZvY2FidWxhcmllcyBzdWZmZXIgZnJvbSBvdXQtb2Ytdm9jYWJ1bGFyeSB0b2tlbnMgYW5kIHJlcXVpcmUgNTAwSysgZW50cmllcyB0byBjb3ZlciBtb3JwaG9sb2dpY2FsbHkgcmljaCBsYW5ndWFnZXMuIENoYXJhY3Rlci1sZXZlbCBtb2RlbHMgYXZvaWQgT09WIGJ1dCBwcm9kdWNlIHZlcnkgbG9uZyBzZXF1ZW5jZXMuIEJQRSBmaW5kcyBhIG1pZGRsZSBncm91bmQ6IGEgMzJL4oCTMTAwSyBzdWJ3b3JkIHZvY2FidWxhcnkgY292ZXJzIGFueSBpbnB1dCB3aXRob3V0IFVOSyB3aGlsZSBrZWVwaW5nIGF2ZXJhZ2Ugc2VxdWVuY2UgbGVuZ3RoIG1hbmFnZWFibGUuIEdQVC0yIHVzZXMgNTAsMjU3LXRva2VuIGJ5dGUtbGV2ZWwgQlBFIHdoZXJlIGFsbCAyNTYgYnl0ZXMgZm9ybSB0aGUgYmFzZSB2b2NhYnVsYXJ5LCBlbnN1cmluZyB6ZXJvIE9PVi4gR1BULTRcdTAwMjdzIGNsMTAwa19iYXNlIHVzZXMgMTAwLDI3NyB0b2tlbnMgd2l0aCBhIHJlZmluZWQgNS1wYXR0ZXJuIHJlZ2V4IHByZS10b2tlbml6ZXIuIFRoZSBmZXJ0aWxpdHkgbWV0cmlj4oCUYXZlcmFnZSB0b2tlbnMgcGVyIHdvcmTigJRtZWFzdXJlcyBob3cgZWZmaWNpZW50bHkgYSB0b2tlbml6ZXIgdXNlcyBjb250ZXh0LXdpbmRvdyBzcGFjZTsgR1BULTRcdTAwMjdzIGxhcmdlciB2b2NhYnVsYXJ5IGFjaGlldmVzIHJvdWdobHkgMS4y4oCTMS4zIHRva2Vucy93b3JkIG9uIEVuZ2xpc2ggdGV4dCwgdmVyc3VzIDEuM+KAkzEuNSBmb3IgR1BULTIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVyZ2UgQWxnb3JpdGhtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCUEUgdHJhaW5pbmcgbWFpbnRhaW5zIGEgZnJlcXVlbmN5IHRhYmxlIG1hcHBpbmcgZWFjaCBjdXJyZW50IHRva2VuIHNlcXVlbmNlIChhIHdvcmQgcmVwcmVzZW50ZWQgYXMgaXRzIGN1cnJlbnQgdG9rZW5zKSB0byBpdHMgY29ycHVzIGNvdW50LiBBdCBlYWNoIGl0ZXJhdGlvbjogKDEpIGNvdW50IGFsbCBhZGphY2VudCB0b2tlbiBwYWlycyBhY3Jvc3MgYWxsIHdvcmRzLCB3ZWlnaHRpbmcgYnkgd29yZCBmcmVxdWVuY3k7ICgyKSBzZWxlY3QgdGhlIG1vc3QgZnJlcXVlbnQgcGFpciAoYSwgYik7ICgzKSBhZGQgdGhlIG1lcmdlZCB0b2tlbiBhYiB0byB0aGUgdm9jYWJ1bGFyeTsgKDQpIHVwZGF0ZSB0aGUgdG9rZW4gc2VxdWVuY2VzIGJ5IHJlcGxhY2luZyBldmVyeSBvY2N1cnJlbmNlIG9mIChh4oCJYikgd2l0aCBhYi4gVGhlIHJlc3VsdCBpcyBhbiBvcmRlcmVkIG1lcmdlIHRhYmxl4oCUdGhlIG9yZGVyIG1hdHRlcnMgYmVjYXVzZSBlbmNvZGluZyBhcHBsaWVzIG1lcmdlcyBpbiB0aGUgc2FtZSBvcmRlci4gQSBwcmlvcml0eSBxdWV1ZSBvdmVyIHBhaXIgZnJlcXVlbmNpZXMgcmVkdWNlcyB0aGUgcGVyLW1lcmdlIHNjYW4gZnJvbSBPKE4pIHRvIE8obG9nIE4pLCB3aGljaCBpcyBob3cgdGlrdG9rZW4gYWNoaWV2ZXMgZmFzdCBlbmNvZGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlclxuaW1wb3J0IHJlXG5cbmRlZiBidWlsZF92b2NhYihjb3JwdXMpOlxuICAgIHZvY2FiID0gQ291bnRlcigpXG4gICAgZm9yIHdvcmQgaW4gY29ycHVzLnNwbGl0KCk6XG4gICAgICAgIHZvY2FiW1x1MDAyNyBcdTAwMjcuam9pbihsaXN0KHdvcmQpKSArIFx1MDAyNyBcdTAwM2Mvd1x1MDAzZVx1MDAyN10gKz0gMVxuICAgIHJldHVybiBkaWN0KHZvY2FiKVxuXG5kZWYgZ2V0X3BhaXJfc3RhdHModm9jYWIpOlxuICAgIHBhaXJzID0gQ291bnRlcigpXG4gICAgZm9yIHdvcmQsIGZyZXEgaW4gdm9jYWIuaXRlbXMoKTpcbiAgICAgICAgc3ltYm9scyA9IHdvcmQuc3BsaXQoKVxuICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4oc3ltYm9scykgLSAxKTpcbiAgICAgICAgICAgIHBhaXJzWyhzeW1ib2xzW2ldLCBzeW1ib2xzW2krMV0pXSArPSBmcmVxXG4gICAgcmV0dXJuIHBhaXJzXG5cbmRlZiBtZXJnZV9wYWlyKHBhaXIsIHZvY2FiKTpcbiAgICBwYXQgPSByZS5jb21waWxlKHJcdTAwMjcoP1x1MDAzYyFcXFMpXHUwMDI3ICsgcmUuZXNjYXBlKFx1MDAyNyBcdTAwMjcuam9pbihwYWlyKSkgKyByXHUwMDI3KD8hXFxTKVx1MDAyNylcbiAgICByZXR1cm4ge3BhdC5zdWIoXHUwMDI3XHUwMDI3LmpvaW4ocGFpciksIHcpOiBmIGZvciB3LCBmIGluIHZvY2FiLml0ZW1zKCl9XG5cbmRlZiB0cmFpbl9icGUoY29ycHVzLCBudW1fbWVyZ2VzKTpcbiAgICB2b2NhYiwgbWVyZ2VzID0gYnVpbGRfdm9jYWIoY29ycHVzKSwgW11cbiAgICBmb3IgaSBpbiByYW5nZShudW1fbWVyZ2VzKTpcbiAgICAgICAgc3RhdHMgPSBnZXRfcGFpcl9zdGF0cyh2b2NhYilcbiAgICAgICAgaWYgbm90IHN0YXRzOlxuICAgICAgICAgICAgYnJlYWtcbiAgICAgICAgYmVzdCA9IG1heChzdGF0cywga2V5PXN0YXRzLmdldClcbiAgICAgICAgdm9jYWIgPSBtZXJnZV9wYWlyKGJlc3QsIHZvY2FiKVxuICAgICAgICBtZXJnZXMuYXBwZW5kKGJlc3QpXG4gICAgICAgIHByaW50KGZcdTAwMjcgIE1lcmdlIHtpKzE6MmR9OiB7YmVzdFswXStcIiBcIitiZXN0WzFdOlx1MDAzYzIwfSAtXHUwMDNlIHtcInxcIi5qb2luKGJlc3QpOlx1MDAzYzE4fSBmcmVxPXtzdGF0c1tiZXN0XX1cdTAwMjcpXG4gICAgcmV0dXJuIG1lcmdlc1xuXG5jb3JwdXMgPSBcdTAwMjdsb3cgbG93ZXIgbG93ZXN0IG5ld2VyIG5ld2VzdCB3aWRlciB3aWRlc3QgcnVubmluZyBydW5uZXIgcnVucyBcdTAwMjcgKiAyNVxucHJpbnQoXHUwMDI3QlBFIFRyYWluaW5nOlx1MDAyNylcbm1lcmdlX3RhYmxlID0gdHJhaW5fYnBlKGNvcnB1cywgbnVtX21lcmdlcz0xNSlcbnByaW50KGZcdTAwMjdUb3RhbCBtZXJnZXMgbGVhcm5lZDoge2xlbihtZXJnZV90YWJsZSl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZvY2FidWxhcnkgQ29uc3RydWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZnRlciB0cmFpbmluZywgdGhlIHZvY2FidWxhcnkgPSBpbml0aWFsIGNoYXJhY3RlciBzZXQgKyBvbmUgbmV3IHRva2VuIHBlciBtZXJnZS4gRm9yIEdQVC0yXHUwMDI3cyBieXRlLWxldmVsIEJQRTogMjU2IGJ5dGUgdG9rZW5zICsgNTAsMDAwIG1lcmdlcyArIDEgc3BlY2lhbCB0b2tlbiA9IDUwLDI1Ny4gTGFyZ2VyIHZvY2FidWxhcmllcyByZWR1Y2UgZmVydGlsaXR5IGJ1dCBpbmNyZWFzZSBlbWJlZGRpbmctbWF0cml4IG1lbW9yeS4gQXQgNzY4IGRpbWVuc2lvbnMsIGEgMTAwSy10b2tlbiB2b2NhYnVsYXJ5IHVzZXMgMTAwSyDDlyA3Njggw5cgNCBieXRlcyDiiYggMjk14oCvTUIgZm9yIGVtYmVkZGluZ3MgYWxvbmUuIFRhaWwgdG9rZW5z4oCUdG9rZW5zIHRoYXQgYXBwZWFyIHZlcnkgcmFyZWx5IGluIHRoZSB0cmFpbmluZyBjb3JwdXPigJRjb25zdW1lIHZvY2FidWxhcnkgc2xvdHMgd2l0aG91dCBjb250cmlidXRpbmcgbWVhbmluZ2Z1bGx5IHRvIG1vZGVsIHF1YWxpdHk7IHNvbWUgdG9rZW5pemVyIGltcGxlbWVudGF0aW9ucyBwcnVuZSB0b2tlbnMgYmVsb3cgYSBtaW5pbXVtIGZyZXF1ZW5jeSB0aHJlc2hvbGQgYmVmb3JlIGZpbmFsaXNpbmcgdGhlIHZvY2FidWxhcnkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiBicGVfZW5jb2RlKHdvcmQsIG1lcmdlcyk6XG4gICAgdG9rZW5zID0gbGlzdCh3b3JkKSArIFtcdTAwMjdcdTAwM2Mvd1x1MDAzZVx1MDAyN11cbiAgICBmb3IgcGFpciBpbiBtZXJnZXM6XG4gICAgICAgIGksIG5ldyA9IDAsIFtdXG4gICAgICAgIHdoaWxlIGkgXHUwMDNjIGxlbih0b2tlbnMpOlxuICAgICAgICAgICAgaWYgaSBcdTAwM2MgbGVuKHRva2VucykgLSAxIGFuZCAodG9rZW5zW2ldLCB0b2tlbnNbaSsxXSkgPT0gcGFpcjpcbiAgICAgICAgICAgICAgICBuZXcuYXBwZW5kKFx1MDAyN1x1MDAyNy5qb2luKHBhaXIpKVxuICAgICAgICAgICAgICAgIGkgKz0gMlxuICAgICAgICAgICAgZWxzZTpcbiAgICAgICAgICAgICAgICBuZXcuYXBwZW5kKHRva2Vuc1tpXSlcbiAgICAgICAgICAgICAgICBpICs9IDFcbiAgICAgICAgdG9rZW5zID0gbmV3XG4gICAgcmV0dXJuIHRva2Vuc1xuXG5kZWYgYnBlX2RlY29kZSh0b2tlbnMpOlxuICAgIHJldHVybiBcdTAwMjdcdTAwMjcuam9pbih0b2tlbnMpLnJlcGxhY2UoXHUwMDI3XHUwMDNjL3dcdTAwM2VcdTAwMjcsIFx1MDAyN1x1MDAyNylcblxudGVzdF93b3JkcyA9IFtcdTAwMjdsb3dcdTAwMjcsIFx1MDAyN2xvd2VyXHUwMDI3LCBcdTAwMjdsb3dlc3RcdTAwMjcsIFx1MDAyN25ld2VyXHUwMDI3LCBcdTAwMjd3aWRlc3RcdTAwMjcsIFx1MDAyN3Vua25vd25cdTAwMjcsIFx1MDAyN3J1bm5lclx1MDAyN11cbnByaW50KGZcdTAwMjd7XCJXb3JkXCI6XHUwMDNjMTJ9IHtcIkJQRSBUb2tlbnNcIjpcdTAwM2M0Mn0ge1wiQ291bnRcIjpcdTAwM2U1fVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA2MilcbmZvciB3IGluIHRlc3Rfd29yZHM6XG4gICAgdG9rcyA9IGJwZV9lbmNvZGUodywgbWVyZ2VfdGFibGUpXG4gICAgZGVjICA9IGJwZV9kZWNvZGUodG9rcylcbiAgICBvayAgID0gXHUwMDI3T0tcdTAwMjcgaWYgZGVjID09IHcgZWxzZSBcdTAwMjdFUlJcdTAwMjdcbiAgICBwcmludChmXHUwMDI3e3c6XHUwMDNjMTJ9IHtzdHIodG9rcyk6XHUwMDNjNDJ9IHtsZW4odG9rcyk6XHUwMDNlNX0gIFt7b2t9XVx1MDAyNylcblxucHJpbnQoXHUwMDI3XFxuRGVjb2Rpbmc6IGpvaW4gdG9rZW5zLCBzdHJpcCBcdTAwM2Mvd1x1MDAzZS4gTG9zc2xlc3MgZm9yIGtub3duIGNoYXJzLlx1MDAyNylcbnByaW50KFx1MDAyN1Vua25vd24gd29yZHMgc3BsaXQgdG8gY2hhcnMgZmlyc3QsIHRoZW4gbWVyZ2VzIGFwcGxpZWQgd2hlcmUgcG9zc2libGUuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVuY29kaW5nIGFuZCBEZWNvZGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQlBFIGVuY29kaW5nIGFwcGxpZXMgbGVhcm5lZCBtZXJnZXMgaW4gb3JkZXI6IHNjYW4gdGhlIGN1cnJlbnQgdG9rZW4gbGlzdCBmb3IgdGhlIGhpZ2hlc3QtcHJpb3JpdHkgbWVyZ2UgcGFpciwgYXBwbHkgaXQsIHJlc2Nhbi4gVGhpcyBncmVlZHkgcHJvY2VzcyBpcyBPKE0gw5cgVCkgcGVyIHdvcmQgd2hlcmUgTSBpcyB0aGUgbnVtYmVyIG9mIG1lcmdlcyBhbmQgVCBpcyB0aGUgd29yZCBsZW5ndGguIFRoZSB0aWt0b2tlbiBsaWJyYXJ5IHVzZXMgYSBwcmlvcml0eS1xdWV1ZSBhcHByb2FjaCB0aGF0IGFjaGlldmVzIG5lYXItbGluZWFyIHRpbWUgYW5kIGlzIDXigJMyMMOXIGZhc3RlciB0aGFuIFB5dGhvbiBCUEUgaW1wbGVtZW50YXRpb25zLiBEZWNvZGluZyBpcyB0cml2aWFsOiBjb25jYXRlbmF0ZSB0aGUgc3Vid29yZCB0b2tlbnMgYW5kIHJlbW92ZSB0aGUgZW5kLW9mLXdvcmQgbWFya2VyIChcdTAwM2Mvd1x1MDAzZSBmb3Igc3RhbmRhcmQgQlBFOyBieXRlLWxldmVsIEdQVC0yIHVzZXMgYSBzZXBhcmF0ZSBieXRlLXRvLXVuaWNvZGUgbWFwcGluZyB3aGVyZSBzcGFjZSDDsMKdwoTCoCBhbmQgbmV3bGluZSDEgCBhcmUgcmVwcmVzZW50ZWQgYXMgc2luZ2xlIFVuaWNvZGUgY2hhcmFjdGVycykuIEJlY2F1c2UgZXZlcnkgYnl0ZSBpcyBpbiB0aGUgaW5pdGlhbCB2b2NhYnVsYXJ5LCBkZWNvZGluZyBpcyBhbHdheXMgbG9zc2xlc3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJlLVRva2VuaXphdGlvbiBhbmQgUmVnZXggU3BsaXRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZWZvcmUgQlBFIGlzIGFwcGxpZWQsIEdQVC00XHUwMDI3cyBjbDEwMGtfYmFzZSB1c2VzIGEgNS1wYXR0ZXJuIHJlZ2V4IHRvIHNwbGl0IHRleHQgaW50byBwcmUtdG9rZW5zOiAoMSkgY29udHJhY3Rpb25zIGxpa2UgXHUwMDI3cywgXHUwMDI3dCwgXHUwMDI3cmU7ICgyKSBzZXF1ZW5jZXMgb2YgbGV0dGVyczsgKDMpIHNlcXVlbmNlcyBvZiBkaWdpdHM7ICg0KSBzZXF1ZW5jZXMgb2Ygbm9uLXdoaXRlc3BhY2UsIG5vbi1sZXR0ZXIsIG5vbi1kaWdpdCBjaGFyYWN0ZXJzOyAoNSkgd2hpdGVzcGFjZS4gVGhpcyBwcmV2ZW50cyBCUEUgZnJvbSBwcm9kdWNpbmcgY3Jvc3Mtd29yZCBtZXJnZXMgc3VjaCBhcyBcdTAwMjdlIFx1MDAyNyAoZW5kIG9mIFx1MDAyN3RoZVx1MDAyNyBmdXNlZCB3aXRoIHRoZSBzcGFjZSBiZWZvcmUgdGhlIG5leHQgd29yZCkuIFdpdGhvdXQgcHJlLXRva2VuaXphdGlvbiwgQlBFIHdvdWxkIGZyZWVseSBtZXJnZSBhY3Jvc3Mgd29yZCBib3VuZGFyaWVzLCBjcmVhdGluZyB0b2tlbnMgdGhhdCBkZXBlbmQgb24gY29udGV4dCByYXRoZXIgdGhhbiBqdXN0IHN1YndvcmQgY29udGVudC4gR1BULTIgdXNlcyBhIHNpbXBsZXIgcmVnZXguIExhbmd1YWdlLXNwZWNpZmljIHByZS10b2tlbml6ZXJzIGZvciBDaGluZXNlLCBKYXBhbmVzZSwgYW5kIGNvZGUgdXNlIGRpZmZlcmVudCBzcGxpdCBzdHJhdGVnaWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXJcblxuZGVmIHNpbXBsZV9icGVfZmVydGlsaXR5KGNvcnB1cywgbl9tZXJnZXMpOlxuICAgIFwiXCJcIkNvbXB1dGUgYXZnIHRva2Vucy93b3JkIGFmdGVyIG5fbWVyZ2VzIEJQRSBvcGVyYXRpb25zLlwiXCJcIlxuICAgIHdvcmRfZnJlcSA9IENvdW50ZXIoY29ycHVzLnNwbGl0KCkpXG4gICAgdm9jYWIgPSB7XHUwMDI3IFx1MDAyNy5qb2luKGxpc3QodykpICsgXHUwMDI3IFx1MDAzYy93XHUwMDNlXHUwMDI3OiBmIGZvciB3LCBmIGluIHdvcmRfZnJlcS5pdGVtcygpfVxuXG4gICAgZGVmIGdldF9zdGF0cyh2KTpcbiAgICAgICAgcGFpcnMgPSBDb3VudGVyKClcbiAgICAgICAgZm9yIHdvcmQsIGZyZXEgaW4gdi5pdGVtcygpOlxuICAgICAgICAgICAgc3ltcyA9IHdvcmQuc3BsaXQoKVxuICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKHN5bXMpIC0gMSk6XG4gICAgICAgICAgICAgICAgcGFpcnNbKHN5bXNbaV0sIHN5bXNbaSsxXSldICs9IGZyZXFcbiAgICAgICAgcmV0dXJuIHBhaXJzXG5cbiAgICBkZWYgbWVyZ2UocGFpciwgdik6XG4gICAgICAgIHBhdCA9IHJlLmNvbXBpbGUoclx1MDAyNyg/XHUwMDNjIVxcUylcdTAwMjcgKyByZS5lc2NhcGUoXHUwMDI3IFx1MDAyNy5qb2luKHBhaXIpKSArIHJcdTAwMjcoPyFcXFMpXHUwMDI3KVxuICAgICAgICByZXR1cm4ge3BhdC5zdWIoXHUwMDI3XHUwMDI3LmpvaW4ocGFpciksIHcpOiBmIGZvciB3LCBmIGluIHYuaXRlbXMoKX1cblxuICAgIGZvciBfIGluIHJhbmdlKG5fbWVyZ2VzKTpcbiAgICAgICAgc3RhdHMgPSBnZXRfc3RhdHModm9jYWIpXG4gICAgICAgIGlmIG5vdCBzdGF0czpcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIHZvY2FiID0gbWVyZ2UobWF4KHN0YXRzLCBrZXk9c3RhdHMuZ2V0KSwgdm9jYWIpXG5cbiAgICB0b3RhbF90b2sgPSBzdW0obGVuKHcuc3BsaXQoKSkgKiBmIGZvciB3LCBmIGluIHZvY2FiLml0ZW1zKCkpXG4gICAgcmV0dXJuIHRvdGFsX3RvayAvIHN1bSh3b3JkX2ZyZXEudmFsdWVzKCkpXG5cbmNvcnB1cyA9IChcdTAwMjd0aGUgcXVpY2sgYnJvd24gZm94IGp1bXBzIG92ZXIgdGhlIGxhenkgZG9nIFx1MDAyN1xuICAgICAgICAgIFx1MDAyN3J1bm5pbmcgcnVubmVyIHJ1bnMgbG93ZXIgbG93ZXN0IG5ld2VyIG5ld2VzdCB3aWRlciB3aWRlc3QgXHUwMDI3KSAqIDMwXG5wcmludChcdTAwMjdDb3JwdXMgZmVydGlsaXR5IHZzIEJQRSBtZXJnZSBjb3VudDpcdTAwMjcpXG5wcmludChmXHUwMDI3e1wiTWVyZ2VzXCI6XHUwMDNlOH0ge1wiQXBwcm94IFNjYWxlXCI6XHUwMDNlMTR9IHtcIkZlcnRpbGl0eVwiOlx1MDAzZTEyfVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiAzOClcbmZvciBuLCBsYWJlbCBpbiBbKDAsIFx1MDAyN2NoYXItbGV2ZWxcdTAwMjcpLCAoOCwgXHUwMDI3fjFLIHZvY2FiXHUwMDI3KSwgKDIwLCBcdTAwMjd+OEsgdm9jYWJcdTAwMjcpLCAoNDAsIFx1MDAyN34zMksgdm9jYWJcdTAwMjcpXTpcbiAgICBmID0gc2ltcGxlX2JwZV9mZXJ0aWxpdHkoY29ycHVzLCBuKVxuICAgIHByaW50KGZcdTAwMjd7bjpcdTAwM2U4fSB7bGFiZWw6XHUwMDNlMTR9IHtmOlx1MDAzZTEyLjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGZXJ0aWxpdHkgYW5kIFZvY2FidWxhcnkgU2l6ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmVydGlsaXR5ID0gYXZlcmFnZSB0b2tlbnMgcGVyIHdvcmQuIEZvciBFbmdsaXNoLCBHUFQtMiAoNTBLIHZvY2FiKSBhY2hpZXZlcyBmZXJ0aWxpdHkg4omIMS4z4oCTMS41OyBHUFQtNCAoMTAwSykgYWNoaWV2ZXMg4omIMS4y4oCTMS4zLiBOb24tRW5nbGlzaCBsYW5ndWFnZXMgc3VmZmVyIGhpZ2hlciBmZXJ0aWxpdHkgd2hlbiB1bmRlci1yZXByZXNlbnRlZCBpbiB0cmFpbmluZyBkYXRhOiBDaGluZXNlIHRleHQgbWF5IHJlYWNoIDLigJM0IHRva2Vucy93b3JkIG9uIEdQVC0yIGJlY2F1c2UgQ0pLIGNoYXJhY3RlcnMgYXJlIHJhcmUgaW4gaXRzIEVuZ2xpc2gtaGVhdnkgY29ycHVzLiBGZXJ0aWxpdHkgZGlyZWN0bHkgZGV0ZXJtaW5lcyBlZmZlY3RpdmUgY29udGV4dCB3aW5kb3cgbGVuZ3RoOiBhdCBmZXJ0aWxpdHkgMi4wLCBhIDQwOTYtdG9rZW4gY29udGV4dCBob2xkcyBvbmx5IOKJiDIwNDggd29yZHMuIENob29zaW5nIHZvY2FidWxhcnkgc2l6ZSBWIHJlcXVpcmVzIGJhbGFuY2luZyBmZXJ0aWxpdHksIGVtYmVkZGluZy1tYXRyaXggbWVtb3J5LCBhbmQgZnJlcXVlbmN5IG9mIHRhaWwgdG9rZW5zIGluIHRoZSB0cmFpbmluZyBjb3JwdXMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIk9PViBSYXRlIiwiQXZnIEZlcnRpbGl0eSIsIlZvY2FiIFNpemUiLCJUcmFpbmluZyBDb21wbGV4aXR5IiwiVXNlZCBCeSJdLCJyb3dzIjpbWyJDaGFyYWN0ZXItbGV2ZWwiLCIwJSIsIjTigJM2IHRvay93b3JkIiwifjEwMOKAkzMwMCIsIk8oQykgdHJpdmlhbCIsIkVhcmx5IGNoYXItUk5OcyJdLFsiV29yZC1sZXZlbCIsIjHigJM1JSIsIjEuMCB0b2svd29yZCIsIjUwS+KAkzUwMEsiLCJPKFYpIGZhc3QiLCJDbGFzc2ljIE5MUCwgd29yZDJ2ZWMiXSxbIkJQRSIsIjAlIChieXRlLWxldmVsKSIsIjEuMuKAkzEuOCB0b2svd29yZCIsIjMyS+KAkzEwMEsiLCJPKFYgw5cgbWVyZ2VzKSIsIkdQVC0yLzMvNCwgUm9CRVJUYSJdLFsiVW5pZ3JhbSBMTSIsIjAlIChieXRlIGZhbGxiYWNrKSIsIjEuMuKAkzEuOCB0b2svd29yZCIsIjE2S+KAkzY0SyIsIk8oViDDlyBFTSBpdGVycykiLCJUNSwgbVQ1LCBHZW1tYSwgTExhTUEiXSxbIldvcmRQaWVjZSIsIn4wLjElIChbVU5LXSkiLCIxLjPigJMyLjAgdG9rL3dvcmQiLCIyOEvigJMzMksiLCJPKFYgw5cgbGlrZWxpaG9vZCkiLCJCRVJULCBEaXN0aWxCRVJULCBFTEVDVFJBIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIdWdnaW5nRmFjZSBJbnRlZ3JhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSHVnZ2luZ0ZhY2UgQXV0b1Rva2VuaXplciBsb2FkcyB0aGUgY29ycmVjdCB0b2tlbml6ZXIgY2xhc3MgZm9yIGFueSBtb2RlbCBjaGVja3BvaW50LiBHUFQtMiB1c2VzIFByZVRyYWluZWRUb2tlbml6ZXJGYXN0LCBiYWNrZWQgYnkgdGhlIFJ1c3QgdG9rZW5pemVycyBsaWJyYXJ54oCUdHlwaWNhbGx5IDEw4oCTMTAww5cgZmFzdGVyIHRoYW4gdGhlIFB5dGhvbiBpbXBsZW1lbnRhdGlvbiBhbmQgc3VwcG9ydGluZyBvZmZzZXRfbWFwcGluZyB0byBhbGlnbiB0b2tlbiBwb3NpdGlvbnMgYmFjayB0byBjaGFyYWN0ZXIgc3BhbnMgaW4gdGhlIG9yaWdpbmFsIHRleHQuIFRoaXMgaXMgZXNzZW50aWFsIGZvciBzcGFuLWV4dHJhY3Rpb24gdGFza3Mgc3VjaCBhcyBORVIgYW5kIFFBLiBGb3IgR1BULTRcdTAwMjdzIGNsMTAwa19iYXNlLCB1c2UgdGhlIHRpa3Rva2VuIGxpYnJhcnkgZGlyZWN0bHkgKG5vdCBhdmFpbGFibGUgdGhyb3VnaCBIdWdnaW5nRmFjZSksIHdoaWNoIGlzIHRoZSBwcm9kdWN0aW9uIHRva2VuaXplciB1c2VkIGJ5IE9wZW5BSVx1MDAyN3MgQVBJLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG4jIExvYWQgR1BULTIgdG9rZW5pemVyICg1MCwyNTctdG9rZW4gYnl0ZS1sZXZlbCBCUEUpXG50b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcdTAwMjdncHQyXHUwMDI3KVxuXG50ZXh0ID0gXHUwMDI3Qnl0ZS1wYWlyIGVuY29kaW5nIG1lcmdlcyBmcmVxdWVudCBjaGFyYWN0ZXIgcGFpcnMgaXRlcmF0aXZlbHkuXHUwMDI3XG5lbmNvZGluZyA9IHRva2VuaXplcih0ZXh0LCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNywgcmV0dXJuX29mZnNldHNfbWFwcGluZz1UcnVlKVxuaWRzICAgICA9IGVuY29kaW5nW1x1MDAyN2lucHV0X2lkc1x1MDAyN11bMF0udG9saXN0KClcbm9mZnNldHMgPSBlbmNvZGluZ1tcdTAwMjdvZmZzZXRfbWFwcGluZ1x1MDAyN11bMF0udG9saXN0KClcbnRva2VucyAgPSB0b2tlbml6ZXIuY29udmVydF9pZHNfdG9fdG9rZW5zKGlkcylcblxucHJpbnQoZlx1MDAyN1RleHQgICA6IHt0ZXh0fVx1MDAyNylcbnByaW50KGZcdTAwMjdUb2tlbnMgOiB7dG9rZW5zfVx1MDAyNylcbnByaW50KGZcdTAwMjdWb2NhYiBzaXplIDoge3Rva2VuaXplci52b2NhYl9zaXplfVx1MDAyNylcbnByaW50KGZcdTAwMjdTcGVjaWFsICAgIDoge3Rva2VuaXplci5hbGxfc3BlY2lhbF90b2tlbnN9XHUwMDI3KVxucHJpbnQoKVxucHJpbnQoZlx1MDAyN3tcIlRva2VuXCI6XHUwMDNjMjJ9IHtcIklEXCI6XHUwMDNlNn0gIENoYXIgc3Bhblx1MDAyNylcbmZvciB0b2ssIHRpZCwgKHMsIGUpIGluIHppcCh0b2tlbnMsIGlkcywgb2Zmc2V0cyk6XG4gICAgcHJpbnQoZlx1MDAyN3tyZXByKHRvayk6XHUwMDNjMjJ9IHt0aWQ6XHUwMDNlNn0gIFt7c306e2V9XSAtXHUwMDNlIHtyZXByKHRleHRbczplXSl9XHUwMDI3KVxuXG53b3JkcyA9IFtcdTAwMjdIZWxsb1x1MDAyNywgXHUwMDI3U3VwZXJjYWxpZnJhZ2lsaXN0aWNcdTAwMjcsIFx1MDAyN3Rva2VuaXphdGlvblx1MDAyNywgXHUwMDI3R1BULTRcdTAwMjddXG5wcmludChcdTAwMjdcXG5GZXJ0aWxpdHkgc2FtcGxlcyAoR1BULTIgdG9rZW5pemVyKTpcdTAwMjcpXG5mb3IgdyBpbiB3b3JkczpcbiAgICB0b2tzID0gdG9rZW5pemVyLnRva2VuaXplKHcpXG4gICAgcHJpbnQoZlx1MDAyNyAge3chcjpcdTAwM2MyNX0gLVx1MDAzZSB7bGVuKHRva3MpfSB0b2tlbnM6IHt0b2tzfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6Ik1lcmdlIE9yZGVyIERlcGVuZGVuY3kiLCJjb250ZW50IjoiQlBFIG1lcmdlcyBhcmUgZ3JlZWR5IGFuZCBvcmRlci1kZXBlbmRlbnQg4oCUIGRpZmZlcmVudCBjb3JwdXMgc2FtcGxlcyBvciByYW5kb20gc2VlZHMgcHJvZHVjZSBkaWZmZXJlbnQgbWVyZ2Ugb3JkZXJzIGV2ZW4gZm9yIHRoZSBzYW1lIGZpbmFsIHZvY2FidWxhcnkgc2l6ZSwgbGVhZGluZyB0byBkaWZmZXJlbnQgdG9rZW5pemF0aW9ucyBvZiB0aGUgc2FtZSB0ZXh0LiBUd28gQlBFIHRva2VuaXplcnMgdHJhaW5lZCBvbiBkaWZmZXJlbnQgY29ycG9yYSB3aXRoIGlkZW50aWNhbCB0YXJnZXQgdm9jYWJ1bGFyeSBzaXplcyB3aWxsIGdlbmVyYWxseSBkaXNhZ3JlZSBvbiBob3cgdG8gdG9rZW5pemUgaWRlbnRpY2FsIGlucHV0cy4gQWx3YXlzIHVzZSB0aGUgZXhhY3QgdG9rZW5pemVyIGNoZWNrcG9pbnQgdGhhdCB3YXMgdXNlZCBkdXJpbmcgbW9kZWwgdHJhaW5pbmc7IHN1YnN0aXR1dGluZyBhIGRpZmZlcmVudCBCUEUgdG9rZW5pemVyIG9mIHRoZSBzYW1lIG5vbWluYWwgdm9jYWIgc2l6ZSB3aWxsIHByb2R1Y2UgaW5jb3JyZWN0IHRva2VuIElEcyBhbmQgZGVncmFkZSBtb2RlbCBxdWFsaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJQRSBzdGFydHMgZnJvbSBhIGNoYXJhY3RlciAob3IgYnl0ZSkgdm9jYWJ1bGFyeSBhbmQgZ3JlZWRpbHkgbWVyZ2VzIHRoZSBtb3N0IGZyZXF1ZW50IGFkamFjZW50IHBhaXIg4oCUIG9uZSBtZXJnZSBwZXIgdm9jYWJ1bGFyeSBzbG90LiIsIkdQVC0yIHVzZXMgYnl0ZS1sZXZlbCBCUEUgd2l0aCA1MCwyNTcgdG9rZW5zOyBHUFQtNCB1c2VzIGNsMTAwa19iYXNlIHdpdGggMTAwLDI3NyB0b2tlbnMgYW5kIGEgNS1wYXR0ZXJuIHJlZ2V4IHByZS10b2tlbml6ZXIuIiwiRmVydGlsaXR5IChhdmcgdG9rZW5zIHBlciB3b3JkKSBtZWFzdXJlcyB0b2tlbml6ZXIgZWZmaWNpZW5jeTsgbG93ZXIgZmVydGlsaXR5IG1lYW5zIGZld2VyIHRva2VucyBwZXIgd29yZCBhbmQgbW9yZSB0ZXh0IGZpdHMgaW4gYSBmaXhlZCBjb250ZXh0IHdpbmRvdy4iLCJQcmUtdG9rZW5pemF0aW9uIHdpdGggcmVnZXggcHJldmVudHMgY3Jvc3Mtd29yZCBtZXJnZXM7IEdQVC00XHUwMDI3cyByZWdleCBzcGxpdHMgb24gY29udHJhY3Rpb25zLCBsZXR0ZXJzLCBkaWdpdHMsIGFuZCBwdW5jdHVhdGlvbiBzZXBhcmF0ZWx5LiIsIkJ5dGUtbGV2ZWwgQlBFIGd1YXJhbnRlZXMgemVybyBPT1Yg4oCUIGFueSBieXRlIHNlcXVlbmNlIGNhbiBiZSBlbmNvZGVkIHVzaW5nIHRoZSAyNTYgaW5pdGlhbCBieXRlIHRva2Vucy4iLCJMYXJnZXIgdm9jYWJ1bGFyeSBzaXplcyByZWR1Y2UgZmVydGlsaXR5IGJ1dCBpbmNyZWFzZSBlbWJlZGRpbmctbWF0cml4IG1lbW9yeTsgMTAwSyDDlyA3NjhkID0gMjk14oCvTUIgZm9yIGVtYmVkZGluZ3MgYWxvbmUuIiwiVXNlIHRpa3Rva2VuIGZvciBHUFQtNCB0b2tlbml6YXRpb247IHVzZSBIdWdnaW5nRmFjZSBBdXRvVG9rZW5pemVyIHdpdGggcmV0dXJuX29mZnNldHNfbWFwcGluZz1UcnVlIGZvciBzcGFuLWV4dHJhY3Rpb24gdGFza3MuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# BPE — Byte-Pair Encoding and LLM Vocabulary Construction

Byte-Pair Encoding (BPE) is the tokenization algorithm used by GPT-2, GPT-3, and GPT-4. Originally a lossless data-compression technique, BPE was adapted for NLP by Sennrich et al. (2016) to handle open vocabularies in neural machine translation without out-of-vocabulary tokens. The algorithm starts with a vocabulary of individual characters (or bytes), then iteratively merges the most frequent adjacent symbol pair until the vocabulary reaches a target size V. The result is a set of subword units ranging from single characters to complete common words, with rare words split into their most frequent constituent pieces. Because every possible byte is in the initial vocabulary, byte-level BPE guarantees that any input text can be encoded without an [UNK] token.

## Introduction

Word-level vocabularies suffer from out-of-vocabulary tokens and require 500K+ entries to cover morphologically rich languages. Character-level models avoid OOV but produce very long sequences. BPE finds a middle ground: a 32K–100K subword vocabulary covers any input without UNK while keeping average sequence length manageable. GPT-2 uses 50,257-token byte-level BPE where all 256 bytes form the base vocabulary, ensuring zero OOV. GPT-4's cl100k_base uses 100,277 tokens with a refined 5-pattern regex pre-tokenizer. The fertility metric—average tokens per word—measures how efficiently a tokenizer uses context-window space; GPT-4's larger vocabulary achieves roughly 1.2–1.3 tokens/word on English text, versus 1.3–1.5 for GPT-2.

## Merge Algorithm

BPE training maintains a frequency table mapping each current token sequence (a word represented as its current tokens) to its corpus count. At each iteration: (1) count all adjacent token pairs across all words, weighting by word frequency; (2) select the most frequent pair (a, b); (3) add the merged token ab to the vocabulary; (4) update the token sequences by replacing every occurrence of (a b) with ab. The result is an ordered merge table—the order matters because encoding applies merges in the same order. A priority queue over pair frequencies reduces the per-merge scan from O(N) to O(log N), which is how tiktoken achieves fast encoding.

```python
from collections import Counter
import re

def build_vocab(corpus):
    vocab = Counter()
    for word in corpus.split():
        vocab[' '.join(list(word)) + ' </w>'] += 1
    return dict(vocab)

def get_pair_stats(vocab):
    pairs = Counter()
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_pair(pair, vocab):
    pat = re.compile(r'(?<!\S)' + re.escape(' '.join(pair)) + r'(?!\S)')
    return {pat.sub(''.join(pair), w): f for w, f in vocab.items()}

def train_bpe(corpus, num_merges):
    vocab, merges = build_vocab(corpus), []
    for i in range(num_merges):
        stats = get_pair_stats(vocab)
        if not stats:
            break
        best = max(stats, key=stats.get)
        vocab = merge_pair(best, vocab)
        merges.append(best)
        print(f'  Merge {i+1:2d}: {best[0]+" "+best[1]:<20} -> {"|".join(best):<18} freq={stats[best]}')
    return merges

corpus = 'low lower lowest newer newest wider widest running runner runs ' * 25
print('BPE Training:')
merge_table = train_bpe(corpus, num_merges=15)
print(f'Total merges learned: {len(merge_table)}')
```

## Vocabulary Construction

After training, the vocabulary = initial character set + one new token per merge. For GPT-2's byte-level BPE: 256 byte tokens + 50,000 merges + 1 special token = 50,257. Larger vocabularies reduce fertility but increase embedding-matrix memory. At 768 dimensions, a 100K-token vocabulary uses 100K × 768 × 4 bytes ≈ 295 MB for embeddings alone. Tail tokens—tokens that appear very rarely in the training corpus—consume vocabulary slots without contributing meaningfully to model quality; some tokenizer implementations prune tokens below a minimum frequency threshold before finalising the vocabulary.

```python
def bpe_encode(word, merges):
    tokens = list(word) + ['</w>']
    for pair in merges:
        i, new = 0, []
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i+1]) == pair:
                new.append(''.join(pair))
                i += 2
            else:
                new.append(tokens[i])
                i += 1
        tokens = new
    return tokens

def bpe_decode(tokens):
    return ''.join(tokens).replace('</w>', '')

test_words = ['low', 'lower', 'lowest', 'newer', 'widest', 'unknown', 'runner']
print(f'{"Word":<12} {"BPE Tokens":<42} {"Count":>5}')
print('-' * 62)
for w in test_words:
    toks = bpe_encode(w, merge_table)
    dec  = bpe_decode(toks)
    ok   = 'OK' if dec == w else 'ERR'
    print(f'{w:<12} {str(toks):<42} {len(toks):>5}  [{ok}]')

print('\nDecoding: join tokens, strip </w>. Lossless for known chars.')
print('Unknown words split to chars first, then merges applied where possible.')
```

## Encoding and Decoding

BPE encoding applies learned merges in order: scan the current token list for the highest-priority merge pair, apply it, rescan. This greedy process is O(M × T) per word where M is the number of merges and T is the word length. The tiktoken library uses a priority-queue approach that achieves near-linear time and is 5–20× faster than Python BPE implementations. Decoding is trivial: concatenate the subword tokens and remove the end-of-word marker (</w> for standard BPE; byte-level GPT-2 uses a separate byte-to-unicode mapping where space ð  and newline Ā are represented as single Unicode characters). Because every byte is in the initial vocabulary, decoding is always lossless.

## Pre-Tokenization and Regex Splits

Before BPE is applied, GPT-4's cl100k_base uses a 5-pattern regex to split text into pre-tokens: (1) contractions like 's, 't, 're; (2) sequences of letters; (3) sequences of digits; (4) sequences of non-whitespace, non-letter, non-digit characters; (5) whitespace. This prevents BPE from producing cross-word merges such as 'e ' (end of 'the' fused with the space before the next word). Without pre-tokenization, BPE would freely merge across word boundaries, creating tokens that depend on context rather than just subword content. GPT-2 uses a simpler regex. Language-specific pre-tokenizers for Chinese, Japanese, and code use different split strategies.

```python
import re
from collections import Counter

def simple_bpe_fertility(corpus, n_merges):
    """Compute avg tokens/word after n_merges BPE operations."""
    word_freq = Counter(corpus.split())
    vocab = {' '.join(list(w)) + ' </w>': f for w, f in word_freq.items()}

    def get_stats(v):
        pairs = Counter()
        for word, freq in v.items():
            syms = word.split()
            for i in range(len(syms) - 1):
                pairs[(syms[i], syms[i+1])] += freq
        return pairs

    def merge(pair, v):
        pat = re.compile(r'(?<!\S)' + re.escape(' '.join(pair)) + r'(?!\S)')
        return {pat.sub(''.join(pair), w): f for w, f in v.items()}

    for _ in range(n_merges):
        stats = get_stats(vocab)
        if not stats:
            break
        vocab = merge(max(stats, key=stats.get), vocab)

    total_tok = sum(len(w.split()) * f for w, f in vocab.items())
    return total_tok / sum(word_freq.values())

corpus = ('the quick brown fox jumps over the lazy dog '
          'running runner runs lower lowest newer newest wider widest ') * 30
print('Corpus fertility vs BPE merge count:')
print(f'{"Merges":>8} {"Approx Scale":>14} {"Fertility":>12}')
print('-' * 38)
for n, label in [(0, 'char-level'), (8, '~1K vocab'), (20, '~8K vocab'), (40, '~32K vocab')]:
    f = simple_bpe_fertility(corpus, n)
    print(f'{n:>8} {label:>14} {f:>12.3f}')
```

## Fertility and Vocabulary Size

Fertility = average tokens per word. For English, GPT-2 (50K vocab) achieves fertility ≈1.3–1.5; GPT-4 (100K) achieves ≈1.2–1.3. Non-English languages suffer higher fertility when under-represented in training data: Chinese text may reach 2–4 tokens/word on GPT-2 because CJK characters are rare in its English-heavy corpus. Fertility directly determines effective context window length: at fertility 2.0, a 4096-token context holds only ≈2048 words. Choosing vocabulary size V requires balancing fertility, embedding-matrix memory, and frequency of tail tokens in the training corpus.

| Method | OOV Rate | Avg Fertility | Vocab Size | Training Complexity | Used By |
| --- | --- | --- | --- | --- | --- |
| Character-level | 0% | 4–6 tok/word | ~100–300 | O(C) trivial | Early char-RNNs |
| Word-level | 1–5% | 1.0 tok/word | 50K–500K | O(V) fast | Classic NLP, word2vec |
| BPE | 0% (byte-level) | 1.2–1.8 tok/word | 32K–100K | O(V × merges) | GPT-2/3/4, RoBERTa |
| Unigram LM | 0% (byte fallback) | 1.2–1.8 tok/word | 16K–64K | O(V × EM iters) | T5, mT5, Gemma, LLaMA |
| WordPiece | ~0.1% ([UNK]) | 1.3–2.0 tok/word | 28K–32K | O(V × likelihood) | BERT, DistilBERT, ELECTRA |

## HuggingFace Integration

HuggingFace AutoTokenizer loads the correct tokenizer class for any model checkpoint. GPT-2 uses PreTrainedTokenizerFast, backed by the Rust tokenizers library—typically 10–100× faster than the Python implementation and supporting offset_mapping to align token positions back to character spans in the original text. This is essential for span-extraction tasks such as NER and QA. For GPT-4's cl100k_base, use the tiktoken library directly (not available through HuggingFace), which is the production tokenizer used by OpenAI's API.

```python
from transformers import AutoTokenizer

# Load GPT-2 tokenizer (50,257-token byte-level BPE)
tokenizer = AutoTokenizer.from_pretrained('gpt2')

text = 'Byte-pair encoding merges frequent character pairs iteratively.'
encoding = tokenizer(text, return_tensors='pt', return_offsets_mapping=True)
ids     = encoding['input_ids'][0].tolist()
offsets = encoding['offset_mapping'][0].tolist()
tokens  = tokenizer.convert_ids_to_tokens(ids)

print(f'Text   : {text}')
print(f'Tokens : {tokens}')
print(f'Vocab size : {tokenizer.vocab_size}')
print(f'Special    : {tokenizer.all_special_tokens}')
print()
print(f'{"Token":<22} {"ID":>6}  Char span')
for tok, tid, (s, e) in zip(tokens, ids, offsets):
    print(f'{repr(tok):<22} {tid:>6}  [{s}:{e}] -> {repr(text[s:e])}')

words = ['Hello', 'Supercalifragilistic', 'tokenization', 'GPT-4']
print('\nFertility samples (GPT-2 tokenizer):')
for w in words:
    toks = tokenizer.tokenize(w)
    print(f'  {w!r:<25} -> {len(toks)} tokens: {toks}')
```

> **Merge Order Dependency**: BPE merges are greedy and order-dependent — different corpus samples or random seeds produce different merge orders even for the same final vocabulary size, leading to different tokenizations of the same text. Two BPE tokenizers trained on different corpora with identical target vocabulary sizes will generally disagree on how to tokenize identical inputs. Always use the exact tokenizer checkpoint that was used during model training; substituting a different BPE tokenizer of the same nominal vocab size will produce incorrect token IDs and degrade model quality.

## Key Takeaways

- BPE starts from a character (or byte) vocabulary and greedily merges the most frequent adjacent pair — one merge per vocabulary slot.
- GPT-2 uses byte-level BPE with 50,257 tokens; GPT-4 uses cl100k_base with 100,277 tokens and a 5-pattern regex pre-tokenizer.
- Fertility (avg tokens per word) measures tokenizer efficiency; lower fertility means fewer tokens per word and more text fits in a fixed context window.
- Pre-tokenization with regex prevents cross-word merges; GPT-4's regex splits on contractions, letters, digits, and punctuation separately.
- Byte-level BPE guarantees zero OOV — any byte sequence can be encoded using the 256 initial byte tokens.
- Larger vocabulary sizes reduce fertility but increase embedding-matrix memory; 100K × 768d = 295 MB for embeddings alone.
- Use tiktoken for GPT-4 tokenization; use HuggingFace AutoTokenizer with return_offsets_mapping=True for span-extraction tasks.

---

