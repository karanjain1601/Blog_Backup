---
title: "Entity Embeddings — Learning Representations for Categorical Variables"
slug: "entity-embeddings"
description: "Entity embeddings learn dense vector representations for high-cardinality categorical features — capturing similarity structure and dramatically outperforming one-hot encoding."
tags: ["tabular", "deep-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT25lLWhvdCBlbmNvZGluZyBmb3IgaGlnaC1jYXJkaW5hbGl0eSBjYXRlZ29yaWNhbCBjb2x1bW5zIChjaXRpZXMsIHByb2R1Y3RzLCB1c2VycykgcHJvZHVjZXMgZXh0cmVtZWx5IGhpZ2gtZGltZW5zaW9uYWwsIHNwYXJzZSByZXByZXNlbnRhdGlvbnMgd2l0aCBubyBzaW1pbGFyaXR5IHN0cnVjdHVyZS4gRW50aXR5IGVtYmVkZGluZ3MgKEd1byBcdTAwMjYgQmVya2hhaG4gMjAxNiwgcG9wdWxhcml6ZWQgYnkgdGhlIFJvc3NtYW4gS2FnZ2xlIGNvbXBldGl0aW9uIHdpbm5lcikgbGVhcm4gZGVuc2UgdmVjdG9yIHJlcHJlc2VudGF0aW9ucyB0aGF0IGVuY29kZSBzZW1hbnRpYyBzaW1pbGFyaXR5IOKAlCBQYXJpcyBhbmQgTG9uZG9uIGVuZCB1cCBuZWFyYnkgaW4gZW1iZWRkaW5nIHNwYWNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBQcm9ibGVtIHdpdGggT25lLUhvdCBFbmNvZGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgY2F0ZWdvcmljYWwgY29sdW1uIHdpdGggMTAsMDAwIHVuaXF1ZSB2YWx1ZXMgKGUuZy4sIFpJUCBjb2RlcyksIG9uZS1ob3QgZW5jb2RpbmcgY3JlYXRlcyAxMCwwMDAgYmluYXJ5IGZlYXR1cmVzLiBUaGUgcmVwcmVzZW50YXRpb24gaXMgKDEpIHNwYXJzZSwgd2FzdGluZyBtZW1vcnkgYW5kIGNvbXB1dGU7ICgyKSBlcXVhbGx5IGRpc3RhbnQg4oCUIFpJUCBjb2RlIDkwMjEwIGlzIGV4YWN0bHkgYXMgZGlzdGFudCBmcm9tIDkwMjExIGFzIGZyb20gMTAwMDEsIGRlc3BpdGUgYmVpbmcgZ2VvZ3JhcGhpY2FsbHkgYWRqYWNlbnQ7ICgzKSBub3QgbGVhcm5hYmxlIOKAlCB0aGVyZSBpcyBubyBtZWNoYW5pc20gdG8gcHVzaCBzaW1pbGFyIGNhdGVnb3JpZXMgY2xvc2VyIHRvZ2V0aGVyLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRGltZW5zaW9uYWxpdHk6IHx2b2NhYnwgZmVhdHVyZXMgcGVyIGNvbHVtbiDigJQgZ3Jvd3MgbGluZWFybHkgd2l0aCBjYXJkaW5hbGl0eSIsIk5vIHNpbWlsYXJpdHkgc3RydWN0dXJlOiBhbGwgY2F0ZWdvcnkgcGFpcnMgYXJlIGVxdWlkaXN0YW50IGluIEhhbW1pbmcgZGlzdGFuY2UiLCJTcGFyc2UgZ3JhZGllbnRzOiBlYWNoIHRyYWluaW5nIHNhbXBsZSB1cGRhdGVzIG9ubHkgb25lIHBvc2l0aW9uIG9mIGVhY2ggb25lLWhvdCBjb2x1bW4iLCJIZXVyaXN0aWMgZW1iZWRkaW5nIGRpbTogayA9IGNlaWwofHZvY2FifF4wLjI1KSBvciBrID0gbWluKDUwLCB8dm9jYWJ8IC8vIDIpIGFyZSBjb21tb24gY2hvaWNlcyIsIkVuZC10by1lbmQgdHJhaW5pbmc6IGVtYmVkZGluZ3MgYXJlIGxlYXJuZWQgam9pbnRseSB3aXRoIHRoZSBtb2RlbCwgY2FwdHVyaW5nIHRhc2stcmVsZXZhbnQgc2ltaWxhcml0eSJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFbnRpdHkgRW1iZWRkaW5nIExheWVyIGluIFB5VG9yY2gifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuIGVudGl0eSBlbWJlZGRpbmcgaXMgc2ltcGx5IGFuIG5uLkVtYmVkZGluZyBsb29rdXAgdGFibGUuIEdpdmVuIGFuIGludGVnZXIgY2F0ZWdvcnkgaW5kZXgsIGl0IHJldHVybnMgdGhlIGNvcnJlc3BvbmRpbmcgZGVuc2UgdmVjdG9yLiBBbGwgZW1iZWRkaW5nIHZlY3RvcnMgYXJlIHRyYWluZWQgam9pbnRseSB3aXRoIHRoZSByZXN0IG9mIHRoZSBuZXVyYWwgbmV0d29yayB2aWEgYmFja3Byb3BhZ2F0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIFRhYnVsYXJNb2RlbChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIk1peGVkIG1vZGVsOiBlbnRpdHkgZW1iZWRkaW5ncyBmb3IgY2F0ZWdvcmljYWxzICsgTUxQIGZvciBudW1lcmljcy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgY2F0X2RpbXM6IGxpc3QsIGVtYl9kaW1zOiBsaXN0LCBuX2NvbnQ6IGludCxcbiAgICAgICAgICAgICAgICAgaGlkZGVuX3NpemVzOiBsaXN0LCBuX291dDogaW50LCBkcm9wb3V0OiBmbG9hdCA9IDAuMyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICAjIEVudGl0eSBlbWJlZGRpbmcgdGFibGVzOiBvbmUgcGVyIGNhdGVnb3JpY2FsIGNvbHVtblxuICAgICAgICBzZWxmLmVtYmVkZGluZ3MgPSBubi5Nb2R1bGVMaXN0KFtcbiAgICAgICAgICAgIG5uLkVtYmVkZGluZyhuX2NhdHMsIGVtYl9kaW0pXG4gICAgICAgICAgICBmb3Igbl9jYXRzLCBlbWJfZGltIGluIHppcChjYXRfZGltcywgZW1iX2RpbXMpXG4gICAgICAgIF0pXG4gICAgICAgIGVtYl90b3RhbCA9IHN1bShlbWJfZGltcylcbiAgICAgICAgaW5fZGltID0gZW1iX3RvdGFsICsgbl9jb250ICAjIGNvbmNhdCBlbWJlZGRpbmdzICsgbnVtZXJpYyBmZWF0dXJlc1xuXG4gICAgICAgICMgTUxQIG9uIHRvcCBvZiBjb25jYXRlbmF0ZWQgcmVwcmVzZW50YXRpb25cbiAgICAgICAgbGF5ZXJzID0gW11cbiAgICAgICAgZm9yIGggaW4gaGlkZGVuX3NpemVzOlxuICAgICAgICAgICAgbGF5ZXJzICs9IFtubi5MaW5lYXIoaW5fZGltLCBoKSwgbm4uQmF0Y2hOb3JtMWQoaCksXG4gICAgICAgICAgICAgICAgICAgICAgIG5uLlJlTFUoKSwgbm4uRHJvcG91dChkcm9wb3V0KV1cbiAgICAgICAgICAgIGluX2RpbSA9IGhcbiAgICAgICAgbGF5ZXJzLmFwcGVuZChubi5MaW5lYXIoaW5fZGltLCBuX291dCkpXG4gICAgICAgIHNlbGYubWxwID0gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeF9jYXQ6IHRvcmNoLlRlbnNvciwgeF9jb250OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBjYXRfZW1icyA9IFtlbWIoeF9jYXRbOiwgaV0pIGZvciBpLCBlbWIgaW4gZW51bWVyYXRlKHNlbGYuZW1iZWRkaW5ncyldXG4gICAgICAgIHggPSB0b3JjaC5jYXQoY2F0X2VtYnMgKyBbeF9jb250XSwgZGltPTEpXG4gICAgICAgIHJldHVybiBzZWxmLm1scCh4KVxuXG4jIEhldXJpc3RpYzogZW1iZWRkaW5nIGRpbSA9IG1pbig1MCwgY2VpbCh2b2NhYl9zaXplXjAuMjUgKiA2KSlcbmRlZiBnZXRfZW1iX2RpbSh2b2NhYl9zaXplOiBpbnQpIC1cdTAwM2UgaW50OlxuICAgIHJldHVybiBtaW4oNTAsIGludChucC5jZWlsKHZvY2FiX3NpemUgKiogMC4yNSAqIDYpKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWaXN1YWxpemluZyBMZWFybmVkIEVtYmVkZGluZ3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFmdGVyIHRyYWluaW5nLCB0LVNORSBvciBVTUFQIHByb2plY3Rpb24gb2YgZW50aXR5IGVtYmVkZGluZ3MgcmV2ZWFscyB0aGUgbGVhcm5lZCBzaW1pbGFyaXR5IHN0cnVjdHVyZS4gU2ltaWxhciBjYXRlZ29yaWVzIGNsdXN0ZXIgdG9nZXRoZXIgaW4gMkQg4oCUIGEgdmlzdWFsIHNhbml0eSBjaGVjayB0aGF0IHRoZSBlbWJlZGRpbmdzIGFyZSBjYXB0dXJpbmcgbWVhbmluZ2Z1bCByZWxhdGlvbnNoaXBzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5tYW5pZm9sZCBpbXBvcnQgVFNORVxuaW1wb3J0IHRvcmNoXG5cbmRlZiB2aXN1YWxpemVfZW1iZWRkaW5ncyhlbWJlZGRpbmdfbGF5ZXIsIGNhdGVnb3J5X2xhYmVscywgdGl0bGU9XHUwMDI3RW50aXR5IEVtYmVkZGluZ3NcdTAwMjcpOlxuICAgIFwiXCJcIlByb2plY3QgZW50aXR5IGVtYmVkZGluZ3MgdG8gMkQgdmlhIHQtU05FIGFuZCBwbG90LlwiXCJcIlxuICAgIHdlaWdodHMgPSBlbWJlZGRpbmdfbGF5ZXIud2VpZ2h0LmRldGFjaCgpLmNwdSgpLm51bXB5KCkgICMgKHZvY2FiX3NpemUsIGVtYl9kaW0pXG5cbiAgICBpZiB3ZWlnaHRzLnNoYXBlWzFdIFx1MDAzZSAyOlxuICAgICAgICB0c25lID0gVFNORShuX2NvbXBvbmVudHM9MiwgcmFuZG9tX3N0YXRlPTQyLCBwZXJwbGV4aXR5PW1pbigzMCwgbGVuKHdlaWdodHMpLy8zKSlcbiAgICAgICAgY29vcmRzID0gdHNuZS5maXRfdHJhbnNmb3JtKHdlaWdodHMpXG4gICAgZWxzZTpcbiAgICAgICAgY29vcmRzID0gd2VpZ2h0cyAgIyBhbHJlYWR5IDJEXG5cbiAgICBmaWcsIGF4ID0gcGx0LnN1YnBsb3RzKGZpZ3NpemU9KDEwLCA4KSlcbiAgICBheC5zY2F0dGVyKGNvb3Jkc1s6LCAwXSwgY29vcmRzWzosIDFdLCBhbHBoYT0wLjYsIHM9MzApXG5cbiAgICBmb3IgaSwgbGFiZWwgaW4gZW51bWVyYXRlKGNhdGVnb3J5X2xhYmVsc1s6MzBdKTogICMgbGFiZWwgdG9wIDMwXG4gICAgICAgIGF4LmFubm90YXRlKGxhYmVsLCAoY29vcmRzW2ksIDBdLCBjb29yZHNbaSwgMV0pLFxuICAgICAgICAgICAgICAgICAgICBmb250c2l6ZT04LCBhbHBoYT0wLjgpXG5cbiAgICBheC5zZXRfdGl0bGUodGl0bGUpXG4gICAgYXguc2V0X3hsYWJlbChcdTAwMjd0LVNORSBkaW0gMVx1MDAyNylcbiAgICBheC5zZXRfeWxhYmVsKFx1MDAyN3QtU05FIGRpbSAyXHUwMDI3KVxuICAgIHBsdC50aWdodF9sYXlvdXQoKVxuICAgIHBsdC5zYXZlZmlnKFx1MDAyN2VtYmVkZGluZ3NfdHNuZS5wbmdcdTAwMjcsIGRwaT0xNTApXG4gICAgcmV0dXJuIGNvb3JkcyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikh5YnJpZDogRW1iZWRkaW5ncyBhcyBGZWF0dXJlcyBmb3IgWEdCb29zdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBwb3dlcmZ1bCBwYXR0ZXJuICh1c2VkIGJ5IHRoZSBSb3NzbWFuIEthZ2dsZSB3aW5uZXIpOiB0cmFpbiBhbiBlbnRpdHkgZW1iZWRkaW5nIG5ldHdvcmsgZmlyc3QsIGV4dHJhY3QgZW1iZWRkaW5ncywgdGhlbiBmZWVkIHRoZW0gYXMgZGVuc2UgZmVhdHVyZXMgdG8gWEdCb29zdC4gVGhpcyBnaXZlcyB0cmVlIG1vZGVscyB0aGUgYmVuZWZpdCBvZiBsZWFybmVkIGNhdGVnb3JpY2FsIHJlcHJlc2VudGF0aW9ucyB3aXRob3V0IGVuZC10by1lbmQgbmV1cmFsIHRyYWluaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFMb2FkZXIsIFRlbnNvckRhdGFzZXRcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBMYWJlbEVuY29kZXJcbmltcG9ydCB4Z2Jvb3N0IGFzIHhnYlxuXG4jIFN0ZXAgMTogRW5jb2RlIGNhdGVnb3JpY2FscyBhcyBpbnRlZ2Vyc1xuY2l0eV9sZSA9IExhYmVsRW5jb2RlcigpXG5jaXR5X2lkcyA9IGNpdHlfbGUuZml0X3RyYW5zZm9ybShbXHUwMDI3UGFyaXNcdTAwMjcsIFx1MDAyN0xvbmRvblx1MDAyNywgXHUwMDI3UGFyaXNcdTAwMjcsIFx1MDAyN0Jlcmxpblx1MDAyNywgXHUwMDI3TG9uZG9uXHUwMDI3XSlcblxuIyBTdGVwIDI6IFRyYWluIGVtYmVkZGluZyBuZXR3b3JrXG5lbWJlZGRpbmcgPSBubi5FbWJlZGRpbmcobnVtX2VtYmVkZGluZ3M9bGVuKGNpdHlfbGUuY2xhc3Nlc18pLCBlbWJlZGRpbmdfZGltPTgpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKGVtYmVkZGluZy5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5cbiMgKE5vcm1hbGx5OiB0cmFpbiB3aXRoaW4gYSBsYXJnZXIgbW9kZWwgd2l0aCBiYWNrcHJvcCBmcm9tIHRhc2sgbG9zcylcbiMgSGVyZSB3ZSBzaW11bGF0ZSBieSB1c2luZyByYW5kb20gdGFyZ2V0cyBhcyBhIHN0YW5kLWluXG5jaXR5X3RlbnNvciA9IHRvcmNoLkxvbmdUZW5zb3IoY2l0eV9pZHMpXG5mb3IgXyBpbiByYW5nZSgxMDApOlxuICAgIGVtYl9vdXQgPSBlbWJlZGRpbmcoY2l0eV90ZW5zb3IpLm1lYW4oZGltPTApICAjIGFnZ3JlZ2F0ZVxuICAgIGxvc3MgPSAtZW1iX291dC5zdW0oKSAgIyBkdW1teSBsb3NzIGZvciBpbGx1c3RyYXRpb25cbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG5cbiMgU3RlcCAzOiBFeHRyYWN0IGxlYXJuZWQgZW1iZWRkaW5nc1xud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgY2l0eV9lbWJzID0gZW1iZWRkaW5nLndlaWdodC5udW1weSgpICAjIChuX2NpdGllcywgOClcblxucHJpbnQoZlx1MDAyN0VtYmVkZGluZyBtYXRyaXggc2hhcGU6IHtjaXR5X2VtYnMuc2hhcGV9XHUwMDI3KVxucHJpbnQoXHUwMDI3Tm93IHVzZSBjaXR5X2VtYnNbY2l0eV9pZF0gYXMgZGVuc2UgZmVhdHVyZXMgZm9yIFhHQm9vc3RcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaW5nIEVuY29kaW5nIE1ldGhvZHMgb24gSGlnaC1DYXJkaW5hbGl0eSBGZWF0dXJlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT24gYSBoaWdoLWNhcmRpbmFsaXR5IGNvbHVtbiAoMTAwMCB1bmlxdWUgY2F0ZWdvcmllcyksIG9uZS1ob3QgZW5jb2RpbmcgY3JlYXRlcyBhIDEwMDAtY29sdW1uIHNwYXJzZSBtYXRyaXggdGhhdCBvdmVyd2hlbG1zIGFueSBtb2RlbCB3aXRoIG5vaXNlLiBUYXJnZXQgZW5jb2RpbmcgbGVha3MgaWYgbm90IGRvbmUgd2l0aGluIGNyb3NzLXZhbGlkYXRpb24gZm9sZHMuIEVudGl0eSBlbWJlZGRpbmdzIG91dHBlcmZvcm0gYm90aCB3aGVuIHRyYWluZWQgZW5kLXRvLWVuZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgT25lSG90RW5jb2RlclxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgTG9naXN0aWNSZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ucGlwZWxpbmUgaW1wb3J0IFBpcGVsaW5lXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCBjcm9zc192YWxfc2NvcmVcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0Milcbm4sIG5fY2F0cyA9IDIwMDAsIDIwMCAgIyBoaWdoLWNhcmRpbmFsaXR5OiAyMDAgdW5pcXVlIGNhdGVnb3JpZXNcblxuIyBTaW11bGF0ZTogY2F0ZWdvcnkgY29ycmVsYXRlcyB3aXRoIHRhcmdldFxuY2F0X2lkcyA9IHJuZy5pbnRlZ2VycygwLCBuX2NhdHMsIG4pICAgICAgICAgICAgICMgaW50ZWdlciBjYXRlZ29yeSBjb2x1bW5cbmNhdF9lZmZlY3QgPSBybmcubm9ybWFsKDAsIDEsIG5fY2F0cykgICAgICAgICAgICAjIHBlci1jYXRlZ29yeSBlZmZlY3RcbnkgPSAoY2F0X2VmZmVjdFtjYXRfaWRzXSArIHJuZy5ub3JtYWwoMCwgMC41LCBuKSBcdTAwM2UgMCkuYXN0eXBlKGludClcblxuWF9jYXQgPSBjYXRfaWRzLnJlc2hhcGUoLTEsIDEpICAjIChuLCAxKSBpbnRlZ2VyIGNvbHVtblxuXG4jIE1ldGhvZCAxOiBPbmUtaG90IGVuY29kaW5nXG5vbmVfaG90ID0gT25lSG90RW5jb2RlcihzcGFyc2Vfb3V0cHV0PUZhbHNlLCBoYW5kbGVfdW5rbm93bj1cdTAwMjdpZ25vcmVcdTAwMjcpXG5waXBlX29oZSA9IFBpcGVsaW5lKFsoXHUwMDI3ZW5jXHUwMDI3LCBvbmVfaG90KSxcbiAgICAgICAgICAgICAgICAgICAgICAoXHUwMDI3Y2xmXHUwMDI3LCBMb2dpc3RpY1JlZ3Jlc3Npb24obWF4X2l0ZXI9NTAwLCBDPTAuMSkpXSlcbnNjb3Jlc19vaGUgPSBjcm9zc192YWxfc2NvcmUocGlwZV9vaGUsIFhfY2F0LCB5LCBjdj01KS5tZWFuKClcbnByaW50KGZcdTAwMjdPbmUtaG90ICgyMDAgY2F0cyk6IHtzY29yZXNfb2hlOi40Zn1cdTAwMjcpXG5cbiMgTWV0aG9kIDI6IE9yZGluYWwgZW5jb2RpbmcgKHRyZWF0cyBjYXRlZ29yaWVzIGFzIG51bWJlcnMg4oCUIHdyb25nISlcblhfb3JkID0gY2F0X2lkcy5yZXNoYXBlKC0xLCAxKS5hc3R5cGUoZmxvYXQpXG5waXBlX29yZCA9IFBpcGVsaW5lKFsoXHUwMDI3Y2xmXHUwMDI3LCBMb2dpc3RpY1JlZ3Jlc3Npb24obWF4X2l0ZXI9MzAwKSldKVxuc2NvcmVzX29yZCA9IGNyb3NzX3ZhbF9zY29yZShwaXBlX29yZCwgWF9vcmQsIHksIGN2PTUpLm1lYW4oKVxucHJpbnQoZlx1MDAyN09yZGluYWwgKHdyb25nKTogICAge3Njb3Jlc19vcmQ6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN0VudGl0eSBlbWJlZGRpbmdzIHRyYWluZWQgZW5kLXRvLWVuZCB0eXBpY2FsbHkgb3V0cGVyZm9ybSBib3RoXHUwMDI3KSJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDYXRlZ29yaWNhbCBFbmNvZGluZyBNZXRob2RzIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRW5jb2RpbmciLCJNYXggQ2FyZGluYWxpdHkiLCJTaW1pbGFyaXR5IiwiTGVha2FnZSBSaXNrIiwiQmVzdCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJPbmUtaG90IiwiTG93LW1lZGl1bSAoXHUwMDNjNTApIiwiTm9uZSIsIk5vbmUiLCJMb3ctY2FyZGluYWxpdHkgbm9taW5hbHMsIHRyZWUgbW9kZWxzIl0sWyJPcmRpbmFsIiwiQW55IiwiTm9uZSAoYXJiaXRyYXJ5KSIsIk5vbmUiLCJPcmRlcmVkIGNhdGVnb3JpZXMgb25seSJdLFsiVGFyZ2V0IGVuY29kaW5nIiwiQW55IiwiVmlhIHRhcmdldCBjb3JyZWxhdGlvbiIsIkhpZ2ggKG5lZWRzIENWKSIsIkhpZ2gtY2FyZGluYWxpdHkgd2l0aCBzdHJvbmcgdGFyZ2V0IHNpZ25hbCJdLFsiRW50aXR5IGVtYmVkZGluZyIsIkhpZ2ggKDFr4oCTMU0pIiwiTGVhcm5lZCwgdGFzay1yZWxldmFudCIsIk5vbmUiLCJIaWdoLWNhcmRpbmFsaXR5IGluIG5ldXJhbCBtb2RlbHMiXSxbIkNhdEJvb3N0IG5hdGl2ZSIsIlZlcnkgaGlnaCIsIk9yZGVyZWQgdGFyZ2V0IHN0YXRzIiwiTG93IChvcmRlcmVkIGVuY29kaW5nKSIsIkNhdEJvb3N0LWJhc2VkIHBpcGVsaW5lcyJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkVtYmVkZGluZyBEaW1lbnNpb24gSGV1cmlzdGljIiwiY29udGVudCI6IkEgcmVsaWFibGUgcnVsZSBvZiB0aHVtYjogZW1iX2RpbSA9IG1pbig1MCwgY2VpbCh2b2NhYl9zaXplXjAuMjUgKiA2KSkuIFRoaXMgZ2l2ZXMgNiBmb3Igdm9jYWI9MTAsIDE1IGZvciB2b2NhYj0xMDAsIDM3IGZvciB2b2NhYj0xMDAwLCA1MCBmb3Igdm9jYWIgXHUwMDNlPSA1MDAwLiBOZXZlciB1c2UgYSBkaW1lbnNpb24gbGFyZ2VyIHRoYW4gdGhlIHZvY2FidWxhcnkgc2l6ZSDigJQgdGhhdCBpcyB3YXN0ZWZ1bCBhbmQgYWRkcyBubyBleHByZXNzaXZlIHBvd2VyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkVudGl0eSBlbWJlZGRpbmdzIHJlcGxhY2Ugc3BhcnNlIG9uZS1ob3QgdmVjdG9ycyB3aXRoIGRlbnNlIGxlYXJuZWQgcmVwcmVzZW50YXRpb25zIGZvciBjYXRlZ29yaWNhbCBmZWF0dXJlcyIsIlNpbWlsYXIgY2F0ZWdvcmllcyBjbHVzdGVyIHRvZ2V0aGVyIGluIGVtYmVkZGluZyBzcGFjZSDigJQgY2FwdHVyaW5nIGdlb2dyYXBoaWMsIHNlbWFudGljLCBvciBiZWhhdmlvcmFsIHNpbWlsYXJpdHkiLCJSZWNvbW1lbmRlZCBkaW06IG1pbig1MCwgY2VpbCh2b2NhYl4wLjI1IMOXIDYpKSBiYWxhbmNlcyBleHByZXNzaXZpdHkgYW5kIHBhcmFtZXRlciBlZmZpY2llbmN5IiwiRW1iZWRkaW5ncyB0cmFpbmVkIGVuZC10by1lbmQgYXJlIHRhc2stc3BlY2lmaWM7IHRoZXkgY2FuIGFsc28gYmUgcHJlLXRyYW5zZmVycmVkIHRvIHRyZWUgbW9kZWxzIGFzIGRlbnNlIGZlYXR1cmVzIiwiQ2F0Qm9vc3RcdTAwMjdzIG5hdGl2ZSBjYXRlZ29yaWNhbCBoYW5kbGluZyBpcyBjb21wZXRpdGl2ZSB3aXRoIGVudGl0eSBlbWJlZGRpbmdzIGZvciB0cmVlLWJhc2VkIG1vZGVscyJdfV0="
---
# Entity Embeddings — Learning Representations for Categorical Variables

One-hot encoding for high-cardinality categorical columns (cities, products, users) produces extremely high-dimensional, sparse representations with no similarity structure. Entity embeddings (Guo & Berkhahn 2016, popularized by the Rossman Kaggle competition winner) learn dense vector representations that encode semantic similarity — Paris and London end up nearby in embedding space.

## The Problem with One-Hot Encoding

For a categorical column with 10,000 unique values (e.g., ZIP codes), one-hot encoding creates 10,000 binary features. The representation is (1) sparse, wasting memory and compute; (2) equally distant — ZIP code 90210 is exactly as distant from 90211 as from 10001, despite being geographically adjacent; (3) not learnable — there is no mechanism to push similar categories closer together.

- Dimensionality: |vocab| features per column — grows linearly with cardinality
- No similarity structure: all category pairs are equidistant in Hamming distance
- Sparse gradients: each training sample updates only one position of each one-hot column
- Heuristic embedding dim: k = ceil(|vocab|^0.25) or k = min(50, |vocab| // 2) are common choices
- End-to-end training: embeddings are learned jointly with the model, capturing task-relevant similarity

## Entity Embedding Layer in PyTorch

An entity embedding is simply an nn.Embedding lookup table. Given an integer category index, it returns the corresponding dense vector. All embedding vectors are trained jointly with the rest of the neural network via backpropagation.

```python
import torch
import torch.nn as nn
import numpy as np

class TabularModel(nn.Module):
    """Mixed model: entity embeddings for categoricals + MLP for numerics."""
    def __init__(self, cat_dims: list, emb_dims: list, n_cont: int,
                 hidden_sizes: list, n_out: int, dropout: float = 0.3):
        super().__init__()
        # Entity embedding tables: one per categorical column
        self.embeddings = nn.ModuleList([
            nn.Embedding(n_cats, emb_dim)
            for n_cats, emb_dim in zip(cat_dims, emb_dims)
        ])
        emb_total = sum(emb_dims)
        in_dim = emb_total + n_cont  # concat embeddings + numeric features

        # MLP on top of concatenated representation
        layers = []
        for h in hidden_sizes:
            layers += [nn.Linear(in_dim, h), nn.BatchNorm1d(h),
                       nn.ReLU(), nn.Dropout(dropout)]
            in_dim = h
        layers.append(nn.Linear(in_dim, n_out))
        self.mlp = nn.Sequential(*layers)

    def forward(self, x_cat: torch.Tensor, x_cont: torch.Tensor) -> torch.Tensor:
        cat_embs = [emb(x_cat[:, i]) for i, emb in enumerate(self.embeddings)]
        x = torch.cat(cat_embs + [x_cont], dim=1)
        return self.mlp(x)

# Heuristic: embedding dim = min(50, ceil(vocab_size^0.25 * 6))
def get_emb_dim(vocab_size: int) -> int:
    return min(50, int(np.ceil(vocab_size ** 0.25 * 6)))
```

## Visualizing Learned Embeddings

After training, t-SNE or UMAP projection of entity embeddings reveals the learned similarity structure. Similar categories cluster together in 2D — a visual sanity check that the embeddings are capturing meaningful relationships.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import torch

def visualize_embeddings(embedding_layer, category_labels, title='Entity Embeddings'):
    """Project entity embeddings to 2D via t-SNE and plot."""
    weights = embedding_layer.weight.detach().cpu().numpy()  # (vocab_size, emb_dim)

    if weights.shape[1] > 2:
        tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, len(weights)//3))
        coords = tsne.fit_transform(weights)
    else:
        coords = weights  # already 2D

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(coords[:, 0], coords[:, 1], alpha=0.6, s=30)

    for i, label in enumerate(category_labels[:30]):  # label top 30
        ax.annotate(label, (coords[i, 0], coords[i, 1]),
                    fontsize=8, alpha=0.8)

    ax.set_title(title)
    ax.set_xlabel('t-SNE dim 1')
    ax.set_ylabel('t-SNE dim 2')
    plt.tight_layout()
    plt.savefig('embeddings_tsne.png', dpi=150)
    return coords
```

## Hybrid: Embeddings as Features for XGBoost

A powerful pattern (used by the Rossman Kaggle winner): train an entity embedding network first, extract embeddings, then feed them as dense features to XGBoost. This gives tree models the benefit of learned categorical representations without end-to-end neural training.

```python
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb

# Step 1: Encode categoricals as integers
city_le = LabelEncoder()
city_ids = city_le.fit_transform(['Paris', 'London', 'Paris', 'Berlin', 'London'])

# Step 2: Train embedding network
embedding = nn.Embedding(num_embeddings=len(city_le.classes_), embedding_dim=8)
optimizer = torch.optim.Adam(embedding.parameters(), lr=1e-3)

# (Normally: train within a larger model with backprop from task loss)
# Here we simulate by using random targets as a stand-in
city_tensor = torch.LongTensor(city_ids)
for _ in range(100):
    emb_out = embedding(city_tensor).mean(dim=0)  # aggregate
    loss = -emb_out.sum()  # dummy loss for illustration
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Step 3: Extract learned embeddings
with torch.no_grad():
    city_embs = embedding.weight.numpy()  # (n_cities, 8)

print(f'Embedding matrix shape: {city_embs.shape}')
print('Now use city_embs[city_id] as dense features for XGBoost')
```

## Comparing Encoding Methods on High-Cardinality Features

On a high-cardinality column (1000 unique categories), one-hot encoding creates a 1000-column sparse matrix that overwhelms any model with noise. Target encoding leaks if not done within cross-validation folds. Entity embeddings outperform both when trained end-to-end.

```python
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import torch
import torch.nn as nn

rng = np.random.default_rng(42)
n, n_cats = 2000, 200  # high-cardinality: 200 unique categories

# Simulate: category correlates with target
cat_ids = rng.integers(0, n_cats, n)             # integer category column
cat_effect = rng.normal(0, 1, n_cats)            # per-category effect
y = (cat_effect[cat_ids] + rng.normal(0, 0.5, n) > 0).astype(int)

X_cat = cat_ids.reshape(-1, 1)  # (n, 1) integer column

# Method 1: One-hot encoding
one_hot = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
pipe_ohe = Pipeline([('enc', one_hot),
                      ('clf', LogisticRegression(max_iter=500, C=0.1))])
scores_ohe = cross_val_score(pipe_ohe, X_cat, y, cv=5).mean()
print(f'One-hot (200 cats): {scores_ohe:.4f}')

# Method 2: Ordinal encoding (treats categories as numbers — wrong!)
X_ord = cat_ids.reshape(-1, 1).astype(float)
pipe_ord = Pipeline([('clf', LogisticRegression(max_iter=300))])
scores_ord = cross_val_score(pipe_ord, X_ord, y, cv=5).mean()
print(f'Ordinal (wrong):    {scores_ord:.4f}')
print('Entity embeddings trained end-to-end typically outperform both')
```

---

## Categorical Encoding Methods Comparison

| Encoding | Max Cardinality | Similarity | Leakage Risk | Best Use Case |
| --- | --- | --- | --- | --- |
| One-hot | Low-medium (<50) | None | None | Low-cardinality nominals, tree models |
| Ordinal | Any | None (arbitrary) | None | Ordered categories only |
| Target encoding | Any | Via target correlation | High (needs CV) | High-cardinality with strong target signal |
| Entity embedding | High (1k–1M) | Learned, task-relevant | None | High-cardinality in neural models |
| CatBoost native | Very high | Ordered target stats | Low (ordered encoding) | CatBoost-based pipelines |

> **Embedding Dimension Heuristic**: A reliable rule of thumb: emb_dim = min(50, ceil(vocab_size^0.25 * 6)). This gives 6 for vocab=10, 15 for vocab=100, 37 for vocab=1000, 50 for vocab >= 5000. Never use a dimension larger than the vocabulary size — that is wasteful and adds no expressive power.

## Key Takeaways

- Entity embeddings replace sparse one-hot vectors with dense learned representations for categorical features
- Similar categories cluster together in embedding space — capturing geographic, semantic, or behavioral similarity
- Recommended dim: min(50, ceil(vocab^0.25 × 6)) balances expressivity and parameter efficiency
- Embeddings trained end-to-end are task-specific; they can also be pre-transferred to tree models as dense features
- CatBoost's native categorical handling is competitive with entity embeddings for tree-based models

