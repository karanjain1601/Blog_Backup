---
title: "SGD and Stochastic Approximation"
slug: "sgd-stochastic-approximation"
description: "Deep dive into stochastic gradient descent: unbiased gradient estimates, variance scaling with batch size, Robbins-Monro convergence conditions, linear scaling rule, gradient accumulation, and why SGD noise aids generalization."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0b2NoYXN0aWMgR3JhZGllbnQgRXN0aW1hdGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikluc3RlYWQgb2YgY29tcHV0aW5nIHRoZSBmdWxsIGdyYWRpZW50IOKIh0wozrgpID0gKDEvTinOo+KIh+KEkyjOuCwgeF9pKSwgU0dEIGVzdGltYXRlcyBpdCB1c2luZyBhIHJhbmRvbSBtaW5pYmF0Y2ggQiBvZiBzaXplIEI6IGdfQiA9ICgxL0IpzqNfe2niiIhCfSDiiIfihJMozrgsIHhfaSkuIFRoaXMgZXN0aW1hdGUgaXMgdW5iaWFzZWQg4oCUIGl0cyBleHBlY3RhdGlvbiBlcXVhbHMgdGhlIHRydWUgZ3JhZGllbnQg4oCUIGJ1dCBoYXMgdmFyaWFuY2UgdGhhdCBkZWNyZWFzZXMgd2l0aCBCLiBUaGUgdXBkYXRlIHJ1bGUgYmVjb21lcyDOuCDihpAgzrgg4oiSIM63IGdfQi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVbmJpYXNlZG5lc3MgYW5kIFZhcmlhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJZiBzYW1wbGVzIGFyZSBkcmF3biBpLmkuZC4sIHRoZSBtaW5pYmF0Y2ggZ3JhZGllbnQgaXMgdW5iaWFzZWQ6IEVbZ19CXSA9IOKIh0wozrgpLiBUaGUgdmFyaWFuY2Ugc2NhbGVzIGludmVyc2VseSB3aXRoIGJhdGNoIHNpemU6IFZhcltnX0JdID0gz4PCsi9CLCB3aGVyZSDPg8KyID0gRVvigJbiiIfihJMozrgsIHhfaSkg4oiSIOKIh0wozrgp4oCWwrJdIGlzIHRoZSBwZXItc2FtcGxlIGdyYWRpZW50IHZhcmlhbmNlLiBUaGlzIG1lYW5zIGRvdWJsaW5nIHRoZSBiYXRjaCBzaXplIGhhbHZlcyB0aGUgZ3JhZGllbnQgbm9pc2UsIGJ1dCB0aGUgYmVuZWZpdCBpcyBzdWJsaW5lYXIg4oCUIHlvdSBwYXkgdHdpY2UgdGhlIGNvbXB1dGUgZm9yIGhhbGYgdGhlIHZhcmlhbmNlIHJlZHVjdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuTiwgZCA9IDEwMDAsIDEwXG5YID0gbnAucmFuZG9tLnJhbmRuKE4sIGQpXG53X3RydWUgPSBucC5yYW5kb20ucmFuZG4oZClcbnkgPSBYIEAgd190cnVlICsgMC4xICogbnAucmFuZG9tLnJhbmRuKE4pXG5cbmRlZiBtaW5pYmF0Y2hfc2dkKFgsIHksIGxyPTAuMDUsIGJhdGNoX3NpemU9MzIsIGVwb2Nocz01MCk6XG4gICAgbiwgZCA9IFguc2hhcGVcbiAgICB3ID0gbnAuemVyb3MoZClcbiAgICBsb3NzZXMgPSBbXVxuICAgIGZvciBlcG9jaCBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICBpZHggPSBucC5yYW5kb20ucGVybXV0YXRpb24obilcbiAgICAgICAgWF9zLCB5X3MgPSBYW2lkeF0sIHlbaWR4XVxuICAgICAgICBmb3IgaSBpbiByYW5nZSgwLCBuLCBiYXRjaF9zaXplKTpcbiAgICAgICAgICAgIFhiID0gWF9zW2k6aStiYXRjaF9zaXplXVxuICAgICAgICAgICAgeWIgPSB5X3NbaTppK2JhdGNoX3NpemVdXG4gICAgICAgICAgICBncmFkID0gKDIgLyBsZW4oWGIpKSAqIFhiLlQgQCAoWGIgQCB3IC0geWIpXG4gICAgICAgICAgICB3ID0gdyAtIGxyICogZ3JhZFxuICAgICAgICBsb3NzID0gbnAubWVhbigoWCBAIHcgLSB5KSoqMilcbiAgICAgICAgbG9zc2VzLmFwcGVuZChsb3NzKVxuICAgIHJldHVybiB3LCBsb3NzZXNcblxud19oYXQsIGxvc3NlcyA9IG1pbmliYXRjaF9zZ2QoWCwgeSwgbHI9MC4wNSwgYmF0Y2hfc2l6ZT0zMiwgZXBvY2hzPTYwKVxucGx0LmZpZ3VyZShmaWdzaXplPSg3LCAzKSlcbnBsdC5wbG90KGxvc3NlcylcbnBsdC54bGFiZWwoXHUwMDI3RXBvY2hcdTAwMjcpOyBwbHQueWxhYmVsKFx1MDAyN01TRVx1MDAyNylcbnBsdC50aXRsZShcdTAwMjdNaW5pYmF0Y2ggU0dEIENvbnZlcmdlbmNlIChCPTMyKVx1MDAyNylcbnBsdC5ncmlkKFRydWUsIGFscGhhPTAuMylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3c2dkX2NvbnZlcmdlbmNlLnBuZ1x1MDAyNywgZHBpPTE1MClcbnBsdC5zaG93KClcbnByaW50KGZcdTAwMjdXZWlnaHQgZXJyb3I6IHtucC5saW5hbGcubm9ybSh3X2hhdCAtIHdfdHJ1ZSk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdGaW5hbCBsb3NzOiB7bG9zc2VzWy0xXTouNmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiU2FtcGxpbmcgV2l0aG91dCBSZXBsYWNlbWVudCIsImNvbnRlbnQiOiJBbHdheXMgc2h1ZmZsZSBkYXRhIGFuZCBpdGVyYXRlIHdpdGhvdXQgcmVwbGFjZW1lbnQgd2l0aGluIGVhY2ggZXBvY2ggKG5vdCB3aXRoIHJlcGxhY2VtZW50KS4gV2l0aG91dC1yZXBsYWNlbWVudCBzYW1wbGluZyByZWR1Y2VzIHZhcmlhbmNlIGFuZCBpcyBndWFyYW50ZWVkIHRvIHNlZSBhbGwgZGF0YSBlYWNoIGVwb2NoLiBQeVRvcmNoIERhdGFMb2FkZXIgd2l0aCBzaHVmZmxlPVRydWUgZG9lcyB0aGlzIGNvcnJlY3RseS4gRHJhd2luZyB3aXRoIHJlcGxhY2VtZW50ICh0cnVlIFNHRCkgaGFzIGhpZ2hlciB2YXJpYW5jZSBhbmQgc2xvd2VyIGNvbnZlcmdlbmNlIGluIHByYWN0aWNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJvYmJpbnMtTW9ucm8gQ29udmVyZ2VuY2UgQ29uZGl0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIFNHRCB3aXRoIGRpbWluaXNoaW5nIGxlYXJuaW5nIHJhdGVzIHRvIGNvbnZlcmdlIGFsbW9zdCBzdXJlbHkgdG8gYSBzdGF0aW9uYXJ5IHBvaW50LCB0aGUgUm9iYmlucy1Nb25ybyBjb25kaXRpb25zIG11c3QgaG9sZDogKDEpIM6jX3t0PTF9XuKIniDOt190ID0g4oieIChsZWFybmluZyByYXRlcyBzdW0gdG8gaW5maW5pdHksIGVuc3VyaW5nIHRoZSBhbGdvcml0aG0gY2FuIHRyYXZlbCBhbnkgZGlzdGFuY2UpIGFuZCAoMikgzqNfe3Q9MX1e4oieIM63X3TCsiBcdTAwM2Mg4oieIChzcXVhcmVkIGxlYXJuaW5nIHJhdGVzIGFyZSBzdW1tYWJsZSwgZW5zdXJpbmcgbm9pc2UgYXZlcmFnZXMgb3V0KS4gVGhlIHNjaGVkdWxlIM63X3QgPSBjL3Qgc2F0aXNmaWVzIGJvdGggY29uZGl0aW9ucy4gQ29uc3RhbnQgbGVhcm5pbmcgcmF0ZXMgdmlvbGF0ZSBjb25kaXRpb24gMjogU0dEIG9zY2lsbGF0ZXMgYXJvdW5kIHRoZSBtaW5pbXVtIHJhdGhlciB0aGFuIGNvbnZlcmdpbmcgdG8gaXQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmF0Y2ggU2l6ZSBFZmZlY3RzIG9uIFZhcmlhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbmNyZWFzaW5nIHRoZSBiYXRjaCBzaXplIHJlZHVjZXMgZ3JhZGllbnQgdmFyaWFuY2UgYXQgdGhlIGNvc3Qgb2YgbW9yZSBjb21wdXRlIHBlciBzdGVwLiBUaGUgcmVsYXRpb25zaGlwIGlzIGxpbmVhcjogZG91YmxpbmcgQiBoYWx2ZXMgdGhlIHZhcmlhbmNlLiBIb3dldmVyLCB0aGUgY29udmVyZ2VuY2UgYmVuZWZpdCBpbiB0ZXJtcyBvZiBlcG9jaHMgKG5vdCBzdGVwcykgaXMgc3VibGluZWFyIOKAlCBsYXJnZSBiYXRjaGVzIHJlcXVpcmUgbW9yZSB0b3RhbCBjb21wdXRhdGlvbiB0byBtYXRjaCBzbWFsbC1iYXRjaCBjb252ZXJnZW5jZS4gVGhpcyBpcyBrbm93biBhcyB0aGUgbGluZWFyIHNjYWxpbmcgZGVncmFkYXRpb246IGJleW9uZCBhIGNyaXRpY2FsIGJhdGNoIHNpemUsIGxhcmdlciBiYXRjaGVzIHByb3ZpZGUgZGltaW5pc2hpbmcgcmV0dXJucyBwZXIgdW5pdCBvZiBjb21wdXRlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxubnAucmFuZG9tLnNlZWQoMClcbk4sIGQgPSA1MDAsIDVcblggPSBucC5yYW5kb20ucmFuZG4oTiwgZClcbnkgPSBYIEAgbnAub25lcyhkKSArIDAuMSAqIG5wLnJhbmRvbS5yYW5kbihOKVxuXG5kZWYgc2dkX2Vwb2NoX2xvc3NlcyhYLCB5LCBicywgbHI9MC4wNSwgZXBvY2hzPTQwKTpcbiAgICB3ID0gbnAuemVyb3MoWC5zaGFwZVsxXSlcbiAgICBsb3NzZXMgPSBbXVxuICAgIGZvciBfIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIGlkeCA9IG5wLnJhbmRvbS5wZXJtdXRhdGlvbihsZW4oWCkpXG4gICAgICAgIGZvciBpIGluIHJhbmdlKDAsIGxlbihYKSwgYnMpOlxuICAgICAgICAgICAgWGIgPSBYW2lkeFtpOmkrYnNdXVxuICAgICAgICAgICAgeWIgPSB5W2lkeFtpOmkrYnNdXVxuICAgICAgICAgICAgdyAtPSBsciAqICgyL2xlbihYYikpICogWGIuVCBAIChYYiBAIHcgLSB5YilcbiAgICAgICAgbG9zc2VzLmFwcGVuZChmbG9hdChucC5tZWFuKChYIEAgdyAtIHkpKioyKSkpXG4gICAgcmV0dXJuIGxvc3Nlc1xuXG5iYXRjaF9jb25maWdzID0gW1xuICAgICgxLCAgIFx1MDAyN1NHRCBCPTEgKG5vaXN5KVx1MDAyNyksXG4gICAgKDMyLCAgXHUwMDI3TWluaS1iYXRjaCBCPTMyXHUwMDI3KSxcbiAgICAoMTI4LCBcdTAwMjdMYXJnZSBiYXRjaCBCPTEyOFx1MDAyNyksXG4gICAgKE4sICAgXHUwMDI3RnVsbC1iYXRjaCBHRFx1MDAyNylcbl1cbnBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpXG5mb3IgYnMsIGxibCBpbiBiYXRjaF9jb25maWdzOlxuICAgIHBsdC5wbG90KHNnZF9lcG9jaF9sb3NzZXMoWCwgeSwgYnMpLCBsYWJlbD1sYmwpXG5wbHQueGxhYmVsKFx1MDAyN0Vwb2NoXHUwMDI3KVxucGx0LnlsYWJlbChcdTAwMjdNU0UgTG9zc1x1MDAyNylcbnBsdC50aXRsZShcdTAwMjdFZmZlY3Qgb2YgQmF0Y2ggU2l6ZSBvbiBQZXItRXBvY2ggQ29udmVyZ2VuY2VcdTAwMjcpXG5wbHQubGVnZW5kKClcbnBsdC55c2NhbGUoXHUwMDI3bG9nXHUwMDI3KVxucGx0LmdyaWQoVHJ1ZSwgYWxwaGE9MC4zKVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdiYXRjaF9zaXplcy5wbmdcdTAwMjcsIGRwaT0xNTApXG5wbHQuc2hvdygpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGF0YSBTaHVmZmxpbmcgUGVyIEVwb2NoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaHVmZmxpbmcgdGhlIGRhdGFzZXQgYmVmb3JlIGVhY2ggZXBvY2ggaXMgY3JpdGljYWwgZm9yIGNvbnZlcmdlbmNlLiBXaXRob3V0IHNodWZmbGluZywgdGhlIG9wdGltaXplciBzZWVzIHRoZSBzYW1lIHNlcXVlbmNlIG9mIGdyYWRpZW50IGRpcmVjdGlvbnMgZWFjaCBlcG9jaCwgd2hpY2ggY2FuIGNyZWF0ZSBwZXJpb2RpYyBiaWFzZXMuIFdpdGggc2h1ZmZsaW5nLCBlYWNoIGVwb2NoIHByb3ZpZGVzIGEgZnJlc2ggcmFuZG9tIG9yZGVyaW5nLCByZWR1Y2luZyB0aGUgY29ycmVsYXRpb24gYmV0d2VlbiBjb25zZWN1dGl2ZSB1cGRhdGVzLiBUaGVvcmV0aWNhbCBhbmFseXNpcyBzaG93cyB0aGF0IHdpdGhvdXQtcmVwbGFjZW1lbnQgc2FtcGxpbmcgYWNoaWV2ZXMgbG93ZXIgdmFyaWFuY2UgdGhhbiB3aXRoLXJlcGxhY2VtZW50ICh0cnVlIFNHRCksIGVzcGVjaWFsbHkgd2hlbiBOL0IgaXMgc21hbGwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIExpbmVhciBTY2FsaW5nIFJ1bGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gaW5jcmVhc2luZyBiYXRjaCBzaXplIGJ5IGEgZmFjdG9yIGssIG11bHRpcGx5IHRoZSBsZWFybmluZyByYXRlIGJ5IGsgYXMgd2VsbCAodGhlIGxpbmVhciBzY2FsaW5nIHJ1bGUsIGZyb20gR295YWwgZXQgYWwuIDIwMTcpLiBUaGUgaW50dWl0aW9uOiB3aXRoIGsgdGltZXMgbGFyZ2VyIGJhdGNoZXMsIGVhY2ggc3RlcCBpcyBrIHRpbWVzIGxlc3Mgbm9pc3ksIHNvIHlvdSBjYW4gdGFrZSBrIHRpbWVzIGxhcmdlciBzdGVwcy4gVGhpcyBydWxlIGhvbGRzIGVtcGlyaWNhbGx5IGZvciBtb2RlcmF0ZSBzY2FsaW5nICh1cCB0byBCPTgxOTIgZm9yIFJlc05ldHMpIGJ1dCBicmVha3MgYXQgdmVyeSBsYXJnZSBiYXRjaGVzLCB3aGVyZSBhIGxpbmVhciB3YXJtdXAgb2YgdGhlIGxlYXJuaW5nIHJhdGUgaXMgbmVlZGVkIHRvIHN0YWJpbGl6ZSBlYXJseSB0cmFpbmluZy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQmF0Y2ggc2l6ZSIsIlNjYWxlIGZhY3RvciB2cyBCPTMyIiwiU2NhbGVkIExSIChiYXNlIGxyPTAuMSkiLCJOb3RlcyJdLCJyb3dzIjpbWyIzMiAoYmFzZWxpbmUpIiwiMcOXIiwiMC4xIiwiUmVmZXJlbmNlIHBvaW50Il0sWyI2NCIsIjLDlyIsIjAuMiIsIlNpbXBsZSBzY2FsaW5nLCBzdGFibGUiXSxbIjI1NiIsIjjDlyIsIjAuOCIsIk5lZWRzIHNob3J0IExSIHdhcm11cCJdLFsiMTAyNCIsIjMyw5ciLCIzLjIiLCJXYXJtdXAgZXNzZW50aWFsOyBtYXkgbmVlZCBMUiBjbGlwcGluZyJdLFsiNDA5NiIsIjEyOMOXIiwiMTIuOCIsIkxpbmVhciBydWxlIG9mdGVuIGJyZWFrczsgdXNlIHNxcnQgc2NhbGluZyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgQWNjdW11bGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIEdQVSBtZW1vcnkgbGltaXRzIGJhdGNoIHNpemUsIGdyYWRpZW50IGFjY3VtdWxhdGlvbiBzaW11bGF0ZXMgYSBsYXJnZSBiYXRjaCB3aXRob3V0IGV4dHJhIG1lbW9yeS4gUnVuIEsgZm9yd2FyZC1iYWNrd2FyZCBwYXNzZXMgb24gbWljcm8tYmF0Y2hlcywgYWNjdW11bGF0aW5nIChzdW1taW5nKSBncmFkaWVudHMsIHRoZW4gcGVyZm9ybSBvbmUgb3B0aW1pemVyIHN0ZXAuIFRoZSBlZmZlY3RpdmUgYmF0Y2ggc2l6ZSBpcyBLIMOXIG1pY3JvX2JhdGNoX3NpemUuIFRoZSBrZXkgaW1wbGVtZW50YXRpb24gZGV0YWlsOiBkaXZpZGUgbG9zcyBieSBLIGJlZm9yZSBiYWNrd2FyZCBzbyB0aGUgYWNjdW11bGF0ZWQgZ3JhZGllbnQgaGFzIHRoZSBjb3JyZWN0IHNjYWxlIChhdmVyYWdlIG92ZXIgYWxsIEsgbWljcm8tYmF0Y2hlcywgbm90IHN1bSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5YX2RhdGEgPSB0b3JjaC5yYW5kbigyNTYsIDIwKVxueV9kYXRhID0gdG9yY2gucmFuZG4oMjU2LCAxKVxuXG5kZWYgdHJhaW5fd2l0aF9hY2N1bXVsYXRpb24oYWNjdW1fc3RlcHM9OCwgbWljcm9fYmF0Y2g9MTYsIGVwb2Nocz01KTpcbiAgICBtb2RlbCA9IG5uLkxpbmVhcigyMCwgMSlcbiAgICBvcHRpbWl6ZXIgPSBvcHRpbS5TR0QobW9kZWwucGFyYW1ldGVycygpLCBscj0wLjAxKVxuICAgIGNyaXRlcmlvbiA9IG5uLk1TRUxvc3MoKVxuICAgIGRhdGFzZXQgPSB0b3JjaC51dGlscy5kYXRhLlRlbnNvckRhdGFzZXQoWF9kYXRhLCB5X2RhdGEpXG4gICAgbG9hZGVyID0gdG9yY2gudXRpbHMuZGF0YS5EYXRhTG9hZGVyKGRhdGFzZXQsIGJhdGNoX3NpemU9bWljcm9fYmF0Y2gsIHNodWZmbGU9VHJ1ZSlcbiAgICBhbGxfbG9zc2VzID0gW11cbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgIGFjY3VtX2NvdW50ID0gMFxuICAgICAgICBmb3IgaSwgKHhiLCB5YikgaW4gZW51bWVyYXRlKGxvYWRlcik6XG4gICAgICAgICAgICAjIERpdmlkZSBieSBhY2N1bV9zdGVwcyBzbyBhY2N1bXVsYXRlZCBncmFkID0gbWVhbiBvdmVyIGVmZmVjdGl2ZSBiYXRjaFxuICAgICAgICAgICAgbG9zcyA9IGNyaXRlcmlvbihtb2RlbCh4YiksIHliKSAvIGFjY3VtX3N0ZXBzXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIGFjY3VtX2NvdW50ICs9IDFcbiAgICAgICAgICAgIGlmIGFjY3VtX2NvdW50ID09IGFjY3VtX3N0ZXBzOlxuICAgICAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgICAgICAgICBhY2N1bV9jb3VudCA9IDBcbiAgICAgICAgICAgICAgICBhbGxfbG9zc2VzLmFwcGVuZChsb3NzLml0ZW0oKSAqIGFjY3VtX3N0ZXBzKVxuICAgIHJldHVybiBhbGxfbG9zc2VzXG5cbiMgRWZmZWN0aXZlIGJhdGNoIHNpemUgPSAxNiAqIDggPSAxMjhcbmxvc3NlcyA9IHRyYWluX3dpdGhfYWNjdW11bGF0aW9uKGFjY3VtX3N0ZXBzPTgsIG1pY3JvX2JhdGNoPTE2KVxucHJpbnQoZlx1MDAyN1N0ZXBzOiB7bGVuKGxvc3Nlcyl9LCBGaW5hbCBsb3NzOiB7bG9zc2VzWy0xXTouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3R3JhZGllbnQgYWNjdW11bGF0aW9uOiBlZmZlY3RpdmUgYmF0Y2g9MTI4IHVzaW5nIG1pY3JvX2JhdGNoPTE2XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNHRCBOb2lzZSBhbmQgR2VuZXJhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNHRCBub2lzZSBkb2VzIG5vdCBqdXN0IHNsb3cgY29udmVyZ2VuY2Ug4oCUIGl0IGNhbiBhY3RpdmVseSBpbXByb3ZlIGdlbmVyYWxpemF0aW9uLiBUaGUgbm9pc2UgYWN0cyBhcyBhbiBpbXBsaWNpdCByZWd1bGFyaXplciwgYmlhc2luZyB0aGUgb3B0aW1pemVyIHRvd2FyZCBmbGF0IG1pbmltYSAobG93IGN1cnZhdHVyZSByZWdpb25zIG9mIHRoZSBsb3NzIGxhbmRzY2FwZSkuIEZsYXQgbWluaW1hIGdlbmVyYWxpemUgYmV0dGVyIGJlY2F1c2Ugc21hbGwgcGVydHVyYmF0aW9ucyB0byB3ZWlnaHRzIGNhdXNlIHNtYWxsIGNoYW5nZXMgaW4gbG9zcy4gTGFyZ2UtYmF0Y2ggR0QgY29udmVyZ2VzIHRvIHNoYXJwIG1pbmltYSB0aGF0IGdlbmVyYWxpemUgd29yc2UsIGEgcGhlbm9tZW5vbiBjb25maXJtZWQgZW1waXJpY2FsbHkgYnkgS2Vza2FyIGV0IGFsLiAoMjAxNikuIFRoaXMgaXMgd2h5IHNtYWxsLWJhdGNoIFNHRCBvZnRlbiBvdXRwZXJmb3JtcyBsYXJnZS1iYXRjaCBHRCBvbiB0ZXN0IGFjY3VyYWN5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbnRvcmNoLm1hbnVhbF9zZWVkKDcpXG5YX3RyID0gdG9yY2gucmFuZG4oNTAsIDgpXG55X3RyID0gKFhfdHJbOiwgMF0gXHUwMDNlIDApLmZsb2F0KCkudW5zcXVlZXplKDEpXG5YX3RlID0gdG9yY2gucmFuZG4oMjAwLCA4KVxueV90ZSA9IChYX3RlWzosIDBdIFx1MDAzZSAwKS5mbG9hdCgpLnVuc3F1ZWV6ZSgxKVxuXG5kZWYgdHJhaW5fZXZhbChiYXRjaF9zaXplLCBscj0wLjEsIGVwb2Nocz0xMDApOlxuICAgIG1vZGVsID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoOCwgMzIpLCBubi5SZUxVKCksIG5uLkxpbmVhcigzMiwgMSksIG5uLlNpZ21vaWQoKSlcbiAgICBvcHQgPSBvcHRpbS5TR0QobW9kZWwucGFyYW1ldGVycygpLCBscj1scilcbiAgICBjcml0ID0gbm4uQkNFTG9zcygpXG4gICAgdHJfbG9zc2VzLCB0ZV9sb3NzZXMgPSBbXSwgW11cbiAgICBkcyA9IHRvcmNoLnV0aWxzLmRhdGEuVGVuc29yRGF0YXNldChYX3RyLCB5X3RyKVxuICAgIGxvYWRlciA9IHRvcmNoLnV0aWxzLmRhdGEuRGF0YUxvYWRlcihkcywgYmF0Y2hfc2l6ZT1iYXRjaF9zaXplLCBzaHVmZmxlPVRydWUpXG4gICAgZm9yIF8gaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgZm9yIHhiLCB5YiBpbiBsb2FkZXI6XG4gICAgICAgICAgICBvcHQuemVyb19ncmFkKCk7IGNyaXQobW9kZWwoeGIpLCB5YikuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIHRyX2xvc3Nlcy5hcHBlbmQoY3JpdChtb2RlbChYX3RyKSwgeV90cikuaXRlbSgpKVxuICAgICAgICAgICAgdGVfbG9zc2VzLmFwcGVuZChjcml0KG1vZGVsKFhfdGUpLCB5X3RlKS5pdGVtKCkpXG4gICAgcmV0dXJuIHRyX2xvc3NlcywgdGVfbG9zc2VzXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMSwgNCkpXG5mb3IgYnMsIGxibCBpbiBbKDEsIFx1MDAyN1NHRCBCPTEgKG5vaXN5KVx1MDAyNyksICg1MCwgXHUwMDI3RnVsbC1iYXRjaCBHRFx1MDAyNyldOlxuICAgIHRyLCB0ZSA9IHRyYWluX2V2YWwoYnMpXG4gICAgYXhlc1swXS5wbG90KHRyLCBsYWJlbD1sYmwpOyBheGVzWzFdLnBsb3QodGUsIGxhYmVsPWxibClcbmZvciBheCwgdCBpbiB6aXAoYXhlcywgW1x1MDAyN1RyYWluIExvc3NcdTAwMjcsIFx1MDAyN1Rlc3QgTG9zcyAoR2VuZXJhbGl6YXRpb24pXHUwMDI3XSk6XG4gICAgYXguc2V0X3hsYWJlbChcdTAwMjdFcG9jaFx1MDAyNyk7IGF4LmxlZ2VuZCgpOyBheC5zZXRfdGl0bGUodClcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3c2dkX2dlbmVyYWxpemF0aW9uLnBuZ1x1MDAyNywgZHBpPTE1MClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIk1pbmliYXRjaCBncmFkaWVudCBpcyB1bmJpYXNlZDogRVtnX0JdID0g4oiHTCjOuCkiLCJWYXJpYW5jZSBzY2FsZXMgYXMgz4PCsi9CIOKAlCBkb3VibGluZyBiYXRjaCBoYWx2ZXMgbm9pc2UiLCJSb2JiaW5zLU1vbnJvOiBuZWVkIM6jzrdfdD3iiJ4gYW5kIM6jzrdfdMKyXHUwMDNj4oieIGZvciBjb252ZXJnZW5jZSIsIkxpbmVhciBzY2FsaW5nIHJ1bGU6IGxyIOKInSBCLCBzY2FsZSB1cCBwcm9wb3J0aW9uYWxseSIsIlNHRCBub2lzZSBiaWFzZXMgdG93YXJkIGZsYXQgbWluaW1hIOKAlCBiZXR0ZXIgZ2VuZXJhbGl6YXRpb24gdGhhbiBsYXJnZS1iYXRjaCBHRCJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQmVzdCBQcmFjdGljZSIsImNvbnRlbnQiOiJVc2UgYmF0Y2ggc2l6ZSAyNTbigJMxMDI0IGZvciB2aXNpb24gdGFza3MgYW5kIDMy4oCTMTI4IGZvciBOTFAuIFNjYWxlIGxlYXJuaW5nIHJhdGUgbGluZWFybHkgd2l0aCBiYXRjaCBzaXplIGZyb20gYSBiYXNlIGxyIGF0IEI9MzIgb3IgQj02NC4gVXNlIDXigJMxMCUgb2YgdG90YWwgdHJhaW5pbmcgc3RlcHMgYXMgbGluZWFyIExSIHdhcm11cCB3aGVuIHVzaW5nIGxhcmdlIGJhdGNoZXMuIEdyYWRpZW50IGFjY3VtdWxhdGlvbiBpcyBhIHByYWN0aWNhbCB3b3JrYXJvdW5kIHdoZW4gR1BVIG1lbW9yeSBpcyB0aGUgYm90dGxlbmVjay4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# SGD and Stochastic Approximation

## Stochastic Gradient Estimate

Instead of computing the full gradient ∇L(θ) = (1/N)Σ∇ℓ(θ, x_i), SGD estimates it using a random minibatch B of size B: g_B = (1/B)Σ_{i∈B} ∇ℓ(θ, x_i). This estimate is unbiased — its expectation equals the true gradient — but has variance that decreases with B. The update rule becomes θ ← θ − η g_B.

## Unbiasedness and Variance

If samples are drawn i.i.d., the minibatch gradient is unbiased: E[g_B] = ∇L(θ). The variance scales inversely with batch size: Var[g_B] = σ²/B, where σ² = E[‖∇ℓ(θ, x_i) − ∇L(θ)‖²] is the per-sample gradient variance. This means doubling the batch size halves the gradient noise, but the benefit is sublinear — you pay twice the compute for half the variance reduction.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N, d = 1000, 10
X = np.random.randn(N, d)
w_true = np.random.randn(d)
y = X @ w_true + 0.1 * np.random.randn(N)

def minibatch_sgd(X, y, lr=0.05, batch_size=32, epochs=50):
    n, d = X.shape
    w = np.zeros(d)
    losses = []
    for epoch in range(epochs):
        idx = np.random.permutation(n)
        X_s, y_s = X[idx], y[idx]
        for i in range(0, n, batch_size):
            Xb = X_s[i:i+batch_size]
            yb = y_s[i:i+batch_size]
            grad = (2 / len(Xb)) * Xb.T @ (Xb @ w - yb)
            w = w - lr * grad
        loss = np.mean((X @ w - y)**2)
        losses.append(loss)
    return w, losses

w_hat, losses = minibatch_sgd(X, y, lr=0.05, batch_size=32, epochs=60)
plt.figure(figsize=(7, 3))
plt.plot(losses)
plt.xlabel('Epoch'); plt.ylabel('MSE')
plt.title('Minibatch SGD Convergence (B=32)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sgd_convergence.png', dpi=150)
plt.show()
print(f'Weight error: {np.linalg.norm(w_hat - w_true):.4f}')
print(f'Final loss: {losses[-1]:.6f}')
```

> **Sampling Without Replacement**: Always shuffle data and iterate without replacement within each epoch (not with replacement). Without-replacement sampling reduces variance and is guaranteed to see all data each epoch. PyTorch DataLoader with shuffle=True does this correctly. Drawing with replacement (true SGD) has higher variance and slower convergence in practice.

## Robbins-Monro Convergence Conditions

For SGD with diminishing learning rates to converge almost surely to a stationary point, the Robbins-Monro conditions must hold: (1) Σ_{t=1}^∞ η_t = ∞ (learning rates sum to infinity, ensuring the algorithm can travel any distance) and (2) Σ_{t=1}^∞ η_t² < ∞ (squared learning rates are summable, ensuring noise averages out). The schedule η_t = c/t satisfies both conditions. Constant learning rates violate condition 2: SGD oscillates around the minimum rather than converging to it.

## Batch Size Effects on Variance

Increasing the batch size reduces gradient variance at the cost of more compute per step. The relationship is linear: doubling B halves the variance. However, the convergence benefit in terms of epochs (not steps) is sublinear — large batches require more total computation to match small-batch convergence. This is known as the linear scaling degradation: beyond a critical batch size, larger batches provide diminishing returns per unit of compute.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
N, d = 500, 5
X = np.random.randn(N, d)
y = X @ np.ones(d) + 0.1 * np.random.randn(N)

def sgd_epoch_losses(X, y, bs, lr=0.05, epochs=40):
    w = np.zeros(X.shape[1])
    losses = []
    for _ in range(epochs):
        idx = np.random.permutation(len(X))
        for i in range(0, len(X), bs):
            Xb = X[idx[i:i+bs]]
            yb = y[idx[i:i+bs]]
            w -= lr * (2/len(Xb)) * Xb.T @ (Xb @ w - yb)
        losses.append(float(np.mean((X @ w - y)**2)))
    return losses

batch_configs = [
    (1,   'SGD B=1 (noisy)'),
    (32,  'Mini-batch B=32'),
    (128, 'Large batch B=128'),
    (N,   'Full-batch GD')
]
plt.figure(figsize=(9, 4))
for bs, lbl in batch_configs:
    plt.plot(sgd_epoch_losses(X, y, bs), label=lbl)
plt.xlabel('Epoch')
plt.ylabel('MSE Loss')
plt.title('Effect of Batch Size on Per-Epoch Convergence')
plt.legend()
plt.yscale('log')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('batch_sizes.png', dpi=150)
plt.show()
```

## Data Shuffling Per Epoch

Shuffling the dataset before each epoch is critical for convergence. Without shuffling, the optimizer sees the same sequence of gradient directions each epoch, which can create periodic biases. With shuffling, each epoch provides a fresh random ordering, reducing the correlation between consecutive updates. Theoretical analysis shows that without-replacement sampling achieves lower variance than with-replacement (true SGD), especially when N/B is small.

## The Linear Scaling Rule

When increasing batch size by a factor k, multiply the learning rate by k as well (the linear scaling rule, from Goyal et al. 2017). The intuition: with k times larger batches, each step is k times less noisy, so you can take k times larger steps. This rule holds empirically for moderate scaling (up to B=8192 for ResNets) but breaks at very large batches, where a linear warmup of the learning rate is needed to stabilize early training.

| Batch size | Scale factor vs B=32 | Scaled LR (base lr=0.1) | Notes |
| --- | --- | --- | --- |
| 32 (baseline) | 1× | 0.1 | Reference point |
| 64 | 2× | 0.2 | Simple scaling, stable |
| 256 | 8× | 0.8 | Needs short LR warmup |
| 1024 | 32× | 3.2 | Warmup essential; may need LR clipping |
| 4096 | 128× | 12.8 | Linear rule often breaks; use sqrt scaling |

## Gradient Accumulation

When GPU memory limits batch size, gradient accumulation simulates a large batch without extra memory. Run K forward-backward passes on micro-batches, accumulating (summing) gradients, then perform one optimizer step. The effective batch size is K × micro_batch_size. The key implementation detail: divide loss by K before backward so the accumulated gradient has the correct scale (average over all K micro-batches, not sum).

```python
import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(42)
X_data = torch.randn(256, 20)
y_data = torch.randn(256, 1)

def train_with_accumulation(accum_steps=8, micro_batch=16, epochs=5):
    model = nn.Linear(20, 1)
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()
    dataset = torch.utils.data.TensorDataset(X_data, y_data)
    loader = torch.utils.data.DataLoader(dataset, batch_size=micro_batch, shuffle=True)
    all_losses = []
    for epoch in range(epochs):
        optimizer.zero_grad()
        accum_count = 0
        for i, (xb, yb) in enumerate(loader):
            # Divide by accum_steps so accumulated grad = mean over effective batch
            loss = criterion(model(xb), yb) / accum_steps
            loss.backward()
            accum_count += 1
            if accum_count == accum_steps:
                optimizer.step()
                optimizer.zero_grad()
                accum_count = 0
                all_losses.append(loss.item() * accum_steps)
    return all_losses

# Effective batch size = 16 * 8 = 128
losses = train_with_accumulation(accum_steps=8, micro_batch=16)
print(f'Steps: {len(losses)}, Final loss: {losses[-1]:.4f}')
print('Gradient accumulation: effective batch=128 using micro_batch=16')
```

## SGD Noise and Generalization

SGD noise does not just slow convergence — it can actively improve generalization. The noise acts as an implicit regularizer, biasing the optimizer toward flat minima (low curvature regions of the loss landscape). Flat minima generalize better because small perturbations to weights cause small changes in loss. Large-batch GD converges to sharp minima that generalize worse, a phenomenon confirmed empirically by Keskar et al. (2016). This is why small-batch SGD often outperforms large-batch GD on test accuracy.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

torch.manual_seed(7)
X_tr = torch.randn(50, 8)
y_tr = (X_tr[:, 0] > 0).float().unsqueeze(1)
X_te = torch.randn(200, 8)
y_te = (X_te[:, 0] > 0).float().unsqueeze(1)

def train_eval(batch_size, lr=0.1, epochs=100):
    model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 1), nn.Sigmoid())
    opt = optim.SGD(model.parameters(), lr=lr)
    crit = nn.BCELoss()
    tr_losses, te_losses = [], []
    ds = torch.utils.data.TensorDataset(X_tr, y_tr)
    loader = torch.utils.data.DataLoader(ds, batch_size=batch_size, shuffle=True)
    for _ in range(epochs):
        for xb, yb in loader:
            opt.zero_grad(); crit(model(xb), yb).backward(); opt.step()
        with torch.no_grad():
            tr_losses.append(crit(model(X_tr), y_tr).item())
            te_losses.append(crit(model(X_te), y_te).item())
    return tr_losses, te_losses

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for bs, lbl in [(1, 'SGD B=1 (noisy)'), (50, 'Full-batch GD')]:
    tr, te = train_eval(bs)
    axes[0].plot(tr, label=lbl); axes[1].plot(te, label=lbl)
for ax, t in zip(axes, ['Train Loss', 'Test Loss (Generalization)']):
    ax.set_xlabel('Epoch'); ax.legend(); ax.set_title(t)
plt.tight_layout()
plt.savefig('sgd_generalization.png', dpi=150)
plt.show()
```

- Minibatch gradient is unbiased: E[g_B] = ∇L(θ)
- Variance scales as σ²/B — doubling batch halves noise
- Robbins-Monro: need Ση_t=∞ and Ση_t²<∞ for convergence
- Linear scaling rule: lr ∝ B, scale up proportionally
- SGD noise biases toward flat minima — better generalization than large-batch GD

> **Best Practice**: Use batch size 256–1024 for vision tasks and 32–128 for NLP. Scale learning rate linearly with batch size from a base lr at B=32 or B=64. Use 5–10% of total training steps as linear LR warmup when using large batches. Gradient accumulation is a practical workaround when GPU memory is the bottleneck.

---

