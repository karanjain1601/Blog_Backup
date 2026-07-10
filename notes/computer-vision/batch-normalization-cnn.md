---
title: "Batch Normalization in CNNs"
slug: "batch-normalization-cnn"
description: "Batch normalization for convolutional layers — how it normalizes per-channel statistics across spatial locations, placement conventions, training vs eval mode differences, and layer norm alternatives."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXRjaCBub3JtYWxpemF0aW9uIChCTikgd2FzIGludHJvZHVjZWQgYnkgSW9mZmUgYW5kIFN6ZWdlZHkgaW4gMjAxNSBhbmQgYmVjYW1lIGEgc3RhbmRhcmQgYnVpbGRpbmcgYmxvY2sgb2YgQ05Ocy4gSXQgbm9ybWFsaXplcyBhY3RpdmF0aW9ucyB3aXRoaW4gZWFjaCBtaW5pLWJhdGNoLCBzdGFiaWxpemluZyB0aGUgZGlzdHJpYnV0aW9uIG9mIGlucHV0cyB0byBlYWNoIGxheWVyLiBUaGlzIHJlZHVjZXMgaW50ZXJuYWwgY292YXJpYXRlIHNoaWZ0LCBlbmFibGluZyBoaWdoZXIgbGVhcm5pbmcgcmF0ZXMsIHJlZHVjaW5nIHNlbnNpdGl2aXR5IHRvIGluaXRpYWxpemF0aW9uLCBhbmQgcHJvdmlkaW5nIG1pbGQgcmVndWxhcml6YXRpb24gdGhhdCByZWR1Y2VzIHRoZSBuZWVkIGZvciBkcm9wb3V0LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gY29udm9sdXRpb25hbCBsYXllcnMsIEJOIG9wZXJhdGVzIHBlci1jaGFubmVsOiBmb3IgZWFjaCBjaGFubmVsIGMsIGl0IGNvbXB1dGVzIHRoZSBtZWFuIGFuZCB2YXJpYW5jZSBhY3Jvc3MgdGhlIGJhdGNoIGRpbWVuc2lvbiBCIGFuZCBzcGF0aWFsIGRpbWVuc2lvbnMgSCBhbmQgVyBzaW11bHRhbmVvdXNseS4gVGhpcyBpcyBkaWZmZXJlbnQgZnJvbSBmdWxseSBjb25uZWN0ZWQgQk4sIHdoaWNoIG5vcm1hbGl6ZXMgcGVyLWZlYXR1cmUgYWNyb3NzIHRoZSBiYXRjaCBvbmx5LiBUaGUgc3BhdGlhbCBzaGFyaW5nIG1ha2VzIEJOIGZvciBjb252IGxheWVycyBwYXJhbWV0ZXItZWZmaWNpZW50OiBvbmx5IDIgw5cgQyBsZWFybmFibGUgcGFyYW1ldGVycyAozrMgYW5kIM6yKSByZWdhcmRsZXNzIG9mIHNwYXRpYWwgc2l6ZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCTiBNYXRoIGZvciBDb252b2x1dGlvbmFsIExheWVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgZmVhdHVyZSBtYXAgeCBvZiBzaGFwZSBbQiwgQywgSCwgV10sIEJOIGNvbXB1dGVzIHBlci1jaGFubmVsIHN0YXRpc3RpY3M6IM68X2MgPSBtZWFuIG92ZXIgW0IsIEgsIFddLCDPg8KyX2MgPSB2YXJpYW5jZSBvdmVyIFtCLCBILCBXXS4gTm9ybWFsaXplZDogeMyCID0gKHgg4oiSIM68X2MpIC8g4oiaKM+DwrJfYyArIM61KS4gT3V0cHV0OiB5ID0gzrNfYyDCtyB4zIIgKyDOsl9jLCB3aGVyZSDOsyBhbmQgzrIgYXJlIGxlYXJuYWJsZSBzY2FsYXJzIHBlciBjaGFubmVsLiBEdXJpbmcgdHJhaW5pbmcsIGJhdGNoIHN0YXRpc3RpY3MgYXJlIHVzZWQuIER1cmluZyBpbmZlcmVuY2UsIHJ1bm5pbmcgZXhwb25lbnRpYWwgbW92aW5nIGF2ZXJhZ2VzIG9mIM68IGFuZCDPg8KyIGFyZSB1c2VkIGluc3RlYWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmJuID0gbm4uQmF0Y2hOb3JtMmQobnVtX2ZlYXR1cmVzPTY0LCBlcHM9MWUtNSwgbW9tZW50dW09MC4xKVxucHJpbnQoXCJHYW1tYSAod2VpZ2h0KTpcIiwgYm4ud2VpZ2h0LnNoYXBlKSAgIyBbNjRdXG5wcmludChcIkJldGEgIChiaWFzKTogIFwiLCBibi5iaWFzLnNoYXBlKSAgICAjIFs2NF1cbnByaW50KFwiUnVubmluZyBtZWFuOiAgXCIsIGJuLnJ1bm5pbmdfbWVhbi5zaGFwZSkgICMgWzY0XVxucHJpbnQoXCJSdW5uaW5nIHZhcjogICBcIiwgYm4ucnVubmluZ192YXIuc2hhcGUpICAgIyBbNjRdXG5cbnggPSB0b3JjaC5yYW5kbig4LCA2NCwgMTYsIDE2KSAgIyBbQiwgQywgSCwgV11cbmJuLnRyYWluKClcbnRyYWluX291dCA9IGJuKHgpICAgIyBVc2VzIGJhdGNoIHN0YXRzLCB1cGRhdGVzIHJ1bm5pbmcgc3RhdHNcbmJuLmV2YWwoKVxuZXZhbF9vdXQgPSBibih4KSAgICAjIFVzZXMgcnVubmluZyBzdGF0c1xucHJpbnQoXCJNYXggZGlmZiB0cmFpbiB2cyBldmFsOlwiLCAodHJhaW5fb3V0IC0gZXZhbF9vdXQpLmFicygpLm1heCgpLml0ZW0oKSkifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBtYW51YWxfYm5fY29udih4LCBnYW1tYSwgYmV0YSwgZXBzPTFlLTUpOlxuICAgIFwiXCJcIk1hbnVhbCBCTiBmb3J3YXJkIGZvciBbQiwgQywgSCwgV10gaW5wdXQuXCJcIlwiXG4gICAgIyBDb21wdXRlIHBlci1jaGFubmVsIG1lYW4gYW5kIHZhciBvdmVyIFtCLCBILCBXXVxuICAgIG1lYW4gPSB4Lm1lYW4oZGltPSgwLCAyLCAzKSwga2VlcGRpbT1UcnVlKSAgIyBbMSwgQywgMSwgMV1cbiAgICB2YXIgID0geC52YXIoZGltPSgwLCAyLCAzKSwga2VlcGRpbT1UcnVlLCB1bmJpYXNlZD1GYWxzZSlcbiAgICB4X2hhdCA9ICh4IC0gbWVhbikgLyAodmFyICsgZXBzKS5zcXJ0KClcbiAgICByZXR1cm4gZ2FtbWEudmlldygxLCAtMSwgMSwgMSkgKiB4X2hhdCArIGJldGEudmlldygxLCAtMSwgMSwgMSlcblxuQyA9IDE2XG54ID0gdG9yY2gucmFuZG4oNCwgQywgOCwgOClcbmdhbW1hID0gdG9yY2gub25lcyhDKTsgYmV0YSA9IHRvcmNoLnplcm9zKEMpXG5vdXQgPSBtYW51YWxfYm5fY29udih4LCBnYW1tYSwgYmV0YSlcbnByaW50KFwiT3V0cHV0IHNoYXBlOlwiLCBvdXQuc2hhcGUpICAgICAgICAgICMgWzQsIDE2LCA4LCA4XVxucHJpbnQoXCJDaGFubmVsIG1lYW4gfjA6XCIsIG91dC5tZWFuKGRpbT0oMCwyLDMpKS5hYnMoKS5tYXgoKS5pdGVtKCkgXHUwMDNjIDFlLTUpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGxhY2VtZW50OiBCZWZvcmUgb3IgQWZ0ZXIgQWN0aXZhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG9yaWdpbmFsIEJOIHBhcGVyIHBsYWNlZCBub3JtYWxpemF0aW9uIGFmdGVyIHRoZSBsaW5lYXIgdHJhbnNmb3JtIGFuZCBiZWZvcmUgdGhlIGFjdGl2YXRpb246IENvbnYg4oaSIEJOIOKGkiBSZUxVLiBUaGlzIGlzIHN0aWxsIHRoZSBtb3N0IGNvbW1vbiBjb252ZW50aW9uLiBBbiBhbHRlcm5hdGl2ZSwgc29tZXRpbWVzIGNhbGxlZCBcdTAwMjdwcmUtYWN0aXZhdGlvblx1MDAyNyAoSGUgZXQgYWwuLCBJZGVudGl0eSBNYXBwaW5ncyBpbiBSZXNOZXRzKSwgcGxhY2VzIEJOIGJlZm9yZSB0aGUgY29udjogQk4g4oaSIFJlTFUg4oaSIENvbnYuIFByZS1hY3RpdmF0aW9uIEJOIGNhbiBpbXByb3ZlIGdyYWRpZW50IGZsb3cgaW4gdmVyeSBkZWVwIG5ldHdvcmtzIGFuZCBtYWtlcyByZXNpZHVhbCBpZGVudGl0eSBzaG9ydGN1dHMgY2xlYW5lciwgYnV0IGlzIGxlc3MgdW5pdmVyc2FsbHkgYWRvcHRlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbiB2cyBFdmFsIE1vZGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtb3N0IGltcG9ydGFudCBvcGVyYXRpb25hbCBkaWZmZXJlbmNlIGluIEJOIGlzIGJldHdlZW4gdHJhaW5pbmcgYW5kIGV2YWx1YXRpb24uIER1cmluZyB0cmFpbmluZywgQk4gdXNlcyBtaW5pLWJhdGNoIHN0YXRpc3RpY3MgKG1lYW4gYW5kIHZhcmlhbmNlIGNvbXB1dGVkIGZyb20gdGhlIGN1cnJlbnQgYmF0Y2gpLiBUaGlzIGludHJvZHVjZXMgc3RvY2hhc3RpY2l0eSBiZW5lZmljaWFsIGZvciBnZW5lcmFsaXphdGlvbi4gRHVyaW5nIGluZmVyZW5jZSwgYmF0Y2ggc3RhdGlzdGljcyBhcmUgdW5hdmFpbGFibGUgb3IgdW5yZWxpYWJsZSAoYmF0Y2ggc2l6ZSBtYXkgYmUgMSksIHNvIEJOIHVzZXMgcnVubmluZyBleHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZXMgYWNjdW11bGF0ZWQgZHVyaW5nIHRyYWluaW5nLiBGb3JnZXR0aW5nIHRvIHN3aXRjaCBtb2RlcyBpcyBhIHZlcnkgY29tbW9uIGJ1Zy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJjb250ZW50IjoiQmF0Y2hOb3JtIGJlaGF2ZXMgZGlmZmVyZW50bHkgaW4gdHJhaW4gdnMgZXZhbCBtb2RlIOKAlCBhbHdheXMgY2FsbCBtb2RlbC5ldmFsKCkgYXQgaW5mZXJlbmNlIG9yIEJOIHdpbGwgdXNlIGJhdGNoIHN0YXRpc3RpY3MgaW5zdGVhZCBvZiBydW5uaW5nIHN0YXRpc3RpY3MsIGNhdXNpbmcgcGVyZm9ybWFuY2UgZGVncmFkYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGF5ZXIgTm9ybSBhbmQgR3JvdXAgTm9ybSBBbHRlcm5hdGl2ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJOXHUwMDI3cyBkZXBlbmRlbmNlIG9uIGJhdGNoIHNpemUgbWFrZXMgaXQgcHJvYmxlbWF0aWMgZm9yIHNtYWxsIGJhdGNoZXMgKGJhdGNoIHNpemUgMeKAkzIgY2F1c2VzIG5vaXN5IHN0YXRpc3RpY3MpIGFuZCBkaXN0cmlidXRlZCB0cmFpbmluZyBhY3Jvc3MgR1BVcy4gQWx0ZXJuYXRpdmVzOiBHcm91cCBOb3JtYWxpemF0aW9uIChHTikgbm9ybWFsaXplcyBvdmVyIGdyb3VwcyBvZiBjaGFubmVscyB3aXRoaW4gYSBzaW5nbGUgc2FtcGxlLCBlbGltaW5hdGluZyBiYXRjaC1zaXplIGRlcGVuZGVuY2UuIExheWVyIE5vcm1hbGl6YXRpb24gbm9ybWFsaXplcyBvdmVyIGFsbCBjaGFubmVscyBhbmQgc3BhdGlhbCBkaW1zIGZvciBvbmUgc2FtcGxlLiBJbnN0YW5jZSBOb3JtYWxpemF0aW9uIG5vcm1hbGl6ZXMgcGVyLXNhbXBsZSBwZXItY2hhbm5lbC4gUk1TTm9ybSAodXNlZCBpbiB0cmFuc2Zvcm1lcnMpIG9taXRzIHRoZSBtZWFuIGNlbnRlcmluZyBzdGVwLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5CLCBDLCBILCBXID0gNCwgMzIsIDE2LCAxNlxueCA9IHRvcmNoLnJhbmRuKEIsIEMsIEgsIFcpXG5cbiMgR3JvdXAgTm9ybTogOCBncm91cHMgb2YgNCBjaGFubmVscyBlYWNoIOKAlCBubyBiYXRjaCBkZXBlbmRlbmN5XG5nbiA9IG5uLkdyb3VwTm9ybShudW1fZ3JvdXBzPTgsIG51bV9jaGFubmVscz1DKVxub3V0X2duID0gZ24oeClcbnByaW50KFwiR3JvdXBOb3JtIG91dHB1dDpcIiwgb3V0X2duLnNoYXBlKSAgIyBbNCwgMzIsIDE2LCAxNl1cblxuIyBCYXRjaCBOb3JtIGZvciBjb21wYXJpc29uXG5ibiA9IG5uLkJhdGNoTm9ybTJkKEMpXG5vdXRfYm4gPSBibih4KVxucHJpbnQoXCJCYXRjaE5vcm0gb3V0cHV0OlwiLCBvdXRfYm4uc2hhcGUpICAjIFs0LCAzMiwgMTYsIDE2XVxuXG4jIEF0IGJhdGNoX3NpemU9MSwgR04gaXMgc3RhYmxlLCBCTiBpcyBub2lzeVxueDEgPSB0b3JjaC5yYW5kbigxLCBDLCBILCBXKVxucHJpbnQoXCJHTiBhdCBicz0xOlwiLCBnbih4MSkuc3RkKCkuaXRlbSgpKSAgICMgfjEuMCwgc3RhYmxlIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbkIsIEMsIEgsIFcgPSA0LCAzMiwgOCwgOFxueCA9IHRvcmNoLnJhbmRuKEIsIEMsIEgsIFcpXG5cbiMgQk4gYmVmb3JlIFJlTFUgKG9yaWdpbmFsIHBsYWNlbWVudClcbmNvbnZfYm5fcmVsdSA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uQ29udjJkKEMsIEMsIDMsIHBhZGRpbmc9MSksXG4gICAgbm4uQmF0Y2hOb3JtMmQoQyksXG4gICAgbm4uUmVMVShpbnBsYWNlPVRydWUpXG4pXG5cbiMgQk4gYWZ0ZXIgUmVMVSAocHJlLWFjdGl2YXRpb24gLyBIZSAyMDE2IHZhcmlhbnQpXG5jb252X3JlbHVfYm4gPSBubi5TZXF1ZW50aWFsKFxuICAgIG5uLkNvbnYyZChDLCBDLCAzLCBwYWRkaW5nPTEpLFxuICAgIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICBubi5CYXRjaE5vcm0yZChDKVxuKVxuXG5vdXQxID0gY29udl9ibl9yZWx1KHgpXG5vdXQyID0gY29udl9yZWx1X2JuKHgpXG5wcmludChcIkJOLWJlZm9yZTogZGVhZCBuZXVyb25zXCIsIChvdXQxID09IDApLmZsb2F0KCkubWVhbigpLml0ZW0oKSlcbnByaW50KFwiQk4tYWZ0ZXI6ICBkZWFkIG5ldXJvbnNcIiwgKG91dDIgPT0gMCkuZmxvYXQoKS5tZWFuKCkuaXRlbSgpKSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJOb3JtIFR5cGUiLCJOb3JtYWxpemVzIE92ZXIiLCJCYXRjaC1TaXplIFNlbnNpdGl2ZSIsIlNtYWxsIEJhdGNoIFdvcmtzIiwiVXNlIENhc2UiXSwicm93cyI6W1siQmF0Y2hOb3JtIiwiQmF0Y2ggQiArIHNwYXRpYWwgSMOXVyBwZXIgY2hhbm5lbCIsIlllcyIsIk5vIChic1x1MDAzYzggdW5zdGFibGUpIiwiU3RhbmRhcmQgQ05OcywgbGFyZ2UtYmF0Y2ggdmlzaW9uIHRyYWluaW5nIl0sWyJMYXllck5vcm0iLCJBbGwgY2hhbm5lbHMgKyBzcGF0aWFsIHBlciBzYW1wbGUiLCJObyIsIlllcyIsIlRyYW5zZm9ybWVycywgVmlULCBOTFAiXSxbIkdyb3VwTm9ybSIsIkNoYW5uZWwgZ3JvdXBzIHBlciBzYW1wbGUiLCJObyIsIlllcyIsIk9iamVjdCBkZXRlY3Rpb24gKGJzPTHigJMyKSwgc2VnbWVudGF0aW9uIl0sWyJJbnN0YW5jZU5vcm0iLCJTcGF0aWFsIEjDl1cgcGVyIGNoYW5uZWwgcGVyIHNhbXBsZSIsIk5vIiwiWWVzIiwiU3R5bGUgdHJhbnNmZXIsIGltYWdlIHN5bnRoZXNpcyJdLFsiUk1TTm9ybSIsIkFsbCBkaW1zIHBlciBzYW1wbGUgKG5vIG1lYW4pIiwiTm8iLCJZZXMiLCJMTE1zLCBtb2Rlcm4gdHJhbnNmb3JtZXJzIChMbGFtYSwgR2VtbWEpIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXRjaE5vcm0gaXMgdGhlIGRlZmF1bHQgbm9ybWFsaXphdGlvbiBmb3IgQ05OIGNsYXNzaWZpY2F0aW9uIGJhY2tib25lcyB0cmFpbmVkIHdpdGggbGFyZ2UgYmF0Y2ggc2l6ZXMuIEFsd2F5cyByZW1lbWJlciB0aGUgdHJhaW4vZXZhbCBtb2RlIGRpc3RpbmN0aW9uIOKAlCBmYWlsaW5nIHRvIGNhbGwgbW9kZWwuZXZhbCgpIGlzIG9uZSBvZiB0aGUgbW9zdCBjb21tb24gZGVwbG95bWVudCBidWdzLiBUaGUgcnVubmluZyBtZWFuIGFuZCBydW5uaW5nIHZhcmlhbmNlIGJ1ZmZlcnMgYXJlIG5vdCBwYXJhbWV0ZXJzIChubyBncmFkaWVudHMpIGJ1dCBhcmUgcGFydCBvZiB0aGUgbW9kZWwgc3RhdGUgYW5kIG11c3QgYmUgaW5jbHVkZWQgaW4gY2hlY2twb2ludCBzYXZlcyBhbmQgbG9hZHMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZGV0ZWN0aW9uIGFuZCBzZWdtZW50YXRpb24gdGFza3Mgd2hlcmUgYmF0Y2ggc2l6ZSBpcyBzbWFsbCAoMuKAkzQgaW1hZ2VzLCBlYWNoIHdpdGggbWFueSBjcm9wcyksIEdyb3VwIE5vcm1hbGl6YXRpb24gb3V0cGVyZm9ybXMgQmF0Y2hOb3JtLiBGb3IgdHJhbnNmb3JtZXItYmFzZWQgdmlzaW9uIG1vZGVscyAoVmlULCBTd2luKSwgTGF5ZXIgTm9ybWFsaXphdGlvbiBpcyBwcmVmZXJyZWQuIFRoZSBjaG9pY2Ugb2Ygbm9ybWFsaXphdGlvbiBsYXllciBzaWduaWZpY2FudGx5IGFmZmVjdHMgdHJhaW5pbmcgc3RhYmlsaXR5IGFuZCBmaW5hbCBhY2N1cmFjeSDigJQgdHJlYXQgaXQgYXMgYSBmaXJzdC1jbGFzcyBhcmNoaXRlY3R1cmFsIGRlY2lzaW9uIGFsb25nc2lkZSB0aGUgY2hvaWNlIG9mIGFjdGl2YXRpb24gZnVuY3Rpb24gYW5kIG9wdGltaXplci4ifV0="
---
# Batch Normalization in CNNs

## Overview

Batch normalization (BN) was introduced by Ioffe and Szegedy in 2015 and became a standard building block of CNNs. It normalizes activations within each mini-batch, stabilizing the distribution of inputs to each layer. This reduces internal covariate shift, enabling higher learning rates, reducing sensitivity to initialization, and providing mild regularization that reduces the need for dropout.

In convolutional layers, BN operates per-channel: for each channel c, it computes the mean and variance across the batch dimension B and spatial dimensions H and W simultaneously. This is different from fully connected BN, which normalizes per-feature across the batch only. The spatial sharing makes BN for conv layers parameter-efficient: only 2 × C learnable parameters (γ and β) regardless of spatial size.

## BN Math for Convolutional Layers

For a feature map x of shape [B, C, H, W], BN computes per-channel statistics: μ_c = mean over [B, H, W], σ²_c = variance over [B, H, W]. Normalized: x̂ = (x − μ_c) / √(σ²_c + ε). Output: y = γ_c · x̂ + β_c, where γ and β are learnable scalars per channel. During training, batch statistics are used. During inference, running exponential moving averages of μ and σ² are used instead.

```python
import torch
import torch.nn as nn

bn = nn.BatchNorm2d(num_features=64, eps=1e-5, momentum=0.1)
print("Gamma (weight):", bn.weight.shape)  # [64]
print("Beta  (bias):  ", bn.bias.shape)    # [64]
print("Running mean:  ", bn.running_mean.shape)  # [64]
print("Running var:   ", bn.running_var.shape)   # [64]

x = torch.randn(8, 64, 16, 16)  # [B, C, H, W]
bn.train()
train_out = bn(x)   # Uses batch stats, updates running stats
bn.eval()
eval_out = bn(x)    # Uses running stats
print("Max diff train vs eval:", (train_out - eval_out).abs().max().item())
```

```python
import torch

def manual_bn_conv(x, gamma, beta, eps=1e-5):
    """Manual BN forward for [B, C, H, W] input."""
    # Compute per-channel mean and var over [B, H, W]
    mean = x.mean(dim=(0, 2, 3), keepdim=True)  # [1, C, 1, 1]
    var  = x.var(dim=(0, 2, 3), keepdim=True, unbiased=False)
    x_hat = (x - mean) / (var + eps).sqrt()
    return gamma.view(1, -1, 1, 1) * x_hat + beta.view(1, -1, 1, 1)

C = 16
x = torch.randn(4, C, 8, 8)
gamma = torch.ones(C); beta = torch.zeros(C)
out = manual_bn_conv(x, gamma, beta)
print("Output shape:", out.shape)          # [4, 16, 8, 8]
print("Channel mean ~0:", out.mean(dim=(0,2,3)).abs().max().item() < 1e-5)
```

## Placement: Before or After Activation

The original BN paper placed normalization after the linear transform and before the activation: Conv → BN → ReLU. This is still the most common convention. An alternative, sometimes called 'pre-activation' (He et al., Identity Mappings in ResNets), places BN before the conv: BN → ReLU → Conv. Pre-activation BN can improve gradient flow in very deep networks and makes residual identity shortcuts cleaner, but is less universally adopted.

## Train vs Eval Mode

The most important operational difference in BN is between training and evaluation. During training, BN uses mini-batch statistics (mean and variance computed from the current batch). This introduces stochasticity beneficial for generalization. During inference, batch statistics are unavailable or unreliable (batch size may be 1), so BN uses running exponential moving averages accumulated during training. Forgetting to switch modes is a very common bug.

> **warning**: BatchNorm behaves differently in train vs eval mode — always call model.eval() at inference or BN will use batch statistics instead of running statistics, causing performance degradation.

## Layer Norm and Group Norm Alternatives

BN's dependence on batch size makes it problematic for small batches (batch size 1–2 causes noisy statistics) and distributed training across GPUs. Alternatives: Group Normalization (GN) normalizes over groups of channels within a single sample, eliminating batch-size dependence. Layer Normalization normalizes over all channels and spatial dims for one sample. Instance Normalization normalizes per-sample per-channel. RMSNorm (used in transformers) omits the mean centering step.

```python
import torch
import torch.nn as nn

B, C, H, W = 4, 32, 16, 16
x = torch.randn(B, C, H, W)

# Group Norm: 8 groups of 4 channels each — no batch dependency
gn = nn.GroupNorm(num_groups=8, num_channels=C)
out_gn = gn(x)
print("GroupNorm output:", out_gn.shape)  # [4, 32, 16, 16]

# Batch Norm for comparison
bn = nn.BatchNorm2d(C)
out_bn = bn(x)
print("BatchNorm output:", out_bn.shape)  # [4, 32, 16, 16]

# At batch_size=1, GN is stable, BN is noisy
x1 = torch.randn(1, C, H, W)
print("GN at bs=1:", gn(x1).std().item())   # ~1.0, stable
```

```python
import torch
import torch.nn as nn

B, C, H, W = 4, 32, 8, 8
x = torch.randn(B, C, H, W)

# BN before ReLU (original placement)
conv_bn_relu = nn.Sequential(
    nn.Conv2d(C, C, 3, padding=1),
    nn.BatchNorm2d(C),
    nn.ReLU(inplace=True)
)

# BN after ReLU (pre-activation / He 2016 variant)
conv_relu_bn = nn.Sequential(
    nn.Conv2d(C, C, 3, padding=1),
    nn.ReLU(inplace=True),
    nn.BatchNorm2d(C)
)

out1 = conv_bn_relu(x)
out2 = conv_relu_bn(x)
print("BN-before: dead neurons", (out1 == 0).float().mean().item())
print("BN-after:  dead neurons", (out2 == 0).float().mean().item())
```

| Norm Type | Normalizes Over | Batch-Size Sensitive | Small Batch Works | Use Case |
| --- | --- | --- | --- | --- |
| BatchNorm | Batch B + spatial H×W per channel | Yes | No (bs<8 unstable) | Standard CNNs, large-batch vision training |
| LayerNorm | All channels + spatial per sample | No | Yes | Transformers, ViT, NLP |
| GroupNorm | Channel groups per sample | No | Yes | Object detection (bs=1–2), segmentation |
| InstanceNorm | Spatial H×W per channel per sample | No | Yes | Style transfer, image synthesis |
| RMSNorm | All dims per sample (no mean) | No | Yes | LLMs, modern transformers (Llama, Gemma) |

## Key Takeaways

BatchNorm is the default normalization for CNN classification backbones trained with large batch sizes. Always remember the train/eval mode distinction — failing to call model.eval() is one of the most common deployment bugs. The running mean and running variance buffers are not parameters (no gradients) but are part of the model state and must be included in checkpoint saves and loads.

For detection and segmentation tasks where batch size is small (2–4 images, each with many crops), Group Normalization outperforms BatchNorm. For transformer-based vision models (ViT, Swin), Layer Normalization is preferred. The choice of normalization layer significantly affects training stability and final accuracy — treat it as a first-class architectural decision alongside the choice of activation function and optimizer.

