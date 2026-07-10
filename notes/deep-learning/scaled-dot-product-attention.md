---
title: "Scaled Dot-Product Attention — Derivation and Numerical Stability"
slug: "scaled-dot-product-attention"
description: "Derive Attention(Q,K,V)=softmax(QKᵀ/√dₖ)V from first principles, prove why √dₖ scaling prevents softmax saturation, and explore O(n²d) complexity and FlashAttention tiling."
tags: ["deep-learning", "transformers", "attention"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2NhbGVkIGRvdC1wcm9kdWN0IGF0dGVudGlvbiBpcyB0aGUgY29tcHV0YXRpb25hbCBjb3JlIG9mIGV2ZXJ5IFRyYW5zZm9ybWVyLiBHaXZlbiBxdWVyaWVzIFEsIGtleXMgSywgYW5kIHZhbHVlcyBWIGl0IGNvbXB1dGVzIGEgd2VpZ2h0ZWQgc3VtIG9mIHZhbHVlIHZlY3RvcnMgd2hlcmUgdGhlIHdlaWdodHMgYXJlIGRldGVybWluZWQgYnkgcXVlcnkta2V5IHNpbWlsYXJpdHk6IEF0dGVudGlvbihRLEssVikgPSBzb2Z0bWF4KFFL4bWAL+KImmTigpYpVi4gVGhyZWUgZGVzaWduIGNob2ljZXMg4oCUIGRvdC1wcm9kdWN0IHNjb3JpbmcsIOKImmTigpYgc2NhbGluZywgYW5kIHNvZnRtYXggbm9ybWFsaXNhdGlvbiDigJQgZWFjaCBoYXZlIHByZWNpc2UgbWF0aGVtYXRpY2FsIG1vdGl2YXRpb25zIHRoYXQgYXJlIGVhc3kgdG8gbWlzcyB3aGVuIHJlYWRpbmcgb25seSB0aGUgZm9ybXVsYS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYXRoZW1hdGljYWwgRGVmaW5pdGlvbiBhbmQgVGVuc29yIFNoYXBlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUXVlcmllcyBRIOKIiCDihJ1ee25xw5dk4oKWfSByZXByZXNlbnQgbnEgcG9zaXRpb25zIGFza2luZyBmb3IgaW5mb3JtYXRpb24uIEtleXMgSyDiiIgg4oSdXntua8OXZOKCln0gcmVwcmVzZW50IG5rIHBvc2l0aW9ucyBhZHZlcnRpc2luZyB3aGF0IHRoZXkgY29udGFpbi4gVmFsdWVzIFYg4oiIIOKEnV57bmvDl2R2fSBjYXJyeSB0aGUgYWN0dWFsIGNvbnRlbnQgdG8gYmUgcmV0cmlldmVkLiBUaGUgc2NvcmUgbWF0cml4IFMgPSBRS+G1gC/iiJpk4oKWIOKIiCDihJ1ee25xw5dua30gbWVhc3VyZXMgcGFpcndpc2UgY29tcGF0aWJpbGl0eSDigJQgZW50cnkgU+G1ouKxvCA9IHHhtaLCt2visbwv4oiaZOKCliBpcyBob3cgcmVsZXZhbnQga2V5IGogaXMgdG8gcXVlcnkgaS4gQXBwbHlpbmcgcm93LXdpc2Ugc29mdG1heCBnaXZlcyBhdHRlbnRpb24gd2VpZ2h0cyBBID0gc29mdG1heChTKSDiiIgg4oSdXntuccOXbmt9IHdpdGggcm93cyBzdW1taW5nIHRvIG9uZS4gVGhlIG91dHB1dCBPID0gQVYg4oiIIOKEnV57bnHDl2R2fSBpcyBhIGNvbnZleCBjb21iaW5hdGlvbiBvZiB2YWx1ZSB2ZWN0b3JzIGZvciBlYWNoIHF1ZXJ5LiJ9LHsidHlwZSI6Im1hdGgiLCJjb250ZW50IjoiXFx0ZXh0e0F0dGVudGlvbn0oUSxLLFYpID0gXFx0ZXh0e3NvZnRtYXh9XFwhXFxsZWZ0KFxcZnJhY3tRS15cXHRvcH17XFxzcXJ0e2Rfa319XFxyaWdodClWIiwiZGlzcGxheSI6dHJ1ZX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIOKImmTigpYgU2NhbGluZyBGYWN0b3Ig4oCUIERlcml2YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN1cHBvc2UgUSBhbmQgSyBoYXZlIGluZGVwZW5kZW50IGVudHJpZXMgZHJhd24gZnJvbSBOKDAsMSkuIFRoZSBkb3QgcHJvZHVjdCBx4bWiwrdr4rG8ID0gzqPigpcgceG1ouKCl2visbzigpcgaXMgYSBzdW0gb2YgZOKCliBpbmRlcGVuZGVudCB0ZXJtcyBlYWNoIHdpdGggbWVhbiAwIGFuZCB2YXJpYW5jZSAxLCBzbyBx4bWiwrdr4rG8IH4gTigwLCBk4oKWKS4gVGhlIHN0YW5kYXJkIGRldmlhdGlvbiBpcyDiiJpk4oKWIOKAlCBmb3IgZOKClj02NCB0aGlzIGlzIDgsIG1lYW5pbmcgcmF3IHNjb3JlcyBzcGFuIHJvdWdobHkgwrEyNC4gVGhlIHNvZnRtYXggZXhwKHgpL86jZXhwIHB1c2hlcyB2YWx1ZXMgaW4gaXRzIGZsYXQgc2F0dXJhdGlvbiByZWdpb24gd2hlbiB8eHwgaXMgbGFyZ2U6IGFsbCBwcm9iYWJpbGl0eSBtYXNzIGNvbGxhcHNlcyBvbnRvIHRoZSBtYXhpbXVtLXNjb3Jpbmcga2V5LiBEaXZpZGluZyBieSDiiJpk4oKWIHJlc3RvcmVzIHVuaXQgdmFyaWFuY2UsIGtlZXBpbmcgc2NvcmVzIGluIHRoZSByZWdpbWUgd2hlcmUgc29mdG1heCBkaXN0cmlidXRlcyBtYXNzIGFjcm9zcyBtdWx0aXBsZSBrZXlzIGFuZCBpdHMgSmFjb2JpYW4gcmV0YWlucyBub24tbmVnbGlnaWJsZSBlbnRyaWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgc2RwX2F0dGVudGlvbl9udW1weShRLCBLLCBWLCBtYXNrPU5vbmUpOlxuICAgICMgUTogKG5xLCBkayksIEs6IChuaywgZGspLCBWOiAobmssIGR2KVxuICAgICMgUmV0dXJuczogb3V0cHV0IChucSwgZHYpLCB3ZWlnaHRzIChucSwgbmspXG4gICAgZGsgPSBRLnNoYXBlWy0xXVxuICAgIHNjb3JlcyA9IFEgQCBLLlQgLyBucC5zcXJ0KGRrKVxuICAgIGlmIG1hc2sgaXMgbm90IE5vbmU6XG4gICAgICAgIHNjb3JlcyA9IHNjb3JlcyArIG1hc2sgKiAtMWU5XG4gICAgc2NvcmVzID0gc2NvcmVzIC0gc2NvcmVzLm1heChheGlzPS0xLCBrZWVwZGltcz1UcnVlKSAgIyBudW1lcmljIHN0YWJpbGl0eVxuICAgIHdlaWdodHMgPSBucC5leHAoc2NvcmVzKVxuICAgIHdlaWdodHMgPSB3ZWlnaHRzIC8gd2VpZ2h0cy5zdW0oYXhpcz0tMSwga2VlcGRpbXM9VHJ1ZSlcbiAgICByZXR1cm4gd2VpZ2h0cyBAIFYsIHdlaWdodHNcblxuZGVmIHNkcF9hdHRlbnRpb25fdG9yY2goUSwgSywgVik6XG4gICAgZGsgPSBRLnNoYXBlWy0xXVxuICAgIHNjb3JlcyA9IFEgQCBLLnRyYW5zcG9zZSgtMiwgLTEpIC8gZGsgKiogMC41XG4gICAgd2VpZ2h0cyA9IEYuc29mdG1heChzY29yZXMsIGRpbT0tMSlcbiAgICByZXR1cm4gd2VpZ2h0cyBAIFYsIHdlaWdodHNcblxubnAucmFuZG9tLnNlZWQoNDIpXG5ucSwgbmssIGRrLCBkdiA9IDUsIDcsIDY0LCA2NFxuUSA9IG5wLnJhbmRvbS5yYW5kbihucSwgZGspLmFzdHlwZShucC5mbG9hdDMyKVxuSyA9IG5wLnJhbmRvbS5yYW5kbihuaywgZGspLmFzdHlwZShucC5mbG9hdDMyKVxuViA9IG5wLnJhbmRvbS5yYW5kbihuaywgZHYpLmFzdHlwZShucC5mbG9hdDMyKVxub3V0X25wLCB3X25wID0gc2RwX2F0dGVudGlvbl9udW1weShRLCBLLCBWKVxuUXQgPSB0b3JjaC50ZW5zb3IoUSk7IEt0ID0gdG9yY2gudGVuc29yKEspOyBWdCA9IHRvcmNoLnRlbnNvcihWKVxub3V0X3B0LCB3X3B0ID0gc2RwX2F0dGVudGlvbl90b3JjaChRdCwgS3QsIFZ0KVxucHJpbnQoXHUwMDI3T3V0cHV0IHNoYXBlOlx1MDAyNywgb3V0X25wLnNoYXBlKVxucHJpbnQoXHUwMDI3V2VpZ2h0cyByb3ctc3VtOlx1MDAyNywgd19ucC5zdW0oYXhpcz0xKS5yb3VuZCg1KSlcbnByaW50KFx1MDAyN01heCBkaWZmIE51bVB5IHZzIFB5VG9yY2g6XHUwMDI3LCBucC5hYnMob3V0X25wIC0gb3V0X3B0Lm51bXB5KCkpLm1heCgpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNvZnRtYXggU2F0dXJhdGlvbiBhbmQgR3JhZGllbnQgRmxvdyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHNvZnRtYXggSmFjb2JpYW4g4oiCz4Mv4oiCeiA9IGRpYWcoz4MpIOKIkiDPg8+D4bWAIGhhcyBlbnRyaWVzIGJvdW5kZWQgYnkgz4PhtaIoMeKIks+D4bWiKS4gV2hlbiBzb2Z0bWF4IGFwcHJvYWNoZXMgYSBvbmUtaG90IHZlY3RvciAoZHVlIHRvIGxhcmdlIHVuc2NhbGVkIHNjb3JlcyksIGFsbCBlbnRyaWVzIM+D4bWiKDHiiJLPg+G1oikgY29sbGFwc2UgdG93YXJkIHplcm8gYW5kIHRoZSBGcm9iZW5pdXMgbm9ybSBvZiB0aGUgSmFjb2JpYW4gdmFuaXNoZXMg4oCUIGJsb2NraW5nIGdyYWRpZW50IGZsb3cgZHVyaW5nIGJhY2twcm9wYWdhdGlvbi4gV2l0aCDiiJpk4oKWIHNjYWxpbmcgdGhlIHNjb3JlIGRpc3RyaWJ1dGlvbiByZW1haW5zIGFwcHJveGltYXRlbHkgTigwLDEpIHJlZ2FyZGxlc3Mgb2YgZOKCliwga2VlcGluZyB0aGUgSmFjb2JpYW4gbm9ybSBzdGFibGUgYWNyb3NzIGFsbCBtb2RlbCBzaXplcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBzb2Z0bWF4KHgpOlxuICAgIGUgPSBucC5leHAoeCAtIHgubWF4KCkpXG4gICAgcmV0dXJuIGUgLyBlLnN1bSgpXG5cbmRlZiBqYWNvYmlhbl9mcm9iX25vcm0ocyk6XG4gICAgIyBGcm9iZW5pdXMgbm9ybSBvZiBzb2Z0bWF4IEphY29iaWFuOiBkaWFnKHMpIC0gcypzXlRcbiAgICByZXR1cm4gbnAuc3FydChucC5zdW0oKG5wLmRpYWcocykgLSBucC5vdXRlcihzLCBzKSkgKiogMikpXG5cbnByaW50KFx1MDAyN3s6XHUwMDNlNX0gfCB7Olx1MDAzZTl9IHwgezpcdTAwM2UxMX0gfCB7Olx1MDAzZTE0fSB8IHs6XHUwMDNlMTJ9XHUwMDI3LmZvcm1hdChcbiAgICBcdTAwMjdka1x1MDAyNywgXHUwMDI3ZG90X3N0ZFx1MDAyNywgXHUwMDI3c2NhbGVkX3N0ZFx1MDAyNywgXHUwMDI3Sl91bnNjYWxlZFx1MDAyNywgXHUwMDI3Sl9zY2FsZWRcdTAwMjcpKVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDYwKVxubnAucmFuZG9tLnNlZWQoMClcbmZvciBkayBpbiBbMSwgNCwgMTYsIDY0LCAyNTYsIDEwMjRdOlxuICAgIHEgPSBucC5yYW5kb20ucmFuZG4oZGspXG4gICAga2V5cyA9IG5wLnJhbmRvbS5yYW5kbig2LCBkaylcbiAgICBkb3RzID0ga2V5cyBAIHEgICAgICAgICAgICAgICAgICAgICMgfiBOKDAsIGRrKVxuICAgIHNjYWxlZCA9IGRvdHMgLyBucC5zcXJ0KGRrKSAgICAgICAgIyB+IE4oMCwgMSlcbiAgICBqbl91ID0gamFjb2JpYW5fZnJvYl9ub3JtKHNvZnRtYXgoZG90cykpXG4gICAgam5fcyA9IGphY29iaWFuX2Zyb2Jfbm9ybShzb2Z0bWF4KHNjYWxlZCkpXG4gICAgcHJpbnQoXHUwMDI3ezpcdTAwM2U1fSB8IHs6XHUwMDNlOS4zZn0gfCB7Olx1MDAzZTExLjNmfSB8IHs6XHUwMDNlMTQuNmZ9IHwgezpcdTAwM2UxMi42Zn1cdTAwMjcuZm9ybWF0KFxuICAgICAgICBkaywgZG90cy5zdGQoKSwgc2NhbGVkLnN0ZCgpLCBqbl91LCBqbl9zKSlcbnByaW50KFx1MDAyN1Vuc2NhbGVkIEphY29iaWFuIG5vcm0gY29sbGFwc2VzIGFzIGRrIGdyb3dzIC1cdTAwM2UgdmFuaXNoaW5nIGdyYWRpZW50cy5cdTAwMjcpXG5wcmludChcdTAwMjdTY2FsZWQgbm9ybSBzdGF5cyBuZWFyIGNvbnN0YW50IC1cdTAwM2Ugc3RhYmxlIGdyYWRpZW50IGZsb3cuXHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJOdW1lcmljYWwgU3RhYmlsaXR5IGluIEltcGxlbWVudGF0aW9uIiwiY29udGVudCI6IkFsd2F5cyBzdWJ0cmFjdCB0aGUgcm93IG1heGltdW0gYmVmb3JlIGNvbXB1dGluZyBleHA6IHNjb3JlcyAtPSBzY29yZXMubWF4KC0xLCBrZWVwZGltcz1UcnVlKS4gVGhpcyBwcmV2ZW50cyBvdmVyZmxvdyB3aXRob3V0IGNoYW5naW5nIHRoZSByZXN1bHQgc2luY2UgZXhwKHgtYykvzqNleHAoeC1jKSA9IGV4cCh4KS/Oo2V4cCh4KS4gUHlUb3JjaCBGLnNvZnRtYXggaGFuZGxlcyB0aGlzIGludGVybmFsbHkuIEZvciBjdXN0b20gQ1VEQSBrZXJuZWxzIHRoaXMgc3RlcCBpcyBub24tbmVnb3RpYWJsZSDigJQgYSBzaW5nbGUgaW5mIHByb2R1Y2VkIGJ5IGV4cCBydWlucyB0aGUgZW50aXJlIHJvdy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBdHRlbnRpb24gUGF0dGVybiBWaXN1YWxpc2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgYXR0ZW50aW9uIHdlaWdodCBtYXRyaXggQSDiiIgg4oSdXntuccOXbmt9IGlzIGludGVycHJldGFibGUgYXMgYSBzb2Z0IHJvdXRpbmcgbWFwOiBlbnRyeSBB4bWi4rG8IGlzIHRoZSBmcmFjdGlvbiBvZiB2YWx1ZS12ZWN0b3IgaiBhZ2dyZWdhdGVkIGludG8gb3V0cHV0IHBvc2l0aW9uIGkuIFZpc3VhbGlzaW5nIEEgYXMgYSBoZWF0bWFwIHJldmVhbHMgd2hpY2gga2V5IHBvc2l0aW9ucyBlYWNoIHF1ZXJ5IHJlbGllcyBvbi4gSGlnaC1lbnRyb3B5IHJvd3MgKGRpZmZ1c2UgYXR0ZW50aW9uKSBpbmRpY2F0ZSBnZW5lcmFsIGluZm9ybWF0aW9uIGdhdGhlcmluZzsgbG93LWVudHJvcHkgcm93cyAocGVha2VkIGF0dGVudGlvbikgaW5kaWNhdGUgc3BlY2lmaWMgcmV0cmlldmFsLiBJbiBsYW5ndWFnZSBtb2RlbHMsIHBhdHRlcm5zIGxpa2UgZGlhZ29uYWwgY29uY2VudHJhdGlvbiAobG9jYWwgYXR0ZW50aW9uKSwgY29sdW1uIGNvbmNlbnRyYXRpb24gKGF0dGVuZGluZyB0byBhIHNwZWNpYWwgdG9rZW4pLCBhbmQgYmxvY2sgc3RydWN0dXJlIChwaHJhc2UtbGV2ZWwgZ3JvdXBpbmcpIGVhY2ggcmVmbGVjdCBkaWZmZXJlbnQgbGluZ3Vpc3RpYyBiZWhhdmlvdXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHNkcF9hdHRlbnRpb24oUSwgSywgVik6XG4gICAgZGsgPSBRLnNoYXBlWy0xXVxuICAgIFMgPSBRIEAgSy5UIC8gbnAuc3FydChkaylcbiAgICBTIC09IFMubWF4KGF4aXM9LTEsIGtlZXBkaW1zPVRydWUpXG4gICAgQSA9IG5wLmV4cChTKTsgQSAvPSBBLnN1bShheGlzPS0xLCBrZWVwZGltcz1UcnVlKVxuICAgIHJldHVybiBBIEAgViwgQVxuXG5kZWYgcHJpbnRfaGVhdG1hcChBLCByb3dfbGFiZWxzLCBjb2xfbGFiZWxzKTpcbiAgICBjb2xfdyA9IG1heChsZW4oYykgZm9yIGMgaW4gY29sX2xhYmVscykgKyAxXG4gICAgaGVhZGVyID0gXHUwMDI3ezpcdTAwM2UxMH1cdTAwMjcuZm9ybWF0KFx1MDAyN1x1MDAyNykgKyBcdTAwMjdcdTAwMjcuam9pbihcdTAwMjd7Olx1MDAzZXt3fX1cdTAwMjcuZm9ybWF0KGMsIHc9Y29sX3cpIGZvciBjIGluIGNvbF9sYWJlbHMpXG4gICAgcHJpbnQoaGVhZGVyKVxuICAgIHByaW50KFx1MDAyNy1cdTAwMjcgKiBsZW4oaGVhZGVyKSlcbiAgICBmb3IgcmwsIHJvdyBpbiB6aXAocm93X2xhYmVscywgQSk6XG4gICAgICAgIGNlbGxzID0gXHUwMDI3XHUwMDI3LmpvaW4oXG4gICAgICAgICAgICBcdTAwMjd7Olx1MDAzZXt3fX1cdTAwMjcuZm9ybWF0KFx1MDAyNysrXHUwMDI3IGlmIHcgXHUwMDNlIDAuMyBlbHNlIFx1MDAyNytcdTAwMjcgaWYgdyBcdTAwM2UgMC4xIGVsc2UgXHUwMDI3Llx1MDAyNywgdz1jb2xfdylcbiAgICAgICAgICAgIGZvciB3IGluIHJvdylcbiAgICAgICAgcHJpbnQoXHUwMDI3ezpcdTAwM2UxMH17fVx1MDAyNy5mb3JtYXQocmxbOjEwXSwgY2VsbHMpICsgXHUwMDI3ICBwZWFrLVx1MDAzZVx1MDAyNyArIGNvbF9sYWJlbHNbcm93LmFyZ21heCgpXSlcblxubnAucmFuZG9tLnNlZWQoOTkpXG50b2tlbnMgPSBbXHUwMDI3VGhlXHUwMDI3LCBcdTAwMjdjYXRcdTAwMjcsIFx1MDAyN3NhdFx1MDAyNywgXHUwMDI3b25cdTAwMjcsIFx1MDAyN3RoZVx1MDAyNywgXHUwMDI3bWF0XHUwMDI3XVxuZGssIGR2ID0gMzIsIDMyXG5RID0gbnAucmFuZG9tLnJhbmRuKGxlbih0b2tlbnMpLCBkaylcbksgPSBucC5yYW5kb20ucmFuZG4obGVuKHRva2VucyksIGRrKVxuViA9IG5wLnJhbmRvbS5yYW5kbihsZW4odG9rZW5zKSwgZHYpXG5fLCBBID0gc2RwX2F0dGVudGlvbihRLCBLLCBWKVxucHJpbnRfaGVhdG1hcChBLCB0b2tlbnMsIHRva2VucylcbmVudHJvcHkgPSAtKEEgKiBucC5sb2coQSArIDFlLTkpKS5zdW0oYXhpcz0xKVxucHJpbnQoXHUwMDI3QXR0ZW50aW9uIGVudHJvcHkgcGVyIHRva2VuIChuYXRzKTpcdTAwMjcsIGVudHJvcHkucm91bmQoMykpXG5wcmludChcdTAwMjdVbmlmb3JtIGVudHJvcHkgd291bGQgYmU6IHs6LjNmfVx1MDAyNy5mb3JtYXQobnAubG9nKGxlbih0b2tlbnMpKSkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcHV0YXRpb25hbCBDb21wbGV4aXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdHRlbnRpb24gaGFzIHRocmVlIHN0YWdlczogc2NvcmUgY29tcHV0YXRpb24gUUvhtYAgY29zdHMgTyhuccK3bmvCt2TigpYpLCBzb2Z0bWF4IGNvc3RzIE8obnHCt25rKSwgYW5kIHZhbHVlIGFnZ3JlZ2F0aW9uIEFWIGNvc3RzIE8obnHCt25rwrdkdikuIFRvdGFsOiBPKG5xwrdua8K3KGTigpYrZHYpKS4gRm9yIHNlbGYtYXR0ZW50aW9uIG5xPW5rPW4sIGdpdmluZyBPKG7CsmQpLiBUaGlzIHF1YWRyYXRpYyBkZXBlbmRlbmNlIG9uIHNlcXVlbmNlIGxlbmd0aCBpcyB0aGUgcHJpbWFyeSBzY2FsYWJpbGl0eSBib3R0bGVuZWNrOiBhIDTDlyBzZXF1ZW5jZSBsZW5ndGggaW5jcmVhc2UgY29zdHMgMTbDlyBpbiBjb21wdXRhdGlvbiBhbmQgMTbDlyBpbiBtZW1vcnkgZm9yIHRoZSBzY29yZSBtYXRyaXggUyDiiIgg4oSdXntuw5dufS4gVGhlIG1lbW9yeSBmb290cHJpbnQgaXMgbsKywrc0IGJ5dGVzIChmbG9hdDMyKTsgYXQgbj00MDk2IHdpdGggZOKClj02NCB0aGUgc2NvcmUgbWF0cml4IGFsb25lIGNvbnN1bWVzIDY0IE1CIHBlciBoZWFkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0aW1lXG5cbmRlZiBhdHRlbnRpb25fdGltZV9tcyhzZXFfbGVuLCBkaz02NCwgZHY9NjQsIG5fdHJpYWxzPTMpOlxuICAgIHJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZSg0MilcbiAgICB0aW1pbmdzID0gW11cbiAgICBmb3IgXyBpbiByYW5nZShuX3RyaWFscyk6XG4gICAgICAgIFEgPSBybmcucmFuZG4oc2VxX2xlbiwgZGspLmFzdHlwZShucC5mbG9hdDMyKVxuICAgICAgICBLID0gcm5nLnJhbmRuKHNlcV9sZW4sIGRrKS5hc3R5cGUobnAuZmxvYXQzMilcbiAgICAgICAgViA9IHJuZy5yYW5kbihzZXFfbGVuLCBkdikuYXN0eXBlKG5wLmZsb2F0MzIpXG4gICAgICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgICAgICBTID0gUSBAIEsuVCAvIG5wLnNxcnQoZGspICAgICAgICAgIyBPKG5eMiAqIGRrKVxuICAgICAgICBTIC09IFMubWF4KDEsIGtlZXBkaW1zPVRydWUpXG4gICAgICAgIEEgPSBucC5leHAoUyk7IEEgLz0gQS5zdW0oMSwga2VlcGRpbXM9VHJ1ZSlcbiAgICAgICAgXyA9IEEgQCBWICAgICAgICAgICAgICAgICAgICAgICAgICAjIE8obl4yICogZHYpXG4gICAgICAgIHRpbWluZ3MuYXBwZW5kKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MClcbiAgICByZXR1cm4gbnAubWVkaWFuKHRpbWluZ3MpICogMTAwMFxuXG5zZXFfbGVucyA9IFsxMjgsIDI1NiwgNTEyLCAxMDI0LCAyMDQ4XVxucHJpbnQoXHUwMDI3ezpcdTAwM2U2fSB7Olx1MDAzZTl9IHs6XHUwMDNlOH0gezpcdTAwM2UxMH0gezpcdTAwM2U4fVx1MDAyNy5mb3JtYXQoXHUwMDI3blx1MDAyNywgXHUwMDI3dGltZV9tc1x1MDAyNywgXHUwMDI3cmF0aW9cdTAwMjcsIFx1MDAyN25eMl9yYXRpb1x1MDAyNywgXHUwMDI3bWVtX01CXHUwMDI3KSlcbnByZXZfdCwgcHJldl9uID0gTm9uZSwgTm9uZVxuZm9yIG4gaW4gc2VxX2xlbnM6XG4gICAgdCA9IGF0dGVudGlvbl90aW1lX21zKG4pXG4gICAgcmF0aW8gPSB0IC8gcHJldl90IGlmIHByZXZfdCBlbHNlIDEuMFxuICAgIG4yciA9IChuIC8gcHJldl9uKSAqKiAyIGlmIHByZXZfbiBlbHNlIDEuMFxuICAgIG1lbSA9IG4gKiBuICogNCAvIDFlNlxuICAgIHByaW50KFx1MDAyN3s6XHUwMDNlNn0gezpcdTAwM2U5LjJmfSB7Olx1MDAzZTguMmZ9IHs6XHUwMDNlMTAuMmZ9IHs6XHUwMDNlOC4xZn1cdTAwMjcuZm9ybWF0KG4sIHQsIHJhdGlvLCBuMnIsIG1lbSkpXG4gICAgcHJldl90LCBwcmV2X24gPSB0LCBuXG5wcmludChcdTAwMjdUaW1lIHJhdGlvIHRyYWNrcyBuXjIgcmF0aW8gLVx1MDAzZSBPKG5eMipkKSBjb21wbGV4aXR5IGNvbmZpcm1lZC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXR0ZW50aW9uIGFzIFNvZnQgRGljdGlvbmFyeSBMb29rdXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF0dGVudGlvbiBnZW5lcmFsaXNlcyBhIGhhcmQga2V5LXZhbHVlIHN0b3JlLiBJbiBhIGhhcmQgbG9va3VwIGEgcXVlcnkgZXhhY3RseSBtYXRjaGVzIG9uZSBrZXkgYW5kIHJldHJpZXZlcyB0aGUgY29ycmVzcG9uZGluZyB2YWx1ZS4gSW4gc29mdCBhdHRlbnRpb24gdGhlIHF1ZXJ5IGNvbXB1dGVzIGEgc2ltaWxhcml0eSBzY29yZSB3aXRoIGV2ZXJ5IGtleSBhbmQgcmV0cmlldmVzIGEgZGlmZmVyZW50aWFibGUgd2VpZ2h0ZWQgYmxlbmQgb2YgYWxsIHZhbHVlcy4gVGhlIHNvZnRtYXggcGxheXMgdGhlIHJvbGUgb2YgYSBkaWZmZXJlbnRpYWJsZSBhcmdtYXgg4oCUIGFwcHJveGltYXRpbmcgZGlzY3JldGUgc2VsZWN0aW9uIHdoaWxlIHJlbWFpbmluZyBkaWZmZXJlbnRpYWJsZSB0aHJvdWdob3V0LiBUaGlzIGZyYW1pbmcgY2xhcmlmaWVzIHRoZSBkZXNpZ246IHF1ZXJpZXMgYXNrIHF1ZXN0aW9ucywga2V5cyBkZXNjcmliZSB3aGF0IGVhY2ggcG9zaXRpb24ga25vd3MgYWJvdXQgaXRzZWxmLCBhbmQgdmFsdWVzIGNhcnJ5IHRoZSBwYXlsb2FkIHRvIGJlIGFnZ3JlZ2F0ZWQuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkNvbXBvbmVudCIsIlNoYXBlIiwiUm9sZSIsIkFuYWxvZ3kiLCJFeHRyZW1lIEJlaGF2aW91ciJdLCJyb3dzIjpbWyJRdWVyeSAoUSkiLCJucSDDlyBk4oKWIiwiV2hhdCBpbmZvcm1hdGlvbiBhbSBJIGxvb2tpbmcgZm9yPyIsIlNlYXJjaCBxdWVyeSIsIk9uZS1ob3QgYXR0ZW50aW9uIGlmIHNjb3JlcyBwZWFrIHNoYXJwbHkiXSxbIktleSAoSykiLCJuayDDlyBk4oKWIiwiV2hhdCBkbyBJIGFkdmVydGlzZT8iLCJJbmRleCBrZXkgaW4gYSBkYXRhYmFzZSIsIlVuaWZvcm0gYXR0ZW50aW9uIGlmIGFsbCBrZXlzIGVxdWFsIl0sWyJWYWx1ZSAoVikiLCJuayDDlyBkdiIsIldoYXQgY29udGVudCBkbyBJIGNhcnJ5PyIsIlN0b3JlZCByZWNvcmQgLyBjb250ZW50IiwiUmV0cmlldmFsIHVuaW5mb3JtYXRpdmUgaWYgViBpcyBjb25zdGFudCJdLFsiU2NvcmUgUyA9IFFL4bWAL+KImmTigpYiLCJucSDDlyBuayIsIlF1ZXJ5LWtleSBjb21wYXRpYmlsaXR5IiwiU2ltaWxhcml0eSBtZXRyaWMiLCJMYXJnZSBzY29yZXMgc2F0dXJhdGUgc29mdG1heCDihpIgbmVhci16ZXJvIGdyYWRpZW50cyJdLFsiV2VpZ2h0IEEgPSBzb2Z0bWF4KFMpIiwibnEgw5cgbmsiLCJOb3JtYWxpc2VkIGltcG9ydGFuY2UgcGVyIHF1ZXJ5LWtleSBwYWlyIiwiUmVsZXZhbmNlIHByb2JhYmlsaXR5IiwiUm93cyBhbHdheXMgc3VtIHRvIDE7IGVudHJvcHkgbWVhc3VyZXMgZm9jdXMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmljaWVudCBJbXBsZW1lbnRhdGlvbnMg4oCUIEZsYXNoQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBhdHRlbnRpb24gbWF0ZXJpYWxpc2VzIHRoZSBmdWxsIG7Dl24gc2NvcmUgbWF0cml4IGluIEdQVSBIQk0gKGhpZ2gtYmFuZHdpZHRoIG1lbW9yeSksIHJlcXVpcmluZyBPKG7CsikgbWVtb3J5LiBGbGFzaEF0dGVudGlvbiAoRGFvIGV0IGFsLiAyMDIyKSBhdm9pZHMgdGhpcyBieSB0aWxpbmcgY29tcHV0YXRpb24gaW4gZmFzdCBvbi1jaGlwIFNSQU06IGl0IGZ1c2VzIHNjb3JlIGNvbXB1dGF0aW9uLCBzb2Z0bWF4LCBhbmQgdmFsdWUgYWdncmVnYXRpb24gaW50byBhIHNpbmdsZSBrZXJuZWwgcGFzcywgbWFpbnRhaW5pbmcgcnVubmluZyBzb2Z0bWF4IHN0YXRpc3RpY3MgKG9ubGluZSBub3JtYWxpc2F0aW9uKSB0byBtZXJnZSBwYXJ0aWFsIHJlc3VsdHMgY29ycmVjdGx5LiBUaGUgb3V0cHV0IE8gaXMgd3JpdHRlbiB0byBIQk0gZGlyZWN0bHkg4oCUIHRoZSBzY29yZSBtYXRyaXggUyBpcyBuZXZlciBtYXRlcmlhbGlzZWQuIFRoaXMgYWNoaWV2ZXMgZXhhY3QgYXR0ZW50aW9uIGluIE8obikgbWVtb3J5IHdpdGggMuKAkzTDlyB3YWxsLWNsb2NrIHNwZWVkdXAgb24gQTEwMCBHUFVzIGNvbXBhcmVkIHRvIHN0YW5kYXJkIGltcGxlbWVudGF0aW9ucy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRpbGluZzogZGl2aWRlIFEsIEssIFYgaW50byBibG9ja3Mgb2YgfjY04oCTMTI4IHJvd3MgdGhhdCBmaXQgaW4gU1JBTSIsIk9ubGluZSBzb2Z0bWF4OiB0cmFjayBydW5uaW5nIG1heGltdW0gYW5kIG5vcm1hbGlzYXRpb24gY29uc3RhbnQgYWNyb3NzIGJsb2NrcyIsIk5vIG1hdGVyaWFsaXNhdGlvbjogbmV2ZXIgd3JpdGUgdGhlIG7Dl24gc2NvcmUgbWF0cml4IHRvIEhCTSDigJQgd3JpdGUgb25seSBvdXRwdXQgTyIsIlJlY29tcHV0YXRpb24gaW4gYmFja3dhcmQgcGFzczogcmVjb21wdXRlIFMgYW5kIEEgb24tdGhlLWZseSBmcm9tIHNhdmVkIFEsIEssIFYiLCJNZW1vcnk6IE8obikgdnMgTyhuwrIpIGZvciBzdGFuZGFyZCBhdHRlbnRpb24g4oCUIGNyaXRpY2FsIGZvciBuIFx1MDAzZSA0MDk2IiwiRmxhc2hBdHRlbnRpb24tMiAoRGFvIDIwMjMpIGZ1cnRoZXIgaW1wcm92ZXMgcGFyYWxsZWxpc20gYWNyb3NzIHRoZSBzZXF1ZW5jZSBkaW1lbnNpb24iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Scaled Dot-Product Attention — Derivation and Numerical Stability

Scaled dot-product attention is the computational core of every Transformer. Given queries Q, keys K, and values V it computes a weighted sum of value vectors where the weights are determined by query-key similarity: Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V. Three design choices — dot-product scoring, √dₖ scaling, and softmax normalisation — each have precise mathematical motivations that are easy to miss when reading only the formula.

## Mathematical Definition and Tensor Shapes

Queries Q ∈ ℝ^{nq×dₖ} represent nq positions asking for information. Keys K ∈ ℝ^{nk×dₖ} represent nk positions advertising what they contain. Values V ∈ ℝ^{nk×dv} carry the actual content to be retrieved. The score matrix S = QKᵀ/√dₖ ∈ ℝ^{nq×nk} measures pairwise compatibility — entry Sᵢⱼ = qᵢ·kⱼ/√dₖ is how relevant key j is to query i. Applying row-wise softmax gives attention weights A = softmax(S) ∈ ℝ^{nq×nk} with rows summing to one. The output O = AV ∈ ℝ^{nq×dv} is a convex combination of value vectors for each query.

$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

## The √dₖ Scaling Factor — Derivation

Suppose Q and K have independent entries drawn from N(0,1). The dot product qᵢ·kⱼ = Σₗ qᵢₗkⱼₗ is a sum of dₖ independent terms each with mean 0 and variance 1, so qᵢ·kⱼ ~ N(0, dₖ). The standard deviation is √dₖ — for dₖ=64 this is 8, meaning raw scores span roughly ±24. The softmax exp(x)/Σexp pushes values in its flat saturation region when |x| is large: all probability mass collapses onto the maximum-scoring key. Dividing by √dₖ restores unit variance, keeping scores in the regime where softmax distributes mass across multiple keys and its Jacobian retains non-negligible entries.

```python
import numpy as np
import torch
import torch.nn.functional as F

def sdp_attention_numpy(Q, K, V, mask=None):
    # Q: (nq, dk), K: (nk, dk), V: (nk, dv)
    # Returns: output (nq, dv), weights (nq, nk)
    dk = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(dk)
    if mask is not None:
        scores = scores + mask * -1e9
    scores = scores - scores.max(axis=-1, keepdims=True)  # numeric stability
    weights = np.exp(scores)
    weights = weights / weights.sum(axis=-1, keepdims=True)
    return weights @ V, weights

def sdp_attention_torch(Q, K, V):
    dk = Q.shape[-1]
    scores = Q @ K.transpose(-2, -1) / dk ** 0.5
    weights = F.softmax(scores, dim=-1)
    return weights @ V, weights

np.random.seed(42)
nq, nk, dk, dv = 5, 7, 64, 64
Q = np.random.randn(nq, dk).astype(np.float32)
K = np.random.randn(nk, dk).astype(np.float32)
V = np.random.randn(nk, dv).astype(np.float32)
out_np, w_np = sdp_attention_numpy(Q, K, V)
Qt = torch.tensor(Q); Kt = torch.tensor(K); Vt = torch.tensor(V)
out_pt, w_pt = sdp_attention_torch(Qt, Kt, Vt)
print('Output shape:', out_np.shape)
print('Weights row-sum:', w_np.sum(axis=1).round(5))
print('Max diff NumPy vs PyTorch:', np.abs(out_np - out_pt.numpy()).max())
```

## Softmax Saturation and Gradient Flow

The softmax Jacobian ∂σ/∂z = diag(σ) − σσᵀ has entries bounded by σᵢ(1−σᵢ). When softmax approaches a one-hot vector (due to large unscaled scores), all entries σᵢ(1−σᵢ) collapse toward zero and the Frobenius norm of the Jacobian vanishes — blocking gradient flow during backpropagation. With √dₖ scaling the score distribution remains approximately N(0,1) regardless of dₖ, keeping the Jacobian norm stable across all model sizes.

```python
import numpy as np

def softmax(x):
    e = np.exp(x - x.max())
    return e / e.sum()

def jacobian_frob_norm(s):
    # Frobenius norm of softmax Jacobian: diag(s) - s*s^T
    return np.sqrt(np.sum((np.diag(s) - np.outer(s, s)) ** 2))

print('{:>5} | {:>9} | {:>11} | {:>14} | {:>12}'.format(
    'dk', 'dot_std', 'scaled_std', 'J_unscaled', 'J_scaled'))
print('-' * 60)
np.random.seed(0)
for dk in [1, 4, 16, 64, 256, 1024]:
    q = np.random.randn(dk)
    keys = np.random.randn(6, dk)
    dots = keys @ q                    # ~ N(0, dk)
    scaled = dots / np.sqrt(dk)        # ~ N(0, 1)
    jn_u = jacobian_frob_norm(softmax(dots))
    jn_s = jacobian_frob_norm(softmax(scaled))
    print('{:>5} | {:>9.3f} | {:>11.3f} | {:>14.6f} | {:>12.6f}'.format(
        dk, dots.std(), scaled.std(), jn_u, jn_s))
print('Unscaled Jacobian norm collapses as dk grows -> vanishing gradients.')
print('Scaled norm stays near constant -> stable gradient flow.')
```

> **Numerical Stability in Implementation**: Always subtract the row maximum before computing exp: scores -= scores.max(-1, keepdims=True). This prevents overflow without changing the result since exp(x-c)/Σexp(x-c) = exp(x)/Σexp(x). PyTorch F.softmax handles this internally. For custom CUDA kernels this step is non-negotiable — a single inf produced by exp ruins the entire row.

## Attention Pattern Visualisation

The attention weight matrix A ∈ ℝ^{nq×nk} is interpretable as a soft routing map: entry Aᵢⱼ is the fraction of value-vector j aggregated into output position i. Visualising A as a heatmap reveals which key positions each query relies on. High-entropy rows (diffuse attention) indicate general information gathering; low-entropy rows (peaked attention) indicate specific retrieval. In language models, patterns like diagonal concentration (local attention), column concentration (attending to a special token), and block structure (phrase-level grouping) each reflect different linguistic behaviours.

```python
import numpy as np

def sdp_attention(Q, K, V):
    dk = Q.shape[-1]
    S = Q @ K.T / np.sqrt(dk)
    S -= S.max(axis=-1, keepdims=True)
    A = np.exp(S); A /= A.sum(axis=-1, keepdims=True)
    return A @ V, A

def print_heatmap(A, row_labels, col_labels):
    col_w = max(len(c) for c in col_labels) + 1
    header = '{:>10}'.format('') + ''.join('{:>{w}}'.format(c, w=col_w) for c in col_labels)
    print(header)
    print('-' * len(header))
    for rl, row in zip(row_labels, A):
        cells = ''.join(
            '{:>{w}}'.format('++' if w > 0.3 else '+' if w > 0.1 else '.', w=col_w)
            for w in row)
        print('{:>10}{}'.format(rl[:10], cells) + '  peak->' + col_labels[row.argmax()])

np.random.seed(99)
tokens = ['The', 'cat', 'sat', 'on', 'the', 'mat']
dk, dv = 32, 32
Q = np.random.randn(len(tokens), dk)
K = np.random.randn(len(tokens), dk)
V = np.random.randn(len(tokens), dv)
_, A = sdp_attention(Q, K, V)
print_heatmap(A, tokens, tokens)
entropy = -(A * np.log(A + 1e-9)).sum(axis=1)
print('Attention entropy per token (nats):', entropy.round(3))
print('Uniform entropy would be: {:.3f}'.format(np.log(len(tokens))))
```

## Computational Complexity

Attention has three stages: score computation QKᵀ costs O(nq·nk·dₖ), softmax costs O(nq·nk), and value aggregation AV costs O(nq·nk·dv). Total: O(nq·nk·(dₖ+dv)). For self-attention nq=nk=n, giving O(n²d). This quadratic dependence on sequence length is the primary scalability bottleneck: a 4× sequence length increase costs 16× in computation and 16× in memory for the score matrix S ∈ ℝ^{n×n}. The memory footprint is n²·4 bytes (float32); at n=4096 with dₖ=64 the score matrix alone consumes 64 MB per head.

```python
import numpy as np
import time

def attention_time_ms(seq_len, dk=64, dv=64, n_trials=3):
    rng = np.random.RandomState(42)
    timings = []
    for _ in range(n_trials):
        Q = rng.randn(seq_len, dk).astype(np.float32)
        K = rng.randn(seq_len, dk).astype(np.float32)
        V = rng.randn(seq_len, dv).astype(np.float32)
        t0 = time.perf_counter()
        S = Q @ K.T / np.sqrt(dk)         # O(n^2 * dk)
        S -= S.max(1, keepdims=True)
        A = np.exp(S); A /= A.sum(1, keepdims=True)
        _ = A @ V                          # O(n^2 * dv)
        timings.append(time.perf_counter() - t0)
    return np.median(timings) * 1000

seq_lens = [128, 256, 512, 1024, 2048]
print('{:>6} {:>9} {:>8} {:>10} {:>8}'.format('n', 'time_ms', 'ratio', 'n^2_ratio', 'mem_MB'))
prev_t, prev_n = None, None
for n in seq_lens:
    t = attention_time_ms(n)
    ratio = t / prev_t if prev_t else 1.0
    n2r = (n / prev_n) ** 2 if prev_n else 1.0
    mem = n * n * 4 / 1e6
    print('{:>6} {:>9.2f} {:>8.2f} {:>10.2f} {:>8.1f}'.format(n, t, ratio, n2r, mem))
    prev_t, prev_n = t, n
print('Time ratio tracks n^2 ratio -> O(n^2*d) complexity confirmed.')
```

## Attention as Soft Dictionary Lookup

Attention generalises a hard key-value store. In a hard lookup a query exactly matches one key and retrieves the corresponding value. In soft attention the query computes a similarity score with every key and retrieves a differentiable weighted blend of all values. The softmax plays the role of a differentiable argmax — approximating discrete selection while remaining differentiable throughout. This framing clarifies the design: queries ask questions, keys describe what each position knows about itself, and values carry the payload to be aggregated.

| Component | Shape | Role | Analogy | Extreme Behaviour |
| --- | --- | --- | --- | --- |
| Query (Q) | nq × dₖ | What information am I looking for? | Search query | One-hot attention if scores peak sharply |
| Key (K) | nk × dₖ | What do I advertise? | Index key in a database | Uniform attention if all keys equal |
| Value (V) | nk × dv | What content do I carry? | Stored record / content | Retrieval uninformative if V is constant |
| Score S = QKᵀ/√dₖ | nq × nk | Query-key compatibility | Similarity metric | Large scores saturate softmax → near-zero gradients |
| Weight A = softmax(S) | nq × nk | Normalised importance per query-key pair | Relevance probability | Rows always sum to 1; entropy measures focus |

## Efficient Implementations — FlashAttention

Standard attention materialises the full n×n score matrix in GPU HBM (high-bandwidth memory), requiring O(n²) memory. FlashAttention (Dao et al. 2022) avoids this by tiling computation in fast on-chip SRAM: it fuses score computation, softmax, and value aggregation into a single kernel pass, maintaining running softmax statistics (online normalisation) to merge partial results correctly. The output O is written to HBM directly — the score matrix S is never materialised. This achieves exact attention in O(n) memory with 2–4× wall-clock speedup on A100 GPUs compared to standard implementations.

- Tiling: divide Q, K, V into blocks of ~64–128 rows that fit in SRAM
- Online softmax: track running maximum and normalisation constant across blocks
- No materialisation: never write the n×n score matrix to HBM — write only output O
- Recomputation in backward pass: recompute S and A on-the-fly from saved Q, K, V
- Memory: O(n) vs O(n²) for standard attention — critical for n > 4096
- FlashAttention-2 (Dao 2023) further improves parallelism across the sequence dimension

---

