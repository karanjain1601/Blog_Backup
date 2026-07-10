---
title: "Kaplan Scaling Laws — Power Laws for LLM Loss, Parameters, and Compute"
slug: "kaplan-scaling-laws"
description: "Kaplan et al. (2020): test loss scales as a power law in N (parameters), D (tokens), and C (compute) over seven orders of magnitude, with compute-optimal frontier predictions and irreducible loss estimation."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gMjAyMCwgS2FwbGFuIGV0IGFsLiBhdCBPcGVuQUkgcHVibGlzaGVkIGEgbGFuZG1hcmsgZW1waXJpY2FsIHN0dWR5IHNob3dpbmcgdGhhdCB0aGUgdGVzdCBsb3NzIG9mIGxhbmd1YWdlIG1vZGVscyBmb2xsb3dzIHNtb290aCBwb3dlciBsYXdzIG92ZXIgbW9yZSB0aGFuIHNldmVuIG9yZGVycyBvZiBtYWduaXR1ZGUgaW4gcGFyYW1ldGVycyBOLCB0b2tlbnMgRCwgYW5kIGNvbXB1dGUgQy4gTWVhc3VyZWQgb24gV2ViVGV4dDIgd2l0aCBHUFQtc3R5bGUgYXJjaGl0ZWN0dXJlcywgdGhlc2Ugc2NhbGluZyBsYXdzIHByb3ZpZGVkIHRoZSBmaXJzdCByaWdvcm91cyBmcmFtZXdvcmsgZm9yIHByZWRpY3RpbmcgbW9kZWwgcGVyZm9ybWFuY2UgYmVmb3JlIHRyYWluaW5nIGFuZCBmb3IgYWxsb2NhdGluZyBjb21wdXRlIGJ1ZGdldHMgYWNyb3NzIG1vZGVsIHNpemUgYW5kIHRyYWluaW5nIGR1cmF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBDb3JlIFBvd2VyIExhd3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRocmVlIGZ1bmRhbWVudGFsIHJlbGF0aW9uc2hpcHMgZ292ZXJuIExMTSBsb3NzLiBMb3NzIHZzIHBhcmFtZXRlcnM6IEwoTikgPSBhX04gKiBOXigtYWxwaGFfTiksIGFscGhhX04gYXBwcm94aW1hdGVseSAwLjA3NiDigJQgZG91YmxpbmcgcGFyYW1ldGVycyByZWR1Y2VzIGxvc3MgYnkgcm91Z2hseSA1JS4gTG9zcyB2cyB0b2tlbnM6IEwoRCkgPSBhX0QgKiBEXigtYWxwaGFfRCksIGFscGhhX0QgYXBwcm94aW1hdGVseSAwLjA5NSDigJQgZG91YmxpbmcgdG9rZW5zIHJlZHVjZXMgbG9zcyBieSByb3VnaGx5IDYlLiBMb3NzIHZzIGNvbXB1dGU6IEwoQykgPSBhX0MgKiBDXigtYWxwaGFfQyksIGFscGhhX0MgYXBwcm94aW1hdGVseSAwLjA1NyDigJQgZG91YmxpbmcgY29tcHV0ZSByZWR1Y2VzIGxvc3MgYnkgcm91Z2hseSA0JS4gRWFjaCBsYXcgaG9sZHMgd2hlbiB0aGUgb3RoZXIgZmFjdG9ycyBhcmUgbm90IHRoZSBiaW5kaW5nIGNvbnN0cmFpbnQuIFRoZSBzdHJpa2luZyByZXN1bHQgaXMgdGhhdCBhbGwgdGhyZWUgaG9sZCBvdmVyIHNldmVuIG9yZGVycyBvZiBtYWduaXR1ZGUgd2l0aCBubyBvYnNlcnZlZCBzYXR1cmF0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTChOKSBwcm9wb3J0aW9uYWwgdG8gTl4oLTAuMDc2KTogcGFyYW1ldGVycyBsYXcsIG1lYXN1cmVkIHdpdGggdW5saW1pdGVkIGRhdGEgYW5kIGNvbXB1dGUiLCJMKEQpIHByb3BvcnRpb25hbCB0byBEXigtMC4wOTUpOiBkYXRhIGxhdywgbWVhc3VyZWQgd2l0aCBsYXJnZSBlbm91Z2ggbW9kZWxzIiwiTChDKSBwcm9wb3J0aW9uYWwgdG8gQ14oLTAuMDU3KTogY29tcHV0ZSBsYXcsIHRyYWNlcyB0aGUgY29tcHV0ZS1vcHRpbWFsIGZyb250aWVyIiwiQXJjaGl0ZWN0dXJlIChkZXB0aCwgd2lkdGgsIGhlYWRzKSBjb250cmlidXRlcyBsZXNzIHRoYW4gNSUgb2YgbG9zcyB2YXJpYW5jZSB2cyB0b3RhbCBOIiwiSXJyZWR1Y2libGUgbG9zcyBFIGFwcHJveGltYXRlbHkgMS42OSBuYXRzIG9uIFdlYlRleHQg4oCUIHRoZSBlbnRyb3B5IGZsb29yIG9mIG5hdHVyYWwgbGFuZ3VhZ2UiLCJTZXZlbiBvcmRlcnMgb2YgbWFnbml0dWRlIG9mIHNtb290aCBzY2FsaW5nOiBmcm9tIDFNIHRvIDEwQiBwYXJhbWV0ZXJzLCAxQiB0byAxVCB0b2tlbnMiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAxIOKAlCBQb3dlciBMYXcgRml0dGluZyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IGN1cnZlX2ZpdFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG4jIEVtcGlyaWNhbCBsb3NzIHZzIHBhcmFtZXRlciBjb3VudCAoTiBpbiBiaWxsaW9ucywgTCBpbiBuYXRzKVxuTl9kYXRhID0gbnAuYXJyYXkoWzAuMDAxLCAwLjAwMywgMC4wMSwgMC4wMywgMC4xLCAwLjMsIDEuMCwgMy4wLCAxMC4wLCAzMC4wXSlcbkxfZGF0YSA9IG5wLmFycmF5KFs0LjIwLCAgMy44NSwgIDMuNTUsIDMuMjgsIDMuMDIsIDIuODAsIDIuNjAsIDIuNDIsICAyLjI3LCAgMi4xNF0pXG5cbmRlZiBwb3dlcl9sYXcoTiwgYSwgYWxwaGEpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0woTikgPSBhICogTl4oLWFscGhhKSAtLSBzaW5nbGUtZmFjdG9yIHBvd2VyIGxhd1x1MDAyN1x1MDAyN1x1MDAyN1xuICAgIHJldHVybiBhICogTiAqKiAoLWFscGhhKVxuXG4jIEZpdCB2aWEgbm9ubGluZWFyIGxlYXN0IHNxdWFyZXNcbnBvcHQsIHBjb3YgPSBjdXJ2ZV9maXQocG93ZXJfbGF3LCBOX2RhdGEsIExfZGF0YSwgcDA9WzUuMCwgMC4wNzZdLCBtYXhmZXY9NTAwMClcbmFfZml0LCBhbHBoYV9maXQgPSBwb3B0XG5wZXJyID0gbnAuc3FydChucC5kaWFnKHBjb3YpKVxucHJpbnQoXHUwMDI3Rml0dGVkOiBhID0gezouNGZ9ICsvLSB7Oi40Zn1cdTAwMjcuZm9ybWF0KGFfZml0LCBwZXJyWzBdKSlcbnByaW50KFx1MDAyN0ZpdHRlZDogYWxwaGFfTiA9IHs6LjRmfSArLy0gezouNGZ9ICAoS2FwbGFuIHBhcGVyOiB+MC4wNzYpXHUwMDI3LmZvcm1hdChhbHBoYV9maXQsIHBlcnJbMV0pKVxuXG4jIEV4dHJhcG9sYXRlIHRvIGxhcmdlciBtb2RlbCBzaXplc1xuTl9leHRyYXAgPSBucC5sb2dzcGFjZSgtMywgMywgMjAwKSAgIyAxTSB0byAxVCBwYXJhbWV0ZXJzXG5MX3ByZWQgICA9IHBvd2VyX2xhdyhOX2V4dHJhcCwgYV9maXQsIGFscGhhX2ZpdClcblxucGx0LmZpZ3VyZShmaWdzaXplPSg5LCA1KSlcbnBsdC5sb2dsb2coTl9kYXRhLCBMX2RhdGEsIFx1MDAyN2tvXHUwMDI3LCBtYXJrZXJzaXplPTgsIGxhYmVsPVx1MDAyN0VtcGlyaWNhbCBkYXRhXHUwMDI3KVxucGx0LmxvZ2xvZyhOX2V4dHJhcCwgTF9wcmVkLCBcdTAwMjdiLVx1MDAyNywgbHc9MiwgbGFiZWw9XHUwMDI3Rml0OiBMID0gezouMmZ9ICogTl4oLXs6LjNmfSlcdTAwMjcuZm9ybWF0KGFfZml0LCBhbHBoYV9maXQpKVxucGx0LnhsYWJlbChcdTAwMjdQYXJhbWV0ZXJzIE4gKGJpbGxpb25zKVx1MDAyNywgZm9udHNpemU9MTIpXG5wbHQueWxhYmVsKFx1MDAyN1Rlc3QgTG9zcyBMIChuYXRzKVx1MDAyNywgZm9udHNpemU9MTIpXG5wbHQudGl0bGUoXHUwMDI3S2FwbGFuIFBvd2VyIExhdzogTChOKSBwcm9wb3J0aW9uYWwgdG8gTl4oLWFscGhhX04pXHUwMDI3LCBmb250c2l6ZT0xMylcbnBsdC5sZWdlbmQoZm9udHNpemU9MTEpXG5wbHQuZ3JpZChUcnVlLCB3aGljaD1cdTAwMjdib3RoXHUwMDI3LCBhbHBoYT0wLjMpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zYXZlZmlnKFx1MDAyN2thcGxhbl9wb3dlcl9sYXcucG5nXHUwMDI3LCBkcGk9MTUwKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBDb21wdXRlLU9wdGltYWwgRnJvbnRpZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdpdmVuIGEgZml4ZWQgY29tcHV0ZSBidWRnZXQgQyAoRkxPUHMpLCB0aGUgY29tcHV0ZS1vcHRpbWFsIG1vZGVsIHNpemUgc2NhbGVzIGFzIE4qIHByb3BvcnRpb25hbCB0byBDXjAuNzMgYW5kIHRoZSBjb21wdXRlLW9wdGltYWwgdG9rZW4gY291bnQgYXMgRCogcHJvcG9ydGlvbmFsIHRvIENeMC4yNy4gVGhpcyBhc3ltbWV0cnkgbWVhbnMgbW9kZWwgc2l6ZSBzaG91bGQgc2NhbGUgbXVjaCBmYXN0ZXIgdGhhbiBkYXRhOiBkb3VibGluZyBjb21wdXRlIHNob3VsZCBncm93IE4gYnkgcm91Z2hseSA2NiUgYnV0IEQgYnkgb25seSBhYm91dCAyMSUuIFRoZSBwcmFjdGljYWwgaW1wbGljYXRpb24gS2FwbGFuIGRyZXc6IHRyYWluIHRoZSBsYXJnZXN0IGZlYXNpYmxlIG1vZGVsIG9uIHJlbGF0aXZlbHkgZmV3IHRva2Vucywgc3RvcHBpbmcgd2VsbCBiZWZvcmUgY29udmVyZ2VuY2UuIFRoaXMgd2FzIHRoZSBwYXJhZGlnbSB1c2VkIGZvciBHUFQtMyAoMTc1QiBwYXJhbWV0ZXJzIG9uIDMwMEIgdG9rZW5zKS4gVGhlIEQvTiByYXRpbyBpbXBsaWVkIGJ5IEthcGxhbiBpcyBhcHByb3hpbWF0ZWx5IDEg4oCUIG9uZSB0b2tlbiBwZXIgcGFyYW1ldGVyIGF0IHRoZSBjb21wdXRlLW9wdGltYWwgcG9pbnQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAyIOKAlCBDb21wdXRlLU9wdGltYWwgTiogUHJlZGljdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBLYXBsYW4gY29tcHV0ZS1vcHRpbWFsOiBOKiBwcm9wb3J0aW9uYWwgdG8gQ14wLjczLCBEKiA9IEMgLyAoNiAqIE4qKVxuIyBDID0gNiAqIE4gKiBEIGFwcHJveGltYXRpb24gZm9yIHRyYW5zZm9ybWVyIHRyYWluaW5nIEZMT1BzXG5LQVBMQU5fRVhQX04gPSAwLjczXG5cbmRlZiBrYXBsYW5fb3B0aW1hbChDX2Zsb3BzLCBrX049MS4zZS01KTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdQcmVkaWN0IGNvbXB1dGUtb3B0aW1hbCAoTiosIEQqKSBmb3IgYSBnaXZlbiBGTE9QIGJ1ZGdldCBwZXIgS2FwbGFuLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIE5fc3RhciA9IGtfTiAqIChDX2Zsb3BzICoqIEtBUExBTl9FWFBfTilcbiAgICBEX3N0YXIgPSBDX2Zsb3BzIC8gKDYuMCAqIE5fc3RhcikgICMgZnJvbSBDID0gNk5EXG4gICAgcmV0dXJuIE5fc3RhciwgRF9zdGFyXG5cbmRlZiBjaGluY2hpbGxhX29wdGltYWwoQ19mbG9wcyk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3Q2hpbmNoaWxsYTogRCogPSAyMCpOKiwgQyA9IDYqTipEID0gMTIwKk5eMiA9XHUwMDNlIE4qID0gc3FydChDLzEyMCkuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgTl9zdGFyID0gbnAuc3FydChDX2Zsb3BzIC8gMTIwLjApXG4gICAgRF9zdGFyID0gMjAuMCAqIE5fc3RhclxuICAgIHJldHVybiBOX3N0YXIsIERfc3RhclxuXG5idWRnZXRzID0gW1xuICAgIChcdTAwMjc2ZTE4ICh+MUItc2NhbGUpXHUwMDI3LCAgIDZlMTgpLFxuICAgIChcdTAwMjc2ZTIwICh+N0Itc2NhbGUpXHUwMDI3LCAgIDZlMjApLFxuICAgIChcdTAwMjc2ZTIyICh+NzBCLXNjYWxlKVx1MDAyNywgNmUyMiksXG4gICAgKFx1MDAyNzZlMjMgKEdQVC00IGVzdC4pXHUwMDI3LCA2ZTIzKSxcbl1cbnByaW50KFx1MDAyN3s6XHUwMDNjMjJ9IHs6XHUwMDNlMTJ9IHs6XHUwMDNlMTJ9IHs6XHUwMDNlMTJ9IHs6XHUwMDNlMTJ9XHUwMDI3LmZvcm1hdChcdTAwMjdDb21wdXRlIEJ1ZGdldFx1MDAyNywgXHUwMDI3S2FwbGFuIE4qKEIpXHUwMDI3LCBcdTAwMjdLYXBsYW4gRCooQilcdTAwMjcsIFx1MDAyN0NoaW5jaCBOKihCKVx1MDAyNywgXHUwMDI3Q2hpbmNoIEQqKEIpXHUwMDI3KSlcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA3NClcbmZvciBuYW1lLCBDIGluIGJ1ZGdldHM6XG4gICAga04sIGtEID0ga2FwbGFuX29wdGltYWwoQylcbiAgICBjTiwgY0QgPSBjaGluY2hpbGxhX29wdGltYWwoQylcbiAgICBwcmludChcdTAwMjd7Olx1MDAzYzIyfSB7Olx1MDAzZTEyLjJmfSB7Olx1MDAzZTEyLjJmfSB7Olx1MDAzZTEyLjJmfSB7Olx1MDAzZTEyLjJmfVx1MDAyNy5mb3JtYXQobmFtZSwga04vMWU5LCBrRC8xZTksIGNOLzFlOSwgY0QvMWU5KSlcbnByaW50KFx1MDAyN1xcbkthcGxhbiBEL04gfiAxOyBDaGluY2hpbGxhIEQvTiA9IDIwIC0tIGEgMjB4IGRpZmZlcmVuY2UgaW4gZGF0YSBwcmVzY3JpcHRpb24uXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMyDigJQgU2NhbGluZyBMYXcgQ29tcGFyaXNvbiBWaXN1YWxpemF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYga2FwbGFuX2xvc3NfQyhDLCBhPTQuMCwgYWxwaGFfYz0wLjA1Nyk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3S2FwbGFuIGNvbXB1dGUgc2NhbGluZzogTChDKSA9IGEgKiBDXigtYWxwaGFfYylcdTAwMjdcdTAwMjdcdTAwMjdcbiAgICByZXR1cm4gYSAqIEMgKiogKC1hbHBoYV9jKVxuXG5kZWYgY2hpbmNoaWxsYV9sb3NzX0MoQywgYT0zLjEsIGFscGhhX2M9MC4wNTApOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0NoaW5jaGlsbGEgY29tcHV0ZSBzY2FsaW5nIHdpdGggc2xpZ2h0bHkgZGlmZmVyZW50IGV4cG9uZW50XHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgcmV0dXJuIGEgKiBDICoqICgtYWxwaGFfYylcblxuQ19yYW5nZSA9IG5wLmxvZ3NwYWNlKDE3LCAyNCwgMjAwKSAgIyAxZTE3IHRvIDFlMjQgRkxPUHNcblxuIyBBcHByb3hpbWF0ZSByZWZlcmVuY2UgcG9pbnRzIGZyb20gbGl0ZXJhdHVyZVxucmVmX21vZGVscyA9IHtcbiAgICBcdTAwMjdHUFQtMiAoMS41QilcdTAwMjc6ICAgICAoMS41ZTIxLCAzLjMwKSxcbiAgICBcdTAwMjdHUFQtMyAoMTc1QilcdTAwMjc6ICAgICAoMy4xZTIzLCAyLjg4KSxcbiAgICBcdTAwMjdDaGluY2hpbGxhICg3MEIpXHUwMDI3OiAoMy4wZTIzLCAyLjU1KSxcbn1cblxuZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSg5LCA1KSlcbmF4LmxvZ2xvZyhDX3JhbmdlLCBrYXBsYW5fbG9zc19DKENfcmFuZ2UpLCAgICAgXHUwMDI3Yi1cdTAwMjcsICBsdz0yLCBsYWJlbD1cdTAwMjdLYXBsYW4gKGFscGhhX2MgPSAwLjA1NylcdTAwMjcpXG5heC5sb2dsb2coQ19yYW5nZSwgY2hpbmNoaWxsYV9sb3NzX0MoQ19yYW5nZSksIFx1MDAyN2ctLVx1MDAyNywgbHc9MiwgbGFiZWw9XHUwMDI3Q2hpbmNoaWxsYSBmaXQgKGFscGhhX2MgPSAwLjA1MClcdTAwMjcpXG5jb2xvcnMgPSBbXHUwMDI3I2U3NGMzY1x1MDAyNywgXHUwMDI3IzhlNDRhZFx1MDAyNywgXHUwMDI3IzI3YWU2MFx1MDAyN11cbmZvciAobmFtZSwgKEMsIEwpKSwgY29sIGluIHppcChyZWZfbW9kZWxzLml0ZW1zKCksIGNvbG9ycyk6XG4gICAgYXguc2NhdHRlcihDLCBMLCBzPTE1MCwgY29sb3I9Y29sLCB6b3JkZXI9NSwgbGFiZWw9bmFtZSlcbmF4LnNldF94bGFiZWwoXHUwMDI3Q29tcHV0ZSBCdWRnZXQgQyAoRkxPUHMpXHUwMDI3LCBmb250c2l6ZT0xMilcbmF4LnNldF95bGFiZWwoXHUwMDI3VGVzdCBMb3NzIEwgKG5hdHMpXHUwMDI3LCBmb250c2l6ZT0xMilcbmF4LnNldF90aXRsZShcdTAwMjdQcmVkaWN0ZWQgdnMgQWN0dWFsIExvc3M6IEthcGxhbiB2cyBDaGluY2hpbGxhIENvbXB1dGUgU2NhbGluZ1x1MDAyNywgZm9udHNpemU9MTIpXG5heC5sZWdlbmQoZm9udHNpemU9OSlcbmF4LmdyaWQoVHJ1ZSwgd2hpY2g9XHUwMDI3Ym90aFx1MDAyNywgYWxwaGE9MC4zKVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdzY2FsaW5nX2NvbXBhcmlzb24ucG5nXHUwMDI3LCBkcGk9MTUwKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IklycmVkdWNpYmxlIExvc3MgYW5kIHRoZSBFbnRyb3B5IEZsb29yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZnVsbCBqb2ludCBzY2FsaW5nIGxhdyBpcyBMKE4sIEQpID0gRSArIEEvTl5hbHBoYSArIEIvRF5iZXRhLCB3aGVyZSBFIGFwcHJveGltYXRlbHkgMS42OSBuYXRzIGlzIHRoZSBpcnJlZHVjaWJsZSBsb3NzIOKAlCB0aGUgZW50cm9weSBvZiBuYXR1cmFsIGxhbmd1YWdlIGl0c2VsZiwgcmVwcmVzZW50aW5nIGluZm9ybWF0aW9uIG5vIG1vZGVsIGNhbiBwcmVkaWN0IHJlZ2FyZGxlc3Mgb2Ygc2l6ZS4gVGhlIHRlcm0gQS9OXmFscGhhIGNhcHR1cmVzIGNhcGFjaXR5LWxpbWl0ZWQgbG9zcyAobW9kZWwgdG9vIHNtYWxsKSBhbmQgQi9EXmJldGEgY2FwdHVyZXMgZGF0YS1saW1pdGVkIGxvc3MgKGluc3VmZmljaWVudCB0cmFpbmluZyB0b2tlbnMpLiBGaXR0aW5nIHRoaXMgam9pbnQgZm9ybXVsYSByZXF1aXJlcyBhIGdyaWQgb2YgKE4sIEQsIEwpIG9ic2VydmF0aW9ucy4gVGhlIENoaW5jaGlsbGEgcGFwZXIgZml0dGVkIEU9MS42OSwgQT00MDYuNCwgYWxwaGE9MC4zNCwgQj00MTAuNywgYmV0YT0wLjI4IGFjcm9zcyBvdmVyIDQwMCBtb2RlbHMgcmFuZ2luZyBmcm9tIDcwTSB0byAxNkIgcGFyYW1ldGVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDQg4oCUIElycmVkdWNpYmxlIExvc3MgRXN0aW1hdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5cbmRlZiBsb3NzX21vZGVsKHBhcmFtcywgTiwgRCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3TChOLCBEKSA9IEUgKyBBICogTl4oLWFscGhhKSArIEIgKiBEXigtYmV0YSlcdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBFLCBBLCBhbHBoYSwgQiwgYmV0YSA9IHBhcmFtc1xuICAgIHJldHVybiBFICsgQSAqIE4gKiogKC1hbHBoYSkgKyBCICogRCAqKiAoLWJldGEpXG5cbmRlZiBvYmplY3RpdmUocGFyYW1zLCBOX2FyciwgRF9hcnIsIExfb2JzKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdTdW0gb2Ygc3F1YXJlZCByZXNpZHVhbHMgZm9yIGxlYXN0LXNxdWFyZXMgZml0dGluZy5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICByZXR1cm4gbnAuc3VtKChsb3NzX21vZGVsKHBhcmFtcywgTl9hcnIsIERfYXJyKSAtIExfb2JzKSAqKiAyKVxuXG4jIFNpbXVsYXRlZCBsb3NzIGdyaWQ6IE4gaW4gQiBwYXJhbXMsIEQgaW4gQiB0b2tlbnNcbm5wLnJhbmRvbS5zZWVkKDQyKVxuTl92YWxzID0gbnAuYXJyYXkoWzAuMSwgMC4zLCAxLjAsIDMuMCwgMTAuMF0pXG5EX3ZhbHMgPSBucC5hcnJheShbMTAuMCwgMzAuMCwgMTAwLjAsIDMwMC4wXSlcbk5fZ3JpZCwgRF9ncmlkID0gbnAubWVzaGdyaWQoTl92YWxzLCBEX3ZhbHMsIGluZGV4aW5nPVx1MDAyN2lqXHUwMDI3KVxuTl9mbGF0LCBEX2ZsYXQgPSBOX2dyaWQucmF2ZWwoKSwgRF9ncmlkLnJhdmVsKClcblxuIyBHcm91bmQgdHJ1dGg6IENoaW5jaGlsbGEgY29uc3RhbnRzXG50cnVlX3AgPSBbMS42OSwgNDA2LjQsIDAuMzQsIDQxMC43LCAwLjI4XVxuTF9vYnMgID0gbG9zc19tb2RlbCh0cnVlX3AsIE5fZmxhdCwgRF9mbGF0KSArIG5wLnJhbmRvbS5ub3JtYWwoMCwgMC4wMSwgbGVuKE5fZmxhdCkpXG5cbiMgSm9pbnRseSBmaXQgYWxsIDUgcGFyYW1ldGVycyB1c2luZyBOZWxkZXItTWVhZFxucmVzdWx0ID0gbWluaW1pemUob2JqZWN0aXZlLCB4MD1bMi4wLCAzMDAuMCwgMC4zMCwgMzAwLjAsIDAuMjVdLFxuICAgICAgICAgICAgICAgICAgYXJncz0oTl9mbGF0LCBEX2ZsYXQsIExfb2JzKSwgbWV0aG9kPVx1MDAyN05lbGRlci1NZWFkXHUwMDI3LFxuICAgICAgICAgICAgICAgICAgb3B0aW9ucz17XHUwMDI3bWF4aXRlclx1MDAyNzogMjAwMDAsIFx1MDAyN3hhdG9sXHUwMDI3OiAxZS03fSlcbkVfZiwgQV9mLCBhX2YsIEJfZiwgYl9mID0gcmVzdWx0LnhcbnByaW50KFx1MDAyN0ZpdHRlZDogIEU9ezouM2Z9LCBBPXs6LjFmfSwgYWxwaGE9ezouM2Z9LCBCPXs6LjFmfSwgYmV0YT17Oi4zZn1cdTAwMjcuZm9ybWF0KEVfZiwgQV9mLCBhX2YsIEJfZiwgYl9mKSlcbnByaW50KFx1MDAyN1RhcmdldDogIEU9MS42OTAsIEE9NDA2LjQsIGFscGhhPTAuMzQwLCBCPTQxMC43LCBiZXRhPTAuMjgwXHUwMDI3KVxucHJpbnQoXHUwMDI3TVNFIHBlciBwb2ludDogezouNmZ9XHUwMDI3LmZvcm1hdChyZXN1bHQuZnVuIC8gbGVuKE5fZmxhdCkpKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRhYmxlIGJlbG93IGNvbXBhcmVzIGNvbXB1dGUtb3B0aW1hbCBtb2RlbCBzaXplIE4qIGFuZCB0b2tlbiBjb3VudCBEKiBwcmVkaWN0ZWQgYnkgS2FwbGFuICgyMDIwKSB2ZXJzdXMgQ2hpbmNoaWxsYSAoMjAyMikgZm9yIHRocmVlIHJlcHJlc2VudGF0aXZlIGNvbXB1dGUgYnVkZ2V0cy4gVGhlIGRyYW1hdGljIGRpZmZlcmVuY2UgaW4gRC9OIHJhdGlvIOKAlCByb3VnaGx5IDF4IGZvciBLYXBsYW4gdnMgMjB4IGZvciBDaGluY2hpbGxhIOKAlCBleHBsYWlucyB3aHkgZWFybHkgbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzIHN1Y2ggYXMgR1BULTMgYW5kIEdvcGhlciB3ZXJlIG1hc3NpdmVseSB1bmRlcnRyYWluZWQgb24gZGF0YSByZWxhdGl2ZSB0byB0aGVpciBwYXJhbWV0ZXIgY291bnRzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDb21wdXRlIEJ1ZGdldCAoRkxPUHMpIiwiS2FwbGFuIE4qIChCIHBhcmFtcykiLCJLYXBsYW4gRCogKEIgdG9rZW5zKSIsIkthcGxhbiBEL04iLCJDaGluY2hpbGxhIE4qIChCIHBhcmFtcykiLCJDaGluY2hpbGxhIEQqIChCIHRva2VucykiLCJDaGluY2hpbGxhIEQvTiJdLCJyb3dzIjpbWyI2ZTE4ICh+MUItc2NhbGUpIiwiMS4wIiwiMS4wIiwifjF4IiwiMC4yMiIsIjQuNSIsIn4yMHgiXSxbIjZlMjAgKH43Qi1zY2FsZSkiLCI3LjAiLCI3LjAiLCJ+MXgiLCIyLjI0IiwiNDQuNyIsIn4yMHgiXSxbIjZlMjIgKH43MEItc2NhbGUpIiwiNzAuMCIsIjcwLjAiLCJ+MXgiLCIyMi40IiwiNDQ3IiwifjIweCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhyZWUgUmVnaW1lcyBhbmQgQ2F2ZWF0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS2FwbGFuIGlkZW50aWZpZWQgdGhyZWUgbGltaXRpbmcgcmVnaW1lcyBmb3IgTExNIHRyYWluaW5nLiBUaGUgY29tcHV0ZS1saW1pdGVkIHJlZ2ltZSBhcHBsaWVzIHdoZW4gYm90aCBOIGFuZCBEIGNvdWxkIGdyb3cgZnJlZWx5IGJ1dCBjb21wdXRlIGlzIGZpeGVkIOKAlCBMKEMpIGxhdyBkZXNjcmliZXMgcGVyZm9ybWFuY2UuIFRoZSBwYXJhbWV0ZXItbGltaXRlZCByZWdpbWUgYXBwbGllcyB3aGVuIHRoZSBtb2RlbCBpcyB0b28gc21hbGwgcmVsYXRpdmUgdG8gZGF0YSDigJQgdGhlIEEvTl5hbHBoYSB0ZXJtIGRvbWluYXRlcyBsb3NzIGFuZCBtb3JlIHBhcmFtZXRlcnMgZ2l2ZSByYXBpZCBnYWlucy4gVGhlIGRhdGEtbGltaXRlZCByZWdpbWUgYXBwbGllcyB3aGVuIGRhdGEgaXMgZXhoYXVzdGVkIG9yIHJlY3ljbGVkIOKAlCBCL0ReYmV0YSBkb21pbmF0ZXMgYW5kIGFkZGl0aW9uYWwgdG9rZW5zIGRlZ3JhZGUgZHVlIHRvIHJlcGV0aXRpb24uIEltcG9ydGFudCBjYXZlYXRzOiBsYXdzIHdlcmUgbWVhc3VyZWQgb24gV2ViVGV4dDI7IHRyYW5zZmVyIHRvIGNvZGUsIG1hdGgsIG9yIG11bHRpbGluZ3VhbCBkYXRhIG1heSBkaWZmZXI7IGFyY2hpdGVjdHVyZSBzcGVjaWZpY3MgbWF0dGVyIGxlc3MgdGhhbiB0b3RhbCBOOyBhbmQgS2FwbGFuIGRpZCBub3Qgc3dlZXAgRCBpbmRlcGVuZGVudGx5IGF0IGVhY2ggTiwgYSBjb25mb3VuZCB0aGF0IENoaW5jaGlsbGEgY29ycmVjdGVkLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQ29tcHV0ZS1saW1pdGVkOiBncm93IE4gYW5kIEQgdG9nZXRoZXIgYWxvbmcgY29tcHV0ZS1vcHRpbWFsIGZyb250aWVyIHVzaW5nIEwoQykgbGF3IiwiUGFyYW1ldGVyLWxpbWl0ZWQ6IHNtYWxsIG1vZGVsIHdpdGggYW1wbGUgZGF0YSDigJQgbW9yZSBwYXJhbWV0ZXJzIGdpdmUgcmFwaWQgaW1wcm92ZW1lbnQiLCJEYXRhLWxpbWl0ZWQ6IGRhdGEgZXhoYXVzdGVkIG9yIHJlY3ljbGVkIOKAlCBkaW1pbmlzaGluZyByZXR1cm5zLCBwb3RlbnRpYWwgZGVncmFkYXRpb24iLCJNZWFzdXJlZCBvbiBXZWJUZXh0MiDigJQgbWF5IG5vdCBnZW5lcmFsaXplIHRvIGNvZGUsIG1hdGgsIG9yIG11bHRpbGluZ3VhbCBjb3Jwb3JhIiwiQXJjaGl0ZWN0dXJlIChkZXB0aCB2cyB3aWR0aCwgYXR0ZW50aW9uIGhlYWRzKSBjb250cmlidXRlcyBsZXNzIHRoYW4gTiB0byBvdmVyYWxsIGxvc3MiLCJLYXBsYW5cdTAwMjdzIGV4cGVyaW1lbnRzIGxhY2tlZCBzdWZmaWNpZW50IGRhdGEgdmFyaWF0aW9uIOKAlCBDaGluY2hpbGxhIGNvcnJlY3RlZCB0aGlzIGNvbmZvdW5kIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiV2FybmluZyIsImNvbnRlbnQiOiJLYXBsYW4gc2NhbGluZyBsYXdzIHByZWRpY3Qgc2NhbGluZyBtb2RlbHMgZmFzdGVyIHRoYW4gZGF0YSAoTiogcHJvcG9ydGlvbmFsIHRvIENeMC43Mykg4oCUIENoaW5jaGlsbGEgbGF0ZXIgc2hvd2VkIHRoaXMgd2FzIHdyb25nIGR1ZSB0byBpbnN1ZmZpY2llbnQgZGF0YSBpbiBLYXBsYW5cdTAwMjdzIGV4cGVyaW1lbnRzLCBhbmQgY29ycmVjdGVkIHRoZSBvcHRpbWFsIHRva2VuLXRvLXBhcmFtZXRlciByYXRpbyB0byB+MjA6MS4ifV0="
---
# Kaplan Scaling Laws — Power Laws for LLM Loss, Parameters, and Compute

In 2020, Kaplan et al. at OpenAI published a landmark empirical study showing that the test loss of language models follows smooth power laws over more than seven orders of magnitude in parameters N, tokens D, and compute C. Measured on WebText2 with GPT-style architectures, these scaling laws provided the first rigorous framework for predicting model performance before training and for allocating compute budgets across model size and training duration.

## The Core Power Laws

Three fundamental relationships govern LLM loss. Loss vs parameters: L(N) = a_N * N^(-alpha_N), alpha_N approximately 0.076 — doubling parameters reduces loss by roughly 5%. Loss vs tokens: L(D) = a_D * D^(-alpha_D), alpha_D approximately 0.095 — doubling tokens reduces loss by roughly 6%. Loss vs compute: L(C) = a_C * C^(-alpha_C), alpha_C approximately 0.057 — doubling compute reduces loss by roughly 4%. Each law holds when the other factors are not the binding constraint. The striking result is that all three hold over seven orders of magnitude with no observed saturation.

- L(N) proportional to N^(-0.076): parameters law, measured with unlimited data and compute
- L(D) proportional to D^(-0.095): data law, measured with large enough models
- L(C) proportional to C^(-0.057): compute law, traces the compute-optimal frontier
- Architecture (depth, width, heads) contributes less than 5% of loss variance vs total N
- Irreducible loss E approximately 1.69 nats on WebText — the entropy floor of natural language
- Seven orders of magnitude of smooth scaling: from 1M to 10B parameters, 1B to 1T tokens

## Code 1 — Power Law Fitting

```python
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Empirical loss vs parameter count (N in billions, L in nats)
N_data = np.array([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0])
L_data = np.array([4.20,  3.85,  3.55, 3.28, 3.02, 2.80, 2.60, 2.42,  2.27,  2.14])

def power_law(N, a, alpha):
    '''L(N) = a * N^(-alpha) -- single-factor power law'''
    return a * N ** (-alpha)

# Fit via nonlinear least squares
popt, pcov = curve_fit(power_law, N_data, L_data, p0=[5.0, 0.076], maxfev=5000)
a_fit, alpha_fit = popt
perr = np.sqrt(np.diag(pcov))
print('Fitted: a = {:.4f} +/- {:.4f}'.format(a_fit, perr[0]))
print('Fitted: alpha_N = {:.4f} +/- {:.4f}  (Kaplan paper: ~0.076)'.format(alpha_fit, perr[1]))

# Extrapolate to larger model sizes
N_extrap = np.logspace(-3, 3, 200)  # 1M to 1T parameters
L_pred   = power_law(N_extrap, a_fit, alpha_fit)

plt.figure(figsize=(9, 5))
plt.loglog(N_data, L_data, 'ko', markersize=8, label='Empirical data')
plt.loglog(N_extrap, L_pred, 'b-', lw=2, label='Fit: L = {:.2f} * N^(-{:.3f})'.format(a_fit, alpha_fit))
plt.xlabel('Parameters N (billions)', fontsize=12)
plt.ylabel('Test Loss L (nats)', fontsize=12)
plt.title('Kaplan Power Law: L(N) proportional to N^(-alpha_N)', fontsize=13)
plt.legend(fontsize=11)
plt.grid(True, which='both', alpha=0.3)
plt.tight_layout()
plt.savefig('kaplan_power_law.png', dpi=150)
plt.show()
```

## The Compute-Optimal Frontier

Given a fixed compute budget C (FLOPs), the compute-optimal model size scales as N* proportional to C^0.73 and the compute-optimal token count as D* proportional to C^0.27. This asymmetry means model size should scale much faster than data: doubling compute should grow N by roughly 66% but D by only about 21%. The practical implication Kaplan drew: train the largest feasible model on relatively few tokens, stopping well before convergence. This was the paradigm used for GPT-3 (175B parameters on 300B tokens). The D/N ratio implied by Kaplan is approximately 1 — one token per parameter at the compute-optimal point.

## Code 2 — Compute-Optimal N* Prediction

```python
import numpy as np

# Kaplan compute-optimal: N* proportional to C^0.73, D* = C / (6 * N*)
# C = 6 * N * D approximation for transformer training FLOPs
KAPLAN_EXP_N = 0.73

def kaplan_optimal(C_flops, k_N=1.3e-5):
    '''Predict compute-optimal (N*, D*) for a given FLOP budget per Kaplan.'''
    N_star = k_N * (C_flops ** KAPLAN_EXP_N)
    D_star = C_flops / (6.0 * N_star)  # from C = 6ND
    return N_star, D_star

def chinchilla_optimal(C_flops):
    '''Chinchilla: D* = 20*N*, C = 6*N*D = 120*N^2 => N* = sqrt(C/120).'''
    N_star = np.sqrt(C_flops / 120.0)
    D_star = 20.0 * N_star
    return N_star, D_star

budgets = [
    ('6e18 (~1B-scale)',   6e18),
    ('6e20 (~7B-scale)',   6e20),
    ('6e22 (~70B-scale)', 6e22),
    ('6e23 (GPT-4 est.)', 6e23),
]
print('{:<22} {:>12} {:>12} {:>12} {:>12}'.format('Compute Budget', 'Kaplan N*(B)', 'Kaplan D*(B)', 'Chinch N*(B)', 'Chinch D*(B)'))
print('-' * 74)
for name, C in budgets:
    kN, kD = kaplan_optimal(C)
    cN, cD = chinchilla_optimal(C)
    print('{:<22} {:>12.2f} {:>12.2f} {:>12.2f} {:>12.2f}'.format(name, kN/1e9, kD/1e9, cN/1e9, cD/1e9))
print('\nKaplan D/N ~ 1; Chinchilla D/N = 20 -- a 20x difference in data prescription.')
```

## Code 3 — Scaling Law Comparison Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

def kaplan_loss_C(C, a=4.0, alpha_c=0.057):
    '''Kaplan compute scaling: L(C) = a * C^(-alpha_c)'''
    return a * C ** (-alpha_c)

def chinchilla_loss_C(C, a=3.1, alpha_c=0.050):
    '''Chinchilla compute scaling with slightly different exponent'''
    return a * C ** (-alpha_c)

C_range = np.logspace(17, 24, 200)  # 1e17 to 1e24 FLOPs

# Approximate reference points from literature
ref_models = {
    'GPT-2 (1.5B)':     (1.5e21, 3.30),
    'GPT-3 (175B)':     (3.1e23, 2.88),
    'Chinchilla (70B)': (3.0e23, 2.55),
}

fig, ax = plt.subplots(figsize=(9, 5))
ax.loglog(C_range, kaplan_loss_C(C_range),     'b-',  lw=2, label='Kaplan (alpha_c = 0.057)')
ax.loglog(C_range, chinchilla_loss_C(C_range), 'g--', lw=2, label='Chinchilla fit (alpha_c = 0.050)')
colors = ['#e74c3c', '#8e44ad', '#27ae60']
for (name, (C, L)), col in zip(ref_models.items(), colors):
    ax.scatter(C, L, s=150, color=col, zorder=5, label=name)
ax.set_xlabel('Compute Budget C (FLOPs)', fontsize=12)
ax.set_ylabel('Test Loss L (nats)', fontsize=12)
ax.set_title('Predicted vs Actual Loss: Kaplan vs Chinchilla Compute Scaling', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, which='both', alpha=0.3)
plt.tight_layout()
plt.savefig('scaling_comparison.png', dpi=150)
plt.show()
```

## Irreducible Loss and the Entropy Floor

The full joint scaling law is L(N, D) = E + A/N^alpha + B/D^beta, where E approximately 1.69 nats is the irreducible loss — the entropy of natural language itself, representing information no model can predict regardless of size. The term A/N^alpha captures capacity-limited loss (model too small) and B/D^beta captures data-limited loss (insufficient training tokens). Fitting this joint formula requires a grid of (N, D, L) observations. The Chinchilla paper fitted E=1.69, A=406.4, alpha=0.34, B=410.7, beta=0.28 across over 400 models ranging from 70M to 16B parameters.

## Code 4 — Irreducible Loss Estimation

```python
import numpy as np
from scipy.optimize import minimize

def loss_model(params, N, D):
    '''L(N, D) = E + A * N^(-alpha) + B * D^(-beta)'''
    E, A, alpha, B, beta = params
    return E + A * N ** (-alpha) + B * D ** (-beta)

def objective(params, N_arr, D_arr, L_obs):
    '''Sum of squared residuals for least-squares fitting.'''
    return np.sum((loss_model(params, N_arr, D_arr) - L_obs) ** 2)

# Simulated loss grid: N in B params, D in B tokens
np.random.seed(42)
N_vals = np.array([0.1, 0.3, 1.0, 3.0, 10.0])
D_vals = np.array([10.0, 30.0, 100.0, 300.0])
N_grid, D_grid = np.meshgrid(N_vals, D_vals, indexing='ij')
N_flat, D_flat = N_grid.ravel(), D_grid.ravel()

# Ground truth: Chinchilla constants
true_p = [1.69, 406.4, 0.34, 410.7, 0.28]
L_obs  = loss_model(true_p, N_flat, D_flat) + np.random.normal(0, 0.01, len(N_flat))

# Jointly fit all 5 parameters using Nelder-Mead
result = minimize(objective, x0=[2.0, 300.0, 0.30, 300.0, 0.25],
                  args=(N_flat, D_flat, L_obs), method='Nelder-Mead',
                  options={'maxiter': 20000, 'xatol': 1e-7})
E_f, A_f, a_f, B_f, b_f = result.x
print('Fitted:  E={:.3f}, A={:.1f}, alpha={:.3f}, B={:.1f}, beta={:.3f}'.format(E_f, A_f, a_f, B_f, b_f))
print('Target:  E=1.690, A=406.4, alpha=0.340, B=410.7, beta=0.280')
print('MSE per point: {:.6f}'.format(result.fun / len(N_flat)))
```

The table below compares compute-optimal model size N* and token count D* predicted by Kaplan (2020) versus Chinchilla (2022) for three representative compute budgets. The dramatic difference in D/N ratio — roughly 1x for Kaplan vs 20x for Chinchilla — explains why early large language models such as GPT-3 and Gopher were massively undertrained on data relative to their parameter counts.

| Compute Budget (FLOPs) | Kaplan N* (B params) | Kaplan D* (B tokens) | Kaplan D/N | Chinchilla N* (B params) | Chinchilla D* (B tokens) | Chinchilla D/N |
| --- | --- | --- | --- | --- | --- | --- |
| 6e18 (~1B-scale) | 1.0 | 1.0 | ~1x | 0.22 | 4.5 | ~20x |
| 6e20 (~7B-scale) | 7.0 | 7.0 | ~1x | 2.24 | 44.7 | ~20x |
| 6e22 (~70B-scale) | 70.0 | 70.0 | ~1x | 22.4 | 447 | ~20x |

## Three Regimes and Caveats

Kaplan identified three limiting regimes for LLM training. The compute-limited regime applies when both N and D could grow freely but compute is fixed — L(C) law describes performance. The parameter-limited regime applies when the model is too small relative to data — the A/N^alpha term dominates loss and more parameters give rapid gains. The data-limited regime applies when data is exhausted or recycled — B/D^beta dominates and additional tokens degrade due to repetition. Important caveats: laws were measured on WebText2; transfer to code, math, or multilingual data may differ; architecture specifics matter less than total N; and Kaplan did not sweep D independently at each N, a confound that Chinchilla corrected.

- Compute-limited: grow N and D together along compute-optimal frontier using L(C) law
- Parameter-limited: small model with ample data — more parameters give rapid improvement
- Data-limited: data exhausted or recycled — diminishing returns, potential degradation
- Measured on WebText2 — may not generalize to code, math, or multilingual corpora
- Architecture (depth vs width, attention heads) contributes less than N to overall loss
- Kaplan's experiments lacked sufficient data variation — Chinchilla corrected this confound

> **Warning**: Kaplan scaling laws predict scaling models faster than data (N* proportional to C^0.73) — Chinchilla later showed this was wrong due to insufficient data in Kaplan's experiments, and corrected the optimal token-to-parameter ratio to ~20:1.

