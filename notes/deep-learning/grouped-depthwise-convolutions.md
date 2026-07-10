---
title: "Grouped and Depthwise Convolutions — MobileNet Efficiency"
slug: "grouped-depthwise-convolutions"
description: "Understand how grouped and depthwise separable convolutions slash parameters and FLOPs, with MobileNetV1/V2 and ShuffleNet as case studies."
tags: ["deep-learning", "cnns"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgY29udm9sdXRpb24gdHJlYXRzIGFsbCBpbnB1dCBjaGFubmVscyBqb2ludGx5OiBlYWNoIG91dHB1dCBjaGFubmVsIHNlZXMgZXZlcnkgaW5wdXQgY2hhbm5lbCB0aHJvdWdoIGl0cyBvd24ga2VybmVsLCBlbmFibGluZyBmdWxsIGNyb3NzLWNoYW5uZWwgY29tbXVuaWNhdGlvbiBidXQgYXQgdGhlIGNvc3Qgb2YgQ19pbsOXQ19vdXTDl2vCsiBwYXJhbWV0ZXJzLiBHcm91cGVkIGFuZCBkZXB0aHdpc2UgY29udm9sdXRpb25zIGJyZWFrIHRoaXMgY291cGxpbmcgc2VsZWN0aXZlbHkuIEJ5IHNwbGl0dGluZyBjaGFubmVscyBpbnRvIGdyb3VwcyBvciBwcm9jZXNzaW5nIGVhY2ggY2hhbm5lbCBpbmRlcGVuZGVudGx5LCB0aGVzZSBvcGVyYXRpb25zIGFjaGlldmUgZHJhbWF0aWMgcGFyYW1ldGVyIGFuZCBGTE9QIHJlZHVjdGlvbnMgd2hpbGUgcmV0YWluaW5nIG1vc3Qgb2YgdGhlIHJlcHJlc2VudGF0aW9uYWwgcG93ZXIg4oCUIHRoZSBmb3VuZGF0aW9uIG9mIGVmZmljaWVudCBDTk5zIGZvciBtb2JpbGUgYW5kIGVkZ2UgZGVwbG95bWVudC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcm91cGVkIENvbnZvbHV0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHcm91cGVkIGNvbnZvbHV0aW9uIChubi5Db252MmQoLi4uLCBncm91cHM9ZykpIHNwbGl0cyBDX2luIGludG8gZyBncm91cHMgb2YgQ19pbi9nIGNoYW5uZWxzIGVhY2gsIGFuZCBDX291dCBpbnRvIGcgZ3JvdXBzIG9mIENfb3V0L2cuIEVhY2ggZ3JvdXAgcHJvY2Vzc2VzIG9ubHkgaXRzIGNvcnJlc3BvbmRpbmcgaW5wdXQgY2hhbm5lbHMgaW5kZXBlbmRlbnRseS4gVG90YWwgcGFyYW1ldGVyczogQ19pbiDDlyBDX291dCDDlyBrwrIgLyBnIOKAlCBhIGZhY3Rvci1nIHJlZHVjdGlvbi4gRkxPUHMgcmVkdWNlIGJ5IHRoZSBzYW1lIGZhY3Rvci4gQWxleE5ldCB1c2VkIGdyb3Vwcz0yIGFzIGEgcHJhY3RpY2FsIHdvcmthcm91bmQgdG8gZml0IG9uIHR3byBHUFVzIGluIDIwMTIuIFJlc05lWHQgKDIwMTcpIHJlZnJhbWVkIGdyb3VwZWQgY29udiBhcyBcdTAwMjdhZ2dyZWdhdGVkIHJlc2lkdWFsIHRyYW5zZm9ybWF0aW9uc1x1MDAyNzogZ3JvdXBzPTMyIHdpdGggd2lkZXIgY2hhbm5lbHMgbWF0Y2hlcyBSZXNOZXQgYWNjdXJhY3kgd2l0aCBmZXdlciBGTE9Qcy4gVGhlIGNvc3Q6IG5vIGNyb3NzLWdyb3VwIGNvbW11bmljYXRpb24gd2l0aG91dCBhbiBhZGRpdGlvbmFsIG1peGluZyBzdGVwLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5DX2luLCBDX291dCwgayA9IDI1NiwgMjU2LCAzXG5cbmNvbmZpZ3MgPSBbXG4gICAgKFx1MDAyN1N0YW5kYXJkIChnPTEpXHUwMDI3LCAgMSksXG4gICAgKFx1MDAyN0dyb3VwZWQgZz0yXHUwMDI3LCAgICAgMiksXG4gICAgKFx1MDAyN0dyb3VwZWQgZz00XHUwMDI3LCAgICAgNCksXG4gICAgKFx1MDAyN0dyb3VwZWQgZz04XHUwMDI3LCAgICAgOCksXG4gICAgKFx1MDAyN0dyb3VwZWQgZz0zMlx1MDAyNywgICAzMiksXG4gICAgKFx1MDAyN0RlcHRod2lzZSBnPUNcdTAwMjcsIENfaW4pLFxuXVxuXG5wcmludChmXHUwMDI3e1x1MDAyN0NvbmZpZ1x1MDAyNzpcdTAwM2MyMn0ge1x1MDAyN1BhcmFtc1x1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN1JlZHVjdGlvblx1MDAyNzpcdTAwM2UxMH1cdTAwMjcpXG5zdGFuZGFyZF9wYXJhbXMgPSBOb25lXG5mb3IgbmFtZSwgZyBpbiBjb25maWdzOlxuICAgIGNvbnYgPSBubi5Db252MmQoQ19pbiwgQ19vdXQsIGssIHBhZGRpbmc9MSwgZ3JvdXBzPWcsIGJpYXM9RmFsc2UpXG4gICAgcCA9IHN1bSh4Lm51bWVsKCkgZm9yIHggaW4gY29udi5wYXJhbWV0ZXJzKCkpXG4gICAgaWYgc3RhbmRhcmRfcGFyYW1zIGlzIE5vbmU6XG4gICAgICAgIHN0YW5kYXJkX3BhcmFtcyA9IHBcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMjJ9IHtwOlx1MDAzZTEwLH0ge3Avc3RhbmRhcmRfcGFyYW1zOlx1MDAzZTkuM2Z9eFx1MDAyNylcblxuIyBWZXJpZnkgb3V0cHV0IHNoYXBlIGlzIHNhbWUgZm9yIGFsbFxueCA9IHRvcmNoLnJhbmRuKDIsIENfaW4sIDE0LCAxNClcbmZvciBuYW1lLCBnIGluIGNvbmZpZ3M6XG4gICAgY29udiA9IG5uLkNvbnYyZChDX2luLCBDX291dCwgaywgcGFkZGluZz0xLCBncm91cHM9ZywgYmlhcz1GYWxzZSlcbiAgICBhc3NlcnQgY29udih4KS5zaGFwZSA9PSAoMiwgQ19vdXQsIDE0LCAxNCksIGZcdTAwMjdTaGFwZSBtaXNtYXRjaCBmb3Ige25hbWV9XHUwMDI3XG5wcmludChcdTAwMjdcXG5BbGwgcHJvZHVjZSBpZGVudGljYWwgb3V0cHV0IHNoYXBlICgyLCAyNTYsIDE0LCAxNCkg4pyTXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlcHRod2lzZSBTZXBhcmFibGUgQ29udm9sdXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlcHRod2lzZSBzZXBhcmFibGUgY29udm9sdXRpb24gZmFjdG9yaXNlcyBhIHN0YW5kYXJkIGNvbnYgaW50byB0d28gc3RlcHMuIFN0ZXAgMSDigJQgRGVwdGh3aXNlIGNvbnY6IGFwcGx5IG9uZSBrw5drIGtlcm5lbCBwZXIgaW5wdXQgY2hhbm5lbCBpbmRlcGVuZGVudGx5IChncm91cHM9Q19pbiksIHByb2R1Y2luZyBDX2luIG91dHB1dCBjaGFubmVscyB3aXRoIENfaW7Dl2vCsiBwYXJhbWV0ZXJzLiBTdGVwIDIg4oCUIFBvaW50d2lzZSBjb252OiBhcHBseSBhIDHDlzEgY29udiB0byBtaXggY2hhbm5lbHMgKENfaW7Dl0Nfb3V0IHBhcmFtZXRlcnMpLiBUb3RhbDogQ19pbsOXa8KyICsgQ19pbsOXQ19vdXQgdnMgQ19pbsOXQ19vdXTDl2vCsiBmb3Igc3RhbmRhcmQuIFRoZSByYXRpbyBpcyAxL0Nfb3V0ICsgMS9rwrIg4omIIDEva8KyID0gMS85IGZvciBrPTMgYW5kIGxhcmdlIENfb3V0LiBUaGlzIGlzIHRoZSBjb3JlIGlubm92YXRpb24gb2YgTW9iaWxlTmV0VjE6IHJlcGxhY2UgZXZlcnkgM8OXMyBjb252IHdpdGggYSBkZXB0aHdpc2Ugc2VwYXJhYmxlIGJsb2NrLCBhY2hpZXZpbmcgfjjigJM5w5cgcmVkdWN0aW9uIGluIGNvbXB1dGF0aW9uIHdpdGggb25seSB+MSUgdG9wLTEgYWNjdXJhY3kgbG9zcyBvbiBJbWFnZU5ldC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgRGVwdGh3aXNlU2VwYXJhYmxlQ29udihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIk1vYmlsZU5ldFYxLXN0eWxlIGRlcHRod2lzZSBzZXBhcmFibGUgY29udiBibG9jay5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgQ19pbiwgQ19vdXQsIHN0cmlkZT0xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZHcgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKENfaW4sIENfaW4sIDMsIHN0cmlkZT1zdHJpZGUsIHBhZGRpbmc9MSxcbiAgICAgICAgICAgICAgICAgICAgICBncm91cHM9Q19pbiwgYmlhcz1GYWxzZSksICAjIGRlcHRod2lzZVxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQoQ19pbiksXG4gICAgICAgICAgICBubi5SZUxVNihpbnBsYWNlPVRydWUpXG4gICAgICAgIClcbiAgICAgICAgc2VsZi5wdyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoQ19pbiwgQ19vdXQsIDEsIGJpYXM9RmFsc2UpLCAgIyBwb2ludHdpc2VcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKENfb3V0KSxcbiAgICAgICAgICAgIG5uLlJlTFU2KGlucGxhY2U9VHJ1ZSlcbiAgICAgICAgKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLnB3KHNlbGYuZHcoeCkpXG5cbiMgQ29tcGFyZSBwYXJhbWV0ZXIgY291bnRzXG5DX2luLCBDX291dCA9IDEyOCwgMjU2XG5zdGFuZGFyZCA9IG5uLkNvbnYyZChDX2luLCBDX291dCwgMywgcGFkZGluZz0xLCBiaWFzPUZhbHNlKVxuZHdzICAgICAgPSBEZXB0aHdpc2VTZXBhcmFibGVDb252KENfaW4sIENfb3V0KVxuXG5wX3N0ZCA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gc3RhbmRhcmQucGFyYW1ldGVycygpKVxucF9kd3MgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIGR3cy5wYXJhbWV0ZXJzKCkpXG5wcmludChmXHUwMDI3U3RhbmRhcmQgY29udiBwYXJhbXM6ICAgICAge3Bfc3RkOix9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0RlcHRod2lzZS1zZXAgcGFyYW1zOiAgICAgIHtwX2R3czosfVx1MDAyNylcbnByaW50KGZcdTAwMjdSZWR1Y3Rpb24gZmFjdG9yOiAgICAgICAgICB7cF9zdGQvcF9kd3M6LjJmfXhcdTAwMjcpXG5cbnggPSB0b3JjaC5yYW5kbig0LCBDX2luLCAyOCwgMjgpXG5wcmludChmXHUwMDI3XFxuSW5wdXQge3R1cGxlKHguc2hhcGUpfSAtXHUwMDNlIE91dHB1dCB7dHVwbGUoZHdzKHgpLnNoYXBlKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9iaWxlTmV0VjIg4oCUIEludmVydGVkIFJlc2lkdWFscyBhbmQgTGluZWFyIEJvdHRsZW5lY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vYmlsZU5ldFYyIGludHJvZHVjZXMgdHdvIGtleSBpZGVhcy4gRmlyc3QsIHRoZSBpbnZlcnRlZCByZXNpZHVhbDogdW5saWtlIFJlc05ldFx1MDAyN3MgYm90dGxlbmVjayAod2lkZSDihpIgbmFycm93IOKGkiB3aWRlKSwgTW9iaWxlTmV0VjIgZXhwYW5kcyBjaGFubmVscyAobmFycm93IOKGkiB3aWRlIOKGkiBuYXJyb3cpLCBhcHBseWluZyB0aGUgZGVwdGh3aXNlIGNvbnYgaW4gdGhlIGV4cGFuZGVkIGhpZ2gtZGltZW5zaW9uYWwgc3BhY2Ugd2hlcmUgc3BhdGlhbCBtaXhpbmcgaXMgcmljaGVyLCB0aGVuIHByb2plY3RzIGJhY2suIFNlY29uZCwgdGhlIGxpbmVhciBib3R0bGVuZWNrOiB0aGUgZmluYWwgcG9pbnR3aXNlIHByb2plY3Rpb24gdXNlcyBubyBhY3RpdmF0aW9uIChsaW5lYXIpLCBiZWNhdXNlIFJlTFUgaW4gbG93LWRpbWVuc2lvbmFsIHNwYWNlcyBkZXN0cm95cyBpbmZvcm1hdGlvbiBieSBjb2xsYXBzaW5nIHRoZSBtYW5pZm9sZC4gVGhlIHNraXAgY29ubmVjdGlvbiBpcyBhZGRlZCBvbmx5IHdoZW4gaW5wdXQgYW5kIG91dHB1dCBoYXZlIHRoZSBzYW1lIHNoYXBlLiBUaGlzIGRlc2lnbiBhY2hpZXZlcyBiZXR0ZXIgYWNjdXJhY3kvRkxPUCB0cmFkZW9mZiB0aGFuIE1vYmlsZU5ldFYxLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBJbnZlcnRlZFJlc2lkdWFsKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTW9iaWxlTmV0VjIgaW52ZXJ0ZWQgcmVzaWR1YWwgYmxvY2suXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIENfaW4sIENfb3V0LCBzdHJpZGU9MSwgZXhwYW5kX3JhdGlvPTYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgQ19taWQgPSBDX2luICogZXhwYW5kX3JhdGlvXG4gICAgICAgIHNlbGYudXNlX3NraXAgPSAoc3RyaWRlID09IDEgYW5kIENfaW4gPT0gQ19vdXQpXG4gICAgICAgIGxheWVycyA9IFtdXG4gICAgICAgIGlmIGV4cGFuZF9yYXRpbyAhPSAxOiAgIyBleHBhbnNpb24gcGhhc2VcbiAgICAgICAgICAgIGxheWVycyArPSBbbm4uQ29udjJkKENfaW4sIENfbWlkLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQoQ19taWQpLCBubi5SZUxVNihpbnBsYWNlPVRydWUpXVxuICAgICAgICBsYXllcnMgKz0gW1xuICAgICAgICAgICAgbm4uQ29udjJkKENfbWlkLCBDX21pZCwgMywgc3RyaWRlPXN0cmlkZSwgICMgZGVwdGh3aXNlXG4gICAgICAgICAgICAgICAgICAgICAgcGFkZGluZz0xLCBncm91cHM9Q19taWQsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQoQ19taWQpLCBubi5SZUxVNihpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uQ29udjJkKENfbWlkLCBDX291dCwgMSwgYmlhcz1GYWxzZSksICAgICMgbGluZWFyIHByb2plY3Rpb25cbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKENfb3V0KVxuICAgICAgICAgICAgIyBOTyBhY3RpdmF0aW9uIGFmdGVyIGxhc3QgQk4g4oCUIGxpbmVhciBib3R0bGVuZWNrXG4gICAgICAgIF1cbiAgICAgICAgc2VsZi5jb252ID0gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG91dCA9IHNlbGYuY29udih4KVxuICAgICAgICByZXR1cm4gb3V0ICsgeCBpZiBzZWxmLnVzZV9za2lwIGVsc2Ugb3V0XG5cbmJsb2NrID0gSW52ZXJ0ZWRSZXNpZHVhbCgzMiwgMzIsIHN0cmlkZT0xLCBleHBhbmRfcmF0aW89NilcbnggPSB0b3JjaC5yYW5kbig0LCAzMiwgMjgsIDI4KVxucHJpbnQoZlx1MDAyN091dHB1dDoge3R1cGxlKGJsb2NrKHgpLnNoYXBlKX1cdTAwMjcpXG5wID0gc3VtKHEubnVtZWwoKSBmb3IgcSBpbiBibG9jay5wYXJhbWV0ZXJzKCkpXG5wcmludChmXHUwMDI3UGFyYW1zIChDPTMyLCB0PTYpOiB7cDosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaHVmZmxlTmV0IOKAlCBDaGFubmVsIFNodWZmbGUgZm9yIENyb3NzLUdyb3VwIENvbW11bmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikdyb3VwZWQgY29udm9sdXRpb24gY3V0cyBGTE9QIGFuZCBwYXJhbWV0ZXIgY291bnRzIGJ1dCBwcmV2ZW50cyBpbmZvcm1hdGlvbiBmbG93IGJldHdlZW4gZ3JvdXBzLiBTaHVmZmxlTmV0IChaaGFuZyBldCBhbC4gMjAxOCkgc29sdmVzIHRoaXMgd2l0aCBhIGNoYW5uZWwgc2h1ZmZsZSBvcGVyYXRpb246IGFmdGVyIGEgZ3JvdXBlZCBwb2ludHdpc2UgY29udiwgdGhlIG91dHB1dCBjaGFubmVscyBhcmUgZGl2aWRlZCBpbnRvIGcgZ3JvdXBzIGFuZCB0aGVuIGludGVybGVhdmVkIHNvIGVhY2ggZ3JvdXAgb2YgdGhlIG5leHQgbGF5ZXIgc2VlcyBjaGFubmVscyBmcm9tIGFsbCBwcmV2aW91cyBncm91cHMuIFRoZSBzaHVmZmxlIGlzIGEgc2ltcGxlIHJlc2hhcGUgKyB0cmFuc3Bvc2UgKyBmbGF0dGVuIOKAlCB6ZXJvIGV4dHJhIHBhcmFtZXRlcnMsIHplcm8gZXh0cmEgRkxPUHMuIFNodWZmbGVOZXRWMiAoTWEgZXQgYWwuIDIwMTgpIGZ1cnRoZXIgc2hvd3MgdGhhdCBlcXVhbCBjaGFubmVsIHdpZHRocyBpbiBpbnB1dC9vdXRwdXQsIGZld2VyIGdyb3VwcywgYW5kIHNwbGl0K2NvbmNhdCAobm90IGFkZCkgZ2l2ZSB0aGUgYmVzdCB0aHJvdWdocHV0IG9uIHJlYWwgaGFyZHdhcmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBjaGFubmVsX3NodWZmbGUoeCwgZ3JvdXBzKTpcbiAgICBcIlwiXCJSZWFycmFuZ2UgY2hhbm5lbHMgc28gZ3JvdXBlZCBjb252IG91dHB1dHMgZ2V0IGNyb3NzLWdyb3VwIGluZm8uXCJcIlwiXG4gICAgTiwgQywgSCwgVyA9IHguc2hhcGVcbiAgICBhc3NlcnQgQyAlIGdyb3VwcyA9PSAwXG4gICAgeCA9IHgudmlldyhOLCBncm91cHMsIEMgLy8gZ3JvdXBzLCBILCBXKVxuICAgIHggPSB4LnRyYW5zcG9zZSgxLCAyKS5jb250aWd1b3VzKCkgICMgc3dhcCBncm91cCBhbmQgY2hhbm5lbCBkaW1zXG4gICAgcmV0dXJuIHgudmlldyhOLCBDLCBILCBXKVxuXG5jbGFzcyBTaHVmZmxlQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgQ19pbiwgQ19vdXQsIGdyb3Vwcz00KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZ3JvdXBzID0gZ3JvdXBzXG4gICAgICAgIENfbWlkID0gQ19vdXRcbiAgICAgICAgc2VsZi5wdzEgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKENfaW4sIENfbWlkLCAxLCBncm91cHM9Z3JvdXBzLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKENfbWlkKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpXG4gICAgICAgIClcbiAgICAgICAgc2VsZi5kdyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoQ19taWQsIENfbWlkLCAzLCBwYWRkaW5nPTEsIGdyb3Vwcz1DX21pZCwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0yZChDX21pZClcbiAgICAgICAgKVxuICAgICAgICBzZWxmLnB3MiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoQ19taWQsIENfb3V0LCAxLCBncm91cHM9Z3JvdXBzLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKENfb3V0KSwgbm4uUmVMVShpbnBsYWNlPVRydWUpXG4gICAgICAgIClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICB4ID0gc2VsZi5wdzEoeClcbiAgICAgICAgeCA9IGNoYW5uZWxfc2h1ZmZsZSh4LCBzZWxmLmdyb3VwcykgICMgXHUwMDNjLS0gY3Jvc3MtZ3JvdXAgY29tbXVuaWNhdGlvblxuICAgICAgICB4ID0gc2VsZi5kdyh4KVxuICAgICAgICB4ID0gc2VsZi5wdzIoeClcbiAgICAgICAgcmV0dXJuIHhcblxuYmxrID0gU2h1ZmZsZUJsb2NrKDY0LCA2NCwgZ3JvdXBzPTQpXG54ID0gdG9yY2gucmFuZG4oMiwgNjQsIDE0LCAxNClcbnByaW50KGZcdTAwMjdPdXRwdXQ6IHt0dXBsZShibGsoeCkuc2hhcGUpfVx1MDAyNylcbnByaW50KGZcdTAwMjdQYXJhbXM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIGJsay5wYXJhbWV0ZXJzKCkpOix9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiRGVwdGh3aXNlIENvbnYgaXMgU2xvdyBvbiBBY2NlbGVyYXRvcnMiLCJjb250ZW50IjoiRGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbiBoYXMgZmV3ZXIgRkxPUHMgdGhhbiBzdGFuZGFyZCBjb252IG9uIHBhcGVyLCBidXQgaXQgY2FuIGJlIHNsb3dlciBvbiBHUFVzIGJlY2F1c2UgaXRzIG1lbW9yeSBhY2Nlc3MgcGF0dGVybiBpcyBsZXNzIGNhY2hlLWZyaWVuZGx5IGFuZCBpdCB1bmRlci11dGlsaXNlcyB0ZW5zb3IgY29yZXMgZGVzaWduZWQgZm9yIGxhcmdlIG1hdHJpeCBtdWx0aXBsaWNhdGlvbnMuIFNodWZmbGVOZXRWMiBleHBsaWNpdGx5IGJlbmNobWFya3Mgd2FsbC1jbG9jayB0aW1lIHJhdGhlciB0aGFuIEZMT1BzLCBmaW5kaW5nIHRoYXQgZmV3ZXIgZ3JvdXBzIGFuZCBiYWxhbmNlZCBjaGFubmVsIHdpZHRocyBtYXR0ZXIgbW9yZSB0aGFuIHJhdyBGTE9QIGNvdW50cyBmb3IgYWN0dWFsIHRocm91Z2hwdXQuIEFsd2F5cyBwcm9maWxlIG9uIHRhcmdldCBoYXJkd2FyZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBY2N1cmFjeS1FZmZpY2llbmN5IFRyYWRlb2ZmcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGVmZmljaWVuY3kgZ2FpbnMgZnJvbSBncm91cGVkIGFuZCBkZXB0aHdpc2Ugc2VwYXJhYmxlIGNvbnZvbHV0aW9ucyBjb21lIHdpdGggYW4gYWNjdXJhY3kgY29zdCDigJQgZmV3ZXIgY3Jvc3MtY2hhbm5lbCBpbnRlcmFjdGlvbnMgbWVhbiB0aGUgbmV0d29yayBtdXN0IGxlYXJuIHRvIGNvbXBlbnNhdGUgd2l0aCBtb3JlIGRlcHRoIG9yIHdpZHRoLiBJbiBwcmFjdGljZSwgdGhlIHRyYWRlb2ZmIGlzIGV4Y2VsbGVudCBmb3IgbW9iaWxlIGRlcGxveW1lbnQ6IE1vYmlsZU5ldFYzLUxhcmdlIGFjaGlldmVzIDc1LjIlIEltYWdlTmV0IHRvcC0xIGF0IDIxOU0gTUZMT1BzLCBjb21wYXJlZCB0byBSZXNOZXQtNTBcdTAwMjdzIDc2LjElIGF0IDQxMDBNIE1GTE9QcyDigJQgMTnDlyBmZXdlciBGTE9QcyBmb3IgbmVhcmx5IHRoZSBzYW1lIGFjY3VyYWN5LiBUaGUga2V5IGVuYWJsZXIgaXMgdGhlIE5ldXJhbCBBcmNoaXRlY3R1cmUgU2VhcmNoIChOQVMpIHVzZWQgdG8gdHVuZSB0aGUgY2hhbm5lbCB3aWR0aHMgYW5kIGV4cGFuc2lvbiByYXRpb3MgcGVyIGxheWVyLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDb252IFR5cGUiLCJQYXJhbXMiLCJGTE9QcyIsIkNyb3NzLUNoYW5uZWwgTWl4aW5nIiwiQWNjdXJhY3kgVHJhZGVvZmYiLCJVc2UgQ2FzZSJdLCJyb3dzIjpbWyJTdGFuZGFyZCIsIkNfaW7Ct0Nfb3V0wrdrwrIiLCIySFfCt0NfaW7Ct0Nfb3V0wrdrwrIiLCJGdWxsIChhbGzihpJhbGwpIiwiQmFzZWxpbmUiLCJHZW5lcmFsLCBhY2N1cmFjeS1maXJzdCJdLFsiR3JvdXBlZCAoZykiLCJDX2luwrdDX291dMK3a8KyL2ciLCJTYW1lIMO3ZyIsIldpdGhpbiBncm91cCBvbmx5IiwiU21hbGwgZHJvcCIsIlJlc05lWHQsIG11bHRpLUdQVSJdLFsiRGVwdGh3aXNlIiwiQ19pbsK3a8KyIiwiMkhXwrdDX2luwrdrwrIiLCJOb25lIChwZXItY2hhbm5lbCkiLCJMYXJnZSBkcm9wIGFsb25lIiwiQWx3YXlzIHBhaXJlZCB3aXRoIFBXIl0sWyJEVy1TZXBhcmFibGUiLCJDX2luwrdrwrIrQ19pbsK3Q19vdXQiLCIySFfCt0NfaW7CtyhrwrIrQ19vdXQpIiwiVmlhIFBXIGNvbnYiLCJ+MSUgZHJvcCB2cyBzdGFuZGFyZCIsIk1vYmlsZU5ldCwgZWRnZSBkZXZpY2VzIl0sWyJTaHVmZmxlIChnKSIsIlNhbWUgYXMgZ3JvdXBlZMO3ZyIsIlNhbWUgw7dnIiwiQ3Jvc3MtZ3JvdXAgdmlhIHNodWZmbGUiLCJNaW5pbWFsIGRyb3AiLCJTaHVmZmxlTmV0LCBtb2JpbGUiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTW9iaWxlTmV0VjEgd2lkdGggbXVsdGlwbGllciDOsTogc2NhbGVzIGFsbCBjaGFubmVscyBieSDOsSwgcmVkdWNpbmcgcGFyYW1zIGJ5IM6xwrIsIEZMT1BzIGJ5IM6xwrIuIiwiTW9iaWxlTmV0VjEgcmVzb2x1dGlvbiBtdWx0aXBsaWVyIM+BOiBzY2FsZXMgaW5wdXQgcmVzb2x1dGlvbiwgcmVkdWNpbmcgRkxPUHMgYnkgz4HCsi4iLCJFZmZpY2llbnROZXQ6IGNvbXBvdW5kIHNjYWxpbmcgb2YgZGVwdGgsIHdpZHRoLCBhbmQgcmVzb2x1dGlvbiBzaW11bHRhbmVvdXNseSB2aWEgTkFTLiIsIkZvciBncm91cHM9Q19pbiAoZGVwdGh3aXNlKSwgUHlUb3JjaCByZXF1aXJlcyBDX291dD09Q19pbjsgdXNlIGEgc3Vic2VxdWVudCAxw5cxIHRvIGNoYW5nZSBjaGFubmVsIGNvdW50LiIsIlRGTGl0ZSBhbmQgQ29yZU1MIG9wdGltaXNlIGRlcHRod2lzZSBjb252IHNlcGFyYXRlbHkgZnJvbSBzdGFuZGFyZCBjb252IOKAlCBjaGVjayBwbGF0Zm9ybSBzdXBwb3J0LiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIYXJkd2FyZS1Bd2FyZSBEZXNpZ24gd2l0aCBHcm91cGVkIENvbnZvbHV0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvbXB1dGF0aW9uYWwgYWR2YW50YWdlIG9mIGRlcHRod2lzZSBzZXBhcmFibGUgYW5kIGdyb3VwZWQgY29udm9sdXRpb25zIGlzIHJlYWwgaW4gRkxPUCB0ZXJtcyBidXQgY2FuIGJlIGVsdXNpdmUgb24gR1BVIGhhcmR3YXJlLiBjdUROTlx1MDAyN3MgR0VNTS1iYXNlZCBjb252b2x1dGlvbiBpcyBoaWdobHkgdHVuZWQgZm9yIGxhcmdlIG1hdHJpeCBtdWx0aXBsaWNhdGlvbnMgdGhhdCBhcmlzZSBpbiBzdGFuZGFyZCBjb252OyBncm91cGVkIGNvbnYgd2l0aCBtYW55IHNtYWxsIGdyb3VwcyB1bmRlcnV0aWxpc2VzIHRlbnNvciBjb3Jlcy4gTlZJRElBXHUwMDI3cyBBbXBlcmUgQTEwMCBhZGRlZCBkZWRpY2F0ZWQgc3VwcG9ydCBmb3IgZ3JvdXBlZCBjb252b2x1dGlvbnMgYXQgdGhlIGhhcmR3YXJlIGxldmVsLiBPbiBBUk0gQ1BVcyAobW9iaWxlIFNvQ3MpLCBkZXB0aHdpc2UgY29udiBiZW5lZml0cyBmcm9tIE5FT04gU0lNRCBpbnN0cnVjdGlvbnMgYW5kIGlzIGdlbnVpbmVseSBmYXN0ZXIg4oCUIEFwcGxlXHUwMDI3cyBOZXVyYWwgRW5naW5lLCBRdWFsY29tbVx1MDAyN3MgQUkgRW5naW5lLCBhbmQgR29vZ2xlXHUwMDI3cyBFZGdlIFRQVSBhbGwgaGF2ZSBmaXJzdC1jbGFzcyBkZXB0aHdpc2UgY29udiBzdXBwb3J0LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJhY3RpY2FsIGRlcGxveW1lbnQgcmVjb21tZW5kYXRpb246IGJlbmNobWFyayB5b3VyIHNwZWNpZmljIGFyY2hpdGVjdHVyZSBvbiB5b3VyIHNwZWNpZmljIHRhcmdldCBoYXJkd2FyZS4gVG9vbHMgbGlrZSBBSSBCZW5jaG1hcmssIE1MUGVyZiBNb2JpbGUsIGFuZCB0b3JjaC51dGlscy5iZW5jaG1hcmsgcHJvdmlkZSBhY2N1cmF0ZSBsYXRlbmN5IG51bWJlcnMuIEEgcnVsZSBvZiB0aHVtYjogZm9yIHNlcnZlciBHUFUgaW5mZXJlbmNlLCBwcmVmZXIgc3RhbmRhcmQgY29udiB3aXRoIG1vZGVyYXRlIGNoYW5uZWwgY291bnRzOyBmb3IgbW9iaWxlIENQVS9OUFUgaW5mZXJlbmNlLCBkZXB0aHdpc2Ugc2VwYXJhYmxlIGNvbnYgd2l0aCB3aWR0aCBtdWx0aXBsaWVyIM6xPTAuNzXigJMxLjAgZ2l2ZXMgdGhlIGJlc3QgbGF0ZW5jeS9hY2N1cmFjeSB0cmFkZW9mZi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVzZSBncm91cHM9Q19pbiAoZGVwdGh3aXNlKSBvbmx5IHdoZW4gZm9sbG93ZWQgaW1tZWRpYXRlbHkgYnkgYSBwb2ludHdpc2UgMcOXMSBjb252IOKAlCBhbG9uZSBpdCBoYXMgbGltaXRlZCBleHByZXNzaXZpdHkuIiwiRWZmaWNpZW50TmV0LUIwIHRocm91Z2ggQjcgdXNlIGNvbXBvdW5kIHNjYWxpbmc6IGRlcHRoIM6xXs+GLCB3aWR0aCDOsl7PhiwgcmVzb2x1dGlvbiDOs17PhiB3aXRoIM6xwrfOssKywrfOs8KyIOKJiCAyLiIsIkdob3N0TmV0OiBnZW5lcmF0ZXMgXHUwMDI3Z2hvc3RcdTAwMjcgZmVhdHVyZSBtYXBzIGJ5IGNoZWFwIGxpbmVhciBvcGVyYXRpb25zIG9uIGEgc3Vic2V0IG9mIHJlYWwgY29udiBvdXRwdXRzLiIsIkNvbmRDb252IGFuZCBEeW5hbWljQ29udjogaW5wdXQtY29uZGl0aW9uZWQgY29tYmluYXRpb25zIG9mIG11bHRpcGxlIGtlcm5lbHMg4oCUIGFkYXB0aXZlIGdyb3VwZWQgY29udi4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Grouped and Depthwise Convolutions — MobileNet Efficiency

Standard convolution treats all input channels jointly: each output channel sees every input channel through its own kernel, enabling full cross-channel communication but at the cost of C_in×C_out×k² parameters. Grouped and depthwise convolutions break this coupling selectively. By splitting channels into groups or processing each channel independently, these operations achieve dramatic parameter and FLOP reductions while retaining most of the representational power — the foundation of efficient CNNs for mobile and edge deployment.

## Grouped Convolution

Grouped convolution (nn.Conv2d(..., groups=g)) splits C_in into g groups of C_in/g channels each, and C_out into g groups of C_out/g. Each group processes only its corresponding input channels independently. Total parameters: C_in × C_out × k² / g — a factor-g reduction. FLOPs reduce by the same factor. AlexNet used groups=2 as a practical workaround to fit on two GPUs in 2012. ResNeXt (2017) reframed grouped conv as 'aggregated residual transformations': groups=32 with wider channels matches ResNet accuracy with fewer FLOPs. The cost: no cross-group communication without an additional mixing step.

```python
import torch
import torch.nn as nn

C_in, C_out, k = 256, 256, 3

configs = [
    ('Standard (g=1)',  1),
    ('Grouped g=2',     2),
    ('Grouped g=4',     4),
    ('Grouped g=8',     8),
    ('Grouped g=32',   32),
    ('Depthwise g=C', C_in),
]

print(f'{'Config':<22} {'Params':>10} {'Reduction':>10}')
standard_params = None
for name, g in configs:
    conv = nn.Conv2d(C_in, C_out, k, padding=1, groups=g, bias=False)
    p = sum(x.numel() for x in conv.parameters())
    if standard_params is None:
        standard_params = p
    print(f'{name:<22} {p:>10,} {p/standard_params:>9.3f}x')

# Verify output shape is same for all
x = torch.randn(2, C_in, 14, 14)
for name, g in configs:
    conv = nn.Conv2d(C_in, C_out, k, padding=1, groups=g, bias=False)
    assert conv(x).shape == (2, C_out, 14, 14), f'Shape mismatch for {name}'
print('\nAll produce identical output shape (2, 256, 14, 14) ✓')
```

## Depthwise Separable Convolution

Depthwise separable convolution factorises a standard conv into two steps. Step 1 — Depthwise conv: apply one k×k kernel per input channel independently (groups=C_in), producing C_in output channels with C_in×k² parameters. Step 2 — Pointwise conv: apply a 1×1 conv to mix channels (C_in×C_out parameters). Total: C_in×k² + C_in×C_out vs C_in×C_out×k² for standard. The ratio is 1/C_out + 1/k² ≈ 1/k² = 1/9 for k=3 and large C_out. This is the core innovation of MobileNetV1: replace every 3×3 conv with a depthwise separable block, achieving ~8–9× reduction in computation with only ~1% top-1 accuracy loss on ImageNet.

```python
import torch
import torch.nn as nn

class DepthwiseSeparableConv(nn.Module):
    """MobileNetV1-style depthwise separable conv block."""
    def __init__(self, C_in, C_out, stride=1):
        super().__init__()
        self.dw = nn.Sequential(
            nn.Conv2d(C_in, C_in, 3, stride=stride, padding=1,
                      groups=C_in, bias=False),  # depthwise
            nn.BatchNorm2d(C_in),
            nn.ReLU6(inplace=True)
        )
        self.pw = nn.Sequential(
            nn.Conv2d(C_in, C_out, 1, bias=False),  # pointwise
            nn.BatchNorm2d(C_out),
            nn.ReLU6(inplace=True)
        )

    def forward(self, x):
        return self.pw(self.dw(x))

# Compare parameter counts
C_in, C_out = 128, 256
standard = nn.Conv2d(C_in, C_out, 3, padding=1, bias=False)
dws      = DepthwiseSeparableConv(C_in, C_out)

p_std = sum(p.numel() for p in standard.parameters())
p_dws = sum(p.numel() for p in dws.parameters())
print(f'Standard conv params:      {p_std:,}')
print(f'Depthwise-sep params:      {p_dws:,}')
print(f'Reduction factor:          {p_std/p_dws:.2f}x')

x = torch.randn(4, C_in, 28, 28)
print(f'\nInput {tuple(x.shape)} -> Output {tuple(dws(x).shape)}')
```

## MobileNetV2 — Inverted Residuals and Linear Bottleneck

MobileNetV2 introduces two key ideas. First, the inverted residual: unlike ResNet's bottleneck (wide → narrow → wide), MobileNetV2 expands channels (narrow → wide → narrow), applying the depthwise conv in the expanded high-dimensional space where spatial mixing is richer, then projects back. Second, the linear bottleneck: the final pointwise projection uses no activation (linear), because ReLU in low-dimensional spaces destroys information by collapsing the manifold. The skip connection is added only when input and output have the same shape. This design achieves better accuracy/FLOP tradeoff than MobileNetV1.

```python
import torch
import torch.nn as nn

class InvertedResidual(nn.Module):
    """MobileNetV2 inverted residual block."""
    def __init__(self, C_in, C_out, stride=1, expand_ratio=6):
        super().__init__()
        C_mid = C_in * expand_ratio
        self.use_skip = (stride == 1 and C_in == C_out)
        layers = []
        if expand_ratio != 1:  # expansion phase
            layers += [nn.Conv2d(C_in, C_mid, 1, bias=False),
                       nn.BatchNorm2d(C_mid), nn.ReLU6(inplace=True)]
        layers += [
            nn.Conv2d(C_mid, C_mid, 3, stride=stride,  # depthwise
                      padding=1, groups=C_mid, bias=False),
            nn.BatchNorm2d(C_mid), nn.ReLU6(inplace=True),
            nn.Conv2d(C_mid, C_out, 1, bias=False),    # linear projection
            nn.BatchNorm2d(C_out)
            # NO activation after last BN — linear bottleneck
        ]
        self.conv = nn.Sequential(*layers)

    def forward(self, x):
        out = self.conv(x)
        return out + x if self.use_skip else out

block = InvertedResidual(32, 32, stride=1, expand_ratio=6)
x = torch.randn(4, 32, 28, 28)
print(f'Output: {tuple(block(x).shape)}')
p = sum(q.numel() for q in block.parameters())
print(f'Params (C=32, t=6): {p:,}')
```

## ShuffleNet — Channel Shuffle for Cross-Group Communication

Grouped convolution cuts FLOP and parameter counts but prevents information flow between groups. ShuffleNet (Zhang et al. 2018) solves this with a channel shuffle operation: after a grouped pointwise conv, the output channels are divided into g groups and then interleaved so each group of the next layer sees channels from all previous groups. The shuffle is a simple reshape + transpose + flatten — zero extra parameters, zero extra FLOPs. ShuffleNetV2 (Ma et al. 2018) further shows that equal channel widths in input/output, fewer groups, and split+concat (not add) give the best throughput on real hardware.

```python
import torch
import torch.nn as nn

def channel_shuffle(x, groups):
    """Rearrange channels so grouped conv outputs get cross-group info."""
    N, C, H, W = x.shape
    assert C % groups == 0
    x = x.view(N, groups, C // groups, H, W)
    x = x.transpose(1, 2).contiguous()  # swap group and channel dims
    return x.view(N, C, H, W)

class ShuffleBlock(nn.Module):
    def __init__(self, C_in, C_out, groups=4):
        super().__init__()
        self.groups = groups
        C_mid = C_out
        self.pw1 = nn.Sequential(
            nn.Conv2d(C_in, C_mid, 1, groups=groups, bias=False),
            nn.BatchNorm2d(C_mid), nn.ReLU(inplace=True)
        )
        self.dw = nn.Sequential(
            nn.Conv2d(C_mid, C_mid, 3, padding=1, groups=C_mid, bias=False),
            nn.BatchNorm2d(C_mid)
        )
        self.pw2 = nn.Sequential(
            nn.Conv2d(C_mid, C_out, 1, groups=groups, bias=False),
            nn.BatchNorm2d(C_out), nn.ReLU(inplace=True)
        )

    def forward(self, x):
        x = self.pw1(x)
        x = channel_shuffle(x, self.groups)  # <-- cross-group communication
        x = self.dw(x)
        x = self.pw2(x)
        return x

blk = ShuffleBlock(64, 64, groups=4)
x = torch.randn(2, 64, 14, 14)
print(f'Output: {tuple(blk(x).shape)}')
print(f'Params: {sum(p.numel() for p in blk.parameters()):,}')
```

> **Depthwise Conv is Slow on Accelerators**: Depthwise separable convolution has fewer FLOPs than standard conv on paper, but it can be slower on GPUs because its memory access pattern is less cache-friendly and it under-utilises tensor cores designed for large matrix multiplications. ShuffleNetV2 explicitly benchmarks wall-clock time rather than FLOPs, finding that fewer groups and balanced channel widths matter more than raw FLOP counts for actual throughput. Always profile on target hardware.

## Accuracy-Efficiency Tradeoffs

The efficiency gains from grouped and depthwise separable convolutions come with an accuracy cost — fewer cross-channel interactions mean the network must learn to compensate with more depth or width. In practice, the tradeoff is excellent for mobile deployment: MobileNetV3-Large achieves 75.2% ImageNet top-1 at 219M MFLOPs, compared to ResNet-50's 76.1% at 4100M MFLOPs — 19× fewer FLOPs for nearly the same accuracy. The key enabler is the Neural Architecture Search (NAS) used to tune the channel widths and expansion ratios per layer.

| Conv Type | Params | FLOPs | Cross-Channel Mixing | Accuracy Tradeoff | Use Case |
| --- | --- | --- | --- | --- | --- |
| Standard | C_in·C_out·k² | 2HW·C_in·C_out·k² | Full (all→all) | Baseline | General, accuracy-first |
| Grouped (g) | C_in·C_out·k²/g | Same ÷g | Within group only | Small drop | ResNeXt, multi-GPU |
| Depthwise | C_in·k² | 2HW·C_in·k² | None (per-channel) | Large drop alone | Always paired with PW |
| DW-Separable | C_in·k²+C_in·C_out | 2HW·C_in·(k²+C_out) | Via PW conv | ~1% drop vs standard | MobileNet, edge devices |
| Shuffle (g) | Same as grouped÷g | Same ÷g | Cross-group via shuffle | Minimal drop | ShuffleNet, mobile |

- MobileNetV1 width multiplier α: scales all channels by α, reducing params by α², FLOPs by α².
- MobileNetV1 resolution multiplier ρ: scales input resolution, reducing FLOPs by ρ².
- EfficientNet: compound scaling of depth, width, and resolution simultaneously via NAS.
- For groups=C_in (depthwise), PyTorch requires C_out==C_in; use a subsequent 1×1 to change channel count.
- TFLite and CoreML optimise depthwise conv separately from standard conv — check platform support.

## Hardware-Aware Design with Grouped Convolutions

The computational advantage of depthwise separable and grouped convolutions is real in FLOP terms but can be elusive on GPU hardware. cuDNN's GEMM-based convolution is highly tuned for large matrix multiplications that arise in standard conv; grouped conv with many small groups underutilises tensor cores. NVIDIA's Ampere A100 added dedicated support for grouped convolutions at the hardware level. On ARM CPUs (mobile SoCs), depthwise conv benefits from NEON SIMD instructions and is genuinely faster — Apple's Neural Engine, Qualcomm's AI Engine, and Google's Edge TPU all have first-class depthwise conv support.

Practical deployment recommendation: benchmark your specific architecture on your specific target hardware. Tools like AI Benchmark, MLPerf Mobile, and torch.utils.benchmark provide accurate latency numbers. A rule of thumb: for server GPU inference, prefer standard conv with moderate channel counts; for mobile CPU/NPU inference, depthwise separable conv with width multiplier α=0.75–1.0 gives the best latency/accuracy tradeoff.

- Use groups=C_in (depthwise) only when followed immediately by a pointwise 1×1 conv — alone it has limited expressivity.
- EfficientNet-B0 through B7 use compound scaling: depth α^φ, width β^φ, resolution γ^φ with α·β²·γ² ≈ 2.
- GhostNet: generates 'ghost' feature maps by cheap linear operations on a subset of real conv outputs.
- CondConv and DynamicConv: input-conditioned combinations of multiple kernels — adaptive grouped conv.

---

