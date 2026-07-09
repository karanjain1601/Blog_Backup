---
title: "PyTorch — Autograd, Tensors, nn.Module, and DataLoader"
slug: "pytorch-fundamentals"
description: "PyTorch core primitives: tensor operations with autograd, building models with nn.Module, loading data with DataLoader, and writing a complete training loop."
tags: ["pytorch", "tools", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHlUb3JjaCBpcyB0aGUgZG9taW5hbnQgZGVlcCBsZWFybmluZyBmcmFtZXdvcmsgZm9yIHJlc2VhcmNoIGFuZCBpbmNyZWFzaW5nbHkgZm9yIHByb2R1Y3Rpb24uIEl0cyBjb3JlIGRlc2lnbiDigJQgZWFnZXIgZXhlY3V0aW9uLCBkeW5hbWljIGdyYXBocywgUHl0aG9uaWMgQVBJIOKAlCBtYWtlcyBkZWJ1Z2dpbmcgbmF0dXJhbCBhbmQgY3VzdG9tIGFyY2hpdGVjdHVyZXMgc3RyYWlnaHRmb3J3YXJkLiBVbmRlcnN0YW5kaW5nIHRoZSBmb3VyIHByaW1pdGl2ZXMgKHRlbnNvcnMsIGF1dG9ncmFkLCBubi5Nb2R1bGUsIERhdGFMb2FkZXIpIHVubG9ja3MgZXZlcnl0aGluZyBlbHNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRlbnNvcnMgYW5kIERhdGEgVHlwZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgdG9yY2guVGVuc29yIGlzIGFuIE4tZGltZW5zaW9uYWwgYXJyYXkgYmFja2VkIGJ5IGEgY29udGlndW91cyBibG9jayBvZiBtZW1vcnksIHdpdGggYSBkdHlwZSAoZmxvYXQzMiwgZmxvYXQxNiwgYmZsb2F0MTYsIGludDY0LCBib29sKSwgYSBkZXZpY2UgKGNwdSwgY3VkYSwgbXBzKSwgYW5kIG9wdGlvbmFsIGF1dG9ncmFkIHRyYWNraW5nIHZpYSByZXF1aXJlc19ncmFkLiBPcGVyYXRpb25zIG9uIHRlbnNvcnMgd2l0aCByZXF1aXJlc19ncmFkPVRydWUgYXJlIHJlY29yZGVkIGludG8gYSBjb21wdXRhdGlvbmFsIGdyYXBoLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiZmxvYXQzMjogZGVmYXVsdCBkdHlwZSBmb3IgbW9kZWwgd2VpZ2h0cyDigJQgMzItYml0IElFRUUgNzU0LCBzYWZlIGZvciBtb3N0IG9wZXJhdGlvbnMiLCJmbG9hdDE2OiAxNi1iaXQgcmVkdWNlZCBwcmVjaXNpb24g4oCUIGZhc3RlciBvbiB0ZW5zb3IgY29yZXMsIHJpc2tzIG92ZXJmbG93IChtYXggfjY1NTA0KSIsImJmbG9hdDE2OiAxNi1iaXQgd2l0aCBzYW1lIGV4cG9uZW50IHJhbmdlIGFzIGZsb2F0MzIg4oCUIHByZWZlcnJlZCBmb3IgdHJhaW5pbmcgb24gQTEwMC9IMTAwIiwiTGVhZiB0ZW5zb3JzOiB0ZW5zb3JzIGNyZWF0ZWQgYnkgdGhlIHVzZXIgKG5vdCBieSBvcGVyYXRpb25zKSDigJQgb25seSB0aGVzZSBhY2N1bXVsYXRlIC5ncmFkIiwiTm9uLWxlYWYgdGVuc29yczogb3V0cHV0cyBvZiBvcGVyYXRpb25zIOKAlCB0aGVpciAuZ3JhZCBpcyBub3QgcmV0YWluZWQgdW5sZXNzIHJldGFpbl9ncmFkKCkgY2FsbGVkIiwiRGV2aWNlIG1vdmVtZW50OiB0ZW5zb3IudG8oXHUwMDI3Y3VkYVx1MDAyNyksIHRlbnNvci5jdWRhKCksIHRlbnNvci5jcHUoKSDigJQgYWx3YXlzIHN5bmNocm9ub3VzIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRlbnNvcnMgYW5kIEF1dG9ncmFkIGZyb20gU2NyYXRjaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvbXB1dGF0aW9uYWwgZ3JhcGggaXMgYnVpbHQgZHluYW1pY2FsbHkgZHVyaW5nIHRoZSBmb3J3YXJkIHBhc3MuIENhbGxpbmcgLmJhY2t3YXJkKCkgb24gYSBzY2FsYXIgdHJhdmVyc2VzIHRoaXMgZ3JhcGggaW4gcmV2ZXJzZSwgY29tcHV0aW5nIGdyYWRpZW50cyB2aWEgY2hhaW4gcnVsZSBhbmQgYWNjdW11bGF0aW5nIHRoZW0gaW4gLmdyYWQgb2YgZWFjaCBsZWFmIHRlbnNvci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuIyBCYXNpYyB0ZW5zb3Igd2l0aCBncmFkaWVudCB0cmFja2luZ1xueCA9IHRvcmNoLnRlbnNvcihbWzEuMCwgMi4wXSwgWzMuMCwgNC4wXV0sIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcblcgPSB0b3JjaC50ZW5zb3IoW1swLjUsIC0wLjVdLCBbMS4wLCAwLjNdXSwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxuXG4jIEZvcndhcmQgcGFzcyDigJQgYnVpbGRzIGNvbXB1dGF0aW9uYWwgZ3JhcGhcbnogPSB4IEAgVyAgICAgICAgICAjIG1hdHJpeCBtdWx0aXBseVxubG9zcyA9IHouc3VtKCkgICAgICMgc2NhbGFyIGxvc3NcblxuIyBCYWNrd2FyZCBwYXNzIOKAlCB0cmF2ZXJzZXMgZ3JhcGgsIGZpbGxzIC5ncmFkXG5sb3NzLmJhY2t3YXJkKClcbnByaW50KFx1MDAyN3guZ3JhZDpcdTAwMjcsIHguZ3JhZCkgICAjIGRsL2R4XG5wcmludChcdTAwMjdXLmdyYWQ6XHUwMDI3LCBXLmdyYWQpICAgIyBkbC9kV1xuXG4jIENyaXRpY2FsOiB6ZXJvIGdyYWRpZW50cyBiZWZvcmUgbmV4dCBiYWNrd2FyZCBwYXNzXG4jIChncmFkaWVudHMgYWNjdW11bGF0ZSBieSBkZWZhdWx0IOKAlCBhIGNvbW1vbiBidWcpXG54LmdyYWQuemVyb18oKVxuVy5ncmFkLnplcm9fKClcblxuIyB0b3JjaC5ub19ncmFkKCkgZm9yIGluZmVyZW5jZSDigJQgbm8gZ3JhcGgsIGxvd2VyIG1lbW9yeVxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgel9pbmYgPSB4IEAgV1xuICAgIHByaW50KFx1MDAyN1JlcXVpcmVzIGdyYWQgKGluZmVyZW5jZSk6XHUwMDI3LCB6X2luZi5yZXF1aXJlc19ncmFkKSAgIyBGYWxzZVxuXG4jIERldGFjaCBhIHRlbnNvciBmcm9tIHRoZSBncmFwaCAodXNlZCBpbiBSTCwgR0FOIHRhcmdldHMpXG56X2RldGFjaGVkID0gei5kZXRhY2goKVxucHJpbnQoXHUwMDI3RGV0YWNoZWQgcmVxdWlyZXMgZ3JhZDpcdTAwMjcsIHpfZGV0YWNoZWQucmVxdWlyZXNfZ3JhZCkgICMgRmFsc2UifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCdWlsZGluZyBNb2RlbHMgd2l0aCBubi5Nb2R1bGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Im5uLk1vZHVsZSBpcyB0aGUgYmFzZSBjbGFzcyBmb3IgYWxsIG5ldXJhbCBuZXR3b3JrIGxheWVycyBhbmQgbW9kZWxzLiBJdCB0cmFja3MgcGFyYW1ldGVycyBhdXRvbWF0aWNhbGx5LCBzdXBwb3J0cyBkZXZpY2UgbW92ZW1lbnQgdmlhIC50bygpLCBhbmQgcHJvdmlkZXMgc3RhdGVfZGljdCgpIGZvciBzZXJpYWxpemF0aW9uLiBFdmVyeSBjdXN0b20gbGF5ZXIgc3ViY2xhc3NlcyBubi5Nb2R1bGUgYW5kIGltcGxlbWVudHMgZm9yd2FyZCgpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBSZXNpZHVhbEJsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbTogaW50LCBkcm9wb3V0OiBmbG9hdCA9IDAuMSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmZjMSAgICA9IG5uLkxpbmVhcihkaW0sIGRpbSAqIDIpXG4gICAgICAgIHNlbGYuZmMyICAgID0gbm4uTGluZWFyKGRpbSAqIDIsIGRpbSlcbiAgICAgICAgc2VsZi5ub3JtMSAgPSBubi5MYXllck5vcm0oZGltKVxuICAgICAgICBzZWxmLm5vcm0yICA9IG5uLkxheWVyTm9ybShkaW0pXG4gICAgICAgIHNlbGYuZHJvcCAgID0gbm4uRHJvcG91dChkcm9wb3V0KVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgcmVzaWR1YWwgPSB4XG4gICAgICAgIHggPSBzZWxmLm5vcm0xKHgpXG4gICAgICAgIHggPSBGLmdlbHUoc2VsZi5mYzEoeCkpXG4gICAgICAgIHggPSBzZWxmLmRyb3AoeClcbiAgICAgICAgeCA9IHNlbGYuZmMyKHgpXG4gICAgICAgIHJldHVybiBzZWxmLm5vcm0yKHggKyByZXNpZHVhbCkgICMgcmVzaWR1YWwgY29ubmVjdGlvblxuXG5jbGFzcyBUYWJ1bGFyTUxQKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5faW46IGludCwgbl9vdXQ6IGludCwgZGVwdGg6IGludCA9IDMsIHdpZHRoOiBpbnQgPSAyNTYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5pbnB1dF9wcm9qID0gbm4uTGluZWFyKG5faW4sIHdpZHRoKVxuICAgICAgICBzZWxmLmJsb2NrcyAgICAgPSBubi5Nb2R1bGVMaXN0KFtSZXNpZHVhbEJsb2NrKHdpZHRoKSBmb3IgXyBpbiByYW5nZShkZXB0aCldKVxuICAgICAgICBzZWxmLmhlYWQgICAgICAgPSBubi5MaW5lYXIod2lkdGgsIG5fb3V0KVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgeCA9IHNlbGYuaW5wdXRfcHJvaih4KVxuICAgICAgICBmb3IgYmxvY2sgaW4gc2VsZi5ibG9ja3M6XG4gICAgICAgICAgICB4ID0gYmxvY2soeClcbiAgICAgICAgcmV0dXJuIHNlbGYuaGVhZCh4KVxuXG5tb2RlbCA9IFRhYnVsYXJNTFAobl9pbj0yMCwgbl9vdXQ9MilcbnByaW50KGZcdTAwMjdQYXJhbWV0ZXJzOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpOix9XHUwMDI3KVxucHJpbnQobW9kZWwpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3VzdG9tIERhdGFzZXQgYW5kIERhdGFMb2FkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRhdGFMb2FkZXIgd3JhcHMgYSBEYXRhc2V0LCBoYW5kbGVzIGJhdGNoaW5nLCBzaHVmZmxpbmcsIGFuZCBwYXJhbGxlbCBsb2FkaW5nLiBJbXBsZW1lbnRpbmcgX19sZW5fXyBhbmQgX19nZXRpdGVtX18gaXMgYWxsIHRoYXQgaXMgcmVxdWlyZWQgZm9yIGEgY3VzdG9tIERhdGFzZXQuIHBpbl9tZW1vcnk9VHJ1ZSBhbmQgbnVtX3dvcmtlcnNcdTAwM2UwIGFyZSBrZXkgZm9yIEdQVSB0cmFpbmluZyB0aHJvdWdocHV0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YXNldCwgRGF0YUxvYWRlclxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuY2xhc3MgVGFidWxhckRhdGFzZXQoRGF0YXNldCk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIFg6IG5wLm5kYXJyYXksIHk6IG5wLm5kYXJyYXksIHNjYWxlcj1Ob25lLCBmaXRfc2NhbGVyPUZhbHNlKTpcbiAgICAgICAgaWYgc2NhbGVyIGlzIE5vbmU6XG4gICAgICAgICAgICBzY2FsZXIgPSBTdGFuZGFyZFNjYWxlcigpXG4gICAgICAgIGlmIGZpdF9zY2FsZXI6XG4gICAgICAgICAgICBYID0gc2NhbGVyLmZpdF90cmFuc2Zvcm0oWClcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIFggPSBzY2FsZXIudHJhbnNmb3JtKFgpXG4gICAgICAgIHNlbGYuWCAgICAgID0gdG9yY2guRmxvYXRUZW5zb3IoWClcbiAgICAgICAgc2VsZi55ICAgICAgPSB0b3JjaC5Mb25nVGVuc29yKHkpXG4gICAgICAgIHNlbGYuc2NhbGVyID0gc2NhbGVyXG5cbiAgICBkZWYgX19sZW5fXyhzZWxmKSAtXHUwMDNlIGludDpcbiAgICAgICAgcmV0dXJuIGxlbihzZWxmLlgpXG5cbiAgICBkZWYgX19nZXRpdGVtX18oc2VsZiwgaWR4OiBpbnQpOlxuICAgICAgICByZXR1cm4gc2VsZi5YW2lkeF0sIHNlbGYueVtpZHhdXG5cbiMgVXNhZ2VcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24obl9zYW1wbGVzPTUwMDAsIG5fZmVhdHVyZXM9MjAsIHJhbmRvbV9zdGF0ZT00MilcblxudHJhaW5fZHMgPSBUYWJ1bGFyRGF0YXNldChYWzo0MDAwXSwgeVs6NDAwMF0sIGZpdF9zY2FsZXI9VHJ1ZSlcbnZhbF9kcyAgID0gVGFidWxhckRhdGFzZXQoWFs0MDAwOl0sIHlbNDAwMDpdLCBzY2FsZXI9dHJhaW5fZHMuc2NhbGVyKVxuXG50cmFpbl9sb2FkZXIgPSBEYXRhTG9hZGVyKHRyYWluX2RzLCBiYXRjaF9zaXplPTI1Niwgc2h1ZmZsZT1UcnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICBudW1fd29ya2Vycz0wLCBwaW5fbWVtb3J5PUZhbHNlKVxudmFsX2xvYWRlciAgID0gRGF0YUxvYWRlcih2YWxfZHMsICAgYmF0Y2hfc2l6ZT01MTIsIHNodWZmbGU9RmFsc2UpXG5cbmZvciBYX2JhdGNoLCB5X2JhdGNoIGluIHRyYWluX2xvYWRlcjpcbiAgICBwcmludChmXHUwMDI3QmF0Y2ggc2hhcGU6IHtYX2JhdGNoLnNoYXBlfSwgZHR5cGU6IHtYX2JhdGNoLmR0eXBlfVx1MDAyNylcbiAgICBicmVhayJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBsZXRlIFRyYWluaW5nIExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcHJvZHVjdGlvbiB0cmFpbmluZyBsb29wIGluY2x1ZGVzOiBncmFkaWVudCB6ZXJvaW5nIGJlZm9yZSBlYWNoIGZvcndhcmQgcGFzcywgbW9kZWwuZXZhbCgpIGZvciB2YWxpZGF0aW9uIChkaXNhYmxlcyBkcm9wb3V0L0JhdGNoTm9ybSksIGEgbGVhcm5pbmcgcmF0ZSBzY2hlZHVsZXIsIGFuZCBlYXJseSBzdG9wcGluZyBiYXNlZCBvbiB2YWxpZGF0aW9uIGxvc3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLm9wdGltLmxyX3NjaGVkdWxlciBpbXBvcnQgQ29zaW5lQW5uZWFsaW5nTFJcblxuZGVmIHRyYWluX2Vwb2NoKG1vZGVsLCBsb2FkZXIsIG9wdGltaXplciwgY3JpdGVyaW9uLCBkZXZpY2UpOlxuICAgIG1vZGVsLnRyYWluKClcbiAgICB0b3RhbF9sb3NzLCBjb3JyZWN0LCB0b3RhbCA9IDAuMCwgMCwgMFxuICAgIGZvciBYX2JhdGNoLCB5X2JhdGNoIGluIGxvYWRlcjpcbiAgICAgICAgWF9iYXRjaCwgeV9iYXRjaCA9IFhfYmF0Y2gudG8oZGV2aWNlKSwgeV9iYXRjaC50byhkZXZpY2UpXG4gICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoc2V0X3RvX25vbmU9VHJ1ZSkgICMgbWVtb3J5LWVmZmljaWVudCB6ZXJvX2dyYWRcbiAgICAgICAgbG9naXRzID0gbW9kZWwoWF9iYXRjaClcbiAgICAgICAgbG9zcyAgID0gY3JpdGVyaW9uKGxvZ2l0cywgeV9iYXRjaClcbiAgICAgICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgICAgIG5uLnV0aWxzLmNsaXBfZ3JhZF9ub3JtXyhtb2RlbC5wYXJhbWV0ZXJzKCksIG1heF9ub3JtPTEuMClcbiAgICAgICAgb3B0aW1pemVyLnN0ZXAoKVxuICAgICAgICB0b3RhbF9sb3NzICs9IGxvc3MuaXRlbSgpICogbGVuKHlfYmF0Y2gpXG4gICAgICAgIGNvcnJlY3QgICAgKz0gKGxvZ2l0cy5hcmdtYXgoMSkgPT0geV9iYXRjaCkuc3VtKCkuaXRlbSgpXG4gICAgICAgIHRvdGFsICAgICAgKz0gbGVuKHlfYmF0Y2gpXG4gICAgcmV0dXJuIHRvdGFsX2xvc3MgLyB0b3RhbCwgY29ycmVjdCAvIHRvdGFsXG5cbkB0b3JjaC5ub19ncmFkKClcbmRlZiBldmFsX2Vwb2NoKG1vZGVsLCBsb2FkZXIsIGNyaXRlcmlvbiwgZGV2aWNlKTpcbiAgICBtb2RlbC5ldmFsKCkgICMgZGlzYWJsZXMgZHJvcG91dCBhbmQgc2V0cyBCTiB0byBldmFsIG1vZGVcbiAgICB0b3RhbF9sb3NzLCBjb3JyZWN0LCB0b3RhbCA9IDAuMCwgMCwgMFxuICAgIGZvciBYX2JhdGNoLCB5X2JhdGNoIGluIGxvYWRlcjpcbiAgICAgICAgWF9iYXRjaCwgeV9iYXRjaCA9IFhfYmF0Y2gudG8oZGV2aWNlKSwgeV9iYXRjaC50byhkZXZpY2UpXG4gICAgICAgIGxvZ2l0cyA9IG1vZGVsKFhfYmF0Y2gpXG4gICAgICAgIHRvdGFsX2xvc3MgKz0gY3JpdGVyaW9uKGxvZ2l0cywgeV9iYXRjaCkuaXRlbSgpICogbGVuKHlfYmF0Y2gpXG4gICAgICAgIGNvcnJlY3QgICAgKz0gKGxvZ2l0cy5hcmdtYXgoMSkgPT0geV9iYXRjaCkuc3VtKCkuaXRlbSgpXG4gICAgICAgIHRvdGFsICAgICAgKz0gbGVuKHlfYmF0Y2gpXG4gICAgcmV0dXJuIHRvdGFsX2xvc3MgLyB0b3RhbCwgY29ycmVjdCAvIHRvdGFsIn0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBubi5Nb2R1bGUgTWV0aG9kcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJQdXJwb3NlIiwiQ29tbW9uIFVzYWdlIl0sInJvd3MiOltbImZvcndhcmQoeCkiLCJEZWZpbmUgdGhlIGNvbXB1dGF0aW9uIiwiQ2FsbGVkIHZpYSBtb2RlbCh4KSwgbm90IG1vZGVsLmZvcndhcmQoeCkiXSxbInBhcmFtZXRlcnMoKSIsIkl0ZXJhdG9yIG92ZXIgYWxsIHRyYWluYWJsZSBwYXJhbXMiLCJvcHRpbWl6ZXIgPSBBZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSkiXSxbInN0YXRlX2RpY3QoKSIsIk9yZGVyZWQgZGljdCBvZiBhbGwgcGFyYW0gdGVuc29ycyIsInRvcmNoLnNhdmUobW9kZWwuc3RhdGVfZGljdCgpLCBwYXRoKSJdLFsibG9hZF9zdGF0ZV9kaWN0KGQpIiwiTG9hZCBzYXZlZCB3ZWlnaHRzIiwibW9kZWwubG9hZF9zdGF0ZV9kaWN0KHRvcmNoLmxvYWQocGF0aCkpIl0sWyJ0byhkZXZpY2UpIiwiTW92ZSBhbGwgcGFyYW1zIHRvIGRldmljZSIsIm1vZGVsLnRvKFx1MDAyN2N1ZGFcdTAwMjcpIG9yIG1vZGVsLmN1ZGEoKSJdLFsidHJhaW4oKSAvIGV2YWwoKSIsIlNldCB0cmFpbmluZyB2cyBpbmZlcmVuY2UgbW9kZSIsIkFmZmVjdHMgRHJvcG91dCBhbmQgQmF0Y2hOb3JtIGJlaGF2aW9yIl0sWyJuYW1lZF9wYXJhbWV0ZXJzKCkiLCJJdGVyYXRvciBvdmVyIChuYW1lLCBwYXJhbSkgcGFpcnMiLCJJbnNwZWN0aW5nIG9yIGZyZWV6aW5nIHNwZWNpZmljIGxheWVycyJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6InNldF90b19ub25lPVRydWUgaW4gemVyb19ncmFkIiwiY29udGVudCI6IlVzaW5nIG9wdGltaXplci56ZXJvX2dyYWQoc2V0X3RvX25vbmU9VHJ1ZSkgc2V0cyBncmFkaWVudCB0ZW5zb3JzIHRvIE5vbmUgaW5zdGVhZCBvZiB6ZXJvaW5nIHRoZW0uIFRoaXMgYXZvaWRzIGFsbG9jYXRpbmcgbWVtb3J5IGZvciBncmFkaWVudHMgdGhhdCB3aWxsIGJlIGltbWVkaWF0ZWx5IG92ZXJ3cml0dGVuLCBzYXZpbmcgMTAtMjAlIEdQVSBtZW1vcnkgaW4gbGFyZ2UgbW9kZWxzLiBJdCBpcyB0aGUgZGVmYXVsdCBpbiByZWNlbnQgUHlUb3JjaCB2ZXJzaW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJ0b3JjaC5UZW5zb3IgPSBOLWRpbSBhcnJheSB3aXRoIGR0eXBlLCBkZXZpY2UsIGFuZCBvcHRpb25hbCBhdXRvZ3JhZCAocmVxdWlyZXNfZ3JhZD1UcnVlIGZvciBsZWFmIHRlbnNvcnMpIiwiYXV0b2dyYWQgYnVpbGRzIHRoZSBjb21wdXRhdGlvbmFsIGdyYXBoIG9uIHRoZSBmb3J3YXJkIHBhc3M7IC5iYWNrd2FyZCgpIGNvbXB1dGVzIGdyYWRpZW50cyB2aWEgcmV2ZXJzZS1tb2RlIEFEIiwibm4uTW9kdWxlIHRyYWNrcyBwYXJhbWV0ZXJzIGF1dG9tYXRpY2FsbHkg4oCUIGltcGxlbWVudCBmb3J3YXJkKCksIHVzZSBNb2R1bGVMaXN0L01vZHVsZURpY3QgZm9yIHN1Ym1vZHVsZXMiLCJEYXRhTG9hZGVyIGhhbmRsZXMgYmF0Y2hpbmcsIHNodWZmbGluZywgYW5kIHBhcmFsbGVsIGxvYWRpbmcg4oCUIHNldCBwaW5fbWVtb3J5PVRydWUgYW5kIG51bV93b3JrZXJzXHUwMDNlMCBmb3IgR1BVIiwiVHJhaW5pbmcgbG9vcCBwYXR0ZXJuOiB6ZXJvX2dyYWQg4oaSIGZvcndhcmQg4oaSIGxvc3Mg4oaSIGJhY2t3YXJkIOKGkiBjbGlwX2dyYWQg4oaSIHN0ZXAg4oaSIHNjaGVkdWxlci5zdGVwIl19XQ=="
---
# PyTorch — Autograd, Tensors, nn.Module, and DataLoader

PyTorch is the dominant deep learning framework for research and increasingly for production. Its core design — eager execution, dynamic graphs, Pythonic API — makes debugging natural and custom architectures straightforward. Understanding the four primitives (tensors, autograd, nn.Module, DataLoader) unlocks everything else.

## Tensors and Data Types

A torch.Tensor is an N-dimensional array backed by a contiguous block of memory, with a dtype (float32, float16, bfloat16, int64, bool), a device (cpu, cuda, mps), and optional autograd tracking via requires_grad. Operations on tensors with requires_grad=True are recorded into a computational graph.

- float32: default dtype for model weights — 32-bit IEEE 754, safe for most operations
- float16: 16-bit reduced precision — faster on tensor cores, risks overflow (max ~65504)
- bfloat16: 16-bit with same exponent range as float32 — preferred for training on A100/H100
- Leaf tensors: tensors created by the user (not by operations) — only these accumulate .grad
- Non-leaf tensors: outputs of operations — their .grad is not retained unless retain_grad() called
- Device movement: tensor.to('cuda'), tensor.cuda(), tensor.cpu() — always synchronous

## Tensors and Autograd from Scratch

The computational graph is built dynamically during the forward pass. Calling .backward() on a scalar traverses this graph in reverse, computing gradients via chain rule and accumulating them in .grad of each leaf tensor.

```python
import torch
import torch.nn as nn

# Basic tensor with gradient tracking
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
W = torch.tensor([[0.5, -0.5], [1.0, 0.3]], requires_grad=True)

# Forward pass — builds computational graph
z = x @ W          # matrix multiply
loss = z.sum()     # scalar loss

# Backward pass — traverses graph, fills .grad
loss.backward()
print('x.grad:', x.grad)   # dl/dx
print('W.grad:', W.grad)   # dl/dW

# Critical: zero gradients before next backward pass
# (gradients accumulate by default — a common bug)
x.grad.zero_()
W.grad.zero_()

# torch.no_grad() for inference — no graph, lower memory
with torch.no_grad():
    z_inf = x @ W
    print('Requires grad (inference):', z_inf.requires_grad)  # False

# Detach a tensor from the graph (used in RL, GAN targets)
z_detached = z.detach()
print('Detached requires grad:', z_detached.requires_grad)  # False
```

## Building Models with nn.Module

nn.Module is the base class for all neural network layers and models. It tracks parameters automatically, supports device movement via .to(), and provides state_dict() for serialization. Every custom layer subclasses nn.Module and implements forward().

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ResidualBlock(nn.Module):
    def __init__(self, dim: int, dropout: float = 0.1):
        super().__init__()
        self.fc1    = nn.Linear(dim, dim * 2)
        self.fc2    = nn.Linear(dim * 2, dim)
        self.norm1  = nn.LayerNorm(dim)
        self.norm2  = nn.LayerNorm(dim)
        self.drop   = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        residual = x
        x = self.norm1(x)
        x = F.gelu(self.fc1(x))
        x = self.drop(x)
        x = self.fc2(x)
        return self.norm2(x + residual)  # residual connection

class TabularMLP(nn.Module):
    def __init__(self, n_in: int, n_out: int, depth: int = 3, width: int = 256):
        super().__init__()
        self.input_proj = nn.Linear(n_in, width)
        self.blocks     = nn.ModuleList([ResidualBlock(width) for _ in range(depth)])
        self.head       = nn.Linear(width, n_out)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.input_proj(x)
        for block in self.blocks:
            x = block(x)
        return self.head(x)

model = TabularMLP(n_in=20, n_out=2)
print(f'Parameters: {sum(p.numel() for p in model.parameters()):,}')
print(model)
```

## Custom Dataset and DataLoader

DataLoader wraps a Dataset, handles batching, shuffling, and parallel loading. Implementing __len__ and __getitem__ is all that is required for a custom Dataset. pin_memory=True and num_workers>0 are key for GPU training throughput.

```python
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
from sklearn.preprocessing import StandardScaler

class TabularDataset(Dataset):
    def __init__(self, X: np.ndarray, y: np.ndarray, scaler=None, fit_scaler=False):
        if scaler is None:
            scaler = StandardScaler()
        if fit_scaler:
            X = scaler.fit_transform(X)
        else:
            X = scaler.transform(X)
        self.X      = torch.FloatTensor(X)
        self.y      = torch.LongTensor(y)
        self.scaler = scaler

    def __len__(self) -> int:
        return len(self.X)

    def __getitem__(self, idx: int):
        return self.X[idx], self.y[idx]

# Usage
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=5000, n_features=20, random_state=42)

train_ds = TabularDataset(X[:4000], y[:4000], fit_scaler=True)
val_ds   = TabularDataset(X[4000:], y[4000:], scaler=train_ds.scaler)

train_loader = DataLoader(train_ds, batch_size=256, shuffle=True,
                          num_workers=0, pin_memory=False)
val_loader   = DataLoader(val_ds,   batch_size=512, shuffle=False)

for X_batch, y_batch in train_loader:
    print(f'Batch shape: {X_batch.shape}, dtype: {X_batch.dtype}')
    break
```

## Complete Training Loop

A production training loop includes: gradient zeroing before each forward pass, model.eval() for validation (disables dropout/BatchNorm), a learning rate scheduler, and early stopping based on validation loss.

```python
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import CosineAnnealingLR

def train_epoch(model, loader, optimizer, criterion, device):
    model.train()
    total_loss, correct, total = 0.0, 0, 0
    for X_batch, y_batch in loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        optimizer.zero_grad(set_to_none=True)  # memory-efficient zero_grad
        logits = model(X_batch)
        loss   = criterion(logits, y_batch)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        total_loss += loss.item() * len(y_batch)
        correct    += (logits.argmax(1) == y_batch).sum().item()
        total      += len(y_batch)
    return total_loss / total, correct / total

@torch.no_grad()
def eval_epoch(model, loader, criterion, device):
    model.eval()  # disables dropout and sets BN to eval mode
    total_loss, correct, total = 0.0, 0, 0
    for X_batch, y_batch in loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        logits = model(X_batch)
        total_loss += criterion(logits, y_batch).item() * len(y_batch)
        correct    += (logits.argmax(1) == y_batch).sum().item()
        total      += len(y_batch)
    return total_loss / total, correct / total
```

---

## Key nn.Module Methods

| Method | Purpose | Common Usage |
| --- | --- | --- |
| forward(x) | Define the computation | Called via model(x), not model.forward(x) |
| parameters() | Iterator over all trainable params | optimizer = Adam(model.parameters()) |
| state_dict() | Ordered dict of all param tensors | torch.save(model.state_dict(), path) |
| load_state_dict(d) | Load saved weights | model.load_state_dict(torch.load(path)) |
| to(device) | Move all params to device | model.to('cuda') or model.cuda() |
| train() / eval() | Set training vs inference mode | Affects Dropout and BatchNorm behavior |
| named_parameters() | Iterator over (name, param) pairs | Inspecting or freezing specific layers |

> **set_to_none=True in zero_grad**: Using optimizer.zero_grad(set_to_none=True) sets gradient tensors to None instead of zeroing them. This avoids allocating memory for gradients that will be immediately overwritten, saving 10-20% GPU memory in large models. It is the default in recent PyTorch versions.

## Key Takeaways

- torch.Tensor = N-dim array with dtype, device, and optional autograd (requires_grad=True for leaf tensors)
- autograd builds the computational graph on the forward pass; .backward() computes gradients via reverse-mode AD
- nn.Module tracks parameters automatically — implement forward(), use ModuleList/ModuleDict for submodules
- DataLoader handles batching, shuffling, and parallel loading — set pin_memory=True and num_workers>0 for GPU
- Training loop pattern: zero_grad → forward → loss → backward → clip_grad → step → scheduler.step

