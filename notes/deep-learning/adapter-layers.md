---
title: "Adapter Layers — Bottleneck Modules Between Transformer Layers"
slug: "adapter-layers"
description: "Adapter layers (Houlsby et al., 2019) insert small bottleneck FFN modules between transformer sub-layers. Covers the bottleneck architecture, near-identity initialization, serial vs parallel variants, Compacter, AdapterHub, adapter stacking, adapter fusion, and training procedure."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWRhcHRlciBsYXllcnMgKEhvdWxzYnkgZXQgYWwuLCAyMDE5KSBhcmUgc21hbGwgYm90dGxlbmVjayBmZWVkLWZvcndhcmQgbW9kdWxlcyBpbnNlcnRlZCBiZXR3ZWVuIHN1Yi1sYXllcnMgb2YgYSBmcm96ZW4gcHJldHJhaW5lZCB0cmFuc2Zvcm1lci4gT25seSB0aGUgYWRhcHRlciBwYXJhbWV0ZXJzIGFyZSB0cmFpbmVkOyBhbGwgb3JpZ2luYWwgd2VpZ2h0cyByZW1haW4gZml4ZWQuIFRoaXMgYWxsb3dzIGEgc2luZ2xlIGxhcmdlIHByZXRyYWluZWQgbW9kZWwgdG8gc3VwcG9ydCBtYW55IHRhc2tzIHNpbXVsdGFuZW91c2x5OiBkaWZmZXJlbnQgYWRhcHRlcnMgYXJlIGxvYWRlZCBwZXIgdGFzayB3aGlsZSB0aGUgYmFja2JvbmUgaXMgc2hhcmVkLiBBZGFwdGVycyBhcmUgdGhlIGVhcmxpZXN0IGFuZCBtb3N0IHdpZGVseSBzdHVkaWVkIFBFRlQgbWV0aG9kLCBwcmVkYXRpbmcgTG9SQSwgYW5kIHRoZWlyIG1vZHVsYXIgZGVzaWduIGhhcyBzcGF3bmVkIGFuIGVjb3N5c3RlbSBvZiB2YXJpYW50cyBhbmQgdG9vbGluZyBpbmNsdWRpbmcgQWRhcHRlckh1YiwgYSBwdWJsaWMgcmVnaXN0cnkgd2l0aCA0MDArIHByZXRyYWluZWQgYWRhcHRlcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQm90dGxlbmVjayBBcmNoaXRlY3R1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVhY2ggYWRhcHRlciBhcHBsaWVzIHRoZSBmdW5jdGlvbjogYWRhcHRlcihoKSA9IGggKyBXX3VwKM+DKFdfZG93bihMYXllck5vcm0oaCkpKSkgd2hlcmUgV19kb3duIOKIiCDihJ1eKGTDl20pIGlzIHRoZSBkb3duLXByb2plY3Rpb24gYW5kIFdfdXAg4oiIIOKEnV4obcOXZCkgaXMgdGhlIHVwLXByb2plY3Rpb24uIFRoZSBib3R0bGVuZWNrIGRpbWVuc2lvbiBtIGNvbnRyb2xzIHRoZSBjYXBhY2l0eSBhbmQgcGFyYW1ldGVyIGNvdW50LiBUeXBpY2FsIHZhbHVlczogbSDiiIggezgsIDE2LCAzMiwgNjR9LiBUaGUgcmVzaWR1YWwgY29ubmVjdGlvbiAoaCArKSBlbnN1cmVzIHRoYXQgd2hlbiBXX3VwIGlzIGluaXRpYWxpemVkIG5lYXIgemVybywgdGhlIGFkYXB0ZXIgb3V0cHV0IGlzIGFwcHJveGltYXRlbHkgaC4gRm9yIHRoZSBIb3Vsc2J5IGRlc2lnbiwgdHdvIGFkYXB0ZXJzIGFyZSBpbnNlcnRlZCBwZXIgdHJhbnNmb3JtZXIgbGF5ZXI6IG9uZSBhZnRlciB0aGUgc2VsZi1hdHRlbnRpb24gc3ViLWxheWVyIGFuZCBvbmUgYWZ0ZXIgdGhlIEZGTiBzdWItbGF5ZXIuIEZvciBCRVJULWJhc2UgKGQ9NzY4LCAxMiBsYXllcnMsIG09NjQpOiBwYXJhbXMgcGVyIGFkYXB0ZXIgPSAyw5c3NjjDlzY0ICsgMsOXNjQgYmlhc2VzID0gOTgsNDMyOyB0d28gYWRhcHRlcnMgcGVyIGxheWVyIMOXIDEyIGxheWVycyA9IDIuMzZNIHRvdGFsIOKAlCBhYm91dCAwLjklIG9mIEJFUlQtYmFzZVx1MDAyN3MgMTEwTSBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5lYXItSWRlbnRpdHkgSW5pdGlhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBuZWFyLWlkZW50aXR5IGluaXRpYWxpemF0aW9uIGlzIG5vdCBvcHRpb25hbCDigJQgaXQgaXMgdGhlIHByb3BlcnR5IHRoYXQgbWFrZXMgYWRhcHRlciBpbnNlcnRpb24gc2FmZSBmb3IgYSBwcmV0cmFpbmVkIG1vZGVsLiBXaGVuIFdfdXAgaXMgaW5pdGlhbGl6ZWQgd2l0aCB2YWx1ZXMgbmVhciB6ZXJvIChlLmcuLCBOKDAsIDAuMDAxKSksIHRoZSBhZGFwdGVyIGNvbnRyaWJ1dGlvbiBXX3VwKM+DKFdfZG93bihoKSkpIOKJiCAwLCBzbyB0aGUgYWRhcHRlciBvdXRwdXQg4omIIGguIFRoZSBwcmV0cmFpbmVkIG1vZGVsXHUwMDI3cyBwcmVkaWN0aW9ucyBhcmUgcHJlc2VydmVkIGF0IHRoZSBzdGFydCBvZiB0cmFpbmluZy4gV2l0aG91dCBuZWFyLWlkZW50aXR5IGluaXQsIGluc2VydGluZyBhZGFwdGVycyBpbnRvIGEgcHJldHJhaW5lZCBCRVJUIGFuZCBldmFsdWF0aW5nIG9uIGFueSBkb3duc3RyZWFtIHRhc2sgYmVmb3JlIHRyYWluaW5nIGdpdmVzIHJhbmRvbSBvdXRwdXRzLiBUaGlzIGluaXRpYWxpemF0aW9uIGFsc28gbWFrZXMgdGhlIGFkYXB0ZXJcdTAwMjdzIG9wdGltaXphdGlvbiB3ZWxsLWNvbmRpdGlvbmVkOiB0aGUgdGFzayBsb3NzIHN0YXJ0cyBhdCB0aGUgcHJldHJhaW5lZCBtb2RlbFx1MDAyN3MgbG9zcywgYW5kIHRoZSBhZGFwdGVycyBncmFkdWFsbHkgZGl2ZXJnZSB0b3dhcmQgYSB0YXNrLXNwZWNpZmljIGNvbmZpZ3VyYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWRhcHRlciBMYXllciBJbXBsZW1lbnRhdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuY2xhc3MgQWRhcHRlckxheWVyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiXG4gICAgQm90dGxlbmVjayBhZGFwdGVyOiBMYXllck5vcm0gLVx1MDAzZSBkb3duLXByb2plY3QgLVx1MDAzZSBhY3RpdmF0ZSAtXHUwMDNlIHVwLXByb2plY3QgLVx1MDAzZSByZXNpZHVhbC5cbiAgICBOZWFyLWlkZW50aXR5IGF0IGluaXQ6IFdfdXAgaW5pdGlhbGl6ZWQgbmVhciB6ZXJvLlxuICAgIFwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgYm90dGxlbmVja19kaW06IGludCxcbiAgICAgICAgICAgICAgICAgYWN0aXZhdGlvbjogc3RyID0gXHUwMDI3Z2VsdVx1MDAyNywgZHJvcG91dDogZmxvYXQgPSAwLjApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5sYXllcl9ub3JtID0gbm4uTGF5ZXJOb3JtKGRfbW9kZWwpXG4gICAgICAgIHNlbGYuZG93bl9wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGJvdHRsZW5lY2tfZGltKVxuICAgICAgICBzZWxmLnVwX3Byb2ogICA9IG5uLkxpbmVhcihib3R0bGVuZWNrX2RpbSwgZF9tb2RlbClcbiAgICAgICAgc2VsZi5kcm9wb3V0ICAgPSBubi5Ecm9wb3V0KGRyb3BvdXQpXG4gICAgICAgIHNlbGYuYWN0ID0gbm4uR0VMVSgpIGlmIGFjdGl2YXRpb24gPT0gXHUwMDI3Z2VsdVx1MDAyNyBlbHNlIG5uLlJlTFUoKVxuICAgICAgICBzZWxmLl9uZWFyX2lkZW50aXR5X2luaXQoKVxuXG4gICAgZGVmIF9uZWFyX2lkZW50aXR5X2luaXQoc2VsZik6XG4gICAgICAgIFwiXCJcIkluaXRpYWxpemUgV191cCBuZWFyIHplcm8gc28gYWRhcHRlciBvdXRwdXQg4omIIGlucHV0IGF0IHN0YXJ0LlwiXCJcIlxuICAgICAgICBubi5pbml0LmthaW1pbmdfdW5pZm9ybV8oc2VsZi5kb3duX3Byb2oud2VpZ2h0LCBhPW1hdGguc3FydCg1KSlcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5kb3duX3Byb2ouYmlhcylcbiAgICAgICAgbm4uaW5pdC5ub3JtYWxfKHNlbGYudXBfcHJvai53ZWlnaHQsIG1lYW49MC4wLCBzdGQ9MWUtMylcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi51cF9wcm9qLmJpYXMpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBoaWRkZW46IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIHJlc2lkdWFsID0gaGlkZGVuXG4gICAgICAgIGggPSBzZWxmLmxheWVyX25vcm0oaGlkZGVuKVxuICAgICAgICBoID0gc2VsZi5kb3duX3Byb2ooaClcbiAgICAgICAgaCA9IHNlbGYuYWN0KGgpXG4gICAgICAgIGggPSBzZWxmLmRyb3BvdXQoaClcbiAgICAgICAgaCA9IHNlbGYudXBfcHJvaihoKVxuICAgICAgICByZXR1cm4gcmVzaWR1YWwgKyBoXG5cbmFkYXB0ZXIgPSBBZGFwdGVyTGF5ZXIoZF9tb2RlbD03NjgsIGJvdHRsZW5lY2tfZGltPTY0KVxueCA9IHRvcmNoLnJhbmRuKDIsIDEwLCA3NjgpXG5vdXQgPSBhZGFwdGVyKHgpXG5tYXhfZGlmZiA9IChvdXQgLSB4KS5hYnMoKS5tYXgoKS5pdGVtKClcbnByaW50KGZcdTAwMjdNYXggZGV2aWF0aW9uIGZyb20gaWRlbnRpdHkgYXQgaW5pdDoge21heF9kaWZmOi42Zn1cdTAwMjcpICAjIHNob3VsZCBiZSB+MFxucHJpbnQoZlx1MDAyN0FkYXB0ZXIgdHJhaW5hYmxlIHBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gYWRhcHRlci5wYXJhbWV0ZXJzKCkpOix9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkluamVjdGluZyBBZGFwdGVycyBpbnRvIGEgVHJhbnNmb3JtZXIifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBCZXJ0TW9kZWwsIEJlcnRDb25maWdcblxuY2xhc3MgQmVydExheWVyV2l0aEFkYXB0ZXJzKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiV3JhcCBhIEJFUlQgbGF5ZXIgdG8gaW5zZXJ0IEhvdWxzYnktc3R5bGUgYWRhcHRlcnMgYWZ0ZXIgYXR0ZW50aW9uIGFuZCBGRk4uXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmVydF9sYXllciwgZF9tb2RlbDogaW50ID0gNzY4LCBib3R0bGVuZWNrX2RpbTogaW50ID0gNjQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5iZXJ0X2xheWVyID0gYmVydF9sYXllclxuICAgICAgICBmb3IgcGFyYW0gaW4gc2VsZi5iZXJ0X2xheWVyLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgICAgIHBhcmFtLnJlcXVpcmVzX2dyYWQgPSBGYWxzZVxuICAgICAgICBzZWxmLmFkYXB0ZXJfYXR0biA9IEFkYXB0ZXJMYXllcihkX21vZGVsLCBib3R0bGVuZWNrX2RpbSlcbiAgICAgICAgc2VsZi5hZGFwdGVyX2ZmbiAgPSBBZGFwdGVyTGF5ZXIoZF9tb2RlbCwgYm90dGxlbmVja19kaW0pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBoaWRkZW5fc3RhdGVzLCBhdHRlbnRpb25fbWFzaz1Ob25lKTpcbiAgICAgICAgYXR0bl9vdXQgPSBzZWxmLmJlcnRfbGF5ZXIuYXR0ZW50aW9uKGhpZGRlbl9zdGF0ZXMsIGF0dGVudGlvbl9tYXNrKVxuICAgICAgICBoaWRkZW5fc3RhdGVzID0gc2VsZi5hZGFwdGVyX2F0dG4oYXR0bl9vdXRbMF0pXG4gICAgICAgIGludGVybWVkaWF0ZSA9IHNlbGYuYmVydF9sYXllci5pbnRlcm1lZGlhdGUoaGlkZGVuX3N0YXRlcylcbiAgICAgICAgZmZuX291dCA9IHNlbGYuYmVydF9sYXllci5vdXRwdXQoaW50ZXJtZWRpYXRlLCBoaWRkZW5fc3RhdGVzKVxuICAgICAgICBoaWRkZW5fc3RhdGVzID0gc2VsZi5hZGFwdGVyX2ZmbihmZm5fb3V0KVxuICAgICAgICByZXR1cm4gKGhpZGRlbl9zdGF0ZXMsKVxuXG5kZWYgaW5qZWN0X2FkYXB0ZXJzKG1vZGVsX25hbWU6IHN0ciA9IFx1MDAyN2JlcnQtYmFzZS11bmNhc2VkXHUwMDI3LFxuICAgICAgICAgICAgICAgICAgICBib3R0bGVuZWNrX2RpbTogaW50ID0gNjQpOlxuICAgIGNvbmZpZyA9IEJlcnRDb25maWcuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG4gICAgYmVydCA9IEJlcnRNb2RlbC5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSlcbiAgICBmb3IgaSwgbGF5ZXIgaW4gZW51bWVyYXRlKGJlcnQuZW5jb2Rlci5sYXllcik6XG4gICAgICAgIGJlcnQuZW5jb2Rlci5sYXllcltpXSA9IEJlcnRMYXllcldpdGhBZGFwdGVycyhcbiAgICAgICAgICAgIGxheWVyLCBjb25maWcuaGlkZGVuX3NpemUsIGJvdHRsZW5lY2tfZGltXG4gICAgICAgIClcbiAgICB0cmFpbmFibGUgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIGJlcnQucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZClcbiAgICB0b3RhbCA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gYmVydC5wYXJhbWV0ZXJzKCkpXG4gICAgcHJpbnQoZlx1MDAyN1RyYWluYWJsZToge3RyYWluYWJsZTosfSAvIHt0b3RhbDosfSAoezEwMCp0cmFpbmFibGUvdG90YWw6LjJmfSUpXHUwMDI3KVxuICAgIHJldHVybiBiZXJ0XG5cbnByaW50KFx1MDAyN0hvdWxzYnkgZGVzaWduOiAyIGFkYXB0ZXJzIHBlciBsYXllciwgZnJlZXplIGJhY2tib25lLCB0cmFpbiBhZGFwdGVycyBvbmx5Llx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZGFwdGVySHViIEludGVncmF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXJcbmZyb20gYWRhcHRlcnMgaW1wb3J0IEF1dG9BZGFwdGVyTW9kZWxcblxuZGVmIGxvYWRfcHJldHJhaW5lZF9hZGFwdGVyKHRhc2s6IHN0ciA9IFx1MDAyN3NlbnRpbWVudFx1MDAyNyk6XG4gICAgXCJcIlwiXG4gICAgTG9hZCBhIHByZXRyYWluZWQgYWRhcHRlciBmcm9tIEFkYXB0ZXJIdWIgZm9yIGEgc3BlY2lmaWMgdGFzay5cbiAgICBBZGFwdGVySHViIGhvc3RzIHRhc2stc3BlY2lmaWMgYWRhcHRlcnMgZm9yIEJFUlQsIFJvQkVSVGEsIFQ1LCBYTE0tUi5cbiAgICBcIlwiXCJcbiAgICBtb2RlbCA9IEF1dG9BZGFwdGVyTW9kZWwuZnJvbV9wcmV0cmFpbmVkKFx1MDAyN2JlcnQtYmFzZS11bmNhc2VkXHUwMDI3KVxuICAgIHRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFx1MDAyN2JlcnQtYmFzZS11bmNhc2VkXHUwMDI3KVxuICAgIGFkYXB0ZXJfbmFtZSA9IG1vZGVsLmxvYWRfYWRhcHRlcihcbiAgICAgICAgXHUwMDI3QWRhcHRlckh1Yi9iZXJ0LWJhc2UtdW5jYXNlZC1wZi1zc3QyXHUwMDI3LFxuICAgICAgICBzb3VyY2U9XHUwMDI3aGZcdTAwMjcsXG4gICAgICAgIHNldF9hY3RpdmU9VHJ1ZVxuICAgIClcbiAgICBtb2RlbC5zZXRfYWN0aXZlX2FkYXB0ZXJzKGFkYXB0ZXJfbmFtZSlcbiAgICB0cmFpbmFibGUgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWQpXG4gICAgcHJpbnQoZlx1MDAyN0FjdGl2ZSBhZGFwdGVyOiB7YWRhcHRlcl9uYW1lfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3VHJhaW5hYmxlIHBhcmFtczoge3RyYWluYWJsZTosfVx1MDAyNylcbiAgICBpbnB1dHMgPSB0b2tlbml6ZXIoXHUwMDI3VGhlIGZpbG0gd2FzIGEgbWFzdGVycGllY2UuXHUwMDI3LCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNylcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgbG9naXRzID0gbW9kZWwoKippbnB1dHMpLmxvZ2l0c1xuICAgIHByaW50KGZcdTAwMjdMb2dpdHMgc2hhcGU6IHtsb2dpdHMuc2hhcGV9XHUwMDI3KVxuICAgIHJldHVybiBtb2RlbFxuXG5wcmludChcdTAwMjdBZGFwdGVySHViOiA0MDArIHByZXRyYWluZWQgYWRhcHRlcnM7IGxvYWQgaW4gMiBsaW5lcyBvZiBjb2RlLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZGFwdGVyIEZ1c2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWRhcHRlciBmdXNpb24gKFBmZWlmZmVyIGV0IGFsLiwgMjAyMSkgY29tYmluZXMgb3V0cHV0cyBmcm9tIEsgaW5kZXBlbmRlbnRseSB0cmFpbmVkIHRhc2stc3BlY2lmaWMgYWRhcHRlcnMgdmlhIGxlYXJuZWQgYXR0ZW50aW9uIHdlaWdodHMgYXQgaW5mZXJlbmNlIHRpbWUuIEVhY2ggYWRhcHRlciB3YXMgdHJhaW5lZCBvbiBhIGRpZmZlcmVudCBzb3VyY2UgdGFzayAoZS5nLiwgTkxJLCBRQSwgc2VudGltZW50KS4gRm9yIGEgbmV3IHRhcmdldCB0YXNrLCB0aGUgYWRhcHRlciB3ZWlnaHRzIGFyZSBmcm96ZW4gYW5kIG9ubHkgdGhlIGZ1c2lvbiBhdHRlbnRpb24gd2VpZ2h0cyBhcmUgdHJhaW5lZC4gVGhpcyBhbGxvd3MgdGhlIG1vZGVsIHRvIGxlYXJuIHdoaWNoIHNvdXJjZS10YXNrIGFkYXB0ZXJzIGFyZSBtb3N0IHJlbGV2YW50IGZvciB0aGUgbmV3IHRhc2suIEZ1c2lvbiBpcyBhcHBsaWVkIGF0IGVhY2ggdHJhbnNmb3JtZXIgbGF5ZXI6IGEgbGVhcm5lZCBxdWVyeS1rZXkgYXR0ZW50aW9uIG92ZXIgYWRhcHRlciBvdXRwdXRzIHByb2R1Y2VzIGEgd2VpZ2h0ZWQgc3VtLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBBZGFwdGVyRnVzaW9uKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiXG4gICAgQ29tYmluZSBLIHRhc2stc3BlY2lmaWMgYWRhcHRlciBvdXRwdXRzIHZpYSBsZWFybmVkIGF0dGVudGlvbiB3ZWlnaHRpbmcuXG4gICAgQWRhcHRlciB3ZWlnaHRzIGFyZSBmcm96ZW47IG9ubHkgZnVzaW9uIGF0dGVudGlvbiB3ZWlnaHRzIGFyZSB0cmFpbmVkLlxuICAgIFwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgbl9hZGFwdGVyczogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucXVlcnkgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5rZXlzID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKG5fYWRhcHRlcnMsIGRfbW9kZWwpICogMC4wMilcbiAgICAgICAgc2VsZi5zY2FsZSA9IGRfbW9kZWwgKiogLTAuNVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgaGlkZGVuOiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgYWRhcHRlcl9vdXRwdXRzOiBsaXN0KSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgcSA9IHNlbGYucXVlcnkoaGlkZGVuKSAgICAgICAgICAgICAgICAgICAgICAjIChic3osIHNlcSwgZClcbiAgICAgICAgc2NvcmVzID0gdG9yY2guZWluc3VtKFx1MDAyN2JzZCxuZC1cdTAwM2Vic25cdTAwMjcsIHEsIHNlbGYua2V5cykgKiBzZWxmLnNjYWxlXG4gICAgICAgIHdlaWdodHMgPSB0b3JjaC5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKSAgICAgIyAoYnN6LCBzZXEsIG5fYWRhcHRlcnMpXG4gICAgICAgIHN0YWNrZWQgPSB0b3JjaC5zdGFjayhhZGFwdGVyX291dHB1dHMsIGRpbT0yKSAgIyAoYnN6LCBzZXEsIEssIGQpXG4gICAgICAgIGZ1c2VkID0gdG9yY2guZWluc3VtKFx1MDAyN2Jzbixic25kLVx1MDAzZWJzZFx1MDAyNywgd2VpZ2h0cywgc3RhY2tlZClcbiAgICAgICAgcmV0dXJuIGhpZGRlbiArIGZ1c2VkXG5cbmJzeiwgc2VxLCBkLCBLID0gMiwgMTAsIDc2OCwgM1xuZnVzaW9uID0gQWRhcHRlckZ1c2lvbihkX21vZGVsPWQsIG5fYWRhcHRlcnM9SylcbmhpZGRlbiA9IHRvcmNoLnJhbmRuKGJzeiwgc2VxLCBkKVxuYWRhcHRlcl9vdXRzID0gW3RvcmNoLnJhbmRuKGJzeiwgc2VxLCBkKSBmb3IgXyBpbiByYW5nZShLKV1cbm91dCA9IGZ1c2lvbihoaWRkZW4sIGFkYXB0ZXJfb3V0cylcbnByaW50KGZcdTAwMjdGdXNpb24gb3V0cHV0IHNoYXBlOiB7b3V0LnNoYXBlfVx1MDAyNykgICMgKDIsIDEwLCA3NjgpXG5mdXNpb25fdHJhaW5hYmxlID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBmdXNpb24ucGFyYW1ldGVycygpKVxucHJpbnQoZlx1MDAyN0Z1c2lvbiB0cmFpbmFibGUgcGFyYW1zOiB7ZnVzaW9uX3RyYWluYWJsZTosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZGFwdGVyIFZhcmlhbnRzIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmFyaWFudCIsIlBsYWNlbWVudCIsIlBhcmFtcyBwZXIgTGF5ZXIiLCJRdWFsaXR5IHZzIEZ1bGwgRlQiLCJNb2R1bGFyIChTd2FwIGF0IEluZmVyZW5jZSkiXSwicm93cyI6W1siSG91bHNieSAoc2VyaWFsKSIsIkFmdGVyIGF0dGVudGlvbiArIGFmdGVyIEZGTiAoMiBwZXIgbGF5ZXIpIiwiMiDDlyAyZG0iLCJ+OTklIiwiWWVzIl0sWyJQZmVpZmZlciAoc2VyaWFsLCBzaW5nbGUpIiwiQWZ0ZXIgRkZOIG9ubHkgKDEgcGVyIGxheWVyKSIsIjJkbSIsIn45OCUiLCJZZXMiXSxbIlBhcmFsbGVsIGFkYXB0ZXIgKFBBTHMpIiwiUGFyYWxsZWwgdG8gYXR0ZW50aW9uIHN1Yi1sYXllciIsIjJkbSIsIn45OCUiLCJZZXMiXSxbIkNvbXBhY3RlciIsIkFmdGVyIEZGTiwgS3JvbmVja2VyIHByb2R1Y3Qgd2VpZ2h0cyIsIn40w5cgc21hbGxlciB0aGFuIEhvdWxzYnkiLCJ+OTclIiwiWWVzIl0sWyJMb1JBLWFzLWFkYXB0ZXIiLCJJbiBRLCBWIHdlaWdodCBtYXRyaWNlcyAoYWRkaXRpdmUpIiwiMmRyIHBlciBtYXRyaXgiLCJ+OTklIiwiWWVzIChtZXJnZSBvciBzd2FwKSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWRhcHRlciBTdGFja2luZyBhbmQgQ29tcG9zaXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik11bHRpcGxlIGFkYXB0ZXJzIGNhbiBiZSBzdGFja2VkIHdpdGhpbiBhIHNpbmdsZSBsYXllcjogdGhlIG91dHB1dCBvZiBvbmUgYWRhcHRlciBmZWVkcyBpbnRvIHRoZSBuZXh0LiBUaGlzIGlzIHVzZWZ1bCBmb3IgY29tcG9zaW5nIGEgZ2VuZXJhbC1kb21haW4gYWRhcHRlciAoZS5nLiwgdHJhaW5lZCBvbiBXaWtpcGVkaWEpIHdpdGggYSB0YXNrLXNwZWNpZmljIGFkYXB0ZXIuIEFkYXB0ZXJIdWIgc3VwcG9ydHMgc3RhY2tpbmcgdmlhIGFkYXB0ZXIgY29tcG9zaXRpb24gcHJpbWl0aXZlczogU3RhY2soW2RvbWFpbl9hZGFwdGVyLCB0YXNrX2FkYXB0ZXJdKSBhcHBsaWVzIHRoZW0gc2VxdWVudGlhbGx5LiBBIHNpbXBsZXIgYWx0ZXJuYXRpdmUgaXMgYWRhcHRlciBhdmVyYWdpbmc6IHRha2UgdGhlIGVsZW1lbnQtd2lzZSBhdmVyYWdlIG9mIHR3byBhZGFwdGVyc1x1MDAyNyB3ZWlnaHQgbWF0cmljZXMgd2hlbiB0aGUgdGFza3MgYXJlIHJlbGF0ZWQuIFRoaXMgaGFzIGJlZW4gc2hvd24gdG8gb3V0cGVyZm9ybSBlaXRoZXIgc2luZ2xlIGFkYXB0ZXIgb24gY3Jvc3MtbGluZ3VhbCB0cmFuc2ZlciB0YXNrcyB3aXRob3V0IGFueSBhZGRpdGlvbmFsIHRyYWluaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIFByb2NlZHVyZSBhbmQgSHlwZXJwYXJhbWV0ZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZGFwdGVyIHRyYWluaW5nIGZvbGxvd3MgdGhlIHNhbWUgcHJvY2VkdXJlIGFzIGZ1bGwgZmluZS10dW5pbmcgYnV0IHdpdGggdHdvIGtleSBkaWZmZXJlbmNlczogKDEpIHRoZSBiYWNrYm9uZSBvcHRpbWl6ZXIgZ3JvdXAgaGFzIGxlYXJuaW5nIHJhdGUgMCAoZnJvemVuIHBhcmFtZXRlcnMgZG8gbm90IHJlY2VpdmUgZ3JhZGllbnQgdXBkYXRlcywgYnV0IGFyZSBpbmNsdWRlZCBpbiB0aGUgb3B0aW1pemVyIGZvciBjb21wYXRpYmlsaXR5IHdpdGggc29tZSBzY2hlZHVsZXJzKSwgYW5kICgyKSBhZGFwdGVyIHBhcmFtZXRlcnMgdXNlIGEgaGlnaGVyIGxlYXJuaW5nIHJhdGUgdGhhbiBmdWxsIGZpbmUtdHVuaW5nIOKAlCB0eXBpY2FsbHkgMWUtNCB0byA1ZS00IHJhdGhlciB0aGFuIDJlLTUuIFNpbmNlIGFkYXB0ZXJzIGhhdmUgZmFyIGZld2VyIHBhcmFtZXRlcnMgdGhhbiB0aGUgZnVsbCBtb2RlbCwgdGhleSBjYW4gYWZmb3JkIG1vcmUgYWdncmVzc2l2ZSBsZWFybmluZyByYXRlcyB3aXRob3V0IGluc3RhYmlsaXR5LiBUcmFpbmluZyBkdXJhdGlvbjogYWRhcHRlciBjb252ZXJnZW5jZSB0eXBpY2FsbHkgcmVxdWlyZXMgMuKAkzUgZXBvY2hzLCBzaW1pbGFyIHRvIGZ1bGwgZmluZS10dW5pbmcsIGFzIHRoZSBsb3NzIGxhbmRzY2FwZSBpcyBzbW9vdGhlciBkdWUgdG8gdGhlIG5lYXItaWRlbnRpdHkgaW5pdGlhbGl6YXRpb24uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlByZWZlciBQZmVpZmZlciBBZGFwdGVycyIsImNvbnRlbnQiOiJQZmVpZmZlciBhZGFwdGVycyAoc2luZ2xlIGFkYXB0ZXIgYWZ0ZXIgRkZOIG9ubHksIHNraXBwaW5nIHBvc3QtYXR0ZW50aW9uKSBhY2hpZXZlIDk4JSBvZiBIb3Vsc2J5IGFkYXB0ZXIgcGVyZm9ybWFuY2Ugd2l0aCBoYWxmIHRoZSBwYXJhbWV0ZXJzIOKAlCBwcmVmZXIgUGZlaWZmZXIgYWRhcHRlciBhcmNoaXRlY3R1cmUgdW5sZXNzIHRhc2stc3BlY2lmaWMgYWJsYXRpb25zIGZhdm9yIHRoZSBkdWFsLWFkYXB0ZXIgZGVzaWduLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTmVhci1pZGVudGl0eSBpbml0IGlzIGNyaXRpY2FsOiBXX3VwIOKJiCAwIGF0IHN0YXJ0IHByZXZlbnRzIGFkYXB0ZXIgZnJvbSBkaXNydXB0aW5nIHByZXRyYWluZWQgcGVyZm9ybWFuY2UuIiwiQm90dGxlbmVjayBkaW0gbT02NCBpcyBhIGdvb2QgZGVmYXVsdDsgbT044oCTMTYgZm9yIGV4dHJlbWUgcGFyYW1ldGVyIGVmZmljaWVuY3kgd2l0aCBzbGlnaHQgYWNjdXJhY3kgZHJvcC4iLCJQZmVpZmZlciBcdTAwM2UgSG91bHNieSBpbiBwYXJhbXMvcGVyZm9ybWFuY2UgcmF0aW87IHVzZSBIb3Vsc2J5IG9ubHkgaWYgYWJsYXRpb25zIHNob3cgY2xlYXIgYmVuZWZpdC4iLCJBZGFwdGVySHViOiA0MDArIHByZXRyYWluZWQgYWRhcHRlcnMgZm9yIEJFUlQsIFJvQkVSVGEsIFhMTS1SIGFjcm9zcyAzMCsgTkxQIHRhc2tzLiIsIkFkYXB0ZXIgZnVzaW9uOiB0cmFpbiBmdXNpb24gd2VpZ2h0cyBvbiB0YXJnZXQgdGFzayBhZnRlciBsb2FkaW5nIHRhc2stc3BlY2lmaWMgYWRhcHRlcnMgZnJvbSBBZGFwdGVySHViLiIsIlBhcmFsbGVsIGFkYXB0ZXJzIGFyZSBmYXN0ZXIgYXQgaW5mZXJlbmNlIChubyBzZXF1ZW50aWFsIGJvdHRsZW5lY2spIGJ1dCByZXF1aXJlIGFyY2hpdGVjdHVyZSBjaGFuZ2VzLiIsIkFkYXB0ZXIgbGVhcm5pbmcgcmF0ZTogMWUtNCB0byA1ZS00ICgxMMOXIGhpZ2hlciB0aGFuIGZ1bGwgZmluZS10dW5pbmcgTFIpIGlzIHN0YW5kYXJkLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Adapter Layers — Bottleneck Modules Between Transformer Layers

Adapter layers (Houlsby et al., 2019) are small bottleneck feed-forward modules inserted between sub-layers of a frozen pretrained transformer. Only the adapter parameters are trained; all original weights remain fixed. This allows a single large pretrained model to support many tasks simultaneously: different adapters are loaded per task while the backbone is shared. Adapters are the earliest and most widely studied PEFT method, predating LoRA, and their modular design has spawned an ecosystem of variants and tooling including AdapterHub, a public registry with 400+ pretrained adapters.

## Bottleneck Architecture

Each adapter applies the function: adapter(h) = h + W_up(σ(W_down(LayerNorm(h)))) where W_down ∈ ℝ^(d×m) is the down-projection and W_up ∈ ℝ^(m×d) is the up-projection. The bottleneck dimension m controls the capacity and parameter count. Typical values: m ∈ {8, 16, 32, 64}. The residual connection (h +) ensures that when W_up is initialized near zero, the adapter output is approximately h. For the Houlsby design, two adapters are inserted per transformer layer: one after the self-attention sub-layer and one after the FFN sub-layer. For BERT-base (d=768, 12 layers, m=64): params per adapter = 2×768×64 + 2×64 biases = 98,432; two adapters per layer × 12 layers = 2.36M total — about 0.9% of BERT-base's 110M parameters.

## Near-Identity Initialization

The near-identity initialization is not optional — it is the property that makes adapter insertion safe for a pretrained model. When W_up is initialized with values near zero (e.g., N(0, 0.001)), the adapter contribution W_up(σ(W_down(h))) ≈ 0, so the adapter output ≈ h. The pretrained model's predictions are preserved at the start of training. Without near-identity init, inserting adapters into a pretrained BERT and evaluating on any downstream task before training gives random outputs. This initialization also makes the adapter's optimization well-conditioned: the task loss starts at the pretrained model's loss, and the adapters gradually diverge toward a task-specific configuration.

## Adapter Layer Implementation

```python
import torch
import torch.nn as nn
import math

class AdapterLayer(nn.Module):
    """
    Bottleneck adapter: LayerNorm -> down-project -> activate -> up-project -> residual.
    Near-identity at init: W_up initialized near zero.
    """

    def __init__(self, d_model: int, bottleneck_dim: int,
                 activation: str = 'gelu', dropout: float = 0.0):
        super().__init__()
        self.layer_norm = nn.LayerNorm(d_model)
        self.down_proj = nn.Linear(d_model, bottleneck_dim)
        self.up_proj   = nn.Linear(bottleneck_dim, d_model)
        self.dropout   = nn.Dropout(dropout)
        self.act = nn.GELU() if activation == 'gelu' else nn.ReLU()
        self._near_identity_init()

    def _near_identity_init(self):
        """Initialize W_up near zero so adapter output ≈ input at start."""
        nn.init.kaiming_uniform_(self.down_proj.weight, a=math.sqrt(5))
        nn.init.zeros_(self.down_proj.bias)
        nn.init.normal_(self.up_proj.weight, mean=0.0, std=1e-3)
        nn.init.zeros_(self.up_proj.bias)

    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        residual = hidden
        h = self.layer_norm(hidden)
        h = self.down_proj(h)
        h = self.act(h)
        h = self.dropout(h)
        h = self.up_proj(h)
        return residual + h

adapter = AdapterLayer(d_model=768, bottleneck_dim=64)
x = torch.randn(2, 10, 768)
out = adapter(x)
max_diff = (out - x).abs().max().item()
print(f'Max deviation from identity at init: {max_diff:.6f}')  # should be ~0
print(f'Adapter trainable params: {sum(p.numel() for p in adapter.parameters()):,}')
```

## Injecting Adapters into a Transformer

```python
import torch
import torch.nn as nn
from transformers import BertModel, BertConfig

class BertLayerWithAdapters(nn.Module):
    """Wrap a BERT layer to insert Houlsby-style adapters after attention and FFN."""

    def __init__(self, bert_layer, d_model: int = 768, bottleneck_dim: int = 64):
        super().__init__()
        self.bert_layer = bert_layer
        for param in self.bert_layer.parameters():
            param.requires_grad = False
        self.adapter_attn = AdapterLayer(d_model, bottleneck_dim)
        self.adapter_ffn  = AdapterLayer(d_model, bottleneck_dim)

    def forward(self, hidden_states, attention_mask=None):
        attn_out = self.bert_layer.attention(hidden_states, attention_mask)
        hidden_states = self.adapter_attn(attn_out[0])
        intermediate = self.bert_layer.intermediate(hidden_states)
        ffn_out = self.bert_layer.output(intermediate, hidden_states)
        hidden_states = self.adapter_ffn(ffn_out)
        return (hidden_states,)

def inject_adapters(model_name: str = 'bert-base-uncased',
                    bottleneck_dim: int = 64):
    config = BertConfig.from_pretrained(model_name)
    bert = BertModel.from_pretrained(model_name)
    for i, layer in enumerate(bert.encoder.layer):
        bert.encoder.layer[i] = BertLayerWithAdapters(
            layer, config.hidden_size, bottleneck_dim
        )
    trainable = sum(p.numel() for p in bert.parameters() if p.requires_grad)
    total = sum(p.numel() for p in bert.parameters())
    print(f'Trainable: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)')
    return bert

print('Houlsby design: 2 adapters per layer, freeze backbone, train adapters only.')
```

## AdapterHub Integration

```python
import torch
from transformers import AutoTokenizer
from adapters import AutoAdapterModel

def load_pretrained_adapter(task: str = 'sentiment'):
    """
    Load a pretrained adapter from AdapterHub for a specific task.
    AdapterHub hosts task-specific adapters for BERT, RoBERTa, T5, XLM-R.
    """
    model = AutoAdapterModel.from_pretrained('bert-base-uncased')
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    adapter_name = model.load_adapter(
        'AdapterHub/bert-base-uncased-pf-sst2',
        source='hf',
        set_active=True
    )
    model.set_active_adapters(adapter_name)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f'Active adapter: {adapter_name}')
    print(f'Trainable params: {trainable:,}')
    inputs = tokenizer('The film was a masterpiece.', return_tensors='pt')
    with torch.no_grad():
        logits = model(**inputs).logits
    print(f'Logits shape: {logits.shape}')
    return model

print('AdapterHub: 400+ pretrained adapters; load in 2 lines of code.')
```

## Adapter Fusion

Adapter fusion (Pfeiffer et al., 2021) combines outputs from K independently trained task-specific adapters via learned attention weights at inference time. Each adapter was trained on a different source task (e.g., NLI, QA, sentiment). For a new target task, the adapter weights are frozen and only the fusion attention weights are trained. This allows the model to learn which source-task adapters are most relevant for the new task. Fusion is applied at each transformer layer: a learned query-key attention over adapter outputs produces a weighted sum.

```python
import torch
import torch.nn as nn

class AdapterFusion(nn.Module):
    """
    Combine K task-specific adapter outputs via learned attention weighting.
    Adapter weights are frozen; only fusion attention weights are trained.
    """

    def __init__(self, d_model: int, n_adapters: int):
        super().__init__()
        self.query = nn.Linear(d_model, d_model, bias=False)
        self.keys = nn.Parameter(torch.randn(n_adapters, d_model) * 0.02)
        self.scale = d_model ** -0.5

    def forward(self, hidden: torch.Tensor,
                adapter_outputs: list) -> torch.Tensor:
        q = self.query(hidden)                      # (bsz, seq, d)
        scores = torch.einsum('bsd,nd->bsn', q, self.keys) * self.scale
        weights = torch.softmax(scores, dim=-1)     # (bsz, seq, n_adapters)
        stacked = torch.stack(adapter_outputs, dim=2)  # (bsz, seq, K, d)
        fused = torch.einsum('bsn,bsnd->bsd', weights, stacked)
        return hidden + fused

bsz, seq, d, K = 2, 10, 768, 3
fusion = AdapterFusion(d_model=d, n_adapters=K)
hidden = torch.randn(bsz, seq, d)
adapter_outs = [torch.randn(bsz, seq, d) for _ in range(K)]
out = fusion(hidden, adapter_outs)
print(f'Fusion output shape: {out.shape}')  # (2, 10, 768)
fusion_trainable = sum(p.numel() for p in fusion.parameters())
print(f'Fusion trainable params: {fusion_trainable:,}')
```

## Adapter Variants Comparison

| Variant | Placement | Params per Layer | Quality vs Full FT | Modular (Swap at Inference) |
| --- | --- | --- | --- | --- |
| Houlsby (serial) | After attention + after FFN (2 per layer) | 2 × 2dm | ~99% | Yes |
| Pfeiffer (serial, single) | After FFN only (1 per layer) | 2dm | ~98% | Yes |
| Parallel adapter (PALs) | Parallel to attention sub-layer | 2dm | ~98% | Yes |
| Compacter | After FFN, Kronecker product weights | ~4× smaller than Houlsby | ~97% | Yes |
| LoRA-as-adapter | In Q, V weight matrices (additive) | 2dr per matrix | ~99% | Yes (merge or swap) |

## Adapter Stacking and Composition

Multiple adapters can be stacked within a single layer: the output of one adapter feeds into the next. This is useful for composing a general-domain adapter (e.g., trained on Wikipedia) with a task-specific adapter. AdapterHub supports stacking via adapter composition primitives: Stack([domain_adapter, task_adapter]) applies them sequentially. A simpler alternative is adapter averaging: take the element-wise average of two adapters' weight matrices when the tasks are related. This has been shown to outperform either single adapter on cross-lingual transfer tasks without any additional training.

## Training Procedure and Hyperparameters

Adapter training follows the same procedure as full fine-tuning but with two key differences: (1) the backbone optimizer group has learning rate 0 (frozen parameters do not receive gradient updates, but are included in the optimizer for compatibility with some schedulers), and (2) adapter parameters use a higher learning rate than full fine-tuning — typically 1e-4 to 5e-4 rather than 2e-5. Since adapters have far fewer parameters than the full model, they can afford more aggressive learning rates without instability. Training duration: adapter convergence typically requires 2–5 epochs, similar to full fine-tuning, as the loss landscape is smoother due to the near-identity initialization.

> **Prefer Pfeiffer Adapters**: Pfeiffer adapters (single adapter after FFN only, skipping post-attention) achieve 98% of Houlsby adapter performance with half the parameters — prefer Pfeiffer adapter architecture unless task-specific ablations favor the dual-adapter design.

- Near-identity init is critical: W_up ≈ 0 at start prevents adapter from disrupting pretrained performance.
- Bottleneck dim m=64 is a good default; m=8–16 for extreme parameter efficiency with slight accuracy drop.
- Pfeiffer > Houlsby in params/performance ratio; use Houlsby only if ablations show clear benefit.
- AdapterHub: 400+ pretrained adapters for BERT, RoBERTa, XLM-R across 30+ NLP tasks.
- Adapter fusion: train fusion weights on target task after loading task-specific adapters from AdapterHub.
- Parallel adapters are faster at inference (no sequential bottleneck) but require architecture changes.
- Adapter learning rate: 1e-4 to 5e-4 (10× higher than full fine-tuning LR) is standard.

---

