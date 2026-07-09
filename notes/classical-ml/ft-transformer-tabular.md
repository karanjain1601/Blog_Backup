---
title: "FT-Transformer — Feature Tokenization for Tabular Data"
slug: "ft-transformer-tabular"
description: "FT-Transformer converts each tabular feature into an embedding token and processes them with a standard Transformer encoder, enabling explicit pairwise feature interactions via self-attention."
tags: ["tabular", "deep-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRlQtVHJhbnNmb3JtZXIgKEdvcmlzaG5peSBldCBhbC4sIFlhbmRleCBSZXNlYXJjaCwgMjAyMSkgYXBwbGllcyB0aGUgVHJhbnNmb3JtZXIgYXJjaGl0ZWN0dXJlIHRvIHRhYnVsYXIgZGF0YSBieSB0cmVhdGluZyBlYWNoIGZlYXR1cmUgYXMgYSB0b2tlbi4gQSBzdGFuZGFyZCBNTFAgb3BlcmF0ZXMgb24gY29uY2F0ZW5hdGVkIHJhdyBmZWF0dXJlcyBhbmQgbGFja3MgZXhwbGljaXQgZmVhdHVyZS1pbnRlcmFjdGlvbiBtb2RlbGluZzsgRlQtVHJhbnNmb3JtZXJcdTAwMjdzIHNlbGYtYXR0ZW50aW9uIGxldHMgYW55IGZlYXR1cmUgYXR0ZW5kIHRvIGFueSBvdGhlciwgY2FwdHVyaW5nIGludGVyYWN0aW9uIGVmZmVjdHMgZGlyZWN0bHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmVhdHVyZSBUb2tlbml6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVhY2ggZmVhdHVyZSBpcyBwcm9qZWN0ZWQgdG8gYSBkLWRpbWVuc2lvbmFsIGVtYmVkZGluZyBiZWZvcmUgYmVpbmcgcHJvY2Vzc2VkIGJ5IHRoZSBUcmFuc2Zvcm1lciBlbmNvZGVyLiBOdW1lcmljYWwgYW5kIGNhdGVnb3JpY2FsIGZlYXR1cmVzIGFyZSB0b2tlbml6ZWQgZGlmZmVyZW50bHksIGJ1dCB0aGUgcmVzdWx0IGlzIHRoZSBzYW1lIHNoYXBlOiBvbmUgdmVjdG9yIG9mIGRpbWVuc2lvbiBkIHBlciBmZWF0dXJlIHBlciBzYW1wbGUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJOdW1lcmljYWwgZmVhdHVyZSBpOiBlbWJlZF9pID0gV19pIMK3IHhfaSArIGJfaSAgKHNjYWxhciDDlyBkLXZlY3RvciArIGJpYXMgPSB1bmlxdWUgZW1iZWRkaW5nIHBlciBmZWF0dXJlIHZhbHVlKSIsIkNhdGVnb3JpY2FsIGZlYXR1cmUgajogc3RhbmRhcmQgZW1iZWRkaW5nIGxvb2t1cCB0YWJsZSwgb25lIHZlY3RvciBwZXIgY2F0ZWdvcnkiLCJTcGVjaWFsIFtDTFNdIHRva2VuIHByZXBlbmRlZCB0byB0aGUgc2VxdWVuY2Ug4oCUIGl0cyBvdXRwdXQgaXMgdXNlZCBmb3IgdGhlIGZpbmFsIHByZWRpY3Rpb24iLCJTZXF1ZW5jZSBsZW5ndGggPSBudW1iZXIgb2YgZmVhdHVyZXMgKyAxIChbQ0xTXSkiLCJUcmFuc2Zvcm1lciBlbmNvZGVyIHdpdGggbXVsdGktaGVhZCBzZWxmLWF0dGVudGlvbiBwcm9jZXNzZXMgdGhlIGZ1bGwgZmVhdHVyZSB0b2tlbiBzZXF1ZW5jZSJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGVC1UcmFuc2Zvcm1lciBJbXBsZW1lbnRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVsb3cgaXMgYSBtaW5pbWFsIEZULVRyYW5zZm9ybWVyIGZvciBudW1lcmljYWwgZmVhdHVyZXMuIFRoZSBrZXkgbW9kdWxlIGlzIE51bWVyaWNhbFRva2VuaXplciwgd2hpY2ggZ2l2ZXMgZWFjaCBmZWF0dXJlIGl0cyBvd24gbGluZWFyIHByb2plY3Rpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoIGltcG9ydCBUZW5zb3JcblxuY2xhc3MgTnVtZXJpY2FsVG9rZW5pemVyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiUHJvamVjdCBlYWNoIG51bWVyaWNhbCBmZWF0dXJlIHRvIGEgZC1kaW0gZW1iZWRkaW5nLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2ZlYXR1cmVzOiBpbnQsIGRfdG9rZW46IGludCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICAjIE9uZSB3ZWlnaHQgdmVjdG9yIHBlciBmZWF0dXJlIChub3Qgc2hhcmVkKVxuICAgICAgICBzZWxmLndlaWdodCA9IG5uLlBhcmFtZXRlcih0b3JjaC5lbXB0eShuX2ZlYXR1cmVzLCBkX3Rva2VuKSlcbiAgICAgICAgc2VsZi5iaWFzICAgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mobl9mZWF0dXJlcywgZF90b2tlbikpXG4gICAgICAgIG5uLmluaXQua2FpbWluZ191bmlmb3JtXyhzZWxmLndlaWdodClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IFRlbnNvcikgLVx1MDAzZSBUZW5zb3I6ICAjIHg6IChCLCBGKVxuICAgICAgICAjIE91dGVyIHByb2R1Y3Q6IGVhY2ggc2NhbGFyIHhfaSBtdWx0aXBsaWVzIGl0cyBvd24gd2VpZ2h0IHZlY3RvclxuICAgICAgICByZXR1cm4geC51bnNxdWVlemUoLTEpICogc2VsZi53ZWlnaHQudW5zcXVlZXplKDApICsgc2VsZi5iaWFzLnVuc3F1ZWV6ZSgwKVxuICAgICAgICAjIE91dHB1dCBzaGFwZTogKEIsIEYsIGRfdG9rZW4pXG5cbmNsYXNzIEZUVHJhbnNmb3JtZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl9mZWF0dXJlczogaW50LCBkX3Rva2VuOiBpbnQsIG5faGVhZHM6IGludCxcbiAgICAgICAgICAgICAgICAgbl9sYXllcnM6IGludCwgZF9mZm46IGludCwgbl9jbGFzc2VzOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi50b2tlbml6ZXIgPSBOdW1lcmljYWxUb2tlbml6ZXIobl9mZWF0dXJlcywgZF90b2tlbilcbiAgICAgICAgc2VsZi5jbHNfdG9rZW4gPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3MoMSwgMSwgZF90b2tlbikpXG4gICAgICAgIGVuY29kZXJfbGF5ZXIgID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyTGF5ZXIoXG4gICAgICAgICAgICBkX21vZGVsPWRfdG9rZW4sIG5oZWFkPW5faGVhZHMsXG4gICAgICAgICAgICBkaW1fZmVlZGZvcndhcmQ9ZF9mZm4sIGJhdGNoX2ZpcnN0PVRydWVcbiAgICAgICAgKVxuICAgICAgICBzZWxmLmVuY29kZXIgPSBubi5UcmFuc2Zvcm1lckVuY29kZXIoZW5jb2Rlcl9sYXllciwgbnVtX2xheWVycz1uX2xheWVycylcbiAgICAgICAgc2VsZi5oZWFkICAgID0gbm4uTGluZWFyKGRfdG9rZW4sIG5fY2xhc3NlcylcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IFRlbnNvcikgLVx1MDAzZSBUZW5zb3I6ICAjIHg6IChCLCBGKVxuICAgICAgICB0b2tlbnMgPSBzZWxmLnRva2VuaXplcih4KSAgICAgICAgICAgICAgICAgICAgICAgIyAoQiwgRiwgZClcbiAgICAgICAgY2xzICAgID0gc2VsZi5jbHNfdG9rZW4uZXhwYW5kKHguc2l6ZSgwKSwgLTEsIC0xKSAgIyAoQiwgMSwgZClcbiAgICAgICAgdG9rZW5zID0gdG9yY2guY2F0KFtjbHMsIHRva2Vuc10sIGRpbT0xKSAgICAgICAgICMgKEIsIEYrMSwgZClcbiAgICAgICAgb3V0ICAgID0gc2VsZi5lbmNvZGVyKHRva2VucykgICAgICAgICAgICAgICAgICAgICMgKEIsIEYrMSwgZClcbiAgICAgICAgcmV0dXJuIHNlbGYuaGVhZChvdXRbOiwgMF0pICAgICAgICAgICAgICAgICAgICAgICMgKEIsIG5fY2xhc3NlcykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWaXN1YWxpemluZyBBdHRlbnRpb24gUGF0dGVybnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNlbGYtYXR0ZW50aW9uIHdlaWdodHMgcmV2ZWFsIHdoaWNoIGZlYXR1cmUgcGFpcnMgdGhlIG1vZGVsIHRyZWF0cyBhcyBpbnRlcmFjdGluZy4gRXh0cmFjdGluZyBhdHRlbnRpb24gbWFwcyBmcm9tIGEgdHJhaW5lZCBGVC1UcmFuc2Zvcm1lciBwcm92aWRlcyBpbnRlcnByZXRhYmxlIGZlYXR1cmUtaW50ZXJhY3Rpb24gaGVhdG1hcHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiBleHRyYWN0X2F0dGVudGlvbl93ZWlnaHRzKG1vZGVsLCB4X3NhbXBsZSk6XG4gICAgXCJcIlwiRXh0cmFjdCBhdHRlbnRpb24gd2VpZ2h0cyBmcm9tIGVhY2ggVHJhbnNmb3JtZXIgbGF5ZXIuXCJcIlwiXG4gICAgbW9kZWwuZXZhbCgpXG4gICAgYXR0ZW50aW9uX21hcHMgPSBbXVxuXG4gICAgZGVmIGhvb2tfZm4obW9kdWxlLCBpbnB1dCwgb3V0cHV0KTpcbiAgICAgICAgIyBUcmFuc2Zvcm1lckVuY29kZXJMYXllciBzdG9yZXMgYXR0bl9vdXRwdXRfd2VpZ2h0cyB3aGVuIG5lZWRfd2VpZ2h0cz1UcnVlXG4gICAgICAgIHBhc3MgICMgaG9vayBhcHByb2FjaCB2YXJpZXMgYnkgUHlUb3JjaCB2ZXJzaW9uXG5cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgdG9rZW5zID0gbW9kZWwudG9rZW5pemVyKHhfc2FtcGxlKVxuICAgICAgICBjbHMgICAgPSBtb2RlbC5jbHNfdG9rZW4uZXhwYW5kKHhfc2FtcGxlLnNpemUoMCksIC0xLCAtMSlcbiAgICAgICAgdG9rZW5zID0gdG9yY2guY2F0KFtjbHMsIHRva2Vuc10sIGRpbT0xKVxuICAgICAgICAjIEFjY2VzcyBhdHRlbnRpb24gd2VpZ2h0cyB2aWEgZm9yd2FyZCB3aXRoIG91dHB1dF9hdHRlbnRpb25zXG4gICAgICAgIGZvciBsYXllciBpbiBtb2RlbC5lbmNvZGVyLmxheWVyczpcbiAgICAgICAgICAgIGF0dG5fb3V0LCBhdHRuX3dlaWdodHMgPSBsYXllci5zZWxmX2F0dG4oXG4gICAgICAgICAgICAgICAgdG9rZW5zLCB0b2tlbnMsIHRva2VucywgbmVlZF93ZWlnaHRzPVRydWUsIGF2ZXJhZ2VfYXR0bl93ZWlnaHRzPVRydWVcbiAgICAgICAgICAgIClcbiAgICAgICAgICAgIGF0dGVudGlvbl9tYXBzLmFwcGVuZChhdHRuX3dlaWdodHMuZGV0YWNoKCkuY3B1KCkubnVtcHkoKSlcbiAgICAgICAgICAgIHRva2VucyA9IGxheWVyKHRva2VucykgICMgY29udGludWUgZm9yd2FyZCBwYXNzXG4gICAgcmV0dXJuIGF0dGVudGlvbl9tYXBzXG5cbiMgUGxvdCBhdmVyYWdlIGF0dGVudGlvbiBmb3IgZmlyc3Qgc2FtcGxlIChmZWF0dXJlIHZzIGZlYXR1cmUpXG5mZWF0dXJlX25hbWVzID0gW2ZcdTAwMjdGe2l9XHUwMDI3IGZvciBpIGluIHJhbmdlKDEwKV1cbmF0dG4gPSBucC5yYW5kb20ucmFuZCgxMSwgMTEpICAjIHBsYWNlaG9sZGVyIOKAlCByZXBsYWNlIHdpdGggYWN0dWFsIHdlaWdodHNcbnBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNikpXG5wbHQuaW1zaG93KGF0dG4sIGNtYXA9XHUwMDI3Qmx1ZXNcdTAwMjcsIHZtaW49MCwgdm1heD1hdHRuLm1heCgpKVxucGx0LmNvbG9yYmFyKGxhYmVsPVx1MDAyN0F0dGVudGlvbiB3ZWlnaHRcdTAwMjcpXG5wbHQudGl0bGUoXHUwMDI3RlQtVHJhbnNmb3JtZXIgRmVhdHVyZSBBdHRlbnRpb24gKGxheWVyIDEpXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdmdF9hdHRlbnRpb24ucG5nXHUwMDI3LCBkcGk9MTUwKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZULVRyYW5zZm9ybWVyIHZzIE1MUCB2cyBYR0Jvb3N0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPbiBhIGNvbnRyb2xsZWQgYmVuY2htYXJrLCBGVC1UcmFuc2Zvcm1lciBvdXRwZXJmb3JtcyBhIHBsYWluIE1MUCBvbiBkYXRhc2V0cyB3aXRoIHJpY2ggZmVhdHVyZSBpbnRlcmFjdGlvbnMsIGFuZCBjYW4gbWF0Y2ggWEdCb29zdCBvbiBsYXJnZXIgdGFidWxhciBkYXRhc2V0cy4gVGhlIGFkdmFudGFnZSBvdmVyIE1MUCBjb21lcyBmcm9tIGV4cGxpY2l0IHBhaXJ3aXNlIGF0dGVudGlvbjsgdGhlIGdhcCB2ZXJzdXMgWEdCb29zdCBzaHJpbmtzIHdpdGggaW5jcmVhc2luZyBuLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBhY2N1cmFjeV9zY29yZVxuZnJvbSBza2xlYXJuLm5ldXJhbF9uZXR3b3JrIGltcG9ydCBNTFBDbGFzc2lmaWVyXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcbmZyb20gc2tsZWFybi5waXBlbGluZSBpbXBvcnQgUGlwZWxpbmVcbmltcG9ydCB4Z2Jvb3N0IGFzIHhnYlxuXG4jIERhdGFzZXQgd2l0aCBpbnRlcmFjdGlvbiBlZmZlY3RzXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihcbiAgICBuX3NhbXBsZXM9NTAwMCwgbl9mZWF0dXJlcz0xMCwgbl9pbmZvcm1hdGl2ZT04LFxuICAgIG5fcmVkdW5kYW50PTAsIG5fY2x1c3RlcnNfcGVyX2NsYXNzPTIsIHJhbmRvbV9zdGF0ZT00MlxuKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoXG4gICAgWC5hc3R5cGUobnAuZmxvYXQzMiksIHksIHRlc3Rfc2l6ZT0wLjIsIHJhbmRvbV9zdGF0ZT00MlxuKVxuXG4jIFhHQm9vc3QgYmFzZWxpbmVcbnhnYl9tb2RlbCA9IHhnYi5YR0JDbGFzc2lmaWVyKG5fZXN0aW1hdG9ycz0yMDAsIG1heF9kZXB0aD02LCByYW5kb21fc3RhdGU9NDIpXG54Z2JfbW9kZWwuZml0KFhfdHIsIHlfdHIpXG5wcmludChmXHUwMDI3WEdCb29zdDogICAgICAge2FjY3VyYWN5X3Njb3JlKHlfdGUsIHhnYl9tb2RlbC5wcmVkaWN0KFhfdGUpKTouNGZ9XHUwMDI3KVxuXG4jIE1MUCBiYXNlbGluZVxubWxwID0gUGlwZWxpbmUoWyhcdTAwMjdzY1x1MDAyNywgU3RhbmRhcmRTY2FsZXIoKSksXG4gICAgICAgICAgICAgICAgKFx1MDAyN25ldFx1MDAyNywgTUxQQ2xhc3NpZmllcihoaWRkZW5fbGF5ZXJfc2l6ZXM9KDEyOCwgNjQpLCBtYXhfaXRlcj0zMDApKV0pXG5tbHAuZml0KFhfdHIsIHlfdHIpXG5wcmludChmXHUwMDI3TUxQOiAgICAgICAgICAge2FjY3VyYWN5X3Njb3JlKHlfdGUsIG1scC5wcmVkaWN0KFhfdGUpKTouNGZ9XHUwMDI3KVxuXG4jIEZULVRyYW5zZm9ybWVyIChzaW1wbGlmaWVkIHRyYWluaW5nIGxvb3ApXG5tb2RlbCA9IEZUVHJhbnNmb3JtZXIobl9mZWF0dXJlcz0xMCwgZF90b2tlbj02NCwgbl9oZWFkcz00LFxuICAgICAgICAgICAgICAgICAgICAgIG5fbGF5ZXJzPTMsIGRfZmZuPTEyOCwgbl9jbGFzc2VzPTIpXG5wcmludChmXHUwMDI3RlQtVHJhbnNmb3JtZXIgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpOix9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik51bWVyaWNhbCB2cyBDYXRlZ29yaWNhbCBUb2tlbml6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrZXkgZGVzaWduIGRlY2lzaW9uIGluIEZULVRyYW5zZm9ybWVyIGlzIGhvdyB0byB0b2tlbml6ZSBoZXRlcm9nZW5lb3VzIGZlYXR1cmUgdHlwZXMuIE51bWVyaWNhbCBmZWF0dXJlcyB1c2UgYSB1bmlxdWUgbGluZWFyIHByb2plY3Rpb24gcGVyIGZlYXR1cmU7IGNhdGVnb3JpY2FscyB1c2UgbGVhcm5lZCBlbWJlZGRpbmcgdGFibGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBDYXRlZ29yaWNhbFRva2VuaXplcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjYXJkaW5hbGl0aWVzOiBsaXN0LCBkX3Rva2VuOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgIyBPbmUgZW1iZWRkaW5nIHRhYmxlIHBlciBjYXRlZ29yaWNhbCBjb2x1bW5cbiAgICAgICAgc2VsZi5lbWJlZGRpbmdzID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBubi5FbWJlZGRpbmcobl9jYXRzLCBkX3Rva2VuKSBmb3Igbl9jYXRzIGluIGNhcmRpbmFsaXRpZXNcbiAgICAgICAgXSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHhfY2F0OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICAjIHhfY2F0OiAoQiwgbl9jYXRfZmVhdHVyZXMpIOKAlCBpbnRlZ2VyIGluZGljZXNcbiAgICAgICAgdG9rZW5zID0gW2VtYih4X2NhdFs6LCBpXSkgZm9yIGksIGVtYiBpbiBlbnVtZXJhdGUoc2VsZi5lbWJlZGRpbmdzKV1cbiAgICAgICAgcmV0dXJuIHRvcmNoLnN0YWNrKHRva2VucywgZGltPTEpICAjIChCLCBuX2NhdF9mZWF0dXJlcywgZF90b2tlbilcblxuY2xhc3MgTWl4ZWRUb2tlbml6ZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl9udW06IGludCwgY2FyZGluYWxpdGllczogbGlzdCwgZF90b2tlbjogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubnVtX3Rva2VuaXplciA9IE51bWVyaWNhbFRva2VuaXplcihuX251bSwgZF90b2tlbilcbiAgICAgICAgc2VsZi5jYXRfdG9rZW5pemVyID0gQ2F0ZWdvcmljYWxUb2tlbml6ZXIoY2FyZGluYWxpdGllcywgZF90b2tlbilcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHhfbnVtOiB0b3JjaC5UZW5zb3IsIHhfY2F0OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBudW1fdG9rZW5zID0gc2VsZi5udW1fdG9rZW5pemVyKHhfbnVtKSAgIyAoQiwgbl9udW0sIGQpXG4gICAgICAgIGNhdF90b2tlbnMgPSBzZWxmLmNhdF90b2tlbml6ZXIoeF9jYXQpICAjIChCLCBuX2NhdCwgZClcbiAgICAgICAgcmV0dXJuIHRvcmNoLmNhdChbbnVtX3Rva2VucywgY2F0X3Rva2Vuc10sIGRpbT0xKSAgIyAoQiwgbl9udW0rbl9jYXQsIGQpXG5cbiMgVGVzdFxudG9rZW5pemVyID0gTWl4ZWRUb2tlbml6ZXIobl9udW09NSwgY2FyZGluYWxpdGllcz1bMTAsIDUwLCAyMDBdLCBkX3Rva2VuPTY0KVxueF9udW0gPSB0b3JjaC5yYW5kbigzMiwgNSlcbnhfY2F0ID0gdG9yY2gucmFuZGludCgwLCAxMCwgKDMyLCAzKSlcbnRva2VucyA9IHRva2VuaXplcih4X251bSwgeF9jYXQpXG5wcmludChmXHUwMDI3VG9rZW4gc2VxdWVuY2Ugc2hhcGU6IHt0b2tlbnMuc2hhcGV9XHUwMDI3KSAgIyAoMzIsIDgsIDY0KSJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcmNoaXRlY3R1cmUgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJBcmNoaXRlY3R1cmUiLCJGZWF0dXJlIEludGVyYWN0aW9ucyIsIkF0dGVudGlvbiIsIlByZXRyYWluaW5nIiwiQmVuY2htYXJrIiwiU2NhbGFiaWxpdHkiXSwicm93cyI6W1siUGxhaW4gTUxQIiwiSW1wbGljaXQgKGFsbCBsYXllcnMpIiwiTm9uZSIsIk5vbmUiLCJXZWFrZXIgb24gaW50ZXJhY3Rpb24taGVhdnkgZGF0YSIsIkZhc3QgdHJhaW5pbmciXSxbIkZULVRyYW5zZm9ybWVyIiwiRXhwbGljaXQgcGFpcndpc2UgKHNlbGYtYXR0ZW50aW9uKSIsIkZlYXR1cmUtdG8tZmVhdHVyZSIsIk1MTS1zdHlsZSBwb3NzaWJsZSIsIkNvbXBldGl0aXZlIHdpdGggWEdCb29zdCBhdCBsYXJnZSBuIiwiTyhGwrIpIHBlciBsYXllciJdLFsiVGFiTmV0IiwiU2VxdWVudGlhbCBzcGFyc2UgKGF0dGVudGlvbiBtYXNrKSIsIlN0ZXAtd2lzZSBmZWF0dXJlIHNlbGVjdGlvbiIsIlJlY29uc3RydWN0aW9uIHByZXRyYWluaW5nIiwiQ29tcGV0aXRpdmUsIG9mdGVuIGJlaGluZCBGVC1UcmFuc2Zvcm1lciIsIk8oRikgcGVyIHN0ZXAiXSxbIlhHQm9vc3QiLCJFeHBsaWNpdCAoc3BsaXQgaGllcmFyY2h5KSIsIk5vbmUg4oCUIGdyZWVkeSBzcGxpdHRpbmciLCJOb25lIiwiU3RhdGUtb2YtdGhlLWFydCBvbiBtb3N0IGJlbmNobWFya3MiLCJTY2FsZXMgdG8gbWlsbGlvbnMgb2Ygcm93cyJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJGVC1UcmFuc2Zvcm1lciBCZXN0IFVzZSBDYXNlcyIsImNvbnRlbnQiOiJGVC1UcmFuc2Zvcm1lciBpcyBtb3N0IGVmZmVjdGl2ZSB3aGVuICgxKSB5b3VyIGRhdGFzZXQgaXMgbGFyZ2UgZW5vdWdoIChuIFx1MDAzZSAxMGspIHRvIHRyYWluIGRlZXAgYXR0ZW50aW9uIGxheWVycywgKDIpIGZlYXR1cmVzIGhhdmUgbWVhbmluZ2Z1bCBwYWlyd2lzZSBpbnRlcmFjdGlvbnMgdGhhdCBheGlzLWFsaWduZWQgc3BsaXRzIG1pc3MsIGFuZCAoMykgeW91IHdhbnQgYSBzaW5nbGUgbmV1cmFsIGJhY2tib25lIGZvciB0YWJ1bGFyICsgb3RoZXIgbW9kYWxpdGllcyBpbiBhbiBlbmQtdG8tZW5kIHN5c3RlbS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJGVC1UcmFuc2Zvcm1lciB0b2tlbml6ZXMgZWFjaCBmZWF0dXJlIGludG8gYSBkLWRpbSB2ZWN0b3Ig4oCUIG51bWVyaWNhbCB2aWEgdW5pcXVlIGxpbmVhciBwcm9qZWN0aW9uLCBjYXRlZ29yaWNhbCB2aWEgZW1iZWRkaW5nIGxvb2t1cCIsIkEgW0NMU10gdG9rZW4gYWdncmVnYXRlcyBpbmZvcm1hdGlvbiBmcm9tIGFsbCBmZWF0dXJlIHRva2VuczsgaXRzIG91dHB1dCBkcml2ZXMgdGhlIHByZWRpY3Rpb24gaGVhZCIsIlNlbGYtYXR0ZW50aW9uIGVuYWJsZXMgZXhwbGljaXQsIGxlYXJuYWJsZSBwYWlyd2lzZSBmZWF0dXJlIGludGVyYWN0aW9ucyDigJQgdW5saWtlIE1MUCB3aGljaCByZWxpZXMgb24gaW1wbGljaXQgaW50ZXJhY3Rpb25zIiwiRlQtVHJhbnNmb3JtZXIgY29tcGV0ZXMgd2l0aCBYR0Jvb3N0IG9uIGxhcmdlIHRhYnVsYXIgZGF0YXNldHMgYnV0IHJhcmVseSBvdXRwZXJmb3JtcyBpdCBvbiBzbWFsbCBuIiwiTWl4ZWQgbnVtZXJpY2FsLWNhdGVnb3JpY2FsIGlucHV0cyBhcmUgaGFuZGxlZCBjbGVhbmx5IHdpdGggZGlmZmVyZW50IHRva2VuaXplciBoZWFkcyJdfV0="
---
# FT-Transformer — Feature Tokenization for Tabular Data

FT-Transformer (Gorishniy et al., Yandex Research, 2021) applies the Transformer architecture to tabular data by treating each feature as a token. A standard MLP operates on concatenated raw features and lacks explicit feature-interaction modeling; FT-Transformer's self-attention lets any feature attend to any other, capturing interaction effects directly.

## Feature Tokenization

Each feature is projected to a d-dimensional embedding before being processed by the Transformer encoder. Numerical and categorical features are tokenized differently, but the result is the same shape: one vector of dimension d per feature per sample.

- Numerical feature i: embed_i = W_i · x_i + b_i  (scalar × d-vector + bias = unique embedding per feature value)
- Categorical feature j: standard embedding lookup table, one vector per category
- Special [CLS] token prepended to the sequence — its output is used for the final prediction
- Sequence length = number of features + 1 ([CLS])
- Transformer encoder with multi-head self-attention processes the full feature token sequence

## FT-Transformer Implementation

Below is a minimal FT-Transformer for numerical features. The key module is NumericalTokenizer, which gives each feature its own linear projection.

```python
import torch
import torch.nn as nn
from torch import Tensor

class NumericalTokenizer(nn.Module):
    """Project each numerical feature to a d-dim embedding."""
    def __init__(self, n_features: int, d_token: int):
        super().__init__()
        # One weight vector per feature (not shared)
        self.weight = nn.Parameter(torch.empty(n_features, d_token))
        self.bias   = nn.Parameter(torch.zeros(n_features, d_token))
        nn.init.kaiming_uniform_(self.weight)

    def forward(self, x: Tensor) -> Tensor:  # x: (B, F)
        # Outer product: each scalar x_i multiplies its own weight vector
        return x.unsqueeze(-1) * self.weight.unsqueeze(0) + self.bias.unsqueeze(0)
        # Output shape: (B, F, d_token)

class FTTransformer(nn.Module):
    def __init__(self, n_features: int, d_token: int, n_heads: int,
                 n_layers: int, d_ffn: int, n_classes: int):
        super().__init__()
        self.tokenizer = NumericalTokenizer(n_features, d_token)
        self.cls_token = nn.Parameter(torch.zeros(1, 1, d_token))
        encoder_layer  = nn.TransformerEncoderLayer(
            d_model=d_token, nhead=n_heads,
            dim_feedforward=d_ffn, batch_first=True
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        self.head    = nn.Linear(d_token, n_classes)

    def forward(self, x: Tensor) -> Tensor:  # x: (B, F)
        tokens = self.tokenizer(x)                       # (B, F, d)
        cls    = self.cls_token.expand(x.size(0), -1, -1)  # (B, 1, d)
        tokens = torch.cat([cls, tokens], dim=1)         # (B, F+1, d)
        out    = self.encoder(tokens)                    # (B, F+1, d)
        return self.head(out[:, 0])                      # (B, n_classes)
```

## Visualizing Attention Patterns

Self-attention weights reveal which feature pairs the model treats as interacting. Extracting attention maps from a trained FT-Transformer provides interpretable feature-interaction heatmaps.

```python
import torch
import numpy as np
import matplotlib.pyplot as plt

def extract_attention_weights(model, x_sample):
    """Extract attention weights from each Transformer layer."""
    model.eval()
    attention_maps = []

    def hook_fn(module, input, output):
        # TransformerEncoderLayer stores attn_output_weights when need_weights=True
        pass  # hook approach varies by PyTorch version

    with torch.no_grad():
        tokens = model.tokenizer(x_sample)
        cls    = model.cls_token.expand(x_sample.size(0), -1, -1)
        tokens = torch.cat([cls, tokens], dim=1)
        # Access attention weights via forward with output_attentions
        for layer in model.encoder.layers:
            attn_out, attn_weights = layer.self_attn(
                tokens, tokens, tokens, need_weights=True, average_attn_weights=True
            )
            attention_maps.append(attn_weights.detach().cpu().numpy())
            tokens = layer(tokens)  # continue forward pass
    return attention_maps

# Plot average attention for first sample (feature vs feature)
feature_names = [f'F{i}' for i in range(10)]
attn = np.random.rand(11, 11)  # placeholder — replace with actual weights
plt.figure(figsize=(8, 6))
plt.imshow(attn, cmap='Blues', vmin=0, vmax=attn.max())
plt.colorbar(label='Attention weight')
plt.title('FT-Transformer Feature Attention (layer 1)')
plt.tight_layout()
plt.savefig('ft_attention.png', dpi=150)
```

## FT-Transformer vs MLP vs XGBoost

On a controlled benchmark, FT-Transformer outperforms a plain MLP on datasets with rich feature interactions, and can match XGBoost on larger tabular datasets. The advantage over MLP comes from explicit pairwise attention; the gap versus XGBoost shrinks with increasing n.

```python
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import xgboost as xgb

# Dataset with interaction effects
X, y = make_classification(
    n_samples=5000, n_features=10, n_informative=8,
    n_redundant=0, n_clusters_per_class=2, random_state=42
)
X_tr, X_te, y_tr, y_te = train_test_split(
    X.astype(np.float32), y, test_size=0.2, random_state=42
)

# XGBoost baseline
xgb_model = xgb.XGBClassifier(n_estimators=200, max_depth=6, random_state=42)
xgb_model.fit(X_tr, y_tr)
print(f'XGBoost:       {accuracy_score(y_te, xgb_model.predict(X_te)):.4f}')

# MLP baseline
mlp = Pipeline([('sc', StandardScaler()),
                ('net', MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=300))])
mlp.fit(X_tr, y_tr)
print(f'MLP:           {accuracy_score(y_te, mlp.predict(X_te)):.4f}')

# FT-Transformer (simplified training loop)
model = FTTransformer(n_features=10, d_token=64, n_heads=4,
                      n_layers=3, d_ffn=128, n_classes=2)
print(f'FT-Transformer params: {sum(p.numel() for p in model.parameters()):,}')
```

## Numerical vs Categorical Tokenization

The key design decision in FT-Transformer is how to tokenize heterogeneous feature types. Numerical features use a unique linear projection per feature; categoricals use learned embedding tables.

```python
import torch
import torch.nn as nn

class CategoricalTokenizer(nn.Module):
    def __init__(self, cardinalities: list, d_token: int):
        super().__init__()
        # One embedding table per categorical column
        self.embeddings = nn.ModuleList([
            nn.Embedding(n_cats, d_token) for n_cats in cardinalities
        ])

    def forward(self, x_cat: torch.Tensor) -> torch.Tensor:
        # x_cat: (B, n_cat_features) — integer indices
        tokens = [emb(x_cat[:, i]) for i, emb in enumerate(self.embeddings)]
        return torch.stack(tokens, dim=1)  # (B, n_cat_features, d_token)

class MixedTokenizer(nn.Module):
    def __init__(self, n_num: int, cardinalities: list, d_token: int):
        super().__init__()
        self.num_tokenizer = NumericalTokenizer(n_num, d_token)
        self.cat_tokenizer = CategoricalTokenizer(cardinalities, d_token)

    def forward(self, x_num: torch.Tensor, x_cat: torch.Tensor) -> torch.Tensor:
        num_tokens = self.num_tokenizer(x_num)  # (B, n_num, d)
        cat_tokens = self.cat_tokenizer(x_cat)  # (B, n_cat, d)
        return torch.cat([num_tokens, cat_tokens], dim=1)  # (B, n_num+n_cat, d)

# Test
tokenizer = MixedTokenizer(n_num=5, cardinalities=[10, 50, 200], d_token=64)
x_num = torch.randn(32, 5)
x_cat = torch.randint(0, 10, (32, 3))
tokens = tokenizer(x_num, x_cat)
print(f'Token sequence shape: {tokens.shape}')  # (32, 8, 64)
```

---

## Architecture Comparison

| Architecture | Feature Interactions | Attention | Pretraining | Benchmark | Scalability |
| --- | --- | --- | --- | --- | --- |
| Plain MLP | Implicit (all layers) | None | None | Weaker on interaction-heavy data | Fast training |
| FT-Transformer | Explicit pairwise (self-attention) | Feature-to-feature | MLM-style possible | Competitive with XGBoost at large n | O(F²) per layer |
| TabNet | Sequential sparse (attention mask) | Step-wise feature selection | Reconstruction pretraining | Competitive, often behind FT-Transformer | O(F) per step |
| XGBoost | Explicit (split hierarchy) | None — greedy splitting | None | State-of-the-art on most benchmarks | Scales to millions of rows |

> **FT-Transformer Best Use Cases**: FT-Transformer is most effective when (1) your dataset is large enough (n > 10k) to train deep attention layers, (2) features have meaningful pairwise interactions that axis-aligned splits miss, and (3) you want a single neural backbone for tabular + other modalities in an end-to-end system.

## Key Takeaways

- FT-Transformer tokenizes each feature into a d-dim vector — numerical via unique linear projection, categorical via embedding lookup
- A [CLS] token aggregates information from all feature tokens; its output drives the prediction head
- Self-attention enables explicit, learnable pairwise feature interactions — unlike MLP which relies on implicit interactions
- FT-Transformer competes with XGBoost on large tabular datasets but rarely outperforms it on small n
- Mixed numerical-categorical inputs are handled cleanly with different tokenizer heads

