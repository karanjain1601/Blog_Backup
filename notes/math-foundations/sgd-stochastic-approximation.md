---
title: "SGD and Stochastic Approximation"
slug: "sgd-stochastic-approximation"
description: "Rigorous treatment of SGD as stochastic approximation, variance analysis, Robbins-Monro convergence conditions, linear scaling rule, gradient accumulation, and SGD's implicit regularization toward flat minima."
tags: ["optimization", "sgd", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3RvY2hhc3RpYyBncmFkaWVudCBkZXNjZW50IHJlcGxhY2VzIHRoZSBleHBlbnNpdmUgZnVsbC1ncmFkaWVudCB3aXRoIGEgY2hlYXAgbm9pc3kgZXN0aW1hdGUsIGVuYWJsaW5nIHRyYWluaW5nIG9uIG1hc3NpdmUgZGF0YXNldHMuIEJ1dCBTR0QgaXMgbm90IG1lcmVseSBncmFkaWVudCBkZXNjZW50IHdpdGggc29tZSBub2lzZSBhZGRlZC4gVGhlIHN0b2NoYXN0aWNpdHkgZnVuZGFtZW50YWxseSBjaGFuZ2VzIHRoZSBhbGdvcml0aG0ncyBiZWhhdmlvcjogaXQgZW5hYmxlcyBlc2NhcGUgZnJvbSBzaGFycCBtaW5pbWEsIHByb3ZpZGVzIGltcGxpY2l0IHJlZ3VsYXJpemF0aW9uLCBhbmQgcmVxdWlyZXMgZGlmZmVyZW50IGNvbnZlcmdlbmNlIGFuYWx5c2lzIChSb2JiaW5zLU1vbnJvIGNvbmRpdGlvbnMpLiBVbmRlcnN0YW5kaW5nIFNHRCB0aHJvdWdoIHRoZSBsZW5zIG9mIHN0b2NoYXN0aWMgYXBwcm94aW1hdGlvbiB0aGVvcnkg4oCUIHZhcmlhbmNlLCBiaWFzLCBzdGVwLXNpemUgY29uZGl0aW9ucywgYW5kIHRoZSBnZW5lcmFsaXphdGlvbiBnYXAg4oCUIGlzIGVzc2VudGlhbCBmb3IgZGlhZ25vc2luZyB0cmFpbmluZyBpbnN0YWJpbGl0eSwgdHVuaW5nIGJhdGNoIHNpemUgYW5kIGxlYXJuaW5nIHJhdGUsIGFuZCB1bmRlcnN0YW5kaW5nIHdoeSBTR0Qgb2Z0ZW4gZ2VuZXJhbGl6ZXMgYmV0dGVyIHRoYW4gQWRhbSBvbiBpbWFnZSBjbGFzc2lmaWNhdGlvbiB0YXNrcyBkZXNwaXRlIEFkYW3igJlzIGZhc3RlciBjb252ZXJnZW5jZSBzcGVlZCBkdXJpbmcgdHJhaW5pbmcuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29yZSBEZWZpbml0aW9uOiBTdG9jaGFzdGljIEdyYWRpZW50IEVzdGltYXRlcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZvciBhIGxvc3MgTCjOuCkgPSAoMS9uKc6j4bWibOG1oijOuCksIHRoZSBTR0QgZ3JhZGllbnQgZXN0aW1hdGUgdXNpbmcgbWluaWJhdGNoIELiioZbbl0gb2Ygc2l6ZSBCIGlzIMSd4oKcID0gKDEvfEJ8Kc6j4bWi4oiIQuKIh2zhtaIozrjigpwpLiBLZXkgcHJvcGVydGllczogKDEpIFVuYmlhc2VkbmVzczogRVvEneKCnHzOuOKCnF0gPSDiiIdMKM644oKcKS4gKDIpIFZhcmlhbmNlOiBWYXJbxJ3igpxdID0gz4PCsi9CIHdoZXJlIM+DwrIgPSAoMS9uKc6j4bWi4oCW4oiHbOG1oijOuCniiJLiiIdMKM64KeKAlsKyIGlzIHRoZSBwZXItc2FtcGxlIGdyYWRpZW50IHZhcmlhbmNlLiAoMykgQXMgQuKGkm46IGZ1bGwtYmF0Y2ggZ3JhZGllbnQsIHplcm8gbm9pc2UuIFRoZSBncmFkaWVudCBlc3RpbWF0ZSBlbnRlcnMgdGhlIHVwZGF0ZTogzrjigpzigorigoEgPSDOuOKCnCDiiJIgzrfigpzEneKCnC4gVGhlIG5vaXNlIM624oKcID0gxJ3igpwg4oiSIOKIh0wozrjigpwpIGhhcyBFW8624oKcXT0wICh1bmJpYXNlZCkgYnV0IG5vbnplcm8gdmFyaWFuY2Ugz4PCsi9CLiBUaGlzIG5vaXNlIGZ1bmRhbWVudGFsbHkgY2hhbmdlcyBjb252ZXJnZW5jZSBiZWhhdmlvcjogU0dEIHdpdGggY29uc3RhbnQgTFIgZG9lcyBub3QgY29udmVyZ2UgdG8gYSBzdGF0aW9uYXJ5IHBvaW50IGJ1dCBvc2NpbGxhdGVzIGFyb3VuZCBvbmUgd2l0aGluIGEgYmFsbCBvZiByYWRpdXMgcHJvcG9ydGlvbmFsIHRvIM63z4Mv4oiaQi4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiBzZ2RfdmFyaWFuY2VfZGVtbyhuPTEwMDAsIGQ9MTAsIGJhdGNoX3NpemVzPVsxLCAzMiwgMjU2LCAxMDAwXSwgbl9zdGVwcz01MDApOlxuICAgIFwiXCJcIlxuICAgIERlbW9uc3RyYXRlIGdyYWRpZW50IHZhcmlhbmNlIHZzIGJhdGNoIHNpemUuXG4gICAgU2hvd3M6IFZhcltnX2hhdF0gYXBwcm94IHNpZ21hXjIgLyBCICh2YXJpYW5jZSByZWR1Y2VzIGxpbmVhcmx5IHdpdGggQikuXG4gICAgXCJcIlwiXG4gICAgbnAucmFuZG9tLnNlZWQoNDIpXG4gICAgWCA9IG5wLnJhbmRvbS5yYW5kbihuLCBkKVxuICAgIHdfdHJ1ZSA9IG5wLnJhbmRvbS5yYW5kbihkKVxuICAgIHkgPSBYIEAgd190cnVlICsgbnAucmFuZG9tLnJhbmRuKG4pICogMC41XG5cbiAgICAjIEZ1bGwgZ3JhZGllbnQgKGdyb3VuZCB0cnV0aClcbiAgICB3ID0gbnAuemVyb3MoZClcbiAgICBncmFkX3RydWUgPSAyICogWC5UIEAgKFggQCB3IC0geSkgLyBuXG5cbiAgICAjIEVzdGltYXRlIGdyYWRpZW50IHZhcmlhbmNlIGZvciBlYWNoIGJhdGNoIHNpemVcbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgQiBpbiBiYXRjaF9zaXplczpcbiAgICAgICAgZ3JhZF9lc3RpbWF0ZXMgPSBbXVxuICAgICAgICBmb3IgXyBpbiByYW5nZSgyMDApOiAgIyAyMDAgc2FtcGxlcyBvZiBncmFkaWVudCBlc3RpbWF0ZVxuICAgICAgICAgICAgaWR4ID0gbnAucmFuZG9tLmNob2ljZShuLCBCLCByZXBsYWNlPUZhbHNlKVxuICAgICAgICAgICAgWGIsIHliID0gWFtpZHhdLCB5W2lkeF1cbiAgICAgICAgICAgIGcgPSAyICogWGIuVCBAIChYYiBAIHcgLSB5YikgLyBCXG4gICAgICAgICAgICBncmFkX2VzdGltYXRlcy5hcHBlbmQoZylcblxuICAgICAgICBncmFkX2VzdGltYXRlcyA9IG5wLmFycmF5KGdyYWRfZXN0aW1hdGVzKVxuICAgICAgICB2YXJpYW5jZSA9IGdyYWRfZXN0aW1hdGVzLnZhcihheGlzPTApLm1lYW4oKSAgIyBhdmVyYWdlIHZhcmlhbmNlIGFjcm9zcyBkaW1zXG4gICAgICAgIHJlc3VsdHNbQl0gPSB2YXJpYW5jZVxuICAgICAgICBwcmludChmXCJCPXtCOjVkfTogZ3JhZGllbnQgdmFyaWFuY2UgPSB7dmFyaWFuY2U6LjRmfVwiKVxuXG4gICAgIyBWZXJpZnkgbGluZWFyIHJlbGF0aW9uc2hpcDogVmFyIHByb3BvcnRpb25hbCB0byAxL0JcbiAgICBCX2FycmF5ID0gbnAuYXJyYXkobGlzdChyZXN1bHRzLmtleXMoKSkpXG4gICAgdmFyX2FycmF5ID0gbnAuYXJyYXkobGlzdChyZXN1bHRzLnZhbHVlcygpKSlcbiAgICBzaWdtYTJfZXN0ID0gKHZhcl9hcnJheSAqIEJfYXJyYXkpLm1lYW4oKVxuICAgIHByaW50KGZcIlxcbkVzdGltYXRlZCBzaWdtYV4yID0ge3NpZ21hMl9lc3Q6LjRmfVwiKVxuICAgIGZvciBCLCB2YXIgaW4gemlwKEJfYXJyYXksIHZhcl9hcnJheSk6XG4gICAgICAgIHByZWRpY3RlZCA9IHNpZ21hMl9lc3QgLyBCXG4gICAgICAgIHByaW50KGZcIkI9e0J9OiBhY3R1YWw9e3ZhcjouNGZ9LCBwcmVkaWN0ZWQgc2lnbWFeMi9CPXtwcmVkaWN0ZWQ6LjRmfVwiKVxuXG5zZ2RfdmFyaWFuY2VfZGVtbygpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUm9iYmlucy1Nb25ybyBDb252ZXJnZW5jZSBDb25kaXRpb25zIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIFJvYmJpbnMtTW9ucm8gKDE5NTEpIGNvbmRpdGlvbnMgZm9yIFNHRCBjb252ZXJnZW5jZSB3aXRoIGRlY2F5aW5nIHN0ZXAgc2l6ZXMgzrfigpwgYXJlOiAoMSkgzqPigpwgzrfigpwgPSDiiJ4gKHN0ZXBzIHN1bSB0byBpbmZpbml0eSDigJQgZW5zdXJlcyB3ZSBjYW4gcmVhY2ggYW55IHBvaW50IGluIHBhcmFtZXRlciBzcGFjZSk7ICgyKSDOo863wrLigpwgPCDiiJ4gKHN1bSBvZiBzcXVhcmVkIHN0ZXBzIGlzIGZpbml0ZSDigJQgZW5zdXJlcyB2YXJpYW5jZSBzaHJpbmtzIGZhc3QgZW5vdWdoIGZvciBjb252ZXJnZW5jZSkuIFRoZSBjYW5vbmljYWwgc2NoZWR1bGUgzrfigpwgPSDOt+KCgC90Xs6xIHdpdGggzrEg4oiIICgwLjUsIDFdIHNhdGlzZmllcyB0aGVzZSBjb25kaXRpb25zOiDOo8634oKAL3RezrEgZGl2ZXJnZXMgKGhhcm1vbmljIHNlcmllcyBmb3IgzrE9MSksIGJ1dCDOo8634oKAwrIvdF57Ms6xfSBjb252ZXJnZXMgZm9yIDLOsSA+IDEuIFVuZGVyIHRoZXNlIGNvbmRpdGlvbnMsIFNHRCBjb252ZXJnZXMgdG8gYSBzdGF0aW9uYXJ5IHBvaW50IGZvciBub24tY29udmV4IGYgYW5kIHRvIHRoZSBnbG9iYWwgbWluaW11bSBmb3IgY29udmV4IGYuIFRoZSBkZWNheSBtdXN0IGJlIHNsb3cgZW5vdWdoICjOsSDiiaQgMSkgdG8gZXhwbG9yZSB0aGUgc3BhY2UsIGJ1dCBmYXN0IGVub3VnaCAozrEgPiAwLjUpIHRvIHN1cHByZXNzIG5vaXNlIGFuZCBhY2hpZXZlIGNvbnZlcmdlbmNlLiBDb25zdGFudCBMUiB2aW9sYXRlcyBjb25kaXRpb24gMiDigJQgU0dEIG9zY2lsbGF0ZXMgcGVybWFuZW50bHkgYnV0IGNhbiBiZSBhdmVyYWdlZCAoUG9seWFrLVJ1cHBlcnQgYXZlcmFnaW5nKSBmb3IgY29udmVyZ2VuY2UuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc2dkX3dpdGhfbHJfc2NoZWR1bGUoZ3JhZF9mbiwgdGhldGEwLCBuLCBzY2hlZHVsZT0nZGVjYXknLCBuX3N0ZXBzPTIwMDAsIGV0YTA9MC4xKTpcbiAgICBcIlwiXCJcbiAgICBDb21wYXJlIFNHRCB3aXRoIGNvbnN0YW50IHZzIGRlY2F5aW5nIGxlYXJuaW5nIHJhdGUuXG4gICAgQWxzbyBkZW1vbnN0cmF0ZXMgUG9seWFrLVJ1cHBlcnQgYXZlcmFnaW5nLlxuICAgIFwiXCJcIlxuICAgIHRoZXRhID0gdGhldGEwLmNvcHkoKVxuICAgIHRoZXRhX2F2ZyA9IHRoZXRhMC5jb3B5KCkgICMgUG9seWFrLVJ1cHBlcnQgYXZlcmFnZVxuICAgIGxvc3NlcyA9IFtdXG5cbiAgICAjIFRydWUgb3B0aW11bSBmb3IgY29tcGFyaXNvbiAoYXNzdW1lIHF1YWRyYXRpYylcbiAgICBmID0gbGFtYmRhIHQ6IG5wLnN1bSh0KioyKVxuXG4gICAgZm9yIHQgaW4gcmFuZ2UoMSwgbl9zdGVwcyArIDEpOlxuICAgICAgICBpZiBzY2hlZHVsZSA9PSAnZGVjYXknOlxuICAgICAgICAgICAgZXRhX3QgPSBldGEwIC8gbnAuc3FydCh0KSAgIyBhbHBoYSA9IDAuNToganVzdCBiYXJlbHkgc2F0aXNmaWVzIFItTVxuICAgICAgICBlbGlmIHNjaGVkdWxlID09ICdjb25zdGFudCc6XG4gICAgICAgICAgICBldGFfdCA9IGV0YTBcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIGV0YV90ID0gZXRhMCAvIHQgICMgYWxwaGEgPSAxOiBzYXRpc2ZpZXMgUi1NIHN0cm9uZ2x5XG5cbiAgICAgICAgIyBOb2lzeSBncmFkaWVudCAodHJ1ZSBncmFkaWVudCArIG5vaXNlKVxuICAgICAgICBnX3RydWUgPSBncmFkX2ZuKHRoZXRhKVxuICAgICAgICBub2lzZSA9IDAuMSAqIG5wLnJhbmRvbS5yYW5kbihsZW4odGhldGEpKSAgIyBzaW11bGF0ZSBTR0Qgbm9pc2VcbiAgICAgICAgZ19ub2lzeSA9IGdfdHJ1ZSArIG5vaXNlXG5cbiAgICAgICAgdGhldGEgPSB0aGV0YSAtIGV0YV90ICogZ19ub2lzeVxuICAgICAgICAjIFBvbHlhay1SdXBwZXJ0OiBydW5uaW5nIGF2ZXJhZ2Ugb2YgaXRlcmF0ZXNcbiAgICAgICAgdGhldGFfYXZnID0gKHRoZXRhX2F2ZyAqICh0IC0gMSkgKyB0aGV0YSkgLyB0XG5cbiAgICAgICAgaWYgdCAlIDEwMCA9PSAwOlxuICAgICAgICAgICAgbG9zc2VzLmFwcGVuZCgodCwgZih0aGV0YSksIGYodGhldGFfYXZnKSkpXG5cbiAgICByZXR1cm4gbG9zc2VzXG5cbiMgVGVzdCBvbiBmKHRoZXRhKSA9IHN1bSh0aGV0YV4yKSwgZ3JhZGllbnQgPSAyKnRoZXRhXG5ncmFkX2ZuID0gbGFtYmRhIHRoZXRhOiAyICogdGhldGFcbnRoZXRhMCA9IG5wLmFycmF5KFszLjAsIDIuMCwgMS4wXSlcblxucHJpbnQoXCJTdGVwICB8IHRoZXRhX2xvc3MgfCB0aGV0YV9hdmdfbG9zcyB8IHNjaGVkdWxlXCIpXG5mb3Igc2NoZWR1bGUgaW4gWydjb25zdGFudCcsICdkZWNheScsICd0LWRlY2F5J106XG4gICAgbG9zc2VzID0gc2dkX3dpdGhfbHJfc2NoZWR1bGUoZ3JhZF9mbiwgdGhldGEwLCBuPTEwMCwgc2NoZWR1bGU9c2NoZWR1bGUpXG4gICAgZmluYWwgPSBsb3NzZXNbLTFdXG4gICAgcHJpbnQoZlwie2ZpbmFsWzBdfSB8IHtmaW5hbFsxXTouNGV9IHwge2ZpbmFsWzJdOi40ZX0gfCB7c2NoZWR1bGV9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTGluZWFyIFNjYWxpbmcgUnVsZSBhbmQgQmF0Y2ggU2l6ZSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBsaW5lYXIgc2NhbGluZyBydWxlIChHb3lhbCBldCBhbC4sIEZhY2Vib29rIDIwMTcpOiB3aGVuIG11bHRpcGx5aW5nIGJhdGNoIHNpemUgYnkgaywgbXVsdGlwbHkgdGhlIGxlYXJuaW5nIHJhdGUgYnkgay4gSW50dWl0aW9uOiBTR0Qgd2l0aCBiYXRjaCBCIGFuZCBMUiDOtyB1cGRhdGVzIHVzaW5nIGEgZ3JhZGllbnQgZXN0aW1hdGUgd2l0aCB2YXJpYW5jZSDPg8KyL0IuIFRvIG1haW50YWluIHRoZSBzYW1lIHNpZ25hbC10by1ub2lzZSByYXRpbyB3aGVuIGRvdWJsaW5nIEIsIGRvdWJsZSDOtyDigJQgdGhpcyBwcmVzZXJ2ZXMgZ3JhZGllbnQgbm9pc2Ugc3RhdGlzdGljcyBwZXIgdXBkYXRlLiBGb3JtYWxseTogayBzdGVwcyBvZiBTR0Qgd2l0aCAoQiwgzrcpIGFwcHJveGltYXRlIG9uZSBzdGVwIG9mIFNHRCB3aXRoIChrQiwga863KSB0byBmaXJzdCBvcmRlciBpbiB0aGUgc3RlcCBzaXplLiBMaW1pdGF0aW9uczogdGhlIGxpbmVhciBzY2FsaW5nIHJ1bGUgYnJlYWtzIGF0IHZlcnkgbGFyZ2UgYmF0Y2ggc2l6ZXMsIGJleW9uZCB0aGUgY3JpdGljYWwgYmF0Y2ggc2l6ZSBCX2Mg4omIIM+DwrIv4oCW4oiHTOKAlsKyIOKAlCBiZXlvbmQgdGhpcyBwb2ludCwgYWRkaW5nIG1vcmUgc2FtcGxlcyBkb2VzIG5vdCBwcm9wb3J0aW9uYWxseSByZWR1Y2Ugbm9pc2UuIEFsc28sIHdoZW4gdXNpbmcgbGFyZ2UgYmF0Y2hlcyAoQj4xMDI0KSwgYWx3YXlzIHdhcm0gdXAgdGhlIExSIGZvciB0aGUgZmlyc3QgZmV3IGVwb2NocywgYXMgdGhlIGdyYWRpZW50IHZhcmlhbmNlIGlzIGluaXRpYWxseSB0b28gaGlnaCByZWxhdGl2ZSB0byB0aGUgZ3JhZGllbnQgc2lnbmFsIHRvIHNhZmVseSB1c2UgdGhlIHNjYWxlZCBMUi4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJJbXBsaWNpdCBSZWd1bGFyaXphdGlvbjogV2h5IFNHRCBHZW5lcmFsaXplcyBCZXR0ZXIifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJFbXBpcmljYWxseSwgU0dEIGdlbmVyYWxpemVzIGJldHRlciB0aGFuIGZ1bGwtYmF0Y2ggR0Qgb24gaW1hZ2UgY2xhc3NpZmljYXRpb24sIGV2ZW4gYXQgZXF1aXZhbGVudCB0cmFpbmluZyBsb3NzLiBUaGUgdGhlb3JldGljYWwgZXhwbGFuYXRpb246IFNHRCdzIGdyYWRpZW50IG5vaXNlIGluZHVjZXMgYW4gaW1wbGljaXQgYmlhcyB0b3dhcmQgZmxhdHRlciBtaW5pbWEuIEludHVpdGl2ZWx5LCBhIHNoYXJwIG1pbmltdW0gKGhpZ2ggY3VydmF0dXJlKSBpcyB1bnN0YWJsZSB1bmRlciBncmFkaWVudCBub2lzZSDigJQgdGhlIG5vaXNlIGtpY2tzIHRoZSBvcHRpbWl6ZXIgb3V0IG9mIHNoYXJwIG1pbmltYSwgYW5kIGl0IGV2ZW50dWFsbHkgc2V0dGxlcyBpbiBmbGF0IG1pbmltYSAod2lkZSBiYXNpbnMpIHRoYXQgYXJlIG1vcmUgcm9idXN0IHRvIHBlcnR1cmJhdGlvbi4gRm9ybWFsbHksIHRoZSBTR0QgZHluYW1pY3MgKHdpdGggZmluaXRlIExSIM63KSBjYW4gYmUgd3JpdHRlbiBhcyBmb2xsb3dpbmcgdGhlIGdyYWRpZW50IG9mIGYgKyAozrcvNEIpzpRMLCB3aGVyZSDOlEwgaXMgdGhlIHRyYWNlIG9mIHRoZSBIZXNzaWFuIOKAlCB0aGlzIHBlbmFsaXplcyBoaWdoLWN1cnZhdHVyZSByZWdpb25zLiBGbGF0IG1pbmltYSBoYXZlIGJldHRlciB0ZXN0IGdlbmVyYWxpemF0aW9uIGJ5IHRoZSBQQUMtQmF5ZXMgcGVyc3BlY3RpdmU6IGEgZmxhdCBtaW5pbXVtIG1lYW5zIGEgbGFyZ2VyIG5laWdoYm9yaG9vZCBvZiBwYXJhbWV0ZXJzIHdpdGggZ29vZCBsb3NzLCBpbXBseWluZyB0aGUgc29sdXRpb24gaXMgcm9idXN0IHRvIHRoZSBkaXN0cmlidXRpb24gc2hpZnQgYmV0d2VlbiB0cmFpbmluZyBhbmQgdGVzdCBzZXRzLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBjb21wYXJlX3NnZF9iYXRjaF9nZW5lcmFsaXphdGlvbihuX3RyYWluPTUwMCwgbl90ZXN0PTUwMCwgbl9lcG9jaHM9MTAwKTpcbiAgICBcIlwiXCJcbiAgICBDb21wYXJlIGxhcmdlLWJhdGNoIHZzIHNtYWxsLWJhdGNoIFNHRCBvbiBhIHNpbXBsZSBvdmVycGFyYW1ldGVyaXplZCBwcm9ibGVtLlxuICAgIFNob3dzOiBzbWFsbCBiYXRjaCBnZW5lcmFsaXplcyBiZXR0ZXIgKGZsYXR0ZXIgbWluaW1hKS5cbiAgICBcIlwiXCJcbiAgICB0b3JjaC5tYW51YWxfc2VlZCg0MilcblxuICAgICMgU3ludGhldGljIGRhdGE6IDItY2xhc3MgY2xhc3NpZmljYXRpb25cbiAgICBYX3RyYWluID0gdG9yY2gucmFuZG4obl90cmFpbiwgMjApXG4gICAgeV90cmFpbiA9IChYX3RyYWluWzosIDBdID4gMCkuZmxvYXQoKS51bnNxdWVlemUoMSlcbiAgICBYX3Rlc3QgPSB0b3JjaC5yYW5kbihuX3Rlc3QsIDIwKVxuICAgIHlfdGVzdCA9IChYX3Rlc3RbOiwgMF0gPiAwKS5mbG9hdCgpLnVuc3F1ZWV6ZSgxKVxuXG4gICAgZGVmIG1ha2VfbW9kZWwoKTpcbiAgICAgICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDIwLCA2NCksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5uLkxpbmVhcig2NCwgNjQpLCBubi5SZUxVKCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICBubi5MaW5lYXIoNjQsIDEpLCBubi5TaWdtb2lkKCkpXG5cbiAgICBkZWYgdHJhaW4obW9kZWwsIGJhdGNoX3NpemUsIGxyLCBuX2Vwb2Nocyk6XG4gICAgICAgIG9wdCA9IHRvcmNoLm9wdGltLlNHRChtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPWxyKVxuICAgICAgICBjcml0ZXJpb24gPSBubi5CQ0VMb3NzKClcbiAgICAgICAgZm9yIGVwb2NoIGluIHJhbmdlKG5fZXBvY2hzKTpcbiAgICAgICAgICAgIGlkeCA9IHRvcmNoLnJhbmRwZXJtKG5fdHJhaW4pXG4gICAgICAgICAgICBmb3Igc3RhcnQgaW4gcmFuZ2UoMCwgbl90cmFpbiwgYmF0Y2hfc2l6ZSk6XG4gICAgICAgICAgICAgICAgWGIgPSBYX3RyYWluW2lkeFtzdGFydDpzdGFydCtiYXRjaF9zaXplXV1cbiAgICAgICAgICAgICAgICB5YiA9IHlfdHJhaW5baWR4W3N0YXJ0OnN0YXJ0K2JhdGNoX3NpemVdXVxuICAgICAgICAgICAgICAgIG9wdC56ZXJvX2dyYWQoKVxuICAgICAgICAgICAgICAgIGxvc3MgPSBjcml0ZXJpb24obW9kZWwoWGIpLCB5YilcbiAgICAgICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgICAgICBvcHQuc3RlcCgpXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgdHJhaW5fYWNjID0gKChtb2RlbChYX3RyYWluKSA+IDAuNSkgPT0geV90cmFpbikuZmxvYXQoKS5tZWFuKClcbiAgICAgICAgICAgIHRlc3RfYWNjID0gKChtb2RlbChYX3Rlc3QpID4gMC41KSA9PSB5X3Rlc3QpLmZsb2F0KCkubWVhbigpXG4gICAgICAgIHJldHVybiB0cmFpbl9hY2MuaXRlbSgpLCB0ZXN0X2FjYy5pdGVtKClcblxuICAgICMgTGluZWFyIHNjYWxpbmcgcnVsZTogbGFyZ2UgYmF0Y2ggdXNlcyBwcm9wb3J0aW9uYWxseSBsYXJnZXIgTFJcbiAgICBmb3IgYmF0Y2hfc2l6ZSwgbHIgaW4gWyg4LCAwLjAxKSwgKDI1NiwgMC4zMildOlxuICAgICAgICBtb2RlbCA9IG1ha2VfbW9kZWwoKVxuICAgICAgICB0cmFpbl9hY2MsIHRlc3RfYWNjID0gdHJhaW4obW9kZWwsIGJhdGNoX3NpemUsIGxyLCBuX2Vwb2NocylcbiAgICAgICAgZ2VuX2dhcCA9IHRyYWluX2FjYyAtIHRlc3RfYWNjXG4gICAgICAgIHByaW50KGZcIkI9e2JhdGNoX3NpemU6NGR9IGxyPXtscjouMmZ9OiB0cmFpbj17dHJhaW5fYWNjOi4zZn0gdGVzdD17dGVzdF9hY2M6LjNmfSBnYXA9e2dlbl9nYXA6LjNmfVwiKVxuXG5jb21wYXJlX3NnZF9iYXRjaF9nZW5lcmFsaXphdGlvbigpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiR3JhZGllbnQgQWNjdW11bGF0aW9uIGZvciBTaW11bGF0aW5nIExhcmdlIEJhdGNoZXMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJXaGVuIEdQVSBtZW1vcnkgbGltaXRzIGJhdGNoIHNpemUsIGdyYWRpZW50IGFjY3VtdWxhdGlvbiBzaW11bGF0ZXMgbGFyZ2VyIGVmZmVjdGl2ZSBiYXRjaGVzOiBydW4gQl9taWNybyBtaWNyby1iYXRjaGVzIHRocm91Z2ggZm9yd2FyZCBhbmQgYmFja3dhcmQgcGFzc2VzLCBhY2N1bXVsYXRlIGdyYWRpZW50cywgdGhlbiB0YWtlIG9uZSBvcHRpbWl6ZXIgc3RlcC4gRWZmZWN0aXZlIGJhdGNoIHNpemUgPSBCX21pY3JvIMOXIG5fYWNjdW11bGF0aW9uX3N0ZXBzLiBDcml0aWNhbCBpbXBsZW1lbnRhdGlvbiBkZXRhaWw6IGRpdmlkZSBsb3NzIGJ5IG5fYWNjdW11bGF0aW9uX3N0ZXBzIGJlZm9yZSB0aGUgYmFja3dhcmQgcGFzcyAob3Igc2V0IHJlZHVjdGlvbj0nbWVhbicgd2l0aGluIGVhY2ggbWljcm8tYmF0Y2gpLCBvdGhlcndpc2UgZ3JhZGllbnRzIGFyZSBzY2FsZWQgYnkgbl9hY2N1bXVsYXRpb25fc3RlcHMgcmVsYXRpdmUgdG8gdGhlIGV4cGVjdGVkIG1hZ25pdHVkZS4gVGhpcyBzY2FsaW5nIG1hdHRlcnMgZXNwZWNpYWxseSBmb3IgZ3JhZGllbnQgY2xpcHBpbmc6IGFsd2F5cyBjbGlwIGFmdGVyIGFjY3VtdWxhdGlvbiB1c2luZyB0aGUgYWNjdW11bGF0ZWQgZ3JhZGllbnQgbm9ybSwgbm90IHRoZSBwZXItbWljcm8tYmF0Y2ggbm9ybS4gVGhpcyBhcHByb2FjaCB3b3JrcyBpZGVudGljYWxseSB0byB0cnVlIGxhcmdlIGJhdGNoIGZvciBkZXRlcm1pbmlzdGljIG1vZGVscywgYnV0IGRyb3BvdXQgYW5kIGJhdGNoIG5vcm1hbGl6YXRpb24gYmVoYXZpb3IgZGlmZmVyIHNsaWdodGx5IChCTiBydW5uaW5nIHN0YXRpc3RpY3MgYXJlIGNvbXB1dGVkIG9uIHRoZSBtaWNyby1iYXRjaCBzaXplLCBub3QgdGhlIGZ1bGwgYWNjdW11bGF0ZWQgZWZmZWN0aXZlIGJhdGNoKS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIHRyYWluaW5nX2xvb3Bfd2l0aF9ncmFkaWVudF9hY2N1bXVsYXRpb24oXG4gICAgbW9kZWwsIG9wdGltaXplciwgZGF0YWxvYWRlciwgbl9hY2N1bXVsYXRpb25fc3RlcHM9NCwgY2xpcF9ub3JtPTEuMFxuKTpcbiAgICBcIlwiXCJcbiAgICBUcmFpbmluZyBsb29wIHdpdGggZ3JhZGllbnQgYWNjdW11bGF0aW9uLlxuICAgIEVmZmVjdGl2ZSBiYXRjaCBzaXplID0gbG9hZGVyIGJhdGNoX3NpemUgKiBuX2FjY3VtdWxhdGlvbl9zdGVwcy5cbiAgICBcIlwiXCJcbiAgICBtb2RlbC50cmFpbigpXG4gICAgY3JpdGVyaW9uID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpXG4gICAgdG90YWxfbG9zcyA9IDAuMFxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuXG4gICAgZm9yIHN0ZXAsIChYLCB5KSBpbiBlbnVtZXJhdGUoZGF0YWxvYWRlcik6XG4gICAgICAgICMgRm9yd2FyZCBwYXNzIG9uIG1pY3JvLWJhdGNoXG4gICAgICAgIGxvZ2l0cyA9IG1vZGVsKFgpXG4gICAgICAgICMgRGl2aWRlIGxvc3MgYnkgYWNjdW11bGF0aW9uIHN0ZXBzIHNvIGdyYWRpZW50cyBhcmUgY29ycmVjdCBzY2FsZVxuICAgICAgICBsb3NzID0gY3JpdGVyaW9uKGxvZ2l0cywgeSkgLyBuX2FjY3VtdWxhdGlvbl9zdGVwc1xuICAgICAgICBsb3NzLmJhY2t3YXJkKClcblxuICAgICAgICB0b3RhbF9sb3NzICs9IGxvc3MuaXRlbSgpICogbl9hY2N1bXVsYXRpb25fc3RlcHNcblxuICAgICAgICAjIEV2ZXJ5IG5fYWNjdW11bGF0aW9uX3N0ZXBzLCB1cGRhdGUgcGFyYW1ldGVyc1xuICAgICAgICBpZiAoc3RlcCArIDEpICUgbl9hY2N1bXVsYXRpb25fc3RlcHMgPT0gMDpcbiAgICAgICAgICAgICMgQ2xpcCBBRlRFUiBhY2N1bXVsYXRpb24gKHVzZXMgYWNjdW11bGF0ZWQgZ3JhZGllbnQgbm9ybSlcbiAgICAgICAgICAgIHRvcmNoLm5uLnV0aWxzLmNsaXBfZ3JhZF9ub3JtXyhtb2RlbC5wYXJhbWV0ZXJzKCksIGNsaXBfbm9ybSlcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuXG4gICAgICAgICAgICBlZmZlY3RpdmVfc3RlcCA9IChzdGVwICsgMSkgLy8gbl9hY2N1bXVsYXRpb25fc3RlcHNcbiAgICAgICAgICAgIGF2Z19sb3NzID0gdG90YWxfbG9zcyAvIG5fYWNjdW11bGF0aW9uX3N0ZXBzXG4gICAgICAgICAgICBpZiBlZmZlY3RpdmVfc3RlcCAlIDEwID09IDA6XG4gICAgICAgICAgICAgICAgcHJpbnQoZlwiU3RlcCB7ZWZmZWN0aXZlX3N0ZXB9OiBsb3NzPXthdmdfbG9zczouNGZ9XCIpXG4gICAgICAgICAgICB0b3RhbF9sb3NzID0gMC4wXG5cbiAgICAjIEhhbmRsZSByZW1haW5pbmcgbWljcm8tYmF0Y2hlcyBhdCBlbmQgb2YgZXBvY2hcbiAgICBpZiAoc3RlcCArIDEpICUgbl9hY2N1bXVsYXRpb25fc3RlcHMgIT0gMDpcbiAgICAgICAgdG9yY2gubm4udXRpbHMuY2xpcF9ncmFkX25vcm1fKG1vZGVsLnBhcmFtZXRlcnMoKSwgY2xpcF9ub3JtKVxuICAgICAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuXG5wcmludChcIkdyYWRpZW50IGFjY3VtdWxhdGlvbiB0cmFpbmluZyBsb29wIGRlZmluZWQuXCIpXG5wcmludChcIktleTogZGl2aWRlIGxvc3MgYnkgbl9hY2N1bXVsYXRpb25fc3RlcHMgQkVGT1JFIGJhY2t3YXJkLlwiKVxucHJpbnQoXCJLZXk6IGNsaXAgZ3JhZGllbnRzIEFGVEVSIGFjY3VtdWxhdGlvbiwgbm90IHBlciBtaWNyby1iYXRjaC5cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJJbXBsZW1lbnRhdGlvbiBQaXRmYWxscyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIk5vdCBzaHVmZmxpbmcgZGF0YTogaWYgc2FtcGxlcyBhcmUgb3JkZXJlZCBieSBjbGFzcywgY3ljbGljIFNHRCBzZWVzIGNvcnJlbGF0ZWQgYmF0Y2hlcywgaW50cm9kdWNpbmcgc3lzdGVtYXRpYyBiaWFzIGluIGdyYWRpZW50IGVzdGltYXRlcy4gQWx3YXlzIHNodWZmbGUgZWFjaCBlcG9jaCB3aXRoIHRvcmNoLnJhbmRwZXJtKG4pLiBGb3JnZXR0aW5nIHRvIHNjYWxlIGxvc3MgaW4gZ3JhZGllbnQgYWNjdW11bGF0aW9uOiBpZiBsb3NzIGlzIG5vdCBkaXZpZGVkIGJ5IG5fYWNjdW11bGF0aW9uX3N0ZXBzLCBlZmZlY3RpdmUgTFIgaW5jcmVhc2VzIGJ5IHRoYXQgZmFjdG9yIOKAlCBjYXVzaW5nIGluc3RhYmlsaXR5IGFuZCBwb3RlbnRpYWwgZGl2ZXJnZW5jZS4gVXNpbmcgYmF0Y2ggbm9ybSB3aXRoIHZlcnkgc21hbGwgZWZmZWN0aXZlIGJhdGNoIHNpemU6IEJOIHdpdGggQjw4IHByb2R1Y2VzIG5vaXN5IG1lYW4gYW5kIHZhcmlhbmNlIHN0YXRpc3RpY3MgdGhhdCBodXJ0IHBlcmZvcm1hbmNlIHNpZ25pZmljYW50bHkuIFVzZSBHcm91cCBOb3JtIG9yIExheWVyIE5vcm0gZm9yIHNtYWxsLWJhdGNoIHRyYWluaW5nIGluc3RlYWQuIERlY3JlYXNpbmcgTFIgdG9vIGZhc3Q6IM634oKcID0gzrfigoAvdCAoYWxwaGE9MSkgc2F0aXNmaWVzIFJvYmJpbnMtTW9ucm8gdGhlb3JldGljYWxseSBidXQgY29udmVyZ2VzIHZlcnkgc2xvd2x5IGluIHByYWN0aWNlIGJlY2F1c2UgdGhlIExSIGRyb3BzIGJlbG93IHRoZSB1c2VmdWwgcmFuZ2UgcXVpY2tseS4gVXNlIM634oKcID0gzrfigoAv4oiadCBvciBjb3NpbmUgYW5uZWFsaW5nIGZvciBiZXR0ZXIgZW1waXJpY2FsIHBlcmZvcm1hbmNlIGFuZCBmYXN0ZXIgcHJhY3RpY2FsIGNvbnZlcmdlbmNlLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlByYWN0aWNhbCBHdWlkYW5jZSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlN0YXJ0IHdpdGggQj0yNTYgYW5kIExSPTAuMSBmb3IgaW1hZ2UgY2xhc3NpZmljYXRpb24gd2l0aCBTR0QrbW9tZW50dW0uIFNjYWxlIGJvdGggcHJvcG9ydGlvbmFsbHkgZm9yIGRpZmZlcmVudCBoYXJkd2FyZSAobGluZWFyIHNjYWxpbmcgcnVsZSB1cCB0byBCX2NyaXRpY2FsIOKJiCA4MTkyIGZvciBJbWFnZU5ldCkuIFVzZSBsaW5lYXIgd2FybXVwIG92ZXIgNSBlcG9jaHMgd2hlbiB1c2luZyBsYXJnZSBiYXRjaGVzIChCPjEwMjQpIHRvIGF2b2lkIGluc3RhYmlsaXR5IGZyb20gaGlnaCBpbml0aWFsIGdyYWRpZW50IHZhcmlhbmNlLiBQcmVmZXIgY29zaW5lIGFubmVhbGluZyBvdmVyIHN0ZXAgZGVjYXkg4oCUIGl0IHByb2R1Y2VzIHNtb290aGVyIGxvc3MgY3VydmVzIGFuZCBhdm9pZHMgdGhlIG5lZWQgZm9yIG1hbnVhbCBzY2hlZHVsZSB0dW5pbmcuIE1vbml0b3IgZ3JhZGllbnQgdmFyaWFuY2UgYWNyb3NzIHRyYWluaW5nIHN0ZXBzIChjb21wdXRlIHN0YW5kYXJkIGRldmlhdGlvbiBvZiBncmFkaWVudCBlc3RpbWF0ZXMgb3ZlciBzZXZlcmFsIGNvbnNlY3V0aXZlIHN0ZXBzKTogaWYgc3RkL21lYW4gPCAwLjEsIHlvdSBjYW4gc2FmZWx5IGluY3JlYXNlIGJhdGNoIHNpemU7IGlmID4gMTAsIHRoZSBncmFkaWVudCBpcyB0b28gbm9pc3kgYW5kIGJhdGNoIHNpemUgc2hvdWxkIGluY3JlYXNlLiBGb3IgTkxQIHRhc2tzIHdpdGggc3BhcnNlIGZlYXR1cmVzLCBwcmVmZXIgQWRhbSBvdmVyIFNHRCDigJQgZ3JhZGllbnQgdmFyaWFuY2UgaXMgc3RydWN0dXJhbGx5IGhpZ2hlciBpbiBOTFAgZHVlIHRvIHNwYXJzZSB0b2tlbiBncmFkaWVudHMuIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInRpdGxlIjogIkNvbnN0YW50IExSIFByZXZlbnRzIFRydWUgQ29udmVyZ2VuY2UiLCAiY29udGVudCI6ICJXaXRoIGNvbnN0YW50IGxlYXJuaW5nIHJhdGUgZXRhLCBTR0QgY29udmVyZ2VzIHRvIHdpdGhpbiBhIGJhbGwgb2YgcmFkaXVzIE8oZXRhKnNpZ21hL3NxcnQoQikpIGFyb3VuZCB0aGUgbWluaW11bSwgbm90IHRvIHRoZSBleGFjdCBtaW5pbXVtLiBUbyBjb252ZXJnZSB0byBhIHN0YXRpb25hcnkgcG9pbnQsIHlvdSBuZWVkIGRlY2F5aW5nIExSIChSb2JiaW5zLU1vbnJvKSBvciBQb2x5YWstUnVwcGVydCBhdmVyYWdpbmcgKGF2ZXJhZ2Ugb2YgYWxsIGl0ZXJhdGVzKS4gSW4gcHJhY3RpY2UsIGNvc2luZSBhbm5lYWxpbmcgdG8gYSB2ZXJ5IHNtYWxsIExSICgxJSBvZiBwZWFrKSBhcHByb3hpbWF0ZXMgY29udmVyZ2VuY2UuIEFsdGVybmF0aXZlbHksIHJ1biBTR0Qgd2l0aCBjb25zdGFudCBMUiBhbmQgc3dpdGNoIHRvIGZ1bGwtYmF0Y2ggR0QgZm9yIHRoZSBsYXN0IGZldyBzdGVwcyBmb3IgZXhhY3QgY29udmVyZ2VuY2UuIn0sIHsidHlwZSI6ICJ0YWJsZSIsICJoZWFkZXJzIjogWyJCYXRjaCBTaXplIEIiLCAiR3JhZGllbnQgVmFyaWFuY2UiLCAiU3RlcHMvRXBvY2giLCAiR2VuZXJhbGl6YXRpb24iLCAiUHJhY3RpY2FsIFVzZSJdLCAicm93cyI6IFtbIjEgKHRydWUgU0dEKSIsICJzaWdtYV4yIiwgIm4gc3RlcHMiLCAiQmVzdCAoZmxhdHRlc3QgbWluaW1hKSIsICJSYXJlbHkgdXNlZCAoc2xvdykiXSwgWyIzMi02NCAoc21hbGwpIiwgInNpZ21hXjIvMzItNjQiLCAibi9CIHN0ZXBzIiwgIlZlcnkgZ29vZCIsICJTbWFsbCBtb2RlbHMsIFJMIl0sIFsiMjU2LTEwMjQgKG1lZGl1bSkiLCAic2lnbWFeMi8yNTYtMTAyNCIsICJuL0Igc3RlcHMiLCAiR29vZCIsICJTdGFuZGFyZCBJbWFnZU5ldCwgTkxQIl0sIFsiNDA5Ni0zMjc2OCAobGFyZ2UpIiwgInNpZ21hXjIvNDA5Ni0zMjc2OCIsICJuL0Igc3RlcHMiLCAiUmVkdWNlZCAoc2hhcnBlciBtaW5pbWEpIiwgIkRpc3RyaWJ1dGVkIHRyYWluaW5nLCByZXF1aXJlcyB3YXJtdXAiXSwgWyJGdWxsIGJhdGNoIChuKSIsICIwIChleGFjdCkiLCAiMSBzdGVwIiwgIldvcnN0IGdlbmVyYWxpemF0aW9uIiwgIkNvbnZleCBwcm9ibGVtcyBvbmx5Il1dfSwgeyJ0eXBlIjogImRpdmlkZXIifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJLZXkgVGFrZWF3YXlzIn0sIHsidHlwZSI6ICJsaXN0IiwgIml0ZW1zIjogWyJTR0QgZ3JhZGllbnQgZXN0aW1hdGUgZ19oYXQgPSAoMS9CKSpzdW0oZ3JhZChsX2kpKSBpcyB1bmJpYXNlZDogRVtnX2hhdF09Z3JhZChMKS4gVmFyaWFuY2UgaXMgc2lnbWFeMi9CIOKAlCByZWR1Y2VzIGxpbmVhcmx5IHdpdGggYmF0Y2ggc2l6ZS4iLCAiUm9iYmlucy1Nb25ybyBjb25kaXRpb25zIGZvciBjb252ZXJnZW5jZSB3aXRoIGRlY2F5aW5nIExSOiBzdW0oZXRhX3QpPWluZmluaXR5IChjYW4gcmVhY2ggYW55IHBvaW50KSBhbmQgc3VtKGV0YV90XjIpPGluZmluaXR5ICh2YXJpYW5jZSBzaHJpbmtzKS4gU2F0aXNmaWVkIGJ5IGV0YV90PWV0YV8wL3ReYWxwaGEgZm9yIGFscGhhIGluICgwLjUsMV0uIiwgIkxpbmVhciBzY2FsaW5nIHJ1bGU6IG11bHRpcGx5IExSIGJ5IGsgd2hlbiBtdWx0aXBseWluZyBiYXRjaCBzaXplIGJ5IGsuIEJyZWFrcyBhYm92ZSBjcml0aWNhbCBiYXRjaCBzaXplIEJfYyBhcHByb3ggc2lnbWFeMi98fGdyYWQoTCl8fF4yLiIsICJTR0Qgbm9pc2UgaW1wbGljaXRseSByZWd1bGFyaXplcyB0b3dhcmQgZmxhdCBtaW5pbWEg4oCUIHRoZXNlIGVtcGlyaWNhbGx5IGdlbmVyYWxpemUgYmV0dGVyIHRoYW4gZnVsbC1iYXRjaCBHRC4gVGhlIG5vaXNlIGFjdHMgYXMgYSBwZW5hbHR5IG9uIHRoZSBIZXNzaWFuIHRyYWNlLiIsICJHcmFkaWVudCBhY2N1bXVsYXRpb24gc2ltdWxhdGVzIGxhcmdlIGJhdGNoZXM6IGRpdmlkZSBsb3NzIGJ5IG5fYWNjdW11bGF0aW9uX3N0ZXBzLCBjbGlwIGFmdGVyIGZ1bGwgYWNjdW11bGF0aW9uLCBub3QgcGVyIG1pY3JvLWJhdGNoLiIsICJDb25zdGFudCBMUiBTR0Qgb3NjaWxsYXRlcyBhcm91bmQgbWluaW11bSAoZG9lcyBub3QgY29udmVyZ2UgdG8gaXQpLiBVc2UgZGVjYXlpbmcgTFIgb3IgUG9seWFrLVJ1cHBlcnQgYXZlcmFnaW5nIChhdmVyYWdlIG9mIGFsbCBpdGVyYXRlcykgZm9yIGV4YWN0IGNvbnZlcmdlbmNlLiIsICJBbHdheXMgc2h1ZmZsZSBkYXRhIGVhY2ggZXBvY2guIE5vdCBzaHVmZmxpbmcgd2l0aCBjb3JyZWxhdGVkIG1pbmktYmF0Y2hlcyBpbnRyb2R1Y2VzIGdyYWRpZW50IGJpYXMgYW5kIHNsb3dzIGNvbnZlcmdlbmNlIHNpZ25pZmljYW50bHkuIl19XQ=="
---

# SGD and Stochastic Approximation

Stochastic gradient descent replaces the expensive full-gradient with a cheap noisy estimate, enabling training on massive datasets. But SGD is not merely gradient descent with some noise added. The stochasticity fundamentally changes the algorithm's behavior: it enables escape from sharp minima, provides implicit regularization, and requires different convergence analysis (Robbins-Monro conditions). Understanding SGD through the lens of stochastic approximation theory — variance, bias, step-size conditions, and the generalization gap — is essential for diagnosing training instability, tuning batch size and learning rate, and understanding why SGD often generalizes better than Adam on image classification tasks despite Adam’s faster convergence speed during training.

## Core Definition: Stochastic Gradient Estimates

For a loss L(θ) = (1/n)Σᵢlᵢ(θ), the SGD gradient estimate using minibatch B⊆[n] of size B is ĝₜ = (1/|B|)Σᵢ∈B∇lᵢ(θₜ). Key properties: (1) Unbiasedness: E[ĝₜ|θₜ] = ∇L(θₜ). (2) Variance: Var[ĝₜ] = σ²/B where σ² = (1/n)Σᵢ‖∇lᵢ(θ)−∇L(θ)‖² is the per-sample gradient variance. (3) As B→n: full-batch gradient, zero noise. The gradient estimate enters the update: θₜ₊₁ = θₜ − ηₜĝₜ. The noise ζₜ = ĝₜ − ∇L(θₜ) has E[ζₜ]=0 (unbiased) but nonzero variance σ²/B. This noise fundamentally changes convergence behavior: SGD with constant LR does not converge to a stationary point but oscillates around one within a ball of radius proportional to ησ/√B.

```python
import numpy as np
import matplotlib.pyplot as plt

def sgd_variance_demo(n=1000, d=10, batch_sizes=[1, 32, 256, 1000], n_steps=500):
    """
    Demonstrate gradient variance vs batch size.
    Shows: Var[g_hat] approx sigma^2 / B (variance reduces linearly with B).
    """
    np.random.seed(42)
    X = np.random.randn(n, d)
    w_true = np.random.randn(d)
    y = X @ w_true + np.random.randn(n) * 0.5

    # Full gradient (ground truth)
    w = np.zeros(d)
    grad_true = 2 * X.T @ (X @ w - y) / n

    # Estimate gradient variance for each batch size
    results = {}
    for B in batch_sizes:
        grad_estimates = []
        for _ in range(200):  # 200 samples of gradient estimate
            idx = np.random.choice(n, B, replace=False)
            Xb, yb = X[idx], y[idx]
            g = 2 * Xb.T @ (Xb @ w - yb) / B
            grad_estimates.append(g)

        grad_estimates = np.array(grad_estimates)
        variance = grad_estimates.var(axis=0).mean()  # average variance across dims
        results[B] = variance
        print(f"B={B:5d}: gradient variance = {variance:.4f}")

    # Verify linear relationship: Var proportional to 1/B
    B_array = np.array(list(results.keys()))
    var_array = np.array(list(results.values()))
    sigma2_est = (var_array * B_array).mean()
    print(f"\nEstimated sigma^2 = {sigma2_est:.4f}")
    for B, var in zip(B_array, var_array):
        predicted = sigma2_est / B
        print(f"B={B}: actual={var:.4f}, predicted sigma^2/B={predicted:.4f}")

sgd_variance_demo()
```

## Robbins-Monro Convergence Conditions

The Robbins-Monro (1951) conditions for SGD convergence with decaying step sizes ηₜ are: (1) Σₜ ηₜ = ∞ (steps sum to infinity — ensures we can reach any point in parameter space); (2) Ση²ₜ < ∞ (sum of squared steps is finite — ensures variance shrinks fast enough for convergence). The canonical schedule ηₜ = η₀/t^α with α ∈ (0.5, 1] satisfies these conditions: Ση₀/t^α diverges (harmonic series for α=1), but Ση₀²/t^{2α} converges for 2α > 1. Under these conditions, SGD converges to a stationary point for non-convex f and to the global minimum for convex f. The decay must be slow enough (α ≤ 1) to explore the space, but fast enough (α > 0.5) to suppress noise and achieve convergence. Constant LR violates condition 2 — SGD oscillates permanently but can be averaged (Polyak-Ruppert averaging) for convergence.

```python
import numpy as np

def sgd_with_lr_schedule(grad_fn, theta0, n, schedule='decay', n_steps=2000, eta0=0.1):
    """
    Compare SGD with constant vs decaying learning rate.
    Also demonstrates Polyak-Ruppert averaging.
    """
    theta = theta0.copy()
    theta_avg = theta0.copy()  # Polyak-Ruppert average
    losses = []

    # True optimum for comparison (assume quadratic)
    f = lambda t: np.sum(t**2)

    for t in range(1, n_steps + 1):
        if schedule == 'decay':
            eta_t = eta0 / np.sqrt(t)  # alpha = 0.5: just barely satisfies R-M
        elif schedule == 'constant':
            eta_t = eta0
        else:
            eta_t = eta0 / t  # alpha = 1: satisfies R-M strongly

        # Noisy gradient (true gradient + noise)
        g_true = grad_fn(theta)
        noise = 0.1 * np.random.randn(len(theta))  # simulate SGD noise
        g_noisy = g_true + noise

        theta = theta - eta_t * g_noisy
        # Polyak-Ruppert: running average of iterates
        theta_avg = (theta_avg * (t - 1) + theta) / t

        if t % 100 == 0:
            losses.append((t, f(theta), f(theta_avg)))

    return losses

# Test on f(theta) = sum(theta^2), gradient = 2*theta
grad_fn = lambda theta: 2 * theta
theta0 = np.array([3.0, 2.0, 1.0])

print("Step  | theta_loss | theta_avg_loss | schedule")
for schedule in ['constant', 'decay', 't-decay']:
    losses = sgd_with_lr_schedule(grad_fn, theta0, n=100, schedule=schedule)
    final = losses[-1]
    print(f"{final[0]} | {final[1]:.4e} | {final[2]:.4e} | {schedule}")
```

## Linear Scaling Rule and Batch Size

The linear scaling rule (Goyal et al., Facebook 2017): when multiplying batch size by k, multiply the learning rate by k. Intuition: SGD with batch B and LR η updates using a gradient estimate with variance σ²/B. To maintain the same signal-to-noise ratio when doubling B, double η — this preserves gradient noise statistics per update. Formally: k steps of SGD with (B, η) approximate one step of SGD with (kB, kη) to first order in the step size. Limitations: the linear scaling rule breaks at very large batch sizes, beyond the critical batch size B_c ≈ σ²/‖∇L‖² — beyond this point, adding more samples does not proportionally reduce noise. Also, when using large batches (B>1024), always warm up the LR for the first few epochs, as the gradient variance is initially too high relative to the gradient signal to safely use the scaled LR.

## Implicit Regularization: Why SGD Generalizes Better

Empirically, SGD generalizes better than full-batch GD on image classification, even at equivalent training loss. The theoretical explanation: SGD's gradient noise induces an implicit bias toward flatter minima. Intuitively, a sharp minimum (high curvature) is unstable under gradient noise — the noise kicks the optimizer out of sharp minima, and it eventually settles in flat minima (wide basins) that are more robust to perturbation. Formally, the SGD dynamics (with finite LR η) can be written as following the gradient of f + (η/4B)ΔL, where ΔL is the trace of the Hessian — this penalizes high-curvature regions. Flat minima have better test generalization by the PAC-Bayes perspective: a flat minimum means a larger neighborhood of parameters with good loss, implying the solution is robust to the distribution shift between training and test sets.

```python
import torch
import torch.nn as nn
import numpy as np

def compare_sgd_batch_generalization(n_train=500, n_test=500, n_epochs=100):
    """
    Compare large-batch vs small-batch SGD on a simple overparameterized problem.
    Shows: small batch generalizes better (flatter minima).
    """
    torch.manual_seed(42)

    # Synthetic data: 2-class classification
    X_train = torch.randn(n_train, 20)
    y_train = (X_train[:, 0] > 0).float().unsqueeze(1)
    X_test = torch.randn(n_test, 20)
    y_test = (X_test[:, 0] > 0).float().unsqueeze(1)

    def make_model():
        return nn.Sequential(nn.Linear(20, 64), nn.ReLU(),
                              nn.Linear(64, 64), nn.ReLU(),
                              nn.Linear(64, 1), nn.Sigmoid())

    def train(model, batch_size, lr, n_epochs):
        opt = torch.optim.SGD(model.parameters(), lr=lr)
        criterion = nn.BCELoss()
        for epoch in range(n_epochs):
            idx = torch.randperm(n_train)
            for start in range(0, n_train, batch_size):
                Xb = X_train[idx[start:start+batch_size]]
                yb = y_train[idx[start:start+batch_size]]
                opt.zero_grad()
                loss = criterion(model(Xb), yb)
                loss.backward()
                opt.step()
        with torch.no_grad():
            train_acc = ((model(X_train) > 0.5) == y_train).float().mean()
            test_acc = ((model(X_test) > 0.5) == y_test).float().mean()
        return train_acc.item(), test_acc.item()

    # Linear scaling rule: large batch uses proportionally larger LR
    for batch_size, lr in [(8, 0.01), (256, 0.32)]:
        model = make_model()
        train_acc, test_acc = train(model, batch_size, lr, n_epochs)
        gen_gap = train_acc - test_acc
        print(f"B={batch_size:4d} lr={lr:.2f}: train={train_acc:.3f} test={test_acc:.3f} gap={gen_gap:.3f}")

compare_sgd_batch_generalization()
```

## Gradient Accumulation for Simulating Large Batches

When GPU memory limits batch size, gradient accumulation simulates larger effective batches: run B_micro micro-batches through forward and backward passes, accumulate gradients, then take one optimizer step. Effective batch size = B_micro × n_accumulation_steps. Critical implementation detail: divide loss by n_accumulation_steps before the backward pass (or set reduction='mean' within each micro-batch), otherwise gradients are scaled by n_accumulation_steps relative to the expected magnitude. This scaling matters especially for gradient clipping: always clip after accumulation using the accumulated gradient norm, not the per-micro-batch norm. This approach works identically to true large batch for deterministic models, but dropout and batch normalization behavior differ slightly (BN running statistics are computed on the micro-batch size, not the full accumulated effective batch).

```python
import torch
import torch.nn as nn

def training_loop_with_gradient_accumulation(
    model, optimizer, dataloader, n_accumulation_steps=4, clip_norm=1.0
):
    """
    Training loop with gradient accumulation.
    Effective batch size = loader batch_size * n_accumulation_steps.
    """
    model.train()
    criterion = nn.CrossEntropyLoss()
    total_loss = 0.0
    optimizer.zero_grad()

    for step, (X, y) in enumerate(dataloader):
        # Forward pass on micro-batch
        logits = model(X)
        # Divide loss by accumulation steps so gradients are correct scale
        loss = criterion(logits, y) / n_accumulation_steps
        loss.backward()

        total_loss += loss.item() * n_accumulation_steps

        # Every n_accumulation_steps, update parameters
        if (step + 1) % n_accumulation_steps == 0:
            # Clip AFTER accumulation (uses accumulated gradient norm)
            torch.nn.utils.clip_grad_norm_(model.parameters(), clip_norm)
            optimizer.step()
            optimizer.zero_grad()

            effective_step = (step + 1) // n_accumulation_steps
            avg_loss = total_loss / n_accumulation_steps
            if effective_step % 10 == 0:
                print(f"Step {effective_step}: loss={avg_loss:.4f}")
            total_loss = 0.0

    # Handle remaining micro-batches at end of epoch
    if (step + 1) % n_accumulation_steps != 0:
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip_norm)
        optimizer.step()
        optimizer.zero_grad()

print("Gradient accumulation training loop defined.")
print("Key: divide loss by n_accumulation_steps BEFORE backward.")
print("Key: clip gradients AFTER accumulation, not per micro-batch.")
```

## Implementation Pitfalls

Not shuffling data: if samples are ordered by class, cyclic SGD sees correlated batches, introducing systematic bias in gradient estimates. Always shuffle each epoch with torch.randperm(n). Forgetting to scale loss in gradient accumulation: if loss is not divided by n_accumulation_steps, effective LR increases by that factor — causing instability and potential divergence. Using batch norm with very small effective batch size: BN with B<8 produces noisy mean and variance statistics that hurt performance significantly. Use Group Norm or Layer Norm for small-batch training instead. Decreasing LR too fast: ηₜ = η₀/t (alpha=1) satisfies Robbins-Monro theoretically but converges very slowly in practice because the LR drops below the useful range quickly. Use ηₜ = η₀/√t or cosine annealing for better empirical performance and faster practical convergence.

## Practical Guidance

Start with B=256 and LR=0.1 for image classification with SGD+momentum. Scale both proportionally for different hardware (linear scaling rule up to B_critical ≈ 8192 for ImageNet). Use linear warmup over 5 epochs when using large batches (B>1024) to avoid instability from high initial gradient variance. Prefer cosine annealing over step decay — it produces smoother loss curves and avoids the need for manual schedule tuning. Monitor gradient variance across training steps (compute standard deviation of gradient estimates over several consecutive steps): if std/mean < 0.1, you can safely increase batch size; if > 10, the gradient is too noisy and batch size should increase. For NLP tasks with sparse features, prefer Adam over SGD — gradient variance is structurally higher in NLP due to sparse token gradients.

> **Constant LR Prevents True Convergence**: With constant learning rate eta, SGD converges to within a ball of radius O(eta*sigma/sqrt(B)) around the minimum, not to the exact minimum. To converge to a stationary point, you need decaying LR (Robbins-Monro) or Polyak-Ruppert averaging (average of all iterates). In practice, cosine annealing to a very small LR (1% of peak) approximates convergence. Alternatively, run SGD with constant LR and switch to full-batch GD for the last few steps for exact convergence.

| Batch Size B | Gradient Variance | Steps/Epoch | Generalization | Practical Use |
|---|---|---|---|---|
| 1 (true SGD) | sigma^2 | n steps | Best (flattest minima) | Rarely used (slow) |
| 32-64 (small) | sigma^2/32-64 | n/B steps | Very good | Small models, RL |
| 256-1024 (medium) | sigma^2/256-1024 | n/B steps | Good | Standard ImageNet, NLP |
| 4096-32768 (large) | sigma^2/4096-32768 | n/B steps | Reduced (sharper minima) | Distributed training, requires warmup |
| Full batch (n) | 0 (exact) | 1 step | Worst generalization | Convex problems only |

---

## Key Takeaways

- SGD gradient estimate g_hat = (1/B)*sum(grad(l_i)) is unbiased: E[g_hat]=grad(L). Variance is sigma^2/B — reduces linearly with batch size.
- Robbins-Monro conditions for convergence with decaying LR: sum(eta_t)=infinity (can reach any point) and sum(eta_t^2)<infinity (variance shrinks). Satisfied by eta_t=eta_0/t^alpha for alpha in (0.5,1].
- Linear scaling rule: multiply LR by k when multiplying batch size by k. Breaks above critical batch size B_c approx sigma^2/||grad(L)||^2.
- SGD noise implicitly regularizes toward flat minima — these empirically generalize better than full-batch GD. The noise acts as a penalty on the Hessian trace.
- Gradient accumulation simulates large batches: divide loss by n_accumulation_steps, clip after full accumulation, not per micro-batch.
- Constant LR SGD oscillates around minimum (does not converge to it). Use decaying LR or Polyak-Ruppert averaging (average of all iterates) for exact convergence.
- Always shuffle data each epoch. Not shuffling with correlated mini-batches introduces gradient bias and slows convergence significantly.

