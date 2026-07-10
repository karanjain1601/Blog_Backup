---
title: "DenseNet — Dense Connections and Feature Reuse"
slug: "densenet-dense-connections"
description: "DenseNet (Huang et al., 2017) connects every layer to every subsequent layer within a dense block, maximising gradient flow and feature reuse. Growth rate k controls new feature maps per layer; bottleneck + compression (DenseNet-BC) reduces parameters; gradient checkpointing addresses O(n²) memory."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVuc2VOZXQgKEh1YW5nIGV0IGFsLiwgMjAxNykgdGFrZXMgdGhlIGNvbm5lY3Rpdml0eSBwYXR0ZXJuIG9mIFJlc05ldCB0byBpdHMgbG9naWNhbCBleHRyZW1lOiBpbnN0ZWFkIG9mIGNvbm5lY3RpbmcgZWFjaCBsYXllciB0byBvbmx5IHRoZSBuZXh0IGxheWVyIChwbGFpbiBuZXQpIG9yIGFkZGluZyBhIHNraXAgY29ubmVjdGlvbiBmcm9tIHRoZSBsYXllciB0d28gbGV2ZWxzIGJhY2sgKFJlc05ldCksIGV2ZXJ5IGxheWVyIHJlY2VpdmVzIGZlYXR1cmUgbWFwcyBmcm9tIGFsbCBwcmVjZWRpbmcgbGF5ZXJzIHdpdGhpbiBhIGRlbnNlIGJsb2NrLiBMYXllciBsIHJlY2VpdmVzIGNvbmNhdGVuYXRlZCBmZWF0dXJlIG1hcHMgW3jigoAsIHjigoEsIC4uLiwgeF97bC0xfV0gYXMgaW5wdXQgYW5kIHByb2R1Y2VzIGsgbmV3IGZlYXR1cmUgbWFwcyAodGhlIGdyb3d0aCByYXRlKS4gVGhpcyBkZW5zZSBjb25uZWN0aXZpdHkgbWF4aW1pc2VzIGdyYWRpZW50IGZsb3csIHByb21vdGVzIGZlYXR1cmUgcmV1c2UsIGFuZCBhY2hpZXZlcyBzdGF0ZS1vZi10aGUtYXJ0IGFjY3VyYWN5IHdpdGggc2lnbmlmaWNhbnRseSBmZXdlciBwYXJhbWV0ZXJzIHRoYW4gUmVzTmV0IOKAlCBhbGwgYXQgdGhlIGNvc3Qgb2YgaGlnaGVyIG1lbW9yeSB1c2FnZSBkdXJpbmcgdHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVuc2UgQ29ubmVjdGl2aXR5OiBFdmVyeSBMYXllciB0byBFdmVyeSBMYXllciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gYSBkZW5zZSBibG9jayB3aXRoIEwgbGF5ZXJzIGFuZCBncm93dGggcmF0ZSBrLCBsYXllciBsIGhhcyBr4oKAICsga8OXKGziiJIxKSBpbnB1dCBjaGFubmVscyAoa+KCgCA9IGluaXRpYWwgY2hhbm5lbHMgZW50ZXJpbmcgdGhlIGJsb2NrKS4gVGhlIHRvdGFsIG51bWJlciBvZiBjb25uZWN0aW9ucyB3aXRoaW4gYSBibG9jayBpcyBMKEwrMSkvMiDigJQgcXVhZHJhdGljIGluIGRlcHRoLiBGb3IgTD02LCBrPTMyLCBr4oKAPTY0OiBsYXllciAxIGhhcyA2NCBpbnB1dHMsIGxheWVyIDIgaGFzIDk2LCAuLi4sIGxheWVyIDYgaGFzIDIyNCBpbnB1dHMuIFVubGlrZSBSZXNOZXRcdTAwMjdzIHkgPSBGKHgpICsgeCAoYWRkaXRpb24pLCBEZW5zZU5ldCB1c2VzIHkgPSBIKFt44oKALCB44oKBLCAuLi4sIHhfe2wtMX1dKSAoY29uY2F0ZW5hdGlvbikuIENvbmNhdGVuYXRpb24gcHJlc2VydmVzIGFsbCBwcmlvciBmZWF0dXJlcyBleHBsaWNpdGx5IOKAlCBlYXJseSBlZGdlIGRldGVjdG9ycyByZW1haW4gZGlyZWN0bHkgYXZhaWxhYmxlIHRvIGRlZXAgbGF5ZXJzIOKAlCB3aGlsZSBSZXNOZXRcdTAwMjdzIGFkZGl0aW9uIG1peGVzIHRoZW0gaXJyZXZlcnNpYmx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBEZW5zZUxheWVyKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3U2luZ2xlIERlbnNlTmV0IGxheWVyOiBCTi1SZUxVLUNvbnYxeDEoYm90dGxlbmVjayktQk4tUmVMVS1Db252M3gzLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgZ3Jvd3RoX3JhdGU9MzIsIGJvdHRsZW5lY2s9VHJ1ZSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBtaWRfY2ggPSA0ICogZ3Jvd3RoX3JhdGUgaWYgYm90dGxlbmVjayBlbHNlIGluX2NoXG4gICAgICAgIGxheWVycyA9IFtdXG4gICAgICAgIGlmIGJvdHRsZW5lY2s6XG4gICAgICAgICAgICBsYXllcnMgKz0gW25uLkJhdGNoTm9ybTJkKGluX2NoKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgICAgICAgICAgICBubi5Db252MmQoaW5fY2gsIG1pZF9jaCwgMSwgYmlhcz1GYWxzZSldXG4gICAgICAgIGxheWVycyArPSBbbm4uQmF0Y2hOb3JtMmQobWlkX2NoKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgICAgICAgIG5uLkNvbnYyZChtaWRfY2gsIGdyb3d0aF9yYXRlLCAzLCBwYWRkaW5nPTEsIGJpYXM9RmFsc2UpXVxuICAgICAgICBzZWxmLmxheWVyID0gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiB0b3JjaC5jYXQoW3gsIHNlbGYubGF5ZXIoeCldLCBkaW09MSkgICMgY29uY2F0ZW5hdGUsIG5vdCBhZGRcblxuY2xhc3MgRGVuc2VCbG9jayhubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0RlbnNlIGJsb2NrOiBlYWNoIGxheWVyIHJlY2VpdmVzIGFsbCBwcmVjZWRpbmcgZmVhdHVyZSBtYXBzLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgbl9sYXllcnMsIGdyb3d0aF9yYXRlPTMyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGxheWVycywgY2ggPSBbXSwgaW5fY2hcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9sYXllcnMpOlxuICAgICAgICAgICAgbGF5ZXJzLmFwcGVuZChEZW5zZUxheWVyKGNoLCBncm93dGhfcmF0ZSkpXG4gICAgICAgICAgICBjaCArPSBncm93dGhfcmF0ZVxuICAgICAgICBzZWxmLmxheWVycyA9IG5uLlNlcXVlbnRpYWwoKmxheWVycylcbiAgICAgICAgc2VsZi5vdXRfY2hhbm5lbHMgPSBjaFxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6IHJldHVybiBzZWxmLmxheWVycyh4KVxuXG5ibG9jayA9IERlbnNlQmxvY2soaW5fY2g9NjQsIG5fbGF5ZXJzPTYsIGdyb3d0aF9yYXRlPTMyKVxueCA9IHRvcmNoLnJhbmRuKDIsIDY0LCA1NiwgNTYpXG5vdXQgPSBibG9jayh4KVxucGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBibG9jay5wYXJhbWV0ZXJzKCkpIC8gMWUzXG5wcmludChcdTAwMjdEZW5zZUJsb2NrIGlucHV0OiB7fSAtXHUwMDNlIG91dHB1dDoge31cdTAwMjcuZm9ybWF0KHguc2hhcGUsIG91dC5zaGFwZSkpXG5wcmludChcdTAwMjdPdXRwdXQgY2hhbm5lbHM6IDY0ICsgNiozMiA9IHt9IChjb25jYXQsIG5vdCBhZGQpXHUwMDI3LmZvcm1hdCg2NCArIDYqMzIpKVxucHJpbnQoXHUwMDI3UGFyYW1ldGVyczogezouMWZ9S1x1MDAyNy5mb3JtYXQocGFyYW1zKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcm93dGggUmF0ZSBhbmQgRmVhdHVyZSBSZXVzZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGdyb3d0aCByYXRlIGsgaXMgYSBrZXkgaHlwZXJwYXJhbWV0ZXI6IGl0IGNvbnRyb2xzIGhvdyBtYW55IG5ldyBmZWF0dXJlIG1hcHMgZWFjaCBsYXllciBjb250cmlidXRlcyB0byB0aGUgY29sbGVjdGl2ZSBrbm93bGVkZ2UuIEEgc21hbGwgayAoZS5nLiwgaz0xMiBvciBrPTMyKSBpcyBzdWZmaWNpZW50IGJlY2F1c2UgZWFjaCBsYXllciBhZGRzIHRvIGFsbCBhY2N1bXVsYXRlZCBmZWF0dXJlcyByYXRoZXIgdGhhbiBvdmVyd3JpdGluZyB0aGVtLiBEZW5zZU5ldC0xMjEgdXNlcyBrPTMyIGFuZCBhY2hpZXZlcyBjb21wYXJhYmxlIGFjY3VyYWN5IHRvIFJlc05ldC01MCB3aXRoIDhNIHZzIDI1TSBwYXJhbWV0ZXJzLiBIdWFuZyBldCBhbC4gYW5hbHlzZWQgZmlsdGVyIGFjdGl2YXRpb25zIGFuZCBmb3VuZCB0aGF0IGFsbCBsYXllcnMgd2l0aGluIGEgZGVuc2UgYmxvY2sgYWN0aXZlbHkgdXNlIGZlYXR1cmVzIGZyb20gYWxsIHByZWNlZGluZyBsYXllcnMg4oCUIGluY2x1ZGluZyB0aGUgdmVyeSBmaXJzdCBsYXllclx1MDAyN3MgZWRnZSBkZXRlY3RvcnMg4oCUIGNvbmZpcm1pbmcgZ2VudWluZSBmZWF0dXJlIHJldXNlIHJhdGhlciB0aGFuIHJlZHVuZGFudCByZWNvbXB1dGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJvdHRsZW5lY2sgYW5kIENvbXByZXNzaW9uOiBEZW5zZU5ldC1CQyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVuc2VOZXQtQiAoQm90dGxlbmVjayk6IGVhY2ggbGF5ZXIgdXNlcyBhIDHDlzEgY29udiBiZWZvcmUgdGhlIDPDlzMgdG8gcmVkdWNlIHRoZSBncm93aW5nIGlucHV0IGNoYW5uZWxzIHRvIDRrLCBwcmV2ZW50aW5nIHRoZSBwYXJhbWV0ZXIgY291bnQgZnJvbSBncm93aW5nIHF1YWRyYXRpY2FsbHkgd2l0aCBkZXB0aC4gRGVuc2VOZXQtQyAoQ29tcHJlc3Npb24pOiBiZXR3ZWVuIGRlbnNlIGJsb2NrcywgYSB0cmFuc2l0aW9uIGxheWVyIHJlZHVjZXMgY2hhbm5lbHMgYnkgYSBmYWN0b3IgzrggKHR5cGljYWxseSAwLjUpIGJlZm9yZSBkb3duc2FtcGxpbmcuIERlbnNlTmV0LUJDIGNvbWJpbmVzIGJvdGg6IERlbnNlTmV0LUJDLUwtayBkZW5vdGVzIGEgbmV0d29yayB3aXRoIEwgbGF5ZXJzIHBlciBibG9jaywgZ3Jvd3RoIHJhdGUgaywgYm90dGxlbmVja3MsIGFuZCDOuD0wLjUgY29tcHJlc3Npb24uIERlbnNlTmV0LUJDLTE5MC00MCBhY2hpZXZlcyAzLjQ2JSBlcnJvciBvbiBDSUZBUi0xMCDigJQgc3RhdGUtb2YtdGhlLWFydCBhdCB0aGUgdGltZSDigJQgd2l0aCAyNU0gcGFyYW1ldGVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgVHJhbnNpdGlvbkxheWVyKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3RGVuc2VOZXQgdHJhbnNpdGlvbjogMXgxIGNvbnYgY29tcHJlc3Npb24gKyAyeDIgYXZnIHBvb2wgZG93bnNhbXBsaW5nLlxuICAgIHRoZXRhIFx1MDAzYyAxIGNvbXByZXNzZXMgY2hhbm5lbHMgdG8gcmVkdWNlIHBhcmFtZXRlciBncm93dGggYmV0d2VlbiBibG9ja3MuXG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCB0aGV0YT0wLjUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgb3V0X2NoID0gaW50KGluX2NoICogdGhldGEpXG4gICAgICAgIHNlbGYudHJhbnNpdGlvbiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0yZChpbl9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkF2Z1Bvb2wyZCgyLCBzdHJpZGU9MikpXG4gICAgICAgIHNlbGYub3V0X2NoYW5uZWxzID0gb3V0X2NoXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYudHJhbnNpdGlvbih4KVxuXG4jIFNpbXVsYXRlIERlbnNlTmV0LTEyMSBhZnRlciBmaXJzdCBkZW5zZSBibG9jazogNjQgKyA2KjMyID0gMjU2IGNoYW5uZWxzXG5pbl9jaGFubmVscyA9IDI1NlxudHJhbnNpdGlvbiA9IFRyYW5zaXRpb25MYXllcihpbl9jaGFubmVscywgdGhldGE9MC41KVxueCA9IHRvcmNoLnJhbmRuKDIsIGluX2NoYW5uZWxzLCA1NiwgNTYpXG5vdXQgPSB0cmFuc2l0aW9uKHgpXG5wcmludChcdTAwMjdUcmFuc2l0aW9uIGlucHV0OiAge31cdTAwMjcuZm9ybWF0KHguc2hhcGUpKVxucHJpbnQoXHUwMDI3VHJhbnNpdGlvbiBvdXRwdXQ6IHt9XHUwMDI3LmZvcm1hdChvdXQuc2hhcGUpKVxucHJpbnQoXHUwMDI3Q2hhbm5lbHM6IHt9IC1cdTAwM2Uge30gICh0aGV0YT0wLjUpXHUwMDI3LmZvcm1hdChpbl9jaGFubmVscywgdHJhbnNpdGlvbi5vdXRfY2hhbm5lbHMpKVxucHJpbnQoXHUwMDI3U3BhdGlhbDogIDU2eDU2IC1cdTAwM2UgMjh4MjggICgyeDIgYXZnIHBvb2wpXHUwMDI3KVxucGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiB0cmFuc2l0aW9uLnBhcmFtZXRlcnMoKSkgLyAxZTNcbnByaW50KFx1MDAyN1BhcmFtZXRlcnM6IHs6LjFmfUtcdTAwMjcuZm9ybWF0KHBhcmFtcykpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJNZW1vcnkgQ29zdCBpcyBPKG7CsikgV2l0aG91dCBPcHRpbWlzYXRpb24iLCJjb250ZW50IjoiQSBuYWl2ZSBEZW5zZU5ldCBpbXBsZW1lbnRhdGlvbiBhbGxvY2F0ZXMgc2VwYXJhdGUgdGVuc29ycyBmb3IgYWxsIEwoTCsxKS8yIGludGVybWVkaWF0ZSBmZWF0dXJlIG1hcHMgYW5kIGtlZXBzIHRoZW0gaW4gR1BVIG1lbW9yeSBmb3IgdGhlIGJhY2t3YXJkIHBhc3MuIEZvciBEZW5zZU5ldC0yNjQgd2l0aCBMPTY0IGxheWVycyBwZXIgYmxvY2ssIHRoaXMgaXMgNjTDlzY1LzIgPSAyLDA4MCB0ZW5zb3IgYWxsb2NhdGlvbnMgcGVyIGJsb2NrLiBUaGUgUHlUb3JjaCBEZW5zZU5ldCBpbXBsZW1lbnRhdGlvbiB1c2VzIGEgc2hhcmVkIG1lbW9yeSBhbGxvY2F0aW9uIHRyaWNrOiBhbGwgaW5wdXQgY29uY2F0ZW5hdGlvbnMgcmVmZXJlbmNlIHRoZSBzYW1lIHByZS1hbGxvY2F0ZWQgbWVtb3J5IGJ1ZmZlciwgcmVkdWNpbmcgcGVhayBtZW1vcnkgZnJvbSBPKG7CsikgdG8gbmVhciBPKG4pLiBHcmFkaWVudCBjaGVja3BvaW50aW5nICh0b3JjaC51dGlscy5jaGVja3BvaW50KSBwcm92aWRlcyBhbiBhbHRlcm5hdGl2ZTogcmVjb21wdXRlIGFjdGl2YXRpb25zIGR1cmluZyB0aGUgYmFja3dhcmQgcGFzcyByYXRoZXIgdGhhbiBzdG9yaW5nIHRoZW0uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVtb3J5LUVmZmljaWVudCBJbXBsZW1lbnRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR3JhZGllbnQgY2hlY2twb2ludGluZyB0cmFkZXMgY29tcHV0ZSBmb3IgbWVtb3J5OiBpbnN0ZWFkIG9mIHN0b3JpbmcgaW50ZXJtZWRpYXRlIGFjdGl2YXRpb25zIGZvciB0aGUgYmFja3dhcmQgcGFzcywgdGhleSBhcmUgcmVjb21wdXRlZCBvbiB0aGUgZmx5IGR1cmluZyBiYWNrcHJvcGFnYXRpb24uIEZvciBEZW5zZU5ldCwgd2hlcmUgZWFjaCBsYXllclx1MDAyN3MgaW5wdXQgaXMgdGhlIGNvbmNhdGVuYXRpb24gb2YgYWxsIHByaW9yIG91dHB1dHMsIGNoZWNrcG9pbnRpbmcgdGhlIGNvbmNhdGVuYXRpb24gb3BlcmF0aW9uIGlzIGVzcGVjaWFsbHkgZWZmZWN0aXZlLiB0b3JjaC51dGlscy5jaGVja3BvaW50LmNoZWNrcG9pbnQgd3JhcHMgYSBmdW5jdGlvbiBhbmQgZGlzY2FyZHMgaXRzIGludGVybWVkaWF0ZSBhY3RpdmF0aW9ucywgcmVjb21wdXRpbmcgdGhlbSBkdXJpbmcgdGhlIGJhY2t3YXJkIHBhc3MuIFRoaXMgdHlwaWNhbGx5IGRvdWJsZXMgdHJhaW5pbmcgdGltZSAoc2luY2UgYWN0aXZhdGlvbnMgYXJlIGNvbXB1dGVkIHR3aWNlKSBidXQgcmVkdWNlcyBtZW1vcnkgYnkgdXAgdG8gMTDDlyBmb3IgZGVlcCBEZW5zZU5ldHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLnV0aWxzLmNoZWNrcG9pbnQgaW1wb3J0IGNoZWNrcG9pbnRcblxuY2xhc3MgQ2hlY2twb2ludGVkRGVuc2VMYXllcihubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0RlbnNlTmV0IGxheWVyIHVzaW5nIGdyYWRpZW50IGNoZWNrcG9pbnRpbmcgdG8gdHJhZGUgbWVtb3J5IGZvciBjb21wdXRlLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgZ3Jvd3RoX3JhdGU9MzIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgbWlkX2NoID0gNCAqIGdyb3d0aF9yYXRlXG4gICAgICAgIHNlbGYuYm4xICAgPSBubi5CYXRjaE5vcm0yZChpbl9jaClcbiAgICAgICAgc2VsZi5jb252MSA9IG5uLkNvbnYyZChpbl9jaCwgbWlkX2NoLCAxLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmJuMiAgID0gbm4uQmF0Y2hOb3JtMmQobWlkX2NoKVxuICAgICAgICBzZWxmLmNvbnYyID0gbm4uQ29udjJkKG1pZF9jaCwgZ3Jvd3RoX3JhdGUsIDMsIHBhZGRpbmc9MSwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5yZWx1ICA9IG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuXG4gICAgZGVmIF9mb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBvdXQgPSBzZWxmLmNvbnYxKHNlbGYucmVsdShzZWxmLmJuMSh4KSkpXG4gICAgICAgIHJldHVybiBzZWxmLmNvbnYyKHNlbGYucmVsdShzZWxmLmJuMihvdXQpKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBuZXdfZmVhdCA9IGNoZWNrcG9pbnQoc2VsZi5fZm9yd2FyZCwgeCwgdXNlX3JlZW50cmFudD1GYWxzZSlcbiAgICAgICAgcmV0dXJuIHRvcmNoLmNhdChbeCwgbmV3X2ZlYXRdLCBkaW09MSlcblxuY2xhc3MgTWVtRWZmaWNpZW50RGVuc2VCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgbl9sYXllcnMsIGdyb3d0aF9yYXRlPTMyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubGF5ZXJzID0gbm4uTW9kdWxlTGlzdCgpXG4gICAgICAgIGNoID0gaW5fY2hcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9sYXllcnMpOlxuICAgICAgICAgICAgc2VsZi5sYXllcnMuYXBwZW5kKENoZWNrcG9pbnRlZERlbnNlTGF5ZXIoY2gsIGdyb3d0aF9yYXRlKSlcbiAgICAgICAgICAgIGNoICs9IGdyb3d0aF9yYXRlXG4gICAgICAgIHNlbGYub3V0X2NoYW5uZWxzID0gY2hcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBmb3IgbGF5ZXIgaW4gc2VsZi5sYXllcnM6XG4gICAgICAgICAgICB4ID0gbGF5ZXIoeClcbiAgICAgICAgcmV0dXJuIHhcblxuYmxvY2sgPSBNZW1FZmZpY2llbnREZW5zZUJsb2NrKGluX2NoPTY0LCBuX2xheWVycz0xMiwgZ3Jvd3RoX3JhdGU9MzIpXG54ID0gdG9yY2gucmFuZG4oMiwgNjQsIDI4LCAyOClcbm91dCA9IGJsb2NrKHgpXG5wcmludChcdTAwMjdDaGVja3BvaW50ZWQgRGVuc2VCbG9jazoge30gLVx1MDAzZSB7fVx1MDAyNy5mb3JtYXQoeC5zaGFwZSwgb3V0LnNoYXBlKSlcbnByaW50KFx1MDAyN091dHB1dCBjaGFubmVsczogNjQgKyAxMiozMiA9IHt9XHUwMDI3LmZvcm1hdCg2NCArIDEyKjMyKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGZWF0dXJlIFJldXNlIFZpc3VhbGlzYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikh1YW5nIGV0IGFsLiB2aXN1YWxpc2VkIHdoaWNoIHNvdXJjZSBmZWF0dXJlcyBlYWNoIGxheWVyIGFjdHVhbGx5IHVzZXMgYnkgYW5hbHlzaW5nIHRoZSBhYnNvbHV0ZSB3ZWlnaHQgbWFnbml0dWRlcyBpbiB0aGUgMcOXMSBib3R0bGVuZWNrIGNvbnZvbHV0aW9ucy4gSWYgbGF5ZXIgbCBhbGxvY2F0ZXMgaGlnaCB3ZWlnaHQgdG8gZmVhdHVyZXMgZnJvbSBsYXllciBqLCBpdCBnZW51aW5lbHkgcmV1c2VzIHRoZW0uIFRoZSBhbmFseXNpcyByZXZlYWxlZCB0aGF0IGFsbCBzb3VyY2UgbGF5ZXJzIGNvbnRyaWJ1dGUgbm9uLXRyaXZpYWxseSDigJQgaW5jbHVkaW5nIHRoZSB2ZXJ5IGZpcnN0IGxheWVyXHUwMDI3cyBsb3ctbGV2ZWwgZmVhdHVyZXMgYXQgZGVlcCBsYXllcnMuIFRoaXMgaXMgaW4gY29udHJhc3QgdG8gUmVzTmV0cyB3aGVyZSBlYXJseSBmZWF0dXJlcyBhcmUgZWZmZWN0aXZlbHkgZm9yZ290dGVuIChvdmVyd3JpdHRlbiBieSBhZGRpdGlvbikgYXMgdGhlIG5ldHdvcmsgZGVlcGVucy4gRGVuc2VOZXRcdTAwMjdzIGZlYXR1cmUgcmV1c2UgcGF0dGVybiBpcyBsaWtlIGEgY29tbWl0dGVlOiBldmVyeSBtZW1iZXIgKGxheWVyKSBhbHdheXMgaGFzIGFjY2VzcyB0byBhbGwgcHJpb3IgZXZpZGVuY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuY2xhc3MgQW5hbHlzaXNEZW5zZUxheWVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBncm93dGhfcmF0ZT0zMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBtaWRfY2ggPSA0ICogZ3Jvd3RoX3JhdGVcbiAgICAgICAgc2VsZi5ibjEgICA9IG5uLkJhdGNoTm9ybTJkKGluX2NoKVxuICAgICAgICBzZWxmLmNvbnYxID0gbm4uQ29udjJkKGluX2NoLCBtaWRfY2gsIDEsIGJpYXM9RmFsc2UpICAjIHdlaWdodHMgdG8gYW5hbHlzZVxuICAgICAgICBzZWxmLmJuMiAgID0gbm4uQmF0Y2hOb3JtMmQobWlkX2NoKVxuICAgICAgICBzZWxmLmNvbnYyID0gbm4uQ29udjJkKG1pZF9jaCwgZ3Jvd3RoX3JhdGUsIDMsIHBhZGRpbmc9MSwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5yZWx1ICA9IG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBvdXQgPSBzZWxmLmNvbnYxKHNlbGYucmVsdShzZWxmLmJuMSh4KSkpXG4gICAgICAgIHJldHVybiB0b3JjaC5jYXQoW3gsIHNlbGYuY29udjIoc2VsZi5yZWx1KHNlbGYuYm4yKG91dCkpKV0sIGRpbT0xKVxuXG5uX2xheWVycywgaywgaW5fY2ggPSA2LCAzMiwgNjRcbmxheWVycyA9IFtBbmFseXNpc0RlbnNlTGF5ZXIoaW5fY2ggKyBpKmssIGspIGZvciBpIGluIHJhbmdlKG5fbGF5ZXJzKV1cbiMgQ29tcHV0ZSBtZWFuIGFic29sdXRlIHdlaWdodCBwZXIgc291cmNlIGZlYXR1cmUgYmxvY2sgaW4gY29udjFcbnByaW50KFx1MDAyN0ZlYXR1cmUgcmV1c2UgbWF0cml4IChyb3dzPWxheWVyLCBjb2xzPXNvdXJjZSBjb250cmlidXRpb24pOlx1MDAyNylcbnByaW50KFx1MDAyN3s6XHUwMDNjMTB9IFx1MDAyNy5mb3JtYXQoXHUwMDI3TGF5ZXJcdTAwMjcpICsgXHUwMDI3ICBcdTAwMjcuam9pbihcdTAwMjdzcmN7fVx1MDAyNy5mb3JtYXQoaSkgZm9yIGkgaW4gcmFuZ2Uobl9sYXllcnMrMSkpKVxuZm9yIGxfaWR4LCBsYXllciBpbiBlbnVtZXJhdGUobGF5ZXJzKTpcbiAgICB3ID0gbGF5ZXIuY29udjEud2VpZ2h0LmRhdGEuYWJzKCkgICAjIHNoYXBlOiAoNGssIGluX2NoICsgbF9pZHgqaywgMSwgMSlcbiAgICBjaF9wdHIsIGNvbnRyaWJzID0gMCwgW11cbiAgICBmb3Igc3JjIGluIHJhbmdlKGxfaWR4ICsgMSk6XG4gICAgICAgIHNyY19jaCA9IGluX2NoIGlmIHNyYyA9PSAwIGVsc2Uga1xuICAgICAgICBjb250cmlicy5hcHBlbmQod1s6LCBjaF9wdHI6Y2hfcHRyK3NyY19jaF0ubWVhbigpLml0ZW0oKSlcbiAgICAgICAgY2hfcHRyICs9IHNyY19jaFxuICAgIHJvdyA9IFx1MDAyNyAgXHUwMDI3LmpvaW4oXHUwMDI3ezouM2Z9XHUwMDI3LmZvcm1hdChjKSBmb3IgYyBpbiBjb250cmlicylcbiAgICBwcmludChcdTAwMjdMYXllciB7Olx1MDAzZTJ9OiAge31cdTAwMjcuZm9ybWF0KGxfaWR4KzEsIHJvdykpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IERlbnNlIENvbm5lY3Rpb25zIFdvcmsifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlbnNlIGNvbm5lY3Rpdml0eSBwcm92aWRlcyBzZXZlcmFsIG9ydGhvZ29uYWwgYmVuZWZpdHM6ICgxKSBpbXBsaWNpdCBkZWVwIHN1cGVydmlzaW9uIOKAlCBldmVyeSBsYXllciByZWNlaXZlcyBncmFkaWVudCBmcm9tIHRoZSBsb3NzIHRocm91Z2ggbXVsdGlwbGUgcGF0aHMgb2YgdmFyeWluZyBsZW5ndGhzLCBzaW1pbGFyIHRvIGF1eGlsaWFyeSBjbGFzc2lmaWVycyBidXQgd2l0aG91dCBleHRyYSBwYXJhbWV0ZXJzOyAoMikgZmVhdHVyZSByZXVzZSDigJQgZWFybGllciBsYXllcnNcdTAwMjcgZmlsdGVycyByZW1haW4gYWNjZXNzaWJsZSB0aHJvdWdob3V0LCBzbyB0aGUgbmV0d29yayBkb2VzIG5vdCBuZWVkIHRvIHJlbGVhcm4gbG93LWxldmVsIGZlYXR1cmVzOyAoMykgcmVndWxhcmlzYXRpb24g4oCUIHRoZSBzaGFyZWQgZmVhdHVyZSBtYXAgcG9vbCBhY3RzIGFzIGEgZm9ybSBvZiBkcm9wb3V0IGluIGZlYXR1cmUgc3BhY2UsIGZvcmNpbmcgbGF5ZXJzIHRvIGJlIGNvbXBsZW1lbnRhcnkgcmF0aGVyIHRoYW4gcmVkdW5kYW50OyAoNCkgcGFyYW1ldGVyIGVmZmljaWVuY3kg4oCUIGsgbmV3IGZlYXR1cmVzIHBlciBsYXllciBzdWZmaWNlcyBiZWNhdXNlIGVhY2ggbGF5ZXIgYnVpbGRzIG9uIGFsbCBhY2N1bXVsYXRlZCBjb250ZXh0IHJhdGhlciB0aGFuIHN0YXJ0aW5nIGZyb20gc2NyYXRjaC4gRGVuc2VOZXQgYWNoaWV2ZXMgUmVzTmV0LWxldmVsIGFjY3VyYWN5IHdpdGggM8OXIGZld2VyIHBhcmFtZXRlcnMgb24gSW1hZ2VOZXQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJJbXBsaWNpdCBkZWVwIHN1cGVydmlzaW9uOiBncmFkaWVudHMgcmVhY2ggZWFybHkgbGF5ZXJzIHRocm91Z2ggTyhMKSBkaXJlY3QgcGF0aHMgcmF0aGVyIHRoYW4gdGhlIHNpbmdsZSBjaGFpbmVkIHBhdGggaW4gcGxhaW4gbmV0d29ya3MuIiwiRmVhdHVyZSByZXVzZTogZWRnZSBkZXRlY3RvcnMgbGVhcm5lZCBpbiBsYXllciAxIGFyZSBkaXJlY3RseSBhdmFpbGFibGUgdG8gbGF5ZXIgTCB3aXRob3V0IGJlaW5nIGRpbHV0ZWQgYnkgcmVwZWF0ZWQgYWRkaXRpb24uIiwiQ29tcGxlbWVudGFyeSBmaWx0ZXJzOiBlYWNoIGxheWVyIGFkZHMgZXhhY3RseSBrIG5ldyBmZWF0dXJlIG1hcHMsIGluY2VudGl2aXNpbmcgaXQgdG8gbGVhcm4gZmVhdHVyZXMgZGlzdGluY3QgZnJvbSBhbGwgcHJpb3IgbGF5ZXJzLiIsIkNvbGxlY3RpdmUga25vd2xlZGdlOiB0aGUgY29uY2F0ZW5hdGVkIGZlYXR1cmUgbWFwIGlzIGEgc2hhcmVkLCBldmVyLWdyb3dpbmcgcmVwcmVzZW50YXRpb24g4oCUIGFuYWxvZ291cyB0byBhbiBlbnNlbWJsZVx1MDAyN3MgcHJlZGljdGlvbiBwb29sLiIsIkNvbm5lY3Rpb24gdG8gRlBOOiBkZW5zZSBibG9ja3MgYXJlIGEgZm9ybSBvZiBhbGwtdG8tYWxsIGZlYXR1cmUgcHlyYW1pZCwgd2hlcmVhcyBGUE4gYnVpbGRzIGEgdG9wLWRvd24gcHlyYW1pZCBvZiBmaXhlZCByZXNvbHV0aW9uIGxldmVscy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVuc2VOZXQgdnMgUmVzTmV0IHZzIFBsYWluTmV0In0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiUGxhaW5OZXQiLCJSZXNOZXQiLCJEZW5zZU5ldCJdLCJyb3dzIjpbWyJDb25uZWN0aW9uIHR5cGUiLCJTZXF1ZW50aWFsLCBsYXllciB0byBuZXh0IiwiU2tpcDogYWRkIHggdG8gRih4KSIsIkRlbnNlOiBjb25jYXQgYWxsIHByaW9yIHRvIGVhY2giXSxbIkZlYXR1cmUgcmV1c2UiLCJOb25lIOKAlCBvdmVyd3JpdHRlbiBlYWNoIGxheWVyIiwiUGFydGlhbCDigJQgYWRkaXRpb24gbWl4ZXMgZmVhdHVyZXMiLCJGdWxsIOKAlCBhbGwgcHJpb3IgZmVhdHVyZXMgYWx3YXlzIGF2YWlsYWJsZSJdLFsiR3JhZGllbnQgcGF0aHMiLCIxIHBhdGggcGVyIGxheWVyIiwiMiBwYXRocyBwZXIgYmxvY2sgKG1haW4gKyBza2lwKSIsIk8oTCkgcGF0aHMgcGVyIGxheWVyIl0sWyJQYXJhbWV0ZXJzIiwiSGlnaCAocmVkdW5kYW50IHJlbGVhcm5pbmcpIiwiTWVkaXVtIiwiTG93IChrIHBlciBsYXllciBzdWZmaWNlcykiXSxbIk1lbW9yeSAodHJhaW5pbmcpIiwiTyhMKSIsIk8oTCkiLCJPKEzCsikgbmFpdmU7IE8oTCkgd2l0aCBzaGFyZWQgYWxsb2MiXSxbIkRlcHRoIHNjYWxhYmlsaXR5IiwiUG9vciAodmFuaXNoaW5nIGdyYWRpZW50cykiLCJFeGNlbGxlbnQgKDEwMDArIGxheWVycykiLCJHb29kIChodW5kcmVkcyBvZiBsYXllcnMgcHJhY3RpY2FsKSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZW5zZU5ldCBpcyBtb3N0IGVmZmVjdGl2ZSB3aGVuIHBhcmFtZXRlciBlZmZpY2llbmN5IG1hdHRlcnMgbW9yZSB0aGFuIGluZmVyZW5jZSBzcGVlZDogaXRzIGRlbnNlIGNvbm5lY3Rpb25zIGNyZWF0ZSBtYW55IHNtYWxsIHRlbnNvcnMgdGhhdCBhcmUgY2FjaGUtdW5mcmllbmRseSBvbiBHUFUsIG1ha2luZyBpdCBzbG93ZXIgYXQgaW5mZXJlbmNlIHRoYW4gUmVzTmV0IGF0IGVxdWFsIGFjY3VyYWN5LiBGb3IgZGVwbG95bWVudC1jb25zdHJhaW5lZCBzY2VuYXJpb3MsIE1vYmlsZU5ldCAoZGVwdGh3aXNlIHNlcGFyYWJsZSArIGludmVydGVkIHJlc2lkdWFscykgYW5kIEVmZmljaWVudE5ldCAoY29tcG91bmQgc2NhbGluZykgdHlwaWNhbGx5IGRvbWluYXRlLiBEZW5zZU5ldCByZW1haW5zIHRoZSBhcmNoaXRlY3R1cmUgb2YgY2hvaWNlIGZvciBtZWRpY2FsIGltYWdlIHNlZ21lbnRhdGlvbiAoYXMgdGhlIGVuY29kZXIgaW4gVS1OZXQgdmFyaWFudHMpIGFuZCB0YXNrcyB3aGVyZSBpbnRlcm1lZGlhdGUgZmVhdHVyZSByZXVzZSBpcyBjcml0aWNhbC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# DenseNet — Dense Connections and Feature Reuse

DenseNet (Huang et al., 2017) takes the connectivity pattern of ResNet to its logical extreme: instead of connecting each layer to only the next layer (plain net) or adding a skip connection from the layer two levels back (ResNet), every layer receives feature maps from all preceding layers within a dense block. Layer l receives concatenated feature maps [x₀, x₁, ..., x_{l-1}] as input and produces k new feature maps (the growth rate). This dense connectivity maximises gradient flow, promotes feature reuse, and achieves state-of-the-art accuracy with significantly fewer parameters than ResNet — all at the cost of higher memory usage during training.

## Dense Connectivity: Every Layer to Every Layer

In a dense block with L layers and growth rate k, layer l has k₀ + k×(l−1) input channels (k₀ = initial channels entering the block). The total number of connections within a block is L(L+1)/2 — quadratic in depth. For L=6, k=32, k₀=64: layer 1 has 64 inputs, layer 2 has 96, ..., layer 6 has 224 inputs. Unlike ResNet's y = F(x) + x (addition), DenseNet uses y = H([x₀, x₁, ..., x_{l-1}]) (concatenation). Concatenation preserves all prior features explicitly — early edge detectors remain directly available to deep layers — while ResNet's addition mixes them irreversibly.

```python
import torch
import torch.nn as nn

class DenseLayer(nn.Module):
    '''Single DenseNet layer: BN-ReLU-Conv1x1(bottleneck)-BN-ReLU-Conv3x3.'''
    def __init__(self, in_ch, growth_rate=32, bottleneck=True):
        super().__init__()
        mid_ch = 4 * growth_rate if bottleneck else in_ch
        layers = []
        if bottleneck:
            layers += [nn.BatchNorm2d(in_ch), nn.ReLU(inplace=True),
                       nn.Conv2d(in_ch, mid_ch, 1, bias=False)]
        layers += [nn.BatchNorm2d(mid_ch), nn.ReLU(inplace=True),
                   nn.Conv2d(mid_ch, growth_rate, 3, padding=1, bias=False)]
        self.layer = nn.Sequential(*layers)

    def forward(self, x):
        return torch.cat([x, self.layer(x)], dim=1)  # concatenate, not add

class DenseBlock(nn.Module):
    '''Dense block: each layer receives all preceding feature maps.'''
    def __init__(self, in_ch, n_layers, growth_rate=32):
        super().__init__()
        layers, ch = [], in_ch
        for _ in range(n_layers):
            layers.append(DenseLayer(ch, growth_rate))
            ch += growth_rate
        self.layers = nn.Sequential(*layers)
        self.out_channels = ch

    def forward(self, x): return self.layers(x)

block = DenseBlock(in_ch=64, n_layers=6, growth_rate=32)
x = torch.randn(2, 64, 56, 56)
out = block(x)
params = sum(p.numel() for p in block.parameters()) / 1e3
print('DenseBlock input: {} -> output: {}'.format(x.shape, out.shape))
print('Output channels: 64 + 6*32 = {} (concat, not add)'.format(64 + 6*32))
print('Parameters: {:.1f}K'.format(params))
```

## Growth Rate and Feature Reuse

The growth rate k is a key hyperparameter: it controls how many new feature maps each layer contributes to the collective knowledge. A small k (e.g., k=12 or k=32) is sufficient because each layer adds to all accumulated features rather than overwriting them. DenseNet-121 uses k=32 and achieves comparable accuracy to ResNet-50 with 8M vs 25M parameters. Huang et al. analysed filter activations and found that all layers within a dense block actively use features from all preceding layers — including the very first layer's edge detectors — confirming genuine feature reuse rather than redundant recomputation.

## Bottleneck and Compression: DenseNet-BC

DenseNet-B (Bottleneck): each layer uses a 1×1 conv before the 3×3 to reduce the growing input channels to 4k, preventing the parameter count from growing quadratically with depth. DenseNet-C (Compression): between dense blocks, a transition layer reduces channels by a factor θ (typically 0.5) before downsampling. DenseNet-BC combines both: DenseNet-BC-L-k denotes a network with L layers per block, growth rate k, bottlenecks, and θ=0.5 compression. DenseNet-BC-190-40 achieves 3.46% error on CIFAR-10 — state-of-the-art at the time — with 25M parameters.

```python
import torch
import torch.nn as nn

class TransitionLayer(nn.Module):
    '''DenseNet transition: 1x1 conv compression + 2x2 avg pool downsampling.
    theta < 1 compresses channels to reduce parameter growth between blocks.
    '''
    def __init__(self, in_ch, theta=0.5):
        super().__init__()
        out_ch = int(in_ch * theta)
        self.transition = nn.Sequential(
            nn.BatchNorm2d(in_ch), nn.ReLU(inplace=True),
            nn.Conv2d(in_ch, out_ch, 1, bias=False),
            nn.AvgPool2d(2, stride=2))
        self.out_channels = out_ch

    def forward(self, x): return self.transition(x)

# Simulate DenseNet-121 after first dense block: 64 + 6*32 = 256 channels
in_channels = 256
transition = TransitionLayer(in_channels, theta=0.5)
x = torch.randn(2, in_channels, 56, 56)
out = transition(x)
print('Transition input:  {}'.format(x.shape))
print('Transition output: {}'.format(out.shape))
print('Channels: {} -> {}  (theta=0.5)'.format(in_channels, transition.out_channels))
print('Spatial:  56x56 -> 28x28  (2x2 avg pool)')
params = sum(p.numel() for p in transition.parameters()) / 1e3
print('Parameters: {:.1f}K'.format(params))
```

> **Memory Cost is O(n²) Without Optimisation**: A naive DenseNet implementation allocates separate tensors for all L(L+1)/2 intermediate feature maps and keeps them in GPU memory for the backward pass. For DenseNet-264 with L=64 layers per block, this is 64×65/2 = 2,080 tensor allocations per block. The PyTorch DenseNet implementation uses a shared memory allocation trick: all input concatenations reference the same pre-allocated memory buffer, reducing peak memory from O(n²) to near O(n). Gradient checkpointing (torch.utils.checkpoint) provides an alternative: recompute activations during the backward pass rather than storing them.

## Memory-Efficient Implementation

Gradient checkpointing trades compute for memory: instead of storing intermediate activations for the backward pass, they are recomputed on the fly during backpropagation. For DenseNet, where each layer's input is the concatenation of all prior outputs, checkpointing the concatenation operation is especially effective. torch.utils.checkpoint.checkpoint wraps a function and discards its intermediate activations, recomputing them during the backward pass. This typically doubles training time (since activations are computed twice) but reduces memory by up to 10× for deep DenseNets.

```python
import torch
import torch.nn as nn
from torch.utils.checkpoint import checkpoint

class CheckpointedDenseLayer(nn.Module):
    '''DenseNet layer using gradient checkpointing to trade memory for compute.'''
    def __init__(self, in_ch, growth_rate=32):
        super().__init__()
        mid_ch = 4 * growth_rate
        self.bn1   = nn.BatchNorm2d(in_ch)
        self.conv1 = nn.Conv2d(in_ch, mid_ch, 1, bias=False)
        self.bn2   = nn.BatchNorm2d(mid_ch)
        self.conv2 = nn.Conv2d(mid_ch, growth_rate, 3, padding=1, bias=False)
        self.relu  = nn.ReLU(inplace=True)

    def _forward(self, x):
        out = self.conv1(self.relu(self.bn1(x)))
        return self.conv2(self.relu(self.bn2(out)))

    def forward(self, x):
        new_feat = checkpoint(self._forward, x, use_reentrant=False)
        return torch.cat([x, new_feat], dim=1)

class MemEfficientDenseBlock(nn.Module):
    def __init__(self, in_ch, n_layers, growth_rate=32):
        super().__init__()
        self.layers = nn.ModuleList()
        ch = in_ch
        for _ in range(n_layers):
            self.layers.append(CheckpointedDenseLayer(ch, growth_rate))
            ch += growth_rate
        self.out_channels = ch

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

block = MemEfficientDenseBlock(in_ch=64, n_layers=12, growth_rate=32)
x = torch.randn(2, 64, 28, 28)
out = block(x)
print('Checkpointed DenseBlock: {} -> {}'.format(x.shape, out.shape))
print('Output channels: 64 + 12*32 = {}'.format(64 + 12*32))
```

## Feature Reuse Visualisation

Huang et al. visualised which source features each layer actually uses by analysing the absolute weight magnitudes in the 1×1 bottleneck convolutions. If layer l allocates high weight to features from layer j, it genuinely reuses them. The analysis revealed that all source layers contribute non-trivially — including the very first layer's low-level features at deep layers. This is in contrast to ResNets where early features are effectively forgotten (overwritten by addition) as the network deepens. DenseNet's feature reuse pattern is like a committee: every member (layer) always has access to all prior evidence.

```python
import torch
import torch.nn as nn
import numpy as np

class AnalysisDenseLayer(nn.Module):
    def __init__(self, in_ch, growth_rate=32):
        super().__init__()
        mid_ch = 4 * growth_rate
        self.bn1   = nn.BatchNorm2d(in_ch)
        self.conv1 = nn.Conv2d(in_ch, mid_ch, 1, bias=False)  # weights to analyse
        self.bn2   = nn.BatchNorm2d(mid_ch)
        self.conv2 = nn.Conv2d(mid_ch, growth_rate, 3, padding=1, bias=False)
        self.relu  = nn.ReLU(inplace=True)
    def forward(self, x):
        out = self.conv1(self.relu(self.bn1(x)))
        return torch.cat([x, self.conv2(self.relu(self.bn2(out)))], dim=1)

n_layers, k, in_ch = 6, 32, 64
layers = [AnalysisDenseLayer(in_ch + i*k, k) for i in range(n_layers)]
# Compute mean absolute weight per source feature block in conv1
print('Feature reuse matrix (rows=layer, cols=source contribution):')
print('{:<10} '.format('Layer') + '  '.join('src{}'.format(i) for i in range(n_layers+1)))
for l_idx, layer in enumerate(layers):
    w = layer.conv1.weight.data.abs()   # shape: (4k, in_ch + l_idx*k, 1, 1)
    ch_ptr, contribs = 0, []
    for src in range(l_idx + 1):
        src_ch = in_ch if src == 0 else k
        contribs.append(w[:, ch_ptr:ch_ptr+src_ch].mean().item())
        ch_ptr += src_ch
    row = '  '.join('{:.3f}'.format(c) for c in contribs)
    print('Layer {:>2}:  {}'.format(l_idx+1, row))
```

## Why Dense Connections Work

Dense connectivity provides several orthogonal benefits: (1) implicit deep supervision — every layer receives gradient from the loss through multiple paths of varying lengths, similar to auxiliary classifiers but without extra parameters; (2) feature reuse — earlier layers' filters remain accessible throughout, so the network does not need to relearn low-level features; (3) regularisation — the shared feature map pool acts as a form of dropout in feature space, forcing layers to be complementary rather than redundant; (4) parameter efficiency — k new features per layer suffices because each layer builds on all accumulated context rather than starting from scratch. DenseNet achieves ResNet-level accuracy with 3× fewer parameters on ImageNet.

- Implicit deep supervision: gradients reach early layers through O(L) direct paths rather than the single chained path in plain networks.
- Feature reuse: edge detectors learned in layer 1 are directly available to layer L without being diluted by repeated addition.
- Complementary filters: each layer adds exactly k new feature maps, incentivising it to learn features distinct from all prior layers.
- Collective knowledge: the concatenated feature map is a shared, ever-growing representation — analogous to an ensemble's prediction pool.
- Connection to FPN: dense blocks are a form of all-to-all feature pyramid, whereas FPN builds a top-down pyramid of fixed resolution levels.

## DenseNet vs ResNet vs PlainNet

| Property | PlainNet | ResNet | DenseNet |
| --- | --- | --- | --- |
| Connection type | Sequential, layer to next | Skip: add x to F(x) | Dense: concat all prior to each |
| Feature reuse | None — overwritten each layer | Partial — addition mixes features | Full — all prior features always available |
| Gradient paths | 1 path per layer | 2 paths per block (main + skip) | O(L) paths per layer |
| Parameters | High (redundant relearning) | Medium | Low (k per layer suffices) |
| Memory (training) | O(L) | O(L) | O(L²) naive; O(L) with shared alloc |
| Depth scalability | Poor (vanishing gradients) | Excellent (1000+ layers) | Good (hundreds of layers practical) |

DenseNet is most effective when parameter efficiency matters more than inference speed: its dense connections create many small tensors that are cache-unfriendly on GPU, making it slower at inference than ResNet at equal accuracy. For deployment-constrained scenarios, MobileNet (depthwise separable + inverted residuals) and EfficientNet (compound scaling) typically dominate. DenseNet remains the architecture of choice for medical image segmentation (as the encoder in U-Net variants) and tasks where intermediate feature reuse is critical.

---

