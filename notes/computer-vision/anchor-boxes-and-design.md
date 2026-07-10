---
title: "Anchor Boxes in Object Detection"
slug: "anchor-boxes-and-design"
description: "Anchor-based detection — anchor design (scales, ratios), anchor assignment (IoU thresholding), regression targets, and the motivation for moving to anchor-free approaches."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbmNob3IgYm94ZXMgYXJlIHByZS1kZWZpbmVkIHJlZmVyZW5jZSByZWN0YW5nbGVzIHRpbGVkIGFjcm9zcyB0aGUgZmVhdHVyZSBtYXAuIEVhY2ggc3BhdGlhbCBsb2NhdGlvbiBnZW5lcmF0ZXMgYSBmaXhlZCBzZXQgb2YgYW5jaG9ycyB3aXRoIHZhcnlpbmcgc2NhbGVzIGFuZCBhc3BlY3QgcmF0aW9zLiBEdXJpbmcgdHJhaW5pbmcsIGFuY2hvcnMgYXJlIGFzc2lnbmVkIHRvIGdyb3VuZC10cnV0aCBib3hlcyBiYXNlZCBvbiBJb1Ugb3ZlcmxhcCwgY3JlYXRpbmcgcG9zaXRpdmUgc2FtcGxlcyBmb3IgYm94ZXMgdGhlIG5ldHdvcmsgc2hvdWxkIHByZWRpY3QgYW5kIG5lZ2F0aXZlIHNhbXBsZXMgZm9yIGJhY2tncm91bmQgcmVnaW9ucy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuY2hvciBkZXNpZ24gZW5jb2RlcyBwcmlvciBrbm93bGVkZ2UgYWJvdXQgZXhwZWN0ZWQgb2JqZWN0IHNpemVzIGluIHRoZSBkYXRhc2V0LiBBIHR5cGljYWwgY29uZmlndXJhdGlvbiB1c2VzIDMgc2NhbGVzIChzbWFsbCwgbWVkaXVtLCBsYXJnZSkgYW5kIDMgYXNwZWN0IHJhdGlvcyAoMC41LCAxLjAsIDIuMCksIHByb2R1Y2luZyA5IGFuY2hvcnMgcGVyIGxvY2F0aW9uLiBHaXZlbiBhIGZlYXR1cmUgbWFwIG9mIHNpemUgSMOXVywgdGhpcyB5aWVsZHMgSMOXV8OXOSB0b3RhbCBhbmNob3JzIOKAlCBvZnRlbiBodW5kcmVkcyBvZiB0aG91c2FuZHMgZm9yIGEgc2luZ2xlIGltYWdlLCByZXF1aXJpbmcgZWZmaWNpZW50IGJhdGNoIHByb2Nlc3NpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQW5jaG9yIEdlbmVyYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuY2hvcnMgYXJlIGdlbmVyYXRlZCByZWxhdGl2ZSB0byBlYWNoIGZlYXR1cmUgbWFwIGNlbGwsIHRoZW4gcHJvamVjdGVkIHRvIHRoZSBpbnB1dCBpbWFnZSBjb29yZGluYXRlIHNwYWNlLiBGb3IgYSBzdHJpZGUtMTYgZmVhdHVyZSBtYXAsIGVhY2ggY2VsbCBjb3ZlcnMgYSAxNsOXMTYgcGl4ZWwgcmVnaW9uIGluIHRoZSBvcmlnaW5hbCBpbWFnZS4gQW5jaG9yIHNjYWxlcyBhcmUgYXBwbGllZCB0byB0aGlzIHN0cmlkZSAoZS5nLiwgMzLCsiwgNjTCsiwgMTI4wrIgcGl4ZWxzKSwgc28gYW5jaG9ycyBhdCBlYWNoIGxvY2F0aW9uIGNvdmVyIGRpZmZlcmVudCBhYnNvbHV0ZSBzaXplcyBpbiB0aGUgaW1hZ2UuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGZWF0dXJlIFB5cmFtaWQgTmV0d29ya3MgKEZQTikgYWRkcmVzcyBtdWx0aS1zY2FsZSBkZXRlY3Rpb24gYnkgZ2VuZXJhdGluZyBhbmNob3JzIGF0IG11bHRpcGxlIHB5cmFtaWQgbGV2ZWxzLiBMYXJnZXIgYW5jaG9ycyBhcHBlYXIgYXQgY29hcnNlciBmZWF0dXJlIGxldmVscyB3aXRoIGxhcmdlciByZWNlcHRpdmUgZmllbGRzLCBhbmQgc21hbGxlciBhbmNob3JzIGF0IGZpbmVyIGxldmVscy4gVGhpcyBhbGxvd3MgYSBzaW5nbGUgZGV0ZWN0b3IgdG8gaGFuZGxlIG9iamVjdHMgc3Bhbm5pbmcgc2V2ZXJhbCBvcmRlcnMgb2YgbWFnbml0dWRlIGluIHNpemUgd2l0aG91dCBuZWVkaW5nIGV4Y2Vzc2l2ZWx5IGxhcmdlIGFuY2hvciBzZXRzIGF0IG9uZSBsZXZlbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBnZW5lcmF0ZV9hbmNob3JzKHN0cmlkZSwgc2NhbGVzLCByYXRpb3MsIGZlYXRfaCwgZmVhdF93KTpcbiAgICBhbmNob3JzID0gW11cbiAgICBmb3IgeSBpbiByYW5nZShmZWF0X2gpOlxuICAgICAgICBmb3IgeCBpbiByYW5nZShmZWF0X3cpOlxuICAgICAgICAgICAgY3ggPSAoeCArIDAuNSkgKiBzdHJpZGVcbiAgICAgICAgICAgIGN5ID0gKHkgKyAwLjUpICogc3RyaWRlXG4gICAgICAgICAgICBmb3IgcyBpbiBzY2FsZXM6XG4gICAgICAgICAgICAgICAgZm9yIHIgaW4gcmF0aW9zOlxuICAgICAgICAgICAgICAgICAgICB3ID0gcyAqIG5wLnNxcnQoMS4wIC8gcilcbiAgICAgICAgICAgICAgICAgICAgaCA9IHMgKiBucC5zcXJ0KHIpXG4gICAgICAgICAgICAgICAgICAgIGFuY2hvcnMuYXBwZW5kKFtjeC13LzIsIGN5LWgvMiwgY3grdy8yLCBjeStoLzJdKVxuICAgIHJldHVybiBucC5hcnJheShhbmNob3JzKSAgIyBbSCpXKm51bV9zY2FsZXMqbnVtX3JhdGlvcywgNF0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBbmNob3IgQXNzaWdubWVudCB2aWEgSW9VIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbmNob3IgYXNzaWdubWVudCBkZXRlcm1pbmVzIHdoaWNoIGFuY2hvcnMgcGFydGljaXBhdGUgaW4gdHJhaW5pbmcuIFRoZSBhc3NpZ25tZW50IHJ1bGUgaXMgSW9VLWJhc2VkOiBhbmNob3JzIHdpdGggSW9VIFx1MDAzZT0gMC43IHdpdGggYW55IEdUIGJveCBhcmUgcG9zaXRpdmU7IGFuY2hvcnMgd2l0aCBJb1UgXHUwMDNjIDAuMyB3aXRoIGFsbCBHVCBib3hlcyBhcmUgbmVnYXRpdmU7IGFuY2hvcnMgaW4gYmV0d2VlbiBhcmUgaWdub3JlZC4gRWFjaCBHVCBib3ggaXMgYWxzbyBhc3NpZ25lZCB0byBpdHMgaGlnaGVzdC1Jb1UgYW5jaG9yIHRvIGVuc3VyZSBldmVyeSBvYmplY3QgaGFzIGF0IGxlYXN0IG9uZSBwb3NpdGl2ZSB0cmFpbmluZyBzYW1wbGUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQb3NpdGl2ZSBhbmNob3JzIGxlYXJuIHRvIHByZWRpY3QgdGhlIEdUIGJveCB0aGV5IGFyZSBhc3NpZ25lZCB0by4gTmVnYXRpdmUgYW5jaG9ycyBsZWFybiB0byBwcmVkaWN0IGJhY2tncm91bmQuIEluIHByYWN0aWNlLCBwb3NpdGl2ZSBhbmNob3JzIGFyZSByYXJlIOKAlCBmb3IgRmFzdGVyIFItQ05OLCByb3VnaGx5IDI1JSBvZiBlYWNoIG1pbmktYmF0Y2ggY29uc2lzdHMgb2YgcG9zaXRpdmUgYW5jaG9ycywgd2l0aCB0aGUgcmVzdCByYW5kb21seSBzYW1wbGVkIG5lZ2F0aXZlcy4gVGhpcyBzYW1wbGluZyBwcmV2ZW50cyB0aGUgZ3JhZGllbnQgZnJvbSBiZWluZyBkb21pbmF0ZWQgYnkgdGhlIGFidW5kYW50IGVhc3kgbmVnYXRpdmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGFzc2lnbl9hbmNob3JzKGFuY2hvcnMsIGd0X2JveGVzLCBwb3NfdGhyPTAuNywgbmVnX3Rocj0wLjMpOlxuICAgICMgUmV0dXJucyBsYWJlbHM6IDE9cG9zaXRpdmUsIDA9bmVnYXRpdmUsIC0xPWlnbm9yZVxuICAgIGlvdV9tYXQgPSBjb21wdXRlX2lvdV9tYXRyaXgoYW5jaG9ycywgZ3RfYm94ZXMpICAjIFtOX2FuYywgTl9ndF1cbiAgICBtYXhfaW91ID0gaW91X21hdC5tYXgoYXhpcz0xKVxuICAgIGFzc2lnbmVkX2d0ID0gaW91X21hdC5hcmdtYXgoYXhpcz0xKVxuXG4gICAgbGFiZWxzID0gbnAuZnVsbChsZW4oYW5jaG9ycyksIC0xKVxuICAgIGxhYmVsc1ttYXhfaW91IFx1MDAzZT0gcG9zX3Rocl0gPSAxXG4gICAgbGFiZWxzW21heF9pb3UgXHUwMDNjIG5lZ190aHJdID0gMFxuICAgICMgRm9yY2UtYXNzaWduIHRoZSBiZXN0IGFuY2hvciBwZXIgR1QgdG8gZW5zdXJlIGNvdmVyYWdlXG4gICAgYmVzdF9hbmNfcGVyX2d0ID0gaW91X21hdC5hcmdtYXgoYXhpcz0wKVxuICAgIGxhYmVsc1tiZXN0X2FuY19wZXJfZ3RdID0gMVxuICAgIHJldHVybiBsYWJlbHMsIGFzc2lnbmVkX2d0In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVncmVzc2lvbiBUYXJnZXRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZXRlY3Rpb24gaGVhZHMgcHJlZGljdCBvZmZzZXRzIHJlbGF0aXZlIHRvIHRoZSBhc3NpZ25lZCBhbmNob3IsIG5vdCBhYnNvbHV0ZSBjb29yZGluYXRlcy4gUmVncmVzc2lvbiB0YXJnZXRzIChkZWx0YV94LCBkZWx0YV95LCBkZWx0YV93LCBkZWx0YV9oKSBhcmUgbm9ybWFsaXplZCBieSB0aGUgYW5jaG9yXHUwMDI3cyBkaW1lbnNpb25zLCBtYWtpbmcgdGhlIGxlYXJuaW5nIHNjYWxlLWludmFyaWFudC4gQSBuZXR3b3JrIHByZWRpY3RpbmcgZGVsdGFfdyBuZWFyIDAgbWVhbnMgdGhlIHByZWRpY3RlZCB3aWR0aCBlcXVhbHMgdGhlIGFuY2hvciB3aWR0aCwgc28gcHJlZGljdGlvbnMgaW5pdGlhbGl6ZSBuZWFyIGFuY2hvciBnZW9tZXRyeS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBlbmNvZGluZyBmb3JtdWxhIGlzOiBkeCA9IChndF9jeCAtIGFuY19jeCkgLyBhbmNfdywgZHkgPSAoZ3RfY3kgLSBhbmNfY3kpIC8gYW5jX2gsIGR3ID0gbG9nKGd0X3cgLyBhbmNfdyksIGRoID0gbG9nKGd0X2ggLyBhbmNfaCkuIFRoZSBsb2cgdHJhbnNmb3JtIHByZXZlbnRzIG5lZ2F0aXZlIHByZWRpY3Rpb25zIGFuZCBzdGFiaWxpemVzIGdyYWRpZW50cyBmb3IgbGFyZ2Ugc2l6ZSBkaWZmZXJlbmNlcy4gU21vb3RoIEwxIGxvc3MgKEh1YmVyKSBpcyB1c2VkIGluc3RlYWQgb2YgTVNFIHRvIHJlZHVjZSBzZW5zaXRpdml0eSB0byBsYXJnZSBvdXRsaWVycyBlYXJseSBpbiB0cmFpbmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBlbmNvZGVfdGFyZ2V0cyhhbmNob3JzX2N4Y3l3aCwgZ3RfY3hjeXdoKTpcbiAgICAjIEVuY29kZSBHVCBib3hlcyBhcyBkZWx0YXMgcmVsYXRpdmUgdG8gbWF0Y2hlZCBhbmNob3JzXG4gICAgYW5jX2N4LCBhbmNfY3kgPSBhbmNob3JzX2N4Y3l3aFs6LDBdLCBhbmNob3JzX2N4Y3l3aFs6LDFdXG4gICAgYW5jX3csICBhbmNfaCAgPSBhbmNob3JzX2N4Y3l3aFs6LDJdLCBhbmNob3JzX2N4Y3l3aFs6LDNdXG4gICAgZ3RfY3gsICBndF9jeSAgPSBndF9jeGN5d2hbOiwwXSwgZ3RfY3hjeXdoWzosMV1cbiAgICBndF93LCAgIGd0X2ggICA9IGd0X2N4Y3l3aFs6LDJdLCBndF9jeGN5d2hbOiwzXVxuXG4gICAgZHggPSAoZ3RfY3ggLSBhbmNfY3gpIC8gYW5jX3dcbiAgICBkeSA9IChndF9jeSAtIGFuY19jeSkgLyBhbmNfaFxuICAgIGR3ID0gbnAubG9nKGd0X3cgLyBhbmNfdylcbiAgICBkaCA9IG5wLmxvZyhndF9oIC8gYW5jX2gpXG4gICAgcmV0dXJuIG5wLnN0YWNrKFtkeCwgZHksIGR3LCBkaF0sIGF4aXM9MSkifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBkZWNvZGVfcHJlZGljdGlvbnMoYW5jaG9yc19jeGN5d2gsIGRlbHRhcyk6XG4gICAgIyBEZWNvZGUgcHJlZGljdGVkIGRlbHRhcyBiYWNrIHRvIGFic29sdXRlIHh5eHkgYm94ZXNcbiAgICBhbmNfY3gsIGFuY19jeSA9IGFuY2hvcnNfY3hjeXdoWzosMF0sIGFuY2hvcnNfY3hjeXdoWzosMV1cbiAgICBhbmNfdywgIGFuY19oICA9IGFuY2hvcnNfY3hjeXdoWzosMl0sIGFuY2hvcnNfY3hjeXdoWzosM11cblxuICAgIHByZWRfY3ggPSBkZWx0YXNbOiwwXSAqIGFuY193ICsgYW5jX2N4XG4gICAgcHJlZF9jeSA9IGRlbHRhc1s6LDFdICogYW5jX2ggKyBhbmNfY3lcbiAgICBwcmVkX3cgID0gbnAuZXhwKGRlbHRhc1s6LDJdKSAqIGFuY193XG4gICAgcHJlZF9oICA9IG5wLmV4cChkZWx0YXNbOiwzXSkgKiBhbmNfaFxuXG4gICAgeDEgPSBwcmVkX2N4IC0gcHJlZF93IC8gMlxuICAgIHkxID0gcHJlZF9jeSAtIHByZWRfaCAvIDJcbiAgICB4MiA9IHByZWRfY3ggKyBwcmVkX3cgLyAyXG4gICAgeTIgPSBwcmVkX2N5ICsgcHJlZF9oIC8gMlxuICAgIHJldHVybiBucC5zdGFjayhbeDEsIHkxLCB4MiwgeTJdLCBheGlzPTEpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGltaXRhdGlvbnMgb2YgQW5jaG9ycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW5jaG9yLWJhc2VkIGRldGVjdG9ycyByZXF1aXJlIGNhcmVmdWwgaHlwZXItcGFyYW1ldGVyIHR1bmluZy4gQW5jaG9yIHNjYWxlcyBhbmQgcmF0aW9zIG11c3QgYmUgY2hvc2VuIHRvIGNvdmVyIHRoZSBkYXRhc2V0XHUwMDI3cyBvYmplY3Qgc2l6ZSBkaXN0cmlidXRpb24g4oCUIGFuY2hvcnMgdGhhdCBkbyBub3QgY292ZXIgR1Qgc2l6ZXMgd2VsbCBsZWFkIHRvIHBvb3IgcG9zaXRpdmUgYXNzaWdubWVudCBhbmQgZGVncmFkZWQgcmVjYWxsLiBUaGlzIG1ha2VzIGFuY2hvciBkZXNpZ24gZGF0YXNldC1zcGVjaWZpYzogYW5jaG9ycyBvcHRpbWFsIGZvciBDT0NPIG1heSBiZSBzdWJvcHRpbWFsIGZvciBzYXRlbGxpdGUgaW1hZ2VyeSBvciBtZWRpY2FsIGltYWdpbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZW5zZSBhbmNob3IgZ3JpZHMgaW50cm9kdWNlIHNldmVyZSBjbGFzcyBpbWJhbGFuY2Ug4oCUIGluIGEgdHlwaWNhbCBGUE4gZGV0ZWN0b3IsIGZld2VyIHRoYW4gMSUgb2YgYW5jaG9ycyBhcmUgcG9zaXRpdmUuIFRoaXMgcmVxdWlyZXMgZWl0aGVyIGhhcmQgbmVnYXRpdmUgbWluaW5nLCBPSEVNIChvbmxpbmUgaGFyZCBleGFtcGxlIG1pbmluZyksIG9yIGZvY2FsIGxvc3MgdG8gcHJldmVudCBlYXN5IG5lZ2F0aXZlcyBmcm9tIG92ZXJ3aGVsbWluZyB0aGUgdHJhaW5pbmcgc2lnbmFsLiBBbmNob3ItZnJlZSBkZXRlY3RvcnMgbGlrZSBGQ09TIGFuZCBDZW50ZXJOZXQgYnlwYXNzIHRoaXMgaXNzdWUgZW50aXJlbHkgd2l0aCBkaWZmZXJlbnQgYXNzaWdubWVudCBzdHJhdGVnaWVzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsImNvbnRlbnQiOiJBbmNob3IgZGVzaWduIHJlcXVpcmVzIGNhcmVmdWwgdHVuaW5nIGZvciBlYWNoIGRhdGFzZXRcdTAwMjdzIG9iamVjdCBzaXplIGRpc3RyaWJ1dGlvbiDigJQgdGhpcyBicml0dGxlbmVzcyBpcyB3aHkgYW5jaG9yLWZyZWUgZGV0ZWN0b3JzIChGQ09TLCBERVRSKSBoYXZlIGdhaW5lZCBwb3B1bGFyaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuY2hvciBib3hlcyByZW1haW4gdGhlIGZvdW5kYXRpb24gb2YgbWFueSBwcm9kdWN0aW9uIGRldGVjdG9ycy4gVW5kZXJzdGFuZGluZyBhbmNob3IgZ2VuZXJhdGlvbiwgSW9VLWJhc2VkIGFzc2lnbm1lbnQsIGFuZCBkZWx0YS1lbmNvZGluZyBpcyBlc3NlbnRpYWwgZm9yIGRlYnVnZ2luZyB0cmFpbmluZyBmYWlsdXJlcywgYWRhcHRpbmcgZGV0ZWN0b3JzIHRvIGN1c3RvbSBkYXRhc2V0cywgYW5kIGV4dGVuZGluZyBleGlzdGluZyBhcmNoaXRlY3R1cmVzLiBBbmNob3ItZnJlZSBhcHByb2FjaGVzIHRyYWRlIHRoaXMgY29tcGxleGl0eSBmb3IgZGlmZmVyZW50IGRlc2lnbiBjaG9pY2VzIGFyb3VuZCBjZW50ZXItcG9pbnQgb3IgcGl4ZWwtd2lzZSBwcmVkaWN0aW9uLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJEZXRlY3RvciIsIkFuY2hvcnMvTG9jYXRpb24iLCJTY2FsZXMiLCJSYXRpb3MiLCJQb3NpdGl2ZSBJb1UgVGhyZXNob2xkIl0sInJvd3MiOltbIkZhc3RlciBSLUNOTiIsIjkiLCIzIiwiMyIsIjAuNyJdLFsiU1NEIiwiNC02IiwiNC02IiwiMSwyLDMiLCIwLjUiXSxbIlJldGluYU5ldCIsIjkiLCIzIiwiMyIsIjAuNSJdLFsiWU9MT3YzIiwiMyIsIjMgKHBlciBsZXZlbCkiLCIxIChjbHVzdGVyZWQpIiwiMC41Il0sWyJGQ09TIiwiMCAoYW5jaG9yLWZyZWUpIiwi4oCUIiwi4oCUIiwiTi9BIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gYWRhcHRpbmcgYW4gYW5jaG9yLWJhc2VkIGRldGVjdG9yIHRvIGEgbmV3IGRvbWFpbiwgdXNlIGstbWVhbnMgY2x1c3RlcmluZyBvbiBHVCBib3ggZGltZW5zaW9ucyB0byBmaW5kIG9wdGltYWwgYW5jaG9yIHNjYWxlcyBhbmQgcmF0aW9zLiBUaGUgWU9MT3Y1IGF1dG9hbmNob3Igc2NyaXB0IGF1dG9tYXRlcyB0aGlzLiBBbHRlcm5hdGl2ZWx5LCBjb25zaWRlciBtaWdyYXRpbmcgdG8gYW4gYW5jaG9yLWZyZWUgYXJjaGl0ZWN0dXJlIGlmIHRoZSBvYmplY3Qgc2l6ZSBkaXN0cmlidXRpb24gaXMgaGlnaGx5IHZhcmllZCBvciBkaWZmaWN1bHQgdG8gcGFyYW1ldGVyaXplIHdpdGggYSBmaXhlZCBhbmNob3Igc2V0LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVncmVzc2lvbiB0YXJnZXQgbm9ybWFsaXphdGlvbiDigJQgZGl2aWRpbmcgYnkgYW5jaG9yIGRpbWVuc2lvbnMsIGxvZy10cmFuc2Zvcm0gZm9yIHNpemVzIOKAlCBpcyBjcml0aWNhbCBmb3IgdHJhaW5pbmcgc3RhYmlsaXR5LiBXaXRob3V0IGl0LCByYXcgcGl4ZWwgY29vcmRpbmF0ZXMgc3BhbiB3aWxkbHkgZGlmZmVyZW50IHJhbmdlcywgbWFraW5nIGl0IGhhcmQgZm9yIHRoZSBuZXR3b3JrIHRvIGxlYXJuIHVuaWZvcm0gcmVwcmVzZW50YXRpb25zIGFjcm9zcyBvYmplY3Qgc2NhbGVzLiBNb3N0IG1vZGVybiBmcmFtZXdvcmtzIGVuY29kZSB0aGVzZSBub3JtYWxpemF0aW9ucyBpbnRvIHRoZSBsb3NzIGZ1bmN0aW9uIG9yIGRhdGEgY29sbGF0aW9uIHBpcGVsaW5lLiJ9XQ=="
---
# Anchor Boxes in Object Detection

## Overview

Anchor boxes are pre-defined reference rectangles tiled across the feature map. Each spatial location generates a fixed set of anchors with varying scales and aspect ratios. During training, anchors are assigned to ground-truth boxes based on IoU overlap, creating positive samples for boxes the network should predict and negative samples for background regions.

Anchor design encodes prior knowledge about expected object sizes in the dataset. A typical configuration uses 3 scales (small, medium, large) and 3 aspect ratios (0.5, 1.0, 2.0), producing 9 anchors per location. Given a feature map of size H×W, this yields H×W×9 total anchors — often hundreds of thousands for a single image, requiring efficient batch processing.

## Anchor Generation

Anchors are generated relative to each feature map cell, then projected to the input image coordinate space. For a stride-16 feature map, each cell covers a 16×16 pixel region in the original image. Anchor scales are applied to this stride (e.g., 32², 64², 128² pixels), so anchors at each location cover different absolute sizes in the image.

Feature Pyramid Networks (FPN) address multi-scale detection by generating anchors at multiple pyramid levels. Larger anchors appear at coarser feature levels with larger receptive fields, and smaller anchors at finer levels. This allows a single detector to handle objects spanning several orders of magnitude in size without needing excessively large anchor sets at one level.

```python
import numpy as np

def generate_anchors(stride, scales, ratios, feat_h, feat_w):
    anchors = []
    for y in range(feat_h):
        for x in range(feat_w):
            cx = (x + 0.5) * stride
            cy = (y + 0.5) * stride
            for s in scales:
                for r in ratios:
                    w = s * np.sqrt(1.0 / r)
                    h = s * np.sqrt(r)
                    anchors.append([cx-w/2, cy-h/2, cx+w/2, cy+h/2])
    return np.array(anchors)  # [H*W*num_scales*num_ratios, 4]
```

## Anchor Assignment via IoU

Anchor assignment determines which anchors participate in training. The assignment rule is IoU-based: anchors with IoU >= 0.7 with any GT box are positive; anchors with IoU < 0.3 with all GT boxes are negative; anchors in between are ignored. Each GT box is also assigned to its highest-IoU anchor to ensure every object has at least one positive training sample.

Positive anchors learn to predict the GT box they are assigned to. Negative anchors learn to predict background. In practice, positive anchors are rare — for Faster R-CNN, roughly 25% of each mini-batch consists of positive anchors, with the rest randomly sampled negatives. This sampling prevents the gradient from being dominated by the abundant easy negatives.

```python
import numpy as np

def assign_anchors(anchors, gt_boxes, pos_thr=0.7, neg_thr=0.3):
    # Returns labels: 1=positive, 0=negative, -1=ignore
    iou_mat = compute_iou_matrix(anchors, gt_boxes)  # [N_anc, N_gt]
    max_iou = iou_mat.max(axis=1)
    assigned_gt = iou_mat.argmax(axis=1)

    labels = np.full(len(anchors), -1)
    labels[max_iou >= pos_thr] = 1
    labels[max_iou < neg_thr] = 0
    # Force-assign the best anchor per GT to ensure coverage
    best_anc_per_gt = iou_mat.argmax(axis=0)
    labels[best_anc_per_gt] = 1
    return labels, assigned_gt
```

## Regression Targets

Detection heads predict offsets relative to the assigned anchor, not absolute coordinates. Regression targets (delta_x, delta_y, delta_w, delta_h) are normalized by the anchor's dimensions, making the learning scale-invariant. A network predicting delta_w near 0 means the predicted width equals the anchor width, so predictions initialize near anchor geometry.

The encoding formula is: dx = (gt_cx - anc_cx) / anc_w, dy = (gt_cy - anc_cy) / anc_h, dw = log(gt_w / anc_w), dh = log(gt_h / anc_h). The log transform prevents negative predictions and stabilizes gradients for large size differences. Smooth L1 loss (Huber) is used instead of MSE to reduce sensitivity to large outliers early in training.

```python
import numpy as np

def encode_targets(anchors_cxcywh, gt_cxcywh):
    # Encode GT boxes as deltas relative to matched anchors
    anc_cx, anc_cy = anchors_cxcywh[:,0], anchors_cxcywh[:,1]
    anc_w,  anc_h  = anchors_cxcywh[:,2], anchors_cxcywh[:,3]
    gt_cx,  gt_cy  = gt_cxcywh[:,0], gt_cxcywh[:,1]
    gt_w,   gt_h   = gt_cxcywh[:,2], gt_cxcywh[:,3]

    dx = (gt_cx - anc_cx) / anc_w
    dy = (gt_cy - anc_cy) / anc_h
    dw = np.log(gt_w / anc_w)
    dh = np.log(gt_h / anc_h)
    return np.stack([dx, dy, dw, dh], axis=1)
```

```python
import numpy as np

def decode_predictions(anchors_cxcywh, deltas):
    # Decode predicted deltas back to absolute xyxy boxes
    anc_cx, anc_cy = anchors_cxcywh[:,0], anchors_cxcywh[:,1]
    anc_w,  anc_h  = anchors_cxcywh[:,2], anchors_cxcywh[:,3]

    pred_cx = deltas[:,0] * anc_w + anc_cx
    pred_cy = deltas[:,1] * anc_h + anc_cy
    pred_w  = np.exp(deltas[:,2]) * anc_w
    pred_h  = np.exp(deltas[:,3]) * anc_h

    x1 = pred_cx - pred_w / 2
    y1 = pred_cy - pred_h / 2
    x2 = pred_cx + pred_w / 2
    y2 = pred_cy + pred_h / 2
    return np.stack([x1, y1, x2, y2], axis=1)
```

## Limitations of Anchors

Anchor-based detectors require careful hyper-parameter tuning. Anchor scales and ratios must be chosen to cover the dataset's object size distribution — anchors that do not cover GT sizes well lead to poor positive assignment and degraded recall. This makes anchor design dataset-specific: anchors optimal for COCO may be suboptimal for satellite imagery or medical imaging.

Dense anchor grids introduce severe class imbalance — in a typical FPN detector, fewer than 1% of anchors are positive. This requires either hard negative mining, OHEM (online hard example mining), or focal loss to prevent easy negatives from overwhelming the training signal. Anchor-free detectors like FCOS and CenterNet bypass this issue entirely with different assignment strategies.

> **info**: Anchor design requires careful tuning for each dataset's object size distribution — this brittleness is why anchor-free detectors (FCOS, DETR) have gained popularity.

## Key Takeaways

Anchor boxes remain the foundation of many production detectors. Understanding anchor generation, IoU-based assignment, and delta-encoding is essential for debugging training failures, adapting detectors to custom datasets, and extending existing architectures. Anchor-free approaches trade this complexity for different design choices around center-point or pixel-wise prediction.

| Detector | Anchors/Location | Scales | Ratios | Positive IoU Threshold |
| --- | --- | --- | --- | --- |
| Faster R-CNN | 9 | 3 | 3 | 0.7 |
| SSD | 4-6 | 4-6 | 1,2,3 | 0.5 |
| RetinaNet | 9 | 3 | 3 | 0.5 |
| YOLOv3 | 3 | 3 (per level) | 1 (clustered) | 0.5 |
| FCOS | 0 (anchor-free) | — | — | N/A |

When adapting an anchor-based detector to a new domain, use k-means clustering on GT box dimensions to find optimal anchor scales and ratios. The YOLOv5 autoanchor script automates this. Alternatively, consider migrating to an anchor-free architecture if the object size distribution is highly varied or difficult to parameterize with a fixed anchor set.

Regression target normalization — dividing by anchor dimensions, log-transform for sizes — is critical for training stability. Without it, raw pixel coordinates span wildly different ranges, making it hard for the network to learn uniform representations across object scales. Most modern frameworks encode these normalizations into the loss function or data collation pipeline.

