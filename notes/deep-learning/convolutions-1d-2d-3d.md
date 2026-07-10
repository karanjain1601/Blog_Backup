---
title: "1D, 2D, and 3D Convolutions — Applications for Each"
slug: "convolutions-1d-2d-3d"
description: "Compare 1D, 2D, and 3D convolutions across input shapes, parameter counts, and domains — from time-series and audio to images, video, and volumetric medical data."
tags: ["deep-learning", "cnns"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udm9sdXRpb24gZ2VuZXJhbGlzZXMgbmF0dXJhbGx5IGFjcm9zcyBkaW1lbnNpb25hbGl0aWVzOiAxRCBzbGlkZXMgYSBrZXJuZWwgYWxvbmcgYSBzaW5nbGUgYXhpcyAodGltZSBvciBzZXF1ZW5jZSBsZW5ndGgpLCAyRCBzbGlkZXMgb3ZlciBhIHNwYXRpYWwgcGxhbmUgKGhlaWdodCDDlyB3aWR0aCksIGFuZCAzRCBzbGlkZXMgb3ZlciBhIHZvbHVtZSAoZGVwdGggw5cgaGVpZ2h0IMOXIHdpZHRoIG9yIHRpbWUgw5cgaGVpZ2h0IMOXIHdpZHRoKS4gQ2hvb3NpbmcgdGhlIHJpZ2h0IGRpbWVuc2lvbmFsaXR5IGlzIG5vdCBhcmJpdHJhcnkg4oCUIGl0IGVuY29kZXMgYSBzdHJ1Y3R1cmFsIGFzc3VtcHRpb24gYWJvdXQgd2hlcmUgbG9jYWwgY29ycmVsYXRpb25zIGV4aXN0IGluIHRoZSBkYXRhLCBhbmQgbWF0Y2hpbmcgdGhhdCBhc3N1bXB0aW9uIHRvIHRoZSB0cnVlIGRhdGEgZ2VvbWV0cnkgaXMgdGhlIGZpcnN0IGFyY2hpdGVjdHVyYWwgZGVjaXNpb24gZm9yIGFueSBDTk4gZGVzaWduLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IjFEIENvbnZvbHV0aW9uIOKAlCBTZXF1ZW5jZXMsIEF1ZGlvLCBhbmQgVGltZSBTZXJpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Im5uLkNvbnYxZCB0YWtlcyBpbnB1dCBvZiBzaGFwZSAoTiwgQywgTCkg4oCUIGJhdGNoLCBjaGFubmVscywgbGVuZ3RoIOKAlCBhbmQgcHJvZHVjZXMgb3V0cHV0IChOLCBDX291dCwgTF9vdXQpLiBUaGUga2VybmVsIHNsaWRlcyBhbG9uZyB0aGUgTCBkaW1lbnNpb24gb25seS4gQXBwbGljYXRpb25zOiB0aW1lLXNlcmllcyBjbGFzc2lmaWNhdGlvbiAoRUNHLCBhY2NlbGVyb21ldGVyKSwgYXVkaW8gd2F2ZWZvcm0gbW9kZWxsaW5nIChXYXZlTmV0IHN0YWNrcyBkaWxhdGVkIDFEIGNvbnZzIHRvIGFjaGlldmUgcmVjZXB0aXZlIGZpZWxkcyBvZiB0aG91c2FuZHMgb2Ygc2FtcGxlcyksIHRleHQgY2xhc3NpZmljYXRpb24gKFRleHRDTk4gYXBwbGllcyBtdWx0aXBsZSBrZXJuZWwgc2l6ZXMgbGlrZSAzLCA0LCA1IHRoZW4gbWF4LXBvb2xzKSwgYW5kIHBvc2l0aW9uIG1peGluZyBpbiBoeWJyaWQgbW9kZWxzLiAxRCBjb252IGlzIG11Y2ggZmFzdGVyIHRoYW4gUk5OcyBmb3IgZml4ZWQtY29udGV4dCB0YXNrcyBhbmQgZnVsbHkgcGFyYWxsZWxpc2FibGUgZHVyaW5nIHRyYWluaW5nLiBXYXZlTmV0IGFjaGlldmVkIHN0YXRlLW9mLXRoZS1hcnQgdGV4dC10by1zcGVlY2ggYnkgc3RhY2tpbmcgMzAgZGlsYXRlZCAxRCBjb252IGxheWVycyB3aXRoIGRpbGF0aW9uIHJhdGVzIFsxLDIsNCwuLi4sNTEyXSByZXBlYXRlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgRUNHQ2xhc3NpZmllcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIjFEIENOTiBmb3IgdGltZS1zZXJpZXMgKEVDRykgY2xhc3NpZmljYXRpb24uXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fY2xhc3Nlcz01KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuY29udjEgPSBubi5Db252MWQoMSwgMzIsIGtlcm5lbF9zaXplPTcsIHBhZGRpbmc9MykgICAjIChOLDMyLEwpXG4gICAgICAgIHNlbGYuY29udjIgPSBubi5Db252MWQoMzIsIDY0LCBrZXJuZWxfc2l6ZT01LCBwYWRkaW5nPTIpICAjIChOLDY0LEwpXG4gICAgICAgIHNlbGYuY29udjMgPSBubi5Db252MWQoNjQsIDEyOCwga2VybmVsX3NpemU9MywgcGFkZGluZz0xKSAjIChOLDEyOCxMKVxuICAgICAgICBzZWxmLnBvb2wgID0gbm4uQWRhcHRpdmVBdmdQb29sMWQoMSkgICAgICAgICAgICAgICAgICAgICAgICMgKE4sMTI4LDEpXG4gICAgICAgIHNlbGYuZmMgICAgPSBubi5MaW5lYXIoMTI4LCBuX2NsYXNzZXMpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgeCA9IEYucmVsdShzZWxmLmNvbnYxKHgpKVxuICAgICAgICB4ID0gRi5tYXhfcG9vbDFkKHgsIDIpICAgICAgICAgICMgaGFsdmUgc2VxdWVuY2UgbGVuZ3RoXG4gICAgICAgIHggPSBGLnJlbHUoc2VsZi5jb252Mih4KSlcbiAgICAgICAgeCA9IEYubWF4X3Bvb2wxZCh4LCAyKVxuICAgICAgICB4ID0gRi5yZWx1KHNlbGYuY29udjMoeCkpXG4gICAgICAgIHggPSBzZWxmLnBvb2woeCkuc3F1ZWV6ZSgtMSkgICAgIyBnbG9iYWwgYXZnIHBvb2wgLVx1MDAzZSAoTiwxMjgpXG4gICAgICAgIHJldHVybiBzZWxmLmZjKHgpXG5cbm1vZGVsID0gRUNHQ2xhc3NpZmllcigpXG54ID0gdG9yY2gucmFuZG4oOCwgMSwgMjU2KSAgIyA4IEVDRyB0cmFjZXMsIHNpbmdsZSBsZWFkLCAyNTYgdGltZXN0ZXBzXG5vdXQgPSBtb2RlbCh4KVxucHJpbnQoZlx1MDAyN0lucHV0OiAge3R1cGxlKHguc2hhcGUpfVx1MDAyNylcbnByaW50KGZcdTAwMjdPdXRwdXQ6IHt0dXBsZShvdXQuc2hhcGUpfVx1MDAyNylcbnBhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKVxucHJpbnQoZlx1MDAyN1RvdGFsIHBhcmFtczoge3BhcmFtczosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiIyRCBDb252b2x1dGlvbiDigJQgSW1hZ2VzIGFuZCBTcGF0aWFsIEZlYXR1cmUgTWFwcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50Ijoibm4uQ29udjJkIHRha2VzIGlucHV0IChOLCBDLCBILCBXKSBhbmQgaXMgdGhlIHN0YW5kYXJkIGJ1aWxkaW5nIGJsb2NrIGZvciBpbWFnZSB0YXNrcy4gSXQgc2xpZGVzIHRoZSBrZXJuZWwgb3ZlciB0d28gc3BhdGlhbCBkaW1lbnNpb25zIHNpbXVsdGFuZW91c2x5LCBsZWFybmluZyB0cmFuc2xhdGlvbi1lcXVpdmFyaWFudCBmZWF0dXJlIGRldGVjdG9ycy4gVmlydHVhbGx5IGFsbCBpbWFnZSBjbGFzc2lmaWNhdGlvbiwgZGV0ZWN0aW9uLCBhbmQgc2VnbWVudGF0aW9uIG5ldHdvcmtzIChWR0csIFJlc05ldCwgRWZmaWNpZW50TmV0LCBZT0xPLCBNYXNrIFItQ05OKSBhcmUgYnVpbHQgb24gMkQgY29udi4gVGhlIGtleSBkZXNpZ24gY2hvaWNlcyBhcmU6IGhvdyBtYW55IGNoYW5uZWxzICh3aWR0aCksIGhvdyBkZWVwIHRvIGdvIChkZXB0aCksIHdoZXJlIHRvIGRvd25zYW1wbGUgKHN0cmlkZSBvciBwb29sKSwgYW5kIHdoYXQga2VybmVsIHNpemVzIHRvIHVzZS4gVGhlIHRyZW5kIHNpbmNlIDIwMTUgaGFzIGJlZW4gdG93YXJkIGFsbC0zw5czIGtlcm5lbHMgKFZHRyBpbnNpZ2h0OiB0d28gM8OXMyBjb252cyBoYXZlIHRoZSBzYW1lIFJGIGFzIG9uZSA1w5c1IGJ1dCBmZXdlciBwYXJhbWV0ZXJzKSwgc2tpcCBjb25uZWN0aW9ucyAoUmVzTmV0KSwgYW5kIGRlcHRod2lzZSBzZXBhcmFibGUgY29udnMgKE1vYmlsZU5ldCkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFNtYWxsSW1hZ2VDTk4obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJDb21wYWN0IDJEIENOTiBmb3IgQ0lGQVItMTAgKDMyeDMyIGlucHV0KS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbnVtX2NsYXNzZXM9MTApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5mZWF0dXJlcyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoMywgMzIsIDMsIHBhZGRpbmc9MSksIG5uLkJhdGNoTm9ybTJkKDMyKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uQ29udjJkKDMyLCA2NCwgMywgcGFkZGluZz0xKSwgbm4uQmF0Y2hOb3JtMmQoNjQpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5NYXhQb29sMmQoMiksICAgICAgICAgICAgICAgICAjIDMyLVx1MDAzZTE2XG4gICAgICAgICAgICBubi5Db252MmQoNjQsIDEyOCwgMywgcGFkZGluZz0xKSwgbm4uQmF0Y2hOb3JtMmQoMTI4KSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uQ29udjJkKDEyOCwgMTI4LCAzLCBwYWRkaW5nPTEpLCBubi5CYXRjaE5vcm0yZCgxMjgpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5NYXhQb29sMmQoMiksICAgICAgICAgICAgICAgICAjIDE2LVx1MDAzZThcbiAgICAgICAgICAgIG5uLkNvbnYyZCgxMjgsIDI1NiwgMywgcGFkZGluZz0xKSwgbm4uQmF0Y2hOb3JtMmQoMjU2KSwgbm4uUmVMVSgpLFxuICAgICAgICApXG4gICAgICAgIHNlbGYuaGVhZCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5BZGFwdGl2ZUF2Z1Bvb2wyZCgxKSxcbiAgICAgICAgICAgIG5uLkZsYXR0ZW4oKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcigyNTYsIG51bV9jbGFzc2VzKVxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYuaGVhZChzZWxmLmZlYXR1cmVzKHgpKVxuXG5tb2RlbCA9IFNtYWxsSW1hZ2VDTk4oKVxueCA9IHRvcmNoLnJhbmRuKDQsIDMsIDMyLCAzMilcbm91dCA9IG1vZGVsKHgpXG5wcmludChmXHUwMDI3SW5wdXQ6IHt0dXBsZSh4LnNoYXBlKX0gLVx1MDAzZSBPdXRwdXQ6IHt0dXBsZShvdXQuc2hhcGUpfVx1MDAyNylcbnByaW50KGZcdTAwMjdQYXJhbXM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSk6LH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiM0QgQ29udm9sdXRpb24g4oCUIFZpZGVvIGFuZCBWb2x1bWV0cmljIERhdGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Im5uLkNvbnYzZCB0YWtlcyBpbnB1dCAoTiwgQywgRCwgSCwgVykgd2hlcmUgRCBpcyBkZXB0aCAodGltZSBmcmFtZXMgZm9yIHZpZGVvLCB6LXNsaWNlcyBmb3IgbWVkaWNhbCBpbWFnaW5nKS4gSXQgYXBwbGllcyBhIDNEIGtlcm5lbCB0aGF0IHNsaWRlcyBvdmVyIGFsbCB0aHJlZSBzcGF0aWFsL3RlbXBvcmFsIGF4ZXMgc2ltdWx0YW5lb3VzbHksIGxlYXJuaW5nIHNwYXRpby10ZW1wb3JhbCBmZWF0dXJlcy4gQzNEIChUcmFuIGV0IGFsLiwgMjAxNSkgdXNlZCAzw5czw5czIGtlcm5lbHMgdGhyb3VnaG91dCBmb3IgYWN0aW9uIHJlY29nbml0aW9uLiBJM0QgaW5mbGF0ZWQgSW1hZ2VOZXQtcHJldHJhaW5lZCAyRCBjb252IHdlaWdodHMgaW50byAzRCBieSByZXBlYXRpbmcgdGhlbSBhbG9uZyB0aGUgdGVtcG9yYWwgYXhpcy4gRm9yIG1lZGljYWwgaW1hZ2luZyAoQ1QsIE1SSSksIDNEIGNvbnYgY2FwdHVyZXMgaW50ZXItc2xpY2UgcmVsYXRpb25zaGlwcyB0aGF0IDJEIHNsaWNlLWJ5LXNsaWNlIHByb2Nlc3NpbmcgbWlzc2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBWaWRlb0NsaXBDTk4obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJNaW5pbWFsIDNEIENOTiBmb3Igc2hvcnQgdmlkZW8gY2xpcCBjbGFzc2lmaWNhdGlvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbnVtX2NsYXNzZXM9MTAxKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgICMgSW5wdXQ6IChOLCAzLCBULCBILCBXKSBlLmcuIChOLCAzLCAxNiwgMTEyLCAxMTIpXG4gICAgICAgIHNlbGYuY29udjEgPSBubi5Db252M2QoMywgIDY0LCBrZXJuZWxfc2l6ZT0oMywzLDMpLCBwYWRkaW5nPTEpXG4gICAgICAgIHNlbGYuY29udjIgPSBubi5Db252M2QoNjQsIDEyOCwga2VybmVsX3NpemU9KDMsMywzKSwgcGFkZGluZz0xKVxuICAgICAgICBzZWxmLmNvbnYzID0gbm4uQ29udjNkKDEyOCwgMjU2LCBrZXJuZWxfc2l6ZT0oMywzLDMpLCBwYWRkaW5nPTEpXG4gICAgICAgIHNlbGYucG9vbCAgPSBubi5BZGFwdGl2ZUF2Z1Bvb2wzZCgxKVxuICAgICAgICBzZWxmLmZjICAgID0gbm4uTGluZWFyKDI1NiwgbnVtX2NsYXNzZXMpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgeCA9IEYucmVsdShzZWxmLmNvbnYxKHgpKVxuICAgICAgICB4ID0gRi5tYXhfcG9vbDNkKHgsIGtlcm5lbF9zaXplPSgxLDIsMikpICAjIG9ubHkgcG9vbCBzcGF0aWFsXG4gICAgICAgIHggPSBGLnJlbHUoc2VsZi5jb252Mih4KSlcbiAgICAgICAgeCA9IEYubWF4X3Bvb2wzZCh4LCBrZXJuZWxfc2l6ZT0oMiwyLDIpKVxuICAgICAgICB4ID0gRi5yZWx1KHNlbGYuY29udjMoeCkpXG4gICAgICAgIHggPSBzZWxmLnBvb2woeCkuc3F1ZWV6ZSgtMSkuc3F1ZWV6ZSgtMSkuc3F1ZWV6ZSgtMSlcbiAgICAgICAgcmV0dXJuIHNlbGYuZmMoeClcblxubW9kZWwgPSBWaWRlb0NsaXBDTk4oKVxueCA9IHRvcmNoLnJhbmRuKDIsIDMsIDE2LCAxMTIsIDExMikgICMgMiBjbGlwcywgMTYgZnJhbWVzLCAxMTJ4MTEyXG5vdXQgPSBtb2RlbCh4KVxucHJpbnQoZlx1MDAyN0lucHV0IDoge3R1cGxlKHguc2hhcGUpfVx1MDAyNylcbnByaW50KGZcdTAwMjdPdXRwdXQ6IHt0dXBsZShvdXQuc2hhcGUpfVx1MDAyNylcbnByaW50KGZcdTAwMjdQYXJhbXM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSk6LH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHNldWRvLTNEIENvbnZvbHV0aW9uIOKAlCBGYWN0b3Jpc2luZyBmb3IgRWZmaWNpZW5jeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRnVsbCAzRCBjb252IGhhcyBrwrMgcGFyYW1ldGVycyBwZXIgZmlsdGVyIHBvc2l0aW9uLiBQc2V1ZG8tM0QgKFAzRCwgUWl1IGV0IGFsLiAyMDE3KSBmYWN0b3Jpc2VzIGEgM8OXM8OXMyBjb252IGludG8gYSBzcGF0aWFsIDPDlzMgKDJELCBubyB0ZW1wb3JhbCBtaXhpbmcpIGZvbGxvd2VkIGJ5IGEgdGVtcG9yYWwgMcOXMcOXMyAoMUQgYWxvbmcgdGltZSwgbm8gc3BhdGlhbCBtaXhpbmcpLiBUaGlzIHJlZHVjZXMgcGFyYW1ldGVycyBmcm9tIGvCs8OXQ19pbsOXQ19vdXQgdG8gKGvCsitrKcOXQ19pbsOXQ19vdXQg4omIIDMuNMOXIGZld2VyIGZvciBrPTMsIHdpdGggY29tcGFyYWJsZSBhY2N1cmFjeSBvbiBhY3Rpb24gcmVjb2duaXRpb24gYmVuY2htYXJrcy4gKDIrMSlEIGNvbnYgKFIoMisxKUQsIFRyYW4gZXQgYWwuIDIwMTgpIGFkZHMgYSBub25saW5lYXJpdHkgYmV0d2VlbiB0aGUgdHdvIGZhY3RvcnMsIGZ1cnRoZXIgaW1wcm92aW5nIGV4cHJlc3Npdml0eS4gVGhlc2UgZmFjdG9yZWQgZGVzaWducyBtYWtlIDNELWNvbnYtYmFzZWQgdmlkZW8gdW5kZXJzdGFuZGluZyBwcmFjdGljYWwgb24gc3RhbmRhcmQgR1BVIGJ1ZGdldHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdGltZVxuXG5jbGFzcyBGdWxsQ29udjNEKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIEMpOiBzdXBlcigpLl9faW5pdF9fKCk7IHNlbGYuY29udiA9IG5uLkNvbnYzZChDLCBDLCAzLCBwYWRkaW5nPTEpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6IHJldHVybiBzZWxmLmNvbnYoeClcblxuY2xhc3MgUHNldWRvM0Qobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTcGF0aWFsIDJEIGNvbnYgKyB0ZW1wb3JhbCAxRCBjb252LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBDKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuc3BhdGlhbCAgPSBubi5Db252M2QoQywgQywgKDEsMywzKSwgcGFkZGluZz0oMCwxLDEpKVxuICAgICAgICBzZWxmLnRlbXBvcmFsID0gbm4uQ29udjNkKEMsIEMsICgzLDEsMSksIHBhZGRpbmc9KDEsMCwwKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYudGVtcG9yYWwoc2VsZi5zcGF0aWFsKHgpKVxuXG5DLCBULCBILCBXID0gNjQsIDgsIDI4LCAyOFxueCA9IHRvcmNoLnJhbmRuKDIsIEMsIFQsIEgsIFcpXG5cbmZvciBuYW1lLCBtb2RlbCBpbiBbKFx1MDAyN0Z1bGwgM0RcdTAwMjcsIEZ1bGxDb252M0QoQykpLCAoXHUwMDI3UHNldWRvLTNEXHUwMDI3LCBQc2V1ZG8zRChDKSldOlxuICAgIHBhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKVxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBmb3IgXyBpbiByYW5nZSgxMCk6IF8gPSBtb2RlbCh4KVxuICAgIGVsYXBzZWQgPSAodGltZS50aW1lKCkgLSB0MCkgLyAxMCAqIDEwMDBcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMTJ9OiBwYXJhbXM9e3BhcmFtczosfSAgdGltZT17ZWxhcHNlZDouMWZ9bXNcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkNvbnYyRCArIExTVE0gdnMgQ29udjNEIGZvciBWaWRlbyIsImNvbnRlbnQiOiJDb252MkQrTFNUTSAoQ29udkxTVE0pIHByb2Nlc3NlcyBlYWNoIGZyYW1lIHdpdGggMkQgY29udiBhbmQgcHJvcGFnYXRlcyB0ZW1wb3JhbCBzdGF0ZSB0aHJvdWdoIExTVE0gY2VsbHMuIFRoaXMgaXMgYmV0dGVyIGZvciBsb25nIHZpZGVvcyB3aGVyZSB0ZW1wb3JhbCBkZXBlbmRlbmNpZXMgc3BhbiBtYW55IGZyYW1lcy4gQ29udjNEIGlzIGJldHRlciBmb3Igc2hvcnQgY2xpcHMgKDjigJMzMiBmcmFtZXMpIHdoZXJlIGxvY2FsIHNwYXRpby10ZW1wb3JhbCBwYXR0ZXJucyBtYXR0ZXIgKGUuZy4sIGRldGVjdGluZyBhIGhhbmQgZ2VzdHVyZSkuIEZvciB2ZXJ5IGxvbmcgdmlkZW9zLCBjb25zaWRlciBWaVQtYmFzZWQgYXBwcm9hY2hlcyB3aXRoIHRlbXBvcmFsIGF0dGVudGlvbiwgd2hpY2ggaGF2ZSBnbG9iYWwgcmVjZXB0aXZlIGZpZWxkcyBmcm9tIHRoZSBmaXJzdCBsYXllci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaGVuIHRvIFVzZSBFYWNoIERpbWVuc2lvbmFsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2hvaWNlIG9mIGNvbnYgZGltZW5zaW9uYWxpdHkgc2hvdWxkIG1hdGNoIHdoZXJlIGxvY2FsIHN0cnVjdHVyZSBleGlzdHMgaW4gdGhlIGRhdGEuIDFEIGlzIGJlc3QgZm9yIG9yZGVyZWQgc2VxdWVuY2VzIHdpdGggbG9jYWwgdGVtcG9yYWwvcG9zaXRpb25hbCBwYXR0ZXJucyBhbmQgbm8gaW5oZXJlbnQgMkQgc3RydWN0dXJlLiAyRCBpcyB0aGUgZGVmYXVsdCBmb3IgYW55IGdyaWQtbGlrZSBkYXRhIHdpdGggdHdvIHNwYXRpYWwgYXhlcy4gM0QgaXMgYXBwcm9wcmlhdGUgd2hlbiBhIHRoaXJkIGRpbWVuc2lvbiAodGltZSBvciBkZXB0aCkgaGFzIGxvY2FsIGNvcnJlbGF0aW9ucyB3aXRoIHRoZSBzcGF0aWFsIGRpbWVuc2lvbnMgc2ltdWx0YW5lb3VzbHksIG5vdCBqdXN0IHNlcXVlbnRpYWxseS4gVXNpbmcgM0QgY29udiBvbiBkYXRhIHdpdGggc3BhcnNlIHRlbXBvcmFsIHN0cnVjdHVyZSAoZS5nLiwgbG9uZyB2aWRlb3Mgd2l0aCBtb3N0bHkgc3RhdGljIHNjZW5lcykgd2FzdGVzIHBhcmFtZXRlcnM7IHBlci1mcmFtZSAyRCBjb252IGlzIG1vcmUgZWZmaWNpZW50LiBVc2luZyAxRCBjb252IG9uIGltYWdlcyB3b3VsZCBtaXNzIDJEIHNwYXRpYWwgc3RydWN0dXJlIGVudGlyZWx5LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJEaW1lbnNpb24iLCJJbnB1dCBTaGFwZSIsIktlcm5lbCBTaGFwZSIsIlN0cmlkZSBEaW1zIiwiUGFyYW1zICh2cyAyRCkiLCJNYWluIEFwcGxpY2F0aW9ucyJdLCJyb3dzIjpbWyJDb252MUQiLCIoTiwgQywgTCkiLCIoQ19vdXQsIENfaW4sIGspIiwiTCBvbmx5Iiwiay9rwrIgPSAxL2siLCJUaW1lIHNlcmllcywgYXVkaW8sIHRleHQsIDFEIHNpZ25hbHMiXSxbIkNvbnYyRCIsIihOLCBDLCBILCBXKSIsIihDX291dCwgQ19pbiwgaywgaykiLCJILCBXIiwiMcOXIChiYXNlbGluZSkiLCJJbWFnZXMsIHNwYXRpYWwgZmVhdHVyZSBtYXBzIl0sWyJDb252M0QiLCIoTiwgQywgRCwgSCwgVykiLCIoQ19vdXQsIENfaW4sIGssIGssIGspIiwiRCwgSCwgVyIsImvDlyBtb3JlIiwiVmlkZW8gY2xpcHMsIENUL01SSSB2b2x1bWVzIl0sWyJQc2V1ZG8tM0QiLCIoTiwgQywgVCwgSCwgVykiLCIxw5drw5drIHRoZW4ga8OXMcOXMSIsIkgsVyB0aGVuIFQiLCLiiYgxLzMgb2YgM0QiLCJFZmZpY2llbnQgdmlkZW8gdW5kZXJzdGFuZGluZyJdLFsiRGVwdGh3aXNlIDJEIiwiKE4sIEMsIEgsIFcpIiwiQyBrZXJuZWxzIG9mICgxLGssaykiLCJILCBXIiwiMS9DX291dCIsIk1vYmlsZSwgY2hhbm5lbC1pbmRlcGVuZGVudCBmZWF0dXJlcyJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJubi5Db252MWQgaW5wdXQgbXVzdCBiZSAoTiwgQywgTCkg4oCUIHJlc2hhcGUgKE4sIEwsIEMpIGlucHV0cyB3aXRoIC5wZXJtdXRlKDAsMiwxKSBiZWZvcmUgcGFzc2luZy4iLCJubi5Db252M2QgaXMgbWVtb3J5LWludGVuc2l2ZTogYSAzRCBmZWF0dXJlIG1hcCAoTiwyNTYsMTYsMTQsMTQpIHVzZXMgMy4yIEdCIGF0IGZsb2F0MzIgYmF0Y2g9OC4iLCJGb3IgbWVkaWNhbCBpbWFnaW5nLCBublUtTmV0IGF1dG8tY29uZmlndXJlcyAyRCB2cyAzRCBjb252IGJhc2VkIG9uIGRhdGFzZXQgYW5pc290cm9weSAoei1zcGFjaW5nKS4iLCJXYXZlTmV0IHVzZWQgY2F1c2FsIGRpbGF0ZWQgQ29udjFEIChtYXNrZWQgdG8gcHJldmVudCBmdXR1cmUgbGVha2FnZSkgZm9yIGF1dG9yZWdyZXNzaXZlIGF1ZGlvIHN5bnRoZXNpcy4iLCJUZXh0Q05OIChLaW0gMjAxNCk6IHRocmVlIENvbnYxRCB3aXRoIGtlcm5lbHMgWzMsNCw1XSwgZ2xvYmFsIG1heCBwb29sIHBlciBrZXJuZWwsIGNvbmNhdCDihpIgTUxQLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcnkgYW5kIFRocm91Z2hwdXQgQ29uc2lkZXJhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IjNEIGNvbnZvbHV0aW9ucyBhcmUgbWVtb3J5LWludGVuc2l2ZSBiZWNhdXNlIGFjdGl2YXRpb25zIGdyb3cgd2l0aCBEw5dIw5dXLiBBIHNpbmdsZSBsYXllciB3aXRoIEM9MjU2LCBUPTE2LCBIPTU2LCBXPTU2IHVzZXMgMjU2w5cxNsOXNTbDlzU2w5c0IGJ5dGVzIOKJiCAxLjYgR0IgYXQgZmxvYXQzMiBmb3Igb25lIHNhbXBsZS4gR3JhZGllbnQgY2hlY2twb2ludGluZyAocmVjb21wdXRpbmcgYWN0aXZhdGlvbnMgZHVyaW5nIGJhY2t3YXJkIHBhc3MpIHRyYWRlcyBjb21wdXRlIGZvciBtZW1vcnkg4oCUIGVzc2VudGlhbCBmb3IgdHJhaW5pbmcgZGVlcCB2aWRlbyBuZXR3b3Jrcy4gTWl4ZWQtcHJlY2lzaW9uIChmbG9hdDE2KSBoYWx2ZXMgYWN0aXZhdGlvbiBtZW1vcnkgd2l0aCBtaW5pbWFsIGFjY3VyYWN5IGxvc3MuIEZvciBpbmZlcmVuY2Ugb24gZWRnZSBkZXZpY2VzLCByZWR1Y2UgVCAoY2xpcCBsZW5ndGgpIGJlZm9yZSBDIChjaGFubmVsIHdpZHRoKSBzaW5jZSB0ZW1wb3JhbCBkaW1lbnNpb24gcmVkdWN0aW9uIGNvc3RzIGZld2VyIHBhcmFtZXRlcnMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXRjaCBzaXplIHNlbGVjdGlvbiBhbHNvIGRpZmZlcnMgYnkgY29udiB0eXBlOiAxRCBjb252IG5ldHdvcmtzIGNhbiB1c2UgbGFyZ2UgYmF0Y2hlcyAoZS5nLiwgMjU2KSBzaW5jZSBzZXF1ZW5jZSBpbnB1dHMgYXJlIGNvbXBhY3Q7IDNEIHZpZGVvIGNvbnYgbmV0d29ya3Mgb2Z0ZW4gcmVxdWlyZSBiYXRjaCBzaXplIDLigJM4IGV2ZW4gb24gaGlnaC1lbmQgR1BVcyBkdWUgdG8gYWN0aXZhdGlvbiBtZW1vcnkuIEdyYWRpZW50IGFjY3VtdWxhdGlvbiBvdmVyIG11bHRpcGxlIHNtYWxsIGJhdGNoZXMgc2ltdWxhdGVzIGxhcmdlciBlZmZlY3RpdmUgYmF0Y2ggc2l6ZXMgd2l0aG91dCBleGNlZWRpbmcgR1BVIG1lbW9yeSBsaW1pdHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQcm9maWxlIHdpdGggdG9yY2gucHJvZmlsZXIgdG8gaWRlbnRpZnkgd2hldGhlciAzRCBjb252IGlzIGNvbXB1dGUtYm91bmQgb3IgbWVtb3J5LWJhbmR3aWR0aC1ib3VuZC4iLCJGb3IgM0QgY29udiBvbiB2aWRlbywgY29uc2lkZXIgdGVtcG9yYWwgc3RyaWRpbmcgKHN0cmlkZT0oMiwxLDEpKSB0byByZWR1Y2UgdGltZSBkaW1lbnNpb24gY2hlYXBseS4iLCJDb252MWQgaXMgZXF1aXZhbGVudCB0byBDb252MmQgd2l0aCBoZWlnaHQ9MSDigJQgeW91IGNhbiBpbXBsZW1lbnQgMUQgY29udiB1c2luZyAyRCBwcmltaXRpdmVzIGlmIG5lZWRlZC4iLCJUZW1wb3JhbFNoaWZ0IE1vZHVsZSAoVFNNKTogc2hpZnRzIGEgZnJhY3Rpb24gb2YgY2hhbm5lbHMgYWxvbmcgdGhlIHRpbWUgYXhpcyDigJQgemVyby1wYXJhbWV0ZXIgdGVtcG9yYWwgbW9kZWxsaW5nIGJ1aWx0IG9uIDJEIGNvbnYuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# 1D, 2D, and 3D Convolutions — Applications for Each

Convolution generalises naturally across dimensionalities: 1D slides a kernel along a single axis (time or sequence length), 2D slides over a spatial plane (height × width), and 3D slides over a volume (depth × height × width or time × height × width). Choosing the right dimensionality is not arbitrary — it encodes a structural assumption about where local correlations exist in the data, and matching that assumption to the true data geometry is the first architectural decision for any CNN design.

## 1D Convolution — Sequences, Audio, and Time Series

nn.Conv1d takes input of shape (N, C, L) — batch, channels, length — and produces output (N, C_out, L_out). The kernel slides along the L dimension only. Applications: time-series classification (ECG, accelerometer), audio waveform modelling (WaveNet stacks dilated 1D convs to achieve receptive fields of thousands of samples), text classification (TextCNN applies multiple kernel sizes like 3, 4, 5 then max-pools), and position mixing in hybrid models. 1D conv is much faster than RNNs for fixed-context tasks and fully parallelisable during training. WaveNet achieved state-of-the-art text-to-speech by stacking 30 dilated 1D conv layers with dilation rates [1,2,4,...,512] repeated.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ECGClassifier(nn.Module):
    """1D CNN for time-series (ECG) classification."""
    def __init__(self, n_classes=5):
        super().__init__()
        self.conv1 = nn.Conv1d(1, 32, kernel_size=7, padding=3)   # (N,32,L)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=5, padding=2)  # (N,64,L)
        self.conv3 = nn.Conv1d(64, 128, kernel_size=3, padding=1) # (N,128,L)
        self.pool  = nn.AdaptiveAvgPool1d(1)                       # (N,128,1)
        self.fc    = nn.Linear(128, n_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool1d(x, 2)          # halve sequence length
        x = F.relu(self.conv2(x))
        x = F.max_pool1d(x, 2)
        x = F.relu(self.conv3(x))
        x = self.pool(x).squeeze(-1)    # global avg pool -> (N,128)
        return self.fc(x)

model = ECGClassifier()
x = torch.randn(8, 1, 256)  # 8 ECG traces, single lead, 256 timesteps
out = model(x)
print(f'Input:  {tuple(x.shape)}')
print(f'Output: {tuple(out.shape)}')
params = sum(p.numel() for p in model.parameters())
print(f'Total params: {params:,}')
```

## 2D Convolution — Images and Spatial Feature Maps

nn.Conv2d takes input (N, C, H, W) and is the standard building block for image tasks. It slides the kernel over two spatial dimensions simultaneously, learning translation-equivariant feature detectors. Virtually all image classification, detection, and segmentation networks (VGG, ResNet, EfficientNet, YOLO, Mask R-CNN) are built on 2D conv. The key design choices are: how many channels (width), how deep to go (depth), where to downsample (stride or pool), and what kernel sizes to use. The trend since 2015 has been toward all-3×3 kernels (VGG insight: two 3×3 convs have the same RF as one 5×5 but fewer parameters), skip connections (ResNet), and depthwise separable convs (MobileNet).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SmallImageCNN(nn.Module):
    """Compact 2D CNN for CIFAR-10 (32x32 input)."""
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.MaxPool2d(2),                 # 32->16
            nn.Conv2d(64, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(),
            nn.Conv2d(128, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(),
            nn.MaxPool2d(2),                 # 16->8
            nn.Conv2d(128, 256, 3, padding=1), nn.BatchNorm2d(256), nn.ReLU(),
        )
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        return self.head(self.features(x))

model = SmallImageCNN()
x = torch.randn(4, 3, 32, 32)
out = model(x)
print(f'Input: {tuple(x.shape)} -> Output: {tuple(out.shape)}')
print(f'Params: {sum(p.numel() for p in model.parameters()):,}')
```

## 3D Convolution — Video and Volumetric Data

nn.Conv3d takes input (N, C, D, H, W) where D is depth (time frames for video, z-slices for medical imaging). It applies a 3D kernel that slides over all three spatial/temporal axes simultaneously, learning spatio-temporal features. C3D (Tran et al., 2015) used 3×3×3 kernels throughout for action recognition. I3D inflated ImageNet-pretrained 2D conv weights into 3D by repeating them along the temporal axis. For medical imaging (CT, MRI), 3D conv captures inter-slice relationships that 2D slice-by-slice processing misses.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class VideoClipCNN(nn.Module):
    """Minimal 3D CNN for short video clip classification."""
    def __init__(self, num_classes=101):
        super().__init__()
        # Input: (N, 3, T, H, W) e.g. (N, 3, 16, 112, 112)
        self.conv1 = nn.Conv3d(3,  64, kernel_size=(3,3,3), padding=1)
        self.conv2 = nn.Conv3d(64, 128, kernel_size=(3,3,3), padding=1)
        self.conv3 = nn.Conv3d(128, 256, kernel_size=(3,3,3), padding=1)
        self.pool  = nn.AdaptiveAvgPool3d(1)
        self.fc    = nn.Linear(256, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool3d(x, kernel_size=(1,2,2))  # only pool spatial
        x = F.relu(self.conv2(x))
        x = F.max_pool3d(x, kernel_size=(2,2,2))
        x = F.relu(self.conv3(x))
        x = self.pool(x).squeeze(-1).squeeze(-1).squeeze(-1)
        return self.fc(x)

model = VideoClipCNN()
x = torch.randn(2, 3, 16, 112, 112)  # 2 clips, 16 frames, 112x112
out = model(x)
print(f'Input : {tuple(x.shape)}')
print(f'Output: {tuple(out.shape)}')
print(f'Params: {sum(p.numel() for p in model.parameters()):,}')
```

## Pseudo-3D Convolution — Factorising for Efficiency

Full 3D conv has k³ parameters per filter position. Pseudo-3D (P3D, Qiu et al. 2017) factorises a 3×3×3 conv into a spatial 3×3 (2D, no temporal mixing) followed by a temporal 1×1×3 (1D along time, no spatial mixing). This reduces parameters from k³×C_in×C_out to (k²+k)×C_in×C_out ≈ 3.4× fewer for k=3, with comparable accuracy on action recognition benchmarks. (2+1)D conv (R(2+1)D, Tran et al. 2018) adds a nonlinearity between the two factors, further improving expressivity. These factored designs make 3D-conv-based video understanding practical on standard GPU budgets.

```python
import torch
import torch.nn as nn
import time

class FullConv3D(nn.Module):
    def __init__(self, C): super().__init__(); self.conv = nn.Conv3d(C, C, 3, padding=1)
    def forward(self, x): return self.conv(x)

class Pseudo3D(nn.Module):
    """Spatial 2D conv + temporal 1D conv."""
    def __init__(self, C):
        super().__init__()
        self.spatial  = nn.Conv3d(C, C, (1,3,3), padding=(0,1,1))
        self.temporal = nn.Conv3d(C, C, (3,1,1), padding=(1,0,0))
    def forward(self, x):
        return self.temporal(self.spatial(x))

C, T, H, W = 64, 8, 28, 28
x = torch.randn(2, C, T, H, W)

for name, model in [('Full 3D', FullConv3D(C)), ('Pseudo-3D', Pseudo3D(C))]:
    params = sum(p.numel() for p in model.parameters())
    t0 = time.time()
    for _ in range(10): _ = model(x)
    elapsed = (time.time() - t0) / 10 * 1000
    print(f'{name:<12}: params={params:,}  time={elapsed:.1f}ms')
```

> **Conv2D + LSTM vs Conv3D for Video**: Conv2D+LSTM (ConvLSTM) processes each frame with 2D conv and propagates temporal state through LSTM cells. This is better for long videos where temporal dependencies span many frames. Conv3D is better for short clips (8–32 frames) where local spatio-temporal patterns matter (e.g., detecting a hand gesture). For very long videos, consider ViT-based approaches with temporal attention, which have global receptive fields from the first layer.

## When to Use Each Dimensionality

The choice of conv dimensionality should match where local structure exists in the data. 1D is best for ordered sequences with local temporal/positional patterns and no inherent 2D structure. 2D is the default for any grid-like data with two spatial axes. 3D is appropriate when a third dimension (time or depth) has local correlations with the spatial dimensions simultaneously, not just sequentially. Using 3D conv on data with sparse temporal structure (e.g., long videos with mostly static scenes) wastes parameters; per-frame 2D conv is more efficient. Using 1D conv on images would miss 2D spatial structure entirely.

| Dimension | Input Shape | Kernel Shape | Stride Dims | Params (vs 2D) | Main Applications |
| --- | --- | --- | --- | --- | --- |
| Conv1D | (N, C, L) | (C_out, C_in, k) | L only | k/k² = 1/k | Time series, audio, text, 1D signals |
| Conv2D | (N, C, H, W) | (C_out, C_in, k, k) | H, W | 1× (baseline) | Images, spatial feature maps |
| Conv3D | (N, C, D, H, W) | (C_out, C_in, k, k, k) | D, H, W | k× more | Video clips, CT/MRI volumes |
| Pseudo-3D | (N, C, T, H, W) | 1×k×k then k×1×1 | H,W then T | ≈1/3 of 3D | Efficient video understanding |
| Depthwise 2D | (N, C, H, W) | C kernels of (1,k,k) | H, W | 1/C_out | Mobile, channel-independent features |

- nn.Conv1d input must be (N, C, L) — reshape (N, L, C) inputs with .permute(0,2,1) before passing.
- nn.Conv3d is memory-intensive: a 3D feature map (N,256,16,14,14) uses 3.2 GB at float32 batch=8.
- For medical imaging, nnU-Net auto-configures 2D vs 3D conv based on dataset anisotropy (z-spacing).
- WaveNet used causal dilated Conv1D (masked to prevent future leakage) for autoregressive audio synthesis.
- TextCNN (Kim 2014): three Conv1D with kernels [3,4,5], global max pool per kernel, concat → MLP.

## Memory and Throughput Considerations

3D convolutions are memory-intensive because activations grow with D×H×W. A single layer with C=256, T=16, H=56, W=56 uses 256×16×56×56×4 bytes ≈ 1.6 GB at float32 for one sample. Gradient checkpointing (recomputing activations during backward pass) trades compute for memory — essential for training deep video networks. Mixed-precision (float16) halves activation memory with minimal accuracy loss. For inference on edge devices, reduce T (clip length) before C (channel width) since temporal dimension reduction costs fewer parameters.

Batch size selection also differs by conv type: 1D conv networks can use large batches (e.g., 256) since sequence inputs are compact; 3D video conv networks often require batch size 2–8 even on high-end GPUs due to activation memory. Gradient accumulation over multiple small batches simulates larger effective batch sizes without exceeding GPU memory limits.

- Profile with torch.profiler to identify whether 3D conv is compute-bound or memory-bandwidth-bound.
- For 3D conv on video, consider temporal striding (stride=(2,1,1)) to reduce time dimension cheaply.
- Conv1d is equivalent to Conv2d with height=1 — you can implement 1D conv using 2D primitives if needed.
- TemporalShift Module (TSM): shifts a fraction of channels along the time axis — zero-parameter temporal modelling built on 2D conv.

---

