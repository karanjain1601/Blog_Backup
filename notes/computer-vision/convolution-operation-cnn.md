---
title: "Convolution Operation in CNNs"
slug: "convolution-operation-cnn"
description: "The 2D convolution operation — kernel sliding, stride, padding, dilation, output size formula, and grouped convolutions — with worked examples in PyTorch."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb252b2x1dGlvbiBpcyB0aGUgZnVuZGFtZW50YWwgb3BlcmF0aW9uIGluIGNvbnZvbHV0aW9uYWwgbmV1cmFsIG5ldHdvcmtzLiBBIGxlYXJuYWJsZSBrZXJuZWwgc2xpZGVzIGFjcm9zcyB0aGUgaW5wdXQgZmVhdHVyZSBtYXAsIGNvbXB1dGluZyBkb3QgcHJvZHVjdHMgYXQgZWFjaCBwb3NpdGlvbiB0byBwcm9kdWNlIGFuIG91dHB1dCBmZWF0dXJlIG1hcC4gVGhpcyBsb2NhbCBjb25uZWN0aXZpdHkgYW5kIHdlaWdodCBzaGFyaW5nIGRyYW1hdGljYWxseSByZWR1Y2UgcGFyYW1ldGVycyBjb21wYXJlZCB0byBmdWxseSBjb25uZWN0ZWQgbGF5ZXJzLCB3aGlsZSBwcmVzZXJ2aW5nIHNwYXRpYWwgc3RydWN0dXJlIGluIHZpc3VhbCBkYXRhLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ05OcyBleHBsb2l0IHRocmVlIGtleSBwcm9wZXJ0aWVzOiBsb2NhbCBjb25uZWN0aXZpdHkgKGVhY2ggb3V0cHV0IGRlcGVuZHMgb24gYSBzbWFsbCBpbnB1dCByZWdpb24pLCB3ZWlnaHQgc2hhcmluZyAodGhlIHNhbWUga2VybmVsIGlzIGFwcGxpZWQgZXZlcnl3aGVyZSksIGFuZCB0cmFuc2xhdGlvbiBlcXVpdmFyaWFuY2UgKHNoaWZ0aW5nIHRoZSBpbnB1dCBzaGlmdHMgdGhlIG91dHB1dCBieSB0aGUgc2FtZSBhbW91bnQpLiBUaGVzZSBwcm9wZXJ0aWVzIG1ha2UgY29udm9sdXRpb25zIGlkZWFsIGZvciBpbWFnZSBkYXRhIHdoZXJlIHBhdHRlcm5zIGNhbiBhcHBlYXIgYW55d2hlcmUgaW4gdGhlIHNjZW5lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IjJEIENvbnZvbHV0aW9uIE1hdGgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIDJEIGlucHV0IFggb2Ygc2hhcGUgKEgsIFcpIGFuZCBrZXJuZWwgSyBvZiBzaGFwZSAoa0gsIGtXKSwgdGhlIG91dHB1dCBZIGF0IHBvc2l0aW9uIChpLCBqKSBpcyBjb21wdXRlZCBhcyBhIHN1bSBvZiBlbGVtZW50LXdpc2UgcHJvZHVjdHM6IFlbaSxqXSA9IM6jX20gzqNfbiBYW2krbSwgaituXSDCtyBLW20sbl0uIEluIGRlZXAgbGVhcm5pbmcsIHRoaXMgb3BlcmF0aW9uIGlzIHRlY2huaWNhbGx5IGNyb3NzLWNvcnJlbGF0aW9uIChubyBrZXJuZWwgZmxpcCksIGJ1dCBpcyB1bml2ZXJzYWxseSBjYWxsZWQgY29udm9sdXRpb24uIExlYXJuYWJsZSBiaWFzIGlzIGFkZGVkIGFmdGVyIHRoZSBzdW1tYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBtYW51YWxfY3Jvc3NfY29ycmVsYXRlKHgsIGspOlxuICAgIEgsIFcgPSB4LnNoYXBlXG4gICAga0gsIGtXID0gay5zaGFwZVxuICAgIG91dCA9IG5wLnplcm9zKChIIC0ga0ggKyAxLCBXIC0ga1cgKyAxKSlcbiAgICBmb3IgaSBpbiByYW5nZShvdXQuc2hhcGVbMF0pOlxuICAgICAgICBmb3IgaiBpbiByYW5nZShvdXQuc2hhcGVbMV0pOlxuICAgICAgICAgICAgb3V0W2ksIGpdID0gKHhbaTppK2tILCBqOmora1ddICogaykuc3VtKClcbiAgICByZXR1cm4gb3V0XG5cbnhfbnAgPSBucC5yYW5kb20ucmFuZG4oNiwgNikuYXN0eXBlKG5wLmZsb2F0MzIpXG5rX25wID0gbnAucmFuZG9tLnJhbmRuKDMsIDMpLmFzdHlwZShucC5mbG9hdDMyKVxubWFudWFsX291dCA9IG1hbnVhbF9jcm9zc19jb3JyZWxhdGUoeF9ucCwga19ucClcbnRvcmNoX291dCA9IEYuY29udjJkKHRvcmNoLnRlbnNvcih4X25wW05vbmUsTm9uZV0pLCB0b3JjaC50ZW5zb3Ioa19ucFtOb25lLE5vbmVdKSlcbnByaW50KG5wLmFsbGNsb3NlKG1hbnVhbF9vdXQsIHRvcmNoX291dC5udW1weSgpWzAsMF0sIGF0b2w9MWUtNSkpICAjIFRydWUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvdXRwdXQgc3BhdGlhbCBzaXplIGFmdGVyIGNvbnZvbHV0aW9uIGlzIGRldGVybWluZWQgYnkgaW5wdXQgc2l6ZSwga2VybmVsIHNpemUsIHN0cmlkZSwgYW5kIHBhZGRpbmcuIEZvciBhIDFEIGNhc2U6IG91dHB1dF9sZW5ndGggPSBmbG9vcigoaW5wdXQgKyAyKnBhZGRpbmcgLSBrZXJuZWwpIC8gc3RyaWRlKSArIDEuIEluIFB5VG9yY2gsIG5uLkNvbnYyZCBoYW5kbGVzIHRoaXMgYXV0b21hdGljYWxseSwgYnV0IHVuZGVyc3RhbmRpbmcgdGhlIGZvcm11bGEgaGVscHMgZGlhZ25vc2Ugc2hhcGUgbWlzbWF0Y2hlcyBhbmQgZGVzaWduIGFyY2hpdGVjdHVyZXMgd2l0aCBzcGVjaWZpYyBvdXRwdXQgcmVzb2x1dGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RyaWRlIGFuZCBQYWRkaW5nIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBvdXRwdXRfc2l6ZShILCBXLCBLLCBTLCBQKTpcbiAgICBvdXRfSCA9IChIICsgMipQIC0gSykgLy8gUyArIDFcbiAgICBvdXRfVyA9IChXICsgMipQIC0gSykgLy8gUyArIDFcbiAgICByZXR1cm4gb3V0X0gsIG91dF9XXG5cbiMgU3RhbmRhcmQ6IHN0cmlkZT0xLCBubyBwYWRkaW5nXG5wcmludChvdXRwdXRfc2l6ZSgzMiwgMzIsIDMsIDEsIDApKSAgICMgKDMwLCAzMClcbiMgU2FtZSBwYWRkaW5nOiBvdXRwdXQgPT0gaW5wdXRcbnByaW50KG91dHB1dF9zaXplKDMyLCAzMiwgMywgMSwgMSkpICAgIyAoMzIsIDMyKVxuIyBTdHJpZGUtMiBoYWx2aW5nXG5wcmludChvdXRwdXRfc2l6ZSgzMiwgMzIsIDMsIDIsIDEpKSAgICMgKDE2LCAxNilcbiMgVmVyaWZ5IHdpdGggbm4uQ29udjJkXG5jb252ID0gbm4uQ29udjJkKDEsIDEsIGtlcm5lbF9zaXplPTMsIHN0cmlkZT0yLCBwYWRkaW5nPTEpXG54ID0gdG9yY2guemVyb3MoMSwgMSwgMzIsIDMyKVxucHJpbnQoY29udih4KS5zaGFwZSkgICMgdG9yY2guU2l6ZShbMSwgMSwgMTYsIDE2XSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0cmlkZSBjb250cm9scyBob3cgZmFyIHRoZSBrZXJuZWwgbW92ZXMgYXQgZWFjaCBzdGVwLiBTdHJpZGU9MSBwcmVzZXJ2ZXMgc3BhdGlhbCByZXNvbHV0aW9uOyBzdHJpZGU9MiBoYWx2ZXMgaXQgd2l0aG91dCBleHBsaWNpdCBwb29saW5nLCB3aGljaCBpcyB1c2VkIGluIG1vZGVybiBhcmNoaXRlY3R1cmVzIGxpa2UgUmVzTmV0IHRvIHJlZHVjZSBjb21wdXRhdGlvbi4gUGFkZGluZyBhZGRzIHplcm9zIGFyb3VuZCB0aGUgaW5wdXQgYm91bmRhcnkuIFx1MDAyN1NhbWVcdTAwMjcgcGFkZGluZyAoUCA9IChLLTEpLzIgZm9yIG9kZCBrZXJuZWxzKSBtYWludGFpbnMgc3BhdGlhbCBkaW1lbnNpb25zIGFuZCBwcmV2ZW50cyBpbmZvcm1hdGlvbiBsb3NzIGF0IGVkZ2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpbGF0ZWQgQ29udm9sdXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaWxhdGVkIChhdHJvdXMpIGNvbnZvbHV0aW9ucyBpbnNlcnQgZ2FwcyBiZXR3ZWVuIGtlcm5lbCBlbGVtZW50cywgZXhwYW5kaW5nIHRoZSByZWNlcHRpdmUgZmllbGQgd2l0aG91dCBpbmNyZWFzaW5nIHBhcmFtZXRlcnMgb3IgbG9zaW5nIHNwYXRpYWwgcmVzb2x1dGlvbi4gQSBkaWxhdGlvbiByYXRlIGQ9MiBvbiBhIDPDlzMga2VybmVsIGNvdmVycyBhIDXDlzUgcmVnaW9uOyBkPTQgY292ZXJzIDnDlzkuIFRoaXMgaXMgZXNwZWNpYWxseSB1c2VmdWwgZm9yIGRlbnNlIHByZWRpY3Rpb24gdGFza3MgKHNlZ21lbnRhdGlvbiwgZGV0ZWN0aW9uKSB3aGVyZSBsYXJnZSBjb250ZXh0IGlzIG5lZWRlZCBhdCBmdWxsIHJlc29sdXRpb24sIGFzIHVzZWQgaW4gRGVlcExhYiBhbmQgV2F2ZU5ldCBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG54ID0gdG9yY2guYXJhbmdlKDI1LCBkdHlwZT10b3JjaC5mbG9hdDMyKS5yZXNoYXBlKDEsIDEsIDUsIDUpXG5wcmludChcIklucHV0OlxcblwiLCB4WzAsMF0pXG5cbiMgU3RhbmRhcmQgM3gzIGNvbnY6IHNlZXMgM3gzIHJlZ2lvblxuY29udl9zdGQgPSBubi5Db252MmQoMSwgMSwgMywgZGlsYXRpb249MSwgcGFkZGluZz0wKVxucHJpbnQoXCJTdGFuZGFyZCBvdXRwdXQgc2hhcGU6XCIsIGNvbnZfc3RkKHgpLnNoYXBlKSAgIyBbMSwxLDMsM11cblxuIyBEaWxhdGVkIDN4MyBjb252IChkPTIpOiBzZWVzIDV4NSByZWdpb24sIHNhbWUgcGFyYW1zXG5jb252X2RpbCA9IG5uLkNvbnYyZCgxLCAxLCAzLCBkaWxhdGlvbj0yLCBwYWRkaW5nPTApXG4jIFdpdGggZGlsYXRpb249MiwgZWZmZWN0aXZlIGtlcm5lbCBzaXplID0gMiooMy0xKSsxID0gNVxucHJpbnQoXCJEaWxhdGVkIG91dHB1dCBzaGFwZTpcIiwgY29udl9kaWwoeCkuc2hhcGUpICAgIyBbMSwxLDEsMV1cbnByaW50KFwiUmVjZXB0aXZlIGZpZWxkOiA1eDUgZnJvbSA5IHBhcmFtc1wiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikdyb3VwZWQgYW5kIERlcHRod2lzZSBDb252b2x1dGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikdyb3VwZWQgY29udm9sdXRpb25zIHNwbGl0IHRoZSBpbnB1dCBjaGFubmVscyBpbnRvIEcgZ3JvdXBzIGFuZCBhcHBseSBzZXBhcmF0ZSBjb252b2x1dGlvbnMgdG8gZWFjaC4gV2hlbiBncm91cHMgZXF1YWxzIHRoZSBudW1iZXIgb2YgaW5wdXQgY2hhbm5lbHMsIGVhY2ggY2hhbm5lbCBnZXRzIGl0cyBvd24gZmlsdGVyIOKAlCB0aGlzIGlzIGRlcHRod2lzZSBjb252b2x1dGlvbi4gQ29tYmluaW5nIGRlcHRod2lzZSBjb252IHdpdGggYSAxw5cxIHBvaW50d2lzZSBjb252IGdpdmVzIGRlcHRod2lzZSBzZXBhcmFibGUgY29udm9sdXRpb24sIHdoaWNoIGFjaGlldmVzIHNpbWlsYXIgY2FwYWNpdHkgYXMgc3RhbmRhcmQgY29udm9sdXRpb24gd2l0aCBhIGZyYWN0aW9uIG9mIHRoZSBwYXJhbWV0ZXJzIGFuZCBGTE9Qcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuQ19pbiwgQ19vdXQsIEgsIFcgPSAzMiwgNjQsIDgsIDhcbnggPSB0b3JjaC5yYW5kbigxLCBDX2luLCBILCBXKVxuXG4jIFN0YW5kYXJkIGNvbnZcbnN0ZCA9IG5uLkNvbnYyZChDX2luLCBDX291dCwgMywgcGFkZGluZz0xKVxuc3RkX3BhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gc3RkLnBhcmFtZXRlcnMoKSlcblxuIyBEZXB0aHdpc2Ugc2VwYXJhYmxlIGNvbnZcbmR3ID0gbm4uQ29udjJkKENfaW4sIENfaW4sIDMsIHBhZGRpbmc9MSwgZ3JvdXBzPUNfaW4pICAjIGRlcHRod2lzZVxucHcgPSBubi5Db252MmQoQ19pbiwgQ19vdXQsIDEpICAgICAgICAgICAgICAgICAgICAgICAgICAjIHBvaW50d2lzZVxuZHdzX3BhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbGlzdChkdy5wYXJhbWV0ZXJzKCkpICsgbGlzdChwdy5wYXJhbWV0ZXJzKCkpKVxuXG5wcmludChmXCJTdGFuZGFyZCBwYXJhbXM6IHtzdGRfcGFyYW1zfVwiKSAgICAgIyAxOCw0OTZcbnByaW50KGZcIkRXUyBwYXJhbXM6ICAgICAge2R3c19wYXJhbXN9XCIpICAgICAjIDIsMzM2ICAofjh4IGZld2VyKSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDb252IFR5cGUiLCJQYXJhbXMiLCJGTE9QcyIsIlJlY2VwdGl2ZSBGaWVsZCIsIlVzZSBDYXNlIl0sInJvd3MiOltbIlN0YW5kYXJkIiwiQ19pbiDDlyBDX291dCDDlyBrSCDDlyBrVyIsIkhpZ2giLCJrIMOXIGsiLCJHZW5lcmFsIGZlYXR1cmUgZXh0cmFjdGlvbiJdLFsiRGVwdGh3aXNlIiwiQ19pbiDDlyBrSCDDlyBrVyIsIlZlcnkgbG93IiwiayDDlyBrIHBlciBjaGFubmVsIiwiU3BhdGlhbCBmaWx0ZXJpbmcgKE1vYmlsZU5ldCkiXSxbIlBvaW50d2lzZSAoMcOXMSkiLCJDX2luIMOXIENfb3V0IiwiTG93IiwiMSDDlyAxIiwiQ2hhbm5lbCBtaXhpbmcgLyBwcm9qZWN0aW9uIl0sWyJHcm91cGVkIChHIGdyb3VwcykiLCJDX2luIMOXIENfb3V0IMOXIGtIIMOXIGtXIC8gRyIsIk1lZGl1bSIsImsgw5cgayIsIkVmZmljaWVudCBjaGFubmVsIHNlcGFyYXRpb24gKFJlc05lWHQpIl0sWyJEaWxhdGVkIiwiQ19pbiDDlyBDX291dCDDlyBrSCDDlyBrVyIsIkhpZ2giLCJkw5coay0xKSsxIMOXIGTDlyhrLTEpKzEiLCJTZWdtZW50YXRpb24sIGRlbnNlIHByZWRpY3Rpb24gKERlZXBMYWIpIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJjb250ZW50IjoiRGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbiByZWR1Y2VzIHBhcmFtcyBieSB+OOKAkznDlyB2cyBzdGFuZGFyZCBjb252b2x1dGlvbiBhdCBzaW1pbGFyIGFjY3VyYWN5IOKAlCB0aGlzIGlzIHRoZSBjb3JlIGluc2lnaHQgYmVoaW5kIE1vYmlsZU5ldC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgb3V0cHV0IHNpemUgZm9ybXVsYSAoSCsyUC1LKS9TKzEgaXMgZXNzZW50aWFsIGZvciBhcmNoaXRlY3R1cmFsIGRlc2lnbi4gU3RyaWRlLTIgY29udm9sdXRpb25zIHJlcGxhY2UgcG9vbGluZyBpbiBtb2Rlcm4gbmV0d29ya3MuIERpbGF0ZWQgY29udm9sdXRpb25zIGV4cGFuZCByZWNlcHRpdmUgZmllbGQgd2l0aG91dCBkb3duc2FtcGxpbmcg4oCUIGNyaXRpY2FsIGZvciBkZW5zZSB0YXNrcy4gRGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbnMgKGRlcHRod2lzZSArIHBvaW50d2lzZSkgb2ZmZXIgdGhlIGJlc3QgZWZmaWNpZW5jeSB0cmFkZS1vZmYgYW5kIHBvd2VyIGxpZ2h0d2VpZ2h0IG1vZGVscyBsaWtlIE1vYmlsZU5ldCwgRWZmaWNpZW50TmV0LCBhbmQgU2h1ZmZsZU5ldC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikdyb3VwZWQgY29udm9sdXRpb25zIHdpdGggRz0zMiBvciBHPTY0IChhcyBpbiBSZXNOZVh0KSBvZmZlciBhIG1pZGRsZSBncm91bmQ6IG1vcmUgZXhwcmVzc2l2ZSB0aGFuIGRlcHRod2lzZSBidXQgbW9yZSBlZmZpY2llbnQgdGhhbiBzdGFuZGFyZC4gVGhlIDHDlzEgcG9pbnR3aXNlIGNvbnZvbHV0aW9uIGlzIHRoZSBTd2lzcyBBcm15IGtuaWZlIG9mIENOTnMg4oCUIGl0IG1peGVzIGNoYW5uZWxzLCBjaGFuZ2VzIGRpbWVuc2lvbmFsaXR5LCBhbmQgYWRkcyBub24tbGluZWFyaXR5IGF0IG1pbmltYWwgY29zdC4gQ29tYmluaW5nIHRoZXNlIGJ1aWxkaW5nIGJsb2NrcyBlbmFibGVzIGRlc2lnbmluZyBlZmZpY2llbnQgYXJjaGl0ZWN0dXJlcyBmb3IgYW55IGNvbXB1dGUgYnVkZ2V0LiJ9XQ=="
---
# Convolution Operation in CNNs

## Overview

Convolution is the fundamental operation in convolutional neural networks. A learnable kernel slides across the input feature map, computing dot products at each position to produce an output feature map. This local connectivity and weight sharing dramatically reduce parameters compared to fully connected layers, while preserving spatial structure in visual data.

CNNs exploit three key properties: local connectivity (each output depends on a small input region), weight sharing (the same kernel is applied everywhere), and translation equivariance (shifting the input shifts the output by the same amount). These properties make convolutions ideal for image data where patterns can appear anywhere in the scene.

## 2D Convolution Math

For a 2D input X of shape (H, W) and kernel K of shape (kH, kW), the output Y at position (i, j) is computed as a sum of element-wise products: Y[i,j] = Σ_m Σ_n X[i+m, j+n] · K[m,n]. In deep learning, this operation is technically cross-correlation (no kernel flip), but is universally called convolution. Learnable bias is added after the summation.

```python
import numpy as np
import torch
import torch.nn.functional as F

def manual_cross_correlate(x, k):
    H, W = x.shape
    kH, kW = k.shape
    out = np.zeros((H - kH + 1, W - kW + 1))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = (x[i:i+kH, j:j+kW] * k).sum()
    return out

x_np = np.random.randn(6, 6).astype(np.float32)
k_np = np.random.randn(3, 3).astype(np.float32)
manual_out = manual_cross_correlate(x_np, k_np)
torch_out = F.conv2d(torch.tensor(x_np[None,None]), torch.tensor(k_np[None,None]))
print(np.allclose(manual_out, torch_out.numpy()[0,0], atol=1e-5))  # True
```

The output spatial size after convolution is determined by input size, kernel size, stride, and padding. For a 1D case: output_length = floor((input + 2*padding - kernel) / stride) + 1. In PyTorch, nn.Conv2d handles this automatically, but understanding the formula helps diagnose shape mismatches and design architectures with specific output resolutions.

## Stride and Padding

```python
import torch
import torch.nn as nn

def output_size(H, W, K, S, P):
    out_H = (H + 2*P - K) // S + 1
    out_W = (W + 2*P - K) // S + 1
    return out_H, out_W

# Standard: stride=1, no padding
print(output_size(32, 32, 3, 1, 0))   # (30, 30)
# Same padding: output == input
print(output_size(32, 32, 3, 1, 1))   # (32, 32)
# Stride-2 halving
print(output_size(32, 32, 3, 2, 1))   # (16, 16)
# Verify with nn.Conv2d
conv = nn.Conv2d(1, 1, kernel_size=3, stride=2, padding=1)
x = torch.zeros(1, 1, 32, 32)
print(conv(x).shape)  # torch.Size([1, 1, 16, 16])
```

Stride controls how far the kernel moves at each step. Stride=1 preserves spatial resolution; stride=2 halves it without explicit pooling, which is used in modern architectures like ResNet to reduce computation. Padding adds zeros around the input boundary. 'Same' padding (P = (K-1)/2 for odd kernels) maintains spatial dimensions and prevents information loss at edges.

## Dilated Convolutions

Dilated (atrous) convolutions insert gaps between kernel elements, expanding the receptive field without increasing parameters or losing spatial resolution. A dilation rate d=2 on a 3×3 kernel covers a 5×5 region; d=4 covers 9×9. This is especially useful for dense prediction tasks (segmentation, detection) where large context is needed at full resolution, as used in DeepLab and WaveNet architectures.

```python
import torch
import torch.nn as nn

x = torch.arange(25, dtype=torch.float32).reshape(1, 1, 5, 5)
print("Input:\n", x[0,0])

# Standard 3x3 conv: sees 3x3 region
conv_std = nn.Conv2d(1, 1, 3, dilation=1, padding=0)
print("Standard output shape:", conv_std(x).shape)  # [1,1,3,3]

# Dilated 3x3 conv (d=2): sees 5x5 region, same params
conv_dil = nn.Conv2d(1, 1, 3, dilation=2, padding=0)
# With dilation=2, effective kernel size = 2*(3-1)+1 = 5
print("Dilated output shape:", conv_dil(x).shape)   # [1,1,1,1]
print("Receptive field: 5x5 from 9 params")
```

## Grouped and Depthwise Convolutions

Grouped convolutions split the input channels into G groups and apply separate convolutions to each. When groups equals the number of input channels, each channel gets its own filter — this is depthwise convolution. Combining depthwise conv with a 1×1 pointwise conv gives depthwise separable convolution, which achieves similar capacity as standard convolution with a fraction of the parameters and FLOPs.

```python
import torch
import torch.nn as nn

C_in, C_out, H, W = 32, 64, 8, 8
x = torch.randn(1, C_in, H, W)

# Standard conv
std = nn.Conv2d(C_in, C_out, 3, padding=1)
std_params = sum(p.numel() for p in std.parameters())

# Depthwise separable conv
dw = nn.Conv2d(C_in, C_in, 3, padding=1, groups=C_in)  # depthwise
pw = nn.Conv2d(C_in, C_out, 1)                          # pointwise
dws_params = sum(p.numel() for p in list(dw.parameters()) + list(pw.parameters()))

print(f"Standard params: {std_params}")     # 18,496
print(f"DWS params:      {dws_params}")     # 2,336  (~8x fewer)
```

| Conv Type | Params | FLOPs | Receptive Field | Use Case |
| --- | --- | --- | --- | --- |
| Standard | C_in × C_out × kH × kW | High | k × k | General feature extraction |
| Depthwise | C_in × kH × kW | Very low | k × k per channel | Spatial filtering (MobileNet) |
| Pointwise (1×1) | C_in × C_out | Low | 1 × 1 | Channel mixing / projection |
| Grouped (G groups) | C_in × C_out × kH × kW / G | Medium | k × k | Efficient channel separation (ResNeXt) |
| Dilated | C_in × C_out × kH × kW | High | d×(k-1)+1 × d×(k-1)+1 | Segmentation, dense prediction (DeepLab) |

> **info**: Depthwise separable convolution reduces params by ~8–9× vs standard convolution at similar accuracy — this is the core insight behind MobileNet.

## Key Takeaways

The output size formula (H+2P-K)/S+1 is essential for architectural design. Stride-2 convolutions replace pooling in modern networks. Dilated convolutions expand receptive field without downsampling — critical for dense tasks. Depthwise separable convolutions (depthwise + pointwise) offer the best efficiency trade-off and power lightweight models like MobileNet, EfficientNet, and ShuffleNet.

Grouped convolutions with G=32 or G=64 (as in ResNeXt) offer a middle ground: more expressive than depthwise but more efficient than standard. The 1×1 pointwise convolution is the Swiss Army knife of CNNs — it mixes channels, changes dimensionality, and adds non-linearity at minimal cost. Combining these building blocks enables designing efficient architectures for any compute budget.

