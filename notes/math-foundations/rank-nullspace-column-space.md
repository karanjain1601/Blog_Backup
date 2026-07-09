---
title: "Rank, Nullspace, Column Space, and Row Space"
slug: "rank-nullspace-column-space"
description: "The four fundamental subspaces, rank-nullity theorem, numerical rank via SVD, overdetermined and underdetermined linear systems."
tags: ["linear-algebra", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXZlcnkgbWF0cml4IGRlZmluZXMgZm91ciBmdW5kYW1lbnRhbCBzdWJzcGFjZXMg4oCUIGNvbHVtbiBzcGFjZSwgcm93IHNwYWNlLCBudWxsIHNwYWNlLCBhbmQgbGVmdCBudWxsIHNwYWNlIOKAlCB0aGF0IHRvZ2V0aGVyIGNvbXBsZXRlbHkgY2hhcmFjdGVyaXplIHRoZSBtYXRyaXgncyBhY3Rpb24gYXMgYSBsaW5lYXIgbWFwLiBVbmRlcnN0YW5kaW5nIHRoZXNlIHN1YnNwYWNlcywgdGhlIHJhbmstbnVsbGl0eSB0aGVvcmVtLCBhbmQgaG93IHRvIGNvbXB1dGUgbnVtZXJpY2FsIHJhbmsgcmV2ZWFscyB3aHkgbGluZWFyIHN5c3RlbXMgYXJlIHNvbHZhYmxlIG9yIG5vdCwgd2h5IHJlZ3Jlc3Npb24gd29ya3MsIGFuZCBob3cgY29tcHJlc3NlZCBzZW5zaW5nIGNhbiByZWNvdmVyIHNwYXJzZSBzaWduYWxzIGZyb20gZmFyIGZld2VyIG1lYXN1cmVtZW50cyB0aGFuIGNsYXNzaWNhbCB0aGVvcnkgc3VnZ2VzdHMuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEZvdXIgRnVuZGFtZW50YWwgU3Vic3BhY2VzIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBtYXRyaXggKipBKiogKG3Dl24pLCB0aGUgZm91ciBmdW5kYW1lbnRhbCBzdWJzcGFjZXMgYXJlOlxuXG4xLiAqKkNvbHVtbiBzcGFjZSAocmFuZ2UpKiogQygqKkEqKikg4oqGIOKEneG1kDogc3BhbiBvZiBhbGwgY29sdW1ucyBvZiAqKkEqKiA9IHsqKkF4KiogOiAqKngqKiDiiIgg4oSd4oG/fS4gRGltZW5zaW9uID0gcmFuaygqKkEqKilcbjIuICoqTnVsbCBzcGFjZSAoa2VybmVsKSoqIE4oKipBKiopIOKKhiDihJ3igb86IHsqKngqKiA6ICoqQXgqKiA9ICoqMCoqfS4gRGltZW5zaW9uID0gbiAtIHJhbmsoKipBKiopXG4zLiAqKlJvdyBzcGFjZSoqIEMoKipB4bWAKiopIOKKhiDihJ3igb86IHNwYW4gb2YgYWxsIHJvd3Mgb2YgKipBKiogPSBjb2x1bW4gc3BhY2Ugb2YgKipB4bWAKiouIERpbWVuc2lvbiA9IHJhbmsoKipBKiopXG40LiAqKkxlZnQgbnVsbCBzcGFjZSoqIE4oKipB4bWAKiopIOKKhiDihJ3htZA6IHsqKnkqKiA6ICoqQeG1gHkqKiA9ICoqMCoqfS4gRGltZW5zaW9uID0gbSAtIHJhbmsoKipBKiopXG5cblN0cmFuZydzIGZ1bmRhbWVudGFsIHRoZW9yZW06IE4oKipBKiopIOKKpSBDKCoqQeG1gCoqKSBpbiDihJ3igb8sIGFuZCBOKCoqQeG1gCoqKSDiiqUgQygqKkEqKikgaW4g4oSd4bWQLiBUaGUgZm91ciBzdWJzcGFjZXMgY29tZSBpbiB0d28gb3J0aG9nb25hbCBjb21wbGVtZW50YXJ5IHBhaXJzLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkubGluYWxnIGltcG9ydCBudWxsX3NwYWNlXG5cbkEgPSBucC5hcnJheShbWzEuLCAyLiwgMy5dLFxuICAgICAgICAgICAgICBbNC4sIDUuLCA2Ll0sXG4gICAgICAgICAgICAgIFs3LiwgOC4sIDkuXV0pICAgIyByYW5rIDIgKHJvdzMgPSByb3cxICsgcm93MiByb3VnaGx5KVxuXG5yID0gbnAubGluYWxnLm1hdHJpeF9yYW5rKEEpXG5wcmludCgnUmFuazonLCByKSAgICAgICAgICAgICAgIyAyXG5cbiMgQ29sdW1uIHNwYWNlOiBmaXJzdCByIGxlZnQgc2luZ3VsYXIgdmVjdG9yc1xuVSwgcywgVnQgPSBucC5saW5hbGcuc3ZkKEEpXG5jb2xfc3BhY2UgPSBVWzosIDpyXSAgICAgICAgICAjICgzLCAyKVxucHJpbnQoJ0NvbHVtbiBzcGFjZSBiYXNpczpcXG4nLCBjb2xfc3BhY2UpXG5cbiMgTnVsbCBzcGFjZTogcmlnaHQgc2luZ3VsYXIgdmVjdG9ycyBmb3IgemVybyBzaW5ndWxhciB2YWx1ZXNcbm51bGwgPSBWdFtyOl0uVCAgICAgICAgICAgICAgICMgKDMsIDEpIC0tIHRoZSBudWxsIHNwYWNlIGJhc2lzXG5wcmludCgnTnVsbCBzcGFjZSB2ZWN0b3I6JywgbnVsbC5UKVxucHJpbnQoJ0EgQCBudWxsX3ZlYzonLCBBIEAgbnVsbFs6LCAwXSkgICMgc2hvdWxkIGJlIH4wXG5cbiMgUm93IHNwYWNlOiBmaXJzdCByIHJpZ2h0IHNpbmd1bGFyIHZlY3RvcnNcbnJvd19zcGFjZSA9IFZ0WzpyXS5UICAgICAgICAgICMgKDMsIDIpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIFJhbmstTnVsbGl0eSBUaGVvcmVtIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgKipyYW5rLW51bGxpdHkgdGhlb3JlbSoqIGlzIG9uZSBvZiB0aGUgbW9zdCBmdW5kYW1lbnRhbCByZXN1bHRzIGluIGxpbmVhciBhbGdlYnJhOlxuXG4gIHJhbmsoKipBKiopICsgbnVsbGl0eSgqKkEqKikgPSBuXG5cbndoZXJlIG4gaXMgdGhlIG51bWJlciBvZiBjb2x1bW5zLCByYW5rKCoqQSoqKSA9IGRpbShjb2x1bW4gc3BhY2UpID0gZGltKHJvdyBzcGFjZSksIGFuZCBudWxsaXR5KCoqQSoqKSA9IGRpbShudWxsIHNwYWNlKS4gVGhlIGlucHV0IHNwYWNlIOKEneKBvyBpcyBwYXJ0aXRpb25lZCBpbnRvIHR3byBvcnRob2dvbmFsIHN1YnNwYWNlczogdGhlIHJvdyBzcGFjZSAod2hpY2ggKipBKiogbWFwcyBub24tdHJpdmlhbGx5KSBhbmQgdGhlIG51bGwgc3BhY2UgKHdoaWNoICoqQSoqIGNvbGxhcHNlcyB0byB6ZXJvKS5cblxuQ29uc2VxdWVuY2VzOlxuLSBJZiByYW5rKCoqQSoqKSA9IG4gKGZ1bGwgY29sdW1uIHJhbmspOiBudWxsaXR5ID0gMCwgc28gKipBeCA9IDAqKiBvbmx5IGZvciAqKnggPSAwKiouIFRoZSBzeXN0ZW0gKipBeCA9IGIqKiBoYXMgYXQgbW9zdCBvbmUgc29sdXRpb24uXG4tIElmIHJhbmsoKipBKiopIDwgbjogdGhlcmUgYXJlIGluZmluaXRlbHkgbWFueSBzb2x1dGlvbnMgKGlmIGNvbnNpc3RlbnQpIOKAlCB0aGUgbnVsbCBzcGFjZSBnaXZlcyB0aGUgZGVncmVlcyBvZiBmcmVlZG9tLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZ1bGwgUmFuayB2cyBSYW5rLURlZmljaWVudCBNYXRyaWNlcyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBtYXRyaXggKipBKiogKG3Dl24pIGlzICoqZnVsbCByYW5rKiogaWYgcmFuaygqKkEqKikgPSBtaW4obSxuKS4gVHdvIHR5cGVzIG9mIGZ1bGwgcmFuazpcblxuLSAqKkZ1bGwgY29sdW1uIHJhbmsqKjogcmFuayA9IG4g4omkIG0uIEFsbCBjb2x1bW5zIGFyZSBsaW5lYXJseSBpbmRlcGVuZGVudC4gTnVsbCBzcGFjZSBpcyB0cml2aWFsLiBUaGUgc3lzdGVtICoqQXggPSBiKiogaGFzIGEgdW5pcXVlIHNvbHV0aW9uICh3aGVuIGNvbnNpc3RlbnQpLiBUaGUgbm9ybWFsIGVxdWF0aW9ucyAqKihB4bWAQSkqKiBhcmUgaW52ZXJ0aWJsZS4gVGhpcyBpcyB0aGUgY2FzZSBmb3Igd2VsbC1kZXNpZ25lZCByZWdyZXNzaW9uIHByb2JsZW1zIHdoZXJlIGZlYXR1cmVzIGFyZSBub3QgcGVyZmVjdGx5IGNvbGxpbmVhci5cblxuLSAqKkZ1bGwgcm93IHJhbmsqKjogcmFuayA9IG0g4omkIG4uIEFsbCByb3dzIGFyZSBsaW5lYXJseSBpbmRlcGVuZGVudC4gKipBeCA9IGIqKiBpcyBjb25zaXN0ZW50IGZvciBldmVyeSAqKmIqKiDiiIgg4oSd4bWQLiBUaGVyZSBhcmUgbi1tIGRlZ3JlZXMgb2YgZnJlZWRvbSBpbiB0aGUgc29sdXRpb24uIFRoaXMgaXMgdGhlIHVuZGVyZGV0ZXJtaW5lZCBjYXNlLlxuXG4qKlJhbmstZGVmaWNpZW50KiogKG5vdCBmdWxsIHJhbmspOiB0aGUgY29sdW1uIHNwYWNlIGlzIGEgcHJvcGVyIHN1YnNwYWNlIG9mIOKEneG1kCwgbWVhbmluZyBzb21lICoqYioqIHZlY3RvcnMgaGF2ZSBubyBzb2x1dGlvbi4gSW5kaWNhdGVzIGxpbmVhciBkZXBlbmRlbmNlIGFtb25nIGZlYXR1cmVzIChtdWx0aWNvbGxpbmVhcml0eSkuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTnVtZXJpY2FsIFJhbmsgdmlhIFNWRCJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gZXhhY3QgYXJpdGhtZXRpYywgcmFuayBpcyB0aGUgY291bnQgb2Ygbm9uemVybyBlaWdlbnZhbHVlcy4gQnV0IGZsb2F0aW5nLXBvaW50IGNvbXB1dGF0aW9uIG1ha2VzIG5lYXJseS16ZXJvIHZhbHVlcyBhbWJpZ3VvdXMuICoqTnVtZXJpY2FsIHJhbmsqKiB1c2VzIHNpbmd1bGFyIHZhbHVlcyBhbmQgYSB0aHJlc2hvbGQ6XG5cbiAgbnVtZXJpY2FsX3JhbmsoKipBKiopID0gI3vPg+G1oiA6IM+D4bWiID4gz4R9XG5cbndoZXJlIM+EID0gbWF4KG0sbikgwrcgz4NfbWF4IMK3IM61X21hY2hpbmUgKHdpdGggzrVfbWFjaGluZSDiiYggMi4yw5cxMOKBu8K54oG2IGZvciBmbG9hdDY0KS4gVGhpcyBpcyBleGFjdGx5IHdoYXQgYG51bXB5LmxpbmFsZy5tYXRyaXhfcmFua2AgdXNlcy4gTmV2ZXIgZGV0ZXJtaW5lIHJhbmsgYnkgY29tcHV0aW5nIHRoZSBkZXRlcm1pbmFudCAobnVtZXJpY2FsbHkgdW5zdGFibGUg4oCUIGNhbiBiZSBub256ZXJvIGZvciBwcmFjdGljYWxseSBzaW5ndWxhciBtYXRyaWNlcykgb3IgYnkgR2F1c3NpYW4gZWxpbWluYXRpb24gd2l0aG91dCBjYXJlZnVsIHBpdm90aW5nLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBOdW1lcmljYWwgcmFuayBleGFtcGxlXG4jIEJ1aWxkIHJhbmstMiBtYXRyaXggYW5kIGFkZCB0aW55IG5vaXNlXG5VID0gbnAucmFuZG9tLnJhbmRuKDUsIDIpXG5WID0gbnAucmFuZG9tLnJhbmRuKDUsIDIpXG5BID0gVSBAIFYuVCArIDFlLTE0ICogbnAucmFuZG9tLnJhbmRuKDUsIDUpICAjIG5vbWluYWxseSByYW5rLTJcblxuc3ZkX3ZhbHMgPSBucC5saW5hbGcuc3ZkKEEsIGNvbXB1dGVfdXY9RmFsc2UpXG5wcmludCgnU2luZ3VsYXIgdmFsdWVzOicsIHN2ZF92YWxzKSAgIyBmaXJzdCAyIGxhcmdlLCByZXN0IH4xZS0xNFxuXG4jIG51bXB5IG1hdHJpeF9yYW5rIHVzZXMgcmNvbmQgdGhyZXNob2xkXG5wcmludCgnbnVtcHkgcmFuazonLCBucC5saW5hbGcubWF0cml4X3JhbmsoQSkpICAgICAgICAjIDIgKGNvcnJlY3QpXG5wcmludCgnU3RyaWN0IHJhbms6JywgbnAuc3VtKHN2ZF92YWxzID4gMWUtMTApKSAgICAgICAgICMgMlxucHJpbnQoJ1Blcm1pc3NpdmUgcmFuazonLCBucC5zdW0oc3ZkX3ZhbHMgPiAxZS0xNSkpICAgICAjIG1pZ2h0IGJlIDUhXG5cbiMgQ29uZGl0aW9uIG51bWJlcjogcmF0aW8gb2YgbGFyZ2VzdCB0byBzbWFsbGVzdCBzaW5ndWxhciB2YWx1ZVxuY29uZCA9IHN2ZF92YWxzWzBdIC8gc3ZkX3ZhbHNbLTFdXG5wcmludChmJ0NvbmRpdGlvbiBudW1iZXI6IHtjb25kOi4yZX0nKSAgIyBodWdlIC0tIGlsbC1jb25kaXRpb25lZCJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJkZXRlcm1pbmVkIFN5c3RlbXM6IE5vcm1hbCBFcXVhdGlvbnMgYW5kIFJlZ3Jlc3Npb24ifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuICoqb3ZlcmRldGVybWluZWQgc3lzdGVtKiogKipBeCA9IGIqKiAobSA+IG4sIG1vcmUgZXF1YXRpb25zIHRoYW4gdW5rbm93bnMpIGlzIGdlbmVyYWxseSBpbmNvbnNpc3RlbnQg4oCUIG5vIGV4YWN0IHNvbHV0aW9uIGV4aXN0cy4gVGhlICoqbGVhc3Qtc3F1YXJlcyBzb2x1dGlvbioqIG1pbmltaXplcyB8fCoqQXggLSBiKip8fOKCgsKyIGFuZCBpcyBnaXZlbiBieSB0aGUgKipub3JtYWwgZXF1YXRpb25zKio6XG5cbiAgKipB4bWAQXgqKiogPSAqKkHhtYBiKiogIOKGkiAgKip4KioqID0gKCoqQeG1gEEqKinigbvCuSoqQeG1gGIqKiAod2hlbiBmdWxsIGNvbHVtbiByYW5rKVxuXG5UaGlzIGlzIHRoZSBoZWFydCBvZiBsaW5lYXIgcmVncmVzc2lvbjogZml0dGluZyBhIG1vZGVsIHRvIG4gZGF0YSBwb2ludHMgd2l0aCBkIDwgbiBwYXJhbWV0ZXJzLiBUaGUgcHJlZGljdGlvbiAqKkF4KioqIGlzIHRoZSBwcm9qZWN0aW9uIG9mICoqYioqIG9udG8gdGhlIGNvbHVtbiBzcGFjZSBvZiAqKkEqKi5cblxuTnVtZXJpY2FsIGJlc3QgcHJhY3RpY2U6IG5ldmVyIHNvbHZlIHRoZSBub3JtYWwgZXF1YXRpb25zIGRpcmVjdGx5IChjb21wdXRpbmcgKipB4bWAQSoqIHNxdWFyZXMgdGhlIGNvbmRpdGlvbiBudW1iZXIsIGRvdWJsaW5nIHRoZSBwcmVjaXNpb24gbG9zcykuIEluc3RlYWQsIHVzZSBRUiBkZWNvbXBvc2l0aW9uIChgbnAubGluYWxnLmxzdHNxYCkgb3IgU1ZELCB3aGljaCBhcmUgYm90aCBtb3JlIG51bWVyaWNhbGx5IHN0YWJsZS4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgTGluZWFyIHJlZ3Jlc3Npb24gYXMgb3ZlcmRldGVybWluZWQgc3lzdGVtXG5ucC5yYW5kb20uc2VlZCgwKVxubiwgZCA9IDEwMCwgM1xuWCA9IG5wLmNvbHVtbl9zdGFjayhbbnAub25lcyhuKSwgbnAucmFuZG9tLnJhbmRuKG4sIGQtMSldKSAgIyAoMTAwLCAzKVxudHJ1ZV93ID0gbnAuYXJyYXkoWzEuLCAyLiwgLTEuXSlcbnkgPSBYIEAgdHJ1ZV93ICsgbnAucmFuZG9tLnJhbmRuKG4pICogMC41XG5cbiMgTWV0aG9kIDE6IE5vcm1hbCBlcXVhdGlvbnMgKGxlc3Mgc3RhYmxlKVxud19ub3JtYWwgPSBucC5saW5hbGcuc29sdmUoWC5UIEAgWCwgWC5UIEAgeSlcbnByaW50KCdOb3JtYWwgZXEgc29sdXRpb246Jywgd19ub3JtYWwpXG5cbiMgTWV0aG9kIDI6IGxzdHNxIChTVkQtYmFzZWQsIHByZWZlcnJlZClcbndfbHN0c3EsIHJlc2lkdWFscywgcmFuaywgc3YgPSBucC5saW5hbGcubHN0c3EoWCwgeSwgcmNvbmQ9Tm9uZSlcbnByaW50KCdsc3RzcSBzb2x1dGlvbjonLCB3X2xzdHNxKVxucHJpbnQoJ1Jhbms6JywgcmFuaywgJyAgU2luZ3VsYXIgdmFsdWVzOicsIHN2KVxucHJpbnQoJ01hdGNoPycsIG5wLmFsbGNsb3NlKHdfbm9ybWFsLCB3X2xzdHNxLCBhdG9sPTFlLTYpKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuZGVyZGV0ZXJtaW5lZCBTeXN0ZW1zOiBDb21wcmVzc2VkIFNlbnNpbmcifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuICoqdW5kZXJkZXRlcm1pbmVkIHN5c3RlbSoqICoqQXggPSBiKiogKG0gPCBuLCBmZXdlciBlcXVhdGlvbnMgdGhhbiB1bmtub3ducykgaGFzIGluZmluaXRlbHkgbWFueSBzb2x1dGlvbnMgd2hlbiBjb25zaXN0ZW50LiBUaGUgc29sdXRpb24gc2V0IGlzIGFuIGFmZmluZSBzdWJzcGFjZTogeCA9IHhfcGFydGljdWxhciArIHhfbnVsbCwgd2hlcmUgeF9udWxsIGxpZXMgaW4gTigqKkEqKikuXG5cblRoZSAqKm1pbmltdW0tbm9ybSBzb2x1dGlvbioqIHgqID0gKipB4bWAKiooKipBQeG1gCoqKeKBu8K5YiBzZWxlY3RzIHRoZSB1bmlxdWUgc29sdXRpb24gd2l0aCBzbWFsbGVzdCBMMiBub3JtLiBCdXQgKipjb21wcmVzc2VkIHNlbnNpbmcqKiBzaG93cyBzb21ldGhpbmcgcmVtYXJrYWJsZTogaWYgeCBpcyAqKnNwYXJzZSoqIChmZXcgbm9uemVybyBlbnRyaWVzKSwgYW5kICoqQSoqIHNhdGlzZmllcyB0aGUgKipSZXN0cmljdGVkIElzb21ldHJ5IFByb3BlcnR5IChSSVApKiosIHRoZSBzcGFyc2Ugc29sdXRpb24gY2FuIGJlIHVuaXF1ZWx5IHJlY292ZXJlZCBieSBzb2x2aW5nOlxuXG4gIG1pbiB8fHh8fOKCgSAgc3ViamVjdCB0byBBeCA9IGJcblxuVGhpcyBMMSBtaW5pbWl6YXRpb24gKGEgbGluZWFyIHByb2dyYW0pIHJlY292ZXJzIHRoZSBzcGFyc2UgdmVjdG9yIGV2ZW4gd2l0aCBtIDw8IG4gbWVhc3VyZW1lbnRzLCBhcyBsb25nIGFzIHRoZSBudW1iZXIgb2Ygbm9uemVyb3MgayBzYXRpc2ZpZXMgayDiibIgbS8obG9nIG4pLiBUaGlzIGlzIHRoZSBtYXRoZW1hdGljYWwgZm91bmRhdGlvbiBvZiBtb2Rlcm4gc2Vuc29yIGRlc2lnbiwgTVJJIGFjY2VsZXJhdGlvbiwgYW5kIHNwYXJzZSBhdXRvZW5jb2RlcnMgaW4gTUwuIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG4jIENvbXByZXNzZWQgc2Vuc2luZzogcmVjb3ZlciBhIGstc3BhcnNlIHNpZ25hbCBmcm9tIG0gPCBuIG1lYXN1cmVtZW50c1xubnAucmFuZG9tLnNlZWQoNDIpXG5uLCBtLCBrID0gMTAwLCA0MCwgNSAgICAjIDEwMCB1bmtub3ducywgNDAgbWVhc3VyZW1lbnRzLCA1IG5vbnplcm9cblxuIyBUcnVlIHNwYXJzZSBzaWduYWxcbnhfdHJ1ZSA9IG5wLnplcm9zKG4pXG5pZHggPSBucC5yYW5kb20uY2hvaWNlKG4sIGssIHJlcGxhY2U9RmFsc2UpXG54X3RydWVbaWR4XSA9IG5wLnJhbmRvbS5yYW5kbihrKVxuXG4jIFNlbnNpbmcgbWF0cml4IChHYXVzc2lhbiByYW5kb20gc2F0aXNmaWVzIFJJUCB3aXRoIGhpZ2ggcHJvYmFiaWxpdHkpXG5BID0gbnAucmFuZG9tLnJhbmRuKG0sIG4pIC8gbnAuc3FydChtKVxuYiA9IEEgQCB4X3RydWUgICMgbWVhc3VyZW1lbnRzXG5cbiMgTDIgbWluaW11bSBub3JtOiB4KiA9IEFeVCAoQUFeVCleLTEgYiAocHNldWRvLWludmVyc2UpXG54X2wyID0gQS5UIEAgbnAubGluYWxnLnNvbHZlKEEgQCBBLlQsIGIpXG5wcmludChmJ0wyIG1pbi1ub3JtIGVycm9yOiB7bnAubGluYWxnLm5vcm0oeF9sMiAtIHhfdHJ1ZSk6LjRmfScpXG5wcmludChmJ0wyIG5vbnplcm9zICg+MWUtMyk6IHtucC5zdW0obnAuYWJzKHhfbDIpID4gMWUtMyl9JykgICMgZGVuc2UhXG5cbiMgTDEgbWluaW1pemF0aW9uIHZpYSBzY2lweSAoYmFzaXMgcHVyc3VpdClcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IGxpbnByb2cgICMgc2ltcGxpZmllZCAtLSBpbiBwcmFjdGljZSB1c2UgY3Z4cHlcbnByaW50KCdMMSBwdXJzdWl0IHdvdWxkIHJlY292ZXIgdGhlIHNwYXJzZSBzb2x1dGlvbiAoc2VlIENWWFBZL1NQR0wxKScpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29sdW1uIFNwYWNlIGFuZCBMaW5lYXIgSW5kZXBlbmRlbmNlIGluIEZlYXR1cmUgRW5naW5lZXJpbmcifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVuZGVyc3RhbmRpbmcgdGhlIGNvbHVtbiBzcGFjZSBpcyBjcnVjaWFsIGZvciBwcmFjdGljYWwgTUw6XG5cbi0gKipNdWx0aWNvbGxpbmVhcml0eSoqOiBXaGVuIHR3byBmZWF0dXJlcyBhcmUgbmVhcmx5IGxpbmVhcmx5IGRlcGVuZGVudCAoZS5nLiwgJ2luY29tZScgYW5kICdzYWxhcnknIGluIHRoZSBzYW1lIGRhdGFzZXQpLCB0aGUgZGVzaWduIG1hdHJpeCBpcyBuZWFyIHJhbmstZGVmaWNpZW50LiAqKkHhtYBBKiogaXMgbmVhci1zaW5ndWxhciwgbWFraW5nIHRoZSBub3JtYWwgZXF1YXRpb25zIGlsbC1jb25kaXRpb25lZC4gUmlkZ2UgcmVncmVzc2lvbiAoYWRkaW5nIM67SSkgZml4ZXMgdGhpcyBieSBlbnN1cmluZyB0aGUgR3JhbSBtYXRyaXggaXMgUEQuXG4tICoqT25lLWhvdCBlbmNvZGluZyoqOiBBIGZ1bGwgc2V0IG9mIG9uZS1ob3QgZmVhdHVyZXMgZm9yIGEgY2F0ZWdvcmljYWwgdmFyaWFibGUgd2l0aCBDIGNhdGVnb3JpZXMgY3JlYXRlcyBhIHJhbmstQy0xIG1hdHJpeCAodGhlIGNvbHVtbnMgc3VtIHRvIHRoZSBhbGwtb25lcyB2ZWN0b3IsIGNyZWF0aW5nIGxpbmVhciBkZXBlbmRlbmNlKS4gU3RhbmRhcmQgcHJhY3RpY2U6IGRyb3Agb25lIGNhdGVnb3J5IG9yIHVzZSBhbiBpbnRlcmNlcHQtZnJlZSBtb2RlbC5cbi0gKipQb2x5bm9taWFsIGZlYXR1cmVzKio6IEFkZGluZyBkZWdyZWUtZCBwb2x5bm9taWFsIGZlYXR1cmVzIGNhbiBjcmVhdGUgbmVhci1saW5lYXIgZGVwZW5kZW5jZSBiZXR3ZWVuIGNvbHVtbnMsIGVzcGVjaWFsbHkgZm9yIGNsb3NlbHkgc3BhY2VkIGRhdGEgcG9pbnRzIOKAlCBsZWFkaW5nIHRvIG51bWVyaWNhbCBpc3N1ZXMuIn0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJCZXdhcmUgUGVyZmVjdCBNdWx0aWNvbGxpbmVhcml0eSIsImNvbnRlbnQiOiJJZiBvbmUgZmVhdHVyZSBjb2x1bW4gaXMgYW4gZXhhY3QgbGluZWFyIGNvbWJpbmF0aW9uIG9mIG90aGVycywgdGhlIGRlc2lnbiBtYXRyaXggaXMgcmFuay1kZWZpY2llbnQsIChB4bWAQSkgaXMgc2luZ3VsYXIsIGFuZCB0aGUgbm9ybWFsIGVxdWF0aW9ucyBoYXZlIG5vIHVuaXF1ZSBzb2x1dGlvbi4gU3ltcHRvbXM6IG5wLmxpbmFsZy5zb2x2ZSByYWlzZXMgYSBzaW5ndWxhciBtYXRyaXggZXJyb3I7IHNjaWtpdC1sZWFybidzIExpbmVhclJlZ3Jlc3Npb24gcmV0dXJucyBuZWFyLWluZmluaXRlIGNvZWZmaWNpZW50cy4gRGlhZ25vc2lzOiBjaGVjayBjb25kaXRpb24gbnVtYmVyIChucC5saW5hbGcuY29uZChYKSkuIEZpeDogcmVtb3ZlIHJlZHVuZGFudCBmZWF0dXJlcywgdXNlIFJpZGdlIHJlZ3Jlc3Npb24sIG9yIGFwcGx5IFNWRC1iYXNlZCByZWdyZXNzaW9uLiJ9LAogIHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJTeXN0ZW0iLCJTaGFwZSIsIlJhbmsiLCJTb2x1dGlvbnMiLCJNTCBSZWxldmFuY2UiXSwicm93cyI6W1siU3F1YXJlLCBmdWxsIHJhbmsiLCJtPW4sIHI9biIsIm4iLCJVbmlxdWUgc29sdXRpb24iLCJEaXJlY3QgbWF0cml4IGludmVyc2lvbiJdLFsiT3ZlcmRldGVybWluZWQiLCJtPm4sIHI9biIsIm4iLCJVbmlxdWUgbGVhc3Qtc3F1YXJlcyIsIkxpbmVhciByZWdyZXNzaW9uIChub3JtYWwgZXF1YXRpb25zKSJdLFsiVW5kZXJkZXRlcm1pbmVkIiwibTxuLCByPW0iLCJtIiwiSW5maW5pdGUgKGFmZmluZSBzdWJzcGFjZSkiLCJDb21wcmVzc2VkIHNlbnNpbmcsIGVtYmVkZGluZyBzcGFjZXMiXSxbIlJhbmstZGVmaWNpZW50IChvdmVyKSIsIm0+biwgcjxuIiwicjxuIiwiTFMgaW4gY29sdW1uIHNwYWNlIG9ubHkiLCJNdWx0aWNvbGxpbmVhciBmZWF0dXJlcyJdLFsiUmFuay1kZWZpY2llbnQgKHVuZGVyKSIsIm08biwgcjxtIiwicjxtIiwiTWlnaHQgYmUgaW5jb25zaXN0ZW50IiwiRGVnZW5lcmF0ZSBzeXN0ZW0iXV19Cl0K"
---

# Rank, Nullspace, Column Space, and Row Space

Every matrix defines four fundamental subspaces — column space, row space, null space, and left null space — that together completely characterize the matrix's action as a linear map. Understanding these subspaces, the rank-nullity theorem, and how to compute numerical rank reveals why linear systems are solvable or not, why regression works, and how compressed sensing can recover sparse signals from far fewer measurements than classical theory suggests.

## The Four Fundamental Subspaces

For a matrix **A** (m×n), the four fundamental subspaces are:

1. **Column space (range)** C(**A**) ⊆ ℝᵐ: span of all columns of **A** = {**Ax** : **x** ∈ ℝⁿ}. Dimension = rank(**A**)
2. **Null space (kernel)** N(**A**) ⊆ ℝⁿ: {**x** : **Ax** = **0**}. Dimension = n - rank(**A**)
3. **Row space** C(**Aᵀ**) ⊆ ℝⁿ: span of all rows of **A** = column space of **Aᵀ**. Dimension = rank(**A**)
4. **Left null space** N(**Aᵀ**) ⊆ ℝᵐ: {**y** : **Aᵀy** = **0**}. Dimension = m - rank(**A**)

Strang's fundamental theorem: N(**A**) ⊥ C(**Aᵀ**) in ℝⁿ, and N(**Aᵀ**) ⊥ C(**A**) in ℝᵐ. The four subspaces come in two orthogonal complementary pairs.

```python
import numpy as np
from scipy.linalg import null_space

A = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.]])   # rank 2 (row3 = row1 + row2 roughly)

r = np.linalg.matrix_rank(A)
print('Rank:', r)              # 2

# Column space: first r left singular vectors
U, s, Vt = np.linalg.svd(A)
col_space = U[:, :r]          # (3, 2)
print('Column space basis:\n', col_space)

# Null space: right singular vectors for zero singular values
null = Vt[r:].T               # (3, 1) -- the null space basis
print('Null space vector:', null.T)
print('A @ null_vec:', A @ null[:, 0])  # should be ~0

# Row space: first r right singular vectors
row_space = Vt[:r].T          # (3, 2)
```

## The Rank-Nullity Theorem

The **rank-nullity theorem** is one of the most fundamental results in linear algebra:

  rank(**A**) + nullity(**A**) = n

where n is the number of columns, rank(**A**) = dim(column space) = dim(row space), and nullity(**A**) = dim(null space). The input space ℝⁿ is partitioned into two orthogonal subspaces: the row space (which **A** maps non-trivially) and the null space (which **A** collapses to zero).

Consequences:
- If rank(**A**) = n (full column rank): nullity = 0, so **Ax = 0** only for **x = 0**. The system **Ax = b** has at most one solution.
- If rank(**A**) < n: there are infinitely many solutions (if consistent) — the null space gives the degrees of freedom.

## Full Rank vs Rank-Deficient Matrices

A matrix **A** (m×n) is **full rank** if rank(**A**) = min(m,n). Two types of full rank:

- **Full column rank**: rank = n ≤ m. All columns are linearly independent. Null space is trivial. The system **Ax = b** has a unique solution (when consistent). The normal equations **(AᵀA)** are invertible. This is the case for well-designed regression problems where features are not perfectly collinear.

- **Full row rank**: rank = m ≤ n. All rows are linearly independent. **Ax = b** is consistent for every **b** ∈ ℝᵐ. There are n-m degrees of freedom in the solution. This is the underdetermined case.

**Rank-deficient** (not full rank): the column space is a proper subspace of ℝᵐ, meaning some **b** vectors have no solution. Indicates linear dependence among features (multicollinearity).

## Numerical Rank via SVD

In exact arithmetic, rank is the count of nonzero eigenvalues. But floating-point computation makes nearly-zero values ambiguous. **Numerical rank** uses singular values and a threshold:

  numerical_rank(**A**) = #{σᵢ : σᵢ > τ}

where τ = max(m,n) · σ_max · ε_machine (with ε_machine ≈ 2.2×10⁻¹⁶ for float64). This is exactly what `numpy.linalg.matrix_rank` uses. Never determine rank by computing the determinant (numerically unstable — can be nonzero for practically singular matrices) or by Gaussian elimination without careful pivoting.

```python
import numpy as np

# Numerical rank example
# Build rank-2 matrix and add tiny noise
U = np.random.randn(5, 2)
V = np.random.randn(5, 2)
A = U @ V.T + 1e-14 * np.random.randn(5, 5)  # nominally rank-2

svd_vals = np.linalg.svd(A, compute_uv=False)
print('Singular values:', svd_vals)  # first 2 large, rest ~1e-14

# numpy matrix_rank uses rcond threshold
print('numpy rank:', np.linalg.matrix_rank(A))        # 2 (correct)
print('Strict rank:', np.sum(svd_vals > 1e-10))         # 2
print('Permissive rank:', np.sum(svd_vals > 1e-15))     # might be 5!

# Condition number: ratio of largest to smallest singular value
cond = svd_vals[0] / svd_vals[-1]
print(f'Condition number: {cond:.2e}')  # huge -- ill-conditioned
```

## Overdetermined Systems: Normal Equations and Regression

An **overdetermined system** **Ax = b** (m > n, more equations than unknowns) is generally inconsistent — no exact solution exists. The **least-squares solution** minimizes ||**Ax - b**||₂² and is given by the **normal equations**:

  **AᵀAx*** = **Aᵀb**  →  **x*** = (**AᵀA**)⁻¹**Aᵀb** (when full column rank)

This is the heart of linear regression: fitting a model to n data points with d < n parameters. The prediction **Ax*** is the projection of **b** onto the column space of **A**.

Numerical best practice: never solve the normal equations directly (computing **AᵀA** squares the condition number, doubling the precision loss). Instead, use QR decomposition (`np.linalg.lstsq`) or SVD, which are both more numerically stable.

```python
import numpy as np

# Linear regression as overdetermined system
np.random.seed(0)
n, d = 100, 3
X = np.column_stack([np.ones(n), np.random.randn(n, d-1)])  # (100, 3)
true_w = np.array([1., 2., -1.])
y = X @ true_w + np.random.randn(n) * 0.5

# Method 1: Normal equations (less stable)
w_normal = np.linalg.solve(X.T @ X, X.T @ y)
print('Normal eq solution:', w_normal)

# Method 2: lstsq (SVD-based, preferred)
w_lstsq, residuals, rank, sv = np.linalg.lstsq(X, y, rcond=None)
print('lstsq solution:', w_lstsq)
print('Rank:', rank, '  Singular values:', sv)
print('Match?', np.allclose(w_normal, w_lstsq, atol=1e-6))
```

## Underdetermined Systems: Compressed Sensing

An **underdetermined system** **Ax = b** (m < n, fewer equations than unknowns) has infinitely many solutions when consistent. The solution set is an affine subspace: x = x_particular + x_null, where x_null lies in N(**A**).

The **minimum-norm solution** x* = **Aᵀ**(**AAᵀ**)⁻¹b selects the unique solution with smallest L2 norm. But **compressed sensing** shows something remarkable: if x is **sparse** (few nonzero entries), and **A** satisfies the **Restricted Isometry Property (RIP)**, the sparse solution can be uniquely recovered by solving:

  min ||x||₁  subject to Ax = b

This L1 minimization (a linear program) recovers the sparse vector even with m << n measurements, as long as the number of nonzeros k satisfies k ≲ m/(log n). This is the mathematical foundation of modern sensor design, MRI acceleration, and sparse autoencoders in ML.

```python
import numpy as np

# Compressed sensing: recover a k-sparse signal from m < n measurements
np.random.seed(42)
n, m, k = 100, 40, 5    # 100 unknowns, 40 measurements, 5 nonzero

# True sparse signal
x_true = np.zeros(n)
idx = np.random.choice(n, k, replace=False)
x_true[idx] = np.random.randn(k)

# Sensing matrix (Gaussian random satisfies RIP with high probability)
A = np.random.randn(m, n) / np.sqrt(m)
b = A @ x_true  # measurements

# L2 minimum norm: x* = A^T (AA^T)^-1 b (pseudo-inverse)
x_l2 = A.T @ np.linalg.solve(A @ A.T, b)
print(f'L2 min-norm error: {np.linalg.norm(x_l2 - x_true):.4f}')
print(f'L2 nonzeros (>1e-3): {np.sum(np.abs(x_l2) > 1e-3)}')  # dense!

# L1 minimization via scipy (basis pursuit)
from scipy.optimize import linprog  # simplified -- in practice use cvxpy
print('L1 pursuit would recover the sparse solution (see CVXPY/SPGL1)')
```

## Column Space and Linear Independence in Feature Engineering

Understanding the column space is crucial for practical ML:

- **Multicollinearity**: When two features are nearly linearly dependent (e.g., 'income' and 'salary' in the same dataset), the design matrix is near rank-deficient. **AᵀA** is near-singular, making the normal equations ill-conditioned. Ridge regression (adding λI) fixes this by ensuring the Gram matrix is PD.
- **One-hot encoding**: A full set of one-hot features for a categorical variable with C categories creates a rank-C-1 matrix (the columns sum to the all-ones vector, creating linear dependence). Standard practice: drop one category or use an intercept-free model.
- **Polynomial features**: Adding degree-d polynomial features can create near-linear dependence between columns, especially for closely spaced data points — leading to numerical issues.

> **[WARNING] Beware Perfect Multicollinearity**
>
> If one feature column is an exact linear combination of others, the design matrix is rank-deficient, (AᵀA) is singular, and the normal equations have no unique solution. Symptoms: np.linalg.solve raises a singular matrix error; scikit-learn's LinearRegression returns near-infinite coefficients. Diagnosis: check condition number (np.linalg.cond(X)). Fix: remove redundant features, use Ridge regression, or apply SVD-based regression.

| System | Shape | Rank | Solutions | ML Relevance |
| --- | --- | --- | --- | --- |
| Square, full rank | m=n, r=n | n | Unique solution | Direct matrix inversion |
| Overdetermined | m>n, r=n | n | Unique least-squares | Linear regression (normal equations) |
| Underdetermined | m<n, r=m | m | Infinite (affine subspace) | Compressed sensing, embedding spaces |
| Rank-deficient (over) | m>n, r<n | r<n | LS in column space only | Multicollinear features |
| Rank-deficient (under) | m<n, r<m | r<m | Might be inconsistent | Degenerate system |
