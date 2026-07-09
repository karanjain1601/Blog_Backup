---
title: "Tensor Operations in ML"
slug: "tensor-operations"
description: "Higher-order tensors, einsum notation, tensor contractions, CP and Tucker decompositions, convolutions, and tensor parallelism."
tags: ["linear-algebra", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGVuc29ycyBnZW5lcmFsaXplIG1hdHJpY2VzIHRvIGhpZ2hlciBkaW1lbnNpb25zIOKAlCBhIDREIHRlbnNvciBob2xkcyBhbiBpbWFnZSBiYXRjaCwgYSA1RCB0ZW5zb3IgaG9sZHMgYSB2aWRlbyBiYXRjaC4gVGVuc29yIG9wZXJhdGlvbnMgYXJlIHRoZSBjb21wdXRhdGlvbmFsIHN1YnN0cmF0ZSBvZiBkZWVwIGxlYXJuaW5nOiBjb252b2x1dGlvbnMsIGF0dGVudGlvbiwgYmF0Y2hlZCBtYXRyaXggbXVsdGlwbGllcywgYW5kIGVtYmVkZGluZyBsb29rdXBzIGFyZSBhbGwgdGVuc29yIG9wZXJhdGlvbnMuIE1hc3RlcmluZyBlaW5zdW0gbm90YXRpb24gYW5kIHVuZGVyc3RhbmRpbmcgdGVuc29yIGRlY29tcG9zaXRpb25zIGVuYWJsZXMgYm90aCBlZmZpY2llbnQgaW1wbGVtZW50YXRpb24gYW5kIG1vZGVsIGNvbXByZXNzaW9uLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhpZ2hlci1PcmRlciBUZW5zb3JzIGluIERlZXAgTGVhcm5pbmcifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcmFuay1OIHRlbnNvciBoYXMgTiBheGVzIChkaW1lbnNpb25zKS4gVGhlIG1vc3QgY29tbW9uIHRlbnNvciBzaGFwZXMgaW4gZGVlcCBsZWFybmluZzpcblxuLSAqKlJhbmstMSoqOiBgKGQsKWAg4oCUIHZlY3RvciwgZW1iZWRkaW5nXG4tICoqUmFuay0yKio6IGAoQiwgZClgIOKAlCBiYXRjaCBvZiBlbWJlZGRpbmdzXG4tICoqUmFuay0zKio6IGAoQiwgVCwgZClgIOKAlCBiYXRjaCBvZiBzZXF1ZW5jZXMgKHRleHQsIHRpbWUgc2VyaWVzKVxuLSAqKlJhbmstNCoqOiBgKEIsIEMsIEgsIFcpYCBvciBgKEIsIEgsIFcsIEMpYCDigJQgYmF0Y2ggb2YgaW1hZ2VzXG4tICoqUmFuay01Kio6IGAoQiwgVCwgQywgSCwgVylgIOKAlCBiYXRjaCBvZiB2aWRlbyBmcmFtZXNcblxuVGhlICoqYmF0Y2ggZGltZW5zaW9uIEIqKiBpcyBhbG1vc3QgYWx3YXlzIHRoZSBmaXJzdCBheGlzIGluIFB5VG9yY2ggY29udmVudGlvbi4gT3BlcmF0aW9ucyBhcmUgdmVjdG9yaXplZCBvdmVyIHRoZSBiYXRjaCwgZW5hYmxpbmcgR1BVcyB0byBwcm9jZXNzIGh1bmRyZWRzIG9mIGV4YW1wbGVzIHNpbXVsdGFuZW91c2x5LiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuIyBDb21tb24gdGVuc29yIHNoYXBlcyBpbiBNTFxudG9rZW5zICAgID0gdG9yY2gucmFuZG4oMzIsIDEyOCwgNTEyKSAgICMgKGJhdGNoLCBzZXFfbGVuLCBkX21vZGVsKVxuaW1hZ2UgICAgID0gdG9yY2gucmFuZG4oMzIsIDMsIDIyNCwgMjI0KSAjIChiYXRjaCwgY2hhbm5lbHMsIEgsIFcpXG5hdHRlbnRpb24gPSB0b3JjaC5yYW5kbigzMiwgOCwgMTI4LCAxMjgpICMgKGJhdGNoLCBoZWFkcywgVF9xLCBUX2spXG52aWRlbyAgICAgPSB0b3JjaC5yYW5kbig0LCAxNiwgMywgMTEyLCAxMTIpICMgKGJhdGNoLCBmcmFtZXMsIEMsIEgsIFcpXG5cbmZvciBuYW1lLCB0IGluIFsoJ3Rva2VucycsIHRva2VucyksICgnaW1hZ2UnLCBpbWFnZSksXG4gICAgICAgICAgICAgICAgKCdhdHRlbnRpb24nLCBhdHRlbnRpb24pLCAoJ3ZpZGVvJywgdmlkZW8pXTpcbiAgICBwcmludChmJ3tuYW1lfTogc2hhcGU9e3Quc2hhcGV9LCBudW1lbD17dC5udW1lbCgpOix9LCBNQj17dC5uYnl0ZXMvMWU2Oi4xZn0nKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVpbnN0ZWluIFN1bW1hdGlvbiBOb3RhdGlvbiAoZWluc3VtKSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiKipFaW5zdW0qKiBpcyBhIGNvbXBhY3Qgbm90YXRpb24gZm9yIGV4cHJlc3NpbmcgYW55IG11bHRpbGluZWFyIG9wZXJhdGlvbiAoZG90IHByb2R1Y3RzLCBtYXRyaXggbXVsdGlwbGllcywgb3V0ZXIgcHJvZHVjdHMsIHRyYWNlcywgdHJhbnNwb3NlcywgYW5kIGJleW9uZCkgdXNpbmcgaW5kZXggbGFiZWxzOlxuXG4gIG91dHB1dFtpLGtdID0gzqPisbwgQVtpLGpdICogQltqLGtdICDihpIgIGVpbnN1bSgnaWosamstPmlrJywgQSwgQilcblxuVGhlIHJ1bGVzOiBmcmVlIGluZGljZXMgKGFwcGVhcmluZyBpbiB0aGUgb3V0cHV0KSBhcmUga2VwdDsgY29udHJhY3RlZCBpbmRpY2VzIChhcHBlYXJpbmcgaW4gaW5wdXRzIGJ1dCBub3Qgb3V0cHV0KSBhcmUgc3VtbWVkIG92ZXIuIFRoaXMgbm90YXRpb24gaXMgbW9yZSBleHByZXNzaXZlIHRoYW4gYW55IHNpbmdsZSBmdW5jdGlvbiBhbmQgb2Z0ZW4gZ2VuZXJhdGVzIG1vcmUgZWZmaWNpZW50IGNvZGUgdGhhbiBleHBsaWNpdCBsb29wcyBvciBuZXN0ZWQgb3BlcmF0aW9ucy5cblxuRWluc3VtIGF2b2lkcyBtYXRlcmlhbGl6aW5nIGludGVybWVkaWF0ZSB0ZW5zb3JzLCBzdXBwb3J0cyBiYXRjaGluZyBuYXR1cmFsbHksIGFuZCBpcyBhdmFpbGFibGUgaW4gTnVtUHksIFB5VG9yY2gsIEpBWCAod2hlcmUgaXQncyBldmVuIEpJVC1jb21waWxlZCkuIFJlYWRpbmcgZWluc3VtOiB0aGUgYXJyb3cgc2VwYXJhdGVzIGlucHV0IGluZGV4IHBhdHRlcm5zIGZyb20gdGhlIG91dHB1dCBpbmRleCBwYXR0ZXJuLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuQSA9IHRvcmNoLnJhbmRuKDMsIDQpXG5CID0gdG9yY2gucmFuZG4oNCwgNSlcbnggPSB0b3JjaC5yYW5kbig0KVxuXG4jIE1hdHJpeCBtdWx0aXBseTogQ1tpLGtdID0gc3VtX2ogQVtpLGpdICogQltqLGtdXG5DID0gdG9yY2guZWluc3VtKCdpaixqay0+aWsnLCBBLCBCKSAgICMgKDMsNSlcbnByaW50KCdtYXRtdWw6JywgQy5zaGFwZSwgdG9yY2guYWxsY2xvc2UoQywgQSBAIEIpKVxuXG4jIE1hdHJpeC12ZWN0b3I6IHlbaV0gPSBzdW1faiBBW2ksal0gKiB4W2pdXG55ID0gdG9yY2guZWluc3VtKCdpaixqLT5pJywgQSwgeCkgICAgICMgKDMsKVxucHJpbnQoJ21hdHZlYzonLCB5LnNoYXBlLCB0b3JjaC5hbGxjbG9zZSh5LCBBIEAgeCkpXG5cbiMgT3V0ZXIgcHJvZHVjdDogUFtpLGpdID0gdVtpXSAqIHZbal1cbnUsIHYgPSB0b3JjaC5yYW5kbigzKSwgdG9yY2gucmFuZG4oNSlcblAgPSB0b3JjaC5laW5zdW0oJ2ksai0+aWonLCB1LCB2KSAgICAgIyAoMyw1KVxuXG4jIEJhdGNoIG1hdHJpeCBtdWx0aXBseTogQ1tiLGksa10gPSBzdW1faiBBW2IsaSxqXSpCW2IsaixrXVxuQTMgPSB0b3JjaC5yYW5kbig4LCAzLCA0KVxuQjMgPSB0b3JjaC5yYW5kbig4LCA0LCA1KVxuQzMgPSB0b3JjaC5laW5zdW0oJ2JpaixiamstPmJpaycsIEEzLCBCMykgICMgKDgsMyw1KVxucHJpbnQoJ2JhdGNoIG1hdG11bDonLCBDMy5zaGFwZSwgdG9yY2guYWxsY2xvc2UoQzMsIHRvcmNoLmJtbShBMywgQjMpKSlcblxuIyBUcmFjZTogdHIoQSlcbkFzcSA9IHRvcmNoLnJhbmRuKDQsIDQpXG50cmFjZSA9IHRvcmNoLmVpbnN1bSgnaWktPicsIEFzcSkgICAgICAjIHNjYWxhclxucHJpbnQoJ3RyYWNlOicsIHRyYWNlLml0ZW0oKSwgdG9yY2gudHJhY2UoQXNxKS5pdGVtKCkpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGVuc29yIENvbnRyYWN0aW9ucyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSAqKnRlbnNvciBjb250cmFjdGlvbioqIHN1bXMgb3ZlciBzaGFyZWQgaW5kaWNlcyBiZXR3ZWVuIHR3byB0ZW5zb3JzLCBnZW5lcmFsaXppbmcgbWF0cml4IG11bHRpcGxpY2F0aW9uIHRvIGhpZ2hlci1vcmRlciB0ZW5zb3JzLiBFaW5zdW0gY29tcGFjdGx5IGV4cHJlc3NlcyBhbnkgY29udHJhY3Rpb246XG5cbi0gTWF0cml4IG11bHRpcGx5OiBjb250cmFjdCBvdmVyIG9uZSBzaGFyZWQgaW5kZXhcbi0gRG91YmxlIGNvbnRyYWN0aW9uIChlLmcuLCBGcm9iZW5pdXMgaW5uZXIgcHJvZHVjdCDin6hBLELin6kgPSDOo+G1ouKxvCBB4bWi4rG8QuG1ouKxvCk6IGNvbnRyYWN0IG92ZXIgYWxsIHNoYXJlZCBpbmRpY2VzXG4tIE11bHRpLWluZGV4IGNvbnRyYWN0aW9uOiB1c2VkIGluIHRlbnNvciBuZXR3b3JrIG1ldGhvZHNcblxuSW4gZGVlcCBsZWFybmluZywgbXVsdGktaGVhZCBhdHRlbnRpb24gaXMgYSBmb3VyLXdheSBvcGVyYXRpb24uIENvbnZvbHV0aW9uIGlzIGVxdWl2YWxlbnQgdG8gYSB0ZW5zb3IgY29udHJhY3Rpb24gYmV0d2VlbiB0aGUgaW5wdXQgZmVhdHVyZSBtYXAgYW5kIHRoZSBmaWx0ZXIgdGVuc29yLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuIyBNdWx0aS1oZWFkIGF0dGVudGlvbiBlaW5zdW06IHNjb3Jlc1tiLGgsaSxqXSA9IFFbYixoLGksZF0gKiBLW2IsaCxqLGRdXG5CLCBILCBULCBEID0gMiwgOCwgMTYsIDY0XG5RID0gdG9yY2gucmFuZG4oQiwgSCwgVCwgRClcbksgPSB0b3JjaC5yYW5kbihCLCBILCBULCBEKVxuViA9IHRvcmNoLnJhbmRuKEIsIEgsIFQsIEQpXG5cbiMgUUteVCB2aWEgZWluc3VtIChhdm9pZHMgdHJhbnNwb3NlICsgbWF0bXVsKVxuc2NvcmVzID0gdG9yY2guZWluc3VtKCdiaGlkLGJoamQtPmJoaWonLCBRLCBLKSAvIEQqKjAuNSAgIyAoQixILFQsVClcbndlaWdodHMgPSB0b3JjaC5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKVxuIyBXZWlnaHRlZCBzdW0gb2YgdmFsdWVzXG5vdXRwdXQgPSB0b3JjaC5laW5zdW0oJ2JoaWosYmhqZC0+YmhpZCcsIHdlaWdodHMsIFYpICAgICMgKEIsSCxULEQpXG5wcmludCgnQXR0ZW50aW9uIG91dHB1dDonLCBvdXRwdXQuc2hhcGUpXG5cbiMgRnJvYmVuaXVzIGlubmVyIHByb2R1Y3Q6IHN1bSBvZiBlbGVtZW50d2lzZSBwcm9kdWN0c1xuQSA9IHRvcmNoLnJhbmRuKDMsIDQpXG5CXyA9IHRvcmNoLnJhbmRuKDMsIDQpXG5mcm9faXAgPSB0b3JjaC5laW5zdW0oJ2lqLGlqLT4nLCBBLCBCXykgICMgc2NhbGFyXG5wcmludCgnRnJvYiBpbm5lciBwcm9kdWN0OicsIGZyb19pcC5pdGVtKCksIChBICogQl8pLnN1bSgpLml0ZW0oKSkifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDUCBEZWNvbXBvc2l0aW9uIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiIqKkNBTkRFQ09NUC9QQVJBRkFDIChDUCkgZGVjb21wb3NpdGlvbioqIGV4cHJlc3NlcyBhIHJhbmstUiBhcHByb3hpbWF0aW9uIG9mIGEgdGVuc29yICoqVCoqIGFzIGEgc3VtIG9mIFIgcmFuay0xIHRlcm1zOlxuXG4gIFQg4omIIM6j4bWj4oKM4oKB4bS/IGHhtaMg4oqXIGLhtaMg4oqXIGPhtaNcblxud2hlcmUgKiphKirhtaMg4oqXICoqYioq4bWjIOKKlyAqKmMqKuG1oyBkZW5vdGVzIHRoZSBvdXRlciBwcm9kdWN0IG9mIHZlY3RvcnMuIFRoaXMgaXMgdGhlIHRlbnNvciBnZW5lcmFsaXphdGlvbiBvZiBTVkQncyByYW5rLTEgZGVjb21wb3NpdGlvbiBBID0gzqPhtaIgz4PhtaIgdeG1onbhtaLhtYAuIENQIGRlY29tcG9zaXRpb24gaXMgdXNlZCBmb3I6XG4tIENvbXByZXNzaW5nIDNEIHdlaWdodCB0ZW5zb3JzIGluIENOTnMvUk5Oc1xuLSBEaXNjb3ZlcmluZyBsYXRlbnQgZmFjdG9ycyBpbiBtdWx0aS1yZWxhdGlvbmFsIGRhdGEgKGtub3dsZWRnZSBncmFwaHMpXG4tIEFwcHJveGltYXRpbmcgaW50ZXJhY3Rpb24gdGVuc29ycyBpbiBwb2x5bm9taWFsIG5ldHdvcmtzIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHVja2VyIGFuZCBUZW5zb3IgVHJhaW4gRGVjb21wb3NpdGlvbnMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IioqVHVja2VyIGRlY29tcG9zaXRpb24qKiBnZW5lcmFsaXplcyBDUCBieSB1c2luZyBhIGNvcmUgdGVuc29yICoqRyoqIHdpdGggZmFjdG9yIG1hdHJpY2VzIGFsb25nIGVhY2ggbW9kZTpcblxuICBUIOKJiCBHIMOX4oKBIEEgw5figoIgQiDDl+KCgyBDXG5cbndoZXJlIMOX4oKZIGRlbm90ZXMgbW9kZS1uIHByb2R1Y3QuIFR1Y2tlciBjb21wcmVzc2VzIGVhY2ggbW9kZSBpbmRlcGVuZGVudGx5IGFuZCBjYW4gcmVwcmVzZW50IG1vcmUgZ2VuZXJhbCBzdHJ1Y3R1cmUgdGhhbiBDUC4gSXQgaXMgdGhlIHRlbnNvciBhbmFsb2cgb2YgdHJ1bmNhdGVkIFNWRC5cblxuKipUZW5zb3IgVHJhaW4gKFRUKSBkZWNvbXBvc2l0aW9uKiogcmVwcmVzZW50cyBhIGhpZ2gtb3JkZXIgdGVuc29yIGFzIGEgc2VxdWVuY2Ugb2YgM0QgJ2NvcmVzJyBjb25uZWN0ZWQgbGlrZSBhIGNoYWluOiBUW2nigoEsLi4uLGnigpldID0gR+KCgVtp4oKBXSBH4oKCW2nigoJdIC4uLiBH4oKZW2nigpldIChtYXRyaXggcHJvZHVjdHMpLiBUVCBkZWNvbXBvc2l0aW9uIGNhbiByZXByZXNlbnQgZXhwb25lbnRpYWxseSBsYXJnZSB0ZW5zb3JzIHdpdGggcG9seW5vbWlhbCBzdG9yYWdlIOKAlCB1c2VkIGZvciBjb21wcmVzc2luZyBlbWJlZGRpbmcgdGFibGVzIGluIHJlY29tbWVuZGF0aW9uIHN5c3RlbXMgYW5kIGFwcHJveGltYXRpbmcgaGlnaC1kaW1lbnNpb25hbCBmdW5jdGlvbnMuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udm9sdXRpb25zIGFzIFRlbnNvciBPcGVyYXRpb25zIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIDJEIGNvbnZvbHV0aW9uIGJldHdlZW4gaW5wdXQgKipYKiogKHNoYXBlIELDl0PhtaLigpnDl0jDl1cpIGFuZCBmaWx0ZXJzICoqVyoqIChD4oKS4bWk4oKcw5dD4bWi4oKZw5drSMOXa1cpIGlzIGEgdGVuc29yIGNvbnRyYWN0aW9uOlxuXG4gIFlbYiwgY19vdXQsIGgsIHddID0gzqNfe2NfaW4sIGtoLCBrd30gV1tjX291dCwgY19pbiwga2gsIGt3XSDCtyBYW2IsIGNfaW4sIGgra2gsIHcra3ddXG5cblRoaXMgaXMgYSBsb2NhbCBjb250cmFjdGlvbiBvdmVyIHRoZSBzcGF0aWFsIChrSCwga1cpIGFuZCBjaGFubmVsIChD4bWi4oKZKSBkaW1lbnNpb25zLiBFZmZpY2llbnQgY29udm9sdXRpb24gaW1wbGVtZW50YXRpb25zIChpbTJjb2wsIFdpbm9ncmFkLCBGRlQtYmFzZWQpIGFsbCByZWR1Y2UgdGhpcyB0ZW5zb3Igb3BlcmF0aW9uIHRvIGJhdGNoZWQgbWF0cml4IG11bHRpcGxpZXMsIGV4cGxvaXRpbmcgQkxBUyByb3V0aW5lcyBhbmQgVGVuc29yIENvcmVzLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuIyBFeHBsaWNpdCBzbWFsbCBjb252b2x1dGlvbiBmb3IgdW5kZXJzdGFuZGluZ1xuWCA9IHRvcmNoLnJhbmRuKDIsIDMsIDgsIDgpICAgICAjIChCLCBDX2luLCBILCBXKVxuVyA9IHRvcmNoLnJhbmRuKDE2LCAzLCAzLCAzKSAgICAjIChDX291dCwgQ19pbiwga0gsIGtXKVxuWSA9IEYuY29udjJkKFgsIFcsIHBhZGRpbmc9MSkgICAjICgyLCAxNiwgOCwgOClcbnByaW50KCdDb252IG91dHB1dDonLCBZLnNoYXBlKVxuXG4jIEVxdWl2YWxlbnQgZWluc3VtIChuYWl2ZSwgbm8gc2xpZGluZyDigJQganVzdCB0byBzaG93IHN0cnVjdHVyZSlcbiMgRm9yIGEgc2luZ2xlIHBvc2l0aW9uIChubyBzbGlkaW5nIHdpbmRvdyk6XG5YX3BhdGNoID0gWFs6LCA6LCA6MywgOjNdICAgICAgICMgKDIsIDMsIDMsIDMpIC0tIHRvcC1sZWZ0IHBhdGNoXG5ZXzAwID0gdG9yY2guZWluc3VtKCdiY2lqLG9jaWotPmJvJywgWF9wYXRjaCwgVykgICMgKDIsIDE2KVxucHJpbnQoJ1NpbmdsZSBwb3NpdGlvbiByZXN1bHQgc2hhcGU6JywgWV8wMC5zaGFwZSlcblxuIyBCYXRjaGVkIG1hdG11bCAoYm1tKTogYmF0Y2ggb2YgbWF0cml4IG11bHRpcGxpZXNcbkEgPSB0b3JjaC5yYW5kbigzMiwgMTI4LCA2NCkgICAjIChiYXRjaCwgVCwgZClcbkJfID0gdG9yY2gucmFuZG4oMzIsIDY0LCAxMjgpICAjIChiYXRjaCwgZCwgVClcbkMgPSB0b3JjaC5ibW0oQSwgQl8pICAgICAgICAgICAjICgzMiwgMTI4LCAxMjgpIC0tIGJhdGNoIG1hdG11bFxucHJpbnQoJ0JNTSBvdXRwdXQ6JywgQy5zaGFwZSkifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW5zb3IgUGFyYWxsZWxpc20gaW4gRGlzdHJpYnV0ZWQgVHJhaW5pbmcifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBtb2RlbHMgdG9vIGxhcmdlIHRvIGZpdCBvbiBhIHNpbmdsZSBHUFUsICoqdGVuc29yIHBhcmFsbGVsaXNtKiogc2hhcmRzIGluZGl2aWR1YWwgd2VpZ2h0IHRlbnNvcnMgYWNyb3NzIG11bHRpcGxlIEdQVXMuIEEgbGluZWFyIGxheWVyICoqWSA9IFhXKiogY2FuIGJlIHNwbGl0OlxuXG4tICoqQ29sdW1uLXBhcmFsbGVsKio6IFcgc3BsaXQgYnkgY29sdW1ucyDihpIgVyA9IFtX4oKBfFfigoJdOyBlYWNoIEdQVSBjb21wdXRlcyBYV+G1oiBhbmQgcmVzdWx0cyBhcmUgY29uY2F0ZW5hdGVkXG4tICoqUm93LXBhcmFsbGVsKio6IFcgc3BsaXQgYnkgcm93cyDihpIgVyA9IFtX4oKBO1figoJdOyBlYWNoIEdQVSBob2xkcyBhIHNsaWNlIG9mIFggYW5kIHBhcnQgb2YgVywgcmVzdWx0cyBhcmUgYWxsLXJlZHVjZWRcblxuTWVnYXRyb24tTE0gKE5WSURJQSkgcGlvbmVlcmVkIHRlbnNvciBwYXJhbGxlbGlzbSBmb3IgdHJhbnNmb3JtZXIgYXR0ZW50aW9uIGFuZCBmZWVkZm9yd2FyZCBsYXllcnMuIFRoZSBrZXkgaW5zaWdodDogdGhlIG1hdG11bCBpcyB0aGUgbW9zdCBjb21wdXRlLWludGVuc2l2ZSBvcGVyYXRpb24gYW5kIGNhbiBiZSBwYXJ0aXRpb25lZCB3aXRoIG1pbmltYWwgaW50ZXItR1BVIGNvbW11bmljYXRpb24gKG9ubHkgb25lIGFsbC1yZWR1Y2UgcGVyIGxheWVyIGhhbGYsIG5vdCBwZXIgbXVsdGlwbHkpLiJ9LAogIHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJQcmVmZXIgZWluc3VtIE92ZXIgRXhwbGljaXQgUmVzaGFwZStNYXRtdWwiLCJjb250ZW50IjoiRXhwcmVzc2luZyBtdWx0aS1kaW1lbnNpb25hbCBjb250cmFjdGlvbnMgd2l0aCBlaW5zdW0gaXMgY2xlYW5lciwgbGVzcyBlcnJvci1wcm9uZSwgYW5kIG9mdGVuIGZhc3RlciB0aGFuIHNlcXVlbmNlcyBvZiByZXNoYXBlL3RyYW5zcG9zZS9tYXRtdWwuIFB5VG9yY2gncyBlaW5zdW0gY2FuIGZ1c2Ugb3BlcmF0aW9ucyBhbmQgcmVkdWNlIHRlbXBvcmFyeSBhbGxvY2F0aW9ucy4gdG9yY2guZWluc3VtKCdiaGlkLGJoamQtPmJoaWonLCBRLCBLKSBpcyBjbGVhcmVyIGFuZCBlcXVpdmFsZW50IHRvIChRIEAgSy50cmFuc3Bvc2UoLTIsLTEpKSwgYnV0IGdlbmVyYWxpemVzIHRvIGFyYml0cmFyeSBpbmRleCBwYXR0ZXJucy4gVXNlIG9wdF9laW5zdW0gbGlicmFyeSBmb3Igb3B0aW1hbCBjb250cmFjdGlvbiBvcmRlciBvbiBsYXJnZSBuZXR3b3Jrcy4ifSwKICB7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRGVjb21wb3NpdGlvbiIsIkZvcm11bGEiLCJLZXkgVXNlIENhc2UiXSwicm93cyI6W1siQ1AiLCLOoyBh4bWj4oqXYuG1o+KKl2PhtaMiLCJDTk4gd2VpZ2h0IGNvbXByZXNzaW9uLCBmYWN0b3IgbW9kZWxzIl0sWyJUdWNrZXIiLCJHIMOX4oKBIEEgw5figoIgQiDDl+KCgyBDIiwiTXVsdGktbW9kZSBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb24iXSxbIlRlbnNvciBUcmFpbiIsIkfigoFH4oKCLi4uR+KCmSIsIkVtYmVkZGluZyBjb21wcmVzc2lvbiwgaGlnaC1kaW0gYXBwcm94Il0sWyJTVkQgKG1hdHJpeCkiLCJVzqNW4bWAIiwiTWF0cml4IGZhY3Rvcml6YXRpb24sIFBDQSJdLFsiTWF0cml4IHByb2R1Y3Qgc3RhdGUiLCJTYW1lIGFzIFRUIiwiUXVhbnR1bSBwaHlzaWNzLCBzZXF1ZW5jZSBtb2RlbGluZyJdXX0KXQo="
---

# Tensor Operations in ML

Tensors generalize matrices to higher dimensions — a 4D tensor holds an image batch, a 5D tensor holds a video batch. Tensor operations are the computational substrate of deep learning: convolutions, attention, batched matrix multiplies, and embedding lookups are all tensor operations. Mastering einsum notation and understanding tensor decompositions enables both efficient implementation and model compression.

## Higher-Order Tensors in Deep Learning

A rank-N tensor has N axes (dimensions). The most common tensor shapes in deep learning:

- **Rank-1**: `(d,)` — vector, embedding
- **Rank-2**: `(B, d)` — batch of embeddings
- **Rank-3**: `(B, T, d)` — batch of sequences (text, time series)
- **Rank-4**: `(B, C, H, W)` or `(B, H, W, C)` — batch of images
- **Rank-5**: `(B, T, C, H, W)` — batch of video frames

The **batch dimension B** is almost always the first axis in PyTorch convention. Operations are vectorized over the batch, enabling GPUs to process hundreds of examples simultaneously.

```python
import torch

# Common tensor shapes in ML
tokens    = torch.randn(32, 128, 512)   # (batch, seq_len, d_model)
image     = torch.randn(32, 3, 224, 224) # (batch, channels, H, W)
attention = torch.randn(32, 8, 128, 128) # (batch, heads, T_q, T_k)
video     = torch.randn(4, 16, 3, 112, 112) # (batch, frames, C, H, W)

for name, t in [('tokens', tokens), ('image', image),
                ('attention', attention), ('video', video)]:
    print(f'{name}: shape={t.shape}, numel={t.numel():,}, MB={t.nbytes/1e6:.1f}')
```

## Einstein Summation Notation (einsum)

**Einsum** is a compact notation for expressing any multilinear operation (dot products, matrix multiplies, outer products, traces, transposes, and beyond) using index labels:

  output[i,k] = Σⱼ A[i,j] * B[j,k]  →  einsum('ij,jk->ik', A, B)

The rules: free indices (appearing in the output) are kept; contracted indices (appearing in inputs but not output) are summed over. This notation is more expressive than any single function and often generates more efficient code than explicit loops or nested operations.

Einsum avoids materializing intermediate tensors, supports batching naturally, and is available in NumPy, PyTorch, JAX (where it's even JIT-compiled). Reading einsum: the arrow separates input index patterns from the output index pattern.

```python
import torch

A = torch.randn(3, 4)
B = torch.randn(4, 5)
x = torch.randn(4)

# Matrix multiply: C[i,k] = sum_j A[i,j] * B[j,k]
C = torch.einsum('ij,jk->ik', A, B)   # (3,5)
print('matmul:', C.shape, torch.allclose(C, A @ B))

# Matrix-vector: y[i] = sum_j A[i,j] * x[j]
y = torch.einsum('ij,j->i', A, x)     # (3,)
print('matvec:', y.shape, torch.allclose(y, A @ x))

# Outer product: P[i,j] = u[i] * v[j]
u, v = torch.randn(3), torch.randn(5)
P = torch.einsum('i,j->ij', u, v)     # (3,5)

# Batch matrix multiply: C[b,i,k] = sum_j A[b,i,j]*B[b,j,k]
A3 = torch.randn(8, 3, 4)
B3 = torch.randn(8, 4, 5)
C3 = torch.einsum('bij,bjk->bik', A3, B3)  # (8,3,5)
print('batch matmul:', C3.shape, torch.allclose(C3, torch.bmm(A3, B3)))

# Trace: tr(A)
Asq = torch.randn(4, 4)
trace = torch.einsum('ii->', Asq)      # scalar
print('trace:', trace.item(), torch.trace(Asq).item())
```

## Tensor Contractions

A **tensor contraction** sums over shared indices between two tensors, generalizing matrix multiplication to higher-order tensors. Einsum compactly expresses any contraction:

- Matrix multiply: contract over one shared index
- Double contraction (e.g., Frobenius inner product ⟨A,B⟩ = Σᵢⱼ AᵢⱼBᵢⱼ): contract over all shared indices
- Multi-index contraction: used in tensor network methods

In deep learning, multi-head attention is a four-way operation. Convolution is equivalent to a tensor contraction between the input feature map and the filter tensor.

```python
import torch

# Multi-head attention einsum: scores[b,h,i,j] = Q[b,h,i,d] * K[b,h,j,d]
B, H, T, D = 2, 8, 16, 64
Q = torch.randn(B, H, T, D)
K = torch.randn(B, H, T, D)
V = torch.randn(B, H, T, D)

# QK^T via einsum (avoids transpose + matmul)
scores = torch.einsum('bhid,bhjd->bhij', Q, K) / D**0.5  # (B,H,T,T)
weights = torch.softmax(scores, dim=-1)
# Weighted sum of values
output = torch.einsum('bhij,bhjd->bhid', weights, V)    # (B,H,T,D)
print('Attention output:', output.shape)

# Frobenius inner product: sum of elementwise products
A = torch.randn(3, 4)
B_ = torch.randn(3, 4)
fro_ip = torch.einsum('ij,ij->', A, B_)  # scalar
print('Frob inner product:', fro_ip.item(), (A * B_).sum().item())
```

## CP Decomposition

**CANDECOMP/PARAFAC (CP) decomposition** expresses a rank-R approximation of a tensor **T** as a sum of R rank-1 terms:

  T ≈ Σᵣ₌₁ᴿ aᵣ ⊗ bᵣ ⊗ cᵣ

where **a**ᵣ ⊗ **b**ᵣ ⊗ **c**ᵣ denotes the outer product of vectors. This is the tensor generalization of SVD's rank-1 decomposition A = Σᵢ σᵢ uᵢvᵢᵀ. CP decomposition is used for:
- Compressing 3D weight tensors in CNNs/RNNs
- Discovering latent factors in multi-relational data (knowledge graphs)
- Approximating interaction tensors in polynomial networks

## Tucker and Tensor Train Decompositions

**Tucker decomposition** generalizes CP by using a core tensor **G** with factor matrices along each mode:

  T ≈ G ×₁ A ×₂ B ×₃ C

where ×ₙ denotes mode-n product. Tucker compresses each mode independently and can represent more general structure than CP. It is the tensor analog of truncated SVD.

**Tensor Train (TT) decomposition** represents a high-order tensor as a sequence of 3D 'cores' connected like a chain: T[i₁,...,iₙ] = G₁[i₁] G₂[i₂] ... Gₙ[iₙ] (matrix products). TT decomposition can represent exponentially large tensors with polynomial storage — used for compressing embedding tables in recommendation systems and approximating high-dimensional functions.

## Convolutions as Tensor Operations

A 2D convolution between input **X** (shape B×Cᵢₙ×H×W) and filters **W** (Cₒᵤₜ×Cᵢₙ×kH×kW) is a tensor contraction:

  Y[b, c_out, h, w] = Σ_{c_in, kh, kw} W[c_out, c_in, kh, kw] · X[b, c_in, h+kh, w+kw]

This is a local contraction over the spatial (kH, kW) and channel (Cᵢₙ) dimensions. Efficient convolution implementations (im2col, Winograd, FFT-based) all reduce this tensor operation to batched matrix multiplies, exploiting BLAS routines and Tensor Cores.

```python
import torch
import torch.nn.functional as F

# Explicit small convolution for understanding
X = torch.randn(2, 3, 8, 8)     # (B, C_in, H, W)
W = torch.randn(16, 3, 3, 3)    # (C_out, C_in, kH, kW)
Y = F.conv2d(X, W, padding=1)   # (2, 16, 8, 8)
print('Conv output:', Y.shape)

# Equivalent einsum (naive, no sliding — just to show structure)
# For a single position (no sliding window):
X_patch = X[:, :, :3, :3]       # (2, 3, 3, 3) -- top-left patch
Y_00 = torch.einsum('bcij,ocij->bo', X_patch, W)  # (2, 16)
print('Single position result shape:', Y_00.shape)

# Batched matmul (bmm): batch of matrix multiplies
A = torch.randn(32, 128, 64)   # (batch, T, d)
B_ = torch.randn(32, 64, 128)  # (batch, d, T)
C = torch.bmm(A, B_)           # (32, 128, 128) -- batch matmul
print('BMM output:', C.shape)
```

## Tensor Parallelism in Distributed Training

For models too large to fit on a single GPU, **tensor parallelism** shards individual weight tensors across multiple GPUs. A linear layer **Y = XW** can be split:

- **Column-parallel**: W split by columns → W = [W₁|W₂]; each GPU computes XWᵢ and results are concatenated
- **Row-parallel**: W split by rows → W = [W₁;W₂]; each GPU holds a slice of X and part of W, results are all-reduced

Megatron-LM (NVIDIA) pioneered tensor parallelism for transformer attention and feedforward layers. The key insight: the matmul is the most compute-intensive operation and can be partitioned with minimal inter-GPU communication (only one all-reduce per layer half, not per multiply).

> **[TIP] Prefer einsum Over Explicit Reshape+Matmul**
>
> Expressing multi-dimensional contractions with einsum is cleaner, less error-prone, and often faster than sequences of reshape/transpose/matmul. PyTorch's einsum can fuse operations and reduce temporary allocations. torch.einsum('bhid,bhjd->bhij', Q, K) is clearer and equivalent to (Q @ K.transpose(-2,-1)), but generalizes to arbitrary index patterns. Use opt_einsum library for optimal contraction order on large networks.

| Decomposition | Formula | Key Use Case |
| --- | --- | --- |
| CP | Σ aᵣ⊗bᵣ⊗cᵣ | CNN weight compression, factor models |
| Tucker | G ×₁ A ×₂ B ×₃ C | Multi-mode dimensionality reduction |
| Tensor Train | G₁G₂...Gₙ | Embedding compression, high-dim approx |
| SVD (matrix) | UΣVᵀ | Matrix factorization, PCA |
| Matrix product state | Same as TT | Quantum physics, sequence modeling |
