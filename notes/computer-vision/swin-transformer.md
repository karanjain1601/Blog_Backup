---
title: "Swin Transformer: Hierarchical Vision Transformer with Shifted Windows"
slug: "swin-transformer"
description: "Swin Transformer applies self-attention within local windows and shifts them between layers to enable cross-window connections — achieving CNN-like hierarchy with transformer expressiveness."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgU3dpbiBUcmFuc2Zvcm1lciAoU2hpZnRlZCBXaW5kb3cgVHJhbnNmb3JtZXIpLCBpbnRyb2R1Y2VkIGJ5IExpdSBldCBhbC4gYXQgTWljcm9zb2Z0IFJlc2VhcmNoIGluIDIwMjEsIGlzIGEgaGllcmFyY2hpY2FsIHZpc2lvbiB0cmFuc2Zvcm1lciB1c2luZyBsb2NhbCBzZWxmLWF0dGVudGlvbiB3aXRoaW4gbm9uLW92ZXJsYXBwaW5nIHdpbmRvd3MuIFVubGlrZSBWaVQsIHdoaWNoIGFwcGxpZXMgZ2xvYmFsIGF0dGVudGlvbiBhY3Jvc3MgYWxsIHBhdGNoZXMsIFN3aW4gcmVzdHJpY3RzIGF0dGVudGlvbiB0byBmaXhlZC1zaXplIHdpbmRvd3MsIHJlZHVjaW5nIGNvbXBsZXhpdHkgZnJvbSBPKE7CsikgdG8gTyhOKS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN3aW4gYWNoaWV2ZXMgbXVsdGktc2NhbGUgZmVhdHVyZSByZXByZXNlbnRhdGlvbnMgYnkgcHJvZ3Jlc3NpdmVseSBtZXJnaW5nIHBhdGNoIHRva2VucyBhY3Jvc3MgZm91ciBzdGFnZXMsIHNpbWlsYXIgdG8gQ05OIGZlYXR1cmUgcHlyYW1pZHMuIFRoaXMgaGllcmFyY2hpY2FsIGRlc2lnbiBtYWtlcyBpdCBzdWl0YWJsZSBub3Qgb25seSBmb3IgaW1hZ2UgY2xhc3NpZmljYXRpb24gYnV0IGFsc28gZm9yIGRlbnNlIHByZWRpY3Rpb24gdGFza3Mgc3VjaCBhcyBvYmplY3QgZGV0ZWN0aW9uIGFuZCBzZW1hbnRpYyBzZWdtZW50YXRpb24sIGVuYWJsaW5nIGl0IHRvIHNlcnZlIGFzIGEgdW5pdmVyc2FsIGJhY2tib25lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldpbmRvdy1CYXNlZCBTZWxmLUF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gc3RhbmRhcmQgVmlULCBzZWxmLWF0dGVudGlvbiBpcyBjb21wdXRlZCBnbG9iYWxseSBhY3Jvc3MgYWxsIE4gcGF0Y2hlcywgcmVzdWx0aW5nIGluIE8oTsKyKSBjb21wdXRhdGlvbmFsIGFuZCBtZW1vcnkgY29zdC4gU3dpbiBwYXJ0aXRpb25zIHRoZSBmZWF0dXJlIG1hcCBpbnRvIG5vbi1vdmVybGFwcGluZyBNw5dNIHdpbmRvd3MgKHR5cGljYWxseSA3w5c3KSBhbmQgYXBwbGllcyBzZWxmLWF0dGVudGlvbiBvbmx5IHdpdGhpbiBlYWNoIHdpbmRvdy4gRm9yIGFuIEjDl1cgZmVhdHVyZSBtYXAsIHRoaXMgeWllbGRzIGxpbmVhciBPKEhXKSBjb21wbGV4aXR5IGluIHRoZSBudW1iZXIgb2YgcGF0Y2hlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSBlaW5vcHMgaW1wb3J0IHJlYXJyYW5nZVxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiB3aW5kb3dfcGFydGl0aW9uKHgsIHdpbj03KTpcbiAgICAjIHg6IChCLCBILCBXLCBDKVxuICAgIEIsIEgsIFcsIEMgPSB4LnNoYXBlXG4gICAgeCA9IHgudmlldyhCLCBILy93aW4sIHdpbiwgVy8vd2luLCB3aW4sIEMpXG4gICAgeCA9IHgucGVybXV0ZSgwLDEsMywyLDQsNSkuY29udGlndW91cygpXG4gICAgd2luZG93cyA9IHgudmlldygtMSwgd2luLCB3aW4sIEMpXG4gICAgcmV0dXJuIHdpbmRvd3MgICMgKG51bV93aW5kb3dzKkIsIHdpbiwgd2luLCBDKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWFjaCB3aW5kb3dcdTAwMjdzIHRva2VucyB1bmRlcmdvIHN0YW5kYXJkIG11bHRpLWhlYWQgc2VsZi1hdHRlbnRpb24gd2l0aCBhIGxlYXJuYWJsZSByZWxhdGl2ZSBwb3NpdGlvbiBiaWFzIGFkZGVkIHRvIGF0dGVudGlvbiBsb2dpdHMgYmVmb3JlIHNvZnRtYXguIEJlY2F1c2Ugd2luZG93IHNpemUgTSBpcyBmaXhlZCByZWdhcmRsZXNzIG9mIGltYWdlIHJlc29sdXRpb24sIHRvdGFsIGNvbXB1dGUgc2NhbGVzIGxpbmVhcmx5IHdpdGggaW1hZ2Ugc2l6ZS4gT3V0cHV0IHdpbmRvd3MgYXJlIHJlYXNzZW1ibGVkIGludG8gdGhlIG9yaWdpbmFsIHNwYXRpYWwgbGF5b3V0IGJlZm9yZSB0aGUgbmV4dCBUcmFuc2Zvcm1lciBibG9jay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaGlmdGVkIFdpbmRvdyBQYXJ0aXRpb25pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrZXkgbGltaXRhdGlvbiBvZiBpbmRlcGVuZGVudCB3aW5kb3cgYXR0ZW50aW9uIGlzIHRoYXQgd2luZG93cyBjYW5ub3QgY29tbXVuaWNhdGUsIGJyZWFraW5nIHNwYXRpYWwgY29udGV4dCBhY3Jvc3MgYm91bmRhcmllcy4gU3dpbiBhbHRlcm5hdGVzIGJldHdlZW4gdHdvIHBhcnRpdGlvbmluZyBzY2hlbWVzIGVhY2ggbGF5ZXI6IGEgcmVndWxhciBncmlkIGFuZCBhIGdyaWQgc2hpZnRlZCBieSAoTS8yLCBNLzIpIHBpeGVscywgc28gd2luZG93IGJvdW5kYXJpZXMgc2hpZnQgYWNyb3NzIGxheWVycyBhbmQgZW5hYmxlIGNyb3NzLXdpbmRvdyBpbmZvcm1hdGlvbiBmbG93IGVmZmljaWVudGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIHNoaWZ0ZWRfd2luZG93X2F0dGVudGlvbih4LCBzaGlmdD0oMywzKSwgd2luPTcpOlxuICAgICMgQ3ljbGljIHNoaWZ0XG4gICAgeF9zaGlmdGVkID0gdG9yY2gucm9sbCh4LCBzaGlmdHM9KC1zaGlmdFswXSwgLXNoaWZ0WzFdKSwgZGltcz0oMSwyKSlcbiAgICAjIFBhcnRpdGlvbiBpbnRvIHdpbmRvd3NcbiAgICB3aW5kb3dzID0gd2luZG93X3BhcnRpdGlvbih4X3NoaWZ0ZWQsIHdpbilcbiAgICAjIEFwcGx5IG1hc2tlZCBzZWxmLWF0dGVudGlvbiAobWFzayBhcHBsaWVkIGluc2lkZSBhdHRuKVxuICAgIGF0dG5fb3V0ID0gd2luZG93X2F0dGVudGlvbih3aW5kb3dzKVxuICAgICMgUmV2ZXJzZSBjeWNsaWMgc2hpZnRcbiAgICB4X291dCA9IHdpbmRvd19yZXZlcnNlKGF0dG5fb3V0LCB3aW4sIHguc2hhcGUpXG4gICAgeF9vdXQgPSB0b3JjaC5yb2xsKHhfb3V0LCBzaGlmdHM9KHNoaWZ0WzBdLCBzaGlmdFsxXSksIGRpbXM9KDEsMikpXG4gICAgcmV0dXJuIHhfb3V0In0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiBjcmVhdGVfc2hpZnRfbWFzayhILCBXLCB3aW49Nywgc2hpZnQ9MywgZGV2aWNlPVx1MDAyN2NwdVx1MDAyNyk6XG4gICAgbWFzayA9IHRvcmNoLnplcm9zKDEsIEgsIFcsIDEsIGRldmljZT1kZXZpY2UpXG4gICAgc2xpY2VzID0gKHNsaWNlKDAsLXdpbiksIHNsaWNlKC13aW4sLXNoaWZ0KSwgc2xpY2UoLXNoaWZ0LE5vbmUpKVxuICAgIGlkeCA9IDBcbiAgICBmb3IgaCBpbiBzbGljZXM6XG4gICAgICAgIGZvciB3IGluIHNsaWNlczpcbiAgICAgICAgICAgIG1hc2tbOiwgaCwgdywgOl0gPSBpZHhcbiAgICAgICAgICAgIGlkeCArPSAxXG4gICAgbWFza193aW5kb3dzID0gd2luZG93X3BhcnRpdGlvbihtYXNrLCB3aW4pLnZpZXcoLTEsIHdpbip3aW4pXG4gICAgYXR0bl9tYXNrID0gbWFza193aW5kb3dzLnVuc3F1ZWV6ZSgxKSAtIG1hc2tfd2luZG93cy51bnNxdWVlemUoMilcbiAgICAjIEZpbGwgY3Jvc3MtYm91bmRhcnkgcG9zaXRpb25zIHdpdGggbGFyZ2UgbmVnYXRpdmUgdmFsdWVcbiAgICBhdHRuX21hc2sgPSBhdHRuX21hc2subWFza2VkX2ZpbGwoYXR0bl9tYXNrICE9IDAsIC0xMDAuMClcbiAgICByZXR1cm4gYXR0bl9tYXNrIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRUeXBlIjoiaW5mbyIsImNvbnRlbnQiOiJTd2luXHUwMDI3cyBzaGlmdGVkIHdpbmRvdyBzY2hlbWUgaXMgYSBwcmFnbWF0aWMgZml4IGZvciBWaVRcdTAwMjdzIHF1YWRyYXRpYyBhdHRlbnRpb24gY29zdC4gQnkgY29uZmluaW5nIGF0dGVudGlvbiB0byA3w5c3IHdpbmRvd3MgYW5kIHNoaWZ0aW5nIGJ5ICgzLDMpIGV2ZXJ5IG90aGVyIGxheWVyLCBpdCBhY2hpZXZlcyBPKE4pIGNvbXBsZXhpdHkgd2hpbGUgc3RpbGwgYWxsb3dpbmcgYWxsIHBhdGNoZXMgdG8gZXZlbnR1YWxseSBjb21tdW5pY2F0ZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIaWVyYXJjaGljYWwgRmVhdHVyZSBNYXBzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTd2luIGJ1aWxkcyBhIGZvdXItc3RhZ2UgaGllcmFyY2h5IGJ5IHByb2dyZXNzaXZlbHkgbWVyZ2luZyBwYXRjaGVzLiBTdGFnZSAxIHVzZXMgNMOXNCBwYXRjaGVzIGF0IEMgY2hhbm5lbHMuIEVhY2ggc3RhZ2UgdHJhbnNpdGlvbiBhcHBsaWVzIHBhdGNoIG1lcmdpbmc6IGFkamFjZW50IDLDlzIgcGF0Y2hlcyBhcmUgY29uY2F0ZW5hdGVkIGFuZCBsaW5lYXJseSBwcm9qZWN0ZWQsIGhhbHZpbmcgc3BhdGlhbCByZXNvbHV0aW9uIGFuZCBkb3VibGluZyBjaGFubmVscyDigJQgYW5hbG9nb3VzIHRvIHN0cmlkZWQgY29udm9sdXRpb25zIGluIFJlc05ldFx1MDAyN3Mgc3RhZ2UgdHJhbnNpdGlvbnMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlZhcmlhbnQiLCJXaW5kb3cgU2l6ZSIsIlN0YWdlcyIsIkNoYW5uZWxzIiwiUGFyYW1zIChNKSIsIklOLTFLIFRvcC0xICUiLCJGTE9QcyAoRykiXSwicm93cyI6W1siU3dpbi1UIiwiN3g3IiwiNCIsIjk2IiwiMjgiLCI4MS4zIiwiNC41Il0sWyJTd2luLVMiLCI3eDciLCI0IiwiOTYiLCI1MCIsIjgzLjAiLCI4LjciXSxbIlN3aW4tQiIsIjd4NyIsIjQiLCIxMjgiLCI4OCIsIjgzLjUiLCIxNS40Il0sWyJTd2luLUwiLCI3eDciLCI0IiwiMTkyIiwiMTk3IiwiODYuMyIsIjEwMy45Il0sWyJTd2luLVYyLUciLCIxNngxNiIsIjQiLCIxOTIiLCIzMDAwIiwiOTAuMiIsIjI2MDAiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHN0YWdlZCBkZXNpZ24gcHJvZHVjZXMgZmVhdHVyZSBtYXBzIGF0IDEvNCwgMS84LCAxLzE2LCBhbmQgMS8zMiBvZiBpbnB1dCByZXNvbHV0aW9uLCBtaXJyb3JpbmcgUmVzTmV0XHUwMDI3cyBDMi1DNSBvdXRwdXRzLiBUaGVzZSBtdWx0aS1zY2FsZSBmZWF0dXJlcyBwbHVnIGRpcmVjdGx5IGludG8gZGV0ZWN0aW9uIGhlYWRzIGxpa2UgRlBOIG9yIENhc2NhZGUgUi1DTk4sIGVuYWJsaW5nIFN3aW4gdG8gcmVwbGFjZSBDTk4gYmFja2JvbmVzIGluIGV4aXN0aW5nIHBpcGVsaW5lcyB3aXRoIG1pbmltYWwgYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzIGFuZCBjb25zaXN0ZW50IGFjY3VyYWN5IGdhaW5zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN3aW4gYXMgVW5pdmVyc2FsIEJhY2tib25lIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZXlvbmQgY2xhc3NpZmljYXRpb24sIFN3aW4gc2VydmVzIGFzIGEgZHJvcC1pbiBiYWNrYm9uZSBmb3Igb2JqZWN0IGRldGVjdGlvbiB3aXRoIENhc2NhZGUgTWFzayBSLUNOTiwgc2VtYW50aWMgc2VnbWVudGF0aW9uIHdpdGggVXBlck5ldCwgYW5kIGluc3RhbmNlIHNlZ21lbnRhdGlvbiB0YXNrcy4gSXQgYWNoaWV2ZWQgc3RhdGUtb2YtdGhlLWFydCByZXN1bHRzIG9uIENPQ08gYW5kIEFERTIwSyBpbiAyMDIxLiBJdHMgQVBJIG1pcnJvcnMgUmVzTmV0OiBhIGZlYXR1cmUgZXh0cmFjdG9yIHJldHVybmluZyBtdWx0aS1zY2FsZSBtYXBzIGF0IGZvdXIgcmVzb2x1dGlvbiBsZXZlbHMgZm9yIGRvd25zdHJlYW0gaGVhZHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaHZpc2lvbi5tb2RlbHMgaW1wb3J0IHN3aW5fdCwgU3dpbl9UX1dlaWdodHNcblxuIyBMb2FkIHByZXRyYWluZWQgU3dpbi1UXG5tb2RlbCA9IHN3aW5fdCh3ZWlnaHRzPVN3aW5fVF9XZWlnaHRzLklNQUdFTkVUMUtfVjEpXG5tb2RlbC5ldmFsKClcblxuaW1nID0gdG9yY2gucmFuZG4oMSwgMywgMjI0LCAyMjQpXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBmZWF0dXJlcyA9IG1vZGVsLmZvcndhcmRfZmVhdHVyZXMoaW1nKVxuXG4jIGZlYXR1cmVzIHNoYXBlOiAoMSwgNywgNywgNzY4KSBhZnRlciBmaW5hbCBzdGFnZVxuZGVuc2VfZmVhdCA9IGZlYXR1cmVzICAjIGZlZWQgdG8gZGV0ZWN0aW9uIGhlYWRcbnByaW50KGZcdTAwMjdGZWF0dXJlIHNoYXBlOiB7ZGVuc2VfZmVhdC5zaGFwZX1cdTAwMjcpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTd2luLVYyIGV4dGVuZHMgdGhlIG9yaWdpbmFsIHdpdGggbG9nLXNwYWNlZCBjb250aW51b3VzIHJlbGF0aXZlIHBvc2l0aW9uIGJpYXMsIHJlc2lkdWFsIHBvc3Qtbm9ybSBsYXllcnMsIGFuZCBzY2FsZWQgY29zaW5lIGF0dGVudGlvbiwgZW5hYmxpbmcgc3RhYmxlIHRyYWluaW5nIGF0IDNCIHBhcmFtZXRlcnMgYW5kIHJlc29sdXRpb25zIHVwIHRvIDE1MzZ4MTUzNi4gVGhlc2UgY2hhbmdlcyBkZW1vbnN0cmF0ZSB0aGF0IHRoZSBTd2luIGFyY2hpdGVjdHVyZSBzY2FsZXMgcHJlZGljdGFibHkgd2l0aCBtb2RlbCBzaXplLCBkYXRhIHZvbHVtZSwgYW5kIGNvbXB1dGUgYnVkZ2V0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN3aW4gVHJhbnNmb3JtZXIgYnJpZGdlcyBDTk5zIGFuZCB2aXNpb24gdHJhbnNmb3JtZXJzIGJ5IHJlaW50cm9kdWNpbmcgbG9jYWxpdHkgYW5kIGhpZXJhcmNoeSDigJQgdHdvIGluZHVjdGl2ZSBiaWFzZXMgdGhhdCBDTk5zIHBvc3Nlc3MgbmF0dXJhbGx5LiBUaGUgc2hpZnRlZCB3aW5kb3cgbWVjaGFuaXNtIGRlbGl2ZXJzIGVmZmljaWVudCBnbG9iYWwgY29udGV4dCBhY2N1bXVsYXRpb24gd2l0aG91dCBxdWFkcmF0aWMgYXR0ZW50aW9uIGNvc3QsIG1ha2luZyBpdCBwcmFjdGljYWwgZm9yIGhpZ2gtcmVzb2x1dGlvbiBpbnB1dHMgaW4gcmVhbCBwcm9kdWN0aW9uIHZpc2lvbiBkZXBsb3ltZW50cy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldpbmRvdyBzaXplIGlzIGEgY3JpdGljYWwgaHlwZXJwYXJhbWV0ZXI6IHNtYWxsZXIgd2luZG93cyBjdXQgRkxPUHMgYnV0IHNsb3cgcmVjZXB0aXZlIGZpZWxkIGdyb3d0aCBwZXIgbGF5ZXIuIFN3aW4tVjIgdXNlcyBsYXJnZXIgMTZ4MTYgd2luZG93cyBmb3IgaXRzIGJpZ2dlc3QgbW9kZWxzIHRvIGJhbGFuY2UgZXhwcmVzc2l2ZW5lc3MgYW5kIGVmZmljaWVuY3kuIFByZS10cmFpbmVkIFN3aW4gY2hlY2twb2ludHMgdHJhbnNmZXIgd2VsbCBhY3Jvc3MgZG9tYWlucyBpbmNsdWRpbmcgbWVkaWNhbCBpbWFnaW5nLCBzYXRlbGxpdGUgaW1hZ2VyeSwgYW5kIHZpZGVvIHVuZGVyc3RhbmRpbmcgdGFza3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTd2luXHUwMDI3cyBpbmZsdWVuY2UgZXh0ZW5kcyB3ZWxsIGJleW9uZCB0aGUgb3JpZ2luYWwgcGFwZXIuIEl0IGluc3BpcmVkIGhpZXJhcmNoaWNhbCB0cmFuc2Zvcm1lcnMgaW5jbHVkaW5nIENTV2luLCBUd2lucywgYW5kIFBvb2xGb3JtZXIsIGVhY2ggZXhwbG9yaW5nIGFsdGVybmF0aXZlIHRva2VuLW1peGluZyBzdHJhdGVnaWVzIHdpdGhpbiBhIHN0YWdlZCBhcmNoaXRlY3R1cmUuIFVuZGVyc3RhbmRpbmcgU3dpbiBpcyBlc3NlbnRpYWwgZm9yIGFueW9uZSBidWlsZGluZyBtb2Rlcm4gbXVsdGktc2NhbGUgdmlzaW9uIHN5c3RlbXMgb3IgYWRhcHRpbmcgdHJhbnNmb3JtZXIgYmFja2JvbmVzIHRvIGRlbnNlIHByZWRpY3Rpb24uIn1d"
---
# Swin Transformer: Hierarchical Vision Transformer with Shifted Windows

## Overview

The Swin Transformer (Shifted Window Transformer), introduced by Liu et al. at Microsoft Research in 2021, is a hierarchical vision transformer using local self-attention within non-overlapping windows. Unlike ViT, which applies global attention across all patches, Swin restricts attention to fixed-size windows, reducing complexity from O(N²) to O(N).

Swin achieves multi-scale feature representations by progressively merging patch tokens across four stages, similar to CNN feature pyramids. This hierarchical design makes it suitable not only for image classification but also for dense prediction tasks such as object detection and semantic segmentation, enabling it to serve as a universal backbone.

## Window-Based Self-Attention

In standard ViT, self-attention is computed globally across all N patches, resulting in O(N²) computational and memory cost. Swin partitions the feature map into non-overlapping M×M windows (typically 7×7) and applies self-attention only within each window. For an H×W feature map, this yields linear O(HW) complexity in the number of patches.

```python
from einops import rearrange
import torch.nn as nn

def window_partition(x, win=7):
    # x: (B, H, W, C)
    B, H, W, C = x.shape
    x = x.view(B, H//win, win, W//win, win, C)
    x = x.permute(0,1,3,2,4,5).contiguous()
    windows = x.view(-1, win, win, C)
    return windows  # (num_windows*B, win, win, C)
```

Each window's tokens undergo standard multi-head self-attention with a learnable relative position bias added to attention logits before softmax. Because window size M is fixed regardless of image resolution, total compute scales linearly with image size. Output windows are reassembled into the original spatial layout before the next Transformer block.

## Shifted Window Partitioning

The key limitation of independent window attention is that windows cannot communicate, breaking spatial context across boundaries. Swin alternates between two partitioning schemes each layer: a regular grid and a grid shifted by (M/2, M/2) pixels, so window boundaries shift across layers and enable cross-window information flow efficiently.

```python
import torch

def shifted_window_attention(x, shift=(3,3), win=7):
    # Cyclic shift
    x_shifted = torch.roll(x, shifts=(-shift[0], -shift[1]), dims=(1,2))
    # Partition into windows
    windows = window_partition(x_shifted, win)
    # Apply masked self-attention (mask applied inside attn)
    attn_out = window_attention(windows)
    # Reverse cyclic shift
    x_out = window_reverse(attn_out, win, x.shape)
    x_out = torch.roll(x_out, shifts=(shift[0], shift[1]), dims=(1,2))
    return x_out
```

```python
def create_shift_mask(H, W, win=7, shift=3, device='cpu'):
    mask = torch.zeros(1, H, W, 1, device=device)
    slices = (slice(0,-win), slice(-win,-shift), slice(-shift,None))
    idx = 0
    for h in slices:
        for w in slices:
            mask[:, h, w, :] = idx
            idx += 1
    mask_windows = window_partition(mask, win).view(-1, win*win)
    attn_mask = mask_windows.unsqueeze(1) - mask_windows.unsqueeze(2)
    # Fill cross-boundary positions with large negative value
    attn_mask = attn_mask.masked_fill(attn_mask != 0, -100.0)
    return attn_mask
```

> ****: Swin's shifted window scheme is a pragmatic fix for ViT's quadratic attention cost. By confining attention to 7×7 windows and shifting by (3,3) every other layer, it achieves O(N) complexity while still allowing all patches to eventually communicate.

## Hierarchical Feature Maps

Swin builds a four-stage hierarchy by progressively merging patches. Stage 1 uses 4×4 patches at C channels. Each stage transition applies patch merging: adjacent 2×2 patches are concatenated and linearly projected, halving spatial resolution and doubling channels — analogous to strided convolutions in ResNet's stage transitions.

| Variant | Window Size | Stages | Channels | Params (M) | IN-1K Top-1 % | FLOPs (G) |
| --- | --- | --- | --- | --- | --- | --- |
| Swin-T | 7x7 | 4 | 96 | 28 | 81.3 | 4.5 |
| Swin-S | 7x7 | 4 | 96 | 50 | 83.0 | 8.7 |
| Swin-B | 7x7 | 4 | 128 | 88 | 83.5 | 15.4 |
| Swin-L | 7x7 | 4 | 192 | 197 | 86.3 | 103.9 |
| Swin-V2-G | 16x16 | 4 | 192 | 3000 | 90.2 | 2600 |

The staged design produces feature maps at 1/4, 1/8, 1/16, and 1/32 of input resolution, mirroring ResNet's C2-C5 outputs. These multi-scale features plug directly into detection heads like FPN or Cascade R-CNN, enabling Swin to replace CNN backbones in existing pipelines with minimal architectural changes and consistent accuracy gains.

## Swin as Universal Backbone

Beyond classification, Swin serves as a drop-in backbone for object detection with Cascade Mask R-CNN, semantic segmentation with UperNet, and instance segmentation tasks. It achieved state-of-the-art results on COCO and ADE20K in 2021. Its API mirrors ResNet: a feature extractor returning multi-scale maps at four resolution levels for downstream heads.

```python
import torch
from torchvision.models import swin_t, Swin_T_Weights

# Load pretrained Swin-T
model = swin_t(weights=Swin_T_Weights.IMAGENET1K_V1)
model.eval()

img = torch.randn(1, 3, 224, 224)
with torch.no_grad():
    features = model.forward_features(img)

# features shape: (1, 7, 7, 768) after final stage
dense_feat = features  # feed to detection head
print(f'Feature shape: {dense_feat.shape}')
```

Swin-V2 extends the original with log-spaced continuous relative position bias, residual post-norm layers, and scaled cosine attention, enabling stable training at 3B parameters and resolutions up to 1536x1536. These changes demonstrate that the Swin architecture scales predictably with model size, data volume, and compute budget.

## Key Takeaways

Swin Transformer bridges CNNs and vision transformers by reintroducing locality and hierarchy — two inductive biases that CNNs possess naturally. The shifted window mechanism delivers efficient global context accumulation without quadratic attention cost, making it practical for high-resolution inputs in real production vision deployments.

Window size is a critical hyperparameter: smaller windows cut FLOPs but slow receptive field growth per layer. Swin-V2 uses larger 16x16 windows for its biggest models to balance expressiveness and efficiency. Pre-trained Swin checkpoints transfer well across domains including medical imaging, satellite imagery, and video understanding tasks.

Swin's influence extends well beyond the original paper. It inspired hierarchical transformers including CSWin, Twins, and PoolFormer, each exploring alternative token-mixing strategies within a staged architecture. Understanding Swin is essential for anyone building modern multi-scale vision systems or adapting transformer backbones to dense prediction.

