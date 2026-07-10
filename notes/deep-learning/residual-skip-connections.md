---
title: "Residual / Skip Connections — Gradient Highway"
slug: "residual-skip-connections"
description: "Understand the gradient highway identity behind ResNets, compare pre- vs post-activation variants, implement DenseNet dense blocks, measure gradient magnitude improvement empirically, and survey skip connections across modern architectures."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlc2lkdWFsIGNvbm5lY3Rpb24geSA9IEYoeCxXKSArIHgsIGludHJvZHVjZWQgaW4gUmVzTmV0IChIZSBldCBhbC4gMjAxNSksIHNvbHZlZCB0aGUgZGVncmFkYXRpb24gcHJvYmxlbSDigJQgdGhlIGVtcGlyaWNhbCBvYnNlcnZhdGlvbiB0aGF0IHNpbXBseSBhZGRpbmcgbW9yZSBsYXllcnMgdG8gYSBwbGFpbiBuZXR3b3JrIGluY3JlYXNlcyB0cmFpbmluZyBlcnJvci4gVGhlIGluc2lnaHQgaXMgdGhhdCBsZWFybmluZyBhbiBpZGVudGl0eSBtYXBwaW5nIHRocm91Z2ggc3RhY2tlZCBub24tbGluZWFyIGxheWVycyBpcyBkaWZmaWN1bHQsIGJ1dCBsZWFybmluZyBhIHplcm8gcmVzaWR1YWwgRih4KSDiiaEgMCAoc28geSA9IHgpIGlzIHRyaXZpYWwuIFRoaXMgcmVmcmFtaW5nIG1ha2VzIHZlcnkgZGVlcCBuZXR3b3JrcyB0cmFpbmFibGUgYW5kIGVuYWJsZWQgMTAwKyBsYXllciBhcmNoaXRlY3R1cmVzIHRoYXQgZG9taW5hdGUgY29tcHV0ZXIgdmlzaW9uIGJlbmNobWFya3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgSGlnaHdheSDigJQgTWF0aGVtYXRpY2FsIFZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIHJlc2lkdWFsIGJsb2NrIHkgPSBGKHgpICsgeCwgdGhlIGdyYWRpZW50IHdpdGggcmVzcGVjdCB0byB0aGUgaW5wdXQgaXMg4oiCeS/iiIJ4ID0g4oiCRi/iiIJ4ICsgSS4gRXZlbiBpZiDiiIJGL+KIgnggaXMgc21hbGwgKHZhbmlzaGluZyByZWdpbWUpLCB0aGUgaWRlbnRpdHkgdGVybSBJIGVuc3VyZXMgdGhlIGdyYWRpZW50IGlzIGF0IGxlYXN0IDEuIEZvciBhIG5ldHdvcmsgb2YgTCByZXNpZHVhbCBibG9ja3MsIHRoZSBncmFkaWVudCBvZiB0aGUgbG9zcyB3aXRoIHJlc3BlY3QgdG8gaW5wdXQgeF9sIGNvbnRhaW5zIGFkZGl0aXZlIGlkZW50aXR5IHRlcm1zIHRoYXQgY2Fubm90IGFsbCBiZSB6ZXJvIHNpbXVsdGFuZW91c2x5IOKAlCB0aGlzIGlzIHRoZSBncmFkaWVudCBoaWdod2F5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBQb3N0QWN0UmVzQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKGQsZCksIG5uLkxheWVyTm9ybShkKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5uLkxpbmVhcihkLGQpLCBubi5MYXllck5vcm0oZCkpXG4gICAgICAgIHNlbGYucmVsdSA9IG5uLlJlTFUoKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiByZXR1cm4gc2VsZi5yZWx1KHNlbGYubmV0KHgpICsgeClcblxuY2xhc3MgUHJlQWN0UmVzQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwobm4uTGF5ZXJOb3JtKGQpLCBubi5SZUxVKCksIG5uLkxpbmVhcihkLGQpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5uLkxheWVyTm9ybShkKSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoZCxkKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYubmV0KHgpICsgeFxuXG5mb3IgbmFtZSwgQ2xzIGluIFsoXHUwMDI3UG9zdC1hY3RcdTAwMjcsIFBvc3RBY3RSZXNCbG9jayksIChcdTAwMjdQcmUtYWN0XHUwMDI3LCBQcmVBY3RSZXNCbG9jayldOlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKDApXG4gICAgbmV0ID0gbm4uU2VxdWVudGlhbCgqW0Nscyg2NCkgZm9yIF8gaW4gcmFuZ2UoMjApXSlcbiAgICBuZXQodG9yY2gucmFuZG4oMTYsIDY0KSkubWVhbigpLmJhY2t3YXJkKClcbiAgICBnID0gbGlzdChuZXRbMF0ucGFyYW1ldGVycygpKVswXS5ncmFkLm5vcm0oKS5pdGVtKClcbiAgICBwcmludChmXHUwMDI3e25hbWV9ICgyMCBibG9ja3MpOiBmaXJzdC1ibG9jayBncmFkID0ge2c6LjRlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQbGFpbiB2cyBSZXNpZHVhbCDigJQgR3JhZGllbnQgRGVwdGggQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRlZ3JhZGF0aW9uIHByb2JsZW0gaXMgbm90IG92ZXJmaXR0aW5nIOKAlCBhIGRlZXBlciBwbGFpbiBuZXR3b3JrIGhhcyBoaWdoZXIgdHJhaW5pbmcgZXJyb3IgdGhhbiBhIHNoYWxsb3dlciBvbmUuIFJlc2lkdWFscyBmaXggdGhpcyBieSBhbGxvd2luZyB0aGUgbmV0d29yayB0byBsZWFybiBuZWFyLWlkZW50aXR5IG1hcHBpbmdzIHRyaXZpYWxseS4gRW1waXJpY2FsbHksIHBsYWluIG5ldHdvcmtzIGxvc2UgZ3JhZGllbnQgc2lnbmFsIGFmdGVyIH4xNSBsYXllcnMgd2hpbGUgcmVzaWR1YWwgbmV0d29ya3MgbWFpbnRhaW4gaXQgdGhyb3VnaCAxMDArIGxheWVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGdyYWRfbm9ybV9maXJzdChibG9ja19mbiwgbiwgZD02NCwgc2VlZD0wKTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZChzZWVkKVxuICAgIG5ldCA9IG5uLlNlcXVlbnRpYWwoKltibG9ja19mbihkKSBmb3IgXyBpbiByYW5nZShuKV0pXG4gICAgbmV0KHRvcmNoLnJhbmRuKDE2LCBkKSkubWVhbigpLmJhY2t3YXJkKClcbiAgICByZXR1cm4gbGlzdChuZXRbMF0ucGFyYW1ldGVycygpKVswXS5ncmFkLm5vcm0oKS5pdGVtKClcblxuZGVmIHBsYWluX2Jsb2NrKGQpOlxuICAgIHJldHVybiBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkLGQpLCBubi5SZUxVKCksIG5uLkxpbmVhcihkLGQpLCBubi5SZUxVKCkpXG5cbmNsYXNzIFJlc0Jsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkLGQpLCBubi5SZUxVKCksIG5uLkxpbmVhcihkLGQpKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiByZXR1cm4gc2VsZi5uZXQoeCkgKyB4XG5cbnByaW50KGZcdTAwMjd7XCJEZXB0aFwiOlx1MDAzZTZ9IHwge1wiUGxhaW5cIjpcdTAwM2UxMn0gfCB7XCJSZXNpZHVhbFwiOlx1MDAzZTEyfVx1MDAyNylcbmZvciBuIGluIFs1LCAxMCwgMjAsIDQwXTpcbiAgICBwZyA9IGdyYWRfbm9ybV9maXJzdChwbGFpbl9ibG9jaywgbilcbiAgICByZyA9IGdyYWRfbm9ybV9maXJzdChSZXNCbG9jaywgbilcbiAgICBwcmludChmXHUwMDI3e246XHUwMDNlNn0gfCB7cGc6XHUwMDNlMTIuNGV9IHwge3JnOlx1MDAzZTEyLjRlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZW5zZU5ldCDigJQgRXh0cmVtZSBTa2lwIENvbm5lY3Rpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZW5zZU5ldCAoSHVhbmcgZXQgYWwuIDIwMTcpIGNvbm5lY3RzIGVhY2ggbGF5ZXIgdG8gYWxsIHN1YnNlcXVlbnQgbGF5ZXJzLCBjb25jYXRlbmF0aW5nIGZlYXR1cmUgbWFwczogbGF5ZXIgbCByZWNlaXZlcyBpbnB1dHMgZnJvbSBsYXllcnMgMCwgMSwgLi4uLCBs4oiSMS4gVGhpcyBjcmVhdGVzIEwoTCsxKS8yIGNvbm5lY3Rpb25zIGZvciBhIGJsb2NrIG9mIEwgbGF5ZXJzLiBUaGUgZ3JhZGllbnQgZnJvbSBhbnkgbGF0ZXIgbGF5ZXIgZmxvd3MgZGlyZWN0bHkgdG8gYWxsIGVhcmxpZXIgbGF5ZXJzLCBuZWFybHkgZWxpbWluYXRpbmcgdmFuaXNoaW5nIGdyYWRpZW50cy4gVGhlIGRvd25zaWRlIGlzIHF1YWRyYXRpYyBtZW1vcnkgZ3Jvd3RoLCBtaXRpZ2F0ZWQgYnkgMcOXMSBib3R0bGVuZWNrIGxheWVycyBhbmQgY29tcHJlc3Npb24gYXQgdHJhbnNpdGlvbiBsYXllcnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIERlbnNlTGF5ZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fZmVhdHVyZXMsIGdyb3d0aF9yYXRlPTE2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubGF5ZXIgPSBubi5TZXF1ZW50aWFsKG5uLkxheWVyTm9ybShpbl9mZWF0dXJlcyksIG5uLlJlTFUoKSwgbm4uTGluZWFyKGluX2ZlYXR1cmVzLCBncm93dGhfcmF0ZSkpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiB0b3JjaC5jYXQoW3gsIHNlbGYubGF5ZXIoeCldLCBkaW09LTEpXG5cbmNsYXNzIERlbnNlQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl9sYXllcnMsIGluX2ZlYXR1cmVzLCBncm93dGhfcmF0ZT0xNik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmxheWVycyA9IG5uLk1vZHVsZUxpc3QoKVxuICAgICAgICBjdXIgPSBpbl9mZWF0dXJlc1xuICAgICAgICBmb3IgXyBpbiByYW5nZShuX2xheWVycyk6XG4gICAgICAgICAgICBzZWxmLmxheWVycy5hcHBlbmQoRGVuc2VMYXllcihjdXIsIGdyb3d0aF9yYXRlKSlcbiAgICAgICAgICAgIGN1ciArPSBncm93dGhfcmF0ZVxuICAgICAgICBzZWxmLm91dF9mZWF0dXJlcyA9IGN1clxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBmb3IgbCBpbiBzZWxmLmxheWVyczogeCA9IGwoeClcbiAgICAgICAgcmV0dXJuIHhcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmJsb2NrID0gRGVuc2VCbG9jayhuX2xheWVycz02LCBpbl9mZWF0dXJlcz02NCwgZ3Jvd3RoX3JhdGU9MTYpXG54ID0gdG9yY2gucmFuZG4oOCwgNjQsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbm91dCA9IGJsb2NrKHgpXG5vdXQubWVhbigpLmJhY2t3YXJkKClcbnByaW50KGZcdTAwMjdEZW5zZUJsb2NrOiBpbj17NjR9LCBvdXQ9e2Jsb2NrLm91dF9mZWF0dXJlc31cdTAwMjcpXG5wcmludChmXHUwMDI3Rmlyc3QgbGF5ZXIgd2VpZ2h0IGdyYWQ6IHtsaXN0KGJsb2NrLmxheWVyc1swXS5wYXJhbWV0ZXJzKCkpWzBdLmdyYWQubm9ybSgpOi40ZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2tpcCBDb25uZWN0aW9ucyBpbiBUcmFuc2Zvcm1lcnMgYW5kIFUtTmV0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFdmVyeSBUcmFuc2Zvcm1lciBibG9jayBhcHBsaWVzIHJlc2lkdWFsIGNvbm5lY3Rpb25zIHR3aWNlOiB4ID0geCArIEF0dGVudGlvbihMTih4KSkgYW5kIHggPSB4ICsgRkZOKExOKHgpKS4gVGhlIHByZS1MTiB2YXJpYW50IHBsYWNlcyBMYXllck5vcm0gaW5zaWRlIHRoZSByZXNpZHVhbCBicmFuY2gsIGVuc3VyaW5nIGEgY2xlYW4gZ3JhZGllbnQgcGF0aCBmcm9tIG91dHB1dCB0byBldmVyeSBpbnB1dCB0b2tlbiB3aXRob3V0IExOIGludGVyZmVyaW5nIHdpdGggdGhlIGlkZW50aXR5LiBJbiBVLU5ldCwgZW5jb2RlciBmZWF0dXJlIG1hcHMgYXJlIGNvbmNhdGVuYXRlZCB3aXRoIGRlY29kZXIgZmVhdHVyZSBtYXBzIGF0IGVhY2ggcmVzb2x1dGlvbiDigJQgc2tpcCBjb25uZWN0aW9ucyBjYXJyeSBwcmVjaXNlIHNwYXRpYWwgbG9jYWxpemF0aW9uIGFjcm9zcyB0aGUgYm90dGxlbmVjayB0aGF0IHdvdWxkIG90aGVyd2lzZSBiZSBsb3N0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBQcmVMTlRyYW5zZm9ybWVyQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgbl9oZWFkcywgZF9mZik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmxuMSAgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5hdHRuID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYubG4yICA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmZmbiAgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKSwgbm4uR0VMVSgpLCBubi5MaW5lYXIoZF9mZiwgZF9tb2RlbCkpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGgsIF8gPSBzZWxmLmF0dG4oc2VsZi5sbjEoeCksIHNlbGYubG4xKHgpLCBzZWxmLmxuMSh4KSlcbiAgICAgICAgeCA9IHggKyBoXG4gICAgICAgIHJldHVybiB4ICsgc2VsZi5mZm4oc2VsZi5sbjIoeCkpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5ibG9ja3MgPSBubi5TZXF1ZW50aWFsKCpbUHJlTE5UcmFuc2Zvcm1lckJsb2NrKDEyOCwgNCwgNTEyKSBmb3IgXyBpbiByYW5nZSgxMildKVxueCA9IHRvcmNoLnJhbmRuKDIsIDMyLCAxMjgpXG5ibG9ja3MoeCkubWVhbigpLmJhY2t3YXJkKClcbmcgPSBsaXN0KGJsb2Nrc1swXS5wYXJhbWV0ZXJzKCkpWzBdLmdyYWQubm9ybSgpLml0ZW0oKVxucHJpbnQoZlx1MDAyN1ByZS1MTiBUcmFuc2Zvcm1lciAoMTIgYmxvY2tzKTogZmlyc3QtYmxvY2sgZ3JhZCA9IHtnOi40ZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVzaWR1YWxzIGFzIEVuc2VtYmxlcyBvZiBTaGFsbG93IFBhdGhzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWZWl0IGV0IGFsLiAoMjAxNikgc2hvd2VkIHRoYXQgcmVzaWR1YWwgbmV0d29ya3MgYmVoYXZlIGxpa2UgZW5zZW1ibGVzIG9mIGV4cG9uZW50aWFsbHkgbWFueSBzaGFsbG93IG5ldHdvcmtzLiBBIFJlc05ldCB3aXRoIEwgYmxvY2tzIGhhcyAyXkwgcGF0aHMgdGhyb3VnaCB0aGUgbmV0d29yayAoZWFjaCBza2lwIGNhbiBiZSB0YWtlbiBvciBieXBhc3NlZCkuIEluIHByYWN0aWNlLCBzaG9ydGVyIHBhdGhzIGRvbWluYXRlIGdyYWRpZW50IGZsb3cgZHVyaW5nIHRyYWluaW5nIOKAlCBwYXRocyBvZiBsZW5ndGggMSAoZGlyZWN0IHNraXApIGNvbnRyaWJ1dGUgdGhlIG1vc3QuIFRoaXMgZXhwbGFpbnMgd2h5IFJlc05ldHMgYXJlIHJvYnVzdCB0byBsYXllciBkZWxldGlvbjogcmVtb3Zpbmcgb25lIGJsb2NrIHJlbW92ZXMgb25seSBPKDJee0wtMX0pIHBhdGhzIG9mIDJeTCB0b3RhbCwgbGVhdmluZyBtb3N0IG9mIHRoZSBlbnNlbWJsZSBpbnRhY3QuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGlzIGVuc2VtYmxlIHZpZXcgYWxzbyBleHBsYWlucyB0aGUgZGVwdGggZWZmaWNpZW5jeSBvZiBSZXNOZXRzLiBUcmFpbmluZyBhIFJlc05ldC01MCBpcyBub3QgZXF1aXZhbGVudCB0byB0cmFpbmluZyBhIDUwLWxheWVyIG5ldHdvcmsg4oCUIGl0IGlzIG1vcmUgbGlrZSB0cmFpbmluZyBhbiBlbnNlbWJsZSBvZiBuZXR3b3JrcyB3aXRoIGRlcHRocyByYW5naW5nIGZyb20gMCB0byA1MC4gVGhlIGVmZmVjdGl2ZSBkZXB0aCBpcyBtdWNoIHNoYWxsb3dlciB0aGFuIHRoZSBub21pbmFsIGRlcHRoLCB3aGljaCBpcyB3aHkgMTAwMC1sYXllciBSZXNOZXRzIHJlbWFpbiB0cmFpbmFibGUgZGVzcGl0ZSB0aGVvcmV0aWNhbCBjb25jZXJucyBhYm91dCBncmFkaWVudCBmbG93IGF0IGV4dHJlbWUgZGVwdGguIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZW5zZW1ibGUgaW50ZXJwcmV0YXRpb24gaGFzIHByYWN0aWNhbCBpbXBsaWNhdGlvbnM6IHN0b2NoYXN0aWMgZGVwdGggKEh1YW5nIGV0IGFsLiAyMDE2KSByYW5kb21seSBkcm9wcyBlbnRpcmUgcmVzaWR1YWwgYmxvY2tzIGR1cmluZyB0cmFpbmluZyAocmVwbGFjaW5nIHRoZSBibG9jayBvdXRwdXQgd2l0aCB0aGUgaWRlbnRpdHkpLCBzaW11bGF0aW5nIHRyYWluaW5nIG9uIHN1Ym5ldHdvcmtzIG9mIHZhcnlpbmcgbGVuZ3RoLiBUaGlzIGFjdHMgYXMgZGF0YSBhdWdtZW50YXRpb24gb3ZlciB0aGUgZW5zZW1ibGUgb2YgcGF0aHMsIGltcHJvdmluZyBnZW5lcmFsaXphdGlvbiBhbmQgcmVkdWNpbmcgdHJhaW5pbmcgdGltZSBieSB+MjUlIGZvciBSZXNOZXQtMTAwMS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaGVuIHRvIFVzZSBQcm9qZWN0aW9uIFNob3J0Y3V0cyJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJQcm9qZWN0aW9uIFNob3J0Y3V0cyBmb3IgRGltZW5zaW9uIENoYW5nZXMiLCJjb250ZW50IjoiV2hlbiBpbnB1dCBhbmQgb3V0cHV0IGRpbWVuc2lvbnMgZGlmZmVyIChlLmcuLCBzdHJpZGUtMiBkb3duc2FtcGxpbmcgZG91YmxlcyBjaGFubmVscyksIHRoZSBza2lwIGNvbm5lY3Rpb24gbmVlZHMgYSAxw5cxIGNvbnYgcHJvamVjdGlvbjogeCA9IEYoeCkgKyBXX3PCt3guIFVzZSBwcm9qZWN0aW9uIHNob3J0Y3V0cyBvbmx5IHdoZXJlIGRpbWVuc2lvbnMgY2hhbmdlIOKAlCBmb3Igc2FtZS1kaW1lbnNpb24gYmxvY2tzIHRoZSBpZGVudGl0eSBzaG9ydGN1dCAoemVybyBwYXJhbWV0ZXJzLCBwZXJmZWN0IGdyYWRpZW50KSBpcyBzdHJpY3RseSBiZXR0ZXIuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFyY2hpdGVjdHVyZSIsIlNraXAgdHlwZSIsIkdyYWRpZW50IGZsb3ciLCJNYXggcHJhY3RpY2FsIGRlcHRoIiwiTWVtb3J5IG92ZXJoZWFkIl0sInJvd3MiOltbIlBsYWluIG5ldHdvcmsiLCJOb25lIiwiRXhwb25lbnRpYWwgZGVjYXkiLCJ+MTDigJMxNSBsYXllcnMiLCJMb3dlc3QiXSxbIkhpZ2h3YXkgbmV0d29yayIsIkdhdGVkOiBUwrdGKHgpKygx4oiSVCnCt3giLCJDb250cm9sbGVkIGJ1dCBjYW4gc3RpbGwgdmFuaXNoIiwifjUwIGxheWVycyIsIkdhdGUgcGFyYW1zIl0sWyJSZXNOZXQgKHBvc3QtYWN0KSIsIklkZW50aXR5ICt4IGFmdGVyIGFjdGl2YXRpb24iLCJTdHJvbmcg4oCUIEkgdGVybSBhbHdheXMgcHJlc2VudCIsIjEwMOKAkzEwMDArIGxheWVycyIsIk5lZ2xpZ2libGUiXSxbIlJlc05ldCAocHJlLWFjdCkiLCJDbGVhbiBpZGVudGl0eSDigJQgbm8gUmVMVSBvbiBza2lwIHBhdGgiLCJDbGVhbmVyIOKAlCBwcmVmZXJyZWQgZm9yIHZlcnkgZGVlcCBuZXRzIiwiMTAwMCsgbGF5ZXJzIiwiTmVnbGlnaWJsZSJdLFsiRGVuc2VOZXQiLCJDb25jYXQgYWxsIHByZXZpb3VzIGZlYXR1cmUgbWFwcyIsIkV4dHJlbWVseSBzdHJvbmcg4oCUIGRpcmVjdCBwYXRocyIsIjEwMOKAkzIwMCBsYXllcnMgcHJhY3RpY2FsIiwiUXVhZHJhdGljIGluIGJsb2NrIGRlcHRoIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRoZSBpZGVudGl0eSBzaG9ydGN1dCBjb3N0cyB6ZXJvIHBhcmFtZXRlcnMgYW5kIG5lZ2xpZ2libGUgY29tcHV0ZSDigJQgdXNlIGl0IGJ5IGRlZmF1bHQgZm9yIHNhbWUtZGltZW5zaW9uIGxheWVycy4iLCJQcmUtYWN0aXZhdGlvbiBSZXNOZXQgcHJvdmlkZXMgYSBjbGVhbmVyIGdyYWRpZW50IHBhdGggYW5kIHNsaWdodGx5IGJldHRlciBhY2N1cmFjeSBhdCB2ZXJ5IGhpZ2ggZGVwdGhzLiIsIkRlbnNlTmV0IGhhcyBiZXR0ZXIgZ3JhZGllbnQgZmxvdyB0aGFuIFJlc05ldCBidXQgcmVxdWlyZXMgY2FyZWZ1bCBtZW1vcnkgbWFuYWdlbWVudCBwYXN0IDEwMCBsYXllcnMuIiwiQWxsIFRyYW5zZm9ybWVyIGFyY2hpdGVjdHVyZXMgcmVseSBvbiByZXNpZHVhbCBjb25uZWN0aW9ucyDigJQgcHJlLUxOIGlzIG5vdyBwcmVmZXJyZWQgb3ZlciBwb3N0LUxOIGZvciBzdGFiaWxpdHkuIiwiVmVpdCBldCBhbC4gc2hvd2VkIFJlc05ldHMgYmVoYXZlIGFzIGVuc2VtYmxlcyBvZiAyXkwgcGF0aHMg4oCUIHJlbW92aW5nIGFueSBzaW5nbGUgcGF0aCBiYXJlbHkgYWZmZWN0cyBvdXRwdXQuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Residual / Skip Connections — Gradient Highway

The residual connection y = F(x,W) + x, introduced in ResNet (He et al. 2015), solved the degradation problem — the empirical observation that simply adding more layers to a plain network increases training error. The insight is that learning an identity mapping through stacked non-linear layers is difficult, but learning a zero residual F(x) ≡ 0 (so y = x) is trivial. This reframing makes very deep networks trainable and enabled 100+ layer architectures that dominate computer vision benchmarks.

## Gradient Highway — Mathematical View

For a residual block y = F(x) + x, the gradient with respect to the input is ∂y/∂x = ∂F/∂x + I. Even if ∂F/∂x is small (vanishing regime), the identity term I ensures the gradient is at least 1. For a network of L residual blocks, the gradient of the loss with respect to input x_l contains additive identity terms that cannot all be zero simultaneously — this is the gradient highway.

```python
import torch
import torch.nn as nn

class PostActResBlock(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(d,d), nn.LayerNorm(d), nn.ReLU(),
                                  nn.Linear(d,d), nn.LayerNorm(d))
        self.relu = nn.ReLU()
    def forward(self, x): return self.relu(self.net(x) + x)

class PreActResBlock(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.net = nn.Sequential(nn.LayerNorm(d), nn.ReLU(), nn.Linear(d,d),
                                  nn.LayerNorm(d), nn.ReLU(), nn.Linear(d,d))
    def forward(self, x): return self.net(x) + x

for name, Cls in [('Post-act', PostActResBlock), ('Pre-act', PreActResBlock)]:
    torch.manual_seed(0)
    net = nn.Sequential(*[Cls(64) for _ in range(20)])
    net(torch.randn(16, 64)).mean().backward()
    g = list(net[0].parameters())[0].grad.norm().item()
    print(f'{name} (20 blocks): first-block grad = {g:.4e}')
```

## Plain vs Residual — Gradient Depth Comparison

The degradation problem is not overfitting — a deeper plain network has higher training error than a shallower one. Residuals fix this by allowing the network to learn near-identity mappings trivially. Empirically, plain networks lose gradient signal after ~15 layers while residual networks maintain it through 100+ layers.

```python
import torch
import torch.nn as nn

def grad_norm_first(block_fn, n, d=64, seed=0):
    torch.manual_seed(seed)
    net = nn.Sequential(*[block_fn(d) for _ in range(n)])
    net(torch.randn(16, d)).mean().backward()
    return list(net[0].parameters())[0].grad.norm().item()

def plain_block(d):
    return nn.Sequential(nn.Linear(d,d), nn.ReLU(), nn.Linear(d,d), nn.ReLU())

class ResBlock(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(d,d), nn.ReLU(), nn.Linear(d,d))
    def forward(self, x): return self.net(x) + x

print(f'{"Depth":>6} | {"Plain":>12} | {"Residual":>12}')
for n in [5, 10, 20, 40]:
    pg = grad_norm_first(plain_block, n)
    rg = grad_norm_first(ResBlock, n)
    print(f'{n:>6} | {pg:>12.4e} | {rg:>12.4e}')
```

## DenseNet — Extreme Skip Connections

DenseNet (Huang et al. 2017) connects each layer to all subsequent layers, concatenating feature maps: layer l receives inputs from layers 0, 1, ..., l−1. This creates L(L+1)/2 connections for a block of L layers. The gradient from any later layer flows directly to all earlier layers, nearly eliminating vanishing gradients. The downside is quadratic memory growth, mitigated by 1×1 bottleneck layers and compression at transition layers.

```python
import torch
import torch.nn as nn

class DenseLayer(nn.Module):
    def __init__(self, in_features, growth_rate=16):
        super().__init__()
        self.layer = nn.Sequential(nn.LayerNorm(in_features), nn.ReLU(), nn.Linear(in_features, growth_rate))
    def forward(self, x):
        return torch.cat([x, self.layer(x)], dim=-1)

class DenseBlock(nn.Module):
    def __init__(self, n_layers, in_features, growth_rate=16):
        super().__init__()
        self.layers = nn.ModuleList()
        cur = in_features
        for _ in range(n_layers):
            self.layers.append(DenseLayer(cur, growth_rate))
            cur += growth_rate
        self.out_features = cur
    def forward(self, x):
        for l in self.layers: x = l(x)
        return x

torch.manual_seed(0)
block = DenseBlock(n_layers=6, in_features=64, growth_rate=16)
x = torch.randn(8, 64, requires_grad=True)
out = block(x)
out.mean().backward()
print(f'DenseBlock: in={64}, out={block.out_features}')
print(f'First layer weight grad: {list(block.layers[0].parameters())[0].grad.norm():.4e}')
```

## Skip Connections in Transformers and U-Net

Every Transformer block applies residual connections twice: x = x + Attention(LN(x)) and x = x + FFN(LN(x)). The pre-LN variant places LayerNorm inside the residual branch, ensuring a clean gradient path from output to every input token without LN interfering with the identity. In U-Net, encoder feature maps are concatenated with decoder feature maps at each resolution — skip connections carry precise spatial localization across the bottleneck that would otherwise be lost.

```python
import torch
import torch.nn as nn

class PreLNTransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff):
        super().__init__()
        self.ln1  = nn.LayerNorm(d_model)
        self.attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.ln2  = nn.LayerNorm(d_model)
        self.ffn  = nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(), nn.Linear(d_ff, d_model))
    def forward(self, x):
        h, _ = self.attn(self.ln1(x), self.ln1(x), self.ln1(x))
        x = x + h
        return x + self.ffn(self.ln2(x))

torch.manual_seed(0)
blocks = nn.Sequential(*[PreLNTransformerBlock(128, 4, 512) for _ in range(12)])
x = torch.randn(2, 32, 128)
blocks(x).mean().backward()
g = list(blocks[0].parameters())[0].grad.norm().item()
print(f'Pre-LN Transformer (12 blocks): first-block grad = {g:.4e}')
```

## Residuals as Ensembles of Shallow Paths

Veit et al. (2016) showed that residual networks behave like ensembles of exponentially many shallow networks. A ResNet with L blocks has 2^L paths through the network (each skip can be taken or bypassed). In practice, shorter paths dominate gradient flow during training — paths of length 1 (direct skip) contribute the most. This explains why ResNets are robust to layer deletion: removing one block removes only O(2^{L-1}) paths of 2^L total, leaving most of the ensemble intact.

This ensemble view also explains the depth efficiency of ResNets. Training a ResNet-50 is not equivalent to training a 50-layer network — it is more like training an ensemble of networks with depths ranging from 0 to 50. The effective depth is much shallower than the nominal depth, which is why 1000-layer ResNets remain trainable despite theoretical concerns about gradient flow at extreme depth.

The ensemble interpretation has practical implications: stochastic depth (Huang et al. 2016) randomly drops entire residual blocks during training (replacing the block output with the identity), simulating training on subnetworks of varying length. This acts as data augmentation over the ensemble of paths, improving generalization and reducing training time by ~25% for ResNet-1001.

## When to Use Projection Shortcuts

> **Projection Shortcuts for Dimension Changes**: When input and output dimensions differ (e.g., stride-2 downsampling doubles channels), the skip connection needs a 1×1 conv projection: x = F(x) + W_s·x. Use projection shortcuts only where dimensions change — for same-dimension blocks the identity shortcut (zero parameters, perfect gradient) is strictly better.

| Architecture | Skip type | Gradient flow | Max practical depth | Memory overhead |
| --- | --- | --- | --- | --- |
| Plain network | None | Exponential decay | ~10–15 layers | Lowest |
| Highway network | Gated: T·F(x)+(1−T)·x | Controlled but can still vanish | ~50 layers | Gate params |
| ResNet (post-act) | Identity +x after activation | Strong — I term always present | 100–1000+ layers | Negligible |
| ResNet (pre-act) | Clean identity — no ReLU on skip path | Cleaner — preferred for very deep nets | 1000+ layers | Negligible |
| DenseNet | Concat all previous feature maps | Extremely strong — direct paths | 100–200 layers practical | Quadratic in block depth |

- The identity shortcut costs zero parameters and negligible compute — use it by default for same-dimension layers.
- Pre-activation ResNet provides a cleaner gradient path and slightly better accuracy at very high depths.
- DenseNet has better gradient flow than ResNet but requires careful memory management past 100 layers.
- All Transformer architectures rely on residual connections — pre-LN is now preferred over post-LN for stability.
- Veit et al. showed ResNets behave as ensembles of 2^L paths — removing any single path barely affects output.

---

