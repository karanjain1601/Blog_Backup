---
title: "Reward Modeling — Bradley-Terry Model and Pairwise Preference Learning"
slug: "reward-modeling"
description: "Covers reward model training on pairwise preference data using the Bradley-Terry model and log-sigmoid loss, RM architecture (pretrained LLM backbone with scalar head), preference dataset creation from human comparisons, pairwise accuracy and margin evaluation, reward hacking detection via score distribution monitoring, and comparison of InstructGPT, Anthropic, Llama-3, Zephyr, and Nemotron reward models."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSByZXdhcmQgbW9kZWwgKFJNKSBpcyBhIG5ldXJhbCBuZXR3b3JrIHRyYWluZWQgdG8gcHJlZGljdCB3aGljaCBvZiB0d28gcmVzcG9uc2VzIGEgaHVtYW4gd291bGQgcHJlZmVyLCBnaXZlbiB0aGUgc2FtZSBwcm9tcHQuIEl0IGNvbnZlcnRzIHF1YWxpdGF0aXZlIGh1bWFuIGp1ZGdlbWVudHMgaW50byBhIHNjYWxhciBzaWduYWwgdGhhdCBkb3duc3RyZWFtIHRyYWluaW5nIChSTEhGLCBiZXN0LW9mLU4gc2FtcGxpbmcpIGNhbiBvcHRpbWlzZS4gVGhlIFJNIGlzIHRoZSBjcml0aWNhbCBib3R0bGVuZWNrIGluIHRoZSBSTEhGIHBpcGVsaW5lOiBpdHMgZXJyb3JzIGNvbXBvdW5kIOKAlCBhIGJpYXNlZCBSTSBwcm9kdWNlcyBiaWFzZWQgcG9saWN5IHVwZGF0ZXMsIGFuZCB0aGUgcG9saWN5IGlzIHRoZW4gdHJhaW5lZCB0byBleHBsb2l0IFJNIHdlYWtuZXNzZXMgKHJld2FyZCBoYWNraW5nKS4gVW5kZXJzdGFuZGluZyB0aGUgQnJhZGxleS1UZXJyeSBsb3NzLCBSTSBhcmNoaXRlY3R1cmUsIGRhdGEgY29sbGVjdGlvbiwgZXZhbHVhdGlvbiwgYW5kIGJpYXMgbWl0aWdhdGlvbiBpcyBlc3NlbnRpYWwgZm9yIGFueW9uZSBidWlsZGluZyBSTEhGIG9yIHByZWZlcmVuY2UtbGVhcm5pbmcgc3lzdGVtcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCcmFkbGV5LVRlcnJ5IE1vZGVsIGFuZCBQYWlyd2lzZSBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQnJhZGxleS1UZXJyeSBtb2RlbCBwcm92aWRlcyBhIHByaW5jaXBsZWQgcHJvYmFiaWxpc3RpYyBmb3VuZGF0aW9uIGZvciBwYWlyd2lzZSBwcmVmZXJlbmNlIGxlYXJuaW5nLiBHaXZlbiBwcm9tcHQgeCwgY2hvc2VuIHJlc3BvbnNlIHlfdywgYW5kIHJlamVjdGVkIHJlc3BvbnNlIHlfbCwgdGhlIHByb2JhYmlsaXR5IHRoYXQgYSBodW1hbiBwcmVmZXJzIHlfdyBpcyBtb2RlbGxlZCBhcyBQKHlfdyBcdTAwM2UgeV9sIHwgeCkgPSDPgyhyKHgsIHlfdykg4oiSIHIoeCwgeV9sKSkgd2hlcmUgz4MgaXMgdGhlIHNpZ21vaWQgZnVuY3Rpb24gYW5kIHIgaXMgdGhlIHNjYWxhciByZXdhcmQgZnVuY3Rpb24uIFRoZSBSTSBsb3NzIGlzIHRoZSBuZWdhdGl2ZSBsb2ctbGlrZWxpaG9vZCBvZiBvYnNlcnZlZCBwcmVmZXJlbmNlczogTCA9IOKIkkVbbG9nIM+DKHJfdyDiiJIgcl9sKV0uIE1pbmltaXNpbmcgdGhpcyBsb3NzIHB1c2hlcyByKHgsIHlfdykgdG8gYmUgbGFyZ2VyIHRoYW4gcih4LCB5X2wpIGJ5IGFuIGFtb3VudCBwcm9wb3J0aW9uYWwgdG8gaG93IGNvbmZpZGVudGx5IHRoZSBtb2RlbCBhc3NpZ25zIHRoZSBwcmVmZXJlbmNlLiBUaGUgbWFyZ2luIHJfdyDiiJIgcl9sIGlzIHRoZSBrZXkgcXVhbnRpdHk6IGxhcmdlIHBvc2l0aXZlIG1hcmdpbnMgaW5kaWNhdGUgaGlnaC1jb25maWRlbmNlIGNvcnJlY3QgcHJlZmVyZW5jZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmV3YXJkIE1vZGVsIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFJNIGlzIGluaXRpYWxpc2VkIGZyb20gYSBwcmV0cmFpbmVkIExMTSAob2Z0ZW4gdGhlIFNGVCBtb2RlbCkgd2l0aCBpdHMgbGFuZ3VhZ2UgbW9kZWxsaW5nIGhlYWQgcmVwbGFjZWQgYnkgYSBzaW5nbGUgbGluZWFyIGxheWVyIHRoYXQgb3V0cHV0cyBhIHNjYWxhciByZXdhcmQuIFRoZSBiYWNrYm9uZSBwcm9jZXNzZXMgdGhlIGZ1bGwgcHJvbXB0LXBsdXMtcmVzcG9uc2Ugc2VxdWVuY2UsIGFuZCB0aGUgc2NhbGFyIGhlYWQgcG9vbHMgdGhlIGZpbmFsIGhpZGRlbiBzdGF0ZSBhdCB0aGUgbGFzdCBub24tcGFkZGluZyB0b2tlbiBwb3NpdGlvbi4gVXNpbmcgdGhlIGxhc3QgdG9rZW4gY2FwdHVyZXMgdGhlIGN1bXVsYXRpdmUgY29udGV4dCBvZiB0aGUgZW50aXJlIHJlc3BvbnNlLiBJbml0aWFsaXNpbmcgZnJvbSB0aGUgU0ZUIG1vZGVsIChyYXRoZXIgdGhhbiB0aGUgcmF3IHByZXRyYWluZWQgbW9kZWwpIGlzIGltcG9ydGFudCDigJQgdGhlIFNGVCBtb2RlbCBhbHJlYWR5IHNwZWFrcyBpbnN0cnVjdGlvbi1mb2xsb3dpbmcgbGFuZ3VhZ2UsIHNvIGl0IHJlcXVpcmVzIGxlc3MgZGF0YSB0byBsZWFybiBwcmVmZXJlbmNlIGRpc3RpbmN0aW9ucy4gUk0gc2l6ZSB0eXBpY2FsbHkgbWF0Y2hlcyBvciBpcyBsYXJnZXIgdGhhbiB0aGUgcG9saWN5IG1vZGVsIHRvIGFjdCBhcyBhbiBhY2N1cmF0ZSBjcml0aWMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsRm9yQ2F1c2FsTE0sIEF1dG9Ub2tlbml6ZXJcblxuY2xhc3MgUmV3YXJkTW9kZWwobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmFzZV9tb2RlbF9uYW1lLCBkdHlwZT10b3JjaC5iZmxvYXQxNik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmJhY2tib25lID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKGJhc2VfbW9kZWxfbmFtZSwgdG9yY2hfZHR5cGU9ZHR5cGUpXG4gICAgICAgIGRfbW9kZWwgPSBzZWxmLmJhY2tib25lLmNvbmZpZy5oaWRkZW5fc2l6ZVxuICAgICAgICBzZWxmLmJhY2tib25lLmxtX2hlYWQgPSBubi5JZGVudGl0eSgpICAjIHJlbW92ZSB0b2tlbiBwcmVkaWN0aW9uIGhlYWRcbiAgICAgICAgc2VsZi5yZXdhcmRfaGVhZCA9IG5uLkxpbmVhcihkX21vZGVsLCAxLCBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgaW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzayk6XG4gICAgICAgIG91dCA9IHNlbGYuYmFja2JvbmUoaW5wdXRfaWRzPWlucHV0X2lkcywgYXR0ZW50aW9uX21hc2s9YXR0ZW50aW9uX21hc2ssIG91dHB1dF9oaWRkZW5fc3RhdGVzPVRydWUpXG4gICAgICAgIGxhc3RfaGlkZGVuID0gb3V0LmhpZGRlbl9zdGF0ZXNbLTFdICAgICAgICAgICMgKEIsIFQsIGRfbW9kZWwpXG4gICAgICAgIHNlcV9sZW5zID0gYXR0ZW50aW9uX21hc2suc3VtKGRpbT0xKSAtIDEgICAgIyBpbmRleCBvZiBsYXN0IHJlYWwgdG9rZW5cbiAgICAgICAgYmF0Y2hfaWR4ID0gdG9yY2guYXJhbmdlKGxhc3RfaGlkZGVuLnNpemUoMCksIGRldmljZT1sYXN0X2hpZGRlbi5kZXZpY2UpXG4gICAgICAgIHBvb2xlZCA9IGxhc3RfaGlkZGVuW2JhdGNoX2lkeCwgc2VxX2xlbnNdICAgIyAoQiwgZF9tb2RlbClcbiAgICAgICAgcmV0dXJuIHNlbGYucmV3YXJkX2hlYWQocG9vbGVkKS5zcXVlZXplKC0xKSAjIChCLClcblxuZGVmIGJyYWRsZXlfdGVycnlfbG9zcyhyX2Nob3Nlbiwgcl9yZWplY3RlZCk6XG4gICAgXCJcIlwiTCA9IC1FW2xvZyBzaWdtYShyX3cgLSByX2wpXSwgdGhlIHBhaXJ3aXNlIEJyYWRsZXktVGVycnkgbG9zcy5cIlwiXCJcbiAgICByZXR1cm4gLXRvcmNoLm5uLmZ1bmN0aW9uYWwubG9nc2lnbW9pZChyX2Nob3NlbiAtIHJfcmVqZWN0ZWQpLm1lYW4oKVxuXG5kZWYgcm1fdHJhaW5fc3RlcChtb2RlbCwgY2hvc2VuX2JhdGNoLCByZWplY3RlZF9iYXRjaCwgb3B0aW1pemVyKTpcbiAgICByX3cgPSBtb2RlbCgqKmNob3Nlbl9iYXRjaClcbiAgICByX2wgPSBtb2RlbCgqKnJlamVjdGVkX2JhdGNoKVxuICAgIGxvc3MgPSBicmFkbGV5X3RlcnJ5X2xvc3Mocl93LCByX2wpXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgdG9yY2gubm4udXRpbHMuY2xpcF9ncmFkX25vcm1fKG1vZGVsLnBhcmFtZXRlcnMoKSwgMS4wKVxuICAgIG9wdGltaXplci5zdGVwKClcbiAgICBhY2N1cmFjeSA9IChyX3cgXHUwMDNlIHJfbCkuZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG4gICAgbWFyZ2luICAgPSAocl93IC0gcl9sKS5tZWFuKCkuaXRlbSgpXG4gICAgcmV0dXJuIHtcImxvc3NcIjogbG9zcy5pdGVtKCksIFwiYWNjdXJhY3lcIjogYWNjdXJhY3ksIFwibWFyZ2luXCI6IG1hcmdpbn0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmVmZXJlbmNlIERhdGFzZXQgQ3JlYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJNIHRyYWluaW5nIHJlcXVpcmVzIHBhaXJ3aXNlIGNvbXBhcmlzb24gZGF0YTogZm9yIGVhY2ggcHJvbXB0LCBhdCBsZWFzdCB0d28gcmVzcG9uc2VzIGFyZSBnZW5lcmF0ZWQgYW5kIGEgaHVtYW4gbGFiZWxsZXIgc2VsZWN0cyB0aGUgcHJlZmVycmVkIG9uZS4gSW4gcHJhY3RpY2UsIGxhYmVsbGVycyBjb21wYXJlIDLigJM4IGNvbXBsZXRpb25zIHBlciBwcm9tcHQgYW5kIHJhbmsgdGhlbSDigJQgdGhpcyB5aWVsZHMgTyhrwrIpIHBhaXJzIGZyb20gayBjb21wbGV0aW9ucywgbWFraW5nIGNvbXBhcmlzb24gbW9yZSBlZmZpY2llbnQgdGhhbiBhYnNvbHV0ZSBzY29yaW5nLiBMYWJlbGxlciBhZ3JlZW1lbnQgaXMgdHlwaWNhbGx5IDcw4oCTODAlIChpbnRlci1hbm5vdGF0b3IgYWdyZWVtZW50KSwgc2V0dGluZyB0aGUgdXBwZXIgYm91bmQgb24gUk0gYWNjdXJhY3kuIFRoZSBBbnRocm9waWMgSEgtUkxIRiBkYXRhc2V0IChoZWxwZnVsbmVzcyArIGhhcm1sZXNzbmVzcykgYW5kIE9wZW5BSVx1MDAyN3MgSW5zdHJ1Y3RHUFQgY29tcGFyaXNvbnMgYXJlIHRoZSBtb3N0IHdpZGVseSB1c2VkIHB1YmxpYyBkYXRhc2V0cy4gRGF0YSBzY2FsZSByYW5nZXMgZnJvbSAxMEsgcGFpcnMgKHNtYWxsIGludGVybmFsIFJNKSB0byAxTSsgKHByb2R1Y3Rpb24gc3lzdGVtcyBsaWtlIEluc3RydWN0R1BUIG9yIENsYXVkZVx1MDAyN3MgUk0pLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIGRhdGFzZXRzIGltcG9ydCBsb2FkX2RhdGFzZXRcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvVG9rZW5pemVyXG5pbXBvcnQgdG9yY2hcblxuZGVmIGZvcm1hdF9wcmVmZXJlbmNlX3BhaXIodG9rZW5pemVyLCBwcm9tcHQsIGNob3NlbiwgcmVqZWN0ZWQsIG1heF9sZW5ndGg9NTEyKTpcbiAgICBcIlwiXCJUb2tlbml6ZSBjaG9zZW4gYW5kIHJlamVjdGVkIHJlc3BvbnNlcyBmb3IgQnJhZGxleS1UZXJyeSBSTSB0cmFpbmluZy5cIlwiXCJcbiAgICBkZWYgZW5jb2RlKHJlc3BvbnNlKTpcbiAgICAgICAgdGV4dCA9IGZcIkh1bWFuOiB7cHJvbXB0fVxcblxcbkFzc2lzdGFudDoge3Jlc3BvbnNlfVwiXG4gICAgICAgIGVuYyAgPSB0b2tlbml6ZXIodGV4dCwgbWF4X2xlbmd0aD1tYXhfbGVuZ3RoLCB0cnVuY2F0aW9uPVRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgcGFkZGluZz1cIm1heF9sZW5ndGhcIiwgcmV0dXJuX3RlbnNvcnM9XCJwdFwiKVxuICAgICAgICByZXR1cm4gZW5jW1wiaW5wdXRfaWRzXCJdWzBdLCBlbmNbXCJhdHRlbnRpb25fbWFza1wiXVswXVxuXG4gICAgY2hvc2VuX2lkcywgICBjaG9zZW5fbWFzayAgID0gZW5jb2RlKGNob3NlbilcbiAgICByZWplY3RlZF9pZHMsIHJlamVjdGVkX21hc2sgPSBlbmNvZGUocmVqZWN0ZWQpXG4gICAgcmV0dXJuIHtcbiAgICAgICAgXCJjaG9zZW5faW5wdXRfaWRzXCI6ICAgICAgIGNob3Nlbl9pZHMsXG4gICAgICAgIFwiY2hvc2VuX2F0dGVudGlvbl9tYXNrXCI6ICBjaG9zZW5fbWFzayxcbiAgICAgICAgXCJyZWplY3RlZF9pbnB1dF9pZHNcIjogICAgIHJlamVjdGVkX2lkcyxcbiAgICAgICAgXCJyZWplY3RlZF9hdHRlbnRpb25fbWFza1wiOiByZWplY3RlZF9tYXNrLFxuICAgIH1cblxudG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQoXCJtZXRhLWxsYW1hL0xsYW1hLTMtOEJcIilcbnRva2VuaXplci5wYWRfdG9rZW4gPSB0b2tlbml6ZXIuZW9zX3Rva2VuXG5cbmRhdGFzZXQgPSBsb2FkX2RhdGFzZXQoXCJBbnRocm9waWMvaGgtcmxoZlwiLCBzcGxpdD1cInRyYWluWzo1MDAwXVwiKVxuXG5kZWYgcHJlcHJvY2VzcyhleCk6XG4gICAgIyBISC1STEhGIGZvcm1hdDogY2hvc2VuIGFuZCByZWplY3RlZCBhcmUgZnVsbCBjb252ZXJzYXRpb24gc3RyaW5nc1xuICAgIHByb21wdCAgID0gZXhbXCJjaG9zZW5cIl0ucnNwbGl0KFwiQXNzaXN0YW50OlwiLCAxKVswXS5zdHJpcCgpXG4gICAgY2hvc2VuX3IgPSBleFtcImNob3NlblwiXS5yc3BsaXQoXCJBc3Npc3RhbnQ6XCIsIDEpWy0xXS5zdHJpcCgpXG4gICAgcmVqZWN0ZWRfciA9IGV4W1wicmVqZWN0ZWRcIl0ucnNwbGl0KFwiQXNzaXN0YW50OlwiLCAxKVstMV0uc3RyaXAoKVxuICAgIHJldHVybiBmb3JtYXRfcHJlZmVyZW5jZV9wYWlyKHRva2VuaXplciwgcHJvbXB0LCBjaG9zZW5fciwgcmVqZWN0ZWRfcilcblxudG9rZW5pemVkID0gZGF0YXNldC5tYXAocHJlcHJvY2VzcywgcmVtb3ZlX2NvbHVtbnM9ZGF0YXNldC5jb2x1bW5fbmFtZXMpXG5wcmludChmXCJQcmVmZXJlbmNlIHBhaXJzIHRva2VuaXplZDoge2xlbih0b2tlbml6ZWQpfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJNIEV2YWx1YXRpb24g4oCUIEFjY3VyYWN5LCBNYXJnaW4sIGFuZCBDYWxpYnJhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHByaW1hcnkgUk0gZXZhbHVhdGlvbiBtZXRyaWMgaXMgcGFpcndpc2UgYWNjdXJhY3k6IHRoZSBmcmFjdGlvbiBvZiBoZWxkLW91dCBwYWlycyB3aGVyZSB0aGUgUk0gYXNzaWducyBhIGhpZ2hlciByZXdhcmQgdG8gdGhlIGNob3NlbiByZXNwb25zZS4gUmFuZG9tIGNoYW5jZSBpcyA1MCU7IGEgd2VsbC10cmFpbmVkIFJNIGFjaGlldmVzIDcw4oCTODUlIGRlcGVuZGluZyBvbiBkYXRhIHF1YWxpdHkgYW5kIG1vZGVsIHNpemUuIFRoZSBtZWFuIHJld2FyZCBtYXJnaW4gKHJfdyDiiJIgcl9sKSBtZWFzdXJlcyBzZXBhcmFiaWxpdHkg4oCUIGxhcmdlciBtYXJnaW5zIGluZGljYXRlIG1vcmUgY29uZmlkZW50LCBjYWxpYnJhdGVkIHByZWRpY3Rpb25zLiBDYWxpYnJhdGlvbiBhc3Nlc3NtZW50IGNoZWNrcyB3aGV0aGVyIHRoZSBSTVx1MDAyN3Mgd2luIHByb2JhYmlsaXR5IM+DKHJfdyDiiJIgcl9sKSBtYXRjaGVzIGVtcGlyaWNhbCB3aW4gcmF0ZXM6IGEgUk0gcHJlZGljdGluZyA4MCUgd2luIHJhdGUgc2hvdWxkIGJlIGNvcnJlY3QgODAlIG9mIHRoZSB0aW1lLiBSZXdhcmRCZW5jaCBpcyB0aGUgc3RhbmRhcmQgYmVuY2htYXJrIGZvciBjb21wYXJpbmcgUk1zIGFjcm9zcyBoZWxwZnVsbmVzcywgc2FmZXR5LCBhbmQgcmVhc29uaW5nIGF4ZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBldmFsdWF0ZV9yZXdhcmRfbW9kZWwobW9kZWwsIGV2YWxfbG9hZGVyLCBkZXZpY2U9XCJjdWRhXCIpOlxuICAgIFwiXCJcIkNvbXB1dGUgcGFpcndpc2UgYWNjdXJhY3ksIG1lYW4gbWFyZ2luLCBhbmQgc2NvcmUgZGlzdHJpYnV0aW9uIHN0YXRpc3RpY3MuXCJcIlwiXG4gICAgbW9kZWwuZXZhbCgpXG4gICAgcl9jaG9zZW5fYWxsLCByX3JlamVjdGVkX2FsbCA9IFtdLCBbXVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgYmF0Y2ggaW4gZXZhbF9sb2FkZXI6XG4gICAgICAgICAgICByX3cgPSBtb2RlbChcbiAgICAgICAgICAgICAgICBpbnB1dF9pZHM9YmF0Y2hbXCJjaG9zZW5faW5wdXRfaWRzXCJdLnRvKGRldmljZSksXG4gICAgICAgICAgICAgICAgYXR0ZW50aW9uX21hc2s9YmF0Y2hbXCJjaG9zZW5fYXR0ZW50aW9uX21hc2tcIl0udG8oZGV2aWNlKVxuICAgICAgICAgICAgKVxuICAgICAgICAgICAgcl9sID0gbW9kZWwoXG4gICAgICAgICAgICAgICAgaW5wdXRfaWRzPWJhdGNoW1wicmVqZWN0ZWRfaW5wdXRfaWRzXCJdLnRvKGRldmljZSksXG4gICAgICAgICAgICAgICAgYXR0ZW50aW9uX21hc2s9YmF0Y2hbXCJyZWplY3RlZF9hdHRlbnRpb25fbWFza1wiXS50byhkZXZpY2UpXG4gICAgICAgICAgICApXG4gICAgICAgICAgICByX2Nob3Nlbl9hbGwuZXh0ZW5kKHJfdy5jcHUoKS5mbG9hdCgpLnRvbGlzdCgpKVxuICAgICAgICAgICAgcl9yZWplY3RlZF9hbGwuZXh0ZW5kKHJfbC5jcHUoKS5mbG9hdCgpLnRvbGlzdCgpKVxuICAgIHJ3ID0gbnAuYXJyYXkocl9jaG9zZW5fYWxsKVxuICAgIHJsID0gbnAuYXJyYXkocl9yZWplY3RlZF9hbGwpXG4gICAgYWNjdXJhY3kgID0gZmxvYXQoKHJ3IFx1MDAzZSBybCkubWVhbigpKVxuICAgIG1hcmdpbiAgICA9IGZsb2F0KChydyAtIHJsKS5tZWFuKCkpXG4gICAgb3ZlcmxhcCAgID0gZmxvYXQoKHJ3IFx1MDAzYyBybCkubWVhbigpKSAgIyBmcmFjdGlvbiB3aGVyZSBSTSBpcyB3cm9uZ1xuICAgIHByaW50KGZcIlBhaXJ3aXNlIGFjY3VyYWN5IDoge2FjY3VyYWN5Oi4zZn1cIilcbiAgICBwcmludChmXCJNZWFuIG1hcmdpbiAgICAgICA6IHttYXJnaW46LjNmfVwiKVxuICAgIHByaW50KGZcIkNob3NlbiAg4oCUIG1lYW46IHtydy5tZWFuKCk6LjNmfSwgc3RkOiB7cncuc3RkKCk6LjNmfVwiKVxuICAgIHByaW50KGZcIlJlamVjdGVkIOKAlCBtZWFuOiB7cmwubWVhbigpOi4zZn0sIHN0ZDoge3JsLnN0ZCgpOi4zZn1cIilcbiAgICBwcmludChmXCJSTSBlcnJvciByYXRlICAgICA6IHtvdmVybGFwOi4zZn1cIilcbiAgICByZXR1cm4ge1wiYWNjdXJhY3lcIjogYWNjdXJhY3ksIFwibWFyZ2luXCI6IG1hcmdpbn0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXdhcmQgSGFja2luZyBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJld2FyZCBoYWNraW5nIG9jY3VycyB3aGVuIHRoZSBwb2xpY3kgYmVpbmcgdHJhaW5lZCBieSBSTEhGIGxlYXJucyB0byBleHBsb2l0IHNwdXJpb3VzIGZlYXR1cmVzIHRoYXQgdGhlIFJNIGhhcyBvdmVyZml0OiB2ZXJib3NlIHJlc3BvbnNlcywgcGFydGljdWxhciBzZW50ZW5jZSBvcGVuZXJzLCBvciBmb3JtYXR0aW5nIHBhdHRlcm5zIHRoYXQgY29ycmVsYXRlIHdpdGggaGlnaCByZXdhcmQgYnV0IG5vdCBnZW51aW5lIHF1YWxpdHkuIERldGVjdGlvbiByZXF1aXJlcyBtb25pdG9yaW5nIHRoZSByZXdhcmQgc2NvcmUgZGlzdHJpYnV0aW9uIGFjcm9zcyB0cmFpbmluZyBpdGVyYXRpb25zIOKAlCByZXdhcmQgaGFja2luZyBtYW5pZmVzdHMgYXMgbW9ub3RvbmljIHNjb3JlIGluZmxhdGlvbiB3aXRob3V0IGNvcnJlc3BvbmRpbmcgcXVhbGl0eSBpbXByb3ZlbWVudC4gRW5zZW1ibGUgUk1zIChhdmVyYWdpbmcgYWNyb3NzIDPigJM1IGluZGVwZW5kZW50bHkgdHJhaW5lZCBSTXMpIHJlZHVjZSBoYWNraW5nIGJ5IG1ha2luZyBpdCBoYXJkZXIgdG8gc2ltdWx0YW5lb3VzbHkgZXhwbG9pdCBhbGwgbW9kZWxzLiBLTC1kaXZlcmdlbmNlIHJlZ3VsYXJpc2F0aW9uIChwZW5hbGlzaW5nIGRpdmVyZ2VuY2UgZnJvbSB0aGUgU0ZUIHBvbGljeSkgYm91bmRzIGhvdyBmYXIgdGhlIHBvbGljeSBjYW4gZXhwbG9pdCB0aGUgUk0gYmVmb3JlIHRoZSBLTCBwZW5hbHR5IGRvbWluYXRlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIFJld2FyZEhhY2tpbmdNb25pdG9yOlxuICAgIFwiXCJcIlRyYWNrIHJld2FyZCBkaXN0cmlidXRpb24gYWNyb3NzIFJMIHRyYWluaW5nIHRvIGRldGVjdCBzY29yZSBpbmZsYXRpb24uXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmFzZWxpbmVfd2luZG93PTUwLCBkZXRlY3Rpb25fd2luZG93PTIwLCB6X3RocmVzaG9sZD0zLjApOlxuICAgICAgICBzZWxmLmhpc3RvcnkgPSBbXSAgIyBsaXN0IG9mIChzdGVwLCBtZWFuLCBzdGQpXG4gICAgICAgIHNlbGYuYmFzZWxpbmVfd2luZG93ICA9IGJhc2VsaW5lX3dpbmRvd1xuICAgICAgICBzZWxmLmRldGVjdGlvbl93aW5kb3cgPSBkZXRlY3Rpb25fd2luZG93XG4gICAgICAgIHNlbGYuel90aHJlc2hvbGQgPSB6X3RocmVzaG9sZFxuXG4gICAgZGVmIHJlY29yZChzZWxmLCBzdGVwLCByZXdhcmRzKTpcbiAgICAgICAgc2VsZi5oaXN0b3J5LmFwcGVuZCgoc3RlcCwgZmxvYXQobnAubWVhbihyZXdhcmRzKSksIGZsb2F0KG5wLnN0ZChyZXdhcmRzKSkpKVxuXG4gICAgZGVmIGRldGVjdF9pbmZsYXRpb24oc2VsZik6XG4gICAgICAgIGlmIGxlbihzZWxmLmhpc3RvcnkpIFx1MDAzYyBzZWxmLmJhc2VsaW5lX3dpbmRvdyArIHNlbGYuZGV0ZWN0aW9uX3dpbmRvdzpcbiAgICAgICAgICAgIHJldHVybiBGYWxzZVxuICAgICAgICBtZWFucyA9IFtoWzFdIGZvciBoIGluIHNlbGYuaGlzdG9yeV1cbiAgICAgICAgYmFzZWxpbmUgPSBucC5hcnJheShtZWFuc1s6c2VsZi5iYXNlbGluZV93aW5kb3ddKVxuICAgICAgICByZWNlbnQgICA9IG5wLmFycmF5KG1lYW5zWy1zZWxmLmRldGVjdGlvbl93aW5kb3c6XSlcbiAgICAgICAgeiA9IChyZWNlbnQubWVhbigpIC0gYmFzZWxpbmUubWVhbigpKSAvIChiYXNlbGluZS5zdGQoKSArIDFlLTgpXG4gICAgICAgIGluZmxhdGluZyA9IHogXHUwMDNlIHNlbGYuel90aHJlc2hvbGRcbiAgICAgICAgcHJpbnQoZlwiQmFzZWxpbmUgbWVhbjoge2Jhc2VsaW5lLm1lYW4oKTouM2Z9ICBSZWNlbnQgbWVhbjoge3JlY2VudC5tZWFuKCk6LjNmfSAgWj17ejouMmZ9XCIpXG4gICAgICAgIGlmIGluZmxhdGluZzpcbiAgICAgICAgICAgIHByaW50KGZcIltXQVJOSU5HXSBSZXdhcmQgaW5mbGF0aW9uIGRldGVjdGVkIChaPXt6Oi4yZn0gXHUwMDNlIHtzZWxmLnpfdGhyZXNob2xkfSkg4oCUIHBvc3NpYmxlIHJld2FyZCBoYWNraW5nXCIpXG4gICAgICAgIHJldHVybiBpbmZsYXRpbmdcblxuIyBTaW11bGF0ZSB0cmFpbmluZyB3aXRoIGdyYWR1YWwgcmV3YXJkIGluZmxhdGlvblxubW9uaXRvciA9IFJld2FyZEhhY2tpbmdNb25pdG9yKGJhc2VsaW5lX3dpbmRvdz01MCwgZGV0ZWN0aW9uX3dpbmRvdz0yMClcbmZvciBzdGVwIGluIHJhbmdlKDE1MCk6XG4gICAgcmV3YXJkcyA9IG5wLnJhbmRvbS5ub3JtYWwoMC41ICsgc3RlcCAqIDAuMDEyLCAwLjMsIHNpemU9MzIpXG4gICAgbW9uaXRvci5yZWNvcmQoc3RlcCwgcmV3YXJkcylcbm1vbml0b3IuZGV0ZWN0X2luZmxhdGlvbigpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmV3YXJkIE1vZGVsIENoYXJhY3RlcmlzdGljcyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiU2l6ZSIsIlRyYWluaW5nIERhdGEiLCJQYWlyd2lzZSBBY2N1cmFjeSIsIk5vdGFibGUgQmlhcyAvIE5vdGVzIl0sInJvd3MiOltbIkluc3RydWN0R1BUIFJNIChPcGVuQUkpIiwiNkIiLCI1MEsgaHVtYW4gY29tcGFyaXNvbnMsIDLigJM3IGNvbXBsZXRpb25zL3Byb21wdCIsIn43MCUgaGVsZC1vdXQiLCJMZW5ndGggYmlhczsgaHVtYW4gbGFiZWxsZXIgYWdyZWVtZW50IH43MiUiXSxbIkFudGhyb3BpYyAoQ2xhdWRlKSBSTSIsIjUyQiIsIjUwMEsrIEhILVJMSEYgaGVscGZ1bG5lc3MgKyBoYXJtbGVzc25lc3MgcGFpcnMiLCJ+NzUlIiwiSGVscGZ1bG5lc3MtaGFybWxlc3NuZXNzIHRyYWRlLW9mZiBleHBsaWNpdGx5IG1vZGVsbGVkIl0sWyJMbGFtYS0zIFJNIChNZXRhKSIsIjcwQiIsIlByb3ByaWV0YXJ5IGh1bWFuICsgc3ludGhldGljIHByZWZlcmVuY2UgcGFpcnMiLCJ+ODAlIChBcmVuYSkiLCJMZW5ndGggYmlhcyByZWR1Y2VkIHZpYSBub3JtYWxpc2F0aW9uOyBzdHJvbmcgb24gcmVhc29uaW5nIl0sWyJaZXBoeXIgUkxBSUYgUk0iLCI3QiIsIkFJIEZlZWRiYWNrIOKAlCBDbGF1ZGUgYXMgbGFiZWxsZXIgKFVsdHJhRmVlZGJhY2spIiwifjY1JSIsIkxlc3MgbGVuZ3RoIGJpYXM7IGJvdW5kZWQgYnkgTExNIGp1ZGdlIHF1YWxpdHkgY2VpbGluZyJdLFsiTmVtb3Ryb24tNC0zNDBCLVJld2FyZCIsIjM0MEIiLCJQcm9wcmlldGFyeSBsYXJnZS1zY2FsZSBzeW50aGV0aWMgcHJlZmVyZW5jZXMiLCJ+ODIlIChSZXdhcmRCZW5jaCkiLCJOZWFyIGh1bWFuLWFncmVlbWVudDsgYmVzdCBvcGVuIHB1Ymxpc2hlZCBSTSBhcyBvZiAyMDI0Il1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEUE8sIEltcGxpY2l0IFJld2FyZHMsIGFuZCBCeXBhc3NpbmcgdGhlIFJNIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaXJlY3QgUHJlZmVyZW5jZSBPcHRpbWlzYXRpb24gKERQTykgYnlwYXNzZXMgZXhwbGljaXQgUk0gdHJhaW5pbmcgZW50aXJlbHkuIEl0IHNob3dzIHRoYXQgdGhlIG9wdGltYWwgUkxIRiBwb2xpY3kgaGFzIGEgY2xvc2VkLWZvcm0gZXhwcmVzc2lvbiBpbiB0ZXJtcyBvZiB0aGUgcHJlZmVyZW5jZSBkYXRhLCBhbGxvd2luZyBkaXJlY3QgcG9saWN5IG9wdGltaXNhdGlvbiBmcm9tIHBhaXJ3aXNlIGNvbXBhcmlzb25zLiBUaGUgRFBPIGxvc3MgaXMgTF9EUE8gPSDiiJJsb2cgz4MozrIgbG9nKM+AX864KHlfd3x4KS/PgF9yZWYoeV93fHgpKSDiiJIgzrIgbG9nKM+AX864KHlfbHx4KS/PgF9yZWYoeV9sfHgpKSksIHdoaWNoIGltcGxpY2l0bHkgZGVmaW5lcyBhIHJld2FyZCByKHgseSkgPSDOsiBsb2coz4BfzrgoeXx4KS/PgF9yZWYoeXx4KSkuIERQTyBlbGltaW5hdGVzIFJNIHRyYWluaW5nIG92ZXJoZWFkIGFuZCBhdm9pZHMgcmV3YXJkIGhhY2tpbmcgKHRoZXJlIGlzIG5vIHNlcGFyYXRlIFJNIHRvIGhhY2spLCBidXQgcmVxdWlyZXMgdGhlIHByZWZlcmVuY2UgZGF0YSB0byBiZSBoaWdoIHF1YWxpdHkgc2luY2UgdGhlIHBvbGljeSBpcyB0cmFpbmVkIGRpcmVjdGx5IG9uIGl0LiBIeWJyaWQgYXBwcm9hY2hlcyBsaWtlIElQTyBhbmQgS1RPIGV4dGVuZCBEUE8gdG8gaGFuZGxlIGxhYmVsIG5vaXNlIGFuZCBub24tcGFpcndpc2UgZGF0YS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlJMSEYgcGlwZWxpbmU6IFNGVCDihpIgUk0gdHJhaW5pbmcgb24gaHVtYW4gcGFpcnMg4oaSIFBQTyBvcHRpbWlzYXRpb24gd2l0aCBLTCBwZW5hbHR5IOKGkiBldmFsdWF0ZSB3aXRoIFJNLiIsIkRQTyBzaG9ydGN1dDogU0ZUIOKGkiBEUE8gZGlyZWN0bHkgb24gcHJlZmVyZW5jZSBwYWlycyDigJQgbm8gUk0sIG5vIFBQTywgaGFsZiB0aGUgdHJhaW5pbmcgc3RhZ2VzLiIsIkJlc3Qtb2YtTiBzYW1wbGluZzogZ2VuZXJhdGUgTiByZXNwb25zZXMsIHJlLXJhbmsgd2l0aCBSTSwgc2VsZWN0IHRoZSB0b3Atc2NvcmluZyBvbmUg4oCUIGluZmVyZW5jZS10aW1lIHJld2FyZCBoYWNraW5nLiIsIlJNIGVuc2VtYmxlOiB0cmFpbiAz4oCTNSBSTXMgb24gZGlmZmVyZW50IGRhdGEgc3BsaXRzLCBhdmVyYWdlIHJld2FyZHMg4oCUIHJlZHVjZXMgaGFja2luZyBzdXJmYWNlIGFyZWEgc2lnbmlmaWNhbnRseS4iLCJMZW5ndGggbm9ybWFsaXNhdGlvbjogZGl2aWRlIHJld2FyZCBieSByZXNwb25zZSBsZW5ndGggKGluIHRva2VucykgdG8gcGVuYWxpc2UgdmVyYm9zaXR5IGJpYXMgaW4gdGhlIFJNIHNpZ25hbC4iLCJSZXdhcmQgbW9kZWwgY2FsaWJyYXRpb246IGNoZWNrIHRoYXQgz4Mocl93IC0gcl9sKSBtYXRjaGVzIGVtcGlyaWNhbCB3aW4gcmF0ZSBvbiBoZWxkLW91dCBkYXRhIHZpYSByZWxpYWJpbGl0eSBkaWFncmFtcy4iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJMZW5ndGggQmlhcyBpbiBSZXdhcmQgTW9kZWxzIiwiY29udGVudCI6Ikxlbmd0aCBiaWFzIGluIHJld2FyZCBtb2RlbHMgaXMgcGVydmFzaXZlIOKAlCBSTXMgdHJhaW5lZCBvbiBodW1hbiBwcmVmZXJlbmNlcyBzeXN0ZW1hdGljYWxseSByYXRlIGxvbmdlciByZXNwb25zZXMgaGlnaGVyIGV2ZW4gd2hlbiBzaG9ydGVyIHJlc3BvbnNlcyBhcmUgbW9yZSBhY2N1cmF0ZS4gQWx3YXlzIGNoZWNrIHJld2FyZCB2cyBsZW5ndGggY29ycmVsYXRpb24gYW5kIHVzZSBsZW5ndGgtbm9ybWFsaXNlZCBzY29yaW5nLiBBIHNpbXBsZSB0ZXN0OiBnZW5lcmF0ZSB0d28gdmVyc2lvbnMgb2YgZWFjaCByZXNwb25zZSAoc2hvcnQgYW5kIHZlcmJvc2UpIGFuZCBjaGVjayBpZiB0aGUgUk0gY29uc2lzdGVudGx5IHByZWZlcnMgdGhlIGxvbmdlciBvbmUgcmVnYXJkbGVzcyBvZiBjb250ZW50IHF1YWxpdHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXdhcmQgbW9kZWxsaW5nIGlzIHRoZSBtb3N0IGRhdGEtc2Vuc2l0aXZlIGNvbXBvbmVudCBvZiB0aGUgUkxIRiBwaXBlbGluZS4gVGhlIFJNIHF1YWxpdHkgY2VpbGluZyBpcyBzZXQgYnkgaHVtYW4gbGFiZWxsZXIgYWdyZWVtZW50ICh+NzLigJM4MCUpLCBzbyBpbnZlc3RpbmcgaW4gbGFiZWxsZXIgdHJhaW5pbmcsIGNsZWFyIGFubm90YXRpb24gZ3VpZGVsaW5lcywgYW5kIGNhcmVmdWwgcHJvbXB0IGRlc2lnbiBwYXlzIGxhcmdlIGRpdmlkZW5kcy4gTW9uaXRvcmluZyByZXdhcmQgc2NvcmUgZGlzdHJpYnV0aW9ucyB0aHJvdWdob3V0IFJMIHRyYWluaW5nIChub3QganVzdCBhdCB0aGUgZW5kKSBpcyBlc3NlbnRpYWwgZm9yIGNhdGNoaW5nIHJld2FyZCBoYWNraW5nIGJlZm9yZSBpdCBjb3JydXB0cyB0aGUgcG9saWN5LiBGb3IgdGVhbXMgd2l0aG91dCB0aGUgYnVkZ2V0IGZvciBsYXJnZS1zY2FsZSBodW1hbiBhbm5vdGF0aW9uLCBSTEFJRiAodXNpbmcgYSBzdHJvbmcgTExNIGFzIHRoZSBwcmVmZXJlbmNlIGxhYmVsbGVyKSBvciBEUE8gd2l0aCBwdWJsaWMgcHJlZmVyZW5jZSBkYXRhc2V0cyAoVWx0cmFGZWVkYmFjaywgSEgtUkxIRikgYXJlIHZpYWJsZSBhbHRlcm5hdGl2ZXMgdGhhdCBhcHByb2FjaCBSTSBxdWFsaXR5IHdpdGhpbiA14oCTMTAgcGVyY2VudGFnZSBwb2ludHMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Reward Modeling — Bradley-Terry Model and Pairwise Preference Learning

A reward model (RM) is a neural network trained to predict which of two responses a human would prefer, given the same prompt. It converts qualitative human judgements into a scalar signal that downstream training (RLHF, best-of-N sampling) can optimise. The RM is the critical bottleneck in the RLHF pipeline: its errors compound — a biased RM produces biased policy updates, and the policy is then trained to exploit RM weaknesses (reward hacking). Understanding the Bradley-Terry loss, RM architecture, data collection, evaluation, and bias mitigation is essential for anyone building RLHF or preference-learning systems.

## Bradley-Terry Model and Pairwise Loss

The Bradley-Terry model provides a principled probabilistic foundation for pairwise preference learning. Given prompt x, chosen response y_w, and rejected response y_l, the probability that a human prefers y_w is modelled as P(y_w > y_l | x) = σ(r(x, y_w) − r(x, y_l)) where σ is the sigmoid function and r is the scalar reward function. The RM loss is the negative log-likelihood of observed preferences: L = −E[log σ(r_w − r_l)]. Minimising this loss pushes r(x, y_w) to be larger than r(x, y_l) by an amount proportional to how confidently the model assigns the preference. The margin r_w − r_l is the key quantity: large positive margins indicate high-confidence correct preferences.

## Reward Model Architecture

The RM is initialised from a pretrained LLM (often the SFT model) with its language modelling head replaced by a single linear layer that outputs a scalar reward. The backbone processes the full prompt-plus-response sequence, and the scalar head pools the final hidden state at the last non-padding token position. Using the last token captures the cumulative context of the entire response. Initialising from the SFT model (rather than the raw pretrained model) is important — the SFT model already speaks instruction-following language, so it requires less data to learn preference distinctions. RM size typically matches or is larger than the policy model to act as an accurate critic.

```python
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer

class RewardModel(nn.Module):
    def __init__(self, base_model_name, dtype=torch.bfloat16):
        super().__init__()
        self.backbone = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype=dtype)
        d_model = self.backbone.config.hidden_size
        self.backbone.lm_head = nn.Identity()  # remove token prediction head
        self.reward_head = nn.Linear(d_model, 1, bias=False)

    def forward(self, input_ids, attention_mask):
        out = self.backbone(input_ids=input_ids, attention_mask=attention_mask, output_hidden_states=True)
        last_hidden = out.hidden_states[-1]          # (B, T, d_model)
        seq_lens = attention_mask.sum(dim=1) - 1    # index of last real token
        batch_idx = torch.arange(last_hidden.size(0), device=last_hidden.device)
        pooled = last_hidden[batch_idx, seq_lens]   # (B, d_model)
        return self.reward_head(pooled).squeeze(-1) # (B,)

def bradley_terry_loss(r_chosen, r_rejected):
    """L = -E[log sigma(r_w - r_l)], the pairwise Bradley-Terry loss."""
    return -torch.nn.functional.logsigmoid(r_chosen - r_rejected).mean()

def rm_train_step(model, chosen_batch, rejected_batch, optimizer):
    r_w = model(**chosen_batch)
    r_l = model(**rejected_batch)
    loss = bradley_terry_loss(r_w, r_l)
    optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()
    accuracy = (r_w > r_l).float().mean().item()
    margin   = (r_w - r_l).mean().item()
    return {"loss": loss.item(), "accuracy": accuracy, "margin": margin}
```

## Preference Dataset Creation

RM training requires pairwise comparison data: for each prompt, at least two responses are generated and a human labeller selects the preferred one. In practice, labellers compare 2–8 completions per prompt and rank them — this yields O(k²) pairs from k completions, making comparison more efficient than absolute scoring. Labeller agreement is typically 70–80% (inter-annotator agreement), setting the upper bound on RM accuracy. The Anthropic HH-RLHF dataset (helpfulness + harmlessness) and OpenAI's InstructGPT comparisons are the most widely used public datasets. Data scale ranges from 10K pairs (small internal RM) to 1M+ (production systems like InstructGPT or Claude's RM).

```python
from datasets import load_dataset
from transformers import AutoTokenizer
import torch

def format_preference_pair(tokenizer, prompt, chosen, rejected, max_length=512):
    """Tokenize chosen and rejected responses for Bradley-Terry RM training."""
    def encode(response):
        text = f"Human: {prompt}\n\nAssistant: {response}"
        enc  = tokenizer(text, max_length=max_length, truncation=True,
                         padding="max_length", return_tensors="pt")
        return enc["input_ids"][0], enc["attention_mask"][0]

    chosen_ids,   chosen_mask   = encode(chosen)
    rejected_ids, rejected_mask = encode(rejected)
    return {
        "chosen_input_ids":       chosen_ids,
        "chosen_attention_mask":  chosen_mask,
        "rejected_input_ids":     rejected_ids,
        "rejected_attention_mask": rejected_mask,
    }

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3-8B")
tokenizer.pad_token = tokenizer.eos_token

dataset = load_dataset("Anthropic/hh-rlhf", split="train[:5000]")

def preprocess(ex):
    # HH-RLHF format: chosen and rejected are full conversation strings
    prompt   = ex["chosen"].rsplit("Assistant:", 1)[0].strip()
    chosen_r = ex["chosen"].rsplit("Assistant:", 1)[-1].strip()
    rejected_r = ex["rejected"].rsplit("Assistant:", 1)[-1].strip()
    return format_preference_pair(tokenizer, prompt, chosen_r, rejected_r)

tokenized = dataset.map(preprocess, remove_columns=dataset.column_names)
print(f"Preference pairs tokenized: {len(tokenized)}")
```

## RM Evaluation — Accuracy, Margin, and Calibration

The primary RM evaluation metric is pairwise accuracy: the fraction of held-out pairs where the RM assigns a higher reward to the chosen response. Random chance is 50%; a well-trained RM achieves 70–85% depending on data quality and model size. The mean reward margin (r_w − r_l) measures separability — larger margins indicate more confident, calibrated predictions. Calibration assessment checks whether the RM's win probability σ(r_w − r_l) matches empirical win rates: a RM predicting 80% win rate should be correct 80% of the time. RewardBench is the standard benchmark for comparing RMs across helpfulness, safety, and reasoning axes.

```python
import torch
import numpy as np

def evaluate_reward_model(model, eval_loader, device="cuda"):
    """Compute pairwise accuracy, mean margin, and score distribution statistics."""
    model.eval()
    r_chosen_all, r_rejected_all = [], []
    with torch.no_grad():
        for batch in eval_loader:
            r_w = model(
                input_ids=batch["chosen_input_ids"].to(device),
                attention_mask=batch["chosen_attention_mask"].to(device)
            )
            r_l = model(
                input_ids=batch["rejected_input_ids"].to(device),
                attention_mask=batch["rejected_attention_mask"].to(device)
            )
            r_chosen_all.extend(r_w.cpu().float().tolist())
            r_rejected_all.extend(r_l.cpu().float().tolist())
    rw = np.array(r_chosen_all)
    rl = np.array(r_rejected_all)
    accuracy  = float((rw > rl).mean())
    margin    = float((rw - rl).mean())
    overlap   = float((rw < rl).mean())  # fraction where RM is wrong
    print(f"Pairwise accuracy : {accuracy:.3f}")
    print(f"Mean margin       : {margin:.3f}")
    print(f"Chosen  — mean: {rw.mean():.3f}, std: {rw.std():.3f}")
    print(f"Rejected — mean: {rl.mean():.3f}, std: {rl.std():.3f}")
    print(f"RM error rate     : {overlap:.3f}")
    return {"accuracy": accuracy, "margin": margin}
```

## Reward Hacking Detection

Reward hacking occurs when the policy being trained by RLHF learns to exploit spurious features that the RM has overfit: verbose responses, particular sentence openers, or formatting patterns that correlate with high reward but not genuine quality. Detection requires monitoring the reward score distribution across training iterations — reward hacking manifests as monotonic score inflation without corresponding quality improvement. Ensemble RMs (averaging across 3–5 independently trained RMs) reduce hacking by making it harder to simultaneously exploit all models. KL-divergence regularisation (penalising divergence from the SFT policy) bounds how far the policy can exploit the RM before the KL penalty dominates.

```python
import numpy as np

class RewardHackingMonitor:
    """Track reward distribution across RL training to detect score inflation."""

    def __init__(self, baseline_window=50, detection_window=20, z_threshold=3.0):
        self.history = []  # list of (step, mean, std)
        self.baseline_window  = baseline_window
        self.detection_window = detection_window
        self.z_threshold = z_threshold

    def record(self, step, rewards):
        self.history.append((step, float(np.mean(rewards)), float(np.std(rewards))))

    def detect_inflation(self):
        if len(self.history) < self.baseline_window + self.detection_window:
            return False
        means = [h[1] for h in self.history]
        baseline = np.array(means[:self.baseline_window])
        recent   = np.array(means[-self.detection_window:])
        z = (recent.mean() - baseline.mean()) / (baseline.std() + 1e-8)
        inflating = z > self.z_threshold
        print(f"Baseline mean: {baseline.mean():.3f}  Recent mean: {recent.mean():.3f}  Z={z:.2f}")
        if inflating:
            print(f"[WARNING] Reward inflation detected (Z={z:.2f} > {self.z_threshold}) — possible reward hacking")
        return inflating

# Simulate training with gradual reward inflation
monitor = RewardHackingMonitor(baseline_window=50, detection_window=20)
for step in range(150):
    rewards = np.random.normal(0.5 + step * 0.012, 0.3, size=32)
    monitor.record(step, rewards)
monitor.detect_inflation()
```

## Reward Model Characteristics Comparison

| Model | Size | Training Data | Pairwise Accuracy | Notable Bias / Notes |
| --- | --- | --- | --- | --- |
| InstructGPT RM (OpenAI) | 6B | 50K human comparisons, 2–7 completions/prompt | ~70% held-out | Length bias; human labeller agreement ~72% |
| Anthropic (Claude) RM | 52B | 500K+ HH-RLHF helpfulness + harmlessness pairs | ~75% | Helpfulness-harmlessness trade-off explicitly modelled |
| Llama-3 RM (Meta) | 70B | Proprietary human + synthetic preference pairs | ~80% (Arena) | Length bias reduced via normalisation; strong on reasoning |
| Zephyr RLAIF RM | 7B | AI Feedback — Claude as labeller (UltraFeedback) | ~65% | Less length bias; bounded by LLM judge quality ceiling |
| Nemotron-4-340B-Reward | 340B | Proprietary large-scale synthetic preferences | ~82% (RewardBench) | Near human-agreement; best open published RM as of 2024 |

## DPO, Implicit Rewards, and Bypassing the RM

Direct Preference Optimisation (DPO) bypasses explicit RM training entirely. It shows that the optimal RLHF policy has a closed-form expression in terms of the preference data, allowing direct policy optimisation from pairwise comparisons. The DPO loss is L_DPO = −log σ(β log(π_θ(y_w|x)/π_ref(y_w|x)) − β log(π_θ(y_l|x)/π_ref(y_l|x))), which implicitly defines a reward r(x,y) = β log(π_θ(y|x)/π_ref(y|x)). DPO eliminates RM training overhead and avoids reward hacking (there is no separate RM to hack), but requires the preference data to be high quality since the policy is trained directly on it. Hybrid approaches like IPO and KTO extend DPO to handle label noise and non-pairwise data.

- RLHF pipeline: SFT → RM training on human pairs → PPO optimisation with KL penalty → evaluate with RM.
- DPO shortcut: SFT → DPO directly on preference pairs — no RM, no PPO, half the training stages.
- Best-of-N sampling: generate N responses, re-rank with RM, select the top-scoring one — inference-time reward hacking.
- RM ensemble: train 3–5 RMs on different data splits, average rewards — reduces hacking surface area significantly.
- Length normalisation: divide reward by response length (in tokens) to penalise verbosity bias in the RM signal.
- Reward model calibration: check that σ(r_w - r_l) matches empirical win rate on held-out data via reliability diagrams.

> **Length Bias in Reward Models**: Length bias in reward models is pervasive — RMs trained on human preferences systematically rate longer responses higher even when shorter responses are more accurate. Always check reward vs length correlation and use length-normalised scoring. A simple test: generate two versions of each response (short and verbose) and check if the RM consistently prefers the longer one regardless of content quality.

Reward modelling is the most data-sensitive component of the RLHF pipeline. The RM quality ceiling is set by human labeller agreement (~72–80%), so investing in labeller training, clear annotation guidelines, and careful prompt design pays large dividends. Monitoring reward score distributions throughout RL training (not just at the end) is essential for catching reward hacking before it corrupts the policy. For teams without the budget for large-scale human annotation, RLAIF (using a strong LLM as the preference labeller) or DPO with public preference datasets (UltraFeedback, HH-RLHF) are viable alternatives that approach RM quality within 5–10 percentage points.

---

