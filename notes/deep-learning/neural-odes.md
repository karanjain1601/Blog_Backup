---
title: "Neural ODEs — Continuous-Depth Models"
slug: "neural-odes"
description: "Neural ODEs (Chen et al. 2018) replace discrete layers with a continuous ODE dx/dt = f(x,t,theta) solved by Runge-Kutta. The adjoint method backpropagates through the solver in O(1) memory. FFJORD uses Hutchinson's trace estimator for scalable continuous normalizing flows."
tags: ["deep-learning", "generative-models", "diffusion-models", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmV1cmFsIE9ERXMgKENoZW4gZXQgYWwuLCAyMDE4KSBkZWZpbmUgYSBtb2RlbCB3aGVyZSB0aGUgaGlkZGVuIHN0YXRlIGV2b2x2ZXMgY29udGludW91c2x5OiBkeC9kdCA9IGYoeCwgdCwgzrgpLiBUaGUgb3V0cHV0IGlzIHgoVCkgPSB4KDApICsg4oyg4oyhIGYoeCh0KSwgdCwgzrgpIGR0LCBjb21wdXRlZCBieSBhbiBPREUgc29sdmVyLiBJbnN0ZWFkIG9mIGEgZml4ZWQgbnVtYmVyIG9mIGRpc2NyZXRlIGxheWVycywgdGhlIHNvbHZlciBhZGFwdGl2ZWx5IGNob29zZXMgaG93IG1hbnkgZnVuY3Rpb24gZXZhbHVhdGlvbnMgdG8gdXNlLiBUaGlzIGdpdmVzIGNvbnRpbnVvdXMtdGltZSBkeW5hbWljcywgTygxKSBtZW1vcnkgYmFja3Byb3BhZ2F0aW9uIHZpYSB0aGUgYWRqb2ludCBtZXRob2QsIGFuZCBhIG5hdHVyYWwgZnJhbWV3b3JrIGZvciBjb250aW51b3VzIG5vcm1hbGl6aW5nIGZsb3dzIHdoZXJlIHRoZSBsb2ctZGV0ZXJtaW5hbnQgZXZvbHZlcyB2aWEgdGhlIHRyYWNlIG9mIHRoZSBKYWNvYmlhbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGcm9tIERpc2NyZXRlIExheWVycyB0byBDb250aW51b3VzIER5bmFtaWNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHJlc2lkdWFsIG5ldHdvcmsgY29tcHV0ZXMgeF97bCsxfSA9IHhfbCArIGYoeF9sLCDOuF9sKS4gQXMgdGhlIHN0ZXAgc2l6ZSDOlHQg4oaSIDAgYW5kIHRoZSBudW1iZXIgb2YgbGF5ZXJzIOKGkiDiiJ4gd2l0aCDOlHQgZml4ZWQsIHRoaXMgY29udmVyZ2VzIHRvIHRoZSBPREUgZHgvZHQgPSBmKHgsIHQsIM64KS4gTmV1cmFsIE9ERSBwYXJhbWV0ZXJpemVzIGYgd2l0aCBhIG5ldXJhbCBuZXR3b3JrIGFuZCB1c2VzIGFuIE9ERSBzb2x2ZXIgKEV1bGVyLCBSSzQsIG9yIGFkYXB0aXZlIERvcHJpNSkgdG8gaW50ZWdyYXRlIGZyb20gdD0wIHRvIHQ9VC4gVGhlIHNvbHZlciBldmFsdWF0ZXMgZiBtdWx0aXBsZSB0aW1lcyBwZXIgc3RlcDsgdGhlIHRvdGFsIG51bWJlciBvZiBldmFsdWF0aW9ucyBpcyB0aGUgZWZmZWN0aXZlIGRlcHRoLCBjaG9zZW4gYWRhcHRpdmVseSBiYXNlZCBvbiBlcnJvciB0b2xlcmFuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT0RFIFNvbHZlcnMgYW5kIEFkYXB0aXZlIENvbXB1dGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgRG9ybWFuZC1QcmluY2UgKERvcHJpNSkgc29sdmVyIGlzIGEgNCg1KXRoLW9yZGVyIFJ1bmdlLUt1dHRhIG1ldGhvZCB3aXRoIGFkYXB0aXZlIHN0ZXAgc2l6ZS4gSXQgZXN0aW1hdGVzIHRoZSBsb2NhbCB0cnVuY2F0aW9uIGVycm9yIGJ5IGNvbXBhcmluZyA0dGggYW5kIDV0aCBvcmRlciBzb2x1dGlvbnM7IGlmIHRoZSBlcnJvciBleGNlZWRzIHRoZSB0b2xlcmFuY2UsIHRoZSBzdGVwIGlzIHJlamVjdGVkIGFuZCByZXRyaWVkIHdpdGggYSBzbWFsbGVyIHN0ZXAuIFRoaXMgbWVhbnMgdGhlIHNvbHZlciB1c2VzIG1vcmUgZXZhbHVhdGlvbnMgaW4gcmVnaW9ucyB3aGVyZSBmIGNoYW5nZXMgcmFwaWRseSBhbmQgZmV3ZXIgd2hlcmUgZHluYW1pY3MgYXJlIHNtb290aC4gVGhlIG51bWJlciBvZiBmdW5jdGlvbiBldmFsdWF0aW9ucyBpcyBub3QgZml4ZWQ6IGl0IGRlcGVuZHMgb24gdGhlIGlucHV0LCBtYWtpbmcgTmV1cmFsIE9ERXMgaXJyZWd1bGFyIGNvbXB1dGUgbW9kZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuIyBJbnN0YWxsOiBwaXAgaW5zdGFsbCB0b3JjaGRpZmZlcVxuZnJvbSB0b3JjaGRpZmZlcSBpbXBvcnQgb2RlaW50XG5cbmNsYXNzIE9ERUZ1bmMobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJEeW5hbWljczogZHgvZHQgPSBmKHgsIHQsIHRoZXRhKS4gTmV0d29yayB0YWtlcyAoeCwgdF9lbmNvZGVkKSBhcyBpbnB1dC5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZCArIDEsIDY0KSwgbm4uVGFuaCgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDY0LCA2NCksICAgbm4uVGFuaCgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDY0LCBkKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHQsIHgpOlxuICAgICAgICB0X3ZlYyA9IHQuZXhwYW5kKHguc2hhcGVbMF0sIDEpXG4gICAgICAgIHJldHVybiBzZWxmLm5ldCh0b3JjaC5jYXQoW3gsIHRfdmVjXSwgZGltPTEpKVxuXG5jbGFzcyBOZXVyYWxPREUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCwgdF9zcGFuPSgwLiwgMS4pLCBtZXRob2Q9XHUwMDI3ZG9wcmk1XHUwMDI3KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZnVuYyAgID0gT0RFRnVuYyhkKVxuICAgICAgICBzZWxmLnQgICAgICA9IHRvcmNoLnRlbnNvcih0X3NwYW4pXG4gICAgICAgIHNlbGYubWV0aG9kID0gbWV0aG9kXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4MCk6XG4gICAgICAgICMgb2RlaW50IHJldHVybnMgc2hhcGUgKHRpbWVfcG9pbnRzLCBiYXRjaCwgZClcbiAgICAgICAgdHJhaiA9IG9kZWludChzZWxmLmZ1bmMsIHgwLCBzZWxmLnQsIG1ldGhvZD1zZWxmLm1ldGhvZClcbiAgICAgICAgcmV0dXJuIHRyYWpbLTFdICAgIyBmaW5hbCBzdGF0ZSB4KFQpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5tb2RlbCA9IE5ldXJhbE9ERShkPTQpXG54MCA9IHRvcmNoLnJhbmRuKDMyLCA0KVxueF9UID0gbW9kZWwoeDApXG5wcmludChmXCJJbnB1dDoge3gwLnNoYXBlfSAtXHUwMDNlIE91dHB1dDoge3hfVC5zaGFwZX1cIilcbnByaW50KFwiRG9wcmk1IGFkYXB0aXZlbHkgY2hvb3NlcyBzdGVwIHNpemU7IGVmZmVjdGl2ZSBkZXB0aCBpcyBpbnB1dC1kZXBlbmRlbnRcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZGpvaW50IFNlbnNpdGl2aXR5IE1ldGhvZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgYXV0b2dyYWQgc3RvcmVzIGFsbCBpbnRlcm1lZGlhdGUgYWN0aXZhdGlvbnMgZnJvbSB0aGUgT0RFIHNvbHZlciwgcmVxdWlyaW5nIE8oTl9zdGVwcykgbWVtb3J5LiBUaGUgYWRqb2ludCBtZXRob2QgYXZvaWRzIHRoaXM6IGRlZmluZSB0aGUgYWRqb2ludCBhKHQpID0gZEwvZHgodCkuIEl0IHNhdGlzZmllcyBpdHMgb3duIE9ERSBkYS9kdCA9IC1hKHQpIMOXICjiiIJmL+KIgngpLCBzb2x2ZWQgYmFja3dhcmQgZnJvbSB0PVQgdG8gdD0wLiBHcmFkaWVudHMgd2l0aCByZXNwZWN0IHRvIM64IGFyZSBvYnRhaW5lZCBieSBpbnRlZ3JhdGluZyBhKHQpIMOXICjiiIJmL+KIgs64KSBhbG9uZyB0aGlzIHRyYWplY3RvcnkuIFRoZSBiYWNrd2FyZCBPREUgcmVxdWlyZXMgb25seSBvbmUgT0RFIHNvbHZlIChubyBzdG9yZWQgYWN0aXZhdGlvbnMpLCBnaXZpbmcgTygxKSBtZW1vcnkgcmVnYXJkbGVzcyBvZiBzb2x2ZXIgc3RlcHMuIFRoZSB0cmFkZS1vZmY6IGFwcHJveGltYXRlbHkgMsOXIHRoZSBjb21wdXRlIG9mIHRoZSBmb3J3YXJkIHBhc3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG4jIHRvcmNoZGlmZmVxIHByb3ZpZGVzIGFkam9pbnQtYmFzZWQgYmFja3Byb3BcbmZyb20gdG9yY2hkaWZmZXEgaW1wb3J0IG9kZWludF9hZGpvaW50XG5cbmNsYXNzIEFkam9pbnROZXVyYWxPREUobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJcbiAgICBVc2VzIGFkam9pbnQgc2Vuc2l0aXZpdHkgbWV0aG9kOlxuICAgIC0gRm9yd2FyZDogc29sdmUgT0RFIGZyb20gdD0wIHRvIFQgKHN0YW5kYXJkKS5cbiAgICAtIEJhY2t3YXJkOiBzb2x2ZSBhZGpvaW50IE9ERSBmcm9tIFQgdG8gMCDigJQgbm8gc3RvcmVkIGludGVybWVkaWF0ZXMuXG4gICAgLSBNZW1vcnk6IE8oMSkgcmVnYXJkbGVzcyBvZiBudW1iZXIgb2Ygc29sdmVyIHN0ZXBzLlxuICAgIFwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZnVuYyA9IE9ERUZ1bmMoZClcbiAgICAgICAgc2VsZi50ICAgID0gdG9yY2gudGVuc29yKFswLiwgMS5dKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDApOlxuICAgICAgICByZXR1cm4gb2RlaW50X2Fkam9pbnQoXG4gICAgICAgICAgICBzZWxmLmZ1bmMsIHgwLCBzZWxmLnQsXG4gICAgICAgICAgICBtZXRob2Q9XHUwMDI3ZG9wcmk1XHUwMDI3LFxuICAgICAgICAgICAgYWRqb2ludF9wYXJhbXM9bGlzdChzZWxmLmZ1bmMucGFyYW1ldGVycygpKVxuICAgICAgICApWy0xXVxuXG5kZWYgY291bnRfcGFyYW1zKG0pOiByZXR1cm4gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtLnBhcmFtZXRlcnMoKSlcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5kLCBCID0gOCwgNjRcbm5vZGUgPSBBZGpvaW50TmV1cmFsT0RFKGQpXG54MCA9IHRvcmNoLnJhbmRuKEIsIGQsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbnhfVCA9IG5vZGUoeDApXG5sb3NzID0geF9ULnN1bSgpXG5sb3NzLmJhY2t3YXJkKClcblxucHJpbnQoZlwiUGFyYW1ldGVyczoge2NvdW50X3BhcmFtcyhub2RlKX1cIilcbnByaW50KGZcIngwIGdyYWRpZW50IHNoYXBlOiB7eDAuZ3JhZC5zaGFwZX1cIilcbnByaW50KFwiQWRqb2ludDogYmFja3dhcmQgcGFzcyBzb2x2ZXMgYW5vdGhlciBPREUgLS0gTygxKSBtZW1vcnksIH4yeCBjb21wdXRlXCIpXG5wcmludChcIlN0YW5kYXJkIGF1dG9ncmFkOiBPKE5fc3RlcHMpIG1lbW9yeSAtLSBpbmZlYXNpYmxlIGZvciB0aWdodCB0b2xlcmFuY2VzXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udGludW91cyBOb3JtYWxpemluZyBGbG93cyAoRkZKT1JEKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBDb250aW51b3VzIE5vcm1hbGl6aW5nIEZsb3cgKENORikgbW9kZWxzIHRoZSBjaGFuZ2UgaW4gbG9nLWRlbnNpdHkgYXMgZHggZXZvbHZlczogZCBsb2cgcCh4KSAvIGR0ID0gLVRyKOKIgmYv4oiCeCkuIENvbXB1dGluZyB0aGUgZXhhY3QgdHJhY2UgcmVxdWlyZXMgZCBiYWNrd2FyZCBwYXNzZXMgKG9uZSBwZXIgb3V0cHV0IGRpbWVuc2lvbiksIGNvc3RpbmcgTyhkwrIpIHBlciBzdGVwLiBGRkpPUkQgKEdyYXRod29obCBldCBhbC4sIDIwMTkpIHVzZXMgSHV0Y2hpbnNvblx1MDAyN3MgZXN0aW1hdG9yOiBUcihKKSDiiYggRVtl4bWAIEogZV0gZm9yIGUgfiBOKDAsSSkgb3IgUmFkZW1hY2hlci4gT25lIHNhbXBsZSBzdWZmaWNlcyBkdXJpbmcgdHJhaW5pbmcsIHJlZHVjaW5nIHRyYWNlIGNvc3QgdG8gTyhkKSBwZXIgT0RFIHN0ZXAuIEZGSk9SRCBhY2hpZXZlcyBjb21wZXRpdGl2ZSBsb2ctbGlrZWxpaG9vZCB3aXRoIGZld2VyIHBhcmFtZXRlcnMgdGhhbiBkaXNjcmV0ZSBmbG93cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgQ05GRHluYW1pY3Mobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJcbiAgICBDTkYgam9pbnQgZHluYW1pY3M6IGQoeiwgbG9nX3B6KS9kdCA9IChmKHosdCksIC1UcihkZi9keikpLlxuICAgIEh1dGNoaW5zb24gZXN0aW1hdG9yOiBUcihKKSB+IGVeVCAoSiBlKSBmb3IgZSB+IFJhZGVtYWNoZXIuXG4gICAgUmVkdWNlcyBPKGReMikgZXhhY3QgdHJhY2UgdG8gTyhkKSBwZXIgc3RlcC5cbiAgICBcIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCwgaGlkZGVuPTY0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkICsgMSwgaGlkZGVuKSwgbm4uVGFuaCgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuKSwgbm4uVGFuaCgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgZCkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB0LCBzdGF0ZSk6XG4gICAgICAgIHosIGxvZ19weiA9IHN0YXRlXG4gICAgICAgIHRfdmVjID0gdC5leHBhbmQoei5zaGFwZVswXSwgMSlcbiAgICAgICAgel9pbiAgPSB0b3JjaC5jYXQoW3osIHRfdmVjXSwgZGltPS0xKS5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgICAgICBmID0gc2VsZi5uZXQoel9pbilcbiAgICAgICAgIyBIdXRjaGluc29uIHRyYWNlIGVzdGltYXRvclxuICAgICAgICBlID0gKHRvcmNoLnJhbmRpbnRfbGlrZSh6LCAwLCAyKS5mbG9hdCgpICogMiAtIDEpICAjIFJhZGVtYWNoZXJcbiAgICAgICAgZV9KZiA9IHRvcmNoLmF1dG9ncmFkLmdyYWQoZiwgel9pbiwgZSwgY3JlYXRlX2dyYXBoPVRydWUpWzBdWy4uLiwgOnouc2hhcGVbLTFdXVxuICAgICAgICB0cmFjZV9lc3QgPSAoZSAqIGVfSmYpLnN1bShkaW09LTEsIGtlZXBkaW09VHJ1ZSlcbiAgICAgICAgcmV0dXJuIGYsIC10cmFjZV9lc3RcblxuZGVmIGh1dGNoaW5zb25fdHJhY2VfY2hlY2soZD0xNiwgbl9lc3Q9MTAwKTpcbiAgICBcIlwiXCJWZXJpZnkgSHV0Y2hpbnNvbiBlc3RpbWF0b3IgY29udmVyZ2VzIHRvIGV4YWN0IHRyYWNlLlwiXCJcIlxuICAgIEogPSB0b3JjaC5yYW5kbihkLCBkKVxuICAgIGV4YWN0X3RyYWNlID0gSi50cmFjZSgpLml0ZW0oKVxuICAgIGVzdGltYXRlcyA9IFsodG9yY2gucmFuZG4oZCkgQCBKIEAgdG9yY2gucmFuZG4oZCkpLml0ZW0oKSBmb3IgXyBpbiByYW5nZShuX2VzdCldXG4gICAgcHJpbnQoZlwiRXhhY3QgdHJhY2U6IHtleGFjdF90cmFjZTouNGZ9XCIpXG4gICAgcHJpbnQoZlwiSHV0Y2hpbnNvbiBtZWFuICh7bl9lc3R9IHNhbXBsZXMpOiB7c3VtKGVzdGltYXRlcykvbl9lc3Q6LjRmfVwiKVxuICAgIHByaW50KFwiVHIoSikgPSBFW2VeVCBKIGVdIGlzIHVuYmlhc2VkIGZvciBhbnkgZSB3aXRoIEVbZWVeVF09SVwiKVxuXG5odXRjaGluc29uX3RyYWNlX2NoZWNrKCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOZXVyYWwgT0RFIHZzIFJlc05ldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQm90aCBSZXNOZXRzIGFuZCBOZXVyYWwgT0RFcyBjb21wdXRlIGEgc2VxdWVuY2Ugb2YgdHJhbnNmb3JtYXRpb25zLCBidXQgUmVzTmV0cyBmaXggdGhlIG51bWJlciBvZiBmdW5jdGlvbiBldmFsdWF0aW9ucyBhdCBncmFwaCBjb25zdHJ1Y3Rpb24gdGltZSB3aGlsZSBOZXVyYWwgT0RFcyBhZGFwdCB0byBpbnB1dCBjb21wbGV4aXR5LiBBIE5ldXJhbCBPREUgd2l0aCB0b2xlcmFuY2UgMWUtNSBtYXkgdXNlIDEwLTEwMCBmdW5jdGlvbiBldmFsdWF0aW9ucyB3aGVyZSBhIDYtYmxvY2sgUmVzTmV0IHVzZXMgZXhhY3RseSA2LiBGb3Igc2ltcGxlIGlucHV0cywgdGhlIE9ERSBzb2x2ZXIgbWF5IG5lZWQgZmV3ZXIgZXZhbHVhdGlvbnMgdGhhbiB0aGUgUmVzTmV0OyBmb3IgY29tcGxleCBpbnB1dHMsIG1vcmUuIFRoaXMgbWFrZXMgTmV1cmFsIE9ERXMgbW9yZSBleHByZXNzaXZlIHBlciBwYXJhbWV0ZXIgYnV0IHNsb3dlciBhbmQgbGVzcyBwcmVkaWN0YWJsZSBpbiB3YWxsLWNsb2NrIHRpbWUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdGltZVxuXG5jbGFzcyBSZXNOZXQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCwgbl9ibG9ja3MpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5ibG9ja3MgPSBubi5Nb2R1bGVMaXN0KFtcbiAgICAgICAgICAgIG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKGQsIGQpLCBubi5UYW5oKCksIG5uLkxpbmVhcihkLCBkKSlcbiAgICAgICAgICAgIGZvciBfIGluIHJhbmdlKG5fYmxvY2tzKV0pXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGZvciBibGsgaW4gc2VsZi5ibG9ja3M6XG4gICAgICAgICAgICB4ID0geCArIGJsayh4KVxuICAgICAgICByZXR1cm4geFxuXG5kZWYgY29tcGFyZShkPTMyLCBCPTEyOCwgbl9ibG9ja3M9Nik6XG4gICAgcmVzbmV0ID0gUmVzTmV0KGQsIG5fYmxvY2tzKVxuICAgIG5vZGUgICA9IE5ldXJhbE9ERShkLCBtZXRob2Q9XHUwMDI3ZG9wcmk1XHUwMDI3KVxuICAgIHggPSB0b3JjaC5yYW5kbihCLCBkKVxuICAgIGZvciBuYW1lLCBtb2RlbCBpbiBbKFx1MDAyN1Jlc05ldFx1MDAyNywgcmVzbmV0KSwgKFx1MDAyN05ldXJhbE9ERVx1MDAyNywgbm9kZSldOlxuICAgICAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2UoMTApOlxuICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICAgICAgXyA9IG1vZGVsKHgpXG4gICAgICAgIG1zID0gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MCkgLyAxMCAqIDEwMDBcbiAgICAgICAgbl9wID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpXG4gICAgICAgIHByaW50KGZcIntuYW1lOjEyc306IHttczo2LjFmfSBtcy9mb3J3YXJkICB7bl9wOjZkfSBwYXJhbXNcIilcblxuY29tcGFyZSgpXG5wcmludChcIk5ldXJhbE9ERTogYWRhcHRpdmUgZGVwdGggKHNvbHZlciBORkVzIH4gMTItNTAgZm9yIERvcHJpNSBhdCB0b2w9MWUtMylcIilcbnByaW50KFwiUmVzTmV0OiAgICBmaXhlZCBkZXB0aCAoYWx3YXlzIG5fYmxvY2tzIGV2YWx1YXRpb25zKVwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiUHJhY3RpY2FsIExpbWl0YXRpb25zIG9mIE5ldXJhbCBPREVzIiwiY29udGVudCI6Ik5ldXJhbCBPREVzIGFyZSBzbG93ZXIgdGhhbiBSZXNOZXRzIGF0IGVxdWl2YWxlbnQgcGFyYW1ldGVyIGNvdW50cyBkdWUgdG8gdGhlIG92ZXJoZWFkIG9mIGFkYXB0aXZlIE9ERSBzb2x2ZXJzLiBCYWNrcHJvcGFnYXRpb24gdGhyb3VnaCB0aGUgc29sdmVyIChldmVuIHdpdGggYWRqb2ludCkgcmVxdWlyZXMgc29sdmluZyB0d28gT0RFcy4gRm9yIGltYWdlIGdlbmVyYXRpb24gdGFza3MsIGRpc2NyZXRlIG5vcm1hbGl6aW5nIGZsb3dzIChHbG93LCBSZWFsTlZQKSBhcmUgZmFzdGVyIGluIHByYWN0aWNlLiBOZXVyYWwgT0RFcyBzaGluZSBmb3IgaXJyZWd1bGFyIHRpbWUtc2VyaWVzIGRhdGEsIGxhdGVudCBkeW5hbWljcyBtb2RlbGluZywgYW5kIHNldHRpbmdzIHdoZXJlIG1lbW9yeSBpcyB0aGUgcHJpbWFyeSBjb25zdHJhaW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFkdmFudGFnZXMgYW5kIExpbWl0YXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOZXVyYWwgT0RFcyBvZmZlciB1bmlxdWUgYmVuZWZpdHMgdGhhdCBubyBkaXNjcmV0ZS1sYXllciBhcmNoaXRlY3R1cmUgY2FuIG1hdGNoOiBjb250aW51b3VzLXRpbWUgbGF0ZW50IGR5bmFtaWNzLCBtZW1vcnktZWZmaWNpZW50IGdyYWRpZW50cyB2aWEgdGhlIGFkam9pbnQsIGFuZCBuYXR1cmFsIGhhbmRsaW5nIG9mIGlycmVndWxhciB0aW1lLXNlcmllcy4gSG93ZXZlciwgdGhleSBjb21lIHdpdGggcHJhY3RpY2FsIGNvc3RzOiBPREUgc29sdmVycyBhZGQgb3ZlcmhlYWQsIGFkYXB0aXZlIHN0ZXAgc2l6ZXMgbWFrZSB0cmFpbmluZyB0aW1lIHVucHJlZGljdGFibGUsIGFuZCB0aGUgc21vb3RobmVzcyBjb25zdHJhaW50IG9uIGYgbGltaXRzIGV4cHJlc3Npdml0eS4gRm9yIG1vc3QgaW1hZ2UgZ2VuZXJhdGlvbiB0YXNrcywgZGlzY3JldGUgZmxvd3Mgb3IgZGlmZnVzaW9uIG1vZGVscyBhcmUgZmFzdGVyLiBOZXVyYWwgT0RFcyBhcmUgbW9zdCBjb21wZWxsaW5nIGZvciBzY2llbnRpZmljIGFwcGxpY2F0aW9ucyAocGh5c2ljcyBzaW11bGF0aW9ucywgZHluYW1pY2FsIHN5c3RlbXMpIGFuZCBzdHJ1Y3R1cmVkIGxhdGVudCBzcGFjZXMgd2hlcmUgY29udGludWl0eSBpcyBhIHVzZWZ1bCBpbmR1Y3RpdmUgYmlhcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFkYXB0aXZlIGNvbXB1dGU6IHNvbHZlciB1c2VzIG1vcmUgc3RlcHMgd2hlcmUgZHluYW1pY3MgYXJlIGNvbXBsZXgsIGZld2VyIHdoZXJlIHNtb290aC4iLCJPKDEpIG1lbW9yeTogYWRqb2ludCBtZXRob2QgYmFja3Byb3BhZ2F0ZXMgd2l0aG91dCBzdG9yaW5nIGludGVybWVkaWF0ZSBhY3RpdmF0aW9ucy4iLCJDb250aW51b3VzIHRpbWU6IG5hdHVyYWwgZm9yIGlycmVndWxhcmx5LXNhbXBsZWQgdGltZSBzZXJpZXMgKG5vIGZpeGVkIM6UdCByZXF1aXJlZCkuIiwiQ29udGludW91cyBub3JtYWxpemluZyBmbG93czogRkZKT1JEIGFjaGlldmVzIGZsZXhpYmxlIGRlbnNpdGllcyB2aWEgSHV0Y2hpbnNvbiB0cmFjZS4iLCJTbG93IHRyYWluaW5nOiBlYWNoIGdyYWRpZW50IHN0ZXAgcmVxdWlyZXMgYXQgbWluaW11bSAyIE9ERSBzb2x2ZXMgKGZvcndhcmQgKyBhZGpvaW50KS4iLCJMaW1pdGVkIGV4cHJlc3Npdml0eSBpbiBwcmFjdGljZTogT0RFIGR5bmFtaWNzIG11c3QgYmUgc21vb3RoIChMaXBzY2hpdHopLCBsaW1pdGluZyBleHByZXNzaWJpbGl0eS4iLCJOb24taW50ZXJzZWN0aW5nIHRyYWplY3RvcmllczogZmxvd3MgY2Fubm90IG1vZGVsIG11bHRpLW1vZGFsIGRpc3RyaWJ1dGlvbnMgd2l0aG91dCBhdWdtZW50YXRpb24uIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vZGVsIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJSZXNOZXQiLCJOZXVyYWwgT0RFIiwiRkZKT1JEIl0sInJvd3MiOltbIkNvbXB1dGF0aW9uIiwiRGlzY3JldGUsIGZpeGVkIGRlcHRoIiwiQ29udGludW91cyBPREUsIGFkYXB0aXZlIiwiQ29udGludW91cyBPREUsIGFkYXB0aXZlIl0sWyJNZW1vcnkgKGJhY2twcm9wKSIsIk8oZGVwdGgpIiwiTygxKSB2aWEgYWRqb2ludCIsIk8oMSkgdmlhIGFkam9pbnQiXSxbIkJhY2twcm9wIG1ldGhvZCIsIlN0YW5kYXJkIGF1dG9ncmFkIiwiQWRqb2ludCBPREUgc29sdmUiLCJBZGpvaW50IE9ERSBzb2x2ZSJdLFsiRGVwdGggYWRhcHRpdml0eSIsIkZpeGVkIGF0IGJ1aWxkIHRpbWUiLCJBZGFwdGl2ZSAoc29sdmVyIHRvbGVyYW5jZSkiLCJBZGFwdGl2ZSAoc29sdmVyIHRvbGVyYW5jZSkiXSxbIkxvZy1kZXQgLyBkZW5zaXR5IiwiTi9BIiwiRXhhY3QgKE8oZF4yKSBwZXIgc3RlcCkiLCJIdXRjaGluc29uIGVzdC4gKE8oZCkgcGVyIHN0ZXApIl0sWyJNYWluIHVzZSIsIkNsYXNzaWZpY2F0aW9uLCBnZW5lcmF0aW9uIiwiVGltZS1zZXJpZXMsIGxhdGVudCBkeW5hbWljcyIsIkdlbmVyYXRpdmUgZmxvdywgZGVuc2l0eSBlc3RpbWF0aW9uIl1dfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Neural ODEs — Continuous-Depth Models

Neural ODEs (Chen et al., 2018) define a model where the hidden state evolves continuously: dx/dt = f(x, t, θ). The output is x(T) = x(0) + ⌠⌡ f(x(t), t, θ) dt, computed by an ODE solver. Instead of a fixed number of discrete layers, the solver adaptively chooses how many function evaluations to use. This gives continuous-time dynamics, O(1) memory backpropagation via the adjoint method, and a natural framework for continuous normalizing flows where the log-determinant evolves via the trace of the Jacobian.

## From Discrete Layers to Continuous Dynamics

A residual network computes x_{l+1} = x_l + f(x_l, θ_l). As the step size Δt → 0 and the number of layers → ∞ with Δt fixed, this converges to the ODE dx/dt = f(x, t, θ). Neural ODE parameterizes f with a neural network and uses an ODE solver (Euler, RK4, or adaptive Dopri5) to integrate from t=0 to t=T. The solver evaluates f multiple times per step; the total number of evaluations is the effective depth, chosen adaptively based on error tolerance.

## ODE Solvers and Adaptive Computation

The Dormand-Prince (Dopri5) solver is a 4(5)th-order Runge-Kutta method with adaptive step size. It estimates the local truncation error by comparing 4th and 5th order solutions; if the error exceeds the tolerance, the step is rejected and retried with a smaller step. This means the solver uses more evaluations in regions where f changes rapidly and fewer where dynamics are smooth. The number of function evaluations is not fixed: it depends on the input, making Neural ODEs irregular compute models.

```python
import torch
import torch.nn as nn
# Install: pip install torchdiffeq
from torchdiffeq import odeint

class ODEFunc(nn.Module):
    """Dynamics: dx/dt = f(x, t, theta). Network takes (x, t_encoded) as input."""
    def __init__(self, d):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d + 1, 64), nn.Tanh(),
            nn.Linear(64, 64),   nn.Tanh(),
            nn.Linear(64, d))

    def forward(self, t, x):
        t_vec = t.expand(x.shape[0], 1)
        return self.net(torch.cat([x, t_vec], dim=1))

class NeuralODE(nn.Module):
    def __init__(self, d, t_span=(0., 1.), method='dopri5'):
        super().__init__()
        self.func   = ODEFunc(d)
        self.t      = torch.tensor(t_span)
        self.method = method

    def forward(self, x0):
        # odeint returns shape (time_points, batch, d)
        traj = odeint(self.func, x0, self.t, method=self.method)
        return traj[-1]   # final state x(T)

torch.manual_seed(0)
model = NeuralODE(d=4)
x0 = torch.randn(32, 4)
x_T = model(x0)
print(f"Input: {x0.shape} -> Output: {x_T.shape}")
print("Dopri5 adaptively chooses step size; effective depth is input-dependent")
```

## Adjoint Sensitivity Method

Standard autograd stores all intermediate activations from the ODE solver, requiring O(N_steps) memory. The adjoint method avoids this: define the adjoint a(t) = dL/dx(t). It satisfies its own ODE da/dt = -a(t) × (∂f/∂x), solved backward from t=T to t=0. Gradients with respect to θ are obtained by integrating a(t) × (∂f/∂θ) along this trajectory. The backward ODE requires only one ODE solve (no stored activations), giving O(1) memory regardless of solver steps. The trade-off: approximately 2× the compute of the forward pass.

```python
import torch
import torch.nn as nn
# torchdiffeq provides adjoint-based backprop
from torchdiffeq import odeint_adjoint

class AdjointNeuralODE(nn.Module):
    """
    Uses adjoint sensitivity method:
    - Forward: solve ODE from t=0 to T (standard).
    - Backward: solve adjoint ODE from T to 0 — no stored intermediates.
    - Memory: O(1) regardless of number of solver steps.
    """
    def __init__(self, d):
        super().__init__()
        self.func = ODEFunc(d)
        self.t    = torch.tensor([0., 1.])

    def forward(self, x0):
        return odeint_adjoint(
            self.func, x0, self.t,
            method='dopri5',
            adjoint_params=list(self.func.parameters())
        )[-1]

def count_params(m): return sum(p.numel() for p in m.parameters())

torch.manual_seed(42)
d, B = 8, 64
node = AdjointNeuralODE(d)
x0 = torch.randn(B, d, requires_grad=True)
x_T = node(x0)
loss = x_T.sum()
loss.backward()

print(f"Parameters: {count_params(node)}")
print(f"x0 gradient shape: {x0.grad.shape}")
print("Adjoint: backward pass solves another ODE -- O(1) memory, ~2x compute")
print("Standard autograd: O(N_steps) memory -- infeasible for tight tolerances")
```

## Continuous Normalizing Flows (FFJORD)

A Continuous Normalizing Flow (CNF) models the change in log-density as dx evolves: d log p(x) / dt = -Tr(∂f/∂x). Computing the exact trace requires d backward passes (one per output dimension), costing O(d²) per step. FFJORD (Grathwohl et al., 2019) uses Hutchinson's estimator: Tr(J) ≈ E[eᵀ J e] for e ~ N(0,I) or Rademacher. One sample suffices during training, reducing trace cost to O(d) per ODE step. FFJORD achieves competitive log-likelihood with fewer parameters than discrete flows.

```python
import torch
import torch.nn as nn

class CNFDynamics(nn.Module):
    """
    CNF joint dynamics: d(z, log_pz)/dt = (f(z,t), -Tr(df/dz)).
    Hutchinson estimator: Tr(J) ~ e^T (J e) for e ~ Rademacher.
    Reduces O(d^2) exact trace to O(d) per step.
    """
    def __init__(self, d, hidden=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d + 1, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, d))

    def forward(self, t, state):
        z, log_pz = state
        t_vec = t.expand(z.shape[0], 1)
        z_in  = torch.cat([z, t_vec], dim=-1).requires_grad_(True)
        f = self.net(z_in)
        # Hutchinson trace estimator
        e = (torch.randint_like(z, 0, 2).float() * 2 - 1)  # Rademacher
        e_Jf = torch.autograd.grad(f, z_in, e, create_graph=True)[0][..., :z.shape[-1]]
        trace_est = (e * e_Jf).sum(dim=-1, keepdim=True)
        return f, -trace_est

def hutchinson_trace_check(d=16, n_est=100):
    """Verify Hutchinson estimator converges to exact trace."""
    J = torch.randn(d, d)
    exact_trace = J.trace().item()
    estimates = [(torch.randn(d) @ J @ torch.randn(d)).item() for _ in range(n_est)]
    print(f"Exact trace: {exact_trace:.4f}")
    print(f"Hutchinson mean ({n_est} samples): {sum(estimates)/n_est:.4f}")
    print("Tr(J) = E[e^T J e] is unbiased for any e with E[ee^T]=I")

hutchinson_trace_check()
```

## Neural ODE vs ResNet

Both ResNets and Neural ODEs compute a sequence of transformations, but ResNets fix the number of function evaluations at graph construction time while Neural ODEs adapt to input complexity. A Neural ODE with tolerance 1e-5 may use 10-100 function evaluations where a 6-block ResNet uses exactly 6. For simple inputs, the ODE solver may need fewer evaluations than the ResNet; for complex inputs, more. This makes Neural ODEs more expressive per parameter but slower and less predictable in wall-clock time.

```python
import torch
import torch.nn as nn
import time

class ResNet(nn.Module):
    def __init__(self, d, n_blocks):
        super().__init__()
        self.blocks = nn.ModuleList([
            nn.Sequential(nn.Linear(d, d), nn.Tanh(), nn.Linear(d, d))
            for _ in range(n_blocks)])
    def forward(self, x):
        for blk in self.blocks:
            x = x + blk(x)
        return x

def compare(d=32, B=128, n_blocks=6):
    resnet = ResNet(d, n_blocks)
    node   = NeuralODE(d, method='dopri5')
    x = torch.randn(B, d)
    for name, model in [('ResNet', resnet), ('NeuralODE', node)]:
        t0 = time.perf_counter()
        for _ in range(10):
            with torch.no_grad():
                _ = model(x)
        ms = (time.perf_counter() - t0) / 10 * 1000
        n_p = sum(p.numel() for p in model.parameters())
        print(f"{name:12s}: {ms:6.1f} ms/forward  {n_p:6d} params")

compare()
print("NeuralODE: adaptive depth (solver NFEs ~ 12-50 for Dopri5 at tol=1e-3)")
print("ResNet:    fixed depth (always n_blocks evaluations)")
```

> **Practical Limitations of Neural ODEs**: Neural ODEs are slower than ResNets at equivalent parameter counts due to the overhead of adaptive ODE solvers. Backpropagation through the solver (even with adjoint) requires solving two ODEs. For image generation tasks, discrete normalizing flows (Glow, RealNVP) are faster in practice. Neural ODEs shine for irregular time-series data, latent dynamics modeling, and settings where memory is the primary constraint.

## Advantages and Limitations

Neural ODEs offer unique benefits that no discrete-layer architecture can match: continuous-time latent dynamics, memory-efficient gradients via the adjoint, and natural handling of irregular time-series. However, they come with practical costs: ODE solvers add overhead, adaptive step sizes make training time unpredictable, and the smoothness constraint on f limits expressivity. For most image generation tasks, discrete flows or diffusion models are faster. Neural ODEs are most compelling for scientific applications (physics simulations, dynamical systems) and structured latent spaces where continuity is a useful inductive bias.

- Adaptive compute: solver uses more steps where dynamics are complex, fewer where smooth.
- O(1) memory: adjoint method backpropagates without storing intermediate activations.
- Continuous time: natural for irregularly-sampled time series (no fixed Δt required).
- Continuous normalizing flows: FFJORD achieves flexible densities via Hutchinson trace.
- Slow training: each gradient step requires at minimum 2 ODE solves (forward + adjoint).
- Limited expressivity in practice: ODE dynamics must be smooth (Lipschitz), limiting expressibility.
- Non-intersecting trajectories: flows cannot model multi-modal distributions without augmentation.

## Model Comparison

| Property | ResNet | Neural ODE | FFJORD |
| --- | --- | --- | --- |
| Computation | Discrete, fixed depth | Continuous ODE, adaptive | Continuous ODE, adaptive |
| Memory (backprop) | O(depth) | O(1) via adjoint | O(1) via adjoint |
| Backprop method | Standard autograd | Adjoint ODE solve | Adjoint ODE solve |
| Depth adaptivity | Fixed at build time | Adaptive (solver tolerance) | Adaptive (solver tolerance) |
| Log-det / density | N/A | Exact (O(d^2) per step) | Hutchinson est. (O(d) per step) |
| Main use | Classification, generation | Time-series, latent dynamics | Generative flow, density estimation |

---

