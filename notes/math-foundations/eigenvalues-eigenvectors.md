---
title: "Eigenvalues and Eigenvectors"
slug: "eigenvalues-eigenvectors"
description: "Invariant directions of linear transformations, spectral decomposition, PCA, PageRank, and eigenvalue applications in deep learning."
tags: ["linear-algebra", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWlnZW52YWx1ZXMgYW5kIGVpZ2VudmVjdG9ycyByZXZlYWwgdGhlIGludHJpbnNpYyBnZW9tZXRyeSBvZiBhIGxpbmVhciB0cmFuc2Zvcm1hdGlvbiDigJQgdGhlIGRpcmVjdGlvbnMgdGhhdCB0aGUgdHJhbnNmb3JtYXRpb24gbWVyZWx5IHN0cmV0Y2hlcyB3aXRob3V0IHJvdGF0aW5nLCBhbmQgdGhlIGFtb3VudHMgYnkgd2hpY2ggaXQgc3RyZXRjaGVzIHRoZW0uIFRoaXMgY29uY2VwdCBhcHBlYXJzIGV2ZXJ5d2hlcmUgaW4gTUw6IFBDQSwgc3BlY3RyYWwgY2x1c3RlcmluZywgc3RhYmlsaXR5IGFuYWx5c2lzLCBQYWdlUmFuaywgYW5kIHRoZSBhbmFseXNpcyBvZiBuZXVyYWwgbmV0d29yayBkeW5hbWljcyBhbGwgcmVseSBvbiBlaWdlbmRlY29tcG9zaXRpb24uIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVmaW5pdGlvbiBhbmQgR2VvbWV0cmljIE1lYW5pbmcifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgbm9uemVybyB2ZWN0b3IgKip2KiogaXMgYW4gKiplaWdlbnZlY3RvcioqIG9mIG1hdHJpeCAqKkEqKiBpZiBtdWx0aXBseWluZyBieSAqKkEqKiBvbmx5IHNjYWxlcyBpdCwgd2l0aG91dCBjaGFuZ2luZyBpdHMgZGlyZWN0aW9uOlxuXG4gICoqQXYqKiA9IM67Kip2KipcblxuVGhlIHNjYWxhciDOuyBpcyB0aGUgY29ycmVzcG9uZGluZyAqKmVpZ2VudmFsdWUqKi4gR2VvbWV0cmljYWxseTogZWlnZW52ZWN0b3JzIGFyZSB0aGUgKmludmFyaWFudCBheGVzKiBvZiB0aGUgdHJhbnNmb3JtYXRpb24g4oCUIHRoZXkgc3BhbiB0aGUgZGlyZWN0aW9ucyB0aGF0IGFyZSBtZXJlbHkgc3RyZXRjaGVkICjOuyA+IDEpLCBjb21wcmVzc2VkICgwIDwgzrsgPCAxKSwgZmxpcHBlZCAozrsgPCAwKSwgb3IgYW5uaWhpbGF0ZWQgKM67ID0gMCkuIEZvciBhIHJvdGF0aW9uIG1hdHJpeCAoZXhjZXB0IDDCsCBvciAxODDCsCksIHRoZXJlIGFyZSBubyByZWFsIGVpZ2VudmVjdG9ycyDigJQgbm8gZGlyZWN0aW9uIGlzIHByZXNlcnZlZCBieSByb3RhdGlvbi4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgU3ltbWV0cmljIG1hdHJpeDogcmVhbCBlaWdlbnZhbHVlcyBndWFyYW50ZWVkXG5BID0gbnAuYXJyYXkoW1s0LiwgMi5dLFxuICAgICAgICAgICAgICBbMi4sIDMuXV0pXG5cbmVpZ2VudmFsdWVzLCBlaWdlbnZlY3RvcnMgPSBucC5saW5hbGcuZWlnKEEpXG5wcmludCgnRWlnZW52YWx1ZXM6JywgZWlnZW52YWx1ZXMpICAgICAgICMgWzUuLCAyLl1cbnByaW50KCdFaWdlbnZlY3RvcnMgKGNvbHVtbnMpOicpICAgICAgICAgIyBvcnRob2dvbmFsIGZvciBzeW1tZXRyaWMgQVxucHJpbnQoZWlnZW52ZWN0b3JzKVxuXG4jIFZlcmlmeTogQXYgPSBsYW1iZGEgKiB2XG5mb3IgaSBpbiByYW5nZShsZW4oZWlnZW52YWx1ZXMpKTpcbiAgICB2ID0gZWlnZW52ZWN0b3JzWzosIGldXG4gICAgbGFtID0gZWlnZW52YWx1ZXNbaV1cbiAgICBBdiA9IEEgQCB2XG4gICAgcHJpbnQoZid8fEF2IC0ge2xhbTouMWZ9dnx8ID0ge25wLmxpbmFsZy5ub3JtKEF2IC0gbGFtKnYpOi4yZX0nKSAgIyBuZWFyIHplcm8ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgQ2hhcmFjdGVyaXN0aWMgUG9seW5vbWlhbCJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG8gZmluZCBlaWdlbnZhbHVlcywgd2UgcmVhcnJhbmdlICoqQXYgPSDOu3YqKiB0byAqKihBIC0gzrtJKXYgPSAwKiouIEZvciB0aGlzIHRvIGhhdmUgYSBub256ZXJvIHNvbHV0aW9uICoqdioqLCB0aGUgbWF0cml4ICoqKEEgLSDOu0kpKiogbXVzdCBiZSBzaW5ndWxhciDigJQgaXRzIGRldGVybWluYW50IG11c3QgYmUgemVybzpcblxuICBkZXQoKipBKiogLSDOuyoqSSoqKSA9IDBcblxuRXhwYW5kaW5nIHRoaXMgZGV0ZXJtaW5hbnQgZ2l2ZXMgdGhlICoqY2hhcmFjdGVyaXN0aWMgcG9seW5vbWlhbCoqIGluIM67LCB3aXRoIGRlZ3JlZSBuIGZvciBhbiBuw5duIG1hdHJpeC4gSXRzIG4gcm9vdHMgKHBvc3NpYmx5IGNvbXBsZXgsIHBvc3NpYmx5IHJlcGVhdGVkKSBhcmUgdGhlIGVpZ2VudmFsdWVzLiBGb3IgYSAyw5cyIG1hdHJpeCBgW1thLGJdLFtjLGRdXWAsIHRoZSBjaGFyYWN0ZXJpc3RpYyBwb2x5bm9taWFsIGlzIM67wrIgLSAoYStkKc67ICsgKGFkLWJjKSA9IDAg4oCUIHRoZSBjb2VmZmljaWVudHMgaW52b2x2ZSB0aGUgdHJhY2UgKHN1bSBvZiBkaWFnb25hbCA9IHN1bSBvZiBlaWdlbnZhbHVlcykgYW5kIGRldGVybWluYW50IChwcm9kdWN0IG9mIGVpZ2VudmFsdWVzKS4ifSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlRyYWNlIGFuZCBEZXRlcm1pbmFudCBJZGVudGl0aWVzIiwiY29udGVudCI6IkZvciBhbnkgc3F1YXJlIG1hdHJpeCBBOiB0aGUgc3VtIG9mIGVpZ2VudmFsdWVzIGVxdWFscyB0aGUgdHJhY2UgKHRyKEEpID0gzqPOu+G1oiksIGFuZCB0aGUgcHJvZHVjdCBvZiBlaWdlbnZhbHVlcyBlcXVhbHMgdGhlIGRldGVybWluYW50IChkZXQoQSkgPSDOoM674bWiKS4gVGhlc2UgaG9sZCBldmVuIHdoZW4gdGhlIGZ1bGwgZWlnZW5kZWNvbXBvc2l0aW9uIGlzIGV4cGVuc2l2ZSB0byBjb21wdXRlLCBhbmQgYXJlIHVzZWZ1bCBmb3IgcXVpY2sgc2FuaXR5IGNoZWNrcyBhbmQgcmVndWxhcml6YXRpb24gYW5hbHlzaXMuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3BlY3RyYWwgRGVjb21wb3NpdGlvbiBmb3IgU3ltbWV0cmljIE1hdHJpY2VzIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgKipTcGVjdHJhbCBUaGVvcmVtKiogc3RhdGVzIHRoYXQgZXZlcnkgcmVhbCBzeW1tZXRyaWMgbWF0cml4ICoqQSA9IEHhtYAqKiBjYW4gYmUgZmFjdG9yZWQgYXM6XG5cbiAgKipBID0gUc6bUeG1gCoqXG5cbndoZXJlICoqUSoqIGlzIGFuIG9ydGhvZ29uYWwgbWF0cml4IChjb2x1bW5zIGFyZSBvcnRob25vcm1hbCBlaWdlbnZlY3RvcnMsICoqUVHhtYAgPSBJKiopIGFuZCAqKs6bKiogaXMgYSBkaWFnb25hbCBtYXRyaXggb2YgcmVhbCBlaWdlbnZhbHVlcy4gVGhpcyBkZWNvbXBvc2l0aW9uIGlzIGVub3Jtb3VzbHkgdXNlZnVsIGJlY2F1c2U6XG5cbjEuIFN5bW1ldHJpYyBtYXRyaWNlcyBhbHdheXMgaGF2ZSByZWFsIGVpZ2VudmFsdWVzIOKAlCBubyBjb21wbGV4IG51bWJlcnNcbjIuIEVpZ2VudmVjdG9ycyBmb3IgZGlzdGluY3QgZWlnZW52YWx1ZXMgYXJlIG9ydGhvZ29uYWxcbjMuIFRoZSBtYXRyaXggY2FuIGJlIHdyaXR0ZW4gYXMgYSBzdW0gb2YgcmFuay0xIHByb2plY3Rpb25zOiAqKkEgPSDOo+G1oiDOu+G1oiBx4bWiIHHhtaLhtYAqKlxuXG5Db3ZhcmlhbmNlIG1hdHJpY2VzLCBHcmFtIG1hdHJpY2VzLCBMYXBsYWNpYW4gbWF0cmljZXMsIGFuZCBIZXNzaWFucyBhcmUgYWxsIHN5bW1ldHJpYy4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgQnVpbGQgYSBzeW1tZXRyaWMgUFNEIG1hdHJpeFxubnAucmFuZG9tLnNlZWQoNDIpXG5YID0gbnAucmFuZG9tLnJhbmRuKDUsIDUpXG5BID0gWCBAIFguVCAgICMgYWx3YXlzIHN5bW1ldHJpYywgUFNEXG5cbiMgU3BlY3RyYWwgZGVjb21wb3NpdGlvblxubGFtYiwgUSA9IG5wLmxpbmFsZy5laWdoKEEpICAgIyBlaWdoOiBzeW1tZXRyaWMgLS0gc29ydGVkLCByZWFsXG5MYW1iZGEgPSBucC5kaWFnKGxhbWIpXG5cbiMgVmVyaWZ5IEEgPSBRIExhbWJkYSBRXlRcbkFfcmVjb25zdHJ1Y3RlZCA9IFEgQCBMYW1iZGEgQCBRLlRcbnByaW50KCdSZWNvbnN0cnVjdGlvbiBlcnJvcjonLCBucC5saW5hbGcubm9ybShBIC0gQV9yZWNvbnN0cnVjdGVkKSkgICMgfjFlLTE0XG5cbiMgUmFuay0xIGRlY29tcG9zaXRpb25cbkFfc3VtID0gc3VtKGxhbWJbaV0gKiBucC5vdXRlcihRWzosaV0sIFFbOixpXSkgZm9yIGkgaW4gcmFuZ2UoNSkpXG5wcmludCgnUmFuay0xIHN1bSBlcnJvcjonLCBucC5saW5hbGcubm9ybShBIC0gQV9zdW0pKSAgIyB+MWUtMTQifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQQ0EgYXMgRWlnZW5kZWNvbXBvc2l0aW9uIG9mIHRoZSBDb3ZhcmlhbmNlIE1hdHJpeCJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiKipQcmluY2lwYWwgQ29tcG9uZW50IEFuYWx5c2lzIChQQ0EpKiogZmluZHMgdGhlIGRpcmVjdGlvbnMgb2YgbWF4aW11bSB2YXJpYW5jZSBpbiBkYXRhLiBHaXZlbiBjZW50ZXJlZCBkYXRhIG1hdHJpeCAqKlgqKiAoc2hhcGUgbsOXZCksIHRoZSBjb3ZhcmlhbmNlIG1hdHJpeCBpcyAqKkMgPSAoMS9uKSBY4bWAWCoqIChzaGFwZSBkw5dkLCBzeW1tZXRyaWMgUFNEKS4gRWlnZW5kZWNvbXBvc2luZyAqKkMqKjpcblxuICAqKkMgPSBRzptR4bWAKipcblxuVGhlIGVpZ2VudmVjdG9ycyAoY29sdW1ucyBvZiAqKlEqKikgYXJlIHRoZSAqKnByaW5jaXBhbCBjb21wb25lbnRzKiog4oCUIHRoZSBvcnRob2dvbmFsIGRpcmVjdGlvbnMgb2YgdmFyaWFuY2UuIFRoZSBlaWdlbnZhbHVlcyDOu+G1oiBhcmUgdGhlIHZhcmlhbmNlIGluIGVhY2ggZGlyZWN0aW9uLiBQcm9qZWN0aW5nIGRhdGEgb250byB0aGUgdG9wLWsgZWlnZW52ZWN0b3JzIGdpdmVzIHRoZSBvcHRpbWFsIGstZGltZW5zaW9uYWwgcmVwcmVzZW50YXRpb24gdGhhdCBtaW5pbWl6ZXMgcmVjb25zdHJ1Y3Rpb24gZXJyb3IuIFRoZSBmcmFjdGlvbiBvZiB2YXJpYW5jZSBleHBsYWluZWQgYnkgdGhlIHRvcC1rIGNvbXBvbmVudHMgaXMgzqPhtaLiiaTigpYgzrvhtaIgLyDOo+G1oiDOu+G1oi4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbm5wLnJhbmRvbS5zZWVkKDApXG5uLCBkID0gMjAwLCAxMFxuWCA9IG5wLnJhbmRvbS5yYW5kbihuLCBkKVxuIyBNYWtlIGZpcnN0IDIgZGltcyBoYXZlIGhpZ2ggdmFyaWFuY2VcblhbOiwgMF0gKj0gNVxuWFs6LCAxXSAqPSAzXG5cbiMgQ2VudGVyIGFuZCBjb21wdXRlIGNvdmFyaWFuY2VcblhfYyA9IFggLSBYLm1lYW4oYXhpcz0wKVxuQyA9IChYX2MuVCBAIFhfYykgLyBuICAgIyAoZCwgZCkgY292YXJpYW5jZVxuXG4jIEVpZ2VuZGVjb21wb3NpdGlvblxubGFtYiwgUSA9IG5wLmxpbmFsZy5laWdoKEMpXG5sYW1iID0gbGFtYls6Oi0xXTsgUSA9IFFbOiwgOjotMV0gICMgc29ydCBkZXNjZW5kaW5nXG5cbiMgUHJvamVjdCB0byB0b3AtMiBQQ3NcblhfcGNhID0gWF9jIEAgUVs6LCA6Ml0gICAgICAgICAgICAgIyAobiwgMilcbnZhcl9leHBsYWluZWQgPSBsYW1iWzoyXS5zdW0oKSAvIGxhbWIuc3VtKClcbnByaW50KGYnVmFyaWFuY2UgZXhwbGFpbmVkIGJ5IHRvcCAyIFBDczoge3Zhcl9leHBsYWluZWQ6LjElfScpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUG93ZXIgSXRlcmF0aW9uIGFuZCB0aGUgRG9taW5hbnQgRWlnZW52ZWN0b3IifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBsYXJnZSBtYXRyaWNlcyB3aGVyZSBmdWxsIGVpZ2VuZGVjb21wb3NpdGlvbiBpcyB0b28gZXhwZW5zaXZlLCAqKnBvd2VyIGl0ZXJhdGlvbioqIGZpbmRzIHRoZSBsYXJnZXN0IChkb21pbmFudCkgZWlnZW52ZWN0b3IgaXRlcmF0aXZlbHk6XG5cbjEuIFN0YXJ0IHdpdGggYSByYW5kb20gdmVjdG9yICoqduKCgCoqXG4yLiBSZXBlYXRlZGx5IGNvbXB1dGUgKip2X3trKzF9ID0gQSB2X2sgLyB8fEEgdl9rfHwqKlxuMy4gQ29udmVyZ2VuY2U6IHRoZSB2ZWN0b3IgYWxpZ25zIHdpdGggdGhlIGRvbWluYW50IGVpZ2VudmVjdG9yIGF0IHJhdGUgfM674oKCL8674oKBfOG1j1xuXG5Qb3dlciBpdGVyYXRpb24gY29udmVyZ2VzIGZhc3RlciB3aGVuIHRoZSByYXRpbyBvZiB0aGUgdHdvIGxhcmdlc3QgZWlnZW52YWx1ZXMgaXMgc21hbGwgKGxhcmdlIGVpZ2VuZ2FwKS4gVGhlICoqTGFuY3pvcyBhbGdvcml0aG0qKiBpcyBhbiBlZmZpY2llbnQgZXh0ZW5zaW9uIGZvciBzeW1tZXRyaWMgbWF0cmljZXMgdGhhdCBidWlsZHMgYSBLcnlsb3Ygc3Vic3BhY2UgYW5kIGZpbmRzIG11bHRpcGxlIGVpZ2VudmVjdG9ycyB3aXRob3V0IGNvbXB1dGluZyB0aGUgZnVsbCBlaWdlbmRlY29tcG9zaXRpb24uIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWFya292IENoYWlucyBhbmQgdGhlIFN0YXRpb25hcnkgRGlzdHJpYnV0aW9uIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBICoqTWFya292IGNoYWluKiogaXMgZGVmaW5lZCBieSBhIHRyYW5zaXRpb24gbWF0cml4ICoqUCoqIHdoZXJlICoqUFtpLGpdKiogaXMgdGhlIHByb2JhYmlsaXR5IG9mIG1vdmluZyBmcm9tIHN0YXRlIGogdG8gc3RhdGUgaSAoY29sdW1uLXN0b2NoYXN0aWM6IGNvbHVtbnMgc3VtIHRvIDEpLiBUaGUgc3RhdGlvbmFyeSBkaXN0cmlidXRpb24gKirPgCoqIHNhdGlzZmllcyAqKlDPgCA9IM+AKiosIG1lYW5pbmcgKirPgCoqIGlzIGFuIGVpZ2VudmVjdG9yIG9mICoqUCoqIHdpdGggZWlnZW52YWx1ZSAxLlxuXG5CeSB0aGUgUGVycm9uLUZyb2Jlbml1cyB0aGVvcmVtLCBmb3IgaXJyZWR1Y2libGUgYXBlcmlvZGljIGNoYWlucywgdGhlIGRvbWluYW50IGVpZ2VudmFsdWUgaXMgZXhhY3RseSAxIChhbGwgb3RoZXJzIGhhdmUgfM67fCA8IDEpLiBQb3dlciBpdGVyYXRpb24gb24gKipQKiogY29ycmVzcG9uZHMgdG8gcmVwZWF0ZWRseSBtdWx0aXBseWluZyB0aGUgc3RhdGUgZGlzdHJpYnV0aW9uIGJ5ICoqUCoqIOKAlCBpdCBjb252ZXJnZXMgdG8gKirPgCoqIGJlY2F1c2UgYWxsIGNvbXBvbmVudHMgYWxvbmcgbm9uLWRvbWluYW50IGVpZ2VudmVjdG9ycyBkZWNheSBnZW9tZXRyaWNhbGx5LiBUaGlzIGlzIHRoZSBtYXRoZW1hdGljYWwgZm91bmRhdGlvbiBvZiAqKkdvb2dsZSBQYWdlUmFuayoqLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBTaW1wbGUgMy1zdGF0ZSBNYXJrb3YgY2hhaW4gKGNvbHVtbi1zdG9jaGFzdGljKVxuUCA9IG5wLmFycmF5KFtbMC43LCAwLjIsIDAuMV0sXG4gICAgICAgICAgICAgIFswLjIsIDAuNSwgMC4zXSxcbiAgICAgICAgICAgICAgWzAuMSwgMC4zLCAwLjZdXSlcblxuIyBQb3dlciBpdGVyYXRpb246IGFwcGx5IFAgcmVwZWF0ZWRseVxucGkgPSBucC5hcnJheShbMS8zLCAxLzMsIDEvM10pICAgIyBzdGFydCB1bmlmb3JtXG5mb3IgXyBpbiByYW5nZSgxMDApOlxuICAgIHBpID0gUCBAIHBpXG5wcmludCgnU3RhdGlvbmFyeSBkaXN0cmlidXRpb24gKHBvd2VyIGl0ZXIpOicsIHBpKVxuXG4jIEVpZ2VuZGVjb21wb3NpdGlvbiBhcHByb2FjaFxudmFscywgdmVjcyA9IG5wLmxpbmFsZy5laWcoUClcbmlkeCA9IG5wLmFyZ21heChucC5hYnModmFscykpXG5waV9laWcgPSBucC5hYnModmVjc1s6LCBpZHhdKVxucGlfZWlnIC89IHBpX2VpZy5zdW0oKVxucHJpbnQoJ1N0YXRpb25hcnkgZGlzdHJpYnV0aW9uIChlaWdlbnZlY3Rvcik6JywgcGlfZWlnKVxucHJpbnQoJ01hdGNoOicsIG5wLmFsbGNsb3NlKHBpLCBwaV9laWcsIGF0b2w9MWUtNikpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWlnZW52YWx1ZXMgaW4gTmV1cmFsIE5ldHdvcmsgQW5hbHlzaXMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVpZ2VudmFsdWVzIGFwcGVhciB0aHJvdWdob3V0IGRlZXAgbGVhcm5pbmcgYW5hbHlzaXM6XG5cbi0gKipMb3NzIGxhbmRzY2FwZSoqOiBUaGUgSGVzc2lhbiAqKkgqKiBvZiB0aGUgbG9zcyAoc2Vjb25kIGRlcml2YXRpdmVzKSBoYXMgZWlnZW52YWx1ZXMgdGhhdCBtZWFzdXJlIHRoZSBjdXJ2YXR1cmUgaW4gZWFjaCBkaXJlY3Rpb24uIExhcmdlIGVpZ2VudmFsdWVzIOKGkiBzaGFycCBjdXJ2YXR1cmUg4oaSIHNlbnNpdGl2ZSB0byBsZWFybmluZyByYXRlLiBUaGUgcmF0aW8gzrtfbWF4L867X21pbiAoY29uZGl0aW9uIG51bWJlcikgZGV0ZXJtaW5lcyBncmFkaWVudCBkZXNjZW50IGNvbnZlcmdlbmNlIHNwZWVkLlxuLSAqKkdyYWRpZW50IGV4cGxvc2lvbi92YW5pc2hpbmcqKjogSW4gUk5OcywgaWYgdGhlIHJlY3VycmVudCB3ZWlnaHQgbWF0cml4ICoqVyoqIGhhcyBlaWdlbnZhbHVlcyB8zrt8ID4gMSwgcmVwZWF0ZWQgbXVsdGlwbGljYXRpb24gKipX4bWXKiogZ3Jvd3MgZXhwb25lbnRpYWxseSAoZXhwbG9zaW9uKTsgaWYgfM67fCA8IDEsIGl0IHZhbmlzaGVzLiBUaGUgb3J0aG9nb25hbC91bml0YXJ5IFJOTiByZXNlYXJjaCBjb25zdHJhaW5zIGVpZ2VudmFsdWVzIHRvIHRoZSB1bml0IGNpcmNsZS5cbi0gKipTcGVjdHJhbCBub3JtYWxpemF0aW9uKio6IERpdmlkaW5nIHdlaWdodCBtYXRyaWNlcyBieSB0aGVpciBsYXJnZXN0IHNpbmd1bGFyIHZhbHVlIChvcGVyYXRvciBub3JtKSBzdGFiaWxpemVzIEdBTiB0cmFpbmluZyBieSBjb25zdHJhaW5pbmcgdGhlIExpcHNjaGl0eiBjb25zdGFudC4ifSwKICB7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXBwbGljYXRpb24iLCJNYXRyaXgiLCJFaWdlbnZhbHVlIE1lYW5pbmciXSwicm93cyI6W1siUENBIiwiQ292YXJpYW5jZSBDID0gWOG1gFgvbiIsIlZhcmlhbmNlIGluIGVhY2ggcHJpbmNpcGFsIGRpcmVjdGlvbiJdLFsiR3JhcGggTGFwbGFjaWFuIiwiTCA9IEQgLSBBIiwiTnVtYmVyIG9mIGNvbm5lY3RlZCBjb21wb25lbnRzICh6ZXJvIGVpZ2VudmFsdWVzKSJdLFsiUGFnZVJhbmsiLCJUcmFuc2l0aW9uIG1hdHJpeCBQIiwiRG9taW5hbnQgZWlnZW52ZWN0b3IgPSBwYWdlIGltcG9ydGFuY2Ugc2NvcmVzIl0sWyJSTk4gc3RhYmlsaXR5IiwiUmVjdXJyZW50IHdlaWdodCBXIiwifM67fCA+IDEg4oaSIGV4cGxvc2lvbiwgfM67fCA8IDEg4oaSIHZhbmlzaGluZyJdLFsiTG9zcyBsYW5kc2NhcGUiLCJIZXNzaWFuIEggPSDiiILCskwv4oiCzrjCsiIsIkN1cnZhdHVyZTsgY29uZGl0aW9uIG51bWJlciBhZmZlY3RzIGNvbnZlcmdlbmNlIl0sWyJHQU4gdHJhaW5pbmciLCJXZWlnaHQgbWF0cml4IFciLCJTcGVjdHJhbCBub3JtID0gTGlwc2NoaXR6IGNvbnN0YW50Il1dfSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiVXNlIGVpZ2ggZm9yIFN5bW1ldHJpYyBNYXRyaWNlcyIsImNvbnRlbnQiOiJOdW1QeSdzIG5wLmxpbmFsZy5laWdoIChub3RlIHRoZSAnaCcpIGlzIHNwZWNpZmljYWxseSBmb3IgSGVybWl0aWFuL3N5bW1ldHJpYyBtYXRyaWNlcy4gSXQgaXMgZmFzdGVyIHRoYW4gZWlnLCBndWFyYW50ZWVzIHJlYWwgZWlnZW52YWx1ZXMsIGFuZCByZXR1cm5zIHRoZW0gc29ydGVkIGluIGFzY2VuZGluZyBvcmRlci4gRm9yIGNvdmFyaWFuY2UgbWF0cmljZXMsIEdyYW0gbWF0cmljZXMsIG9yIEhlc3NpYW5zLCBhbHdheXMgdXNlIGVpZ2ggcmF0aGVyIHRoYW4gdGhlIGdlbmVyYWwgZWlnLiJ9Cl0K"
---

# Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors reveal the intrinsic geometry of a linear transformation — the directions that the transformation merely stretches without rotating, and the amounts by which it stretches them. This concept appears everywhere in ML: PCA, spectral clustering, stability analysis, PageRank, and the analysis of neural network dynamics all rely on eigendecomposition.

## Definition and Geometric Meaning

A nonzero vector **v** is an **eigenvector** of matrix **A** if multiplying by **A** only scales it, without changing its direction:

  **Av** = λ**v**

The scalar λ is the corresponding **eigenvalue**. Geometrically: eigenvectors are the *invariant axes* of the transformation — they span the directions that are merely stretched (λ > 1), compressed (0 < λ < 1), flipped (λ < 0), or annihilated (λ = 0). For a rotation matrix (except 0° or 180°), there are no real eigenvectors — no direction is preserved by rotation.

```python
import numpy as np

# Symmetric matrix: real eigenvalues guaranteed
A = np.array([[4., 2.],
              [2., 3.]])

eigenvalues, eigenvectors = np.linalg.eig(A)
print('Eigenvalues:', eigenvalues)       # [5., 2.]
print('Eigenvectors (columns):')         # orthogonal for symmetric A
print(eigenvectors)

# Verify: Av = lambda * v
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]
    Av = A @ v
    print(f'||Av - {lam:.1f}v|| = {np.linalg.norm(Av - lam*v):.2e}')  # near zero
```

## The Characteristic Polynomial

To find eigenvalues, we rearrange **Av = λv** to **(A - λI)v = 0**. For this to have a nonzero solution **v**, the matrix **(A - λI)** must be singular — its determinant must be zero:

  det(**A** - λ**I**) = 0

Expanding this determinant gives the **characteristic polynomial** in λ, with degree n for an n×n matrix. Its n roots (possibly complex, possibly repeated) are the eigenvalues. For a 2×2 matrix `[[a,b],[c,d]]`, the characteristic polynomial is λ² - (a+d)λ + (ad-bc) = 0 — the coefficients involve the trace (sum of diagonal = sum of eigenvalues) and determinant (product of eigenvalues).

> **[INFO] Trace and Determinant Identities**
>
> For any square matrix A: the sum of eigenvalues equals the trace (tr(A) = Σλᵢ), and the product of eigenvalues equals the determinant (det(A) = Πλᵢ). These hold even when the full eigendecomposition is expensive to compute, and are useful for quick sanity checks and regularization analysis.

## Spectral Decomposition for Symmetric Matrices

The **Spectral Theorem** states that every real symmetric matrix **A = Aᵀ** can be factored as:

  **A = QΛQᵀ**

where **Q** is an orthogonal matrix (columns are orthonormal eigenvectors, **QQᵀ = I**) and **Λ** is a diagonal matrix of real eigenvalues. This decomposition is enormously useful because:

1. Symmetric matrices always have real eigenvalues — no complex numbers
2. Eigenvectors for distinct eigenvalues are orthogonal
3. The matrix can be written as a sum of rank-1 projections: **A = Σᵢ λᵢ qᵢ qᵢᵀ**

Covariance matrices, Gram matrices, Laplacian matrices, and Hessians are all symmetric.

```python
import numpy as np

# Build a symmetric PSD matrix
np.random.seed(42)
X = np.random.randn(5, 5)
A = X @ X.T   # always symmetric, PSD

# Spectral decomposition
lamb, Q = np.linalg.eigh(A)   # eigh: symmetric -- sorted, real
Lambda = np.diag(lamb)

# Verify A = Q Lambda Q^T
A_reconstructed = Q @ Lambda @ Q.T
print('Reconstruction error:', np.linalg.norm(A - A_reconstructed))  # ~1e-14

# Rank-1 decomposition
A_sum = sum(lamb[i] * np.outer(Q[:,i], Q[:,i]) for i in range(5))
print('Rank-1 sum error:', np.linalg.norm(A - A_sum))  # ~1e-14
```

## PCA as Eigendecomposition of the Covariance Matrix

**Principal Component Analysis (PCA)** finds the directions of maximum variance in data. Given centered data matrix **X** (shape n×d), the covariance matrix is **C = (1/n) XᵀX** (shape d×d, symmetric PSD). Eigendecomposing **C**:

  **C = QΛQᵀ**

The eigenvectors (columns of **Q**) are the **principal components** — the orthogonal directions of variance. The eigenvalues λᵢ are the variance in each direction. Projecting data onto the top-k eigenvectors gives the optimal k-dimensional representation that minimizes reconstruction error. The fraction of variance explained by the top-k components is Σᵢ≤ₖ λᵢ / Σᵢ λᵢ.

```python
import numpy as np

np.random.seed(0)
n, d = 200, 10
X = np.random.randn(n, d)
# Make first 2 dims have high variance
X[:, 0] *= 5
X[:, 1] *= 3

# Center and compute covariance
X_c = X - X.mean(axis=0)
C = (X_c.T @ X_c) / n   # (d, d) covariance

# Eigendecomposition
lamb, Q = np.linalg.eigh(C)
lamb = lamb[::-1]; Q = Q[:, ::-1]  # sort descending

# Project to top-2 PCs
X_pca = X_c @ Q[:, :2]             # (n, 2)
var_explained = lamb[:2].sum() / lamb.sum()
print(f'Variance explained by top 2 PCs: {var_explained:.1%}')
```

## Power Iteration and the Dominant Eigenvector

For large matrices where full eigendecomposition is too expensive, **power iteration** finds the largest (dominant) eigenvector iteratively:

1. Start with a random vector **v₀**
2. Repeatedly compute **v_{k+1} = A v_k / ||A v_k||**
3. Convergence: the vector aligns with the dominant eigenvector at rate |λ₂/λ₁|ᵏ

Power iteration converges faster when the ratio of the two largest eigenvalues is small (large eigengap). The **Lanczos algorithm** is an efficient extension for symmetric matrices that builds a Krylov subspace and finds multiple eigenvectors without computing the full eigendecomposition.

## Markov Chains and the Stationary Distribution

A **Markov chain** is defined by a transition matrix **P** where **P[i,j]** is the probability of moving from state j to state i (column-stochastic: columns sum to 1). The stationary distribution **π** satisfies **Pπ = π**, meaning **π** is an eigenvector of **P** with eigenvalue 1.

By the Perron-Frobenius theorem, for irreducible aperiodic chains, the dominant eigenvalue is exactly 1 (all others have |λ| < 1). Power iteration on **P** corresponds to repeatedly multiplying the state distribution by **P** — it converges to **π** because all components along non-dominant eigenvectors decay geometrically. This is the mathematical foundation of **Google PageRank**.

```python
import numpy as np

# Simple 3-state Markov chain (column-stochastic)
P = np.array([[0.7, 0.2, 0.1],
              [0.2, 0.5, 0.3],
              [0.1, 0.3, 0.6]])

# Power iteration: apply P repeatedly
pi = np.array([1/3, 1/3, 1/3])   # start uniform
for _ in range(100):
    pi = P @ pi
print('Stationary distribution (power iter):', pi)

# Eigendecomposition approach
vals, vecs = np.linalg.eig(P)
idx = np.argmax(np.abs(vals))
pi_eig = np.abs(vecs[:, idx])
pi_eig /= pi_eig.sum()
print('Stationary distribution (eigenvector):', pi_eig)
print('Match:', np.allclose(pi, pi_eig, atol=1e-6))
```

## Eigenvalues in Neural Network Analysis

Eigenvalues appear throughout deep learning analysis:

- **Loss landscape**: The Hessian **H** of the loss (second derivatives) has eigenvalues that measure the curvature in each direction. Large eigenvalues → sharp curvature → sensitive to learning rate. The ratio λ_max/λ_min (condition number) determines gradient descent convergence speed.
- **Gradient explosion/vanishing**: In RNNs, if the recurrent weight matrix **W** has eigenvalues |λ| > 1, repeated multiplication **Wᵗ** grows exponentially (explosion); if |λ| < 1, it vanishes. The orthogonal/unitary RNN research constrains eigenvalues to the unit circle.
- **Spectral normalization**: Dividing weight matrices by their largest singular value (operator norm) stabilizes GAN training by constraining the Lipschitz constant.

| Application | Matrix | Eigenvalue Meaning |
| --- | --- | --- |
| PCA | Covariance C = XᵀX/n | Variance in each principal direction |
| Graph Laplacian | L = D - A | Number of connected components (zero eigenvalues) |
| PageRank | Transition matrix P | Dominant eigenvector = page importance scores |
| RNN stability | Recurrent weight W | |λ| > 1 → explosion, |λ| < 1 → vanishing |
| Loss landscape | Hessian H = ∂²L/∂θ² | Curvature; condition number affects convergence |
| GAN training | Weight matrix W | Spectral norm = Lipschitz constant |

> **[TIP] Use eigh for Symmetric Matrices**
>
> NumPy's np.linalg.eigh (note the 'h') is specifically for Hermitian/symmetric matrices. It is faster than eig, guarantees real eigenvalues, and returns them sorted in ascending order. For covariance matrices, Gram matrices, or Hessians, always use eigh rather than the general eig.
