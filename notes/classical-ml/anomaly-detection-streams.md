---
title: "Streaming Anomaly Detection — CUSUM, ADWIN, Online Methods"
slug: "anomaly-detection-streams"
description: "Detect anomalies and concept drift in high-frequency data streams: CUSUM for mean shifts, ADWIN for adaptive windowing, Half-Space Trees for online isolation, and concept drift simulation comparing detector response times."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmF0Y2ggYW5vbWFseSBkZXRlY3Rpb24gaXMgaW5mZWFzaWJsZSBmb3IgaGlnaC1mcmVxdWVuY3kgZGF0YSBzdHJlYW1zOiBmaXR0aW5nIGEgbW9kZWwgYW5kIHNjYW5uaW5nIGFsbCBkYXRhIHJldHJvc3BlY3RpdmVseSBpbnRyb2R1Y2VzIHVuYWNjZXB0YWJsZSBsYXRlbmN5IGFuZCBtZW1vcnkgcmVxdWlyZW1lbnRzLiBTdHJlYW1pbmcgYW5vbWFseSBkZXRlY3Rpb24gYWxnb3JpdGhtcyBwcm9jZXNzIGVhY2ggb2JzZXJ2YXRpb24gaW4gTygxKSBvciBPKGxvZyBuKSB0aW1lLCBtYWludGFpbmluZyBvbmx5IGEgY29tcGFjdCBzdW1tYXJ5IG9mIHJlY2VudCBoaXN0b3J5LiBUaGlzIG5vdGUgY292ZXJzIENVU1VNIGZvciBwZXJzaXN0ZW50IHNoaWZ0IGRldGVjdGlvbiwgQURXSU4gZm9yIGFkYXB0aXZlIHdpbmRvd2luZyBhbmQgZHJpZnQgZGV0ZWN0aW9uLCBIYWxmLVNwYWNlIFRyZWVzIGZvciBvbmxpbmUgaXNvbGF0aW9uIHNjb3JpbmcsIGFuZCBtZXRob2RzIGZvciBldmFsdWF0aW5nIHN0cmVhbSBkZXRlY3RvcnMgdW5kZXIgdmFyaW91cyBjb25jZXB0IGRyaWZ0IHR5cGVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNVU1VNIOKAlCBDdW11bGF0aXZlIFN1bSBDb250cm9sIENoYXJ0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDVVNVTSAoUGFnZSAxOTU0KSB0cmFja3MgY3VtdWxhdGl2ZSBkZXZpYXRpb24gZnJvbSBhbiBleHBlY3RlZCBtZWFuIM68LiBGb3IgZGV0ZWN0aW5nIHVwd2FyZCBzaGlmdHM6IENVU1VN4oG6X3QgPSBtYXgoMCwgQ1VTVU3igbpfe3QtMX0gKyAoeF90IC0gzrwgLSBrKSkgd2hlcmUgayA9ICjOvF8xIC0gzrxfMCkvMiBpcyB0aGUgc2xhY2sgKGhhbGYgdGhlIGV4cGVjdGVkIHNoaWZ0IG1hZ25pdHVkZSkuIEFuIGFsYXJtIGZpcmVzIHdoZW4gQ1VTVU3igbpfdCBcdTAwM2UgaCB3aGVyZSBoIGlzIHRoZSBkZXRlY3Rpb24gdGhyZXNob2xkLiBUaGUgbWV0aG9kIGlzIHNlbnNpdGl2ZSB0byBzbWFsbCBwZXJzaXN0ZW50IHNoaWZ0cyAoc2lnbmFsLXRvLW5vaXNlIHJhdGlvIG1hdHRlcnMpIGFuZCBoYXMgTygxKSBwZXItc3RlcCBjb21wbGV4aXR5LiBBZnRlciBhbiBhbGFybSwgdGhlIHN0YXRpc3RpYyBpcyByZXNldCB0byAwLiBDVVNVTSBpcyBvcHRpbWFsIChtaW5pbWlzZXMgZXhwZWN0ZWQgZGV0ZWN0aW9uIGRlbGF5KSBmb3IgR2F1c3NpYW4gb2JzZXJ2YXRpb25zIHdpdGgga25vd24gcHJlLSBhbmQgcG9zdC1jaGFuZ2UgbWVhbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY3VzdW1fZGV0ZWN0b3Ioc3RyZWFtLCBtdTA9MC4wLCBrPTAuNSwgaD01LjApOlxuICAgIFwiXCJcIlxuICAgIFR3by1zaWRlZCBDVVNVTSBkZXRlY3Rvci5cbiAgICBrOiBzbGFjayAoaGFsZiB0aGUgZXhwZWN0ZWQgc2hpZnQgbWFnbml0dWRlKVxuICAgIGg6IHRocmVzaG9sZCBmb3IgYWxhcm1cbiAgICBSZXR1cm5zIGxpc3Qgb2YgYWxhcm0gaW5kaWNlcy5cbiAgICBcIlwiXCJcbiAgICBjdXN1bV9wb3MgPSAwLjBcbiAgICBjdXN1bV9uZWcgPSAwLjBcbiAgICBhbGFybXMgPSBbXVxuICAgIGZvciBpLCB4IGluIGVudW1lcmF0ZShzdHJlYW0pOlxuICAgICAgICBjdXN1bV9wb3MgPSBtYXgoMCwgY3VzdW1fcG9zICsgKHggLSBtdTApIC0gaylcbiAgICAgICAgY3VzdW1fbmVnID0gbWF4KDAsIGN1c3VtX25lZyAtICh4IC0gbXUwKSAtIGspXG4gICAgICAgIGlmIGN1c3VtX3BvcyBcdTAwM2UgaCBvciBjdXN1bV9uZWcgXHUwMDNlIGg6XG4gICAgICAgICAgICBhbGFybXMuYXBwZW5kKGkpXG4gICAgICAgICAgICBjdXN1bV9wb3MgPSAwLjAgICMgcmVzZXQgYWZ0ZXIgYWxhcm1cbiAgICAgICAgICAgIGN1c3VtX25lZyA9IDAuMFxuICAgIHJldHVybiBhbGFybXNcblxubnAucmFuZG9tLnNlZWQoNDIpXG5ub3JtYWxfc2VnbWVudCA9IG5wLnJhbmRvbS5yYW5kbigyMDApXG5zaGlmdF9zZWdtZW50ICA9IG5wLnJhbmRvbS5yYW5kbigxMDApICsgMS41ICAjIG1lYW4gc2hpZnQgb2YgMS41XG5zdHJlYW0gPSBucC5jb25jYXRlbmF0ZShbbm9ybWFsX3NlZ21lbnQsIHNoaWZ0X3NlZ21lbnRdKVxuXG5hbGFybXMgPSBjdXN1bV9kZXRlY3RvcihzdHJlYW0sIG11MD0wLjAsIGs9MC41LCBoPTUuMClcbmZpcnN0X2FsYXJtID0gYWxhcm1zWzBdIGlmIGFsYXJtcyBlbHNlIE5vbmVcbnByaW50KGZcdTAwMjdUcnVlIGNoYW5nZSBwb2ludDogMjAwXHUwMDI3KVxucHJpbnQoZlx1MDAyN0NVU1VNIGZpcnN0IGFsYXJtOiB7Zmlyc3RfYWxhcm19ICAoZGV0ZWN0aW9uIGRlbGF5OiB7Zmlyc3RfYWxhcm0gLSAyMDAgaWYgZmlyc3RfYWxhcm0gZWxzZSBcIm5vIGFsYXJtXCJ9KVx1MDAyNylcbnByaW50KGZcdTAwMjdUb3RhbCBhbGFybXMgZmlyZWQ6IHtsZW4oYWxhcm1zKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQURXSU4g4oCUIEFkYXB0aXZlIFdpbmRvd2luZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQURXSU4gKEJpZmV0IFx1MDAyNiBHYXZhbGRhLCAyMDA3KSBtYWludGFpbnMgYSB2YXJpYWJsZS1sZW5ndGggd2luZG93IG9mIHJlY2VudCBkYXRhLiBJdCBkZXRlY3RzIGRpc3RyaWJ1dGlvbiBzaGlmdCBieSBwYXJ0aXRpb25pbmcgdGhlIHdpbmRvdyBpbnRvIHR3byBjb25zZWN1dGl2ZSBzdWItd2luZG93cyBhbmQgdGVzdGluZyB3aGV0aGVyIHRoZWlyIG1lYW5zIGRpZmZlciBzaWduaWZpY2FudGx5IHVzaW5nIHRoZSBIb2VmZmRpbmcgYm91bmQuIElmIGEgc2lnbmlmaWNhbnQgZGlmZmVyZW5jZSBpcyBmb3VuZCwgdGhlIG9sZGVyIHBvcnRpb24gaXMgZGlzY2FyZGVkICh0aGUgd2luZG93IHNocmlua3MpLiBBRFdJTiBwcm92aWRlcyB0aGVvcmV0aWNhbCBndWFyYW50ZWVzOiBmYWxzZSBhbGFybSByYXRlIGlzIGF0IG1vc3QgzrQgKHVzZXItc3BlY2lmaWVkKSwgYW5kIGl0IGRldGVjdHMgYWxsIGRpc3RyaWJ1dGlvbiBzaGlmdHMgd2l0aCBwcm9iYWJpbGl0eSDiiaUgMS3OtCBhZnRlciBPKGxvZyBuKSBvYnNlcnZhdGlvbnMuIFdpbmRvdyBzaXplIGFkYXB0cyBhdXRvbWF0aWNhbGx5IOKAlCBsYXJnZSB3aW5kb3dzIGR1cmluZyBzdGFibGUgcGVyaW9kcywgc21hbGwgd2luZG93cyBhZnRlciBkcmlmdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbnRyeTpcbiAgICBmcm9tIHJpdmVyLmRyaWZ0IGltcG9ydCBBRFdJTlxuICAgIGZyb20gcml2ZXIuZGF0YXNldHMgaW1wb3J0IHN5bnRoXG5cbiAgICBhZHdpbiA9IEFEV0lOKGRlbHRhPTAuMDAyKVxuICAgIG5wLnJhbmRvbS5zZWVkKDQyKVxuICAgIHN0cmVhbV92YWxzID0gbnAuY29uY2F0ZW5hdGUoW1xuICAgICAgICBucC5yYW5kb20ucmFuZG4oMzAwKSxcbiAgICAgICAgbnAucmFuZG9tLnJhbmRuKDIwMCkgKyAyLjUsICAgIyBjb25jZXB0IGRyaWZ0IGF0IHN0ZXAgMzAwXG4gICAgICAgIG5wLnJhbmRvbS5yYW5kbigyMDApLFxuICAgIF0pXG4gICAgYWxhcm1zLCB3aW5kb3dfc2l6ZXMgPSBbXSwgW11cbiAgICBmb3IgaSwgeCBpbiBlbnVtZXJhdGUoc3RyZWFtX3ZhbHMpOlxuICAgICAgICBhZHdpbi51cGRhdGUoeClcbiAgICAgICAgd2luZG93X3NpemVzLmFwcGVuZChhZHdpbi53aWR0aClcbiAgICAgICAgaWYgYWR3aW4uZHJpZnRfZGV0ZWN0ZWQ6XG4gICAgICAgICAgICBhbGFybXMuYXBwZW5kKGkpXG5cbiAgICBwcmludChmXHUwMDI3VHJ1ZSBkcmlmdCBwb2ludHM6IFszMDAsIDUwMF1cdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN0FEV0lOIGFsYXJtcyBhdDoge2FsYXJtc31cdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN1dpbmRvdyBzaXplIGF0IHN0YWJsZSByZWdpb24gKHQ9MTUwKToge3dpbmRvd19zaXplc1sxNTBdfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3V2luZG93IHNpemUganVzdCBhZnRlciBkcmlmdCAodD0zMjApOiB7d2luZG93X3NpemVzW21pbigzMjAsIGxlbih3aW5kb3dfc2l6ZXMpLTEpXX1cdTAwMjcpXG5leGNlcHQgSW1wb3J0RXJyb3I6XG4gICAgcHJpbnQoXHUwMDI3SW5zdGFsbCByaXZlcjogcGlwIGluc3RhbGwgcml2ZXJcdTAwMjcpXG4gICAgcHJpbnQoXHUwMDI3QURXSU4gdXNhZ2U6XHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgZnJvbSByaXZlci5kcmlmdCBpbXBvcnQgQURXSU5cdTAwMjcpXG4gICAgcHJpbnQoXHUwMDI3ICBhZHdpbiA9IEFEV0lOKGRlbHRhPTAuMDAyKVx1MDAyNylcbiAgICBwcmludChcdTAwMjcgIGZvciB4IGluIHN0cmVhbTogYWR3aW4udXBkYXRlKHgpOyBpZiBhZHdpbi5kcmlmdF9kZXRlY3RlZDogaGFuZGxlKClcdTAwMjcpXG4gICAgcHJpbnQoXHUwMDI3ICBhZHdpbi53aWR0aDogY3VycmVudCB3aW5kb3cgc2l6ZSAoYWRhcHRzIGF1dG9tYXRpY2FsbHkpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhhbGYtU3BhY2UgVHJlZXMgZm9yIFN0cmVhbWluZyBBbm9tYWx5IERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSGFsZi1TcGFjZSBUcmVlcyAoSFNUOyBUYW4gZXQgYWwuLCAyMDExKSBhcmUgYW4gb25saW5lIHZlcnNpb24gb2YgSXNvbGF0aW9uIEZvcmVzdCBhZGFwdGVkIGZvciBkYXRhIHN0cmVhbXMuIEVhY2ggdHJlZSBwYXJ0aXRpb25zIHRoZSBmZWF0dXJlIHNwYWNlIHVzaW5nIHJhbmRvbSBheGlzLWFsaWduZWQgc3BsaXRzLiBBbm9tYWx5IHNjb3JlID0gbWFzcyBvZiB0aGUgbGVhZiBub2RlIHRoZSBzYW1wbGUgZmFsbHMgaW50byAoaGlnaGVyIG1hc3MgPSBtb3JlIG5vcm1hbCkuIEhTVCB1cGRhdGVzIGluY3JlbWVudGFsbHk6IGV2ZXJ5IHdpbmRvd19zaXplIHN0ZXBzLCB0aGUgcmVmZXJlbmNlIGFuZCBsYXRlc3Qgd2luZG93cyBzd2FwIGFuZCBsZWFmIG1hc3NlcyBhcmUgdXBkYXRlZC4gSFNUIGhhbmRsZXMgY29uY2VwdCBkcmlmdCBuYXR1cmFsbHkgYW5kIGFjaGlldmVzIE8oMSkgYW1vcnRpc2VkIHVwZGF0ZSB0aW1lIHBlciBvYnNlcnZhdGlvbi4gSXQgaXMgaW1wbGVtZW50ZWQgaW4gUml2ZXIgYXMgSGFsZlNwYWNlVHJlZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG50cnk6XG4gICAgZnJvbSByaXZlci5hbm9tYWx5IGltcG9ydCBIYWxmU3BhY2VUcmVlc1xuXG4gICAgaHN0ID0gSGFsZlNwYWNlVHJlZXMoXG4gICAgICAgIG5fdHJlZXM9MjUsXG4gICAgICAgIGhlaWdodD04LFxuICAgICAgICB3aW5kb3dfc2l6ZT0yNTAsXG4gICAgICAgIGxpbWl0cz17MDogKDAsIDEpLCAxOiAoMCwgMSl9LFxuICAgIClcbiAgICBucC5yYW5kb20uc2VlZCg3KVxuICAgIG5vcm1hbF9kYXRhICAgPSBucC5yYW5kb20udW5pZm9ybSgwLjIsIDAuOCwgKDQwMCwgMikpXG4gICAgYW5vbWFseV9kYXRhICA9IG5wLnJhbmRvbS51bmlmb3JtKDAuMCwgMC4wNSwgKDIwLCAyKSkgICMgY29ybmVyIGFub21hbGllc1xuICAgIHN0cmVhbV9kYXRhICAgPSBucC52c3RhY2soW25vcm1hbF9kYXRhLCBhbm9tYWx5X2RhdGFdKVxuICAgIHN0cmVhbV9sYWJlbHMgPSBbMF0qNDAwICsgWzFdKjIwXG5cbiAgICBzY29yZXMgPSBbXVxuICAgIGZvciBwb2ludCBpbiBzdHJlYW1fZGF0YTpcbiAgICAgICAgb2JzID0gezA6IHBvaW50WzBdLCAxOiBwb2ludFsxXX1cbiAgICAgICAgc2NvcmUgPSBoc3Quc2NvcmVfb25lKG9icylcbiAgICAgICAgaHN0LmxlYXJuX29uZShvYnMpXG4gICAgICAgIHNjb3Jlcy5hcHBlbmQoc2NvcmUpXG5cbiAgICBzY29yZXMgPSBucC5hcnJheShzY29yZXMpXG4gICAgdGhyZXNob2xkID0gbnAucGVyY2VudGlsZShzY29yZXNbOjQwMF0sIDk1KVxuICAgIHRwID0gbnAuc3VtKHNjb3Jlc1s0MDA6XSBcdTAwM2UgdGhyZXNob2xkKVxuICAgIGZwID0gbnAuc3VtKHNjb3Jlc1s6NDAwXSBcdTAwM2UgdGhyZXNob2xkKVxuICAgIHByaW50KGZcdTAwMjdBbm9tYWx5IHNjb3JlIHRocmVzaG9sZCAoOTV0aCBwY3Qgbm9ybWFsKToge3RocmVzaG9sZDouNGZ9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdUcnVlIHBvc2l0aXZlczoge3RwfS8yMCwgRmFsc2UgcG9zaXRpdmVzOiB7ZnB9LzQwMFx1MDAyNylcbmV4Y2VwdCBJbXBvcnRFcnJvcjpcbiAgICBwcmludChcdTAwMjdJbnN0YWxsIHJpdmVyOiBwaXAgaW5zdGFsbCByaXZlclx1MDAyNylcbiAgICBwcmludChcdTAwMjdIYWxmU3BhY2VUcmVlczogb25saW5lIGFub21hbHkgc2NvcmluZyBpbiBPKDEpIHBlciBvYnNlcnZhdGlvblx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25jZXB0IERyaWZ0IOKAlCBUeXBlcyBhbmQgQ2hhbGxlbmdlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uY2VwdCBkcmlmdCBvY2N1cnMgd2hlbiB0aGUgZGF0YSBkaXN0cmlidXRpb24gUChYLCB5KSBjaGFuZ2VzIG92ZXIgdGltZS4gRGlmZmVyZW50IGRyaWZ0IHR5cGVzIHJlcXVpcmUgZGlmZmVyZW50IGRldGVjdGlvbiBzdHJhdGVnaWVzLiBTdWRkZW4gZHJpZnQgKGFicnVwdCBjaGFuZ2UpIGlzIGVhc2llc3QgdG8gZGV0ZWN0IHdpdGggQ1VTVU0uIEdyYWR1YWwgZHJpZnQgKHNsb3cgdHJhbnNpdGlvbikgcmVxdWlyZXMgc2xpZGluZyB3aW5kb3cgbWV0aG9kcy4gSW5jcmVtZW50YWwgZHJpZnQgKG1vbm90b25lIHNoaWZ0KSBjYW4gYmUgdHJhY2tlZCB3aXRoIEFEV0lO4oCZcyBhZGFwdGl2ZSB3aW5kb3cuIFJlY3VycmluZyBkcmlmdCAocGVyaW9kaWMgc2Vhc29uYWxpdHkgb3IgcmVnaW1lIHNoaWZ0cykgcmVxdWlyZXMgbWVtb3J5IG9mIHBhc3QgY29uY2VwdHMuIEV2YWx1YXRpbmcgZGV0ZWN0b3JzIHJlcXVpcmVzIHNpbXVsYXRpb24gYmVjYXVzZSByZWFsLXdvcmxkIGRyaWZ0IGdyb3VuZCB0cnV0aCBpcyByYXJlbHkgYXZhaWxhYmxlLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3VkZGVuIGRyaWZ0OiBQIGNoYW5nZXMgYWJydXB0bHkgYXQgb25lIHBvaW50IOKAlCBDVVNVTSBhbmQgUGFnZS1IaW5rbGV5IGFyZSBvcHRpbWFsLiIsIkdyYWR1YWwgZHJpZnQ6IFAgdHJhbnNpdGlvbnMgb3ZlciBhIHdpbmRvdyBXIOKAlCBBRFdJTiBhbmQgc2xpZGluZyB3aW5kb3cgZGV0ZWN0b3JzIHdvcmsgd2VsbC4iLCJJbmNyZW1lbnRhbCBkcmlmdDogUCBzaGlmdHMgbW9ub3RvbmljYWxseSDigJQgcmVxdWlyZXMgbW9kZWxzIHRoYXQgY29udGludW91c2x5IHVwZGF0ZSBwYXJhbWV0ZXJzLiIsIlJlY3VycmluZyBkcmlmdDogUCBjeWNsZXMgYmV0d2VlbiBrbm93biBjb25jZXB0cyDigJQgY29uY2VwdCBsaWJyYXJpZXMgYW5kIGVuc2VtYmxlIHN3aXRjaGluZyBuZWVkZWQuIiwiQ292YXJpYXRlIHNoaWZ0OiBQKFgpIGNoYW5nZXMgYnV0IFAoeXxYKSBzdGF5cyB0aGUgc2FtZSDigJQgaW1wb3J0YW5jZSB3ZWlnaHRpbmcgcmF0aGVyIHRoYW4gZHJpZnQgZGV0ZWN0aW9uLiIsIlJlYWwgZHJpZnQ6IFAoeXxYKSBjaGFuZ2VzIOKAlCByZXF1aXJlcyBsYWJlbGxlZCBmZWVkYmFjazsgZGV0ZWN0aW9uIGRlbGF5cyBhcmUgdW5hdm9pZGFibGUgd2l0aG91dCBsYWJlbHMuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmluZyBEZXRlY3RvciBSZXNwb25zZSB0byBTaW11bGF0ZWQgRHJpZnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIGNvbXBhcmUgZGV0ZWN0b3JzLCBzaW11bGF0ZSBzdHJlYW1zIHdpdGgga25vd24gY2hhbmdlIHBvaW50cyBhbmQgbWVhc3VyZSBkZXRlY3Rpb24gZGVsYXkgKHN0ZXBzIGFmdGVyIHRydWUgZHJpZnQgdW50aWwgYWxhcm0pIGFuZCBmYWxzZSBhbGFybSByYXRlIChhbGFybXMgcGVyIDEwMDAgbm9ybWFsIHN0ZXBzKS4gTG93ZXIgZGV0ZWN0aW9uIGRlbGF5IGFuZCBsb3dlciBmYWxzZSBhbGFybSByYXRlIGFyZSBib3RoIGRlc2lyYWJsZSDigJQgdGhlcmUgaXMgdHlwaWNhbGx5IGEgdHJhZGUtb2ZmIGNvbnRyb2xsZWQgYnkgdGhlIGRldGVjdGlvbiB0aHJlc2hvbGQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY3VzdW0oc3RyZWFtLCBtdTAsIGssIGgpOlxuICAgIHMsIGFsYXJtcyA9IDAuMCwgW11cbiAgICBmb3IgaSwgeCBpbiBlbnVtZXJhdGUoc3RyZWFtKTpcbiAgICAgICAgcyA9IG1heCgwLCBzICsgeCAtIG11MCAtIGspXG4gICAgICAgIGlmIHMgXHUwMDNlIGg6XG4gICAgICAgICAgICBhbGFybXMuYXBwZW5kKGkpXG4gICAgICAgICAgICBzID0gMC4wXG4gICAgcmV0dXJuIGFsYXJtc1xuXG5kZWYgcGFnZV9oaW5rbGV5KHN0cmVhbSwgZGVsdGE9MC4wMDUsIHRocmVzaG9sZD01MCwgYWxwaGE9MS4wKTpcbiAgICBcIlwiXCJQYWdlLUhpbmtsZXkgdGVzdCBmb3IgbWVhbiBzaGlmdHMuXCJcIlwiXG4gICAgbV90ID0geF9iYXIgPSAwLjBcbiAgICBhbGFybXMsIG4gPSBbXSwgMFxuICAgIGZvciBpLCB4IGluIGVudW1lcmF0ZShzdHJlYW0pOlxuICAgICAgICBuICs9IDFcbiAgICAgICAgeF9iYXIgKz0gKHggLSB4X2JhcikgLyBuXG4gICAgICAgIG1fdCArPSB4IC0geF9iYXIgLSBkZWx0YVxuICAgICAgICBpZiBtX3QgXHUwMDNlIHRocmVzaG9sZDpcbiAgICAgICAgICAgIGFsYXJtcy5hcHBlbmQoaSlcbiAgICAgICAgICAgIG1fdCA9IDAuMFxuICAgIHJldHVybiBhbGFybXNcblxubnAucmFuZG9tLnNlZWQoMClcbm5vcm1hbCAgID0gbnAucmFuZG9tLnJhbmRuKDUwMClcbnNoaWZ0ZWQgID0gbnAucmFuZG9tLnJhbmRuKDMwMCkgKyAyLjBcbnN0cmVhbSAgID0gbnAuY29uY2F0ZW5hdGUoW25vcm1hbCwgc2hpZnRlZF0pXG50cnVlX2NwICA9IDUwMFxuXG5jdXN1bV9hbGFybXMgPSBjdXN1bShzdHJlYW0sIG11MD0wLjAsIGs9MC41LCBoPTQuMClcbnBoX2FsYXJtcyAgICA9IHBhZ2VfaGlua2xleShzdHJlYW0sIGRlbHRhPTAuMDEsIHRocmVzaG9sZD00MClcblxuY3VzdW1fZGVsYXkgPSBjdXN1bV9hbGFybXNbMF0gLSB0cnVlX2NwIGlmIGN1c3VtX2FsYXJtcyBlbHNlIGZsb2F0KFx1MDAyN2luZlx1MDAyNylcbnBoX2RlbGF5ICAgID0gcGhfYWxhcm1zWzBdICAgIC0gdHJ1ZV9jcCBpZiBwaF9hbGFybXMgICAgZWxzZSBmbG9hdChcdTAwMjdpbmZcdTAwMjcpXG5wcmludChmXHUwMDI3VHJ1ZSBjaGFuZ2UgcG9pbnQ6IHt0cnVlX2NwfVx1MDAyNylcbnByaW50KGZcdTAwMjdDVVNVTSBmaXJzdCBhbGFybToge2N1c3VtX2FsYXJtc1swXSBpZiBjdXN1bV9hbGFybXMgZWxzZSBcIm5vbmVcIn0gIGRlbGF5PXtjdXN1bV9kZWxheX1cdTAwMjcpXG5wcmludChmXHUwMDI3UGFnZS1IaW5rbGV5OiAgICAgIHtwaF9hbGFybXNbMF0gaWYgcGhfYWxhcm1zIGVsc2UgXCJub25lXCJ9ICBkZWxheT17cGhfZGVsYXl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0NVU1VNIGZhbHNlIGFsYXJtcyAoZmlyc3QgNTAwKToge3N1bShhIFx1MDAzYyA1MDAgZm9yIGEgaW4gY3VzdW1fYWxhcm1zKX1cdTAwMjcpXG5wcmludChmXHUwMDI3UEggICAgZmFsc2UgYWxhcm1zIChmaXJzdCA1MDApOiB7c3VtKGEgXHUwMDNjIDUwMCBmb3IgYSBpbiBwaF9hbGFybXMpfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkRldGVjdGlvbiBEZWxheSB2cyBGYWxzZSBBbGFybSBUcmFkZS1vZmYiLCJjb250ZW50IjoiTG93ZXJpbmcgdGhlIGRldGVjdGlvbiB0aHJlc2hvbGQgaCByZWR1Y2VzIGRldGVjdGlvbiBkZWxheSBidXQgaW5jcmVhc2VzIGZhbHNlIGFsYXJtcy4gRm9yIHNhZmV0eS1jcml0aWNhbCBzeXN0ZW1zIChmcmF1ZCwgaW5kdXN0cmlhbCBmYXVsdHMpLCBtaW5pbWlzZSBmYWxzZSBhbGFybXMgYnkgc2V0dGluZyBoIGhpZ2ggYW5kIGFjY2VwdGluZyBsb25nZXIgZGVsYXlzLiBGb3IgZGF0YSBwaXBlbGluZXMgd2hlcmUgc3RhbGUgbW9kZWxzIGRlZ3JhZGUgYWNjdXJhY3ksIHByaW9yaXRpc2Ugc2hvcnQgZGVsYXlzIHdpdGggYSBzbWFsbCBmYWxzZSBhbGFybSBidWRnZXQgKGUuZy4sIDEgcGVyIDEwMDAgc3RlcHMpLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0cmVhbWluZyBBbm9tYWx5IE1ldGhvZCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkRyaWZ0IFR5cGUiLCJEZXRlY3Rpb24gRGVsYXkiLCJGYWxzZSBBbGFybSBDb250cm9sIiwiT25saW5lIFVwZGF0ZSIsIkxpYnJhcnkiXSwicm93cyI6W1siQ1VTVU0iLCJTdWRkZW4gbWVhbiBzaGlmdCIsIkxvdyAob3B0aW1hbCBmb3IgR2F1c3NpYW4pIiwiVmlhIHRocmVzaG9sZCBoIiwiTygxKSIsIlNjcmF0Y2ggb3Igcml2ZXIiXSxbIlBhZ2UtSGlua2xleSIsIlN1ZGRlbiBtZWFuIHNoaWZ0IiwiTG93IiwiVmlhIHRocmVzaG9sZCDOuyIsIk8oMSkiLCJyaXZlci5kcmlmdC5QYWdlSGlua2xleSJdLFsiQURXSU4iLCJTdWRkZW4gKyBncmFkdWFsIiwiTW9kZXJhdGUiLCJWaWEgZGVsdGEgcGFyYW1ldGVyIiwiTyhsb2cgbikgYW1vcnRpc2VkIiwicml2ZXIuZHJpZnQuQURXSU4iXSxbIkhhbGYtU3BhY2UgVHJlZXMiLCJHZW5lcmFsIC8gbXVsdGl2YXJpYXRlIiwiV2luZG93LWJhc2VkIiwiVmlhIHRocmVzaG9sZCBvbiBzY29yZSIsIk8oMSkgYW1vcnRpc2VkIiwicml2ZXIuYW5vbWFseS5IYWxmU3BhY2VUcmVlcyJdLFsiT25saW5lIGlGb3Jlc3QiLCJHZW5lcmFsIiwiV2luZG93LWJhc2VkIiwiVmlhIGNvbnRhbWluYXRpb24iLCJPKG5fdHJlZXMpIiwiQ3VzdG9tIC8gcHlzYWQiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV2YWx1YXRpb24gTWV0cmljcyBmb3IgU3RyZWFtIERldGVjdG9ycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RyZWFtIGRldGVjdG9yIGV2YWx1YXRpb24gdXNlczogKDEpIE1lYW4gVGltZSBUbyBEZXRlY3Rpb24gKE1UVEQpIOKAlCBleHBlY3RlZCBzdGVwcyBiZXR3ZWVuIHRydWUgY2hhbmdlIHBvaW50IGFuZCBmaXJzdCBhbGFybSwgKDIpIE1lYW4gVGltZSBCZXR3ZWVuIEZhbHNlIEFsYXJtcyAoTVRCRkEpIOKAlCBleHBlY3RlZCBzdGVwcyBiZXR3ZWVuIGNvbnNlY3V0aXZlIGZhbHNlIGFsYXJtcyBpbiBhIHN0YWJsZSByZWdpb24sICgzKSBEZXRlY3Rpb24gUmF0ZSAoRFIpIOKAlCBmcmFjdGlvbiBvZiBjaGFuZ2UgcG9pbnRzIGRldGVjdGVkIHdpdGhpbiBhIHRvbGVyYW5jZSB3aW5kb3cuIFRoZSBOYWIgc2NvcmUgKE51bWVudGEgQW5vbWFseSBCZW5jaG1hcmspIGNvbWJpbmVzIHRoZXNlIGludG8gYSBzaW5nbGUgbWV0cmljIHdpdGggYXN5bW1ldHJpYyB3aW5kb3cgc2NvcmluZy4gRm9yIHNpbXVsYXRlZCBldmFsdWF0aW9uLCB1c2UgbXVsdGlwbGUgcmFuZG9tIHNlZWRzIGFuZCBtdWx0aXBsZSBkcmlmdCBtYWduaXR1ZGVzLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Streaming Anomaly Detection — CUSUM, ADWIN, Online Methods

Batch anomaly detection is infeasible for high-frequency data streams: fitting a model and scanning all data retrospectively introduces unacceptable latency and memory requirements. Streaming anomaly detection algorithms process each observation in O(1) or O(log n) time, maintaining only a compact summary of recent history. This note covers CUSUM for persistent shift detection, ADWIN for adaptive windowing and drift detection, Half-Space Trees for online isolation scoring, and methods for evaluating stream detectors under various concept drift types.

## CUSUM — Cumulative Sum Control Chart

CUSUM (Page 1954) tracks cumulative deviation from an expected mean μ. For detecting upward shifts: CUSUM⁺_t = max(0, CUSUM⁺_{t-1} + (x_t - μ - k)) where k = (μ_1 - μ_0)/2 is the slack (half the expected shift magnitude). An alarm fires when CUSUM⁺_t > h where h is the detection threshold. The method is sensitive to small persistent shifts (signal-to-noise ratio matters) and has O(1) per-step complexity. After an alarm, the statistic is reset to 0. CUSUM is optimal (minimises expected detection delay) for Gaussian observations with known pre- and post-change means.

```python
import numpy as np

def cusum_detector(stream, mu0=0.0, k=0.5, h=5.0):
    """
    Two-sided CUSUM detector.
    k: slack (half the expected shift magnitude)
    h: threshold for alarm
    Returns list of alarm indices.
    """
    cusum_pos = 0.0
    cusum_neg = 0.0
    alarms = []
    for i, x in enumerate(stream):
        cusum_pos = max(0, cusum_pos + (x - mu0) - k)
        cusum_neg = max(0, cusum_neg - (x - mu0) - k)
        if cusum_pos > h or cusum_neg > h:
            alarms.append(i)
            cusum_pos = 0.0  # reset after alarm
            cusum_neg = 0.0
    return alarms

np.random.seed(42)
normal_segment = np.random.randn(200)
shift_segment  = np.random.randn(100) + 1.5  # mean shift of 1.5
stream = np.concatenate([normal_segment, shift_segment])

alarms = cusum_detector(stream, mu0=0.0, k=0.5, h=5.0)
first_alarm = alarms[0] if alarms else None
print(f'True change point: 200')
print(f'CUSUM first alarm: {first_alarm}  (detection delay: {first_alarm - 200 if first_alarm else "no alarm"})')
print(f'Total alarms fired: {len(alarms)}')
```

## ADWIN — Adaptive Windowing

ADWIN (Bifet & Gavalda, 2007) maintains a variable-length window of recent data. It detects distribution shift by partitioning the window into two consecutive sub-windows and testing whether their means differ significantly using the Hoeffding bound. If a significant difference is found, the older portion is discarded (the window shrinks). ADWIN provides theoretical guarantees: false alarm rate is at most δ (user-specified), and it detects all distribution shifts with probability ≥ 1-δ after O(log n) observations. Window size adapts automatically — large windows during stable periods, small windows after drift.

```python
import numpy as np

try:
    from river.drift import ADWIN
    from river.datasets import synth

    adwin = ADWIN(delta=0.002)
    np.random.seed(42)
    stream_vals = np.concatenate([
        np.random.randn(300),
        np.random.randn(200) + 2.5,   # concept drift at step 300
        np.random.randn(200),
    ])
    alarms, window_sizes = [], []
    for i, x in enumerate(stream_vals):
        adwin.update(x)
        window_sizes.append(adwin.width)
        if adwin.drift_detected:
            alarms.append(i)

    print(f'True drift points: [300, 500]')
    print(f'ADWIN alarms at: {alarms}')
    print(f'Window size at stable region (t=150): {window_sizes[150]}')
    print(f'Window size just after drift (t=320): {window_sizes[min(320, len(window_sizes)-1)]}')
except ImportError:
    print('Install river: pip install river')
    print('ADWIN usage:')
    print('  from river.drift import ADWIN')
    print('  adwin = ADWIN(delta=0.002)')
    print('  for x in stream: adwin.update(x); if adwin.drift_detected: handle()')
    print('  adwin.width: current window size (adapts automatically)')
```

## Half-Space Trees for Streaming Anomaly Detection

Half-Space Trees (HST; Tan et al., 2011) are an online version of Isolation Forest adapted for data streams. Each tree partitions the feature space using random axis-aligned splits. Anomaly score = mass of the leaf node the sample falls into (higher mass = more normal). HST updates incrementally: every window_size steps, the reference and latest windows swap and leaf masses are updated. HST handles concept drift naturally and achieves O(1) amortised update time per observation. It is implemented in River as HalfSpaceTrees.

```python
import numpy as np

try:
    from river.anomaly import HalfSpaceTrees

    hst = HalfSpaceTrees(
        n_trees=25,
        height=8,
        window_size=250,
        limits={0: (0, 1), 1: (0, 1)},
    )
    np.random.seed(7)
    normal_data   = np.random.uniform(0.2, 0.8, (400, 2))
    anomaly_data  = np.random.uniform(0.0, 0.05, (20, 2))  # corner anomalies
    stream_data   = np.vstack([normal_data, anomaly_data])
    stream_labels = [0]*400 + [1]*20

    scores = []
    for point in stream_data:
        obs = {0: point[0], 1: point[1]}
        score = hst.score_one(obs)
        hst.learn_one(obs)
        scores.append(score)

    scores = np.array(scores)
    threshold = np.percentile(scores[:400], 95)
    tp = np.sum(scores[400:] > threshold)
    fp = np.sum(scores[:400] > threshold)
    print(f'Anomaly score threshold (95th pct normal): {threshold:.4f}')
    print(f'True positives: {tp}/20, False positives: {fp}/400')
except ImportError:
    print('Install river: pip install river')
    print('HalfSpaceTrees: online anomaly scoring in O(1) per observation')
```

## Concept Drift — Types and Challenges

Concept drift occurs when the data distribution P(X, y) changes over time. Different drift types require different detection strategies. Sudden drift (abrupt change) is easiest to detect with CUSUM. Gradual drift (slow transition) requires sliding window methods. Incremental drift (monotone shift) can be tracked with ADWIN’s adaptive window. Recurring drift (periodic seasonality or regime shifts) requires memory of past concepts. Evaluating detectors requires simulation because real-world drift ground truth is rarely available.

- Sudden drift: P changes abruptly at one point — CUSUM and Page-Hinkley are optimal.
- Gradual drift: P transitions over a window W — ADWIN and sliding window detectors work well.
- Incremental drift: P shifts monotonically — requires models that continuously update parameters.
- Recurring drift: P cycles between known concepts — concept libraries and ensemble switching needed.
- Covariate shift: P(X) changes but P(y|X) stays the same — importance weighting rather than drift detection.
- Real drift: P(y|X) changes — requires labelled feedback; detection delays are unavoidable without labels.

## Comparing Detector Response to Simulated Drift

To compare detectors, simulate streams with known change points and measure detection delay (steps after true drift until alarm) and false alarm rate (alarms per 1000 normal steps). Lower detection delay and lower false alarm rate are both desirable — there is typically a trade-off controlled by the detection threshold.

```python
import numpy as np

def cusum(stream, mu0, k, h):
    s, alarms = 0.0, []
    for i, x in enumerate(stream):
        s = max(0, s + x - mu0 - k)
        if s > h:
            alarms.append(i)
            s = 0.0
    return alarms

def page_hinkley(stream, delta=0.005, threshold=50, alpha=1.0):
    """Page-Hinkley test for mean shifts."""
    m_t = x_bar = 0.0
    alarms, n = [], 0
    for i, x in enumerate(stream):
        n += 1
        x_bar += (x - x_bar) / n
        m_t += x - x_bar - delta
        if m_t > threshold:
            alarms.append(i)
            m_t = 0.0
    return alarms

np.random.seed(0)
normal   = np.random.randn(500)
shifted  = np.random.randn(300) + 2.0
stream   = np.concatenate([normal, shifted])
true_cp  = 500

cusum_alarms = cusum(stream, mu0=0.0, k=0.5, h=4.0)
ph_alarms    = page_hinkley(stream, delta=0.01, threshold=40)

cusum_delay = cusum_alarms[0] - true_cp if cusum_alarms else float('inf')
ph_delay    = ph_alarms[0]    - true_cp if ph_alarms    else float('inf')
print(f'True change point: {true_cp}')
print(f'CUSUM first alarm: {cusum_alarms[0] if cusum_alarms else "none"}  delay={cusum_delay}')
print(f'Page-Hinkley:      {ph_alarms[0] if ph_alarms else "none"}  delay={ph_delay}')
print(f'CUSUM false alarms (first 500): {sum(a < 500 for a in cusum_alarms)}')
print(f'PH    false alarms (first 500): {sum(a < 500 for a in ph_alarms)}')
```

> **Detection Delay vs False Alarm Trade-off**: Lowering the detection threshold h reduces detection delay but increases false alarms. For safety-critical systems (fraud, industrial faults), minimise false alarms by setting h high and accepting longer delays. For data pipelines where stale models degrade accuracy, prioritise short delays with a small false alarm budget (e.g., 1 per 1000 steps).

## Streaming Anomaly Method Comparison

| Method | Drift Type | Detection Delay | False Alarm Control | Online Update | Library |
| --- | --- | --- | --- | --- | --- |
| CUSUM | Sudden mean shift | Low (optimal for Gaussian) | Via threshold h | O(1) | Scratch or river |
| Page-Hinkley | Sudden mean shift | Low | Via threshold λ | O(1) | river.drift.PageHinkley |
| ADWIN | Sudden + gradual | Moderate | Via delta parameter | O(log n) amortised | river.drift.ADWIN |
| Half-Space Trees | General / multivariate | Window-based | Via threshold on score | O(1) amortised | river.anomaly.HalfSpaceTrees |
| Online iForest | General | Window-based | Via contamination | O(n_trees) | Custom / pysad |

## Evaluation Metrics for Stream Detectors

Stream detector evaluation uses: (1) Mean Time To Detection (MTTD) — expected steps between true change point and first alarm, (2) Mean Time Between False Alarms (MTBFA) — expected steps between consecutive false alarms in a stable region, (3) Detection Rate (DR) — fraction of change points detected within a tolerance window. The Nab score (Numenta Anomaly Benchmark) combines these into a single metric with asymmetric window scoring. For simulated evaluation, use multiple random seeds and multiple drift magnitudes.

---

