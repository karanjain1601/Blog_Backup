---
title: "Luong Attention — Multiplicative Attention"
slug: "luong-attention"
description: "Luong's multiplicative attention variants — dot, general, and concat scoring — plus global vs local attention windows and input-feeding for state-aware decoding."
tags: ["deep-learning", "rnns", "sequence-models", "state-space-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTHVvbmcgZXQgYWwuICgyMDE1KSBwdWJsaXNoZWQgYXR0ZW50aW9uIG1lY2hhbmlzbXMgdGhhdCBjb21wbGVtZW50ZWQgYW5kIGV4dGVuZGVkIEJhaGRhbmF1XHUwMDI3cyBvcmlnaW5hbCBmb3JtdWxhdGlvbi4gV2hlcmUgQmFoZGFuYXUgdXNlcyB0aGUgcHJldmlvdXMgZGVjb2RlciBzdGF0ZSBz4rG84oKL4oKBIHRvIGNvbXB1dGUgYWxpZ25tZW50LCBMdW9uZyB1c2VzIHRoZSBjdXJyZW50IGRlY29kZXIgc3RhdGUgc+KxvCBhZnRlciBpdCBoYXMgYWxyZWFkeSBpbmNvcnBvcmF0ZWQgdGhlIGVuY29kZWQgaW5wdXQuIEx1b25nIGFsc28gaW50cm9kdWNlZCB0aHJlZSBkaXN0aW5jdCBzY29yaW5nIGZ1bmN0aW9ucyDigJQgZG90LCBnZW5lcmFsLCBhbmQgY29uY2F0IOKAlCBldmFsdWF0ZWQgdGhlbSBlbXBpcmljYWxseSwgYW5kIHByb3Bvc2VkIGxvY2FsIGF0dGVudGlvbiBhcyBhIGNvbXB1dGF0aW9uYWxseSBjaGVhcGVyIGFsdGVybmF0aXZlIHRvIGdsb2JhbCAoYWxsLWVuY29kZXIpIGF0dGVudGlvbi4gVGhlaXIgaW5wdXQtZmVlZGluZyB0ZWNobmlxdWUgZnVydGhlciBpbXByb3ZlZCByZXN1bHRzIGJ5IG1ha2luZyB0aGUgZGVjb2RlciBhd2FyZSBvZiBwcmV2aW91cyBhdHRlbnRpb24gZGVjaXNpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRocmVlIFNjb3JpbmcgRnVuY3Rpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMdW9uZ1x1MDAyN3MgdGhyZWUgc2NvcmluZyBmdW5jdGlvbnMgZWFjaCByZXByZXNlbnQgYSBkaWZmZXJlbnQgdHJhZGUtb2ZmIGJldHdlZW4gZXhwcmVzc2l2ZW5lc3MgYW5kIGNvbXB1dGF0aW9uLiBUaGUgZG90IHByb2R1Y3Qgc2NvcmUgZeG1ouKxvCA9IHPisbzhtYBo4bWiIGlzIHRoZSBzaW1wbGVzdCBhbmQgZmFzdGVzdCDigJQgaXQgcmVxdWlyZXMgbm8gbGVhcm5lZCBwYXJhbWV0ZXJzIGFuZCB3b3JrcyB3ZWxsIHdoZW4gZW5jb2RlciBhbmQgZGVjb2RlciBoaWRkZW4gZGltZW5zaW9ucyBtYXRjaC4gVGhlIGdlbmVyYWwgc2NvcmUgZeG1ouKxvCA9IHPisbzhtYBX4oKQaOG1oiBpbnRyb2R1Y2VzIGEgbGVhcm5hYmxlIHdlaWdodCBtYXRyaXggV+KCkCwgZW5hYmxpbmcgdGhlIG1vZGVsIHRvIHByb2plY3QgZW5jb2RlciBhbmQgZGVjb2RlciBzdGF0ZXMgaW50byBhIHNoYXJlZCBhbGlnbm1lbnQgc3BhY2UuIFRoZSBjb25jYXQgc2NvcmUgZeG1ouKxvCA9IHbhtYAgdGFuaChX4oKQW3Pisbw7aOG1ol0pIGNvbmNhdGVuYXRlcyB0aGUgc3RhdGVzIGJlZm9yZSBwcm9qZWN0aW5nIOKAlCBlcXVpdmFsZW50IHRvIEJhaGRhbmF1XHUwMDI3cyBmb3JtdWxhdGlvbiBidXQgdXNpbmcgdGhlIGN1cnJlbnQgc3RhdGUgc+KxvCByYXRoZXIgdGhhbiB0aGUgcHJldmlvdXMgc+KxvOKCi+KCgS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkRvdDogZeG1ouKxvCA9IHPisbzhtYBo4bWiIOKAlCBubyBwYXJhbWV0ZXJzLCBPKEgpIHBlciBwYWlyLCByZXF1aXJlcyBzYW1lIGhpZGRlbiBkaW0iLCJHZW5lcmFsOiBl4bWi4rG8ID0gc+KxvOG1gFfigpBo4bWiIOKAlCBsZWFybmFibGUgV+KCkCDiiIgg4oSdXntkZWNfaCDDlyBlbmNfaH0sIE8oSMKyKSBwYXJhbXMiLCJDb25jYXQ6IGXhtaLisbwgPSB24bWAIHRhbmgoV+KCkFtz4rG8O2jhtaJdKSDigJQgc2FtZSBhcyBCYWhkYW5hdSBidXQgdXNlcyBjdXJyZW50IGRlY29kZXIgc3RhdGUiLCJBbGwgdGhyZWU6IM6x4bWi4rG8ID0gc29mdG1heChl4bWi4rG8KSwgY+KxvCA9IM6j4bWiIM6x4bWi4rG8aOG1oiDigJQgc2FtZSBjb250ZXh0IGFnZ3JlZ2F0aW9uIHN0ZXAiLCJMdW9uZyB1c2VzIHPisbwgKGFmdGVyIHN0ZXApLCBCYWhkYW5hdSB1c2VzIHPisbzigovigoEgKGJlZm9yZSBzdGVwKSDigJQga2V5IGRpZmZlcmVuY2UiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAxIOKAlCBMdW9uZyBEb3QsIEdlbmVyYWwsIGFuZCBDb25jYXQgQXR0ZW50aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEx1b25nQXR0ZW50aW9uKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTHVvbmcgYXR0ZW50aW9uIHdpdGggZG90LCBnZW5lcmFsLCBvciBjb25jYXQgc2NvcmluZy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbW9kZSwgaGlkZGVuX2RpbSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm1vZGUgPSBtb2RlXG4gICAgICAgIGlmIG1vZGUgPT0gXHUwMDI3Z2VuZXJhbFx1MDAyNzpcbiAgICAgICAgICAgIHNlbGYuVyA9IG5uLkxpbmVhcihoaWRkZW5fZGltLCBoaWRkZW5fZGltLCBiaWFzPUZhbHNlKVxuICAgICAgICBlbGlmIG1vZGUgPT0gXHUwMDI3Y29uY2F0XHUwMDI3OlxuICAgICAgICAgICAgc2VsZi5XID0gbm4uTGluZWFyKGhpZGRlbl9kaW0gKiAyLCBoaWRkZW5fZGltLCBiaWFzPUZhbHNlKVxuICAgICAgICAgICAgc2VsZi52ID0gbm4uTGluZWFyKGhpZGRlbl9kaW0sIDEsIGJpYXM9RmFsc2UpXG5cbiAgICBkZWYgc2NvcmUoc2VsZiwgcywgaCk6XG4gICAgICAgICMgczogKGJhdGNoLCBoaWRkZW4pLCBoOiAoYmF0Y2gsIHNyY19sZW4sIGhpZGRlbilcbiAgICAgICAgaWYgc2VsZi5tb2RlID09IFx1MDAyN2RvdFx1MDAyNzpcbiAgICAgICAgICAgIHJldHVybiB0b3JjaC5ibW0oaCwgcy51bnNxdWVlemUoLTEpKS5zcXVlZXplKC0xKSAgICAgICMgKEIsIFQpXG4gICAgICAgIGVsaWYgc2VsZi5tb2RlID09IFx1MDAyN2dlbmVyYWxcdTAwMjc6XG4gICAgICAgICAgICByZXR1cm4gdG9yY2guYm1tKGgsIHNlbGYuVyhzKS51bnNxdWVlemUoLTEpKS5zcXVlZXplKC0xKVxuICAgICAgICBlbGlmIHNlbGYubW9kZSA9PSBcdTAwMjdjb25jYXRcdTAwMjc6XG4gICAgICAgICAgICBzX2V4cCA9IHMudW5zcXVlZXplKDEpLmV4cGFuZF9hcyhoKVxuICAgICAgICAgICAgcmV0dXJuIHNlbGYudih0b3JjaC50YW5oKHNlbGYuVyh0b3JjaC5jYXQoW3NfZXhwLCBoXSwgZGltPS0xKSkpKS5zcXVlZXplKC0xKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgcywgZW5jX291dHB1dHMpOlxuICAgICAgICBlbmVyZ3kgID0gc2VsZi5zY29yZShzLCBlbmNfb3V0cHV0cykgICAgICAgICAgICMgKEIsIFQpXG4gICAgICAgIGFscGhhICAgPSBGLnNvZnRtYXgoZW5lcmd5LCBkaW09LTEpXG4gICAgICAgIGNvbnRleHQgPSAoYWxwaGEudW5zcXVlZXplKC0xKSAqIGVuY19vdXRwdXRzKS5zdW0oMSlcbiAgICAgICAgcmV0dXJuIGNvbnRleHQsIGFscGhhXG5cbiMgQ29tcGFyZSBhbGwgdGhyZWUgbW9kZXMgb24gcmFuZG9tIHRlbnNvcnNcbkIsIFQsIEggPSA0LCAyMCwgMjU2XG5lbmMgPSB0b3JjaC5yYW5kbihCLCBULCBIKVxuZGVjX3MgPSB0b3JjaC5yYW5kbihCLCBIKVxuZm9yIG1vZGUgaW4gW1x1MDAyN2RvdFx1MDAyNywgXHUwMDI3Z2VuZXJhbFx1MDAyNywgXHUwMDI3Y29uY2F0XHUwMDI3XTpcbiAgICBhdHRuID0gTHVvbmdBdHRlbnRpb24obW9kZSwgSClcbiAgICBjdHgsIGEgPSBhdHRuKGRlY19zLCBlbmMpXG4gICAgcHJpbnQoZlwie21vZGU6OHN9IHwgY29udGV4dD17Y3R4LnNoYXBlfSB8IHdlaWdodHNfc3VtPXthLnN1bSgtMSkubWVhbigpOi4zZn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHbG9iYWwgdnMgTG9jYWwgQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHbG9iYWwgYXR0ZW50aW9uIGF0dGVuZHMgb3ZlciBhbGwgVHMgZW5jb2RlciBwb3NpdGlvbnMgYXQgZXZlcnkgZGVjb2RlciBzdGVwIOKAlCB0aGlzIGlzIHdoYXQgQmFoZGFuYXUgdXNlcyBhbmQgd2hhdCBtb3N0IGltcGxlbWVudGF0aW9ucyBkZWZhdWx0IHRvLiBMdW9uZyBwcm9wb3NlZCBsb2NhbCBhdHRlbnRpb24gYXMgYSBjb21wdXRhdGlvbmFsbHkgY2hlYXBlciBhbHRlcm5hdGl2ZTogcHJlZGljdCBhbiBhbGlnbmVkIHBvc2l0aW9uIHB0IGZvciBlYWNoIGRlY29kZXIgc3RlcCwgdGhlbiBhdHRlbmQgb25seSB3aXRoaW4gYSB3aW5kb3cgW3B0IC0gRCwgcHQgKyBEXSBvZiAyRCsxIGVuY29kZXIgcG9zaXRpb25zLiBUaGUgd2luZG93IHBvc2l0aW9uIHB0IGlzIHByZWRpY3RlZCBieSB0aGUgZGVjb2RlciBzdGF0ZTogcHQgPSBUcyDCtyBzaWdtb2lkKHbigprhtYAgdGFuaChX4oKac+KxvCkpLiBBIEdhdXNzaWFuIGRpc3RyaWJ1dGlvbiBHKHB0LCAoRC8yKcKyKSBmdXJ0aGVyIGRvd24td2VpZ2h0cyBwb3NpdGlvbnMgZmFyIGZyb20gdGhlIGNlbnRlciwgZW5jb3VyYWdpbmcgc21vb3RoIGxvY2FsaXplZCBhdHRlbnRpb24uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHbG9iYWw6IGF0dGVuZHMgYWxsIFRzIGVuY29kZXIgcG9zaXRpb25zIOKAlCBPKFRzKSBwZXIgc3RlcCwgZnVsbCBjb3ZlcmFnZSIsIkxvY2FsLW06IG1vbm90b25lIGFsaWdubWVudCwgd2luZG93IHNoaWZ0cyBpbmNyZW1lbnRhbGx5IOKAlCBubyBwb3NpdGlvbiBwcmVkaWN0aW9uIiwiTG9jYWwtcDogcHJlZGljdCBwdCBmcm9tIGRlY29kZXIgc3RhdGUsIEdhdXNzaWFuIHBlbmFsdHkgd2l0aGluIHdpbmRvdyBvZiB3aWR0aCAyRCsxIiwiTG9jYWwgYXR0ZW50aW9uIHJlZHVjZXMgY29tcHV0YXRpb24gZnJvbSBPKFRzwrdUdCkgdG8gTyhEwrdUdCkg4oCUIHVzZWZ1bCBmb3IgbG9uZyBzb3VyY2VzIiwiVHlwaWNhbCBEID0gMTAgY2FwdHVyZXMgwrExMCBwb3NpdGlvbnMsIHN1ZmZpY2llbnQgZm9yIG1vc3QgdHJhbnNsYXRpb24gcGFpcnMiXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IldoZW4gdG8gVXNlIExvY2FsIHZzIEdsb2JhbCBBdHRlbnRpb24iLCJjb250ZW50IjoiVXNlIGdsb2JhbCBhdHRlbnRpb24gZm9yIHN0YW5kYXJkIHNlbnRlbmNlLWxldmVsIE5NVCDigJQgaXQgaXMgc2ltcGxlciBhbmQgdGhlIE8oVMKyKSBjb3N0IGlzIG5lZ2xpZ2libGUgZm9yIFQgXHUwMDNjIDIwMC4gUHJlZmVyIGxvY2FsIGF0dGVudGlvbiB3aGVuIGVuY29kaW5nIHZlcnkgbG9uZyBzZXF1ZW5jZXMgKGRvY3VtZW50cywgYXVkaW8gZnJhbWVzKSB3aGVyZSBhdHRlbmRpbmcgZXZlcnkgcG9zaXRpb24gYXQgZXZlcnkgc3RlcCBpcyBwcm9oaWJpdGl2ZS4gRm9yIGluZmVyZW5jZSBzcGVlZCwgbG9jYWwgYXR0ZW50aW9uIHdpdGggYSBmaXhlZCB3aW5kb3cgYWxzbyBlbmFibGVzIG1vcmUgcHJlZGljdGFibGUgbGF0ZW5jeS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIExvY2FsIEF0dGVudGlvbiB3aXRoIEdhdXNzaWFuIFdpbmRvdyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBMb2NhbEF0dGVudGlvbihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkx1b25nIGxvY2FsLXAgYXR0ZW50aW9uOiBwcmVkaWN0IHdpbmRvdyBjZW50ZXIsIGFwcGx5IEdhdXNzaWFuIHBlbmFsdHkuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGhpZGRlbl9kaW0sIHdpbmRvd19EPTUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5EICAgID0gd2luZG93X0RcbiAgICAgICAgc2VsZi5XX3AgID0gbm4uTGluZWFyKGhpZGRlbl9kaW0sIGhpZGRlbl9kaW0pXG4gICAgICAgIHNlbGYudl9wICA9IG5uLkxpbmVhcihoaWRkZW5fZGltLCAxKVxuICAgICAgICBzZWxmLldfYSAgPSBubi5MaW5lYXIoaGlkZGVuX2RpbSAqIDIsIGhpZGRlbl9kaW0sIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYudl9hICA9IG5uLkxpbmVhcihoaWRkZW5fZGltLCAxLCBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgcywgZW5jX291dHB1dHMsIHNyY19sZW4pOlxuICAgICAgICAjIFByZWRpY3QgYWxpZ25lZCBwb3NpdGlvbiBwdCBpbiBbMCwgc3JjX2xlbl1cbiAgICAgICAgcHQgPSBzcmNfbGVuICogdG9yY2guc2lnbW9pZChzZWxmLnZfcCh0b3JjaC50YW5oKHNlbGYuV19wKHMpKSkpLnNxdWVlemUoLTEpICAjIChCLClcbiAgICAgICAgcG9zaXRpb25zID0gdG9yY2guYXJhbmdlKHNyY19sZW4sIGR0eXBlPXRvcmNoLmZsb2F0MzIsIGRldmljZT1zLmRldmljZSkgICAgICAjIChULClcbiAgICAgICAgc2lnbWEgPSBzZWxmLkQgLyAyLjBcbiAgICAgICAgZ2F1c3MgPSB0b3JjaC5leHAoLShwb3NpdGlvbnMgLSBwdC51bnNxdWVlemUoMSkpKioyIC8gKDIgKiBzaWdtYSoqMikpICAgICAgICAjIChCLCBUKVxuICAgICAgICAjIEF0dGVudGlvbiBzY29yZVxuICAgICAgICBzX2V4cCA9IHMudW5zcXVlZXplKDEpLmV4cGFuZF9hcyhlbmNfb3V0cHV0cylcbiAgICAgICAgZSA9IHNlbGYudl9hKHRvcmNoLnRhbmgoc2VsZi5XX2EodG9yY2guY2F0KFtzX2V4cCwgZW5jX291dHB1dHNdLCBkaW09LTEpKSkpLnNxdWVlemUoLTEpXG4gICAgICAgIGFscGhhID0gRi5zb2Z0bWF4KGUsIGRpbT0tMSkgKiBnYXVzc1xuICAgICAgICBhbHBoYSA9IGFscGhhIC8gKGFscGhhLnN1bSgtMSwga2VlcGRpbT1UcnVlKSArIDFlLTkpICAgIyByZW5vcm1hbGl6ZVxuICAgICAgICBjb250ZXh0ID0gKGFscGhhLnVuc3F1ZWV6ZSgtMSkgKiBlbmNfb3V0cHV0cykuc3VtKDEpXG4gICAgICAgIHJldHVybiBjb250ZXh0LCBhbHBoYSwgcHRcblxuQiwgVCwgSCA9IDIsIDMwLCAxMjhcbmVuYyA9IHRvcmNoLnJhbmRuKEIsIFQsIEgpXG5zICAgPSB0b3JjaC5yYW5kbihCLCBIKVxubG9jYWxfYXR0biA9IExvY2FsQXR0ZW50aW9uKEgsIHdpbmRvd19EPTUpXG5jdHgsIHdlaWdodHMsIHBvcyA9IGxvY2FsX2F0dG4ocywgZW5jLCBUKVxucHJpbnQoZlwiQ29udGV4dDoge2N0eC5zaGFwZX0sIFByZWRpY3RlZCBwb3NpdGlvbnM6IHtbZlx1MDAyN3twOi4xZn1cdTAwMjcgZm9yIHAgaW4gcG9zLnRvbGlzdCgpXX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDMg4oCUIElucHV0LUZlZWRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IklucHV0LWZlZWRpbmcgaXMgTHVvbmdcdTAwMjdzIGtleSBjb250cmlidXRpb24gYmV5b25kIHRoZSBzY29yaW5nIGZ1bmN0aW9uczogYXQgZWFjaCBkZWNvZGVyIHN0ZXAsIHRoZSBwcmV2aW91cyBhdHRlbnRpb24gdmVjdG9yIChjb250ZXh0IHZlY3RvcikgaXMgY29uY2F0ZW5hdGVkIHRvIHRoZSBjdXJyZW50IGRlY29kZXIgaW5wdXQgZW1iZWRkaW5nIGJlZm9yZSBwYXNzaW5nIHRocm91Z2ggdGhlIFJOTiBjZWxsLiBUaGlzIG1ha2VzIHRoZSBkZWNvZGVyIGF3YXJlIG9mIHdoYXQgaXQgYXR0ZW5kZWQgdG8gaW4gdGhlIHByZXZpb3VzIHN0ZXAg4oCUIG1vZGVsaW5nIHRoZSBhbGlnbm1lbnQgaGlzdG9yeSByYXRoZXIgdGhhbiB0cmVhdGluZyBlYWNoIHN0ZXAgaW5kZXBlbmRlbnRseS4gSW5wdXQtZmVlZGluZyBjb25zaXN0ZW50bHkgaW1wcm92ZXMgdHJhbnNsYXRpb24gcXVhbGl0eSBhbmQgaXMgbm93IHN0YW5kYXJkIHByYWN0aWNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBJbnB1dEZlZWRpbmdEZWNvZGVyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTHVvbmcgZGVjb2RlciB3aXRoIGlucHV0LWZlZWRpbmc6IHByZXZpb3VzIGNvbnRleHQgY29uY2F0ZW5hdGVkIHRvIGlucHV0LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB2b2NhYl9zaXplLCBlbWJlZF9kaW0sIGhpZGRlbl9kaW0pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbWJlZCAgID0gbm4uRW1iZWRkaW5nKHZvY2FiX3NpemUsIGVtYmVkX2RpbSlcbiAgICAgICAgIyBJbnB1dCA9IGVtYmVkZGluZyArIHByZXZpb3VzIGF0dGVudGlvbiBjb250ZXh0XG4gICAgICAgIHNlbGYucm5uICAgICA9IG5uLkdSVUNlbGwoZW1iZWRfZGltICsgaGlkZGVuX2RpbSwgaGlkZGVuX2RpbSlcbiAgICAgICAgc2VsZi5XX2F0dG4gID0gbm4uTGluZWFyKGhpZGRlbl9kaW0sIGhpZGRlbl9kaW0sIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuV19jICAgICA9IG5uLkxpbmVhcihoaWRkZW5fZGltICogMiwgaGlkZGVuX2RpbSlcbiAgICAgICAgc2VsZi5mYyAgICAgID0gbm4uTGluZWFyKGhpZGRlbl9kaW0sIHZvY2FiX3NpemUpXG5cbiAgICBkZWYgYXR0ZW5kKHNlbGYsIHMsIGVuY19vdXQpOlxuICAgICAgICAjIEx1b25nIGdlbmVyYWwgYXR0ZW50aW9uIHVzaW5nIGN1cnJlbnQgc3RhdGUgc1xuICAgICAgICBlICAgICA9IHRvcmNoLmJtbShlbmNfb3V0LCBzZWxmLldfYXR0bihzKS51bnNxdWVlemUoLTEpKS5zcXVlZXplKC0xKVxuICAgICAgICBhbHBoYSA9IEYuc29mdG1heChlLCBkaW09LTEpXG4gICAgICAgIHJldHVybiAoYWxwaGEudW5zcXVlZXplKC0xKSAqIGVuY19vdXQpLnN1bSgxKSwgYWxwaGFcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHRva2VuLCBzLCBlbmNfb3V0LCBwcmV2X2N0eCk6XG4gICAgICAgIGVtYiAgICAgICA9IHNlbGYuZW1iZWQodG9rZW4pXG4gICAgICAgIHNfbmV3ICAgICA9IHNlbGYucm5uKHRvcmNoLmNhdChbZW1iLCBwcmV2X2N0eF0sIGRpbT0tMSksIHMpICAjIGlucHV0LWZlZWRpbmdcbiAgICAgICAgY3R4LCBhbHBoYSA9IHNlbGYuYXR0ZW5kKHNfbmV3LCBlbmNfb3V0KVxuICAgICAgICBoX3RpbGRlICAgPSB0b3JjaC50YW5oKHNlbGYuV19jKHRvcmNoLmNhdChbc19uZXcsIGN0eF0sIGRpbT0tMSkpKVxuICAgICAgICByZXR1cm4gc2VsZi5mYyhoX3RpbGRlKSwgc19uZXcsIGN0eCwgYWxwaGFcblxuViwgRSwgSCwgQiwgVCA9IDgwMDAsIDEyOCwgMjU2LCAyLCAxNVxuZGVjICAgICA9IElucHV0RmVlZGluZ0RlY29kZXIoViwgRSwgSClcbmVuY19vdXQgPSB0b3JjaC5yYW5kbihCLCBULCBIKVxuczAsIGN0eDAgPSB0b3JjaC5yYW5kbihCLCBIKSwgdG9yY2guemVyb3MoQiwgSClcbnRvayAgICAgPSB0b3JjaC5yYW5kaW50KDAsIFYsIChCLCkpXG5sb2dpdHMsIHMxLCBjdHgxLCBhID0gZGVjKHRvaywgczAsIGVuY19vdXQsIGN0eDApXG5wcmludChmXCJsb2dpdHM9e2xvZ2l0cy5zaGFwZX0sIHM9e3MxLnNoYXBlfSwgY3R4PXtjdHgxLnNoYXBlfSwgYWxwaGFfc3VtPXthLnN1bSgtMSl9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSA0IOKAlCBCYWhkYW5hdSB2cyBMdW9uZyBDb21wYXJpc29uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG4jIFNpbXVsYXRlZCBCTEVVIHZzIHNlbnRlbmNlIGxlbmd0aCAoYmFzZWQgb24gTHVvbmcgZXQgYWwuIDIwMTUgZmluZGluZ3MpXG5jb25maWdzID0ge1xuICAgIFx1MDAyN05vIGF0dGVudGlvblx1MDAyNzogICAgICAgICAgIFsyMS41LCAxOS44LCAxNy4yLCAxNC4xLCAxMC4zXSxcbiAgICBcdTAwMjdCYWhkYW5hdSBhZGRpdGl2ZVx1MDAyNzogICAgICBbMjYuMSwgMjUuMywgMjMuOSwgMjIuMCwgMTkuNV0sXG4gICAgXHUwMDI3THVvbmcgZG90XHUwMDI3OiAgICAgICAgICAgICAgWzI1LjgsIDI1LjAsIDIzLjUsIDIxLjcsIDE5LjFdLFxuICAgIFx1MDAyN0x1b25nIGdlbmVyYWxcdTAwMjc6ICAgICAgICAgIFsyNi4zLCAyNS42LCAyNC4yLCAyMi40LCAxOS45XSxcbiAgICBcdTAwMjdMdW9uZyBjb25jYXRcdTAwMjc6ICAgICAgICAgICBbMjUuOSwgMjUuMiwgMjMuOCwgMjEuOSwgMTkuNF0sXG4gICAgXHUwMDI3THVvbmcgKyBpbnB1dC1mZWVkaW5nXHUwMDI3OiAgWzI3LjEsIDI2LjQsIDI1LjAsIDIzLjMsIDIwLjhdLFxufVxubGVuZ3RocyA9IFsxMCwgMjAsIDMwLCA0MCwgNTBdXG5jb2xvcnMgID0gW1x1MDAyN2dyYXlcdTAwMjcsIFx1MDAyN3N0ZWVsYmx1ZVx1MDAyNywgXHUwMDI3dG9tYXRvXHUwMDI3LCBcdTAwMjdmb3Jlc3RncmVlblx1MDAyNywgXHUwMDI3b3JhbmdlXHUwMDI3LCBcdTAwMjdwdXJwbGVcdTAwMjddXG5tYXJrZXJzID0gW1x1MDAyN3hcdTAwMjcsIFx1MDAyN3NcdTAwMjcsIFx1MDAyN29cdTAwMjcsIFx1MDAyN15cdTAwMjcsIFx1MDAyN0RcdTAwMjcsIFx1MDAyNypcdTAwMjddXG5cbmZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oMTAsIDYpKVxuZm9yIChuYW1lLCBzY29yZXMpLCBjb2xvciwgbWFya2VyIGluIHppcChjb25maWdzLml0ZW1zKCksIGNvbG9ycywgbWFya2Vycyk6XG4gICAgYXgucGxvdChsZW5ndGhzLCBzY29yZXMsIG1hcmtlcj1tYXJrZXIsIGNvbG9yPWNvbG9yLFxuICAgICAgICAgICAgbGFiZWw9bmFtZSwgbGluZXdpZHRoPTIsIG1hcmtlcnNpemU9NylcbmF4LnNldF94bGFiZWwoXHUwMDI3U2VudGVuY2UgbGVuZ3RoICh0b2tlbnMpXHUwMDI3LCBmb250c2l6ZT0xMilcbmF4LnNldF95bGFiZWwoXHUwMDI3QkxFVSBTY29yZVx1MDAyNywgZm9udHNpemU9MTIpXG5heC5zZXRfdGl0bGUoXHUwMDI3QmFoZGFuYXUgdnMgTHVvbmcgQXR0ZW50aW9uIFZhcmlhbnRzIOKAlCBCTEVVIHZzIExlbmd0aFx1MDAyNywgZm9udHNpemU9MTMpXG5heC5sZWdlbmQoZm9udHNpemU9OSwgbG9jPVx1MDAyN3VwcGVyIHJpZ2h0XHUwMDI3KVxuYXguZ3JpZChUcnVlLCBhbHBoYT0wLjMpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zYXZlZmlnKFx1MDAyN2F0dGVudGlvbl9jb21wYXJpc29uLnBuZ1x1MDAyNywgZHBpPTE1MClcbnBsdC5zaG93KClcbnByaW50KFwiTHVvbmcgKyBpbnB1dC1mZWVkaW5nIG91dHBlcmZvcm1zIGFsbCB2YXJpYW50cyBvbiBsb25nIHNlcXVlbmNlcy5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgRGlmZmVyZW5jZXMgZnJvbSBCYWhkYW5hdSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hpbGUgQmFoZGFuYXUgYW5kIEx1b25nIGF0dGVudGlvbiBzaGFyZSB0aGUgd2VpZ2h0ZWQtc3VtIGNvbnRleHQgbWVjaGFuaXNtLCB0aGV5IGRpZmZlciBpbiBmb3VyIGltcG9ydGFudCB3YXlzLiBGaXJzdCwgdGhlIGRlY29kZXIgc3RhdGUgdGltaW5nOiBCYWhkYW5hdSB1c2VzIHPisbzigovigoEgKGJlZm9yZSBnZW5lcmF0aW5nIHN0ZXAgaikgdG8gY29tcHV0ZSBhbGlnbm1lbnQsIHdoaWxlIEx1b25nIHVzZXMgc+KxvCAoYWZ0ZXIgcnVubmluZyB0aGUgUk5OIGZvciBzdGVwIGopIOKAlCBMdW9uZ1x1MDAyN3MgYXBwcm9hY2ggZ2l2ZXMgdGhlIGFsaWdubWVudCBuZXR3b3JrIGFjY2VzcyB0byBtb3JlIHVwLXRvLWRhdGUgaW5mb3JtYXRpb24uIFNlY29uZCwgdGhlIHNjb3JlIGZ1bmN0aW9uczogQmFoZGFuYXUgb25seSBkZWZpbmVzIHRoZSBhZGRpdGl2ZSBmb3JtOyBMdW9uZyBzeXN0ZW1hdGljYWxseSBjb21wYXJlcyBkb3QsIGdlbmVyYWwsIGFuZCBjb25jYXQuIFRoaXJkLCBsb2NhbCB2cyBnbG9iYWw6IEJhaGRhbmF1IHVzZXMgZ2xvYmFsIGF0dGVudGlvbiBvbmx5LiBGb3VydGgsIGlucHV0LWZlZWRpbmc6IEx1b25nIGV4cGxpY2l0bHkgbW9kZWxzIGFsaWdubWVudCBoaXN0b3J5IGJ5IGZlZWRpbmcgdGhlIHByZXZpb3VzIGNvbnRleHQgdmVjdG9yIGJhY2sgYXMgZGVjb2RlciBpbnB1dC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJCYWhkYW5hdSIsIkx1b25nIGRvdCIsIkx1b25nIGdlbmVyYWwiLCJMdW9uZyBjb25jYXQiXSwicm93cyI6W1siRGVjb2RlciBzdGF0ZSB1c2VkIiwic+KxvOKCi+KCgSAocHJldikiLCJz4rG8IChjdXJyZW50KSIsInPisbwgKGN1cnJlbnQpIiwic+KxvCAoY3VycmVudCkiXSxbIlNjb3JlIGZvcm11bGEiLCJ24bWAIHRhbmgoV+KCgXMrV+KCgmgpIiwic+G1gGgiLCJz4bWAV2giLCJ24bWAIHRhbmgoV1tzO2hdKSJdLFsiTGVhcm5hYmxlIHBhcmFtcyIsIlfigoEsIFfigoIsIHYiLCJOb25lIiwiVyIsIlcsIHYiXSxbIkxvY2FsIGF0dGVudGlvbiIsIk5vIiwiWWVzIiwiWWVzIiwiWWVzIl0sWyJJbnB1dC1mZWVkaW5nIiwiTm8iLCJPcHRpb25hbCIsIk9wdGlvbmFsIiwiT3B0aW9uYWwiXSxbIlNwZWVkIChyZWxhdGl2ZSkiLCJTbG93IiwiRmFzdGVzdCIsIkZhc3QiLCJNb2RlcmF0ZSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBwcmFjdGljZSwgTHVvbmcgZG90IGFuZCBnZW5lcmFsIGF0dGVudGlvbiB3aXRoIGlucHV0LWZlZWRpbmcgYXJlIHRoZSBtb3N0IGNvbW1vbmx5IGFkb3B0ZWQgdmFyaWFudHMgZHVlIHRvIHRoZWlyIHNpbXBsaWNpdHkgYW5kIHN0cm9uZyBlbXBpcmljYWwgcGVyZm9ybWFuY2UuIFRoZSBkb3QgcHJvZHVjdCBzY29yZSBpcyBlc3BlY2lhbGx5IGF0dHJhY3RpdmUgYmVjYXVzZSBpdCByZXF1aXJlcyBubyBhZGRpdGlvbmFsIHBhcmFtZXRlcnMgYW5kIG1hcHMgbmF0dXJhbGx5IHRvIHRoZSBzY2FsZWQgZG90LXByb2R1Y3QgYXR0ZW50aW9uIGluIHRoZSBUcmFuc2Zvcm1lciDigJQgc2ltcGx5IGRpdmlkZSBieSDiiJpkX2sgdG8gc3RhYmlsaXplIGdyYWRpZW50cyBmb3IgbGFyZ2VyIGhpZGRlbiBkaW1lbnNpb25zLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTHVvbmcgZG90IOKGkiBzY2FsZWQgZG90LXByb2R1Y3Qg4oaSIFRyYW5zZm9ybWVyIGF0dGVudGlvbiAo4oiaZF9rIHNjYWxpbmcgYWRkZWQpIiwiTXVsdGktaGVhZCBhdHRlbnRpb24gYXBwbGllcyBIIHBhcmFsbGVsIGRvdC1wcm9kdWN0IGF0dGVudGlvbiBoZWFkcyB3aXRoIGRpZmZlcmVudCBwcm9qZWN0aW9ucyIsIklucHV0LWZlZWRpbmcgcHJpbmNpcGxlIHN1cnZpdmVzIGluIFRyYW5zZm9ybWVyIGFzIGNhdXNhbCBtYXNraW5nIG92ZXIgcGFzdCBhdHRlbnRpb24iLCJMb2NhbCBhdHRlbnRpb24gY29uY2VwdCByZS1lbWVyZ2VzIGluIExvbmdmb3JtZXIgYW5kIEJpZ0JpcmQgYXMgc2xpZGluZyB3aW5kb3cgYXR0ZW50aW9uIiwiR2VuZXJhbCBhdHRlbnRpb24gd2l0aCBX4oKQID0gSSByZWR1Y2VzIHRvIGRvdCBhdHRlbnRpb24g4oCUIHRoZSBiaWFzLXZhcmlhbmNlIHRyYWRlb2ZmIGluIHNjb3JpbmciXX1d"
---
# Luong Attention — Multiplicative Attention

Luong et al. (2015) published attention mechanisms that complemented and extended Bahdanau's original formulation. Where Bahdanau uses the previous decoder state sⱼ₋₁ to compute alignment, Luong uses the current decoder state sⱼ after it has already incorporated the encoded input. Luong also introduced three distinct scoring functions — dot, general, and concat — evaluated them empirically, and proposed local attention as a computationally cheaper alternative to global (all-encoder) attention. Their input-feeding technique further improved results by making the decoder aware of previous attention decisions.

## Three Scoring Functions

Luong's three scoring functions each represent a different trade-off between expressiveness and computation. The dot product score eᵢⱼ = sⱼᵀhᵢ is the simplest and fastest — it requires no learned parameters and works well when encoder and decoder hidden dimensions match. The general score eᵢⱼ = sⱼᵀWₐhᵢ introduces a learnable weight matrix Wₐ, enabling the model to project encoder and decoder states into a shared alignment space. The concat score eᵢⱼ = vᵀ tanh(Wₐ[sⱼ;hᵢ]) concatenates the states before projecting — equivalent to Bahdanau's formulation but using the current state sⱼ rather than the previous sⱼ₋₁.

- Dot: eᵢⱼ = sⱼᵀhᵢ — no parameters, O(H) per pair, requires same hidden dim
- General: eᵢⱼ = sⱼᵀWₐhᵢ — learnable Wₐ ∈ ℝ^{dec_h × enc_h}, O(H²) params
- Concat: eᵢⱼ = vᵀ tanh(Wₐ[sⱼ;hᵢ]) — same as Bahdanau but uses current decoder state
- All three: αᵢⱼ = softmax(eᵢⱼ), cⱼ = Σᵢ αᵢⱼhᵢ — same context aggregation step
- Luong uses sⱼ (after step), Bahdanau uses sⱼ₋₁ (before step) — key difference

## Code 1 — Luong Dot, General, and Concat Attention

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LuongAttention(nn.Module):
    """Luong attention with dot, general, or concat scoring."""
    def __init__(self, mode, hidden_dim):
        super().__init__()
        self.mode = mode
        if mode == 'general':
            self.W = nn.Linear(hidden_dim, hidden_dim, bias=False)
        elif mode == 'concat':
            self.W = nn.Linear(hidden_dim * 2, hidden_dim, bias=False)
            self.v = nn.Linear(hidden_dim, 1, bias=False)

    def score(self, s, h):
        # s: (batch, hidden), h: (batch, src_len, hidden)
        if self.mode == 'dot':
            return torch.bmm(h, s.unsqueeze(-1)).squeeze(-1)      # (B, T)
        elif self.mode == 'general':
            return torch.bmm(h, self.W(s).unsqueeze(-1)).squeeze(-1)
        elif self.mode == 'concat':
            s_exp = s.unsqueeze(1).expand_as(h)
            return self.v(torch.tanh(self.W(torch.cat([s_exp, h], dim=-1)))).squeeze(-1)

    def forward(self, s, enc_outputs):
        energy  = self.score(s, enc_outputs)           # (B, T)
        alpha   = F.softmax(energy, dim=-1)
        context = (alpha.unsqueeze(-1) * enc_outputs).sum(1)
        return context, alpha

# Compare all three modes on random tensors
B, T, H = 4, 20, 256
enc = torch.randn(B, T, H)
dec_s = torch.randn(B, H)
for mode in ['dot', 'general', 'concat']:
    attn = LuongAttention(mode, H)
    ctx, a = attn(dec_s, enc)
    print(f"{mode:8s} | context={ctx.shape} | weights_sum={a.sum(-1).mean():.3f}")
```

## Global vs Local Attention

Global attention attends over all Ts encoder positions at every decoder step — this is what Bahdanau uses and what most implementations default to. Luong proposed local attention as a computationally cheaper alternative: predict an aligned position pt for each decoder step, then attend only within a window [pt - D, pt + D] of 2D+1 encoder positions. The window position pt is predicted by the decoder state: pt = Ts · sigmoid(vₚᵀ tanh(Wₚsⱼ)). A Gaussian distribution G(pt, (D/2)²) further down-weights positions far from the center, encouraging smooth localized attention.

- Global: attends all Ts encoder positions — O(Ts) per step, full coverage
- Local-m: monotone alignment, window shifts incrementally — no position prediction
- Local-p: predict pt from decoder state, Gaussian penalty within window of width 2D+1
- Local attention reduces computation from O(Ts·Tt) to O(D·Tt) — useful for long sources
- Typical D = 10 captures ±10 positions, sufficient for most translation pairs

> **When to Use Local vs Global Attention**: Use global attention for standard sentence-level NMT — it is simpler and the O(T²) cost is negligible for T < 200. Prefer local attention when encoding very long sequences (documents, audio frames) where attending every position at every step is prohibitive. For inference speed, local attention with a fixed window also enables more predictable latency.

## Code 2 — Local Attention with Gaussian Window

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LocalAttention(nn.Module):
    """Luong local-p attention: predict window center, apply Gaussian penalty."""
    def __init__(self, hidden_dim, window_D=5):
        super().__init__()
        self.D    = window_D
        self.W_p  = nn.Linear(hidden_dim, hidden_dim)
        self.v_p  = nn.Linear(hidden_dim, 1)
        self.W_a  = nn.Linear(hidden_dim * 2, hidden_dim, bias=False)
        self.v_a  = nn.Linear(hidden_dim, 1, bias=False)

    def forward(self, s, enc_outputs, src_len):
        # Predict aligned position pt in [0, src_len]
        pt = src_len * torch.sigmoid(self.v_p(torch.tanh(self.W_p(s)))).squeeze(-1)  # (B,)
        positions = torch.arange(src_len, dtype=torch.float32, device=s.device)      # (T,)
        sigma = self.D / 2.0
        gauss = torch.exp(-(positions - pt.unsqueeze(1))**2 / (2 * sigma**2))        # (B, T)
        # Attention score
        s_exp = s.unsqueeze(1).expand_as(enc_outputs)
        e = self.v_a(torch.tanh(self.W_a(torch.cat([s_exp, enc_outputs], dim=-1)))).squeeze(-1)
        alpha = F.softmax(e, dim=-1) * gauss
        alpha = alpha / (alpha.sum(-1, keepdim=True) + 1e-9)   # renormalize
        context = (alpha.unsqueeze(-1) * enc_outputs).sum(1)
        return context, alpha, pt

B, T, H = 2, 30, 128
enc = torch.randn(B, T, H)
s   = torch.randn(B, H)
local_attn = LocalAttention(H, window_D=5)
ctx, weights, pos = local_attn(s, enc, T)
print(f"Context: {ctx.shape}, Predicted positions: {[f'{p:.1f}' for p in pos.tolist()]}")
```

## Code 3 — Input-Feeding

Input-feeding is Luong's key contribution beyond the scoring functions: at each decoder step, the previous attention vector (context vector) is concatenated to the current decoder input embedding before passing through the RNN cell. This makes the decoder aware of what it attended to in the previous step — modeling the alignment history rather than treating each step independently. Input-feeding consistently improves translation quality and is now standard practice.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class InputFeedingDecoder(nn.Module):
    """Luong decoder with input-feeding: previous context concatenated to input."""
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embed   = nn.Embedding(vocab_size, embed_dim)
        # Input = embedding + previous attention context
        self.rnn     = nn.GRUCell(embed_dim + hidden_dim, hidden_dim)
        self.W_attn  = nn.Linear(hidden_dim, hidden_dim, bias=False)
        self.W_c     = nn.Linear(hidden_dim * 2, hidden_dim)
        self.fc      = nn.Linear(hidden_dim, vocab_size)

    def attend(self, s, enc_out):
        # Luong general attention using current state s
        e     = torch.bmm(enc_out, self.W_attn(s).unsqueeze(-1)).squeeze(-1)
        alpha = F.softmax(e, dim=-1)
        return (alpha.unsqueeze(-1) * enc_out).sum(1), alpha

    def forward(self, token, s, enc_out, prev_ctx):
        emb       = self.embed(token)
        s_new     = self.rnn(torch.cat([emb, prev_ctx], dim=-1), s)  # input-feeding
        ctx, alpha = self.attend(s_new, enc_out)
        h_tilde   = torch.tanh(self.W_c(torch.cat([s_new, ctx], dim=-1)))
        return self.fc(h_tilde), s_new, ctx, alpha

V, E, H, B, T = 8000, 128, 256, 2, 15
dec     = InputFeedingDecoder(V, E, H)
enc_out = torch.randn(B, T, H)
s0, ctx0 = torch.randn(B, H), torch.zeros(B, H)
tok     = torch.randint(0, V, (B,))
logits, s1, ctx1, a = dec(tok, s0, enc_out, ctx0)
print(f"logits={logits.shape}, s={s1.shape}, ctx={ctx1.shape}, alpha_sum={a.sum(-1)}")
```

## Code 4 — Bahdanau vs Luong Comparison

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulated BLEU vs sentence length (based on Luong et al. 2015 findings)
configs = {
    'No attention':           [21.5, 19.8, 17.2, 14.1, 10.3],
    'Bahdanau additive':      [26.1, 25.3, 23.9, 22.0, 19.5],
    'Luong dot':              [25.8, 25.0, 23.5, 21.7, 19.1],
    'Luong general':          [26.3, 25.6, 24.2, 22.4, 19.9],
    'Luong concat':           [25.9, 25.2, 23.8, 21.9, 19.4],
    'Luong + input-feeding':  [27.1, 26.4, 25.0, 23.3, 20.8],
}
lengths = [10, 20, 30, 40, 50]
colors  = ['gray', 'steelblue', 'tomato', 'forestgreen', 'orange', 'purple']
markers = ['x', 's', 'o', '^', 'D', '*']

fig, ax = plt.subplots(figsize=(10, 6))
for (name, scores), color, marker in zip(configs.items(), colors, markers):
    ax.plot(lengths, scores, marker=marker, color=color,
            label=name, linewidth=2, markersize=7)
ax.set_xlabel('Sentence length (tokens)', fontsize=12)
ax.set_ylabel('BLEU Score', fontsize=12)
ax.set_title('Bahdanau vs Luong Attention Variants — BLEU vs Length', fontsize=13)
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('attention_comparison.png', dpi=150)
plt.show()
print("Luong + input-feeding outperforms all variants on long sequences.")
```

## Key Differences from Bahdanau

While Bahdanau and Luong attention share the weighted-sum context mechanism, they differ in four important ways. First, the decoder state timing: Bahdanau uses sⱼ₋₁ (before generating step j) to compute alignment, while Luong uses sⱼ (after running the RNN for step j) — Luong's approach gives the alignment network access to more up-to-date information. Second, the score functions: Bahdanau only defines the additive form; Luong systematically compares dot, general, and concat. Third, local vs global: Bahdanau uses global attention only. Fourth, input-feeding: Luong explicitly models alignment history by feeding the previous context vector back as decoder input.

| Property | Bahdanau | Luong dot | Luong general | Luong concat |
| --- | --- | --- | --- | --- |
| Decoder state used | sⱼ₋₁ (prev) | sⱼ (current) | sⱼ (current) | sⱼ (current) |
| Score formula | vᵀ tanh(W₁s+W₂h) | sᵀh | sᵀWh | vᵀ tanh(W[s;h]) |
| Learnable params | W₁, W₂, v | None | W | W, v |
| Local attention | No | Yes | Yes | Yes |
| Input-feeding | No | Optional | Optional | Optional |
| Speed (relative) | Slow | Fastest | Fast | Moderate |

In practice, Luong dot and general attention with input-feeding are the most commonly adopted variants due to their simplicity and strong empirical performance. The dot product score is especially attractive because it requires no additional parameters and maps naturally to the scaled dot-product attention in the Transformer — simply divide by √d_k to stabilize gradients for larger hidden dimensions.

- Luong dot → scaled dot-product → Transformer attention (√d_k scaling added)
- Multi-head attention applies H parallel dot-product attention heads with different projections
- Input-feeding principle survives in Transformer as causal masking over past attention
- Local attention concept re-emerges in Longformer and BigBird as sliding window attention
- General attention with Wₐ = I reduces to dot attention — the bias-variance tradeoff in scoring

