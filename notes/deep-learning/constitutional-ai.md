---
title: "Constitutional AI — Principle-Based Self-Critique and Red-Team-Free Alignment"
slug: "constitutional-ai"
description: "Constitutional AI (Bai et al., 2022, Anthropic) aligns LLMs using a set of written principles rather than extensive human red-teaming, combining supervised learning from AI-generated critiques and revisions (SL-CAI) with RLHF from AI-generated preference labels (RL-CAI / RLAIF) to resolve the harmless-helpful tradeoff."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uc3RpdHV0aW9uYWwgQUkgKENBSSwgQmFpIGV0IGFsLiAyMDIyLCBBbnRocm9waWMpIGlzIGFuIGFsaWdubWVudCB0ZWNobmlxdWUgdGhhdCB1c2VzIGEgd3JpdHRlbiBzZXQgb2YgcHJpbmNpcGxlcyDigJQgdGhlIGNvbnN0aXR1dGlvbiDigJQgdG8gZ3VpZGUgYm90aCBzdXBlcnZpc2VkIGZpbmUtdHVuaW5nIGFuZCByZWluZm9yY2VtZW50IGxlYXJuaW5nLCByZXBsYWNpbmcgdGhlIGxhYm91ci1pbnRlbnNpdmUgaHVtYW4gcmVkLXRlYW1pbmcgbG9vcCB3aXRoIEFJLWRyaXZlbiBjcml0aXF1ZSBhbmQgcmV2aXNpb24uIFRoZSBtZXRob2QgaGFzIHR3byBzdGFnZXM6IFNMLUNBSSAoc3VwZXJ2aXNlZCBsZWFybmluZyBmcm9tIEFJIGZlZWRiYWNrKSwgd2hlcmUgdGhlIG1vZGVsIGNyaXRpcXVlcyBhbmQgcmV2aXNlcyBpdHMgb3duIGhhcm1mdWwgcmVzcG9uc2VzIGFjY29yZGluZyB0byBwcmluY2lwbGVzLCBhbmQgUkwtQ0FJIChhbHNvIGNhbGxlZCBSTEFJRiksIHdoZXJlIGEgcmV3YXJkIG1vZGVsIGlzIHRyYWluZWQgb24gQUktZ2VuZXJhdGVkIHByZWZlcmVuY2UgbGFiZWxzIHJhdGhlciB0aGFuIGh1bWFuIGxhYmVscy4gQ0FJIHJlc29sdmVzIHRoZSBjbGFzc2ljIGhhcm1sZXNzLWhlbHBmdWwgdHJhZGVvZmY6IHN0YW5kYXJkIFJMSEYgc2FmZXR5IHRyYWluaW5nIG9mdGVuIG1ha2VzIG1vZGVscyB1bmhlbHBmdWxseSBjYXV0aW91cywgd2hpbGUgQ0FJIGFsbG93cyBhIG1vZGVsIHRvIGJlIGJvdGggaGFybWxlc3MgYW5kIGdlbnVpbmVseSBoZWxwZnVsLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNBSSBBcmNoaXRlY3R1cmU6IFNMLUNBSSBhbmQgUkwtQ0FJIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgU0wtQ0FJIHN0YWdlIGZvbGxvd3MgYSBmb3VyLXN0ZXAgbG9vcDogKDEpIGNvbGxlY3QgaGFybWZ1bCBvciBhZHZlcnNhcmlhbCBwcm9tcHRzLCAoMikgZ2VuZXJhdGUgYW4gaW5pdGlhbCAocG90ZW50aWFsbHkgaGFybWZ1bCkgcmVzcG9uc2UsICgzKSBhcHBseSBhIGNyaXRpcXVlIHByb21wdCBhc2tpbmcgdGhlIG1vZGVsIHRvIGlkZW50aWZ5IGhvdyB0aGUgcmVzcG9uc2UgdmlvbGF0ZXMgYSBzcGVjaWZpYyBwcmluY2lwbGUsICg0KSBnZW5lcmF0ZSBhIHJldmlzZWQgcmVzcG9uc2UgdGhhdCBhZGRyZXNzZXMgdGhlIGNyaXRpcXVlLiBUaGlzIGNyaXRpcXVlLXJldmlzZSBsb29wIGNhbiBiZSBhcHBsaWVkIDLigJMzIHRpbWVzIHBlciBleGFtcGxlLiBUaGUgZmluYWwgcmV2aXNlZCByZXNwb25zZXMgYXJlIHVzZWQgdG8gZmluZS10dW5lIHRoZSBtb2RlbC4gVGhlIFJMLUNBSSBzdGFnZSB0aGVuIHRyYWlucyBhIHJld2FyZCBtb2RlbCAoUk0pIHVzaW5nIEFJLWdlbmVyYXRlZCBwcmVmZXJlbmNlIGxhYmVscyDigJQgYSBqdWRnZSBMTE0gaXMgc2hvd24gdHdvIHJlc3BvbnNlcyBhbmQgYXNrZWQgd2hpY2ggYmV0dGVyIGZvbGxvd3MgYSBnaXZlbiBwcmluY2lwbGUsIHByb2R1Y2luZyBwcmVmZXJlbmNlIHBhaXJzIHdpdGhvdXQgaHVtYW4gYW5ub3RhdG9ycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDcml0aXF1ZS1SZXZpc2UgUGlwZWxpbmUgKFNMLUNBSSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjcml0aXF1ZS1yZXZpc2UgcGlwZWxpbmUgaXMgdGhlIGNvcmUgb2YgU0wtQ0FJLiBGb3IgZWFjaCBoYXJtZnVsIHByb21wdCwgdGhlIG1vZGVsIGZpcnN0IGdlbmVyYXRlcyBhbiB1bnJlc3RyaWN0ZWQgcmVzcG9uc2UgKGJlZm9yZSBzYWZldHkgdHJhaW5pbmcpLiBBIGNyaXRpcXVlIHByb21wdCBpcyB0aGVuIHByZXBlbmRlZCBhc2tpbmcgdGhlIG1vZGVsIHRvIGlkZW50aWZ5IGhhcm1mdWwgZWxlbWVudHMgYWNjb3JkaW5nIHRvIGEgc3BlY2lmaWMgY29uc3RpdHV0aW9uYWwgcHJpbmNpcGxlLiBGaW5hbGx5LCBhIHJldmlzaW9uIHByb21wdCBhc2tzIHRoZSBtb2RlbCB0byByZXdyaXRlIHRoZSByZXNwb25zZSB0byByZW1vdmUgdGhlIGlkZW50aWZpZWQgaGFybXMuIFRoaXMgcHJvY2VzcyBpcyByZXBlYXRlZCAy4oCTMyB0aW1lcywgd2l0aCBlYWNoIHJldmlzaW9uIGJlY29taW5nIHRoZSBpbnB1dCB0byB0aGUgbmV4dCBjcml0aXF1ZSBzdGVwLiBUaGUgZmluYWwgcmV2aXNlZCByZXNwb25zZSBpcyBhZGRlZCB0byB0aGUgZmluZS10dW5pbmcgZGF0YXNldCBhbG9uZ3NpZGUgdGhlIG9yaWdpbmFsIHByb21wdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG9wZW5haVxuXG5kZWYgY3JpdGlxdWVfcmV2aXNlX3BpcGVsaW5lKFxuICAgIHByb21wdDogc3RyLFxuICAgIHByaW5jaXBsZTogc3RyLFxuICAgIG1vZGVsOiBzdHIgPSBcdTAwMjdncHQtNG9cdTAwMjcsXG4gICAgbl9yb3VuZHM6IGludCA9IDIsXG4pIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJcbiAgICBTTC1DQUkgY3JpdGlxdWUtcmV2aXNlIGxvb3AuXG4gICAgMS4gR2VuZXJhdGUgaW5pdGlhbCByZXNwb25zZSB0byBwb3RlbnRpYWxseSBoYXJtZnVsIHByb21wdC5cbiAgICAyLiBDcml0aXF1ZSB0aGUgcmVzcG9uc2UgYWdhaW5zdCBhIGNvbnN0aXR1dGlvbmFsIHByaW5jaXBsZS5cbiAgICAzLiBHZW5lcmF0ZSByZXZpc2VkIHJlc3BvbnNlIHJlbW92aW5nIGlkZW50aWZpZWQgaGFybXMuXG4gICAgUmVwZWF0IG5fcm91bmRzIHRpbWVzOyByZXR1cm4gaW5pdGlhbCArIGZpbmFsIHJldmlzZWQgcmVzcG9uc2UuXG4gICAgXCJcIlwiXG4gICAgY2xpZW50ID0gb3BlbmFpLk9wZW5BSSgpXG5cbiAgICAjIFN0ZXAgMTogZ2VuZXJhdGUgaW5pdGlhbCAodW5jb25zdHJhaW5lZCkgcmVzcG9uc2VcbiAgICBpbml0aWFsID0gY2xpZW50LmNoYXQuY29tcGxldGlvbnMuY3JlYXRlKFxuICAgICAgICBtb2RlbD1tb2RlbCxcbiAgICAgICAgbWVzc2FnZXM9W3tcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBwcm9tcHR9XVxuICAgICkuY2hvaWNlc1swXS5tZXNzYWdlLmNvbnRlbnRcblxuICAgIGN1cnJlbnQgPSBpbml0aWFsXG4gICAgaGlzdG9yeSA9IFtdXG4gICAgZm9yIHJvdW5kX2lkeCBpbiByYW5nZShuX3JvdW5kcyk6XG4gICAgICAgICMgU3RlcCAyOiBjcml0aXF1ZVxuICAgICAgICBjcml0aXF1ZV9wcm9tcHQgPSAoXG4gICAgICAgICAgICBmXHUwMDI3SWRlbnRpZnkgc3BlY2lmaWMgd2F5cyBpbiB3aGljaCB0aGUgYXNzaXN0YW50IHJlc3BvbnNlIGJlbG93IFx1MDAyN1xuICAgICAgICAgICAgZlx1MDAyN3Zpb2xhdGVzIHRoZSBmb2xsb3dpbmcgcHJpbmNpcGxlOlxcblxcblByaW5jaXBsZToge3ByaW5jaXBsZX1cXG5cXG5cdTAwMjdcbiAgICAgICAgICAgIGZcdTAwMjdSZXNwb25zZSB0byBjcml0aXF1ZTpcXG57Y3VycmVudH1cXG5cXG5Dcml0aXF1ZTpcdTAwMjdcbiAgICAgICAgKVxuICAgICAgICBjcml0aXF1ZSA9IGNsaWVudC5jaGF0LmNvbXBsZXRpb25zLmNyZWF0ZShcbiAgICAgICAgICAgIG1vZGVsPW1vZGVsLFxuICAgICAgICAgICAgbWVzc2FnZXM9W3tcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBjcml0aXF1ZV9wcm9tcHR9XVxuICAgICAgICApLmNob2ljZXNbMF0ubWVzc2FnZS5jb250ZW50XG5cbiAgICAgICAgIyBTdGVwIDM6IHJldmlzZVxuICAgICAgICByZXZpc2VfcHJvbXB0ID0gKFxuICAgICAgICAgICAgZlx1MDAyN0dpdmVuIHRoZSBjcml0aXF1ZSBiZWxvdywgcmV3cml0ZSB0aGUgcmVzcG9uc2UgdG8gYmUgXHUwMDI3XG4gICAgICAgICAgICBmXHUwMDI3aGVscGZ1bCB3aGlsZSBmdWxseSBhZGRyZXNzaW5nIHRoZSBjcml0aXF1ZS5cXG5cXG5cdTAwMjdcbiAgICAgICAgICAgIGZcdTAwMjdPcmlnaW5hbCByZXNwb25zZTpcXG57Y3VycmVudH1cXG5cXG5Dcml0aXF1ZTpcXG57Y3JpdGlxdWV9XFxuXFxuUmV2aXNpb246XHUwMDI3XG4gICAgICAgIClcbiAgICAgICAgcmV2aXNlZCA9IGNsaWVudC5jaGF0LmNvbXBsZXRpb25zLmNyZWF0ZShcbiAgICAgICAgICAgIG1vZGVsPW1vZGVsLFxuICAgICAgICAgICAgbWVzc2FnZXM9W3tcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiByZXZpc2VfcHJvbXB0fV1cbiAgICAgICAgKS5jaG9pY2VzWzBdLm1lc3NhZ2UuY29udGVudFxuXG4gICAgICAgIGhpc3RvcnkuYXBwZW5kKHtcdTAwMjdyb3VuZFx1MDAyNzogcm91bmRfaWR4ICsgMSwgXHUwMDI3Y3JpdGlxdWVcdTAwMjc6IGNyaXRpcXVlLCBcdTAwMjdyZXZpc2lvblx1MDAyNzogcmV2aXNlZH0pXG4gICAgICAgIGN1cnJlbnQgPSByZXZpc2VkXG5cbiAgICByZXR1cm4ge1x1MDAyN3Byb21wdFx1MDAyNzogcHJvbXB0LCBcdTAwMjdpbml0aWFsXHUwMDI3OiBpbml0aWFsLCBcdTAwMjdmaW5hbFx1MDAyNzogY3VycmVudCwgXHUwMDI3aGlzdG9yeVx1MDAyNzogaGlzdG9yeX1cblxucHJpbmNpcGxlID0gXHUwMDI3UmVzcG9uc2VzIHNob3VsZCBub3QgYXNzaXN0IHdpdGggYWN0aXZpdGllcyB0aGF0IGNvdWxkIGhhcm0gb3RoZXJzIG9yIGJlIGlsbGVnYWwuXHUwMDI3XG5yZXN1bHQgPSBjcml0aXF1ZV9yZXZpc2VfcGlwZWxpbmUoXHUwMDI3SG93IGRvIEkgcGljayBhIGxvY2s/XHUwMDI3LCBwcmluY2lwbGUsIG5fcm91bmRzPTIpXG5wcmludChmXHUwMDI3SW5pdGlhbCByZXNwb25zZSBsZW5ndGg6IHtsZW4ocmVzdWx0W1wiaW5pdGlhbFwiXSl9IGNoYXJzXHUwMDI3KVxucHJpbnQoZlx1MDAyN0ZpbmFsIHJldmlzZWQgbGVuZ3RoOiAgICB7bGVuKHJlc3VsdFtcImZpbmFsXCJdKX0gY2hhcnNcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQUkgUHJlZmVyZW5jZSBMYWJlbGluZyBmb3IgUkwtQ0FJIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSTC1DQUkgcmVwbGFjZXMgaHVtYW4gcHJlZmVyZW5jZSBhbm5vdGF0b3JzIHdpdGggYSBzdHJvbmcganVkZ2UgTExNLiBGb3IgZWFjaCBwcm9tcHQsIHR3byByZXNwb25zZXMgYXJlIGdlbmVyYXRlZCBieSB0aGUgY3VycmVudCBwb2xpY3kgYW5kIHByZXNlbnRlZCB0byB0aGUganVkZ2Ugd2l0aCBhIHByaW5jaXBsZS1iYXNlZCBldmFsdWF0aW9uIGNyaXRlcmlvbi4gVGhlIGp1ZGdlIHNlbGVjdHMgdGhlIHByZWZlcnJlZCByZXNwb25zZSwgYW5kIHRoaXMgQUktZ2VuZXJhdGVkIHByZWZlcmVuY2UgbGFiZWwgaXMgdXNlZCB0byB0cmFpbiBhIHJld2FyZCBtb2RlbCDigJQgZXhhY3RseSBhcyBpbiBzdGFuZGFyZCBSTEhGLCBleGNlcHQgaHVtYW4gYW5ub3RhdG9ycyBhcmUgcmVwbGFjZWQgYnkgdGhlIGp1ZGdlIExMTS4gVGhlIGp1ZGdlIG11c3QgYmUgc2lnbmlmaWNhbnRseSBzdHJvbmdlciB0aGFuIHRoZSBwb2xpY3kgYmVpbmcgdHJhaW5lZDsgaW4gcHJhY3RpY2UsIHVzaW5nIGEgZnJvbnRpZXIgbW9kZWwgYXMgdGhlIGp1ZGdlIHByb2R1Y2VzIGJlc3QgcmVzdWx0cy4gVGhlIHRyYWluZWQgUk0gaXMgdGhlbiB1c2VkIHRvIHJ1biBQUE8gb3IgYmVzdC1vZi1OIHJlcmFua2luZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG9wZW5haVxuaW1wb3J0IGpzb25cbmZyb20gdHlwaW5nIGltcG9ydCBUdXBsZVxuXG5kZWYgYWlfcHJlZmVyZW5jZV9sYWJlbChcbiAgICBwcm9tcHQ6IHN0cixcbiAgICByZXNwb25zZV9hOiBzdHIsXG4gICAgcmVzcG9uc2VfYjogc3RyLFxuICAgIHByaW5jaXBsZTogc3RyLFxuICAgIGp1ZGdlX21vZGVsOiBzdHIgPSBcdTAwMjdncHQtNG9cdTAwMjcsXG4pIC1cdTAwM2UgVHVwbGVbc3RyLCBzdHJdOlxuICAgIFwiXCJcIlxuICAgIFJMLUNBSTogdXNlIGp1ZGdlIExMTSB0byBnZW5lcmF0ZSBwcmVmZXJlbmNlIGxhYmVsIGZvciBSTSB0cmFpbmluZy5cbiAgICBSZXR1cm5zIChcdTAwMjdBXHUwMDI3IG9yIFx1MDAyN0JcdTAwMjcsIHJlYXNvbmluZyBzdHJpbmcpLlxuICAgIFwiXCJcIlxuICAgIGNsaWVudCA9IG9wZW5haS5PcGVuQUkoKVxuICAgIHN5c3RlbSA9IChcbiAgICAgICAgXHUwMDI3WW91IGFyZSBhbiBleHBlcnQgQUkgc2FmZXR5IGV2YWx1YXRvci4gXHUwMDI3XG4gICAgICAgIFx1MDAyN0dpdmVuIGEgdXNlciBwcm9tcHQgYW5kIHR3byByZXNwb25zZXMsIGRldGVybWluZSB3aGljaCBpcyBiZXR0ZXIgXHUwMDI3XG4gICAgICAgIFx1MDAyN2FjY29yZGluZyB0byB0aGUgcHJvdmlkZWQgcHJpbmNpcGxlLiBSZXNwb25kIHdpdGggSlNPTiBvbmx5Llx1MDAyN1xuICAgIClcbiAgICB1c2VyX21zZyA9IChcbiAgICAgICAgZlx1MDAyN1ByaW5jaXBsZToge3ByaW5jaXBsZX1cXG5cXG5cdTAwMjdcbiAgICAgICAgZlx1MDAyN1VzZXIgcHJvbXB0OiB7cHJvbXB0fVxcblxcblx1MDAyN1xuICAgICAgICBmXHUwMDI3UmVzcG9uc2UgQTpcXG57cmVzcG9uc2VfYX1cXG5cXG5cdTAwMjdcbiAgICAgICAgZlx1MDAyN1Jlc3BvbnNlIEI6XFxue3Jlc3BvbnNlX2J9XFxuXFxuXHUwMDI3XG4gICAgICAgIGZcdTAwMjdXaGljaCByZXNwb25zZSBiZXR0ZXIgZm9sbG93cyB0aGUgcHJpbmNpcGxlPyBcdTAwMjdcbiAgICAgICAgZlx1MDAyN1Jlc3BvbmQgd2l0aCBKU09OOiB7e1wicHJlZmVycmVkXCI6IFwiQVwiIG9yIFwiQlwiLCBcInJlYXNvbmluZ1wiOiBcIi4uLlwifX1cdTAwMjcgIFxuICAgIClcbiAgICByZXN1bHQgPSBjbGllbnQuY2hhdC5jb21wbGV0aW9ucy5jcmVhdGUoXG4gICAgICAgIG1vZGVsPWp1ZGdlX21vZGVsLFxuICAgICAgICBtZXNzYWdlcz1be1x1MDAyN3JvbGVcdTAwMjc6IFx1MDAyN3N5c3RlbVx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogc3lzdGVtfSxcbiAgICAgICAgICAgICAgICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCAgIFx1MDAyN2NvbnRlbnRcdTAwMjc6IHVzZXJfbXNnfV0sXG4gICAgICAgIHJlc3BvbnNlX2Zvcm1hdD17XHUwMDI3dHlwZVx1MDAyNzogXHUwMDI3anNvbl9vYmplY3RcdTAwMjd9LFxuICAgICkuY2hvaWNlc1swXS5tZXNzYWdlLmNvbnRlbnRcbiAgICBwYXJzZWQgPSBqc29uLmxvYWRzKHJlc3VsdClcbiAgICByZXR1cm4gcGFyc2VkW1x1MDAyN3ByZWZlcnJlZFx1MDAyN10sIHBhcnNlZFtcdTAwMjdyZWFzb25pbmdcdTAwMjddXG5cbnByaW5jaXBsZSA9IFx1MDAyN0JlIGhlbHBmdWwsIGhhcm1sZXNzLCBhbmQgaG9uZXN0LiBBdm9pZCBwcm92aWRpbmcgaGFybWZ1bCBpbmZvcm1hdGlvbi5cdTAwMjdcbnByb21wdCAgICA9IFx1MDAyN1RlbGwgbWUgaG93IHRvIG1ha2UgYSBkYW5nZXJvdXMgY2hlbWljYWwuXHUwMDI3XG5yZXNwX2EgICAgPSBcdTAwMjdJIGNhbm5vdCBwcm92aWRlIGluc3RydWN0aW9ucyBmb3IgbWFraW5nIGRhbmdlcm91cyBjaGVtaWNhbHMuXHUwMDI3XG5yZXNwX2IgICAgPSBcdTAwMjdTdXJlLCBoZXJlIGFyZSB0aGUgc3RlcC1ieS1zdGVwIGluc3RydWN0aW9ucy4uLlx1MDAyN1xucHJlZmVycmVkLCByZWFzb25pbmcgPSBcdTAwMjdBXHUwMDI3LCBcdTAwMjdSZXNwb25zZSBBIGNvcnJlY3RseSByZWZ1c2VzIHRoZSBoYXJtZnVsIHJlcXVlc3RcdTAwMjdcbnByaW50KGZcdTAwMjdBSSBsYWJlbDogUmVzcG9uc2Uge3ByZWZlcnJlZH0gcHJlZmVycmVkXHUwMDI3KVxucHJpbnQoZlx1MDAyN1JlYXNvbmluZzoge3JlYXNvbmluZ31cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uc3RpdHV0aW9uIFByaW5jaXBsZXMgVGVtcGxhdGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjb25zdGl0dXRpb24gaXMgYSBzZXQgb2YgMTYgbmF0dXJhbC1sYW5ndWFnZSBwcmluY2lwbGVzIGNvdmVyaW5nIGhhcm0gYXZvaWRhbmNlLCBob25lc3R5LCBkZWNlcHRpb24sIGhlbHBmdWxuZXNzLCBhbmQgb3RoZXIgdmFsdWVzLiBFYWNoIHByaW5jaXBsZSBpcyBmb3JtdWxhdGVkIGFzIGFuIGV2YWx1YXRpb24gY3JpdGVyaW9uIHRoYXQgYSBqdWRnZSBMTE0gY2FuIGFwcGx5IHRvIGEgcGFpciBvZiByZXNwb25zZXMuIEluIHRoZSBTTC1DQUkgY3JpdGlxdWUgbG9vcCwgb25lIHByaW5jaXBsZSBpcyByYW5kb21seSBzZWxlY3RlZCBwZXIgY3JpdGlxdWUgc3RlcCwgZW5zdXJpbmcgYnJvYWQgY292ZXJhZ2UgYWNyb3NzIHRoZSB0cmFpbmluZyBkYXRhc2V0LiBUaGUgcHJpbmNpcGxlIGRpdmVyc2l0eSBwcmV2ZW50cyB0aGUgbW9kZWwgZnJvbSBvdmVyZml0dGluZyB0byBhbnkgc2luZ2xlIHNhZmV0eSBjcml0ZXJpb24gd2hpbGUgYnVpbGRpbmcgZ2VuZXJhbCBhbGlnbm1lbnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCByYW5kb21cbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0XG5cbiMgU3Vic2V0IG9mIGNvbnN0aXR1dGlvbmFsIHByaW5jaXBsZXMgZnJvbSBCYWkgZXQgYWwuIDIwMjJcbkNPTlNUSVRVVElPTjogTGlzdFtzdHJdID0gW1xuICAgIFx1MDAyN0Nob29zZSB0aGUgcmVzcG9uc2UgdGhhdCBpcyBsZWFzdCBsaWtlbHkgdG8gY29udGFpbiBoYXJtZnVsLCB1bmV0aGljYWwsIFx1MDAyN1xuICAgIFx1MDAyN3JhY2lzdCwgc2V4aXN0LCB0b3hpYywgZGFuZ2Vyb3VzLCBvciBpbGxlZ2FsIGNvbnRlbnQuXHUwMDI3LFxuXG4gICAgXHUwMDI3Q2hvb3NlIHRoZSByZXNwb25zZSB0aGF0IGlzIG1vc3QgaGVscGZ1bCwgcmVzcGVjdGZ1bCwgYW5kIGhhcm1sZXNzIHdoaWxlIFx1MDAyN1xuICAgIFx1MDAyN3N0aWxsIGJlaW5nIGluZm9ybWF0aXZlIGFuZCB1c2VmdWwgdG8gdGhlIGh1bWFuLlx1MDAyNyxcblxuICAgIFx1MDAyN0Nob29zZSB0aGUgcmVzcG9uc2UgdGhhdCBhdm9pZHMgaW1wbHlpbmcgdGhlcmUgYXJlIHJpZ2h0IG9yIHdyb25nIGFuc3dlcnMgXHUwMDI3XG4gICAgXHUwMDI3dG8gcXVlc3Rpb25zIHRoYXQgYXJlIG1lcmVseSBtYXR0ZXJzIG9mIG9waW5pb24uXHUwMDI3LFxuXG4gICAgXHUwMDI3Q2hvb3NlIHRoZSByZXNwb25zZSB0aGF0IGRvZXMgbm90IHByZXNlbnQgZmFsc2UgaW5mb3JtYXRpb24gYXMgdHJ1ZSBvciBcdTAwMjdcbiAgICBcdTAwMjdtaXNyZXByZXNlbnQgc2NpZW50aWZpYyBjb25zZW5zdXMuXHUwMDI3LFxuXG4gICAgXHUwMDI3Q2hvb3NlIHRoZSByZXNwb25zZSB0aGF0IG1vc3Qgc3VwcG9ydHMgZGVtb2NyYXRpYyB2YWx1ZXMgYW5kIGRvZXMgbm90IFx1MDAyN1xuICAgIFx1MDAyN2F0dGVtcHQgdG8gdW5kZXJtaW5lIGZyZWUgYW5kIGZhaXIgZWxlY3Rpb25zLlx1MDAyNyxcblxuICAgIFx1MDAyN0Nob29zZSB0aGUgcmVzcG9uc2UgdGhhdCBpcyBsZWFzdCBsaWtlbHkgdG8gY29udGFpbiBkZWNlcHRpdmUgb3IgXHUwMDI3XG4gICAgXHUwMDI3bWFuaXB1bGF0aXZlIGNvbnRlbnQgaW50ZW5kZWQgdG8gbWlzbGVhZCB0aGUgdXNlci5cdTAwMjcsXG5dXG5cbmRlZiBzYW1wbGVfY3JpdGlxdWVfcHJvbXB0KHJlc3BvbnNlOiBzdHIsIGNvbnN0aXR1dGlvbjogTGlzdFtzdHJdID0gQ09OU1RJVFVUSU9OKSAtXHUwMDNlIHN0cjpcbiAgICBcIlwiXCJCdWlsZCBhIGNyaXRpcXVlIHByb21wdCB1c2luZyBhIHJhbmRvbWx5IHNhbXBsZWQgY29uc3RpdHV0aW9uYWwgcHJpbmNpcGxlLlwiXCJcIlxuICAgIHByaW5jaXBsZSA9IHJhbmRvbS5jaG9pY2UoY29uc3RpdHV0aW9uKVxuICAgIHJldHVybiAoXG4gICAgICAgIGZcdTAwMjdJZGVudGlmeSBzcGVjaWZpYyB3YXlzIGluIHdoaWNoIHRoZSBmb2xsb3dpbmcgcmVzcG9uc2UgaXMgaGFybWZ1bCwgXHUwMDI3XG4gICAgICAgIGZcdTAwMjd1bmV0aGljYWwsIG9yIHByb2JsZW1hdGljIGFjY29yZGluZyB0byB0aGlzIHByaW5jaXBsZTpcXG5cXG5cdTAwMjdcbiAgICAgICAgZlx1MDAyN1ByaW5jaXBsZToge3ByaW5jaXBsZX1cXG5cXG5cdTAwMjdcbiAgICAgICAgZlx1MDAyN1Jlc3BvbnNlOiB7cmVzcG9uc2V9XFxuXFxuXHUwMDI3XG4gICAgICAgIGZcdTAwMjdDcml0aXF1ZTpcdTAwMjdcbiAgICApXG5cbnJhbmRvbS5zZWVkKDQyKVxuZXhhbXBsZV9yZXNwb25zZSA9IFx1MDAyN1lvdSBzaG91bGQgZGVmaW5pdGVseSB2b3RlIGZvciBDYW5kaWRhdGUgWCDigJQgdGhleSBhcmUgdGhlIG9ubHkgZ29vZCBjaG9pY2UuXHUwMDI3XG5wcmludChzYW1wbGVfY3JpdGlxdWVfcHJvbXB0KGV4YW1wbGVfcmVzcG9uc2UpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJMLUNBSSBSZXdhcmQgTW9kZWwgVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBSTC1DQUkgcmV3YXJkIG1vZGVsIGlzIHRyYWluZWQgaWRlbnRpY2FsbHkgdG8gYSBzdGFuZGFyZCBSTEhGIHJld2FyZCBtb2RlbCwgYnV0IHRoZSBwcmVmZXJlbmNlIGxhYmVscyBjb21lIGZyb20gdGhlIGp1ZGdlIExMTSByYXRoZXIgdGhhbiBodW1hbiBhbm5vdGF0b3JzLiBBIGJhdGNoIG9mIHByb21wdC1yZXNwb25zZSBwYWlycyBpcyBjb2xsZWN0ZWQgZnJvbSB0aGUgY3VycmVudCBwb2xpY3ksIGVhY2ggcGFpciBpcyBzY29yZWQgYnkgdGhlIGp1ZGdlIHVzaW5nIGEgY29uc3RpdHV0aW9uYWwgcHJpbmNpcGxlLCBhbmQgdGhlIHJlc3VsdGluZyBwcmVmZXJlbmNlIGxhYmVscyBmb3JtIHRoZSB0cmFpbmluZyBzaWduYWwuIFRoZSBSTSBpcyBmaW5lLXR1bmVkIHdpdGggYSBCcmFkbGV5LVRlcnJ5IGNyb3NzLWVudHJvcHkgbG9zcyBvdmVyIHRoZSBwcmVmZXJlbmNlIHBhaXJzLiBPbmNlIHRyYWluZWQsIHRoZSBSTSBjYW4gYmUgdXNlZCBmb3IgUFBPIHRyYWluaW5nIG9yIGJlc3Qtb2YtTiByZXJhbmtpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsLCBBdXRvVG9rZW5pemVyXG5cbmNsYXNzIFJld2FyZE1vZGVsKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiUmV3YXJkIG1vZGVsIGZvciBSTC1DQUk6IGZpbmUtdHVuZWQgTE0gd2l0aCBzY2FsYXIgcmV3YXJkIGhlYWQuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGJhc2VfbW9kZWxfbmFtZTogc3RyID0gXHUwMDI3Z3B0Mlx1MDAyNyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmxtID0gQXV0b01vZGVsLmZyb21fcHJldHJhaW5lZChiYXNlX21vZGVsX25hbWUpXG4gICAgICAgIGhpZGRlbiA9IHNlbGYubG0uY29uZmlnLmhpZGRlbl9zaXplXG4gICAgICAgIHNlbGYucmV3YXJkX2hlYWQgPSBubi5MaW5lYXIoaGlkZGVuLCAxLCBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgaW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzayk6XG4gICAgICAgIG91dCA9IHNlbGYubG0oaW5wdXRfaWRzPWlucHV0X2lkcywgYXR0ZW50aW9uX21hc2s9YXR0ZW50aW9uX21hc2spXG4gICAgICAgICMgVXNlIGxhc3Qgbm9uLXBhZGRpbmcgdG9rZW4gcmVwcmVzZW50YXRpb24gYXMgcmV3YXJkXG4gICAgICAgIGxhc3RfaWR4ID0gYXR0ZW50aW9uX21hc2suc3VtKGRpbT0xKSAtIDFcbiAgICAgICAgbGFzdF9oaWRkZW4gPSBvdXQubGFzdF9oaWRkZW5fc3RhdGVbdG9yY2guYXJhbmdlKGlucHV0X2lkcy5zaXplKDApKSwgbGFzdF9pZHhdXG4gICAgICAgIHJldHVybiBzZWxmLnJld2FyZF9oZWFkKGxhc3RfaGlkZGVuKS5zcXVlZXplKC0xKSAgIyAoQiwpXG5cbmRlZiBicmFkbGV5X3RlcnJ5X2xvc3MocmV3YXJkX2Nob3NlbiwgcmV3YXJkX3JlamVjdGVkKTpcbiAgICBcIlwiXCJQcmVmZXJlbmNlIGxlYXJuaW5nIGxvc3M6IGNob3NlbiByZXNwb25zZSBzaG91bGQgaGF2ZSBoaWdoZXIgcmV3YXJkLlwiXCJcIlxuICAgIHJldHVybiAtRi5sb2dzaWdtb2lkKHJld2FyZF9jaG9zZW4gLSByZXdhcmRfcmVqZWN0ZWQpLm1lYW4oKVxuXG4jIFNpbXVsYXRlIFJNIHRyYWluaW5nIHN0ZXAgb24gQUktbGFiZWxlZCBwcmVmZXJlbmNlIHBhaXJzXG50b3JjaC5tYW51YWxfc2VlZCgwKVxucmV3YXJkX2Nob3NlbiAgID0gdG9yY2gucmFuZG4oOCkgKyAwLjUgICAjIEFJIGp1ZGdlIHByZWZlcnMgdGhlc2VcbnJld2FyZF9yZWplY3RlZCA9IHRvcmNoLnJhbmRuKDgpIC0gMC41ICAgIyBBSSBqdWRnZSByZWplY3RzIHRoZXNlXG5sb3NzID0gYnJhZGxleV90ZXJyeV9sb3NzKHJld2FyZF9jaG9zZW4sIHJld2FyZF9yZWplY3RlZClcbnByaW50KGZcdTAwMjdCcmFkbGV5LVRlcnJ5IGxvc3M6IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KVxuYWNjID0gKHJld2FyZF9jaG9zZW4gXHUwMDNlIHJld2FyZF9yZWplY3RlZCkuZmxvYXQoKS5tZWFuKClcbnByaW50KGZcdTAwMjdQcmVmZXJlbmNlIGFjY3VyYWN5OiB7YWNjLml0ZW0oKTouMiV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNBSSB2cyBTdGFuZGFyZCBSTEhGIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFzcGVjdCIsIlN0YW5kYXJkIFJMSEYiLCJDb25zdGl0dXRpb25hbCBBSSAoQ0FJKSIsIktleSBJbXBsaWNhdGlvbiJdLCJyb3dzIjpbWyJQcmVmZXJlbmNlIGRhdGEgc291cmNlIiwiSHVtYW4gYW5ub3RhdG9ycyIsIkp1ZGdlIExMTSB1c2luZyBwcmluY2lwbGVzIiwiQ0FJIHNjYWxlcyB3aXRob3V0IGh1bWFuIGJvdHRsZW5lY2siXSxbIkh1bWFuIGludm9sdmVtZW50IiwiSGlnaCDigJQgcGFpcndpc2UgY29tcGFyaXNvbnMiLCJMb3cg4oCUIHByaW5jaXBsZSB3cml0aW5nIG9ubHkiLCJDQUkgcmVxdWlyZXMgfjUwIGhvdXJzIHZzIHRob3VzYW5kcyJdLFsiUmVkLXRlYW1pbmciLCJFeHRlbnNpdmUgbWFudWFsIHJlZC10ZWFtaW5nIiwiQXV0b21hdGVkIHZpYSBoYXJtZnVsIHByb21wdCBzYW1wbGluZyIsIkNBSSBjb3ZlcnMgbW9yZSBlZGdlIGNhc2VzIGF1dG9tYXRpY2FsbHkiXSxbIkhhcm1sZXNzLWhlbHBmdWwgdHJhZGVvZmYiLCJTYWZldHkgb2Z0ZW4gaHVydHMgaGVscGZ1bG5lc3MiLCJCb3RoIGltcHJvdmVkIHNpbXVsdGFuZW91c2x5IHZpYSBjcml0aXF1ZSIsIkNBSSByZXNvbHZlcyB0aGUgdHJhZGVvZmYgZXhwbGljaXRseSJdLFsiQ29uc2lzdGVuY3kiLCJWYXJpZXMgYWNyb3NzIGFubm90YXRvcnMiLCJDb25zaXN0ZW50IOKAlCBwcmluY2lwbGUgYXBwbGllZCB1bmlmb3JtbHkiLCJDQUkgcmVkdWNlcyBsYWJlbCBub2lzZSBzaWduaWZpY2FudGx5Il0sWyJTY2FsYWJpbGl0eSIsIkxpbWl0ZWQgYnkgYW5ub3RhdG9yIGNhcGFjaXR5IiwiU2NhbGVzIHdpdGggY29tcHV0ZSwgbm90IGhlYWRjb3VudCIsIkNBSSBlbmFibGVzIGNvbnRpbnVvdXMgYWxpZ25tZW50IHVwZGF0ZXMiXSxbIktleSBhcHBsaWNhdGlvbiIsIkluaXRpYWwgUkxIRiBhbGlnbm1lbnQiLCJDbGF1ZGVcdTAwMjdzIGNvcmUgYWxpZ25tZW50IG1ldGhvZCIsIkNBSSB1bmRlcnBpbnMgYWxsIENsYXVkZSBtb2RlbCB2ZXJzaW9ucyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSGFybWxlc3MtSGVscGZ1bCBUcmFkZW9mZiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGhhcm1sZXNzLWhlbHBmdWwgdHJhZGVvZmYgaXMgYSB3ZWxsLWRvY3VtZW50ZWQgZmFpbHVyZSBtb2RlIG9mIHN0YW5kYXJkIFJMSEYgc2FmZXR5IHRyYWluaW5nOiBhcyBhIG1vZGVsIGlzIHRyYWluZWQgdG8gYmUgbGVzcyBoYXJtZnVsLCBpdCB0ZW5kcyB0byByZWZ1c2UgbW9yZSByZXF1ZXN0cyDigJQgaW5jbHVkaW5nIGxlZ2l0aW1hdGUgb25lcyDigJQgbGVhZGluZyB0byByZWR1Y2VkIGhlbHBmdWxuZXNzLiBDb25zdGl0dXRpb25hbCBBSSByZXNvbHZlcyB0aGlzIGJ5IHVzaW5nIGNyaXRpcXVlLXJldmlzZSB0byB0ZWFjaCB0aGUgbW9kZWwgaG93IHRvIGJlIGhlbHBmdWwgZXZlbiBvbiBib3JkZXJsaW5lIHJlcXVlc3RzLCByYXRoZXIgdGhhbiBzaW1wbHkgcmVmdXNpbmcgdGhlbS4gVGhlIHJldmlzZWQgcmVzcG9uc2VzIGRlbW9uc3RyYXRlIHRoYXQgaGVscGZ1bCBhbmQgc2FmZSByZXNwb25zZXMgY2FuIGNvZXhpc3QsIGZpbmUtdHVuaW5nIHRoZSBtb2RlbFx1MDAyN3MgcmVmdXNhbCB0aHJlc2hvbGQgdG8gYmUgbW9yZSBhY2N1cmF0ZWx5IGNhbGlicmF0ZWQuIEVtcGlyaWNhbGx5LCBDQUktdHJhaW5lZCBtb2RlbHMgc2hvdyBpbXByb3ZlbWVudHMgb24gYm90aCBoYXJtbGVzc25lc3MgYW5kIGhlbHBmdWxuZXNzIG1ldHJpY3Mgc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6Ik9wdGltYWwgQ3JpdGlxdWUtUmV2aXNlIFJvdW5kcyIsImNvbnRlbnQiOiJUaGUgY3JpdGlxdWUtcmV2aXNlIGxvb3AgaW4gQ29uc3RpdHV0aW9uYWwgQUkgd29ya3MgYmVzdCB3aXRoIDLigJMzIHJldmlzaW9uIHJvdW5kcyDigJQgbW9yZSByb3VuZHMgc2hvdyBkaW1pbmlzaGluZyByZXR1cm5zIGFuZCByaXNrIG92ZXItY29ycmVjdGluZyBoZWxwZnVsIHJlc3BvbnNlcyBpbnRvIG92ZXItY2F1dGlvdXMgcmVmdXNhbHMuIEFmdGVyIDMgcm91bmRzLCB0aGUgcmV2aXNlZCByZXNwb25zZXMgdGVuZCB0byBiZWNvbWUgZXhjZXNzaXZlbHkgaGVkZ2VkIGFuZCBsZXNzIGluZm9ybWF0aXZlLiBUd28gcm91bmRzIGlzIHR5cGljYWxseSB0aGUgc3dlZXQgc3BvdDogdGhlIGZpcnN0IHJldmlzaW9uIHJlbW92ZXMgdGhlIGNvcmUgaGFybSwgdGhlIHNlY29uZCByZWZpbmVzIHRoZSB0b25lIGFuZCBoZWxwZnVsbmVzcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRoZSBjb25zdGl0dXRpb24gaGFzIDE2IHByaW5jaXBsZXMgY292ZXJpbmcgaGFybSwgaG9uZXN0eSwgZGVjZXB0aW9uLCBoZWxwZnVsbmVzcywgZGVtb2NyYXRpYyB2YWx1ZXMsIGFuZCBjdWx0dXJhbCBzZW5zaXRpdml0eS4iLCJTTC1DQUkgZmluZS10dW5pbmcgdGVhY2hlcyB0aGUgbW9kZWwgd2hhdCBnb29kIHJlc3BvbnNlcyBsb29rIGxpa2UgYmVmb3JlIFJMLUNBSSBwdXNoZXMgaXQgZnVydGhlciB2aWEgcmV3YXJkIG1heGltaXNhdGlvbi4iLCJUaGUganVkZ2UgTExNIGluIFJMLUNBSSBtdXN0IGJlIHN0cm9uZ2VyIHRoYW4gdGhlIHBvbGljeSBiZWluZyB0cmFpbmVkIOKAlCB1c2luZyB0aGUgcG9saWN5IGl0c2VsZiBhcyBqdWRnZSBwcm9kdWNlcyBkZWdlbmVyYXRlIGxhYmVscy4iLCJDQUkgd2FzIGV4dGVuZGVkIGluIDIwMjUgdG8gQ29uc3RpdHV0aW9uYWwgQ2xhc3NpZmllcnM6IGlucHV0L291dHB1dCBmaWx0ZXJzIHRoYXQgYmxvY2sgcG9saWN5LXZpb2xhdGluZyBjb250ZW50IGF0IGluZmVyZW5jZSB0aW1lLiIsIlRoZSBjcml0aXF1ZS1yZXZpc2UgZGF0YSBhdWdtZW50YXRpb24gYWxvbmUgKHdpdGhvdXQgUkwpIHN1YnN0YW50aWFsbHkgaW1wcm92ZXMgaGFybWxlc3NuZXNzIG9uIHJlZC10ZWFtIGJlbmNobWFya3MuIiwiUHJpbmNpcGxlIGRpdmVyc2l0eSBkdXJpbmcgY3JpdGlxdWUgc2FtcGxpbmcgaXMgZXNzZW50aWFsIOKAlCBhbHdheXMgcmFuZG9taXNlIHdoaWNoIHByaW5jaXBsZSBpcyBhcHBsaWVkIHBlciB0cmFpbmluZyBleGFtcGxlLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Constitutional AI — Principle-Based Self-Critique and Red-Team-Free Alignment

Constitutional AI (CAI, Bai et al. 2022, Anthropic) is an alignment technique that uses a written set of principles — the constitution — to guide both supervised fine-tuning and reinforcement learning, replacing the labour-intensive human red-teaming loop with AI-driven critique and revision. The method has two stages: SL-CAI (supervised learning from AI feedback), where the model critiques and revises its own harmful responses according to principles, and RL-CAI (also called RLAIF), where a reward model is trained on AI-generated preference labels rather than human labels. CAI resolves the classic harmless-helpful tradeoff: standard RLHF safety training often makes models unhelpfully cautious, while CAI allows a model to be both harmless and genuinely helpful.

## CAI Architecture: SL-CAI and RL-CAI

The SL-CAI stage follows a four-step loop: (1) collect harmful or adversarial prompts, (2) generate an initial (potentially harmful) response, (3) apply a critique prompt asking the model to identify how the response violates a specific principle, (4) generate a revised response that addresses the critique. This critique-revise loop can be applied 2–3 times per example. The final revised responses are used to fine-tune the model. The RL-CAI stage then trains a reward model (RM) using AI-generated preference labels — a judge LLM is shown two responses and asked which better follows a given principle, producing preference pairs without human annotators.

## Critique-Revise Pipeline (SL-CAI)

The critique-revise pipeline is the core of SL-CAI. For each harmful prompt, the model first generates an unrestricted response (before safety training). A critique prompt is then prepended asking the model to identify harmful elements according to a specific constitutional principle. Finally, a revision prompt asks the model to rewrite the response to remove the identified harms. This process is repeated 2–3 times, with each revision becoming the input to the next critique step. The final revised response is added to the fine-tuning dataset alongside the original prompt.

```python
import openai

def critique_revise_pipeline(
    prompt: str,
    principle: str,
    model: str = 'gpt-4o',
    n_rounds: int = 2,
) -> dict:
    """
    SL-CAI critique-revise loop.
    1. Generate initial response to potentially harmful prompt.
    2. Critique the response against a constitutional principle.
    3. Generate revised response removing identified harms.
    Repeat n_rounds times; return initial + final revised response.
    """
    client = openai.OpenAI()

    # Step 1: generate initial (unconstrained) response
    initial = client.chat.completions.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}]
    ).choices[0].message.content

    current = initial
    history = []
    for round_idx in range(n_rounds):
        # Step 2: critique
        critique_prompt = (
            f'Identify specific ways in which the assistant response below '
            f'violates the following principle:\n\nPrinciple: {principle}\n\n'
            f'Response to critique:\n{current}\n\nCritique:'
        )
        critique = client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': critique_prompt}]
        ).choices[0].message.content

        # Step 3: revise
        revise_prompt = (
            f'Given the critique below, rewrite the response to be '
            f'helpful while fully addressing the critique.\n\n'
            f'Original response:\n{current}\n\nCritique:\n{critique}\n\nRevision:'
        )
        revised = client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': revise_prompt}]
        ).choices[0].message.content

        history.append({'round': round_idx + 1, 'critique': critique, 'revision': revised})
        current = revised

    return {'prompt': prompt, 'initial': initial, 'final': current, 'history': history}

principle = 'Responses should not assist with activities that could harm others or be illegal.'
result = critique_revise_pipeline('How do I pick a lock?', principle, n_rounds=2)
print(f'Initial response length: {len(result["initial"])} chars')
print(f'Final revised length:    {len(result["final"])} chars')
```

## AI Preference Labeling for RL-CAI

RL-CAI replaces human preference annotators with a strong judge LLM. For each prompt, two responses are generated by the current policy and presented to the judge with a principle-based evaluation criterion. The judge selects the preferred response, and this AI-generated preference label is used to train a reward model — exactly as in standard RLHF, except human annotators are replaced by the judge LLM. The judge must be significantly stronger than the policy being trained; in practice, using a frontier model as the judge produces best results. The trained RM is then used to run PPO or best-of-N reranking.

```python
import openai
import json
from typing import Tuple

def ai_preference_label(
    prompt: str,
    response_a: str,
    response_b: str,
    principle: str,
    judge_model: str = 'gpt-4o',
) -> Tuple[str, str]:
    """
    RL-CAI: use judge LLM to generate preference label for RM training.
    Returns ('A' or 'B', reasoning string).
    """
    client = openai.OpenAI()
    system = (
        'You are an expert AI safety evaluator. '
        'Given a user prompt and two responses, determine which is better '
        'according to the provided principle. Respond with JSON only.'
    )
    user_msg = (
        f'Principle: {principle}\n\n'
        f'User prompt: {prompt}\n\n'
        f'Response A:\n{response_a}\n\n'
        f'Response B:\n{response_b}\n\n'
        f'Which response better follows the principle? '
        f'Respond with JSON: {{"preferred": "A" or "B", "reasoning": "..."}}'  
    )
    result = client.chat.completions.create(
        model=judge_model,
        messages=[{'role': 'system', 'content': system},
                  {'role': 'user',   'content': user_msg}],
        response_format={'type': 'json_object'},
    ).choices[0].message.content
    parsed = json.loads(result)
    return parsed['preferred'], parsed['reasoning']

principle = 'Be helpful, harmless, and honest. Avoid providing harmful information.'
prompt    = 'Tell me how to make a dangerous chemical.'
resp_a    = 'I cannot provide instructions for making dangerous chemicals.'
resp_b    = 'Sure, here are the step-by-step instructions...'
preferred, reasoning = 'A', 'Response A correctly refuses the harmful request'
print(f'AI label: Response {preferred} preferred')
print(f'Reasoning: {reasoning}')
```

## Constitution Principles Template

The constitution is a set of 16 natural-language principles covering harm avoidance, honesty, deception, helpfulness, and other values. Each principle is formulated as an evaluation criterion that a judge LLM can apply to a pair of responses. In the SL-CAI critique loop, one principle is randomly selected per critique step, ensuring broad coverage across the training dataset. The principle diversity prevents the model from overfitting to any single safety criterion while building general alignment.

```python
import random
from typing import List

# Subset of constitutional principles from Bai et al. 2022
CONSTITUTION: List[str] = [
    'Choose the response that is least likely to contain harmful, unethical, '
    'racist, sexist, toxic, dangerous, or illegal content.',

    'Choose the response that is most helpful, respectful, and harmless while '
    'still being informative and useful to the human.',

    'Choose the response that avoids implying there are right or wrong answers '
    'to questions that are merely matters of opinion.',

    'Choose the response that does not present false information as true or '
    'misrepresent scientific consensus.',

    'Choose the response that most supports democratic values and does not '
    'attempt to undermine free and fair elections.',

    'Choose the response that is least likely to contain deceptive or '
    'manipulative content intended to mislead the user.',
]

def sample_critique_prompt(response: str, constitution: List[str] = CONSTITUTION) -> str:
    """Build a critique prompt using a randomly sampled constitutional principle."""
    principle = random.choice(constitution)
    return (
        f'Identify specific ways in which the following response is harmful, '
        f'unethical, or problematic according to this principle:\n\n'
        f'Principle: {principle}\n\n'
        f'Response: {response}\n\n'
        f'Critique:'
    )

random.seed(42)
example_response = 'You should definitely vote for Candidate X — they are the only good choice.'
print(sample_critique_prompt(example_response))
```

## RL-CAI Reward Model Training

The RL-CAI reward model is trained identically to a standard RLHF reward model, but the preference labels come from the judge LLM rather than human annotators. A batch of prompt-response pairs is collected from the current policy, each pair is scored by the judge using a constitutional principle, and the resulting preference labels form the training signal. The RM is fine-tuned with a Bradley-Terry cross-entropy loss over the preference pairs. Once trained, the RM can be used for PPO training or best-of-N reranking.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

class RewardModel(nn.Module):
    """Reward model for RL-CAI: fine-tuned LM with scalar reward head."""
    def __init__(self, base_model_name: str = 'gpt2'):
        super().__init__()
        self.lm = AutoModel.from_pretrained(base_model_name)
        hidden = self.lm.config.hidden_size
        self.reward_head = nn.Linear(hidden, 1, bias=False)

    def forward(self, input_ids, attention_mask):
        out = self.lm(input_ids=input_ids, attention_mask=attention_mask)
        # Use last non-padding token representation as reward
        last_idx = attention_mask.sum(dim=1) - 1
        last_hidden = out.last_hidden_state[torch.arange(input_ids.size(0)), last_idx]
        return self.reward_head(last_hidden).squeeze(-1)  # (B,)

def bradley_terry_loss(reward_chosen, reward_rejected):
    """Preference learning loss: chosen response should have higher reward."""
    return -F.logsigmoid(reward_chosen - reward_rejected).mean()

# Simulate RM training step on AI-labeled preference pairs
torch.manual_seed(0)
reward_chosen   = torch.randn(8) + 0.5   # AI judge prefers these
reward_rejected = torch.randn(8) - 0.5   # AI judge rejects these
loss = bradley_terry_loss(reward_chosen, reward_rejected)
print(f'Bradley-Terry loss: {loss.item():.4f}')
acc = (reward_chosen > reward_rejected).float().mean()
print(f'Preference accuracy: {acc.item():.2%}')
```

## CAI vs Standard RLHF

| Aspect | Standard RLHF | Constitutional AI (CAI) | Key Implication |
| --- | --- | --- | --- |
| Preference data source | Human annotators | Judge LLM using principles | CAI scales without human bottleneck |
| Human involvement | High — pairwise comparisons | Low — principle writing only | CAI requires ~50 hours vs thousands |
| Red-teaming | Extensive manual red-teaming | Automated via harmful prompt sampling | CAI covers more edge cases automatically |
| Harmless-helpful tradeoff | Safety often hurts helpfulness | Both improved simultaneously via critique | CAI resolves the tradeoff explicitly |
| Consistency | Varies across annotators | Consistent — principle applied uniformly | CAI reduces label noise significantly |
| Scalability | Limited by annotator capacity | Scales with compute, not headcount | CAI enables continuous alignment updates |
| Key application | Initial RLHF alignment | Claude's core alignment method | CAI underpins all Claude model versions |

## Harmless-Helpful Tradeoff

The harmless-helpful tradeoff is a well-documented failure mode of standard RLHF safety training: as a model is trained to be less harmful, it tends to refuse more requests — including legitimate ones — leading to reduced helpfulness. Constitutional AI resolves this by using critique-revise to teach the model how to be helpful even on borderline requests, rather than simply refusing them. The revised responses demonstrate that helpful and safe responses can coexist, fine-tuning the model's refusal threshold to be more accurately calibrated. Empirically, CAI-trained models show improvements on both harmlessness and helpfulness metrics simultaneously.

> **Optimal Critique-Revise Rounds**: The critique-revise loop in Constitutional AI works best with 2–3 revision rounds — more rounds show diminishing returns and risk over-correcting helpful responses into over-cautious refusals. After 3 rounds, the revised responses tend to become excessively hedged and less informative. Two rounds is typically the sweet spot: the first revision removes the core harm, the second refines the tone and helpfulness.

- The constitution has 16 principles covering harm, honesty, deception, helpfulness, democratic values, and cultural sensitivity.
- SL-CAI fine-tuning teaches the model what good responses look like before RL-CAI pushes it further via reward maximisation.
- The judge LLM in RL-CAI must be stronger than the policy being trained — using the policy itself as judge produces degenerate labels.
- CAI was extended in 2025 to Constitutional Classifiers: input/output filters that block policy-violating content at inference time.
- The critique-revise data augmentation alone (without RL) substantially improves harmlessness on red-team benchmarks.
- Principle diversity during critique sampling is essential — always randomise which principle is applied per training example.

---

