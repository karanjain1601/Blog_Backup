---
title: "Efficient ViT: Token Merging and Reduction Strategies"
slug: "efficient-vit-token-merging"
description: "A practical guide to token merging, pruning, and pooling strategies that cut ViT inference cost by 1.5–3× with minimal accuracy loss."
tags: ["vision-transformer", "efficiency", "token-merging", "pruning", "inference"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBWaVRzIHNjYWxlIHF1YWRyYXRpY2FsbHkgd2l0aCB0b2tlbiBjb3VudDogYSAyMjRweCBpbWFnZSBhdCBwYXRjaCBzaXplIDE2IHByb2R1Y2VzIDE5NiB0b2tlbnMsIGJ1dCBhdCA1MTJweCB0aGF0IGJlY29tZXMgMTAyNCB0b2tlbnMgYW5kIGF0dGVudGlvbiBjb3N0IGdyb3dzIDI3w5cuIFRva2VuIHJlZHVjdGlvbiBzdHJhdGVnaWVzIOKAlCBtZXJnaW5nLCBwcnVuaW5nLCBvciBwb29saW5nIOKAlCBicmVhayB0aGlzIGJvdHRsZW5lY2sgYnkgcmVkdWNpbmcgZWZmZWN0aXZlIHNlcXVlbmNlIGxlbmd0aCB3aGlsZSBwcmVzZXJ2aW5nIG1vc3QgaW5mb3JtYXRpb24gY29udGVudCBmb3IgZG93bnN0cmVhbSB0YXNrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjb3JlIG9ic2VydmF0aW9uIG1vdGl2YXRpbmcgdG9rZW4gcmVkdWN0aW9uIGlzIHRoYXQgaW1hZ2UgcGF0Y2hlcyBhcmUgaGlnaGx5IHJlZHVuZGFudC4gSW4gbmF0dXJhbCBpbWFnZXMsIGFkamFjZW50IHBhdGNoZXMgc2hhcmUgY29sb3IsIHRleHR1cmUsIGFuZCBzZW1hbnRpYyBjb250ZW50LiBBIG1vZGVsIHByb2Nlc3NpbmcgYSB1bmlmb3JtIHNreSByZWdpb24gY29tcHV0ZXMgbmVhcmx5IGlkZW50aWNhbCBhdHRlbnRpb24gcGF0dGVybnMgYWNyb3NzIGRvemVucyBvZiB0b2tlbnMuIElkZW50aWZ5aW5nIGFuZCBjb2xsYXBzaW5nIHRoZXNlIHJlZHVuZGFudCB0b2tlbnMgaXMgdGhlIGNlbnRyYWwgY2hhbGxlbmdlIG9mIGVmZmljaWVudCBWaVQgZGVzaWduLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJUaXAiLCJjb250ZW50IjoiVG9NZSByZXF1aXJlcyB6ZXJvIHJldHJhaW5pbmcg4oCUIHBsdWcgaXQgaW50byBhbnkgcHJldHJhaW5lZCBWaVQgYnkgd3JhcHBpbmcgdGhlIGF0dGVudGlvbiBtb2R1bGUuIFN0YXJ0IGF0IHI9OCBmb3IgfjEuNXggc3BlZWR1cCB3aXRoIFx1MDAzYzAuMyUgYWNjdXJhY3kgZHJvcC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUb2tlbiBSZWR1bmRhbmN5IGluIEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXR0ZW50aW9uIG1hcHMgaW4gZWFybHkgVmlUIGxheWVycyBzaG93IHN0cm9uZyBzcGF0aWFsIGxvY2FsaXR5OiBtb3N0IHRva2VucyBhdHRlbmQgcHJpbWFyaWx5IHRvIGltbWVkaWF0ZSBuZWlnaGJvcnMuIEluIGxhdGVyIGxheWVycywgZ2xvYmFsIHNlbWFudGljcyBlbWVyZ2UgYnV0IG1hbnkgdG9rZW5zIHN0aWxsIGNhcnJ5IG5lYXJseSBpZGVudGljYWwga2V5LXF1ZXJ5IHJlcHJlc2VudGF0aW9ucy4gTWVhc3VyaW5nIHBhaXJ3aXNlIGNvc2luZSBzaW1pbGFyaXR5IGJldHdlZW4gdG9rZW4gZmVhdHVyZXMgcmV2ZWFscyB0aGF0IDMw4oCTNTAlIG9mIHRva2VucyBoYXZlIGF0IGxlYXN0IG9uZSBuZWFyLWR1cGxpY2F0ZSAoc2ltIFx1MDAzZSAwLjkpIGluIHR5cGljYWwgSW1hZ2VOZXQgaW1hZ2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIENvbXB1dGUgdG9rZW4gc2ltaWxhcml0eSBtYXRyaXg7IHRocmVzaG9sZCBhdCB0YXUgdG8gZmluZCBtZXJnZWFibGUgcGFpcnNcbmltcG9ydCB0b3JjaFxuXG5kZWYgdG9rZW5fc2ltaWxhcml0eSh4LCB0YXU9MC45KTpcbiAgICAjIHg6IChCLCBOLCBEKSB0b2tlbiBmZWF0dXJlc1xuICAgIGQgPSB4LnNoYXBlWy0xXVxuICAgIHhfbm9ybSA9IHggLyB4Lm5vcm0oZGltPS0xLCBrZWVwZGltPVRydWUpXG4gICAgc2ltID0gKHhfbm9ybSBAIHhfbm9ybS50cmFuc3Bvc2UoLTEsIC0yKSkgLyAoZCAqKiAwLjUpICAjIChCLCBOLCBOKVxuICAgIG1hc2sgPSB0b3JjaC5leWUoc2ltLnNoYXBlWy0xXSwgZGV2aWNlPXguZGV2aWNlKS5ib29sKClcbiAgICBzaW0gPSBzaW0ubWFza2VkX2ZpbGwobWFzay51bnNxdWVlemUoMCksIC0xLjApXG4gICAgbWVyZ2VhYmxlID0gKHNpbSBcdTAwM2UgdGF1KS5hbnkoZGltPS0xKSAgICMgKEIsIE4pIGJvb2xlYW4gbWFza1xuICAgIHJlZHVuZGFuY3kgPSBtZXJnZWFibGUuZmxvYXQoKS5tZWFuKClcbiAgICByZXR1cm4gc2ltLCByZWR1bmRhbmN5XG5cbnNpbV9tYXQsIHJlZCA9IHRva2VuX3NpbWlsYXJpdHkocGF0Y2hfdG9rZW5zKVxucHJpbnQoZlx1MDAyN1Rva2VuIHJlZHVuZGFuY3k6IHtyZWQ6LjElfVx1MDAyNykifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlZHVuZGFuY3kgaXMgbm90IHVuaWZvcm1seSBkaXN0cmlidXRlZCBhY3Jvc3MgbGF5ZXJzLiBFYXJseSBibG9ja3Mgc2hvdyBoaWdoIHNwYXRpYWwgcmVkdW5kYW5jeSAoYWRqYWNlbnQgcGF0Y2hlcyk7IG1pZGRsZSBibG9ja3Mgc2hvdyBzZW1hbnRpYyByZWR1bmRhbmN5IChzYW1lLW9iamVjdCBwYXRjaGVzKTsgZmluYWwgYmxvY2tzIGFyZSBtb3N0IGRpdmVyc2Ugc2luY2UgZWFjaCB0b2tlbiBoYXMgYWNjdW11bGF0ZWQgZ2xvYmFsIGNvbnRleHQuIFRoaXMgcHJvZmlsZSBtb3RpdmF0ZXMgYXBwbHlpbmcgbW9yZSBhZ2dyZXNzaXZlIHJlZHVjdGlvbiBpbiBlYXJseSBsYXllcnMgYW5kIHByZXNlcnZpbmcgbW9yZSB0b2tlbnMgaW4gbGF0ZXIgbGF5ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRva2VuIE1lcmdpbmcgKFRvTWUpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUb2tlbiBNZXJnaW5nIChUb01lKSBieSBCb2x5YSBldCBhbC4gMjAyMyBpbnRyb2R1Y2VzIGEgdHJhaW5pbmctZnJlZSBtZXRob2QgdG8gcmVkdWNlIFZpVCB0b2tlbiBjb3VudCBhdCBpbmZlcmVuY2UuIEF0IGVhY2ggdHJhbnNmb3JtZXIgYmxvY2ssIGl0IHBhcnRpdGlvbnMgdG9rZW5zIGludG8gdHdvIHNldHMg4oCUIHNvdXJjZSAoc3JjKSBhbmQgZGVzdGluYXRpb24gKGRzdCkg4oCUIHVzaW5nIGJpcGFydGl0ZSBtYXRjaGluZy4gVGhlIHRvcC1yIG1vc3Qgc2ltaWxhciBzcmMtZHN0IHBhaXJzIGFyZSBtZXJnZWQgYnkgYXZlcmFnaW5nIHRoZWlyIGZlYXR1cmVzLCByZWR1Y2luZyB0aGUgc2VxdWVuY2UgYnkgciB0b2tlbnMgcGVyIGJsb2NrLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIFRvTWUgYmlwYXJ0aXRlIG1hdGNoaW5nOiBtZXJnZSB0b3AtciBzcmMgdG9rZW5zIGludG8gbmVhcmVzdCBkc3QgdG9rZW5zXG5pbXBvcnQgdG9yY2hcblxuZGVmIHRvbWVfbWVyZ2UoeCwgcik6XG4gICAgIyB4OiAoQiwgTiwgRCk7IHI6IHRva2VucyB0byBtZXJnZSBwZXIgYmxvY2tcbiAgICBCLCBOLCBEID0geC5zaGFwZVxuICAgIHNyYyA9IHhbOiwgMTo6MiwgOl0gICAjIG9kZC1pbmRleGVkIHRva2Vuc1xuICAgIGRzdCA9IHhbOiwgMDo6MiwgOl0gICAjIGV2ZW4taW5kZXhlZCB0b2tlbnNcbiAgICBzcmNfbiA9IHNyYyAvIHNyYy5ub3JtKGRpbT0tMSwga2VlcGRpbT1UcnVlKVxuICAgIGRzdF9uID0gZHN0IC8gZHN0Lm5vcm0oZGltPS0xLCBrZWVwZGltPVRydWUpXG4gICAgc2ltID0gc3JjX24gQCBkc3Rfbi50cmFuc3Bvc2UoLTEsIC0yKSAgICMgKEIsIE4vLzIsIE4vLzIpXG4gICAgc2NvcmVzLCBiZXN0X2RzdCA9IHNpbS5tYXgoZGltPS0xKSAgICAgICMgcGVyLXNyYyBiZXN0IGRzdFxuICAgIF8sIHRvcF9yX2lkeCA9IHNjb3Jlcy50b3BrKHIsIGRpbT0tMSkgICMgdG9wLXIgc3JjIGJ5IHNpbWlsYXJpdHlcbiAgICBmb3IgYiBpbiByYW5nZShCKTpcbiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uocik6XG4gICAgICAgICAgICBzX2kgPSB0b3Bfcl9pZHhbYiwgaV1cbiAgICAgICAgICAgIGRfaSA9IGJlc3RfZHN0W2IsIHNfaV1cbiAgICAgICAgICAgIGRzdFtiLCBkX2ldID0gKGRzdFtiLCBkX2ldICsgc3JjW2IsIHNfaV0pIC8gMlxuICAgIHJldHVybiBkc3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvTWUgb3BlcmF0ZXMgaW5zaWRlIHRoZSBhdHRlbnRpb24gbW9kdWxlIGJlZm9yZSB0aGUgc29mdG1heCwgc28gbWVyZ2VkIHRva2VucyByZWR1Y2UgYm90aCB0aGUgUUteVCBtYXRyaXggc2l6ZSBhbmQgZmVlZGZvcndhcmQgY29tcHV0YXRpb24gaW4gdGhlIHNhbWUgYmxvY2suIE5vIGdyYWRpZW50IGZsb3dzIHRocm91Z2ggdGhlIG1lcmdlIG9wZXJhdGlvbiBhdCBpbmZlcmVuY2UsIGJ1dCBkdXJpbmcgdHJhaW5pbmctYXdhcmUgVG9NZSwgYSBzdHJhaWdodC10aHJvdWdoIGVzdGltYXRvciBhbGxvd3MgdGhlIG1lcmdlIHNjaGVkdWxlIHRvIGJlIGxlYXJuZWQgam9pbnRseSB3aXRoIHRoZSBuZXR3b3JrIHdlaWdodHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVG9rZW4gUHJ1bmluZyBhbmQgUG9vbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG9rZW4gcHJ1bmluZyB0YWtlcyBhIGhhcmRlciBkZWNpc2lvbiB0aGFuIG1lcmdpbmc6IHRva2VucyBiZWxvdyBhIHJlbGV2YW5jZSB0aHJlc2hvbGQgYXJlIGRyb3BwZWQgZW50aXJlbHkgcmF0aGVyIHRoYW4gYXZlcmFnZWQgaW50byBuZWlnaGJvcnMuIER5bmFtaWNWaVQgcHJlZGljdHMgcGVyLXRva2VuIGltcG9ydGFuY2Ugc2NvcmVzIHdpdGggYSBsaWdodHdlaWdodCAyLWxheWVyIE1MUCwgdGhlbiB1c2VzIEd1bWJlbC1zb2Z0bWF4IHRvIG1ha2UgdGhlIGRyb3AgZGVjaXNpb24gZGlmZmVyZW50aWFibGUgZHVyaW5nIHRyYWluaW5nLiBBdCBpbmZlcmVuY2UgdGhlIEd1bWJlbCBub2lzZSBpcyByZW1vdmVkIGFuZCBzY29yZXMgYXJlIHRocmVzaG9sZGVkIGRldGVybWluaXN0aWNhbGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIER5bmFtaWNWaVQ6IHByZWRpY3QgdG9rZW4ga2VlcCBzY29yZXMgd2l0aCBNTFAsIEd1bWJlbC1zb2Z0bWF4IGRyb3BcbmltcG9ydCB0b3JjaCwgdG9yY2gubm4gYXMgbm4sIHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBUb2tlblByZWRpY3Rvcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW0pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5zY29yZSA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZGltLCBkaW0gLy8gNCksIG5uLkdFTFUoKSwgbm4uTGluZWFyKGRpbSAvLyA0LCAyKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIGtlZXBfcmF0aW89MC43LCB0cmFpbmluZz1UcnVlKTpcbiAgICAgICAgbG9naXRzID0gc2VsZi5zY29yZSh4KSAgICAgICAgICAgICMgKEIsIE4sIDIpOiBbZHJvcCwga2VlcF1cbiAgICAgICAgaWYgdHJhaW5pbmc6XG4gICAgICAgICAgICBkZWNpc2lvbnMgPSBGLmd1bWJlbF9zb2Z0bWF4KGxvZ2l0cywgdGF1PTEuMCwgaGFyZD1UcnVlKVxuICAgICAgICAgICAga2VlcF9tYXNrID0gZGVjaXNpb25zWy4uLiwgMV1cbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIHNjb3JlcyA9IGxvZ2l0cy5zb2Z0bWF4KC0xKVsuLi4sIDFdXG4gICAgICAgICAgICB0b3BrID0gaW50KHguc2hhcGVbMV0gKiBrZWVwX3JhdGlvKVxuICAgICAgICAgICAgXywgaWR4ID0gc2NvcmVzLnRvcGsodG9waywgZGltPS0xKVxuICAgICAgICAgICAga2VlcF9tYXNrID0gdG9yY2guemVyb3NfbGlrZShzY29yZXMpLnNjYXR0ZXJfKC0xLCBpZHgsIDEuMClcbiAgICAgICAgcmV0dXJuIHggKiBrZWVwX21hc2sudW5zcXVlZXplKC0xKSwga2VlcF9tYXNrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTcGF0aWFsIHBvb2xpbmcgaXMgdGhlIHNpbXBsZXN0IHJlZHVjdGlvbjogYXBwbHkgYXZlcmFnZSBwb29saW5nIG92ZXIgMsOXMiB3aW5kb3dzIG9mIHBhdGNoIHRva2VucywgcmVkdWNpbmcgdGhlIHNlcXVlbmNlIGJ5IDTDlyBwZXIgcG9vbGluZyBzdGFnZS4gVGhpcyBpcyB0aGUgYXBwcm9hY2ggdXNlZCBpbiBQVlQgYW5kIFR3aW5zLiBVbmxpa2UgbWVyZ2luZyBvciBwcnVuaW5nLCBwb29saW5nIGlzIGNvbnRlbnQtYWdub3N0aWMg4oCUIGl0IGFsd2F5cyByZWR1Y2VzIGJ5IGEgZml4ZWQgZmFjdG9yIHJlZ2FyZGxlc3Mgb2YgaW1hZ2UgY29udGVudCDigJQgYnV0IGl0IGNvbXBvc2VzIG5hdHVyYWxseSB3aXRoIGNvbnZvbHV0aW9uIGFuZCByZXF1aXJlcyBubyBsZWFybmVkIHNlbGVjdGlvbiBtZWNoYW5pc20uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3BlZWQtQWNjdXJhY3kgVHJhZGVvZmZzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZW5jaG1hcmtpbmcgdG9rZW4gcmVkdWN0aW9uIHJlcXVpcmVzIG1lYXN1cmluZyB0aHJvdWdocHV0IGF0IGEgZml4ZWQgYmF0Y2ggc2l6ZSBhbmQgcmVzb2x1dGlvbiwgbm90IGp1c3QgRkxPUHMuIFdhbGwtY2xvY2sgc3BlZWR1cCBvZnRlbiBkZXZpYXRlcyBmcm9tIEZMT1AgcmVkdWN0aW9uIGJlY2F1c2UgdG9rZW4gcmVkdWN0aW9uIGludHJvZHVjZXMgaXJyZWd1bGFyIGNvbXB1dGF0aW9uIHBhdHRlcm5zIHRoYXQgR1BVcyBoYW5kbGUgbGVzcyBlZmZpY2llbnRseSB0aGFuIHVuaWZvcm0gbWF0bXVsIG9wZXJhdGlvbnMuIFRvTWUgYXQgcj04IHJlZHVjZXMgRkxPUHMgYnkgfjMwJSBidXQgYWNoaWV2ZXMgb25seSB+MS41w5cgd2FsbC1jbG9jayBzcGVlZHVwIGR1ZSB0byBvdmVyaGVhZCBmcm9tIHRoZSBtZXJnZSBib29ra2VlcGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBCZW5jaG1hcmsgdGhyb3VnaHB1dCBhdCB2YXJ5aW5nIHIgbWVyZ2UgYnVkZ2V0c1xuaW1wb3J0IHRvcmNoLCB0aW1lXG5cbmRlZiBiZW5jaG1hcmsobW9kZWwsIHJfdmFsdWVzPVswLCA4LCAxNiwgMjRdLCBiYXRjaD0zMiwgcnVucz0xMDApOlxuICAgIHggPSB0b3JjaC5yYW5kbihiYXRjaCwgMywgMjI0LCAyMjQpLmN1ZGEoKVxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciByIGluIHJfdmFsdWVzOlxuICAgICAgICBtb2RlbC5zZXRfdG9tZV9yKHIpICAgICAjIHNldHMgbWVyZ2UgYnVkZ2V0IHBlciBibG9ja1xuICAgICAgICBmb3IgXyBpbiByYW5nZSgxMCk6ICAgICAjIHdhcm11cFxuICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6IG1vZGVsKHgpXG4gICAgICAgIHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuICAgICAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2UocnVucyk6XG4gICAgICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTogbW9kZWwoeClcbiAgICAgICAgdG9yY2guY3VkYS5zeW5jaHJvbml6ZSgpXG4gICAgICAgIGltZ3NfcGVyX3NlYyA9IChiYXRjaCAqIHJ1bnMpIC8gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MClcbiAgICAgICAgcmVzdWx0cy5hcHBlbmQoe1x1MDAyN3JcdTAwMjc6IHIsIFx1MDAyN2ltZ3NfcGVyX3NlY1x1MDAyNzogaW1nc19wZXJfc2VjfSlcbiAgICByZXR1cm4gcmVzdWx0cyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJSZWR1Y3Rpb24iLCJUaHJvdWdocHV0IEdhaW4iLCJUb3AtMSBEcm9wIiwiQ29tcGF0aWJsZSBXaXRoIl0sInJvd3MiOltbIlRvTWUgcj04IiwifjE1JSIsIjEuNXgiLCJcdTAwM2MwLjMlIiwiQW55IHByZXRyYWluZWQgVmlUIl0sWyJUb01lIHI9MTYiLCJ+MzAlIiwiMS45eCIsIjAuNSUiLCJBbnkgcHJldHJhaW5lZCBWaVQiXSxbIkR5bmFtaWNWaVQgMzAlIiwiMzAlIiwiMS42eCIsIjAuNCUiLCJSZXF1aXJlcyByZXRyYWluaW5nIl0sWyJFVmlUIDMwJSIsIjMwJSIsIjEuN3giLCIwLjUlIiwiUmVxdWlyZXMgcmV0cmFpbmluZyJdLFsiUG9vbGluZyAyeDIiLCI3NSUiLCIyLjh4IiwiMS41JSIsIkFyY2hpdGVjdHVyZS1zcGVjaWZpYyJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgcHJvZHVjdGlvbiwgVG9NZSBhdCByPTggaXMgdGhlIHByYWdtYXRpYyBkZWZhdWx0OiB6ZXJvIHJldHJhaW5pbmcsIGRyb3AtaW4gY29tcGF0aWJpbGl0eSwgc2FmZSBhY2N1cmFjeSB0cmFkZW9mZi4gSWYgdHJhaW5pbmcgZnJvbSBzY3JhdGNoLCBEeW5hbWljVmlUIG9yIEVWaVQgcHJvdmlkZSBiZXR0ZXIgcGVyLWxheWVyIHJlZHVjdGlvbiBjb250cm9sLiBQb29saW5nIGlzIGJlc3Qgd2hlbiB0aGUgdGFzayBpcyBjbGFzc2lmaWNhdGlvbi1vbmx5IGFuZCBzcGF0aWFsIHJlc29sdXRpb24gaXMgbm90IG5lZWRlZCBiZXlvbmQgdGhlIGZpcnN0IGZldyBibG9ja3Mgb2YgdGhlIHRyYW5zZm9ybWVyIHN0YWNrLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRva2VuIHJlZHVjdGlvbiBpcyBub3cgYSBzdGFuZGFyZCB0b29sIGluIHRoZSBlZmZpY2llbnQgVmlUIHRvb2xraXQuIFRoZSBkZXNpZ24gc3BhY2UgaGFzIHRocmVlIGF4ZXM6IHdoZW4gdG8gcmVkdWNlICh3aGljaCBsYXllcnMpLCBob3cgbXVjaCB0byByZWR1Y2UgKHJhdGlvIG9yIGZpeGVkIGNvdW50KSwgYW5kIGhvdyB0byByZWR1Y2UgKG1lcmdlLCBwcnVuZSwgb3IgcG9vbCkuIEJlc3QgcmVzdWx0cyBjb21iaW5lIG1vZGVzdCByZWR1Y3Rpb24gaW4gZWFybHkgbGF5ZXJzIHdpdGggbW9yZSBhZ2dyZXNzaXZlIHJlZHVjdGlvbiBpbiBtaWQtbGF5ZXJzLCBsZWF2aW5nIGxhdGUgbGF5ZXJzIGF0IGZ1bGwgdG9rZW4gY291bnQgdG8gcHJlc2VydmUgZ2xvYmFsIHJlcHJlc2VudGF0aW9ucy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0cmFpbmluZy1mcmVlIHZzIHRyYWluaW5nLWF3YXJlIHNwbGl0IGlzIGEgcHJhY3RpY2FsIGRlY2lzaW9uLiBUcmFpbmluZy1mcmVlIG1ldGhvZHMgbGlrZSBUb01lIHdvcmsgaW1tZWRpYXRlbHkgb24gYW55IGNoZWNrcG9pbnQgYW5kIGFyZSBlc3NlbnRpYWwgd2hlbiB5b3UgY2Fubm90IGFmZm9yZCB0byByZXRyYWluLiBUcmFpbmluZy1hd2FyZSBtZXRob2RzIHJlY292ZXIgYWNjdXJhY3kgYXQgaGlnaGVyIHJlZHVjdGlvbiByYXRlcyBidXQgcmVxdWlyZSByZXJ1bm5pbmcgdGhlIHRyYWluaW5nIHBpcGVsaW5lLiBGb3IgbW9zdCB0ZWFtcywgdHJhaW5pbmctZnJlZSBtZXRob2RzIHdpbGwgY2FwdHVyZSA4MCUgb2YgdGhlIHNwZWVkdXAgYmVuZWZpdCBhdCB6ZXJvIGFkZGl0aW9uYWwgdHJhaW5pbmcgY29zdC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRva2VuIHJlZHVjdGlvbiBkb2VzIG5vdCBjaGFuZ2UgdGhlIFZpVCBhcmNoaXRlY3R1cmUg4oCUIGl0IGNoYW5nZXMgdGhlIGlucHV0IHNlcXVlbmNlIHRvIGVhY2ggYmxvY2suIFRoaXMgbWVhbnMgcmVkdWNlZCBtb2RlbHMgcmV0YWluIGZ1bGwgY29tcGF0aWJpbGl0eSB3aXRoIHRoZSBvcmlnaW5hbCBhdHRlbnRpb24gbWVjaGFuaXNtLCBwb3NpdGlvbmFsIGVtYmVkZGluZ3MsIGFuZCBsYXllciBub3JtYWxpemF0aW9uLiBUaGUgcmVkdWN0aW9uIGNhbiBiZSBhcHBsaWVkLCB0dW5lZCwgb3IgcmVtb3ZlZCBhdCBpbmZlcmVuY2UgdGltZSB3aXRob3V0IGFueSB3ZWlnaHQgbW9kaWZpY2F0aW9uLCBtYWtpbmcgaXQgYSB0cnVlIGluZmVyZW5jZS10aW1lIGh5cGVycGFyYW1ldGVyLiJ9XQ=="
---
# Efficient ViT: Token Merging and Reduction Strategies

## Overview

Standard ViTs scale quadratically with token count: a 224px image at patch size 16 produces 196 tokens, but at 512px that becomes 1024 tokens and attention cost grows 27×. Token reduction strategies — merging, pruning, or pooling — break this bottleneck by reducing effective sequence length while preserving most information content for downstream tasks.

The core observation motivating token reduction is that image patches are highly redundant. In natural images, adjacent patches share color, texture, and semantic content. A model processing a uniform sky region computes nearly identical attention patterns across dozens of tokens. Identifying and collapsing these redundant tokens is the central challenge of efficient ViT design.

> **Tip**: ToMe requires zero retraining — plug it into any pretrained ViT by wrapping the attention module. Start at r=8 for ~1.5x speedup with <0.3% accuracy drop.

## Token Redundancy in Attention

Attention maps in early ViT layers show strong spatial locality: most tokens attend primarily to immediate neighbors. In later layers, global semantics emerge but many tokens still carry nearly identical key-query representations. Measuring pairwise cosine similarity between token features reveals that 30–50% of tokens have at least one near-duplicate (sim > 0.9) in typical ImageNet images.

```python
# Compute token similarity matrix; threshold at tau to find mergeable pairs
import torch

def token_similarity(x, tau=0.9):
    # x: (B, N, D) token features
    d = x.shape[-1]
    x_norm = x / x.norm(dim=-1, keepdim=True)
    sim = (x_norm @ x_norm.transpose(-1, -2)) / (d ** 0.5)  # (B, N, N)
    mask = torch.eye(sim.shape[-1], device=x.device).bool()
    sim = sim.masked_fill(mask.unsqueeze(0), -1.0)
    mergeable = (sim > tau).any(dim=-1)   # (B, N) boolean mask
    redundancy = mergeable.float().mean()
    return sim, redundancy

sim_mat, red = token_similarity(patch_tokens)
print(f'Token redundancy: {red:.1%}')
```

Redundancy is not uniformly distributed across layers. Early blocks show high spatial redundancy (adjacent patches); middle blocks show semantic redundancy (same-object patches); final blocks are most diverse since each token has accumulated global context. This profile motivates applying more aggressive reduction in early layers and preserving more tokens in later layers.

## Token Merging (ToMe)

Token Merging (ToMe) by Bolya et al. 2023 introduces a training-free method to reduce ViT token count at inference. At each transformer block, it partitions tokens into two sets — source (src) and destination (dst) — using bipartite matching. The top-r most similar src-dst pairs are merged by averaging their features, reducing the sequence by r tokens per block.

```python
# ToMe bipartite matching: merge top-r src tokens into nearest dst tokens
import torch

def tome_merge(x, r):
    # x: (B, N, D); r: tokens to merge per block
    B, N, D = x.shape
    src = x[:, 1::2, :]   # odd-indexed tokens
    dst = x[:, 0::2, :]   # even-indexed tokens
    src_n = src / src.norm(dim=-1, keepdim=True)
    dst_n = dst / dst.norm(dim=-1, keepdim=True)
    sim = src_n @ dst_n.transpose(-1, -2)   # (B, N//2, N//2)
    scores, best_dst = sim.max(dim=-1)      # per-src best dst
    _, top_r_idx = scores.topk(r, dim=-1)  # top-r src by similarity
    for b in range(B):
        for i in range(r):
            s_i = top_r_idx[b, i]
            d_i = best_dst[b, s_i]
            dst[b, d_i] = (dst[b, d_i] + src[b, s_i]) / 2
    return dst
```

ToMe operates inside the attention module before the softmax, so merged tokens reduce both the QK^T matrix size and feedforward computation in the same block. No gradient flows through the merge operation at inference, but during training-aware ToMe, a straight-through estimator allows the merge schedule to be learned jointly with the network weights.

## Token Pruning and Pooling

Token pruning takes a harder decision than merging: tokens below a relevance threshold are dropped entirely rather than averaged into neighbors. DynamicViT predicts per-token importance scores with a lightweight 2-layer MLP, then uses Gumbel-softmax to make the drop decision differentiable during training. At inference the Gumbel noise is removed and scores are thresholded deterministically.

```python
# DynamicViT: predict token keep scores with MLP, Gumbel-softmax drop
import torch, torch.nn as nn, torch.nn.functional as F

class TokenPredictor(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.score = nn.Sequential(
            nn.Linear(dim, dim // 4), nn.GELU(), nn.Linear(dim // 4, 2))

    def forward(self, x, keep_ratio=0.7, training=True):
        logits = self.score(x)            # (B, N, 2): [drop, keep]
        if training:
            decisions = F.gumbel_softmax(logits, tau=1.0, hard=True)
            keep_mask = decisions[..., 1]
        else:
            scores = logits.softmax(-1)[..., 1]
            topk = int(x.shape[1] * keep_ratio)
            _, idx = scores.topk(topk, dim=-1)
            keep_mask = torch.zeros_like(scores).scatter_(-1, idx, 1.0)
        return x * keep_mask.unsqueeze(-1), keep_mask
```

Spatial pooling is the simplest reduction: apply average pooling over 2×2 windows of patch tokens, reducing the sequence by 4× per pooling stage. This is the approach used in PVT and Twins. Unlike merging or pruning, pooling is content-agnostic — it always reduces by a fixed factor regardless of image content — but it composes naturally with convolution and requires no learned selection mechanism.

## Speed-Accuracy Tradeoffs

Benchmarking token reduction requires measuring throughput at a fixed batch size and resolution, not just FLOPs. Wall-clock speedup often deviates from FLOP reduction because token reduction introduces irregular computation patterns that GPUs handle less efficiently than uniform matmul operations. ToMe at r=8 reduces FLOPs by ~30% but achieves only ~1.5× wall-clock speedup due to overhead from the merge bookkeeping.

```python
# Benchmark throughput at varying r merge budgets
import torch, time

def benchmark(model, r_values=[0, 8, 16, 24], batch=32, runs=100):
    x = torch.randn(batch, 3, 224, 224).cuda()
    results = []
    for r in r_values:
        model.set_tome_r(r)     # sets merge budget per block
        for _ in range(10):     # warmup
            with torch.no_grad(): model(x)
        torch.cuda.synchronize()
        t0 = time.perf_counter()
        for _ in range(runs):
            with torch.no_grad(): model(x)
        torch.cuda.synchronize()
        imgs_per_sec = (batch * runs) / (time.perf_counter() - t0)
        results.append({'r': r, 'imgs_per_sec': imgs_per_sec})
    return results
```

| Method | Reduction | Throughput Gain | Top-1 Drop | Compatible With |
| --- | --- | --- | --- | --- |
| ToMe r=8 | ~15% | 1.5x | <0.3% | Any pretrained ViT |
| ToMe r=16 | ~30% | 1.9x | 0.5% | Any pretrained ViT |
| DynamicViT 30% | 30% | 1.6x | 0.4% | Requires retraining |
| EViT 30% | 30% | 1.7x | 0.5% | Requires retraining |
| Pooling 2x2 | 75% | 2.8x | 1.5% | Architecture-specific |

For production, ToMe at r=8 is the pragmatic default: zero retraining, drop-in compatibility, safe accuracy tradeoff. If training from scratch, DynamicViT or EViT provide better per-layer reduction control. Pooling is best when the task is classification-only and spatial resolution is not needed beyond the first few blocks of the transformer stack.

## Key Takeaways

Token reduction is now a standard tool in the efficient ViT toolkit. The design space has three axes: when to reduce (which layers), how much to reduce (ratio or fixed count), and how to reduce (merge, prune, or pool). Best results combine modest reduction in early layers with more aggressive reduction in mid-layers, leaving late layers at full token count to preserve global representations.

The training-free vs training-aware split is a practical decision. Training-free methods like ToMe work immediately on any checkpoint and are essential when you cannot afford to retrain. Training-aware methods recover accuracy at higher reduction rates but require rerunning the training pipeline. For most teams, training-free methods will capture 80% of the speedup benefit at zero additional training cost.

Token reduction does not change the ViT architecture — it changes the input sequence to each block. This means reduced models retain full compatibility with the original attention mechanism, positional embeddings, and layer normalization. The reduction can be applied, tuned, or removed at inference time without any weight modification, making it a true inference-time hyperparameter.

