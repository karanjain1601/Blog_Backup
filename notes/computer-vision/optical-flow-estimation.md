---
title: "Optical Flow Estimation: Classical and Deep Learning Approaches"
slug: "optical-flow-estimation"
description: ""
tags: [""]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPcHRpY2FsIGZsb3cgaXMgdGhlIGFwcGFyZW50IG1vdGlvbiBvZiBpbWFnZSBwaXhlbHMgYmV0d2VlbiBjb25zZWN1dGl2ZSB2aWRlbyBmcmFtZXMgY2F1c2VkIGJ5IG1vdmVtZW50IG9mIG9iamVjdHMgb3IgdGhlIGNhbWVyYS4gRGVuc2Ugb3B0aWNhbCBmbG93IGVzdGltYXRlcyBhIDJEIGRpc3BsYWNlbWVudCB2ZWN0b3IgZm9yIGV2ZXJ5IHBpeGVsLCB5aWVsZGluZyBhIGZsb3cgZmllbGQgdGhhdCBjYXB0dXJlcyB3aGVyZSBlYWNoIHBpeGVsIG1vdmVkLiBJdCBzZXJ2ZXMgYXMgYSBmb3VuZGF0aW9uYWwgcHJpbWl0aXZlIGZvciBhY3Rpb24gcmVjb2duaXRpb24sIG9iamVjdCB0cmFja2luZywgdmlkZW8gc3RhYmlsaXphdGlvbiwgYW5kIGZyYW1lIGludGVycG9sYXRpb24gdGFza3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFzc2ljYWwgbWV0aG9kcyByZWx5IG9uIGJyaWdodG5lc3MgY29uc3RhbmN5IGFuZCBzcGF0aWFsIHNtb290aG5lc3MgdG8gc29sdmUgYW4gdW5kZXJkZXRlcm1pbmVkIHN5c3RlbS4gRGVlcCBsZWFybmluZyBhcHByb2FjaGVzIGxlYXJuIHJpY2ggZmVhdHVyZSByZXByZXNlbnRhdGlvbnMsIHJlcGxhY2luZyBoYW5kLWNyYWZ0ZWQgYXNzdW1wdGlvbnMgd2l0aCBsZWFybmVkIHByaW9ycy4gU2luY2UgRmxvd05ldCAoMjAxNSksIHRoZSBnYXAgaGFzIGdyb3duIGRyYW1hdGljYWxseSDigJQgbW9kZXJuIG5ldHdvcmtzIGxpa2UgUkFGVCBhY2hpZXZlIGVuZHBvaW50IGVycm9ycyBiZWxvdyAxLjUgcGl4ZWxzIG9uIFNpbnRlbCBDbGVhbiwgc3VycGFzc2luZyBhbGwgY2xhc3NpY2FsIG1ldGhvZHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTHVjYXMtS2FuYWRlIGFuZCBIb3JuLVNjaHVuY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikx1Y2FzLUthbmFkZSBhc3N1bWVzIGJyaWdodG5lc3MgY29uc3RhbmN5OiBJKHgseSx0KSA9IEkoeCt1LHkrdix0KzEpLiBBIGxpbmVhcml6YXRpb24geWllbGRzIHRoZSBvcHRpY2FsIGZsb3cgY29uc3RyYWludCBJeMK3dSArIEl5wrd2ICsgSXQgPSAwIOKAlCBvbmUgZXF1YXRpb24gaW4gdHdvIHVua25vd25zLiBTcGF0aWFsIGNvaGVyZW5jZSByZXNvbHZlcyB0aGlzOiBwaXhlbHMgaW4gYSBzbWFsbCBwYXRjaCBzaGFyZSBvbmUgZmxvdyB2ZWN0b3IuIFN0YWNraW5nIE4gcGF0Y2ggZXF1YXRpb25zIGdpdmVzIGFuIG92ZXJkZXRlcm1pbmVkIHN5c3RlbSBzb2x2ZWQgdmlhIHdlaWdodGVkIGxlYXN0IHNxdWFyZXMgdXNpbmcgdGhlIGltYWdlIHN0cnVjdHVyZSB0ZW5zb3IuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgY3YyXG5cbmRlZiBsdWNhc19rYW5hZGUoSTEsIEkyLCBwdHMsIHdpbj03KTpcbiAgICBJeCA9IGN2Mi5Tb2JlbChJMSwgY3YyLkNWXzY0RiwgMSwgMClcbiAgICBJeSA9IGN2Mi5Tb2JlbChJMSwgY3YyLkNWXzY0RiwgMCwgMSlcbiAgICBJdCA9IEkyLmFzdHlwZShmbG9hdCkgLSBJMS5hc3R5cGUoZmxvYXQpXG4gICAgZmxvd3MgPSBbXVxuICAgIGZvciB4LCB5IGluIHB0czpcbiAgICAgICAgc2wgPSBucC5zX1t5LXdpbjp5K3dpbisxLCB4LXdpbjp4K3dpbisxXVxuICAgICAgICBBID0gbnAuc3RhY2soW0l4W3NsXS5yYXZlbCgpLCBJeVtzbF0ucmF2ZWwoKV0sIDEpXG4gICAgICAgIGIgPSAtSXRbc2xdLnJhdmVsKClcbiAgICAgICAgdSwgdiA9IG5wLmxpbmFsZy5sc3RzcShBLCBiLCByY29uZD1Ob25lKVswXVxuICAgICAgICBmbG93cy5hcHBlbmQoKHUsIHYpKVxuICAgIHJldHVybiBmbG93cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSG9ybi1TY2h1bmNrIG1pbmltaXplcyBhIGdsb2JhbCBlbmVyZ3k6IM674oirKEl4wrd1ICsgSXnCt3YgKyBJdCnCsiArIHziiId1fMKyICsgfOKIh3Z8wrIgZM6pLiBUaGUgcmVndWxhcml6YXRpb24gdGVybSBwZW5hbGl6ZXMgbGFyZ2UgZmxvdyBncmFkaWVudHMsIHByb2R1Y2luZyBnbG9iYWxseSBzbW9vdGggZmxvdyBmaWVsZHMuIFRoaXMgaGFuZGxlcyB0aGUgYXBlcnR1cmUgcHJvYmxlbSBlbGVnYW50bHkgYnV0IG92ZXItc21vb3RocyBtb3Rpb24gYm91bmRhcmllcy4gQm90aCBMSyBhbmQgSFMgZmFpbCBvbiBsYXJnZSBkaXNwbGFjZW1lbnRzIGJlY2F1c2UgbGluZWFyaXphdGlvbiBvZiBicmlnaHRuZXNzIGNvbnN0YW5jeSBvbmx5IGhvbGRzIGZvciBzdWItcGl4ZWwgbW90aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZsb3dOZXQgYW5kIExlYXJuaW5nLUJhc2VkIEZsb3cifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZsb3dOZXQgKDIwMTUpIHdhcyB0aGUgZmlyc3QgZW5kLXRvLWVuZCBDTk4gZm9yIG9wdGljYWwgZmxvdyBlc3RpbWF0aW9uLiBJdCBpbnRyb2R1Y2VkIHR3byBkZXNpZ25zOiBGbG93TmV0UyAoc2ltcGxlIGVuY29kZXItZGVjb2RlcikgYW5kIEZsb3dOZXRDICh3aXRoIGEgY29ycmVsYXRpb24gbGF5ZXIgY29tcHV0aW5nIGZlYXR1cmUgZG90IHByb2R1Y3RzIGFjcm9zcyBzcGF0aWFsIG9mZnNldHMpLiBUaGUgY29ycmVsYXRpb24gbGF5ZXIgYnVpbGRzIGEgY29zdCB2b2x1bWUgY29tcGFyaW5nIGZlYXR1cmVzIGZyb20gYm90aCBmcmFtZXMsIHRoZW4gZGVjb2RlZCBpbnRvIGEgZGVuc2UgZmxvdyBmaWVsZCB1c2luZyBzdHJpZGVkIGNvbnZvbHV0aW9ucyBhbmQgc2tpcCBjb25uZWN0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGNvcnJlbGF0aW9uX2xheWVyKGYxLCBmMiwgbWF4X2Rpc3A9NCk6XG4gICAgQiwgQywgSCwgVyA9IGYxLnNoYXBlXG4gICAgRCA9IDIgKiBtYXhfZGlzcCArIDFcbiAgICBmMl9wYWQgPSBGLnBhZChmMiwgW21heF9kaXNwXSo0KVxuICAgIGNvc3QgPSB0b3JjaC56ZXJvcyhCLCBEKkQsIEgsIFcsIGRldmljZT1mMS5kZXZpY2UpXG4gICAgZm9yIGksIGRoIGluIGVudW1lcmF0ZShyYW5nZSgtbWF4X2Rpc3AsIG1heF9kaXNwKzEpKTpcbiAgICAgICAgZm9yIGosIGR3IGluIGVudW1lcmF0ZShyYW5nZSgtbWF4X2Rpc3AsIG1heF9kaXNwKzEpKTpcbiAgICAgICAgICAgIGYycyA9IGYyX3BhZFs6LCA6LCBkaCttYXhfZGlzcDpkaCttYXhfZGlzcCtILFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGR3K21heF9kaXNwOmR3K21heF9kaXNwK1ddXG4gICAgICAgICAgICBjb3N0WzosIGkqRCtqXSA9IChmMSAqIGYycykuc3VtKDEpXG4gICAgcmV0dXJuIGNvc3QgLyBDIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGbG93TmV0MiBzdGFja3MgbXVsdGlwbGUgRmxvd05ldCBtb2R1bGVzIHdpdGggd2FycGluZzogdGhlIHNlY29uZCBtb2R1bGUgcmVjZWl2ZXMgZnJhbWUyIHdhcnBlZCBieSB0aGUgZmlyc3QgZmxvdyBlc3RpbWF0ZSwgcmVmaW5pbmcgcmVzaWR1YWwgZmxvdy4gU3B5TmV0IGludHJvZHVjZWQgc3BhdGlhbCBweXJhbWlkIG5ldHdvcmtzIGNvbXB1dGluZyBmbG93IGNvYXJzZS10by1maW5lIHVzaW5nIG9ubHkgMS4yTSBwYXJhbWV0ZXJzLiBQV0NOZXQgY29tYmluZWQgcHlyYW1pZCB3YXJwaW5nIHdpdGggYSBjb3N0IHZvbHVtZSBhbmQgY29udGV4dCBuZXR3b3JrcywgYWNoaWV2aW5nIGFjY3VyYWN5IG5lYXIgRmxvd05ldDIgYXQgdGVuIHRpbWVzIGxvd2VyIGNvbXB1dGF0aW9uYWwgY29zdC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSQUZUOiBSZWN1cnJlbnQgQWxsLVBhaXJzIEZsb3cifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJBRlQgKFRlZWQgXHUwMDI2IERlbmcsIE5ldXJJUFMgMjAyMCkgYnVpbGRzIGEgNC1sZXZlbCBmZWF0dXJlIHB5cmFtaWQgZnJvbSBlYWNoIGlucHV0IGltYWdlIHVzaW5nIGEgc2hhcmVkIGVuY29kZXIuIEl0IGNvbnN0cnVjdHMgYW4gYWxsLXBhaXJzIGNvcnJlbGF0aW9uIHZvbHVtZSBieSBjb21wdXRpbmcgZG90IHByb2R1Y3RzIGJldHdlZW4gZXZlcnkgcGFpciBvZiBwaXhlbHMgaW4gdGhlIHR3byBmZWF0dXJlIG1hcHMuIEEgcmVjdXJyZW50IEdSVS1iYXNlZCB1cGRhdGUgb3BlcmF0b3IgdGhlbiBpdGVyYXRpdmVseSByZWZpbmVzIGEgZmxvdyBmaWVsZCBlc3RpbWF0ZSwgbG9va2luZyB1cCBmcm9tIHRoZSBjb3JyZWxhdGlvbiBweXJhbWlkIGF0IGVhY2ggaXRlcmF0aW9uIHN0ZXAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiZGVmIHJhZnRfZm9yd2FyZChpbWcxLCBpbWcyLCBpdGVycz0xMik6XG4gICAgZm1hcDEgPSBmZWF0dXJlX2VuY29kZXIoaW1nMSlcbiAgICBmbWFwMiA9IGZlYXR1cmVfZW5jb2RlcihpbWcyKVxuICAgIGNvcnJfcHlyYW1pZCA9IGJ1aWxkX2NvcnJfcHlyYW1pZChmbWFwMSwgZm1hcDIsIGxldmVscz00KVxuICAgIGNvbnRleHQgPSBjb250ZXh0X2VuY29kZXIoaW1nMSlcbiAgICBuZXQsIGlucCA9IGNvbnRleHQuc3BsaXQoW2hpZGRlbl9kaW0sIGlucF9kaW1dLCBkaW09MSlcbiAgICBmbG93ID0gdG9yY2guemVyb3MoQiwgMiwgSC8vOCwgVy8vOCwgZGV2aWNlPWltZzEuZGV2aWNlKVxuICAgIGZsb3dfcHJlZHMgPSBbXVxuICAgIGZvciBfIGluIHJhbmdlKGl0ZXJzKTpcbiAgICAgICAgY29yciA9IGNvcnJfbG9va3VwKGZsb3csIGNvcnJfcHlyYW1pZCwgcmFkaXVzPTQpXG4gICAgICAgIG5ldCwgZGVsdGFfZmxvdyA9IGdydV91cGRhdGUobmV0LCBpbnAsIGNvcnIsIGZsb3cpXG4gICAgICAgIGZsb3cgPSBmbG93ICsgZGVsdGFfZmxvd1xuICAgICAgICBmbG93X3ByZWRzLmFwcGVuZCh1cHNhbXBsZV9mbG93KGZsb3cpKVxuICAgIHJldHVybiBmbG93X3ByZWRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSQUZUXHUwMDI3cyBhbGwtcGFpcnMgY29ycmVsYXRpb24gdm9sdW1lIGlzIGNvbXB1dGVkIG9uY2UgYW5kIGluZGV4ZWQgYXQgZWFjaCBHUlUgc3RlcCB1c2luZyBiaWxpbmVhciBpbnRlcnBvbGF0aW9uIGluIGEgbG9jYWwgcmFkaXVzIGFyb3VuZCBlYWNoIHByZWRpY3RlZCBmbG93IHZlY3Rvci4gVW5saWtlIGNhc2NhZGVkIGFyY2hpdGVjdHVyZXMgdGhhdCByZS1leHRyYWN0IGZlYXR1cmVzIHBlciBzY2FsZSwgUkFGVCBzaGFyZXMgZmVhdHVyZXMgYWNyb3NzIGFsbCBpdGVyYXRpb25zLiBUaGlzIGRlc2lnbiBlbmFibGVzIFJBRlQgdG8gZ2VuZXJhbGl6ZSB3ZWxsIHRvIHVuc2VlbiBkYXRhc2V0cyB3aXRob3V0IGZpbmUtdHVuaW5nLCB1bmxpa2UgZG9tYWluLXNwZWNpZmljIHByZWRlY2Vzc29ycy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJjb250ZW50IjoiUkFGVFx1MDAyN3Mga2V5IGlubm92YXRpb24gaXMgaXRlcmF0aXZlIHJlZmluZW1lbnQgdmlhIGEgR1JVIOKAlCBpdCB1cGRhdGVzIGZsb3cgZXN0aW1hdGVzIDEyIHRpbWVzIHVzaW5nIGEgNC1sZXZlbCBjb3JyZWxhdGlvbiBweXJhbWlkLiBFYWNoIEdSVSBzdGVwIHJlZmluZXMgdGhlIHByZXZpb3VzIGVzdGltYXRlIHJhdGhlciB0aGFuIHByZWRpY3RpbmcgZmxvdyBmcm9tIHNjcmF0Y2gsIGVuYWJsaW5nIGJvdGggYWNjdXJhY3kgYW5kIGdlbmVyYWxpemF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV2YWx1YXRpb24gTWV0cmljcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW5kLVBvaW50IEVycm9yIChFUEUpIG1lYXN1cmVzIHRoZSBFdWNsaWRlYW4gZGlzdGFuY2UgYmV0d2VlbiBwcmVkaWN0ZWQgYW5kIGdyb3VuZC10cnV0aCBmbG93IHZlY3RvcnMsIGF2ZXJhZ2VkIGFjcm9zcyBhbGwgdmFsaWQgcGl4ZWxzLiBJdCBpcyB0aGUgcHJpbWFyeSBtZXRyaWMgb24gTVBJLVNpbnRlbCAoc3ludGhldGljLCBsb25nIHNlcXVlbmNlcywgbGFyZ2UgZGlzcGxhY2VtZW50cykgYW5kIEtJVFRJIChyZWFsLXdvcmxkIGRyaXZpbmcpLiBFUEUgaXMgcmVwb3J0ZWQgc2VwYXJhdGVseSBvbiBTaW50ZWwgQ2xlYW4gKG5vIHJlbmRlcmluZyBlZmZlY3RzKSBhbmQgU2ludGVsIEZpbmFsIChhdG1vc3BoZXJpYyBlZmZlY3RzIGluY2x1ZGluZyBtb3Rpb24gYmx1ciBhbmQgZm9nKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGV2YWx1YXRlX2Zsb3cocHJlZF9mbG93LCBndF9mbG93LCB2YWxpZF9tYXNrPU5vbmUpOlxuICAgIGRpZmYgPSBwcmVkX2Zsb3cgLSBndF9mbG93XG4gICAgZXBlID0gZGlmZi5ub3JtKGRpbT0xKSAgICAgICAgICAgICAgICAgICAgIyAoQiwgSCwgVylcbiAgICBndF9tYWcgPSBndF9mbG93Lm5vcm0oZGltPTEpLmNsYW1wKG1pbj0xZS02KVxuICAgIGZsX21hc2sgPSAoZXBlIFx1MDAzZSAzLjApIFx1MDAyNiAoZXBlIC8gZ3RfbWFnIFx1MDAzZSAwLjA1KVxuICAgIGlmIHZhbGlkX21hc2sgaXMgbm90IE5vbmU6XG4gICAgICAgIGVwZSA9IGVwZVt2YWxpZF9tYXNrXVxuICAgICAgICBmbF9tYXNrID0gZmxfbWFza1t2YWxpZF9tYXNrXVxuICAgIHByaW50KGZcIkVQRT17ZXBlLm1lYW4oKTouMmZ9ICBGbD17ZmxfbWFzay5mbG9hdCgpLm1lYW4oKTouM2Z9XCIpXG4gICAgcmV0dXJuIGVwZS5tZWFuKCkuaXRlbSgpLCBmbF9tYXNrLmZsb2F0KCkubWVhbigpLml0ZW0oKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEZsIChmbG93IG91dGxpZXIpIG1ldHJpYyBmcm9tIEtJVFRJIGNvdW50cyBwaXhlbHMgd2hlcmUgRVBFIGV4Y2VlZHMgMyBweCBBTkQgcmVsYXRpdmUgZXJyb3IgZXhjZWVkcyA1JSBvZiB0aGUgZ3JvdW5kLXRydXRoIG1hZ25pdHVkZS4gVGhpcyB0aHJlc2hvbGQtYmFzZWQgbWV0cmljIGlzIHJvYnVzdCB0byBsYXJnZSBtb3Rpb24gbWFnbml0dWRlcyBhbmQgbWVhc3VyZXMgY2F0YXN0cm9waGljIGZhaWx1cmVzIHJhdGhlciB0aGFuIGF2ZXJhZ2UgYWNjdXJhY3kuIEtJVFRJIGZ1cnRoZXIgc3BsaXRzIEZsIGludG8gRmwtYmcgKHN0YXRpYyBiYWNrZ3JvdW5kKSBhbmQgRmwtZmcgKGR5bmFtaWMgZm9yZWdyb3VuZCkgdG8gYW5hbHl6ZSBwZXItcmVnaW9uIGZhaWx1cmUgbW9kZXMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlR5cGUiLCJTaW50ZWwgQ2xlYW4gRVBFIiwiU2ludGVsIEZpbmFsIEVQRSIsIktJVFRJIEZsICUiLCJTcGVlZCAobXMpIl0sInJvd3MiOltbIkxLIiwiQ2xhc3NpY2FsIiwiNy40MCIsIjguOTAiLCLigJQiLCIxNSJdLFsiRXBpY0Zsb3ciLCJDbGFzc2ljYWwrQ05OIiwiNC4xMiIsIjYuMjkiLCIyNi4zIiwiMjgwIl0sWyJGbG93TmV0MiIsIkNOTiIsIjEuNDUiLCIzLjk2IiwiMTEuNSIsIjEyMCJdLFsiUFdDTmV0IiwiQ05OIiwiMi41NSIsIjMuOTMiLCI5LjYwIiwiMzUiXSxbIlJBRlQiLCJSTk4iLCIxLjQzIiwiMi43MSIsIjUuMTAiLCIxNjAiXSxbIkZsb3dGb3JtZXIiLCJUcmFuc2Zvcm1lciIsIjEuMDEiLCIyLjQwIiwiNC4wOSIsIjE4MCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BhcnNlLXRvLWRlbnNlIGV2b2x1dGlvbjogb3B0aWNhbCBmbG93IHJlc2VhcmNoIHByb2dyZXNzZWQgZnJvbSBzcGFyc2UgZmVhdHVyZSB0cmFja2luZyAoS0xUKSB0byBkZW5zZSBjbGFzc2ljYWwgZXN0aW1hdGlvbiAoTEssIEhTKSB0byBsZWFybmVkIGNvc3Qtdm9sdW1lIG1ldGhvZHMgKEZsb3dOZXQsIFBXQ05ldCkgdG8gaXRlcmF0aXZlIHJlZmluZW1lbnQgKFJBRlQpLiBFYWNoIGdlbmVyYXRpb24gaW1wcm92ZWQgYWNjdXJhY3kgcm91Z2hseSAyw5cgb24gU2ludGVsLCBzaG93aW5nIHRoYXQgYXJjaGl0ZWN0dXJhbCBpbm5vdmF0aW9ucyBjb21wb3VuZCBvdmVyIHRpbWUgaW4gZGVuc2Ugc3BhdGlvdGVtcG9yYWwgZXN0aW1hdGlvbiBwcm9ibGVtcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvcnJlbGF0aW9uIHZvbHVtZXMgYXJlIHRoZSBrZXkgZGlmZmVyZW50aWF0b3IgYmV0d2VlbiBjbGFzc2ljYWwgYW5kIGxlYXJuZWQgZmxvdyBtZXRob2RzLiBDbGFzc2ljYWwgbWV0aG9kcyBjb21wdXRlIGNvcnJlbGF0aW9uIG92ZXIgcmF3IHBpeGVsIHBhdGNoZXM7IGxlYXJuZWQgbWV0aG9kcyBjb21wdXRlIGl0IG92ZXIgZGVlcCBmZWF0dXJlIG1hcHMuIFJBRlRcdTAwMjdzIGFsbC1wYWlycyBjb3JyZWxhdGlvbiDigJQgTyhOwrIpIGluIHBpeGVsIGNvdW50IGJ1dCBjb21wdXRlZCBvbmNlIOKAlCBlbmFibGVzIHJpY2hlciBtYXRjaGluZyB0aGFuIHNsaWRpbmctd2luZG93IGFwcHJvYWNoZXMgYW5kIGRyaXZlcyBpdHMgc3RhdGUtb2YtdGhlLWFydCBhY2N1cmFjeSBvbiBhbGwgc3RhbmRhcmQgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJlbmNobWFyayBvdmVyZml0dGluZyByZW1haW5zIGEgY29uY2VybjogbW9kZWxzIHRyYWluZWQgb24gRmx5aW5nQ2hhaXJzIGFuZCBGbHlpbmdUaGluZ3MzRCBtYXkgbm90IGdlbmVyYWxpemUgdG8gcmVhbCB2aWRlby4gUkFGVCBtaXRpZ2F0ZXMgdGhpcyB2aWEgaXRlcmF0aXZlIHJlZmluZW1lbnQgYW5kIHdlaWdodCBzaGFyaW5nLCBidXQgdGhlIGRvbWFpbiBnYXAgYmV0d2VlbiBzeW50aGV0aWMgdHJhaW5pbmcgZGF0YSBhbmQgcmVhbCBkZXBsb3ltZW50IHBlcnNpc3RzLiBTaW50ZWwtRmluYWwgY29ycmVsYXRlcyBiZXR0ZXIgd2l0aCByZWFsLXdvcmxkIHBlcmZvcm1hbmNlIHRoYW4gU2ludGVsLUNsZWFuIGR1ZSB0byBpdHMgcmVhbGlzdGljIHJlbmRlcmluZyBlZmZlY3RzLiJ9XQ=="
---
# Optical Flow Estimation: Classical and Deep Learning Approaches

## Overview

Optical flow is the apparent motion of image pixels between consecutive video frames caused by movement of objects or the camera. Dense optical flow estimates a 2D displacement vector for every pixel, yielding a flow field that captures where each pixel moved. It serves as a foundational primitive for action recognition, object tracking, video stabilization, and frame interpolation tasks.

Classical methods rely on brightness constancy and spatial smoothness to solve an underdetermined system. Deep learning approaches learn rich feature representations, replacing hand-crafted assumptions with learned priors. Since FlowNet (2015), the gap has grown dramatically — modern networks like RAFT achieve endpoint errors below 1.5 pixels on Sintel Clean, surpassing all classical methods.

## Lucas-Kanade and Horn-Schunck

Lucas-Kanade assumes brightness constancy: I(x,y,t) = I(x+u,y+v,t+1). A linearization yields the optical flow constraint Ix·u + Iy·v + It = 0 — one equation in two unknowns. Spatial coherence resolves this: pixels in a small patch share one flow vector. Stacking N patch equations gives an overdetermined system solved via weighted least squares using the image structure tensor.

```
import numpy as np
import cv2

def lucas_kanade(I1, I2, pts, win=7):
    Ix = cv2.Sobel(I1, cv2.CV_64F, 1, 0)
    Iy = cv2.Sobel(I1, cv2.CV_64F, 0, 1)
    It = I2.astype(float) - I1.astype(float)
    flows = []
    for x, y in pts:
        sl = np.s_[y-win:y+win+1, x-win:x+win+1]
        A = np.stack([Ix[sl].ravel(), Iy[sl].ravel()], 1)
        b = -It[sl].ravel()
        u, v = np.linalg.lstsq(A, b, rcond=None)[0]
        flows.append((u, v))
    return flows
```

Horn-Schunck minimizes a global energy: λ∫(Ix·u + Iy·v + It)² + |∇u|² + |∇v|² dΩ. The regularization term penalizes large flow gradients, producing globally smooth flow fields. This handles the aperture problem elegantly but over-smooths motion boundaries. Both LK and HS fail on large displacements because linearization of brightness constancy only holds for sub-pixel motion.

## FlowNet and Learning-Based Flow

FlowNet (2015) was the first end-to-end CNN for optical flow estimation. It introduced two designs: FlowNetS (simple encoder-decoder) and FlowNetC (with a correlation layer computing feature dot products across spatial offsets). The correlation layer builds a cost volume comparing features from both frames, then decoded into a dense flow field using strided convolutions and skip connections.

```
import torch
import torch.nn.functional as F

def correlation_layer(f1, f2, max_disp=4):
    B, C, H, W = f1.shape
    D = 2 * max_disp + 1
    f2_pad = F.pad(f2, [max_disp]*4)
    cost = torch.zeros(B, D*D, H, W, device=f1.device)
    for i, dh in enumerate(range(-max_disp, max_disp+1)):
        for j, dw in enumerate(range(-max_disp, max_disp+1)):
            f2s = f2_pad[:, :, dh+max_disp:dh+max_disp+H,
                               dw+max_disp:dw+max_disp+W]
            cost[:, i*D+j] = (f1 * f2s).sum(1)
    return cost / C
```

FlowNet2 stacks multiple FlowNet modules with warping: the second module receives frame2 warped by the first flow estimate, refining residual flow. SpyNet introduced spatial pyramid networks computing flow coarse-to-fine using only 1.2M parameters. PWCNet combined pyramid warping with a cost volume and context networks, achieving accuracy near FlowNet2 at ten times lower computational cost.

## RAFT: Recurrent All-Pairs Flow

RAFT (Teed & Deng, NeurIPS 2020) builds a 4-level feature pyramid from each input image using a shared encoder. It constructs an all-pairs correlation volume by computing dot products between every pair of pixels in the two feature maps. A recurrent GRU-based update operator then iteratively refines a flow field estimate, looking up from the correlation pyramid at each iteration step.

```
def raft_forward(img1, img2, iters=12):
    fmap1 = feature_encoder(img1)
    fmap2 = feature_encoder(img2)
    corr_pyramid = build_corr_pyramid(fmap1, fmap2, levels=4)
    context = context_encoder(img1)
    net, inp = context.split([hidden_dim, inp_dim], dim=1)
    flow = torch.zeros(B, 2, H//8, W//8, device=img1.device)
    flow_preds = []
    for _ in range(iters):
        corr = corr_lookup(flow, corr_pyramid, radius=4)
        net, delta_flow = gru_update(net, inp, corr, flow)
        flow = flow + delta_flow
        flow_preds.append(upsample_flow(flow))
    return flow_preds
```

RAFT's all-pairs correlation volume is computed once and indexed at each GRU step using bilinear interpolation in a local radius around each predicted flow vector. Unlike cascaded architectures that re-extract features per scale, RAFT shares features across all iterations. This design enables RAFT to generalize well to unseen datasets without fine-tuning, unlike domain-specific predecessors.

> **info**: RAFT's key innovation is iterative refinement via a GRU — it updates flow estimates 12 times using a 4-level correlation pyramid. Each GRU step refines the previous estimate rather than predicting flow from scratch, enabling both accuracy and generalization.

## Evaluation Metrics

End-Point Error (EPE) measures the Euclidean distance between predicted and ground-truth flow vectors, averaged across all valid pixels. It is the primary metric on MPI-Sintel (synthetic, long sequences, large displacements) and KITTI (real-world driving). EPE is reported separately on Sintel Clean (no rendering effects) and Sintel Final (atmospheric effects including motion blur and fog).

```
import torch

def evaluate_flow(pred_flow, gt_flow, valid_mask=None):
    diff = pred_flow - gt_flow
    epe = diff.norm(dim=1)                    # (B, H, W)
    gt_mag = gt_flow.norm(dim=1).clamp(min=1e-6)
    fl_mask = (epe > 3.0) & (epe / gt_mag > 0.05)
    if valid_mask is not None:
        epe = epe[valid_mask]
        fl_mask = fl_mask[valid_mask]
    print(f"EPE={epe.mean():.2f}  Fl={fl_mask.float().mean():.3f}")
    return epe.mean().item(), fl_mask.float().mean().item()
```

The Fl (flow outlier) metric from KITTI counts pixels where EPE exceeds 3 px AND relative error exceeds 5% of the ground-truth magnitude. This threshold-based metric is robust to large motion magnitudes and measures catastrophic failures rather than average accuracy. KITTI further splits Fl into Fl-bg (static background) and Fl-fg (dynamic foreground) to analyze per-region failure modes.

| Method | Type | Sintel Clean EPE | Sintel Final EPE | KITTI Fl % | Speed (ms) |
| --- | --- | --- | --- | --- | --- |
| LK | Classical | 7.40 | 8.90 | — | 15 |
| EpicFlow | Classical+CNN | 4.12 | 6.29 | 26.3 | 280 |
| FlowNet2 | CNN | 1.45 | 3.96 | 11.5 | 120 |
| PWCNet | CNN | 2.55 | 3.93 | 9.60 | 35 |
| RAFT | RNN | 1.43 | 2.71 | 5.10 | 160 |
| FlowFormer | Transformer | 1.01 | 2.40 | 4.09 | 180 |

## Key Takeaways

Sparse-to-dense evolution: optical flow research progressed from sparse feature tracking (KLT) to dense classical estimation (LK, HS) to learned cost-volume methods (FlowNet, PWCNet) to iterative refinement (RAFT). Each generation improved accuracy roughly 2× on Sintel, showing that architectural innovations compound over time in dense spatiotemporal estimation problems.

Correlation volumes are the key differentiator between classical and learned flow methods. Classical methods compute correlation over raw pixel patches; learned methods compute it over deep feature maps. RAFT's all-pairs correlation — O(N²) in pixel count but computed once — enables richer matching than sliding-window approaches and drives its state-of-the-art accuracy on all standard benchmarks.

Benchmark overfitting remains a concern: models trained on FlyingChairs and FlyingThings3D may not generalize to real video. RAFT mitigates this via iterative refinement and weight sharing, but the domain gap between synthetic training data and real deployment persists. Sintel-Final correlates better with real-world performance than Sintel-Clean due to its realistic rendering effects.

