---
title: "K-Means Convergence — Monotone Decrease and Local Optima"
slug: "k-means-convergence"
description: "Prove that Lloyd's algorithm converges in finite steps via monotone WCSS decrease, understand why convergence is to a local not global minimum, quantify the O(log k) approximation from k-means++ initialization, and demonstrate pathological cases where k-means gets stuck."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSy1tZWFucyBpcyBndWFyYW50ZWVkIHRvIGNvbnZlcmdlLCBidXQgb25seSB0byBhIGxvY2FsIG1pbmltdW0gb2YgdGhlIFdpdGhpbi1DbHVzdGVyIFN1bSBvZiBTcXVhcmVzLiBUaGlzIG5vdGUgcHJvdmVzIHRoZSBjb252ZXJnZW5jZSBhcmd1bWVudCByaWdvcm91c2x5LCBkZW1vbnN0cmF0ZXMgaG93IHBvb3IgaW5pdGlhbGl6YXRpb24gbGVhZHMgdG8gYmFkIGxvY2FsIG9wdGltYSwgYW5kIHNob3dzIHdoeSBrLW1lYW5zKysgYW5kIG11bHRpcGxlIHJlc3RhcnRzIGFyZSBlc3NlbnRpYWwgZm9yIHJlbGlhYmxlIHJlc3VsdHMuIFVuZGVyc3RhbmRpbmcgY29udmVyZ2VuY2UgYmVoYXZpb3IgaGVscHMgcHJhY3RpdGlvbmVycyBkZWNpZGUgaG93IG1hbnkgcmVzdGFydHMgdG8gdXNlIGFuZCB3aGVuIHRvIHRydXN0IHRoZSBmaW5hbCBjbHVzdGVyaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldDU1MgYXMgdGhlIENvbnZlcmdlbmNlIENyaXRlcmlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG9iamVjdGl2ZSBXQ1NTID0gzqPhtaIgzqNfe3jiiIhD4bWifSDigJZ4IOKIkiDOvOG1ouKAlsKyIGlzIGJvdW5kZWQgYmVsb3cgYnkgemVybyAoZGlzdGFuY2VzIGFyZSBub24tbmVnYXRpdmUpLiBBdCBpbml0aWFsaXphdGlvbiwgV0NTUyBoYXMgc29tZSBmaW5pdGUgdmFsdWUgZGV0ZXJtaW5lZCBieSB0aGUgaW5pdGlhbCBjZW50cm9pZHMuIFRoZSBjb252ZXJnZW5jZSBhcmd1bWVudCBpczogaWYgV0NTUyBjYW5ub3QgaW5jcmVhc2UgYXQgYW55IHN0ZXAgYW5kIGl0IGlzIGJvdW5kZWQgYmVsb3csIGl0IG11c3QgY29udmVyZ2UuIFRoZSBrZXkgaXMgc2hvd2luZyB0aGF0IGVhY2ggb2YgdGhlIHR3byBzdGVwcyDigJQgRS1zdGVwIGFuZCBNLXN0ZXAg4oCUIGlzIG5vbi1pbmNyZWFzaW5nLiBTaW5jZSB0aGVyZSBhcmUgZmluaXRlbHkgbWFueSBwYXJ0aXRpb25zIG9mIG4gcG9pbnRzIGludG8gayBsYWJlbGVkIGNsdXN0ZXJzIChhdCBtb3N0IGvigb8pLCBXQ1NTIGNhbiBkZWNyZWFzZSBvbmx5IGZpbml0ZWx5IG1hbnkgdGltZXMgYmVmb3JlIHJlYWNoaW5nIGEgZml4ZWQgcG9pbnQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IEVhY2ggU3RlcCBEZWNyZWFzZXMgV0NTUyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRS1zdGVwIChhc3NpZ25tZW50KTogZm9yIGZpeGVkIGNlbnRyb2lkcyDOvOKCgSwuLi4szrzigpYsIGFzc2lnbmluZyBlYWNoIHBvaW50IHggdG8gaXRzIG5lYXJlc3QgY2VudHJvaWQgYXJnIG1pbl9pIOKAlnjiiJLOvOG1ouKAlsKyIGlzIGV4YWN0bHkgbWluaW1pemluZyB0aGUgV0NTUyBjb250cmlidXRpb24gb2YgeC4gQW55IHJlYXNzaWdubWVudCB0byBhIGZhcnRoZXIgY2VudHJvaWQgd291bGQgc3RyaWN0bHkgaW5jcmVhc2UgV0NTUy4gVGhlcmVmb3JlIHRoZSBFLXN0ZXAgY2Fubm90IGluY3JlYXNlIFdDU1MgYW5kIHdpbGwgZGVjcmVhc2UgaXQgd2hlbmV2ZXIgYW55IHBvaW50IGlzIGNsb3NlciB0byBhIGRpZmZlcmVudCBjZW50cm9pZC4gTS1zdGVwICh1cGRhdGUpOiBmb3IgZml4ZWQgYXNzaWdubWVudHMsIHRoZSBjZW50cm9pZCB0aGF0IG1pbmltaXplcyDOo197eOKIiEPhtaJ9IOKAlnjiiJLOvOKAlsKyIG92ZXIgzrwgaXMgZXhhY3RseSB0aGUgbWVhbiDOvOG1oiA9ICgxL3xD4bWifCnOo197eOKIiEPhtaJ9IHguIFRoaXMgZm9sbG93cyBiZWNhdXNlIOKIh1/OvCDOoyDigJZ44oiSzrzigJbCsiA9IOKIkjLOoyh44oiSzrwpID0gMCBpbXBsaWVzIM68ID0gbWVhbihD4bWiKS4gQW55IG90aGVyIGNlbnRyb2lkIHBvc2l0aW9uIGdpdmVzIHN0cmljdGx5IGhpZ2hlciBXQ1NTLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNylcblgsIF8gPSBtYWtlX2Jsb2JzKG5fc2FtcGxlcz0zMDAsIGNlbnRlcnM9NCwgY2x1c3Rlcl9zdGQ9MC45LCByYW5kb21fc3RhdGU9NDIpXG5rID0gNFxuXG4jIFJhbmRvbSBpbml0aWFsaXphdGlvbiB0byBtYWtlIGNvbnZlcmdlbmNlIHRyYWNraW5nIGludGVyZXN0aW5nXG5jZW50ZXJzID0gWFtybmcuY2hvaWNlKGxlbihYKSwgaywgcmVwbGFjZT1GYWxzZSldLmNvcHkoKVxuXG53Y3NzX2hpc3RvcnkgPSBbXVxuZm9yIGl0ZXJhdGlvbiBpbiByYW5nZSg1MCk6XG4gICAgIyBFLXN0ZXBcbiAgICBkaWZmcyA9IFhbOiwgTm9uZSwgOl0gLSBjZW50ZXJzW05vbmUsIDosIDpdXG4gICAgbGFiZWxzID0gbnAuYXJnbWluKChkaWZmcyAqKiAyKS5zdW0oYXhpcz0yKSwgYXhpcz0xKVxuICAgICMgQ29tcHV0ZSBXQ1NTIGFmdGVyIEUtc3RlcFxuICAgIHdjc3NfZSA9IHN1bShucC5zdW0oKFhbbGFiZWxzID09IGldIC0gY2VudGVyc1tpXSkgKiogMikgZm9yIGkgaW4gcmFuZ2UoaykpXG4gICAgd2Nzc19oaXN0b3J5LmFwcGVuZCgoXHUwMDI3RVx1MDAyNywgaXRlcmF0aW9uLCB3Y3NzX2UpKVxuICAgICMgTS1zdGVwXG4gICAgbmV3X2NlbnRlcnMgPSBucC5hcnJheShbWFtsYWJlbHMgPT0gaV0ubWVhbihheGlzPTApIGZvciBpIGluIHJhbmdlKGspXSlcbiAgICB3Y3NzX20gPSBzdW0obnAuc3VtKChYW2xhYmVscyA9PSBpXSAtIG5ld19jZW50ZXJzW2ldKSAqKiAyKSBmb3IgaSBpbiByYW5nZShrKSlcbiAgICB3Y3NzX2hpc3RvcnkuYXBwZW5kKChcdTAwMjdNXHUwMDI3LCBpdGVyYXRpb24sIHdjc3NfbSkpXG4gICAgYXNzZXJ0IHdjc3NfbSBcdTAwM2M9IHdjc3NfZSArIDFlLTksIFwiTS1zdGVwIGluY3JlYXNlZCBXQ1NTIVwiXG4gICAgaWYgbnAubWF4KG5wLmxpbmFsZy5ub3JtKG5ld19jZW50ZXJzIC0gY2VudGVycywgYXhpcz0xKSkgXHUwMDNjIDFlLTY6XG4gICAgICAgIHByaW50KGZcIkNvbnZlcmdlZCBhdCBpdGVyYXRpb24ge2l0ZXJhdGlvbiArIDF9XCIpXG4gICAgICAgIGNlbnRlcnMgPSBuZXdfY2VudGVyc1xuICAgICAgICBicmVha1xuICAgIGNlbnRlcnMgPSBuZXdfY2VudGVyc1xuXG5wcmludChcIlxcbkl0ZXJhdGlvbiB8IFN0ZXAgfCBXQ1NTXCIpXG5mb3Igc3RlcCwgaXQsIHcgaW4gd2Nzc19oaXN0b3J5WzoxMl06XG4gICAgcHJpbnQoZlwiICAgIHtpdDo1ZH0gfCAgICB7c3RlcH0gfCB7dzouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udmVyZ2VuY2UgdG8gTG9jYWwgT3B0aW1hIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb252ZXJnZW5jZSBpcyBndWFyYW50ZWVkLCBidXQgdGhlIGZpeGVkIHBvaW50IGlzIGEgbG9jYWwgbWluaW11bSBvZiBXQ1NTIOKAlCBub3QgbmVjZXNzYXJpbHkgdGhlIGdsb2JhbCBtaW5pbXVtLiBUaGUgbGFuZHNjYXBlIG9mIFdDU1MgYXMgYSBmdW5jdGlvbiBvZiBjZW50cm9pZCBwb3NpdGlvbnMgaXMgbm9uLWNvbnZleCB3aXRoIGV4cG9uZW50aWFsbHkgbWFueSBsb2NhbCBtaW5pbWEuIFJ1bm5pbmcgay1tZWFucyB3aXRoIGRpZmZlcmVudCByYW5kb20gaW5pdGlhbGl6YXRpb25zIHByb2R1Y2VzIGRpZmZlcmVudCBmaW5hbCBXQ1NTIHZhbHVlczsgdGhlIHZhcmlhbmNlIGFjcm9zcyByZXN0YXJ0cyBkaXJlY3RseSBtZWFzdXJlcyBob3cgaGFyZCB0aGUgcHJvYmxlbSBpcy4gSW4gdGhlIHdvcnN0IGNhc2UsIGstbWVhbnMgY2FuIGNvbnZlcmdlIHRvIGEgcGFydGl0aW9uIHdoZXJlIFdDU1MgaXMgzpgobikgdGltZXMgdGhlIG9wdGltdW0sIHRob3VnaCB0aGlzIGlzIHJhcmUgaW4gcHJhY3RpY2Ugd2l0aCBrLW1lYW5zKysgc2VlZGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uY2x1c3RlciBpbXBvcnQgS01lYW5zXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcblxuWCwgXyA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTQwMCwgY2VudGVycz01LCBjbHVzdGVyX3N0ZD0xLjIsIHJhbmRvbV9zdGF0ZT0wKVxuayA9IDVcblxuIyBSdW4gMjAgcmVzdGFydHMgd2l0aCByYW5kb20gaW5pdFxuZmluYWxfd2Nzc19yYW5kb20sIGZpbmFsX3djc3NfcHAgPSBbXSwgW11cbmZvciBzZWVkIGluIHJhbmdlKDIwKTpcbiAgICBrbV9yID0gS01lYW5zKG5fY2x1c3RlcnM9aywgaW5pdD1cdTAwMjdyYW5kb21cdTAwMjcsIG5faW5pdD0xLCByYW5kb21fc3RhdGU9c2VlZCwgbWF4X2l0ZXI9MzAwKVxuICAgIGttX3IuZml0KFgpXG4gICAgZmluYWxfd2Nzc19yYW5kb20uYXBwZW5kKGttX3IuaW5lcnRpYV8pXG5cbiAgICBrbV9wID0gS01lYW5zKG5fY2x1c3RlcnM9aywgaW5pdD1cdTAwMjdrLW1lYW5zKytcdTAwMjcsIG5faW5pdD0xLCByYW5kb21fc3RhdGU9c2VlZCwgbWF4X2l0ZXI9MzAwKVxuICAgIGttX3AuZml0KFgpXG4gICAgZmluYWxfd2Nzc19wcC5hcHBlbmQoa21fcC5pbmVydGlhXylcblxucHJpbnQoZlwiUmFuZG9tIGluaXQgIOKAlCBtZWFuOiB7bnAubWVhbihmaW5hbF93Y3NzX3JhbmRvbSk6LjJmfSwgXCJcbiAgICAgIGZcInN0ZDoge25wLnN0ZChmaW5hbF93Y3NzX3JhbmRvbSk6LjJmfSwgXCJcbiAgICAgIGZcIm1pbjoge21pbihmaW5hbF93Y3NzX3JhbmRvbSk6LjJmfSwgbWF4OiB7bWF4KGZpbmFsX3djc3NfcmFuZG9tKTouMmZ9XCIpXG5wcmludChmXCJLLU1lYW5zKysg4oCUIG1lYW46IHtucC5tZWFuKGZpbmFsX3djc3NfcHApOi4yZn0sIFwiXG4gICAgICBmXCJzdGQ6IHtucC5zdGQoZmluYWxfd2Nzc19wcCk6LjJmfSwgXCJcbiAgICAgIGZcIm1pbjoge21pbihmaW5hbF93Y3NzX3BwKTouMmZ9LCBtYXg6IHttYXgoZmluYWxfd2Nzc19wcCk6LjJmfVwiKVxucHJpbnQoZlwiXFxuVmFyaWFuY2UgcmVkdWN0aW9uIGZyb20gay1tZWFucysrOiB7bnAuc3RkKGZpbmFsX3djc3NfcmFuZG9tKS9ucC5zdGQoZmluYWxfd2Nzc19wcCk6LjFmfXhcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLLU1lYW5zKysgdnMgUmFuZG9tIEluaXQg4oCUIFF1YWxpdHkgR3VhcmFudGVlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJLLU1lYW5zKysgcHJvdmlkZXMgYSB0aGVvcmV0aWNhbCBndWFyYW50ZWU6IEVbV0NTUyBhZnRlciBpbml0aWFsaXphdGlvbl0g4omkIDgobG4gayArIDIpIMOXIE9QVC4gVGhpcyBPKGxvZyBrKSBhcHByb3hpbWF0aW9uIG1lYW5zIHRoYXQgZXZlbiBiZWZvcmUgcnVubmluZyBMbG95ZFx1MDAyN3MgYWxnb3JpdGhtLCB0aGUgaW5pdGlhbCBjZW50cm9pZHMgYWxyZWFkeSBoYXZlIGJvdW5kZWQgcXVhbGl0eS4gQWZ0ZXIgcnVubmluZyBMbG95ZFx1MDAyN3MgdG8gY29udmVyZ2VuY2UgZnJvbSBhIGstbWVhbnMrKyBpbml0aWFsaXphdGlvbiwgdGhlIGV4cGVjdGVkIGZpbmFsIFdDU1MgaXMgd2l0aGluIE8obG9nIGspIG9mIG9wdGltYWwuIFRoZSBpbml0aWFsaXphdGlvbiBjb3N0IGlzIE8obsK3aykgYWRkaXRpb25hbCBkaXN0YW5jZSBjb21wdXRhdGlvbnMg4oCUIG5lZ2xpZ2libGUgY29tcGFyZWQgdG8gdGhlIGZ1bGwgTGxveWRcdTAwMjdzIHJ1bi4gVGhlIHByYWN0aWNhbCBjb25zZXF1ZW5jZSBpcyB0aGF0IDPigJM1IHJlc3RhcnRzIHdpdGggay1tZWFucysrIHR5cGljYWxseSBnaXZlcyByZXN1bHRzIGFzIGdvb2QgYXMgNTArIHJlc3RhcnRzIHdpdGggcmFuZG9tIGluaXRpYWxpemF0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBLTWVhbnNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuaW1wb3J0IG1hdHBsb3RsaWJcbm1hdHBsb3RsaWIudXNlKFx1MDAyN0FnZ1x1MDAyNylcblxuWCwgXyA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTYwMCwgY2VudGVycz02LCBjbHVzdGVyX3N0ZD0xLjAsIHJhbmRvbV9zdGF0ZT0xKVxuayA9IDZcbm5fdHJpYWxzID0gMzBcblxud2Nzc19yYW5kb20gPSBbS01lYW5zKG5fY2x1c3RlcnM9aywgaW5pdD1cdTAwMjdyYW5kb21cdTAwMjcsIG5faW5pdD0xLFxuICAgICAgICAgICAgICAgICAgICAgICByYW5kb21fc3RhdGU9cykuZml0KFgpLmluZXJ0aWFfIGZvciBzIGluIHJhbmdlKG5fdHJpYWxzKV1cbndjc3NfcHAgPSBbS01lYW5zKG5fY2x1c3RlcnM9aywgaW5pdD1cdTAwMjdrLW1lYW5zKytcdTAwMjcsIG5faW5pdD0xLFxuICAgICAgICAgICAgICAgICAgIHJhbmRvbV9zdGF0ZT1zKS5maXQoWCkuaW5lcnRpYV8gZm9yIHMgaW4gcmFuZ2Uobl90cmlhbHMpXVxuXG5iZXN0X3Bvc3NpYmxlID0gS01lYW5zKG5fY2x1c3RlcnM9aywgaW5pdD1cdTAwMjdrLW1lYW5zKytcdTAwMjcsIG5faW5pdD01MCwgcmFuZG9tX3N0YXRlPTQyKS5maXQoWCkuaW5lcnRpYV9cblxucHJpbnQoZlwiQmVzdCBwb3NzaWJsZSBXQ1NTICg1MCByZXN0YXJ0cywgay1tZWFucysrKToge2Jlc3RfcG9zc2libGU6LjJmfVwiKVxucHJpbnQoZlwiXFxuUmFuZG9tIGluaXQgb3ZlciB7bl90cmlhbHN9IHRyaWFsczpcIilcbnByaW50KGZcIiAgTWVhbiByYXRpbyB0byBiZXN0OiB7bnAubWVhbih3Y3NzX3JhbmRvbSkvYmVzdF9wb3NzaWJsZTouNGZ9XCIpXG5wcmludChmXCIgIFdvcnN0IHJhdGlvOiAgICAgICAge21heCh3Y3NzX3JhbmRvbSkvYmVzdF9wb3NzaWJsZTouNGZ9XCIpXG5wcmludChmXCIgIEZyYWN0aW9uIG9wdGltYWw6ICAge3N1bSh3IFx1MDAzYyBiZXN0X3Bvc3NpYmxlKjEuMDEgZm9yIHcgaW4gd2Nzc19yYW5kb20pL25fdHJpYWxzOi4wJX1cIilcbnByaW50KGZcIlxcbkstTWVhbnMrKyBvdmVyIHtuX3RyaWFsc30gdHJpYWxzOlwiKVxucHJpbnQoZlwiICBNZWFuIHJhdGlvIHRvIGJlc3Q6IHtucC5tZWFuKHdjc3NfcHApL2Jlc3RfcG9zc2libGU6LjRmfVwiKVxucHJpbnQoZlwiICBXb3JzdCByYXRpbzogICAgICAgIHttYXgod2Nzc19wcCkvYmVzdF9wb3NzaWJsZTouNGZ9XCIpXG5wcmludChmXCIgIEZyYWN0aW9uIG9wdGltYWw6ICAge3N1bSh3IFx1MDAzYyBiZXN0X3Bvc3NpYmxlKjEuMDEgZm9yIHcgaW4gd2Nzc19wcCkvbl90cmlhbHM6LjAlfVwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJIb3cgTWFueSBSZXN0YXJ0cz8iLCJjb250ZW50IjoiV2l0aCBrLW1lYW5zKysgaW5pdGlhbGl6YXRpb24sIDPigJMxMCByZXN0YXJ0cyAobl9pbml0IGluIHNrbGVhcm4pIGlzIHVzdWFsbHkgc3VmZmljaWVudCBmb3Igd2VsbC1zZXBhcmF0ZWQgY2x1c3RlcnMuIEZvciBoaWdoLW92ZXJsYXAgb3IgaGlnaC1kaW1lbnNpb25hbCBkYXRhLCB1c2Ugbl9pbml0PTIwIG9yIG5faW5pdD1cdTAwMjdhdXRvXHUwMDI3IChza2xlYXJuIOKJpTEuMikuIFdpdGggcmFuZG9tIGluaXRpYWxpemF0aW9uIHlvdSBuZWVkIDUwKyByZXN0YXJ0cyB0byBhY2hpZXZlIGNvbXBhcmFibGUgcmVsaWFiaWxpdHkuIEFsd2F5cyByZXBvcnQgdGhlIG1pbmltdW0gV0NTUyBhY3Jvc3MgcmVzdGFydHMsIG5vdCB0aGUgbWVhbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXRob2xvZ2ljYWwgQ2FzZSDigJQgQmFkIExvY2FsIE1pbmltdW0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjbGFzc2ljIHBhdGhvbG9naWNhbCBjYXNlIGZvciBrLW1lYW5zIGlzIHR3byBlbG9uZ2F0ZWQgY2x1c3RlcnMgYWxvbmcgZGlmZmVyZW50IGF4ZXMgaW5pdGlhbGl6ZWQgd2l0aCBjZW50cm9pZHMgdGhhdCBiaXNlY3QgZWFjaCBjbHVzdGVyIGhvcml6b250YWxseS4gTGxveWRcdTAwMjdzIGFsZ29yaXRobSBjb252ZXJnZXMgdG8gYSBwYXJ0aXRpb24gdGhhdCBzcGxpdHMgZWFjaCB0cnVlIGNsdXN0ZXIgaW50byB0d28gaGFsdmVzIHJhdGhlciB0aGFuIGNvcnJlY3RseSBpZGVudGlmeWluZyB0aGUgdHdvIGVsb25nYXRlZCBncm91cHMuIEstbWVhbnMrKyBzaWduaWZpY2FudGx5IHJlZHVjZXMgKGJ1dCBkb2VzIG5vdCBlbGltaW5hdGUpIHRoZSBwcm9iYWJpbGl0eSBvZiBsYW5kaW5nIGluIHN1Y2ggYmFkIGNvbmZpZ3VyYXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBLTWVhbnNcblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDk5KVxuIyBUd28gaG9yaXpvbnRhbGx5IGVsb25nYXRlZCBjbHVzdGVycyBhdCBkaWZmZXJlbnQgaGVpZ2h0c1xuY2x1c3Rlcl9hID0gcm5nLm5vcm1hbChsb2M9WzAsIDBdLCBzY2FsZT1bMy4wLCAwLjE1XSwgc2l6ZT0oMTUwLCAyKSlcbmNsdXN0ZXJfYiA9IHJuZy5ub3JtYWwobG9jPVswLCAyXSwgc2NhbGU9WzMuMCwgMC4xNV0sIHNpemU9KDE1MCwgMikpXG5YID0gbnAudnN0YWNrKFtjbHVzdGVyX2EsIGNsdXN0ZXJfYl0pXG55X3RydWUgPSBucC5hcnJheShbMF0qMTUwICsgWzFdKjE1MClcblxuIyBCYWQgaW5pdDogYm90aCBjZW50cm9pZHMgbmVhciB4LWF4aXMsIG9uZSBsZWZ0IG9uZSByaWdodFxuYmFkX2luaXQgPSBucC5hcnJheShbWy0yLjAsIDEuMF0sIFsyLjAsIDEuMF1dKVxua21fYmFkID0gS01lYW5zKG5fY2x1c3RlcnM9MiwgaW5pdD1iYWRfaW5pdCwgbl9pbml0PTEsIG1heF9pdGVyPTMwMClcbmttX2JhZC5maXQoWClcblxuIyBHb29kIGluaXQ6IG9uZSBjZW50cm9pZCBwZXIgdHJ1ZSBjbHVzdGVyXG5nb29kX2luaXQgPSBucC5hcnJheShbWzAuMCwgMC4wXSwgWzAuMCwgMi4wXV0pXG5rbV9nb29kID0gS01lYW5zKG5fY2x1c3RlcnM9MiwgaW5pdD1nb29kX2luaXQsIG5faW5pdD0xLCBtYXhfaXRlcj0zMDApXG5rbV9nb29kLmZpdChYKVxuXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWRqdXN0ZWRfcmFuZF9zY29yZVxucHJpbnQoZlwiQmFkIGluaXQgIFdDU1M9e2ttX2JhZC5pbmVydGlhXzouMmZ9LCBBUkk9e2FkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCBrbV9iYWQubGFiZWxzXyk6LjNmfVwiKVxucHJpbnQoZlwiR29vZCBpbml0IFdDU1M9e2ttX2dvb2QuaW5lcnRpYV86LjJmfSwgQVJJPXthZGp1c3RlZF9yYW5kX3Njb3JlKHlfdHJ1ZSwga21fZ29vZC5sYWJlbHNfKTouM2Z9XCIpXG5wcmludChcIlxcbkJhZCBpbml0IHByb2R1Y2VzIExPV0VSIFdDU1MgYnV0IFdST05HIGNsdXN0ZXJzOiBjbGFzc2ljIGxvY2FsIG1pbmltdW0gdHJhcC5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wbGV4aXR5IGFuZCBQcmFjdGljYWwgR3VpZGFuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0aW1lIGNvbXBsZXhpdHkgb2Ygay1tZWFucyBpcyBPKG7Ct2vCt2TCt1QpIHdoZXJlIG4gaXMgcG9pbnRzLCBrIGlzIGNsdXN0ZXJzLCBkIGlzIGRpbWVuc2lvbnMsIGFuZCBUIGlzIGl0ZXJhdGlvbnMuIFQgaXMgdXN1YWxseSAxMOKAkzMwMCBpbiBwcmFjdGljZS4gVGhlIG51bWJlciBvZiBkaXN0aW5jdCBwYXJ0aXRpb25zIGlzIE8oa+KBvyksIGJ1dCBjb252ZXJnZW5jZSBoYXBwZW5zIGxvbmcgYmVmb3JlIHRoZSBhbGdvcml0aG0gZW51bWVyYXRlcyB0aGVtLiBGb3IgbGFyZ2UgbiwgTWluaS1CYXRjaCBLLU1lYW5zIHJlcGxhY2VzIHRoZSBmdWxsIHBhc3Mgd2l0aCBhIGJhdGNoIG9mIHNpemUgYiwgcmVkdWNpbmcgcGVyLWl0ZXJhdGlvbiBjb3N0IHRvIE8oYsK3a8K3ZCkuIFNwYWNlIGNvbXBsZXhpdHkgaXMgTyhuwrdkICsga8K3ZCkgZm9yIHN0b3JpbmcgZGF0YSBhbmQgY2VudHJvaWRzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIG5faW5pdD0xMCAoc2tsZWFybiBkZWZhdWx0KSB3aXRoIGstbWVhbnMrKyBmb3IgbW9zdCBwcm9ibGVtczsgaW5jcmVhc2UgdG8gMjDigJM1MCBmb3IgayBcdTAwM2UgMjAgb3IgaGlnaC1vdmVybGFwIGRhdGEuIiwiU2V0IG1heF9pdGVyPTMwMCAoZGVmYXVsdCk7IG1vc3QgcnVucyBjb252ZXJnZSBpbiAxMOKAkzUwIGl0ZXJhdGlvbnMg4oCUIHdhdGNoIGZvciBjb252ZXJnZW5jZSB3YXJuaW5ncy4iLCJTY2FsZSBmZWF0dXJlcyBiZWZvcmUgY2x1c3RlcmluZyDigJQgay1tZWFucyB1c2VzIEV1Y2xpZGVhbiBkaXN0YW5jZTsgdW5zY2FsZWQgZmVhdHVyZXMgd2l0aCBsYXJnZSB2YXJpYW5jZSBkb21pbmF0ZS4iLCJGb3IgbiBcdTAwM2UgMTAwSywgdXNlIE1pbmlCYXRjaEtNZWFucyB3aXRoIGJhdGNoX3NpemU9MTAyNOKAkzQwOTYgZm9yIGEgMTDigJMxMDB4IHNwZWVkdXAuIiwiQWx3YXlzIGNoZWNrIG11bHRpcGxlIGsgdmFsdWVzIHdpdGggc2lsaG91ZXR0ZSBzY29yZTsgdGhlIGVsYm93IGFsb25lIGlzIHVucmVsaWFibGUgZm9yIGRpZmZ1c2UgY2x1c3RlcnMuIl19LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJJbml0aWFsaXphdGlvbiIsIlF1YWxpdHkiLCJFeHRyYSBDb3N0IiwiUmVzdGFydHMgTmVlZGVkIiwiR3VhcmFudGVlIl0sInJvd3MiOltbIlJhbmRvbSIsIlBvb3Ig4oCUIGhpZ2ggdmFyaWFuY2UiLCJOb25lIiwiMjDigJM1MCBmb3IgcmVsaWFiaWxpdHkiLCJOb25lIl0sWyJLLU1lYW5zKysiLCJHb29kIOKAlCBsb3cgdmFyaWFuY2UiLCJPKG7Ct2spIGRpc3RhbmNlcyIsIjPigJMxMCBzdWZmaWNpZW50IiwiTyhsb2cgaykgYXBwcm94aW1hdGlvbiJdLFsiSy1NZWFuc+KAliAocGFyYWxsZWwpIiwiVmVyeSBnb29kIOKAlCBzY2FsYWJsZSIsIk8obsK3ay9yb3VuZCkgw5cgcm91bmRzIiwiMeKAkzMgdHlwaWNhbGx5IiwiTyhsb2cgaykgd2l0aCBmZXdlciByb3VuZHMiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gcHJhY3RpY2UsIHJ1biBza2xlYXJuIEtNZWFucyB3aXRoIG5faW5pdD1cdTAwMjdhdXRvXHUwMDI3IChhZGFwdGl2ZSDigJQgMTAgZm9yIHNtYWxsIGssIG1vcmUgZm9yIGxhcmdlIGspIGFuZCBhbHdheXMgY2hlY2sgdGhhdCBpbmVydGlhXyBpcyBjb25zaXN0ZW50IGFjcm9zcyAz4oCTNSBpbmRlcGVuZGVudCBydW5zIGJlZm9yZSB0cnVzdGluZyB0aGUgcmVzdWx0LiBJZiB0aGUgYmVzdCBXQ1NTIGFjcm9zcyByZXN0YXJ0cyB2YXJpZXMgYnkgbW9yZSB0aGFuIDUlLCBpbmNyZWFzZSBuX2luaXQgb3Igc3dpdGNoIHRvIGEgc3Ryb25nZXIgaW5pdGlhbGl6YXRpb24gc3RyYXRlZ3kuIENvbnZlcmdlbmNlIHdpdGhpbiAxMOKAkzMwIGl0ZXJhdGlvbnMgaXMgdHlwaWNhbCBmb3Igd2VsbC1zZXBhcmF0ZWQgY2x1c3RlcnM7IHNsb3cgY29udmVyZ2VuY2UgKFx1MDAzZTEwMCBpdGVyYXRpb25zKSBzaWduYWxzIHRoYXQgayBpcyB0b28gbGFyZ2UsIGZlYXR1cmVzIGFyZSBwb29ybHkgc2NhbGVkLCBvciB0aGUgZGF0YSBzdHJ1Y3R1cmUgaXMgZnVuZGFtZW50YWxseSBub24tc3BoZXJpY2FsLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# K-Means Convergence — Monotone Decrease and Local Optima

K-means is guaranteed to converge, but only to a local minimum of the Within-Cluster Sum of Squares. This note proves the convergence argument rigorously, demonstrates how poor initialization leads to bad local optima, and shows why k-means++ and multiple restarts are essential for reliable results. Understanding convergence behavior helps practitioners decide how many restarts to use and when to trust the final clustering.

## WCSS as the Convergence Criterion

The objective WCSS = Σᵢ Σ_{x∈Cᵢ} ‖x − μᵢ‖² is bounded below by zero (distances are non-negative). At initialization, WCSS has some finite value determined by the initial centroids. The convergence argument is: if WCSS cannot increase at any step and it is bounded below, it must converge. The key is showing that each of the two steps — E-step and M-step — is non-increasing. Since there are finitely many partitions of n points into k labeled clusters (at most kⁿ), WCSS can decrease only finitely many times before reaching a fixed point.

## Why Each Step Decreases WCSS

E-step (assignment): for fixed centroids μ₁,...,μₖ, assigning each point x to its nearest centroid arg min_i ‖x−μᵢ‖² is exactly minimizing the WCSS contribution of x. Any reassignment to a farther centroid would strictly increase WCSS. Therefore the E-step cannot increase WCSS and will decrease it whenever any point is closer to a different centroid. M-step (update): for fixed assignments, the centroid that minimizes Σ_{x∈Cᵢ} ‖x−μ‖² over μ is exactly the mean μᵢ = (1/|Cᵢ|)Σ_{x∈Cᵢ} x. This follows because ∇_μ Σ ‖x−μ‖² = −2Σ(x−μ) = 0 implies μ = mean(Cᵢ). Any other centroid position gives strictly higher WCSS.

```python
import numpy as np
from sklearn.datasets import make_blobs

rng = np.random.default_rng(7)
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.9, random_state=42)
k = 4

# Random initialization to make convergence tracking interesting
centers = X[rng.choice(len(X), k, replace=False)].copy()

wcss_history = []
for iteration in range(50):
    # E-step
    diffs = X[:, None, :] - centers[None, :, :]
    labels = np.argmin((diffs ** 2).sum(axis=2), axis=1)
    # Compute WCSS after E-step
    wcss_e = sum(np.sum((X[labels == i] - centers[i]) ** 2) for i in range(k))
    wcss_history.append(('E', iteration, wcss_e))
    # M-step
    new_centers = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    wcss_m = sum(np.sum((X[labels == i] - new_centers[i]) ** 2) for i in range(k))
    wcss_history.append(('M', iteration, wcss_m))
    assert wcss_m <= wcss_e + 1e-9, "M-step increased WCSS!"
    if np.max(np.linalg.norm(new_centers - centers, axis=1)) < 1e-6:
        print(f"Converged at iteration {iteration + 1}")
        centers = new_centers
        break
    centers = new_centers

print("\nIteration | Step | WCSS")
for step, it, w in wcss_history[:12]:
    print(f"    {it:5d} |    {step} | {w:.4f}")
```

## Convergence to Local Optima

Convergence is guaranteed, but the fixed point is a local minimum of WCSS — not necessarily the global minimum. The landscape of WCSS as a function of centroid positions is non-convex with exponentially many local minima. Running k-means with different random initializations produces different final WCSS values; the variance across restarts directly measures how hard the problem is. In the worst case, k-means can converge to a partition where WCSS is Θ(n) times the optimum, though this is rare in practice with k-means++ seeding.

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=400, centers=5, cluster_std=1.2, random_state=0)
k = 5

# Run 20 restarts with random init
final_wcss_random, final_wcss_pp = [], []
for seed in range(20):
    km_r = KMeans(n_clusters=k, init='random', n_init=1, random_state=seed, max_iter=300)
    km_r.fit(X)
    final_wcss_random.append(km_r.inertia_)

    km_p = KMeans(n_clusters=k, init='k-means++', n_init=1, random_state=seed, max_iter=300)
    km_p.fit(X)
    final_wcss_pp.append(km_p.inertia_)

print(f"Random init  — mean: {np.mean(final_wcss_random):.2f}, "
      f"std: {np.std(final_wcss_random):.2f}, "
      f"min: {min(final_wcss_random):.2f}, max: {max(final_wcss_random):.2f}")
print(f"K-Means++ — mean: {np.mean(final_wcss_pp):.2f}, "
      f"std: {np.std(final_wcss_pp):.2f}, "
      f"min: {min(final_wcss_pp):.2f}, max: {max(final_wcss_pp):.2f}")
print(f"\nVariance reduction from k-means++: {np.std(final_wcss_random)/np.std(final_wcss_pp):.1f}x")
```

## K-Means++ vs Random Init — Quality Guarantee

K-Means++ provides a theoretical guarantee: E[WCSS after initialization] ≤ 8(ln k + 2) × OPT. This O(log k) approximation means that even before running Lloyd's algorithm, the initial centroids already have bounded quality. After running Lloyd's to convergence from a k-means++ initialization, the expected final WCSS is within O(log k) of optimal. The initialization cost is O(n·k) additional distance computations — negligible compared to the full Lloyd's run. The practical consequence is that 3–5 restarts with k-means++ typically gives results as good as 50+ restarts with random initialization.

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib
matplotlib.use('Agg')

X, _ = make_blobs(n_samples=600, centers=6, cluster_std=1.0, random_state=1)
k = 6
n_trials = 30

wcss_random = [KMeans(n_clusters=k, init='random', n_init=1,
                       random_state=s).fit(X).inertia_ for s in range(n_trials)]
wcss_pp = [KMeans(n_clusters=k, init='k-means++', n_init=1,
                   random_state=s).fit(X).inertia_ for s in range(n_trials)]

best_possible = KMeans(n_clusters=k, init='k-means++', n_init=50, random_state=42).fit(X).inertia_

print(f"Best possible WCSS (50 restarts, k-means++): {best_possible:.2f}")
print(f"\nRandom init over {n_trials} trials:")
print(f"  Mean ratio to best: {np.mean(wcss_random)/best_possible:.4f}")
print(f"  Worst ratio:        {max(wcss_random)/best_possible:.4f}")
print(f"  Fraction optimal:   {sum(w < best_possible*1.01 for w in wcss_random)/n_trials:.0%}")
print(f"\nK-Means++ over {n_trials} trials:")
print(f"  Mean ratio to best: {np.mean(wcss_pp)/best_possible:.4f}")
print(f"  Worst ratio:        {max(wcss_pp)/best_possible:.4f}")
print(f"  Fraction optimal:   {sum(w < best_possible*1.01 for w in wcss_pp)/n_trials:.0%}")
```

> **How Many Restarts?**: With k-means++ initialization, 3–10 restarts (n_init in sklearn) is usually sufficient for well-separated clusters. For high-overlap or high-dimensional data, use n_init=20 or n_init='auto' (sklearn ≥1.2). With random initialization you need 50+ restarts to achieve comparable reliability. Always report the minimum WCSS across restarts, not the mean.

## Pathological Case — Bad Local Minimum

The classic pathological case for k-means is two elongated clusters along different axes initialized with centroids that bisect each cluster horizontally. Lloyd's algorithm converges to a partition that splits each true cluster into two halves rather than correctly identifying the two elongated groups. K-means++ significantly reduces (but does not eliminate) the probability of landing in such bad configurations.

```python
import numpy as np
from sklearn.cluster import KMeans

rng = np.random.default_rng(99)
# Two horizontally elongated clusters at different heights
cluster_a = rng.normal(loc=[0, 0], scale=[3.0, 0.15], size=(150, 2))
cluster_b = rng.normal(loc=[0, 2], scale=[3.0, 0.15], size=(150, 2))
X = np.vstack([cluster_a, cluster_b])
y_true = np.array([0]*150 + [1]*150)

# Bad init: both centroids near x-axis, one left one right
bad_init = np.array([[-2.0, 1.0], [2.0, 1.0]])
km_bad = KMeans(n_clusters=2, init=bad_init, n_init=1, max_iter=300)
km_bad.fit(X)

# Good init: one centroid per true cluster
good_init = np.array([[0.0, 0.0], [0.0, 2.0]])
km_good = KMeans(n_clusters=2, init=good_init, n_init=1, max_iter=300)
km_good.fit(X)

from sklearn.metrics import adjusted_rand_score
print(f"Bad init  WCSS={km_bad.inertia_:.2f}, ARI={adjusted_rand_score(y_true, km_bad.labels_):.3f}")
print(f"Good init WCSS={km_good.inertia_:.2f}, ARI={adjusted_rand_score(y_true, km_good.labels_):.3f}")
print("\nBad init produces LOWER WCSS but WRONG clusters: classic local minimum trap.")
```

## Complexity and Practical Guidance

The time complexity of k-means is O(n·k·d·T) where n is points, k is clusters, d is dimensions, and T is iterations. T is usually 10–300 in practice. The number of distinct partitions is O(kⁿ), but convergence happens long before the algorithm enumerates them. For large n, Mini-Batch K-Means replaces the full pass with a batch of size b, reducing per-iteration cost to O(b·k·d). Space complexity is O(n·d + k·d) for storing data and centroids.

- Use n_init=10 (sklearn default) with k-means++ for most problems; increase to 20–50 for k > 20 or high-overlap data.
- Set max_iter=300 (default); most runs converge in 10–50 iterations — watch for convergence warnings.
- Scale features before clustering — k-means uses Euclidean distance; unscaled features with large variance dominate.
- For n > 100K, use MiniBatchKMeans with batch_size=1024–4096 for a 10–100x speedup.
- Always check multiple k values with silhouette score; the elbow alone is unreliable for diffuse clusters.

| Initialization | Quality | Extra Cost | Restarts Needed | Guarantee |
| --- | --- | --- | --- | --- |
| Random | Poor — high variance | None | 20–50 for reliability | None |
| K-Means++ | Good — low variance | O(n·k) distances | 3–10 sufficient | O(log k) approximation |
| K-Means‖ (parallel) | Very good — scalable | O(n·k/round) × rounds | 1–3 typically | O(log k) with fewer rounds |

In practice, run sklearn KMeans with n_init='auto' (adaptive — 10 for small k, more for large k) and always check that inertia_ is consistent across 3–5 independent runs before trusting the result. If the best WCSS across restarts varies by more than 5%, increase n_init or switch to a stronger initialization strategy. Convergence within 10–30 iterations is typical for well-separated clusters; slow convergence (>100 iterations) signals that k is too large, features are poorly scaled, or the data structure is fundamentally non-spherical.

---

