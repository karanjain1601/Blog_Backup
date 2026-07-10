---
title: "DPO — Direct Preference Optimization Without the RL Loop"
slug: "dpo-direct-preference"
description: "Complete treatment of DPO: derivation from the KL-constrained RL objective, loss implementation, training loop with frozen reference, implicit reward interpretation, and comparison against PPO-RLHF."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRFBPIChEaXJlY3QgUHJlZmVyZW5jZSBPcHRpbWl6YXRpb24sIFJhZmFpbG92IGV0IGFsLiAyMDIzKSBlbGltaW5hdGVzIHRoZSByZXdhcmQgbW9kZWwgYW5kIFJMIHRyYWluaW5nIGxvb3AgZW50aXJlbHkuIEJ5IGRlcml2aW5nIGEgY2xvc2VkLWZvcm0gcmVsYXRpb25zaGlwIGJldHdlZW4gdGhlIG9wdGltYWwgcG9saWN5LCB0aGUgcmVmZXJlbmNlIHBvbGljeSwgYW5kIGh1bWFuIHByZWZlcmVuY2VzLCBEUE8gY29udmVydHMgUkxIRiBpbnRvIGEgc3VwZXJ2aXNlZCBjbGFzc2lmaWNhdGlvbiBwcm9ibGVtIG92ZXIgcHJlZmVyZW5jZSBwYWlycyDigJQgbWFraW5nIGFsaWdubWVudCB0cmFpbmluZyBzdWJzdGFudGlhbGx5IG1vcmUgc3RhYmxlIGFuZCBjb21wdXRhdGlvbmFsbHkgZWZmaWNpZW50IHRoYW4gUFBPLVJMSEYuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRFBPIERlcml2YXRpb24gZnJvbSBPcHRpbWFsIFBvbGljeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRFBPIHN0YXJ0cyBmcm9tIHRoZSBLTC1jb25zdHJhaW5lZCBSTCBvYmplY3RpdmU6IG1heF9waSBFW3IoeCx5KV0gLSBiZXRhICogS0xbcGkgfHwgcGlfcmVmXS4gVGhlIG9wdGltYWwgcG9saWN5IHNhdGlzZmllcyBwaSooeXx4KSBwcm9wb3J0aW9uYWwgdG8gcGlfcmVmKHl8eCkgKiBleHAociooeCx5KS9iZXRhKS4gUmVhcnJhbmdpbmc6IHIqKHgseSkgPSBiZXRhICogbG9nW3BpKih5fHgpIC8gcGlfcmVmKHl8eCldICsgYmV0YSAqIGxvZyBaKHgpLiBTdWJzdGl0dXRpbmcgaW50byB0aGUgQnJhZGxleS1UZXJyeSBwcmVmZXJlbmNlIG1vZGVsIGVsaW1pbmF0ZXMgYm90aCByKiBhbmQgdGhlIHBhcnRpdGlvbiBmdW5jdGlvbiBaKHgpLCB5aWVsZGluZyB0aGUgRFBPIGxvc3MgZGlyZWN0bHkgZnJvbSBwYWlyZWQgcHJlZmVyZW5jZXMgKHgsIHlfdywgeV9sKSB3aXRob3V0IGV2ZXIgdHJhaW5pbmcgYSByZXdhcmQgbW9kZWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRFBPIExvc3MgSW1wbGVtZW50YXRpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHR5cGluZyBpbXBvcnQgVHVwbGVcblxuZGVmIGRwb19sb3NzKFxuICAgIHBvbGljeV9jaG9zZW5fbG9ncHM6IHRvcmNoLlRlbnNvcixcbiAgICBwb2xpY3lfcmVqZWN0ZWRfbG9ncHM6IHRvcmNoLlRlbnNvcixcbiAgICByZWZfY2hvc2VuX2xvZ3BzOiB0b3JjaC5UZW5zb3IsXG4gICAgcmVmX3JlamVjdGVkX2xvZ3BzOiB0b3JjaC5UZW5zb3IsXG4gICAgYmV0YTogZmxvYXQgPSAwLjEsXG4pIC1cdTAwM2UgVHVwbGVbdG9yY2guVGVuc29yLCBkaWN0XTpcbiAgICAjIERQTyBsb3NzOiAtRVtsb2cgc2lnbWEoYmV0YSAqIChsb2dfcmF0aW9fY2hvc2VuIC0gbG9nX3JhdGlvX3JlamVjdGVkKSldXG4gICAgIyBMb2cgcmF0aW86IGxvZ1twaV90aGV0YSh5fHgpIC8gcGlfcmVmKHl8eCldXG4gICAgY2hvc2VuX2xvZ19yYXRpbyA9IHBvbGljeV9jaG9zZW5fbG9ncHMgLSByZWZfY2hvc2VuX2xvZ3BzXG4gICAgcmVqZWN0ZWRfbG9nX3JhdGlvID0gcG9saWN5X3JlamVjdGVkX2xvZ3BzIC0gcmVmX3JlamVjdGVkX2xvZ3BzXG4gICAgbG9naXRzID0gYmV0YSAqIChjaG9zZW5fbG9nX3JhdGlvIC0gcmVqZWN0ZWRfbG9nX3JhdGlvKVxuICAgIGxvc3MgPSAtRi5sb2dzaWdtb2lkKGxvZ2l0cykubWVhbigpXG4gICAgIyBJbXBsaWNpdCByZXdhcmRzIGZvciBtb25pdG9yaW5nIHByZWZlcmVuY2UgYWxpZ25tZW50XG4gICAgY2hvc2VuX3Jld2FyZHMgPSBiZXRhICogY2hvc2VuX2xvZ19yYXRpby5kZXRhY2goKVxuICAgIHJlamVjdGVkX3Jld2FyZHMgPSBiZXRhICogcmVqZWN0ZWRfbG9nX3JhdGlvLmRldGFjaCgpXG4gICAgcmV3YXJkX21hcmdpbiA9IChjaG9zZW5fcmV3YXJkcyAtIHJlamVjdGVkX3Jld2FyZHMpLm1lYW4oKS5pdGVtKClcbiAgICBhY2N1cmFjeSA9IChsb2dpdHMgXHUwMDNlIDApLmZsb2F0KCkubWVhbigpLml0ZW0oKVxuICAgIHJldHVybiBsb3NzLCB7XG4gICAgICAgIFwicmV3YXJkX21hcmdpblwiOiByZXdhcmRfbWFyZ2luLFxuICAgICAgICBcImRwb19hY2N1cmFjeVwiOiBhY2N1cmFjeSxcbiAgICAgICAgXCJjaG9zZW5fcmV3YXJkXCI6IGNob3Nlbl9yZXdhcmRzLm1lYW4oKS5pdGVtKCksXG4gICAgICAgIFwicmVqZWN0ZWRfcmV3YXJkXCI6IHJlamVjdGVkX3Jld2FyZHMubWVhbigpLml0ZW0oKSxcbiAgICB9In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRFBPIFRyYWluaW5nIExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBEUE8gdHJhaW5pbmcgc2V0dXAgcmVxdWlyZXMgb25seSB0d28gbW9kZWxzOiB0aGUgZnJvemVuIHJlZmVyZW5jZSBwaV9yZWYgKHRoZSBTRlQgY2hlY2twb2ludCkgYW5kIHRoZSB0cmFpbmFibGUgcG9saWN5IHBpX3RoZXRhLiBCb3RoIG1vZGVscyBmb3J3YXJkLXBhc3MgdGhyb3VnaCBlYWNoIHNlcXVlbmNlIHRvIGNvbXB1dGUgbG9nLXByb2JhYmlsaXRpZXMsIGJ1dCBvbmx5IHRoZSBwb2xpY3kgcmVjZWl2ZXMgZ3JhZGllbnQgdXBkYXRlcy4gVGhlIHJlZmVyZW5jZSBtb2RlbCBzZXJ2ZXMgYXMgYSBzb2Z0IGNvbnN0cmFpbnQgcHJldmVudGluZyB0aGUgcG9saWN5IGZyb20gZHJpZnRpbmcgdG9vIGZhciBmcm9tIG5hdHVyYWwgbGFuZ3VhZ2UgZGlzdHJpYnV0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsRm9yQ2F1c2FsTE1cbmZyb20gdG9yY2gub3B0aW0gaW1wb3J0IEFkYW1XXG5mcm9tIHR5cGluZyBpbXBvcnQgVHVwbGVcblxuZGVmIGdldF9zZXF1ZW5jZV9sb2dwcyhtb2RlbCwgaW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzaywgbGFiZWxzLCBkZXZpY2UpOlxuICAgIG91dHB1dHMgPSBtb2RlbChcbiAgICAgICAgaW5wdXRfaWRzPWlucHV0X2lkcy50byhkZXZpY2UpLFxuICAgICAgICBhdHRlbnRpb25fbWFzaz1hdHRlbnRpb25fbWFzay50byhkZXZpY2UpLFxuICAgIClcbiAgICBsb2dpdHMgPSBvdXRwdXRzLmxvZ2l0c1s6LCA6LTFdICAjIHNoaWZ0IGZvciBuZXh0LXRva2VuIHByZWRpY3Rpb25cbiAgICBsb2dfcHJvYnMgPSB0b3JjaC5sb2dfc29mdG1heChsb2dpdHMsIGRpbT0tMSlcbiAgICB0b2tlbl9sb2dwcyA9IGxvZ19wcm9icy5nYXRoZXIoMiwgbGFiZWxzWzosIDE6XS50byhkZXZpY2UpLnVuc3F1ZWV6ZSgyKSkuc3F1ZWV6ZSgyKVxuICAgIGxhYmVsX21hc2sgPSAobGFiZWxzWzosIDE6XS50byhkZXZpY2UpICE9IC0xMDApLmZsb2F0KClcbiAgICByZXR1cm4gKHRva2VuX2xvZ3BzICogbGFiZWxfbWFzaykuc3VtKGRpbT0xKSAvIGxhYmVsX21hc2suc3VtKGRpbT0xKS5jbGFtcChtaW49MSlcblxuZGVmIGRwb190cmFpbmluZ19zdGVwKHBvbGljeV9tb2RlbCwgcmVmX21vZGVsLCBiYXRjaCwgb3B0aW1pemVyLCBiZXRhPTAuMSwgZGV2aWNlPVwiY3VkYVwiKTpcbiAgICAjIEZvcndhcmQgYm90aCBjaG9zZW4gYW5kIHJlamVjdGVkIHRocm91Z2ggcG9saWN5IGFuZCBmcm96ZW4gcmVmZXJlbmNlXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgcF9jaG9zZW4gPSBnZXRfc2VxdWVuY2VfbG9ncHMoXG4gICAgICAgIHBvbGljeV9tb2RlbCwgYmF0Y2hbXCJjaG9zZW5faWRzXCJdLCBiYXRjaFtcImNob3Nlbl9tYXNrXCJdLCBiYXRjaFtcImNob3Nlbl9sYWJlbHNcIl0sIGRldmljZVxuICAgIClcbiAgICBwX3JlamVjdGVkID0gZ2V0X3NlcXVlbmNlX2xvZ3BzKFxuICAgICAgICBwb2xpY3lfbW9kZWwsIGJhdGNoW1wicmVqZWN0ZWRfaWRzXCJdLCBiYXRjaFtcInJlamVjdGVkX21hc2tcIl0sIGJhdGNoW1wicmVqZWN0ZWRfbGFiZWxzXCJdLCBkZXZpY2VcbiAgICApXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHJfY2hvc2VuID0gZ2V0X3NlcXVlbmNlX2xvZ3BzKFxuICAgICAgICAgICAgcmVmX21vZGVsLCBiYXRjaFtcImNob3Nlbl9pZHNcIl0sIGJhdGNoW1wiY2hvc2VuX21hc2tcIl0sIGJhdGNoW1wiY2hvc2VuX2xhYmVsc1wiXSwgZGV2aWNlXG4gICAgICAgIClcbiAgICAgICAgcl9yZWplY3RlZCA9IGdldF9zZXF1ZW5jZV9sb2dwcyhcbiAgICAgICAgICAgIHJlZl9tb2RlbCwgYmF0Y2hbXCJyZWplY3RlZF9pZHNcIl0sIGJhdGNoW1wicmVqZWN0ZWRfbWFza1wiXSwgYmF0Y2hbXCJyZWplY3RlZF9sYWJlbHNcIl0sIGRldmljZVxuICAgICAgICApXG4gICAgbG9zcywgbWV0cmljcyA9IGRwb19sb3NzKHBfY2hvc2VuLCBwX3JlamVjdGVkLCByX2Nob3Nlbiwgcl9yZWplY3RlZCwgYmV0YSlcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgcmV0dXJuIG1ldHJpY3MifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbXBsaWNpdCBSZXdhcmQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRQT1x1MDAyN3MgaW1wbGljaXQgcmV3YXJkIGJldGEgKiBsb2dbcGlfdGhldGEoeXx4KSAvIHBpX3JlZih5fHgpXSBlbWVyZ2VzIGZyb20gdGhlIHBvbGljeVx1MDAyN3MgbG9nLXByb2JhYmlsaXR5IHJhdGlvIHdpdGggdGhlIHJlZmVyZW5jZS4gVGhpcyByZXdhcmQgaXMgbm90IGV4cGxpY2l0bHkgdHJhaW5lZCDigJQgaXQgYXJpc2VzIGFzIGEgbmF0dXJhbCBjb25zZXF1ZW5jZSBvZiB0aGUgcG9saWN5IGxlYXJuaW5nIHRvIHByZWZlciBjaG9zZW4gcmVzcG9uc2VzIG92ZXIgcmVqZWN0ZWQgb25lcy4gTW9uaXRvcmluZyB0aGlzIGltcGxpY2l0IHJld2FyZCBkdXJpbmcgdHJhaW5pbmcgaGVscHMgZGlhZ25vc2Ugd2hldGhlciBEUE8gaXMgbGVhcm5pbmcgbWVhbmluZ2Z1bCBwcmVmZXJlbmNlcyBvciBvdmVyZml0dGluZyB0byBzdXJmYWNlIGFydGlmYWN0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBjb21wdXRlX2Rwb19pbXBsaWNpdF9yZXdhcmQoXG4gICAgcG9saWN5X21vZGVsLFxuICAgIHJlZl9tb2RlbCxcbiAgICBpbnB1dF9pZHM6IHRvcmNoLlRlbnNvcixcbiAgICBhdHRlbnRpb25fbWFzazogdG9yY2guVGVuc29yLFxuICAgIGxhYmVsczogdG9yY2guVGVuc29yLFxuICAgIGJldGE6IGZsb2F0ID0gMC4xLFxuICAgIGRldmljZTogc3RyID0gXCJjdWRhXCIsXG4pIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICMgRFBPIGltcGxpY2l0IHJld2FyZDogYmV0YSAqIGxvZ1twaV90aGV0YSh5fHgpIC8gcGlfcmVmKHl8eCldXG4gICAgZGVmIHNlcXVlbmNlX2xvZ3BzKG1vZGVsLCBpZHMsIG1hc2ssIGxibHMpOlxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIG91dCA9IG1vZGVsKFxuICAgICAgICAgICAgICAgIGlucHV0X2lkcz1pZHMudG8oZGV2aWNlKSwgYXR0ZW50aW9uX21hc2s9bWFzay50byhkZXZpY2UpXG4gICAgICAgICAgICApXG4gICAgICAgICAgICBscCA9IHRvcmNoLmxvZ19zb2Z0bWF4KG91dC5sb2dpdHNbOiwgOi0xXSwgZGltPS0xKVxuICAgICAgICAgICAgdG9rX2xwID0gbHAuZ2F0aGVyKDIsIGxibHNbOiwgMTpdLnRvKGRldmljZSkudW5zcXVlZXplKDIpKS5zcXVlZXplKDIpXG4gICAgICAgICAgICBsYmxfbWFzayA9IChsYmxzWzosIDE6XS50byhkZXZpY2UpICE9IC0xMDApLmZsb2F0KClcbiAgICAgICAgICAgIHJldHVybiAodG9rX2xwICogbGJsX21hc2spLnN1bSgxKSAvIGxibF9tYXNrLnN1bSgxKS5jbGFtcChtaW49MSlcbiAgICBwb2xpY3lfbG9ncHMgPSBzZXF1ZW5jZV9sb2dwcyhwb2xpY3lfbW9kZWwsIGlucHV0X2lkcywgYXR0ZW50aW9uX21hc2ssIGxhYmVscylcbiAgICByZWZfbG9ncHMgPSBzZXF1ZW5jZV9sb2dwcyhyZWZfbW9kZWwsIGlucHV0X2lkcywgYXR0ZW50aW9uX21hc2ssIGxhYmVscylcbiAgICAjIFBvc2l0aXZlIHZhbHVlIG1lYW5zIHBvbGljeSBhc3NpZ25zIGhpZ2hlciBwcm9iYWJpbGl0eSB0aGFuIHJlZmVyZW5jZVxuICAgIHJldHVybiBiZXRhICogKHBvbGljeV9sb2dwcyAtIHJlZl9sb2dwcykgICMgW2JhdGNoXSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vbml0b3JpbmcgQ2hvc2VuIHZzIFJlamVjdGVkIExvZy1Qcm9iYWJpbGl0aWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEdXJpbmcgc3VjY2Vzc2Z1bCBEUE8gdHJhaW5pbmcsIHRoZSBsb2ctcHJvYmFiaWxpdHkgcmF0aW8gZm9yIGNob3NlbiByZXNwb25zZXMgc2hvdWxkIGluY3JlYXNlIHdoaWxlIHRoZSByYXRpbyBmb3IgcmVqZWN0ZWQgcmVzcG9uc2VzIGRlY3JlYXNlcy4gVGhlIG1hcmdpbiAoY2hvc2VuX3JhdGlvIC0gcmVqZWN0ZWRfcmF0aW8pIGlzIHRoZSBtb3N0IGRpYWdub3N0aWMgc2lnbmFsIOKAlCBhIHN0YWduYW50IG9yIGRlY3JlYXNpbmcgbWFyZ2luIGluZGljYXRlcyB0aGUgcG9saWN5IGlzIG5vdCBsZWFybmluZyB0byBkaXN0aW5ndWlzaCBwcmVmZXJlbmNlcy4gVHJhY2sgYm90aCByYXRpb3MgYXQgZXZlcnkgc3RlcDsgaWYgY2hvc2VuX3JhdGlvIGRlY3JlYXNlcyBvdmVyIGFueSA1LXN0ZXAgd2luZG93LCByZWR1Y2UgdGhlIGxlYXJuaW5nIHJhdGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5cbmRlZiBtb25pdG9yX2Rwb19sb2dwcm9iX2V2b2x1dGlvbihcbiAgICBwb2xpY3lfY2hvc2VuX2xvZ3BzOiB0b3JjaC5UZW5zb3IsXG4gICAgcG9saWN5X3JlamVjdGVkX2xvZ3BzOiB0b3JjaC5UZW5zb3IsXG4gICAgcmVmX2Nob3Nlbl9sb2dwczogdG9yY2guVGVuc29yLFxuICAgIHJlZl9yZWplY3RlZF9sb2dwczogdG9yY2guVGVuc29yLFxuICAgIHN0ZXA6IGludCxcbiAgICBoaXN0b3J5OiBsaXN0LFxuKSAtXHUwMDNlIGRpY3Q6XG4gICAgIyBUcmFjayBsb2ctcHJvYiByYXRpb3MgZHVyaW5nIERQTyB0cmFpbmluZyB0byBkZXRlY3QgZGl2ZXJnZW5jZVxuICAgIGNob3Nlbl9yYXRpbyA9IChwb2xpY3lfY2hvc2VuX2xvZ3BzIC0gcmVmX2Nob3Nlbl9sb2dwcykubWVhbigpLml0ZW0oKVxuICAgIHJlamVjdGVkX3JhdGlvID0gKHBvbGljeV9yZWplY3RlZF9sb2dwcyAtIHJlZl9yZWplY3RlZF9sb2dwcykubWVhbigpLml0ZW0oKVxuICAgIG1ldHJpY3MgPSB7XG4gICAgICAgIFwic3RlcFwiOiBzdGVwLFxuICAgICAgICBcImNob3Nlbl9sb2dwX3JhdGlvXCI6IGNob3Nlbl9yYXRpbyxcbiAgICAgICAgXCJyZWplY3RlZF9sb2dwX3JhdGlvXCI6IHJlamVjdGVkX3JhdGlvLFxuICAgICAgICBcIm1hcmdpblwiOiBjaG9zZW5fcmF0aW8gLSByZWplY3RlZF9yYXRpbyxcbiAgICB9XG4gICAgaGlzdG9yeS5hcHBlbmQobWV0cmljcylcbiAgICBpZiBsZW4oaGlzdG9yeSkgXHUwMDNlIDEwOlxuICAgICAgICByZWNlbnQgPSBucC5tZWFuKFtoW1wiY2hvc2VuX2xvZ3BfcmF0aW9cIl0gZm9yIGggaW4gaGlzdG9yeVstNTpdXSlcbiAgICAgICAgZWFybGllciA9IG5wLm1lYW4oW2hbXCJjaG9zZW5fbG9ncF9yYXRpb1wiXSBmb3IgaCBpbiBoaXN0b3J5Wy0xMDotNV1dKVxuICAgICAgICBpZiByZWNlbnQgXHUwMDNjIGVhcmxpZXI6XG4gICAgICAgICAgICBwcmludChmXCJbU3RlcCB7c3RlcH1dIFdBUk5JTkc6IENob3NlbiBsb2ctcHJvYiByYXRpbyBkZWNyZWFzaW5nIOKAlCBjaGVjayBMUlwiKVxuICAgIHJldHVybiBtZXRyaWNzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUFBPLVJMSEYgdnMgRFBPIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXNwZWN0IiwiUFBPLVJMSEYiLCJEUE8iXSwicm93cyI6W1siTW9kZWxzIG5lZWRlZCIsIjQgKHBvbGljeSwgcmVmZXJlbmNlLCByZXdhcmQgbW9kZWwsIHZhbHVlKSIsIjIgKHBvbGljeSwgZnJvemVuIHJlZmVyZW5jZSkiXSxbIkNvbXB1dGUiLCJIaWdoIOKAlCBvbmxpbmUgcm9sbG91dHMgYW5kIFJNIHNjb3JpbmcgZWFjaCBzdGVwIiwiTG93IOKAlCBvZmZsaW5lIHN1cGVydmlzZWQgdHJhaW5pbmcgb25seSJdLFsiRGF0YSByZXF1aXJlbWVudCIsIlByZWZlcmVuY2UgbGFiZWxzIHBsdXMgcHJvbXB0cyBmb3Igcm9sbG91dHMiLCJQYWlyZWQgKGNob3NlbiwgcmVqZWN0ZWQpIGNvbXBsZXRpb25zIl0sWyJUcmFpbmluZyBzdGFiaWxpdHkiLCJVbnN0YWJsZSAocmV3YXJkIGhhY2tpbmcsIEtMIGV4cGxvc2lvbiBwb3NzaWJsZSkiLCJTdGFibGUgKGNyb3NzLWVudHJvcHkgc3R5bGUgbG9zcykiXSxbIlJld2FyZCBnZW5lcmFsaXphdGlvbiIsIkJldHRlciDigJQgZXhwbGljaXQgUk0gdHJhaW5lZCBvbiB2YXJpZWQgcHJvbXB0cyIsIldlYWtlciDigJQgaW1wbGljaXQsIG9mZmxpbmUsIG5vIG9ubGluZSBzaWduYWwiXSxbIlBlcmZvcm1hbmNlIiwiSGlnaGVyIGNlaWxpbmcgd2l0aCBjb21wdXRlIGFuZCBzY2FsZSIsIkNvbXBldGl0aXZlIGF0IG1vZGVyYXRlIHNjYWxlIGFuZCBkYXRhIGJ1ZGdldCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRFBPIFZhcmlhbnRzIGFuZCBMaW1pdGF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2V2ZXJhbCBEUE8gdmFyaWFudHMgYWRkcmVzcyBpdHMgY29yZSBsaW1pdGF0aW9uczogcmVsaWFuY2Ugb24gcGFpcmVkIHByZWZlcmVuY2VzLCBubyBvbmxpbmUgbGVhcm5pbmcgY2FwYWJpbGl0eSwgYW5kIHdlYWtlciByZXdhcmQgZ2VuZXJhbGl6YXRpb24gY29tcGFyZWQgdG8gYW4gZXhwbGljaXQgcmV3YXJkIG1vZGVsLiBFYWNoIHZhcmlhbnQgbWFrZXMgYSBkaWZmZXJlbnQgdHJhZGVvZmYgYmV0d2VlbiBkYXRhIHJlcXVpcmVtZW50cywgY29tcHV0ZSwgYW5kIGFsaWdubWVudCBxdWFsaXR5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiSVBPIChJZGVudGl0eSBQcmVmZXJlbmNlIE9wdGltaXphdGlvbik6IGFkZHMgYSByZWd1bGFyaXphdGlvbiB0ZXJtIHRvIHByZXZlbnQgb3ZlcmZpdHRpbmcgdG8gcHJlZmVyZW5jZSBwYWlycyB3aGVuIGRhdGEgaXMgc2NhcmNlIiwiT1JQTyAoT2RkcyBSYXRpbyBQcmVmZXJlbmNlIE9wdGltaXphdGlvbik6IHJlcGxhY2VzIHRoZSByZWZlcmVuY2UgbW9kZWwgd2l0aCBhbiBvZGRzIHJhdGlvLCBlbmFibGluZyBzaW5nbGUtbW9kZWwgdHJhaW5pbmciLCJTaW1QTyAoU2ltcGxlIFByZWZlcmVuY2UgT3B0aW1pemF0aW9uKTogbGVuZ3RoLW5vcm1hbGl6ZWQgcmV3YXJkIG1hcmdpbiB3aXRob3V0IHJlcXVpcmluZyBhIHNlcGFyYXRlIHJlZmVyZW5jZSBtb2RlbCIsIk9ubGluZSBEUE86IHBlcmlvZGljYWxseSByZWdlbmVyYXRlcyBwcmVmZXJlbmNlIHBhaXJzIHVzaW5nIHRoZSBjdXJyZW50IHBvbGljeSB0byBlbmFibGUgb25saW5lIGxlYXJuaW5nIGFuZCBkaXN0cmlidXRpb24gc2hpZnQiLCJLVE8gKEthaG5lbWFuLVR2ZXJza3kgT3B0aW1pemF0aW9uKTogYWxpZ25zIGZyb20gYmluYXJ5IGdvb2QvYmFkIGZlZWRiYWNrIHdpdGhvdXQgcmVxdWlyaW5nIHBhaXJlZCBjb21wYXJpc29ucyJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiVGlwIiwiY29udGVudCI6IkRQT1x1MDAyN3MgaW1wbGljaXQgcmV3YXJkIGJldGEgKiBsb2dbcGlfdGhldGEoeXx4KSAvIHBpX3JlZih5fHgpXSBjYW4gYmUgbmVnYXRpdmUgaWYgdGhlIHBvbGljeSBoYXMgYmVlbiBwdXNoZWQgYXdheSBmcm9tIHNvbWUgcmVzcG9uc2VzIGR1cmluZyBTRlQg4oCUIGFsd2F5cyBpbml0aWFsaXplIERQTyBmcm9tIHRoZSBTRlQgY2hlY2twb2ludCB0aGF0IGdlbmVyYXRlZCB0aGUgcHJlZmVyZW5jZSBkYXRhIHRvIGF2b2lkIGRpc3RyaWJ1dGlvbiBtaXNtYXRjaC4gVXNpbmcgYSBkaWZmZXJlbnQgU0ZUIGNoZWNrcG9pbnQgZnJvbSB0aGUgb25lIHRoYXQgcHJvZHVjZWQgdGhlIHByZWZlcmVuY2UgcGFpcnMgY2F1c2VzIHJlZmVyZW5jZSBsb2ctcHJvYnMgdG8gYmUgbWlzY2FsaWJyYXRlZCBhbmQgZGVzdGFiaWxpemVzIHRyYWluaW5nLiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRQTyBoYXMgYmVjb21lIHRoZSBwcmVmZXJyZWQgYWxpZ25tZW50IG1ldGhvZCBmb3IgYWNhZGVtaWMgYW5kIHNtYWxsLXNjYWxlIHByb2R1Y3Rpb24gc2V0dGluZ3MgZHVlIHRvIGl0cyBzaW1wbGljaXR5LCBzdGFiaWxpdHksIGFuZCBjb21wZXRpdGl2ZSBwZXJmb3JtYW5jZS4gSXRzIG1haW4gbGltaXRhdGlvbiDigJQgb2ZmbGluZS1vbmx5IGxlYXJuaW5nIGZyb20gZml4ZWQgcHJlZmVyZW5jZSBkYXRhc2V0cyDigJQgaXMgYWRkcmVzc2VkIGJ5IG9ubGluZSBEUE8gdmFyaWFudHMgdGhhdCBwZXJpb2RpY2FsbHkgcmVnZW5lcmF0ZSBwcmVmZXJlbmNlIHBhaXJzIGZyb20gdGhlIGN1cnJlbnQgcG9saWN5LCBjb21iaW5pbmcgdGhlIHN0YWJpbGl0eSBvZiBEUE8gd2l0aCB0aGUgb25saW5lIGxlYXJuaW5nIGJlbmVmaXRzIG9mIFBQTy1STEhGLiJ9XQ=="
---
# DPO — Direct Preference Optimization Without the RL Loop

DPO (Direct Preference Optimization, Rafailov et al. 2023) eliminates the reward model and RL training loop entirely. By deriving a closed-form relationship between the optimal policy, the reference policy, and human preferences, DPO converts RLHF into a supervised classification problem over preference pairs — making alignment training substantially more stable and computationally efficient than PPO-RLHF.

## DPO Derivation from Optimal Policy

DPO starts from the KL-constrained RL objective: max_pi E[r(x,y)] - beta * KL[pi || pi_ref]. The optimal policy satisfies pi*(y|x) proportional to pi_ref(y|x) * exp(r*(x,y)/beta). Rearranging: r*(x,y) = beta * log[pi*(y|x) / pi_ref(y|x)] + beta * log Z(x). Substituting into the Bradley-Terry preference model eliminates both r* and the partition function Z(x), yielding the DPO loss directly from paired preferences (x, y_w, y_l) without ever training a reward model.

## DPO Loss Implementation

```python
import torch
import torch.nn.functional as F
from typing import Tuple

def dpo_loss(
    policy_chosen_logps: torch.Tensor,
    policy_rejected_logps: torch.Tensor,
    ref_chosen_logps: torch.Tensor,
    ref_rejected_logps: torch.Tensor,
    beta: float = 0.1,
) -> Tuple[torch.Tensor, dict]:
    # DPO loss: -E[log sigma(beta * (log_ratio_chosen - log_ratio_rejected))]
    # Log ratio: log[pi_theta(y|x) / pi_ref(y|x)]
    chosen_log_ratio = policy_chosen_logps - ref_chosen_logps
    rejected_log_ratio = policy_rejected_logps - ref_rejected_logps
    logits = beta * (chosen_log_ratio - rejected_log_ratio)
    loss = -F.logsigmoid(logits).mean()
    # Implicit rewards for monitoring preference alignment
    chosen_rewards = beta * chosen_log_ratio.detach()
    rejected_rewards = beta * rejected_log_ratio.detach()
    reward_margin = (chosen_rewards - rejected_rewards).mean().item()
    accuracy = (logits > 0).float().mean().item()
    return loss, {
        "reward_margin": reward_margin,
        "dpo_accuracy": accuracy,
        "chosen_reward": chosen_rewards.mean().item(),
        "rejected_reward": rejected_rewards.mean().item(),
    }
```

## DPO Training Loop

The DPO training setup requires only two models: the frozen reference pi_ref (the SFT checkpoint) and the trainable policy pi_theta. Both models forward-pass through each sequence to compute log-probabilities, but only the policy receives gradient updates. The reference model serves as a soft constraint preventing the policy from drifting too far from natural language distributions.

```python
import torch
from transformers import AutoModelForCausalLM
from torch.optim import AdamW
from typing import Tuple

def get_sequence_logps(model, input_ids, attention_mask, labels, device):
    outputs = model(
        input_ids=input_ids.to(device),
        attention_mask=attention_mask.to(device),
    )
    logits = outputs.logits[:, :-1]  # shift for next-token prediction
    log_probs = torch.log_softmax(logits, dim=-1)
    token_logps = log_probs.gather(2, labels[:, 1:].to(device).unsqueeze(2)).squeeze(2)
    label_mask = (labels[:, 1:].to(device) != -100).float()
    return (token_logps * label_mask).sum(dim=1) / label_mask.sum(dim=1).clamp(min=1)

def dpo_training_step(policy_model, ref_model, batch, optimizer, beta=0.1, device="cuda"):
    # Forward both chosen and rejected through policy and frozen reference
    optimizer.zero_grad()
    p_chosen = get_sequence_logps(
        policy_model, batch["chosen_ids"], batch["chosen_mask"], batch["chosen_labels"], device
    )
    p_rejected = get_sequence_logps(
        policy_model, batch["rejected_ids"], batch["rejected_mask"], batch["rejected_labels"], device
    )
    with torch.no_grad():
        r_chosen = get_sequence_logps(
            ref_model, batch["chosen_ids"], batch["chosen_mask"], batch["chosen_labels"], device
        )
        r_rejected = get_sequence_logps(
            ref_model, batch["rejected_ids"], batch["rejected_mask"], batch["rejected_labels"], device
        )
    loss, metrics = dpo_loss(p_chosen, p_rejected, r_chosen, r_rejected, beta)
    loss.backward()
    optimizer.step()
    return metrics
```

## Implicit Reward

DPO's implicit reward beta * log[pi_theta(y|x) / pi_ref(y|x)] emerges from the policy's log-probability ratio with the reference. This reward is not explicitly trained — it arises as a natural consequence of the policy learning to prefer chosen responses over rejected ones. Monitoring this implicit reward during training helps diagnose whether DPO is learning meaningful preferences or overfitting to surface artifacts.

```python
import torch

def compute_dpo_implicit_reward(
    policy_model,
    ref_model,
    input_ids: torch.Tensor,
    attention_mask: torch.Tensor,
    labels: torch.Tensor,
    beta: float = 0.1,
    device: str = "cuda",
) -> torch.Tensor:
    # DPO implicit reward: beta * log[pi_theta(y|x) / pi_ref(y|x)]
    def sequence_logps(model, ids, mask, lbls):
        with torch.no_grad():
            out = model(
                input_ids=ids.to(device), attention_mask=mask.to(device)
            )
            lp = torch.log_softmax(out.logits[:, :-1], dim=-1)
            tok_lp = lp.gather(2, lbls[:, 1:].to(device).unsqueeze(2)).squeeze(2)
            lbl_mask = (lbls[:, 1:].to(device) != -100).float()
            return (tok_lp * lbl_mask).sum(1) / lbl_mask.sum(1).clamp(min=1)
    policy_logps = sequence_logps(policy_model, input_ids, attention_mask, labels)
    ref_logps = sequence_logps(ref_model, input_ids, attention_mask, labels)
    # Positive value means policy assigns higher probability than reference
    return beta * (policy_logps - ref_logps)  # [batch]
```

## Monitoring Chosen vs Rejected Log-Probabilities

During successful DPO training, the log-probability ratio for chosen responses should increase while the ratio for rejected responses decreases. The margin (chosen_ratio - rejected_ratio) is the most diagnostic signal — a stagnant or decreasing margin indicates the policy is not learning to distinguish preferences. Track both ratios at every step; if chosen_ratio decreases over any 5-step window, reduce the learning rate.

```python
import numpy as np
import torch

def monitor_dpo_logprob_evolution(
    policy_chosen_logps: torch.Tensor,
    policy_rejected_logps: torch.Tensor,
    ref_chosen_logps: torch.Tensor,
    ref_rejected_logps: torch.Tensor,
    step: int,
    history: list,
) -> dict:
    # Track log-prob ratios during DPO training to detect divergence
    chosen_ratio = (policy_chosen_logps - ref_chosen_logps).mean().item()
    rejected_ratio = (policy_rejected_logps - ref_rejected_logps).mean().item()
    metrics = {
        "step": step,
        "chosen_logp_ratio": chosen_ratio,
        "rejected_logp_ratio": rejected_ratio,
        "margin": chosen_ratio - rejected_ratio,
    }
    history.append(metrics)
    if len(history) > 10:
        recent = np.mean([h["chosen_logp_ratio"] for h in history[-5:]])
        earlier = np.mean([h["chosen_logp_ratio"] for h in history[-10:-5]])
        if recent < earlier:
            print(f"[Step {step}] WARNING: Chosen log-prob ratio decreasing — check LR")
    return metrics
```

## PPO-RLHF vs DPO Comparison

| Aspect | PPO-RLHF | DPO |
| --- | --- | --- |
| Models needed | 4 (policy, reference, reward model, value) | 2 (policy, frozen reference) |
| Compute | High — online rollouts and RM scoring each step | Low — offline supervised training only |
| Data requirement | Preference labels plus prompts for rollouts | Paired (chosen, rejected) completions |
| Training stability | Unstable (reward hacking, KL explosion possible) | Stable (cross-entropy style loss) |
| Reward generalization | Better — explicit RM trained on varied prompts | Weaker — implicit, offline, no online signal |
| Performance | Higher ceiling with compute and scale | Competitive at moderate scale and data budget |

## DPO Variants and Limitations

Several DPO variants address its core limitations: reliance on paired preferences, no online learning capability, and weaker reward generalization compared to an explicit reward model. Each variant makes a different tradeoff between data requirements, compute, and alignment quality.

- IPO (Identity Preference Optimization): adds a regularization term to prevent overfitting to preference pairs when data is scarce
- ORPO (Odds Ratio Preference Optimization): replaces the reference model with an odds ratio, enabling single-model training
- SimPO (Simple Preference Optimization): length-normalized reward margin without requiring a separate reference model
- Online DPO: periodically regenerates preference pairs using the current policy to enable online learning and distribution shift
- KTO (Kahneman-Tversky Optimization): aligns from binary good/bad feedback without requiring paired comparisons

> **Tip**: DPO's implicit reward beta * log[pi_theta(y|x) / pi_ref(y|x)] can be negative if the policy has been pushed away from some responses during SFT — always initialize DPO from the SFT checkpoint that generated the preference data to avoid distribution mismatch. Using a different SFT checkpoint from the one that produced the preference pairs causes reference log-probs to be miscalibrated and destabilizes training.

---

DPO has become the preferred alignment method for academic and small-scale production settings due to its simplicity, stability, and competitive performance. Its main limitation — offline-only learning from fixed preference datasets — is addressed by online DPO variants that periodically regenerate preference pairs from the current policy, combining the stability of DPO with the online learning benefits of PPO-RLHF.

