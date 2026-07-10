---
title: "Beyond Chinchilla — Inference-Aware Training and the LLaMA Efficiency Insight"
slug: "beyond-chinchilla"
description: "Chinchilla optimizes training compute but ignores inference cost. When serving at scale, smaller models trained on far more tokens dominate — the insight behind LLaMA-1, LLaMA-3, and the broader shift to inference-optimal training."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2hpbmNoaWxsYSBhbnN3ZXJzIHRoZSBxdWVzdGlvbjogZ2l2ZW4gYSBmaXhlZCB0cmFpbmluZyBjb21wdXRlIGJ1ZGdldCBDLCBob3cgc2hvdWxkIHlvdSBzcGxpdCBpdCBiZXR3ZWVuIG1vZGVsIHNpemUgTiBhbmQgdHJhaW5pbmcgdG9rZW5zIEQ/IFRoZSBhbnN3ZXIg4oCUIE4qIHByb3BvcnRpb25hbCB0byBDXjAuNSwgRCogPSAyMCpOKiDigJQgbWluaW1pemVzIHRoZSBmaW5hbCB0cmFpbmluZyBsb3NzLiBCdXQgdGhpcyBvYmplY3RpdmUgaWdub3JlcyB3aGF0IGhhcHBlbnMgYWZ0ZXIgdHJhaW5pbmcuIEF0IGRlcGxveW1lbnQgc2NhbGUsIGluZmVyZW5jZSBjb3N0IGR3YXJmcyB0cmFpbmluZyBjb3N0OiBhIG1vZGVsIHNlcnZpbmcgMSBtaWxsaW9uIHF1ZXJpZXMgcGVyIGRheSBydW5zIG1vcmUgdG90YWwgRkxPUHMgaW4gYSB3ZWVrIG9mIHNlcnZpbmcgdGhhbiB3ZXJlIHNwZW50IHRyYWluaW5nIGl0LiBUaGUgTExhTUEgaW5zaWdodCAoVG91dnJvbiBldCBhbC4sIDIwMjMpIHdhcyB0byBvcHRpbWl6ZSBmb3IgaW5mZXJlbmNlIGVmZmljaWVuY3kgYnkgdHJhaW5pbmcgc21hbGxlciBtb2RlbHMgb24gZmFyIG1vcmUgdG9rZW5zIHRoYW4gQ2hpbmNoaWxsYSByZWNvbW1lbmRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBDaGluY2hpbGxhIE1pc3NlcyBIYWxmIHRoZSBQaWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdG90YWwgY29zdCBvZiBhIGRlcGxveWVkIGxhbmd1YWdlIG1vZGVsIGhhcyB0d28gY29tcG9uZW50czogQ190b3RhbCA9IENfdHJhaW4gKyBDX2luZiwgd2hlcmUgQ190cmFpbiA9IDYqTipEICh0cmFpbmluZyBjb3N0KSBhbmQgQ19pbmYgPSAyKk4qUSAoaW5mZXJlbmNlIGNvc3QsIFEgPSB0b3RhbCBxdWVyaWVzIHNlcnZlZCkuIEZvciBhIDcwQiBtb2RlbCBzZXJ2aW5nIDFNIHF1ZXJpZXMgcGVyIGRheSwgdGhlIGRhaWx5IGluZmVyZW5jZSBjb3N0IGlzIDIgKiA3MGU5ICogMWU2ID0gMS40ZTE3IEZMT1BzIOKAlCBlcXVpdmFsZW50IHRvIHRyYWluaW5nIGEgMUIgcGFyYW1ldGVyIG1vZGVsIGZvciA3MDAgYmlsbGlvbiB0b2tlbnMuIEFmdGVyIG9uZSB5ZWFyIG9mIGRlcGxveW1lbnQsIGluZmVyZW5jZSBoYXMgY29uc3VtZWQgNWUxOSBGTE9QcyDigJQgbGlrZWx5IGV4Y2VlZGluZyB0aGUgdHJhaW5pbmcgY29zdC4gQSA3QiBtb2RlbCB0cmFpbmVkIDEweCBtb3JlIHdvdWxkIHNlcnZlIGVhY2ggcXVlcnkgYXQgMTB4IGxvd2VyIEZMT1AgY29zdCwgZHJhbWF0aWNhbGx5IHJlZHVjaW5nIENfaW5mIHdoaWxlIGFjaGlldmluZyBjb21wYXJhYmxlIHF1YWxpdHkuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJDX3RyYWluID0gNipOKkQ6IG9uZS10aW1lIGNvc3QsIHBhaWQgb25jZSBiZWZvcmUgZGVwbG95bWVudCIsIkNfaW5mID0gMipOIHBlciBxdWVyeTogc2NhbGVzIGxpbmVhcmx5IHdpdGggdG90YWwgcXVlcmllcyBzZXJ2ZWQsIHVuYm91bmRlZCIsIkF0IDFNIHF1ZXJpZXMvZGF5IGEgNzBCIG1vZGVsIHNwZW5kcyB+NWUxOSBGTE9Qcy95ZWFyIG9uIGluZmVyZW5jZSBhbG9uZSIsIkEgN0IgbW9kZWwgYXQgc2FtZSBxdWFsaXR5IGNvc3RzIDEweCBsZXNzIHBlciBxdWVyeTogMTB4IGJldHRlciBpbmZlcmVuY2UgZWNvbm9taWNzIiwiTExhTUEgaW5zaWdodDogdHJhaW4gN0Igb24gMVQgdG9rZW5zIGluc3RlYWQgb2YgNTBCIG9uIDEwMEIgdG9rZW5zIGZvciBzYW1lIHRyYWluaW5nIEMiLCJMTGFNQS0zLjEgOEIgdHJhaW5lZCBvbiAxNVQgdG9rZW5zOiA5M3ggQ2hpbmNoaWxsYS1vcHRpbWFsLCBvcHRpbWl6ZWQgZm9yIHNlcnZpbmciXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAxIOKAlCBJbmZlcmVuY2UtT3B0aW1hbCBBbGxvY2F0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5vcHRpbWl6ZSBpbXBvcnQgbWluaW1pemVfc2NhbGFyXG5cbkVfQ09OU1QsIEFfQ09OU1QsIEJfQ09OU1QsIEFMUEhBLCBCRVRBID0gMS42OSwgNDA2LjQsIDQxMC43LCAwLjM0LCAwLjI4XG5cbmRlZiB0b2tlbnNfZm9yX3RhcmdldF9sb3NzKE4sIHRhcmdldF9sb3NzPTIuNSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3RmluZCBEIHN1Y2ggdGhhdCBMKE4sIEQpID0gdGFyZ2V0X2xvc3MgdXNpbmcgQ2hpbmNoaWxsYSBmb3JtdWxhLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIHJlc2lkdWFsID0gdGFyZ2V0X2xvc3MgLSBFX0NPTlNUIC0gQV9DT05TVCAqIE4gKiogKC1BTFBIQSlcbiAgICBpZiByZXNpZHVhbCBcdTAwM2M9IDA6XG4gICAgICAgIHJldHVybiBucC5pbmYgICMgbW9kZWwgdG9vIHNtYWxsIHRvIHJlYWNoIHRhcmdldCByZWdhcmRsZXNzIG9mIGRhdGFcbiAgICByZXR1cm4gKEJfQ09OU1QgLyByZXNpZHVhbCkgKiogKDEuMCAvIEJFVEEpXG5cbmRlZiB0b3RhbF9jb3N0KE4sIFFfdG90YWwsIHRhcmdldF9sb3NzPTIuNSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3Q190b3RhbCA9IDYqTipEICh0cmFpbmluZykgKyAyKk4qUSAoaW5mZXJlbmNlIEZMT1BzKS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBEID0gdG9rZW5zX2Zvcl90YXJnZXRfbG9zcyhOLCB0YXJnZXRfbG9zcylcbiAgICBpZiBucC5pc2luZihEKTpcbiAgICAgICAgcmV0dXJuIG5wLmluZlxuICAgIHJldHVybiA2LjAgKiBOICogRCArIDIuMCAqIE4gKiBRX3RvdGFsXG5cbk5fcmFuZ2UgPSBucC5sb2dzcGFjZSg4LCAxMiwgMzAwKSAgIyAxMDBNIHRvIDFUIHBhcmFtZXRlcnNcblxucXVlcnlfc2NlbmFyaW9zID0gW1xuICAgIChcdTAwMjcxSyBxdWVyaWVzIChkZXYpXHUwMDI3LCAgIDFlMyksXG4gICAgKFx1MDAyNzFNIHF1ZXJpZXMgKHByb2QpXHUwMDI3LCAgMWU2KSxcbiAgICAoXHUwMDI3MUIgcXVlcmllcyAoc2NhbGUpXHUwMDI3LCAxZTkpLFxuXVxuXG5wcmludChcdTAwMjd7Olx1MDAzYzIyfSB7Olx1MDAzZTE0fSB7Olx1MDAzZTIwfSB7Olx1MDAzZTh9XHUwMDI3LmZvcm1hdChcdTAwMjdRdWVyeSBTY2FsZVx1MDAyNywgXHUwMDI3T3B0aW1hbCBOKiAoQilcdTAwMjcsIFx1MDAyN09wdGltYWwgRCogKEIgdG9rZW5zKVx1MDAyNywgXHUwMDI3RC9OXHUwMDI3KSlcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA2OClcbmZvciBsYWJlbCwgUSBpbiBxdWVyeV9zY2VuYXJpb3M6XG4gICAgY29zdHMgPSBucC5hcnJheShbdG90YWxfY29zdChOLCBRKSBmb3IgTiBpbiBOX3JhbmdlXSlcbiAgICB2YWxpZCA9IG5wLmlzZmluaXRlKGNvc3RzKVxuICAgIGJlc3RfaSA9IG5wLmFyZ21pbihucC53aGVyZSh2YWxpZCwgY29zdHMsIG5wLmluZikpXG4gICAgTl9iZXN0ID0gTl9yYW5nZVtiZXN0X2ldXG4gICAgRF9iZXN0ID0gdG9rZW5zX2Zvcl90YXJnZXRfbG9zcyhOX2Jlc3QpXG4gICAgcHJpbnQoXHUwMDI3ezpcdTAwM2MyMn0gezpcdTAwM2UxNC4yZn0gezpcdTAwM2UyMC4xZn0gezpcdTAwM2U4LjFmfVx1MDAyNy5mb3JtYXQobGFiZWwsIE5fYmVzdC8xZTksIERfYmVzdC8xZTksIERfYmVzdC9OX2Jlc3QpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBMTGFNQSBJbnNpZ2h0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUb3V2cm9uIGV0IGFsLiAoMjAyMykgb2JzZXJ2ZWQgdGhhdCBDaGluY2hpbGxhIG9wdGltaXplcyB0cmFpbmluZyBjb21wdXRlIGJ1dCBwcmFjdGl0aW9uZXJzIGNhcmUgbW9yZSBhYm91dCBpbmZlcmVuY2UgY29zdCBhdCBhIHRhcmdldCBxdWFsaXR5IGxldmVsLiBMTGFNQS0xIDdCIHdhcyB0cmFpbmVkIG9uIDFUIHRva2VucyDigJQgYXBwcm94aW1hdGVseSA3eCB0aGUgQ2hpbmNoaWxsYS1vcHRpbWFsIHRva2VuIGNvdW50IGZvciBhIDdCIG1vZGVsICh3aGljaCBpcyB+MTQwQiB0b2tlbnMpLiBUaGlzIG1lYW5zIExMYU1BLTEgN0IgYWNoaWV2ZXMgcm91Z2hseSB0aGUgc2FtZSBxdWFsaXR5IGFzIHRoZSBDaGluY2hpbGxhLW9wdGltYWwgbW9kZWwgZm9yIGEgNTBCIHBhcmFtZXRlciBzeXN0ZW0sIGJ1dCBydW5zIGluZmVyZW5jZSBhdCA3eCBsb3dlciBjb3N0IHBlciBxdWVyeS4gVGhlIG1vZGVsIHRvb2sgbG9uZ2VyIHRvIHRyYWluICg3eCBtb3JlIHRva2VucyksIGJ1dCB0aGF0IG9uZS10aW1lIGNvc3QgcGF5cyBvZmYgYWZ0ZXIgb25seSBhIHJlbGF0aXZlbHkgc21hbGwgbnVtYmVyIG9mIHF1ZXJpZXMgc2VydmVkLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTExhTUEtMSA3QjogMVQgdG9rZW5zIChDaGluY2hpbGxhLW9wdGltYWwgZm9yIDUwQiBtb2RlbCkg4oCUIDE0MyB0b2tlbnMvcGFyYW0iLCJMTGFNQS0zLjEgOEI6IDE1VCB0b2tlbnMg4oCUIGFwcHJveGltYXRlbHkgMSw4NzUgdG9rZW5zL3BhcmFtLCA5M3ggQ2hpbmNoaWxsYS1vcHRpbWFsIiwiTExhTUEtMy4xIDcwQjogMTVUIHRva2VucyDigJQgYXBwcm94aW1hdGVseSAyMTQgdG9rZW5zL3BhcmFtLCAxMC43eCBDaGluY2hpbGxhLW9wdGltYWwiLCJQaGktMyBNaW5pICgzLjhCLCAzLjNUIHRva2Vucyk6IDg2OCB0b2tlbnMvcGFyYW0g4oCUIGV4dHJlbWUgZGF0YS10by1wYXJhbSByYXRpbyIsIlF1YWxpdHkgb2Ygb3Zlci10cmFpbmVkIHNtYWxsIG1vZGVsIG9mdGVuIG1hdGNoZXMgcXVhbGl0eSBvZiBDaGluY2hpbGxhLW9wdGltYWwgbGFyZ2VyIG1vZGVsIiwiQnJlYWstZXZlbiBxdWVyaWVzOiAoQ19vdmVyX3RyYWluIC0gQ19jaGluX3RyYWluKSAvIChDX2luZl9sYXJnZSAtIENfaW5mX3NtYWxsKSJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIENvc3QgQ29tcGFyaXNvbiBhdCBEZXBsb3ltZW50IFNjYWxlIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5FX0NPTlNULCBBX0NPTlNULCBCX0NPTlNULCBBTFBIQSwgQkVUQSA9IDEuNjksIDQwNi40LCA0MTAuNywgMC4zNCwgMC4yOFxuXG5kZWYgdG9rZW5zX2Zvcl90YXJnZXQoTiwgTF90YXJnZXQ9Mi41KTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdUb2tlbnMgbmVlZGVkIHRvIHJlYWNoIExfdGFyZ2V0IHdpdGggTiBwYXJhbWV0ZXJzLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIHJlcyA9IExfdGFyZ2V0IC0gRV9DT05TVCAtIEFfQ09OU1QgKiBOICoqICgtQUxQSEEpXG4gICAgcmV0dXJuIChCX0NPTlNUIC8gcmVzKSAqKiAoMS4wIC8gQkVUQSkgaWYgcmVzIFx1MDAzZSAwIGVsc2UgbnAuaW5mXG5cbk5fcmFuZ2UgICA9IG5wLmxvZ3NwYWNlKDgsIDEyLCAxNTApICAjIDEwME0gdG8gMVQgcGFyYW1zXG5zY2VuYXJpb3MgPSBbXG4gICAgKFx1MDAyNzFLIHF1ZXJpZXNcdTAwMjcsICAxZTMsICBcdTAwMjcjMzQ5OGRiXHUwMDI3KSxcbiAgICAoXHUwMDI3MU0gcXVlcmllc1x1MDAyNywgIDFlNiwgIFx1MDAyNyNlNjdlMjJcdTAwMjcpLFxuICAgIChcdTAwMjcxQiBxdWVyaWVzXHUwMDI3LCAgMWU5LCAgXHUwMDI3I2U3NGMzY1x1MDAyNyksXG5dXG5cbmZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oMTAsIDYpKVxuZm9yIGxhYmVsLCBRLCBjb2xvciBpbiBzY2VuYXJpb3M6XG4gICAgY29zdHMgPSBbXVxuICAgIGZvciBOIGluIE5fcmFuZ2U6XG4gICAgICAgIEQgPSB0b2tlbnNfZm9yX3RhcmdldChOKVxuICAgICAgICBjb3N0cy5hcHBlbmQoNi4wICogTiAqIEQgKyAyLjAgKiBOICogUSBpZiBucC5pc2Zpbml0ZShEKSBlbHNlIG5wLmluZilcbiAgICBjb3N0cyA9IG5wLmFycmF5KGNvc3RzKVxuICAgIHZhbGlkID0gbnAuaXNmaW5pdGUoY29zdHMpXG4gICAgYXguc2VtaWxvZ3koTl9yYW5nZVt2YWxpZF0gLyAxZTksIGNvc3RzW3ZhbGlkXSwgY29sb3I9Y29sb3IsIGx3PTIsIGxhYmVsPWxhYmVsKVxuICAgIGJlc3RfaSA9IGludChucC5hcmdtaW4obnAud2hlcmUodmFsaWQsIGNvc3RzLCBucC5pbmYpKSlcbiAgICBheC5heHZsaW5lKE5fcmFuZ2VbYmVzdF9pXSAvIDFlOSwgY29sb3I9Y29sb3IsIGxzPVx1MDAyNzpcdTAwMjcsIGFscGhhPTAuNylcblxuYXguc2V0X3hsYWJlbChcdTAwMjdNb2RlbCBTaXplIE4gKGJpbGxpb25zIG9mIHBhcmFtZXRlcnMpXHUwMDI3LCBmb250c2l6ZT0xMilcbmF4LnNldF95bGFiZWwoXHUwMDI3VG90YWwgQ29zdCAodHJhaW4gKyBpbmZlcmVuY2UgRkxPUHMpXHUwMDI3LCBmb250c2l6ZT0xMilcbmF4LnNldF90aXRsZShcdTAwMjdJbmZlcmVuY2UtQXdhcmUgVG90YWwgQ29zdCB2cyBNb2RlbCBTaXplIGF0IERpZmZlcmVudCBEZXBsb3ltZW50IFNjYWxlc1x1MDAyNywgZm9udHNpemU9MTEpXG5heC5sZWdlbmQoZm9udHNpemU9MTEpXG5heC5ncmlkKFRydWUsIGFscGhhPTAuMylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3aW5mZXJlbmNlX2Nvc3RfY29tcGFyaXNvbi5wbmdcdTAwMjcsIGRwaT0xNTApXG5wbHQuc2hvdygpXG5wcmludChcdTAwMjdEb3R0ZWQgdmVydGljYWwgbGluZXMgbWFyayBpbmZlcmVuY2Utb3B0aW1hbCBOKiBmb3IgZWFjaCBkZXBsb3ltZW50IHNjYWxlLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1FcG9jaCBUcmFpbmluZyBFZmZlY3RzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGEgbW9kZWwgaXMgdHJhaW5lZCBiZXlvbmQgdGhlIENoaW5jaGlsbGEtb3B0aW1hbCB0b2tlbiBjb3VudCwgaXQgd2lsbCBpbmV2aXRhYmx5IHJldmlzaXQgdG9rZW5zIGlmIHRoZSB1bmlxdWUgZGF0YSBjb3JwdXMgaXMgc21hbGxlciB0aGFuIEQqLiBNdWx0aXBsZSBlcG9jaHMgb3ZlciB0aGUgc2FtZSBkYXRhIGV4aGliaXQgZGltaW5pc2hpbmcgcmV0dXJuczogdGhlIGVmZmVjdGl2ZSBkYXRhIGNvbnRyaWJ1dGlvbiBmcm9tIHJlcGVhdGVkIHRva2VucyBzY2FsZXMgc3ViLWxpbmVhcmx5IChyb3VnaGx5IGFzIGVwb2Noc14wLjUgZW1waXJpY2FsbHkpLiBBdCB2ZXJ5IGhpZ2ggZXBvY2ggY291bnRzIOKAlCBzYXksIDEwMCBwYXNzZXMgb3ZlciB0aGUgc2FtZSBkYXRhIOKAlCBsb3NzIGRlZ3JhZGF0aW9uIGNhbiBiZWNvbWUgc2lnbmlmaWNhbnQsIGFzIHRoZSBtb2RlbCBiZWdpbnMgdG8gbWVtb3JpemUgcmF0aGVyIHRoYW4gZ2VuZXJhbGl6ZS4gVGhlIHByYWN0aWNhbCBtaXRpZ2F0aW9uIGlzIGFnZ3Jlc3NpdmUgZGF0YSBjdXJhdGlvbiwgZGVkdXBsaWNhdGlvbiwgYW5kIG1peGluZyBpbiBzeW50aGV0aWMgZGF0YSAoYXMgd2l0aCBQaGktMyBhbmQgcmVsYXRlZCBtb2RlbHMpIHRvIG1haW50YWluIGRhdGEgZGl2ZXJzaXR5IGV2ZW4gYXQgaGlnaCB0b2tlbiBjb3VudHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAzIOKAlCBNdWx0aS1FcG9jaCBUcmFpbmluZyBEZWdyYWRhdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIGxvc3Nfd2l0aF9yZXBldGl0aW9uKE4sIERfdW5pcXVlLCBlcG9jaHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgRT0xLjY5LCBBPTQwNi40LCBhbHBoYT0wLjM0LCBCPTQxMC43LCBiZXRhPTAuMjgpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN01vZGVsIGxvc3MgdW5kZXIgZGF0YSByZXBldGl0aW9uOiBEX2VmZmVjdGl2ZSA9IERfdW5pcXVlICogZXBvY2hzXjAuNVxuICAgIChzdWItbGluZWFyIGVmZmVjdGl2ZSBkYXRhIGdhaW4gZnJvbSByZXBlYXRlZCB0b2tlbnMpLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIERfZWZmID0gRF91bmlxdWUgKiAoZXBvY2hzICoqIDAuNSlcbiAgICByZXR1cm4gRSArIEEgKiBOICoqICgtYWxwaGEpICsgQiAqIERfZWZmICoqICgtYmV0YSlcblxuTiAgICAgICAgPSA3ZTkgICAgIyA3QiBwYXJhbWV0ZXIgbW9kZWxcbkRfdW5pcXVlID0gMTAwZTkgICMgMTAwQiB1bmlxdWUgaGlnaC1xdWFsaXR5IHRva2Vuc1xuZXBvY2hzICAgPSBucC5saW5zcGFjZSgxLjAsIDI1LjAsIDI1MClcbmxvc3NlcyAgID0gW2xvc3Nfd2l0aF9yZXBldGl0aW9uKE4sIERfdW5pcXVlLCBlKSBmb3IgZSBpbiBlcG9jaHNdXG5cbmNoaW5jaGlsbGFfRCAgICAgPSAyMC4wICogTiAgICAgICAgICMgMTQwQiA9IENoaW5jaGlsbGEtb3B0aW1hbFxuY2hpbmNoaWxsYV9lcG9jaCA9IGNoaW5jaGlsbGFfRCAvIERfdW5pcXVlICAgIyAxLjQgZXBvY2hzXG5cbmZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oOSwgNSkpXG5heC5wbG90KGVwb2NocywgbG9zc2VzLCBcdTAwMjdiLVx1MDAyNywgbHc9MiwgbGFiZWw9XHUwMDI3VGVzdCBsb3NzIHdpdGggZGF0YSByZXBldGl0aW9uXHUwMDI3KVxuYXguYXh2bGluZShjaGluY2hpbGxhX2Vwb2NoLCBjb2xvcj1cdTAwMjdnXHUwMDI3LCBscz1cdTAwMjctLVx1MDAyNywgbHc9MixcbiAgICAgICAgICAgbGFiZWw9XHUwMDI3Q2hpbmNoaWxsYS1vcHRpbWFsICh7Oi4xZn0gZXBvY2hzKVx1MDAyNy5mb3JtYXQoY2hpbmNoaWxsYV9lcG9jaCkpXG5heC5heGhsaW5lKG1pbihsb3NzZXMpLCBjb2xvcj1cdTAwMjdncmF5XHUwMDI3LCBscz1cdTAwMjc6XHUwMDI3LCBsdz0xLjUsIGxhYmVsPVx1MDAyN0Jlc3QgYWNoaWV2YWJsZSBsb3NzXHUwMDI3KVxuYXguc2V0X3hsYWJlbChcdTAwMjdUcmFpbmluZyBFcG9jaHMgT3ZlciBVbmlxdWUgRGF0YVx1MDAyNywgZm9udHNpemU9MTIpXG5heC5zZXRfeWxhYmVsKFx1MDAyN1ByZWRpY3RlZCBUZXN0IExvc3MgKG5hdHMpXHUwMDI3LCBmb250c2l6ZT0xMilcbmF4LnNldF90aXRsZShcdTAwMjdNdWx0aS1FcG9jaCBUcmFpbmluZzogRGltaW5pc2hpbmcgUmV0dXJucyBQYXN0IENoaW5jaGlsbGEtT3B0aW1hbFx1MDAyNywgZm9udHNpemU9MTIpXG5heC5sZWdlbmQoZm9udHNpemU9MTEpXG5heC5ncmlkKFRydWUsIGFscGhhPTAuMylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3bXVsdGlfZXBvY2hfZGVncmFkYXRpb24ucG5nXHUwMDI3LCBkcGk9MTUwKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgNCDigJQgTExhTUEgdnMgQ2hpbmNoaWxsYS1PcHRpbWFsIENvbXBhcmlzb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBjaGluY2hpbGxhX29wdGltYWxfdG9rZW5zKE4pOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0NoaW5jaGlsbGEtb3B0aW1hbCB0b2tlbiBjb3VudCBmb3IgTiBwYXJhbWV0ZXJzOiBEKiA9IDIwICogTi5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICByZXR1cm4gMjAuMCAqIE5cblxuIyBQdWJsaXNoZWQgbW9kZWwgc3BlY3M6IChuYW1lLCBOX3BhcmFtcywgRF90b2tlbnNfYWN0dWFsKVxucHVibGlzaGVkX21vZGVscyA9IFtcbiAgICAoXHUwMDI3TExhTUEtMSA3Qlx1MDAyNywgICAgN2U5LCAgICAxLjBlMTIpLFxuICAgIChcdTAwMjdMTGFNQS0zLjEgOEJcdTAwMjcsICA4ZTksICAgMTUuMGUxMiksXG4gICAgKFx1MDAyN0xMYU1BLTIgNzBCXHUwMDI3LCAgNzBlOSwgICAgMi4wZTEyKSxcbiAgICAoXHUwMDI3TExhTUEtMy4xIDcwQlx1MDAyNyw3MGU5LCAgIDE1LjBlMTIpLFxuICAgIChcdTAwMjdNaXN0cmFsIDdCXHUwMDI3LCAgICA3ZTksICAgIDIuMGUxMiksXG4gICAgKFx1MDAyN1BoaS0zIE1pbmlcdTAwMjcsICAgIDMuOGU5LCAgMy4zZTEyKSxcbl1cblxucHJpbnQoXHUwMDI3ezpcdTAwM2MxOH0gezpcdTAwM2U3fSB7Olx1MDAzZTEzfSB7Olx1MDAzZTE4fSB7Olx1MDAzZTEyfSB7Olx1MDAzZTE2fVx1MDAyNy5mb3JtYXQoXG4gICAgXHUwMDI3TW9kZWxcdTAwMjcsIFx1MDAyN04gKEIpXHUwMDI3LCBcdTAwMjdEIGFjdHVhbCAoQilcdTAwMjcsIFx1MDAyN0QgQ2hpbmNoaWxsYSAoQilcdTAwMjcsIFx1MDAyN011bHRpcGxpZXJcdTAwMjcsIFx1MDAyN0NfdHJhaW4gKEZMT1BzKVx1MDAyNykpXG5wcmludChcdTAwMjctXHUwMDI3ICogOTApXG5mb3IgbmFtZSwgTiwgRCBpbiBwdWJsaXNoZWRfbW9kZWxzOlxuICAgIERfY2ggPSBjaGluY2hpbGxhX29wdGltYWxfdG9rZW5zKE4pXG4gICAgbXVsdCA9IEQgLyBEX2NoXG4gICAgQyAgICA9IDYuMCAqIE4gKiBEXG4gICAgcHJpbnQoXHUwMDI3ezpcdTAwM2MxOH0gezpcdTAwM2U3LjFmfSB7Olx1MDAzZTEzLjFmfSB7Olx1MDAzZTE4LjFmfSB7Olx1MDAzZTEyLjFmfXggezpcdTAwM2UxNi4yZX1cdTAwMjcuZm9ybWF0KFxuICAgICAgICBuYW1lLCBOLzFlOSwgRC8xZTksIERfY2gvMWU5LCBtdWx0LCBDKSlcbnByaW50KFx1MDAyN1xcbk1vZGVscyB0cmFpbmVkIHdlbGwgYmV5b25kIENoaW5jaGlsbGEtb3B0aW1hbCBhcmUgaW5mZXJlbmNlLW9wdGltaXplZCBmb3IgZGVwbG95bWVudC5cdTAwMjcpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdGFibGUgYmVsb3cgc3VtbWFyaXplcyB0aGUgaW5mZXJlbmNlLWF3YXJlIHBpY3R1cmUgZm9yIG5vdGFibGUgbW9kZWxzIOKAlCBzaG93aW5nIGhvdyBmYXIgZWFjaCBkZXZpYXRlcyBmcm9tIENoaW5jaGlsbGEtb3B0aW1hbCBhbmQgd2hhdCBkZXBsb3ltZW50IGNvbnRleHQgdGhhdCBjaG9pY2Ugc2VydmVzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIlBhcmFtcyAoQikiLCJUb2tlbnMgKEIpIiwiRC9OIFJhdGlvIiwiQ2hpbmNoaWxsYSBNdWx0aXBsaWVyIiwiUHJpbWFyeSBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJMTGFNQS0zLjEgOEIiLCI4IiwiMTUwMDAiLCIxODc1IiwiOTMuNzV4IiwiRWRnZSAvIG9uLWRldmljZSBpbmZlcmVuY2UiXSxbIkxMYU1BLTMuMSA3MEIiLCI3MCIsIjE1MDAwIiwiMjE0IiwiMTAuN3giLCJIaWdoLXF1YWxpdHkgaG9zdGVkIGluZmVyZW5jZSJdLFsiTWlzdHJhbCA3QiIsIjciLCIyMDAwIiwiMjg2IiwiMTQuM3giLCJFZmZpY2llbnQgbG9jYWwgZGVwbG95bWVudCJdLFsiUGhpLTMgTWluaSIsIjMuOCIsIjMzMDAiLCI4NjgiLCI0My40eCIsIk1vYmlsZSAvIGVkZ2UgZGV2aWNlIGluZmVyZW5jZSJdLFsiR2VtbWEgMiA5QiIsIjkiLCI4MDAwIiwiODg5IiwiNDQuNHgiLCJFZmZpY2llbnQgZmluZS10dW5pbmcgYmFzZSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgU2FyZGFuYSAvIENoaW5jaGlsbGEtaW5mIGZyYW1ld29yayAoU2FyZGFuYSBcdTAwMjYgRnJhbmtsZSwgMjAyMykgZm9ybWFsaXplcyB0aGUgaW5mZXJlbmNlLWF3YXJlIG9iamVjdGl2ZTogbWluaW1pemUgQ190cmFpbiArIGxhbWJkYSAqIENfaW5mLCB3aGVyZSBsYW1iZGEgcmVwcmVzZW50cyB0aGUgZXhwZWN0ZWQgdG90YWwgcXVlcnkgdm9sdW1lLiBTb2x2aW5nIHRoaXMgbW9kaWZpZWQgb3B0aW1pemF0aW9uIHlpZWxkcyBhIG5ldyBvcHRpbWFsIE4qIHRoYXQgaXMgc3RyaWN0bHkgc21hbGxlciB0aGFuIENoaW5jaGlsbGEtb3B0aW1hbCBOKiBmb3IgYW55IGxhbWJkYSBcdTAwM2UgMC4gQXMgbGFtYmRhIGdyb3dzIChtb3JlIHF1ZXJpZXMgZXhwZWN0ZWQpLCB0aGUgb3B0aW1hbCBtb2RlbCBzaHJpbmtzIGFuZCB0aGUgb3B0aW1hbCB0b2tlbiBjb3VudCBncm93cy4gVGhpcyBleHBsYWlucyB0aGUgb2JzZXJ2ZWQgdHJlbmQ6IGZyb250aWVyIGxhYnMgYXJlIGNvbnZlcmdpbmcgb24gc21hbGxlciwgbG9uZ2VyLXRyYWluZWQgbW9kZWxzIGZvciBwdWJsaWMgZGVwbG95bWVudC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNhcmRhbmEgb2JqZWN0aXZlOiBtaW5pbWl6ZSA2Kk4qRCArIGxhbWJkYSoyKk4qUSBzdWJqZWN0IHRvIEwoTixEKSBcdTAwM2M9IExfdGFyZ2V0IiwiRm9yIGxhbWJkYSA9IDAgKG5vIGluZmVyZW5jZSk6IHJlY292ZXJzIENoaW5jaGlsbGEtb3B0aW1hbCBOKiBhbmQgRCoiLCJGb3IgbGFyZ2UgbGFtYmRhOiBvcHRpbWFsIE4qIHNocmlua3MsIG9wdGltYWwgRCogZ3Jvd3MgcHJvcG9ydGlvbmFsbHkiLCJCcmVhay1ldmVuOiBleHRyYSB0cmFpbmluZyBjb3N0IC8gcGVyLXF1ZXJ5IHNhdmluZ3MgPSBudW1iZXIgb2YgcXVlcmllcyB0byByZWNvdXAiLCJMTGFNQS0zLjEgOEIgdnMgNzBCOiA4QiBjb3N0cyB+OXggbGVzcyBwZXIgcXVlcnksIHdvcnRoIHRyYWluaW5nIGxvbmdlciBmb3IgaGlnaC12b2x1bWUgQVBJcyIsIlN5bnRoZXRpYyBkYXRhIChQaGktMyBhcHByb2FjaCkgZW5hYmxlcyBoaWdoIHRva2VuIGNvdW50cyB3aXRob3V0IHdlYiBkYXRhIHJlcGV0aXRpb24iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlRpcCIsImNvbnRlbnQiOiJJZiB5b3UgZXhwZWN0IHRvIHNlcnZlIGEgbW9kZWwgZm9yIG1pbGxpb25zIG9mIHF1ZXJpZXMsIHRyYWluaW5nIGEgMi00eCBzbWFsbGVyIG1vZGVsIG9uIDQtOHggbW9yZSB0b2tlbnMgb2Z0ZW4gZ2l2ZXMgYmV0dGVyIHRvdGFsIGNvc3QgKHRyYWluICsgc2VydmUpIHRoYW4gdGhlIENoaW5jaGlsbGEtb3B0aW1hbCBtb2RlbCDigJQgc21hbGxlciBtb2RlbHMgYXJlIGRyYW1hdGljYWxseSBjaGVhcGVyIHBlciBpbmZlcmVuY2UgcXVlcnkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIFNoaWZ0aW5nIEZyb250aWVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZmllbGQgaGFzIG1vdmVkIGRlY2lzaXZlbHkgYmV5b25kIENoaW5jaGlsbGEtb3B0aW1hbCB0cmFpbmluZy4gTExhTUEtMy4xIDhCICgxNVQgdG9rZW5zLCA5M3ggQ2hpbmNoaWxsYS1vcHRpbWFsKSBkZW1vbnN0cmF0ZXMgdGhhdCBzbWFsbCBtb2RlbHMgdHJhaW5lZCBleHRyZW1lbHkgbG9uZyBjYW4gbWF0Y2ggbXVjaCBsYXJnZXIgQ2hpbmNoaWxsYS1vcHRpbWFsIG1vZGVscyBpbiBxdWFsaXR5IHdoaWxlIHJ1bm5pbmcgYXQgYSBmcmFjdGlvbiBvZiB0aGUgaW5mZXJlbmNlIGNvc3QuIFRoZSBpbXBsaWNhdGlvbiBmb3IgcHJhY3RpdGlvbmVyczogd2hlbiBjaG9vc2luZyBhIGJhc2UgbW9kZWwgZm9yIGZpbmUtdHVuaW5nIG9yIGRlcGxveW1lbnQsIHByZWZlciBtb2RlbHMgdGhhdCBoYXZlIGJlZW4gb3Zlci10cmFpbmVkIHJlbGF0aXZlIHRvIENoaW5jaGlsbGEg4oCUIHRoZXkgd2lsbCBiZSBzbWFsbGVyIChjaGVhcGVyIHRvIHNlcnZlKSwgZmFzdGVyIChsb3dlciBsYXRlbmN5KSwgYW5kIG9mdGVuIGNvbXBhcmFibGUgaW4gcXVhbGl0eSB0byBsYXJnZXIgQ2hpbmNoaWxsYS1vcHRpbWFsIGNvdW50ZXJwYXJ0cyBvbiBzdGFuZGFyZCBiZW5jaG1hcmtzLiBUaGUgY29tcHV0ZS1vcHRpbWFsIHF1ZXN0aW9uIGlzIG5vIGxvbmdlciBqdXN0IGFib3V0IHRyYWluaW5nIOKAlCBpdCBpcyBhYm91dCB0aGUgZnVsbCBsaWZlY3ljbGUgY29zdCBmcm9tIHByZS10cmFpbmluZyB0aHJvdWdoIG1pbGxpb25zIG9mIGluZmVyZW5jZSBjYWxscy4ifV0="
---
# Beyond Chinchilla — Inference-Aware Training and the LLaMA Efficiency Insight

Chinchilla answers the question: given a fixed training compute budget C, how should you split it between model size N and training tokens D? The answer — N* proportional to C^0.5, D* = 20*N* — minimizes the final training loss. But this objective ignores what happens after training. At deployment scale, inference cost dwarfs training cost: a model serving 1 million queries per day runs more total FLOPs in a week of serving than were spent training it. The LLaMA insight (Touvron et al., 2023) was to optimize for inference efficiency by training smaller models on far more tokens than Chinchilla recommends.

## Why Chinchilla Misses Half the Picture

The total cost of a deployed language model has two components: C_total = C_train + C_inf, where C_train = 6*N*D (training cost) and C_inf = 2*N*Q (inference cost, Q = total queries served). For a 70B model serving 1M queries per day, the daily inference cost is 2 * 70e9 * 1e6 = 1.4e17 FLOPs — equivalent to training a 1B parameter model for 700 billion tokens. After one year of deployment, inference has consumed 5e19 FLOPs — likely exceeding the training cost. A 7B model trained 10x more would serve each query at 10x lower FLOP cost, dramatically reducing C_inf while achieving comparable quality.

- C_train = 6*N*D: one-time cost, paid once before deployment
- C_inf = 2*N per query: scales linearly with total queries served, unbounded
- At 1M queries/day a 70B model spends ~5e19 FLOPs/year on inference alone
- A 7B model at same quality costs 10x less per query: 10x better inference economics
- LLaMA insight: train 7B on 1T tokens instead of 50B on 100B tokens for same training C
- LLaMA-3.1 8B trained on 15T tokens: 93x Chinchilla-optimal, optimized for serving

## Code 1 — Inference-Optimal Allocation

```python
import numpy as np
from scipy.optimize import minimize_scalar

E_CONST, A_CONST, B_CONST, ALPHA, BETA = 1.69, 406.4, 410.7, 0.34, 0.28

def tokens_for_target_loss(N, target_loss=2.5):
    '''Find D such that L(N, D) = target_loss using Chinchilla formula.'''
    residual = target_loss - E_CONST - A_CONST * N ** (-ALPHA)
    if residual <= 0:
        return np.inf  # model too small to reach target regardless of data
    return (B_CONST / residual) ** (1.0 / BETA)

def total_cost(N, Q_total, target_loss=2.5):
    '''C_total = 6*N*D (training) + 2*N*Q (inference FLOPs).'''
    D = tokens_for_target_loss(N, target_loss)
    if np.isinf(D):
        return np.inf
    return 6.0 * N * D + 2.0 * N * Q_total

N_range = np.logspace(8, 12, 300)  # 100M to 1T parameters

query_scenarios = [
    ('1K queries (dev)',   1e3),
    ('1M queries (prod)',  1e6),
    ('1B queries (scale)', 1e9),
]

print('{:<22} {:>14} {:>20} {:>8}'.format('Query Scale', 'Optimal N* (B)', 'Optimal D* (B tokens)', 'D/N'))
print('-' * 68)
for label, Q in query_scenarios:
    costs = np.array([total_cost(N, Q) for N in N_range])
    valid = np.isfinite(costs)
    best_i = np.argmin(np.where(valid, costs, np.inf))
    N_best = N_range[best_i]
    D_best = tokens_for_target_loss(N_best)
    print('{:<22} {:>14.2f} {:>20.1f} {:>8.1f}'.format(label, N_best/1e9, D_best/1e9, D_best/N_best))
```

## The LLaMA Insight

Touvron et al. (2023) observed that Chinchilla optimizes training compute but practitioners care more about inference cost at a target quality level. LLaMA-1 7B was trained on 1T tokens — approximately 7x the Chinchilla-optimal token count for a 7B model (which is ~140B tokens). This means LLaMA-1 7B achieves roughly the same quality as the Chinchilla-optimal model for a 50B parameter system, but runs inference at 7x lower cost per query. The model took longer to train (7x more tokens), but that one-time cost pays off after only a relatively small number of queries served.

- LLaMA-1 7B: 1T tokens (Chinchilla-optimal for 50B model) — 143 tokens/param
- LLaMA-3.1 8B: 15T tokens — approximately 1,875 tokens/param, 93x Chinchilla-optimal
- LLaMA-3.1 70B: 15T tokens — approximately 214 tokens/param, 10.7x Chinchilla-optimal
- Phi-3 Mini (3.8B, 3.3T tokens): 868 tokens/param — extreme data-to-param ratio
- Quality of over-trained small model often matches quality of Chinchilla-optimal larger model
- Break-even queries: (C_over_train - C_chin_train) / (C_inf_large - C_inf_small)

## Code 2 — Cost Comparison at Deployment Scale

```python
import numpy as np
import matplotlib.pyplot as plt

E_CONST, A_CONST, B_CONST, ALPHA, BETA = 1.69, 406.4, 410.7, 0.34, 0.28

def tokens_for_target(N, L_target=2.5):
    '''Tokens needed to reach L_target with N parameters.'''
    res = L_target - E_CONST - A_CONST * N ** (-ALPHA)
    return (B_CONST / res) ** (1.0 / BETA) if res > 0 else np.inf

N_range   = np.logspace(8, 12, 150)  # 100M to 1T params
scenarios = [
    ('1K queries',  1e3,  '#3498db'),
    ('1M queries',  1e6,  '#e67e22'),
    ('1B queries',  1e9,  '#e74c3c'),
]

fig, ax = plt.subplots(figsize=(10, 6))
for label, Q, color in scenarios:
    costs = []
    for N in N_range:
        D = tokens_for_target(N)
        costs.append(6.0 * N * D + 2.0 * N * Q if np.isfinite(D) else np.inf)
    costs = np.array(costs)
    valid = np.isfinite(costs)
    ax.semilogy(N_range[valid] / 1e9, costs[valid], color=color, lw=2, label=label)
    best_i = int(np.argmin(np.where(valid, costs, np.inf)))
    ax.axvline(N_range[best_i] / 1e9, color=color, ls=':', alpha=0.7)

ax.set_xlabel('Model Size N (billions of parameters)', fontsize=12)
ax.set_ylabel('Total Cost (train + inference FLOPs)', fontsize=12)
ax.set_title('Inference-Aware Total Cost vs Model Size at Different Deployment Scales', fontsize=11)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('inference_cost_comparison.png', dpi=150)
plt.show()
print('Dotted vertical lines mark inference-optimal N* for each deployment scale.')
```

## Multi-Epoch Training Effects

When a model is trained beyond the Chinchilla-optimal token count, it will inevitably revisit tokens if the unique data corpus is smaller than D*. Multiple epochs over the same data exhibit diminishing returns: the effective data contribution from repeated tokens scales sub-linearly (roughly as epochs^0.5 empirically). At very high epoch counts — say, 100 passes over the same data — loss degradation can become significant, as the model begins to memorize rather than generalize. The practical mitigation is aggressive data curation, deduplication, and mixing in synthetic data (as with Phi-3 and related models) to maintain data diversity even at high token counts.

## Code 3 — Multi-Epoch Training Degradation

```python
import numpy as np
import matplotlib.pyplot as plt

def loss_with_repetition(N, D_unique, epochs,
                         E=1.69, A=406.4, alpha=0.34, B=410.7, beta=0.28):
    '''Model loss under data repetition: D_effective = D_unique * epochs^0.5
    (sub-linear effective data gain from repeated tokens).'''
    D_eff = D_unique * (epochs ** 0.5)
    return E + A * N ** (-alpha) + B * D_eff ** (-beta)

N        = 7e9    # 7B parameter model
D_unique = 100e9  # 100B unique high-quality tokens
epochs   = np.linspace(1.0, 25.0, 250)
losses   = [loss_with_repetition(N, D_unique, e) for e in epochs]

chinchilla_D     = 20.0 * N         # 140B = Chinchilla-optimal
chinchilla_epoch = chinchilla_D / D_unique   # 1.4 epochs

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(epochs, losses, 'b-', lw=2, label='Test loss with data repetition')
ax.axvline(chinchilla_epoch, color='g', ls='--', lw=2,
           label='Chinchilla-optimal ({:.1f} epochs)'.format(chinchilla_epoch))
ax.axhline(min(losses), color='gray', ls=':', lw=1.5, label='Best achievable loss')
ax.set_xlabel('Training Epochs Over Unique Data', fontsize=12)
ax.set_ylabel('Predicted Test Loss (nats)', fontsize=12)
ax.set_title('Multi-Epoch Training: Diminishing Returns Past Chinchilla-Optimal', fontsize=12)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('multi_epoch_degradation.png', dpi=150)
plt.show()
```

## Code 4 — LLaMA vs Chinchilla-Optimal Comparison

```python
import numpy as np

def chinchilla_optimal_tokens(N):
    '''Chinchilla-optimal token count for N parameters: D* = 20 * N.'''
    return 20.0 * N

# Published model specs: (name, N_params, D_tokens_actual)
published_models = [
    ('LLaMA-1 7B',    7e9,    1.0e12),
    ('LLaMA-3.1 8B',  8e9,   15.0e12),
    ('LLaMA-2 70B',  70e9,    2.0e12),
    ('LLaMA-3.1 70B',70e9,   15.0e12),
    ('Mistral 7B',    7e9,    2.0e12),
    ('Phi-3 Mini',    3.8e9,  3.3e12),
]

print('{:<18} {:>7} {:>13} {:>18} {:>12} {:>16}'.format(
    'Model', 'N (B)', 'D actual (B)', 'D Chinchilla (B)', 'Multiplier', 'C_train (FLOPs)'))
print('-' * 90)
for name, N, D in published_models:
    D_ch = chinchilla_optimal_tokens(N)
    mult = D / D_ch
    C    = 6.0 * N * D
    print('{:<18} {:>7.1f} {:>13.1f} {:>18.1f} {:>12.1f}x {:>16.2e}'.format(
        name, N/1e9, D/1e9, D_ch/1e9, mult, C))
print('\nModels trained well beyond Chinchilla-optimal are inference-optimized for deployment.')
```

The table below summarizes the inference-aware picture for notable models — showing how far each deviates from Chinchilla-optimal and what deployment context that choice serves.

| Model | Params (B) | Tokens (B) | D/N Ratio | Chinchilla Multiplier | Primary Use Case |
| --- | --- | --- | --- | --- | --- |
| LLaMA-3.1 8B | 8 | 15000 | 1875 | 93.75x | Edge / on-device inference |
| LLaMA-3.1 70B | 70 | 15000 | 214 | 10.7x | High-quality hosted inference |
| Mistral 7B | 7 | 2000 | 286 | 14.3x | Efficient local deployment |
| Phi-3 Mini | 3.8 | 3300 | 868 | 43.4x | Mobile / edge device inference |
| Gemma 2 9B | 9 | 8000 | 889 | 44.4x | Efficient fine-tuning base |

The Sardana / Chinchilla-inf framework (Sardana & Frankle, 2023) formalizes the inference-aware objective: minimize C_train + lambda * C_inf, where lambda represents the expected total query volume. Solving this modified optimization yields a new optimal N* that is strictly smaller than Chinchilla-optimal N* for any lambda > 0. As lambda grows (more queries expected), the optimal model shrinks and the optimal token count grows. This explains the observed trend: frontier labs are converging on smaller, longer-trained models for public deployment.

- Sardana objective: minimize 6*N*D + lambda*2*N*Q subject to L(N,D) <= L_target
- For lambda = 0 (no inference): recovers Chinchilla-optimal N* and D*
- For large lambda: optimal N* shrinks, optimal D* grows proportionally
- Break-even: extra training cost / per-query savings = number of queries to recoup
- LLaMA-3.1 8B vs 70B: 8B costs ~9x less per query, worth training longer for high-volume APIs
- Synthetic data (Phi-3 approach) enables high token counts without web data repetition

> **Tip**: If you expect to serve a model for millions of queries, training a 2-4x smaller model on 4-8x more tokens often gives better total cost (train + serve) than the Chinchilla-optimal model — smaller models are dramatically cheaper per inference query.

## The Shifting Frontier

The field has moved decisively beyond Chinchilla-optimal training. LLaMA-3.1 8B (15T tokens, 93x Chinchilla-optimal) demonstrates that small models trained extremely long can match much larger Chinchilla-optimal models in quality while running at a fraction of the inference cost. The implication for practitioners: when choosing a base model for fine-tuning or deployment, prefer models that have been over-trained relative to Chinchilla — they will be smaller (cheaper to serve), faster (lower latency), and often comparable in quality to larger Chinchilla-optimal counterparts on standard benchmarks. The compute-optimal question is no longer just about training — it is about the full lifecycle cost from pre-training through millions of inference calls.

