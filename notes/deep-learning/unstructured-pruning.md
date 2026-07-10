---
title: "Unstructured Pruning — Weight Magnitude and Gradual Pruning"
slug: "unstructured-pruning"
description: "Unstructured pruning zeros individual weights by magnitude, producing sparse models. Covers global vs local pruning, the Zhu & Gupta polynomial gradual schedule, prune-retrain cycles, the PyTorch prune API, GPU acceleration limitations, and the lottery ticket hypothesis connection."
tags: ["deep-learning", "model-compression", "knowledge-distillation", "pruning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVW5zdHJ1Y3R1cmVkIHBydW5pbmcgcmVtb3ZlcyBpbmRpdmlkdWFsIHdlaWdodHMgZnJvbSBhIG5ldXJhbCBuZXR3b3JrIGJhc2VkIG9uIHRoZWlyIG1hZ25pdHVkZTogd2VpZ2h0cyB3aXRoIHNtYWxsIGFic29sdXRlIHZhbHVlcyBjb250cmlidXRlIGxpdHRsZSB0byB0aGUgbmV0d29ya1x1MDAyN3Mgb3V0cHV0IGFuZCBjYW4gYmUgemVyb2VkIHdpdGhvdXQgbGFyZ2UgYWNjdXJhY3kgbG9zcy4gVW5saWtlIHN0cnVjdHVyZWQgcHJ1bmluZywgd2hpY2ggcmVtb3ZlcyBlbnRpcmUgZmlsdGVycyBvciBsYXllcnMsIHVuc3RydWN0dXJlZCBwcnVuaW5nIGlzIGFyY2hpdGVjdHVyZS1hZ25vc3RpYyBhbmQgY2FuIGFjaGlldmUgdmVyeSBoaWdoIHNwYXJzaXR5ICg5MC05OSUpIHdpdGggc3VycHJpc2luZ2x5IHNtYWxsIGFjY3VyYWN5IGRyb3BzIHdoZW4gY29tYmluZWQgd2l0aCBhIGdyYWR1YWwgc2NoZWR1bGUgYW5kIGZpbmUtdHVuaW5nLiBUaGUgdHJhZGUtb2ZmIGlzIHRoYXQgdGhlIHJlc3VsdGluZyBzcGFyc2Ugd2VpZ2h0IG1hdHJpY2VzIGRvIG5vdCBhY2NlbGVyYXRlIGluZmVyZW5jZSBvbiBzdGFuZGFyZCBHUFUgaGFyZHdhcmUgd2l0aG91dCBzcGVjaWFsaXNlZCBzdXBwb3J0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikdsb2JhbCB2cyBMb2NhbCBNYWduaXR1ZGUgUHJ1bmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2xvYmFsIHBydW5pbmcgcmFua3MgYWxsIHdlaWdodHMgYWNyb3NzIHRoZSBlbnRpcmUgbmV0d29yayBieSB8d19pfCBhbmQgcHJ1bmVzIHRoZSBib3R0b20gcCUgcmVnYXJkbGVzcyBvZiBsYXllci4gVGhpcyBhbGxvd3Mgc3BhcnNpdHkgdG8gY29uY2VudHJhdGUgaW4gcmVkdW5kYW50IGxheWVycyDigJQgZnVsbHkgY29ubmVjdGVkIGxheWVycyB0eXBpY2FsbHkgYWNjdW11bGF0ZSBtdWNoIGhpZ2hlciBzcGFyc2l0eSB0aGFuIGNvbnZvbHV0aW9uYWwgbGF5ZXJzIHVuZGVyIGdsb2JhbCBwcnVuaW5nLiBMb2NhbCBwcnVuaW5nIGFwcGxpZXMgdGhlIHNhbWUgcmF0aW8gcCUgaW5kZXBlbmRlbnRseSB3aXRoaW4gZWFjaCBsYXllci4gTG9jYWwgcHJ1bmluZyBhdm9pZHMgbGF5ZXIgY29sbGFwc2UgKGEgc2luZ2xlIGxheWVyIGxvc2luZyB0b28gbWFueSB3ZWlnaHRzKSBidXQgaXMgbGVzcyBhY2N1cmF0ZSB0aGFuIGdsb2JhbCBwcnVuaW5nIGF0IGhpZ2ggc3BhcnNpdHkgYmVjYXVzZSBpdCBjYW5ub3QgcmVhbGxvY2F0ZSB0aGUgc3BhcnNpdHkgYnVkZ2V0IGZyb20gcmVkdW5kYW50IHRvIGltcG9ydGFudCBsYXllcnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4udXRpbHMucHJ1bmUgYXMgcHJ1bmVcblxuZGVmIGFwcGx5X2dsb2JhbF9tYWduaXR1ZGVfcHJ1bmluZyhtb2RlbDogbm4uTW9kdWxlLCBzcGFyc2l0eTogZmxvYXQpOlxuICAgIFwiXCJcIlBydW5lIGdsb2JhbGx5OiByYW5rIGFsbCB3ZWlnaHRzIHRvZ2V0aGVyLCB6ZXJvIHRoZSBib3R0b20gc3BhcnNpdHklLlwiXCJcIlxuICAgIHBhcmFtcyA9IFsobSwgXHUwMDI3d2VpZ2h0XHUwMDI3KSBmb3IgbSBpbiBtb2RlbC5tb2R1bGVzKClcbiAgICAgICAgICAgICAgIGlmIGlzaW5zdGFuY2UobSwgKG5uLkxpbmVhciwgbm4uQ29udjJkKSldXG4gICAgcHJ1bmUuZ2xvYmFsX3Vuc3RydWN0dXJlZChwYXJhbXMsIHBydW5pbmdfbWV0aG9kPXBydW5lLkwxVW5zdHJ1Y3R1cmVkLCBhbW91bnQ9c3BhcnNpdHkpXG4gICAgdG90YWwgPSBzdW0obS53ZWlnaHQubnVtZWwoKSBmb3IgbSwgXyBpbiBwYXJhbXMpXG4gICAgemVybyAgPSBzdW0oKG0ud2VpZ2h0ID09IDApLnN1bSgpLml0ZW0oKSBmb3IgbSwgXyBpbiBwYXJhbXMpXG4gICAgcHJpbnQoZlx1MDAyN0dsb2JhbCBwcnVuaW5nOiB0YXJnZXQ9e3NwYXJzaXR5Oi4wJX0gIGFjdHVhbD17emVyby90b3RhbDouMSV9ICAoe3plcm99L3t0b3RhbH0gemVyb3MpXHUwMDI3KVxuXG5kZWYgYXBwbHlfbG9jYWxfbWFnbml0dWRlX3BydW5pbmcobW9kZWw6IG5uLk1vZHVsZSwgc3BhcnNpdHk6IGZsb2F0KTpcbiAgICBcIlwiXCJQcnVuZSBsb2NhbGx5OiB6ZXJvIGJvdHRvbSBzcGFyc2l0eSUgd2l0aGluIGVhY2ggbGF5ZXIgaW5kZXBlbmRlbnRseS5cIlwiXCJcbiAgICBmb3IgbW9kdWxlIGluIG1vZGVsLm1vZHVsZXMoKTpcbiAgICAgICAgaWYgaXNpbnN0YW5jZShtb2R1bGUsIChubi5MaW5lYXIsIG5uLkNvbnYyZCkpOlxuICAgICAgICAgICAgcHJ1bmUubDFfdW5zdHJ1Y3R1cmVkKG1vZHVsZSwgbmFtZT1cdTAwMjd3ZWlnaHRcdTAwMjcsIGFtb3VudD1zcGFyc2l0eSlcbiAgICBtb2RzICA9IFttIGZvciBtIGluIG1vZGVsLm1vZHVsZXMoKSBpZiBpc2luc3RhbmNlKG0sIChubi5MaW5lYXIsIG5uLkNvbnYyZCkpXVxuICAgIHRvdGFsID0gc3VtKG0ud2VpZ2h0Lm51bWVsKCkgZm9yIG0gaW4gbW9kcylcbiAgICB6ZXJvICA9IHN1bSgobS53ZWlnaHQgPT0gMCkuc3VtKCkuaXRlbSgpIGZvciBtIGluIG1vZHMpXG4gICAgcHJpbnQoZlx1MDAyN0xvY2FsIHBydW5pbmc6ICB0YXJnZXQ9e3NwYXJzaXR5Oi4wJX0gIGFjdHVhbD17emVyby90b3RhbDouMSV9ICAoe3plcm99L3t0b3RhbH0gemVyb3MpXHUwMDI3KVxuXG5kZWYgcmVtb3ZlX21hc2tzKG1vZGVsOiBubi5Nb2R1bGUpOlxuICAgIFwiXCJcIk1ha2UgcHJ1bmluZyBwZXJtYW5lbnQgYnkgcmVtb3ZpbmcgcmVwYXJhbWV0ZXJpc2F0aW9uIG1hc2tzLlwiXCJcIlxuICAgIGZvciBtIGluIG1vZGVsLm1vZHVsZXMoKTpcbiAgICAgICAgaWYgaXNpbnN0YW5jZShtLCAobm4uTGluZWFyLCBubi5Db252MmQpKTpcbiAgICAgICAgICAgIHRyeTogcHJ1bmUucmVtb3ZlKG0sIFx1MDAyN3dlaWdodFx1MDAyNylcbiAgICAgICAgICAgIGV4Y2VwdCBWYWx1ZUVycm9yOiBwYXNzXG5cbm1vZGVsID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoNzg0LCAyNTYpLCBubi5SZUxVKCksIG5uLkxpbmVhcigyNTYsIDEwKSlcbmFwcGx5X2dsb2JhbF9tYWduaXR1ZGVfcHJ1bmluZyhtb2RlbCwgMC43KVxucmVtb3ZlX21hc2tzKG1vZGVsKVxucHJpbnQoXHUwMDI3cHJ1bmUucmVtb3ZlKCkgY29udmVydHMgd2VpZ2h0X29yaWcgKyB3ZWlnaHRfbWFzayAtXHUwMDNlIHdlaWdodCAocGVybWFuZW50KS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2VpZ2h0IERpc3RyaWJ1dGlvbiBBZnRlciBQcnVuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZWZvcmUgcHJ1bmluZywgbmV1cmFsIG5ldHdvcmsgd2VpZ2h0cyBmb2xsb3cgYW4gYXBwcm94aW1hdGVseSBHYXVzc2lhbiBkaXN0cmlidXRpb24gY2VudHJlZCBuZWFyIHplcm8uIEFmdGVyIG1hZ25pdHVkZSBwcnVuaW5nLCB0aGUgZGlzdHJpYnV0aW9uIGJlY29tZXMgYmltb2RhbDogYSBzaGFycCBzcGlrZSBhdCBleGFjdGx5IHplcm8gKHRoZSBwcnVuZWQgd2VpZ2h0cykgYW5kIGEgYnJvYWRlciBkaXN0cmlidXRpb24gb2YgbGFyZ2UtbWFnbml0dWRlIHN1cnZpdm9ycy4gVGhlIGJpbW9kYWwgc2lnbmF0dXJlIGNhbiBiZSBkZXRlY3RlZCBieSBwbG90dGluZyB3ZWlnaHQgaGlzdG9ncmFtcy4gVGhlIFB5VG9yY2ggcHJ1bmUgQVBJIGltcGxlbWVudHMgcHJ1bmluZyB2aWEgcmVwYXJhbWV0ZXJpc2F0aW9uOiBpdCBzdG9yZXMgd2VpZ2h0X29yaWcgKG9yaWdpbmFsIHZhbHVlcykgYW5kIGEgYmluYXJ5IHdlaWdodF9tYXNrLCBjb21wdXRpbmcgd2VpZ2h0ID0gd2VpZ2h0X29yaWcgKiB3ZWlnaHRfbWFzayBvbiBlYWNoIGZvcndhcmQgcGFzcy4gQ2FsbGluZyBwcnVuZS5yZW1vdmUoKSBjb2xsYXBzZXMgdGhpcyBpbnRvIGEgc2luZ2xlIHNwYXJzZSB3ZWlnaHQgdGVuc29yLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWR1YWwgUHJ1bmluZyBTY2hlZHVsZSAoWmh1IFx1MDAyNiBHdXB0YSAyMDE4KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT25lLXNob3QgcHJ1bmluZyDigJQgcmVtb3ZpbmcgYWxsIHRhcmdldCB3ZWlnaHRzIGF0IG9uY2Ug4oCUIGNhdXNlcyBhIGxhcmdlIGFjY3VyYWN5IGRyb3AgdGhhdCBmaW5lLXR1bmluZyBtYXkgbm90IHJlY292ZXIuIFpodSBcdTAwMjYgR3VwdGEgKDIwMTgpIHByb3Bvc2VkIGdyYWR1YWwgcHJ1bmluZyB3aXRoIGEgcG9seW5vbWlhbCBzY2hlZHVsZTogcyh0KSA9IHNfZiArIChzX2kgLSBzX2YpKDEgLSAodC104oKAKS8obsK3zpR0KSnCsywgd2hlcmUgdOKCgCBpcyB0aGUgc3RhcnQgc3RlcCwgbiBpcyB0aGUgbnVtYmVyIG9mIHBydW5pbmcgc3RlcHMsIGFuZCDOlHQgaXMgdGhlIHN0ZXAgaW50ZXJ2YWwuIFRoZSBjdWJpYyBwb2x5bm9taWFsIGdpdmVzIGEgc2xvdyBzdGFydCAobWluaW1hbCBlYXJseSBwcnVuaW5nKSwgYWdncmVzc2l2ZSBtaWRkbGUgcGhhc2UsIGFuZCBzbG93IGZpbmlzaCAoZmluZS1ncmFpbmVkIHR1bmluZyBhdCBoaWdoIHNwYXJzaXR5KS4gUHJ1bmluZyBpcyBhcHBsaWVkIGV2ZXJ5IM6UdCB0cmFpbmluZyBzdGVwcywgd2l0aCBub3JtYWwgZ3JhZGllbnQgdXBkYXRlcyBjb250aW51aW5nIGJldHdlZW4gc3RlcHMgc28gdGhlIG5ldHdvcmsgY2FuIHJlZGlzdHJpYnV0ZSBpbmZvcm1hdGlvbiBhZnRlciBlYWNoIHBydW5pbmcgZXZlbnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4udXRpbHMucHJ1bmUgYXMgcHJ1bmVcblxuZGVmIHBvbHlub21pYWxfc3BhcnNpdHkoc3RlcDogaW50LCB0MDogaW50LCBuX3N0ZXBzOiBpbnQsIGRlbHRhX3Q6IGludCxcbiAgICAgICAgICAgICAgICAgICAgICAgICBzX2k6IGZsb2F0ID0gMC4wLCBzX2Y6IGZsb2F0ID0gMC45KSAtXHUwMDNlIGZsb2F0OlxuICAgIFwiXCJcIlxuICAgIFpodSBcdTAwMjYgR3VwdGEgKDIwMTgpIGN1YmljIHBvbHlub21pYWwgcHJ1bmluZyBzY2hlZHVsZS5cbiAgICBzKHQpID0gc19mICsgKHNfaSAtIHNfZikgKiAoMSAtICh0IC0gdDApIC8gKG4gKiBkZWx0YV90KSleM1xuICAgIFwiXCJcIlxuICAgIGlmIHN0ZXAgXHUwMDNjIHQwOlxuICAgICAgICByZXR1cm4gMC4wXG4gICAgaWYgc3RlcCBcdTAwM2U9IHQwICsgbl9zdGVwcyAqIGRlbHRhX3Q6XG4gICAgICAgIHJldHVybiBzX2ZcbiAgICBwcm9ncmVzcyA9IChzdGVwIC0gdDApIC8gKG5fc3RlcHMgKiBkZWx0YV90KVxuICAgIHJldHVybiBzX2YgKyAoc19pIC0gc19mKSAqICgxLjAgLSBwcm9ncmVzcykgKiogM1xuXG5kZWYgZ3JhZHVhbF9wcnVuZV9zdGVwKG1vZGVsOiBubi5Nb2R1bGUsIHN0ZXA6IGludCwgdDA6IGludCxcbiAgICAgICAgICAgICAgICAgICAgICAgIG5fc3RlcHM6IGludCwgZGVsdGFfdDogaW50LCBzX2Y6IGZsb2F0ID0gMC45KTpcbiAgICBcIlwiXCJBcHBseSBwcnVuaW5nIHRvIHJlYWNoIHRoZSBzY2hlZHVsZWQgc3BhcnNpdHkgYXQgdGhpcyB0cmFpbmluZyBzdGVwLlwiXCJcIlxuICAgIGlmIHN0ZXAgJSBkZWx0YV90ICE9IDA6XG4gICAgICAgIHJldHVybiAwLjAgICMgb25seSBwcnVuZSBhdCBzY2hlZHVsZWQgaW50ZXJ2YWxzXG4gICAgY3VycmVudF9zID0gcG9seW5vbWlhbF9zcGFyc2l0eShzdGVwLCB0MCwgbl9zdGVwcywgZGVsdGFfdCwgc19mPXNfZilcbiAgICBpZiBjdXJyZW50X3MgXHUwMDNlIDA6XG4gICAgICAgIHBhcmFtcyA9IFsobSwgXHUwMDI3d2VpZ2h0XHUwMDI3KSBmb3IgbSBpbiBtb2RlbC5tb2R1bGVzKClcbiAgICAgICAgICAgICAgICAgICBpZiBpc2luc3RhbmNlKG0sIChubi5MaW5lYXIsIG5uLkNvbnYyZCkpXVxuICAgICAgICBwcnVuZS5nbG9iYWxfdW5zdHJ1Y3R1cmVkKHBhcmFtcywgcHJ1bmUuTDFVbnN0cnVjdHVyZWQsIGFtb3VudD1jdXJyZW50X3MpXG4gICAgcmV0dXJuIGN1cnJlbnRfc1xuXG4jIFZpc3VhbGlzZSBzY2hlZHVsZTogdDA9MTAwLCBuPTEwLCBkZWx0YV90PTEwMCwgc19mPTAuOVxucHJpbnQoZlx1MDAyN3tcIlN0ZXBcIjpcdTAwM2U2fSAge1wiU2NoZWR1bGVkIFNwYXJzaXR5XCI6XHUwMDNlMjB9XHUwMDI3KVxuZm9yIHN0ZXAgaW4gWzAsIDEwMCwgMjAwLCA0MDAsIDcwMCwgMTAwMCwgMTEwMCwgMTIwMF06XG4gICAgcyA9IHBvbHlub21pYWxfc3BhcnNpdHkoc3RlcCwgdDA9MTAwLCBuX3N0ZXBzPTEwLCBkZWx0YV90PTEwMCwgc19mPTAuOSlcbiAgICBwcmludChmXHUwMDI3e3N0ZXA6XHUwMDNlNn0gIHtzOlx1MDAzZTIwLjElfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcnVuZS1SZXRyYWluIEN5Y2xlcyBhbmQgV2VpZ2h0IFJlY292ZXJ5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZXR3ZWVuIGVhY2ggc2NoZWR1bGVkIHBydW5pbmcgc3RlcCwgdGhlIG5ldHdvcmsgaXMgdHJhaW5lZCBub3JtYWxseSB2aWEgYmFja3Byb3BhZ2F0aW9uLiBQcnVuZWQgd2VpZ2h0cyByZWNlaXZlIHplcm8gZ3JhZGllbnQgKHRoZXkgYXJlIG1hc2tlZCksIGJ1dCBzdXJ2aXZpbmcgd2VpZ2h0cyBjYW4gZ3JvdyBpbiBtYWduaXR1ZGUgdG8gY29tcGVuc2F0ZS4gVGhpcyByZWRpc3RyaWJ1dGlvbiBpcyB0aGUga2V5IG1lY2hhbmlzbSBiZWhpbmQgZ3JhZHVhbCBwcnVuaW5nXHUwMDI3cyBhY2N1cmFjeSBhZHZhbnRhZ2U6IHN1cnZpdmluZyB3ZWlnaHRzIHNwZWNpYWxpc2UgdG8gY292ZXIgdGhlIGZ1bmN0aW9ucyBvZiB0aGUgcmVtb3ZlZCBvbmVzLiBUaGUgbGVhcm5pbmcgcmF0ZSBkdXJpbmcgZ3JhZHVhbCBwcnVuaW5nIHNob3VsZCBiZSAxMC0zMCUgb2YgdGhlIG9yaWdpbmFsIHRyYWluaW5nIExSIOKAlCB0b28gaGlnaCBjYXVzZXMgaW5zdGFiaWxpdHkgd2hlbiB0aGUgbWFzayBzdWRkZW5seSBjaGFuZ2VzLCB0b28gbG93IHByZXZlbnRzIHJlY292ZXJ5LiBBZnRlciByZWFjaGluZyB0YXJnZXQgc3BhcnNpdHksIGEgZmluYWwgZmluZS10dW5pbmcgcGhhc2UgYXQgMSUgb2Ygb3JpZ2luYWwgTFIgcG9saXNoZXMgdGhlIHNwYXJzZSBtb2RlbC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHUFUgQWNjZWxlcmF0aW9uIExpbWl0YXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGNvbW1vbiBtaXNjb25jZXB0aW9uIGlzIHRoYXQgYSA5MCUgc3BhcnNlIG1vZGVsIHJ1bnMgMTB4IGZhc3Rlci4gVGhpcyBpcyBmYWxzZSBmb3Igc3RhbmRhcmQgR1BVIGhhcmR3YXJlLiBHUFUgbWF0cml4IG11bHRpcGxpY2F0aW9uIGlzIGltcGxlbWVudGVkIGFzIGRlbnNlIEdFTU0gdmlhIGN1QkxBUy4gQSB3ZWlnaHQgbWF0cml4IHdpdGggOTAlIHplcm9zIHN0aWxsIHBlcmZvcm1zIHRoZSBmdWxsIE3Dl0vDl04gbXVsdGlwbHktYWRkIG9wZXJhdGlvbnMg4oCUIHRoZSBoYXJkd2FyZSBkb2VzIG5vdCBza2lwIHplcm8gbXVsdGlwbGljYXRpb25zLiBaZXJvIHdlaWdodHMgYXJlIG11bHRpcGxpZWQgYnkgYWN0aXZhdGlvbnMsIHByb2R1Y2luZyB6ZXJvIHByb2R1Y3RzIHRoYXQgYWNjdW11bGF0ZSBub3JtYWxseTogd2FzdGVkIGNvbXB1dGUsIG5vdCBza2lwcGVkIGNvbXB1dGUuIFJlYWwgc3BlZWR1cCBmcm9tIHVuc3RydWN0dXJlZCBzcGFyc2l0eSByZXF1aXJlczogKDEpIE5WSURJQSBBMTAwKyB3aXRoIE46TSBzcGFyc2l0eSAoNTAlIHNwYXJzaXR5LCAyeCBzcGVlZHVwKSwgKDIpIGN1c3RvbSBTcE1NIGtlcm5lbHMgb24gQ1BVLCBvciAoMykgc3RydWN0dXJlZCBwcnVuaW5nIHRoYXQgcmVkdWNlcyBtYXRyaXggZGltZW5zaW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi51dGlscy5wcnVuZSBhcyBwcnVuZVxuaW1wb3J0IHRpbWVcblxuZGVmIHRpbWVkX2luZmVyZW5jZShtb2RlbDogbm4uTW9kdWxlLCB4OiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgICAgICBuX3dhcm11cDogaW50ID0gNSwgbl9ydW5zOiBpbnQgPSAzMCkgLVx1MDAzZSBmbG9hdDpcbiAgICBcIlwiXCJSZXR1cm4gYXZlcmFnZSBpbmZlcmVuY2UgdGltZSAobXMpIG92ZXIgbl9ydW5zIGZvcndhcmQgcGFzc2VzLlwiXCJcIlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIGlmIHguaXNfY3VkYTogdG9yY2guY3VkYS5zeW5jaHJvbml6ZSgpXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl93YXJtdXApOlxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTogXyA9IG1vZGVsKHgpXG4gICAgaWYgeC5pc19jdWRhOiB0b3JjaC5jdWRhLnN5bmNocm9uaXplKClcbiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICBmb3IgXyBpbiByYW5nZShuX3J1bnMpOlxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTogXyA9IG1vZGVsKHgpXG4gICAgaWYgeC5pc19jdWRhOiB0b3JjaC5jdWRhLnN5bmNocm9uaXplKClcbiAgICByZXR1cm4gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MCkgLyBuX3J1bnMgKiAxMDAwXG5cbmRldmljZSA9IHRvcmNoLmRldmljZShcdTAwMjdjdWRhXHUwMDI3IGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcdTAwMjdjcHVcdTAwMjcpXG5tb2RlbCAgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcigxMDI0LCAyMDQ4KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoMjA0OCwgMTApKS50byhkZXZpY2UpXG54ICAgICAgPSB0b3JjaC5yYW5kbig2NCwgMTAyNCwgZGV2aWNlPWRldmljZSlcblxuZGVuc2VfbXMgPSB0aW1lZF9pbmZlcmVuY2UobW9kZWwsIHgpXG5cbnBhcmFtcyA9IFsobSwgXHUwMDI3d2VpZ2h0XHUwMDI3KSBmb3IgbSBpbiBtb2RlbC5tb2R1bGVzKCkgaWYgaXNpbnN0YW5jZShtLCBubi5MaW5lYXIpXVxucHJ1bmUuZ2xvYmFsX3Vuc3RydWN0dXJlZChwYXJhbXMsIHBydW5lLkwxVW5zdHJ1Y3R1cmVkLCBhbW91bnQ9MC45KVxuc3BhcnNlX21zID0gdGltZWRfaW5mZXJlbmNlKG1vZGVsLCB4KVxuXG5wcmludChmXHUwMDI3RGV2aWNlOiB7ZGV2aWNlfVx1MDAyNylcbnByaW50KGZcdTAwMjdEZW5zZSBtb2RlbCAoMCUgc3BhcnNpdHkpOiAgICB7ZGVuc2VfbXM6LjNmfSBtcy9iYXRjaFx1MDAyNylcbnByaW50KGZcdTAwMjdTcGFyc2UgbW9kZWwgKDkwJSBzcGFyc2l0eSk6ICB7c3BhcnNlX21zOi4zZn0gbXMvYmF0Y2hcdTAwMjcpXG5wcmludChmXHUwMDI3U3BlZWR1cDoge2RlbnNlX21zL3NwYXJzZV9tczouMmZ9eCAgKGV4cGVjdGVkIH4xLjB4IHdpdGhvdXQgaGFyZHdhcmUgc3VwcG9ydClcdTAwMjcpXG5wcmludChcdTAwMjdVbnN0cnVjdHVyZWQgc3BhcnNpdHk6IHplcm9zIHN0aWxsIHBhcnRpY2lwYXRlIGluIGRlbnNlIG1hdG11bCBvbiBzdGFuZGFyZCBHUFUuXHUwMDI3KVxucHJpbnQoXHUwMDI3TmVlZCBOOk0gc3BhcnNpdHkgKEExMDAgU3BhcnNlIFRlbnNvciBDb3Jlcykgb3Igc3RydWN0dXJlZCBwcnVuaW5nIGZvciBzcGVlZHVwLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBY2N1cmFjeSB2cyBTcGFyc2l0eSBDdXJ2ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW1waXJpY2FsIHN0dWRpZXMgc2hvdyB0aGF0IHdpdGggZ3JhZHVhbCBtYWduaXR1ZGUgcHJ1bmluZywgUmVzTmV0LTIwIG9uIENJRkFSLTEwIG1haW50YWlucyBhY2N1cmFjeSB3aXRoaW4gMSUgb2YgdGhlIGJhc2VsaW5lIHVwIHRvIH44MCUgc3BhcnNpdHkuIEJleW9uZCA5MCUsIGFjY3VyYWN5IGRyb3BzIHN0ZWVwbHkg4oCUIHRoZSBhY2N1cmFjeSBjbGlmZi4gVGhlIGNsaWZmIGxvY2F0aW9uIGRlcGVuZHMgb24gbW9kZWwgc2l6ZTogbGFyZ2VyIG1vZGVscyAoUmVzTmV0LTUwIG9uIEltYWdlTmV0KSBtYWludGFpbiBhY2N1cmFjeSB1cCB0byA5NSUgc3BhcnNpdHkgZHVlIHRvIGhpZ2hlciBvdmVyLXBhcmFtZXRlcmlzYXRpb24uIExvY2FsIHBydW5pbmcgc2hpZnRzIHRoZSBjbGlmZiB0byBsb3dlciBzcGFyc2l0eSB0aGFuIGdsb2JhbCBwcnVuaW5nIGJlY2F1c2UgaXQgY2Fubm90IHJlYWxsb2NhdGUgdGhlIGJ1ZGdldCBmcm9tIHJlZHVuZGFudCB0byBjcml0aWNhbCBsYXllcnMuIEdyYWR1YWwgcHJ1bmluZyBleHRlbmRzIHRoZSBjbGlmZiBieSB+NSUgYWJzb2x1dGUgc3BhcnNpdHkgY29tcGFyZWQgdG8gb25lLXNob3QgcHJ1bmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgUmVzTmV0LTIwIG9uIENJRkFSLTEwOiBhY2N1cmFjeSB1bmRlciBkaWZmZXJlbnQgcHJ1bmluZyBzdHJhdGVnaWVzXG5zcGFyc2l0eSAgPSBbMC4wLCAgMC41LCAgMC43LCAgMC45LCAgMC45NSwgMC45OV1cbm1hZ19nbG9iICA9IFs5MS44LCA5MS4zLCA5MC43LCA4Ny45LCA4Mi4xLCA2MC4zXSAgIyBnbG9iYWwgbWFnbml0dWRlLCBvbmUtc2hvdFxubWFnX2xvY2FsID0gWzkxLjgsIDkwLjgsIDg5LjUsIDg0LjgsIDc2LjUsIDUxLjJdICAjIGxvY2FsIG1hZ25pdHVkZSwgb25lLXNob3RcbmdyYWR1YWwgICA9IFs5MS44LCA5MS42LCA5MS4yLCA4OS43LCA4NS40LCA2Ni44XSAgIyBncmFkdWFsIHNjaGVkdWxlIChaaHUgXHUwMDI2IEd1cHRhKVxuXG5wcmludChmXHUwMDI3e1wiU3BhcnNpdHlcIjpcdTAwM2UxMH0gIHtcIkdsb2JhbCBNYWdcIjpcdTAwM2UxMn0gIHtcIkxvY2FsIE1hZ1wiOlx1MDAzZTExfSAge1wiR3JhZHVhbFwiOlx1MDAzZTl9ICB7XCJHcmFkdWFsIEdhaW5cIjpcdTAwM2UxNH1cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNjQpXG5mb3IgcywgZywgbCwgZ3IgaW4gemlwKHNwYXJzaXR5LCBtYWdfZ2xvYiwgbWFnX2xvY2FsLCBncmFkdWFsKTpcbiAgICBnYWluID0gZ3IgLSBnXG4gICAgcHJpbnQoZlx1MDAyN3tzOlx1MDAzZTEwLjAlfSAge2c6XHUwMDNlMTIuMWZ9ICB7bDpcdTAwM2UxMS4xZn0gIHtncjpcdTAwM2U5LjFmfSAge2dhaW46XHUwMDNlKzE0LjFmfVx1MDAyNylcblxuYmFzZWxpbmUgPSBtYWdfZ2xvYlswXVxuY2xpZmZfZ2xvYmFsICA9IG5leHQoKHMgZm9yIHMsIGEgaW4gemlwKHNwYXJzaXR5LCBtYWdfZ2xvYikgIGlmIGJhc2VsaW5lIC0gYSBcdTAwM2UgMiksIE5vbmUpXG5jbGlmZl9ncmFkdWFsID0gbmV4dCgocyBmb3IgcywgYSBpbiB6aXAoc3BhcnNpdHksIGdyYWR1YWwpICAgaWYgYmFzZWxpbmUgLSBhIFx1MDAzZSAyKSwgTm9uZSlcbnByaW50KGZcdTAwMjdcXG5BY2N1cmFjeSBjbGlmZiAoXHUwMDNlMnBwIGRyb3ApOiBnbG9iYWw9e2NsaWZmX2dsb2JhbDouMCV9ICBncmFkdWFsPXtjbGlmZl9ncmFkdWFsOi4wJX1cdTAwMjcpXG5tZWFuX2JlbmVmaXQgPSBucC5tZWFuKFtnciAtIGcgZm9yIGdyLCBnIGluIHppcChncmFkdWFsWzE6XSwgbWFnX2dsb2JbMTpdKV0pXG5wcmludChmXHUwMDI3TWVhbiBhY2N1cmFjeSBiZW5lZml0IG9mIGdyYWR1YWwgb3ZlciBvbmUtc2hvdDogK3ttZWFuX2JlbmVmaXQ6LjFmfSBwcFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb3R0ZXJ5IFRpY2tldCBIeXBvdGhlc2lzIENvbm5lY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZyYW5rbGUgXHUwMDI2IENhcmxpbiAoMjAxOSkgb2JzZXJ2ZWQgdGhhdCB3aXRoaW4gYSBsYXJnZSBkZW5zZSBuZXR3b3JrIHRoZXJlIGV4aXN0IHNwYXJzZSBzdWJuZXR3b3JrcyDigJQgd2lubmluZyB0aWNrZXRzIOKAlCB0aGF0LCB3aGVuIHRyYWluZWQgZnJvbSB0aGUgb3JpZ2luYWwgd2VpZ2h0IGluaXRpYWxpc2F0aW9uLCBtYXRjaCB0aGUgZnVsbCBuZXR3b3JrXHUwMDI3cyBhY2N1cmFjeS4gVGhlc2UgYXJlIGlkZW50aWZpZWQgYnkgdHJhaW5pbmcgdGhlIGZ1bGwgbmV0d29yaywgcHJ1bmluZyB0aGUgc21hbGxlc3Qgd2VpZ2h0cywgYW5kIHJlc2V0dGluZyBzdXJ2aXZpbmcgd2VpZ2h0cyB0byB0aGVpciBpbml0aWFsIHZhbHVlcy4gQ3JpdGljYWxseSwgdGhlIGxvdHRlcnkgdGlja2V0IG11c3QgYmUgdHJhaW5lZCBmcm9tIHRoZSBzYW1lIGluaXRpYWxpc2F0aW9uIOKAlCByYW5kb21seSByZWluaXRpYWxpc2luZyB0aGUgc3Vydml2aW5nIHdlaWdodHMgZmFpbHMuIEl0ZXJhdGl2ZSBtYWduaXR1ZGUgcHJ1bmluZyAoSU1QKSBpcyB0aGUgcHJhY3RpY2FsIGFsZ29yaXRobTogcHJ1bmUgMjAlIG9mIHJlbWFpbmluZyB3ZWlnaHRzIHBlciBjeWNsZSwgcmVzZXQgdG8gb3JpZ2luYWwgaW5pdCwgcmV0cmFpbi4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoZW4gVW5zdHJ1Y3R1cmVkIFBydW5pbmcgSXMgdGhlIFJpZ2h0IENob2ljZSIsImNvbnRlbnQiOiJDaG9vc2UgdW5zdHJ1Y3R1cmVkIHBydW5pbmcgd2hlbjogKDEpIHRhcmdldGluZyBhIENQVSB3aXRoIGEgc3BhcnNlIGxpbmVhciBhbGdlYnJhIGxpYnJhcnkgKE1LTCBzcGFyc2UgQkxBUywgb25lRE5OKSwgKDIpIHlvdSBoYXZlIGFuIEExMDArIEdQVSBhbmQgY2FuIHVzZSAyOjQgTjpNIHNwYXJzaXR5IGZvciAyeCB0aHJvdWdocHV0LCAoMykgZXhwZXJpbWVudGluZyB3aXRoIGxvdHRlcnkgdGlja2V0cyBhbmQgbmVlZCBleHRyZW1lIHNwYXJzaXR5IChcdTAwM2U5MCUpIHdpdGggbWluaW1hbCBhY2N1cmFjeSBsb3NzLCBvciAoNCkgbW9kZWwgc3RvcmFnZSBhbmQgbWVtb3J5IGZvb3RwcmludCBhcmUgdGhlIGJvdHRsZW5lY2sgcmF0aGVyIHRoYW4gaW5mZXJlbmNlIGxhdGVuY3kuIEZvciByYXcgR1BVIGluZmVyZW5jZSBzcGVlZHVwIG9uIHN0YW5kYXJkIGhhcmR3YXJlLCBzdHJ1Y3R1cmVkIHBydW5pbmcgb3IgSU5UOCBxdWFudGlzYXRpb24gYXJlIG1vcmUgZWZmZWN0aXZlIGNob2ljZXMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlNwYXJzaXR5IiwiQWNjdXJhY3kgKFJlc05ldC0yMCBDSUZBUi0xMCkiLCJOb24tWmVybyBQYXJhbXMiLCJNb2RlbCBTaXplIiwiR1BVIFNwZWVkdXAiLCJDUFUgU3BlZWR1cCAoU3BNTSkiXSwicm93cyI6W1siMCUgKGRlbnNlKSIsIjkxLjglIiwiMTAwJSIsIjEuMHgiLCIxLjB4IiwiMS4weCJdLFsiNTAlIiwiOTEuMyUiLCI1MCUiLCJ+MC42eCIsIn4xLjB4IChubyBiZW5lZml0KSIsIn4xLjJ4Il0sWyI3MCUiLCI5MC43JSIsIjMwJSIsIn4wLjR4IiwifjEuMHgiLCJ+MS44eCJdLFsiOTAlIiwiODcuOSUiLCIxMCUiLCJ+MC4yeCIsIn4xLjB4IiwifjMuNXgiXSxbIjkwJSBOOk0gKEExMDApIiwiOTEuMiUiLCI1MCUgKHN0cnVjdHVyZWQpIiwifjAuNngiLCJ+Mi4weCIsIk4vQSJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHbG9iYWwgcHJ1bmluZyBjb25jZW50cmF0ZXMgc3BhcnNpdHkgaW4gb3Zlci1wYXJhbWV0ZXJpc2VkIGxheWVyczsgbG9jYWwgcHJ1bmluZyBhcHBsaWVzIGEgdW5pZm9ybSByYXRpbyBwZXIgbGF5ZXIuIiwiUHlUb3JjaCBwcnVuZSBBUEk6IHBydW5lLmwxX3Vuc3RydWN0dXJlZCBmb3IgbG9jYWwsIHBydW5lLmdsb2JhbF91bnN0cnVjdHVyZWQgZm9yIGdsb2JhbCBtYWduaXR1ZGUgcHJ1bmluZy4iLCJwcnVuZS5yZW1vdmUoKSBjb2xsYXBzZXMgd2VpZ2h0X29yaWcgKyB3ZWlnaHRfbWFzayBpbnRvIGEgc2luZ2xlIHNwYXJzZSB3ZWlnaHQgdGVuc29yIHBlcm1hbmVudGx5LiIsIlpodSBcdTAwMjYgR3VwdGEgY3ViaWMgc2NoZWR1bGU6IHNsb3cgc3RhcnQsIGFnZ3Jlc3NpdmUgbWlkZGxlLCBzbG93IGZpbmlzaCDigJQgYmV0dGVyIHRoYW4gbGluZWFyIG9yIHN0ZXAgc2NoZWR1bGVzLiIsIkFjY3VyYWN5IGNsaWZmOiBhYm92ZSB+ODAtOTAlIHNwYXJzaXR5IGZvciBtb3N0IGFyY2hpdGVjdHVyZXMsIGFjY3VyYWN5IGRyb3BzIHNoYXJwbHkgd2l0aCBtYWduaXR1ZGUgcHJ1bmluZy4iLCJMb3R0ZXJ5IHRpY2tldDogd2lubmluZyB0aWNrZXQgc3VibmV0d29ya3MgcmVxdWlyZSB0aGUgZXhhY3Qgb3JpZ2luYWwgaW5pdGlhbGlzYXRpb24g4oCUIHJhbmRvbSByZXNldCBmYWlscy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Unstructured Pruning — Weight Magnitude and Gradual Pruning

Unstructured pruning removes individual weights from a neural network based on their magnitude: weights with small absolute values contribute little to the network's output and can be zeroed without large accuracy loss. Unlike structured pruning, which removes entire filters or layers, unstructured pruning is architecture-agnostic and can achieve very high sparsity (90-99%) with surprisingly small accuracy drops when combined with a gradual schedule and fine-tuning. The trade-off is that the resulting sparse weight matrices do not accelerate inference on standard GPU hardware without specialised support.

## Global vs Local Magnitude Pruning

Global pruning ranks all weights across the entire network by |w_i| and prunes the bottom p% regardless of layer. This allows sparsity to concentrate in redundant layers — fully connected layers typically accumulate much higher sparsity than convolutional layers under global pruning. Local pruning applies the same ratio p% independently within each layer. Local pruning avoids layer collapse (a single layer losing too many weights) but is less accurate than global pruning at high sparsity because it cannot reallocate the sparsity budget from redundant to important layers.

```python
import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

def apply_global_magnitude_pruning(model: nn.Module, sparsity: float):
    """Prune globally: rank all weights together, zero the bottom sparsity%."""
    params = [(m, 'weight') for m in model.modules()
               if isinstance(m, (nn.Linear, nn.Conv2d))]
    prune.global_unstructured(params, pruning_method=prune.L1Unstructured, amount=sparsity)
    total = sum(m.weight.numel() for m, _ in params)
    zero  = sum((m.weight == 0).sum().item() for m, _ in params)
    print(f'Global pruning: target={sparsity:.0%}  actual={zero/total:.1%}  ({zero}/{total} zeros)')

def apply_local_magnitude_pruning(model: nn.Module, sparsity: float):
    """Prune locally: zero bottom sparsity% within each layer independently."""
    for module in model.modules():
        if isinstance(module, (nn.Linear, nn.Conv2d)):
            prune.l1_unstructured(module, name='weight', amount=sparsity)
    mods  = [m for m in model.modules() if isinstance(m, (nn.Linear, nn.Conv2d))]
    total = sum(m.weight.numel() for m in mods)
    zero  = sum((m.weight == 0).sum().item() for m in mods)
    print(f'Local pruning:  target={sparsity:.0%}  actual={zero/total:.1%}  ({zero}/{total} zeros)')

def remove_masks(model: nn.Module):
    """Make pruning permanent by removing reparameterisation masks."""
    for m in model.modules():
        if isinstance(m, (nn.Linear, nn.Conv2d)):
            try: prune.remove(m, 'weight')
            except ValueError: pass

model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(), nn.Linear(256, 10))
apply_global_magnitude_pruning(model, 0.7)
remove_masks(model)
print('prune.remove() converts weight_orig + weight_mask -> weight (permanent).')
```

## Weight Distribution After Pruning

Before pruning, neural network weights follow an approximately Gaussian distribution centred near zero. After magnitude pruning, the distribution becomes bimodal: a sharp spike at exactly zero (the pruned weights) and a broader distribution of large-magnitude survivors. The bimodal signature can be detected by plotting weight histograms. The PyTorch prune API implements pruning via reparameterisation: it stores weight_orig (original values) and a binary weight_mask, computing weight = weight_orig * weight_mask on each forward pass. Calling prune.remove() collapses this into a single sparse weight tensor.

## Gradual Pruning Schedule (Zhu & Gupta 2018)

One-shot pruning — removing all target weights at once — causes a large accuracy drop that fine-tuning may not recover. Zhu & Gupta (2018) proposed gradual pruning with a polynomial schedule: s(t) = s_f + (s_i - s_f)(1 - (t-t₀)/(n·Δt))³, where t₀ is the start step, n is the number of pruning steps, and Δt is the step interval. The cubic polynomial gives a slow start (minimal early pruning), aggressive middle phase, and slow finish (fine-grained tuning at high sparsity). Pruning is applied every Δt training steps, with normal gradient updates continuing between steps so the network can redistribute information after each pruning event.

```python
import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

def polynomial_sparsity(step: int, t0: int, n_steps: int, delta_t: int,
                         s_i: float = 0.0, s_f: float = 0.9) -> float:
    """
    Zhu & Gupta (2018) cubic polynomial pruning schedule.
    s(t) = s_f + (s_i - s_f) * (1 - (t - t0) / (n * delta_t))^3
    """
    if step < t0:
        return 0.0
    if step >= t0 + n_steps * delta_t:
        return s_f
    progress = (step - t0) / (n_steps * delta_t)
    return s_f + (s_i - s_f) * (1.0 - progress) ** 3

def gradual_prune_step(model: nn.Module, step: int, t0: int,
                        n_steps: int, delta_t: int, s_f: float = 0.9):
    """Apply pruning to reach the scheduled sparsity at this training step."""
    if step % delta_t != 0:
        return 0.0  # only prune at scheduled intervals
    current_s = polynomial_sparsity(step, t0, n_steps, delta_t, s_f=s_f)
    if current_s > 0:
        params = [(m, 'weight') for m in model.modules()
                   if isinstance(m, (nn.Linear, nn.Conv2d))]
        prune.global_unstructured(params, prune.L1Unstructured, amount=current_s)
    return current_s

# Visualise schedule: t0=100, n=10, delta_t=100, s_f=0.9
print(f'{"Step":>6}  {"Scheduled Sparsity":>20}')
for step in [0, 100, 200, 400, 700, 1000, 1100, 1200]:
    s = polynomial_sparsity(step, t0=100, n_steps=10, delta_t=100, s_f=0.9)
    print(f'{step:>6}  {s:>20.1%}')
```

## Prune-Retrain Cycles and Weight Recovery

Between each scheduled pruning step, the network is trained normally via backpropagation. Pruned weights receive zero gradient (they are masked), but surviving weights can grow in magnitude to compensate. This redistribution is the key mechanism behind gradual pruning's accuracy advantage: surviving weights specialise to cover the functions of the removed ones. The learning rate during gradual pruning should be 10-30% of the original training LR — too high causes instability when the mask suddenly changes, too low prevents recovery. After reaching target sparsity, a final fine-tuning phase at 1% of original LR polishes the sparse model.

## GPU Acceleration Limitations

A common misconception is that a 90% sparse model runs 10x faster. This is false for standard GPU hardware. GPU matrix multiplication is implemented as dense GEMM via cuBLAS. A weight matrix with 90% zeros still performs the full M×K×N multiply-add operations — the hardware does not skip zero multiplications. Zero weights are multiplied by activations, producing zero products that accumulate normally: wasted compute, not skipped compute. Real speedup from unstructured sparsity requires: (1) NVIDIA A100+ with N:M sparsity (50% sparsity, 2x speedup), (2) custom SpMM kernels on CPU, or (3) structured pruning that reduces matrix dimensions.

```python
import torch
import torch.nn as nn
import torch.nn.utils.prune as prune
import time

def timed_inference(model: nn.Module, x: torch.Tensor,
                     n_warmup: int = 5, n_runs: int = 30) -> float:
    """Return average inference time (ms) over n_runs forward passes."""
    model.eval()
    if x.is_cuda: torch.cuda.synchronize()
    for _ in range(n_warmup):
        with torch.no_grad(): _ = model(x)
    if x.is_cuda: torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(n_runs):
        with torch.no_grad(): _ = model(x)
    if x.is_cuda: torch.cuda.synchronize()
    return (time.perf_counter() - t0) / n_runs * 1000

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model  = nn.Sequential(nn.Linear(1024, 2048), nn.ReLU(), nn.Linear(2048, 10)).to(device)
x      = torch.randn(64, 1024, device=device)

dense_ms = timed_inference(model, x)

params = [(m, 'weight') for m in model.modules() if isinstance(m, nn.Linear)]
prune.global_unstructured(params, prune.L1Unstructured, amount=0.9)
sparse_ms = timed_inference(model, x)

print(f'Device: {device}')
print(f'Dense model (0% sparsity):    {dense_ms:.3f} ms/batch')
print(f'Sparse model (90% sparsity):  {sparse_ms:.3f} ms/batch')
print(f'Speedup: {dense_ms/sparse_ms:.2f}x  (expected ~1.0x without hardware support)')
print('Unstructured sparsity: zeros still participate in dense matmul on standard GPU.')
print('Need N:M sparsity (A100 Sparse Tensor Cores) or structured pruning for speedup.')
```

## Accuracy vs Sparsity Curve

Empirical studies show that with gradual magnitude pruning, ResNet-20 on CIFAR-10 maintains accuracy within 1% of the baseline up to ~80% sparsity. Beyond 90%, accuracy drops steeply — the accuracy cliff. The cliff location depends on model size: larger models (ResNet-50 on ImageNet) maintain accuracy up to 95% sparsity due to higher over-parameterisation. Local pruning shifts the cliff to lower sparsity than global pruning because it cannot reallocate the budget from redundant to critical layers. Gradual pruning extends the cliff by ~5% absolute sparsity compared to one-shot pruning.

```python
import numpy as np

# ResNet-20 on CIFAR-10: accuracy under different pruning strategies
sparsity  = [0.0,  0.5,  0.7,  0.9,  0.95, 0.99]
mag_glob  = [91.8, 91.3, 90.7, 87.9, 82.1, 60.3]  # global magnitude, one-shot
mag_local = [91.8, 90.8, 89.5, 84.8, 76.5, 51.2]  # local magnitude, one-shot
gradual   = [91.8, 91.6, 91.2, 89.7, 85.4, 66.8]  # gradual schedule (Zhu & Gupta)

print(f'{"Sparsity":>10}  {"Global Mag":>12}  {"Local Mag":>11}  {"Gradual":>9}  {"Gradual Gain":>14}')
print('-' * 64)
for s, g, l, gr in zip(sparsity, mag_glob, mag_local, gradual):
    gain = gr - g
    print(f'{s:>10.0%}  {g:>12.1f}  {l:>11.1f}  {gr:>9.1f}  {gain:>+14.1f}')

baseline = mag_glob[0]
cliff_global  = next((s for s, a in zip(sparsity, mag_glob)  if baseline - a > 2), None)
cliff_gradual = next((s for s, a in zip(sparsity, gradual)   if baseline - a > 2), None)
print(f'\nAccuracy cliff (>2pp drop): global={cliff_global:.0%}  gradual={cliff_gradual:.0%}')
mean_benefit = np.mean([gr - g for gr, g in zip(gradual[1:], mag_glob[1:])])
print(f'Mean accuracy benefit of gradual over one-shot: +{mean_benefit:.1f} pp')
```

## Lottery Ticket Hypothesis Connection

Frankle & Carlin (2019) observed that within a large dense network there exist sparse subnetworks — winning tickets — that, when trained from the original weight initialisation, match the full network's accuracy. These are identified by training the full network, pruning the smallest weights, and resetting surviving weights to their initial values. Critically, the lottery ticket must be trained from the same initialisation — randomly reinitialising the surviving weights fails. Iterative magnitude pruning (IMP) is the practical algorithm: prune 20% of remaining weights per cycle, reset to original init, retrain.

> **When Unstructured Pruning Is the Right Choice**: Choose unstructured pruning when: (1) targeting a CPU with a sparse linear algebra library (MKL sparse BLAS, oneDNN), (2) you have an A100+ GPU and can use 2:4 N:M sparsity for 2x throughput, (3) experimenting with lottery tickets and need extreme sparsity (>90%) with minimal accuracy loss, or (4) model storage and memory footprint are the bottleneck rather than inference latency. For raw GPU inference speedup on standard hardware, structured pruning or INT8 quantisation are more effective choices.

| Sparsity | Accuracy (ResNet-20 CIFAR-10) | Non-Zero Params | Model Size | GPU Speedup | CPU Speedup (SpMM) |
| --- | --- | --- | --- | --- | --- |
| 0% (dense) | 91.8% | 100% | 1.0x | 1.0x | 1.0x |
| 50% | 91.3% | 50% | ~0.6x | ~1.0x (no benefit) | ~1.2x |
| 70% | 90.7% | 30% | ~0.4x | ~1.0x | ~1.8x |
| 90% | 87.9% | 10% | ~0.2x | ~1.0x | ~3.5x |
| 90% N:M (A100) | 91.2% | 50% (structured) | ~0.6x | ~2.0x | N/A |

- Global pruning concentrates sparsity in over-parameterised layers; local pruning applies a uniform ratio per layer.
- PyTorch prune API: prune.l1_unstructured for local, prune.global_unstructured for global magnitude pruning.
- prune.remove() collapses weight_orig + weight_mask into a single sparse weight tensor permanently.
- Zhu & Gupta cubic schedule: slow start, aggressive middle, slow finish — better than linear or step schedules.
- Accuracy cliff: above ~80-90% sparsity for most architectures, accuracy drops sharply with magnitude pruning.
- Lottery ticket: winning ticket subnetworks require the exact original initialisation — random reset fails.

---

