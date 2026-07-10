---
title: "LSTM Gradient Flow — How Gates Solve Vanishing Gradient"
slug: "lstm-gradient-flow"
description: "How LSTM cell-state gradients bypass vanishing gradient: dL/dCt multiplied only by forget gate ft+1 not Whh at every step. Constant error carousel (Hochreiter 1997), forget gate as gradient valve, LSTM vs RNN gradient norms over 100 steps, copying task benchmark, and LSTM variant extensions."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHZhbmlzaGluZyBncmFkaWVudCBwcm9ibGVtIGlzIHRoZSBjZW50cmFsIG9ic3RhY2xlIGluIHRyYWluaW5nIHJlY3VycmVudCBuZXR3b3JrcyBvbiBsb25nIHNlcXVlbmNlczogZ3JhZGllbnRzIHNocmluayBleHBvbmVudGlhbGx5IGFzIHRoZXkgZmxvdyBiYWNrd2FyZCB0aHJvdWdoIHRpbWUsIG1ha2luZyBpdCBpbXBvc3NpYmxlIGZvciB0aGUgbmV0d29yayB0byBsZWFybiBkZXBlbmRlbmNpZXMgc3Bhbm5pbmcgbW9yZSB0aGFuIGEgZmV3IGRvemVuIHN0ZXBzLiBMU1RNIChMb25nIFNob3J0LVRlcm0gTWVtb3J5LCBIb2NocmVpdGVyIFx1MDAyNiBTY2htaWRodWJlciAxOTk3KSBhZGRyZXNzZXMgdGhpcyB3aXRoIHRoZSBjb25zdGFudCBlcnJvciBjYXJvdXNlbCDigJQgYSBkZWRpY2F0ZWQgY2VsbCBzdGF0ZSBDdCB3aG9zZSBncmFkaWVudCBpcyBtdWx0aXBsaWVkIGJ5IGZvcmdldCBnYXRlIHZhbHVlcyBpbnN0ZWFkIG9mIHRoZSBmdWxsIHJlY3VycmVudCB3ZWlnaHQgbWF0cml4IFdoaCwgYWxsb3dpbmcgZ3JhZGllbnQgdG8gZmxvdyBhY3Jvc3MgaHVuZHJlZHMgb2YgdGltZXN0ZXBzIHdpdGhvdXQgZXhwb25lbnRpYWwgZGVjYXkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVmFuaWxsYSBSTk4gYW5kIHRoZSBWYW5pc2hpbmcgR3JhZGllbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIGEgdmFuaWxsYSBSTk4sIGh0ID0gdGFuaChXeHggeHQgKyBXaGggaHQtMSArIGIpLiBUaGUgZ3JhZGllbnQgb2YgdGhlIGxvc3Mgd2l0aCByZXNwZWN0IHRvIGh0IGZsb3dzIGJhY2t3YXJkIGFzIGRML2RodCA9IChkTC9kaHQrMSkgV2ho4bWAIGRpYWcoMSAtIGh0KzHCsikuIEVhY2ggYmFja3dhcmQgc3RlcCBtdWx0aXBsaWVzIGJ5IFdoaOG1gCDigJQgaWYgdGhlIGxhcmdlc3Qgc2luZ3VsYXIgdmFsdWUgb2YgV2hoIGlzIGxlc3MgdGhhbiAxLCB0aGUgcG93ZXIgV2ho4bWA4bWAIHNocmlua3MgdG8gemVybyBleHBvbmVudGlhbGx5OyBpZiBncmVhdGVyIHRoYW4gMSwgaXQgZXhwbG9kZXMuIFRoZSB0YW5oIGZhY3RvciBkaWFnKDEgLSBodMKyKSBpcyBhbHdheXMgaW4gWzAsMV0sIGFkZGluZyBmdXJ0aGVyIHNocmlua2FnZS4gR3JhZGllbnRzIGZyb20gZGlzdGFudCB0aW1lc3RlcHMgYmVjb21lIG5lZ2xpZ2libGUgYWZ0ZXIgMTXigJMyMCBzdGVwcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMU1RNIEFyY2hpdGVjdHVyZSDigJQgQ2VsbCBTdGF0ZSBhbmQgR2F0ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxTVE0gaW50cm9kdWNlcyBhIGNlbGwgc3RhdGUgQ3Qg4oiIIOKEneG0tCBydW5uaW5nIGFsb25nc2lkZSB0aGUgaGlkZGVuIHN0YXRlLiBGb3VyIGdhdGUgY29tcHV0YXRpb25zIGNvbnRyb2wgaW5mb3JtYXRpb24gZmxvdzogZm9yZ2V0IGdhdGUgZnQgPSDPgyhXZltodC0xLCB4dF0gKyBiZikgZGVjaWRlcyB3aGF0IHRvIGVyYXNlOyBpbnB1dCBnYXRlIGl0ID0gz4MoV2lbaHQtMSwgeHRdICsgYmkpIGFuZCBjYW5kaWRhdGUgZ8yDdCA9IHRhbmgoV2dbaHQtMSwgeHRdICsgYmcpIHdyaXRlIG5ldyBpbmZvcm1hdGlvbjsgb3V0cHV0IGdhdGUgb3QgPSDPgyhXb1todC0xLCB4dF0gKyBibykgcmVhZHMgZnJvbSBjZWxsLiBUaGUgYWRkaXRpdmUgY2VsbCB1cGRhdGUgaXMgQ3QgPSBmdCDiipkgQ3QtMSArIGl0IOKKmSBnzIN0LiBUaGlzIGFkZGl0aXZlIHN0cnVjdHVyZSBpcyB0aGUga2V5IHRvIGdyYWRpZW50IGZsb3cg4oCUIGdyYWRpZW50IGNhbiBieXBhc3MgdGhlIHJlY3VycmVudCBtYXRyaXggbXVsdGlwbGljYXRpb24gZW50aXJlbHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc2lnbW9pZCh4KTpcbiAgICByZXR1cm4gMS4wIC8gKDEuMCArIG5wLmV4cCgtbnAuY2xpcCh4LCAtMTAsIDEwKSkpXG5cbmRlZiBzaW11bGF0ZV9ncmFkaWVudF9mbG93KFQ9MTAwLCBIPTMyLCBmb3JnZXRfYmlhcz0yLjAsIHNlZWQ9NDIpOlxuICAgIFwiXCJcIlRyYWNrIGdyYWRpZW50IG5vcm0gdGhyb3VnaCBUIHRpbWVzdGVwczogTFNUTSBjZWxsIHBhdGggdnMgdmFuaWxsYSBSTk4uXCJcIlwiXG4gICAgcm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKHNlZWQpXG4gICAgV2hoID0gcm5nLm5vcm1hbCgwLCAxLjAgLyBucC5zcXJ0KEgpLCAoSCwgSCkpICAjIFJOTiByZWN1cnJlbnQgd2VpZ2h0IG1hdHJpeFxuICAgIGNlbGxfZ3JhZCA9IG5wLm9uZXMoSClcbiAgICBybm5fZ3JhZCAgPSBucC5vbmVzKEgpXG4gICAgY2VsbF9ub3Jtcywgcm5uX25vcm1zID0gWzEuMF0sIFsxLjBdXG5cbiAgICBmb3IgdCBpbiByYW5nZShUKTpcbiAgICAgICAgZiA9IHNpZ21vaWQocm5nLm5vcm1hbChmb3JnZXRfYmlhcywgMC4zLCBIKSkgICMgZm9yZ2V0IGdhdGVzIH5zaWdtb2lkKDIpPTAuODhcbiAgICAgICAgY2VsbF9ncmFkID0gY2VsbF9ncmFkICogZiAgICAgICAgICAgICAgICAgICAgICAjIExTVE06IGVsZW1lbnQtd2lzZSBmb3JnZXQgZ2F0ZSBvbmx5XG4gICAgICAgIHJubl9ncmFkICA9IFdoaC5UIEAgcm5uX2dyYWQgICAgICAgICAgICAgICAgICAgIyBSTk46IGZ1bGwgSCB4IEggbWF0cml4IG11bHRpcGx5XG4gICAgICAgIGNlbGxfbm9ybXMuYXBwZW5kKGZsb2F0KG5wLmxpbmFsZy5ub3JtKGNlbGxfZ3JhZCkpKVxuICAgICAgICBybm5fbm9ybXMuYXBwZW5kKGZsb2F0KG5wLmxpbmFsZy5ub3JtKHJubl9ncmFkKSkpXG5cbiAgICByZXR1cm4gbnAuYXJyYXkoY2VsbF9ub3JtcyksIG5wLmFycmF5KHJubl9ub3JtcylcblxubHN0bV9ub3Jtcywgcm5uX25vcm1zID0gc2ltdWxhdGVfZ3JhZGllbnRfZmxvdyhUPTEwMClcbnByaW50KFx1MDAyN0dyYWRpZW50IG5vcm0gKHN0YXJ0PTEuMCwgZmxvd2luZyBiYWNrd2FyZCB0b3dhcmQgdD0wKTpcdTAwMjcpXG5wcmludChcdTAwMjd7Olx1MDAzZTZ9IHs6XHUwMDNlMTJ9IHs6XHUwMDNlMTR9XHUwMDI3LmZvcm1hdChcdTAwMjdTdGVwXHUwMDI3LCBcdTAwMjdMU1RNIGNlbGxcdTAwMjcsIFx1MDAyN1ZhbmlsbGEgUk5OXHUwMDI3KSlcbmZvciB0IGluIFsxMCwgMjUsIDUwLCA3NSwgMTAwXTpcbiAgICBwcmludChcdTAwMjd7Olx1MDAzZTZ9IHs6XHUwMDNlMTIuNGZ9IHs6XHUwMDNlMTQuNGV9XHUwMDI3LmZvcm1hdCh0LCBsc3RtX25vcm1zW3RdLCBybm5fbm9ybXNbdF0pKVxucHJpbnQoXHUwMDI3TFNUTSByZXRhaW5zIHs6LjFmfSUgb2YgZ3JhZGllbnQgYXQgdD0xMDBcdTAwMjcuZm9ybWF0KDEwMCAqIGxzdG1fbm9ybXNbMTAwXSkpXG5wcmludChcdTAwMjdSTk4gIHJldGFpbnMgezouMmV9JSBvZiBncmFkaWVudCBhdCB0PTEwMFx1MDAyNy5mb3JtYXQoMTAwICogcm5uX25vcm1zWzEwMF0pKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZvcmdldCBHYXRlIGFzIEluZm9ybWF0aW9uIFZhbHZlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY3JpdGljYWwgaW5zaWdodCBpcyBpbiB0aGUgYmFja3dhcmQgcGFzcyB0aHJvdWdoIHRoZSBjZWxsIHN0YXRlOiBkTC9kQ3QgPSBkTC9kQ3QrMSDiipkgZnQrMSArIChjb250cmlidXRpb25zIGZyb20gb3V0cHV0IGdhdGUgcGF0aCkuIEF0IGVhY2ggc3RlcCBiYWNrd2FyZCwgdGhlIGNlbGwgZ3JhZGllbnQgaXMgZWxlbWVudC13aXNlIG11bHRpcGxpZWQgYnkgdGhlIGZvcmdldCBnYXRlIGZ0KzEg4oiIICgwLDEpLiBJZiBmdCDiiYggMSBmb3IgYWxsIHQg4oCUIHRoZSBnYXRlIHN0YXlzIG9wZW4g4oCUIGdyYWRpZW50IGZsb3dzIHRocm91Z2ggYWxsIFQgc3RlcHMgd2l0aCBtaW5pbWFsIGRlY2F5OiB0aGlzIGlzIEhvY2hyZWl0ZXJcdTAwMjdzIGNvbnN0YW50IGVycm9yIGNhcm91c2VsLiBJZiBmdCDiiYggMCwgZ3JhZGllbnQgaXMgYmxvY2tlZCBhdCB0aGF0IHN0ZXAuIFRoZSBtdWx0aXBsaWNhdGlvbiBpcyBieSBmdCAoYSBsZWFybmVkIGdhdGUgdmVjdG9yKSByYXRoZXIgdGhhbiBXaGggKGEgZnVsbCBIw5dIIG1hdHJpeCksIGF2b2lkaW5nIHRoZSBzcGVjdHJhbCByYWRpdXMgcHJvYmxlbSBlbnRpcmVseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZXh0cmFjdF9mb3JnZXRfZ2F0ZXMoc2VxX2xlbj02MCwgaW5wdXRfc2l6ZT00LCBoaWRkZW5fc2l6ZT0xNiwgc2VlZD0xKTpcbiAgICBcIlwiXCJTaG93IGZvcmdldCBnYXRlIGFjdGl2YXRpb25zIHN0ZXAtYnktc3RlcCB1c2luZyBMU1RNQ2VsbC5cIlwiXCJcbiAgICB0b3JjaC5tYW51YWxfc2VlZChzZWVkKVxuICAgIGNlbGwgPSBubi5MU1RNQ2VsbChpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSlcbiAgICB4ID0gdG9yY2guY2F0KFtcbiAgICAgICAgdG9yY2gub25lcyhzZXFfbGVuIC8vIDIsIGlucHV0X3NpemUpLFxuICAgICAgICAtdG9yY2gub25lcyhzZXFfbGVuIC8vIDIsIGlucHV0X3NpemUpXG4gICAgXSwgZGltPTApXG4gICAgaCA9IHRvcmNoLnplcm9zKDEsIGhpZGRlbl9zaXplKVxuICAgIGMgPSB0b3JjaC56ZXJvcygxLCBoaWRkZW5fc2l6ZSlcbiAgICBmZ19tZWFucyA9IFtdXG5cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZm9yIHQgaW4gcmFuZ2Uoc2VxX2xlbik6XG4gICAgICAgICAgICBnYXRlcyA9IHhbdDp0KzFdIEAgY2VsbC53ZWlnaHRfaWguVCArIGggQCBjZWxsLndlaWdodF9oaC5UXG4gICAgICAgICAgICBnYXRlcyArPSBjZWxsLmJpYXNfaWggKyBjZWxsLmJpYXNfaGhcbiAgICAgICAgICAgIGYgPSB0b3JjaC5zaWdtb2lkKGdhdGVzWzosIGhpZGRlbl9zaXplOjIqaGlkZGVuX3NpemVdKVxuICAgICAgICAgICAgZmdfbWVhbnMuYXBwZW5kKGYubWVhbigpLml0ZW0oKSlcbiAgICAgICAgICAgIGgsIGMgPSBjZWxsKHhbdDp0KzFdLCAoaCwgYykpXG5cbiAgICBybSA9IG5wLmFycmF5KGZnX21lYW5zKVxuICAgIHByaW50KFx1MDAyN0ZvcmdldCBnYXRlIG1lYW4gKDE9a2VlcCBtZW1vcnksIDA9ZXJhc2UpOlx1MDAyNylcbiAgICBwcmludChcdTAwMjcgIFBoYXNlIDEgdD0wMC0yOTogezouM2Z9XHUwMDI3LmZvcm1hdChybVs6MzBdLm1lYW4oKSkpXG4gICAgcHJpbnQoXHUwMDI3ICBUcmFuc2l0aW9uIHQ9MzA6IHs6LjNmfSAgXHUwMDNjLSBkcm9wcyBvbiBpbnB1dCBkaXN0cmlidXRpb24gc2hpZnRcdTAwMjcuZm9ybWF0KHJtWzMwXSkpXG4gICAgcHJpbnQoXHUwMDI3ICBQaGFzZSAyIHQ9MzEtNTk6IHs6LjNmfVx1MDAyNy5mb3JtYXQocm1bMzE6XS5tZWFuKCkpKVxuXG5leHRyYWN0X2ZvcmdldF9nYXRlcygpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgUGF0aHM6IENlbGwgU3RhdGUgdnMgSGlkZGVuIFN0YXRlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMU1RNIGhhcyB0d28gZGlzdGluY3QgZ3JhZGllbnQgcGF0aHM6IHRoZSBjZWxsIHN0YXRlIHBhdGggd2hlcmUgZEwvZEN0IGlzIG11bHRpcGxpZWQgb25seSBieSBlbGVtZW50LXdpc2UgZm9yZ2V0IGdhdGVzLCBhbmQgdGhlIGhpZGRlbiBzdGF0ZSBwYXRoIHdoZXJlIGRML2RodCBmbG93cyB0aHJvdWdoIGdhdGUgSmFjb2JpYW5zIGFuZCB3ZWlnaHQgbWF0cmljZXMuIFRoZSBjZWxsIHBhdGggaXMgdGhlIGhpZ2gtc3BlZWQgZ3JhZGllbnQgaGlnaHdheTsgdGhlIGhpZGRlbiBwYXRoIGlzIHN1YmplY3QgdG8gbW9yZSBkZWNheS4gSW4gcHJhY3RpY2UsIGdyYWRpZW50cyBhdCB0PTAgZnJvbSBsb3NzZXMgYXQgdD1UIGFyZSBvcmRlcnMgb2YgbWFnbml0dWRlIGxhcmdlciB2aWEgdGhlIGNlbGwgcGF0aCB0aGFuIHZpYSB0aGUgUk5OIGhpZGRlbiBwYXRoLCB3aGljaCBpcyB3aHkgTFNUTSBjYW4gY2FwdHVyZSBkZXBlbmRlbmNpZXMgYXQgMTAwKyBzdGVwIGRpc3RhbmNlcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiR3JhZGllbnQgUGF0aCIsIk11bHRpcGxpZWQgQnkgRWFjaCBTdGVwIiwiVmFuaXNoaW5nIFJpc2siLCJMb25nLVJhbmdlIChUPTEwMCkiXSwicm93cyI6W1siVmFuaWxsYSBSTk4gaGlkZGVuIiwiV2ho4bWAIMK3IGRpYWcoMS1odMKyKSIsIkhpZ2gg4oCUIG1hdHJpeCBwb3dlciwgc3BlY3RyYWwgcmFkaXVzIFx1MDAzYyAxIGtpbGxzIGdyYWRpZW50IiwiTmVhciB6ZXJvIGZvciBtb3N0IHdlaWdodCBpbml0cyJdLFsiTFNUTSBjZWxsIHN0YXRlIiwiZnQrMSBlbGVtZW50LXdpc2UsIGZ0IOKIiCAoMCwxKSIsIkxvdyDigJQgcHJvZHVjdCBvZiBzY2FsYXJzOyBzdGF5cyBuZWFyIDEgaWYgZm9yZ2V0IGJpYXMgXHUwMDNlIDAiLCI1MOKAkzkwJSByZXRhaW5lZCB3aXRoIGZ0IOKJiCAwLjg4Il0sWyJMU1RNIGhpZGRlbiBzdGF0ZSIsIkdhdGUgSmFjb2JpYW5zICsgcGFydGlhbCBXaGggdGVybXMiLCJNZWRpdW0g4oCUIG1vcmUgcGF0aHMgYnV0IHN0aWxsIHBhcnRpYWxseSBtYXRyaXgtZ2F0ZWQiLCJQYXJ0aWFsIOKAlCBiZXR0ZXIgdGhhbiBSTk4sIHdvcnNlIHRoYW4gY2VsbCJdLFsiR1JVIGhpZGRlbiBzdGF0ZSIsInp0IHVwZGF0ZSBnYXRlIChpbnRlcnBvbGF0aW9uKSIsIk1lZGl1bSDigJQgdXBkYXRlIGdhdGUgYWN0cyBhcyBjb21iaW5lZCBmb3JnZXQvaW5wdXQiLCJTaW1pbGFyIHRvIExTVE0gY2VsbCBpbiBwcmFjdGljZSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29weWluZyBUYXNrIEJlbmNobWFyayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvcHlpbmcgdGFzayB0ZXN0cyBsb25nLXJhbmdlIG1lbW9yeSBkaXJlY3RseTogYSB0b2tlbiBwcmVzZW50ZWQgYXQgdD0wIG11c3QgYmUgcmVwcm9kdWNlZCBhZnRlciBUIGJsYW5rIGZpbGxlciB0aW1lc3RlcHMuIE5vIHNob3J0Y3V0IGV4aXN0cyDigJQgdGhlIG1vZGVsIG11c3QgaG9sZCB0aGUgaW5pdGlhbCB0b2tlbiBpbiB3b3JraW5nIG1lbW9yeSBhY3Jvc3MgVCBzdGVwcy4gVmFuaWxsYSBSTk5zIGZhaWwgYXQgVCBcdTAwM2UgMjDigJMzMCBkdWUgdG8gdmFuaXNoaW5nIGdyYWRpZW50cy4gTFNUTXMgc29sdmUgdGhlIHRhc2sgcmVsaWFibHkgZm9yIFQgdXAgdG8gMjAwKyBzdGVwcyBiZWNhdXNlIHRoZSBjZWxsIHN0YXRlIGNhbiBtYWludGFpbiB0aGUgcmVxdWlyZWQgaW5mb3JtYXRpb24gdGhyb3VnaCB0aGUgZm9yZ2V0IGdhdGUgaG9sZGluZyBuZWFyIDEuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cblxuY2xhc3MgVmFuaWxsYVJOTkNvcHkobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl90b2ssIGgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbWIgPSBubi5FbWJlZGRpbmcobl90b2sgKyAxLCBoKVxuICAgICAgICBzZWxmLnJubiA9IG5uLlJOTihoLCBoLCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLmZjICA9IG5uLkxpbmVhcihoLCBuX3RvaylcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgXywgaG4gPSBzZWxmLnJubihzZWxmLmVtYih4KSlcbiAgICAgICAgcmV0dXJuIHNlbGYuZmMoaG4uc3F1ZWV6ZSgwKSlcblxuY2xhc3MgTFNUTUNvcHkobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl90b2ssIGgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbWIgID0gbm4uRW1iZWRkaW5nKG5fdG9rICsgMSwgaClcbiAgICAgICAgc2VsZi5sc3RtID0gbm4uTFNUTShoLCBoLCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLmZjICAgPSBubi5MaW5lYXIoaCwgbl90b2spXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIF8sIChobiwgXykgPSBzZWxmLmxzdG0oc2VsZi5lbWIoeCkpXG4gICAgICAgIHJldHVybiBzZWxmLmZjKGhuLnNxdWVlemUoMCkpXG5cbmRlZiBydW5fdGFzayhNb2RlbENsYXNzLCBUPTUwLCBuX3Rvaz04LCBoPTY0LCBlcG9jaHM9NDApOlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuICAgIHRhcmdldHMgPSB0b3JjaC5yYW5kaW50KDAsIG5fdG9rLCAoMjU2LCkpXG4gICAgc2VxcyA9IHRvcmNoLmZ1bGwoKDI1NiwgVCArIDEpLCBuX3RvaykgICMgYmxhbmsgPSBuX3Rva1xuICAgIHNlcXNbOiwgMF0gPSB0YXJnZXRzXG4gICAgbW9kZWwgPSBNb2RlbENsYXNzKG5fdG9rLCBoKVxuICAgIG9wdCA9IG9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0yZS0zKVxuICAgIGZvciBfIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIGxvc3MgPSBubi5Dcm9zc0VudHJvcHlMb3NzKCkobW9kZWwoc2VxcyksIHRhcmdldHMpXG4gICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgcmV0dXJuIChtb2RlbChzZXFzKS5hcmdtYXgoMSkgPT0gdGFyZ2V0cykuZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG5cbnByaW50KFx1MDAyN0NvcHlpbmcgdGFzayAoVD01MCBibGFuayBzdGVwcywgOCB0b2tlbiBjbGFzc2VzLCBjaGFuY2U9MC4xMjUpOlx1MDAyNylcbnByaW50KFx1MDAyNyAgVmFuaWxsYSBSTk4gYWNjdXJhY3k6IHs6LjNmfVx1MDAyNy5mb3JtYXQocnVuX3Rhc2soVmFuaWxsYVJOTkNvcHkpKSlcbnByaW50KFx1MDAyNyAgTFNUTSAgICAgICAgYWNjdXJhY3k6IHs6LjNmfVx1MDAyNy5mb3JtYXQocnVuX3Rhc2soTFNUTUNvcHkpKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcmFkaWVudCBIaWdod2F5IOKAlCBDZWxsIHZzIEhpZGRlbiBOb3JtcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG8gdmlzdWFsaXplIHRoZSBncmFkaWVudCBoaWdod2F5IGVtcGlyaWNhbGx5LCBjb21wdXRlIHRoZSBncmFkaWVudCBvZiB0aGUgbGFzdC1zdGVwIGxvc3Mgd2l0aCByZXNwZWN0IHRvIGVhY2ggdGltZXN0ZXBcdTAwMjdzIGlucHV0IHZlY3Rvci4gTGFyZ2UgZ3JhZGllbnQgYXQgZWFybHkgdGltZXN0ZXBzIG1lYW5zIHRoZSBuZXR3b3JrIGlzIGxlYXJuaW5nIGZyb20gZGlzdGFudCBpbnB1dHMuIE5lYXItemVybyBncmFkaWVudCBhdCB0PTAgbWVhbnMgdGhlIHNpZ25hbCBoYXMgdmFuaXNoZWQgYW5kIHRob3NlIHN0ZXBzIGNvbnRyaWJ1dGUgbm90aGluZyB0byBsZWFybmluZy4gTFNUTVx1MDAyN3MgY2VsbCBwYXRoIGRlbGl2ZXJzIGdyYWRpZW50cyBhdCB0PTAgdGhhdCBhcmUgb3JkZXJzIG9mIG1hZ25pdHVkZSBsYXJnZXIgdGhhbiB2YW5pbGxhIFJOTiDigJQgd2hpY2ggZXhwbGFpbnMgd2h5IExTVE0gY2FuIGFjdHVhbGx5IHVwZGF0ZSB3ZWlnaHRzIGJhc2VkIG9uIGlucHV0cyBzZWVuIDQwKyBzdGVwcyBlYXJsaWVyLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBncmFkaWVudF9oaWdod2F5KG1ha2Vfcm5uLCBUPTQwLCBIPTI0LCBJPTQpOlxuICAgIFwiXCJcIkdyYWRpZW50IG5vcm0gYXQgZWFjaCB0aW1lc3RlcFx1MDAyN3MgaW5wdXQgZnJvbSBsb3NzIGF0IHRoZSBmaW5hbCB0aW1lc3RlcC5cIlwiXCJcbiAgICB0b3JjaC5tYW51YWxfc2VlZCgwKVxuICAgIG1vZGVsID0gbWFrZV9ybm4oSSwgSCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICB4ID0gdG9yY2gucmFuZG4oMSwgVCwgSSwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxuICAgIG91dCwgXyA9IG1vZGVsKHgpXG4gICAgb3V0WzAsIC0xLCA6XS5zdW0oKS5iYWNrd2FyZCgpXG4gICAgcmV0dXJuIHguZ3JhZFswXS5ub3JtKGRpbT0xKS5kZXRhY2goKS5udW1weSgpXG5cbmxzdG1fZyA9IGdyYWRpZW50X2hpZ2h3YXkobm4uTFNUTSlcbnJubl9nICA9IGdyYWRpZW50X2hpZ2h3YXkobm4uUk5OKVxuXG5wcmludChcdTAwMjdHcmFkaWVudCBub3JtIHBlciBpbnB1dCB0aW1lc3RlcCAobG9zcyBhdCB0PTM5LCBUPTQwKTpcdTAwMjcpXG5wcmludChcdTAwMjd7Olx1MDAzZTV9IHs6XHUwMDNlMTJ9IHs6XHUwMDNlMTJ9XHUwMDI3LmZvcm1hdChcdTAwMjd0XHUwMDI3LCBcdTAwMjdMU1RNXHUwMDI3LCBcdTAwMjdSTk5cdTAwMjcpKVxuZm9yIHQgaW4gWzAsIDUsIDEwLCAyMCwgMzAsIDM5XTpcbiAgICBwcmludChcdTAwMjd7Olx1MDAzZTV9IHs6XHUwMDNlMTIuNGZ9IHs6XHUwMDNlMTIuNGV9XHUwMDI3LmZvcm1hdCh0LCBmbG9hdChsc3RtX2dbdF0pLCBmbG9hdChybm5fZ1t0XSkpKVxucmF0aW8gPSBmbG9hdChsc3RtX2dbMF0pIC8gbWF4KGZsb2F0KHJubl9nWzBdKSwgMWUtMjApXG5wcmludChcdTAwMjdSYXRpbyBMU1RNL1JOTiBhdCB0PTA6IHs6LjJlfXggbW9yZSBncmFkaWVudCBwcmVzZXJ2ZWRcdTAwMjcuZm9ybWF0KHJhdGlvKSkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkxTVE0gRG9lcyBOb3QgRnVsbHkgU29sdmUgVmFuaXNoaW5nIEdyYWRpZW50IiwiY29udGVudCI6IklmIHRoZSBmb3JnZXQgZ2F0ZSBzYXR1cmF0ZXMgbmVhciB6ZXJvIChmdCDiiYggMCksIGdyYWRpZW50IGlzIGJsb2NrZWQgYXQgdGhhdCB0aW1lc3RlcCDigJQgYSBsZWFybmVkIGZvcmdldHRpbmcgZXZlbnQgc3RvcHMgZ3JhZGllbnQgZmxvdyBqdXN0IGFzIGVmZmVjdGl2ZWx5IGFzIHZhbmlzaGluZy4gT3ZlciB2ZXJ5IGxvbmcgc2VxdWVuY2VzLCB0aGUgcHJvZHVjdCBvZiBmb3JnZXQgZ2F0ZXMgzqAgZnQgc3RpbGwgc2hyaW5rcyBpZiBmdCBcdTAwM2MgMSBjb25zaXN0ZW50bHkuIExTVE1zIHdpdGggbGFyZ2UgZm9yZ2V0IGdhdGUgYmlhcyAoaW5pdGlhbGl6ZWQgbmVhciAxLCBlLmcuIGJpYXNfZiA9IDEuMCkgY29tYmluZWQgd2l0aCBncmFkaWVudCBjbGlwcGluZyB3b3JrIHdlbGwgaW4gcHJhY3RpY2UsIGJ1dCBwcm92aWRlIG5vIHRoZW9yZXRpY2FsIGd1YXJhbnRlZSBvZiBjb21wbGV0ZSBncmFkaWVudCBwcmVzZXJ2YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTFNUTSBWYXJpYW50cyBhbmQgRXh0ZW5zaW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2V2ZXJhbCB2YXJpYW50cyBleHRlbmQgdGhlIGJhc2ljIExTVE06IHBlZXBob2xlIGNvbm5lY3Rpb25zIGFsbG93IGdhdGVzIHRvIHNlZSB0aGUgY2VsbCBzdGF0ZSBkaXJlY3RseSDigJQgZnQgPSDPgyhXZltodC0xLCBDdC0xLCB4dF0gKyBiZikg4oCUIGltcHJvdmluZyBwcmVjaXNpb24gZm9yIHBlcmlvZGljIHRpbWluZyB0YXNrczsgUGhhc2VkIExTVE0gYWRkcyBhbiBvc2NpbGxhdG9yeSB0aW1lIGdhdGUgdGhhdCBvcGVucyBvbmx5IGF0IGNlcnRhaW4gcGhhc2VzLCBlbmFibGluZyBlZmZpY2llbnQgcHJvY2Vzc2luZyBvZiBpcnJlZ3VsYXJseS1zYW1wbGVkIHRpbWUgc2VyaWVzOyBHUlUgKENobyBldCBhbC4gMjAxNCkgbWVyZ2VzIGZvcmdldCBhbmQgaW5wdXQgZ2F0ZXMgaW50byBhbiB1cGRhdGUgZ2F0ZSBhbmQgZWxpbWluYXRlcyB0aGUgc2VwYXJhdGUgY2VsbCBzdGF0ZSwgb2Z0ZW4gbWF0Y2hpbmcgTFNUTSBwZXJmb3JtYW5jZSB3aXRoIGZld2VyIHBhcmFtZXRlcnM7IExheWVyIE5vcm0gTFNUTSBhcHBsaWVzIGxheWVyIG5vcm1hbGl6YXRpb24gaW5zaWRlIGVhY2ggZ2F0ZSBmb3Igc3RhYmlsaXR5IGluIGRlZXAgc3RhY2tzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUGVlcGhvbGUgTFNUTTogZ2F0ZXMgc2VlIEN0LTEgZGlyZWN0bHkg4oCUIGJldHRlciB0ZW1wb3JhbCBwcmVjaXNpb24gZm9yIENUQyBzcGVlY2ggdGFza3MuIiwiUGhhc2VkIExTVE06IG9zY2lsbGF0b3J5IHRpbWUgZ2F0ZSDigJQgdXBkYXRlcyBvbmx5IGF0IGNlcnRhaW4gcGhhc2VzIGZvciBhc3luY2hyb25vdXMgc2Vuc29yIGRhdGEuIiwiR1JVIChDaG8gMjAxNCk6IDIgZ2F0ZXMsIG5vIGNlbGwgc3RhdGUsIH4yNSUgZmV3ZXIgcGFyYW1zIOKAlCBvZnRlbiBjb21wZXRpdGl2ZSBvbiBzaG9ydCBzZXF1ZW5jZXMuIiwiQ291cGxlZCBJbnB1dC1Gb3JnZXQ6IGl0ID0gMSAtIGZ0IOKAlCBvbmUgZmV3ZXIgZ2F0ZSwgZW5mb3JjZXMgY29uc2VydmF0aW9uICh3aGF0IGlzIGZvcmdvdHRlbiBpcyByZXBsYWNlZCkuIiwiTGF5ZXIgTm9ybSBMU1RNOiBub3JtYWxpemVzIGdhdGUgcHJlLWFjdGl2YXRpb25zIOKAlCBzdGFiaWxpemVzIGRlZXAgc3RhY2tzIG9mIDQrIGxheWVycy4iLCJtaW5MU1RNIC8gbWluR1JVICgyMDI0KTogc2ltcGxpZmllZCB2YXJpYW50cyBwYXJhbGxlbGl6YWJsZSB2aWEgYXNzb2NpYXRpdmUgc2NhbiDigJQgbm8gc2VxdWVudGlhbCBkZXBlbmRlbmN5IGF0IHRyYWluaW5nIHRpbWUuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGZ1bmRhbWVudGFsIGluc2lnaHQgb2YgTFNUTSDigJQgdXNpbmcgYW4gYWRkaXRpdmUgY2VsbCB1cGRhdGUgd2l0aCBsZWFybmVkIGdhdGluZyByYXRoZXIgdGhhbiBtdWx0aXBsaWNhdGl2ZSByZWN1cnJlbnQgbWF0cml4IOKAlCBpbmZsdWVuY2VkIHZpcnR1YWxseSBldmVyeSBzdWJzZXF1ZW50IHNlcXVlbmNlIG1vZGVsLiBUcmFuc2Zvcm1lcnMgZXh0ZW5kIHRoaXMgaWRlYSBmdXJ0aGVyIGJ5IHVzaW5nIGF0dGVudGlvbiB0byByb3V0ZSBncmFkaWVudCBhY3Jvc3MgYXJiaXRyYXJ5IHBvc2l0aW9ucyB3aXRob3V0IGFueSByZWN1cnJlbnQgc3RydWN0dXJlLCBidXQgTFNUTSByZW1haW5zIHRoZSByZWZlcmVuY2UgYmFzZWxpbmUgZm9yIHRhc2tzIHJlcXVpcmluZyBpbnRlcnByZXRhYmxlIGdhdGUgYmVoYXZpb3IgYW5kIGV4YWN0IHNlcXVlbnRpYWwgcHJvY2Vzc2luZy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# LSTM Gradient Flow — How Gates Solve Vanishing Gradient

The vanishing gradient problem is the central obstacle in training recurrent networks on long sequences: gradients shrink exponentially as they flow backward through time, making it impossible for the network to learn dependencies spanning more than a few dozen steps. LSTM (Long Short-Term Memory, Hochreiter & Schmidhuber 1997) addresses this with the constant error carousel — a dedicated cell state Ct whose gradient is multiplied by forget gate values instead of the full recurrent weight matrix Whh, allowing gradient to flow across hundreds of timesteps without exponential decay.

## Vanilla RNN and the Vanishing Gradient

In a vanilla RNN, ht = tanh(Wxx xt + Whh ht-1 + b). The gradient of the loss with respect to ht flows backward as dL/dht = (dL/dht+1) Whhᵀ diag(1 - ht+1²). Each backward step multiplies by Whhᵀ — if the largest singular value of Whh is less than 1, the power Whhᵀᵀ shrinks to zero exponentially; if greater than 1, it explodes. The tanh factor diag(1 - ht²) is always in [0,1], adding further shrinkage. Gradients from distant timesteps become negligible after 15–20 steps.

## LSTM Architecture — Cell State and Gates

LSTM introduces a cell state Ct ∈ ℝᴴ running alongside the hidden state. Four gate computations control information flow: forget gate ft = σ(Wf[ht-1, xt] + bf) decides what to erase; input gate it = σ(Wi[ht-1, xt] + bi) and candidate g̃t = tanh(Wg[ht-1, xt] + bg) write new information; output gate ot = σ(Wo[ht-1, xt] + bo) reads from cell. The additive cell update is Ct = ft ⊙ Ct-1 + it ⊙ g̃t. This additive structure is the key to gradient flow — gradient can bypass the recurrent matrix multiplication entirely.

```python
import numpy as np

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -10, 10)))

def simulate_gradient_flow(T=100, H=32, forget_bias=2.0, seed=42):
    """Track gradient norm through T timesteps: LSTM cell path vs vanilla RNN."""
    rng = np.random.default_rng(seed)
    Whh = rng.normal(0, 1.0 / np.sqrt(H), (H, H))  # RNN recurrent weight matrix
    cell_grad = np.ones(H)
    rnn_grad  = np.ones(H)
    cell_norms, rnn_norms = [1.0], [1.0]

    for t in range(T):
        f = sigmoid(rng.normal(forget_bias, 0.3, H))  # forget gates ~sigmoid(2)=0.88
        cell_grad = cell_grad * f                      # LSTM: element-wise forget gate only
        rnn_grad  = Whh.T @ rnn_grad                   # RNN: full H x H matrix multiply
        cell_norms.append(float(np.linalg.norm(cell_grad)))
        rnn_norms.append(float(np.linalg.norm(rnn_grad)))

    return np.array(cell_norms), np.array(rnn_norms)

lstm_norms, rnn_norms = simulate_gradient_flow(T=100)
print('Gradient norm (start=1.0, flowing backward toward t=0):')
print('{:>6} {:>12} {:>14}'.format('Step', 'LSTM cell', 'Vanilla RNN'))
for t in [10, 25, 50, 75, 100]:
    print('{:>6} {:>12.4f} {:>14.4e}'.format(t, lstm_norms[t], rnn_norms[t]))
print('LSTM retains {:.1f}% of gradient at t=100'.format(100 * lstm_norms[100]))
print('RNN  retains {:.2e}% of gradient at t=100'.format(100 * rnn_norms[100]))
```

## Forget Gate as Information Valve

The critical insight is in the backward pass through the cell state: dL/dCt = dL/dCt+1 ⊙ ft+1 + (contributions from output gate path). At each step backward, the cell gradient is element-wise multiplied by the forget gate ft+1 ∈ (0,1). If ft ≈ 1 for all t — the gate stays open — gradient flows through all T steps with minimal decay: this is Hochreiter's constant error carousel. If ft ≈ 0, gradient is blocked at that step. The multiplication is by ft (a learned gate vector) rather than Whh (a full H×H matrix), avoiding the spectral radius problem entirely.

```python
import torch
import torch.nn as nn
import numpy as np

def extract_forget_gates(seq_len=60, input_size=4, hidden_size=16, seed=1):
    """Show forget gate activations step-by-step using LSTMCell."""
    torch.manual_seed(seed)
    cell = nn.LSTMCell(input_size, hidden_size)
    x = torch.cat([
        torch.ones(seq_len // 2, input_size),
        -torch.ones(seq_len // 2, input_size)
    ], dim=0)
    h = torch.zeros(1, hidden_size)
    c = torch.zeros(1, hidden_size)
    fg_means = []

    with torch.no_grad():
        for t in range(seq_len):
            gates = x[t:t+1] @ cell.weight_ih.T + h @ cell.weight_hh.T
            gates += cell.bias_ih + cell.bias_hh
            f = torch.sigmoid(gates[:, hidden_size:2*hidden_size])
            fg_means.append(f.mean().item())
            h, c = cell(x[t:t+1], (h, c))

    rm = np.array(fg_means)
    print('Forget gate mean (1=keep memory, 0=erase):')
    print('  Phase 1 t=00-29: {:.3f}'.format(rm[:30].mean()))
    print('  Transition t=30: {:.3f}  <- drops on input distribution shift'.format(rm[30]))
    print('  Phase 2 t=31-59: {:.3f}'.format(rm[31:].mean()))

extract_forget_gates()
```

## Gradient Paths: Cell State vs Hidden State

LSTM has two distinct gradient paths: the cell state path where dL/dCt is multiplied only by element-wise forget gates, and the hidden state path where dL/dht flows through gate Jacobians and weight matrices. The cell path is the high-speed gradient highway; the hidden path is subject to more decay. In practice, gradients at t=0 from losses at t=T are orders of magnitude larger via the cell path than via the RNN hidden path, which is why LSTM can capture dependencies at 100+ step distances.

| Gradient Path | Multiplied By Each Step | Vanishing Risk | Long-Range (T=100) |
| --- | --- | --- | --- |
| Vanilla RNN hidden | Whhᵀ · diag(1-ht²) | High — matrix power, spectral radius < 1 kills gradient | Near zero for most weight inits |
| LSTM cell state | ft+1 element-wise, ft ∈ (0,1) | Low — product of scalars; stays near 1 if forget bias > 0 | 50–90% retained with ft ≈ 0.88 |
| LSTM hidden state | Gate Jacobians + partial Whh terms | Medium — more paths but still partially matrix-gated | Partial — better than RNN, worse than cell |
| GRU hidden state | zt update gate (interpolation) | Medium — update gate acts as combined forget/input | Similar to LSTM cell in practice |

## Copying Task Benchmark

The copying task tests long-range memory directly: a token presented at t=0 must be reproduced after T blank filler timesteps. No shortcut exists — the model must hold the initial token in working memory across T steps. Vanilla RNNs fail at T > 20–30 due to vanishing gradients. LSTMs solve the task reliably for T up to 200+ steps because the cell state can maintain the required information through the forget gate holding near 1.

```python
import torch
import torch.nn as nn
import torch.optim as optim

class VanillaRNNCopy(nn.Module):
    def __init__(self, n_tok, h):
        super().__init__()
        self.emb = nn.Embedding(n_tok + 1, h)
        self.rnn = nn.RNN(h, h, batch_first=True)
        self.fc  = nn.Linear(h, n_tok)
    def forward(self, x):
        _, hn = self.rnn(self.emb(x))
        return self.fc(hn.squeeze(0))

class LSTMCopy(nn.Module):
    def __init__(self, n_tok, h):
        super().__init__()
        self.emb  = nn.Embedding(n_tok + 1, h)
        self.lstm = nn.LSTM(h, h, batch_first=True)
        self.fc   = nn.Linear(h, n_tok)
    def forward(self, x):
        _, (hn, _) = self.lstm(self.emb(x))
        return self.fc(hn.squeeze(0))

def run_task(ModelClass, T=50, n_tok=8, h=64, epochs=40):
    torch.manual_seed(42)
    targets = torch.randint(0, n_tok, (256,))
    seqs = torch.full((256, T + 1), n_tok)  # blank = n_tok
    seqs[:, 0] = targets
    model = ModelClass(n_tok, h)
    opt = optim.Adam(model.parameters(), lr=2e-3)
    for _ in range(epochs):
        loss = nn.CrossEntropyLoss()(model(seqs), targets)
        opt.zero_grad(); loss.backward(); opt.step()
    return (model(seqs).argmax(1) == targets).float().mean().item()

print('Copying task (T=50 blank steps, 8 token classes, chance=0.125):')
print('  Vanilla RNN accuracy: {:.3f}'.format(run_task(VanillaRNNCopy)))
print('  LSTM        accuracy: {:.3f}'.format(run_task(LSTMCopy)))
```

## Gradient Highway — Cell vs Hidden Norms

To visualize the gradient highway empirically, compute the gradient of the last-step loss with respect to each timestep's input vector. Large gradient at early timesteps means the network is learning from distant inputs. Near-zero gradient at t=0 means the signal has vanished and those steps contribute nothing to learning. LSTM's cell path delivers gradients at t=0 that are orders of magnitude larger than vanilla RNN — which explains why LSTM can actually update weights based on inputs seen 40+ steps earlier.

```python
import torch
import torch.nn as nn
import numpy as np

def gradient_highway(make_rnn, T=40, H=24, I=4):
    """Gradient norm at each timestep's input from loss at the final timestep."""
    torch.manual_seed(0)
    model = make_rnn(I, H, batch_first=True)
    x = torch.randn(1, T, I, requires_grad=True)
    out, _ = model(x)
    out[0, -1, :].sum().backward()
    return x.grad[0].norm(dim=1).detach().numpy()

lstm_g = gradient_highway(nn.LSTM)
rnn_g  = gradient_highway(nn.RNN)

print('Gradient norm per input timestep (loss at t=39, T=40):')
print('{:>5} {:>12} {:>12}'.format('t', 'LSTM', 'RNN'))
for t in [0, 5, 10, 20, 30, 39]:
    print('{:>5} {:>12.4f} {:>12.4e}'.format(t, float(lstm_g[t]), float(rnn_g[t])))
ratio = float(lstm_g[0]) / max(float(rnn_g[0]), 1e-20)
print('Ratio LSTM/RNN at t=0: {:.2e}x more gradient preserved'.format(ratio))
```

> **LSTM Does Not Fully Solve Vanishing Gradient**: If the forget gate saturates near zero (ft ≈ 0), gradient is blocked at that timestep — a learned forgetting event stops gradient flow just as effectively as vanishing. Over very long sequences, the product of forget gates Π ft still shrinks if ft < 1 consistently. LSTMs with large forget gate bias (initialized near 1, e.g. bias_f = 1.0) combined with gradient clipping work well in practice, but provide no theoretical guarantee of complete gradient preservation.

## LSTM Variants and Extensions

Several variants extend the basic LSTM: peephole connections allow gates to see the cell state directly — ft = σ(Wf[ht-1, Ct-1, xt] + bf) — improving precision for periodic timing tasks; Phased LSTM adds an oscillatory time gate that opens only at certain phases, enabling efficient processing of irregularly-sampled time series; GRU (Cho et al. 2014) merges forget and input gates into an update gate and eliminates the separate cell state, often matching LSTM performance with fewer parameters; Layer Norm LSTM applies layer normalization inside each gate for stability in deep stacks.

- Peephole LSTM: gates see Ct-1 directly — better temporal precision for CTC speech tasks.
- Phased LSTM: oscillatory time gate — updates only at certain phases for asynchronous sensor data.
- GRU (Cho 2014): 2 gates, no cell state, ~25% fewer params — often competitive on short sequences.
- Coupled Input-Forget: it = 1 - ft — one fewer gate, enforces conservation (what is forgotten is replaced).
- Layer Norm LSTM: normalizes gate pre-activations — stabilizes deep stacks of 4+ layers.
- minLSTM / minGRU (2024): simplified variants parallelizable via associative scan — no sequential dependency at training time.

The fundamental insight of LSTM — using an additive cell update with learned gating rather than multiplicative recurrent matrix — influenced virtually every subsequent sequence model. Transformers extend this idea further by using attention to route gradient across arbitrary positions without any recurrent structure, but LSTM remains the reference baseline for tasks requiring interpretable gate behavior and exact sequential processing.

---

