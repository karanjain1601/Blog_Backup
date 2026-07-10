---
title: "Image Preprocessing Pipeline for Vision Models"
slug: "image-preprocessing-pipeline"
description: "End-to-end preprocessing — decoding, resizing, padding, normalization, and batching — covering torchvision transforms, aspect-ratio-preserving resize, letterbox padding, and variable-size batching."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbWFnZSBwcmVwcm9jZXNzaW5nIHRyYW5zZm9ybXMgcmF3IHBpeGVsIGRhdGEgaW50byBub3JtYWxpemVkIHRlbnNvcnMgdGhhdCB2aXNpb24gbW9kZWxzIGV4cGVjdC4gQSB0eXBpY2FsIHBpcGVsaW5lIGNvdmVycyBmb3VyIHN0YWdlczogZGVjb2RpbmcgY29tcHJlc3NlZCBpbWFnZXMgZnJvbSBkaXNrLCByZXNpemluZyB0byBhIHRhcmdldCBzcGF0aWFsIHJlc29sdXRpb24sIHBhZGRpbmcgdG8gZW5zdXJlIHVuaWZvcm0gZGltZW5zaW9ucywgYW5kIG5vcm1hbGl6aW5nIHBpeGVsIHZhbHVlcyB0byBtYXRjaCB0cmFpbmluZyBzdGF0aXN0aWNzLiBFYWNoIHN0YWdlIGhhcyB0cmFkZW9mZnMgdGhhdCBkaXJlY3RseSBhZmZlY3QgbW9kZWwgYWNjdXJhY3kgYW5kIGluZmVyZW5jZSBzcGVlZC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzYW1lIHByZXByb2Nlc3NpbmcgYXBwbGllZCBhdCB0cmFpbmluZyBtdXN0IGJlIHJlcGxpY2F0ZWQgYXQgaW5mZXJlbmNlLiBEaWZmZXJlbmNlcyBpbiByZXNpemUgaW50ZXJwb2xhdGlvbiwgY3JvcCBwb3NpdGlvbiwgb3Igbm9ybWFsaXphdGlvbiBjb25zdGFudHMgaW50cm9kdWNlIHN5c3RlbWF0aWMgYmlhcy4gSW4gcHJhY3RpY2UsIG1pc21hdGNoZXMgYXJlIGEgbGVhZGluZyBjYXVzZSBvZiB0aGUgZ2FwIGJldHdlZW4gb2ZmbGluZSBiZW5jaG1hcmsgYWNjdXJhY3kgYW5kIHByb2R1Y3Rpb24gbWV0cmljcyDigJQgb2Z0ZW4gbGFyZ2VyIHRoYW4gdGhlIGdhcCBiZXR3ZWVuIGNvbXBldGluZyBtb2RlbCBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlY29kZSBhbmQgUmVzaXplIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJKUEVHIGFuZCBQTkcgZmlsZXMgbXVzdCBiZSBkZWNvZGVkIGludG8gcGl4ZWwgYXJyYXlzIGJlZm9yZSBhbnkgdGVuc29yIG9wZXJhdGlvbi4gUGlsbG93IGRlY29kZXMgdG8gYW4gUkdCIG51bXB5IGFycmF5OyB0b3JjaHZpc2lvbi5pby5yZWFkX2ltYWdlIHJldHVybnMgYSB1aW50OCB0ZW5zb3IgZGlyZWN0bHkuIEFmdGVyIGRlY29kaW5nLCBpbWFnZXMgYXJlIHJlc2l6ZWQgdG8gdGhlIHNwYXRpYWwgcmVzb2x1dGlvbiB0aGUgbW9kZWwgd2FzIHRyYWluZWQgb24uIHRvcmNodmlzaW9uLnRyYW5zZm9ybXMudjIgaXMgdGhlIG1vZGVybiwgY29tcG9zYWJsZSBBUEkgdGhhdCBoYW5kbGVzIGJvdGggUElMIGltYWdlcyBhbmQgdGVuc29ycyB1bmlmb3JtbHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNodmlzaW9uLnRyYW5zZm9ybXMudjIgYXMgVFxuZnJvbSBQSUwgaW1wb3J0IEltYWdlXG5pbXBvcnQgdG9yY2hcblxudHJhbnNmb3JtID0gVC5Db21wb3NlKFtcbiAgICBULlJlc2l6ZSgyNTYpLFxuICAgIFQuQ2VudGVyQ3JvcCgyMjQpLFxuICAgIFQuVG9JbWFnZSgpLFxuICAgIFQuVG9EdHlwZSh0b3JjaC5mbG9hdDMyLCBzY2FsZT1UcnVlKSxcbiAgICBULk5vcm1hbGl6ZShtZWFuPVswLjQ4NSwgMC40NTYsIDAuNDA2XSxcbiAgICAgICAgICAgICAgICBzdGQ9WzAuMjI5LCAwLjIyNCwgMC4yMjVdKSxcbl0pXG5cbmltZyA9IEltYWdlLm9wZW4oXCJwaG90by5qcGdcIikuY29udmVydChcIlJHQlwiKVxudGVuc29yID0gdHJhbnNmb3JtKGltZykgICAjIHNoYXBlOiBbMywgMjI0LCAyMjRdIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJULlJlc2l6ZSgyNTYpIHNjYWxlcyB0aGUgc2hvcnRlciBzaWRlIHRvIDI1NiBwaXhlbHMgd2hpbGUgcHJlc2VydmluZyBhc3BlY3QgcmF0aW8uIFQuQ2VudGVyQ3JvcCgyMjQpIHRoZW4gY3JvcHMgdGhlIGNlbnRyYWwgMjI0eDIyNCBwYXRjaC4gVC5Ub0R0eXBlIHdpdGggc2NhbGU9VHJ1ZSBjb252ZXJ0cyB1aW50OCBbMCwyNTVdIHRvIGZsb2F0MzIgWzAuMCwxLjBdLiBUaGUgSW1hZ2VOZXQgbWVhbiBhbmQgc3RkIGluIFQuTm9ybWFsaXplIGFyZSBzdGFuZGFyZCBiYXNlbGluZXMg4oCUIHJlcGxhY2UgdGhlbSB3aXRoIHlvdXIgZGF0YXNldCBzdGF0aXN0aWNzIHdoZW4gZmluZS10dW5pbmcgb24gYSBuZXcgZG9tYWluLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFzcGVjdC1SYXRpby1QcmVzZXJ2aW5nIFJlc2l6ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3F1YXNoIHJlc2l6aW5nIChmb3JjaW5nIGJvdGggZGltZW5zaW9ucyB0byBhIGZpeGVkIHNpemUpIGRpc3RvcnRzIG9iamVjdCBnZW9tZXRyeSwgaHVydGluZyBtb2RlbHMgc2Vuc2l0aXZlIHRvIHNoYXBlIOKAlCBtb3N0IGNsYXNzaWZpZXJzIGFuZCBhbGwgZGV0ZWN0b3JzLiBSZXNpemluZyB0aGUgc2hvcnRlciBzaWRlIHRvIHRoZSB0YXJnZXQgd2hpbGUgc2NhbGluZyB0aGUgbG9uZ2VyIHNpZGUgcHJvcG9ydGlvbmFsbHkga2VlcHMgZ2VvbWV0cnkgaW50YWN0LiBUaGUgcmVzdWx0aW5nIGltYWdlIGlzIG5vdCBzcXVhcmUsIHdoaWNoIGNvbXBsaWNhdGVzIGJhdGNoaW5nIGJ1dCBwcmVzZXJ2ZXMgdGhlIGluZm9ybWF0aW9uIHRoZSBuZXR3b3JrIG5lZWRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gUElMIGltcG9ydCBJbWFnZVxuXG5kZWYgcmVzaXplX3Nob3J0ZXJfc2lkZShpbWc6IEltYWdlLkltYWdlLCBzaXplOiBpbnQpIC1cdTAwM2UgSW1hZ2UuSW1hZ2U6XG4gICAgVywgSCA9IGltZy5zaXplXG4gICAgc2NhbGUgPSBzaXplIC8gbWluKEgsIFcpXG4gICAgbmV3X1cgPSByb3VuZChXICogc2NhbGUpXG4gICAgbmV3X0ggPSByb3VuZChIICogc2NhbGUpXG4gICAgcmV0dXJuIGltZy5yZXNpemUoKG5ld19XLCBuZXdfSCksIEltYWdlLkJJTElORUFSKVxuXG4jIEV4YW1wbGU6IDE5MjB4MTA4MCAtXHUwMDNlIHNob3J0ZXIgc2lkZSBiZWNvbWVzIDIyNFxucmVzaXplZCA9IHJlc2l6ZV9zaG9ydGVyX3NpZGUoaW1nLCAyMjQpXG4jIHJlc2l6ZWQuc2l6ZSA9PSAoMzk4LCAyMjQpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGlzIHN0cmF0ZWd5IGlzIHRoZSBkZWZhdWx0IGZvciBjbGFzc2lmaWNhdGlvbiBiYWNrYm9uZXMgKFJlc05ldCwgVmlUKSB3aGVyZSBhIHN1YnNlcXVlbnQgY2VudGVyIGNyb3AgYnJpbmdzIHRoZSBpbWFnZSB0byB0aGUgcmVxdWlyZWQgc3F1YXJlLiBGb3IgZGV0ZWN0aW9uIGFuZCBzZWdtZW50YXRpb24sIHNraXBwaW5nIHRoZSBjcm9wIGlzIHByZWZlcmFibGUg4oCUIHRoZSBtb2RlbCBuZWVkcyBjb250ZXh0IG91dHNpZGUgdGhlIGNlbnRyYWwgcmVnaW9uLiBUaGUgbG9uZ2VyIGRpbWVuc2lvbiB3aWxsIHRoZW4gdmFyeSBwZXIgaW1hZ2UsIHJlcXVpcmluZyBhIHBhZGRpbmcgc3RlcCBiZWZvcmUgYmF0Y2hpbmcuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlJlc2l6ZSBTdHJhdGVneSIsIkFzcGVjdCBSYXRpbyBQcmVzZXJ2ZWQiLCJQYWRkaW5nIiwiQmJveCBDb3JyZWN0aW9uIiwiVXNlIENhc2UiXSwicm93cyI6W1siU3F1YXNoIiwiTm8iLCJObyIsIk5vIiwiRmFzdCBwcm90b3R5cGluZyJdLFsiQ2VudGVyIENyb3AiLCJQYXJ0aWFsIiwiTm8iLCJObyIsIkNsYXNzaWZpY2F0aW9uIl0sWyJSZXNpemUgU2hvcnRlc3QiLCJZZXMiLCJObyIsIk5vIiwiU2luZ2xlLWltYWdlIGluZmVyZW5jZSJdLFsiTGV0dGVyYm94IiwiWWVzIiwiWWVzIiwiWWVzIiwiRGV0ZWN0aW9uIC8gc2VnbWVudGF0aW9uIl0sWyJTbGlkaW5nIFdpbmRvdyIsIlllcyIsIlZhcmllcyIsIlllcyIsIkhpZ2gtcmVzIHNlZ21lbnRhdGlvbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGV0dGVyYm94IFBhZGRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxldHRlcmJveCBwYWRkaW5nIHJlc2l6ZXMgYW4gaW1hZ2Ugc28gaXRzIGxvbmdlciBzaWRlIG1hdGNoZXMgdGhlIHRhcmdldCBzaXplLCB0aGVuIGZpbGxzIHRoZSByZW1haW5pbmcgcGl4ZWxzIG9uIHRoZSBzaG9ydGVyIGF4aXMgd2l0aCBhIG5ldXRyYWwgY29sb3IgKHR5cGljYWxseSBtaWQtZ3JheSwgdmFsdWUgMTE0KS4gVGhpcyBwcm9kdWNlcyBhIHNxdWFyZSB0ZW5zb3Igd2l0aCBubyBkaXN0b3J0aW9uLiBUaGUgcGFkZGluZyBvZmZzZXRzIOKAlCBwaXhlbHMgYWRkZWQgdG8gZWFjaCBzaWRlIOKAlCBtdXN0IGJlIHJlY29yZGVkIHNvIHRoYXQgcHJlZGljdGVkIGJvdW5kaW5nIGJveCBjb29yZGluYXRlcyBjYW4gYmUgc2hpZnRlZCBiYWNrIHRvIHRoZSBvcmlnaW5hbCBpbWFnZSBzcGFjZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIFBJTCBpbXBvcnQgSW1hZ2VcblxuZGVmIGxldHRlcmJveChpbWc6IEltYWdlLkltYWdlLCBzaXplOiBpbnQgPSA2NDAsIGZpbGw6IGludCA9IDExNCk6XG4gICAgVywgSCA9IGltZy5zaXplXG4gICAgc2NhbGUgPSBzaXplIC8gbWF4KEgsIFcpXG4gICAgbmV3X1csIG5ld19IID0gcm91bmQoVyAqIHNjYWxlKSwgcm91bmQoSCAqIHNjYWxlKVxuICAgIGltZyA9IGltZy5yZXNpemUoKG5ld19XLCBuZXdfSCksIEltYWdlLkJJTElORUFSKVxuICAgIHBhZF90b3AgID0gKHNpemUgLSBuZXdfSCkgLy8gMlxuICAgIHBhZF9sZWZ0ID0gKHNpemUgLSBuZXdfVykgLy8gMlxuICAgIGNhbnZhcyA9IEltYWdlLm5ldyhcIlJHQlwiLCAoc2l6ZSwgc2l6ZSksIChmaWxsLCBmaWxsLCBmaWxsKSlcbiAgICBjYW52YXMucGFzdGUoaW1nLCAocGFkX2xlZnQsIHBhZF90b3ApKVxuICAgIHJldHVybiBjYW52YXMsIChwYWRfbGVmdCwgcGFkX3RvcCwgc2NhbGUpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwiY29udGVudCI6IkFwcGx5IHRoZSBzYW1lIHByZXByb2Nlc3NpbmcgYXQgaW5mZXJlbmNlIGFzIGF0IHRyYWluaW5nIOKAlCBhIG1pc21hdGNoIChlLmcuIGNlbnRlciBjcm9wIGF0IHRyYWluIHZzIGZ1bGwgaW1hZ2UgYXQgaW5mZXJlbmNlKSBjb21tb25seSBjYXVzZXMgMeKAkzMlIGFjY3VyYWN5IGRyb3AgaW4gcHJvZHVjdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIG1hcCBhIHByZWRpY3RlZCBib3ggKHgxLCB5MSwgeDIsIHkyKSBpbiBsZXR0ZXJib3hlZCBjb29yZGluYXRlcyBiYWNrIHRvIHRoZSBvcmlnaW5hbCBpbWFnZSwgc3VidHJhY3QgdGhlIHBhZGRpbmcgb2Zmc2V0IGFuZCBkaXZpZGUgYnkgdGhlIHNjYWxlIGZhY3RvcjogeF9vcmlnID0gKHhfbGIgLSBwYWRfbGVmdCkgLyBzY2FsZS4gVGhpcyBpbnZlcnNlIHRyYW5zZm9ybSBtdXN0IGJlIGFwcGxpZWQgYmVmb3JlIGNvbXB1dGluZyBJb1UgYWdhaW5zdCBncm91bmQtdHJ1dGggYm94ZXMgb3IgYmVmb3JlIGRyYXdpbmcgcmVzdWx0cyBvbiB0aGUgc291cmNlIGltYWdlLiBGYWlsaW5nIHRvIGRvIHNvIHNpbGVudGx5IHNoaWZ0cyBhbGwgYm94ZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmF0Y2hpbmcgVmFyaWFibGUtU2l6ZSBJbWFnZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6InRvcmNoLnN0YWNrIHJlcXVpcmVzIGFsbCB0ZW5zb3JzIGluIGEgYmF0Y2ggdG8gc2hhcmUgdGhlIHNhbWUgc2hhcGUuIFdoZW4gaW1hZ2VzIGhhdmUgYmVlbiByZXNpemVkIHRvIHByZXNlcnZlIGFzcGVjdCByYXRpbyBidXQgbm90IHBhZGRlZCB0byBhIHVuaWZvcm0gc3F1YXJlLCB5b3UgbXVzdCBwYWQgd2l0aGluIHRoZSBiYXRjaCBpdHNlbGYuIEEgY3VzdG9tIGNvbGxhdGVfZm4gcGFzc2VkIHRvIERhdGFMb2FkZXIgaGFuZGxlcyB0aGlzOiBmaW5kIHRoZSBtYXhpbXVtIGhlaWdodCBhbmQgd2lkdGggaW4gdGhlIG1pbmktYmF0Y2gsIGFsbG9jYXRlIGEgemVybyB0ZW5zb3Igb2YgdGhhdCBzaGFwZSwgYW5kIGNvcHkgZWFjaCBpbWFnZSBpbnRvIHRoZSB0b3AtbGVmdCBjb3JuZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBjb2xsYXRlX3ZhcmlhYmxlKGJhdGNoKTpcbiAgICBpbWdzLCBsYWJlbHMgPSB6aXAoKmJhdGNoKVxuICAgIG1heF9IID0gbWF4KGltLnNoYXBlWzFdIGZvciBpbSBpbiBpbWdzKVxuICAgIG1heF9XID0gbWF4KGltLnNoYXBlWzJdIGZvciBpbSBpbiBpbWdzKVxuICAgIHBhZGRlZCA9IHRvcmNoLnplcm9zKGxlbihpbWdzKSwgMywgbWF4X0gsIG1heF9XKVxuICAgIG1hc2sgICA9IHRvcmNoLnplcm9zKGxlbihpbWdzKSwgbWF4X0gsIG1heF9XLCBkdHlwZT10b3JjaC5ib29sKVxuICAgIGZvciBpLCBpbSBpbiBlbnVtZXJhdGUoaW1ncyk6XG4gICAgICAgIGgsIHcgPSBpbS5zaGFwZVsxXSwgaW0uc2hhcGVbMl1cbiAgICAgICAgcGFkZGVkW2ksIDosIDpoLCA6d10gPSBpbVxuICAgICAgICBtYXNrW2ksIDpoLCA6d10gPSBUcnVlXG4gICAgcmV0dXJuIHBhZGRlZCwgdG9yY2gudGVuc29yKGxhYmVscyksIG1hc2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtYXNrIHRlbnNvciBtYXJrcyB2YWxpZCBwaXhlbCByZWdpb25zIHNvIHRoZSBtb2RlbCBjYW4gaWdub3JlIHBhZGRpbmcgZHVyaW5nIGF0dGVudGlvbiBvciBwb29saW5nLiBWaVQtc3R5bGUgbW9kZWxzIGJlbmVmaXQgbW9zdDogbWFza2luZyBwYWRkZWQgcGF0Y2hlcyBwcmV2ZW50cyBhdHRlbmRpbmcgdG8gbWVhbmluZ2xlc3MgemVybyByZWdpb25zLiBGb3IgQ05OcywgYmF0Y2gtbGV2ZWwgcGFkZGluZyBhZGRzIGxpdHRsZSBvdmVyaGVhZCB1bmxlc3MgaW1hZ2VzIHZhcnkgd2lkZWx5IGluIHNpemUg4oCUIHNvcnRpbmcgYnkgYXNwZWN0IHJhdGlvIGJlZm9yZSBiYXRjaGluZyByZWR1Y2VzIHdhc3RlZCBwYWRkaW5nIHNpZ25pZmljYW50bHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcmVmZXRjaCBwcmVwcm9jZXNzaW5nIHRvIENQVSB3b3JrZXJzIGJ5IHNldHRpbmcgbnVtX3dvcmtlcnMgXHUwMDNlIDAgaW4gRGF0YUxvYWRlci4gUGluIG1lbW9yeSB3aXRoIHBpbl9tZW1vcnk9VHJ1ZSB0byBhY2NlbGVyYXRlIGhvc3QtdG8tZGV2aWNlIHRyYW5zZmVycy4gRm9yIGRldGVjdGlvbiB3b3JrbG9hZHMgd2l0aCBsYXJnZSBpbWFnZXMgKGUuZy4gMTI4MHgxMjgwKSwgcmVkdWNlIGJhdGNoIHNpemUgYW5kIGluY3JlYXNlIGdyYWRpZW50IGFjY3VtdWxhdGlvbiBzdGVwcy4gUHJvZmlsZSB0aGUgZnVsbCBwaXBlbGluZSB3aXRoIHRvcmNoLnByb2ZpbGVyIHRvIGxvY2F0ZSB0aGUgYm90dGxlbmVjayBiZWZvcmUgb3B0aW1pemluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcmVwcm9jZXNzaW5nIGlzIHBhcnQgb2YgdGhlIG1vZGVsIGNvbnRyYWN0OiB0aGUgYXJjaGl0ZWN0dXJlIGV4cGVjdHMgYSBzcGVjaWZpYyByZXNvbHV0aW9uLCBjaGFubmVsIG9yZGVyLCBhbmQgbm9ybWFsaXphdGlvbiByYW5nZS4gRG9jdW1lbnRpbmcgdGhlc2UgY29uc3RhbnRzIOKAlCB0YXJnZXQgc2l6ZSwgbWVhbiwgc3RkLCBpbnRlcnBvbGF0aW9uIG1vZGUg4oCUIGFsb25nc2lkZSBtb2RlbCB3ZWlnaHRzIHByZXZlbnRzIHNpbGVudCByZWdyZXNzaW9ucyB3aGVuIHJlLWRlcGxveWluZy4gQ29uc2lkZXIgZW5jb2RpbmcgdGhlIHRyYW5zZm9ybSBhcyBhIFRvcmNoU2NyaXB0IG1vZHVsZSBhbmQgc2F2aW5nIGl0IHdpdGggdGhlIGNoZWNrcG9pbnQuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMZXR0ZXJib3ggaXMgdGhlIGdvbGQgc3RhbmRhcmQgZm9yIGRldGVjdGlvbiBhbmQgc2VnbWVudGF0aW9uIGJlY2F1c2UgaXQgcHJlc2VydmVzIGFsbCBpbWFnZSBjb250ZW50LiBDZW50ZXIgY3JvcCBpcyBzdWZmaWNpZW50IGZvciBjbGFzc2lmaWNhdGlvbiB3aGVyZSBnbG9iYWwgY29udGV4dCBvdXRzaWRlIHRoZSBjcm9wIHJhcmVseSBtYXR0ZXJzLiBWYXJpYWJsZS1zaXplIGJhdGNoaW5nIHdpdGggbWFza3MgdW5sb2NrcyBmbGV4aWJsZSB0cmFpbmluZyBidXQgcmVxdWlyZXMgbW9kZWwgYXJjaGl0ZWN0dXJlcyB0aGF0IGFjY2VwdCBtYXNrZWQgaW5wdXRzIOKAlCB2ZXJpZnkgc3VwcG9ydCBiZWZvcmUgYWRvcHRpbmcgdGhpcyBzdHJhdGVneS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdQVS1zaWRlIHByZXByb2Nlc3Npbmcg4oCUIHVzaW5nIHRvcmNodmlzaW9uXHUwMDI3cyBmdW5jdGlvbmFsIEFQSSBvbiBDVURBIHRlbnNvcnMgb3IgTlZJRElBIERBTEkg4oCUIG1vdmVzIHRoZSBib3R0bGVuZWNrIG9mZiB0aGUgQ1BVLiBUaGlzIG1hdHRlcnMgd2hlbiBudW1fd29ya2VycyBpcyBhbHJlYWR5IG1heGVkIGFuZCB0aGUgR1BVIGlzIHN0YXJ2ZWQgZm9yIGRhdGEuIERBTEkgaGFuZGxlcyBKUEVHIGRlY29kaW5nLCByZXNpemluZywgYW5kIG5vcm1hbGl6YXRpb24gZW50aXJlbHkgb24gdGhlIEdQVSwgY3V0dGluZyBlbmQtdG8tZW5kIHRyYWluaW5nIHRpbWUgYnkgdXAgdG8gMjAlIG9uIGltYWdlLWhlYXZ5IHdvcmtsb2Fkcy4ifV0="
---
# Image Preprocessing Pipeline for Vision Models

## Overview

Image preprocessing transforms raw pixel data into normalized tensors that vision models expect. A typical pipeline covers four stages: decoding compressed images from disk, resizing to a target spatial resolution, padding to ensure uniform dimensions, and normalizing pixel values to match training statistics. Each stage has tradeoffs that directly affect model accuracy and inference speed.

The same preprocessing applied at training must be replicated at inference. Differences in resize interpolation, crop position, or normalization constants introduce systematic bias. In practice, mismatches are a leading cause of the gap between offline benchmark accuracy and production metrics — often larger than the gap between competing model architectures.

## Decode and Resize

JPEG and PNG files must be decoded into pixel arrays before any tensor operation. Pillow decodes to an RGB numpy array; torchvision.io.read_image returns a uint8 tensor directly. After decoding, images are resized to the spatial resolution the model was trained on. torchvision.transforms.v2 is the modern, composable API that handles both PIL images and tensors uniformly.

```
import torchvision.transforms.v2 as T
from PIL import Image
import torch

transform = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToImage(),
    T.ToDtype(torch.float32, scale=True),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]),
])

img = Image.open("photo.jpg").convert("RGB")
tensor = transform(img)   # shape: [3, 224, 224]
```

T.Resize(256) scales the shorter side to 256 pixels while preserving aspect ratio. T.CenterCrop(224) then crops the central 224x224 patch. T.ToDtype with scale=True converts uint8 [0,255] to float32 [0.0,1.0]. The ImageNet mean and std in T.Normalize are standard baselines — replace them with your dataset statistics when fine-tuning on a new domain.

## Aspect-Ratio-Preserving Resize

Squash resizing (forcing both dimensions to a fixed size) distorts object geometry, hurting models sensitive to shape — most classifiers and all detectors. Resizing the shorter side to the target while scaling the longer side proportionally keeps geometry intact. The resulting image is not square, which complicates batching but preserves the information the network needs.

```
from PIL import Image

def resize_shorter_side(img: Image.Image, size: int) -> Image.Image:
    W, H = img.size
    scale = size / min(H, W)
    new_W = round(W * scale)
    new_H = round(H * scale)
    return img.resize((new_W, new_H), Image.BILINEAR)

# Example: 1920x1080 -> shorter side becomes 224
resized = resize_shorter_side(img, 224)
# resized.size == (398, 224)
```

This strategy is the default for classification backbones (ResNet, ViT) where a subsequent center crop brings the image to the required square. For detection and segmentation, skipping the crop is preferable — the model needs context outside the central region. The longer dimension will then vary per image, requiring a padding step before batching.

| Resize Strategy | Aspect Ratio Preserved | Padding | Bbox Correction | Use Case |
| --- | --- | --- | --- | --- |
| Squash | No | No | No | Fast prototyping |
| Center Crop | Partial | No | No | Classification |
| Resize Shortest | Yes | No | No | Single-image inference |
| Letterbox | Yes | Yes | Yes | Detection / segmentation |
| Sliding Window | Yes | Varies | Yes | High-res segmentation |

## Letterbox Padding

Letterbox padding resizes an image so its longer side matches the target size, then fills the remaining pixels on the shorter axis with a neutral color (typically mid-gray, value 114). This produces a square tensor with no distortion. The padding offsets — pixels added to each side — must be recorded so that predicted bounding box coordinates can be shifted back to the original image space.

```
from PIL import Image

def letterbox(img: Image.Image, size: int = 640, fill: int = 114):
    W, H = img.size
    scale = size / max(H, W)
    new_W, new_H = round(W * scale), round(H * scale)
    img = img.resize((new_W, new_H), Image.BILINEAR)
    pad_top  = (size - new_H) // 2
    pad_left = (size - new_W) // 2
    canvas = Image.new("RGB", (size, size), (fill, fill, fill))
    canvas.paste(img, (pad_left, pad_top))
    return canvas, (pad_left, pad_top, scale)
```

> **warning**: Apply the same preprocessing at inference as at training — a mismatch (e.g. center crop at train vs full image at inference) commonly causes 1–3% accuracy drop in production.

To map a predicted box (x1, y1, x2, y2) in letterboxed coordinates back to the original image, subtract the padding offset and divide by the scale factor: x_orig = (x_lb - pad_left) / scale. This inverse transform must be applied before computing IoU against ground-truth boxes or before drawing results on the source image. Failing to do so silently shifts all boxes.

## Batching Variable-Size Images

torch.stack requires all tensors in a batch to share the same shape. When images have been resized to preserve aspect ratio but not padded to a uniform square, you must pad within the batch itself. A custom collate_fn passed to DataLoader handles this: find the maximum height and width in the mini-batch, allocate a zero tensor of that shape, and copy each image into the top-left corner.

```
import torch

def collate_variable(batch):
    imgs, labels = zip(*batch)
    max_H = max(im.shape[1] for im in imgs)
    max_W = max(im.shape[2] for im in imgs)
    padded = torch.zeros(len(imgs), 3, max_H, max_W)
    mask   = torch.zeros(len(imgs), max_H, max_W, dtype=torch.bool)
    for i, im in enumerate(imgs):
        h, w = im.shape[1], im.shape[2]
        padded[i, :, :h, :w] = im
        mask[i, :h, :w] = True
    return padded, torch.tensor(labels), mask
```

The mask tensor marks valid pixel regions so the model can ignore padding during attention or pooling. ViT-style models benefit most: masking padded patches prevents attending to meaningless zero regions. For CNNs, batch-level padding adds little overhead unless images vary widely in size — sorting by aspect ratio before batching reduces wasted padding significantly.

Prefetch preprocessing to CPU workers by setting num_workers > 0 in DataLoader. Pin memory with pin_memory=True to accelerate host-to-device transfers. For detection workloads with large images (e.g. 1280x1280), reduce batch size and increase gradient accumulation steps. Profile the full pipeline with torch.profiler to locate the bottleneck before optimizing.

## Key Takeaways

Preprocessing is part of the model contract: the architecture expects a specific resolution, channel order, and normalization range. Documenting these constants — target size, mean, std, interpolation mode — alongside model weights prevents silent regressions when re-deploying. Consider encoding the transform as a TorchScript module and saving it with the checkpoint.

Letterbox is the gold standard for detection and segmentation because it preserves all image content. Center crop is sufficient for classification where global context outside the crop rarely matters. Variable-size batching with masks unlocks flexible training but requires model architectures that accept masked inputs — verify support before adopting this strategy.

GPU-side preprocessing — using torchvision's functional API on CUDA tensors or NVIDIA DALI — moves the bottleneck off the CPU. This matters when num_workers is already maxed and the GPU is starved for data. DALI handles JPEG decoding, resizing, and normalization entirely on the GPU, cutting end-to-end training time by up to 20% on image-heavy workloads.

