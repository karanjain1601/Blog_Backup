---
title: "Video Classification with 3D CNNs: C3D, I3D, and SlowFast"
slug: "video-classification-3dcnn"
description: ""
tags: [""]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWaWRlbyBjbGFzc2lmaWNhdGlvbiBhc3NpZ25zIGEgc2VtYW50aWMgbGFiZWwg4oCUIHdhbGtpbmcsIGNvb2tpbmcsIHBsYXlpbmcgYmFza2V0YmFsbCDigJQgdG8gYW4gdW50cmltbWVkIG9yIHRyaW1tZWQgdmlkZW8gY2xpcC4gVW5saWtlIGltYWdlIGNsYXNzaWZpY2F0aW9uLCB0aGUgbW9kZWwgbXVzdCBhZ2dyZWdhdGUgZXZpZGVuY2UgYWNyb3NzIHRpbWU6IGEgc2luZ2xlIGZyYW1lIHJhcmVseSBkaXNhbWJpZ3VhdGVzIGJldHdlZW4gc2ltaWxhci1sb29raW5nIGFjdGl2aXRpZXMuIFRlbXBvcmFsIG1vZGVsaW5nIGlzIHRoZXJlZm9yZSB0aGUgY2VudHJhbCBhcmNoaXRlY3R1cmFsIGNoYWxsZW5nZSwgYW5kIGRpZmZlcmVudCBkZXNpZ25zIGVuY29kZSBmdW5kYW1lbnRhbGx5IGRpZmZlcmVudCBpbmR1Y3RpdmUgYmlhc2VzIGFib3V0IG1vdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVhcmx5IGFwcHJvYWNoZXMgYXBwbGllZCAyRCBDTk5zIGZyYW1lLWJ5LWZyYW1lIGFuZCBwb29sZWQgcHJlZGljdGlvbnMsIGRpc2NhcmRpbmcgdGVtcG9yYWwgc3RydWN0dXJlIGVudGlyZWx5LiBNb3JlIHByaW5jaXBsZWQgbWV0aG9kcyBtb2RlbCB0aW1lIGV4cGxpY2l0bHk6IHR3by1zdHJlYW0gbmV0d29ya3Mgc2VwYXJhdGUgUkdCIGFuZCBvcHRpY2FsIGZsb3cgcGF0aHdheXM7IDNEIENOTnMgdHJlYXQgdmlkZW8gYXMgYSBzcGF0aW90ZW1wb3JhbCB2b2x1bWU7IHRyYW5zZm9ybWVyLWJhc2VkIG1ldGhvZHMgYXR0ZW5kIGFjcm9zcyBmcmFtZSB0b2tlbnMuIERhdGFzZXQgc2NhbGUg4oCUIEtpbmV0aWNzICg0MDBLIGNsaXBzKSDigJQgcHJvdmVkIGFzIGltcG9ydGFudCBhcyBhcmNoaXRlY3R1cmUgY2hvaWNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRlbXBvcmFsIE1vZGVsaW5nIEFwcHJvYWNoZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzaW1wbGVzdCB0ZW1wb3JhbCBiYXNlbGluZSBpcyBsYXRlIGZ1c2lvbjogcnVuIGEgUmVzTmV0IG9uIGVhY2ggc2FtcGxlZCBmcmFtZSwgcG9vbCBsb2dpdHMgb3ZlciB0aW1lLCBhbmQgY2xhc3NpZnkuIERlc3BpdGUgaXRzIHNpbXBsaWNpdHksIGxhdGUgZnVzaW9uIHdpdGggYSBzdHJvbmcgMkQgYmFja2JvbmUgaXMgY29tcGV0aXRpdmUgb24gbWFueSBiZW5jaG1hcmtzLiBTaW5nbGUtZnJhbWUgYWNjdXJhY3kgb24gS2luZXRpY3MtNDAwIGNhbiByZWFjaCBhcm91bmQgNzMlLCBzdXJwcmlzaW5nbHkgY2xvc2UgdG8gZWFybHkgM0QgbW9kZWxzLCBzdWdnZXN0aW5nIDJEIG1vZGVscyBjYXB0dXJlIGNvbnRleHR1YWwgc2NlbmUgY3VlcyBiZXlvbmQgcHVyZSB0ZW1wb3JhbCBtb3Rpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiIzRCBjb252b2x1dGlvbnMgZXh0ZW5kIHRoZSAyRCBrZXJuZWwgd2l0aCBhIHRlbXBvcmFsIGRpbWVuc2lvbjogYSAzw5czw5czIGtlcm5lbCBwcm9jZXNzZXMgYSBUw5dIw5dXIHNwYXRpb3RlbXBvcmFsIHZvbHVtZSBqb2ludGx5LiBUaGlzIGNhcHR1cmVzIG1vdGlvbiBwYXR0ZXJucyBkaXJlY3RseSB3aXRob3V0IGV4cGxpY2l0IG9wdGljYWwgZmxvdy4gVGhlIGNvc3QgaXMgY3ViaWMgaW4ga2VybmVsIHNpemU6IGEgdGVtcG9yYWwga2VybmVsIG9mIDMgdHJpcGxlcyBwYXJhbWV0ZXIgY291bnQuIEZhY3Rvcml6ZWQgZGVzaWducyBsaWtlICgyKzEpRCDigJQgc2VwYXJhdGUgc3BhdGlhbCB0aGVuIHRlbXBvcmFsIGNvbnZvbHV0aW9ucyDigJQgcGFydGlhbGx5IGFkZHJlc3MgdGhpcyBjb21wdXRhdGlvbmFsIG92ZXJoZWFkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkMzRCBhbmQgM0QgQ29udm9sdXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDM0QgKFRyYW4gZXQgYWwuLCAyMDE1KSB3YXMgYW1vbmcgdGhlIGZpcnN0IGxhcmdlLXNjYWxlIDNEIENOTiBtb2RlbHMsIHRyYWluZWQgb24gU3BvcnRzLTFNIHdpdGggM8OXM8OXMyBjb252b2x1dGlvbnMgdGhyb3VnaG91dCA4IGxheWVycy4gSXQgZXh0cmFjdGVkIGZjNiBhY3RpdmF0aW9ucyBhcyA0MDk2LWRpbWVuc2lvbmFsIHZpZGVvIGRlc2NyaXB0b3JzLiBEZXNwaXRlIGl0cyA3OE0gcGFyYW1ldGVycyBhbmQgbG93ZXIgYWNjdXJhY3kgY29tcGFyZWQgdG8gbGF0ZXIgbW9kZWxzLCBDM0QgZGVtb25zdHJhdGVkIHRoYXQgM0QgY29udm9sdXRpb25zIGNhbiBsZWFybiBnZW5lcmljIHNwYXRpb3RlbXBvcmFsIGZlYXR1cmVzIHRyYW5zZmVyYWJsZSBhY3Jvc3MgcmVjb2duaXRpb24gdGFza3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbiMgM0QgY29udiBibG9jazogcHJvY2Vzc2VzIFQgeCBIIHggVyB2b2x1bWVzIGpvaW50bHlcbiMga2VybmVsX3NpemU9KDMsMywzKSBoYXMgM3ggbW9yZSBwYXJhbXMgdGhhbiAyRCBvZiBzYW1lIHNwYXRpYWwgc2l6ZVxuY29udjNkID0gbm4uQ29udjNkKENfaW4sIENfb3V0LFxuICAgICAgICAgICAgICAgICAgIGtlcm5lbF9zaXplPSgzLCAzLCAzKSxcbiAgICAgICAgICAgICAgICAgICBzdHJpZGU9KDEsIDEsIDEpLFxuICAgICAgICAgICAgICAgICAgIHBhZGRpbmc9KDEsIDEsIDEpLFxuICAgICAgICAgICAgICAgICAgIGJpYXM9RmFsc2UpXG5cbiMgRmFjdG9yaXplZCAoMisxKUQgYWx0ZXJuYXRpdmUg4oCUIHNhbWUgYWNjdXJhY3ksIGZld2VyIEZMT1BzOlxuY29udl9zID0gbm4uQ29udjNkKENfaW4sICBDX291dCwgKDEsIDMsIDMpLCBwYWRkaW5nPSgwLCAxLCAxKSlcbmNvbnZfdCA9IG5uLkNvbnYzZChDX291dCwgQ19vdXQsICgzLCAxLCAxKSwgcGFkZGluZz0oMSwgMCwgMCkpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDM0RcdTAwMjdzIGxpbWl0YXRpb25zIGFyZSBzaWduaWZpY2FudDogNzhNIHBhcmFtZXRlcnMsIDM4IEdGTE9QcyBwZXIgY2xpcCwgYW5kIGZpeGVkIDE2LWZyYW1lIDExMsOXMTEyIGlucHV0LiBJdCB3YXMgcHJldHJhaW5lZCBvbiBub2lzaWx5IGxhYmVsbGVkIFNwb3J0cy0xTS4gTGF0ZXIgd29yayBmb3VuZCBkZXB0aCBhbmQgd2lkdGggd2l0aCBzbWFsbGVyIDNEIGtlcm5lbHMgZ2VuZXJhbGl6ZSBiZXR0ZXIgdGhhbiBDM0RcdTAwMjdzIGRlc2lnbi4gVGhlIHNoaWZ0IHRvIEtpbmV0aWNzIGFzIHRoZSBzdGFuZGFyZCBiZW5jaG1hcmsgYWxzbyBleHBvc2VkIEMzRFx1MDAyN3MgbGltaXRlZCBzcGF0aWFsIHJlc29sdXRpb24gYW5kIGl0cyBzZW5zaXRpdml0eSB0byBpbnB1dCBjbGlwIGxlbmd0aC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUd28tU3RyZWFtIGFuZCBJM0QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlR3by1zdHJlYW0gbmV0d29ya3MgKFNpbW9ueWFuIFx1MDAyNiBaaXNzZXJtYW4sIDIwMTQpIGNvbXB1dGUgb3B0aWNhbCBmbG93IG9mZmxpbmUgYW5kIHRyYWluIHR3byBzZXBhcmF0ZSBDTk5zOiBhIHNwYXRpYWwgc3RyZWFtIG9uIFJHQiBmcmFtZXMgYW5kIGEgdGVtcG9yYWwgc3RyZWFtIG9uIHN0YWNrZWQgb3B0aWNhbCBmbG93IGZpZWxkcyAoMTAgaG9yaXpvbnRhbCArIDEwIHZlcnRpY2FsIGNoYW5uZWxzKS4gU3RyZWFtcyBhcmUgZnVzZWQgYXQgcHJlZGljdGlvbiB0aW1lIGJ5IGF2ZXJhZ2luZyBzb2Z0bWF4IHNjb3Jlcy4gVGhlIHRlbXBvcmFsIHN0cmVhbVx1MDAyN3MgZmxvdyBpbnB1dCBlbmNvZGVzIG1vdGlvbiBleHBsaWNpdGx5LCBjb21wbGVtZW50aW5nIHRoZSBSR0IgYXBwZWFyYW5jZSBzdHJlYW0uIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiZGVmIGluZmxhdGVfY29udjJkX3RvXzNkKGNvbnYyZCwgVD0xKTpcbiAgICBcIlwiXCJJbmZsYXRlIDJEIHdlaWdodHMgdG8gM0QgYnkgcmVwZWF0aW5nIGFsb25nIHRoZSB0aW1lIGF4aXMuXCJcIlwiXG4gICAgdzJkID0gY29udjJkLndlaWdodC5kYXRhICAgICAgICAgICAjIChDX291dCwgQ19pbiwga0gsIGtXKVxuICAgIHczZCA9IHcyZC51bnNxdWVlemUoMikgICAgICAgICAgICAgIyAoQ19vdXQsIENfaW4sIDEsIGtILCBrVylcbiAgICB3M2QgPSB3M2QucmVwZWF0KDEsIDEsIFQsIDEsIDEpICAgIyAoQ19vdXQsIENfaW4sIFQsIGtILCBrVylcbiAgICB3M2QgPSB3M2QgLyBUICAgICAgICAgICAgICAgICAgICAgICMgcHJlc2VydmUgYWN0aXZhdGlvbiBzY2FsZVxuICAgIGtILCBrVyA9IGNvbnYyZC5rZXJuZWxfc2l6ZVxuICAgIHBILCBwVyA9IGNvbnYyZC5wYWRkaW5nXG4gICAgY29udjNkID0gbm4uQ29udjNkKFxuICAgICAgICBjb252MmQuaW5fY2hhbm5lbHMsIGNvbnYyZC5vdXRfY2hhbm5lbHMsXG4gICAgICAgIChULCBrSCwga1cpLCBwYWRkaW5nPShULy8yLCBwSCwgcFcpLCBiaWFzPUZhbHNlXG4gICAgKVxuICAgIGNvbnYzZC53ZWlnaHQuZGF0YS5jb3B5Xyh3M2QpXG4gICAgcmV0dXJuIGNvbnYzZCJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiB0d29fc3RyZWFtX2luZmVyZW5jZShzcGF0aWFsX25ldCwgdGVtcG9yYWxfbmV0LFxuICAgICAgICAgICAgICAgICAgICAgICAgIGZyYW1lcywgZmxvd3MsIGFscGhhPTEuMCk6XG4gICAgIyBmcmFtZXM6IChCLCAzLCBILCBXKSDigJQgc2luZ2xlIFJHQiBmcmFtZSBvciBtZWFuLXBvb2xlZFxuICAgICMgZmxvd3M6ICAoQiwgMjAsIEgsIFcpIOKAlCAxMCBob3Jpem9udGFsICsgMTAgdmVydGljYWwgY2hhbm5lbHNcbiAgICByZ2JfbG9naXRzICA9IHNwYXRpYWxfbmV0KGZyYW1lcy5tZWFuKDIpKSAgICMgbWVhbiBwb29sIG92ZXIgVFxuICAgIGZsb3dfbG9naXRzID0gdGVtcG9yYWxfbmV0KGZsb3dzKVxuICAgIHJnYl9wcm9iICAgID0gdG9yY2guc29mdG1heChyZ2JfbG9naXRzLCAgZGltPTEpXG4gICAgZmxvd19wcm9iICAgPSB0b3JjaC5zb2Z0bWF4KGZsb3dfbG9naXRzLCBkaW09MSlcbiAgICBmdXNlZCA9IHJnYl9wcm9iICsgYWxwaGEgKiBmbG93X3Byb2IgICAgICAgICAgIyBsYXRlIGZ1c2lvblxuICAgIHJldHVybiBmdXNlZC5hcmdtYXgoZGltPTEpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJM0QgdHJhaW5pbmcgZm9sbG93cyB0aHJlZSBzdGFnZXM6IGluZmxhdGUgSW1hZ2VOZXQtcHJldHJhaW5lZCB3ZWlnaHRzIGludG8gM0QsIHByZXRyYWluIG9uIEtpbmV0aWNzLTQwMCBvciA2MDAsIHRoZW4gZmluZS10dW5lIG9uIHRoZSB0YXJnZXQgZGF0YXNldC4gVGhlIGluZmxhdGVkIGluaXRpYWxpemF0aW9uIGRyYW1hdGljYWxseSBhY2NlbGVyYXRlcyBjb252ZXJnZW5jZSB2ZXJzdXMgcmFuZG9tIGluaXRpYWxpemF0aW9uLiBUd28tc3RyZWFtIEkzRCBhY2hpZXZlcyA3NS43JSBvbiBLaW5ldGljcy00MDAsIGEgbWFqb3IgbWlsZXN0b25lIHRoYXQgc2V0IHRoZSBzdGFuZGFyZCBmb3Igc3Vic2VxdWVudCB2aWRlbyBjbGFzc2lmaWNhdGlvbiBtb2RlbHMgdGhyb3VnaCAyMDE4IGFuZCAyMDE5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNsb3dGYXN0IE5ldHdvcmsifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNsb3dGYXN0IChGZWljaHRlbmJvZmVyIGV0IGFsLiwgMjAxOSkgdXNlcyB0d28gcGF0aHdheXM6IGEgU2xvdyBwYXRod2F5IGF0IDggZnBzIHdpdGggZnVsbCBjaGFubmVsIHdpZHRoLCBhbmQgYSBGYXN0IHBhdGh3YXkgYXQgMzIgZnBzIHdpdGggb25seSAxLzggdGhlIGNoYW5uZWxzLiBUaGUgRmFzdCBwYXRod2F5IGNhcHR1cmVzIGZpbmUtZ3JhaW5lZCB0ZW1wb3JhbCBtb3Rpb24gY2hlYXBseTsgdGhlIFNsb3cgcGF0aHdheSBmb2N1c2VzIG9uIHJpY2ggc2VtYW50aWMgZmVhdHVyZXMuIExhdGVyYWwgY29ubmVjdGlvbnMgYXQgZWFjaCBzdGFnZSBmdXNlIHRlbXBvcmFsIGluZm9ybWF0aW9uIGZyb20gRmFzdCBpbnRvIFNsb3csIGVucmljaGluZyBzZW1hbnRpYyByZXByZXNlbnRhdGlvbnMgd2l0aCBtb3Rpb24gY3Vlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJkZWYgc2xvd2Zhc3RfZm9yd2FyZChmcmFtZXMsIHNsb3dfcmF0ZT04LCBmYXN0X3JhdGU9Mik6XG4gICAgIyBmcmFtZXM6IChCLCAzLCBUX2Z1bGwsIEgsIFcpIOKAlCBkZW5zZSB0ZW1wb3JhbCBzYW1wbGluZ1xuICAgIHNsb3dfZnJhbWVzID0gZnJhbWVzWzosIDosIDo6c2xvd19yYXRlXSAgICMgKEIsIDMsICA4LCBILCBXKVxuICAgIGZhc3RfZnJhbWVzID0gZnJhbWVzWzosIDosIDo6ZmFzdF9yYXRlXSAgICMgKEIsIDMsIDMyLCBILCBXKVxuICAgIHNsb3dfZmVhdHMsIGxhdGVyYWxzID0gc2xvd19wYXRod2F5KHNsb3dfZnJhbWVzKVxuICAgIGZhc3RfZmVhdHMgICAgICAgICAgID0gZmFzdF9wYXRod2F5KGZhc3RfZnJhbWVzKVxuICAgICMgTGF0ZXJhbCBjb25uZWN0aW9uczogZnVzZSBtb3Rpb24gaW5mbyBmcm9tIGZhc3QgaW50byBzbG93XG4gICAgZm9yIGkgaW4gcmFuZ2UobGVuKHNsb3dfZmVhdHMpKTpcbiAgICAgICAgc2xvd19mZWF0c1tpXSA9IHNsb3dfZmVhdHNbaV0gKyBsYXRlcmFsX2NvbnZbaV0oZmFzdF9mZWF0c1tpXSlcbiAgICBwb29sZWQgPSB0b3JjaC5jYXQoW3Nsb3dfZmVhdHNbLTFdLCBmYXN0X2ZlYXRzWy0xXV0sIGRpbT0xKVxuICAgIHJldHVybiBjbGFzc2lmaWVyX2hlYWQocG9vbGVkKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2xvd0Zhc3QgYXZvaWRzIG9wdGljYWwgZmxvdyBlbnRpcmVseTogdGhlIEZhc3QgcGF0aHdheSBsZWFybnMgbW90aW9uLXNlbnNpdGl2ZSBmZWF0dXJlcyBkaXJlY3RseSBmcm9tIGRlbnNlIFJHQiBmcmFtZXMuIEF0IGluZmVyZW5jZSwgYm90aCBwYXRod2F5cyBydW4gc2ltdWx0YW5lb3VzbHkgYW5kIHRoZWlyIGdsb2JhbCBhdmVyYWdlLXBvb2xlZCBmZWF0dXJlcyBhcmUgY29uY2F0ZW5hdGVkIGJlZm9yZSB0aGUgY2xhc3NpZmllciBoZWFkLiBTbG93RmFzdCB3aXRoIGEgUmVzTmV0LTEwMSBiYWNrYm9uZSByZWFjaGVzIDc5JSBvbiBLaW5ldGljcy00MDAsIHN1cnBhc3NpbmcgSTNEIGJ5IG92ZXIgMyUgd2l0aG91dCBhbnkgb3B0aWNhbCBmbG93IGNvbXB1dGF0aW9uIGF0IGluZmVyZW5jZSB0aW1lLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwiY29udGVudCI6IlNsb3dGYXN0XHUwMDI3cyBpbnNpZ2h0OiBodW1hbnMgcHJvY2VzcyB2aWRlbyBhdCB0d28gdGltZXNjYWxlcyDigJQgc2xvdyAoc2VtYW50aWMgdW5kZXJzdGFuZGluZykgYW5kIGZhc3QgKG1vdGlvbikuIFRoZSBzbG93IHBhdGh3YXkgdXNlcyA4IGZyYW1lcyBhdCBmdWxsIHJlc29sdXRpb247IHRoZSBmYXN0IHBhdGh3YXkgdXNlcyAzMiBmcmFtZXMgYXQgbG93IGNoYW5uZWwgY291bnQuIExhdGVyYWwgY29ubmVjdGlvbnMgbGV0IHNsb3cgcmVjZWl2ZSBtb3Rpb24gY3VlcyBmcm9tIGZhc3QuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiSW5wdXQiLCJLaW5ldGljcy00MDAgVG9wLTEgJSIsIlBhcmFtcyAoTSkiLCJGTE9QcyAoRykiLCJQcmV0cmFpbiJdLCJyb3dzIjpbWyJDM0QiLCIxNsOXMTEywrIiLCI2Ny4yIiwiNzgiLCIzOCIsIlNwb3J0cy0xTSJdLFsiSTNEIiwiNjTDlzIyNMKyIiwiNzIuMSIsIjEyIiwiMTA4IiwiSW1hZ2VOZXQiXSxbIlR3by1TdHJlYW0gSTNEIiwiUkdCK0Zsb3ciLCI3NS43IiwiMjUiLCIyMTYiLCJJbWFnZU5ldCJdLFsiU2xvd0Zhc3QgUjUwIiwiOCszMsOXMjI0wrIiLCI3Ny4wIiwiMzQiLCI2NSIsIk5vbmUiXSxbIlNsb3dGYXN0IFIxMDEiLCI4KzMyw5cyMjTCsiIsIjc5LjAiLCI1MyIsIjIxMyIsIk5vbmUiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IjNEIGNvbnZvbHV0aW9ucyBhcmUgcG93ZXJmdWwgYnV0IGV4cGVuc2l2ZTogM0QgUmVzTmV0cyByZXF1aXJlIGNhcmVmdWwgZmFjdG9yaXphdGlvbiB0byBzdGF5IHRyYWN0YWJsZS4gVGhlICgyKzEpRCBkZWNvbXBvc2l0aW9uIOKAlCBmaXJzdCBhIDJEIHNwYXRpYWwgY29udiB0aGVuIGEgMUQgdGVtcG9yYWwgY29udiDigJQgbWF0Y2hlcyBmdWxsIDNEIGFjY3VyYWN5IHdoaWxlIHVzaW5nIGZld2VyIEZMT1BzLiBTbG93RmFzdCBnb2VzIGZ1cnRoZXIsIGZhY3Rvcml6aW5nIHRlbXBvcmFsIHNhbXBsaW5nIHJhdGhlciB0aGFuIGtlcm5lbCBzaGFwZSBieSBvcGVyYXRpbmcgYXQgdHdvIGRpZmZlcmVudCBmcmFtZSByYXRlcyBpbiBwYXJhbGxlbCB3aXRoaW4gYSBzaGFyZWQgYXJjaGl0ZWN0dXJlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT3B0aWNhbCBmbG93IGFzIGV4cGxpY2l0IGlucHV0IGhhcyBsYXJnZWx5IGJlZW4gc3VwZXJzZWRlZCBieSBhcmNoaXRlY3R1cmVzIHRoYXQgbGVhcm4gbW90aW9uIGltcGxpY2l0bHk6IFNsb3dGYXN0LCBUaW1lU2Zvcm1lciwgYW5kIFZpZGVvIFN3aW4gYWxsIG9wZXJhdGUgb24gcmF3IFJHQiBvbmx5LiBJbXBsaWNpdCBtb3Rpb24gbGVhcm5pbmcgYXZvaWRzIHRoZSBvdmVyaGVhZCBvZiBmbG93IGVzdGltYXRpb24g4oCUIHdoaWNoIGNhbiBjb3N0IG1vcmUgdGhhbiB0aGUgY2xhc3NpZmllciBpdHNlbGYg4oCUIGFuZCBsZXRzIHRoZSBtb2RlbCBsZWFybiB0YXNrLXJlbGV2YW50IG1vdGlvbiBmZWF0dXJlcyByYXRoZXIgdGhhbiBnZW5lcmFsLXB1cnBvc2UgZmxvdyBkaXNwbGFjZW1lbnQgZmllbGRzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGF0YXNldCBzY2FsZSBhbmQgbGFiZWwgcXVhbGl0eSBtYXR0ZXIgYXMgbXVjaCBhcyBhcmNoaXRlY3R1cmU6IEtpbmV0aWNzLTQwMCBlbmFibGVkIHRoZSBJbWFnZU5ldCBtb21lbnQgZm9yIHZpZGVvIHVuZGVyc3RhbmRpbmcuIE1vZGVscyBwcmV0cmFpbmVkIG9uIGxhcmdlciBzZXRzIOKAlCBLaW5ldGljcy02MDAsIEtpbmV0aWNzLTcwMCwgb3IgSkZUIOKAlCBnYWluIDEgdG8gNCUgb24gZG93bnN0cmVhbSB0YXNrcy4gU2VsZi1zdXBlcnZpc2VkIHByZXRyYWluaW5nIG9uIHVubGFiZWxlZCB2aWRlbyB1c2luZyBtYXNrZWQgYXV0b2VuY29kaW5nIG5vdyBtYXRjaGVzIHN1cGVydmlzZWQgS2luZXRpY3MgcHJldHJhaW5pbmcgZm9yIG1hbnkgZmluZS1ncmFpbmVkIHZpZGVvIHJlY29nbml0aW9uIGJlbmNobWFya3MuIn1d"
---
# Video Classification with 3D CNNs: C3D, I3D, and SlowFast

## Overview

Video classification assigns a semantic label — walking, cooking, playing basketball — to an untrimmed or trimmed video clip. Unlike image classification, the model must aggregate evidence across time: a single frame rarely disambiguates between similar-looking activities. Temporal modeling is therefore the central architectural challenge, and different designs encode fundamentally different inductive biases about motion.

Early approaches applied 2D CNNs frame-by-frame and pooled predictions, discarding temporal structure entirely. More principled methods model time explicitly: two-stream networks separate RGB and optical flow pathways; 3D CNNs treat video as a spatiotemporal volume; transformer-based methods attend across frame tokens. Dataset scale — Kinetics (400K clips) — proved as important as architecture choice.

## Temporal Modeling Approaches

The simplest temporal baseline is late fusion: run a ResNet on each sampled frame, pool logits over time, and classify. Despite its simplicity, late fusion with a strong 2D backbone is competitive on many benchmarks. Single-frame accuracy on Kinetics-400 can reach around 73%, surprisingly close to early 3D models, suggesting 2D models capture contextual scene cues beyond pure temporal motion.

3D convolutions extend the 2D kernel with a temporal dimension: a 3×3×3 kernel processes a T×H×W spatiotemporal volume jointly. This captures motion patterns directly without explicit optical flow. The cost is cubic in kernel size: a temporal kernel of 3 triples parameter count. Factorized designs like (2+1)D — separate spatial then temporal convolutions — partially address this computational overhead.

## C3D and 3D Convolutions

C3D (Tran et al., 2015) was among the first large-scale 3D CNN models, trained on Sports-1M with 3×3×3 convolutions throughout 8 layers. It extracted fc6 activations as 4096-dimensional video descriptors. Despite its 78M parameters and lower accuracy compared to later models, C3D demonstrated that 3D convolutions can learn generic spatiotemporal features transferable across recognition tasks.

```
import torch.nn as nn

# 3D conv block: processes T x H x W volumes jointly
# kernel_size=(3,3,3) has 3x more params than 2D of same spatial size
conv3d = nn.Conv3d(C_in, C_out,
                   kernel_size=(3, 3, 3),
                   stride=(1, 1, 1),
                   padding=(1, 1, 1),
                   bias=False)

# Factorized (2+1)D alternative — same accuracy, fewer FLOPs:
conv_s = nn.Conv3d(C_in,  C_out, (1, 3, 3), padding=(0, 1, 1))
conv_t = nn.Conv3d(C_out, C_out, (3, 1, 1), padding=(1, 0, 0))
```

C3D's limitations are significant: 78M parameters, 38 GFLOPs per clip, and fixed 16-frame 112×112 input. It was pretrained on noisily labelled Sports-1M. Later work found depth and width with smaller 3D kernels generalize better than C3D's design. The shift to Kinetics as the standard benchmark also exposed C3D's limited spatial resolution and its sensitivity to input clip length.

## Two-Stream and I3D

Two-stream networks (Simonyan & Zisserman, 2014) compute optical flow offline and train two separate CNNs: a spatial stream on RGB frames and a temporal stream on stacked optical flow fields (10 horizontal + 10 vertical channels). Streams are fused at prediction time by averaging softmax scores. The temporal stream's flow input encodes motion explicitly, complementing the RGB appearance stream.

```
def inflate_conv2d_to_3d(conv2d, T=1):
    """Inflate 2D weights to 3D by repeating along the time axis."""
    w2d = conv2d.weight.data           # (C_out, C_in, kH, kW)
    w3d = w2d.unsqueeze(2)             # (C_out, C_in, 1, kH, kW)
    w3d = w3d.repeat(1, 1, T, 1, 1)   # (C_out, C_in, T, kH, kW)
    w3d = w3d / T                      # preserve activation scale
    kH, kW = conv2d.kernel_size
    pH, pW = conv2d.padding
    conv3d = nn.Conv3d(
        conv2d.in_channels, conv2d.out_channels,
        (T, kH, kW), padding=(T//2, pH, pW), bias=False
    )
    conv3d.weight.data.copy_(w3d)
    return conv3d
```

```
def two_stream_inference(spatial_net, temporal_net,
                         frames, flows, alpha=1.0):
    # frames: (B, 3, H, W) — single RGB frame or mean-pooled
    # flows:  (B, 20, H, W) — 10 horizontal + 10 vertical channels
    rgb_logits  = spatial_net(frames.mean(2))   # mean pool over T
    flow_logits = temporal_net(flows)
    rgb_prob    = torch.softmax(rgb_logits,  dim=1)
    flow_prob   = torch.softmax(flow_logits, dim=1)
    fused = rgb_prob + alpha * flow_prob          # late fusion
    return fused.argmax(dim=1)
```

I3D training follows three stages: inflate ImageNet-pretrained weights into 3D, pretrain on Kinetics-400 or 600, then fine-tune on the target dataset. The inflated initialization dramatically accelerates convergence versus random initialization. Two-stream I3D achieves 75.7% on Kinetics-400, a major milestone that set the standard for subsequent video classification models through 2018 and 2019.

## SlowFast Network

SlowFast (Feichtenbofer et al., 2019) uses two pathways: a Slow pathway at 8 fps with full channel width, and a Fast pathway at 32 fps with only 1/8 the channels. The Fast pathway captures fine-grained temporal motion cheaply; the Slow pathway focuses on rich semantic features. Lateral connections at each stage fuse temporal information from Fast into Slow, enriching semantic representations with motion cues.

```
def slowfast_forward(frames, slow_rate=8, fast_rate=2):
    # frames: (B, 3, T_full, H, W) — dense temporal sampling
    slow_frames = frames[:, :, ::slow_rate]   # (B, 3,  8, H, W)
    fast_frames = frames[:, :, ::fast_rate]   # (B, 3, 32, H, W)
    slow_feats, laterals = slow_pathway(slow_frames)
    fast_feats           = fast_pathway(fast_frames)
    # Lateral connections: fuse motion info from fast into slow
    for i in range(len(slow_feats)):
        slow_feats[i] = slow_feats[i] + lateral_conv[i](fast_feats[i])
    pooled = torch.cat([slow_feats[-1], fast_feats[-1]], dim=1)
    return classifier_head(pooled)
```

SlowFast avoids optical flow entirely: the Fast pathway learns motion-sensitive features directly from dense RGB frames. At inference, both pathways run simultaneously and their global average-pooled features are concatenated before the classifier head. SlowFast with a ResNet-101 backbone reaches 79% on Kinetics-400, surpassing I3D by over 3% without any optical flow computation at inference time.

> **tip**: SlowFast's insight: humans process video at two timescales — slow (semantic understanding) and fast (motion). The slow pathway uses 8 frames at full resolution; the fast pathway uses 32 frames at low channel count. Lateral connections let slow receive motion cues from fast.

| Model | Input | Kinetics-400 Top-1 % | Params (M) | FLOPs (G) | Pretrain |
| --- | --- | --- | --- | --- | --- |
| C3D | 16×112² | 67.2 | 78 | 38 | Sports-1M |
| I3D | 64×224² | 72.1 | 12 | 108 | ImageNet |
| Two-Stream I3D | RGB+Flow | 75.7 | 25 | 216 | ImageNet |
| SlowFast R50 | 8+32×224² | 77.0 | 34 | 65 | None |
| SlowFast R101 | 8+32×224² | 79.0 | 53 | 213 | None |

## Key Takeaways

3D convolutions are powerful but expensive: 3D ResNets require careful factorization to stay tractable. The (2+1)D decomposition — first a 2D spatial conv then a 1D temporal conv — matches full 3D accuracy while using fewer FLOPs. SlowFast goes further, factorizing temporal sampling rather than kernel shape by operating at two different frame rates in parallel within a shared architecture.

Optical flow as explicit input has largely been superseded by architectures that learn motion implicitly: SlowFast, TimeSformer, and Video Swin all operate on raw RGB only. Implicit motion learning avoids the overhead of flow estimation — which can cost more than the classifier itself — and lets the model learn task-relevant motion features rather than general-purpose flow displacement fields.

Dataset scale and label quality matter as much as architecture: Kinetics-400 enabled the ImageNet moment for video understanding. Models pretrained on larger sets — Kinetics-600, Kinetics-700, or JFT — gain 1 to 4% on downstream tasks. Self-supervised pretraining on unlabeled video using masked autoencoding now matches supervised Kinetics pretraining for many fine-grained video recognition benchmarks.

