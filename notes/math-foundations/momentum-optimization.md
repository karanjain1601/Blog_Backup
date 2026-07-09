---
title: "Momentum and Exponential Moving Averages"
slug: "momentum-optimization"
description: "Deep dive into heavy ball momentum, exponential moving averages as low-pass filters, accelerated convergence on convex problems, EMA target networks in RL, and stochastic weight averaging for improved generalization."
tags: ["optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTW9tZW50dW0gaXMgdGhlIHNpbmdsZSBtb3N0IGltcGFjdGZ1bCBtb2RpZmljYXRpb24gdG8gYmFzaWMgZ3JhZGllbnQgZGVzY2VudCwgcHJvdmlkaW5nIE8oMS9UwrIpIGNvbnZlcmdlbmNlIGZvciBjb252ZXggc21vb3RoIGZ1bmN0aW9ucyB2cyBPKDEvVCkgZm9yIHZhbmlsbGEgR0QuIEJ1dCBtb21lbnR1bSBpcyBtb3JlIHRoYW4gYW4gYWNjZWxlcmF0aW9uIHRlY2huaXF1ZSDigJQgaXRzIHVuZGVybHlpbmcgbWVjaGFuaXNtIChleHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZSBvZiBncmFkaWVudHMpIGlzIHRoZSBjb3JlIHByaW1pdGl2ZSBpbiBBZGFtJ3MgZmlyc3QgbW9tZW50LCBFTUEgdGFyZ2V0IG5ldHdvcmtzIGluIGRlZXAgUkwgKERRTiwgQllPTCksIG1vZGVsIHdlaWdodCBhdmVyYWdpbmcgKFNXQSwgRU1BIGVuc2VtYmxlcyksIGFuZCB0ZW1wb3JhbCBkaWZmZXJlbmNlIGJvb3RzdHJhcHBpbmcuIFVuZGVyc3RhbmRpbmcgbW9tZW50dW0gdGhyb3VnaCB0aGUgbGVucyBvZiBleHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZXMsIGVmZmVjdGl2ZSBzdGVwIHNpemUsIG9zY2lsbGF0aW9uIGRhbXBpbmcsIGFuZCB0aGUgcGh5c2ljYWwgYmFsbC1vbi1zbG9wZSBhbmFsb2d5IHVuaWZpZXMgdGhlc2Ugc2VlbWluZ2x5IGRpc3BhcmF0ZSBhcHBsaWNhdGlvbnMgdW5kZXIgYSBzaW5nbGUgbWF0aGVtYXRpY2FsIGZyYW1ld29yayBhcHBsaWNhYmxlIGFjcm9zcyBvcHRpbWl6YXRpb24sIHJlaW5mb3JjZW1lbnQgbGVhcm5pbmcsIGFuZCBnZW5lcmF0aXZlIG1vZGVsaW5nLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkNvcmUgRGVmaW5pdGlvbjogSGVhdnkgQmFsbCBNZXRob2QifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgaGVhdnkgYmFsbCBtb21lbnR1bSB1cGRhdGUgKFBvbHlhayAxOTY0KTogduKCnCA9IM6yduKCnOKCi+KCgSArIM63Z+KCnDsgzrjigpwgPSDOuOKCnOKCi+KCgSDiiJIgduKCnCwgd2hlcmUgZ+KCnCA9IOKIh0wozrjigpzigovigoEpLCDOsiDiiIggWzAsMSkgaXMgdGhlIG1vbWVudHVtIGNvZWZmaWNpZW50LCDOtyBpcyB0aGUgbGVhcm5pbmcgcmF0ZSwgYW5kIHbigpwgaXMgdGhlIHZlbG9jaXR5IHZlY3Rvci4gRXF1aXZhbGVudGx5OiDOuOKCnCA9IM644oKc4oKL4oKBIOKIkiDOt2figpwg4oiSIM6yKM644oKc4oKL4oKBIOKIkiDOuOKCnOKCi+KCgikuIEdlb21ldHJpYyBzZXJpZXMgaW50ZXJwcmV0YXRpb246IHbigpwgPSDOt86j4oKW4oKM4oKAXuKIniDOsuG1jyBn4oKc4oKL4oKWIOKAlCB2ZWxvY2l0eSBpcyBhbiBleHBvbmVudGlhbGx5IGRlY2F5aW5nIHdlaWdodGVkIGF2ZXJhZ2Ugb2YgYWxsIHBhc3QgZ3JhZGllbnRzLiBJbiBjb25zaXN0ZW50IGdyYWRpZW50IGRpcmVjdGlvbnMsIGdyYWRpZW50cyByZWluZm9yY2U6IHbigpwg4oaSIM63Lygx4oiSzrIpIMK3IGcgKHN0ZWFkeS1zdGF0ZSB2ZWxvY2l0eSkuIEluIG9zY2lsbGF0aW5nIGRpcmVjdGlvbnMsIHRoZXkgY2FuY2VsOiBtb21lbnR1bSBkYW1wcyBvc2NpbGxhdGlvbnMgYWNyb3NzIHRoZSB2YWxsZXkuIEVmZmVjdGl2ZSBzdGVwIHNpemUgaW4gYSBjb25zaXN0ZW50IGRpcmVjdGlvbjogzrcvKDHiiJLOsikuIEZvciDOsj0wLjkgdGhpcyBpcyAxMMOXIGFtcGxpZmljYXRpb247IGZvciDOsj0wLjk5IGl0IGdpdmVzIDEwMMOXIGFtcGxpZmljYXRpb24uIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgc2dkX21vbWVudHVtKGdyYWRfZiwgdGhldGEwLCBsciwgYmV0YSwgbl9zdGVwcywgZj1Ob25lKTpcbiAgICBcIlwiXCJcbiAgICBTR0Qgd2l0aCBoZWF2eSBiYWxsIG1vbWVudHVtLlxuICAgIHZ0ID0gYmV0YSAqIHZfe3QtMX0gKyBsciAqIGdyYWQodGhldGFfe3QtMX0pXG4gICAgdGhldGFfdCA9IHRoZXRhX3t0LTF9IC0gdnRcbiAgICBcIlwiXCJcbiAgICB0aGV0YSA9IG5wLmFycmF5KHRoZXRhMCwgZHR5cGU9bnAuZmxvYXQ2NClcbiAgICB2ID0gbnAuemVyb3NfbGlrZSh0aGV0YSlcbiAgICBoaXN0b3J5ID0geyd0aGV0YSc6IFt0aGV0YS5jb3B5KCldLCAnbG9zcyc6IFtmKHRoZXRhKV0gaWYgZiBlbHNlIFtdfVxuXG4gICAgZm9yIHQgaW4gcmFuZ2Uobl9zdGVwcyk6XG4gICAgICAgIGcgPSBncmFkX2YodGhldGEpXG4gICAgICAgIHYgPSBiZXRhICogdiArIGxyICogZyAgICAgICAjIHZlbG9jaXR5IGFjY3VtdWxhdGVzXG4gICAgICAgIHRoZXRhID0gdGhldGEgLSB2XG4gICAgICAgIGhpc3RvcnlbJ3RoZXRhJ10uYXBwZW5kKHRoZXRhLmNvcHkoKSlcbiAgICAgICAgaWYgZjogaGlzdG9yeVsnbG9zcyddLmFwcGVuZChmKHRoZXRhKSlcblxuICAgIHJldHVybiBoaXN0b3J5XG5cbiMgQ29tcGFyZSB2YW5pbGxhIEdEIHZzIG1vbWVudHVtIG9uIGlsbC1jb25kaXRpb25lZCBxdWFkcmF0aWNcbiMgZih4LHkpID0gMC41Kih4XjIgKyAxMDAqeV4yKSAgLS0gY29uZGl0aW9uIG51bWJlciBrYXBwYT0xMDBcbmYgPSBsYW1iZGEgeDogMC41ICogKHhbMF0qKjIgKyAxMDAqeFsxXSoqMilcbmdyYWRfZiA9IGxhbWJkYSB4OiBucC5hcnJheShbeFswXSwgMTAwKnhbMV1dKVxueDAgPSBucC5hcnJheShbMTAuMCwgMS4wXSlcblxuTCwgbXUgPSAxMDAuMCwgMS4wXG5ldGFfZ2QgPSAyLyhtdSArIEwpICAgICAgICMgb3B0aW1hbCBmb3IgR0RcbmV0YV9tb20gPSAyLyhucC5zcXJ0KG11KSArIG5wLnNxcnQoTCkpKioyICAjIG9wdGltYWwgZm9yIG1vbWVudHVtXG5iZXRhX21vbSA9ICgobnAuc3FydChMKSAtIG5wLnNxcnQobXUpKS8obnAuc3FydChMKSArIG5wLnNxcnQobXUpKSkqKjJcblxuaGlzdF9nZCA9IHNnZF9tb21lbnR1bShncmFkX2YsIHgwLCBscj1ldGFfZ2QsIGJldGE9MCwgbl9zdGVwcz0zMDAsIGY9Zilcbmhpc3RfbW9tID0gc2dkX21vbWVudHVtKGdyYWRfZiwgeDAsIGxyPWV0YV9tb20sIGJldGE9YmV0YV9tb20sIG5fc3RlcHM9MzAwLCBmPWYpXG5cbiMgRmluZCBzdGVwcyB0byByZWFjaCAxZS00IHByZWNpc2lvblxuc3RlcHNfZ2QgPSBuZXh0KChpIGZvciBpLCBsIGluIGVudW1lcmF0ZShoaXN0X2dkWydsb3NzJ10pIGlmIGwgPCAxZS00KSwgMzAwKVxuc3RlcHNfbW9tID0gbmV4dCgoaSBmb3IgaSwgbCBpbiBlbnVtZXJhdGUoaGlzdF9tb21bJ2xvc3MnXSkgaWYgbCA8IDFlLTQpLCAzMDApXG5wcmludChmXCJHRDogICAgICAge3N0ZXBzX2dkfSBzdGVwcyB0byAxZS00ICAoa2FwcGE9e0wvbXU6LjBmfSlcIilcbnByaW50KGZcIk1vbWVudHVtOiB7c3RlcHNfbW9tfSBzdGVwcyB0byAxZS00ICAoc3BlZWR1cDoge3N0ZXBzX2dkL21heChzdGVwc19tb20sMSk6LjFmfXgpXCIpXG5wcmludChmXCJFZmZlY3RpdmUgbW9tZW50dW0gc3RlcCBzaXplOiBldGEvKDEtYmV0YSkgPSB7ZXRhX21vbS8oMS1iZXRhX21vbSk6LjRmfVwiKVxucHJpbnQoZlwiTW9tZW50dW0gY29lZmZpY2llbnQgYmV0YSA9IHtiZXRhX21vbTouNGZ9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiRXhwb25lbnRpYWwgTW92aW5nIEF2ZXJhZ2UgYXMgTG93LVBhc3MgRmlsdGVyIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIEVNQSBt4oKcID0gzrJt4oKc4oKL4oKBICsgKDHiiJLOsil44oKcIGlzIGEgcmVjdXJzaXZlIGZvcm11bGEgd2l0aCBleHBsaWNpdCBzb2x1dGlvbiBt4oKcID0gKDHiiJLOsinOo+KCluKCjOKCgF50IM6y4bWPIHhfe3Qta30uIFRoZSB3ZWlnaHRzICgx4oiSzrIpzrLhtY8gc3VtIHRvIDEgKGdlb21ldHJpYyBzZXJpZXMpIGFuZCBkZWNheSBleHBvbmVudGlhbGx5IOKAlCByZWNlbnQgdmFsdWVzIGRvbWluYXRlLiBFZmZlY3RpdmUgd2luZG93OiDPhCA9IDEvKDHiiJLOsikuIEZvciDOsj0wLjk6IHdpbmRvd+KJiDEwIHN0ZXBzOyDOsj0wLjk5OiB3aW5kb3fiiYgxMDAgc3RlcHM7IM6yPTAuOTk5OiB3aW5kb3fiiYgxMDAwIHN0ZXBzLiBJbiBmcmVxdWVuY3kgZG9tYWluOiBFTUEgaXMgYSBmaXJzdC1vcmRlciBJSVIgbG93LXBhc3MgZmlsdGVyLCBwYXNzaW5nIGxvdy1mcmVxdWVuY3kgKHNsb3cgdHJlbmQpIHNpZ25hbHMgYW5kIGF0dGVudWF0aW5nIGhpZ2gtZnJlcXVlbmN5IChub2lzZSkgc2lnbmFscy4gVGhlIGN1dG9mZiBmcmVxdWVuY3kgaXMgYXBwcm94aW1hdGVseSAoMeKIks6yKS8oMs+AKS4gSGVhdnkgYmFsbCBtb21lbnR1bSB1c2VzIEVNQSBvZiBncmFkaWVudHM6IM6yPTAuOSBzbW9vdGhzIGdyYWRpZW50IG5vaXNlIHdoaWxlIHByZXNlcnZpbmcgdGhlIHRyZW5kIGRpcmVjdGlvbiwgZW5hYmxpbmcgbGFyZ2VyIGVmZmVjdGl2ZSBzdGVwIHNpemVzIHRoYW4gdmFuaWxsYSBHRCB3aXRob3V0IHRoZSBpbnN0YWJpbGl0eSB0aGF0IHdvdWxkIGFyaXNlIGZyb20gc2ltcGx5IHVzaW5nIGEgbGFyZ2VyIGxlYXJuaW5nIHJhdGUgZGlyZWN0bHkuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZW1hKHZhbHVlcywgYmV0YT0wLjksIGJpYXNfY29ycmVjdD1UcnVlKTpcbiAgICBcIlwiXCJcbiAgICBFeHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZS5cbiAgICBtX3QgPSBiZXRhICogbV97dC0xfSArICgxIC0gYmV0YSkgKiB4X3RcbiAgICBXaXRoIGJpYXMgY29ycmVjdGlvbjogbV9oYXRfdCA9IG1fdCAvICgxIC0gYmV0YV50KVxuICAgIFwiXCJcIlxuICAgIG0gPSAwLjBcbiAgICBlbWFzID0gW11cbiAgICBmb3IgdCwgeCBpbiBlbnVtZXJhdGUodmFsdWVzLCBzdGFydD0xKTpcbiAgICAgICAgbSA9IGJldGEgKiBtICsgKDEgLSBiZXRhKSAqIHhcbiAgICAgICAgaWYgYmlhc19jb3JyZWN0OlxuICAgICAgICAgICAgbV9oYXQgPSBtIC8gKDEgLSBiZXRhKip0KVxuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgbV9oYXQgPSBtXG4gICAgICAgIGVtYXMuYXBwZW5kKG1faGF0KVxuICAgIHJldHVybiBlbWFzXG5cbiMgRGVtb25zdHJhdGUgZWZmZWN0aXZlIHdpbmRvdyBzaXplXG5iZXRhID0gMC45XG5lZmZlY3RpdmVfd2luZG93ID0gMSAvICgxIC0gYmV0YSlcbnByaW50KGZcImJldGE9e2JldGF9OiBlZmZlY3RpdmUgd2luZG93IGFwcHJveCB7ZWZmZWN0aXZlX3dpbmRvdzouMGZ9IHN0ZXBzXCIpXG5cbiMgU2hvdyBFTUEgdHJhY2tpbmcgYSBzdGVwIGZ1bmN0aW9uXG5uID0gMjAwXG5zaWduYWwgPSBucC5jb25jYXRlbmF0ZShbbnAuemVyb3MoMTAwKSwgbnAub25lcygxMDApXSkgICMgc3RlcCBhdCB0PTEwMFxuZW1hXzkwID0gZW1hKHNpZ25hbCwgYmV0YT0wLjkpXG5lbWFfOTkgPSBlbWEoc2lnbmFsLCBiZXRhPTAuOTkpXG5cbiMgRmluZCB0cmFja2luZyBsYWc6IHN0ZXBzIHRvIHJlYWNoIDYzJSBvZiBzdGVwIHZhbHVlIGFmdGVyIHRoZSBzdGVwXG5sYWdfOTAgPSBuZXh0KCh0IGZvciB0LCB2IGluIGVudW1lcmF0ZShlbWFfOTBbMTAwOl0pIGlmIHYgPiAwLjYzKSwgTm9uZSkgKyAxXG5sYWdfOTkgPSBuZXh0KCh0IGZvciB0LCB2IGluIGVudW1lcmF0ZShlbWFfOTlbMTAwOl0pIGlmIHYgPiAwLjYzKSwgTm9uZSkgKyAxXG5wcmludChmXCJiZXRhPTAuOTogIGxhZyB0byA2MyUgb2Ygc3RlcCA9IHtsYWdfOTB9IHN0ZXBzICAoYXBwcm94IDEvKDEtYmV0YSk9ezEvKDEtMC45KTouMGZ9KVwiKVxucHJpbnQoZlwiYmV0YT0wLjk5OiBsYWcgdG8gNjMlIG9mIHN0ZXAgPSB7bGFnXzk5fSBzdGVwcyAgKGFwcHJveCAxLygxLWJldGEpPXsxLygxLTAuOTkpOi4wZn0pXCIpXG5cbiMgQmlhcyBjb3JyZWN0aW9uIGltcG9ydGFuY2UgZm9yIGVhcmx5IHN0ZXBzXG5lYXJseV9lbWFfbm9fYmMgPSBlbWEoWzEuMF0qMjAsIGJldGE9MC45LCBiaWFzX2NvcnJlY3Q9RmFsc2UpXG5lYXJseV9lbWFfYmMgPSBlbWEoWzEuMF0qMjAsIGJldGE9MC45LCBiaWFzX2NvcnJlY3Q9VHJ1ZSlcbnByaW50KGZcIlxcbkFmdGVyIDEgc3RlcCB3aXRoIGNvbnN0YW50IGlucHV0PTE6IG5vLUJDPXtlYXJseV9lbWFfbm9fYmNbMF06LjNmfSB2cyBCQz17ZWFybHlfZW1hX2JjWzBdOi4zZn1cIilcbnByaW50KGZcIkFmdGVyIDEwIHN0ZXBzOiBuby1CQz17ZWFybHlfZW1hX25vX2JjWzldOi4zZn0gdnMgQkM9e2Vhcmx5X2VtYV9iY1s5XTouM2Z9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQWNjZWxlcmF0ZWQgQ29udmVyZ2VuY2U6IE1vbWVudHVtIEFjaGlldmVzIE8oMS9UwrIpIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTmVzdGVyb3YncyBhY2NlbGVyYXRpb24gdGhlb3JlbTogZm9yIEwtc21vb3RoIGNvbnZleCBmLCBHRCB3aXRoIG1vbWVudHVtIGFjaGlldmVzIGYozrjigpwp4oiSZiog4omkIE8oTOKAls644oKA4oiSzrgq4oCWwrIvVMKyKSwgY29tcGFyZWQgdG8gTyhM4oCWzrjigoDiiJLOuCrigJbCsi9UKSBmb3IgdmFuaWxsYSBHRCDigJQgYSBmYWN0b3Igb2YgVCBzcGVlZHVwLiBGb3Igc3Ryb25nbHkgY29udmV4IGZ1bmN0aW9uczogbW9tZW50dW0gYWNoaWV2ZXMgTyhleHAo4oiSVOKImijOvC9MKSkpIGNvbnZlcmdlbmNlIHZzIE8oZXhwKOKIklTCt868L0wpKSBmb3IgR0Qg4oCUIGxpbmVhciByYXRlIGJ1dCB3aXRoIOKIms66IGluc3RlYWQgb2YgzrogZGVwZW5kZW5jZS4gT3B0aW1hbCBtb21lbnR1bSBjb2VmZmljaWVudCBmb3IgY29udmV4IHNtb290aCBwcm9ibGVtczogzrIgPSAo4oiazrriiJIxKS8o4oiazrorMSkgd2hlcmUgzrogPSBML868LiBQaHlzaWNhbCBpbnR1aXRpb246IHRoZSBiYWxsIHBpY2tzIHVwIHNwZWVkIGRvd25oaWxsIChtb21lbnR1bSBhY2N1bXVsYXRlcykgYW5kIHVzZXMgaW5lcnRpYSB0byBjcm9zcyBzbWFsbCBiYXJyaWVycyBhbmQgbWFpbnRhaW4gZm9yd2FyZCBwcm9ncmVzcy4gVGhlIGRlY2VsZXJhdGlvbiBuZWFyIHRoZSBtaW5pbXVtIHByZXZlbnRzIG92ZXJzaG9vdDogbmVhciDOuCosIHRoZSBncmFkaWVudCByZXZlcnNlcyBkaXJlY3Rpb24sIGFwcGx5aW5nIGEgYnJha2luZyBmb3JjZSB0aGF0IG9wcG9zZXMgdGhlIGFjY3VtdWxhdGVkIG1vbWVudHVtIGFuZCBhbGxvd3MgdGhlIG9wdGltaXplciB0byBzZXR0bGUuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTUwgQ29ubmVjdGlvbnM6IEVNQSBpbiBEZWVwIExlYXJuaW5nIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiRU1BIGFwcGVhcnMgaW4gbXVsdGlwbGUgY3JpdGljYWwgTUwgY29tcG9uZW50cyBiZXlvbmQgb3B0aW1pemF0aW9uOiAoMSkgQWRhbSdzIGZpcnN0IG1vbWVudDogbeKCnCA9IM6y4oKBbeKCnOKCi+KCgSArICgx4oiSzrLigoEpZ+KCnCAoRU1BIG9mIGdyYWRpZW50cyB3aXRoIM6y4oKBPTAuOSkuICgyKSBEUU4gdGFyZ2V0IG5ldHdvcms6IM644oG7ID0gzrLCt8644oG7ICsgKDHiiJLOsinCt864IOKAlCBzbG93LW1vdmluZyBjb3B5IG9mIFEtbmV0d29yayBmb3Igc3RhYmxlIEJlbGxtYW4gdGFyZ2V0cyAoTW5paCAyMDE1KS4gKDMpIEJZT0wgKEdyaWxsIDIwMjApOiBvbmxpbmUgZW5jb2RlciDOuCB1cGRhdGVkIGJ5IGdyYWRpZW50OyB0YXJnZXQgZW5jb2RlciDOviA9IM+EwrfOviArICgx4oiSz4QpwrfOuCAobW9tZW50dW0gZW5jb2RlciksIGVuYWJsaW5nIHNlbGYtc3VwZXJ2aXNlZCBsZWFybmluZyB3aXRob3V0IG5lZ2F0aXZlIHNhbXBsZXMuICg0KSBTdG9jaGFzdGljIFdlaWdodCBBdmVyYWdpbmcgKFNXQSwgSXptYWlsb3YgMjAxOCk6IM64X1NXQSA9ICgxL24pzqPOuOKCnCAodW5pZm9ybSBhdmVyYWdlIG9mIFNHRCBpdGVyYXRlcyksIGNvbnZlcmdlcyB0byBmbGF0IG1pbmltYSBhbmQgaW1wcm92ZXMgZ2VuZXJhbGl6YXRpb24uICg1KSBFTUEgZW5zZW1ibGVzIGluIGRpZmZ1c2lvbiBtb2RlbHM6IGEgc2xvdy1tb3ZpbmcgY29weSBvZiBtb2RlbCB3ZWlnaHRzIGlzIHVzZWQgZm9yIGluZmVyZW5jZSwgeWllbGRpbmcgYmV0dGVyIHNhbXBsZSBxdWFsaXR5IHRoYW4gdGhlIGN1cnJlbnQgdHJhaW5pbmcgY2hlY2twb2ludCBkdWUgdG8gcmVkdWNlZCBub2lzZSBzZW5zaXRpdml0eS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBjb3B5XG5cbmNsYXNzIEVNQU1vZGVsOlxuICAgIFwiXCJcIlxuICAgIEV4cG9uZW50aWFsIE1vdmluZyBBdmVyYWdlIG9mIG1vZGVsIHdlaWdodHMuXG4gICAgVXNlZCBpbjogQllPTCB0YXJnZXQgbmV0d29yaywgZGlmZnVzaW9uIG1vZGVsIGluZmVyZW5jZSwgU1dBLlxuICAgIFwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBtb2RlbCwgZGVjYXk9MC45OTkpOlxuICAgICAgICBzZWxmLmRlY2F5ID0gZGVjYXlcbiAgICAgICAgc2VsZi5zaGFkb3cgPSBjb3B5LmRlZXBjb3B5KG1vZGVsKVxuICAgICAgICAjIEZyZWV6ZSBzaGFkb3cgLS0gZ3JhZGllbnRzIG5vdCBuZWVkZWRcbiAgICAgICAgZm9yIHAgaW4gc2VsZi5zaGFkb3cucGFyYW1ldGVycygpOlxuICAgICAgICAgICAgcC5yZXF1aXJlc19ncmFkXyhGYWxzZSlcblxuICAgIEB0b3JjaC5ub19ncmFkKClcbiAgICBkZWYgdXBkYXRlKHNlbGYsIG1vZGVsKTpcbiAgICAgICAgXCJcIlwiVXBkYXRlIHNoYWRvdyB3ZWlnaHRzOiB0aGV0YV9lbWEgPSBkZWNheSAqIHRoZXRhX2VtYSArICgxLWRlY2F5KSAqIHRoZXRhXCJcIlwiXG4gICAgICAgIGZvciBlbWFfcGFyYW0sIHBhcmFtIGluIHppcChzZWxmLnNoYWRvdy5wYXJhbWV0ZXJzKCksIG1vZGVsLnBhcmFtZXRlcnMoKSk6XG4gICAgICAgICAgICBlbWFfcGFyYW0uZGF0YS5tdWxfKHNlbGYuZGVjYXkpLmFkZF8ocGFyYW0uZGF0YSwgYWxwaGE9MS4wIC0gc2VsZi5kZWNheSlcblxuICAgIGRlZiBnZXRfbW9kZWwoc2VsZik6XG4gICAgICAgIHJldHVybiBzZWxmLnNoYWRvd1xuXG4jIERlbW9uc3RyYXRlIEVNQSBtb2RlbCB0cmFja2luZ1xuY2xhc3MgVGlueU5ldChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZmMgPSBubi5MaW5lYXIoNCwgMilcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYuZmMoeClcblxubW9kZWwgPSBUaW55TmV0KClcbmVtYV9tb2RlbCA9IEVNQU1vZGVsKG1vZGVsLCBkZWNheT0wLjk5OSlcblxuIyBTaW11bGF0ZSB0cmFpbmluZzogbW9kZWwgd2VpZ2h0cyBjaGFuZ2UsIEVNQSB0cmFja3Mgc2xvd2x5XG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5TR0QobW9kZWwucGFyYW1ldGVycygpLCBscj0wLjEpXG54ID0gdG9yY2gucmFuZG4oMTYsIDQpXG55ID0gdG9yY2gucmFuZGludCgwLCAyLCAoMTYsKSlcblxuZm9yIHN0ZXAgaW4gcmFuZ2UoMTAwKTpcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpKG1vZGVsKHgpLCB5KVxuICAgIGxvc3MuYmFja3dhcmQoKVxuICAgIG9wdGltaXplci5zdGVwKClcbiAgICBlbWFfbW9kZWwudXBkYXRlKG1vZGVsKVxuXG4jIENoZWNrOiBFTUEgd2VpZ2h0cyBhcmUgc21vb3RoZWQgdmVyc2lvbiBvZiBjdXJyZW50IHdlaWdodHNcbnBhcmFtID0gbGlzdChtb2RlbC5wYXJhbWV0ZXJzKCkpWzBdLmRhdGFbMCwgMF0uaXRlbSgpXG5lbWFfcGFyYW0gPSBsaXN0KGVtYV9tb2RlbC5nZXRfbW9kZWwoKS5wYXJhbWV0ZXJzKCkpWzBdLmRhdGFbMCwgMF0uaXRlbSgpXG5wcmludChmXCJDdXJyZW50IHdlaWdodFswLDBdOiB7cGFyYW06LjRmfVwiKVxucHJpbnQoZlwiRU1BIHdlaWdodFswLDBdOiAgICAge2VtYV9wYXJhbTouNGZ9XCIpXG5wcmludChmXCJEaWZmZXJlbmNlOiB7YWJzKHBhcmFtIC0gZW1hX3BhcmFtKTouNGZ9IChFTUEgbGFncyBiZWhpbmQpXCIpXG5wcmludChmXCJFZmZlY3RpdmUgd2luZG93OiB7MS8oMS0wLjk5OSk6LjBmfSBzdGVwc1wiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlN0b2NoYXN0aWMgV2VpZ2h0IEF2ZXJhZ2luZyAoU1dBKSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlNXQSAoSXptYWlsb3YgMjAxOCkgYXZlcmFnZXMgdGhlIHdlaWdodHMgb2YgU0dEIGl0ZXJhdGVzIHNhbXBsZWQgcGVyaW9kaWNhbGx5OiDOuF9TV0EgPSAoMS9uKc6jzrjigpwuIEtleSBpbnNpZ2h0OiB0aGUgYXZlcmFnZSBvZiBtdWx0aXBsZSBwb2ludHMgb24gYSBsb3NzIGxhbmRzY2FwZSB2YWxsZXkgdHlwaWNhbGx5IGxpZXMgYXQgYSBmbGF0dGVyIHBvaW50IHRoYW4gYW55IGluZGl2aWR1YWwgaXRlcmF0ZS4gU1dBIHdpdGggYSBjeWNsaWNhbCBMUiBzY2hlZHVsZSB3b3JrcyBhcyBmb2xsb3dzOiB0cmFpbiB3aXRoIGEgaGlnaCBMUiBmb3IgayBzdGVwcyAoZXhwbG9yZXMgdGhlIGxvc3MgYmFzaW4gYnJvYWRseSksIHRoZW4gc3RlcCB0byBsb3cgTFIgKHNoYXJwIGRlc2NlbnQgdG8gYSBsb2NhbCBtaW5pbXVtKSwgdGFrZSBhIHdlaWdodCBzbmFwc2hvdDsgcmVwZWF0LiBBdmVyYWdlIGFsbCBzbmFwc2hvdHMgYXQgdGhlIGVuZC4gUmVzdWx0OiB0aGUgZmluYWwgYXZlcmFnZWQgcGFyYW1ldGVycyBjb252ZXJnZSB0byBhIGJyb2FkIGZsYXQgbWluaW11bSB3aXRoIGJldHRlciB0ZXN0IGFjY3VyYWN5IHRoYW4gdXNpbmcgYW55IHNpbmdsZSBjaGVja3BvaW50LiBJbXBsZW1lbnRhdGlvbiB1c2VzIHRvcmNoLm9wdGltLnN3YV91dGlscy5BdmVyYWdlZE1vZGVsIGZvciB3ZWlnaHQgdHJhY2tpbmcgYW5kIHVwZGF0ZV9ibihsb2FkZXIsIHN3YV9tb2RlbCkgdG8gcmVjYWxjdWxhdGUgYmF0Y2ggbm9ybWFsaXphdGlvbiBydW5uaW5nIHN0YXRpc3RpY3MgZm9yIHRoZSBhdmVyYWdlZCB3ZWlnaHRzIOKAlCBCTiBhZmZpbmUgcGFyYW1ldGVycyBhcmUgYXZlcmFnZWQgYnV0IHJ1bm5pbmcgc3RhdGlzdGljcyBtdXN0IGJlIHJlY29tcHV0ZWQgZnJvbSBkYXRhLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkltcGxlbWVudGF0aW9uIFBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTW9tZW50dW0gdG9vIGhpZ2ggKM6y4oaSMSk6IHRoZSB2ZWxvY2l0eSB0ZXJtIGRvbWluYXRlcyBhbmQgdGhlIG9wdGltaXplciBvdmVyc2hvb3RzLCBjYXVzaW5nIG9zY2lsbGF0aW9ucyBhbmQgZXZlbnR1YWwgZGl2ZXJnZW5jZS4gRm9yIGNvbnZleCBwcm9ibGVtcywgb3B0aW1hbCDOsiA9ICjiiJrOuuKIkjEpLyjiiJrOuisxKS4gRm9yIG5ldXJhbCBuZXR3b3JrcywgzrI9MC45IGlzIHN0YW5kYXJkOyDOsj0wLjk5IGlzIHVzZWQgaW4gc29tZSBBZGFtIHZhcmlhbnRzLiBTZXR0aW5nIM6yPTAgcmVjb3ZlcnMgdmFuaWxsYSBTR0QuIEVNQSBkZWNheSB0b28gaGlnaDogaWYgZGVjYXk9MC45OTk5LCB0aGUgRU1BIGxhZ3MgMTAsMDAwIHN0ZXBzIGJlaGluZCB0aGUgY3VycmVudCBtb2RlbCDigJQgaXQgdHJhY2tzIG1vZGVsIGNoYW5nZXMgdG9vIHNsb3dseSBkdXJpbmcgZWFybHkgdHJhaW5pbmcuIFVzZSBsb3dlciBkZWNheSAoMC45OTkpIGR1cmluZyBlYXJseSB0cmFpbmluZyBhbmQgaW5jcmVhc2UgaXQgdG93YXJkIDAuOTk5OSBkdXJpbmcgbGF0ZXIgdHJhaW5pbmcgc3RhZ2VzLiBTV0EgcGl0ZmFsbDogaWYgQk4gcnVubmluZyBzdGF0aXN0aWNzIGFyZSBub3QgcmVjYWxjdWxhdGVkIGFmdGVyIHdlaWdodCBhdmVyYWdpbmcsIHRoZSBtb2RlbCBwcm9kdWNlcyBpbmNvcnJlY3Qgbm9ybWFsaXphdGlvbnMgYmVjYXVzZSB0aGUgYXZlcmFnZWQgd2VpZ2h0cyBwcm9kdWNlIGEgZGlmZmVyZW50IGFjdGl2YXRpb24gZGlzdHJpYnV0aW9uIHRoYW4gYW55IGluZGl2aWR1YWwgY2hlY2twb2ludC4gQWx3YXlzIGNhbGwgdG9yY2gub3B0aW0uc3dhX3V0aWxzLnVwZGF0ZV9ibihsb2FkZXIsIHN3YV9tb2RlbCkgYWZ0ZXIgU1dBIGF2ZXJhZ2luZyBhbmQgYmVmb3JlIGV2YWx1YXRpb24uIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUHJhY3RpY2FsIEd1aWRhbmNlIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVXNlIM6yPTAuOSBhcyB0aGUgZGVmYXVsdCBtb21lbnR1bSBjb2VmZmljaWVudCBmb3IgU0dEIHdpdGggbW9tZW50dW0g4oCUIHRoaXMgaXMgdGhlIHN0YW5kYXJkIHNldHRpbmcgZm9yIGltYWdlIGNsYXNzaWZpY2F0aW9uIChSZXNOZXQvSW1hZ2VOZXQgdHJhaW5pbmcpLiBGb3IgQWRhbSwgzrLigoE9MC45IGFuZCDOsuKCgj0wLjk5OSBhcmUgc3RhbmRhcmQgZGVmYXVsdHMgdGhhdCByYXJlbHkgbmVlZCB0dW5pbmcuIFVzZSBTV0Egd2hlbiB0cmFpbmluZyBidWRnZXQgaXMgZml4ZWQgYW5kIHlvdSB3YW50IDEtMiUgYWNjdXJhY3kgaW1wcm92ZW1lbnQgZm9yIGZyZWU6IHVzZSBBdmVyYWdlZE1vZGVsIGZyb20gdG9yY2gub3B0aW0uc3dhX3V0aWxzIGFuZCBhY3RpdmF0ZSBTV0EgZm9yIHRoZSBmaW5hbCAyMC0yNSUgb2YgdHJhaW5pbmcgZXBvY2hzLiBGb3IgRU1BIHRhcmdldCBuZXR3b3JrcyBpbiBSTCBhbmQgY29udHJhc3RpdmUgbGVhcm5pbmcsIHN0YXJ0IHdpdGggZGVjYXk9MC45OTYgKHVzZWQgaW4gQllPTCkgb3IgMC45OSAodXNlZCBpbiBEUU4pIOKAlCBoaWdoZXIgZGVjYXkgZ2l2ZXMgbW9yZSBzdGFibGUgdGFyZ2V0cyBidXQgc2xvd2VyIHRyYWNraW5nIG9mIHRoZSBjdXJyZW50IG1vZGVsLiBNb25pdG9yIHRoZSByYXRpbyDigJZ24oCWL+KAls644oCWICh2ZWxvY2l0eSBtYWduaXR1ZGUgcmVsYXRpdmUgdG8gcGFyYW1ldGVyIG1hZ25pdHVkZSkgdG8gY2hlY2sgbW9tZW50dW0gYWdncmVzc2l2ZW5lc3M6IGlmIHRoaXMgcmF0aW8gZXhjZWVkcyAxLCBtb21lbnR1bSBpcyB0b28gYWdncmVzc2l2ZSBmb3IgdGhlIGN1cnJlbnQgTFIgY29tYmluYXRpb24uIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLm9wdGltLnN3YV91dGlscyBpbXBvcnQgQXZlcmFnZWRNb2RlbCwgU1dBTFJcblxuZGVmIHRyYWluX3dpdGhfc3dhKG1vZGVsLCB0cmFpbl9sb2FkZXIsIG5fZXBvY2hzPTUwLCBzd2Ffc3RhcnQ9NDApOlxuICAgIFwiXCJcIlxuICAgIFNXQSB0cmFpbmluZzogcmVndWxhciBTR0QgZm9yIGZpcnN0IHN3YV9zdGFydCBlcG9jaHMsXG4gICAgdGhlbiBzd2l0Y2ggdG8gU1dBIG1vZGUgd2l0aCBjeWNsaWNhbCBMUi5cbiAgICBcIlwiXCJcbiAgICBvcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5TR0QobW9kZWwucGFyYW1ldGVycygpLCBscj0wLjEsIG1vbWVudHVtPTAuOSlcbiAgICBzd2FfbW9kZWwgPSBBdmVyYWdlZE1vZGVsKG1vZGVsKVxuICAgIHN3YV9zY2hlZHVsZXIgPSBTV0FMUihvcHRpbWl6ZXIsIHN3YV9scj0wLjA1KVxuICAgIGNyaXRlcmlvbiA9IG5uLkNyb3NzRW50cm9weUxvc3MoKVxuXG4gICAgZm9yIGVwb2NoIGluIHJhbmdlKG5fZXBvY2hzKTpcbiAgICAgICAgbW9kZWwudHJhaW4oKVxuICAgICAgICBmb3IgWCwgeSBpbiB0cmFpbl9sb2FkZXI6XG4gICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgICAgIGxvc3MgPSBjcml0ZXJpb24obW9kZWwoWCksIHkpXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcblxuICAgICAgICBpZiBlcG9jaCA+PSBzd2Ffc3RhcnQ6XG4gICAgICAgICAgICAjIFNXQSBwaGFzZTogYXZlcmFnZSB3ZWlnaHRzIGFjcm9zcyBlcG9jaHNcbiAgICAgICAgICAgIHN3YV9tb2RlbC51cGRhdGVfcGFyYW1ldGVycyhtb2RlbClcbiAgICAgICAgICAgIHN3YV9zY2hlZHVsZXIuc3RlcCgpXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICAjIFdhcm11cC9jb3NpbmUgcGhhc2VcbiAgICAgICAgICAgIHBhc3NcblxuICAgICMgQ1JJVElDQUw6IHJlY2FsY3VsYXRlIEJOIHN0YXRpc3RpY3MgZm9yIGF2ZXJhZ2VkIG1vZGVsXG4gICAgIyAoQk4gcnVubmluZyBzdGF0cyBhcmUgbm90IGF2ZXJhZ2VkLCBvbmx5IGFmZmluZSBwYXJhbXMpXG4gICAgIyB0b3JjaC5vcHRpbS5zd2FfdXRpbHMudXBkYXRlX2JuKHRyYWluX2xvYWRlciwgc3dhX21vZGVsKVxuXG4gICAgcHJpbnQoZlwiU1dBIHRyYWluaW5nIGNvbXBsZXRlLiBVc2Ugc3dhX21vZGVsIGZvciBpbmZlcmVuY2UuXCIpXG4gICAgcHJpbnQoXCJSZW1lbWJlcjogY2FsbCB1cGRhdGVfYm4odHJhaW5fbG9hZGVyLCBzd2FfbW9kZWwpIGJlZm9yZSBldmFsdWF0aW9uIVwiKVxuICAgIHJldHVybiBzd2FfbW9kZWxcblxucHJpbnQoXCJTV0EgdHJhaW5pbmcgZnVuY3Rpb24gZGVmaW5lZC5cIilcbnByaW50KFwiS2V5IGluc2lnaHQ6IFNXQSBhdmVyYWdlcyB3ZWlnaHRzIG9mIFNHRCBzbmFwc2hvdHMgLT4gZmxhdCBtaW5pbWEgLT4gYmV0dGVyIGdlbmVyYWxpemF0aW9uLlwiKSJ9LCB7InR5cGUiOiAiY2FsbG91dCIsICJ0aXRsZSI6ICJNb21lbnR1bSBBbXBsaWZpZXMgQmFkIEdyYWRpZW50cyBUb28iLCAiY29udGVudCI6ICJNb21lbnR1bSBhY2N1bXVsYXRlcyBhbGwgcGFzdCBncmFkaWVudHMg4oCUIGluY2x1ZGluZyBpbmNvcnJlY3Qgb25lcyBhdCB0aGUgc3RhcnQgb2YgdHJhaW5pbmcgb3IgYWZ0ZXIgYSBzdWRkZW4gTFIgY2hhbmdlLiBJZiB0aGUgaW5pdGlhbCBMUiBpcyB0b28gbGFyZ2UgKGNhdXNpbmcgYSBiYWQgZmlyc3Qgc3RlcCksIG1vbWVudHVtIHdpbGwgYW1wbGlmeSB0aGF0IGJhZCBkaXJlY3Rpb24gZm9yIHRoZSBuZXh0IDEvKDEtYmV0YSkgc3RlcHMuIEFsd2F5cyB3YXJtIHVwIHRoZSBsZWFybmluZyByYXRlIGZvciB0aGUgZmlyc3QgNS0xMCUgb2YgdHJhaW5pbmcuIFdoZW4gcmVzdW1pbmcgZnJvbSBhIGNoZWNrcG9pbnQsIGNvbnNpZGVyIHplcm9pbmcgdGhlIG1vbWVudHVtIGJ1ZmZlciAob3B0aW1pemVyLnN0YXRlID0ge30pIHRvIGF2b2lkIGNhcnJ5aW5nIG92ZXIgc3RhbGUgdmVsb2NpdGllcyB0aGF0IGRvIG5vdCBhcHBseSB0byB0aGUgbmV3IExSIHNjaGVkdWxlLiJ9LCB7InR5cGUiOiAidGFibGUiLCAiaGVhZGVycyI6IFsiTWV0aG9kIiwgIkNvbnZlcmdlbmNlIFJhdGUgKGNvbnZleCkiLCAiQ29udmVyZ2VuY2UgUmF0ZSAoc3Ryb25nbHkgY29udmV4KSIsICJFZmZlY3RpdmUgU3RlcCJdLCAicm93cyI6IFtbIlZhbmlsbGEgR0QiLCAiTygxL1QpIiwgIk8oZXhwKC1tdSpUL0wpKSIsICJldGEiXSwgWyJIZWF2eSBCYWxsIChtb21lbnR1bSkiLCAiTygxL1ReMikgKHF1YWRyYXRpYykiLCAiTyhleHAoLVQqc3FydChtdS9MKSkpIiwgImV0YS8oMS1iZXRhKSJdLCBbIk5lc3Rlcm92IChsb29rYWhlYWQpIiwgIk8oMS9UXjIpIChnZW5lcmFsKSIsICJPKGV4cCgtVCpzcXJ0KG11L0wpKSkiLCAiZXRhLygxLWJldGEpIl0sIFsiU1dBIChpdGVyYXRlIGF2ZykiLCAiTygxL1QpIiwgIk8oMS9UKSAoY29udmV4IHJhdGUpIiwgIk4vQSJdLCBbIkVNQSAoZXhwb25lbnRpYWwgYXZnKSIsICJCaWFzZWQgZXN0aW1hdG9yIiwgIkJpYXMtdmFyaWFuY2UgdHJhZGVvZmYiLCAiTi9BIl1dfSwgeyJ0eXBlIjogImRpdmlkZXIifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJLZXkgVGFrZWF3YXlzIn0sIHsidHlwZSI6ICJsaXN0IiwgIml0ZW1zIjogWyJIZWF2eSBiYWxsIG1vbWVudHVtIHZ0ID0gYmV0YSp2X3t0LTF9ICsgZXRhKmd0LCB0aGV0YV90ID0gdGhldGFfe3QtMX0gLSB2dCBhbXBsaWZpZXMgY29uc2lzdGVudCBncmFkaWVudHMgYnkgZmFjdG9yIDEvKDEtYmV0YSkgYW5kIGRhbXBzIG9zY2lsbGF0aW5nIGdyYWRpZW50cy4iLCAiRU1BIG10ID0gYmV0YSptX3t0LTF9ICsgKDEtYmV0YSkqeHQgaGFzIGVmZmVjdGl2ZSB3aW5kb3cgMS8oMS1iZXRhKS4gQmlhcyBjb3JyZWN0aW9uIG1faGF0X3QgPSBtdC8oMS1iZXRhXnQpIGlzIGVzc2VudGlhbCBmb3IgZWFybHkgdGltZXN0ZXBzLiIsICJNb21lbnR1bSBhY2hpZXZlcyBPKDEvVF4yKSBjb252ZXJnZW5jZSBmb3IgY29udmV4IHNtb290aCBmdW5jdGlvbnMgdnMgTygxL1QpIGZvciBHRCDigJQgZXF1aXZhbGVudCB0byBzcXJ0KGthcHBhKSBzcGVlZHVwIGZvciBzdHJvbmdseSBjb252ZXggcHJvYmxlbXMuIiwgIkVNQSBhcHBlYXJzIGluIEFkYW0gKGZpcnN0IG1vbWVudCksIERRTiB0YXJnZXQgbmV0d29ya3MsIEJZT0wgY29udHJhc3RpdmUgbGVhcm5pbmcsIFNXQSwgYW5kIGRpZmZ1c2lvbiBtb2RlbCBpbmZlcmVuY2Ug4oCUIGEgdW5pdmVyc2FsIHNtb290aGluZyBwcmltaXRpdmUuIiwgIlNXQSBhdmVyYWdlcyBTR0QgaXRlcmF0ZXMgc2FtcGxlZCB3aXRoIGN5Y2xpY2FsIExSLCBjb252ZXJnaW5nIHRvIGZsYXQgbWluaW1hIHdpdGggYmV0dGVyIGdlbmVyYWxpemF0aW9uIHRoYW4gYW55IHNpbmdsZSBjaGVja3BvaW50LiIsICJGb3IgRU1BIG1vZGVscywgYWx3YXlzIHJlY2FsY3VsYXRlIEJOIHJ1bm5pbmcgc3RhdGlzdGljcyBhZnRlciB3ZWlnaHQgYXZlcmFnaW5nIOKAlCB0aGV5IGFyZSBub3QgYXZlcmFnZWQsIG9ubHkgYWZmaW5lIHBhcmFtZXRlcnMgKGdhbW1hLCBiZXRhKSBhcmUuIiwgIldoZW4gcmVzdW1pbmcgdHJhaW5pbmcgYWZ0ZXIgYSBjaGVja3BvaW50LCBjb25zaWRlciB6ZXJvaW5nIHRoZSBtb21lbnR1bSBidWZmZXIgdG8gYXZvaWQgc3RhbGUgdmVsb2NpdHkgY29udGFtaW5hdGluZyB0aGUgbmV3IExSIHJlZ2ltZS4iXX1d"
---

# Momentum and Exponential Moving Averages

Momentum is the single most impactful modification to basic gradient descent, providing O(1/T²) convergence for convex smooth functions vs O(1/T) for vanilla GD. But momentum is more than an acceleration technique — its underlying mechanism (exponential moving average of gradients) is the core primitive in Adam's first moment, EMA target networks in deep RL (DQN, BYOL), model weight averaging (SWA, EMA ensembles), and temporal difference bootstrapping. Understanding momentum through the lens of exponential moving averages, effective step size, oscillation damping, and the physical ball-on-slope analogy unifies these seemingly disparate applications under a single mathematical framework applicable across optimization, reinforcement learning, and generative modeling.

## Core Definition: Heavy Ball Method

The heavy ball momentum update (Polyak 1964): vₜ = βvₜ₋₁ + ηgₜ; θₜ = θₜ₋₁ − vₜ, where gₜ = ∇L(θₜ₋₁), β ∈ [0,1) is the momentum coefficient, η is the learning rate, and vₜ is the velocity vector. Equivalently: θₜ = θₜ₋₁ − ηgₜ − β(θₜ₋₁ − θₜ₋₂). Geometric series interpretation: vₜ = ηΣₖ₌₀^∞ βᵏ gₜ₋ₖ — velocity is an exponentially decaying weighted average of all past gradients. In consistent gradient directions, gradients reinforce: vₜ → η/(1−β) · g (steady-state velocity). In oscillating directions, they cancel: momentum damps oscillations across the valley. Effective step size in a consistent direction: η/(1−β). For β=0.9 this is 10× amplification; for β=0.99 it gives 100× amplification.

```python
import numpy as np
import matplotlib.pyplot as plt

def sgd_momentum(grad_f, theta0, lr, beta, n_steps, f=None):
    """
    SGD with heavy ball momentum.
    vt = beta * v_{t-1} + lr * grad(theta_{t-1})
    theta_t = theta_{t-1} - vt
    """
    theta = np.array(theta0, dtype=np.float64)
    v = np.zeros_like(theta)
    history = {'theta': [theta.copy()], 'loss': [f(theta)] if f else []}

    for t in range(n_steps):
        g = grad_f(theta)
        v = beta * v + lr * g       # velocity accumulates
        theta = theta - v
        history['theta'].append(theta.copy())
        if f: history['loss'].append(f(theta))

    return history

# Compare vanilla GD vs momentum on ill-conditioned quadratic
# f(x,y) = 0.5*(x^2 + 100*y^2)  -- condition number kappa=100
f = lambda x: 0.5 * (x[0]**2 + 100*x[1]**2)
grad_f = lambda x: np.array([x[0], 100*x[1]])
x0 = np.array([10.0, 1.0])

L, mu = 100.0, 1.0
eta_gd = 2/(mu + L)       # optimal for GD
eta_mom = 2/(np.sqrt(mu) + np.sqrt(L))**2  # optimal for momentum
beta_mom = ((np.sqrt(L) - np.sqrt(mu))/(np.sqrt(L) + np.sqrt(mu)))**2

hist_gd = sgd_momentum(grad_f, x0, lr=eta_gd, beta=0, n_steps=300, f=f)
hist_mom = sgd_momentum(grad_f, x0, lr=eta_mom, beta=beta_mom, n_steps=300, f=f)

# Find steps to reach 1e-4 precision
steps_gd = next((i for i, l in enumerate(hist_gd['loss']) if l < 1e-4), 300)
steps_mom = next((i for i, l in enumerate(hist_mom['loss']) if l < 1e-4), 300)
print(f"GD:       {steps_gd} steps to 1e-4  (kappa={L/mu:.0f})")
print(f"Momentum: {steps_mom} steps to 1e-4  (speedup: {steps_gd/max(steps_mom,1):.1f}x)")
print(f"Effective momentum step size: eta/(1-beta) = {eta_mom/(1-beta_mom):.4f}")
print(f"Momentum coefficient beta = {beta_mom:.4f}")
```

## Exponential Moving Average as Low-Pass Filter

The EMA mₜ = βmₜ₋₁ + (1−β)xₜ is a recursive formula with explicit solution mₜ = (1−β)Σₖ₌₀^t βᵏ x_{t-k}. The weights (1−β)βᵏ sum to 1 (geometric series) and decay exponentially — recent values dominate. Effective window: τ = 1/(1−β). For β=0.9: window≈10 steps; β=0.99: window≈100 steps; β=0.999: window≈1000 steps. In frequency domain: EMA is a first-order IIR low-pass filter, passing low-frequency (slow trend) signals and attenuating high-frequency (noise) signals. The cutoff frequency is approximately (1−β)/(2π). Heavy ball momentum uses EMA of gradients: β=0.9 smooths gradient noise while preserving the trend direction, enabling larger effective step sizes than vanilla GD without the instability that would arise from simply using a larger learning rate directly.

```python
import numpy as np

def ema(values, beta=0.9, bias_correct=True):
    """
    Exponential moving average.
    m_t = beta * m_{t-1} + (1 - beta) * x_t
    With bias correction: m_hat_t = m_t / (1 - beta^t)
    """
    m = 0.0
    emas = []
    for t, x in enumerate(values, start=1):
        m = beta * m + (1 - beta) * x
        if bias_correct:
            m_hat = m / (1 - beta**t)
        else:
            m_hat = m
        emas.append(m_hat)
    return emas

# Demonstrate effective window size
beta = 0.9
effective_window = 1 / (1 - beta)
print(f"beta={beta}: effective window approx {effective_window:.0f} steps")

# Show EMA tracking a step function
n = 200
signal = np.concatenate([np.zeros(100), np.ones(100)])  # step at t=100
ema_90 = ema(signal, beta=0.9)
ema_99 = ema(signal, beta=0.99)

# Find tracking lag: steps to reach 63% of step value after the step
lag_90 = next((t for t, v in enumerate(ema_90[100:]) if v > 0.63), None) + 1
lag_99 = next((t for t, v in enumerate(ema_99[100:]) if v > 0.63), None) + 1
print(f"beta=0.9:  lag to 63% of step = {lag_90} steps  (approx 1/(1-beta)={1/(1-0.9):.0f})")
print(f"beta=0.99: lag to 63% of step = {lag_99} steps  (approx 1/(1-beta)={1/(1-0.99):.0f})")

# Bias correction importance for early steps
early_ema_no_bc = ema([1.0]*20, beta=0.9, bias_correct=False)
early_ema_bc = ema([1.0]*20, beta=0.9, bias_correct=True)
print(f"\nAfter 1 step with constant input=1: no-BC={early_ema_no_bc[0]:.3f} vs BC={early_ema_bc[0]:.3f}")
print(f"After 10 steps: no-BC={early_ema_no_bc[9]:.3f} vs BC={early_ema_bc[9]:.3f}")
```

## Accelerated Convergence: Momentum Achieves O(1/T²)

Nesterov's acceleration theorem: for L-smooth convex f, GD with momentum achieves f(θₜ)−f* ≤ O(L‖θ₀−θ*‖²/T²), compared to O(L‖θ₀−θ*‖²/T) for vanilla GD — a factor of T speedup. For strongly convex functions: momentum achieves O(exp(−T√(μ/L))) convergence vs O(exp(−T·μ/L)) for GD — linear rate but with √κ instead of κ dependence. Optimal momentum coefficient for convex smooth problems: β = (√κ−1)/(√κ+1) where κ = L/μ. Physical intuition: the ball picks up speed downhill (momentum accumulates) and uses inertia to cross small barriers and maintain forward progress. The deceleration near the minimum prevents overshoot: near θ*, the gradient reverses direction, applying a braking force that opposes the accumulated momentum and allows the optimizer to settle.

## ML Connections: EMA in Deep Learning

EMA appears in multiple critical ML components beyond optimization: (1) Adam's first moment: mₜ = β₁mₜ₋₁ + (1−β₁)gₜ (EMA of gradients with β₁=0.9). (2) DQN target network: θ⁻ = β·θ⁻ + (1−β)·θ — slow-moving copy of Q-network for stable Bellman targets (Mnih 2015). (3) BYOL (Grill 2020): online encoder θ updated by gradient; target encoder ξ = τ·ξ + (1−τ)·θ (momentum encoder), enabling self-supervised learning without negative samples. (4) Stochastic Weight Averaging (SWA, Izmailov 2018): θ_SWA = (1/n)Σθₜ (uniform average of SGD iterates), converges to flat minima and improves generalization. (5) EMA ensembles in diffusion models: a slow-moving copy of model weights is used for inference, yielding better sample quality than the current training checkpoint due to reduced noise sensitivity.

```python
import torch
import torch.nn as nn
import copy

class EMAModel:
    """
    Exponential Moving Average of model weights.
    Used in: BYOL target network, diffusion model inference, SWA.
    """
    def __init__(self, model, decay=0.999):
        self.decay = decay
        self.shadow = copy.deepcopy(model)
        # Freeze shadow -- gradients not needed
        for p in self.shadow.parameters():
            p.requires_grad_(False)

    @torch.no_grad()
    def update(self, model):
        """Update shadow weights: theta_ema = decay * theta_ema + (1-decay) * theta"""
        for ema_param, param in zip(self.shadow.parameters(), model.parameters()):
            ema_param.data.mul_(self.decay).add_(param.data, alpha=1.0 - self.decay)

    def get_model(self):
        return self.shadow

# Demonstrate EMA model tracking
class TinyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(4, 2)
    def forward(self, x):
        return self.fc(x)

model = TinyNet()
ema_model = EMAModel(model, decay=0.999)

# Simulate training: model weights change, EMA tracks slowly
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
x = torch.randn(16, 4)
y = torch.randint(0, 2, (16,))

for step in range(100):
    optimizer.zero_grad()
    loss = nn.CrossEntropyLoss()(model(x), y)
    loss.backward()
    optimizer.step()
    ema_model.update(model)

# Check: EMA weights are smoothed version of current weights
param = list(model.parameters())[0].data[0, 0].item()
ema_param = list(ema_model.get_model().parameters())[0].data[0, 0].item()
print(f"Current weight[0,0]: {param:.4f}")
print(f"EMA weight[0,0]:     {ema_param:.4f}")
print(f"Difference: {abs(param - ema_param):.4f} (EMA lags behind)")
print(f"Effective window: {1/(1-0.999):.0f} steps")
```

## Stochastic Weight Averaging (SWA)

SWA (Izmailov 2018) averages the weights of SGD iterates sampled periodically: θ_SWA = (1/n)Σθₜ. Key insight: the average of multiple points on a loss landscape valley typically lies at a flatter point than any individual iterate. SWA with a cyclical LR schedule works as follows: train with a high LR for k steps (explores the loss basin broadly), then step to low LR (sharp descent to a local minimum), take a weight snapshot; repeat. Average all snapshots at the end. Result: the final averaged parameters converge to a broad flat minimum with better test accuracy than using any single checkpoint. Implementation uses torch.optim.swa_utils.AveragedModel for weight tracking and update_bn(loader, swa_model) to recalculate batch normalization running statistics for the averaged weights — BN affine parameters are averaged but running statistics must be recomputed from data.

## Implementation Pitfalls

Momentum too high (β→1): the velocity term dominates and the optimizer overshoots, causing oscillations and eventual divergence. For convex problems, optimal β = (√κ−1)/(√κ+1). For neural networks, β=0.9 is standard; β=0.99 is used in some Adam variants. Setting β=0 recovers vanilla SGD. EMA decay too high: if decay=0.9999, the EMA lags 10,000 steps behind the current model — it tracks model changes too slowly during early training. Use lower decay (0.999) during early training and increase it toward 0.9999 during later training stages. SWA pitfall: if BN running statistics are not recalculated after weight averaging, the model produces incorrect normalizations because the averaged weights produce a different activation distribution than any individual checkpoint. Always call torch.optim.swa_utils.update_bn(loader, swa_model) after SWA averaging and before evaluation.

## Practical Guidance

Use β=0.9 as the default momentum coefficient for SGD with momentum — this is the standard setting for image classification (ResNet/ImageNet training). For Adam, β₁=0.9 and β₂=0.999 are standard defaults that rarely need tuning. Use SWA when training budget is fixed and you want 1-2% accuracy improvement for free: use AveragedModel from torch.optim.swa_utils and activate SWA for the final 20-25% of training epochs. For EMA target networks in RL and contrastive learning, start with decay=0.996 (used in BYOL) or 0.99 (used in DQN) — higher decay gives more stable targets but slower tracking of the current model. Monitor the ratio ‖v‖/‖θ‖ (velocity magnitude relative to parameter magnitude) to check momentum aggressiveness: if this ratio exceeds 1, momentum is too aggressive for the current LR combination.

```python
import torch
import torch.nn as nn
from torch.optim.swa_utils import AveragedModel, SWALR

def train_with_swa(model, train_loader, n_epochs=50, swa_start=40):
    """
    SWA training: regular SGD for first swa_start epochs,
    then switch to SWA mode with cyclical LR.
    """
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
    swa_model = AveragedModel(model)
    swa_scheduler = SWALR(optimizer, swa_lr=0.05)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(n_epochs):
        model.train()
        for X, y in train_loader:
            optimizer.zero_grad()
            loss = criterion(model(X), y)
            loss.backward()
            optimizer.step()

        if epoch >= swa_start:
            # SWA phase: average weights across epochs
            swa_model.update_parameters(model)
            swa_scheduler.step()
        else:
            # Warmup/cosine phase
            pass

    # CRITICAL: recalculate BN statistics for averaged model
    # (BN running stats are not averaged, only affine params)
    # torch.optim.swa_utils.update_bn(train_loader, swa_model)

    print(f"SWA training complete. Use swa_model for inference.")
    print("Remember: call update_bn(train_loader, swa_model) before evaluation!")
    return swa_model

print("SWA training function defined.")
print("Key insight: SWA averages weights of SGD snapshots -> flat minima -> better generalization.")
```

> **Momentum Amplifies Bad Gradients Too**: Momentum accumulates all past gradients — including incorrect ones at the start of training or after a sudden LR change. If the initial LR is too large (causing a bad first step), momentum will amplify that bad direction for the next 1/(1-beta) steps. Always warm up the learning rate for the first 5-10% of training. When resuming from a checkpoint, consider zeroing the momentum buffer (optimizer.state = {}) to avoid carrying over stale velocities that do not apply to the new LR schedule.

| Method | Convergence Rate (convex) | Convergence Rate (strongly convex) | Effective Step |
|---|---|---|---|
| Vanilla GD | O(1/T) | O(exp(-mu*T/L)) | eta |
| Heavy Ball (momentum) | O(1/T^2) (quadratic) | O(exp(-T*sqrt(mu/L))) | eta/(1-beta) |
| Nesterov (lookahead) | O(1/T^2) (general) | O(exp(-T*sqrt(mu/L))) | eta/(1-beta) |
| SWA (iterate avg) | O(1/T) | O(1/T) (convex rate) | N/A |
| EMA (exponential avg) | Biased estimator | Bias-variance tradeoff | N/A |

---

## Key Takeaways

- Heavy ball momentum vt = beta*v_{t-1} + eta*gt, theta_t = theta_{t-1} - vt amplifies consistent gradients by factor 1/(1-beta) and damps oscillating gradients.
- EMA mt = beta*m_{t-1} + (1-beta)*xt has effective window 1/(1-beta). Bias correction m_hat_t = mt/(1-beta^t) is essential for early timesteps.
- Momentum achieves O(1/T^2) convergence for convex smooth functions vs O(1/T) for GD — equivalent to sqrt(kappa) speedup for strongly convex problems.
- EMA appears in Adam (first moment), DQN target networks, BYOL contrastive learning, SWA, and diffusion model inference — a universal smoothing primitive.
- SWA averages SGD iterates sampled with cyclical LR, converging to flat minima with better generalization than any single checkpoint.
- For EMA models, always recalculate BN running statistics after weight averaging — they are not averaged, only affine parameters (gamma, beta) are.
- When resuming training after a checkpoint, consider zeroing the momentum buffer to avoid stale velocity contaminating the new LR regime.

