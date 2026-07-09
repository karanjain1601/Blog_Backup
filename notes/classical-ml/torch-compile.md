---
title: "torch.compile — Dynamo Tracing and Inductor Code Generation"
slug: "torch-compile"
description: "torch.compile wraps Python model code in three optimization stages — Dynamo bytecode analysis, AOT Autograd, and Inductor kernel generation — delivering 1.5–4x speedup with one line of code."
tags: ["pytorch", "tools", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoidG9yY2guY29tcGlsZSAoUHlUb3JjaCAyLjArKSB0cmFuc2Zvcm1zIGVhZ2VyIFB5dGhvbiBtb2RlbCBjb2RlIGludG8gb3B0aW1pemVkIGNvbXBpbGVkIGtlcm5lbHMgd2l0aG91dCByZXF1aXJpbmcgbW9kZWwgcmV3cml0ZXMuIEEgc2luZ2xlIGRlY29yYXRvciDigJQgQHRvcmNoLmNvbXBpbGUgb3IgdG9yY2guY29tcGlsZShtb2RlbCkg4oCUIHRyaWdnZXJzIHRocmVlIGNvbXBpbGF0aW9uIHN0YWdlcyB0aGF0IGZ1c2Ugb3BlcmF0b3JzLCBlbGltaW5hdGUgUHl0aG9uIG92ZXJoZWFkLCBhbmQgZ2VuZXJhdGUgaGFyZHdhcmUtb3B0aW1pemVkIENVREEvVHJpdG9uIG9yIEMrKyBjb2RlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRocmVlIENvbXBpbGF0aW9uIFN0YWdlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVW5kZXJzdGFuZGluZyBlYWNoIHN0YWdlIGNsYXJpZmllcyB3aGF0IHRvcmNoLmNvbXBpbGUgY2FuIGFuZCBjYW5ub3Qgb3B0aW1pemUsIGFuZCB3aHkgZ3JhcGggYnJlYWtzIG9jY3VyLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3RhZ2UgMSDigJQgVG9yY2hEeW5hbW86IFB5dGhvbiBieXRlY29kZSBhbmFseXNpczsgaWRlbnRpZmllcyBjb21waWxhYmxlIHN1YmdyYXBoczsgZ2VuZXJhdGVzIGFuIEZYIGdyYXBoOyBjcmVhdGVzIGEgZ3JhcGggYnJlYWsgd2hlbiBQeXRob24gY29udHJvbCBmbG93IG9yIHNpZGUgZWZmZWN0cyBwcmV2ZW50IHRyYWNpbmciLCJTdGFnZSAyIOKAlCBBT1QgQXV0b2dyYWQ6IGNhcHR1cmVzIHRoZSBiYWNrd2FyZCBncmFwaCBhaGVhZCBvZiB0aW1lIChub3QgbGF6aWx5IGF0IGJhY2t3YXJkKCkgY2FsbCk7IGZ1c2VzIGZvcndhcmQgYW5kIGJhY2t3YXJkIGludG8gYSBzaW5nbGUgY29tcGlsZWQgYXJ0aWZhY3QiLCJTdGFnZSAzIOKAlCBUb3JjaEluZHVjdG9yOiB0YWtlcyB0aGUgRlggZ3JhcGggYW5kIGdlbmVyYXRlcyBvcHRpbWl6ZWQgQysrL09wZW5NUCAoQ1BVKSBvciBUcml0b24gKENVREEpIGtlcm5lbHM7IHBlcmZvcm1zIG9wZXJhdG9yIGZ1c2lvbiwgbWVtb3J5IGxheW91dCBvcHRpbWl6YXRpb24sIGFuZCBsb29wIG9yZGVyaW5nIiwiR3JhcGggYnJlYWtzOiBwb2ludHMgd2hlcmUgRHluYW1vIGdpdmVzIHVwIGFuZCBmYWxscyBiYWNrIHRvIGVhZ2VyIOKAlCBjb21tb24gY2F1c2VzOiBQeXRob24gcHJpbnQsIGRhdGEtZGVwZW5kZW50IHNoYXBlcywgdW5zdXBwb3J0ZWQgUHl0aG9uIGJ1aWx0aW5zIiwiQ29tcGlsYXRpb24gb3ZlcmhlYWQ6IGZpcnN0IGZvcndhcmQgcGFzcyB0cmlnZ2VycyBKSVQgY29tcGlsYXRpb24gKHNlY29uZHMpOyBzdWJzZXF1ZW50IGNhbGxzIHVzZSB0aGUgY29tcGlsZWQga2VybmVsIChjYWNoZWQpIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhc2ljIFVzYWdlIGFuZCBTcGVlZHVwIE1lYXN1cmVtZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJ0b3JjaC5jb21waWxlIHdyYXBzIGFueSBjYWxsYWJsZSDigJQgYSBtb2RlbCwgYSBmdW5jdGlvbiwgZXZlbiBhIHRyYWluaW5nIHN0ZXAuIFRoZSBBUEkgaXMgYSBzaW5nbGUgZnVuY3Rpb24gY2FsbCB3aXRoIG5vIG1vZGVsIG1vZGlmaWNhdGlvbnMgcmVxdWlyZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdGltZVxuXG5jbGFzcyBEZWVwTUxQKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbTogaW50ID0gNTEyLCBkZXB0aDogaW50ID0gOCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBsYXllcnMgPSBbXVxuICAgICAgICBmb3IgXyBpbiByYW5nZShkZXB0aCk6XG4gICAgICAgICAgICBsYXllcnMgKz0gW25uLkxpbmVhcihkaW0sIGRpbSksIG5uLkxheWVyTm9ybShkaW0pLCBubi5HRUxVKCldXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuICAgICAgICBzZWxmLmhlYWQgPSBubi5MaW5lYXIoZGltLCAxMClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIHJldHVybiBzZWxmLmhlYWQoc2VsZi5uZXQoeCkpXG5cbmRldmljZSA9IFx1MDAyN2N1ZGFcdTAwMjcgaWYgdG9yY2guY3VkYS5pc19hdmFpbGFibGUoKSBlbHNlIFx1MDAyN2NwdVx1MDAyN1xubW9kZWxfZWFnZXIgICA9IERlZXBNTFAoKS50byhkZXZpY2UpXG5tb2RlbF9jb21waWxlZCA9IHRvcmNoLmNvbXBpbGUobW9kZWxfZWFnZXIsIG1vZGU9XHUwMDI3ZGVmYXVsdFx1MDAyNylcblxueCA9IHRvcmNoLnJhbmRuKDI1NiwgNTEyLCBkZXZpY2U9ZGV2aWNlKVxuXG4jIFdhcm0gdXAgYm90aCAoY29tcGlsZWQgbW9kZWwgSklULWNvbXBpbGVzIG9uIGZpcnN0IGNhbGwpXG5mb3IgXyBpbiByYW5nZSgzKTpcbiAgICBfID0gbW9kZWxfZWFnZXIoeClcbiAgICBfID0gbW9kZWxfY29tcGlsZWQoeClcblxuaWYgZGV2aWNlID09IFx1MDAyN2N1ZGFcdTAwMjc6XG4gICAgdG9yY2guY3VkYS5zeW5jaHJvbml6ZSgpXG5cbnQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuZm9yIF8gaW4gcmFuZ2UoMTAwKTpcbiAgICBfID0gbW9kZWxfZWFnZXIoeClcbmlmIGRldmljZSA9PSBcdTAwMjdjdWRhXHUwMDI3OiB0b3JjaC5jdWRhLnN5bmNocm9uaXplKClcbmVhZ2VyX3QgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gdDBcblxudDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG5mb3IgXyBpbiByYW5nZSgxMDApOlxuICAgIF8gPSBtb2RlbF9jb21waWxlZCh4KVxuaWYgZGV2aWNlID09IFx1MDAyN2N1ZGFcdTAwMjc6IHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuY29tcGlsZWRfdCA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuXG5wcmludChmXHUwMDI3RWFnZXI6ICAgIHtlYWdlcl90KjEwOi4yZn0gbXMvaXRlclx1MDAyNylcbnByaW50KGZcdTAwMjdDb21waWxlZDoge2NvbXBpbGVkX3QqMTA6LjJmfSBtcy9pdGVyXHUwMDI3KVxucHJpbnQoZlx1MDAyN1NwZWVkdXA6ICB7ZWFnZXJfdC9jb21waWxlZF90Oi4yZn14XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBpbGF0aW9uIE1vZGVzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGUiLCJDb21waWxlIFRpbWUiLCJSdW50aW1lIFNwZWVkdXAiLCJCZXN0IEZvciIsIkdyYXBoIEJyZWFrIEhhbmRsaW5nIl0sInJvd3MiOltbImRlZmF1bHQiLCJTZWNvbmRzIiwiMS414oCTMnggdHlwaWNhbCIsIkJhbGFuY2VkIOKAlCBmaXJzdCBjaG9pY2UiLCJBbGxvd2VkIOKAlCBmYWxscyBiYWNrIHRvIGVhZ2VyIl0sWyJyZWR1Y2Utb3ZlcmhlYWQiLCJMb25nZXIiLCIy4oCTM3ggKENVREEgZ3JhcGhzKSIsIkluZmVyZW5jZSB3aXRoIGZpeGVkIHNoYXBlcyIsIkFsbG93ZWQg4oCUIENVREEgZ3JhcGggY2FwdHVyZXMgZW50aXJlIGxvb3AiXSxbIm1heC1hdXRvdHVuZSIsIk1pbnV0ZXMiLCIy4oCTNHggcG90ZW50aWFsIiwiUHJvZHVjdGlvbiBzZXJ2aW5nIOKAlCBmaXhlZCBzaGFwZXMiLCJNaW5pbWFsIOKAlCBtYXhpbWl6ZXMgZnVzaW9uIl0sWyJlYWdlciAobm8gY29tcGlsZSkiLCJOb25lIiwiMXggYmFzZWxpbmUiLCJEZWJ1Z2dpbmcgZ3JhcGggYnJlYWtzIiwiTi9BIOKAlCBydW5zIGluIFB5dGhvbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVW5kZXJzdGFuZGluZyBHcmFwaCBCcmVha3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgZ3JhcGggYnJlYWsgb2NjdXJzIHdoZW4gRHluYW1vIGVuY291bnRlcnMgUHl0aG9uIGNvZGUgaXQgY2Fubm90IHRyYWNlIHN5bWJvbGljYWxseSDigJQgdHlwaWNhbGx5IGRhdGEtZGVwZW5kZW50IGNvbnRyb2wgZmxvdywgUHl0aG9uIHNpZGUgZWZmZWN0cywgb3IgdW5zdXBwb3J0ZWQgb3BlcmF0aW9ucy4gRWFjaCBncmFwaCBicmVhayBhZGRzIG92ZXJoZWFkIGFuZCByZWR1Y2VzIHRoZSBvcHRpbWl6YXRpb24gc2NvcGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLl9keW5hbW8gYXMgZHluYW1vXG5cbiMgTW9kZWwgd2l0aCBhIGdyYXBoIGJyZWFrIChwcmludCBpcyBhIHNpZGUgZWZmZWN0KVxuY2xhc3MgQnJlYWtpbmdNb2RlbCh0b3JjaC5ubi5Nb2R1bGUpOlxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIHggPSB0b3JjaC5yZWx1KHgpXG4gICAgICAgIHByaW50KGZcdTAwMjdTaGFwZToge3guc2hhcGV9XHUwMDI3KSAgIyBcdTAwM2MtLSBncmFwaCBicmVhayEgcHJpbnQgaXMgYSBQeXRob24gc2lkZSBlZmZlY3RcbiAgICAgICAgcmV0dXJuIHggKiAyXG5cbiMgRXhwbGFpbiBncmFwaCBicmVha3Mgd2l0aG91dCBhY3R1YWxseSBjb21waWxpbmdcbm1vZGVsID0gQnJlYWtpbmdNb2RlbCgpXG5leHBsYW5hdGlvbiA9IGR5bmFtby5leHBsYWluKG1vZGVsKSh0b3JjaC5yYW5kbig0LCA4KSlcbnByaW50KGZcdTAwMjdOdW1iZXIgb2YgZ3JhcGhzOiB7ZXhwbGFuYXRpb24uZ3JhcGhfY291bnR9XHUwMDI3KVxucHJpbnQoZlx1MDAyN051bWJlciBvZiBicmVha3M6IHtleHBsYW5hdGlvbi5icmVha19yZWFzb25zfVx1MDAyNylcblxuIyBGaXhlZCBtb2RlbCDigJQgcmVtb3ZlIHByaW50LCB1c2UgVGVuc29yIG9wZXJhdGlvbnMgb25seVxuY2xhc3MgRml4ZWRNb2RlbCh0b3JjaC5ubi5Nb2R1bGUpOlxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIHggPSB0b3JjaC5yZWx1KHgpXG4gICAgICAgIHJldHVybiB4ICogMlxuXG5maXhlZF9jb21waWxlZCA9IHRvcmNoLmNvbXBpbGUoRml4ZWRNb2RlbCgpKVxub3V0ID0gZml4ZWRfY29tcGlsZWQodG9yY2gucmFuZG4oNCwgOCkpXG5wcmludChmXHUwMDI3T3V0cHV0IHNoYXBlOiB7b3V0LnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDVURBIEdyYXBoIENhcHR1cmUgd2l0aCByZWR1Y2Utb3ZlcmhlYWQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNVREEgZ3JhcGhzIGNhcHR1cmUgYW4gZW50aXJlIHNlcXVlbmNlIG9mIEdQVSBvcGVyYXRpb25zIGFuZCByZXBsYXkgdGhlbSB3aXRoIGEgc2luZ2xlIENQVSBsYXVuY2gg4oCUIGVsaW1pbmF0aW5nIHBlci1rZXJuZWwgQ1BVLUdQVSBzeW5jaHJvbml6YXRpb24gb3ZlcmhlYWQuIFRoZSByZWR1Y2Utb3ZlcmhlYWQgY29tcGlsZSBtb2RlIGRvZXMgdGhpcyBhdXRvbWF0aWNhbGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG4jIHJlZHVjZS1vdmVyaGVhZDogYmVzdCBmb3IgZml4ZWQtc2hhcGUgaW5mZXJlbmNlIChubyBkeW5hbWljIHNoYXBlcylcbm1vZGVsID0gbm4uU2VxdWVudGlhbChcbiAgICBubi5MaW5lYXIoNTEyLCAyNTYpLCBubi5HRUxVKCksXG4gICAgbm4uTGluZWFyKDI1NiwgMTI4KSwgbm4uR0VMVSgpLFxuICAgIG5uLkxpbmVhcigxMjgsIDEwKVxuKVxuXG5kZXZpY2UgPSBcdTAwMjdjdWRhXHUwMDI3IGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcdTAwMjdjcHVcdTAwMjdcbm1vZGVsID0gbW9kZWwudG8oZGV2aWNlKVxuXG4jIENvbXBpbGUgd2l0aCBDVURBIGdyYXBoIG1vZGVcbmNvbXBpbGVkID0gdG9yY2guY29tcGlsZShtb2RlbCwgbW9kZT1cdTAwMjdyZWR1Y2Utb3ZlcmhlYWRcdTAwMjcpXG5cbnggPSB0b3JjaC5yYW5kbig2NCwgNTEyLCBkZXZpY2U9ZGV2aWNlKVxuXG4jIEZpcnN0IGZldyBjYWxsczogd2FybSB1cCBhbmQgY2FwdHVyZSB0aGUgQ1VEQSBncmFwaFxuZm9yIF8gaW4gcmFuZ2UoNSk6XG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG91dCA9IGNvbXBpbGVkKHgpXG5cbmlmIGRldmljZSA9PSBcdTAwMjdjdWRhXHUwMDI3OlxuICAgIHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuICAgIHByaW50KGZcdTAwMjdHUFUgbWVtb3J5OiB7dG9yY2guY3VkYS5tZW1vcnlfYWxsb2NhdGVkKCkvMWU2Oi4xZn0gTUJcdTAwMjcpXG5cbiMgTm90ZTogaW5wdXQgc2hhcGUgbXVzdCBzdGF5IGZpeGVkIGZvciBDVURBIGdyYXBoIHRvIGJlIHZhbGlkXG4jIENoYW5naW5nIHguc2hhcGUgdHJpZ2dlcnMgcmVjb21waWxhdGlvblxucHJpbnQoZlx1MDAyN091dHB1dCBzaGFwZToge291dC5zaGFwZX1cdTAwMjcpXG5wcmludChcdTAwMjdDVURBIGdyYXBoIGNhcHR1cmVkIGFuZCByZWFkeSBmb3IgZmFzdCBpbmZlcmVuY2VcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVhc3VyaW5nIENvbXBpbGF0aW9uIE92ZXJoZWFkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJ0b3JjaC5jb21waWxlIGluY3VycyBhIG9uZS10aW1lIGNvbXBpbGF0aW9uIGNvc3Qgb24gdGhlIGZpcnN0IGNhbGwuIFN1YnNlcXVlbnQgY2FsbHMgYXJlIGZhc3QuIEZvciBzaG9ydC1ydW5uaW5nIHNjcmlwdHMsIHRoZSBjb21waWxlIG92ZXJoZWFkIGNhbiBvdXR3ZWlnaCB0aGUgcnVudGltZSBiZW5lZml0IOKAlCBjb21waWxlIGlzIHdvcnRoIGl0IG9ubHkgd2hlbiB0aGUgY29tcGlsZWQga2VybmVsIHdpbGwgYmUgY2FsbGVkIG1hbnkgdGltZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdGltZVxuXG5tb2RlbCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uTGluZWFyKDI1NiwgNTEyKSwgbm4uR0VMVSgpLFxuICAgIG5uLkxpbmVhcig1MTIsIDI1NiksIG5uLkdFTFUoKSxcbiAgICBubi5MaW5lYXIoMjU2LCAxMClcbilcbmRldmljZSA9IFx1MDAyN2N1ZGFcdTAwMjcgaWYgdG9yY2guY3VkYS5pc19hdmFpbGFibGUoKSBlbHNlIFx1MDAyN2NwdVx1MDAyN1xubW9kZWwgPSBtb2RlbC50byhkZXZpY2UpXG5jb21waWxlZCA9IHRvcmNoLmNvbXBpbGUobW9kZWwsIG1vZGU9XHUwMDI3ZGVmYXVsdFx1MDAyNylcblxueCA9IHRvcmNoLnJhbmRuKDEyOCwgMjU2LCBkZXZpY2U9ZGV2aWNlKVxuXG4jIEZpcnN0IGNhbGw6IHRyaWdnZXJzIGNvbXBpbGF0aW9uIChleHBlbnNpdmUpXG50MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIF8gPSBjb21waWxlZCh4KVxuaWYgZGV2aWNlID09IFx1MDAyN2N1ZGFcdTAwMjc6IHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuZmlyc3RfY2FsbF90ID0gdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwXG5cbiMgU3Vic2VxdWVudCBjYWxsczogdXNlIGNhY2hlZCBjb21waWxlZCBrZXJuZWxcbnRpbWVzID0gW11cbmZvciBfIGluIHJhbmdlKDUwKTpcbiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgXyA9IGNvbXBpbGVkKHgpXG4gICAgaWYgZGV2aWNlID09IFx1MDAyN2N1ZGFcdTAwMjc6IHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuICAgIHRpbWVzLmFwcGVuZCh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApXG5cbnByaW50KGZcdTAwMjdGaXJzdCBjYWxsIChjb21waWxlKToge2ZpcnN0X2NhbGxfdCoxMDAwOi4xZn0gbXNcdTAwMjcpXG5wcmludChmXHUwMDI3U3Vic2VxdWVudCBhdmc6ICAgICAgIHtzdW0odGltZXMpL2xlbih0aW1lcykqMTAwMDouMmZ9IG1zXHUwMDI3KVxucHJpbnQoZlx1MDAyN0JyZWFrLWV2ZW4gYXQ6ICAgICAgICB7aW50KGZpcnN0X2NhbGxfdCAvIChzdW0odGltZXMpL2xlbih0aW1lcykpKX0gaW5mZXJlbmNlIGNhbGxzXHUwMDI3KSJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoZW4gdG9yY2guY29tcGlsZSBIZWxwcyBNb3N0IiwiY29udGVudCI6InRvcmNoLmNvbXBpbGUgZGVsaXZlcnMgdGhlIGxhcmdlc3Qgc3BlZWR1cHMgZm9yICgxKSBtb2RlbHMgd2l0aCBtYW55IHNtYWxsIG9wZXJhdGlvbnMgdGhhdCBiZW5lZml0IGZyb20gZnVzaW9uIChUcmFuc2Zvcm1lcnMsIGF0dGVudGlvbiksICgyKSB0cmFpbmluZyBsb29wcyB3aGVyZSBBT1QgQXV0b2dyYWQgZnVzZXMgZm9yd2FyZCtiYWNrd2FyZCBpbnRvIG9uZSBrZXJuZWwgc2VxdWVuY2UsIGFuZCAoMykgbW9kZWxzIHJ1bm5pbmcgb24gQTEwMC9IMTAwIEdQVXMgd2l0aCBUcml0b24tY29tcGF0aWJsZSBvcGVyYXRpb25zLiBTbWFsbCBtb2RlbHMgb24gQ1BVIG1heSBzZWUgbmVnbGlnaWJsZSBvciBuZWdhdGl2ZSBzcGVlZHVwIGR1ZSB0byBjb21waWxhdGlvbiBvdmVyaGVhZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJ0b3JjaC5jb21waWxlIGhhcyB0aHJlZSBzdGFnZXM6IER5bmFtbyAoUHl0aG9uIHRyYWNlIOKGkiBGWCBncmFwaCksIEFPVCBBdXRvZ3JhZCAoZnVzZWQgZm9yd2FyZCtiYWNrd2FyZCksIEluZHVjdG9yIChUcml0b24vQysrIGtlcm5lbHMpIiwiR3JhcGggYnJlYWtzIHJlZHVjZSBvcHRpbWl6YXRpb24gc2NvcGUg4oCUIGF2b2lkIFB5dGhvbiBwcmludCwgZGF0YS1kZXBlbmRlbnQgc2hhcGVzLCBhbmQgc2lkZSBlZmZlY3RzIGluIGNvbXBpbGVkIGNvZGUiLCJkZWZhdWx0IG1vZGU6IGJhbGFuY2VkIGZpcnN0IGNob2ljZTsgcmVkdWNlLW92ZXJoZWFkOiBDVURBIGdyYXBocyBmb3IgZml4ZWQtc2hhcGUgaW5mZXJlbmNlOyBtYXgtYXV0b3R1bmU6IHR1bmVkIGtlcm5lbHMgZm9yIHByb2R1Y3Rpb24iLCJGaXJzdCBmb3J3YXJkIHBhc3MgaXMgc2xvdyAoSklUIGNvbXBpbGF0aW9uKTsgc3Vic2VxdWVudCBjYWxscyB1c2UgdGhlIGNhY2hlZCBjb21waWxlZCBrZXJuZWwiLCJVc2UgdG9yY2guX2R5bmFtby5leHBsYWluKG1vZGVsKSh4KSB0byBkaWFnbm9zZSBncmFwaCBicmVha3MgYmVmb3JlIG9wdGltaXppbmciXX1d"
---
# torch.compile — Dynamo Tracing and Inductor Code Generation

torch.compile (PyTorch 2.0+) transforms eager Python model code into optimized compiled kernels without requiring model rewrites. A single decorator — @torch.compile or torch.compile(model) — triggers three compilation stages that fuse operators, eliminate Python overhead, and generate hardware-optimized CUDA/Triton or C++ code.

## Three Compilation Stages

Understanding each stage clarifies what torch.compile can and cannot optimize, and why graph breaks occur.

- Stage 1 — TorchDynamo: Python bytecode analysis; identifies compilable subgraphs; generates an FX graph; creates a graph break when Python control flow or side effects prevent tracing
- Stage 2 — AOT Autograd: captures the backward graph ahead of time (not lazily at backward() call); fuses forward and backward into a single compiled artifact
- Stage 3 — TorchInductor: takes the FX graph and generates optimized C++/OpenMP (CPU) or Triton (CUDA) kernels; performs operator fusion, memory layout optimization, and loop ordering
- Graph breaks: points where Dynamo gives up and falls back to eager — common causes: Python print, data-dependent shapes, unsupported Python builtins
- Compilation overhead: first forward pass triggers JIT compilation (seconds); subsequent calls use the compiled kernel (cached)

## Basic Usage and Speedup Measurement

torch.compile wraps any callable — a model, a function, even a training step. The API is a single function call with no model modifications required.

```python
import torch
import torch.nn as nn
import time

class DeepMLP(nn.Module):
    def __init__(self, dim: int = 512, depth: int = 8):
        super().__init__()
        layers = []
        for _ in range(depth):
            layers += [nn.Linear(dim, dim), nn.LayerNorm(dim), nn.GELU()]
        self.net = nn.Sequential(*layers)
        self.head = nn.Linear(dim, 10)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.head(self.net(x))

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_eager   = DeepMLP().to(device)
model_compiled = torch.compile(model_eager, mode='default')

x = torch.randn(256, 512, device=device)

# Warm up both (compiled model JIT-compiles on first call)
for _ in range(3):
    _ = model_eager(x)
    _ = model_compiled(x)

if device == 'cuda':
    torch.cuda.synchronize()

t0 = time.perf_counter()
for _ in range(100):
    _ = model_eager(x)
if device == 'cuda': torch.cuda.synchronize()
eager_t = time.perf_counter() - t0

t0 = time.perf_counter()
for _ in range(100):
    _ = model_compiled(x)
if device == 'cuda': torch.cuda.synchronize()
compiled_t = time.perf_counter() - t0

print(f'Eager:    {eager_t*10:.2f} ms/iter')
print(f'Compiled: {compiled_t*10:.2f} ms/iter')
print(f'Speedup:  {eager_t/compiled_t:.2f}x')
```

## Compilation Modes

| Mode | Compile Time | Runtime Speedup | Best For | Graph Break Handling |
| --- | --- | --- | --- | --- |
| default | Seconds | 1.5–2x typical | Balanced — first choice | Allowed — falls back to eager |
| reduce-overhead | Longer | 2–3x (CUDA graphs) | Inference with fixed shapes | Allowed — CUDA graph captures entire loop |
| max-autotune | Minutes | 2–4x potential | Production serving — fixed shapes | Minimal — maximizes fusion |
| eager (no compile) | None | 1x baseline | Debugging graph breaks | N/A — runs in Python |

## Understanding Graph Breaks

A graph break occurs when Dynamo encounters Python code it cannot trace symbolically — typically data-dependent control flow, Python side effects, or unsupported operations. Each graph break adds overhead and reduces the optimization scope.

```python
import torch
import torch._dynamo as dynamo

# Model with a graph break (print is a side effect)
class BreakingModel(torch.nn.Module):
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(x)
        print(f'Shape: {x.shape}')  # <-- graph break! print is a Python side effect
        return x * 2

# Explain graph breaks without actually compiling
model = BreakingModel()
explanation = dynamo.explain(model)(torch.randn(4, 8))
print(f'Number of graphs: {explanation.graph_count}')
print(f'Number of breaks: {explanation.break_reasons}')

# Fixed model — remove print, use Tensor operations only
class FixedModel(torch.nn.Module):
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(x)
        return x * 2

fixed_compiled = torch.compile(FixedModel())
out = fixed_compiled(torch.randn(4, 8))
print(f'Output shape: {out.shape}')
```

## CUDA Graph Capture with reduce-overhead

CUDA graphs capture an entire sequence of GPU operations and replay them with a single CPU launch — eliminating per-kernel CPU-GPU synchronization overhead. The reduce-overhead compile mode does this automatically.

```python
import torch
import torch.nn as nn

# reduce-overhead: best for fixed-shape inference (no dynamic shapes)
model = nn.Sequential(
    nn.Linear(512, 256), nn.GELU(),
    nn.Linear(256, 128), nn.GELU(),
    nn.Linear(128, 10)
)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)

# Compile with CUDA graph mode
compiled = torch.compile(model, mode='reduce-overhead')

x = torch.randn(64, 512, device=device)

# First few calls: warm up and capture the CUDA graph
for _ in range(5):
    with torch.no_grad():
        out = compiled(x)

if device == 'cuda':
    torch.cuda.synchronize()
    print(f'GPU memory: {torch.cuda.memory_allocated()/1e6:.1f} MB')

# Note: input shape must stay fixed for CUDA graph to be valid
# Changing x.shape triggers recompilation
print(f'Output shape: {out.shape}')
print('CUDA graph captured and ready for fast inference')
```

## Measuring Compilation Overhead

torch.compile incurs a one-time compilation cost on the first call. Subsequent calls are fast. For short-running scripts, the compile overhead can outweigh the runtime benefit — compile is worth it only when the compiled kernel will be called many times.

```python
import torch
import torch.nn as nn
import time

model = nn.Sequential(
    nn.Linear(256, 512), nn.GELU(),
    nn.Linear(512, 256), nn.GELU(),
    nn.Linear(256, 10)
)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)
compiled = torch.compile(model, mode='default')

x = torch.randn(128, 256, device=device)

# First call: triggers compilation (expensive)
t0 = time.perf_counter()
with torch.no_grad():
    _ = compiled(x)
if device == 'cuda': torch.cuda.synchronize()
first_call_t = time.perf_counter() - t0

# Subsequent calls: use cached compiled kernel
times = []
for _ in range(50):
    t0 = time.perf_counter()
    with torch.no_grad():
        _ = compiled(x)
    if device == 'cuda': torch.cuda.synchronize()
    times.append(time.perf_counter() - t0)

print(f'First call (compile): {first_call_t*1000:.1f} ms')
print(f'Subsequent avg:       {sum(times)/len(times)*1000:.2f} ms')
print(f'Break-even at:        {int(first_call_t / (sum(times)/len(times)))} inference calls')
```

---

> **When torch.compile Helps Most**: torch.compile delivers the largest speedups for (1) models with many small operations that benefit from fusion (Transformers, attention), (2) training loops where AOT Autograd fuses forward+backward into one kernel sequence, and (3) models running on A100/H100 GPUs with Triton-compatible operations. Small models on CPU may see negligible or negative speedup due to compilation overhead.

## Key Takeaways

- torch.compile has three stages: Dynamo (Python trace → FX graph), AOT Autograd (fused forward+backward), Inductor (Triton/C++ kernels)
- Graph breaks reduce optimization scope — avoid Python print, data-dependent shapes, and side effects in compiled code
- default mode: balanced first choice; reduce-overhead: CUDA graphs for fixed-shape inference; max-autotune: tuned kernels for production
- First forward pass is slow (JIT compilation); subsequent calls use the cached compiled kernel
- Use torch._dynamo.explain(model)(x) to diagnose graph breaks before optimizing

