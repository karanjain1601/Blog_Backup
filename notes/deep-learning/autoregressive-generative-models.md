---
title: "Autoregressive Models — PixelCNN, WaveNet, and Language Models"
slug: "autoregressive-generative-models"
description: "A deep dive into autoregressive generative models — how masked convolutions in PixelCNN, dilated causal convolutions in WaveNet, and transformer-based language models all share the same factorization p(x)=∏p(xᵢ|x<i), covering evaluation via bits-per-dim and the two-stage VQ-VAE+PixelCNN approach."
tags: ["deep-learning", "generative-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXV0b3JlZ3Jlc3NpdmUgbW9kZWxzIGRlY29tcG9zZSB0aGUgam9pbnQgZGlzdHJpYnV0aW9uIG9mIGEgaGlnaC1kaW1lbnNpb25hbCB2YXJpYWJsZSB4IGludG8gYSBwcm9kdWN0IG9mIGNvbmRpdGlvbmFsczogcCh4KSA9IOKIj+G1oiBwKHjhtaIgfCB44oKBLCDigKYsIHjhtaLigovigoEpLiBUaGlzIGZhY3Rvcml6YXRpb24gaXMgZXhhY3Qg4oCUIG5vIGFwcHJveGltYXRpb24gaXMgaW50cm9kdWNlZCDigJQgYW5kIHRoZSBjaGFpbiBydWxlIG9mIHByb2JhYmlsaXR5IGd1YXJhbnRlZXMgaXQgYWx3YXlzIHlpZWxkcyBhIHZhbGlkIHByb2JhYmlsaXR5IGRpc3RyaWJ1dGlvbi4gVGhlIG9yZGVyaW5nIG9mIGRpbWVuc2lvbnMgaXMgYSBkZXNpZ24gY2hvaWNlOiByYXN0ZXIgc2NhbiBvcmRlciAocm93IGJ5IHJvdywgbGVmdCB0byByaWdodCkgZm9yIGltYWdlcywgdGltZSBvcmRlciBmb3IgYXVkaW8sIGFuZCB0b2tlbiBvcmRlciBmb3IgdGV4dC4gRXZlcnkgZWxlbWVudCBpbiB0aGUgc2VxdWVuY2UgaXMgcHJlZGljdGVkIGZyb20gYWxsIHByZXZpb3VzIGVsZW1lbnRzLCBtYWtpbmcgdGhlc2UgbW9kZWxzIFR1cmluZy1jb21wbGV0ZSBnZW5lcmF0aXZlIG1vZGVscyBjYXBhYmxlIG9mIGNhcHR1cmluZyBhcmJpdHJhcmlseSBjb21wbGV4IGRlcGVuZGVuY2llcyBnaXZlbiBzdWZmaWNpZW50IGNhcGFjaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1dG9yZWdyZXNzaXZlIEZhY3Rvcml6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjb3JlIGVxdWF0aW9uIHAoeCkgPSDiiI/htaIgcCh44bWiIHwgeOKCgSwg4oCmLCB44bWi4oKL4oKBKSBoYXMgc2V2ZXJhbCBjcml0aWNhbCBwcm9wZXJ0aWVzLiBGaXJzdCwgYmVjYXVzZSBpdCBmb2xsb3dzIGZyb20gdGhlIGNoYWluIHJ1bGUgb2YgcHJvYmFiaWxpdHksIHRyYWluaW5nIGJ5IG1heGltdW0gbGlrZWxpaG9vZCAobWluaW1pemluZyBuZWdhdGl2ZSBsb2ctbGlrZWxpaG9vZCkgaXMgc3RyYWlnaHRmb3J3YXJkIGFuZCBzdGFibGUg4oCUIHRoZXJlIGlzIG5vIGFkdmVyc2FyaWFsIG9iamVjdGl2ZSwgbm8gcmVjb25zdHJ1Y3Rpb24tYXBwcm94aW1hdGlvbiB0cmFkZW9mZiwgYW5kIG5vIHBvc3RlcmlvciBjb2xsYXBzZS4gU2Vjb25kLCBkdXJpbmcgdHJhaW5pbmcgYWxsIGNvbmRpdGlvbmFscyBjYW4gYmUgY29tcHV0ZWQgaW4gcGFyYWxsZWwgdXNpbmcgdGVhY2hlciBmb3JjaW5nOiB0aGUgZ3JvdW5kLXRydXRoIHByZWZpeCBpcyBmZWQgYXMgaW5wdXQgYW5kIHRoZSBtb2RlbCBwcmVkaWN0cyB0aGUgbmV4dCBlbGVtZW50IGF0IGV2ZXJ5IHBvc2l0aW9uIHNpbXVsdGFuZW91c2x5LiBUaGlyZCwgZHVyaW5nIGdlbmVyYXRpb24gc2FtcGxlcyBtdXN0IGJlIGRyYXduIHNlcXVlbnRpYWxseSDigJQgZWFjaCBuZXcgZWxlbWVudCByZXF1aXJlcyBhIGZ1bGwgZm9yd2FyZCBwYXNzIOKAlCBtYWtpbmcgc2FtcGxpbmcgTyhMKSBpbiBzZXF1ZW5jZSBsZW5ndGggYW5kIG9mdGVuIHRoZSBwcmltYXJ5IGJvdHRsZW5lY2sgZm9yIGxvbmcgc2VxdWVuY2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBpeGVsQ05OIOKAlCBNYXNrZWQgQ29udm9sdXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQaXhlbENOTiAodmFuIGRlbiBPb3JkIGV0IGFsLiAyMDE2KSBtb2RlbHMgaW1hZ2VzIGF1dG9yZWdyZXNzaXZlbHkgaW4gcmFzdGVyIHNjYW4gb3JkZXIgdXNpbmcgbWFza2VkIGNvbnZvbHV0aW9ucyB0byBlbmZvcmNlIGNhdXNhbGl0eS4gQSBUeXBlLUEgbWFzayB6ZXJvcyBvdXQgdGhlIGNlbnRlciBwaXhlbCBhbmQgYWxsIHBpeGVscyB0byBpdHMgcmlnaHQgYW5kIGJlbG93LCBlbnN1cmluZyBwKHhfaSB8IHhfe1x1MDAzY2l9KSBkb2VzIG5vdCBpbmNsdWRlIHhfaSBpdHNlbGYg4oCUIHVzZWQgb25seSBpbiB0aGUgZmlyc3QgbGF5ZXIuIEEgVHlwZS1CIG1hc2sgaW5jbHVkZXMgdGhlIGNlbnRlciBwaXhlbCwgYWxsb3dpbmcgdGhlIG1vZGVsIHRvIHJlZmluZSBpdHMgcmVwcmVzZW50YXRpb24gb2YgeF9pIGZyb20gcHJldmlvdXMgbGF5ZXJzIGJ1dCBuZXZlciBsZWFraW5nIGZ1dHVyZSBwaXhlbHMuIFN0YWNraW5nIG1hbnkgZ2F0ZWQgcmVzaWR1YWwgYmxvY2tzIHdpdGggVHlwZS1CIG1hc2tzIGFsbG93cyB0aGUgbW9kZWwgdG8gYnVpbGQgZGVlcCByZXByZXNlbnRhdGlvbnMgd2hpbGUgcmVzcGVjdGluZyB0aGUgY2F1c2FsIGNvbnN0cmFpbnQuIFBpeGVsQ05OKysgcmVwbGFjZXMgdGhlIDI1Ni13YXkgc29mdG1heCBvdXRwdXQgd2l0aCBhIG1peHR1cmUgb2YgbG9naXN0aWNzLCBkcmFtYXRpY2FsbHkgcmVkdWNpbmcgdGhlIG51bWJlciBvZiBvdXRwdXQgcGFyYW1ldGVycyBhbmQgaW1wcm92aW5nIHNhbXBsZSBxdWFsaXR5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBNYXNrZWRDb252MmQobm4uQ29udjJkKTpcbiAgICBcIlwiXCJUeXBlIEE6IGV4Y2x1ZGVzIGNlbnRlciBwaXhlbCAoZmlyc3QgbGF5ZXIpLiBUeXBlIEI6IGluY2x1ZGVzIGNlbnRlciAoc3Vic2VxdWVudCBsYXllcnMpLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBtYXNrX3R5cGUsICphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKmFyZ3MsICoqa3dhcmdzKVxuICAgICAgICBhc3NlcnQgbWFza190eXBlIGluIChcdTAwMjdBXHUwMDI3LCBcdTAwMjdCXHUwMDI3KVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdtYXNrXHUwMDI3LCBzZWxmLndlaWdodC5kYXRhLmNsb25lKCkpXG4gICAgICAgIF8sIF8sIGtILCBrVyA9IHNlbGYud2VpZ2h0LnNpemUoKVxuICAgICAgICBzZWxmLm1hc2suZmlsbF8oMSlcbiAgICAgICAgc2VsZi5tYXNrWzosIDosIGtIIC8vIDIsIGtXIC8vIDIgKyAoMSBpZiBtYXNrX3R5cGUgPT0gXHUwMDI3Qlx1MDAyNyBlbHNlIDApOl0gPSAwXG4gICAgICAgIHNlbGYubWFza1s6LCA6LCBrSCAvLyAyICsgMTosIDpdID0gMFxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHNlbGYud2VpZ2h0LmRhdGEgKj0gc2VsZi5tYXNrXG4gICAgICAgIHJldHVybiBzdXBlcigpLmZvcndhcmQoeClcblxuY2xhc3MgR2F0ZWRSZXNCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2ZpbHRlcnM9NjQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5jb252ID0gTWFza2VkQ29udjJkKFx1MDAyN0JcdTAwMjcsIG5fZmlsdGVycywgMiAqIG5fZmlsdGVycywga2VybmVsX3NpemU9MywgcGFkZGluZz0xKVxuICAgICAgICBzZWxmLnJlc19jb252ID0gbm4uQ29udjJkKG5fZmlsdGVycywgbl9maWx0ZXJzLCAxKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG91dCA9IHNlbGYuY29udih4KVxuICAgICAgICB0YW5oX3BhcnQsIHNpZ19wYXJ0ID0gb3V0LmNodW5rKDIsIGRpbT0xKVxuICAgICAgICBnYXRlZCA9IHRvcmNoLnRhbmgodGFuaF9wYXJ0KSAqIHRvcmNoLnNpZ21vaWQoc2lnX3BhcnQpXG4gICAgICAgIHJldHVybiB4ICsgc2VsZi5yZXNfY29udihnYXRlZClcblxubWFza19hID0gTWFza2VkQ29udjJkKFx1MDAyN0FcdTAwMjcsIDEsIDY0LCBrZXJuZWxfc2l6ZT03LCBwYWRkaW5nPTMpXG5tYXNrX2IgPSBHYXRlZFJlc0Jsb2NrKG5fZmlsdGVycz02NClcbnggPSB0b3JjaC5yYW5kbigyLCAxLCAyOCwgMjgpXG5wcmludChcdTAwMjdUeXBlLUEgb3V0cHV0Olx1MDAyNywgbWFza19hKHgpLnNoYXBlKVxucHJpbnQoXHUwMDI3R2F0ZWQgUmVzQmxvY2sgb3V0cHV0Olx1MDAyNywgbWFza19iKG1hc2tfYSh4KSkuc2hhcGUpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2F1c2FsIG1hc2tpbmcgcHJvcGVydHkgY2FuIGJlIHZlcmlmaWVkIGVtcGlyaWNhbGx5OiBpZiBhbnkgZ3JhZGllbnQgZmxvd3MgZnJvbSBwb3NpdGlvbiBpIGJhY2sgdG8gcG9zaXRpb24gaiBcdTAwM2UgaSwgdGhlIG1hc2tpbmcgaXMgaW5jb3JyZWN0LiBUeXBlLUEgY29udm9sdXRpb25zIGd1YXJhbnRlZSB0aGF0IHRoZSByZWNlcHRpdmUgZmllbGQgb2YgcGl4ZWwgaSBpcyBzdHJpY3RseSBjb250YWluZWQgaW4ge3BpeGVsIDAsIOKApiwgcGl4ZWwgaS0xfS4gSW4gcHJhY3RpY2UsIFBpeGVsQ05OIG1vZGVscyA4LWJpdCBwaXhlbCB2YWx1ZXMgKDI1NiBjbGFzc2VzKSBhdCBlYWNoIGxvY2F0aW9uOyBQaXhlbENOTisrIG1vZGVscyB0aGUgbG9naXN0aWMgbWl4dHVyZSBkaXJlY3RseSB0byBhdm9pZCB0aGUgMjU2LXdheSBzb2Z0bWF4IGJvdHRsZW5lY2suIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2F2ZU5ldCDigJQgRGlsYXRlZCBDYXVzYWwgQ29udm9sdXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXYXZlTmV0ICh2YW4gZGVuIE9vcmQgZXQgYWwuIDIwMTYpIGFwcGxpZXMgYXV0b3JlZ3Jlc3NpdmUgbW9kZWxpbmcgdG8gcmF3IGF1ZGlvIHdhdmVmb3JtcyBhdCAxNuKAkzI0IGtIei4gVGhlIGtleSBhcmNoaXRlY3R1cmFsIGlubm92YXRpb24gaXMgZGlsYXRlZCBjYXVzYWwgY29udm9sdXRpb25zIHdpdGggZXhwb25lbnRpYWxseSBncm93aW5nIGRpbGF0aW9uIHJhdGVzOiAxLCAyLCA0LCA4LCAxNiwg4oCmLCA1MTIuIEEgc2luZ2xlIGRpbGF0ZWQgY29udm9sdXRpb24gd2l0aCBkaWxhdGlvbiBkIGhhcyBhIHJlY2VwdGl2ZSBmaWVsZCBvZiBkKzEgc3RlcHMuIFN0YWNraW5nIGRpbGF0aW9uIHJhdGVzIDEsIDIsIDQsIOKApiwgNTEyIGluIG9uZSBibG9jayBjb3ZlcnMgMTAyNCB0aW1lc3RlcHMuIE11bHRpcGxlIHN1Y2ggc3RhY2tzIGNvdmVyIHJlY2VwdGl2ZSBmaWVsZHMgb2YgdGVucyBvZiB0aG91c2FuZHMgb2Ygc2FtcGxlcy4gQ2F1c2FsaXR5IGlzIGVuZm9yY2VkIGJ5IHNoaWZ0aW5nIHRoZSBpbnB1dCByaWdodCBzbyB0aGF0IHBvc2l0aW9uIGkgY2FuIG9ubHkgc2VlIHBvc2l0aW9ucyDiiaQgaS4gV2F2ZU5ldCBjb25kaXRpb25zIG9uIGxvY2FsIGZlYXR1cmVzIChzcGVha2VyIGlkZW50aXR5LCBtZWwgc3BlY3Ryb2dyYW0pIGJ5IGFkZGluZyBhIGNvbmRpdGlvbmluZyBzaWduYWwgdG8gdGhlIGdhdGVkIGFjdGl2YXRpb24gYXQgZWFjaCBsYXllci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgRGlsYXRlZENhdXNhbENvbnYxZChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkNhdXNhbCBkaWxhdGVkIGNvbnY6IHBhZHMgbGVmdCBvbmx5IHNvIG91dHB1dFt0XSBkZXBlbmRzIG9ubHkgb24gaW5wdXRbXHUwMDNjPXRdLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgb3V0X2NoLCBrZXJuZWxfc2l6ZT0yLCBkaWxhdGlvbj0xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZGlsYXRpb24gPSBkaWxhdGlvblxuICAgICAgICBzZWxmLnBhZCA9IChrZXJuZWxfc2l6ZSAtIDEpICogZGlsYXRpb24gICMgbGVmdCBwYWQgb25seSBmb3IgY2F1c2FsaXR5XG4gICAgICAgIHNlbGYuY29udiA9IG5uLkNvbnYxZChpbl9jaCwgb3V0X2NoLCBrZXJuZWxfc2l6ZSwgZGlsYXRpb249ZGlsYXRpb24pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgeCA9IEYucGFkKHgsIChzZWxmLnBhZCwgMCkpXG4gICAgICAgIHJldHVybiBzZWxmLmNvbnYoeClcblxuY2xhc3MgV2F2ZU5ldEJsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fY2hhbm5lbHM9NjQsIGRpbGF0aW9uPTEsIGNvbmRfY2hhbm5lbHM9Tm9uZSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmRpbGF0ZWRfY29udiA9IERpbGF0ZWRDYXVzYWxDb252MWQobl9jaGFubmVscywgMiAqIG5fY2hhbm5lbHMsIGtlcm5lbF9zaXplPTIsIGRpbGF0aW9uPWRpbGF0aW9uKVxuICAgICAgICBzZWxmLnJlc19jb252ID0gbm4uQ29udjFkKG5fY2hhbm5lbHMsIG5fY2hhbm5lbHMsIDEpXG4gICAgICAgIHNlbGYuc2tpcF9jb252ID0gbm4uQ29udjFkKG5fY2hhbm5lbHMsIG5fY2hhbm5lbHMsIDEpXG4gICAgICAgIHNlbGYuY29uZF9jb252ID0gbm4uQ29udjFkKGNvbmRfY2hhbm5lbHMsIDIgKiBuX2NoYW5uZWxzLCAxKSBpZiBjb25kX2NoYW5uZWxzIGVsc2UgTm9uZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgY29uZD1Ob25lKTpcbiAgICAgICAgaCA9IHNlbGYuZGlsYXRlZF9jb252KHgpXG4gICAgICAgIGlmIGNvbmQgaXMgbm90IE5vbmUgYW5kIHNlbGYuY29uZF9jb252IGlzIG5vdCBOb25lOlxuICAgICAgICAgICAgaCA9IGggKyBzZWxmLmNvbmRfY29udihjb25kKVxuICAgICAgICB0YW5oX2gsIHNpZ19oID0gaC5jaHVuaygyLCBkaW09MSlcbiAgICAgICAgaCA9IHRvcmNoLnRhbmgodGFuaF9oKSAqIHRvcmNoLnNpZ21vaWQoc2lnX2gpXG4gICAgICAgIHNraXAgPSBzZWxmLnNraXBfY29udihoKVxuICAgICAgICByZXMgID0gc2VsZi5yZXNfY29udihoKSArIHhcbiAgICAgICAgcmV0dXJuIHJlcywgc2tpcFxuXG4jIEJ1aWxkIFdhdmVOZXQgc3RhY2sgd2l0aCBleHBvbmVudGlhbCBkaWxhdGlvbiByYXRlc1xuZGlsYXRpb25zID0gWzEsIDIsIDQsIDgsIDE2LCAzMiwgNjQsIDEyOCwgMjU2LCA1MTJdXG5ibG9ja3MgPSBubi5Nb2R1bGVMaXN0KFtXYXZlTmV0QmxvY2sobl9jaGFubmVscz02NCwgZGlsYXRpb249ZCkgZm9yIGQgaW4gZGlsYXRpb25zXSlcbnggPSB0b3JjaC5yYW5kbigyLCA2NCwgMTAyNCkgICMgYmF0Y2g9MiwgY2hhbm5lbHM9NjQsIFQ9MTAyNFxuc2tpcHMgPSBbXVxuZm9yIGJsb2NrIGluIGJsb2NrczpcbiAgICB4LCBza2lwID0gYmxvY2soeClcbiAgICBza2lwcy5hcHBlbmQoc2tpcClcbm91dCA9IHN1bShza2lwcylcbnByaW50KGZcdTAwMjdSZWNlcHRpdmUgZmllbGQ6IHtzdW0oZGlsYXRpb25zKSArIDF9IHRpbWVzdGVwcywgb3V0cHV0IHNoYXBlOiB7b3V0LnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYW5ndWFnZSBNb2RlbHMgYXMgQXV0b3JlZ3Jlc3NpdmUgTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHUFQgYW5kIGl0cyBzdWNjZXNzb3JzIGFwcGx5IGF1dG9yZWdyZXNzaXZlIG1vZGVsaW5nIG92ZXIgdG9rZW4gc2VxdWVuY2VzLiBUaGUgdm9jYWJ1bGFyeSBkZWZpbmVzIHRoZSBkaXNjcmV0ZSBzcGFjZSAoNTBr4oCTMTAwayB0b2tlbnMgZm9yIEJQRSksIGFuZCB0aGUgbW9kZWwgbGVhcm5zIHAodG9rZW5fdCB8IHRva2VuXzEsIOKApiwgdG9rZW5fe3QtMX0pLiBUcmFuc2Zvcm1lcnMgaW1wbGVtZW50IGNhdXNhbCBtYXNraW5nIHZpYSBhbiB1cHBlci10cmlhbmd1bGFyIGF0dGVudGlvbiBtYXNrIHRoYXQgcHJldmVudHMgZWFjaCBwb3NpdGlvbiBmcm9tIGF0dGVuZGluZyB0byBmdXR1cmUgcG9zaXRpb25zLiBVbmxpa2UgUGl4ZWxDTk5cdTAwMjdzIGZpeGVkIHJhc3RlciBvcmRlciwgbGFuZ3VhZ2UgbW9kZWxzIGJlbmVmaXQgZnJvbSB0aGUgbmF0dXJhbCBzZXF1ZW50aWFsIHN0cnVjdHVyZSBvZiB0ZXh0LiBUcmFpbmluZyBvbiBuZXh0LXRva2VuIHByZWRpY3Rpb24gYXQgc2NhbGUgbGVhZHMgdG8gZW1lcmdlbnQgY2FwYWJpbGl0aWVzOiB0aGUgc2FtZSBtYXhpbXVtLWxpa2VsaWhvb2Qgb2JqZWN0aXZlIHByb2R1Y2VzIG1vZGVscyB0aGF0IHRyYW5zbGF0ZSwgc3VtbWFyaXplLCByZWFzb24sIGFuZCBnZW5lcmF0ZSBjb2RlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBTaW1wbGVQaXhlbENOTihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIk1pbmltYWwgUGl4ZWxDTk4gZm9yIE1OSVNUOiB0cmFpbiB3aXRoIE5MTCwgZ2VuZXJhdGUgc2VxdWVudGlhbGx5LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2ZpbHRlcnM9NjQsIG5fbGF5ZXJzPTYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5maXJzdCA9IE1hc2tlZENvbnYyZChcdTAwMjdBXHUwMDI3LCAxLCBuX2ZpbHRlcnMsIGtlcm5lbF9zaXplPTcsIHBhZGRpbmc9MylcbiAgICAgICAgc2VsZi5sYXllcnMgPSBubi5TZXF1ZW50aWFsKCpbR2F0ZWRSZXNCbG9jayhuX2ZpbHRlcnMpIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKV0pXG4gICAgICAgIHNlbGYub3V0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChuX2ZpbHRlcnMsIDI1NiwgMSksICAjIDI1Ni13YXkgc29mdG1heCBwZXIgcGl4ZWxcbiAgICAgICAgKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGggPSBzZWxmLmZpcnN0KHguZmxvYXQoKSAvIDI1NS4wIC0gMC41KVxuICAgICAgICBoID0gc2VsZi5sYXllcnMoaClcbiAgICAgICAgcmV0dXJuIHNlbGYub3V0KGgpICAjIChCLCAyNTYsIEgsIFcpIGxvZ2l0c1xuXG5jbGFzcyBNYXNrZWRDb252MmQobm4uQ29udjJkKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbWFza190eXBlLCAqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKCphcmdzLCAqKmt3YXJncylcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3bWFza1x1MDAyNywgc2VsZi53ZWlnaHQuZGF0YS5jbG9uZSgpKVxuICAgICAgICBfLCBfLCBrSCwga1cgPSBzZWxmLndlaWdodC5zaXplKClcbiAgICAgICAgc2VsZi5tYXNrLmZpbGxfKDEpXG4gICAgICAgIHNlbGYubWFza1s6LCA6LCBrSCAvLyAyLCBrVyAvLyAyICsgKDEgaWYgbWFza190eXBlID09IFx1MDAyN0JcdTAwMjcgZWxzZSAwKTpdID0gMFxuICAgICAgICBzZWxmLm1hc2tbOiwgOiwga0ggLy8gMiArIDE6LCA6XSA9IDBcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgc2VsZi53ZWlnaHQuZGF0YSAqPSBzZWxmLm1hc2tcbiAgICAgICAgcmV0dXJuIHN1cGVyKCkuZm9yd2FyZCh4KVxuXG5jbGFzcyBHYXRlZFJlc0Jsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fZmlsdGVycyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmNvbnYgPSBNYXNrZWRDb252MmQoXHUwMDI3Qlx1MDAyNywgbl9maWx0ZXJzLCAyICogbl9maWx0ZXJzLCBrZXJuZWxfc2l6ZT0zLCBwYWRkaW5nPTEpXG4gICAgICAgIHNlbGYucmVzID0gbm4uQ29udjJkKG5fZmlsdGVycywgbl9maWx0ZXJzLCAxKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICB0LCBzID0gc2VsZi5jb252KHgpLmNodW5rKDIsIGRpbT0xKVxuICAgICAgICByZXR1cm4geCArIHNlbGYucmVzKHRvcmNoLnRhbmgodCkgKiB0b3JjaC5zaWdtb2lkKHMpKVxuXG5tb2RlbCA9IFNpbXBsZVBpeGVsQ05OKClcbnhfYmF0Y2ggPSB0b3JjaC5yYW5kaW50KDAsIDI1NiwgKDQsIDEsIDI4LCAyOCkpXG5sb2dpdHMgPSBtb2RlbCh4X2JhdGNoKVxubG9zcyA9IEYuY3Jvc3NfZW50cm9weShsb2dpdHMsIHhfYmF0Y2hbOiwgMF0ubG9uZygpKVxucHJpbnQoZlx1MDAyN0xvZ2l0czoge2xvZ2l0cy5zaGFwZX0sIE5MTCBsb3NzOiB7bG9zcy5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCaXRzLXBlci1EaW0gRXZhbHVhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXV0b3JlZ3Jlc3NpdmUgbW9kZWxzIHByb2R1Y2UgZXhhY3QgbG9nLWxpa2VsaWhvb2RzLCBlbmFibGluZyByaWdvcm91cyBldmFsdWF0aW9uIHZpYSBiaXRzLXBlci1kaW0gKEJQRCkuIEJQRCBjb252ZXJ0cyB0aGUgbmVnYXRpdmUgbG9nLWxpa2VsaWhvb2QgKGluIG5hdHMsIGJhc2UtZSkgdG8gYml0cywgbm9ybWFsaXNlZCBieSB0aGUgbnVtYmVyIG9mIGRpbWVuc2lvbnMgKHBpeGVscyBvciBzYW1wbGVzKS4gSXQgY29ycmVzcG9uZHMgdG8gdGhlIG51bWJlciBvZiBiaXRzIG5lZWRlZCB0byBsb3NzbGVzc2x5IGNvbXByZXNzIGVhY2ggZGltZW5zaW9uIG9uIGF2ZXJhZ2Ug4oCUIGxvd2VyIGlzIGJldHRlciwgYW5kIGVudHJvcHkgb2YgdGhlIGRhdGEgZGlzdHJpYnV0aW9uIGlzIHRoZSB0aGVvcmV0aWNhbCBtaW5pbXVtLiBCUEQgbWFrZXMgbW9kZWxzIGNvbXBhcmFibGUgYWNyb3NzIGRhdGFzZXRzIG9mIGRpZmZlcmVudCBzaXplIGFuZCByZXNvbHV0aW9uLiBGb3IgTU5JU1QsIHN0YXRlLW9mLXRoZS1hcnQgYXV0b3JlZ3Jlc3NpdmUgbW9kZWxzIGFjaGlldmUgfjAuOCBCUEQ7IGZvciBDSUZBUi0xMCwgYXJvdW5kIDIuOCBCUEQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuZGVmIGNvbXB1dGVfYml0c19wZXJfZGltKG1vZGVsLCBkYXRhbG9hZGVyLCBkZXZpY2U9XHUwMDI3Y3B1XHUwMDI3KTpcbiAgICBcIlwiXCJcbiAgICBDb21wdXRlIGJpdHMtcGVyLWRpbTogYXZlcmFnZSBOTEwgaW4gbmF0cyAvIChIICogVykgLyBsbigyKS5cbiAgICBGb3IgaW1hZ2VzOiBsb3dlciA9IGJldHRlciBjb21wcmVzc2lvbiA9IGJldHRlciBnZW5lcmF0aXZlIG1vZGVsLlxuICAgIEJQRCA9IEVbLWxvZzIgcCh4KV0gLyAoSCAqIFcpID0gRVstbG9nIHAoeCldIC8gKEggKiBXICogbG9nKDIpKVxuICAgIFwiXCJcIlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIHRvdGFsX25sbCA9IDAuMFxuICAgIHRvdGFsX3BpeGVscyA9IDBcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZm9yIHgsIF8gaW4gZGF0YWxvYWRlcjpcbiAgICAgICAgICAgIHggPSB4LnRvKGRldmljZSkgICMgKEIsIDEsIEgsIFcpIGluIFswLCAyNTVdXG4gICAgICAgICAgICBCLCBDLCBILCBXID0geC5zaGFwZVxuICAgICAgICAgICAgbG9naXRzID0gbW9kZWwoeCkgICMgKEIsIDI1NiwgSCwgVylcbiAgICAgICAgICAgICMgTkxMIHN1bW1lZCBvdmVyIGFsbCBwaXhlbHMgaW4gYmF0Y2hcbiAgICAgICAgICAgIG5sbCA9IEYuY3Jvc3NfZW50cm9weShsb2dpdHMsIHhbOiwgMF0ubG9uZygpLCByZWR1Y3Rpb249XHUwMDI3c3VtXHUwMDI3KVxuICAgICAgICAgICAgdG90YWxfbmxsICs9IG5sbC5pdGVtKClcbiAgICAgICAgICAgIHRvdGFsX3BpeGVscyArPSBCICogSCAqIFdcbiAgICBhdmdfbmxsX3Blcl9waXhlbCA9IHRvdGFsX25sbCAvIHRvdGFsX3BpeGVsc1xuICAgIGJpdHNfcGVyX2RpbSA9IGF2Z19ubGxfcGVyX3BpeGVsIC8gbWF0aC5sb2coMilcbiAgICByZXR1cm4gYml0c19wZXJfZGltXG5cbiMgRGVtb25zdHJhdGUgY29udmVyc2lvbiBmb3JtdWxhXG5kZWYgbmxsX3RvX2JwZChubGxfbmF0cywgaGVpZ2h0LCB3aWR0aCwgbl9zYW1wbGVzKTpcbiAgICBhdmcgPSBubGxfbmF0cyAvIChuX3NhbXBsZXMgKiBoZWlnaHQgKiB3aWR0aClcbiAgICByZXR1cm4gYXZnIC8gbWF0aC5sb2coMilcblxuZm9yIG5sbCwgaCwgdywgbiBpbiBbKDUwMC4wLCAyOCwgMjgsIDEpLCAoMzIwMC4wLCAzMiwgMzIsIDEpXTpcbiAgICBicGQgPSBubGxfdG9fYnBkKG5sbCwgaCwgdywgbilcbiAgICBwcmludChmXHUwMDI3TkxMPXtubGw6LjBmfSBuYXRzLCB7aH14e3d9IGltYWdlIC1cdTAwM2Uge2JwZDouM2Z9IGJpdHMvZGltXHUwMDI3KVxuXG5wcmludChcdTAwMjdNTklTVCBTT1RBOiB+MC44IEJQRCB8IENJRkFSLTEwIFNPVEE6IH4yLjggQlBEIHwgSW1hZ2VOZXQgNjR4NjQgU09UQTogfjMuNCBCUERcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHdvLVN0YWdlOiBWUS1WQUUgKyBQaXhlbENOTiBQcmlvciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGl4ZWwtc3BhY2UgYXV0b3JlZ3Jlc3NpdmUgZ2VuZXJhdGlvbiBvdmVyIDI1NsOXMjU2IGltYWdlcyByZXF1aXJlcyBtb2RlbGluZyAxOTYsNjA4IGRpbWVuc2lvbnMg4oCUIGNvbXB1dGF0aW9uYWxseSBwcm9oaWJpdGl2ZS4gVlEtVkFFICh2YW4gZGVuIE9vcmQgZXQgYWwuIDIwMTcpIHNvbHZlcyB0aGlzIGJ5IGZpcnN0IGNvbXByZXNzaW5nIGltYWdlcyBpbnRvIGEgZGlzY3JldGUgbGF0ZW50IGdyaWQgKGUuZy4sIDMyw5czMiB0b2tlbnMgZnJvbSBhIGNvZGVib29rIG9mIDUxMiBlbnRyaWVzKSwgdGhlbiB0cmFpbmluZyBhbiBhdXRvcmVncmVzc2l2ZSBwcmlvciAoUGl4ZWxDTk4gb3IgVHJhbnNmb3JtZXIpIG92ZXIgdGhlIG11Y2ggc2hvcnRlciAzMsOXMzIgPSAxMDI0IHRva2VuIHNlcXVlbmNlLiBHZW5lcmF0aW9uIHByb2NlZWRzIGluIHR3byBzdGFnZXM6IHNhbXBsZSB0aGUgZGlzY3JldGUgbGF0ZW50IGdyaWQgYXV0b3JlZ3Jlc3NpdmVseSwgdGhlbiBkZWNvZGUgdG8gcGl4ZWxzIHdpdGggdGhlIFZRLVZBRSBkZWNvZGVyLiBUaGlzIHR3by1zdGFnZSBhcHByb2FjaCBhbGxvd3MgYXV0b3JlZ3Jlc3NpdmUgbW9kZWxzIHRvIHNjYWxlIHRvIGhpZ2gtcmVzb2x1dGlvbiBpbWFnZXMgYW5kIGlzIHRoZSBhcmNoaXRlY3R1cmFsIGFuY2VzdG9yIG9mIERBTEwtRSBhbmQgbW9kZXJuIGltYWdlIHRva2VuaXplcnMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJTYW1wbGluZyBTcGVlZCBCb3R0bGVuZWNrIiwiY29udGVudCI6IkF1dG9yZWdyZXNzaXZlIG1vZGVscyBhcmUgc2xvdyB0byBzYW1wbGUgYmVjYXVzZSBlYWNoIHRva2VuIHJlcXVpcmVzIGEgZnVsbCBmb3J3YXJkIHBhc3Mgd2l0aCBubyBwYXJhbGxlbGlzbS4gRm9yIGEgMjU2w5cyNTYgaW1hZ2UgKDY1LDUzNiBwaXhlbHMpIHdpdGggYSAxMDBtcyBmb3J3YXJkIHBhc3MsIHNhbXBsaW5nIHRha2VzIH4xLjggaG91cnMgc2VxdWVudGlhbGx5LiBTcGVjdWxhdGl2ZSBkZWNvZGluZywgY2FjaGluZyBLViBzdGF0ZXMgaW4gdHJhbnNmb3JtZXJzLCBhbmQgd29ya2luZyBpbiBjb21wcmVzc2VkIGxhdGVudCBzcGFjZSAoVlEtVkFFKSBhcmUgdGhlIG1haW4gcHJhY3RpY2FsIG1pdGlnYXRpb25zLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIk1vZGFsaXR5IiwiQXJjaGl0ZWN0dXJlIiwiVHJhaW5pbmcgT2JqZWN0aXZlIiwiU2FtcGxpbmcgU3BlZWQiLCJFdmFsdWF0aW9uIE1ldHJpYyJdLCJyb3dzIjpbWyJQaXhlbENOTiIsIkltYWdlcyIsIk1hc2tlZCBjb252IHN0YWNrIiwiQ3Jvc3MtZW50cm9weSAoMjU2LXdheSkiLCJTbG93IOKAlCBPKEjDl1cpIHN0ZXBzIiwiQml0cy1wZXItZGltIChCUEQpIl0sWyJQaXhlbENOTisrIiwiSW1hZ2VzIiwiTWFza2VkIGNvbnYgKyBsb2dpc3RpYyBtaXgiLCJMb2dpc3RpYyBtaXh0dXJlIE5MTCIsIlNsb3cg4oCUIE8oSMOXVykgc3RlcHMiLCJCaXRzLXBlci1kaW0gKEJQRCkiXSxbIldhdmVOZXQiLCJBdWRpbyAocmF3KSIsIkRpbGF0ZWQgY2F1c2FsIGNvbnYgc3RhY2siLCJDcm9zcy1lbnRyb3B5ICjCtS1sYXcgMjU2KSIsIlNsb3cg4oCUIE8oVCkgc3RlcHMsIFR+MTYwMDAvcyIsIkJpdHMtcGVyLWRpbSAvIE1PUyJdLFsiR1BUIC8gTE0iLCJUZXh0IHRva2VucyIsIkNhdXNhbCBUcmFuc2Zvcm1lciIsIkNyb3NzLWVudHJvcHkgbmV4dC10b2tlbiIsIn4xMOKAkzEwMCB0b2svcyAoS1YgY2FjaGUpIiwiUGVycGxleGl0eSAvIEJQRCJdLFsiSW1hZ2VHUFQiLCJQaXhlbHMgYXMgdG9rZW5zIiwiQ2F1c2FsIFRyYW5zZm9ybWVyIiwiQ3Jvc3MtZW50cm9weSBwaXhlbCB0b2tlbnMiLCJTbG93IOKAlCBPKEjDl1cpIHN0ZXBzIiwiQml0cy1wZXItZGltIChCUEQpIl0sWyJWUS1WQUUgKyBQaXhlbENOTiIsIkltYWdlcyAoMi1zdGFnZSkiLCJWUS1WQUUgZW5jb2RlciArIG1hc2tlZCBwcmlvciIsIlN0YWdlLTEgVlEgKyBTdGFnZS0yIE5MTCIsIkZhc3RlciDigJQgTyhsYXRlbnQgdG9rZW5zKSIsIkZJRCAvIFJlY29uc3RydWN0aW9uIFBTTlIiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQXV0b3JlZ3Jlc3NpdmUgbW9kZWxzIHByb3ZpZGUgZXhhY3QgbGlrZWxpaG9vZHMg4oCUIG5vIEVMQk8gYXBwcm94aW1hdGlvbiwgbm8gZGlzY3JpbWluYXRvciBpbnN0YWJpbGl0eS4iLCJUeXBlLUEgbWFza3MgZXhjbHVkZSB0aGUgY3VycmVudCBwaXhlbDsgVHlwZS1CIG1hc2tzIGluY2x1ZGUgaXQg4oCUIHN0YWNraW5nIEEgdGhlbiBCIGxheWVycyBpcyBhIHN0YW5kYXJkIFBpeGVsQ05OIHBhdHRlcm4uIiwiV2F2ZU5ldFx1MDAyN3MgZXhwb25lbnRpYWwgZGlsYXRpb24gKDEsMiw0LOKApiw1MTIpIGNvdmVycyAxMDIzIHNhbXBsZXMgcGVyIHN0YWNrOyAzIHN0YWNrcyBjb3ZlciB+MzAwMCBzYW1wbGVzLiIsIkltYWdlR1BUIGZsYXR0ZW5zIGltYWdlcyB0byBwaXhlbCBzZXF1ZW5jZXMgYW5kIHRyYWlucyBhIEdQVCwgc2hvd2luZyB0aGF0IGF1dG9yZWdyZXNzaXZlIHRyYW5zZm9ybWVycyBjYW4gZ2VuZXJhdGUgaW1hZ2VzIHdpdGhvdXQgYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzLiIsIlZRLVZBRSArIFBpeGVsQ05OIHByaW9yIGlzIHRoZSBjb25jZXB0dWFsIHByZWRlY2Vzc29yIG9mIERBTEwtRSAxLCB3aGljaCB1c2VkIGEgZGlzY3JldGUgaW1hZ2UgdG9rZW5pemVyIHdpdGggYSB0cmFuc2Zvcm1lciBwcmlvci4iLCJCaXRzLXBlci1kaW0gaXMgbG93ZXItYm91bmRlZCBieSB0aGUgdHJ1ZSBlbnRyb3B5IG9mIHRoZSBkYXRhIGRpc3RyaWJ1dGlvbiDigJQgbm8gbW9kZWwgY2FuIGJlYXQgdGhlIHRydWUgZGF0YSBlbnRyb3B5LiJdfSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdXRvcmVncmVzc2l2ZSBtb2RlbHMgcmVtYWluIGNvbXBldGl0aXZlIGZvciBsaWtlbGlob29kIGVzdGltYXRpb24gYW5kIGhhdmUgc2VlbiBhIHJlc3VyZ2VuY2Ugd2l0aCB0cmFuc2Zvcm1lciBhcmNoaXRlY3R1cmVzLiBUaGVpciBhZHZhbnRhZ2VzIOKAlCBleGFjdCBsaWtlbGlob29kLCBzdGFibGUgdHJhaW5pbmcsIG5vIG1vZGUgY29sbGFwc2Ug4oCUIG1ha2UgdGhlbSByZWxpYWJsZSBiYXNlbGluZXMuIFRoZWlyIGRpc2FkdmFudGFnZXMg4oCUIE8oTCkgc2VxdWVudGlhbCBzYW1wbGluZyBhbmQgYWJzZW5jZSBvZiBhIGNvbnRpbnVvdXMgbGF0ZW50IHNwYWNlIOKAlCBtb3RpdmF0ZSBoeWJyaWQgYXBwcm9hY2hlcyBsaWtlIFZRLVZBRSwgd2hpY2ggcmV0YWlucyB0aGUgdHJhY3RhYmxlIHByaW9yIHdoaWxlIGVuYWJsaW5nIGZhc3RlciBnZW5lcmF0aW9uIGluIGEgY29tcHJlc3NlZCBzcGFjZS4ifV0="
---
# Autoregressive Models — PixelCNN, WaveNet, and Language Models

Autoregressive models decompose the joint distribution of a high-dimensional variable x into a product of conditionals: p(x) = ∏ᵢ p(xᵢ | x₁, …, xᵢ₋₁). This factorization is exact — no approximation is introduced — and the chain rule of probability guarantees it always yields a valid probability distribution. The ordering of dimensions is a design choice: raster scan order (row by row, left to right) for images, time order for audio, and token order for text. Every element in the sequence is predicted from all previous elements, making these models Turing-complete generative models capable of capturing arbitrarily complex dependencies given sufficient capacity.

## Autoregressive Factorization

The core equation p(x) = ∏ᵢ p(xᵢ | x₁, …, xᵢ₋₁) has several critical properties. First, because it follows from the chain rule of probability, training by maximum likelihood (minimizing negative log-likelihood) is straightforward and stable — there is no adversarial objective, no reconstruction-approximation tradeoff, and no posterior collapse. Second, during training all conditionals can be computed in parallel using teacher forcing: the ground-truth prefix is fed as input and the model predicts the next element at every position simultaneously. Third, during generation samples must be drawn sequentially — each new element requires a full forward pass — making sampling O(L) in sequence length and often the primary bottleneck for long sequences.

## PixelCNN — Masked Convolutions

PixelCNN (van den Oord et al. 2016) models images autoregressively in raster scan order using masked convolutions to enforce causality. A Type-A mask zeros out the center pixel and all pixels to its right and below, ensuring p(x_i | x_{<i}) does not include x_i itself — used only in the first layer. A Type-B mask includes the center pixel, allowing the model to refine its representation of x_i from previous layers but never leaking future pixels. Stacking many gated residual blocks with Type-B masks allows the model to build deep representations while respecting the causal constraint. PixelCNN++ replaces the 256-way softmax output with a mixture of logistics, dramatically reducing the number of output parameters and improving sample quality.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MaskedConv2d(nn.Conv2d):
    """Type A: excludes center pixel (first layer). Type B: includes center (subsequent layers)."""
    def __init__(self, mask_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert mask_type in ('A', 'B')
        self.register_buffer('mask', self.weight.data.clone())
        _, _, kH, kW = self.weight.size()
        self.mask.fill_(1)
        self.mask[:, :, kH // 2, kW // 2 + (1 if mask_type == 'B' else 0):] = 0
        self.mask[:, :, kH // 2 + 1:, :] = 0

    def forward(self, x):
        self.weight.data *= self.mask
        return super().forward(x)

class GatedResBlock(nn.Module):
    def __init__(self, n_filters=64):
        super().__init__()
        self.conv = MaskedConv2d('B', n_filters, 2 * n_filters, kernel_size=3, padding=1)
        self.res_conv = nn.Conv2d(n_filters, n_filters, 1)

    def forward(self, x):
        out = self.conv(x)
        tanh_part, sig_part = out.chunk(2, dim=1)
        gated = torch.tanh(tanh_part) * torch.sigmoid(sig_part)
        return x + self.res_conv(gated)

mask_a = MaskedConv2d('A', 1, 64, kernel_size=7, padding=3)
mask_b = GatedResBlock(n_filters=64)
x = torch.randn(2, 1, 28, 28)
print('Type-A output:', mask_a(x).shape)
print('Gated ResBlock output:', mask_b(mask_a(x)).shape)
```

The causal masking property can be verified empirically: if any gradient flows from position i back to position j > i, the masking is incorrect. Type-A convolutions guarantee that the receptive field of pixel i is strictly contained in {pixel 0, …, pixel i-1}. In practice, PixelCNN models 8-bit pixel values (256 classes) at each location; PixelCNN++ models the logistic mixture directly to avoid the 256-way softmax bottleneck.

## WaveNet — Dilated Causal Convolutions

WaveNet (van den Oord et al. 2016) applies autoregressive modeling to raw audio waveforms at 16–24 kHz. The key architectural innovation is dilated causal convolutions with exponentially growing dilation rates: 1, 2, 4, 8, 16, …, 512. A single dilated convolution with dilation d has a receptive field of d+1 steps. Stacking dilation rates 1, 2, 4, …, 512 in one block covers 1024 timesteps. Multiple such stacks cover receptive fields of tens of thousands of samples. Causality is enforced by shifting the input right so that position i can only see positions ≤ i. WaveNet conditions on local features (speaker identity, mel spectrogram) by adding a conditioning signal to the gated activation at each layer.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DilatedCausalConv1d(nn.Module):
    """Causal dilated conv: pads left only so output[t] depends only on input[<=t]."""
    def __init__(self, in_ch, out_ch, kernel_size=2, dilation=1):
        super().__init__()
        self.dilation = dilation
        self.pad = (kernel_size - 1) * dilation  # left pad only for causality
        self.conv = nn.Conv1d(in_ch, out_ch, kernel_size, dilation=dilation)

    def forward(self, x):
        x = F.pad(x, (self.pad, 0))
        return self.conv(x)

class WaveNetBlock(nn.Module):
    def __init__(self, n_channels=64, dilation=1, cond_channels=None):
        super().__init__()
        self.dilated_conv = DilatedCausalConv1d(n_channels, 2 * n_channels, kernel_size=2, dilation=dilation)
        self.res_conv = nn.Conv1d(n_channels, n_channels, 1)
        self.skip_conv = nn.Conv1d(n_channels, n_channels, 1)
        self.cond_conv = nn.Conv1d(cond_channels, 2 * n_channels, 1) if cond_channels else None

    def forward(self, x, cond=None):
        h = self.dilated_conv(x)
        if cond is not None and self.cond_conv is not None:
            h = h + self.cond_conv(cond)
        tanh_h, sig_h = h.chunk(2, dim=1)
        h = torch.tanh(tanh_h) * torch.sigmoid(sig_h)
        skip = self.skip_conv(h)
        res  = self.res_conv(h) + x
        return res, skip

# Build WaveNet stack with exponential dilation rates
dilations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
blocks = nn.ModuleList([WaveNetBlock(n_channels=64, dilation=d) for d in dilations])
x = torch.randn(2, 64, 1024)  # batch=2, channels=64, T=1024
skips = []
for block in blocks:
    x, skip = block(x)
    skips.append(skip)
out = sum(skips)
print(f'Receptive field: {sum(dilations) + 1} timesteps, output shape: {out.shape}')
```

## Language Models as Autoregressive Models

GPT and its successors apply autoregressive modeling over token sequences. The vocabulary defines the discrete space (50k–100k tokens for BPE), and the model learns p(token_t | token_1, …, token_{t-1}). Transformers implement causal masking via an upper-triangular attention mask that prevents each position from attending to future positions. Unlike PixelCNN's fixed raster order, language models benefit from the natural sequential structure of text. Training on next-token prediction at scale leads to emergent capabilities: the same maximum-likelihood objective produces models that translate, summarize, reason, and generate code.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SimplePixelCNN(nn.Module):
    """Minimal PixelCNN for MNIST: train with NLL, generate sequentially."""
    def __init__(self, n_filters=64, n_layers=6):
        super().__init__()
        self.first = MaskedConv2d('A', 1, n_filters, kernel_size=7, padding=3)
        self.layers = nn.Sequential(*[GatedResBlock(n_filters) for _ in range(n_layers)])
        self.out = nn.Sequential(
            nn.Conv2d(n_filters, 256, 1),  # 256-way softmax per pixel
        )

    def forward(self, x):
        h = self.first(x.float() / 255.0 - 0.5)
        h = self.layers(h)
        return self.out(h)  # (B, 256, H, W) logits

class MaskedConv2d(nn.Conv2d):
    def __init__(self, mask_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_buffer('mask', self.weight.data.clone())
        _, _, kH, kW = self.weight.size()
        self.mask.fill_(1)
        self.mask[:, :, kH // 2, kW // 2 + (1 if mask_type == 'B' else 0):] = 0
        self.mask[:, :, kH // 2 + 1:, :] = 0
    def forward(self, x):
        self.weight.data *= self.mask
        return super().forward(x)

class GatedResBlock(nn.Module):
    def __init__(self, n_filters):
        super().__init__()
        self.conv = MaskedConv2d('B', n_filters, 2 * n_filters, kernel_size=3, padding=1)
        self.res = nn.Conv2d(n_filters, n_filters, 1)
    def forward(self, x):
        t, s = self.conv(x).chunk(2, dim=1)
        return x + self.res(torch.tanh(t) * torch.sigmoid(s))

model = SimplePixelCNN()
x_batch = torch.randint(0, 256, (4, 1, 28, 28))
logits = model(x_batch)
loss = F.cross_entropy(logits, x_batch[:, 0].long())
print(f'Logits: {logits.shape}, NLL loss: {loss.item():.4f}')
```

## Bits-per-Dim Evaluation

Autoregressive models produce exact log-likelihoods, enabling rigorous evaluation via bits-per-dim (BPD). BPD converts the negative log-likelihood (in nats, base-e) to bits, normalised by the number of dimensions (pixels or samples). It corresponds to the number of bits needed to losslessly compress each dimension on average — lower is better, and entropy of the data distribution is the theoretical minimum. BPD makes models comparable across datasets of different size and resolution. For MNIST, state-of-the-art autoregressive models achieve ~0.8 BPD; for CIFAR-10, around 2.8 BPD.

```python
import torch
import torch.nn.functional as F
import math

def compute_bits_per_dim(model, dataloader, device='cpu'):
    """
    Compute bits-per-dim: average NLL in nats / (H * W) / ln(2).
    For images: lower = better compression = better generative model.
    BPD = E[-log2 p(x)] / (H * W) = E[-log p(x)] / (H * W * log(2))
    """
    model.eval()
    total_nll = 0.0
    total_pixels = 0
    with torch.no_grad():
        for x, _ in dataloader:
            x = x.to(device)  # (B, 1, H, W) in [0, 255]
            B, C, H, W = x.shape
            logits = model(x)  # (B, 256, H, W)
            # NLL summed over all pixels in batch
            nll = F.cross_entropy(logits, x[:, 0].long(), reduction='sum')
            total_nll += nll.item()
            total_pixels += B * H * W
    avg_nll_per_pixel = total_nll / total_pixels
    bits_per_dim = avg_nll_per_pixel / math.log(2)
    return bits_per_dim

# Demonstrate conversion formula
def nll_to_bpd(nll_nats, height, width, n_samples):
    avg = nll_nats / (n_samples * height * width)
    return avg / math.log(2)

for nll, h, w, n in [(500.0, 28, 28, 1), (3200.0, 32, 32, 1)]:
    bpd = nll_to_bpd(nll, h, w, n)
    print(f'NLL={nll:.0f} nats, {h}x{w} image -> {bpd:.3f} bits/dim')

print('MNIST SOTA: ~0.8 BPD | CIFAR-10 SOTA: ~2.8 BPD | ImageNet 64x64 SOTA: ~3.4 BPD')
```

## Two-Stage: VQ-VAE + PixelCNN Prior

Pixel-space autoregressive generation over 256×256 images requires modeling 196,608 dimensions — computationally prohibitive. VQ-VAE (van den Oord et al. 2017) solves this by first compressing images into a discrete latent grid (e.g., 32×32 tokens from a codebook of 512 entries), then training an autoregressive prior (PixelCNN or Transformer) over the much shorter 32×32 = 1024 token sequence. Generation proceeds in two stages: sample the discrete latent grid autoregressively, then decode to pixels with the VQ-VAE decoder. This two-stage approach allows autoregressive models to scale to high-resolution images and is the architectural ancestor of DALL-E and modern image tokenizers.

> **Sampling Speed Bottleneck**: Autoregressive models are slow to sample because each token requires a full forward pass with no parallelism. For a 256×256 image (65,536 pixels) with a 100ms forward pass, sampling takes ~1.8 hours sequentially. Speculative decoding, caching KV states in transformers, and working in compressed latent space (VQ-VAE) are the main practical mitigations.

| Model | Modality | Architecture | Training Objective | Sampling Speed | Evaluation Metric |
| --- | --- | --- | --- | --- | --- |
| PixelCNN | Images | Masked conv stack | Cross-entropy (256-way) | Slow — O(H×W) steps | Bits-per-dim (BPD) |
| PixelCNN++ | Images | Masked conv + logistic mix | Logistic mixture NLL | Slow — O(H×W) steps | Bits-per-dim (BPD) |
| WaveNet | Audio (raw) | Dilated causal conv stack | Cross-entropy (µ-law 256) | Slow — O(T) steps, T~16000/s | Bits-per-dim / MOS |
| GPT / LM | Text tokens | Causal Transformer | Cross-entropy next-token | ~10–100 tok/s (KV cache) | Perplexity / BPD |
| ImageGPT | Pixels as tokens | Causal Transformer | Cross-entropy pixel tokens | Slow — O(H×W) steps | Bits-per-dim (BPD) |
| VQ-VAE + PixelCNN | Images (2-stage) | VQ-VAE encoder + masked prior | Stage-1 VQ + Stage-2 NLL | Faster — O(latent tokens) | FID / Reconstruction PSNR |

- Autoregressive models provide exact likelihoods — no ELBO approximation, no discriminator instability.
- Type-A masks exclude the current pixel; Type-B masks include it — stacking A then B layers is a standard PixelCNN pattern.
- WaveNet's exponential dilation (1,2,4,…,512) covers 1023 samples per stack; 3 stacks cover ~3000 samples.
- ImageGPT flattens images to pixel sequences and trains a GPT, showing that autoregressive transformers can generate images without architectural changes.
- VQ-VAE + PixelCNN prior is the conceptual predecessor of DALL-E 1, which used a discrete image tokenizer with a transformer prior.
- Bits-per-dim is lower-bounded by the true entropy of the data distribution — no model can beat the true data entropy.

---

Autoregressive models remain competitive for likelihood estimation and have seen a resurgence with transformer architectures. Their advantages — exact likelihood, stable training, no mode collapse — make them reliable baselines. Their disadvantages — O(L) sequential sampling and absence of a continuous latent space — motivate hybrid approaches like VQ-VAE, which retains the tractable prior while enabling faster generation in a compressed space.

