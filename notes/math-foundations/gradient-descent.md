---
title: "Gradient Descent — Convergence Analysis and Step Size"
slug: "gradient-descent"
description: "Rigorous treatment of gradient descent convergence theory including L-smooth functions, convex and strongly convex rates, saddle points in non-convex settings, gradient flow ODE, and the Polyak-Łojasiewicz condition."
tags: ["optimization", "calculus", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiR3JhZGllbnQgZGVzY2VudCBpcyB0aGUgYmFja2JvbmUgb2YgdmlydHVhbGx5IGV2ZXJ5IG1hY2hpbmUgbGVhcm5pbmcgb3B0aW1pemVyLiBZZXQgbW9zdCBwcmFjdGl0aW9uZXJzIHRyZWF0IGl0IGFzIGEgYmxhY2sgYm94OiBzdWJ0cmFjdCB0aGUgZ3JhZGllbnQsIHNjYWxlIGJ5IGxlYXJuaW5nIHJhdGUsIHJlcGVhdC4gQSByaWdvcm91cyB1bmRlcnN0YW5kaW5nIOKAlCBjb252ZXJnZW5jZSByYXRlcywgc21vb3RobmVzcyBjb25kaXRpb25zLCBzYWRkbGUgcG9pbnQgZHluYW1pY3MsIGFuZCB0aGUgcmVsYXRpb25zaGlwIGJldHdlZW4gZGlzY3JldGUgdXBkYXRlcyBhbmQgY29udGludW91cyBncmFkaWVudCBmbG93IOKAlCBpcyBlc3NlbnRpYWwgZm9yIGNob29zaW5nIGxlYXJuaW5nIHJhdGVzIGNvcnJlY3RseSwgZGlhZ25vc2luZyB0cmFpbmluZyBmYWlsdXJlcywgYW5kIHVuZGVyc3RhbmRpbmcgd2h5IG1vcmUgc29waGlzdGljYXRlZCBvcHRpbWl6ZXJzIChBZGFtLCBMaW9uKSBoZWxwLiBUaGlzIG5vdGUgY292ZXJzOiB1cGRhdGUgcnVsZSBkZXJpdmF0aW9uLCBMLXNtb290aCBjb252ZXJnZW5jZSBndWFyYW50ZWVzLCBjb252ZXggdnMgc3Ryb25nbHkgY29udmV4IHJhdGVzLCBub24tY29udmV4IGxhbmRzY2FwZSBkaWZmaWN1bHRpZXMsIGFuZCB0aGUgZ3JhZGllbnQgZmxvdyBPREUgcGVyc3BlY3RpdmUuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29yZSBEZWZpbml0aW9uOiBUaGUgVXBkYXRlIFJ1bGUifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgZ3JhZGllbnQgZGVzY2VudCB1cGRhdGUgZm9yIG1pbmltaXppbmcgZjog4oSd4oG/IOKGkiDihJ0gaXMgzrjigpzigorigoEgPSDOuOKCnCDiiJIgzrfiiIdmKM644oKcKSwgd2hlcmUgzrcgPiAwIGlzIHRoZSBsZWFybmluZyByYXRlIChzdGVwIHNpemUpLiBUaGUgbmVnYXRpdmUgZ3JhZGllbnQgZGlyZWN0aW9uIOKIkuKIh2YozrgpIGlzIHRoZSBzdGVlcGVzdCBkZXNjZW50IGRpcmVjdGlvbiAoYnkgQ2F1Y2h5LVNjaHdhcno6IHRoZSBkaXJlY3Rpb24gbWF4aW1hbGx5IGRlY3JlYXNpbmcgZiBwZXIgdW5pdCBkaXN0YW5jZSkuIEVhY2ggc3RlcCBkZWNyZWFzZXMgZiBieSBhcHByb3hpbWF0ZWx5IM634oCW4oiHZuKAlsKyICh0byBmaXJzdCBvcmRlcik6IGYozrjigpwg4oiSIM634oiHZikg4omIIGYozrgpIOKIkiDOt+KAluKIh2bigJbCsi4gVGhlIGNvbnRpbnVvdXMgYW5hbG9ndWUgaXMgdGhlIGdyYWRpZW50IGZsb3cgT0RFOiBkzrgvZHQgPSDiiJLiiIdmKM64KSwgd2hpY2ggY29udmVyZ2VzIHRvIGEgc3RhdGlvbmFyeSBwb2ludCBhcyB04oaS4oieIHVuZGVyIG1pbGQgY29uZGl0aW9ucy4gRGlzY3JldGUgR0QgYXBwcm94aW1hdGVzIHRoaXMgT0RFIHdpdGggc3RlcCBzaXplIM63IGFzIHRoZSB0ZW1wb3JhbCBkaXNjcmV0aXphdGlvbiBwYXJhbWV0ZXIuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgZ3JhZGllbnRfZGVzY2VudChncmFkX2YsIHgwLCBsciwgbl9zdGVwcywgZj1Ob25lKTpcbiAgICBcIlwiXCJCYXNpYyBncmFkaWVudCBkZXNjZW50LiBSZXR1cm5zIHRyYWplY3RvcnkgYW5kIGxvc3MgaGlzdG9yeS5cIlwiXCJcbiAgICB4ID0gbnAuYXJyYXkoeDAsIGR0eXBlPW5wLmZsb2F0NjQpXG4gICAgdHJhamVjdG9yeSA9IFt4LmNvcHkoKV1cbiAgICBsb3NzZXMgPSBbZih4KV0gaWYgZiBlbHNlIFtdXG5cbiAgICBmb3IgdCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgZyA9IGdyYWRfZih4KVxuICAgICAgICB4ID0geCAtIGxyICogZ1xuICAgICAgICB0cmFqZWN0b3J5LmFwcGVuZCh4LmNvcHkoKSlcbiAgICAgICAgaWYgZjogbG9zc2VzLmFwcGVuZChmKHgpKVxuXG4gICAgcmV0dXJuIG5wLmFycmF5KHRyYWplY3RvcnkpLCBsb3NzZXNcblxuIyBFeGFtcGxlOiBtaW5pbWl6ZSBmKHgsIHkpID0geF4yICsgNHleMiAoY29uZGl0aW9uIG51bWJlciBrYXBwYSA9IDQpXG5mID0gbGFtYmRhIHg6IHhbMF0qKjIgKyA0KnhbMV0qKjJcbmdyYWRfZiA9IGxhbWJkYSB4OiBucC5hcnJheShbMip4WzBdLCA4KnhbMV1dKVxuXG54MCA9IG5wLmFycmF5KFszLjAsIDIuMF0pXG5cbiMgVGhyZWUgbGVhcm5pbmcgcmF0ZXM6IG9wdGltYWwgZXRhID0gMS9MID0gMS84LCB0b28gc21hbGwsIHRvbyBsYXJnZVxuZm9yIGxyLCBsYWJlbCBpbiBbKDAuMDAxLCAndG9vIHNtYWxsJyksICgwLjEyNSwgJ29wdGltYWwgZXRhPTEvTCcpLCAoMC4yNiwgJ3RvbyBsYXJnZScpXTpcbiAgICB0cmFqLCBsb3NzZXMgPSBncmFkaWVudF9kZXNjZW50KGdyYWRfZiwgeDAsIGxyPWxyLCBuX3N0ZXBzPTIwMCwgZj1mKVxuICAgIGlmIGxvc3NlczpcbiAgICAgICAgZmluYWwgPSBsb3NzZXNbLTFdXG4gICAgICAgIHByaW50KGZcImxyPXtscn0gKHtsYWJlbH0pOiBmaW5hbCBsb3NzPXtmaW5hbDouNmZ9IGFmdGVyIDIwMCBzdGVwc1wiKVxuICAgIGVsc2U6XG4gICAgICAgIHByaW50KGZcImxyPXtscn0gKHtsYWJlbH0pOiBkaXZlcmdlZFwiKVxuXG4jIEV4YWN0IGNvbnZlcmdlbmNlIHJhdGUgZm9yIHN0cm9uZ2x5IGNvbnZleDogZih0aGV0YV9UKSAtIGYqIDw9ICgxIC0gMipldGEqbXUqTC8obXUrTCkpXlQgKiAoZih0aGV0YV8wKSAtIGYqKVxuIyBGb3IgZih4LHkpID0geF4yICsgNHleMjogbXUgPSAyIChtaW4gZWlnZW52YWx1ZSBvZiBIZXNzaWFuKSwgTCA9IDggKG1heCBlaWdlbnZhbHVlKVxubXUsIEwgPSAyLjAsIDguMFxuZXRhX29wdCA9IDIgLyAobXUgKyBMKSAgIyBPcHRpbWFsIHN0ZXAgZm9yIHN0cm9uZ2x5IGNvbnZleDogMi8obXUrTClcbnJobyA9IChMIC0gbXUpIC8gKEwgKyBtdSkgICMgQ29udmVyZ2VuY2UgcmF0ZVxucHJpbnQoZlwiXFxuT3B0aW1hbCBldGEgZm9yIHN0cm9uZ2x5IGNvbnZleDoge2V0YV9vcHQ6LjRmfSwgcmhvID0ge3JobzouNGZ9XCIpXG5wcmludChmXCJTdGVwcyB0byAxZS02IHByZWNpc2lvbjoge2ludChucC5sb2coMWUtNikgLyBucC5sb2cocmhvKSkgKyAxfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkwtU21vb3RobmVzcyBhbmQgQ29udmVyZ2VuY2UgR3VhcmFudGVlcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkEgZnVuY3Rpb24gZiBpcyBMLXNtb290aCAoTC1MaXBzY2hpdHogZ3JhZGllbnQpIGlmIOKAluKIh2YoeCkg4oiSIOKIh2YoeSnigJYg4omkIEzigJZ44oiSeeKAliBmb3IgYWxsIHgseS4gRXF1aXZhbGVudGx5OiBmKHkpIOKJpCBmKHgpICsg4oiHZih4KeG1gCh54oiSeCkgKyBMLzLigJZ54oiSeOKAlsKyICh0aGUgZ3JhZGllbnQgZGVzY2VudCBsZW1tYSkuIFRoaXMgcXVhZHJhdGljIHVwcGVyIGJvdW5kIGd1YXJhbnRlZXMgdGhhdCBhIHN0ZXAgzrcgPSAxL0wgYWx3YXlzIGRlY3JlYXNlcyBmOiBmKM644oiSzrfiiIdmKSDiiaQgZijOuCkg4oiSICgxLzJMKeKAluKIh2Yozrgp4oCWwrIuIEZvciBjb252ZXggTC1zbW9vdGggZjogZ3JhZGllbnQgZGVzY2VudCB3aXRoIM63IOKJpCAxL0wgYWNoaWV2ZXMgZijOuOKCnCkg4oiSIGYqIOKJpCDigJbOuOKCgOKIks64KuKAlsKyLygyzrdUKSDigJQgcmF0ZSBPKDEvVCkuIEZvciDOvC1zdHJvbmdseSBjb252ZXggTC1zbW9vdGggZjogZijOuOKCnCkg4oiSIGYqIOKJpCAoMeKIkjLOt868TC8ozrwrTCkp4bWAKGYozrjigoAp4oiSZiopIOKAlCBsaW5lYXIgcmF0ZSBPKM+B4bWAKSB3aGVyZSDPgSA9ICjOuuKIkjEpLyjOuisxKSA8IDEsIM66ID0gTC/OvC4gU3Ryb25nIGNvbnZleGl0eSBwcm92aWRlcyB0aGUgcHVsbCB0b3dhcmQgbWluaW11bSB0aGF0IGVuYWJsZXMgbGluZWFyIGNvbnZlcmdlbmNlLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHZlcmlmeV9sX3Ntb290aG5lc3MoZiwgZ3JhZF9mLCB4LCB5LCBMX2NhbmRpZGF0ZSk6XG4gICAgXCJcIlwiQ2hlY2sgaWYgTC1zbW9vdGhuZXNzIGluZXF1YWxpdHkgaG9sZHMgYXQgeCwgeS5cIlwiXCJcbiAgICBsaHMgPSBmKHkpXG4gICAgcmhzID0gZih4KSArIGdyYWRfZih4KSBAICh5IC0geCkgKyBMX2NhbmRpZGF0ZS8yICogbnAubGluYWxnLm5vcm0oeS14KSoqMlxuICAgIHJldHVybiBsaHMgPD0gcmhzICsgMWUtMTAsIGxocywgcmhzXG5cbmRlZiBjb252ZXJnZW5jZV9yYXRlX2FuYWx5c2lzKGYsIGdyYWRfZiwgeDAsIGZfc3RhciwgbXUsIEwsIG5fc3RlcHM9NTAwKTpcbiAgICBcIlwiXCJcbiAgICBBbmFseXplIGNvbnZlcmdlbmNlIHJhdGUgZm9yIEwtc21vb3RoIHN0cm9uZ2x5IGNvbnZleCBmdW5jdGlvbi5cbiAgICBFeHBlY3RlZDogbGluZWFyIHJhdGUgcmhvID0gKEwtbXUpLyhMK211KS5cbiAgICBcIlwiXCJcbiAgICBldGEgPSAyLjAgLyAobXUgKyBMKSAgIyBPcHRpbWFsIHN0ZXAgc2l6ZSBmb3Igc3Ryb25nbHkgY29udmV4XG4gICAgeCA9IHgwLmNvcHkoKVxuICAgIGdhcHMgPSBbXVxuXG4gICAgZm9yIHQgaW4gcmFuZ2Uobl9zdGVwcyk6XG4gICAgICAgIGdhcCA9IGYoeCkgLSBmX3N0YXJcbiAgICAgICAgZ2Fwcy5hcHBlbmQoZ2FwKVxuICAgICAgICBpZiBnYXAgPCAxZS0xMjogYnJlYWtcbiAgICAgICAgeCA9IHggLSBldGEgKiBncmFkX2YoeClcblxuICAgICMgRml0IGVtcGlyaWNhbCBjb252ZXJnZW5jZSByYXRlXG4gICAgcmhvX3RoZW9yeSA9IChMIC0gbXUpIC8gKEwgKyBtdSlcbiAgICByaG9fZW1waXJpY2FsID0gKGdhcHNbLTFdIC8gZ2Fwc1swXSkgKiogKDEgLyBsZW4oZ2FwcykpXG5cbiAgICByZXR1cm4gbnAuYXJyYXkoZ2FwcyksIHJob190aGVvcnksIHJob19lbXBpcmljYWxcblxuIyBmKHgpID0geF5UIEEgeCAvIDIgIHdoZXJlIEEgPSBkaWFnKDIsIDQsIDYsIDgpICAoc3Ryb25nbHkgY29udmV4LCBMLXNtb290aClcbkEgPSBucC5kaWFnKFsyLjAsIDQuMCwgNi4wLCA4LjBdKVxuZiA9IGxhbWJkYSB4OiAwLjUgKiB4IEAgQSBAIHhcbmdyYWRfZiA9IGxhbWJkYSB4OiBBIEAgeFxueDAgPSBucC5hcnJheShbMy4wLCAyLjAsIDEuMCwgMC41XSlcbmZfc3RhciA9IDAuMCAgIyBtaW5pbXVtIGF0IG9yaWdpblxubXUsIEwgPSAyLjAsIDguMCAgIyBtaW4gYW5kIG1heCBlaWdlbnZhbHVlcyBvZiBBXG5cbmdhcHMsIHJob190aCwgcmhvX2VtcCA9IGNvbnZlcmdlbmNlX3JhdGVfYW5hbHlzaXMoZiwgZ3JhZF9mLCB4MCwgZl9zdGFyLCBtdSwgTClcbnByaW50KGZcIlRoZW9yZXRpY2FsIHJhdGUgcmhvID0ge3Job190aDouNGZ9XCIpXG5wcmludChmXCJFbXBpcmljYWwgcmF0ZSByaG8gPSB7cmhvX2VtcDouNGZ9XCIpXG5wcmludChmXCJTdGVwcyB0byAxZS02OiB0aGVvcmV0aWNhbCB7aW50KG5wLmxvZygxZS02KSAvIG5wLmxvZyhyaG9fdGgpKSsxfSwgYWN0dWFsIHtsZW4oZ2Fwcyl9XCIpXG5cbiMgVmVyaWZ5IEwtc21vb3RobmVzc1xueF90ZXN0ID0gbnAuYXJyYXkoWzEuMCwgMS4wLCAxLjAsIDEuMF0pXG55X3Rlc3QgPSB4X3Rlc3QgKyAwLjEgKiBucC5yYW5kb20ucmFuZG4oNClcbm9rLCBsaHMsIHJocyA9IHZlcmlmeV9sX3Ntb290aG5lc3MoZiwgZ3JhZF9mLCB4X3Rlc3QsIHlfdGVzdCwgTClcbnByaW50KGZcIlxcbkwtc21vb3RobmVzcyBjaGVjazoge29rfSAgKGxocz17bGhzOi40Zn0gPD0gcmhzPXtyaHM6LjRmfSlcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJOb24tQ29udmV4IExhbmRzY2FwZXM6IFNhZGRsZSBQb2ludHMgYW5kIExvY2FsIE1pbmltYSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZvciBub24tY29udmV4IGYgKGFsbCBuZXVyYWwgbmV0d29ya3MpLCBHRCBpcyBub3QgZ3VhcmFudGVlZCB0byBmaW5kIHRoZSBnbG9iYWwgbWluaW11bS4gVHdvIG9ic3RhY2xlcyBhcmlzZTogKDEpIExvY2FsIG1pbmltYSDigJQgR0QgY29udmVyZ2VzIHRvIGEgbG9jYWwgc3RhdGlvbmFyeSBwb2ludCDiiIdmKM64Kik9MC4gSG93ZXZlciwgZm9yIG92ZXItcGFyYW1ldGVyaXplZCBuZXR3b3JrcywgcmVjZW50IHRoZW9yeSAoZS5nLiwgTlRLIHJlZ2ltZSkgc3VnZ2VzdHMgdGhhdCBsb2NhbCBtaW5pbWEgYXJlIG9mdGVuIG5lYXItZ2xvYmFsLiAoMikgU2FkZGxlIHBvaW50cyDigJQgY3JpdGljYWwgcG9pbnRzIHdoZXJlIHNvbWUgSGVzc2lhbiBlaWdlbnZhbHVlcyBhcmUgbmVnYXRpdmUgKGRpcmVjdGlvbnMgb2YgZGVjcmVhc2UgZXhpc3QpLiBJbiBoaWdoIGRpbWVuc2lvbnMsIHNhZGRsZSBwb2ludHMgYXJlIGV4cG9uZW50aWFsbHkgbW9yZSBjb21tb24gdGhhbiBsb2NhbCBtaW5pbWEgKEJob2phbmFwYWxsaSBldCBhbC4pLiBUaGUgUG9seWFrLcWBb2phc2lld2ljeiAoUEwpIGNvbmRpdGlvbiBwcm92aWRlcyBub24tY29udmV4IGNvbnZlcmdlbmNlOiBpZiDigJbiiIdm4oCWwrIg4omlIDLOvChm4oiSZiopLCB0aGVuIEdEIGNvbnZlcmdlcyBsaW5lYXJseSBldmVuIHdpdGhvdXQgY29udmV4aXR5LiBPdmVyLXBhcmFtZXRlcml6ZWQgbmV1cmFsIG5ldHdvcmtzIG9mdGVuIHNhdGlzZnkgUEwgZW1waXJpY2FsbHksIHdoaWNoIGhlbHBzIGV4cGxhaW4gd2h5IEdEIGZpbmRzIGdvb2Qgc29sdXRpb25zIGRlc3BpdGUgdGhlIG5vbi1jb252ZXggbGFuZHNjYXBlLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk1MIENvbm5lY3Rpb25zOiBCYXRjaCBHRCB2cyBNaW5pLUJhdGNoIHZzIFNHRCJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZ1bGwtYmF0Y2ggR0QgY29tcHV0ZXMgdGhlIGdyYWRpZW50IG92ZXIgdGhlIGVudGlyZSBkYXRhc2V0LiBGb3IgbiBzYW1wbGVzIGFuZCBkIHBhcmFtZXRlcnM6IGNvc3QgTyhuZCkgcGVyIHN0ZXAuIE1pbmktYmF0Y2ggR0QgdXNlcyBhIHJhbmRvbSBzdWJzZXQgQiBvZiBzaXplIEI6IGdyYWRpZW50IGVzdGltYXRlIMSdID0gKDEvQinOo197aeKIiEJ94oiHTOG1oijOuCkuIFRoaXMgaXMgYW4gdW5iaWFzZWQgZXN0aW1hdGUgb2YgdGhlIHRydWUgZ3JhZGllbnQ6IEVbxJ1dID0g4oiHTC4gVmFyaWFuY2U6IFZhclvEnV0g4omIIM+DwrIvQiB3aGVyZSDPg8KyIGlzIHRoZSBwZXItc2FtcGxlIGdyYWRpZW50IHZhcmlhbmNlLiBTR0QgKEI9MSkgaGFzIGhpZ2hlc3QgdmFyaWFuY2UgYnV0IGJlc3QgcGFyYWxsZWxpc20gYW5kIGltcGxpY2l0IHJlZ3VsYXJpemF0aW9uLiBNaW5pYmF0Y2ggU0dEIHdpdGggQj0yNTbigJM0MDk2IGlzIHRoZSBwcmFjdGljYWwgc3dlZXQgc3BvdDogZW5vdWdoIG5vaXNlIGZvciBnZW5lcmFsaXphdGlvbiwgZW5vdWdoIHNpZ25hbCBmb3Igc3RhYmxlIGNvbnZlcmdlbmNlLiBUaGUgbGluZWFyIHNjYWxpbmcgcnVsZSAoR295YWwgZXQgYWwuIDIwMTcpOiBtdWx0aXBseSBMUiBieSBCLzI1NiB3aGVuIHNjYWxpbmcgYmF0Y2ggc2l6ZSDigJQgdGhpcyBwcmVzZXJ2ZXMgZ3JhZGllbnQgbm9pc2Ugc3RhdGlzdGljcyBhbmQga2VlcHMgdGhlIGVmZmVjdGl2ZSB1cGRhdGUgbWFnbml0dWRlIGNvbnN0YW50IGFjcm9zcyBkaWZmZXJlbnQgaGFyZHdhcmUgY29uZmlndXJhdGlvbnMuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbWluaWJhdGNoX3NnZChsb3NzX2ZuLCBncmFkX2ZuLCB0aGV0YTAsIFgsIHksIGxyLCBiYXRjaF9zaXplLCBuX2Vwb2Nocyk6XG4gICAgXCJcIlwiXG4gICAgTWluaWJhdGNoIFNHRCB3aXRoIGRhdGEgc2h1ZmZsaW5nIHBlciBlcG9jaC5cbiAgICBSZXR1cm5zOiBmaW5hbCB0aGV0YSwgcGVyLWVwb2NoIGF2ZXJhZ2UgbG9zcy5cbiAgICBcIlwiXCJcbiAgICB0aGV0YSA9IHRoZXRhMC5jb3B5KClcbiAgICBuID0gbGVuKFgpXG4gICAgZXBvY2hfbG9zc2VzID0gW11cblxuICAgIGZvciBlcG9jaCBpbiByYW5nZShuX2Vwb2Nocyk6XG4gICAgICAgICMgU2h1ZmZsZSBkYXRhIGVhY2ggZXBvY2ggKGNyaXRpY2FsIGZvciBjb252ZXJnZW5jZSlcbiAgICAgICAgaWR4ID0gbnAucmFuZG9tLnBlcm11dGF0aW9uKG4pXG4gICAgICAgIFhfc2h1ZiwgeV9zaHVmID0gWFtpZHhdLCB5W2lkeF1cblxuICAgICAgICBiYXRjaF9sb3NzZXMgPSBbXVxuICAgICAgICBmb3Igc3RhcnQgaW4gcmFuZ2UoMCwgbiwgYmF0Y2hfc2l6ZSk6XG4gICAgICAgICAgICBlbmQgPSBtaW4oc3RhcnQgKyBiYXRjaF9zaXplLCBuKVxuICAgICAgICAgICAgWGIgPSBYX3NodWZbc3RhcnQ6ZW5kXVxuICAgICAgICAgICAgeWIgPSB5X3NodWZbc3RhcnQ6ZW5kXVxuXG4gICAgICAgICAgICBnID0gZ3JhZF9mbih0aGV0YSwgWGIsIHliKVxuICAgICAgICAgICAgdGhldGEgPSB0aGV0YSAtIGxyICogZ1xuICAgICAgICAgICAgYmF0Y2hfbG9zc2VzLmFwcGVuZChsb3NzX2ZuKHRoZXRhLCBYYiwgeWIpKVxuXG4gICAgICAgIGVwb2NoX2xvc3Nlcy5hcHBlbmQobnAubWVhbihiYXRjaF9sb3NzZXMpKVxuXG4gICAgcmV0dXJuIHRoZXRhLCBlcG9jaF9sb3NzZXNcblxuIyBMaW5lYXIgcmVncmVzc2lvbjogTCh3KSA9IHx8WHcgLSB5fHxeMiAvIG5cbm5wLnJhbmRvbS5zZWVkKDApXG5uLCBkID0gMTAwMCwgMjBcblggPSBucC5yYW5kb20ucmFuZG4obiwgZClcbndfdHJ1ZSA9IG5wLnJhbmRvbS5yYW5kbihkKVxueSA9IFggQCB3X3RydWUgKyAwLjEgKiBucC5yYW5kb20ucmFuZG4obilcblxubG9zc19mbiA9IGxhbWJkYSB3LCBYLCB5OiBucC5tZWFuKChYIEAgdyAtIHkpKioyKVxuZ3JhZF9mbiA9IGxhbWJkYSB3LCBYLCB5OiAyICogWC5UIEAgKFggQCB3IC0geSkgLyBsZW4oeSlcblxuIyBDb21wYXJlIGJhdGNoIHNpemVzXG5mb3IgYnMgaW4gWzEsIDMyLCAyNTYsIG5dOlxuICAgIHcwID0gbnAuemVyb3MoZClcbiAgICBuX2Vwb2NocyA9IDIwIGlmIGJzIDwgbiBlbHNlIDIwMFxuICAgIGxyID0gMC4wMVxuICAgIHdfZmluYWwsIGxvc3NlcyA9IG1pbmliYXRjaF9zZ2QobG9zc19mbiwgZ3JhZF9mbiwgdzAsIFgsIHksIGxyLCBicywgbl9lcG9jaHMpXG4gICAgZmluYWxfbG9zcyA9IGxvc3NfZm4od19maW5hbCwgWCwgeSlcbiAgICBwcmludChmXCJCPXticzo0ZH06IGZpbmFsX2xvc3M9e2ZpbmFsX2xvc3M6LjRmfSwgd19lcnJvcj17bnAubGluYWxnLm5vcm0od19maW5hbCAtIHdfdHJ1ZSk6LjRmfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkdyYWRpZW50IEZsb3c6IFRoZSBDb250aW51b3VzLVRpbWUgUGVyc3BlY3RpdmUifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgZ3JhZGllbnQgZmxvdyBPREUgZM64L2R0ID0g4oiS4oiHZijOuCkgaXMgdGhlIGNvbnRpbnVvdXMtdGltZSBsaW1pdCBvZiBncmFkaWVudCBkZXNjZW50IGFzIM634oaSMC4gU29sdXRpb25zIM64KHQpIHNhdGlzZnkgZijOuCh0KSkgZGVjcmVhc2luZyBtb25vdG9uaWNhbGx5LiBGb3IgY29udmV4IGYsIGdyYWRpZW50IGZsb3cgY29udmVyZ2VzIGFzIGYozrgodCkpIOKIkiBmKiDiiaQg4oCWzrgoMCniiJLOuCrigJbCsi8oMnQpLiBGb3Igc3Ryb25nbHkgY29udmV4OiBmKM64KHQpKSDiiJIgZiog4omkIGVee+KIkjLOvHR9KGYozrgoMCkp4oiSZiopLiBHcmFkaWVudCBkZXNjZW50IHdpdGggc3RlcCDOtyBhcHByb3hpbWF0ZXMgZ3JhZGllbnQgZmxvdyB3aXRoIHQgPSDOt1QuIFRoZSBncmFkaWVudCBmbG93IHBlcnNwZWN0aXZlIGVuYWJsZXM6ICgxKSBjb250aW51b3VzIGNvbnZlcmdlbmNlIHByb29mcyB0aGF0IHRyYW5zZmVyIGNsZWFubHkgdG8gZGlzY3JldGUgdXBkYXRlczsgKDIpIGFuYWx5c2lzIG9mIG1vbWVudHVtIGFzIGEgc2Vjb25kLW9yZGVyIE9ERSAoaGVhdnkgYmFsbDogzrgnJyArIM6zzrgnICsg4oiHZijOuCkgPSAwKTsgKDMpIHN0b2NoYXN0aWMgZ3JhZGllbnQgZmxvdyAoTGFuZ2V2aW4gZHluYW1pY3M6IGTOuCA9IOKIkuKIh2bCt2R0ICsg4oiaKDJUKWRXKSBhcyBhIHByaW5jaXBsZWQgbW9kZWwgZm9yIFNHROKAmXMgaW5oZXJlbnQgbm9pc2UgaW4gZmluaXRlLWJhdGNoIHRyYWluaW5nIHJlZ2ltZXMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiSW1wbGVtZW50YXRpb24gUGl0ZmFsbHMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJMZWFybmluZyByYXRlIHRvbyBsYXJnZTogR0QgZGl2ZXJnZXMgd2hlbiDOtyA+IDIvTCAodGhlIHN0ZXAgZXhjZWVkcyB0aGUgY3VydmF0dXJlIGJvdW5kIGFuZCBvc2NpbGxhdGVzKS4gU3ltcHRvbTogbG9zcyBpbmNyZWFzZXMgYWZ0ZXIgYSBmZXcgc3RlcHMgb3Igb3NjaWxsYXRlcyB3aWxkbHkuIEZpeDogY2hlY2sgTCB2aWEgcG93ZXIgaXRlcmF0aW9uIG9uIHRoZSBIZXNzaWFuLCBzZXQgzrcg4omkIDEvTC4gTGVhcm5pbmcgcmF0ZSB0b28gc21hbGw6IGNvbnZlcmdlbmNlIGlzIGd1YXJhbnRlZWQgYnV0IGdsYWNpYWxseSBzbG93IOKAlCBlc3BlY2lhbGx5IHByb2JsZW1hdGljIHdpdGggaGlnaCBjb25kaXRpb24gbnVtYmVyIM66LCB3aGVyZSBPKM66KSBzdGVwcyBhcmUgbmVlZGVkIHBlciBkaWdpdCBvZiBwcmVjaXNpb24uIFN5bXB0b206IGxvc3MgZGVjcmVhc2VzIHN0ZWFkaWx5IGJ1dCB2ZXJ5IHNsb3dseS4gRm9yZ2V0dGluZyB0byBzaHVmZmxlIGRhdGE6IGN5Y2xpYyBncmFkaWVudCBlc3RpbWF0ZXMgY2FuIGhhdmUgc3lzdGVtYXRpYyBiaWFzIGFuZCBzbG93IGNvbnZlcmdlbmNlIHNpZ25pZmljYW50bHkuIERpYWdub3NpczogY29tcGFyZSBjeWNsaWMgdnMgc2h1ZmZsZWQgb24gYSBzaW1wbGUgcHJvYmxlbS4gTm90IG5vcm1hbGl6aW5nIGZlYXR1cmVzOiBjcmVhdGVzIGlsbC1jb25kaXRpb25lZCBsb3NzIGxhbmRzY2FwZSB3aGVyZSDOuiDiiYggKG1heCBmZWF0dXJlIHNjYWxlL21pbiBmZWF0dXJlIHNjYWxlKcKyIOKAlCBncmFkaWVudCBkZXNjZW50IHppZ3phZ3MgcmF0aGVyIHRoYW4gY29udmVyZ2luZyBkaXJlY3RseS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQcmFjdGljYWwgR3VpZGFuY2UifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJTZXQgaW5pdGlhbCBMUiB2aWEgdGhlIGxlYXJuaW5nIHJhdGUgcmFuZ2UgdGVzdDogaW5jcmVhc2UgTFIgZnJvbSAxZS03IHRvIDEwIG92ZXIgMTAwIHN0ZXBzLCBwbG90IGxvc3MgdnMgTFIsIHBpY2sgdGhlIExSIGp1c3QgYmVmb3JlIHRoZSBsb3NzIHN0YXJ0cyB0byBpbmNyZWFzZS4gRm9yIGNvbnZleCBwcm9ibGVtcyB3aXRoIGtub3duIEwsIHNldCDOtyA9IDEvTCBleGFjdGx5LiBGb3IgbmV1cmFsIG5ldHdvcmtzLCBzdGFydCBhdCDOtyA9IDFlLTMgKEFkYW0pIG9yIM63ID0gMC4xIChTR0Qgd2l0aCBtb21lbnR1bSkuIFVzZSBjb3NpbmUgYW5uZWFsaW5nIGZyb20gzrdfbWF4IHRvIM63X21pbiA9IM63X21heC8xMDAgb3ZlciB0cmFpbmluZy4gTW9uaXRvciBncmFkaWVudCBub3JtIOKAluKIh0zigJY6IHNob3VsZCBkZWNyZWFzZSBvdmVyIHRyYWluaW5nIGZvciBjb252ZXggb2JqZWN0aXZlcy4gU3VkZGVuIHNwaWtlcyBpbiBncmFkaWVudCBub3JtIGluZGljYXRlIGluc3RhYmlsaXR5IOKAlCByZWR1Y2UgTFIgb3IgYWRkIGdyYWRpZW50IGNsaXBwaW5nLiBGZWF0dXJlIG5vcm1hbGl6YXRpb24gKHplcm8gbWVhbiwgdW5pdCB2YXJpYW5jZSkgaXMgY3JpdGljYWw6IGl0IHRyYW5zZm9ybXMgdGhlIGxvc3MgbGFuZHNjYXBlIGZyb20gaGlnaGx5IGFuaXNvdHJvcGljIHRvIGFwcHJveGltYXRlbHkgaXNvdHJvcGljLCByZWR1Y2luZyB0aGUgZWZmZWN0aXZlIGNvbmRpdGlvbiBudW1iZXIgYW5kIGVuYWJsaW5nIGxhcmdlciBzYWZlIGxlYXJuaW5nIHJhdGVzLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuXG5kZWYgbGVhcm5pbmdfcmF0ZV9yYW5nZV90ZXN0KG1vZGVsLCBvcHRpbWl6ZXJfY2xzLCB0cmFpbl9sb2FkZXIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdGFydF9scj0xZS03LCBlbmRfbHI9MTAuMCwgbl9zdGVwcz0xMDApOlxuICAgIFwiXCJcIlxuICAgIExSIHJhbmdlIHRlc3QgKFNtaXRoIDIwMTUpOiBpbmNyZWFzZSBMUiBnZW9tZXRyaWNhbGx5LCBmaW5kIHN3ZWV0IHNwb3QuXG4gICAgUmV0dXJucyBscl9oaXN0b3J5LCBsb3NzX2hpc3RvcnkgZm9yIHBsb3R0aW5nLlxuICAgIFwiXCJcIlxuICAgICMgQnVpbGQgTFIgc2NoZWR1bGU6IGdlb21ldHJpYyBpbmNyZWFzZVxuICAgIGxyX3NjaGVkdWxlID0gbnAuZ2VvbXNwYWNlKHN0YXJ0X2xyLCBlbmRfbHIsIG5fc3RlcHMpXG4gICAgb3B0aW1pemVyID0gb3B0aW1pemVyX2Nscyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPXN0YXJ0X2xyKVxuXG4gICAgbHJfaGlzdG9yeSA9IFtdXG4gICAgbG9zc19oaXN0b3J5ID0gW11cbiAgICBzbW9vdGhlZF9sb3NzID0gTm9uZVxuICAgIGJldGEgPSAwLjkgICMgRU1BIHNtb290aGluZ1xuXG4gICAgZm9yIHN0ZXAsIChsciwgYmF0Y2gpIGluIGVudW1lcmF0ZSh6aXAobHJfc2NoZWR1bGUsIHRyYWluX2xvYWRlcikpOlxuICAgICAgICAjIFVwZGF0ZSBMUlxuICAgICAgICBmb3IgcGcgaW4gb3B0aW1pemVyLnBhcmFtX2dyb3VwczpcbiAgICAgICAgICAgIHBnWydsciddID0gZmxvYXQobHIpXG5cbiAgICAgICAgWCwgeSA9IGJhdGNoXG4gICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgICAgICBsb3NzID0gdG9yY2gubm4uZnVuY3Rpb25hbC5tc2VfbG9zcyhtb2RlbChYKSwgeSlcbiAgICAgICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgICAgIG9wdGltaXplci5zdGVwKClcblxuICAgICAgICByYXcgPSBsb3NzLml0ZW0oKVxuICAgICAgICBzbW9vdGhlZF9sb3NzID0gYmV0YSAqIChzbW9vdGhlZF9sb3NzIG9yIHJhdykgKyAoMSAtIGJldGEpICogcmF3XG4gICAgICAgIGxyX2hpc3RvcnkuYXBwZW5kKGZsb2F0KGxyKSlcbiAgICAgICAgbG9zc19oaXN0b3J5LmFwcGVuZChzbW9vdGhlZF9sb3NzIC8gKDEgLSBiZXRhKiooc3RlcCsxKSkpXG5cbiAgICAjIEZpbmQgc3VnZ2VzdGVkIExSOiB3aGVyZSBsb3NzIHN0YXJ0cyBpbmNyZWFzaW5nXG4gICAgYmVzdF9pZHggPSBucC5hcmdtaW4obG9zc19oaXN0b3J5KVxuICAgIHN1Z2dlc3RlZF9sciA9IGxyX2hpc3RvcnlbbWF4KDAsIGJlc3RfaWR4IC0gNSldICAjIHNsaWdodGx5IGJlZm9yZSBtaW5pbXVtXG4gICAgcHJpbnQoZlwiU3VnZ2VzdGVkIExSOiB7c3VnZ2VzdGVkX2xyOi4yZX1cIilcbiAgICByZXR1cm4gbHJfaGlzdG9yeSwgbG9zc19oaXN0b3J5XG5cbnByaW50KFwiTFIgcmFuZ2UgdGVzdCBmdW5jdGlvbiBkZWZpbmVkIOKAlCBjYWxsIHdpdGggbW9kZWwgKyBkYXRhbG9hZGVyXCIpXG4jIEV4YW1wbGUgdXNlOiBscl9oaXN0LCBsb3NzX2hpc3QgPSBsZWFybmluZ19yYXRlX3JhbmdlX3Rlc3QobW9kZWwsIHRvcmNoLm9wdGltLlNHRCwgbG9hZGVyKSJ9LCB7InR5cGUiOiAiY2FsbG91dCIsICJ0aXRsZSI6ICJMZWFybmluZyBSYXRlIElzIHRoZSBNb3N0IENyaXRpY2FsIEh5cGVycGFyYW1ldGVyIiwgImNvbnRlbnQiOiAiRm9yIGNvbnZleCBMLXNtb290aCBmdW5jdGlvbnMsIGV0YSA+IDIvTCBjYXVzZXMgZGl2ZXJnZW5jZSDigJQgdGhlIGxvc3Mgd2lsbCBpbmNyZWFzZSBtb25vdG9uaWNhbGx5LiBGb3IgbmV1cmFsIG5ldHdvcmtzLCB0aGUgY3JpdGljYWwgTFIgaXMgaGFyZGVyIHRvIGJvdW5kIGJ1dCB0aGUgc3ltcHRvbSBpcyB0aGUgc2FtZTogbG9zcyBzcGlrZXMgYWZ0ZXIgMS0zIHN0ZXBzLiBTZXR0aW5nIGV0YSA9IDEvTCAod2hlcmUgTCBpcyBhcHByb3hpbWF0ZWx5IHRoZSBtYXggSGVzc2lhbiBlaWdlbnZhbHVlKSBndWFyYW50ZWVzIGRlc2NlbnQgYnV0IG1heSBiZSAxMC0xMDB4IHRvbyBjb25zZXJ2YXRpdmUuIFRoZSBwcmFjdGljYWwgc3dlZXQgc3BvdCBpcyBpZGVudGlmaWVkIHZpYSB0aGUgTFIgcmFuZ2UgdGVzdCBvciBncmlkIHNlYXJjaC4gV2l0aCBjb3NpbmUgYW5uZWFsaW5nLCB1c2UgZXRhX21heCBmcm9tIHRoZSByYW5nZSB0ZXN0IGFuZCBkZWNheSB0byBldGFfbWF4LzEwMC4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIkZ1bmN0aW9uIENsYXNzIiwgIkdEIENvbnZlcmdlbmNlIFJhdGUiLCAiU3RlcHMgdG8gZXBzaWxvbiIsICJPcHRpbWFsIGV0YSJdLCAicm93cyI6IFtbIk5vbi1zbW9vdGggY29udmV4IiwgIk8oMS9zcXJ0KFQpKSIsICJPKDEvZXBzaWxvbl4yKSIsICJPKDEvc3FydChUKSkgZGVjcmVhc2luZyJdLCBbIlNtb290aCBjb252ZXggKEwtc21vb3RoKSIsICJPKDEvVCkiLCAiTygxL2Vwc2lsb24pIiwgIjEvTCJdLCBbIlN0cm9uZ2x5IGNvbnZleCArIHNtb290aCIsICJPKHJob15UKSwgcmhvPShrYXBwYS0xKS8oa2FwcGErMSkiLCAiTyhrYXBwYSBsb2coMS9lcHNpbG9uKSkiLCAiMi8obXUrTCkiXSwgWyJQTCBjb25kaXRpb24gKG5vbi1jb252ZXgpIiwgIk8ocmhvXlQpIGxpbmVhciIsICJPKGxvZygxL2Vwc2lsb24pKSIsICIxL0wiXSwgWyJOb24tY29udmV4IChnZW5lcmFsKSIsICJ8fGdyYWQgZih0aGV0YV9UKXx8LT4wIChzdGF0aW9uYXJ5KSIsICJPKDEvZXBzaWxvbl4yKSIsICIxL0wiXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAiaXRlbXMiOiBbIkdEIHVwZGF0ZSB0aGV0YSA8LSB0aGV0YSAtIGV0YSpncmFkKGYpIGlzIHN0ZWVwZXN0IGRlc2NlbnQ7IHRoZSBuZWdhdGl2ZSBncmFkaWVudCBkaXJlY3Rpb24gaXMgdGhlIGxvY2FsbHkgZmFzdGVzdCBwYXRoIGRvd25oaWxsIGJ5IENhdWNoeS1TY2h3YXJ6LiIsICJMLXNtb290aG5lc3MgZ3VhcmFudGVlcyBkZXNjZW50IGZvciBldGEgPD0gMS9MLiBGb3IgY29udmV4IGZ1bmN0aW9uczogTygxL1QpIHJhdGUuIEZvciBtdS1zdHJvbmdseSBjb252ZXg6IGxpbmVhciByYXRlIE8ocmhvXlQpIHdpdGggcmhvPShrYXBwYS0xKS8oa2FwcGErMSkuIiwgIkNvbmRpdGlvbiBudW1iZXIga2FwcGEgPSBML211IGNvbnRyb2xzIGNvbnZlcmdlbmNlIHNwZWVkLiBIaWdoIGthcHBhIG1lYW5zIGVsb25nYXRlZCBsb3NzIGxhbmRzY2FwZSDigJQgR0QgemlnemFncy4gTW9tZW50dW0gYW5kIEFkYW0gaW1wbGljaXRseSBhZGRyZXNzIHRoaXMuIiwgIk5vbi1jb252ZXggZnVuY3Rpb25zIChuZXVyYWwgbmV0d29ya3MpIGhhdmUgc2FkZGxlIHBvaW50cyB3aGVyZSBHRCBjYW4gc3RhbGwuIFRoZSBQb2x5YWstTG9qYXNpZXdpY3ogY29uZGl0aW9uIGVuYWJsZXMgbGluZWFyIGNvbnZlcmdlbmNlIHdpdGhvdXQgY29udmV4aXR5LiIsICJNaW5pLWJhdGNoIFNHRCB3aXRoIHNodWZmbGluZyBpcyB0aGUgcHJhY3RpY2FsIGFsZ29yaXRobS4gQmF0Y2ggc2l6ZSBCIHJlZHVjZXMgdmFyaWFuY2UgYnkgQiBidXQgcmVxdWlyZXMgTFIgc2NhbGluZyAobGluZWFyIHNjYWxpbmcgcnVsZSkuIiwgIlRoZSBncmFkaWVudCBmbG93IE9ERSBkKHRoZXRhKS9kdCA9IC1ncmFkKGYpKHRoZXRhKSBpcyB0aGUgY29udGludW91cyBsaW1pdDsgaXQgZW5hYmxlcyBjbGVhbmVyIGNvbnZlcmdlbmNlIHByb29mcyB0aGF0IHRyYW5zZmVyIHRvIGRpc2NyZXRlIEdEIHZpYSBzdGVwLXNpemUgZGlzY3JldGl6YXRpb24uIiwgIlVzZSB0aGUgTFIgcmFuZ2UgdGVzdCB0byBmaW5kIGV0YV9tYXg7IGFwcGx5IGNvc2luZSBhbm5lYWxpbmcgZnJvbSBldGFfbWF4IHRvIGV0YV9tYXgvMTAwIGFjcm9zcyB0cmFpbmluZy4iXX1d"
---

# Gradient Descent — Convergence Analysis and Step Size

Gradient descent is the backbone of virtually every machine learning optimizer. Yet most practitioners treat it as a black box: subtract the gradient, scale by learning rate, repeat. A rigorous understanding — convergence rates, smoothness conditions, saddle point dynamics, and the relationship between discrete updates and continuous gradient flow — is essential for choosing learning rates correctly, diagnosing training failures, and understanding why more sophisticated optimizers (Adam, Lion) help. This note covers: update rule derivation, L-smooth convergence guarantees, convex vs strongly convex rates, non-convex landscape difficulties, and the gradient flow ODE perspective.

## Core Definition: The Update Rule

The gradient descent update for minimizing f: ℝⁿ → ℝ is θₜ₊₁ = θₜ − η∇f(θₜ), where η > 0 is the learning rate (step size). The negative gradient direction −∇f(θ) is the steepest descent direction (by Cauchy-Schwarz: the direction maximally decreasing f per unit distance). Each step decreases f by approximately η‖∇f‖² (to first order): f(θₜ − η∇f) ≈ f(θ) − η‖∇f‖². The continuous analogue is the gradient flow ODE: dθ/dt = −∇f(θ), which converges to a stationary point as t→∞ under mild conditions. Discrete GD approximates this ODE with step size η as the temporal discretization parameter.

```python
import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(grad_f, x0, lr, n_steps, f=None):
    """Basic gradient descent. Returns trajectory and loss history."""
    x = np.array(x0, dtype=np.float64)
    trajectory = [x.copy()]
    losses = [f(x)] if f else []

    for t in range(n_steps):
        g = grad_f(x)
        x = x - lr * g
        trajectory.append(x.copy())
        if f: losses.append(f(x))

    return np.array(trajectory), losses

# Example: minimize f(x, y) = x^2 + 4y^2 (condition number kappa = 4)
f = lambda x: x[0]**2 + 4*x[1]**2
grad_f = lambda x: np.array([2*x[0], 8*x[1]])

x0 = np.array([3.0, 2.0])

# Three learning rates: optimal eta = 1/L = 1/8, too small, too large
for lr, label in [(0.001, 'too small'), (0.125, 'optimal eta=1/L'), (0.26, 'too large')]:
    traj, losses = gradient_descent(grad_f, x0, lr=lr, n_steps=200, f=f)
    if losses:
        final = losses[-1]
        print(f"lr={lr} ({label}): final loss={final:.6f} after 200 steps")
    else:
        print(f"lr={lr} ({label}): diverged")

# Exact convergence rate for strongly convex: f(theta_T) - f* <= (1 - 2*eta*mu*L/(mu+L))^T * (f(theta_0) - f*)
# For f(x,y) = x^2 + 4y^2: mu = 2 (min eigenvalue of Hessian), L = 8 (max eigenvalue)
mu, L = 2.0, 8.0
eta_opt = 2 / (mu + L)  # Optimal step for strongly convex: 2/(mu+L)
rho = (L - mu) / (L + mu)  # Convergence rate
print(f"\nOptimal eta for strongly convex: {eta_opt:.4f}, rho = {rho:.4f}")
print(f"Steps to 1e-6 precision: {int(np.log(1e-6) / np.log(rho)) + 1}")
```

## L-Smoothness and Convergence Guarantees

A function f is L-smooth (L-Lipschitz gradient) if ‖∇f(x) − ∇f(y)‖ ≤ L‖x−y‖ for all x,y. Equivalently: f(y) ≤ f(x) + ∇f(x)ᵀ(y−x) + L/2‖y−x‖² (the gradient descent lemma). This quadratic upper bound guarantees that a step η = 1/L always decreases f: f(θ−η∇f) ≤ f(θ) − (1/2L)‖∇f(θ)‖². For convex L-smooth f: gradient descent with η ≤ 1/L achieves f(θₜ) − f* ≤ ‖θ₀−θ*‖²/(2ηT) — rate O(1/T). For μ-strongly convex L-smooth f: f(θₜ) − f* ≤ (1−2ημL/(μ+L))ᵀ(f(θ₀)−f*) — linear rate O(ρᵀ) where ρ = (κ−1)/(κ+1) < 1, κ = L/μ. Strong convexity provides the pull toward minimum that enables linear convergence.

```python
import numpy as np

def verify_l_smoothness(f, grad_f, x, y, L_candidate):
    """Check if L-smoothness inequality holds at x, y."""
    lhs = f(y)
    rhs = f(x) + grad_f(x) @ (y - x) + L_candidate/2 * np.linalg.norm(y-x)**2
    return lhs <= rhs + 1e-10, lhs, rhs

def convergence_rate_analysis(f, grad_f, x0, f_star, mu, L, n_steps=500):
    """
    Analyze convergence rate for L-smooth strongly convex function.
    Expected: linear rate rho = (L-mu)/(L+mu).
    """
    eta = 2.0 / (mu + L)  # Optimal step size for strongly convex
    x = x0.copy()
    gaps = []

    for t in range(n_steps):
        gap = f(x) - f_star
        gaps.append(gap)
        if gap < 1e-12: break
        x = x - eta * grad_f(x)

    # Fit empirical convergence rate
    rho_theory = (L - mu) / (L + mu)
    rho_empirical = (gaps[-1] / gaps[0]) ** (1 / len(gaps))

    return np.array(gaps), rho_theory, rho_empirical

# f(x) = x^T A x / 2  where A = diag(2, 4, 6, 8)  (strongly convex, L-smooth)
A = np.diag([2.0, 4.0, 6.0, 8.0])
f = lambda x: 0.5 * x @ A @ x
grad_f = lambda x: A @ x
x0 = np.array([3.0, 2.0, 1.0, 0.5])
f_star = 0.0  # minimum at origin
mu, L = 2.0, 8.0  # min and max eigenvalues of A

gaps, rho_th, rho_emp = convergence_rate_analysis(f, grad_f, x0, f_star, mu, L)
print(f"Theoretical rate rho = {rho_th:.4f}")
print(f"Empirical rate rho = {rho_emp:.4f}")
print(f"Steps to 1e-6: theoretical {int(np.log(1e-6) / np.log(rho_th))+1}, actual {len(gaps)}")

# Verify L-smoothness
x_test = np.array([1.0, 1.0, 1.0, 1.0])
y_test = x_test + 0.1 * np.random.randn(4)
ok, lhs, rhs = verify_l_smoothness(f, grad_f, x_test, y_test, L)
print(f"\nL-smoothness check: {ok}  (lhs={lhs:.4f} <= rhs={rhs:.4f})")
```

## Non-Convex Landscapes: Saddle Points and Local Minima

For non-convex f (all neural networks), GD is not guaranteed to find the global minimum. Two obstacles arise: (1) Local minima — GD converges to a local stationary point ∇f(θ*)=0. However, for over-parameterized networks, recent theory (e.g., NTK regime) suggests that local minima are often near-global. (2) Saddle points — critical points where some Hessian eigenvalues are negative (directions of decrease exist). In high dimensions, saddle points are exponentially more common than local minima (Bhojanapalli et al.). The Polyak-Łojasiewicz (PL) condition provides non-convex convergence: if ‖∇f‖² ≥ 2μ(f−f*), then GD converges linearly even without convexity. Over-parameterized neural networks often satisfy PL empirically, which helps explain why GD finds good solutions despite the non-convex landscape.

## ML Connections: Batch GD vs Mini-Batch vs SGD

Full-batch GD computes the gradient over the entire dataset. For n samples and d parameters: cost O(nd) per step. Mini-batch GD uses a random subset B of size B: gradient estimate ĝ = (1/B)Σ_{i∈B}∇Lᵢ(θ). This is an unbiased estimate of the true gradient: E[ĝ] = ∇L. Variance: Var[ĝ] ≈ σ²/B where σ² is the per-sample gradient variance. SGD (B=1) has highest variance but best parallelism and implicit regularization. Minibatch SGD with B=256–4096 is the practical sweet spot: enough noise for generalization, enough signal for stable convergence. The linear scaling rule (Goyal et al. 2017): multiply LR by B/256 when scaling batch size — this preserves gradient noise statistics and keeps the effective update magnitude constant across different hardware configurations.

```python
import numpy as np

def minibatch_sgd(loss_fn, grad_fn, theta0, X, y, lr, batch_size, n_epochs):
    """
    Minibatch SGD with data shuffling per epoch.
    Returns: final theta, per-epoch average loss.
    """
    theta = theta0.copy()
    n = len(X)
    epoch_losses = []

    for epoch in range(n_epochs):
        # Shuffle data each epoch (critical for convergence)
        idx = np.random.permutation(n)
        X_shuf, y_shuf = X[idx], y[idx]

        batch_losses = []
        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            Xb = X_shuf[start:end]
            yb = y_shuf[start:end]

            g = grad_fn(theta, Xb, yb)
            theta = theta - lr * g
            batch_losses.append(loss_fn(theta, Xb, yb))

        epoch_losses.append(np.mean(batch_losses))

    return theta, epoch_losses

# Linear regression: L(w) = ||Xw - y||^2 / n
np.random.seed(0)
n, d = 1000, 20
X = np.random.randn(n, d)
w_true = np.random.randn(d)
y = X @ w_true + 0.1 * np.random.randn(n)

loss_fn = lambda w, X, y: np.mean((X @ w - y)**2)
grad_fn = lambda w, X, y: 2 * X.T @ (X @ w - y) / len(y)

# Compare batch sizes
for bs in [1, 32, 256, n]:
    w0 = np.zeros(d)
    n_epochs = 20 if bs < n else 200
    lr = 0.01
    w_final, losses = minibatch_sgd(loss_fn, grad_fn, w0, X, y, lr, bs, n_epochs)
    final_loss = loss_fn(w_final, X, y)
    print(f"B={bs:4d}: final_loss={final_loss:.4f}, w_error={np.linalg.norm(w_final - w_true):.4f}")
```

## Gradient Flow: The Continuous-Time Perspective

The gradient flow ODE dθ/dt = −∇f(θ) is the continuous-time limit of gradient descent as η→0. Solutions θ(t) satisfy f(θ(t)) decreasing monotonically. For convex f, gradient flow converges as f(θ(t)) − f* ≤ ‖θ(0)−θ*‖²/(2t). For strongly convex: f(θ(t)) − f* ≤ e^{−2μt}(f(θ(0))−f*). Gradient descent with step η approximates gradient flow with t = ηT. The gradient flow perspective enables: (1) continuous convergence proofs that transfer cleanly to discrete updates; (2) analysis of momentum as a second-order ODE (heavy ball: θ'' + γθ' + ∇f(θ) = 0); (3) stochastic gradient flow (Langevin dynamics: dθ = −∇f·dt + √(2T)dW) as a principled model for SGD’s inherent noise in finite-batch training regimes.

## Implementation Pitfalls

Learning rate too large: GD diverges when η > 2/L (the step exceeds the curvature bound and oscillates). Symptom: loss increases after a few steps or oscillates wildly. Fix: check L via power iteration on the Hessian, set η ≤ 1/L. Learning rate too small: convergence is guaranteed but glacially slow — especially problematic with high condition number κ, where O(κ) steps are needed per digit of precision. Symptom: loss decreases steadily but very slowly. Forgetting to shuffle data: cyclic gradient estimates can have systematic bias and slow convergence significantly. Diagnosis: compare cyclic vs shuffled on a simple problem. Not normalizing features: creates ill-conditioned loss landscape where κ ≈ (max feature scale/min feature scale)² — gradient descent zigzags rather than converging directly.

## Practical Guidance

Set initial LR via the learning rate range test: increase LR from 1e-7 to 10 over 100 steps, plot loss vs LR, pick the LR just before the loss starts to increase. For convex problems with known L, set η = 1/L exactly. For neural networks, start at η = 1e-3 (Adam) or η = 0.1 (SGD with momentum). Use cosine annealing from η_max to η_min = η_max/100 over training. Monitor gradient norm ‖∇L‖: should decrease over training for convex objectives. Sudden spikes in gradient norm indicate instability — reduce LR or add gradient clipping. Feature normalization (zero mean, unit variance) is critical: it transforms the loss landscape from highly anisotropic to approximately isotropic, reducing the effective condition number and enabling larger safe learning rates.

```python
import numpy as np
import torch

def learning_rate_range_test(model, optimizer_cls, train_loader,
                              start_lr=1e-7, end_lr=10.0, n_steps=100):
    """
    LR range test (Smith 2015): increase LR geometrically, find sweet spot.
    Returns lr_history, loss_history for plotting.
    """
    # Build LR schedule: geometric increase
    lr_schedule = np.geomspace(start_lr, end_lr, n_steps)
    optimizer = optimizer_cls(model.parameters(), lr=start_lr)

    lr_history = []
    loss_history = []
    smoothed_loss = None
    beta = 0.9  # EMA smoothing

    for step, (lr, batch) in enumerate(zip(lr_schedule, train_loader)):
        # Update LR
        for pg in optimizer.param_groups:
            pg['lr'] = float(lr)

        X, y = batch
        optimizer.zero_grad()
        loss = torch.nn.functional.mse_loss(model(X), y)
        loss.backward()
        optimizer.step()

        raw = loss.item()
        smoothed_loss = beta * (smoothed_loss or raw) + (1 - beta) * raw
        lr_history.append(float(lr))
        loss_history.append(smoothed_loss / (1 - beta**(step+1)))

    # Find suggested LR: where loss starts increasing
    best_idx = np.argmin(loss_history)
    suggested_lr = lr_history[max(0, best_idx - 5)]  # slightly before minimum
    print(f"Suggested LR: {suggested_lr:.2e}")
    return lr_history, loss_history

print("LR range test function defined — call with model + dataloader")
# Example use: lr_hist, loss_hist = learning_rate_range_test(model, torch.optim.SGD, loader)
```

> **Learning Rate Is the Most Critical Hyperparameter**: For convex L-smooth functions, eta > 2/L causes divergence — the loss will increase monotonically. For neural networks, the critical LR is harder to bound but the symptom is the same: loss spikes after 1-3 steps. Setting eta = 1/L (where L is approximately the max Hessian eigenvalue) guarantees descent but may be 10-100x too conservative. The practical sweet spot is identified via the LR range test or grid search. With cosine annealing, use eta_max from the range test and decay to eta_max/100.

| Function Class | GD Convergence Rate | Steps to epsilon | Optimal eta |
|---|---|---|---|
| Non-smooth convex | O(1/sqrt(T)) | O(1/epsilon^2) | O(1/sqrt(T)) decreasing |
| Smooth convex (L-smooth) | O(1/T) | O(1/epsilon) | 1/L |
| Strongly convex + smooth | O(rho^T), rho=(kappa-1)/(kappa+1) | O(kappa log(1/epsilon)) | 2/(mu+L) |
| PL condition (non-convex) | O(rho^T) linear | O(log(1/epsilon)) | 1/L |
| Non-convex (general) | ||grad f(theta_T)||->0 (stationary) | O(1/epsilon^2) | 1/L |

---

## Key Takeaways

- GD update theta <- theta - eta*grad(f) is steepest descent; the negative gradient direction is the locally fastest path downhill by Cauchy-Schwarz.
- L-smoothness guarantees descent for eta <= 1/L. For convex functions: O(1/T) rate. For mu-strongly convex: linear rate O(rho^T) with rho=(kappa-1)/(kappa+1).
- Condition number kappa = L/mu controls convergence speed. High kappa means elongated loss landscape — GD zigzags. Momentum and Adam implicitly address this.
- Non-convex functions (neural networks) have saddle points where GD can stall. The Polyak-Lojasiewicz condition enables linear convergence without convexity.
- Mini-batch SGD with shuffling is the practical algorithm. Batch size B reduces variance by B but requires LR scaling (linear scaling rule).
- The gradient flow ODE d(theta)/dt = -grad(f)(theta) is the continuous limit; it enables cleaner convergence proofs that transfer to discrete GD via step-size discretization.
- Use the LR range test to find eta_max; apply cosine annealing from eta_max to eta_max/100 across training.

