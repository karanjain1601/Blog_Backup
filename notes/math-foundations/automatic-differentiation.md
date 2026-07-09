---
title: "Forward-Mode vs Reverse-Mode Automatic Differentiation"
slug: "automatic-differentiation"
description: "Explains how automatic differentiation works — dual numbers for forward mode, the Wengert tape for reverse mode — and why neural networks always use reverse mode. Includes JAX and gradient checkpointing."
tags: ["calculus", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXV0b21hdGljIGRpZmZlcmVudGlhdGlvbiAoQUQpIGNvbXB1dGVzIGV4YWN0IGRlcml2YXRpdmVzIG9mIHByb2dyYW1zIHRvIG1hY2hpbmUgcHJlY2lzaW9uIOKAlCBubyBhcHByb3hpbWF0aW9uLCBubyBleHByZXNzaW9uIHN3ZWxsLiBJdCBpcyB0aGUgZW5naW5lIGJlaGluZCBldmVyeSBncmFkaWVudC1iYXNlZCBNTCBmcmFtZXdvcmsuIFVuZGVyc3RhbmRpbmcgaXRzIHR3byBtb2RlcyAoZm9yd2FyZCBhbmQgcmV2ZXJzZSkgY2xhcmlmaWVzIHdoeSBuZXVyYWwgbmV0d29yayB0cmFpbmluZyBpcyBzbyBjb21wdXRhdGlvbmFsbHkgZWZmaWNpZW50LCBhbmQgd2h5IGNlcnRhaW4gYXJjaGl0ZWN0dXJlcyBiZW5lZml0IGZyb20gZ3JhZGllbnQgY2hlY2twb2ludGluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaHkgTm90IFN5bWJvbGljIG9yIE51bWVyaWNhbCBEaWZmZXJlbnRpYXRpb24/In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTeW1ib2xpYyBkaWZmZXJlbnRpYXRpb24gKGxpa2UgYSBDQVMpIHByb2R1Y2VzIGV4YWN0IGV4cHJlc3Npb25zIGJ1dCBzdWZmZXJzIGZyb20gZXhwcmVzc2lvbiBzd2VsbCDigJQgdGhlIHN5bWJvbGljIGdyYWRpZW50IG9mIGEgZGVlcCBuZXR3b3JrIGNhbiBiZSBleHBvbmVudGlhbGx5IGxhcmdlciB0aGFuIHRoZSBvcmlnaW5hbC4gTnVtZXJpY2FsIGRpZmZlcmVudGlhdGlvbiB1c2VzIGZpbml0ZSBkaWZmZXJlbmNlcyAoaCBzbWFsbCBidXQgbm9uemVybyksIGludHJvZHVjaW5nIHJvdW5kaW5nIGVycm9yIE8oaCkgb3IgTyhowrIpIGFuZCByZXF1aXJpbmcgTyhuKSBmdW5jdGlvbiBldmFsdWF0aW9ucyBmb3IgbiBwYXJhbWV0ZXJzLiBBRCBhdm9pZHMgYm90aCBwcm9ibGVtcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQWNjdXJhY3kiLCJDb3N0IChmdWxsIGdyYWRpZW50KSIsIkV4dHJhIE1lbW9yeSIsIkZyYW1ld29yayJdLCJyb3dzIjpbWyJTeW1ib2xpYyBkaWZmIiwiRXhhY3QiLCJFeHByZXNzaW9uIHN3ZWxsIOKAlCBpbXByYWN0aWNhbCIsIkdyb3dzIHdpdGggZXhwcmVzc2lvbiIsIk1hdGhlbWF0aWNhLCBTeW1QeSJdLFsiTnVtZXJpY2FsIChmd2QgZGlmZikiLCJPKGgpIGVycm9yIiwiTyhuKSBldmFsdWF0aW9ucyIsIk8oMSkiLCJNYW51YWwsIHNjaXB5Lm9wdGltaXplIl0sWyJGb3J3YXJkLW1vZGUgQUQiLCJNYWNoaW5lIHByZWNpc2lvbiIsIk8obikgcGFzc2VzIGZvciBuIGlucHV0cyIsIk8oMSkgcGVyIHBhc3MiLCJKQVggKGphY2Z3ZCksIFRhcGVuYWRlIl0sWyJSZXZlcnNlLW1vZGUgQUQiLCJNYWNoaW5lIHByZWNpc2lvbiIsIk8oMSkgcGFzcyBmb3Igc2NhbGFyIG91dHB1dCIsIk8oZGVwdGgpIHRhcGUiLCJQeVRvcmNoLCBKQVgsIFRlbnNvckZsb3ciXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZvcndhcmQtTW9kZSBBRDogRHVhbCBOdW1iZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3J3YXJkLW1vZGUgQUQgYXVnbWVudHMgZWFjaCByZWFsIG51bWJlciB4IHdpdGggYSB0YW5nZW50IHhcdTAwMjcg4oCUIGZvcm1pbmcgYSBkdWFsIG51bWJlciB4ICsgzrV4XHUwMDI3IHdoZXJlIM61wrIgPSAwLiBBcml0aG1ldGljIHByb3BhZ2F0ZXMgYm90aCB0aGUgdmFsdWUgYW5kIGl0cyBkZXJpdmF0aXZlIHNpbXVsdGFuZW91c2x5LiBPbmUgZm9yd2FyZCBwYXNzIHdpdGggc2VlZCB4XHUwMDI3PTEgZm9yIGlucHV0IHjhtaIgZ2l2ZXMg4oiCZi/iiIJ44bWiLiBGb3IgdGhlIGZ1bGwgZ3JhZGllbnQgeW91IG5lZWQgbiBmb3J3YXJkIHBhc3NlcyDigJQgZXhwZW5zaXZlIGZvciBtYW55IGlucHV0cywgY2hlYXAgZm9yIG1hbnkgb3V0cHV0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG1hdGhcblxuY2xhc3MgRHVhbDpcbiAgICAjIER1YWwgbnVtYmVyOiB2YWwgKyBlcHMgKiBkZXJpdiAgKGVwc14yID0gMClcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdmFsLCBkZXJpdj0wLjApOlxuICAgICAgICBzZWxmLnZhbCAgID0gdmFsXG4gICAgICAgIHNlbGYuZGVyaXYgPSBkZXJpdlxuXG4gICAgZGVmIF9fYWRkX18oc2VsZiwgb3RoZXIpOlxuICAgICAgICBpZiBpc2luc3RhbmNlKG90aGVyLCBEdWFsKTpcbiAgICAgICAgICAgIHJldHVybiBEdWFsKHNlbGYudmFsICsgb3RoZXIudmFsLCBzZWxmLmRlcml2ICsgb3RoZXIuZGVyaXYpXG4gICAgICAgIHJldHVybiBEdWFsKHNlbGYudmFsICsgb3RoZXIsIHNlbGYuZGVyaXYpXG5cbiAgICBkZWYgX19yYWRkX18oc2VsZiwgb3RoZXIpOlxuICAgICAgICByZXR1cm4gc2VsZi5fX2FkZF9fKG90aGVyKVxuXG4gICAgZGVmIF9fbXVsX18oc2VsZiwgb3RoZXIpOlxuICAgICAgICBpZiBpc2luc3RhbmNlKG90aGVyLCBEdWFsKTpcbiAgICAgICAgICAgICMgcHJvZHVjdCBydWxlOiAodSp2KVx1MDAyNyA9IHVcdTAwMjd2ICsgdXZcdTAwMjdcbiAgICAgICAgICAgIHJldHVybiBEdWFsKHNlbGYudmFsICogb3RoZXIudmFsLFxuICAgICAgICAgICAgICAgICAgICAgICAgc2VsZi52YWwgKiBvdGhlci5kZXJpdiArIHNlbGYuZGVyaXYgKiBvdGhlci52YWwpXG4gICAgICAgIHJldHVybiBEdWFsKHNlbGYudmFsICogb3RoZXIsIHNlbGYuZGVyaXYgKiBvdGhlcilcblxuICAgIGRlZiBfX3JlcHJfXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIFx1MDAyN0R1YWwoJS42ZiArIGVwcyolLjZmKVx1MDAyNyAlIChzZWxmLnZhbCwgc2VsZi5kZXJpdilcblxuZGVmIHNpbl9kKHgpOiAgcmV0dXJuIER1YWwobWF0aC5zaW4oeC52YWwpLCB4LmRlcml2ICogbWF0aC5jb3MoeC52YWwpKVxuZGVmIGV4cF9kKHgpOiAgcmV0dXJuIER1YWwobWF0aC5leHAoeC52YWwpLCB4LmRlcml2ICogbWF0aC5leHAoeC52YWwpKVxuXG4jIGYoeCkgPSB4XjIgKiBzaW4oeCkgKyBleHAoeCkgIGF0IHg9MS41XG54ID0gRHVhbCgxLjUsIDEuMCkgICAgIyBzZWVkIGRlcml2PTEgdG8gZ2V0IGRmL2R4XG55ID0geCAqIHggKiBzaW5fZCh4KSArIGV4cF9kKHgpXG5wcmludChcdTAwMjdmKDEuNSkgICAgICAgICAgICAgICA9XHUwMDI3LCByb3VuZCh5LnZhbCwgICA2KSlcbnByaW50KFx1MDAyN2YgcHJpbWUoMS41KSBbZHVhbF0gID1cdTAwMjcsIHJvdW5kKHkuZGVyaXYsIDYpKVxuXG4jIEFuYWx5dGljYWw6IGZcdTAwMjcoeCkgPSAyeCpzaW4oeCkgKyB4XjIqY29zKHgpICsgZXhwKHgpXG54diA9IDEuNVxuYW5hID0gMip4diptYXRoLnNpbih4dikgKyB4dioqMiptYXRoLmNvcyh4dikgKyBtYXRoLmV4cCh4dilcbnByaW50KFx1MDAyN2YgcHJpbWUoMS41KSBbZXhhY3RdID1cdTAwMjcsIHJvdW5kKGFuYSwgNikpXG5wcmludChcdTAwMjdFcnJvcjpcdTAwMjcsIGFicyh5LmRlcml2IC0gYW5hKSkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkZvcndhcmQgTW9kZSBJcyBJZGVhbCBmb3IgbiBcdTAwM2NcdTAwM2MgbSIsImNvbnRlbnQiOiJJZiBhIGZ1bmN0aW9uIG1hcHMgMSBpbnB1dCB0byAxMDAwIG91dHB1dHMgKG49MSwgbT0xMDAwKSwgb25lIGZvcndhcmQtbW9kZSBwYXNzIGdpdmVzIGFsbCAxMDAwIHBhcnRpYWwgZGVyaXZhdGl2ZXMg4oiCZuG1oi/iiIJ4IHNpbXVsdGFuZW91c2x5LiBSZXZlcnNlIG1vZGUgd291bGQgbmVlZCAxMDAwIGJhY2t3YXJkIHBhc3Nlcy4gSkFYXHUwMDI3cyBqYWNmd2QgdXNlcyB2ZWN0b3JpemVkIGZvcndhcmQgbW9kZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXZlcnNlLU1vZGUgQUQ6IFRoZSBUYXBlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXZlcnNlLW1vZGUgQUQgcmVjb3JkcyBvcGVyYXRpb25zIGluIHRoZSBmb3J3YXJkIHBhc3Mgb250byBhIHRhcGUgKFdlbmdlcnQgbGlzdCkuIFRoZSBiYWNrd2FyZCBwYXNzIHJlcGxheXMgdGhlIHRhcGUgaW4gcmV2ZXJzZSwgcHJvcGFnYXRpbmcgYWRqb2ludHMgKHBhcnRpYWwgZGVyaXZhdGl2ZXMgb2YgdGhlIG91dHB1dCB3aXRoIHJlc3BlY3QgdG8gZWFjaCBpbnRlcm1lZGlhdGUgdmFsdWUpIGZyb20gb3V0cHV0IHRvIGlucHV0cy4gT25lIGJhY2t3YXJkIHBhc3MgY29tcHV0ZXMg4oiCTC/iiIJ44bWiIGZvciBBTEwgaSBzaW11bHRhbmVvdXNseSDigJQgYXQgY29zdCBPKDEpIHBhc3NlcyByZWdhcmRsZXNzIG9mIG4uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgZih4KTpcbiAgICAjIGY6IFJebiAtXHUwMDNlIFIgIChzY2FsYXIgb3V0cHV0LCBtYW55IGlucHV0cylcbiAgICByZXR1cm4gKHgqKjMpLnN1bSgpICsgKHhbOi0xXSAqIHhbMTpdKS5zdW0oKVxuXG4jIFJldmVyc2UtbW9kZTogb25lIGJhY2t3YXJkIHBhc3MgZ2l2ZXMgZ3JhZGllbnQgZm9yIEFMTCBuIGlucHV0c1xubiA9IDEyXG50b3JjaC5tYW51YWxfc2VlZCgwKVxueCA9IHRvcmNoLnJhbmRuKG4sIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbnkgPSBmKHgpXG55LmJhY2t3YXJkKClcblxucHJpbnQoXHUwMDI3biBpbnB1dHM6XHUwMDI3LCBuKVxucHJpbnQoXHUwMDI3eDogICAgICBcdTAwMjcsIHguZGV0YWNoKCkucm91bmQoZGVjaW1hbHM9MykudG9saXN0KCkpXG5wcmludChcdTAwMjdHcmFkaWVudDpcdTAwMjcsIHguZ3JhZC5yb3VuZChkZWNpbWFscz0zKS50b2xpc3QoKSlcblxuIyBOdW1lcmljYWwgdmVyaWZpY2F0aW9uXG5kZWYgbnVtX2dyYWQoZnVuYywgeCwgaD0xZS01KTpcbiAgICBnID0gdG9yY2guemVyb3NfbGlrZSh4KVxuICAgIGZvciBpIGluIHJhbmdlKGxlbih4KSk6XG4gICAgICAgIHhwID0geC5kZXRhY2goKS5jbG9uZSgpOyB4bSA9IHguZGV0YWNoKCkuY2xvbmUoKVxuICAgICAgICB4cFtpXSArPSBoOyB4bVtpXSAtPSBoXG4gICAgICAgIGdbaV0gPSAoZnVuYyh4cCkgLSBmdW5jKHhtKSkgLyAoMiAqIGgpXG4gICAgcmV0dXJuIGdcblxubmcgPSBudW1fZ3JhZChmLCB4KVxucHJpbnQoXHUwMDI3TnVtZXJpY2FsOlx1MDAyNywgbmcucm91bmQoZGVjaW1hbHM9MykudG9saXN0KCkpXG5wcmludChcdTAwMjdNYXggZXJyb3I6XHUwMDI3LCAoeC5ncmFkIC0gbmcpLmFicygpLm1heCgpLml0ZW0oKSlcbnByaW50KFx1MDAyN1JldmVyc2UgbW9kZSBjb21wdXRlZCBncmFkaWVudCBmb3IgJWQgaW5wdXRzIGluIE9ORSBiYWNrd2FyZCBwYXNzLlx1MDAyNyAlIG4pIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSkFYOiBGdW5jdGlvbmFsIEFEIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJKQVggZXhwb3NlcyBBRCBhcyBjb21wb3NhYmxlIGZ1bmN0aW9uIHRyYW5zZm9ybWF0aW9uczogamF4LmdyYWQgKHJldmVyc2UtbW9kZSBncmFkaWVudCksIGpheC5qYWNyZXYvamFjZndkIChKYWNvYmlhbnMpLCBqYXguaml0IChYTEEgY29tcGlsYXRpb24pLCBqYXgudm1hcCAodmVjdG9yaXplIG92ZXIgYmF0Y2gpLiBGdW5jdGlvbnMgbXVzdCBiZSBwdXJlIChubyBpbi1wbGFjZSBtdXRhdGlvbikuIFRoaXMgY29tcG9zaXRpb25hbCBkZXNpZ24gbWFrZXMgaXQgZWFzeSB0byBjb21iaW5lIGdyYWQoaml0KHZtYXAoZikpKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBKQVg6IGZ1bmN0aW9uYWwgYXV0b21hdGljIGRpZmZlcmVudGlhdGlvblxuIyBJbnN0YWxsOiBwaXAgaW5zdGFsbCBqYXggamF4bGliXG5pbXBvcnQgamF4XG5pbXBvcnQgamF4Lm51bXB5IGFzIGpucFxuXG5kZWYgZl9zY2FsYXIoeCk6XG4gICAgIyBmOiBSXm4gLVx1MDAzZSBSXG4gICAgcmV0dXJuIGpucC5zdW0oeCoqMykgKyBqbnAuc3VtKHhbOi0xXSAqIHhbMTpdKVxuXG5kZWYgZl92ZWN0b3IoeCk6XG4gICAgIyBmOiBSXm4gLVx1MDAzZSBSXjJcbiAgICByZXR1cm4gam5wLmFycmF5KFtqbnAuc3VtKHgqKjIpLCBqbnAuc3VtKHgqKjMpXSlcblxueCA9IGpucC5hcnJheShbMS4wLCAyLjAsIDMuMF0pXG5cbiMgR3JhZGllbnQgb2Ygc2NhbGFyIGZ1bmN0aW9uIChyZXZlcnNlLW1vZGUpXG5ncmFkX2YgID0gamF4LmdyYWQoZl9zY2FsYXIpXG5nID0gZ3JhZF9mKHgpXG5wcmludChcdTAwMjdKQVggZ3JhZCAocmV2ZXJzZSk6XHUwMDI3LCBnLnRvbGlzdCgpKVxuXG4jIEZ1bGwgSmFjb2JpYW46IGphY3JldiB1c2VzIHJldmVyc2UtbW9kZSAoY2hlYXAgZm9yIG0gb3V0cHV0cylcbkogPSBqYXguamFjcmV2KGZfdmVjdG9yKSh4KVxucHJpbnQoXHUwMDI3SmFjb2JpYW4gKGphY3Jldik6XHUwMDI3LCBKLnRvbGlzdCgpKVxuXG4jIEpJVC1jb21waWxlIGZvciBzcGVlZFxuaml0X2dyYWQgPSBqYXguaml0KGdyYWRfZilcbmcyID0gaml0X2dyYWQoeClcbnByaW50KFx1MDAyN0pJVCBncmFkaWVudDpcdTAwMjcsIGcyLnRvbGlzdCgpKVxuXG4jIHZtYXA6IHZlY3Rvcml6ZSBncmFkaWVudCBvdmVyIGJhdGNoXG5iYXRjaF94ID0gam5wLm9uZXMoKDUsIDMpKVxuYmF0Y2hfZyA9IGpheC52bWFwKGdyYWRfZikoYmF0Y2hfeClcbnByaW50KFx1MDAyN0JhdGNoIGdyYWRpZW50IHNoYXBlOlx1MDAyNywgYmF0Y2hfZy5zaGFwZSlcbnByaW50KFx1MDAyN0JhdGNoIGdyYWRpZW50czpcdTAwMjcpXG5wcmludChiYXRjaF9nLnRvbGlzdCgpKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJKQVggdnMgUHlUb3JjaCBBRCIsImNvbnRlbnQiOiJCb3RoIHVzZSByZXZlcnNlLW1vZGUgQUQuIEpBWCByZXF1aXJlcyBwdXJlIGZ1bmN0aW9ucyAobm8gc2lkZSBlZmZlY3RzKSBidXQgZ2FpbnMgY29tcG9zYWJpbGl0eSBhbmQgWExBIGNvbXBpbGF0aW9uLiBQeVRvcmNoXHUwMDI3cyBlYWdlciBtb2RlIGlzIG1vcmUgZmxleGlibGUgZm9yIGRlYnVnZ2luZy4gRm9yIHByb2R1Y3Rpb24gdHJhaW5pbmcgYXQgc2NhbGUsIGJvdGggYXJlIGNvbXBldGl0aXZlOyBKQVggZXhjZWxzIGZvciByZXNlYXJjaCByZXF1aXJpbmcgY3VzdG9tIGdyYWRpZW50IHRyYW5zZm9ybWF0aW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcmFkaWVudCBDaGVja3BvaW50aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXZlcnNlLW1vZGUgQUQgbXVzdCBzdG9yZSBhbGwgaW50ZXJtZWRpYXRlIGFjdGl2YXRpb25zIGZyb20gdGhlIGZvcndhcmQgcGFzcyBvbiB0aGUgdGFwZSBmb3IgdXNlIGluIHRoZSBiYWNrd2FyZCBwYXNzLiBNZW1vcnkgZ3Jvd3Mgd2l0aCBuZXR3b3JrIGRlcHRoOiBPKGRlcHRoKSB0ZW5zb3JzLiBHcmFkaWVudCBjaGVja3BvaW50aW5nIHRyYWRlcyBjb21wdXRlIGZvciBtZW1vcnkgYnkgbm90IHN0b3JpbmcgaW50ZXJtZWRpYXRlIGFjdGl2YXRpb25zIOKAlCByZWNvbXB1dGluZyB0aGVtIGR1cmluZyBiYWNrd2FyZC4gUmVkdWNlcyBtZW1vcnkgZnJvbSBPKG4pIHRvIE8o4oiabikgYXQgY29zdCBvZiBvbmUgZXh0cmEgZm9yd2FyZCBwYXNzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaC51dGlscy5jaGVja3BvaW50IGltcG9ydCBjaGVja3BvaW50XG5cbmNsYXNzIFRyYW5zZm9ybWVyQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmZjMSA9IG5uLkxpbmVhcihkLCBkICogNClcbiAgICAgICAgc2VsZi5hY3QgPSBubi5HRUxVKClcbiAgICAgICAgc2VsZi5mYzIgPSBubi5MaW5lYXIoZCAqIDQsIGQpXG4gICAgICAgIHNlbGYubG4gID0gbm4uTGF5ZXJOb3JtKGQpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYubG4oeCArIHNlbGYuZmMyKHNlbGYuYWN0KHNlbGYuZmMxKHgpKSkpXG5cbmNsYXNzIERlZXBOZXQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZCwgbl9sYXllcnMsIHVzZV9jaGVja3BvaW50PUZhbHNlKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmxvY2tzID0gbm4uTW9kdWxlTGlzdChbVHJhbnNmb3JtZXJCbG9jayhkKSBmb3IgXyBpbiByYW5nZShuX2xheWVycyldKVxuICAgICAgICBzZWxmLnVzZV9ja3B0ID0gdXNlX2NoZWNrcG9pbnRcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBmb3IgYmxrIGluIHNlbGYuYmxvY2tzOlxuICAgICAgICAgICAgeCA9IGNoZWNrcG9pbnQoYmxrLCB4LCB1c2VfcmVlbnRyYW50PUZhbHNlKSBpZiBzZWxmLnVzZV9ja3B0IGVsc2UgYmxrKHgpXG4gICAgICAgIHJldHVybiB4XG5cbmQsIG5fbGF5ZXJzID0gMTI4LCA4XG54ID0gdG9yY2gucmFuZG4oNCwgZClcblxuZm9yIG5hbWUsIHVzZV9ja3B0IGluIFsoXHUwMDI3Tm9ybWFsXHUwMDI3LCBGYWxzZSksIChcdTAwMjdDaGVja3BvaW50ZWRcdTAwMjcsIFRydWUpXTpcbiAgICBtb2RlbCA9IERlZXBOZXQoZCwgbl9sYXllcnMsIHVzZV9jaGVja3BvaW50PXVzZV9ja3B0KVxuICAgIG91dCAgID0gbW9kZWwoeCkuc3VtKClcbiAgICBvdXQuYmFja3dhcmQoKVxuICAgIHByaW50KFx1MDAyNyVzIGJhY2t3YXJkOiBncmFkaWVudHMgT0tcdTAwMjcgJSBuYW1lKVxuXG5wcmludChcdTAwMjdDaGVja3BvaW50aW5nOiByZWNvbXB1dGVzIGFjdGl2YXRpb25zIGluIGJhY2t3YXJkIHBhc3MuXHUwMDI3KVxucHJpbnQoXHUwMDI3TWVtb3J5OiBPKG5fbGF5ZXJzKSAtXHUwMDNlIE8oc3FydChuX2xheWVycykpIHdpdGggc2VnbWVudCBjaGVja3BvaW50aW5nLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaHkgTmV1cmFsIE5ldHdvcmtzIEFsd2F5cyBVc2UgUmV2ZXJzZSBNb2RlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIG5ldXJhbCBuZXR3b3JrIGhhcyBvbmUgb3V0cHV0ICh0aGUgc2NhbGFyIGxvc3MgTCkgYW5kIG1pbGxpb25zIG9mIGlucHV0cyAodGhlIHdlaWdodHMpLiBSZXZlcnNlIG1vZGUgY29zdHMgTygxKSBwYXNzZXMgdG8gY29tcHV0ZSDiiIJML+KIgs644bWiIGZvciBBTEwgzrjhtaIgc2ltdWx0YW5lb3VzbHkuIEZvcndhcmQgbW9kZSB3b3VsZCBjb3N0IE8obl9wYXJhbXMpIHBhc3NlcyDigJQgbWlsbGlvbnMgb2YgcGFzc2VzIHBlciBncmFkaWVudCBzdGVwLiBUaGUgYXN5bW1ldHJ5IChvbmUgb3V0cHV0LCBtYW55IGlucHV0cykgbWFrZXMgcmV2ZXJzZSBtb2RlIHRoZSBvbmx5IHByYWN0aWNhbCBjaG9pY2UuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJGb3J3YXJkIG1vZGU6IGNvc3QgPSBPKG5faW5wdXRzKSBwYXNzZXM7IGlkZWFsIHdoZW4gbl9pbnB1dHMgXHUwMDNjXHUwMDNjIG5fb3V0cHV0cyIsIlJldmVyc2UgbW9kZTogY29zdCA9IE8obl9vdXRwdXRzKSBwYXNzZXM7IGlkZWFsIHdoZW4gbl9vdXRwdXRzIFx1MDAzY1x1MDAzYyBuX2lucHV0cyIsIk5ldXJhbCBuZXR3b3JrIHRyYWluaW5nOiAxIHNjYWxhciBsb3NzLCBtaWxsaW9ucyBvZiB3ZWlnaHRzIC1cdTAwM2UgcmV2ZXJzZSBtb2RlIHdpbnMiLCJKQVggamFjZndkIHZzIGphY3JldjogY2hvb3NlIGJhc2VkIG9uIHdoaWNoIGRpbWVuc2lvbiBpcyBzbWFsbGVyIiwiR3JhZGllbnQgY2hlY2twb2ludGluZyByZWR1Y2VzIHBlYWsgYWN0aXZhdGlvbiBtZW1vcnkgYXQgY29zdCBvZiBleHRyYSBjb21wdXRlIiwiSGlnaGVyLW9yZGVyIGdyYWRpZW50cyAoSGVzc2lhbnMpIHJlcXVpcmUgdHdvIGJhY2t3YXJkIHBhc3NlcyBvciBmb3J3YXJkLW92ZXItcmV2ZXJzZSJdfSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBRCBpcyBleGFjdCAobWFjaGluZSBwcmVjaXNpb24pLCBjb21wb3NhYmxlLCBhbmQgZWZmaWNpZW50LiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCBpdCBkb2VzIG5vdCBzeW1ib2xpY2FsbHkgZGlmZmVyZW50aWF0ZSB0aGUgY29kZSDigJQgaXQgdHJhY2VzIHRoZSBhY3R1YWwgY29tcHV0YXRpb24gYW5kIHByb3BhZ2F0ZXMgZGVyaXZhdGl2ZXMgdGhyb3VnaCB0aGUgdHJhY2UsIG9uZSBvcGVyYXRpb24gYXQgYSB0aW1lLiJ9XQ=="
---
# Forward-Mode vs Reverse-Mode Automatic Differentiation

Automatic differentiation (AD) computes exact derivatives of programs to machine precision — no approximation, no expression swell. It is the engine behind every gradient-based ML framework. Understanding its two modes (forward and reverse) clarifies why neural network training is so computationally efficient, and why certain architectures benefit from gradient checkpointing.

## Why Not Symbolic or Numerical Differentiation?

Symbolic differentiation (like a CAS) produces exact expressions but suffers from expression swell — the symbolic gradient of a deep network can be exponentially larger than the original. Numerical differentiation uses finite differences (h small but nonzero), introducing rounding error O(h) or O(h²) and requiring O(n) function evaluations for n parameters. AD avoids both problems.

| Method | Accuracy | Cost (full gradient) | Extra Memory | Framework |
| --- | --- | --- | --- | --- |
| Symbolic diff | Exact | Expression swell — impractical | Grows with expression | Mathematica, SymPy |
| Numerical (fwd diff) | O(h) error | O(n) evaluations | O(1) | Manual, scipy.optimize |
| Forward-mode AD | Machine precision | O(n) passes for n inputs | O(1) per pass | JAX (jacfwd), Tapenade |
| Reverse-mode AD | Machine precision | O(1) pass for scalar output | O(depth) tape | PyTorch, JAX, TensorFlow |

## Forward-Mode AD: Dual Numbers

Forward-mode AD augments each real number x with a tangent x' — forming a dual number x + εx' where ε² = 0. Arithmetic propagates both the value and its derivative simultaneously. One forward pass with seed x'=1 for input xᵢ gives ∂f/∂xᵢ. For the full gradient you need n forward passes — expensive for many inputs, cheap for many outputs.

```python
import math

class Dual:
    # Dual number: val + eps * deriv  (eps^2 = 0)
    def __init__(self, val, deriv=0.0):
        self.val   = val
        self.deriv = deriv

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.val + other.val, self.deriv + other.deriv)
        return Dual(self.val + other, self.deriv)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Dual):
            # product rule: (u*v)' = u'v + uv'
            return Dual(self.val * other.val,
                        self.val * other.deriv + self.deriv * other.val)
        return Dual(self.val * other, self.deriv * other)

    def __repr__(self):
        return 'Dual(%.6f + eps*%.6f)' % (self.val, self.deriv)

def sin_d(x):  return Dual(math.sin(x.val), x.deriv * math.cos(x.val))
def exp_d(x):  return Dual(math.exp(x.val), x.deriv * math.exp(x.val))

# f(x) = x^2 * sin(x) + exp(x)  at x=1.5
x = Dual(1.5, 1.0)    # seed deriv=1 to get df/dx
y = x * x * sin_d(x) + exp_d(x)
print('f(1.5)               =', round(y.val,   6))
print('f prime(1.5) [dual]  =', round(y.deriv, 6))

# Analytical: f'(x) = 2x*sin(x) + x^2*cos(x) + exp(x)
xv = 1.5
ana = 2*xv*math.sin(xv) + xv**2*math.cos(xv) + math.exp(xv)
print('f prime(1.5) [exact] =', round(ana, 6))
print('Error:', abs(y.deriv - ana))
```

> **Forward Mode Is Ideal for n << m**: If a function maps 1 input to 1000 outputs (n=1, m=1000), one forward-mode pass gives all 1000 partial derivatives ∂fᵢ/∂x simultaneously. Reverse mode would need 1000 backward passes. JAX's jacfwd uses vectorized forward mode.

## Reverse-Mode AD: The Tape

Reverse-mode AD records operations in the forward pass onto a tape (Wengert list). The backward pass replays the tape in reverse, propagating adjoints (partial derivatives of the output with respect to each intermediate value) from output to inputs. One backward pass computes ∂L/∂xᵢ for ALL i simultaneously — at cost O(1) passes regardless of n.

```python
import torch

def f(x):
    # f: R^n -> R  (scalar output, many inputs)
    return (x**3).sum() + (x[:-1] * x[1:]).sum()

# Reverse-mode: one backward pass gives gradient for ALL n inputs
n = 12
torch.manual_seed(0)
x = torch.randn(n, requires_grad=True)
y = f(x)
y.backward()

print('n inputs:', n)
print('x:      ', x.detach().round(decimals=3).tolist())
print('Gradient:', x.grad.round(decimals=3).tolist())

# Numerical verification
def num_grad(func, x, h=1e-5):
    g = torch.zeros_like(x)
    for i in range(len(x)):
        xp = x.detach().clone(); xm = x.detach().clone()
        xp[i] += h; xm[i] -= h
        g[i] = (func(xp) - func(xm)) / (2 * h)
    return g

ng = num_grad(f, x)
print('Numerical:', ng.round(decimals=3).tolist())
print('Max error:', (x.grad - ng).abs().max().item())
print('Reverse mode computed gradient for %d inputs in ONE backward pass.' % n)
```

## JAX: Functional AD

JAX exposes AD as composable function transformations: jax.grad (reverse-mode gradient), jax.jacrev/jacfwd (Jacobians), jax.jit (XLA compilation), jax.vmap (vectorize over batch). Functions must be pure (no in-place mutation). This compositional design makes it easy to combine grad(jit(vmap(f))).

```python
# JAX: functional automatic differentiation
# Install: pip install jax jaxlib
import jax
import jax.numpy as jnp

def f_scalar(x):
    # f: R^n -> R
    return jnp.sum(x**3) + jnp.sum(x[:-1] * x[1:])

def f_vector(x):
    # f: R^n -> R^2
    return jnp.array([jnp.sum(x**2), jnp.sum(x**3)])

x = jnp.array([1.0, 2.0, 3.0])

# Gradient of scalar function (reverse-mode)
grad_f  = jax.grad(f_scalar)
g = grad_f(x)
print('JAX grad (reverse):', g.tolist())

# Full Jacobian: jacrev uses reverse-mode (cheap for m outputs)
J = jax.jacrev(f_vector)(x)
print('Jacobian (jacrev):', J.tolist())

# JIT-compile for speed
jit_grad = jax.jit(grad_f)
g2 = jit_grad(x)
print('JIT gradient:', g2.tolist())

# vmap: vectorize gradient over batch
batch_x = jnp.ones((5, 3))
batch_g = jax.vmap(grad_f)(batch_x)
print('Batch gradient shape:', batch_g.shape)
print('Batch gradients:')
print(batch_g.tolist())
```

> **JAX vs PyTorch AD**: Both use reverse-mode AD. JAX requires pure functions (no side effects) but gains composability and XLA compilation. PyTorch's eager mode is more flexible for debugging. For production training at scale, both are competitive; JAX excels for research requiring custom gradient transformations.

## Gradient Checkpointing

Reverse-mode AD must store all intermediate activations from the forward pass on the tape for use in the backward pass. Memory grows with network depth: O(depth) tensors. Gradient checkpointing trades compute for memory by not storing intermediate activations — recomputing them during backward. Reduces memory from O(n) to O(√n) at cost of one extra forward pass.

```python
import torch
import torch.nn as nn
from torch.utils.checkpoint import checkpoint

class TransformerBlock(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.fc1 = nn.Linear(d, d * 4)
        self.act = nn.GELU()
        self.fc2 = nn.Linear(d * 4, d)
        self.ln  = nn.LayerNorm(d)

    def forward(self, x):
        return self.ln(x + self.fc2(self.act(self.fc1(x))))

class DeepNet(nn.Module):
    def __init__(self, d, n_layers, use_checkpoint=False):
        super().__init__()
        self.blocks = nn.ModuleList([TransformerBlock(d) for _ in range(n_layers)])
        self.use_ckpt = use_checkpoint

    def forward(self, x):
        for blk in self.blocks:
            x = checkpoint(blk, x, use_reentrant=False) if self.use_ckpt else blk(x)
        return x

d, n_layers = 128, 8
x = torch.randn(4, d)

for name, use_ckpt in [('Normal', False), ('Checkpointed', True)]:
    model = DeepNet(d, n_layers, use_checkpoint=use_ckpt)
    out   = model(x).sum()
    out.backward()
    print('%s backward: gradients OK' % name)

print('Checkpointing: recomputes activations in backward pass.')
print('Memory: O(n_layers) -> O(sqrt(n_layers)) with segment checkpointing.')
```

## Why Neural Networks Always Use Reverse Mode

A neural network has one output (the scalar loss L) and millions of inputs (the weights). Reverse mode costs O(1) passes to compute ∂L/∂θᵢ for ALL θᵢ simultaneously. Forward mode would cost O(n_params) passes — millions of passes per gradient step. The asymmetry (one output, many inputs) makes reverse mode the only practical choice.

- Forward mode: cost = O(n_inputs) passes; ideal when n_inputs << n_outputs
- Reverse mode: cost = O(n_outputs) passes; ideal when n_outputs << n_inputs
- Neural network training: 1 scalar loss, millions of weights -> reverse mode wins
- JAX jacfwd vs jacrev: choose based on which dimension is smaller
- Gradient checkpointing reduces peak activation memory at cost of extra compute
- Higher-order gradients (Hessians) require two backward passes or forward-over-reverse

---

AD is exact (machine precision), composable, and efficient. The key insight is that it does not symbolically differentiate the code — it traces the actual computation and propagates derivatives through the trace, one operation at a time.

