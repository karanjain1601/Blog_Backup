---
title: "Receptive Field Analysis in Convolutional Networks"
slug: "receptive-field-analysis"
description: "Theoretical vs effective receptive field, how stride and dilation affect coverage, and why large receptive fields matter for detecting context-dependent patterns."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcmVjZXB0aXZlIGZpZWxkIG9mIGEgbmV1cm9uIGluIGEgQ05OIGlzIHRoZSByZWdpb24gb2YgdGhlIGlucHV0IGltYWdlIHRoYXQgaW5mbHVlbmNlcyBpdHMgYWN0aXZhdGlvbi4gVW5kZXJzdGFuZGluZyByZWNlcHRpdmUgZmllbGRzIGlzIGNyaXRpY2FsIGZvciBhcmNoaXRlY3R1cmUgZGVzaWduOiB0b28gc21hbGwgYW5kIHRoZSBuZXR3b3JrIG1pc3NlcyBjb250ZXh0OyB0b28gbGFyZ2UgYW5kIGl0IHdhc3RlcyBjYXBhY2l0eSBvbiBpcnJlbGV2YW50IHJlZ2lvbnMuIE1vZGVybiBkZXRlY3RvcnMgZGVwZW5kIG9uIGNhcmVmdWxseSBlbmdpbmVlcmVkIFJGIGNvdmVyYWdlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHdvIGRpc3RpbmN0IG5vdGlvbnMgZG9taW5hdGUgdGhlIGxpdGVyYXR1cmU6IHRoZSB0aGVvcmV0aWNhbCByZWNlcHRpdmUgZmllbGQsIGRlcml2ZWQgYW5hbHl0aWNhbGx5IGZyb20ga2VybmVsIHNpemVzIGFuZCBzdHJpZGVzLCBhbmQgdGhlIGVmZmVjdGl2ZSByZWNlcHRpdmUgZmllbGQsIG1lYXN1cmVkIGVtcGlyaWNhbGx5IGFzIHRoZSBncmFkaWVudCBvZiBhIGNlbnRlciBvdXRwdXQgbmV1cm9uIHdpdGggcmVzcGVjdCB0byBlYWNoIGlucHV0IHBpeGVsLiBUaGVzZSB0d28gcXVhbnRpdGllcyBkaWZmZXIgc3Vic3RhbnRpYWxseSBhbmQgaGF2ZSBkaWZmZXJlbnQgaW1wbGljYXRpb25zIGZvciBkZXNpZ24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlb3JldGljYWwgUmVjZXB0aXZlIEZpZWxkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBzdGFjayBvZiBjb252b2x1dGlvbmFsIGxheWVycyBlYWNoIHdpdGgga2VybmVsIHNpemUga19pIGFuZCBzdHJpZGUgc19pLCB0aGUgdGhlb3JldGljYWwgUkYgb2YgdGhlIGZpbmFsIGZlYXR1cmUgbWFwIHBpeGVsIGlzIGNvbXB1dGVkIHJlY3Vyc2l2ZWx5LiBUaGUgZm9ybXVsYSBhY2N1bXVsYXRlcyBjb250cmlidXRpb25zIGZyb20gZWFjaCBsYXllciwgd2VpZ2h0ZWQgYnkgdGhlIHByb2R1Y3Qgb2YgYWxsIHByaW9yIHN0cmlkZXMuIEFkZGluZyBsYXllcnMgZ3Jvd3MgdGhlIFJGLCBidXQgZGVlcGVyIGNvbnRyaWJ1dGlvbnMgYXJlIGRpbHV0ZWQgYnkgcmVwZWF0ZWQgZG93bnNhbXBsaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJkZWYgY29tcHV0ZV90aGVvcmV0aWNhbF9yZihsYXllcnMpOlxuICAgICMgbGF5ZXJzOiBsaXN0IG9mIChrZXJuZWxfc2l6ZSwgc3RyaWRlKSB0dXBsZXNcbiAgICByZiA9IDFcbiAgICB0b3RhbF9zdHJpZGUgPSAxXG4gICAgZm9yIGssIHMgaW4gbGF5ZXJzOlxuICAgICAgICByZiA9IHJmICsgKGsgLSAxKSAqIHRvdGFsX3N0cmlkZVxuICAgICAgICB0b3RhbF9zdHJpZGUgKj0gc1xuICAgIHJldHVybiByZlxuXG5sYXllcnMgPSBbKDMsMSksKDMsMSksKDMsMiksKDMsMSksKDMsMiksKDMsMSldXG5wcmludChmXCJUaGVvcmV0aWNhbCBSRjoge2NvbXB1dGVfdGhlb3JldGljYWxfcmYobGF5ZXJzKX1cIikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciB0aHJlZSBzZXF1ZW50aWFsIDN4MyBjb252b2x1dGlvbnMgd2l0aCBzdHJpZGUgMSwgdGhlIFRSRiBpcyA3LiBBZGRpbmcgYSBzdHJpZGUtMiBsYXllciBkb3VibGVzIHRoZSBlZmZlY3RpdmUganVtcCwgcmFwaWRseSBleHRlbmRpbmcgY292ZXJhZ2UuIFRoZSBmb3JtdWxhIHNob3dzIHRoYXQgc3RyaWRlIGhhcyBhIG11bHRpcGxpY2F0aXZlIGVmZmVjdDogYSBzaW5nbGUgc3RyaWRlLTQgbGF5ZXIgY29udHJpYnV0ZXMgNHggbW9yZSBwZXIga2VybmVsIHBvc2l0aW9uIHRoYW4gYSBzdHJpZGUtMSBsYXllciBhdCB0aGUgc2FtZSBkZXB0aCBpbiB0aGUgbmV0d29yay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFZmZlY3RpdmUgUmVjZXB0aXZlIEZpZWxkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMdW8gZXQgYWwuICgyMDE2KSBzaG93ZWQgdGhhdCB0aGUgZWZmZWN0aXZlIHJlY2VwdGl2ZSBmaWVsZCBmb2xsb3dzIGEgR2F1c3NpYW4gZGlzdHJpYnV0aW9uIG92ZXIgdGhlIHRoZW9yZXRpY2FsIFJGIGFyZWEuIENlbnRyYWwgcGl4ZWxzIGNvbnRyaWJ1dGUgZXhwb25lbnRpYWxseSBtb3JlIHRoYW4gcGVyaXBoZXJhbCBvbmVzIGR1ZSB0byB0aGUgY29tYmluYXRvcmlhbCBwYXRoIGNvdW50IGluIHRoZSBjb21wdXRhdGlvbmFsIGdyYXBoLiBBcyBkZXB0aCBpbmNyZWFzZXMsIHRoZSBFUkYgZ3Jvd3Mgb25seSBhcyBPKHNxcnQoZGVwdGgpKSByYXRoZXIgdGhhbiBsaW5lYXJseSB3aXRoIGRlcHRoLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIGVmZmVjdGl2ZV9yZihtb2RlbCwgaW5wdXRfc2l6ZT0oMSwgMywgMjI0LCAyMjQpKTpcbiAgICB4ID0gdG9yY2guemVyb3MoKmlucHV0X3NpemUsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbiAgICBvdXQgPSBtb2RlbCh4KVxuICAgIGgsIHcgPSBvdXQuc2hhcGVbLTJdLCBvdXQuc2hhcGVbLTFdXG4gICAgb3V0WzAsIDAsIGggLy8gMiwgdyAvLyAyXS5iYWNrd2FyZCgpXG4gICAgZXJmID0geC5ncmFkWzBdLmFicygpLnN1bSgwKVxuICAgIHBsdC5pbXNob3coZXJmLmRldGFjaCgpLm51bXB5KCksIGNtYXA9XHUwMDI3aG90XHUwMDI3KVxuICAgIHBsdC50aXRsZShcdTAwMjdFZmZlY3RpdmUgUmVjZXB0aXZlIEZpZWxkXHUwMDI3KVxuICAgIHBsdC5jb2xvcmJhcigpXG4gICAgcmV0dXJuIGVyZiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmlzdWFsaXppbmcgdGhlIEVSRiByZXZlYWxzIHRoYXQgb25seSB0aGUgY2VudHJhbCB+NDAlIG9mIHRoZSB0aGVvcmV0aWNhbCBSRiBjYXJyaWVzIHN1YnN0YW50aWFsIGdyYWRpZW50IG1hZ25pdHVkZS4gVGhpcyBoYXMgYXJjaGl0ZWN0dXJhbCBjb25zZXF1ZW5jZXM6IHNpbXBseSBzdGFja2luZyBtb3JlIGxheWVycyBkb2VzIG5vdCBndWFyYW50ZWUgdGhhdCBkaXN0YW50IGNvbnRleHQgaXMgYWN0dWFsbHkgdXNlZC4gU2tpcCBjb25uZWN0aW9ucyBhbmQgYXR0ZW50aW9uIG1lY2hhbmlzbXMgY29tcGVuc2F0ZSBieSBjcmVhdGluZyBzaG9ydGN1dHMgZm9yIGxvbmctcmFuZ2UgaW5mb3JtYXRpb24gZmxvdy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJjb250ZW50IjoiVGhlIHRoZW9yZXRpY2FsIHJlY2VwdGl2ZSBmaWVsZCBncm93cyBxdWFkcmF0aWNhbGx5IHdpdGggZGVwdGgsIGJ1dCB0aGUgKmVmZmVjdGl2ZSogcmVjZXB0aXZlIGZpZWxkIGZvbGxvd3MgYSBHYXVzc2lhbiBkaXN0cmlidXRpb24g4oCUIG9ubHkgdGhlIGNlbnRyYWwgfjQwJSBvZiB0aGUgdGhlb3JldGljYWwgUkYgY29udHJpYnV0ZXMgbWVhbmluZ2Z1bGx5LiBEZXB0aCBhbG9uZSBkb2Vzblx1MDAyN3QgZ3VhcmFudGVlIGdsb2JhbCBjb250ZXh0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpbGF0aW9uIGFuZCBBdHJvdXMgQ29udm9sdXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaWxhdGVkIChhdHJvdXMpIGNvbnZvbHV0aW9ucyBpbnNlcnQgemVyb3MgYmV0d2VlbiBrZXJuZWwgd2VpZ2h0cywgZXhwYW5kaW5nIHRoZSByZWNlcHRpdmUgZmllbGQgd2l0aG91dCBpbmNyZWFzaW5nIHBhcmFtZXRlcnMgb3IgcmVkdWNpbmcgcmVzb2x1dGlvbi4gQSAzeDMgY29udiB3aXRoIGRpbGF0aW9uIHJhdGUgciBjb3ZlcnMgYSAoMnIrMSl4KDJyKzEpIHJlZ2lvbiB1c2luZyBvbmx5IDkgd2VpZ2h0cy4gVGhpcyBtYWtlcyB0aGVtIGlkZWFsIGZvciBkZW5zZSBwcmVkaWN0aW9uIHRhc2tzIGxpa2Ugc2VtYW50aWMgc2VnbWVudGF0aW9uIGFuZCBkZXB0aCBlc3RpbWF0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuQyA9IDY0XG4jIERpbGF0ZWQgM3gzIHdpdGggcmF0ZT0yOiBjb3ZlcnMgNXg1IHJlZ2lvbiwgb25seSA5IHBhcmFtc1xuZGlsYXRlZCA9IG5uLkNvbnYyZChDLCBDLCBrZXJuZWxfc2l6ZT0zLCBwYWRkaW5nPTIsIGRpbGF0aW9uPTIpXG5cbiMgU3RhbmRhcmQgNXg1IGNvbnY6IHNhbWUgc3BhdGlhbCBjb3ZlcmFnZSwgMjUgcGFyYW1zIHBlciBjaGFubmVsXG5zdGFuZGFyZF81eDUgPSBubi5Db252MmQoQywgQywga2VybmVsX3NpemU9NSwgcGFkZGluZz0yKVxuXG5kX3BhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gZGlsYXRlZC5wYXJhbWV0ZXJzKCkpXG5zX3BhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gc3RhbmRhcmRfNXg1LnBhcmFtZXRlcnMoKSlcbnByaW50KGZcIkRpbGF0ZWQgM3gzOiB7ZF9wYXJhbXN9IHwgU3RhbmRhcmQgNXg1OiB7c19wYXJhbXN9IHBhcmFtc1wiKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBkaWxhdGVkIDN4MyB3aXRoIHJhdGU9MiBzcGFucyA1eDUgaW5wdXQgcG9zaXRpb25zLCBtYXRjaGluZyBhIHN0YW5kYXJkIDV4NSBjb252IGJ1dCB1c2luZyBvbmx5IDkgd2VpZ2h0cyBpbnN0ZWFkIG9mIDI1LiBTdGFja2luZyBkaWxhdGlvbnMgZXhwb25lbnRpYWxseSAoMSwgMiwgNCwgOCkgYWNoaWV2ZXMgUkY9MTUgaW4gZm91ciBsYXllcnMgd2l0aCAzNiBwYXJhbWV0ZXJzLiBEZWVwTGFidjMrIHVzZXMgYXRyb3VzIHNwYXRpYWwgcHlyYW1pZCBwb29saW5nIHdpdGggcmF0ZXMgKDYsIDEyLCAxOCkgdG8gY2FwdHVyZSBtdWx0aS1zY2FsZSBjb250ZXh0IHNpbXVsdGFuZW91c2x5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlY2VwdGl2ZSBGaWVsZCB2cyBUYXNrIFNjYWxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPYmplY3QgZGV0ZWN0aW9uIHBlcmZvcm1hbmNlIHZhcmllcyB3aXRoIFJGLXRvLW9iamVjdC1zaXplIGFsaWdubWVudC4gU21hbGwgb2JqZWN0cyAoQ09DTyBhcmVhIFx1MDAzYyAzMl4yKSByZXF1aXJlIGZpbmUtZ3JhaW5lZCwgc21hbGwtUkYgZmVhdHVyZXMgcHJlc2VydmVkIHRocm91Z2ggRlBOIGxhdGVyYWwgY29ubmVjdGlvbnMuIExhcmdlIG9iamVjdHMgKGFyZWEgXHUwMDNlIDk2XjIpIGJlbmVmaXQgZnJvbSBnbG9iYWwgY29udGV4dCBjYXB0dXJlZCBieSBkZWVwIGxheWVycy4gTWlzbWF0Y2hlZCBSRiBhbmQgb2JqZWN0IHNjYWxlIGlzIGEgcHJpbWFyeSBzb3VyY2Ugb2YgQVAgZGVncmFkYXRpb24gaW4gb25lLXN0YWdlIGRldGVjdG9ycy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXJjaGl0ZWN0dXJlIiwiTGF5ZXJzIiwiVGhlb3JldGljYWwgUkYiLCJFZmZlY3RpdmUgUkYgKGFwcHJveCkiLCJBUF9zIiwiQVBfbCJdLCJyb3dzIjpbWyJWR0ctMTYiLCIxMyBjb252IiwiMjEyIiwifjMyIiwiMTIuMyIsIjUxLjEiXSxbIlJlc05ldC01MCIsIjQ5IGNvbnYiLCI0ODMiLCJ+NDgiLCIxNi40IiwiNTYuMiJdLFsiUmVzTmV0LTUwICsgRlBOIiwiNDkgY29udiArIEZQTiIsIjQ4MyAobXVsdGktc2NhbGUpIiwifjQ4IG11bHRpIiwiMjMuNyIsIjU1LjMiXSxbIkRlZXBMYWJ2MysiLCI0OSArIEFTUFAiLCIxMDI1KyIsIn45NiIsIuKAlCIsIuKAlCJdXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBqc29uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHJmX3ZzX2NvY29fYXAocmVzdWx0c19wYXRoKTpcbiAgICB3aXRoIG9wZW4ocmVzdWx0c19wYXRoKSBhcyBmOlxuICAgICAgICByZXN1bHRzID0ganNvbi5sb2FkKGYpXG4gICAgcmZfc2l6ZXMgPSBbcltcdTAwMjd0aGVvcmV0aWNhbF9yZlx1MDAyN10gZm9yIHIgaW4gcmVzdWx0c11cbiAgICBhcF9zID0gW3JbXHUwMDI3QVBfc21hbGxcdTAwMjddIGZvciByIGluIHJlc3VsdHNdXG4gICAgYXBfbCA9IFtyW1x1MDAyN0FQX2xhcmdlXHUwMDI3XSBmb3IgciBpbiByZXN1bHRzXVxuICAgIGNvcnJfcyA9IG5wLmNvcnJjb2VmKHJmX3NpemVzLCBhcF9zKVswLCAxXVxuICAgIGNvcnJfbCA9IG5wLmNvcnJjb2VmKHJmX3NpemVzLCBhcF9sKVswLCAxXVxuICAgIHByaW50KGZcIlJGIHZzIEFQX3NtYWxsIGNvcnI6IHtjb3JyX3M6LjNmfVwiKVxuICAgIHByaW50KGZcIlJGIHZzIEFQX2xhcmdlIGNvcnI6IHtjb3JyX2w6LjNmfVwiKVxuICAgIHJldHVybiBjb3JyX3MsIGNvcnJfbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXJjaGl0ZWN0dXJlcyB3aXRoIEZQTiBhY2hpZXZlIHRoZSBiZXN0IEFQIGJhbGFuY2UgYnkgYWdncmVnYXRpbmcgZmVhdHVyZXMgZnJvbSBtdWx0aXBsZSBSRiBzY2FsZXMuIFBsYWluIGRlZXAgbmV0d29ya3MgZXhjZWwgYXQgQVBfbCBidXQgc2FjcmlmaWNlIEFQX3MgYmVjYXVzZSBlYXJseSBoaWdoLXJlc29sdXRpb24gZmVhdHVyZXMgYXJlIGRpc2NhcmRlZC4gVGhlIFJGLXNjYWxlIG1pc21hdGNoIGV4cGxhaW5zIHdoeSBuYWl2ZSBkZXB0aCBzY2FsaW5nIGZhaWxzIHRvIHVuaWZvcm1seSBpbXByb3ZlIGRldGVjdGlvbiBhY3Jvc3MgYWxsIG9iamVjdCBzaXplcyBpbiB0aGUgQ09DTyBiZW5jaG1hcmsuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlb3JldGljYWwgUkYgcHJvdmlkZXMgYSBkZXNpZ24gY2VpbGluZyBidXQgbm90IG9wZXJhdGlvbmFsIGd1YXJhbnRlZXMuIEFsd2F5cyBtZWFzdXJlIHRoZSBFUkYgZW1waXJpY2FsbHkgb24gcmVwcmVzZW50YXRpdmUgaW5wdXRzIGFuZCBjb21wYXJlIGl0IHRvIHRoZSBzY2FsZSBvZiBzdHJ1Y3R1cmVzIHlvdSBuZWVkIHRvIGRldGVjdC4gRm9yIGxhcmdlLWNvbnRleHQgdGFza3MsIGNvbWJpbmUgZGlsYXRpb24sIEZQTiwgYW5kIGF0dGVudGlvbiByYXRoZXIgdGhhbiByZWx5aW5nIHNvbGVseSBvbiBkZXB0aCB0byBleHRlbmQgY292ZXJhZ2UgYWNyb3NzIHRoZSBpbnB1dCBpbWFnZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpbGF0aW9uIGV4cGFuZHMgUkYgY2hlYXBseSB3aXRob3V0IHJlc29sdXRpb24gbG9zcywgbWFraW5nIGl0IHRoZSBwcmVmZXJyZWQgdG9vbCBmb3Igc2VnbWVudGF0aW9uIGJhY2tib25lcy4gRlBOIHByb3ZpZGVzIG11bHRpLXNjYWxlIFJGIGNvdmVyYWdlIGZvciBkZXRlY3Rpb24uIEF0dGVudGlvbiBsYXllcnMgcmVwbGFjZSBmaXhlZCBSRiB3aXRoIGR5bmFtaWMsIGNvbnRlbnQtZGVwZW5kZW50IGNvdmVyYWdlLiBNb2Rlcm4gYXJjaGl0ZWN0dXJlcyBpbmNyZWFzaW5nbHkgY29tYmluZSBhbGwgdGhyZWUgc3RyYXRlZ2llcyBmb3Igcm9idXN0IG11bHRpLXNjYWxlIHJlYXNvbmluZyBhY3Jvc3MgZGl2ZXJzZSB2aXN1YWwgdGFza3MuIn1d"
---
# Receptive Field Analysis in Convolutional Networks

## Overview

The receptive field of a neuron in a CNN is the region of the input image that influences its activation. Understanding receptive fields is critical for architecture design: too small and the network misses context; too large and it wastes capacity on irrelevant regions. Modern detectors depend on carefully engineered RF coverage.

Two distinct notions dominate the literature: the theoretical receptive field, derived analytically from kernel sizes and strides, and the effective receptive field, measured empirically as the gradient of a center output neuron with respect to each input pixel. These two quantities differ substantially and have different implications for design.

## Theoretical Receptive Field

For a stack of convolutional layers each with kernel size k_i and stride s_i, the theoretical RF of the final feature map pixel is computed recursively. The formula accumulates contributions from each layer, weighted by the product of all prior strides. Adding layers grows the RF, but deeper contributions are diluted by repeated downsampling.

```python
def compute_theoretical_rf(layers):
    # layers: list of (kernel_size, stride) tuples
    rf = 1
    total_stride = 1
    for k, s in layers:
        rf = rf + (k - 1) * total_stride
        total_stride *= s
    return rf

layers = [(3,1),(3,1),(3,2),(3,1),(3,2),(3,1)]
print(f"Theoretical RF: {compute_theoretical_rf(layers)}")
```

For three sequential 3x3 convolutions with stride 1, the TRF is 7. Adding a stride-2 layer doubles the effective jump, rapidly extending coverage. The formula shows that stride has a multiplicative effect: a single stride-4 layer contributes 4x more per kernel position than a stride-1 layer at the same depth in the network.

## Effective Receptive Field

Luo et al. (2016) showed that the effective receptive field follows a Gaussian distribution over the theoretical RF area. Central pixels contribute exponentially more than peripheral ones due to the combinatorial path count in the computational graph. As depth increases, the ERF grows only as O(sqrt(depth)) rather than linearly with depth.

```python
import torch
import matplotlib.pyplot as plt

def effective_rf(model, input_size=(1, 3, 224, 224)):
    x = torch.zeros(*input_size, requires_grad=True)
    out = model(x)
    h, w = out.shape[-2], out.shape[-1]
    out[0, 0, h // 2, w // 2].backward()
    erf = x.grad[0].abs().sum(0)
    plt.imshow(erf.detach().numpy(), cmap='hot')
    plt.title('Effective Receptive Field')
    plt.colorbar()
    return erf
```

Visualizing the ERF reveals that only the central ~40% of the theoretical RF carries substantial gradient magnitude. This has architectural consequences: simply stacking more layers does not guarantee that distant context is actually used. Skip connections and attention mechanisms compensate by creating shortcuts for long-range information flow.

> **warning**: The theoretical receptive field grows quadratically with depth, but the *effective* receptive field follows a Gaussian distribution — only the central ~40% of the theoretical RF contributes meaningfully. Depth alone doesn't guarantee global context.

## Dilation and Atrous Convolutions

Dilated (atrous) convolutions insert zeros between kernel weights, expanding the receptive field without increasing parameters or reducing resolution. A 3x3 conv with dilation rate r covers a (2r+1)x(2r+1) region using only 9 weights. This makes them ideal for dense prediction tasks like semantic segmentation and depth estimation.

```python
import torch.nn as nn

C = 64
# Dilated 3x3 with rate=2: covers 5x5 region, only 9 params
dilated = nn.Conv2d(C, C, kernel_size=3, padding=2, dilation=2)

# Standard 5x5 conv: same spatial coverage, 25 params per channel
standard_5x5 = nn.Conv2d(C, C, kernel_size=5, padding=2)

d_params = sum(p.numel() for p in dilated.parameters())
s_params = sum(p.numel() for p in standard_5x5.parameters())
print(f"Dilated 3x3: {d_params} | Standard 5x5: {s_params} params")
```

A dilated 3x3 with rate=2 spans 5x5 input positions, matching a standard 5x5 conv but using only 9 weights instead of 25. Stacking dilations exponentially (1, 2, 4, 8) achieves RF=15 in four layers with 36 parameters. DeepLabv3+ uses atrous spatial pyramid pooling with rates (6, 12, 18) to capture multi-scale context simultaneously.

## Receptive Field vs Task Scale

Object detection performance varies with RF-to-object-size alignment. Small objects (COCO area < 32^2) require fine-grained, small-RF features preserved through FPN lateral connections. Large objects (area > 96^2) benefit from global context captured by deep layers. Mismatched RF and object scale is a primary source of AP degradation in one-stage detectors.

| Architecture | Layers | Theoretical RF | Effective RF (approx) | AP_s | AP_l |
| --- | --- | --- | --- | --- | --- |
| VGG-16 | 13 conv | 212 | ~32 | 12.3 | 51.1 |
| ResNet-50 | 49 conv | 483 | ~48 | 16.4 | 56.2 |
| ResNet-50 + FPN | 49 conv + FPN | 483 (multi-scale) | ~48 multi | 23.7 | 55.3 |
| DeepLabv3+ | 49 + ASPP | 1025+ | ~96 | — | — |

```python
import json
import numpy as np

def rf_vs_coco_ap(results_path):
    with open(results_path) as f:
        results = json.load(f)
    rf_sizes = [r['theoretical_rf'] for r in results]
    ap_s = [r['AP_small'] for r in results]
    ap_l = [r['AP_large'] for r in results]
    corr_s = np.corrcoef(rf_sizes, ap_s)[0, 1]
    corr_l = np.corrcoef(rf_sizes, ap_l)[0, 1]
    print(f"RF vs AP_small corr: {corr_s:.3f}")
    print(f"RF vs AP_large corr: {corr_l:.3f}")
    return corr_s, corr_l
```

Architectures with FPN achieve the best AP balance by aggregating features from multiple RF scales. Plain deep networks excel at AP_l but sacrifice AP_s because early high-resolution features are discarded. The RF-scale mismatch explains why naive depth scaling fails to uniformly improve detection across all object sizes in the COCO benchmark.

## Key Takeaways

Theoretical RF provides a design ceiling but not operational guarantees. Always measure the ERF empirically on representative inputs and compare it to the scale of structures you need to detect. For large-context tasks, combine dilation, FPN, and attention rather than relying solely on depth to extend coverage across the input image.

Dilation expands RF cheaply without resolution loss, making it the preferred tool for segmentation backbones. FPN provides multi-scale RF coverage for detection. Attention layers replace fixed RF with dynamic, content-dependent coverage. Modern architectures increasingly combine all three strategies for robust multi-scale reasoning across diverse visual tasks.

