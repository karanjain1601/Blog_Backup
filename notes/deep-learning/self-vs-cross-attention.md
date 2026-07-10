---
title: "Self-Attention vs Cross-Attention — Encoder and Decoder Patterns"
slug: "self-vs-cross-attention"
description: "Contrast self-attention (Q=K=V from same sequence) with cross-attention (Q from decoder, K/V from encoder), implement both from scratch, and trace their roles in BERT, GPT, T5, and diffusion models."
tags: ["deep-learning", "transformers", "attention"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXR0ZW50aW9uIG1lY2hhbmlzbXMgZGlmZmVyIGZ1bmRhbWVudGFsbHkgaW4gd2hlcmUgdGhlaXIgUSwgSywgYW5kIFYgaW5wdXRzIGNvbWUgZnJvbS4gU2VsZi1hdHRlbnRpb24gdGFrZXMgYWxsIHRocmVlIGZyb20gdGhlIHNhbWUgc2VxdWVuY2UsIGFsbG93aW5nIGVhY2ggcG9zaXRpb24gdG8gYXR0ZW5kIHRvIGV2ZXJ5IG90aGVyIHBvc2l0aW9uIGluIHRoYXQgc2FtZSBzZXF1ZW5jZS4gQ3Jvc3MtYXR0ZW50aW9uIHRha2VzIFEgZnJvbSBvbmUgc2VxdWVuY2UgYW5kIEssIFYgZnJvbSBhIGRpZmZlcmVudCBzZXF1ZW5jZSwgYnJpZGdpbmcgaW5mb3JtYXRpb24gYmV0d2VlbiB0d28gc2VwYXJhdGUgcmVwcmVzZW50YXRpb25zLiBUaGVzZSB0d28gdmFyaWFudHMgYXJlIG5vdCBpbnRlcmNoYW5nZWFibGUg4oCUIGVhY2ggaXMgdXNlZCBpbiBzcGVjaWZpYyBhcmNoaXRlY3R1cmFsIHBvc2l0aW9ucyB3aXRoIHNwZWNpZmljIGNvbXB1dGF0aW9uYWwgcHVycG9zZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VsZi1BdHRlbnRpb24g4oCUIERlZmluaXRpb24gYW5kIFByb3BlcnRpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIHNlbGYtYXR0ZW50aW9uIFEgPSBYwrdXUSwgSyA9IFjCt1dLLCBWID0gWMK3V1Ygd2hlcmUgWCBpcyB0aGUgc2FtZSBpbnB1dCBzZXF1ZW5jZS4gRXZlcnkgcG9zaXRpb24gcHJvZHVjZXMgYSBxdWVyeSB0aGF0IGlzIHNjb3JlZCBhZ2FpbnN0IGtleXMgZnJvbSBhbGwgb3RoZXIgcG9zaXRpb25zIGluIFgg4oCUIHRoZSBhdHRlbnRpb24gbWF0cml4IEEg4oiIIOKEnV57bsOXbn0gaXMgc3F1YXJlLiBCaWRpcmVjdGlvbmFsIHNlbGYtYXR0ZW50aW9uIGFsbG93cyBlYWNoIHBvc2l0aW9uIHRvIGF0dGVuZCB0byBhbGwgb3RoZXJzIChpbmNsdWRpbmcgZnV0dXJlIHBvc2l0aW9ucyksIG1ha2luZyB0aGUgcmVwcmVzZW50YXRpb25zIGNvbnRleHQtYXdhcmUgaW4gYm90aCBkaXJlY3Rpb25zLiBDYXVzYWwgKG1hc2tlZCkgc2VsZi1hdHRlbnRpb24gYXBwbGllcyBhbiB1cHBlci10cmlhbmd1bGFyIG1hc2sgb2Yg4oiS4oieIHRvIHRoZSBzY29yZSBtYXRyaXggYmVmb3JlIHNvZnRtYXgsIHByZXZlbnRpbmcgcG9zaXRpb24gaSBmcm9tIGF0dGVuZGluZyB0byBwb3NpdGlvbnMgaiBcdTAwM2UgaS4gVGhpcyBwcmVzZXJ2ZXMgdGhlIGF1dG9yZWdyZXNzaXZlIHByb3BlcnR5IHJlcXVpcmVkIGZvciB0ZXh0IGdlbmVyYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc2VsZl9hdHRlbnRpb24oWCwgV19RLCBXX0ssIFdfViwgY2F1c2FsPUZhbHNlKTpcbiAgICAjIFg6IChuLCBkX21vZGVsKTsgUT1LPVYgYWxsIGRlcml2ZWQgZnJvbSBzYW1lIFhcbiAgICBRID0gWCBAIFdfUSAgICAjIChuLCBkaylcbiAgICBLID0gWCBAIFdfSyAgICAjIChuLCBkaylcbiAgICBWID0gWCBAIFdfViAgICAjIChuLCBkdilcbiAgICBkayA9IFEuc2hhcGVbLTFdXG4gICAgUyA9IFEgQCBLLlQgLyBucC5zcXJ0KGRrKSAgICAjIChuLCBuKSDigJQgc3F1YXJlIG1hdHJpeFxuICAgIGlmIGNhdXNhbDpcbiAgICAgICAgIyBVcHBlciB0cmlhbmdsZSAtXHUwMDNlIC1pbmYgc28gc29mdG1heCBnaXZlcyAwIHdlaWdodFxuICAgICAgICBtYXNrID0gbnAudHJpdShucC5vbmVzX2xpa2UoUyksIGs9MSkgKiAtMWU5XG4gICAgICAgIFMgPSBTICsgbWFza1xuICAgIFMgLT0gUy5tYXgoYXhpcz0tMSwga2VlcGRpbXM9VHJ1ZSlcbiAgICBBID0gbnAuZXhwKFMpOyBBIC89IEEuc3VtKGF4aXM9LTEsIGtlZXBkaW1zPVRydWUpXG4gICAgcmV0dXJuIEEgQCBWLCBBXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubiwgZF9tb2RlbCwgZGssIGR2ID0gNiwgNjQsIDMyLCAzMlxuWCA9IG5wLnJhbmRvbS5yYW5kbihuLCBkX21vZGVsKVxuV19RID0gbnAucmFuZG9tLnJhbmRuKGRfbW9kZWwsIGRrKSAqIDAuMVxuV19LID0gbnAucmFuZG9tLnJhbmRuKGRfbW9kZWwsIGRrKSAqIDAuMVxuV19WID0gbnAucmFuZG9tLnJhbmRuKGRfbW9kZWwsIGR2KSAqIDAuMVxuXG5fLCBBX2JpICA9IHNlbGZfYXR0ZW50aW9uKFgsIFdfUSwgV19LLCBXX1YsIGNhdXNhbD1GYWxzZSlcbl8sIEFfY2F1ID0gc2VsZl9hdHRlbnRpb24oWCwgV19RLCBXX0ssIFdfViwgY2F1c2FsPVRydWUpXG5wcmludChcdTAwMjdCaWRpcmVjdGlvbmFsIFNBIHNoYXBlOlx1MDAyNywgQV9iaS5zaGFwZSwgXHUwMDI3KG4geCBuLCBzcXVhcmUpXHUwMDI3KVxucHJpbnQoXHUwMDI3VXBwZXIgdHJpYW5nbGUgemVybyBpbiBjYXVzYWwgU0E6XHUwMDI3LCBucC5hbGxjbG9zZShucC50cml1KEFfY2F1LCAxKSwgMCkpXG5wcmludChcdTAwMjdDYXVzYWw6IHBvc2l0aW9uIDAgYXR0ZW5kcyBvbmx5IHRvIGl0c2VsZjpcdTAwMjcsIEFfY2F1WzBdLnJvdW5kKDQpKVxucHJpbnQoXHUwMDI3Q2F1c2FsOiBwb3NpdGlvbiA1IGF0dGVuZHMgdG8gYWxsIDY6XHUwMDI3LCAoQV9jYXVbNV0gXHUwMDNlIDFlLTYpLnN1bSgpLCBcdTAwMjdwb3NpdGlvbnNcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtQXR0ZW50aW9uIOKAlCBEZWZpbml0aW9uIGFuZCBQcm9wZXJ0aWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBjcm9zcy1hdHRlbnRpb24gdGhlIHF1ZXJ5IFEgY29tZXMgZnJvbSBvbmUgc2VxdWVuY2UgKGUuZy4sIGRlY29kZXIgc3RhdGVzKSB3aGlsZSBrZXlzIEsgYW5kIHZhbHVlcyBWIGNvbWUgZnJvbSBhIHNlY29uZCBzZXF1ZW5jZSAoZS5nLiwgZW5jb2RlciBvdXRwdXQpLiBRdWVyaWVzIGFuZCBrZXlzIG11c3Qgc2hhcmUgdGhlIHNhbWUgaW5uZXIgZGltZW5zaW9uIGTigpYgYnV0IHRoZSB0d28gc2VxdWVuY2VzIGNhbiBoYXZlIGRpZmZlcmVudCBsZW5ndGhzOiBucSDiiaAgbmsuIFRoZSBhdHRlbnRpb24gbWF0cml4IEEg4oiIIOKEnV57bnHDl25rfSBpcyByZWN0YW5ndWxhciDigJQgZWFjaCBvZiB0aGUgbnEgcXVlcnkgcG9zaXRpb25zIGF0dGVuZHMgb3ZlciBhbGwgbmsga2V5LXZhbHVlIHBvc2l0aW9ucy4gTm8gY2F1c2FsIG1hc2tpbmcgaXMgbmVlZGVkIChhbmQgbm9uZSBpcyBhcHBsaWVkKSBiZWNhdXNlIHRoZSBxdWVyeSBzZXF1ZW5jZSBpcyBhdHRlbmRpbmcgdG8gYSBmdWxseS1vYnNlcnZlZCBjb250ZXh0IHNlcXVlbmNlLCBub3QgdG8gaXRzIG93biBmdXR1cmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY3Jvc3NfYXR0ZW50aW9uKFFfc2VxLCBLVl9zZXEsIFdfUSwgV19LLCBXX1YpOlxuICAgICMgUV9zZXE6IChucSwgZF9xKSDigJQgZGVjb2RlciBzdGF0ZXM7IEtWX3NlcTogKG5rLCBkX2t2KSDigJQgZW5jb2RlciBvdXRwdXRcbiAgICBRID0gUV9zZXEgIEAgV19RICAgICMgKG5xLCBkaylcbiAgICBLID0gS1Zfc2VxIEAgV19LICAgICMgKG5rLCBkaylcbiAgICBWID0gS1Zfc2VxIEAgV19WICAgICMgKG5rLCBkdilcbiAgICBkayA9IFEuc2hhcGVbLTFdXG4gICAgUyA9IFEgQCBLLlQgLyBucC5zcXJ0KGRrKSAgICAjIChucSwgbmspIOKAlCBSRUNUQU5HVUxBUiwgbnEgIT0gbmtcbiAgICBTIC09IFMubWF4KGF4aXM9LTEsIGtlZXBkaW1zPVRydWUpXG4gICAgQSA9IG5wLmV4cChTKTsgQSAvPSBBLnN1bShheGlzPS0xLCBrZWVwZGltcz1UcnVlKVxuICAgIHJldHVybiBBIEAgViwgQSAgICAgICAgICAgICAgIyBvdXRwdXQ6IChucSwgZHYpLCB3ZWlnaHRzOiAobnEsIG5rKVxuXG5ucC5yYW5kb20uc2VlZCg3KVxubnEsIG5rLCBkX21vZGVsLCBkaywgZHYgPSA0LCAxMCwgNjQsIDMyLCAzMlxuZGVjX3N0YXRlcyA9IG5wLnJhbmRvbS5yYW5kbihucSwgZF9tb2RlbCkgICAjIHNob3J0IHRhcmdldCBzZXF1ZW5jZVxuZW5jX3N0YXRlcyAgPSBucC5yYW5kb20ucmFuZG4obmssIGRfbW9kZWwpICAjIGxvbmdlciBzb3VyY2Ugc2VxdWVuY2VcbldfUSA9IG5wLnJhbmRvbS5yYW5kbihkX21vZGVsLCBkaykgKiAwLjFcbldfSyA9IG5wLnJhbmRvbS5yYW5kbihkX21vZGVsLCBkaykgKiAwLjFcbldfViA9IG5wLnJhbmRvbS5yYW5kbihkX21vZGVsLCBkdikgKiAwLjFcblxub3V0LCBBID0gY3Jvc3NfYXR0ZW50aW9uKGRlY19zdGF0ZXMsIGVuY19zdGF0ZXMsIFdfUSwgV19LLCBXX1YpXG5wcmludChcdTAwMjdEZWMgc3RhdGVzOlx1MDAyNywgZGVjX3N0YXRlcy5zaGFwZSwgXHUwMDI3ICBFbmMgc3RhdGVzOlx1MDAyNywgZW5jX3N0YXRlcy5zaGFwZSlcbnByaW50KFx1MDAyN0F0dGVudGlvbiBtYXRyaXg6XHUwMDI3LCBBLnNoYXBlLCBcdTAwMjdcdTAwM2MtIHJlY3Rhbmd1bGFyIChucSB4IG5rKVx1MDAyNylcbnByaW50KFx1MDAyN091dHB1dDpcdTAwMjcsIG91dC5zaGFwZSlcbnByaW50KFx1MDAyN1JvdyBzdW1zIChzaG91bGQgYmUgMSk6XHUwMDI3LCBBLnN1bShheGlzPTEpLnJvdW5kKDUpKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiS2V5IERpZmZlcmVuY2Ug4oCUIFdoZXJlIFEsIEssIFYgQ29tZSBGcm9tIiwiY29udGVudCI6IlNlbGYtYXR0ZW50aW9uOiBRLCBLLCBWIGFsbCBmcm9tIHRoZSBzYW1lIHRlbnNvciBYIOKAlCB0aGUgYXR0ZW50aW9uIG1hdHJpeCBpcyBhbHdheXMgc3F1YXJlIChuw5duKS4gQ3Jvc3MtYXR0ZW50aW9uOiBRIGZyb20gc2VxdWVuY2UgQSwgSyBhbmQgViBmcm9tIHNlcXVlbmNlIEIg4oCUIHRoZSBhdHRlbnRpb24gbWF0cml4IGlzIHJlY3Rhbmd1bGFyIChuQcOXbkIpIGFuZCBuQSBjYW4gZGlmZmVyIGZyb20gbkIuIENvbmZ1c2luZyB0aGVzZSBjYXVzZXMgc2hhcGUgZXJyb3JzOiBpZiB5b3UgcGFzcyBhIGNyb3NzLWF0dGVudGlvbiBkZWNvZGVyIHF1ZXJ5IChucT04KSBhZ2FpbnN0IGVuY29kZXIga2V5cyAobms9MTAwKSBhbmQgZXhwZWN0IGEgc3F1YXJlIG1hdHJpeCwgeW91IHdpbGwgZ2V0IGEgKDjDlzEwMCkgbWF0cml4IOKAlCBjb3JyZWN0IGZvciBjcm9zcy1hdHRlbnRpb24sIG5vdCBmb3Igc2VsZi1hdHRlbnRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRW5jb2RlciBTZWxmLUF0dGVudGlvbiDigJQgQmlkaXJlY3Rpb25hbCBDb250ZXh0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmFuc2Zvcm1lciBlbmNvZGVycyAoQkVSVCwgUm9CRVJUYSwgVmlUKSB1c2UgYmlkaXJlY3Rpb25hbCBzZWxmLWF0dGVudGlvbiB0aHJvdWdob3V0LiBFdmVyeSB0b2tlbi9wYXRjaCBwb3NpdGlvbiBhdHRlbmRzIHRvIGV2ZXJ5IG90aGVyIHBvc2l0aW9uIGluIHRoZSBzYW1lIHNlcXVlbmNlIHdpdGggbm8gbWFza2luZy4gVGhpcyBhbGxvd3MgZWFjaCBwb3NpdGlvbiB0byBpbnRlZ3JhdGUgY29udGV4dCBmcm9tIGJvdGggaXRzIGxlZnQgYW5kIHJpZ2h0IG5laWdoYm91cnMgaW4gZXZlcnkgbGF5ZXIsIGJ1aWxkaW5nIHJlcHJlc2VudGF0aW9ucyB0aGF0IGFyZSBjb25kaXRpb25lZCBvbiB0aGUgZnVsbCBpbnB1dCBzZXF1ZW5jZS4gVGhlIGVuY29kZXIgb3V0cHV0IEgg4oiIIOKEnV57bsOXZF9tb2RlbH0gaXMgYSBjb250ZXh0dWFsaXNlZCByZXByZXNlbnRhdGlvbiBvZiBldmVyeSBpbnB1dCBwb3NpdGlvbiDigJQgaXQgaXMgdGhlbiBwYXNzZWQgYXMgdGhlIEsgYW5kIFYgc291cmNlIHRvIHRoZSBkZWNvZGVyXHUwMDI3cyBjcm9zcy1hdHRlbnRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVjb2RlciBBdHRlbnRpb24gUGF0dGVybnMg4oCUIENhdXNhbCBTZWxmICsgQ3Jvc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc3RhbmRhcmQgVHJhbnNmb3JtZXIgZGVjb2RlciAoVDUsIEJBUlQsIG9yaWdpbmFsIHNlcTJzZXEpIGNvbnRhaW5zIHR3byBhdHRlbnRpb24gc3ViLWxheWVycyBwZXIgYmxvY2suIEZpcnN0LCBjYXVzYWwgc2VsZi1hdHRlbnRpb246IHRoZSBkZWNvZGVyXHUwMDI3cyBvd24gZ2VuZXJhdGVkIHRva2VucyBhdHRlbmQgb25seSB0byBwcmV2aW91c2x5IGdlbmVyYXRlZCB0b2tlbnMgKHBvc2l0aW9ucyAwLi50LTEgZm9yIHBvc2l0aW9uIHQpLCBlbmZvcmNpbmcgYXV0b3JlZ3Jlc3NpdmUgbGVmdC10by1yaWdodCBnZW5lcmF0aW9uLiBTZWNvbmQsIGNyb3NzLWF0dGVudGlvbjogdGhlIGRlY29kZXIgcXVlcmllcyBhdHRlbmQgb3ZlciB0aGUgZnVsbCBlbmNvZGVyIG91dHB1dCB0byBwdWxsIGluIHNvdXJjZS1zZXF1ZW5jZSBpbmZvcm1hdGlvbi4gVGhpcyBjcm9zcy1hdHRlbnRpb24gaXMgdGhlIGluZm9ybWF0aW9uIGJyaWRnZSB0aGF0IHJlcGxhY2VkIHRoZSBSTk4gY29udGV4dCB2ZWN0b3IgaW4gcHJlLVRyYW5zZm9ybWVyIHNlcTJzZXEgbW9kZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBFbmNEZWNCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkLCBoLCBmZik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVuY19zYSAgID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGQsIGgsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZGVjX3NhICAgPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oZCwgaCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5kZWNfY2EgICA9IG5uLk11bHRpaGVhZEF0dGVudGlvbihkLCBoLCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLmVuY19mZiAgID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoZCwgZmYpLCBubi5SZUxVKCksIG5uLkxpbmVhcihmZiwgZCkpXG4gICAgICAgIHNlbGYuZGVjX2ZmICAgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkLCBmZiksIG5uLlJlTFUoKSwgbm4uTGluZWFyKGZmLCBkKSlcbiAgICAgICAgc2VsZi5ub3JtcyAgICA9IG5uLk1vZHVsZUxpc3QoW25uLkxheWVyTm9ybShkKSBmb3IgXyBpbiByYW5nZSg1KV0pXG5cbiAgICBkZWYgZW5jb2RlKHNlbGYsIHNyYyk6XG4gICAgICAgIGEsIF8gPSBzZWxmLmVuY19zYShzcmMsIHNyYywgc3JjKSAgICAgICAgICAgICAgIyBiaWRpcmVjdGlvbmFsIHNlbGYtYXR0blxuICAgICAgICB4ID0gc2VsZi5ub3Jtc1swXShzcmMgKyBhKVxuICAgICAgICByZXR1cm4gc2VsZi5ub3Jtc1sxXSh4ICsgc2VsZi5lbmNfZmYoeCkpXG5cbiAgICBkZWYgZGVjb2RlKHNlbGYsIHRndCwgZW5jX291dCwgY2F1c2FsX21hc2s9Tm9uZSk6XG4gICAgICAgIGEsIF8gPSBzZWxmLmRlY19zYSh0Z3QsIHRndCwgdGd0LCBhdHRuX21hc2s9Y2F1c2FsX21hc2spICAjIGNhdXNhbFxuICAgICAgICB4ID0gc2VsZi5ub3Jtc1syXSh0Z3QgKyBhKVxuICAgICAgICBhLCBjcm9zc193ID0gc2VsZi5kZWNfY2EoeCwgZW5jX291dCwgZW5jX291dCkgICAgICAgICAgICAgICMgY3Jvc3MtYXR0blxuICAgICAgICB4ID0gc2VsZi5ub3Jtc1szXSh4ICsgYSlcbiAgICAgICAgcmV0dXJuIHNlbGYubm9ybXNbNF0oeCArIHNlbGYuZGVjX2ZmKHgpKSwgY3Jvc3Nfd1xuXG50b3JjaC5tYW51YWxfc2VlZCgzKVxuZCwgaCwgZmYgPSAxMjgsIDQsIDI1NlxubW9kZWwgPSBFbmNEZWNCbG9jayhkLCBoLCBmZilcbnNyYyA9IHRvcmNoLnJhbmRuKDIsIDE1LCBkKSAgICMgYmF0Y2g9Miwgc3JjX2xlbj0xNVxudGd0ID0gdG9yY2gucmFuZG4oMiwgIDgsIGQpICAgIyBiYXRjaD0yLCB0Z3RfbGVuPThcbmVuY19vdXQgICAgICAgID0gbW9kZWwuZW5jb2RlKHNyYylcbmRlY19vdXQsIGNyb3NzX3cgPSBtb2RlbC5kZWNvZGUodGd0LCBlbmNfb3V0KVxucHJpbnQoXHUwMDI3RW5jb2RlciBvdXRwdXQ6XHUwMDI3LCB0dXBsZShlbmNfb3V0LnNoYXBlKSlcbnByaW50KFx1MDAyN0RlY29kZXIgb3V0cHV0Olx1MDAyNywgdHVwbGUoZGVjX291dC5zaGFwZSkpXG5wcmludChcdTAwMjdDcm9zcy1hdHRlbnRpb24gd2VpZ2h0czpcdTAwMjcsIHR1cGxlKGNyb3NzX3cuc2hhcGUpLCBcdTAwMjcoYmF0Y2ggeCB0Z3QgeCBzcmMpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNyb3NzLUF0dGVudGlvbiBBbGlnbm1lbnQgVmlzdWFsaXNhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gc2VxMnNlcSBtb2RlbHMsIHRoZSBjcm9zcy1hdHRlbnRpb24gd2VpZ2h0IG1hdHJpeCBpcyBhbiBhbGlnbm1lbnQ6IGVudHJ5IEFbaSxqXSBpcyBob3cgbXVjaCBkZWNvZGVyIHBvc2l0aW9uIGkgKHRhcmdldCB0b2tlbikgYXR0ZW5kcyB0byBlbmNvZGVyIHBvc2l0aW9uIGogKHNvdXJjZSB0b2tlbikuIEZvciB0cmFuc2xhdGlvbiwgdGhpcyByb3VnaGx5IHJlY292ZXJzIG1vbm90b25pYyBhbGlnbm1lbnQgZm9yIHNpbWlsYXItbGFuZ3VhZ2UgcGFpcnMgYW5kIHJlb3JkZXJpbmcgYWxpZ25tZW50IGZvciBkaXN0YW50LWxhbmd1YWdlIHBhaXJzLiBJbiBpbWFnZSBjYXB0aW9uaW5nLCBBW2ksal0gc2hvd3Mgd2hpY2ggaW1hZ2UgcGF0Y2ggZGVjb2RlciBzdGVwIGkgZm9jdXNlcyBvbiB3aGVuIGdlbmVyYXRpbmcgd29yZCBpLiBJbiB0ZXh0LXRvLXNwZWVjaCwgaXQgcHJvdmlkZXMgYSBzb2Z0IGFsaWdubWVudCBiZXR3ZWVuIHBob25lbWUgb3V0cHV0IGZyYW1lcyBhbmQgaW5wdXQgY2hhcmFjdGVyIHBvc2l0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBjcm9zc19hdHRuKGRlY19RLCBlbmNfS1YsIFdfUSwgV19LLCBXX1YpOlxuICAgIFEgPSBkZWNfUSBAIFdfUTsgSyA9IGVuY19LViBAIFdfSzsgViA9IGVuY19LViBAIFdfVlxuICAgIFMgPSBRIEAgSy5UIC8gbnAuc3FydChXX1Euc2hhcGVbMV0pXG4gICAgUyAtPSBTLm1heCgxLCBrZWVwZGltcz1UcnVlKVxuICAgIEEgPSBucC5leHAoUyk7IEEgLz0gQS5zdW0oMSwga2VlcGRpbXM9VHJ1ZSlcbiAgICByZXR1cm4gQSBAIFYsIEFcblxubnAucmFuZG9tLnNlZWQoMTEpXG5zcmNfdG9rID0gW1x1MDAyN0xlXHUwMDI3LCBcdTAwMjdjaGF0XHUwMDI3LCBcdTAwMjdlc3RcdTAwMjcsIFx1MDAyN2Fzc2lzXHUwMDI3LCBcdTAwMjdzdXJcdTAwMjcsIFx1MDAyN2xlXHUwMDI3LCBcdTAwMjd0YXBpc1x1MDAyNywgXHUwMDI3Llx1MDAyN11cbnRndF90b2sgPSBbXHUwMDI3VGhlXHUwMDI3LCBcdTAwMjdjYXRcdTAwMjcsIFx1MDAyN3NhdFx1MDAyNywgXHUwMDI3b25cdTAwMjcsIFx1MDAyN3RoZVx1MDAyNywgXHUwMDI3bWF0XHUwMDI3LCBcdTAwMjcuXHUwMDI3XVxubnEsIG5rLCBkLCBkayA9IGxlbih0Z3RfdG9rKSwgbGVuKHNyY190b2spLCAzMiwgMTZcbldfUSA9IG5wLnJhbmRvbS5yYW5kbihkLCBkaykgKiAwLjNcbldfSyA9IG5wLnJhbmRvbS5yYW5kbihkLCBkaykgKiAwLjNcbldfViA9IG5wLnJhbmRvbS5yYW5kbihkLCBkaykgKiAwLjNcbmRlY19zdGF0ZXMgPSBucC5yYW5kb20ucmFuZG4obnEsIGQpXG5lbmNfc3RhdGVzICA9IG5wLnJhbmRvbS5yYW5kbihuaywgZClcbl8sIEEgPSBjcm9zc19hdHRuKGRlY19zdGF0ZXMsIGVuY19zdGF0ZXMsIFdfUSwgV19LLCBXX1YpXG5cbmNvbF93ID0gbWF4KGxlbih0KSBmb3IgdCBpbiBzcmNfdG9rKSArIDFcbnByaW50KFx1MDAyN0Nyb3NzLWF0dGVudGlvbiBhbGlnbm1lbnQgKHJvd3M9dGFyZ2V0LCBjb2xzPXNvdXJjZSk6XHUwMDI3KVxucHJpbnQoXHUwMDI3ezpcdTAwM2U4fVx1MDAyNy5mb3JtYXQoXHUwMDI3XHUwMDI3KSArIFx1MDAyN1x1MDAyNy5qb2luKFx1MDAyN3s6XHUwMDNle3d9fVx1MDAyNy5mb3JtYXQodCwgdz1jb2xfdykgZm9yIHQgaW4gc3JjX3RvaykpXG5wcmludChcdTAwMjctXHUwMDI3ICogKDggKyBjb2xfdyAqIG5rKSlcbmZvciBpLCB0Z3QgaW4gZW51bWVyYXRlKHRndF90b2spOlxuICAgIHJvdyA9IEFbaV1cbiAgICBjZWxscyA9IFx1MDAyN1x1MDAyNy5qb2luKFxuICAgICAgICBcdTAwMjd7Olx1MDAzZXt3fX1cdTAwMjcuZm9ybWF0KFx1MDAyNyMjXHUwMDI3IGlmIGogPT0gcm93LmFyZ21heCgpIGVsc2UgXHUwMDI3LS1cdTAwMjcgaWYgcm93W2pdIFx1MDAzZSAwLjE1IGVsc2UgXHUwMDI3ICBcdTAwMjcsIHc9Y29sX3cpXG4gICAgICAgIGZvciBqIGluIHJhbmdlKG5rKSlcbiAgICBwcmludChcdTAwMjd7Olx1MDAzZTh9e30gcGVhay1cdTAwM2V7fVx1MDAyNy5mb3JtYXQodGd0LCBjZWxscywgc3JjX3Rva1tyb3cuYXJnbWF4KCldKSlcbnByaW50KFx1MDAyN0FsaWdubWVudCBzaGFwZTpcdTAwMjcsIEEuc2hhcGUsIFx1MDAyNyhucT17fSB4IG5rPXt9KVx1MDAyNy5mb3JtYXQobnEsIG5rKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVc2FnZSBBY3Jvc3MgQXJjaGl0ZWN0dXJlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkVSVCBhbmQgZW5jb2Rlci1vbmx5IG1vZGVscyB1c2UgYmlkaXJlY3Rpb25hbCBzZWxmLWF0dGVudGlvbiBleGNsdXNpdmVseSDigJQgbm8gY3Jvc3MtYXR0ZW50aW9uLCBubyBjYXVzYWwgbWFzay4gR1BUIGFuZCBkZWNvZGVyLW9ubHkgbW9kZWxzIHVzZSBjYXVzYWwgc2VsZi1hdHRlbnRpb24gZXhjbHVzaXZlbHkg4oCUIG5vIGNyb3NzLWF0dGVudGlvbiwgbm8gZW5jb2Rlci4gVDUgYW5kIEJBUlQgYXJlIGVuY29kZXItZGVjb2RlciBtb2RlbHMgd2l0aCBib3RoOiB0aGUgZW5jb2RlciBzdGFjayB1c2VzIGJpZGlyZWN0aW9uYWwgc2VsZi1hdHRlbnRpb24gYW5kIHRoZSBkZWNvZGVyIHVzZXMgY2F1c2FsIHNlbGYtYXR0ZW50aW9uIHBsdXMgY3Jvc3MtYXR0ZW50aW9uIHRvIHRoZSBlbmNvZGVyIG91dHB1dC4gVmlzaW9uIFRyYW5zZm9ybWVycyAoVmlUKSB1c2UgYmlkaXJlY3Rpb25hbCBzZWxmLWF0dGVudGlvbiBhbW9uZyBpbWFnZSBwYXRjaGVzOyBjcm9zcy1hdHRlbnRpb24gaXMgYWRkZWQgaW4gZGVjb2RlciBoZWFkcyBmb3IgZGVuc2UgcHJlZGljdGlvbiB0YXNrcyAoREVUUiwgTWFzazJGb3JtZXIpLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIlNlbGYtQXR0ZW50aW9uIiwiQ3Jvc3MtQXR0ZW50aW9uIl0sInJvd3MiOltbIlEgc291cmNlIiwiU2FtZSBzZXF1ZW5jZSBYIGFzIEsgYW5kIFYiLCJEaWZmZXJlbnQgc2VxdWVuY2UgKGUuZy4sIGRlY29kZXIgc3RhdGVzKSJdLFsiSywgViBzb3VyY2UiLCJTYW1lIHNlcXVlbmNlIFggYXMgUSIsIkRpZmZlcmVudCBzZXF1ZW5jZSAoZS5nLiwgZW5jb2RlciBvdXRwdXQpIl0sWyJBdHRlbnRpb24gbWF0cml4IHNoYXBlIiwibiDDlyBuIChzcXVhcmUpIiwibnEgw5cgbmsgKHJlY3Rhbmd1bGFyLCBucSDiiaAgbmsgaW4gZ2VuZXJhbCkiXSxbIkRpcmVjdGlvbmFsaXR5IiwiQmlkaXJlY3Rpb25hbCBvciBjYXVzYWwgKG1hc2tlZCkiLCJVbnJlc3RyaWN0ZWQg4oCUIGFsbCBuayBlbmNvZGVyIHBvc2l0aW9ucyB2aXNpYmxlIl0sWyJVc2VkIGluIiwiQkVSVCAoYmlkaXIpLCBHUFQgKGNhdXNhbCksIFZpVCAoYmlkaXIpIiwiVDUsIEJBUlQsIGNsYXNzaWMgc2VxMnNlcSwgREVUUiwgQ29udHJvbE5ldCJdLFsiQ29tcHV0YXRpb25hbCByb2xlIiwiQnVpbGQgY29udGV4dHVhbCByZXByZXNlbnRhdGlvbnMgd2l0aGluIG9uZSBzZXF1ZW5jZSIsIkJyaWRnZSBpbmZvcm1hdGlvbiBhY3Jvc3MgdHdvIGRpZmZlcmVudCBzZXF1ZW5jZXMiXSxbIkNhbiBhdHRlbmQgdG8gaXRzIG93biBmdXR1cmU/IiwiWWVzIChiaWRpcikgb3Igbm8gKGNhdXNhbCBtYXNrKSIsIk4vQSDigJQgSy9WIGNvbWUgZnJvbSBhIHNlcGFyYXRlIGZ1bGx5LW9ic2VydmVkIHNlcXVlbmNlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDcm9zcy1BdHRlbnRpb24gQmV5b25kIE5MUCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ3Jvc3MtYXR0ZW50aW9uIGhhcyBiZWNvbWUgYSBnZW5lcmFsIG1lY2hhbmlzbSBmb3IgY29uZGl0aW9uaW5nIG9uZSBtb2RhbGl0eSBvbiBhbm90aGVyLiBJbiBkaWZmdXNpb24gbW9kZWxzIChTdGFibGUgRGlmZnVzaW9uKSwgdGhlIGRlbm9pc2luZyBVLU5ldCB1c2VzIGNyb3NzLWF0dGVudGlvbiBhdCBlYWNoIHJlc29sdXRpb24gdG8gY29uZGl0aW9uIGltYWdlIGZlYXR1cmVzIG9uIHRleHQgZW1iZWRkaW5ncyDigJQgdGhlIGltYWdlIGZlYXR1cmVzIHByb3ZpZGUgcXVlcmllcywgdGhlIENMSVAgdGV4dCBlbmNvZGVyIG91dHB1dCBwcm92aWRlcyBrZXlzIGFuZCB2YWx1ZXMuIENvbnRyb2xOZXQgYWRkcyBhIGNvcHkgb2YgdGhlIFUtTmV0IGVuY29kZXIgd2l0aCBhZGRpdGlvbmFsIGNyb3NzLWF0dGVudGlvbiBpbnB1dHMgZnJvbSBzcGF0aWFsIGNvbmRpdGlvbmluZyBzaWduYWxzIChkZXB0aCBtYXBzLCBwb3NlLCBlZGdlcykuIEluIG11bHRpbW9kYWwgTExNcyAoRmxhbWluZ28sIExMYVZBKSwgY3Jvc3MtYXR0ZW50aW9uIGFsbG93cyB0aGUgbGFuZ3VhZ2UgbW9kZWwgdG8gYXR0ZW5kIHRvIHZpc3VhbCBwYXRjaCBlbWJlZGRpbmdzIGZyb20gYSBmcm96ZW4gdmlzaW9uIGVuY29kZXIuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJEaWZmdXNpb24gVS1OZXQ6IGltYWdlIHBhdGNoIHF1ZXJpZXMgYXR0ZW5kIG92ZXIgQ0xJUCB0ZXh0IGVtYmVkZGluZyBrZXlzL3ZhbHVlcyBmb3IgdGV4dC10by1pbWFnZSBnZW5lcmF0aW9uIiwiQ29udHJvbE5ldDogc3BhdGlhbCBjb250cm9sIHNpZ25hbHMgKGVkZ2UsIGRlcHRoLCBwb3NlKSBwcm92aWRlIGFkZGl0aW9uYWwgY3Jvc3MtYXR0ZW50aW9uIGNvbmRpdGlvbmluZyB0byBVLU5ldCIsIkZsYW1pbmdvIC8gTExhVkE6IGxhbmd1YWdlIGRlY29kZXIgY3Jvc3MtYXR0ZW5kcyB0byB2aXN1YWwgcGF0Y2ggZW1iZWRkaW5ncyBmcm9tIGEgVmlUIHZpc2lvbiBlbmNvZGVyIiwiREVUUiBvYmplY3QgZGV0ZWN0aW9uOiBvYmplY3QgcXVlcnkgZW1iZWRkaW5ncyBjcm9zcy1hdHRlbmQgdG8gQ05OIGZlYXR1cmUgbWFwcyBmb3IgZW5kLXRvLWVuZCBkZXRlY3Rpb24iLCJBbHBoYUZvbGQyIChFdm9mb3JtZXIpOiBzZXF1ZW5jZS1zdHJ1Y3R1cmUgY3Jvc3MtYXR0ZW50aW9uOyBjcm9zcy1hdHRlbnRpb24gYmV0d2VlbiBNU0Egcm93cyBhbmQgcGFpciByZXByZXNlbnRhdGlvbnMiLCJQZXJjZWl2ZXIgSU86IGxhdGVudCBhcnJheSBjcm9zcy1hdHRlbmRzIHRvIGFyYml0cmFyeS1tb2RhbGl0eSBpbnB1dCBhcnJheXMsIGVuYWJsaW5nIG1vZGFsaXR5LWFnbm9zdGljIHByb2Nlc3NpbmciXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Self-Attention vs Cross-Attention — Encoder and Decoder Patterns

Attention mechanisms differ fundamentally in where their Q, K, and V inputs come from. Self-attention takes all three from the same sequence, allowing each position to attend to every other position in that same sequence. Cross-attention takes Q from one sequence and K, V from a different sequence, bridging information between two separate representations. These two variants are not interchangeable — each is used in specific architectural positions with specific computational purposes.

## Self-Attention — Definition and Properties

In self-attention Q = X·WQ, K = X·WK, V = X·WV where X is the same input sequence. Every position produces a query that is scored against keys from all other positions in X — the attention matrix A ∈ ℝ^{n×n} is square. Bidirectional self-attention allows each position to attend to all others (including future positions), making the representations context-aware in both directions. Causal (masked) self-attention applies an upper-triangular mask of −∞ to the score matrix before softmax, preventing position i from attending to positions j > i. This preserves the autoregressive property required for text generation.

```python
import numpy as np

def self_attention(X, W_Q, W_K, W_V, causal=False):
    # X: (n, d_model); Q=K=V all derived from same X
    Q = X @ W_Q    # (n, dk)
    K = X @ W_K    # (n, dk)
    V = X @ W_V    # (n, dv)
    dk = Q.shape[-1]
    S = Q @ K.T / np.sqrt(dk)    # (n, n) — square matrix
    if causal:
        # Upper triangle -> -inf so softmax gives 0 weight
        mask = np.triu(np.ones_like(S), k=1) * -1e9
        S = S + mask
    S -= S.max(axis=-1, keepdims=True)
    A = np.exp(S); A /= A.sum(axis=-1, keepdims=True)
    return A @ V, A

np.random.seed(42)
n, d_model, dk, dv = 6, 64, 32, 32
X = np.random.randn(n, d_model)
W_Q = np.random.randn(d_model, dk) * 0.1
W_K = np.random.randn(d_model, dk) * 0.1
W_V = np.random.randn(d_model, dv) * 0.1

_, A_bi  = self_attention(X, W_Q, W_K, W_V, causal=False)
_, A_cau = self_attention(X, W_Q, W_K, W_V, causal=True)
print('Bidirectional SA shape:', A_bi.shape, '(n x n, square)')
print('Upper triangle zero in causal SA:', np.allclose(np.triu(A_cau, 1), 0))
print('Causal: position 0 attends only to itself:', A_cau[0].round(4))
print('Causal: position 5 attends to all 6:', (A_cau[5] > 1e-6).sum(), 'positions')
```

## Cross-Attention — Definition and Properties

In cross-attention the query Q comes from one sequence (e.g., decoder states) while keys K and values V come from a second sequence (e.g., encoder output). Queries and keys must share the same inner dimension dₖ but the two sequences can have different lengths: nq ≠ nk. The attention matrix A ∈ ℝ^{nq×nk} is rectangular — each of the nq query positions attends over all nk key-value positions. No causal masking is needed (and none is applied) because the query sequence is attending to a fully-observed context sequence, not to its own future.

```python
import numpy as np

def cross_attention(Q_seq, KV_seq, W_Q, W_K, W_V):
    # Q_seq: (nq, d_q) — decoder states; KV_seq: (nk, d_kv) — encoder output
    Q = Q_seq  @ W_Q    # (nq, dk)
    K = KV_seq @ W_K    # (nk, dk)
    V = KV_seq @ W_V    # (nk, dv)
    dk = Q.shape[-1]
    S = Q @ K.T / np.sqrt(dk)    # (nq, nk) — RECTANGULAR, nq != nk
    S -= S.max(axis=-1, keepdims=True)
    A = np.exp(S); A /= A.sum(axis=-1, keepdims=True)
    return A @ V, A              # output: (nq, dv), weights: (nq, nk)

np.random.seed(7)
nq, nk, d_model, dk, dv = 4, 10, 64, 32, 32
dec_states = np.random.randn(nq, d_model)   # short target sequence
enc_states  = np.random.randn(nk, d_model)  # longer source sequence
W_Q = np.random.randn(d_model, dk) * 0.1
W_K = np.random.randn(d_model, dk) * 0.1
W_V = np.random.randn(d_model, dv) * 0.1

out, A = cross_attention(dec_states, enc_states, W_Q, W_K, W_V)
print('Dec states:', dec_states.shape, '  Enc states:', enc_states.shape)
print('Attention matrix:', A.shape, '<- rectangular (nq x nk)')
print('Output:', out.shape)
print('Row sums (should be 1):', A.sum(axis=1).round(5))
```

> **Key Difference — Where Q, K, V Come From**: Self-attention: Q, K, V all from the same tensor X — the attention matrix is always square (n×n). Cross-attention: Q from sequence A, K and V from sequence B — the attention matrix is rectangular (nA×nB) and nA can differ from nB. Confusing these causes shape errors: if you pass a cross-attention decoder query (nq=8) against encoder keys (nk=100) and expect a square matrix, you will get a (8×100) matrix — correct for cross-attention, not for self-attention.

## Encoder Self-Attention — Bidirectional Context

Transformer encoders (BERT, RoBERTa, ViT) use bidirectional self-attention throughout. Every token/patch position attends to every other position in the same sequence with no masking. This allows each position to integrate context from both its left and right neighbours in every layer, building representations that are conditioned on the full input sequence. The encoder output H ∈ ℝ^{n×d_model} is a contextualised representation of every input position — it is then passed as the K and V source to the decoder's cross-attention.

## Decoder Attention Patterns — Causal Self + Cross

A standard Transformer decoder (T5, BART, original seq2seq) contains two attention sub-layers per block. First, causal self-attention: the decoder's own generated tokens attend only to previously generated tokens (positions 0..t-1 for position t), enforcing autoregressive left-to-right generation. Second, cross-attention: the decoder queries attend over the full encoder output to pull in source-sequence information. This cross-attention is the information bridge that replaced the RNN context vector in pre-Transformer seq2seq models.

```python
import torch
import torch.nn as nn

class EncDecBlock(nn.Module):
    def __init__(self, d, h, ff):
        super().__init__()
        self.enc_sa   = nn.MultiheadAttention(d, h, batch_first=True)
        self.dec_sa   = nn.MultiheadAttention(d, h, batch_first=True)
        self.dec_ca   = nn.MultiheadAttention(d, h, batch_first=True)
        self.enc_ff   = nn.Sequential(nn.Linear(d, ff), nn.ReLU(), nn.Linear(ff, d))
        self.dec_ff   = nn.Sequential(nn.Linear(d, ff), nn.ReLU(), nn.Linear(ff, d))
        self.norms    = nn.ModuleList([nn.LayerNorm(d) for _ in range(5)])

    def encode(self, src):
        a, _ = self.enc_sa(src, src, src)              # bidirectional self-attn
        x = self.norms[0](src + a)
        return self.norms[1](x + self.enc_ff(x))

    def decode(self, tgt, enc_out, causal_mask=None):
        a, _ = self.dec_sa(tgt, tgt, tgt, attn_mask=causal_mask)  # causal
        x = self.norms[2](tgt + a)
        a, cross_w = self.dec_ca(x, enc_out, enc_out)              # cross-attn
        x = self.norms[3](x + a)
        return self.norms[4](x + self.dec_ff(x)), cross_w

torch.manual_seed(3)
d, h, ff = 128, 4, 256
model = EncDecBlock(d, h, ff)
src = torch.randn(2, 15, d)   # batch=2, src_len=15
tgt = torch.randn(2,  8, d)   # batch=2, tgt_len=8
enc_out        = model.encode(src)
dec_out, cross_w = model.decode(tgt, enc_out)
print('Encoder output:', tuple(enc_out.shape))
print('Decoder output:', tuple(dec_out.shape))
print('Cross-attention weights:', tuple(cross_w.shape), '(batch x tgt x src)')
```

## Cross-Attention Alignment Visualisation

In seq2seq models, the cross-attention weight matrix is an alignment: entry A[i,j] is how much decoder position i (target token) attends to encoder position j (source token). For translation, this roughly recovers monotonic alignment for similar-language pairs and reordering alignment for distant-language pairs. In image captioning, A[i,j] shows which image patch decoder step i focuses on when generating word i. In text-to-speech, it provides a soft alignment between phoneme output frames and input character positions.

```python
import numpy as np

def cross_attn(dec_Q, enc_KV, W_Q, W_K, W_V):
    Q = dec_Q @ W_Q; K = enc_KV @ W_K; V = enc_KV @ W_V
    S = Q @ K.T / np.sqrt(W_Q.shape[1])
    S -= S.max(1, keepdims=True)
    A = np.exp(S); A /= A.sum(1, keepdims=True)
    return A @ V, A

np.random.seed(11)
src_tok = ['Le', 'chat', 'est', 'assis', 'sur', 'le', 'tapis', '.']
tgt_tok = ['The', 'cat', 'sat', 'on', 'the', 'mat', '.']
nq, nk, d, dk = len(tgt_tok), len(src_tok), 32, 16
W_Q = np.random.randn(d, dk) * 0.3
W_K = np.random.randn(d, dk) * 0.3
W_V = np.random.randn(d, dk) * 0.3
dec_states = np.random.randn(nq, d)
enc_states  = np.random.randn(nk, d)
_, A = cross_attn(dec_states, enc_states, W_Q, W_K, W_V)

col_w = max(len(t) for t in src_tok) + 1
print('Cross-attention alignment (rows=target, cols=source):')
print('{:>8}'.format('') + ''.join('{:>{w}}'.format(t, w=col_w) for t in src_tok))
print('-' * (8 + col_w * nk))
for i, tgt in enumerate(tgt_tok):
    row = A[i]
    cells = ''.join(
        '{:>{w}}'.format('##' if j == row.argmax() else '--' if row[j] > 0.15 else '  ', w=col_w)
        for j in range(nk))
    print('{:>8}{} peak->{}'.format(tgt, cells, src_tok[row.argmax()]))
print('Alignment shape:', A.shape, '(nq={} x nk={})'.format(nq, nk))
```

## Usage Across Architectures

BERT and encoder-only models use bidirectional self-attention exclusively — no cross-attention, no causal mask. GPT and decoder-only models use causal self-attention exclusively — no cross-attention, no encoder. T5 and BART are encoder-decoder models with both: the encoder stack uses bidirectional self-attention and the decoder uses causal self-attention plus cross-attention to the encoder output. Vision Transformers (ViT) use bidirectional self-attention among image patches; cross-attention is added in decoder heads for dense prediction tasks (DETR, Mask2Former).

| Property | Self-Attention | Cross-Attention |
| --- | --- | --- |
| Q source | Same sequence X as K and V | Different sequence (e.g., decoder states) |
| K, V source | Same sequence X as Q | Different sequence (e.g., encoder output) |
| Attention matrix shape | n × n (square) | nq × nk (rectangular, nq ≠ nk in general) |
| Directionality | Bidirectional or causal (masked) | Unrestricted — all nk encoder positions visible |
| Used in | BERT (bidir), GPT (causal), ViT (bidir) | T5, BART, classic seq2seq, DETR, ControlNet |
| Computational role | Build contextual representations within one sequence | Bridge information across two different sequences |
| Can attend to its own future? | Yes (bidir) or no (causal mask) | N/A — K/V come from a separate fully-observed sequence |

## Cross-Attention Beyond NLP

Cross-attention has become a general mechanism for conditioning one modality on another. In diffusion models (Stable Diffusion), the denoising U-Net uses cross-attention at each resolution to condition image features on text embeddings — the image features provide queries, the CLIP text encoder output provides keys and values. ControlNet adds a copy of the U-Net encoder with additional cross-attention inputs from spatial conditioning signals (depth maps, pose, edges). In multimodal LLMs (Flamingo, LLaVA), cross-attention allows the language model to attend to visual patch embeddings from a frozen vision encoder.

- Diffusion U-Net: image patch queries attend over CLIP text embedding keys/values for text-to-image generation
- ControlNet: spatial control signals (edge, depth, pose) provide additional cross-attention conditioning to U-Net
- Flamingo / LLaVA: language decoder cross-attends to visual patch embeddings from a ViT vision encoder
- DETR object detection: object query embeddings cross-attend to CNN feature maps for end-to-end detection
- AlphaFold2 (Evoformer): sequence-structure cross-attention; cross-attention between MSA rows and pair representations
- Perceiver IO: latent array cross-attends to arbitrary-modality input arrays, enabling modality-agnostic processing

---

