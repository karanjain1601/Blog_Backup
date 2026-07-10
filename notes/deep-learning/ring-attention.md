---
title: "Ring Attention — Sequence Parallelism for Long Contexts"
slug: "ring-attention"
description: "Simulate ring attention with Python lists, implement online softmax normalisation for distributed attention, combine ring attention with FlashAttention blocks, and analyse per-GPU memory scaling with sequence length and device count."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmluZyBBdHRlbnRpb24gKExpdSBldCBhbC4gMjAyMykgZW5hYmxlcyB0cmFpbmluZyBvbiBzZXF1ZW5jZXMgZmFyIGxvbmdlciB0aGFuIGEgc2luZ2xlIEdQVSBjYW4gaG9sZCBieSBkaXN0cmlidXRpbmcgdGhlIHNlcXVlbmNlIGFjcm9zcyBtdWx0aXBsZSBHUFVzLiBFYWNoIEdQVSBob2xkcyBhIGNvbnRpZ3VvdXMgc2VnbWVudCBvZiBRLCBLLCBhbmQgVi4gVGhlIEdQVXMgYXJlIGFycmFuZ2VkIGluIGEgbG9naWNhbCByaW5nOiBhdCBlYWNoIHN0ZXAgYSBHUFUgY29tcHV0ZXMgbG9jYWwgYXR0ZW50aW9uIGJldHdlZW4gaXRzIFEgc2VnbWVudCBhbmQgaXRzIGN1cnJlbnQgSyxWIHNlZ21lbnQsIHRoZW4gcGFzc2VzIGl0cyBLLFYgdG8gdGhlIG5leHQgR1BVIGluIHRoZSByaW5nLiBBZnRlciBOIHN0ZXBzIChOID0gbnVtYmVyIG9mIEdQVXMpLCBldmVyeSBRIGhhcyBhdHRlbmRlZCB0byBldmVyeSBLIGFuZCBWLiBDcnVjaWFsbHksIHRoZSBLLFYgY29tbXVuaWNhdGlvbiBvdmVybGFwcyB3aXRoIGxvY2FsIEZsYXNoQXR0ZW50aW9uIGNvbXB1dGF0aW9uLCBoaWRpbmcgbW9zdCBvZiB0aGUgbmV0d29yayBsYXRlbmN5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlcXVlbmNlIFBhcmFsbGVsaXNtIGFuZCB0aGUgUmluZyBDb21tdW5pY2F0aW9uIFBhdHRlcm4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRlbnNvciBwYXJhbGxlbGlzbSAoTWVnYXRyb24tTE0pIHNwbGl0cyBtb2RlbCB3ZWlnaHRzIGFjcm9zcyBHUFVzLiBEYXRhIHBhcmFsbGVsaXNtIHNwbGl0cyB0aGUgYmF0Y2guIFNlcXVlbmNlIHBhcmFsbGVsaXNtIHNwbGl0cyB0aGUgc2VxdWVuY2UgZGltZW5zaW9uIEwgYWNyb3NzIEdQVXMuIEZvciBOIEdQVXMgZWFjaCBob2xkaW5nIEwvTiB0b2tlbnMsIHRoZSBsb2NhbCBhdHRlbnRpb24gbWF0cml4IGlzIChML04pIMOXIChML04pIGluc3RlYWQgb2YgTCDDlyBMIOKAlCBhbiBOwrIgcmVkdWN0aW9uIGluIHBlci1HUFUgbWVtb3J5LiBSaW5nIEF0dGVudGlvbiBpbXBsZW1lbnRzIHNlcXVlbmNlIHBhcmFsbGVsaXNtIGZvciBhdHRlbnRpb246IGF0IHN0ZXAgcywgR1BVIGkgY29tcHV0ZXMgYXR0ZW50aW9uIGJldHdlZW4gaXRzIFFfaSBhbmQgdGhlIEssViBibG9jayBpdCBjdXJyZW50bHkgaG9sZHMgKGluaXRpYWxseSBmcm9tIEdQVSBpLCB0aGVuIGN5Y2xlZCBmcm9tIEdQVSAoaStzKSBtb2QgTikuIEFmdGVyIE4gc3RlcHMsIHRoZSBwYXJ0aWFsIGF0dGVudGlvbiBvdXRwdXRzIGFyZSBjb21iaW5lZCB1c2luZyBvbmxpbmUgc29mdG1heCBub3JtYWxpc2F0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJpbmcgQXR0ZW50aW9uIEZvcndhcmQgUGFzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJpbmcgYXR0ZW50aW9uIGFsZ29yaXRobTogaW5pdGlhbGlzZSBvdXRwdXQgT19pID0gMCwgcnVubmluZyBsb2ctc3VtLWV4cCBsc2VfaSA9IC3iiJ4gZm9yIGVhY2ggR1BVIGkuIEZvciBzID0gMCB0byBOLTE6IGNvbXB1dGUgbG9jYWwgYXR0ZW50aW9uIHNjb3JlcyBBX3tpLGp9ID0gUV9pIEtfauG1gCAvIOKImmQgd2hlcmUgaiA9IChpK3MpIG1vZCBOOyB1cGRhdGUgdGhlIHJ1bm5pbmcgc29mdG1heCB1c2luZyBvbmxpbmUgbm9ybWFsaXNhdGlvbiAoRmxhc2hBdHRlbnRpb24tc3R5bGUpOyBzZW5kIEtfaiwgVl9qIHRvIEdQVSAoaSsxKSBtb2QgTiB3aGlsZSBjb21wdXRpbmc7IHJlY2VpdmUgS197ai0xfSwgVl97ai0xfSBmcm9tIEdQVSAoaS0xKSBtb2QgTi4gQWZ0ZXIgTiBzdGVwcyBlYWNoIEdQVSBob2xkcyBPX2kgPSBzb2Z0bWF4KFFfaSBbS18wOyBLXzE7IC4uLjsgS197Ti0xfV3htYApIFYg4oCUIHRoZSBjb3JyZWN0IGZ1bGwtc2VxdWVuY2UgYXR0ZW50aW9uIG91dHB1dCBmb3IgaXRzIFEgc2VnbWVudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5kZWYgcmluZ19hdHRlbnRpb25fc2ltdWxhdGUoUV9zZWdzLCBLX3NlZ3MsIFZfc2Vncyk6XG4gICAgXCJcIlwiU2ltdWxhdGUgcmluZyBhdHRlbnRpb24gd2l0aCBQeXRob24gbGlzdHMgKG5vIGFjdHVhbCBtdWx0aS1HUFUgY29tbXMpLlxuICAgIFFfc2VncywgS19zZWdzLCBWX3NlZ3M6IGxpc3RzIG9mIHRlbnNvcnMsIG9uZSBwZXIgR1BVLCBzaGFwZSAoQixoLExzLGQpLlxuICAgIFJldHVybnM6IGxpc3Qgb2Ygb3V0cHV0IHNlZ21lbnRzLCBvbmUgcGVyIEdQVS5cbiAgICBcIlwiXCJcbiAgICBOID0gbGVuKFFfc2VncykgICMgbnVtYmVyIG9mIEdQVXNcbiAgICBCLCBoLCBMcywgZCA9IFFfc2Vnc1swXS5zaGFwZVxuICAgICMgRWFjaCBHUFUgbWFpbnRhaW5zIHJ1bm5pbmcgb3V0cHV0IE8gYW5kIGxvZy1zdW0tZXhwIGZvciBvbmxpbmUgc29mdG1heFxuICAgIE9zICAgPSBbdG9yY2guemVyb3MoQiwgaCwgTHMsIGQpIGZvciBfIGluIHJhbmdlKE4pXVxuICAgIGxzZXMgPSBbdG9yY2guZnVsbCgoQiwgaCwgTHMsIDEpLCBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSkgZm9yIF8gaW4gcmFuZ2UoTildXG4gICAga3ZfcmluZyA9IGxpc3QoemlwKEtfc2VncywgVl9zZWdzKSkgICMgaW5pdGlhbCBLLFYgYXNzaWdubWVudFxuICAgIGZvciBzdGVwIGluIHJhbmdlKE4pOlxuICAgICAgICBmb3IgaSBpbiByYW5nZShOKTpcbiAgICAgICAgICAgIGogPSAoaSArIHN0ZXApICUgTiAgICAgICAgICAjIHdoaWNoIEssViBibG9jayBHUFUgaSBob2xkc1xuICAgICAgICAgICAgS19qLCBWX2ogPSBrdl9yaW5nW2pdXG4gICAgICAgICAgICBzY29yZXMgPSBRX3NlZ3NbaV0gQCBLX2oudHJhbnNwb3NlKC0yLC0xKSAvIG1hdGguc3FydChkKSAgIyAoQixoLExzLExzKVxuICAgICAgICAgICAgYmxvY2tfbWF4ID0gc2NvcmVzLm1heChkaW09LTEsIGtlZXBkaW09VHJ1ZSkudmFsdWVzXG4gICAgICAgICAgICBleHBfc2NvcmVzID0gdG9yY2guZXhwKHNjb3JlcyAtIGJsb2NrX21heClcbiAgICAgICAgICAgIGJsb2NrX2xzZSAgPSBibG9ja19tYXggKyB0b3JjaC5sb2coZXhwX3Njb3Jlcy5zdW0oLTEsIGtlZXBkaW09VHJ1ZSkpXG4gICAgICAgICAgICAjIE1lcmdlIHdpdGggcnVubmluZyBsc2UgKG9ubGluZSBzb2Z0bWF4KVxuICAgICAgICAgICAgbHNlX25ldyA9IHRvcmNoLmxvZ2FkZGV4cChsc2VzW2ldLCBibG9ja19sc2UpXG4gICAgICAgICAgICBhbHBoYSA9IHRvcmNoLmV4cChsc2VzW2ldIC0gbHNlX25ldylcbiAgICAgICAgICAgIGJldGEgID0gdG9yY2guZXhwKGJsb2NrX2xzZSAtIGxzZV9uZXcpXG4gICAgICAgICAgICBPc1tpXSAgID0gYWxwaGEgKiBPc1tpXSArIGJldGEgKiAoZXhwX3Njb3JlcyAvIGV4cF9zY29yZXMuc3VtKC0xLGtlZXBkaW09VHJ1ZSkgQCBWX2opXG4gICAgICAgICAgICBsc2VzW2ldID0gbHNlX25ld1xuICAgICAgICAjIFNpbXVsYXRlIHJpbmcgcm90YXRpb246IGVhY2ggR1BVIHNlbmRzIEssViB0byBuZXh0XG4gICAgICAgIGt2X3JpbmcgPSBba3ZfcmluZ1soaSAtIDEpICUgTl0gZm9yIGkgaW4gcmFuZ2UoTildXG4gICAgcmV0dXJuIE9zXG5cbk4sIEIsIGgsIExzLCBkID0gNCwgMSwgMiwgOCwgMTYgICMgNCBHUFVzLCA4IHRva2VucyBlYWNoID0gMzIgdG90YWxcblFfc2VncyA9IFt0b3JjaC5yYW5kbihCLGgsTHMsZCkgZm9yIF8gaW4gcmFuZ2UoTildXG5LX3NlZ3MgPSBbdG9yY2gucmFuZG4oQixoLExzLGQpIGZvciBfIGluIHJhbmdlKE4pXVxuVl9zZWdzID0gW3RvcmNoLnJhbmRuKEIsaCxMcyxkKSBmb3IgXyBpbiByYW5nZShOKV1cbk9zID0gcmluZ19hdHRlbnRpb25fc2ltdWxhdGUoUV9zZWdzLCBLX3NlZ3MsIFZfc2VncylcblFfZnVsbCA9IHRvcmNoLmNhdChRX3NlZ3MsIGRpbT0yKVxuS19mdWxsID0gdG9yY2guY2F0KEtfc2VncywgZGltPTIpXG5WX2Z1bGwgPSB0b3JjaC5jYXQoVl9zZWdzLCBkaW09Milcbk9fcmVmICA9IEYuc2NhbGVkX2RvdF9wcm9kdWN0X2F0dGVudGlvbihRX2Z1bGwsIEtfZnVsbCwgVl9mdWxsKVxuT19yaW5nID0gdG9yY2guY2F0KE9zLCBkaW09MilcbnByaW50KGZcdTAwMjdSaW5nIG91dHB1dCBzaGFwZToge09fcmluZy5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3TWF4IGRpZmYgdnMgZnVsbCBhdHRlbnRpb246IHsoT19yaW5nIC0gT19yZWYpLmFicygpLm1heCgpLml0ZW0oKTouNmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9ubGluZSBOb3JtYWxpc2F0aW9uIGZvciBEaXN0cmlidXRlZCBTb2Z0bWF4In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2V5IGFsZ29yaXRobWljIGNoYWxsZW5nZSBpbiByaW5nIGF0dGVudGlvbiBpcyBjb21iaW5pbmcgcGFydGlhbCBzb2Z0bWF4IHJlc3VsdHMgY29tcHV0ZWQgb24gZGlmZmVyZW50IEssViBibG9ja3MuIFN0YW5kYXJkIHNvZnRtYXggcmVxdWlyZXMgc2VlaW5nIGFsbCBrZXlzIHRvIGNvbXB1dGUgdGhlIGRlbm9taW5hdG9yIM6jX2ogZXhwKHHCt2visbwv4oiaZCkuIE9ubGluZSBub3JtYWxpc2F0aW9uIChmcm9tIEZsYXNoQXR0ZW50aW9uKSBtYWludGFpbnMgYSBydW5uaW5nIGxvZy1zdW0tZXhwIChsc2UpIHRoYXQgYWxsb3dzIHVwZGF0aW5nIHRoZSBvdXRwdXQgaW5jcmVtZW50YWxseS4gRm9yIGVhY2ggbmV3IEsgYmxvY2s6IGNvbXB1dGUgYmxvY2tfbHNlLCBtZXJnZSB3aXRoIHJ1bm5pbmcgbHNlIHVzaW5nIGxvZ2FkZGV4cCwgcmVzY2FsZSB0aGUgcHJldmlvdXMgb3V0cHV0IGJ5IGV4cChvbGRfbHNlIC0gbmV3X2xzZSksIGFkZCB0aGUgY29udHJpYnV0aW9uIGZyb20gdGhlIG5ldyBibG9jayBzY2FsZWQgYnkgZXhwKGJsb2NrX2xzZSAtIG5ld19sc2UpLiBBZnRlciBhbGwgTiByaW5nIHN0ZXBzLCB0aGUgb3V0cHV0IGlzIG51bWVyaWNhbGx5IGVxdWl2YWxlbnQgdG8gZnVsbCBzb2Z0bWF4IGF0dGVudGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbWF0aFxuXG5kZWYgb25saW5lX3NvZnRtYXhfYWNjdW11bGF0ZShxLCBrX2Jsb2Nrcywgdl9ibG9ja3MpOlxuICAgIFwiXCJcIkFjY3VtdWxhdGUgYXR0ZW50aW9uIG92ZXIgSyxWIGJsb2NrcyB1c2luZyBvbmxpbmUgKGxvZy1zdW0tZXhwKSBub3JtYWxpc2F0aW9uLlxuICAgIHE6IChMX3EsIGQpICBrX2Jsb2Nrcy92X2Jsb2NrczogbGlzdCBvZiAoTF9rLCBkKSB0ZW5zb3JzLlxuICAgIFJldHVybnMgb3V0cHV0IChMX3EsIGQpIGVxdWl2YWxlbnQgdG8gZnVsbCBzb2Z0bWF4IGF0dGVudGlvbi5cbiAgICBcIlwiXCJcbiAgICBkID0gcS5zaGFwZVstMV1cbiAgICBMX3EgPSBxLnNoYXBlWzBdXG4gICAgTyAgID0gdG9yY2guemVyb3MoTF9xLCBkKVxuICAgIGxzZSA9IHRvcmNoLmZ1bGwoKExfcSwgMSksIGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpKVxuICAgIGZvciBLX2IsIFZfYiBpbiB6aXAoa19ibG9ja3MsIHZfYmxvY2tzKTpcbiAgICAgICAgc2NvcmVzICAgID0gcSBAIEtfYi5UIC8gbWF0aC5zcXJ0KGQpICAgICAgICAgICAgICAjIChMX3EsIExfaylcbiAgICAgICAgYmxvY2tfbWF4ID0gc2NvcmVzLm1heChkaW09LTEsIGtlZXBkaW09VHJ1ZSkudmFsdWVzXG4gICAgICAgIGVfc2NvcmVzICA9IHRvcmNoLmV4cChzY29yZXMgLSBibG9ja19tYXgpICAgICAgICAgICMgbnVtZXJpY2FsbHkgc3RhYmxlXG4gICAgICAgIGJsb2NrX2xzZSA9IGJsb2NrX21heCArIHRvcmNoLmxvZyhlX3Njb3Jlcy5zdW0oLTEsIGtlZXBkaW09VHJ1ZSkpXG4gICAgICAgIGxzZV9uZXcgICA9IHRvcmNoLmxvZ2FkZGV4cChsc2UsIGJsb2NrX2xzZSlcbiAgICAgICAgYWxwaGEgICAgID0gdG9yY2guZXhwKGxzZSAtIGxzZV9uZXcpICAgICAgICAgICAgICAgIyByZXNjYWxlIG9sZCBjb250cmlidXRpb25cbiAgICAgICAgYmV0YSAgICAgID0gdG9yY2guZXhwKGJsb2NrX2xzZSAtIGxzZV9uZXcpICAgICAgICAgIyBzY2FsZSBuZXcgY29udHJpYnV0aW9uXG4gICAgICAgIE8gICAgICAgICA9IGFscGhhICogTyArIGJldGEgKiAoZV9zY29yZXMgLyBlX3Njb3Jlcy5zdW0oLTEsa2VlcGRpbT1UcnVlKSBAIFZfYilcbiAgICAgICAgbHNlICAgICAgID0gbHNlX25ld1xuICAgIHJldHVybiBPXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDEpXG5MLCBkID0gMzIsIDE2XG5xID0gdG9yY2gucmFuZG4oTCwgZClcbksgPSB0b3JjaC5yYW5kbihMLCBkKVxuViA9IHRvcmNoLnJhbmRuKEwsIGQpXG4jIFNwbGl0IEssIFYgaW50byA0IGJsb2NrcyBhcyBpZiBkaXN0cmlidXRlZCBhY3Jvc3MgNCBHUFVzXG5rX2Jsb2NrcyA9IEsuY2h1bmsoNCwgZGltPTApXG52X2Jsb2NrcyA9IFYuY2h1bmsoNCwgZGltPTApXG5PX29ubGluZSA9IG9ubGluZV9zb2Z0bWF4X2FjY3VtdWxhdGUocSwga19ibG9ja3MsIHZfYmxvY2tzKVxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuT19mdWxsID0gRi5zY2FsZWRfZG90X3Byb2R1Y3RfYXR0ZW50aW9uKHEudW5zcXVlZXplKDApLnVuc3F1ZWV6ZSgwKSxcbiAgICAgICAgICAgICBLLnVuc3F1ZWV6ZSgwKS51bnNxdWVlemUoMCksIFYudW5zcXVlZXplKDApLnVuc3F1ZWV6ZSgwKSkuc3F1ZWV6ZSgpXG5wcmludChmXHUwMDI3T25saW5lIG5vcm0gbWF4IGRpZmY6IHsoT19vbmxpbmUgLSBPX2Z1bGwpLmFicygpLm1heCgpLml0ZW0oKTouOGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3TnVtZXJpY2FsbHkgaWRlbnRpY2FsIHRvIGZ1bGwgc29mdG1heCBhdHRlbnRpb24gYWNyb3NzIDQgYmxvY2tzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21iaW5pbmcgUmluZyBBdHRlbnRpb24gd2l0aCBGbGFzaEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gcHJhY3RpY2UsIHJpbmcgYXR0ZW50aW9uIGRvZXMgbm90IGNvbXB1dGUgbmFpdmUgbG9jYWwgYXR0ZW50aW9uIOKAlCBpdCB1c2VzIEZsYXNoQXR0ZW50aW9uIHdpdGhpbiBlYWNoIHJpbmcgc3RlcCBmb3IgbWVtb3J5IGVmZmljaWVuY3kuIEZsYXNoQXR0ZW50aW9uIHRpbGVzIHRoZSBsb2NhbCAoTC9OKSDDlyAoTC9OKSBhdHRlbnRpb24gbWF0cml4IHRvIGF2b2lkIG1hdGVyaWFsaXNpbmcgaXQsIGtlZXBpbmcgcGVyLUdQVSBtZW1vcnkgTyhML04pIHJhdGhlciB0aGFuIE8oKEwvTinCsikuIFRoZSBjb21iaW5hdGlvbjogcmluZyBhdHRlbnRpb24gaGFuZGxlcyB0aGUgc2VxdWVuY2UgZGlzdHJpYnV0aW9uIGFjcm9zcyBHUFVzIChpbnRlci1HUFUgbGV2ZWwpLCBGbGFzaEF0dGVudGlvbiBoYW5kbGVzIHRoZSBtZW1vcnktZWZmaWNpZW50IHRpbGluZyB3aXRoaW4gZWFjaCBHUFUgKGludHJhLUdQVSBsZXZlbCkuIFRvZ2V0aGVyIHRoZXkgYWNoaWV2ZSBPKEwvTikgbWVtb3J5IHBlciBHUFUgaW4gYm90aCBzZXF1ZW5jZSBsZW5ndGggYW5kIGF0dGVudGlvbiBzY29yZXMsIGVuYWJsaW5nIGNvbnRleHRzIG9mIEwgPSBOIMOXIExfR1BVIHdoZXJlIExfR1BVIGlzIHRoZSBwZXItR1BVIEZsYXNoQXR0ZW50aW9uIGxpbWl0ICh+MTI4SyBvbiBhbiA4MCBHQiBBMTAwKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5kZWYgZmxhc2hfYXR0ZW50aW9uX2Jsb2NrKFEsIEssIFYsIGJsb2NrX3NpemU9MzIpOlxuICAgIFwiXCJcIlNpbXBsaWZpZWQgRmxhc2hBdHRlbnRpb246IHRpbGVkIGNvbXB1dGF0aW9uIHRvIGF2b2lkIE8oTF4yKSBtZW1vcnkuXG4gICAgUTogKEIsaCxMcSxkKSAgSyxWOiAoQixoLExrLGQpLiBSZXR1cm5zIChCLGgsTHEsZCkuXG4gICAgXCJcIlwiXG4gICAgQiwgaCwgTHEsIGQgPSBRLnNoYXBlXG4gICAgTGsgPSBLLnNoYXBlWzJdXG4gICAgTyAgID0gdG9yY2guemVyb3NfbGlrZShRKVxuICAgIGxzZSA9IHRvcmNoLmZ1bGwoKEIsIGgsIExxLCAxKSwgZmxvYXQoXHUwMDI3LWluZlx1MDAyNykpXG4gICAgZm9yIGogaW4gcmFuZ2UoMCwgTGssIGJsb2NrX3NpemUpOlxuICAgICAgICBLaiA9IEtbOiwgOiwgajpqK2Jsb2NrX3NpemVdXG4gICAgICAgIFZqID0gVls6LCA6LCBqOmorYmxvY2tfc2l6ZV1cbiAgICAgICAgcyAgPSBRIEAgS2oudHJhbnNwb3NlKC0yLC0xKSAvIG1hdGguc3FydChkKVxuICAgICAgICBibSA9IHMubWF4KC0xLCBrZWVwZGltPVRydWUpLnZhbHVlc1xuICAgICAgICBlICA9IHRvcmNoLmV4cChzIC0gYm0pXG4gICAgICAgIGJsID0gYm0gKyB0b3JjaC5sb2coZS5zdW0oLTEsIGtlZXBkaW09VHJ1ZSkpXG4gICAgICAgIGxzZV9uZXcgPSB0b3JjaC5sb2dhZGRleHAobHNlLCBibClcbiAgICAgICAgTyA9IHRvcmNoLmV4cChsc2UgLSBsc2VfbmV3KSAqIE8gKyB0b3JjaC5leHAoYmwgLSBsc2VfbmV3KSAqIChlIC8gZS5zdW0oLTEsa2VlcGRpbT1UcnVlKSBAIFZqKVxuICAgICAgICBsc2UgPSBsc2VfbmV3XG4gICAgcmV0dXJuIE9cblxuZGVmIHJpbmdfZmxhc2hfYXR0ZW50aW9uKFFfc2VncywgS19zZWdzLCBWX3NlZ3MsIGJsb2NrX3NpemU9MTYpOlxuICAgIFwiXCJcIlJpbmcgYXR0ZW50aW9uIHdpdGggRmxhc2hBdHRlbnRpb24gYXMgdGhlIGxvY2FsIGNvbXB1dGUga2VybmVsLlwiXCJcIlxuICAgIE4gPSBsZW4oUV9zZWdzKVxuICAgIE9zICAgPSBbdG9yY2guemVyb3NfbGlrZShxKSBmb3IgcSBpbiBRX3NlZ3NdXG4gICAgbHNlcyA9IFt0b3JjaC5mdWxsKCgqcS5zaGFwZVs6M10sIDEpLCBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSkgZm9yIHEgaW4gUV9zZWdzXVxuICAgIGt2ICAgPSBsaXN0KHppcChLX3NlZ3MsIFZfc2VncykpXG4gICAgZm9yIHN0ZXAgaW4gcmFuZ2UoTik6XG4gICAgICAgIGZvciBpIGluIHJhbmdlKE4pOlxuICAgICAgICAgICAgaiA9IChpICsgc3RlcCkgJSBOXG4gICAgICAgICAgICBLaiwgVmogPSBrdltqXVxuICAgICAgICAgICAgYmxvY2tfb3V0ID0gZmxhc2hfYXR0ZW50aW9uX2Jsb2NrKFFfc2Vnc1tpXSwgS2osIFZqLCBibG9ja19zaXplKVxuICAgICAgICAgICAgIyBNZXJnZSB1c2luZyBvbmxpbmUgbm9ybWFsaXNhdGlvbiBhdCBzZWdtZW50IGxldmVsXG4gICAgICAgICAgICBibCA9IHRvcmNoLmxvZyh0b3JjaC5vbmVzKCpRX3NlZ3NbaV0uc2hhcGVbOjNdLCAxKSkgICMgc2ltcGxpZmllZFxuICAgICAgICAgICAgbHNlX25ldyA9IHRvcmNoLmxvZ2FkZGV4cChsc2VzW2ldLCBibClcbiAgICAgICAgICAgIE9zW2ldID0gMC41ICogT3NbaV0gKyAwLjUgKiBibG9ja19vdXQgICMgc2ltcGxpZmllZCBtZXJnZSBmb3IgZGVtb1xuICAgICAgICAgICAgbHNlc1tpXSA9IGxzZV9uZXdcbiAgICAgICAga3YgPSBba3ZbKGkgLSAxKSAlIE5dIGZvciBpIGluIHJhbmdlKE4pXVxuICAgIHJldHVybiBPc1xuXG5OLCBCLCBoLCBMcywgZCA9IDIsIDEsIDEsIDE2LCA4XG5RX3NlZ3MgPSBbdG9yY2gucmFuZG4oQixoLExzLGQpIGZvciBfIGluIHJhbmdlKE4pXVxuS19zZWdzID0gW3RvcmNoLnJhbmRuKEIsaCxMcyxkKSBmb3IgXyBpbiByYW5nZShOKV1cblZfc2VncyA9IFt0b3JjaC5yYW5kbihCLGgsTHMsZCkgZm9yIF8gaW4gcmFuZ2UoTildXG5PcyA9IHJpbmdfZmxhc2hfYXR0ZW50aW9uKFFfc2VncywgS19zZWdzLCBWX3NlZ3MpXG5wcmludChmXHUwMDI3UmluZytGbGFzaDoge059IEdQVXMsIHtMc30gdG9rZW5zL0dQVSA9IHtOKkxzfSB0b3RhbCB0b2tlbnNcdTAwMjcpXG5wcmludChmXHUwMDI3T3V0cHV0IHNlZyAwOiB7T3NbMF0uc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1Blci1HUFUgYXR0biBtZW1vcnk6IE8oKExzL2Jsb2NrKV4yKSA9IE8oe0xzfV4yKSB2cyBPKHtOKkxzfV4yKSBmdWxsXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNjYWxpbmcgQW5hbHlzaXM6IE1lbW9yeSBwZXIgR1BVIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSaW5nIGF0dGVudGlvblx1MDAyN3MgbWVtb3J5IGFkdmFudGFnZSBpcyBsaW5lYXIgaW4gTi4gV2l0aCBOIEdQVXMsIGVhY2ggaG9sZGluZyBML04gdG9rZW5zLCB0aGUgbG9jYWwgYXR0ZW50aW9uIG1hdHJpeCBpcyAoTC9OKcKyIOKAlCBOwrIgc21hbGxlciB0aGFuIHRoZSBmdWxsIEzCsiBtYXRyaXguIENvbWJpbmVkIHdpdGggRmxhc2hBdHRlbnRpb24gKHdoaWNoIGF2b2lkcyBtYXRlcmlhbGlzaW5nIGV2ZW4gdGhlIGxvY2FsIG1hdHJpeCksIHBlci1HUFUgbWVtb3J5IGZvciBhdHRlbnRpb24gaXMgTyhML04pIGluIHNlcXVlbmNlIGxlbmd0aC4gUGFyYW1ldGVyIG1lbW9yeSByZW1haW5zIHRoZSBzYW1lIGFjcm9zcyBHUFVzIChtb2RlbCB3ZWlnaHRzIGFyZSByZXBsaWNhdGVkIG9yIHRlbnNvci1wYXJ0aXRpb25lZCBzZXBhcmF0ZWx5KS4gQ29tbXVuaWNhdGlvbiBjb3N0IHBlciByaW5nIHN0ZXAgaXMgc2VuZGluZyBLIGFuZCBWIG9mIHNoYXBlIChCIMOXIGggw5cgTC9OIMOXIGRfaGVhZCkgdG8gdGhlIG5laWdoYm91cmluZyBHUFUg4oCUIHByb3BvcnRpb25hbCB0byBML04sIG5vdCBMwrIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBtYXRoXG5cbmRlZiByaW5nX2F0dGVudGlvbl9tZW1vcnkoTCwgTiwgaCwgZF9oZWFkLCBkdHlwZV9ieXRlcz0yKTpcbiAgICBcIlwiXCJFc3RpbWF0ZSBwZXItR1BVIG1lbW9yeSBmb3IgcmluZyBhdHRlbnRpb24gKGF0dGVudGlvbiB0ZW5zb3JzIG9ubHkpLlwiXCJcIlxuICAgIExzID0gTCAvLyBOICAjIHRva2VucyBwZXIgR1BVXG4gICAgIyBRLCBLLCBWIHNlZ21lbnRzOiBlYWNoIChoLCBMcywgZF9oZWFkKVxuICAgIHFrdl9tZW0gPSAzICogaCAqIExzICogZF9oZWFkICogZHR5cGVfYnl0ZXNcbiAgICAjIExvY2FsIGF0dGVudGlvbiBzY29yZSBibG9jayAod2l0aCBGbGFzaEF0dGVudGlvbiwgbmV2ZXIgZnVsbHkgbWF0ZXJpYWxpc2VkKVxuICAgICMgRmxhc2hBdHRlbnRpb24gdGlsZXMgd2l0aCBibG9ja19zaXplIGI6IG1heCBibG9jayA9IGggKiBMcyAqIGJcbiAgICBiID0gbWluKDEyOCwgTHMpXG4gICAgZmxhc2hfdGlsZSA9IGggKiBMcyAqIGIgKiBkdHlwZV9ieXRlc1xuICAgICMgT3V0cHV0IGJ1ZmZlciBPOiBzYW1lIHNoYXBlIGFzIFFcbiAgICBvdXRfbWVtID0gaCAqIExzICogZF9oZWFkICogZHR5cGVfYnl0ZXNcbiAgICAjIENvbW11bmljYXRpb246IG9uZSBLLFYgc2VuZCBwZXIgc3RlcFxuICAgIGNvbW1fcGVyX3N0ZXAgPSAyICogaCAqIExzICogZF9oZWFkICogZHR5cGVfYnl0ZXNcbiAgICByZXR1cm4gcWt2X21lbSArIGZsYXNoX3RpbGUgKyBvdXRfbWVtLCBjb21tX3Blcl9zdGVwXG5cbmgsIGRfaGVhZCA9IDE2LCA2NFxucHJpbnQoZlwie1x1MDAyN0xcdTAwMjc6XHUwMDNlOH0ge1x1MDAyN04gR1BVc1x1MDAyNzpcdTAwM2U4fSB7XHUwMDI3TWVtL0dQVSBNQlx1MDAyNzpcdTAwM2UxMn0ge1x1MDAyN0NvbW0vc3RlcCBNQlx1MDAyNzpcdTAwM2UxNH0ge1x1MDAyN0Z1bGwtYXR0biBNQlx1MDAyNzpcdTAwM2UxNH1cIilcbmZvciBMIGluIFs4MTkyLCAzMjc2OCwgMTMxMDcyLCA1MjQyODhdOlxuICAgIGZvciBOIGluIFsxLCA0LCA4LCAxNl06XG4gICAgICAgIGlmIEwgLy8gTiBcdTAwM2MgNjQ6XG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICBtZW0sIGNvbW0gPSByaW5nX2F0dGVudGlvbl9tZW1vcnkoTCwgTiwgaCwgZF9oZWFkKVxuICAgICAgICBmdWxsX2F0dG4gPSBoICogTCAqIEwgKiAyIC8gMTAyNCoqMiAgIyBmdWxsIExeMiBhdHRlbnRpb24sIGZsb2F0MTZcbiAgICAgICAgcHJpbnQoZlx1MDAyN3tMOlx1MDAzZTh9IHtOOlx1MDAzZTh9IHttZW0vMTAyNCoqMjpcdTAwM2UxMi4xZn0ge2NvbW0vMTAyNCoqMjpcdTAwM2UxNC4yZn0ge2Z1bGxfYXR0bjpcdTAwM2UxNC4xZn1cdTAwMjcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlN0cmF0ZWd5IiwiRGltZW5zaW9uIHBhcmFsbGVsaXplZCIsIkNvbW11bmljYXRpb24gcGF0dGVybiIsIk1heCBzZXF1ZW5jZSBsZW5ndGgiLCJVc2UgY2FzZSJdLCJyb3dzIjpbWyJEYXRhIHBhcmFsbGVsaXNtIiwiQmF0Y2ggKEIpIiwiQWxsUmVkdWNlIGdyYWRpZW50cyIsIlNpbmdsZS1HUFUgbGltaXQiLCJTdGFuZGFyZCB0cmFpbmluZyB3aXRoIGxhcmdlIGJhdGNoIl0sWyJUZW5zb3IgcGFyYWxsZWxpc20iLCJNb2RlbCB3ZWlnaHRzIChoIG9yIGRfbW9kZWwpIiwiQWxsUmVkdWNlIHBlciBsYXllciBmb3J3YXJkIiwiU2luZ2xlLUdQVSBsaW1pdCIsIkxhcmdlIG1vZGVscyB0aGF0IGRvblx1MDAyN3QgZml0IG9uIG9uZSBHUFUiXSxbIlNlcXVlbmNlIHBhcmFsbGVsaXNtIChub24tcmluZykiLCJTZXF1ZW5jZSAoTCkg4oCUIG5vbi1hdHRlbnRpb24gbGF5ZXJzIiwiQWxsR2F0aGVyIC8gUmVkdWNlU2NhdHRlciIsIk1vZGVzdCBpbXByb3ZlbWVudCIsIlVzZWQgaW4gTWVnYXRyb24tTE0gZm9yIExheWVyTm9ybSwgRHJvcG91dCJdLFsiUmluZyBhdHRlbnRpb24iLCJTZXF1ZW5jZSAoTCkg4oCUIGF0dGVudGlvbiBsYXllciIsIlAyUCBLLFYgcmluZyByb3RhdGlvbiAoTiBzdGVwcykiLCJMIMOXIE4gKGxpbmVhciBpbiBHUFUgY291bnQpIiwiVmVyeSBsb25nIGNvbnRleHRzOiAxMjhL4oCTMU0gdG9rZW5zIl0sWyJDb21iaW5lZCAoYWxsIGZvdXIpIiwiQiwgaCwgZF9tb2RlbCwgTCBzaW11bHRhbmVvdXNseSIsIkFsbCBvZiB0aGUgYWJvdmUiLCJQcm9kdWN0IG9mIGFsbCBheGVzIiwiR2VtaW5pL0xMYU1BIDMgbG9uZy1jb250ZXh0IHRyYWluaW5nIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21tdW5pY2F0aW9uIE92ZXJoZWFkIGFuZCBPdmVybGFwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSaW5nIGF0dGVudGlvbiByZXF1aXJlcyBOIHJpbmcgc3RlcHMgd2hlcmUgTiBpcyB0aGUgbnVtYmVyIG9mIEdQVXMuIEF0IGVhY2ggc3RlcCBHUFUgaSBzZW5kcyBpdHMgY3VycmVudCBLLFYgYmxvY2sgKEwvTiDDlyBoIMOXIGRfaGVhZCBmbG9hdHMpIHRvIEdQVSAoaSsxKSB3aGlsZSBzaW11bHRhbmVvdXNseSBjb21wdXRpbmcgbG9jYWwgYXR0ZW50aW9uIHdpdGggaXRzIGN1cnJlbnQgSyxWIGJsb2NrLiBJZiB0aGUgTlZMaW5rIG9yIEluZmluaUJhbmQgYmFuZHdpZHRoIGlzIHN1ZmZpY2llbnQgdG8gc2VuZCBML04gw5cgaCDDlyBkX2hlYWQgZmxvYXRzIGluIHRoZSB0aW1lIGl0IHRha2VzIHRvIHJ1biBGbGFzaEF0dGVudGlvbiBvbiBML04gw5cgTC9OIHRva2VucywgY29tbXVuaWNhdGlvbiBpcyBmdWxseSBoaWRkZW4uIEluIHByYWN0aWNlLCBmb3IgTlZMaW5rIGF0IDYwMCBHQi9zIGFuZCBBMTAwIGF0IH4zMDAgVEZMT1BTLCBjb21tdW5pY2F0aW9uIGlzIGhpZGRlbiBmb3IgTC9OIOKJpSA0MDk2IHdpdGggdHlwaWNhbCBtb2RlbCBkaW1lbnNpb25zLiBCbG9ja2luZyBSaW5nIEF0dGVudGlvbiByZWR1Y2VzIGNvbW11bmljYXRpb24gcm91bmRzIHRvIOKMiE4vMuKMiSBieSBiaWRpcmVjdGlvbmFsIHJpbmcgcm90YXRpb24uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJSaW5nIEF0dGVudGlvbiBFbmFibGVzIE1pbGxpb24tVG9rZW4gQ29udGV4dHMiLCJjb250ZW50IjoiUmluZyBhdHRlbnRpb24gc2NhbGVzIHNlcXVlbmNlIGxlbmd0aCBsaW5lYXJseSB3aXRoIEdQVSBjb3VudDogOCDDlyBBMTAwIEdQVXMgZWFjaCBoYW5kbGluZyAxMjhLIHRva2VucyA9IDFNIHRvdGFsIGNvbnRleHQuIFRoaXMgaXMgaG93IGxvbmctY29udGV4dCBMTGFNQSB2YXJpYW50cyAoTExhTUEgMy4xIHdpdGggMTI4SyBjb250ZXh0KSBhbmQgR2VtaW5pICgxTSBjb250ZXh0KSBhcmUgdHJhaW5lZC4gVGhlIGNvbW11bmljYXRpb24gb3ZlcmhlYWQgaXMgYm91bmRlZCBieSBML04gKG5vdCBMwrIpLCBhbmQgb3ZlcmxhcHMgd2l0aCBjb21wdXRlLiBGb3IgaW5mZXJlbmNlLCByaW5nIGF0dGVudGlvbiBpcyBsZXNzIGNvbW1vbiDigJQgS1YgY2FjaGUgY29tcHJlc3Npb24gKEdRQSwgTUxBKSBpcyBwcmVmZXJyZWQgYmVjYXVzZSBpbmZlcmVuY2UgaXMgdHlwaWNhbGx5IHNpbmdsZS1HUFUgb3IgdXNlcyBwaXBlbGluZSBwYXJhbGxlbGlzbS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb25nLUNvbnRleHQgVHJhaW5pbmcgaW4gUHJhY3RpY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJpbmcgYXR0ZW50aW9uIGlzIHByaW1hcmlseSBhIHRyYWluaW5nIHRlY2huaXF1ZSDigJQgaXQgZW5hYmxlcyBmaXR0aW5nIGxvbmcgc2VxdWVuY2VzIGludG8gR1BVIG1lbW9yeSBkdXJpbmcgdGhlIGZvcndhcmQgYW5kIGJhY2t3YXJkIHBhc3MuIEF0IGluZmVyZW5jZSwgdGhlIGZ1bGwgc2VxdWVuY2UgdHlwaWNhbGx5IGZpdHMgaW4gYSBzaW5nbGUgR1BVXHUwMDI3cyBtZW1vcnkgaWYgS1YgY2FjaGUgY29tcHJlc3Npb24gKEdRQSBvciBNTEEpIGlzIHVzZWQsIG1ha2luZyByaW5nIGF0dGVudGlvbiB1bm5lY2Vzc2FyeS4gUHJvZHVjdGlvbiBsb25nLWNvbnRleHQgdHJhaW5pbmcgcGlwZWxpbmVzIGNvbWJpbmUgcmluZyBhdHRlbnRpb24gKHNlcXVlbmNlIHBhcmFsbGVsaXNtKSB3aXRoIHRlbnNvciBwYXJhbGxlbGlzbSAoc3BsaXQgaGVhZHMgYWNyb3NzIEdQVXMpIGFuZCBkYXRhIHBhcmFsbGVsaXNtIChzcGxpdCBiYXRjaCkg4oCUIGFsbCB0aHJlZSBkaW1lbnNpb25zIHBhcnRpdGlvbmVkIHNpbXVsdGFuZW91c2x5LiBUaGUgY29kZSBjaGFuZ2VzIHJlcXVpcmVkIHRvIGFkZCByaW5nIGF0dGVudGlvbiB0byBhbiBleGlzdGluZyB0cmFuc2Zvcm1lciBhcmUgaXNvbGF0ZWQgdG8gdGhlIGF0dGVudGlvbiBsYXllcjsgdGhlIHJlc3Qgb2YgdGhlIHRyYW5zZm9ybWVyIG9wZXJhdGVzIG9uIEwvTiB0b2tlbiBzZWdtZW50cyB3aXRob3V0IG1vZGlmaWNhdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlJpbmcgYXR0ZW50aW9uIHBhcGVyIChMaXUgZXQgYWwuIDIwMjMpOiBmaXJzdCBwYXBlciB0byBkZW1vbnN0cmF0ZSBPKEwvTikgcGVyLUdQVSBtZW1vcnkgZm9yIGF0dGVudGlvbiBhY3Jvc3MgTiBHUFVzLiIsIkxMYU1BIDMuMSAoMTI4SyBjb250ZXh0KTogdHJhaW5lZCB3aXRoIHJpbmcgYXR0ZW50aW9uIGFjcm9zcyA4IEdQVXMgcGVyIHNlcXVlbmNlIGZvciBsb25nLWNvbnRleHQgdmFyaWFudHMuIiwiR2VtaW5pICgxTSBjb250ZXh0KTogdXNlcyBhIGNvbWJpbmF0aW9uIG9mIHJpbmctc3R5bGUgc2VxdWVuY2UgcGFyYWxsZWxpc20gYW5kIHRlbnNvciBwYXJhbGxlbGlzbS4iLCJCbG9ja2luZ1JpbmdBdHRlbnRpb246IHJlZHVjZXMgY29tbXVuaWNhdGlvbiBzdGVwcyBmcm9tIE4gdG8g4oyITi8y4oyJIHVzaW5nIGJpZGlyZWN0aW9uYWwgcmluZyByb3RhdGlvbi4iLCJFYXN5Q29udGV4dCAob3BlbiBzb3VyY2UpOiBQeVRvcmNoIGltcGxlbWVudGF0aW9uIG9mIHJpbmcgYXR0ZW50aW9uIHdpdGggRGVlcFNwZWVkIGFuZCBGU0RQIGludGVncmF0aW9uLiIsIlJpbmcgYXR0ZW50aW9uIGlzIG9ydGhvZ29uYWwgdG8gRmxhc2hBdHRlbnRpb24g4oCUIGVhY2ggcmluZyBzdGVwIHVzZXMgRmxhc2hBdHRlbnRpb24gaW50ZXJuYWxseSBmb3IgbWVtb3J5LWVmZmljaWVudCBsb2NhbCBjb21wdXRlLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Ring Attention — Sequence Parallelism for Long Contexts

Ring Attention (Liu et al. 2023) enables training on sequences far longer than a single GPU can hold by distributing the sequence across multiple GPUs. Each GPU holds a contiguous segment of Q, K, and V. The GPUs are arranged in a logical ring: at each step a GPU computes local attention between its Q segment and its current K,V segment, then passes its K,V to the next GPU in the ring. After N steps (N = number of GPUs), every Q has attended to every K and V. Crucially, the K,V communication overlaps with local FlashAttention computation, hiding most of the network latency.

## Sequence Parallelism and the Ring Communication Pattern

Tensor parallelism (Megatron-LM) splits model weights across GPUs. Data parallelism splits the batch. Sequence parallelism splits the sequence dimension L across GPUs. For N GPUs each holding L/N tokens, the local attention matrix is (L/N) × (L/N) instead of L × L — an N² reduction in per-GPU memory. Ring Attention implements sequence parallelism for attention: at step s, GPU i computes attention between its Q_i and the K,V block it currently holds (initially from GPU i, then cycled from GPU (i+s) mod N). After N steps, the partial attention outputs are combined using online softmax normalisation.

## Ring Attention Forward Pass

The ring attention algorithm: initialise output O_i = 0, running log-sum-exp lse_i = -∞ for each GPU i. For s = 0 to N-1: compute local attention scores A_{i,j} = Q_i K_jᵀ / √d where j = (i+s) mod N; update the running softmax using online normalisation (FlashAttention-style); send K_j, V_j to GPU (i+1) mod N while computing; receive K_{j-1}, V_{j-1} from GPU (i-1) mod N. After N steps each GPU holds O_i = softmax(Q_i [K_0; K_1; ...; K_{N-1}]ᵀ) V — the correct full-sequence attention output for its Q segment.

```python
import torch
import torch.nn.functional as F
import math

def ring_attention_simulate(Q_segs, K_segs, V_segs):
    """Simulate ring attention with Python lists (no actual multi-GPU comms).
    Q_segs, K_segs, V_segs: lists of tensors, one per GPU, shape (B,h,Ls,d).
    Returns: list of output segments, one per GPU.
    """
    N = len(Q_segs)  # number of GPUs
    B, h, Ls, d = Q_segs[0].shape
    # Each GPU maintains running output O and log-sum-exp for online softmax
    Os   = [torch.zeros(B, h, Ls, d) for _ in range(N)]
    lses = [torch.full((B, h, Ls, 1), float('-inf')) for _ in range(N)]
    kv_ring = list(zip(K_segs, V_segs))  # initial K,V assignment
    for step in range(N):
        for i in range(N):
            j = (i + step) % N          # which K,V block GPU i holds
            K_j, V_j = kv_ring[j]
            scores = Q_segs[i] @ K_j.transpose(-2,-1) / math.sqrt(d)  # (B,h,Ls,Ls)
            block_max = scores.max(dim=-1, keepdim=True).values
            exp_scores = torch.exp(scores - block_max)
            block_lse  = block_max + torch.log(exp_scores.sum(-1, keepdim=True))
            # Merge with running lse (online softmax)
            lse_new = torch.logaddexp(lses[i], block_lse)
            alpha = torch.exp(lses[i] - lse_new)
            beta  = torch.exp(block_lse - lse_new)
            Os[i]   = alpha * Os[i] + beta * (exp_scores / exp_scores.sum(-1,keepdim=True) @ V_j)
            lses[i] = lse_new
        # Simulate ring rotation: each GPU sends K,V to next
        kv_ring = [kv_ring[(i - 1) % N] for i in range(N)]
    return Os

N, B, h, Ls, d = 4, 1, 2, 8, 16  # 4 GPUs, 8 tokens each = 32 total
Q_segs = [torch.randn(B,h,Ls,d) for _ in range(N)]
K_segs = [torch.randn(B,h,Ls,d) for _ in range(N)]
V_segs = [torch.randn(B,h,Ls,d) for _ in range(N)]
Os = ring_attention_simulate(Q_segs, K_segs, V_segs)
Q_full = torch.cat(Q_segs, dim=2)
K_full = torch.cat(K_segs, dim=2)
V_full = torch.cat(V_segs, dim=2)
O_ref  = F.scaled_dot_product_attention(Q_full, K_full, V_full)
O_ring = torch.cat(Os, dim=2)
print(f'Ring output shape: {O_ring.shape}')
print(f'Max diff vs full attention: {(O_ring - O_ref).abs().max().item():.6f}')
```

## Online Normalisation for Distributed Softmax

The key algorithmic challenge in ring attention is combining partial softmax results computed on different K,V blocks. Standard softmax requires seeing all keys to compute the denominator Σ_j exp(q·kⱼ/√d). Online normalisation (from FlashAttention) maintains a running log-sum-exp (lse) that allows updating the output incrementally. For each new K block: compute block_lse, merge with running lse using logaddexp, rescale the previous output by exp(old_lse - new_lse), add the contribution from the new block scaled by exp(block_lse - new_lse). After all N ring steps, the output is numerically equivalent to full softmax attention.

```python
import torch
import math

def online_softmax_accumulate(q, k_blocks, v_blocks):
    """Accumulate attention over K,V blocks using online (log-sum-exp) normalisation.
    q: (L_q, d)  k_blocks/v_blocks: list of (L_k, d) tensors.
    Returns output (L_q, d) equivalent to full softmax attention.
    """
    d = q.shape[-1]
    L_q = q.shape[0]
    O   = torch.zeros(L_q, d)
    lse = torch.full((L_q, 1), float('-inf'))
    for K_b, V_b in zip(k_blocks, v_blocks):
        scores    = q @ K_b.T / math.sqrt(d)              # (L_q, L_k)
        block_max = scores.max(dim=-1, keepdim=True).values
        e_scores  = torch.exp(scores - block_max)          # numerically stable
        block_lse = block_max + torch.log(e_scores.sum(-1, keepdim=True))
        lse_new   = torch.logaddexp(lse, block_lse)
        alpha     = torch.exp(lse - lse_new)               # rescale old contribution
        beta      = torch.exp(block_lse - lse_new)         # scale new contribution
        O         = alpha * O + beta * (e_scores / e_scores.sum(-1,keepdim=True) @ V_b)
        lse       = lse_new
    return O

torch.manual_seed(1)
L, d = 32, 16
q = torch.randn(L, d)
K = torch.randn(L, d)
V = torch.randn(L, d)
# Split K, V into 4 blocks as if distributed across 4 GPUs
k_blocks = K.chunk(4, dim=0)
v_blocks = V.chunk(4, dim=0)
O_online = online_softmax_accumulate(q, k_blocks, v_blocks)
import torch.nn.functional as F
O_full = F.scaled_dot_product_attention(q.unsqueeze(0).unsqueeze(0),
             K.unsqueeze(0).unsqueeze(0), V.unsqueeze(0).unsqueeze(0)).squeeze()
print(f'Online norm max diff: {(O_online - O_full).abs().max().item():.8f}')
print('Numerically identical to full softmax attention across 4 blocks.')
```

## Combining Ring Attention with FlashAttention

In practice, ring attention does not compute naive local attention — it uses FlashAttention within each ring step for memory efficiency. FlashAttention tiles the local (L/N) × (L/N) attention matrix to avoid materialising it, keeping per-GPU memory O(L/N) rather than O((L/N)²). The combination: ring attention handles the sequence distribution across GPUs (inter-GPU level), FlashAttention handles the memory-efficient tiling within each GPU (intra-GPU level). Together they achieve O(L/N) memory per GPU in both sequence length and attention scores, enabling contexts of L = N × L_GPU where L_GPU is the per-GPU FlashAttention limit (~128K on an 80 GB A100).

```python
import torch
import torch.nn.functional as F
import math

def flash_attention_block(Q, K, V, block_size=32):
    """Simplified FlashAttention: tiled computation to avoid O(L^2) memory.
    Q: (B,h,Lq,d)  K,V: (B,h,Lk,d). Returns (B,h,Lq,d).
    """
    B, h, Lq, d = Q.shape
    Lk = K.shape[2]
    O   = torch.zeros_like(Q)
    lse = torch.full((B, h, Lq, 1), float('-inf'))
    for j in range(0, Lk, block_size):
        Kj = K[:, :, j:j+block_size]
        Vj = V[:, :, j:j+block_size]
        s  = Q @ Kj.transpose(-2,-1) / math.sqrt(d)
        bm = s.max(-1, keepdim=True).values
        e  = torch.exp(s - bm)
        bl = bm + torch.log(e.sum(-1, keepdim=True))
        lse_new = torch.logaddexp(lse, bl)
        O = torch.exp(lse - lse_new) * O + torch.exp(bl - lse_new) * (e / e.sum(-1,keepdim=True) @ Vj)
        lse = lse_new
    return O

def ring_flash_attention(Q_segs, K_segs, V_segs, block_size=16):
    """Ring attention with FlashAttention as the local compute kernel."""
    N = len(Q_segs)
    Os   = [torch.zeros_like(q) for q in Q_segs]
    lses = [torch.full((*q.shape[:3], 1), float('-inf')) for q in Q_segs]
    kv   = list(zip(K_segs, V_segs))
    for step in range(N):
        for i in range(N):
            j = (i + step) % N
            Kj, Vj = kv[j]
            block_out = flash_attention_block(Q_segs[i], Kj, Vj, block_size)
            # Merge using online normalisation at segment level
            bl = torch.log(torch.ones(*Q_segs[i].shape[:3], 1))  # simplified
            lse_new = torch.logaddexp(lses[i], bl)
            Os[i] = 0.5 * Os[i] + 0.5 * block_out  # simplified merge for demo
            lses[i] = lse_new
        kv = [kv[(i - 1) % N] for i in range(N)]
    return Os

N, B, h, Ls, d = 2, 1, 1, 16, 8
Q_segs = [torch.randn(B,h,Ls,d) for _ in range(N)]
K_segs = [torch.randn(B,h,Ls,d) for _ in range(N)]
V_segs = [torch.randn(B,h,Ls,d) for _ in range(N)]
Os = ring_flash_attention(Q_segs, K_segs, V_segs)
print(f'Ring+Flash: {N} GPUs, {Ls} tokens/GPU = {N*Ls} total tokens')
print(f'Output seg 0: {Os[0].shape}')
print(f'Per-GPU attn memory: O((Ls/block)^2) = O({Ls}^2) vs O({N*Ls}^2) full')
```

## Scaling Analysis: Memory per GPU

Ring attention's memory advantage is linear in N. With N GPUs, each holding L/N tokens, the local attention matrix is (L/N)² — N² smaller than the full L² matrix. Combined with FlashAttention (which avoids materialising even the local matrix), per-GPU memory for attention is O(L/N) in sequence length. Parameter memory remains the same across GPUs (model weights are replicated or tensor-partitioned separately). Communication cost per ring step is sending K and V of shape (B × h × L/N × d_head) to the neighbouring GPU — proportional to L/N, not L².

```python
import math

def ring_attention_memory(L, N, h, d_head, dtype_bytes=2):
    """Estimate per-GPU memory for ring attention (attention tensors only)."""
    Ls = L // N  # tokens per GPU
    # Q, K, V segments: each (h, Ls, d_head)
    qkv_mem = 3 * h * Ls * d_head * dtype_bytes
    # Local attention score block (with FlashAttention, never fully materialised)
    # FlashAttention tiles with block_size b: max block = h * Ls * b
    b = min(128, Ls)
    flash_tile = h * Ls * b * dtype_bytes
    # Output buffer O: same shape as Q
    out_mem = h * Ls * d_head * dtype_bytes
    # Communication: one K,V send per step
    comm_per_step = 2 * h * Ls * d_head * dtype_bytes
    return qkv_mem + flash_tile + out_mem, comm_per_step

h, d_head = 16, 64
print(f"{'L':>8} {'N GPUs':>8} {'Mem/GPU MB':>12} {'Comm/step MB':>14} {'Full-attn MB':>14}")
for L in [8192, 32768, 131072, 524288]:
    for N in [1, 4, 8, 16]:
        if L // N < 64:
            continue
        mem, comm = ring_attention_memory(L, N, h, d_head)
        full_attn = h * L * L * 2 / 1024**2  # full L^2 attention, float16
        print(f'{L:>8} {N:>8} {mem/1024**2:>12.1f} {comm/1024**2:>14.2f} {full_attn:>14.1f}')
```

| Strategy | Dimension parallelized | Communication pattern | Max sequence length | Use case |
| --- | --- | --- | --- | --- |
| Data parallelism | Batch (B) | AllReduce gradients | Single-GPU limit | Standard training with large batch |
| Tensor parallelism | Model weights (h or d_model) | AllReduce per layer forward | Single-GPU limit | Large models that don't fit on one GPU |
| Sequence parallelism (non-ring) | Sequence (L) — non-attention layers | AllGather / ReduceScatter | Modest improvement | Used in Megatron-LM for LayerNorm, Dropout |
| Ring attention | Sequence (L) — attention layer | P2P K,V ring rotation (N steps) | L × N (linear in GPU count) | Very long contexts: 128K–1M tokens |
| Combined (all four) | B, h, d_model, L simultaneously | All of the above | Product of all axes | Gemini/LLaMA 3 long-context training |

## Communication Overhead and Overlap

Ring attention requires N ring steps where N is the number of GPUs. At each step GPU i sends its current K,V block (L/N × h × d_head floats) to GPU (i+1) while simultaneously computing local attention with its current K,V block. If the NVLink or InfiniBand bandwidth is sufficient to send L/N × h × d_head floats in the time it takes to run FlashAttention on L/N × L/N tokens, communication is fully hidden. In practice, for NVLink at 600 GB/s and A100 at ~300 TFLOPS, communication is hidden for L/N ≥ 4096 with typical model dimensions. Blocking Ring Attention reduces communication rounds to ⌈N/2⌉ by bidirectional ring rotation.

> **Ring Attention Enables Million-Token Contexts**: Ring attention scales sequence length linearly with GPU count: 8 × A100 GPUs each handling 128K tokens = 1M total context. This is how long-context LLaMA variants (LLaMA 3.1 with 128K context) and Gemini (1M context) are trained. The communication overhead is bounded by L/N (not L²), and overlaps with compute. For inference, ring attention is less common — KV cache compression (GQA, MLA) is preferred because inference is typically single-GPU or uses pipeline parallelism.

## Long-Context Training in Practice

Ring attention is primarily a training technique — it enables fitting long sequences into GPU memory during the forward and backward pass. At inference, the full sequence typically fits in a single GPU's memory if KV cache compression (GQA or MLA) is used, making ring attention unnecessary. Production long-context training pipelines combine ring attention (sequence parallelism) with tensor parallelism (split heads across GPUs) and data parallelism (split batch) — all three dimensions partitioned simultaneously. The code changes required to add ring attention to an existing transformer are isolated to the attention layer; the rest of the transformer operates on L/N token segments without modification.

- Ring attention paper (Liu et al. 2023): first paper to demonstrate O(L/N) per-GPU memory for attention across N GPUs.
- LLaMA 3.1 (128K context): trained with ring attention across 8 GPUs per sequence for long-context variants.
- Gemini (1M context): uses a combination of ring-style sequence parallelism and tensor parallelism.
- BlockingRingAttention: reduces communication steps from N to ⌈N/2⌉ using bidirectional ring rotation.
- EasyContext (open source): PyTorch implementation of ring attention with DeepSpeed and FSDP integration.
- Ring attention is orthogonal to FlashAttention — each ring step uses FlashAttention internally for memory-efficient local compute.

---

