---
title: "Vision Transformer (ViT): Patch Embeddings and Global Attention"
slug: "vit-architecture"
description: "ViT applies a standard Transformer encoder to sequences of image patches — no convolutions, just patch embeddings, positional encodings, and multi-head self-attention for image classification."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWaXNpb24gVHJhbnNmb3JtZXIgKFZpVCksIGludHJvZHVjZWQgYnkgRG9zb3ZpdHNraXkgZXQgYWwuIGluIDIwMjAsIGFwcGxpZXMgYSBzdGFuZGFyZCBUcmFuc2Zvcm1lciBlbmNvZGVyIOKAlCBvcmlnaW5hbGx5IGRlc2lnbmVkIGZvciBOTFAg4oCUIGRpcmVjdGx5IHRvIGltYWdlIGNsYXNzaWZpY2F0aW9uLiBWaVQgZGl2aWRlcyBhbiBpbnB1dCBpbWFnZSBpbnRvIGZpeGVkLXNpemUgcGF0Y2hlcywgbGluZWFybHkgZW1iZWRzIGVhY2ggcGF0Y2gsIGFuZCBwcm9jZXNzZXMgdGhlIHJlc3VsdGluZyBzZXF1ZW5jZSB3aXRoIG11bHRpLWhlYWQgc2VsZi1hdHRlbnRpb24sIGFjaGlldmluZyBzdGF0ZS1vZi10aGUtYXJ0IHJlc3VsdHMgd2hlbiBwcmV0cmFpbmVkIGF0IHNjYWxlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBpbnNpZ2h0IGlzIHRoYXQgaW1hZ2UgcGF0Y2hlcyBjYW4gYmUgdHJlYXRlZCBsaWtlIHdvcmQgdG9rZW5zIGluIE5MUC4gRm9yIGEgMjI0w5cyMjQgaW1hZ2Ugd2l0aCBwYXRjaCBzaXplIFA9MTYsIHdlIGdldCBOPSgyMjQvMTYpwrI9MTk2IHBhdGNoZXMuIEVhY2ggcGF0Y2ggaXMgZmxhdHRlbmVkIGFuZCBwcm9qZWN0ZWQgdG8gYSBELWRpbWVuc2lvbmFsIGVtYmVkZGluZywgdGhlbiBwYXNzZWQgdGhyb3VnaCBMIGlkZW50aWNhbCBUcmFuc2Zvcm1lciBlbmNvZGVyIGJsb2Nrcywgd2l0aCBhIGxlYXJuYWJsZSBbQ0xTXSB0b2tlbiBwcmVwZW5kZWQgdG8gcHJvZHVjZSB0aGUgZmluYWwgaW1hZ2UgcmVwcmVzZW50YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGF0Y2ggRW1iZWRkaW5nIGFuZCBUb2tlbml6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBhdGNoIGVtYmVkZGluZyBjb252ZXJ0cyBhIDJEIGltYWdlIChIw5dXw5dDKSBpbnRvIGEgMUQgc2VxdWVuY2Ugb2YgTiBwYXRjaCB0b2tlbnMuIEEgc2luZ2xlIG5uLkNvbnYyZCB3aXRoIGtlcm5lbF9zaXplPXBhdGNoX3NpemUgYW5kIHN0cmlkZT1wYXRjaF9zaXplIGFjaGlldmVzIHRoaXMgZWZmaWNpZW50bHkg4oCUIGl0IGV4dHJhY3RzIG5vbi1vdmVybGFwcGluZyBwYXRjaGVzIGFuZCBwcm9qZWN0cyBlYWNoIHRvIGRpbWVuc2lvbiBEIGluIG9uZSBvcGVyYXRpb24uIFRoZSByZXN1bHRpbmcgdGVuc29yIHNoYXBlIGlzIChCLCBOLCBEKSB3aGVyZSBOPUhXL1DCsiBpcyB0aGUgbnVtYmVyIG9mIHRva2VucyBwZXIgaW1hZ2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFBhdGNoRW1iZWQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW1nX3NpemU9MjI0LCBwYXRjaF9zaXplPTE2LCBpbl9jaD0zLCBkaW09NzY4KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubl9wYXRjaGVzID0gKGltZ19zaXplIC8vIHBhdGNoX3NpemUpICoqIDJcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uQ29udjJkKGluX2NoLCBkaW0sIGtlcm5lbF9zaXplPXBhdGNoX3NpemUsIHN0cmlkZT1wYXRjaF9zaXplKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgICMgeDogKEIsIEMsIEgsIFcpIC1cdTAwM2UgKEIsIEQsIEgvUCwgVy9QKSAtXHUwMDNlIChCLCBOLCBEKVxuICAgICAgICB4ID0gc2VsZi5wcm9qKHgpICAgICAgICAgICAjIChCLCBkaW0sIEgvUCwgVy9QKVxuICAgICAgICB4ID0geC5mbGF0dGVuKDIpICAgICAgICAgICAjIChCLCBkaW0sIE4pXG4gICAgICAgIHJldHVybiB4LnRyYW5zcG9zZSgxLCAyKSAgICMgKEIsIE4sIGRpbSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBvc2l0aW9uYWwgZW1iZWRkaW5ncyBhcmUgYWRkZWQgdG8gcGF0Y2ggdG9rZW5zIHNvIHRoZSBtb2RlbCBjYW4gcmVhc29uIGFib3V0IHNwYXRpYWwgc3RydWN0dXJlLiBWaVQgdXNlcyAxRCBsZWFybmFibGUgcG9zaXRpb25hbCBlbmNvZGluZ3Mg4oCUIGEgcGFyYW1ldGVyIG9mIHNoYXBlICgxLCBOKzEsIEQpIGFkZGVkIGVsZW1lbnQtd2lzZSB0byB0aGUgZnVsbCB0b2tlbiBzZXF1ZW5jZS4gRGVzcGl0ZSBpZ25vcmluZyAyRCBzdHJ1Y3R1cmUsIDFEIHBvc2l0aW9uYWwgZW5jb2RpbmdzIHdvcmsgd2VsbCBpbiBwcmFjdGljZTsgMkQtYXdhcmUgdmFyaWFudHMgbGlrZSBDUFZUIG9mZmVyIG9ubHkgbWFyZ2luYWwgaW1wcm92ZW1lbnRzIG9uIHN0YW5kYXJkIGJlbmNobWFya3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktSGVhZCBTZWxmLUF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2VsZi1hdHRlbnRpb24gbGV0cyBldmVyeSBwYXRjaCB0b2tlbiBhdHRlbmQgdG8gYWxsIG90aGVyIHBhdGNoIHRva2VucyBzaW11bHRhbmVvdXNseSwgZ2l2aW5nIFZpVCBhIGdsb2JhbCByZWNlcHRpdmUgZmllbGQgZnJvbSBsYXllciBvbmUuIFRoaXMgY29udHJhc3RzIHdpdGggQ05Ocywgd2hpY2ggYnVpbGQgZ2xvYmFsIGNvbnRleHQgZ3JhZHVhbGx5IHRocm91Z2ggc3RhY2tlZCBsb2NhbCBjb252b2x1dGlvbnMuIEluIFZpVCwgZXZlbiB0aGUgZmlyc3QgYXR0ZW50aW9uIGxheWVyIGNhbiBkaXJlY3RseSByZWxhdGUgYSBwYXRjaCBmcm9tIHRoZSB0b3AtbGVmdCBjb3JuZXIgb2YgdGhlIGltYWdlIHRvIG9uZSBmcm9tIHRoZSBib3R0b20tcmlnaHQgY29ybmVyLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbWF0aFxuXG5kZWYgbXVsdGloZWFkX2F0dGVudGlvbih4LCBXX3FrdiwgV19vLCBuX2hlYWRzKTpcbiAgICBCLCBOLCBEID0geC5zaGFwZVxuICAgIGRfayA9IEQgLy8gbl9oZWFkc1xuICAgIHFrdiA9IHggQCBXX3FrdiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIE4sIDNEKVxuICAgIHEsIGssIHYgPSBxa3YuY2h1bmsoMywgZGltPS0xKSAgICAgICAgICAgICAgICAgICAgIyBlYWNoIChCLCBOLCBEKVxuICAgIHJlc2hhcGUgPSBsYW1iZGEgdDogdC52aWV3KEIsIE4sIG5faGVhZHMsIGRfaykudHJhbnNwb3NlKDEsIDIpXG4gICAgcSwgaywgdiA9IHJlc2hhcGUocSksIHJlc2hhcGUoayksIHJlc2hhcGUodikgICAgICAjIChCLCBoLCBOLCBkX2spXG4gICAgYXR0biA9IChxIEAgay50cmFuc3Bvc2UoLTIsIC0xKSkgLyBtYXRoLnNxcnQoZF9rKVxuICAgIGF0dG4gPSBhdHRuLnNvZnRtYXgoZGltPS0xKVxuICAgIG91dCA9IChhdHRuIEAgdikudHJhbnNwb3NlKDEsIDIpLnJlc2hhcGUoQiwgTiwgRClcbiAgICByZXR1cm4gb3V0IEAgV19vIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdHRlbnRpb24gY29tcGxleGl0eSBzY2FsZXMgYXMgTyhOwrJEKSwgbWFraW5nIFZpVCBxdWFkcmF0aWMgaW4gdGhlIG51bWJlciBvZiBwYXRjaGVzLiBGb3IgVmlULUIvMTYgb24gMjI0w5cyMjQgaW1hZ2VzIHRoaXMgbWVhbnMgMTk2wrIg4omIIDM4SyBhdHRlbnRpb24gcGFpcnMgcGVyIGhlYWQg4oCUIG1hbmFnZWFibGUuIEF0IGhpZ2hlciByZXNvbHV0aW9ucyAoNTEyw5c1MTIsIE49MTAyNCkgbWVtb3J5IGJlY29tZXMgYSBib3R0bGVuZWNrLiBFZmZpY2llbnQgdmFyaWFudHMgbGlrZSBTd2luIFRyYW5zZm9ybWVyIGFkZHJlc3MgdGhpcyB3aXRoIGxvY2FsIHdpbmRvdyBhdHRlbnRpb24sIHJlZHVjaW5nIG92ZXJhbGwgY29tcGxleGl0eSBmcm9tIE8oTsKyKSB0byBPKE4pLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYW5zZm9ybWVyIEVuY29kZXIgQmxvY2tzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFYWNoIFRyYW5zZm9ybWVyIGVuY29kZXIgYmxvY2sgYXBwbGllcyB0d28gc3ViLWxheWVycyB3aXRoIHJlc2lkdWFsIGNvbm5lY3Rpb25zOiAoMSkgTGF5ZXIgTm9ybSBmb2xsb3dlZCBieSBNdWx0aS1IZWFkIFNlbGYtQXR0ZW50aW9uLCBhbmQgKDIpIExheWVyIE5vcm0gZm9sbG93ZWQgYnkgYW4gTUxQIHdpdGggdHdvIGxpbmVhciBsYXllcnMgYW5kIEdFTFUgYWN0aXZhdGlvbi4gVmlUIHVzZXMgcHJlLW5vcm0gKExheWVyTm9ybSBiZWZvcmUgZWFjaCBzdWItbGF5ZXIpLCB3aGljaCBzdGFiaWxpemVzIHRyYWluaW5nIGFuZCBhbGxvd3MgZGVlcGVyIG5ldHdvcmtzIHZlcnN1cyBwb3N0LW5vcm0gdXNlZCBpbiB0aGUgb3JpZ2luYWwgVHJhbnNmb3JtZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImNsYXNzIFZpVChubi5Nb2R1bGUpOlxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGltZyk6XG4gICAgICAgICMgMS4gUGF0Y2ggZW1iZWRkaW5nOiAoQixDLEgsVykgLVx1MDAzZSAoQixOLEQpXG4gICAgICAgIHRva2VucyA9IHNlbGYucGF0Y2hfZW1iZWQoaW1nKVxuICAgICAgICAjIDIuIFByZXBlbmQgQ0xTIHRva2VuIGFuZCBhZGQgcG9zaXRpb25hbCBlbmNvZGluZ1xuICAgICAgICBjbHMgPSBzZWxmLmNsc190b2tlbi5leHBhbmQoaW1nLnNpemUoMCksIC0xLCAtMSkgICMgKEIsMSxEKVxuICAgICAgICB0b2tlbnMgPSB0b3JjaC5jYXQoW2NscywgdG9rZW5zXSwgZGltPTEpICAgICAgICAgICAjIChCLE4rMSxEKVxuICAgICAgICB0b2tlbnMgPSB0b2tlbnMgKyBzZWxmLnBvc19lbWJlZFxuICAgICAgICB0b2tlbnMgPSBzZWxmLnBvc19kcm9wKHRva2VucylcbiAgICAgICAgIyAzLiBQYXNzIHRocm91Z2ggTCBlbmNvZGVyIGJsb2Nrc1xuICAgICAgICBmb3IgYmxvY2sgaW4gc2VsZi5ibG9ja3M6XG4gICAgICAgICAgICB0b2tlbnMgPSBibG9jayh0b2tlbnMpXG4gICAgICAgICMgNC4gQ2xhc3NpZnkgZnJvbSBDTFMgdG9rZW4gb3V0cHV0XG4gICAgICAgIHJldHVybiBzZWxmLmhlYWQoc2VsZi5ub3JtKHRva2Vuc1s6LCAwXSkpICAgICAgICAgICMgKEIsIEMpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlZhcmlhbnQiLCJQYXRjaCBTaXplIiwiTGF5ZXJzIiwiSGVhZHMiLCJEaW0iLCJQYXJhbXMgKE0pIiwiSU4tMUsgVG9wLTEgJSJdLCJyb3dzIjpbWyJWaVQtVGkiLCIxNiIsIjEyIiwiMyIsIjE5MiIsIjUuNyIsIjcyLjIiXSxbIlZpVC1TIiwiMTYiLCIxMiIsIjYiLCIzODQiLCIyMi4xIiwiNzkuOCJdLFsiVmlULUIiLCIxNiIsIjEyIiwiMTIiLCI3NjgiLCI4Ni42IiwiODEuOCJdLFsiVmlULUwiLCIxNiIsIjI0IiwiMTYiLCIxMDI0IiwiMzA3IiwiODUuMiJdLFsiVmlULUgiLCIxNCIsIjMyIiwiMTYiLCIxMjgwIiwiNjMyIiwiODguNSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgTUxQIGluc2lkZSBlYWNoIGVuY29kZXIgYmxvY2sgdXNlcyBoaWRkZW4gZGltZW5zaW9uIDTDl0QgKGUuZy4gMzA3MiBmb3IgVmlULUIvMTYgd2l0aCBEPTc2OCkgYW5kIEdFTFUgYWN0aXZhdGlvbi4gRHJvcG91dCBmb2xsb3dzIGJvdGggYXR0ZW50aW9uIGFuZCBNTFAgc3ViLWxheWVycy4gQmxvY2sgY291bnQgdmFyaWVzIGJ5IHZhcmlhbnQ6IFZpVC1UaSBhbmQgVmlULVMgdXNlIDEyIGJsb2NrcywgVmlULUwgdXNlcyAyNCwgVmlULUggdXNlcyAzMi4gRGVlcGVyIGFuZCB3aWRlciBtb2RlbHMgcmVxdWlyZSBsYXJnZS1zY2FsZSBwcmV0cmFpbmluZyB0byBsZXZlcmFnZSB0aGVpciBhZGRpdGlvbmFsIHJlcHJlc2VudGF0aW9uYWwgY2FwYWNpdHkgZWZmZWN0aXZlbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ0xTIFRva2VuIGFuZCBDbGFzc2lmaWNhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBsZWFybmFibGUgW0NMU10gdG9rZW4gaXMgcHJlcGVuZGVkIHRvIHRoZSBwYXRjaCBzZXF1ZW5jZSBiZWZvcmUgdGhlIGZpcnN0IGVuY29kZXIgYmxvY2suIEFmdGVyIEwgVHJhbnNmb3JtZXIgYmxvY2tzLCB0aGUgb3V0cHV0IGF0IHBvc2l0aW9uIDAg4oCUIGNvcnJlc3BvbmRpbmcgdG8gdGhlIFtDTFNdIHRva2VuIOKAlCBhZ2dyZWdhdGVzIGdsb2JhbCBpbmZvcm1hdGlvbiBmcm9tIGFsbCBwYXRjaGVzIHRocm91Z2ggc2VsZi1hdHRlbnRpb24gYW5kIHNlcnZlcyBhcyB0aGUgaW1hZ2UgcmVwcmVzZW50YXRpb24uIEEgbGluZWFyIGNsYXNzaWZpY2F0aW9uIGhlYWQgdGhlbiBtYXBzIHRoaXMgRC1kaW1lbnNpb25hbCB2ZWN0b3IgdG8gdGhlIG51bWJlciBvZiB0YXJnZXQgb3V0cHV0IGNsYXNzZXMuIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRUeXBlIjoid2FybmluZyIsImNvbnRlbnQiOiJWaVQgcmVxdWlyZXMgbGFyZ2Utc2NhbGUgcHJldHJhaW5pbmcgdG8gbWF0Y2ggQ05OIGFjY3VyYWN5IOKAlCBWaVQtQi8xNiB0cmFpbmVkIGZyb20gc2NyYXRjaCBvbiBJbWFnZU5ldC0xSyB1bmRlcnBlcmZvcm1zIFJlc05ldC01MC4gSXQgb25seSBzdXJwYXNzZXMgQ05OcyB3aXRoIEpGVC0zMDBNIG9yIDIxSyBwcmV0cmFpbmluZy4gVXNlIERlaVQgb3IgcHJldHJhaW5lZCBjaGVja3BvaW50cyBmb3Igc21hbGwtZGF0YSBmaW5lLXR1bmluZy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkR1cmluZyBmaW5lLXR1bmluZywgdGhlIGNsYXNzaWZpY2F0aW9uIGhlYWQgaXMgcmVwbGFjZWQgd2l0aCBhIGZyZXNoIGxpbmVhciBsYXllciBmb3IgdGhlIHRhcmdldCBjbGFzcyBjb3VudCwgYW5kIHBvc2l0aW9uYWwgZW1iZWRkaW5ncyBhcmUgaW50ZXJwb2xhdGVkIHdoZW4gdGhlIGZpbmUtdHVuaW5nIHJlc29sdXRpb24gZGlmZmVycyBmcm9tIHByZXRyYWluaW5nLiBWaVQtQi8xNiBwcmV0cmFpbmVkIG9uIEltYWdlTmV0LTIxSyBhY2hpZXZlcyA4NSUrIHRvcC0xIG9uIEltYWdlTmV0LTFLLCBmYXIgZXhjZWVkaW5nIHRoZSA3NyUgb2J0YWluZWQgd2hlbiB0cmFpbmluZyBmcm9tIHNjcmF0Y2ggb24gSW1hZ2VOZXQtMUsgYWxvbmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaCwgdGltZSwgdGltbVxuZnJvbSB0b3JjaHZpc2lvbi5tb2RlbHMgaW1wb3J0IHZpdF9iXzE2LCByZXNuZXQ1MFxuXG5kZWYgYmVuY2htYXJrKG1vZGVsLCBuYW1lLCB4KTpcbiAgICBtb2RlbC5ldmFsKClcbiAgICBuID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpIC8gMWU2XG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZvciBfIGluIHJhbmdlKDEwKTogbW9kZWwoeCkgICAjIHdhcm11cFxuICAgICAgICB0MCA9IHRpbWUudGltZSgpXG4gICAgICAgIGZvciBfIGluIHJhbmdlKDEwMCk6IG1vZGVsKHgpXG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lfToge246LjFmfU0gcGFyYW1zIHwgezEwMC8odGltZS50aW1lKCktdDApOi4xZn0gaW1nL3NcdTAwMjcpXG5cbnggPSB0b3JjaC5yYW5kbigzMiwgMywgMjI0LCAyMjQpXG5iZW5jaG1hcmsodml0X2JfMTYod2VpZ2h0cz1cdTAwMjdERUZBVUxUXHUwMDI3KSwgXHUwMDI3VmlULUIvMTZcdTAwMjcsIHgpXG5iZW5jaG1hcmsocmVzbmV0NTAod2VpZ2h0cz1cdTAwMjdERUZBVUxUXHUwMDI3KSwgXHUwMDI3UmVzTmV0LTUwXHUwMDI3LCB4KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZpVCByZXBsYWNlcyBDTk4gaW5kdWN0aXZlIGJpYXNlcyDigJQgdHJhbnNsYXRpb24gZXF1aXZhcmlhbmNlIGFuZCBsb2NhbGl0eSDigJQgd2l0aCByYXcgc2VsZi1hdHRlbnRpb24gb3ZlciBwYXRjaCB0b2tlbnMuIFRoaXMgbWFrZXMgVmlUIG1vcmUgZ2VuZXJhbCBidXQgZGF0YS1odW5ncnkuIFRyYWluZWQgb24gSkZULTMwME0gKDMwMCBtaWxsaW9uIGltYWdlcyksIFZpVC1IIGFjaGlldmVzIDg4LjUlIHRvcC0xIG9uIEltYWdlTmV0LCBzdXJwYXNzaW5nIGFsbCBDTk5zIG9mIGNvbXBhcmFibGUgcGFyYW1ldGVyIGNvdW50IGFuZCBlc3RhYmxpc2hpbmcgVHJhbnNmb3JtZXJzIGFzIGZpcnN0LWNsYXNzIGltYWdlIGNsYXNzaWZpY2F0aW9uIG1vZGVscy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBhdGNoIHNpemUgaXMgdGhlIHByaW1hcnkgcmVzb2x1dGlvbi1hY2N1cmFjeSB0cmFkZS1vZmYgaW4gVmlULiBTbWFsbGVyIHBhdGNoZXMgKFA9MTQgaW4gVmlULUgpIHlpZWxkIG1vcmUgdG9rZW5zIGFuZCBmaW5lciBzcGF0aWFsIGRldGFpbCBidXQgaW5jcmVhc2UgYXR0ZW50aW9uIGNvbXB1dGUgcXVhZHJhdGljYWxseS4gTGFyZ2VyIHBhdGNoZXMgKFA9MzIpIHRyYWluIGZhc3RlciBhbmQgc3VpdCBoaWdoLXRocm91Z2hwdXQgaW5mZXJlbmNlIGJ1dCBtaXNzIGZpbmUtZ3JhaW5lZCB0ZXh0dXJlcy4gUD0xNiBiYWxhbmNlcyBhY2N1cmFjeSBhbmQgc3BlZWQgZm9yIGNsYXNzaWZpY2F0aW9uOyBkZW5zZSBwcmVkaWN0aW9uIHRhc2tzIHR5cGljYWxseSB1c2Ugc21hbGxlciBwYXRjaGVzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmlUXHUwMDI3cyBhcmNoaXRlY3R1cmUgZW5hYmxlZCBrZXkgc3VjY2Vzc29yczogRGVpVCBhZGRzIGtub3dsZWRnZSBkaXN0aWxsYXRpb24gZm9yIHNtYWxsLWRhdGEgdHJhaW5pbmcsIFN3aW4gVHJhbnNmb3JtZXIgaW50cm9kdWNlcyBoaWVyYXJjaGljYWwgd2luZG93ZWQgYXR0ZW50aW9uIGZvciBkZW5zZSBwcmVkaWN0aW9uLCBCRWlUIGFuZCBNQUUgYXBwbHkgbWFza2VkIGF1dG9lbmNvZGVycyBmb3Igc2VsZi1zdXBlcnZpc2VkIHByZXRyYWluaW5nLCBhbmQgQ0xJUCBwYWlycyBWaVQgd2l0aCBjb250cmFzdGl2ZSBsYW5ndWFnZS1pbWFnZSBwcmV0cmFpbmluZy4gVmlUIGlzIG5vdyB0aGUgZG9taW5hbnQgYmFja2JvbmUgZm9yIGxhcmdlLXNjYWxlIHZpc2lvbiBhbmQgbXVsdGltb2RhbCBtb2RlbHMuIn1d"
---
# Vision Transformer (ViT): Patch Embeddings and Global Attention

## Overview

Vision Transformer (ViT), introduced by Dosovitskiy et al. in 2020, applies a standard Transformer encoder — originally designed for NLP — directly to image classification. ViT divides an input image into fixed-size patches, linearly embeds each patch, and processes the resulting sequence with multi-head self-attention, achieving state-of-the-art results when pretrained at scale.

The key insight is that image patches can be treated like word tokens in NLP. For a 224×224 image with patch size P=16, we get N=(224/16)²=196 patches. Each patch is flattened and projected to a D-dimensional embedding, then passed through L identical Transformer encoder blocks, with a learnable [CLS] token prepended to produce the final image representation.

## Patch Embedding and Tokenization

Patch embedding converts a 2D image (H×W×C) into a 1D sequence of N patch tokens. A single nn.Conv2d with kernel_size=patch_size and stride=patch_size achieves this efficiently — it extracts non-overlapping patches and projects each to dimension D in one operation. The resulting tensor shape is (B, N, D) where N=HW/P² is the number of tokens per image.

```python
import torch
import torch.nn as nn

class PatchEmbed(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_ch=3, dim=768):
        super().__init__()
        self.n_patches = (img_size // patch_size) ** 2
        self.proj = nn.Conv2d(in_ch, dim, kernel_size=patch_size, stride=patch_size)

    def forward(self, x):
        # x: (B, C, H, W) -> (B, D, H/P, W/P) -> (B, N, D)
        x = self.proj(x)           # (B, dim, H/P, W/P)
        x = x.flatten(2)           # (B, dim, N)
        return x.transpose(1, 2)   # (B, N, dim)
```

Positional embeddings are added to patch tokens so the model can reason about spatial structure. ViT uses 1D learnable positional encodings — a parameter of shape (1, N+1, D) added element-wise to the full token sequence. Despite ignoring 2D structure, 1D positional encodings work well in practice; 2D-aware variants like CPVT offer only marginal improvements on standard benchmarks.

## Multi-Head Self-Attention

Self-attention lets every patch token attend to all other patch tokens simultaneously, giving ViT a global receptive field from layer one. This contrasts with CNNs, which build global context gradually through stacked local convolutions. In ViT, even the first attention layer can directly relate a patch from the top-left corner of the image to one from the bottom-right corner.

```python
import math

def multihead_attention(x, W_qkv, W_o, n_heads):
    B, N, D = x.shape
    d_k = D // n_heads
    qkv = x @ W_qkv                                    # (B, N, 3D)
    q, k, v = qkv.chunk(3, dim=-1)                    # each (B, N, D)
    reshape = lambda t: t.view(B, N, n_heads, d_k).transpose(1, 2)
    q, k, v = reshape(q), reshape(k), reshape(v)      # (B, h, N, d_k)
    attn = (q @ k.transpose(-2, -1)) / math.sqrt(d_k)
    attn = attn.softmax(dim=-1)
    out = (attn @ v).transpose(1, 2).reshape(B, N, D)
    return out @ W_o
```

Attention complexity scales as O(N²D), making ViT quadratic in the number of patches. For ViT-B/16 on 224×224 images this means 196² ≈ 38K attention pairs per head — manageable. At higher resolutions (512×512, N=1024) memory becomes a bottleneck. Efficient variants like Swin Transformer address this with local window attention, reducing overall complexity from O(N²) to O(N).

## Transformer Encoder Blocks

Each Transformer encoder block applies two sub-layers with residual connections: (1) Layer Norm followed by Multi-Head Self-Attention, and (2) Layer Norm followed by an MLP with two linear layers and GELU activation. ViT uses pre-norm (LayerNorm before each sub-layer), which stabilizes training and allows deeper networks versus post-norm used in the original Transformer.

```python
class ViT(nn.Module):
    def forward(self, img):
        # 1. Patch embedding: (B,C,H,W) -> (B,N,D)
        tokens = self.patch_embed(img)
        # 2. Prepend CLS token and add positional encoding
        cls = self.cls_token.expand(img.size(0), -1, -1)  # (B,1,D)
        tokens = torch.cat([cls, tokens], dim=1)           # (B,N+1,D)
        tokens = tokens + self.pos_embed
        tokens = self.pos_drop(tokens)
        # 3. Pass through L encoder blocks
        for block in self.blocks:
            tokens = block(tokens)
        # 4. Classify from CLS token output
        return self.head(self.norm(tokens[:, 0]))          # (B, C)
```

| Variant | Patch Size | Layers | Heads | Dim | Params (M) | IN-1K Top-1 % |
| --- | --- | --- | --- | --- | --- | --- |
| ViT-Ti | 16 | 12 | 3 | 192 | 5.7 | 72.2 |
| ViT-S | 16 | 12 | 6 | 384 | 22.1 | 79.8 |
| ViT-B | 16 | 12 | 12 | 768 | 86.6 | 81.8 |
| ViT-L | 16 | 24 | 16 | 1024 | 307 | 85.2 |
| ViT-H | 14 | 32 | 16 | 1280 | 632 | 88.5 |

The MLP inside each encoder block uses hidden dimension 4×D (e.g. 3072 for ViT-B/16 with D=768) and GELU activation. Dropout follows both attention and MLP sub-layers. Block count varies by variant: ViT-Ti and ViT-S use 12 blocks, ViT-L uses 24, ViT-H uses 32. Deeper and wider models require large-scale pretraining to leverage their additional representational capacity effectively.

## CLS Token and Classification

A learnable [CLS] token is prepended to the patch sequence before the first encoder block. After L Transformer blocks, the output at position 0 — corresponding to the [CLS] token — aggregates global information from all patches through self-attention and serves as the image representation. A linear classification head then maps this D-dimensional vector to the number of target output classes.

> ****: ViT requires large-scale pretraining to match CNN accuracy — ViT-B/16 trained from scratch on ImageNet-1K underperforms ResNet-50. It only surpasses CNNs with JFT-300M or 21K pretraining. Use DeiT or pretrained checkpoints for small-data fine-tuning.

During fine-tuning, the classification head is replaced with a fresh linear layer for the target class count, and positional embeddings are interpolated when the fine-tuning resolution differs from pretraining. ViT-B/16 pretrained on ImageNet-21K achieves 85%+ top-1 on ImageNet-1K, far exceeding the 77% obtained when training from scratch on ImageNet-1K alone.

```python
import torch, time, timm
from torchvision.models import vit_b_16, resnet50

def benchmark(model, name, x):
    model.eval()
    n = sum(p.numel() for p in model.parameters()) / 1e6
    with torch.no_grad():
        for _ in range(10): model(x)   # warmup
        t0 = time.time()
        for _ in range(100): model(x)
    print(f'{name}: {n:.1f}M params | {100/(time.time()-t0):.1f} img/s')

x = torch.randn(32, 3, 224, 224)
benchmark(vit_b_16(weights='DEFAULT'), 'ViT-B/16', x)
benchmark(resnet50(weights='DEFAULT'), 'ResNet-50', x)
```

## Key Takeaways

ViT replaces CNN inductive biases — translation equivariance and locality — with raw self-attention over patch tokens. This makes ViT more general but data-hungry. Trained on JFT-300M (300 million images), ViT-H achieves 88.5% top-1 on ImageNet, surpassing all CNNs of comparable parameter count and establishing Transformers as first-class image classification models.

Patch size is the primary resolution-accuracy trade-off in ViT. Smaller patches (P=14 in ViT-H) yield more tokens and finer spatial detail but increase attention compute quadratically. Larger patches (P=32) train faster and suit high-throughput inference but miss fine-grained textures. P=16 balances accuracy and speed for classification; dense prediction tasks typically use smaller patches.

ViT's architecture enabled key successors: DeiT adds knowledge distillation for small-data training, Swin Transformer introduces hierarchical windowed attention for dense prediction, BEiT and MAE apply masked autoencoders for self-supervised pretraining, and CLIP pairs ViT with contrastive language-image pretraining. ViT is now the dominant backbone for large-scale vision and multimodal models.

