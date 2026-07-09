---
title: "Kronecker and Hadamard Products"
slug: "kronecker-hadamard-products"
description: "Hadamard elementwise product for gating, Kronecker product block structure, the vectorization identity, and K-FAC optimization."
tags: ["linear-algebra", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWF0cml4IGFsZ2VicmEgaGFzIHR3byBpbXBvcnRhbnQgcHJvZHVjdHMgYmV5b25kIG9yZGluYXJ5IG11bHRpcGxpY2F0aW9uOiB0aGUgKipIYWRhbWFyZCBwcm9kdWN0KiogKGVsZW1lbnR3aXNlKSBhbmQgdGhlICoqS3JvbmVja2VyIHByb2R1Y3QqKiAoYmxvY2stc3RydWN0dXJlZCkuIFRoZXNlIHByb2R1Y3RzIGFwcGVhciBpbiBnYXRpbmcgbWVjaGFuaXNtcywgc3RydWN0dXJlZCBjb252b2x1dGlvbnMsIHNlY29uZC1vcmRlciBvcHRpbWl6YXRpb24sIGFuZCB0aGUgdmVjdG9yaXphdGlvbiBvZiBtYXRyaXggZXF1YXRpb25zLiBVbmRlcnN0YW5kaW5nIHRoZW0gcmV2ZWFscyBlbGVnYW50IHN0cnVjdHVyZSBpbiBjb21wdXRhdGlvbnMgdGhhdCB3b3VsZCBvdGhlcndpc2Ugc2VlbSBhZCBob2MuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEhhZGFtYXJkIFByb2R1Y3Q6IEVsZW1lbnR3aXNlIE11bHRpcGxpY2F0aW9uIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgKipIYWRhbWFyZCBwcm9kdWN0KiogKGFsc28gY2FsbGVkIGVsZW1lbnR3aXNlIHByb2R1Y3QsIG9yIFNjaHVyIHByb2R1Y3QpIG9mIHR3byBtYXRyaWNlcyBvZiB0aGUgc2FtZSBzaGFwZSBpcyBkZWZpbmVkIGVudHJ5LWJ5LWVudHJ5OlxuXG4gICgqKkEqKiDiipkgKipCKiopW2ksal0gPSBBW2ksal0gwrcgQltpLGpdXG5cblRoaXMgaXMgdGhlIGRlZmF1bHQgYCpgIG9wZXJhdG9yIGluIE51bVB5IGFuZCBQeVRvcmNoICh3aGVuIHNoYXBlcyBhcmUgY29tcGF0aWJsZSkuIFVubGlrZSBtYXRyaXggbXVsdGlwbGljYXRpb24sIHRoZSBIYWRhbWFyZCBwcm9kdWN0IGlzIGNvbW11dGF0aXZlICgqKkEqKiDiipkgKipCKiogPSAqKkIqKiDiipkgKipBKiopLCBhc3NvY2lhdGl2ZSwgYW5kIGRpc3RyaWJ1dGVzIG92ZXIgYWRkaXRpb24uIEl0IGlzIHRoZSAnbmF0dXJhbCcgcG9pbnR3aXNlIG9wZXJhdGlvbiB3aGVuIG1hdHJpY2VzIHJlcHJlc2VudCBwaXhlbCBtYXBzLCBhdHRlbnRpb24gbWFza3MsIG9yIGZlYXR1cmUtd2lzZSB3ZWlnaHRzLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnAsIHRvcmNoXG5cbkEgPSBucC5hcnJheShbWzEsIDJdLCBbMywgNF1dKVxuQiA9IG5wLmFycmF5KFtbNSwgNl0sIFs3LCA4XV0pXG5cbiMgSGFkYW1hcmQgcHJvZHVjdCAoZWxlbWVudHdpc2UpXG5DID0gQSAqIEIgICAgICAgICAgICAgICMgbnVtcHk6IFtbNSwxMl0sWzIxLDMyXV1cbnByaW50KCdBICogQjpcXG4nLCBDKVxuXG4jIHZzIG1hdHJpeCBtdWx0aXBsaWNhdGlvblxucHJpbnQoJ0EgQCBCOlxcbicsIEEgQCBCKSAgICMgW1sxOSwyMl0sWzQzLDUwXV0gLS0gdmVyeSBkaWZmZXJlbnQhXG5cbiMgUHJvcGVydGllc1xucHJpbnQoJ0NvbW11dGF0aXZlPycsIG5wLmFsbGNsb3NlKEEqQiwgQipBKSkgICAgICAgICAgIyBUcnVlXG5wcmludCgnKEEqQikqQyA9PSBBKihCKkMpPycsIG5wLmFsbGNsb3NlKChBKkIpKkEsIEEqKEIqQSkpKSAgIyBUcnVlXG5cbiMgRnJvYmVuaXVzIGlubmVyIHByb2R1Y3QgdmlhIEhhZGFtYXJkXG5mcm9faXAgPSBucC5zdW0oQSAqIEIpICAgIyA9IHRyKEFeVCBCKVxucHJpbnQoJ0Zyb2Jlbml1cyBpbm5lciBwcm9kdWN0OicsIGZyb19pcCkgICAjID0gNSsxMisyMSszMiA9IDcwIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSGFkYW1hcmQgUHJvZHVjdCBpbiBOZXVyYWwgTmV0d29ya3M6IEdhdGluZyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2F0aW5nIG1lY2hhbmlzbXMgdXNlIHRoZSBIYWRhbWFyZCBwcm9kdWN0IHRvIHNlbGVjdGl2ZWx5IHBhc3Mgb3Igc3VwcHJlc3MgaW5mb3JtYXRpb246XG5cbi0gKipMU1RNIGdhdGVzKio6IFRoZSBmb3JnZXQgZ2F0ZSBjb21wdXRlcyBoJyA9IGYg4oqZIGMgKGVsZW1lbnR3aXNlIGdhdGUgb24gY2VsbCBzdGF0ZSksIHdoZXJlIGYg4oiIIFswLDFdIGFjdHMgYXMgYSBsZWFybmVkICdmb3JnZXQgZmFjdG9yJyBmb3IgZWFjaCBkaW1lbnNpb24gaW5kZXBlbmRlbnRseS5cbi0gKipHUlUgdXBkYXRlIGdhdGUqKjogaCA9ICgxLXopIOKKmSBoX3ByZXYgKyB6IOKKmSBoX2NhbmRpZGF0ZVxuLSAqKkF0dGVudGlvbiBtYXNraW5nKio6IE11bHRpcGx5IGF0dGVudGlvbiBsb2dpdHMgYnkgYSBiaW5hcnkgbWFzayAoMC8xKSBiZWZvcmUgc29mdG1heCB0byBwcmV2ZW50IGF0dGVuZGluZyB0byBwYWRkaW5nIHRva2Vuc1xuLSAqKkZlYXR1cmUtd2lzZSBMaW5lYXIgTW9kdWxhdGlvbiAoRmlMTSkqKjogeSA9IM6zKGMpIOKKmSB4ICsgzrIoYykgZm9yIGNvbmRpdGlvbmFsIGdlbmVyYXRpb24sIHdoZXJlIM6zIGFuZCDOsiBhcmUgY29tcHV0ZWQgZnJvbSBjb25kaXRpb25pbmcgdmFyaWFibGUgY1xuLSAqKk1peHR1cmUgb2YgRXhwZXJ0cyBnYXRpbmcqKjogbyA9IM6j4bWiIGfhtaIg4oqZIEXhtaIoeCkgd2hlcmUgZyBpcyBhIHNvZnQgcm91dGVyIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbiMgU2ltcGxpZmllZCBMU1RNIGNlbGwgc2hvd2luZyBIYWRhbWFyZCBnYXRpbmdcbmRlZiBsc3RtX2NlbGwoeCwgaF9wcmV2LCBjX3ByZXYsIFdfeCwgV19oLCBiKTpcbiAgICBcIlwiXCJ4OiAoYmF0Y2gsIGlucHV0X3NpemUpLCBoX3ByZXYsIGNfcHJldjogKGJhdGNoLCBoaWRkZW5fc2l6ZSlcIlwiXCJcbiAgICBnYXRlcyA9IHggQCBXX3guVCArIGhfcHJldiBAIFdfaC5UICsgYiAgIyAoYmF0Y2gsIDQqaGlkZGVuKVxuICAgIGhpZGRlbiA9IGdhdGVzLnNoYXBlWy0xXSAvLyA0XG4gICAgaSwgZiwgZywgbyA9IGdhdGVzLnNwbGl0KGhpZGRlbiwgZGltPS0xKSAgIyBpbnB1dCwgZm9yZ2V0LCBjZWxsLCBvdXRwdXRcbiAgICBpID0gdG9yY2guc2lnbW9pZChpKVxuICAgIGYgPSB0b3JjaC5zaWdtb2lkKGYpXG4gICAgZyA9IHRvcmNoLnRhbmgoZylcbiAgICBvID0gdG9yY2guc2lnbW9pZChvKVxuICAgICMgSGFkYW1hcmQgcHJvZHVjdDogZWxlbWVudHdpc2UgZ2F0aW5nIG9mIGNlbGwgc3RhdGVcbiAgICBjX25ldyA9IGYgKiBjX3ByZXYgKyBpICogZyAgICMgZm9yZ2V0IG9sZCArIGlucHV0IG5ld1xuICAgIGhfbmV3ID0gbyAqIHRvcmNoLnRhbmgoY19uZXcpXG4gICAgcmV0dXJuIGhfbmV3LCBjX25ld1xuXG4jIEZpTE0gY29uZGl0aW9uaW5nXG5jbGFzcyBGaUxNKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNvbmRfZGltLCBmZWF0X2RpbSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmdhbW1hID0gbm4uTGluZWFyKGNvbmRfZGltLCBmZWF0X2RpbSlcbiAgICAgICAgc2VsZi5iZXRhICA9IG5uLkxpbmVhcihjb25kX2RpbSwgZmVhdF9kaW0pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBjb25kKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuZ2FtbWEoY29uZCkgKiB4ICsgc2VsZi5iZXRhKGNvbmQpICAjIEhhZGFtYXJkIHNjYWxlK3NoaWZ0In0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEtyb25lY2tlciBQcm9kdWN0OiBCbG9jayBNYXRyaXggU3RydWN0dXJlIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgKipLcm9uZWNrZXIgcHJvZHVjdCoqICoqQSoqIOKKlyAqKkIqKiBvZiBhbiBtw5duIG1hdHJpeCAqKkEqKiBhbmQgYSBww5dxIG1hdHJpeCAqKkIqKiBpcyB0aGUgbXDDl25xIGJsb2NrIG1hdHJpeDpcblxuICAqKkEqKiDiipcgKipCKiogPSBbW2HigoHigoFCLCBh4oKB4oKCQiwgLi4uLCBh4oKB4oKZQl0sIFth4oKC4oKBQiwgLi4uLCBh4oKC4oKZQl0sIC4uLiwgW2HigpjigoFCLCAuLi4sIGHigpjigplCXV1cblxuRWFjaCBlbnRyeSBvZiAqKkEqKiBpcyByZXBsYWNlZCBieSBhIHNjYWxlZCBjb3B5IG9mICoqQioqLiBLZXkgcHJvcGVydGllczpcbi0gKCoqQSoqIOKKlyAqKkIqKinhtYAgPSAqKkHhtYAqKiDiipcgKipC4bWAKipcbi0gKCoqQSoqIOKKlyAqKkIqKinigbvCuSA9ICoqQeKBu8K5Kiog4oqXICoqQuKBu8K5KiogKGlmIGludmVydGlibGUpXG4tICgqKkEqKiDiipcgKipCKiopKCoqQyoqIOKKlyAqKkQqKikgPSAoKipBQyoqKSDiipcgKCoqQkQqKikgKG1peGVkIHByb2R1Y3QgcHJvcGVydHkpXG4tIEVpZ2VudmFsdWVzIG9mICoqQSoqIOKKlyAqKkIqKiBhcmUgcHJvZHVjdHMgb2YgZWlnZW52YWx1ZXM6IHvOu+G1oihBKSDCtyDOvOKxvChCKX0ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbkEgPSBucC5hcnJheShbWzEsIDJdLCBbMywgNF1dKVxuQiA9IG5wLmFycmF5KFtbMCwgNV0sIFs2LCA3XV0pXG5cbiMgS3JvbmVja2VyIHByb2R1Y3RcbksgPSBucC5rcm9uKEEsIEIpICAgIyAoNCwgNCkgc2luY2UgYm90aCBhcmUgMngyXG5wcmludCgnQSDiipcgQjpcXG4nLCBLKVxuIyBbWzAsNSwwLDEwXSxbNiw3LDEyLDE0XSxbMCwxNSwwLDIwXSxbMTgsMjEsMjQsMjhdXVxuXG4jIEVpZ2VudmFsdWUgcHJvZHVjdCBwcm9wZXJ0eVxuQV9zeW0gPSBBICsgQS5UICAgIyBtYWtlIHN5bW1ldHJpYyBmb3IgcmVhbCBlaWdlbnZhbHVlc1xuQl9zeW0gPSBCICsgQi5UXG5laWdfQSA9IG5wLnNvcnQobnAubGluYWxnLmVpZ3ZhbHNoKEFfc3ltKSlcbmVpZ19CID0gbnAuc29ydChucC5saW5hbGcuZWlndmFsc2goQl9zeW0pKVxuS19zeW0gPSBucC5rcm9uKEFfc3ltLCBCX3N5bSlcbmVpZ19LID0gbnAuc29ydChucC5saW5hbGcuZWlndmFsc2goS19zeW0pKVxuIyBQcm9kdWN0cyBvZiBlaWdlbnZhbHVlc1xucHJvZHVjdHMgPSBucC5zb3J0KFthKmIgZm9yIGEgaW4gZWlnX0EgZm9yIGIgaW4gZWlnX0JdKVxucHJpbnQoJ0VpZ3Mgb2YgSyBtYXRjaCBwcm9kdWN0cz8nLCBucC5hbGxjbG9zZShlaWdfSywgcHJvZHVjdHMpKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBWZWN0b3JpemF0aW9uIFRyaWNrOiB2ZWMoQVhCKSA9IChC4bWAIOKKlyBBKSB2ZWMoWCkifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtb3N0IHVzZWZ1bCBpZGVudGl0eSBpbnZvbHZpbmcgS3JvbmVja2VyIHByb2R1Y3RzIGlzIHRoZSAqKnZlY3Rvcml6YXRpb24gaWRlbnRpdHkqKi4gVGhlICoqdmVjKiogb3BlcmF0b3Igc3RhY2tzIHRoZSBjb2x1bW5zIG9mIGEgbWF0cml4IGludG8gYSBzaW5nbGUgbG9uZyB2ZWN0b3I6IHZlYygqKlgqKikg4oiIIOKEneG1kOKBvyBmb3IgKipYKiog4oiIIOKEneG1kMuj4oG/LlxuXG5UaGUgaWRlbnRpdHkgc3RhdGVzOlxuXG4gIHZlYygqKkFYQioqKSA9ICgqKkLhtYAqKiDiipcgKipBKiopIHZlYygqKlgqKilcblxuVGhpcyBjb252ZXJ0cyBhIG1hdHJpeCBlcXVhdGlvbiBpbnRvIGEgdmVjdG9yLW1hdHJpeCBlcXVhdGlvbiwgZW5hYmxpbmcgdGhlIHVzZSBvZiBzdGFuZGFyZCBsaW5lYXIgYWxnZWJyYSB0b29scyAobGVhc3Qgc3F1YXJlcywgZWlnZW5zb2x2ZXJzKSB0byBzb2x2ZSBwcm9ibGVtcyBpbnZvbHZpbmcgbWF0cml4IHVua25vd25zLiBJdCBpcyB0aGUga2V5IHN0ZXAgaW4gZGVyaXZpbmcgc29sdXRpb25zIHRvIHRoZSBTeWx2ZXN0ZXIgZXF1YXRpb24gKCoqQVggKyBYQiA9IEMqKikgYW5kIGluIGFuYWx5emluZyBLcm9uZWNrZXItZmFjdG9yZWQgYXBwcm94aW1hdGlvbnMgdG8gdGhlIEZpc2hlciBpbmZvcm1hdGlvbiBtYXRyaXguIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5tLCBuLCBwID0gMywgNCwgMlxuQSA9IG5wLnJhbmRvbS5yYW5kbihtLCBtKVxuWCA9IG5wLnJhbmRvbS5yYW5kbihtLCBuKVxuQiA9IG5wLnJhbmRvbS5yYW5kbihuLCBwKVxuXG4jIExlZnQgc2lkZTogdmVjKEFYQilcbkFYQiA9IEEgQCBYIEAgQiAgICAgICAgICAjIChtLCBwKVxudmVjX0FYQiA9IEFYQi5mbGF0dGVuKG9yZGVyPSdGJykgICMgY29sdW1uLW1ham9yIHZlYzogc3RhY2sgY29sdW1uc1xuXG4jIFJpZ2h0IHNpZGU6IChCXlQg4oqXIEEpIHZlYyhYKVxuS3JvbmVja2VyID0gbnAua3JvbihCLlQsIEEpICAgICAgICAjIChtKnAsIG0qbilcbnZlY19YID0gWC5mbGF0dGVuKG9yZGVyPSdGJykgICAgICAgIyAobSpuLClcbnJocyA9IEtyb25lY2tlciBAIHZlY19YICAgICAgICAgICAgIyAobSpwLClcblxucHJpbnQoJ3ZlYyhBWEIpID09IChCXlQg4oqXIEEpIHZlYyhYKT8nLCBucC5hbGxjbG9zZSh2ZWNfQVhCLCByaHMpKSAgIyBUcnVlIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSy1GQUM6IEtyb25lY2tlci1GYWN0b3JlZCBBcHByb3hpbWF0ZSBDdXJ2YXR1cmUifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IioqSy1GQUMqKiAoTWFydGVucyAmIEdyb3NzZSwgMjAxNSkgYXBwcm94aW1hdGVzIHRoZSBGaXNoZXIgaW5mb3JtYXRpb24gbWF0cml4IChGSU0pIOKAlCB0aGUgZXhhY3QgbmF0dXJhbCBncmFkaWVudCBwcmVjb25kaXRpb25lciDigJQgdXNpbmcgS3JvbmVja2VyIHByb2R1Y3RzLiBGb3IgYSBsaW5lYXIgbGF5ZXIgeSA9IFd4LCB0aGUgRklNIGlzOlxuXG4gIEZfVyA9IEVbYSBh4bWAIOKKlyBnIGfhtYBdXG5cbndoZXJlICoqYSoqIGlzIHRoZSBsYXllcidzIGlucHV0IGFuZCAqKmcqKiBpcyB0aGUgZ3JhZGllbnQgb2YgdGhlIGxvc3Mgdy5yLnQuIHRoZSBwcmUtYWN0aXZhdGlvbiBvdXRwdXQuIEstRkFDIGFwcHJveGltYXRlcyB0aGlzIGFzOlxuXG4gIEbMgl9XID0gw4Ig4oqXIMScLCAgd2hlcmUgw4IgPSBFW2Fh4bWAXSwgxJwgPSBFW2dn4bWAXVxuXG5UaGlzIEtyb25lY2tlciBmYWN0b3JpemF0aW9uIG1ha2VzIHRoZSBwcmVjb25kaXRpb25lciBlZmZpY2llbnQ6IGludmVydGluZyBGzIJfVyBjb3N0cyBPKGTCsyArIGTCsykgaW5zdGVhZCBvZiBPKGTigbYpIGZvciB0aGUgZnVsbCBtYXRyaXguIFRoZSB1cGRhdGUgcnVsZSB2ZWMozpRXKSA9IC3OtyBGzIJfV+KBu8K5IHZlYyhnX1cpIGJlY29tZXMgzpRXID0gLc63IMOC4oG7wrkgR19XIMSc4oG7wrkgKHNpbXBsZSBtYXRyaXggb3BlcmF0aW9ucykuIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5jbGFzcyBLRkFDTGF5ZXI6XG4gICAgXCJcIlwiU2ltcGxpZmllZCBLLUZBQyBzdGF0ZSBmb3Igb25lIGxpbmVhciBsYXllci5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fZGltLCBvdXRfZGltLCBkZWNheT0wLjk1KTpcbiAgICAgICAgc2VsZi5BX2JhciA9IHRvcmNoLnplcm9zKGluX2RpbSwgaW5fZGltKSAgICMgaW5wdXQgY292YXJpYW5jZVxuICAgICAgICBzZWxmLkdfYmFyID0gdG9yY2guemVyb3Mob3V0X2RpbSwgb3V0X2RpbSkgICMgZ3JhZGllbnQgY292YXJpYW5jZVxuICAgICAgICBzZWxmLmRlY2F5ID0gZGVjYXlcblxuICAgIGRlZiB1cGRhdGVfc3RhdHMoc2VsZiwgYSwgZyk6XG4gICAgICAgIFwiXCJcImE6IGlucHV0IHRvIGxheWVyIChiYXRjaCwgaW5fZGltKSwgZzogZ3JhZCBvZiBwcmUtYWN0IChiYXRjaCwgb3V0X2RpbSlcIlwiXCJcbiAgICAgICAgQSA9IGEuVCBAIGEgLyBhLnNoYXBlWzBdICAgIyAoaW5fZGltLCBpbl9kaW0pXG4gICAgICAgIEcgPSBnLlQgQCBnIC8gZy5zaGFwZVswXSAgICMgKG91dF9kaW0sIG91dF9kaW0pXG4gICAgICAgIHNlbGYuQV9iYXIgPSBzZWxmLmRlY2F5ICogc2VsZi5BX2JhciArICgxLXNlbGYuZGVjYXkpICogQVxuICAgICAgICBzZWxmLkdfYmFyID0gc2VsZi5kZWNheSAqIHNlbGYuR19iYXIgKyAoMS1zZWxmLmRlY2F5KSAqIEdcblxuICAgIGRlZiBwcmVjb25kaXRpb25lZF9ncmFkKHNlbGYsIGRXLCBkYW1waW5nPTFlLTMpOlxuICAgICAgICBcIlwiXCJBcHBseSBLLUZBQyBpbnZlcnNlIHRvIHdlaWdodCBncmFkaWVudC5cIlwiXCJcbiAgICAgICAgIyBJbnZlcnQgQSBhbmQgRyBzZXBhcmF0ZWx5IChtdWNoIGNoZWFwZXIgdGhhbiBmdWxsIEZJTSBpbnZlcnNlKVxuICAgICAgICBBX2ludiA9IHRvcmNoLmxpbmFsZy5pbnYoc2VsZi5BX2JhciArIGRhbXBpbmcgKiB0b3JjaC5leWUoc2VsZi5BX2Jhci5zaGFwZVswXSkpXG4gICAgICAgIEdfaW52ID0gdG9yY2gubGluYWxnLmludihzZWxmLkdfYmFyICsgZGFtcGluZyAqIHRvcmNoLmV5ZShzZWxmLkdfYmFyLnNoYXBlWzBdKSlcbiAgICAgICAgcmV0dXJuIEdfaW52IEAgZFcgQCBBX2ludiAgIyDOlFcgPSBH4oG7wrkg4oiHVyBB4oG7wrkifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdHJ1Y3R1cmVkIE1hdHJpY2VzIGFuZCBFZmZpY2llbnQgQ29tcHV0YXRpb24ifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Iktyb25lY2tlciBwcm9kdWN0cyBlbmFibGUgcmVwcmVzZW50aW5nIGxhcmdlIHN0cnVjdHVyZWQgbWF0cmljZXMgZWZmaWNpZW50bHkuIEEgS3JvbmVja2VyIHByb2R1Y3QgKipBKiog4oqXICoqQioqIChzaXplIG1ww5ducSkgcmVxdWlyZXMgb25seSBtbiArIHBxIHBhcmFtZXRlcnMgaW5zdGVhZCBvZiBtbnBxLiBBcHBseWluZyBpdCB0byBhIHZlY3RvciBjb3N0cyBPKG3Ct27Ct3EgKyBwwrdxwrduKSBpbnN0ZWFkIG9mIE8obW5wcSkuXG5cbkFwcGxpY2F0aW9uczpcbi0gKipTZXBhcmFibGUgZmlsdGVycyoqIGluIGltYWdlIHByb2Nlc3Npbmc6IDJEIEdhdXNzaWFuIGJsdXIgPSAxRCBob3Jpem9udGFsIOKKlyAxRCB2ZXJ0aWNhbCBHYXVzc2lhblxuLSAqKlN0cnVjdHVyZWQgd2VpZ2h0IG1hdHJpY2VzKio6IFNvbWUgYXJjaGl0ZWN0dXJlIHdvcmsgcmVwbGFjZXMgZGVuc2UgbGF5ZXJzIHdpdGggS3JvbmVja2VyLXN0cnVjdHVyZWQgbGF5ZXJzIGZvciBjb21wcmVzc2lvblxuLSAqKk11bHRpdGFzayBsZWFybmluZyoqOiBLcm9uZWNrZXIgcHJpb3JzIG92ZXIgdGFzayDDlyBmZWF0dXJlIGNvdmFyaWFuY2UgbWF0cmljZXNcbi0gKipOZXVyYWwgT0RFIGFuZCBIYW1pbHRvbmlhbiBzeXN0ZW1zKio6IEtyb25lY2tlciBzdHJ1Y3R1cmUgYXJpc2VzIGluIHBoeXNpY3MtaW5mb3JtZWQgbW9kZWxzIn0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkhhZGFtYXJkIHZzIEtyb25lY2tlciBhdCBhIEdsYW5jZSIsImNvbnRlbnQiOiJIYWRhbWFyZCAo4oqZKTogc2FtZS1zaGFwZSBlbGVtZW50d2lzZSBtdWx0aXBseS4gUmVzdWx0IHNoYXBlID0gaW5wdXQgc2hhcGUuIFVzZWQgZm9yIGdhdGluZyBhbmQgbWFza2luZy5cblxuS3JvbmVja2VyICjiipcpOiBibG9jay1vdXRlci1wcm9kdWN0LiBJZiBBIGlzIG3Dl24gYW5kIEIgaXMgcMOXcSwgcmVzdWx0IGlzIG1ww5ducS4gVXNlZCBmb3Igc3RydWN0dXJlZCBsaW5lYXIgbWFwcyBhbmQgRmlzaGVyIG1hdHJpeCBhcHByb3hpbWF0aW9ucy5cblxuS3JvbmVja2VyIGNhbiBiZSBjb21wdXRlZCBhczogbnAua3JvbihBLCBCKS4gSGFkYW1hcmQgaXMganVzdDogQSAqIEIgKG9yIHRvcmNoLm11bCkuIn0sCiAgeyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb2R1Y3QiLCJTeW1ib2wiLCJTaGFwZSBSdWxlIiwiS2V5IFByb3BlcnR5IiwiTUwgQXBwbGljYXRpb24iXSwicm93cyI6W1siSGFkYW1hcmQiLCJBIOKKmSBCIiwiU2FtZSBhcyBpbnB1dHMiLCJFbGVtZW50d2lzZSwgY29tbXV0YXRpdmUiLCJHYXRpbmcgKExTVE0vR1JVKSwgbWFza2luZyJdLFsiS3JvbmVja2VyIiwiQSDiipcgQiIsIihtcCnDlyhucSkgZnJvbSBtw5duIGFuZCBww5dxIiwiQmxvY2sgc3RydWN0dXJlLCAoQl5U4oqXQSl2ZWMoWCk9dmVjKEFYQikiLCJLLUZBQywgc2VwYXJhYmxlIGZpbHRlcnMiXSxbIlN0YW5kYXJkIiwiQSBAIEIiLCIobSxuKUAobixrKT0obSxrKSIsIk5vbi1jb21tdXRhdGl2ZSIsIkxpbmVhciBsYXllcnMsIGF0dGVudGlvbiJdLFsiT3V0ZXIiLCJ1IOKKlyB2IiwiKG0sbikgZnJvbSAobSwpIGFuZCAobiwpIiwiUmFuay0xIHVwZGF0ZSIsIkdyYWRpZW50IG9mIGxpbmVhciBsYXllcnMiXV19Cl0K"
---

# Kronecker and Hadamard Products

Matrix algebra has two important products beyond ordinary multiplication: the **Hadamard product** (elementwise) and the **Kronecker product** (block-structured). These products appear in gating mechanisms, structured convolutions, second-order optimization, and the vectorization of matrix equations. Understanding them reveals elegant structure in computations that would otherwise seem ad hoc.

## The Hadamard Product: Elementwise Multiplication

The **Hadamard product** (also called elementwise product, or Schur product) of two matrices of the same shape is defined entry-by-entry:

  (**A** ⊙ **B**)[i,j] = A[i,j] · B[i,j]

This is the default `*` operator in NumPy and PyTorch (when shapes are compatible). Unlike matrix multiplication, the Hadamard product is commutative (**A** ⊙ **B** = **B** ⊙ **A**), associative, and distributes over addition. It is the 'natural' pointwise operation when matrices represent pixel maps, attention masks, or feature-wise weights.

```python
import numpy as np, torch

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Hadamard product (elementwise)
C = A * B              # numpy: [[5,12],[21,32]]
print('A * B:\n', C)

# vs matrix multiplication
print('A @ B:\n', A @ B)   # [[19,22],[43,50]] -- very different!

# Properties
print('Commutative?', np.allclose(A*B, B*A))          # True
print('(A*B)*C == A*(B*C)?', np.allclose((A*B)*A, A*(B*A)))  # True

# Frobenius inner product via Hadamard
fro_ip = np.sum(A * B)   # = tr(A^T B)
print('Frobenius inner product:', fro_ip)   # = 5+12+21+32 = 70
```

## Hadamard Product in Neural Networks: Gating

Gating mechanisms use the Hadamard product to selectively pass or suppress information:

- **LSTM gates**: The forget gate computes h' = f ⊙ c (elementwise gate on cell state), where f ∈ [0,1] acts as a learned 'forget factor' for each dimension independently.
- **GRU update gate**: h = (1-z) ⊙ h_prev + z ⊙ h_candidate
- **Attention masking**: Multiply attention logits by a binary mask (0/1) before softmax to prevent attending to padding tokens
- **Feature-wise Linear Modulation (FiLM)**: y = γ(c) ⊙ x + β(c) for conditional generation, where γ and β are computed from conditioning variable c
- **Mixture of Experts gating**: o = Σᵢ gᵢ ⊙ Eᵢ(x) where g is a soft router

```python
import torch
import torch.nn as nn

# Simplified LSTM cell showing Hadamard gating
def lstm_cell(x, h_prev, c_prev, W_x, W_h, b):
    """x: (batch, input_size), h_prev, c_prev: (batch, hidden_size)"""
    gates = x @ W_x.T + h_prev @ W_h.T + b  # (batch, 4*hidden)
    hidden = gates.shape[-1] // 4
    i, f, g, o = gates.split(hidden, dim=-1)  # input, forget, cell, output
    i = torch.sigmoid(i)
    f = torch.sigmoid(f)
    g = torch.tanh(g)
    o = torch.sigmoid(o)
    # Hadamard product: elementwise gating of cell state
    c_new = f * c_prev + i * g   # forget old + input new
    h_new = o * torch.tanh(c_new)
    return h_new, c_new

# FiLM conditioning
class FiLM(nn.Module):
    def __init__(self, cond_dim, feat_dim):
        super().__init__()
        self.gamma = nn.Linear(cond_dim, feat_dim)
        self.beta  = nn.Linear(cond_dim, feat_dim)

    def forward(self, x, cond):
        return self.gamma(cond) * x + self.beta(cond)  # Hadamard scale+shift
```

## The Kronecker Product: Block Matrix Structure

The **Kronecker product** **A** ⊗ **B** of an m×n matrix **A** and a p×q matrix **B** is the mp×nq block matrix:

  **A** ⊗ **B** = [[a₁₁B, a₁₂B, ..., a₁ₙB], [a₂₁B, ..., a₂ₙB], ..., [aₘ₁B, ..., aₘₙB]]

Each entry of **A** is replaced by a scaled copy of **B**. Key properties:
- (**A** ⊗ **B**)ᵀ = **Aᵀ** ⊗ **Bᵀ**
- (**A** ⊗ **B**)⁻¹ = **A⁻¹** ⊗ **B⁻¹** (if invertible)
- (**A** ⊗ **B**)(**C** ⊗ **D**) = (**AC**) ⊗ (**BD**) (mixed product property)
- Eigenvalues of **A** ⊗ **B** are products of eigenvalues: {λᵢ(A) · μⱼ(B)}

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 5], [6, 7]])

# Kronecker product
K = np.kron(A, B)   # (4, 4) since both are 2x2
print('A ⊗ B:\n', K)
# [[0,5,0,10],[6,7,12,14],[0,15,0,20],[18,21,24,28]]

# Eigenvalue product property
A_sym = A + A.T   # make symmetric for real eigenvalues
B_sym = B + B.T
eig_A = np.sort(np.linalg.eigvalsh(A_sym))
eig_B = np.sort(np.linalg.eigvalsh(B_sym))
K_sym = np.kron(A_sym, B_sym)
eig_K = np.sort(np.linalg.eigvalsh(K_sym))
# Products of eigenvalues
products = np.sort([a*b for a in eig_A for b in eig_B])
print('Eigs of K match products?', np.allclose(eig_K, products))
```

## The Vectorization Trick: vec(AXB) = (Bᵀ ⊗ A) vec(X)

The most useful identity involving Kronecker products is the **vectorization identity**. The **vec** operator stacks the columns of a matrix into a single long vector: vec(**X**) ∈ ℝᵐⁿ for **X** ∈ ℝᵐˣⁿ.

The identity states:

  vec(**AXB**) = (**Bᵀ** ⊗ **A**) vec(**X**)

This converts a matrix equation into a vector-matrix equation, enabling the use of standard linear algebra tools (least squares, eigensolvers) to solve problems involving matrix unknowns. It is the key step in deriving solutions to the Sylvester equation (**AX + XB = C**) and in analyzing Kronecker-factored approximations to the Fisher information matrix.

```python
import numpy as np

m, n, p = 3, 4, 2
A = np.random.randn(m, m)
X = np.random.randn(m, n)
B = np.random.randn(n, p)

# Left side: vec(AXB)
AXB = A @ X @ B          # (m, p)
vec_AXB = AXB.flatten(order='F')  # column-major vec: stack columns

# Right side: (B^T ⊗ A) vec(X)
Kronecker = np.kron(B.T, A)        # (m*p, m*n)
vec_X = X.flatten(order='F')       # (m*n,)
rhs = Kronecker @ vec_X            # (m*p,)

print('vec(AXB) == (B^T ⊗ A) vec(X)?', np.allclose(vec_AXB, rhs))  # True
```

## K-FAC: Kronecker-Factored Approximate Curvature

**K-FAC** (Martens & Grosse, 2015) approximates the Fisher information matrix (FIM) — the exact natural gradient preconditioner — using Kronecker products. For a linear layer y = Wx, the FIM is:

  F_W = E[a aᵀ ⊗ g gᵀ]

where **a** is the layer's input and **g** is the gradient of the loss w.r.t. the pre-activation output. K-FAC approximates this as:

  F̂_W = Â ⊗ Ĝ,  where Â = E[aaᵀ], Ĝ = E[ggᵀ]

This Kronecker factorization makes the preconditioner efficient: inverting F̂_W costs O(d³ + d³) instead of O(d⁶) for the full matrix. The update rule vec(ΔW) = -η F̂_W⁻¹ vec(g_W) becomes ΔW = -η Â⁻¹ G_W Ĝ⁻¹ (simple matrix operations).

```python
import torch

class KFACLayer:
    """Simplified K-FAC state for one linear layer."""
    def __init__(self, in_dim, out_dim, decay=0.95):
        self.A_bar = torch.zeros(in_dim, in_dim)   # input covariance
        self.G_bar = torch.zeros(out_dim, out_dim)  # gradient covariance
        self.decay = decay

    def update_stats(self, a, g):
        """a: input to layer (batch, in_dim), g: grad of pre-act (batch, out_dim)"""
        A = a.T @ a / a.shape[0]   # (in_dim, in_dim)
        G = g.T @ g / g.shape[0]   # (out_dim, out_dim)
        self.A_bar = self.decay * self.A_bar + (1-self.decay) * A
        self.G_bar = self.decay * self.G_bar + (1-self.decay) * G

    def preconditioned_grad(self, dW, damping=1e-3):
        """Apply K-FAC inverse to weight gradient."""
        # Invert A and G separately (much cheaper than full FIM inverse)
        A_inv = torch.linalg.inv(self.A_bar + damping * torch.eye(self.A_bar.shape[0]))
        G_inv = torch.linalg.inv(self.G_bar + damping * torch.eye(self.G_bar.shape[0]))
        return G_inv @ dW @ A_inv  # ΔW = G⁻¹ ∇W A⁻¹
```

## Structured Matrices and Efficient Computation

Kronecker products enable representing large structured matrices efficiently. A Kronecker product **A** ⊗ **B** (size mp×nq) requires only mn + pq parameters instead of mnpq. Applying it to a vector costs O(m·n·q + p·q·n) instead of O(mnpq).

Applications:
- **Separable filters** in image processing: 2D Gaussian blur = 1D horizontal ⊗ 1D vertical Gaussian
- **Structured weight matrices**: Some architecture work replaces dense layers with Kronecker-structured layers for compression
- **Multitask learning**: Kronecker priors over task × feature covariance matrices
- **Neural ODE and Hamiltonian systems**: Kronecker structure arises in physics-informed models

> **[TIP] Hadamard vs Kronecker at a Glance**
>
> Hadamard (⊙): same-shape elementwise multiply. Result shape = input shape. Used for gating and masking.

Kronecker (⊗): block-outer-product. If A is m×n and B is p×q, result is mp×nq. Used for structured linear maps and Fisher matrix approximations.

Kronecker can be computed as: np.kron(A, B). Hadamard is just: A * B (or torch.mul).

| Product | Symbol | Shape Rule | Key Property | ML Application |
| --- | --- | --- | --- | --- |
| Hadamard | A ⊙ B | Same as inputs | Elementwise, commutative | Gating (LSTM/GRU), masking |
| Kronecker | A ⊗ B | (mp)×(nq) from m×n and p×q | Block structure, (B^T⊗A)vec(X)=vec(AXB) | K-FAC, separable filters |
| Standard | A @ B | (m,n)@(n,k)=(m,k) | Non-commutative | Linear layers, attention |
| Outer | u ⊗ v | (m,n) from (m,) and (n,) | Rank-1 update | Gradient of linear layers |
