---
title: "Convolution Operation — Cross-Correlation, Padding, Stride, Dilation"
slug: "convolution-operation"
description: "Derive 2D convolution from first principles, contrast it with cross-correlation, and master stride, padding, dilation, and multi-channel extensions with FLOP analysis."
tags: ["deep-learning", "cnns"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udm9sdXRpb24gaXMgdGhlIGNvcmUgYnVpbGRpbmcgYmxvY2sgb2YgZXZlcnkgY29udm9sdXRpb25hbCBuZXVyYWwgbmV0d29yay4gSW4gc2lnbmFsIHByb2Nlc3NpbmcsIGNvbnZvbHV0aW9uIGlzIGRlZmluZWQgYXMgKGbimIVnKVtuXSA9IM6j4oKWIGZba13Ct2dbbi1rXSwgd2hlcmUgdGhlIGtlcm5lbCBpcyBmbGlwcGVkIGJlZm9yZSBzbGlkaW5nLiBEZWVwIGxlYXJuaW5nIGZyYW1ld29ya3MgaW1wbGVtZW50IGNyb3NzLWNvcnJlbGF0aW9uIOKAlCB0aGUga2VybmVsIGlzIE5PVCBmbGlwcGVkIOKAlCBidXQgdGhlIG9wZXJhdGlvbiBpcyBzdGlsbCBjYWxsZWQgY29udm9sdXRpb24gYmVjYXVzZSB0aGUgbmV0d29yayBsZWFybnMgdGhlIGtlcm5lbCBhbnl3YXkuIFVuZGVyc3RhbmRpbmcgdGhlIG1hdGhlbWF0aWNzIGJlaGluZCBvdXRwdXQgc2l6ZSwgcmVjZXB0aXZlIGZpZWxkLCBhbmQgY29tcHV0YXRpb25hbCBjb3N0IGlzIGVzc2VudGlhbCBmb3IgZGVzaWduaW5nIGVmZmljaWVudCBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNyb3NzLUNvcnJlbGF0aW9uIHZzIFRydWUgQ29udm9sdXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRydWUgY29udm9sdXRpb24gZmxpcHMgdGhlIGtlcm5lbDogKGbimIVnKVtpLGpdID0gzqPigpXOo3cgZltoLHddwrdnW2ktaCwgai13XS4gQ3Jvc3MtY29ycmVsYXRpb24gZG9lcyBub3QgZmxpcDogKGbii4ZnKVtpLGpdID0gzqPigpXOo3cgZltpK2gsIGord13Ct2dbaCx3XS4gRm9yIGEgbGVhcm5lZCBrZXJuZWwgdGhlIGRpc3RpbmN0aW9uIGlzIGlycmVsZXZhbnQg4oCUIHRoZSBuZXR3b3JrIGNhbiBhYnNvcmIgdGhlIGZsaXAgaW50byB0aGUgbGVhcm5lZCB3ZWlnaHRzLiBQeVRvcmNoXHUwMDI3cyBubi5Db252MmQgYW5kIEYuY29udjJkIGltcGxlbWVudCBjcm9zcy1jb3JyZWxhdGlvbi4gVGhlIG1hdGhlbWF0aWNhbCBjb252b2x1dGlvbiB0aGVvcmVtIChjb252b2x1dGlvbiBpbiBzcGF0aWFsIGRvbWFpbiA9IG11bHRpcGxpY2F0aW9uIGluIGZyZXF1ZW5jeSBkb21haW4pIGFwcGxpZXMgdG8gdHJ1ZSBjb252b2x1dGlvbjsgaW4gcHJhY3RpY2UgQ05OcyBhcmUgZGVzaWduZWQgYXJvdW5kIGNyb3NzLWNvcnJlbGF0aW9uIGFuZCB0aGUgdGVybSBcdTAwMjdjb252b2x1dGlvblx1MDAyNyBpcyB1c2VkIGxvb3NlbHkgdGhyb3VnaG91dCB0aGUgZmllbGQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiMkQgQ29udm9sdXRpb24gZnJvbSBTY3JhdGNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBzaW5nbGUtY2hhbm5lbCBpbnB1dCBvZiBzaGFwZSBIw5dXIGFuZCBhIGtlcm5lbCBvZiBzaGFwZSBrw5drLCB0aGUgb3V0cHV0IGF0IHBvc2l0aW9uIChpLGopIGlzOiBvdXRwdXRbaSxqXSA9IM6j4oKVzqN3IGlucHV0W2nCt3MraCwgasK3cyt3XSDCtyBrZXJuZWxbaCx3XSwgd2hlcmUgcyBpcyB0aGUgc3RyaWRlLiBXaXRoIHBhZGRpbmcgcCB6ZXJvcyBhZGRlZCBvbiBlYWNoIHNpZGUsIHRoZSBvdXRwdXQgc3BhdGlhbCBkaW1lbnNpb25zIGFyZTogSF9vdXQgPSAoSCArIDJwIC0gaykgLy8gcyArIDEsIFdfb3V0ID0gKFcgKyAycCAtIGspIC8vIHMgKyAxLiBGb3IgbXVsdGktY2hhbm5lbCBpbnB1dHMgKENfaW4gY2hhbm5lbHMpLCBlYWNoIG91dHB1dCBjaGFubmVsIGhhcyBvbmUga2VybmVsIHBlciBpbnB1dCBjaGFubmVsIGFuZCB0aGUgcmVzdWx0cyBhcmUgc3VtbWVkOiB0aGUgcGFyYW1ldGVyIGNvdW50IHBlciBvdXRwdXQgY2hhbm5lbCBpcyBrw5drw5dDX2luLCBhbmQgZm9yIENfb3V0IG91dHB1dCBjaGFubmVscyB0aGUgdG90YWwgaXMga8OXa8OXQ19pbsOXQ19vdXQgKyBDX291dCAoYmlhcykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY29udjJkX3NjcmF0Y2goeCwga2VybmVsLCBzdHJpZGU9MSwgcGFkZGluZz0wKTpcbiAgICBcIlwiXCJDcm9zcy1jb3JyZWxhdGlvbiAod2hhdCBETCBmcmFtZXdvcmtzIGNhbGwgXHUwMDI3Y29udm9sdXRpb25cdTAwMjcpLlwiXCJcIlxuICAgIGlmIHBhZGRpbmcgXHUwMDNlIDA6XG4gICAgICAgIHggPSBucC5wYWQoeCwgWygwLDApLCgwLDApLChwYWRkaW5nLHBhZGRpbmcpLChwYWRkaW5nLHBhZGRpbmcpXSlcbiAgICBOLCBDX2luLCBILCBXID0geC5zaGFwZVxuICAgIENfb3V0LCBfLCBrLCBfID0ga2VybmVsLnNoYXBlXG4gICAgSF9vdXQgPSAoSCAtIGspIC8vIHN0cmlkZSArIDFcbiAgICBXX291dCA9IChXIC0gaykgLy8gc3RyaWRlICsgMVxuICAgIG91dCA9IG5wLnplcm9zKChOLCBDX291dCwgSF9vdXQsIFdfb3V0KSlcbiAgICBmb3IgbiBpbiByYW5nZShOKTpcbiAgICAgICAgZm9yIGNvIGluIHJhbmdlKENfb3V0KTpcbiAgICAgICAgICAgIGZvciBjaSBpbiByYW5nZShDX2luKTpcbiAgICAgICAgICAgICAgICBmb3IgaSBpbiByYW5nZShIX291dCk6XG4gICAgICAgICAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKFdfb3V0KTpcbiAgICAgICAgICAgICAgICAgICAgICAgIHBhdGNoID0geFtuLCBjaSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBpKnN0cmlkZTppKnN0cmlkZStrLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGoqc3RyaWRlOmoqc3RyaWRlK2tdXG4gICAgICAgICAgICAgICAgICAgICAgICBvdXRbbiwgY28sIGksIGpdICs9IChwYXRjaCAqIGtlcm5lbFtjbywgY2ldKS5zdW0oKVxuICAgIHJldHVybiBvdXRcblxubnAucmFuZG9tLnNlZWQoMClcbnggPSBucC5yYW5kb20ucmFuZG4oMSwgMywgOCwgOCkgICAgICAgIyAoTiwgQ19pbiwgSCwgVylcbmsgPSBucC5yYW5kb20ucmFuZG4oMTYsIDMsIDMsIDMpICAgICAgIyAoQ19vdXQsIENfaW4sIGtILCBrVylcbm91dCA9IGNvbnYyZF9zY3JhdGNoKHgsIGssIHN0cmlkZT0xLCBwYWRkaW5nPTEpXG5wcmludChcdTAwMjdJbnB1dDogXHUwMDI3LCB4LnNoYXBlKVxucHJpbnQoXHUwMDI3S2VybmVsOlx1MDAyNywgay5zaGFwZSlcbnByaW50KFx1MDAyN091dHB1dDpcdTAwMjcsIG91dC5zaGFwZSkgICMgKDEsIDE2LCA4LCA4KSDigJQgc2FtZSBwYWRkaW5nIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGFkZGluZyBhbmQgU3RyaWRlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQYWRkaW5nIGNvbnRyb2xzIG91dHB1dCBzaXplIHJlbGF0aXZlIHRvIGlucHV0LiBWYWxpZCBwYWRkaW5nIChwPTApOiBubyB6ZXJvcyBhZGRlZCwgb3V0cHV0IHNocmlua3MgYnkgay0xIHBlciBzaWRlLiBTYW1lIHBhZGRpbmcgKHA9KGstMSkvMiBmb3Igb2RkIGspOiBvdXRwdXQgaGFzIHRoZSBzYW1lIEjDl1cgYXMgaW5wdXQuIFN0cmlkZSBzIGNvbnRyb2xzIHRoZSBzdGVwIHNpemUgb2YgdGhlIHNsaWRpbmcgd2luZG93OiBzdHJpZGUgMiBoYWx2ZXMgdGhlIHNwYXRpYWwgZGltZW5zaW9ucyAoY2hlYXBlciB0aGFuIHBvb2xpbmcsIGxlYXJuYWJsZSkuIENvbWJpbmluZyBzdHJpZGUgYW5kIHBhZGRpbmc6IEhfb3V0ID0g4oyKKEgrMnAtaykvc+KMiyArIDEuIEluIHByYWN0aWNlLCBrPTMsIHA9MSwgcz0xIGlzIHRoZSB3b3JraG9yc2UgKHByZXNlcnZlcyBzaXplKTsgaz0zLCBwPTEsIHM9MiBvciBrPTEsIHA9MCwgcz0yIGlzIHVzZWQgZm9yIGRvd25zYW1wbGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxueCA9IHRvcmNoLnJhbmRuKDEsIDMsIDMyLCAzMilcblxuY29uZmlncyA9IFtcbiAgICBkaWN0KGtlcm5lbF9zaXplPTMsIHN0cmlkZT0xLCBwYWRkaW5nPTAsIGRpbGF0aW9uPTEpLCAgICMgdmFsaWRcbiAgICBkaWN0KGtlcm5lbF9zaXplPTMsIHN0cmlkZT0xLCBwYWRkaW5nPTEsIGRpbGF0aW9uPTEpLCAgICMgc2FtZVxuICAgIGRpY3Qoa2VybmVsX3NpemU9Mywgc3RyaWRlPTIsIHBhZGRpbmc9MSwgZGlsYXRpb249MSksICAgIyBzdHJpZGUtMiBkb3duXG4gICAgZGljdChrZXJuZWxfc2l6ZT0zLCBzdHJpZGU9MSwgcGFkZGluZz0yLCBkaWxhdGlvbj0yKSwgICAjIGRpbGF0ZWRcbiAgICBkaWN0KGtlcm5lbF9zaXplPTUsIHN0cmlkZT0xLCBwYWRkaW5nPTIsIGRpbGF0aW9uPTEpLCAgICMgNXg1IHNhbWVcbiAgICBkaWN0KGtlcm5lbF9zaXplPTEsIHN0cmlkZT0xLCBwYWRkaW5nPTAsIGRpbGF0aW9uPTEpLCAgICMgcG9pbnR3aXNlXG5dXG5cbnByaW50KGZcdTAwMjd7XHUwMDI3Q29uZmlnXHUwMDI3Olx1MDAzYzQwfSBPdXRwdXQgc2hhcGVcdTAwMjcpXG5mb3IgY2ZnIGluIGNvbmZpZ3M6XG4gICAgY29udiA9IG5uLkNvbnYyZCgzLCAxNiwgKipjZmcpXG4gICAgb3V0ID0gY29udih4KVxuICAgIGssIHMsIHAsIGQgPSBjZmdbXHUwMDI3a2VybmVsX3NpemVcdTAwMjddLCBjZmdbXHUwMDI3c3RyaWRlXHUwMDI3XSwgY2ZnW1x1MDAyN3BhZGRpbmdcdTAwMjddLCBjZmdbXHUwMDI3ZGlsYXRpb25cdTAwMjddXG4gICAgbGFiZWwgPSBmXHUwMDI3az17a30gcz17c30gcD17cH0gZD17ZH1cdTAwMjdcbiAgICBwcmludChmXHUwMDI3e2xhYmVsOlx1MDAzYzQwfSB7dHVwbGUob3V0LnNoYXBlKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGlsYXRpb24g4oCUIEV4cGFuZGluZyBSZWNlcHRpdmUgRmllbGQgZm9yIEZyZWUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpbGF0aW9uIChhdHJvdXMgY29udm9sdXRpb24pIGluc2VydHMgZC0xIHplcm9zIGJldHdlZW4ga2VybmVsIGVsZW1lbnRzLiBBIDPDlzMga2VybmVsIHdpdGggZGlsYXRpb24gZD0yIHNhbXBsZXMgNcOXNSByZWdpb25zOyB3aXRoIGQ9MyBpdCBzYW1wbGVzIDfDlzcuIFRoZSBlZmZlY3RpdmUga2VybmVsIHNpemUgaXMgKGstMSnCt2QgKyAxLCBidXQgdGhlIHBhcmFtZXRlciBjb3VudCByZW1haW5zIGvDl2vDl0NfaW7Dl0Nfb3V0LiBUaGlzIGlzIGh1Z2VseSB2YWx1YWJsZSBmb3Igc2VtYW50aWMgc2VnbWVudGF0aW9uIChEZWVwTGFiKSBhbmQgYXVkaW8gZ2VuZXJhdGlvbiAoV2F2ZU5ldCkgd2hlcmUgbGFyZ2UgY29udGV4dCBpcyBuZWVkZWQgd2l0aG91dCBzdHJpZGVkIGRvd25zYW1wbGluZy4gSHlicmlkIGRpbGF0ZWQgY29udm9sdXRpb24gKEhEQykgc3RhY2tzIGxheWVycyB3aXRoIGdyb3dpbmcgZGlsYXRpb24gcmF0ZXMgKDEsIDIsIDUpIHRvIGF2b2lkIHRoZSBcdTAwMjdncmlkZGluZyBhcnRlZmFjdFx1MDAyNyB3aGVyZSBkaWxhdGVkIGNvbnZvbHV0aW9ucyBtaXNzIGlucHV0IHBpeGVscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGVmZmVjdGl2ZV9yZihrZXJuZWxfc2l6ZSwgZGlsYXRpb24pOlxuICAgIFwiXCJcIkVmZmVjdGl2ZSByZWNlcHRpdmUgZmllbGQgc2l6ZSBmb3IgYSBzaW5nbGUgZGlsYXRlZCBjb252IGxheWVyLlwiXCJcIlxuICAgIHJldHVybiAoa2VybmVsX3NpemUgLSAxKSAqIGRpbGF0aW9uICsgMVxuXG5kaWxhdGlvbnMgPSBbMSwgMiwgNCwgOCwgMTZdXG5wcmludChmXHUwMDI3e1x1MDAyN0RpbGF0aW9uXHUwMDI3Olx1MDAzYzEwfSB7XHUwMDI3RWZmLiBrZXJuZWxcdTAwMjc6XHUwMDNjMTR9IHtcdTAwMjdSRiBjb3ZlcmVkXHUwMDI3Olx1MDAzYzEyfSBQYXJhbXMgKDN4MywgNjQtXHUwMDNlNjQpXHUwMDI3KVxuZm9yIGQgaW4gZGlsYXRpb25zOlxuICAgIGVmZiA9IGVmZmVjdGl2ZV9yZigzLCBkKVxuICAgIHBhcmFtcyA9IDMgKiAzICogNjQgKiA2NCArIDY0ICAjIGZpeGVkIHJlZ2FyZGxlc3Mgb2YgZGlsYXRpb25cbiAgICBwcmludChmXHUwMDI3e2Q6XHUwMDNjMTB9IHtlZmZ9eHtlZmY6XHUwMDNjMTB9IHtlZmYqZWZmOlx1MDAzYzEyfSB7cGFyYW1zOix9XHUwMDI3KVxuXG4jIENvbXBhcmUgb3V0cHV0IHNoYXBlc1xueCA9IHRvcmNoLnJhbmRuKDEsIDEsIDE2LCAxNilcbmZvciBkIGluIFsxLCAyLCA0XTpcbiAgICBjb252ID0gbm4uQ29udjJkKDEsIDEsIGtlcm5lbF9zaXplPTMsIHBhZGRpbmc9ZCwgZGlsYXRpb249ZClcbiAgICBwcmludChmXHUwMDI3ZGlsYXRpb249e2R9OiBvdXQge3R1cGxlKGNvbnYoeCkuc2hhcGUpfSAoc2FtZS1zaXplIHdpdGggcD1kKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWaXN1YWxpc2luZyBMZWFybmVkIEtlcm5lbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZpcnN0LWxheWVyIGtlcm5lbHMgb2YgYSBuZXR3b3JrIHRyYWluZWQgb24gbmF0dXJhbCBpbWFnZXMgbGVhcm4gR2Fib3ItbGlrZSBmaWx0ZXJzIOKAlCBvcmllbnRlZCBlZGdlIGRldGVjdG9ycywgY29sb3VyIGJsb2JzLCBhbmQgZnJlcXVlbmN5IGRldGVjdG9ycyDigJQgYmVjYXVzZSB0aGVzZSBhcmUgdGhlIG1vc3QgZWZmaWNpZW50IGJhc2lzIGZvciBuYXR1cmFsIGltYWdlIHN0YXRpc3RpY3MuIFZpc3VhbGlzaW5nIHRoZW0gY29uZmlybXMgdGhlIG5ldHdvcmsgaXMgbGVhcm5pbmcgbWVhbmluZ2Z1bCBmZWF0dXJlcyByYXRoZXIgdGhhbiBub2lzZS4gRm9yIGRlZXBlciBsYXllcnMsIGFjdGl2YXRpb24gbWF4aW1pc2F0aW9uIG9yIGZlYXR1cmUgaW52ZXJzaW9uIGlzIG5lZWRlZC4gV2VpZ2h0IGluaXRpYWxpc2F0aW9uIG1hdHRlcnM6IEhlL0thaW1pbmcgaW5pdCBzZXRzIHN0ZCA9IHNxcnQoMi9mYW5faW4pIGZvciBSZUxVIG5ldHdvcmtzLCBwcmV2ZW50aW5nIHZhbmlzaGluZy9leHBsb2RpbmcgYWN0aXZhdGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNodmlzaW9uLm1vZGVscyBhcyBtb2RlbHNcbmltcG9ydCBtYXRwbG90bGliXG5tYXRwbG90bGliLnVzZShcdTAwMjdBZ2dcdTAwMjcpXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBMb2FkIHByZXRyYWluZWQgUmVzTmV0LTE4IGFuZCBleHRyYWN0IGZpcnN0IGNvbnYgbGF5ZXIga2VybmVsc1xubW9kZWwgPSBtb2RlbHMucmVzbmV0MTgod2VpZ2h0cz1tb2RlbHMuUmVzTmV0MThfV2VpZ2h0cy5ERUZBVUxUKVxua2VybmVscyA9IG1vZGVsLmNvbnYxLndlaWdodC5kYXRhLmNsb25lKCkgICMgKDY0LCAzLCA3LCA3KVxuXG4jIE5vcm1hbGl6ZSBlYWNoIGtlcm5lbCBmb3IgdmlzdWFsaXphdGlvblxuZGVmIG5vcm1hbGl6ZSh0KTpcbiAgICB0ID0gdCAtIHQubWluKClcbiAgICByZXR1cm4gdCAvICh0Lm1heCgpICsgMWUtOClcblxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDQsIDgsIGZpZ3NpemU9KDEyLCA2KSlcbmZvciBpZHgsIGF4IGluIGVudW1lcmF0ZShheGVzLmZsYXQpOlxuICAgIGlmIGlkeCBcdTAwM2MgMzI6XG4gICAgICAgIGsgPSBub3JtYWxpemUoa2VybmVsc1tpZHhdLnBlcm11dGUoMSwgMiwgMCkubnVtcHkoKSlcbiAgICAgICAgYXguaW1zaG93KGspXG4gICAgYXguYXhpcyhcdTAwMjdvZmZcdTAwMjcpXG5wbHQuc3VwdGl0bGUoXHUwMDI3Rmlyc3QgMzIgb2YgNjQgUmVzTmV0LTE4IGNvbnYxIGtlcm5lbHMgKDd4NywgUkdCKVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3a2VybmVscy5wbmdcdTAwMjcsIGRwaT04MClcbnByaW50KGZcdTAwMjdjb252MSBrZXJuZWwgc2hhcGU6IHt0dXBsZShrZXJuZWxzLnNoYXBlKX1cdTAwMjcpXG5wcmludChmXHUwMDI3UGFyYW1zIGluIGNvbnYxOiB7a2VybmVscy5udW1lbCgpOix9ICgrIHttb2RlbC5jb252MS5iaWFzIGlzIE5vbmUgYW5kIDB9IGJpYXMpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXB1dGF0aW9uYWwgQ29zdCBBbmFseXNpcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGZsb2F0aW5nLXBvaW50IG9wZXJhdGlvbnMgKEZMT1BzKSBmb3IgYSBjb252b2x1dGlvbiBsYXllciBhcmU6IEZMT1BzIOKJiCAyIMOXIEhfb3V0IMOXIFdfb3V0IMOXIENfaW4gw5cgQ19vdXQgw5cga8KyLiBUaGUgZmFjdG9yIDIgYWNjb3VudHMgZm9yIG11bHRpcGx5LWFjY3VtdWxhdGUgKE1BQyA9IDEgbXVsdGlwbHkgKyAxIGFkZCkuIEZvciBhIHR5cGljYWwgUmVzTmV0LTUwIGxheWVyIHdpdGggSF9vdXQ9NTYsIFdfb3V0PTU2LCBDX2luPTY0LCBDX291dD02NCwgaz0zOiBGTE9QcyDiiYggMsOXNTbDlzU2w5c2NMOXNjTDlzkg4omIIDIuMyBHRkxPUHMgZm9yIHRoYXQgc2luZ2xlIGxheWVyLiBNZW1vcnkgYmFuZHdpZHRoIG9mdGVuIGJvdHRsZW5lY2tzIHRocm91Z2hwdXQgYmVmb3JlIGNvbXB1dGUgZG9lcywgZXNwZWNpYWxseSBmb3IgbGFyZ2UgZmVhdHVyZSBtYXBzLiBSZWR1Y2luZyBDX2luIG9yIENfb3V0IGJ5IDLDlyBzYXZlcyA0w5cgRkxPUHM7IHJlZHVjaW5nIGsgZnJvbSAzIHRvIDEgc2F2ZXMgOcOXIEZMT1BzIGF0IHRoZSBjb3N0IG9mIG5vIHNwYXRpYWwgbWl4aW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgY29udl9mbG9wcyhIX2luLCBXX2luLCBDX2luLCBDX291dCwgaywgcz0xLCBwPTApOlxuICAgIEhfb3V0ID0gKEhfaW4gKyAyKnAgLSBrKSAvLyBzICsgMVxuICAgIFdfb3V0ID0gKFdfaW4gKyAyKnAgLSBrKSAvLyBzICsgMVxuICAgICMgMiBvcHMgcGVyIE1BQyAobXVsdGlwbHkgKyBhZGQpLCBrKmsgTUFDcyBwZXIgb3V0cHV0IGVsZW1lbnQgcGVyIGlucHV0IGNoYW5uZWxcbiAgICBmbG9wcyA9IDIgKiBIX291dCAqIFdfb3V0ICogQ19pbiAqIENfb3V0ICogayAqIGtcbiAgICBwYXJhbXMgPSBDX291dCAqIENfaW4gKiBrICogayArIENfb3V0XG4gICAgcmV0dXJuIEhfb3V0LCBXX291dCwgZmxvcHMsIHBhcmFtc1xuXG5sYXllcnMgPSBbXG4gICAgKFx1MDAyN2NvbnYxIGs9N1x1MDAyNywgIDIyNCwgMjI0LCAzLCAgIDY0LCAgNywgMiwgMyksXG4gICAgKFx1MDAyN2xheWVyMSBrPTNcdTAwMjcsIDU2LCAgNTYsICA2NCwgIDY0LCAgMywgMSwgMSksXG4gICAgKFx1MDAyN2xheWVyMSBrPTFcdTAwMjcsIDU2LCAgNTYsICA2NCwgIDY0LCAgMSwgMSwgMCksXG4gICAgKFx1MDAyN2xheWVyNCBrPTNcdTAwMjcsIDcsICAgNywgICA1MTIsIDUxMiwgMywgMSwgMSksXG4gICAgKFx1MDAyN3B3ICBrPTFcdTAwMjcsICAgIDE0LCAgMTQsICAyNTYsIDEwMjQsMSwgMSwgMCksXG5dXG5wcmludChmXHUwMDI3e1x1MDAyN0xheWVyXHUwMDI3Olx1MDAzYzE0fSB7XHUwMDI3SHhXIG91dFx1MDAyNzpcdTAwM2MxMH0ge1x1MDAyN0dGTE9Qc1x1MDAyNzpcdTAwM2U4fSB7XHUwMDI3UGFyYW1zXHUwMDI3Olx1MDAzZTEwfVx1MDAyNylcbmZvciBuYW1lLCBILCBXLCBDaSwgQ28sIGssIHMsIHAgaW4gbGF5ZXJzOlxuICAgIEhvLCBXbywgZmwsIHBhID0gY29udl9mbG9wcyhILCBXLCBDaSwgQ28sIGssIHMsIHApXG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lOlx1MDAzYzE0fSB7SG99eHtXbzpcdTAwM2M2fSB7ZmwvMWU5Olx1MDAzZTguM2Z9IHtwYTpcdTAwM2UxMCx9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2VpZ2h0IFNoYXJpbmcgPSBUcmFuc2xhdGlvbiBFcXVpdmFyaWFuY2UiLCJjb250ZW50IjoiVGhlIHNhbWUga2VybmVsIGlzIGFwcGxpZWQgYXQgZXZlcnkgc3BhdGlhbCBsb2NhdGlvbiDigJQgdGhpcyBpcyB3ZWlnaHQgc2hhcmluZy4gSXQgbWVhbnMgYSBmZWF0dXJlIGRldGVjdG9yIHRyYWluZWQgb24gYSBjYXQgaW4gdGhlIHVwcGVyLWxlZnQgd29ya3MgZXF1YWxseSB3ZWxsIGluIHRoZSBsb3dlci1yaWdodC4gRm9ybWFsbHksIGlmIFRfZCBkZW5vdGVzIGEgc2hpZnQtYnktZCBvcGVyYXRvciwgY29udm9sdXRpb24gc2F0aXNmaWVzIGYoVF9kIHgpID0gVF9kKGYoeCkpOiBzaGlmdGluZyB0aGUgaW5wdXQgc2hpZnRzIHRoZSBvdXRwdXQgYnkgdGhlIHNhbWUgYW1vdW50LiBUaGlzIGluZHVjdGl2ZSBiaWFzIGRyYW1hdGljYWxseSByZWR1Y2VzIHRoZSBwYXJhbWV0ZXJzIG5lZWRlZCBhbmQgaXMgd2h5IENOTnMgZ2VuZXJhbGlzZSBzbyB3ZWxsIG9uIGltYWdlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1DaGFubmVsIEV4dGVuc2lvbiBhbmQgUGFyYW1ldGVyIENvdW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYW4gaW5wdXQgd2l0aCBDX2luIGNoYW5uZWxzIGFuZCBDX291dCBvdXRwdXQgY2hhbm5lbHMsIHRoZSBrZXJuZWwgdGVuc29yIGhhcyBzaGFwZSAoQ19vdXQsIENfaW4sIGssIGspLiBFYWNoIG91dHB1dCBjaGFubmVsIGlzIHByb2R1Y2VkIGJ5IGNvbnZvbHZpbmcgdGhlIGZ1bGwgQ19pbi1jaGFubmVsIGlucHV0IHdpdGggb25lIChDX2luLCBrLCBrKSBrZXJuZWwgYW5kIHN1bW1pbmcgYWNyb3NzIGNoYW5uZWxzLiBUaGUgcGFyYW1ldGVyIGNvdW50IGlzIENfb3V0IMOXIENfaW4gw5cgayDDlyBrICsgQ19vdXQgKGJpYXMpLiBGb3Igaz0zLCBDX2luPTI1NiwgQ19vdXQ9MjU2OiAyNTbDlzI1NsOXOSArIDI1NiA9IDU5MCwwODAgcGFyYW1ldGVycy4gQ29tcGFyZTogYSBmdWxseS1jb25uZWN0ZWQgbGF5ZXIgbWFwcGluZyB0aGUgc2FtZSAyNTbDlzfDlzcgPSAxMiw1NDQgZmVhdHVyZXMgdG8gMTIsNTQ0IG91dHB1dHMgd291bGQgbmVlZCAxMiw1NDTCsiDiiYggMTU3TSBwYXJhbWV0ZXJzIOKAlCAyNjbDlyBtb3JlLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQYXJhbWV0ZXIiLCJFZmZlY3Qgb24gT3V0cHV0IFNpemUiLCJFZmZlY3Qgb24gUmVjZXB0aXZlIEZpZWxkIiwiRWZmZWN0IG9uIFBhcmFtcyIsIkVmZmVjdCBvbiBGTE9QcyJdLCJyb3dzIjpbWyJLZXJuZWwgc2l6ZSBr4oaRIiwiKEgrMnAtaykvL3MrMSBzaHJpbmtzIiwiR3Jvd3MgbGluZWFybHkgd2l0aCBrIiwiw5drwrIgcGVyIGxheWVyIiwiw5drwrIiXSxbIlN0cmlkZSBz4oaRIiwiRGl2aWRlcyBieSBzIChkb3duc2FtcGxlcykiLCJNdWx0aXBsaWVzIGFsbCBkb3duc3RyZWFtIFJGIiwiVW5jaGFuZ2VkIiwiw7dzwrIiXSxbIlBhZGRpbmcgcOKGkSIsIisoMnApIGJlZm9yZSBkaXZpc2lvbiIsIk5vIGVmZmVjdCIsIlVuY2hhbmdlZCIsIlNsaWdodGx5IOKGkSJdLFsiRGlsYXRpb24gZOKGkSIsIlVuY2hhbmdlZCAod2l0aCBwPWQpIiwiw5dkIHBlciBsYXllciIsIlVuY2hhbmdlZCIsIlVuY2hhbmdlZCJdLFsiQ19pbuKGkSIsIlVuY2hhbmdlZCIsIlVuY2hhbmdlZCIsIsOXQ19pbiIsIsOXQ19pbiJdLFsiQ19vdXTihpEiLCJNb3JlIG91dHB1dCBjaGFubmVscyIsIlVuY2hhbmdlZCIsIsOXQ19vdXQiLCLDl0Nfb3V0Il1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlZhbGlkIHBhZGRpbmcgKHA9MCk6IG91dHB1dCBzaHJpbmtzIGJ5IGstMSBlYWNoIHNpZGUg4oCUIHVzZSB3aGVuIHJlZHVjaW5nIHNwYXRpYWwgc2l6ZSBpbnRlbnRpb25hbGx5LiIsIlNhbWUgcGFkZGluZyAocD0oay0xKS8vMik6IG91dHB1dCBtYXRjaGVzIGlucHV0IHNpemUg4oCUIHN0YW5kYXJkIGluIHJlc2lkdWFsIGJsb2Nrcy4iLCJTQU1FIHZzIFZBTElEIGluIFRlbnNvckZsb3c6IFNBTUUgYWRkcyBhc3ltbWV0cmljIHBhZGRpbmc7IFB5VG9yY2ggcmVxdWlyZXMgbWFudWFsIHNwZWNpZmljYXRpb24uIiwiR3JvdXBlZCBjb252b2x1dGlvbiAoZ3JvdXBzPWcpOiByZWR1Y2VzIHBhcmFtcyBhbmQgRkxPUHMgYnkgZmFjdG9yIGcg4oCUIGNvdmVyZWQgaW4gdGhlIG5leHQgbm90ZS4iLCJCaWFzIGNhbiBiZSBvbWl0dGVkIChiaWFzPUZhbHNlKSB3aGVuIEJhdGNoTm9ybSBmb2xsb3dzIOKAlCBCTiBoYXMgaXRzIG93biBsZWFybmFibGUgc2hpZnQgcGFyYW1ldGVyLiIsIk91dHB1dCBjaGFubmVsIG9yZGVyaW5nOiBQeVRvcmNoIHVzZXMgKE4sIEMsIEgsIFcpOyBUZW5zb3JGbG93IGRlZmF1bHRzIHRvIChOLCBILCBXLCBDKS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Convolution Operation — Cross-Correlation, Padding, Stride, Dilation

Convolution is the core building block of every convolutional neural network. In signal processing, convolution is defined as (f★g)[n] = Σₖ f[k]·g[n-k], where the kernel is flipped before sliding. Deep learning frameworks implement cross-correlation — the kernel is NOT flipped — but the operation is still called convolution because the network learns the kernel anyway. Understanding the mathematics behind output size, receptive field, and computational cost is essential for designing efficient architectures.

## Cross-Correlation vs True Convolution

True convolution flips the kernel: (f★g)[i,j] = ΣₕΣw f[h,w]·g[i-h, j-w]. Cross-correlation does not flip: (f⋆g)[i,j] = ΣₕΣw f[i+h, j+w]·g[h,w]. For a learned kernel the distinction is irrelevant — the network can absorb the flip into the learned weights. PyTorch's nn.Conv2d and F.conv2d implement cross-correlation. The mathematical convolution theorem (convolution in spatial domain = multiplication in frequency domain) applies to true convolution; in practice CNNs are designed around cross-correlation and the term 'convolution' is used loosely throughout the field.

## 2D Convolution from Scratch

For a single-channel input of shape H×W and a kernel of shape k×k, the output at position (i,j) is: output[i,j] = ΣₕΣw input[i·s+h, j·s+w] · kernel[h,w], where s is the stride. With padding p zeros added on each side, the output spatial dimensions are: H_out = (H + 2p - k) // s + 1, W_out = (W + 2p - k) // s + 1. For multi-channel inputs (C_in channels), each output channel has one kernel per input channel and the results are summed: the parameter count per output channel is k×k×C_in, and for C_out output channels the total is k×k×C_in×C_out + C_out (bias).

```python
import numpy as np

def conv2d_scratch(x, kernel, stride=1, padding=0):
    """Cross-correlation (what DL frameworks call 'convolution')."""
    if padding > 0:
        x = np.pad(x, [(0,0),(0,0),(padding,padding),(padding,padding)])
    N, C_in, H, W = x.shape
    C_out, _, k, _ = kernel.shape
    H_out = (H - k) // stride + 1
    W_out = (W - k) // stride + 1
    out = np.zeros((N, C_out, H_out, W_out))
    for n in range(N):
        for co in range(C_out):
            for ci in range(C_in):
                for i in range(H_out):
                    for j in range(W_out):
                        patch = x[n, ci,
                                  i*stride:i*stride+k,
                                  j*stride:j*stride+k]
                        out[n, co, i, j] += (patch * kernel[co, ci]).sum()
    return out

np.random.seed(0)
x = np.random.randn(1, 3, 8, 8)       # (N, C_in, H, W)
k = np.random.randn(16, 3, 3, 3)      # (C_out, C_in, kH, kW)
out = conv2d_scratch(x, k, stride=1, padding=1)
print('Input: ', x.shape)
print('Kernel:', k.shape)
print('Output:', out.shape)  # (1, 16, 8, 8) — same padding
```

## Padding and Stride

Padding controls output size relative to input. Valid padding (p=0): no zeros added, output shrinks by k-1 per side. Same padding (p=(k-1)/2 for odd k): output has the same H×W as input. Stride s controls the step size of the sliding window: stride 2 halves the spatial dimensions (cheaper than pooling, learnable). Combining stride and padding: H_out = ⌊(H+2p-k)/s⌋ + 1. In practice, k=3, p=1, s=1 is the workhorse (preserves size); k=3, p=1, s=2 or k=1, p=0, s=2 is used for downsampling.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

x = torch.randn(1, 3, 32, 32)

configs = [
    dict(kernel_size=3, stride=1, padding=0, dilation=1),   # valid
    dict(kernel_size=3, stride=1, padding=1, dilation=1),   # same
    dict(kernel_size=3, stride=2, padding=1, dilation=1),   # stride-2 down
    dict(kernel_size=3, stride=1, padding=2, dilation=2),   # dilated
    dict(kernel_size=5, stride=1, padding=2, dilation=1),   # 5x5 same
    dict(kernel_size=1, stride=1, padding=0, dilation=1),   # pointwise
]

print(f'{'Config':<40} Output shape')
for cfg in configs:
    conv = nn.Conv2d(3, 16, **cfg)
    out = conv(x)
    k, s, p, d = cfg['kernel_size'], cfg['stride'], cfg['padding'], cfg['dilation']
    label = f'k={k} s={s} p={p} d={d}'
    print(f'{label:<40} {tuple(out.shape)}')
```

## Dilation — Expanding Receptive Field for Free

Dilation (atrous convolution) inserts d-1 zeros between kernel elements. A 3×3 kernel with dilation d=2 samples 5×5 regions; with d=3 it samples 7×7. The effective kernel size is (k-1)·d + 1, but the parameter count remains k×k×C_in×C_out. This is hugely valuable for semantic segmentation (DeepLab) and audio generation (WaveNet) where large context is needed without strided downsampling. Hybrid dilated convolution (HDC) stacks layers with growing dilation rates (1, 2, 5) to avoid the 'gridding artefact' where dilated convolutions miss input pixels.

```python
import torch
import torch.nn as nn

def effective_rf(kernel_size, dilation):
    """Effective receptive field size for a single dilated conv layer."""
    return (kernel_size - 1) * dilation + 1

dilations = [1, 2, 4, 8, 16]
print(f'{'Dilation':<10} {'Eff. kernel':<14} {'RF covered':<12} Params (3x3, 64->64)')
for d in dilations:
    eff = effective_rf(3, d)
    params = 3 * 3 * 64 * 64 + 64  # fixed regardless of dilation
    print(f'{d:<10} {eff}x{eff:<10} {eff*eff:<12} {params:,}')

# Compare output shapes
x = torch.randn(1, 1, 16, 16)
for d in [1, 2, 4]:
    conv = nn.Conv2d(1, 1, kernel_size=3, padding=d, dilation=d)
    print(f'dilation={d}: out {tuple(conv(x).shape)} (same-size with p=d)')
```

## Visualising Learned Kernels

First-layer kernels of a network trained on natural images learn Gabor-like filters — oriented edge detectors, colour blobs, and frequency detectors — because these are the most efficient basis for natural image statistics. Visualising them confirms the network is learning meaningful features rather than noise. For deeper layers, activation maximisation or feature inversion is needed. Weight initialisation matters: He/Kaiming init sets std = sqrt(2/fan_in) for ReLU networks, preventing vanishing/exploding activations.

```python
import torch
import torchvision.models as models
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Load pretrained ResNet-18 and extract first conv layer kernels
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
kernels = model.conv1.weight.data.clone()  # (64, 3, 7, 7)

# Normalize each kernel for visualization
def normalize(t):
    t = t - t.min()
    return t / (t.max() + 1e-8)

fig, axes = plt.subplots(4, 8, figsize=(12, 6))
for idx, ax in enumerate(axes.flat):
    if idx < 32:
        k = normalize(kernels[idx].permute(1, 2, 0).numpy())
        ax.imshow(k)
    ax.axis('off')
plt.suptitle('First 32 of 64 ResNet-18 conv1 kernels (7x7, RGB)')
plt.tight_layout()
plt.savefig('kernels.png', dpi=80)
print(f'conv1 kernel shape: {tuple(kernels.shape)}')
print(f'Params in conv1: {kernels.numel():,} (+ {model.conv1.bias is None and 0} bias)')
```

## Computational Cost Analysis

The floating-point operations (FLOPs) for a convolution layer are: FLOPs ≈ 2 × H_out × W_out × C_in × C_out × k². The factor 2 accounts for multiply-accumulate (MAC = 1 multiply + 1 add). For a typical ResNet-50 layer with H_out=56, W_out=56, C_in=64, C_out=64, k=3: FLOPs ≈ 2×56×56×64×64×9 ≈ 2.3 GFLOPs for that single layer. Memory bandwidth often bottlenecks throughput before compute does, especially for large feature maps. Reducing C_in or C_out by 2× saves 4× FLOPs; reducing k from 3 to 1 saves 9× FLOPs at the cost of no spatial mixing.

```python
import torch
import torch.nn as nn

def conv_flops(H_in, W_in, C_in, C_out, k, s=1, p=0):
    H_out = (H_in + 2*p - k) // s + 1
    W_out = (W_in + 2*p - k) // s + 1
    # 2 ops per MAC (multiply + add), k*k MACs per output element per input channel
    flops = 2 * H_out * W_out * C_in * C_out * k * k
    params = C_out * C_in * k * k + C_out
    return H_out, W_out, flops, params

layers = [
    ('conv1 k=7',  224, 224, 3,   64,  7, 2, 3),
    ('layer1 k=3', 56,  56,  64,  64,  3, 1, 1),
    ('layer1 k=1', 56,  56,  64,  64,  1, 1, 0),
    ('layer4 k=3', 7,   7,   512, 512, 3, 1, 1),
    ('pw  k=1',    14,  14,  256, 1024,1, 1, 0),
]
print(f'{'Layer':<14} {'HxW out':<10} {'GFLOPs':>8} {'Params':>10}')
for name, H, W, Ci, Co, k, s, p in layers:
    Ho, Wo, fl, pa = conv_flops(H, W, Ci, Co, k, s, p)
    print(f'{name:<14} {Ho}x{Wo:<6} {fl/1e9:>8.3f} {pa:>10,}')
```

> **Weight Sharing = Translation Equivariance**: The same kernel is applied at every spatial location — this is weight sharing. It means a feature detector trained on a cat in the upper-left works equally well in the lower-right. Formally, if T_d denotes a shift-by-d operator, convolution satisfies f(T_d x) = T_d(f(x)): shifting the input shifts the output by the same amount. This inductive bias dramatically reduces the parameters needed and is why CNNs generalise so well on images.

## Multi-Channel Extension and Parameter Count

For an input with C_in channels and C_out output channels, the kernel tensor has shape (C_out, C_in, k, k). Each output channel is produced by convolving the full C_in-channel input with one (C_in, k, k) kernel and summing across channels. The parameter count is C_out × C_in × k × k + C_out (bias). For k=3, C_in=256, C_out=256: 256×256×9 + 256 = 590,080 parameters. Compare: a fully-connected layer mapping the same 256×7×7 = 12,544 features to 12,544 outputs would need 12,544² ≈ 157M parameters — 266× more.

| Parameter | Effect on Output Size | Effect on Receptive Field | Effect on Params | Effect on FLOPs |
| --- | --- | --- | --- | --- |
| Kernel size k↑ | (H+2p-k)//s+1 shrinks | Grows linearly with k | ×k² per layer | ×k² |
| Stride s↑ | Divides by s (downsamples) | Multiplies all downstream RF | Unchanged | ÷s² |
| Padding p↑ | +(2p) before division | No effect | Unchanged | Slightly ↑ |
| Dilation d↑ | Unchanged (with p=d) | ×d per layer | Unchanged | Unchanged |
| C_in↑ | Unchanged | Unchanged | ×C_in | ×C_in |
| C_out↑ | More output channels | Unchanged | ×C_out | ×C_out |

- Valid padding (p=0): output shrinks by k-1 each side — use when reducing spatial size intentionally.
- Same padding (p=(k-1)//2): output matches input size — standard in residual blocks.
- SAME vs VALID in TensorFlow: SAME adds asymmetric padding; PyTorch requires manual specification.
- Grouped convolution (groups=g): reduces params and FLOPs by factor g — covered in the next note.
- Bias can be omitted (bias=False) when BatchNorm follows — BN has its own learnable shift parameter.
- Output channel ordering: PyTorch uses (N, C, H, W); TensorFlow defaults to (N, H, W, C).

---

