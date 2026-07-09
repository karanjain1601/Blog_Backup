---
title: "Lagrangian Optimization and KKT Conditions"
slug: "lagrangian-kkt-conditions"
description: "Equality and inequality constrained optimization via Lagrange multipliers, KKT conditions, strong duality, the SVM dual, and penalty methods in PyTorch."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uc3RyYWluZWQgb3B0aW1pemF0aW9uIGlzIGNlbnRyYWwgdG8gTUw6IFNWTXMgbWF4aW1pemUgdGhlIG1hcmdpbiBzdWJqZWN0IHRvIGEgY2xhc3NpZmljYXRpb24gY29uc3RyYWludCwgUkwgcG9saWN5IG9wdGltaXphdGlvbiBlbmZvcmNlcyBhIEtMIGRpdmVyZ2VuY2UgYnVkZ2V0LCBhbmQgbmV0d29yayBjb21wcmVzc2lvbiBlbmZvcmNlcyBzcGFyc2l0eSBvciBzaXplIGNvbnN0cmFpbnRzLiBUaGUgTGFncmFuZ2lhbiBtZXRob2QgY29udmVydHMgY29uc3RyYWluZWQgcHJvYmxlbXMgaW50byB1bmNvbnN0cmFpbmVkIG9uZXMgYnkgcGVuYWxpemluZyBjb25zdHJhaW50IHZpb2xhdGlvbnMgd2l0aCBtdWx0aXBsaWVycywgYW5kIEtLVCBjb25kaXRpb25zIHByb3ZpZGUgbmVjZXNzYXJ5IChhbmQgdW5kZXIgY29udmV4aXR5LCBzdWZmaWNpZW50KSBjb25kaXRpb25zIGZvciBvcHRpbWFsaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVxdWFsaXR5IENvbnN0cmFpbnRzIGFuZCBMYWdyYW5nZSBNdWx0aXBsaWVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG8gbWluaW1pemUgZih4KSBzdWJqZWN0IHRvIGcoeCkgPSAwLCBmb3JtIHRoZSBMYWdyYW5naWFuOiBMKHgsIM67KSA9IGYoeCkgKyDOu+G1gGcoeCkuIEF0IG9wdGltYWxpdHksIHRoZSBncmFkaWVudCBvZiB0aGUgTGFncmFuZ2lhbiB3LnIudC4geCBpcyB6ZXJvOiDiiIfigpNMID0g4oiHZih4KikgKyDOu+G1gOKIh2coeCopID0gMC4gVGhpcyBtZWFucyDiiIdmIGlzIGluIHRoZSBzcGFuIG9mIHviiIdn4bWifSDigJQgdGhlIGdyYWRpZW50IG9mIHRoZSBvYmplY3RpdmUgaXMgYSBsaW5lYXIgY29tYmluYXRpb24gb2YgY29uc3RyYWludCBncmFkaWVudHMuIEdlb21ldHJpY2FsbHk6IHRoZSBsZXZlbCBjdXJ2ZXMgb2YgZiBhbmQgZyBhcmUgdGFuZ2VudCBhdCB4Kiwgc28gbm8gZmVhc2libGUgbW92ZW1lbnQgY2FuIGRlY3JlYXNlIGYuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJMYWdyYW5nZSBNdWx0aXBsaWVyIEludGVycHJldGF0aW9uIiwiY29udGVudCI6IlRoZSBtdWx0aXBsaWVyIM674bWiIGVxdWFscyDiiIJmKi/iiIJi4bWiIHdoZXJlIGLhtaIgaXMgdGhlIFJIUyBvZiBjb25zdHJhaW50IGfhtaIoeCk9YuG1oi4gSWYgzrvhtaIgaXMgbGFyZ2UsIHRpZ2h0ZW5pbmcgY29uc3RyYWludCBpIHNpZ25pZmljYW50bHkgaW1wcm92ZXMgdGhlIG9iamVjdGl2ZSDigJQgdGhlIGNvbnN0cmFpbnQgaXMgYmluZGluZyBhbmQgdmFsdWFibGUuIElmIM674bWiPTAsIHRoZSBjb25zdHJhaW50IGlzIGluYWN0aXZlIChzYXRpc2ZpZWQgd2l0aCBzbGFjaykgYW5kIHJlbW92aW5nIGl0IGRvZXNuXHUwMDI3dCBjaGFuZ2UgdGhlIHNvbHV0aW9uLiBUaGlzIHNoYWRvdyBwcmljZSBpbnRlcnByZXRhdGlvbiBpcyB1c2VkIGluIGVjb25vbWljcyAoc2hhZG93IHByaWNlcyBvZiByZXNvdXJjZXMpIGFuZCBpbiBSTCAoS0wgYnVkZ2V0IGNvc3QpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5cbiMgTWluaW1pemUgZih4LHkpID0gKHgtMileMiArICh5LTMpXjIgc3ViamVjdCB0byB4ICsgeSA9IDRcbiMgTGFncmFuZ2lhbjogTCA9ICh4LTIpXjIgKyAoeS0zKV4yICsgbGFtYmRhKih4K3ktNClcbiMgU3RhdGlvbmFyaXR5OiBkTC9keCA9IDIoeC0yKSArIGxhbWJkYSA9IDAgPVx1MDAzZSB4ID0gMiAtIGxhbWJkYS8yXG4jICAgICAgICAgICAgICAgZEwvZHkgPSAyKHktMykgKyBsYW1iZGEgPSAwID1cdTAwM2UgeSA9IDMgLSBsYW1iZGEvMlxuIyBDb25zdHJhaW50OiAgICgyIC0gbGFtYmRhLzIpICsgKDMgLSBsYW1iZGEvMikgPSA0ID1cdTAwM2UgbGFtYmRhID0gMVxuXG5sYW1iZGFfc3RhciA9IDEuMFxueF9zdGFyID0gMi4wIC0gbGFtYmRhX3N0YXIgLyAyLjAgICMgPSAxLjVcbnlfc3RhciA9IDMuMCAtIGxhbWJkYV9zdGFyIC8gMi4wICAjID0gMi41XG5cbmRlZiBmKHYpOiByZXR1cm4gKHZbMF0tMikqKjIgKyAodlsxXS0zKSoqMlxuZGVmIGdyYWRfZih2KTogcmV0dXJuIG5wLmFycmF5KFsyKih2WzBdLTIpLCAyKih2WzFdLTMpXSlcbmRlZiBnKHYpOiByZXR1cm4gdlswXSArIHZbMV0gLSA0XG5cbnByaW50KFwiQW5hbHl0aWNhbCBMYWdyYW5naWFuIHNvbHV0aW9uOlwiKVxucHJpbnQoZlwiICB4KiA9IHt4X3N0YXJ9LCB5KiA9IHt5X3N0YXJ9XCIpXG5wcmludChmXCIgIGYqID0ge2YoW3hfc3RhciwgeV9zdGFyXSk6LjRmfVwiKVxucHJpbnQoZlwiICBsYW1iZGEqID0ge2xhbWJkYV9zdGFyfSAoc2hhZG93IHByaWNlIG9mIGNvbnN0cmFpbnQpXCIpXG5cbiMgVmVyaWZ5IHdpdGggc2NpcHlcbnJlc3VsdCA9IG1pbmltaXplKGYsIFswLCAwXSxcbiAgICBjb25zdHJhaW50cz17XHUwMDI3dHlwZVx1MDAyNzogXHUwMDI3ZXFcdTAwMjcsIFx1MDAyN2Z1blx1MDAyNzogZ30sXG4gICAgbWV0aG9kPVx1MDAyN1NMU1FQXHUwMDI3KVxucHJpbnQoZlwiXFxuU2NpcHkgU0xTUVA6IHg9e3Jlc3VsdC54WzBdOi40Zn0sIHk9e3Jlc3VsdC54WzFdOi40Zn0sIGY9e3Jlc3VsdC5mdW46LjRmfVwiKVxucHJpbnQoZlwiQ29uc3RyYWludCBzYXRpc2ZpZWQ6IHgreSA9IHtyZXN1bHQueC5zdW0oKTouNmZ9XCIpXG5cbiMgU2Vuc2l0aXZpdHk6IHRpZ2h0ZW4gY29uc3RyYWludCBmcm9tIDQuMCB0byA0LjAxXG5mX3RpZ2h0ID0gbWluaW1pemUoZiwgWzAsMF0sXG4gICAgY29uc3RyYWludHM9e1x1MDAyN3R5cGVcdTAwMjc6XHUwMDI3ZXFcdTAwMjcsXHUwMDI3ZnVuXHUwMDI3OiBsYW1iZGEgdjogdlswXSt2WzFdLTQuMDF9LFxuICAgIG1ldGhvZD1cdTAwMjdTTFNRUFx1MDAyNykuZnVuXG5kZl9kcmhzID0gKGZfdGlnaHQgLSByZXN1bHQuZnVuKSAvIDAuMDFcbnByaW50KGZcIlxcblNlbnNpdGl2aXR5OiBkZiovZChSSFMpID0ge2RmX2RyaHM6LjRmfSDiiYggbGFtYmRhKiA9IHtsYW1iZGFfc3Rhcn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbmVxdWFsaXR5IENvbnN0cmFpbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgaW5lcXVhbGl0eSBjb25zdHJhaW50cyBoKHgpIOKJpCAwLCB0aGUgTGFncmFuZ2lhbiBiZWNvbWVzIEwoeCwgzrwpID0gZih4KSArIM684bWAaCh4KSB3aGVyZSDOvCDiiaUgMC4gVGhlIG5vbi1uZWdhdGl2aXR5IG9mIM68IHJlZmxlY3RzIHRoYXQgdGlnaHRlbmluZyBhbiBpbmVxdWFsaXR5IGNvbnN0cmFpbnQgKG1ha2luZyBpdCBoYXJkZXIgdG8gc2F0aXNmeSkgY2FuIG9ubHkgaW5jcmVhc2Ugb3IgbWFpbnRhaW4gdGhlIG9wdGltYWwgdmFsdWUsIG5ldmVyIGRlY3JlYXNlIGl0LiBBdCB0aGUgb3B0aW11bSwgZWl0aGVyIHRoZSBjb25zdHJhaW50IGlzIGFjdGl2ZSAoaCh4Kik9MCwgzrxcdTAwM2UwKSBvciBpbmFjdGl2ZSAoaCh4KilcdTAwM2MwLCDOvD0wKS4gVGhlc2UgdHdvIGNhc2VzIGFyZSB1bmlmaWVkIGJ5IGNvbXBsZW1lbnRhcnkgc2xhY2tuZXNzOiDOvOG1omjhtaIoeCopPTAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS0tUIENvbmRpdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciB0aGUgZ2VuZXJhbCBwcm9ibGVtOiBtaW5pbWl6ZSBmKHgpIHN1YmplY3QgdG8gZ+G1oih4KT0wIChpPTEuLm0pIGFuZCBo4rG8KHgp4omkMCAoaj0xLi5wKSwgdGhlIEthcnVzaC1LdWhuLVR1Y2tlciAoS0tUKSBjb25kaXRpb25zIGFyZSBuZWNlc3NhcnkgZm9yIGFueSBsb2NhbCBvcHRpbXVtICh1bmRlciBjb25zdHJhaW50IHF1YWxpZmljYXRpb24pIGFuZCBzdWZmaWNpZW50IGZvciBnbG9iYWwgb3B0aW11bSB1bmRlciBjb252ZXhpdHkuIFRoZXNlIGZvdXIgY29uZGl0aW9ucyBtdXN0IGhvbGQgc2ltdWx0YW5lb3VzbHkgYXQgeCouIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOnRydWUsIml0ZW1zIjpbIlN0YXRpb25hcml0eTog4oiHZih4KikgKyDOo+G1os674bWi4oiHZ+G1oih4KikgKyDOo+KxvM684rG84oiHaOKxvCh4KikgPSAwIiwiUHJpbWFsIGZlYXNpYmlsaXR5OiBn4bWiKHgqKT0wIGZvciBhbGwgaTsgaOKxvCh4KiniiaQwIGZvciBhbGwgaiIsIkR1YWwgZmVhc2liaWxpdHk6IM684rG8IOKJpSAwIGZvciBhbGwgaiAoaW5lcXVhbGl0eSBtdWx0aXBsaWVycyBub24tbmVnYXRpdmUpIiwiQ29tcGxlbWVudGFyeSBzbGFja25lc3M6IM684rG8aOKxvCh4Kik9MCBmb3IgYWxsIGogKGVpdGhlciBjb25zdHJhaW50IGFjdGl2ZSBvciBtdWx0aXBsaWVyIHplcm8pIl19LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDb25kaXRpb24iLCJFcXVhbGl0eSBDb25zdHJhaW50cyIsIkluZXF1YWxpdHkgQ29uc3RyYWludHMiLCJHZW9tZXRyaWMgTWVhbmluZyJdLCJyb3dzIjpbWyJTdGF0aW9uYXJpdHkiLCLiiIdmICsgzrvhtYDiiIdnID0gMCIsIuKIh2YgKyDOu+G1gOKIh2cgKyDOvOG1gOKIh2ggPSAwIiwiTm8gZmVhc2libGUgZGVzY2VudCBkaXJlY3Rpb24iXSxbIlByaW1hbCBGZWFzaWJpbGl0eSIsImcoeCopID0gMCIsImcoeCopPTAgYW5kIGgoeCop4omkMCIsIlNvbHV0aW9uIGlzIGluIGZlYXNpYmxlIHNldCJdLFsiRHVhbCBGZWFzaWJpbGl0eSIsIs67IHVucmVzdHJpY3RlZCIsIs68IOKJpSAwIiwiQ29uc3RyYWludCB0aWdodGVuaW5nIGNhbiBvbmx5IHdvcnNlbiBvYmplY3RpdmUiXSxbIkNvbXBsZW1lbnRhcnkgU2xhY2tuZXNzIiwiTi9BIiwizrzisbxo4rG8KHgqKT0wIOKIgGoiLCJFaXRoZXIgY29uc3RyYWludCBiaW5kcyBvciBpdHMgbXVsdGlwbGllciBpcyB6ZXJvIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdHJvbmcgRHVhbGl0eSBhbmQgU2xhdGVyXHUwMDI3cyBDb25kaXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBkdWFsIHByb2JsZW0gbWF4aW1pemVzIHRoZSBkdWFsIGZ1bmN0aW9uIGcozrsszrwpID0gaW5mX3ggTCh4LM67LM68KSBvdmVyICjOuyzOvOKJpTApLiBXZWFrIGR1YWxpdHkgYWx3YXlzIGhvbGRzOiBnKM67LM68KSDiiaQgZiouIFN0cm9uZyBkdWFsaXR5IChnKM67KizOvCopPWYqKSBob2xkcyB3aGVuIFNsYXRlclx1MDAyN3MgY29uZGl0aW9uIGlzIHNhdGlzZmllZDogdGhlcmUgZXhpc3RzIGEgc3RyaWN0bHkgZmVhc2libGUgcG9pbnQgeMyDIHdpdGggaOKxvCh4zIMpXHUwMDNjMCBmb3IgYWxsIGouIEZvciBjb252ZXggcHJvYmxlbXMgd2l0aCBTbGF0ZXJcdTAwMjdzIGNvbmRpdGlvbiwgdGhlIGR1YWxpdHkgZ2FwIGlzIHplcm8gYW5kIEtLVCBjb25kaXRpb25zIGFyZSBib3RoIG5lY2Vzc2FyeSBhbmQgc3VmZmljaWVudCBmb3IgZ2xvYmFsIG9wdGltYWxpdHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU1ZNIER1YWwgRm9ybXVsYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBTVk0gcHJpbWFsIG1pbmltaXplcyAoMS8yKeKAlnfigJbCsiBzdWJqZWN0IHRvIHnhtaIod+G1gHjhtaIrYiniiaUxLiBUaGUgTGFncmFuZ2lhbiBpbnRyb2R1Y2VzIM6x4bWi4omlMCBmb3IgZWFjaCBtYXJnaW4gY29uc3RyYWludC4gVGFraW5nIHN0YXRpb25hcml0eSB3LnIudC4gdyBhbmQgYiBnaXZlcyB3Pc6jzrHhtaJ54bWieOG1oiBhbmQgzqPOseG1onnhtaI9MC4gU3Vic3RpdHV0aW5nIGJhY2sgZWxpbWluYXRlcyB3IGFuZCBiLCB5aWVsZGluZyB0aGUgZHVhbDogbWF4aW1pemUgzqPOseG1oiAtICgxLzIpzqPhtaLisbzOseG1os6x4rG8eeG1onnisbx44bWi4bWAeOKxvCBzdWJqZWN0IHRvIDDiiaTOseG1ouKJpEMgYW5kIM6jzrHhtaJ54bWiPTAuIE9ubHkgc3VwcG9ydCB2ZWN0b3JzICjOseG1olx1MDAzZTApIGNvbnRyaWJ1dGUgdG8gdywgYW5kIGNvbXBsZW1lbnRhcnkgc2xhY2tuZXNzIHBpbnMgdGhlIGJpYXMgYi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5Lm9wdGltaXplIGltcG9ydCBtaW5pbWl6ZVxuXG5kZWYgc29sdmVfc3ZtX2R1YWwoWCwgeSwgQz0xLjApOlxuICAgIFwiXCJcIlNvbHZlIHRoZSBTVk0gZHVhbCBRUCB2aWEgc2NpcHkgU0xTUVAuXCJcIlwiXG4gICAgbiA9IGxlbih5KVxuICAgIEsgPSBYIEAgWC5UICAjIGxpbmVhciBrZXJuZWwgbWF0cml4XG4gICAgeXlfSyA9IG5wLm91dGVyKHksIHkpICogS1xuXG4gICAgZGVmIG5lZ19kdWFsKGFscGhhKTogICMgbmVnYXRlIGZvciBtaW5pbWl6YXRpb25cbiAgICAgICAgcmV0dXJuIDAuNSAqIGFscGhhIEAgeXlfSyBAIGFscGhhIC0gYWxwaGEuc3VtKClcblxuICAgIGRlZiBuZWdfZHVhbF9ncmFkKGFscGhhKTpcbiAgICAgICAgcmV0dXJuIHl5X0sgQCBhbHBoYSAtIG5wLm9uZXMobilcblxuICAgIGNvbnN0cmFpbnRzID0gW1xuICAgICAgICB7XHUwMDI3dHlwZVx1MDAyNzogXHUwMDI3ZXFcdTAwMjcsIFx1MDAyN2Z1blx1MDAyNzogbGFtYmRhIGE6IGEgQCB5LCBcdTAwMjdqYWNcdTAwMjc6IGxhbWJkYSBhOiB5fVxuICAgIF1cbiAgICBib3VuZHMgPSBbKDAuMCwgQyldICogblxuICAgIHJlc3VsdCA9IG1pbmltaXplKG5lZ19kdWFsLCBucC56ZXJvcyhuKSwgamFjPW5lZ19kdWFsX2dyYWQsXG4gICAgICAgICAgICAgICAgICAgICAgYm91bmRzPWJvdW5kcywgY29uc3RyYWludHM9Y29uc3RyYWludHMsIG1ldGhvZD1cdTAwMjdTTFNRUFx1MDAyNyxcbiAgICAgICAgICAgICAgICAgICAgICBvcHRpb25zPXtcdTAwMjdmdG9sXHUwMDI3OiAxZS05LCBcdTAwMjdtYXhpdGVyXHUwMDI3OiA1MDB9KVxuXG4gICAgYWxwaGEgPSByZXN1bHQueFxuICAgIHN2ID0gYWxwaGEgXHUwMDNlIDFlLTUgICAgICAgICAgICMgc3VwcG9ydCB2ZWN0b3IgbWFza1xuICAgIHcgPSAoYWxwaGEgKiB5KSBAIFggICAgICAgICMgcHJpbWFsIHdlaWdodHNcbiAgICBiID0gbnAubWVhbih5W3N2XSAtIFhbc3ZdIEAgdylcbiAgICByZXR1cm4gYWxwaGEsIHcsIGIsIHN2XG5cbm5wLnJhbmRvbS5zZWVkKDApXG5YID0gbnAudnN0YWNrKFtucC5yYW5kb20ucmFuZG4oMzAsIDIpICsgWzIsIDJdLCBucC5yYW5kb20ucmFuZG4oMzAsIDIpIC0gWzIsIDJdXSlcbnkgPSBucC5hcnJheShbMS4wXSozMCArIFstMS4wXSozMClcblxuYWxwaGEsIHcsIGIsIHN2ID0gc29sdmVfc3ZtX2R1YWwoWCwgeSwgQz0xLjApXG5hY2MgPSBucC5tZWFuKG5wLnNpZ24oWCBAIHcgKyBiKSA9PSB5KVxucHJpbnQoZlwiU3VwcG9ydCB2ZWN0b3JzOiB7c3Yuc3VtKCl9IC8ge2xlbih5KX0gdG90YWwgcG9pbnRzXCIpXG5wcmludChmXCJBbHBoYSByYW5nZTogW3thbHBoYS5taW4oKTouNGZ9LCB7YWxwaGEubWF4KCk6LjRmfV1cIilcbnByaW50KGZcIncgPSB7d30sICBiID0ge2I6LjRmfVwiKVxucHJpbnQoZlwiVHJhaW5pbmcgYWNjdXJhY3k6IHthY2M6LjIlfVwiKVxucHJpbnQoZlwiQ29tcGxlbWVudGFyeSBzbGFja25lc3MgY2hlY2s6XCIpXG5wcmludChmXCIgIFBvaW50cyB3aXRoIGFscGhhfjAgQU5EIG1hcmdpbiB2aW9sYXRlZDogeygoYWxwaGFcdTAwM2MxZS01KSBcdTAwMjYgKHkqKFhAdytiKVx1MDAzYzEtMWUtNCkpLnN1bSgpfVwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQ29tcGxlbWVudGFyeSBTbGFja25lc3MgaW4gU1ZNcyIsImNvbnRlbnQiOiJDb21wbGVtZW50YXJ5IHNsYWNrbmVzcyBtZWFucyDOseG1osK3KHnhtaIod+G1gHjhtaIrYiniiJIxKT0wLiBTbyBlaXRoZXIgzrHhtaI9MCAocG9pbnQgaXMgbm90IGEgc3VwcG9ydCB2ZWN0b3IsIGxpZXMgb3V0c2lkZSB0aGUgbWFyZ2luKSBvciB54bWiKHfhtYB44bWiK2IpPTEgKHBvaW50IGlzIG9uIHRoZSBtYXJnaW4gYm91bmRhcnkpLiBOb24tc3VwcG9ydCB2ZWN0b3JzIGhhdmUgemVybyBpbmZsdWVuY2Ugb24gdy4gVmlvbGF0aW5nIGNvbXBsZW1lbnRhcnkgc2xhY2tuZXNzIGluIHlvdXIgc29sdmVyIG1lYW5zIHRoZSBLS1QgY29uZGl0aW9ucyBhcmUgbm90IHNhdGlzZmllZCDigJQgdGhlIG9wdGltaXphdGlvbiBoYXMgbm90IGNvbnZlcmdlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5Lm9wdGltaXplIGltcG9ydCBtaW5pbWl6ZVxuXG5kZWYgY2hlY2tfa2t0KHhfb3B0LCBncmFkX2YsIGVxX2ZucywgaW5lcV9mbnMsIHRvbD0xZS01KTpcbiAgICBcIlwiXCJWZXJpZnkgS0tUIGNvbmRpdGlvbnMgYXQgYSBjYW5kaWRhdGUgc29sdXRpb24uXCJcIlwiXG4gICAgcHJpbnQoXCJLS1QgQ29uZGl0aW9uIFZlcmlmaWNhdGlvblwiKVxuICAgIHByaW50KFwiLVwiICogNDUpXG5cbiAgICAjIFByaW1hbCBmZWFzaWJpbGl0eVxuICAgIHByaW50KFwiXFxuWzFdIFByaW1hbCBGZWFzaWJpbGl0eTpcIilcbiAgICBmb3IgbmFtZSwgZm4gaW4gZXFfZm5zOlxuICAgICAgICB2YWwgPSBmbih4X29wdClcbiAgICAgICAgb2sgPSBhYnModmFsKSBcdTAwM2MgdG9sXG4gICAgICAgIHByaW50KGZcIiAgICB7bmFtZX0gPSB7dmFsOi4yZX0gIHtcdTAwMjdPS1x1MDAyNyBpZiBvayBlbHNlIFx1MDAyN1ZJT0xBVEVEXHUwMDI3fVwiKVxuICAgIGZvciBuYW1lLCBmbiBpbiBpbmVxX2ZuczpcbiAgICAgICAgdmFsID0gZm4oeF9vcHQpXG4gICAgICAgIG9rID0gdmFsIFx1MDAzYz0gdG9sXG4gICAgICAgIHByaW50KGZcIiAgICB7bmFtZX0gPSB7dmFsOi4yZX0gIHtcdTAwMjdPS1x1MDAyNyBpZiBvayBlbHNlIFx1MDAyN1ZJT0xBVEVEXHUwMDI3fVwiKVxuXG4gICAgZ2YgPSBncmFkX2YoeF9vcHQpXG4gICAgcHJpbnQoZlwiXFxuWzJdIFN0YXRpb25hcml0eSAoZ3JhZF9mIGF0IHgqKToge2dmfVwiKVxuICAgIHByaW50KFwiICAgIChGdWxsIGNoZWNrIHJlcXVpcmVzIGNvbXB1dGluZyBMYWdyYW5nZSBtdWx0aXBsaWVycylcIilcbiAgICByZXR1cm4gZ2ZcblxuIyBFeGFtcGxlOiBtaW4geF4yKzJ5XjIrM3peMiAgcy50LiAgeCt5K3o9NiwgIHhcdTAwM2U9MVxuZGVmIGYodik6IHJldHVybiB2WzBdKioyICsgMip2WzFdKioyICsgMyp2WzJdKioyXG5kZWYgZ2Yodik6IHJldHVybiBucC5hcnJheShbMip2WzBdLCA0KnZbMV0sIDYqdlsyXV0pXG5cbmNvbnN0cnMgPSBbXG4gICAge1x1MDAyN3R5cGVcdTAwMjc6IFx1MDAyN2VxXHUwMDI3LCAgIFx1MDAyN2Z1blx1MDAyNzogbGFtYmRhIHY6IHZbMF0rdlsxXSt2WzJdLTZ9LFxuICAgIHtcdTAwMjd0eXBlXHUwMDI3OiBcdTAwMjdpbmVxXHUwMDI3LCBcdTAwMjdmdW5cdTAwMjc6IGxhbWJkYSB2OiB2WzBdLTF9LCAgIyB4IFx1MDAzZT0gMVxuXVxucmVzID0gbWluaW1pemUoZiwgWzIsMiwyXSwgamFjPWdmLCBjb25zdHJhaW50cz1jb25zdHJzLCBtZXRob2Q9XHUwMDI3U0xTUVBcdTAwMjcpXG54X29wdCA9IHJlcy54XG5cbmNoZWNrX2trdCh4X29wdCwgZ2YsXG4gICAgZXFfZm5zPVsoXCJ4K3krei02XCIsIGxhbWJkYSB2OiB2WzBdK3ZbMV0rdlsyXS02KV0sXG4gICAgaW5lcV9mbnM9WyhcIngtMSAoXHUwMDNlPTApXCIsIGxhbWJkYSB2OiB2WzBdLTEpXSlcbnByaW50KGZcIlxcbk9wdGltYWw6IHg9e3hfb3B0WzBdOi40Zn0sIHk9e3hfb3B0WzFdOi40Zn0sIHo9e3hfb3B0WzJdOi40Zn1cIilcbnByaW50KGZcImYoeCopID0ge2YoeF9vcHQpOi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25zdHJhaW5lZCBPcHRpbWl6YXRpb24gaW4gUHlUb3JjaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHlUb3JjaCBkb2VzIG5vdCBuYXRpdmVseSBzdXBwb3J0IGNvbnN0cmFpbmVkIG9wdGltaXphdGlvbiwgYnV0IHRoZSBwZW5hbHR5IC8gYXVnbWVudGVkIExhZ3JhbmdpYW4gbWV0aG9kIGNvbnZlcnRzIGNvbnN0cmFpbnRzIGludG8gc29mdCBwZW5hbHRpZXMgYWRkZWQgdG8gdGhlIGxvc3MuIFRoZSBwZW5hbHR5IGNvZWZmaWNpZW50IM+BIGlzIGluY3JlYXNlZCBhY3Jvc3Mgb3V0ZXIgaXRlcmF0aW9ucywgZHJpdmluZyB0aGUgc29sdXRpb24gdG93YXJkIGZlYXNpYmlsaXR5LiBUaGUgYXVnbWVudGVkIExhZ3JhbmdpYW4gYWRkcyBleHBsaWNpdCBtdWx0aXBsaWVyIGVzdGltYXRlcyBmb3IgYmV0dGVyIGNvbnZlcmdlbmNlOiBMX2F1ZyA9IGYoeCkgKyDOu+G1gGcoeCkgKyAoz4EvMinigJZnKHgp4oCWwrIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgcGVuYWx0eV9vcHRpbWl6ZShmX2ZuLCBnX2VxLCBoX2luZXEsIHhfaW5pdCwgbHI9MC4wMixcbiAgICAgICAgICAgICAgICAgICAgIHJob19pbml0PTEuMCwgbl9vdXRlcj04LCBuX2lubmVyPTE1MCk6XG4gICAgXCJcIlwiXG4gICAgUXVhZHJhdGljIHBlbmFsdHkgbWV0aG9kOlxuICAgICAgICBtaW4gZih4KSArIChyaG8vMikqfHxnKHgpfHxeMiArIChyaG8vMikqfHxtYXgoMCxoKHgpKXx8XjJcbiAgICBJbmNyZWFzZSByaG8gZWFjaCBvdXRlciBpdGVyYXRpb24gdG8gZW5mb3JjZSBmZWFzaWJpbGl0eS5cbiAgICBcIlwiXCJcbiAgICB4ID0geF9pbml0LmNsb25lKCkuZGV0YWNoKCkucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICByaG8gPSByaG9faW5pdFxuICAgIGxvZyA9IFtdXG5cbiAgICBmb3Igb3V0ZXIgaW4gcmFuZ2Uobl9vdXRlcik6XG4gICAgICAgIG9wdCA9IHRvcmNoLm9wdGltLkFkYW0oW3hdLCBscj1scilcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9pbm5lcik6XG4gICAgICAgICAgICBvcHQuemVyb19ncmFkKClcbiAgICAgICAgICAgIGxvc3MgPSAoZl9mbih4KVxuICAgICAgICAgICAgICAgICAgICArIChyaG8vMikgKiBnX2VxKHgpKioyXG4gICAgICAgICAgICAgICAgICAgICsgKHJoby8yKSAqIHRvcmNoLmNsYW1wKGhfaW5lcSh4KSwgbWluPTAuMCkqKjIpXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdC5zdGVwKClcbiAgICAgICAgcmhvICo9IDQuMFxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIGxvZy5hcHBlbmQoe1x1MDAyN3Job1x1MDAyNzogcmhvLFxuICAgICAgICAgICAgICAgICAgICAgICAgXHUwMDI3Zlx1MDAyNzogZl9mbih4KS5pdGVtKCksXG4gICAgICAgICAgICAgICAgICAgICAgICBcdTAwMjdnXHUwMDI3OiBnX2VxKHgpLml0ZW0oKSxcbiAgICAgICAgICAgICAgICAgICAgICAgIFx1MDAyN2hcdTAwMjc6IGhfaW5lcSh4KS5pdGVtKCl9KVxuICAgICAgICBwcmludChmXCJPdXRlciB7b3V0ZXIrMX06IHJobz17cmhvOi4xZn0gIGY9e2xvZ1stMV1bXHUwMDI3Zlx1MDAyN106LjRmfSAgXCJcbiAgICAgICAgICAgICAgZlwiZz17bG9nWy0xXVtcdTAwMjdnXHUwMDI3XTouNGZ9ICBoPXtsb2dbLTFdW1x1MDAyN2hcdTAwMjddOi40Zn1cIilcbiAgICByZXR1cm4geC5kZXRhY2goKSwgbG9nXG5cbiMgbWluICh4MC0zKV4yICsgKHgxLTIpXjIgIHMudC4gIHgwK3gxPTQsICB4MFx1MDAzZT0xXG5mX2ZuICA9IGxhbWJkYSB4OiAoeFswXS0zKSoqMiArICh4WzFdLTIpKioyXG5nX2VxICA9IGxhbWJkYSB4OiB4WzBdICsgeFsxXSAtIDQuMFxuaF9pbmVxID0gbGFtYmRhIHg6IDEuMCAtIHhbMF0gICMgaFx1MDAzYz0wIG1lYW5zIHgwXHUwMDNlPTFcblxueF9vcHQsIGhpc3RvcnkgPSBwZW5hbHR5X29wdGltaXplKGZfZm4sIGdfZXEsIGhfaW5lcSwgdG9yY2gudGVuc29yKFsyLjAsIDIuMF0pKVxucHJpbnQoZlwiXFxuT3B0aW1hbDoge3hfb3B0Lm51bXB5KCl9LCBmPXtmX2ZuKHhfb3B0KS5pdGVtKCk6LjRmfVwiKVxucHJpbnQoZlwiRmVhc2liaWxpdHk6IGc9e2dfZXEoeF9vcHQpLml0ZW0oKTouNGZ9ICh0YXJnZXQgMCksIGg9e2hfaW5lcSh4X29wdCkuaXRlbSgpOi40Zn0gKHRhcmdldCBcdTAwM2M9MClcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcHBsaWNhdGlvbnMgaW4gTWFjaGluZSBMZWFybmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS0tUIGNvbmRpdGlvbnMgYW5kIExhZ3JhbmdpYW4gZHVhbGl0eSBhcHBlYXIgdGhyb3VnaG91dCBNTCBiZXlvbmQgU1ZNcy4gQ29uc3RyYWluZWQgcG9saWN5IG9wdGltaXphdGlvbiAoQ1BPKSBpbiBSTCBlbmZvcmNlcyBzYWZldHkgY29uc3RyYWludHMgYXMgS0tUIGluZXF1YWxpdHkgY29uZGl0aW9ucy4gVmFyaWF0aW9uYWwgYXV0b2VuY29kZXJzIHVzZSBhIExhZ3JhbmdpYW4gdG8gYmFsYW5jZSByZWNvbnN0cnVjdGlvbiBsb3NzIGFuZCBLTCBkaXZlcmdlbmNlICjOsi1WQUUgc2V0cyB0aGUgS0wgbXVsdGlwbGllciDOsikuIE5ldHdvcmsgY29tcHJlc3Npb24gd2l0aCBzcGFyc2l0eSBidWRnZXRzIGlzIGEgY29uc3RyYWluZWQgb3B0aW1pemF0aW9uIHByb2JsZW0gYW1lbmFibGUgdG8gTGFncmFuZ2lhbiByZWxheGF0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU1ZNOiBkdWFsIFFQIGdpdmVzIHNwYXJzZSBzb2x1dGlvbiB2aWEgY29tcGxlbWVudGFyeSBzbGFja25lc3Mg4oCUIG9ubHkgc3VwcG9ydCB2ZWN0b3JzIG1hdHRlciIsIkNQTyAoQ29uc3RyYWluZWQgUG9saWN5IE9wdGltaXphdGlvbik6IEtMIGNvbnN0cmFpbnQgYXMgTGFncmFuZ2lhbiBpbiBSTCIsIs6yLVZBRTogzrIgaXMgdGhlIExhZ3JhbmdlIG11bHRpcGxpZXIgb24gdGhlIEtMIOKJpCDOtSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrIGNvbnN0cmFpbnQiLCJXYXRlci1maWxsaW5nIChwb3dlciBhbGxvY2F0aW9uKTogS0tUIGdpdmVzIGNsb3NlZC1mb3JtIHNvbHV0aW9uIGZvciBjaGFubmVsIGNhcGFjaXR5IiwiTGFzc28gLyBBRE1NOiBhdWdtZW50ZWQgTGFncmFuZ2lhbiBzcGxpdHRpbmcgZm9yIEwxLWNvbnN0cmFpbmVkIHJlZ3Jlc3Npb24iLCJGYWlyIE1MOiBkZW1vZ3JhcGhpYyBwYXJpdHkgYXMgZXF1YWxpdHkgY29uc3RyYWludCBvbiBtb2RlbCBvdXRwdXRzIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Lagrangian Optimization and KKT Conditions

Constrained optimization is central to ML: SVMs maximize the margin subject to a classification constraint, RL policy optimization enforces a KL divergence budget, and network compression enforces sparsity or size constraints. The Lagrangian method converts constrained problems into unconstrained ones by penalizing constraint violations with multipliers, and KKT conditions provide necessary (and under convexity, sufficient) conditions for optimality.

## Equality Constraints and Lagrange Multipliers

To minimize f(x) subject to g(x) = 0, form the Lagrangian: L(x, λ) = f(x) + λᵀg(x). At optimality, the gradient of the Lagrangian w.r.t. x is zero: ∇ₓL = ∇f(x*) + λᵀ∇g(x*) = 0. This means ∇f is in the span of {∇gᵢ} — the gradient of the objective is a linear combination of constraint gradients. Geometrically: the level curves of f and g are tangent at x*, so no feasible movement can decrease f.

> **Lagrange Multiplier Interpretation**: The multiplier λᵢ equals ∂f*/∂bᵢ where bᵢ is the RHS of constraint gᵢ(x)=bᵢ. If λᵢ is large, tightening constraint i significantly improves the objective — the constraint is binding and valuable. If λᵢ=0, the constraint is inactive (satisfied with slack) and removing it doesn't change the solution. This shadow price interpretation is used in economics (shadow prices of resources) and in RL (KL budget cost).

```python
import numpy as np
from scipy.optimize import minimize

# Minimize f(x,y) = (x-2)^2 + (y-3)^2 subject to x + y = 4
# Lagrangian: L = (x-2)^2 + (y-3)^2 + lambda*(x+y-4)
# Stationarity: dL/dx = 2(x-2) + lambda = 0 => x = 2 - lambda/2
#               dL/dy = 2(y-3) + lambda = 0 => y = 3 - lambda/2
# Constraint:   (2 - lambda/2) + (3 - lambda/2) = 4 => lambda = 1

lambda_star = 1.0
x_star = 2.0 - lambda_star / 2.0  # = 1.5
y_star = 3.0 - lambda_star / 2.0  # = 2.5

def f(v): return (v[0]-2)**2 + (v[1]-3)**2
def grad_f(v): return np.array([2*(v[0]-2), 2*(v[1]-3)])
def g(v): return v[0] + v[1] - 4

print("Analytical Lagrangian solution:")
print(f"  x* = {x_star}, y* = {y_star}")
print(f"  f* = {f([x_star, y_star]):.4f}")
print(f"  lambda* = {lambda_star} (shadow price of constraint)")

# Verify with scipy
result = minimize(f, [0, 0],
    constraints={'type': 'eq', 'fun': g},
    method='SLSQP')
print(f"\nScipy SLSQP: x={result.x[0]:.4f}, y={result.x[1]:.4f}, f={result.fun:.4f}")
print(f"Constraint satisfied: x+y = {result.x.sum():.6f}")

# Sensitivity: tighten constraint from 4.0 to 4.01
f_tight = minimize(f, [0,0],
    constraints={'type':'eq','fun': lambda v: v[0]+v[1]-4.01},
    method='SLSQP').fun
df_drhs = (f_tight - result.fun) / 0.01
print(f"\nSensitivity: df*/d(RHS) = {df_drhs:.4f} ≈ lambda* = {lambda_star}")
```

## Inequality Constraints

For inequality constraints h(x) ≤ 0, the Lagrangian becomes L(x, μ) = f(x) + μᵀh(x) where μ ≥ 0. The non-negativity of μ reflects that tightening an inequality constraint (making it harder to satisfy) can only increase or maintain the optimal value, never decrease it. At the optimum, either the constraint is active (h(x*)=0, μ>0) or inactive (h(x*)<0, μ=0). These two cases are unified by complementary slackness: μᵢhᵢ(x*)=0.

## KKT Conditions

For the general problem: minimize f(x) subject to gᵢ(x)=0 (i=1..m) and hⱼ(x)≤0 (j=1..p), the Karush-Kuhn-Tucker (KKT) conditions are necessary for any local optimum (under constraint qualification) and sufficient for global optimum under convexity. These four conditions must hold simultaneously at x*.

1. Stationarity: ∇f(x*) + Σᵢλᵢ∇gᵢ(x*) + Σⱼμⱼ∇hⱼ(x*) = 0
2. Primal feasibility: gᵢ(x*)=0 for all i; hⱼ(x*)≤0 for all j
3. Dual feasibility: μⱼ ≥ 0 for all j (inequality multipliers non-negative)
4. Complementary slackness: μⱼhⱼ(x*)=0 for all j (either constraint active or multiplier zero)

| Condition | Equality Constraints | Inequality Constraints | Geometric Meaning |
| --- | --- | --- | --- |
| Stationarity | ∇f + λᵀ∇g = 0 | ∇f + λᵀ∇g + μᵀ∇h = 0 | No feasible descent direction |
| Primal Feasibility | g(x*) = 0 | g(x*)=0 and h(x*)≤0 | Solution is in feasible set |
| Dual Feasibility | λ unrestricted | μ ≥ 0 | Constraint tightening can only worsen objective |
| Complementary Slackness | N/A | μⱼhⱼ(x*)=0 ∀j | Either constraint binds or its multiplier is zero |

## Strong Duality and Slater's Condition

The dual problem maximizes the dual function g(λ,μ) = inf_x L(x,λ,μ) over (λ,μ≥0). Weak duality always holds: g(λ,μ) ≤ f*. Strong duality (g(λ*,μ*)=f*) holds when Slater's condition is satisfied: there exists a strictly feasible point x̃ with hⱼ(x̃)<0 for all j. For convex problems with Slater's condition, the duality gap is zero and KKT conditions are both necessary and sufficient for global optimality.

## SVM Dual Formulation

The SVM primal minimizes (1/2)‖w‖² subject to yᵢ(wᵀxᵢ+b)≥1. The Lagrangian introduces αᵢ≥0 for each margin constraint. Taking stationarity w.r.t. w and b gives w=Σαᵢyᵢxᵢ and Σαᵢyᵢ=0. Substituting back eliminates w and b, yielding the dual: maximize Σαᵢ - (1/2)Σᵢⱼαᵢαⱼyᵢyⱼxᵢᵀxⱼ subject to 0≤αᵢ≤C and Σαᵢyᵢ=0. Only support vectors (αᵢ>0) contribute to w, and complementary slackness pins the bias b.

```python
import numpy as np
from scipy.optimize import minimize

def solve_svm_dual(X, y, C=1.0):
    """Solve the SVM dual QP via scipy SLSQP."""
    n = len(y)
    K = X @ X.T  # linear kernel matrix
    yy_K = np.outer(y, y) * K

    def neg_dual(alpha):  # negate for minimization
        return 0.5 * alpha @ yy_K @ alpha - alpha.sum()

    def neg_dual_grad(alpha):
        return yy_K @ alpha - np.ones(n)

    constraints = [
        {'type': 'eq', 'fun': lambda a: a @ y, 'jac': lambda a: y}
    ]
    bounds = [(0.0, C)] * n
    result = minimize(neg_dual, np.zeros(n), jac=neg_dual_grad,
                      bounds=bounds, constraints=constraints, method='SLSQP',
                      options={'ftol': 1e-9, 'maxiter': 500})

    alpha = result.x
    sv = alpha > 1e-5           # support vector mask
    w = (alpha * y) @ X        # primal weights
    b = np.mean(y[sv] - X[sv] @ w)
    return alpha, w, b, sv

np.random.seed(0)
X = np.vstack([np.random.randn(30, 2) + [2, 2], np.random.randn(30, 2) - [2, 2]])
y = np.array([1.0]*30 + [-1.0]*30)

alpha, w, b, sv = solve_svm_dual(X, y, C=1.0)
acc = np.mean(np.sign(X @ w + b) == y)
print(f"Support vectors: {sv.sum()} / {len(y)} total points")
print(f"Alpha range: [{alpha.min():.4f}, {alpha.max():.4f}]")
print(f"w = {w},  b = {b:.4f}")
print(f"Training accuracy: {acc:.2%}")
print(f"Complementary slackness check:")
print(f"  Points with alpha~0 AND margin violated: {((alpha<1e-5) & (y*(X@w+b)<1-1e-4)).sum()}")
```

> **Complementary Slackness in SVMs**: Complementary slackness means αᵢ·(yᵢ(wᵀxᵢ+b)−1)=0. So either αᵢ=0 (point is not a support vector, lies outside the margin) or yᵢ(wᵀxᵢ+b)=1 (point is on the margin boundary). Non-support vectors have zero influence on w. Violating complementary slackness in your solver means the KKT conditions are not satisfied — the optimization has not converged.

```python
import numpy as np
from scipy.optimize import minimize

def check_kkt(x_opt, grad_f, eq_fns, ineq_fns, tol=1e-5):
    """Verify KKT conditions at a candidate solution."""
    print("KKT Condition Verification")
    print("-" * 45)

    # Primal feasibility
    print("\n[1] Primal Feasibility:")
    for name, fn in eq_fns:
        val = fn(x_opt)
        ok = abs(val) < tol
        print(f"    {name} = {val:.2e}  {'OK' if ok else 'VIOLATED'}")
    for name, fn in ineq_fns:
        val = fn(x_opt)
        ok = val <= tol
        print(f"    {name} = {val:.2e}  {'OK' if ok else 'VIOLATED'}")

    gf = grad_f(x_opt)
    print(f"\n[2] Stationarity (grad_f at x*): {gf}")
    print("    (Full check requires computing Lagrange multipliers)")
    return gf

# Example: min x^2+2y^2+3z^2  s.t.  x+y+z=6,  x>=1
def f(v): return v[0]**2 + 2*v[1]**2 + 3*v[2]**2
def gf(v): return np.array([2*v[0], 4*v[1], 6*v[2]])

constrs = [
    {'type': 'eq',   'fun': lambda v: v[0]+v[1]+v[2]-6},
    {'type': 'ineq', 'fun': lambda v: v[0]-1},  # x >= 1
]
res = minimize(f, [2,2,2], jac=gf, constraints=constrs, method='SLSQP')
x_opt = res.x

check_kkt(x_opt, gf,
    eq_fns=[("x+y+z-6", lambda v: v[0]+v[1]+v[2]-6)],
    ineq_fns=[("x-1 (>=0)", lambda v: v[0]-1)])
print(f"\nOptimal: x={x_opt[0]:.4f}, y={x_opt[1]:.4f}, z={x_opt[2]:.4f}")
print(f"f(x*) = {f(x_opt):.4f}")
```

## Constrained Optimization in PyTorch

PyTorch does not natively support constrained optimization, but the penalty / augmented Lagrangian method converts constraints into soft penalties added to the loss. The penalty coefficient ρ is increased across outer iterations, driving the solution toward feasibility. The augmented Lagrangian adds explicit multiplier estimates for better convergence: L_aug = f(x) + λᵀg(x) + (ρ/2)‖g(x)‖².

```python
import torch

def penalty_optimize(f_fn, g_eq, h_ineq, x_init, lr=0.02,
                     rho_init=1.0, n_outer=8, n_inner=150):
    """
    Quadratic penalty method:
        min f(x) + (rho/2)*||g(x)||^2 + (rho/2)*||max(0,h(x))||^2
    Increase rho each outer iteration to enforce feasibility.
    """
    x = x_init.clone().detach().requires_grad_(True)
    rho = rho_init
    log = []

    for outer in range(n_outer):
        opt = torch.optim.Adam([x], lr=lr)
        for _ in range(n_inner):
            opt.zero_grad()
            loss = (f_fn(x)
                    + (rho/2) * g_eq(x)**2
                    + (rho/2) * torch.clamp(h_ineq(x), min=0.0)**2)
            loss.backward()
            opt.step()
        rho *= 4.0
        with torch.no_grad():
            log.append({'rho': rho,
                        'f': f_fn(x).item(),
                        'g': g_eq(x).item(),
                        'h': h_ineq(x).item()})
        print(f"Outer {outer+1}: rho={rho:.1f}  f={log[-1]['f']:.4f}  "
              f"g={log[-1]['g']:.4f}  h={log[-1]['h']:.4f}")
    return x.detach(), log

# min (x0-3)^2 + (x1-2)^2  s.t.  x0+x1=4,  x0>=1
f_fn  = lambda x: (x[0]-3)**2 + (x[1]-2)**2
g_eq  = lambda x: x[0] + x[1] - 4.0
h_ineq = lambda x: 1.0 - x[0]  # h<=0 means x0>=1

x_opt, history = penalty_optimize(f_fn, g_eq, h_ineq, torch.tensor([2.0, 2.0]))
print(f"\nOptimal: {x_opt.numpy()}, f={f_fn(x_opt).item():.4f}")
print(f"Feasibility: g={g_eq(x_opt).item():.4f} (target 0), h={h_ineq(x_opt).item():.4f} (target <=0)")
```

## Applications in Machine Learning

KKT conditions and Lagrangian duality appear throughout ML beyond SVMs. Constrained policy optimization (CPO) in RL enforces safety constraints as KKT inequality conditions. Variational autoencoders use a Lagrangian to balance reconstruction loss and KL divergence (β-VAE sets the KL multiplier β). Network compression with sparsity budgets is a constrained optimization problem amenable to Lagrangian relaxation.

- SVM: dual QP gives sparse solution via complementary slackness — only support vectors matter
- CPO (Constrained Policy Optimization): KL constraint as Lagrangian in RL
- β-VAE: β is the Lagrange multiplier on the KL ≤ ε information bottleneck constraint
- Water-filling (power allocation): KKT gives closed-form solution for channel capacity
- Lasso / ADMM: augmented Lagrangian splitting for L1-constrained regression
- Fair ML: demographic parity as equality constraint on model outputs

---

