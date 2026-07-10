---
title: "Data-Free Knowledge Distillation — Synthesizing Proxy Data"
slug: "data-free-distillation"
description: "Data-free KD synthesises proxy training data using only the trained teacher model, enabling distillation without access to the original dataset. Covers activation maximisation, BN statistic regularisation, DAFL generator methods, CMI, privacy use cases, and the accuracy gap vs data-dependent KD."
tags: ["deep-learning", "model-compression", "knowledge-distillation", "pruning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQga25vd2xlZGdlIGRpc3RpbGxhdGlvbiByZXF1aXJlcyB0aGUgc2FtZSB0cmFpbmluZyBkYXRhIHVzZWQgdG8gdHJhaW4gdGhlIHRlYWNoZXIuIFdoZW4gdGhhdCBkYXRhIGlzIHVuYXZhaWxhYmxlIOKAlCBkdWUgdG8gcHJpdmFjeSByZWd1bGF0aW9ucywgcHJvcHJpZXRhcnkgbGljZW5zaW5nLCBvciBzaW1wbHkgYmVpbmcgZGlzY2FyZGVkIGFmdGVyIHRyYWluaW5nIOKAlCBkaXN0aWxsYXRpb24gY2Fubm90IHByb2NlZWQuIERhdGEtZnJlZSBrbm93bGVkZ2UgZGlzdGlsbGF0aW9uIChERktEKSBzb2x2ZXMgdGhpcyBieSBzeW50aGVzaXNpbmcgcHJveHkgdHJhaW5pbmcgZGF0YSB1c2luZyBvbmx5IHRoZSB0cmFpbmVkIHRlYWNoZXIgbW9kZWwgaXRzZWxmLiBUaGUgZnJvemVuIHRlYWNoZXIgYmVjb21lcyBhIHN1cGVydmlzb3J5IG9yYWNsZTogaXQgY2FuIGxhYmVsIGFueSBzeW50aGV0aWMgaW5wdXQsIGFuZCBpdHMgaW50ZXJuYWwgQmF0Y2hOb3JtIHN0YXRpc3RpY3MgcmV2ZWFsIHByb3BlcnRpZXMgb2YgdGhlIG9yaWdpbmFsIHRyYWluaW5nIGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgRGF0YSBBY2Nlc3MgUHJvYmxlbSBpbiBTdGFuZGFyZCBLRCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgS0QgdHJhbnNmZXJzIGtub3dsZWRnZSBieSBjb21wdXRpbmcgS0wgZGl2ZXJnZW5jZSBiZXR3ZWVuIHRlYWNoZXIgYW5kIHN0dWRlbnQgb3V0cHV0cyBvbiByZWFsIHRyYWluaW5nIGRhdGEuIFdpdGhvdXQgdGhpcyBkYXRhLCB0aGVyZSBhcmUgbm8gaW5wdXRzIHRvIGNvbXB1dGUgc29mdCB0YXJnZXRzIGZyb20uIERGS0QgcmVmcmFtZXMgdGhlIHByb2JsZW06IGdlbmVyYXRlIHN5bnRoZXRpYyBpbnB1dHMgdGhhdCB0aGUgdGVhY2hlciByZXNwb25kcyB0byBtZWFuaW5nZnVsbHkuIFRoZSB0ZWFjaGVyXHUwMDI3cyBCYXRjaE5vcm0gcnVubmluZyBzdGF0aXN0aWNzIOKAlCBzdG9yZWQgbWVhbnMgYW5kIHZhcmlhbmNlcyBhdCBldmVyeSBsYXllciDigJQgZW5jb2RlIGFnZ3JlZ2F0ZSBpbmZvcm1hdGlvbiBhYm91dCB0aGUgcmVhbCB0cmFpbmluZyBkaXN0cmlidXRpb24uIFRoZXNlIHN0YXRpc3RpY3MgYmVjb21lIHRoZSBhbmNob3IgZm9yIGdlbmVyYXRpbmcgcmVhbGlzdGljIHN5bnRoZXRpYyBpbWFnZXMgd2l0aG91dCBhbnkgcmVhbCBkYXRhIGFjY2Vzcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBY3RpdmF0aW9uIE1heGltaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWN0aXZhdGlvbiBtYXhpbWlzYXRpb24gaXMgdGhlIHNpbXBsZXN0IERGS0QgYXBwcm9hY2g6IG9wdGltaXNlIGEgc3ludGhldGljIGltYWdlIHogZGlyZWN0bHkgaW4gcGl4ZWwgc3BhY2UgdG8gbWF4aW1pc2UgdGhlIHRlYWNoZXJcdTAwMjdzIGNvbmZpZGVuY2UgZm9yIGEgdGFyZ2V0IGNsYXNzLiBUaGUgb2JqZWN0aXZlIGlzIHoqID0gYXJnbWF4X3ogW2xvZyBwX3RlYWNoZXIoeT1jfHopXS4gV2l0aG91dCByZWd1bGFyaXNhdGlvbiwgdGhpcyBwcm9kdWNlcyBhZHZlcnNhcmlhbC1saWtlIGltYWdlcyDigJQgaGlnaC1mcmVxdWVuY3kgcGF0dGVybnMgdGhhdCBtYXhpbWlzZSBuZXVyb24gYWN0aXZhdGlvbnMgYnV0IGxvb2sgbm90aGluZyBsaWtlIHJlYWwgZGF0YS4gQmF0Y2hOb3JtIHN0YXRpc3RpY3MgbWF0Y2hpbmcgaXMgdGhlIGtleSByZWd1bGFyaXNlcjogcGVuYWxpc2Ugc3ludGhldGljIGltYWdlcyB3aG9zZSBpbnRlcm1lZGlhdGUgYWN0aXZhdGlvbnMgZGV2aWF0ZSBmcm9tIHRoZSB0ZWFjaGVyXHUwMDI3cyBzdG9yZWQgcnVubmluZyBzdGF0aXN0aWNzLiBUaGlzIGZvcmNlcyBnZW5lcmF0ZWQgaW1hZ2VzIHRvIHByb2R1Y2UgcmVhbGlzdGljIGludGVybmFsIHJlcHJlc2VudGF0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuXG5kZWYgYWN0aXZhdGlvbl9tYXhpbWl6YXRpb24odGVhY2hlcjogbm4uTW9kdWxlLCB0YXJnZXRfY2xhc3M6IGludCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9zdGVwczogaW50ID0gMzAwLCBscjogZmxvYXQgPSAwLjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJuX3JlZzogZmxvYXQgPSAwLjAwMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaW1nX3NoYXBlOiB0dXBsZSA9ICgxLCAzLCAzMiwgMzIpKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJTeW50aGVzaXNlIGltYWdlIGJ5IG1heGltaXNpbmcgdGVhY2hlciBjbGFzcyBwcm9iYWJpbGl0eSArIEJOIHJlZ3VsYXJpc2F0aW9uLlwiXCJcIlxuICAgIHRlYWNoZXIuZXZhbCgpXG4gICAgeiA9IHRvcmNoLnJhbmRuKCppbWdfc2hhcGUsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbiAgICBvcHRpbWl6ZXIgPSBvcHRpbS5BZGFtKFt6XSwgbHI9bHIpXG4gICAgYm5faG9va3MgPSBbXVxuICAgIGZvciBtb2R1bGUgaW4gdGVhY2hlci5tb2R1bGVzKCk6XG4gICAgICAgIGlmIGlzaW5zdGFuY2UobW9kdWxlLCBubi5CYXRjaE5vcm0yZCk6XG4gICAgICAgICAgICBtdSAgPSBtb2R1bGUucnVubmluZ19tZWFuLmRldGFjaCgpXG4gICAgICAgICAgICB2YXIgPSBtb2R1bGUucnVubmluZ192YXIuZGV0YWNoKClcbiAgICAgICAgICAgIGRlZiBtYWtlX2hvb2sodGFyZ2V0X211LCB0YXJnZXRfdmFyKTpcbiAgICAgICAgICAgICAgICBkZWYgaG9vayhtLCBpbnAsIG91dCk6XG4gICAgICAgICAgICAgICAgICAgIG0uX2JuX2xvc3MgPSAoRi5tc2VfbG9zcyhvdXQubWVhbigoMCwgMiwgMykpLCB0YXJnZXRfbXUpICtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBGLm1zZV9sb3NzKG91dC52YXIoKDAsIDIsIDMpKSwgIHRhcmdldF92YXIpKVxuICAgICAgICAgICAgICAgIHJldHVybiBob29rXG4gICAgICAgICAgICBibl9ob29rcy5hcHBlbmQobW9kdWxlLnJlZ2lzdGVyX2ZvcndhcmRfaG9vayhtYWtlX2hvb2sobXUsIHZhcikpKVxuICAgIGZvciBzdGVwIGluIHJhbmdlKG5fc3RlcHMpOlxuICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgb3V0ID0gdGVhY2hlcih6KVxuICAgICAgICBjbHNfbG9zcyA9IC1GLmxvZ19zb2Z0bWF4KG91dCwgZGltPS0xKVswLCB0YXJnZXRfY2xhc3NdXG4gICAgICAgIGJuX2xvc3MgID0gc3VtKG0uX2JuX2xvc3MgZm9yIG0gaW4gdGVhY2hlci5tb2R1bGVzKClcbiAgICAgICAgICAgICAgICAgICAgICAgaWYgaXNpbnN0YW5jZShtLCBubi5CYXRjaE5vcm0yZCkgYW5kIGhhc2F0dHIobSwgXHUwMDI3X2JuX2xvc3NcdTAwMjcpKVxuICAgICAgICAoY2xzX2xvc3MgKyBibl9yZWcgKiBibl9sb3NzKS5iYWNrd2FyZCgpXG4gICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICBmb3IgaCBpbiBibl9ob29rczpcbiAgICAgICAgaC5yZW1vdmUoKVxuICAgIHJldHVybiB6LmRldGFjaCgpXG5cbnByaW50KFx1MDAyN0FjdGl2YXRpb24gbWF4aW1pc2F0aW9uIHN5bnRoZXNpc2VzIGNsYXNzLWNvbmRpdGlvbmFsIGltYWdlcyBmcm9tIHRlYWNoZXIgb25seS5cdTAwMjcpXG5wcmludChcdTAwMjdCTiByZWd1bGFyaXNhdGlvbiBlbnN1cmVzIGdlbmVyYXRlZCBpbWFnZXMgaGF2ZSByZWFsaXN0aWMgYWN0aXZhdGlvbiBzdGF0aXN0aWNzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCYXRjaE5vcm0gU3RhdGlzdGljIFJlZ3VsYXJpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFdmVyeSBCYXRjaE5vcm0yZCBsYXllciBzdG9yZXMgcnVubmluZ19tZWFuIGFuZCBydW5uaW5nX3ZhciBjb21wdXRlZCBvdmVyIHRoZSB0cmFpbmluZyBkYXRhIGR1cmluZyB0cmFpbmluZy4gRm9yIGEgc3ludGhldGljIGltYWdlIHRvIHByb2R1Y2UgcmVhbGlzdGljIGludGVybWVkaWF0ZSBhY3RpdmF0aW9ucywgaXRzIGFjdGl2YXRpb25zIGF0IGVhY2ggQk4gbGF5ZXIgc2hvdWxkIG1hdGNoIHRoZXNlIHN0b3JlZCBzdGF0aXN0aWNzLiBUaGUgQk4gc3RhdGlzdGljcyBsb3NzIGlzOiBMX0JOID0gc3VtX2wgW01TRShtZWFuX2dlbmVyYXRlZF9sLCBtZWFuX3J1bm5pbmdfbCkgKyBNU0UodmFyX2dlbmVyYXRlZF9sLCB2YXJfcnVubmluZ19sKV0uIFRoaXMgbG9zcyBpcyBkaWZmZXJlbnRpYWJsZSB3aXRoIHJlc3BlY3QgdG8gdGhlIGlucHV0IGltYWdlIHogYW5kIGNhbiBiZSBiYWNrcHJvcGFnYXRlZCB0aHJvdWdoIHRoZSBmcm96ZW4gdGVhY2hlciB0byBzaGFwZSB0aGUgZ2VuZXJhdGVkIGltYWdlLiBCTiBtYXRjaGluZyBpcyB3aGF0IGRpc3Rpbmd1aXNoZXMgZ29vZCBERktEIGZyb20gbmFpdmUgYWN0aXZhdGlvbiBtYXhpbWlzYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHR5cGluZyBpbXBvcnQgTGlzdCwgVHVwbGVcblxuZGVmIGdldF90ZWFjaGVyX2JuX3N0YXRzKHRlYWNoZXI6IG5uLk1vZHVsZSkgLVx1MDAzZSBMaXN0W1R1cGxlW3RvcmNoLlRlbnNvciwgdG9yY2guVGVuc29yXV06XG4gICAgXCJcIlwiUmV0dXJuIChydW5uaW5nX21lYW4sIHJ1bm5pbmdfdmFyKSBmb3IgZXZlcnkgQmF0Y2hOb3JtMmQgaW4gdGVhY2hlci5cIlwiXCJcbiAgICByZXR1cm4gWyhtLnJ1bm5pbmdfbWVhbi5kZXRhY2goKS5jbG9uZSgpLCBtLnJ1bm5pbmdfdmFyLmRldGFjaCgpLmNsb25lKCkpXG4gICAgICAgICAgICBmb3IgbSBpbiB0ZWFjaGVyLm1vZHVsZXMoKSBpZiBpc2luc3RhbmNlKG0sIG5uLkJhdGNoTm9ybTJkKV1cblxuZGVmIGJuX3N0YXRfbWF0Y2hpbmdfbG9zcyh0ZWFjaGVyOiBubi5Nb2R1bGUsIHg6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHRhcmdldF9zdGF0czogTGlzdFtUdXBsZVt0b3JjaC5UZW5zb3IsIHRvcmNoLlRlbnNvcl1dKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJQZW5hbGlzZSBtaXNtYXRjaCBiZXR3ZWVuIHhcdTAwMjdzIEJOIGFjdGl2YXRpb24gc3RhdHMgYW5kIHRlYWNoZXJcdTAwMjdzIHN0b3JlZCBzdGF0cy5cIlwiXCJcbiAgICBsb3NzZXMsIGhvb2tzID0gW10sIFtdXG4gICAgYm5fbW9kdWxlcyA9IFttIGZvciBtIGluIHRlYWNoZXIubW9kdWxlcygpIGlmIGlzaW5zdGFuY2UobSwgbm4uQmF0Y2hOb3JtMmQpXVxuICAgIGZvciBpLCBtb2R1bGUgaW4gZW51bWVyYXRlKGJuX21vZHVsZXMpOlxuICAgICAgICB0X21lYW4sIHRfdmFyID0gdGFyZ2V0X3N0YXRzW2ldXG4gICAgICAgIGRlZiBtYWtlX2hvb2sodG0sIHR2KTpcbiAgICAgICAgICAgIGRlZiBob29rKG0sIGlucCwgb3V0KTpcbiAgICAgICAgICAgICAgICBsb3NzZXMuYXBwZW5kKEYubXNlX2xvc3Mob3V0Lm1lYW4oKDAsIDIsIDMpKSwgdG0pICtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBGLm1zZV9sb3NzKG91dC52YXIoKDAsIDIsIDMpKSwgIHR2KSlcbiAgICAgICAgICAgIHJldHVybiBob29rXG4gICAgICAgIGhvb2tzLmFwcGVuZChtb2R1bGUucmVnaXN0ZXJfZm9yd2FyZF9ob29rKG1ha2VfaG9vayh0X21lYW4sIHRfdmFyKSkpXG4gICAgdGVhY2hlci5ldmFsKClcbiAgICBfID0gdGVhY2hlcih4KVxuICAgIGZvciBoIGluIGhvb2tzOlxuICAgICAgICBoLnJlbW92ZSgpXG4gICAgcmV0dXJuIHRvcmNoLnN0YWNrKGxvc3NlcykubWVhbigpIGlmIGxvc3NlcyBlbHNlIHgubmV3X3RlbnNvcigwLjApXG5cbnRlYWNoZXIgPSBubi5TZXF1ZW50aWFsKG5uLkNvbnYyZCgzLCAxNiwgMywgcGFkZGluZz0xKSwgbm4uQmF0Y2hOb3JtMmQoMTYpLCBubi5SZUxVKCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgbm4uQ29udjJkKDE2LCA4LCAzLCBwYWRkaW5nPTEpLCBubi5CYXRjaE5vcm0yZCg4KSwgbm4uUmVMVSgpKVxucmVhbF9zdGF0cyA9IGdldF90ZWFjaGVyX2JuX3N0YXRzKHRlYWNoZXIpXG5nZW5faW1hZ2UgID0gdG9yY2gucmFuZG4oNCwgMywgMzIsIDMyLCByZXF1aXJlc19ncmFkPVRydWUpXG5sb3NzID0gYm5fc3RhdF9tYXRjaGluZ19sb3NzKHRlYWNoZXIsIGdlbl9pbWFnZSwgcmVhbF9zdGF0cylcbnByaW50KGZcdTAwMjdCTiBzdGF0IG1hdGNoaW5nIGxvc3MgKHJhbmRvbSBpbWFnZSk6IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3TWluaW1pc2luZyB0aGlzIGxvc3MgZHVyaW5nIHN5bnRoZXNpcyB5aWVsZHMgcmVhbGlzdGljIGludGVybmFsIGFjdGl2YXRpb25zLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHZW5lcmF0b3ItQmFzZWQgTWV0aG9kcyDigJQgREFGTCBhbmQgQ01JIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEQUZMIChEYXRhLUZyZWUgTGVhcm5pbmcgb2YgU3R1ZGVudCBOZXR3b3JrcywgQ2hlbiBldCBhbC4gMjAxOSkgcmVwbGFjZXMgcGVyLWltYWdlIG9wdGltaXNhdGlvbiB3aXRoIGEgbGVhcm5lZCBnZW5lcmF0b3IgRy4gRyB0YWtlcyBhIG5vaXNlIHZlY3RvciB6IGFuZCBwcm9kdWNlcyBzeW50aGV0aWMgaW1hZ2VzIHhfZ2VuID0gRyh6KS4gRyBpcyB0cmFpbmVkIGFkdmVyc2FyaWFsbHk6IHByb2R1Y2UgaW1hZ2VzIHRoYXQgbWF4aW1pc2UgdGVhY2hlciBjb25maWRlbmNlIGFuZCBhY3RpdmF0aW9uIG1hZ25pdHVkZXMgd2hpbGUgbWFpbnRhaW5pbmcgZGl2ZXJzaXR5LiBUaGUgc3R1ZGVudCBTIGlzIHNpbXVsdGFuZW91c2x5IHRyYWluZWQgdG8gbWF0Y2ggdGVhY2hlciBvdXRwdXRzIG9uIGdlbmVyYXRlZCBkYXRhLiBDTUkgKENvbnRyYXN0aXZlIE1vZGVsIEludmVyc2lvbiwgRmFuZyBldCBhbC4gMjAyMikgaW1wcm92ZXMgZGl2ZXJzaXR5IGJ5IGFkZGluZyBhIGNvbnRyYXN0aXZlIGxvc3MgdGhhdCBlbmNvdXJhZ2VzIGRpZmZlcmVudCBzYW1wbGVzIHRvIHByb2R1Y2UgZGlzdGluY3QgYWN0aXZhdGlvbiBwYXR0ZXJucywgcmVkdWNpbmcgbW9kZSBjb2xsYXBzZSBpbiB0aGUgZ2VuZXJhdGVkIGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBEYXRhRnJlZUdlbmVyYXRvcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB6X2RpbT0xMDAsIGNoYW5uZWxzPTMsIHNpemU9MzIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKHpfZGltLCA1MTIpLCBubi5CYXRjaE5vcm0xZCg1MTIpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoNTEyLCBjaGFubmVscyAqIHNpemUgKiBzaXplKSwgbm4uVGFuaCgpKVxuICAgICAgICBzZWxmLm91dF9zaGFwZSA9IChjaGFubmVscywgc2l6ZSwgc2l6ZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHopOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeikudmlldyh6LnNpemUoMCksICpzZWxmLm91dF9zaGFwZSlcblxuZGVmIHRyYWluX2Rma2QodGVhY2hlciwgc3R1ZGVudCwgZ2VuZXJhdG9yLCBuX3N0ZXBzPTEwMCwgel9kaW09MTAwLCBCPTMyLCBUPTQuMCk6XG4gICAgXCJcIlwiRGF0YS1mcmVlIEtEOiBqb2ludGx5IHRyYWluIGdlbmVyYXRvciArIHN0dWRlbnQgdXNpbmcgZnJvemVuIHRlYWNoZXIuXCJcIlwiXG4gICAgdGVhY2hlci5ldmFsKClcbiAgICBvcHRfZyA9IG9wdGltLkFkYW0oZ2VuZXJhdG9yLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBvcHRfcyA9IG9wdGltLkFkYW0oc3R1ZGVudC5wYXJhbWV0ZXJzKCksICAgbHI9MWUtMylcbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgeiA9IHRvcmNoLnJhbmRuKEIsIHpfZGltKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIHNvZnQgPSBGLnNvZnRtYXgodGVhY2hlcihnZW5lcmF0b3IoeikpIC8gVCwgZGltPS0xKVxuICAgICAgICBvcHRfcy56ZXJvX2dyYWQoKVxuICAgICAgICBrZCA9IEYua2xfZGl2KEYubG9nX3NvZnRtYXgoc3R1ZGVudChnZW5lcmF0b3IoeikuZGV0YWNoKCkpIC8gVCwgZGltPS0xKSxcbiAgICAgICAgICAgICAgICAgICAgICAgc29mdCwgcmVkdWN0aW9uPVx1MDAyN2JhdGNobWVhblx1MDAyNykgKiBUICoqIDJcbiAgICAgICAga2QuYmFja3dhcmQoKTsgb3B0X3Muc3RlcCgpXG4gICAgICAgIG9wdF9nLnplcm9fZ3JhZCgpXG4gICAgICAgIGdfbG9zcyA9IC10ZWFjaGVyKGdlbmVyYXRvcih0b3JjaC5yYW5kbihCLCB6X2RpbSkpKS5zb2Z0bWF4KC0xKS5tYXgoLTEpLnZhbHVlcy5tZWFuKClcbiAgICAgICAgZ19sb3NzLmJhY2t3YXJkKCk7IG9wdF9nLnN0ZXAoKVxuICAgICAgICBpZiAoc3RlcCArIDEpICUgMjUgPT0gMDpcbiAgICAgICAgICAgIHByaW50KGZcdTAwMjdTdGVwIHtzdGVwKzF9OiBLRD17a2QuaXRlbSgpOi4zZn0gIEc9e2dfbG9zcy5pdGVtKCk6LjNmfVx1MDAyNylcblxudGVhY2hlciA9IG5uLlNlcXVlbnRpYWwobm4uRmxhdHRlbigpLCBubi5MaW5lYXIoMzA3MiwgMTApKVxuc3R1ZGVudCA9IG5uLlNlcXVlbnRpYWwobm4uRmxhdHRlbigpLCBubi5MaW5lYXIoMzA3MiwgMTApKVxuZ2VuID0gRGF0YUZyZWVHZW5lcmF0b3IoKVxudHJhaW5fZGZrZCh0ZWFjaGVyLCBzdHVkZW50LCBnZW4sIG5fc3RlcHM9NTApIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJpdmFjeSBhbmQgR0RQUiBVc2UgQ2FzZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9uZSBjb21wZWxsaW5nIG1vdGl2YXRpb24gZm9yIERGS0QgaXMgcHJpdmFjeSBwcmVzZXJ2YXRpb24uIFRyYWluaW5nIGRhdGEgb2Z0ZW4gY29udGFpbnMgcGVyc29uYWwgaW5mb3JtYXRpb24g4oCUIG1lZGljYWwgcmVjb3JkcywgdXNlciBjb21tdW5pY2F0aW9ucywgcHJpdmF0ZSBpbWFnZXMg4oCUIHRoYXQgY2Fubm90IGJlIHNoYXJlZCBvciBzdG9yZWQgYWZ0ZXIgdHJhaW5pbmcgdW5kZXIgR0RQUiBBcnRpY2xlIDE3IChyaWdodCB0byBlcmFzdXJlKS4gT25jZSBhIG1vZGVsIGlzIHRyYWluZWQsIHRoZSBvcmlnaW5hbCBkYXRhIGNhbiBiZSBsZWdhbGx5IGRlbGV0ZWQsIGxlYXZpbmcgb25seSB0aGUgbW9kZWwgd2VpZ2h0cy4gREZLRCBhbGxvd3Mga25vd2xlZGdlIHRyYW5zZmVyIGZyb20gdGhlIGZyb3plbiB0ZWFjaGVyIHRvIGEgc21hbGxlciBzdHVkZW50IHdpdGhvdXQgZXZlciBhY2Nlc3NpbmcgdGhlIGRlbGV0ZWQgZGF0YSwgZW5hYmxpbmcgbW9kZWwgY29tcHJlc3Npb24gYW5kIGRlcGxveW1lbnQgb3B0aW1pc2F0aW9uIHdoaWxlIG1haW50YWluaW5nIGZ1bGwgcmVndWxhdG9yeSBjb21wbGlhbmNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFjY3VyYWN5IEdhcCB2cyBEYXRhLURlcGVuZGVudCBLRCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGF0YS1mcmVlIEtEIGNvbnNpc3RlbnRseSB1bmRlcnBlcmZvcm1zIGRhdGEtZGVwZW5kZW50IEtELiBBdCBsb3cgY29tcHJlc3Npb24gKHJldGFpbmluZyBcdTAwM2U3NSUgb2YgdGVhY2hlciBwYXJhbWV0ZXJzKSwgdGhlIGdhcCBpcyAxLTIlLiBBdCBhZ2dyZXNzaXZlIGNvbXByZXNzaW9uIChcdTAwM2MyNSUgb2YgcGFyYW1ldGVycyksIHRoZSBnYXAgd2lkZW5zIHRvIDQtOCUuIENNSSBhY2hpZXZlcyB0aGUgc21hbGxlc3QgZ2FwIGJ5IG1heGltaXNpbmcgbXV0dWFsIGluZm9ybWF0aW9uIGJldHdlZW4gZ2VuZXJhdGVkIHNhbXBsZXMuIFRoZSBmdW5kYW1lbnRhbCBib3R0bGVuZWNrIGlzIGRpc3RyaWJ1dGlvbiBzaGlmdDogZXZlbiB0aGUgYmVzdCBnZW5lcmF0b3JzIGRvIG5vdCBwZXJmZWN0bHkgcmVwbGljYXRlIHRoZSB0cmFpbmluZyBkaXN0cmlidXRpb24sIHNvIHRoZSBzdHVkZW50IHNlZXMgYSBzbGlnaHRseSBkaWZmZXJlbnQgZGlzdHJpYnV0aW9uIHRoYW4gdGhlIHRlYWNoZXIgd2FzIG9wdGltaXNlZCBmb3IuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG4jIEFjY3VyYWN5IGNvbXBhcmlzb246IGRhdGEtZnJlZSBLRCBtZXRob2RzIHZzIGRhdGEtZGVwZW5kZW50IEtEIG9uIENJRkFSLTEwMFxuIyBUZWFjaGVyOiBSZXNOZXQtMzQgKDc3LjglKSwgU3R1ZGVudDogUmVzTmV0LTE4IGZhbWlseSBhdCB2YXJpb3VzIGNvbXByZXNzaW9uc1xuY29tcHJlc3Npb25fcGN0ID0gWzEwMCwgNzUsIDUwLCAyNSwgMTBdICAjIHN0dWRlbnQgcGFyYW0gJSByZWxhdGl2ZSB0byB0ZWFjaGVyXG5cbmRhdGFfZGVwZW5kZW50ID0gWzc3LjgsIDc2LjQsIDc1LjEsIDcxLjMsIDYzLjJdICAjIHN0YW5kYXJkIEtEIHdpdGggcmVhbCBkYXRhXG5kZmtkX2RhZmwgICAgICA9IFs3Ny44LCA3My44LCA3Mi4xLCA2Ny40LCA1OC4xXSAgIyBEQUZMIChDaGVuIGV0IGFsLiAyMDE5KVxuZGZrZF9jbWkgICAgICAgPSBbNzcuOCwgNzQuOSwgNzMuMiwgNjkuMSwgNjAuOF0gICMgQ01JICAoRmFuZyBldCBhbC4gMjAyMilcbmRma2RfemVyb3Nob3QgID0gWzc3LjgsIDcyLjEsIDcwLjQsIDY1LjIsIDU1LjddICAjIFplcm8tc2hvdCBLRCAoTmF5YWsgMjAxOSlcblxucHJpbnQoZlx1MDAyN3tcIkNvbXByZXNzaW9uXCI6XHUwMDNlMTJ9ICB7XCJEYXRhLURlcFwiOlx1MDAzZTl9ICB7XCJEQUZMXCI6XHUwMDNlN30gIHtcIkNNSVwiOlx1MDAzZTd9ICB7XCJaZXJvU2hvdFwiOlx1MDAzZTl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN3tcIiglIHBhcmFtcylcIjpcdTAwM2UxMn0gIHtcIihyZWFsKVwiOiBcdTAwM2U5fSAge1wiKERGS0QpXCI6XHUwMDNlN30gIHtcIihERktEKVwiOlx1MDAzZTd9ICB7XCIoREZLRClcIjpcdTAwM2U5fVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA1NSlcbmZvciBjLCBkZCwgZGEsIGNtLCB6cyBpbiB6aXAoY29tcHJlc3Npb25fcGN0LCBkYXRhX2RlcGVuZGVudCwgZGZrZF9kYWZsLCBkZmtkX2NtaSwgZGZrZF96ZXJvc2hvdCk6XG4gICAgcHJpbnQoZlx1MDAyN3tjOlx1MDAzZTExfSUgIHtkZDpcdTAwM2U5LjFmfSAge2RhOlx1MDAzZTcuMWZ9ICB7Y206XHUwMDNlNy4xZn0gIHt6czpcdTAwM2U5LjFmfVx1MDAyNylcblxuZ2Fwc19kYWZsID0gW2RkIC0gZGEgZm9yIGRkLCBkYSBpbiB6aXAoZGF0YV9kZXBlbmRlbnQsIGRma2RfZGFmbCldXG5nYXBzX2NtaSAgPSBbZGQgLSBjbSBmb3IgZGQsIGNtIGluIHppcChkYXRhX2RlcGVuZGVudCwgZGZrZF9jbWkpXVxucHJpbnQoZlx1MDAyN1xcbk1lYW4gYWNjdXJhY3kgZ2FwIOKAlCBEQUZMOiB7bnAubWVhbihnYXBzX2RhZmwpOi4xZn0lICBDTUk6IHtucC5tZWFuKGdhcHNfY21pKTouMWZ9JVx1MDAyNylcbnByaW50KGZcdTAwMjdUeXBpY2FsIGRhdGEtZnJlZSBxdWFsaXR5IGdhcDogMi01JSB2cyBkYXRhLWRlcGVuZGVudCBLRC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmFzdC1ERktEIGFuZCBBbW9ydGl6ZWQgR2VuZXJhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmFzdC1ERktEIChGYW5nIGV0IGFsLiAyMDIxKSByZWR1Y2VzIHRoZSBjb21wdXRhdGlvbmFsIGNvc3Qgb2YgREZLRCB0aHJvdWdoIG1ldGEtbGVhcm5pbmcuIFJhdGhlciB0aGFuIHRyYWluaW5nIGEgbmV3IGdlbmVyYXRvciBmcm9tIHNjcmF0Y2ggZm9yIGVhY2ggdGVhY2hlciBtb2RlbCwgRmFzdC1ERktEIG1ldGEtbGVhcm5zIGEgZ2VuZXJhdG9yIGluaXRpYWxpc2F0aW9uIHRoYXQgYWRhcHRzIHF1aWNrbHkgdG8gYW55IHRlYWNoZXIgd2l0aCBvbmx5IGEgZmV3IGdyYWRpZW50IHN0ZXBzLiBUaGUgbWV0YS1sZWFybmVkIGluaXRpYWxpc2F0aW9uIGNhcHR1cmVzIGdlbmVyYWwgdmlzdWFsIHByaW9ycyAoZWRnZXMsIHRleHR1cmVzLCBzaGFwZXMpIHRoYXQgYXJlIHVzZWZ1bCBmb3IgYW55IGNsYXNzaWZpY2F0aW9uIHRlYWNoZXIsIHJlcXVpcmluZyBvbmx5IHRhc2stc3BlY2lmaWMgZmluZS10dW5pbmcuIFplcm8tc2hvdCBLRCAoTmF5YWsgZXQgYWwuIDIwMTkpIGlzIGFub3RoZXIgZmFzdCBhcHByb2FjaDogaXQgc2FtcGxlcyBmcm9tIGEgRGlyaWNobGV0IGRpc3RyaWJ1dGlvbiBjb25kaXRpb25lZCBvbiB0aGUgdGVhY2hlclx1MDAyN3MgY2xhc3Mgc3RhdGlzdGljcywgYnlwYXNzaW5nIG5ldXJhbCBzeW50aGVzaXMgZW50aXJlbHkgYXQgbG93ZXIgYWNjdXJhY3kuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJEYXRhLUZyZWUgS0QgQ2Fubm90IEZ1bGx5IFJlY292ZXIgRGF0YS1EZXBlbmRlbnQgS0QgQWNjdXJhY3kiLCJjb250ZW50IjoiVGhlIDItNSUgYWNjdXJhY3kgZ2FwIGJldHdlZW4gZGF0YS1mcmVlIGFuZCBkYXRhLWRlcGVuZGVudCBLRCBpcyBhIGZ1bmRhbWVudGFsIGluZm9ybWF0aW9uLXRoZW9yZXRpYyBsaW1pdGF0aW9uLiBUaGUgdGVhY2hlciB3ZWlnaHRzIGVuY29kZSBpbmZvcm1hdGlvbiBhYm91dCB0cmFpbmluZyBkYXRhLCBidXQgbm90IGFsbCBvZiBpdC4gR2VuZXJhdGVkIGltYWdlcyBjYW4gbWF0Y2ggQk4gc3RhdGlzdGljcyBnbG9iYWxseSBidXQgbm90IGNhcHR1cmUgcmFyZSBleGFtcGxlcywgY2xhc3MgYm91bmRhcmllcywgb3IgZG9tYWluLXNwZWNpZmljIHBhdHRlcm5zLiBJZiBhY2N1cmFjeSByZWNvdmVyeSBpcyBjcml0aWNhbCwgY29uc2lkZXIgdXNpbmcgZXZlbiBhIHNtYWxsIGFtb3VudCBvZiByZWFsIGRhdGEg4oCUIDEwMCBzYW1wbGVzIHBlciBjbGFzcyDigJQgdG8gYW5jaG9yIHRoZSBzeW50aGVzaXMuIFRoaXMgZHJhbWF0aWNhbGx5IGNsb3NlcyB0aGUgZ2FwIGF0IG1pbmltYWwgcHJpdmFjeSBjb3N0LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJEYXRhIFJlcXVpcmVkIiwiR2VuZXJhdG9yIFR5cGUiLCJBY2N1cmFjeSB2cyBSZWFsIEtEIiwiUHJpdmFjeSBTYWZlIiwiVHJhaW5pbmcgQ29zdCJdLCJyb3dzIjpbWyJBY3RpdmF0aW9uIG1heGltaXNhdGlvbiIsIk5vbmUiLCJQZXItaW1hZ2Ugb3B0aW1pc2F0aW9uIiwiLTQgdG8gLTglIiwiWWVzIiwiSGlnaCAocGVyLWltYWdlIG9wdCkiXSxbIkRBRkwgKENoZW4gMjAxOSkiLCJOb25lIiwiR0FOIGdlbmVyYXRvciIsIi0zIHRvIC01JSIsIlllcyIsIk1lZGl1bSAodHJhaW4gRyBvbmNlKSJdLFsiQ01JIChGYW5nIDIwMjIpIiwiTm9uZSIsIkdBTiArIGNvbnRyYXN0aXZlIiwiLTIgdG8gLTQlIiwiWWVzIiwiTWVkaXVtIl0sWyJaZXJvLXNob3QgS0QgKE5heWFrIDIwMTkpIiwiTm9uZSIsIkRpcmljaGxldCBzYW1wbGluZyIsIi00IHRvIC03JSIsIlllcyIsIkxvdyAobm8gZ2VuZXJhdG9yKSJdLFsiRmFzdC1ERktEIiwiTm9uZSIsIk1ldGEtbGVhcm5lZCBnZW5lcmF0b3IiLCItMyB0byAtNSUiLCJZZXMiLCJMb3cgKGZhc3QgYWRhcHRhdGlvbikiXSxbIkRhdGEtZGVwZW5kZW50IEtEIiwiRnVsbCB0cmFpbmluZyBzZXQiLCJSZWFsIGRhdGEiLCJCYXNlbGluZSIsIk5vIiwiTG93IChubyBnZW5lcmF0b3IpIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJOIHN0YXRpc3RpYyBtYXRjaGluZyBpcyB0aGUga2V5IHJlZ3VsYXJpc2VyOiB3aXRob3V0IGl0LCBnZW5lcmF0ZWQgaW1hZ2VzIGFyZSBhZHZlcnNhcmlhbC1saWtlIG5vaXNlLiIsIlRlbXBlcmF0dXJlIGZvciBERktEIGdlbmVyYXRvciB0cmFpbmluZzogdXNlIFQ9MjAgKHZlcnkgc29mdCkgdG8gbWF4aW1pc2UgZ3JhZGllbnQgc2lnbmFsLiIsIkdlbmVyYXRvciBkaXZlcnNpdHk6IGNvbmRpdGlvbiBHIG9uIG9uZS1ob3QgY2xhc3MgbGFiZWxzIGZvciBjbGFzcy1jb25kaXRpb25hbCBpbWFnZSBzeW50aGVzaXMuIiwiREFGTCBvYmplY3RpdmU6IG1heGltaXNlIHRlYWNoZXIgY29uZmlkZW5jZSArIGFjdGl2YXRpb24gbWFnbml0dWRlICsgc2FtcGxlIGRpdmVyc2l0eSAodGhyZWUgdGVybXMpLiIsIkdEUFIgY29tcGxpYW5jZTogREZLRCBhbGxvd3MgbGVnYWwgbW9kZWwgY29tcHJlc3Npb24gd2hlbiB0cmFpbmluZyBkYXRhIG11c3QgYmUgZGVsZXRlZCBwb3N0LXRyYWluaW5nLiIsIlF1YWxpdHkgZ2FwIGNsb3NlcyB3aXRoIGRhdGE6IDEwMCByZWFsIHNhbXBsZXMgcGVyIGNsYXNzIHJlZHVjZXMgdGhlIGdhcCBieSB+NTAlIHZzIGZ1bGx5IGRhdGEtZnJlZS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Data-Free Knowledge Distillation — Synthesizing Proxy Data

Standard knowledge distillation requires the same training data used to train the teacher. When that data is unavailable — due to privacy regulations, proprietary licensing, or simply being discarded after training — distillation cannot proceed. Data-free knowledge distillation (DFKD) solves this by synthesising proxy training data using only the trained teacher model itself. The frozen teacher becomes a supervisory oracle: it can label any synthetic input, and its internal BatchNorm statistics reveal properties of the original training distribution.

## The Data Access Problem in Standard KD

Standard KD transfers knowledge by computing KL divergence between teacher and student outputs on real training data. Without this data, there are no inputs to compute soft targets from. DFKD reframes the problem: generate synthetic inputs that the teacher responds to meaningfully. The teacher's BatchNorm running statistics — stored means and variances at every layer — encode aggregate information about the real training distribution. These statistics become the anchor for generating realistic synthetic images without any real data access.

## Activation Maximization

Activation maximisation is the simplest DFKD approach: optimise a synthetic image z directly in pixel space to maximise the teacher's confidence for a target class. The objective is z* = argmax_z [log p_teacher(y=c|z)]. Without regularisation, this produces adversarial-like images — high-frequency patterns that maximise neuron activations but look nothing like real data. BatchNorm statistics matching is the key regulariser: penalise synthetic images whose intermediate activations deviate from the teacher's stored running statistics. This forces generated images to produce realistic internal representations.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

def activation_maximization(teacher: nn.Module, target_class: int,
                             n_steps: int = 300, lr: float = 0.1,
                             bn_reg: float = 0.001,
                             img_shape: tuple = (1, 3, 32, 32)) -> torch.Tensor:
    """Synthesise image by maximising teacher class probability + BN regularisation."""
    teacher.eval()
    z = torch.randn(*img_shape, requires_grad=True)
    optimizer = optim.Adam([z], lr=lr)
    bn_hooks = []
    for module in teacher.modules():
        if isinstance(module, nn.BatchNorm2d):
            mu  = module.running_mean.detach()
            var = module.running_var.detach()
            def make_hook(target_mu, target_var):
                def hook(m, inp, out):
                    m._bn_loss = (F.mse_loss(out.mean((0, 2, 3)), target_mu) +
                                  F.mse_loss(out.var((0, 2, 3)),  target_var))
                return hook
            bn_hooks.append(module.register_forward_hook(make_hook(mu, var)))
    for step in range(n_steps):
        optimizer.zero_grad()
        out = teacher(z)
        cls_loss = -F.log_softmax(out, dim=-1)[0, target_class]
        bn_loss  = sum(m._bn_loss for m in teacher.modules()
                       if isinstance(m, nn.BatchNorm2d) and hasattr(m, '_bn_loss'))
        (cls_loss + bn_reg * bn_loss).backward()
        optimizer.step()
    for h in bn_hooks:
        h.remove()
    return z.detach()

print('Activation maximisation synthesises class-conditional images from teacher only.')
print('BN regularisation ensures generated images have realistic activation statistics.')
```

## BatchNorm Statistic Regularization

Every BatchNorm2d layer stores running_mean and running_var computed over the training data during training. For a synthetic image to produce realistic intermediate activations, its activations at each BN layer should match these stored statistics. The BN statistics loss is: L_BN = sum_l [MSE(mean_generated_l, mean_running_l) + MSE(var_generated_l, var_running_l)]. This loss is differentiable with respect to the input image z and can be backpropagated through the frozen teacher to shape the generated image. BN matching is what distinguishes good DFKD from naive activation maximisation.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple

def get_teacher_bn_stats(teacher: nn.Module) -> List[Tuple[torch.Tensor, torch.Tensor]]:
    """Return (running_mean, running_var) for every BatchNorm2d in teacher."""
    return [(m.running_mean.detach().clone(), m.running_var.detach().clone())
            for m in teacher.modules() if isinstance(m, nn.BatchNorm2d)]

def bn_stat_matching_loss(teacher: nn.Module, x: torch.Tensor,
                           target_stats: List[Tuple[torch.Tensor, torch.Tensor]]) -> torch.Tensor:
    """Penalise mismatch between x's BN activation stats and teacher's stored stats."""
    losses, hooks = [], []
    bn_modules = [m for m in teacher.modules() if isinstance(m, nn.BatchNorm2d)]
    for i, module in enumerate(bn_modules):
        t_mean, t_var = target_stats[i]
        def make_hook(tm, tv):
            def hook(m, inp, out):
                losses.append(F.mse_loss(out.mean((0, 2, 3)), tm) +
                               F.mse_loss(out.var((0, 2, 3)),  tv))
            return hook
        hooks.append(module.register_forward_hook(make_hook(t_mean, t_var)))
    teacher.eval()
    _ = teacher(x)
    for h in hooks:
        h.remove()
    return torch.stack(losses).mean() if losses else x.new_tensor(0.0)

teacher = nn.Sequential(nn.Conv2d(3, 16, 3, padding=1), nn.BatchNorm2d(16), nn.ReLU(),
                         nn.Conv2d(16, 8, 3, padding=1), nn.BatchNorm2d(8), nn.ReLU())
real_stats = get_teacher_bn_stats(teacher)
gen_image  = torch.randn(4, 3, 32, 32, requires_grad=True)
loss = bn_stat_matching_loss(teacher, gen_image, real_stats)
print(f'BN stat matching loss (random image): {loss.item():.4f}')
print('Minimising this loss during synthesis yields realistic internal activations.')
```

## Generator-Based Methods — DAFL and CMI

DAFL (Data-Free Learning of Student Networks, Chen et al. 2019) replaces per-image optimisation with a learned generator G. G takes a noise vector z and produces synthetic images x_gen = G(z). G is trained adversarially: produce images that maximise teacher confidence and activation magnitudes while maintaining diversity. The student S is simultaneously trained to match teacher outputs on generated data. CMI (Contrastive Model Inversion, Fang et al. 2022) improves diversity by adding a contrastive loss that encourages different samples to produce distinct activation patterns, reducing mode collapse in the generated distribution.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class DataFreeGenerator(nn.Module):
    def __init__(self, z_dim=100, channels=3, size=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(z_dim, 512), nn.BatchNorm1d(512), nn.ReLU(),
            nn.Linear(512, channels * size * size), nn.Tanh())
        self.out_shape = (channels, size, size)

    def forward(self, z):
        return self.net(z).view(z.size(0), *self.out_shape)

def train_dfkd(teacher, student, generator, n_steps=100, z_dim=100, B=32, T=4.0):
    """Data-free KD: jointly train generator + student using frozen teacher."""
    teacher.eval()
    opt_g = optim.Adam(generator.parameters(), lr=1e-3)
    opt_s = optim.Adam(student.parameters(),   lr=1e-3)
    for step in range(n_steps):
        z = torch.randn(B, z_dim)
        with torch.no_grad():
            soft = F.softmax(teacher(generator(z)) / T, dim=-1)
        opt_s.zero_grad()
        kd = F.kl_div(F.log_softmax(student(generator(z).detach()) / T, dim=-1),
                       soft, reduction='batchmean') * T ** 2
        kd.backward(); opt_s.step()
        opt_g.zero_grad()
        g_loss = -teacher(generator(torch.randn(B, z_dim))).softmax(-1).max(-1).values.mean()
        g_loss.backward(); opt_g.step()
        if (step + 1) % 25 == 0:
            print(f'Step {step+1}: KD={kd.item():.3f}  G={g_loss.item():.3f}')

teacher = nn.Sequential(nn.Flatten(), nn.Linear(3072, 10))
student = nn.Sequential(nn.Flatten(), nn.Linear(3072, 10))
gen = DataFreeGenerator()
train_dfkd(teacher, student, gen, n_steps=50)
```

## Privacy and GDPR Use Cases

One compelling motivation for DFKD is privacy preservation. Training data often contains personal information — medical records, user communications, private images — that cannot be shared or stored after training under GDPR Article 17 (right to erasure). Once a model is trained, the original data can be legally deleted, leaving only the model weights. DFKD allows knowledge transfer from the frozen teacher to a smaller student without ever accessing the deleted data, enabling model compression and deployment optimisation while maintaining full regulatory compliance.

## Accuracy Gap vs Data-Dependent KD

Data-free KD consistently underperforms data-dependent KD. At low compression (retaining >75% of teacher parameters), the gap is 1-2%. At aggressive compression (<25% of parameters), the gap widens to 4-8%. CMI achieves the smallest gap by maximising mutual information between generated samples. The fundamental bottleneck is distribution shift: even the best generators do not perfectly replicate the training distribution, so the student sees a slightly different distribution than the teacher was optimised for.

```python
import numpy as np

# Accuracy comparison: data-free KD methods vs data-dependent KD on CIFAR-100
# Teacher: ResNet-34 (77.8%), Student: ResNet-18 family at various compressions
compression_pct = [100, 75, 50, 25, 10]  # student param % relative to teacher

data_dependent = [77.8, 76.4, 75.1, 71.3, 63.2]  # standard KD with real data
dfkd_dafl      = [77.8, 73.8, 72.1, 67.4, 58.1]  # DAFL (Chen et al. 2019)
dfkd_cmi       = [77.8, 74.9, 73.2, 69.1, 60.8]  # CMI  (Fang et al. 2022)
dfkd_zeroshot  = [77.8, 72.1, 70.4, 65.2, 55.7]  # Zero-shot KD (Nayak 2019)

print(f'{"Compression":>12}  {"Data-Dep":>9}  {"DAFL":>7}  {"CMI":>7}  {"ZeroShot":>9}')
print(f'{"(% params)":>12}  {"(real)": >9}  {"(DFKD)":>7}  {"(DFKD)":>7}  {"(DFKD)":>9}')
print('-' * 55)
for c, dd, da, cm, zs in zip(compression_pct, data_dependent, dfkd_dafl, dfkd_cmi, dfkd_zeroshot):
    print(f'{c:>11}%  {dd:>9.1f}  {da:>7.1f}  {cm:>7.1f}  {zs:>9.1f}')

gaps_dafl = [dd - da for dd, da in zip(data_dependent, dfkd_dafl)]
gaps_cmi  = [dd - cm for dd, cm in zip(data_dependent, dfkd_cmi)]
print(f'\nMean accuracy gap — DAFL: {np.mean(gaps_dafl):.1f}%  CMI: {np.mean(gaps_cmi):.1f}%')
print(f'Typical data-free quality gap: 2-5% vs data-dependent KD.')
```

## Fast-DFKD and Amortized Generation

Fast-DFKD (Fang et al. 2021) reduces the computational cost of DFKD through meta-learning. Rather than training a new generator from scratch for each teacher model, Fast-DFKD meta-learns a generator initialisation that adapts quickly to any teacher with only a few gradient steps. The meta-learned initialisation captures general visual priors (edges, textures, shapes) that are useful for any classification teacher, requiring only task-specific fine-tuning. Zero-shot KD (Nayak et al. 2019) is another fast approach: it samples from a Dirichlet distribution conditioned on the teacher's class statistics, bypassing neural synthesis entirely at lower accuracy.

> **Data-Free KD Cannot Fully Recover Data-Dependent KD Accuracy**: The 2-5% accuracy gap between data-free and data-dependent KD is a fundamental information-theoretic limitation. The teacher weights encode information about training data, but not all of it. Generated images can match BN statistics globally but not capture rare examples, class boundaries, or domain-specific patterns. If accuracy recovery is critical, consider using even a small amount of real data — 100 samples per class — to anchor the synthesis. This dramatically closes the gap at minimal privacy cost.

| Method | Data Required | Generator Type | Accuracy vs Real KD | Privacy Safe | Training Cost |
| --- | --- | --- | --- | --- | --- |
| Activation maximisation | None | Per-image optimisation | -4 to -8% | Yes | High (per-image opt) |
| DAFL (Chen 2019) | None | GAN generator | -3 to -5% | Yes | Medium (train G once) |
| CMI (Fang 2022) | None | GAN + contrastive | -2 to -4% | Yes | Medium |
| Zero-shot KD (Nayak 2019) | None | Dirichlet sampling | -4 to -7% | Yes | Low (no generator) |
| Fast-DFKD | None | Meta-learned generator | -3 to -5% | Yes | Low (fast adaptation) |
| Data-dependent KD | Full training set | Real data | Baseline | No | Low (no generator) |

- BN statistic matching is the key regulariser: without it, generated images are adversarial-like noise.
- Temperature for DFKD generator training: use T=20 (very soft) to maximise gradient signal.
- Generator diversity: condition G on one-hot class labels for class-conditional image synthesis.
- DAFL objective: maximise teacher confidence + activation magnitude + sample diversity (three terms).
- GDPR compliance: DFKD allows legal model compression when training data must be deleted post-training.
- Quality gap closes with data: 100 real samples per class reduces the gap by ~50% vs fully data-free.

---

