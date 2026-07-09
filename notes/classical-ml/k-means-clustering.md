---
title: "K-Means Clustering — Lloyd's Algorithm and Initialization"
slug: "k-means-clustering"
description: "Master Lloyd's algorithm for k-means clustering: the assign-update loop that minimizes WCSS, k-means++ initialization for O(log k) approximation, elbow and silhouette methods for choosing k, mini-batch k-means for large data, and color quantization as a practical application."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSy1NZWFucyBpcyB0aGUgbW9zdCB3aWRlbHkgZGVwbG95ZWQgY2x1c3RlcmluZyBhbGdvcml0aG0uIEdpdmVuIG4gcG9pbnRzIGFuZCBhIHRhcmdldCBudW1iZXIgb2YgY2x1c3RlcnMgaywgaXQgcGFydGl0aW9ucyB0aGUgZGF0YSB0byBtaW5pbWl6ZSB0aGUgV2l0aGluLUNsdXN0ZXIgU3VtIG9mIFNxdWFyZXMgKFdDU1MpLiBUaGUgYWxnb3JpdGhtIGFsdGVybmF0ZXMgYmV0d2VlbiB0d28gc2ltcGxlIHN0ZXBzIOKAlCBhc3NpZ25pbmcgcG9pbnRzIHRvIGNsdXN0ZXJzIGFuZCB1cGRhdGluZyBjbHVzdGVyIGNlbnRlcnMg4oCUIHVudGlsIGNvbnZlcmdlbmNlLiBVbmRlcnN0YW5kaW5nIGl0cyBnZW9tZXRyaWMgb2JqZWN0aXZlLCB0aGUgay1tZWFucysrIGluaXRpYWxpemF0aW9uIHN0cmF0ZWd5LCBhbmQgaG93IHRvIHNlbGVjdCBrIGFyZSBlc3NlbnRpYWwgZm9yIHByYWN0aWNhbCB1bnN1cGVydmlzZWQgbGVhcm5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEstTWVhbnMgT2JqZWN0aXZlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJLLU1lYW5zIG1pbmltaXplcyBXQ1NTID0gzqPhtaIgzqNfe3jiiIhD4bWifSDigJZ4IOKIkiDOvOG1ouKAlsKyIHdoZXJlIEPhtaIgaXMgdGhlIGktdGggY2x1c3RlciBhbmQgzrzhtaIgaXMgaXRzIGNlbnRyb2lkLiBUaGlzIG9iamVjdGl2ZSBmYXZvcnMgY29tcGFjdCwgc3BoZXJpY2FsIGNsdXN0ZXJzIG9mIHJvdWdobHkgZXF1YWwgc2l6ZS4gQmVjYXVzZSBXQ1NTIGlzIG5vbi1jb252ZXggaW4gYm90aCB0aGUgYXNzaWdubWVudHMgYW5kIGNlbnRyb2lkcyBqb2ludGx5LCB0aGUgYWxnb3JpdGhtIGNvbnZlcmdlcyB0byBhIGxvY2FsIG1pbmltdW0gcmF0aGVyIHRoYW4gdGhlIGdsb2JhbCBvcHRpbXVtLiBGaW5kaW5nIHRoZSBnbG9iYWxseSBvcHRpbWFsIGstbWVhbnMgcGFydGl0aW9uIGlzIE5QLWhhcmQ7IGluIHByYWN0aWNlIHdlIHJ1biB0aGUgYWxnb3JpdGhtIHdpdGggbXVsdGlwbGUgcmVzdGFydHMgYW5kIGtlZXAgdGhlIGJlc3QgcmVzdWx0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikxsb3lkXHUwMDI3cyBBbGdvcml0aG0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikxsb3lkXHUwMDI3cyBhbGdvcml0aG0gYWx0ZXJuYXRlczogKDEpIEUtc3RlcCDigJQgYXNzaWduIGVhY2ggcG9pbnQgdG8gaXRzIG5lYXJlc3QgY2VudHJvaWQsIHdoaWNoIGNhbm5vdCBpbmNyZWFzZSBXQ1NTIGZvciBmaXhlZCBjZW50cm9pZHM7ICgyKSBNLXN0ZXAg4oCUIHNldCBlYWNoIGNlbnRyb2lkIHRvIHRoZSBtZWFuIG9mIGl0cyBhc3NpZ25lZCBwb2ludHMsIHdoaWNoIG1pbmltaXplcyBXQ1NTIGZvciBmaXhlZCBhc3NpZ25tZW50cyBzaW5jZSB0aGUgbWVhbiB1bmlxdWVseSBtaW5pbWl6ZXMgdGhlIHN1bSBvZiBzcXVhcmVkIGRldmlhdGlvbnMuIEJlY2F1c2UgZWFjaCBzdGVwIGlzIG5vbi1pbmNyZWFzaW5nIGFuZCBXQ1NTIGlzIGJvdW5kZWQgYmVsb3cgYnkgemVybywgYW5kIHRoZXJlIGFyZSBmaW5pdGVseSBtYW55IGRpc3RpbmN0IHBhcnRpdGlvbnMgb2YgbiBwb2ludHMgaW50byBrIG5vbi1lbXB0eSBjbHVzdGVycywgY29udmVyZ2VuY2UgaW4gZmluaXRlIHN0ZXBzIGlzIGd1YXJhbnRlZWQuIFRoZSBxdWFsaXR5IG9mIHRoZSBsb2NhbCBtaW5pbXVtIGZvdW5kIGRlcGVuZHMgaGVhdmlseSBvbiBpbml0aWFsaXphdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcblxuZGVmIGttZWFuc19wbHVzX3BsdXMoWCwgaywgcm5nKTpcbiAgICBcIlwiXCJLLU1lYW5zKysgc2VlZGluZyDigJQgTyhsb2cgaykgYXBwcm94aW1hdGlvbiBndWFyYW50ZWUuXCJcIlwiXG4gICAgbiA9IFguc2hhcGVbMF1cbiAgICBjZW50ZXJzID0gW1hbcm5nLmludGVnZXJzKG4pXS5jb3B5KCldXG4gICAgZm9yIF8gaW4gcmFuZ2UoayAtIDEpOlxuICAgICAgICBkaXN0cyA9IG5wLmFycmF5KFttaW4obnAuc3VtKCh4IC0gYykgKiogMikgZm9yIGMgaW4gY2VudGVycykgZm9yIHggaW4gWF0pXG4gICAgICAgIHByb2JzID0gZGlzdHMgLyBkaXN0cy5zdW0oKVxuICAgICAgICBjZW50ZXJzLmFwcGVuZChYW3JuZy5jaG9pY2UobiwgcD1wcm9icyldLmNvcHkoKSlcbiAgICByZXR1cm4gbnAuYXJyYXkoY2VudGVycylcblxuZGVmIGxsb3lkX2ttZWFucyhYLCBrLCBtYXhfaXRlcj0zMDAsIHRvbD0xZS00LCBzZWVkPTQyKTpcbiAgICBcIlwiXCJMbG95ZFx1MDAyN3MgYWxnb3JpdGhtIHdpdGggSy1NZWFucysrIGluaXRpYWxpemF0aW9uLlwiXCJcIlxuICAgIHJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyhzZWVkKVxuICAgIGNlbnRlcnMgPSBrbWVhbnNfcGx1c19wbHVzKFgsIGssIHJuZylcbiAgICBmb3IgaXQgaW4gcmFuZ2UobWF4X2l0ZXIpOlxuICAgICAgICBkaWZmcyA9IFhbOiwgTm9uZSwgOl0gLSBjZW50ZXJzW05vbmUsIDosIDpdXG4gICAgICAgIGxhYmVscyA9IG5wLmFyZ21pbigoZGlmZnMgKiogMikuc3VtKGF4aXM9MiksIGF4aXM9MSlcbiAgICAgICAgbmV3X2NlbnRlcnMgPSBucC5hcnJheShbWFtsYWJlbHMgPT0gaV0ubWVhbihheGlzPTApIGZvciBpIGluIHJhbmdlKGspXSlcbiAgICAgICAgc2hpZnQgPSBucC5tYXgobnAubGluYWxnLm5vcm0obmV3X2NlbnRlcnMgLSBjZW50ZXJzLCBheGlzPTEpKVxuICAgICAgICBjZW50ZXJzID0gbmV3X2NlbnRlcnNcbiAgICAgICAgaWYgc2hpZnQgXHUwMDNjIHRvbDpcbiAgICAgICAgICAgIHByaW50KGZcIkNvbnZlcmdlZCBhdCBpdGVyYXRpb24ge2l0ICsgMX1cIilcbiAgICAgICAgICAgIGJyZWFrXG4gICAgd2NzcyA9IHN1bShucC5zdW0oKFhbbGFiZWxzID09IGldIC0gY2VudGVyc1tpXSkgKiogMikgZm9yIGkgaW4gcmFuZ2UoaykpXG4gICAgcmV0dXJuIGxhYmVscywgY2VudGVycywgd2Nzc1xuXG5YLCB5X3RydWUgPSBtYWtlX2Jsb2JzKG5fc2FtcGxlcz00MDAsIGNlbnRlcnM9NCwgY2x1c3Rlcl9zdGQ9MC44LCByYW5kb21fc3RhdGU9NDIpXG5sYWJlbHMsIGNlbnRlcnMsIHdjc3MgPSBsbG95ZF9rbWVhbnMoWCwgaz00KVxucHJpbnQoZlwiRmluYWwgV0NTUzoge3djc3M6LjJmfVwiKVxucHJpbnQoZlwiQ2x1c3RlciBzaXplczoge1tpbnQoKGxhYmVscyA9PSBpKS5zdW0oKSkgZm9yIGkgaW4gcmFuZ2UoNCldfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkstTWVhbnMrKyBJbml0aWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmFuZG9tIGluaXRpYWxpemF0aW9uIGZyZXF1ZW50bHkgbGFuZHMgaW4gcG9vciBsb2NhbCBvcHRpbWEuIEstTWVhbnMrKyBzZWVkcyBjZW50cm9pZHMgc3ByZWFkIGFjcm9zcyB0aGUgZGF0YSBieSBjaG9vc2luZyBlYWNoIG5ldyBjZW50cm9pZCB3aXRoIHByb2JhYmlsaXR5IHByb3BvcnRpb25hbCB0byBpdHMgc3F1YXJlZCBkaXN0YW5jZSBmcm9tIHRoZSBuZWFyZXN0IGFscmVhZHktY2hvc2VuIGNlbnRyb2lkLiBUaGlzIGdpdmVzIGEgdGhlb3JldGljYWwgZ3VhcmFudGVlOiBFW1dDU1NfaW5pdF0g4omkIE8obG9nIGspIMOXIE9QVC4gSW4gcHJhY3RpY2Ugay1tZWFucysrIHJlZHVjZXMgdmFyaWFuY2UgYWNyb3NzIHJlc3RhcnRzIGRyYW1hdGljYWxseSBhbmQgdXN1YWxseSByZWFjaGVzIGEgZ29vZCBzb2x1dGlvbiBpbiAz4oCTNSByZXN0YXJ0cyByYXRoZXIgdGhhbiB0aGUgMjDigJM1MCBuZWVkZWQgd2l0aCBwdXJlIHJhbmRvbSBpbml0aWFsaXphdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNob29zZSBmaXJzdCBjZW50cm9pZCB1bmlmb3JtbHkgYXQgcmFuZG9tIGZyb20gdGhlIGRhdGEuIiwiRm9yIGVhY2ggcmVtYWluaW5nIHBvaW50IHgsIGNvbXB1dGUgZMKyKHgpID0gbWluIHNxdWFyZWQgZGlzdGFuY2UgdG8gdGhlIG5lYXJlc3QgY2hvc2VuIGNlbnRyb2lkLiIsIlNhbXBsZSB0aGUgbmV4dCBjZW50cm9pZCB3aXRoIHByb2JhYmlsaXR5IHByb3BvcnRpb25hbCB0byBkwrIoeCkg4oCUIGZhcnRoZXIgcG9pbnRzIGFyZSBtb3JlIGxpa2VseSB0byBiZSBjaG9zZW4uIiwiUmVwZWF0IHN0ZXBzIDLigJMzIHVudGlsIGsgY2VudHJvaWRzIGFyZSBzZWxlY3RlZCwgdGhlbiBydW4gTGxveWRcdTAwMjdzIGFsZ29yaXRobS4iLCJHdWFyYW50ZWU6IEVbV0NTU10g4omkIDgobG4gayArIDIpIMOXIE9QVCDigJQgYSBsb2dhcml0aG1pYyBhcHByb3hpbWF0aW9uIGZhY3Rvci4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hvb3NpbmcgSyDigJQgRWxib3csIFNpbGhvdWV0dGUsIGFuZCBHYXAgU3RhdGlzdGljIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZWxlY3RpbmcgayBpcyB1bnN1cGVydmlzZWQg4oCUIHRoZXJlIGlzIG5vIGdyb3VuZCB0cnV0aCBsYWJlbC4gVGhyZWUgY29tcGxlbWVudGFyeSBkaWFnbm9zdGljcyBoZWxwOiAoMSkgRWxib3cgbWV0aG9kIOKAlCBwbG90IFdDU1MgdnMgazsgdGhlIFx1MDAyN2VsYm93XHUwMDI3IChsYXJnZXN0IHNlY29uZCBkZXJpdmF0aXZlKSBpbmRpY2F0ZXMgZGltaW5pc2hpbmcgcmV0dXJucyBmcm9tIGFkZGluZyBjbHVzdGVycy4gKDIpIFNpbGhvdWV0dGUgc2NvcmUg4oCUIHMoaSkgPSAoYihpKeKIkmEoaSkpIC8gbWF4KGEoaSksYihpKSkgd2hlcmUgYShpKSBpcyB0aGUgbWVhbiBpbnRyYS1jbHVzdGVyIGRpc3RhbmNlIGFuZCBiKGkpIGlzIHRoZSBtZWFuIGRpc3RhbmNlIHRvIHRoZSBuZWFyZXN0IG90aGVyIGNsdXN0ZXI7IHJhbmdlIFviiJIxLDFdLCBoaWdoZXIgaXMgYmV0dGVyLiAoMykgR2FwIHN0YXRpc3RpYyDigJQgY29tcGFyZXMgbG9nKFdDU1NfaykgdG8gaXRzIGV4cGVjdGVkIHZhbHVlIHVuZGVyIGEgbnVsbCB1bmlmb3JtIHJlZmVyZW5jZSBkaXN0cmlidXRpb247IGNob29zZSB0aGUgc21hbGxlc3QgayB3aGVyZSBHYXAoaykg4omlIEdhcChrKzEpIOKIkiBzZShrKzEpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBLTWVhbnNcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBzaWxob3VldHRlX3Njb3JlXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcblxuWCwgXyA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTUwMCwgY2VudGVycz01LCBjbHVzdGVyX3N0ZD0wLjksIHJhbmRvbV9zdGF0ZT0wKVxuXG5rX3JhbmdlID0gcmFuZ2UoMiwgMTEpXG53Y3NzX3ZhbHMsIHNpbF92YWxzID0gW10sIFtdXG5cbmZvciBrIGluIGtfcmFuZ2U6XG4gICAga20gPSBLTWVhbnMobl9jbHVzdGVycz1rLCBpbml0PVx1MDAyN2stbWVhbnMrK1x1MDAyNywgbl9pbml0PTEwLCByYW5kb21fc3RhdGU9NDIpXG4gICAgbGFiZWxzID0ga20uZml0X3ByZWRpY3QoWClcbiAgICB3Y3NzX3ZhbHMuYXBwZW5kKGttLmluZXJ0aWFfKVxuICAgIHNpbF92YWxzLmFwcGVuZChzaWxob3VldHRlX3Njb3JlKFgsIGxhYmVscykpXG5cbndjc3NfYXJyID0gbnAuYXJyYXkod2Nzc192YWxzKVxuZGlmZnMyID0gbnAuZGlmZihucC5kaWZmKHdjc3NfYXJyKSlcbmVsYm93X2sgPSBsaXN0KGtfcmFuZ2UpW25wLmFyZ21heChkaWZmczIpICsgMV1cbmJlc3Rfc2lsX2sgPSBsaXN0KGtfcmFuZ2UpW25wLmFyZ21heChzaWxfdmFscyldXG5cbnByaW50KGZcIkVsYm93IG1ldGhvZCBzdWdnZXN0cyBrPXtlbGJvd19rfVwiKVxucHJpbnQoZlwiQmVzdCBzaWxob3VldHRlIGF0IGs9e2Jlc3Rfc2lsX2t9IChzY29yZT17bWF4KHNpbF92YWxzKTouNGZ9KVwiKVxucHJpbnQoXCJcXG5rICB8IFdDU1MgICAgICAgIHwgU2lsaG91ZXR0ZVwiKVxuZm9yIGssIHcsIHMgaW4gemlwKGtfcmFuZ2UsIHdjc3NfdmFscywgc2lsX3ZhbHMpOlxuICAgIG1hcmsgPSBcIiBcdTAwM2NcdTAwM2NcIiBpZiBrID09IGJlc3Rfc2lsX2sgZWxzZSBcIlwiXG4gICAgcHJpbnQoZlwie2s6MmR9IHwge3c6MTEuMmZ9IHwge3M6LjRmfXttYXJrfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1pbmktQmF0Y2ggSy1NZWFucyBmb3IgTGFyZ2UgRGF0YXNldHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIGstbWVhbnMgc2NhbGVzIGFzIE8obsK3a8K3ZCkgcGVyIGl0ZXJhdGlvbiwgd2hpY2ggYmVjb21lcyBleHBlbnNpdmUgZm9yIG1pbGxpb25zIG9mIHBvaW50cy4gTWluaS1iYXRjaCBrLW1lYW5zIHByb2Nlc3NlcyBhIHJhbmRvbSBtaW5pLWJhdGNoIGF0IGVhY2ggc3RlcCBhbmQgdXBkYXRlcyBjZW50cm9pZHMgd2l0aCBhIHJ1bm5pbmcgYXZlcmFnZSwgcmVkdWNpbmcgcGVyLWl0ZXJhdGlvbiBjb3N0IHRvIE8oYsK3a8K3ZCkgd2hlcmUgYiBpcyB0aGUgYmF0Y2ggc2l6ZS4gVGhlIGNlbnRyb2lkIHVwZGF0ZSBydWxlIGlzOiDOvCDihpAgzrwgKyAoMS9jb3VudCkoeCDiiJIgzrwpIGZvciBlYWNoIHBvaW50IGluIHRoZSBiYXRjaC4gVGhpcyB0cmFkZXMgYSBzbWFsbCBpbmNyZWFzZSBpbiBmaW5hbCBXQ1NTICh0eXBpY2FsbHkgMeKAkzUlKSBmb3IgYSBkcmFtYXRpYyByZWR1Y3Rpb24gaW4gd2FsbC1jbG9jayB0aW1lLCBtYWtpbmcgaXQgdGhlIGdvLXRvIGFsZ29yaXRobSBmb3Igc3RyZWFtaW5nIG9yIHZlcnkgbGFyZ2UgZGF0YXNldHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRpbWVcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBLTWVhbnMsIE1pbmlCYXRjaEtNZWFuc1xuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5YX2xhcmdlID0gcm5nLnN0YW5kYXJkX25vcm1hbCgoMzAwXzAwMCwgMTUpKVxuXG5rID0gMjBcbnJlc3VsdHMgPSB7fVxuXG50MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbmttID0gS01lYW5zKG5fY2x1c3RlcnM9aywgaW5pdD1cdTAwMjdrLW1lYW5zKytcdTAwMjcsIG5faW5pdD0zLCBtYXhfaXRlcj0xMDAsIHJhbmRvbV9zdGF0ZT00MilcbmttLmZpdChYX2xhcmdlWzozMF8wMDBdKVxucmVzdWx0c1tcdTAwMjdLTWVhbnMgKDMwSyBwdHMpXHUwMDI3XSA9IChrbS5pbmVydGlhXywgdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKVxuXG50MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbm1ia20gPSBNaW5pQmF0Y2hLTWVhbnMobl9jbHVzdGVycz1rLCBiYXRjaF9zaXplPTIwNDgsIG5faW5pdD01LFxuICAgICAgICAgICAgICAgICAgICAgICAgbWF4X2l0ZXI9MjAwLCByYW5kb21fc3RhdGU9NDIpXG5tYmttLmZpdChYX2xhcmdlKVxucmVzdWx0c1tcdTAwMjdNaW5pQmF0Y2ggKDMwMEsgcHRzKVx1MDAyN10gPSAobWJrbS5pbmVydGlhXywgdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKVxuXG5wcmludChmXCJ7XHUwMDI3QWxnb3JpdGhtXHUwMDI3Olx1MDAzYzI1fSB7XHUwMDI3SW5lcnRpYVx1MDAyNzpcdTAwM2UxNH0ge1x1MDAyN1RpbWUgKHMpXHUwMDI3Olx1MDAzZTEwfVwiKVxuZm9yIG5hbWUsIChpbmVydGlhLCBlbGFwc2VkKSBpbiByZXN1bHRzLml0ZW1zKCk6XG4gICAgcHJpbnQoZlwie25hbWU6XHUwMDNjMjV9IHtpbmVydGlhOlx1MDAzZTE0LjJmfSB7ZWxhcHNlZDpcdTAwM2UxMC4zZn1cIilcbnByaW50KFwiXFxuTWluaS1iYXRjaCBoYW5kbGVzIDEweCBtb3JlIGRhdGEgaW4gY29tcGFyYWJsZSB0aW1lLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkltYWdlIENvbXByZXNzaW9uIHZpYSBDb2xvciBRdWFudGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbG9yIHF1YW50aXphdGlvbiByZXByZXNlbnRzIGFuIGltYWdlIHVzaW5nIG9ubHkgayBjb2xvcnMgYnkgdHJlYXRpbmcgZWFjaCBwaXhlbFx1MDAyN3MgUkdCIHRyaXBsZXQgYXMgYSBwb2ludCBpbiAzRCBjb2xvciBzcGFjZSBhbmQgcnVubmluZyBrLW1lYW5zLiBFYWNoIHBpeGVsIGlzIHJlcGxhY2VkIGJ5IGl0cyBuZWFyZXN0IGNsdXN0ZXIgY2VudGVyIChyZXByZXNlbnRhdGl2ZSBjb2xvciksIHJlZHVjaW5nIHN0b3JhZ2UgZnJvbSAyNCBiaXRzL3BpeGVsIHRvIOKMiGxvZ+KCgiBr4oyJIGJpdHMvcGl4ZWwgcGx1cyB0aGUga8OXMjQtYml0IHBhbGV0dGUuIFRoZSBjb21wcmVzc2lvbiByYXRpbyBhbmQgTVNFIHJlY29uc3RydWN0aW9uIGVycm9yIGJvdGggZGVwZW5kIG9uIGsg4oCUIG1vcmUgY29sb3JzIG1lYW5zIGJldHRlciBxdWFsaXR5IGJ1dCBsZXNzIGNvbXByZXNzaW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBNaW5pQmF0Y2hLTWVhbnNcblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxuSCwgVyA9IDEyOCwgMTI4XG5wYWxldHRlID0gbnAuYXJyYXkoW1syMDAsNTAsNTBdLFs1MCwxODAsNTBdLFs1MCw1MCwyMDBdLFsyMDAsMTgwLDUwXSxbMTYwLDUwLDE4MF1dLCBkdHlwZT1ucC5mbG9hdDMyKVxucmVnaW9ucyA9IHJuZy5pbnRlZ2VycygwLCA1LCBzaXplPShILCBXKSlcbmltZyA9IHBhbGV0dGVbcmVnaW9uc10gKyBybmcubm9ybWFsKDAsIDEyLCAoSCwgVywgMykpXG5pbWcgPSBucC5jbGlwKGltZywgMCwgMjU1KS5hc3R5cGUobnAudWludDgpXG5cbnBpeGVscyA9IGltZy5yZXNoYXBlKC0xLCAzKS5hc3R5cGUobnAuZmxvYXQzMilcbm9yaWdpbmFsX2JpdHMgPSBIICogVyAqIDI0XG5cbnByaW50KGZcIkltYWdlOiB7SH14e1d9IHB4IHwge0gqV30gcGl4ZWxzIHwgT3JpZ2luYWw6IHtvcmlnaW5hbF9iaXRzIC8vIDggLy8gMTAyNDouMWZ9IEtCIHVuY29tcHJlc3NlZFwiKVxucHJpbnQoZlwie1x1MDAyN0NvbG9yc1x1MDAyNzpcdTAwM2U4fSB7XHUwMDI3TVNFXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3Qml0cy9weFx1MDAyNzpcdTAwM2U4fSB7XHUwMDI3UmF0aW9cdTAwMjc6XHUwMDNlOH1cIilcbmZvciBuX2NvbG9ycyBpbiBbMiwgNCwgOCwgMTYsIDMyLCA2NCwgMTI4XTpcbiAgICBrbSA9IE1pbmlCYXRjaEtNZWFucyhuX2NsdXN0ZXJzPW5fY29sb3JzLCByYW5kb21fc3RhdGU9NDIsIG5faW5pdD01KVxuICAgIGttLmZpdChwaXhlbHMpXG4gICAgcXVhbnRpemVkID0ga20uY2x1c3Rlcl9jZW50ZXJzX1trbS5sYWJlbHNfXVxuICAgIG1zZSA9IG5wLm1lYW4oKHBpeGVscyAtIHF1YW50aXplZCkgKiogMilcbiAgICBicHAgPSBpbnQobnAuY2VpbChucC5sb2cyKG5fY29sb3JzKSkpXG4gICAgcmF0aW8gPSBvcmlnaW5hbF9iaXRzIC8gKEggKiBXICogYnBwICsgbl9jb2xvcnMgKiAyNClcbiAgICBwcmludChmXCJ7bl9jb2xvcnM6XHUwMDNlOH0ge21zZTpcdTAwM2UxMC4yZn0ge2JwcDpcdTAwM2U4fSB7cmF0aW86XHUwMDNlOC4xZn14XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSy1NZWFucyBMaW1pdGF0aW9ucyBhbmQgQWx0ZXJuYXRpdmVzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTcGhlcmljYWwgY2x1c3RlciBhc3N1bXB0aW9uOiBXQ1NTIG1pbmltaXphdGlvbiBpcyBiaWFzZWQgdG93YXJkIHJvdW5kLCBlcXVhbC1zaXplZCBjbHVzdGVyczsgbm9uLWNvbnZleCBzaGFwZXMgbGlrZSBjcmVzY2VudHMgb3IgcmluZ3MgYXJlIHNwbGl0IGFyYml0cmFyaWx5LiIsIkVxdWFsLXNpemUgYmlhczogdGhlIFZvcm9ub2kgcGFydGl0aW9uIG5hdHVyYWxseSBjcmVhdGVzIHNpbWlsYXJseS1zaXplZCBjZWxscywgc28gdHJ1ZSBpbWJhbGFuY2VkIGNsdXN0ZXJzIGFyZSBvZnRlbiBtaXNpZGVudGlmaWVkLiIsIk91dGxpZXIgc2Vuc2l0aXZpdHk6IHRoZSBtZWFuIGlzIG5vdCByb2J1c3Q7IGEgc2luZ2xlIGV4dHJlbWUgcG9pbnQgZHJhZ3MgaXRzIGNlbnRyb2lkIGF3YXkgZnJvbSB0aGUgdHJ1ZSBjbHVzdGVyIGNlbnRlci4iLCJSZXF1aXJlcyBrIHVwZnJvbnQ6IHVubGlrZSBkZW5zaXR5LWJhc2VkIG1ldGhvZHMsIGsgbXVzdCBiZSBzcGVjaWZpZWQgYmVmb3JlIHJ1bm5pbmcg4oCUIGEgc2lnbmlmaWNhbnQgcHJhY3RpY2FsIGxpbWl0YXRpb24uIiwiTG9jYWwgb3B0aW1hOiBMbG95ZFx1MDAyN3MgYWxnb3JpdGhtIGNvbnZlcmdlcyB0byBhIGxvY2FsIG1pbmltdW07IHRoZSBnbG9iYWwgb3B0aW11bSBpcyBOUC1oYXJkIHRvIGZpbmQuIiwiSGlnaC1kaW1lbnNpb25hbCBmYWlsdXJlOiBpbiBoaWdoIGRpbWVuc2lvbnMgRXVjbGlkZWFuIGRpc3RhbmNlcyBjb25jZW50cmF0ZSAoYWxsIHBhaXJ3aXNlIGRpc3RhbmNlcyBiZWNvbWUgc2ltaWxhciksIGRlZ3JhZGluZyBjbHVzdGVyIHF1YWxpdHkuIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiV2hlbiBOb3QgdG8gVXNlIEstTWVhbnMiLCJjb250ZW50IjoiQXZvaWQgay1tZWFucyBmb3Igbm9uLWNvbnZleCBjbHVzdGVyIHNoYXBlcyAodXNlIERCU0NBTiBvciBzcGVjdHJhbCBjbHVzdGVyaW5nKSwgZm9yIGRhdGEgd2l0aCBzaWduaWZpY2FudCBvdXRsaWVycyAodXNlIGstbWVkb2lkcy9QQU0pLCBvciB3aGVuIHRoZSBudW1iZXIgb2YgY2x1c3RlcnMgaXMgdW5rbm93biBhbmQgaGFyZCB0byBlc3RpbWF0ZS4gSy1tZWRvaWRzIHJlcGxhY2VzIHRoZSBtZWFuIGNlbnRyb2lkIHdpdGggYW4gYWN0dWFsIGRhdGEgcG9pbnQgKHRoZSBtZWRvaWQpLCBtYWtpbmcgaXQgcm9idXN0IHRvIG91dGxpZXJzIHdoaWxlIHJldGFpbmluZyB0aGUgc2FtZSBhc3NpZ24tdXBkYXRlIHN0cnVjdHVyZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDbHVzdGVyaW5nIEFsZ29yaXRobSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFsZ29yaXRobSIsIkNsdXN0ZXIgQXNzdW1wdGlvbiIsIk91dGxpZXIgUm9idXN0IiwiQ2x1c3RlciBTaGFwZSIsImsgUmVxdWlyZWQiXSwicm93cyI6W1siSy1NZWFucyIsIlNwaGVyaWNhbCwgZXF1YWwtc2l6ZSBjbHVzdGVycyIsIk5vIOKAlCBtZWFuIHNoaWZ0cyB3aXRoIG91dGxpZXJzIiwiQ29udmV4IG9ubHkiLCJZZXMiXSxbIkstTWVkb2lkcyAoUEFNKSIsIlNwaGVyaWNhbCwgbWVkb2lkIGFzIGNlbnRlciIsIlllcyDigJQgbWVkb2lkIGlzIHJvYnVzdCB0byBleHRyZW1lcyIsIkNvbnZleCBvbmx5IiwiWWVzIl0sWyJEQlNDQU4iLCJEZW5zaXR5LWNvbm5lY3RlZCByZWdpb25zIiwiWWVzIOKAlCBub2lzZSBsYWJlbGVkIGV4cGxpY2l0bHkiLCJBcmJpdHJhcnkiLCJObyAozrUsIG1pblB0cykiXSxbIkdNTSIsIkdhdXNzaWFuLWRpc3RyaWJ1dGVkIGNsdXN0ZXJzIiwiUGFydGlhbCDigJQgc29mdCBhc3NpZ25tZW50cyBkaWx1dGVkIiwiRWxsaXB0aWNhbCIsIlllcyJdXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# K-Means Clustering — Lloyd's Algorithm and Initialization

K-Means is the most widely deployed clustering algorithm. Given n points and a target number of clusters k, it partitions the data to minimize the Within-Cluster Sum of Squares (WCSS). The algorithm alternates between two simple steps — assigning points to clusters and updating cluster centers — until convergence. Understanding its geometric objective, the k-means++ initialization strategy, and how to select k are essential for practical unsupervised learning.

## The K-Means Objective

K-Means minimizes WCSS = Σᵢ Σ_{x∈Cᵢ} ‖x − μᵢ‖² where Cᵢ is the i-th cluster and μᵢ is its centroid. This objective favors compact, spherical clusters of roughly equal size. Because WCSS is non-convex in both the assignments and centroids jointly, the algorithm converges to a local minimum rather than the global optimum. Finding the globally optimal k-means partition is NP-hard; in practice we run the algorithm with multiple restarts and keep the best result.

## Lloyd's Algorithm

Lloyd's algorithm alternates: (1) E-step — assign each point to its nearest centroid, which cannot increase WCSS for fixed centroids; (2) M-step — set each centroid to the mean of its assigned points, which minimizes WCSS for fixed assignments since the mean uniquely minimizes the sum of squared deviations. Because each step is non-increasing and WCSS is bounded below by zero, and there are finitely many distinct partitions of n points into k non-empty clusters, convergence in finite steps is guaranteed. The quality of the local minimum found depends heavily on initialization.

```python
import numpy as np
from sklearn.datasets import make_blobs

def kmeans_plus_plus(X, k, rng):
    """K-Means++ seeding — O(log k) approximation guarantee."""
    n = X.shape[0]
    centers = [X[rng.integers(n)].copy()]
    for _ in range(k - 1):
        dists = np.array([min(np.sum((x - c) ** 2) for c in centers) for x in X])
        probs = dists / dists.sum()
        centers.append(X[rng.choice(n, p=probs)].copy())
    return np.array(centers)

def lloyd_kmeans(X, k, max_iter=300, tol=1e-4, seed=42):
    """Lloyd's algorithm with K-Means++ initialization."""
    rng = np.random.default_rng(seed)
    centers = kmeans_plus_plus(X, k, rng)
    for it in range(max_iter):
        diffs = X[:, None, :] - centers[None, :, :]
        labels = np.argmin((diffs ** 2).sum(axis=2), axis=1)
        new_centers = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        shift = np.max(np.linalg.norm(new_centers - centers, axis=1))
        centers = new_centers
        if shift < tol:
            print(f"Converged at iteration {it + 1}")
            break
    wcss = sum(np.sum((X[labels == i] - centers[i]) ** 2) for i in range(k))
    return labels, centers, wcss

X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.8, random_state=42)
labels, centers, wcss = lloyd_kmeans(X, k=4)
print(f"Final WCSS: {wcss:.2f}")
print(f"Cluster sizes: {[int((labels == i).sum()) for i in range(4)]}")
```

## K-Means++ Initialization

Random initialization frequently lands in poor local optima. K-Means++ seeds centroids spread across the data by choosing each new centroid with probability proportional to its squared distance from the nearest already-chosen centroid. This gives a theoretical guarantee: E[WCSS_init] ≤ O(log k) × OPT. In practice k-means++ reduces variance across restarts dramatically and usually reaches a good solution in 3–5 restarts rather than the 20–50 needed with pure random initialization.

- Choose first centroid uniformly at random from the data.
- For each remaining point x, compute d²(x) = min squared distance to the nearest chosen centroid.
- Sample the next centroid with probability proportional to d²(x) — farther points are more likely to be chosen.
- Repeat steps 2–3 until k centroids are selected, then run Lloyd's algorithm.
- Guarantee: E[WCSS] ≤ 8(ln k + 2) × OPT — a logarithmic approximation factor.

## Choosing K — Elbow, Silhouette, and Gap Statistic

Selecting k is unsupervised — there is no ground truth label. Three complementary diagnostics help: (1) Elbow method — plot WCSS vs k; the 'elbow' (largest second derivative) indicates diminishing returns from adding clusters. (2) Silhouette score — s(i) = (b(i)−a(i)) / max(a(i),b(i)) where a(i) is the mean intra-cluster distance and b(i) is the mean distance to the nearest other cluster; range [−1,1], higher is better. (3) Gap statistic — compares log(WCSS_k) to its expected value under a null uniform reference distribution; choose the smallest k where Gap(k) ≥ Gap(k+1) − se(k+1).

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=500, centers=5, cluster_std=0.9, random_state=0)

k_range = range(2, 11)
wcss_vals, sil_vals = [], []

for k in k_range:
    km = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    labels = km.fit_predict(X)
    wcss_vals.append(km.inertia_)
    sil_vals.append(silhouette_score(X, labels))

wcss_arr = np.array(wcss_vals)
diffs2 = np.diff(np.diff(wcss_arr))
elbow_k = list(k_range)[np.argmax(diffs2) + 1]
best_sil_k = list(k_range)[np.argmax(sil_vals)]

print(f"Elbow method suggests k={elbow_k}")
print(f"Best silhouette at k={best_sil_k} (score={max(sil_vals):.4f})")
print("\nk  | WCSS        | Silhouette")
for k, w, s in zip(k_range, wcss_vals, sil_vals):
    mark = " <<" if k == best_sil_k else ""
    print(f"{k:2d} | {w:11.2f} | {s:.4f}{mark}")
```

## Mini-Batch K-Means for Large Datasets

Standard k-means scales as O(n·k·d) per iteration, which becomes expensive for millions of points. Mini-batch k-means processes a random mini-batch at each step and updates centroids with a running average, reducing per-iteration cost to O(b·k·d) where b is the batch size. The centroid update rule is: μ ← μ + (1/count)(x − μ) for each point in the batch. This trades a small increase in final WCSS (typically 1–5%) for a dramatic reduction in wall-clock time, making it the go-to algorithm for streaming or very large datasets.

```python
import numpy as np
import time
from sklearn.cluster import KMeans, MiniBatchKMeans

rng = np.random.default_rng(42)
X_large = rng.standard_normal((300_000, 15))

k = 20
results = {}

t0 = time.perf_counter()
km = KMeans(n_clusters=k, init='k-means++', n_init=3, max_iter=100, random_state=42)
km.fit(X_large[:30_000])
results['KMeans (30K pts)'] = (km.inertia_, time.perf_counter() - t0)

t0 = time.perf_counter()
mbkm = MiniBatchKMeans(n_clusters=k, batch_size=2048, n_init=5,
                        max_iter=200, random_state=42)
mbkm.fit(X_large)
results['MiniBatch (300K pts)'] = (mbkm.inertia_, time.perf_counter() - t0)

print(f"{'Algorithm':<25} {'Inertia':>14} {'Time (s)':>10}")
for name, (inertia, elapsed) in results.items():
    print(f"{name:<25} {inertia:>14.2f} {elapsed:>10.3f}")
print("\nMini-batch handles 10x more data in comparable time.")
```

## Image Compression via Color Quantization

Color quantization represents an image using only k colors by treating each pixel's RGB triplet as a point in 3D color space and running k-means. Each pixel is replaced by its nearest cluster center (representative color), reducing storage from 24 bits/pixel to ⌈log₂ k⌉ bits/pixel plus the k×24-bit palette. The compression ratio and MSE reconstruction error both depend on k — more colors means better quality but less compression.

```python
import numpy as np
from sklearn.cluster import MiniBatchKMeans

rng = np.random.default_rng(42)
H, W = 128, 128
palette = np.array([[200,50,50],[50,180,50],[50,50,200],[200,180,50],[160,50,180]], dtype=np.float32)
regions = rng.integers(0, 5, size=(H, W))
img = palette[regions] + rng.normal(0, 12, (H, W, 3))
img = np.clip(img, 0, 255).astype(np.uint8)

pixels = img.reshape(-1, 3).astype(np.float32)
original_bits = H * W * 24

print(f"Image: {H}x{W} px | {H*W} pixels | Original: {original_bits // 8 // 1024:.1f} KB uncompressed")
print(f"{'Colors':>8} {'MSE':>10} {'Bits/px':>8} {'Ratio':>8}")
for n_colors in [2, 4, 8, 16, 32, 64, 128]:
    km = MiniBatchKMeans(n_clusters=n_colors, random_state=42, n_init=5)
    km.fit(pixels)
    quantized = km.cluster_centers_[km.labels_]
    mse = np.mean((pixels - quantized) ** 2)
    bpp = int(np.ceil(np.log2(n_colors)))
    ratio = original_bits / (H * W * bpp + n_colors * 24)
    print(f"{n_colors:>8} {mse:>10.2f} {bpp:>8} {ratio:>8.1f}x")
```

## K-Means Limitations and Alternatives

- Spherical cluster assumption: WCSS minimization is biased toward round, equal-sized clusters; non-convex shapes like crescents or rings are split arbitrarily.
- Equal-size bias: the Voronoi partition naturally creates similarly-sized cells, so true imbalanced clusters are often misidentified.
- Outlier sensitivity: the mean is not robust; a single extreme point drags its centroid away from the true cluster center.
- Requires k upfront: unlike density-based methods, k must be specified before running — a significant practical limitation.
- Local optima: Lloyd's algorithm converges to a local minimum; the global optimum is NP-hard to find.
- High-dimensional failure: in high dimensions Euclidean distances concentrate (all pairwise distances become similar), degrading cluster quality.

> **When Not to Use K-Means**: Avoid k-means for non-convex cluster shapes (use DBSCAN or spectral clustering), for data with significant outliers (use k-medoids/PAM), or when the number of clusters is unknown and hard to estimate. K-medoids replaces the mean centroid with an actual data point (the medoid), making it robust to outliers while retaining the same assign-update structure.

## Clustering Algorithm Comparison

| Algorithm | Cluster Assumption | Outlier Robust | Cluster Shape | k Required |
| --- | --- | --- | --- | --- |
| K-Means | Spherical, equal-size clusters | No — mean shifts with outliers | Convex only | Yes |
| K-Medoids (PAM) | Spherical, medoid as center | Yes — medoid is robust to extremes | Convex only | Yes |
| DBSCAN | Density-connected regions | Yes — noise labeled explicitly | Arbitrary | No (ε, minPts) |
| GMM | Gaussian-distributed clusters | Partial — soft assignments diluted | Elliptical | Yes |

---

