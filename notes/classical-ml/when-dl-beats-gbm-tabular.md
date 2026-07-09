---
title: "When Deep Learning Beats Gradient Boosting on Tabular Data"
slug: "when-dl-beats-gbm-tabular"
description: "Conditions where neural networks outperform gradient-boosted trees on tabular data: large datasets, multi-modal inputs, smooth functions, online learning, and multi-task scenarios."
tags: ["tabular", "deep-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR3JhZGllbnQtYm9vc3RlZCB0cmVlcyB3aW4gb24gbW9zdCB0YWJ1bGFyIGJlbmNobWFya3Mg4oCUIGJ1dCBub3QgYWxsLiBOZXVyYWwgbmV0d29ya3MgaGF2ZSBzdHJ1Y3R1cmFsIGFkdmFudGFnZXMgaW4gc3BlY2lmaWMgc2NlbmFyaW9zOiB2ZXJ5IGxhcmdlIGRhdGFzZXRzLCBtdWx0aS1tb2RhbCBpbnB1dHMsIHN0cmVhbWluZyBkYXRhLCBtdWx0aS10YXNrIGxlYXJuaW5nLCBhbmQgc21vb3RoIHRhcmdldCBmdW5jdGlvbnMuIEtub3dpbmcgdGhlc2UgY29uZGl0aW9ucyBoZWxwcyB5b3UgY2hvb3NlIHRoZSByaWdodCB0b29sIHJhdGhlciB0aGFuIGRlZmF1bHRpbmcgdG8gWEdCb29zdCBldmVyeXdoZXJlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbmRpdGlvbnMgRmF2b3JpbmcgRGVlcCBMZWFybmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2V2ZW4gY29uZGl0aW9ucyB3aGVyZSBETCBvdXRwZXJmb3JtcyBHQk0gb24gdGFidWxhciBkYXRhLCBlYWNoIHJvb3RlZCBpbiBhIHN0cnVjdHVyYWwgYWR2YW50YWdlIG9mIG5ldXJhbCBuZXR3b3JrcyBvdmVyIGRlY2lzaW9uIHRyZWVzOiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVmVyeSBsYXJnZSBuIChcdTAwM2UxTSk6IHRyZWUgaW5mZXJlbmNlIGlzIGxpbmVhciBpbiBuX2VzdGltYXRvcnMgw5cgdHJlZSBkZXB0aDsgTk4gaW5mZXJlbmNlIGlzIE8oMSkgaW4gbiIsIk11bHRpLW1vZGFsIGlucHV0czogTk4gaGFuZGxlcyB0YWJ1bGFyICsgaW1hZ2VzICsgdGV4dCBpbiBvbmUgbW9kZWw7IHRyZWVzIGNhbm5vdCBwcm9jZXNzIHJhdyBwaXhlbHMgb3IgdG9rZW4gc2VxdWVuY2VzIiwiU21vb3RoIHRhcmdldCBmdW5jdGlvbnM6IHBoeXNpY2FsIHNpbXVsYXRpb25zLCBmaW5hbmNpYWwgcHJpY2luZyBtb2RlbHMg4oCUIE5OIGltcGxpY2l0IHJlZ3VsYXJpemF0aW9uIGZpdHMgc21vb3RoIGZ1bmN0aW9ucyBiZXR0ZXIiLCJPbmxpbmUvc3RyZWFtaW5nIGxlYXJuaW5nOiBOTiB3aXRoIFNHRCB1cGRhdGVzIGluY3JlbWVudGFsbHkgZnJvbSBuZXcgc2FtcGxlczsgdHJlZXMgbmVlZCBmdWxsIHJlYnVpbGRzIiwiTXVsdGktdGFzayBsZWFybmluZzogc2hhcmVkIE5OIHJlcHJlc2VudGF0aW9ucyBnZW5lcmFsaXplIGFjcm9zcyByZWxhdGVkIHRhc2tzOyBzZXBhcmF0ZSB0cmVlcyBwZXIgdGFzayBkb25cdTAwMjd0IHNoYXJlIGNhcGFjaXR5IiwiVHJhbnNmZXIgbGVhcm5pbmc6IHByZS10cmFpbmVkIHRhYnVsYXIgdHJhbnNmb3JtZXJzIChUYWJQRk4sIHByaW9yIHdvcmspIGNhbiBiZSBmaW5lLXR1bmVkOyBubyB0cmVlIGVxdWl2YWxlbnQiLCJFbmQtdG8tZW5kIHN5c3RlbXM6IHJlY29tbWVuZGF0aW9uLCByYW5raW5nIOKAlCBOTiBpbnRlZ3JhdGVzIHVzZXIgZW1iZWRkaW5nICsgaXRlbSBmZWF0dXJlcyArIGNvbnRleHQgam9pbnRseSJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJETCB2cyBHQk0gQWNyb3NzIERhdGFzZXQgU2l6ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjcm9zc292ZXIgYmV0d2VlbiBHQk0gYW5kIERMIGFjY3VyYWN5IGRlcGVuZHMgb24gZGF0YXNldCBzaXplLiBUcmVlcyBkb21pbmF0ZSBhdCBzbWFsbCBuOyB0aGUgZ2FwIG5hcnJvd3MgYXMgbiBncm93cy4gVGhpcyBiZW5jaG1hcmsgaWxsdXN0cmF0ZXMgdGhlIHRyZW5kIGFjcm9zcyBmaXZlIG9yZGVycyBvZiBtYWduaXR1ZGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCBjcm9zc192YWxfc2NvcmVcbmZyb20gc2tsZWFybi5uZXVyYWxfbmV0d29yayBpbXBvcnQgTUxQQ2xhc3NpZmllclxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5mcm9tIHNrbGVhcm4ucGlwZWxpbmUgaW1wb3J0IFBpcGVsaW5lXG5pbXBvcnQgeGdib29zdCBhcyB4Z2JcbmltcG9ydCB0aW1lXG5cbnNpemVzID0gWzEwMCwgNTAwLCAxMDAwLCA1MDAwLCAxMDAwMCwgNTAwMDBdXG5yZXN1bHRzID0gW11cblxuZm9yIG4gaW4gc2l6ZXM6XG4gICAgWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24oXG4gICAgICAgIG5fc2FtcGxlcz1uLCBuX2ZlYXR1cmVzPTIwLCBuX2luZm9ybWF0aXZlPTEwLCByYW5kb21fc3RhdGU9NDJcbiAgICApXG4gICAgZ2JtID0geGdiLlhHQkNsYXNzaWZpZXIobl9lc3RpbWF0b3JzPTIwMCwgbWF4X2RlcHRoPTYsIGxlYXJuaW5nX3JhdGU9MC4wNSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcmFuZG9tX3N0YXRlPTQyLCBldmFsX21ldHJpYz1cdTAwMjdsb2dsb3NzXHUwMDI3KVxuICAgIG1scCA9IFBpcGVsaW5lKFtcbiAgICAgICAgKFx1MDAyN3NjXHUwMDI3LCBTdGFuZGFyZFNjYWxlcigpKSxcbiAgICAgICAgKFx1MDAyN25ldFx1MDAyNywgTUxQQ2xhc3NpZmllcihcbiAgICAgICAgICAgIGhpZGRlbl9sYXllcl9zaXplcz0oMjU2LCAxMjgsIDY0KSwgbWF4X2l0ZXI9NDAwLFxuICAgICAgICAgICAgZWFybHlfc3RvcHBpbmc9VHJ1ZSwgcmFuZG9tX3N0YXRlPTQyXG4gICAgICAgICkpXG4gICAgXSlcbiAgICBjdiA9IG1heCgzLCBtaW4oNSwgbiAvLyA1MDApKVxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBnYm1fc2NvcmUgPSBjcm9zc192YWxfc2NvcmUoZ2JtLCBYLCB5LCBjdj1jdikubWVhbigpXG4gICAgZ2JtX3RpbWUgID0gdGltZS50aW1lKCkgLSB0MFxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBtbHBfc2NvcmUgPSBjcm9zc192YWxfc2NvcmUobWxwLCBYLCB5LCBjdj1jdikubWVhbigpXG4gICAgbWxwX3RpbWUgID0gdGltZS50aW1lKCkgLSB0MFxuICAgIHByaW50KGZcdTAwMjduPXtuOlx1MDAzZTZ9OiBHQk09e2dibV9zY29yZTouM2Z9KHtnYm1fdGltZTouMWZ9cykgIE1MUD17bWxwX3Njb3JlOi4zZn0oe21scF90aW1lOi4xZn1zKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1UYXNrIExlYXJuaW5nIHdpdGggU2hhcmVkIFJlcHJlc2VudGF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmV1cmFsIG5ldHdvcmtzIGxlYXJuIHNoYXJlZCBmZWF0dXJlIHJlcHJlc2VudGF0aW9ucyBhY3Jvc3MgcmVsYXRlZCB0YXNrcy4gQSBzaW5nbGUgYmFja2JvbmUgdHJhaW5lZCBvbiBtdWx0aXBsZSB0YWJ1bGFyIHRhcmdldHMgc2ltdWx0YW5lb3VzbHkgb2Z0ZW4gb3V0cGVyZm9ybXMgcGVyLXRhc2sgdHJlZXMsIGVzcGVjaWFsbHkgd2hlbiB0YXNrcyBzaGFyZSB1bmRlcmx5aW5nIHN0cnVjdHVyZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YUxvYWRlciwgVGVuc29yRGF0YXNldFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cblxuY2xhc3MgTXVsdGlUYXNrVGFidWxhcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2ZlYXR1cmVzOiBpbnQsIGhpZGRlbjogaW50LCBuX3Rhc2tzOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgIyBTaGFyZWQgZW5jb2RlciDigJQgbGVhcm5zIHJlcHJlc2VudGF0aW9ucyB1c2VmdWwgYWNyb3NzIGFsbCB0YXNrc1xuICAgICAgICBzZWxmLmJhY2tib25lID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihuX2ZlYXR1cmVzLCBoaWRkZW4pLCBubi5MYXllck5vcm0oaGlkZGVuKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuIC8vIDIpLCBubi5MYXllck5vcm0oaGlkZGVuIC8vIDIpLCBubi5SZUxVKClcbiAgICAgICAgKVxuICAgICAgICAjIFRhc2stc3BlY2lmaWMgaGVhZHNcbiAgICAgICAgc2VsZi5oZWFkcyA9IG5uLk1vZHVsZUxpc3QoW1xuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiAvLyAyLCAxKSBmb3IgXyBpbiByYW5nZShuX3Rhc2tzKVxuICAgICAgICBdKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIGxpc3Q6XG4gICAgICAgIHNoYXJlZCA9IHNlbGYuYmFja2JvbmUoeClcbiAgICAgICAgcmV0dXJuIFtoZWFkKHNoYXJlZCkuc3F1ZWV6ZSgtMSkgZm9yIGhlYWQgaW4gc2VsZi5oZWFkc11cblxuIyBNdWx0aS10YXNrIGRhdGFzZXQ6IDMgY29ycmVsYXRlZCBiaW5hcnkgdGFyZ2V0c1xubnAucmFuZG9tLnNlZWQoNDIpXG5YID0gbnAucmFuZG9tLnJhbmRuKDIwMDAsIDIwKS5hc3R5cGUobnAuZmxvYXQzMilcbnkxID0gKFhbOiwgMF0gKyBYWzosIDFdIFx1MDAzZSAwKS5hc3R5cGUobnAuZmxvYXQzMilcbnkyID0gKFhbOiwgMF0gLSBYWzosIDJdIFx1MDAzZSAwKS5hc3R5cGUobnAuZmxvYXQzMilcbnkzID0gKFhbOiwgMV0gKyBYWzosIDNdIFx1MDAzZSAwKS5hc3R5cGUobnAuZmxvYXQzMilcblxubW9kZWwgID0gTXVsdGlUYXNrVGFidWxhcihuX2ZlYXR1cmVzPTIwLCBoaWRkZW49MTI4LCBuX3Rhc2tzPTMpXG5jcml0ZXJpb24gPSBubi5CQ0VXaXRoTG9naXRzTG9zcygpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbnByaW50KGZcdTAwMjdTaGFyZWQgYmFja2JvbmUgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5iYWNrYm9uZS5wYXJhbWV0ZXJzKCkpOix9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9ubGluZSBMZWFybmluZzogSW5jcmVtZW50YWwgTk4gdnMgUmVidWlsZGluZyBUcmVlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIHN0cmVhbWluZyBkYXRhLCBuZXVyYWwgbmV0d29ya3MgdXBkYXRlIG5hdHVyYWxseSBmcm9tIGVhY2ggbmV3IGJhdGNoIHZpYSBTR0QuIFRyZWUgbW9kZWxzIHJlcXVpcmUgZnVsbCByZXRyYWluaW5nIHdoZW4gbmV3IGRhdGEgYXJyaXZlcywgbWFraW5nIHRoZW0gaW1wcmFjdGljYWwgZm9yIGhpZ2gtdmVsb2NpdHkgc3RyZWFtcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgU0dEQ2xhc3NpZmllclxuZnJvbSBza2xlYXJuLmVuc2VtYmxlIGltcG9ydCBSYW5kb21Gb3Jlc3RDbGFzc2lmaWVyXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWNjdXJhY3lfc2NvcmVcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ybmcgID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxubl90b3RhbCwgbl9pbml0LCBiYXRjaF9zaXplID0gNTAwMCwgMTAwMCwgMTAwXG5cblhfYWxsID0gcm5nLnN0YW5kYXJkX25vcm1hbCgobl90b3RhbCwgMTApKS5hc3R5cGUobnAuZmxvYXQzMilcbnlfYWxsID0gKFhfYWxsWzosIDBdICsgWF9hbGxbOiwgMV0gXHUwMDNlIDApLmFzdHlwZShpbnQpXG5cbnNjID0gU3RhbmRhcmRTY2FsZXIoKS5maXQoWF9hbGxbOm5faW5pdF0pXG5YX2FsbF9zYyA9IHNjLnRyYW5zZm9ybShYX2FsbClcblxuIyBPbmxpbmUgbGVhcm5lcjogU0dEQ2xhc3NpZmllciBzdXBwb3J0cyBwYXJ0aWFsX2ZpdFxuc2dkID0gU0dEQ2xhc3NpZmllcihsb3NzPVx1MDAyN2xvZ19sb3NzXHUwMDI3LCByYW5kb21fc3RhdGU9NDIpXG5zZ2QucGFydGlhbF9maXQoWF9hbGxfc2NbOm5faW5pdF0sIHlfYWxsWzpuX2luaXRdLCBjbGFzc2VzPVswLCAxXSlcblxuIyBCYXRjaCBsZWFybmVyOiBSYW5kb21Gb3Jlc3QgcmVxdWlyZXMgZnVsbCByZWZpdFxucmYgPSBSYW5kb21Gb3Jlc3RDbGFzc2lmaWVyKG5fZXN0aW1hdG9ycz01MCwgcmFuZG9tX3N0YXRlPTQyKVxucmYuZml0KFhfYWxsX3NjWzpuX2luaXRdLCB5X2FsbFs6bl9pbml0XSlcblxuIyBTdHJlYW0gbmV3IGJhdGNoZXNcbmZvciBzdGFydCBpbiByYW5nZShuX2luaXQsIG5fdG90YWwsIGJhdGNoX3NpemUpOlxuICAgIGVuZCA9IHN0YXJ0ICsgYmF0Y2hfc2l6ZVxuICAgIFhfYmF0Y2gsIHlfYmF0Y2ggPSBYX2FsbF9zY1tzdGFydDplbmRdLCB5X2FsbFtzdGFydDplbmRdXG4gICAgc2dkLnBhcnRpYWxfZml0KFhfYmF0Y2gsIHlfYmF0Y2gpICAjIE8oYmF0Y2gpIHVwZGF0ZVxuICAgICMgUkY6IHdvdWxkIG5lZWQgcmYuZml0KFhfYWxsX3NjWzplbmRdLCB5X2FsbFs6ZW5kXSkg4oCUIE8obikgcmVidWlsZFxuXG5wcmludChmXHUwMDI3U0dEIG9ubGluZSBhY2N1cmFjeToge2FjY3VyYWN5X3Njb3JlKHlfYWxsW25faW5pdDpdLCBzZ2QucHJlZGljdChYX2FsbF9zY1tuX2luaXQ6XSkpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktTW9kYWw6IFRhYnVsYXIgKyBUZXh0IEZlYXR1cmUgRnVzaW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIHRhYnVsYXIgcm93cyBpbmNsdWRlIGEgZnJlZS10ZXh0IGNvbHVtbiAocHJvZHVjdCBkZXNjcmlwdGlvbiwgY3VzdG9tZXIgcmV2aWV3KSwgbmV1cmFsIG5ldHdvcmtzIGNhbiBmdXNlIHRoZSB0ZXh0IGVuY29kaW5nIHdpdGggdGFidWxhciBmZWF0dXJlcyBpbiBhIHNpbmdsZSBtb2RlbC4gVHJlZXMgcmVxdWlyZSBhIGhhbmQtY3JhZnRlZCB0ZXh0LXRvLW51bWVyaWMgcGlwZWxpbmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplciwgQXV0b01vZGVsXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuY2xhc3MgTXVsdGlNb2RhbFRhYnVsYXJUZXh0KG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiRnVzZSB0YWJ1bGFyIG51bWVyaWMgZmVhdHVyZXMgd2l0aCBCRVJUIHRleHQgZW1iZWRkaW5ncy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl90YWJ1bGFyOiBpbnQsIHRleHRfZGltOiBpbnQsIGhpZGRlbjogaW50LCBuX2NsYXNzZXM6IGludCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnRleHRfZW5jb2RlciA9IEF1dG9Nb2RlbC5mcm9tX3ByZXRyYWluZWQoXHUwMDI3ZGlzdGlsYmVydC1iYXNlLXVuY2FzZWRcdTAwMjcpXG4gICAgICAgIHNlbGYudGV4dF9wcm9qICAgID0gbm4uTGluZWFyKHRleHRfZGltLCBoaWRkZW4pXG4gICAgICAgIHNlbGYudGFiX3Byb2ogICAgID0gbm4uTGluZWFyKG5fdGFidWxhciwgaGlkZGVuKVxuICAgICAgICBzZWxmLmZ1c2lvbiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MYXllck5vcm0oaGlkZGVuICogMiksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuICogMiwgaGlkZGVuKSxcbiAgICAgICAgICAgIG5uLkdFTFUoKSxcbiAgICAgICAgICAgIG5uLkRyb3BvdXQoMC4yKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW4sIG5fY2xhc3NlcylcbiAgICAgICAgKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeF90YWI6IHRvcmNoLlRlbnNvciwgaW5wdXRfaWRzOiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgYXR0ZW50aW9uX21hc2s6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgICMgRW5jb2RlIHRleHQgd2l0aCBEaXN0aWxCRVJUXG4gICAgICAgIHRleHRfb3V0ICAgPSBzZWxmLnRleHRfZW5jb2RlcihpbnB1dF9pZHMsIGF0dGVudGlvbl9tYXNrKS5sYXN0X2hpZGRlbl9zdGF0ZVxuICAgICAgICB0ZXh0X2NscyAgID0gdGV4dF9vdXRbOiwgMF0gICAgICAgICAgICMgQ0xTIHRva2VuOiAoQiwgNzY4KVxuICAgICAgICB0ZXh0X2ZlYXQgID0gc2VsZi50ZXh0X3Byb2oodGV4dF9jbHMpICAjIChCLCBoaWRkZW4pXG4gICAgICAgICMgRW5jb2RlIHRhYnVsYXIgZmVhdHVyZXNcbiAgICAgICAgdGFiX2ZlYXQgICA9IHNlbGYudGFiX3Byb2ooeF90YWIpICAgICAgIyAoQiwgaGlkZGVuKVxuICAgICAgICAjIEZ1c2UgYW5kIGNsYXNzaWZ5XG4gICAgICAgIGZ1c2VkID0gdG9yY2guY2F0KFt0ZXh0X2ZlYXQsIHRhYl9mZWF0XSwgZGltPTEpXG4gICAgICAgIHJldHVybiBzZWxmLmZ1c2lvbihmdXNlZClcblxubW9kZWwgPSBNdWx0aU1vZGFsVGFidWxhclRleHQobl90YWJ1bGFyPTEwLCB0ZXh0X2RpbT03NjgsIGhpZGRlbj0xMjgsIG5fY2xhc3Nlcz0yKVxucHJpbnQoZlx1MDAyN1RvdGFsIHBhcmFtZXRlcnM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSk6LH1cdTAwMjcpIn0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRMIHZzIEdCTSBEZWNpc2lvbiBGcmFtZXdvcmsifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQ29uZGl0aW9uIiwiRGF0YXNldCBTaXplIiwiV2lubmVyIiwiUmVjb21tZW5kYXRpb24iXSwicm93cyI6W1siU21hbGwgdGFidWxhciwgblx1MDAzYzFrIiwiU21hbGwiLCJHQk0gLyBUYWJQRk4iLCJVc2UgVGFiUEZOIG9yIFhHQm9vc3Qgd2l0aCBIUE8iXSxbIk1lZGl1bSB0YWJ1bGFyLCBuPTFrLTEwMGsiLCJNZWRpdW0iLCJHQk0iLCJYR0Jvb3N0L0xpZ2h0R0JNIHdpdGggT3B0dW5hIHR1bmluZyJdLFsiTGFyZ2UgdGFidWxhciwgblx1MDAzZTFNIiwiTGFyZ2UiLCJDb21wZXRpdGl2ZSIsIkZULVRyYW5zZm9ybWVyIG9yIExpZ2h0R0JNOyBiZW5jaG1hcmsgYm90aCJdLFsiTXVsdGktbW9kYWwgKHRhYnVsYXIrdGV4dC9pbWFnZSkiLCJBbnkiLCJETCIsIk5ldXJhbCBmdXNpb24gbW9kZWwgcmVxdWlyZWQiXSxbIlN0cmVhbWluZyAvIG9ubGluZSB1cGRhdGVzIiwiQW55IiwiREwiLCJTR0QtYmFzZWQgTk47IHRyZWVzIG5lZWQgZnVsbCByZWJ1aWxkIl0sWyJNdWx0aS10YXNrIChzaGFyZWQgcmVwcmVzZW50YXRpb24pIiwiQW55IiwiREwiLCJTaGFyZWQgYmFja2JvbmUgTk4gd2l0aCB0YXNrLXNwZWNpZmljIGhlYWRzIl0sWyJTbW9vdGggdGFyZ2V0IGZ1bmN0aW9uIiwiQW55IiwiREwiLCJNTFAgb3IgRlQtVHJhbnNmb3JtZXI7IGxlc3MgcmVndWxhcml6YXRpb24iXSxbIk5lZWQgbmF0aXZlIGludGVycHJldGFiaWxpdHkiLCJBbnkiLCJEZXBlbmRzIiwiU0hBUCBmb3IgR0JNOyBhdHRlbnRpb24gbWFwcyBmb3IgVGFiTmV0L1NBSU5UIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiSFBPIEJ1ZGdldCBNYXR0ZXJzIiwiY29udGVudCI6IlhHQm9vc3Qgd2l0aCBkZWZhdWx0IGh5cGVycGFyYW1ldGVycyBzb21ldGltZXMgbG9zZXMgdG8gd2VsbC10dW5lZCBkZWVwIGxlYXJuaW5nLiBBbHdheXMgY29tcGFyZSB1bmRlciBlcXVhbCBIUE8gYnVkZ2V0czogaWYgeW91IHNwZW5kIDEwMCBPcHR1bmEgdHJpYWxzIG9uIFhHQm9vc3QgYW5kIDEwMCBvbiBGVC1UcmFuc2Zvcm1lciwgdGhlIERMIGdhcCBvZnRlbiBuYXJyb3dzIHNpZ25pZmljYW50bHkg4oCUIGVzcGVjaWFsbHkgb24gZGF0YXNldHMgd2l0aCBuIFx1MDAzZSAxMGsuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiREwgd2lucyBvbiBtdWx0aS1tb2RhbCBpbnB1dHMsIG9ubGluZSBsZWFybmluZywgbXVsdGktdGFzayBsZWFybmluZywgYW5kIHZlcnkgbGFyZ2UgZGF0YXNldHMiLCJUaGUgbi10aHJlc2hvbGQgZm9yIERMIGNvbXBldGl0aXZlbmVzcyBpcyByb3VnaGx5IDEway0xMDBrIGRlcGVuZGluZyBvbiBmZWF0dXJlIGNvbXBsZXhpdHkiLCJGVC1UcmFuc2Zvcm1lciBhbmQgU0FJTlQgYXJlIHRoZSBzdHJvbmdlc3QgdGFidWxhciBETCBtb2RlbHMgYXQgbGFyZ2UgbiIsIk11bHRpLXRhc2sgc2hhcmVkIGJhY2tib25lcyBhcmUgYSBuYXR1cmFsIGZpdCBmb3IgcmVsYXRlZCBwcmVkaWN0aW9uIHByb2JsZW1zIHRoYXQgR0JNIGNhbm5vdCBoYW5kbGUgam9pbnRseSIsIkFsd2F5cyBiZW5jaG1hcmsgdW5kZXIgZXF1YWwgSFBPIGVmZm9ydCDigJQgWEdCb29zdCBkZWZhdWx0IG9mdGVuIGxvc2VzIHRvIHdlbGwtdHVuZWQgREwgb24gbGFyZ2VyIGRhdGFzZXRzIl19XQ=="
---
# When Deep Learning Beats Gradient Boosting on Tabular Data

Gradient-boosted trees win on most tabular benchmarks — but not all. Neural networks have structural advantages in specific scenarios: very large datasets, multi-modal inputs, streaming data, multi-task learning, and smooth target functions. Knowing these conditions helps you choose the right tool rather than defaulting to XGBoost everywhere.

## Conditions Favoring Deep Learning

Seven conditions where DL outperforms GBM on tabular data, each rooted in a structural advantage of neural networks over decision trees:

- Very large n (>1M): tree inference is linear in n_estimators × tree depth; NN inference is O(1) in n
- Multi-modal inputs: NN handles tabular + images + text in one model; trees cannot process raw pixels or token sequences
- Smooth target functions: physical simulations, financial pricing models — NN implicit regularization fits smooth functions better
- Online/streaming learning: NN with SGD updates incrementally from new samples; trees need full rebuilds
- Multi-task learning: shared NN representations generalize across related tasks; separate trees per task don't share capacity
- Transfer learning: pre-trained tabular transformers (TabPFN, prior work) can be fine-tuned; no tree equivalent
- End-to-end systems: recommendation, ranking — NN integrates user embedding + item features + context jointly

## DL vs GBM Across Dataset Sizes

The crossover between GBM and DL accuracy depends on dataset size. Trees dominate at small n; the gap narrows as n grows. This benchmark illustrates the trend across five orders of magnitude.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import xgboost as xgb
import time

sizes = [100, 500, 1000, 5000, 10000, 50000]
results = []

for n in sizes:
    X, y = make_classification(
        n_samples=n, n_features=20, n_informative=10, random_state=42
    )
    gbm = xgb.XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.05,
                             random_state=42, eval_metric='logloss')
    mlp = Pipeline([
        ('sc', StandardScaler()),
        ('net', MLPClassifier(
            hidden_layer_sizes=(256, 128, 64), max_iter=400,
            early_stopping=True, random_state=42
        ))
    ])
    cv = max(3, min(5, n // 500))
    t0 = time.time()
    gbm_score = cross_val_score(gbm, X, y, cv=cv).mean()
    gbm_time  = time.time() - t0
    t0 = time.time()
    mlp_score = cross_val_score(mlp, X, y, cv=cv).mean()
    mlp_time  = time.time() - t0
    print(f'n={n:>6}: GBM={gbm_score:.3f}({gbm_time:.1f}s)  MLP={mlp_score:.3f}({mlp_time:.1f}s)')
```

## Multi-Task Learning with Shared Representations

Neural networks learn shared feature representations across related tasks. A single backbone trained on multiple tabular targets simultaneously often outperforms per-task trees, especially when tasks share underlying structure.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from sklearn.datasets import make_classification

class MultiTaskTabular(nn.Module):
    def __init__(self, n_features: int, hidden: int, n_tasks: int):
        super().__init__()
        # Shared encoder — learns representations useful across all tasks
        self.backbone = nn.Sequential(
            nn.Linear(n_features, hidden), nn.LayerNorm(hidden), nn.ReLU(),
            nn.Linear(hidden, hidden // 2), nn.LayerNorm(hidden // 2), nn.ReLU()
        )
        # Task-specific heads
        self.heads = nn.ModuleList([
            nn.Linear(hidden // 2, 1) for _ in range(n_tasks)
        ])

    def forward(self, x: torch.Tensor) -> list:
        shared = self.backbone(x)
        return [head(shared).squeeze(-1) for head in self.heads]

# Multi-task dataset: 3 correlated binary targets
np.random.seed(42)
X = np.random.randn(2000, 20).astype(np.float32)
y1 = (X[:, 0] + X[:, 1] > 0).astype(np.float32)
y2 = (X[:, 0] - X[:, 2] > 0).astype(np.float32)
y3 = (X[:, 1] + X[:, 3] > 0).astype(np.float32)

model  = MultiTaskTabular(n_features=20, hidden=128, n_tasks=3)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
print(f'Shared backbone params: {sum(p.numel() for p in model.backbone.parameters()):,}')
```

## Online Learning: Incremental NN vs Rebuilding Trees

For streaming data, neural networks update naturally from each new batch via SGD. Tree models require full retraining when new data arrives, making them impractical for high-velocity streams.

```python
import numpy as np
import torch
import torch.nn as nn
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

rng  = np.random.default_rng(42)
n_total, n_init, batch_size = 5000, 1000, 100

X_all = rng.standard_normal((n_total, 10)).astype(np.float32)
y_all = (X_all[:, 0] + X_all[:, 1] > 0).astype(int)

sc = StandardScaler().fit(X_all[:n_init])
X_all_sc = sc.transform(X_all)

# Online learner: SGDClassifier supports partial_fit
sgd = SGDClassifier(loss='log_loss', random_state=42)
sgd.partial_fit(X_all_sc[:n_init], y_all[:n_init], classes=[0, 1])

# Batch learner: RandomForest requires full refit
rf = RandomForestClassifier(n_estimators=50, random_state=42)
rf.fit(X_all_sc[:n_init], y_all[:n_init])

# Stream new batches
for start in range(n_init, n_total, batch_size):
    end = start + batch_size
    X_batch, y_batch = X_all_sc[start:end], y_all[start:end]
    sgd.partial_fit(X_batch, y_batch)  # O(batch) update
    # RF: would need rf.fit(X_all_sc[:end], y_all[:end]) — O(n) rebuild

print(f'SGD online accuracy: {accuracy_score(y_all[n_init:], sgd.predict(X_all_sc[n_init:])):.4f}')
```

## Multi-Modal: Tabular + Text Feature Fusion

When tabular rows include a free-text column (product description, customer review), neural networks can fuse the text encoding with tabular features in a single model. Trees require a hand-crafted text-to-numeric pipeline.

```python
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
import numpy as np

class MultiModalTabularText(nn.Module):
    """Fuse tabular numeric features with BERT text embeddings."""
    def __init__(self, n_tabular: int, text_dim: int, hidden: int, n_classes: int):
        super().__init__()
        self.text_encoder = AutoModel.from_pretrained('distilbert-base-uncased')
        self.text_proj    = nn.Linear(text_dim, hidden)
        self.tab_proj     = nn.Linear(n_tabular, hidden)
        self.fusion = nn.Sequential(
            nn.LayerNorm(hidden * 2),
            nn.Linear(hidden * 2, hidden),
            nn.GELU(),
            nn.Dropout(0.2),
            nn.Linear(hidden, n_classes)
        )

    def forward(self, x_tab: torch.Tensor, input_ids: torch.Tensor,
                attention_mask: torch.Tensor) -> torch.Tensor:
        # Encode text with DistilBERT
        text_out   = self.text_encoder(input_ids, attention_mask).last_hidden_state
        text_cls   = text_out[:, 0]           # CLS token: (B, 768)
        text_feat  = self.text_proj(text_cls)  # (B, hidden)
        # Encode tabular features
        tab_feat   = self.tab_proj(x_tab)      # (B, hidden)
        # Fuse and classify
        fused = torch.cat([text_feat, tab_feat], dim=1)
        return self.fusion(fused)

model = MultiModalTabularText(n_tabular=10, text_dim=768, hidden=128, n_classes=2)
print(f'Total parameters: {sum(p.numel() for p in model.parameters()):,}')
```

---

## DL vs GBM Decision Framework

| Condition | Dataset Size | Winner | Recommendation |
| --- | --- | --- | --- |
| Small tabular, n<1k | Small | GBM / TabPFN | Use TabPFN or XGBoost with HPO |
| Medium tabular, n=1k-100k | Medium | GBM | XGBoost/LightGBM with Optuna tuning |
| Large tabular, n>1M | Large | Competitive | FT-Transformer or LightGBM; benchmark both |
| Multi-modal (tabular+text/image) | Any | DL | Neural fusion model required |
| Streaming / online updates | Any | DL | SGD-based NN; trees need full rebuild |
| Multi-task (shared representation) | Any | DL | Shared backbone NN with task-specific heads |
| Smooth target function | Any | DL | MLP or FT-Transformer; less regularization |
| Need native interpretability | Any | Depends | SHAP for GBM; attention maps for TabNet/SAINT |

> **HPO Budget Matters**: XGBoost with default hyperparameters sometimes loses to well-tuned deep learning. Always compare under equal HPO budgets: if you spend 100 Optuna trials on XGBoost and 100 on FT-Transformer, the DL gap often narrows significantly — especially on datasets with n > 10k.

## Key Takeaways

- DL wins on multi-modal inputs, online learning, multi-task learning, and very large datasets
- The n-threshold for DL competitiveness is roughly 10k-100k depending on feature complexity
- FT-Transformer and SAINT are the strongest tabular DL models at large n
- Multi-task shared backbones are a natural fit for related prediction problems that GBM cannot handle jointly
- Always benchmark under equal HPO effort — XGBoost default often loses to well-tuned DL on larger datasets

