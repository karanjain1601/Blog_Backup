---
title: "3D Gaussian Splatting: Real-Time Novel View Synthesis"
slug: "3d-gaussian-splatting"
description: ""
tags: ["computer-vision", "3d-gaussian-splatting", "novel-view-synthesis", "real-time-rendering", "rasterization"]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiIzRCBHYXVzc2lhbiBTcGxhdHRpbmcgKDNER1MpIHJlcHJlc2VudHMgYSBzY2VuZSBhcyBhIGNvbGxlY3Rpb24gb2YgM0QgR2F1c3NpYW5zIOKAlCBlbGxpcHNvaWRhbCBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb25zIGluIHNwYWNlIOKAlCBlYWNoIHdpdGggcG9zaXRpb24sIGNvdmFyaWFuY2UsIG9wYWNpdHksIGFuZCB2aWV3LWRlcGVuZGVudCBjb2xvdXIgZW5jb2RlZCBhcyBzcGhlcmljYWwgaGFybW9uaWNzLiBOb3ZlbCB2aWV3cyBhcmUgcmVuZGVyZWQgYnkgcHJvamVjdGluZyBhbGwgR2F1c3NpYW5zIG9udG8gdGhlIGltYWdlIHBsYW5lIGFuZCBhbHBoYS1ibGVuZGluZyB0aGVtIGZyb250LXRvLWJhY2sgaW4gYSBzaW5nbGUgZmFzdCBHUFUgcmFzdGVyaXphdGlvbiBwYXNzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiM0RHUyB3YXMgaW50cm9kdWNlZCBieSBLZXJibCBldCBhbC4gKFNJR0dSQVBIIDIwMjMpIGFuZCBkZW1vbnN0cmF0ZWQgcmVhbC10aW1lIG5vdmVsIHZpZXcgc3ludGhlc2lzIGF0IDEwMCsgRlBTIG9uIGNvbW1vZGl0eSBHUFVzLCBtYXRjaGluZyBOZVJGIHF1YWxpdHkgd2hpbGUgYmVpbmcgb3JkZXJzIG9mIG1hZ25pdHVkZSBmYXN0ZXIgYXQgcmVuZGVyaW5nLiBUaGUgbWV0aG9kIGluaXRpYWxpc2VzIEdhdXNzaWFucyBmcm9tIGEgc3BhcnNlIFNmTSBwb2ludCBjbG91ZCwgdGhlbiBqb2ludGx5IG9wdGltaXNlcyBhbGwgR2F1c3NpYW4gYXR0cmlidXRlcyB2aWEgZGlmZmVyZW50aWFibGUgdGlsZS1iYXNlZCByYXN0ZXJpemF0aW9uIGFuZCBhZGFwdGl2ZSBkZW5zaXR5IGNvbnRyb2wuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiM0QgR2F1c3NpYW4gUmVwcmVzZW50YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVhY2ggR2F1c3NpYW4gaXMgZGVmaW5lZCBieSBhIG1lYW4gzrwg4oiIIFLCsyBhbmQgY292YXJpYW5jZSDOoyA9IFJTU15UIFJeVCwgd2hlcmUgUiBpcyBhIHJvdGF0aW9uIG1hdHJpeCAocGFyYW1ldGVyaXNlZCBhcyBhIHVuaXQgcXVhdGVybmlvbiBmb3IgZ3JhZGllbnQgc3RhYmlsaXR5KSBhbmQgUyBpcyBhIGRpYWdvbmFsIHNjYWxlIG1hdHJpeC4gU3RvcmluZyByb3RhdGlvbiBhcyBhIHF1YXRlcm5pb24gKDQgZmxvYXRzKSBlbnN1cmVzIHRoZSBjb3ZhcmlhbmNlIHN0YXlzIHBvc2l0aXZlIHNlbWktZGVmaW5pdGUgZHVyaW5nIGdyYWRpZW50IHVwZGF0ZXMg4oCUIGRpcmVjdCBvcHRpbWlzYXRpb24gb2YgdGhlIDPDlzMgbWF0cml4IGRvZXMgbm90IGd1YXJhbnRlZSB0aGlzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuY2xhc3MgR2F1c3NpYW4zRDpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbik6XG4gICAgICAgIHNlbGYueHl6ICAgICA9IHRvcmNoLnplcm9zKG4sIDMpICAgICAgIyBwb3NpdGlvblxuICAgICAgICBzZWxmLnJvdCAgICAgPSB0b3JjaC56ZXJvcyhuLCA0KSAgICAgICMgcXVhdGVybmlvblxuICAgICAgICBzZWxmLnNjYWxlICAgPSB0b3JjaC56ZXJvcyhuLCAzKSAgICAgICMgbG9nLXNjYWxlXG4gICAgICAgIHNlbGYub3BhY2l0eSA9IHRvcmNoLnplcm9zKG4sIDEpICAgICAgIyBwcmUtc2lnbW9pZFxuICAgICAgICBzZWxmLnNoICAgICAgPSB0b3JjaC56ZXJvcyhuLCAxNiwgMykgIyBTSCBjb2VmZmljaWVudHNcbiAgICAjIFRvdGFsOiAzKzQrMysxKzQ4ID0gNTkgZmxvYXRzIHBlciBHYXVzc2lhbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29sb3VyIGlzIGVuY29kZWQgYXMgZGVncmVlLTMgc3BoZXJpY2FsIGhhcm1vbmljIGNvZWZmaWNpZW50cyDigJQgMTYgcGVyIFJHQiBjaGFubmVsICg0OCBmbG9hdHMgdG90YWwpIOKAlCBjYXB0dXJpbmcgdmlldy1kZXBlbmRlbnQgYXBwZWFyYW5jZSBsaWtlIHNwZWN1bGFyIGhpZ2hsaWdodHMuIER1cmluZyByZW5kZXJpbmcsIFNIIGNvZWZmaWNpZW50cyBhcmUgZXZhbHVhdGVkIGF0IHRoZSBjdXJyZW50IHZpZXdpbmcgZGlyZWN0aW9uIHRvIG9idGFpbiB0aGUgR2F1c3NpYW5cdTAwMjdzIGNvbG91ciBmcm9tIHRoYXQgdmlld3BvaW50LCBlbmFibGluZyB0aGUgc2FtZSBsaWdodGluZyBlZmZlY3RzIHRoYXQgTmVSRlx1MDAyN3Mgdmlldy1jb25kaXRpb25lZCBNTFAgb3V0cHV0IGFsc28gbW9kZWxzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpZmZlcmVudGlhYmxlIFJhc3Rlcml6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJhc3Rlcml6YXRpb24gcmVwbGFjZXMgTmVSRlx1MDAyN3MgcmF5IG1hcmNoaW5nLiBFYWNoIEdhdXNzaWFuIGlzIHByb2plY3RlZCBmcm9tIDNEIHRvIDJEIHVzaW5nIHZpZXcgYW5kIHByb2plY3Rpb24gbWF0cmljZXMuIFRoZSBwcm9qZWN0ZWQgMkQgR2F1c3NpYW4gaXMgc3BsYXR0ZWQgb250byBhIDE2w5cxNiBwaXhlbCB0aWxlIGdyaWQuIEdhdXNzaWFucyBhcmUgc29ydGVkIGJ5IGRlcHRoIHBlciB0aWxlIHVzaW5nIGEgZmFzdCBwYXJhbGxlbCByYWRpeCBzb3J0IG9uIHRoZSBHUFUsIGVuYWJsaW5nIGNvcnJlY3QgZnJvbnQtdG8tYmFjayBhbHBoYSBjb21wb3NpdGluZyB3aXRob3V0IHBlci1yYXkgc2VxdWVudGlhbCBzYW1wbGluZyBsb29wcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZGVmIHByb2plY3RfZ2F1c3NpYW4obWVhbjNkLCBjb3YzZCwgdmlld19tYXQsIHByb2pfbWF0KTpcbiAgICAjIEphY29iaWFuIG9mIHBlcnNwZWN0aXZlIHByb2plY3Rpb24gYXQgcG9pbnQgdFxuICAgIHQgPSB2aWV3X21hdCBAIG1lYW4zZFxuICAgIEogPSBmb2NhbF9qYWNvYmlhbih0LCBmeCwgZnkpXG4gICAgVyA9IHZpZXdfbWF0WzozLCA6M11cbiAgICBjb3YyZCA9IEogQCBXIEAgY292M2QgQCBXLlQgQCBKLlRcbiAgICBtZWFuMmQgPSBwcm9qX21hdCBAIG1lYW4zZFxuICAgIGRlcHRoICA9IHRbMl0gICAgICAgICAgICAgICAjIGZvciBkZXB0aC1zb3J0XG4gICAgcmV0dXJuIG1lYW4yZFs6Ml0sIGNvdjJkWzoyLCA6Ml0sIGRlcHRoIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiByZW5kZXJfcGl4ZWwoZ2F1c3NpYW5zXzJkLCBwaXhlbCk6XG4gICAgYWNjdW1fYWxwaGEsIGNvbG9yID0gMC4wLCB0b3JjaC56ZXJvcygzKVxuICAgIGZvciBnIGluIGdhdXNzaWFuc18yZDogICAgICAjIGZyb250LXRvLWJhY2sgb3JkZXJcbiAgICAgICAgZCA9IHBpeGVsIC0gZy5tdV8yZFxuICAgICAgICBlID0gLTAuNSAqIGQgQCBnLmNvdjJkX2ludiBAIGRcbiAgICAgICAgYSA9IGcub3BhY2l0eSAqIHRvcmNoLmV4cChlKVxuICAgICAgICBjb2xvciArPSAoMSAtIGFjY3VtX2FscGhhKSAqIGEgKiBnLmNvbG9yXG4gICAgICAgIGFjY3VtX2FscGhhICs9ICgxIC0gYWNjdW1fYWxwaGEpICogYVxuICAgICAgICBpZiBhY2N1bV9hbHBoYSBcdTAwM2UgMC45OTk5OlxuICAgICAgICAgICAgYnJlYWtcbiAgICByZXR1cm4gY29sb3IifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjdXN0b20gQ1VEQSB0aWxlLWJhc2VkIHJhc3Rlcml6ZXIgaXMgdGhlIGtleSBwZXJmb3JtYW5jZSBlbmFibGVyLiBJdCBwcm9jZXNzZXMgYWxsIHBpeGVscyBpbiBhIHRpbGUgc2ltdWx0YW5lb3VzbHksIGF2b2lkaW5nIHBlci1yYXkgc2FtcGxpbmcuIFRoZSBmb3J3YXJkIHBhc3MgaXMgZnVsbHkgZGlmZmVyZW50aWFibGUgc28gZ3JhZGllbnRzIGZsb3cgYmFjayBmcm9tIHRoZSBwaG90b21ldHJpYyBsb3NzIChMMSArIEQtU1NJTSkgdG8gYWxsIEdhdXNzaWFuIGF0dHJpYnV0ZXMgc2ltdWx0YW5lb3VzbHkuIFRoaXMgdGlsZS1iYXNlZCBkZXNpZ24gc2NhbGVzIHRvIG1pbGxpb25zIG9mIEdhdXNzaWFucyBhdCBjb25zaXN0ZW50bHkgaW50ZXJhY3RpdmUgZnJhbWUgcmF0ZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhaW5pbmcgd2l0aCBTZk0gSW5pdGlhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRyYWluaW5nIHN0YXJ0cyBmcm9tIGEgc3BhcnNlIHBvaW50IGNsb3VkIHByb2R1Y2VkIGJ5IENPTE1BUCAoU3RydWN0dXJlLWZyb20tTW90aW9uKS4gRWFjaCBwb2ludCBiZWNvbWVzIGFuIGluaXRpYWwgR2F1c3NpYW4gd2l0aCBzbWFsbCBpc290cm9waWMgY292YXJpYW5jZS4gVGhlIHNjZW5lIGlzIG9wdGltaXNlZCBvdmVyIHRob3VzYW5kcyBvZiBpdGVyYXRpb25zIG9uIG11bHRpLXZpZXcgaW1hZ2VzIHVzaW5nIEwxIHBob3RvbWV0cmljIGxvc3MgY29tYmluZWQgd2l0aCBELVNTSU0gc3RydWN0dXJhbCBzaW1pbGFyaXR5LCB3aXRoIEFkYW0gYXMgdGhlIG9wdGltaXNlciBhbmQgc2VwYXJhdGUgbGVhcm5pbmcgcmF0ZXMgcGVyIGF0dHJpYnV0ZSB0eXBlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJkZWYgYWRhcHRpdmVfZGVuc2l0eV9jb250cm9sKGdhdXNzaWFucywgc3RlcCk6XG4gICAgZ3JhZHMgPSBnYXVzc2lhbnMueHl6LmdyYWQubm9ybShkaW09LTEpXG4gICAgYmlnID0gZ2F1c3NpYW5zLnNjYWxlLm1heCgtMSkudmFsdWVzXG4gICAgIyBDbG9uZSB1bmRlci1yZWNvbnN0cnVjdGVkIHNtYWxsIEdhdXNzaWFuc1xuICAgIG1hc2tfY2xvbmUgPSAoZ3JhZHMgXHUwMDNlIHRhdV9kZW5zaWZ5KSBcdTAwMjYgKGJpZyBcdTAwM2Mgc2l6ZV90aHJlc2gpXG4gICAgY2xvbmVfZ2F1c3NpYW5zKGdhdXNzaWFucywgbWFza19jbG9uZSlcbiAgICAjIFNwbGl0IG92ZXItcmVjb25zdHJ1Y3RlZCBsYXJnZSBHYXVzc2lhbnMgaW50byAyXG4gICAgbWFza19zcGxpdCA9IChncmFkcyBcdTAwM2UgdGF1X2RlbnNpZnkpIFx1MDAyNiAoYmlnIFx1MDAzZT0gc2l6ZV90aHJlc2gpXG4gICAgc3BsaXRfZ2F1c3NpYW5zKGdhdXNzaWFucywgbWFza19zcGxpdClcbiAgICBpZiBzdGVwICUgMTAwID09IDA6XG4gICAgICAgIHBydW5lX2dhdXNzaWFucyhnYXVzc2lhbnMsIG9wYWNpdHlfdGhyZXNoPTAuMDA1KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWZ0ZXIgZGVuc2lmaWNhdGlvbiBzdGFiaWxpc2VzIGFyb3VuZCAxNWsgaXRlcmF0aW9ucywgM0RHUyBjb252ZXJnZXMgaW4gMzDigJM2MCBtaW51dGVzIG9uIGEgc2luZ2xlIEExMDAuIE9wYWNpdHkgcmVndWxhcmlzYXRpb24g4oCUIHBlcmlvZGljIHJlc2V0dGluZyBvZiBvcGFjaXRpZXMgZm9sbG93ZWQgYnkgcHJ1bmluZyBiZWxvdyBhIHRocmVzaG9sZCDigJQgcHJldmVudHMgR2F1c3NpYW4gY291bnQgZnJvbSBleHBsb2RpbmcuIEEgdHlwaWNhbCBvdXRkb29yIHNjZW5lIGVuZHMgd2l0aCAx4oCTNiBtaWxsaW9uIEdhdXNzaWFucyBvY2N1cHlpbmcgMjAw4oCTODAwIE1CIG9mIEdQVSBtZW1vcnkgZGVwZW5kaW5nIG9uIHNjZW5lIGNvbXBsZXhpdHkgYW5kIGNhcHR1cmUgZGVuc2l0eS4ifSx7InR5cGUiOiJjYWxsb3V0IiwiY2FsbG91dF90eXBlIjoidGlwIiwiY29udGVudCI6IjNER1MgYWNoaWV2ZXMgcmVhbC10aW1lIHJlbmRlcmluZyAoXHUwMDNlMTAwIEZQUykgYnkgcmVwbGFjaW5nIHJheSBtYXJjaGluZyB3aXRoIHJhc3Rlcml6YXRpb24uIFRoZSBrZXkgdHJpY2s6IHNvcnQgR2F1c3NpYW5zIGJ5IGRlcHRoIG9uY2UgcGVyIGZyYW1lIGFuZCBhbHBoYS1ibGVuZCBmcm9udC10by1iYWNrIOKAlCB0aGlzIGlzIEdQVS1mcmllbmRseSBhbmQgYXZvaWRzIHRoZSBwZXItcmF5IHNhbXBsaW5nIGJvdHRsZW5lY2sgb2YgTmVSRi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIHRvIE5lUkYifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjb3JlIHRyYWRlLW9mZjogTmVSRiBpcyBpbXBsaWNpdCBhbmQgY29tcGFjdCAoTUxQIHdlaWdodHMgfjUgTUIpIGJ1dCBzbG93IHRvIHJlbmRlcjsgM0RHUyBpcyBleHBsaWNpdCBhbmQgbGFyZ2UgKGh1bmRyZWRzIG9mIE1CKSBidXQgcmVhbC10aW1lLiBOZVJGIHJlbmRlcnMgdmlhIHNlcXVlbnRpYWwgTUxQIHF1ZXJpZXMgYWxvbmcgcmF5cywgd2hpY2ggaXMgR1BVLXVuZnJpZW5kbHkuIDNER1MgcmVuZGVycyB2aWEgdGlsZS1iYXNlZCByYXN0ZXJpemF0aW9uLCB3aGljaCBtYXBzIG5hdHVyYWxseSB0byBHUFUgcGFyYWxsZWxpc20gYW5kIGZ1bGx5IHNhdHVyYXRlcyB0ZW5zb3IgY29yZSB0aHJvdWdocHV0IG9uIG1vZGVybiBoYXJkd2FyZS4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiUmVwcmVzZW50YXRpb24iLCJUcmFpbiB0aW1lIiwiUmVuZGVyIEZQUyIsIlBTTlIgKE5lUkYtU3luKSIsIk1lbW9yeSJdLCJyb3dzIjpbWyJOZVJGIiwiTUxQIiwiMeKAkzIgZGF5cyIsIlx1MDAzYzEiLCIzMS4wIiwifjUgTUIiXSxbIkluc3RhbnQtTkdQIiwiSGFzaCBncmlkICsgTUxQIiwiM+KAkzUgbWluIiwiMTDigJMzMCIsIjMzLjIiLCJ+NTAgTUIiXSxbIlRlbnNvUkYiLCJWZWN0b3ItbWF0cml4IGZhY3RvcnMiLCIxMOKAkzMwIG1pbiIsIjXigJMyMCIsIjMzLjEiLCJ+NzAgTUIiXSxbIjNER1MiLCIzRCBHYXVzc2lhbnMiLCIzMOKAkzYwIG1pbiIsIjEwMOKAkzE1MCIsIjMzLjMiLCIyMDDigJM4MDAgTUIiXSxbIjRER1MiLCJEZWZvcm1hYmxlIEdhdXNzaWFucyIsIjHigJMyIGhycyIsIjMw4oCTNjAiLCIzMi4wIiwiNDAwKyBNQiJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiIzREdTIHN0cnVnZ2xlcyB3aGVyZSBOZVJGIGV4Y2VsczogdW5ib3VuZGVkIG91dGRvb3Igc2NlbmVzLCB2ZXJ5IHRoaW4gc3RydWN0dXJlcywgYW5kIHNtb290aCB0cmFuc3BhcmVudCBzdXJmYWNlcy4gVGhlIEdhdXNzaWFuIHByaW1pdGl2ZSBwb29ybHkgYXBwcm94aW1hdGVzIGZpbmUgZmlsYW1lbnRzIGxpa2UgdHJlZSBicmFuY2hlcyBhbmQgd2lyZSBmZW5jZXMuIDRER1MgYW5kIERlZm9ybWFibGUtM0RHUyBleHRlbmQgdGhlIG1ldGhvZCB0byBkeW5hbWljIHNjZW5lcyBieSBhZGRpbmcgYSBkZWZvcm1hdGlvbiBmaWVsZCB0aGF0IG1vdmVzIGFuZCByZXNoYXBlcyBHYXVzc2lhbnMgb3ZlciB0aW1lIGdpdmVuIGEgcGVyLWZyYW1lIGxhdGVudCBjb2RlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQm90aCBtZXRob2RzIHJlcXVpcmUgcG9zZWQgaW5wdXQgaW1hZ2VzIGZyb20gQ09MTUFQIG9yIGtub3duIGNhbWVyYSBwYXJhbWV0ZXJzLiAzREdTIGFkZGl0aW9uYWxseSBkZXBlbmRzIG9uIGEgcmVhc29uYWJsZSBTZk0gaW5pdGlhbGlzYXRpb24g4oCUIHNjZW5lcyB3aXRoIGluc3VmZmljaWVudCBDT0xNQVAgY292ZXJhZ2UgcHJvZHVjZSBmbG9hdGVycyBhbmQgYXJ0ZWZhY3RzIGluIHVuZGVyLXNhbXBsZWQgcmVnaW9ucy4gR2F1c3NpYW4gT3BhY2l0eSBGaWVsZHMgYW5kIDJEIEdhdXNzaWFuIFNwbGF0dGluZyBpbXByb3ZlIHN1cmZhY2UgcmVjb25zdHJ1Y3Rpb24gcXVhbGl0eSBieSBhZGRpbmcgZ2VvbWV0cmljIHJlZ3VsYXJpc2F0aW9uIHRlcm1zIHRvIHRoZSB0cmFpbmluZyBvYmplY3RpdmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiM0RHUyBpcyBub3cgdGhlIGRvbWluYW50IG1ldGhvZCBmb3Igbm92ZWwgdmlldyBzeW50aGVzaXMgaW4gcHJvZHVjdGlvbiBzZXR0aW5ncywgdXNlZCBpbiB0ZWxlcHJlc2VuY2UsIGdhbWUgYXNzZXQgY3JlYXRpb24sIGFuZCBWUiBjb250ZW50IHBpcGVsaW5lcy4gSXRzIHJlbmRlcmluZyBzcGVlZCBhZHZhbnRhZ2Ugb3ZlciBOZVJGIGlzIGRlY2lzaXZlIGZvciByZWFsLXRpbWUgYXBwbGljYXRpb25zLiBUaGUgbWFpbiBsaW1pdGF0aW9uIGlzIHNjZW5lIHJlcHJlc2VudGF0aW9uIHNpemUsIHdoaWNoIHJlc3RyaWN0cyBpbi1tZW1vcnkgc2NlbmUgY29tcGxleGl0eSBmb3IgbGFyZ2Utc2NhbGUgb3V0ZG9vciBvciBjaXR5LWxldmVsIGVudmlyb25tZW50cy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzdWNjZXNzIG9mIDNER1Mgc3BhcmtlZCBhIHdhdmUgb2YgZXh0ZW5zaW9uczogbGFuZ3VhZ2UtZW1iZWRkZWQgR2F1c3NpYW5zIGZvciBvcGVuLXZvY2FidWxhcnkgc2VnbWVudGF0aW9uIChMYW5nU3BsYXQpLCBnZW5lcmF0aXZlIEdhdXNzaWFuIG1vZGVscyBmb3IgdGV4dC10by0zRCAoRHJlYW1HYXVzc2lhbiksIGhpZXJhcmNoaWNhbCBHYXVzc2lhbnMgZm9yIGNpdHktc2NhbGUgc2NlbmVzLCBhbmQgcGh5c2ljcy1iYXNlZCBHYXVzc2lhbiBzaW11bGF0b3JzLiBUaGUgZXhwbGljaXQsIGRpZmZlcmVudGlhYmxlIG5hdHVyZSBvZiBHYXVzc2lhbnMgbWFrZXMgdGhlbSBjb21wb3NhYmxlIGFuZCBlZGl0YWJsZSBpbiB3YXlzIHRoYXQgaW1wbGljaXQgTmVSRnMgZnVuZGFtZW50YWxseSBhcmUgbm90LiJ9XQ=="
---
# 3D Gaussian Splatting: Real-Time Novel View Synthesis

## Overview

3D Gaussian Splatting (3DGS) represents a scene as a collection of 3D Gaussians — ellipsoidal probability distributions in space — each with position, covariance, opacity, and view-dependent colour encoded as spherical harmonics. Novel views are rendered by projecting all Gaussians onto the image plane and alpha-blending them front-to-back in a single fast GPU rasterization pass.

3DGS was introduced by Kerbl et al. (SIGGRAPH 2023) and demonstrated real-time novel view synthesis at 100+ FPS on commodity GPUs, matching NeRF quality while being orders of magnitude faster at rendering. The method initialises Gaussians from a sparse SfM point cloud, then jointly optimises all Gaussian attributes via differentiable tile-based rasterization and adaptive density control.

## 3D Gaussian Representation

Each Gaussian is defined by a mean μ ∈ R³ and covariance Σ = RSS^T R^T, where R is a rotation matrix (parameterised as a unit quaternion for gradient stability) and S is a diagonal scale matrix. Storing rotation as a quaternion (4 floats) ensures the covariance stays positive semi-definite during gradient updates — direct optimisation of the 3×3 matrix does not guarantee this.

```python
import torch

class Gaussian3D:
    def __init__(self, n):
        self.xyz     = torch.zeros(n, 3)      # position
        self.rot     = torch.zeros(n, 4)      # quaternion
        self.scale   = torch.zeros(n, 3)      # log-scale
        self.opacity = torch.zeros(n, 1)      # pre-sigmoid
        self.sh      = torch.zeros(n, 16, 3) # SH coefficients
    # Total: 3+4+3+1+48 = 59 floats per Gaussian
```

Colour is encoded as degree-3 spherical harmonic coefficients — 16 per RGB channel (48 floats total) — capturing view-dependent appearance like specular highlights. During rendering, SH coefficients are evaluated at the current viewing direction to obtain the Gaussian's colour from that viewpoint, enabling the same lighting effects that NeRF's view-conditioned MLP output also models.

## Differentiable Rasterization

Rasterization replaces NeRF's ray marching. Each Gaussian is projected from 3D to 2D using view and projection matrices. The projected 2D Gaussian is splatted onto a 16×16 pixel tile grid. Gaussians are sorted by depth per tile using a fast parallel radix sort on the GPU, enabling correct front-to-back alpha compositing without per-ray sequential sampling loops.

```python
def project_gaussian(mean3d, cov3d, view_mat, proj_mat):
    # Jacobian of perspective projection at point t
    t = view_mat @ mean3d
    J = focal_jacobian(t, fx, fy)
    W = view_mat[:3, :3]
    cov2d = J @ W @ cov3d @ W.T @ J.T
    mean2d = proj_mat @ mean3d
    depth  = t[2]               # for depth-sort
    return mean2d[:2], cov2d[:2, :2], depth
```

```python
def render_pixel(gaussians_2d, pixel):
    accum_alpha, color = 0.0, torch.zeros(3)
    for g in gaussians_2d:      # front-to-back order
        d = pixel - g.mu_2d
        e = -0.5 * d @ g.cov2d_inv @ d
        a = g.opacity * torch.exp(e)
        color += (1 - accum_alpha) * a * g.color
        accum_alpha += (1 - accum_alpha) * a
        if accum_alpha > 0.9999:
            break
    return color
```

The custom CUDA tile-based rasterizer is the key performance enabler. It processes all pixels in a tile simultaneously, avoiding per-ray sampling. The forward pass is fully differentiable so gradients flow back from the photometric loss (L1 + D-SSIM) to all Gaussian attributes simultaneously. This tile-based design scales to millions of Gaussians at consistently interactive frame rates.

## Training with SfM Initialization

Training starts from a sparse point cloud produced by COLMAP (Structure-from-Motion). Each point becomes an initial Gaussian with small isotropic covariance. The scene is optimised over thousands of iterations on multi-view images using L1 photometric loss combined with D-SSIM structural similarity, with Adam as the optimiser and separate learning rates per attribute type.

```python
def adaptive_density_control(gaussians, step):
    grads = gaussians.xyz.grad.norm(dim=-1)
    big = gaussians.scale.max(-1).values
    # Clone under-reconstructed small Gaussians
    mask_clone = (grads > tau_densify) & (big < size_thresh)
    clone_gaussians(gaussians, mask_clone)
    # Split over-reconstructed large Gaussians into 2
    mask_split = (grads > tau_densify) & (big >= size_thresh)
    split_gaussians(gaussians, mask_split)
    if step % 100 == 0:
        prune_gaussians(gaussians, opacity_thresh=0.005)
```

After densification stabilises around 15k iterations, 3DGS converges in 30–60 minutes on a single A100. Opacity regularisation — periodic resetting of opacities followed by pruning below a threshold — prevents Gaussian count from exploding. A typical outdoor scene ends with 1–6 million Gaussians occupying 200–800 MB of GPU memory depending on scene complexity and capture density.

> ****: 3DGS achieves real-time rendering (>100 FPS) by replacing ray marching with rasterization. The key trick: sort Gaussians by depth once per frame and alpha-blend front-to-back — this is GPU-friendly and avoids the per-ray sampling bottleneck of NeRF.

## Comparison to NeRF

The core trade-off: NeRF is implicit and compact (MLP weights ~5 MB) but slow to render; 3DGS is explicit and large (hundreds of MB) but real-time. NeRF renders via sequential MLP queries along rays, which is GPU-unfriendly. 3DGS renders via tile-based rasterization, which maps naturally to GPU parallelism and fully saturates tensor core throughput on modern hardware.

| Method | Representation | Train time | Render FPS | PSNR (NeRF-Syn) | Memory |
| --- | --- | --- | --- | --- | --- |
| NeRF | MLP | 1–2 days | <1 | 31.0 | ~5 MB |
| Instant-NGP | Hash grid + MLP | 3–5 min | 10–30 | 33.2 | ~50 MB |
| TensoRF | Vector-matrix factors | 10–30 min | 5–20 | 33.1 | ~70 MB |
| 3DGS | 3D Gaussians | 30–60 min | 100–150 | 33.3 | 200–800 MB |
| 4DGS | Deformable Gaussians | 1–2 hrs | 30–60 | 32.0 | 400+ MB |

3DGS struggles where NeRF excels: unbounded outdoor scenes, very thin structures, and smooth transparent surfaces. The Gaussian primitive poorly approximates fine filaments like tree branches and wire fences. 4DGS and Deformable-3DGS extend the method to dynamic scenes by adding a deformation field that moves and reshapes Gaussians over time given a per-frame latent code.

Both methods require posed input images from COLMAP or known camera parameters. 3DGS additionally depends on a reasonable SfM initialisation — scenes with insufficient COLMAP coverage produce floaters and artefacts in under-sampled regions. Gaussian Opacity Fields and 2D Gaussian Splatting improve surface reconstruction quality by adding geometric regularisation terms to the training objective.

## Key Takeaways

3DGS is now the dominant method for novel view synthesis in production settings, used in telepresence, game asset creation, and VR content pipelines. Its rendering speed advantage over NeRF is decisive for real-time applications. The main limitation is scene representation size, which restricts in-memory scene complexity for large-scale outdoor or city-level environments.

The success of 3DGS sparked a wave of extensions: language-embedded Gaussians for open-vocabulary segmentation (LangSplat), generative Gaussian models for text-to-3D (DreamGaussian), hierarchical Gaussians for city-scale scenes, and physics-based Gaussian simulators. The explicit, differentiable nature of Gaussians makes them composable and editable in ways that implicit NeRFs fundamentally are not.

