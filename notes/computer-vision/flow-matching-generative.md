---
title: "Flow Matching: Continuous Normalizing Flows for Generation"
slug: "flow-matching-generative"
description: "How flow matching trains a velocity field to transport noise to data along straight paths — with fewer ODE steps than diffusion."
tags: ["flow-matching", "generative-models", "normalizing-flows", "diffusion"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGbG93IG1hdGNoaW5nIGlzIGEgc2ltdWxhdGlvbi1mcmVlIGZyYW1ld29yayBmb3IgdHJhaW5pbmcgY29udGludW91cyBub3JtYWxpemluZyBmbG93cy4gUmF0aGVyIHRoYW4gc29sdmluZyBhbiBPREUgZHVyaW5nIHRyYWluaW5nLCBpdCBkaXJlY3RseSByZWdyZXNzZXMgYSB2ZWxvY2l0eSBmaWVsZCB0aGF0IHRyYW5zcG9ydHMgc2FtcGxlcyBmcm9tIEdhdXNzaWFuIG5vaXNlIHRvIHRoZSBkYXRhIGRpc3RyaWJ1dGlvbiBhbG9uZyBzbW9vdGggaW50ZXJwb2xhdGVkIHBhdGhzIOKAlCBtYWtpbmcgdHJhaW5pbmcgYXMgY2hlYXAgYXMgc2NvcmUgbWF0Y2hpbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2V5IGluc2lnaHQ6IGluc3RlYWQgb2YgbGVhcm5pbmcgdG8gcmV2ZXJzZSBhIGZpeGVkIG5vaXNpbmcgcHJvY2VzcywgZmxvdyBtYXRjaGluZyBsZWFybnMgYSB2ZWN0b3IgZmllbGQgdl90KHgpIHN1Y2ggdGhhdCBpbnRlZ3JhdGluZyBmcm9tIHQ9MCB0byB0PTEgdHJhbnNmb3JtcyBub2lzZSBpbnRvIGRhdGEuIFRoZSBwYXRoIHNoYXBlIGlzIGEgZGVzaWduIGNob2ljZSDigJQgbGluZWFyIGludGVycG9sYXRpb24sIG9wdGltYWwgdHJhbnNwb3J0LCBvciBjb3NpbmUgc2NoZWR1bGVzIGFsbCB3b3JrLCBlYWNoIHdpdGggZGlmZmVyZW50IGVmZmljaWVuY3kgdHJhZGVvZmZzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsImNvbnRlbnQiOiJGbG93IG1hdGNoaW5nIHdpdGggb3B0aW1hbCB0cmFuc3BvcnQgcGF0aHMgcHJvZHVjZXMgc3RyYWlnaHRlciB0cmFqZWN0b3JpZXMgdGhhbiBkaWZmdXNpb24g4oCUIG1lYW5pbmcgZmV3ZXIgaW50ZWdyYXRpb24gc3RlcHMgYXJlIG5lZWRlZC4gUmVjdGlmaWVkIEZsb3cgKHVzZWQgaW4gU0QzL0ZsdXgpIGl0ZXJhdGl2ZWx5IHN0cmFpZ2h0ZW5zIHBhdGhzIGJ5IHJlc2FtcGxpbmcgcGFpcnMgYWxvbmcgbGVhcm5lZCB0cmFqZWN0b3JpZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uZGl0aW9uYWwgRmxvdyBNYXRjaGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uZGl0aW9uYWwgZmxvdyBtYXRjaGluZyAoQ0ZNKSBjb25zdHJ1Y3RzIGEgcGVyLXNhbXBsZSBwcm9iYWJpbGl0eSBwYXRoIGZyb20gbm9pc2UgeDAgdG8gZGF0YSBwb2ludCB4MS4gRm9yIGEgbGluZWFyIGludGVycG9sYXRpb24gcGF0aCwgdGhlIGNvbmRpdGlvbmFsIHBhdGggaXMgeF90ID0gKDEtdCkqeDAgKyB0KngxIHdoZXJlIHgwIH4gTigwLEkpLiBUaGUgY29uZGl0aW9uYWwgdmVsb2NpdHkgZmllbGQgaXMgc2ltcGx5IHRoZSBjb25zdGFudCB2ZWN0b3IgdV90ID0geDEgLSB4MCwgcG9pbnRpbmcgZnJvbSBub2lzZSB0byBkYXRhLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIExpbmVhciBpbnRlcnBvbGF0aW9uIHBhdGggYW5kIGNvbnN0YW50IHZlbG9jaXR5IHRhcmdldFxuaW1wb3J0IHRvcmNoXG5cbmRlZiBzYW1wbGVfcGF0aCh4MCwgeDEsIHQpOlxuICAgIFwiXCJcIngwOiBub2lzZSwgeDE6IGRhdGEsIHQ6IHNjYWxhciBpbiBbMCwxXVwiXCJcIlxuICAgIHhfdCA9ICgxIC0gdCkgKiB4MCArIHQgKiB4MVxuICAgIHVfdCA9IHgxIC0geDAgICMgY29uc3RhbnQgZm9yIHN0cmFpZ2h0IHBhdGhzXG4gICAgcmV0dXJuIHhfdCwgdV90XG5cbngwID0gdG9yY2gucmFuZG4oNCwgMywgNjQsIDY0KSAgICMgbm9pc2VcbngxID0gcmVhbF9iYXRjaCAgICAgICAgICAgICAgICAgICAjIGRhdGFcbnQgID0gdG9yY2gucmFuZCg0LCAxLCAxLCAxKSAgICAgICMgcmFuZG9tIHRpbWVzdGVwc1xueF90LCB0YXJnZXRfdiA9IHNhbXBsZV9wYXRoKHgwLCB4MSwgdCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB2ZWxvY2l0eSBuZXR3b3JrIHZfdGhldGEoeF90LCB0KSBpcyB0cmFpbmVkIHRvIHByZWRpY3QgdV90LiBBdCBpbmZlcmVuY2UsIHN0YXJ0aW5nIGZyb20geDAgfiBOKDAsSSksIGludGVncmF0ZSBkeC9kdCA9IHZfdGhldGEoeF90LCB0KSBmcm9tIHQ9MCB0byB0PTEgd2l0aCBhbiBPREUgc29sdmVyLiBUaGUgc2ltcGxpY2l0eSBvZiB0aGUgY29uc3RhbnQgdmVsb2NpdHkgdGFyZ2V0IG1ha2VzIHRyYWluaW5nIHN0YWJsZSBmcm9tIGluaXRpYWxpemF0aW9uIOKAlCBubyBhbm5lYWxpbmcgb3Igd2FybS11cCBzY2hlZHVsZXMgbmVlZGVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9wdGltYWwgVHJhbnNwb3J0IFBhdGhzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGlsZSBhbnkgaW50ZXJwb2xhdGlvbiB3b3JrcyBmb3IgQ0ZNLCBvcHRpbWFsIHRyYW5zcG9ydCAoT1QpIHBhdGhzIG1pbmltaXplIGF2ZXJhZ2UgcGF0aCBsZW5ndGguIEJ5IHBhaXJpbmcgbm9pc2Ugc2FtcGxlcyB3aXRoIGRhdGEgcG9pbnRzIHRoYXQgbWluaW1pemUgZXhwZWN0ZWQgc3F1YXJlZCBkaXN0YW5jZSwgT1QgQ0ZNIHByb2R1Y2VzIG5lYXJseSBzdHJhaWdodCB0cmFqZWN0b3JpZXMgYWNyb3NzIHRoZSBkYXRhc2V0IOKAlCBkcmFtYXRpY2FsbHkgcmVkdWNpbmcgdGhlIG51bWJlciBvZiBPREUgc3RlcHMgbmVlZGVkIGF0IGluZmVyZW5jZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1pbmktYmF0Y2ggT1QgaXMgdGhlIHByYWN0aWNhbCBhcHByb3hpbWF0aW9uOiB3aXRoaW4gZWFjaCBiYXRjaCwgc29sdmUgdGhlIGFzc2lnbm1lbnQgcHJvYmxlbSBiZXR3ZWVuIG5vaXNlIGFuZCBkYXRhIHNhbXBsZXMgdXNpbmcgdGhlIFNpbmtob3JuIGFsZ29yaXRobS4gUmVjdGlmaWVkIEZsb3cgb2ZmZXJzIGFuIGFsdGVybmF0aXZlIOKAlCB0cmFpbiB3aXRoIHJhbmRvbSBwYWlycyBmaXJzdCwgdGhlbiByZWZsb3cgdXNpbmcgY291cGxlZCAoeDAsIHgxKSBwYWlycyBnZW5lcmF0ZWQgYnkgdGhlIGxlYXJuZWQgZmxvdy4gRWFjaCByZWZsb3cgaXRlcmF0aW9uIHN0cmFpZ2h0ZW5zIHRyYWplY3RvcmllcyBmdXJ0aGVyLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJQYXRoIFR5cGUiLCJUcmFpbmluZyBMb3NzIiwiTkZFIE5lZWRlZCIsIkZJRCAoSW1hZ2VOZXQgMjU2KSIsIkRldGVybWluaXN0aWMiXSwicm93cyI6W1siRERQTSIsIk1hcmtvdiBjaGFpbiAoMTAwMCBzdGVwcykiLCJEZW5vaXNpbmcgc2NvcmUgbWF0Y2hpbmciLCIxMDAwIiwifjMuMCIsIk5vIl0sWyJERElNIiwiT0RFIChkZXRlcm1pbmlzdGljKSIsIlNjb3JlIG1hdGNoaW5nIiwiNTAiLCJ+NC4yIiwiWWVzIl0sWyJGbG93IE1hdGNoaW5nIChsaW5lYXIpIiwiU3RyYWlnaHQtbGluZSBpbnRlcnBvbGF0aW9uIiwiVmVsb2NpdHkgcmVncmVzc2lvbiIsIjIwIiwifjIuNSIsIlllcyJdLFsiRmxvdyBNYXRjaGluZyAoT1QpIiwiT3B0aW1hbCB0cmFuc3BvcnQgcGF0aCIsIlZlbG9jaXR5IHJlZ3Jlc3Npb24gKE9UIHBhaXJzKSIsIjEwIiwifjIuMSIsIlllcyJdLFsiUmVjdGlmaWVkIEZsb3ciLCJJdGVyYXRpdmVseSBzdHJhaWdodGVuZWQiLCJWZWxvY2l0eSByZWdyZXNzaW9uIChyZWZsb3cpIiwiOC0xNSIsIn4yLjAiLCJZZXMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNGTSBUcmFpbmluZyBPYmplY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBDRk0gbG9zcyBpcyBhIHNpbXBsZSBtZWFuLXNxdWFyZWQgZXJyb3IgYmV0d2VlbiB0aGUgbmV0d29ya1x1MDAyN3MgcHJlZGljdGVkIHZlbG9jaXR5IGFuZCB0aGUgYW5hbHl0aWMgY29uZGl0aW9uYWwgdGFyZ2V0IHZlbG9jaXR5LiBCZWNhdXNlIHRoZSB0YXJnZXQgaXMgeDEgLSB4MCBmb3IgbGluZWFyIHBhdGhzLCBubyBzY29yZSBuZXR3b3JrIG9yIGVuZXJneSBmdW5jdGlvbiBpcyBuZWVkZWQuIFRoaXMgbWFrZXMgQ0ZNIHN0cmljdGx5IHNpbXBsZXIgdG8gaW1wbGVtZW50IHRoYW4gRERQTSB3aGlsZSBtYXRjaGluZyBvciBleGNlZWRpbmcgZ2VuZXJhdGlvbiBxdWFsaXR5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIENGTSB0cmFpbmluZyBsb29wXG5pbXBvcnQgdG9yY2gsIHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgY2ZtX2xvc3ModmVsb2NpdHlfbmV0LCBkYXRhX2JhdGNoKTpcbiAgICBCID0gZGF0YV9iYXRjaC5zaGFwZVswXVxuICAgIG5vaXNlID0gdG9yY2gucmFuZG5fbGlrZShkYXRhX2JhdGNoKVxuICAgIHQgPSB0b3JjaC5yYW5kKEIsIDEsIDEsIDEsIGRldmljZT1kYXRhX2JhdGNoLmRldmljZSlcblxuICAgIHhfdCA9ICgxIC0gdCkgKiBub2lzZSArIHQgKiBkYXRhX2JhdGNoXG4gICAgdGFyZ2V0X3YgPSBkYXRhX2JhdGNoIC0gbm9pc2UgICMgY29uc3RhbnQgdmVsb2NpdHlcblxuICAgIHByZWRfdiA9IHZlbG9jaXR5X25ldCh4X3QsIHQuc3F1ZWV6ZSgpKVxuICAgIHJldHVybiBGLm1zZV9sb3NzKHByZWRfdiwgdGFyZ2V0X3YpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdmVsb2NpdHkgbmV0d29yayBhcmNoaXRlY3R1cmUgbWlycm9ycyBkaWZmdXNpb24gVS1OZXRzIG9yIERpVHMuIFRoZSBvbmx5IGNoYW5nZSBpcyB0aGUgb3V0cHV0IHJlcHJlc2VudHMgYSB2ZWxvY2l0eSBmaWVsZCByYXRoZXIgdGhhbiBwcmVkaWN0ZWQgbm9pc2UuIE1vc3QgZGlmZnVzaW9uIGNvZGViYXNlcyBjYW4gYmUgYWRhcHRlZCB0byBmbG93IG1hdGNoaW5nIGJ5IGNoYW5naW5nIG9ubHkgdGhlIGxvc3MgZnVuY3Rpb24gYW5kIHNhbXBsaW5nIGxvb3Ag4oCUIHByZXRyYWluZWQgZGlmZnVzaW9uIHdlaWdodHMgY2FuIGV2ZW4gYmUgZmluZS10dW5lZCB3aXRoIGZsb3cgbWF0Y2hpbmcgb2JqZWN0aXZlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGbG93IE1hdGNoaW5nIHZzIERpZmZ1c2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlmZnVzaW9uIGxlYXJucyBhIHNjb3JlIGZ1bmN0aW9uIChncmFkaWVudCBvZiBsb2cgZGVuc2l0eSkgYXQgZWFjaCBub2lzZSBsZXZlbC4gRmxvdyBtYXRjaGluZyBsZWFybnMgYSB2ZWxvY2l0eSBmaWVsZCBkaXJlY3RseSDigJQgYSBtb3JlIGRpcmVjdCBwYXJhbWV0ZXJpemF0aW9uIHRoYXQgb2Z0ZW4gY29udmVyZ2VzIGZhc3RlciBhbmQgcHJvZHVjZXMgc3RyYWlnaHRlciBzYW1wbGluZyB0cmFqZWN0b3JpZXMuIEZ1bmN0aW9uIGV2YWx1YXRpb25zIChORkUpIGFyZSB0aGUga2V5IGVmZmljaWVuY3kgbWV0cmljOiBmbG93IG1hdGNoaW5nIHR5cGljYWxseSBuZWVkcyA4LTIwIHZzIGRpZmZ1c2lvblx1MDAyN3MgNTAtMTAwMC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBPREUgc2FtcGxpbmcgd2l0aCB0b3JjaGRpZmZlcVxuZnJvbSB0b3JjaGRpZmZlcSBpbXBvcnQgb2RlaW50XG5pbXBvcnQgdG9yY2hcblxuZGVmIHZlbG9jaXR5X2ZuKHQsIHgpOlxuICAgIHRfYmF0Y2ggPSB0LmV4cGFuZCh4LnNoYXBlWzBdKVxuICAgIHJldHVybiB2ZWxvY2l0eV9uZXQoeCwgdF9iYXRjaClcblxueF9pbml0ICA9IHRvcmNoLnJhbmRuKDQsIDMsIDI1NiwgMjU2KVxudF9zcGFuICA9IHRvcmNoLmxpbnNwYWNlKDAsIDEsIDUwKVxuXG4jIEZ1bGwgdHJhamVjdG9yeSDigJQgZmluYWwgZnJhbWUgaXMgdGhlIGdlbmVyYXRlZCBpbWFnZVxudHJhamVjdG9yeSA9IG9kZWludCh2ZWxvY2l0eV9mbiwgeF9pbml0LCB0X3NwYW4sXG4gICAgICAgICAgICAgICAgICAgIG1ldGhvZD1cdTAwMjdkb3ByaTVcdTAwMjcsIHJ0b2w9MWUtNCwgYXRvbD0xZS00KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWRhcHRpdmUgT0RFIHNvbHZlcnMgKGRvcHJpNSkgYXV0b21hdGljYWxseSBhZGp1c3Qgc3RlcCBzaXplIGZvciBhY2N1cmFjeS4gRm9yIGEgZml4ZWQtTkZFIHRyYWRlb2ZmLCBFdWxlciBpbnRlZ3JhdGlvbiB3aXRoIDEwLTIwIHN0ZXBzIG9mdGVuIHN1ZmZpY2VzIGFmdGVyIHJlZmxvdy4gR3VpZGFuY2Ugd29ya3MgaWRlbnRpY2FsbHkgdG8gZGlmZnVzaW9uOiBjbGFzc2lmaWVyLWZyZWUgZ3VpZGFuY2UgYXBwbGllcyBhdCBzYW1wbGluZyB0aW1lIGJ5IGludGVycG9sYXRpbmcgY29uZGl0aW9uYWwgYW5kIHVuY29uZGl0aW9uYWwgdmVsb2NpdHkgcHJlZGljdGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6IiMgTkZFIHZzIEZJRCB0cmFkZW9mZiBiZW5jaG1hcmtcbmRlZiBtZWFzdXJlX25mZV9maWQobW9kZWwsIHN0ZXBzX2xpc3QsIG5fc2FtcGxlcz01MDAwKTpcbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgbmZlIGluIHN0ZXBzX2xpc3Q6XG4gICAgICAgIHRfc3BhbiA9IHRvcmNoLmxpbnNwYWNlKDAsIDEsIG5mZSlcbiAgICAgICAgaW1ncyA9IGdlbmVyYXRlX3NhbXBsZXMobW9kZWwsIHRfc3Bhbiwgbl9zYW1wbGVzKVxuICAgICAgICBmaWQgPSBjb21wdXRlX2ZpZChpbWdzLCByZWFsX2RhdGFzZXQpXG4gICAgICAgIHJlc3VsdHNbbmZlXSA9IGZpZFxuICAgICAgICBwcmludChmXCJORkU9e25mZX06IEZJRD17ZmlkOi4yZn1cIilcbiAgICByZXR1cm4gcmVzdWx0c1xuXG5uZmVfbGlzdCAgICAgPSBbNSwgMTAsIDIwLCA1MCwgMTAwXVxuZmxvd19yZXN1bHRzID0gbWVhc3VyZV9uZmVfZmlkKGZsb3dfbW9kZWwsIG5mZV9saXN0KVxuZGlmZl9yZXN1bHRzID0gbWVhc3VyZV9uZmVfZmlkKGRkaW1fbW9kZWwsIG5mZV9saXN0KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZsb3cgbWF0Y2hpbmcgaXMgbm93IHRoZSBkb21pbmFudCBwYXJhZGlnbSBmb3Igc3RhdGUtb2YtdGhlLWFydCB0ZXh0LXRvLWltYWdlIG1vZGVscy4gU3RhYmxlIERpZmZ1c2lvbiAzIGFuZCBGbHV4IGJvdGggdXNlIFJlY3RpZmllZCBGbG93IHdpdGggbXVsdGktbW9kYWwgRGlUIGFyY2hpdGVjdHVyZXMuIFRyYWluaW5nIHNpbXBsaWNpdHkgKE1TRSBsb3NzLCBhbmFseXRpYyB0YXJnZXRzKSBhbmQgc2FtcGxpbmcgZWZmaWNpZW5jeSAoZmV3IE9ERSBzdGVwcykgbWFrZSBpdCBzdHJpY3RseSBzdXBlcmlvciB0byBERFBNL0RESU0gZm9yIG1vc3QgcHJhY3RpY2FsIHVzZSBjYXNlcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBwcmFjdGl0aW9uZXJzIHdpdGggZXhpc3RpbmcgZGlmZnVzaW9uIGNvZGViYXNlczogc3dpdGNoaW5nIHRvIGZsb3cgbWF0Y2hpbmcgcmVxdWlyZXMgb25seSBjaGFuZ2luZyB0aGUgbG9zcyAocHJlZGljdCB2ZWxvY2l0eSBpbnN0ZWFkIG9mIG5vaXNlKSBhbmQgdXBkYXRpbmcgdGhlIHNhbXBsaW5nIGxvb3AgdG8gdXNlIGFuIE9ERSBpbnRlZ3JhdG9yLiBUaGUgZ2VuZXJhbGl6YXRpb24gYmV5b25kIGltYWdlcyBpcyBzdWJzdGFudGlhbCDigJQgZmxvdyBtYXRjaGluZyBpcyBub3cgdXNlZCBmb3IgcHJvdGVpbiBzdHJ1Y3R1cmUsIG1vbGVjdWxhciBkeW5hbWljcywgdmlkZW8sIGFuZCBhdWRpbyBnZW5lcmF0aW9uLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVjdGlmaWVkIEZsb3dcdTAwMjdzIGl0ZXJhdGl2ZSByZWZsb3cgcHJvY2VkdXJlIGlzIHBhcnRpY3VsYXJseSBwb3dlcmZ1bDogb25lIHJlZmxvdyBpdGVyYXRpb24gdHlwaWNhbGx5IGhhbHZlcyB0aGUgTkZFIG5lZWRlZCBmb3IgdGhlIHNhbWUgRklELCBhbmQgdHdvIGl0ZXJhdGlvbnMgY2FuIGFwcHJvYWNoIG9wdGltYWwgc3RyYWlnaHQtbGluZSBwYXRocy4gVGhpcyBwb3N0LXRyYWluaW5nIHJlZmluZW1lbnQgd29ya3Mgb24gYW55IHRyYWluZWQgZmxvdyBtb2RlbCB3aXRob3V0IGFjY2VzcyB0byB0aGUgb3JpZ2luYWwgdHJhaW5pbmcgZGF0YS4ifV0="
---
# Flow Matching: Continuous Normalizing Flows for Generation

## Overview

Flow matching is a simulation-free framework for training continuous normalizing flows. Rather than solving an ODE during training, it directly regresses a velocity field that transports samples from Gaussian noise to the data distribution along smooth interpolated paths — making training as cheap as score matching.

The key insight: instead of learning to reverse a fixed noising process, flow matching learns a vector field v_t(x) such that integrating from t=0 to t=1 transforms noise into data. The path shape is a design choice — linear interpolation, optimal transport, or cosine schedules all work, each with different efficiency tradeoffs.

> **info**: Flow matching with optimal transport paths produces straighter trajectories than diffusion — meaning fewer integration steps are needed. Rectified Flow (used in SD3/Flux) iteratively straightens paths by resampling pairs along learned trajectories.

## Conditional Flow Matching

Conditional flow matching (CFM) constructs a per-sample probability path from noise x0 to data point x1. For a linear interpolation path, the conditional path is x_t = (1-t)*x0 + t*x1 where x0 ~ N(0,I). The conditional velocity field is simply the constant vector u_t = x1 - x0, pointing from noise to data.

```python
# Linear interpolation path and constant velocity target
import torch

def sample_path(x0, x1, t):
    """x0: noise, x1: data, t: scalar in [0,1]"""
    x_t = (1 - t) * x0 + t * x1
    u_t = x1 - x0  # constant for straight paths
    return x_t, u_t

x0 = torch.randn(4, 3, 64, 64)   # noise
x1 = real_batch                   # data
t  = torch.rand(4, 1, 1, 1)      # random timesteps
x_t, target_v = sample_path(x0, x1, t)
```

The velocity network v_theta(x_t, t) is trained to predict u_t. At inference, starting from x0 ~ N(0,I), integrate dx/dt = v_theta(x_t, t) from t=0 to t=1 with an ODE solver. The simplicity of the constant velocity target makes training stable from initialization — no annealing or warm-up schedules needed.

## Optimal Transport Paths

While any interpolation works for CFM, optimal transport (OT) paths minimize average path length. By pairing noise samples with data points that minimize expected squared distance, OT CFM produces nearly straight trajectories across the dataset — dramatically reducing the number of ODE steps needed at inference.

Mini-batch OT is the practical approximation: within each batch, solve the assignment problem between noise and data samples using the Sinkhorn algorithm. Rectified Flow offers an alternative — train with random pairs first, then reflow using coupled (x0, x1) pairs generated by the learned flow. Each reflow iteration straightens trajectories further.

| Method | Path Type | Training Loss | NFE Needed | FID (ImageNet 256) | Deterministic |
| --- | --- | --- | --- | --- | --- |
| DDPM | Markov chain (1000 steps) | Denoising score matching | 1000 | ~3.0 | No |
| DDIM | ODE (deterministic) | Score matching | 50 | ~4.2 | Yes |
| Flow Matching (linear) | Straight-line interpolation | Velocity regression | 20 | ~2.5 | Yes |
| Flow Matching (OT) | Optimal transport path | Velocity regression (OT pairs) | 10 | ~2.1 | Yes |
| Rectified Flow | Iteratively straightened | Velocity regression (reflow) | 8-15 | ~2.0 | Yes |

## CFM Training Objective

The CFM loss is a simple mean-squared error between the network's predicted velocity and the analytic conditional target velocity. Because the target is x1 - x0 for linear paths, no score network or energy function is needed. This makes CFM strictly simpler to implement than DDPM while matching or exceeding generation quality.

```python
# CFM training loop
import torch, torch.nn.functional as F

def cfm_loss(velocity_net, data_batch):
    B = data_batch.shape[0]
    noise = torch.randn_like(data_batch)
    t = torch.rand(B, 1, 1, 1, device=data_batch.device)

    x_t = (1 - t) * noise + t * data_batch
    target_v = data_batch - noise  # constant velocity

    pred_v = velocity_net(x_t, t.squeeze())
    return F.mse_loss(pred_v, target_v)
```

The velocity network architecture mirrors diffusion U-Nets or DiTs. The only change is the output represents a velocity field rather than predicted noise. Most diffusion codebases can be adapted to flow matching by changing only the loss function and sampling loop — pretrained diffusion weights can even be fine-tuned with flow matching objectives.

## Flow Matching vs Diffusion

Diffusion learns a score function (gradient of log density) at each noise level. Flow matching learns a velocity field directly — a more direct parameterization that often converges faster and produces straighter sampling trajectories. Function evaluations (NFE) are the key efficiency metric: flow matching typically needs 8-20 vs diffusion's 50-1000.

```python
# ODE sampling with torchdiffeq
from torchdiffeq import odeint
import torch

def velocity_fn(t, x):
    t_batch = t.expand(x.shape[0])
    return velocity_net(x, t_batch)

x_init  = torch.randn(4, 3, 256, 256)
t_span  = torch.linspace(0, 1, 50)

# Full trajectory — final frame is the generated image
trajectory = odeint(velocity_fn, x_init, t_span,
                    method='dopri5', rtol=1e-4, atol=1e-4)
```

Adaptive ODE solvers (dopri5) automatically adjust step size for accuracy. For a fixed-NFE tradeoff, Euler integration with 10-20 steps often suffices after reflow. Guidance works identically to diffusion: classifier-free guidance applies at sampling time by interpolating conditional and unconditional velocity predictions.

```python
# NFE vs FID tradeoff benchmark
def measure_nfe_fid(model, steps_list, n_samples=5000):
    results = {}
    for nfe in steps_list:
        t_span = torch.linspace(0, 1, nfe)
        imgs = generate_samples(model, t_span, n_samples)
        fid = compute_fid(imgs, real_dataset)
        results[nfe] = fid
        print(f"NFE={nfe}: FID={fid:.2f}")
    return results

nfe_list     = [5, 10, 20, 50, 100]
flow_results = measure_nfe_fid(flow_model, nfe_list)
diff_results = measure_nfe_fid(ddim_model, nfe_list)
```

## Key Takeaways

Flow matching is now the dominant paradigm for state-of-the-art text-to-image models. Stable Diffusion 3 and Flux both use Rectified Flow with multi-modal DiT architectures. Training simplicity (MSE loss, analytic targets) and sampling efficiency (few ODE steps) make it strictly superior to DDPM/DDIM for most practical use cases.

For practitioners with existing diffusion codebases: switching to flow matching requires only changing the loss (predict velocity instead of noise) and updating the sampling loop to use an ODE integrator. The generalization beyond images is substantial — flow matching is now used for protein structure, molecular dynamics, video, and audio generation.

Rectified Flow's iterative reflow procedure is particularly powerful: one reflow iteration typically halves the NFE needed for the same FID, and two iterations can approach optimal straight-line paths. This post-training refinement works on any trained flow model without access to the original training data.

