---
title: "Linear Attention — Kernel Approximation of Softmax Attention"
slug: "linear-attention"
description: "Derive the kernel trick that reduces attention from O(L²) to O(Ld²), implement Performer FAVOR+ random feature approximation, verify quality versus softmax on short and long sequences, and benchmark throughput at L=1K, 4K, and 16K."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU29mdG1heCBhdHRlbnRpb24gY29tcHV0ZXMgTyA9IHNvZnRtYXgoUUvhtYAv4oiaZCkgwrcgViB3aGVyZSB0aGUgaW50ZXJtZWRpYXRlIFFL4bWAIG1hdHJpeCBoYXMgc2hhcGUgKEIsIGgsIEwsIEwpIOKAlCBxdWFkcmF0aWMgaW4gc2VxdWVuY2UgbGVuZ3RoLiBMaW5lYXIgYXR0ZW50aW9uIHJlcGxhY2VzIHRoZSBzb2Z0bWF4IHdpdGggYSBrZXJuZWwgZnVuY3Rpb24gz4YgdGhhdCBmYWN0b3Jpc2VzIG92ZXIgcXVlcnkgYW5kIGtleTogYXR0bihRLCBLLCBWKSDiiYggz4YoUSkoz4YoSynhtYBWKS4gQmVjYXVzZSBtYXRyaXggbXVsdGlwbGljYXRpb24gaXMgYXNzb2NpYXRpdmUsIGNvbXB1dGluZyDPhihLKeG1gFYgZmlyc3QgKHNoYXBlIGQgw5cgZCkgY29zdHMgTyhMZMKyKTsgdGhlbiBtdWx0aXBseWluZyDPhihRKSBieSB0aGlzIChzaGFwZSBMIMOXIGQpIGNvc3RzIE8oTGTCsikg4oCUIHRvdGFsIE8oTGTCsikgaW5kZXBlbmRlbnQgb2YgTC4gVGhpcyBlbGltaW5hdGVzIHRoZSBMwrIgYm90dGxlbmVjayBhdCB0aGUgY29zdCBvZiBhcHByb3hpbWF0aW9uIGVycm9yIGluIHRoZSBhdHRlbnRpb24gZGlzdHJpYnV0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNvZnRtYXggQXR0ZW50aW9uIGlzIE8oTMKyZCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjYW5vbmljYWwgZGVyaXZhdGlvbjogc29mdG1heChRS+G1gC/iiJpkKSBpcyAoTCDDlyBMKTsgbXVsdGlwbHlpbmcgYnkgViBpcyAoTCDDlyBMKSDDlyAoTCDDlyBkKSA9IE8oTMKyZCkgRkxPUHMgYW5kIE8oTMKyKSBtZW1vcnkuIFRoaXMgY2Fubm90IGJlIGZhY3RvcmVkIHdpdGhvdXQgYXBwcm94aW1hdGlvbiBiZWNhdXNlIHNvZnRtYXggaXMgbm90IGEgbGluZWFyIGZ1bmN0aW9uOiBzb2Z0bWF4KFFL4bWAKSDiiaAgUSDCtyAoS+G1gCDCtyBzb21ldGhpbmcpLiBUaGUga2V5IG9ic2VydmF0aW9uIGlzIHRoYXQgc29mdG1heChx4bWi4bWAa+KxvCkgY2FuIGJlIHZpZXdlZCBhcyBhIGtlcm5lbCBmdW5jdGlvbiBLKHHhtaIsIGvisbwpID0gZXhwKHHhtaLhtYBr4rG8L+KImmQpIC8gWiDigJQgaWYgSyhxLCBrKSA9IM+GKHEp4bWAz4YoaykgZm9yIHNvbWUgZmVhdHVyZSBtYXAgz4YsIHRoZW4gdGhlIG5vcm1hbGlzYXRpb24gWiA9IM6j4rG8IM+GKHEp4bWAz4Yoa+KxvCkgPSDPhihxKeG1gCjOo+KxvCDPhihr4rG8KSkgY2FuIGJlIGNvbXB1dGVkIGluIE8oTGQpIGFuZCB0aGUgZW50aXJlIGF0dGVudGlvbiBpbiBPKExkwrIpLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbmVhciBBdHRlbnRpb24gdmlhIHRoZSBLZXJuZWwgVHJpY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkthdGhhcm9wb3Vsb3MgZXQgYWwuICgyMDIwKSBwcm9wb3NlIHVzaW5nIHRoZSBmZWF0dXJlIG1hcCDPhih4KSA9IGVsdSh4KSArIDEsIHdoaWNoIGlzIGFsd2F5cyBwb3NpdGl2ZSBhbmQgYXBwcm94aW1hdGVzIHRoZSBleHBvbmVudGlhbCBrZXJuZWwuIFRoZSBsaW5lYXIgYXR0ZW50aW9uIGZvcm11bGEgaXM6IE9faSA9IM+GKFFfaSnhtYAgKM6j4rG8IM+GKEvisbwpVuKxvOG1gCkgLyAoz4YoUV9pKeG1gCDOo+KxvCDPhihL4rG8KSkuIFRoZSBkZW5vbWluYXRvciAodGhlIG5vcm1hbGlzYXRpb24pIGlzIM+GKFEp4bWAIMK3ICjOoyDPhihLKSkg4oCUIGEgZG90IHByb2R1Y3QgYWZ0ZXIgc3VtbWluZyB0aGUgZmVhdHVyZSBtYXBzLiBCb3RoIHRoZSBudW1lcmF0b3IgKHRoZSBvdXRwdXQpIGFuZCBkZW5vbWluYXRvciBhcmUgY29tcHV0ZWQgaW4gTyhMZMKyKSB0b3RhbCBieSBmaXJzdCBhY2N1bXVsYXRpbmcgzqPisbwgz4YoS+KxvClW4rG84bWAIChzaGFwZSBkIMOXIGQpIGFuZCDOo+KxvCDPhihL4rG8KSAoc2hhcGUgZCksIHRoZW4gbXVsdGlwbHlpbmcgZWFjaCBxdWVyeVx1MDAyN3Mgz4YoUV9pKSBhZ2FpbnN0IHRoZXNlIGFjY3VtdWxhdG9ycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5kZWYgZWx1X2ZlYXR1cmVfbWFwKHgpOlxuICAgIFwiXCJcIkVMVSsxIGZlYXR1cmUgbWFwOiBhbHdheXMgcG9zaXRpdmUsIGFwcHJveGltYXRlcyBleHAga2VybmVsLlwiXCJcIlxuICAgIHJldHVybiBGLmVsdSh4KSArIDFcblxuZGVmIGxpbmVhcl9hdHRlbnRpb24oUSwgSywgVik6XG4gICAgXCJcIlwiTGluZWFyIGF0dGVudGlvbiBPKExkXjIpIHZpYSBrZXJuZWwgdHJpY2sgd2l0aCBFTFUrMSBmZWF0dXJlIG1hcC5cbiAgICBRLCBLLCBWOiAoQiwgaCwgTCwgZCkuIFJldHVybnM6IChCLCBoLCBMLCBkKS5cbiAgICBcIlwiXCJcbiAgICBwaGlfUSA9IGVsdV9mZWF0dXJlX21hcChRKSAgIyAoQiwgaCwgTCwgZClcbiAgICBwaGlfSyA9IGVsdV9mZWF0dXJlX21hcChLKSAgIyAoQiwgaCwgTCwgZClcbiAgICAjIEFjY3VtdWxhdGU6IEtWID0gc3VtX2ogcGhpKEtfaikgVl9qXlQgIC0tIHNoYXBlIChCLCBoLCBkLCBkKVxuICAgIEtWID0gcGhpX0sudHJhbnNwb3NlKC0yLCAtMSkgQCBWICAgICAgICAgICMgTyhMICogZF4yKVxuICAgICMgQWNjdW11bGF0ZTogS3N1bSA9IHN1bV9qIHBoaShLX2opICAgICAgIC0tIHNoYXBlIChCLCBoLCBkKVxuICAgIEtzdW0gPSBwaGlfSy5zdW0oZGltPS0yKSAgICAgICAgICAgICAgICAgICMgTyhMICogZClcbiAgICAjIE51bWVyYXRvcjogcGhpKFEpIEAgS1YgICAgICAgICAgICAgICAgICAtLSBzaGFwZSAoQiwgaCwgTCwgZClcbiAgICBudW0gPSBwaGlfUSBAIEtWICAgICAgICAgICAgICAgICAgICAgICAgICAjIE8oTCAqIGReMilcbiAgICAjIERlbm9taW5hdG9yOiBwaGkoUSkgLiBLc3VtICAgICAgICAgICAgICAtLSBzaGFwZSAoQiwgaCwgTCwgMSlcbiAgICBkZW5vbSA9IChwaGlfUSAqIEtzdW0udW5zcXVlZXplKC0yKSkuc3VtKGRpbT0tMSwga2VlcGRpbT1UcnVlKSAgIyBPKEwqZClcbiAgICByZXR1cm4gbnVtIC8gKGRlbm9tICsgMWUtNilcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5CLCBoLCBMLCBkID0gMSwgMiwgMzIsIDE2XG5RLCBLLCBWID0gdG9yY2gucmFuZG4oQixoLEwsZCksIHRvcmNoLnJhbmRuKEIsaCxMLGQpLCB0b3JjaC5yYW5kbihCLGgsTCxkKVxub3V0X2xpbmVhciA9IGxpbmVhcl9hdHRlbnRpb24oUSwgSywgVilcbm91dF9zb2Z0bWF4ID0gRi5zY2FsZWRfZG90X3Byb2R1Y3RfYXR0ZW50aW9uKFEsIEssIFYpXG5wcmludChmXHUwMDI3TGluZWFyIGF0dGVudGlvbiBvdXRwdXQ6IHtvdXRfbGluZWFyLnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdNYXggYWJzb2x1dGUgZGlmZiBmcm9tIHNvZnRtYXg6IHsob3V0X2xpbmVhciAtIG91dF9zb2Z0bWF4KS5hYnMoKS5tYXgoKS5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdMaW5lYXIgYXR0ZW50aW9uIEZMT1BzOiBPKEwqZF4yKSA9IHtMICogZCoqMn0gfCBTb2Z0bWF4OiBPKExeMipkKSA9IHtMKioyICogZH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGVyZm9ybWVyOiBGQVZPUisgUmFuZG9tIEZlYXR1cmUgQXBwcm94aW1hdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGVyZm9ybWVyIChDaG9yb21hbnNraSBldCBhbC4gMjAyMSkgYXBwcm94aW1hdGVzIHRoZSBzb2Z0bWF4IGtlcm5lbCBleHAoceG1ouG1gGvisbwv4oiaZCkgdXNpbmcgdGhlIEZBVk9SKyAoRmFzdCBBdHRlbnRpb24gVmlhIHBvc2l0aXZlIE9ydGhvZ29uYWwgUmFuZG9tIGZlYXR1cmVzKSBtZXRob2QuIFRoZSBpZGVhOiBieSB0aGUgSm9obnNvbi1MaW5kZW5zdHJhdXNzIGxlbW1hLCBleHAoceG1ouG1gGvisbwv4oiaZCkg4omIICgxL+KImm0pIM6jX3IgY29zKM+J4bWj4bWAceG1oikgY29zKM+J4bWj4bWAa+KxvCkgKyBzaW4oz4nhtaPhtYBx4bWiKSBzaW4oz4nhtaPhtYBr4rG8KSB3aGVyZSDPieG1oyBhcmUgR2F1c3NpYW4gcmFuZG9tIHZlY3RvcnMuIFVzaW5nIG0gcmFuZG9tIGZlYXR1cmVzLCB0aGUgZmVhdHVyZSBtYXAgz4ZfRkFWT1IoeCkg4oiIIOKEnV57Mm19IHByb3ZpZGVzIGFuIHVuYmlhc2VkIGVzdGltYXRlIG9mIHRoZSBrZXJuZWwgd2l0aCB2YXJpYW5jZSBkZWNyZWFzaW5nIGFzIDEvbS4gVGhlIEZBVk9SKyB2YXJpYW50IHVzZXMgb3J0aG9nb25hbCByYW5kb20gZmVhdHVyZXMgKHNhbXBsZXMgZnJvbSB0aGUgU3RpZWZlbCBtYW5pZm9sZCkgdG8gcmVkdWNlIHZhcmlhbmNlIGZ1cnRoZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuZGVmIGZhdm9yX3BsdXNfZmVhdHVyZXMoeCwgb21lZ2EpOlxuICAgIFwiXCJcIkZBVk9SKyByYW5kb20gZmVhdHVyZSBtYXAgZm9yIHNvZnRtYXgga2VybmVsIGFwcHJveGltYXRpb24uXG4gICAgeDogKEIsIGgsIEwsIGQpICAgb21lZ2E6IChkLCBtKSByYW5kb20gcHJvamVjdGlvbnNcbiAgICBSZXR1cm5zOiAoQiwgaCwgTCwgMm0pIC0tIGV4cC1ub3JtYWxpc2VkIHRyaWcgZmVhdHVyZXNcbiAgICBcIlwiXCJcbiAgICBkLCBtID0gb21lZ2Euc2hhcGVcbiAgICBwcm9qID0geCBAIG9tZWdhICAjIChCLCBoLCBMLCBtKVxuICAgICMgTm9ybWFsaXNlIGJ5IGV4cCh8fHh8fF4yIC8gMikgZm9yIHVuYmlhc2VkIHNvZnRtYXggYXBwcm94aW1hdGlvblxuICAgIHhfbm9ybV9zcSA9ICh4ICoqIDIpLnN1bShkaW09LTEsIGtlZXBkaW09VHJ1ZSkgLyAyICAjIChCLCBoLCBMLCAxKVxuICAgIHNjYWxlID0gbWF0aC5zcXJ0KDEuMCAvIG0pXG4gICAgcGhpID0gc2NhbGUgKiB0b3JjaC5leHAoLXhfbm9ybV9zcSkgKiB0b3JjaC5jYXQoW3RvcmNoLmNvcyhwcm9qKSwgdG9yY2guc2luKHByb2opXSwgZGltPS0xKVxuICAgIHJldHVybiBwaGkgICMgKEIsIGgsIEwsIDJtKVxuXG5kZWYgcGVyZm9ybWVyX2F0dGVudGlvbihRLCBLLCBWLCBudW1fZmVhdHVyZXM9NjQpOlxuICAgIFwiXCJcIlBlcmZvcm1lciBhdHRlbnRpb24gdXNpbmcgRkFWT1IrIGZlYXR1cmVzLiBPKEwgKiBtICogZCkuXCJcIlwiXG4gICAgZCA9IFEuc2hhcGVbLTFdXG4gICAgb21lZ2EgPSB0b3JjaC5yYW5kbihkLCBudW1fZmVhdHVyZXMpIC8gbWF0aC5zcXJ0KGQpXG4gICAgcGhpX1EgPSBmYXZvcl9wbHVzX2ZlYXR1cmVzKFEsIG9tZWdhKSAgIyAoQixoLEwsMm0pXG4gICAgcGhpX0sgPSBmYXZvcl9wbHVzX2ZlYXR1cmVzKEssIG9tZWdhKVxuICAgICMgS1YgYWNjdW11bGF0b3I6IChCLCBoLCAybSwgZClcbiAgICBLViAgID0gcGhpX0sudHJhbnNwb3NlKC0yLC0xKSBAIFZcbiAgICBLc3VtID0gcGhpX0suc3VtKGRpbT0tMikgICAgICAgICAgICAgICMgKEIsIGgsIDJtKVxuICAgIG51bSAgPSBwaGlfUSBAIEtWXG4gICAgZGVub20gPSAocGhpX1EgKiBLc3VtLnVuc3F1ZWV6ZSgtMikpLnN1bShkaW09LTEsIGtlZXBkaW09VHJ1ZSlcbiAgICByZXR1cm4gbnVtIC8gKGRlbm9tICsgMWUtNilcblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIGgsIGQgPSAxLCAxLCAzMlxuZm9yIEwsIG0gaW4gWyg2NCwgMzIpLCAoMjU2LCA2NCksICgxMDI0LCAxMjgpXTpcbiAgICBRLCBLLCBWID0gdG9yY2gucmFuZG4oQixoLEwsZCksIHRvcmNoLnJhbmRuKEIsaCxMLGQpLCB0b3JjaC5yYW5kbihCLGgsTCxkKVxuICAgIG91dF9wID0gcGVyZm9ybWVyX2F0dGVudGlvbihRLCBLLCBWLCBtKVxuICAgIG91dF9zID0gRi5zY2FsZWRfZG90X3Byb2R1Y3RfYXR0ZW50aW9uKFEsIEssIFYpXG4gICAgZGlmZiA9IChvdXRfcCAtIG91dF9zKS5hYnMoKS5tZWFuKCkuaXRlbSgpXG4gICAgcHJpbnQoZlx1MDAyN0w9e0w6NGR9LCBtPXttOjNkfTogbWVhbiBhYnMgZGlmZiA9IHtkaWZmOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUXVhbGl0eTogTGluZWFyIHZzIFNvZnRtYXgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBxdWFsaXR5IGdhcCBiZXR3ZWVuIGxpbmVhciBhbmQgc29mdG1heCBhdHRlbnRpb24gZGVwZW5kcyBvbiBzZXF1ZW5jZSBsZW5ndGggYW5kIHRhc2suIEZvciBzaG9ydCBzZXF1ZW5jZXMgKEwgXHUwMDNjIDI1NiksIHRoZSBFTFUrMSBrZXJuZWwgYW5kIEZBVk9SKyBib3RoIGFwcHJveGltYXRlIHNvZnRtYXggY2xvc2VseSDigJQgZGlmZmVyZW5jZXMgaW4gcGVycGxleGl0eSBhcmUgbmVnbGlnaWJsZS4gRm9yIGxvbmcgc2VxdWVuY2VzIChMIFx1MDAzZSAyMDQ4KSwgYXBwcm94aW1hdGlvbiBlcnJvcnMgYWNjdW11bGF0ZTogdGhlIGxpbmVhciBtb2RlbCBtYXkgbG9zZSB0cmFjayBvZiByYXJlIGJ1dCBpbXBvcnRhbnQgdG9rZW5zIHRoYXQgc29mdG1heCB3b3VsZCBhc3NpZ24gaGlnaCBhdHRlbnRpb24gd2VpZ2h0LiBQZXJwbGV4aXR5IGdhcHMgb2YgMeKAkzMgcG9pbnRzIGFyZSB0eXBpY2FsIG9uIGxhbmd1YWdlIG1vZGVsbGluZyBiZW5jaG1hcmtzLiBUYXNrcyByZXF1aXJpbmcgaGFyZCByZXRyaWV2YWwgKGZpbmQgdGhlIG9uZSByZWxldmFudCBzZW50ZW5jZSBpbiBhIDE2SyBkb2N1bWVudCkgc2hvdyBsYXJnZXIgZGVncmFkYXRpb247IHRhc2tzIHdpdGggZGlmZnVzZSBhdHRlbnRpb24gKHN1bW1hcmlzYXRpb24pIHNob3cgbGVzcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5kZWYgZWx1X2ZlYXR1cmVfbWFwKHgpOlxuICAgIHJldHVybiBGLmVsdSh4KSArIDFcblxuZGVmIGxpbmVhcl9hdHRlbnRpb24oUSwgSywgVik6XG4gICAgcGhpX1EsIHBoaV9LID0gZWx1X2ZlYXR1cmVfbWFwKFEpLCBlbHVfZmVhdHVyZV9tYXAoSylcbiAgICBLViA9IHBoaV9LLnRyYW5zcG9zZSgtMiwtMSkgQCBWXG4gICAgS3N1bSA9IHBoaV9LLnN1bSgtMilcbiAgICByZXR1cm4gKHBoaV9RIEAgS1YpIC8gKChwaGlfUSAqIEtzdW0udW5zcXVlZXplKC0yKSkuc3VtKC0xLCBrZWVwZGltPVRydWUpICsgMWUtNilcblxudG9yY2gubWFudWFsX3NlZWQoNylcbkIsIGgsIGQgPSAxLCAxLCAzMlxucHJpbnQoZlwie1x1MDAyN0xcdTAwMjc6XHUwMDNlNn0ge1x1MDAyN0wtYXR0biBNU0VcdTAwMjc6XHUwMDNlMTR9IHtcdTAwMjdMLWF0dG4gTWF4RXJyXHUwMDI3Olx1MDAzZTE2fSB7XHUwMDI3UXVhbGl0eSB2ZXJkaWN0XHUwMDI3Olx1MDAzZTE4fVwiKVxuZm9yIEwgaW4gWzMyLCAxMjgsIDUxMiwgMjA0OCwgODE5Ml06XG4gICAgUSA9IHRvcmNoLnJhbmRuKEIsIGgsIEwsIGQpXG4gICAgSyA9IHRvcmNoLnJhbmRuKEIsIGgsIEwsIGQpXG4gICAgViA9IHRvcmNoLnJhbmRuKEIsIGgsIEwsIGQpXG4gICAgb3V0X3MgPSBGLnNjYWxlZF9kb3RfcHJvZHVjdF9hdHRlbnRpb24oUSwgSywgVilcbiAgICBvdXRfbCA9IGxpbmVhcl9hdHRlbnRpb24oUSwgSywgVilcbiAgICBtc2UgICA9IEYubXNlX2xvc3Mob3V0X2wsIG91dF9zKS5pdGVtKClcbiAgICBtYXhlICA9IChvdXRfbCAtIG91dF9zKS5hYnMoKS5tYXgoKS5pdGVtKClcbiAgICB2ZXJkaWN0ID0gXHUwMDI3R29vZFx1MDAyNyBpZiBtc2UgXHUwMDNjIDAuMDEgZWxzZSAoXHUwMDI3TW9kZXJhdGVcdTAwMjcgaWYgbXNlIFx1MDAzYyAwLjEgZWxzZSBcdTAwMjdQb29yXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjd7TDpcdTAwM2U2fSB7bXNlOlx1MDAzZTE0LjZmfSB7bWF4ZTpcdTAwM2UxNi40Zn0ge3ZlcmRpY3Q6XHUwMDNlMTh9XHUwMDI3KVxucHJpbnQoXHUwMDI3XFxuQ29uY2x1c2lvbjogbGluZWFyIGF0dGVudGlvbiBxdWFsaXR5IGRlZ3JhZGVzIHdpdGggTC5cdTAwMjcpXG5wcmludChcdTAwMjdGb3IgTFx1MDAzZTJLLCBxdWFsaXR5IGdhcCBpcyBzaWduaWZpY2FudCBmb3IgcmV0cmlldmFsLWhlYXZ5IHRhc2tzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaHJvdWdocHV0IGF0IFNjYWxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMaW5lYXIgYXR0ZW50aW9uIGFjaGlldmVzIGl0cyB0aHJvdWdocHV0IGFkdmFudGFnZSBhdCBsYXJnZSBMIHdoZXJlIE8oTMKyKSBtZW1vcnkgY2F1c2VzIHNvZnRtYXggYXR0ZW50aW9uIHRvIE9PTSBvciB0aHJhc2ggbWVtb3J5IGJhbmR3aWR0aC4gVGhlIGNyb3Nzb3ZlciBwb2ludCDigJQgd2hlcmUgbGluZWFyIGF0dGVudGlvbiBiZWNvbWVzIGZhc3RlciDigJQgZGVwZW5kcyBvbiBkIGFuZCBiYXRjaCBzaXplLiBGb3IgZD02NCwgdGhlIGNyb3Nzb3ZlciBpcyB0eXBpY2FsbHkgYXJvdW5kIEw9MTAwMOKAkzIwMDAgb24gR1BVLiBGb3IgZD0yNTYsIHRoZSBPKExkwrIpIGNvc3Qgb2YgbGluZWFyIGF0dGVudGlvbiBpcyBoaWdoZXIgYW5kIHRoZSBjcm9zc292ZXIgc2hpZnRzIHRvIEziiYg0MDAwLiBUaGUgUGVyZm9ybWVyIGltcGxlbWVudGF0aW9uIGF2b2lkcyBzdG9yaW5nIHRoZSBMw5dMIGF0dGVudGlvbiBtYXRyaXggZW50aXJlbHksIG1ha2luZyBpdCBtZW1vcnktYm91bmRlZCBieSBPKEzDl20pIHJhdGhlciB0aGFuIE8oTMKyKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuaW1wb3J0IHRpbWVcblxuZGVmIGVsdV9mZWF0dXJlX21hcCh4KTpcbiAgICByZXR1cm4gRi5lbHUoeCkgKyAxXG5cbmRlZiBsaW5lYXJfYXR0ZW50aW9uKFEsIEssIFYpOlxuICAgIHBoaV9RLCBwaGlfSyA9IGVsdV9mZWF0dXJlX21hcChRKSwgZWx1X2ZlYXR1cmVfbWFwKEspXG4gICAgS1YgPSBwaGlfSy50cmFuc3Bvc2UoLTIsLTEpIEAgVlxuICAgIEtzdW0gPSBwaGlfSy5zdW0oLTIpXG4gICAgcmV0dXJuIChwaGlfUSBAIEtWKSAvICgocGhpX1EgKiBLc3VtLnVuc3F1ZWV6ZSgtMikpLnN1bSgtMSwga2VlcGRpbT1UcnVlKSArIDFlLTYpXG5cbmRlZiBiZW5jaChmbiwgKmFyZ3MsIG49MjApOlxuICAgIGZvciBfIGluIHJhbmdlKDMpOiBmbigqYXJncykgICMgd2FybXVwXG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgZm9yIF8gaW4gcmFuZ2Uobik6IGZuKCphcmdzKVxuICAgIHJldHVybiAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAvIG4gKiAxMDAwXG5cbkIsIGgsIGQgPSAxLCA0LCA2NFxucHJpbnQoZlwie1x1MDAyN0xcdTAwMjc6XHUwMDNlNn0ge1x1MDAyN1NvZnRtYXggbXNcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdMaW5lYXIgbXNcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdTcGVlZHVwXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3U29mdG1heCBNQlx1MDAyNzpcdTAwM2UxMn1cIilcbmZvciBMIGluIFs1MTIsIDEwMjQsIDIwNDgsIDQwOTYsIDgxOTJdOlxuICAgIFEsIEssIFYgPSBbdG9yY2gucmFuZG4oQiwgaCwgTCwgZCkgZm9yIF8gaW4gcmFuZ2UoMyldXG4gICAgdHJ5OlxuICAgICAgICB0X3MgPSBiZW5jaChGLnNjYWxlZF9kb3RfcHJvZHVjdF9hdHRlbnRpb24sIFEsIEssIFYpXG4gICAgICAgIHNtX21lbSA9IEIgKiBoICogTCAqIEwgKiAyIC8gMTAyNCoqMlxuICAgIGV4Y2VwdCBSdW50aW1lRXJyb3I6XG4gICAgICAgIHRfcywgc21fbWVtID0gZmxvYXQoXHUwMDI3aW5mXHUwMDI3KSwgLTFcbiAgICB0X2wgPSBiZW5jaChsaW5lYXJfYXR0ZW50aW9uLCBRLCBLLCBWKVxuICAgIHNwZWVkdXAgPSB0X3MgLyB0X2wgaWYgdF9zICE9IGZsb2F0KFx1MDAyN2luZlx1MDAyNykgZWxzZSBmbG9hdChcdTAwMjdpbmZcdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN3tMOlx1MDAzZTZ9IHt0X3M6XHUwMDNlMTIuMmZ9IHt0X2w6XHUwMDNlMTIuMmZ9IHtzcGVlZHVwOlx1MDAzZTEwLjJmfSB7c21fbWVtOlx1MDAzZTEyLjFmfVx1MDAyNykifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQ29tcGxleGl0eSIsIk1lbW9yeSIsIlF1YWxpdHkiLCJQYXJhbGxlbGl6YWJsZSIsIkNhdXNhbCBzdXBwb3J0IiwiTm90ZXMiXSwicm93cyI6W1siU29mdG1heCBhdHRlbnRpb24iLCJPKEzCsmQpIiwiTyhMwrIpIiwiRXhhY3Qg4oCUIGJlc3QiLCJZZXMg4oCUIGJhdGNoZWQgbWF0bXVsIiwiWWVzIOKAlCBjYXVzYWwgbWFzayIsIkZsYXNoQXR0ZW50aW9uIHJlZHVjZXMgbWVtb3J5IHRvIE8oTCkiXSxbIlBlcmZvcm1lciAoRkFWT1IrKSIsIk8oTG1kKSIsIk8oTG0pIiwiR29vZCAobeKJpTY0KSwgZGVncmFkZXMgYXQgbGFyZ2UgTCIsIlllcyIsIlllcyIsIlVuYmlhc2VkIGVzdGltYXRvcjsgdmFyaWFuY2Ug4oidIDEvbSJdLFsiTGluZWFyIFRyYW5zZm9ybWVyIiwiTyhMZMKyKSIsIk8oTGQpIiwiTW9kZXJhdGUg4oCUIHF1YWxpdHkgZ2FwIGF0IGxhcmdlIEwiLCJZZXMgKG5vbi1jYXVzYWwpOyBzZXF1ZW50aWFsIChjYXVzYWwpIiwiWWVzIOKAlCByZWN1cnJlbnQgZm9ybSIsIkVMVSsxIGZlYXR1cmUgbWFwOyBLYXRoYXJvcG91bG9zIDIwMjAiXSxbIlJldE5ldCIsIk8oTGTCsikgdHJhaW4gLyBPKGTCsikgcGVyIHN0ZXAiLCJPKGTCsikgYXQgaW5mZXJlbmNlIiwiQ29tcGV0aXRpdmUgd2l0aCBUcmFuc2Zvcm1lciIsIlllcyAocGFyYWxsZWwgdHJhaW5pbmcpIiwiWWVzIOKAlCByZXRlbnRpb24gZGVjYXkiLCJSZWN1cnJlbnQgaW5mZXJlbmNlIGxpa2UgUk5OIl0sWyJSV0tWIiwiTyhMZCkgdHJhaW4gLyBPKGQpIHBlciBzdGVwIiwiTyhkKSIsIlN0cm9uZyBvbiBOTFAgYmVuY2htYXJrcyIsIlBhcnRpYWxseSAoV0tWIG9wZXJhdG9yKSIsIlllcyDigJQgdGltZS1taXhpbmciLCJIeWJyaWQgUk5OL1RyYW5zZm9ybWVyIGRlc2lnbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIFRyYWRlb2ZmcyBhbmQgQWx0ZXJuYXRpdmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMaW5lYXIgYXR0ZW50aW9uIGlzIG5vdCBhIGZyZWUgbHVuY2guIFRoZSBxdWFsaXR5IGRlZ3JhZGF0aW9uIGF0IGxhcmdlIEwgbWFrZXMgaXQgdW5zdWl0YWJsZSBmb3IgdGFza3MgcmVxdWlyaW5nIHByZWNpc2UgYXR0ZW50aW9uIG92ZXIgbG9uZyBjb250ZXh0cyDigJQgcmV0cmlldmFsLWF1Z21lbnRlZCBnZW5lcmF0aW9uLCBsb25nLWRvY3VtZW50IFFBLCBvciBjb2RlIGdlbmVyYXRpb24gd2l0aCBsYXJnZSByZXBvcy4gVGhlIEVMVSsxIGFuZCBGQVZPUisgYXBwcm94aW1hdGlvbnMgYXJlIGJlc3Qgc3VpdGVkIHRvIHRhc2tzIHdpdGggZGlmZnVzZSBhdHRlbnRpb24gcGF0dGVybnMgd2hlcmUgbm8gc2luZ2xlIGtleSBkb21pbmF0ZXMgdGhlIGRpc3RyaWJ1dGlvbi4gUmV0ZW50aXZlIE5ldHdvcmtzIChSZXROZXQpIGFuZCBSV0tWIHRha2UgYSBkaWZmZXJlbnQgYXBwcm9hY2g6IHRoZXkgYWNoaWV2ZSBsaW5lYXIgY29tcGxleGl0eSBkdXJpbmcgaW5mZXJlbmNlIChyZWN1cnJlbnQgZm9yd2FyZCBwYXNzKSB3aGlsZSB0cmFpbmluZyBpbiBwYXJhbGxlbCDigJQgYmV0dGVyIHByYWN0aWNhbCBxdWFsaXR5IHRoYW4gbGluZWFyIGF0dGVudGlvbiBhdCB0aGUgY29zdCBvZiBhIG1vcmUgY29tcGxleCBhcmNoaXRlY3R1cmUuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJMaW5lYXIgQXR0ZW50aW9uIFF1YWxpdHkgR2FwIElzIFJlYWwiLCJjb250ZW50IjoiRG8gbm90IHVzZSBsaW5lYXIgYXR0ZW50aW9uIGFzIGEgZHJvcC1pbiByZXBsYWNlbWVudCBmb3Igc29mdG1heCBhdHRlbnRpb24gd2l0aG91dCBlbXBpcmljYWwgdmFsaWRhdGlvbiBvbiB5b3VyIHRhc2suIFRoZSBxdWFsaXR5IGdhcCBpcyBzbWFsbCBmb3IgZGlmZnVzZSBhdHRlbnRpb24gdGFza3MgKHN1bW1hcmlzYXRpb24sIGNsYXNzaWZpY2F0aW9uKSBidXQgc2lnbmlmaWNhbnQgZm9yIHJldHJpZXZhbC1oZWF2eSB0YXNrcyAoZG9jdW1lbnQgUUEsIG11bHRpLWhvcCByZWFzb25pbmcpLiBPbiBsb25nLWNvbnRleHQgbGFuZ3VhZ2UgbW9kZWxsaW5nIChMPTgxOTIrKSwgbGluZWFyIGF0dGVudGlvbiBwZXJwbGV4aXR5IGlzIHR5cGljYWxseSAx4oCTMyBwb2ludHMgaGlnaGVyIHRoYW4gRmxhc2hBdHRlbnRpb24uIEFsd2F5cyBtZWFzdXJlIG9uIHlvdXIgZG93bnN0cmVhbSB0YXNrIGJlZm9yZSBjb21taXR0aW5nIHRvIGEgbGluZWFyIGF0dGVudGlvbiBhcmNoaXRlY3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3ViLVF1YWRyYXRpYyBBcmNoaXRlY3R1cmVzIEJleW9uZCBMaW5lYXIgQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZXZlcmFsIGFyY2hpdGVjdHVyZXMgYWNoaWV2ZSBzdWItcXVhZHJhdGljIGNvbXBsZXhpdHkgd2l0aCBiZXR0ZXIgcHJhY3RpY2FsIHF1YWxpdHkgdGhhbiBrZXJuZWwgbGluZWFyIGF0dGVudGlvbi4gSHllbmEgKE5ndXllbiBldCBhbC4gMjAyMykgcmVwbGFjZXMgYXR0ZW50aW9uIHdpdGggaW1wbGljaXQgbG9uZyBjb252b2x1dGlvbnMsIGFjaGlldmluZyBPKEwgbG9nIEwpIGNvbXBsZXhpdHkgd2l0aCBjb21wZXRpdGl2ZSBsYW5ndWFnZSBtb2RlbGxpbmcgcXVhbGl0eS4gTWFtYmEgKEd1IFx1MDAyNiBEYW8gMjAyMykgdXNlcyBhIHNlbGVjdGl2ZSBzdGF0ZSBzcGFjZSBtb2RlbCB3aXRoIE8oTCkgY29tcGxleGl0eSBhbmQgaGFyZHdhcmUtYXdhcmUgcGFyYWxsZWwgc2NhbiBmb3IgdHJhaW5pbmcuIFM0IChHdSBldCBhbC4gMjAyMSkgcGFyYW1ldHJpc2VzIHRoZSBzdGF0ZSBzcGFjZSB3aXRoIEhpUFBPIG1hdHJpY2VzIGZvciBlZmZpY2llbnQgbG9uZy1zZXF1ZW5jZSBtb2RlbGxpbmcuIFRoZXNlIG1vZGVscyByZXByZXNlbnQgYW4gYWN0aXZlIHJlc2VhcmNoIGZyb250aWVyIHdoZXJlIGFyY2hpdGVjdHVyZSBjaG9pY2UgZGVwZW5kcyBvbiB0aGUgc3BlY2lmaWMgdGFzaywgc2VxdWVuY2UgbGVuZ3RoIHJlZ2ltZSwgYW5kIGhhcmR3YXJlIGNvbnN0cmFpbnRzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTGluZWFyIFRyYW5zZm9ybWVyIChLYXRoYXJvcG91bG9zIDIwMjApOiBFTFUrMSBmZWF0dXJlIG1hcCwgZXhhY3QgbGluZWFyIGNvbXBsZXhpdHksIHF1YWxpdHkgZ2FwIGF0IExcdTAwM2UySy4iLCJQZXJmb3JtZXIgKENob3JvbWFuc2tpIDIwMjEpOiBGQVZPUisgcmFuZG9tIGZlYXR1cmVzLCB1bmJpYXNlZCBzb2Z0bWF4IGFwcHJveGltYXRpb24sIG0gY29udHJvbHMgcXVhbGl0eS1zcGVlZCB0cmFkZS1vZmYuIiwiUmV0TmV0IChTdW4gZXQgYWwuIDIwMjMpOiB0cmFpbmluZy10aW1lIHBhcmFsbGVsLCBpbmZlcmVuY2UtdGltZSByZWN1cnJlbnQgTyhkwrIvc3RlcCksIGNvbXBldGl0aXZlIE5MUCBxdWFsaXR5LiIsIlJXS1YgKFBlbmcgZXQgYWwuIDIwMjMpOiB0aW1lLW1peGluZyByZXBsYWNlcyBhdHRlbnRpb24sIE8oZCkgaW5mZXJlbmNlLCBzdHJvbmcgZW1waXJpY2FsIHJlc3VsdHMgb24gTkxQLiIsIk1hbWJhIChHdSBcdTAwMjYgRGFvIDIwMjMpOiBzZWxlY3RpdmUgU1NNIHdpdGggTyhMKSBjb21wbGV4aXR5IGFuZCBoYXJkd2FyZS1hd2FyZSBzY2FuLCBzdGF0ZS1vZi10aGUtYXJ0IGF0IHRpbWUgb2YgcHVibGljYXRpb24uIiwiSHllbmEgKE5ndXllbiBldCBhbC4gMjAyMyk6IGltcGxpY2l0IGNvbnZvbHV0aW9uLCBPKEwgbG9nIEwpLCBwcm9taXNpbmcgZm9yIEROQS9hdWRpbyB3aXRoIHZlcnkgbG9uZyBzZXF1ZW5jZXMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Linear Attention — Kernel Approximation of Softmax Attention

Softmax attention computes O = softmax(QKᵀ/√d) · V where the intermediate QKᵀ matrix has shape (B, h, L, L) — quadratic in sequence length. Linear attention replaces the softmax with a kernel function φ that factorises over query and key: attn(Q, K, V) ≈ φ(Q)(φ(K)ᵀV). Because matrix multiplication is associative, computing φ(K)ᵀV first (shape d × d) costs O(Ld²); then multiplying φ(Q) by this (shape L × d) costs O(Ld²) — total O(Ld²) independent of L. This eliminates the L² bottleneck at the cost of approximation error in the attention distribution.

## Softmax Attention is O(L²d)

The canonical derivation: softmax(QKᵀ/√d) is (L × L); multiplying by V is (L × L) × (L × d) = O(L²d) FLOPs and O(L²) memory. This cannot be factored without approximation because softmax is not a linear function: softmax(QKᵀ) ≠ Q · (Kᵀ · something). The key observation is that softmax(qᵢᵀkⱼ) can be viewed as a kernel function K(qᵢ, kⱼ) = exp(qᵢᵀkⱼ/√d) / Z — if K(q, k) = φ(q)ᵀφ(k) for some feature map φ, then the normalisation Z = Σⱼ φ(q)ᵀφ(kⱼ) = φ(q)ᵀ(Σⱼ φ(kⱼ)) can be computed in O(Ld) and the entire attention in O(Ld²).

## Linear Attention via the Kernel Trick

Katharopoulos et al. (2020) propose using the feature map φ(x) = elu(x) + 1, which is always positive and approximates the exponential kernel. The linear attention formula is: O_i = φ(Q_i)ᵀ (Σⱼ φ(Kⱼ)Vⱼᵀ) / (φ(Q_i)ᵀ Σⱼ φ(Kⱼ)). The denominator (the normalisation) is φ(Q)ᵀ · (Σ φ(K)) — a dot product after summing the feature maps. Both the numerator (the output) and denominator are computed in O(Ld²) total by first accumulating Σⱼ φ(Kⱼ)Vⱼᵀ (shape d × d) and Σⱼ φ(Kⱼ) (shape d), then multiplying each query's φ(Q_i) against these accumulators.

```python
import torch
import torch.nn.functional as F
import math

def elu_feature_map(x):
    """ELU+1 feature map: always positive, approximates exp kernel."""
    return F.elu(x) + 1

def linear_attention(Q, K, V):
    """Linear attention O(Ld^2) via kernel trick with ELU+1 feature map.
    Q, K, V: (B, h, L, d). Returns: (B, h, L, d).
    """
    phi_Q = elu_feature_map(Q)  # (B, h, L, d)
    phi_K = elu_feature_map(K)  # (B, h, L, d)
    # Accumulate: KV = sum_j phi(K_j) V_j^T  -- shape (B, h, d, d)
    KV = phi_K.transpose(-2, -1) @ V          # O(L * d^2)
    # Accumulate: Ksum = sum_j phi(K_j)       -- shape (B, h, d)
    Ksum = phi_K.sum(dim=-2)                  # O(L * d)
    # Numerator: phi(Q) @ KV                  -- shape (B, h, L, d)
    num = phi_Q @ KV                          # O(L * d^2)
    # Denominator: phi(Q) . Ksum              -- shape (B, h, L, 1)
    denom = (phi_Q * Ksum.unsqueeze(-2)).sum(dim=-1, keepdim=True)  # O(L*d)
    return num / (denom + 1e-6)

torch.manual_seed(42)
B, h, L, d = 1, 2, 32, 16
Q, K, V = torch.randn(B,h,L,d), torch.randn(B,h,L,d), torch.randn(B,h,L,d)
out_linear = linear_attention(Q, K, V)
out_softmax = F.scaled_dot_product_attention(Q, K, V)
print(f'Linear attention output: {out_linear.shape}')
print(f'Max absolute diff from softmax: {(out_linear - out_softmax).abs().max().item():.4f}')
print(f'Linear attention FLOPs: O(L*d^2) = {L * d**2} | Softmax: O(L^2*d) = {L**2 * d}')
```

## Performer: FAVOR+ Random Feature Approximation

Performer (Choromanski et al. 2021) approximates the softmax kernel exp(qᵢᵀkⱼ/√d) using the FAVOR+ (Fast Attention Via positive Orthogonal Random features) method. The idea: by the Johnson-Lindenstrauss lemma, exp(qᵢᵀkⱼ/√d) ≈ (1/√m) Σ_r cos(ωᵣᵀqᵢ) cos(ωᵣᵀkⱼ) + sin(ωᵣᵀqᵢ) sin(ωᵣᵀkⱼ) where ωᵣ are Gaussian random vectors. Using m random features, the feature map φ_FAVOR(x) ∈ ℝ^{2m} provides an unbiased estimate of the kernel with variance decreasing as 1/m. The FAVOR+ variant uses orthogonal random features (samples from the Stiefel manifold) to reduce variance further.

```python
import torch
import torch.nn.functional as F
import math

def favor_plus_features(x, omega):
    """FAVOR+ random feature map for softmax kernel approximation.
    x: (B, h, L, d)   omega: (d, m) random projections
    Returns: (B, h, L, 2m) -- exp-normalised trig features
    """
    d, m = omega.shape
    proj = x @ omega  # (B, h, L, m)
    # Normalise by exp(||x||^2 / 2) for unbiased softmax approximation
    x_norm_sq = (x ** 2).sum(dim=-1, keepdim=True) / 2  # (B, h, L, 1)
    scale = math.sqrt(1.0 / m)
    phi = scale * torch.exp(-x_norm_sq) * torch.cat([torch.cos(proj), torch.sin(proj)], dim=-1)
    return phi  # (B, h, L, 2m)

def performer_attention(Q, K, V, num_features=64):
    """Performer attention using FAVOR+ features. O(L * m * d)."""
    d = Q.shape[-1]
    omega = torch.randn(d, num_features) / math.sqrt(d)
    phi_Q = favor_plus_features(Q, omega)  # (B,h,L,2m)
    phi_K = favor_plus_features(K, omega)
    # KV accumulator: (B, h, 2m, d)
    KV   = phi_K.transpose(-2,-1) @ V
    Ksum = phi_K.sum(dim=-2)              # (B, h, 2m)
    num  = phi_Q @ KV
    denom = (phi_Q * Ksum.unsqueeze(-2)).sum(dim=-1, keepdim=True)
    return num / (denom + 1e-6)

torch.manual_seed(0)
B, h, d = 1, 1, 32
for L, m in [(64, 32), (256, 64), (1024, 128)]:
    Q, K, V = torch.randn(B,h,L,d), torch.randn(B,h,L,d), torch.randn(B,h,L,d)
    out_p = performer_attention(Q, K, V, m)
    out_s = F.scaled_dot_product_attention(Q, K, V)
    diff = (out_p - out_s).abs().mean().item()
    print(f'L={L:4d}, m={m:3d}: mean abs diff = {diff:.4f}')
```

## Quality: Linear vs Softmax

The quality gap between linear and softmax attention depends on sequence length and task. For short sequences (L < 256), the ELU+1 kernel and FAVOR+ both approximate softmax closely — differences in perplexity are negligible. For long sequences (L > 2048), approximation errors accumulate: the linear model may lose track of rare but important tokens that softmax would assign high attention weight. Perplexity gaps of 1–3 points are typical on language modelling benchmarks. Tasks requiring hard retrieval (find the one relevant sentence in a 16K document) show larger degradation; tasks with diffuse attention (summarisation) show less.

```python
import torch
import torch.nn.functional as F
import math

def elu_feature_map(x):
    return F.elu(x) + 1

def linear_attention(Q, K, V):
    phi_Q, phi_K = elu_feature_map(Q), elu_feature_map(K)
    KV = phi_K.transpose(-2,-1) @ V
    Ksum = phi_K.sum(-2)
    return (phi_Q @ KV) / ((phi_Q * Ksum.unsqueeze(-2)).sum(-1, keepdim=True) + 1e-6)

torch.manual_seed(7)
B, h, d = 1, 1, 32
print(f"{'L':>6} {'L-attn MSE':>14} {'L-attn MaxErr':>16} {'Quality verdict':>18}")
for L in [32, 128, 512, 2048, 8192]:
    Q = torch.randn(B, h, L, d)
    K = torch.randn(B, h, L, d)
    V = torch.randn(B, h, L, d)
    out_s = F.scaled_dot_product_attention(Q, K, V)
    out_l = linear_attention(Q, K, V)
    mse   = F.mse_loss(out_l, out_s).item()
    maxe  = (out_l - out_s).abs().max().item()
    verdict = 'Good' if mse < 0.01 else ('Moderate' if mse < 0.1 else 'Poor')
    print(f'{L:>6} {mse:>14.6f} {maxe:>16.4f} {verdict:>18}')
print('\nConclusion: linear attention quality degrades with L.')
print('For L>2K, quality gap is significant for retrieval-heavy tasks.')
```

## Throughput at Scale

Linear attention achieves its throughput advantage at large L where O(L²) memory causes softmax attention to OOM or thrash memory bandwidth. The crossover point — where linear attention becomes faster — depends on d and batch size. For d=64, the crossover is typically around L=1000–2000 on GPU. For d=256, the O(Ld²) cost of linear attention is higher and the crossover shifts to L≈4000. The Performer implementation avoids storing the L×L attention matrix entirely, making it memory-bounded by O(L×m) rather than O(L²).

```python
import torch
import torch.nn.functional as F
import math
import time

def elu_feature_map(x):
    return F.elu(x) + 1

def linear_attention(Q, K, V):
    phi_Q, phi_K = elu_feature_map(Q), elu_feature_map(K)
    KV = phi_K.transpose(-2,-1) @ V
    Ksum = phi_K.sum(-2)
    return (phi_Q @ KV) / ((phi_Q * Ksum.unsqueeze(-2)).sum(-1, keepdim=True) + 1e-6)

def bench(fn, *args, n=20):
    for _ in range(3): fn(*args)  # warmup
    t0 = time.perf_counter()
    for _ in range(n): fn(*args)
    return (time.perf_counter() - t0) / n * 1000

B, h, d = 1, 4, 64
print(f"{'L':>6} {'Softmax ms':>12} {'Linear ms':>12} {'Speedup':>10} {'Softmax MB':>12}")
for L in [512, 1024, 2048, 4096, 8192]:
    Q, K, V = [torch.randn(B, h, L, d) for _ in range(3)]
    try:
        t_s = bench(F.scaled_dot_product_attention, Q, K, V)
        sm_mem = B * h * L * L * 2 / 1024**2
    except RuntimeError:
        t_s, sm_mem = float('inf'), -1
    t_l = bench(linear_attention, Q, K, V)
    speedup = t_s / t_l if t_s != float('inf') else float('inf')
    print(f'{L:>6} {t_s:>12.2f} {t_l:>12.2f} {speedup:>10.2f} {sm_mem:>12.1f}')
```

| Method | Complexity | Memory | Quality | Parallelizable | Causal support | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Softmax attention | O(L²d) | O(L²) | Exact — best | Yes — batched matmul | Yes — causal mask | FlashAttention reduces memory to O(L) |
| Performer (FAVOR+) | O(Lmd) | O(Lm) | Good (m≥64), degrades at large L | Yes | Yes | Unbiased estimator; variance ∝ 1/m |
| Linear Transformer | O(Ld²) | O(Ld) | Moderate — quality gap at large L | Yes (non-causal); sequential (causal) | Yes — recurrent form | ELU+1 feature map; Katharopoulos 2020 |
| RetNet | O(Ld²) train / O(d²) per step | O(d²) at inference | Competitive with Transformer | Yes (parallel training) | Yes — retention decay | Recurrent inference like RNN |
| RWKV | O(Ld) train / O(d) per step | O(d) | Strong on NLP benchmarks | Partially (WKV operator) | Yes — time-mixing | Hybrid RNN/Transformer design |

## Practical Tradeoffs and Alternatives

Linear attention is not a free lunch. The quality degradation at large L makes it unsuitable for tasks requiring precise attention over long contexts — retrieval-augmented generation, long-document QA, or code generation with large repos. The ELU+1 and FAVOR+ approximations are best suited to tasks with diffuse attention patterns where no single key dominates the distribution. Retentive Networks (RetNet) and RWKV take a different approach: they achieve linear complexity during inference (recurrent forward pass) while training in parallel — better practical quality than linear attention at the cost of a more complex architecture.

> **Linear Attention Quality Gap Is Real**: Do not use linear attention as a drop-in replacement for softmax attention without empirical validation on your task. The quality gap is small for diffuse attention tasks (summarisation, classification) but significant for retrieval-heavy tasks (document QA, multi-hop reasoning). On long-context language modelling (L=8192+), linear attention perplexity is typically 1–3 points higher than FlashAttention. Always measure on your downstream task before committing to a linear attention architecture.

## Sub-Quadratic Architectures Beyond Linear Attention

Several architectures achieve sub-quadratic complexity with better practical quality than kernel linear attention. Hyena (Nguyen et al. 2023) replaces attention with implicit long convolutions, achieving O(L log L) complexity with competitive language modelling quality. Mamba (Gu & Dao 2023) uses a selective state space model with O(L) complexity and hardware-aware parallel scan for training. S4 (Gu et al. 2021) parametrises the state space with HiPPO matrices for efficient long-sequence modelling. These models represent an active research frontier where architecture choice depends on the specific task, sequence length regime, and hardware constraints.

- Linear Transformer (Katharopoulos 2020): ELU+1 feature map, exact linear complexity, quality gap at L>2K.
- Performer (Choromanski 2021): FAVOR+ random features, unbiased softmax approximation, m controls quality-speed trade-off.
- RetNet (Sun et al. 2023): training-time parallel, inference-time recurrent O(d²/step), competitive NLP quality.
- RWKV (Peng et al. 2023): time-mixing replaces attention, O(d) inference, strong empirical results on NLP.
- Mamba (Gu & Dao 2023): selective SSM with O(L) complexity and hardware-aware scan, state-of-the-art at time of publication.
- Hyena (Nguyen et al. 2023): implicit convolution, O(L log L), promising for DNA/audio with very long sequences.

---

