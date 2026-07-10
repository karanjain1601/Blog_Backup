---
title: "DDPM — Forward Process and Reverse Denoising"
slug: "ddpm-denoising-diffusion"
description: "DDPM (Ho et al. 2020) defines a T=1000-step Markov chain that gradually adds Gaussian noise (forward) and learns to reverse it (reverse process). Covers the closed-form q(x_t|x_0), linear vs cosine beta schedules, U-Net with time embedding, and the full sampling loop."
tags: ["deep-learning", "generative-models", "diffusion-models", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRERQTSAoSG8gZXQgYWwuLCAyMDIwKSBkZWZpbmVzIGEgZ2VuZXJhdGl2ZSBtb2RlbCBhcyB0aGUgcmV2ZXJzZSBvZiBhIGZpeGVkIGZvcndhcmQgTWFya292IGNoYWluIHRoYXQgZ3JhZHVhbGx5IGNvcnJ1cHRzIGRhdGEgd2l0aCBHYXVzc2lhbiBub2lzZS4gVGhlIGZvcndhcmQgcHJvY2VzcyBxKHhfdCB8IHhfe3QtMX0pID0gTih4X3Q7IOKImigxLc6yX3QpIHhfe3QtMX0sIM6yX3QgSSkgaGFzIGEgY2xvc2VkLWZvcm0gbWFyZ2luYWwgcSh4X3QgfCB4XzApID0gTih4X3Q7IOKIms6xzIVfdCB4XzAsICgxLc6xzIVfdCkgSSksIGFsbG93aW5nIGRpcmVjdCBzYW1wbGluZyBhdCBhbnkgbm9pc2UgbGV2ZWwgd2l0aG91dCBzaW11bGF0aW9uLiBBIFUtTmV0IGxlYXJucyB0byByZXZlcnNlIHRoaXMgcHJvY2VzczogZ2l2ZW4gbm9pc3kgeF90IGFuZCB0aW1lc3RlcCB0LCBwcmVkaWN0IHRoZSBub2lzZSDOtSB0aGF0IHdhcyBhZGRlZC4gQXQgZ2VuZXJhdGlvbiwgdGhlIG1vZGVsIHN0YXJ0cyBmcm9tIHhfVCB+IE4oMCxJKSBhbmQgaXRlcmF0aXZlbHkgZGVub2lzZXMgb3ZlciBUPTEwMDAgc3RlcHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRm9yd2FyZCBEaWZmdXNpb24gUHJvY2VzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGZvcndhcmQgcHJvY2VzcyBhZGRzIG5vaXNlIHN0ZXAtYnktc3RlcDogcSh4X3QgfCB4X3t0LTF9KSA9IE4oeF90OyDiiJooMS3Osl90KSB4X3t0LTF9LCDOsl90IEkpLiBUaGUgc2lnbmFsIGlzIGF0dGVudWF0ZWQgYnkg4oiaKDEtzrJfdCkgYXQgZWFjaCBzdGVwIHdoaWxlIEdhdXNzaWFuIG5vaXNlIG9mIHZhcmlhbmNlIM6yX3QgaXMgYWRkZWQuIEJlY2F1c2UgZWFjaCBzdGVwIGlzIEdhdXNzaWFuLCB0aGUgbWFyZ2luYWwgcSh4X3QgfCB4XzApIGlzIGFsc28gR2F1c3NpYW4gd2l0aCBhIGNsb3NlZC1mb3JtIGV4cHJlc3Npb246IHhfdCA9IOKIms6xzIVfdCB4XzAgKyDiiJooMS3OscyFX3QpIM61LCDOtSB+IE4oMCxJKSwgd2hlcmUgzrHMhV90ID0gzqBfe3M9MX1ee3R9ICgxLc6yX3MpLiBUaGlzIGxldHMgdXMgY29ycnVwdCB4XzAgdG8gYW55IHRpbWVzdGVwIHQgaW4gb25lIHN0ZXAsIGVuYWJsaW5nIGVmZmljaWVudCB0cmFpbmluZyBieSBzYW1wbGluZyB0IHVuaWZvcm1seS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG1ha2VfYWxwaGFfYmFyKGJldGEpOlxuICAgIFwiXCJcIkN1bXVsYXRpdmUgcHJvZHVjdDogYWxwaGFfYmFyX3QgPSBwcm9kX3tzPTF9Xnt0fSAoMSAtIGJldGFfcykuXCJcIlwiXG4gICAgcmV0dXJuIHRvcmNoLmN1bXByb2QoMS4wIC0gYmV0YSwgZGltPTApXG5cbmRlZiBxX3NhbXBsZSh4MCwgdCwgYWxwaGFfYmFyLCBub2lzZT1Ob25lKTpcbiAgICBcIlwiXCJcbiAgICBDbG9zZWQtZm9ybSBmb3J3YXJkIHByb2Nlc3M6IHEoeF90IHwgeF8wKS5cbiAgICB4X3QgPSBzcXJ0KGFscGhhX2Jhcl90KSAqIHgwICsgc3FydCgxIC0gYWxwaGFfYmFyX3QpICogZXBzXG4gICAgQWxsb3dzIGp1bXBpbmcgZGlyZWN0bHkgdG8gYW55IG5vaXNlIGxldmVsIHdpdGhvdXQgVCBzZXF1ZW50aWFsIHN0ZXBzLlxuICAgIFwiXCJcIlxuICAgIGlmIG5vaXNlIGlzIE5vbmU6XG4gICAgICAgIG5vaXNlID0gdG9yY2gucmFuZG5fbGlrZSh4MClcbiAgICBhYiAgID0gYWxwaGFfYmFyW3RdLnZpZXcoLTEsIDEsIDEsIDEpXG4gICAgcmV0dXJuIGFiLnNxcnQoKSAqIHgwICsgKDEgLSBhYikuc3FydCgpICogbm9pc2UsIG5vaXNlXG5cblQgICAgPSAxMDAwXG5iZXRhID0gdG9yY2gubGluc3BhY2UoMWUtNCwgMC4wMiwgVClcbmFiICAgPSBtYWtlX2FscGhhX2JhcihiZXRhKVxueDAgICA9IHRvcmNoLnJhbmRuKDQsIDMsIDMyLCAzMilcbnQgICAgPSB0b3JjaC50ZW5zb3IoWzAsIDI0OSwgNDk5LCA5OTldKVxueHQsIG5vaXNlID0gcV9zYW1wbGUoeDAsIHQsIGFiKVxucHJpbnQoZlwieDA6IHt4MC5zaGFwZX0gIHh0OiB7eHQuc2hhcGV9XCIpXG5mb3IgaSwgdGkgaW4gZW51bWVyYXRlKHQudG9saXN0KCkpOlxuICAgIHNuciA9IChhYlt0aV0gLyAoMSAtIGFiW3RpXSkpLml0ZW0oKVxuICAgIHByaW50KGZcIiAgdD17dGk6NGR9OiBhbHBoYV9iYXI9e2FiW3RpXTouNGZ9ICBTTlI9e3NucjouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTm9pc2UgU2NoZWR1bGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgzrJfdCBzY2hlZHVsZSBjb250cm9scyBob3cgcXVpY2tseSBzaWduYWwgaXMgZGVzdHJveWVkLiBUaGUgb3JpZ2luYWwgRERQTSB1c2VzIGEgbGluZWFyIHNjaGVkdWxlOiDOsl90IGluY3JlYXNlcyBsaW5lYXJseSBmcm9tIDEwXnstNH0gdG8gMC4wMiBvdmVyIFQ9MTAwMCBzdGVwcy4gSW1wcm92ZWQgRERQTSAoTmljaG9sIFx1MDAyNiBEaGFyaXdhbCwgMjAyMSkgZm91bmQgdGhhdCB0aGlzIHNjaGVkdWxlIGRlc3Ryb3lzIHNpZ25hbCB0b28gYWdncmVzc2l2ZWx5IGF0IHNtYWxsIHQgYW5kIGludHJvZHVjZWQgYSBjb3NpbmUgc2NoZWR1bGUgd2hlcmUgzrHMhV90ID0gY29zwrIoz4AvMiDDlyAodC9UICsgcykvKDErcykpLCByZXN1bHRpbmcgaW4gYSBzbW9vdGhlciBzaWduYWwtdG8tbm9pc2UgcmF0aW8gdHJhamVjdG9yeS4gVGhlIGNvc2luZSBzY2hlZHVsZSBpbXByb3ZlcyBzYW1wbGUgcXVhbGl0eSwgZXNwZWNpYWxseSBmb3IgaGlnaC1yZXNvbHV0aW9uIGltYWdlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbWF0aFxuXG5kZWYgbGluZWFyX3NjaGVkdWxlKFQ9MTAwMCwgYl9zdGFydD0xZS00LCBiX2VuZD0wLjAyKTpcbiAgICBcIlwiXCJPcmlnaW5hbCBERFBNIGxpbmVhciBiZXRhIHNjaGVkdWxlLlwiXCJcIlxuICAgIHJldHVybiB0b3JjaC5saW5zcGFjZShiX3N0YXJ0LCBiX2VuZCwgVClcblxuZGVmIGNvc2luZV9zY2hlZHVsZShUPTEwMDAsIHM9MC4wMDgpOlxuICAgIFwiXCJcIlxuICAgIENvc2luZSBzY2hlZHVsZSAoTmljaG9sIFx1MDAyNiBEaGFyaXdhbCAyMDIxKS5cbiAgICBhbHBoYV9iYXJfdCA9IGNvc14yKCBwaS8yICogKHQvVCArIHMpIC8gKDEgKyBzKSApXG4gICAgQXZvaWRzIG92ZXItZGVzdHJ1Y3Rpb24gb2Ygc2lnbmFsIGF0IHNtYWxsIHQuXG4gICAgXCJcIlwiXG4gICAgc3RlcHMgPSB0b3JjaC5hcmFuZ2UoVCArIDEsIGR0eXBlPXRvcmNoLmZsb2F0NjQpXG4gICAgZiAgICAgPSB0b3JjaC5jb3MoKChzdGVwcyAvIFQgKyBzKSAvICgxICsgcykpICogKG1hdGgucGkgLyAyKSkgKiogMlxuICAgIGFiICAgID0gKGYgLyBmWzBdKS5mbG9hdCgpXG4gICAgYmV0YSAgPSAoMSAtIGFiWzE6XSAvIGFiWzotMV0pLmNsYW1wKDAsIDAuOTk5KVxuICAgIHJldHVybiBiZXRhLCBhYlsxOl1cblxuYmV0YV9saW4gID0gbGluZWFyX3NjaGVkdWxlKClcbmFiX2xpbiAgICA9IHRvcmNoLmN1bXByb2QoMSAtIGJldGFfbGluLCBkaW09MClcbmJldGFfY29zLCBhYl9jb3MgPSBjb3NpbmVfc2NoZWR1bGUoKVxuXG5mb3IgbGFiZWwsIGFiIGluIFsoXHUwMDI3TGluZWFyIFx1MDAyNywgYWJfbGluKSwgKFx1MDAyN0Nvc2luZSBcdTAwMjcsIGFiX2NvcyldOlxuICAgIHZhbHMgPSBbYWJbaV0uaXRlbSgpIGZvciBpIGluIFswLCAyNDksIDQ5OSwgNzQ5LCA5OTldXVxuICAgIHByaW50KGZcIntsYWJlbH0gYWxwaGFfYmFyIGF0IHQ9MCwyNTAsNTAwLDc1MCw5OTk6IFwiXG4gICAgICAgICAgKyBcdTAwMjcgIFx1MDAyNy5qb2luKGZcdTAwMjd7djouNGZ9XHUwMDI3IGZvciB2IGluIHZhbHMpKVxucHJpbnQoXCJDb3NpbmU6IHNsb3dlciBzaWduYWwgZGVjYXkgYXQgbG93IHQsIHNpbWlsYXIgdG90YWwgYXQgVFwiKVxucHJpbnQoXCJMaW5lYXI6IHJlYWNoZXMgbmVhci16ZXJvIHNpZ25hbCBhdCB0XHUwMDNjVC8yIC0tIHByb2JsZW1hdGljIGZvciBoaWdoIHJlc1wiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNsb3NlZC1Gb3JtIE5vaXNpbmcgYW5kIFdoeSBJdCBNYXR0ZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2xvc2VkLWZvcm0gcSh4X3QgfCB4XzApIGlzIHRoZSBrZXkgdGhhdCBtYWtlcyBERFBNIHRyYWluaW5nIHRyYWN0YWJsZS4gV2l0aG91dCBpdCwgY29tcHV0aW5nIHhfdCB3b3VsZCByZXF1aXJlIHNpbXVsYXRpbmcgdCBzdGVwcyBvZiB0aGUgTWFya292IGNoYWluIGZvciBlYWNoIHRyYWluaW5nIGV4YW1wbGUsIG1ha2luZyBzYW1wbGluZyBvZiBoaWdoIHQgY29tcHV0YXRpb25hbGx5IGV4cGVuc2l2ZS4gV2l0aCB0aGUgY2xvc2VkIGZvcm0sIHRyYWluaW5nIHNhbXBsZXMgYSB0aW1lc3RlcCB0IH4gVW5pZm9ybVsxLCBUXSB1bmlmb3JtbHksIGNvbXB1dGVzIHhfdCA9IOKIms6xzIVfdCB4XzAgKyDiiJooMS3OscyFX3QpIM61IGluIGEgc2luZ2xlIG9wZXJhdGlvbiwgYW5kIHRyYWlucyB0aGUgZGVub2lzZXIgdG8gcHJlZGljdCDOtS4gVGhpcyByZXBhcmFtZXRlcml6YXRpb24gYWxzbyBtZWFucyB0aGUgbmV0d29yayBzZWVzIGRhdGEgYXQgYWxsIG5vaXNlIGxldmVscyBlcXVhbGx5IG9mdGVuIGR1cmluZyB0cmFpbmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXZlcnNlIFByb2Nlc3MgYW5kIFUtTmV0IERlbm9pc2VyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcmV2ZXJzZSBwcm9jZXNzIHBfzrgoeF97dC0xfSB8IHhfdCkgPSBOKHhfe3QtMX07IM68X864KHhfdCwgdCksIM6jX864KSBpcyBwYXJhbWV0ZXJpemVkIGJ5IGEgVS1OZXQuIFRoZSBVLU5ldCB0YWtlcyB4X3QgYW5kIHRpbWVzdGVwIHQgYXMgaW5wdXRzIGFuZCBwcmVkaWN0cyB0aGUgbm9pc2UgzrUgKG9yIGVxdWl2YWxlbnRseSB4XzApLiBUaW1lc3RlcCB0IGlzIGVuY29kZWQgd2l0aCBzaW51c29pZGFsIHBvc2l0aW9uYWwgZW1iZWRkaW5ncyAobWF0Y2hpbmcgVHJhbnNmb3JtZXItc3R5bGUgZW1iZWRkaW5ncykgYW5kIGluamVjdGVkIGludG8gZWFjaCByZXNpZHVhbCBibG9jayB2aWEgYW4gYWZmaW5lIHByb2plY3Rpb24uIFNraXAgY29ubmVjdGlvbnMgaW4gdGhlIFUtTmV0IHByZXNlcnZlIHNwYXRpYWwgaW5mb3JtYXRpb24sIGFuZCBhdHRlbnRpb24gbGF5ZXJzIGF0IGxvd2VyIHJlc29sdXRpb25zIGNhcHR1cmUgZ2xvYmFsIHN0cnVjdHVyZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBtYXRoXG5cbmNsYXNzIFNpblRpbWVFbWIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubGluID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoZGltLCBkaW0gKiA0KSwgbm4uU2lMVSgpLCBubi5MaW5lYXIoZGltICogNCwgZGltKSlcbiAgICAgICAgc2VsZi5kaW0gPSBkaW1cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB0KTpcbiAgICAgICAgaGFsZiA9IHNlbGYuZGltIC8vIDJcbiAgICAgICAgZiA9IHRvcmNoLmV4cCgtbWF0aC5sb2coMTAwMDApICogdG9yY2guYXJhbmdlKGhhbGYpLmZsb2F0KCkgLyBoYWxmKVxuICAgICAgICBlID0gdC5mbG9hdCgpLnVuc3F1ZWV6ZSgxKSAqIGYudW5zcXVlZXplKDApXG4gICAgICAgIHJldHVybiBzZWxmLmxpbih0b3JjaC5jYXQoW2Uuc2luKCksIGUuY29zKCldLCBkaW09LTEpKVxuXG5jbGFzcyBSZXNCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjLCB0X2RpbSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5vcm0xICA9IG5uLkdyb3VwTm9ybSg0LCBjKVxuICAgICAgICBzZWxmLmNvbnYxICA9IG5uLkNvbnYyZChjLCBjLCAzLCBwYWRkaW5nPTEpXG4gICAgICAgIHNlbGYudF9wcm9qID0gbm4uTGluZWFyKHRfZGltLCBjKVxuICAgICAgICBzZWxmLm5vcm0yICA9IG5uLkdyb3VwTm9ybSg0LCBjKVxuICAgICAgICBzZWxmLmNvbnYyICA9IG5uLkNvbnYyZChjLCBjLCAzLCBwYWRkaW5nPTEpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgdF9lbWIpOlxuICAgICAgICBoID0gc2VsZi5jb252MShGLnNpbHUoc2VsZi5ub3JtMSh4KSkpXG4gICAgICAgIGggPSBoICsgc2VsZi50X3Byb2oodF9lbWIpWzosIDosIE5vbmUsIE5vbmVdXG4gICAgICAgIHJldHVybiBzZWxmLmNvbnYyKEYuc2lsdShzZWxmLm5vcm0yKGgpKSkgKyB4XG5cbmNsYXNzIFNpbXBsZVVOZXQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgY19pbj0zLCBjPTY0LCB0X2RpbT0xMjgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi50X2VtYiA9IFNpblRpbWVFbWIodF9kaW0pXG4gICAgICAgIHNlbGYucHJvaiAgPSBubi5Db252MmQoY19pbiwgYywgMSlcbiAgICAgICAgc2VsZi5ibGsgICA9IFJlc0Jsb2NrKGMsIHRfZGltKVxuICAgICAgICBzZWxmLm91dCAgID0gbm4uQ29udjJkKGMsIGNfaW4sIDEpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgdCk6XG4gICAgICAgIHJldHVybiBzZWxmLm91dChzZWxmLmJsayhzZWxmLnByb2ooeCksIHNlbGYudF9lbWIodCkpKVxuXG5tb2RlbCA9IFNpbXBsZVVOZXQoKVxueCA9IHRvcmNoLnJhbmRuKDQsIDMsIDMyLCAzMilcbnQgPSB0b3JjaC5yYW5kaW50KDAsIDEwMDAsICg0LCkpXG5wcmludChmXCJJbnB1dDoge3guc2hhcGV9IC1cdTAwM2UgTm9pc2UgcHJlZDoge21vZGVsKHgsIHQpLnNoYXBlfVwiKVxucHJpbnQoXCJUaW1lIGVtYmVkZGluZzogc2ludXNvaWRhbCAtXHUwMDNlIE1MUCAtXHUwMDNlIGluamVjdGVkIGluIGVhY2ggUmVzQmxvY2tcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJERFBNIFNhbXBsaW5nIExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdlbmVyYXRpb24gc3RhcnRzIGZyb20geF9UIH4gTigwLCBJKSBhbmQgaXRlcmF0aXZlbHkgYXBwbGllcyB0aGUgcmV2ZXJzZSBzdGVwLiBBdCBlYWNoIHN0ZXAgdCwgdGhlIG1vZGVsIHByZWRpY3RzIM61LCByZWNvdmVycyBhbiBlc3RpbWF0ZSBvZiB4XzAsIGNvbXB1dGVzIHRoZSBwb3N0ZXJpb3IgbWVhbiDOvMyDX3QsIGFuZCBhZGRzIHN0b2NoYXN0aWMgbm9pc2Ugc2NhbGVkIGJ5IM6yX3QgKGV4Y2VwdCBhdCB0PTApLiBUaGUgcG9zdGVyaW9yIHZhcmlhbmNlIGlzIGZpeGVkIHRvIM6yzINfdCA9IM6yX3QoMS3OscyFX3t0LTF9KSAvICgxLc6xzIVfdCkuIEFmdGVyIFQ9MTAwMCBzdGVwcywgeF8wIGlzIHRoZSBnZW5lcmF0ZWQgc2FtcGxlLiBUaGUgc2FtcGxpbmcgaXMgc2xvdyAoVCBtb2RlbCBldmFsdWF0aW9ucyk7IHN1YnNlcXVlbnQgd29yayAoRERJTSwgRFBNLVNvbHZlcikgcmVkdWNlcyB0aGlzIHRvIDEwLTUwIHN0ZXBzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuQHRvcmNoLm5vX2dyYWQoKVxuZGVmIGRkcG1fc2FtcGxlKG1vZGVsLCBULCBiZXRhLCBhbHBoYV9iYXIsIHNoYXBlLCBkZXZpY2U9XHUwMDI3Y3B1XHUwMDI3KTpcbiAgICBcIlwiXCJERFBNIGFuY2VzdHJhbCBzYW1wbGluZzogc3RhcnQgZnJvbSB4X1QgfiBOKDAsSSksIGRlbm9pc2UgVCBzdGVwcy5cIlwiXCJcbiAgICBhbHBoYSAgPSAxLjAgLSBiZXRhXG4gICAgbW9kZWwuZXZhbCgpXG4gICAgeCA9IHRvcmNoLnJhbmRuKCpzaGFwZSwgZGV2aWNlPWRldmljZSlcbiAgICBmb3IgdF9pZHggaW4gcmV2ZXJzZWQocmFuZ2UoVCkpOlxuICAgICAgICB0X2IgICA9IHRvcmNoLmZ1bGwoKHNoYXBlWzBdLCksIHRfaWR4LCBkZXZpY2U9ZGV2aWNlLCBkdHlwZT10b3JjaC5sb25nKVxuICAgICAgICBlcHNfcCA9IG1vZGVsKHgsIHRfYikgICAgICAgICAgICAgICAgIyBwcmVkaWN0ZWQgbm9pc2VcbiAgICAgICAgYWJfdCAgPSBhbHBoYV9iYXJbdF9pZHhdXG4gICAgICAgIGFiX3AgID0gYWxwaGFfYmFyW3RfaWR4IC0gMV0gaWYgdF9pZHggXHUwMDNlIDAgZWxzZSB0b3JjaC50ZW5zb3IoMS4wKVxuICAgICAgICBidCAgICA9IGJldGFbdF9pZHhdXG4gICAgICAgICMgRXN0aW1hdGUgeDAgYW5kIGNvbXB1dGUgcG9zdGVyaW9yIG1lYW5cbiAgICAgICAgeDBfaGF0ID0gKHggLSAoMSAtIGFiX3QpLnNxcnQoKSAqIGVwc19wKSAvIGFiX3Quc3FydCgpXG4gICAgICAgIHgwX2hhdCA9IHgwX2hhdC5jbGFtcCgtMSwgMSlcbiAgICAgICAgYzEgPSBhYl9wLnNxcnQoKSAqIGJ0IC8gKDEgLSBhYl90KVxuICAgICAgICBjMiA9IGFscGhhW3RfaWR4XS5zcXJ0KCkgKiAoMSAtIGFiX3ApIC8gKDEgLSBhYl90KVxuICAgICAgICBtdSA9IGMxICogeDBfaGF0ICsgYzIgKiB4XG4gICAgICAgIG5vaXNlID0gdG9yY2gucmFuZG5fbGlrZSh4KSBpZiB0X2lkeCBcdTAwM2UgMCBlbHNlIHRvcmNoLnplcm9zX2xpa2UoeClcbiAgICAgICAgeCA9IG11ICsgYnQuc3FydCgpICogbm9pc2VcbiAgICAgICAgaWYgdF9pZHggJSAyNTAgPT0gMDpcbiAgICAgICAgICAgIHByaW50KGZcIiAgdD17dF9pZHg6NGR9ICB4LnN0ZD17eC5zdGQoKTouM2Z9ICB4MF9oYXQuc3RkPXt4MF9oYXQuc3RkKCk6LjNmfVwiKVxuICAgIHJldHVybiB4XG5cblQgPSAxMDAwXG5iZXRhICAgICAgPSB0b3JjaC5saW5zcGFjZSgxZS00LCAwLjAyLCBUKVxuYWxwaGFfYmFyID0gdG9yY2guY3VtcHJvZCgxIC0gYmV0YSwgZGltPTApXG5tb2RlbCAgICAgPSBTaW1wbGVVTmV0KClcbnNhbXBsZSAgICA9IGRkcG1fc2FtcGxlKG1vZGVsLCBULCBiZXRhLCBhbHBoYV9iYXIsIHNoYXBlPSgxLCAzLCAzMiwgMzIpKVxucHJpbnQoZlwiU2FtcGxlIHNoYXBlOiB7c2FtcGxlLnNoYXBlfVwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IFQ9MTAwMCBTdGVwcz8iLCJjb250ZW50IjoiRmV3ZXIgc3RlcHMgbWVhbnMgbGFyZ2VyIM6yX3QgcGVyIHN0ZXAsIG1ha2luZyB0aGUgR2F1c3NpYW4gcmV2ZXJzZSBhcHByb3hpbWF0aW9uIHBfzrgoeF97dC0xfXx4X3QpIOKJiCBOKM68X864LCDOo1/OuCkgbGVzcyBhY2N1cmF0ZSAodGhlIHRydWUgcmV2ZXJzZSBpcyBub24tR2F1c3NpYW4gZm9yIGxhcmdlIM6yKS4gVD0xMDAwIGVuc3VyZXMgZWFjaCBzdGVwIGlzIHNtYWxsIGVub3VnaCB0aGF0IHRoZSBHYXVzc2lhbiBhcHByb3hpbWF0aW9uIGhvbGRzLiBERElNIChTb25nIGV0IGFsLiAyMDIwKSByZWZvcm11bGF0ZXMgc2FtcGxpbmcgdG8gc2tpcCBzdGVwcyBkZXRlcm1pbmlzdGljYWxseSwgYWNoaWV2aW5nIGNvbXBhcmFibGUgcXVhbGl0eSBpbiAxMC01MCBzdGVwcyB3aXRob3V0IHJldHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IEREUE0gRXF1YXRpb25zIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkVxdWF0aW9uIiwiRm9ybXVsYSIsIlB1cnBvc2UiXSwicm93cyI6W1siRm9yd2FyZCBxKHhfdHx4X3t0LTF9KSIsIk4oeF90OyBzcXJ0KDEtYmV0YV90KSB4X3t0LTF9LCBiZXRhX3QgSSkiLCJBZGQgc21hbGwgR2F1c3NpYW4gbm9pc2UgYXQgZWFjaCBzdGVwIl0sWyJDbG9zZWQgZm9ybSBxKHhfdHx4XzApIiwiTih4X3Q7IHNxcnQoYWJfdCkgeF8wLCAoMS1hYl90KSBJKSIsIkp1bXAgdG8gYW55IG5vaXNlIGxldmVsIGluIG9uZSBzdGVwIl0sWyJSZXZlcnNlIHBfdGhldGEoeF97dC0xfXx4X3QpIiwiTih4X3t0LTF9OyBtdV90aGV0YSh4X3QsdCksIHNpZ21hX3ReMiBJKSIsIkxlYXJuZWQgR2F1c3NpYW4gZGVub2lzaW5nIHN0ZXAiXSxbIlNpbXBsaWZpZWQgbG9zcyBMX3NpbXBsZSIsIkVbfHxlcHMgLSBlcHNfdGhldGEoc3FydChhYl90KSB4MCArIHNxcnQoMS1hYl90KSBlcHMsIHQpfHxeMl0iLCJUcmFpbiBkZW5vaXNlciB0byBwcmVkaWN0IGFkZGVkIG5vaXNlIl0sWyJQb3N0ZXJpb3IgbWVhbiBtdV90aWxkZV90IiwiKHNxcnQoYWJfe3QtMX0pIGJldGFfdCB4MCArIHNxcnQoYWxwaGFfdCkoMS1hYl97dC0xfSkgeHQpIC8gKDEtYWJfdCkiLCJUcmFjdGFibGUgcmV2ZXJzZSBwb3N0ZXJpb3IgbWVhbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3VtbWFyeSBhbmQgSW5zaWdodHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkREUE0gYWNoaWV2ZXMgaGlnaCBzYW1wbGUgcXVhbGl0eSBieSBicmVha2luZyBnZW5lcmF0aW9uIGludG8gVCBzbWFsbCBkZW5vaXNpbmcgc3RlcHMsIGVhY2ggZWFzeSB0byBsZWFybiBpbmRpdmlkdWFsbHkuIFRoZSBjbG9zZWQtZm9ybSBmb3J3YXJkIHByb2Nlc3MgYW5kIHNpbXBsaWZpZWQgbm9pc2UtcHJlZGljdGlvbiBsb3NzIG1ha2UgdHJhaW5pbmcgc3RyYWlnaHRmb3J3YXJkLiBUaGUgbWFpbiBkcmF3YmFja3MgYXJlIHNsb3cgc2FtcGxpbmcgKFQgbW9kZWwgZXZhbHVhdGlvbnMpIGFuZCB0aGUgYWJzZW5jZSBvZiBhbiBlbmNvZGVyICh1bmxpa2UgVkFFcyBvciBmbG93cykuIFN1YnNlcXVlbnQgd29yayBhZGRyZXNzZXMgdGhlc2U6IERESU0gZm9yIGZhc3QgZGV0ZXJtaW5pc3RpYyBzYW1wbGluZywgbGF0ZW50IGRpZmZ1c2lvbiBtb2RlbHMgZm9yIGVmZmljaWVuY3ksIGFuZCBjbGFzc2lmaWVyLWZyZWUgZ3VpZGFuY2UgZm9yIGNvbmRpdGlvbmluZy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZvcndhcmQgcHJvY2VzczogZml4ZWQgTWFya292IGNoYWluIHdpdGggY2xvc2VkLWZvcm0gbWFyZ2luYWxzIC0tIG5vIHBhcmFtZXRlcnMgdG8gbGVhcm4uIiwiVHJhaW5pbmc6IHNhbXBsZSB0IH4gVW5pZm9ybSwgY29ycnVwdCB4MCB0byB4dCBpbiBvbmUgc3RlcCwgbWluaW1pemUgfHxlcHMgLSBlcHNfaGF0fHxeMi4iLCJSZXZlcnNlOiBUIEdhdXNzaWFuIHN0ZXBzIGxlYXJuZWQgYnkgVS1OZXQgY29uZGl0aW9uZWQgb24gdGltZXN0ZXAgdCB2aWEgc2ludXNvaWRhbCBlbWJlZGRpbmcuIiwiQmV0YSBzY2hlZHVsZTogbGluZWFyIChvcmlnaW5hbCkgb3IgY29zaW5lIChpbXByb3ZlZCkgLS0gY29zaW5lIGJldHRlciBhdCBwcmVzZXJ2aW5nIGxvdy10IHNpZ25hbC4iLCJTYW1wbGUgcXVhbGl0eTogY29tcGV0aXRpdmUgd2l0aCBHQU5zIG9uIENJRkFSLTEwIEZJRCB3aXRob3V0IGFkdmVyc2FyaWFsIHRyYWluaW5nLiIsIlNhbXBsaW5nIHNwZWVkOiBUPTEwMDAgZm9yd2FyZCBwYXNzZXMgLS0gdGhlIG1haW4gYm90dGxlbmVjayBhZGRyZXNzZWQgYnkgRERJTS9EUE0tU29sdmVyLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# DDPM — Forward Process and Reverse Denoising

DDPM (Ho et al., 2020) defines a generative model as the reverse of a fixed forward Markov chain that gradually corrupts data with Gaussian noise. The forward process q(x_t | x_{t-1}) = N(x_t; √(1-β_t) x_{t-1}, β_t I) has a closed-form marginal q(x_t | x_0) = N(x_t; √α̅_t x_0, (1-α̅_t) I), allowing direct sampling at any noise level without simulation. A U-Net learns to reverse this process: given noisy x_t and timestep t, predict the noise ε that was added. At generation, the model starts from x_T ~ N(0,I) and iteratively denoises over T=1000 steps.

## Forward Diffusion Process

The forward process adds noise step-by-step: q(x_t | x_{t-1}) = N(x_t; √(1-β_t) x_{t-1}, β_t I). The signal is attenuated by √(1-β_t) at each step while Gaussian noise of variance β_t is added. Because each step is Gaussian, the marginal q(x_t | x_0) is also Gaussian with a closed-form expression: x_t = √α̅_t x_0 + √(1-α̅_t) ε, ε ~ N(0,I), where α̅_t = Π_{s=1}^{t} (1-β_s). This lets us corrupt x_0 to any timestep t in one step, enabling efficient training by sampling t uniformly.

```python
import torch
import numpy as np

def make_alpha_bar(beta):
    """Cumulative product: alpha_bar_t = prod_{s=1}^{t} (1 - beta_s)."""
    return torch.cumprod(1.0 - beta, dim=0)

def q_sample(x0, t, alpha_bar, noise=None):
    """
    Closed-form forward process: q(x_t | x_0).
    x_t = sqrt(alpha_bar_t) * x0 + sqrt(1 - alpha_bar_t) * eps
    Allows jumping directly to any noise level without T sequential steps.
    """
    if noise is None:
        noise = torch.randn_like(x0)
    ab   = alpha_bar[t].view(-1, 1, 1, 1)
    return ab.sqrt() * x0 + (1 - ab).sqrt() * noise, noise

T    = 1000
beta = torch.linspace(1e-4, 0.02, T)
ab   = make_alpha_bar(beta)
x0   = torch.randn(4, 3, 32, 32)
t    = torch.tensor([0, 249, 499, 999])
xt, noise = q_sample(x0, t, ab)
print(f"x0: {x0.shape}  xt: {xt.shape}")
for i, ti in enumerate(t.tolist()):
    snr = (ab[ti] / (1 - ab[ti])).item()
    print(f"  t={ti:4d}: alpha_bar={ab[ti]:.4f}  SNR={snr:.4f}")
```

## Noise Schedules

The β_t schedule controls how quickly signal is destroyed. The original DDPM uses a linear schedule: β_t increases linearly from 10^{-4} to 0.02 over T=1000 steps. Improved DDPM (Nichol & Dhariwal, 2021) found that this schedule destroys signal too aggressively at small t and introduced a cosine schedule where α̅_t = cos²(π/2 × (t/T + s)/(1+s)), resulting in a smoother signal-to-noise ratio trajectory. The cosine schedule improves sample quality, especially for high-resolution images.

```python
import torch
import math

def linear_schedule(T=1000, b_start=1e-4, b_end=0.02):
    """Original DDPM linear beta schedule."""
    return torch.linspace(b_start, b_end, T)

def cosine_schedule(T=1000, s=0.008):
    """
    Cosine schedule (Nichol & Dhariwal 2021).
    alpha_bar_t = cos^2( pi/2 * (t/T + s) / (1 + s) )
    Avoids over-destruction of signal at small t.
    """
    steps = torch.arange(T + 1, dtype=torch.float64)
    f     = torch.cos(((steps / T + s) / (1 + s)) * (math.pi / 2)) ** 2
    ab    = (f / f[0]).float()
    beta  = (1 - ab[1:] / ab[:-1]).clamp(0, 0.999)
    return beta, ab[1:]

beta_lin  = linear_schedule()
ab_lin    = torch.cumprod(1 - beta_lin, dim=0)
beta_cos, ab_cos = cosine_schedule()

for label, ab in [('Linear ', ab_lin), ('Cosine ', ab_cos)]:
    vals = [ab[i].item() for i in [0, 249, 499, 749, 999]]
    print(f"{label} alpha_bar at t=0,250,500,750,999: "
          + '  '.join(f'{v:.4f}' for v in vals))
print("Cosine: slower signal decay at low t, similar total at T")
print("Linear: reaches near-zero signal at t<T/2 -- problematic for high res")
```

## Closed-Form Noising and Why It Matters

The closed-form q(x_t | x_0) is the key that makes DDPM training tractable. Without it, computing x_t would require simulating t steps of the Markov chain for each training example, making sampling of high t computationally expensive. With the closed form, training samples a timestep t ~ Uniform[1, T] uniformly, computes x_t = √α̅_t x_0 + √(1-α̅_t) ε in a single operation, and trains the denoiser to predict ε. This reparameterization also means the network sees data at all noise levels equally often during training.

## Reverse Process and U-Net Denoiser

The reverse process p_θ(x_{t-1} | x_t) = N(x_{t-1}; μ_θ(x_t, t), Σ_θ) is parameterized by a U-Net. The U-Net takes x_t and timestep t as inputs and predicts the noise ε (or equivalently x_0). Timestep t is encoded with sinusoidal positional embeddings (matching Transformer-style embeddings) and injected into each residual block via an affine projection. Skip connections in the U-Net preserve spatial information, and attention layers at lower resolutions capture global structure.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class SinTimeEmb(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.lin = nn.Sequential(nn.Linear(dim, dim * 4), nn.SiLU(), nn.Linear(dim * 4, dim))
        self.dim = dim
    def forward(self, t):
        half = self.dim // 2
        f = torch.exp(-math.log(10000) * torch.arange(half).float() / half)
        e = t.float().unsqueeze(1) * f.unsqueeze(0)
        return self.lin(torch.cat([e.sin(), e.cos()], dim=-1))

class ResBlock(nn.Module):
    def __init__(self, c, t_dim):
        super().__init__()
        self.norm1  = nn.GroupNorm(4, c)
        self.conv1  = nn.Conv2d(c, c, 3, padding=1)
        self.t_proj = nn.Linear(t_dim, c)
        self.norm2  = nn.GroupNorm(4, c)
        self.conv2  = nn.Conv2d(c, c, 3, padding=1)
    def forward(self, x, t_emb):
        h = self.conv1(F.silu(self.norm1(x)))
        h = h + self.t_proj(t_emb)[:, :, None, None]
        return self.conv2(F.silu(self.norm2(h))) + x

class SimpleUNet(nn.Module):
    def __init__(self, c_in=3, c=64, t_dim=128):
        super().__init__()
        self.t_emb = SinTimeEmb(t_dim)
        self.proj  = nn.Conv2d(c_in, c, 1)
        self.blk   = ResBlock(c, t_dim)
        self.out   = nn.Conv2d(c, c_in, 1)
    def forward(self, x, t):
        return self.out(self.blk(self.proj(x), self.t_emb(t)))

model = SimpleUNet()
x = torch.randn(4, 3, 32, 32)
t = torch.randint(0, 1000, (4,))
print(f"Input: {x.shape} -> Noise pred: {model(x, t).shape}")
print("Time embedding: sinusoidal -> MLP -> injected in each ResBlock")
```

## DDPM Sampling Loop

Generation starts from x_T ~ N(0, I) and iteratively applies the reverse step. At each step t, the model predicts ε, recovers an estimate of x_0, computes the posterior mean μ̃_t, and adds stochastic noise scaled by β_t (except at t=0). The posterior variance is fixed to β̃_t = β_t(1-α̅_{t-1}) / (1-α̅_t). After T=1000 steps, x_0 is the generated sample. The sampling is slow (T model evaluations); subsequent work (DDIM, DPM-Solver) reduces this to 10-50 steps.

```python
import torch

@torch.no_grad()
def ddpm_sample(model, T, beta, alpha_bar, shape, device='cpu'):
    """DDPM ancestral sampling: start from x_T ~ N(0,I), denoise T steps."""
    alpha  = 1.0 - beta
    model.eval()
    x = torch.randn(*shape, device=device)
    for t_idx in reversed(range(T)):
        t_b   = torch.full((shape[0],), t_idx, device=device, dtype=torch.long)
        eps_p = model(x, t_b)                # predicted noise
        ab_t  = alpha_bar[t_idx]
        ab_p  = alpha_bar[t_idx - 1] if t_idx > 0 else torch.tensor(1.0)
        bt    = beta[t_idx]
        # Estimate x0 and compute posterior mean
        x0_hat = (x - (1 - ab_t).sqrt() * eps_p) / ab_t.sqrt()
        x0_hat = x0_hat.clamp(-1, 1)
        c1 = ab_p.sqrt() * bt / (1 - ab_t)
        c2 = alpha[t_idx].sqrt() * (1 - ab_p) / (1 - ab_t)
        mu = c1 * x0_hat + c2 * x
        noise = torch.randn_like(x) if t_idx > 0 else torch.zeros_like(x)
        x = mu + bt.sqrt() * noise
        if t_idx % 250 == 0:
            print(f"  t={t_idx:4d}  x.std={x.std():.3f}  x0_hat.std={x0_hat.std():.3f}")
    return x

T = 1000
beta      = torch.linspace(1e-4, 0.02, T)
alpha_bar = torch.cumprod(1 - beta, dim=0)
model     = SimpleUNet()
sample    = ddpm_sample(model, T, beta, alpha_bar, shape=(1, 3, 32, 32))
print(f"Sample shape: {sample.shape}")
```

> **Why T=1000 Steps?**: Fewer steps means larger β_t per step, making the Gaussian reverse approximation p_θ(x_{t-1}|x_t) ≈ N(μ_θ, Σ_θ) less accurate (the true reverse is non-Gaussian for large β). T=1000 ensures each step is small enough that the Gaussian approximation holds. DDIM (Song et al. 2020) reformulates sampling to skip steps deterministically, achieving comparable quality in 10-50 steps without retraining.

## Key DDPM Equations

| Equation | Formula | Purpose |
| --- | --- | --- |
| Forward q(x_t|x_{t-1}) | N(x_t; sqrt(1-beta_t) x_{t-1}, beta_t I) | Add small Gaussian noise at each step |
| Closed form q(x_t|x_0) | N(x_t; sqrt(ab_t) x_0, (1-ab_t) I) | Jump to any noise level in one step |
| Reverse p_theta(x_{t-1}|x_t) | N(x_{t-1}; mu_theta(x_t,t), sigma_t^2 I) | Learned Gaussian denoising step |
| Simplified loss L_simple | E[||eps - eps_theta(sqrt(ab_t) x0 + sqrt(1-ab_t) eps, t)||^2] | Train denoiser to predict added noise |
| Posterior mean mu_tilde_t | (sqrt(ab_{t-1}) beta_t x0 + sqrt(alpha_t)(1-ab_{t-1}) xt) / (1-ab_t) | Tractable reverse posterior mean |

## Summary and Insights

DDPM achieves high sample quality by breaking generation into T small denoising steps, each easy to learn individually. The closed-form forward process and simplified noise-prediction loss make training straightforward. The main drawbacks are slow sampling (T model evaluations) and the absence of an encoder (unlike VAEs or flows). Subsequent work addresses these: DDIM for fast deterministic sampling, latent diffusion models for efficiency, and classifier-free guidance for conditioning.

- Forward process: fixed Markov chain with closed-form marginals -- no parameters to learn.
- Training: sample t ~ Uniform, corrupt x0 to xt in one step, minimize ||eps - eps_hat||^2.
- Reverse: T Gaussian steps learned by U-Net conditioned on timestep t via sinusoidal embedding.
- Beta schedule: linear (original) or cosine (improved) -- cosine better at preserving low-t signal.
- Sample quality: competitive with GANs on CIFAR-10 FID without adversarial training.
- Sampling speed: T=1000 forward passes -- the main bottleneck addressed by DDIM/DPM-Solver.

---

