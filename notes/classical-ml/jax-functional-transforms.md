---
title: "JAX — jit, grad, vmap, and pmap"
slug: "jax-functional-transforms"
description: "JAX's four functional transforms — jit (JIT compilation), grad (autodiff), vmap (vectorization), and pmap (multi-device parallelism) — compose to build high-performance ML research code."
tags: ["pytorch", "tools", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSkFYIGlzIE51bVB5LWNvbXBhdGlibGUgKyB0cmFuc2Zvcm1hYmxlOiBhbnkgUHl0aG9uIGZ1bmN0aW9uIHRoYXQgY29tcHV0ZXMgd2l0aCBhcnJheXMgY2FuIGJlIEpJVC1jb21waWxlZCwgZGlmZmVyZW50aWF0ZWQsIHZlY3Rvcml6ZWQsIG9yIHBhcmFsbGVsaXplZCBieSB3cmFwcGluZyBpdCBpbiBhIHRyYW5zZm9ybWF0aW9uLiBUaGUga2V5IGNvbnN0cmFpbnQ6IGZ1bmN0aW9ucyBtdXN0IGJlIHB1cmUgKG5vIHNpZGUgZWZmZWN0cykgc28gSkFYIGNhbiB0cmFjZSBhbmQgdHJhbnNmb3JtIHRoZW0gc2FmZWx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBGb3VyIENvcmUgVHJhbnNmb3JtcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSkFYXHUwMDI3cyBwb3dlciBjb21lcyBmcm9tIGNvbXBvc2FiaWxpdHk6IGdyYWQodm1hcChqaXQoZikpKSB3b3JrcywgYW5kIHRoZSByZXN1bHQgaXMgZWZmaWNpZW50LiBFYWNoIHRyYW5zZm9ybSBhZGRzIG9uZSBjYXBhYmlsaXR5IHdpdGhvdXQgY2hhbmdpbmcgdGhlIG90aGVycy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbImpheC5qaXQoZik6IEpJVC1jb21waWxlIHZpYSBYTEEg4oCUIHRyYWNlcyBmIG9uIGFic3RyYWN0IHZhbHVlcywgZ2VuZXJhdGVzIGZ1c2VkIGRldmljZSBrZXJuZWxzLCBjYWNoZXMgY29tcGlsYXRpb24iLCJqYXguZ3JhZChmKTogY29tcHV0ZSBncmFkaWVudCBvZiBmIHcuci50LiBmaXJzdCBhcmd1bWVudCAob3IgYXJnbnVtcykg4oCUIHJldmVyc2UtbW9kZSBBRCBieSBkZWZhdWx0IiwiamF4LnZtYXAoZik6IHZlY3Rvcml6ZSBmIG92ZXIgYSBiYXRjaCBkaW1lbnNpb24g4oCUIGVsaW1pbmF0ZXMgZXhwbGljaXQgbG9vcHMgd2l0aG91dCBtb2RpZnlpbmcgZiIsImpheC5wbWFwKGYpOiBwYXJhbGxlbCBtYXAgb3ZlciBtdWx0aXBsZSBhY2NlbGVyYXRvcnMg4oCUIGVhY2ggZGV2aWNlIGdldHMgb25lIHNsaWNlIG9mIHRoZSBpbnB1dCIsIlB1cmUgZnVuY3Rpb25zIHJlcXVpcmVkOiBubyBQeXRob24gZ2xvYmFscywgbm8gaW4tcGxhY2UgbXV0YXRpb24sIG5vIEkvTyBpbnNpZGUgdHJhY2VkIGZ1bmN0aW9ucyIsIlB5dHJlZXM6IEpBWCB0cmVhdHMgbmVzdGVkIGRpY3RzL2xpc3RzL3R1cGxlcyBvZiBhcnJheXMgYXMgZmlyc3QtY2xhc3Mg4oCUIG1vZGVsIHBhcmFtcyBhcyBkaWN0cyB3b3JrIG5hdHVyYWxseSJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJqaXQsIGdyYWQsIGFuZCB2bWFwIEJhc2ljcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlc2UgdGhyZWUgdHJhbnNmb3JtcyBjb21wb3NlIGNsZWFubHkuIHZtYXAoZ3JhZChmKSkgY29tcHV0ZXMgcGVyLXNhbXBsZSBncmFkaWVudHMgaW4gb25lIHZlY3Rvcml6ZWQgcGFzcyDigJQgc29tZXRoaW5nIHRoYXQgd291bGQgcmVxdWlyZSBhIFB5dGhvbiBsb29wIGluIFB5VG9yY2guIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBqYXhcbmltcG9ydCBqYXgubnVtcHkgYXMgam5wXG5mcm9tIGpheCBpbXBvcnQgaml0LCBncmFkLCB2bWFwXG5cbiMgUHVyZSBmdW5jdGlvbjogbm8gc2lkZSBlZmZlY3RzLCBubyBnbG9iYWxzXG5kZWYgbXNlX2xvc3MocGFyYW1zLCB4LCB5KTpcbiAgICBwcmVkID0geCBAIHBhcmFtc1tcdTAwMjdXXHUwMDI3XSArIHBhcmFtc1tcdTAwMjdiXHUwMDI3XVxuICAgIHJldHVybiBqbnAubWVhbigocHJlZCAtIHkpICoqIDIpXG5cbiMgSklULWNvbXBpbGU6IGZpcnN0IGNhbGwgdHJhY2VzLCBzdWJzZXF1ZW50IGNhbGxzIHVzZSBjb21waWxlZCBrZXJuZWxcbnBhcmFtcyA9IHtcdTAwMjdXXHUwMDI3OiBqbnAub25lcygoNCwgMSkpLCBcdTAwMjdiXHUwMDI3OiBqbnAuemVyb3MoMSl9XG5YID0gam5wLm9uZXMoKDEwMCwgNCkpXG55ID0gam5wLm9uZXMoKDEwMCwgMSkpXG5cbmppdF9sb3NzID0gaml0KG1zZV9sb3NzKVxucHJpbnQoZlx1MDAyN0xvc3M6IHtqaXRfbG9zcyhwYXJhbXMsIFgsIHkpOi40Zn1cdTAwMjcpXG5cbiMgZ3JhZDogZGVyaXZhdGl2ZSB3LnIudC4gcGFyYW1zIChhcmdudW1zPTAgaXMgdGhlIGRlZmF1bHQpXG5ncmFkX2ZuID0gaml0KGdyYWQobXNlX2xvc3MsIGFyZ251bXM9MCkpXG5ncmFkcyA9IGdyYWRfZm4ocGFyYW1zLCBYLCB5KVxucHJpbnQoZlx1MDAyN0dyYWRpZW50IGtleXM6ICAgIHtsaXN0KGdyYWRzLmtleXMoKSl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0dyYWRpZW50IFcgc2hhcGU6IHtncmFkc1tcIldcIl0uc2hhcGV9XHUwMDI3KVxuXG4jIHZtYXA6IHZlY3Rvcml6ZSBhIHBlci1zYW1wbGUgZnVuY3Rpb24gb3ZlciBhIGJhdGNoIGF4aXNcbmRlZiBzaW5nbGVfc2FtcGxlX2xvc3MocGFyYW1zLCB4X3NpbmdsZSwgeV9zaW5nbGUpOlxuICAgIHByZWQgPSB4X3NpbmdsZSBAIHBhcmFtc1tcdTAwMjdXXHUwMDI3XSArIHBhcmFtc1tcdTAwMjdiXHUwMDI3XVxuICAgIHJldHVybiBqbnAubWVhbigocHJlZCAtIHlfc2luZ2xlKSAqKiAyKVxuXG5iYXRjaF9ncmFkX2ZuID0gdm1hcChncmFkKHNpbmdsZV9zYW1wbGVfbG9zcyksIGluX2F4ZXM9KE5vbmUsIDAsIDApKVxucGVyX3NhbXBsZV9ncmFkcyA9IGJhdGNoX2dyYWRfZm4ocGFyYW1zLCBYLCB5KSAgIyBwZXItc2FtcGxlIGdyYWRpZW50cyFcbnByaW50KGZcdTAwMjdQZXItc2FtcGxlIGdyYWQgVyBzaGFwZToge3Blcl9zYW1wbGVfZ3JhZHNbXCJXXCJdLnNoYXBlfVx1MDAyNykgICMgKDEwMCwgNCwgMSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGdWxsIEpBWCBUcmFpbmluZyBMb29wIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGZ1bmN0aW9uYWwgSkFYIHRyYWluaW5nIGxvb3AgZXhwbGljaXRseSBwYXNzZXMgc3RhdGUgKHBhcmFtcywgb3B0aW1pemVyIHN0YXRlKSBhcyBhcmd1bWVudHMgYW5kIHJldHVybnMgdXBkYXRlZCBzdGF0ZS4gTm8gY2xhc3NlcyBvciBtdXRhdGlvbnMg4oCUIGV2ZXJ5IHN0ZXAgaXMgYSBwdXJlIGZ1bmN0aW9uIHRoYXQgY2FuIGJlIGppdC1jb21waWxlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGpheFxuaW1wb3J0IGpheC5udW1weSBhcyBqbnBcbmZyb20gamF4IGltcG9ydCBqaXQsIGdyYWQsIHJhbmRvbVxuaW1wb3J0IG9wdGF4ICAjIEpBWCBvcHRpbWl6ZXIgbGlicmFyeVxuXG4jIEluaXRpYWxpemUgcGFyYW1zIGFzIGEgcHl0cmVlIGRpY3RcbmtleSA9IHJhbmRvbS5QUk5HS2V5KDQyKVxucGFyYW1zID0ge1xuICAgIFx1MDAyN1cxXHUwMDI3OiByYW5kb20ubm9ybWFsKGtleSwgKDIwLCA2NCkpICogMC4xLFxuICAgIFx1MDAyN2IxXHUwMDI3OiBqbnAuemVyb3MoNjQpLFxuICAgIFx1MDAyN1cyXHUwMDI3OiByYW5kb20ubm9ybWFsKGtleSwgKDY0LCAyKSkgKiAwLjEsXG4gICAgXHUwMDI3YjJcdTAwMjc6IGpucC56ZXJvcygyKVxufVxuXG5kZWYgZm9yd2FyZChwYXJhbXMsIHgpOlxuICAgIGggPSBqbnAudGFuaCh4IEAgcGFyYW1zW1x1MDAyN1cxXHUwMDI3XSArIHBhcmFtc1tcdTAwMjdiMVx1MDAyN10pXG4gICAgcmV0dXJuIGggQCBwYXJhbXNbXHUwMDI3VzJcdTAwMjddICsgcGFyYW1zW1x1MDAyN2IyXHUwMDI3XVxuXG5kZWYgY3Jvc3NfZW50cm9weV9sb3NzKHBhcmFtcywgeCwgeSk6XG4gICAgbG9naXRzID0gZm9yd2FyZChwYXJhbXMsIHgpXG4gICAgbG9nX3Byb2JzID0gamF4Lm5uLmxvZ19zb2Z0bWF4KGxvZ2l0cywgYXhpcz0tMSlcbiAgICByZXR1cm4gLWpucC5tZWFuKGxvZ19wcm9ic1tqbnAuYXJhbmdlKGxlbih5KSksIHldKVxuXG4jIE9wdGF4IG9wdGltaXplcjogQWRhbVxub3B0aW1pemVyID0gb3B0YXguYWRhbShsZWFybmluZ19yYXRlPTFlLTMpXG5vcHRfc3RhdGUgID0gb3B0aW1pemVyLmluaXQocGFyYW1zKVxuXG5Aaml0XG5kZWYgdHJhaW5fc3RlcChwYXJhbXMsIG9wdF9zdGF0ZSwgeCwgeSk6XG4gICAgbG9zcywgZ3JhZHMgPSBqYXgudmFsdWVfYW5kX2dyYWQoY3Jvc3NfZW50cm9weV9sb3NzKShwYXJhbXMsIHgsIHkpXG4gICAgdXBkYXRlcywgbmV3X29wdF9zdGF0ZSA9IG9wdGltaXplci51cGRhdGUoZ3JhZHMsIG9wdF9zdGF0ZSlcbiAgICBuZXdfcGFyYW1zID0gb3B0YXguYXBwbHlfdXBkYXRlcyhwYXJhbXMsIHVwZGF0ZXMpXG4gICAgcmV0dXJuIG5ld19wYXJhbXMsIG5ld19vcHRfc3RhdGUsIGxvc3NcblxuIyBUcmFpbmluZyBsb29wXG5rZXksIHN1YmtleSA9IHJhbmRvbS5zcGxpdChrZXkpXG5YX2RhdGEgPSByYW5kb20ubm9ybWFsKHN1YmtleSwgKDUwMCwgMjApKVxueV9kYXRhID0gcmFuZG9tLnJhbmRpbnQoa2V5LCAoNTAwLCksIDAsIDIpXG5mb3Igc3RlcCBpbiByYW5nZSg1KTpcbiAgICBwYXJhbXMsIG9wdF9zdGF0ZSwgbG9zcyA9IHRyYWluX3N0ZXAocGFyYW1zLCBvcHRfc3RhdGUsIFhfZGF0YSwgeV9kYXRhKVxuICAgIHByaW50KGZcdTAwMjdTdGVwIHtzdGVwKzF9OiBsb3NzPXtsb3NzOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50Ijoidm1hcCBmb3IgUGVyLVNhbXBsZSBHcmFkaWVudCBDb21wdXRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGVyLXNhbXBsZSBncmFkaWVudHMgYXJlIHJlcXVpcmVkIGZvciBkaWZmZXJlbnRpYWwgcHJpdmFjeSAoRFAtU0dEKSBhbmQgaW5mbHVlbmNlIGZ1bmN0aW9uIGNvbXB1dGF0aW9uLiBJbiBQeVRvcmNoIHRoaXMgcmVxdWlyZXMgYSBQeXRob24gbG9vcCBvdmVyIHRoZSBiYXRjaDsgaW4gSkFYLCB2bWFwKGdyYWQoZikpIGNvbXB1dGVzIHRoZW0gZWZmaWNpZW50bHkgaW4gb25lIHZlY3Rvcml6ZWQgcGFzcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGpheFxuaW1wb3J0IGpheC5udW1weSBhcyBqbnBcbmZyb20gamF4IGltcG9ydCB2bWFwLCBncmFkLCBqaXQsIHJhbmRvbVxuXG5rZXkgPSByYW5kb20uUFJOR0tleSgwKVxucGFyYW1zID0ge1x1MDAyN1dcdTAwMjc6IHJhbmRvbS5ub3JtYWwoa2V5LCAoMTAsIDUpKSwgXHUwMDI3Ylx1MDAyNzogam5wLnplcm9zKDUpfVxuXG5kZWYgc2luZ2xlX2xvc3MocGFyYW1zLCB4X2ksIHlfaSk6XG4gICAgbG9naXQgPSB4X2kgQCBwYXJhbXNbXHUwMDI3V1x1MDAyN10gKyBwYXJhbXNbXHUwMDI3Ylx1MDAyN11cbiAgICByZXR1cm4gamF4Lm5uLnNvZnRtYXhfY3Jvc3NfZW50cm9weV93aXRoX2ludGVnZXJfbGFiZWxzKGxvZ2l0LCB5X2kpXG5cbiMgdm1hcCBvdmVyIGJhdGNoIGRpbWVuc2lvbjogaW5fYXhlcz0oTm9uZSwgMCwgMClcbiMgcGFyYW1zOiBzYW1lIGZvciBhbGwgc2FtcGxlcyAoTm9uZSksIHggYW5kIHk6IG9uZSBwZXIgc2FtcGxlICgwKVxuYmF0Y2hfZ3JhZHNfZm4gPSBqaXQodm1hcChncmFkKHNpbmdsZV9sb3NzKSwgaW5fYXhlcz0oTm9uZSwgMCwgMCkpKVxuXG5YX2JhdGNoID0gcmFuZG9tLm5vcm1hbChrZXksICg2NCwgMTApKSAgICMgNjQgc2FtcGxlcywgMTAgZmVhdHVyZXNcbnlfYmF0Y2ggPSByYW5kb20ucmFuZGludChrZXksICg2NCwpLCAwLCA1KSAgIyA2NCBsYWJlbHNcblxucGVyX3NhbXBsZV9ncmFkcyA9IGJhdGNoX2dyYWRzX2ZuKHBhcmFtcywgWF9iYXRjaCwgeV9iYXRjaClcbnByaW50KGZcdTAwMjdQZXItc2FtcGxlIGdyYWQgVzoge3Blcl9zYW1wbGVfZ3JhZHNbXCJXXCJdLnNoYXBlfVx1MDAyNykgICMgKDY0LCAxMCwgNSlcblxuIyBGb3IgRFAtU0dEOiBjbGlwIGVhY2ggcGVyLXNhbXBsZSBncmFkaWVudCwgdGhlbiBhZ2dyZWdhdGVcbm1heF9ub3JtID0gMS4wXG5jbGlwcGVkX1cgPSBqbnAuY2xpcChcbiAgICBwZXJfc2FtcGxlX2dyYWRzW1x1MDAyN1dcdTAwMjddLFxuICAgIC1tYXhfbm9ybSAvIGpucC5zcXJ0KDEwICogNSksXG4gICAgbWF4X25vcm0gLyBqbnAuc3FydCgxMCAqIDUpXG4pXG5tZWFuX2dyYWRfVyA9IGNsaXBwZWRfVy5tZWFuKGF4aXM9MClcbnByaW50KGZcdTAwMjdDbGlwcGVkIG1lYW4gZ3JhZCBXOiB7bWVhbl9ncmFkX1cuc2hhcGV9XHUwMDI3KSAgIyAoMTAsIDUpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoicG1hcCBmb3IgTXVsdGktRGV2aWNlIERhdGEgUGFyYWxsZWxpc20ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6InBtYXAgbWFwcyBhIGZ1bmN0aW9uIG92ZXIgdGhlIGZpcnN0IGF4aXMgb2YgZWFjaCBhcnJheSwgZGlzdHJpYnV0aW5nIHNsaWNlcyBhY3Jvc3MgYWxsIGF2YWlsYWJsZSBkZXZpY2VzLiBFYWNoIGRldmljZSBydW5zIHRoZSBzYW1lIGNvbXB1dGF0aW9uIG9uIGl0cyBkYXRhIHNsaWNlLCB3aXRoIGNvbGxlY3RpdmUgb3BlcmF0aW9ucyAobGlrZSBsYXgucG1lYW4pIHRvIHN5bmNocm9uaXplLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgamF4XG5pbXBvcnQgamF4Lm51bXB5IGFzIGpucFxuZnJvbSBqYXggaW1wb3J0IHBtYXAsIHJhbmRvbVxuZnJvbSBqYXgubGF4IGltcG9ydCBwbWVhblxuXG5uX2RldmljZXMgPSBqYXguZGV2aWNlX2NvdW50KClcbnByaW50KGZcdTAwMjdBdmFpbGFibGUgZGV2aWNlczoge25fZGV2aWNlc31cdTAwMjcpXG5cbiMgUmVwbGljYXRlIHBhcmFtcyBhY3Jvc3MgYWxsIGRldmljZXNcbmRlZiByZXBsaWNhdGUoeCk6XG4gICAgcmV0dXJuIGpucC5icm9hZGNhc3RfdG8oeCwgKG5fZGV2aWNlcywpICsgeC5zaGFwZSlcblxua2V5ID0gcmFuZG9tLlBSTkdLZXkoNDIpXG5wYXJhbXNfcmVwID0ge1xuICAgIFx1MDAyN1dcdTAwMjc6IHJlcGxpY2F0ZShyYW5kb20ubm9ybWFsKGtleSwgKDEwLCA1KSkpLFxuICAgIFx1MDAyN2JcdTAwMjc6IHJlcGxpY2F0ZShqbnAuemVyb3MoNSkpXG59XG5cbkBwbWFwXG5kZWYgcGFyYWxsZWxfdHJhaW5fc3RlcChwYXJhbXMsIHhfc2hhcmQsIHlfc2hhcmQpOlxuICAgIGRlZiBsb3NzX2ZuKHApOlxuICAgICAgICBsb2dpdCA9IHhfc2hhcmQgQCBwW1x1MDAyN1dcdTAwMjddICsgcFtcdTAwMjdiXHUwMDI3XVxuICAgICAgICByZXR1cm4gam5wLm1lYW4oKGxvZ2l0IC0geV9zaGFyZCkgKiogMilcbiAgICBncmFkcyA9IGpheC5ncmFkKGxvc3NfZm4pKHBhcmFtcylcbiAgICAjIEF2ZXJhZ2UgZ3JhZGllbnRzIGFjcm9zcyBkZXZpY2VzIChhbGxyZWR1Y2UpXG4gICAgZ3JhZHMgPSBqYXgudHJlZV91dGlsLnRyZWVfbWFwKGxhbWJkYSBnOiBwbWVhbihnLCBheGlzX25hbWU9XHUwMDI3YmF0Y2hcdTAwMjcpLCBncmFkcylcbiAgICByZXR1cm4gZ3JhZHNcblxucHJpbnQoZlx1MDAyN3BtYXAgZGlzdHJpYnV0ZXMgYmF0Y2ggYXhpcyBvdmVyIHtuX2RldmljZXN9IGRldmljZShzKVx1MDAyNykifSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSkFYIHZzIFB5VG9yY2ggQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJBc3BlY3QiLCJQeVRvcmNoIiwiSkFYIl0sInJvd3MiOltbIlByb2dyYW1taW5nIG1vZGVsIiwiT2JqZWN0LW9yaWVudGVkIChubi5Nb2R1bGUsIHN0YXRlIGluIG9iamVjdCkiLCJGdW5jdGlvbmFsIOKAlCBzdGF0ZSBwYXNzZWQgZXhwbGljaXRseSBhcyBweXRyZWVzIl0sWyJBdXRvZGlmZiIsIkR5bmFtaWMgZ3JhcGgsIGVhZ2VyIGJhY2t3YXJkKCkiLCJDb21wb3NhYmxlIHRyYW5zZm9ybXM6IGdyYWQsIHZhbHVlX2FuZF9ncmFkIl0sWyJWZWN0b3JpemF0aW9uIiwiTWFudWFsIGxvb3Agb3IgdG9yY2gudm1hcCAobmV3ZXIpIiwidm1hcCDigJQgZmlyc3QtY2xhc3MsIGNvbXBvc2VzIHdpdGggZ3JhZCJdLFsiUGFyYWxsZWxpc20iLCJEaXN0cmlidXRlZERhdGFQYXJhbGxlbCwgRlNEUCIsInBtYXAg4oCUIGVsZWdhbnQgYnV0IGxpbWl0ZWQgdG8gb25lIGhvc3QiXSxbIkRlYnVnZ2luZyIsIkVhZ2VyIG1vZGUsIHBkYi1mcmllbmRseSIsIkhhcmRlciDigJQgdHJhY2VkIGZ1bmN0aW9ucyBjYW5cdTAwMjd0IHByaW50IGluc2lkZSBqaXQiXSxbIkVjb3N5c3RlbSIsIk1hc3NpdmUgKEh1Z2dpbmdGYWNlLCB0aW1tLCBldGMuKSIsIkdyb3dpbmcgKEZsYXgsIEhhaWt1LCBPcHRheCwgRXF1aW5veCkiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSkFYXHUwMDI3cyBQdXJlIEZ1bmN0aW9uIFJlcXVpcmVtZW50IiwiY29udGVudCI6IkpBWCB0cmFjZXMgZnVuY3Rpb25zIGJ5IHJ1bm5pbmcgdGhlbSB3aXRoIGFic3RyYWN0IHZhbHVlcywgbm90IHJlYWwgZGF0YS4gQW55IFB5dGhvbiBzaWRlIGVmZmVjdCBpbnNpZGUgYSBqaXQtY29tcGlsZWQgZnVuY3Rpb24gKHByaW50LCBnbG9iYWwgbXV0YXRpb24sIHJhbmRvbW5lc3Mgd2l0aG91dCBleHBsaWNpdCBrZXkgc3BsaXR0aW5nKSBwcm9kdWNlcyBpbmNvcnJlY3QgYmVoYXZpb3Ig4oCUIHRoZSBzaWRlIGVmZmVjdCBvbmx5IGhhcHBlbnMgZHVyaW5nIHRyYWNpbmcsIG5vdCBhdCBydW50aW1lLiBBbHdheXMgcGFzcyBqYXgucmFuZG9tLlBSTkdLZXkgZXhwbGljaXRseSBhbmQgc3BsaXQga2V5cyBmb3IgZWFjaCBvcGVyYXRpb24gdGhhdCBuZWVkcyByYW5kb21uZXNzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbImppdCBjb21waWxlcyB2aWEgWExBIOKAlCBmaXJzdCBjYWxsIHRyYWNlcywgc3Vic2VxdWVudCBjYWxscyBydW4gY29tcGlsZWQga2VybmVsOyBubyBtb2RlbCBjaGFuZ2VzIG5lZWRlZCIsImdyYWQgZGlmZmVyZW50aWF0ZXMgYW55IHB1cmUgUHl0aG9uIGZ1bmN0aW9uIOKAlCBjb21wb3NlcyB3aXRoIGppdCBhbmQgdm1hcCBmcmVlbHkiLCJ2bWFwIHZlY3Rvcml6ZXMgYSBwZXItZWxlbWVudCBmdW5jdGlvbiBvdmVyIGEgYmF0Y2ggZGltZW5zaW9uIOKAlCByZXBsYWNlcyBQeXRob24gbG9vcHMiLCJwbWFwIHBhcmFsbGVsaXplcyBvdmVyIG11bHRpcGxlIGFjY2VsZXJhdG9ycyB3aXRoIGNvbGxlY3RpdmUgb3BlcmF0aW9ucyBmb3IgZ3JhZGllbnQgYXZlcmFnaW5nIiwiUHVyZSBmdW5jdGlvbnMgcmVxdWlyZWQ6IG5vIHNpZGUgZWZmZWN0cywgZXhwbGljaXQgc3RhdGUgcGFzc2luZywgZXhwbGljaXQgUFJORyBrZXkgc3BsaXR0aW5nIl19XQ=="
---
# JAX — jit, grad, vmap, and pmap

JAX is NumPy-compatible + transformable: any Python function that computes with arrays can be JIT-compiled, differentiated, vectorized, or parallelized by wrapping it in a transformation. The key constraint: functions must be pure (no side effects) so JAX can trace and transform them safely.

## The Four Core Transforms

JAX's power comes from composability: grad(vmap(jit(f))) works, and the result is efficient. Each transform adds one capability without changing the others.

- jax.jit(f): JIT-compile via XLA — traces f on abstract values, generates fused device kernels, caches compilation
- jax.grad(f): compute gradient of f w.r.t. first argument (or argnums) — reverse-mode AD by default
- jax.vmap(f): vectorize f over a batch dimension — eliminates explicit loops without modifying f
- jax.pmap(f): parallel map over multiple accelerators — each device gets one slice of the input
- Pure functions required: no Python globals, no in-place mutation, no I/O inside traced functions
- Pytrees: JAX treats nested dicts/lists/tuples of arrays as first-class — model params as dicts work naturally

## jit, grad, and vmap Basics

These three transforms compose cleanly. vmap(grad(f)) computes per-sample gradients in one vectorized pass — something that would require a Python loop in PyTorch.

```python
import jax
import jax.numpy as jnp
from jax import jit, grad, vmap

# Pure function: no side effects, no globals
def mse_loss(params, x, y):
    pred = x @ params['W'] + params['b']
    return jnp.mean((pred - y) ** 2)

# JIT-compile: first call traces, subsequent calls use compiled kernel
params = {'W': jnp.ones((4, 1)), 'b': jnp.zeros(1)}
X = jnp.ones((100, 4))
y = jnp.ones((100, 1))

jit_loss = jit(mse_loss)
print(f'Loss: {jit_loss(params, X, y):.4f}')

# grad: derivative w.r.t. params (argnums=0 is the default)
grad_fn = jit(grad(mse_loss, argnums=0))
grads = grad_fn(params, X, y)
print(f'Gradient keys:    {list(grads.keys())}')
print(f'Gradient W shape: {grads["W"].shape}')

# vmap: vectorize a per-sample function over a batch axis
def single_sample_loss(params, x_single, y_single):
    pred = x_single @ params['W'] + params['b']
    return jnp.mean((pred - y_single) ** 2)

batch_grad_fn = vmap(grad(single_sample_loss), in_axes=(None, 0, 0))
per_sample_grads = batch_grad_fn(params, X, y)  # per-sample gradients!
print(f'Per-sample grad W shape: {per_sample_grads["W"].shape}')  # (100, 4, 1)
```

## Full JAX Training Loop

A functional JAX training loop explicitly passes state (params, optimizer state) as arguments and returns updated state. No classes or mutations — every step is a pure function that can be jit-compiled.

```python
import jax
import jax.numpy as jnp
from jax import jit, grad, random
import optax  # JAX optimizer library

# Initialize params as a pytree dict
key = random.PRNGKey(42)
params = {
    'W1': random.normal(key, (20, 64)) * 0.1,
    'b1': jnp.zeros(64),
    'W2': random.normal(key, (64, 2)) * 0.1,
    'b2': jnp.zeros(2)
}

def forward(params, x):
    h = jnp.tanh(x @ params['W1'] + params['b1'])
    return h @ params['W2'] + params['b2']

def cross_entropy_loss(params, x, y):
    logits = forward(params, x)
    log_probs = jax.nn.log_softmax(logits, axis=-1)
    return -jnp.mean(log_probs[jnp.arange(len(y)), y])

# Optax optimizer: Adam
optimizer = optax.adam(learning_rate=1e-3)
opt_state  = optimizer.init(params)

@jit
def train_step(params, opt_state, x, y):
    loss, grads = jax.value_and_grad(cross_entropy_loss)(params, x, y)
    updates, new_opt_state = optimizer.update(grads, opt_state)
    new_params = optax.apply_updates(params, updates)
    return new_params, new_opt_state, loss

# Training loop
key, subkey = random.split(key)
X_data = random.normal(subkey, (500, 20))
y_data = random.randint(key, (500,), 0, 2)
for step in range(5):
    params, opt_state, loss = train_step(params, opt_state, X_data, y_data)
    print(f'Step {step+1}: loss={loss:.4f}')
```

## vmap for Per-Sample Gradient Computation

Per-sample gradients are required for differential privacy (DP-SGD) and influence function computation. In PyTorch this requires a Python loop over the batch; in JAX, vmap(grad(f)) computes them efficiently in one vectorized pass.

```python
import jax
import jax.numpy as jnp
from jax import vmap, grad, jit, random

key = random.PRNGKey(0)
params = {'W': random.normal(key, (10, 5)), 'b': jnp.zeros(5)}

def single_loss(params, x_i, y_i):
    logit = x_i @ params['W'] + params['b']
    return jax.nn.softmax_cross_entropy_with_integer_labels(logit, y_i)

# vmap over batch dimension: in_axes=(None, 0, 0)
# params: same for all samples (None), x and y: one per sample (0)
batch_grads_fn = jit(vmap(grad(single_loss), in_axes=(None, 0, 0)))

X_batch = random.normal(key, (64, 10))   # 64 samples, 10 features
y_batch = random.randint(key, (64,), 0, 5)  # 64 labels

per_sample_grads = batch_grads_fn(params, X_batch, y_batch)
print(f'Per-sample grad W: {per_sample_grads["W"].shape}')  # (64, 10, 5)

# For DP-SGD: clip each per-sample gradient, then aggregate
max_norm = 1.0
clipped_W = jnp.clip(
    per_sample_grads['W'],
    -max_norm / jnp.sqrt(10 * 5),
    max_norm / jnp.sqrt(10 * 5)
)
mean_grad_W = clipped_W.mean(axis=0)
print(f'Clipped mean grad W: {mean_grad_W.shape}')  # (10, 5)
```

## pmap for Multi-Device Data Parallelism

pmap maps a function over the first axis of each array, distributing slices across all available devices. Each device runs the same computation on its data slice, with collective operations (like lax.pmean) to synchronize.

```python
import jax
import jax.numpy as jnp
from jax import pmap, random
from jax.lax import pmean

n_devices = jax.device_count()
print(f'Available devices: {n_devices}')

# Replicate params across all devices
def replicate(x):
    return jnp.broadcast_to(x, (n_devices,) + x.shape)

key = random.PRNGKey(42)
params_rep = {
    'W': replicate(random.normal(key, (10, 5))),
    'b': replicate(jnp.zeros(5))
}

@pmap
def parallel_train_step(params, x_shard, y_shard):
    def loss_fn(p):
        logit = x_shard @ p['W'] + p['b']
        return jnp.mean((logit - y_shard) ** 2)
    grads = jax.grad(loss_fn)(params)
    # Average gradients across devices (allreduce)
    grads = jax.tree_util.tree_map(lambda g: pmean(g, axis_name='batch'), grads)
    return grads

print(f'pmap distributes batch axis over {n_devices} device(s)')
```

---

## JAX vs PyTorch Comparison

| Aspect | PyTorch | JAX |
| --- | --- | --- |
| Programming model | Object-oriented (nn.Module, state in object) | Functional — state passed explicitly as pytrees |
| Autodiff | Dynamic graph, eager backward() | Composable transforms: grad, value_and_grad |
| Vectorization | Manual loop or torch.vmap (newer) | vmap — first-class, composes with grad |
| Parallelism | DistributedDataParallel, FSDP | pmap — elegant but limited to one host |
| Debugging | Eager mode, pdb-friendly | Harder — traced functions can't print inside jit |
| Ecosystem | Massive (HuggingFace, timm, etc.) | Growing (Flax, Haiku, Optax, Equinox) |

> **JAX's Pure Function Requirement**: JAX traces functions by running them with abstract values, not real data. Any Python side effect inside a jit-compiled function (print, global mutation, randomness without explicit key splitting) produces incorrect behavior — the side effect only happens during tracing, not at runtime. Always pass jax.random.PRNGKey explicitly and split keys for each operation that needs randomness.

## Key Takeaways

- jit compiles via XLA — first call traces, subsequent calls run compiled kernel; no model changes needed
- grad differentiates any pure Python function — composes with jit and vmap freely
- vmap vectorizes a per-element function over a batch dimension — replaces Python loops
- pmap parallelizes over multiple accelerators with collective operations for gradient averaging
- Pure functions required: no side effects, explicit state passing, explicit PRNG key splitting

