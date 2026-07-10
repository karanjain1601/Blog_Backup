---
title: "Multi-Epoch Training for LLMs — Data Repetition Effects and Degradation"
slug: "multi-epoch-training"
description: "How training language models on repeated data degrades quality — DeepMind findings on loss increases at 4x and 32x repetition, double descent in multi-epoch regimes, domain-specific repetition thresholds, model memorization measurement, and mitigation via data augmentation and synthetic data mixing."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9kZXJuIGxhcmdlIGxhbmd1YWdlIG1vZGVscyBhcmUgdHJhaW5lZCBvbiB0cmlsbGlvbnMgb2YgdG9rZW5zIOKAlCBMTGFNQS0zLjEtOEIgb24gMTUgdHJpbGxpb24sIGZvciBleGFtcGxlIOKAlCB5ZXQgdGhlIHRvdGFsIHVuaXF1ZSB3ZWIgZGF0YSBhdmFpbGFibGUgZmFsbHMgd2VsbCBzaG9ydCBvZiB0aGF0IHRocmVzaG9sZC4gVGhlIHJlc3VsdCBpcyBpbmV2aXRhYmxlOiBzb21lIGRvY3VtZW50cyBhcmUgc2VlbiBtdWx0aXBsZSB0aW1lcyBkdXJpbmcgdHJhaW5pbmcuIFVuZGVyc3RhbmRpbmcgaG93IHJlcGV0aXRpb24gYWZmZWN0cyBtb2RlbCBxdWFsaXR5LCBtZW1vcml6YXRpb24sIGFuZCBkb3duc3RyZWFtIHBlcmZvcm1hbmNlIGlzIGVzc2VudGlhbCBmb3IgYW55b25lIGRlc2lnbmluZyBhIHByZXRyYWluaW5nIGRhdGEgcGlwZWxpbmUuIFRoZSBDaGluY2hpbGxhIHBhcGVyIGVzdGFibGlzaGVkIHRoYXQgZm9yIGEgY29tcHV0ZS1vcHRpbWFsIG1vZGVsLCB0cmFpbmluZyBvbiByb3VnaGx5IDEgZXBvY2ggaXMgaWRlYWw7IGJ1dCBpbmZlcmVuY2Utb3B0aW1pemVkIG1vZGVscyBpbnRlbnRpb25hbGx5IG92ZXJ0cmFpbiBwYXN0IHRoYXQgcG9pbnQsIHN1cmZhY2luZyB0aGUgbXVsdGktZXBvY2ggcHJvYmxlbSBhdCBzY2FsZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDaGluY2hpbGxhIFNjYWxpbmcgYW5kIHRoZSBTaW5nbGUtRXBvY2ggQXNzdW1wdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSG9mZm1hbm4gZXQgYWwuICgyMDIyKSBzaG93ZWQgdGhhdCBjb21wdXRlLW9wdGltYWwgdHJhaW5pbmcgYmFsYW5jZXMgbW9kZWwgcGFyYW1ldGVycyBOIGFuZCB0cmFpbmluZyB0b2tlbnMgRCBhcyBEIOKJiCAyME46IGEgNzBCIG1vZGVsIHRyYWluZWQgb24gMS40VCB0b2tlbnMsIHJvdWdobHkgb25lIHBhc3Mgb3ZlciBhIGxhcmdlIENvbW1vbiBDcmF3bCBzbmFwc2hvdC4gVGhlIGltcGxpY2l0IGFzc3VtcHRpb24gaXMgYSBzaW5nbGUgcGFzcyBvdmVyIHRoZSBkYXRhLiBJbmZlcmVuY2Utb3B0aW1pemVkIG1vZGVscyDigJQgTExhTUEtMy4xLCBNaXN0cmFsLCBHZW1tYSDigJQgZGVsaWJlcmF0ZWx5IHZpb2xhdGUgdGhpcyBieSBvdmVydHJhaW5pbmcgb24gMTXigJMzMFQgdG9rZW5zIHdpdGggc21hbGxlciBwYXJhbWV0ZXIgY291bnRzLCBwcm9kdWNpbmcgY2hlYXBlci10by1zZXJ2ZSBtb2RlbHMgdGhhdCBzdGlsbCBwZXJmb3JtIHdlbGwuIFRoZSB0cmFkZW9mZiBpcyBkYXRhIHJlcGV0aXRpb246IGFueSAxVC10b2tlbiBzb3VyY2UgaW4gYSAxNVQtdG9rZW4gcnVuIGFwcGVhcnMgcm91Z2hseSAxNSB0aW1lcyBpZiBub3QgZGl2ZXJzaWZpZWQgd2l0aCBmcmVzaCBjcmF3bCBkYXRhLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRhdGEgUmVwZXRpdGlvbiBFZmZlY3RzIOKAlCBEZWVwTWluZCBSZXNlYXJjaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVlcE1pbmRcdTAwMjdzIHJlc2VhcmNoIGludG8gbXVsdGktZXBvY2ggdHJhaW5pbmcgKEhlcm5hbmRleiBldCBhbC4gMjAyMiwgTXVlbm5pZ2hvZmYgZXQgYWwuIDIwMjMpIHByb2R1Y2VkIHF1YW50aXRhdGl2ZSBiYXNlbGluZXM6IHJlcGVhdGluZyB0aGUgdHJhaW5pbmcgY29ycHVzIDQgdGltZXMgY2F1c2VzIGFwcHJveGltYXRlbHkgNSUgdmFsaWRhdGlvbiBsb3NzIGluY3JlYXNlIHZlcnN1cyBhIHNpbmdsZS1lcG9jaCBiYXNlbGluZTsgMzIgcmVwZXRpdGlvbnMgY2F1c2VzIGFwcHJveGltYXRlbHkgMjAlIGxvc3MgaW5jcmVhc2UuIFRoZSBkZWdyYWRhdGlvbiBpcyBub24tbGluZWFyIOKAlCB0aGUgZmlyc3QgcmVwZXRpdGlvbiBhZGRzIGFsbW9zdCBubyBjb3N0LCB0aGUgZm91cnRoIGFkZHMgYSBub3RpY2VhYmxlIGFtb3VudCwgYW5kIGVhY2ggc3Vic2VxdWVudCBkb3VibGluZyBhZGRzIHByb3BvcnRpb25hbGx5IG1vcmUuIE11ZW5uaWdob2ZmIGV0IGFsLiBhbHNvIG9ic2VydmVkIGEgZG91YmxlIGRlc2NlbnQgYW5hbG9nOiBhZnRlciBlbm91Z2ggcmVwZXRpdGlvbiwgbG9zcyBpbml0aWFsbHkgd29yc2VucywgYnJpZWZseSBpbXByb3ZlcyBhcyB0aGUgbW9kZWwgbWVtb3JpemVzLCB0aGVuIHdvcnNlbnMgYWdhaW4gYXMgbWVtb3JpemF0aW9uIGRvbWluYXRlcyBnZW5lcmFsaXphdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHJhbmRvbVxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3QsIEl0ZXJhdG9yXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IEl0ZXJhYmxlRGF0YXNldFxuXG5jbGFzcyBNdWx0aUVwb2NoRGF0YXNldChJdGVyYWJsZURhdGFzZXQpOlxuICAgIFwiXCJcIlNodWZmbGUgZG9jdW1lbnRzIGFjcm9zcyBlcG9jaHM7IHRyYWNrIHBlci1kb2N1bWVudCByZXBldGl0aW9uIGNvdW50LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkb2N1bWVudHM6IExpc3QsIG1heF9lcG9jaHM6IGludCA9IDQsIHNlZWQ6IGludCA9IDQyKTpcbiAgICAgICAgc2VsZi5kb2N1bWVudHMgPSBkb2N1bWVudHNcbiAgICAgICAgc2VsZi5tYXhfZXBvY2hzID0gbWF4X2Vwb2Noc1xuICAgICAgICBzZWxmLnJuZyA9IHJhbmRvbS5SYW5kb20oc2VlZClcbiAgICAgICAgc2VsZi5lcG9jaF9jb3VudHMgPSBbMF0gKiBsZW4oZG9jdW1lbnRzKVxuXG4gICAgZGVmIF9faXRlcl9fKHNlbGYpIC1cdTAwM2UgSXRlcmF0b3I6XG4gICAgICAgIGZvciBlcG9jaCBpbiByYW5nZShzZWxmLm1heF9lcG9jaHMpOlxuICAgICAgICAgICAgaW5kaWNlcyA9IGxpc3QocmFuZ2UobGVuKHNlbGYuZG9jdW1lbnRzKSkpXG4gICAgICAgICAgICBzZWxmLnJuZy5zaHVmZmxlKGluZGljZXMpICAgICAgICAgICMgZGlmZmVyZW50IG9yZGVyIGVhY2ggZXBvY2hcbiAgICAgICAgICAgIGZvciBpZHggaW4gaW5kaWNlczpcbiAgICAgICAgICAgICAgICBzZWxmLmVwb2NoX2NvdW50c1tpZHhdICs9IDFcbiAgICAgICAgICAgICAgICB5aWVsZCB7XCJ0b2tlbnNcIjogc2VsZi5kb2N1bWVudHNbaWR4XSwgXCJlcG9jaFwiOiBlcG9jaCxcbiAgICAgICAgICAgICAgICAgICAgICAgXCJkb2NfaWRcIjogaWR4LCBcInJlcGV0aXRpb25fY291bnRcIjogc2VsZi5lcG9jaF9jb3VudHNbaWR4XX1cblxuIyAxLDAwMCBkb2N1bWVudHMgeCA0IGVwb2NocyAtLSBubyBkb2N1bWVudCBleGNlZWRzIDR4IHJlcGV0aXRpb25cbmRvY3MgPSBbbGlzdChyYW5nZSg1MTIpKSBmb3IgXyBpbiByYW5nZSgxXzAwMCldXG5kYXRhc2V0ID0gTXVsdGlFcG9jaERhdGFzZXQoZG9jcywgbWF4X2Vwb2Nocz00KVxudG90YWwgPSBzdW0oMSBmb3IgXyBpbiBkYXRhc2V0KVxucHJpbnQoZlwiVG90YWwgc2FtcGxlczoge3RvdGFsfSwgbWF4IHJlcGV0aXRpb25zOiB7bWF4KGRhdGFzZXQuZXBvY2hfY291bnRzKX1cIilcbmFzc2VydCBtYXgoZGF0YXNldC5lcG9jaF9jb3VudHMpID09IDQsIFwiUmVwZXRpdGlvbiBsaW1pdCB2aW9sYXRlZFwiXG5wcmludChcIkFsbCBkb2N1bWVudHMgc3RheSB3aXRoaW4gdGhlIDR4IHJlcGV0aXRpb24gbGltaXRcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZWFzdXJpbmcgRGVncmFkYXRpb24gRW1waXJpY2FsbHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZ3JhZGF0aW9uIGZyb20gZGF0YSByZXBldGl0aW9uIGlzIG1lYXN1cmVkIGJ5IHRyYWluaW5nIGlkZW50aWNhbCBtb2RlbCBhcmNoaXRlY3R1cmVzIG9uIDF4LCAyeCwgNHgsIGFuZCA4eCByZXBldGl0aW9ucyBvZiB0aGUgc2FtZSBmaXhlZCBkYXRhc2V0LCB0aGVuIGV2YWx1YXRpbmcgb24gYSBoZWxkLW91dCBzZXQgdGhhdCB3YXMgbmV2ZXIgcmVwZWF0ZWQuIFRoZSBrZXkgaXMgZW5zdXJpbmcgaGVsZC1vdXQgZGF0YSBjb21lcyBmcm9tIHRoZSBzYW1lIGRpc3RyaWJ1dGlvbiBidXQgaXMgY29tcGxldGVseSBkaXNqb2ludCBmcm9tIHRyYWluaW5nIOKAlCBvdGhlcndpc2UgdGhlIG1lYXN1cmVtZW50IGNvbmZsYXRlcyBkaXN0cmlidXRpb24gc2hpZnQgd2l0aCByZXBldGl0aW9uIGVmZmVjdHMuIFRoZSBtZXRyaWMgaXMgYWJzb2x1dGUgdmFsaWRhdGlvbiBsb3NzIGFuZCB0aGUgcGVyY2VudGFnZSBpbmNyZWFzZSByZWxhdGl2ZSB0byB0aGUgMXggYmFzZWxpbmUuIFBlcnBsZXhpdHkgaXMgbGVzcyB1c2VmdWwgaGVyZSBiZWNhdXNlIGl0IGdyb3dzIGV4cG9uZW50aWFsbHkgd2l0aCBsb3NzLCBhbXBsaWZ5aW5nIHNtYWxsIGFic29sdXRlIGNoYW5nZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCByYW5kb21cbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFMb2FkZXIsIFRlbnNvckRhdGFzZXRcblxuZGVmIG1lYXN1cmVfcmVwZXRpdGlvbl9kZWdyYWRhdGlvbih0b2tlbl9jb3JwdXMsIHJlcF9jb3VudHMsIHNlcV9sZW49NjQsIHN0ZXBzPTMwMCk6XG4gICAgXCJcIlwiVHJhaW4gYSB0aW55IExNIG9uIGNvcnB1cyByZXBlYXRlZCBOIHRpbWVzOyByZXR1cm4gZXZhbCBsb3NzIHBlciByZXAgY291bnQuXCJcIlwiXG4gICAgdm9jYWJfc2l6ZSA9IG1heCh0b2tlbl9jb3JwdXMpICsgMVxuICAgIHJlc3VsdHMgPSB7fVxuICAgIGZvciByZXBzIGluIHJlcF9jb3VudHM6XG4gICAgICAgIHRva2VucyA9IHRva2VuX2NvcnB1cyAqIHJlcHNcbiAgICAgICAgcmFuZG9tLnNodWZmbGUodG9rZW5zKVxuICAgICAgICBzZXFzID0gW3Rva2Vuc1tpOmkrc2VxX2xlbisxXSBmb3IgaSBpbiByYW5nZSgwLCBsZW4odG9rZW5zKS1zZXFfbGVuLCBzZXFfbGVuKV1cbiAgICAgICAgeHMgICA9IHRvcmNoLnRlbnNvcihbc1s6LTFdIGZvciBzIGluIHNlcXNdKVxuICAgICAgICB5cyAgID0gdG9yY2gudGVuc29yKFtzWzE6XSAgZm9yIHMgaW4gc2Vxc10pXG4gICAgICAgIGxvYWRlciA9IERhdGFMb2FkZXIoVGVuc29yRGF0YXNldCh4cywgeXMpLCBiYXRjaF9zaXplPTY0LCBzaHVmZmxlPVRydWUpXG4gICAgICAgIG1vZGVsICA9IG5uLlNlcXVlbnRpYWwobm4uRW1iZWRkaW5nKHZvY2FiX3NpemUsIDY0KSwgbm4uTGluZWFyKDY0LCB2b2NhYl9zaXplKSlcbiAgICAgICAgb3B0ICAgID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTNlLTQpXG4gICAgICAgIGZvciBzdGVwLCAoeCwgeSkgaW4gemlwKHJhbmdlKHN0ZXBzKSwgbG9hZGVyKTpcbiAgICAgICAgICAgIGVtYiAgPSBtb2RlbFswXSh4KS5tZWFuKDEpXG4gICAgICAgICAgICBsb3NzID0gbm4uZnVuY3Rpb25hbC5jcm9zc19lbnRyb3B5KG1vZGVsWzFdKGVtYiksIHlbOiwgc2VxX2xlbiAvLyAyXSlcbiAgICAgICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgICAgIHJlc3VsdHNbcmVwc10gPSBsb3NzLml0ZW0oKVxuICAgIHJldHVybiByZXN1bHRzXG5cbmNvcnB1cyA9IGxpc3QocmFuZ2UoNTAwKSkgKiAyMDAgICAgIyAxMDBLIHRva2VuIGNvcnB1c1xubG9zc2VzID0gbWVhc3VyZV9yZXBldGl0aW9uX2RlZ3JhZGF0aW9uKGNvcnB1cywgcmVwX2NvdW50cz1bMSwgMiwgNCwgOF0pXG5iYXNlICAgPSBsb3NzZXNbMV1cbmZvciByLCBsIGluIGxvc3Nlcy5pdGVtcygpOlxuICAgIHByaW50KGZcIiAge3J9eDogbG9zcz17bDouNGZ9ICAoK3sobCAtIGJhc2UpIC8gYmFzZSAqIDEwMDouMWZ9JSB2cyAxeClcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEb21haW4tU3BlY2lmaWMgUmVwZXRpdGlvbiBTdHJhdGVnaWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOb3QgYWxsIGRhdGEgZG9tYWlucyBkZWdyYWRlIGVxdWFsbHkgd2l0aCByZXBldGl0aW9uLiBSZXBlYXRlZCBjb2RlIGRhdGEgc2hvd3MgbGVzcyBsb3NzIGRlZ3JhZGF0aW9uIHRoYW4gcmVwZWF0ZWQgd2ViIHRleHQsIHBvc3NpYmx5IGJlY2F1c2UgY29kZSBoYXMgbW9yZSBzdHJ1Y3R1cmVkLCBsZWFybmFibGUgcGF0dGVybnMgd2l0aCBsb3dlciBlbnRyb3B5LiBCb29rcyB0b2xlcmF0ZSBtb2RlcmF0ZSByZXBldGl0aW9uICgz4oCTNHgpIGJlY2F1c2Ugc2lnbmFsIGRlbnNpdHkgaXMgaGlnaCBhbmQgcmVkdW5kYW5jeSBpcyBsb3cuIFdlYiBjcmF3bCB0ZXh0IOKAlCB0aGUgbGFyZ2VzdCBhbmQgbm9pc2llc3Qgc291cmNlIOKAlCBzaG91bGQgYmUga2VwdCBhdCAxeCB3aGVyZXZlciBwb3NzaWJsZS4gVGhlIHByYWN0aWNhbCBzb2x1dGlvbiBpcyBhIGRvbWFpbi13ZWlnaHRlZCBtaXhpbmcgc2NoZWR1bGU6IGFzc2lnbiBwZXItZG9tYWluIGVwb2NoIGJ1ZGdldHMgdGhhdCByZWZsZWN0IGVhY2ggZG9tYWluXHUwMDI3cyByZXBldGl0aW9uIHRvbGVyYW5jZSByYXRoZXIgdGhhbiByZXBlYXRpbmcgdGhlIGVudGlyZSBjb3JwdXMgdW5pZm9ybWx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmFuZG9tXG5mcm9tIHR5cGluZyBpbXBvcnQgRGljdCwgTGlzdFxuXG5kZWYgYnVpbGRfbWl4ZWRfZGF0YXNldChkb21haW5fY29ycG9yYTogRGljdFtzdHIsIExpc3RdLCBkb21haW5fZXBvY2hzOiBEaWN0W3N0ciwgaW50XSxcbiAgICAgICAgICAgICAgICAgICAgICAgIHNlZWQ6IGludCA9IDQyKSAtXHUwMDNlIExpc3Q6XG4gICAgXCJcIlwiTWl4IGRvbWFpbiBjb3Jwb3JhIHdpdGggZGlmZmVyZW50IHJlcGV0aXRpb24gY291bnRzIGludG8gb25lIHRyYWluaW5nIHNldC5cIlwiXCJcbiAgICBybmcgPSByYW5kb20uUmFuZG9tKHNlZWQpXG4gICAgbWl4ZWQgPSBbXVxuICAgIGZvciBkb21haW4sIGNvcnB1cyBpbiBkb21haW5fY29ycG9yYS5pdGVtcygpOlxuICAgICAgICBlcG9jaHMgPSBkb21haW5fZXBvY2hzLmdldChkb21haW4sIDEpXG4gICAgICAgIHJlcGVhdGVkID0gY29ycHVzICogZXBvY2hzXG4gICAgICAgIHJuZy5zaHVmZmxlKHJlcGVhdGVkKVxuICAgICAgICBtaXhlZC5leHRlbmQocmVwZWF0ZWQpXG4gICAgICAgIHByaW50KGZcIiAge2RvbWFpbjoxMHN9OiB7bGVuKGNvcnB1cyk6XHUwMDNlOCx9IGRvY3MgeCB7ZXBvY2hzfWVwID0ge2xlbihyZXBlYXRlZCk6XHUwMDNlOCx9IHNhbXBsZXNcIilcbiAgICBybmcuc2h1ZmZsZShtaXhlZCkgICAgIyBnbG9iYWwgc2h1ZmZsZSBhY3Jvc3MgYWxsIGRvbWFpbnNcbiAgICByZXR1cm4gbWl4ZWRcblxuIyBMTGFNQS0zLjEtc3R5bGUgZG9tYWluIG1peGluZzogaGlnaC1xdWFsaXR5IHNvdXJjZXMgZ2V0IG1vcmUgcmVwZXRpdGlvbnNcbkRPTUFJTl9DT1JQT1JBID0ge1xuICAgIFwiYm9va3NcIjogIFtmXCJib29rX2RvY197aX1cIiAgZm9yIGkgaW4gcmFuZ2UoNTBfMDAwKV0sXG4gICAgXCJjb2RlXCI6ICAgW2ZcImNvZGVfZG9jX3tpfVwiICBmb3IgaSBpbiByYW5nZSg4MF8wMDApXSxcbiAgICBcIndlYlwiOiAgICBbZlwid2ViX2RvY197aX1cIiAgIGZvciBpIGluIHJhbmdlKDUwMF8wMDApXSxcbn1cbkRPTUFJTl9FUE9DSFMgPSB7XCJib29rc1wiOiA0LCBcImNvZGVcIjogMiwgXCJ3ZWJcIjogMX0gICMgc3RheSBiZWxvdyA0eCBmb3IgYm9va3Ncbm1peGVkID0gYnVpbGRfbWl4ZWRfZGF0YXNldChET01BSU5fQ09SUE9SQSwgRE9NQUlOX0VQT0NIUylcbnByaW50KGZcIlRvdGFsIHRyYWluaW5nIHNhbXBsZXM6IHtsZW4obWl4ZWQpOix9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9kZWwgTWVtb3JpemF0aW9uIGFuZCBQcml2YWN5IFJpc2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNhcmxpbmkgZXQgYWwuICgyMDIxLCAyMDIzKSBkZW1vbnN0cmF0ZWQgdGhhdCBMTE1zIG1lbW9yaXplIHRyYWluaW5nIGRhdGEgdmVyYmF0aW0gaW4gbWVhc3VyYWJsZSB3YXlzLCBhbmQgdGhhdCBtZW1vcml6YXRpb24gcmF0ZSBzY2FsZXMgd2l0aCByZXBldGl0aW9uIGNvdW50LiBBIGRvY3VtZW50IGFwcGVhcmluZyBvbmNlIGlzIHJhcmVseSBleHRyYWN0YWJsZSB2aWEgcHJlZml4IGNvbXBsZXRpb247IGEgZG9jdW1lbnQgYXBwZWFyaW5nIDEwMCB0aW1lcyBpcyBvZnRlbiByZWNvdmVyYWJsZSB3aXRoIGEgc2hvcnQgcHJlZml4LiBCZXlvbmQgcXVhbGl0eSBkZWdyYWRhdGlvbiwgbWVtb3JpemF0aW9uIGNhcnJpZXMgcHJpdmFjeSBhbmQgbGVnYWwgcmlzazogUElJIGluIHJlcGVhdGVkIGRvY3VtZW50cywgY29weXJpZ2h0IHRleHQsIG9yIHByb3ByaWV0YXJ5IGNvZGUgY2FuIGJlIGV4dHJhY3RlZCBieSBhZHZlcnNhcmllcy4gTWVhc3VyaW5nIGV4dHJhY3Rpb24gcmF0ZSDigJQgdGhlIGZyYWN0aW9uIG9mIHRyYWluaW5nIGRvY3VtZW50cyByZWNvdmVyYWJsZSB2aWEgZ3JlZWR5IGRlY29kaW5nIGdpdmVuIGEgNTAtdG9rZW4gcHJlZml4IOKAlCBpcyB0aGUgc3RhbmRhcmQgZW1waXJpY2FsIHByb3h5IGZvciBtZW1vcml6YXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3RcblxuZGVmIGNvbXB1dGVfZXh0cmFjdGlvbl9yYXRlKG1vZGVsLCB0b2tlbml6ZXIsIHRyYWluX2RvY3M6IExpc3Rbc3RyXSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmVmaXhfbGVuOiBpbnQgPSA1MCwgZ2VuX2xlbjogaW50ID0gNTAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF0Y2hfdGhyZXNob2xkOiBmbG9hdCA9IDAuNykgLVx1MDAzZSBmbG9hdDpcbiAgICBcIlwiXCJFc3RpbWF0ZSBmcmFjdGlvbiBvZiB0cmFpbmluZyBkb2NzIHJlY292ZXJhYmxlIHZpYSBncmVlZHkgcHJlZml4IGNvbXBsZXRpb24uXCJcIlwiXG4gICAgZXh0cmFjdGVkID0gMFxuICAgIGZvciBkb2MgaW4gdHJhaW5fZG9jczpcbiAgICAgICAgaWRzID0gdG9rZW5pemVyKGRvYywgcmV0dXJuX3RlbnNvcnM9XCJwdFwiLCB0cnVuY2F0aW9uPVRydWUsIG1heF9sZW5ndGg9MjAwKS5pbnB1dF9pZHNcbiAgICAgICAgcHJlZml4ID0gaWRzWzosIDpwcmVmaXhfbGVuXVxuICAgICAgICBzdWZmaXggPSBpZHNbOiwgcHJlZml4X2xlbjpwcmVmaXhfbGVuICsgZ2VuX2xlbl1cbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICBnZW4gPSBtb2RlbC5nZW5lcmF0ZShwcmVmaXgsIG1heF9uZXdfdG9rZW5zPWdlbl9sZW4sIGRvX3NhbXBsZT1GYWxzZSlcbiAgICAgICAgZ2VuX3N1ZmZpeCA9IGdlbls6LCBwcmVmaXhfbGVuOl1cbiAgICAgICAgbWluX2xlbiA9IG1pbihnZW5fc3VmZml4LnNoYXBlWzFdLCBzdWZmaXguc2hhcGVbMV0pXG4gICAgICAgIG1hdGNoID0gKGdlbl9zdWZmaXhbOiwgOm1pbl9sZW5dID09IHN1ZmZpeFs6LCA6bWluX2xlbl0pLmZsb2F0KCkubWVhbigpLml0ZW0oKVxuICAgICAgICBleHRyYWN0ZWQgKz0gaW50KG1hdGNoIFx1MDAzZT0gbWF0Y2hfdGhyZXNob2xkKVxuICAgIHJldHVybiBleHRyYWN0ZWQgLyBsZW4odHJhaW5fZG9jcylcblxuIyBTeW50aGV0aWMgcHJveHk6IG1lbW9yaXphdGlvbiByYXRlIGdyb3dzIHdpdGggcmVwZXRpdGlvbiBjb3VudFxucHJpbnQoXCJSZXBldGl0aW9uIHwgRXh0cmFjdGlvbiBSYXRlIHwgTWVtb3JpemF0aW9uIFJpc2tcIilcbnByaW50KFwiLVwiICogNDgpXG5mb3IgcmVwcywgcmF0ZSBpbiBbKDEsIDAuMDIpLCAoMiwgMC4wNiksICg0LCAwLjE1KSwgKDgsIDAuMzEpLCAoMTYsIDAuNTIpXTpcbiAgICByaXNrID0gXCJMb3dcIiBpZiByYXRlIFx1MDAzYyAwLjEgZWxzZSAoXCJNZWRpdW1cIiBpZiByYXRlIFx1MDAzYyAwLjMgZWxzZSBcIkhpZ2hcIilcbiAgICBwcmludChmXCIgICB7cmVwczpcdTAwM2UyfXggICAgfCAgICAge3JhdGU6LjAlfSAgICAgICAgICB8IHtyaXNrfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1pdGlnYXRpb24gU3RyYXRlZ2llcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiB0aGUgZGF0YSBidWRnZXQgaXMgZXhoYXVzdGVkIGFuZCBhZGRpdGlvbmFsIHJlcGV0aXRpb24gYmVjb21lcyBuZWNlc3NhcnksIHNldmVyYWwgc3RyYXRlZ2llcyByZWR1Y2UgcXVhbGl0eSBkZWdyYWRhdGlvbi4gRGF0YSBhdWdtZW50YXRpb24g4oCUIGJhY2stdHJhbnNsYXRpb24sIHBhcmFwaHJhc2UgbW9kZWxzLCBzZW50ZW5jZSByZW9yZGVyaW5nIOKAlCBjcmVhdGVzIHNlbWFudGljYWxseSBzaW1pbGFyIGJ1dCB0b2tlbi1kaXN0aW5jdCB2YXJpYW50cyB0aGF0IHByb3ZpZGUgZnJlc2ggc2lnbmFsLiBNaXhpbmcgZnJlc2ggd2ViIGNyYXdsIHNuYXBzaG90cyB3aXRoIGhpZ2gtcXVhbGl0eSByZXBlYXRlZCBzb3VyY2VzIGRpbHV0ZXMgdGhlIGVmZmVjdGl2ZSByZXBldGl0aW9uIHJhdGUuIEN1cnJpY3VsdW0gbGVhcm5pbmcsIHByZXNlbnRpbmcgbGVzcy1yZXBlYXRlZCBkYXRhIGxhdGVyIGluIHRyYWluaW5nIHdoZW4gdGhlIG1vZGVsIGlzIG1vcmUgY2FwYWJsZSwgY2FuIGhlbHAsIHRob3VnaCBldmlkZW5jZSBmb3IgbGFuZ3VhZ2UgbW9kZWxzIHNwZWNpZmljYWxseSBpcyBtaXhlZC4gRGVkdXBsaWNhdGlvbiBpcyB0aGUgY29tcGxlbWVudGFyeSBkZWZlbnNlOiBhZ2dyZXNzaXZlIE1pbkhhc2ggb3IgZXhhY3QtbWF0Y2ggZGVkdXBsaWNhdGlvbiBiZWZvcmUgdHJhaW5pbmcgcmVtb3ZlcyBpbXBsaWNpdCByZXBldGl0aW9uIGZyb20gbmVhci1kdXBsaWNhdGUgd2ViIHBhZ2VzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQmFjay10cmFuc2xhdGlvbjogdHJhbnNsYXRlIGRvY3VtZW50cyB0byBhIHNlY29uZCBsYW5ndWFnZSBhbmQgYmFjayB0byBwcm9kdWNlIG5lYXItZHVwbGljYXRlIGJ1dCB0b2tlbi1kaXN0aW5jdCB0cmFpbmluZyBleGFtcGxlcy4iLCJQYXJhcGhyYXNlIGF1Z21lbnRhdGlvbjogdXNlIGEgc2VwYXJhdGVseSB0cmFpbmVkIHBhcmFwaHJhc2UgbW9kZWwgdG8gcmV3cml0ZSBkb2N1bWVudHMgYmVmb3JlIGVhY2ggcmVwZXRpdGlvbiBlcG9jaC4iLCJDcmF3bCBkaXZlcnNpZmljYXRpb246IG1peCBmcmVzaCBDb21tb25DcmF3bCBzbmFwc2hvdHMgZnJvbSBkaWZmZXJlbnQgbW9udGhzIHJhdGhlciB0aGFuIHJlcGVhdGluZyB0aGUgc2FtZSBzbmFwc2hvdC4iLCJTeW50aGV0aWMgZGF0YSBpbnNlcnRpb246IHVzZSB0aGUgbW9kZWwgaXRzZWxmIG9yIGEgc21hbGxlciB0ZWFjaGVyIHRvIGdlbmVyYXRlIHRleHQgb24gdHJhaW5pbmcgdG9waWNzLCBpbmplY3RpbmcgaXQgYXMgcHNldWRvLWZyZXNoIGRhdGEuIiwiRG9tYWluIGVwb2NoIGJ1ZGdldGluZzogYXNzaWduIHBlci1zb3VyY2UgcmVwZXRpdGlvbiBsaW1pdHMgcmF0aGVyIHRoYW4gcmVwZWF0aW5nIHRoZSBlbnRpcmUgY29ycHVzIHVuaWZvcm1seS4iLCJQcmUtdHJhaW5pbmcgZGVkdXBsaWNhdGlvbjogYXBwbHkgTWluSGFzaCBMU0ggb3IgZXhhY3QtbWF0Y2ggZGVkdXBsaWNhdGlvbiB0byByZW1vdmUgbmVhci1kdXBsaWNhdGUgd2ViIHBhZ2VzIGJlZm9yZSBhbnkgcmVwZXRpdGlvbiBjb3VudGluZy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3ludGhldGljIERhdGEgYW5kIFJMSEYgQ29uc2lkZXJhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vZGVsLWdlbmVyYXRlZCBzeW50aGV0aWMgZGF0YSBzZXJ2ZXMgYXMgcHNldWRvLWZyZXNoIHRyYWluaW5nIHNpZ25hbDogaXQgaGFzIG5ldmVyIGFwcGVhcmVkIGluIHRoZSB0cmFpbmluZyBzZXQgZXhhY3RseSBhcyB3cml0dGVuLCBzbyBpdCBkb2VzIG5vdCBjb3VudCBhcyBhIHJlcGV0aXRpb24gb2YgZXhpc3RpbmcgZG9jdW1lbnRzLiBUaGUgcmlzayBpcyBtb2RlIGNvbGxhcHNlIOKAlCBpZiBzeW50aGV0aWMgZGF0YSBkb21pbmF0ZXMsIHRoZSBtb2RlbCBjb252ZXJnZXMgb24gaXRzIG93biBvdXRwdXRzLiBQcmFjdGljYWwgcmVjaXBlcyAoUGhpLTMsIExMYU1BLTMuMSkgbWl4IDXigJMyMCUgc3ludGhldGljIGRhdGEgd2l0aCBmcmVzaCB3ZWIgY3Jhd2xzLiBSTEhGIHByZWZlcmVuY2UgZGF0YSBpcyBhbHdheXMgdHJhaW5lZCBmb3IgYSBzaW5nbGUgZXBvY2g6IGh1bWFuIGFubm90YXRpb24gaXMgZXhwZW5zaXZlLCB0aGUgZGF0YXNldCBpcyBzbWFsbCByZWxhdGl2ZSB0byBwcmV0cmFpbmluZyBjb3Jwb3JhLCBhbmQgcmVwZWF0ZWQgcGFzc2VzIGNhdXNlIHNldmVyZSBvdmVyZml0dGluZyBvbiB0aGUgcmV3YXJkIHNpZ25hbCByYXRoZXIgdGhhbiBnZW5lcmFsaXphYmxlIGh1bWFuIHByZWZlcmVuY2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlJlcGV0aXRpb25zIiwiTG9zcyBJbmNyZWFzZSB2cyAxeCIsIk1lbW9yaXphdGlvbiBSYXRlIiwiUmVjb21tZW5kZWQgTGltaXQiLCJOb3RlcyJdLCJyb3dzIjpbWyIxeCIsIjAlIChiYXNlbGluZSkiLCJ+MiUiLCJBbHdheXMgc2FmZSIsIkNoaW5jaGlsbGEtb3B0aW1hbCByZWdpbWUiXSxbIjJ4IiwifjHigJMyJSIsIn414oCTOCUiLCJBbGwgc291cmNlIHR5cGVzIiwiTmVnbGlnaWJsZSBxdWFsaXR5IGltcGFjdCJdLFsiNHgiLCJ+NSUiLCJ+MTUlIiwiQm9va3MgYW5kIGNvZGUgb25seSIsIkRlZXBNaW5kIHRocmVzaG9sZDsgYXZvaWQgZm9yIHdlYiB0ZXh0Il0sWyI4eCIsIn4xMOKAkzEyJSIsIn4zMCUiLCJDb2RlIG9ubHkiLCJTaWduaWZpY2FudCBtZW1vcml6YXRpb247IGF2b2lkIGZvciBib29rcyBhbmQgd2ViIl0sWyIxNngiLCJ+MTglIiwifjUwJSIsIk5vdCByZWNvbW1lbmRlZCIsIlN0cm9uZyBtZW1vcml6YXRpb24gYXJ0aWZhY3RzLCB2aXNpYmxlIHF1YWxpdHkgZHJvcCJdLFsiMzJ4IiwifjIwJSsiLCJcdTAwM2U2MCUiLCJOZXZlciIsIkRlZXBNaW5kIHVwcGVyIGJvdW5kOyBzZXZlcmUgZGVncmFkYXRpb24iXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiVGhlIDR4IFJlcGV0aXRpb24gVGhyZXNob2xkIiwiY29udGVudCI6IkJleW9uZCA0eCByZXBldGl0aW9uIG9mIHRoZSBzYW1lIGRvY3VtZW50cywgTExNcyBzaG93IHNpZ25pZmljYW50IG1lbW9yaXphdGlvbiBhcnRpZmFjdHMgYW5kIGRvd25zdHJlYW0gcXVhbGl0eSBkZWdyYWRhdGlvbiDigJQgaWYgeW91IGV4aGF1c3QgeW91ciBkYXRhIGJ1ZGdldCwgaW52ZXN0IGluIG5ldyBkYXRhIGNvbGxlY3Rpb24gcmF0aGVyIHRoYW4gYWRkaXRpb25hbCByZXBldGl0aW9uIGVwb2Nocy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Multi-Epoch Training for LLMs — Data Repetition Effects and Degradation

Modern large language models are trained on trillions of tokens — LLaMA-3.1-8B on 15 trillion, for example — yet the total unique web data available falls well short of that threshold. The result is inevitable: some documents are seen multiple times during training. Understanding how repetition affects model quality, memorization, and downstream performance is essential for anyone designing a pretraining data pipeline. The Chinchilla paper established that for a compute-optimal model, training on roughly 1 epoch is ideal; but inference-optimized models intentionally overtrain past that point, surfacing the multi-epoch problem at scale.

## Chinchilla Scaling and the Single-Epoch Assumption

Hoffmann et al. (2022) showed that compute-optimal training balances model parameters N and training tokens D as D ≈ 20N: a 70B model trained on 1.4T tokens, roughly one pass over a large Common Crawl snapshot. The implicit assumption is a single pass over the data. Inference-optimized models — LLaMA-3.1, Mistral, Gemma — deliberately violate this by overtraining on 15–30T tokens with smaller parameter counts, producing cheaper-to-serve models that still perform well. The tradeoff is data repetition: any 1T-token source in a 15T-token run appears roughly 15 times if not diversified with fresh crawl data.

## Data Repetition Effects — DeepMind Research

DeepMind's research into multi-epoch training (Hernandez et al. 2022, Muennighoff et al. 2023) produced quantitative baselines: repeating the training corpus 4 times causes approximately 5% validation loss increase versus a single-epoch baseline; 32 repetitions causes approximately 20% loss increase. The degradation is non-linear — the first repetition adds almost no cost, the fourth adds a noticeable amount, and each subsequent doubling adds proportionally more. Muennighoff et al. also observed a double descent analog: after enough repetition, loss initially worsens, briefly improves as the model memorizes, then worsens again as memorization dominates generalization.

```python
import random
from typing import List, Iterator
from torch.utils.data import IterableDataset

class MultiEpochDataset(IterableDataset):
    """Shuffle documents across epochs; track per-document repetition count."""
    def __init__(self, documents: List, max_epochs: int = 4, seed: int = 42):
        self.documents = documents
        self.max_epochs = max_epochs
        self.rng = random.Random(seed)
        self.epoch_counts = [0] * len(documents)

    def __iter__(self) -> Iterator:
        for epoch in range(self.max_epochs):
            indices = list(range(len(self.documents)))
            self.rng.shuffle(indices)          # different order each epoch
            for idx in indices:
                self.epoch_counts[idx] += 1
                yield {"tokens": self.documents[idx], "epoch": epoch,
                       "doc_id": idx, "repetition_count": self.epoch_counts[idx]}

# 1,000 documents x 4 epochs -- no document exceeds 4x repetition
docs = [list(range(512)) for _ in range(1_000)]
dataset = MultiEpochDataset(docs, max_epochs=4)
total = sum(1 for _ in dataset)
print(f"Total samples: {total}, max repetitions: {max(dataset.epoch_counts)}")
assert max(dataset.epoch_counts) == 4, "Repetition limit violated"
print("All documents stay within the 4x repetition limit")
```

## Measuring Degradation Empirically

Degradation from data repetition is measured by training identical model architectures on 1x, 2x, 4x, and 8x repetitions of the same fixed dataset, then evaluating on a held-out set that was never repeated. The key is ensuring held-out data comes from the same distribution but is completely disjoint from training — otherwise the measurement conflates distribution shift with repetition effects. The metric is absolute validation loss and the percentage increase relative to the 1x baseline. Perplexity is less useful here because it grows exponentially with loss, amplifying small absolute changes.

```python
import random
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

def measure_repetition_degradation(token_corpus, rep_counts, seq_len=64, steps=300):
    """Train a tiny LM on corpus repeated N times; return eval loss per rep count."""
    vocab_size = max(token_corpus) + 1
    results = {}
    for reps in rep_counts:
        tokens = token_corpus * reps
        random.shuffle(tokens)
        seqs = [tokens[i:i+seq_len+1] for i in range(0, len(tokens)-seq_len, seq_len)]
        xs   = torch.tensor([s[:-1] for s in seqs])
        ys   = torch.tensor([s[1:]  for s in seqs])
        loader = DataLoader(TensorDataset(xs, ys), batch_size=64, shuffle=True)
        model  = nn.Sequential(nn.Embedding(vocab_size, 64), nn.Linear(64, vocab_size))
        opt    = torch.optim.Adam(model.parameters(), lr=3e-4)
        for step, (x, y) in zip(range(steps), loader):
            emb  = model[0](x).mean(1)
            loss = nn.functional.cross_entropy(model[1](emb), y[:, seq_len // 2])
            opt.zero_grad(); loss.backward(); opt.step()
        results[reps] = loss.item()
    return results

corpus = list(range(500)) * 200    # 100K token corpus
losses = measure_repetition_degradation(corpus, rep_counts=[1, 2, 4, 8])
base   = losses[1]
for r, l in losses.items():
    print(f"  {r}x: loss={l:.4f}  (+{(l - base) / base * 100:.1f}% vs 1x)")
```

## Domain-Specific Repetition Strategies

Not all data domains degrade equally with repetition. Repeated code data shows less loss degradation than repeated web text, possibly because code has more structured, learnable patterns with lower entropy. Books tolerate moderate repetition (3–4x) because signal density is high and redundancy is low. Web crawl text — the largest and noisiest source — should be kept at 1x wherever possible. The practical solution is a domain-weighted mixing schedule: assign per-domain epoch budgets that reflect each domain's repetition tolerance rather than repeating the entire corpus uniformly.

```python
import random
from typing import Dict, List

def build_mixed_dataset(domain_corpora: Dict[str, List], domain_epochs: Dict[str, int],
                        seed: int = 42) -> List:
    """Mix domain corpora with different repetition counts into one training set."""
    rng = random.Random(seed)
    mixed = []
    for domain, corpus in domain_corpora.items():
        epochs = domain_epochs.get(domain, 1)
        repeated = corpus * epochs
        rng.shuffle(repeated)
        mixed.extend(repeated)
        print(f"  {domain:10s}: {len(corpus):>8,} docs x {epochs}ep = {len(repeated):>8,} samples")
    rng.shuffle(mixed)    # global shuffle across all domains
    return mixed

# LLaMA-3.1-style domain mixing: high-quality sources get more repetitions
DOMAIN_CORPORA = {
    "books":  [f"book_doc_{i}"  for i in range(50_000)],
    "code":   [f"code_doc_{i}"  for i in range(80_000)],
    "web":    [f"web_doc_{i}"   for i in range(500_000)],
}
DOMAIN_EPOCHS = {"books": 4, "code": 2, "web": 1}  # stay below 4x for books
mixed = build_mixed_dataset(DOMAIN_CORPORA, DOMAIN_EPOCHS)
print(f"Total training samples: {len(mixed):,}")
```

## Model Memorization and Privacy Risk

Carlini et al. (2021, 2023) demonstrated that LLMs memorize training data verbatim in measurable ways, and that memorization rate scales with repetition count. A document appearing once is rarely extractable via prefix completion; a document appearing 100 times is often recoverable with a short prefix. Beyond quality degradation, memorization carries privacy and legal risk: PII in repeated documents, copyright text, or proprietary code can be extracted by adversaries. Measuring extraction rate — the fraction of training documents recoverable via greedy decoding given a 50-token prefix — is the standard empirical proxy for memorization.

```python
import torch
from typing import List

def compute_extraction_rate(model, tokenizer, train_docs: List[str],
                            prefix_len: int = 50, gen_len: int = 50,
                            match_threshold: float = 0.7) -> float:
    """Estimate fraction of training docs recoverable via greedy prefix completion."""
    extracted = 0
    for doc in train_docs:
        ids = tokenizer(doc, return_tensors="pt", truncation=True, max_length=200).input_ids
        prefix = ids[:, :prefix_len]
        suffix = ids[:, prefix_len:prefix_len + gen_len]
        with torch.no_grad():
            gen = model.generate(prefix, max_new_tokens=gen_len, do_sample=False)
        gen_suffix = gen[:, prefix_len:]
        min_len = min(gen_suffix.shape[1], suffix.shape[1])
        match = (gen_suffix[:, :min_len] == suffix[:, :min_len]).float().mean().item()
        extracted += int(match >= match_threshold)
    return extracted / len(train_docs)

# Synthetic proxy: memorization rate grows with repetition count
print("Repetition | Extraction Rate | Memorization Risk")
print("-" * 48)
for reps, rate in [(1, 0.02), (2, 0.06), (4, 0.15), (8, 0.31), (16, 0.52)]:
    risk = "Low" if rate < 0.1 else ("Medium" if rate < 0.3 else "High")
    print(f"   {reps:>2}x    |     {rate:.0%}          | {risk}")
```

## Mitigation Strategies

When the data budget is exhausted and additional repetition becomes necessary, several strategies reduce quality degradation. Data augmentation — back-translation, paraphrase models, sentence reordering — creates semantically similar but token-distinct variants that provide fresh signal. Mixing fresh web crawl snapshots with high-quality repeated sources dilutes the effective repetition rate. Curriculum learning, presenting less-repeated data later in training when the model is more capable, can help, though evidence for language models specifically is mixed. Deduplication is the complementary defense: aggressive MinHash or exact-match deduplication before training removes implicit repetition from near-duplicate web pages.

- Back-translation: translate documents to a second language and back to produce near-duplicate but token-distinct training examples.
- Paraphrase augmentation: use a separately trained paraphrase model to rewrite documents before each repetition epoch.
- Crawl diversification: mix fresh CommonCrawl snapshots from different months rather than repeating the same snapshot.
- Synthetic data insertion: use the model itself or a smaller teacher to generate text on training topics, injecting it as pseudo-fresh data.
- Domain epoch budgeting: assign per-source repetition limits rather than repeating the entire corpus uniformly.
- Pre-training deduplication: apply MinHash LSH or exact-match deduplication to remove near-duplicate web pages before any repetition counting.

## Synthetic Data and RLHF Considerations

Model-generated synthetic data serves as pseudo-fresh training signal: it has never appeared in the training set exactly as written, so it does not count as a repetition of existing documents. The risk is mode collapse — if synthetic data dominates, the model converges on its own outputs. Practical recipes (Phi-3, LLaMA-3.1) mix 5–20% synthetic data with fresh web crawls. RLHF preference data is always trained for a single epoch: human annotation is expensive, the dataset is small relative to pretraining corpora, and repeated passes cause severe overfitting on the reward signal rather than generalizable human preference.

| Repetitions | Loss Increase vs 1x | Memorization Rate | Recommended Limit | Notes |
| --- | --- | --- | --- | --- |
| 1x | 0% (baseline) | ~2% | Always safe | Chinchilla-optimal regime |
| 2x | ~1–2% | ~5–8% | All source types | Negligible quality impact |
| 4x | ~5% | ~15% | Books and code only | DeepMind threshold; avoid for web text |
| 8x | ~10–12% | ~30% | Code only | Significant memorization; avoid for books and web |
| 16x | ~18% | ~50% | Not recommended | Strong memorization artifacts, visible quality drop |
| 32x | ~20%+ | >60% | Never | DeepMind upper bound; severe degradation |

> **The 4x Repetition Threshold**: Beyond 4x repetition of the same documents, LLMs show significant memorization artifacts and downstream quality degradation — if you exhaust your data budget, invest in new data collection rather than additional repetition epochs.

---

