---
title: "Chat Templates — System/User/Assistant Format and Tokenizer Integration"
slug: "chat-templates"
description: "Chat templates standardize multi-turn conversation encoding as Jinja2 templates in tokenizer_config.json — covering LLaMA-3, Mistral, ChatML, and Phi-3 formats, applying templates with HuggingFace tokenizers, implementing SFT loss masking, and encoding tool-calling sequences correctly."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2hhdCB0ZW1wbGF0ZXMgZGVmaW5lIGhvdyBtdWx0aS10dXJuIGNvbnZlcnNhdGlvbnMgYmV0d2VlbiBzeXN0ZW0sIHVzZXIsIGFuZCBhc3Npc3RhbnQgcm9sZXMgYXJlIHNlcmlhbGl6ZWQgaW50byBhIGZsYXQgdG9rZW4gc2VxdWVuY2UgZm9yIGxhbmd1YWdlIG1vZGVsIGlucHV0LiBFYWNoIG1vZGVsIGZhbWlseSB1c2VzIGEgZGlzdGluY3QgZm9ybWF0IHdpdGggdW5pcXVlIHJvbGUgZGVsaW1pdGVycywgc3BlY2lhbCB0b2tlbnMsIGFuZCB0dXJuIGJvdW5kYXJpZXMuIEh1Z2dpbmdGYWNlIHN0b3JlcyB0aGVzZSB0ZW1wbGF0ZXMgYXMgSmluamEyIHN0cmluZ3MgaW4gdG9rZW5pemVyX2NvbmZpZy5qc29uIGFuZCBleHBvc2VzIHRoZW0gdmlhIHRva2VuaXplci5hcHBseV9jaGF0X3RlbXBsYXRlKCkuIFVzaW5nIHRoZSBjb3JyZWN0IHRlbXBsYXRlIGF0IGJvdGggdHJhaW5pbmcgYW5kIGluZmVyZW5jZSB0aW1lIGlzIG5vbi1uZWdvdGlhYmxlIOKAlCBldmVuIG1pbm9yIGZvcm1hdCBkaWZmZXJlbmNlcyBjYXVzZSB0aGUgbW9kZWwgdG8gZmFpbCB0byBmb2xsb3cgaW5zdHJ1Y3Rpb25zIG9yIHByb2R1Y2UgcmVwZXRpdGl2ZSB0ZXh0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBDaGF0IFRlbXBsYXRlcyBNYXR0ZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNoYXQtdHVuZWQgbW9kZWxzIGFyZSB0cmFpbmVkIG9uIG1pbGxpb25zIG9mIGNvbnZlcnNhdGlvbnMgZm9ybWF0dGVkIGFjY29yZGluZyB0byBhIHNwZWNpZmljIHRlbXBsYXRlLiBUaGUgbW9kZWwgbGVhcm5zIHRvIGFzc29jaWF0ZSByb2xlIGRlbGltaXRlciB0b2tlbnMgd2l0aCBiZWhhdmlvcmFsIHBhdHRlcm5zOiBhZnRlciB0aGUgYXNzaXN0YW50IGhlYWRlciB0b2tlbiwgdGhlIG1vZGVsIGdlbmVyYXRlcyBhIHJlc3BvbnNlOyBhZnRlciB0aGUgdXNlciBoZWFkZXIgdG9rZW4sIGl0IHN3aXRjaGVzIHRvIGxpc3RlbmluZyBtb2RlLiBJZiB5b3UgYXBwbHkgdGhlIHdyb25nIHRlbXBsYXRlIGF0IGluZmVyZW5jZSB0aW1lIOKAlCB3cm9uZyBkZWxpbWl0ZXJzLCBtaXNzaW5nIG5ld2xpbmVzLCB3cm9uZyBFT1MgdG9rZW4g4oCUIHRoZSBtb2RlbCBzZWVzIGEgZm9ybWF0IGl0IHdhcyBub3QgdHJhaW5lZCBvbiwgd2hpY2ggZGVncmFkZXMgZ2VuZXJhdGlvbiBxdWFsaXR5IHNpZ25pZmljYW50bHkuIFRoZSBmYWlsdXJlIG1vZGUgaXMgc3VidGxlOiB0aGUgbW9kZWwgbWF5IHN0aWxsIGdlbmVyYXRlIHRleHQsIGJ1dCBpdCBpZ25vcmVzIHRoZSBzeXN0ZW0gcHJvbXB0LCBmYWlscyB0byBzdG9wIGF0IHRoZSByaWdodCB0dXJuIGJvdW5kYXJ5LCBvciBwcm9kdWNlcyBnZW5lcmljIGNvbXBsZXRpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFwcGx5aW5nIEJ1aWx0LWluIFRlbXBsYXRlcyB3aXRoIEh1Z2dpbmdGYWNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJ0b2tlbml6ZXIuYXBwbHlfY2hhdF90ZW1wbGF0ZSgpIGlzIHRoZSBzdGFuZGFyZCBBUEkgZm9yIGNvbnZlcnRpbmcgYSBsaXN0IG9mIHJvbGUtY29udGVudCBkaWN0cyB0byBhIGZvcm1hdHRlZCBzdHJpbmcgb3IgdG9rZW4gSURzLiBUaGUga2V5IHBhcmFtZXRlcnM6IHRva2VuaXplPVRydWUgdG8gZ2V0IHRva2VuIElEcyAoZm9yIG1vZGVsIGlucHV0KSwgdG9rZW5pemU9RmFsc2UgdG8gZ2V0IHRoZSBmb3JtYXR0ZWQgc3RyaW5nIChmb3IgaW5zcGVjdGlvbik7IGFkZF9nZW5lcmF0aW9uX3Byb21wdD1UcnVlIGFwcGVuZHMgdGhlIHN0YXJ0IG9mIHRoZSBhc3Npc3RhbnQgdHVybiB0byBwcm9tcHQgdGhlIG1vZGVsIHRvIGdlbmVyYXRlIGEgcmVzcG9uc2UuIFRoZSB0ZW1wbGF0ZSBpcyBzb3VyY2VkIGZyb20gdG9rZW5pemVyLmNoYXRfdGVtcGxhdGUg4oCUIGEgSmluamEyIHN0cmluZyBpbiB0b2tlbml6ZXJfY29uZmlnLmpzb24uIEZvciBtb2RlbHMgd2l0aG91dCBhIGJ1aWx0LWluIHRlbXBsYXRlLCBhIFZhbHVlRXJyb3IgaXMgcmFpc2VkLCBpbmRpY2F0aW5nIHRoZSBtb2RlbCB3YXMgbm90IHRyYWluZWQgd2l0aCBhIHN0YW5kYXJkIGNoYXQgZm9ybWF0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG5kZWYgY29tcGFyZV9jaGF0X3RlbXBsYXRlcyh1c2VyX3Byb21wdCwgc3lzdGVtX21zZz1cdTAwMjdZb3UgYXJlIGEgaGVscGZ1bCBhc3Npc3RhbnQuXHUwMDI3KTpcbiAgICAjIEFwcGx5IGFuZCBjb21wYXJlIGNoYXQgdGVtcGxhdGVzIGZvciBMTGFNQS0zIGFuZCBNaXN0cmFsXG4gICAgbWVzc2FnZXNfd2l0aF9zeXN0ZW0gPSBbXG4gICAgICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdzeXN0ZW1cdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IHN5c3RlbV9tc2d9LFxuICAgICAgICB7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3dXNlclx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogdXNlcl9wcm9tcHR9LFxuICAgIF1cbiAgICBtZXNzYWdlc19ub19zeXN0ZW0gPSBbe1x1MDAyN3JvbGVcdTAwMjc6IFx1MDAyN3VzZXJcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IHVzZXJfcHJvbXB0fV1cbiAgICBtb2RlbF9jb25maWdzID0gW1xuICAgICAgICAoXHUwMDI3bWV0YS1sbGFtYS9NZXRhLUxsYW1hLTMtOEItSW5zdHJ1Y3RcdTAwMjcsIFRydWUpLFxuICAgICAgICAoXHUwMDI3bWlzdHJhbGFpL01pc3RyYWwtN0ItSW5zdHJ1Y3QtdjAuM1x1MDAyNywgRmFsc2UpLFxuICAgIF1cbiAgICBmb3IgbW9kZWxfaWQsIHN1cHBvcnRzX3N5c3RlbSBpbiBtb2RlbF9jb25maWdzOlxuICAgICAgICB0cnk6XG4gICAgICAgICAgICB0b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9pZClcbiAgICAgICAgICAgIG1zZ3MgPSBtZXNzYWdlc193aXRoX3N5c3RlbSBpZiBzdXBwb3J0c19zeXN0ZW0gZWxzZSBtZXNzYWdlc19ub19zeXN0ZW1cbiAgICAgICAgICAgIGZvcm1hdHRlZCA9IHRva2VuaXplci5hcHBseV9jaGF0X3RlbXBsYXRlKG1zZ3MsIHRva2VuaXplPUZhbHNlLCBhZGRfZ2VuZXJhdGlvbl9wcm9tcHQ9VHJ1ZSlcbiAgICAgICAgICAgIHRva2VucyA9IHRva2VuaXplci5hcHBseV9jaGF0X3RlbXBsYXRlKG1zZ3MsIHRva2VuaXplPVRydWUsIGFkZF9nZW5lcmF0aW9uX3Byb21wdD1UcnVlKVxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyNy0tLSB7bW9kZWxfaWR9IC0tLVx1MDAyNylcbiAgICAgICAgICAgIHByaW50KGZcdTAwMjdGb3JtYXR0ZWQgKHtsZW4odG9rZW5zKX0gdG9rZW5zKTpcdTAwMjcpXG4gICAgICAgICAgICBwcmludChyZXByKGZvcm1hdHRlZFs6MjUwXSkpXG4gICAgICAgICAgICBwcmludCgpXG4gICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZTpcbiAgICAgICAgICAgIHByaW50KGZcdTAwMjd7bW9kZWxfaWR9OiB7ZX1cdTAwMjcpXG5cbmRlZiBpbnNwZWN0X3RlbXBsYXRlKG1vZGVsX2lkKTpcbiAgICB0b2sgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9pZClcbiAgICB0bXBsID0gdG9rLmNoYXRfdGVtcGxhdGUgb3IgXHUwMDI3Tm8gY2hhdF90ZW1wbGF0ZSBmb3VuZFx1MDAyN1xuICAgIHByaW50KGZcdTAwMjdUZW1wbGF0ZSAoe2xlbih0bXBsKX0gY2hhcnMpOlx1MDAyNywgdG1wbFs6MjAwXSwgXHUwMDI3Li4uXHUwMDI3KVxuXG5jb21wYXJlX2NoYXRfdGVtcGxhdGVzKFx1MDAyN0V4cGxhaW4gdHJhbnNmb3JtZXIgYXR0ZW50aW9uIGluIDMgc2VudGVuY2VzLlx1MDAyNylcbnByaW50KFx1MDAyN1RlbXBsYXRlIG1pc21hdGNoIGF0IGluZmVyZW5jZSAtXHUwMDNlIGdlbmVyaWMgb3V0cHV0IG9yIGluc3RydWN0aW9uLWZvbGxvd2luZyBmYWlsdXJlXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkN1c3RvbSBKaW5qYTIgVGVtcGxhdGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGEgbW9kZWwgbGFja3MgYSBidWlsdC1pbiB0ZW1wbGF0ZSBvciB5b3UgbmVlZCBhIGN1c3RvbSBmb3JtYXQsIHlvdSBjYW4gd3JpdGUgYSBKaW5qYTIgdGVtcGxhdGUgYW5kIGFzc2lnbiBpdCB0byB0b2tlbml6ZXIuY2hhdF90ZW1wbGF0ZS4gVGhlIHRlbXBsYXRlIGhhcyBhY2Nlc3MgdG8gdGhlIG1lc3NhZ2VzIGxpc3QgYW5kIGFkZF9nZW5lcmF0aW9uX3Byb21wdCBib29sZWFuLiBSb2xlIG5hbWVzIGFyZSBhY2Nlc3NlZCB2aWEgbWVzc2FnZVtcdTAwMjdyb2xlXHUwMDI3XSBhbmQgY29udGVudCB2aWEgbWVzc2FnZVtcdTAwMjdjb250ZW50XHUwMDI3XS4gVGhlIHRlbXBsYXRlIGlzIHNhdmVkIHRvIHRva2VuaXplcl9jb25maWcuanNvbiB3aGVuIHlvdSBjYWxsIHRva2VuaXplci5zYXZlX3ByZXRyYWluZWQoKSwgcGVyc2lzdGluZyBpdCBmb3IgZnV0dXJlIHVzZS4gQ2hhdE1MIGlzIHRoZSBtb3N0IHdpZGVseSBhZG9wdGVkIGN1c3RvbSBmb3JtYXQg4oCUIGl0IHdhcyBwb3B1bGFyaXplZCBieSBPcGVuQUkgYW5kIGlzIHVzZWQgYXMgdGhlIGRlZmF1bHQgZm9yIG1hbnkgb3Blbi1zb3VyY2UgbW9kZWxzIGZpbmUtdHVuZWQgd2l0aG91dCBmb3JtYXQgc3BlY2lmaWNhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXJcbmZyb20gamluamEyIGltcG9ydCBFbnZpcm9ubWVudFxuXG5DSEFUTUxfVEVNUExBVEUgPSAoXG4gICAgXHUwMDI3eyUtIGZvciBtZXNzYWdlIGluIG1lc3NhZ2VzICV9XHUwMDI3XG4gICAgXHUwMDI3eyUtIGlmIG1lc3NhZ2VbXCJyb2xlXCJdID09IFwic3lzdGVtXCIgJX1cdTAwM2N8aW1fc3RhcnR8XHUwMDNlc3lzdGVtXFxue3sgbWVzc2FnZVtcImNvbnRlbnRcIl0gfX1cdTAwM2N8aW1fZW5kfFx1MDAzZVxcblx1MDAyN1xuICAgIFx1MDAyN3slLSBlbGlmIG1lc3NhZ2VbXCJyb2xlXCJdID09IFwidXNlclwiICV9XHUwMDNjfGltX3N0YXJ0fFx1MDAzZXVzZXJcXG57eyBtZXNzYWdlW1wiY29udGVudFwiXSB9fVx1MDAzY3xpbV9lbmR8XHUwMDNlXFxuXHUwMDI3XG4gICAgXHUwMDI3eyUtIGVsaWYgbWVzc2FnZVtcInJvbGVcIl0gPT0gXCJhc3Npc3RhbnRcIiAlfVx1MDAzY3xpbV9zdGFydHxcdTAwM2Vhc3Npc3RhbnRcXG57eyBtZXNzYWdlW1wiY29udGVudFwiXSB9fVx1MDAzY3xpbV9lbmR8XHUwMDNlXFxuXHUwMDI3XG4gICAgXHUwMDI3eyUtIGVuZGlmICV9eyUtIGVuZGZvciAlfVx1MDAyN1xuICAgIFx1MDAyN3slLSBpZiBhZGRfZ2VuZXJhdGlvbl9wcm9tcHQgJX1cdTAwM2N8aW1fc3RhcnR8XHUwMDNlYXNzaXN0YW50XFxueyUtIGVuZGlmICV9XHUwMDI3XG4pXG5cbmRlZiBhcHBseV90ZW1wbGF0ZV9tYW51YWxseShtZXNzYWdlcywgdGVtcGxhdGVfc3RyLCBhZGRfZ2VuZXJhdGlvbl9wcm9tcHQ9VHJ1ZSk6XG4gICAgIyBBcHBseSBKaW5qYTIgdGVtcGxhdGUgd2l0aG91dCBhIHRva2VuaXplciAoZm9yIGluc3BlY3Rpb24vdGVzdGluZylcbiAgICBlbnYgPSBFbnZpcm9ubWVudCgpXG4gICAgdG1wbCA9IGVudi5mcm9tX3N0cmluZyh0ZW1wbGF0ZV9zdHIpXG4gICAgcmV0dXJuIHRtcGwucmVuZGVyKG1lc3NhZ2VzPW1lc3NhZ2VzLCBhZGRfZ2VuZXJhdGlvbl9wcm9tcHQ9YWRkX2dlbmVyYXRpb25fcHJvbXB0KVxuXG5kZWYgcmVnaXN0ZXJfY3VzdG9tX3RlbXBsYXRlKGJhc2VfbW9kZWxfaWQsIGN1c3RvbV90ZW1wbGF0ZSk6XG4gICAgIyBBc3NpZ24gY3VzdG9tIGNoYXQgdGVtcGxhdGUgdG8gdG9rZW5pemVyIGFuZCBzYXZlXG4gICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQoYmFzZV9tb2RlbF9pZClcbiAgICB0b2tlbml6ZXIuY2hhdF90ZW1wbGF0ZSA9IGN1c3RvbV90ZW1wbGF0ZVxuICAgIHByaW50KGZcdTAwMjdUZW1wbGF0ZSByZWdpc3RlcmVkOiB7bGVuKGN1c3RvbV90ZW1wbGF0ZSl9IGNoYXJzXHUwMDI3KVxuICAgIHByaW50KFx1MDAyN1NhdmUgd2l0aDogdG9rZW5pemVyLnNhdmVfcHJldHJhaW5lZChvdXRwdXRfZGlyKVx1MDAyNylcbiAgICByZXR1cm4gdG9rZW5pemVyXG5cbnNhbXBsZV9tc2dzID0gW1xuICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdzeXN0ZW1cdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IFx1MDAyN1lvdSBhcmUgYSBjb25jaXNlIGFzc2lzdGFudC5cdTAwMjd9LFxuICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBcdTAwMjdXaGF0IGlzIDIrMj9cdTAwMjd9LFxuICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdhc3Npc3RhbnRcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IFx1MDAyNzQuXHUwMDI3fSxcbiAgICB7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3dXNlclx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogXHUwMDI3V2h5P1x1MDAyN30sXG5dXG5mb3JtYXR0ZWQgPSBhcHBseV90ZW1wbGF0ZV9tYW51YWxseShzYW1wbGVfbXNncywgQ0hBVE1MX1RFTVBMQVRFKVxucHJpbnQoXHUwMDI3Q2hhdE1MIGZvcm1hdHRlZCBvdXRwdXQ6XHUwMDI3KVxucHJpbnQocmVwcihmb3JtYXR0ZWQpKVxucHJpbnQoZlx1MDAyN0xlbmd0aDoge2xlbihmb3JtYXR0ZWQpfSBjaGFyc1x1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyB3aXRoIFRlbXBsYXRlLUJhc2VkIExvc3MgTWFza2luZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIFNGVCB0cmFpbmluZyBvbiBtdWx0aS10dXJuIGNvbnZlcnNhdGlvbnMsIHRoZSBsb3NzIHNob3VsZCBiZSBjb21wdXRlZCBvbmx5IG9uIGFzc2lzdGFudCB0b2tlbnMg4oCUIHN5c3RlbSBhbmQgdXNlciB0b2tlbnMgYXJlIGlucHV0cywgbm90IGxlYXJuaW5nIHRhcmdldHMuIFRoZSBzdGFuZGFyZCBhcHByb2FjaDogKDEpIGFwcGx5IHRoZSBjaGF0IHRlbXBsYXRlIHRvIGdldCB0aGUgZnVsbCB0b2tlbiBzZXF1ZW5jZTsgKDIpIGZpbmQgdGhlIHRva2VuIHBvc2l0aW9ucyBvZiBlYWNoIGFzc2lzdGFudCByZXNwb25zZTsgKDMpIHNldCBsYWJlbHMgdG8gLTEwMCAoaWdub3JlZCBieSBjcm9zcy1lbnRyb3B5IGxvc3MpIGZvciBhbGwgbm9uLWFzc2lzdGFudCBwb3NpdGlvbnMuIFRoZSBhc3Npc3RhbnQgcmVzcG9uc2UgYm91bmRhcmllcyBhcmUgaWRlbnRpZmllZCBieSBlbmNvZGluZyB0aGUgcmVzcG9uc2UgdGV4dCBzZXBhcmF0ZWx5IGFuZCBzZWFyY2hpbmcgZm9yIHRoZSBtYXRjaGluZyB0b2tlbiBzdWJzZXF1ZW5jZSBpbiB0aGUgZnVsbCBzZXF1ZW5jZS4gSHVnZ2luZ0ZhY2UgVFJMXHUwMDI3cyBEYXRhQ29sbGF0b3JGb3JDb21wbGV0aW9uT25seUxNIGF1dG9tYXRlcyB0aGlzIG1hc2tpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXJcblxuZGVmIGNyZWF0ZV9zZnRfbGFiZWxzKG1lc3NhZ2VzLCB0b2tlbml6ZXIsIGlnbm9yZV9pbmRleD0tMTAwKTpcbiAgICAjIEFwcGx5IHRlbXBsYXRlLCBtYXNrIG5vbi1hc3Npc3RhbnQgdG9rZW5zIHdpdGggaWdub3JlX2luZGV4XG4gICAgZnVsbF90ZXh0ID0gdG9rZW5pemVyLmFwcGx5X2NoYXRfdGVtcGxhdGUobWVzc2FnZXMsIHRva2VuaXplPUZhbHNlLCBhZGRfZ2VuZXJhdGlvbl9wcm9tcHQ9RmFsc2UpXG4gICAgZW5jb2RpbmdzID0gdG9rZW5pemVyKGZ1bGxfdGV4dCwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcpXG4gICAgaW5wdXRfaWRzID0gZW5jb2RpbmdzW1x1MDAyN2lucHV0X2lkc1x1MDAyN11bMF1cbiAgICBsYWJlbHMgPSBpbnB1dF9pZHMuY2xvbmUoKVxuICAgICMgU3RhcnQgYnkgbWFza2luZyBldmVyeXRoaW5nLCB0aGVuIHVubWFzayBhc3Npc3RhbnQgcmVzcG9uc2UgdG9rZW5zXG4gICAgbGFiZWxzWzpdID0gaWdub3JlX2luZGV4XG4gICAgZm9yIG1zZyBpbiBtZXNzYWdlczpcbiAgICAgICAgaWYgbXNnW1x1MDAyN3JvbGVcdTAwMjddICE9IFx1MDAyN2Fzc2lzdGFudFx1MDAyNzpcbiAgICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgIHJlc3BfaWRzID0gdG9rZW5pemVyLmVuY29kZShtc2dbXHUwMDI3Y29udGVudFx1MDAyN10sIGFkZF9zcGVjaWFsX3Rva2Vucz1GYWxzZSlcbiAgICAgICAgcmVzcF9sZW4gPSBsZW4ocmVzcF9pZHMpXG4gICAgICAgIGZvciBpIGluIHJhbmdlKGxlbihpbnB1dF9pZHMpIC0gcmVzcF9sZW4gKyAxKTpcbiAgICAgICAgICAgIGlmIGlucHV0X2lkc1tpOmkgKyByZXNwX2xlbl0udG9saXN0KCkgPT0gcmVzcF9pZHM6XG4gICAgICAgICAgICAgICAgbGFiZWxzW2k6aSArIHJlc3BfbGVuXSA9IGlucHV0X2lkc1tpOmkgKyByZXNwX2xlbl1cbiAgICAgICAgICAgICAgICBicmVha1xuICAgIG5fc3VwZXJ2aXNlZCA9IChsYWJlbHMgIT0gaWdub3JlX2luZGV4KS5zdW0oKS5pdGVtKClcbiAgICBuX3RvdGFsID0gbGVuKGlucHV0X2lkcylcbiAgICBwcmludChmXHUwMDI3VG90YWwgdG9rZW5zOiB7bl90b3RhbH0sIHN1cGVydmlzZWQ6IHtuX3N1cGVydmlzZWR9LCBtYXNrZWQ6IHtuX3RvdGFsIC0gbl9zdXBlcnZpc2VkfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3U3VwZXJ2aXNpb24gcmF0aW86IHtuX3N1cGVydmlzZWQvbl90b3RhbDouMiV9IChhc3Npc3RhbnQgdG9rZW5zIG9ubHkpXHUwMDI3KVxuICAgIHJldHVybiB7XHUwMDI3aW5wdXRfaWRzXHUwMDI3OiBpbnB1dF9pZHMsIFx1MDAyN2xhYmVsc1x1MDAyNzogbGFiZWxzLFxuICAgICAgICAgICAgXHUwMDI3YXR0ZW50aW9uX21hc2tcdTAwMjc6IGVuY29kaW5nc1tcdTAwMjdhdHRlbnRpb25fbWFza1x1MDAyN11bMF19XG5cbm1zZ3MgPSBbXG4gICAge1x1MDAyN3JvbGVcdTAwMjc6IFx1MDAyN3N5c3RlbVx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogXHUwMDI3QmUgaGVscGZ1bC5cdTAwMjd9LFxuICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBcdTAwMjdXaGF0IGlzIFB5dGhvbj9cdTAwMjd9LFxuICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdhc3Npc3RhbnRcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IFx1MDAyN1B5dGhvbiBpcyBhIGhpZ2gtbGV2ZWwgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2Uga25vd24gZm9yIHJlYWRhYmlsaXR5Llx1MDAyN30sXG5dXG5wcmludChcdTAwMjdTRlQgbWFza2luZzogb25seSBhc3Npc3RhbnQgdG9rZW5zIGNvbnRyaWJ1dGUgdG8gdGhlIHRyYWluaW5nIGxvc3NcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVG9vbCBDYWxsaW5nIFRlbXBsYXRlIEZvcm1hdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG9vbCBjYWxsaW5nIGV4dGVuZHMgdGhlIGNoYXQgdGVtcGxhdGUgdG8gZW5jb2RlIGZ1bmN0aW9uIGRlZmluaXRpb25zLCBmdW5jdGlvbiBjYWxsIGludm9jYXRpb25zLCBhbmQgdG9vbCByZXN1bHRzIGFzIHBhcnQgb2YgdGhlIGNvbnZlcnNhdGlvbi4gTExhTUEtMy4xKyB1c2VzIGEgXHUwMDNjfHB5dGhvbl90YWd8XHUwMDNlIG9yIHNwZWNpYWwgSlNPTiBmb3JtYXQgd2l0aGluIHRoZSBhc3Npc3RhbnQgdHVybi4gTWlzdHJhbCB1c2VzIGEgW1RPT0xfQ0FMTFNdIG1hcmtlci4gTW9kZWxzIHRyYWluZWQgb24gdG9vbC11c2UgZGF0YSBleHBlY3QgdGhlIGV4YWN0IGZvcm1hdCB1c2VkIGR1cmluZyB0cmFpbmluZyDigJQgcGFzc2luZyB0b29scyB0byB0b2tlbml6ZXIuYXBwbHlfY2hhdF90ZW1wbGF0ZSgpIGZvcm1hdHMgdGhlbSBjb3JyZWN0bHkuIFRoZSB0b29sIGRlZmluaXRpb24gaXMgdHlwaWNhbGx5IGluamVjdGVkIGludG8gdGhlIHN5c3RlbSBwcm9tcHQgYXMgYSBKU09OIHNjaGVtYSwgYW5kIGZ1bmN0aW9uIGNhbGwgb3V0cHV0cyBhcmUgaW5qZWN0ZWQgYXMgdG9vbC1yb2xlIG1lc3NhZ2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQganNvblxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXJcblxuZGVmIGZvcm1hdF90b29sX2NvbnZlcnNhdGlvbih0b2tlbml6ZXIpOlxuICAgICMgRm9ybWF0IGEgdG9vbC11c2UgY29udmVyc2F0aW9uIHdpdGggZnVuY3Rpb24gY2FsbCBhbmQgcmVzdWx0XG4gICAgdG9vbHMgPSBbe1xuICAgICAgICBcdTAwMjd0eXBlXHUwMDI3OiBcdTAwMjdmdW5jdGlvblx1MDAyNyxcbiAgICAgICAgXHUwMDI3ZnVuY3Rpb25cdTAwMjc6IHtcbiAgICAgICAgICAgIFx1MDAyN25hbWVcdTAwMjc6IFx1MDAyN2dldF93ZWF0aGVyXHUwMDI3LFxuICAgICAgICAgICAgXHUwMDI3ZGVzY3JpcHRpb25cdTAwMjc6IFx1MDAyN0dldCBjdXJyZW50IHdlYXRoZXIgZm9yIGEgY2l0eVx1MDAyNyxcbiAgICAgICAgICAgIFx1MDAyN3BhcmFtZXRlcnNcdTAwMjc6IHtcbiAgICAgICAgICAgICAgICBcdTAwMjd0eXBlXHUwMDI3OiBcdTAwMjdvYmplY3RcdTAwMjcsXG4gICAgICAgICAgICAgICAgXHUwMDI3cHJvcGVydGllc1x1MDAyNzoge1x1MDAyN2xvY2F0aW9uXHUwMDI3OiB7XHUwMDI3dHlwZVx1MDAyNzogXHUwMDI3c3RyaW5nXHUwMDI3LCBcdTAwMjdkZXNjcmlwdGlvblx1MDAyNzogXHUwMDI3Q2l0eSBuYW1lXHUwMDI3fX0sXG4gICAgICAgICAgICAgICAgXHUwMDI3cmVxdWlyZWRcdTAwMjc6IFtcdTAwMjdsb2NhdGlvblx1MDAyN10sXG4gICAgICAgICAgICB9LFxuICAgICAgICB9LFxuICAgIH1dXG4gICAgbWVzc2FnZXMgPSBbXG4gICAgICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdzeXN0ZW1cdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IFx1MDAyN1lvdSBhcmUgYSBoZWxwZnVsIGFzc2lzdGFudCB3aXRoIHRvb2wgYWNjZXNzLlx1MDAyN30sXG4gICAgICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBcdTAwMjdXaGF0IGlzIHRoZSB3ZWF0aGVyIGluIFRva3lvP1x1MDAyN30sXG4gICAgICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdhc3Npc3RhbnRcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IE5vbmUsXG4gICAgICAgICBcdTAwMjd0b29sX2NhbGxzXHUwMDI3OiBbe1x1MDAyN2lkXHUwMDI3OiBcdTAwMjdjYWxsXzAwMVx1MDAyNywgXHUwMDI3dHlwZVx1MDAyNzogXHUwMDI3ZnVuY3Rpb25cdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgICAgICAgXHUwMDI3ZnVuY3Rpb25cdTAwMjc6IHtcdTAwMjduYW1lXHUwMDI3OiBcdTAwMjdnZXRfd2VhdGhlclx1MDAyNywgXHUwMDI3YXJndW1lbnRzXHUwMDI3OiBcdTAwMjd7XCJsb2NhdGlvblwiOiBcIlRva3lvXCJ9XHUwMDI3fX1dfSxcbiAgICAgICAge1x1MDAyN3JvbGVcdTAwMjc6IFx1MDAyN3Rvb2xcdTAwMjcsIFx1MDAyN3Rvb2xfY2FsbF9pZFx1MDAyNzogXHUwMDI3Y2FsbF8wMDFcdTAwMjcsXG4gICAgICAgICBcdTAwMjdjb250ZW50XHUwMDI3OiBcdTAwMjd7XCJ0ZW1wZXJhdHVyZVwiOiAyMiwgXCJjb25kaXRpb25cIjogXCJzdW5ueVwiLCBcImh1bWlkaXR5XCI6IDYwfVx1MDAyN30sXG4gICAgICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdhc3Npc3RhbnRcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IFx1MDAyN0l0IGlzIGN1cnJlbnRseSAyMiBkZWdyZWVzIENlbHNpdXMgYW5kIHN1bm55IGluIFRva3lvLlx1MDAyN30sXG4gICAgXVxuICAgIHRyeTpcbiAgICAgICAgZm9ybWF0dGVkID0gdG9rZW5pemVyLmFwcGx5X2NoYXRfdGVtcGxhdGUobWVzc2FnZXMsIHRvb2xzPXRvb2xzLCB0b2tlbml6ZT1GYWxzZSlcbiAgICAgICAgcHJpbnQoZlx1MDAyN1Rvb2wgY29udmVyc2F0aW9uIGZvcm1hdHRlZDoge2xlbihmb3JtYXR0ZWQpfSBjaGFyc1x1MDAyNylcbiAgICAgICAgcHJpbnQocmVwcihmb3JtYXR0ZWRbOjQwMF0pKVxuICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZTpcbiAgICAgICAgcHJpbnQoZlx1MDAyN1Rvb2wgZm9ybWF0dGluZyBlcnJvcjoge2V9XHUwMDI3KVxuICAgICAgICBwcmludChcdTAwMjdUb29sIGNhbGxpbmcgcmVxdWlyZXMgbW9kZWwtc3BlY2lmaWMgdGVtcGxhdGUgd2l0aCB0b29sIHN1cHBvcnRcdTAwMjcpXG4gICAgcmV0dXJuIGpzb24uZHVtcHMobWVzc2FnZXMsIGluZGVudD0yKVxuXG5wcmludChcdTAwMjdUb29sIGZvcm1hdDogZnVuY3Rpb24gZGVmcyBpbiBzeXN0ZW0sIGNhbGxzIGluIGFzc2lzdGFudCwgcmVzdWx0cyBpbiB0b29sIHJvbGVcdTAwMjcpXG5wcmludChcdTAwMjdUcmFpbmluZyByZXF1aXJlcyBleGFjdCBzYW1lIGZvcm1hdCBhcyBpbmZlcmVuY2UgZm9yIHJlbGlhYmxlIHRvb2wgaW52b2NhdGlvblx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDaGF0IFRlbXBsYXRlcyBBY3Jvc3MgTW9kZWwgRmFtaWxpZXMifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwgRmFtaWx5IiwiU3lzdGVtIFJvbGUiLCJUdXJuIERlbGltaXRlciIsIkVPUyBUb2tlbiIsIlRvb2wgU3VwcG9ydCIsIkZvcm1hdCBOYW1lIl0sInJvd3MiOltbIkxMYU1BLTMiLCJZZXMgKFx1MDAzY3xzdGFydF9oZWFkZXJfaWR8XHUwMDNlc3lzdGVtXHUwMDNjfGVuZF9oZWFkZXJfaWR8XHUwMDNlKSIsIlx1MDAzY3xlb3RfaWR8XHUwMDNlIiwiXHUwMDNjfGVvdF9pZHxcdTAwM2UiLCJZZXMgKHYzLjErKSIsIkxMYU1BLTMgZm9ybWF0Il0sWyJNaXN0cmFsIC8gTWl4dHJhbCIsIk5vIChpbmplY3RlZCBpbnRvIGZpcnN0IHVzZXIgdHVybikiLCJbSU5TVF0gLyBbL0lOU1RdIiwiXHUwMDNjL3NcdTAwM2UiLCJZZXMgKFtUT09MX0NBTExTXSkiLCJNaXN0cmFsIEluc3RydWN0Il0sWyJDaGF0TUwgKFF3ZW4sIG1hbnkgZmluZS10dW5lcykiLCJZZXMgKFx1MDAzY3xpbV9zdGFydHxcdTAwM2VzeXN0ZW0pIiwiXHUwMDNjfGltX2VuZHxcdTAwM2UiLCJcdTAwM2N8aW1fZW5kfFx1MDAzZSIsIlZhcmllcyBieSBmaW5lLXR1bmUiLCJDaGF0TUwiXSxbIlBoaS0zIiwiWWVzIChcdTAwM2N8c3lzdGVtfFx1MDAzZSkiLCJcdTAwM2N8ZW5kfFx1MDAzZSIsIlx1MDAzY3xlbmR8XHUwMDNlIiwiUGhpLTMuNSsgb25seSIsIlBoaS0zIGZvcm1hdCJdLFsiR2VtbWEiLCJObyBzeXN0ZW0gcm9sZSAoaWdub3JlZCkiLCJcdTAwM2NlbmRfb2ZfdHVyblx1MDAzZSIsIlx1MDAzY2Vvc1x1MDAzZSIsIkdlbW1hIDIrIHdpdGggdG9vbCB0YWciLCJHZW1tYSBmb3JtYXQiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbW1vbiBQaXRmYWxscyBhbmQgQmVzdCBQcmFjdGljZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtb3N0IGNvbW1vbiBwaXRmYWxsIGlzIHVzaW5nIHRoZSBiYXNlIG1vZGVsIHRva2VuaXplciB0ZW1wbGF0ZSBhdCBpbmZlcmVuY2UgZm9yIGEgZmluZS10dW5lZCBtb2RlbCB0aGF0IHdhcyB0cmFpbmVkIG9uIGEgZGlmZmVyZW50IHRlbXBsYXRlIOKAlCBvciBjb252ZXJzZWx5LCB1c2luZyB0aGUgZmluZS10dW5lZCB0ZW1wbGF0ZSBmb3IgYSBiYXNlIG1vZGVsIHRoYXQgd2FzIG5vdCB0cmFpbmVkIG9uIGl0LiBBbm90aGVyIGZyZXF1ZW50IG1pc3Rha2UgaXMgYXBwbHlpbmcgdGhlIHRlbXBsYXRlIG1hbnVhbGx5IHdpdGggc3RyaW5nIGZvcm1hdHRpbmcgaW5zdGVhZCBvZiB0b2tlbml6ZXIuYXBwbHlfY2hhdF90ZW1wbGF0ZSgpLCB3aGljaCBjYW4gcHJvZHVjZSBzdWJ0bGUgZGlmZmVyZW5jZXMgKG1pc3NpbmcgbmV3bGluZXMsIHdyb25nIHNwZWNpYWwgdG9rZW4gSURzKSB0aGF0IGRlZ3JhZGUgcXVhbGl0eS4gQWx3YXlzIHZlcmlmeSB0aGUgdGVtcGxhdGUgcHJvZHVjZXMgdGhlIGV4cGVjdGVkIHRva2VuIElEcyBieSBjb21wYXJpbmcgd2l0aCB0aGUgcmVmZXJlbmNlIHRlbXBsYXRlIG91dHB1dCBiZWZvcmUgdHJhaW5pbmcgb3IgZGVwbG95bWVudC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFsd2F5cyB1c2UgdG9rZW5pemVyLmFwcGx5X2NoYXRfdGVtcGxhdGUoKSDigJQgbmV2ZXIgZm9ybWF0IGNvbnZlcnNhdGlvbnMgbWFudWFsbHkgd2l0aCBzdHJpbmcgY29uY2F0ZW5hdGlvbi4iLCJDaGVjayB0b2tlbml6ZXIuY2hhdF90ZW1wbGF0ZSBpcyBub3QgTm9uZSBiZWZvcmUgaW5mZXJlbmNlIOKAlCBhIG1pc3NpbmcgdGVtcGxhdGUgaXMgYSBzaWxlbnQgZmFpbHVyZSBtb2RlLiIsIlZlcmlmeSBzcGVjaWFsIHRva2VucyAoaW1fc3RhcnQsIGVvdF9pZCwgZXRjLikgYXJlIGluIHRoZSB0b2tlbml6ZXIgdm9jYWJ1bGFyeSDigJQgbWlzc2luZyBzcGVjaWFsIHRva2VucyBhcmUgbWFwcGVkIHRvIFVOSyBhbmQgYnJlYWsgdGhlIGZvcm1hdC4iLCJVc2UgYWRkX2dlbmVyYXRpb25fcHJvbXB0PVRydWUgYXQgaW5mZXJlbmNlIGFuZCBhZGRfZ2VuZXJhdGlvbl9wcm9tcHQ9RmFsc2UgYXQgdHJhaW5pbmcgdG8gYXZvaWQgdHJhaW5pbmcgb24gdGhlIGdlbmVyYXRpb24gcHJlZml4LiIsIkZvciBtdWx0aS10dXJuIFNGVCBkYXRhc2V0cywgdmVyaWZ5IHRoZSBzdXBlcnZpc2lvbiByYXRpbyAoYXNzaXN0YW50IHRva2VucyAvIHRvdGFsIHRva2Vucykg4oCUIGJlbG93IDIwJSBvZnRlbiBpbmRpY2F0ZXMgYSBtYXNraW5nIGJ1Zy4iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJUZW1wbGF0ZSBNaXNtYXRjaCBTaWxlbnRseSBEZWdyYWRlcyBRdWFsaXR5IiwiY29udGVudCI6IkFwcGx5aW5nIHRoZSB3cm9uZyBjaGF0IHRlbXBsYXRlIGF0IGluZmVyZW5jZSB0aW1lIGNhdXNlcyB0aGUgbW9kZWwgdG8gZmFpbCB0byBmb2xsb3cgaW5zdHJ1Y3Rpb25zIOKAlCBldmVuIGEgbWlub3IgZGlmZmVyZW5jZSAobWlzc2luZyBuZXdsaW5lLCB3cm9uZyBzZXBhcmF0b3IpIGJyZWFrcyB0aGUgZXhwZWN0ZWQgZm9ybWF0IHRoZSBtb2RlbCB3YXMgdHJhaW5lZCBvbiBhbmQgcHJvZHVjZXMgZ2VuZXJpYyBvciByZXBlYXRlZCB0ZXh0LiBBbHdheXMgbWF0Y2ggdGhlIGluZmVyZW5jZSB0ZW1wbGF0ZSBleGFjdGx5IHRvIHRoZSB0cmFpbmluZyB0ZW1wbGF0ZSwgaW5jbHVkaW5nIHdoaXRlc3BhY2UgZGV0YWlscy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Chat Templates — System/User/Assistant Format and Tokenizer Integration

Chat templates define how multi-turn conversations between system, user, and assistant roles are serialized into a flat token sequence for language model input. Each model family uses a distinct format with unique role delimiters, special tokens, and turn boundaries. HuggingFace stores these templates as Jinja2 strings in tokenizer_config.json and exposes them via tokenizer.apply_chat_template(). Using the correct template at both training and inference time is non-negotiable — even minor format differences cause the model to fail to follow instructions or produce repetitive text.

## Why Chat Templates Matter

Chat-tuned models are trained on millions of conversations formatted according to a specific template. The model learns to associate role delimiter tokens with behavioral patterns: after the assistant header token, the model generates a response; after the user header token, it switches to listening mode. If you apply the wrong template at inference time — wrong delimiters, missing newlines, wrong EOS token — the model sees a format it was not trained on, which degrades generation quality significantly. The failure mode is subtle: the model may still generate text, but it ignores the system prompt, fails to stop at the right turn boundary, or produces generic completions.

## Applying Built-in Templates with HuggingFace

tokenizer.apply_chat_template() is the standard API for converting a list of role-content dicts to a formatted string or token IDs. The key parameters: tokenize=True to get token IDs (for model input), tokenize=False to get the formatted string (for inspection); add_generation_prompt=True appends the start of the assistant turn to prompt the model to generate a response. The template is sourced from tokenizer.chat_template — a Jinja2 string in tokenizer_config.json. For models without a built-in template, a ValueError is raised, indicating the model was not trained with a standard chat format.

```python
from transformers import AutoTokenizer

def compare_chat_templates(user_prompt, system_msg='You are a helpful assistant.'):
    # Apply and compare chat templates for LLaMA-3 and Mistral
    messages_with_system = [
        {'role': 'system', 'content': system_msg},
        {'role': 'user', 'content': user_prompt},
    ]
    messages_no_system = [{'role': 'user', 'content': user_prompt}]
    model_configs = [
        ('meta-llama/Meta-Llama-3-8B-Instruct', True),
        ('mistralai/Mistral-7B-Instruct-v0.3', False),
    ]
    for model_id, supports_system in model_configs:
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            msgs = messages_with_system if supports_system else messages_no_system
            formatted = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
            tokens = tokenizer.apply_chat_template(msgs, tokenize=True, add_generation_prompt=True)
            print(f'--- {model_id} ---')
            print(f'Formatted ({len(tokens)} tokens):')
            print(repr(formatted[:250]))
            print()
        except Exception as e:
            print(f'{model_id}: {e}')

def inspect_template(model_id):
    tok = AutoTokenizer.from_pretrained(model_id)
    tmpl = tok.chat_template or 'No chat_template found'
    print(f'Template ({len(tmpl)} chars):', tmpl[:200], '...')

compare_chat_templates('Explain transformer attention in 3 sentences.')
print('Template mismatch at inference -> generic output or instruction-following failure')
```

## Custom Jinja2 Templates

When a model lacks a built-in template or you need a custom format, you can write a Jinja2 template and assign it to tokenizer.chat_template. The template has access to the messages list and add_generation_prompt boolean. Role names are accessed via message['role'] and content via message['content']. The template is saved to tokenizer_config.json when you call tokenizer.save_pretrained(), persisting it for future use. ChatML is the most widely adopted custom format — it was popularized by OpenAI and is used as the default for many open-source models fine-tuned without format specification.

```python
from transformers import AutoTokenizer
from jinja2 import Environment

CHATML_TEMPLATE = (
    '{%- for message in messages %}'
    '{%- if message["role"] == "system" %}<|im_start|>system\n{{ message["content"] }}<|im_end|>\n'
    '{%- elif message["role"] == "user" %}<|im_start|>user\n{{ message["content"] }}<|im_end|>\n'
    '{%- elif message["role"] == "assistant" %}<|im_start|>assistant\n{{ message["content"] }}<|im_end|>\n'
    '{%- endif %}{%- endfor %}'
    '{%- if add_generation_prompt %}<|im_start|>assistant\n{%- endif %}'
)

def apply_template_manually(messages, template_str, add_generation_prompt=True):
    # Apply Jinja2 template without a tokenizer (for inspection/testing)
    env = Environment()
    tmpl = env.from_string(template_str)
    return tmpl.render(messages=messages, add_generation_prompt=add_generation_prompt)

def register_custom_template(base_model_id, custom_template):
    # Assign custom chat template to tokenizer and save
    tokenizer = AutoTokenizer.from_pretrained(base_model_id)
    tokenizer.chat_template = custom_template
    print(f'Template registered: {len(custom_template)} chars')
    print('Save with: tokenizer.save_pretrained(output_dir)')
    return tokenizer

sample_msgs = [
    {'role': 'system', 'content': 'You are a concise assistant.'},
    {'role': 'user', 'content': 'What is 2+2?'},
    {'role': 'assistant', 'content': '4.'},
    {'role': 'user', 'content': 'Why?'},
]
formatted = apply_template_manually(sample_msgs, CHATML_TEMPLATE)
print('ChatML formatted output:')
print(repr(formatted))
print(f'Length: {len(formatted)} chars')
```

## Training with Template-Based Loss Masking

For SFT training on multi-turn conversations, the loss should be computed only on assistant tokens — system and user tokens are inputs, not learning targets. The standard approach: (1) apply the chat template to get the full token sequence; (2) find the token positions of each assistant response; (3) set labels to -100 (ignored by cross-entropy loss) for all non-assistant positions. The assistant response boundaries are identified by encoding the response text separately and searching for the matching token subsequence in the full sequence. HuggingFace TRL's DataCollatorForCompletionOnlyLM automates this masking.

```python
import torch
from transformers import AutoTokenizer

def create_sft_labels(messages, tokenizer, ignore_index=-100):
    # Apply template, mask non-assistant tokens with ignore_index
    full_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    encodings = tokenizer(full_text, return_tensors='pt')
    input_ids = encodings['input_ids'][0]
    labels = input_ids.clone()
    # Start by masking everything, then unmask assistant response tokens
    labels[:] = ignore_index
    for msg in messages:
        if msg['role'] != 'assistant':
            continue
        resp_ids = tokenizer.encode(msg['content'], add_special_tokens=False)
        resp_len = len(resp_ids)
        for i in range(len(input_ids) - resp_len + 1):
            if input_ids[i:i + resp_len].tolist() == resp_ids:
                labels[i:i + resp_len] = input_ids[i:i + resp_len]
                break
    n_supervised = (labels != ignore_index).sum().item()
    n_total = len(input_ids)
    print(f'Total tokens: {n_total}, supervised: {n_supervised}, masked: {n_total - n_supervised}')
    print(f'Supervision ratio: {n_supervised/n_total:.2%} (assistant tokens only)')
    return {'input_ids': input_ids, 'labels': labels,
            'attention_mask': encodings['attention_mask'][0]}

msgs = [
    {'role': 'system', 'content': 'Be helpful.'},
    {'role': 'user', 'content': 'What is Python?'},
    {'role': 'assistant', 'content': 'Python is a high-level programming language known for readability.'},
]
print('SFT masking: only assistant tokens contribute to the training loss')
```

## Tool Calling Template Format

Tool calling extends the chat template to encode function definitions, function call invocations, and tool results as part of the conversation. LLaMA-3.1+ uses a <|python_tag|> or special JSON format within the assistant turn. Mistral uses a [TOOL_CALLS] marker. Models trained on tool-use data expect the exact format used during training — passing tools to tokenizer.apply_chat_template() formats them correctly. The tool definition is typically injected into the system prompt as a JSON schema, and function call outputs are injected as tool-role messages.

```python
import json
from transformers import AutoTokenizer

def format_tool_conversation(tokenizer):
    # Format a tool-use conversation with function call and result
    tools = [{
        'type': 'function',
        'function': {
            'name': 'get_weather',
            'description': 'Get current weather for a city',
            'parameters': {
                'type': 'object',
                'properties': {'location': {'type': 'string', 'description': 'City name'}},
                'required': ['location'],
            },
        },
    }]
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant with tool access.'},
        {'role': 'user', 'content': 'What is the weather in Tokyo?'},
        {'role': 'assistant', 'content': None,
         'tool_calls': [{'id': 'call_001', 'type': 'function',
                         'function': {'name': 'get_weather', 'arguments': '{"location": "Tokyo"}'}}]},
        {'role': 'tool', 'tool_call_id': 'call_001',
         'content': '{"temperature": 22, "condition": "sunny", "humidity": 60}'},
        {'role': 'assistant', 'content': 'It is currently 22 degrees Celsius and sunny in Tokyo.'},
    ]
    try:
        formatted = tokenizer.apply_chat_template(messages, tools=tools, tokenize=False)
        print(f'Tool conversation formatted: {len(formatted)} chars')
        print(repr(formatted[:400]))
    except Exception as e:
        print(f'Tool formatting error: {e}')
        print('Tool calling requires model-specific template with tool support')
    return json.dumps(messages, indent=2)

print('Tool format: function defs in system, calls in assistant, results in tool role')
print('Training requires exact same format as inference for reliable tool invocation')
```

## Chat Templates Across Model Families

| Model Family | System Role | Turn Delimiter | EOS Token | Tool Support | Format Name |
| --- | --- | --- | --- | --- | --- |
| LLaMA-3 | Yes (<|start_header_id|>system<|end_header_id|>) | <|eot_id|> | <|eot_id|> | Yes (v3.1+) | LLaMA-3 format |
| Mistral / Mixtral | No (injected into first user turn) | [INST] / [/INST] | </s> | Yes ([TOOL_CALLS]) | Mistral Instruct |
| ChatML (Qwen, many fine-tunes) | Yes (<|im_start|>system) | <|im_end|> | <|im_end|> | Varies by fine-tune | ChatML |
| Phi-3 | Yes (<|system|>) | <|end|> | <|end|> | Phi-3.5+ only | Phi-3 format |
| Gemma | No system role (ignored) | <end_of_turn> | <eos> | Gemma 2+ with tool tag | Gemma format |

## Common Pitfalls and Best Practices

The most common pitfall is using the base model tokenizer template at inference for a fine-tuned model that was trained on a different template — or conversely, using the fine-tuned template for a base model that was not trained on it. Another frequent mistake is applying the template manually with string formatting instead of tokenizer.apply_chat_template(), which can produce subtle differences (missing newlines, wrong special token IDs) that degrade quality. Always verify the template produces the expected token IDs by comparing with the reference template output before training or deployment.

- Always use tokenizer.apply_chat_template() — never format conversations manually with string concatenation.
- Check tokenizer.chat_template is not None before inference — a missing template is a silent failure mode.
- Verify special tokens (im_start, eot_id, etc.) are in the tokenizer vocabulary — missing special tokens are mapped to UNK and break the format.
- Use add_generation_prompt=True at inference and add_generation_prompt=False at training to avoid training on the generation prefix.
- For multi-turn SFT datasets, verify the supervision ratio (assistant tokens / total tokens) — below 20% often indicates a masking bug.

> **Template Mismatch Silently Degrades Quality**: Applying the wrong chat template at inference time causes the model to fail to follow instructions — even a minor difference (missing newline, wrong separator) breaks the expected format the model was trained on and produces generic or repeated text. Always match the inference template exactly to the training template, including whitespace details.

---

