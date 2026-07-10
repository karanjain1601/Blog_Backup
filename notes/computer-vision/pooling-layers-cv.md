---
title: "Pooling Layers in CNNs"
slug: "pooling-layers-cv"
description: "Max pooling, average pooling, global average pooling, adaptive pooling, and spatial pyramid pooling — their functions, implementation, and role in building translation-invariant features."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQb29saW5nIGxheWVycyBwcm9ncmVzc2l2ZWx5IHJlZHVjZSBzcGF0aWFsIGRpbWVuc2lvbnMgaW4gYSBDTk4sIGRlY3JlYXNpbmcgY29tcHV0YXRpb24gYW5kIG1lbW9yeSB3aGlsZSBidWlsZGluZyBoaWVyYXJjaGljYWwgZmVhdHVyZSByZXByZXNlbnRhdGlvbnMuIFVubGlrZSBjb252b2x1dGlvbiwgcG9vbGluZyBoYXMgbm8gbGVhcm5hYmxlIHBhcmFtZXRlcnMg4oCUIGl0IGFwcGxpZXMgYSBmaXhlZCBhZ2dyZWdhdGlvbiBmdW5jdGlvbiBvdmVyIGEgbG9jYWwgd2luZG93LiBUaGUgdHdvIHByaW1hcnkgb3BlcmF0aW9ucyBhcmUgbWF4IHBvb2xpbmcgKHJldGFpbnMgc3Ryb25nZXN0IGFjdGl2YXRpb24pIGFuZCBhdmVyYWdlIHBvb2xpbmcgKGNvbXB1dGVzIHNwYXRpYWwgbWVhbikuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQb29saW5nIHByb3ZpZGVzIGEgZGVncmVlIG9mIHRyYW5zbGF0aW9uIGludmFyaWFuY2U6IHNtYWxsIHNoaWZ0cyBpbiB0aGUgaW5wdXQgcHJvZHVjZSB0aGUgc2FtZSBwb29sZWQgb3V0cHV0IHdoZW4gdGhlIGRvbWluYW50IGFjdGl2YXRpb24gc3RheXMgd2l0aGluIHRoZSBwb29saW5nIHdpbmRvdy4gVGhpcyBpcyBkZXNpcmFibGUgZm9yIGNsYXNzaWZpY2F0aW9uIHRhc2tzIHdoZXJlIHRoZSBhYnNvbHV0ZSBwb3NpdGlvbiBvZiBhIGZlYXR1cmUgbWF0dGVycyBsZXNzIHRoYW4gaXRzIHByZXNlbmNlLiBQb29saW5nIGFsc28gYWN0cyBhcyBhIGZvcm0gb2YgaW1wbGljaXQgcmVndWxhcml6YXRpb24gYnkgZGlzY2FyZGluZyBwcmVjaXNlIHNwYXRpYWwgaW5mb3JtYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWF4IFBvb2xpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1heCBwb29saW5nIHNlbGVjdHMgdGhlIG1heGltdW0gdmFsdWUgd2l0aGluIGVhY2ggcG9vbGluZyB3aW5kb3csIHJldGFpbmluZyB0aGUgc3Ryb25nZXN0IGFjdGl2YXRpb24gaW4gZWFjaCBsb2NhbCByZWdpb24uIEl0IGRpc2NhcmRzIHByZWNpc2UgbG9jYXRpb24gaW5mb3JtYXRpb24gYnV0IHByZXNlcnZlcyB0aGUgcHJlc2VuY2Ugb2YgZGV0ZWN0ZWQgZmVhdHVyZXMuIEEgMsOXMiBtYXggcG9vbCB3aXRoIHN0cmlkZSAyIGhhbHZlcyBib3RoIHNwYXRpYWwgZGltZW5zaW9ucy4gTWF4IHBvb2xpbmcgaXMgbW9yZSBjb21tb24gdGhhbiBhdmVyYWdlIHBvb2xpbmcgaW4gY2xhc3NpZmljYXRpb24gbmV0d29ya3MgYmVjYXVzZSByZXRhaW5pbmcgdGhlIG1heGltdW0gYWN0aXZhdGlvbiBhbGlnbnMgd2l0aCBkZXRlY3Rpbmcgd2hldGhlciBhIGZlYXR1cmUgaXMgcHJlc2VudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxueCA9IHRvcmNoLnJhbmRuKDIsIDE2LCAzMiwgMzIpICAjIFtCLCBDLCBILCBXXVxuXG4jIE1heCBwb29sOiAyeDIgd2luZG93LCBzdHJpZGUgMlxubWF4X3Bvb2wgPSBubi5NYXhQb29sMmQoa2VybmVsX3NpemU9Miwgc3RyaWRlPTIpXG5tYXhfb3V0ID0gbWF4X3Bvb2woeClcbnByaW50KFwiTWF4UG9vbDJkIG91dHB1dDpcIiwgbWF4X291dC5zaGFwZSkgICMgWzIsIDE2LCAxNiwgMTZdXG5cbiMgQXZlcmFnZSBwb29sOiAyeDIgd2luZG93LCBzdHJpZGUgMlxuYXZnX3Bvb2wgPSBubi5BdmdQb29sMmQoa2VybmVsX3NpemU9Miwgc3RyaWRlPTIpXG5hdmdfb3V0ID0gYXZnX3Bvb2woeClcbnByaW50KFwiQXZnUG9vbDJkIG91dHB1dDpcIiwgYXZnX291dC5zaGFwZSkgICMgWzIsIDE2LCAxNiwgMTZdXG5cbiMgV2l0aCBwYWRkaW5nXG5tYXhfcGFkID0gbm4uTWF4UG9vbDJkKGtlcm5lbF9zaXplPTMsIHN0cmlkZT0yLCBwYWRkaW5nPTEpXG5wcmludChcIk1heFBvb2wgcGFkZGVkOlwiLCBtYXhfcGFkKHgpLnNoYXBlKSAjIFsyLCAxNiwgMTYsIDE2XSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF2ZXJhZ2UgUG9vbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXZlcmFnZSBwb29saW5nIGNvbXB1dGVzIHRoZSBtZWFuIG92ZXIgdGhlIHBvb2xpbmcgd2luZG93LCBwcm9kdWNpbmcgc21vb3RoZXIgZmVhdHVyZSBtYXBzIHRoYW4gbWF4IHBvb2xpbmcuIEl0IGlzIGxlc3MgYWdncmVzc2l2ZSBhYm91dCBkaXNjYXJkaW5nIGluZm9ybWF0aW9uIGFuZCBjYW4gYmUgcHJlZmVyYWJsZSBmb3IgdGFza3MgbGlrZSB0ZXh0dXJlIHJlY29nbml0aW9uIHdoZXJlIHRoZSBkZW5zaXR5IG9mIGFjdGl2YXRpb25zIG1hdHRlcnMuIEF2ZXJhZ2UgcG9vbGluZyBpcyBzb21ldGltZXMgdXNlZCBpbiB0aGUgbGF0ZXIgbGF5ZXJzIG9mIGEgbmV0d29yayB3aGVyZSBmZWF0dXJlcyByZXByZXNlbnQgYnJvYWRlciBjb25jZXB0cyByYXRoZXIgdGhhbiBzaGFycCBsb2NhbCBkZXRlY3RvcnMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHNwZWNpYWwgY2FzZSBpcyBmcmFjdGlvbmFsIG1heCBwb29saW5nLCB3aGljaCB1c2VzIG5vbi1pbnRlZ2VyIHN0cmlkZXMgdG8gcHJvZHVjZSBvdXRwdXQgc2l6ZXMgdGhhdCBhcmUgbm90IGV4YWN0IGhhbHZlcy4gUHlUb3JjaCBwcm92aWRlcyBubi5GcmFjdGlvbmFsTWF4UG9vbDJkIGZvciB0aGlzLiBBbm90aGVyIHZhcmlhbnQsIHN0b2NoYXN0aWMgcG9vbGluZywgcmFuZG9tbHkgc2FtcGxlcyBmcm9tIHRoZSBwb29saW5nIHdpbmRvdyB3ZWlnaHRlZCBieSBhY3RpdmF0aW9uIG1hZ25pdHVkZXMgZHVyaW5nIHRyYWluaW5nLCBwcm92aWRpbmcgaW1wbGljaXQgcmVndWxhcml6YXRpb24gc2ltaWxhciB0byBkcm9wb3V0IGZvciBzcGF0aWFsIGZlYXR1cmUgbWFwcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHbG9iYWwgQXZlcmFnZSBQb29saW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHbG9iYWwgYXZlcmFnZSBwb29saW5nIChHQVApIGNvbGxhcHNlcyB0aGUgZW50aXJlIHNwYXRpYWwgZGltZW5zaW9uIG9mIGVhY2ggY2hhbm5lbCBpbnRvIGEgc2luZ2xlIHZhbHVlIGJ5IGF2ZXJhZ2luZyBhbGwgYWN0aXZhdGlvbnMuIEZvciBhIGZlYXR1cmUgbWFwIG9mIHNoYXBlIFtCLCBDLCBILCBXXSwgR0FQIHByb2R1Y2VzIFtCLCBDXS4gVGhpcyBlbGltaW5hdGVzIHRoZSBuZWVkIGZvciBmbGF0dGVuaW5nIGFuZCBsYXJnZSBmdWxseSBjb25uZWN0ZWQgbGF5ZXJzLCBkcmFtYXRpY2FsbHkgcmVkdWNpbmcgcGFyYW1ldGVycyBhbmQgb3ZlcmZpdHRpbmcgcmlzay4gR0FQIHdhcyBpbnRyb2R1Y2VkIGluIE5ldHdvcmstaW4tTmV0d29yayBhbmQgcG9wdWxhcml6ZWQgYnkgUmVzTmV0XHUwMDI3cyBjbGFzc2lmaWVyIGhlYWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbiMgU2ltdWxhdGUgZmVhdHVyZSBtYXBzIG9mIHZhcmlvdXMgc3BhdGlhbCBzaXplc1xuZm9yIEgsIFcgaW4gWyg3LCA3KSwgKDE0LCAxNCksICgyOCwgMjgpXTpcbiAgICB4ID0gdG9yY2gucmFuZG4oNCwgNTEyLCBILCBXKSAgIyBbQiwgQywgSCwgV11cblxuICAgICMgQWRhcHRpdmVBdmdQb29sMmQoKDEsMSkpID0gZ2xvYmFsIGF2ZXJhZ2UgcG9vbFxuICAgIGdhcCA9IG5uLkFkYXB0aXZlQXZnUG9vbDJkKCgxLCAxKSlcbiAgICBvdXQgPSBnYXAoeClcbiAgICBwcmludChmXCJJbnB1dCB7SH14e1d9IC1cdTAwM2UgR0FQIG91dHB1dDoge291dC5zaGFwZX1cIilcbiAgICAjIEFsd2F5cyBbNCwgNTEyLCAxLCAxXSByZWdhcmRsZXNzIG9mIGlucHV0IEgsV1xuXG4jIEZsYXR0ZW4gZm9yIGNsYXNzaWZpZXJcbm91dF9mbGF0ID0gb3V0LmZsYXR0ZW4oMSlcbnByaW50KFwiRmxhdHRlbmVkOlwiLCBvdXRfZmxhdC5zaGFwZSkgICMgWzQsIDUxMl0ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsImNvbnRlbnQiOiJHbG9iYWwgYXZlcmFnZSBwb29saW5nIGJlZm9yZSB0aGUgY2xhc3NpZmllciBpcyBtb3JlIHJvYnVzdCB0byBzcGF0aWFsIHRyYW5zbGF0aW9ucyBhbmQgdXNlcyBmYXIgZmV3ZXIgcGFyYW1ldGVycyB0aGFuIGEgZnVsbHktY29ubmVjdGVkIGxheWVyIOKAlCBwcmVmZXIgaXQgZm9yIGNsYXNzaWZpY2F0aW9uIGhlYWRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFkYXB0aXZlIGFuZCBTcGF0aWFsIFB5cmFtaWQgUG9vbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWRhcHRpdmUgcG9vbGluZyBhdXRvbWF0aWNhbGx5IGNvbXB1dGVzIGtlcm5lbCBzaXplIGFuZCBzdHJpZGUgdG8gcHJvZHVjZSBhbnkgdGFyZ2V0IG91dHB1dCBzaXplIGZyb20gYW55IGlucHV0IHNpemUuIG5uLkFkYXB0aXZlQXZnUG9vbDJkKChIX291dCwgV19vdXQpKSBtYWtlcyBhcmNoaXRlY3R1cmVzIGlucHV0LXNpemUgYWdub3N0aWMsIHdoaWNoIGlzIGVzc2VudGlhbCBmb3IgdHJhbnNmZXIgbGVhcm5pbmcgb24gaW1hZ2VzIG9mIGRpZmZlcmVudCByZXNvbHV0aW9ucy4gU3BhdGlhbCBweXJhbWlkIHBvb2xpbmcgKFNQUCkgdGFrZXMgdGhpcyBmdXJ0aGVyIGJ5IHBvb2xpbmcgYXQgbXVsdGlwbGUgc2NhbGVzIHNpbXVsdGFuZW91c2x5IGFuZCBjb25jYXRlbmF0aW5nIHRoZSByZXN1bHRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBTcGF0aWFsUHlyYW1pZFBvb2wobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbGV2ZWxzPSgxLCAyLCA0KSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBvb2xzID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBubi5BZGFwdGl2ZUF2Z1Bvb2wyZCgobCwgbCkpIGZvciBsIGluIGxldmVsc1xuICAgICAgICBdKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIEIsIEMsIF8sIF8gPSB4LnNoYXBlXG4gICAgICAgIHBhcnRzID0gW3AoeCkuZmxhdHRlbigyKSBmb3IgcCBpbiBzZWxmLnBvb2xzXSAgIyBbQixDLGwqbF1cbiAgICAgICAgcmV0dXJuIHRvcmNoLmNhdChwYXJ0cywgZGltPTIpLmZsYXR0ZW4oMSkgICAgICAgIyBbQiwgQyooMSs0KzE2KV1cblxuc3BwID0gU3BhdGlhbFB5cmFtaWRQb29sKGxldmVscz0oMSwgMiwgNCkpXG54ID0gdG9yY2gucmFuZG4oMiwgNjQsIDEzLCAxMylcbnByaW50KHNwcCh4KS5zaGFwZSkgICMgWzIsIDY0KigxKzQrMTYpXSA9IFsyLCAxMzQ0XSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIHJvaV9wb29sKGZlYXQsIGJveCwgb3V0X3NpemU9Nyk6XG4gICAgXCJcIlwiU2ltcGxpZmllZCBSb0kgcG9vbGluZzogcG9vbCBmZWF0dXJlIG1hcCByZWdpb24gdG8gZml4ZWQgb3V0X3NpemUgeCBvdXRfc2l6ZS5cIlwiXCJcbiAgICB4MSwgeTEsIHgyLCB5MiA9IGJveFxuICAgIHJlZ2lvbiA9IGZlYXRbOiwgOiwgeTE6eTIsIHgxOngyXSAgIyBDcm9wIHJlZ2lvblxuICAgIHJldHVybiBGLmFkYXB0aXZlX21heF9wb29sMmQocmVnaW9uLCAob3V0X3NpemUsIG91dF9zaXplKSlcblxuZmVhdCA9IHRvcmNoLnJhbmRuKDEsIDI1NiwgMzIsIDMyKSAgICMgRmVhdHVyZSBtYXBcbmJveCA9ICg0LCA0LCAyMCwgMjApICAgICAgICAgICAgICAgICAgIyBSZWdpb24gb2YgaW50ZXJlc3QgKHgxLHkxLHgyLHkyKVxucG9vbGVkID0gcm9pX3Bvb2woZmVhdCwgYm94LCBvdXRfc2l6ZT03KVxucHJpbnQoXCJSb0kgcG9vbGVkIHNoYXBlOlwiLCBwb29sZWQuc2hhcGUpICAjIFsxLCAyNTYsIDcsIDddIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlBvb2xpbmcgVHlwZSIsIkRvd25zYW1wbGluZyIsIkluZm8gTG9zcyIsIlRyYW5zbGF0aW9uIEludmFyaWFuY2UiLCJDb21tb24gVXNlIl0sInJvd3MiOltbIk1heCBwb29sIiwiWWVzIChzdHJpZGXiiaUyKSIsIkxvc2VzIHBvc2l0aW9uIHdpdGhpbiB3aW5kb3ciLCJTdHJvbmciLCJDbGFzc2lmaWNhdGlvbiBiYWNrYm9uZXMgKFZHRywgUmVzTmV0KSJdLFsiQXZnIHBvb2wiLCJZZXMgKHN0cmlkZeKJpTIpIiwiRGlsdXRlcyBwZWFrIGFjdGl2YXRpb25zIiwiTW9kZXJhdGUiLCJUZXh0dXJlIGZlYXR1cmVzLCBsYXRlciBzdGFnZXMiXSxbIkdsb2JhbCBhdmcgcG9vbCIsIkZ1bGwgc3BhdGlhbCBjb2xsYXBzZSIsIkxvc2VzIGFsbCBzcGF0aWFsIGluZm8iLCJDb21wbGV0ZSIsIkNsYXNzaWZpY2F0aW9uIGhlYWQgKFJlc05ldCwgTW9iaWxlTmV0KSJdLFsiQWRhcHRpdmUgcG9vbCIsIlRvIGFueSB0YXJnZXQgc2l6ZSIsIlZhcmlhYmxlIiwiU2l6ZS1hZ25vc3RpYyIsIlRyYW5zZmVyIGxlYXJuaW5nLCBmbGV4aWJsZSBhcmNoaXRlY3R1cmVzIl0sWyJTUFAiLCJNdWx0aS1zY2FsZSBjb2xsYXBzZSIsIlBhcnRpYWwgcGVyIHNjYWxlIiwiTXVsdGktc2NhbGUiLCJPYmplY3QgZGV0ZWN0aW9uIChTUFBOZXQsIEZhc3RlciBSLUNOTikiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1heCBwb29saW5nIGlzIHRoZSBkZWZhdWx0IGZvciBjbGFzc2lmaWNhdGlvbiBiYWNrYm9uZXM7IGl0IGlzIGFnZ3Jlc3NpdmUgYnV0IHByZXNlcnZlcyBzYWxpZW50IGFjdGl2YXRpb25zLiBHbG9iYWwgYXZlcmFnZSBwb29saW5nIHJlcGxhY2VzIGZsYXR0ZW4rRkMgaW4gbW9kZXJuIGNsYXNzaWZpZXIgaGVhZHMsIHJlZHVjaW5nIHBhcmFtZXRlcnMgYnkgb3JkZXJzIG9mIG1hZ25pdHVkZS4gQWRhcHRpdmUgcG9vbGluZyBtYWtlcyBuZXR3b3JrcyBpbnB1dC1zaXplIGFnbm9zdGljIOKAlCBlc3NlbnRpYWwgZm9yIGZpbmUtdHVuaW5nIG9uIGRpZmZlcmVudCByZXNvbHV0aW9ucy4gU3BhdGlhbCBweXJhbWlkIHBvb2xpbmcgZW5hYmxlcyBmaXhlZC1zaXplIHJlcHJlc2VudGF0aW9ucyBmcm9tIHZhcmlhYmxlLXNpemUgaW5wdXRzLCBjcml0aWNhbCBmb3IgZGV0ZWN0aW9uLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9kZXJuIGFyY2hpdGVjdHVyZXMgYXJlIG1vdmluZyBhd2F5IGZyb20gZXhwbGljaXQgcG9vbGluZyB0b3dhcmQgc3RyaWRlLTIgY29udm9sdXRpb25zIGZvciBkb3duc2FtcGxpbmcsIHdoaWNoIGFyZSBsZWFybmFibGUgYW5kIGNhbiBiZSBtb3JlIGV4cHJlc3NpdmUuIEhvd2V2ZXIsIHBvb2xpbmcgcmVtYWlucyBpbXBvcnRhbnQgaW4gZGV0ZWN0aW9uIGhlYWRzIChSb0kgcG9vbGluZywgUm9JIGFsaWduKSBhbmQgZ2xvYmFsIGZlYXR1cmUgYWdncmVnYXRpb24uIFVuZGVyc3RhbmRpbmcgd2hpY2ggcG9vbGluZyB2YXJpYW50IHRvIHVzZSBhbmQgd2hlcmUgaW4gdGhlIG5ldHdvcmsgYXJjaGl0ZWN0dXJlIHJlcXVpcmVzIGJhbGFuY2luZyBzcGF0aWFsIHJlc29sdXRpb24sIGNvbXB1dGUgY29zdCwgYW5kIHRoZSBuZWVkcyBvZiB0aGUgZG93bnN0cmVhbSB0YXNrLiJ9XQ=="
---
# Pooling Layers in CNNs

## Overview

Pooling layers progressively reduce spatial dimensions in a CNN, decreasing computation and memory while building hierarchical feature representations. Unlike convolution, pooling has no learnable parameters — it applies a fixed aggregation function over a local window. The two primary operations are max pooling (retains strongest activation) and average pooling (computes spatial mean).

Pooling provides a degree of translation invariance: small shifts in the input produce the same pooled output when the dominant activation stays within the pooling window. This is desirable for classification tasks where the absolute position of a feature matters less than its presence. Pooling also acts as a form of implicit regularization by discarding precise spatial information.

## Max Pooling

Max pooling selects the maximum value within each pooling window, retaining the strongest activation in each local region. It discards precise location information but preserves the presence of detected features. A 2×2 max pool with stride 2 halves both spatial dimensions. Max pooling is more common than average pooling in classification networks because retaining the maximum activation aligns with detecting whether a feature is present.

```python
import torch
import torch.nn as nn

x = torch.randn(2, 16, 32, 32)  # [B, C, H, W]

# Max pool: 2x2 window, stride 2
max_pool = nn.MaxPool2d(kernel_size=2, stride=2)
max_out = max_pool(x)
print("MaxPool2d output:", max_out.shape)  # [2, 16, 16, 16]

# Average pool: 2x2 window, stride 2
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)
avg_out = avg_pool(x)
print("AvgPool2d output:", avg_out.shape)  # [2, 16, 16, 16]

# With padding
max_pad = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
print("MaxPool padded:", max_pad(x).shape) # [2, 16, 16, 16]
```

## Average Pooling

Average pooling computes the mean over the pooling window, producing smoother feature maps than max pooling. It is less aggressive about discarding information and can be preferable for tasks like texture recognition where the density of activations matters. Average pooling is sometimes used in the later layers of a network where features represent broader concepts rather than sharp local detectors.

A special case is fractional max pooling, which uses non-integer strides to produce output sizes that are not exact halves. PyTorch provides nn.FractionalMaxPool2d for this. Another variant, stochastic pooling, randomly samples from the pooling window weighted by activation magnitudes during training, providing implicit regularization similar to dropout for spatial feature maps.

## Global Average Pooling

Global average pooling (GAP) collapses the entire spatial dimension of each channel into a single value by averaging all activations. For a feature map of shape [B, C, H, W], GAP produces [B, C]. This eliminates the need for flattening and large fully connected layers, dramatically reducing parameters and overfitting risk. GAP was introduced in Network-in-Network and popularized by ResNet's classifier head.

```python
import torch
import torch.nn as nn

# Simulate feature maps of various spatial sizes
for H, W in [(7, 7), (14, 14), (28, 28)]:
    x = torch.randn(4, 512, H, W)  # [B, C, H, W]

    # AdaptiveAvgPool2d((1,1)) = global average pool
    gap = nn.AdaptiveAvgPool2d((1, 1))
    out = gap(x)
    print(f"Input {H}x{W} -> GAP output: {out.shape}")
    # Always [4, 512, 1, 1] regardless of input H,W

# Flatten for classifier
out_flat = out.flatten(1)
print("Flattened:", out_flat.shape)  # [4, 512]
```

> **tip**: Global average pooling before the classifier is more robust to spatial translations and uses far fewer parameters than a fully-connected layer — prefer it for classification heads.

## Adaptive and Spatial Pyramid Pooling

Adaptive pooling automatically computes kernel size and stride to produce any target output size from any input size. nn.AdaptiveAvgPool2d((H_out, W_out)) makes architectures input-size agnostic, which is essential for transfer learning on images of different resolutions. Spatial pyramid pooling (SPP) takes this further by pooling at multiple scales simultaneously and concatenating the results.

```python
import torch
import torch.nn as nn

class SpatialPyramidPool(nn.Module):
    def __init__(self, levels=(1, 2, 4)):
        super().__init__()
        self.pools = nn.ModuleList([
            nn.AdaptiveAvgPool2d((l, l)) for l in levels
        ])

    def forward(self, x):
        B, C, _, _ = x.shape
        parts = [p(x).flatten(2) for p in self.pools]  # [B,C,l*l]
        return torch.cat(parts, dim=2).flatten(1)       # [B, C*(1+4+16)]

spp = SpatialPyramidPool(levels=(1, 2, 4))
x = torch.randn(2, 64, 13, 13)
print(spp(x).shape)  # [2, 64*(1+4+16)] = [2, 1344]
```

```python
import torch
import torch.nn.functional as F

def roi_pool(feat, box, out_size=7):
    """Simplified RoI pooling: pool feature map region to fixed out_size x out_size."""
    x1, y1, x2, y2 = box
    region = feat[:, :, y1:y2, x1:x2]  # Crop region
    return F.adaptive_max_pool2d(region, (out_size, out_size))

feat = torch.randn(1, 256, 32, 32)   # Feature map
box = (4, 4, 20, 20)                  # Region of interest (x1,y1,x2,y2)
pooled = roi_pool(feat, box, out_size=7)
print("RoI pooled shape:", pooled.shape)  # [1, 256, 7, 7]
```

| Pooling Type | Downsampling | Info Loss | Translation Invariance | Common Use |
| --- | --- | --- | --- | --- |
| Max pool | Yes (stride≥2) | Loses position within window | Strong | Classification backbones (VGG, ResNet) |
| Avg pool | Yes (stride≥2) | Dilutes peak activations | Moderate | Texture features, later stages |
| Global avg pool | Full spatial collapse | Loses all spatial info | Complete | Classification head (ResNet, MobileNet) |
| Adaptive pool | To any target size | Variable | Size-agnostic | Transfer learning, flexible architectures |
| SPP | Multi-scale collapse | Partial per scale | Multi-scale | Object detection (SPPNet, Faster R-CNN) |

## Key Takeaways

Max pooling is the default for classification backbones; it is aggressive but preserves salient activations. Global average pooling replaces flatten+FC in modern classifier heads, reducing parameters by orders of magnitude. Adaptive pooling makes networks input-size agnostic — essential for fine-tuning on different resolutions. Spatial pyramid pooling enables fixed-size representations from variable-size inputs, critical for detection.

Modern architectures are moving away from explicit pooling toward stride-2 convolutions for downsampling, which are learnable and can be more expressive. However, pooling remains important in detection heads (RoI pooling, RoI align) and global feature aggregation. Understanding which pooling variant to use and where in the network architecture requires balancing spatial resolution, compute cost, and the needs of the downstream task.

