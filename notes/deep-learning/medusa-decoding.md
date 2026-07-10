---
title: "Medusa: Multiple Decoding Heads for Parallel Token Generation"
slug: "medusa-decoding"
description: "Adding multiple lightweight prediction heads to a frozen LLM that each predict tokens several positions ahead, enabling parallel verification of multi-token continuations."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWVkdXNhIChDYWkgZXQgYWwuIDIwMjQsIFRvZ2V0aGVyIEFJKSBpcyBhIHNwZWN1bGF0aXZlIGRlY29kaW5nIGZyYW1ld29yayB0aGF0IHJlcGxhY2VzIHRoZSBzZXBhcmF0ZSBkcmFmdCBtb2RlbCB3aXRoIG11bHRpcGxlIGxpZ2h0d2VpZ2h0IHByZWRpY3Rpb24gaGVhZHMgYXBwZW5kZWQgdG8gYSBmcm96ZW4gYmFzZSBMTE0uIEVhY2ggaGVhZCBpcyBhIGNvbXBhY3QgdHdvLWxheWVyIE1MUCBzaXR0aW5nIG9uIHRvcCBvZiB0aGUgbGFzdCB0cmFuc2Zvcm1lciBibG9ja1x1MDAyN3MgaGlkZGVuIHN0YXRlcywgaW5kZXBlbmRlbnRseSBwcmVkaWN0aW5nIHRoZSB0b2tlbiBhdCBvZmZzZXQgKzEsICsyLCB1cCB0byArSyBwb3NpdGlvbnMgYWhlYWQuIEJlY2F1c2UgdGhlIGhlYWRzIHNoYXJlIHRoZSBiYXNlIG1vZGVsXHUwMDI3cyByaWNoIHJlcHJlc2VudGF0aW9ucywgdGhleSBjYW4gYmUgdHJhaW5lZCB0byBuZWFyLW9yYWNsZSBhY2NlcHRhbmNlIHJhdGVzIHdpdGggYXMgbGl0dGxlIGFzIDAuMyUgYWRkaXRpb25hbCBwYXJhbWV0ZXJzLiBBdCBpbmZlcmVuY2UgdGltZSwgYWxsIGhlYWRzIGdlbmVyYXRlIGNhbmRpZGF0ZSB0b2tlbnMgc2ltdWx0YW5lb3VzbHkgaW4gYSBzaW5nbGUgYWRkaXRpb25hbCBmb3J3YXJkIHBhc3Mg4oCUIG5vIHNlcGFyYXRlIGRyYWZ0IG1vZGVsIGNhbGwgcmVxdWlyZWQg4oCUIGFuZCB0aGUgcmVzdWx0aW5nIHRyZWUgb2YgY2FuZGlkYXRlcyBpcyB2ZXJpZmllZCBieSB0aGUgYmFzZSBtb2RlbCB1c2luZyBhIG1vZGlmaWVkIHRyZWUgYXR0ZW50aW9uIG1hc2sgdGhhdCBzY29yZXMgYWxsIGh5cG90aGVzZXMgaW4gb25lIGJhdGNoZWQgZm9yd2FyZCBwYXNzLiBUaGUgcHJhY3RpY2FsIHJlc3VsdCBpcyBhIDIuMuKAkzIuOMOXIHRocm91Z2hwdXQgaW1wcm92ZW1lbnQgb24gY2hhdCB3b3JrbG9hZHMgd2l0aCBubyBtZWFzdXJhYmxlIGRlZ3JhZGF0aW9uIGluIG91dHB1dCBxdWFsaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBhdXRvcmVncmVzc2l2ZSBkZWNvZGluZyBnZW5lcmF0ZXMgb25lIHRva2VuIHBlciBmb3J3YXJkIHBhc3MsIG1ha2luZyBpdCBtZW1vcnktYmFuZHdpZHRoIGJvdW5kOiBlYWNoIHN0ZXAgcmVhZHMgYWxsIG1vZGVsIHdlaWdodHMgZnJvbSBIQk0gZXZlbiB0aG91Z2ggb25seSBhIHRpbnkgZnJhY3Rpb24gb2YgdG90YWwgY29tcHV0ZSBjYXBhY2l0eSBpcyB1c2VkLiBTcGVjdWxhdGl2ZSBkZWNvZGluZyBzaWRlc3RlcHMgdGhpcyBieSB1c2luZyBhIGZhc3RlciBkcmFmdCBtb2RlbCB0byBwcm9wb3NlIG11bHRpcGxlIHRva2VucyBhbmQgdGhlIHRhcmdldCBtb2RlbCB0byB2ZXJpZnkgdGhlbSBpbiBwYXJhbGxlbCDigJQgYnV0IG1haW50YWluaW5nIGEgc2VwYXJhdGUgZHJhZnQgbW9kZWwgZG91YmxlcyBkZXBsb3ltZW50IGNvbXBsZXhpdHkgYW5kIG1lbW9yeSBmb290cHJpbnQuIE1lZHVzYSBlbGltaW5hdGVzIHRoZSBkcmFmdCBtb2RlbCBlbnRpcmVseTogdGhlIHByZWRpY3Rpb24gaGVhZHMgYXJlIHRyYWluZWQgb25jZSwgZnJvemVuIGFsb25nc2lkZSB0aGUgYmFzZSBtb2RlbCwgYW5kIGFkZCBuZWdsaWdpYmxlIG92ZXJoZWFkIHRvIHRoZSBzdGFuZGFyZCBpbmZlcmVuY2UgZ3JhcGguIFRoZSB0eXBpY2FsIGFjY2VwdGFuY2UgcmF0ZSBmb3IgdGhlIGZpcnN0IE1lZHVzYSBoZWFkIGlzIDYw4oCTODAlLCBtZWFuaW5nIG1vc3QgZ2VuZXJhdGVkIHRva2VucyBhcmUgYWNjZXB0ZWQsIHlpZWxkaW5nIG1lYXN1cmVkIHNwZWVkdXBzIG9mIDIuMOKAkzMuMMOXIG9uIGNoYXQgd29ya2xvYWRzLiBUaGUgYXBwcm9hY2ggd2FzIHBvcHVsYXJpc2VkIGFsb25nc2lkZSBWaWN1bmEgbW9kZWxzIGFuZCBpbnRlZ3JhdGVzIGRpcmVjdGx5IHdpdGggdkxMTSBhbmQgU0dMYW5nIGluZmVyZW5jZSBzZXJ2ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFyY2hpdGVjdHVyZTogTXVsdGlwbGUgTE0gSGVhZHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVhY2ggTWVkdXNhIGhlYWQgayAoZm9yIGsgPSAxLCDigKYsIEspIGlzIGEgdHdvLWxheWVyIE1MUCB3aXRoIGEgTGF5ZXJOb3JtIGFwcGxpZWQgdG8gdGhlIGxhc3QgaGlkZGVuIHN0YXRlIGhfdCBiZWZvcmUgdGhlIGZpcnN0IGxpbmVhciBsYXllci4gVGhlIG91dHB1dCBvZiBoZWFkIGsgaXMgYSBmdWxsIHZvY2FidWxhcnkgZGlzdHJpYnV0aW9uIG92ZXIgdGhlIHRva2VuIGF0IHBvc2l0aW9uIHQray4gRHVyaW5nIGEgZHJhZnQgc3RlcCwgdGhlIGJhc2UgbW9kZWwgZ2VuZXJhdGVzIHRoZSB0b2tlbiBhdCB0KzEgZnJvbSBpdHMgb3duIGxvZ2l0cyAodGhlIHN0YW5kYXJkIExNIGhlYWQpLCB3aGlsZSBzaW11bHRhbmVvdXNseSBhbGwgSyBNZWR1c2EgaGVhZHMgcHJvZHVjZSBjYW5kaWRhdGUgZGlzdHJpYnV0aW9ucyBmb3IgcG9zaXRpb25zIHQrMiB0aHJvdWdoIHQrSysxIOKAlCBhbGwgY29tcHV0ZWQgZnJvbSB0aGUgc2FtZSBzaW5nbGUgZm9yd2FyZCBwYXNzIG92ZXIgdGhlIGN1cnJlbnQgY29udGV4dC4gVGhlIGhlYWRzIGFyZSBwYXJhbWV0ZXJpc2VkIGlkZW50aWNhbGx5IGJ1dCB0cmFpbmVkIGluZGVwZW5kZW50bHksIGFuZCB0aGVyZSBpcyBubyB3ZWlnaHQgc2hhcmluZyBiZXR3ZWVuIGhlYWRzLiBUaGlzIGFyY2hpdGVjdHVyZSBlbnN1cmVzIHRoYXQgaGVhZCBrIHNwZWNpYWxpc2VzIGluIHByZWRpY3RpbmcgdG9rZW5zIGsgc3RlcHMgYWhlYWQgZ2l2ZW4gdGhlIGJhc2UgbW9kZWxcdTAwMjdzIGNvbnRleHR1YWwgcmVwcmVzZW50YXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvQ29uZmlnXG5mcm9tIHR5cGluZyBpbXBvcnQgTGlzdCwgVHVwbGVcblxuY2xhc3MgTWVkdXNhSGVhZChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlR3by1sYXllciBNTFAgcHJlZGljdGluZyB0b2tlbiBhdCBwb3NpdGlvbiB0K2sgZnJvbSBsYXN0IGhpZGRlbiBzdGF0ZS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaGlkZGVuX3NpemU6IGludCwgdm9jYWJfc2l6ZTogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxheWVyTm9ybShoaWRkZW5fc2l6ZSksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuX3NpemUsIGhpZGRlbl9zaXplLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW5fc2l6ZSwgdm9jYWJfc2l6ZSwgYmlhcz1GYWxzZSksXG4gICAgICAgIClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGhpZGRlbjogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgcmV0dXJuIHNlbGYubmV0KGhpZGRlbikgICMgKEIsIFMsIHZvY2FiX3NpemUpXG5cbmNsYXNzIE1lZHVzYVdpdGhIZWFkcyhubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkZyb3plbiBiYXNlIExMTSBwbHVzIEsgdHJhaW5hYmxlIE1lZHVzYSBoZWFkcyBmb3IgcG9zaXRpb25zIHQrMSB0byB0K0suXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG1vZGVsX25hbWU6IHN0ciwgbnVtX2hlYWRzOiBpbnQgPSA1KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmFzZSA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgICAgICBmb3IgcCBpbiBzZWxmLmJhc2UucGFyYW1ldGVycygpOlxuICAgICAgICAgICAgcC5yZXF1aXJlc19ncmFkXyhGYWxzZSkgICAgICAgICAgICMgZnJlZXplIGFsbCBiYXNlIG1vZGVsIHdlaWdodHNcbiAgICAgICAgSCA9IHNlbGYuYmFzZS5jb25maWcuaGlkZGVuX3NpemVcbiAgICAgICAgViA9IHNlbGYuYmFzZS5jb25maWcudm9jYWJfc2l6ZVxuICAgICAgICBzZWxmLm1lZHVzYV9oZWFkcyA9IG5uLk1vZHVsZUxpc3QoXG4gICAgICAgICAgICBbTWVkdXNhSGVhZChILCBWKSBmb3IgXyBpbiByYW5nZShudW1faGVhZHMpXVxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBpbnB1dF9pZHM6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSBUdXBsZVt0b3JjaC5UZW5zb3IsIExpc3RbdG9yY2guVGVuc29yXV06XG4gICAgICAgIG91dHB1dHMgPSBzZWxmLmJhc2UoaW5wdXRfaWRzLCBvdXRwdXRfaGlkZGVuX3N0YXRlcz1UcnVlKVxuICAgICAgICBsYXN0X2hpZGRlbiA9IG91dHB1dHMuaGlkZGVuX3N0YXRlc1stMV0gICAgICAgICAgICAgICAgICAgICAgIyAoQiwgUywgSClcbiAgICAgICAgbWVkdXNhX2xvZ2l0cyA9IFtoZWFkKGxhc3RfaGlkZGVuKSBmb3IgaGVhZCBpbiBzZWxmLm1lZHVzYV9oZWFkc10gICMgSyB4IChCLFMsVilcbiAgICAgICAgcmV0dXJuIG91dHB1dHMubG9naXRzLCBtZWR1c2FfbG9naXRzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVkdXNhIFRyZWUgQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSYXRoZXIgdGhhbiB2ZXJpZnlpbmcgY2FuZGlkYXRlIHRva2VucyBvbmUgYnkgb25lLCBNZWR1c2EgY29uc3RydWN0cyBhIHRva2VuIHRyZWUgZnJvbSBoZWFkIHByZWRpY3Rpb25zIGFuZCB2ZXJpZmllcyBhbGwgYnJhbmNoZXMgc2ltdWx0YW5lb3VzbHkgdXNpbmcgYSBjdXN0b20gYXR0ZW50aW9uIG1hc2suIEZvciBLIGhlYWRzIGVhY2ggdGFraW5nIHRoZSB0b3AtcCBjYW5kaWRhdGVzLCB0aGUgdHJlZSBoYXMgYXQgbW9zdCB0b3AtcF5LIGxlYXZlcy4gVGhlIHRyZWUgYXR0ZW50aW9uIG1hc2sgaXMgYSBib29sZWFuIG1hdHJpeCBvdmVyIGFsbCBjYW5kaWRhdGUgcG9zaXRpb25zOiBwb3NpdGlvbiBqIGNhbiBhdHRlbmQgdG8gcG9zaXRpb24gaSBvbmx5IGlmIGkgaXMgYW4gYW5jZXN0b3Igb2YgaiBpbiB0aGUgdHJlZS4gVGhpcyBtYXNrIHJlcGxhY2VzIHRoZSBzdGFuZGFyZCBjYXVzYWwgbWFzayBkdXJpbmcgdGhlIHZlcmlmaWNhdGlvbiBmb3J3YXJkIHBhc3MsIGFsbG93aW5nIHRoZSBiYXNlIG1vZGVsIHRvIHNjb3JlIGFsbCBjYW5kaWRhdGUgY29udGludWF0aW9ucyBpbiBhIHNpbmdsZSBiYXRjaGVkIGNhbGwg4oCUIHRoZSBzYW1lIGNvbXB1dGUgY29zdCBhcyB2ZXJpZnlpbmcgYSBzaW5nbGUgY29udGludWF0aW9uLiBBIHBhdGggdGhyb3VnaCB0aGUgdHJlZSBjb3JyZXNwb25kcyB0byBhIG11bHRpLXRva2VuIGNvbnRpbnVhdGlvbiBoeXBvdGhlc2lzOiBpZiBhIHBhdGggc3Vydml2ZXMgdmVyaWZpY2F0aW9uIChlYWNoIHRva2VuIG1hdGNoZXMgdGhlIGJhc2UgbW9kZWxcdTAwMjdzIGdyZWVkeSBvciBzYW1wbGVkIGNob2ljZSBhdCB0aGF0IGRlcHRoKSwgYWxsIHRva2VucyBvbiB0aGUgcGF0aCBhcmUgYWNjZXB0ZWQgc2ltdWx0YW5lb3VzbHksIG11bHRpcGx5aW5nIGVmZmVjdGl2ZSB0aHJvdWdocHV0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBpdGVydG9vbHNcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBUdXBsZVxuXG5kZWYgYnVpbGRfbWVkdXNhX3RyZWUoXG4gICAgbWVkdXNhX2xvZ2l0czogTGlzdFt0b3JjaC5UZW5zb3JdLFxuICAgIHRvcF9rOiBpbnQgPSAzLFxuKSAtXHUwMDNlIFR1cGxlW3RvcmNoLlRlbnNvciwgdG9yY2guVGVuc29yXTpcbiAgICBcIlwiXCJcbiAgICBCdWlsZCBjYW5kaWRhdGUgdG9rZW4gdHJlZSBhbmQgdHJlZSBhdHRlbnRpb24gbWFzayBmcm9tIE1lZHVzYSBoZWFkIG91dHB1dHMuXG4gICAgbWVkdXNhX2xvZ2l0czogSyB0ZW5zb3JzIGVhY2ggKDEsIDEsIFYpIOKAlCBsb2dpdHMgZm9yIHBvc2l0aW9ucyB0KzEgLi4gdCtLLlxuICAgIFJldHVybnMgKGNhbmRpZGF0ZXMsIHRyZWVfbWFzayk6IChOLCkgdG9rZW4gaWRzIGFuZCAoTiwgTikgYm9vbCBhdHRlbnRpb24gbWFzay5cbiAgICBcIlwiXCJcbiAgICAjIENvbGxlY3QgdG9wLWsgdG9rZW4gY2FuZGlkYXRlcyBmcm9tIGVhY2ggaGVhZFxuICAgIGhlYWRfdG9wayA9IFtcbiAgICAgICAgdG9yY2gudG9wayhsZ1swLCAtMV0sIHRvcF9rKS5pbmRpY2VzLnRvbGlzdCgpXG4gICAgICAgIGZvciBsZyBpbiBtZWR1c2FfbG9naXRzXG4gICAgXVxuICAgICMgRW51bWVyYXRlIGFsbCBwYXRocyB0aHJvdWdoIHRoZSB0cmVlIChDYXJ0ZXNpYW4gcHJvZHVjdClcbiAgICBwYXRocyA9IGxpc3QoaXRlcnRvb2xzLnByb2R1Y3QoKmhlYWRfdG9waykpICAjIGxpc3Qgb2YgSy10dXBsZXNcbiAgICBOID0gbGVuKHBhdGhzKVxuICAgICMgVHJlZSBhdHRlbnRpb24gbWFzazogcG9zaXRpb24gaiBhdHRlbmRzIHRvIGkgaWYgcGF0aF9pIGlzIGEgcHJlZml4IG9mIHBhdGhfalxuICAgIG1hc2sgPSB0b3JjaC56ZXJvcyhOLCBOLCBkdHlwZT10b3JjaC5ib29sKVxuICAgIGZvciBqLCBwaiBpbiBlbnVtZXJhdGUocGF0aHMpOlxuICAgICAgICBmb3IgaSwgcGkgaW4gZW51bWVyYXRlKHBhdGhzKTpcbiAgICAgICAgICAgIGRlcHRoID0gbWluKGogKyAxLCBpICsgMSlcbiAgICAgICAgICAgIGlmIHR1cGxlKHBpWzpkZXB0aF0pID09IHR1cGxlKHBqWzpkZXB0aF0pIGFuZCBpIFx1MDAzYz0gajpcbiAgICAgICAgICAgICAgICBtYXNrW2osIGldID0gVHJ1ZVxuICAgICMgRmlyc3QgdG9rZW4gb2YgZWFjaCBwYXRoIGlzIHRoZSBjYW5kaWRhdGUgZnJvbSBoZWFkLTFcbiAgICBjYW5kaWRhdGVzID0gdG9yY2gudGVuc29yKFtwWzBdIGZvciBwIGluIHBhdGhzXSlcbiAgICByZXR1cm4gY2FuZGlkYXRlcywgbWFza1xuXG5kdW1teV9sb2dpdHMgPSBbdG9yY2gucmFuZG4oMSwgMSwgMzIwMDApIGZvciBfIGluIHJhbmdlKDMpXVxuY2FuZHMsIHRtYXNrID0gYnVpbGRfbWVkdXNhX3RyZWUoZHVtbXlfbG9naXRzLCB0b3Bfaz0zKVxucHJpbnQoZlwiVHJlZSBub2Rlczoge2xlbihjYW5kcyl9LCBtYXNrIHNoYXBlOiB7dHVwbGUodG1hc2suc2hhcGUpfVwiKVxucHJpbnQoZlwiTm9uLXplcm8gbWFzayBlbnRyaWVzOiB7dG1hc2suc3VtKCkuaXRlbSgpfSBvZiB7dG1hc2subnVtZWwoKX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyB0aGUgTWVkdXNhIEhlYWRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNZWR1c2EgaGVhZHMgYXJlIHRyYWluZWQgaW5kZXBlbmRlbnRseSBvZiB0aGUgYmFzZSBtb2RlbCBvbiBpbnN0cnVjdGlvbi10dW5pbmcgZGF0YS4gVGhlIHRyYWluaW5nIG9iamVjdGl2ZSBpcyBwZXItaGVhZCBjcm9zcy1lbnRyb3B5OiBoZWFkIGsgbWluaW1pc2VzIHRoZSBjcm9zcy1lbnRyb3B5IGxvc3MgYmV0d2VlbiBpdHMgcHJlZGljdGVkIGRpc3RyaWJ1dGlvbiBhbmQgdGhlIGdyb3VuZCB0cnV0aCB0b2tlbiBhdCBvZmZzZXQgaysxIGluIHRoZSBzZXF1ZW5jZS4gQmVjYXVzZSBlYWNoIGhlYWQgcHJlZGljdHMgYSBkaWZmZXJlbnQgb2Zmc2V0LCB0aGV5IGFyZSB0cmFpbmVkIHdpdGggc2hpZnRlZCB0YXJnZXQgc2VxdWVuY2VzIOKAlCBoZWFkLTEgdGFyZ2V0cyB0b2tlbnMgc2hpZnRlZCBieSAxLCBoZWFkLTIgYnkgMiwgYW5kIHNvIG9uLiBUaGUgYmFzZSBtb2RlbCBpcyBrZXB0IGZyb3plbiB0aHJvdWdob3V0LCBzbyBpdHMgaGlkZGVuIHN0YXRlcyBzZXJ2ZSBhcyBzdGF0aWMsIGZpeGVkIGZlYXR1cmVzLiBUcmFpbmluZyBjb252ZXJnZXMgaW4gb25lIHRvIHRocmVlIGVwb2NocyBvbiBtb2RlcmF0ZSBpbnN0cnVjdGlvbiBkYXRhc2V0cyAoU2hhcmVHUFQsIEFscGFjYSwgTE1TWVMtQ2hhdC0xTSkgYW5kIGNhbiBiZSBjb21wbGV0ZWQgb24gYSBzaW5nbGUgQTEwMCBpbiB1bmRlciBzaXggaG91cnMgZm9yIGEgN0IgbW9kZWwuIFRoZSBwZXItaGVhZCBhY2NlcHRhbmNlIHJhdGUgb24gYSBoZWxkLW91dCB2YWxpZGF0aW9uIHNldCBpcyB0aGUga2V5IG1ldHJpYyB0byB0cmFjazogaGVhZC0xIHNob3VsZCByZWFjaCA2NeKAkzc1JSwgd2l0aCBhY2NlcHRhbmNlIGRyb3BwaW5nIHJvdWdobHkgMTUgcGVyY2VudGFnZSBwb2ludHMgcGVyIGFkZGl0aW9uYWwgaGVhZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFMb2FkZXJcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0XG5cbmRlZiB0cmFpbl9tZWR1c2FfaGVhZHMoXG4gICAgbW9kZWwsXG4gICAgdHJhaW5fbG9hZGVyOiBEYXRhTG9hZGVyLFxuICAgIG51bV9oZWFkczogaW50ID0gNSxcbiAgICBscjogZmxvYXQgPSAxZS0zLFxuICAgIGVwb2NoczogaW50ID0gMSxcbikgLVx1MDAzZSBMaXN0W2Zsb2F0XTpcbiAgICBcIlwiXCJGcmVlemUgYmFzZSBtb2RlbCwgdHJhaW4gTWVkdXNhIGhlYWRzIHdpdGggcGVyLWhlYWQgY3Jvc3MtZW50cm9weSBsb3NzZXMuXCJcIlwiXG4gICAgb3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbVcoXG4gICAgICAgIFtwIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWRdLFxuICAgICAgICBscj1sciwgd2VpZ2h0X2RlY2F5PTAuMDEsXG4gICAgKVxuICAgIHBlcl9oZWFkX2xvc3MgPSBbMC4wXSAqIG51bV9oZWFkc1xuICAgIGZvciBlcG9jaCBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICBmb3IgYmF0Y2ggaW4gdHJhaW5fbG9hZGVyOlxuICAgICAgICAgICAgaW5wdXRfaWRzID0gYmF0Y2hbXHUwMDI3aW5wdXRfaWRzXHUwMDI3XVxuICAgICAgICAgICAgXywgbWVkdXNhX2xvZ2l0cyA9IG1vZGVsKGlucHV0X2lkcylcbiAgICAgICAgICAgIHRvdGFsX2xvc3MgPSB0b3JjaC50ZW5zb3IoMC4wLCByZXF1aXJlc19ncmFkPVRydWUpXG4gICAgICAgICAgICBmb3IgaywgaGVhZF9sb2dpdHMgaW4gZW51bWVyYXRlKG1lZHVzYV9sb2dpdHMpOlxuICAgICAgICAgICAgICAgIHRhcmdldCA9IGlucHV0X2lkc1s6LCBrICsgMTpdICAgICAgICAgICAgICAgICAgIyBzaGlmdCB0YXJnZXQgYnkgaysxXG4gICAgICAgICAgICAgICAgcHJlZCAgID0gaGVhZF9sb2dpdHNbOiwgOi0oayArIDEpLCA6XSAgICAgICAgICAjIGFsaWduIHNlcXVlbmNlIGxlbmd0aFxuICAgICAgICAgICAgICAgIGxvc3NfayA9IEYuY3Jvc3NfZW50cm9weShcbiAgICAgICAgICAgICAgICAgICAgcHJlZC5yZXNoYXBlKC0xLCBwcmVkLnNpemUoLTEpKSwgdGFyZ2V0LnJlc2hhcGUoLTEpLCBpZ25vcmVfaW5kZXg9LTEwMFxuICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgICAgICB0b3RhbF9sb3NzID0gdG90YWxfbG9zcyArIGxvc3Nfa1xuICAgICAgICAgICAgICAgIHBlcl9oZWFkX2xvc3Nba10gKz0gbG9zc19rLml0ZW0oKVxuICAgICAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgICAgICB0b3RhbF9sb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICBwZXJfaGVhZF9sb3NzID0gW2wgLyAoZXBvY2hzICogbGVuKHRyYWluX2xvYWRlcikpIGZvciBsIGluIHBlcl9oZWFkX2xvc3NdXG4gICAgZm9yIGssIGx2IGluIGVudW1lcmF0ZShwZXJfaGVhZF9sb3NzKTpcbiAgICAgICAgcHJpbnQoZlwiICBIZWFkIHtrKzF9IChvZmZzZXQgK3trKzF9KTogYXZnIENFIGxvc3MgPSB7bHY6LjRmfVwiKVxuICAgIHJldHVybiBwZXJfaGVhZF9sb3NzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWNjZXB0YW5jZSB3aXRoIFR5cGljYWwgU2FtcGxpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1lZHVzYSB1c2VzIGEgbW9kaWZpZWQgYWNjZXB0YW5jZSBjcml0ZXJpb24gYmFzZWQgb24gdHlwaWNhbCBzYW1wbGluZyByYXRoZXIgdGhhbiB0aGUgc3RhbmRhcmQgc3BlY3VsYXRpdmUgZGVjb2RpbmcgYWNjZXB0YW5jZSBwcm9iYWJpbGl0eSByYXRpby4gSW4gc3RhbmRhcmQgc3BlY3VsYXRpdmUgZGVjb2RpbmcsIGEgY2FuZGlkYXRlIHRva2VuIGMgaXMgYWNjZXB0ZWQgd2l0aCBwcm9iYWJpbGl0eSBtaW4oMSwgcF90YXJnZXQoYykgLyBwX2RyYWZ0KGMpKSwgcmVxdWlyaW5nIGV4cGxpY2l0IGFjY2VzcyB0byB0aGUgZHJhZnQgZGlzdHJpYnV0aW9uLiBNZWR1c2EgcmVwbGFjZXMgdGhpcyB3aXRoIGEgcG9zdGVyaW9yIGNoZWNrIGJhc2VkIG9uIHRoZSBNZWR1c2EgaGVhZCBsb2dpdHMgYW5kIGEgdGVtcGVyYXR1cmUgdGhyZXNob2xkOiBhIGNhbmRpZGF0ZSB0b2tlbiBpcyBhY2NlcHRlZCBpZiBpdCBmYWxscyB3aXRoaW4gdGhlIHR5cGljYWwgc2V0IG9mIHRoZSB0YXJnZXQgZGlzdHJpYnV0aW9uIGF0IHRoYXQgcG9zaXRpb24sIGNvbnRyb2xsZWQgYnkgYSBwb3N0ZXJpb3IgdGhyZXNob2xkIGh5cGVycGFyYW1ldGVyIChkZWZhdWx0IDAuMDkpLiBUaGlzIGF2b2lkcyBkZXBlbmRlbmNlIG9uIHRoZSBkcmFmdCBkaXN0cmlidXRpb24gcmF0aW8sIHNpbXBsaWZpZXMgdGhlIGFjY2VwdGFuY2UgY2hlY2sgdG8gYSBzaW5nbGUgY29tcGFyaXNvbiwgYW5kIG1haW50YWlucyBvdXRwdXQgcXVhbGl0eSBlcXVpdmFsZW50IHRvIHNhbXBsaW5nIGRpcmVjdGx5IGZyb20gdGhlIHRhcmdldCBtb2RlbC4gVGhlIHR5cGljYWwgYWNjZXB0YW5jZSBjcml0ZXJpb24gYWNjZXB0cyBjYW5kaWRhdGVzIHdpdGggcHJvYmFiaWxpdHkgMC424oCTMC45IGZvciB3ZWxsLXRyYWluZWQgaGVhZHMsIHdpdGhvdXQgYW55IG5lZWQgdG8gc3RvcmUgb3IgY29tcHV0ZSBkcmFmdCBtb2RlbCBwcm9iYWJpbGl0aWVzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUGFyYW1ldGVyIEVmZmljaWVuY3kiLCJjb250ZW50IjoiTWVkdXNhIGhlYWRzIGFkZCBcdTAwM2MxJSBwYXJhbWV0ZXJzIGFuZCBjYW4gYmUgdHJhaW5lZCBpbiBhIGZldyBob3VycyBvbiBhIHNpbmdsZSBHUFUg4oCUIHRoZSBrZXkgY29uc3RyYWludCBpcyB0aGF0IGJhc2UgbW9kZWwgd2VpZ2h0cyBtdXN0IHJlbWFpbiBmcm96ZW4sIG1ha2luZyBNZWR1c2EgY29tcGF0aWJsZSB3aXRoIGFueSBxdWFudGl6ZWQgb3IgZmluZS10dW5lZCBjaGVja3BvaW50In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VsZi1EaXN0aWxsYXRpb24gVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1lZHVzYS0yIGludHJvZHVjZXMgc2VsZi1kaXN0aWxsYXRpb246IGluc3RlYWQgb2YgdHJhaW5pbmcgaGVhZHMgdG8gbWF0Y2ggb25lLWhvdCBncm91bmQgdHJ1dGggdG9rZW5zLCB0aGUgaGVhZHMgYXJlIHRyYWluZWQgdG8gbWF0Y2ggdGhlIGJhc2UgbW9kZWxcdTAwMjdzIG93biBvdXRwdXQgZGlzdHJpYnV0aW9uIHZpYSBLTCBkaXZlcmdlbmNlIG1pbmltaXNhdGlvbi4gSGVhZCBrIGlzIGRpc3RpbGxlZCBmcm9tIHRoZSBiYXNlIExNIGhlYWRcdTAwMjdzIHByb2JhYmlsaXR5IGRpc3RyaWJ1dGlvbiBmb3IgcG9zaXRpb24gdCtrKzEgcmF0aGVyIHRoYW4gdGhlIGhhcmQgbGFiZWwuIFNlbGYtZGlzdGlsbGF0aW9uIHByb2R1Y2VzIHNvZnRlciB0YXJnZXRzIHRoYXQgY2FwdHVyZSB0aGUgbW9kZWxcdTAwMjdzIG93biB1bmNlcnRhaW50eSwgbGVhZGluZyB0byBoaWdoZXIgYWNjZXB0YW5jZSByYXRlcyBiZWNhdXNlIHRoZSBoZWFkcyBsZWFybiB0byBwcmVkaWN0IHRoZSBzYW1lIGRpc3RyaWJ1dGlvbiB0aGUgdmVyaWZpZXIgdXNlcy4gVGhpcyByZXF1aXJlcyBvbmUgYWRkaXRpb25hbCBmb3J3YXJkIHBhc3Mgb3ZlciB0aGUgdHJhaW5pbmcgZGF0YSB0byBjb2xsZWN0IGJhc2UgbW9kZWwgcHJvYmFiaWxpdHkgZGlzdHJpYnV0aW9ucywgYnV0IHN1YnN0YW50aWFsbHkgaW1wcm92ZXMgYWNjZXB0YW5jZSByYXRlcyDigJQgaGVhZC0xIGltcHJvdmVzIGZyb20gcm91Z2hseSA3MCUgdG8gb3ZlciA4MCUgd2l0aCBzZWxmLWRpc3RpbGxhdGlvbi4gSW4gcHJhY3RpY2Ugc2VsZi1kaXN0aWxsYXRpb24gaXMgYXBwbGllZCBqb2ludGx5IHdpdGggdGhlIGNyb3NzLWVudHJvcHkgbG9zcyB1c2luZyBhIG1peGluZyBjb2VmZmljaWVudCBsYW1iZGEgdGhhdCB3ZWlnaHRzIHRoZSBkaXN0aWxsYXRpb24gb2JqZWN0aXZlIHJlbGF0aXZlIHRvIHRoZSBoYXJkLWxhYmVsIGxvc3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhyb3VnaHB1dCBSZXN1bHRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNZWFzdXJlZCBvbiBWaWN1bmEtN0IgYW5kIFZpY3VuYS0xM0Igd2l0aCBhbiBBMTAwIDgwIEdCIEdQVSBhdCBiYXRjaCBzaXplIDEgKHNpbmdsZS11c2VyIGNoYXQgbGF0ZW5jeSByZWdpbWUpLCBNZWR1c2EgYWNoaWV2ZXMgMi4y4oCTMi44w5cgdGhyb3VnaHB1dCBpbXByb3ZlbWVudCBvdmVyIHN0YW5kYXJkIGF1dG9yZWdyZXNzaXZlIGRlY29kaW5nLiBUaGUgc3BlZWR1cCBncm93cyB3aXRoIHRoZSBudW1iZXIgb2YgaGVhZHMgdXAgdG8gZml2ZSBvciBzaXggaGVhZHMsIGFmdGVyIHdoaWNoIGFjY2VwdGFuY2UgcmF0ZXMgZm9yIGZhcnRoZXItYWhlYWQgcHJlZGljdGlvbnMgZmFsbCB0b28gbG93IHRvIGNvbnRyaWJ1dGUgbmV0IHRocm91Z2hwdXQgZ2Fpbi4gT24gbXVsdGktYmF0Y2ggaW5mZXJlbmNlIHRoZSBnYWlucyBhcmUgcmVkdWNlZCBiZWNhdXNlIHRoZSBiYXNlIG1vZGVsIGJlY29tZXMgY29tcHV0ZS1ib3VuZCByYXRoZXIgdGhhbiBiYW5kd2lkdGgtYm91bmQsIGJ1dCBNZWR1c2Egc3RpbGwgcHJvdmlkZXMgMS414oCTMS44w5cgaW1wcm92ZW1lbnQgYXQgYmF0Y2ggc2l6ZXMgdXAgdG8gOC4gU2VsZi1kaXN0aWxsYXRpb24gKE1lZHVzYS0yKSBwdXNoZXMgc3BlZWR1cCB0byBhcHByb3hpbWF0ZWx5IDMuMMOXIGF0IGJhdGNoIHNpemUgMSBieSByYWlzaW5nIGFjY2VwdGFuY2UgcmF0ZXMgYWNyb3NzIGFsbCBoZWFkcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWVkdXNhIGhlYWRzIiwiQWNjZXB0YW5jZSByYXRlIChoZWFkIDEpIiwiU3BlZWR1cCB2cyBBUiIsIkFkZGVkIHBhcmFtZXRlcnMiLCJUcmFpbmluZyBkYXRhIG5lZWRlZCJdLCJyb3dzIjpbWyIxIGhlYWQiLCI3MOKAkzc4JSIsIjEuNeKAkzEuN8OXIiwifjAuMyUgb2YgYmFzZSIsIjUwSyBpbnN0cnVjdGlvbiBzYW1wbGVzIl0sWyIzIGhlYWRzIiwiSDE6IDc0JSwgSDI6IDU1JSwgSDM6IDM4JSIsIjEuOeKAkzIuMsOXIiwifjAuOCUgb2YgYmFzZSIsIjIwMEsgaW5zdHJ1Y3Rpb24gc2FtcGxlcyJdLFsiNSBoZWFkcyIsIkgxOiA3NCUsIEgy4oCTSDU6IDU1LzM4LzI2LzE4JSIsIjIuMuKAkzIuOMOXIiwifjEuMyUgb2YgYmFzZSIsIjUwMEsgaW5zdHJ1Y3Rpb24gc2FtcGxlcyJdLFsiOCBoZWFkcyIsIkgxOiA3MiUsIGRyb3BzIHN0ZWVwbHkgYmV5b25kIEg0IiwiMi4z4oCTMi45w5ciLCJ+Mi4xJSBvZiBiYXNlIiwiMU0rIGluc3RydWN0aW9uIHNhbXBsZXMiXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIG1lZHVzYS5tb2RlbC5tZWR1c2FfbW9kZWwgaW1wb3J0IE1lZHVzYU1vZGVsXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdGltZVxuXG5kZWYgYmVuY2htYXJrX21lZHVzYV92c19zdGFuZGFyZChcbiAgICBtb2RlbF9wYXRoOiBzdHIsXG4gICAgcHJvbXB0czogbGlzdCxcbiAgICBtYXhfbmV3X3Rva2VuczogaW50ID0gMTI4LFxuKSAtXHUwMDNlIGRpY3Q6XG4gICAgXCJcIlwiTG9hZCBNZWR1c2EgbW9kZWwgYW5kIGNvbXBhcmUgdGhyb3VnaHB1dCB2cyBzdGFuZGFyZCBncmVlZHkgYXV0b3JlZ3Jlc3NpdmUgZGVjb2RlLlwiXCJcIlxuICAgIHRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX3BhdGgpXG4gICAgbW9kZWwgPSBNZWR1c2FNb2RlbC5mcm9tX3ByZXRyYWluZWQobW9kZWxfcGF0aCwgdG9yY2hfZHR5cGU9dG9yY2guZmxvYXQxNilcbiAgICBtb2RlbCA9IG1vZGVsLmN1ZGEoKS5ldmFsKClcbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgbGFiZWwsIHVzZV9tZWR1c2EgaW4gWyhcInN0YW5kYXJkXCIsIEZhbHNlKSwgKFwibWVkdXNhXCIsIFRydWUpXTpcbiAgICAgICAgdG90YWxfdG9rZW5zLCB0MCA9IDAsIHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgZm9yIHByb21wdCBpbiBwcm9tcHRzOlxuICAgICAgICAgICAgaWRzID0gdG9rZW5pemVyKHByb21wdCwgcmV0dXJuX3RlbnNvcnM9XCJwdFwiKS5pbnB1dF9pZHMuY3VkYSgpXG4gICAgICAgICAgICBpZiB1c2VfbWVkdXNhOlxuICAgICAgICAgICAgICAgIG91dCA9IG1vZGVsLm1lZHVzYV9nZW5lcmF0ZShcbiAgICAgICAgICAgICAgICAgICAgaWRzLCBtYXhfbmV3X3Rva2Vucz1tYXhfbmV3X3Rva2VucyxcbiAgICAgICAgICAgICAgICAgICAgdGVtcGVyYXR1cmU9MC4wLCBwb3N0ZXJpb3JfdGhyZXNob2xkPTAuMDksXG4gICAgICAgICAgICAgICAgKVxuICAgICAgICAgICAgZWxzZTpcbiAgICAgICAgICAgICAgICBvdXQgPSBtb2RlbC5nZW5lcmF0ZShpZHMsIG1heF9uZXdfdG9rZW5zPW1heF9uZXdfdG9rZW5zLCBkb19zYW1wbGU9RmFsc2UpXG4gICAgICAgICAgICB0b3RhbF90b2tlbnMgKz0gb3V0LnNoYXBlWzFdIC0gaWRzLnNoYXBlWzFdXG4gICAgICAgIGVsYXBzZWQgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gdDBcbiAgICAgICAgcmVzdWx0c1tsYWJlbF0gPSB7XCJ0b2tfcGVyX3NcIjogdG90YWxfdG9rZW5zIC8gZWxhcHNlZCwgXCJ0b3RhbF90b2tlbnNcIjogdG90YWxfdG9rZW5zfVxuICAgIHNwZWVkdXAgPSByZXN1bHRzW1wibWVkdXNhXCJdW1widG9rX3Blcl9zXCJdIC8gcmVzdWx0c1tcInN0YW5kYXJkXCJdW1widG9rX3Blcl9zXCJdXG4gICAgcHJpbnQoZlwiU3RhbmRhcmQ6IHtyZXN1bHRzW1x1MDAyN3N0YW5kYXJkXHUwMDI3XVtcdTAwMjd0b2tfcGVyX3NcdTAwMjddOi4xZn0gdG9rL3NcIilcbiAgICBwcmludChmXCJNZWR1c2E6ICAge3Jlc3VsdHNbXHUwMDI3bWVkdXNhXHUwMDI3XVtcdTAwMjd0b2tfcGVyX3NcdTAwMjddOi4xZn0gdG9rL3MgIChzcGVlZHVwIHtzcGVlZHVwOi4yZn14KVwiKVxuICAgIHJldHVybiB7KipyZXN1bHRzLCBcInNwZWVkdXBcIjogc3BlZWR1cH0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNZWR1c2EgaXMgb25lIG9mIHRoZSBtb3N0IHByYWN0aWNhbGx5IGRlcGxveWFibGUgc3BlY3VsYXRpdmUgZGVjb2RpbmcgYXBwcm9hY2hlcyBiZWNhdXNlIGl0IHJlcXVpcmVzIG5vIGNoYW5nZXMgdG8gYmFzZSBtb2RlbCBpbmZlcmVuY2UgaW5mcmFzdHJ1Y3R1cmUgYW5kIG5vIHNlcGFyYXRlIGRyYWZ0IG1vZGVsIHByb2Nlc3MuIFRoZSBoZWFkcyBhcmUgZHJvcC1pbiBhZGRpdGlvbnMgdGhhdCBjYW4gYmUgdHJhaW5lZCBvbiBhbnkgZXhpc3RpbmcgaW5zdHJ1Y3Rpb24gZGF0YXNldCBpbiBhIGZldyBHUFUtaG91cnMuIFRoZSBtYWluIGxpbWl0YXRpb24gaXMgdGhhdCBzcGVlZHVwIGlzIHN0cm9uZ2VzdCBhdCBiYXRjaCBzaXplIDEgKGxhdGVuY3ktc2Vuc2l0aXZlIHNpbmdsZS11c2VyIGNoYXQpIGFuZCBkaW1pbmlzaGVzIGFzIGJhdGNoIHNpemUgZ3Jvd3MgYmVjYXVzZSB0aGUgYm90dGxlbmVjayBzaGlmdHMgZnJvbSBtZW1vcnkgYmFuZHdpZHRoIHRvIGNvbXB1dGUuIEZvciBoaWdoLXRocm91Z2hwdXQgYmF0Y2ggaW5mZXJlbmNlLCBjb250aW51b3VzIGJhdGNoaW5nIHdpdGggZmxhc2gtYXR0ZW50aW9uIHJlbWFpbnMgbW9yZSBlZmZlY3RpdmUgdGhhbiBzcGVjdWxhdGl2ZSBkZWNvZGluZy4gSG93ZXZlciwgZm9yIGxhdGVuY3ktc2Vuc2l0aXZlIGRlcGxveW1lbnRzIOKAlCBBUElzIHRhcmdldGluZyBwNTAgbGF0ZW5jeSBiZWxvdyA1MDAgbXMg4oCUIE1lZHVzYSBvZmZlcnMgdGhlIG1vc3QgcHJhY3RpY2FsIHBhdGggdG8gMsOXIHNwZWVkdXAgd2l0aG91dCBhZGRpdGlvbmFsIGluZnJhc3RydWN0dXJlLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTWVkdXNhIGhlYWRzIGFyZSBmcm96ZW4gYWxvbmdzaWRlIHRoZSBiYXNlIG1vZGVsIOKAlCB0aGV5IGFyZSBjb21wYXRpYmxlIHdpdGggYW55IHF1YW50aXplZCAoR1BUUSwgQVdRKSBvciBmaW5lLXR1bmVkIGNoZWNrcG9pbnQgYXMgbG9uZyBhcyB0aGUgaGlkZGVuIHNpemUgbWF0Y2hlcy4iLCJUcmVlIGF0dGVudGlvbiB2ZXJpZmllcyB0b3Ata15LIGNhbmRpZGF0ZSBwYXRocyBzaW11bHRhbmVvdXNseSBpbiBhIHNpbmdsZSBmb3J3YXJkIHBhc3Mg4oCUIHNhbWUgY29tcHV0ZSBjb3N0IGFzIHZlcmlmeWluZyBvbmUgY2FuZGlkYXRlIHBhdGguIiwiU2VsZi1kaXN0aWxsYXRpb24gKE1lZHVzYS0yKSBpbXByb3ZlcyBhY2NlcHRhbmNlIHJhdGVzIGJ5IDjigJMxMiBwZXJjZW50YWdlIHBvaW50cyB2ZXJzdXMgdHJhaW5pbmcgYWdhaW5zdCBoYXJkIG9uZS1ob3QgbGFiZWxzLiIsIlR5cGljYWwgYWNjZXB0YW5jZSBzYW1wbGluZyBpcyBlcXVpdmFsZW50IGluIG91dHB1dCBkaXN0cmlidXRpb24gdG8gZGlyZWN0IHNhbXBsaW5nIGZyb20gdGhlIHRhcmdldCBtb2RlbCDigJQgbm8gcXVhbGl0eSBkZWdyYWRhdGlvbi4iLCJGaXZlIGhlYWRzIGlzIHRoZSBwcmFjdGljYWwgc3dlZXQgc3BvdDogYmV5b25kIHRoYXQsIGFjY2VwdGFuY2UgcmF0ZXMgZm9yIGhlYWRzIDYrIGFyZSB0b28gbG93IHRvIGNvbnRyaWJ1dGUgbmV0IHNwZWVkdXAuIiwiTWVkdXNhIHNwZWVkdXBzIGFyZSBsYXJnZXN0IGF0IGJhdGNoIHNpemUgMSBhbmQgZGltaW5pc2ggYXQgYmF0Y2ggc2l6ZXMgYWJvdmUgOCB3aGVyZSB0aGUgbW9kZWwgYmVjb21lcyBjb21wdXRlLWJvdW5kIHJhdGhlciB0aGFuIGJhbmR3aWR0aC1ib3VuZC4iLCJQcmV0cmFpbmVkIE1lZHVzYSBoZWFkcyBmb3IgVmljdW5hLTdCLCBWaWN1bmEtMTNCLCBhbmQgTGxhbWEtMiBhcmUgYXZhaWxhYmxlIGluIHRoZSBGYXN0ZXJEZWNvZGluZyByZXBvc2l0b3J5IG9uIEh1Z2dpbmcgRmFjZS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Medusa: Multiple Decoding Heads for Parallel Token Generation

Medusa (Cai et al. 2024, Together AI) is a speculative decoding framework that replaces the separate draft model with multiple lightweight prediction heads appended to a frozen base LLM. Each head is a compact two-layer MLP sitting on top of the last transformer block's hidden states, independently predicting the token at offset +1, +2, up to +K positions ahead. Because the heads share the base model's rich representations, they can be trained to near-oracle acceptance rates with as little as 0.3% additional parameters. At inference time, all heads generate candidate tokens simultaneously in a single additional forward pass — no separate draft model call required — and the resulting tree of candidates is verified by the base model using a modified tree attention mask that scores all hypotheses in one batched forward pass. The practical result is a 2.2–2.8× throughput improvement on chat workloads with no measurable degradation in output quality.

## Overview

Standard autoregressive decoding generates one token per forward pass, making it memory-bandwidth bound: each step reads all model weights from HBM even though only a tiny fraction of total compute capacity is used. Speculative decoding sidesteps this by using a faster draft model to propose multiple tokens and the target model to verify them in parallel — but maintaining a separate draft model doubles deployment complexity and memory footprint. Medusa eliminates the draft model entirely: the prediction heads are trained once, frozen alongside the base model, and add negligible overhead to the standard inference graph. The typical acceptance rate for the first Medusa head is 60–80%, meaning most generated tokens are accepted, yielding measured speedups of 2.0–3.0× on chat workloads. The approach was popularised alongside Vicuna models and integrates directly with vLLM and SGLang inference servers.

## Architecture: Multiple LM Heads

Each Medusa head k (for k = 1, …, K) is a two-layer MLP with a LayerNorm applied to the last hidden state h_t before the first linear layer. The output of head k is a full vocabulary distribution over the token at position t+k. During a draft step, the base model generates the token at t+1 from its own logits (the standard LM head), while simultaneously all K Medusa heads produce candidate distributions for positions t+2 through t+K+1 — all computed from the same single forward pass over the current context. The heads are parameterised identically but trained independently, and there is no weight sharing between heads. This architecture ensures that head k specialises in predicting tokens k steps ahead given the base model's contextual representations.

```python
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoConfig
from typing import List, Tuple

class MedusaHead(nn.Module):
    """Two-layer MLP predicting token at position t+k from last hidden state."""
    def __init__(self, hidden_size: int, vocab_size: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.LayerNorm(hidden_size),
            nn.Linear(hidden_size, hidden_size, bias=False),
            nn.SiLU(),
            nn.Linear(hidden_size, vocab_size, bias=False),
        )

    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        return self.net(hidden)  # (B, S, vocab_size)

class MedusaWithHeads(nn.Module):
    """Frozen base LLM plus K trainable Medusa heads for positions t+1 to t+K."""
    def __init__(self, model_name: str, num_heads: int = 5):
        super().__init__()
        self.base = AutoModelForCausalLM.from_pretrained(model_name)
        for p in self.base.parameters():
            p.requires_grad_(False)           # freeze all base model weights
        H = self.base.config.hidden_size
        V = self.base.config.vocab_size
        self.medusa_heads = nn.ModuleList(
            [MedusaHead(H, V) for _ in range(num_heads)]
        )

    def forward(self, input_ids: torch.Tensor) -> Tuple[torch.Tensor, List[torch.Tensor]]:
        outputs = self.base(input_ids, output_hidden_states=True)
        last_hidden = outputs.hidden_states[-1]                      # (B, S, H)
        medusa_logits = [head(last_hidden) for head in self.medusa_heads]  # K x (B,S,V)
        return outputs.logits, medusa_logits
```

## Medusa Tree Attention

Rather than verifying candidate tokens one by one, Medusa constructs a token tree from head predictions and verifies all branches simultaneously using a custom attention mask. For K heads each taking the top-p candidates, the tree has at most top-p^K leaves. The tree attention mask is a boolean matrix over all candidate positions: position j can attend to position i only if i is an ancestor of j in the tree. This mask replaces the standard causal mask during the verification forward pass, allowing the base model to score all candidate continuations in a single batched call — the same compute cost as verifying a single continuation. A path through the tree corresponds to a multi-token continuation hypothesis: if a path survives verification (each token matches the base model's greedy or sampled choice at that depth), all tokens on the path are accepted simultaneously, multiplying effective throughput.

```python
import torch
import itertools
from typing import List, Tuple

def build_medusa_tree(
    medusa_logits: List[torch.Tensor],
    top_k: int = 3,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Build candidate token tree and tree attention mask from Medusa head outputs.
    medusa_logits: K tensors each (1, 1, V) — logits for positions t+1 .. t+K.
    Returns (candidates, tree_mask): (N,) token ids and (N, N) bool attention mask.
    """
    # Collect top-k token candidates from each head
    head_topk = [
        torch.topk(lg[0, -1], top_k).indices.tolist()
        for lg in medusa_logits
    ]
    # Enumerate all paths through the tree (Cartesian product)
    paths = list(itertools.product(*head_topk))  # list of K-tuples
    N = len(paths)
    # Tree attention mask: position j attends to i if path_i is a prefix of path_j
    mask = torch.zeros(N, N, dtype=torch.bool)
    for j, pj in enumerate(paths):
        for i, pi in enumerate(paths):
            depth = min(j + 1, i + 1)
            if tuple(pi[:depth]) == tuple(pj[:depth]) and i <= j:
                mask[j, i] = True
    # First token of each path is the candidate from head-1
    candidates = torch.tensor([p[0] for p in paths])
    return candidates, mask

dummy_logits = [torch.randn(1, 1, 32000) for _ in range(3)]
cands, tmask = build_medusa_tree(dummy_logits, top_k=3)
print(f"Tree nodes: {len(cands)}, mask shape: {tuple(tmask.shape)}")
print(f"Non-zero mask entries: {tmask.sum().item()} of {tmask.numel()}")
```

## Training the Medusa Heads

Medusa heads are trained independently of the base model on instruction-tuning data. The training objective is per-head cross-entropy: head k minimises the cross-entropy loss between its predicted distribution and the ground truth token at offset k+1 in the sequence. Because each head predicts a different offset, they are trained with shifted target sequences — head-1 targets tokens shifted by 1, head-2 by 2, and so on. The base model is kept frozen throughout, so its hidden states serve as static, fixed features. Training converges in one to three epochs on moderate instruction datasets (ShareGPT, Alpaca, LMSYS-Chat-1M) and can be completed on a single A100 in under six hours for a 7B model. The per-head acceptance rate on a held-out validation set is the key metric to track: head-1 should reach 65–75%, with acceptance dropping roughly 15 percentage points per additional head.

```python
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from typing import List

def train_medusa_heads(
    model,
    train_loader: DataLoader,
    num_heads: int = 5,
    lr: float = 1e-3,
    epochs: int = 1,
) -> List[float]:
    """Freeze base model, train Medusa heads with per-head cross-entropy losses."""
    optimizer = torch.optim.AdamW(
        [p for p in model.parameters() if p.requires_grad],
        lr=lr, weight_decay=0.01,
    )
    per_head_loss = [0.0] * num_heads
    for epoch in range(epochs):
        for batch in train_loader:
            input_ids = batch['input_ids']
            _, medusa_logits = model(input_ids)
            total_loss = torch.tensor(0.0, requires_grad=True)
            for k, head_logits in enumerate(medusa_logits):
                target = input_ids[:, k + 1:]                  # shift target by k+1
                pred   = head_logits[:, :-(k + 1), :]          # align sequence length
                loss_k = F.cross_entropy(
                    pred.reshape(-1, pred.size(-1)), target.reshape(-1), ignore_index=-100
                )
                total_loss = total_loss + loss_k
                per_head_loss[k] += loss_k.item()
            optimizer.zero_grad()
            total_loss.backward()
            optimizer.step()
    per_head_loss = [l / (epochs * len(train_loader)) for l in per_head_loss]
    for k, lv in enumerate(per_head_loss):
        print(f"  Head {k+1} (offset +{k+1}): avg CE loss = {lv:.4f}")
    return per_head_loss
```

## Acceptance with Typical Sampling

Medusa uses a modified acceptance criterion based on typical sampling rather than the standard speculative decoding acceptance probability ratio. In standard speculative decoding, a candidate token c is accepted with probability min(1, p_target(c) / p_draft(c)), requiring explicit access to the draft distribution. Medusa replaces this with a posterior check based on the Medusa head logits and a temperature threshold: a candidate token is accepted if it falls within the typical set of the target distribution at that position, controlled by a posterior threshold hyperparameter (default 0.09). This avoids dependence on the draft distribution ratio, simplifies the acceptance check to a single comparison, and maintains output quality equivalent to sampling directly from the target model. The typical acceptance criterion accepts candidates with probability 0.6–0.9 for well-trained heads, without any need to store or compute draft model probabilities.

> **Parameter Efficiency**: Medusa heads add <1% parameters and can be trained in a few hours on a single GPU — the key constraint is that base model weights must remain frozen, making Medusa compatible with any quantized or fine-tuned checkpoint

## Self-Distillation Training

Medusa-2 introduces self-distillation: instead of training heads to match one-hot ground truth tokens, the heads are trained to match the base model's own output distribution via KL divergence minimisation. Head k is distilled from the base LM head's probability distribution for position t+k+1 rather than the hard label. Self-distillation produces softer targets that capture the model's own uncertainty, leading to higher acceptance rates because the heads learn to predict the same distribution the verifier uses. This requires one additional forward pass over the training data to collect base model probability distributions, but substantially improves acceptance rates — head-1 improves from roughly 70% to over 80% with self-distillation. In practice self-distillation is applied jointly with the cross-entropy loss using a mixing coefficient lambda that weights the distillation objective relative to the hard-label loss.

## Throughput Results

Measured on Vicuna-7B and Vicuna-13B with an A100 80 GB GPU at batch size 1 (single-user chat latency regime), Medusa achieves 2.2–2.8× throughput improvement over standard autoregressive decoding. The speedup grows with the number of heads up to five or six heads, after which acceptance rates for farther-ahead predictions fall too low to contribute net throughput gain. On multi-batch inference the gains are reduced because the base model becomes compute-bound rather than bandwidth-bound, but Medusa still provides 1.5–1.8× improvement at batch sizes up to 8. Self-distillation (Medusa-2) pushes speedup to approximately 3.0× at batch size 1 by raising acceptance rates across all heads.

| Medusa heads | Acceptance rate (head 1) | Speedup vs AR | Added parameters | Training data needed |
| --- | --- | --- | --- | --- |
| 1 head | 70–78% | 1.5–1.7× | ~0.3% of base | 50K instruction samples |
| 3 heads | H1: 74%, H2: 55%, H3: 38% | 1.9–2.2× | ~0.8% of base | 200K instruction samples |
| 5 heads | H1: 74%, H2–H5: 55/38/26/18% | 2.2–2.8× | ~1.3% of base | 500K instruction samples |
| 8 heads | H1: 72%, drops steeply beyond H4 | 2.3–2.9× | ~2.1% of base | 1M+ instruction samples |

```python
from medusa.model.medusa_model import MedusaModel
from transformers import AutoTokenizer
import torch
import time

def benchmark_medusa_vs_standard(
    model_path: str,
    prompts: list,
    max_new_tokens: int = 128,
) -> dict:
    """Load Medusa model and compare throughput vs standard greedy autoregressive decode."""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = MedusaModel.from_pretrained(model_path, torch_dtype=torch.float16)
    model = model.cuda().eval()
    results = {}
    for label, use_medusa in [("standard", False), ("medusa", True)]:
        total_tokens, t0 = 0, time.perf_counter()
        for prompt in prompts:
            ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()
            if use_medusa:
                out = model.medusa_generate(
                    ids, max_new_tokens=max_new_tokens,
                    temperature=0.0, posterior_threshold=0.09,
                )
            else:
                out = model.generate(ids, max_new_tokens=max_new_tokens, do_sample=False)
            total_tokens += out.shape[1] - ids.shape[1]
        elapsed = time.perf_counter() - t0
        results[label] = {"tok_per_s": total_tokens / elapsed, "total_tokens": total_tokens}
    speedup = results["medusa"]["tok_per_s"] / results["standard"]["tok_per_s"]
    print(f"Standard: {results['standard']['tok_per_s']:.1f} tok/s")
    print(f"Medusa:   {results['medusa']['tok_per_s']:.1f} tok/s  (speedup {speedup:.2f}x)")
    return {**results, "speedup": speedup}
```

## Key Takeaways

Medusa is one of the most practically deployable speculative decoding approaches because it requires no changes to base model inference infrastructure and no separate draft model process. The heads are drop-in additions that can be trained on any existing instruction dataset in a few GPU-hours. The main limitation is that speedup is strongest at batch size 1 (latency-sensitive single-user chat) and diminishes as batch size grows because the bottleneck shifts from memory bandwidth to compute. For high-throughput batch inference, continuous batching with flash-attention remains more effective than speculative decoding. However, for latency-sensitive deployments — APIs targeting p50 latency below 500 ms — Medusa offers the most practical path to 2× speedup without additional infrastructure.

- Medusa heads are frozen alongside the base model — they are compatible with any quantized (GPTQ, AWQ) or fine-tuned checkpoint as long as the hidden size matches.
- Tree attention verifies top-k^K candidate paths simultaneously in a single forward pass — same compute cost as verifying one candidate path.
- Self-distillation (Medusa-2) improves acceptance rates by 8–12 percentage points versus training against hard one-hot labels.
- Typical acceptance sampling is equivalent in output distribution to direct sampling from the target model — no quality degradation.
- Five heads is the practical sweet spot: beyond that, acceptance rates for heads 6+ are too low to contribute net speedup.
- Medusa speedups are largest at batch size 1 and diminish at batch sizes above 8 where the model becomes compute-bound rather than bandwidth-bound.
- Pretrained Medusa heads for Vicuna-7B, Vicuna-13B, and Llama-2 are available in the FasterDecoding repository on Hugging Face.

---

