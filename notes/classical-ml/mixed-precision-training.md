---
title: "Mixed Precision Training — FP16, BF16, and GradScaler"
slug: "mixed-precision-training"
description: "Automatic mixed precision training: using FP16/BF16 for forward activations with FP32 master weights, gradient scaling to prevent underflow, and torch.autocast for seamless integration."
tags: ["pytorch", "tools", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWl4ZWQgcHJlY2lzaW9uIHRyYWluaW5nIHJ1bnMgdGhlIGZvcndhcmQgcGFzcyBpbiBGUDE2IG9yIEJGMTYgd2hpbGUgbWFpbnRhaW5pbmcgRlAzMiBtYXN0ZXIgd2VpZ2h0cy4gVGhpcyBkZWxpdmVycyB+MnggbWVtb3J5IHNhdmluZ3Mgb24gYWN0aXZhdGlvbnMgYW5kIDLigJM4eCBjb21wdXRlIHNwZWVkdXAgb24gdGVuc29yIGNvcmVzLCB3aXRoIG1pbmltYWwgYWNjdXJhY3kgZGVncmFkYXRpb24gd2hlbiBjb21iaW5lZCB3aXRoIGdyYWRpZW50IHNjYWxpbmcuIEl0IGlzIG5vdyBzdGFuZGFyZCBwcmFjdGljZSBmb3IgdHJhaW5pbmcgb24gbW9kZXJuIEdQVXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJNZW1vcnkgc2F2aW5nOiBhY3RpdmF0aW9ucyBzdG9yZWQgaW4gRlAxNi9CRjE2IHVzZSBoYWxmIHRoZSBieXRlcyDigJQgZW5hYmxlcyBsYXJnZXIgYmF0Y2ggc2l6ZXMgb3IgYmlnZ2VyIG1vZGVscyIsIkNvbXB1dGUgc3BlZWR1cDogTlZJRElBIHRlbnNvciBjb3JlcyBwZXJmb3JtIEZQMTYgR0VNTSBhdCAy4oCTOHggdGhlIEZQMzIgdGhyb3VnaHB1dCIsIk1hc3RlciB3ZWlnaHRzIGluIEZQMzI6IG9wdGltaXplciBzdGF0ZXMgYW5kIHdlaWdodHMgc3RheSBpbiBGUDMyIOKAlCBhY2N1cmFjeSBwcmVzZXJ2ZWQiLCJHcmFkaWVudCBzY2FsaW5nIChGUDE2IG9ubHkpOiBtdWx0aXBseSBsb3NzIGJlZm9yZSBiYWNrd2FyZCwgZGl2aWRlIGFmdGVyIOKAlCBwcmV2ZW50cyBncmFkaWVudCB1bmRlcmZsb3ciLCJCRjE2IG5lZWRzIG5vIHNjYWxpbmc6IHNhbWUgZXhwb25lbnQgcmFuZ2UgYXMgRlAzMiDigJQgbmF0aXZlIG9uIEExMDAvSDEwMC9UUFUiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRlAzMiB2cyBGUDE2IHZzIEJGMTYifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0aHJlZSBmbG9hdGluZy1wb2ludCBmb3JtYXRzIGRpZmZlciBpbiBleHBvbmVudCByYW5nZSBhbmQgbWFudGlzc2EgcHJlY2lzaW9uLiBUaGVzZSBkaWZmZXJlbmNlcyBkZXRlcm1pbmUgb3ZlcmZsb3cgcmlzaywgbnVtZXJpY2FsIHN0YWJpbGl0eSwgYW5kIHdoaWNoIG9wZXJhdGlvbnMgbXVzdCBzdGF5IGluIEZQMzIuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkZvcm1hdCIsIkV4cG9uZW50IGJpdHMiLCJNYW50aXNzYSBiaXRzIiwiUmFuZ2UiLCJQcmVjaXNpb24iLCJPdmVyZmxvdyByaXNrIiwiR1BVIHN1cHBvcnQiLCJSZWNvbW1lbmRlZCB1c2UiXSwicm93cyI6W1siRlAzMiIsIjgiLCIyMyIsIn4xLjJlLTM4IHRvIH4zLjRlKzM4IiwifjcgZGVjaW1hbCBkaWdpdHMiLCJWZXJ5IGxvdyIsIkFsbCBHUFVzIiwiTWFzdGVyIHdlaWdodHMsIGxvc3MgYWNjdW11bGF0aW9uIl0sWyJGUDE2IiwiNSIsIjEwIiwifjZlLTggdG8gfjY1NTA0IiwifjMgZGVjaW1hbCBkaWdpdHMiLCJIaWdoIChtYXg9NjU1MDQpIiwiVjEwMCwgQTEwMCwgSDEwMCwgY29uc3VtZXIiLCJGb3J3YXJkIGFjdGl2YXRpb25zIHdpdGggR3JhZFNjYWxlciJdLFsiQkYxNiIsIjgiLCI3IiwifjEuMmUtMzggdG8gfjMuNGUrMzgiLCJ+MiBkZWNpbWFsIGRpZ2l0cyIsIlZlcnkgbG93IChGUDMyIHJhbmdlKSIsIkExMDAsIEgxMDAsIFRQVSwgbmV3ZXIgQW1wZXJlIiwiUHJlZmVycmVkIGZvciB0cmFpbmluZyDigJQgbm8gc2NhbGVyIG5lZWRlZCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoidG9yY2guYXV0b2Nhc3QgYW5kIEdyYWRTY2FsZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6InRvcmNoLmF1dG9jYXN0IGF1dG9tYXRpY2FsbHkgc2VsZWN0cyB0aGUgYXBwcm9wcmlhdGUgZHR5cGUgZm9yIGVhY2ggb3BlcmF0aW9uIHdpdGhpbiBpdHMgY29udGV4dCDigJQgR0VNTSBhbmQgY29udm9sdXRpb25zIHJ1biBpbiBGUDE2IGZvciBzcGVlZDsgbG9zcyBmdW5jdGlvbnMgYW5kIG5vcm1hbGl6YXRpb24gc3RheSBpbiBGUDMyIGZvciBzdGFiaWxpdHkuIEdyYWRTY2FsZXIgbXVsdGlwbGllcyB0aGUgbG9zcyBieSBhIHNjYWxlIGZhY3RvciBiZWZvcmUgYmFja3dhcmQoKSB0byBwcmV2ZW50IGdyYWRpZW50IHVuZGVyZmxvdy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2guY3VkYS5hbXAgaW1wb3J0IGF1dG9jYXN0LCBHcmFkU2NhbGVyXG5cbmRldmljZSA9IFx1MDAyN2N1ZGFcdTAwMjcgaWYgdG9yY2guY3VkYS5pc19hdmFpbGFibGUoKSBlbHNlIFx1MDAyN2NwdVx1MDAyN1xuXG5tb2RlbCAgICAgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcig1MTIsIDI1NiksIG5uLkdFTFUoKSwgbm4uTGluZWFyKDI1NiwgMTApKS50byhkZXZpY2UpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtVyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5zY2FsZXIgICAgPSBHcmFkU2NhbGVyKCkgICMgbWFuYWdlcyBkeW5hbWljIGxvc3Mgc2NhbGluZyBmb3IgRlAxNlxuXG5YID0gdG9yY2gucmFuZG4oMTI4LCA1MTIsIGRldmljZT1kZXZpY2UpXG55ID0gdG9yY2gucmFuZGludCgwLCAxMCwgKDEyOCwpLCBkZXZpY2U9ZGV2aWNlKVxuY3JpdGVyaW9uID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpXG5cbmZvciBzdGVwIGluIHJhbmdlKDUpOlxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoc2V0X3RvX25vbmU9VHJ1ZSlcblxuICAgICMgYXV0b2Nhc3Q6IGZvcndhcmQgcGFzcyBpbiBGUDE2IChvciBCRjE2IG9uIEFtcGVyZSlcbiAgICB3aXRoIGF1dG9jYXN0KGRldmljZV90eXBlPWRldmljZSwgZHR5cGU9dG9yY2guZmxvYXQxNik6XG4gICAgICAgIGxvZ2l0cyA9IG1vZGVsKFgpXG4gICAgICAgIGxvc3MgICA9IGNyaXRlcmlvbihsb2dpdHMsIHkpXG5cbiAgICAjIHNjYWxlci5zY2FsZSgpOiBtdWx0aXBseSBsb3NzIGJ5IHNjYWxlIHRvIHByZXZlbnQgZ3JhZGllbnQgdW5kZXJmbG93XG4gICAgc2NhbGVyLnNjYWxlKGxvc3MpLmJhY2t3YXJkKClcblxuICAgICMgc2NhbGVyLnN0ZXAoKTogdW5zY2FsZSBncmFkaWVudHMsIGNoZWNrIGZvciBpbmYvbmFuLCB0aGVuIG9wdGltaXplciBzdGVwXG4gICAgIyAoc2tpcHMgc3RlcCBpZiBpbmYvbmFuIGZvdW5kIOKAlCBwcm90ZWN0cyB3ZWlnaHRzKVxuICAgIHNjYWxlci5zdGVwKG9wdGltaXplcilcblxuICAgICMgc2NhbGVyLnVwZGF0ZSgpOiBhZGp1c3Qgc2NhbGUgZmFjdG9yIGZvciBuZXh0IHN0ZXBcbiAgICBzY2FsZXIudXBkYXRlKClcblxuICAgIHByaW50KGZcdTAwMjdTdGVwIHtzdGVwKzF9OiBsb3NzPXtsb3NzLml0ZW0oKTouNGZ9ICBzY2FsZT17c2NhbGVyLmdldF9zY2FsZSgpOi4wZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IEdyYWRTY2FsZXIgaXMgTmVlZGVkIGZvciBGUDE2In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGUDE2IGdyYWRpZW50cyB1bmRlcmZsb3cgdG8gemVybyB3aGVuIHRoZWlyIG1hZ25pdHVkZSBpcyBiZWxvdyB+NmUtOC4gR3JhZFNjYWxlciBwcmV2ZW50cyB0aGlzIGJ5IHNjYWxpbmcgdXAgdGhlIGxvc3MgYmVmb3JlIGJhY2t3YXJkKCksIGtlZXBpbmcgZ3JhZGllbnRzIGluIHRoZSByZXByZXNlbnRhYmxlIEZQMTYgcmFuZ2UsIHRoZW4gdW5zY2FsaW5nIGJlZm9yZSB0aGUgb3B0aW1pemVyIHVwZGF0ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuIyBEZW1vbnN0cmF0ZSBGUDE2IHVuZGVyZmxvdyB3aXRob3V0IHNjYWxpbmdcbnggPSB0b3JjaC50ZW5zb3IoWzFlLTVdLCBkdHlwZT10b3JjaC5mbG9hdDE2KVxucHJpbnQoZlx1MDAyN0ZQMTYgdmFsdWUgMWUtNToge3guaXRlbSgpfVx1MDAyNykgICMgcHJpbnRzIDAuMCDigJQgdW5kZXJmbG93IVxuXG54X2ZwMzIgPSB0b3JjaC50ZW5zb3IoWzFlLTVdLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxucHJpbnQoZlx1MDAyN0ZQMzIgdmFsdWUgMWUtNToge3hfZnAzMi5pdGVtKCl9XHUwMDI3KSAgIyBwcmludHMgMWUtNSBjb3JyZWN0bHlcblxuIyBHcmFkU2NhbGVyIGJlaGF2aW9yOiBzY2FsZSBsb3NzIGJ5IFMsIGRpdmlkZSBncmFkaWVudHMgYnkgUyBhZnRlciBiYWNrd2FyZFxuUyA9IDY1NTM2LjAgICMgdHlwaWNhbCBpbml0aWFsIHNjYWxlIHZhbHVlXG5zbWFsbF9ncmFkID0gdG9yY2gudGVuc29yKFsxZS01XSkgICMgd291bGQgdW5kZXJmbG93IGluIEZQMTZcbnNjYWxlZF9ncmFkID0gc21hbGxfZ3JhZCAqIFMgICAgICAjIG5vdyB3aXRoaW4gRlAxNiByYW5nZVxucHJpbnQoZlx1MDAyN1xcblNjYWxlZCBncmFkIGluIEZQMTY6IHtzY2FsZWRfZ3JhZC50byh0b3JjaC5mbG9hdDE2KS5pdGVtKCl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1Vuc2NhbGVkOiAgICAgICAgICAgIHsoc2NhbGVkX2dyYWQudG8odG9yY2guZmxvYXQxNikgLyBTKS5pdGVtKCl9XHUwMDI3KVxuXG4jIEJGMTYgZG9lcyBOT1QgbmVlZCBHcmFkU2NhbGVyIChzYW1lIGV4cG9uZW50IHJhbmdlIGFzIEZQMzIpXG5kZXZpY2UgPSBcdTAwMjdjdWRhXHUwMDI3IGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcdTAwMjdjcHVcdTAwMjdcbm1vZGVsID0gbm4uTGluZWFyKDEwLCA1KS50byhkZXZpY2UpXG53aXRoIHRvcmNoLmF1dG9jYXN0KGRldmljZV90eXBlPWRldmljZSwgZHR5cGU9dG9yY2guYmZsb2F0MTYpOlxuICAgIG91dCA9IG1vZGVsKHRvcmNoLnJhbmRuKDQsIDEwLCBkZXZpY2U9ZGV2aWNlKSlcbnByaW50KGZcdTAwMjdcXG5CRjE2IG91dHB1dCBkdHlwZToge291dC5kdHlwZX1cdTAwMjcpICAjIGJmbG9hdDE2In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQkYxNiB2cyBGUDE2IFRyYWluaW5nIFN0YWJpbGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkYxNiBpcyBwcmVmZXJyZWQgZm9yIHRyYWluaW5nIG9uIEFtcGVyZSAoQTEwMCkgYW5kIGxhdGVyIEdQVXMgYmVjYXVzZSBpdCBoYXMgdGhlIHNhbWUgZXhwb25lbnQgcmFuZ2UgYXMgRlAzMiDigJQgbm8gb3ZlcmZsb3cgcmlzayDigJQgd2l0aCBvbmx5IHJlZHVjZWQgbWFudGlzc2EgcHJlY2lzaW9uLiBObyBncmFkaWVudCBzY2FsaW5nIGlzIG5lZWRlZC4gRlAxNiBpcyBzdGlsbCB1c2VkIHdoZXJlIEJGMTYgaGFyZHdhcmUgc3VwcG9ydCBpcyB1bmF2YWlsYWJsZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2guY3VkYS5hbXAgaW1wb3J0IGF1dG9jYXN0LCBHcmFkU2NhbGVyXG5pbXBvcnQgdGltZVxuXG5kZXZpY2UgPSBcdTAwMjdjdWRhXHUwMDI3IGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcdTAwMjdjcHVcdTAwMjdcblxuZGVmIHRyYWluX3ByZWNpc2lvbihkdHlwZSwgdXNlX3NjYWxlciwgbl9zdGVwcz0yMCk6XG4gICAgbW9kZWwgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICBubi5MaW5lYXIoMTAyNCwgNTEyKSwgbm4uR0VMVSgpLFxuICAgICAgICBubi5MaW5lYXIoNTEyLCAyNTYpLCBubi5HRUxVKCksXG4gICAgICAgIG5uLkxpbmVhcigyNTYsIDEwKVxuICAgICkudG8oZGV2aWNlKVxuICAgIG9wdGltaXplciA9IHRvcmNoLm9wdGltLkFkYW1XKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBzY2FsZXIgICAgPSBHcmFkU2NhbGVyKCkgaWYgdXNlX3NjYWxlciBlbHNlIE5vbmVcbiAgICBYID0gdG9yY2gucmFuZG4oMjU2LCAxMDI0LCBkZXZpY2U9ZGV2aWNlKVxuICAgIHkgPSB0b3JjaC5yYW5kaW50KDAsIDEwLCAoMjU2LCksIGRldmljZT1kZXZpY2UpXG4gICAgY3JpdGVyaW9uID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpXG4gICAgbG9zc2VzID0gW11cbiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICBmb3IgXyBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZChzZXRfdG9fbm9uZT1UcnVlKVxuICAgICAgICB3aXRoIGF1dG9jYXN0KGRldmljZV90eXBlPWRldmljZSwgZHR5cGU9ZHR5cGUpOlxuICAgICAgICAgICAgbG9zcyA9IGNyaXRlcmlvbihtb2RlbChYKSwgeSlcbiAgICAgICAgaWYgc2NhbGVyOlxuICAgICAgICAgICAgc2NhbGVyLnNjYWxlKGxvc3MpLmJhY2t3YXJkKCk7IHNjYWxlci5zdGVwKG9wdGltaXplcik7IHNjYWxlci51cGRhdGUoKVxuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgIGxvc3Nlcy5hcHBlbmQobG9zcy5pdGVtKCkpXG4gICAgZWxhcHNlZCA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgIHJldHVybiBsb3NzZXNbLTFdLCBlbGFwc2VkXG5cbmZvciBuYW1lLCBkdCwgc2MgaW4gWyhcdTAwMjdGUDMyXHUwMDI3LCB0b3JjaC5mbG9hdDMyLCBGYWxzZSksXG4gICAgICAgICAgICAgICAgICAgICAgKFx1MDAyN0ZQMTYrc2NhbGVyXHUwMDI3LCB0b3JjaC5mbG9hdDE2LCBUcnVlKSxcbiAgICAgICAgICAgICAgICAgICAgICAoXHUwMDI3QkYxNlx1MDAyNywgdG9yY2guYmZsb2F0MTYsIEZhbHNlKV06XG4gICAgZmluYWxfbG9zcywgdCA9IHRyYWluX3ByZWNpc2lvbihkdCwgc2MpXG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lOlx1MDAzYzE1fTogZmluYWxfbG9zcz17ZmluYWxfbG9zczouNGZ9ICB0aW1lPXt0Oi4yZn1zXHUwMDI3KSJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcnkgUHJvZmlsaW5nIHdpdGggTWl4ZWQgUHJlY2lzaW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNaXhlZCBwcmVjaXNpb24gY3V0cyBhY3RpdmF0aW9uIG1lbW9yeSByb3VnaGx5IGluIGhhbGYuIFRoZSBGUDMyIG1hc3RlciB3ZWlnaHRzIGFuZCBvcHRpbWl6ZXIgc3RhdGVzIHJlbWFpbiwgc28gdGhlIHNhdmluZ3MgZGVwZW5kIG9uIHRoZSByYXRpbyBvZiBhY3RpdmF0aW9uIG1lbW9yeSB0byBwYXJhbWV0ZXIgbWVtb3J5IOKAlCBsYXJnZXIgYmF0Y2ggc2l6ZXMgYW1wbGlmeSB0aGUgYmVuZWZpdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2guY3VkYS5hbXAgaW1wb3J0IGF1dG9jYXN0XG5cbmlmIG5vdCB0b3JjaC5jdWRhLmlzX2F2YWlsYWJsZSgpOlxuICAgIHByaW50KFx1MDAyN0NVREEgbm90IGF2YWlsYWJsZSDigJQgc2tpcHBpbmcgbWVtb3J5IHByb2ZpbGluZ1x1MDAyNylcbmVsc2U6XG4gICAgZGV2aWNlID0gXHUwMDI3Y3VkYVx1MDAyN1xuICAgIG1vZGVsID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgbm4uTGluZWFyKDIwNDgsIDEwMjQpLCBubi5HRUxVKCksXG4gICAgICAgIG5uLkxpbmVhcigxMDI0LCA1MTIpLCBubi5HRUxVKCksXG4gICAgICAgIG5uLkxpbmVhcig1MTIsIDEwKVxuICAgICkudG8oZGV2aWNlKVxuICAgIFggPSB0b3JjaC5yYW5kbig1MTIsIDIwNDgsIGRldmljZT1kZXZpY2UpXG5cbiAgICAjIEZQMzIgYmFzZWxpbmVcbiAgICB0b3JjaC5jdWRhLnJlc2V0X3BlYWtfbWVtb3J5X3N0YXRzKClcbiAgICBvdXRfZnAzMiA9IG1vZGVsKFgpXG4gICAgZnAzMl9tZW0gPSB0b3JjaC5jdWRhLm1heF9tZW1vcnlfYWxsb2NhdGVkKCkgLyAxZTZcbiAgICBkZWwgb3V0X2ZwMzI7IHRvcmNoLmN1ZGEuZW1wdHlfY2FjaGUoKVxuXG4gICAgIyBGUDE2IHdpdGggYXV0b2Nhc3RcbiAgICB0b3JjaC5jdWRhLnJlc2V0X3BlYWtfbWVtb3J5X3N0YXRzKClcbiAgICB3aXRoIGF1dG9jYXN0KGRldmljZV90eXBlPVx1MDAyN2N1ZGFcdTAwMjcsIGR0eXBlPXRvcmNoLmZsb2F0MTYpOlxuICAgICAgICBvdXRfZnAxNiA9IG1vZGVsKFgpXG4gICAgZnAxNl9tZW0gPSB0b3JjaC5jdWRhLm1heF9tZW1vcnlfYWxsb2NhdGVkKCkgLyAxZTZcbiAgICBkZWwgb3V0X2ZwMTY7IHRvcmNoLmN1ZGEuZW1wdHlfY2FjaGUoKVxuXG4gICAgcHJpbnQoZlx1MDAyN0ZQMzIgcGVhayBtZW1vcnk6IHtmcDMyX21lbTouMWZ9IE1CXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdGUDE2IHBlYWsgbWVtb3J5OiB7ZnAxNl9tZW06LjFmfSBNQlx1MDAyNylcbiAgICBwcmludChmXHUwMDI3TWVtb3J5IHJlZHVjdGlvbjogezEwMCooMS1mcDE2X21lbS9mcDMyX21lbSk6LjFmfSVcdTAwMjcpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgcHJvZHVjdGlvbiB0cmFpbmluZyBwaXBlbGluZXMsIG1peGVkIHByZWNpc2lvbiBpcyBuZWFybHkgYWx3YXlzIHdvcnRoIGVuYWJsaW5nLiBUaGUgbWVtb3J5IHNhdmluZ3MgYWxsb3cgbGFyZ2VyIGJhdGNoIHNpemVzIG9yIG1vZGVscyB0aGF0IHdvdWxkIE9PTSBpbiBGUDMyLCBhbmQgdGhlIHRocm91Z2hwdXQgaW5jcmVhc2Ugc2hvcnRlbnMgZXhwZXJpbWVudCBpdGVyYXRpb24gdGltZS4gVGhlIG9uZSBleGNlcHRpb246IHZlcnkgc21hbGwgbW9kZWxzIHdoZXJlIHRoZSBvdmVyaGVhZCBvZiBhdXRvY2FzdCBjb250ZXh0IHN3aXRjaGluZyBleGNlZWRzIHRoZSBjb21wdXRlIHNhdmluZ3MuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJCRjE2IGZvciBBMTAwKyBUcmFpbmluZyIsImNvbnRlbnQiOiJPbiBBbXBlcmUgKEExMDApIGFuZCBsYXRlciBHUFVzLCB1c2UgdG9yY2guYXV0b2Nhc3QoZGV2aWNlX3R5cGU9XHUwMDI3Y3VkYVx1MDAyNywgZHR5cGU9dG9yY2guYmZsb2F0MTYpIHdpdGhvdXQgYSBHcmFkU2NhbGVyLiBCRjE2IGlzIG51bWVyaWNhbGx5IHNhZmVyIHRoYW4gRlAxNiAoc2FtZSBleHBvbmVudCByYW5nZSBhcyBGUDMyKSBhbmQgZXF1YWxseSBmYXN0IG9uIEExMDAgdGVuc29yIGNvcmVzLiBGUDE2IHdpdGggR3JhZFNjYWxlciByZW1haW5zIG5lY2Vzc2FyeSBvbiBWb2x0YSAoVjEwMCkgYW5kIG9sZGVyIGNvbnN1bWVyIEdQVXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRlAxNiBtYXggdmFsdWUgaXMgfjY1NTA0IOKAlCBncmFkaWVudHMgYmVsb3cgfjZlLTggdW5kZXJmbG93IHRvIHplcm87IEdyYWRTY2FsZXIgc2NhbGVzIGxvc3MgdG8ga2VlcCBncmFkaWVudHMgcmVwcmVzZW50YWJsZSIsIkJGMTYgaGFzIEZQMzJcdTAwMjdzIGV4cG9uZW50IHJhbmdlIOKAlCBubyBvdmVyZmxvdyBvciB1bmRlcmZsb3cgcmlzazsgcHJlZmVycmVkIGZvciBBMTAwL0gxMDAgdHJhaW5pbmcgd2l0aG91dCBHcmFkU2NhbGVyIiwidG9yY2guYXV0b2Nhc3Qgc2VsZWN0cyBkdHlwZSBwZXIgb3BlcmF0aW9uIOKAlCBHRU1NL2NvbnYgaW4gRlAxNiwgbm9ybWFsaXphdGlvbiBhbmQgbG9zcyBpbiBGUDMyIGZvciBzdGFiaWxpdHkiLCJHcmFkU2NhbGVyIHdvcmtmbG93OiBzY2FsZShsb3NzKS5iYWNrd2FyZCgpIOKGkiBzdGVwKG9wdGltaXplcikg4oaSIHVwZGF0ZSgpIOKGkiBhdXRvbWF0aWNhbGx5IGFkanVzdHMgc2NhbGUgZmFjdG9yIiwiTWl4ZWQgcHJlY2lzaW9uIGN1dHMgYWN0aXZhdGlvbiBtZW1vcnkgfjJ4IGFuZCBkZWxpdmVycyAy4oCTOHggY29tcHV0ZSBzcGVlZHVwIHZpYSB0ZW5zb3IgY29yZSBHRU1NIl19XQ=="
---
# Mixed Precision Training — FP16, BF16, and GradScaler

Mixed precision training runs the forward pass in FP16 or BF16 while maintaining FP32 master weights. This delivers ~2x memory savings on activations and 2–8x compute speedup on tensor cores, with minimal accuracy degradation when combined with gradient scaling. It is now standard practice for training on modern GPUs.

- Memory saving: activations stored in FP16/BF16 use half the bytes — enables larger batch sizes or bigger models
- Compute speedup: NVIDIA tensor cores perform FP16 GEMM at 2–8x the FP32 throughput
- Master weights in FP32: optimizer states and weights stay in FP32 — accuracy preserved
- Gradient scaling (FP16 only): multiply loss before backward, divide after — prevents gradient underflow
- BF16 needs no scaling: same exponent range as FP32 — native on A100/H100/TPU

## FP32 vs FP16 vs BF16

The three floating-point formats differ in exponent range and mantissa precision. These differences determine overflow risk, numerical stability, and which operations must stay in FP32.

| Format | Exponent bits | Mantissa bits | Range | Precision | Overflow risk | GPU support | Recommended use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FP32 | 8 | 23 | ~1.2e-38 to ~3.4e+38 | ~7 decimal digits | Very low | All GPUs | Master weights, loss accumulation |
| FP16 | 5 | 10 | ~6e-8 to ~65504 | ~3 decimal digits | High (max=65504) | V100, A100, H100, consumer | Forward activations with GradScaler |
| BF16 | 8 | 7 | ~1.2e-38 to ~3.4e+38 | ~2 decimal digits | Very low (FP32 range) | A100, H100, TPU, newer Ampere | Preferred for training — no scaler needed |

## torch.autocast and GradScaler

torch.autocast automatically selects the appropriate dtype for each operation within its context — GEMM and convolutions run in FP16 for speed; loss functions and normalization stay in FP32 for stability. GradScaler multiplies the loss by a scale factor before backward() to prevent gradient underflow.

```python
import torch
import torch.nn as nn
from torch.cuda.amp import autocast, GradScaler

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model     = nn.Sequential(nn.Linear(512, 256), nn.GELU(), nn.Linear(256, 10)).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
scaler    = GradScaler()  # manages dynamic loss scaling for FP16

X = torch.randn(128, 512, device=device)
y = torch.randint(0, 10, (128,), device=device)
criterion = nn.CrossEntropyLoss()

for step in range(5):
    optimizer.zero_grad(set_to_none=True)

    # autocast: forward pass in FP16 (or BF16 on Ampere)
    with autocast(device_type=device, dtype=torch.float16):
        logits = model(X)
        loss   = criterion(logits, y)

    # scaler.scale(): multiply loss by scale to prevent gradient underflow
    scaler.scale(loss).backward()

    # scaler.step(): unscale gradients, check for inf/nan, then optimizer step
    # (skips step if inf/nan found — protects weights)
    scaler.step(optimizer)

    # scaler.update(): adjust scale factor for next step
    scaler.update()

    print(f'Step {step+1}: loss={loss.item():.4f}  scale={scaler.get_scale():.0f}')
```

## Why GradScaler is Needed for FP16

FP16 gradients underflow to zero when their magnitude is below ~6e-8. GradScaler prevents this by scaling up the loss before backward(), keeping gradients in the representable FP16 range, then unscaling before the optimizer update.

```python
import torch
import torch.nn as nn

# Demonstrate FP16 underflow without scaling
x = torch.tensor([1e-5], dtype=torch.float16)
print(f'FP16 value 1e-5: {x.item()}')  # prints 0.0 — underflow!

x_fp32 = torch.tensor([1e-5], dtype=torch.float32)
print(f'FP32 value 1e-5: {x_fp32.item()}')  # prints 1e-5 correctly

# GradScaler behavior: scale loss by S, divide gradients by S after backward
S = 65536.0  # typical initial scale value
small_grad = torch.tensor([1e-5])  # would underflow in FP16
scaled_grad = small_grad * S      # now within FP16 range
print(f'\nScaled grad in FP16: {scaled_grad.to(torch.float16).item()}')
print(f'Unscaled:            {(scaled_grad.to(torch.float16) / S).item()}')

# BF16 does NOT need GradScaler (same exponent range as FP32)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = nn.Linear(10, 5).to(device)
with torch.autocast(device_type=device, dtype=torch.bfloat16):
    out = model(torch.randn(4, 10, device=device))
print(f'\nBF16 output dtype: {out.dtype}')  # bfloat16
```

## BF16 vs FP16 Training Stability

BF16 is preferred for training on Ampere (A100) and later GPUs because it has the same exponent range as FP32 — no overflow risk — with only reduced mantissa precision. No gradient scaling is needed. FP16 is still used where BF16 hardware support is unavailable.

```python
import torch
import torch.nn as nn
from torch.cuda.amp import autocast, GradScaler
import time

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def train_precision(dtype, use_scaler, n_steps=20):
    model = nn.Sequential(
        nn.Linear(1024, 512), nn.GELU(),
        nn.Linear(512, 256), nn.GELU(),
        nn.Linear(256, 10)
    ).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    scaler    = GradScaler() if use_scaler else None
    X = torch.randn(256, 1024, device=device)
    y = torch.randint(0, 10, (256,), device=device)
    criterion = nn.CrossEntropyLoss()
    losses = []
    t0 = time.perf_counter()
    for _ in range(n_steps):
        optimizer.zero_grad(set_to_none=True)
        with autocast(device_type=device, dtype=dtype):
            loss = criterion(model(X), y)
        if scaler:
            scaler.scale(loss).backward(); scaler.step(optimizer); scaler.update()
        else:
            loss.backward(); optimizer.step()
        losses.append(loss.item())
    elapsed = time.perf_counter() - t0
    return losses[-1], elapsed

for name, dt, sc in [('FP32', torch.float32, False),
                      ('FP16+scaler', torch.float16, True),
                      ('BF16', torch.bfloat16, False)]:
    final_loss, t = train_precision(dt, sc)
    print(f'{name:<15}: final_loss={final_loss:.4f}  time={t:.2f}s')
```

---

## Memory Profiling with Mixed Precision

Mixed precision cuts activation memory roughly in half. The FP32 master weights and optimizer states remain, so the savings depend on the ratio of activation memory to parameter memory — larger batch sizes amplify the benefit.

```python
import torch
import torch.nn as nn
from torch.cuda.amp import autocast

if not torch.cuda.is_available():
    print('CUDA not available — skipping memory profiling')
else:
    device = 'cuda'
    model = nn.Sequential(
        nn.Linear(2048, 1024), nn.GELU(),
        nn.Linear(1024, 512), nn.GELU(),
        nn.Linear(512, 10)
    ).to(device)
    X = torch.randn(512, 2048, device=device)

    # FP32 baseline
    torch.cuda.reset_peak_memory_stats()
    out_fp32 = model(X)
    fp32_mem = torch.cuda.max_memory_allocated() / 1e6
    del out_fp32; torch.cuda.empty_cache()

    # FP16 with autocast
    torch.cuda.reset_peak_memory_stats()
    with autocast(device_type='cuda', dtype=torch.float16):
        out_fp16 = model(X)
    fp16_mem = torch.cuda.max_memory_allocated() / 1e6
    del out_fp16; torch.cuda.empty_cache()

    print(f'FP32 peak memory: {fp32_mem:.1f} MB')
    print(f'FP16 peak memory: {fp16_mem:.1f} MB')
    print(f'Memory reduction: {100*(1-fp16_mem/fp32_mem):.1f}%')
```

For production training pipelines, mixed precision is nearly always worth enabling. The memory savings allow larger batch sizes or models that would OOM in FP32, and the throughput increase shortens experiment iteration time. The one exception: very small models where the overhead of autocast context switching exceeds the compute savings.

> **BF16 for A100+ Training**: On Ampere (A100) and later GPUs, use torch.autocast(device_type='cuda', dtype=torch.bfloat16) without a GradScaler. BF16 is numerically safer than FP16 (same exponent range as FP32) and equally fast on A100 tensor cores. FP16 with GradScaler remains necessary on Volta (V100) and older consumer GPUs.

## Key Takeaways

- FP16 max value is ~65504 — gradients below ~6e-8 underflow to zero; GradScaler scales loss to keep gradients representable
- BF16 has FP32's exponent range — no overflow or underflow risk; preferred for A100/H100 training without GradScaler
- torch.autocast selects dtype per operation — GEMM/conv in FP16, normalization and loss in FP32 for stability
- GradScaler workflow: scale(loss).backward() → step(optimizer) → update() → automatically adjusts scale factor
- Mixed precision cuts activation memory ~2x and delivers 2–8x compute speedup via tensor core GEMM

