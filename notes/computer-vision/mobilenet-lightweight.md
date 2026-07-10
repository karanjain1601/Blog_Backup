---
title: "MobileNet: Lightweight CNNs for Edge Deployment"
slug: "mobilenet-lightweight"
description: "Depthwise separable convolutions in MobileNetV1, the inverted residual block in MobileNetV2, and hard-swish + SE modules in MobileNetV3 — optimized for mobile and edge inference."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb2JpbGVOZXQgaXMgYSBmYW1pbHkgb2YgZWZmaWNpZW50IENOTnMgZGVzaWduZWQgZm9yIG1vYmlsZSBhbmQgZW1iZWRkZWQgYXBwbGljYXRpb25zLiBWMSAoMjAxNykgaW50cm9kdWNlZCBkZXB0aHdpc2Ugc2VwYXJhYmxlIGNvbnZvbHV0aW9ucyB0byBjdXQgY29tcHV0ZSBkcmFtYXRpY2FsbHkuIFYyICgyMDE4KSBhZGRlZCBpbnZlcnRlZCByZXNpZHVhbHMgd2l0aCBsaW5lYXIgYm90dGxlbmVja3MuIFYzICgyMDE5KSBpbmNvcnBvcmF0ZWQgbmV1cmFsIGFyY2hpdGVjdHVyZSBzZWFyY2gsIGhhcmQtc3dpc2ggYWN0aXZhdGlvbiwgYW5kIHNxdWVlemUtYW5kLWV4Y2l0YXRpb24gbW9kdWxlcyB0byBmdXJ0aGVyIGJvb3N0IGFjY3VyYWN5LXBlci1GTE9QLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIE1vYmlsZU5ldCBzZXJpZXMgcHJpb3JpdGl6ZXMgcmVhbC13b3JsZCBkZXBsb3lhYmlsaXR5IG92ZXIgcmF3IGJlbmNobWFyayBhY2N1cmFjeS4gQWxsIHRocmVlIHZlcnNpb25zIGFyZSBxdWFudGl6YXRpb24tZnJpZW5kbHksIHdpZGVseSBzdXBwb3J0ZWQgaW4gVEZMaXRlLCBDb3JlTUwsIGFuZCBPTk5YIFJ1bnRpbWUsIGFuZCBzZXJ2ZSBhcyBiYWNrYm9uZXMgZm9yIGRldGVjdGlvbiAoU1NELCBZT0xPKSwgc2VnbWVudGF0aW9uIChEZWVwTGFiKSwgYW5kIGNsYXNzaWZpY2F0aW9uIG9uIGRldmljZXMgcmFuZ2luZyBmcm9tIFJhc3BiZXJyeSBQaSB0byBBcHBsZSBOZXVyYWwgRW5naW5lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlcHRod2lzZSBTZXBhcmFibGUgQ29udm9sdXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc3RhbmRhcmQgY29udiB3aXRoIGtlcm5lbCBLw5dLIG9uIENfaW4gY2hhbm5lbHMgdG8gQ19vdXQgY2hhbm5lbHMgY29zdHMgS8KywrdDX2luwrdDX291dCBGTE9QcyBwZXIgc3BhdGlhbCBwb3NpdGlvbi4gRGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbiBzcGxpdHMgdGhpcyBpbnRvIGEgZGVwdGh3aXNlIHN0ZXAgKG9uZSBmaWx0ZXIgcGVyIGlucHV0IGNoYW5uZWwsIEvCssK3Q19pbikgYW5kIGEgcG9pbnR3aXNlIHN0ZXAgKDHDlzEgY29udiwgQ19pbsK3Q19vdXQpLiBUaGUgRkxPUHMgcmF0aW8gdnMgc3RhbmRhcmQgY29udiBpcyAxL0Nfb3V0ICsgMS9LwrIsIHJvdWdobHkgOOKAkznDlyBjaGVhcGVyIGZvciBLPTMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgZHdfc2VwX2Jsb2NrKENfaW4sIENfb3V0LCBzdHJpZGU9MSk6XG4gICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICMgRGVwdGh3aXNlOiBncm91cHM9Q19pbiBhcHBsaWVzIG9uZSBmaWx0ZXIgcGVyIGNoYW5uZWxcbiAgICAgICAgbm4uQ29udjJkKENfaW4sIENfaW4sIDMsIHN0cmlkZT1zdHJpZGUsIHBhZGRpbmc9MSwgZ3JvdXBzPUNfaW4sIGJpYXM9RmFsc2UpLFxuICAgICAgICBubi5CYXRjaE5vcm0yZChDX2luKSxcbiAgICAgICAgbm4uUmVMVTYoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgIyBQb2ludHdpc2U6IDHDlzEgY29udiBtaXhlcyBjaGFubmVsc1xuICAgICAgICBubi5Db252MmQoQ19pbiwgQ19vdXQsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICBubi5CYXRjaE5vcm0yZChDX291dCksXG4gICAgICAgIG5uLlJlTFU2KGlucGxhY2U9VHJ1ZSksXG4gICAgKVxuIyBGTE9QcyByYXRpbyB2cyBzdGFuZGFyZCBjb252OiAxL0Nfb3V0ICsgMS9LwrJcbiMgRm9yIEs9MywgQ19vdXQ9MzI6IHJhdGlvIOKJiCAxLzMyICsgMS85IOKJiCAwLjE0ICAo4omIN8OXIGNoZWFwZXIpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb2JpbGVOZXRWMSBzdGFja3MgMTMgc3VjaCBkZXB0aHdpc2Ugc2VwYXJhYmxlIGJsb2NrcyB3aXRoIGEgd2lkdGggbXVsdGlwbGllciDOsSDiiIggezAuMjUsIDAuNSwgMC43NSwgMS4wfSB0aGF0IHVuaWZvcm1seSBzY2FsZXMgY2hhbm5lbHMsIGFuZCBhIHJlc29sdXRpb24gbXVsdGlwbGllciDPgSB0aGF0IHNjYWxlcyBpbnB1dCBzaXplLiBUb2dldGhlciB0aGV5IGFsbG93IGFuIGFjY3VyYWN5LWxhdGVuY3kgdHJhZGUtb2ZmIHR1bmFibGUgdG8gdGhlIHRhcmdldCBoYXJkd2FyZSB3aXRob3V0IHJldHJhaW5pbmcgdGhlIGVudGlyZSBhcmNoaXRlY3R1cmUgZnJvbSBzY3JhdGNoLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vYmlsZU5ldFYyIEludmVydGVkIFJlc2lkdWFsIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWMiBmbGlwcyB0aGUgdHJhZGl0aW9uYWwgcmVzaWR1YWwgZGVzaWduLiBXaGVyZSBSZXNOZXQgYm90dGxlbmVja3MgY29tcHJlc3MgdG8gYSBuYXJyb3cgbWlkZGxlIGxheWVyLCBNb2JpbGVOZXRWMiBleHBhbmRzIGNoYW5uZWwgY291bnQgYnkgZmFjdG9yIHQgKHR5cGljYWxseSA2KSBiZWZvcmUgdGhlIGRlcHRod2lzZSBjb252b2x1dGlvbiwgdGhlbiBwcm9qZWN0cyBiYWNrIGRvd24uIFRoaXMga2VlcHMgdGhlIGRlcHRod2lzZSBjb252IG9wZXJhdGluZyBpbiBhIHJpY2ggaGlnaC1kaW1lbnNpb25hbCBzcGFjZSB3aGlsZSB0aGUgc2tpcCBjb25uZWN0aW9uIHJ1bnMgaW4gdGhlIGNvbXBhY3QgbG93LWRpbWVuc2lvbmFsIGJvdHRsZW5lY2sgc3BhY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImNsYXNzIEludmVydGVkUmVzaWR1YWwobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgQ19pbiwgQ19vdXQsIHN0cmlkZSwgZXhwYW5kX3JhdGlvPTYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgQ19taWQgPSBDX2luICogZXhwYW5kX3JhdGlvXG4gICAgICAgIHNlbGYudXNlX3NraXAgPSAoc3RyaWRlID09IDEgYW5kIENfaW4gPT0gQ19vdXQpXG4gICAgICAgIHNlbGYuY29udiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoQ19pbiwgQ19taWQsIDEsIGJpYXM9RmFsc2UpLCBubi5CYXRjaE5vcm0yZChDX21pZCksIG5uLlJlTFU2KGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQoQ19taWQsIENfbWlkLCAzLCBzdHJpZGU9c3RyaWRlLCBwYWRkaW5nPTEsIGdyb3Vwcz1DX21pZCwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTJkKENfbWlkKSwgbm4uUmVMVTYoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgICMgTGluZWFyIGJvdHRsZW5lY2s6IE5PIFJlTFUgYWZ0ZXIgcHJvamVjdCDigJQgcHJlc2VydmVzIGluZm9ybWF0aW9uXG4gICAgICAgICAgICBubi5Db252MmQoQ19taWQsIENfb3V0LCAxLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQoQ19vdXQpLFxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiB4ICsgc2VsZi5jb252KHgpIGlmIHNlbGYudXNlX3NraXAgZWxzZSBzZWxmLmNvbnYoeCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsaW5lYXIgYm90dGxlbmVjayAobm8gUmVMVSBhZnRlciB0aGUgZmluYWwgMcOXMSkgaXMgY3J1Y2lhbDogYXBwbHlpbmcgYSBub24tbGluZWFyaXR5IGluIGxvdy1kaW1lbnNpb25hbCBzcGFjZSBkZXN0cm95cyBpbmZvcm1hdGlvbi4gU2tpcCBjb25uZWN0aW9ucyBhcHBseSBvbmx5IHdoZW4gc3RyaWRlPTEgYW5kIGlucHV0L291dHB1dCBjaGFubmVscyBtYXRjaCwgcHJlc2VydmluZyBncmFkaWVudCBmbG93IHdpdGhvdXQgaW5mbGF0aW5nIHBhcmFtZXRlciBjb3VudC4gVGhpcyBkZXNpZ24gYWNoaWV2ZXMgSW1hZ2VOZXQgVG9wLTEgb2YgNzIuMCUgYXQgb25seSAzMDBNIEZMT1BzLCBoYWxmIHRoZSBjb21wdXRlIG9mIFYxLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vYmlsZU5ldFYzIEhhcmQtU3dpc2ggYW5kIFNFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb2JpbGVOZXRWMyAoMjAxOSkgd2FzIGNvLWRlc2lnbmVkIHdpdGggbmV1cmFsIGFyY2hpdGVjdHVyZSBzZWFyY2ggdXNpbmcgTW5hc05ldCBhcyBhIHN0YXJ0aW5nIHBvaW50LCB0aGVuIHJlZmluZWQgd2l0aCBOZXRBZGFwdC4gVHdvIHZhcmlhbnRzIGV4aXN0OiBWMy1MYXJnZSB0YXJnZXRpbmcgaGlnaCBhY2N1cmFjeSBhbmQgVjMtU21hbGwgdGFyZ2V0aW5nIGV4dHJlbWUgZWZmaWNpZW5jeS4gVGhlIGFyY2hpdGVjdHVyZSBpbnRyb2R1Y2VzIGhhcmQtc3dpc2ggYWN0aXZhdGlvbiBhbmQgc3F1ZWV6ZS1hbmQtZXhjaXRhdGlvbiAoU0UpIGNoYW5uZWwgYXR0ZW50aW9uLCBib3RoIGFic2VudCBpbiBWMSBhbmQgVjIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG4jIEhhcmQtc3dpc2g6IHBpZWNld2lzZSBsaW5lYXIgYXBwcm94aW1hdGlvbiBvZiBzd2lzaFxuZGVmIGhhcmRfc3dpc2goeCk6XG4gICAgcmV0dXJuIHggKiBGLmhhcmR0YW5oKHggKyAzLCAwLjAsIDYuMCkgLyA2LjBcbiAgICAjIEVxdWl2YWxlbnQ6IHggKiBtaW4obWF4KHgrMywgMCksIDYpIC8gNlxuXG54ID0gdG9yY2gubGluc3BhY2UoLTQsIDQsIDkpXG5wcmludChcInggICAgICAgICA6XCIsIHgubnVtcHkoKS5yb3VuZCgxKSlcbnByaW50KFwiUmVMVSAgICAgIDpcIiwgRi5yZWx1KHgpLm51bXB5KCkucm91bmQoMykpXG5wcmludChcIlN3aXNoICAgICA6XCIsICh4ICogdG9yY2guc2lnbW9pZCh4KSkubnVtcHkoKS5yb3VuZCgzKSlcbnByaW50KFwiSGFyZC1zd2lzaDpcIiwgaGFyZF9zd2lzaCh4KS5udW1weSgpLnJvdW5kKDMpKVxuIyBIYXJkLXN3aXNoOiB+MTUlIGZhc3RlciB0aGFuIHN3aXNoIChubyBzaWdtb2lkKSwgYWNjdXJhY3kgcGFyaXR5IG9uIEltYWdlTmV0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTcXVlZXplLWFuZC1leGNpdGF0aW9uIGFkZHMgYSBsaWdodHdlaWdodCBjaGFubmVsIGF0dGVudGlvbiBnYXRlOiBnbG9iYWwgYXZlcmFnZSBwb29sIOKGkiBGQyhDLzQpIOKGkiBSZUxVIOKGkiBGQyhDKSDihpIgaGFyZC1zaWdtb2lkLiBUaGlzIHJlY2FsaWJyYXRlcyBmZWF0dXJlIG1hcHMgYnkgbGVhcm5pbmcgd2hpY2ggY2hhbm5lbHMgYXJlIG1vc3QgaW5mb3JtYXRpdmUuIFYzIGFwcGxpZXMgU0Ugb25seSBpbiBsYXRlciBibG9ja3MgdG8gbGltaXQgbGF0ZW5jeSBjb3N0LCBzaW5jZSBTRSB3aXRoIGxhcmdlIGNoYW5uZWwgY291bnRzIGlzIGV4cGVuc2l2ZSBvbiBtb2JpbGUgQ1BVcyBsYWNraW5nIHdpZGUgU0lNRCB1bml0cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZXBsb3ltZW50IGFuZCBMYXRlbmN5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGTE9QcyBhcmUgYSB1c2VmdWwgcHJveHkgZm9yIG1vZGVsIGNvbXBsZXhpdHkgYnV0IGNvcnJlbGF0ZSBwb29ybHkgd2l0aCByZWFsIGluZmVyZW5jZSBsYXRlbmN5IG9uIG1vYmlsZSBoYXJkd2FyZS4gTWVtb3J5IGJhbmR3aWR0aCwgY2FjaGUgcHJlc3N1cmUsIG9wZXJhdG9yIGZ1c2lvbiwgYW5kIGhhcmR3YXJlLXNwZWNpZmljIGtlcm5lbHMgYWxsIHBsYXkgbGFyZ2VyIHJvbGVzLiBURkxpdGUgd2l0aCBmdWxsLWludGVnZXIgcXVhbnRpemF0aW9uIChJTlQ4KSB0eXBpY2FsbHkgZGVsaXZlcnMgMuKAkzTDlyBzcGVlZHVwIG92ZXIgRlAzMiBvbiBBUk0gQ29ydGV4LUEgQ1BVcywgd2l0aCBmdXJ0aGVyIGdhaW5zIG9uIE5QVXMgYW5kIERTUHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNodmlzaW9uLm1vZGVscyBhcyBtb2RlbHNcbmZyb20gdG9yY2gudXRpbHMuYmVuY2htYXJrIGltcG9ydCBUaW1lclxuXG5kZWYgYmVuY2htYXJrKG1vZGVsLCBzaGFwZT0oMSwzLDIyNCwyMjQpLCBuPTEwMCk6XG4gICAgbW9kZWwuZXZhbCgpXG4gICAgeCA9IHRvcmNoLnJhbmRuKCpzaGFwZSlcbiAgICB0ID0gVGltZXIoc3RtdD1cIm1vZGVsKHgpXCIsIGdsb2JhbHM9e1wibW9kZWxcIjogbW9kZWwsIFwieFwiOiB4fSlcbiAgICByZXR1cm4gdC50aW1laXQobikubWVhbiAqIDFlMyAgIyBtc1xuXG5iZW5jaCA9IHtcIlYyLTEuMFwiOiBtb2RlbHMubW9iaWxlbmV0X3YyKCksXG4gICAgICAgICBcIlYzLVNtYWxsXCI6IG1vZGVscy5tb2JpbGVuZXRfdjNfc21hbGwoKSxcbiAgICAgICAgIFwiVjMtTGFyZ2VcIjogbW9kZWxzLm1vYmlsZW5ldF92M19sYXJnZSgpfVxuZm9yIGssIG0gaW4gYmVuY2guaXRlbXMoKTpcbiAgICBwcmludChmXCJ7a306IHtiZW5jaG1hcmsobSk6LjFmfSBtc1wiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJjYWxsb3V0VHlwZSI6Indhcm5pbmciLCJ0aXRsZSI6IkZMT1BzIOKJoCBNb2JpbGUgTGF0ZW5jeSIsImNvbnRlbnQiOiJGTE9QcyBkbyBub3QgcHJlZGljdCBtb2JpbGUgbGF0ZW5jeSDigJQgbWVtb3J5IGJhbmR3aWR0aCwgcXVhbnRpemF0aW9uIHN1cHBvcnQsIGFuZCBrZXJuZWwgZnVzaW9uIGRldGVybWluZSByZWFsIHNwZWVkLiBBbHdheXMgYmVuY2htYXJrIG9uIHRoZSBhY3R1YWwgdGFyZ2V0IGRldmljZSB3aXRoIFRGTGl0ZSBvciBDb3JlTUwuIn0seyJ0eXBlIjoidGFibGUiLCJjb250ZW50IjoifCBNb2RlbCB8IFRvcC0xICUgfCBQYXJhbXMgKE0pIHwgRkxPUHMgKE0pIHwgQ1BVIExhdGVuY3kgKG1zKSB8IFRhcmdldCB8XG58LS0tfC0tLXwtLS18LS0tfC0tLXwtLS18XG58IFYxLTEuMCB8IDcwLjYgfCA0LjIgfCA1NzUgfCAxMTMgfCBHZW5lcmFsIG1vYmlsZSB8XG58IFYyLTEuMCB8IDcyLjAgfCAzLjQgfCAzMDAgfCA3NSB8IEdlbmVyYWwgbW9iaWxlIHxcbnwgVjMtU21hbGwgfCA2Ny40IHwgMi41IHwgNTYgfCAyMiB8IEV4dHJlbWUgZWZmaWNpZW5jeSB8XG58IFYzLUxhcmdlIHwgNzUuMiB8IDUuNCB8IDIxOSB8IDUxIHwgSGlnaCBhY2N1cmFjeSBtb2JpbGUgfFxufCBFZmZpY2llbnROZXQtTGl0ZTAgfCA3NS4xIHwgNC43IHwgNDA3IHwgOTggfCBCYWxhbmNlZCB8In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPbiBhIFBpeGVsIDQgQ1BVIChBUk0gQ29ydGV4LUE3NiksIFYzLVNtYWxsIGF0IDIyIG1zIGlzIHJvdWdobHkgNcOXIGZhc3RlciB0aGFuIFYxIGF0IDExMyBtcyB3aGlsZSByZWFjaGluZyBzaW1pbGFyIGFjY3VyYWN5LiBWMy1MYXJnZSBtYXRjaGVzIEVmZmljaWVudE5ldC1MaXRlMCBhY2N1cmFjeSBhdCBuZWFybHkgaGFsZiB0aGUgbGF0ZW5jeS4gQWZ0ZXIgSU5UOCBxdWFudGl6YXRpb24gdmlhIFRGTGl0ZSwgYWxsIG1vZGVscyBzZWUgYSAy4oCTM8OXIHNwZWVkdXAsIHdpdGggVjMtU21hbGwgZHJvcHBpbmcgYmVsb3cgMTAgbXMg4oCUIGZhc3QgZW5vdWdoIGZvciByZWFsLXRpbWUgdmlkZW8gYXQgMzAgZnBzIG9uIG1pZC1yYW5nZSBkZXZpY2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNob29zZSBWMy1TbWFsbCB3aGVuIHBvd2VyIGJ1ZGdldCBvciBtZW1vcnkgaXMgdGhlIHByaW1hcnkgY29uc3RyYWludCDigJQgaXQgcnVucyB1bmRlciAxMCBtcyBvbi1kZXZpY2UgYWZ0ZXIgSU5UOCBxdWFudGl6YXRpb24gYXQgfjY3JSBJbWFnZU5ldCBUb3AtMS4gVjMtTGFyZ2UgaXMgdGhlIGRlZmF1bHQgc3RhcnRpbmcgcG9pbnQgZm9yIG5ldyBtb2JpbGUgcHJvamVjdHM6IGl0IG1hdGNoZXMgRWZmaWNpZW50TmV0LUxpdGUwIGFjY3VyYWN5IGF0IGxvd2VyIGxhdGVuY3kgYW5kIGlzIG5hdGl2ZWx5IHN1cHBvcnRlZCBpbiBQeVRvcmNoLCBUZW5zb3JGbG93LCBhbmQgTWVkaWFQaXBlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiBhZGFwdGluZyBNb2JpbGVOZXRzIHRvIGEgY3VzdG9tIHRhc2sgdmlhIHRyYW5zZmVyIGxlYXJuaW5nLCBmcmVlemUgYWxsIGRlcHRod2lzZSBjb252IHdlaWdodHMgaW4gZWFybHkgYmxvY2tzIGFuZCBmaW5lLXR1bmUgb25seSB0aGUgcG9pbnR3aXNlIGxheWVycyBhbmQgdGhlIGZpbmFsIGNsYXNzaWZpZXIuIFRoaXMgcmVkdWNlcyB0cmFpbmluZyBjb3N0IGRyYW1hdGljYWxseSBiZWNhdXNlIGRlcHRod2lzZSBmaWx0ZXJzIGxlYXJuIGxvdy1sZXZlbCBlZGdlIGRldGVjdG9ycyB0aGF0IHRyYW5zZmVyIHVuaXZlcnNhbGx5LCB3aGlsZSBwb2ludHdpc2UgbWl4ZXJzIGVuY29kZSB0YXNrLXNwZWNpZmljIHNlbWFudGljcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBwcm9kdWN0aW9uIGRlcGxveW1lbnQsIGV4cG9ydCB3aXRoIHRvcmNoLmV4cG9ydCBvciB0Zi5saXRlLlRGTGl0ZUNvbnZlcnRlciwgZW5hYmxlIHBlci1jaGFubmVsIHF1YW50aXphdGlvbiAobW9yZSBhY2N1cmF0ZSB0aGFuIHBlci10ZW5zb3IgZm9yIHBvaW50d2lzZSBsYXllcnMpLCBhbmQgcHJvZmlsZSBsYXllci1ieS1sYXllciB3aXRoIHRoZSBURkxpdGUgYmVuY2htYXJrIHRvb2wgb3IgSW5zdHJ1bWVudHMgb24gaU9TLiBTcXVlZXplLWFuZC1leGNpdGF0aW9uIGJsb2NrcyBhcmUgdGhlIG1haW4gbGF0ZW5jeSBob3RzcG90IOKAlCBjb25zaWRlciBkaXNhYmxpbmcgU0Ugb24gZGV2aWNlcyB3aXRob3V0IHZlY3RvciB1bml0cy4ifV0="
---
# MobileNet: Lightweight CNNs for Edge Deployment

## Overview

MobileNet is a family of efficient CNNs designed for mobile and embedded applications. V1 (2017) introduced depthwise separable convolutions to cut compute dramatically. V2 (2018) added inverted residuals with linear bottlenecks. V3 (2019) incorporated neural architecture search, hard-swish activation, and squeeze-and-excitation modules to further boost accuracy-per-FLOP.

The MobileNet series prioritizes real-world deployability over raw benchmark accuracy. All three versions are quantization-friendly, widely supported in TFLite, CoreML, and ONNX Runtime, and serve as backbones for detection (SSD, YOLO), segmentation (DeepLab), and classification on devices ranging from Raspberry Pi to Apple Neural Engine.

## Depthwise Separable Convolution

A standard conv with kernel K×K on C_in channels to C_out channels costs K²·C_in·C_out FLOPs per spatial position. Depthwise separable convolution splits this into a depthwise step (one filter per input channel, K²·C_in) and a pointwise step (1×1 conv, C_in·C_out). The FLOPs ratio vs standard conv is 1/C_out + 1/K², roughly 8–9× cheaper for K=3.

```python
import torch.nn as nn

def dw_sep_block(C_in, C_out, stride=1):
    return nn.Sequential(
        # Depthwise: groups=C_in applies one filter per channel
        nn.Conv2d(C_in, C_in, 3, stride=stride, padding=1, groups=C_in, bias=False),
        nn.BatchNorm2d(C_in),
        nn.ReLU6(inplace=True),
        # Pointwise: 1×1 conv mixes channels
        nn.Conv2d(C_in, C_out, 1, bias=False),
        nn.BatchNorm2d(C_out),
        nn.ReLU6(inplace=True),
    )
# FLOPs ratio vs standard conv: 1/C_out + 1/K²
# For K=3, C_out=32: ratio ≈ 1/32 + 1/9 ≈ 0.14  (≈7× cheaper)
```

MobileNetV1 stacks 13 such depthwise separable blocks with a width multiplier α ∈ {0.25, 0.5, 0.75, 1.0} that uniformly scales channels, and a resolution multiplier ρ that scales input size. Together they allow an accuracy-latency trade-off tunable to the target hardware without retraining the entire architecture from scratch.

## MobileNetV2 Inverted Residual

V2 flips the traditional residual design. Where ResNet bottlenecks compress to a narrow middle layer, MobileNetV2 expands channel count by factor t (typically 6) before the depthwise convolution, then projects back down. This keeps the depthwise conv operating in a rich high-dimensional space while the skip connection runs in the compact low-dimensional bottleneck space.

```python
class InvertedResidual(nn.Module):
    def __init__(self, C_in, C_out, stride, expand_ratio=6):
        super().__init__()
        C_mid = C_in * expand_ratio
        self.use_skip = (stride == 1 and C_in == C_out)
        self.conv = nn.Sequential(
            nn.Conv2d(C_in, C_mid, 1, bias=False), nn.BatchNorm2d(C_mid), nn.ReLU6(inplace=True),
            nn.Conv2d(C_mid, C_mid, 3, stride=stride, padding=1, groups=C_mid, bias=False), nn.BatchNorm2d(C_mid), nn.ReLU6(inplace=True),
            # Linear bottleneck: NO ReLU after project — preserves information
            nn.Conv2d(C_mid, C_out, 1, bias=False), nn.BatchNorm2d(C_out),
        )
    def forward(self, x):
        return x + self.conv(x) if self.use_skip else self.conv(x)
```

The linear bottleneck (no ReLU after the final 1×1) is crucial: applying a non-linearity in low-dimensional space destroys information. Skip connections apply only when stride=1 and input/output channels match, preserving gradient flow without inflating parameter count. This design achieves ImageNet Top-1 of 72.0% at only 300M FLOPs, half the compute of V1.

## MobileNetV3 Hard-Swish and SE

MobileNetV3 (2019) was co-designed with neural architecture search using MnasNet as a starting point, then refined with NetAdapt. Two variants exist: V3-Large targeting high accuracy and V3-Small targeting extreme efficiency. The architecture introduces hard-swish activation and squeeze-and-excitation (SE) channel attention, both absent in V1 and V2.

```python
import torch
import torch.nn.functional as F

# Hard-swish: piecewise linear approximation of swish
def hard_swish(x):
    return x * F.hardtanh(x + 3, 0.0, 6.0) / 6.0
    # Equivalent: x * min(max(x+3, 0), 6) / 6

x = torch.linspace(-4, 4, 9)
print("x         :", x.numpy().round(1))
print("ReLU      :", F.relu(x).numpy().round(3))
print("Swish     :", (x * torch.sigmoid(x)).numpy().round(3))
print("Hard-swish:", hard_swish(x).numpy().round(3))
# Hard-swish: ~15% faster than swish (no sigmoid), accuracy parity on ImageNet
```

Squeeze-and-excitation adds a lightweight channel attention gate: global average pool → FC(C/4) → ReLU → FC(C) → hard-sigmoid. This recalibrates feature maps by learning which channels are most informative. V3 applies SE only in later blocks to limit latency cost, since SE with large channel counts is expensive on mobile CPUs lacking wide SIMD units.

## Deployment and Latency

FLOPs are a useful proxy for model complexity but correlate poorly with real inference latency on mobile hardware. Memory bandwidth, cache pressure, operator fusion, and hardware-specific kernels all play larger roles. TFLite with full-integer quantization (INT8) typically delivers 2–4× speedup over FP32 on ARM Cortex-A CPUs, with further gains on NPUs and DSPs.

```python
import torch
import torchvision.models as models
from torch.utils.benchmark import Timer

def benchmark(model, shape=(1,3,224,224), n=100):
    model.eval()
    x = torch.randn(*shape)
    t = Timer(stmt="model(x)", globals={"model": model, "x": x})
    return t.timeit(n).mean * 1e3  # ms

bench = {"V2-1.0": models.mobilenet_v2(),
         "V3-Small": models.mobilenet_v3_small(),
         "V3-Large": models.mobilenet_v3_large()}
for k, m in bench.items():
    print(f"{k}: {benchmark(m):.1f} ms")
```

> **FLOPs ≠ Mobile Latency**: FLOPs do not predict mobile latency — memory bandwidth, quantization support, and kernel fusion determine real speed. Always benchmark on the actual target device with TFLite or CoreML.

|  |
| --- |

On a Pixel 4 CPU (ARM Cortex-A76), V3-Small at 22 ms is roughly 5× faster than V1 at 113 ms while reaching similar accuracy. V3-Large matches EfficientNet-Lite0 accuracy at nearly half the latency. After INT8 quantization via TFLite, all models see a 2–3× speedup, with V3-Small dropping below 10 ms — fast enough for real-time video at 30 fps on mid-range devices.

## Key Takeaways

Choose V3-Small when power budget or memory is the primary constraint — it runs under 10 ms on-device after INT8 quantization at ~67% ImageNet Top-1. V3-Large is the default starting point for new mobile projects: it matches EfficientNet-Lite0 accuracy at lower latency and is natively supported in PyTorch, TensorFlow, and MediaPipe.

When adapting MobileNets to a custom task via transfer learning, freeze all depthwise conv weights in early blocks and fine-tune only the pointwise layers and the final classifier. This reduces training cost dramatically because depthwise filters learn low-level edge detectors that transfer universally, while pointwise mixers encode task-specific semantics.

For production deployment, export with torch.export or tf.lite.TFLiteConverter, enable per-channel quantization (more accurate than per-tensor for pointwise layers), and profile layer-by-layer with the TFLite benchmark tool or Instruments on iOS. Squeeze-and-excitation blocks are the main latency hotspot — consider disabling SE on devices without vector units.

