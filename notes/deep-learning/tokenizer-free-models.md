---
title: "Tokenizer-Free Models — Byte-Level and Patch-Based Approaches"
slug: "tokenizer-free-models"
description: "Tokenizer-free architectures operate on raw bytes or characters, eliminating BPE artifacts, OOV failures, and language-specific fertility imbalances. Covers ByT5 byte-level processing, MegaByte hierarchical patch models, CharFormer GBST soft tokenization, and CANINE character-level transformers."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udmVudGlvbmFsIGxhbmd1YWdlIG1vZGVscyBpbnRlcnBvc2UgYSB0b2tlbml6ZXIgYmV0d2VlbiByYXcgdGV4dCBhbmQgdGhlIG5ldXJhbCBuZXR3b3JrOiB0ZXh0IGlzIHNlZ21lbnRlZCBpbnRvIHN1YndvcmQgdG9rZW5zIGRyYXduIGZyb20gYSBmaXhlZCB2b2NhYnVsYXJ5LCB0aGVuIG1hcHBlZCB0byBpbnRlZ2VyIGlkcy4gVGhpcyBkZXNpZ24gaW50cm9kdWNlcyBzZXZlcmFsIGZhaWx1cmUgbW9kZXM6IG91dC1vZi12b2NhYnVsYXJ5IGNoYXJhY3RlcnMgZGVncmFkZSB0byBieXRlLWZhbGxiYWNrIHdpdGggZXh0cmVtZSBmZXJ0aWxpdHksIHByZS10b2tlbml6YXRpb24gcnVsZXMgZW1iZWQgbGFuZ3VhZ2Utc3BlY2lmaWMgYXNzdW1wdGlvbnMgKHNwYWNlcywgaHlwaGVucywgYXBvc3Ryb3BoZXMpLCBhbmQgdG9rZW4gZmVydGlsaXR5IGltYmFsYW5jZSBkaXNhZHZhbnRhZ2VzIGxvdy1yZXNvdXJjZSBsYW5ndWFnZXMuIFRva2VuaXplci1mcmVlIGFyY2hpdGVjdHVyZXMgYnlwYXNzIHRoaXMgZW50aXJlbHkgYnkgb3BlcmF0aW5nIG9uIHJhdyBieXRlcyBvciBjaGFyYWN0ZXJzLCBwYXNzaW5nIHRoZSBzZWdtZW50YXRpb24gcHJvYmxlbSB0byB0aGUgbmV1cmFsIG5ldHdvcmsgaXRzZWxmLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBFbGltaW5hdGUgdGhlIFRva2VuaXplcj8ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBmb3VyIG1haW4gbW90aXZhdGlvbnMgZm9yIHRva2VuaXplci1mcmVlIG1vZGVscyBhcmU6ICgxKSBPT1YgZWxpbWluYXRpb24g4oCUIGEgYnl0ZS1sZXZlbCB2b2NhYnVsYXJ5IG9mIDI1NiB2YWx1ZXMgaGFuZGxlcyBhbnkgVW5pY29kZSB0ZXh0IHZpYSBVVEYtOCBlbmNvZGluZywgd2l0aCBubyB1bmtub3duLXRva2VuIGZhbGxiYWNrOyAoMikgbGFuZ3VhZ2UgZXF1YWxpdHkg4oCUIGVhY2ggbGFuZ3VhZ2VcdTAwMjdzIGZlcnRpbGl0eSBpcyBkZXRlcm1pbmVkIGJ5IGl0cyBVVEYtOCBieXRlIGRlbnNpdHksIG5vdCBieSBpdHMgcmVwcmVzZW50YXRpb24gaW4gdGhlIHRva2VuaXplclx1MDAyN3MgdHJhaW5pbmcgY29ycHVzOyAoMykgY2hhcmFjdGVyLWxldmVsIHRhc2sgcGVyZm9ybWFuY2Ug4oCUIHRhc2tzIGxpa2Ugc3BlbGxpbmcgY29ycmVjdGlvbiwgdHlwbyByb2J1c3RuZXNzLCBtb3JwaG9sb2dpY2FsIGFuYWx5c2lzLCBhbmQgcGhvbmV0aWMgdHJhbnNjcmlwdGlvbiByZXF1aXJlIGNoYXJhY3Rlci1sZXZlbCBhY2Nlc3MgdGhhdCBzdWJ3b3JkIHRva2VuaXphdGlvbiBvYnNjdXJlczsgKDQpIGVsaW1pbmF0aW9uIG9mIHByZS10b2tlbml6YXRpb24gcnVsZXMg4oCUIHJlZ2V4LWJhc2VkIHByZS10b2tlbml6ZXJzIChlLmcuLCBHUFRcdTAwMjdzIGhhbmRsaW5nIG9mIGNvbnRyYWN0aW9ucyBhbmQgcHVuY3R1YXRpb24pIGVtYmVkIEVuZ2xpc2gtY2VudHJpYyBhc3N1bXB0aW9ucyB0aGF0IGltcGFpciBtdWx0aWxpbmd1YWwgcGVyZm9ybWFuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQnl0ZS1MZXZlbCBJbnB1dCBQaXBlbGluZSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIHRleHRfdG9fYnl0ZV9wYXRjaGVzKHRleHQsIHBhdGNoX3NpemU9NCwgcGFkX2lkPTApOlxuICAgICMgRW5jb2RlIHRleHQgdG8gVVRGLTggYnl0ZXNcbiAgICByYXdfYnl0ZXMgPSBsaXN0KHRleHQuZW5jb2RlKFx1MDAyN3V0Zi04XHUwMDI3KSlcbiAgICBuX2J5dGVzID0gbGVuKHJhd19ieXRlcylcbiAgICAjIFBhZCB0byBtdWx0aXBsZSBvZiBwYXRjaF9zaXplXG4gICAgcGFkX2xlbiA9IChwYXRjaF9zaXplIC0gbl9ieXRlcyAlIHBhdGNoX3NpemUpICUgcGF0Y2hfc2l6ZVxuICAgIHJhd19ieXRlcyA9IHJhd19ieXRlcyArIFtwYWRfaWRdICogcGFkX2xlblxuICAgIGJ5dGVfdGVuc29yID0gdG9yY2gudGVuc29yKHJhd19ieXRlcywgZHR5cGU9dG9yY2gubG9uZylcbiAgICBuX3BhdGNoZXMgPSBsZW4ocmF3X2J5dGVzKSAvLyBwYXRjaF9zaXplXG4gICAgcGF0Y2hlcyA9IGJ5dGVfdGVuc29yLnZpZXcobl9wYXRjaGVzLCBwYXRjaF9zaXplKVxuICAgIGF0dGVudGlvbl9tYXNrID0gdG9yY2gub25lcyhuX3BhdGNoZXMsIGR0eXBlPXRvcmNoLmxvbmcpXG4gICAgIyBNYXNrIHBhZGRpbmcgcGF0Y2hlc1xuICAgIGZvciBpIGluIHJhbmdlKG5fcGF0Y2hlcyAtIDEsIC0xLCAtMSk6XG4gICAgICAgIGlmIHBhdGNoZXNbaV0uc3VtKCkgPT0gMDpcbiAgICAgICAgICAgIGF0dGVudGlvbl9tYXNrW2ldID0gMFxuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgYnJlYWtcbiAgICByZXR1cm4gcGF0Y2hlcywgYXR0ZW50aW9uX21hc2tcblxuc2FtcGxlcyA9IFtcdTAwMjdIZWxsbyB3b3JsZFx1MDAyNywgXHUwMDI344GT44KT44Gr44Gh44GvXHUwMDI3LCBcdTAwMjfZhdix2K3YqNinXHUwMDI3XVxuZm9yIHRleHQgaW4gc2FtcGxlczpcbiAgICByYXcgPSB0ZXh0LmVuY29kZShcdTAwMjd1dGYtOFx1MDAyNylcbiAgICBwYXRjaGVzLCBtYXNrID0gdGV4dF90b19ieXRlX3BhdGNoZXModGV4dCwgcGF0Y2hfc2l6ZT00KVxuICAgIHByaW50KGZcdTAwMjd7dGV4dCFyOlx1MDAzYzIwfToge2xlbihyYXcpfSBieXRlcyAtXHUwMDNlIHtwYXRjaGVzLnNoYXBlWzBdfSBwYXRjaGVzXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIGJ5dGUgdmFsdWVzOiB7bGlzdChyYXdbOjEyXSl9Li4uXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIHBhdGNoWzBdOiAgICB7cGF0Y2hlc1swXS50b2xpc3QoKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVnYUJ5dGUg4oCUIEhpZXJhcmNoaWNhbCBQYXRjaC1CYXNlZCBQcm9jZXNzaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNZWdhQnl0ZSAoWXUgZXQgYWwuIDIwMjMpIHVzZXMgYSB0d28tbGV2ZWwgaGllcmFyY2hpY2FsIGFyY2hpdGVjdHVyZSB0byByZWR1Y2UgdGhlIHF1YWRyYXRpYyBjb3N0IG9mIGF0dGVudGlvbiBvdmVyIHJhdyBieXRlcy4gQSBnbG9iYWwgdHJhbnNmb3JtZXIgbW9kZWwgcHJvY2Vzc2VzIHNlcXVlbmNlcyBvZiBwYXRjaCBlbWJlZGRpbmdzIChlYWNoIHBhdGNoIGJlaW5nIFAgY29uc2VjdXRpdmUgYnl0ZXMpLiBBIGxvY2FsIHRyYW5zZm9ybWVyIG9wZXJhdGVzIHdpdGhpbiBlYWNoIHBhdGNoIHRvIHByZWRpY3QgdGhlIG5leHQgUCBieXRlcyBnaXZlbiB0aGUgZ2xvYmFsIGNvbnRleHQuIFdpdGggcGF0Y2ggc2l6ZSBQPTQsIHNlcXVlbmNlIGxlbmd0aCBpcyByZWR1Y2VkIFAtZm9sZCBjb21wYXJlZCB0byBwdXJlIGJ5dGUtbGV2ZWwgbW9kZWxzLiBUaGUgZ2xvYmFsIG1vZGVsIGNhcHR1cmVzIGxvbmctcmFuZ2UgZGVwZW5kZW5jaWVzIGFjcm9zcyBwYXRjaGVzOyB0aGUgbG9jYWwgbW9kZWwgaGFuZGxlcyBmaW5lLWdyYWluZWQgY2hhcmFjdGVyLWxldmVsIGdlbmVyYXRpb24gd2l0aGluIGVhY2ggcGF0Y2guIFRoaXMgYWNoaWV2ZXMgY29tcGV0aXRpdmUgcGVycGxleGl0eSB0byBHUFQtc3R5bGUgQlBFIG1vZGVscyBhdCAxL1AgdGhlIGVmZmVjdGl2ZSBzZXF1ZW5jZSBsZW5ndGguIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE1lZ2FCeXRlTG9jYWwobm4uTW9kdWxlKTpcbiAgICAjIExvY2FsIG1vZGVsOiBnaXZlbiBwYXRjaCBjb250ZXh0LCBwcmVkaWN0IG5leHQgYnl0ZSBpbiBwYXRjaFxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwYXRjaF9zaXplPTQsIGRfbW9kZWw9MTI4LCBuX2hlYWRzPTQsIG5fbGF5ZXJzPTIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5wYXRjaF9zaXplID0gcGF0Y2hfc2l6ZVxuICAgICAgICBzZWxmLmJ5dGVfZW1iZWQgPSBubi5FbWJlZGRpbmcoMjU2ICsgMSwgZF9tb2RlbCkgICMgMjU2IGJ5dGVzICsgcGFkXG4gICAgICAgIHNlbGYucG9zX2VtYmVkID0gbm4uRW1iZWRkaW5nKHBhdGNoX3NpemUsIGRfbW9kZWwpXG4gICAgICAgIGVuY29kZXJfbGF5ZXIgPSBubi5UcmFuc2Zvcm1lckVuY29kZXJMYXllcihkX21vZGVsLCBuX2hlYWRzLCBkaW1fZmVlZGZvcndhcmQ9MjU2LCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLnRyYW5zZm9ybWVyID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyKGVuY29kZXJfbGF5ZXIsIG51bV9sYXllcnM9bl9sYXllcnMpXG4gICAgICAgIHNlbGYub3V0X3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgMjU2KVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgYnl0ZV9pZHMsIGdsb2JhbF9jb250ZXh0KTpcbiAgICAgICAgIyBieXRlX2lkczogKGJhdGNoLCBwYXRjaF9zaXplKTsgZ2xvYmFsX2NvbnRleHQ6IChiYXRjaCwgZF9tb2RlbClcbiAgICAgICAgQiwgUCA9IGJ5dGVfaWRzLnNoYXBlXG4gICAgICAgIHBvcyA9IHRvcmNoLmFyYW5nZShQLCBkZXZpY2U9Ynl0ZV9pZHMuZGV2aWNlKVxuICAgICAgICB4ID0gc2VsZi5ieXRlX2VtYmVkKGJ5dGVfaWRzKSArIHNlbGYucG9zX2VtYmVkKHBvcykudW5zcXVlZXplKDApXG4gICAgICAgIHggPSB4ICsgZ2xvYmFsX2NvbnRleHQudW5zcXVlZXplKDEpICAjIGluamVjdCBnbG9iYWwgY29udGV4dFxuICAgICAgICB4ID0gc2VsZi50cmFuc2Zvcm1lcih4KVxuICAgICAgICByZXR1cm4gc2VsZi5vdXRfcHJvaih4KSAgIyAoYmF0Y2gsIHBhdGNoX3NpemUsIDI1NilcblxuY2xhc3MgTWVnYUJ5dGVHbG9iYWwobm4uTW9kdWxlKTpcbiAgICAjIEdsb2JhbCBtb2RlbDogcHJvY2VzcyBwYXRjaCBlbWJlZGRpbmdzIHRvIHByb2R1Y2UgY29udGV4dCB2ZWN0b3JzXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHBhdGNoX3NpemU9NCwgZF9tb2RlbD0xMjgsIG5faGVhZHM9NCwgbl9sYXllcnM9Myk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBhdGNoX2VtYmVkID0gbm4uTGluZWFyKHBhdGNoX3NpemUgKiBkX21vZGVsLCBkX21vZGVsKVxuICAgICAgICBlbmNvZGVyX2xheWVyID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyTGF5ZXIoZF9tb2RlbCwgbl9oZWFkcywgZGltX2ZlZWRmb3J3YXJkPTI1NiwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi50cmFuc2Zvcm1lciA9IG5uLlRyYW5zZm9ybWVyRW5jb2RlcihlbmNvZGVyX2xheWVyLCBudW1fbGF5ZXJzPW5fbGF5ZXJzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgcGF0Y2hfZW1iZWRkaW5ncyk6XG4gICAgICAgIHggPSBzZWxmLnRyYW5zZm9ybWVyKHBhdGNoX2VtYmVkZGluZ3MpXG4gICAgICAgIHJldHVybiB4ICAjIChiYXRjaCwgbl9wYXRjaGVzLCBkX21vZGVsKVxuXG4jIERlbW9cbkIsIE5fcGF0Y2hlcywgUCwgRCA9IDIsIDgsIDQsIDEyOFxuYnl0ZV9pZHMgPSB0b3JjaC5yYW5kaW50KDAsIDI1NiwgKEIsIFApKVxuZ2xvYmFsX2N0eCA9IHRvcmNoLnJhbmRuKEIsIEQpXG5sb2NhbF9tb2RlbCA9IE1lZ2FCeXRlTG9jYWwocGF0Y2hfc2l6ZT1QLCBkX21vZGVsPUQpXG5sb2dpdHMgPSBsb2NhbF9tb2RlbChieXRlX2lkcywgZ2xvYmFsX2N0eClcbnByaW50KGZcdTAwMjdNZWdhQnl0ZSBsb2NhbCBvdXRwdXQ6IHtsb2dpdHMuc2hhcGV9ICAoYmF0Y2gsIHBhdGNoLCB2b2NhYj0yNTYpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNoYXJGb3JtZXIgR0JTVCBTb2Z0IFRva2VuaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2hhckZvcm1lciAoVGF5IGV0IGFsLiAyMDIxKSBpbnRyb2R1Y2VzIEdyYWRpZW50LUJhc2VkIFN1YndvcmQgVG9rZW5pemF0aW9uIChHQlNUKSwgYSBkaWZmZXJlbnRpYWJsZSBtb2R1bGUgdGhhdCBsZWFybnMgdG8gZ3JvdXAgY2hhcmFjdGVycyBpbnRvIHZhcmlhYmxlLWxlbmd0aCBzdWJ3b3JkLWxpa2UgcmVwcmVzZW50YXRpb25zIHdpdGhvdXQgYSBmaXhlZCB2b2NhYnVsYXJ5LiBBIGxlYXJuYWJsZSBzY29yaW5nIGZ1bmN0aW9uIGFzc2lnbnMgZWFjaCBjaGFyYWN0ZXIgcG9zaXRpb24gYSBzb2Z0IGFzc2lnbm1lbnQgb3ZlciBjYW5kaWRhdGUgYmxvY2sgd2lkdGhzICgxLCAyLCAzLCAuLi4gY2hhcmFjdGVycykuIFRoZXNlIHNvZnQgYXNzaWdubWVudHMgYXJlIGxlYXJuZWQgZW5kLXRvLWVuZCBieSBncmFkaWVudCBkZXNjZW50LCBhbGxvd2luZyB0aGUgbW9kZWwgdG8gZGlzY292ZXIgb3B0aW1hbCBncm91cGluZ3MgZm9yIHRoZSB0YXNrLiBUaGUgcmVzdWx0aW5nIHJlcHJlc2VudGF0aW9uIGhhcyByZWR1Y2VkIHNlcXVlbmNlIGxlbmd0aCAoYnkgcm91Z2hseSB0aGUgbWVhbiBibG9jayB3aWR0aCkgYW5kIGlzIGZ1bGx5IGRpZmZlcmVudGlhYmxlLCB1bmxpa2UgaGFyZCBCUEUgc2VnbWVudGF0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBHQlNUQmxvY2sobm4uTW9kdWxlKTpcbiAgICAjIFNpbXBsaWZpZWQgR0JTVDogbGVhcm4gc29mdCBtZXJnaW5nIG9mIGNoYXJhY3RlcnMgaW50byBzdWJ3b3JkIGJsb2Nrc1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsPTY0LCBtYXhfYmxvY2s9NCwgZG93bnNhbXBsZV9mYWN0b3I9Mik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm1heF9ibG9jayA9IG1heF9ibG9ja1xuICAgICAgICBzZWxmLmRvd25zYW1wbGVfZmFjdG9yID0gZG93bnNhbXBsZV9mYWN0b3JcbiAgICAgICAgc2VsZi5jaGFyX2VtYmVkID0gbm4uRW1iZWRkaW5nKDI1NiwgZF9tb2RlbClcbiAgICAgICAgc2VsZi5zY29yZV9wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIG1heF9ibG9jaylcbiAgICAgICAgc2VsZi5ibG9ja19wcm9qID0gbm4uTW9kdWxlTGlzdChbbm4uTGluZWFyKGRfbW9kZWwgKiB3LCBkX21vZGVsKSBmb3IgdyBpbiByYW5nZSgxLCBtYXhfYmxvY2sgKyAxKV0pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBjaGFyX2lkcyk6XG4gICAgICAgICMgY2hhcl9pZHM6IChiYXRjaCwgc2VxX2xlbilcbiAgICAgICAgQiwgTCA9IGNoYXJfaWRzLnNoYXBlXG4gICAgICAgIHggPSBzZWxmLmNoYXJfZW1iZWQoY2hhcl9pZHMpICAjIChCLCBMLCBkX21vZGVsKVxuICAgICAgICBzY29yZXMgPSBzZWxmLnNjb3JlX3Byb2ooeCkgICAgICMgKEIsIEwsIG1heF9ibG9jaykgLS0gYmxvY2sgd2lkdGggc2NvcmVzXG4gICAgICAgIHdlaWdodHMgPSBGLnNvZnRtYXgoc2NvcmVzLCBkaW09LTEpICAjIHNvZnQgYmxvY2sgd2lkdGggYXNzaWdubWVudFxuICAgICAgICAjIEFnZ3JlZ2F0ZTogZm9yIHBvc2l0aW9uIGksIGNvbGxlY3Qgd2VpZ2h0ZWQgc3VtIGFjcm9zcyBibG9jayB3aWR0aHNcbiAgICAgICAgb3V0ID0geC5jbG9uZSgpXG4gICAgICAgIGZvciB3X2lkeCwgdyBpbiBlbnVtZXJhdGUocmFuZ2UoMSwgc2VsZi5tYXhfYmxvY2sgKyAxKSk6XG4gICAgICAgICAgICBpZiB3ID09IDE6XG4gICAgICAgICAgICAgICAgY29udHJpYnV0aW9uID0geCAqIHdlaWdodHNbOiwgOiwgd19pZHg6d19pZHgrMV1cbiAgICAgICAgICAgIGVsc2U6XG4gICAgICAgICAgICAgICAgcGFkZGVkID0gRi5wYWQoeCwgKDAsIDAsIDAsIHcgLSAxKSlcbiAgICAgICAgICAgICAgICBwb29sZWQgPSBwYWRkZWQudW5mb2xkKDEsIHcsIDEpLm1lYW4oLTEpICAjIChCLCBMLCBkX21vZGVsKVxuICAgICAgICAgICAgICAgIGNvbnRyaWJ1dGlvbiA9IHBvb2xlZCAqIHdlaWdodHNbOiwgOiwgd19pZHg6d19pZHgrMV1cbiAgICAgICAgICAgIG91dCA9IG91dCArIGNvbnRyaWJ1dGlvblxuICAgICAgICAjIERvd25zYW1wbGUgYnkgdGFraW5nIGV2ZXJ5IGRvd25zYW1wbGVfZmFjdG9yLXRoIHBvc2l0aW9uXG4gICAgICAgIG91dCA9IG91dFs6LCA6OnNlbGYuZG93bnNhbXBsZV9mYWN0b3IsIDpdICAjIChCLCBMLy9kcywgZF9tb2RlbClcbiAgICAgICAgcmV0dXJuIG91dFxuXG5nYnN0ID0gR0JTVEJsb2NrKGRfbW9kZWw9NjQsIG1heF9ibG9jaz00LCBkb3duc2FtcGxlX2ZhY3Rvcj0yKVxuY2hhcnMgPSB0b3JjaC5yYW5kaW50KDAsIDI1NiwgKDIsIDE2KSlcbm91dCA9IGdic3QoY2hhcnMpXG5wcmludChmXHUwMDI3SW5wdXQ6ICB7Y2hhcnMuc2hhcGV9ICAoYmF0Y2g9Miwgc2VxX2xlbj0xNiBjaGFycylcdTAwMjcpXG5wcmludChmXHUwMDI3T3V0cHV0OiB7b3V0LnNoYXBlfSAgIChiYXRjaD0yLCBzZXFfbGVuPXtvdXQuc2hhcGVbMV19IGFmdGVyIDJ4IGRvd25zYW1wbGUpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJ5VDUgVG9rZW5pemVyIFVzYWdlIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvVG9rZW5pemVyLCBUNVRva2VuaXplclxuaW1wb3J0IHRvcmNoXG5cbmRlZiBjb21wYXJlX2J5dDVfdnNfdDUodGV4dHMpOlxuICAgIGJ5dDVfdG9rID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQoXHUwMDI3Z29vZ2xlL2J5dDUtc21hbGxcdTAwMjcpXG4gICAgdDVfdG9rID0gVDVUb2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFx1MDAyN3Q1LXNtYWxsXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjd7XCJUZXh0XCI6XHUwMDNjNDB9IHtcIkJ5VDUgdG9rZW5zXCI6XHUwMDNlMTJ9IHtcIlQ1IHRva2Vuc1wiOlx1MDAzZTEyfSB7XCJSYXRpb1wiOlx1MDAzZTh9XHUwMDI3KVxuICAgIGZvciB0ZXh0IGluIHRleHRzOlxuICAgICAgICBieXQ1X2lkcyA9IGJ5dDVfdG9rLmVuY29kZSh0ZXh0KVxuICAgICAgICB0NV9pZHMgPSB0NV90b2suZW5jb2RlKHRleHQpXG4gICAgICAgIHJhdGlvID0gbGVuKGJ5dDVfaWRzKSAvIG1heChsZW4odDVfaWRzKSwgMSlcbiAgICAgICAgc2hvcnQgPSB0ZXh0WzozOF0gKyBcdTAwMjcuLlx1MDAyNyBpZiBsZW4odGV4dCkgXHUwMDNlIDQwIGVsc2UgdGV4dFxuICAgICAgICBwcmludChmXHUwMDI3e3Nob3J0Olx1MDAzYzQwfSB7bGVuKGJ5dDVfaWRzKTpcdTAwM2UxMn0ge2xlbih0NV9pZHMpOlx1MDAzZTEyfSB7cmF0aW86XHUwMDNlOC4yZn14XHUwMDI3KVxuICAgICMgU2hvdyBieXRlLWxldmVsIHRva2VucyBmb3IgYSBzaG9ydCB0ZXh0XG4gICAgc2FtcGxlID0gdGV4dHNbMF1cbiAgICBpZHMgPSBieXQ1X3Rvay5lbmNvZGUoc2FtcGxlKVxuICAgIGRlY29kZWQgPSBbYnl0NV90b2suZGVjb2RlKFtpXSkgZm9yIGkgaW4gaWRzWzoxMF1dXG4gICAgcHJpbnQoZlx1MDAyN1xcbkJ5VDUgYnl0ZSB0b2tlbnMgZm9yIHtyZXByKHNhbXBsZVs6MjBdKX06XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIGlkcz17aWRzWzoxMF19ICBkZWNvZGVkPXtkZWNvZGVkfVx1MDAyNylcblxudGV4dHMgPSBbXG4gICAgXHUwMDI3SGVsbG8gd29ybGRcdTAwMjcsXG4gICAgXHUwMDI3bmHDr3ZlIGNhZsOpIHLDqXN1bcOpXHUwMDI3LFxuICAgIFx1MDAyN1NwZWxpbmcgbWlzdGFlayBjb3JyZWtzaW9uXHUwMDI3LFxuICAgIFx1MDAyN+aXpeacrOiqnuODhuOCreOCueODiFx1MDAyNyxcbiAgICBcdTAwMjfZhdix2K3YqNinINio2KfZhNi52KfZhNmFXHUwMDI3LFxuXVxuY29tcGFyZV9ieXQ1X3ZzX3Q1KHRleHRzKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRva2VuaXplci1GcmVlIEFyY2hpdGVjdHVyZXMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJBcmNoaXRlY3R1cmUiLCJBcHByb2FjaCIsIkVmZmVjdGl2ZSBWb2NhYiIsIlNlcSBMZW5ndGggRmFjdG9yIiwiS2V5IFN0cmVuZ3RoIl0sInJvd3MiOltbIkJ5VDUiLCJQdXJlIGJ5dGUtbGV2ZWwgVDUgZW5jb2Rlci1kZWNvZGVyIiwiMjU2IGJ5dGVzICsgMyBzcGVjaWFsIiwiM+KAkzjDlyBsb25nZXIgdGhhbiBCUEUiLCJObyBPT1Y7IGVxdWFsIGxhbmd1YWdlIHRyZWF0bWVudDsgcm9idXN0IHRvIG5vaXNlIl0sWyJNZWdhQnl0ZSIsIlBhdGNoLWJhc2VkOiBnbG9iYWwgbW9kZWwgb3ZlciBwYXRjaGVzICsgbG9jYWwgb3ZlciBieXRlcyIsIjI1NiBieXRlcyAobG9jYWwpIiwifjEvUCBvZiBieXRlLWxldmVsIChQPTTigJMxNikiLCJTY2FsZXMgYnl0ZSBtb2RlbHMgdG8gbG9uZyBzZXF1ZW5jZXM7IGNvbXBldGl0aXZlIHBlcnBsZXhpdHkiXSxbIkNoYXJGb3JtZXIgKEdCU1QpIiwiRGlmZmVyZW50aWFibGUgc29mdCBjaGFyYWN0ZXIgZ3JvdXBpbmciLCIyNTYgY2hhcnM7IGxlYXJuZWQgc3Vid29yZCBibG9ja3MiLCJ+MuKAkzTDlyBsb25nZXIgdGhhbiBCUEUiLCJFbmQtdG8tZW5kIGRpZmZlcmVudGlhYmxlIHRva2VuaXphdGlvbjsgdGFzay1hZGFwdGl2ZSBncm91cGluZyJdLFsiQ0FOSU5FIiwiQ2hhci1sZXZlbCB3aXRoIHN0cmlkZWQgY29udiBjb21wcmVzc2lvbiIsIjE0MywwMDArIFVuaWNvZGUgY29kZSBwb2ludHMiLCJ+NMOXIGxvbmdlciB0aGFuIEJQRSB0aGVuIGNvbXByZXNzZWQiLCJNdWx0aWxpbmd1YWwgd2l0aCBubyBzY3JpcHQgYmlhczsgaGFzaC1iYXNlZCBlbWJlZGRpbmciXSxbIkJ5dGUtbGV2ZWwgQlBFIiwiQlBFIGFwcGxpZWQgdG8gcmF3IGJ5dGVzIGluc3RlYWQgb2YgY2hhcnMiLCIyNTbigJM1MCwwMDAgbWVyZ2VkIGJ5dGUgdG9rZW5zIiwiU2ltaWxhciB0byBzdWJ3b3JkIEJQRSIsIkVsaW1pbmF0ZXMgT09WIHdoaWxlIGtlZXBpbmcgQlBFIG1lcmdlIGVmZmljaWVuY3kiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWRlb2ZmcyB2cyBTdWJ3b3JkIE1vZGVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGZ1bmRhbWVudGFsIHRyYWRlb2ZmIG9mIHRva2VuaXplci1mcmVlIG1vZGVscyBpcyBzZXF1ZW5jZSBsZW5ndGggdmVyc3VzIGdlbmVyYWxpdHkuIE9wZXJhdGluZyBvbiBieXRlcyBvciBjaGFyYWN0ZXJzIGluY3JlYXNlcyBzZXF1ZW5jZSBsZW5ndGggYnkgM+KAkzjDlyBjb21wYXJlZCB0byBCUEUgb24gdGhlIHNhbWUgdGV4dC4gVHJhbnNmb3JtZXIgc2VsZi1hdHRlbnRpb24gc2NhbGVzIHF1YWRyYXRpY2FsbHkgd2l0aCBzZXF1ZW5jZSBsZW5ndGgsIG1ha2luZyBieXRlLWxldmVsIG1vZGVscyBwcm9wb3J0aW9uYWxseSBtb3JlIGV4cGVuc2l2ZS4gQnlUNS1zbWFsbCBhY2hpZXZlcyBjb21wYXJhYmxlIHRyYW5zbGF0aW9uIHF1YWxpdHkgdG8gVDUtc21hbGwgb24gbXVsdGlsaW5ndWFsIGJlbmNobWFya3MgYnV0IHJlcXVpcmVzIDPigJM1w5cgbW9yZSBGTE9QcyBwZXIgZm9yd2FyZCBwYXNzLiBQYXRjaC1iYXNlZCBtb2RlbHMgbGlrZSBNZWdhQnl0ZSByZWR1Y2UgdGhpcyBjb3N0IGJ5IGdyb3VwaW5nIGJ5dGVzLCBidXQgcmVxdWlyZSBhIHR3by1sZXZlbCBhcmNoaXRlY3R1cmUgdGhhdCBjb21wbGljYXRlcyB0cmFpbmluZyBhbmQgaW5mZXJlbmNlLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTWVnYUJ5dGUgUGF0Y2ggTW9kZWxzIFJlZHVjZSBTZXF1ZW5jZSBMZW5ndGggUC1Gb2xkIiwiY29udGVudCI6Ik1lZ2FCeXRlLXN0eWxlIHBhdGNoLWJhc2VkIG1vZGVscyBhY2hpZXZlIGNvbXBldGl0aXZlIHBlcnBsZXhpdHkgYXQgMS9QIHRoZSBzZXF1ZW5jZSBsZW5ndGggb2YgcHVyZSBieXRlIG1vZGVscyBieSBncm91cGluZyBieXRlcyBpbnRvIHBhdGNoZXMg4oCUIHRoZSBsb2NhbCBtb2RlbCBoYW5kbGVzIGludHJhLXBhdGNoIGdlbmVyYXRpb24gd2hpbGUgdGhlIGdsb2JhbCBtb2RlbCBjYXB0dXJlcyBsb25nLXJhbmdlIGNvbnRleHQuIFdpdGggcGF0Y2ggc2l6ZSBQPTgsIGEgMTAwMC1ieXRlIGRvY3VtZW50IHJlcXVpcmVzIG9ubHkgMTI1IGdsb2JhbCBhdHRlbnRpb24gc3RlcHMgaW5zdGVhZCBvZiAxMDAwLCBicmluZ2luZyB0aGUgcXVhZHJhdGljIGF0dGVudGlvbiBjb3N0IGRvd24gYnkgNjTDly4gVGhlIGxvY2FsIG1vZGVsXHUwMDI3cyBjb3N0IGlzIGNvbnN0YW50IHBlciBwYXRjaCBhbmQgcGFyYWxsZWxpc2FibGUgYWNyb3NzIHBhdGNoZXMsIG1ha2luZyBvdmVyYWxsIHRyYWluaW5nIGNvc3QgY29tcGFyYWJsZSB0byBhIHN0YW5kYXJkIHRyYW5zZm9ybWVyIG9uIHRoZSBzYW1lIHRleHQgd2l0aCBzdWJ3b3JkIHRva2VuaXNhdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByYWN0aWNhbCBkZXBsb3ltZW50IGNvbnNpZGVyYXRpb25zOiBCeVQ1IHdvcmtzIGJlc3Qgd2hlbiB0aGUgdGFzayBpcyBjaGFyYWN0ZXItc2Vuc2l0aXZlIOKAlCBzcGVsbGluZyBjb3JyZWN0aW9uLCB0cmFuc2xpdGVyYXRpb24sIHBob25ldGljIGFsaWdubWVudCwgbW9ycGhvbG9naWNhbCBhbmFseXNpcywgb3IgaGFuZGxpbmcgbm9pc3kgdXNlciBpbnB1dCB3aXRoIHR5cG9zLiBGb3IgdGFza3Mgd2hlcmUgc2VtYW50aWMgY29udGVudCBkb21pbmF0ZXMgYW5kIG9ydGhvZ3JhcGhpYyBkZXRhaWwgaXMgaXJyZWxldmFudCwgQlBFIG1vZGVscyBhcmUgbW9yZSBlZmZpY2llbnQuIENBTklORSBhbmQgQ2hhckZvcm1lciBhcmUgaW50ZXJtZWRpYXRlOiB0aGV5IGxlYXJuIHRhc2stYWRhcHRpdmUgY29tcHJlc3Npb24gdGhhdCByZWR1Y2VzIHNlcXVlbmNlIGxlbmd0aCB3aGlsZSByZXRhaW5pbmcgY2hhcmFjdGVyLWxldmVsIGFjY2Vzcy4gRm9yIHByb2R1Y3Rpb24gbXVsdGlsaW5ndWFsIHN5c3RlbXMgd2hlcmUgbGFuZ3VhZ2UgZXF1YWxpdHkgbWF0dGVycyBtb3JlIHRoYW4gaW5mZXJlbmNlIGNvc3QsIEJ5VDUgb3IgQ0FOSU5FIGFyZSBzdHJvbmcgYmFzZWxpbmVzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQnlUNSB2b2NhYnVsYXJ5OiAyNTYgcmF3IGJ5dGVzICsgMyBzcGVjaWFsIHRva2VucyAocGFkLCBFT1MsIFVOSykg4oCUIHRoZSBlbnRpcmUgbW9kZWwgaXMgdG9rZW5pemVyLWZyZWUuIiwiTWVnYUJ5dGUgcGF0Y2ggc2l6ZSBQOiBsYXJnZXIgUCByZWR1Y2VzIHNlcXVlbmNlIGxlbmd0aCBidXQgbWFrZXMgdGhlIGxvY2FsIG1vZGVsXHUwMDI3cyB0YXNrIGhhcmRlcjsgUD004oCTOCBpcyB0eXBpY2FsLiIsIkNoYXJGb3JtZXIgR0JTVCBpcyBkaWZmZXJlbnRpYWJsZTogdGhlIGdyb3VwaW5nIGlzIGxlYXJuZWQgZW5kLXRvLWVuZCwgYWRhcHRpbmcgdG8gdGhlIHRhc2sgcmF0aGVyIHRoYW4gdGV4dCBzdGF0aXN0aWNzLiIsIkNBTklORSB1c2VzIGhhc2ggZW1iZWRkaW5ncyBmb3IgVW5pY29kZSBjb2RlIHBvaW50cywgYXZvaWRpbmcgYSBmaXhlZCBjaGFyYWN0ZXIgdm9jYWJ1bGFyeSB3aGlsZSBjb3ZlcmluZyBhbGwgc2NyaXB0cy4iLCJCeXRlLWxldmVsIEJQRSAodXNlZCBpbiBHUFQtMiBhbmQgUm9CRVJUYSkgaXMgYSBoeWJyaWQ6IEJQRSBtZXJnZXMgYXBwbGllZCB0byBieXRlcywgZWxpbWluYXRpbmcgT09WIGF0IHRoZSBjb3N0IG9mIGhpZ2hlciBmZXJ0aWxpdHkgZm9yIHJhcmUgc2NyaXB0cy4iLCJUb2tlbml6ZXItZnJlZSBtb2RlbHMgZXhjZWwgb24gbm9pc3kgdGV4dCwgY29kZS1zd2l0Y2hpbmcsIGxvdy1yZXNvdXJjZSBsYW5ndWFnZXMsIGFuZCBjaGFyYWN0ZXItbGV2ZWwgdGFza3MuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVzZWFyY2ggZGlyZWN0aW9ucyBmb3IgdG9rZW5pemVyLWZyZWUgbW9kZWxzIGluY2x1ZGUgbGVhcm5lZCBwYXRjaC1zaXplIHNlbGVjdGlvbiAoYWRhcHRpbmcgUCBwZXIgaW5wdXQgcmVnaW9uKSwgY29tYmluaW5nIHBhdGNoLWJhc2VkIGNvbXByZXNzaW9uIHdpdGggc3BhcnNlIGF0dGVudGlvbiBmb3IgdmVyeSBsb25nIGRvY3VtZW50cywgYW5kIGRpc3RpbGxpbmcga25vd2xlZGdlIGZyb20gQlBFIG1vZGVscyBpbnRvIGJ5dGUtbGV2ZWwgbW9kZWxzIHRvIHdhcm0tc3RhcnQgdHJhaW5pbmcuIFRoZSBmaWVsZCBpcyBjb252ZXJnaW5nIHRvd2FyZCBoeWJyaWQgYXBwcm9hY2hlcyDigJQgc29mdCB0b2tlbml6YXRpb24gbW9kdWxlcyB0aGF0IGxlYXJuIEJQRS1saWtlIGdyb3VwaW5ncyBkaWZmZXJlbnRpYWxseSDigJQgd2hpY2ggbWF5IGV2ZW50dWFsbHkgc3VwZXJzZWRlIHRoZSBoYW5kLWRlc2lnbmVkIHRva2VuaXphdGlvbiBwaXBlbGluZXMgb2YgY3VycmVudCBmcm9udGllciBtb2RlbHMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Tokenizer-Free Models — Byte-Level and Patch-Based Approaches

Conventional language models interpose a tokenizer between raw text and the neural network: text is segmented into subword tokens drawn from a fixed vocabulary, then mapped to integer ids. This design introduces several failure modes: out-of-vocabulary characters degrade to byte-fallback with extreme fertility, pre-tokenization rules embed language-specific assumptions (spaces, hyphens, apostrophes), and token fertility imbalance disadvantages low-resource languages. Tokenizer-free architectures bypass this entirely by operating on raw bytes or characters, passing the segmentation problem to the neural network itself.

## Why Eliminate the Tokenizer?

The four main motivations for tokenizer-free models are: (1) OOV elimination — a byte-level vocabulary of 256 values handles any Unicode text via UTF-8 encoding, with no unknown-token fallback; (2) language equality — each language's fertility is determined by its UTF-8 byte density, not by its representation in the tokenizer's training corpus; (3) character-level task performance — tasks like spelling correction, typo robustness, morphological analysis, and phonetic transcription require character-level access that subword tokenization obscures; (4) elimination of pre-tokenization rules — regex-based pre-tokenizers (e.g., GPT's handling of contractions and punctuation) embed English-centric assumptions that impair multilingual performance.

## Byte-Level Input Pipeline

```python
import torch
import torch.nn.functional as F

def text_to_byte_patches(text, patch_size=4, pad_id=0):
    # Encode text to UTF-8 bytes
    raw_bytes = list(text.encode('utf-8'))
    n_bytes = len(raw_bytes)
    # Pad to multiple of patch_size
    pad_len = (patch_size - n_bytes % patch_size) % patch_size
    raw_bytes = raw_bytes + [pad_id] * pad_len
    byte_tensor = torch.tensor(raw_bytes, dtype=torch.long)
    n_patches = len(raw_bytes) // patch_size
    patches = byte_tensor.view(n_patches, patch_size)
    attention_mask = torch.ones(n_patches, dtype=torch.long)
    # Mask padding patches
    for i in range(n_patches - 1, -1, -1):
        if patches[i].sum() == 0:
            attention_mask[i] = 0
        else:
            break
    return patches, attention_mask

samples = ['Hello world', 'こんにちは', 'مرحبا']
for text in samples:
    raw = text.encode('utf-8')
    patches, mask = text_to_byte_patches(text, patch_size=4)
    print(f'{text!r:<20}: {len(raw)} bytes -> {patches.shape[0]} patches')
    print(f'  byte values: {list(raw[:12])}...')
    print(f'  patch[0]:    {patches[0].tolist()}')
```

## MegaByte — Hierarchical Patch-Based Processing

MegaByte (Yu et al. 2023) uses a two-level hierarchical architecture to reduce the quadratic cost of attention over raw bytes. A global transformer model processes sequences of patch embeddings (each patch being P consecutive bytes). A local transformer operates within each patch to predict the next P bytes given the global context. With patch size P=4, sequence length is reduced P-fold compared to pure byte-level models. The global model captures long-range dependencies across patches; the local model handles fine-grained character-level generation within each patch. This achieves competitive perplexity to GPT-style BPE models at 1/P the effective sequence length.

```python
import torch
import torch.nn as nn

class MegaByteLocal(nn.Module):
    # Local model: given patch context, predict next byte in patch
    def __init__(self, patch_size=4, d_model=128, n_heads=4, n_layers=2):
        super().__init__()
        self.patch_size = patch_size
        self.byte_embed = nn.Embedding(256 + 1, d_model)  # 256 bytes + pad
        self.pos_embed = nn.Embedding(patch_size, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model, n_heads, dim_feedforward=256, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        self.out_proj = nn.Linear(d_model, 256)

    def forward(self, byte_ids, global_context):
        # byte_ids: (batch, patch_size); global_context: (batch, d_model)
        B, P = byte_ids.shape
        pos = torch.arange(P, device=byte_ids.device)
        x = self.byte_embed(byte_ids) + self.pos_embed(pos).unsqueeze(0)
        x = x + global_context.unsqueeze(1)  # inject global context
        x = self.transformer(x)
        return self.out_proj(x)  # (batch, patch_size, 256)

class MegaByteGlobal(nn.Module):
    # Global model: process patch embeddings to produce context vectors
    def __init__(self, patch_size=4, d_model=128, n_heads=4, n_layers=3):
        super().__init__()
        self.patch_embed = nn.Linear(patch_size * d_model, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model, n_heads, dim_feedforward=256, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)

    def forward(self, patch_embeddings):
        x = self.transformer(patch_embeddings)
        return x  # (batch, n_patches, d_model)

# Demo
B, N_patches, P, D = 2, 8, 4, 128
byte_ids = torch.randint(0, 256, (B, P))
global_ctx = torch.randn(B, D)
local_model = MegaByteLocal(patch_size=P, d_model=D)
logits = local_model(byte_ids, global_ctx)
print(f'MegaByte local output: {logits.shape}  (batch, patch, vocab=256)')
```

## CharFormer GBST Soft Tokenization

CharFormer (Tay et al. 2021) introduces Gradient-Based Subword Tokenization (GBST), a differentiable module that learns to group characters into variable-length subword-like representations without a fixed vocabulary. A learnable scoring function assigns each character position a soft assignment over candidate block widths (1, 2, 3, ... characters). These soft assignments are learned end-to-end by gradient descent, allowing the model to discover optimal groupings for the task. The resulting representation has reduced sequence length (by roughly the mean block width) and is fully differentiable, unlike hard BPE segmentation.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GBSTBlock(nn.Module):
    # Simplified GBST: learn soft merging of characters into subword blocks
    def __init__(self, d_model=64, max_block=4, downsample_factor=2):
        super().__init__()
        self.max_block = max_block
        self.downsample_factor = downsample_factor
        self.char_embed = nn.Embedding(256, d_model)
        self.score_proj = nn.Linear(d_model, max_block)
        self.block_proj = nn.ModuleList([nn.Linear(d_model * w, d_model) for w in range(1, max_block + 1)])

    def forward(self, char_ids):
        # char_ids: (batch, seq_len)
        B, L = char_ids.shape
        x = self.char_embed(char_ids)  # (B, L, d_model)
        scores = self.score_proj(x)     # (B, L, max_block) -- block width scores
        weights = F.softmax(scores, dim=-1)  # soft block width assignment
        # Aggregate: for position i, collect weighted sum across block widths
        out = x.clone()
        for w_idx, w in enumerate(range(1, self.max_block + 1)):
            if w == 1:
                contribution = x * weights[:, :, w_idx:w_idx+1]
            else:
                padded = F.pad(x, (0, 0, 0, w - 1))
                pooled = padded.unfold(1, w, 1).mean(-1)  # (B, L, d_model)
                contribution = pooled * weights[:, :, w_idx:w_idx+1]
            out = out + contribution
        # Downsample by taking every downsample_factor-th position
        out = out[:, ::self.downsample_factor, :]  # (B, L//ds, d_model)
        return out

gbst = GBSTBlock(d_model=64, max_block=4, downsample_factor=2)
chars = torch.randint(0, 256, (2, 16))
out = gbst(chars)
print(f'Input:  {chars.shape}  (batch=2, seq_len=16 chars)')
print(f'Output: {out.shape}   (batch=2, seq_len={out.shape[1]} after 2x downsample)')
```

## ByT5 Tokenizer Usage

```python
from transformers import AutoTokenizer, T5Tokenizer
import torch

def compare_byt5_vs_t5(texts):
    byt5_tok = AutoTokenizer.from_pretrained('google/byt5-small')
    t5_tok = T5Tokenizer.from_pretrained('t5-small')
    print(f'{"Text":<40} {"ByT5 tokens":>12} {"T5 tokens":>12} {"Ratio":>8}')
    for text in texts:
        byt5_ids = byt5_tok.encode(text)
        t5_ids = t5_tok.encode(text)
        ratio = len(byt5_ids) / max(len(t5_ids), 1)
        short = text[:38] + '..' if len(text) > 40 else text
        print(f'{short:<40} {len(byt5_ids):>12} {len(t5_ids):>12} {ratio:>8.2f}x')
    # Show byte-level tokens for a short text
    sample = texts[0]
    ids = byt5_tok.encode(sample)
    decoded = [byt5_tok.decode([i]) for i in ids[:10]]
    print(f'\nByT5 byte tokens for {repr(sample[:20])}:')
    print(f'  ids={ids[:10]}  decoded={decoded}')

texts = [
    'Hello world',
    'naïve café résumé',
    'Speling mistaek correksion',
    '日本語テキスト',
    'مرحبا بالعالم',
]
compare_byt5_vs_t5(texts)
```

## Tokenizer-Free Architectures Comparison

| Architecture | Approach | Effective Vocab | Seq Length Factor | Key Strength |
| --- | --- | --- | --- | --- |
| ByT5 | Pure byte-level T5 encoder-decoder | 256 bytes + 3 special | 3–8× longer than BPE | No OOV; equal language treatment; robust to noise |
| MegaByte | Patch-based: global model over patches + local over bytes | 256 bytes (local) | ~1/P of byte-level (P=4–16) | Scales byte models to long sequences; competitive perplexity |
| CharFormer (GBST) | Differentiable soft character grouping | 256 chars; learned subword blocks | ~2–4× longer than BPE | End-to-end differentiable tokenization; task-adaptive grouping |
| CANINE | Char-level with strided conv compression | 143,000+ Unicode code points | ~4× longer than BPE then compressed | Multilingual with no script bias; hash-based embedding |
| Byte-level BPE | BPE applied to raw bytes instead of chars | 256–50,000 merged byte tokens | Similar to subword BPE | Eliminates OOV while keeping BPE merge efficiency |

## Tradeoffs vs Subword Models

The fundamental tradeoff of tokenizer-free models is sequence length versus generality. Operating on bytes or characters increases sequence length by 3–8× compared to BPE on the same text. Transformer self-attention scales quadratically with sequence length, making byte-level models proportionally more expensive. ByT5-small achieves comparable translation quality to T5-small on multilingual benchmarks but requires 3–5× more FLOPs per forward pass. Patch-based models like MegaByte reduce this cost by grouping bytes, but require a two-level architecture that complicates training and inference.

> **MegaByte Patch Models Reduce Sequence Length P-Fold**: MegaByte-style patch-based models achieve competitive perplexity at 1/P the sequence length of pure byte models by grouping bytes into patches — the local model handles intra-patch generation while the global model captures long-range context. With patch size P=8, a 1000-byte document requires only 125 global attention steps instead of 1000, bringing the quadratic attention cost down by 64×. The local model's cost is constant per patch and parallelisable across patches, making overall training cost comparable to a standard transformer on the same text with subword tokenisation.

Practical deployment considerations: ByT5 works best when the task is character-sensitive — spelling correction, transliteration, phonetic alignment, morphological analysis, or handling noisy user input with typos. For tasks where semantic content dominates and orthographic detail is irrelevant, BPE models are more efficient. CANINE and CharFormer are intermediate: they learn task-adaptive compression that reduces sequence length while retaining character-level access. For production multilingual systems where language equality matters more than inference cost, ByT5 or CANINE are strong baselines.

- ByT5 vocabulary: 256 raw bytes + 3 special tokens (pad, EOS, UNK) — the entire model is tokenizer-free.
- MegaByte patch size P: larger P reduces sequence length but makes the local model's task harder; P=4–8 is typical.
- CharFormer GBST is differentiable: the grouping is learned end-to-end, adapting to the task rather than text statistics.
- CANINE uses hash embeddings for Unicode code points, avoiding a fixed character vocabulary while covering all scripts.
- Byte-level BPE (used in GPT-2 and RoBERTa) is a hybrid: BPE merges applied to bytes, eliminating OOV at the cost of higher fertility for rare scripts.
- Tokenizer-free models excel on noisy text, code-switching, low-resource languages, and character-level tasks.

Research directions for tokenizer-free models include learned patch-size selection (adapting P per input region), combining patch-based compression with sparse attention for very long documents, and distilling knowledge from BPE models into byte-level models to warm-start training. The field is converging toward hybrid approaches — soft tokenization modules that learn BPE-like groupings differentially — which may eventually supersede the hand-designed tokenization pipelines of current frontier models.

---

