---
title: "Iterative DPO — Online Preference Learning with Self-Generated Pairs"
slug: "iterative-dpo"
description: "Iterative DPO addresses the off-policy distribution mismatch in standard DPO by regenerating preference pairs from the current policy at each training round, closing most of the performance gap between offline DPO and online PPO at significantly lower implementation complexity."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlyZWN0IFByZWZlcmVuY2UgT3B0aW1pemF0aW9uIChEUE8pIGlzIHRyYWluZWQgb24gYSBmaXhlZCBkYXRhc2V0IG9mIChwcm9tcHQsIGNob3NlbiwgcmVqZWN0ZWQpIHRyaXBsZXMgY29sbGVjdGVkIG9mZmxpbmUg4oCUIHR5cGljYWxseSBmcm9tIGh1bWFuIGxhYmVsZXJzIGNvbXBhcmluZyBvdXRwdXRzIG9mIHRoZSBvcmlnaW5hbCBTRlQgbW9kZWwuIFRoaXMgc3RhdGljIGRhdGFzZXQgaGFzIGEgY3JpdGljYWwgbGltaXRhdGlvbjogYXMgdGhlIHBvbGljeSBpbXByb3ZlcyBkdXJpbmcgdHJhaW5pbmcsIHRoZSBwcmVmZXJlbmNlIHBhaXJzIGJlY29tZSBpbmNyZWFzaW5nbHkgb2ZmLXBvbGljeSByZWxhdGl2ZSB0byB0aGUgY3VycmVudCBtb2RlbCBkaXN0cmlidXRpb24uIEl0ZXJhdGl2ZSBEUE8gKGFsc28gY2FsbGVkIG9ubGluZSBEUE8pIGFkZHJlc3NlcyB0aGlzIGJ5IHBlcmlvZGljYWxseSByZWdlbmVyYXRpbmcgcHJlZmVyZW5jZSBwYWlycyBmcm9tIHRoZSBjdXJyZW50IHBvbGljeSwgZW5zdXJpbmcgdHJhaW5pbmcgZGF0YSBzdGF5cyBvbi1wb2xpY3kgYW5kIHJlbWFpbnMgaW5mb3JtYXRpdmUgdGhyb3VnaG91dCB0cmFpbmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaHkgU3RhdGljIERQTyBGYWxscyBTaG9ydCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIERQTyBsb3NzIGZ1bmN0aW9uIGltcGxpY2l0bHkgYXNzdW1lcyB0aGF0IHRoZSBjaG9zZW4gYW5kIHJlamVjdGVkIHJlc3BvbnNlcyBhcmUgZHJhd24gZnJvbSBhIGRpc3RyaWJ1dGlvbiBjbG9zZSB0byB0aGUgcmVmZXJlbmNlIG1vZGVsIM+AX3JlZi4gV2hlbiB0aGUgcG9saWN5IM+AX864IGRyaWZ0cyBmYXIgZnJvbSDPgF9yZWYgZHVyaW5nIHRyYWluaW5nLCB0aGUgcHJlZmVyZW5jZSBkYXRhIGJlY29tZXMgc3RhbGUg4oCUIHRoZSAoY2hvc2VuLCByZWplY3RlZCkgcGFpcnMgbm8gbG9uZ2VyIHJlcHJlc2VudCB0aGUgb3V0cHV0cyB0aGUgY3VycmVudCBwb2xpY3kgd291bGQgZ2VuZXJhdGUuIFRoaXMgaXMgdGhlIG9mZi1wb2xpY3kgcHJvYmxlbTogdGhlIG1vZGVsIGlzIGJlaW5nIHRyYWluZWQgdG8gcHJlZmVyIHJlc3BvbnNlIEEgb3ZlciByZXNwb25zZSBCLCBidXQgQSBhbmQgQiB3ZXJlIGdlbmVyYXRlZCBieSBhIG11Y2ggd2Vha2VyIG1vZGVsLCBzbyB0aGUgbGVzc29uIGlzIHRyaXZpYWwgZm9yIHRoZSBub3ctc3Ryb25nZXIgcG9saWN5LiBPbi1wb2xpY3kgcHJlZmVyZW5jZSBkYXRhIGZyb20gdGhlIGN1cnJlbnQgz4BfzrggcHJvdmlkZXMgYSBtdWNoIGhhcmRlciBhbmQgbW9yZSBpbmZvcm1hdGl2ZSB0cmFpbmluZyBzaWduYWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEl0ZXJhdGl2ZSBEUE8gQWxnb3JpdGhtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJdGVyYXRpdmUgRFBPIHJ1bnMgaW4gcm91bmRzOiAoMSkgc2FtcGxlIEsgY29tcGxldGlvbnMgcGVyIHByb21wdCBmcm9tIHRoZSBjdXJyZW50IHBvbGljeSDPgF/OuDsgKDIpIHNjb3JlIHRoZW0gd2l0aCBhIHJld2FyZCBtb2RlbCBvciBodW1hbiByYXRlcjsgKDMpIGZvcm0gKGNob3NlbiwgcmVqZWN0ZWQpIHBhaXJzIGZyb20gaGlnaGVzdC0gYW5kIGxvd2VzdC1zY29yaW5nIGNvbXBsZXRpb25zOyAoNCkgcnVuIGEgRFBPIHVwZGF0ZSBzdGVwIHdpdGggdGhlIG5ldyBvbi1wb2xpY3kgcGFpcnM7ICg1KSByZXBlYXQuIFRoZSByZWZlcmVuY2UgbW9kZWwgz4BfcmVmIGNhbiBiZSBrZXB0IGZpeGVkIChvcmlnaW5hbCBTRlQpIGZvciBzdGFiaWxpdHkgb3IgdXBkYXRlZCBwZXJpb2RpY2FsbHkuIEtleSBoeXBlcnBhcmFtZXRlcnM6IGhvdyBvZnRlbiB0byByZWdlbmVyYXRlIHBhaXJzIChldmVyeSBOIHN0ZXBzIG9yIGV2ZXJ5IGVwb2NoKSwgaG93IG1hbnkgc2FtcGxlcyBwZXIgcHJvbXB0LCBhbmQgdGhlIERQTyBiZXRhIChLTCBwZW5hbHR5IHdlaWdodCkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzXG5mcm9tIHR5cGluZyBpbXBvcnQgQ2FsbGFibGVcblxuQGRhdGFjbGFzc1xuY2xhc3MgSXRlcmF0aXZlRFBPQ29uZmlnOlxuICAgIG5fcm91bmRzOiBpbnQgPSAzXG4gICAgc2FtcGxlc19wZXJfcHJvbXB0OiBpbnQgPSAyXG4gICAgZHBvX2JldGE6IGZsb2F0ID0gMC4xXG4gICAgZHBvX2Vwb2Noc19wZXJfcm91bmQ6IGludCA9IDFcbiAgICBscjogZmxvYXQgPSA1ZS03XG4gICAgcmVmX3VwZGF0ZV9zdHJhdGVneTogc3RyID0gXHUwMDI3Zml4ZWRcdTAwMjcgICMgXHUwMDI3Zml4ZWRcdTAwMjcsIFx1MDAyN2VtYVx1MDAyNywgb3IgXHUwMDI3Y29weVx1MDAyN1xuXG5kZWYgaXRlcmF0aXZlX2Rwb19yb3VuZChcbiAgICBwb2xpY3ksXG4gICAgcmVmX21vZGVsLFxuICAgIHRva2VuaXplcixcbiAgICByZXdhcmRfbW9kZWwsXG4gICAgcHJvbXB0czogbGlzdCxcbiAgICBjb25maWc6IEl0ZXJhdGl2ZURQT0NvbmZpZyxcbiAgICByb3VuZF9pZHg6IGludCxcbiAgICBkcG9fdHJhaW5fZm46IENhbGxhYmxlLFxuKSAtXHUwMDNlIGRpY3Q6XG4gICAgIyBPbmUgcm91bmQ6IGdlbmVyYXRlIG9uLXBvbGljeSBwYWlycywgc2NvcmUsIHJ1biBEUE8gdXBkYXRlXG4gICAgcHJpbnQoZlx1MDAyN1JvdW5kIHtyb3VuZF9pZHgrMX06IHNhbXBsaW5nIHtjb25maWcuc2FtcGxlc19wZXJfcHJvbXB0fSBjb21wbGV0aW9ucy9wcm9tcHQgZnJvbSBjdXJyZW50IHBvbGljeVx1MDAyNylcbiAgICBwcmVmZXJlbmNlX2RhdGFzZXQgPSBnZW5lcmF0ZV9wcmVmZXJlbmNlX3BhaXJzKFxuICAgICAgICBwb2xpY3ksIHRva2VuaXplciwgcmV3YXJkX21vZGVsLCBwcm9tcHRzLCBjb25maWcuc2FtcGxlc19wZXJfcHJvbXB0XG4gICAgKVxuICAgIG5fcGFpcnMgPSBsZW4ocHJlZmVyZW5jZV9kYXRhc2V0W1x1MDAyN2Nob3Nlblx1MDAyN10pXG4gICAgcHJpbnQoZlx1MDAyN1JvdW5kIHtyb3VuZF9pZHgrMX06IERQTyB1cGRhdGUgb24ge25fcGFpcnN9IG9uLXBvbGljeSBwYWlycyAoYmV0YT17Y29uZmlnLmRwb19iZXRhfSlcdTAwMjcpXG4gICAgZHBvX3RyYWluX2ZuKHBvbGljeSwgcmVmX21vZGVsLCBwcmVmZXJlbmNlX2RhdGFzZXQsIGNvbmZpZylcbiAgICByZXR1cm4ge1x1MDAyN3JvdW5kXHUwMDI3OiByb3VuZF9pZHggKyAxLCBcdTAwMjduX3BhaXJzXHUwMDI3OiBuX3BhaXJzfVxuXG5jb25maWcgPSBJdGVyYXRpdmVEUE9Db25maWcobl9yb3VuZHM9Mywgc2FtcGxlc19wZXJfcHJvbXB0PTIsIGRwb19iZXRhPTAuMSlcbnByaW50KFx1MDAyN0l0ZXJhdGl2ZSBEUE86IG9uLXBvbGljeSBwcmVmZXJlbmNlIGRhdGEgZnJvbSBjdXJyZW50IHBpX3RoZXRhIGF0IGVhY2ggcm91bmRcdTAwMjcpXG5wcmludChcdTAwMjdLZXk6IHBhaXJzIGdlbmVyYXRlZCBieSBjdXJyZW50IHBvbGljeSBhcmUgaGFyZGVyIGFuZCBtb3JlIGluZm9ybWF0aXZlIHRoYW4gU0ZUIHBhaXJzXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9uLVBvbGljeSBQcmVmZXJlbmNlIFBhaXIgR2VuZXJhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXQgZWFjaCByb3VuZCwgdHdvIGNvbXBsZXRpb25zIGFyZSBzYW1wbGVkIGZyb20gdGhlIGN1cnJlbnQgcG9saWN5IHBlciBwcm9tcHQuIFRoZSByZXdhcmQgbW9kZWwgc2NvcmVzIGJvdGggYW5kIGRldGVybWluZXMgd2hpY2ggaXMgcHJlZmVycmVkLiBVc2luZyBvbmx5IDIgc2FtcGxlcyBpcyB0aGUgc2ltcGxlc3Qgc2V0dGluZyDigJQgdGhlIG1hcmdpbiBiZXR3ZWVuIGJlc3QgYW5kIHdvcnN0IHJlZmxlY3RzIHRoZSBwb2xpY3lcdTAwMjdzIGN1cnJlbnQgdW5jZXJ0YWludHkuIFVzaW5nIG1vcmUgc2FtcGxlcyAoNOKAkzgpIGFuZCB0YWtpbmcgdGhlIGhpZ2hlc3QgYW5kIGxvd2VzdCBzY29yZSBjcmVhdGVzIGxhcmdlciByZXdhcmQgbWFyZ2lucyBpbiB0aGUgcHJlZmVyZW5jZSBwYWlycywgcHJvdmlkaW5nIGEgY2xlYW5lciBsZWFybmluZyBzaWduYWwuIEZpbHRlcmluZyBvdXQgcGFpcnMgd2hlcmUgdGhlIHJld2FyZCBtYXJnaW4gaXMgYmVsb3cgYSB0aHJlc2hvbGQgKG1hcmdpbiBmaWx0ZXJpbmcpIHJlbW92ZXMgYW1iaWd1b3VzIHBhaXJzIHRoYXQgYWRkIG5vaXNlIHRvIHRyYWluaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gZGF0YXNldHMgaW1wb3J0IERhdGFzZXRcblxuZGVmIGdlbmVyYXRlX3ByZWZlcmVuY2VfcGFpcnMoXG4gICAgcG9saWN5LFxuICAgIHRva2VuaXplcixcbiAgICByZXdhcmRfbW9kZWwsXG4gICAgcHJvbXB0czogbGlzdCxcbiAgICBuX3NhbXBsZXM6IGludCA9IDIsXG4gICAgdGVtcGVyYXR1cmU6IGZsb2F0ID0gMC44LFxuICAgIG1pbl9tYXJnaW46IGZsb2F0ID0gMC4xLFxuKSAtXHUwMDNlIERhdGFzZXQ6XG4gICAgIyBTYW1wbGUgY29tcGxldGlvbnMgZnJvbSBjdXJyZW50IHBvbGljeSwgdXNlIFJNIHRvIGRldGVybWluZSBwcmVmZXJlbmNlXG4gICAgY2hvc2VuX2xpc3QsIHJlamVjdGVkX2xpc3QsIHByb21wdF9saXN0ID0gW10sIFtdLCBbXVxuICAgIGZvciBwcm9tcHQgaW4gcHJvbXB0czpcbiAgICAgICAgaW5wdXRzID0gdG9rZW5pemVyKHByb21wdCwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcpLnRvKHBvbGljeS5kZXZpY2UpXG4gICAgICAgIGNvbXBsZXRpb25zID0gW11cbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9zYW1wbGVzKTpcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIG91dHB1dCA9IHBvbGljeS5nZW5lcmF0ZShcbiAgICAgICAgICAgICAgICAgICAgKippbnB1dHMsXG4gICAgICAgICAgICAgICAgICAgIG1heF9uZXdfdG9rZW5zPTEyOCxcbiAgICAgICAgICAgICAgICAgICAgZG9fc2FtcGxlPVRydWUsXG4gICAgICAgICAgICAgICAgICAgIHRlbXBlcmF0dXJlPXRlbXBlcmF0dXJlLFxuICAgICAgICAgICAgICAgICAgICBwYWRfdG9rZW5faWQ9dG9rZW5pemVyLmVvc190b2tlbl9pZCxcbiAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICBnZW4gPSBvdXRwdXRbMF1baW5wdXRzW1x1MDAyN2lucHV0X2lkc1x1MDAyN10uc2hhcGVbMV06XVxuICAgICAgICAgICAgY29tcGxldGlvbnMuYXBwZW5kKHRva2VuaXplci5kZWNvZGUoZ2VuLCBza2lwX3NwZWNpYWxfdG9rZW5zPVRydWUpKVxuICAgICAgICBzY29yZXMgPSBbXVxuICAgICAgICBmb3IgYyBpbiBjb21wbGV0aW9uczpcbiAgICAgICAgICAgIGVuYyA9IHRva2VuaXplcihwcm9tcHQgKyBjLCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNywgdHJ1bmNhdGlvbj1UcnVlKS50byhyZXdhcmRfbW9kZWwuZGV2aWNlKVxuICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICAgICAgc2NvcmVzLmFwcGVuZChyZXdhcmRfbW9kZWwoKiplbmMpLmxvZ2l0cy5zcXVlZXplKCkuaXRlbSgpKVxuICAgICAgICBiZXN0X2lkeCA9IGludCh0b3JjaC50ZW5zb3Ioc2NvcmVzKS5hcmdtYXgoKSlcbiAgICAgICAgd29yc3RfaWR4ID0gaW50KHRvcmNoLnRlbnNvcihzY29yZXMpLmFyZ21pbigpKVxuICAgICAgICBtYXJnaW4gPSBzY29yZXNbYmVzdF9pZHhdIC0gc2NvcmVzW3dvcnN0X2lkeF1cbiAgICAgICAgaWYgbWFyZ2luIFx1MDAzZT0gbWluX21hcmdpbjpcbiAgICAgICAgICAgIGNob3Nlbl9saXN0LmFwcGVuZChjb21wbGV0aW9uc1tiZXN0X2lkeF0pXG4gICAgICAgICAgICByZWplY3RlZF9saXN0LmFwcGVuZChjb21wbGV0aW9uc1t3b3JzdF9pZHhdKVxuICAgICAgICAgICAgcHJvbXB0X2xpc3QuYXBwZW5kKHByb21wdClcbiAgICByZXR1cm4gRGF0YXNldC5mcm9tX2RpY3Qoe1x1MDAyN3Byb21wdFx1MDAyNzogcHJvbXB0X2xpc3QsIFx1MDAyN2Nob3Nlblx1MDAyNzogY2hvc2VuX2xpc3QsIFx1MDAyN3JlamVjdGVkXHUwMDI3OiByZWplY3RlZF9saXN0fSlcblxucHJpbnQoXHUwMDI3T24tcG9saWN5IHBhaXJzOiBib3RoIGNob3NlbiBhbmQgcmVqZWN0ZWQgY29tZSBmcm9tIGN1cnJlbnQgcGlfdGhldGFcdTAwMjcpXG5wcmludChcdTAwMjdNYXJnaW4gZmlsdGVyaW5nIChtaW5fbWFyZ2luPTAuMSkgcmVtb3ZlcyBhbWJpZ3VvdXMgcGFpcnMgZnJvbSB0cmFpbmluZ1x1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZWZlcmVuY2UgTW9kZWwgVXBkYXRlIFN0cmF0ZWdpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSByZWZlcmVuY2UgbW9kZWwgz4BfcmVmIGRldGVybWluZXMgdGhlIEtMIHBlbmFsdHkgdGFyZ2V0IOKAlCBrZWVwaW5nIM+AX864IGZyb20gZGV2aWF0aW5nIHRvbyBmYXIuIFRocmVlIHN0cmF0ZWdpZXMgZXhpc3Q6IChBKSBmaXhlZCByZWZlcmVuY2Ug4oCUIGtlZXAgdGhlIG9yaWdpbmFsIFNGVCBtb2RlbCBhcyDPgF9yZWYgdGhyb3VnaG91dCBhbGwgcm91bmRzLCBwcm92aWRpbmcgc3Ryb25nIHJlZ3VsYXJpc2F0aW9uIHRvd2FyZCB0aGUgU0ZUIGJhc2VsaW5lOyAoQikgRU1BIHVwZGF0ZSDigJQgc2xvd2x5IHRyYWNrIHRoZSBwb2xpY3kgd2l0aCBleHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZSwgc29mdGVuaW5nIHJlZ3VsYXJpc2F0aW9uOyAoQykgY29weSBwZXIgcm91bmQg4oCUIHJlc2V0IM+AX3JlZiB0byB0aGUgY3VycmVudCDPgF/OuCBhdCB0aGUgc3RhcnQgb2YgZWFjaCByb3VuZCwgYWxsb3dpbmcgdGhlIHBvbGljeSB0byBkcmlmdCBmdXJ0aGVyLiBGaXhlZCByZWZlcmVuY2UgaXMgbW9zdCBzdGFibGUgYW5kIG1vc3QgY29tbW9ubHkgdXNlZDsgY29weS1wZXItcm91bmQgcmlza3MgZGVnZW5lcmF0aW9uIHdpdGhvdXQgb3RoZXIgcmVndWxhcmlzYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IGNvcHlcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTVxuXG5kZWYgdXBkYXRlX3JlZmVyZW5jZV9tb2RlbChcbiAgICBvcmlnaW5hbF9yZWY6IEF1dG9Nb2RlbEZvckNhdXNhbExNLFxuICAgIGN1cnJlbnRfcG9saWN5OiBBdXRvTW9kZWxGb3JDYXVzYWxMTSxcbiAgICBzdHJhdGVneTogc3RyID0gXHUwMDI3Zml4ZWRcdTAwMjcsXG4gICAgcG9seWFrX3RhdTogZmxvYXQgPSAwLjAxLFxuKSAtXHUwMDNlIEF1dG9Nb2RlbEZvckNhdXNhbExNOlxuICAgICMgUmV0dXJuIHVwZGF0ZWQgcmVmZXJlbmNlIG1vZGVsIGJhc2VkIG9uIHN0cmF0ZWd5XG4gICAgaWYgc3RyYXRlZ3kgPT0gXHUwMDI3Zml4ZWRcdTAwMjc6XG4gICAgICAgICMgS2VlcCBvcmlnaW5hbCBTRlQgYXMgcmVmZXJlbmNlIHRocm91Z2hvdXQgYWxsIHJvdW5kc1xuICAgICAgICByZXR1cm4gb3JpZ2luYWxfcmVmXG4gICAgZWxpZiBzdHJhdGVneSA9PSBcdTAwMjdlbWFcdTAwMjc6XG4gICAgICAgICMgU2xvd2x5IHRyYWNrIHBvbGljeSB3aXRoIGV4cG9uZW50aWFsIG1vdmluZyBhdmVyYWdlXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgZm9yIHBfcmVmLCBwX3BvbGljeSBpbiB6aXAob3JpZ2luYWxfcmVmLnBhcmFtZXRlcnMoKSwgY3VycmVudF9wb2xpY3kucGFyYW1ldGVycygpKTpcbiAgICAgICAgICAgICAgICBwX3JlZi5kYXRhLm11bF8oMSAtIHBvbHlha190YXUpLmFkZF8ocG9seWFrX3RhdSAqIHBfcG9saWN5LmRhdGEpXG4gICAgICAgIHJldHVybiBvcmlnaW5hbF9yZWZcbiAgICBlbGlmIHN0cmF0ZWd5ID09IFx1MDAyN2NvcHlcdTAwMjc6XG4gICAgICAgICMgUmVzZXQgcmVmZXJlbmNlIHRvIGN1cnJlbnQgcG9saWN5IGVhY2ggcm91bmRcbiAgICAgICAgcmV0dXJuIGNvcHkuZGVlcGNvcHkoY3VycmVudF9wb2xpY3kpXG4gICAgZWxzZTpcbiAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihmXHUwMDI3VW5rbm93biBzdHJhdGVneToge3N0cmF0ZWd5fVx1MDAyNylcblxuc3RyYXRlZ2llcyA9IFtcdTAwMjdmaXhlZFx1MDAyNywgXHUwMDI3ZW1hXHUwMDI3LCBcdTAwMjdjb3B5XHUwMDI3XVxuZWZmZWN0cyA9IFtcbiAgICBcdTAwMjdTdHJvbmcgcmVndWxhcmlzYXRpb24gdG93YXJkIFNGVCBiYXNlbGluZTsgbG93ZXN0IHJpc2sgb2YgZGVnZW5lcmF0aW9uXHUwMDI3LFxuICAgIFx1MDAyN1NvZnRlbmluZyBLTCBwZW5hbHR5IG92ZXIgdHJhaW5pbmc7IG1vZGVyYXRlIHBvbGljeSBkcmlmdCBhbGxvd2VkXHUwMDI3LFxuICAgIFx1MDAyN05vIGFuY2hvcmluZyB0byBTRlQ7IGhpZ2hlc3QgZHJpZnQgcmlzayDigJQgbmVlZHMgb3RoZXIgcmVndWxhcmlzYXRpb25cdTAwMjcsXG5dXG5wcmludChmXHUwMDI3e1wiU3RyYXRlZ3lcIjpcdTAwM2MxMH0gIHtcIkVmZmVjdFwifVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA3MClcbmZvciBzLCBlIGluIHppcChzdHJhdGVnaWVzLCBlZmZlY3RzKTpcbiAgICBwcmludChmXHUwMDI3e3M6XHUwMDNjMTB9ICB7ZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT24tUG9saWN5IHZzIE9mZi1Qb2xpY3kgUGVyZm9ybWFuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVtcGlyaWNhbCByZXN1bHRzIGNvbnNpc3RlbnRseSBzaG93IGl0ZXJhdGl2ZSBEUE8gb3V0cGVyZm9ybWluZyBzdGF0aWMgRFBPLCBlc3BlY2lhbGx5IGFmdGVyIHRoZSBmaXJzdCB0cmFpbmluZyByb3VuZCB3aGVyZSB0aGUgcG9saWN5IGhhcyBhbHJlYWR5IHNoaWZ0ZWQgZnJvbSB0aGUgU0ZUIGJhc2VsaW5lLiBUaGUgcGVyZm9ybWFuY2UgZ2FwIHdpZGVucyBvbiBoYXJkZXIgdGFza3Mgd2hlcmUgdGhlIFNGVCBtb2RlbFx1MDAyN3Mgb3V0cHV0IGRpc3RyaWJ1dGlvbiBpcyBmYXIgZnJvbSB0aGUgb3B0aW1hbC4gT24gQWxwYWNhRXZhbCAyLjAgYmVuY2htYXJrcywgaXRlcmF0aXZlIERQTyB0eXBpY2FsbHkgY2xvc2VzIDUw4oCTNzAlIG9mIHRoZSBnYXAgYmV0d2VlbiBzdGF0aWMgRFBPIGFuZCBQUE8uIFRoZSByZW1haW5pbmcgZ2FwIGNvbWVzIGZyb20gUFBPXHUwMDI3cyBhYmlsaXR5IHRvIGV4cGxvcmUgdGhlIGZ1bGwgcmVzcG9uc2Ugc3BhY2UgcmF0aGVyIHRoYW4ganVzdCBjb21wYXJpbmcgc2FtcGxlcyBmcm9tIHRoZSBjdXJyZW50IHBvbGljeS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBzaW11bGF0ZV93aW5fcmF0ZV90cmFqZWN0b3J5KG5fc3RlcHM9NTAwLCBvbl9wb2xpY3k9VHJ1ZSwgc2VlZD00Mik6XG4gICAgIyBTaW11bGF0ZSB3aW4gcmF0ZSB0cmFqZWN0b3J5IGZvciBvbi1wb2xpY3kgdnMgb2ZmLXBvbGljeSBEUE9cbiAgICBybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoc2VlZClcbiAgICB3aW5fcmF0ZSA9IDAuNTVcbiAgICB0cmFqZWN0b3J5ID0gW11cbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgaWYgb25fcG9saWN5OlxuICAgICAgICAgICAgaW1wcm92ZW1lbnQgPSAwLjAwMDM1ICogKDEgLSB3aW5fcmF0ZSkgKyBybmcubm9ybWFsKDAsIDAuMDAyKVxuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgIyBPZmYtcG9saWN5IGRhdGEgYmVjb21lcyBsZXNzIGluZm9ybWF0aXZlIGFzIHBvbGljeSBpbXByb3Zlc1xuICAgICAgICAgICAgZGVjYXkgPSBtYXgoMCwgMSAtIHN0ZXAgLyAyNTApXG4gICAgICAgICAgICBpbXByb3ZlbWVudCA9IDAuMDAwMTIgKiAoMSAtIHdpbl9yYXRlKSAqIGRlY2F5ICsgcm5nLm5vcm1hbCgwLCAwLjAwMylcbiAgICAgICAgd2luX3JhdGUgPSBmbG9hdChucC5jbGlwKHdpbl9yYXRlICsgaW1wcm92ZW1lbnQsIDAuNSwgMC45NSkpXG4gICAgICAgIHRyYWplY3RvcnkuYXBwZW5kKHdpbl9yYXRlKVxuICAgIHJldHVybiB0cmFqZWN0b3J5XG5cbm9uX3RyYWogPSBzaW11bGF0ZV93aW5fcmF0ZV90cmFqZWN0b3J5KDUwMCwgb25fcG9saWN5PVRydWUpXG5vZmZfdHJhaiA9IHNpbXVsYXRlX3dpbl9yYXRlX3RyYWplY3RvcnkoNTAwLCBvbl9wb2xpY3k9RmFsc2UpXG5jaGVja3BvaW50cyA9IFswLCA5OSwgMjQ5LCA0OTldXG5wcmludChmXHUwMDI3e1wiU3RlcFwiOlx1MDAzZTZ9ICB7XCJPbi1Qb2xpY3kgV1JcIjpcdTAwM2UxNH0gIHtcIk9mZi1Qb2xpY3kgV1JcIjpcdTAwM2UxNX0gIHtcIkRlbHRhXCI6XHUwMDNlOH1cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNTIpXG5mb3Igc3RlcCBpbiBjaGVja3BvaW50czpcbiAgICBkID0gb25fdHJhaltzdGVwXSAtIG9mZl90cmFqW3N0ZXBdXG4gICAgc2lnbiA9IFx1MDAyNytcdTAwMjcgaWYgZCBcdTAwM2U9IDAgZWxzZSBcdTAwMjdcdTAwMjdcbiAgICBwcmludChmXHUwMDI3e3N0ZXArMTpcdTAwM2U2fSAge29uX3RyYWpbc3RlcF06XHUwMDNlMTQuNGZ9ICB7b2ZmX3RyYWpbc3RlcF06XHUwMDNlMTUuNGZ9ICB7c2lnbn17ZDpcdTAwM2U3LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdGaW5hbDogb24tcG9saWN5PXtvbl90cmFqWy0xXTouNGZ9LCBvZmYtcG9saWN5PXtvZmZfdHJhalstMV06LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPbmxpbmUgRFBPIFZhcmlhbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZXZlcmFsIHZhcmlhbnRzIGV4dGVuZCBpdGVyYXRpdmUgRFBPLiBTZWxmLVBsYXkgRmluZS1UdW5pbmcgKFNQSU4sIENoZW4gZXQgYWwuIDIwMjQpIHVzZXMgdGhlIGN1cnJlbnQgbW9kZWwgdnMgdGhlIHByZXZpb3VzLXJvdW5kIG1vZGVsIGZvciBzZWxmLXBsYXk6IHRoZSBjdXJyZW50IG1vZGVsIGdlbmVyYXRlcyBjaG9zZW4gcmVzcG9uc2VzLCB0aGUgcHJldmlvdXMgbW9kZWwgZ2VuZXJhdGVzIHJlamVjdGVkIHJlc3BvbnNlcy4gU1BQTyAoU2VsZi1QbGF5IFByZWZlcmVuY2UgT3B0aW1pemF0aW9uKSByZWZvcm11bGF0ZXMgcHJlZmVyZW5jZSBvcHRpbWl6YXRpb24gYXMgYSB0d28tcGxheWVyIGdhbWUuIERpcmVjdCBOYXNoIE9wdGltaXphdGlvbiAoRE5PKSB1c2VzIGdhbWUtdGhlb3JldGljIE5hc2ggZXF1aWxpYnJpYSBhcyB0aGUgb3B0aW1pemF0aW9uIHRhcmdldC4gT25saW5lIERQTyAoR3VvIGV0IGFsLiAyMDI0KSBwcm92aWRlcyBhIHVuaWZpZWQgZnJhbWV3b3JrIHdpdGggdGhlb3JldGljYWwgY29udmVyZ2VuY2UgZ3VhcmFudGVlcy4gVGhlc2UgdmFyaWFudHMgZGlmZmVyIGluIGhvdyB0aGV5IGdlbmVyYXRlIHBhaXJzIGFuZCB3aGV0aGVyIHRoZXkgdXNlIGEgcmV3YXJkIG1vZGVsIG9yIHJlbHkgb24gc2VsZi1wbGF5IGR5bmFtaWNzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJEYXRhIFNvdXJjZSIsIk9ubGluZSIsIlN0YWJpbGl0eSIsIlBlcmZvcm1hbmNlIiwiQ29tcGxleGl0eSJdLCJyb3dzIjpbWyJTdGF0aWMgRFBPIiwiRml4ZWQgaHVtYW4gcHJlZmVyZW5jZSBkYXRhc2V0IGZyb20gU0ZUIG1vZGVsIiwiTm8iLCJIaWdoIiwiQmFzZWxpbmUiLCJMb3cg4oCUIG9mZmxpbmUgU0ZULWxpa2UgdHJhaW5pbmciXSxbIkl0ZXJhdGl2ZSBEUE8iLCJDdXJyZW50IHBvbGljeSArIFJNIHNjb3JpbmcgZWFjaCByb3VuZCIsIlllcyIsIkhpZ2giLCJDbG9zZXMgNTAtNzAlIGdhcCB2cyBQUE8iLCJNZWRpdW0g4oCUIG5lZWRzIFJNICsgZ2VuZXJhdGlvbiJdLFsiU1BJTiIsIkN1cnJlbnQgbW9kZWwgKGNob3NlbikgdnMgcHJldmlvdXMgbW9kZWwgKHJlamVjdGVkKSIsIlllcyIsIk1lZGl1bSIsIk1hdGNoZXMgaXRlcmF0aXZlIERQTyBvbiBtYW55IHRhc2tzIiwiTG93IOKAlCBubyBleHRlcm5hbCBSTSBuZWVkZWQiXSxbIk9ubGluZSBEUE8iLCJDb250aW51b3VzIG9uLXBvbGljeSBnZW5lcmF0aW9uICsgUk0iLCJZZXMgKGNvbnRpbnVvdXMpIiwiTWVkaXVtIiwiTmVhciBQUE8gcGVyZm9ybWFuY2UiLCJIaWdoIOKAlCByZXF1aXJlcyBzdGFibGUgb25saW5lIFJNIl0sWyJQUE8iLCJPbmxpbmUgcm9sbG91dHMgd2l0aCB2YWx1ZSBmdW5jdGlvbiArIFJNIiwiWWVzIChjb250aW51b3VzKSIsIkxvdyIsIkJlc3QgYWxpZ25tZW50IHF1YWxpdHkiLCJIaWdoIOKAlCBSTCBpbmZyYXN0cnVjdHVyZSByZXF1aXJlZCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW1wbGVtZW50YXRpb24gQ29uc2lkZXJhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1lbW9yeSByZXF1aXJlbWVudHMgYXJlIHRoZSBtYWluIHByYWN0aWNhbCBjb25zdHJhaW50OiBpdGVyYXRpdmUgRFBPIG5lZWRzIHRoZSBwb2xpY3ksIHRoZSBmcm96ZW4gcmVmZXJlbmNlIG1vZGVsLCBhbmQgdGhlIHJld2FyZCBtb2RlbCBsb2FkZWQgc2ltdWx0YW5lb3VzbHkuIFdpdGggYSA3QiBwb2xpY3kgYW5kIDdCIHJlZmVyZW5jZSwgdGhpcyByZXF1aXJlcyB+MjggR0IgZm9yIEJGMTYgd2VpZ2h0cyBhbG9uZSwgcGx1cyBhY3RpdmF0aW9ucy4gTG9SQSBmb3IgdGhlIHBvbGljeSAobm90IHRoZSByZWZlcmVuY2UpIHJlZHVjZXMgbWVtb3J5IHNpZ25pZmljYW50bHkgd2hpbGUgbWFpbnRhaW5pbmcgZmluZS10dW5pbmcgcXVhbGl0eS4gVGhlIGdlbmVyYXRpb24gYW5kIERQTyB0cmFpbmluZyBzdGVwcyBjYW4gYmUgYmF0Y2hlZCB0byBtYXhpbWl6ZSBHUFUgdXRpbGl6YXRpb24g4oCUIGdlbmVyYXRlIHBhaXJzIGZvciBhbGwgcHJvbXB0cywgdGhlbiBydW4gb25lIERQTyBlcG9jaCwgcmF0aGVyIHRoYW4gYWx0ZXJuYXRpbmcgcGVyLWJhdGNoLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIExvUkEgZm9yIHRoZSBwb2xpY3kgZHVyaW5nIGl0ZXJhdGl2ZSBEUE8g4oCUIGtlZXBzIHJlZmVyZW5jZSBtb2RlbCBpbiBmdWxsIHByZWNpc2lvbiB3aGlsZSB0aGUgcG9saWN5IGFkYXB0ZXIgdHJhaW5zIGVmZmljaWVudGx5LiIsIlJlZ2VuZXJhdGUgcHJlZmVyZW5jZSBwYWlycyBldmVyeSBlcG9jaCByYXRoZXIgdGhhbiBldmVyeSBiYXRjaCDigJQgcmVkdWNlcyBpbmZlcmVuY2Ugb3ZlcmhlYWQgd2hpbGUgc3RheWluZyBlZmZlY3RpdmVseSBvbi1wb2xpY3kuIiwiTW9uaXRvciBjaG9zZW5fcmV3YXJkcyBhbmQgcmVqZWN0ZWRfcmV3YXJkcyBzZXBhcmF0ZWx5IOKAlCBpZiBib3RoIGluY3JlYXNlIHVuaWZvcm1seSwgdGhlIHBvbGljeSBpcyByZXdhcmQtaGFja2luZyByYXRoZXIgdGhhbiBnZW51aW5lbHkgaW1wcm92aW5nLiIsIlVzZSBtaW5fbWFyZ2luIGZpbHRlcmluZyAodGhyZXNob2xkIDAuMeKAkzAuMyBvbiBub3JtYWxpemVkIHJld2FyZCkgdG8gcmVtb3ZlIGFtYmlndW91cyBwYWlycyB0aGF0IGFkZCBub2lzZS4iLCJTUElOIChzZWxmLXBsYXkgd2l0aG91dCBSTSkgaXMgYSBnb29kIGZhbGxiYWNrIHdoZW4gYSByZWxpYWJsZSByZXdhcmQgbW9kZWwgaXMgdW5hdmFpbGFibGUg4oCUIHVzZXMgTE0gcGVycGxleGl0eSBhcyB0aGUgcHJlZmVyZW5jZSBzaWduYWwuIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSXRlcmF0aXZlIERQTyB2cyBQUE8iLCJjb250ZW50IjoiSXRlcmF0aXZlIERQTyBjbG9zZXMgbW9zdCBvZiB0aGUgcGVyZm9ybWFuY2UgZ2FwIGJldHdlZW4gRFBPIGFuZCBQUE8gYXQgbG93ZXIgY29tcGxleGl0eSDigJQgb24tcG9saWN5IHByZWZlcmVuY2UgZGF0YSBmcm9tIHRoZSBjdXJyZW50IG1vZGVsXHUwMDI3cyBkaXN0cmlidXRpb24gaXMgc2lnbmlmaWNhbnRseSBtb3JlIGluZm9ybWF0aXZlIHRoYW4gc3RhdGljIHByZWZlcmVuY2UgZGF0YSBmcm9tIHRoZSBvcmlnaW5hbCBTRlQgbW9kZWwuIFRoZSByZW1haW5pbmcgUFBPIGFkdmFudGFnZSBjb21lcyBmcm9tIGl0cyBhYmlsaXR5IHRvIGV4cGxvcmUgdGhlIGZ1bGwgcmVzcG9uc2Ugc3BhY2UgcmF0aGVyIHRoYW4gY29tcGFyaW5nIHBvbGljeSBzYW1wbGVzLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Iterative DPO — Online Preference Learning with Self-Generated Pairs

Direct Preference Optimization (DPO) is trained on a fixed dataset of (prompt, chosen, rejected) triples collected offline — typically from human labelers comparing outputs of the original SFT model. This static dataset has a critical limitation: as the policy improves during training, the preference pairs become increasingly off-policy relative to the current model distribution. Iterative DPO (also called online DPO) addresses this by periodically regenerating preference pairs from the current policy, ensuring training data stays on-policy and remains informative throughout training.

## Why Static DPO Falls Short

The DPO loss function implicitly assumes that the chosen and rejected responses are drawn from a distribution close to the reference model π_ref. When the policy π_θ drifts far from π_ref during training, the preference data becomes stale — the (chosen, rejected) pairs no longer represent the outputs the current policy would generate. This is the off-policy problem: the model is being trained to prefer response A over response B, but A and B were generated by a much weaker model, so the lesson is trivial for the now-stronger policy. On-policy preference data from the current π_θ provides a much harder and more informative training signal.

## The Iterative DPO Algorithm

Iterative DPO runs in rounds: (1) sample K completions per prompt from the current policy π_θ; (2) score them with a reward model or human rater; (3) form (chosen, rejected) pairs from highest- and lowest-scoring completions; (4) run a DPO update step with the new on-policy pairs; (5) repeat. The reference model π_ref can be kept fixed (original SFT) for stability or updated periodically. Key hyperparameters: how often to regenerate pairs (every N steps or every epoch), how many samples per prompt, and the DPO beta (KL penalty weight).

```python
import torch
from dataclasses import dataclass
from typing import Callable

@dataclass
class IterativeDPOConfig:
    n_rounds: int = 3
    samples_per_prompt: int = 2
    dpo_beta: float = 0.1
    dpo_epochs_per_round: int = 1
    lr: float = 5e-7
    ref_update_strategy: str = 'fixed'  # 'fixed', 'ema', or 'copy'

def iterative_dpo_round(
    policy,
    ref_model,
    tokenizer,
    reward_model,
    prompts: list,
    config: IterativeDPOConfig,
    round_idx: int,
    dpo_train_fn: Callable,
) -> dict:
    # One round: generate on-policy pairs, score, run DPO update
    print(f'Round {round_idx+1}: sampling {config.samples_per_prompt} completions/prompt from current policy')
    preference_dataset = generate_preference_pairs(
        policy, tokenizer, reward_model, prompts, config.samples_per_prompt
    )
    n_pairs = len(preference_dataset['chosen'])
    print(f'Round {round_idx+1}: DPO update on {n_pairs} on-policy pairs (beta={config.dpo_beta})')
    dpo_train_fn(policy, ref_model, preference_dataset, config)
    return {'round': round_idx + 1, 'n_pairs': n_pairs}

config = IterativeDPOConfig(n_rounds=3, samples_per_prompt=2, dpo_beta=0.1)
print('Iterative DPO: on-policy preference data from current pi_theta at each round')
print('Key: pairs generated by current policy are harder and more informative than SFT pairs')
```

## On-Policy Preference Pair Generation

At each round, two completions are sampled from the current policy per prompt. The reward model scores both and determines which is preferred. Using only 2 samples is the simplest setting — the margin between best and worst reflects the policy's current uncertainty. Using more samples (4–8) and taking the highest and lowest score creates larger reward margins in the preference pairs, providing a cleaner learning signal. Filtering out pairs where the reward margin is below a threshold (margin filtering) removes ambiguous pairs that add noise to training.

```python
import torch
from datasets import Dataset

def generate_preference_pairs(
    policy,
    tokenizer,
    reward_model,
    prompts: list,
    n_samples: int = 2,
    temperature: float = 0.8,
    min_margin: float = 0.1,
) -> Dataset:
    # Sample completions from current policy, use RM to determine preference
    chosen_list, rejected_list, prompt_list = [], [], []
    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors='pt').to(policy.device)
        completions = []
        for _ in range(n_samples):
            with torch.no_grad():
                output = policy.generate(
                    **inputs,
                    max_new_tokens=128,
                    do_sample=True,
                    temperature=temperature,
                    pad_token_id=tokenizer.eos_token_id,
                )
            gen = output[0][inputs['input_ids'].shape[1]:]
            completions.append(tokenizer.decode(gen, skip_special_tokens=True))
        scores = []
        for c in completions:
            enc = tokenizer(prompt + c, return_tensors='pt', truncation=True).to(reward_model.device)
            with torch.no_grad():
                scores.append(reward_model(**enc).logits.squeeze().item())
        best_idx = int(torch.tensor(scores).argmax())
        worst_idx = int(torch.tensor(scores).argmin())
        margin = scores[best_idx] - scores[worst_idx]
        if margin >= min_margin:
            chosen_list.append(completions[best_idx])
            rejected_list.append(completions[worst_idx])
            prompt_list.append(prompt)
    return Dataset.from_dict({'prompt': prompt_list, 'chosen': chosen_list, 'rejected': rejected_list})

print('On-policy pairs: both chosen and rejected come from current pi_theta')
print('Margin filtering (min_margin=0.1) removes ambiguous pairs from training')
```

## Reference Model Update Strategies

The reference model π_ref determines the KL penalty target — keeping π_θ from deviating too far. Three strategies exist: (A) fixed reference — keep the original SFT model as π_ref throughout all rounds, providing strong regularisation toward the SFT baseline; (B) EMA update — slowly track the policy with exponential moving average, softening regularisation; (C) copy per round — reset π_ref to the current π_θ at the start of each round, allowing the policy to drift further. Fixed reference is most stable and most commonly used; copy-per-round risks degeneration without other regularisation.

```python
import torch
import copy
from transformers import AutoModelForCausalLM

def update_reference_model(
    original_ref: AutoModelForCausalLM,
    current_policy: AutoModelForCausalLM,
    strategy: str = 'fixed',
    polyak_tau: float = 0.01,
) -> AutoModelForCausalLM:
    # Return updated reference model based on strategy
    if strategy == 'fixed':
        # Keep original SFT as reference throughout all rounds
        return original_ref
    elif strategy == 'ema':
        # Slowly track policy with exponential moving average
        with torch.no_grad():
            for p_ref, p_policy in zip(original_ref.parameters(), current_policy.parameters()):
                p_ref.data.mul_(1 - polyak_tau).add_(polyak_tau * p_policy.data)
        return original_ref
    elif strategy == 'copy':
        # Reset reference to current policy each round
        return copy.deepcopy(current_policy)
    else:
        raise ValueError(f'Unknown strategy: {strategy}')

strategies = ['fixed', 'ema', 'copy']
effects = [
    'Strong regularisation toward SFT baseline; lowest risk of degeneration',
    'Softening KL penalty over training; moderate policy drift allowed',
    'No anchoring to SFT; highest drift risk — needs other regularisation',
]
print(f'{"Strategy":<10}  {"Effect"}')
print('-' * 70)
for s, e in zip(strategies, effects):
    print(f'{s:<10}  {e}')
```

## On-Policy vs Off-Policy Performance

Empirical results consistently show iterative DPO outperforming static DPO, especially after the first training round where the policy has already shifted from the SFT baseline. The performance gap widens on harder tasks where the SFT model's output distribution is far from the optimal. On AlpacaEval 2.0 benchmarks, iterative DPO typically closes 50–70% of the gap between static DPO and PPO. The remaining gap comes from PPO's ability to explore the full response space rather than just comparing samples from the current policy.

```python
import numpy as np

def simulate_win_rate_trajectory(n_steps=500, on_policy=True, seed=42):
    # Simulate win rate trajectory for on-policy vs off-policy DPO
    rng = np.random.default_rng(seed)
    win_rate = 0.55
    trajectory = []
    for step in range(n_steps):
        if on_policy:
            improvement = 0.00035 * (1 - win_rate) + rng.normal(0, 0.002)
        else:
            # Off-policy data becomes less informative as policy improves
            decay = max(0, 1 - step / 250)
            improvement = 0.00012 * (1 - win_rate) * decay + rng.normal(0, 0.003)
        win_rate = float(np.clip(win_rate + improvement, 0.5, 0.95))
        trajectory.append(win_rate)
    return trajectory

on_traj = simulate_win_rate_trajectory(500, on_policy=True)
off_traj = simulate_win_rate_trajectory(500, on_policy=False)
checkpoints = [0, 99, 249, 499]
print(f'{"Step":>6}  {"On-Policy WR":>14}  {"Off-Policy WR":>15}  {"Delta":>8}')
print('-' * 52)
for step in checkpoints:
    d = on_traj[step] - off_traj[step]
    sign = '+' if d >= 0 else ''
    print(f'{step+1:>6}  {on_traj[step]:>14.4f}  {off_traj[step]:>15.4f}  {sign}{d:>7.4f}')
print(f'Final: on-policy={on_traj[-1]:.4f}, off-policy={off_traj[-1]:.4f}')
```

## Online DPO Variants

Several variants extend iterative DPO. Self-Play Fine-Tuning (SPIN, Chen et al. 2024) uses the current model vs the previous-round model for self-play: the current model generates chosen responses, the previous model generates rejected responses. SPPO (Self-Play Preference Optimization) reformulates preference optimization as a two-player game. Direct Nash Optimization (DNO) uses game-theoretic Nash equilibria as the optimization target. Online DPO (Guo et al. 2024) provides a unified framework with theoretical convergence guarantees. These variants differ in how they generate pairs and whether they use a reward model or rely on self-play dynamics.

| Method | Data Source | Online | Stability | Performance | Complexity |
| --- | --- | --- | --- | --- | --- |
| Static DPO | Fixed human preference dataset from SFT model | No | High | Baseline | Low — offline SFT-like training |
| Iterative DPO | Current policy + RM scoring each round | Yes | High | Closes 50-70% gap vs PPO | Medium — needs RM + generation |
| SPIN | Current model (chosen) vs previous model (rejected) | Yes | Medium | Matches iterative DPO on many tasks | Low — no external RM needed |
| Online DPO | Continuous on-policy generation + RM | Yes (continuous) | Medium | Near PPO performance | High — requires stable online RM |
| PPO | Online rollouts with value function + RM | Yes (continuous) | Low | Best alignment quality | High — RL infrastructure required |

## Implementation Considerations

Memory requirements are the main practical constraint: iterative DPO needs the policy, the frozen reference model, and the reward model loaded simultaneously. With a 7B policy and 7B reference, this requires ~28 GB for BF16 weights alone, plus activations. LoRA for the policy (not the reference) reduces memory significantly while maintaining fine-tuning quality. The generation and DPO training steps can be batched to maximize GPU utilization — generate pairs for all prompts, then run one DPO epoch, rather than alternating per-batch.

- Use LoRA for the policy during iterative DPO — keeps reference model in full precision while the policy adapter trains efficiently.
- Regenerate preference pairs every epoch rather than every batch — reduces inference overhead while staying effectively on-policy.
- Monitor chosen_rewards and rejected_rewards separately — if both increase uniformly, the policy is reward-hacking rather than genuinely improving.
- Use min_margin filtering (threshold 0.1–0.3 on normalized reward) to remove ambiguous pairs that add noise.
- SPIN (self-play without RM) is a good fallback when a reliable reward model is unavailable — uses LM perplexity as the preference signal.

> **Iterative DPO vs PPO**: Iterative DPO closes most of the performance gap between DPO and PPO at lower complexity — on-policy preference data from the current model's distribution is significantly more informative than static preference data from the original SFT model. The remaining PPO advantage comes from its ability to explore the full response space rather than comparing policy samples.

---

