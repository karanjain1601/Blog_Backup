---
title: "Sequence Packing — Concatenating Short Sequences with Attention Masking"
slug: "sequence-packing"
description: "Sequence packing concatenates multiple short documents into a single fixed-length context window to eliminate padding waste — covering greedy first-fit bin packing, block-diagonal attention masks for cross-document isolation, position ID reset strategies for RoPE, and 2–3x throughput gains over naive padded batching."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmFyaWFibGUtbGVuZ3RoIHRleHQgc2VxdWVuY2VzIGNyZWF0ZSBhIGZ1bmRhbWVudGFsIGVmZmljaWVuY3kgcHJvYmxlbSBmb3IgYmF0Y2ggdHJhaW5pbmc6IHRvIGFzc2VtYmxlIHNlcXVlbmNlcyBpbnRvIGEgcmVjdGFuZ3VsYXIgdGVuc29yLCBzaG9ydGVyIHNlcXVlbmNlcyBtdXN0IGJlIHBhZGRlZCB0byB0aGUgbGVuZ3RoIG9mIHRoZSBsb25nZXN0IGluIHRoZSBiYXRjaC4gQSBiYXRjaCBjb250YWluaW5nIG9uZSAyMDQ4LXRva2VuIGRvY3VtZW50IGFuZCAzMSBkb2N1bWVudHMgb2YgNjQgdG9rZW5zIGhhcyA5OCUgcGFkZGluZyDigJQgNjEsNTA0IHdhc3RlZCB0b2tlbnMgb3V0IG9mIDYzLDQ4OCB0b3RhbC4gU2VxdWVuY2UgcGFja2luZyBzb2x2ZXMgdGhpcyBieSBjb25jYXRlbmF0aW5nIG11bHRpcGxlIGRvY3VtZW50cyBlbmQtdG8tZW5kIGludG8gYSBzaW5nbGUgZml4ZWQtbGVuZ3RoIGNvbnRleHQsIHJlY292ZXJpbmcgOTDigJM5OCUgdG9rZW4gdXRpbGl6YXRpb24gYW5kIHlpZWxkaW5nIDLigJMzeCB0cmFpbmluZyB0aHJvdWdocHV0IGltcHJvdmVtZW50cyBpbiBwcmFjdGljZSB3aXRob3V0IGFueSBjaGFuZ2UgdG8gbW9kZWwgYXJjaGl0ZWN0dXJlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBQYWRkaW5nIFdhc3RlIFByb2JsZW0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIHN0YW5kYXJkIHBhZGRlZCBiYXRjaGluZywgZWFjaCBiYXRjaCBpcyBmb3JtZWQgYnkgc2FtcGxpbmcgZG9jdW1lbnRzIGluZGVwZW5kZW50bHkgYW5kIHBhZGRpbmcgZXZlcnkgc2VxdWVuY2UgdG8gdGhlIGJhdGNoIG1heGltdW0gbGVuZ3RoLiBGb3IgdHlwaWNhbCBOTFAgZGF0YXNldHMg4oCUIGluc3RydWN0aW9uIHR1bmluZyBkYXRhLCBwcmVmZXJlbmNlIGRhdGEsIG9yIHdlYiBjcmF3bCB3aXRoIGhpZ2ggbGVuZ3RoIHZhcmlhbmNlIOKAlCBhdmVyYWdlIHV0aWxpemF0aW9uIGlzIDUw4oCTNzAlLiBUaGUgY29tcHV0ZSB1c2VkIG9uIHBhZGRpbmcgdG9rZW5zIGlzIGVudGlyZWx5IHdhc3RlZDogdGhlIGF0dGVudGlvbiBtZWNoYW5pc20gcHJvY2Vzc2VzIHRoZW0sIHRoZSBsb3NzIGZ1bmN0aW9uIGlnbm9yZXMgdGhlbSB2aWEgYSBsb3NzIG1hc2ssIGFuZCB0aGUgZ3JhZGllbnRzIGFyZSB6ZXJvLiBGb3IgYSBHUFUgc3BlbmRpbmcgNDAlIG9mIEZMT1BTIG9uIHBhZGRpbmcsIHBhY2tpbmcgYWxvbmUgaXMgZXF1aXZhbGVudCB0byBhIDEuNjd4IGhhcmR3YXJlIHVwZ3JhZGUg4oCUIGZyZWUgdGhyb3VnaHB1dCBmcm9tIGEgc29mdHdhcmUgY2hhbmdlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRvY3VtZW50IFBhY2tpbmcgQWxnb3JpdGhtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcGFja2luZyBwcm9ibGVtIGlzIGEgdmFyaWFudCBvZiBiaW4gcGFja2luZzogZ2l2ZW4gZG9jdW1lbnRzIG9mIHZhcnlpbmcgbGVuZ3RocyBhbmQgYmlucyBvZiBjYXBhY2l0eSBtYXhfbGVuZ3RoLCBmaWxsIGJpbnMgdG8gbWluaW1pemUgdG90YWwgYmlucyBhbmQgbWF4aW1pemUgdXRpbGl6YXRpb24uIEZpcnN0LWZpdC1kZWNyZWFzaW5nIChGRkQpIGlzIG5lYXItb3B0aW1hbCBidXQgcmVxdWlyZXMgc29ydGluZyBieSBsZW5ndGggZGVzY2VuZGluZy4gR3JlZWR5IGZpcnN0LWZpdCBpcyBzaW1wbGVyOiBpdGVyYXRlIGRvY3VtZW50cyBpbiBhcnJpdmFsIG9yZGVyLCBhcHBlbmQgZWFjaCB0byB0aGUgY3VycmVudCBiaW4gaWYgaXQgZml0cywgZmx1c2ggYW5kIG9wZW4gYSBuZXcgYmluIG90aGVyd2lzZS4gRm9yIExMTSBwcmV0cmFpbmluZyBkYXRhIHdpdGggbmF0dXJhbCBsZW5ndGggZGlzdHJpYnV0aW9ucywgZ3JlZWR5IHBhY2tpbmcgYWNoaWV2ZXMgODXigJM5NSUgdXRpbGl6YXRpb24uIEVhY2ggZG9jdW1lbnQgaXMgZm9sbG93ZWQgYnkgYW4gRU9TIHRva2VuIGFzIGEgc2VwYXJhdG9yLCBhbmQgYW55IHJlbWFpbmRlciBpbiB0aGUgZmluYWwgYmluIGlzIHBhZGRlZCB3aXRoIHplcm9zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHR5cGluZyBpbXBvcnQgTGlzdCwgVHVwbGVcbmltcG9ydCByYW5kb21cblxuZGVmIGdyZWVkeV9wYWNrX2RvY3VtZW50cyh0b2tlbml6ZWRfZG9jczogTGlzdFtMaXN0W2ludF1dLCBtYXhfbGVuZ3RoOiBpbnQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgIGVvc19pZDogaW50ID0gMikgLVx1MDAzZSBMaXN0W1R1cGxlW0xpc3RbaW50XSwgTGlzdFtpbnRdXV06XG4gICAgXCJcIlwiR3JlZWR5IGZpcnN0LWZpdCBwYWNraW5nOiBjb25jYXRlbmF0ZSBkb2NzK0VPUyB1bnRpbCBiaW4gaXMgZnVsbC5cIlwiXCJcbiAgICBiaW5zLCBjdXJfdG9rZW5zLCBjdXJfZG9jcyA9IFtdLCBbXSwgW11cbiAgICBmb3IgaWR4LCBkb2MgaW4gZW51bWVyYXRlKHRva2VuaXplZF9kb2NzKTpcbiAgICAgICAgY2h1bmsgPSBkb2MgKyBbZW9zX2lkXVxuICAgICAgICBpZiBsZW4oY3VyX3Rva2VucykgKyBsZW4oY2h1bmspIFx1MDAzZSBtYXhfbGVuZ3RoOlxuICAgICAgICAgICAgaWYgY3VyX3Rva2VuczogICMgZmx1c2ggY3VycmVudCBiaW4gd2l0aCBwYWRkaW5nXG4gICAgICAgICAgICAgICAgY3VyX3Rva2VucyArPSBbMF0gKiAobWF4X2xlbmd0aCAtIGxlbihjdXJfdG9rZW5zKSlcbiAgICAgICAgICAgICAgICBiaW5zLmFwcGVuZCgoY3VyX3Rva2VucywgY3VyX2RvY3MpKVxuICAgICAgICAgICAgY3VyX3Rva2VucywgY3VyX2RvY3MgPSBjaHVua1s6bWF4X2xlbmd0aF0sIFtpZHhdXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICBjdXJfdG9rZW5zLmV4dGVuZChjaHVuaylcbiAgICAgICAgICAgIGN1cl9kb2NzLmFwcGVuZChpZHgpXG4gICAgaWYgY3VyX3Rva2VuczogICMgZmx1c2ggZmluYWwgYmluXG4gICAgICAgIGN1cl90b2tlbnMgKz0gWzBdICogKG1heF9sZW5ndGggLSBsZW4oY3VyX3Rva2VucykpXG4gICAgICAgIGJpbnMuYXBwZW5kKChjdXJfdG9rZW5zLCBjdXJfZG9jcykpXG4gICAgcmV0dXJuIGJpbnNcblxucmFuZG9tLnNlZWQoNDIpXG5kb2NzID0gW2xpc3QocmFuZ2UocmFuZG9tLnJhbmRpbnQoNTAsIDMwMCkpKSBmb3IgXyBpbiByYW5nZSgyMDApXVxucGFja2VkID0gZ3JlZWR5X3BhY2tfZG9jdW1lbnRzKGRvY3MsIG1heF9sZW5ndGg9NTEyKVxuY29udGVudF90b2tlbnMgPSBzdW0obGVuKGQpIGZvciBkIGluIGRvY3MpXG50b3RhbF9jYXBhY2l0eSA9IGxlbihwYWNrZWQpICogNTEyXG5wcmludChmXCJCaW5zOiB7bGVuKHBhY2tlZCl9LCB0b2tlbiB1dGlsaXphdGlvbjoge2NvbnRlbnRfdG9rZW5zIC8gdG90YWxfY2FwYWNpdHk6LjElfVwiKVxucHJpbnQoZlwiTmFpdmUgcGFkZGVkIGVzdGltYXRlOiB+NjAlIC0tIHBhY2tpbmcgcmVjb3ZlcnMgfnswLjk1IC0gMC42MDouMCV9IHdhc3RlZCBjb21wdXRlXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmxvY2stRGlhZ29uYWwgQXR0ZW50aW9uIE1hc2tpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5haXZlIHBhY2tpbmcgY29uY2F0ZW5hdGVzIGRvY3VtZW50cyBidXQgYWxsb3dzIGF0dGVudGlvbiBhY3Jvc3MgZG9jdW1lbnQgYm91bmRhcmllcyDigJQgYSB0b2tlbiBmcm9tIGRvY3VtZW50IEEgY2FuIGF0dGVuZCB0byB0b2tlbnMgaW4gZG9jdW1lbnQgQi4gVGhpcyBsZWFrcyBmdXR1cmUgY29udGV4dCBhbmQgY29ycnVwdHMgY2F1c2FsIGxhbmd1YWdlIG1vZGVsaW5nOiB0aGUgbG9zcyBvbiBkb2N1bWVudCBCXHUwMDI3cyBmaXJzdCB0b2tlbiBjYW4gdXNlIGRvY3VtZW50IEFcdTAwMjdzIGxhc3QgdG9rZW4gYXMgY29udGV4dCwgd2hpY2ggd291bGQgbmV2ZXIgaGFwcGVuIGF0IGluZmVyZW5jZS4gVGhlIGZpeCBpcyBhIGJsb2NrLWRpYWdvbmFsIGF0dGVudGlvbiBtYXNrOiBlYWNoIGRvY3VtZW50IGF0dGVuZHMgb25seSB0byBpdHMgb3duIHByaW9yIHRva2VucyAoY2F1c2FsIHdpdGhpbiB0aGUgZG9jdW1lbnQpLCBhbmQgYWxsIGNyb3NzLWRvY3VtZW50IGF0dGVudGlvbiBwb3NpdGlvbnMgYXJlIHNldCB0byBuZWdhdGl2ZSBpbmZpbml0eSBhcyBhbiBhZGRpdGl2ZSBiaWFzIGFwcGxpZWQgYmVmb3JlIHNvZnRtYXguIFRoaXMgaXMgdGhlIGRlZmF1bHQgaW4gSHVnZ2luZyBGYWNlIFRSTFx1MDAyN3MgU0ZUVHJhaW5lciB3aGVuIHBhY2tpbmcgaXMgZW5hYmxlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHR5cGluZyBpbXBvcnQgTGlzdFxuXG5kZWYgbWFrZV9ibG9ja19kaWFnb25hbF9tYXNrKGRvY19sZW5ndGhzOiBMaXN0W2ludF0sIGRldmljZTogc3RyID0gXCJjcHVcIikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiQmxvY2stZGlhZ29uYWwgY2F1c2FsIG1hc2s6IHdpdGhpbi1kb2MgY2F1c2FsIGF0dGVudGlvbiwgY3Jvc3MtZG9jID0gLWluZi5cIlwiXCJcbiAgICBUID0gc3VtKGRvY19sZW5ndGhzKVxuICAgIG1hc2sgPSB0b3JjaC5mdWxsKChULCBUKSwgZmxvYXQoXCItaW5mXCIpLCBkZXZpY2U9ZGV2aWNlKVxuICAgIG9mZnNldCA9IDBcbiAgICBmb3IgTCBpbiBkb2NfbGVuZ3RoczpcbiAgICAgICAgbWFza1tvZmZzZXQ6b2Zmc2V0K0wsIG9mZnNldDpvZmZzZXQrTF0gPSB0b3JjaC50cmlsKHRvcmNoLnplcm9zKEwsIEwpKVxuICAgICAgICBvZmZzZXQgKz0gTFxuICAgIHJldHVybiBtYXNrICAjIGFkZGl0aXZlIGJpYXMgYWRkZWQgdG8gYXR0ZW50aW9uIGxvZ2l0cyBiZWZvcmUgc29mdG1heFxuXG5kZWYgcGFja2VkX2F0dGVudGlvbihxLCBrLCB2LCBkb2NfbGVuZ3Rocyk6XG4gICAgXCJcIlwiU2NhbGVkIGRvdC1wcm9kdWN0IGF0dGVudGlvbiB3aXRoIGJsb2NrLWRpYWdvbmFsIG1hc2sgZm9yIHBhY2tlZCBzZXF1ZW5jZXMuXCJcIlwiXG4gICAgbWFzayAgPSBtYWtlX2Jsb2NrX2RpYWdvbmFsX21hc2soZG9jX2xlbmd0aHMsIGRldmljZT1xLmRldmljZSlcbiAgICBzY2FsZSA9IHEuc2hhcGVbLTFdICoqIC0wLjVcbiAgICBhdHRuICA9IHRvcmNoLnNvZnRtYXgoKHEgQCBrLnRyYW5zcG9zZSgtMiwgLTEpKSAqIHNjYWxlICsgbWFzaywgZGltPS0xKVxuICAgIHJldHVybiBhdHRuIEAgdlxuXG4jIFRocmVlIGRvY3VtZW50cyBwYWNrZWQgaW50byBvbmUgc2VxdWVuY2Ugb2YgdG90YWwgbGVuZ3RoIDI1NlxuZG9jX2xlbmd0aHMgPSBbODAsIDEyMCwgNTZdXG5UID0gc3VtKGRvY19sZW5ndGhzKVxucSA9IGsgPSB2ID0gdG9yY2gucmFuZG4oMSwgVCwgNjQpICAgIyAoYmF0Y2g9MSwgc2VxPTI1NiwgZGltPTY0KVxub3V0ID0gcGFja2VkX2F0dGVudGlvbihxLCBrLCB2LCBkb2NfbGVuZ3RocylcbnByaW50KGZcIk91dHB1dCBzaGFwZToge291dC5zaGFwZX1cIikgICMgKDEsIDI1NiwgNjQpXG5tYXNrID0gbWFrZV9ibG9ja19kaWFnb25hbF9tYXNrKGRvY19sZW5ndGhzKVxucHJpbnQoZlwiQ3Jvc3MtZG9jIFt0b2sgMCAtXHUwMDNlIHRvayA4MV06IHttYXNrWzAsIDgxXS5pdGVtKCk6LjBmfVwiKSAgICMgLWluZlxucHJpbnQoZlwiV2l0aGluLWRvYyBbdG9rIDAgLVx1MDAzZSB0b2sgMF06IHttYXNrWzAsIDBdLml0ZW0oKTouMGZ9XCIpICAgIyAwLjAifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQb3NpdGlvbiBJRCBSZXNldCBTdHJhdGVnaWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIHBhY2tpbmcsIGVhY2ggZG9jdW1lbnRcdTAwMjdzIHBvc2l0aW9uIElEcyBjYW4gYmUgcmVzZXQgdG8gMCBhdCBlYWNoIGJvdW5kYXJ5IChsb2NhbCBwb3NpdGlvbnMpIG9yIGFsbG93ZWQgdG8gY29udGludWUgaW5jcmVtZW50aW5nIGFjcm9zcyBib3VuZGFyaWVzIChjdW11bGF0aXZlIHBvc2l0aW9ucykuIFJlc2V0IHBvc2l0aW9uIElEcyBhcmUgcHJlZmVycmVkIGZvciBSb1BFIG1vZGVsczogUm9QRSBlbmNvZGVzIHJlbGF0aXZlIGRpc3RhbmNlIHZpYSBhbmd1bGFyIGZyZXF1ZW5jeSwgc28gdGhlIHN0YXJ0IG9mIGEgbmV3IGRvY3VtZW50IGF0IHBhY2tlZCBwb3NpdGlvbiA1MTIgc2hvdWxkIGJlIHRyZWF0ZWQgYXMgcG9zaXRpb24gMCwgbm90IDUxMi4gQ3VtdWxhdGl2ZSBwb3NpdGlvbnMgY2F1c2UgdGhlIG1vZGVsIHRvIGJlbGlldmUgdGhlIHNlY29uZCBkb2N1bWVudCBpcyA1MTIgdG9rZW5zIGludG8gYSBzaW5nbGUgbG9uZyBzZXF1ZW5jZSwgaW50cm9kdWNpbmcgaW5jb3JyZWN0IGxvbmctcmFuZ2UgcG9zaXRpb25hbCBiaWFzZXMgdGhhdCBkZWdyYWRlIHF1YWxpdHkgb24gdGFza3MgcmVxdWlyaW5nIGFjY3VyYXRlIHBvc2l0aW9uLXNlbnNpdGl2ZSByZWFzb25pbmcuIFJlc2V0IElEcyBhcmUgdGhlIGRlZmF1bHQgaW4gVFJMIGFuZCBtb3N0IHByb2R1Y3Rpb24gcGFja2luZyBpbXBsZW1lbnRhdGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3RcblxuZGVmIGJ1aWxkX3Bvc2l0aW9uX2lkcyhkb2NfbGVuZ3RoczogTGlzdFtpbnRdLCBzdHJhdGVneTogc3RyID0gXCJyZXNldFwiKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJcbiAgICBCdWlsZCBwb3NpdGlvbiBJRHMgZm9yIGEgcGFja2VkIHNlcXVlbmNlLlxuICAgIHN0cmF0ZWd5PVx1MDAyN3Jlc2V0XHUwMDI3ICAgICA6IGVhY2ggZG9jdW1lbnQgc3RhcnRzIGF0IHBvc2l0aW9uIDAgKGxvY2FsIHBvc2l0aW9ucylcbiAgICBzdHJhdGVneT1cdTAwMjdjdW11bGF0aXZlXHUwMDI3OiBwb3NpdGlvbnMgY29udGludWUgYWNyb3NzIGRvY3VtZW50IGJvdW5kYXJpZXNcbiAgICBcIlwiXCJcbiAgICBpZiBzdHJhdGVneSA9PSBcInJlc2V0XCI6XG4gICAgICAgIHBvc2l0aW9ucyA9IFtwb3MgZm9yIEwgaW4gZG9jX2xlbmd0aHMgZm9yIHBvcyBpbiByYW5nZShMKV1cbiAgICBlbGlmIHN0cmF0ZWd5ID09IFwiY3VtdWxhdGl2ZVwiOlxuICAgICAgICBwb3NpdGlvbnMgPSBsaXN0KHJhbmdlKHN1bShkb2NfbGVuZ3RocykpKVxuICAgIGVsc2U6XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZlwiVW5rbm93biBzdHJhdGVneToge3N0cmF0ZWd5IXJ9XCIpXG4gICAgcmV0dXJuIHRvcmNoLnRlbnNvcihwb3NpdGlvbnMsIGR0eXBlPXRvcmNoLmxvbmcpXG5cbmRvY19sZW5ndGhzID0gWzUsIDQsIDZdXG5yZXNldF9pZHMgPSBidWlsZF9wb3NpdGlvbl9pZHMoZG9jX2xlbmd0aHMsIHN0cmF0ZWd5PVwicmVzZXRcIilcbmN1bXVsX2lkcyA9IGJ1aWxkX3Bvc2l0aW9uX2lkcyhkb2NfbGVuZ3Rocywgc3RyYXRlZ3k9XCJjdW11bGF0aXZlXCIpXG5wcmludChmXCJSZXNldDogICAgICB7cmVzZXRfaWRzLnRvbGlzdCgpfVwiKVxucHJpbnQoZlwiQ3VtdWxhdGl2ZToge2N1bXVsX2lkcy50b2xpc3QoKX1cIilcbiMgcmVzZXQ6ICAgICAgWzAsMSwyLDMsNCwgMCwxLDIsMywgMCwxLDIsMyw0LDVdXG4jIGN1bXVsYXRpdmU6IFswLDEsMiwzLDQsIDUsNiw3LDgsIDksMTAsMTEsMTIsMTMsMTRdXG5tYXhfcG9zX2N1bXVsID0gc3VtKGRvY19sZW5ndGhzKSAtIDFcbnByaW50KGZcIk1heCBjdW11bGF0aXZlIHBvc2l0aW9uOiB7bWF4X3Bvc19jdW11bH0gLS0gdmVyaWZ5IGJlbG93IG1vZGVsIG1heF9zZXFfbGVuXCIpXG5wcmludChcIlJlc2V0IHByZWZlcnJlZDogUm9QRSBzZWVzIGxvY2FsIGRvYyBwb3NpdGlvbnMsIG5vIHNwdXJpb3VzIGxvbmctcmFuZ2UgYmlhc1wiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRocm91Z2hwdXQgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRocm91Z2hwdXQgaW1wcm92ZW1lbnQgZnJvbSBwYWNraW5nIGlzIGRpcmVjdGx5IHByb3BvcnRpb25hbCB0byB1dGlsaXphdGlvbiBpbXByb3ZlbWVudC4gRm9yIGEgZGF0YXNldCB3aGVyZSBuYWl2ZSBwYWRkaW5nIGFjaGlldmVzIDYwJSB1dGlsaXphdGlvbiBhbmQgcGFja2luZyBhY2hpZXZlcyA5NSUsIHRoZSBlZmZlY3RpdmUgdGhyb3VnaHB1dCBnYWluIGlzIDk1LzYwIOKJiCAxLjU4eC4gVGhlIGFjdHVhbCB3YWxsLWNsb2NrIHNwZWVkdXAgaXMgdHlwaWNhbGx5IGxhcmdlciBiZWNhdXNlIHBhY2tpbmcgcmVkdWNlcyB0aGUgdG90YWwgbnVtYmVyIG9mIGZvcndhcmQgcGFzc2VzIGZvciB0aGUgc2FtZSBkYXRhLCByZWR1Y2luZyBmaXhlZCBvdmVyaGVhZCBmcm9tIGRhdGEgbG9hZGluZywgb3B0aW1pemVyIHN0ZXBzLCBhbmQgZ3JhZGllbnQgc3luY2hyb25pemF0aW9uIGluIGRpc3RyaWJ1dGVkIHRyYWluaW5nLiBGbGFzaCBBdHRlbnRpb24gMiBuYXRpdmVseSBzdXBwb3J0cyB2YXJpYWJsZS1sZW5ndGggcGFja2VkIHNlcXVlbmNlcyB2aWEgaXRzIHZhcmxlbiBrZXJuZWwsIGVsaW1pbmF0aW5nIGV2ZW4gdGhlIHNtYWxsIHJlc2lkdWFsIHBhZGRpbmcgd2l0aGluIGJpbnMgYW5kIGFjaGlldmluZyB0cnVlIDEwMCUgY29tcHV0ZSB1dGlsaXphdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdGltZVxuaW1wb3J0IHJhbmRvbVxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3RcblxuZGVmIHBhZGRlZF9iYXRjaF91dGlsaXphdGlvbihzZXFfbGVuczogTGlzdFtpbnRdKSAtXHUwMDNlIHR1cGxlOlxuICAgIFwiXCJcIkNvbXB1dGUgdG9rZW4gdXRpbGl6YXRpb24gYW5kIHNpbXVsYXRlIGNvbXB1dGUgdGltZSB3aXRoIHBhZGRlZCBiYXRjaGluZy5cIlwiXCJcbiAgICBtYXhfbGVuICAgPSBtYXgoc2VxX2xlbnMpXG4gICAgdXNlZnVsICAgID0gc3VtKHNlcV9sZW5zKVxuICAgIGFsbG9jYXRlZCA9IG1heF9sZW4gKiBsZW4oc2VxX2xlbnMpXG4gICAgc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgXyAgICAgPSB0b3JjaC5yYW5kbihsZW4oc2VxX2xlbnMpLCBtYXhfbGVuLCAxMjgpIEAgdG9yY2gucmFuZG4oMTI4LCAxMjgpXG4gICAgcmV0dXJuIHVzZWZ1bCAvIGFsbG9jYXRlZCwgdGltZS5wZXJmX2NvdW50ZXIoKSAtIHN0YXJ0XG5cbmRlZiBwYWNrZWRfYmF0Y2hfdXRpbGl6YXRpb24oc2VxX2xlbnM6IExpc3RbaW50XSwgbWF4X2xlbmd0aDogaW50ID0gMjA0OCkgLVx1MDAzZSB0dXBsZTpcbiAgICBcIlwiXCJDb21wdXRlIHRva2VuIHV0aWxpemF0aW9uIGFuZCBzaW11bGF0ZSBjb21wdXRlIHRpbWUgd2l0aCBncmVlZHkgcGFja2luZy5cIlwiXCJcbiAgICB0b3RhbCAgPSBzdW0oc2VxX2xlbnMpXG4gICAgbl9iaW5zID0gKHRvdGFsICsgbWF4X2xlbmd0aCAtIDEpIC8vIG1heF9sZW5ndGhcbiAgICBzdGFydCAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgXyAgICAgID0gdG9yY2gucmFuZG4obl9iaW5zLCBtYXhfbGVuZ3RoLCAxMjgpIEAgdG9yY2gucmFuZG4oMTI4LCAxMjgpXG4gICAgcmV0dXJuIHRvdGFsIC8gKG5fYmlucyAqIG1heF9sZW5ndGgpLCB0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnRcblxucmFuZG9tLnNlZWQoMClcbnNlcV9sZW5zID0gW3JhbmRvbS5yYW5kaW50KDY0LCA0MDApIGZvciBfIGluIHJhbmdlKDEyOCldXG5wYWRfdXRpbCwgIHBhZF90ICA9IHBhZGRlZF9iYXRjaF91dGlsaXphdGlvbihzZXFfbGVucylcbnBhY2tfdXRpbCwgcGFja190ID0gcGFja2VkX2JhdGNoX3V0aWxpemF0aW9uKHNlcV9sZW5zKVxucHJpbnQoZlwie1x1MDAyN01ldGhvZFx1MDAyNzpcdTAwM2MyMn0ge1x1MDAyN1V0aWxpemF0aW9uXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3TGF0ZW5jeSAobXMpXHUwMDI3Olx1MDAzZTE0fVwiKVxucHJpbnQoZlwie1x1MDAyN1BhZGRlZCBiYXRjaGluZ1x1MDAyNzpcdTAwM2MyMn0ge3BhZF91dGlsOlx1MDAzZTExLjElfSB7cGFkX3QgKiAxMDAwOlx1MDAzZTEzLjFmfVwiKVxucHJpbnQoZlwie1x1MDAyN1NlcXVlbmNlIHBhY2tpbmdcdTAwMjc6XHUwMDNjMjJ9IHtwYWNrX3V0aWw6XHUwMDNlMTEuMSV9IHtwYWNrX3QgKiAxMDAwOlx1MDAzZTEzLjFmfVwiKVxucHJpbnQoZlwiVGhyb3VnaHB1dCBnYWluOiB7cGFja191dGlsIC8gcGFkX3V0aWw6LjJmfXhcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGbGFzaCBBdHRlbnRpb24gMiBhbmQgVmFyaWFibGUtTGVuZ3RoIFNlcXVlbmNlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmxhc2ggQXR0ZW50aW9uIDIgKERhbyBldCBhbC4gMjAyMykgaW5jbHVkZXMgZGVkaWNhdGVkIHZhcmlhYmxlLWxlbmd0aCBzZXF1ZW5jZSBrZXJuZWxzOiBmbGFzaF9hdHRuX3Zhcmxlbl9xa3ZwYWNrZWRfZnVuYyBhbmQgZmxhc2hfYXR0bl92YXJsZW5fZnVuYyBhY2NlcHQgY3VtdWxhdGl2ZSBzZXF1ZW5jZSBsZW5ndGhzIChjdV9zZXFsZW5zKSByYXRoZXIgdGhhbiBhIHBhZGRlZCB0ZW5zb3IsIHByb2Nlc3NpbmcgdGhlIHBhY2tlZCBzZXF1ZW5jZSB3aXRob3V0IGFueSBwYWRkaW5nIG92ZXJoZWFkIGF0IGFsbC4gVGhpcyBhY2hpZXZlcyB0cnVlIDEwMCUgdXRpbGl6YXRpb24gaW4gdGhlIGF0dGVudGlvbiBrZXJuZWwuIFRoZSBpbnRlcmZhY2UgZXhwZWN0cyBhIDFEIHRlbnNvciBvZiB0b2tlbiBJRHMgd2l0aCBhbGwgZG9jdW1lbnRzIGNvbmNhdGVuYXRlZCwgYSBjdV9zZXFsZW5zIHRlbnNvciBtYXJraW5nIGRvY3VtZW50IGJvdW5kYXJpZXMsIGFuZCBtYXhfc2VxbGVuIGZvciBrZXJuZWwgY29uZmlndXJhdGlvbi4gVGhpcyBpcyB0aGUgbW9zdCBlZmZpY2llbnQgcGFja2luZyBpbXBsZW1lbnRhdGlvbiBhdmFpbGFibGUgYW5kIGlzIHVzZWQgaW4gcHJvZHVjdGlvbiBwcmV0cmFpbmluZyBhdCBNZXRhLCBNaXN0cmFsIEFJLCBhbmQgb3RoZXJzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRmxhc2ggQXR0ZW50aW9uIHZhcmxlbiBrZXJuZWwgYWNjZXB0cyBjdV9zZXFsZW5zID0gY3VtdWxhdGl2ZSBzdW0gb2YgZG9jIGxlbmd0aHMsIGUuZy4gWzAsIDgwLCAyMDAsIDI1Nl0gZm9yIHRocmVlIGRvY3Mgb2YgbGVuZ3RocyA4MCwgMTIwLCA1Ni4iLCJMb3NzIG1hc2tpbmc6IHNldCBsYWJlbHMgdG8gLTEwMCBmb3IgRU9TIGFuZCBwYWRkaW5nIHBvc2l0aW9ucyBzbyBjcm9zc19lbnRyb3B5IGlnbm9yZXMgdGhlbTsgb25seSBkb2N1bWVudCBjb250ZW50IHRva2VucyBjb250cmlidXRlIGdyYWRpZW50cy4iLCJPdmVyZmxvdyBoYW5kbGluZzogaWYgYSBzaW5nbGUgZG9jdW1lbnQgZXhjZWVkcyBtYXhfbGVuZ3RoIGl0IG11c3QgYmUgc3BsaXQgYXQgc2VudGVuY2UgYm91bmRhcmllcyBvciB0cnVuY2F0ZWQg4oCUIG5ldmVyIHNpbGVudGx5IGRyb3BwZWQuIiwiUm9QRSBwb3NpdGlvbiBJRHM6IGFsd2F5cyByZXNldCB0byAwIGF0IGRvY3VtZW50IGJvdW5kYXJpZXMgdG8gYXZvaWQgc3B1cmlvdXMgbG9uZy1yYW5nZSBwb3NpdGlvbiBlbmNvZGluZyBhcnRpZmFjdHMgZnJvbSBjdW11bGF0aXZlIGluZGV4aW5nLiIsIkZpcnN0LWZpdC1kZWNyZWFzaW5nIChGRkQpIHNvcnRzIGRvY3VtZW50cyBieSBkZXNjZW5kaW5nIGxlbmd0aCBiZWZvcmUgcGFja2luZyDigJQgZW1waXJpY2FsbHkgMuKAkzUlIGhpZ2hlciB1dGlsaXphdGlvbiB0aGFuIGdyZWVkeSBvbiB0eXBpY2FsIGRpc3RyaWJ1dGlvbnMuIiwiVGhyb3VnaHB1dCBiZW5jaG1hcmtzIHNob3VsZCByZXBvcnQgdG9rZW5zLXBlci1zZWNvbmQgb24gY29udGVudCB0b2tlbnMgb25seSwgZXhjbHVkaW5nIHBhZGRpbmcsIGZvciBmYWlyIGNvbXBhcmlzb24gYWNyb3NzIGJhdGNoaW5nIHN0cmF0ZWdpZXMuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNob29zaW5nIGEgUGFja2luZyBTdHJhdGVneSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJpZ2h0IHBhY2tpbmcgc3RyYXRlZ3kgZGVwZW5kcyBvbiBoYXJkd2FyZSwgZnJhbWV3b3JrLCBhbmQgZGF0YXNldCBjaGFyYWN0ZXJpc3RpY3MuIEh1Z2dpbmcgRmFjZSBUUkwgU0ZUVHJhaW5lclx1MDAyN3MgYnVpbHQtaW4gcGFja2luZyB1c2VzIGdyZWVkeSBmaXJzdC1maXQgd2l0aCBibG9jay1kaWFnb25hbCBtYXNraW5nIGFuZCB3b3JrcyBvdXQtb2YtdGhlLWJveCB3aXRoIFBFRlQgYWRhcHRlcnMuIEZvciBwcmV0cmFpbmluZyBhdCBzY2FsZSwgY3VzdG9tIEZsYXNoIEF0dGVudGlvbiB2YXJsZW4ga2VybmVscyBnaXZlIHRoZSBoaWdoZXN0IHRocm91Z2hwdXQgYnV0IHJlcXVpcmUgbW9yZSBlbmdpbmVlcmluZy4gU2ltcGxlIHBhY2tpbmcgd2l0aG91dCBjcm9zcy1kb2N1bWVudCBtYXNraW5nIGlzIGluY29ycmVjdCBhbmQgc2hvdWxkIGJlIGF2b2lkZWQg4oCUIHRoZSBxdWFsaXR5IGRlZ3JhZGF0aW9uIGlzIHN1YnRsZSBhbmQgbWF5IG5vdCBhcHBlYXIgaW4gZWFybHkgdHJhaW5pbmcgbG9zcyBjdXJ2ZXMgYnV0IG1hbmlmZXN0cyBpbiBkb3duc3RyZWFtIGV2YWx1YXRpb25zIG9uIHRhc2tzIHJlcXVpcmluZyBwcmVjaXNlIGNvbnRleHQgYXR0cmlidXRpb24gYW5kIGxvbmctZm9ybSBjb2hlcmVuY2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlN0cmF0ZWd5IiwiVG9rZW4gVXRpbGl6YXRpb24iLCJDcm9zcy1Eb2MgSXNvbGF0aW9uIiwiSW1wbGVtZW50YXRpb24gQ29tcGxleGl0eSIsIlJlY29tbWVuZGVkIEZvciJdLCJyb3dzIjpbWyJOYWl2ZSBwYWRkaW5nIiwiNTDigJM3MCUiLCJOL0EgKG5vIHBhY2tpbmcpIiwiVHJpdmlhbCIsIkJhc2VsaW5lcywgdW5pZm9ybS1sZW5ndGggZGF0YXNldHMiXSxbIlNpbXBsZSBjb25jYXRlbmF0aW9uIChubyBtYXNrKSIsIjk14oCTOTklIiwiTm9uZSDigJQgY3Jvc3MtZG9jIGxlYWthZ2UiLCJMb3ciLCJOZXZlcjogaW50cm9kdWNlcyB0cmFpbmluZyBhcnRpZmFjdHMiXSxbIlBhY2tpbmcgKyBibG9jay1kaWFnb25hbCBtYXNrIiwiOTDigJM5NSUiLCJGdWxsIGlzb2xhdGlvbiIsIk1lZGl1bSIsIkZpbmUtdHVuaW5nLCBpbnN0cnVjdGlvbiB0dW5pbmcsIFNGVCJdLFsiRmxhc2ggQXR0ZW50aW9uIHZhcmxlbiIsIjEwMCUgKG5vIHBhZGRpbmcpIiwiRnVsbCBpc29sYXRpb24iLCJIaWdoIiwiTGFyZ2Utc2NhbGUgcHJldHJhaW5pbmcsIHByb2R1Y3Rpb24iXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJCbG9jay1EaWFnb25hbCBNYXNraW5nIElzIE5vbi1PcHRpb25hbCIsImNvbnRlbnQiOiJCbG9jay1kaWFnb25hbCBhdHRlbnRpb24gbWFza2luZyBwcmV2ZW50cyBjcm9zcy1kb2N1bWVudCBhdHRlbnRpb24gY29udGFtaW5hdGlvbiBpbiBwYWNrZWQgc2VxdWVuY2VzIOKAlCB3aXRob3V0IGl0LCB0aGUgbW9kZWwgc2VlcyB0b2tlbnMgZnJvbSBkb2N1bWVudCBBIGFzIGNvbnRleHQgZm9yIGRvY3VtZW50IEIsIHdoaWNoIGNhbiBjYXVzZSBzdWJ0bGUgYnV0IG1lYXN1cmFibGUgcXVhbGl0eSBkZWdyYWRhdGlvbiBvbiBsb25nLWZvcm0gdGFza3MuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Sequence Packing — Concatenating Short Sequences with Attention Masking

Variable-length text sequences create a fundamental efficiency problem for batch training: to assemble sequences into a rectangular tensor, shorter sequences must be padded to the length of the longest in the batch. A batch containing one 2048-token document and 31 documents of 64 tokens has 98% padding — 61,504 wasted tokens out of 63,488 total. Sequence packing solves this by concatenating multiple documents end-to-end into a single fixed-length context, recovering 90–98% token utilization and yielding 2–3x training throughput improvements in practice without any change to model architecture.

## The Padding Waste Problem

In standard padded batching, each batch is formed by sampling documents independently and padding every sequence to the batch maximum length. For typical NLP datasets — instruction tuning data, preference data, or web crawl with high length variance — average utilization is 50–70%. The compute used on padding tokens is entirely wasted: the attention mechanism processes them, the loss function ignores them via a loss mask, and the gradients are zero. For a GPU spending 40% of FLOPS on padding, packing alone is equivalent to a 1.67x hardware upgrade — free throughput from a software change.

## Document Packing Algorithm

The packing problem is a variant of bin packing: given documents of varying lengths and bins of capacity max_length, fill bins to minimize total bins and maximize utilization. First-fit-decreasing (FFD) is near-optimal but requires sorting by length descending. Greedy first-fit is simpler: iterate documents in arrival order, append each to the current bin if it fits, flush and open a new bin otherwise. For LLM pretraining data with natural length distributions, greedy packing achieves 85–95% utilization. Each document is followed by an EOS token as a separator, and any remainder in the final bin is padded with zeros.

```python
from typing import List, Tuple
import random

def greedy_pack_documents(tokenized_docs: List[List[int]], max_length: int,
                          eos_id: int = 2) -> List[Tuple[List[int], List[int]]]:
    """Greedy first-fit packing: concatenate docs+EOS until bin is full."""
    bins, cur_tokens, cur_docs = [], [], []
    for idx, doc in enumerate(tokenized_docs):
        chunk = doc + [eos_id]
        if len(cur_tokens) + len(chunk) > max_length:
            if cur_tokens:  # flush current bin with padding
                cur_tokens += [0] * (max_length - len(cur_tokens))
                bins.append((cur_tokens, cur_docs))
            cur_tokens, cur_docs = chunk[:max_length], [idx]
        else:
            cur_tokens.extend(chunk)
            cur_docs.append(idx)
    if cur_tokens:  # flush final bin
        cur_tokens += [0] * (max_length - len(cur_tokens))
        bins.append((cur_tokens, cur_docs))
    return bins

random.seed(42)
docs = [list(range(random.randint(50, 300))) for _ in range(200)]
packed = greedy_pack_documents(docs, max_length=512)
content_tokens = sum(len(d) for d in docs)
total_capacity = len(packed) * 512
print(f"Bins: {len(packed)}, token utilization: {content_tokens / total_capacity:.1%}")
print(f"Naive padded estimate: ~60% -- packing recovers ~{0.95 - 0.60:.0%} wasted compute")
```

## Block-Diagonal Attention Masking

Naive packing concatenates documents but allows attention across document boundaries — a token from document A can attend to tokens in document B. This leaks future context and corrupts causal language modeling: the loss on document B's first token can use document A's last token as context, which would never happen at inference. The fix is a block-diagonal attention mask: each document attends only to its own prior tokens (causal within the document), and all cross-document attention positions are set to negative infinity as an additive bias applied before softmax. This is the default in Hugging Face TRL's SFTTrainer when packing is enabled.

```python
import torch
from typing import List

def make_block_diagonal_mask(doc_lengths: List[int], device: str = "cpu") -> torch.Tensor:
    """Block-diagonal causal mask: within-doc causal attention, cross-doc = -inf."""
    T = sum(doc_lengths)
    mask = torch.full((T, T), float("-inf"), device=device)
    offset = 0
    for L in doc_lengths:
        mask[offset:offset+L, offset:offset+L] = torch.tril(torch.zeros(L, L))
        offset += L
    return mask  # additive bias added to attention logits before softmax

def packed_attention(q, k, v, doc_lengths):
    """Scaled dot-product attention with block-diagonal mask for packed sequences."""
    mask  = make_block_diagonal_mask(doc_lengths, device=q.device)
    scale = q.shape[-1] ** -0.5
    attn  = torch.softmax((q @ k.transpose(-2, -1)) * scale + mask, dim=-1)
    return attn @ v

# Three documents packed into one sequence of total length 256
doc_lengths = [80, 120, 56]
T = sum(doc_lengths)
q = k = v = torch.randn(1, T, 64)   # (batch=1, seq=256, dim=64)
out = packed_attention(q, k, v, doc_lengths)
print(f"Output shape: {out.shape}")  # (1, 256, 64)
mask = make_block_diagonal_mask(doc_lengths)
print(f"Cross-doc [tok 0 -> tok 81]: {mask[0, 81].item():.0f}")   # -inf
print(f"Within-doc [tok 0 -> tok 0]: {mask[0, 0].item():.0f}")   # 0.0
```

## Position ID Reset Strategies

When packing, each document's position IDs can be reset to 0 at each boundary (local positions) or allowed to continue incrementing across boundaries (cumulative positions). Reset position IDs are preferred for RoPE models: RoPE encodes relative distance via angular frequency, so the start of a new document at packed position 512 should be treated as position 0, not 512. Cumulative positions cause the model to believe the second document is 512 tokens into a single long sequence, introducing incorrect long-range positional biases that degrade quality on tasks requiring accurate position-sensitive reasoning. Reset IDs are the default in TRL and most production packing implementations.

```python
import torch
from typing import List

def build_position_ids(doc_lengths: List[int], strategy: str = "reset") -> torch.Tensor:
    """
    Build position IDs for a packed sequence.
    strategy='reset'     : each document starts at position 0 (local positions)
    strategy='cumulative': positions continue across document boundaries
    """
    if strategy == "reset":
        positions = [pos for L in doc_lengths for pos in range(L)]
    elif strategy == "cumulative":
        positions = list(range(sum(doc_lengths)))
    else:
        raise ValueError(f"Unknown strategy: {strategy!r}")
    return torch.tensor(positions, dtype=torch.long)

doc_lengths = [5, 4, 6]
reset_ids = build_position_ids(doc_lengths, strategy="reset")
cumul_ids = build_position_ids(doc_lengths, strategy="cumulative")
print(f"Reset:      {reset_ids.tolist()}")
print(f"Cumulative: {cumul_ids.tolist()}")
# reset:      [0,1,2,3,4, 0,1,2,3, 0,1,2,3,4,5]
# cumulative: [0,1,2,3,4, 5,6,7,8, 9,10,11,12,13,14]
max_pos_cumul = sum(doc_lengths) - 1
print(f"Max cumulative position: {max_pos_cumul} -- verify below model max_seq_len")
print("Reset preferred: RoPE sees local doc positions, no spurious long-range bias")
```

## Throughput Comparison

The throughput improvement from packing is directly proportional to utilization improvement. For a dataset where naive padding achieves 60% utilization and packing achieves 95%, the effective throughput gain is 95/60 ≈ 1.58x. The actual wall-clock speedup is typically larger because packing reduces the total number of forward passes for the same data, reducing fixed overhead from data loading, optimizer steps, and gradient synchronization in distributed training. Flash Attention 2 natively supports variable-length packed sequences via its varlen kernel, eliminating even the small residual padding within bins and achieving true 100% compute utilization.

```python
import torch
import time
import random
from typing import List

def padded_batch_utilization(seq_lens: List[int]) -> tuple:
    """Compute token utilization and simulate compute time with padded batching."""
    max_len   = max(seq_lens)
    useful    = sum(seq_lens)
    allocated = max_len * len(seq_lens)
    start = time.perf_counter()
    _     = torch.randn(len(seq_lens), max_len, 128) @ torch.randn(128, 128)
    return useful / allocated, time.perf_counter() - start

def packed_batch_utilization(seq_lens: List[int], max_length: int = 2048) -> tuple:
    """Compute token utilization and simulate compute time with greedy packing."""
    total  = sum(seq_lens)
    n_bins = (total + max_length - 1) // max_length
    start  = time.perf_counter()
    _      = torch.randn(n_bins, max_length, 128) @ torch.randn(128, 128)
    return total / (n_bins * max_length), time.perf_counter() - start

random.seed(0)
seq_lens = [random.randint(64, 400) for _ in range(128)]
pad_util,  pad_t  = padded_batch_utilization(seq_lens)
pack_util, pack_t = packed_batch_utilization(seq_lens)
print(f"{'Method':<22} {'Utilization':>12} {'Latency (ms)':>14}")
print(f"{'Padded batching':<22} {pad_util:>11.1%} {pad_t * 1000:>13.1f}")
print(f"{'Sequence packing':<22} {pack_util:>11.1%} {pack_t * 1000:>13.1f}")
print(f"Throughput gain: {pack_util / pad_util:.2f}x")
```

## Flash Attention 2 and Variable-Length Sequences

Flash Attention 2 (Dao et al. 2023) includes dedicated variable-length sequence kernels: flash_attn_varlen_qkvpacked_func and flash_attn_varlen_func accept cumulative sequence lengths (cu_seqlens) rather than a padded tensor, processing the packed sequence without any padding overhead at all. This achieves true 100% utilization in the attention kernel. The interface expects a 1D tensor of token IDs with all documents concatenated, a cu_seqlens tensor marking document boundaries, and max_seqlen for kernel configuration. This is the most efficient packing implementation available and is used in production pretraining at Meta, Mistral AI, and others.

- Flash Attention varlen kernel accepts cu_seqlens = cumulative sum of doc lengths, e.g. [0, 80, 200, 256] for three docs of lengths 80, 120, 56.
- Loss masking: set labels to -100 for EOS and padding positions so cross_entropy ignores them; only document content tokens contribute gradients.
- Overflow handling: if a single document exceeds max_length it must be split at sentence boundaries or truncated — never silently dropped.
- RoPE position IDs: always reset to 0 at document boundaries to avoid spurious long-range position encoding artifacts from cumulative indexing.
- First-fit-decreasing (FFD) sorts documents by descending length before packing — empirically 2–5% higher utilization than greedy on typical distributions.
- Throughput benchmarks should report tokens-per-second on content tokens only, excluding padding, for fair comparison across batching strategies.

## Choosing a Packing Strategy

The right packing strategy depends on hardware, framework, and dataset characteristics. Hugging Face TRL SFTTrainer's built-in packing uses greedy first-fit with block-diagonal masking and works out-of-the-box with PEFT adapters. For pretraining at scale, custom Flash Attention varlen kernels give the highest throughput but require more engineering. Simple packing without cross-document masking is incorrect and should be avoided — the quality degradation is subtle and may not appear in early training loss curves but manifests in downstream evaluations on tasks requiring precise context attribution and long-form coherence.

| Strategy | Token Utilization | Cross-Doc Isolation | Implementation Complexity | Recommended For |
| --- | --- | --- | --- | --- |
| Naive padding | 50–70% | N/A (no packing) | Trivial | Baselines, uniform-length datasets |
| Simple concatenation (no mask) | 95–99% | None — cross-doc leakage | Low | Never: introduces training artifacts |
| Packing + block-diagonal mask | 90–95% | Full isolation | Medium | Fine-tuning, instruction tuning, SFT |
| Flash Attention varlen | 100% (no padding) | Full isolation | High | Large-scale pretraining, production |

> **Block-Diagonal Masking Is Non-Optional**: Block-diagonal attention masking prevents cross-document attention contamination in packed sequences — without it, the model sees tokens from document A as context for document B, which can cause subtle but measurable quality degradation on long-form tasks.

---

