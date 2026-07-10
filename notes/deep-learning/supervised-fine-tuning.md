---
title: "Supervised Fine-Tuning — Instruction Format, Conversation Templates, and SFT Training"
slug: "supervised-fine-tuning"
description: "Covers supervised fine-tuning of pretrained LLMs on curated instruction-response pairs: instruction format with chat templates, CLM loss masking on instruction tokens, LoRA-based SFT to prevent catastrophic forgetting, multi-turn conversation collation, data scale findings from LIMA, and key SFT configurations across LLaMA-3, Mistral, Phi-3, Gemma, and Qwen2."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3VwZXJ2aXNlZCBmaW5lLXR1bmluZyAoU0ZUKSBhZGFwdHMgYSBwcmV0cmFpbmVkIExMTSB0byBmb2xsb3cgaW5zdHJ1Y3Rpb25zIGJ5IHRyYWluaW5nIG9uIGN1cmF0ZWQgKGluc3RydWN0aW9uLCByZXNwb25zZSkgcGFpcnMgdXNpbmcgY2F1c2FsIGxhbmd1YWdlIG1vZGVsbGluZyBsb3NzIHJlc3RyaWN0ZWQgdG8gdGhlIHJlc3BvbnNlIHRva2Vucy4gVGhlIHByZXRyYWluZWQgbW9kZWwgYWxyZWFkeSBlbmNvZGVzIHdvcmxkIGtub3dsZWRnZSBhbmQgbGFuZ3VhZ2Ugc3RydWN0dXJlOyBTRlQgcmVzaGFwZXMgaXRzIG91dHB1dCBkaXN0cmlidXRpb24gdG93YXJkIGhlbHBmdWwsIGZvcm1hdHRlZCByZXNwb25zZXMgd2l0aG91dCByZWxlYXJuaW5nIGZhY3RzIGZyb20gc2NyYXRjaC4gVW5kZXJzdGFuZGluZyB0aGUgZXhhY3QgbWVjaGFuaWNzIOKAlCBjaGF0IHRlbXBsYXRlIGZvcm1hdHRpbmcsIGxvc3MgbWFza2luZywgZ3JhZGllbnQgYWNjdW11bGF0aW9uLCBhbmQgcmVndWxhcmlzYXRpb24gd2l0aCBMb1JBIOKAlCBpcyBwcmVyZXF1aXNpdGUgZm9yIGJ1aWxkaW5nIGluc3RydWN0aW9uLXR1bmVkIG1vZGVscyB0aGF0IGdlbmVyYWxpc2UgYmV5b25kIHRoZSB0cmFpbmluZyBkaXN0cmlidXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW5zdHJ1Y3Rpb24gRm9ybWF0IGFuZCBDaGF0IFRlbXBsYXRlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9kZXJuIGluc3RydWN0aW9uLXR1bmVkIG1vZGVscyB1c2UgYSBzdHJ1Y3R1cmVkIGNvbnZlcnNhdGlvbiBmb3JtYXQ6IGEgc3lzdGVtIHByb21wdCBlc3RhYmxpc2hlcyB0aGUgYXNzaXN0YW50IHBlcnNvbmEsIGEgdXNlciB0dXJuIHByb3ZpZGVzIHRoZSBpbnN0cnVjdGlvbiwgYW5kIGFuIGFzc2lzdGFudCB0dXJuIGNvbnRhaW5zIHRoZSBleHBlY3RlZCByZXNwb25zZS4gRWFjaCBtb2RlbCBmYW1pbHkgZGVmaW5lcyBhIGNoYXQgdGVtcGxhdGUgdGhhdCBzZXJpYWxpc2VzIHRoaXMgc3RydWN0dXJlIGludG8gYSBmbGF0IHN0cmluZyB3aXRoIHNwZWNpYWwgdG9rZW5zLiBMTGFNQS0zIHVzZXMgXHUwMDNjfGJlZ2luX29mX3RleHR8XHUwMDNlLCBcdTAwM2N8c3RhcnRfaGVhZGVyX2lkfFx1MDAzZXJvbGVcdTAwM2N8ZW5kX2hlYWRlcl9pZHxcdTAwM2VcXG5cXG5jb250ZW50XHUwMDNjfGVvdF9pZHxcdTAwM2UgbWFya2Vycy4gTWlzdHJhbCB1c2VzIFtJTlNUXSAuLi4gWy9JTlNUXSB3cmFwcGluZy4gUGhpLTMgdXNlcyBcdTAwM2N8c3lzdGVtfFx1MDAzZSwgXHUwMDNjfHVzZXJ8XHUwMDNlLCBcdTAwM2N8YXNzaXN0YW50fFx1MDAzZSBzZW50aW5lbHMuIFRoZSB0ZW1wbGF0ZSBpcyBiYWtlZCBpbnRvIHRoZSB0b2tlbmlzZXIgYW5kIGFwcGxpZWQgdmlhIHRva2VuaXplci5hcHBseV9jaGF0X3RlbXBsYXRlKCkuIE1peGluZyB0ZW1wbGF0ZXMgYWNyb3NzIG1vZGVscyBpcyBhIGNvbW1vbiBidWcgdGhhdCBkZWdyYWRlcyBpbnN0cnVjdGlvbiBmb2xsb3dpbmcgc2lsZW50bHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVG9rZW5pc2F0aW9uIGFuZCBMb3NzIE1hc2tpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNMTSBsb3NzIGlzIGNvbXB1dGVkIG92ZXIgYWxsIHRva2VucyBieSBkZWZhdWx0LCBidXQgZm9yIFNGVCBvbmx5IHRoZSBhc3Npc3RhbnQgcmVzcG9uc2UgdG9rZW5zIHNob3VsZCBjb250cmlidXRlIHRvIHRoZSBsb3NzIOKAlCB0aGUgbW9kZWwgaXMgbm90IGJlaW5nIHRyYWluZWQgdG8gcHJlZGljdCB0aGUgaW5zdHJ1Y3Rpb24uIFRoZSBzdGFuZGFyZCBhcHByb2FjaDogYXBwbHkgdGhlIGNoYXQgdGVtcGxhdGUgdG8gdGhlIGZ1bGwgY29udmVyc2F0aW9uIHRvIGdldCBpbnB1dF9pZHMsIHNlcGFyYXRlbHkgdG9rZW5pc2UgdGhlIGluc3RydWN0aW9uIHBvcnRpb24gdG8gZGV0ZXJtaW5lIGl0cyBsZW5ndGgsIHRoZW4gc2V0IGxhYmVsc1s6aW5zdHJ1Y3Rpb25fbGVuXSA9IC0xMDAuIEh1Z2dpbmdGYWNlXHUwMDI3cyBUcmFpbmVyIGlnbm9yZXMgcG9zaXRpb25zIHdpdGggbGFiZWwgLTEwMCB3aGVuIGNvbXB1dGluZyBjcm9zcy1lbnRyb3B5LiBHZXR0aW5nIHRoaXMgbWFza2luZyByaWdodCBpcyBjcml0aWNhbDogaWYgaW5zdHJ1Y3Rpb24gdG9rZW5zIGxlYWsgaW50byB0aGUgbG9zcywgdGhlIG1vZGVsIGxlYXJucyB0byByZXByb2R1Y2Ugc3lzdGVtIGFuZCB1c2VyIHR1cm5zIHJhdGhlciB0aGFuIGZvbGxvdyB0aGVtLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuaW1wb3J0IHRvcmNoXG5cbmRlZiBmb3JtYXRfc2Z0X2V4YW1wbGUodG9rZW5pemVyLCBzeXN0ZW0sIHVzZXIsIGFzc2lzdGFudCwgbWF4X2xlbmd0aD0xMDI0KTpcbiAgICBcIlwiXCJBcHBseSBjaGF0IHRlbXBsYXRlIGFuZCBtYXNrIGluc3RydWN0aW9uIHRva2VucyBmcm9tIENMTSBsb3NzLlwiXCJcIlxuICAgIG1lc3NhZ2VzID0gW1xuICAgICAgICB7XCJyb2xlXCI6IFwic3lzdGVtXCIsIFwiY29udGVudFwiOiBzeXN0ZW19LFxuICAgICAgICB7XCJyb2xlXCI6IFwidXNlclwiLCBcImNvbnRlbnRcIjogdXNlcn0sXG4gICAgICAgIHtcInJvbGVcIjogXCJhc3Npc3RhbnRcIiwgXCJjb250ZW50XCI6IGFzc2lzdGFudH0sXG4gICAgXVxuICAgICMgRnVsbCBjb252ZXJzYXRpb24gdGV4dCAoaW5jbHVkaW5nIGFzc2lzdGFudCByZXNwb25zZSlcbiAgICBmdWxsX3RleHQgPSB0b2tlbml6ZXIuYXBwbHlfY2hhdF90ZW1wbGF0ZShtZXNzYWdlcywgdG9rZW5pemU9RmFsc2UsIGFkZF9nZW5lcmF0aW9uX3Byb21wdD1GYWxzZSlcbiAgICAjIEluc3RydWN0aW9uLW9ubHkgdGV4dCB0byBjb21wdXRlIG1hc2sgYm91bmRhcnlcbiAgICBpbnN0cl90ZXh0ID0gdG9rZW5pemVyLmFwcGx5X2NoYXRfdGVtcGxhdGUobWVzc2FnZXNbOjJdLCB0b2tlbml6ZT1GYWxzZSwgYWRkX2dlbmVyYXRpb25fcHJvbXB0PVRydWUpXG4gICAgZW5jID0gdG9rZW5pemVyKGZ1bGxfdGV4dCwgbWF4X2xlbmd0aD1tYXhfbGVuZ3RoLCB0cnVuY2F0aW9uPVRydWUsIHJldHVybl90ZW5zb3JzPVwicHRcIilcbiAgICBpbnB1dF9pZHMgPSBlbmMuaW5wdXRfaWRzWzBdXG4gICAgaW5zdHJfbGVuID0gbGVuKHRva2VuaXplcihpbnN0cl90ZXh0LCBhZGRfc3BlY2lhbF90b2tlbnM9RmFsc2UpLmlucHV0X2lkcylcbiAgICBsYWJlbHMgPSBpbnB1dF9pZHMuY2xvbmUoKVxuICAgIGxhYmVsc1s6aW5zdHJfbGVuXSA9IC0xMDAgICMgbm8gbG9zcyBvbiBpbnN0cnVjdGlvbiB0b2tlbnNcbiAgICByZXR1cm4ge1wiaW5wdXRfaWRzXCI6IGlucHV0X2lkcywgXCJsYWJlbHNcIjogbGFiZWxzLCBcImF0dGVudGlvbl9tYXNrXCI6IGVuYy5hdHRlbnRpb25fbWFza1swXX1cblxuIyBEZW1vXG50b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcIm1ldGEtbGxhbWEvTGxhbWEtMy04Qi1JbnN0cnVjdFwiKVxuZXhhbXBsZSA9IGZvcm1hdF9zZnRfZXhhbXBsZShcbiAgICB0b2tlbml6ZXIsXG4gICAgc3lzdGVtPVwiWW91IGFyZSBhIGhlbHBmdWwgYXNzaXN0YW50LlwiLFxuICAgIHVzZXI9XCJFeHBsYWluIGJhY2twcm9wYWdhdGlvbiBpbiBvbmUgcGFyYWdyYXBoLlwiLFxuICAgIGFzc2lzdGFudD1cIkJhY2twcm9wYWdhdGlvbiBhcHBsaWVzIHRoZSBjaGFpbiBydWxlIGluIHJldmVyc2UgdGhyb3VnaCB0aGUgY29tcHV0YXRpb25hbCBncmFwaCB0byBjb21wdXRlIGdyYWRpZW50cyBvZiB0aGUgbG9zcyB3cnQgZXZlcnkgcGFyYW1ldGVyLlwiLFxuKVxucHJpbnQoZlwiaW5wdXRfaWRzIHNoYXBlIDoge2V4YW1wbGVbXHUwMDI3aW5wdXRfaWRzXHUwMDI3XS5zaGFwZX1cIilcbnByaW50KGZcIk1hc2tlZCB0b2tlbnMgICA6IHsoZXhhbXBsZVtcdTAwMjdsYWJlbHNcdTAwMjddID09IC0xMDApLnN1bSgpLml0ZW0oKX0gKGluc3RydWN0aW9uKVwiKVxucHJpbnQoZlwiTG9zcyB0b2tlbnMgICAgIDogeyhleGFtcGxlW1x1MDAyN2xhYmVsc1x1MDAyN10gIT0gLTEwMCkuc3VtKCkuaXRlbSgpfSAoYXNzaXN0YW50IHJlc3BvbnNlKVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNGVCBUcmFpbmluZyBEZXRhaWxzIOKAlCBMUiwgRXBvY2hzLCBhbmQgQmF0Y2ggU2l6ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU0ZUIHVzZXMgc21hbGwgbGVhcm5pbmcgcmF0ZXMgKDFlLTUgdG8gNWUtNSkgdG8gcHJldmVudCBvdmVyd3JpdGluZyBwcmV0cmFpbmVkIHJlcHJlc2VudGF0aW9ucy4gVHJhaW5pbmcgcnVucyBmb3IgMeKAkzMgZXBvY2hzIG9uIHNtYWxsIGRhdGFzZXRzIChmZXcgdGhvdXNhbmQgZXhhbXBsZXMpIHRvIGF2b2lkIG92ZXJmaXR0aW5nOyBvbiBsYXJnZXIgZGF0YXNldHMgKDUwSyspIGEgc2luZ2xlIGVwb2NoIG1heSBzdWZmaWNlLiBDb3NpbmUgbGVhcm5pbmcgcmF0ZSBkZWNheSB3aXRoIGEgc2hvcnQgd2FybS11cCAoNeKAkzEwJSBvZiBzdGVwcykgaXMgc3RhbmRhcmQuIEVmZmVjdGl2ZSBiYXRjaCBzaXplIGlzIHR5cGljYWxseSAxMjjigJMyNTYgc2VxdWVuY2VzIGFjaGlldmVkIHZpYSBncmFkaWVudCBhY2N1bXVsYXRpb24gYWNyb3NzIDjigJMzMiBwaHlzaWNhbCBiYXRjaGVzLCBpbXByb3ZpbmcgZ3JhZGllbnQgcXVhbGl0eSBvbiBzbWFsbCBTRlQgZGF0YXNldHMuIEFkYW1XIHdpdGggd2VpZ2h0IGRlY2F5IDAuMDEgaXMgdGhlIGRlZmF1bHQgb3B0aW1pemVyLiBVbmxpa2UgcHJldHJhaW5pbmcsIFNGVCBkYXRhc2V0cyBhcmUgc21hbGwgZW5vdWdoIHRoYXQgdHJhaW5pbmcgdGltZSBpcyBkb21pbmF0ZWQgYnkgZGF0YSBwcmVwcm9jZXNzaW5nIGFuZCB0b2tlbmlzYXRpb24gcmF0aGVyIHRoYW4gY29tcHV0ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvVG9rZW5pemVyLCBnZXRfY29zaW5lX3NjaGVkdWxlX3dpdGhfd2FybXVwXG5mcm9tIHBlZnQgaW1wb3J0IExvcmFDb25maWcsIGdldF9wZWZ0X21vZGVsXG5pbXBvcnQgdG9yY2hcbmZyb20gdG9yY2gub3B0aW0gaW1wb3J0IEFkYW1XXG5cbmRlZiBzZnRfdHJhaW5fc3RlcChtb2RlbCwgYmF0Y2gsIG9wdGltaXplciwgc2NoZWR1bGVyKTpcbiAgICBcIlwiXCJTaW5nbGUgU0ZUIGdyYWRpZW50IHN0ZXAgd2l0aCBMb1JBOyBsb3NzIGNvbXB1dGVkIG9ubHkgb24gcmVzcG9uc2UgdG9rZW5zLlwiXCJcIlxuICAgIGlucHV0X2lkcyA9IGJhdGNoW1wiaW5wdXRfaWRzXCJdLnRvKG1vZGVsLmRldmljZSlcbiAgICBsYWJlbHMgPSBiYXRjaFtcImxhYmVsc1wiXS50byhtb2RlbC5kZXZpY2UpXG4gICAgYXR0ZW50aW9uX21hc2sgPSBiYXRjaFtcImF0dGVudGlvbl9tYXNrXCJdLnRvKG1vZGVsLmRldmljZSlcbiAgICAjIEh1Z2dpbmdGYWNlIENhdXNhbExNIGlnbm9yZXMgbGFiZWw9LTEwMCBwb3NpdGlvbnMgYXV0b21hdGljYWxseVxuICAgIG91dHB1dHMgPSBtb2RlbChpbnB1dF9pZHM9aW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzaz1hdHRlbnRpb25fbWFzaywgbGFiZWxzPWxhYmVscylcbiAgICBsb3NzID0gb3V0cHV0cy5sb3NzXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgdG9yY2gubm4udXRpbHMuY2xpcF9ncmFkX25vcm1fKG1vZGVsLnBhcmFtZXRlcnMoKSwgbWF4X25vcm09MS4wKVxuICAgIG9wdGltaXplci5zdGVwKClcbiAgICBzY2hlZHVsZXIuc3RlcCgpXG4gICAgcmV0dXJuIGxvc3MuaXRlbSgpXG5cbiMgQXR0YWNoIExvUkEgdG8gYmFzZSBtb2RlbFxuYmFzZSA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcIm1ldGEtbGxhbWEvTGxhbWEtMy04QlwiLCB0b3JjaF9kdHlwZT10b3JjaC5iZmxvYXQxNilcbmxvcmFfY2ZnID0gTG9yYUNvbmZpZyhcbiAgICByPTE2LCBsb3JhX2FscGhhPTMyLFxuICAgIHRhcmdldF9tb2R1bGVzPVtcInFfcHJvalwiLCBcImtfcHJvalwiLCBcInZfcHJvalwiLCBcIm9fcHJvalwiXSxcbiAgICBsb3JhX2Ryb3BvdXQ9MC4wNSwgYmlhcz1cIm5vbmVcIiwgdGFza190eXBlPVwiQ0FVU0FMX0xNXCJcbilcbm1vZGVsID0gZ2V0X3BlZnRfbW9kZWwoYmFzZSwgbG9yYV9jZmcpXG5tb2RlbC5wcmludF90cmFpbmFibGVfcGFyYW1ldGVycygpICAjIH4wLjUlIG9mIHBhcmFtcyBmb3Igcj0xNlxuXG5vcHRpbWl6ZXIgPSBBZGFtVyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTJlLTUsIHdlaWdodF9kZWNheT0wLjAxKVxuc2NoZWR1bGVyID0gZ2V0X2Nvc2luZV9zY2hlZHVsZV93aXRoX3dhcm11cChvcHRpbWl6ZXIsIG51bV93YXJtdXBfc3RlcHM9MTAwLCBudW1fdHJhaW5pbmdfc3RlcHM9MzAwMClcbnByaW50KFwiTG9SQSBTRlQgc2V0dXAgY29tcGxldGUg4oCUIG9ubHkgYWRhcHRlciB3ZWlnaHRzIHVwZGF0ZSBkdXJpbmcgdHJhaW5pbmdcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1UdXJuIENvbnZlcnNhdGlvbiBTRlQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBtdWx0aS10dXJuIGNvbnZlcnNhdGlvbnMsIHRoZSBTRlQgZXhhbXBsZSBpbmNsdWRlcyBtdWx0aXBsZSB1c2VyIGFuZCBhc3Npc3RhbnQgZXhjaGFuZ2VzLiBUaGUgdHJhaW5pbmcgb2JqZWN0aXZlIGFwcGxpZXMgdGVhY2hlci1mb3JjaW5nIGN1bXVsYXRpdmVseTogZ2l2ZW4gYWxsIHByZXZpb3VzIHR1cm5zLCBwcmVkaWN0IHRoZSBuZXh0IGFzc2lzdGFudCB0dXJuLiBPbmx5IGFzc2lzdGFudCB0dXJucyBjb250cmlidXRlIHRvIHRoZSBsb3NzOyBhbGwgdXNlciBhbmQgc3lzdGVtIHR1cm5zIGFyZSBtYXNrZWQgd2l0aCAtMTAwLiBUaGlzIGN1bXVsYXRpdmUgc3RydWN0dXJlIG1lYW5zIHRoZSBtb2RlbCBsZWFybnMgdG8gY29uZGl0aW9uIGl0cyByZXNwb25zZSBvbiB0aGUgZnVsbCBjb252ZXJzYXRpb24gaGlzdG9yeSwgZW5hYmxpbmcgaW4tY29udGV4dCBjb2hlcmVuY2UgYWNyb3NzIHR1cm5zLiBQYWNraW5nIG11bHRpcGxlIGNvbnZlcnNhdGlvbnMgaW50byBhIHNpbmdsZSBzZXF1ZW5jZSAod2l0aCBkb2N1bWVudCBib3VuZGFyaWVzIG1hcmtlZCBieSBlbmQtb2Ytc2VxdWVuY2UgdG9rZW5zKSBpcyBjb21tb24gZm9yIGVmZmljaWVuY3kgb24gR1BVIG1lbW9yeS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXJcbmltcG9ydCB0b3JjaFxuXG5kZWYgY29sbGF0ZV9tdWx0aXR1cm4odG9rZW5pemVyLCBjb252ZXJzYXRpb24sIG1heF9sZW5ndGg9MjA0OCk6XG4gICAgXCJcIlwiUGFjayBtdWx0aS10dXJuIGNvbnZlcnNhdGlvbjsgY29tcHV0ZSBsb3NzIG9ubHkgb24gYXNzaXN0YW50IHR1cm5zLlwiXCJcIlxuICAgIGlucHV0X2lkcywgbGFiZWxzID0gW10sIFtdXG4gICAgZm9yIHR1cm4gaW4gY29udmVyc2F0aW9uOlxuICAgICAgICB0ZXh0ID0gdG9rZW5pemVyLmFwcGx5X2NoYXRfdGVtcGxhdGUoW3R1cm5dLCB0b2tlbml6ZT1GYWxzZSwgYWRkX2dlbmVyYXRpb25fcHJvbXB0PUZhbHNlKVxuICAgICAgICBpZHMgPSB0b2tlbml6ZXIodGV4dCwgYWRkX3NwZWNpYWxfdG9rZW5zPUZhbHNlKS5pbnB1dF9pZHNcbiAgICAgICAgaWYgdHVybltcInJvbGVcIl0gPT0gXCJhc3Npc3RhbnRcIjpcbiAgICAgICAgICAgIGxhYmVscy5leHRlbmQoaWRzKSAgICAgICAgICAjIGluY2x1ZGUgaW4gbG9zc1xuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgbGFiZWxzLmV4dGVuZChbLTEwMF0gKiBsZW4oaWRzKSkgICMgbWFzayBzeXN0ZW0vdXNlciB0dXJuc1xuICAgICAgICBpbnB1dF9pZHMuZXh0ZW5kKGlkcylcbiAgICBpbnB1dF9pZHMgPSB0b3JjaC50ZW5zb3IoaW5wdXRfaWRzWzptYXhfbGVuZ3RoXSlcbiAgICBsYWJlbHMgPSB0b3JjaC50ZW5zb3IobGFiZWxzWzptYXhfbGVuZ3RoXSlcbiAgICByZXR1cm4ge1wiaW5wdXRfaWRzXCI6IGlucHV0X2lkcywgXCJsYWJlbHNcIjogbGFiZWxzLFxuICAgICAgICAgICAgXCJhdHRlbnRpb25fbWFza1wiOiB0b3JjaC5vbmVzX2xpa2UoaW5wdXRfaWRzKX1cblxuIyBFeGFtcGxlOiAzLXR1cm4gY29udmVyc2F0aW9uXG50b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcIm1ldGEtbGxhbWEvTGxhbWEtMy04Qi1JbnN0cnVjdFwiKVxuY29udiA9IFtcbiAgICB7XCJyb2xlXCI6IFwic3lzdGVtXCIsICAgIFwiY29udGVudFwiOiBcIllvdSBhcmUgYSBjb2RpbmcgYXNzaXN0YW50LlwifSxcbiAgICB7XCJyb2xlXCI6IFwidXNlclwiLCAgICAgIFwiY29udGVudFwiOiBcIldoYXQgaXMgYSBncmFkaWVudD9cIn0sXG4gICAge1wicm9sZVwiOiBcImFzc2lzdGFudFwiLCBcImNvbnRlbnRcIjogXCJBIGdyYWRpZW50IGlzIHRoZSB2ZWN0b3Igb2YgcGFydGlhbCBkZXJpdmF0aXZlcyBvZiBhIHNjYWxhciBmdW5jdGlvbi5cIn0sXG4gICAge1wicm9sZVwiOiBcInVzZXJcIiwgICAgICBcImNvbnRlbnRcIjogXCJIb3cgaXMgaXQgdXNlZCBpbiB0cmFpbmluZz9cIn0sXG4gICAge1wicm9sZVwiOiBcImFzc2lzdGFudFwiLCBcImNvbnRlbnRcIjogXCJUaGUgZ3JhZGllbnQgb2YgdGhlIGxvc3Mgd3J0IHBhcmFtZXRlcnMgZHJpdmVzIHRoZSBwYXJhbWV0ZXIgdXBkYXRlIGluIGdyYWRpZW50IGRlc2NlbnQuXCJ9LFxuXVxuYmF0Y2ggPSBjb2xsYXRlX211bHRpdHVybih0b2tlbml6ZXIsIGNvbnYpXG5wcmludChmXCJUb3RhbCB0b2tlbnMgOiB7YmF0Y2hbXHUwMDI3aW5wdXRfaWRzXHUwMDI3XS5zaGFwZVswXX1cIilcbnByaW50KGZcIk1hc2tlZCB0b2tlbnM6IHsoYmF0Y2hbXHUwMDI3bGFiZWxzXHUwMDI3XSA9PSAtMTAwKS5zdW0oKS5pdGVtKCl9IChzeXN0ZW0rdXNlcilcIilcbnByaW50KGZcIkxvc3MgdG9rZW5zICA6IHsoYmF0Y2hbXHUwMDI3bGFiZWxzXHUwMDI3XSAhPSAtMTAwKS5zdW0oKS5pdGVtKCl9IChhc3Npc3RhbnQgdHVybnMpXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGF0YSBTY2FsZSDigJQgTElNQSBhbmQgdGhlIExlc3MtaXMtTW9yZSBQcmluY2lwbGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBMSU1BIHBhcGVyICgyMDIzKSBkZW1vbnN0cmF0ZWQgdGhhdCAxLDAwMCBjYXJlZnVsbHkgY3VyYXRlZCwgZGl2ZXJzZSBleGFtcGxlcyBwcm9kdWNlIGFuIFNGVCBtb2RlbCBjb21wZXRpdGl2ZSB3aXRoIG1vZGVscyB0cmFpbmVkIG9uIDUyLDAwMCBBbHBhY2EgZXhhbXBsZXMuIFRoZSBrZXkgaW5zaWdodDogYSBwcmV0cmFpbmVkIG1vZGVsIGFscmVhZHkgaGFzIHRoZSBrbm93bGVkZ2UgYW5kIGxhbmd1YWdlIGFiaWxpdHk7IFNGVCBpcyBtZXJlbHkgdGVhY2hpbmcgaXQgdGhlIHN1cmZhY2UgZm9ybWF0IG9mIGhlbHBmdWxuZXNzLiBSYXcgZGF0YSB2b2x1bWUgbWF0dGVycyBmYXIgbGVzcyB0aGFuIGRpdmVyc2l0eSAoY292ZXJpbmcgZGlmZmVyZW50IHRhc2sgdHlwZXMsIGRvbWFpbnMsIGxlbmd0aHMpIGFuZCBxdWFsaXR5IChjb3JyZWN0LCB3ZWxsLXN0cnVjdHVyZWQgcmVzcG9uc2VzKS4gVGhlIEZMQU4gYXBwcm9hY2ggZ29lcyB0aGUgb3Bwb3NpdGUgZGlyZWN0aW9uIOKAlCBmaW5lLXR1bmluZyBvbiAxLDAwMCsgTkxQIHRhc2tzIGluIGluc3RydWN0aW9uIGZvcm1hdCDigJQgc2hvd2luZyB0aGF0IGJyZWFkdGggZ2VuZXJhbGlzZXMgemVyby1zaG90LiBCb3RoIGZpbmRpbmdzIHBvaW50IHRvIHRoZSBzYW1lIGNvbmNsdXNpb246IHRoZSBpbnN0cnVjdGlvbiBkaXN0cmlidXRpb24sIG5vdCBpdHMgc2l6ZSwgZGV0ZXJtaW5lcyBTRlQgcXVhbGl0eS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSBkYXRhc2V0cyBpbXBvcnQgbG9hZF9kYXRhc2V0XG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplciwgRGF0YUNvbGxhdG9yRm9yU2VxMlNlcVxuZnJvbSB0b3JjaC51dGlscy5kYXRhIGltcG9ydCBEYXRhTG9hZGVyXG5cbnRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFwibWV0YS1sbGFtYS9MbGFtYS0zLThCLUluc3RydWN0XCIpXG50b2tlbml6ZXIucGFkX3Rva2VuID0gdG9rZW5pemVyLmVvc190b2tlblxuXG5kYXRhc2V0ID0gbG9hZF9kYXRhc2V0KFwidGF0c3UtbGFiL2FscGFjYVwiLCBzcGxpdD1cInRyYWluXCIpXG5cbmRlZiBwcmVwcm9jZXNzKGV4YW1wbGUpOlxuICAgIHVzZXJfY29udGVudCA9IGV4YW1wbGVbXCJpbnN0cnVjdGlvblwiXVxuICAgIGlmIGV4YW1wbGUuZ2V0KFwiaW5wdXRcIik6XG4gICAgICAgIHVzZXJfY29udGVudCArPSBcIlxcblwiICsgZXhhbXBsZVtcImlucHV0XCJdXG4gICAgbWVzc2FnZXMgPSBbXG4gICAgICAgIHtcInJvbGVcIjogXCJ1c2VyXCIsICAgICAgXCJjb250ZW50XCI6IHVzZXJfY29udGVudH0sXG4gICAgICAgIHtcInJvbGVcIjogXCJhc3Npc3RhbnRcIiwgXCJjb250ZW50XCI6IGV4YW1wbGVbXCJvdXRwdXRcIl19LFxuICAgIF1cbiAgICBmdWxsID0gdG9rZW5pemVyLmFwcGx5X2NoYXRfdGVtcGxhdGUobWVzc2FnZXMsIHRva2VuaXplPUZhbHNlKVxuICAgIGVuYyAgPSB0b2tlbml6ZXIoZnVsbCwgbWF4X2xlbmd0aD01MTIsIHRydW5jYXRpb249VHJ1ZSwgcGFkZGluZz1GYWxzZSlcbiAgICBpbnN0ciA9IHRva2VuaXplci5hcHBseV9jaGF0X3RlbXBsYXRlKG1lc3NhZ2VzWzoxXSwgdG9rZW5pemU9RmFsc2UsIGFkZF9nZW5lcmF0aW9uX3Byb21wdD1UcnVlKVxuICAgIGluc3RyX2xlbiA9IGxlbih0b2tlbml6ZXIoaW5zdHIsIGFkZF9zcGVjaWFsX3Rva2Vucz1GYWxzZSkuaW5wdXRfaWRzKVxuICAgIGxhYmVscyA9IGVuY1tcImlucHV0X2lkc1wiXVs6XVxuICAgIGxhYmVsc1s6aW5zdHJfbGVuXSA9IFstMTAwXSAqIGluc3RyX2xlblxuICAgIGVuY1tcImxhYmVsc1wiXSA9IGxhYmVsc1xuICAgIHJldHVybiBlbmNcblxudG9rZW5pemVkID0gZGF0YXNldC5tYXAocHJlcHJvY2VzcywgcmVtb3ZlX2NvbHVtbnM9ZGF0YXNldC5jb2x1bW5fbmFtZXMsIG51bV9wcm9jPTQpXG5jb2xsYXRvciAgPSBEYXRhQ29sbGF0b3JGb3JTZXEyU2VxKHRva2VuaXplciwgcGFkZGluZz1UcnVlLCBwYWRfdG9fbXVsdGlwbGVfb2Y9OClcbmxvYWRlciAgICA9IERhdGFMb2FkZXIodG9rZW5pemVkLCBiYXRjaF9zaXplPTQsIGNvbGxhdGVfZm49Y29sbGF0b3IsIHNodWZmbGU9VHJ1ZSlcbnByaW50KGZcIkRhdGFzZXQgc2l6ZToge2xlbih0b2tlbml6ZWQpfSwgc3RlcHMgcGVyIGVwb2NoOiB7bGVuKGxvYWRlcil9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW5zdHJ1Y3Rpb24gRGl2ZXJzaXR5IGFuZCBDYXRhc3Ryb3BoaWMgRm9yZ2V0dGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW5zdHJ1Y3Rpb24gZGl2ZXJzaXR5IOKAlCBzcGFubmluZyByZWFzb25pbmcsIGNvZGluZywgc3VtbWFyaXNhdGlvbiwgUUEsIGNyZWF0aXZlIHdyaXRpbmcsIGFuZCBkaWFsb2d1ZSDigJQgZGV0ZXJtaW5lcyB3aGV0aGVyIHRoZSBTRlQgbW9kZWwgZ2VuZXJhbGlzZXMgb3Igb3ZlcmZpdHMgdG8gYSBuYXJyb3cgZm9ybWF0LiBNb2RlbHMgZmluZS10dW5lZCBvbiBob21vZ2VuZW91cyBkYXRhc2V0cyAoZS5nLiwgb25seSBjb2RpbmcgaW5zdHJ1Y3Rpb25zKSBsb3NlIHBlcmZvcm1hbmNlIG9uIG90aGVyIHRhc2sgdHlwZXMuIENhdGFzdHJvcGhpYyBmb3JnZXR0aW5nIGlzIGEgcmVsYXRlZCBwcm9ibGVtOiBTRlQgd2l0aCBmdWxsIHBhcmFtZXRlciB1cGRhdGVzIGNhbiBkZWdyYWRlIGJhc2UgbW9kZWwgY2FwYWJpbGl0aWVzLCBwYXJ0aWN1bGFybHkgb24gdGFza3Mgbm90IHJlcHJlc2VudGVkIGluIHRoZSBTRlQgZGF0YXNldC4gTG9SQSBtaXRpZ2F0ZXMgdGhpcyBieSBrZWVwaW5nIGJhc2Ugd2VpZ2h0cyBmcm96ZW4gYW5kIHRyYWluaW5nIG9ubHkgbG93LXJhbmsgYWRhcHRlciBtYXRyaWNlcywgYWN0aW5nIGFzIGEgcmVndWxhcmlzZXIuIEVhcmx5IHN0b3BwaW5nIChtb25pdG9yIHZhbGlkYXRpb24gbG9zcyBvbiBhIGhlbGQtb3V0IGRpdmVyc2UgZXZhbCBzZXQpIGlzIGVzc2VudGlhbCBmb3Igc21hbGwgZGF0YXNldHMgd2hlcmUgb3ZlcmZpdHRpbmcgY2FuIGhhcHBlbiB3aXRoaW4gYSBzaW5nbGUgZXBvY2guIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUYXNrIHR5cGVzIHRvIGNvdmVyOiBxdWVzdGlvbiBhbnN3ZXJpbmcsIHN1bW1hcmlzYXRpb24sIGNvZGUgZ2VuZXJhdGlvbiwgdHJhbnNsYXRpb24sIGNyZWF0aXZlIHdyaXRpbmcsIHJlYXNvbmluZyBjaGFpbnMsIGRpYWxvZ3VlLCBkYXRhIGV4dHJhY3Rpb24uIiwiTGVuZ3RoIGRpdmVyc2l0eTogc2hvcnQgZmFjdHVhbCBhbnN3ZXJzICgx4oCTMiBzZW50ZW5jZXMpLCBtZWRpdW0gZXhwbGFuYXRpb25zICgx4oCTMyBwYXJhZ3JhcGhzKSwgbG9uZyBzdHJ1Y3R1cmVkIG91dHB1dHMgKGxpc3RzLCB0YWJsZXMsIGNvZGUpLiIsIkRpZmZpY3VsdHkgc3BlY3RydW06IHNpbXBsZSBsb29rdXAsIG11bHRpLXN0ZXAgcmVhc29uaW5nLCBjb25zdHJhaW50IHNhdGlzZmFjdGlvbiwgb3Blbi1lbmRlZCBnZW5lcmF0aW9uLiIsIkZvcm1hdCBkaXZlcnNpdHk6IHByb3NlLCBidWxsZXQgbGlzdHMsIG1hcmtkb3duIHdpdGggaGVhZGVycywgSlNPTiwgY29kZSB3aXRoIGV4cGxhbmF0aW9uLiIsIkxvUkEgaHlwZXJwYXJhbWV0ZXJzOiByYW5rIHI9OOKAkzY0OyBsYXJnZXIgciBjYXB0dXJlcyBtb3JlIGNhcGFjaXR5IGJ1dCByaXNrcyBvdmVyZml0dGluZzsgYWxwaGEvciByYXRpbyBvZiAyIGlzIGEgc2FmZSBkZWZhdWx0LiIsIkNhdGFzdHJvcGhpYyBmb3JnZXR0aW5nIGNoZWNrOiBldmFsdWF0ZSBvbiBNTUxVL0hlbGxhU3dhZyBiZWZvcmUgYW5kIGFmdGVyIFNGVCB0byBkZXRlY3Qga25vd2xlZGdlIGRlZ3JhZGF0aW9uLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTRlQgQ29uZmlndXJhdGlvbnMgaW4gTm90YWJsZSBNb2RlbHMifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJEYXRhc2V0IFNpemUiLCJFcG9jaHMiLCJMZWFybmluZyBSYXRlIiwiTG9SQSIsIkRhdGEgU291cmNlIl0sInJvd3MiOltbIkxMYU1BLTMtOEItSW5zdHJ1Y3QiLCJ+MTBNIHRva2VucyIsIjLigJMzIiwiMWUtNSIsIk5vIChmdWxsIEZUKSIsIkludGVybmFsIGN1cmF0ZWQgKyBwdWJsaWMgbWl4Il0sWyJNaXN0cmFsLTdCLUluc3RydWN0LXYwLjIiLCJ+MU0gZXhhbXBsZXMiLCIzIiwiMmUtNSIsIk5vIChmdWxsIEZUKSIsIlVsdHJhQ2hhdCArIHB1YmxpYyBvcGVuLXNvdXJjZSJdLFsiUGhpLTMtbWluaS1JbnN0cnVjdCIsIn4zLjNUIHByZXRyYWluICsgU0ZUIHN0YWdlIiwiMyIsIjFlLTUiLCJObyIsIlN5bnRoZXRpYyBHUFQtNC1nZW5lcmF0ZWQgaW5zdHJ1Y3Rpb25zIl0sWyJHZW1tYS03Qi1JbnN0cnVjdCIsIn4yTSBleGFtcGxlcyIsIjIiLCI1ZS02IiwiTm8iLCJGTEFOIHN1YnNldCArIHByb3ByaWV0YXJ5IGRpYWxvZ3VlIl0sWyJRd2VuMi03Qi1JbnN0cnVjdCIsIn4xLjVNIHBhaXJzIiwiMiIsIjdlLTYiLCJObyIsIlByb3ByaWV0YXJ5IG11bHRpbGluZ3VhbCBpbnN0cnVjdGlvbiBkYXRhIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkxJTUE6IExlc3MgSXMgTW9yZSBmb3IgQWxpZ25tZW50IiwiY29udGVudCI6IkxJTUEgc2hvd2VkIHRoYXQgMSwwMDAgY2FyZWZ1bGx5IGN1cmF0ZWQgZXhhbXBsZXMgb3V0cGVyZm9ybSA1MiwwMDAgbm9pc3kgQWxwYWNhIGV4YW1wbGVzIOKAlCBpbnN0cnVjdGlvbiBkaXZlcnNpdHkgKGNvdmVyaW5nIGRpZmZlcmVudCB0YXNrIHR5cGVzKSBtYXR0ZXJzIG1vcmUgdGhhbiByYXcgY291bnQgZm9yIFNGVCBxdWFsaXR5LiBBIHByZXRyYWluZWQgTExNIGFscmVhZHkgaGFzIHRoZSBrbm93bGVkZ2U7IFNGVCBtZXJlbHkgdGVhY2hlcyB0aGUgZm9ybWF0LiBJbnZlc3QgaW4gY3VyYXRpb24gYW5kIGRpdmVyc2l0eSwgbm90IGRhdGEgdm9sdW1lLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU0ZUIGlzIHRoZSBmb3VuZGF0aW9uYWwgYWxpZ25tZW50IHN0ZXAg4oCUIGl0IGNvbnZlcnRzIGEgbmV4dC10b2tlbiBwcmVkaWN0b3IgaW50byBhbiBpbnN0cnVjdGlvbiBmb2xsb3dlci4gVGhlIGtleSBpbXBsZW1lbnRhdGlvbiBkZWNpc2lvbnMgKGNoYXQgdGVtcGxhdGUsIGxvc3MgbWFza2luZywgTG9SQSB2cyBmdWxsIEZULCBkYXRhIGRpdmVyc2l0eSkgY29tcG91bmQ6IGEgbW9kZWwgd2l0aCBjb3JyZWN0IG1hc2tpbmcsIGRpdmVyc2UgZGF0YSwgYW5kIExvUkEgcmVndWxhcmlzYXRpb24gd2lsbCBnZW5lcmFsaXNlIGZhciBiZXR0ZXIgdGhhbiBvbmUgdHJhaW5lZCB3aXRoIGxhcmdlciBidXQgaG9tb2dlbmVvdXMgZGF0YSBhbmQgZnVsbC1wYXJhbWV0ZXIgdXBkYXRlcy4gU0ZUIGFsb25lIGlzIGluc3VmZmljaWVudCBmb3Igc2FmZXR5IGFuZCBoZWxwZnVsbmVzcyBvcHRpbWlzYXRpb247IGl0IGlzIHR5cGljYWxseSBmb2xsb3dlZCBieSBwcmVmZXJlbmNlIGxlYXJuaW5nIChSTEhGIG9yIERQTykgdHJhaW5lZCBvbiByZXdhcmQgc2lnbmFscyBmcm9tIGh1bWFuIG9yIEFJIGZlZWRiYWNrLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Supervised Fine-Tuning — Instruction Format, Conversation Templates, and SFT Training

Supervised fine-tuning (SFT) adapts a pretrained LLM to follow instructions by training on curated (instruction, response) pairs using causal language modelling loss restricted to the response tokens. The pretrained model already encodes world knowledge and language structure; SFT reshapes its output distribution toward helpful, formatted responses without relearning facts from scratch. Understanding the exact mechanics — chat template formatting, loss masking, gradient accumulation, and regularisation with LoRA — is prerequisite for building instruction-tuned models that generalise beyond the training distribution.

## Instruction Format and Chat Templates

Modern instruction-tuned models use a structured conversation format: a system prompt establishes the assistant persona, a user turn provides the instruction, and an assistant turn contains the expected response. Each model family defines a chat template that serialises this structure into a flat string with special tokens. LLaMA-3 uses <|begin_of_text|>, <|start_header_id|>role<|end_header_id|>\n\ncontent<|eot_id|> markers. Mistral uses [INST] ... [/INST] wrapping. Phi-3 uses <|system|>, <|user|>, <|assistant|> sentinels. The template is baked into the tokeniser and applied via tokenizer.apply_chat_template(). Mixing templates across models is a common bug that degrades instruction following silently.

## Tokenisation and Loss Masking

CLM loss is computed over all tokens by default, but for SFT only the assistant response tokens should contribute to the loss — the model is not being trained to predict the instruction. The standard approach: apply the chat template to the full conversation to get input_ids, separately tokenise the instruction portion to determine its length, then set labels[:instruction_len] = -100. HuggingFace's Trainer ignores positions with label -100 when computing cross-entropy. Getting this masking right is critical: if instruction tokens leak into the loss, the model learns to reproduce system and user turns rather than follow them.

```python
from transformers import AutoTokenizer
import torch

def format_sft_example(tokenizer, system, user, assistant, max_length=1024):
    """Apply chat template and mask instruction tokens from CLM loss."""
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
        {"role": "assistant", "content": assistant},
    ]
    # Full conversation text (including assistant response)
    full_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    # Instruction-only text to compute mask boundary
    instr_text = tokenizer.apply_chat_template(messages[:2], tokenize=False, add_generation_prompt=True)
    enc = tokenizer(full_text, max_length=max_length, truncation=True, return_tensors="pt")
    input_ids = enc.input_ids[0]
    instr_len = len(tokenizer(instr_text, add_special_tokens=False).input_ids)
    labels = input_ids.clone()
    labels[:instr_len] = -100  # no loss on instruction tokens
    return {"input_ids": input_ids, "labels": labels, "attention_mask": enc.attention_mask[0]}

# Demo
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3-8B-Instruct")
example = format_sft_example(
    tokenizer,
    system="You are a helpful assistant.",
    user="Explain backpropagation in one paragraph.",
    assistant="Backpropagation applies the chain rule in reverse through the computational graph to compute gradients of the loss wrt every parameter.",
)
print(f"input_ids shape : {example['input_ids'].shape}")
print(f"Masked tokens   : {(example['labels'] == -100).sum().item()} (instruction)")
print(f"Loss tokens     : {(example['labels'] != -100).sum().item()} (assistant response)")
```

## SFT Training Details — LR, Epochs, and Batch Size

SFT uses small learning rates (1e-5 to 5e-5) to prevent overwriting pretrained representations. Training runs for 1–3 epochs on small datasets (few thousand examples) to avoid overfitting; on larger datasets (50K+) a single epoch may suffice. Cosine learning rate decay with a short warm-up (5–10% of steps) is standard. Effective batch size is typically 128–256 sequences achieved via gradient accumulation across 8–32 physical batches, improving gradient quality on small SFT datasets. AdamW with weight decay 0.01 is the default optimizer. Unlike pretraining, SFT datasets are small enough that training time is dominated by data preprocessing and tokenisation rather than compute.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, get_cosine_schedule_with_warmup
from peft import LoraConfig, get_peft_model
import torch
from torch.optim import AdamW

def sft_train_step(model, batch, optimizer, scheduler):
    """Single SFT gradient step with LoRA; loss computed only on response tokens."""
    input_ids = batch["input_ids"].to(model.device)
    labels = batch["labels"].to(model.device)
    attention_mask = batch["attention_mask"].to(model.device)
    # HuggingFace CausalLM ignores label=-100 positions automatically
    outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
    loss = outputs.loss
    optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()
    scheduler.step()
    return loss.item()

# Attach LoRA to base model
base = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3-8B", torch_dtype=torch.bfloat16)
lora_cfg = LoraConfig(
    r=16, lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.05, bias="none", task_type="CAUSAL_LM"
)
model = get_peft_model(base, lora_cfg)
model.print_trainable_parameters()  # ~0.5% of params for r=16

optimizer = AdamW(model.parameters(), lr=2e-5, weight_decay=0.01)
scheduler = get_cosine_schedule_with_warmup(optimizer, num_warmup_steps=100, num_training_steps=3000)
print("LoRA SFT setup complete — only adapter weights update during training")
```

## Multi-Turn Conversation SFT

For multi-turn conversations, the SFT example includes multiple user and assistant exchanges. The training objective applies teacher-forcing cumulatively: given all previous turns, predict the next assistant turn. Only assistant turns contribute to the loss; all user and system turns are masked with -100. This cumulative structure means the model learns to condition its response on the full conversation history, enabling in-context coherence across turns. Packing multiple conversations into a single sequence (with document boundaries marked by end-of-sequence tokens) is common for efficiency on GPU memory.

```python
from transformers import AutoTokenizer
import torch

def collate_multiturn(tokenizer, conversation, max_length=2048):
    """Pack multi-turn conversation; compute loss only on assistant turns."""
    input_ids, labels = [], []
    for turn in conversation:
        text = tokenizer.apply_chat_template([turn], tokenize=False, add_generation_prompt=False)
        ids = tokenizer(text, add_special_tokens=False).input_ids
        if turn["role"] == "assistant":
            labels.extend(ids)          # include in loss
        else:
            labels.extend([-100] * len(ids))  # mask system/user turns
        input_ids.extend(ids)
    input_ids = torch.tensor(input_ids[:max_length])
    labels = torch.tensor(labels[:max_length])
    return {"input_ids": input_ids, "labels": labels,
            "attention_mask": torch.ones_like(input_ids)}

# Example: 3-turn conversation
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3-8B-Instruct")
conv = [
    {"role": "system",    "content": "You are a coding assistant."},
    {"role": "user",      "content": "What is a gradient?"},
    {"role": "assistant", "content": "A gradient is the vector of partial derivatives of a scalar function."},
    {"role": "user",      "content": "How is it used in training?"},
    {"role": "assistant", "content": "The gradient of the loss wrt parameters drives the parameter update in gradient descent."},
]
batch = collate_multiturn(tokenizer, conv)
print(f"Total tokens : {batch['input_ids'].shape[0]}")
print(f"Masked tokens: {(batch['labels'] == -100).sum().item()} (system+user)")
print(f"Loss tokens  : {(batch['labels'] != -100).sum().item()} (assistant turns)")
```

## Data Scale — LIMA and the Less-is-More Principle

The LIMA paper (2023) demonstrated that 1,000 carefully curated, diverse examples produce an SFT model competitive with models trained on 52,000 Alpaca examples. The key insight: a pretrained model already has the knowledge and language ability; SFT is merely teaching it the surface format of helpfulness. Raw data volume matters far less than diversity (covering different task types, domains, lengths) and quality (correct, well-structured responses). The FLAN approach goes the opposite direction — fine-tuning on 1,000+ NLP tasks in instruction format — showing that breadth generalises zero-shot. Both findings point to the same conclusion: the instruction distribution, not its size, determines SFT quality.

```python
from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorForSeq2Seq
from torch.utils.data import DataLoader

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3-8B-Instruct")
tokenizer.pad_token = tokenizer.eos_token

dataset = load_dataset("tatsu-lab/alpaca", split="train")

def preprocess(example):
    user_content = example["instruction"]
    if example.get("input"):
        user_content += "\n" + example["input"]
    messages = [
        {"role": "user",      "content": user_content},
        {"role": "assistant", "content": example["output"]},
    ]
    full = tokenizer.apply_chat_template(messages, tokenize=False)
    enc  = tokenizer(full, max_length=512, truncation=True, padding=False)
    instr = tokenizer.apply_chat_template(messages[:1], tokenize=False, add_generation_prompt=True)
    instr_len = len(tokenizer(instr, add_special_tokens=False).input_ids)
    labels = enc["input_ids"][:]
    labels[:instr_len] = [-100] * instr_len
    enc["labels"] = labels
    return enc

tokenized = dataset.map(preprocess, remove_columns=dataset.column_names, num_proc=4)
collator  = DataCollatorForSeq2Seq(tokenizer, padding=True, pad_to_multiple_of=8)
loader    = DataLoader(tokenized, batch_size=4, collate_fn=collator, shuffle=True)
print(f"Dataset size: {len(tokenized)}, steps per epoch: {len(loader)}")
```

## Instruction Diversity and Catastrophic Forgetting

Instruction diversity — spanning reasoning, coding, summarisation, QA, creative writing, and dialogue — determines whether the SFT model generalises or overfits to a narrow format. Models fine-tuned on homogeneous datasets (e.g., only coding instructions) lose performance on other task types. Catastrophic forgetting is a related problem: SFT with full parameter updates can degrade base model capabilities, particularly on tasks not represented in the SFT dataset. LoRA mitigates this by keeping base weights frozen and training only low-rank adapter matrices, acting as a regulariser. Early stopping (monitor validation loss on a held-out diverse eval set) is essential for small datasets where overfitting can happen within a single epoch.

- Task types to cover: question answering, summarisation, code generation, translation, creative writing, reasoning chains, dialogue, data extraction.
- Length diversity: short factual answers (1–2 sentences), medium explanations (1–3 paragraphs), long structured outputs (lists, tables, code).
- Difficulty spectrum: simple lookup, multi-step reasoning, constraint satisfaction, open-ended generation.
- Format diversity: prose, bullet lists, markdown with headers, JSON, code with explanation.
- LoRA hyperparameters: rank r=8–64; larger r captures more capacity but risks overfitting; alpha/r ratio of 2 is a safe default.
- Catastrophic forgetting check: evaluate on MMLU/HellaSwag before and after SFT to detect knowledge degradation.

## SFT Configurations in Notable Models

| Model | Dataset Size | Epochs | Learning Rate | LoRA | Data Source |
| --- | --- | --- | --- | --- | --- |
| LLaMA-3-8B-Instruct | ~10M tokens | 2–3 | 1e-5 | No (full FT) | Internal curated + public mix |
| Mistral-7B-Instruct-v0.2 | ~1M examples | 3 | 2e-5 | No (full FT) | UltraChat + public open-source |
| Phi-3-mini-Instruct | ~3.3T pretrain + SFT stage | 3 | 1e-5 | No | Synthetic GPT-4-generated instructions |
| Gemma-7B-Instruct | ~2M examples | 2 | 5e-6 | No | FLAN subset + proprietary dialogue |
| Qwen2-7B-Instruct | ~1.5M pairs | 2 | 7e-6 | No | Proprietary multilingual instruction data |

> **LIMA: Less Is More for Alignment**: LIMA showed that 1,000 carefully curated examples outperform 52,000 noisy Alpaca examples — instruction diversity (covering different task types) matters more than raw count for SFT quality. A pretrained LLM already has the knowledge; SFT merely teaches the format. Invest in curation and diversity, not data volume.

SFT is the foundational alignment step — it converts a next-token predictor into an instruction follower. The key implementation decisions (chat template, loss masking, LoRA vs full FT, data diversity) compound: a model with correct masking, diverse data, and LoRA regularisation will generalise far better than one trained with larger but homogeneous data and full-parameter updates. SFT alone is insufficient for safety and helpfulness optimisation; it is typically followed by preference learning (RLHF or DPO) trained on reward signals from human or AI feedback.

---

