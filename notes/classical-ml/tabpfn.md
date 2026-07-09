---
title: "TabPFN — In-Context Learning for Tabular Data"
slug: "tabpfn"
description: "TabPFN performs Bayesian inference on small tabular datasets in a single forward pass by treating the entire training set as context — no gradient updates at inference time."
tags: ["tabular", "deep-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGFiUEZOIChIb2xsbWFubiBldCBhbC4gMjAyMikgaXMgYSBQcmlvci1GaXR0ZWQgTmV0d29yazogYSBUcmFuc2Zvcm1lciB0cmFpbmVkIG9mZmxpbmUgb24gbWlsbGlvbnMgb2Ygc3ludGhldGljIGRhdGFzZXRzIGRyYXduIGZyb20gYSBjYXVzYWwgZ2VuZXJhdGl2ZSBwcmlvci4gQXQgaW5mZXJlbmNlIHRpbWUsIHRoZSBlbnRpcmUgdHJhaW5pbmcgc2V0IChYX3RyYWluLCB5X3RyYWluKSBpcyBhcHBlbmRlZCBhcyBjb250ZXh0IHRva2VucywgYW5kIHRoZSBtb2RlbCBwcmVkaWN0cyB5X3Rlc3QgaW4gYSBzaW5nbGUgZm9yd2FyZCBwYXNzIOKAlCBubyBmaW5lLXR1bmluZywgbm8gdHJhaW5pbmcgbG9vcCwgbm8gaHlwZXJwYXJhbWV0ZXIgc2VhcmNoLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByaW9yLUZpdHRlZCBOZXR3b3JrcyBhbmQgSW4tQ29udGV4dCBMZWFybmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBpbnNpZ2h0OiBpZiB5b3UgdHJhaW4gYSBtZXRhLWxlYXJuZXIgb24gZGl2ZXJzZSBzeW50aGV0aWMgZGF0YXNldHMgc2FtcGxlZCBmcm9tIGEgcHJpb3IgcChEKSwgaXQgbGVhcm5zIHRvIGFwcHJveGltYXRlIEJheWVzaWFuIHBvc3RlcmlvciBpbmZlcmVuY2UgZm9yIGFueSBuZXcgZGF0YXNldCBmcm9tIHRoYXQgcHJpb3IuIEF0IHRlc3QgdGltZSwgaXQgY29uZGl0aW9ucyBvbiB0aGUgb2JzZXJ2ZWQgKFhfdHJhaW4sIHlfdHJhaW4pIHBhaXJzIHRvIHByZWRpY3QgeV90ZXN0IOKAlCB0aGUgc2FtZSBtZWNoYW5pc20gYXMgR1BUIGZldy1zaG90IGxlYXJuaW5nLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUHJpb3I6IHN5bnRoZXRpYyBkYXRhc2V0cyBkcmF3biBmcm9tIGEgY2F1c2FsIEJheWVzaWFuIG5ldHdvcmsgKHJhbmRvbSBncmFwaCwgcmFuZG9tIENQVCBwYXJhbWV0ZXJzKSIsIk1ldGEtdHJhaW5pbmc6IGdpdmVuIChYX3RyYWluLCB5X3RyYWluLCBYX3Rlc3QpLCBwcmVkaWN0IHlfdGVzdCDigJQgdHJhaW5lZCBvbiBtaWxsaW9ucyBvZiBzeW50aGV0aWMgdGFza3MiLCJJbmZlcmVuY2U6IFtYX3RyYWluOyB5X3RyYWluOyBYX3Rlc3RdIOKGkiB5X3Rlc3QgaW4gb25lIFRyYW5zZm9ybWVyIGZvcndhcmQgcGFzcyIsIk5vIGdyYWRpZW50IHVwZGF0ZXMgYXQgaW5mZXJlbmNlIOKAlCB0aGUgXHUwMDI3bGVhcm5pbmdcdTAwMjcgaGFwcGVucyBieSByZWFkaW5nIGNvbnRleHQsIG5vdCB3ZWlnaHQgdXBkYXRlcyIsIk91dHB1dDogY2xhc3MgcHJvYmFiaWxpdGllcyAoY2FsaWJyYXRlZCkgZnJvbSBzb2Z0bWF4IOKAlCBub3QganVzdCBhcmdtYXgiLCJDb21wbGV4aXR5OiBPKG7CsikgaW4gY29udGV4dCBsZW5ndGggKG4gPSBudW1iZXIgb2YgdHJhaW5pbmcgc2FtcGxlcykiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGFiUEZOIEluZmVyZW5jZSDigJQgT25lIExpbmUgb2YgQ29kZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGFiUEZOXHUwMDI3cyBBUEkgaXMgaW50ZW50aW9uYWxseSBtaW5pbWFsLiBJbnN0YWxsYXRpb24gYW5kIGluZmVyZW5jZSByZXF1aXJlIG5vIGNvbmZpZ3VyYXRpb24g4oCUIHRoZSBwcmUtdHJhaW5lZCBtb2RlbCB3ZWlnaHRzIGFyZSBkb3dubG9hZGVkIG9uY2UgYW5kIGNhY2hlZCBsb2NhbGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIHBpcCBpbnN0YWxsIHRhYnBmblxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfYnJlYXN0X2NhbmNlciwgbWFrZV9jbGFzc2lmaWNhdGlvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFjY3VyYWN5X3Njb3JlLCByb2NfYXVjX3Njb3JlXG5mcm9tIHRhYnBmbiBpbXBvcnQgVGFiUEZOQ2xhc3NpZmllclxuXG4jIFNtYWxsIHRhYnVsYXIgZGF0YXNldCAoVGFiUEZOIGRlc2lnbmVkIGZvciBuIFx1MDAzYyAxMDAwKVxuWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24oXG4gICAgbl9zYW1wbGVzPTUwMCwgbl9mZWF0dXJlcz0yMCwgbl9pbmZvcm1hdGl2ZT0xMCwgcmFuZG9tX3N0YXRlPTQyXG4pXG5YX3RyYWluLCBYX3Rlc3QsIHlfdHJhaW4sIHlfdGVzdCA9IHRyYWluX3Rlc3Rfc3BsaXQoXG4gICAgWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyXG4pXG5cbiMgVGFiUEZOOiBubyBoeXBlcnBhcmFtZXRlcnMsIG5vIHRyYWluaW5nIGxvb3BcbmNsZiA9IFRhYlBGTkNsYXNzaWZpZXIoZGV2aWNlPVx1MDAyN2NwdVx1MDAyNywgTl9lbnNlbWJsZV9jb25maWd1cmF0aW9ucz0zMilcbmNsZi5maXQoWF90cmFpbiwgeV90cmFpbikgICAjIHN0b3JlcyB0cmFpbmluZyBkYXRhIOKAlCBubyBncmFkaWVudCB1cGRhdGVzXG5cbnByb2JhICA9IGNsZi5wcmVkaWN0X3Byb2JhKFhfdGVzdClcbnByZWRzICA9IHByb2JhLmFyZ21heChheGlzPTEpXG5hY2MgICAgPSBhY2N1cmFjeV9zY29yZSh5X3Rlc3QsIHByZWRzKVxuYXVjICAgID0gcm9jX2F1Y19zY29yZSh5X3Rlc3QsIHByb2JhWzosIDFdKVxucHJpbnQoZlx1MDAyN0FjY3VyYWN5OiB7YWNjOi40Zn0gIEFVQzoge2F1YzouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmluZyBUYWJQRk4gd2l0aCBDbGFzc2ljYWwgQmFzZWxpbmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPbiBzbWFsbCB0YWJ1bGFyIGRhdGFzZXRzIChuIFx1MDAzYyAxMDAwKSwgVGFiUEZOXHUwMDI3cyBpbi1jb250ZXh0IEJheWVzaWFuIGluZmVyZW5jZSBmcmVxdWVudGx5IG91dHBlcmZvcm1zIFhHQm9vc3Qgd2l0aCBkZWZhdWx0IGh5cGVycGFyYW1ldGVycyBhbmQgY29tcGV0ZXMgd2l0aCB3ZWxsLXR1bmVkIHJhbmRvbSBmb3Jlc3RzLCBhbGwgd2l0aG91dCBhbnkgaHlwZXJwYXJhbWV0ZXIgc2VhcmNoLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgU3RyYXRpZmllZEtGb2xkXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWNjdXJhY3lfc2NvcmVcbmZyb20gc2tsZWFybi5lbnNlbWJsZSBpbXBvcnQgUmFuZG9tRm9yZXN0Q2xhc3NpZmllclxuZnJvbSB0YWJwZm4gaW1wb3J0IFRhYlBGTkNsYXNzaWZpZXJcbmltcG9ydCB4Z2Jvb3N0IGFzIHhnYlxuXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihcbiAgICBuX3NhbXBsZXM9NDAwLCBuX2ZlYXR1cmVzPTE1LCBuX2luZm9ybWF0aXZlPTgsIHJhbmRvbV9zdGF0ZT0wXG4pXG5cbnNrZiA9IFN0cmF0aWZpZWRLRm9sZChuX3NwbGl0cz01LCBzaHVmZmxlPVRydWUsIHJhbmRvbV9zdGF0ZT0wKVxubW9kZWxzID0ge1xuICAgIFx1MDAyN1RhYlBGTlx1MDAyNzogICBUYWJQRk5DbGFzc2lmaWVyKGRldmljZT1cdTAwMjdjcHVcdTAwMjcsIE5fZW5zZW1ibGVfY29uZmlndXJhdGlvbnM9MTYpLFxuICAgIFx1MDAyN1hHQm9vc3RcdTAwMjc6ICB4Z2IuWEdCQ2xhc3NpZmllcihuX2VzdGltYXRvcnM9MTAwLCByYW5kb21fc3RhdGU9MCwgZXZhbF9tZXRyaWM9XHUwMDI3bG9nbG9zc1x1MDAyNyksXG4gICAgXHUwMDI3UkZcdTAwMjc6ICAgICAgIFJhbmRvbUZvcmVzdENsYXNzaWZpZXIobl9lc3RpbWF0b3JzPTIwMCwgcmFuZG9tX3N0YXRlPTApLFxufVxuXG5mb3IgbmFtZSwgbW9kZWwgaW4gbW9kZWxzLml0ZW1zKCk6XG4gICAgc2NvcmVzID0gW11cbiAgICBmb3IgdHIsIHRlIGluIHNrZi5zcGxpdChYLCB5KTpcbiAgICAgICAgbW9kZWwuZml0KFhbdHJdLCB5W3RyXSlcbiAgICAgICAgc2NvcmVzLmFwcGVuZChhY2N1cmFjeV9zY29yZSh5W3RlXSwgbW9kZWwucHJlZGljdChYW3RlXSkpKVxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2MxMH06IHtucC5tZWFuKHNjb3Jlcyk6LjRmfSArLy0ge25wLnN0ZChzY29yZXMpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2FsaWJyYXRpb24gYW5kIFVuY2VydGFpbnR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZWNhdXNlIFRhYlBGTiBhcHByb3hpbWF0ZXMgQmF5ZXNpYW4gcG9zdGVyaW9yIGluZmVyZW5jZSwgaXRzIHByb2JhYmlsaXR5IG91dHB1dHMgYXJlIHdlbGwtY2FsaWJyYXRlZCBvdXQgb2YgdGhlIGJveC4gVGhpcyBtYWtlcyBpdCB1c2VmdWwgZm9yIHJpc2stc2Vuc2l0aXZlIGFwcGxpY2F0aW9ucyB3aGVyZSBvdmVyY29uZmlkZW50IGNsYXNzaWZpZXJzIGFyZSBwcm9ibGVtYXRpYy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmZyb20gc2tsZWFybi5jYWxpYnJhdGlvbiBpbXBvcnQgY2FsaWJyYXRpb25fY3VydmVcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBicmllcl9zY29yZV9sb3NzXG5mcm9tIHRhYnBmbiBpbXBvcnQgVGFiUEZOQ2xhc3NpZmllclxuaW1wb3J0IHhnYm9vc3QgYXMgeGdiXG5cblgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKG5fc2FtcGxlcz00MDAsIG5fZmVhdHVyZXM9MTAsIHJhbmRvbV9zdGF0ZT00MilcblhfdHIsIFhfdGUsIHlfdHIsIHlfdGUgPSB0cmFpbl90ZXN0X3NwbGl0KFgsIHksIHRlc3Rfc2l6ZT0wLjMsIHJhbmRvbV9zdGF0ZT00MilcblxubW9kZWxzID0ge1xuICAgIFx1MDAyN1RhYlBGTlx1MDAyNzogIFRhYlBGTkNsYXNzaWZpZXIoZGV2aWNlPVx1MDAyN2NwdVx1MDAyNyksXG4gICAgXHUwMDI3WEdCb29zdFx1MDAyNzogeGdiLlhHQkNsYXNzaWZpZXIobl9lc3RpbWF0b3JzPTEwMCwgZXZhbF9tZXRyaWM9XHUwMDI3bG9nbG9zc1x1MDAyNylcbn1cblxuZmlnLCBheCA9IHBsdC5zdWJwbG90cygxLCAxLCBmaWdzaXplPSg2LCA1KSlcbmF4LnBsb3QoWzAsIDFdLCBbMCwgMV0sIFx1MDAyN2stLVx1MDAyNywgbGFiZWw9XHUwMDI3UGVyZmVjdCBjYWxpYnJhdGlvblx1MDAyNylcblxuZm9yIG5hbWUsIG1vZGVsIGluIG1vZGVscy5pdGVtcygpOlxuICAgIG1vZGVsLmZpdChYX3RyLCB5X3RyKVxuICAgIHByb2JhID0gbW9kZWwucHJlZGljdF9wcm9iYShYX3RlKVs6LCAxXVxuICAgIHByb2JfdHJ1ZSwgcHJvYl9wcmVkID0gY2FsaWJyYXRpb25fY3VydmUoeV90ZSwgcHJvYmEsIG5fYmlucz0xMClcbiAgICBicmllciA9IGJyaWVyX3Njb3JlX2xvc3MoeV90ZSwgcHJvYmEpXG4gICAgYXgucGxvdChwcm9iX3ByZWQsIHByb2JfdHJ1ZSwgbWFya2VyPVx1MDAyN29cdTAwMjcsIGxhYmVsPWZcdTAwMjd7bmFtZX0gKEJyaWVyPXticmllcjouM2Z9KVx1MDAyNylcblxuYXguc2V0X3hsYWJlbChcdTAwMjdNZWFuIHByZWRpY3RlZCBwcm9iYWJpbGl0eVx1MDAyNylcbmF4LnNldF95bGFiZWwoXHUwMDI3RnJhY3Rpb24gb2YgcG9zaXRpdmVzXHUwMDI3KVxuYXgubGVnZW5kKClcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3Y2FsaWJyYXRpb24ucG5nXHUwMDI3LCBkcGk9MTUwKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNjYWxpbmcgQmVoYXZpb3I6IFdoZW4gVGFiUEZOIERlZ3JhZGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUYWJQRk5cdTAwMjdzIGNvbnRleHQgbGVuZ3RoIGlzIGxpbWl0ZWQgKHRyYWluaW5nIHN1cHBvcnRzIHVwIHRvIH4xMDI0IHJvd3MpLiBQZXJmb3JtYW5jZSBkZWdyYWRlcyBiZXlvbmQgdGhpcyBsaW1pdCwgYW5kIHRoZSBPKG7CsikgYXR0ZW50aW9uIGNvc3QgbWFrZXMgaW5mZXJlbmNlIHNsb3cuIFVuZGVyc3RhbmRpbmcgdGhpcyBjcm9zc292ZXIgaXMgZXNzZW50aWFsIGZvciBkZWNpZGluZyB3aGVuIHRvIHVzZSBUYWJQRk4uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCB0cmFpbl90ZXN0X3NwbGl0XG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWNjdXJhY3lfc2NvcmVcbmZyb20gdGFicGZuIGltcG9ydCBUYWJQRk5DbGFzc2lmaWVyXG5pbXBvcnQgeGdib29zdCBhcyB4Z2JcbmltcG9ydCB0aW1lXG5cbnRyYWluX3NpemVzID0gWzEwMCwgMjUwLCA1MDAsIDgwMCwgMTAwMF1cbnByaW50KGZcdTAwMjd7XCJuX3RyYWluXCI6XHUwMDNlOH0gIHtcIlRhYlBGTlwiOlx1MDAzZTEwfSAge1wiWEdCb29zdFwiOlx1MDAzZTEwfSAge1wiVGFiUEZOX3RcIjpcdTAwM2UxMH1cdTAwMjcpXG5cbmZvciBuIGluIHRyYWluX3NpemVzOlxuICAgIFgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKFxuICAgICAgICBuX3NhbXBsZXM9biArIDIwMCwgbl9mZWF0dXJlcz0xNSwgbl9pbmZvcm1hdGl2ZT04LCByYW5kb21fc3RhdGU9NDJcbiAgICApXG4gICAgWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoXG4gICAgICAgIFgsIHksIHRlc3Rfc2l6ZT0yMDAsIHJhbmRvbV9zdGF0ZT00MlxuICAgIClcbiAgICAjIFRhYlBGTlxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICB0YWJwZm4gPSBUYWJQRk5DbGFzc2lmaWVyKGRldmljZT1cdTAwMjdjcHVcdTAwMjcsIE5fZW5zZW1ibGVfY29uZmlndXJhdGlvbnM9OClcbiAgICB0YWJwZm4uZml0KFhfdHJbOm5dLCB5X3RyWzpuXSlcbiAgICB0YWJwZm5fYWNjID0gYWNjdXJhY3lfc2NvcmUoeV90ZSwgdGFicGZuLnByZWRpY3QoWF90ZSkpXG4gICAgdGFicGZuX3QgICA9IHRpbWUudGltZSgpIC0gdDBcbiAgICAjIFhHQm9vc3RcbiAgICB4Z2JfbW9kZWwgPSB4Z2IuWEdCQ2xhc3NpZmllcihuX2VzdGltYXRvcnM9MTAwLCByYW5kb21fc3RhdGU9NDIsIGV2YWxfbWV0cmljPVx1MDAyN2xvZ2xvc3NcdTAwMjcpXG4gICAgeGdiX21vZGVsLmZpdChYX3RyWzpuXSwgeV90cls6bl0pXG4gICAgeGdiX2FjYyA9IGFjY3VyYWN5X3Njb3JlKHlfdGUsIHhnYl9tb2RlbC5wcmVkaWN0KFhfdGUpKVxuICAgIHByaW50KGZcdTAwMjd7bjpcdTAwM2U4fSAge3RhYnBmbl9hY2M6XHUwMDNlMTAuNGZ9ICB7eGdiX2FjYzpcdTAwM2UxMC40Zn0gIHt0YWJwZm5fdDpcdTAwM2U5LjFmfXNcdTAwMjcpIn0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRhYlBGTiB2cyBDbGFzc2ljYWwgTWV0aG9kcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJuIGxpbWl0IiwiVHJhaW5pbmcgdGltZSIsIkluZmVyZW5jZSB0aW1lIiwiQWNjIChzbWFsbCBuKSIsIkFjYyAobGFyZ2UgbikiLCJIUE8gbmVlZGVkIl0sInJvd3MiOltbIlRhYlBGTiIsIn4xMDAwIChjb250ZXh0KSIsIk5vbmUgKHplcm8tc2hvdCkiLCJTZWNvbmRzIChPKG7CsikpIiwiRXhjZWxsZW50IiwiTi9BIOKAlCBub3QgYXBwbGljYWJsZSIsIk5vIl0sWyJYR0Jvb3N0IiwiTWlsbGlvbnMiLCJTZWNvbmRzIHRvIG1pbnV0ZXMiLCJNaWxsaXNlY29uZHMiLCJHb29kIiwiRXhjZWxsZW50IiwiWWVzIl0sWyJSYW5kb20gRm9yZXN0IiwiTWlsbGlvbnMiLCJTZWNvbmRzIiwiTWlsbGlzZWNvbmRzIiwiR29vZCIsIkdvb2QiLCJNb2RlcmF0ZSJdLFsiTUxQIiwiVGVucyBvZiBtaWxsaW9ucyIsIk1pbnV0ZXMgdG8gaG91cnMiLCJNaWxsaXNlY29uZHMiLCJQb29yIiwiTW9kZXJhdGUiLCJZZXMgKGhlYXZ5KSJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJUYWJQRk4gWmVyby1TaG90IFBlcmZvcm1hbmNlIiwiY29udGVudCI6IlRhYlBGTiB3aXRoIG5vIGh5cGVycGFyYW1ldGVyIHR1bmluZyBvdXRwZXJmb3JtcyBYR0Jvb3N0IHdpdGggZGVmYXVsdCBzZXR0aW5ncyBvbiB0aGUgbWFqb3JpdHkgb2YgT3Blbk1MLUNDMTggYmVuY2htYXJrIGRhdGFzZXRzIHdpdGggZmV3ZXIgdGhhbiAxMDAwIHRyYWluaW5nIHNhbXBsZXMuIEl0IGlzIHRoZSBiZXN0IGZpcnN0LXRyeSBtb2RlbCBmb3Igc21hbGwgdGFidWxhciBjbGFzc2lmaWNhdGlvbiBwcm9ibGVtcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUYWJQRk4gcGVyZm9ybXMgaW4tY29udGV4dCBCYXllc2lhbiBpbmZlcmVuY2U6IGVudGlyZSB0cmFpbmluZyBzZXQgYXMgY29udGV4dCwgcHJlZGljdGlvbnMgaW4gb25lIGZvcndhcmQgcGFzcyIsIk1ldGEtdHJhaW5lZCBvbiBtaWxsaW9ucyBvZiBzeW50aGV0aWMgZGF0YXNldHMgZnJvbSBhIGNhdXNhbCBnZW5lcmF0aXZlIHByaW9yIOKAlCBubyB0YXNrLXNwZWNpZmljIHRyYWluaW5nIiwiQmVzdCBwZXJmb3JtYW5jZSBhdCBuIFx1MDAzYyAxMDAwLCBkIFx1MDAzYyAxMDAg4oCUIG91dHNpZGUgdGhpcyByYW5nZSwgWEdCb29zdCB0eXBpY2FsbHkgd2lucyIsIldlbGwtY2FsaWJyYXRlZCBwcm9iYWJpbGl0eSBvdXRwdXRzIHdpdGhvdXQgcG9zdC1ob2MgY2FsaWJyYXRpb24gKFBsYXR0IHNjYWxpbmcsIGlzb3RvbmljIHJlZ3Jlc3Npb24pIiwiTyhuwrIpIGluZmVyZW5jZSBjb21wbGV4aXR5IOKAlCBwcmFjdGljYWwgbGltaXQgaXMgYXJvdW5kIDEwMDAgdHJhaW5pbmcgc2FtcGxlcyJdfV0="
---
# TabPFN — In-Context Learning for Tabular Data

TabPFN (Hollmann et al. 2022) is a Prior-Fitted Network: a Transformer trained offline on millions of synthetic datasets drawn from a causal generative prior. At inference time, the entire training set (X_train, y_train) is appended as context tokens, and the model predicts y_test in a single forward pass — no fine-tuning, no training loop, no hyperparameter search.

## Prior-Fitted Networks and In-Context Learning

The key insight: if you train a meta-learner on diverse synthetic datasets sampled from a prior p(D), it learns to approximate Bayesian posterior inference for any new dataset from that prior. At test time, it conditions on the observed (X_train, y_train) pairs to predict y_test — the same mechanism as GPT few-shot learning.

- Prior: synthetic datasets drawn from a causal Bayesian network (random graph, random CPT parameters)
- Meta-training: given (X_train, y_train, X_test), predict y_test — trained on millions of synthetic tasks
- Inference: [X_train; y_train; X_test] → y_test in one Transformer forward pass
- No gradient updates at inference — the 'learning' happens by reading context, not weight updates
- Output: class probabilities (calibrated) from softmax — not just argmax
- Complexity: O(n²) in context length (n = number of training samples)

## TabPFN Inference — One Line of Code

TabPFN's API is intentionally minimal. Installation and inference require no configuration — the pre-trained model weights are downloaded once and cached locally.

```python
# pip install tabpfn
import numpy as np
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from tabpfn import TabPFNClassifier

# Small tabular dataset (TabPFN designed for n < 1000)
X, y = make_classification(
    n_samples=500, n_features=20, n_informative=10, random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TabPFN: no hyperparameters, no training loop
clf = TabPFNClassifier(device='cpu', N_ensemble_configurations=32)
clf.fit(X_train, y_train)   # stores training data — no gradient updates

proba  = clf.predict_proba(X_test)
preds  = proba.argmax(axis=1)
acc    = accuracy_score(y_test, preds)
auc    = roc_auc_score(y_test, proba[:, 1])
print(f'Accuracy: {acc:.4f}  AUC: {auc:.4f}')
```

## Comparing TabPFN with Classical Baselines

On small tabular datasets (n < 1000), TabPFN's in-context Bayesian inference frequently outperforms XGBoost with default hyperparameters and competes with well-tuned random forests, all without any hyperparameter search.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from tabpfn import TabPFNClassifier
import xgboost as xgb

X, y = make_classification(
    n_samples=400, n_features=15, n_informative=8, random_state=0
)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
models = {
    'TabPFN':   TabPFNClassifier(device='cpu', N_ensemble_configurations=16),
    'XGBoost':  xgb.XGBClassifier(n_estimators=100, random_state=0, eval_metric='logloss'),
    'RF':       RandomForestClassifier(n_estimators=200, random_state=0),
}

for name, model in models.items():
    scores = []
    for tr, te in skf.split(X, y):
        model.fit(X[tr], y[tr])
        scores.append(accuracy_score(y[te], model.predict(X[te])))
    print(f'{name:<10}: {np.mean(scores):.4f} +/- {np.std(scores):.4f}')
```

## Calibration and Uncertainty

Because TabPFN approximates Bayesian posterior inference, its probability outputs are well-calibrated out of the box. This makes it useful for risk-sensitive applications where overconfident classifiers are problematic.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.calibration import calibration_curve
from sklearn.metrics import brier_score_loss
from tabpfn import TabPFNClassifier
import xgboost as xgb

X, y = make_classification(n_samples=400, n_features=10, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)

models = {
    'TabPFN':  TabPFNClassifier(device='cpu'),
    'XGBoost': xgb.XGBClassifier(n_estimators=100, eval_metric='logloss')
}

fig, ax = plt.subplots(1, 1, figsize=(6, 5))
ax.plot([0, 1], [0, 1], 'k--', label='Perfect calibration')

for name, model in models.items():
    model.fit(X_tr, y_tr)
    proba = model.predict_proba(X_te)[:, 1]
    prob_true, prob_pred = calibration_curve(y_te, proba, n_bins=10)
    brier = brier_score_loss(y_te, proba)
    ax.plot(prob_pred, prob_true, marker='o', label=f'{name} (Brier={brier:.3f})')

ax.set_xlabel('Mean predicted probability')
ax.set_ylabel('Fraction of positives')
ax.legend()
plt.tight_layout()
plt.savefig('calibration.png', dpi=150)
```

## Scaling Behavior: When TabPFN Degrades

TabPFN's context length is limited (training supports up to ~1024 rows). Performance degrades beyond this limit, and the O(n²) attention cost makes inference slow. Understanding this crossover is essential for deciding when to use TabPFN.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tabpfn import TabPFNClassifier
import xgboost as xgb
import time

train_sizes = [100, 250, 500, 800, 1000]
print(f'{"n_train":>8}  {"TabPFN":>10}  {"XGBoost":>10}  {"TabPFN_t":>10}')

for n in train_sizes:
    X, y = make_classification(
        n_samples=n + 200, n_features=15, n_informative=8, random_state=42
    )
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=200, random_state=42
    )
    # TabPFN
    t0 = time.time()
    tabpfn = TabPFNClassifier(device='cpu', N_ensemble_configurations=8)
    tabpfn.fit(X_tr[:n], y_tr[:n])
    tabpfn_acc = accuracy_score(y_te, tabpfn.predict(X_te))
    tabpfn_t   = time.time() - t0
    # XGBoost
    xgb_model = xgb.XGBClassifier(n_estimators=100, random_state=42, eval_metric='logloss')
    xgb_model.fit(X_tr[:n], y_tr[:n])
    xgb_acc = accuracy_score(y_te, xgb_model.predict(X_te))
    print(f'{n:>8}  {tabpfn_acc:>10.4f}  {xgb_acc:>10.4f}  {tabpfn_t:>9.1f}s')
```

---

## TabPFN vs Classical Methods

| Method | n limit | Training time | Inference time | Acc (small n) | Acc (large n) | HPO needed |
| --- | --- | --- | --- | --- | --- | --- |
| TabPFN | ~1000 (context) | None (zero-shot) | Seconds (O(n²)) | Excellent | N/A — not applicable | No |
| XGBoost | Millions | Seconds to minutes | Milliseconds | Good | Excellent | Yes |
| Random Forest | Millions | Seconds | Milliseconds | Good | Good | Moderate |
| MLP | Tens of millions | Minutes to hours | Milliseconds | Poor | Moderate | Yes (heavy) |

> **TabPFN Zero-Shot Performance**: TabPFN with no hyperparameter tuning outperforms XGBoost with default settings on the majority of OpenML-CC18 benchmark datasets with fewer than 1000 training samples. It is the best first-try model for small tabular classification problems.

## Key Takeaways

- TabPFN performs in-context Bayesian inference: entire training set as context, predictions in one forward pass
- Meta-trained on millions of synthetic datasets from a causal generative prior — no task-specific training
- Best performance at n < 1000, d < 100 — outside this range, XGBoost typically wins
- Well-calibrated probability outputs without post-hoc calibration (Platt scaling, isotonic regression)
- O(n²) inference complexity — practical limit is around 1000 training samples

