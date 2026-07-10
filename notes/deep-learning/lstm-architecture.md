---
title: "LSTM — Forget Gate, Input Gate, Output Gate, and Cell State"
slug: "lstm-architecture"
description: "Derive all four LSTM gates from scratch, implement stateful PyTorch nn.LSTM, benchmark on the adding problem, visualise gate activations, and compare parameter count with GRU and vanilla RNN."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIExvbmcgU2hvcnQtVGVybSBNZW1vcnkgKExTVE0pIG5ldHdvcmsgd2FzIGludHJvZHVjZWQgYnkgSG9jaHJlaXRlciBhbmQgU2NobWlkaHViZXIgKDE5OTcpIHRvIHNvbHZlIHRoZSB2YW5pc2hpbmcgZ3JhZGllbnQgcHJvYmxlbSBpbiBwbGFpbiBSTk5zLiBUaGUga2V5IGlubm92YXRpb24gaXMgYSBzZXBhcmF0ZSBjZWxsIHN0YXRlIEPigpwgdGhhdCBhY3RzIGFzIGxvbmctdGVybSBtZW1vcnksIHVwZGF0ZWQgYWRkaXRpdmVseSByYXRoZXIgdGhhbiB0aHJvdWdoIHJlcGVhdGVkIG1hdHJpeCBtdWx0aXBsaWNhdGlvbi4gVGhyZWUgZ2F0aW5nIG1lY2hhbmlzbXMg4oCUIGZvcmdldCAoZuKCnCksIGlucHV0IChp4oKcKSwgYW5kIG91dHB1dCAob+KCnCkgZ2F0ZXMg4oCUIGNvbnRyb2wgaW5mb3JtYXRpb24gZmxvdyB1c2luZyBzaWdtb2lkIGFjdGl2YXRpb25zICgwID0gYmxvY2sgY29tcGxldGVseSwgMSA9IHBhc3MgY29tcGxldGVseSkuIFRoZSBmb3JnZXQgZ2F0ZSBiaWFzIGlzIGluaXRpYWxpc2VkIHRvIDEgKEpvemVmb3dpY3ogMjAxNSksIHdoaWNoIGtlZXBzIHRoZSBjZWxsIHN0YXRlIGFjdGl2ZSBieSBkZWZhdWx0IGFuZCBzaWduaWZpY2FudGx5IGltcHJvdmVzIGxlYXJuaW5nIG9uIGxvbmctcmFuZ2UgdGFza3MuIEFuIExTVE0gaGFzIDTDlyB0aGUgcGFyYW1ldGVycyBvZiBhIHZhbmlsbGEgUk5OOiBmb3VyIHdlaWdodCBtYXRyaWNlcyBvZiBzaXplIEjDlyhIK0kpIGluc3RlYWQgb2Ygb25lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBDZWxsIFN0YXRlIOKAlCBMb25nLVRlcm0gTWVtb3J5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2VsbCBzdGF0ZSBD4oKcIOKIiCDihJ3htLQgaXMgdGhlIExTVE1cdTAwMjdzIGxvbmctdGVybSBtZW1vcnkuIEl0cyB1cGRhdGUgZXF1YXRpb24gQ+KCnCA9IGbigpziiplD4oKc4oKL4oKBICsgaeKCnOKKmUPMg+KCnCBpcyBhZGRpdGl2ZSDigJQgdW5saWtlIHRoZSBSTk4gaGlkZGVuIHN0YXRlIHdoaWNoIGlzIG92ZXJ3cml0dGVuIGF0IGVhY2ggc3RlcC4gVGhlIGFkZGl0aXZlIHN0cnVjdHVyZSBtZWFucyB0aGUgZ3JhZGllbnQg4oiCQ+KCnC/iiIJD4oKc4oKL4oKBID0gZGlhZyhm4oKcKSBpcyBhIGRpYWdvbmFsIG1hdHJpeCwgbm90IGEgZnVsbCBX4oKV4oKV4bWALiBXaXRoIGZvcmdldCBnYXRlcyBuZWFyIDEsIHRoZSBncmFkaWVudCBmbG93cyBiYWNrIHRocm91Z2ggdGhlIGNlbGwgc3RhdGUgd2l0aG91dCBleHBvbmVudGlhbCBkZWNheSDigJQgdGhlIGNvbnN0YW50IGVycm9yIGNhcm91c2VsIGVmZmVjdC4gVGhlIGhpZGRlbiBzdGF0ZSBo4oKcID0gb+KCnOKKmXRhbmgoQ+KCnCkgaXMgYSBmaWx0ZXJlZCB2ZXJzaW9uIG9mIHRoZSBjZWxsIHN0YXRlLCBzaGFyZWQgd2l0aCBkb3duc3RyZWFtIGxheWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHYXRlIEVxdWF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWxsIGZvdXIgZ2F0ZXMgdGFrZSB0aGUgc2FtZSBpbnB1dCDigJQgdGhlIGNvbmNhdGVuYXRpb24gW2jigpzigovigoEsIHjigpxdIOKAlCBhbmQgZGlmZmVyIG9ubHkgaW4gdGhlaXIgd2VpZ2h0IG1hdHJpY2VzIGFuZCByb2xlcy4gRm9yZ2V0IGdhdGU6IGbigpwgPSDPgyhXZlto4oKc4oKL4oKBLHjigpxdK2JmKS4gSW5wdXQgZ2F0ZTogaeKCnCA9IM+DKFdpW2jigpzigovigoEseOKCnF0rYmkpLiBDYW5kaWRhdGUgY2VsbDogQ8yD4oKcID0gdGFuaChXY1to4oKc4oKL4oKBLHjigpxdK2JjKS4gQ2VsbCB1cGRhdGU6IEPigpwgPSBm4oKc4oqZQ+KCnOKCi+KCgSArIGnigpziiplDzIPigpwuIE91dHB1dCBnYXRlOiBv4oKcID0gz4MoV29baOKCnOKCi+KCgSx44oKcXStibykuIEhpZGRlbiBzdGF0ZTogaOKCnCA9IG/igpziipl0YW5oKEPigpwpLiBUaGUgc2lnbW9pZCBnYXRlcyBwcm9kdWNlIHZhbHVlcyBpbiAoMCwxKSwgZW5hYmxpbmcgc29mdCBnYXRpbmcg4oCUIHBhcnRpYWwgZm9yZ2V0dGluZyBvciBwYXJ0aWFsIHdyaXRpbmcg4oCUIHJhdGhlciB0aGFuIGhhcmQgYmluYXJ5IGRlY2lzaW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIExTVE1DZWxsOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSk6XG4gICAgICAgIEgsIEkgPSBoaWRkZW5fc2l6ZSwgaW5wdXRfc2l6ZVxuICAgICAgICBzY2FsZSA9IDEuMCAvIG5wLnNxcnQoSClcbiAgICAgICAgIyBDb21iaW5lZCB3ZWlnaHQgbWF0cml4IGZvciBhbGwgNCBnYXRlcyBbZiwgaSwgZywgb11cbiAgICAgICAgc2VsZi5XID0gbnAucmFuZG9tLnJhbmRuKDQgKiBILCBIICsgSSkgKiBzY2FsZVxuICAgICAgICBzZWxmLmIgPSBucC56ZXJvcygoNCAqIEgsIDEpKVxuICAgICAgICAjIEZvcmdldCBnYXRlIGJpYXMgPSAxIChKb3plZm93aWN6IDIwMTUgcmVjb21tZW5kYXRpb24pXG4gICAgICAgIHNlbGYuYls6SF0gPSAxLjBcbiAgICAgICAgc2VsZi5IID0gSFxuXG4gICAgZGVmIF9zaWdtb2lkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gMS4wIC8gKDEuMCArIG5wLmV4cCgtbnAuY2xpcCh4LCAtMjAsIDIwKSkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBoX3ByZXYsIGNfcHJldik6XG4gICAgICAgIEggPSBzZWxmLkhcbiAgICAgICAgeiA9IHNlbGYuVyBAIG5wLnZzdGFjayhbaF9wcmV2LCB4XSkgKyBzZWxmLmIgICMgKDRILCAxKVxuICAgICAgICBmID0gc2VsZi5fc2lnbW9pZCh6WzpIXSkgICAgICAgICMgZm9yZ2V0IGdhdGVcbiAgICAgICAgaSA9IHNlbGYuX3NpZ21vaWQoeltIOjIqSF0pICAgICAjIGlucHV0IGdhdGVcbiAgICAgICAgZyA9IG5wLnRhbmgoelsyKkg6MypIXSkgICAgICAgICAjIGNhbmRpZGF0ZSBjZWxsXG4gICAgICAgIG8gPSBzZWxmLl9zaWdtb2lkKHpbMypIOl0pICAgICAgIyBvdXRwdXQgZ2F0ZVxuICAgICAgICBjID0gZiAqIGNfcHJldiArIGkgKiBnICAgICAgICAgICMgYWRkaXRpdmUgY2VsbCB1cGRhdGVcbiAgICAgICAgaCA9IG8gKiBucC50YW5oKGMpICAgICAgICAgICAgICAjIGhpZGRlbiBzdGF0ZVxuICAgICAgICByZXR1cm4gaCwgYywgZGljdChmPWYsIGk9aSwgZz1nLCBvPW8pXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuSSwgSCwgVCA9IDgsIDE2LCA2XG5jZWxsID0gTFNUTUNlbGwoSSwgSClcbmggPSBucC56ZXJvcygoSCwgMSkpOyBjID0gbnAuemVyb3MoKEgsIDEpKVxuZm9yIHQgaW4gcmFuZ2UoVCk6XG4gICAgeCA9IG5wLnJhbmRvbS5yYW5kbihJLCAxKVxuICAgIGgsIGMsIGdhdGVzID0gY2VsbC5mb3J3YXJkKHgsIGgsIGMpXG4gICAgcHJpbnQoZlx1MDAyN3Q9e3R9OiB8aHw9e25wLmxpbmFsZy5ub3JtKGgpOi40Zn0sIHxjfD17bnAubGluYWxnLm5vcm0oYyk6LjRmfSwgXHUwMDI3XG4gICAgICAgICAgZlx1MDAyN2ZfbWVhbj17Z2F0ZXNbXCJmXCJdLm1lYW4oKTouM2Z9LCBpX21lYW49e2dhdGVzW1wiaVwiXS5tZWFuKCk6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQeVRvcmNoIG5uLkxTVE0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlB5VG9yY2hcdTAwMjdzIG5uLkxTVE0gaXMgYW4gb3B0aW1pc2VkIGZ1c2VkIGltcGxlbWVudGF0aW9uIG9mIHRoZSBmb3VyIGdhdGUgZXF1YXRpb25zLiBJdCByZXR1cm5zIHR3byB0ZW5zb3JzOiBvdXQgKGFsbCBoaWRkZW4gc3RhdGVzKSBhbmQgYSB0dXBsZSAoaF9uLCBjX24pIG9mIHRoZSBmaW5hbCBoaWRkZW4gYW5kIGNlbGwgc3RhdGVzLiBGb3Igc3RhdGVmdWwgcHJvY2Vzc2luZywgYm90aCBoX24gYW5kIGNfbiBtdXN0IGJlIHBhc3NlZCBhcyB0aGUgaW5pdGlhbCBzdGF0ZSB0byB0aGUgbmV4dCBjaHVuay4gUHlUb3JjaFx1MDAyN3MgZ2F0ZSBvcmRlciBpcyBbaW5wdXQsIGZvcmdldCwgY2VsbCwgb3V0cHV0XSDigJQgZGlmZmVyZW50IGZyb20gdGhlIGNvbnZlbnRpb25hbCBbZm9yZ2V0LCBpbnB1dCwgY2VsbCwgb3V0cHV0XS4gVGhlIGJpYXMgbGF5b3V0IGlzIGJpYXNfaWggKGlucHV0LWhpZGRlbiBiaWFzKSBhbmQgYmlhc19oaCAoaGlkZGVuLWhpZGRlbiBiaWFzKSBlYWNoIG9mIHNoYXBlIDTDl0gsIGNvbmNhdGVuYXRlZCBpbiBnYXRlIG9yZGVyLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbkksIEgsIG51bV9sYXllcnMsIEIsIFQgPSAxNiwgMzIsIDIsIDgsIDIwXG5cbmxzdG0gPSBubi5MU1RNKGlucHV0X3NpemU9SSwgaGlkZGVuX3NpemU9SCxcbiAgICAgICAgICAgICAgIG51bV9sYXllcnM9bnVtX2xheWVycywgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbnggPSB0b3JjaC5yYW5kbihCLCBULCBJKVxuXG4jIFNpbmdsZSBwYXNzIG92ZXIgZnVsbCBzZXF1ZW5jZVxub3V0LCAoaF9uLCBjX24pID0gbHN0bSh4KVxucHJpbnQoZlx1MDAyN291dCBzaGFwZTogIHtvdXQuc2hhcGV9ICAoQiwgVCwgSClcdTAwMjcpXG5wcmludChmXHUwMDI3aF9uIHNoYXBlOiAge2hfbi5zaGFwZX0gIChudW1fbGF5ZXJzLCBCLCBIKVx1MDAyNylcbnByaW50KGZcdTAwMjdjX24gc2hhcGU6ICB7Y19uLnNoYXBlfSAgKG51bV9sYXllcnMsIEIsIEgpXHUwMDI3KVxuXG4jIFN0YXRlZnVsOiBzcGxpdCBpbnRvIGNodW5rcywgY2FycnkgYm90aCBoIGFuZCBjXG5jaHVuayA9IDVcbmhfcyA9IHRvcmNoLnplcm9zKG51bV9sYXllcnMsIEIsIEgpXG5jX3MgPSB0b3JjaC56ZXJvcyhudW1fbGF5ZXJzLCBCLCBIKVxuY2h1bmtfb3V0cyA9IFtdXG5mb3Igc3RhcnQgaW4gcmFuZ2UoMCwgVCwgY2h1bmspOlxuICAgIHhjID0geFs6LCBzdGFydDpzdGFydCArIGNodW5rLCA6XVxuICAgIG91dF9jLCAoaF9zLCBjX3MpID0gbHN0bSh4YywgKGhfcywgY19zKSlcbiAgICBoX3MgPSBoX3MuZGV0YWNoKCk7IGNfcyA9IGNfcy5kZXRhY2goKVxuICAgIGNodW5rX291dHMuYXBwZW5kKG91dF9jKVxuYWxsX291dCA9IHRvcmNoLmNhdChjaHVua19vdXRzLCBkaW09MSlcblxucHJpbnQoZlx1MDAyN1N0YXRlZnVsIHZzIHNpbmdsZS1wYXNzIG1heCBkaWZmOiB7KG91dC5kZXRhY2goKSAtIGFsbF9vdXQpLmFicygpLm1heCgpOi40ZX1cdTAwMjcpXG5uX3BhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbHN0bS5wYXJhbWV0ZXJzKCkpXG5wcmludChmXHUwMDI3TFNUTSBwYXJhbXMgKHtudW1fbGF5ZXJzfUwsIEg9e0h9LCBJPXtJfSk6IHtuX3BhcmFtc31cdTAwMjcpXG4jIDQgZ2F0ZXMgeCAoSCpIICsgSCpJICsgSF9iaWFzKSB4IG51bV9sYXllcnNcbmV4cGVjdGVkID0gbnVtX2xheWVycyAqIDQgKiAoSCAqIEggKyBIICogSSArIDIgKiBIKVxucHJpbnQoZlx1MDAyN0V4cGVjdGVkOiB7ZXhwZWN0ZWR9ICAoNCBnYXRlcyAqIChIXjIgKyBIKkkgKyAyKkgpICogbnVtX2xheWVycylcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEFkZGluZyBQcm9ibGVtIOKAlCBMb25nLVJhbmdlIERlcGVuZGVuY3kgQmVuY2htYXJrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgYWRkaW5nIHByb2JsZW0gKEhvY2hyZWl0ZXIgYW5kIFNjaG1pZGh1YmVyIDE5OTcpIHRlc3RzIGxvbmctcmFuZ2UgZGVwZW5kZW5jeSBsZWFybmluZy4gQSBzZXF1ZW5jZSBvZiBsZW5ndGggVCBjb250YWlucyByYW5kb20gdmFsdWVzIGluIFswLDFdIHdpdGggYSBiaW5hcnkgbWFzayB0aGF0IG1hcmtzIGV4YWN0bHkgdHdvIHBvc2l0aW9ucy4gVGhlIHRhc2sgaXMgdG8gb3V0cHV0IHRoZSBzdW0gb2YgdGhlIHR3byBtYXJrZWQgdmFsdWVzLiBUaGUgTFNUTSBtdXN0IHJlbWVtYmVyIHRoZSBmaXJzdCBtYXJrZWQgdmFsdWUgKHBvdGVudGlhbGx5IGF0IHQ9MCkgdW50aWwgaXQgc2VlcyB0aGUgc2Vjb25kIG1hcmtlciAocG90ZW50aWFsbHkgYXQgdD1ULTEpIOKAlCBhIGxhZyBvZiB1cCB0byBUIHN0ZXBzLiBUaGUgYmFzZWxpbmUgTVNFIGZvciBhbHdheXMgcHJlZGljdGluZyB0aGUgbWVhbiAoMS4wKSBpcyAwLjE2NjcgZm9yIHVuaWZvcm0gWzAsMV0gaW5wdXRzLiBBbiBMU1RNIHRyYWluZWQgd2l0aCBCUFRUIGNhbiBzb2x2ZSB0aGlzIGZvciBUIHVwIHRvIHNldmVyYWwgaHVuZHJlZDsgYSB2YW5pbGxhIFJOTiBmYWlscyBmb3IgVFx1MDAzZTIw4oCTMzAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuXG5kZWYgbWFrZV9hZGRpbmdfYmF0Y2goQj02NCwgVD0xMDAsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpOlxuICAgIHNlcSAgPSB0b3JjaC5yYW5kKEIsIFQsIGRldmljZT1kZXZpY2UpXG4gICAgbWFzayA9IHRvcmNoLnplcm9zKEIsIFQsIGRldmljZT1kZXZpY2UpXG4gICAgZm9yIGIgaW4gcmFuZ2UoQik6XG4gICAgICAgIGlkeCA9IHRvcmNoLnJhbmRwZXJtKFQpWzoyXVxuICAgICAgICBtYXNrW2IsIGlkeF0gPSAxLjBcbiAgICB0YXJnZXQgPSAoc2VxICogbWFzaykuc3VtKGRpbT0xKSAgICMgc2NhbGFyIHRhcmdldCBwZXIgc2VxdWVuY2VcbiAgICB4ID0gdG9yY2guc3RhY2soW3NlcSwgbWFza10sIGRpbT0yKSAgIyAoQiwgVCwgMilcbiAgICByZXR1cm4geCwgdGFyZ2V0XG5cbkgsIEIsIGVwb2NocyA9IDY0LCAxMjgsIDQwMFxuYmFzZWxpbmVfbXNlICA9IDAuMTY2NyAgIyBWYXJbVTErVTJdIGZvciBVIH4gVW5pZm9ybVswLDFdXG5cbmZvciBUIGluIFszMCwgMTAwLCAyMDBdOlxuICAgIGxzdG0gPSBubi5MU1RNKGlucHV0X3NpemU9MiwgaGlkZGVuX3NpemU9SCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICBmYyAgID0gbm4uTGluZWFyKEgsIDEpXG4gICAgb3B0ICA9IHRvcmNoLm9wdGltLkFkYW0obGlzdChsc3RtLnBhcmFtZXRlcnMoKSkgKyBsaXN0KGZjLnBhcmFtZXRlcnMoKSksIGxyPTFlLTMpXG4gICAgZm9yIGVwIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIHgsIHkgID0gbWFrZV9hZGRpbmdfYmF0Y2goQiwgVClcbiAgICAgICAgb3V0LCBfID0gbHN0bSh4KVxuICAgICAgICBwcmVkICAgPSBmYyhvdXRbOiwgLTEsIDpdKS5zcXVlZXplKDEpXG4gICAgICAgIGxvc3MgICA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MocHJlZCwgeSlcbiAgICAgICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgeCwgeSAgPSBtYWtlX2FkZGluZ19iYXRjaCg1MTIsIFQpXG4gICAgICAgIHByZWQgID0gZmMobHN0bSh4KVswXVs6LCAtMSwgOl0pLnNxdWVlemUoMSlcbiAgICAgICAgbXNlICAgPSBubi5mdW5jdGlvbmFsLm1zZV9sb3NzKHByZWQsIHkpLml0ZW0oKVxuICAgIHNvbHZlZCA9IG1zZSBcdTAwM2MgMC4wMSAqIGJhc2VsaW5lX21zZVxuICAgIHByaW50KGZcdTAwMjdUPXtUOjNkfTogdGVzdCBNU0U9e21zZTouNmZ9LCBiYXNlbGluZT17YmFzZWxpbmVfbXNlOi40Zn0sIFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjdzb2x2ZWQ9e3NvbHZlZH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR2F0ZSBBY3RpdmF0aW9uIFZpc3VhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZpc3VhbGlzaW5nIHRoZSBmb3JnZXQgZ2F0ZSBhY3RpdmF0aW9ucyByZXZlYWxzIHRoZSBMU1RNXHUwMDI3cyBsZWFybmVkIG1lbW9yeSBtYW5hZ2VtZW50IHN0cmF0ZWd5LiBPbiB0YXNrcyByZXF1aXJpbmcgbG9uZy1yYW5nZSBtZW1vcnkgKGUuZy4sIHRoZSBhZGRpbmcgcHJvYmxlbSksIHRoZSBmb3JnZXQgZ2F0ZSBuZWFyIHRoZSBtYXJrZXIgcG9zaXRpb24gdHlwaWNhbGx5IGRyb3BzIGJlbG93IDAuNSAoc2VsZWN0aXZlbHkgb3ZlcndyaXRpbmcgbWVtb3J5KSwgd2hpbGUgcmVtYWluaW5nIGFib3ZlIDAuOSBmb3IgZmlsbGVyIHN0ZXBzIChwcmVzZXJ2aW5nIHRoZSBzdG9yZWQgdmFsdWUpLiBUaGUgaW5wdXQgZ2F0ZSBzaG93cyB0aGUgY29tcGxlbWVudGFyeSBwYXR0ZXJuOiBoaWdoIGFjdGl2YXRpb24gb25seSB3aGVuIG1lYW5pbmdmdWwgbmV3IGluZm9ybWF0aW9uIGFycml2ZXMuIEluc3BlY3RpbmcgZ2F0ZSBzdGF0aXN0aWNzIOKAlCBtZWFuLCB2YXJpYW5jZSwgZnJhY3Rpb24gbmVhciAwIG9yIDEg4oCUIGlzIGEga2V5IGRpYWdub3N0aWMgZm9yIHVuZGVyc3RhbmRpbmcgTFNUTSBmYWlsdXJlIG1vZGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5JLCBILCBULCBCID0gNCwgOCwgMjAsIDFcblxubHN0bSA9IG5uLkxTVE0oSSwgSCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiMgSW5pdGlhbGlzZSBmb3JnZXQgZ2F0ZSBiaWFzIHRvIDIuMCBmb3Igc3Ryb25nIGRlZmF1bHQgbWVtb3J5XG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAjIFB5VG9yY2ggZ2F0ZSBvcmRlcjogW2lucHV0KGkpLCBmb3JnZXQoZiksIGNlbGwoZyksIG91dHB1dChvKV1cbiAgICBsc3RtLmJpYXNfaWhfbDBbSDoyKkhdID0gMi4wICAgIyBmb3JnZXQgZ2F0ZSBiaWFzIGluIGJpYXNfaWhcbiAgICBsc3RtLmJpYXNfaGhfbDBbSDoyKkhdID0gMi4wICAgIyBmb3JnZXQgZ2F0ZSBiaWFzIGluIGJpYXNfaGhcblxueCA9IHRvcmNoLnJhbmRuKEIsIFQsIEkpXG5mb3JnZXRfZ2F0ZXMgPSBbXTsgaW5wdXRfZ2F0ZXMgPSBbXVxuaCA9IHRvcmNoLnplcm9zKDEsIEIsIEgpOyBjID0gdG9yY2guemVyb3MoMSwgQiwgSClcblxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgZm9yIHQgaW4gcmFuZ2UoVCk6XG4gICAgICAgIHh0ID0geFs6LCB0OnQrMSwgOl0gICAgICAgICAgICAgICMgKEIsIDEsIEkpXG4gICAgICAgIF8sIChoLCBjKSA9IGxzdG0oeHQsIChoLCBjKSlcbiAgICAgICAgIyBSZWNvbXB1dGUgZ2F0ZXMgZm9yIGluc3BlY3Rpb25cbiAgICAgICAgV19paCA9IGxzdG0ud2VpZ2h0X2loX2wwICAgICAgICAgICMgKDRILCBJKVxuICAgICAgICBXX2hoID0gbHN0bS53ZWlnaHRfaGhfbDAgICAgICAgICAgIyAoNEgsIEgpXG4gICAgICAgIGdhdGVzX3JhdyA9IChXX2loIEAgeHQuc3F1ZWV6ZSgpICtcbiAgICAgICAgICAgICAgICAgICAgIFdfaGggQCBoLnNxdWVlemUoKSArXG4gICAgICAgICAgICAgICAgICAgICBsc3RtLmJpYXNfaWhfbDAgKyBsc3RtLmJpYXNfaGhfbDApXG4gICAgICAgIGlfZ2F0ZSA9IHRvcmNoLnNpZ21vaWQoZ2F0ZXNfcmF3WzpIXSlcbiAgICAgICAgZl9nYXRlID0gdG9yY2guc2lnbW9pZChnYXRlc19yYXdbSDoyKkhdKVxuICAgICAgICBmb3JnZXRfZ2F0ZXMuYXBwZW5kKGZfZ2F0ZS5udW1weSgpLmNvcHkoKSlcbiAgICAgICAgaW5wdXRfZ2F0ZXMuYXBwZW5kKGlfZ2F0ZS5udW1weSgpLmNvcHkoKSlcblxuZmcgPSBucC5hcnJheShmb3JnZXRfZ2F0ZXMpICAjIChULCBIKVxuaWcgPSBucC5hcnJheShpbnB1dF9nYXRlcylcbnByaW50KGZcdTAwMjdGb3JnZXQgZ2F0ZSAtLSBtZWFuOiB7ZmcubWVhbigpOi40Zn0sIHN0ZDoge2ZnLnN0ZCgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3SW5wdXQgIGdhdGUgLS0gbWVhbjoge2lnLm1lYW4oKTouNGZ9LCBzdGQ6IHtpZy5zdGQoKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0ZyYWN0aW9uIGZvcmdldCBcdTAwM2UgMC45IChwcmVzZXJ2aW5nKTogeyhmZyBcdTAwM2UgMC45KS5tZWFuKCk6LjIlfVx1MDAyNylcbnByaW50KGZcdTAwMjdGcmFjdGlvbiBpbnB1dCAgXHUwMDNjIDAuMSAoYmxvY2tpbmcpOiAgIHsoaWcgXHUwMDNjIDAuMSkubWVhbigpOi4yJX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGFyYW1ldGVyIENvdW50IGFuZCBJbml0aWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW4gTFNUTSB3aXRoIGhpZGRlbiBzaXplIEggYW5kIGlucHV0IHNpemUgSSBoYXMgNMOXKEjDl0ggKyBIw5dJICsgSCkgcGFyYW1ldGVycyAoZm9yIGJpYXMpOiA0IGdhdGVzIMOXIChX4oKV4oKVICsgV+KCleKCkyArIGIpLiBGb3IgSD01MTIsIEk9MjU2OiA0w5coMjYyMTQ0ICsgMTMxMDcyICsgNTEyKSA9IDEsNTc0LDkxMiDiiYggMS42TSBwYXJhbWV0ZXJzIHBlciBsYXllci4gVGhlIEdSVSB1c2VzIDMgZ2F0ZXM6IDPDlyhIwrIrSMOXSStIKSDiiYggNzUlIG9mIHRoZSBMU1RNIHBhcmFtZXRlciBjb3VudC4gQSB2YW5pbGxhIFJOTiB1c2VzIDEgc2V0OiBIwrIrSMOXSStIIOKJiCAyNSUgb2YgTFNUTS4gVGhlIGZvcmdldCBnYXRlIGJpYXMgc2hvdWxkIGJlIGluaXRpYWxpc2VkIHRvIDEuMCAobm90IDAuMCk6IEpvemVmb3dpY3ogZXQgYWwuICgyMDE1KSBzaG93ZWQgdGhhdCBmb3JnZXQgZ2F0ZSBiaWFzID0gMSBvdXRwZXJmb3JtcyAwIG9uIG5lYXJseSBhbGwgdGFza3MgYnkgZW5zdXJpbmcgdGhlIGNlbGwgc3RhdGUgaXMgcHJlc2VydmVkIGJ5IGRlZmF1bHQgYXQgdGhlIHN0YXJ0IG9mIHRyYWluaW5nLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJGb3JnZXQgR2F0ZSBCaWFzIEluaXRpYWxpc2F0aW9uIiwiY29udGVudCI6IkFsd2F5cyBpbml0aWFsaXNlIHRoZSBMU1RNIGZvcmdldCBnYXRlIGJpYXMgdG8gMS4wIChvciBoaWdoZXIsIHVwIHRvIDMuMCBmb3IgdGFza3Mgd2l0aCB2ZXJ5IGxvbmcgZGVwZW5kZW5jaWVzKS4gSW4gUHlUb3JjaDogd2l0aCB0b3JjaC5ub19ncmFkKCk6IGxzdG0uYmlhc19paF9sMFtIOjIqSF0uZmlsbF8oMS4wKTsgbHN0bS5iaWFzX2hoX2wwW0g6MipIXS5maWxsXygxLjApLiBUaGlzIGVuc3VyZXMgdGhlIGNlbGwgc3RhdGUgaXMgcHJlc2VydmVkIGJ5IGRlZmF1bHQgYXQgdGhlIHN0YXJ0IG9mIHRyYWluaW5nLCBnaXZpbmcgZ3JhZGllbnRzIGEgY2xlYXIgcGF0aCBiYWNrIHRocm91Z2ggdGltZSBmcm9tIHRoZSBmaXJzdCBlcG9jaC4gRm9yZ2V0IGJpYXMgPSAwIChQeVRvcmNoIGRlZmF1bHQpIGNhdXNlcyB0aGUgbmV0d29yayB0byBmb3JnZXQgZXZlcnl0aGluZyBpbml0aWFsbHksIG1ha2luZyBlYXJseSBncmFkaWVudCBzaWduYWwgc3BhcnNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxTVE0gRXF1YXRpb25zIFN1bW1hcnkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiR2F0ZSAvIFN0YXRlIiwiRXF1YXRpb24iLCJQdXJwb3NlIiwiT3V0cHV0IFJhbmdlIl0sInJvd3MiOltbIkZvcmdldCBnYXRlIiwiZuKCnCA9IM+DKFdmwrdbaOKCnOKCi+KCgSwgeOKCnF0gKyBiZikiLCJEZWNpZGVzIHdoYXQgZnJhY3Rpb24gb2YgQ+KCnOKCi+KCgSB0byBrZWVwIiwiKDAsIDEpIHBlciBkaW1lbnNpb24iXSxbIklucHV0IGdhdGUiLCJp4oKcID0gz4MoV2nCt1to4oKc4oKL4oKBLCB44oKcXSArIGJpKSIsIkRlY2lkZXMgd2hhdCB0byB3cml0ZSBpbnRvIGNlbGwgc3RhdGUiLCIoMCwgMSkgcGVyIGRpbWVuc2lvbiJdLFsiQ2FuZGlkYXRlIGNlbGwiLCJDzIPigpwgPSB0YW5oKFdjwrdbaOKCnOKCi+KCgSwgeOKCnF0gKyBiYykiLCJOZXcgY29udGVudCB0byBwb3RlbnRpYWxseSB3cml0ZSIsIigtMSwgMSkiXSxbIkNlbGwgdXBkYXRlIiwiQ+KCnCA9IGbigpziiplD4oKc4oKL4oKBICsgaeKCnOKKmUPMg+KCnCIsIkFkZGl0aXZlIHVwZGF0ZSDigJQgbGluZWFyIGdyYWRpZW50IGhpZ2h3YXkiLCLihJ0gKHVuYm91bmRlZCkiXSxbIk91dHB1dCBnYXRlIiwib+KCnCA9IM+DKFdvwrdbaOKCnOKCi+KCgSwgeOKCnF0gKyBibykiLCJEZWNpZGVzIHdoYXQgdG8gZXhwb3NlIGFzIGhpZGRlbiBzdGF0ZSIsIigwLCAxKSBwZXIgZGltZW5zaW9uIl0sWyJIaWRkZW4gc3RhdGUiLCJo4oKcID0gb+KCnOKKmXRhbmgoQ+KCnCkiLCJPdXRwdXQgcGFzc2VkIHRvIG5leHQgbGF5ZXIgLyBkZWNvZGVyIiwiKC0xLCAxKSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTFNUTSBWYXJpYW50cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2V2ZXJhbCBMU1RNIHZhcmlhbnRzIGhhdmUgYmVlbiBwcm9wb3NlZCB0byByZWR1Y2UgcGFyYW1ldGVycyBvciBpbXByb3ZlIHBlcmZvcm1hbmNlLiBQZWVwaG9sZSBjb25uZWN0aW9ucyAoR2VycyBcdTAwMjYgU2NobWlkaHViZXIgMjAwMCkgYWxsb3cgZ2F0ZXMgdG8gZGVwZW5kIG9uIHRoZSBjZWxsIHN0YXRlIEPigpzigovigoEgZGlyZWN0bHksIGFkZGluZyBIIHBhcmFtZXRlcnMgcGVyIGdhdGUuIFRoZSBHUlUgKENobyAyMDE0KSBtZXJnZXMgdGhlIGZvcmdldCBhbmQgaW5wdXQgZ2F0ZXMgaW50byBhIHNpbmdsZSB1cGRhdGUgZ2F0ZSBhbmQgZWxpbWluYXRlcyB0aGUgY2VsbCBzdGF0ZSwgdXNpbmcgMyBnYXRlcyBhbmQgNzUlIG9mIExTVE0gcGFyYW1ldGVycyDigJQgb2Z0ZW4gbWF0Y2hpbmcgTFNUTSBxdWFsaXR5LiBDb3VwbGVkIGlucHV0LWZvcmdldCBnYXRlcyAoaeKCnCA9IDHiiJJm4oKcKSByZWR1Y2UgdG8gMyBwYXJhbWV0ZXJzIHNldHMgd2hpbGUgbWFpbnRhaW5pbmcgdGhlIGFkZGl0aXZlIHVwZGF0ZSBzdHJ1Y3R1cmUuIEVtcGlyaWNhbGx5LCBwbGFpbiBMU1RNIHdpdGggZm9yZ2V0IGJpYXMgPSAxIGlzIGNvbXBldGl0aXZlIHdpdGggYWxsIHZhcmlhbnRzIG9uIG1vc3QgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNlbGwgc3RhdGUgQ+KCnDogbG9uZy10ZXJtIG1lbW9yeSB3aXRoIGFkZGl0aXZlIHVwZGF0ZSAtLSBhdm9pZHMgcmVwZWF0ZWQgV2hoIG11bHRpcGxpY2F0aW9uLiIsIkZvcmdldCBnYXRlIGJpYXMgPSAxLjA6IGNyaXRpY2FsIGluaXQgdHJpY2s7IFB5VG9yY2ggZGVmYXVsdCBpcyAwIC0tIGFsd2F5cyBvdmVycmlkZS4iLCJQYXJhbWV0ZXIgY291bnQ6IDQqKEheMiArIEgqSSArIEgpIHBlciBsYXllcjsgfjR4IHZhbmlsbGEgUk5OLCB+MS4zM3ggR1JVLiIsIlBlZXBob2xlIGNvbm5lY3Rpb25zOiBnYXRlcyByZWFkIEN0LTEgZGlyZWN0bHkgLS0gYWRkcyBIIHBhcmFtcyBwZXIgZ2F0ZSwgbWlub3IgaW1wcm92ZW1lbnQuIiwiR1JVOiAzIGdhdGVzLCBubyBjZWxsIHN0YXRlLCBodCA9ICgxLXp0KSpodC0xICsgenQqaF90aWxkZSAtLSBzaW1wbGVyLCBvZnRlbiBjb21wYXJhYmxlLiIsIlN0YWNrZWQgTFNUTTogbXVsdGlwbGUgbGF5ZXJzIChudW1fbGF5ZXJzIFx1MDAzZSAxIGluIFB5VG9yY2gpIC0tIGVhY2ggbGF5ZXIgdGFrZXMgaGlkZGVuIHN0YXRlcyBvZiBwcmV2aW91cyBhcyBpbnB1dC4iLCJEcm9wb3V0IGluIExTVE06IGFwcGx5IGJldHdlZW4gbGF5ZXJzIChub3Qgd2l0aGluIHRpbWUgc3RlcHMpIC0tIHZhcmlhdGlvbmFsIGRyb3BvdXQgZm9yIHRlbXBvcmFsIGNvbnNpc3RlbmN5LiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# LSTM — Forget Gate, Input Gate, Output Gate, and Cell State

The Long Short-Term Memory (LSTM) network was introduced by Hochreiter and Schmidhuber (1997) to solve the vanishing gradient problem in plain RNNs. The key innovation is a separate cell state Cₜ that acts as long-term memory, updated additively rather than through repeated matrix multiplication. Three gating mechanisms — forget (fₜ), input (iₜ), and output (oₜ) gates — control information flow using sigmoid activations (0 = block completely, 1 = pass completely). The forget gate bias is initialised to 1 (Jozefowicz 2015), which keeps the cell state active by default and significantly improves learning on long-range tasks. An LSTM has 4× the parameters of a vanilla RNN: four weight matrices of size H×(H+I) instead of one.

## The Cell State — Long-Term Memory

The cell state Cₜ ∈ ℝᴴ is the LSTM's long-term memory. Its update equation Cₜ = fₜ⊙Cₜ₋₁ + iₜ⊙C̃ₜ is additive — unlike the RNN hidden state which is overwritten at each step. The additive structure means the gradient ∂Cₜ/∂Cₜ₋₁ = diag(fₜ) is a diagonal matrix, not a full Wₕₕᵀ. With forget gates near 1, the gradient flows back through the cell state without exponential decay — the constant error carousel effect. The hidden state hₜ = oₜ⊙tanh(Cₜ) is a filtered version of the cell state, shared with downstream layers.

## Gate Equations

All four gates take the same input — the concatenation [hₜ₋₁, xₜ] — and differ only in their weight matrices and roles. Forget gate: fₜ = σ(Wf[hₜ₋₁,xₜ]+bf). Input gate: iₜ = σ(Wi[hₜ₋₁,xₜ]+bi). Candidate cell: C̃ₜ = tanh(Wc[hₜ₋₁,xₜ]+bc). Cell update: Cₜ = fₜ⊙Cₜ₋₁ + iₜ⊙C̃ₜ. Output gate: oₜ = σ(Wo[hₜ₋₁,xₜ]+bo). Hidden state: hₜ = oₜ⊙tanh(Cₜ). The sigmoid gates produce values in (0,1), enabling soft gating — partial forgetting or partial writing — rather than hard binary decisions.

```python
import numpy as np

class LSTMCell:
    def __init__(self, input_size, hidden_size):
        H, I = hidden_size, input_size
        scale = 1.0 / np.sqrt(H)
        # Combined weight matrix for all 4 gates [f, i, g, o]
        self.W = np.random.randn(4 * H, H + I) * scale
        self.b = np.zeros((4 * H, 1))
        # Forget gate bias = 1 (Jozefowicz 2015 recommendation)
        self.b[:H] = 1.0
        self.H = H

    def _sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-np.clip(x, -20, 20)))

    def forward(self, x, h_prev, c_prev):
        H = self.H
        z = self.W @ np.vstack([h_prev, x]) + self.b  # (4H, 1)
        f = self._sigmoid(z[:H])        # forget gate
        i = self._sigmoid(z[H:2*H])     # input gate
        g = np.tanh(z[2*H:3*H])         # candidate cell
        o = self._sigmoid(z[3*H:])      # output gate
        c = f * c_prev + i * g          # additive cell update
        h = o * np.tanh(c)              # hidden state
        return h, c, dict(f=f, i=i, g=g, o=o)

np.random.seed(42)
I, H, T = 8, 16, 6
cell = LSTMCell(I, H)
h = np.zeros((H, 1)); c = np.zeros((H, 1))
for t in range(T):
    x = np.random.randn(I, 1)
    h, c, gates = cell.forward(x, h, c)
    print(f't={t}: |h|={np.linalg.norm(h):.4f}, |c|={np.linalg.norm(c):.4f}, '
          f'f_mean={gates["f"].mean():.3f}, i_mean={gates["i"].mean():.3f}')
```

## PyTorch nn.LSTM

PyTorch's nn.LSTM is an optimised fused implementation of the four gate equations. It returns two tensors: out (all hidden states) and a tuple (h_n, c_n) of the final hidden and cell states. For stateful processing, both h_n and c_n must be passed as the initial state to the next chunk. PyTorch's gate order is [input, forget, cell, output] — different from the conventional [forget, input, cell, output]. The bias layout is bias_ih (input-hidden bias) and bias_hh (hidden-hidden bias) each of shape 4×H, concatenated in gate order.

```python
import torch
import torch.nn as nn

torch.manual_seed(42)
I, H, num_layers, B, T = 16, 32, 2, 8, 20

lstm = nn.LSTM(input_size=I, hidden_size=H,
               num_layers=num_layers, batch_first=True)
x = torch.randn(B, T, I)

# Single pass over full sequence
out, (h_n, c_n) = lstm(x)
print(f'out shape:  {out.shape}  (B, T, H)')
print(f'h_n shape:  {h_n.shape}  (num_layers, B, H)')
print(f'c_n shape:  {c_n.shape}  (num_layers, B, H)')

# Stateful: split into chunks, carry both h and c
chunk = 5
h_s = torch.zeros(num_layers, B, H)
c_s = torch.zeros(num_layers, B, H)
chunk_outs = []
for start in range(0, T, chunk):
    xc = x[:, start:start + chunk, :]
    out_c, (h_s, c_s) = lstm(xc, (h_s, c_s))
    h_s = h_s.detach(); c_s = c_s.detach()
    chunk_outs.append(out_c)
all_out = torch.cat(chunk_outs, dim=1)

print(f'Stateful vs single-pass max diff: {(out.detach() - all_out).abs().max():.4e}')
n_params = sum(p.numel() for p in lstm.parameters())
print(f'LSTM params ({num_layers}L, H={H}, I={I}): {n_params}')
# 4 gates x (H*H + H*I + H_bias) x num_layers
expected = num_layers * 4 * (H * H + H * I + 2 * H)
print(f'Expected: {expected}  (4 gates * (H^2 + H*I + 2*H) * num_layers)')
```

## The Adding Problem — Long-Range Dependency Benchmark

The adding problem (Hochreiter and Schmidhuber 1997) tests long-range dependency learning. A sequence of length T contains random values in [0,1] with a binary mask that marks exactly two positions. The task is to output the sum of the two marked values. The LSTM must remember the first marked value (potentially at t=0) until it sees the second marker (potentially at t=T-1) — a lag of up to T steps. The baseline MSE for always predicting the mean (1.0) is 0.1667 for uniform [0,1] inputs. An LSTM trained with BPTT can solve this for T up to several hundred; a vanilla RNN fails for T>20–30.

```python
import torch
import torch.nn as nn

torch.manual_seed(42)

def make_adding_batch(B=64, T=100, device='cpu'):
    seq  = torch.rand(B, T, device=device)
    mask = torch.zeros(B, T, device=device)
    for b in range(B):
        idx = torch.randperm(T)[:2]
        mask[b, idx] = 1.0
    target = (seq * mask).sum(dim=1)   # scalar target per sequence
    x = torch.stack([seq, mask], dim=2)  # (B, T, 2)
    return x, target

H, B, epochs = 64, 128, 400
baseline_mse  = 0.1667  # Var[U1+U2] for U ~ Uniform[0,1]

for T in [30, 100, 200]:
    lstm = nn.LSTM(input_size=2, hidden_size=H, batch_first=True)
    fc   = nn.Linear(H, 1)
    opt  = torch.optim.Adam(list(lstm.parameters()) + list(fc.parameters()), lr=1e-3)
    for ep in range(epochs):
        x, y  = make_adding_batch(B, T)
        out, _ = lstm(x)
        pred   = fc(out[:, -1, :]).squeeze(1)
        loss   = nn.functional.mse_loss(pred, y)
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        x, y  = make_adding_batch(512, T)
        pred  = fc(lstm(x)[0][:, -1, :]).squeeze(1)
        mse   = nn.functional.mse_loss(pred, y).item()
    solved = mse < 0.01 * baseline_mse
    print(f'T={T:3d}: test MSE={mse:.6f}, baseline={baseline_mse:.4f}, '
          f'solved={solved}')
```

## Gate Activation Visualization

Visualising the forget gate activations reveals the LSTM's learned memory management strategy. On tasks requiring long-range memory (e.g., the adding problem), the forget gate near the marker position typically drops below 0.5 (selectively overwriting memory), while remaining above 0.9 for filler steps (preserving the stored value). The input gate shows the complementary pattern: high activation only when meaningful new information arrives. Inspecting gate statistics — mean, variance, fraction near 0 or 1 — is a key diagnostic for understanding LSTM failure modes.

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(0)
I, H, T, B = 4, 8, 20, 1

lstm = nn.LSTM(I, H, batch_first=True)
# Initialise forget gate bias to 2.0 for strong default memory
with torch.no_grad():
    # PyTorch gate order: [input(i), forget(f), cell(g), output(o)]
    lstm.bias_ih_l0[H:2*H] = 2.0   # forget gate bias in bias_ih
    lstm.bias_hh_l0[H:2*H] = 2.0   # forget gate bias in bias_hh

x = torch.randn(B, T, I)
forget_gates = []; input_gates = []
h = torch.zeros(1, B, H); c = torch.zeros(1, B, H)

with torch.no_grad():
    for t in range(T):
        xt = x[:, t:t+1, :]              # (B, 1, I)
        _, (h, c) = lstm(xt, (h, c))
        # Recompute gates for inspection
        W_ih = lstm.weight_ih_l0          # (4H, I)
        W_hh = lstm.weight_hh_l0          # (4H, H)
        gates_raw = (W_ih @ xt.squeeze() +
                     W_hh @ h.squeeze() +
                     lstm.bias_ih_l0 + lstm.bias_hh_l0)
        i_gate = torch.sigmoid(gates_raw[:H])
        f_gate = torch.sigmoid(gates_raw[H:2*H])
        forget_gates.append(f_gate.numpy().copy())
        input_gates.append(i_gate.numpy().copy())

fg = np.array(forget_gates)  # (T, H)
ig = np.array(input_gates)
print(f'Forget gate -- mean: {fg.mean():.4f}, std: {fg.std():.4f}')
print(f'Input  gate -- mean: {ig.mean():.4f}, std: {ig.std():.4f}')
print(f'Fraction forget > 0.9 (preserving): {(fg > 0.9).mean():.2%}')
print(f'Fraction input  < 0.1 (blocking):   {(ig < 0.1).mean():.2%}')
```

## Parameter Count and Initialization

An LSTM with hidden size H and input size I has 4×(H×H + H×I + H) parameters (for bias): 4 gates × (Wₕₕ + Wₕₓ + b). For H=512, I=256: 4×(262144 + 131072 + 512) = 1,574,912 ≈ 1.6M parameters per layer. The GRU uses 3 gates: 3×(H²+H×I+H) ≈ 75% of the LSTM parameter count. A vanilla RNN uses 1 set: H²+H×I+H ≈ 25% of LSTM. The forget gate bias should be initialised to 1.0 (not 0.0): Jozefowicz et al. (2015) showed that forget gate bias = 1 outperforms 0 on nearly all tasks by ensuring the cell state is preserved by default at the start of training.

> **Forget Gate Bias Initialisation**: Always initialise the LSTM forget gate bias to 1.0 (or higher, up to 3.0 for tasks with very long dependencies). In PyTorch: with torch.no_grad(): lstm.bias_ih_l0[H:2*H].fill_(1.0); lstm.bias_hh_l0[H:2*H].fill_(1.0). This ensures the cell state is preserved by default at the start of training, giving gradients a clear path back through time from the first epoch. Forget bias = 0 (PyTorch default) causes the network to forget everything initially, making early gradient signal sparse.

## LSTM Equations Summary

| Gate / State | Equation | Purpose | Output Range |
| --- | --- | --- | --- |
| Forget gate | fₜ = σ(Wf·[hₜ₋₁, xₜ] + bf) | Decides what fraction of Cₜ₋₁ to keep | (0, 1) per dimension |
| Input gate | iₜ = σ(Wi·[hₜ₋₁, xₜ] + bi) | Decides what to write into cell state | (0, 1) per dimension |
| Candidate cell | C̃ₜ = tanh(Wc·[hₜ₋₁, xₜ] + bc) | New content to potentially write | (-1, 1) |
| Cell update | Cₜ = fₜ⊙Cₜ₋₁ + iₜ⊙C̃ₜ | Additive update — linear gradient highway | ℝ (unbounded) |
| Output gate | oₜ = σ(Wo·[hₜ₋₁, xₜ] + bo) | Decides what to expose as hidden state | (0, 1) per dimension |
| Hidden state | hₜ = oₜ⊙tanh(Cₜ) | Output passed to next layer / decoder | (-1, 1) |

## LSTM Variants

Several LSTM variants have been proposed to reduce parameters or improve performance. Peephole connections (Gers & Schmidhuber 2000) allow gates to depend on the cell state Cₜ₋₁ directly, adding H parameters per gate. The GRU (Cho 2014) merges the forget and input gates into a single update gate and eliminates the cell state, using 3 gates and 75% of LSTM parameters — often matching LSTM quality. Coupled input-forget gates (iₜ = 1−fₜ) reduce to 3 parameters sets while maintaining the additive update structure. Empirically, plain LSTM with forget bias = 1 is competitive with all variants on most benchmarks.

- Cell state Cₜ: long-term memory with additive update -- avoids repeated Whh multiplication.
- Forget gate bias = 1.0: critical init trick; PyTorch default is 0 -- always override.
- Parameter count: 4*(H^2 + H*I + H) per layer; ~4x vanilla RNN, ~1.33x GRU.
- Peephole connections: gates read Ct-1 directly -- adds H params per gate, minor improvement.
- GRU: 3 gates, no cell state, ht = (1-zt)*ht-1 + zt*h_tilde -- simpler, often comparable.
- Stacked LSTM: multiple layers (num_layers > 1 in PyTorch) -- each layer takes hidden states of previous as input.
- Dropout in LSTM: apply between layers (not within time steps) -- variational dropout for temporal consistency.

---

