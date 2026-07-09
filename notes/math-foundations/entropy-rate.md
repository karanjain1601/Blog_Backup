---
title: "Entropy Rate and Information in Sequences"
slug: "entropy-rate"
description: "Entropy rate characterizes the irreducible uncertainty per symbol in a stochastic process. Covers Markov chains, language model perplexity, bits-per-byte, and Lempel-Ziv complexity."
tags: ["information-theory", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBzaW5nbGUgcmFuZG9tIHZhcmlhYmxlIGhhcyBlbnRyb3B5IEgoWCkuIEJ1dCByZWFsLXdvcmxkIGRhdGEg4oCUIHRleHQsIGF1ZGlvLCB0aW1lIHNlcmllcyDigJQgaXMgYSAqc2VxdWVuY2UqIG9mIHJhbmRvbSB2YXJpYWJsZXMgd2l0aCB0ZW1wb3JhbCBzdHJ1Y3R1cmUuIFRoZSBlbnRyb3B5IHJhdGUgY2FwdHVyZXMgaG93IG11Y2ggZ2VudWluZSB1bmNlcnRhaW50eSBleGlzdHMgcGVyIHN5bWJvbCBvbmNlIHdlIGFjY291bnQgZm9yIGFsbCB0aGUgcGF0dGVybnMgYW5kIGRlcGVuZGVuY2llcyBpbiB0aGUgc2VxdWVuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVmaW5pdGlvbiBvZiBFbnRyb3B5IFJhdGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIHN0b2NoYXN0aWMgcHJvY2VzcyB7WOKCmX0sIHRoZSBlbnRyb3B5IHJhdGUgaXMgZGVmaW5lZCBhcyB0aGUgbGltaXQ6XG5cbmggPSBsaW1fe27ihpLiiJ59ICgxL24pIEgoWOKCgSwgWOKCgiwgLi4uLCBY4oKZKVxuXG5wcm92aWRlZCB0aGUgbGltaXQgZXhpc3RzLiBGb3IgYSAqc3RhdGlvbmFyeSogcHJvY2VzcywgdGhpcyBsaW1pdCBhbHdheXMgZXhpc3RzIGFuZCBlcXVhbHMgdGhlIGNvbmRpdGlvbmFsIGVudHJvcHkgcmF0ZTpcblxuaCA9IGxpbV97buKGkuKInn0gSChY4oKZIHwgWF97bi0xfSwgLi4uLCBY4oKBKVxuXG5UaGUgY29uZGl0aW9uYWwgZm9ybSBzYXlzOiBhcyB3ZSBvYnNlcnZlIG1vcmUgY29udGV4dCwgdGhlIHBlci1zeW1ib2wgdW5jZXJ0YWludHkgZGVjcmVhc2VzIG1vbm90b25pY2FsbHkgYW5kIGNvbnZlcmdlcyB0byBoLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IHRoZSBMaW1pdCBFeGlzdHMgZm9yIFN0YXRpb25hcnkgUHJvY2Vzc2VzIiwiY29udGVudCI6IkZvciBhIHN0YXRpb25hcnkgcHJvY2VzcywgSChY4oKZfFhfe24tMX0sLi4uLFjigoEpIGlzIG5vbi1pbmNyZWFzaW5nIGluIG4gKG1vcmUgY29udGV4dCBuZXZlciBpbmNyZWFzZXMgZW50cm9weSkgYW5kIGJvdW5kZWQgYmVsb3cgYnkgMC4gQnkgdGhlIG1vbm90b25lIGNvbnZlcmdlbmNlIHRoZW9yZW0gdGhlIGxpbWl0IGV4aXN0cy4gVGhpcyBpcyBhIGNvbnNlcXVlbmNlIG9mIHRoZSBjaGFpbiBydWxlIGFuZCBzdWItYWRkaXRpdml0eSBvZiBlbnRyb3B5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwZWNpYWwgQ2FzZXMgYW5kIEV4YW1wbGVzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb2Nlc3MgVHlwZSIsIkVudHJvcHkgUmF0ZSBGb3JtdWxhIiwiRXhhbXBsZSIsIlJhdGUgKGJpdHMvc3ltYm9sKSJdLCJyb3dzIjpbWyJpLmkuZC4gdW5pZm9ybSBiaW5hcnkiLCJIKFjigoEpID0gbG9n4oKCKDIpID0gMSIsIkZhaXIgY29pbiBmbGlwcyIsIjEuMCJdLFsiaS5pLmQuIGJpYXNlZCBiaW5hcnkiLCJIKFjigoEpID0g4oiScCBsb2cgcCDiiJIgKDHiiJJwKSBsb2coMeKIknApIiwiQmlhc2VkIGNvaW4gKHA9MC4xKSIsIuKJiCAwLjQ3Il0sWyJpLmkuZC4gdW5pZm9ybSBvdmVyIGFscGhhYmV0IEEiLCJsb2figoIofEF8KSIsIlVuaWZvcm0gZGllIHJvbGxzICg2LXNpZGVkKSIsIuKJiCAyLjU4Il0sWyJGaXJzdC1vcmRlciBNYXJrb3YgY2hhaW4iLCLiiJLOo+G1oiDPgOG1oiDOo+KxvCBQ4bWi4rG8IGxvZyBQ4bWi4rG8IiwiV2VhdGhlciBtb2RlbCIsIlx1MDAzYyBIKFjigoEpIl0sWyJOYXR1cmFsIEVuZ2xpc2ggdGV4dCIsIlNoYW5ub24gZXhwZXJpbWVudCBlc3RpbWF0ZSIsIldyaXR0ZW4gRW5nbGlzaCIsIuKJiCAxLjDigJMxLjMiXSxbIlJhbmRvbSAoaW5jb21wcmVzc2libGUpIiwiSChY4oKBKSA9IG1heCBlbnRyb3B5IiwiVHJ1ZSByYW5kb20gYml0cyIsIj0gbG9n4oKCKHxBfCkiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVudHJvcHkgUmF0ZSBvZiBhIE1hcmtvdiBDaGFpbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGFuIGVyZ29kaWMsIHRpbWUtaG9tb2dlbmVvdXMgTWFya292IGNoYWluIHdpdGggdHJhbnNpdGlvbiBtYXRyaXggUCBhbmQgc3RhdGlvbmFyeSBkaXN0cmlidXRpb24gz4AsIHRoZSBlbnRyb3B5IHJhdGUgaGFzIGEgY2xvc2VkIGZvcm06XG5cbmggPSDiiJLOo+G1oiDPgOG1oiDOo+KxvCBQ4bWi4rG8IGxvZyBQ4bWi4rG8ID0gzqPhtaIgz4DhtaIgSChY4oKZIHwgWOKCmeKCi+KCgT1pKVxuXG5UaGlzIGlzIHRoZSBzdGF0aW9uYXJ5LWRpc3RyaWJ1dGlvbi13ZWlnaHRlZCBhdmVyYWdlIG9mIHRoZSBjb25kaXRpb25hbCBlbnRyb3B5IGF0IGVhY2ggc3RhdGUuIEEgaGlnaGx5IHByZWRpY3RhYmxlIGNoYWluIChuZWFyLWRldGVybWluaXN0aWMgdHJhbnNpdGlvbnMpIGhhcyBoIOKJiCAwOyBhIGZ1bGx5IHJhbmRvbSBjaGFpbiBoYXMgaCA9IGxvZ3xBfC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LmxpbmFsZyBpbXBvcnQgZWlnXG5cbmRlZiBtYXJrb3ZfZW50cm9weV9yYXRlKFA6IG5wLm5kYXJyYXksIGJhc2U6IGZsb2F0ID0gMi4wKSAtXHUwMDNlIGZsb2F0OlxuICAgIFwiXCJcIkNvbXB1dGUgZW50cm9weSByYXRlIG9mIGEgZmluaXRlIGVyZ29kaWMgTWFya292IGNoYWluLlxuXG4gICAgQXJnczpcbiAgICAgICAgUDogVHJhbnNpdGlvbiBtYXRyaXgsIHNoYXBlIChuX3N0YXRlcywgbl9zdGF0ZXMpLiBSb3dzIHN1bSB0byAxLlxuICAgICAgICBiYXNlOiBMb2dhcml0aG0gYmFzZSAoMiA9IGJpdHMsIGUgPSBuYXRzKS5cbiAgICBSZXR1cm5zOlxuICAgICAgICBFbnRyb3B5IHJhdGUgaCBpbiBzcGVjaWZpZWQgdW5pdHMuXG4gICAgXCJcIlwiXG4gICAgbiA9IFAuc2hhcGVbMF1cbiAgICBhc3NlcnQgbnAuYWxsY2xvc2UoUC5zdW0oYXhpcz0xKSwgMS4wKSwgXCJSb3dzIG11c3Qgc3VtIHRvIDFcIlxuXG4gICAgIyBTdGF0aW9uYXJ5IGRpc3RyaWJ1dGlvbjogbGVmdCBlaWdlbnZlY3RvciBmb3IgZWlnZW52YWx1ZSAxXG4gICAgIyBFcXVpdmFsZW50bHksIHNvbHZlIM+AIFAgPSDPgCB3aXRoIM6jIM+A4bWiID0gMVxuICAgIGVpZ2VudmFsdWVzLCBlaWdlbnZlY3RvcnMgPSBlaWcoUC5UKVxuICAgIHN0YXRpb25hcnlfaWR4ID0gbnAuYXJnbWluKG5wLmFicyhlaWdlbnZhbHVlcyAtIDEuMCkpXG4gICAgcGkgPSBucC5yZWFsKGVpZ2VudmVjdG9yc1s6LCBzdGF0aW9uYXJ5X2lkeF0pXG4gICAgcGkgPSBwaSAvIHBpLnN1bSgpICAjIG5vcm1hbGl6ZVxuXG4gICAgIyBDb21wdXRlIGggPSAtzqPhtaIgz4DhtaIgzqPisbwgUOG1ouKxvCBsb2cgUOG1ouKxvFxuICAgIGxvZ19mbiA9IG5wLmxvZyBpZiBiYXNlID09IG5wLmUgZWxzZSAobGFtYmRhIHg6IG5wLmxvZyh4KSAvIG5wLmxvZyhiYXNlKSlcbiAgICByb3dfZW50cm9waWVzID0gbnAuYXJyYXkoW1xuICAgICAgICAtbnAuc3VtKFBbaSwgUFtpXSBcdTAwM2UgMF0gKiBsb2dfZm4oUFtpLCBQW2ldIFx1MDAzZSAwXSkpXG4gICAgICAgIGZvciBpIGluIHJhbmdlKG4pXG4gICAgXSlcbiAgICBoID0gbnAuZG90KHBpLCByb3dfZW50cm9waWVzKVxuXG4gICAgcHJpbnQoZlwiU3RhdGlvbmFyeSBkaXN0cmlidXRpb24gz4A6IHtwaX1cIilcbiAgICBwcmludChmXCJQZXItc3RhdGUgY29uZGl0aW9uYWwgZW50cm9waWVzOiB7cm93X2VudHJvcGllc31cIilcbiAgICBwcmludChmXCJFbnRyb3B5IHJhdGUgaCA9IHtoOi42Zn0ge1x1MDAyN2JpdHNcdTAwMjcgaWYgYmFzZT09MiBlbHNlIFx1MDAyN25hdHNcdTAwMjd9L3N5bWJvbFwiKVxuICAgIHJldHVybiBoXG5cbiMgRXhhbXBsZTogMy1zdGF0ZSB3ZWF0aGVyIE1hcmtvdiBjaGFpblxuIyAgIFN0YXRlczogMD1zdW5ueSwgMT1jbG91ZHksIDI9cmFpbnlcblAgPSBucC5hcnJheShbXG4gICAgWzAuNywgMC4yLCAwLjFdLFxuICAgIFswLjMsIDAuNCwgMC4zXSxcbiAgICBbMC4yLCAwLjMsIDAuNV1cbl0pXG5tYXJrb3ZfZW50cm9weV9yYXRlKFAsIGJhc2U9MikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFbXBpcmljYWwgRW50cm9weSBSYXRlIG9mIFRleHQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNoYW5ub24gZmFtb3VzbHkgZXN0aW1hdGVkIEVuZ2xpc2ggdGV4dCBoYXMgYW4gZW50cm9weSByYXRlIG9mIGFib3V0IDEgYml0L2NoYXJhY3RlciB0aHJvdWdoIGh1bWFuIHByZWRpY3Rpb24gZXhwZXJpbWVudHMuIFdlIGNhbiBhcHByb3hpbWF0ZSB0aGlzIGNvbXB1dGF0aW9uYWxseSBieSBlc3RpbWF0aW5nIGNvbmRpdGlvbmFsIGVudHJvcHkgSChY4oKZfFjigpnigovigpYsLi4uLFjigpnigovigoEpIHVzaW5nIHNsaWRpbmcgd2luZG93cyBvZiBpbmNyZWFzaW5nIGNvbnRleHQgbGVuZ3RoIGsuIEFzIGsgZ3Jvd3MsIHRoZSBlc3RpbWF0ZSBhcHByb2FjaGVzIHRoZSB0cnVlIGVudHJvcHkgcmF0ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyLCBkZWZhdWx0ZGljdFxuZnJvbSBtYXRoIGltcG9ydCBsb2cyXG5mcm9tIHR5cGluZyBpbXBvcnQgRGljdCwgVHVwbGVcblxuZGVmIGVtcGlyaWNhbF9jb25kaXRpb25hbF9lbnRyb3B5KHRleHQ6IHN0ciwgY29udGV4dF9sZW46IGludCkgLVx1MDAzZSBmbG9hdDpcbiAgICBcIlwiXCJFc3RpbWF0ZSBIKFjigpkgfCBjb250ZXh0IG9mIGxlbmd0aCBjb250ZXh0X2xlbikgZnJvbSB0ZXh0LlxuXG4gICAgVXNlcyBtYXhpbXVtLWxpa2VsaWhvb2QgKGZyZXF1ZW5jeSkgZXN0aW1hdGVzIG9mIGNvbmRpdGlvbmFsIHByb2JhYmlsaXRpZXMuXG4gICAgUmV0dXJucyBlbnRyb3B5IGluIGJpdHMvY2hhcmFjdGVyLlxuICAgIFwiXCJcIlxuICAgIGlmIGNvbnRleHRfbGVuID09IDA6XG4gICAgICAgICMgTWFyZ2luYWwgZW50cm9weVxuICAgICAgICBjb3VudHMgPSBDb3VudGVyKHRleHQpXG4gICAgICAgIHRvdGFsID0gbGVuKHRleHQpXG4gICAgICAgIHByb2JzID0gbnAuYXJyYXkoW3YgLyB0b3RhbCBmb3IgdiBpbiBjb3VudHMudmFsdWVzKCldKVxuICAgICAgICByZXR1cm4gLW5wLnN1bShwcm9icyAqIG5wLmxvZzIocHJvYnMpKVxuXG4gICAgIyBDb3VudCB0cmFuc2l0aW9uczogY29udGV4dCDihpIgbmV4dF9jaGFyXG4gICAgY29udGV4dF9jb3VudHM6IERpY3Rbc3RyLCBpbnRdID0gZGVmYXVsdGRpY3QoaW50KVxuICAgIHRyYW5zaXRpb25fY291bnRzOiBEaWN0W1R1cGxlW3N0ciwgc3RyXSwgaW50XSA9IGRlZmF1bHRkaWN0KGludClcblxuICAgIGZvciBpIGluIHJhbmdlKGxlbih0ZXh0KSAtIGNvbnRleHRfbGVuKTpcbiAgICAgICAgY3R4ID0gdGV4dFtpOmkgKyBjb250ZXh0X2xlbl1cbiAgICAgICAgbnh0ID0gdGV4dFtpICsgY29udGV4dF9sZW5dXG4gICAgICAgIGNvbnRleHRfY291bnRzW2N0eF0gKz0gMVxuICAgICAgICB0cmFuc2l0aW9uX2NvdW50c1soY3R4LCBueHQpXSArPSAxXG5cbiAgICAjIEgoWHxjb250ZXh0KSA9IM6jX3tjdHh9IFAoY3R4KSBIKFh8Y3R4PWMpXG4gICAgdG90YWwgPSBzdW0oY29udGV4dF9jb3VudHMudmFsdWVzKCkpXG4gICAgaF9jb25kID0gMC4wXG4gICAgZm9yIGN0eCwgY3R4X2NvdW50IGluIGNvbnRleHRfY291bnRzLml0ZW1zKCk6XG4gICAgICAgIHBfY3R4ID0gY3R4X2NvdW50IC8gdG90YWxcbiAgICAgICAgIyBDb25kaXRpb25hbCBkaXN0cmlidXRpb24gb3ZlciBuZXh0IGNoYXJzXG4gICAgICAgIG5leHRfY2hhcnMgPSB7bnh0OiB0cmFuc2l0aW9uX2NvdW50c1soY3R4LCBueHQpXSBmb3Igbnh0IGluIHNldChjIGZvciAoYzIsIGMpIGluIHRyYW5zaXRpb25fY291bnRzIGlmIGMyID09IGN0eCl9XG4gICAgICAgIG5fY3R4ID0gc3VtKG5leHRfY2hhcnMudmFsdWVzKCkpXG4gICAgICAgIGhfY3R4ID0gLXN1bSgoYyAvIG5fY3R4KSAqIGxvZzIoYyAvIG5fY3R4KSBmb3IgYyBpbiBuZXh0X2NoYXJzLnZhbHVlcygpIGlmIGMgXHUwMDNlIDApXG4gICAgICAgIGhfY29uZCArPSBwX2N0eCAqIGhfY3R4XG5cbiAgICByZXR1cm4gaF9jb25kXG5cbiMgRG93bmxvYWQgYSBzbWFsbCBzYW1wbGUgb2YgdGV4dFxuc2FtcGxlID0gXCJcIlwidGhlIGVudHJvcHkgcmF0ZSBvZiBlbmdsaXNoIHRleHQgaXMgYXBwcm94aW1hdGVseSBvbmUgYml0IHBlciBjaGFyYWN0ZXJcbndoZW4gY29uZGl0aW9uaW5nIG9uIHN1ZmZpY2llbnQgY29udGV4dCB0aGlzIHdhcyBlc3RpbWF0ZWQgYnkgY2xhdWRlIHNoYW5ub25cbnVzaW5nIGh1bWFuIHByZWRpY3Rpb24gZXhwZXJpbWVudHMgaW4gdGhlIDE5NTBzIHRoZSByZXN1bHQgc2hvd3MgdGhhdCBlbmdsaXNoXG50ZXh0IGhhcyBlbm9ybW91cyByZWR1bmRhbmN5IGNvbXBhcmVkIHRvIHRoZSB0aGVvcmV0aWNhbCBtYXhpbXVtXCJcIlwiXG5cbnByaW50KFwiQ29udGV4dCBsZW5ndGgg4oaSIEVzdGltYXRlZCBIKFh8Y29udGV4dCkgW2JpdHMvY2hhcl1cIilcbmZvciBrIGluIFswLCAxLCAyLCAzLCA0XTpcbiAgICBoID0gZW1waXJpY2FsX2NvbmRpdGlvbmFsX2VudHJvcHkoc2FtcGxlLCBrKVxuICAgIHByaW50KGZcIiAgaz17a306IHtoOi40Zn0gYml0cy9jaGFyXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGFuZ3VhZ2UgTW9kZWwgUGVycGxleGl0eSBhbmQgRW50cm9weSBSYXRlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGxhbmd1YWdlIG1vZGVsIGFzc2lnbnMgcHJvYmFiaWxpdHkgcF9tb2RlbCh44oKBLC4uLix44oKZKSB0byBzZXF1ZW5jZXMuIFRoZSBjcm9zcy1lbnRyb3B5IG9mIHRoZSBtb2RlbCBvbiB0aGUgdHJ1ZSBkYXRhIGRpc3RyaWJ1dGlvbiBpczpcblxuSChwX3RydWUsIHBfbW9kZWwpID0gLUVfe3h+cF90cnVlfVtsb2cgcF9tb2RlbCh4KV1cblxuRm9yIGEgKnBlcmZlY3QqIG1vZGVsIChwX21vZGVsID0gcF90cnVlKSwgY3Jvc3MtZW50cm9weSBlcXVhbHMgdGhlIHRydWUgZW50cm9weSByYXRlLiBQZXJwbGV4aXR5IGlzIFBQTCA9IDJee2Nyb3NzLWVudHJvcHl9IOKAlCB0aGUgZ2VvbWV0cmljIG1lYW4gbnVtYmVyIG9mIGVxdWFsbHkgbGlrZWx5IGNob2ljZXMgdGhlIG1vZGVsIHNlZXMgYXQgZWFjaCB0b2tlbi4gQSBtb2RlbCBtYXRjaGluZyB0aGUgdHJ1ZSBlbnRyb3B5IHJhdGUgb2YgRW5nbGlzaCAofjEgYml0L2NoYXIg4omIIH4yLTMgYml0cy90b2tlbikgd291bGQgaGF2ZSBQUEwg4omIIDQtOCBvbiBjaGFyYWN0ZXItbGV2ZWwgdGFza3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXIsIEF1dG9Nb2RlbEZvckNhdXNhbExNXG5pbXBvcnQgdG9yY2hcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0XG5cbmRlZiBjb21wdXRlX2VudHJvcHlfcmF0ZV9hbmRfcGVycGxleGl0eShcbiAgICB0ZXh0czogTGlzdFtzdHJdLFxuICAgIG1vZGVsX25hbWU6IHN0ciA9IFwiZ3B0MlwiLFxuICAgIHN0cmlkZTogaW50ID0gNTEyXG4pIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJDb21wdXRlIHBlcnBsZXhpdHkgYW5kIGVzdGltYXRlIGVudHJvcHkgcmF0ZSBmcm9tIGFuIExMTS5cblxuICAgIFVzZXMgc3RyaWRlLWJhc2VkIGFwcHJvYWNoIHRvIGhhbmRsZSBsb25nIHRleHRzIHdpdGhvdXQgYm91bmRhcnkgYXJ0aWZhY3RzLlxuICAgIFwiXCJcIlxuICAgIHRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG4gICAgbW9kZWwgPSBBdXRvTW9kZWxGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSlcbiAgICBtb2RlbC5ldmFsKClcblxuICAgIHRvdGFsX2xvZ19wcm9iID0gMC4wXG4gICAgdG90YWxfdG9rZW5zID0gMFxuICAgIHRvdGFsX2NoYXJzID0gc3VtKGxlbih0KSBmb3IgdCBpbiB0ZXh0cylcblxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgdGV4dCBpbiB0ZXh0czpcbiAgICAgICAgICAgIGVuY29kaW5ncyA9IHRva2VuaXplcih0ZXh0LCByZXR1cm5fdGVuc29ycz1cInB0XCIpXG4gICAgICAgICAgICBpbnB1dF9pZHMgPSBlbmNvZGluZ3MuaW5wdXRfaWRzICAjIHNoYXBlICgxLCBUKVxuICAgICAgICAgICAgVCA9IGlucHV0X2lkcy5zaGFwZVsxXVxuICAgICAgICAgICAgbWF4X2xlbiA9IG1vZGVsLmNvbmZpZy5uX3Bvc2l0aW9uc1xuXG4gICAgICAgICAgICBmb3IgYmVnaW4gaW4gcmFuZ2UoMCwgVCwgc3RyaWRlKTpcbiAgICAgICAgICAgICAgICBlbmQgPSBtaW4oYmVnaW4gKyBtYXhfbGVuLCBUKVxuICAgICAgICAgICAgICAgIHRndF9iZWdpbiA9IG1heChiZWdpbiwgYmVnaW4gKyBtYXhfbGVuIC0gc3RyaWRlKSAgIyBvbmx5IHNjb3JlIG5ldyB0b2tlbnNcbiAgICAgICAgICAgICAgICBjaHVuayA9IGlucHV0X2lkc1s6LCBiZWdpbjplbmRdXG4gICAgICAgICAgICAgICAgdGFyZ2V0X2xlbiA9IGVuZCAtIHRndF9iZWdpblxuXG4gICAgICAgICAgICAgICAgb3V0cHV0cyA9IG1vZGVsKGNodW5rLCBsYWJlbHM9Y2h1bmspXG4gICAgICAgICAgICAgICAgIyBvdXRwdXRzLmxvc3MgaXMgbWVhbiBOTEwgb3ZlciBhbGwgdG9rZW5zIGluIGNodW5rXG4gICAgICAgICAgICAgICAgIyBXZSBuZWVkIHRvIHdlaWdodCBieSB0YXJnZXQgdG9rZW5zIG9ubHkg4oCUIHNpbXBsaWZpZWQgaGVyZVxuICAgICAgICAgICAgICAgIGxvZ19wcm9iID0gLW91dHB1dHMubG9zcy5pdGVtKCkgKiAoZW5kIC0gYmVnaW4pXG4gICAgICAgICAgICAgICAgdG90YWxfbG9nX3Byb2IgKz0gbG9nX3Byb2IgKiAodGFyZ2V0X2xlbiAvIChlbmQgLSBiZWdpbikpXG4gICAgICAgICAgICAgICAgdG90YWxfdG9rZW5zICs9IHRhcmdldF9sZW5cblxuICAgIGNyb3NzX2VudHJvcHlfYml0cyA9IC10b3RhbF9sb2dfcHJvYiAvIHRvdGFsX3Rva2VucyAvIG5wLmxvZygyKVxuICAgIHBwbCA9IDIgKiogY3Jvc3NfZW50cm9weV9iaXRzXG4gICAgYXZnX2NoYXJzX3Blcl90b2tlbiA9IHRvdGFsX2NoYXJzIC8gdG90YWxfdG9rZW5zXG4gICAgYnBiID0gY3Jvc3NfZW50cm9weV9iaXRzIC8gYXZnX2NoYXJzX3Blcl90b2tlbiAgIyBiaXRzLXBlci1ieXRlXG5cbiAgICByZXR1cm4ge1xuICAgICAgICBcImNyb3NzX2VudHJvcHlfYml0c19wZXJfdG9rZW5cIjogY3Jvc3NfZW50cm9weV9iaXRzLFxuICAgICAgICBcInBlcnBsZXhpdHlcIjogcHBsLFxuICAgICAgICBcImJpdHNfcGVyX2J5dGVcIjogYnBiLFxuICAgICAgICBcImVudHJvcHlfcmF0ZV9lc3RpbWF0ZV9iaXRzX3Blcl9jaGFyXCI6IGJwYlxuICAgIH1cblxuIyBVc2FnZSAocmVxdWlyZXMgdHJhbnNmb3JtZXJzICsgYSBkb3dubG9hZGVkIG1vZGVsKVxuIyByZXN1bHRzID0gY29tcHV0ZV9lbnRyb3B5X3JhdGVfYW5kX3BlcnBsZXhpdHkoW1wiZXhhbXBsZSB0ZXh0IGhlcmVcIl0pXG4jIHByaW50KHJlc3VsdHMpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGVtcGVsLVppdiBDb21wbGV4aXR5IGFuZCBFbnRyb3B5IFJhdGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBMZW1wZWwtWml2IGFsZ29yaXRobSAoTFo3Ny9MWjc4KSBpcyBhIHVuaXZlcnNhbCBkYXRhIGNvbXByZXNzb3I6IHdpdGhvdXQga25vd2luZyB0aGUgc291cmNlIHN0YXRpc3RpY3MsIGl0IGNvbnZlcmdlcyB0byB0aGUgZW50cm9weSByYXRlIGFzIHNlcXVlbmNlIGxlbmd0aCBpbmNyZWFzZXMuIFRoaXMgbWFrZXMgY29tcHJlc3Npb24gcmF0aW8gYSBtb2RlbC1mcmVlIGVzdGltYXRvciBvZiBlbnRyb3B5IHJhdGUuIFRoZSBMWjc2IGNvbXBsZXhpdHkgYyh4KSBvZiBhIHN0cmluZyB4IGdyb3dzIGFzIGMoeCkgfiBuLyhsb2cgbikgwrcgaCwgd2hlcmUgaCBpcyB0aGUgZW50cm9weSByYXRlLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJCaXRzLXBlci1CeXRlIChCUEIpIGFzIGEgVW5pdmVyc2FsIE1ldHJpYyIsImNvbnRlbnQiOiJCUEIgPSBsb2figoIoUFBMKSAvIGF2Z19jaGFyc19wZXJfdG9rZW4gbWFrZXMgcGVycGxleGl0eSBjb21wYXJhYmxlIGFjcm9zcyBtb2RlbHMgd2l0aCBkaWZmZXJlbnQgdG9rZW5pemVycy4gR1BULTQgdG9rZW5pemVyIHByb2R1Y2VzIH40IGNoYXJzL3Rva2VuIHdoaWxlIExMYU1BIFNlbnRlbmNlUGllY2UgcHJvZHVjZXMgfjMuNSBjaGFycy90b2tlbiDigJQgc28gcmF3IFBQTCBudW1iZXJzIGFyZSBpbmNvbXBhcmFibGUsIGJ1dCBCUEIgdmFsdWVzIGFyZSBkaXJlY3RseSBjb21wYXJhYmxlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgZ3ppcFxuaW1wb3J0IHpsaWJcbmltcG9ydCBiejJcbmltcG9ydCBsem1hXG5pbXBvcnQgc3RydWN0XG5mcm9tIHR5cGluZyBpbXBvcnQgRGljdFxuXG5kZWYgY29tcHJlc3Npb25fdnNfZW50cm9weV9ib3VuZChcbiAgICB0ZXh0OiBzdHIsXG4gICAgZW50cm9weV9yYXRlX2JpdHNfcGVyX2NoYXI6IGZsb2F0XG4pIC1cdTAwM2UgRGljdFtzdHIsIGRpY3RdOlxuICAgIFwiXCJcIkNvbXBhcmUgYWN0dWFsIGNvbXByZXNzaW9uIHJhdGlvcyB2cyB0aGUgZW50cm9weSByYXRlIGxvd2VyIGJvdW5kLlxuXG4gICAgU2hhbm5vblx1MDAyN3Mgc291cmNlIGNvZGluZyB0aGVvcmVtIHNheXMgdGhlIGJlc3QgbG9zc2xlc3MgY29tcHJlc3NvclxuICAgIGFjaGlldmVzIGV4YWN0bHkgaCBiaXRzL2NoYXIuIFdlIGNvbXBhcmUgc3RhbmRhcmQgYWxnb3JpdGhtcyB0byB0aGlzIGJvdW5kLlxuXG4gICAgQXJnczpcbiAgICAgICAgdGV4dDogSW5wdXQgdGV4dCB0byBjb21wcmVzcy5cbiAgICAgICAgZW50cm9weV9yYXRlX2JpdHNfcGVyX2NoYXI6IEVzdGltYXRlZCBlbnRyb3B5IHJhdGUgKGUuZy4sIDEuMCBmb3IgRW5nbGlzaCkuXG4gICAgUmV0dXJuczpcbiAgICAgICAgRGljdCB3aXRoIGNvbXByZXNzaW9uIHN0YXRpc3RpY3MgcGVyIG1ldGhvZC5cbiAgICBcIlwiXCJcbiAgICBkYXRhID0gdGV4dC5lbmNvZGUoXHUwMDI3dXRmLThcdTAwMjcpXG4gICAgb3JpZ2luYWxfYnl0ZXMgPSBsZW4oZGF0YSlcbiAgICBvcmlnaW5hbF9iaXRzX3Blcl9jaGFyID0gOC4wICAjIFVURi04IGJhc2VsaW5lOiA4IGJpdHMvY2hhciAoQVNDSUkgY2hhcnMpXG5cbiAgICBtZXRob2RzID0ge1xuICAgICAgICBcdTAwMjdnemlwLTEgKGZhc3QpXHUwMDI3OiBnemlwLmNvbXByZXNzKGRhdGEsIGNvbXByZXNzbGV2ZWw9MSksXG4gICAgICAgIFx1MDAyN2d6aXAtOSAoYmVzdClcdTAwMjc6IGd6aXAuY29tcHJlc3MoZGF0YSwgY29tcHJlc3NsZXZlbD05KSxcbiAgICAgICAgXHUwMDI3emxpYi02IChkZWZhdWx0KVx1MDAyNzogemxpYi5jb21wcmVzcyhkYXRhLCBsZXZlbD02KSxcbiAgICAgICAgXHUwMDI3YnoyIChibG9jaylcdTAwMjc6IGJ6Mi5jb21wcmVzcyhkYXRhKSxcbiAgICAgICAgXHUwMDI3bHptYSAoeHopXHUwMDI3OiBsem1hLmNvbXByZXNzKGRhdGEpLFxuICAgIH1cblxuICAgIGVudHJvcHlfYm91bmRfYnl0ZXMgPSBsZW4odGV4dCkgKiBlbnRyb3B5X3JhdGVfYml0c19wZXJfY2hhciAvIDguMFxuICAgIHByaW50KGZcIk9yaWdpbmFsIHRleHQ6IHtsZW4odGV4dCl9IGNoYXJzLCB7b3JpZ2luYWxfYnl0ZXN9IGJ5dGVzXCIpXG4gICAgcHJpbnQoZlwiRW50cm9weSBib3VuZCBAIGg9e2VudHJvcHlfcmF0ZV9iaXRzX3Blcl9jaGFyfSBiL2NoYXI6IHtlbnRyb3B5X2JvdW5kX2J5dGVzOi4xZn0gYnl0ZXNcIilcbiAgICBwcmludChmXCJcXG57XHUwMDI3TWV0aG9kXHUwMDI3Olx1MDAzYzIwfSB7XHUwMDI3Q29tcHJlc3NlZFx1MDAyNzpcdTAwM2UxMn0ge1x1MDAyN0JpdHMvY2hhclx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN3ZzIGJvdW5kXHUwMDI3Olx1MDAzZTEwfVwiKVxuICAgIHByaW50KFwiLVwiICogNTUpXG5cbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgbmFtZSwgY29tcHJlc3NlZCBpbiBtZXRob2RzLml0ZW1zKCk6XG4gICAgICAgIG5fYnl0ZXMgPSBsZW4oY29tcHJlc3NlZClcbiAgICAgICAgYml0c19wZXJfY2hhciA9IChuX2J5dGVzICogOCkgLyBsZW4odGV4dClcbiAgICAgICAgZ2FwX3BjdCA9IDEwMCAqIChiaXRzX3Blcl9jaGFyIC0gZW50cm9weV9yYXRlX2JpdHNfcGVyX2NoYXIpIC8gZW50cm9weV9yYXRlX2JpdHNfcGVyX2NoYXJcbiAgICAgICAgcHJpbnQoZlwie25hbWU6XHUwMDNjMjB9IHtuX2J5dGVzOlx1MDAzZTEyfSB7Yml0c19wZXJfY2hhcjpcdTAwM2UxMC4zZn0ge2dhcF9wY3Q6XHUwMDNlKzkuMWZ9JVwiKVxuICAgICAgICByZXN1bHRzW25hbWVdID0ge1x1MDAyN2NvbXByZXNzZWRfYnl0ZXNcdTAwMjc6IG5fYnl0ZXMsIFx1MDAyN2JpdHNfcGVyX2NoYXJcdTAwMjc6IGJpdHNfcGVyX2NoYXJ9XG5cbiAgICByZXR1cm4gcmVzdWx0c1xuXG4jIEVuZ2xpc2ggdGV4dCBzYW1wbGUgKGVudHJvcHkgcmF0ZSDiiYggMS4wLTEuMyBiaXRzL2NoYXIgZW1waXJpY2FsbHkpXG5zYW1wbGUgPSAoXCJ0aGUgcXVpY2sgYnJvd24gZm94IGp1bXBzIG92ZXIgdGhlIGxhenkgZG9nIFwiICogNTAgK1xuICAgICAgICAgIFwiaW5mb3JtYXRpb24gdGhlb3J5IGFuZCBlbnRyb3B5IHJhdGUgb2YgZW5nbGlzaCBcIiAqIDMwKVxuY29tcHJlc3Npb25fdnNfZW50cm9weV9ib3VuZChzYW1wbGUsIGVudHJvcHlfcmF0ZV9iaXRzX3Blcl9jaGFyPTEuMikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTb3VyY2UgQ29kaW5nIFRoZW9yZW0gQ29ubmVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2hhbm5vblx1MDAyN3Mgc291cmNlIGNvZGluZyB0aGVvcmVtIHN0YXRlcyB0aGF0IGZvciBhIHN0YXRpb25hcnkgZXJnb2RpYyBzb3VyY2Ugd2l0aCBlbnRyb3B5IHJhdGUgaCwgdGhlIG9wdGltYWwgbG9zc2xlc3MgY29tcHJlc3Npb24gYWNoaWV2ZXMgZXhhY3RseSBoIGJpdHMvc3ltYm9sIOKAlCBubyBtb3JlLCBubyBsZXNzLiBBbnkgY29kZSBhY2hpZXZpbmcgZmV3ZXIgdGhhbiBoIGJpdHMvc3ltYm9sIG11c3QgaGF2ZSBub24temVybyBlcnJvciBwcm9iYWJpbGl0eTsgYW55IGNvZGUgdXNpbmcgbW9yZSB0aGFuIGggYml0cy9zeW1ib2wgaXMgd2FzdGluZyBjYXBhY2l0eS4gVGhpcyBpcyB3aHkgZW50cm9weSByYXRlIGlzIGJvdGggYSB0aGVvcmV0aWNhbCBsaW1pdCBhbmQgYSBwcmFjdGljYWwgYmVuY2htYXJrIGZvciBjb21wcmVzc2lvbiBhbGdvcml0aG1zIGFuZCBsYW5ndWFnZSBtb2RlbHMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW50cm9weSByYXRlIGlzIHRoZSBmaW5nZXJwcmludCBvZiBhIHN0b2NoYXN0aWMgcHJvY2VzczogaS5pLmQuIHNvdXJjZXMgaGF2ZSBtYXhpbXVtIGVudHJvcHkgcmF0ZSAobm8gZXhwbG9pdGFibGUgcGF0dGVybnMpLCB3aGlsZSBzdHJ1Y3R1cmVkIHByb2Nlc3NlcyBsaWtlIG5hdHVyYWwgbGFuZ3VhZ2UgaGF2ZSByYXRlcyBmYXIgYmVsb3cgdGhlIGFscGhhYmV0IG1heGltdW0uIExhbmd1YWdlIG1vZGVsIHBlcnBsZXhpdHkgaXMgdGhlIGVtcGlyaWNhbCBlbnRyb3B5IHJhdGUgb2YgdGhlIG1vZGVsXHUwMDI3cyBkaXN0cmlidXRpb24gb24gYSB0ZXN0IGNvcnB1cyDigJQgbWluaW1pemluZyBpdCBpcyBlcXVpdmFsZW50IHRvIGZpbmRpbmcgYSBtb2RlbCB3aG9zZSBkaXN0cmlidXRpb24gbWF0Y2hlcyB0aGUgdHJ1ZSBkYXRhIGRpc3RyaWJ1dGlvbiBhcyBjbG9zZWx5IGFzIHBvc3NpYmxlLiJ9XQ=="
---
# Entropy Rate and Information in Sequences

A single random variable has entropy H(X). But real-world data — text, audio, time series — is a *sequence* of random variables with temporal structure. The entropy rate captures how much genuine uncertainty exists per symbol once we account for all the patterns and dependencies in the sequence.

## Definition of Entropy Rate

For a stochastic process {Xₙ}, the entropy rate is defined as the limit:

h = lim_{n→∞} (1/n) H(X₁, X₂, ..., Xₙ)

provided the limit exists. For a *stationary* process, this limit always exists and equals the conditional entropy rate:

h = lim_{n→∞} H(Xₙ | X_{n-1}, ..., X₁)

The conditional form says: as we observe more context, the per-symbol uncertainty decreases monotonically and converges to h.

> **Why the Limit Exists for Stationary Processes**: For a stationary process, H(Xₙ|X_{n-1},...,X₁) is non-increasing in n (more context never increases entropy) and bounded below by 0. By the monotone convergence theorem the limit exists. This is a consequence of the chain rule and sub-additivity of entropy.

## Special Cases and Examples

| Process Type | Entropy Rate Formula | Example | Rate (bits/symbol) |
| --- | --- | --- | --- |
| i.i.d. uniform binary | H(X₁) = log₂(2) = 1 | Fair coin flips | 1.0 |
| i.i.d. biased binary | H(X₁) = −p log p − (1−p) log(1−p) | Biased coin (p=0.1) | ≈ 0.47 |
| i.i.d. uniform over alphabet A | log₂(|A|) | Uniform die rolls (6-sided) | ≈ 2.58 |
| First-order Markov chain | −Σᵢ πᵢ Σⱼ Pᵢⱼ log Pᵢⱼ | Weather model | < H(X₁) |
| Natural English text | Shannon experiment estimate | Written English | ≈ 1.0–1.3 |
| Random (incompressible) | H(X₁) = max entropy | True random bits | = log₂(|A|) |

## Entropy Rate of a Markov Chain

For an ergodic, time-homogeneous Markov chain with transition matrix P and stationary distribution π, the entropy rate has a closed form:

h = −Σᵢ πᵢ Σⱼ Pᵢⱼ log Pᵢⱼ = Σᵢ πᵢ H(Xₙ | Xₙ₋₁=i)

This is the stationary-distribution-weighted average of the conditional entropy at each state. A highly predictable chain (near-deterministic transitions) has h ≈ 0; a fully random chain has h = log|A|.

```python
import numpy as np
from scipy.linalg import eig

def markov_entropy_rate(P: np.ndarray, base: float = 2.0) -> float:
    """Compute entropy rate of a finite ergodic Markov chain.

    Args:
        P: Transition matrix, shape (n_states, n_states). Rows sum to 1.
        base: Logarithm base (2 = bits, e = nats).
    Returns:
        Entropy rate h in specified units.
    """
    n = P.shape[0]
    assert np.allclose(P.sum(axis=1), 1.0), "Rows must sum to 1"

    # Stationary distribution: left eigenvector for eigenvalue 1
    # Equivalently, solve π P = π with Σ πᵢ = 1
    eigenvalues, eigenvectors = eig(P.T)
    stationary_idx = np.argmin(np.abs(eigenvalues - 1.0))
    pi = np.real(eigenvectors[:, stationary_idx])
    pi = pi / pi.sum()  # normalize

    # Compute h = -Σᵢ πᵢ Σⱼ Pᵢⱼ log Pᵢⱼ
    log_fn = np.log if base == np.e else (lambda x: np.log(x) / np.log(base))
    row_entropies = np.array([
        -np.sum(P[i, P[i] > 0] * log_fn(P[i, P[i] > 0]))
        for i in range(n)
    ])
    h = np.dot(pi, row_entropies)

    print(f"Stationary distribution π: {pi}")
    print(f"Per-state conditional entropies: {row_entropies}")
    print(f"Entropy rate h = {h:.6f} {'bits' if base==2 else 'nats'}/symbol")
    return h

# Example: 3-state weather Markov chain
#   States: 0=sunny, 1=cloudy, 2=rainy
P = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])
markov_entropy_rate(P, base=2)
```

## Empirical Entropy Rate of Text

Shannon famously estimated English text has an entropy rate of about 1 bit/character through human prediction experiments. We can approximate this computationally by estimating conditional entropy H(Xₙ|Xₙ₋ₖ,...,Xₙ₋₁) using sliding windows of increasing context length k. As k grows, the estimate approaches the true entropy rate.

```python
import numpy as np
from collections import Counter, defaultdict
from math import log2
from typing import Dict, Tuple

def empirical_conditional_entropy(text: str, context_len: int) -> float:
    """Estimate H(Xₙ | context of length context_len) from text.

    Uses maximum-likelihood (frequency) estimates of conditional probabilities.
    Returns entropy in bits/character.
    """
    if context_len == 0:
        # Marginal entropy
        counts = Counter(text)
        total = len(text)
        probs = np.array([v / total for v in counts.values()])
        return -np.sum(probs * np.log2(probs))

    # Count transitions: context → next_char
    context_counts: Dict[str, int] = defaultdict(int)
    transition_counts: Dict[Tuple[str, str], int] = defaultdict(int)

    for i in range(len(text) - context_len):
        ctx = text[i:i + context_len]
        nxt = text[i + context_len]
        context_counts[ctx] += 1
        transition_counts[(ctx, nxt)] += 1

    # H(X|context) = Σ_{ctx} P(ctx) H(X|ctx=c)
    total = sum(context_counts.values())
    h_cond = 0.0
    for ctx, ctx_count in context_counts.items():
        p_ctx = ctx_count / total
        # Conditional distribution over next chars
        next_chars = {nxt: transition_counts[(ctx, nxt)] for nxt in set(c for (c2, c) in transition_counts if c2 == ctx)}
        n_ctx = sum(next_chars.values())
        h_ctx = -sum((c / n_ctx) * log2(c / n_ctx) for c in next_chars.values() if c > 0)
        h_cond += p_ctx * h_ctx

    return h_cond

# Download a small sample of text
sample = """the entropy rate of english text is approximately one bit per character
when conditioning on sufficient context this was estimated by claude shannon
using human prediction experiments in the 1950s the result shows that english
text has enormous redundancy compared to the theoretical maximum"""

print("Context length → Estimated H(X|context) [bits/char]")
for k in [0, 1, 2, 3, 4]:
    h = empirical_conditional_entropy(sample, k)
    print(f"  k={k}: {h:.4f} bits/char")
```

## Language Model Perplexity and Entropy Rate

A language model assigns probability p_model(x₁,...,xₙ) to sequences. The cross-entropy of the model on the true data distribution is:

H(p_true, p_model) = -E_{x~p_true}[log p_model(x)]

For a *perfect* model (p_model = p_true), cross-entropy equals the true entropy rate. Perplexity is PPL = 2^{cross-entropy} — the geometric mean number of equally likely choices the model sees at each token. A model matching the true entropy rate of English (~1 bit/char ≈ ~2-3 bits/token) would have PPL ≈ 4-8 on character-level tasks.

```python
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from typing import List

def compute_entropy_rate_and_perplexity(
    texts: List[str],
    model_name: str = "gpt2",
    stride: int = 512
) -> dict:
    """Compute perplexity and estimate entropy rate from an LLM.

    Uses stride-based approach to handle long texts without boundary artifacts.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()

    total_log_prob = 0.0
    total_tokens = 0
    total_chars = sum(len(t) for t in texts)

    with torch.no_grad():
        for text in texts:
            encodings = tokenizer(text, return_tensors="pt")
            input_ids = encodings.input_ids  # shape (1, T)
            T = input_ids.shape[1]
            max_len = model.config.n_positions

            for begin in range(0, T, stride):
                end = min(begin + max_len, T)
                tgt_begin = max(begin, begin + max_len - stride)  # only score new tokens
                chunk = input_ids[:, begin:end]
                target_len = end - tgt_begin

                outputs = model(chunk, labels=chunk)
                # outputs.loss is mean NLL over all tokens in chunk
                # We need to weight by target tokens only — simplified here
                log_prob = -outputs.loss.item() * (end - begin)
                total_log_prob += log_prob * (target_len / (end - begin))
                total_tokens += target_len

    cross_entropy_bits = -total_log_prob / total_tokens / np.log(2)
    ppl = 2 ** cross_entropy_bits
    avg_chars_per_token = total_chars / total_tokens
    bpb = cross_entropy_bits / avg_chars_per_token  # bits-per-byte

    return {
        "cross_entropy_bits_per_token": cross_entropy_bits,
        "perplexity": ppl,
        "bits_per_byte": bpb,
        "entropy_rate_estimate_bits_per_char": bpb
    }

# Usage (requires transformers + a downloaded model)
# results = compute_entropy_rate_and_perplexity(["example text here"])
# print(results)
```

## Lempel-Ziv Complexity and Entropy Rate

The Lempel-Ziv algorithm (LZ77/LZ78) is a universal data compressor: without knowing the source statistics, it converges to the entropy rate as sequence length increases. This makes compression ratio a model-free estimator of entropy rate. The LZ76 complexity c(x) of a string x grows as c(x) ~ n/(log n) · h, where h is the entropy rate.

> **Bits-per-Byte (BPB) as a Universal Metric**: BPB = log₂(PPL) / avg_chars_per_token makes perplexity comparable across models with different tokenizers. GPT-4 tokenizer produces ~4 chars/token while LLaMA SentencePiece produces ~3.5 chars/token — so raw PPL numbers are incomparable, but BPB values are directly comparable.

```python
import gzip
import zlib
import bz2
import lzma
import struct
from typing import Dict

def compression_vs_entropy_bound(
    text: str,
    entropy_rate_bits_per_char: float
) -> Dict[str, dict]:
    """Compare actual compression ratios vs the entropy rate lower bound.

    Shannon's source coding theorem says the best lossless compressor
    achieves exactly h bits/char. We compare standard algorithms to this bound.

    Args:
        text: Input text to compress.
        entropy_rate_bits_per_char: Estimated entropy rate (e.g., 1.0 for English).
    Returns:
        Dict with compression statistics per method.
    """
    data = text.encode('utf-8')
    original_bytes = len(data)
    original_bits_per_char = 8.0  # UTF-8 baseline: 8 bits/char (ASCII chars)

    methods = {
        'gzip-1 (fast)': gzip.compress(data, compresslevel=1),
        'gzip-9 (best)': gzip.compress(data, compresslevel=9),
        'zlib-6 (default)': zlib.compress(data, level=6),
        'bz2 (block)': bz2.compress(data),
        'lzma (xz)': lzma.compress(data),
    }

    entropy_bound_bytes = len(text) * entropy_rate_bits_per_char / 8.0
    print(f"Original text: {len(text)} chars, {original_bytes} bytes")
    print(f"Entropy bound @ h={entropy_rate_bits_per_char} b/char: {entropy_bound_bytes:.1f} bytes")
    print(f"\n{'Method':<20} {'Compressed':>12} {'Bits/char':>10} {'vs bound':>10}")
    print("-" * 55)

    results = {}
    for name, compressed in methods.items():
        n_bytes = len(compressed)
        bits_per_char = (n_bytes * 8) / len(text)
        gap_pct = 100 * (bits_per_char - entropy_rate_bits_per_char) / entropy_rate_bits_per_char
        print(f"{name:<20} {n_bytes:>12} {bits_per_char:>10.3f} {gap_pct:>+9.1f}%")
        results[name] = {'compressed_bytes': n_bytes, 'bits_per_char': bits_per_char}

    return results

# English text sample (entropy rate ≈ 1.0-1.3 bits/char empirically)
sample = ("the quick brown fox jumps over the lazy dog " * 50 +
          "information theory and entropy rate of english " * 30)
compression_vs_entropy_bound(sample, entropy_rate_bits_per_char=1.2)
```

## Source Coding Theorem Connection

Shannon's source coding theorem states that for a stationary ergodic source with entropy rate h, the optimal lossless compression achieves exactly h bits/symbol — no more, no less. Any code achieving fewer than h bits/symbol must have non-zero error probability; any code using more than h bits/symbol is wasting capacity. This is why entropy rate is both a theoretical limit and a practical benchmark for compression algorithms and language models.

---

Entropy rate is the fingerprint of a stochastic process: i.i.d. sources have maximum entropy rate (no exploitable patterns), while structured processes like natural language have rates far below the alphabet maximum. Language model perplexity is the empirical entropy rate of the model's distribution on a test corpus — minimizing it is equivalent to finding a model whose distribution matches the true data distribution as closely as possible.

