---
title: "GANs — Minimax Objective and Training Dynamics"
slug: "gans-minimax-training"
description: "The GAN minimax game, Nash equilibrium, non-saturating generator loss, alternating training with k discriminator steps, mode collapse detection, diagnostic monitoring, and practical training tips for stable convergence."
tags: ["deep-learning", "generative-models", "gans"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2VuZXJhdGl2ZSBBZHZlcnNhcmlhbCBOZXR3b3JrcyAoR29vZGZlbGxvdyBldCBhbC4sIDIwMTQpIGZyYW1lIGdlbmVyYXRpdmUgbW9kZWxsaW5nIGFzIGEgdHdvLXBsYXllciB6ZXJvLXN1bSBnYW1lLiBBIGdlbmVyYXRvciBHIG1hcHMgbm9pc2UgeiB+IHAoeikgdG8gRyh6KSB+IHBfZywgYXR0ZW1wdGluZyB0byBtYXRjaCB0aGUgdHJ1ZSBkYXRhIGRpc3RyaWJ1dGlvbiBwX2RhdGEuIEEgZGlzY3JpbWluYXRvciBEOiB4IOKGkiBbMCwxXSBjbGFzc2lmaWVzIGlucHV0cyBhcyByZWFsIG9yIGdlbmVyYXRlZC4gVGhlIGFkdmVyc2FyaWFsIGludGVyYWN0aW9uIGRyaXZlcyBib3RoIG5ldHdvcmtzIHRvd2FyZCBhbiBlcXVpbGlicml1bSB3aGVyZSB0aGUgZ2VuZXJhdGVkIGRpc3RyaWJ1dGlvbiBpcyBpbmRpc3Rpbmd1aXNoYWJsZSBmcm9tIHRoZSByZWFsIG9uZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgR0FOIEZyYW1ld29yayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGdlbmVyYXRvciBHOiB6IOKGkiB4IG1hcHMgYSBsYXRlbnQgdmVjdG9yIHogc2FtcGxlZCBmcm9tIGEgcHJpb3IgKHR5cGljYWxseSBHYXVzc2lhbikgaW50byBkYXRhIHNwYWNlLCBwcm9kdWNpbmcgc3ludGhldGljIHNhbXBsZXMgRyh6KSB+IHBfZy4gVGhlIGRpc2NyaW1pbmF0b3IgRDogeCDihpIgWzAsMV0gZXN0aW1hdGVzIHRoZSBwcm9iYWJpbGl0eSB0aGF0IGl0cyBpbnB1dCBpcyBmcm9tIHBfZGF0YS4gVHJhaW5pbmcgYWx0ZXJuYXRlczogRCBpcyB1cGRhdGVkIHRvIGJldHRlciBzZXBhcmF0ZSByZWFsIGZyb20gZmFrZSwgdGhlbiBHIGlzIHVwZGF0ZWQgdG8gcHJvZHVjZSBzYW1wbGVzIHRoYXQgZm9vbCBELiBOZWl0aGVyIHBsYXllciBoYXMgZGlyZWN0IGFjY2VzcyB0byB0aGUgb3RoZXJcdTAwMjdzIG9iamVjdGl2ZSDigJQgb25seSB0aGUgb3V0cHV0IHNpZ25hbHMgbWF0dGVyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1pbmltYXggT2JqZWN0aXZlIGFuZCBOYXNoIEVxdWlsaWJyaXVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgR0FOIHZhbHVlIGZ1bmN0aW9uIGlzIGEgbWluaW1heCBnYW1lOiBtaW5fRyBtYXhfRCBWKEcsRCkgPSBFX3t4fnBfZGF0YX1bbG9nIEQoeCldICsgRV97en5wKHopfVtsb2coMS1EKEcoeikpKV0uIEZvciBhIGZpeGVkIEcsIHRoZSBvcHRpbWFsIGRpc2NyaW1pbmF0b3IgaXMgRCooeCkgPSBwX2RhdGEoeCkgLyAocF9kYXRhKHgpICsgcF9nKHgpKS4gQXQgTmFzaCBlcXVpbGlicml1bSwgcF9nID0gcF9kYXRhIGV2ZXJ5d2hlcmUgYW5kIEQqID0gMS8yIGV2ZXJ5d2hlcmUg4oCUIHRoZSBkaXNjcmltaW5hdG9yIGNhbm5vdCBkaXN0aW5ndWlzaCByZWFsIGZyb20gZ2VuZXJhdGVkIHNhbXBsZXMsIGFuZCBuZWl0aGVyIHBsYXllciBnYWlucyBieSBkZXZpYXRpbmcgdW5pbGF0ZXJhbGx5LiJ9LHsidHlwZSI6Im1hdGgiLCJjb250ZW50IjoiXFxtaW5fRyBcXG1heF9EIFxcOyBWKEcsRCkgPSBcXG1hdGhiYntFfV97eCBcXHNpbSBwX3tcXHRleHR7ZGF0YX19fVtcXGxvZyBEKHgpXSArIFxcbWF0aGJie0V9X3t6IFxcc2ltIHAoeil9W1xcbG9nKDEgLSBEKEcoeikpKV0iLCJkaXNwbGF5Ijp0cnVlfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgR2VuZXJhdG9yIExvc3M6IE5vbi1TYXR1cmF0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbWluaW1heCBnZW5lcmF0b3Igb2JqZWN0aXZlIChtaW5pbWl6ZSBsb2coMS1EKEcoeikpKSkgc2F0dXJhdGVzIGVhcmx5IGluIHRyYWluaW5nOiB3aGVuIHRoZSBkaXNjcmltaW5hdG9yIGlzIHdpbm5pbmcgYW5kIEQoRyh6KSkgaXMgbmVhciAwLCB0aGUgZ3JhZGllbnQgb2YgbG9nKDEtRChHKHopKSkgd2l0aCByZXNwZWN0IHRvIEdcdTAwMjdzIHBhcmFtZXRlcnMgYXBwcm9hY2hlcyB6ZXJvIOKAlCB0aGUgZ2VuZXJhdG9yIHJlY2VpdmVzIG5vIHVzZWZ1bCBsZWFybmluZyBzaWduYWwuIFRoZSBub24tc2F0dXJhdGluZyBhbHRlcm5hdGl2ZSBtYXhpbWlzZXMgbG9nIEQoRyh6KSkgaW5zdGVhZC4gQm90aCBvYmplY3RpdmVzIGhhdmUgdGhlIHNhbWUgTmFzaCBlcXVpbGlicml1bSBidXQgdGhlIG5vbi1zYXR1cmF0aW5nIGxvc3MgcHJvdmlkZXMgc3Ryb25nIGdyYWRpZW50cyBwcmVjaXNlbHkgd2hlbiB0aGUgZGlzY3JpbWluYXRvciBkb21pbmF0ZXMsIHdoaWNoIG9jY3VycyB0aHJvdWdob3V0IG1vc3Qgb2YgdHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWx0ZXJuYXRpbmcgVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzdGFuZGFyZCBHQU4gdHJhaW5pbmcgcHJvdG9jb2wgdXBkYXRlcyBEIGZvciBrIHN0ZXBzICh1c3VhbGx5IGs9MSkgdGhlbiB1cGRhdGVzIEcgb25jZSBwZXIgaXRlcmF0aW9uLiBNb3JlIEQgdXBkYXRlcyBwZXIgRyBzdGVwIG1haW50YWluIGEgc3Ryb25nZXIgZ3JhZGllbnQgc2lnbmFsIGZvciBHIGJ1dCBpbmNyZWFzZSBwZXItaXRlcmF0aW9uIGNvc3QuIExhYmVsIHNtb290aGluZyByZXBsYWNlcyB0YXJnZXQgMS4wIHdpdGggMC45IGZvciByZWFsIHNhbXBsZXMsIHByZXZlbnRpbmcgdGhlIGRpc2NyaW1pbmF0b3IgZnJvbSBwdXNoaW5nIGl0cyBvdXRwdXRzIHRvIGV4dHJlbWVzLiBBZGRpbmcgc21hbGwgR2F1c3NpYW4gbm9pc2UgdG8gZGlzY3JpbWluYXRvciBpbnB1dHMgKGFubmVhbGVkIG92ZXIgdHJhaW5pbmcpIGFsc28gc3RhYmlsaXNlcyBkeW5hbWljcyBieSBwcmV2ZW50aW5nIEQgZnJvbSBtZW1vcmlzaW5nIGV4YWN0IHRyYWluaW5nIGV4YW1wbGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5cbmRlZiB0cmFpbl9nYW4oZ2VuZXJhdG9yLCBkaXNjcmltaW5hdG9yLCBkYXRhbG9hZGVyLFxuICAgICAgICAgICAgIG51bV9lcG9jaHM9NTAsIGs9MSwgbGF0ZW50X2RpbT0xMDApOlxuICAgIG9wdF9HID0gb3B0aW0uQWRhbShnZW5lcmF0b3IucGFyYW1ldGVycygpLCBscj0wLjAwMDIsIGJldGFzPSgwLjUsIDAuOTk5KSlcbiAgICBvcHRfRCA9IG9wdGltLkFkYW0oZGlzY3JpbWluYXRvci5wYXJhbWV0ZXJzKCksIGxyPTAuMDAwMiwgYmV0YXM9KDAuNSwgMC45OTkpKVxuICAgIGNyaXRlcmlvbiA9IG5uLkJDRUxvc3MoKVxuICAgIGZvciBlcG9jaCBpbiByYW5nZShudW1fZXBvY2hzKTpcbiAgICAgICAgZm9yIHJlYWxfaW1ncywgXyBpbiBkYXRhbG9hZGVyOlxuICAgICAgICAgICAgYnMgPSByZWFsX2ltZ3Muc2l6ZSgwKVxuICAgICAgICAgICAgcmVhbF9sYWJlbHMgPSB0b3JjaC5vbmVzKGJzLCAxKSAqIDAuOSAgICMgbGFiZWwgc21vb3RoaW5nXG4gICAgICAgICAgICBmYWtlX2xhYmVscyA9IHRvcmNoLnplcm9zKGJzLCAxKVxuICAgICAgICAgICAgIyAtLS0gRGlzY3JpbWluYXRvcjogayBzdGVwcyBwZXIgRyBzdGVwIC0tLVxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2Uoayk6XG4gICAgICAgICAgICAgICAgb3B0X0QuemVyb19ncmFkKClcbiAgICAgICAgICAgICAgICB6ID0gdG9yY2gucmFuZG4oYnMsIGxhdGVudF9kaW0pXG4gICAgICAgICAgICAgICAgZF9yZWFsID0gZGlzY3JpbWluYXRvcihyZWFsX2ltZ3MpXG4gICAgICAgICAgICAgICAgZF9mYWtlID0gZGlzY3JpbWluYXRvcihnZW5lcmF0b3IoeikuZGV0YWNoKCkpXG4gICAgICAgICAgICAgICAgZF9sb3NzID0gY3JpdGVyaW9uKGRfcmVhbCwgcmVhbF9sYWJlbHMpICsgY3JpdGVyaW9uKGRfZmFrZSwgZmFrZV9sYWJlbHMpXG4gICAgICAgICAgICAgICAgZF9sb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgICAgICBvcHRfRC5zdGVwKClcbiAgICAgICAgICAgICMgLS0tIEdlbmVyYXRvcjogbm9uLXNhdHVyYXRpbmcgbG9zcyAobWF4aW1pemUgbG9nIEQoRyh6KSkpIC0tLVxuICAgICAgICAgICAgb3B0X0cuemVyb19ncmFkKClcbiAgICAgICAgICAgIHogPSB0b3JjaC5yYW5kbihicywgbGF0ZW50X2RpbSlcbiAgICAgICAgICAgIGdfbG9zcyA9IGNyaXRlcmlvbihkaXNjcmltaW5hdG9yKGdlbmVyYXRvcih6KSksIHJlYWxfbGFiZWxzKVxuICAgICAgICAgICAgZ19sb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdF9HLnN0ZXAoKVxuICAgICAgICBpZiBlcG9jaCAlIDEwID09IDA6XG4gICAgICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NofTogRD17ZF9sb3NzLml0ZW0oKTouNGZ9ICBHPXtnX2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgU2F0dXJhdGlvbjogTWluaW1heCB2cyBOb24tU2F0dXJhdGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBkaWZmZXJlbmNlIGJldHdlZW4gdGhlIHR3byBnZW5lcmF0b3IgbG9zc2VzIGlzIGdyYWRpZW50IG1hZ25pdHVkZSB3aGVuIHRoZSBkaXNjcmltaW5hdG9yIGRvbWluYXRlcy4gRm9yIG1pbmltYXggbG9zcyB0aGUgZ3JhZGllbnQgb2YgbG9nKDEtRChHKHopKSkgaXMgMS8oMS1EKEcoeikpKSDigJQgbGFyZ2Ugd2hlbiBEIGlzIHVuY2VydGFpbiBidXQgdGhlIHNpZ24gbWFrZXMgaXQgdW5oZWxwZnVsIHdoZW4gRCBpcyB3aW5uaW5nLiBGb3Igbm9uLXNhdHVyYXRpbmcgbG9zcywgdGhlIGdyYWRpZW50IG9mIC1sb2cgRChHKHopKSBpcyAxL0QoRyh6KSkg4oCUIGxhcmdlc3QgcHJlY2lzZWx5IHdoZW4gRChHKHopKSBpcyBzbWFsbCwgbWVhbmluZyBHIHJlY2VpdmVzIGEgc3Ryb25nIHVwZGF0ZSBzaWduYWwgd2hlbiBpdCBpcyBsb3NpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBtaW5pbWF4X2dfbG9zcyhkX2Zha2UpOlxuICAgIHJldHVybiB0b3JjaC5sb2coMSAtIGRfZmFrZSArIDFlLTgpLm1lYW4oKVxuXG5kZWYgbm9uc2F0dXJhdGluZ19nX2xvc3MoZF9mYWtlKTpcbiAgICByZXR1cm4gLXRvcmNoLmxvZyhkX2Zha2UgKyAxZS04KS5tZWFuKClcblxuZGVmIGdyYWRpZW50X21hZ25pdHVkZShsb3NzX2ZuLCBkX3ZhbCk6XG4gICAgZCA9IHRvcmNoLnRlbnNvcihbZF92YWxdLCByZXF1aXJlc19ncmFkPVRydWUsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgbG9zc19mbihkKS5iYWNrd2FyZCgpXG4gICAgcmV0dXJuIGFicyhkLmdyYWQuaXRlbSgpKVxuXG5kX3ZhbHVlcyA9IFswLjA1LCAwLjEsIDAuMiwgMC41LCAwLjgsIDAuOSwgMC45NV1cbnByaW50KGZcdTAwMjd7XCJEKEcoeikpXCI6XHUwMDNjMTB9IHtcIm1pbmltYXggfGdyYWR8XCI6XHUwMDNjMjB9IHtcIm5vbi1zYXQgfGdyYWR8XCI6XHUwMDNjMjB9XHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDUwKVxuZm9yIGRfdmFsIGluIGRfdmFsdWVzOlxuICAgIG1tX2dyYWQgPSBncmFkaWVudF9tYWduaXR1ZGUobWluaW1heF9nX2xvc3MsIGRfdmFsKVxuICAgIG5zX2dyYWQgPSBncmFkaWVudF9tYWduaXR1ZGUobm9uc2F0dXJhdGluZ19nX2xvc3MsIGRfdmFsKVxuICAgIHByaW50KGZcdTAwMjd7ZF92YWw6XHUwMDNjMTAuMmZ9IHttbV9ncmFkOlx1MDAzYzIwLjRmfSB7bnNfZ3JhZDpcdTAwM2MyMC40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdNaW5pbWF4IGdyYWRpZW50IGlzIHdlYWsgd2hlbiBEIGlzIHdpbm5pbmcgKGRfdmFsIHNtYWxsKS5cdTAwMjcpXG5wcmludChcdTAwMjdOb24tc2F0dXJhdGluZyBncmFkaWVudCBpcyBzdHJvbmdlc3QgZXhhY3RseSB3aGVuIEQgaXMgd2lubmluZy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tbW9uIFRyYWluaW5nIEZhaWx1cmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHQU4gdHJhaW5pbmcgaXMgbm90b3Jpb3VzbHkgdW5zdGFibGUuIE1vZGUgY29sbGFwc2Ugb2NjdXJzIHdoZW4gRyBtYXBzIG1hbnkgZGlmZmVyZW50IHogdG8gbmVhcmx5IHRoZSBzYW1lIG91dHB1dCwgcHJvZHVjaW5nIGxvdy1kaXZlcnNpdHkgc2FtcGxlcy4gRGlzY3JpbWluYXRvciBkb21pbmFuY2UgaGFwcGVucyB3aGVuIEQgdHJhaW5zIG11Y2ggZmFzdGVyIHRoYW4gRywgbGVhdmluZyBHIHdpdGggdmFuaXNoaW5nIGdyYWRpZW50cy4gT3NjaWxsYXRpb24gaXMgdGhlIGZhaWx1cmUgbW9kZSB3aGVyZSBuZWl0aGVyIGxvc3MgY29udmVyZ2VzIGJ1dCBib3RoIGN5Y2xlIGNvbnRpbnVvdXNseSwgaW5kaWNhdGluZyBhcmNoaXRlY3R1cmUgbWlzbWF0Y2ggb3IgbGVhcm5pbmcgcmF0ZSBpc3N1ZXMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJNb2RlIENvbGxhcHNlIFJpc2siLCJjb250ZW50IjoiTW9kZSBjb2xsYXBzZSBpcyB0aGUgbW9zdCBjb21tb24gR0FOIGZhaWx1cmU6IHRoZSBnZW5lcmF0b3IgZGlzY292ZXJzIGEgZmV3IG91dHB1dHMgdGhhdCBjb25zaXN0ZW50bHkgZm9vbCB0aGUgZGlzY3JpbWluYXRvciBidXQgY292ZXJzIG9ubHkgYSBzbWFsbCBzdWJzZXQgb2YgdGhlIHRydWUgZGF0YSBkaXN0cmlidXRpb24uIE1vbml0b3IgYnkgdHJhY2tpbmcgY2xhc3MgY292ZXJhZ2UgZW50cm9weSBhbmQgRklELiBNaXRpZ2F0aW9ucyBpbmNsdWRlIG1pbmliYXRjaCBkaXNjcmltaW5hdGlvbiwgdW5yb2xsZWQgR0FOcywgYW5kIHN3aXRjaGluZyB0byBXR0FOLUdQIHdoaWNoIGhhcyBzdHJvbmdlciB0aGVvcmV0aWNhbCBndWFyYW50ZWVzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9ibGVtIiwiQ2F1c2UiLCJTeW1wdG9tIiwiRml4Il0sInJvd3MiOltbIk1vZGUgY29sbGFwc2UiLCJHIGZpbmRzIGEgbG9jYWwgb3B0aW11bSBjb3ZlcmluZyBvbmx5IGEgZmV3IGRhdGEgbW9kZXMiLCJHZW5lcmF0ZWQgc2FtcGxlcyBsb29rIGlkZW50aWNhbCBvciBuZWFyLWlkZW50aWNhbDsgbG93IEZJRCBkaXZlcnNpdHkiLCJNaW5pYmF0Y2ggZGlzY3JpbWluYXRpb24sIHVucm9sbGVkIEdBTnMsIFdHQU4iXSxbIlZhbmlzaGluZyBncmFkaWVudCIsIkQgdG9vIHN0cm9uZzsgbWluaW1heCBHIGxvc3Mgc2F0dXJhdGVzIG5lYXIgemVybyIsIkcgbG9zcyBzdHVjaywgZ2VuZXJhdGVkIGltYWdlcyBkbyBub3QgaW1wcm92ZSIsIk5vbi1zYXR1cmF0aW5nIGxvc3MsIHJlZHVjZSBEIGNhcGFjaXR5LCBhZGQgbm9pc2UgdG8gRCBpbnB1dHMiXSxbIk9zY2lsbGF0aW9uIiwiTmVpdGhlciBwbGF5ZXIgY29udmVyZ2VzOyB1bnN0YWJsZSBnYW1lIGR5bmFtaWNzIiwiTG9zc2VzIGN5Y2xlIHdpdGhvdXQgdHJlbmQ7IElTIGFuZCBGSUQgcGxhdGVhdSBvciB3b3JzZW4iLCJSZWR1Y2UgbGVhcm5pbmcgcmF0ZSwgc3BlY3RyYWwgbm9ybSwgZ3JhZGllbnQgcGVuYWx0eSJdLFsiRCBkb21pbmF0ZXMgZWFybHkiLCJEIHRyYWlucyBtdWNoIGZhc3RlciB0aGFuIEcgZnJvbSB0aGUgc3RhcnQiLCJEIGxvc3MgcXVpY2tseSBkcm9wcyB0byB6ZXJvOyBHIG1ha2VzIG5vIHByb2dyZXNzIiwiUmVkdWNlIEQgdXBkYXRlcyBwZXIgRyBzdGVwLCBiYWxhbmNlIGFyY2hpdGVjdHVyZXMiXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlclxuXG5kZWYgZGV0ZWN0X21vZGVfY29sbGFwc2UoZ2VuZXJhdG9yLCBjbGFzc2lmaWVyLCBsYXRlbnRfZGltPTEwMCxcbiAgICAgICAgICAgICAgICAgICAgICAgICBuX3NhbXBsZXM9MTAyNCwgbl9jbGFzc2VzPTEwKTpcbiAgICBnZW5lcmF0b3IuZXZhbCgpXG4gICAgY2xhc3NfY291bnRzID0gQ291bnRlcigpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fc2FtcGxlcyAvLyA2NCk6XG4gICAgICAgICAgICB6ID0gdG9yY2gucmFuZG4oNjQsIGxhdGVudF9kaW0pXG4gICAgICAgICAgICBwcmVkcyA9IGNsYXNzaWZpZXIoZ2VuZXJhdG9yKHopKS5hcmdtYXgoZGltPTEpXG4gICAgICAgICAgICBjbGFzc19jb3VudHMudXBkYXRlKHByZWRzLmNwdSgpLm51bXB5KCkudG9saXN0KCkpXG4gICAgdG90YWwgPSBzdW0oY2xhc3NfY291bnRzLnZhbHVlcygpKVxuICAgIGNvdmVyYWdlID0gbGVuKGNsYXNzX2NvdW50cykgLyBuX2NsYXNzZXNcbiAgICBkaXN0ID0ge2NsczogY2xhc3NfY291bnRzLmdldChjbHMsIDApIC8gdG90YWwgZm9yIGNscyBpbiByYW5nZShuX2NsYXNzZXMpfVxuICAgIHByb2JzID0gbnAuYXJyYXkobGlzdChkaXN0LnZhbHVlcygpKSkgKyAxZS0xMFxuICAgIGVudHJvcHkgPSAtbnAuc3VtKHByb2JzICogbnAubG9nKHByb2JzKSlcbiAgICBtYXhfZW50ID0gbnAubG9nKG5fY2xhc3NlcylcbiAgICBwcmludChmXHUwMDI3Q2xhc3MgY292ZXJhZ2UgOiB7Y292ZXJhZ2U6LjAlfSAoe2xlbihjbGFzc19jb3VudHMpfS97bl9jbGFzc2VzfSBjbGFzc2VzKVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3RGl2ZXJzaXR5IHNjb3JlOiB7ZW50cm9weSAvIG1heF9lbnQ6LjIlfSAoMS4wID0gcGVyZmVjdGx5IHVuaWZvcm0gZGlzdHJpYnV0aW9uKVx1MDAyNylcbiAgICBpZiBjb3ZlcmFnZSBcdTAwM2MgMC41OlxuICAgICAgICBwcmludChcdTAwMjdXQVJOSU5HOiBmZXdlciB0aGFuIGhhbGYgb2YgY2xhc3NlcyBjb3ZlcmVkIOKAlCBtb2RlIGNvbGxhcHNlIGxpa2VseVx1MDAyNylcbiAgICByZXR1cm4ge1x1MDAyN2NvdmVyYWdlXHUwMDI3OiBjb3ZlcmFnZSwgXHUwMDI3ZW50cm9weV9yYXRpb1x1MDAyNzogZW50cm9weSAvIG1heF9lbnQsIFx1MDAyN2Rpc3RcdTAwMjc6IGRpc3R9In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9uaXRvcmluZyBhbmQgRGlhZ25vc3RpY3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlbGlhYmxlIGRpYWdub3N0aWMgbWV0cmljcyBhcmUgZXNzZW50aWFsIGZvciBHQU4gdHJhaW5pbmcuIFRyYWNrIEQocmVhbCkgYW5kIEQoZmFrZSkgc2VwYXJhdGVseSDigJQgYXQgZXF1aWxpYnJpdW0gYm90aCBzaG91bGQgaG92ZXIgbmVhciAwLjUuIFRyYWNrIGdyYWRpZW50IG5vcm1zIGZvciBib3RoIEcgYW5kIEQ6IGV4cGxvZGluZyBvciB2YW5pc2hpbmcgbm9ybXMgc2lnbmFsIGluc3RhYmlsaXR5LiBDb21wdXRlIEZJRCBldmVyeSA1LDAwMOKAkzEwLDAwMCBzdGVwcyB1c2luZyBhIGZpeGVkIHNldCBvZiBnZW5lcmF0ZWQgaW1hZ2VzIGNvbXBhcmVkIHRvIHJlYWwgZGF0YSBzdGF0aXN0aWNzLiBGSUQgcGxhdGVhdSDigJQgbm90IGxvc3MgY29udmVyZ2VuY2Ug4oCUIGlzIHRoZSBiZXN0IHN0b3BwaW5nIGNyaXRlcmlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBkZWZhdWx0ZGljdFxuXG5kZWYgZ3JhZF9ub3JtKG1vZGVsKTpcbiAgICB0b3RhbCA9IDAuMFxuICAgIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgaWYgcC5ncmFkIGlzIG5vdCBOb25lOlxuICAgICAgICAgICAgdG90YWwgKz0gcC5ncmFkLmRhdGEubm9ybSgyKS5pdGVtKCkgKiogMlxuICAgIHJldHVybiB0b3RhbCAqKiAwLjVcblxuY2xhc3MgR0FORGlhZ25vc3RpY3M6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLmggPSBkZWZhdWx0ZGljdChsaXN0KVxuXG4gICAgZGVmIHJlY29yZChzZWxmLCBkX3JlYWwsIGRfZmFrZSwgZF9sb3NzLCBnX2xvc3MsIEcsIEQpOlxuICAgICAgICBzZWxmLmhbXHUwMDI3RF9yZWFsXHUwMDI3XS5hcHBlbmQoZF9yZWFsLm1lYW4oKS5pdGVtKCkpXG4gICAgICAgIHNlbGYuaFtcdTAwMjdEX2Zha2VcdTAwMjddLmFwcGVuZChkX2Zha2UubWVhbigpLml0ZW0oKSlcbiAgICAgICAgc2VsZi5oW1x1MDAyN0RfbG9zc1x1MDAyN10uYXBwZW5kKGRfbG9zcy5pdGVtKCkpXG4gICAgICAgIHNlbGYuaFtcdTAwMjdHX2xvc3NcdTAwMjddLmFwcGVuZChnX2xvc3MuaXRlbSgpKVxuICAgICAgICBzZWxmLmhbXHUwMDI3R19nbm9ybVx1MDAyN10uYXBwZW5kKGdyYWRfbm9ybShHKSlcbiAgICAgICAgc2VsZi5oW1x1MDAyN0RfZ25vcm1cdTAwMjddLmFwcGVuZChncmFkX25vcm0oRCkpXG5cbiAgICBkZWYgcGxvdChzZWxmKTpcbiAgICAgICAgZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDEsIDMsIGZpZ3NpemU9KDE1LCA0KSlcbiAgICAgICAgYXhlc1swXS5wbG90KHNlbGYuaFtcdTAwMjdEX3JlYWxcdTAwMjddLCBsYWJlbD1cdTAwMjdEKHJlYWwpXHUwMDI3LCBjb2xvcj1cdTAwMjdzdGVlbGJsdWVcdTAwMjcpXG4gICAgICAgIGF4ZXNbMF0ucGxvdChzZWxmLmhbXHUwMDI3RF9mYWtlXHUwMDI3XSwgbGFiZWw9XHUwMDI3RChmYWtlKVx1MDAyNywgY29sb3I9XHUwMDI3dG9tYXRvXHUwMDI3KVxuICAgICAgICBheGVzWzBdLmF4aGxpbmUoMC41LCBscz1cdTAwMjctLVx1MDAyNywgY29sb3I9XHUwMDI3Z3JheVx1MDAyNywgbGFiZWw9XHUwMDI3aWRlYWw9MC41XHUwMDI3KVxuICAgICAgICBheGVzWzBdLnNldF90aXRsZShcdTAwMjdEaXNjcmltaW5hdG9yIE91dHB1dHNcdTAwMjcpOyBheGVzWzBdLmxlZ2VuZCgpXG4gICAgICAgIGF4ZXNbMV0ucGxvdChzZWxmLmhbXHUwMDI3RF9sb3NzXHUwMDI3XSwgbGFiZWw9XHUwMDI3RCBsb3NzXHUwMDI3KVxuICAgICAgICBheGVzWzFdLnBsb3Qoc2VsZi5oW1x1MDAyN0dfbG9zc1x1MDAyN10sIGxhYmVsPVx1MDAyN0cgbG9zc1x1MDAyNylcbiAgICAgICAgYXhlc1sxXS5zZXRfdGl0bGUoXHUwMDI3VHJhaW5pbmcgTG9zc2VzXHUwMDI3KTsgYXhlc1sxXS5sZWdlbmQoKVxuICAgICAgICBheGVzWzJdLnBsb3Qoc2VsZi5oW1x1MDAyN0dfZ25vcm1cdTAwMjddLCBsYWJlbD1cdTAwMjdHIGdyYWQgbm9ybVx1MDAyNylcbiAgICAgICAgYXhlc1syXS5wbG90KHNlbGYuaFtcdTAwMjdEX2dub3JtXHUwMDI3XSwgbGFiZWw9XHUwMDI3RCBncmFkIG5vcm1cdTAwMjcpXG4gICAgICAgIGF4ZXNbMl0uc2V0X3RpdGxlKFx1MDAyN0dyYWRpZW50IE5vcm1zXHUwMDI3KTsgYXhlc1syXS5sZWdlbmQoKVxuICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyBUaXBzIGFuZCBUcmlja3MifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkxhYmVsIHNtb290aGluZzogdXNlIDAuOSBpbnN0ZWFkIG9mIDEuMCBmb3IgcmVhbCB0YXJnZXRzIHRvIHByZXZlbnQgZGlzY3JpbWluYXRvciBvdmVyY29uZmlkZW5jZSIsIkFkZCBhbm5lYWxlZCBHYXVzc2lhbiBub2lzZSB0byBEIGlucHV0cyDigJQgc3RhcnQgc3RkPTAuMSBhbmQgZGVjYXkgdG8gMCBvdmVyIHRyYWluaW5nIiwiU3BlY3RyYWwgbm9ybWFsaXphdGlvbiBvbiBEIHdlaWdodHMgZW5mb3JjZXMgYSBMaXBzY2hpdHogY29uc3RyYWludCB3aXRob3V0IGJhdGNoIHN0YXRpc3RpY3MiLCJBdm9pZCBCYXRjaE5vcm0gaW4gRCDigJQgaXQgY291cGxlcyBzYW1wbGVzIGFjcm9zcyB0aGUgYmF0Y2g7IHVzZSBJbnN0YW5jZU5vcm0gb3Igbm8gbm9ybSIsIlVzZSBBZGFtIHdpdGggYmV0YTE9MC41IChub3QgZGVmYXVsdCAwLjkpIOKAlCBsb3dlciBtb21lbnR1bSBwcmV2ZW50cyBvc2NpbGxhdGlvbiBpbiBHQU4gdHJhaW5pbmciLCJNb25pdG9yIEZJRCBldmVyeSA1LDAwMOKAkzEwLDAwMCBzdGVwczsgdXNlIEZJRCBwbGF0ZWF1IG5vdCBsb3NzIHBsYXRlYXUgYXMgc3RvcHBpbmcgY3JpdGVyaW9uIiwiU2F2ZSBHIGNoZWNrcG9pbnRzIGZyZXF1ZW50bHkg4oCUIEdBTiB0cmFpbmluZyBjYW4gZGVncmFkZSBhZnRlciByZWFjaGluZyBhIGdvb2Qgc3RhdGUiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR0FOcyB2cyBEaWZmdXNpb24gTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHQU5zIGdlbmVyYXRlIHNhbXBsZXMgaW4gYSBzaW5nbGUgZm9yd2FyZCBwYXNzIChtaWxsaXNlY29uZHMgcGVyIGltYWdlKSwgbWFraW5nIHRoZW0gZmFzdCBhdCBpbmZlcmVuY2UuIERpZmZ1c2lvbiBtb2RlbHMgcmVxdWlyZSBodW5kcmVkcyBvZiBkZW5vaXNpbmcgc3RlcHMgKHNlY29uZHMgcGVyIGltYWdlKSBidXQgYXJlIGVhc2llciB0byB0cmFpbiwgbW9yZSBzdGFibGUsIHByb2R1Y2UgbW9yZSBkaXZlcnNlIG91dHB1dHMsIGFuZCBkb21pbmF0ZSBGSUQgYmVuY2htYXJrcyBvbiB1bmNvbmRpdGlvbmFsIGltYWdlIGdlbmVyYXRpb24gYXMgb2YgMjAyNC4gR0FOcyByZW1haW4gY29tcGV0aXRpdmUgaW4gdmlkZW8gZ2VuZXJhdGlvbiwgc3VwZXItcmVzb2x1dGlvbiwgYW5kIHJlYWwtdGltZSBhcHBsaWNhdGlvbnMgd2hlcmUgaW5mZXJlbmNlIGxhdGVuY3kgaXMgY3JpdGljYWwuIFdHQU4tR1AgYW5kIFN0eWxlR0FOMiByZXByZXNlbnQgdGhlIGZyb250aWVyIG9mIEdBTiBxdWFsaXR5LiJ9XQ=="
---
# GANs — Minimax Objective and Training Dynamics

Generative Adversarial Networks (Goodfellow et al., 2014) frame generative modelling as a two-player zero-sum game. A generator G maps noise z ~ p(z) to G(z) ~ p_g, attempting to match the true data distribution p_data. A discriminator D: x → [0,1] classifies inputs as real or generated. The adversarial interaction drives both networks toward an equilibrium where the generated distribution is indistinguishable from the real one.

## The GAN Framework

The generator G: z → x maps a latent vector z sampled from a prior (typically Gaussian) into data space, producing synthetic samples G(z) ~ p_g. The discriminator D: x → [0,1] estimates the probability that its input is from p_data. Training alternates: D is updated to better separate real from fake, then G is updated to produce samples that fool D. Neither player has direct access to the other's objective — only the output signals matter.

## Minimax Objective and Nash Equilibrium

The GAN value function is a minimax game: min_G max_D V(G,D) = E_{x~p_data}[log D(x)] + E_{z~p(z)}[log(1-D(G(z)))]. For a fixed G, the optimal discriminator is D*(x) = p_data(x) / (p_data(x) + p_g(x)). At Nash equilibrium, p_g = p_data everywhere and D* = 1/2 everywhere — the discriminator cannot distinguish real from generated samples, and neither player gains by deviating unilaterally.

$$\min_G \max_D \; V(G,D) = \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim p(z)}[\log(1 - D(G(z)))]$$

## Practical Generator Loss: Non-Saturating

The minimax generator objective (minimize log(1-D(G(z)))) saturates early in training: when the discriminator is winning and D(G(z)) is near 0, the gradient of log(1-D(G(z))) with respect to G's parameters approaches zero — the generator receives no useful learning signal. The non-saturating alternative maximises log D(G(z)) instead. Both objectives have the same Nash equilibrium but the non-saturating loss provides strong gradients precisely when the discriminator dominates, which occurs throughout most of training.

## Alternating Training

The standard GAN training protocol updates D for k steps (usually k=1) then updates G once per iteration. More D updates per G step maintain a stronger gradient signal for G but increase per-iteration cost. Label smoothing replaces target 1.0 with 0.9 for real samples, preventing the discriminator from pushing its outputs to extremes. Adding small Gaussian noise to discriminator inputs (annealed over training) also stabilises dynamics by preventing D from memorising exact training examples.

```python
import torch
import torch.nn as nn
import torch.optim as optim

def train_gan(generator, discriminator, dataloader,
             num_epochs=50, k=1, latent_dim=100):
    opt_G = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
    opt_D = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))
    criterion = nn.BCELoss()
    for epoch in range(num_epochs):
        for real_imgs, _ in dataloader:
            bs = real_imgs.size(0)
            real_labels = torch.ones(bs, 1) * 0.9   # label smoothing
            fake_labels = torch.zeros(bs, 1)
            # --- Discriminator: k steps per G step ---
            for _ in range(k):
                opt_D.zero_grad()
                z = torch.randn(bs, latent_dim)
                d_real = discriminator(real_imgs)
                d_fake = discriminator(generator(z).detach())
                d_loss = criterion(d_real, real_labels) + criterion(d_fake, fake_labels)
                d_loss.backward()
                opt_D.step()
            # --- Generator: non-saturating loss (maximize log D(G(z))) ---
            opt_G.zero_grad()
            z = torch.randn(bs, latent_dim)
            g_loss = criterion(discriminator(generator(z)), real_labels)
            g_loss.backward()
            opt_G.step()
        if epoch % 10 == 0:
            print(f'Epoch {epoch}: D={d_loss.item():.4f}  G={g_loss.item():.4f}')
```

## Gradient Saturation: Minimax vs Non-Saturating

The key difference between the two generator losses is gradient magnitude when the discriminator dominates. For minimax loss the gradient of log(1-D(G(z))) is 1/(1-D(G(z))) — large when D is uncertain but the sign makes it unhelpful when D is winning. For non-saturating loss, the gradient of -log D(G(z)) is 1/D(G(z)) — largest precisely when D(G(z)) is small, meaning G receives a strong update signal when it is losing.

```python
import torch
import numpy as np

def minimax_g_loss(d_fake):
    return torch.log(1 - d_fake + 1e-8).mean()

def nonsaturating_g_loss(d_fake):
    return -torch.log(d_fake + 1e-8).mean()

def gradient_magnitude(loss_fn, d_val):
    d = torch.tensor([d_val], requires_grad=True, dtype=torch.float32)
    loss_fn(d).backward()
    return abs(d.grad.item())

d_values = [0.05, 0.1, 0.2, 0.5, 0.8, 0.9, 0.95]
print(f'{"D(G(z))":<10} {"minimax |grad|":<20} {"non-sat |grad|":<20}')
print('-' * 50)
for d_val in d_values:
    mm_grad = gradient_magnitude(minimax_g_loss, d_val)
    ns_grad = gradient_magnitude(nonsaturating_g_loss, d_val)
    print(f'{d_val:<10.2f} {mm_grad:<20.4f} {ns_grad:<20.4f}')
print('Minimax gradient is weak when D is winning (d_val small).')
print('Non-saturating gradient is strongest exactly when D is winning.')
```

## Common Training Failures

GAN training is notoriously unstable. Mode collapse occurs when G maps many different z to nearly the same output, producing low-diversity samples. Discriminator dominance happens when D trains much faster than G, leaving G with vanishing gradients. Oscillation is the failure mode where neither loss converges but both cycle continuously, indicating architecture mismatch or learning rate issues.

> **Mode Collapse Risk**: Mode collapse is the most common GAN failure: the generator discovers a few outputs that consistently fool the discriminator but covers only a small subset of the true data distribution. Monitor by tracking class coverage entropy and FID. Mitigations include minibatch discrimination, unrolled GANs, and switching to WGAN-GP which has stronger theoretical guarantees.

| Problem | Cause | Symptom | Fix |
| --- | --- | --- | --- |
| Mode collapse | G finds a local optimum covering only a few data modes | Generated samples look identical or near-identical; low FID diversity | Minibatch discrimination, unrolled GANs, WGAN |
| Vanishing gradient | D too strong; minimax G loss saturates near zero | G loss stuck, generated images do not improve | Non-saturating loss, reduce D capacity, add noise to D inputs |
| Oscillation | Neither player converges; unstable game dynamics | Losses cycle without trend; IS and FID plateau or worsen | Reduce learning rate, spectral norm, gradient penalty |
| D dominates early | D trains much faster than G from the start | D loss quickly drops to zero; G makes no progress | Reduce D updates per G step, balance architectures |

```python
import torch
import numpy as np
from collections import Counter

def detect_mode_collapse(generator, classifier, latent_dim=100,
                         n_samples=1024, n_classes=10):
    generator.eval()
    class_counts = Counter()
    with torch.no_grad():
        for _ in range(n_samples // 64):
            z = torch.randn(64, latent_dim)
            preds = classifier(generator(z)).argmax(dim=1)
            class_counts.update(preds.cpu().numpy().tolist())
    total = sum(class_counts.values())
    coverage = len(class_counts) / n_classes
    dist = {cls: class_counts.get(cls, 0) / total for cls in range(n_classes)}
    probs = np.array(list(dist.values())) + 1e-10
    entropy = -np.sum(probs * np.log(probs))
    max_ent = np.log(n_classes)
    print(f'Class coverage : {coverage:.0%} ({len(class_counts)}/{n_classes} classes)')
    print(f'Diversity score: {entropy / max_ent:.2%} (1.0 = perfectly uniform distribution)')
    if coverage < 0.5:
        print('WARNING: fewer than half of classes covered — mode collapse likely')
    return {'coverage': coverage, 'entropy_ratio': entropy / max_ent, 'dist': dist}
```

## Monitoring and Diagnostics

Reliable diagnostic metrics are essential for GAN training. Track D(real) and D(fake) separately — at equilibrium both should hover near 0.5. Track gradient norms for both G and D: exploding or vanishing norms signal instability. Compute FID every 5,000–10,000 steps using a fixed set of generated images compared to real data statistics. FID plateau — not loss convergence — is the best stopping criterion.

```python
import torch
import matplotlib.pyplot as plt
from collections import defaultdict

def grad_norm(model):
    total = 0.0
    for p in model.parameters():
        if p.grad is not None:
            total += p.grad.data.norm(2).item() ** 2
    return total ** 0.5

class GANDiagnostics:
    def __init__(self):
        self.h = defaultdict(list)

    def record(self, d_real, d_fake, d_loss, g_loss, G, D):
        self.h['D_real'].append(d_real.mean().item())
        self.h['D_fake'].append(d_fake.mean().item())
        self.h['D_loss'].append(d_loss.item())
        self.h['G_loss'].append(g_loss.item())
        self.h['G_gnorm'].append(grad_norm(G))
        self.h['D_gnorm'].append(grad_norm(D))

    def plot(self):
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        axes[0].plot(self.h['D_real'], label='D(real)', color='steelblue')
        axes[0].plot(self.h['D_fake'], label='D(fake)', color='tomato')
        axes[0].axhline(0.5, ls='--', color='gray', label='ideal=0.5')
        axes[0].set_title('Discriminator Outputs'); axes[0].legend()
        axes[1].plot(self.h['D_loss'], label='D loss')
        axes[1].plot(self.h['G_loss'], label='G loss')
        axes[1].set_title('Training Losses'); axes[1].legend()
        axes[2].plot(self.h['G_gnorm'], label='G grad norm')
        axes[2].plot(self.h['D_gnorm'], label='D grad norm')
        axes[2].set_title('Gradient Norms'); axes[2].legend()
        plt.tight_layout(); plt.show()
```

## Training Tips and Tricks

- Label smoothing: use 0.9 instead of 1.0 for real targets to prevent discriminator overconfidence
- Add annealed Gaussian noise to D inputs — start std=0.1 and decay to 0 over training
- Spectral normalization on D weights enforces a Lipschitz constraint without batch statistics
- Avoid BatchNorm in D — it couples samples across the batch; use InstanceNorm or no norm
- Use Adam with beta1=0.5 (not default 0.9) — lower momentum prevents oscillation in GAN training
- Monitor FID every 5,000–10,000 steps; use FID plateau not loss plateau as stopping criterion
- Save G checkpoints frequently — GAN training can degrade after reaching a good state

## GANs vs Diffusion Models

GANs generate samples in a single forward pass (milliseconds per image), making them fast at inference. Diffusion models require hundreds of denoising steps (seconds per image) but are easier to train, more stable, produce more diverse outputs, and dominate FID benchmarks on unconditional image generation as of 2024. GANs remain competitive in video generation, super-resolution, and real-time applications where inference latency is critical. WGAN-GP and StyleGAN2 represent the frontier of GAN quality.

