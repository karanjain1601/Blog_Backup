---
title: "Bahdanau Attention — Additive Attention and Alignment"
slug: "bahdanau-attention"
description: "Deep dive into Bahdanau's additive attention mechanism — alignment scores, context vectors, and the interpretable alignment matrix that laid the groundwork for the Transformer."
tags: ["deep-learning", "rnns", "sequence-models", "state-space-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gMjAxNOKAkzIwMTUsIEJhaGRhbmF1LCBDaG8sIGFuZCBCZW5naW8gaWRlbnRpZmllZCBhIGNyaXRpY2FsIGJvdHRsZW5lY2sgaW4gc2VxdWVuY2UtdG8tc2VxdWVuY2UgbW9kZWxzOiB0aGUgZW50aXJlIHNvdXJjZSBzZW50ZW5jZSB3YXMgY29tcHJlc3NlZCBpbnRvIGEgc2luZ2xlIGZpeGVkLXNpemUgY29udGV4dCB2ZWN0b3IgYmVmb3JlIGRlY29kaW5nIGJlZ2FuLiBGb3Igc2hvcnQgc2VudGVuY2VzIHRoaXMgd29ya3MgYWRlcXVhdGVseSwgYnV0IGZvciBsb25nZXIgc2VxdWVuY2VzIHRoZSBlbmNvZGVyIHN0cnVnZ2xlcyB0byBwYWNrIGFsbCByZWxldmFudCBpbmZvcm1hdGlvbiBpbnRvIG9uZSB2ZWN0b3Ig4oCUIGFuZCBCTEVVIHNjb3JlcyBkZWdyYWRlIHNoYXJwbHkgYXMgaW5wdXQgbGVuZ3RoIGdyb3dzLiBUaGVpciBzZW1pbmFsIHBhcGVyIGludHJvZHVjZWQgYSBtZWNoYW5pc20gdGhhdCBjb21wdXRlcyBhIGZyZXNoLCBkZWNvZGVyLXN0ZXAtc3BlY2lmaWMgY29udGV4dCB2ZWN0b3IgYXQgZWFjaCBkZWNvZGluZyBzdGVwLCBkcmF3biBhcyBhIHdlaWdodGVkIHN1bSBvZiBhbGwgZW5jb2RlciBoaWRkZW4gc3RhdGVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBTZXEyU2VxIEJvdHRsZW5lY2sgUHJvYmxlbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBzdGFuZGFyZCBzZXEyc2VxIG1vZGVsIGVuY29kZXMgdGhlIHNvdXJjZSBzZXF1ZW5jZSB44oKBLC4uLix4X3tUc30gaW50byBoaWRkZW4gc3RhdGVzIGjigoEsLi4uLGhfe1RzfSB1c2luZyBhIGJpZGlyZWN0aW9uYWwgUk5OLCB0aGVuIHBhc3NlcyBvbmx5IHRoZSBmaW5hbCBzdGF0ZSB0byB0aGUgZGVjb2Rlci4gVGhlIGRlY29kZXIgcHJvZHVjZXMgb3V0cHV0IHRva2VucyB54oKBLC4uLix5X3tUdH0gdXNpbmcgYSB1bmlkaXJlY3Rpb25hbCBSTk4gaW5pdGlhbGl6ZWQgd2l0aCB0aGF0IHNpbmdsZSBjb250ZXh0LiBUaGlzIGZvcmNlcyB0aGUgZW5jb2RlciB0byBzdW1tYXJpemUgYXJiaXRyYXJpbHkgbG9uZyBzZXF1ZW5jZXMgaW50byBhIGZpeGVkLWRpbWVuc2lvbmFsIHZlY3RvciDigJQgYW4gaW5mb3JtYXRpb24gYm90dGxlbmVjayB0aGF0IGdyb3dzIG1vcmUgc2V2ZXJlIGFzIHNvdXJjZSBsZW5ndGggaW5jcmVhc2VzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3RhbmRhcmQgc2VxMnNlcSBCTEVVIGRlZ3JhZGVzIHNpZ25pZmljYW50bHkgZm9yIHNlbnRlbmNlcyBsb25nZXIgdGhhbiAzMCB0b2tlbnMiLCJBIHNpbmdsZSBjb250ZXh0IHZlY3RvciBjYW5ub3QgcmVwcmVzZW50IGFsbCBzb3VyY2UgcG9zaXRpb25zIHNpbXVsdGFuZW91c2x5IiwiR3JhZGllbnQgbXVzdCBmbG93IHRocm91Z2ggZXZlcnkgZGVjb2RlciBzdGVwIGJhY2sgdG8gdGhlIGVuY29kZXIsIGNhdXNpbmcgdmFuaXNoaW5nIGdyYWRpZW50cyIsIkxvbmctZGlzdGFuY2UgZGVwZW5kZW5jaWVzIGJldHdlZW4gc291cmNlIGFuZCB0YXJnZXQgd29yZHMgYXJlIHBvb3JseSBjYXB0dXJlZCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgQmFoZGFuYXUgQXR0ZW50aW9uIE1lY2hhbmlzbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFoZGFuYXUgYXR0ZW50aW9uIGJyZWFrcyB0aGUgYm90dGxlbmVjayBieSBhbGxvd2luZyB0aGUgZGVjb2RlciB0byBsb29rIGJhY2sgYXQgYWxsIGVuY29kZXIgaGlkZGVuIHN0YXRlcyBhdCBlYWNoIGRlY29kaW5nIHN0ZXAuIFRoZSBhbGlnbm1lbnQgc2NvcmUgZeG1ouKxvCA9IHbhtYAgdGFuaChX4oKBc+KxvOKCi+KCgSArIFfigoJo4bWiKSwgd2hlcmUgc+KxvOKCi+KCgSBpcyB0aGUgZGVjb2RlciBzdGF0ZSBmcm9tIHRoZSBwcmV2aW91cyBzdGVwIGFuZCBo4bWiIGlzIHRoZSBpLXRoIGVuY29kZXIgaGlkZGVuIHN0YXRlLiBUaGlzIGFkZGl0aXZlIChjb25jYXQpIGZvcm11bGF0aW9uIHBhc3NlcyB0aGUgc3VtIHRocm91Z2ggdGFuaCBhbmQgYSBsZWFybmVkIHZlY3RvciB2LCBjb21wdXRpbmcgYW4gZW5lcmd5IG1lYXN1cmluZyBjb21wYXRpYmlsaXR5IGJldHdlZW4gcG9zaXRpb25zLiBUaGUgc2NvcmVzIGFyZSBub3JtYWxpemVkIHZpYSBzb2Z0bWF4OiDOseG1ouKxvCA9IHNvZnRtYXgoZeG1ouKxvCkuIFRoZSBjb250ZXh0IHZlY3RvciBmb3Igc3RlcCBqIGlzIHRoZSB3ZWlnaHRlZCBzdW0gY+KxvCA9IM6j4bWiIM6x4bWi4rG8aOG1oi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbImXhtaLisbwgPSB24bWAIHRhbmgoV+KCgXPisbzigovigoEgKyBX4oKCaOG1oikg4oCUIGFkZGl0aXZlL2NvbmNhdCBhbGlnbm1lbnQgc2NvcmUiLCLOseG1ouKxvCA9IHNvZnRtYXgoZeG1ouKxvCkgb3ZlciBhbGwgc291cmNlIHBvc2l0aW9ucyBpIOKAlCBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb24gc3VtbWluZyB0byAxIiwiY+KxvCA9IM6j4bWiIM6x4bWi4rG8aOG1oiDigJQgd2VpZ2h0ZWQgc3VtIG9mIGVuY29kZXIgc3RhdGVzLCBzcGVjaWZpYyB0byBkZWNvZGVyIHN0ZXAgaiIsIk8oVHMgw5cgVHQpIGFsaWdubWVudCBzY29yZXMgY29tcHV0ZWQgcGVyIHNlcXVlbmNlIHBhaXIiLCJBbGlnbm1lbnQgbWF0cml4IHvOseG1ouKxvH0gaXMgaW50ZXJwcmV0YWJsZTogc2hvd3Mgd2hpY2ggc291cmNlIHRva2VucyBkZWNvZGVyIGZvY3VzZXMgb24iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAxIOKAlCBCYWhkYW5hdSBBdHRlbnRpb24gZnJvbSBTY3JhdGNoIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgQmFoZGFuYXVBdHRlbnRpb24obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZW5jX2hpZGRlbl9kaW0sIGRlY19oaWRkZW5fZGltLCBhdHRuX2RpbSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLlcxID0gbm4uTGluZWFyKGRlY19oaWRkZW5fZGltLCBhdHRuX2RpbSwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XMiA9IG5uLkxpbmVhcihlbmNfaGlkZGVuX2RpbSwgYXR0bl9kaW0sIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYudiAgPSBubi5MaW5lYXIoYXR0bl9kaW0sIDEsIGJpYXM9RmFsc2UpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBzX3ByZXYsIGVuY29kZXJfb3V0cHV0cyk6XG4gICAgICAgICMgc19wcmV2OiAoYmF0Y2gsIGRlY19oaWRkZW5fZGltKVxuICAgICAgICAjIGVuY29kZXJfb3V0cHV0czogKGJhdGNoLCBzcmNfbGVuLCBlbmNfaGlkZGVuX2RpbSlcbiAgICAgICAgcyAgICAgID0gc2VsZi5XMShzX3ByZXYpLnVuc3F1ZWV6ZSgxKSAgICAgICAgICAgIyAoYmF0Y2gsIDEsIGF0dG5fZGltKVxuICAgICAgICBoICAgICAgPSBzZWxmLlcyKGVuY29kZXJfb3V0cHV0cykgICAgICAgICAgICAgICAgIyAoYmF0Y2gsIHNyY19sZW4sIGF0dG5fZGltKVxuICAgICAgICBlbmVyZ3kgPSBzZWxmLnYodG9yY2gudGFuaChzICsgaCkpLnNxdWVlemUoLTEpICAjIChiYXRjaCwgc3JjX2xlbilcbiAgICAgICAgYWxwaGEgID0gRi5zb2Z0bWF4KGVuZXJneSwgZGltPS0xKSAgICAgICAgICAgICAgICMgKGJhdGNoLCBzcmNfbGVuKVxuICAgICAgICAjIGNqID0gc3VtX2kgYWxwaGFfaWogKiBoX2lcbiAgICAgICAgY29udGV4dCA9IChhbHBoYS51bnNxdWVlemUoLTEpICogZW5jb2Rlcl9vdXRwdXRzKS5zdW0oZGltPTEpICAjIChiYXRjaCwgZW5jX2gpXG4gICAgICAgIHJldHVybiBjb250ZXh0LCBhbHBoYVxuXG4jIFF1aWNrIHRlc3RcbmJhdGNoLCBzcmNfbGVuLCBlbmNfaCwgZGVjX2gsIGF0dG5fZCA9IDIsIDEwLCAyNTYsIDI1NiwgMTI4XG5hdHRuICAgID0gQmFoZGFuYXVBdHRlbnRpb24oZW5jX2gsIGRlY19oLCBhdHRuX2QpXG5lbmNfb3V0ID0gdG9yY2gucmFuZG4oYmF0Y2gsIHNyY19sZW4sIGVuY19oKVxucyAgICAgICA9IHRvcmNoLnJhbmRuKGJhdGNoLCBkZWNfaClcbmN0eCwgd2VpZ2h0cyA9IGF0dG4ocywgZW5jX291dClcbnByaW50KGZcIkNvbnRleHQ6IHtjdHguc2hhcGV9LCBXZWlnaHRzOiB7d2VpZ2h0cy5zaGFwZX0sIFN1bToge3dlaWdodHMuc3VtKC0xKX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIFNlcTJTZXEgd2l0aCBCYWhkYW5hdSBBdHRlbnRpb24gZm9yIFRyYW5zbGF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEVuY29kZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdm9jYWJfc2l6ZSwgZW1iZWRfZGltLCBoaWRkZW5fZGltKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW1iZWQgPSBubi5FbWJlZGRpbmcodm9jYWJfc2l6ZSwgZW1iZWRfZGltLCBwYWRkaW5nX2lkeD0wKVxuICAgICAgICBzZWxmLnJubiAgID0gbm4uR1JVKGVtYmVkX2RpbSwgaGlkZGVuX2RpbSwgYmF0Y2hfZmlyc3Q9VHJ1ZSwgYmlkaXJlY3Rpb25hbD1UcnVlKVxuICAgICAgICBzZWxmLmZjICAgID0gbm4uTGluZWFyKGhpZGRlbl9kaW0gKiAyLCBoaWRkZW5fZGltKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHNyYyk6XG4gICAgICAgIGVtYiA9IHNlbGYuZW1iZWQoc3JjKVxuICAgICAgICBvdXQsIGhpZGRlbiA9IHNlbGYucm5uKGVtYilcbiAgICAgICAgaGlkZGVuID0gdG9yY2gudGFuaChzZWxmLmZjKHRvcmNoLmNhdChbaGlkZGVuWy0yXSwgaGlkZGVuWy0xXV0sIGRpbT0tMSkpKVxuICAgICAgICByZXR1cm4gb3V0LCBoaWRkZW4gICMgb3V0OiAoQiwgVCwgMkgpLCBoaWRkZW46IChCLCBIKVxuXG5jbGFzcyBEZWNvZGVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHZvY2FiX3NpemUsIGVtYmVkX2RpbSwgZW5jX2gsIGRlY19oLCBhdHRuX2QpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbWJlZCAgPSBubi5FbWJlZGRpbmcodm9jYWJfc2l6ZSwgZW1iZWRfZGltKVxuICAgICAgICBzZWxmLmF0dG5fVzEgPSBubi5MaW5lYXIoZGVjX2gsIGF0dG5fZCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5hdHRuX1cyID0gbm4uTGluZWFyKGVuY19oICogMiwgYXR0bl9kLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmF0dG5fdiAgPSBubi5MaW5lYXIoYXR0bl9kLCAxLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnJubiAgICAgPSBubi5HUlVDZWxsKGVtYmVkX2RpbSArIGVuY19oICogMiwgZGVjX2gpXG4gICAgICAgIHNlbGYuZmNfb3V0ICA9IG5uLkxpbmVhcihkZWNfaCArIGVuY19oICogMiArIGVtYmVkX2RpbSwgdm9jYWJfc2l6ZSlcblxuICAgIGRlZiBhdHRlbnRpb24oc2VsZiwgcywgZW5jX291dCk6XG4gICAgICAgIGUgPSBzZWxmLmF0dG5fdih0b3JjaC50YW5oKHNlbGYuYXR0bl9XMShzKS51bnNxdWVlemUoMSkgKyBzZWxmLmF0dG5fVzIoZW5jX291dCkpKS5zcXVlZXplKC0xKVxuICAgICAgICByZXR1cm4gRi5zb2Z0bWF4KGUsIGRpbT0tMSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHRva2VuLCBzLCBlbmNfb3V0KTpcbiAgICAgICAgZW1iICAgPSBzZWxmLmVtYmVkKHRva2VuKVxuICAgICAgICBhbHBoYSA9IHNlbGYuYXR0ZW50aW9uKHMsIGVuY19vdXQpXG4gICAgICAgIGN0eCAgID0gKGFscGhhLnVuc3F1ZWV6ZSgtMSkgKiBlbmNfb3V0KS5zdW0oMSlcbiAgICAgICAgc19uZXcgPSBzZWxmLnJubih0b3JjaC5jYXQoW2VtYiwgY3R4XSwgZGltPS0xKSwgcylcbiAgICAgICAgbG9naXRzID0gc2VsZi5mY19vdXQodG9yY2guY2F0KFtzX25ldywgY3R4LCBlbWJdLCBkaW09LTEpKVxuICAgICAgICByZXR1cm4gbG9naXRzLCBzX25ldywgYWxwaGFcblxucHJpbnQoXCJFbmNvZGVyIGFuZCBCYWhkYW5hdSBEZWNvZGVyIGRlZmluZWQgc3VjY2Vzc2Z1bGx5LlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMyDigJQgQWxpZ25tZW50IE1hdHJpeCBWaXN1YWxpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgYWxpZ25tZW50IG1hdHJpeCB7zrHhtaLisbx9IGlzIG9uZSBvZiB0aGUgbW9zdCBzdHJpa2luZyBmZWF0dXJlcyBvZiBCYWhkYW5hdSBhdHRlbnRpb24g4oCUIGl0IGlzIGRpcmVjdGx5IGludGVycHJldGFibGUgYXMgYSBzb2Z0IGFsaWdubWVudCBiZXR3ZWVuIHNvdXJjZSBhbmQgdGFyZ2V0IHdvcmRzLiBGb3Igd2VsbC10cmFpbmVkIHRyYW5zbGF0aW9uIG1vZGVscyBpdCByZXZlYWxzIG5lYXItZGlhZ29uYWwgc3RydWN0dXJlIGZvciBsYW5ndWFnZSBwYWlycyB3aXRoIHNpbWlsYXIgd29yZCBvcmRlciAoRnJlbmNoLUVuZ2xpc2gpIGFuZCBvZmYtZGlhZ29uYWwgcGF0dGVybnMgZm9yIGxhbmd1YWdlcyB3aXRoIGRpZmZlcmVudCBzeW50YWN0aWMgb3JkZXIgKEdlcm1hbiB2ZXJiLWZpbmFsKS4gVGhlIGhlYXRtYXAgYmVsb3cgcGxvdHMgZGVjb2RlciBzdGVwcyBvbiB0aGUgeS1heGlzIGFuZCBzb3VyY2UgcG9zaXRpb25zIG9uIHRoZSB4LWF4aXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcGxvdF9hdHRlbnRpb25faGVhdG1hcCh3ZWlnaHRzLCBzcmNfdG9rZW5zLCB0Z3RfdG9rZW5zLCB0aXRsZT1cIkF0dGVudGlvbiBBbGlnbm1lbnRcIik6XG4gICAgXCJcIlwiXG4gICAgd2VpZ2h0czogKHRndF9sZW4sIHNyY19sZW4pIG51bXB5IGFycmF5IG9mIGF0dGVudGlvbiB3ZWlnaHRzIGFscGhhX2lqXG4gICAgc3JjX3Rva2VuczogbGlzdCBvZiBzb3VyY2Ugd29yZHNcbiAgICB0Z3RfdG9rZW5zOiBsaXN0IG9mIHRhcmdldC9kZWNvZGVyIHdvcmRzXG4gICAgXCJcIlwiXG4gICAgZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSgxMCwgOCkpXG4gICAgaW0gPSBheC5pbXNob3cod2VpZ2h0cywgY21hcD1cdTAwMjdCbHVlc1x1MDAyNywgYXNwZWN0PVx1MDAyN2F1dG9cdTAwMjcsIHZtaW49MCwgdm1heD0xKVxuICAgIGF4LnNldF94dGlja3MocmFuZ2UobGVuKHNyY190b2tlbnMpKSlcbiAgICBheC5zZXRfeXRpY2tzKHJhbmdlKGxlbih0Z3RfdG9rZW5zKSkpXG4gICAgYXguc2V0X3h0aWNrbGFiZWxzKHNyY190b2tlbnMsIHJvdGF0aW9uPTQ1LCBoYT1cdTAwMjdyaWdodFx1MDAyNywgZm9udHNpemU9MTEpXG4gICAgYXguc2V0X3l0aWNrbGFiZWxzKHRndF90b2tlbnMsIGZvbnRzaXplPTExKVxuICAgIGF4LnNldF94bGFiZWwoXHUwMDI3U291cmNlIChFbmNvZGVyIHBvc2l0aW9ucylcdTAwMjcsIGZvbnRzaXplPTEyKVxuICAgIGF4LnNldF95bGFiZWwoXHUwMDI3VGFyZ2V0IChEZWNvZGVyIHN0ZXBzKVx1MDAyNywgZm9udHNpemU9MTIpXG4gICAgYXguc2V0X3RpdGxlKHRpdGxlLCBmb250c2l6ZT0xNCwgZm9udHdlaWdodD1cdTAwMjdib2xkXHUwMDI3KVxuICAgIHBsdC5jb2xvcmJhcihpbSwgYXg9YXgsIGxhYmVsPVx1MDAyN0FscGhhIHdlaWdodFx1MDAyNylcbiAgICBmb3IgaSBpbiByYW5nZShsZW4odGd0X3Rva2VucykpOlxuICAgICAgICBmb3IgaiBpbiByYW5nZShsZW4oc3JjX3Rva2VucykpOlxuICAgICAgICAgICAgYXgudGV4dChqLCBpLCBmXHUwMDI3e3dlaWdodHNbaSxqXTouMmZ9XHUwMDI3LCBoYT1cdTAwMjdjZW50ZXJcdTAwMjcsIHZhPVx1MDAyN2NlbnRlclx1MDAyNywgZm9udHNpemU9OClcbiAgICBwbHQudGlnaHRfbGF5b3V0KClcbiAgICBwbHQuc2F2ZWZpZyhcdTAwMjdhdHRlbnRpb25fYWxpZ25tZW50LnBuZ1x1MDAyNywgZHBpPTE1MClcbiAgICBwbHQuc2hvdygpXG5cbiMgU2ltdWxhdGVkIEZyZW5jaCAtXHUwMDNlIEVuZ2xpc2ggYWxpZ25tZW50XG5zcmMgPSBbXHUwMDI3SmVcdTAwMjcsIFx1MDAyN3N1aXNcdTAwMjcsIFx1MDAyN2V0dWRpYW50XHUwMDI3LCBcdTAwMjdcdTAwM2Nlb3NcdTAwM2VcdTAwMjddXG50Z3QgPSBbXHUwMDI3SVx1MDAyNywgXHUwMDI3YW1cdTAwMjcsIFx1MDAyN2FcdTAwMjcsIFx1MDAyN3N0dWRlbnRcdTAwMjcsIFx1MDAyN1x1MDAzY2Vvc1x1MDAzZVx1MDAyN11cbndlaWdodHMgPSBucC5hcnJheShbWzAuODUsIDAuMDgsIDAuMDQsIDAuMDNdLFxuICAgICAgICAgICAgICAgICAgICBbMC4xMCwgMC44MCwgMC4wNiwgMC4wNF0sXG4gICAgICAgICAgICAgICAgICAgIFswLjA1LCAwLjA1LCAwLjg1LCAwLjA1XSxcbiAgICAgICAgICAgICAgICAgICAgWzAuMDQsIDAuMTAsIDAuODIsIDAuMDRdLFxuICAgICAgICAgICAgICAgICAgICBbMC4wMiwgMC4wMywgMC4wNSwgMC45MF1dKVxucGxvdF9hdHRlbnRpb25faGVhdG1hcCh3ZWlnaHRzLCBzcmMsIHRndCwgXCJCYWhkYW5hdSBBdHRlbnRpb246IEZyZW5jaCB0byBFbmdsaXNoXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSA0IOKAlCBBdHRlbnRpb24gdnMgTm8tQXR0ZW50aW9uIEJMRVUgdnMgTGVuZ3RoIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgc2ltX2JsZXUoYmFzZSwgZGVjYXksIGxlbmd0aHMsIG5vaXNlX3N0ZD0wLjUsIHNlZWQ9MCk6XG4gICAgXCJcIlwiU2ltdWxhdGUgQkxFVSBzY29yZXMgdGhhdCBkZWNheSB3aXRoIHNlbnRlbmNlIGxlbmd0aC5cIlwiXCJcbiAgICBucC5yYW5kb20uc2VlZChzZWVkKVxuICAgIHNjb3JlcyA9IFtdXG4gICAgZm9yIEwgaW4gbGVuZ3RoczpcbiAgICAgICAgcyA9IGJhc2UgKiBucC5leHAoLWRlY2F5ICogbWF4KEwgLSAxMCwgMCkpICsgbnAucmFuZG9tLnJhbmRuKCkgKiBub2lzZV9zdGRcbiAgICAgICAgc2NvcmVzLmFwcGVuZChtYXgocm91bmQocywgMiksIDEuMCkpXG4gICAgcmV0dXJuIHNjb3Jlc1xuXG5sZW5ndGhzID0gbGlzdChyYW5nZSg1LCA1NSwgNSkpXG5ub19hdHRuICA9IHNpbV9ibGV1KDI4LjAsIDAuMDQwLCBsZW5ndGhzLCBzZWVkPTEpXG5iYWhkYW5hdSA9IHNpbV9ibGV1KDMwLjUsIDAuMDEyLCBsZW5ndGhzLCBzZWVkPTIpXG5cbmZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oOSwgNSkpXG5heC5wbG90KGxlbmd0aHMsIG5vX2F0dG4sICBcdTAwMjdyLS1vXHUwMDI3LCBsYWJlbD1cdTAwMjdTZXEyU2VxIChubyBhdHRlbnRpb24pXHUwMDI3LCBsaW5ld2lkdGg9MilcbmF4LnBsb3QobGVuZ3RocywgYmFoZGFuYXUsIFx1MDAyN2Itc1x1MDAyNywgIGxhYmVsPVx1MDAyN1NlcTJTZXEgKyBCYWhkYW5hdVx1MDAyNywgICAgbGluZXdpZHRoPTIpXG5heC5maWxsX2JldHdlZW4obGVuZ3Rocywgbm9fYXR0biwgYmFoZGFuYXUsIGFscGhhPTAuMTUsIGNvbG9yPVx1MDAyN2JsdWVcdTAwMjcpXG5heC5zZXRfeGxhYmVsKFx1MDAyN1NvdXJjZSBTZW50ZW5jZSBMZW5ndGggKHRva2VucylcdTAwMjcsIGZvbnRzaXplPTEyKVxuYXguc2V0X3lsYWJlbChcdTAwMjdCTEVVIFNjb3JlXHUwMDI3LCBmb250c2l6ZT0xMilcbmF4LnNldF90aXRsZShcdTAwMjdCTEVVIHZzIFNlbnRlbmNlIExlbmd0aDogQXR0ZW50aW9uIHZzIE5vLUF0dGVudGlvblx1MDAyNywgZm9udHNpemU9MTMpXG5heC5sZWdlbmQoZm9udHNpemU9MTEpXG5heC5ncmlkKFRydWUsIGFscGhhPTAuMylcbmF4LmFubm90YXRlKFx1MDAyN2F0dGVudGlvbiBnYXAgd2lkZW5zXFxud2l0aCBsZW5ndGhcdTAwMjcsIHh5PSgzOCwgMTUpLFxuICAgICAgICAgICAgZm9udHNpemU9MTAsIGNvbG9yPVx1MDAyN2JsdWVcdTAwMjcsIHN0eWxlPVx1MDAyN2l0YWxpY1x1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3YmxldV92c19sZW5ndGgucG5nXHUwMDI3LCBkcGk9MTUwKVxucGx0LnNob3coKVxucHJpbnQoXCJBdHRlbnRpb24gYWR2YW50YWdlIGdyb3dzIGZyb20gfjIgQkxFVSBhdCBMPTEwIHRvIH44IEJMRVUgYXQgTD01MC5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIYXJkIEF0dGVudGlvbiB2cyBTb2Z0IEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFoZGFuYXVcdTAwMjdzIG9yaWdpbmFsIGF0dGVudGlvbiBpcyBzb2Z0IGF0dGVudGlvbjogdGhlIGNvbnRleHQgdmVjdG9yIGlzIGEgZGlmZmVyZW50aWFibGUgd2VpZ2h0ZWQgc3VtIG92ZXIgYWxsIGVuY29kZXIgcG9zaXRpb25zLCBlbmFibGluZyBlbmQtdG8tZW5kIGJhY2twcm9wYWdhdGlvbi4gSGFyZCBhdHRlbnRpb24gKFh1IGV0IGFsLiwgMjAxNSwgZm9yIGltYWdlIGNhcHRpb25pbmcpIHNhbXBsZXMgYSBzaW5nbGUgcG9zaXRpb24gc3RvY2hhc3RpY2FsbHkgcmF0aGVyIHRoYW4gY29tcHV0aW5nIGEgd2VpZ2h0ZWQgYXZlcmFnZS4gSGFyZCBhdHRlbnRpb24gcmVxdWlyZXMgUkVJTkZPUkNFLXN0eWxlIHBvbGljeSBncmFkaWVudCB0cmFpbmluZywgaXMgbm9uLWRpZmZlcmVudGlhYmxlLCBhbmQgcHJvZHVjZXMgc3BhcnNlciDigJQgc29tZXRpbWVzIG1vcmUgaW50ZXJwcmV0YWJsZSDigJQgc2VsZWN0aW9ucy4gTW9zdCBzdWJzZXF1ZW50IHdvcmsgZGVmYXVsdHMgdG8gc29mdCBhdHRlbnRpb24gZHVlIHRvIGl0cyB0cmFpbmluZyBzaW1wbGljaXR5IGFuZCBiZXR0ZXIgb3B0aW1pemF0aW9uIGxhbmRzY2FwZS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkF0dGVudGlvbiBhcyBNZW1vcnkgUmV0cmlldmFsIiwiY29udGVudCI6IkF0dGVudGlvbiBjYW4gYmUgdmlld2VkIGFzIHNvZnQga2V5LXZhbHVlIHJldHJpZXZhbDogdGhlIGRlY29kZXIgaGlkZGVuIHN0YXRlIGFjdHMgYXMgYSBxdWVyeSBRLCBlbmNvZGVyIGhpZGRlbiBzdGF0ZXMgYWN0IGFzIGtleXMgSywgYW5kIGVuY29kZXIgb3V0cHV0cyBhY3QgYXMgdmFsdWVzIFYuIFRoZSBhbGlnbm1lbnQgc2NvcmUgY29tcHV0ZXMgcXVlcnkta2V5IGNvbXBhdGliaWxpdHksIHNvZnRtYXggbm9ybWFsaXplcyBpbnRvIGEgcHJvYmFiaWxpdHksIGFuZCB0aGUgY29udGV4dCB2ZWN0b3IgaXMgdGhlIHdlaWdodGVkIHZhbHVlIHN1bS4gVGhpcyBxdWVyeS1rZXktdmFsdWUgZnJhbWluZyBkaXJlY3RseSBpbnNwaXJlZCB0aGUgVHJhbnNmb3JtZXJcdTAwMjdzIHNjYWxlZCBkb3QtcHJvZHVjdCBhdHRlbnRpb24g4oCUIHJlcGxhY2UgdGhlIGFkZGl0aXZlIHNjb3JlIHdpdGggceG1gGsgLyBzcXJ0KGRfaykgYW5kIHJlbW92ZSB0aGUgUk5OLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZyb20gQmFoZGFuYXUgdG8gVHJhbnNmb3JtZXIgQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYWhkYW5hdSBhdHRlbnRpb24gZXN0YWJsaXNoZWQgdGhlIGNvbmNlcHR1YWwgdGVtcGxhdGUgdGhhdCBzY2FsZWQgaW50byB0aGUgVHJhbnNmb3JtZXIuIFRocmVlIGtleSBldm9sdXRpb25zOiAoMSkgYWRkaXRpdmUgc2NvcmluZyByZXBsYWNlZCBieSBzY2FsZWQgZG90LXByb2R1Y3QgZeG1ouKxvCA9IHHisbzhtYBr4bWiIC8g4oiaZF9rIGZvciBjb21wdXRhdGlvbmFsIGVmZmljaWVuY3kgb24gbW9kZXJuIGhhcmR3YXJlOyAoMikgdGhlIFJOTiBiYWNrYm9uZSByZW1vdmVkIGVudGlyZWx5IOKAlCBzZWxmLWF0dGVudGlvbiByZXBsYWNlZCByZWN1cnJlbmNlLCBlbmFibGluZyBPKDEpIGRlcHRoIGZvciBhbnkgcGFpcndpc2UgaW50ZXJhY3Rpb24gYW5kIGZ1bGwgcGFyYWxsZWxpc20gb3ZlciB0aGUgc2VxdWVuY2U7ICgzKSBtdWx0aS1oZWFkIGF0dGVudGlvbiBhcHBsaWVzIG11bHRpcGxlIGF0dGVudGlvbiBmdW5jdGlvbnMgaW4gcGFyYWxsZWwsIGVhY2ggbGVhcm5pbmcgZGlmZmVyZW50IGFzcGVjdHMgb2YgYWxpZ25tZW50LiBUaGUgZ3JhZGllbnQtZmxvdyBhZHZhbnRhZ2Ug4oCUIGRpcmVjdCBwYXRocyBmcm9tIGFueSBkZWNvZGVyIHBvc2l0aW9uIHRvIGFueSBlbmNvZGVyIHBvc2l0aW9uIOKAlCBpcyBwcmVzZXJ2ZWQgYWNyb3NzIGFsbCB2YXJpYW50cy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmFyaWFudCIsIlNjb3JlIEZvcm11bGEiLCJDb21wbGV4aXR5IiwiVXNlcyBSTk4iLCJPcmlnaW5hbCBQYXBlciJdLCJyb3dzIjpbWyJCYWhkYW5hdSAoYWRkaXRpdmUpIiwiduG1gCB0YW5oKFfigoFzICsgV+KCgmgpIiwiTyhUwrLCt2QpIiwiWWVzIChiaUdSVSkiLCJCYWhkYW5hdSAyMDE1Il0sWyJMdW9uZyBkb3QiLCJz4bWAaCIsIk8oVMKyKSIsIlllcyAoTFNUTSkiLCJMdW9uZyAyMDE1Il0sWyJMdW9uZyBnZW5lcmFsIiwic+G1gFdoIiwiTyhUwrLCt2QpIiwiWWVzIChMU1RNKSIsIkx1b25nIDIwMTUiXSxbIkx1b25nIGNvbmNhdCIsInbhtYAgdGFuaChXW3M7aF0pIiwiTyhUwrLCt2QpIiwiWWVzIChMU1RNKSIsIkx1b25nIDIwMTUiXSxbIlNjYWxlZCBkb3QtcHJvZHVjdCIsInHhtYBrIC8g4oiaZF9rIiwiTyhUwrIpIiwiTm8iLCJWYXN3YW5pIDIwMTciXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFoZGFuYXUgYXR0ZW50aW9uIGhhcyBhZ2VkIHJlbWFya2FibHkgd2VsbC4gSXRzIGNvcmUgaW50dWl0aW9uIOKAlCB0aGF0IGRlY29kaW5nIHNob3VsZCBiZSBjb25kaXRpb25lZCBvbiBhIGNvbnRlbnQtc3BlY2lmaWMgd2VpZ2h0ZWQgY29tYmluYXRpb24gb2YgZW5jb2RlciByZXByZXNlbnRhdGlvbnMgcmF0aGVyIHRoYW4gYSBmaXhlZCBzdW1tYXJ5IOKAlCBwcm92ZWQgZnVuZGFtZW50YWwuIEV2ZXJ5IG1vZGVybiBzZXF1ZW5jZSBtb2RlbCBpbmhlcml0cyB0aGlzIGlkZWE6IEJFUlRcdTAwMjdzIGJpZGlyZWN0aW9uYWwgc2VsZi1hdHRlbnRpb24sIEdQVFx1MDAyN3MgY2F1c2FsIHNlbGYtYXR0ZW50aW9uLCBjcm9zcy1hdHRlbnRpb24gaW4gZGlmZnVzaW9uIGFuZCBzcGVlY2ggbW9kZWxzLiBUaGUgYWxpZ25tZW50IHZpc3VhbGl6YXRpb24gYWxzbyBmb3Jlc2hhZG93ZWQgbW9kZXJuIGV4cGxhaW5hYmlsaXR5OiBhdHRlbnRpb24gd2VpZ2h0IGFuYWx5c2lzIHJlbWFpbnMgYSBwcmltYXJ5IHRvb2wgZm9yIHVuZGVyc3RhbmRpbmcgd2hhdCBzZXF1ZW5jZSBtb2RlbHMgaGF2ZSBsZWFybmVkLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTyhUcyDDlyBUdCkgY29zdCBpcyBhZmZvcmRhYmxlIGZvciBzZW50ZW5jZS1sZXZlbCBzZXF1ZW5jZXMgKFQgXHUwMDNjIDIwMCkiLCJCaWRpcmVjdGlvbmFsIGVuY29kZXIgaGlkZGVuIHN0YXRlcyBo4bWiIGNhcHR1cmUgbG9jYWwgY29udGV4dCBmcm9tIGJvdGggZGlyZWN0aW9ucyIsIkRpcmVjdCBncmFkaWVudCBwYXRoIGZyb20gbG9zcyB0byBlYWNoIGVuY29kZXIgc3RhdGUg4oCUIG5vIGJvdHRsZW5lY2sgdmFuaXNoaW5nIGdyYWRpZW50IiwiQWxpZ25tZW50IG1hdHJpeCBpcyBpbnRlcnByZXRhYmxlOiBuZWFyLWRpYWdvbmFsIGZvciBzaW1pbGFyLW9yZGVyIGxhbmd1YWdlcyIsIkZvdW5kYXRpb24gZm9yIHNlbGYtYXR0ZW50aW9uOiB3aGVuIFE9Sz1WIGFsbCBjb21lIGZyb20gdGhlIHNhbWUgc2VxdWVuY2UiXX1d"
---
# Bahdanau Attention — Additive Attention and Alignment

In 2014–2015, Bahdanau, Cho, and Bengio identified a critical bottleneck in sequence-to-sequence models: the entire source sentence was compressed into a single fixed-size context vector before decoding began. For short sentences this works adequately, but for longer sequences the encoder struggles to pack all relevant information into one vector — and BLEU scores degrade sharply as input length grows. Their seminal paper introduced a mechanism that computes a fresh, decoder-step-specific context vector at each decoding step, drawn as a weighted sum of all encoder hidden states.

## The Seq2Seq Bottleneck Problem

A standard seq2seq model encodes the source sequence x₁,...,x_{Ts} into hidden states h₁,...,h_{Ts} using a bidirectional RNN, then passes only the final state to the decoder. The decoder produces output tokens y₁,...,y_{Tt} using a unidirectional RNN initialized with that single context. This forces the encoder to summarize arbitrarily long sequences into a fixed-dimensional vector — an information bottleneck that grows more severe as source length increases.

- Standard seq2seq BLEU degrades significantly for sentences longer than 30 tokens
- A single context vector cannot represent all source positions simultaneously
- Gradient must flow through every decoder step back to the encoder, causing vanishing gradients
- Long-distance dependencies between source and target words are poorly captured

## The Bahdanau Attention Mechanism

Bahdanau attention breaks the bottleneck by allowing the decoder to look back at all encoder hidden states at each decoding step. The alignment score eᵢⱼ = vᵀ tanh(W₁sⱼ₋₁ + W₂hᵢ), where sⱼ₋₁ is the decoder state from the previous step and hᵢ is the i-th encoder hidden state. This additive (concat) formulation passes the sum through tanh and a learned vector v, computing an energy measuring compatibility between positions. The scores are normalized via softmax: αᵢⱼ = softmax(eᵢⱼ). The context vector for step j is the weighted sum cⱼ = Σᵢ αᵢⱼhᵢ.

- eᵢⱼ = vᵀ tanh(W₁sⱼ₋₁ + W₂hᵢ) — additive/concat alignment score
- αᵢⱼ = softmax(eᵢⱼ) over all source positions i — probability distribution summing to 1
- cⱼ = Σᵢ αᵢⱼhᵢ — weighted sum of encoder states, specific to decoder step j
- O(Ts × Tt) alignment scores computed per sequence pair
- Alignment matrix {αᵢⱼ} is interpretable: shows which source tokens decoder focuses on

## Code 1 — Bahdanau Attention from Scratch

```python
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class BahdanauAttention(nn.Module):
    def __init__(self, enc_hidden_dim, dec_hidden_dim, attn_dim):
        super().__init__()
        self.W1 = nn.Linear(dec_hidden_dim, attn_dim, bias=False)
        self.W2 = nn.Linear(enc_hidden_dim, attn_dim, bias=False)
        self.v  = nn.Linear(attn_dim, 1, bias=False)

    def forward(self, s_prev, encoder_outputs):
        # s_prev: (batch, dec_hidden_dim)
        # encoder_outputs: (batch, src_len, enc_hidden_dim)
        s      = self.W1(s_prev).unsqueeze(1)           # (batch, 1, attn_dim)
        h      = self.W2(encoder_outputs)                # (batch, src_len, attn_dim)
        energy = self.v(torch.tanh(s + h)).squeeze(-1)  # (batch, src_len)
        alpha  = F.softmax(energy, dim=-1)               # (batch, src_len)
        # cj = sum_i alpha_ij * h_i
        context = (alpha.unsqueeze(-1) * encoder_outputs).sum(dim=1)  # (batch, enc_h)
        return context, alpha

# Quick test
batch, src_len, enc_h, dec_h, attn_d = 2, 10, 256, 256, 128
attn    = BahdanauAttention(enc_h, dec_h, attn_d)
enc_out = torch.randn(batch, src_len, enc_h)
s       = torch.randn(batch, dec_h)
ctx, weights = attn(s, enc_out)
print(f"Context: {ctx.shape}, Weights: {weights.shape}, Sum: {weights.sum(-1)}")
```

## Code 2 — Seq2Seq with Bahdanau Attention for Translation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class Encoder(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.rnn   = nn.GRU(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.fc    = nn.Linear(hidden_dim * 2, hidden_dim)
    def forward(self, src):
        emb = self.embed(src)
        out, hidden = self.rnn(emb)
        hidden = torch.tanh(self.fc(torch.cat([hidden[-2], hidden[-1]], dim=-1)))
        return out, hidden  # out: (B, T, 2H), hidden: (B, H)

class Decoder(nn.Module):
    def __init__(self, vocab_size, embed_dim, enc_h, dec_h, attn_d):
        super().__init__()
        self.embed  = nn.Embedding(vocab_size, embed_dim)
        self.attn_W1 = nn.Linear(dec_h, attn_d, bias=False)
        self.attn_W2 = nn.Linear(enc_h * 2, attn_d, bias=False)
        self.attn_v  = nn.Linear(attn_d, 1, bias=False)
        self.rnn     = nn.GRUCell(embed_dim + enc_h * 2, dec_h)
        self.fc_out  = nn.Linear(dec_h + enc_h * 2 + embed_dim, vocab_size)

    def attention(self, s, enc_out):
        e = self.attn_v(torch.tanh(self.attn_W1(s).unsqueeze(1) + self.attn_W2(enc_out))).squeeze(-1)
        return F.softmax(e, dim=-1)

    def forward(self, token, s, enc_out):
        emb   = self.embed(token)
        alpha = self.attention(s, enc_out)
        ctx   = (alpha.unsqueeze(-1) * enc_out).sum(1)
        s_new = self.rnn(torch.cat([emb, ctx], dim=-1), s)
        logits = self.fc_out(torch.cat([s_new, ctx, emb], dim=-1))
        return logits, s_new, alpha

print("Encoder and Bahdanau Decoder defined successfully.")
```

## Code 3 — Alignment Matrix Visualization

The alignment matrix {αᵢⱼ} is one of the most striking features of Bahdanau attention — it is directly interpretable as a soft alignment between source and target words. For well-trained translation models it reveals near-diagonal structure for language pairs with similar word order (French-English) and off-diagonal patterns for languages with different syntactic order (German verb-final). The heatmap below plots decoder steps on the y-axis and source positions on the x-axis.

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_attention_heatmap(weights, src_tokens, tgt_tokens, title="Attention Alignment"):
    """
    weights: (tgt_len, src_len) numpy array of attention weights alpha_ij
    src_tokens: list of source words
    tgt_tokens: list of target/decoder words
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(weights, cmap='Blues', aspect='auto', vmin=0, vmax=1)
    ax.set_xticks(range(len(src_tokens)))
    ax.set_yticks(range(len(tgt_tokens)))
    ax.set_xticklabels(src_tokens, rotation=45, ha='right', fontsize=11)
    ax.set_yticklabels(tgt_tokens, fontsize=11)
    ax.set_xlabel('Source (Encoder positions)', fontsize=12)
    ax.set_ylabel('Target (Decoder steps)', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    plt.colorbar(im, ax=ax, label='Alpha weight')
    for i in range(len(tgt_tokens)):
        for j in range(len(src_tokens)):
            ax.text(j, i, f'{weights[i,j]:.2f}', ha='center', va='center', fontsize=8)
    plt.tight_layout()
    plt.savefig('attention_alignment.png', dpi=150)
    plt.show()

# Simulated French -> English alignment
src = ['Je', 'suis', 'etudiant', '<eos>']
tgt = ['I', 'am', 'a', 'student', '<eos>']
weights = np.array([[0.85, 0.08, 0.04, 0.03],
                    [0.10, 0.80, 0.06, 0.04],
                    [0.05, 0.05, 0.85, 0.05],
                    [0.04, 0.10, 0.82, 0.04],
                    [0.02, 0.03, 0.05, 0.90]])
plot_attention_heatmap(weights, src, tgt, "Bahdanau Attention: French to English")
```

## Code 4 — Attention vs No-Attention BLEU vs Length

```python
import numpy as np
import matplotlib.pyplot as plt

def sim_bleu(base, decay, lengths, noise_std=0.5, seed=0):
    """Simulate BLEU scores that decay with sentence length."""
    np.random.seed(seed)
    scores = []
    for L in lengths:
        s = base * np.exp(-decay * max(L - 10, 0)) + np.random.randn() * noise_std
        scores.append(max(round(s, 2), 1.0))
    return scores

lengths = list(range(5, 55, 5))
no_attn  = sim_bleu(28.0, 0.040, lengths, seed=1)
bahdanau = sim_bleu(30.5, 0.012, lengths, seed=2)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(lengths, no_attn,  'r--o', label='Seq2Seq (no attention)', linewidth=2)
ax.plot(lengths, bahdanau, 'b-s',  label='Seq2Seq + Bahdanau',    linewidth=2)
ax.fill_between(lengths, no_attn, bahdanau, alpha=0.15, color='blue')
ax.set_xlabel('Source Sentence Length (tokens)', fontsize=12)
ax.set_ylabel('BLEU Score', fontsize=12)
ax.set_title('BLEU vs Sentence Length: Attention vs No-Attention', fontsize=13)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.annotate('attention gap widens\nwith length', xy=(38, 15),
            fontsize=10, color='blue', style='italic')
plt.tight_layout()
plt.savefig('bleu_vs_length.png', dpi=150)
plt.show()
print("Attention advantage grows from ~2 BLEU at L=10 to ~8 BLEU at L=50.")
```

## Hard Attention vs Soft Attention

Bahdanau's original attention is soft attention: the context vector is a differentiable weighted sum over all encoder positions, enabling end-to-end backpropagation. Hard attention (Xu et al., 2015, for image captioning) samples a single position stochastically rather than computing a weighted average. Hard attention requires REINFORCE-style policy gradient training, is non-differentiable, and produces sparser — sometimes more interpretable — selections. Most subsequent work defaults to soft attention due to its training simplicity and better optimization landscape.

> **Attention as Memory Retrieval**: Attention can be viewed as soft key-value retrieval: the decoder hidden state acts as a query Q, encoder hidden states act as keys K, and encoder outputs act as values V. The alignment score computes query-key compatibility, softmax normalizes into a probability, and the context vector is the weighted value sum. This query-key-value framing directly inspired the Transformer's scaled dot-product attention — replace the additive score with qᵀk / sqrt(d_k) and remove the RNN.

## From Bahdanau to Transformer Attention

Bahdanau attention established the conceptual template that scaled into the Transformer. Three key evolutions: (1) additive scoring replaced by scaled dot-product eᵢⱼ = qⱼᵀkᵢ / √d_k for computational efficiency on modern hardware; (2) the RNN backbone removed entirely — self-attention replaced recurrence, enabling O(1) depth for any pairwise interaction and full parallelism over the sequence; (3) multi-head attention applies multiple attention functions in parallel, each learning different aspects of alignment. The gradient-flow advantage — direct paths from any decoder position to any encoder position — is preserved across all variants.

| Variant | Score Formula | Complexity | Uses RNN | Original Paper |
| --- | --- | --- | --- | --- |
| Bahdanau (additive) | vᵀ tanh(W₁s + W₂h) | O(T²·d) | Yes (biGRU) | Bahdanau 2015 |
| Luong dot | sᵀh | O(T²) | Yes (LSTM) | Luong 2015 |
| Luong general | sᵀWh | O(T²·d) | Yes (LSTM) | Luong 2015 |
| Luong concat | vᵀ tanh(W[s;h]) | O(T²·d) | Yes (LSTM) | Luong 2015 |
| Scaled dot-product | qᵀk / √d_k | O(T²) | No | Vaswani 2017 |

Bahdanau attention has aged remarkably well. Its core intuition — that decoding should be conditioned on a content-specific weighted combination of encoder representations rather than a fixed summary — proved fundamental. Every modern sequence model inherits this idea: BERT's bidirectional self-attention, GPT's causal self-attention, cross-attention in diffusion and speech models. The alignment visualization also foreshadowed modern explainability: attention weight analysis remains a primary tool for understanding what sequence models have learned.

- O(Ts × Tt) cost is affordable for sentence-level sequences (T < 200)
- Bidirectional encoder hidden states hᵢ capture local context from both directions
- Direct gradient path from loss to each encoder state — no bottleneck vanishing gradient
- Alignment matrix is interpretable: near-diagonal for similar-order languages
- Foundation for self-attention: when Q=K=V all come from the same sequence

