---
title: "Task Arithmetic — Adding and Negating Fine-Tuned Weight Deltas"
slug: "task-arithmetic"
description: "Task vectors encode task-specific knowledge as the weight difference between a fine-tuned and pretrained model. Covers task vector addition for multi-task capability, scaling with lambda, negation for capability removal, analogy operations, and orthogonality analysis explaining low interference."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGFzayBhcml0aG1ldGljIChJbGhhcmNvIGV0IGFsLiwgMjAyMykgZGVmaW5lcyBhIHRhc2sgdmVjdG9yIM+EID0gzrhfZmluZS10dW5lZCDiiJIgzrhfcHJldHJhaW5lZDogdGhlIGVsZW1lbnQtd2lzZSBkaWZmZXJlbmNlIGJldHdlZW4gYSB0YXNrLXNwZWNpZmljIGZpbmUtdHVuZWQgbW9kZWwgYW5kIHRoZSBvcmlnaW5hbCBwcmV0cmFpbmVkIGNoZWNrcG9pbnQuIFRoZXNlIHZlY3RvcnMgbGl2ZSBpbiB0aGUgc2FtZSB3ZWlnaHQgc3BhY2UgYXMgdGhlIG1vZGVsIHBhcmFtZXRlcnMgYW5kIGNhbiBiZSBjb21iaW5lZCBhbGdlYnJhaWNhbGx5LiBBZGRpbmcgYSB0YXNrIHZlY3RvciB0byB0aGUgcHJldHJhaW5lZCBtb2RlbCByZWNvdmVycyAoYXBwcm94aW1hdGVseSkgdGhlIGZpbmUtdHVuZWQgbW9kZWw7IGFkZGluZyBtdWx0aXBsZSB0YXNrIHZlY3RvcnMgZW5kb3dzIHRoZSBwcmV0cmFpbmVkIG1vZGVsIHdpdGggbXVsdGlwbGUgY2FwYWJpbGl0aWVzIHNpbXVsdGFuZW91c2x5OyBuZWdhdGluZyBhIHRhc2sgdmVjdG9yIHJlZHVjZXMgdGhhdCBjYXBhYmlsaXR5LiBUaGUgc3VycHJpc2luZyBmaW5kaW5nIGlzIHRoYXQgdGhlc2Ugb3BlcmF0aW9ucyBjb21wb3NlIG1vcmUgY2xlYW5seSB0aGFuIGV4cGVjdGVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRhc2sgVmVjdG9ycyDigJQgRGVmaW5pdGlvbiBhbmQgRXh0cmFjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgcHJldHJhaW5lZCBtb2RlbCB3aXRoIHBhcmFtZXRlcnMgzrjigoAsIGFuZCBhIG1vZGVsIGZpbmUtdHVuZWQgb24gdGFzayBUIHdpdGggcGFyYW1ldGVycyDOuF9ULCB0aGUgdGFzayB2ZWN0b3IgaXMgz4RfVCA9IM64X1Qg4oiSIM644oKALiBUaGlzIGlzIGEgdmVjdG9yIG9mIHRoZSBzYW1lIGRpbWVuc2lvbmFsaXR5IGFzIHRoZSBtb2RlbDogaWYgdGhlIG1vZGVsIGhhcyA3QiBwYXJhbWV0ZXJzLCBlYWNoIHRhc2sgdmVjdG9yIGhhcyA3QiBlbGVtZW50cy4gVGFzayB2ZWN0b3JzIGFyZSBkZW5zZSAobm90IHNwYXJzZSkgb3ZlciBhbGwgcGFyYW1ldGVyIGdyb3VwcyDigJQgZW5jb2RlciBsYXllcnMsIGF0dGVudGlvbiBwcm9qZWN0aW9ucywgRkZOIHdlaWdodHMsIGFuZCBsYXllciBub3JtcyBhbGwgYWNjdW11bGF0ZSB0YXNrLXNwZWNpZmljIGRlbHRhcyBkdXJpbmcgZmluZS10dW5pbmcuIFRoZSBtYWduaXR1ZGUgb2YgdGhlIHRhc2sgdmVjdG9yICjigJbPhF9U4oCWKSByZWZsZWN0cyB0aGUgdG90YWwgZHJpZnQgZnJvbSBwcmV0cmFpbmVkIHRvIGZpbmUtdHVuZWQgd2VpZ2h0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBPcmRlcmVkRGljdFxuXG5kZWYgZXh0cmFjdF90YXNrX3ZlY3RvcnMoYmFzZV9zdGF0ZV9kaWN0LCBmaW5ldHVuZWRfc3RhdGVfZGljdHMsIG5hbWVzPU5vbmUpOlxuICAgIFwiXCJcIkNvbXB1dGUgdGF1X2kgPSB0aGV0YV9mdF9pIC0gdGhldGFfYmFzZSBmb3IgZWFjaCBmaW5lLXR1bmVkIG1vZGVsLlwiXCJcIlxuICAgIHRhc2tfdmVjdG9ycyA9IFtdXG4gICAgZm9yIGksIGZ0X3NkIGluIGVudW1lcmF0ZShmaW5ldHVuZWRfc3RhdGVfZGljdHMpOlxuICAgICAgICB0YXUgPSBPcmRlcmVkRGljdCgpXG4gICAgICAgIGZvciBrZXkgaW4gYmFzZV9zdGF0ZV9kaWN0OlxuICAgICAgICAgICAgdGF1W2tleV0gPSBmdF9zZFtrZXldLmZsb2F0KCkgLSBiYXNlX3N0YXRlX2RpY3Rba2V5XS5mbG9hdCgpXG4gICAgICAgIHRhc2tfdmVjdG9ycy5hcHBlbmQodGF1KVxuICAgIHJldHVybiB0YXNrX3ZlY3RvcnNcblxuZGVmIHRhc2tfdmVjdG9yX3N0YXRzKHRhc2tfdmVjdG9ycywgbmFtZXM9Tm9uZSk6XG4gICAgZm9yIGksIHR2IGluIGVudW1lcmF0ZSh0YXNrX3ZlY3RvcnMpOlxuICAgICAgICBuYW1lID0gbmFtZXNbaV0gaWYgbmFtZXMgZWxzZSBmXCJUYXNrIHtpKzF9XCJcbiAgICAgICAgdG90YWxfbm9ybSA9IHN1bSh2Lm5vcm0oKS5pdGVtKCkgZm9yIHYgaW4gdHYudmFsdWVzKCkpXG4gICAgICAgIG1heF9kZWx0YSA9IG1heCh2LmFicygpLm1heCgpLml0ZW0oKSBmb3IgdiBpbiB0di52YWx1ZXMoKSlcbiAgICAgICAgcHJpbnQoZlwie25hbWV9OiB0b3RhbF9ub3JtPXt0b3RhbF9ub3JtOi40Zn0sIG1heF9kZWx0YT17bWF4X2RlbHRhOi40Zn0sIGxheWVycz17bGVuKHR2KX1cIilcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5iYXNlID0ge1wiZW5jLndcIjogdG9yY2guemVyb3MoOCwgOCksIFwiaGVhZC53XCI6IHRvcmNoLnplcm9zKDQsIDgpfVxuZnRfZGljdHMgPSBbXG4gICAge1wiZW5jLndcIjogYmFzZVtcImVuYy53XCJdICsgdG9yY2gucmFuZG4oOCw4KSowLjE1LCBcImhlYWQud1wiOiBiYXNlW1wiaGVhZC53XCJdICsgdG9yY2gucmFuZG4oNCw4KSowLjJ9LFxuICAgIHtcImVuYy53XCI6IGJhc2VbXCJlbmMud1wiXSArIHRvcmNoLnJhbmRuKDgsOCkqMC4xMiwgXCJoZWFkLndcIjogYmFzZVtcImhlYWQud1wiXSArIHRvcmNoLnJhbmRuKDQsOCkqMC4xOH0sXG4gICAge1wiZW5jLndcIjogYmFzZVtcImVuYy53XCJdICsgdG9yY2gucmFuZG4oOCw4KSowLjEwLCBcImhlYWQud1wiOiBiYXNlW1wiaGVhZC53XCJdICsgdG9yY2gucmFuZG4oNCw4KSowLjIyfSxcbl1cbnR2cyA9IGV4dHJhY3RfdGFza192ZWN0b3JzKGJhc2UsIGZ0X2RpY3RzKVxudGFza192ZWN0b3Jfc3RhdHModHZzLCBuYW1lcz1bXCJTZW50aW1lbnRcIiwgXCJORVJcIiwgXCJRQVwiXSlcbnByaW50KFwiVGFzayB2ZWN0b3JzOiBlYWNoIGVuY29kZXMgdGFzayBkcmlmdCBmcm9tIHRoZSBzaGFyZWQgcHJldHJhaW5lZCBiYXNlLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRhc2sgVmVjdG9yIEFkZGl0aW9uIOKAlCBNdWx0aS1UYXNrIENvbXBvc2l0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZGRpbmcgdGFzayB2ZWN0b3JzIGNvbWJpbmVzIGNhcGFiaWxpdGllczogzrhfbXVsdGkgPSDOuOKCgCArIM674oKBz4TigoEgKyDOu+KCgs+E4oKCICsgLi4uICsgzrtfbs+EX24uIFRoZSBzY2FsYXIgzrsgY29udHJvbHMgaG93IHN0cm9uZ2x5IGVhY2ggdGFzayBpcyBpbmNvcnBvcmF0ZWQuIEF0IM67PTAgdGhlIGJhc2UgbW9kZWwgaXMgdW5jaGFuZ2VkOyBhdCDOuz0xIHRoZSBmdWxsIHRhc2sgdmVjdG9yIGlzIGFwcGxpZWQ7IGF0IM67XHUwMDNlMSB0aGUgdGFzayBpcyBleHRyYXBvbGF0ZWQgYmV5b25kIHRoZSBmaW5lLXR1bmVkIG9wdGltdW0uIEluIHByYWN0aWNlLCDOuyBpbiBbMC41LCAxLjBdIHdvcmtzIHdlbGwgZm9yIG1vc3QgdGFza3M7IHZhbHVlcyBhYm92ZSAxLjUgb2Z0ZW4gb3ZlcnNob290IGFuZCBkZWdyYWRlIGdlbmVyYWwgY2FwYWJpbGl0aWVzLiBUaGUga2V5IGluc2lnaHQgZnJvbSBJbGhhcmNvIGV0IGFsLiBpcyB0aGF0IHRhc2sgdmVjdG9ycyBmb3Igc2VtYW50aWNhbGx5IGRpc3RpbmN0IE5MUCB0YXNrcyAoc2VudGltZW50LCBORVIsIFFBKSBhcmUgYXBwcm94aW1hdGVseSBvcnRob2dvbmFsLCBzbyB0aGVpciBzdW0gaGFzIGxvdyBpbnRlcmZlcmVuY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgT3JkZXJlZERpY3RcblxuZGVmIGFwcGx5X3Rhc2tfYXJpdGhtZXRpYyhiYXNlX3NkLCB0YXNrX3ZlY3RvcnMsIGxhbWJkYXMpOlxuICAgIFwiXCJcIkFwcGx5IHRhc2sgYXJpdGhtZXRpYzogdGhldGEgPSB0aGV0YV9iYXNlICsgc3VtKGxhbWJkYV9pICogdGF1X2kpLlwiXCJcIlxuICAgIGFzc2VydCBsZW4odGFza192ZWN0b3JzKSA9PSBsZW4obGFtYmRhcylcbiAgICBtZXJnZWQgPSBPcmRlcmVkRGljdCgpXG4gICAgZm9yIGtleSBpbiBiYXNlX3NkOlxuICAgICAgICBkZWx0YSA9IHN1bShsYW0gKiB0dltrZXldLmZsb2F0KCkgZm9yIGxhbSwgdHYgaW4gemlwKGxhbWJkYXMsIHRhc2tfdmVjdG9ycykpXG4gICAgICAgIG1lcmdlZFtrZXldID0gYmFzZV9zZFtrZXldLmZsb2F0KCkgKyBkZWx0YVxuICAgIHJldHVybiBtZXJnZWRcblxuZGVmIHRhc2tfYmVuY2htYXJrKG1vZGVsX3NkLCB0YXNrX25hbWUsIG1ldHJpY19mbik6XG4gICAgc2NvcmUgPSBtZXRyaWNfZm4obW9kZWxfc2QpXG4gICAgcHJpbnQoZlwiICBbe3Rhc2tfbmFtZX1dOiB7c2NvcmU6LjRmfVwiKVxuICAgIHJldHVybiBzY29yZVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuYmFzZSA9IHtcIndcIjogdG9yY2guemVyb3MoNil9XG50YXVfY29kZSA9IHtcIndcIjogdG9yY2gudGVuc29yKFswLjUsIDAuMywgLTAuMSwgMC4yLCAwLjQsIDAuMV0pfVxudGF1X21hdGggPSB7XCJ3XCI6IHRvcmNoLnRlbnNvcihbMC4yLCAtMC4xLCAwLjYsIDAuMywgLTAuMiwgMC40XSl9XG5cbnByaW50KFwiU3dlZXBpbmcgbGFtYmRhIGZvciBzaW5nbGUtdGFzayBhZGRpdGlvbjpcIilcbmZvciBsYW0gaW4gWzAuMCwgMC4yNSwgMC41LCAxLjAsIDEuNV06XG4gICAgcmVzdWx0ID0gYXBwbHlfdGFza19hcml0aG1ldGljKGJhc2UsIFt0YXVfY29kZV0sIFtsYW1dKVxuICAgIHByaW50KGZcIiAgbGFtYmRhPXtsYW19OiB3PXtbcm91bmQodiwzKSBmb3IgdiBpbiByZXN1bHRbXHUwMDI3d1x1MDAyN10udG9saXN0KCldfVwiKVxuXG5wcmludChcIlxcbk11bHRpLXRhc2sgYWRkaXRpb24gKGxhbWJkYT0xLjAgZm9yIGJvdGgpOlwiKVxubXVsdGkgPSBhcHBseV90YXNrX2FyaXRobWV0aWMoYmFzZSwgW3RhdV9jb2RlLCB0YXVfbWF0aF0sIFsxLjAsIDEuMF0pXG5wcmludChmXCIgIGNvbWJpbmVkIHc9e1tyb3VuZCh2LDMpIGZvciB2IGluIG11bHRpW1x1MDAyN3dcdTAwMjddLnRvbGlzdCgpXX1cIilcbnByaW50KFwiU3VtIG9mIG9ydGhvZ29uYWwgdGFzayB2ZWN0b3JzIGNvbXBvc2VzIHdpdGggbG93IGludGVyZmVyZW5jZS5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsaW5nIGFuZCBFeHRyYXBvbGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2NhbGFyIM67IGlzIGEgY29udGludW91cyBrbm9iIG92ZXIgdGFzayBzdHJlbmd0aC4gQXQgzrs9MCwgdGhlIG1vZGVsIGlzIHRoZSBwcmV0cmFpbmVkIGJhc2UuIEF0IM67PTEsIHRoZSBtb2RlbCBlcXVhbHMgdGhlIGZpbmUtdHVuZWQgY2hlY2twb2ludCAoaW4gdGhlIHdlaWdodC1zcGFjZSBhcHByb3hpbWF0aW9uKS4gQXQgzrtcdTAwM2UxLCB0aGUgdGFzayBpcyBleHRyYXBvbGF0ZWQ6IHRoZSBtb2RlbCBpcyBwdXNoZWQgZnVydGhlciBhbG9uZyB0aGUgZGlyZWN0aW9uIG9mIHRoZSB0YXNrIHZlY3RvciB0aGFuIHRoZSBmaW5lLXR1bmVkIG1vZGVsIGl0c2VsZiByZWFjaGVkLiBFeHRyYXBvbGF0aW9uICjOu1x1MDAzZTEpIHNvbWV0aW1lcyB5aWVsZHMgYmV0dGVyIHBlcmZvcm1hbmNlIG9uIGluLWRpc3RyaWJ1dGlvbiB0YXNrcyB0aGFuIHRoZSBmaW5lLXR1bmVkIG1vZGVsLCBiZWNhdXNlIGl0IGFtcGxpZmllcyB0aGUgdGFzay1zcGVjaWZpYyBkaXJlY3Rpb24gd2hpbGUgc3VwcHJlc3NpbmcgZ2VuZXJhbGlzdCBmZWF0dXJlcy4gSG93ZXZlciwgZXh0cmFwb2xhdGlvbiBkZWdyYWRlcyByb2J1c3RuZXNzIG9uIG91dC1vZi1kaXN0cmlidXRpb24gaW5wdXRzIGFuZCBpcyBzZW5zaXRpdmUgdG8gzrsuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTmVnYXRpb24g4oCUIFVubGVhcm5pbmcgYSBDYXBhYmlsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdWJ0cmFjdGluZyBhIHRhc2sgdmVjdG9yIHJlbW92ZXMgdGhlIGNvcnJlc3BvbmRpbmcgY2FwYWJpbGl0eTogzrhfbmVnYXRlZCA9IM644oKAIOKIkiDOuyDCtyDPhF9oYXJtZnVsLiBUaGlzIGlzIHVzZWZ1bCBmb3IgYWxpZ25tZW50OiBpZiBhIG1vZGVsIGhhcyBhIGhhcm1mdWwgY2FwYWJpbGl0eSAoZS5nLiwgcHJvZHVjaW5nIHRveGljIHRleHQpLCB5b3UgY2FuIGZpbmUtdHVuZSBhIHNtYWxsIGRhdGFzZXQgdG8gZXh0cmFjdCB0aGUgaGFybWZ1bCB0YXNrIHZlY3RvciwgdGhlbiBzdWJ0cmFjdCBpdCBmcm9tIHRoZSBhbGlnbmVkIG1vZGVsLiBUaGUgcmVzdWx0IHJlZHVjZXMgaGFybWZ1bCBvdXRwdXRzIHdpdGhvdXQgcmVxdWlyaW5nIGZ1bGwgcmV0cmFpbmluZy4gVGhlIGFudGlkb3RlIGFwcHJvYWNoIGFkZHMgYSBuZWdhdGVkIGhhcm1mdWwgdGFzayB2ZWN0b3IgdG8gYW4gYWxpZ25lZCBtb2RlbCByYXRoZXIgdGhhbiByZXRyYWluaW5nIHdpdGggZmlsdGVyZWQgZGF0YS4gSWxoYXJjbyBldCBhbC4gc2hvdyB0aGF0IG5lZ2F0aW5nIGEgdGFzayB2ZWN0b3IgZm9yIHNlbnRpbWVudCBjbGFzc2lmaWNhdGlvbiByZWR1Y2VzIGFjY3VyYWN5IG9uIHNlbnRpbWVudCBiZW5jaG1hcmtzIGJ5IDIw4oCTMzAlIHdoaWxlIGxlYXZpbmcgdW5yZWxhdGVkIHRhc2tzIGxhcmdlbHkgdW5hZmZlY3RlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBPcmRlcmVkRGljdFxuXG5kZWYgbmVnYXRlX2NhcGFiaWxpdHkoYmFzZV9zZCwgdGFza192ZWN0b3IsIHNjYWxlPTEuMCk6XG4gICAgXCJcIlwiU3VidHJhY3QgdGFzayB2ZWN0b3I6IHRoZXRhID0gdGhldGFfYmFzZSAtIHNjYWxlICogdGF1IChjYXBhYmlsaXR5IHJlbW92YWwpLlwiXCJcIlxuICAgIG5lZ2F0ZWQgPSBPcmRlcmVkRGljdCgpXG4gICAgZm9yIGtleSBpbiBiYXNlX3NkOlxuICAgICAgICBuZWdhdGVkW2tleV0gPSBiYXNlX3NkW2tleV0uZmxvYXQoKSAtIHNjYWxlICogdGFza192ZWN0b3Jba2V5XS5mbG9hdCgpXG4gICAgcmV0dXJuIG5lZ2F0ZWRcblxuZGVmIG1lYXN1cmVfY2FwYWJpbGl0eShtb2RlbF9zZCwgcHJvYmVfa2V5LCBwcm9iZV9kaXJlY3Rpb24pOlxuICAgIFwiXCJcIlByb3h5OiBkb3QgcHJvZHVjdCB3aXRoIHByb2JlIGRpcmVjdGlvbiBtZWFzdXJlcyB0YXNrIGFsaWdubWVudC5cIlwiXCJcbiAgICB3ID0gbW9kZWxfc2RbcHJvYmVfa2V5XS5mbG9hdCgpLmZsYXR0ZW4oKVxuICAgIHJldHVybiAodyAqIHByb2JlX2RpcmVjdGlvbikuc3VtKCkuaXRlbSgpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDcpXG5iYXNlID0ge1wid1wiOiB0b3JjaC5yYW5kbig4KX1cbnRhdV9oYXJtZnVsID0ge1wid1wiOiB0b3JjaC5yYW5kbig4KSAqIDAuNH1cbnByb2JlID0gdGF1X2hhcm1mdWxbXCJ3XCJdIC8gdGF1X2hhcm1mdWxbXCJ3XCJdLm5vcm0oKSAgIyBwcm9iZSBhbGlnbmVkIHdpdGggaGFybWZ1bCBkaXJlY3Rpb25cblxucHJpbnQoXCJDYXBhYmlsaXR5IHNjb3JlIChoaWdoZXIgPSBtb3JlIGhhcm1mdWwgYWxpZ25tZW50KTpcIilcbnByaW50KGZcIiAgQmFzZSBtb2RlbDoge21lYXN1cmVfY2FwYWJpbGl0eShiYXNlLCBcdTAwMjd3XHUwMDI3LCBwcm9iZSk6LjRmfVwiKVxuZm9yIHNjYWxlIGluIFswLjUsIDEuMCwgMS41LCAyLjBdOlxuICAgIG5lZyA9IG5lZ2F0ZV9jYXBhYmlsaXR5KGJhc2UsIHRhdV9oYXJtZnVsLCBzY2FsZT1zY2FsZSlcbiAgICBwcmludChmXCIgIEFmdGVyIG5lZ2F0aW9uIChzY2FsZT17c2NhbGU6LjFmfSk6IHttZWFzdXJlX2NhcGFiaWxpdHkobmVnLCBcdTAwMjd3XHUwMDI3LCBwcm9iZSk6LjRmfVwiKVxucHJpbnQoXCJOZWdhdGlvbiBwcm9ncmVzc2l2ZWx5IHJlbW92ZXMgdGhlIGNhcGFiaWxpdHk7IHNjYWxlIGNvbnRyb2xzIGFnZ3Jlc3NpdmVuZXNzLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9ydGhvZ29uYWxpdHkgQW5hbHlzaXMg4oCUIFdoeSBBZGRpdGlvbiBXb3JrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGFzayBhcml0aG1ldGljIGFkZGl0aW9uIGlzIGludGVyZmVyZW5jZS1mcmVlIHdoZW4gdGFzayB2ZWN0b3JzIGFyZSBvcnRob2dvbmFsOiBpZiDPhF9BIMK3IM+EX0IgPSAwLCB0aGVuIOKAls+EX0EgKyDPhF9C4oCWwrIgPSDigJbPhF9B4oCWwrIgKyDigJbPhF9C4oCWwrIuIEluIHByYWN0aWNlLCB0YXNrIHZlY3RvcnMgZm9yIE5MUCB0YXNrcyB3aXRoIGRpZmZlcmVudCBsYWJlbCBzcGFjZXMgKHNlbnRpbWVudCB2cyBORVIgdnMgUUEpIGhhdmUgcGFpcndpc2UgY29zaW5lIHNpbWlsYXJpdGllcyBiZWxvdyAwLjEg4oCUIG5lYXJseSBvcnRob2dvbmFsLiBUaGlzIG5lYXItb3J0aG9nb25hbGl0eSBicmVha3MgZG93biBmb3Igc2VtYW50aWNhbGx5IHJlbGF0ZWQgdGFza3MgKGUuZy4sIHR3byBkaWZmZXJlbnQgc2VudGltZW50IGRhdGFzZXRzKSB3aGVyZSB2ZWN0b3JzIGFsaWduIHN0cm9uZ2x5LiBNZWFzdXJpbmcgcGFpcndpc2UgY29zaW5lIHNpbWlsYXJpdGllcyBiZWZvcmUgbWVyZ2luZyBpcyBhIGdvb2QgZGlhZ25vc3RpYzogaGlnaCBzaW1pbGFyaXR5IChcdTAwM2UwLjMpIHByZWRpY3RzIGxvdyBpbnRlcmZlcmVuY2U7IGxvdyBzaW1pbGFyaXR5IChcdTAwM2MwLjEpIHByZWRpY3RzIGVmZmVjdGl2ZSBjb21wb3NpdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBjb3NpbmVfc2ltaWxhcml0eV9tYXRyaXgodGFza192ZWN0b3JzLCBuYW1lcz1Ob25lKTpcbiAgICBcIlwiXCJDb21wdXRlIHBhaXJ3aXNlIGNvc2luZSBzaW1pbGFyaXR5IGJldHdlZW4gZmxhdHRlbmVkIHRhc2sgdmVjdG9ycy5cIlwiXCJcbiAgICBuID0gbGVuKHRhc2tfdmVjdG9ycylcbiAgICBmbGF0ID0gW1xuICAgICAgICB0b3JjaC5jYXQoW3YuZmxvYXQoKS5mbGF0dGVuKCkgZm9yIHYgaW4gdHYudmFsdWVzKCldKVxuICAgICAgICBmb3IgdHYgaW4gdGFza192ZWN0b3JzXG4gICAgXVxuICAgIHNpbSA9IHRvcmNoLnplcm9zKG4sIG4pXG4gICAgZm9yIGkgaW4gcmFuZ2Uobik6XG4gICAgICAgIGZvciBqIGluIHJhbmdlKG4pOlxuICAgICAgICAgICAgc2ltW2ksIGpdID0gRi5jb3NpbmVfc2ltaWxhcml0eShmbGF0W2ldLnVuc3F1ZWV6ZSgwKSwgZmxhdFtqXS51bnNxdWVlemUoMCkpXG4gICAgaWYgbmFtZXM6XG4gICAgICAgIGhlYWRlciA9IGZcIntcdTAwMjdcdTAwMjc6XHUwMDNlMTR9XCIgKyBcIlwiLmpvaW4oZlwie25hbWU6XHUwMDNlMTR9XCIgZm9yIG5hbWUgaW4gbmFtZXMpXG4gICAgICAgIHByaW50KGhlYWRlcilcbiAgICAgICAgZm9yIGksIG5hbWUgaW4gZW51bWVyYXRlKG5hbWVzKTpcbiAgICAgICAgICAgIHJvdyA9IGZcIntuYW1lOlx1MDAzZTE0fVwiICsgXCJcIi5qb2luKGZcIntzaW1baSxqXS5pdGVtKCk6XHUwMDNlMTQuM2Z9XCIgZm9yIGogaW4gcmFuZ2UobikpXG4gICAgICAgICAgICBwcmludChyb3cpXG4gICAgb2ZmX2RpYWcgPSAoc2ltLnN1bSgpIC0gc2ltLnRyYWNlKCkpIC8gKG4gKiAobiAtIDEpKVxuICAgIHByaW50KGZcIk9mZi1kaWFnb25hbCBtZWFuIGNvc2luZSBzaW1pbGFyaXR5OiB7b2ZmX2RpYWcuaXRlbSgpOi40Zn1cIilcbiAgICByZXR1cm4gc2ltXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDk5KVxudHZzID0gW1xuICAgIHtcImVuY1wiOiB0b3JjaC5yYW5kbigzMiwgMzIpLCBcImhlYWRcIjogdG9yY2gucmFuZG4oOCwgMzIpfVxuICAgIGZvciBfIGluIHJhbmdlKDQpXG5dXG5uYW1lcyA9IFtcIlNlbnRpbWVudFwiLCBcIk5FUlwiLCBcIlFBXCIsIFwiU3VtbWFyaXphdGlvblwiXVxuc2ltID0gY29zaW5lX3NpbWlsYXJpdHlfbWF0cml4KHR2cywgbmFtZXMpXG5wcmludChcIkxvdyBvZmYtZGlhZ29uYWwgdmFsdWVzIGNvbmZpcm0gbmVhci1vcnRob2dvbmFsaXR5ID1cdTAwM2UgbG93IGFkZGl0aW9uIGludGVyZmVyZW5jZS5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW1pdGF0aW9ucyBhbmQgRXh0ZW5zaW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGFzayBhcml0aG1ldGljIGRlZ3JhZGVzIGFzIG1vcmUgdGFzayB2ZWN0b3JzIGFyZSBhZGRlZC4gV2l0aCAy4oCTMyB0YXNrcywgaW50ZXJmZXJlbmNlIGlzIHR5cGljYWxseSBiZWxvdyAyJSBhYnNvbHV0ZTsgd2l0aCA4KyB0YXNrcywgaW50ZXJmZXJlbmNlIGNhbiBleGNlZWQgMTAlLiBUaGUgZGVncmFkYXRpb24gaXMgd29yc2Ugd2hlbiB0YXNrcyBzaGFyZSBzaW1pbGFyIGZlYXR1cmVzIOKAlCBmb3IgZXhhbXBsZSwgYWRkaW5nIDUgZGlmZmVyZW50IGNvZGUgZ2VuZXJhdGlvbiB0YXNrIHZlY3RvcnMgcHJvZHVjZXMgaGlnaCBtdXR1YWwgaW50ZXJmZXJlbmNlLiBUSUVTIGFuZCBEQVJFIGV4dGVuZCB0YXNrIGFyaXRobWV0aWMgdG8gcmVkdWNlIHRoaXMgaW50ZXJmZXJlbmNlLiBUaGUgYW5hbG9neSBvcGVyYXRpb24gz4RfQSDiiJIgz4RfQiArIM+EX0MgdHJhbnNmZXJzIHRhc2sgc3RydWN0dXJlOiBpZiDPhF9BIGlzIFx1MDAyN0VuZ2xpc2jihpJGcmVuY2ggdHJhbnNsYXRpb25cdTAwMjcgYW5kIM+EX0IgaXMgXHUwMDI3RW5nbGlzaOKGklNwYW5pc2ggdHJhbnNsYXRpb25cdTAwMjcsIHRoZW4gz4RfQyA9IM+EX0Eg4oiSIM+EX0IgKyDPhF9TcGFuaXNoLXRleHQgY2FwdHVyZXMgdGhlIHRyYW5zbGF0aW9uIGRpcmVjdGlvbiB3aXRob3V0IFNwYW5pc2gtc3BlY2lmaWMgYmlhcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRhc2sgdmVjdG9ycyBhcmUgZGVuc2Ugb3ZlciBhbGwgcGFyYW1ldGVyIGdyb3VwcyDigJQgbm90IGp1c3QgTG9SQS1hZGFwdGVkIGxheWVyczsgYXBwbHkgdG8gZnVsbCBmaW5lLXR1bmVzIG9yIG1lcmdlIExvUkEgQkEgcHJvZHVjdHMgZmlyc3QuIiwiU2NhbGluZyByYW5nZTogzrsg4oiIIFswLjMsIDEuMF0gaXMgc2FmZSBmb3IgbW9zdCB0YXNrczsgzrsgXHUwMDNlIDEuNSByaXNrcyBkZWdyYWRpbmcgZ2VuZXJhbCBjYXBhYmlsaXRpZXMuIiwiT3J0aG9nb25hbGl0eSBkaWFnbm9zdGljOiBtZWFzdXJlIHBhaXJ3aXNlIGNvc2luZSBzaW1pbGFyaXRpZXMgYmVmb3JlIG1lcmdpbmc7IFx1MDAzZTAuMyBtZWFucyBoaWdoIGludGVyZmVyZW5jZSByaXNrLiIsIk5lZ2F0aW9uIHNjYWxlOiDOuz0xLjAgZm9yIGZ1bGwgY2FwYWJpbGl0eSByZW1vdmFsOyDOuz0wLjUgZm9yIHBhcnRpYWwgcmVkdWN0aW9uIHdoaWxlIHByZXNlcnZpbmcgcmVsYXRlZCBjYXBhYmlsaXRpZXMuIiwiQW5hbG9neSAoQS1CK0MpOiB0cmFuc2ZlcnMgcmVsYXRpb25hbCB0YXNrIHN0cnVjdHVyZTsgcmVxdWlyZXMgz4RfQSBhbmQgz4RfQiB0byBlbmNvZGUgdGhlIHNhbWUgdHlwZSBvZiB0cmFuc2Zvcm1hdGlvbi4iLCJFeHRlbnNpb246IFRJRVMvREFSRSBpbXByb3ZlIHVwb24gc2ltcGxlIHRhc2sgdmVjdG9yIGFkZGl0aW9uIGZvciBjcm9zcy10YXNrIG1lcmdpbmcgd2l0aCA0KyBtb2RlbHMuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRhc2sgQXJpdGhtZXRpYyBPcGVyYXRpb25zIFN1bW1hcnkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiT3BlcmF0aW9uIiwiRm9ybXVsYSIsIkVmZmVjdCIsIs67IFJhbmdlIiwiSW50ZXJmZXJlbmNlIFJpc2siLCJVc2UgQ2FzZSJdLCJyb3dzIjpbWyJBZGRpdGlvbiIsIs644oKAICsgzrvPhF9BIiwiQWRkIHRhc2sgQSBjYXBhYmlsaXR5IHRvIGJhc2UiLCIwLjXigJMxLjAiLCJMb3cgaWYgb3J0aG9nb25hbCIsIk11bHRpLXRhc2sgY29tcG9zaXRpb24iXSxbIlNjYWxpbmciLCLOuOKCgCArIM67z4RfQSAodmFyeSDOuykiLCJUdW5lIHRhc2sgc3RyZW5ndGggY29udGludW91c2x5IiwiMOKAkzEuNSIsIkxvdyIsIlRhc2sgc3RyZW5ndGggY29udHJvbCJdLFsiTmVnYXRpb24iLCLOuOKCgCDiiJIgzrvPhF9oYXJtZnVsIiwiUmVtb3ZlIG9yIHJlZHVjZSBjYXBhYmlsaXR5IiwiMC414oCTMS41IiwiTG93IChzdWJ0cmFjdGl2ZSkiLCJBbGlnbm1lbnQgLyBjYXBhYmlsaXR5IHJlbW92YWwiXSxbIk11bHRpLWFkZCIsIs644oKAICsgzqPOu+G1os+E4bWiIiwiQ29tYmluZSBOIHRhc2tzIHNpbXVsdGFuZW91c2x5IiwiMC4z4oCTMC44IGVhY2giLCJHcm93cyB3aXRoIE4iLCJVcCB0byB+NCB0YXNrcyBjbGVhbmx5Il0sWyJBbmFsb2d5IEEtQitDIiwizrjigoAgKyDPhF9BIOKIkiDPhF9CICsgz4RfQyIsIlRyYW5zZmVyIHJlbGF0aW9uYWwgc3RydWN0dXJlIiwiMS4wIGVhY2giLCJNb2RlcmF0ZSIsIkNyb3NzLWxpbmd1YWwgLyBkb21haW4gdHJhbnNmZXIiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTmVhci1PcnRob2dvbmFsaXR5IEV4cGxhaW5zIFRhc2sgQXJpdGhtZXRpY1x1MDAyN3MgTG93IEludGVyZmVyZW5jZSIsImNvbnRlbnQiOiJUYXNrIHZlY3RvcnMgZm9yIGRpZmZlcmVudCBOTFAgdGFza3MgKHNlbnRpbWVudCwgTkVSLCBRQSkgYXJlIGFwcHJveGltYXRlbHkgb3J0aG9nb25hbCAoY29zaW5lIHNpbWlsYXJpdHkgXHUwMDNjIDAuMSkg4oCUIHRoaXMgbmVhci1vcnRob2dvbmFsaXR5IGV4cGxhaW5zIHdoeSB0YXNrIGFyaXRobWV0aWMgYWRkaXRpb24gaXMgb2Z0ZW4gaW50ZXJmZXJlbmNlLWZyZWUgZm9yIHRoZSBmaXJzdCAy4oCTMyBhZGRlZCB0YXNrcywgYnV0IGRlZ3JhZGVzIGJleW9uZCB0aGF0LiBNZWFzdXJlIHBhaXJ3aXNlIGNvc2luZSBzaW1pbGFyaXRpZXMgYmVmb3JlIG1lcmdpbmc6IGlmIGFueSBwYWlyIGV4Y2VlZHMgMC4yNSwgZXhwZWN0IG1lYXN1cmFibGUgaW50ZXJmZXJlbmNlIGFuZCBwcmVmZXIgVElFUyBvciBEQVJFIGluc3RlYWQgb2Ygc2ltcGxlIHRhc2sgYXJpdGhtZXRpYyBhZGRpdGlvbi4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Task Arithmetic — Adding and Negating Fine-Tuned Weight Deltas

Task arithmetic (Ilharco et al., 2023) defines a task vector τ = θ_fine-tuned − θ_pretrained: the element-wise difference between a task-specific fine-tuned model and the original pretrained checkpoint. These vectors live in the same weight space as the model parameters and can be combined algebraically. Adding a task vector to the pretrained model recovers (approximately) the fine-tuned model; adding multiple task vectors endows the pretrained model with multiple capabilities simultaneously; negating a task vector reduces that capability. The surprising finding is that these operations compose more cleanly than expected.

## Task Vectors — Definition and Extraction

For a pretrained model with parameters θ₀, and a model fine-tuned on task T with parameters θ_T, the task vector is τ_T = θ_T − θ₀. This is a vector of the same dimensionality as the model: if the model has 7B parameters, each task vector has 7B elements. Task vectors are dense (not sparse) over all parameter groups — encoder layers, attention projections, FFN weights, and layer norms all accumulate task-specific deltas during fine-tuning. The magnitude of the task vector (‖τ_T‖) reflects the total drift from pretrained to fine-tuned weights.

```python
import torch
from collections import OrderedDict

def extract_task_vectors(base_state_dict, finetuned_state_dicts, names=None):
    """Compute tau_i = theta_ft_i - theta_base for each fine-tuned model."""
    task_vectors = []
    for i, ft_sd in enumerate(finetuned_state_dicts):
        tau = OrderedDict()
        for key in base_state_dict:
            tau[key] = ft_sd[key].float() - base_state_dict[key].float()
        task_vectors.append(tau)
    return task_vectors

def task_vector_stats(task_vectors, names=None):
    for i, tv in enumerate(task_vectors):
        name = names[i] if names else f"Task {i+1}"
        total_norm = sum(v.norm().item() for v in tv.values())
        max_delta = max(v.abs().max().item() for v in tv.values())
        print(f"{name}: total_norm={total_norm:.4f}, max_delta={max_delta:.4f}, layers={len(tv)}")

torch.manual_seed(42)
base = {"enc.w": torch.zeros(8, 8), "head.w": torch.zeros(4, 8)}
ft_dicts = [
    {"enc.w": base["enc.w"] + torch.randn(8,8)*0.15, "head.w": base["head.w"] + torch.randn(4,8)*0.2},
    {"enc.w": base["enc.w"] + torch.randn(8,8)*0.12, "head.w": base["head.w"] + torch.randn(4,8)*0.18},
    {"enc.w": base["enc.w"] + torch.randn(8,8)*0.10, "head.w": base["head.w"] + torch.randn(4,8)*0.22},
]
tvs = extract_task_vectors(base, ft_dicts)
task_vector_stats(tvs, names=["Sentiment", "NER", "QA"])
print("Task vectors: each encodes task drift from the shared pretrained base.")
```

## Task Vector Addition — Multi-Task Composition

Adding task vectors combines capabilities: θ_multi = θ₀ + λ₁τ₁ + λ₂τ₂ + ... + λ_nτ_n. The scalar λ controls how strongly each task is incorporated. At λ=0 the base model is unchanged; at λ=1 the full task vector is applied; at λ>1 the task is extrapolated beyond the fine-tuned optimum. In practice, λ in [0.5, 1.0] works well for most tasks; values above 1.5 often overshoot and degrade general capabilities. The key insight from Ilharco et al. is that task vectors for semantically distinct NLP tasks (sentiment, NER, QA) are approximately orthogonal, so their sum has low interference.

```python
import torch
from collections import OrderedDict

def apply_task_arithmetic(base_sd, task_vectors, lambdas):
    """Apply task arithmetic: theta = theta_base + sum(lambda_i * tau_i)."""
    assert len(task_vectors) == len(lambdas)
    merged = OrderedDict()
    for key in base_sd:
        delta = sum(lam * tv[key].float() for lam, tv in zip(lambdas, task_vectors))
        merged[key] = base_sd[key].float() + delta
    return merged

def task_benchmark(model_sd, task_name, metric_fn):
    score = metric_fn(model_sd)
    print(f"  [{task_name}]: {score:.4f}")
    return score

torch.manual_seed(0)
base = {"w": torch.zeros(6)}
tau_code = {"w": torch.tensor([0.5, 0.3, -0.1, 0.2, 0.4, 0.1])}
tau_math = {"w": torch.tensor([0.2, -0.1, 0.6, 0.3, -0.2, 0.4])}

print("Sweeping lambda for single-task addition:")
for lam in [0.0, 0.25, 0.5, 1.0, 1.5]:
    result = apply_task_arithmetic(base, [tau_code], [lam])
    print(f"  lambda={lam}: w={[round(v,3) for v in result['w'].tolist()]}")

print("\nMulti-task addition (lambda=1.0 for both):")
multi = apply_task_arithmetic(base, [tau_code, tau_math], [1.0, 1.0])
print(f"  combined w={[round(v,3) for v in multi['w'].tolist()]}")
print("Sum of orthogonal task vectors composes with low interference.")
```

## Scaling and Extrapolation

The scalar λ is a continuous knob over task strength. At λ=0, the model is the pretrained base. At λ=1, the model equals the fine-tuned checkpoint (in the weight-space approximation). At λ>1, the task is extrapolated: the model is pushed further along the direction of the task vector than the fine-tuned model itself reached. Extrapolation (λ>1) sometimes yields better performance on in-distribution tasks than the fine-tuned model, because it amplifies the task-specific direction while suppressing generalist features. However, extrapolation degrades robustness on out-of-distribution inputs and is sensitive to λ.

## Negation — Unlearning a Capability

Subtracting a task vector removes the corresponding capability: θ_negated = θ₀ − λ · τ_harmful. This is useful for alignment: if a model has a harmful capability (e.g., producing toxic text), you can fine-tune a small dataset to extract the harmful task vector, then subtract it from the aligned model. The result reduces harmful outputs without requiring full retraining. The antidote approach adds a negated harmful task vector to an aligned model rather than retraining with filtered data. Ilharco et al. show that negating a task vector for sentiment classification reduces accuracy on sentiment benchmarks by 20–30% while leaving unrelated tasks largely unaffected.

```python
import torch
from collections import OrderedDict

def negate_capability(base_sd, task_vector, scale=1.0):
    """Subtract task vector: theta = theta_base - scale * tau (capability removal)."""
    negated = OrderedDict()
    for key in base_sd:
        negated[key] = base_sd[key].float() - scale * task_vector[key].float()
    return negated

def measure_capability(model_sd, probe_key, probe_direction):
    """Proxy: dot product with probe direction measures task alignment."""
    w = model_sd[probe_key].float().flatten()
    return (w * probe_direction).sum().item()

torch.manual_seed(7)
base = {"w": torch.randn(8)}
tau_harmful = {"w": torch.randn(8) * 0.4}
probe = tau_harmful["w"] / tau_harmful["w"].norm()  # probe aligned with harmful direction

print("Capability score (higher = more harmful alignment):")
print(f"  Base model: {measure_capability(base, 'w', probe):.4f}")
for scale in [0.5, 1.0, 1.5, 2.0]:
    neg = negate_capability(base, tau_harmful, scale=scale)
    print(f"  After negation (scale={scale:.1f}): {measure_capability(neg, 'w', probe):.4f}")
print("Negation progressively removes the capability; scale controls aggressiveness.")
```

## Orthogonality Analysis — Why Addition Works

Task arithmetic addition is interference-free when task vectors are orthogonal: if τ_A · τ_B = 0, then ‖τ_A + τ_B‖² = ‖τ_A‖² + ‖τ_B‖². In practice, task vectors for NLP tasks with different label spaces (sentiment vs NER vs QA) have pairwise cosine similarities below 0.1 — nearly orthogonal. This near-orthogonality breaks down for semantically related tasks (e.g., two different sentiment datasets) where vectors align strongly. Measuring pairwise cosine similarities before merging is a good diagnostic: high similarity (>0.3) predicts low interference; low similarity (<0.1) predicts effective composition.

```python
import torch
import torch.nn.functional as F

def cosine_similarity_matrix(task_vectors, names=None):
    """Compute pairwise cosine similarity between flattened task vectors."""
    n = len(task_vectors)
    flat = [
        torch.cat([v.float().flatten() for v in tv.values()])
        for tv in task_vectors
    ]
    sim = torch.zeros(n, n)
    for i in range(n):
        for j in range(n):
            sim[i, j] = F.cosine_similarity(flat[i].unsqueeze(0), flat[j].unsqueeze(0))
    if names:
        header = f"{'':>14}" + "".join(f"{name:>14}" for name in names)
        print(header)
        for i, name in enumerate(names):
            row = f"{name:>14}" + "".join(f"{sim[i,j].item():>14.3f}" for j in range(n))
            print(row)
    off_diag = (sim.sum() - sim.trace()) / (n * (n - 1))
    print(f"Off-diagonal mean cosine similarity: {off_diag.item():.4f}")
    return sim

torch.manual_seed(99)
tvs = [
    {"enc": torch.randn(32, 32), "head": torch.randn(8, 32)}
    for _ in range(4)
]
names = ["Sentiment", "NER", "QA", "Summarization"]
sim = cosine_similarity_matrix(tvs, names)
print("Low off-diagonal values confirm near-orthogonality => low addition interference.")
```

## Limitations and Extensions

Task arithmetic degrades as more task vectors are added. With 2–3 tasks, interference is typically below 2% absolute; with 8+ tasks, interference can exceed 10%. The degradation is worse when tasks share similar features — for example, adding 5 different code generation task vectors produces high mutual interference. TIES and DARE extend task arithmetic to reduce this interference. The analogy operation τ_A − τ_B + τ_C transfers task structure: if τ_A is 'English→French translation' and τ_B is 'English→Spanish translation', then τ_C = τ_A − τ_B + τ_Spanish-text captures the translation direction without Spanish-specific bias.

- Task vectors are dense over all parameter groups — not just LoRA-adapted layers; apply to full fine-tunes or merge LoRA BA products first.
- Scaling range: λ ∈ [0.3, 1.0] is safe for most tasks; λ > 1.5 risks degrading general capabilities.
- Orthogonality diagnostic: measure pairwise cosine similarities before merging; >0.3 means high interference risk.
- Negation scale: λ=1.0 for full capability removal; λ=0.5 for partial reduction while preserving related capabilities.
- Analogy (A-B+C): transfers relational task structure; requires τ_A and τ_B to encode the same type of transformation.
- Extension: TIES/DARE improve upon simple task vector addition for cross-task merging with 4+ models.

## Task Arithmetic Operations Summary

| Operation | Formula | Effect | λ Range | Interference Risk | Use Case |
| --- | --- | --- | --- | --- | --- |
| Addition | θ₀ + λτ_A | Add task A capability to base | 0.5–1.0 | Low if orthogonal | Multi-task composition |
| Scaling | θ₀ + λτ_A (vary λ) | Tune task strength continuously | 0–1.5 | Low | Task strength control |
| Negation | θ₀ − λτ_harmful | Remove or reduce capability | 0.5–1.5 | Low (subtractive) | Alignment / capability removal |
| Multi-add | θ₀ + Σλᵢτᵢ | Combine N tasks simultaneously | 0.3–0.8 each | Grows with N | Up to ~4 tasks cleanly |
| Analogy A-B+C | θ₀ + τ_A − τ_B + τ_C | Transfer relational structure | 1.0 each | Moderate | Cross-lingual / domain transfer |

> **Near-Orthogonality Explains Task Arithmetic's Low Interference**: Task vectors for different NLP tasks (sentiment, NER, QA) are approximately orthogonal (cosine similarity < 0.1) — this near-orthogonality explains why task arithmetic addition is often interference-free for the first 2–3 added tasks, but degrades beyond that. Measure pairwise cosine similarities before merging: if any pair exceeds 0.25, expect measurable interference and prefer TIES or DARE instead of simple task arithmetic addition.

---

