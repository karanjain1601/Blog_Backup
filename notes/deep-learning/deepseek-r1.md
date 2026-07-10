---
title: "DeepSeek-R1: Reinforcement Learning for Reasoning"
slug: "deepseek-r1"
description: "How DeepSeek-R1 trains long chain-of-thought reasoning via RL — covering GRPO, cold-start SFT, the RL training pipeline, and distillation to smaller models."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVlcFNlZWstUjEgYWNoaWV2ZXMgbzEtbGV2ZWwgcGVyZm9ybWFuY2Ugb24gbWF0aCBhbmQgY29kaW5nIGJlbmNobWFya3MgdXNpbmcgcmVpbmZvcmNlbWVudCBsZWFybmluZyB3aXRoIEdSUE8sIHdpdGhvdXQgcmVseWluZyBvbiBodW1hbi1sYWJlbGVkIGNoYWluLW9mLXRob3VnaHQgZGF0YS4gUjEtWmVybyBkZW1vbnN0cmF0ZXMgdGhhdCBjb21wbGV4IHJlYXNvbmluZyBiZWhhdmlvcnMg4oCUIGluY2x1ZGluZyBzZWxmLXZlcmlmaWNhdGlvbiBhbmQgcmVmbGVjdGlvbiDigJQgY2FuIGVtZXJnZSBwdXJlbHkgZnJvbSByZXdhcmQgc2lnbmFscywgY2hhbGxlbmdpbmcgdGhlIGFzc3VtcHRpb24gdGhhdCBzdXBlcnZpc2VkIENvVCBkYXRhIGlzIG5lY2Vzc2FyeS4ifSx7InR5cGUiOiJoZWFkaW5nIiwiY29udGVudCI6IkdSUE86IEdyb3VwIFJlbGF0aXZlIFBvbGljeSBPcHRpbWl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdSUE8gcmVwbGFjZXMgdGhlIGFjdG9yLWNyaXRpYyBzZXR1cCB1c2VkIGluIFBQTyB3aXRoIGEgZ3JvdXAtYmFzZWQgYWR2YW50YWdlIGVzdGltYXRpb24uIEZvciBlYWNoIHByb21wdCwgSyByZXNwb25zZXMgYXJlIHNhbXBsZWQgZnJvbSB0aGUgY3VycmVudCBwb2xpY3k7IGVhY2ggcmVjZWl2ZXMgYSBzY2FsYXIgcmV3YXJkLiBUaGUgYWR2YW50YWdlIGZvciBlYWNoIHJlc3BvbnNlIGlzIGNvbXB1dGVkIGJ5IHN1YnRyYWN0aW5nIHRoZSBncm91cCBtZWFuIGFuZCBkaXZpZGluZyBieSB0aGUgZ3JvdXAgc3RhbmRhcmQgZGV2aWF0aW9uIOKAlCBlbGltaW5hdGluZyB0aGUgbmVlZCBmb3IgYSBzZXBhcmF0ZSBjcml0aWMgb3IgdmFsdWUgbW9kZWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgZ3Jwb19sb3NzKHBvbGljeSwgcmVmX3BvbGljeSwgcHJvbXB0cywgSz04LCBiZXRhPTAuMDQsIGVwcz0wLjIpOlxuICAgIGxvc3NlcyA9IFtdXG4gICAgZm9yIHByb21wdCBpbiBwcm9tcHRzOlxuICAgICAgICBjb21wbGV0aW9ucyA9IHBvbGljeS5zYW1wbGUocHJvbXB0LCBuPUssIHRlbXBlcmF0dXJlPTAuOClcbiAgICAgICAgciA9IHRvcmNoLnRlbnNvcihbcmV3YXJkX2ZuKHByb21wdCwgYykgZm9yIGMgaW4gY29tcGxldGlvbnNdKVxuICAgICAgICBhZHYgPSAociAtIHIubWVhbigpKSAvIChyLnN0ZCgpICsgMWUtOClcbiAgICAgICAgbG9ncCA9IHBvbGljeS5sb2dfcHJvYihjb21wbGV0aW9ucylcbiAgICAgICAgcmVmX2xvZ3AgPSByZWZfcG9saWN5LmxvZ19wcm9iKGNvbXBsZXRpb25zKVxuICAgICAgICByYXRpbyA9IChsb2dwIC0gcmVmX2xvZ3ApLmV4cCgpXG4gICAgICAgIGNsaXBwZWQgPSB0b3JjaC5jbGFtcChyYXRpbywgMSAtIGVwcywgMSArIGVwcylcbiAgICAgICAgcGcgPSAtdG9yY2gubWluKHJhdGlvICogYWR2LCBjbGlwcGVkICogYWR2KS5tZWFuKClcbiAgICAgICAgbG9zc2VzLmFwcGVuZChwZyArIGJldGEgKiAobG9ncCAtIHJlZl9sb2dwKS5tZWFuKCkpXG4gICAgcmV0dXJuIHRvcmNoLnN0YWNrKGxvc3NlcykubWVhbigpIn0seyJ0eXBlIjoiaGVhZGluZyIsImNvbnRlbnQiOiJSZXdhcmQgRnVuY3Rpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZWVwU2Vlay1SMSB1c2VzIHR3byBydWxlLWJhc2VkIHJld2FyZHM6IGEgY29ycmVjdG5lc3MgcmV3YXJkIHRoYXQgY2hlY2tzIHRoZSBmaW5hbCBhbnN3ZXIgYWdhaW5zdCBhIGdyb3VuZC10cnV0aCAodXNpbmcgU3ltUHkgZm9yIHN5bWJvbGljIG1hdGggZXF1YWxpdHkgYW5kIHVuaXQgdGVzdHMgZm9yIGNvZGUpLCBhbmQgYSBmb3JtYXQgcmV3YXJkIHRoYXQgZW5mb3JjZXMgdGhlIG1vZGVsIHByb2R1Y2VzIFx1MDAzY3RoaW5rXHUwMDNlLi4uXHUwMDNjL3RoaW5rXHUwMDNlIGFuZCBcdTAwM2NhbnN3ZXJcdTAwM2UuLi5cdTAwM2MvYW5zd2VyXHUwMDNlIHRhZ3MuIE5vIGxlYXJuZWQgcmV3YXJkIG1vZGVsIGlzIG5lZWRlZCwga2VlcGluZyB0aGUgc2lnbmFsIGNsZWFuIGFuZCB2ZXJpZmlhYmxlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmZyb20gc3ltcHkgaW1wb3J0IHNpbXBsaWZ5LCBzeW1waWZ5LCBTeW1waWZ5RXJyb3JcblxuZGVmIHJld2FyZF9mbihwcm9tcHQsIGNvbXBsZXRpb24sIGV4cGVjdGVkKTpcbiAgICBoYXNfdGhpbmsgPSBib29sKHJlLnNlYXJjaChyXHUwMDI3XHUwMDNjdGhpbmtcdTAwM2UuK1x1MDAzYy90aGlua1x1MDAzZVx1MDAyNywgY29tcGxldGlvbiwgcmUuUykpXG4gICAgZm10X2JvbnVzID0gMC4xIGlmIGhhc190aGluayBlbHNlIDAuMFxuICAgIG0gPSByZS5zZWFyY2goclx1MDAyN1x1MDAzY2Fuc3dlclx1MDAzZSguKj8pXHUwMDNjL2Fuc3dlclx1MDAzZVx1MDAyNywgY29tcGxldGlvbiwgcmUuUylcbiAgICBpZiBtIGlzIE5vbmU6XG4gICAgICAgIHJldHVybiBmbXRfYm9udXMgKiAwLjVcbiAgICBwcmVkaWN0ZWQgPSBtLmdyb3VwKDEpLnN0cmlwKClcbiAgICB0cnk6XG4gICAgICAgIGlmIHNpbXBsaWZ5KHN5bXBpZnkocHJlZGljdGVkKSAtIHN5bXBpZnkoZXhwZWN0ZWQpKSA9PSAwOlxuICAgICAgICAgICAgcmV0dXJuIDEuMCArIGZtdF9ib251c1xuICAgIGV4Y2VwdCBTeW1waWZ5RXJyb3I6XG4gICAgICAgIHBhc3NcbiAgICByZXR1cm4gZm10X2JvbnVzIGlmIHByZWRpY3RlZCAhPSBzdHIoZXhwZWN0ZWQpIGVsc2UgMS4wICsgZm10X2JvbnVzIn0seyJ0eXBlIjoiaGVhZGluZyIsImNvbnRlbnQiOiJDb2xkLVN0YXJ0IFByb2JsZW0gYW5kIFNGVCBJbml0aWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUjEtWmVybyAocHVyZSBSTCBmcm9tIGJhc2UpIHByb2R1Y2VzIGVtZXJnZW50IHJlYXNvbmluZyBidXQgc3VmZmVycyBmcm9tIGxhbmd1YWdlIG1peGluZyBhbmQgaW5jb25zaXN0ZW50IG91dHB1dCBmb3JtYXR0aW5nLiBEZWVwU2Vlay1SMSBhZGRyZXNzZXMgdGhpcyB3aXRoIGEgY29sZC1zdGFydCBwaGFzZTogYSBzbWFsbCBzZXQgb2YgaHVtYW4tY3VyYXRlZCBsb25nLUNvVCBleGFtcGxlcyBpbiB0aGUgZGVzaXJlZCBmb3JtYXQgYXJlIHVzZWQgdG8gZmluZS10dW5lIHRoZSBiYXNlIG1vZGVsIGJlZm9yZSBSTCBiZWdpbnMsIGdpdmluZyB0aGUgcG9saWN5IGEgd2VsbC1zdHJ1Y3R1cmVkIHN0YXJ0aW5nIHBvaW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsRm9yQ2F1c2FsTE0sIEF1dG9Ub2tlbml6ZXIsIFRyYWluZXIsIFRyYWluaW5nQXJndW1lbnRzXG5cbmRlZiBjb2xkX3N0YXJ0X3NmdChtb2RlbF9uYW1lLCBzZnRfZGF0YXNldF9wYXRoLCBvdXRwdXRfZGlyKTpcbiAgICBtb2RlbCA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgIHRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG4gICAgZGF0YXNldCA9IGxvYWRfY290X2RhdGFzZXQoc2Z0X2RhdGFzZXRfcGF0aCkgICMgXHUwMDNjdGhpbmtcdTAwM2UuLi5cdTAwM2MvdGhpbmtcdTAwM2VcdTAwM2NhbnN3ZXJcdTAwM2UuLi5cdTAwM2MvYW5zd2VyXHUwMDNlXG4gICAgYXJncyA9IFRyYWluaW5nQXJndW1lbnRzKFxuICAgICAgICBvdXRwdXRfZGlyPW91dHB1dF9kaXIsIG51bV90cmFpbl9lcG9jaHM9MSxcbiAgICAgICAgcGVyX2RldmljZV90cmFpbl9iYXRjaF9zaXplPTQsIGxlYXJuaW5nX3JhdGU9MWUtNSxcbiAgICAgICAgbHJfc2NoZWR1bGVyX3R5cGU9XCJjb3NpbmVcIiwgd2FybXVwX3JhdGlvPTAuMDMsXG4gICAgKVxuICAgIHRyYWluZXIgPSBUcmFpbmVyKG1vZGVsPW1vZGVsLCBhcmdzPWFyZ3MsXG4gICAgICAgICAgICAgICAgICAgICAgdHJhaW5fZGF0YXNldD1kYXRhc2V0LCB0b2tlbml6ZXI9dG9rZW5pemVyKVxuICAgIHRyYWluZXIudHJhaW4oKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJjb250ZW50IjoiUkwgVHJhaW5pbmcgUGlwZWxpbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBSTCBsb29wIHJlcGVhdGVkbHkgc2FtcGxlcyBjb21wbGV0aW9ucyBmcm9tIHRoZSBjdXJyZW50IHBvbGljeSwgc2NvcmVzIHRoZW0gd2l0aCB0aGUgcmV3YXJkIGZ1bmN0aW9uLCBjb21wdXRlcyBHUlBPIGFkdmFudGFnZXMsIGFuZCB1cGRhdGVzIHBvbGljeSB3ZWlnaHRzLiBUcmFpbmluZyBydW5zIGZvciB0aG91c2FuZHMgb2Ygc3RlcHMgd2l0aCBhIEtMLWRpdmVyZ2VuY2UgcGVuYWx0eSBhZ2FpbnN0IGEgZnJvemVuIHJlZmVyZW5jZSBwb2xpY3kgdG8gcHJldmVudCB0aGUgbW9kZWwgZnJvbSBkcmlmdGluZyB0b28gZmFyIGZyb20gdGhlIHByZS10cmFpbmVkIGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFmdGVyIFJMIGNvbnZlcmdlbmNlLCBhIHNlY29uZCBTRlQgcGFzcyBpcyBhcHBsaWVkIHVzaW5nIHJlamVjdGlvbi1zYW1wbGVkIHNvbHV0aW9ucyBmcm9tIHRoZSBSTCBtb2RlbCBwbHVzIHN1cGVydmlzZWQgZGF0YSBmb3IgZ2VuZXJhbCB0YXNrcy4gVGhpcyByb3VuZCByZXN0b3JlcyBoZWxwZnVsbmVzcyBvbiBub24tcmVhc29uaW5nIHRhc2tzLCByZWR1Y2VzIHJlcGV0aXRpb24gYXJ0aWZhY3RzIGZyb20gUkwgdHJhaW5pbmcsIGFuZCBjaGF0LWFsaWducyB0aGUgZmluYWwgbW9kZWwgd2hpbGUgcHJlc2VydmluZyB0aGUgc3Ryb25nIHJlYXNvbmluZyBjYXBhYmlsaXR5IGdhaW5lZCB0aHJvdWdoIEdSUE8uIn0seyJ0eXBlIjoiaGVhZGluZyIsImNvbnRlbnQiOiJEaXN0aWxsYXRpb24gdG8gU21hbGxlciBNb2RlbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJhdGhlciB0aGFuIHJ1bm5pbmcgZXhwZW5zaXZlIFJMIG9uIHNtYWxsZXIgbW9kZWxzLCBEZWVwU2VlayBkaXN0aWxscyByZWFzb25pbmcgYnkgZ2VuZXJhdGluZyBsYXJnZSBxdWFudGl0aWVzIG9mIGxvbmctQ29UIHNvbHV0aW9uIHRyYWNlcyBmcm9tIHRoZSBSMS02NzFCIHRlYWNoZXIsIHRoZW4gZmluZS10dW5pbmcgYSBzbWFsbGVyIHN0dWRlbnQgKDdCIG9yIDMyQikgb24gdGhvc2UgdHJhY2VzIHVzaW5nIHN0YW5kYXJkIHN1cGVydmlzZWQgbGVhcm5pbmcuIFRoaXMgaXMgZmFyIGNoZWFwZXIgdGhhbiBSTCB3aGlsZSBhY2hpZXZpbmcgc3VycHJpc2luZ2x5IHN0cm9uZyBiZW5jaG1hcmsgcmVzdWx0cyBvbiByZWFzb25pbmcgdGFza3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgVHJhaW5lciwgVHJhaW5pbmdBcmd1bWVudHNcbmZyb20gZGF0YXNldHMgaW1wb3J0IGxvYWRfZGF0YXNldFxuXG5kZWYgZGlzdGlsbF9mcm9tX3IxKHN0dWRlbnRfbmFtZSwgdHJhY2VzX3BhdGgsIG91dHB1dF9kaXIsIGV2YWxfZGF0YXNldCk6XG4gICAgc3R1ZGVudCA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChzdHVkZW50X25hbWUpXG4gICAgZGF0YXNldCA9IGxvYWRfZGF0YXNldChcImpzb25cIiwgZGF0YV9maWxlcz10cmFjZXNfcGF0aClbXCJ0cmFpblwiXVxuICAgICMgTWFzayBsb3NzIHRvIGFuc3dlciB0b2tlbnM7IENvVCB0b2tlbnMgYXJlIHN0aWxsIGZlZCBhcyBjb250ZXh0XG4gICAgZGF0YXNldCA9IGRhdGFzZXQubWFwKGxhbWJkYSB4OiBtYXNrX2NvdF90b2tlbnMoeCwgYW5zd2VyX3RhZz1cIlx1MDAzY2Fuc3dlclx1MDAzZVwiKSlcbiAgICBhcmdzID0gVHJhaW5pbmdBcmd1bWVudHMoXG4gICAgICAgIG91dHB1dF9kaXI9b3V0cHV0X2RpciwgbnVtX3RyYWluX2Vwb2Nocz0zLFxuICAgICAgICBwZXJfZGV2aWNlX3RyYWluX2JhdGNoX3NpemU9MiwgbGVhcm5pbmdfcmF0ZT0yZS01LFxuICAgICAgICBncmFkaWVudF9hY2N1bXVsYXRpb25fc3RlcHM9OCxcbiAgICApXG4gICAgdHJhaW5lciA9IFRyYWluZXIobW9kZWw9c3R1ZGVudCwgYXJncz1hcmdzLCB0cmFpbl9kYXRhc2V0PWRhdGFzZXQpXG4gICAgdHJhaW5lci50cmFpbigpXG4gICAgcmV0dXJuIGV2YWx1YXRlX2FpbWUoc3R1ZGVudCwgZXZhbF9kYXRhc2V0KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlzdGlsbGF0aW9uIHdvcmtzIGJlY2F1c2UgdGhlIHN0dWRlbnQgbGVhcm5zIHRvIHJlcHJvZHVjZSB0aGUgc3RydWN0dXJlIG9mIGxvbmcgcmVhc29uaW5nIGNoYWlucyDigJQgaW5jbHVkaW5nIGJhY2t0cmFja2luZywgc2VsZi1jb3JyZWN0aW9uLCBhbmQgdmVyaWZpY2F0aW9uIHN0ZXBzIOKAlCBieSBpbWl0YXRpbmcgdGhlIHRlYWNoZXIuIFJlbWFya2FibHksIGEgN0IgbW9kZWwgZGlzdGlsbGVkIGZyb20gUjEgb3V0cGVyZm9ybXMgbXVjaCBsYXJnZXIgbW9kZWxzIHRyYWluZWQgd2l0aG91dCBjaGFpbi1vZi10aG91Z2h0IGRpc3RpbGxhdGlvbiwgYWNoaWV2aW5nIDU1LjUlIG9uIEFJTUUgMjAyNCBhbmQgOTIuOCUgb24gTUFUSC01MDAuIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRUeXBlIjoiaW5mbyIsImNvbnRlbnQiOiJEZWVwU2Vlay1SMS1aZXJvIHRyYWluZWQgcHVyZWx5IHZpYSBSTCB3aXRoIG5vIFNGVCBzcG9udGFuZW91c2x5IGRldmVsb3BlZCBjaGFpbi1vZi10aG91Z2h0IHJlYXNvbmluZywgc2VsZi12ZXJpZmljYXRpb24sIGFuZCByZWZsZWN0aW9uIGJlaGF2aW9ycyDigJQgZGVtb25zdHJhdGluZyB0aGF0IHJlYXNvbmluZyBjYW4gZW1lcmdlIGZyb20gcmV3YXJkIHNpZ25hbHMgYWxvbmUgd2l0aG91dCBhbnkgaHVtYW4tbGFiZWxlZCByZWFzb25pbmcgdHJhY2VzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIkFJTUUgMjAyNCAoJSkiLCJNQVRILTUwMCAoJSkiLCJDb2RlZm9yY2VzICglaWxlKSIsIlBhcmFtcyJdLCJyb3dzIjpbWyJSMS1aZXJvIiwiNzEuMCIsIjkwLjAiLCI1OC4wIiwiNjcxQiJdLFsiUjEiLCI3OS44IiwiOTcuMyIsIjk2LjMiLCI2NzFCIl0sWyJSMS1EaXN0aWxsLTdCIiwiNTUuNSIsIjkyLjgiLCIzNy42IiwiN0IiXSxbIlIxLURpc3RpbGwtMzJCIiwiNzIuNiIsIjk0LjMiLCI3Mi42IiwiMzJCIl0sWyJHUFQtNG8iLCI5LjMiLCI3Ni42IiwiNDMuNCIsIi0iXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGJlbmNobWFyayBudW1iZXJzIGhpZ2hsaWdodCBhIGtleSBpbnNpZ2h0OiBkaXN0aWxsYXRpb24gdHJhbnNmZXJzIHJlYXNvbmluZyBjYXBhYmlsaXR5IGVmZmljaWVudGx5LiBSMS1EaXN0aWxsLTMyQiBhdCAzMkIgcGFyYW1ldGVycyB2YXN0bHkgZXhjZWVkcyBHUFQtNG8gb24gQUlNRSAyMDI0ICg3Mi42JSB2cyA5LjMlKSwgYW5kIGV2ZW4gUjEtRGlzdGlsbC03QiBzdWJzdGFudGlhbGx5IG91dHBlcmZvcm1zIEdQVC00by4gVGhlIGdhcCBiZXR3ZWVuIFIxLVplcm8gYW5kIFIxIGFsc28gc2hvd3MgdGhlIGNvbmNyZXRlIHZhbHVlIG9mIGNvbGQtc3RhcnQgU0ZUIGFuZCB0aGUgc2Vjb25kIGFsaWdubWVudCBwYXNzLiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJoZWFkaW5nIiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0IiwiaXRlbXMiOlsiR1JQTyBlbGltaW5hdGVzIHRoZSBjcml0aWMvdmFsdWUgbW9kZWwgYnkgZXN0aW1hdGluZyBhZHZhbnRhZ2VzIHdpdGhpbiBhIGdyb3VwIG9mIEsgc2FtcGxlZCByZXNwb25zZXMg4oCUIHJlZHVjaW5nIHRyYWluaW5nIGNvbXBsZXhpdHkgYW5kIEdQVSBtZW1vcnkgdnMgUFBPLiIsIlIxLVplcm8gcHJvdmVzIHJlYXNvbmluZyBjYW4gZW1lcmdlIGZyb20gUkwgd2l0aCBydWxlLWJhc2VkIHJld2FyZHMgYWxvbmUsIHdpdGggbm8gU0ZUIG9uIENvVCBkYXRhIOKAlCB0aG91Z2ggb3V0cHV0IHF1YWxpdHkgaXMgaW5jb25zaXN0ZW50IHdpdGhvdXQgY29sZC1zdGFydCBpbml0aWFsaXphdGlvbi4iLCJDb2xkLXN0YXJ0IFNGVCBvbiBhIHNtYWxsIHNldCBvZiBodW1hbi1jdXJhdGVkIENvVCBleGFtcGxlcyBzdGFiaWxpemVzIGZvcm1hdHRpbmcgYW5kIGxhbmd1YWdlIGNvbnNpc3RlbmN5IGJlZm9yZSBSTCB0cmFpbmluZyBiZWdpbnMuIiwiRGlzdGlsbGF0aW9uIHZpYSBpbWl0YXRpb24gb2YgUjEtNjcxQiB0cmFjZXMgZ2l2ZXMgN0IgYW5kIDMyQiBtb2RlbHMgc3Ryb25nIHJlYXNvbmluZyBhdCBhIGZyYWN0aW9uIG9mIHRoZSBSTCB0cmFpbmluZyBjb3N0IOKAlCBubyBSTCByZXF1aXJlZCBvbiB0aGUgc3R1ZGVudCBtb2RlbC4iLCJSMS1EaXN0aWxsLTMyQiBzY29yZXMgNzIuNiUgb24gQUlNRSAyMDI0LCB2YXN0bHkgZXhjZWVkaW5nIEdQVC00byAoOS4zJSkg4oCUIHNob3dpbmcgdGhhdCBkaXN0aWxsZWQgcmVhc29uaW5nIGRyYW1hdGljYWxseSBvdXRwZXJmb3JtcyBzY2FsZS1vbmx5IGFwcHJvYWNoZXMuIiwiVXNlIGRpc3RpbGxlZCBtb2RlbHMgKDdCLzMyQikgZm9yIHByb2R1Y3Rpb24gc2VydmluZzsgdXNlIGZ1bGwgUjEtNjcxQiBmb3IgZ2VuZXJhdGluZyBoaWdoLXF1YWxpdHkgcmVhc29uaW5nIHRyYWNlcyBmb3IgZnV0dXJlIGRpc3RpbGxhdGlvbiByb3VuZHMuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVlcFNlZWstUjFcdTAwMjdzIGtleSBjb250cmlidXRpb24gaXMgYSBwcmFjdGljYWwgdHJhaW5pbmcgcmVjaXBlOiBncm93IHN0cm9uZyByZWFzb25pbmcgd2l0aCBHUlBPIHVzaW5nIHJ1bGUtYmFzZWQgcmV3YXJkcywgdGhlbiBkaXN0aWxsIHRoYXQgY2FwYWJpbGl0eSBpbnRvIGRlcGxveWFibGUgc21hbGxlciBtb2RlbHMgdmlhIHN1cGVydmlzZWQgaW1pdGF0aW9uLiBUaGUgYXBwcm9hY2ggYnlwYXNzZXMgZXhwZW5zaXZlIGh1bWFuIGFubm90YXRpb24gb2YgcmVhc29uaW5nIGNoYWlucyBhbmQgZGVtb25zdHJhdGVzIHRoYXQgb3V0Y29tZSBzdXBlcnZpc2lvbiBhdCBzY2FsZSBpcyBzdWZmaWNpZW50IHRvIHByb2R1Y2Ugc3RhdGUtb2YtdGhlLWFydCByZWFzb25pbmcuIn1d"
---
# DeepSeek-R1: Reinforcement Learning for Reasoning

DeepSeek-R1 achieves o1-level performance on math and coding benchmarks using reinforcement learning with GRPO, without relying on human-labeled chain-of-thought data. R1-Zero demonstrates that complex reasoning behaviors — including self-verification and reflection — can emerge purely from reward signals, challenging the assumption that supervised CoT data is necessary.

 GRPO: Group Relative Policy Optimization

GRPO replaces the actor-critic setup used in PPO with a group-based advantage estimation. For each prompt, K responses are sampled from the current policy; each receives a scalar reward. The advantage for each response is computed by subtracting the group mean and dividing by the group standard deviation — eliminating the need for a separate critic or value model.

```python
import torch

def grpo_loss(policy, ref_policy, prompts, K=8, beta=0.04, eps=0.2):
    losses = []
    for prompt in prompts:
        completions = policy.sample(prompt, n=K, temperature=0.8)
        r = torch.tensor([reward_fn(prompt, c) for c in completions])
        adv = (r - r.mean()) / (r.std() + 1e-8)
        logp = policy.log_prob(completions)
        ref_logp = ref_policy.log_prob(completions)
        ratio = (logp - ref_logp).exp()
        clipped = torch.clamp(ratio, 1 - eps, 1 + eps)
        pg = -torch.min(ratio * adv, clipped * adv).mean()
        losses.append(pg + beta * (logp - ref_logp).mean())
    return torch.stack(losses).mean()
```

 Reward Functions

DeepSeek-R1 uses two rule-based rewards: a correctness reward that checks the final answer against a ground-truth (using SymPy for symbolic math equality and unit tests for code), and a format reward that enforces the model produces <think>...</think> and <answer>...</answer> tags. No learned reward model is needed, keeping the signal clean and verifiable.

```python
import re
from sympy import simplify, sympify, SympifyError

def reward_fn(prompt, completion, expected):
    has_think = bool(re.search(r'<think>.+</think>', completion, re.S))
    fmt_bonus = 0.1 if has_think else 0.0
    m = re.search(r'<answer>(.*?)</answer>', completion, re.S)
    if m is None:
        return fmt_bonus * 0.5
    predicted = m.group(1).strip()
    try:
        if simplify(sympify(predicted) - sympify(expected)) == 0:
            return 1.0 + fmt_bonus
    except SympifyError:
        pass
    return fmt_bonus if predicted != str(expected) else 1.0 + fmt_bonus
```

 Cold-Start Problem and SFT Initialization

R1-Zero (pure RL from base) produces emergent reasoning but suffers from language mixing and inconsistent output formatting. DeepSeek-R1 addresses this with a cold-start phase: a small set of human-curated long-CoT examples in the desired format are used to fine-tune the base model before RL begins, giving the policy a well-structured starting point.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

def cold_start_sft(model_name, sft_dataset_path, output_dir):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    dataset = load_cot_dataset(sft_dataset_path)  # <think>...</think><answer>...</answer>
    args = TrainingArguments(
        output_dir=output_dir, num_train_epochs=1,
        per_device_train_batch_size=4, learning_rate=1e-5,
        lr_scheduler_type="cosine", warmup_ratio=0.03,
    )
    trainer = Trainer(model=model, args=args,
                      train_dataset=dataset, tokenizer=tokenizer)
    trainer.train()
```

 RL Training Pipeline

The RL loop repeatedly samples completions from the current policy, scores them with the reward function, computes GRPO advantages, and updates policy weights. Training runs for thousands of steps with a KL-divergence penalty against a frozen reference policy to prevent the model from drifting too far from the pre-trained distribution.

After RL convergence, a second SFT pass is applied using rejection-sampled solutions from the RL model plus supervised data for general tasks. This round restores helpfulness on non-reasoning tasks, reduces repetition artifacts from RL training, and chat-aligns the final model while preserving the strong reasoning capability gained through GRPO.

 Distillation to Smaller Models

Rather than running expensive RL on smaller models, DeepSeek distills reasoning by generating large quantities of long-CoT solution traces from the R1-671B teacher, then fine-tuning a smaller student (7B or 32B) on those traces using standard supervised learning. This is far cheaper than RL while achieving surprisingly strong benchmark results on reasoning tasks.

```python
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset

def distill_from_r1(student_name, traces_path, output_dir, eval_dataset):
    student = AutoModelForCausalLM.from_pretrained(student_name)
    dataset = load_dataset("json", data_files=traces_path)["train"]
    # Mask loss to answer tokens; CoT tokens are still fed as context
    dataset = dataset.map(lambda x: mask_cot_tokens(x, answer_tag="<answer>"))
    args = TrainingArguments(
        output_dir=output_dir, num_train_epochs=3,
        per_device_train_batch_size=2, learning_rate=2e-5,
        gradient_accumulation_steps=8,
    )
    trainer = Trainer(model=student, args=args, train_dataset=dataset)
    trainer.train()
    return evaluate_aime(student, eval_dataset)
```

Distillation works because the student learns to reproduce the structure of long reasoning chains — including backtracking, self-correction, and verification steps — by imitating the teacher. Remarkably, a 7B model distilled from R1 outperforms much larger models trained without chain-of-thought distillation, achieving 55.5% on AIME 2024 and 92.8% on MATH-500.

> ****: DeepSeek-R1-Zero trained purely via RL with no SFT spontaneously developed chain-of-thought reasoning, self-verification, and reflection behaviors — demonstrating that reasoning can emerge from reward signals alone without any human-labeled reasoning traces.

| Model | AIME 2024 (%) | MATH-500 (%) | Codeforces (%ile) | Params |
| --- | --- | --- | --- | --- |
| R1-Zero | 71.0 | 90.0 | 58.0 | 671B |
| R1 | 79.8 | 97.3 | 96.3 | 671B |
| R1-Distill-7B | 55.5 | 92.8 | 37.6 | 7B |
| R1-Distill-32B | 72.6 | 94.3 | 72.6 | 32B |
| GPT-4o | 9.3 | 76.6 | 43.4 | - |

The benchmark numbers highlight a key insight: distillation transfers reasoning capability efficiently. R1-Distill-32B at 32B parameters vastly exceeds GPT-4o on AIME 2024 (72.6% vs 9.3%), and even R1-Distill-7B substantially outperforms GPT-4o. The gap between R1-Zero and R1 also shows the concrete value of cold-start SFT and the second alignment pass.

---

 Key Takeaways

- GRPO eliminates the critic/value model by estimating advantages within a group of K sampled responses — reducing training complexity and GPU memory vs PPO.
- R1-Zero proves reasoning can emerge from RL with rule-based rewards alone, with no SFT on CoT data — though output quality is inconsistent without cold-start initialization.
- Cold-start SFT on a small set of human-curated CoT examples stabilizes formatting and language consistency before RL training begins.
- Distillation via imitation of R1-671B traces gives 7B and 32B models strong reasoning at a fraction of the RL training cost — no RL required on the student model.
- R1-Distill-32B scores 72.6% on AIME 2024, vastly exceeding GPT-4o (9.3%) — showing that distilled reasoning dramatically outperforms scale-only approaches.
- Use distilled models (7B/32B) for production serving; use full R1-671B for generating high-quality reasoning traces for future distillation rounds.

DeepSeek-R1's key contribution is a practical training recipe: grow strong reasoning with GRPO using rule-based rewards, then distill that capability into deployable smaller models via supervised imitation. The approach bypasses expensive human annotation of reasoning chains and demonstrates that outcome supervision at scale is sufficient to produce state-of-the-art reasoning.

