---
title: "YaRN: Yet Another RoPE Extension Method"
slug: "yarn-rope-extension"
description: "A piecewise RoPE scaling strategy that applies different scaling to different frequency bands — no interpolation for high-frequency, linear for mid-frequency, NTK for low-frequency — achieving state-of-the-art long context with minimal fine-tuning."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiWWFSTiAoWWV0IEFub3RoZXIgUm9QRSBleHRlbnNpb047IFBlbmcgZXQgYWwuLCAyMDIzKSBpcyB0aGUgY3VycmVudCBzdGF0ZS1vZi10aGUtYXJ0IG1ldGhvZCBmb3IgZXh0ZW5kaW5nIExMTSBjb250ZXh0IHdpbmRvd3Mgd2l0aCBtaW5pbWFsIGZpbmUtdHVuaW5nLiBXaGVyZSBsaW5lYXIgaW50ZXJwb2xhdGlvbiBhcHBsaWVzIHVuaWZvcm0gcG9zaXRpb24gY29tcHJlc3Npb24gYW5kIE5USyBzY2FsaW5nIGFwcGxpZXMgZ3JhZHVhdGVkIGJhc2UgcmVzY2FsaW5nLCBZYVJOIHRha2VzIGEgbW9yZSBwcmluY2lwbGVkIGFwcHJvYWNoOiBpdCBjbGFzc2lmaWVzIGVhY2ggUm9QRSBkaW1lbnNpb24gcGFpciBpbnRvIGEgZnJlcXVlbmN5IGJhbmQgYW5kIGFwcGxpZXMgYSBkaWZmZXJlbnQgc2NhbGluZyBzdHJhdGVneSBwZXIgYmFuZC4gSGlnaC1mcmVxdWVuY3kgZGltZW5zaW9ucyAodGhvc2Ugd2l0aCB3YXZlbGVuZ3RoIHNob3J0ZXIgdGhhbiBhIHRocmVzaG9sZCkgYXJlIGxlZnQgY29tcGxldGVseSB1bnNjYWxlZCDigJQgdGhleSBhbHJlYWR5IGV4dHJhcG9sYXRlIHdlbGwuIExvdy1mcmVxdWVuY3kgZGltZW5zaW9ucyAod2F2ZWxlbmd0aCBsb25nZXIgdGhhbiBhIHNlY29uZCB0aHJlc2hvbGQpIHJlY2VpdmUgbGluZWFyIGludGVycG9sYXRpb24uIE1pZC1mcmVxdWVuY3kgZGltZW5zaW9ucyByZWNlaXZlIGEgc21vb3RoIGJsZW5kLiBUaGlzIHBpZWNld2lzZSB0cmVhdG1lbnQsIGNvbWJpbmVkIHdpdGggYW4gYXR0ZW50aW9uIHRlbXBlcmF0dXJlIGNvcnJlY3Rpb24sIHlpZWxkcyBwZXJwbGV4aXR5IHdpdGhpbiAwLjLigJMwLjUgUFBMIG9mIGZ1bGwgcmV0cmFpbmluZyBhdCBjb250ZXh0IGxlbmd0aHMgdXAgdG8gMTI4SyB3aXRoIG9ubHkgNDAwIGZpbmUtdHVuaW5nIHN0ZXBzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJZYVJOIHdhcyBpbnRyb2R1Y2VkIGJ5IFBlbmcgZXQgYWwuICgyMDIzKSBzcGVjaWZpY2FsbHkgdG8gYWRkcmVzcyBsaW1pdGF0aW9ucyBvZiBib3RoIGxpbmVhciBpbnRlcnBvbGF0aW9uIGFuZCBOVEstYXdhcmUgc2NhbGluZy4gTGluZWFyIGludGVycG9sYXRpb24gaHVydHMgaGlnaC1mcmVxdWVuY3kgZGltZW5zaW9uczsgTlRLIHNjYWxpbmcgaXMgdGhlb3JldGljYWxseSBtb3RpdmF0ZWQgYnV0IGRvZXMgbm90IG9wdGltYWxseSBoYW5kbGUgbWlkLWZyZXF1ZW5jeSBkaW1lbnNpb25zLiBZYVJOIGludHJvZHVjZXMgdHdvIGlubm92YXRpb25zOiAoMSkgYSBwaWVjZXdpc2Ugc2NhbGluZyBmdW5jdGlvbiB0aGF0IHVzZXMgbm8gc2NhbGluZyBmb3IgaGlnaC1mcmVxdWVuY3kgZGltZW5zaW9ucyAod2F2ZWxlbmd0aCBcdTAwM2MgMs+AICogYmV0YV9mYXN0KSwgbGluZWFyIHNjYWxpbmcgZm9yIGxvdy1mcmVxdWVuY3kgZGltZW5zaW9ucyAod2F2ZWxlbmd0aCBcdTAwM2UgMs+AICogYmV0YV9zbG93KSwgYW5kIGEgc21vb3RoIHJhbXAgYmxlbmQgZm9yIG1pZC1mcmVxdWVuY3kgZGltZW5zaW9uczsgYW5kICgyKSBhbiBhdHRlbnRpb24gdGVtcGVyYXR1cmUgY29ycmVjdGlvbiB0aGF0IG11bHRpcGxpZXMgdGhlIHNvZnRtYXggdGVtcGVyYXR1cmUgYnkgMS9zcXJ0KHQpIHdoZXJlIHQgaXMgZGVyaXZlZCBmcm9tIHRoZSBzY2FsZSBmYWN0b3IuIFRvZ2V0aGVyIHRoZXNlIGlubm92YXRpb25zIGFsbG93IG1vZGVscyBsaWtlIExsYW1hLTItN0IgdG8gb3BlcmF0ZSBhdCA2NEsgb3IgMTI4SyBjb250ZXh0IHdpdGggb25seSA0MDAgZ3JhZGllbnQgc3RlcHMgb2YgZmluZS10dW5pbmcgYW5kIG5lYXItYmFzZWxpbmUgcGVycGxleGl0eS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQaWVjZXdpc2UgU2NhbGluZyBTdHJhdGVneSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvcmUgaWRlYSBvZiBZYVJOIGlzIHRoYXQgZGlmZmVyZW50IFJvUEUgZnJlcXVlbmN5IGNvbXBvbmVudHMgaGF2ZSBkaWZmZXJlbnQgb3V0LW9mLWRpc3RyaWJ1dGlvbiAoT09EKSBzZW5zaXRpdml0eS4gSGlnaC1mcmVxdWVuY3kgY29tcG9uZW50cyAobGFyZ2UgdGhldGFfaSwgc2hvcnQgd2F2ZWxlbmd0aCAyz4AvdGhldGFfaSkgbmF0dXJhbGx5IHdyYXAgYXJvdW5kIG1hbnkgdGltZXMgb3ZlciBhIGxvbmcgc2VxdWVuY2Ug4oCUIHRoZWlyIHNpbi9jb3MgdmFsdWVzIGFyZSBkZW5zZWx5IGRpc3RyaWJ1dGVkIGluIFstMSwgMV0gcmVnYXJkbGVzcyBvZiBzZXF1ZW5jZSBsZW5ndGgsIHNvIHRoZXkgZ2VuZXJhbGlzZSB3ZWxsLiBMb3ctZnJlcXVlbmN5IGNvbXBvbmVudHMgKHNtYWxsIHRoZXRhX2ksIGxvbmcgd2F2ZWxlbmd0aCkgb25seSBleGVjdXRlIGEgcGFydGlhbCByb3RhdGlvbiBvdmVyIHRoZSB0cmFpbmluZyBsZW5ndGg7IGV4dGVuZGluZyB0aGUgc2VxdWVuY2UgdG8gOHggdGhlIHRyYWluaW5nIGxlbmd0aCByZXF1aXJlcyB0aGUgbW9kZWwgdG8gaGFuZGxlIHJvdGF0aW9uIGFuZ2xlcyBpdCBoYXMgbmV2ZXIgc2Vlbi4gVGhlc2UgbG93LWZyZXF1ZW5jeSBjb21wb25lbnRzIG5lZWQgc3Ryb25nIGludGVycG9sYXRpb24uIE1pZC1mcmVxdWVuY3kgY29tcG9uZW50cyBuZWVkIGEgYmxlbmQuIFlhUk4gaW1wbGVtZW50cyB0aGlzIGluc2lnaHQgd2l0aCBhIHNtb290aCByYW1wIGZ1bmN0aW9uIGFscGhhKGkpIHRoYXQgdHJhbnNpdGlvbnMgZnJvbSAwIChwdXJlIGxpbmVhciBpbnRlcnBvbGF0aW9uKSB0byAxIChubyBpbnRlcnBvbGF0aW9uKSBhcyB3YXZlbGVuZ3RoIGRlY3JlYXNlcy4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6IlxcdGlsZGV7XFx0aGV0YX1faSA9IFxcYWxwaGEoaSlcXCxcXHRoZXRhX2kgKyAoMS1cXGFscGhhKGkpKVxcLFxcZnJhY3tcXHRoZXRhX2l9e3N9LCBcXHF1YWQgXFxhbHBoYShpKSA9IFxcbWF0aHJte2NsYW1wfVxcIVxcbGVmdChcXGZyYWN7XFxsYW1iZGFfaSAtIDJcXHBpXFxiZXRhX3tcXG1hdGhybXtzbG93fX19ezJcXHBpKFxcYmV0YV97XFxtYXRocm17ZmFzdH19IC0gXFxiZXRhX3tcXG1hdGhybXtzbG93fX0pfSxcXCwgMCxcXCwgMVxccmlnaHQpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiB0aGUgWWFSTiBmb3JtdWxhLCBsYW1iZGFfaSA9IDIqcGkvdGhldGFfaSBpcyB0aGUgd2F2ZWxlbmd0aCBvZiBkaW1lbnNpb24gcGFpciBpLiBiZXRhX2Zhc3QgYW5kIGJldGFfc2xvdyBhcmUgaHlwZXJwYXJhbWV0ZXJzIHRoYXQgZGVmaW5lIHRoZSBmcmVxdWVuY3kgYmFuZCBib3VuZGFyaWVzOyB0aGUgcGFwZXIgdXNlcyBiZXRhX2Zhc3Q9MzIgYW5kIGJldGFfc2xvdz0xIGFzIGRlZmF1bHRzLiBXaGVuIGFscGhhKGkpID0gMSwgdGhlIGRpbWVuc2lvbiBpcyBoaWdoLWZyZXF1ZW5jeSBhbmQgcmVjZWl2ZXMgbm8gc2NhbGluZzogdGhldGFfdGlsZGVfaSA9IHRoZXRhX2kuIFdoZW4gYWxwaGEoaSkgPSAwLCB0aGUgZGltZW5zaW9uIGlzIGxvdy1mcmVxdWVuY3kgYW5kIHJlY2VpdmVzIHB1cmUgbGluZWFyIGludGVycG9sYXRpb246IHRoZXRhX3RpbGRlX2kgPSB0aGV0YV9pIC8gcy4gVGhlIHNtb290aCByYW1wIGVuc3VyZXMgbm8gc2hhcnAgZGlzY29udGludWl0aWVzIGluIHRoZSBmcmVxdWVuY3kgc3BlY3RydW0uIEFuIGFsdGVybmF0aXZlIGJ1dCBlcXVpdmFsZW50IGZvcm11bGF0aW9uIGJsZW5kcyB0aGUgb3JpZ2luYWwgaW52ZXJzZSBmcmVxdWVuY3kgd2l0aCB0aGUgTlRLLXNjYWxlZCBpbnZlcnNlIGZyZXF1ZW5jeSB1c2luZyB0aGUgc2FtZSByYW1wLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZyZXF1ZW5jeSBCYW5kIENsYXNzaWZpY2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgTGxhbWEtMi03QiB3aXRoIGhlYWQgZGltZW5zaW9uIGQ9MTI4IGFuZCBiZXRhX2Zhc3Q9MzIsIGJldGFfc2xvdz0xLCB0aGUgY2xhc3NpZmljYXRpb24gYm91bmRhcmllcyBhcmU6IHdhdmVsZW5ndGggXHUwMDNjIDIqcGkqMSA9IDYuMjggKGhpZ2gtZnJlcXVlbmN5LCBubyBzY2FsaW5nKSBhbmQgd2F2ZWxlbmd0aCBcdTAwM2UgMipwaSozMiA9IDIwMSAobG93LWZyZXF1ZW5jeSwgbGluZWFyIGludGVycG9sYXRpb24pLiBEaW1lbnNpb24gcGFpcnMgMOKAkzUgaGF2ZSB3YXZlbGVuZ3RocyBpbiB0aGUgcmFuZ2UgNi4yOOKAkzQyIGFuZCBmYWxsIGluIHRoZSBoaWdoLWZyZXF1ZW5jeSByZWdpbWUgKGFscGhhIOKJiCAwLjnigJMxLjApLiBEaW1lbnNpb24gcGFpcnMgNDDigJM2MyBoYXZlIHdhdmVsZW5ndGhzIFx1MDAzZSAyMDEgYW5kIGZhbGwgaW4gdGhlIGxvdy1mcmVxdWVuY3kgcmVnaW1lIChhbHBoYSDiiYggMCkuIFRoZSBtaWQtZnJlcXVlbmN5IGJhbmQgY29udGFpbnMgZGltZW5zaW9uIHBhaXJzIDbigJMzOS4gSW1wb3J0YW50bHksIHRoZSBleGFjdCB0aHJlc2hvbGRzIGJldGFfZmFzdCBhbmQgYmV0YV9zbG93IGNhbiBiZSB0dW5lZCBmb3IgZGlmZmVyZW50IG1vZGVsIHNpemVzIGFuZCB0YXJnZXQgY29udGV4dCBsZW5ndGhzOyB0aGUgcGFwZXIgcHJvdmlkZXMgZGVmYXVsdCB2YWx1ZXMgdGhhdCB3b3JrIHdlbGwgYWNyb3NzIExsYW1hLTItN0IgdGhyb3VnaCA3MEIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG1hdGhcblxuZGVmIHlhcm5fcm9wZShkaW06IGludCwgc2VxX2xlbjogaW50LCBzY2FsZTogZmxvYXQsXG4gICAgICAgICAgICAgYmFzZTogaW50ID0gMTAwMDAsIGJldGFfZmFzdDogaW50ID0gMzIsXG4gICAgICAgICAgICAgYmV0YV9zbG93OiBpbnQgPSAxKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJZYVJOIHBpZWNld2lzZSBSb1BFOiBkaWZmZXJlbnQgc2NhbGluZyBwZXIgZnJlcXVlbmN5IGJhbmQuXG4gICAgSGlnaC1mcmVxIChzaG9ydCB3YXZlbGVuZ3RoKTogbm8gaW50ZXJwb2xhdGlvbi5cbiAgICBMb3ctZnJlcSAgKGxvbmcgd2F2ZWxlbmd0aCk6IGxpbmVhciBpbnRlcnBvbGF0aW9uLlxuICAgIE1pZC1mcmVxOiBzbW9vdGggYmxlbmQgdmlhIHJhbXAgZnVuY3Rpb24gYWxwaGEoaSkuXCJcIlwiXG4gICAgZF9oYWxmID0gdG9yY2guYXJhbmdlKDAsIGRpbSwgMikuZmxvYXQoKVxuICAgIGludl9mcmVxX29yaWcgPSAxLjAgLyAoYmFzZSAqKiAoZF9oYWxmIC8gZGltKSkgICAgIyBvcmlnaW5hbCBpbnYgZnJlcXVlbmNpZXNcbiAgICB3YXZlbGVuZ3RocyAgID0gMiAqIG1hdGgucGkgLyBpbnZfZnJlcV9vcmlnICAgICAgICAjIHBlci1kaW0gd2F2ZWxlbmd0aCAoZGltLzIsKVxuXG4gICAgIyBCYW5kIGJvdW5kYXJpZXMgaW4gd2F2ZWxlbmd0aCBzcGFjZVxuICAgIGxvID0gMiAqIG1hdGgucGkgKiBiZXRhX3Nsb3cgICAgIyBiZWxvdyBsbzogaGlnaC1mcmVxIChubyBzY2FsaW5nKVxuICAgIGhpID0gMiAqIG1hdGgucGkgKiBiZXRhX2Zhc3QgICAgIyBhYm92ZSBoaTogbG93LWZyZXEgKGxpbmVhciBpbnRlcnApXG5cbiAgICAjIFJhbXAgYWxwaGEoaSk6IDEgPSBubyBpbnRlcnBvbGF0aW9uIChoaWdoLWZyZXEpLCAwID0gZnVsbCBpbnRlcnBvbGF0aW9uIChsb3ctZnJlcSlcbiAgICBhbHBoYSA9ICgod2F2ZWxlbmd0aHMgLSBsbykgLyAoaGkgLSBsbykpLmNsYW1wKDAuMCwgMS4wKVxuXG4gICAgIyBOVEsgYmFzZSBmb3IgdGhlIGxvdy1mcmVxdWVuY3kgYmxlbmRpbmcgY29tcG9uZW50XG4gICAgbnRrX2Jhc2UgICAgID0gYmFzZSAqIChzY2FsZSAqKiAoZGltIC8gKGRpbSAtIDIpKSlcbiAgICBpbnZfZnJlcV9udGsgPSAxLjAgLyAobnRrX2Jhc2UgKiogKGRfaGFsZiAvIGRpbSkpXG5cbiAgICAjIEJsZW5kZWQgaW52ZXJzZSBmcmVxdWVuY3k6IGhpZ2gtZnJlcSBrZWVwcyBvcmlnaW5hbCwgbG93LWZyZXEgdXNlcyBOVEtcbiAgICBpbnZfZnJlcV95YXJuID0gYWxwaGEgKiBpbnZfZnJlcV9vcmlnICsgKDEuMCAtIGFscGhhKSAqIGludl9mcmVxX250a1xuXG4gICAgdCA9IHRvcmNoLmFyYW5nZShzZXFfbGVuLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgIGZyZXFzID0gdG9yY2gub3V0ZXIodCwgaW52X2ZyZXFfeWFybilcbiAgICByZXR1cm4gdG9yY2guY2F0KFtmcmVxcywgZnJlcXNdLCBkaW09LTEpXG5cbmVtYiA9IHlhcm5fcm9wZSgxMjgsIDMyNzY4LCBzY2FsZT04LjApXG5wcmludChmXCJZYVJOIGVtYiBzaGFwZToge2VtYi5zaGFwZX1cIilcbnByaW50KGZcIk1heCBhbmdsZToge2VtYi5tYXgoKS5pdGVtKCk6LjNmfSB8IE1pbiBhbmdsZToge2VtYi5taW4oKS5pdGVtKCk6LjNmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRlbXBlcmF0dXJlIENvcnJlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IllhUk4gaW50cm9kdWNlcyBhIHNlY29uZCBpbm5vdmF0aW9uOiBhdHRlbnRpb24gdGVtcGVyYXR1cmUgY29ycmVjdGlvbi4gV2hlbiBjb250ZXh0IGxlbmd0aCBpbmNyZWFzZXMsIHRoZSBhdHRlbnRpb24gZGlzdHJpYnV0aW9uIG92ZXIgYSBsb25nZXIga2V5IHNlcXVlbmNlIGJlY29tZXMgbW9yZSBkaWZmdXNlIOKAlCBlYWNoIHF1ZXJ54oCZcyBhdHRlbnRpb24gaXMgc3ByZWFkIG92ZXIgbW9yZSB0b2tlbnMsIHJlZHVjaW5nIHRoZSBhdmVyYWdlIGF0dGVudGlvbiB3ZWlnaHQgcGVyIHRva2VuLiBUaGlzIHNvZnRlbmluZyBvZiBhdHRlbnRpb24gY2FuIGNhdXNlIHRoZSBtb2RlbCB0byBsb3NlIGZvY3VzIG9uIHRoZSBtb3N0IHJlbGV2YW50IGNvbnRleHQuIFlhUk4gYWRkcmVzc2VzIHRoaXMgYnkgbXVsdGlwbHlpbmcgdGhlIGF0dGVudGlvbiBzY2FsZSBmYWN0b3IgYnkgMS9zcXJ0KHQpLCB3aGVyZSB0ID0gMC4xICogbG4oc2NhbGUpICsgMS4wLiBUaGlzIHNocmlua3MgdGhlIHNvZnRtYXggZGVub21pbmF0b3IsIHNoYXJwZW5pbmcgdGhlIGF0dGVudGlvbiBkaXN0cmlidXRpb24gdG8gY29tcGVuc2F0ZSBmb3IgdGhlIGxvbmdlciBjb250ZXh0LiBBdCBzY2FsZT0xIChvcmlnaW5hbCBjb250ZXh0KSwgdD0xIGFuZCB0aGUgY29ycmVjdGlvbiBpcyBuZXV0cmFsLiBBdCBzY2FsZT04LCB0IOKJiCAxLjIwOCBhbmQgdGhlIGF0dGVudGlvbiBzY2FsZSBpcyByZWR1Y2VkIGJ5IGEgZmFjdG9yIG9mIDEvc3FydCgxLjIwOCkg4omIIDAuOTEuIFRoZSBjb3JyZWN0aW9uIGlzIGFwcGxpZWQgdW5pZm9ybWx5IGFjcm9zcyBhbGwgaGVhZHMgYW5kIGxheWVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbWF0aFxuZnJvbSB0eXBpbmcgaW1wb3J0IE9wdGlvbmFsXG5cbmRlZiByb3RhdGVfaGFsZih4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIGhhbGYgPSB4LnNoYXBlWy0xXSAvLyAyXG4gICAgcmV0dXJuIHRvcmNoLmNhdChbLXhbLi4uLCBoYWxmOl0sIHhbLi4uLCA6aGFsZl1dLCBkaW09LTEpXG5cbmRlZiBhcHBseV9yb3BlKHg6IHRvcmNoLlRlbnNvciwgZnJlcXM6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgY29zID0gZnJlcXMuY29zKClbOnguc2hhcGVbLTJdLCA6eC5zaGFwZVstMV1dXG4gICAgc2luID0gZnJlcXMuc2luKClbOnguc2hhcGVbLTJdLCA6eC5zaGFwZVstMV1dXG4gICAgcmV0dXJuIHggKiBjb3MgKyByb3RhdGVfaGFsZih4KSAqIHNpblxuXG5kZWYgeWFybl9hdHRlbnRpb24ocTogdG9yY2guVGVuc29yLCBrOiB0b3JjaC5UZW5zb3IsIHY6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgIHJvcGVfZW1iOiB0b3JjaC5UZW5zb3IsIHNjYWxlOiBmbG9hdCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiWWFSTi1zdHlsZSBhdHRlbnRpb24gd2l0aCB0ZW1wZXJhdHVyZSBjb3JyZWN0aW9uIDEvc3FydCh0KS5cbiAgICBDb3VudGVyYWN0cyBhdHRlbnRpb24gZGlmZnVzaW9uIGF0IGV4dGVuZGVkIHNlcXVlbmNlIGxlbmd0aHMuXCJcIlwiXG4gICAgcV9yID0gYXBwbHlfcm9wZShxLCByb3BlX2VtYilcbiAgICBrX3IgPSBhcHBseV9yb3BlKGssIHJvcGVfZW1iKVxuICAgICMgWWFSTiB0ZW1wZXJhdHVyZTogdCBcdTAwM2U9IDEsIGluY3JlYXNlcyB3aXRoIHNjYWxlIGZhY3RvclxuICAgIHRfeWFybiAgICA9IDAuMSAqIG1hdGgubG9nKG1heChzY2FsZSwgMS4wKSkgKyAxLjBcbiAgICBhdHRuX3NjYWxlID0gMS4wIC8gKG1hdGguc3FydChxLnNoYXBlWy0xXSkgKiBtYXRoLnNxcnQodF95YXJuKSlcbiAgICBzY29yZXMgICAgPSB0b3JjaC5tYXRtdWwocV9yLCBrX3IudHJhbnNwb3NlKC0yLCAtMSkpICogYXR0bl9zY2FsZVxuICAgIHdlaWdodHMgICA9IHRvcmNoLnNvZnRtYXgoc2NvcmVzLCBkaW09LTEpXG4gICAgcmV0dXJuIHdlaWdodHMgQCB2XG5cbiMgU2hvdyB0ZW1wZXJhdHVyZSBmYWN0b3IgYWNyb3NzIHNjYWxlIGZhY3RvcnNcbnByaW50KGZcIntcdTAwMjdTY2FsZVx1MDAyNzpcdTAwM2U4fSAge1x1MDAyN3RfeWFyblx1MDAyNzpcdTAwM2U4fSAge1x1MDAyNzEvc3FydCh0KVx1MDAyNzpcdTAwM2UxMn0gIHtcdTAwMjdTdGQgMS9zcXJ0KGQpXHUwMDI3Olx1MDAzZTE1fVwiKVxuZm9yIHMgaW4gWzEuMCwgMi4wLCA0LjAsIDguMCwgMTYuMF06XG4gICAgdCA9IDAuMSAqIG1hdGgubG9nKHMpICsgMS4wIGlmIHMgXHUwMDNlIDEgZWxzZSAxLjBcbiAgICBkID0gMTI4XG4gICAgcHJpbnQoZlwie3M6XHUwMDNlOC4xZn0gIHt0Olx1MDAzZTguNGZ9ICB7MS9tYXRoLnNxcnQodCk6XHUwMDNlMTIuNmZ9ICB7MS9tYXRoLnNxcnQoZCk6XHUwMDNlMTUuNmZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiWWFSTiBGaW5lLXR1bmluZyBQcm90b2NvbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiWWFSTiBhY2hpZXZlcyBuZWFyLWZ1bGwtcmV0cmFpbiBxdWFsaXR5IHdpdGggb25seSA0MDAgZ3JhZGllbnQgc3RlcHMgb24gbG9uZyBkb2N1bWVudHMuIFRoZSByZWNvbW1lbmRlZCBmaW5lLXR1bmluZyBwcm90b2NvbCBpczogKDEpIGxvYWQgYSA0Sy1wcmV0cmFpbmVkIG1vZGVsIHdpdGggWWFSTiByb3BlX3NjYWxpbmcgY29uZmlnOyAoMikgZmluZS10dW5lIG9uIGEgZGF0YXNldCBvZiBsb25nIGRvY3VtZW50cyBzYW1wbGVkIHRvIHRoZSB0YXJnZXQgY29udGV4dCBsZW5ndGg7ICgzKSB1c2UgYSBjb3NpbmUgbGVhcm5pbmcgcmF0ZSBzY2hlZHVsZSB3aXRoIHBlYWsgTFIgPSAyZS01IChMbGFtYS0yLTdCKSBvciAxZS01IChMbGFtYS0yLTEzQik7ICg0KSBydW4gZm9yIDQwMCBzdGVwcyB3aXRoIGJhdGNoIHNpemUgMeKAkzIgcGVyIEdQVSBhbmQgZ3JhZGllbnQgYWNjdW11bGF0aW9uIHRvIDjigJMxNiBlZmZlY3RpdmUgYmF0Y2ggc2l6ZS4gVGhlIHBhcGVyIHJlcG9ydHMgdGhhdCA0MDAgc3RlcHMgb24gdGhlIFJlZFBhamFtYSBkYXRhc2V0IChzYW1wbGVkIHRvIDY0SyB0b2tlbnMpIGJyaW5ncyBMbGFtYS0yLTdCIHRvIDcuNCBQUEwgYXQgNjRLIGNvbnRleHQsIGNvbXBhcmVkIHRvIDcuMiBQUEwgZm9yIDEwMDAgc3RlcHMuIFRoZSBmaW5lLXR1bmluZyBkYXRhIG1peCBzaG91bGQgaW5jbHVkZSBkb2N1bWVudHMgYXQgdGhlIGZ1bGwgdGFyZ2V0IGxlbmd0aCDigJQgc2hvcnQgZG9jdW1lbnRzIHBhZGRlZCBvciByZXBlYXRlZCBkbyBub3QgaGVscCB0aGUgbW9kZWwgbGVhcm4gbG9uZy1yYW5nZSBkZXBlbmRlbmNpZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IExsYW1hQ29uZmlnLCBMbGFtYUZvckNhdXNhbExNLCBUcmFpbmVyLCBUcmFpbmluZ0FyZ3VtZW50c1xuZnJvbSBwZWZ0IGltcG9ydCBMb3JhQ29uZmlnLCBnZXRfcGVmdF9tb2RlbFxuXG5kZWYgc2V0dXBfeWFybl9maW5ldHVuZShcbiAgICAgICAgbW9kZWxfaWQ6IHN0ciA9IFwibWV0YS1sbGFtYS9MbGFtYS0yLTdiLWhmXCIsXG4gICAgICAgIHlhcm5fc2NhbGU6IGZsb2F0ID0gOC4wLFxuICAgICAgICB0YXJnZXRfbGVuOiBpbnQgPSAzMjc2OCkgLVx1MDAzZSBMbGFtYUZvckNhdXNhbExNOlxuICAgIFwiXCJcIkNvbmZpZ3VyZSBZYVJOLXNjYWxlZCBMbGFtYS0yIGZvciBlZmZpY2llbnQgbG9uZy1jb250ZXh0IGZpbmUtdHVuaW5nLlwiXCJcIlxuICAgIGNvbmZpZyA9IExsYW1hQ29uZmlnLmZyb21fcHJldHJhaW5lZChtb2RlbF9pZClcbiAgICBjb25maWcucm9wZV9zY2FsaW5nID0ge1xuICAgICAgICBcInR5cGVcIjogXCJ5YXJuXCIsIFwiZmFjdG9yXCI6IHlhcm5fc2NhbGUsXG4gICAgICAgIFwib3JpZ2luYWxfbWF4X3Bvc2l0aW9uX2VtYmVkZGluZ3NcIjogNDA5NlxuICAgIH1cbiAgICBjb25maWcubWF4X3Bvc2l0aW9uX2VtYmVkZGluZ3MgPSB0YXJnZXRfbGVuXG4gICAgbW9kZWwgPSBMbGFtYUZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcbiAgICAgICAgbW9kZWxfaWQsIGNvbmZpZz1jb25maWcsIHRvcmNoX2R0eXBlPXRvcmNoLmJmbG9hdDE2XG4gICAgKVxuICAgIHJldHVybiBtb2RlbFxuXG4jIFNpbXVsYXRlZCBQUEwgYXQga2V5IGNvbnRleHQgbGVuZ3RocyBiZWZvcmUgYW5kIGFmdGVyIDQwMC1zdGVwIFlhUk4gZmluZS10dW5pbmdcbmN0eF9sZW5ndGhzID0gWzQwOTYsIDgxOTIsIDE2Mzg0LCAzMjc2OF1cbmJlZm9yZV9mdCAgID0gWzYuMSwgIDguOSwgIDE3LjMsICA0Mi4xXSAgICMgemVyby1zaG90IFlhUk4gKG5vIGZpbmUtdHVuaW5nKVxuYWZ0ZXJfZnQgICAgPSBbNi4xLCAgNi41LCAgIDYuOSwgICA3LjRdICAgIyBhZnRlciA0MDAgZ3JhZGllbnQgc3RlcHNcblxucHJpbnQoZlwie1x1MDAyN0NvbnRleHRcdTAwMjc6XHUwMDNlMTB9ICB7XHUwMDI3WmVyby1zaG90IFlhUk5cdTAwMjc6XHUwMDNlMTZ9ICB7XHUwMDI3QWZ0ZXIgNDAwIHN0ZXBzXHUwMDI3Olx1MDAzZTE3fVwiKVxuZm9yIGN0eCwgYiwgYSBpbiB6aXAoY3R4X2xlbmd0aHMsIGJlZm9yZV9mdCwgYWZ0ZXJfZnQpOlxuICAgIGltcHJvdmVtZW50ID0gYiAtIGFcbiAgICBwcmludChmXCJ7Y3R4Olx1MDAzZTEwfSAge2I6XHUwMDNlMTYuMWZ9ICB7YTpcdTAwM2UxNy4xZn0gIChnYWluOiB7aW1wcm92ZW1lbnQ6LjFmfSlcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb250ZXh0IFdpbmRvdyBFeHRlbnNpb24gUmVzdWx0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFlhUk4gcGFwZXIgcmVwb3J0cyByZXN1bHRzIG9uIExsYW1hLTItN0IgYW5kIDEzQiBleHRlbmRlZCB0byA2NEsgYW5kIDEyOEsgdG9rZW5zLiBBdCA2NEsgY29udGV4dCB3aXRoIDQwMCBmaW5lLXR1bmluZyBzdGVwcywgTGxhbWEtMi03QiBhY2hpZXZlcyA3LjQgUFBMIG9uIHRoZSBQRzE5IGxvbmctZG9jdW1lbnQgYmVuY2htYXJrLCBjb21wYXJlZCB0byA4LjggUFBMIGZvciBOVEstZHluYW1pYyAoemVyby1zaG90KSBhbmQgMTQ3KyBQUEwgZm9yIG5vLXNjYWxpbmcuIFBhc3NrZXkgcmV0cmlldmFsIOKAlCBhIHN5bnRoZXRpYyB0ZXN0IHRoYXQgZW1iZWRzIGEgNS1kaWdpdCBrZXkgZGVlcCBpbiBhIGxvbmcgZG9jdW1lbnQg4oCUIGlzIHVzZWQgdG8gbWVhc3VyZSB3aGV0aGVyIHRoZSBtb2RlbCBjYW4gYWN0dWFsbHkgYWNjZXNzIGluZm9ybWF0aW9uIGF0IGFsbCBwb3NpdGlvbnMuIFlhUk4gbW9kZWxzIGFjaGlldmUgbmVhci1wZXJmZWN0IHBhc3NrZXkgcmV0cmlldmFsIChcdTAwM2U5OSUgYWNjdXJhY3kpIGF0IGFsbCBwb3NpdGlvbnMgdXAgdG8gdGhlIHRhcmdldCBjb250ZXh0IGxlbmd0aCBhZnRlciBmaW5lLXR1bmluZywgd2hpbGUgTlRLLWR5bmFtaWMgbW9kZWxzIGRlZ3JhZGUgYmVsb3cgNTAlIHJldHJpZXZhbCBhY2N1cmFjeSBhdCBwb3NpdGlvbnMgYmV5b25kIDE2Sy4gVGhlIHRlbXBlcmF0dXJlIGNvcnJlY3Rpb24gaXMgcmVzcG9uc2libGUgZm9yIHJvdWdobHkgMC4z4oCTMC41IFBQTCBpbXByb3ZlbWVudCBvdmVyIGFibGF0aW9ucyB3aXRob3V0IGl0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCByYW5kb21cbmltcG9ydCBzdHJpbmdcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplclxuXG5kZWYgcGFzc2tleV9yZXRyaWV2YWxfdGVzdChtb2RlbCwgdG9rZW5pemVyLCBkb2NfbGVuOiBpbnQgPSAzMjc2OCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIGtleV9wb3NfZnJhYzogZmxvYXQgPSAwLjUpIC1cdTAwM2UgYm9vbDpcbiAgICBcIlwiXCJFbWJlZCBhIDUtZGlnaXQgcGFzc2tleSBpbiBhIGxvbmcgZmlsbGVyIGRvY3VtZW50IGFuZCB0ZXN0IHJldHJpZXZhbC5cIlwiXCJcbiAgICBrZXkgPSBcIlwiLmpvaW4ocmFuZG9tLmNob2ljZXMoc3RyaW5nLmRpZ2l0cywgaz01KSlcbiAgICBmaWxsZXIgPSBcIlRoZSBxdWljayBicm93biBmb3gganVtcHMgb3ZlciB0aGUgbGF6eSBkb2cuIFwiICogNTAwXG4gICAgd29yZHMgID0gZmlsbGVyLnNwbGl0KClcbiAgICBpbnNlcnRfaWR4ID0gaW50KGxlbih3b3JkcykgKiBrZXlfcG9zX2ZyYWMpXG4gICAgd29yZHMuaW5zZXJ0KGluc2VydF9pZHgsIGZcIlBBU1NLRVk9e2tleX0uXCIpXG4gICAgcXVlc3Rpb24gPSBcIldoYXQgaXMgdGhlIHBhc3NrZXk/IEFuc3dlciB3aXRoIGp1c3QgdGhlIGRpZ2l0cy4gUGFzc2tleTpcIlxuICAgIHByb21wdCAgID0gXCIgXCIuam9pbih3b3JkcykgKyBcIiBcIiArIHF1ZXN0aW9uXG4gICAgaW5wdXRzICAgPSB0b2tlbml6ZXIocHJvbXB0LCByZXR1cm5fdGVuc29ycz1cInB0XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgdHJ1bmNhdGlvbj1UcnVlLCBtYXhfbGVuZ3RoPWRvY19sZW4pLnRvKG1vZGVsLmRldmljZSlcbiAgICBzZXFfaW4gICA9IGlucHV0c1tcImlucHV0X2lkc1wiXS5zaGFwZVstMV1cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgb3V0ID0gbW9kZWwuZ2VuZXJhdGUoKippbnB1dHMsIG1heF9uZXdfdG9rZW5zPTgsIGRvX3NhbXBsZT1GYWxzZSlcbiAgICBhbnN3ZXIgID0gdG9rZW5pemVyLmRlY29kZShvdXRbMCwgc2VxX2luOl0sIHNraXBfc3BlY2lhbF90b2tlbnM9VHJ1ZSlcbiAgICBjb3JyZWN0ID0ga2V5IGluIGFuc3dlclxuICAgIHByaW50KGZcInBvc19mcmFjPXtrZXlfcG9zX2ZyYWM6LjJmfSAga2V5PXtrZXl9ICBhbnN3ZXI9e2Fuc3dlcls6MTBdfSAgb2s9e2NvcnJlY3R9XCIpXG4gICAgcmV0dXJuIGNvcnJlY3QifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIHdpdGggUHJpb3IgTWV0aG9kcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiWWFSTiBpcyBzdHJpY3RseSBiZXR0ZXIgdGhhbiBsaW5lYXIgaW50ZXJwb2xhdGlvbiBhbmQgTlRLLWF3YXJlIHNjYWxpbmcgb24gbG9uZy1jb250ZXh0IGJlbmNobWFya3Mgd2hlbiBmaW5lLXR1bmluZyBpcyBhdmFpbGFibGUuIFdpdGhvdXQgZmluZS10dW5pbmcsIFlhUk7igJlzIHplcm8tc2hvdCBwZXJmb3JtYW5jZSBpcyBzbGlnaHRseSBiZXR0ZXIgdGhhbiBOVEstZHluYW1pYyAoZHVlIHRvIHRoZSBtb3JlIHByZWNpc2UgcGllY2V3aXNlIGNsYXNzaWZpY2F0aW9uKSBidXQgdGhlIGdhcCBuYXJyb3dzLiBUaGUga2V5IGFkdmFudGFnZSBvZiBZYVJOIGlzIGl0cyBiZWhhdmlvdXIgYXQgdmVyeSBsYXJnZSBzY2FsZSBmYWN0b3JzIChzPTjigJMzMik6IGl0IGNhbiBleHRlbmQgdG8gNjRL4oCTMTI4SyBjb250ZXh0IHdpdGggb25seSA0MDAgc3RlcHMgb2YgZmluZS10dW5pbmcsIHdoaWxlIGxpbmVhciBpbnRlcnBvbGF0aW9uIGFuZCBOVEsgc2NhbGluZyBkZWdyYWRlIHN1YnN0YW50aWFsbHkgYXQgdGhlc2Ugc2NhbGVzIGV2ZW4gd2l0aCBmaW5lLXR1bmluZy4gVGhlIHRlbXBlcmF0dXJlIGNvcnJlY3Rpb24gaXMgdW5pcXVlIHRvIFlhUk4gYW5kIGFjY291bnRzIGZvciBhIG1lYW5pbmdmdWwgUFBMIGltcHJvdmVtZW50LCBwYXJ0aWN1bGFybHkgb24gdGFza3MgcmVxdWlyaW5nIHRoZSBtb2RlbCB0byBhdHRlbmQgb3ZlciB2ZXJ5IGxvbmcgc3BhbnMuIEluIHByYWN0aWNlLCBZYVJOIGlzIHRoZSByZWNvbW1lbmRlZCBtZXRob2Qgd2hlbiB0aGUgdGFyZ2V0IGNvbnRleHQgaXMgMTZLKyBhbmQgYSBzbWFsbCBmaW5lLXR1bmluZyBidWRnZXQgaXMgYXZhaWxhYmxlLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJTY2FsaW5nIHR5cGUiLCJQUEwgYXQgOEsiLCJQUEwgYXQgMzJLIiwiRmluZS10dW5lIHN0ZXBzIiwiTGxhbWEtMiBzdXBwb3J0Il0sInJvd3MiOltbIkxpbmVhciBpbnRlcnBvbGF0aW9uIiwiVW5pZm9ybSBwb3NpdGlvbiAvcyIsIjguOSIsIjUyKyIsIjEwMDArIHJlY29tbWVuZGVkIiwicm9wZV9zY2FsaW5nIGxpbmVhciJdLFsiTlRLLWR5bmFtaWMiLCJHcmFkdWF0ZWQgYmFzZSBzY2FsaW5nIiwiNy44IiwiMTgrIiwiTm90IHJlcXVpcmVkICh6ZXJvLXNob3QpIiwicm9wZV9zY2FsaW5nIGR5bmFtaWMiXSxbIllhUk4gKDY0SyB0YXJnZXQpIiwiUGllY2V3aXNlIHBlci1kaW0gKyB0ZW1wIiwiNi44IiwiNy40IiwiNDAwIHN0ZXBzIiwicm9wZV9zY2FsaW5nIHlhcm4iXSxbIllhUk4gKDEyOEsgdGFyZ2V0KSIsIlBpZWNld2lzZSBwZXItZGltICsgdGVtcCIsIjcuMSIsIjcuNiIsIjQwMOKAkzEwMDAgc3RlcHMiLCJyb3BlX3NjYWxpbmcgeWFybiJdLFsiRnVsbCByZXRyYWluIGF0IDMySyIsIk4vQSAobmF0aXZlIDMySykiLCI2LjMiLCI2LjUiLCJGdWxsIHRyYWluaW5nIGJ1ZGdldCIsIk4vQSAod291bGQgbmVlZCBmdWxsIHJldHJhaW4pIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiWWFSTuKAmXMgQ29yZSBJbnNpZ2h0IiwiY29udGVudCI6IllhUk7igJlzIGtleSBpbm5vdmF0aW9uIGlzIHJlY29nbmlzaW5nIHRoYXQgZGlmZmVyZW50IFJvUEUgZnJlcXVlbmN5IGJhbmRzIGhhdmUgZnVuZGFtZW50YWxseSBkaWZmZXJlbnQgT09EIHNlbnNpdGl2aXRpZXMuIEhpZ2gtZnJlcXVlbmN5IGRpbWVuc2lvbnMgKGNhcHR1cmluZyBsb2NhbCBzeW50YXggd2l0aGluIGEgZmV3IHRva2VucykgZXh0cmFwb2xhdGUgd2VsbCBhbmQgbmVlZCBubyBpbnRlcnBvbGF0aW9uLiBMb3ctZnJlcXVlbmN5IGRpbWVuc2lvbnMgKGNhcHR1cmluZyBwb3NpdGlvbiBhY3Jvc3MgaHVuZHJlZHMgb2YgdG9rZW5zKSBhcmUgc3Ryb25nbHkgT09EIGF0IGV4dGVuZGVkIGxlbmd0aHMgYW5kIG5lZWQgbGluZWFyIGludGVycG9sYXRpb24uIFRoZSBwaWVjZXdpc2UgcmFtcCBhcHBsaWVzIHRoZSByaWdodCB0cmVhdG1lbnQgdG8gZWFjaCBiYW5kLCBnaXZpbmcgdGhlIGJlc3Qgb2YgYm90aCB3b3JsZHMuIEFkZCB0ZW1wZXJhdHVyZSBjb3JyZWN0aW9uICgxL3NxcnQodCkpIGFuZCA0MDAgZmluZS10dW5pbmcgc3RlcHMgdG8gZ2V0IHN0YXRlLW9mLXRoZS1hcnQgbG9uZy1jb250ZXh0IHBlcmZvcm1hbmNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IllhUk4gaXMgdGhlIHJlY29tbWVuZGVkIG1ldGhvZCBmb3IgZXh0ZW5kaW5nIExMTSBjb250ZXh0IHdpbmRvd3MgdG8gMTZL4oCTMTI4SyB3aGVuIGEgc21hbGwgZmluZS10dW5pbmcgYnVkZ2V0IGlzIGF2YWlsYWJsZS4gSXRzIHBpZWNld2lzZSBmcmVxdWVuY3kgYmFuZCBjbGFzc2lmaWNhdGlvbiBhdm9pZHMgdGhlIGNvcmUgZmFpbHVyZXMgb2YgbGluZWFyIGludGVycG9sYXRpb24gKGh1cnRzIGhpZ2gtZnJlcXVlbmN5IGRpbXMpIGFuZCBOVEsgc2NhbGluZyAoaW1wcmVjaXNlIG1pZC1mcmVxdWVuY3kgaGFuZGxpbmcpLiBUaGUgYXR0ZW50aW9uIHRlbXBlcmF0dXJlIGNvcnJlY3Rpb24gaXMgYSBzaW1wbGUgbXVsdGlwbGljYXRpdmUgZmFjdG9yIHRoYXQgbWVhbmluZ2Z1bGx5IGltcHJvdmVzIHBlcmZvcm1hbmNlIGF0IGxvbmcgcmFuZ2UuIFlhUk4gaXMgc3VwcG9ydGVkIG5hdGl2ZWx5IGluIEh1Z2dpbmdGYWNlIFRyYW5zZm9ybWVycyBmb3IgcmVjZW50IExsYW1hIGFuZCBNaXN0cmFsIG1vZGVscy4gVGhlIDQwMC1zdGVwIGZpbmUtdHVuaW5nIHByb3RvY29sIGlzIHByYWN0aWNhbCBldmVuIG9uIGNvbnN1bWVyIEdQVXMgdXNpbmcgUUxvUkEgb3IgZnVsbCBmaW5lLXR1bmluZyBvbiBhIHNpbmdsZSBBMTAwLiBGb3IgemVyby1zaG90IHVzZSB3aXRob3V0IGFueSBmaW5lLXR1bmluZywgTlRLLWR5bmFtaWMgaXMgcHJlZmVycmVkIGZvciBpdHMgbG93ZXIgaW1wbGVtZW50YXRpb24gY29tcGxleGl0eTsgWWFSTuKAmXMgYWR2YW50YWdlIG1haW5seSBtYW5pZmVzdHMgYWZ0ZXIgZmluZS10dW5pbmcuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQaWVjZXdpc2Ugc2NhbGluZzogbm8gaW50ZXJwb2xhdGlvbiBmb3IgaGlnaC1mcmVxIGRpbXMgKHdhdmVsZW5ndGggXHUwMDNjIDLPgMOXYmV0YV9mYXN0KSwgbGluZWFyIGZvciBsb3ctZnJlcSBkaW1zIiwiVGVtcGVyYXR1cmUgY29ycmVjdGlvbjogbXVsdGlwbHkgYXR0ZW50aW9uIHNjYWxlIGJ5IDEvc3FydCgwLjEqbG4ocykrMSkgdG8gY291bnRlcmFjdCBhdHRlbnRpb24gZGlmZnVzaW9uIiwiNDAwIGdyYWRpZW50IHN0ZXBzIG9uIGxvbmcgZG9jdW1lbnRzIGFjaGlldmVzIG5lYXItZnVsbC1yZXRyYWluIHF1YWxpdHkgYXQgNjRLIGNvbnRleHQiLCJEZWZhdWx0IGh5cGVycGFyYW1ldGVyczogYmFzZT0xMDAwMCwgYmV0YV9mYXN0PTMyLCBiZXRhX3Nsb3c9MTsgdHVuYWJsZSBwZXIgbW9kZWwgc2l6ZSIsIkh1Z2dpbmdGYWNlOiByb3BlX3NjYWxpbmc9e1x1MDAyN3R5cGVcdTAwMjc6IFx1MDAyN3lhcm5cdTAwMjcsIFx1MDAyN2ZhY3Rvclx1MDAyNzogcywgXHUwMDI3b3JpZ2luYWxfbWF4X3Bvc2l0aW9uX2VtYmVkZGluZ3NcdTAwMjc6IDQwOTZ9IiwiUGFzc2tleSByZXRyaWV2YWwgYWNjdXJhY3kgXHUwMDNlOTklIGF0IGFsbCBwb3NpdGlvbnMgdXAgdG8gdGFyZ2V0IGNvbnRleHQgYWZ0ZXIgZmluZS10dW5pbmciXX1d"
---
# YaRN: Yet Another RoPE Extension Method

YaRN (Yet Another RoPE extensioN; Peng et al., 2023) is the current state-of-the-art method for extending LLM context windows with minimal fine-tuning. Where linear interpolation applies uniform position compression and NTK scaling applies graduated base rescaling, YaRN takes a more principled approach: it classifies each RoPE dimension pair into a frequency band and applies a different scaling strategy per band. High-frequency dimensions (those with wavelength shorter than a threshold) are left completely unscaled — they already extrapolate well. Low-frequency dimensions (wavelength longer than a second threshold) receive linear interpolation. Mid-frequency dimensions receive a smooth blend. This piecewise treatment, combined with an attention temperature correction, yields perplexity within 0.2–0.5 PPL of full retraining at context lengths up to 128K with only 400 fine-tuning steps.

## Overview

YaRN was introduced by Peng et al. (2023) specifically to address limitations of both linear interpolation and NTK-aware scaling. Linear interpolation hurts high-frequency dimensions; NTK scaling is theoretically motivated but does not optimally handle mid-frequency dimensions. YaRN introduces two innovations: (1) a piecewise scaling function that uses no scaling for high-frequency dimensions (wavelength < 2π * beta_fast), linear scaling for low-frequency dimensions (wavelength > 2π * beta_slow), and a smooth ramp blend for mid-frequency dimensions; and (2) an attention temperature correction that multiplies the softmax temperature by 1/sqrt(t) where t is derived from the scale factor. Together these innovations allow models like Llama-2-7B to operate at 64K or 128K context with only 400 gradient steps of fine-tuning and near-baseline perplexity.

## Piecewise Scaling Strategy

The core idea of YaRN is that different RoPE frequency components have different out-of-distribution (OOD) sensitivity. High-frequency components (large theta_i, short wavelength 2π/theta_i) naturally wrap around many times over a long sequence — their sin/cos values are densely distributed in [-1, 1] regardless of sequence length, so they generalise well. Low-frequency components (small theta_i, long wavelength) only execute a partial rotation over the training length; extending the sequence to 8x the training length requires the model to handle rotation angles it has never seen. These low-frequency components need strong interpolation. Mid-frequency components need a blend. YaRN implements this insight with a smooth ramp function alpha(i) that transitions from 0 (pure linear interpolation) to 1 (no interpolation) as wavelength decreases.

$$\tilde{\theta}_i = \alpha(i)\,\theta_i + (1-\alpha(i))\,\frac{\theta_i}{s}, \quad \alpha(i) = \mathrm{clamp}\!\left(\frac{\lambda_i - 2\pi\beta_{\mathrm{slow}}}{2\pi(\beta_{\mathrm{fast}} - \beta_{\mathrm{slow}})},\, 0,\, 1\right)$$

In the YaRN formula, lambda_i = 2*pi/theta_i is the wavelength of dimension pair i. beta_fast and beta_slow are hyperparameters that define the frequency band boundaries; the paper uses beta_fast=32 and beta_slow=1 as defaults. When alpha(i) = 1, the dimension is high-frequency and receives no scaling: theta_tilde_i = theta_i. When alpha(i) = 0, the dimension is low-frequency and receives pure linear interpolation: theta_tilde_i = theta_i / s. The smooth ramp ensures no sharp discontinuities in the frequency spectrum. An alternative but equivalent formulation blends the original inverse frequency with the NTK-scaled inverse frequency using the same ramp.

## Frequency Band Classification

For Llama-2-7B with head dimension d=128 and beta_fast=32, beta_slow=1, the classification boundaries are: wavelength < 2*pi*1 = 6.28 (high-frequency, no scaling) and wavelength > 2*pi*32 = 201 (low-frequency, linear interpolation). Dimension pairs 0–5 have wavelengths in the range 6.28–42 and fall in the high-frequency regime (alpha ≈ 0.9–1.0). Dimension pairs 40–63 have wavelengths > 201 and fall in the low-frequency regime (alpha ≈ 0). The mid-frequency band contains dimension pairs 6–39. Importantly, the exact thresholds beta_fast and beta_slow can be tuned for different model sizes and target context lengths; the paper provides default values that work well across Llama-2-7B through 70B.

```python
import torch
import math

def yarn_rope(dim: int, seq_len: int, scale: float,
             base: int = 10000, beta_fast: int = 32,
             beta_slow: int = 1) -> torch.Tensor:
    """YaRN piecewise RoPE: different scaling per frequency band.
    High-freq (short wavelength): no interpolation.
    Low-freq  (long wavelength): linear interpolation.
    Mid-freq: smooth blend via ramp function alpha(i)."""
    d_half = torch.arange(0, dim, 2).float()
    inv_freq_orig = 1.0 / (base ** (d_half / dim))    # original inv frequencies
    wavelengths   = 2 * math.pi / inv_freq_orig        # per-dim wavelength (dim/2,)

    # Band boundaries in wavelength space
    lo = 2 * math.pi * beta_slow    # below lo: high-freq (no scaling)
    hi = 2 * math.pi * beta_fast    # above hi: low-freq (linear interp)

    # Ramp alpha(i): 1 = no interpolation (high-freq), 0 = full interpolation (low-freq)
    alpha = ((wavelengths - lo) / (hi - lo)).clamp(0.0, 1.0)

    # NTK base for the low-frequency blending component
    ntk_base     = base * (scale ** (dim / (dim - 2)))
    inv_freq_ntk = 1.0 / (ntk_base ** (d_half / dim))

    # Blended inverse frequency: high-freq keeps original, low-freq uses NTK
    inv_freq_yarn = alpha * inv_freq_orig + (1.0 - alpha) * inv_freq_ntk

    t = torch.arange(seq_len, dtype=torch.float32)
    freqs = torch.outer(t, inv_freq_yarn)
    return torch.cat([freqs, freqs], dim=-1)

emb = yarn_rope(128, 32768, scale=8.0)
print(f"YaRN emb shape: {emb.shape}")
print(f"Max angle: {emb.max().item():.3f} | Min angle: {emb.min().item():.3f}")
```

## Temperature Correction

YaRN introduces a second innovation: attention temperature correction. When context length increases, the attention distribution over a longer key sequence becomes more diffuse — each query’s attention is spread over more tokens, reducing the average attention weight per token. This softening of attention can cause the model to lose focus on the most relevant context. YaRN addresses this by multiplying the attention scale factor by 1/sqrt(t), where t = 0.1 * ln(scale) + 1.0. This shrinks the softmax denominator, sharpening the attention distribution to compensate for the longer context. At scale=1 (original context), t=1 and the correction is neutral. At scale=8, t ≈ 1.208 and the attention scale is reduced by a factor of 1/sqrt(1.208) ≈ 0.91. The correction is applied uniformly across all heads and layers.

```python
import torch
import math
from typing import Optional

def rotate_half(x: torch.Tensor) -> torch.Tensor:
    half = x.shape[-1] // 2
    return torch.cat([-x[..., half:], x[..., :half]], dim=-1)

def apply_rope(x: torch.Tensor, freqs: torch.Tensor) -> torch.Tensor:
    cos = freqs.cos()[:x.shape[-2], :x.shape[-1]]
    sin = freqs.sin()[:x.shape[-2], :x.shape[-1]]
    return x * cos + rotate_half(x) * sin

def yarn_attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor,
                  rope_emb: torch.Tensor, scale: float) -> torch.Tensor:
    """YaRN-style attention with temperature correction 1/sqrt(t).
    Counteracts attention diffusion at extended sequence lengths."""
    q_r = apply_rope(q, rope_emb)
    k_r = apply_rope(k, rope_emb)
    # YaRN temperature: t >= 1, increases with scale factor
    t_yarn    = 0.1 * math.log(max(scale, 1.0)) + 1.0
    attn_scale = 1.0 / (math.sqrt(q.shape[-1]) * math.sqrt(t_yarn))
    scores    = torch.matmul(q_r, k_r.transpose(-2, -1)) * attn_scale
    weights   = torch.softmax(scores, dim=-1)
    return weights @ v

# Show temperature factor across scale factors
print(f"{'Scale':>8}  {'t_yarn':>8}  {'1/sqrt(t)':>12}  {'Std 1/sqrt(d)':>15}")
for s in [1.0, 2.0, 4.0, 8.0, 16.0]:
    t = 0.1 * math.log(s) + 1.0 if s > 1 else 1.0
    d = 128
    print(f"{s:>8.1f}  {t:>8.4f}  {1/math.sqrt(t):>12.6f}  {1/math.sqrt(d):>15.6f}")
```

## YaRN Fine-tuning Protocol

YaRN achieves near-full-retrain quality with only 400 gradient steps on long documents. The recommended fine-tuning protocol is: (1) load a 4K-pretrained model with YaRN rope_scaling config; (2) fine-tune on a dataset of long documents sampled to the target context length; (3) use a cosine learning rate schedule with peak LR = 2e-5 (Llama-2-7B) or 1e-5 (Llama-2-13B); (4) run for 400 steps with batch size 1–2 per GPU and gradient accumulation to 8–16 effective batch size. The paper reports that 400 steps on the RedPajama dataset (sampled to 64K tokens) brings Llama-2-7B to 7.4 PPL at 64K context, compared to 7.2 PPL for 1000 steps. The fine-tuning data mix should include documents at the full target length — short documents padded or repeated do not help the model learn long-range dependencies.

```python
import torch
from transformers import LlamaConfig, LlamaForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model

def setup_yarn_finetune(
        model_id: str = "meta-llama/Llama-2-7b-hf",
        yarn_scale: float = 8.0,
        target_len: int = 32768) -> LlamaForCausalLM:
    """Configure YaRN-scaled Llama-2 for efficient long-context fine-tuning."""
    config = LlamaConfig.from_pretrained(model_id)
    config.rope_scaling = {
        "type": "yarn", "factor": yarn_scale,
        "original_max_position_embeddings": 4096
    }
    config.max_position_embeddings = target_len
    model = LlamaForCausalLM.from_pretrained(
        model_id, config=config, torch_dtype=torch.bfloat16
    )
    return model

# Simulated PPL at key context lengths before and after 400-step YaRN fine-tuning
ctx_lengths = [4096, 8192, 16384, 32768]
before_ft   = [6.1,  8.9,  17.3,  42.1]   # zero-shot YaRN (no fine-tuning)
after_ft    = [6.1,  6.5,   6.9,   7.4]   # after 400 gradient steps

print(f"{'Context':>10}  {'Zero-shot YaRN':>16}  {'After 400 steps':>17}")
for ctx, b, a in zip(ctx_lengths, before_ft, after_ft):
    improvement = b - a
    print(f"{ctx:>10}  {b:>16.1f}  {a:>17.1f}  (gain: {improvement:.1f})")
```

## Context Window Extension Results

The YaRN paper reports results on Llama-2-7B and 13B extended to 64K and 128K tokens. At 64K context with 400 fine-tuning steps, Llama-2-7B achieves 7.4 PPL on the PG19 long-document benchmark, compared to 8.8 PPL for NTK-dynamic (zero-shot) and 147+ PPL for no-scaling. Passkey retrieval — a synthetic test that embeds a 5-digit key deep in a long document — is used to measure whether the model can actually access information at all positions. YaRN models achieve near-perfect passkey retrieval (>99% accuracy) at all positions up to the target context length after fine-tuning, while NTK-dynamic models degrade below 50% retrieval accuracy at positions beyond 16K. The temperature correction is responsible for roughly 0.3–0.5 PPL improvement over ablations without it.

```python
import torch
import random
import string
from transformers import AutoModelForCausalLM, AutoTokenizer

def passkey_retrieval_test(model, tokenizer, doc_len: int = 32768,
                           key_pos_frac: float = 0.5) -> bool:
    """Embed a 5-digit passkey in a long filler document and test retrieval."""
    key = "".join(random.choices(string.digits, k=5))
    filler = "The quick brown fox jumps over the lazy dog. " * 500
    words  = filler.split()
    insert_idx = int(len(words) * key_pos_frac)
    words.insert(insert_idx, f"PASSKEY={key}.")
    question = "What is the passkey? Answer with just the digits. Passkey:"
    prompt   = " ".join(words) + " " + question
    inputs   = tokenizer(prompt, return_tensors="pt",
                         truncation=True, max_length=doc_len).to(model.device)
    seq_in   = inputs["input_ids"].shape[-1]
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=8, do_sample=False)
    answer  = tokenizer.decode(out[0, seq_in:], skip_special_tokens=True)
    correct = key in answer
    print(f"pos_frac={key_pos_frac:.2f}  key={key}  answer={answer[:10]}  ok={correct}")
    return correct
```

## Comparison with Prior Methods

YaRN is strictly better than linear interpolation and NTK-aware scaling on long-context benchmarks when fine-tuning is available. Without fine-tuning, YaRN’s zero-shot performance is slightly better than NTK-dynamic (due to the more precise piecewise classification) but the gap narrows. The key advantage of YaRN is its behaviour at very large scale factors (s=8–32): it can extend to 64K–128K context with only 400 steps of fine-tuning, while linear interpolation and NTK scaling degrade substantially at these scales even with fine-tuning. The temperature correction is unique to YaRN and accounts for a meaningful PPL improvement, particularly on tasks requiring the model to attend over very long spans. In practice, YaRN is the recommended method when the target context is 16K+ and a small fine-tuning budget is available.

| Method | Scaling type | PPL at 8K | PPL at 32K | Fine-tune steps | Llama-2 support |
| --- | --- | --- | --- | --- | --- |
| Linear interpolation | Uniform position /s | 8.9 | 52+ | 1000+ recommended | rope_scaling linear |
| NTK-dynamic | Graduated base scaling | 7.8 | 18+ | Not required (zero-shot) | rope_scaling dynamic |
| YaRN (64K target) | Piecewise per-dim + temp | 6.8 | 7.4 | 400 steps | rope_scaling yarn |
| YaRN (128K target) | Piecewise per-dim + temp | 7.1 | 7.6 | 400–1000 steps | rope_scaling yarn |
| Full retrain at 32K | N/A (native 32K) | 6.3 | 6.5 | Full training budget | N/A (would need full retrain) |

> **YaRN’s Core Insight**: YaRN’s key innovation is recognising that different RoPE frequency bands have fundamentally different OOD sensitivities. High-frequency dimensions (capturing local syntax within a few tokens) extrapolate well and need no interpolation. Low-frequency dimensions (capturing position across hundreds of tokens) are strongly OOD at extended lengths and need linear interpolation. The piecewise ramp applies the right treatment to each band, giving the best of both worlds. Add temperature correction (1/sqrt(t)) and 400 fine-tuning steps to get state-of-the-art long-context performance.

## Key Takeaways

YaRN is the recommended method for extending LLM context windows to 16K–128K when a small fine-tuning budget is available. Its piecewise frequency band classification avoids the core failures of linear interpolation (hurts high-frequency dims) and NTK scaling (imprecise mid-frequency handling). The attention temperature correction is a simple multiplicative factor that meaningfully improves performance at long range. YaRN is supported natively in HuggingFace Transformers for recent Llama and Mistral models. The 400-step fine-tuning protocol is practical even on consumer GPUs using QLoRA or full fine-tuning on a single A100. For zero-shot use without any fine-tuning, NTK-dynamic is preferred for its lower implementation complexity; YaRN’s advantage mainly manifests after fine-tuning.

- Piecewise scaling: no interpolation for high-freq dims (wavelength < 2π×beta_fast), linear for low-freq dims
- Temperature correction: multiply attention scale by 1/sqrt(0.1*ln(s)+1) to counteract attention diffusion
- 400 gradient steps on long documents achieves near-full-retrain quality at 64K context
- Default hyperparameters: base=10000, beta_fast=32, beta_slow=1; tunable per model size
- HuggingFace: rope_scaling={'type': 'yarn', 'factor': s, 'original_max_position_embeddings': 4096}
- Passkey retrieval accuracy >99% at all positions up to target context after fine-tuning

