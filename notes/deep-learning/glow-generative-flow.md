---
title: "Glow — Generative Flow with Invertible 1×1 Convolutions"
slug: "glow-generative-flow"
description: "Glow (Kingma & Dhariwal 2018) improves RealNVP with learnable 1x1 convolutions (LU decomposition for O(c) log-det), Actnorm (data-dependent scale/bias), and affine coupling layers. Covers multi-scale architecture, latent space manipulation, and attribute arithmetic in z-space."
tags: ["deep-learning", "generative-models", "diffusion-models", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2xvdyAoS2luZ21hIFx1MDAyNiBEaGFyaXdhbCwgMjAxOCkgaXMgYSBnZW5lcmF0aXZlIGZsb3cgdGhhdCBleHRlbmRzIFJlYWxOVlAgd2l0aCB0aHJlZSBpbXByb3ZlbWVudHM6IEFjdG5vcm0gcmVwbGFjZXMgYmF0Y2ggbm9ybWFsaXphdGlvbiwgbGVhcm5hYmxlIGludmVydGlibGUgMcOXMSBjb252b2x1dGlvbnMgcmVwbGFjZSBmaXhlZCBjaGFubmVsIHBlcm11dGF0aW9ucywgYW5kIHRoZSBhZmZpbmUgY291cGxpbmcgbGF5ZXIgaXMgcmV0YWluZWQuIFRvZ2V0aGVyIHRoZXNlIGFsbG93IGV4YWN0IGxpa2VsaWhvb2QgY29tcHV0YXRpb24sIGVmZmljaWVudCBzYW1wbGluZywgYW5kIG1lYW5pbmdmdWwgbGF0ZW50LXNwYWNlIGFyaXRobWV0aWMgc3VjaCBhcyBzbWlsZSDihpIgbm8tc21pbGUgYnkgdmVjdG9yIHN1YnRyYWN0aW9uIGluIHotc3BhY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTm9ybWFsaXppbmcgRmxvd3MgUmVjYXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgbm9ybWFsaXppbmcgZmxvdyBkZWZpbmVzIGEgYmlqZWN0aXZlIG1hcHBpbmcgZjogeCDihpIgeiBiZXR3ZWVuIGRhdGEgc3BhY2UgYW5kIGEgc2ltcGxlIGJhc2UgZGlzdHJpYnV0aW9uICh0eXBpY2FsbHkgTigwLEkpKS4gVGhlIGNoYW5nZS1vZi12YXJpYWJsZXMgZm9ybXVsYSBnaXZlcyBsb2cgcCh4KSA9IGxvZyBwX3ooZih4KSkgKyBsb2d8ZGV0IEpfZnwuIFRyYWluaW5nIG1heGltaXplcyB0aGlzIGxvZy1saWtlbGlob29kLiBUaGUga2V5IGNvbnN0cmFpbnQgaXMgdGhhdCBmIG11c3QgYmUgaW52ZXJ0aWJsZSBhbmQgaXRzIEphY29iaWFuIGRldGVybWluYW50IG11c3QgYmUgdHJhY3RhYmxlLiBHbG93IHN0YWNrcyBLIHN0ZXBzIG9mIGZsb3cgYXQgTCBsZXZlbHMgaW4gYSBtdWx0aS1zY2FsZSBhcmNoaXRlY3R1cmUsIGZhY3RvcmluZyBvdXQgaGFsZiB0aGUgY2hhbm5lbHMgYXQgZWFjaCBsZXZlbCB0byBrZWVwIGNvbXB1dGF0aW9uIG1hbmFnZWFibGUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWN0bm9ybSDigJQgRGF0YS1EZXBlbmRlbnQgSW5pdGlhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFjdG5vcm0gaXMgYSBwZXItY2hhbm5lbCBhZmZpbmUgdHJhbnNmb3JtYXRpb24geiA9IHNjYWxlIOKImCAoeCArIGJpYXMpIHdoZXJlIHNjYWxlIGFuZCBiaWFzIGFyZSBsZWFybmFibGUgcGFyYW1ldGVycyBpbml0aWFsaXplZCBmcm9tIHRoZSBmaXJzdCBiYXRjaCBzbyB0aGF0IHRoZSBvdXRwdXQgaGFzIHplcm8gbWVhbiBhbmQgdW5pdCB2YXJpYW5jZS4gVGhpcyBpcyBhIHZhbGlkIGFsdGVybmF0aXZlIHRvIGJhdGNoIG5vcm1hbGl6YXRpb24gdGhhdCBkb2VzIG5vdCBkZXBlbmQgb24gYmF0Y2ggc3RhdGlzdGljcyBhdCBpbmZlcmVuY2UgdGltZS4gVGhlIGxvZy1kZXRlcm1pbmFudCBpcyBIIMOXIFcgw5cgzqMgbG9nfHNjYWxlX2N8LCBjb21wdXRlZCBpbiBPKGMpIHRpbWUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIEFjdG5vcm0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJEYXRhLWRlcGVuZGVudCBpbml0OiBhZnRlciBmaXJzdCBiYXRjaCwgb3V0cHV0IGhhcyBtZWFuPTAsIHN0ZD0xLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuc2NhbGUgPSBubi5QYXJhbWV0ZXIodG9yY2gub25lcygxLCBjLCAxLCAxKSlcbiAgICAgICAgc2VsZi5iaWFzICA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcygxLCBjLCAxLCAxKSlcbiAgICAgICAgc2VsZi5pbml0aWFsaXplZCA9IEZhbHNlXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIGluaXRpYWxpemUoc2VsZiwgeCk6XG4gICAgICAgIG1lYW4gPSB4Lm1lYW4oWzAsIDIsIDNdLCBrZWVwZGltPVRydWUpXG4gICAgICAgIHN0ZCAgPSB4LnN0ZChbMCwgMiwgM10sICBrZWVwZGltPVRydWUpLmNsYW1wKG1pbj0xZS02KVxuICAgICAgICBzZWxmLmJpYXMuY29weV8oLW1lYW4pXG4gICAgICAgIHNlbGYuc2NhbGUuY29weV8oMS4wIC8gc3RkKVxuICAgICAgICBzZWxmLmluaXRpYWxpemVkID0gVHJ1ZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGlmIG5vdCBzZWxmLmluaXRpYWxpemVkOlxuICAgICAgICAgICAgc2VsZi5pbml0aWFsaXplKHgpXG4gICAgICAgIF8sIF8sIEgsIFcgPSB4LnNoYXBlXG4gICAgICAgIHogPSBzZWxmLnNjYWxlICogKHggKyBzZWxmLmJpYXMpXG4gICAgICAgIGxvZ19kZXQgPSBIICogVyAqIHNlbGYuc2NhbGUuYWJzKCkubG9nKCkuc3VtKClcbiAgICAgICAgcmV0dXJuIHosIGxvZ19kZXRcblxuICAgIGRlZiBpbnZlcnNlKHNlbGYsIHopOlxuICAgICAgICByZXR1cm4geiAvIHNlbGYuc2NhbGUgLSBzZWxmLmJpYXNcblxubGF5ZXIgPSBBY3Rub3JtKDMpXG54ID0gdG9yY2gucmFuZG4oMTYsIDMsIDgsIDgpICogNSArIDJcbnosIGxkID0gbGF5ZXIuZm9yd2FyZCh4KVxucHJpbnQoZlwiQmVmb3JlOiBtZWFuPXt4Lm1lYW4oKTouM2Z9ICBzdGQ9e3guc3RkKCk6LjNmfVwiKVxucHJpbnQoZlwiQWZ0ZXI6ICBtZWFuPXt6Lm1lYW4oKTouM2Z9ICBzdGQ9e3ouc3RkKCk6LjNmfVwiKVxucHJpbnQoZlwiUmVjb25zdHJ1Y3Rpb246IHsoeCAtIGxheWVyLmludmVyc2UoeikpLmFicygpLm1heCgpOi4yZX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnZlcnRpYmxlIDHDlzEgQ29udm9sdXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlYWxOVlAgdXNlcyBmaXhlZCBjaGFubmVsIHBlcm11dGF0aW9ucyAocmV2ZXJzZSBvciBzaHVmZmxlKSBiZXR3ZWVuIGNvdXBsaW5nIGxheWVycy4gR2xvdyBnZW5lcmFsaXplcyB0aGlzIHRvIGEgbGVhcm5lZCBzcXVhcmUgbWF0cml4IFcgYXBwbGllZCBhcyBhIDHDlzEgY29udm9sdXRpb24uIFRoZSBsb2ctZGV0ZXJtaW5hbnQgaXMgSCDDlyBXIMOXIGxvZ3xkZXQgV3wsIHdoaWNoIG5haXZlbHkgY29zdHMgTyhjwrMpLiBUaGUgTFUgZGVjb21wb3NpdGlvbiBXID0gUCBMIFUgcmVkdWNlcyB0aGlzIHRvIE8oYyk6IGxvZ3xkZXQgV3wgPSDOoyBsb2d8ZGlhZyhVKV9pfCwgY29tcHV0ZWQgZnJvbSB0aGUgZGlhZ29uYWwgb2YgVSBhbG9uZS4gUCBpcyBhIGZpeGVkIHBlcm11dGF0aW9uIG1hdHJpeCwgTCBhbmQgVSBhcmUgdHJpYW5ndWxhciB3aXRoIGxlYXJuYWJsZSBlbnRyaWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBJbnZlcnRpYmxlMXgxQ29udihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkxVLWRlY29tcG9zZWQgaW52ZXJ0aWJsZSAxeDEgY29udjogbG9nfGRldCBXfCA9IHN1bShsb2d8ZGlhZyBTfCksIE8oYykuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgVyA9IHRvcmNoLmxpbmFsZy5xcih0b3JjaC5yYW5kbihjLCBjKSlbMF1cbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3UFx1MDAyNywgdG9yY2guZXllKGMpW3RvcmNoLnJhbmRwZXJtKGMpXSlcbiAgICAgICAgc2VsZi5MICAgICA9IG5uLlBhcmFtZXRlcih0b3JjaC50cmlsKFcsIC0xKSArIHRvcmNoLmV5ZShjKSlcbiAgICAgICAgc2VsZi5VICAgICA9IG5uLlBhcmFtZXRlcih0b3JjaC50cml1KFcsICAxKSlcbiAgICAgICAgc2VsZi5sb2dfcyA9IG5uLlBhcmFtZXRlcihXLmRpYWcoKS5hYnMoKS5sb2coKSlcbiAgICAgICAgc2VsZi5zX3NnbiA9IG5uLlBhcmFtZXRlcihXLmRpYWcoKS5zaWduKCksIHJlcXVpcmVzX2dyYWQ9RmFsc2UpXG4gICAgICAgIHNlbGYuYyA9IGNcblxuICAgIGRlZiBfVyhzZWxmKTpcbiAgICAgICAgTCA9IHRvcmNoLnRyaWwoc2VsZi5MLCAtMSkgKyB0b3JjaC5leWUoc2VsZi5jLCBkZXZpY2U9c2VsZi5MLmRldmljZSlcbiAgICAgICAgVSA9IHRvcmNoLnRyaXUoc2VsZi5VLCAgMSkgKyB0b3JjaC5kaWFnKHNlbGYuc19zZ24gKiBzZWxmLmxvZ19zLmV4cCgpKVxuICAgICAgICByZXR1cm4gc2VsZi5QIEAgTCBAIFVcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBCLCBDLCBILCBXID0geC5zaGFwZVxuICAgICAgICB6ID0gRi5jb252MmQoeCwgc2VsZi5fVygpLnZpZXcoQywgQywgMSwgMSkpXG4gICAgICAgIHJldHVybiB6LCBIICogVyAqIHNlbGYubG9nX3Muc3VtKClcblxuICAgIGRlZiBpbnZlcnNlKHNlbGYsIHopOlxuICAgICAgICBXX2ludiA9IHRvcmNoLmxpbmFsZy5pbnYoc2VsZi5fVygpKS52aWV3KHNlbGYuYywgc2VsZi5jLCAxLCAxKVxuICAgICAgICByZXR1cm4gRi5jb252MmQoeiwgV19pbnYpXG5cbmMsIEIsIEggPSA4LCAyLCA0XG5sYXllciA9IEludmVydGlibGUxeDFDb252KGMpXG54ID0gdG9yY2gucmFuZG4oQiwgYywgSCwgSClcbnosIGxkID0gbGF5ZXIuZm9yd2FyZCh4KVxucHJpbnQoZlwiUmVjb25zdHJ1Y3Rpb24gZXJyb3I6IHsoeCAtIGxheWVyLmludmVyc2UoeikpLmFicygpLm1heCgpOi4yZX1cIilcbnByaW50KGZcIkxvZy1kZXQ6IHtsZC5pdGVtKCk6LjRmfVwiKVxucHJpbnQoXCJDb3N0OiBPKGNeMykgbWF0cml4IG11bHRpcGx5IG9uY2UsIE8oYykgbG9nLWRldCBmcm9tIGRpYWdvbmFsIG9mIFNcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZmZpbmUgQ291cGxpbmcgTGF5ZXIgYW5kIEZ1bGwgR2xvdyBTdGVwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgYWZmaW5lIGNvdXBsaW5nIGxheWVyIHNwbGl0cyBjaGFubmVscyBpbnRvIHR3byBoYWx2ZXMgeF9hLCB4X2IuIFRoZSBmaXJzdCBoYWxmIHBhc3NlcyB0aHJvdWdoIHVuY2hhbmdlZDsgYSBzbWFsbCBjb252b2x1dGlvbmFsIG5ldHdvcmsgY29tcHV0ZXMgKGxvZ19zLCB0KSA9IE5OKHhfYSksIGFuZCB4X2IgaXMgdHJhbnNmb3JtZWQgYXMgel9iID0geF9iIOKImCBleHAobG9nX3MpICsgdC4gVGhlIGludmVyc2UgaXMgZXhhY3Q6IHhfYiA9ICh6X2IgLSB0KSDiiJggZXhwKC1sb2dfcykuIE9uZSBHbG93IHN0ZXAgc3RhY2tzOiBBY3Rub3JtIOKGkiBJbnYtMcOXMS1Db252IOKGkiBBZmZpbmUtQ291cGxpbmcsIGVhY2ggY29udHJpYnV0aW5nIHRvIHRoZSB0b3RhbCBsb2ctZGV0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBBZmZpbmVDb3VwbGluZyhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjX2hhbGYsIGhpZGRlbj0xMjgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGNfaGFsZiwgaGlkZGVuLCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQoaGlkZGVuLCBoaWRkZW4sIDEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQoaGlkZGVuLCBjX2hhbGYgKiAyLCAzLCBwYWRkaW5nPTEpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHhhLCB4YiA9IHguY2h1bmsoMiwgZGltPTEpXG4gICAgICAgIGxvZ19zLCB0ID0gc2VsZi5uZXQoeGEpLmNodW5rKDIsIGRpbT0xKVxuICAgICAgICBsb2dfcyA9IGxvZ19zLnRhbmgoKVxuICAgICAgICB6YiA9IHhiICogbG9nX3MuZXhwKCkgKyB0XG4gICAgICAgIHJldHVybiB0b3JjaC5jYXQoW3hhLCB6Yl0sIGRpbT0xKSwgbG9nX3Muc3VtKFsxLCAyLCAzXSlcblxuICAgIGRlZiBpbnZlcnNlKHNlbGYsIHopOlxuICAgICAgICB6YSwgemIgPSB6LmNodW5rKDIsIGRpbT0xKVxuICAgICAgICBsb2dfcywgdCA9IHNlbGYubmV0KHphKS5jaHVuaygyLCBkaW09MSlcbiAgICAgICAgeGIgPSAoemIgLSB0KSAqICgtbG9nX3MudGFuaCgpKS5leHAoKVxuICAgICAgICByZXR1cm4gdG9yY2guY2F0KFt6YSwgeGJdLCBkaW09MSlcblxuY2xhc3MgR2xvd1N0ZXAobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJPbmUgR2xvdyBzdGVwOiBBY3Rub3JtIC1cdTAwM2UgSW52LTF4MS1Db252IC1cdTAwM2UgQWZmaW5lIENvdXBsaW5nLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYWN0bm9ybSAgPSBBY3Rub3JtKGMpXG4gICAgICAgIHNlbGYuaW52MXgxICAgPSBJbnZlcnRpYmxlMXgxQ29udihjKVxuICAgICAgICBzZWxmLmNvdXBsaW5nID0gQWZmaW5lQ291cGxpbmcoYyAvLyAyKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHgsIGxkMSA9IHNlbGYuYWN0bm9ybSh4KVxuICAgICAgICB4LCBsZDIgPSBzZWxmLmludjF4MSh4KVxuICAgICAgICB4LCBsZDMgPSBzZWxmLmNvdXBsaW5nKHgpXG4gICAgICAgIHJldHVybiB4LCBsZDEgKyBsZDIgKyBsZDNcblxuYywgQiwgSCA9IDgsIDQsIDhcbnN0ZXAgPSBHbG93U3RlcChjKVxueCA9IHRvcmNoLnJhbmRuKEIsIGMsIEgsIEgpXG56LCBsb2dfZGV0ID0gc3RlcC5mb3J3YXJkKHgpXG5wcmludChmXCJ4OiB7eC5zaGFwZX0gLVx1MDAzZSB6OiB7ei5zaGFwZX0gIGxvZ19kZXQubWVhbj17bG9nX2RldC5tZWFuKCk6LjNmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik11bHRpLVNjYWxlIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2xvdyB1c2VzIGEgbXVsdGktc2NhbGUgZGVzaWduIHdoZXJlLCBhZnRlciBldmVyeSBMIHN0ZXBzLCBoYWxmIHRoZSBjaGFubmVscyBhcmUgZmFjdG9yZWQgb3V0OiB6X2ZhY3RvcmVkID0geFs6LCA6Yy8vMl0sIHggPSB4WzosIGMvLzI6XS4gVGhlIGZhY3RvcmVkLW91dCBjaGFubmVscyBhcmUgY29tYmluZWQgd2l0aCB0aGUgb3V0cHV0IGF0IHRoZSBlbmQuIFRoaXMgcmVkdWNlcyBzcGF0aWFsIHJlc29sdXRpb24gYW5kIGNoYW5uZWwgY291bnQgYXMgZGVwdGggaW5jcmVhc2VzLCBrZWVwaW5nIG1lbW9yeSBhbmQgY29tcHV0YXRpb24gdHJhY3RhYmxlLiBUaGUgZmFjdG9yZWQtb3V0IHBvcnRpb25zIGZvcm0gaW5kZXBlbmRlbnQgR2F1c3NpYW4gZmFjdG9yczsgdGhlIGZpbmFsIGxvZy1saWtlbGlob29kIHN1bXMgb3ZlciBhbGwgbGV2ZWxzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTGV2ZWwgMDogSyBmbG93IHN0ZXBzIG9uIGZ1bGwgKEMsIEgsIFcpIGZlYXR1cmUgbWFwLCBmYWN0b3Igb3V0IEMvLzIgY2hhbm5lbHMuIiwiTGV2ZWwgMTogSyBmbG93IHN0ZXBzIG9uIChDLy8yLCBILy8yLCBXLy8yKSBhZnRlciBzcXVlZXplLCBmYWN0b3Igb3V0IGhhbGYgYWdhaW4uIiwiTGV2ZWwgTC0xOiBmaW5hbCBsZXZlbCBwcm9jZXNzZXMgc21hbGxlc3Qgc3BhdGlhbCByZXNvbHV0aW9uLCBhbGwgY2hhbm5lbHMgcmV0YWluZWQuIiwiU3F1ZWV6ZSBvcGVyYXRpb246IHJlc2hhcGUgKEMsIEgsIFcpIC1cdTAwM2UgKDRDLCBILzIsIFcvMikgYmVmb3JlIGVhY2ggbmV3IGxldmVsLiIsIkF0IGdlbmVyYXRpb246IHNhbXBsZSBlYWNoIGZhY3RvcmVkIHRlbnNvciBmcm9tIE4oMCwgz4PCsiksIHJ1biBhbGwgaW52ZXJzZSBmbG93cy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGF0ZW50IFNwYWNlIE1hbmlwdWxhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVjYXVzZSBHbG93IGxlYXJucyBhbiBleGFjdCBpbnZlcnRpYmxlIG1hcHBpbmcsIGF0dHJpYnV0ZSBtYW5pcHVsYXRpb24gaXMgcHJlY2lzZTogZW5jb2RlIGEgZGF0YXNldCBvZiBpbWFnZXMsIHNlcGFyYXRlIGJ5IGF0dHJpYnV0ZSBsYWJlbCwgY29tcHV0ZSB0aGUgbWVhbiB6LXZlY3RvciBmb3IgZWFjaCBjbGFzcywgYW5kIHRoZSBkaWZmZXJlbmNlIM60ID0gel9wb3NfbWVhbiAtIHpfbmVnX21lYW4gaXMgYW4gYXR0cmlidXRlIGRpcmVjdGlvbi4gQWRkaW5nIM6xzrQgdG8gYW55IGxhdGVudCBjb2RlIG1vdmVzIHRoZSBpbWFnZSBhbG9uZyB0aGF0IGF0dHJpYnV0ZSB3aGlsZSBwcmVzZXJ2aW5nIG90aGVyIGZlYXR1cmVzLiBUaGlzIHdvcmtzIGZvciBzbWlsZSwgYWdlLCBnZW5kZXIsIGFuZCBvdGhlciBDZWxlYkEgYXR0cmlidXRlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGNvbXB1dGVfYXR0cmlidXRlX2RpcmVjdGlvbih6X3Bvc19saXN0LCB6X25lZ19saXN0KTpcbiAgICBcIlwiXCJNZWFuIGRpZmZlcmVuY2UgaW4gei1zcGFjZSBiZXR3ZWVuIHBvc2l0aXZlIGFuZCBuZWdhdGl2ZSBhdHRyaWJ1dGUgZXhhbXBsZXMuXCJcIlwiXG4gICAgel9wb3MgPSB0b3JjaC5jYXQoel9wb3NfbGlzdCkubWVhbigwKVxuICAgIHpfbmVnID0gdG9yY2guY2F0KHpfbmVnX2xpc3QpLm1lYW4oMClcbiAgICBkZWx0YSA9IHpfcG9zIC0gel9uZWdcbiAgICByZXR1cm4gZGVsdGEgLyBkZWx0YS5ub3JtKCkgICAjIHVuaXQgZGlyZWN0aW9uIHZlY3RvclxuXG5kZWYgYXBwbHlfYXR0cmlidXRlKG1vZGVsX2ludiwgeiwgYXR0cl92ZWMsIHN0cmVuZ3Rocz0oLTIsIC0xLCAwLCAxLCAyKSk6XG4gICAgXCJcIlwiVHJhdmVyc2UgbGF0ZW50IHNwYWNlIGFsb25nIGF0dHJpYnV0ZSBkaXJlY3Rpb24gYXQgbXVsdGlwbGUgc3RyZW5ndGhzLlwiXCJcIlxuICAgIHJlc3VsdHMgPSB7fVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgYWxwaGEgaW4gc3RyZW5ndGhzOlxuICAgICAgICAgICAgel9lZGl0ID0geiArIGFscGhhICogYXR0cl92ZWMudG8oei5kZXZpY2UpXG4gICAgICAgICAgICByZXN1bHRzW2FscGhhXSA9IG1vZGVsX2ludih6X2VkaXQpXG4gICAgcmV0dXJuIHJlc3VsdHNcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5kX3ogPSA1MTJcbnpfcG9zID0gW3RvcmNoLnJhbmRuKDMyLCBkX3opICsgMC41IGZvciBfIGluIHJhbmdlKDMpXVxuel9uZWcgPSBbdG9yY2gucmFuZG4oMzIsIGRfeikgLSAwLjUgZm9yIF8gaW4gcmFuZ2UoMyldXG5hdHRyX3NtaWxlID0gY29tcHV0ZV9hdHRyaWJ1dGVfZGlyZWN0aW9uKHpfcG9zLCB6X25lZylcblxuel90ZXN0ID0gdG9yY2gucmFuZG4oMSwgZF96KVxuZm9yIGFscGhhIGluIFstMi4wLCAwLjAsIDIuMF06XG4gICAgel9lZGl0ID0gel90ZXN0ICsgYWxwaGEgKiBhdHRyX3NtaWxlXG4gICAgZGlzdCA9ICh6X2VkaXQgLSB6X3Rlc3QpLm5vcm0oKS5pdGVtKClcbiAgICBwcmludChmXCJhbHBoYT17YWxwaGE6Ky4xZn0gIHx8el9lZGl0IC0genx8PXtkaXN0Oi4zZn0gIG1lYW49e3pfZWRpdC5tZWFuKCk6LjNmfVwiKVxucHJpbnQoXCJMaW5lYXIgaW50ZXJwb2xhdGlvbiBpbiB6LXNwYWNlIGNvcnJlc3BvbmRzIHRvIHNtb290aCBhdHRyaWJ1dGUgbW9ycGhpbmdcIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlRlbXBlcmF0dXJlIFNjYWxpbmcgYXQgU3ludGhlc2lzIiwiY29udGVudCI6IlNhbXBsaW5nIHogfiBOKDAsIM+DwrIpIHdpdGggz4MgXHUwMDNjIDEgKGUuZy4gz4M9MC43KSBwcm9kdWNlcyBzaGFycGVyLCBtb3JlIHJlYWxpc3RpYyBpbWFnZXMgYXQgdGhlIGNvc3Qgb2YgZGl2ZXJzaXR5LiBUaGUgbW9kZWwgd2FzIHRyYWluZWQgd2l0aCDPgz0xIGJ1dCBpbmZlcmVuY2UgYmVuZWZpdHMgZnJvbSBsb3dlciB0ZW1wZXJhdHVyZS4gVGhpcyBpcyBiZWNhdXNlIHRoZSBtb2RlbCBsZWFybnMgdG8gYXNzaWduIGxvdy1saWtlbGlob29kIHJlZ2lvbnMgdG8gdW5saWtlbHkgYnV0IHN0aWxsIHBsYXVzaWJsZSBkYXRhOyBzYW1wbGluZyBmcm9tIGEgdGlnaHRlciBkaXN0cmlidXRpb24gYXZvaWRzIHRoZXNlIGFydGlmYWN0cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZWFsTlZQIHZzIEdsb3cgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIlJlYWxOVlAiLCJHbG93Il0sInJvd3MiOltbIkNoYW5uZWwgcGVybXV0YXRpb24iLCJGaXhlZCByZXZlcnNlIG9yIHNodWZmbGUiLCJMZWFybmFibGUgMcOXMSBjb252IChXID0gUExVKSJdLFsiTm9ybWFsaXphdGlvbiIsIkJhdGNoIE5vcm0gKGJhdGNoLWRlcGVuZGVudCkiLCJBY3Rub3JtIChkYXRhLWluaXQsIG5vIGJhdGNoIGRlcC4pIl0sWyJMb2ctZGV0IGNvc3QiLCJPKDEpIOKAlCBjb3VwbGluZyBvbmx5IiwiTyhjKSDigJQgZGlhZ29uYWwgb2YgVSBpbiBMVSBkZWNvbXAiXSxbIkJpdHMvZGltIG9uIENlbGViQSAyNTYiLCJ+My40OSIsIn4zLjM1IChpbXByb3ZlZCBieSBsZWFybmFibGUgcGVybSkiXSxbIkxhdGVudCBtYW5pcHVsYXRpb24iLCJBcHByb3hpbWF0ZSAoZml4ZWQgcGVybXV0YXRpb24pIiwiUHJlY2lzZSBhcml0aG1ldGljIGluIHotc3BhY2UiXSxbIk11bHRpLXNjYWxlIiwiWWVzIChmYWN0b3Igb3V0IGhhbGYgcGVyIGxldmVsKSIsIlllcyAoc2FtZSBwYXR0ZXJuLCBtb3JlIGxldmVscykiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN5bnRoZXNpcyBhbmQgSW50ZXJwb2xhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG8gZ2VuZXJhdGUgYW4gaW1hZ2U6IHNhbXBsZSB6IH4gTigwLCDPg8KySSkgYW5kIHBhc3MgdGhyb3VnaCB0aGUgaW52ZXJzZSBmbG93IGbigbvCuSh6KS4gRm9yIGludGVycG9sYXRpb24gYmV0d2VlbiB0d28gaW1hZ2VzIHjigoEsIHjigoI6IGVuY29kZSBib3RoIHRvIHrigoEgPSBmKHjigoEpLCB64oKCID0gZih44oKCKSwgdGhlbiBkZWNvZGUgeijOuykgPSAoMS3Ouyl64oKBICsgzrt64oKCIGZvciDOuyDiiIggWzAsMV0uIEludGVycG9sYXRpb24gaW4gei1zcGFjZSBpcyBsaW5lYXI7IHRoZSByZXN1bHRpbmcgaW1hZ2VzIHNtb290aGx5IHRyYW5zaXRpb24uIFRoaXMgd29ya3MgYmV0dGVyIHRoYW4gcGl4ZWwtc3BhY2UgaW50ZXJwb2xhdGlvbiBiZWNhdXNlIHotc3BhY2UgaGFzIGEgc3RydWN0dXJlZCBHYXVzc2lhbiBnZW9tZXRyeS4ifV0="
---
# Glow — Generative Flow with Invertible 1×1 Convolutions

Glow (Kingma & Dhariwal, 2018) is a generative flow that extends RealNVP with three improvements: Actnorm replaces batch normalization, learnable invertible 1×1 convolutions replace fixed channel permutations, and the affine coupling layer is retained. Together these allow exact likelihood computation, efficient sampling, and meaningful latent-space arithmetic such as smile → no-smile by vector subtraction in z-space.

## Normalizing Flows Recap

A normalizing flow defines a bijective mapping f: x → z between data space and a simple base distribution (typically N(0,I)). The change-of-variables formula gives log p(x) = log p_z(f(x)) + log|det J_f|. Training maximizes this log-likelihood. The key constraint is that f must be invertible and its Jacobian determinant must be tractable. Glow stacks K steps of flow at L levels in a multi-scale architecture, factoring out half the channels at each level to keep computation manageable.

## Actnorm — Data-Dependent Initialization

Actnorm is a per-channel affine transformation z = scale ∘ (x + bias) where scale and bias are learnable parameters initialized from the first batch so that the output has zero mean and unit variance. This is a valid alternative to batch normalization that does not depend on batch statistics at inference time. The log-determinant is H × W × Σ log|scale_c|, computed in O(c) time.

```python
import torch
import torch.nn as nn

class Actnorm(nn.Module):
    """Data-dependent init: after first batch, output has mean=0, std=1."""
    def __init__(self, c):
        super().__init__()
        self.scale = nn.Parameter(torch.ones(1, c, 1, 1))
        self.bias  = nn.Parameter(torch.zeros(1, c, 1, 1))
        self.initialized = False

    @torch.no_grad()
    def initialize(self, x):
        mean = x.mean([0, 2, 3], keepdim=True)
        std  = x.std([0, 2, 3],  keepdim=True).clamp(min=1e-6)
        self.bias.copy_(-mean)
        self.scale.copy_(1.0 / std)
        self.initialized = True

    def forward(self, x):
        if not self.initialized:
            self.initialize(x)
        _, _, H, W = x.shape
        z = self.scale * (x + self.bias)
        log_det = H * W * self.scale.abs().log().sum()
        return z, log_det

    def inverse(self, z):
        return z / self.scale - self.bias

layer = Actnorm(3)
x = torch.randn(16, 3, 8, 8) * 5 + 2
z, ld = layer.forward(x)
print(f"Before: mean={x.mean():.3f}  std={x.std():.3f}")
print(f"After:  mean={z.mean():.3f}  std={z.std():.3f}")
print(f"Reconstruction: {(x - layer.inverse(z)).abs().max():.2e}")
```

## Invertible 1×1 Convolution

RealNVP uses fixed channel permutations (reverse or shuffle) between coupling layers. Glow generalizes this to a learned square matrix W applied as a 1×1 convolution. The log-determinant is H × W × log|det W|, which naively costs O(c³). The LU decomposition W = P L U reduces this to O(c): log|det W| = Σ log|diag(U)_i|, computed from the diagonal of U alone. P is a fixed permutation matrix, L and U are triangular with learnable entries.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class Invertible1x1Conv(nn.Module):
    """LU-decomposed invertible 1x1 conv: log|det W| = sum(log|diag S|), O(c)."""
    def __init__(self, c):
        super().__init__()
        W = torch.linalg.qr(torch.randn(c, c))[0]
        self.register_buffer('P', torch.eye(c)[torch.randperm(c)])
        self.L     = nn.Parameter(torch.tril(W, -1) + torch.eye(c))
        self.U     = nn.Parameter(torch.triu(W,  1))
        self.log_s = nn.Parameter(W.diag().abs().log())
        self.s_sgn = nn.Parameter(W.diag().sign(), requires_grad=False)
        self.c = c

    def _W(self):
        L = torch.tril(self.L, -1) + torch.eye(self.c, device=self.L.device)
        U = torch.triu(self.U,  1) + torch.diag(self.s_sgn * self.log_s.exp())
        return self.P @ L @ U

    def forward(self, x):
        B, C, H, W = x.shape
        z = F.conv2d(x, self._W().view(C, C, 1, 1))
        return z, H * W * self.log_s.sum()

    def inverse(self, z):
        W_inv = torch.linalg.inv(self._W()).view(self.c, self.c, 1, 1)
        return F.conv2d(z, W_inv)

c, B, H = 8, 2, 4
layer = Invertible1x1Conv(c)
x = torch.randn(B, c, H, H)
z, ld = layer.forward(x)
print(f"Reconstruction error: {(x - layer.inverse(z)).abs().max():.2e}")
print(f"Log-det: {ld.item():.4f}")
print("Cost: O(c^3) matrix multiply once, O(c) log-det from diagonal of S")
```

## Affine Coupling Layer and Full Glow Step

The affine coupling layer splits channels into two halves x_a, x_b. The first half passes through unchanged; a small convolutional network computes (log_s, t) = NN(x_a), and x_b is transformed as z_b = x_b ∘ exp(log_s) + t. The inverse is exact: x_b = (z_b - t) ∘ exp(-log_s). One Glow step stacks: Actnorm → Inv-1×1-Conv → Affine-Coupling, each contributing to the total log-det.

```python
import torch
import torch.nn as nn

class AffineCoupling(nn.Module):
    def __init__(self, c_half, hidden=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(c_half, hidden, 3, padding=1), nn.ReLU(),
            nn.Conv2d(hidden, hidden, 1), nn.ReLU(),
            nn.Conv2d(hidden, c_half * 2, 3, padding=1))

    def forward(self, x):
        xa, xb = x.chunk(2, dim=1)
        log_s, t = self.net(xa).chunk(2, dim=1)
        log_s = log_s.tanh()
        zb = xb * log_s.exp() + t
        return torch.cat([xa, zb], dim=1), log_s.sum([1, 2, 3])

    def inverse(self, z):
        za, zb = z.chunk(2, dim=1)
        log_s, t = self.net(za).chunk(2, dim=1)
        xb = (zb - t) * (-log_s.tanh()).exp()
        return torch.cat([za, xb], dim=1)

class GlowStep(nn.Module):
    """One Glow step: Actnorm -> Inv-1x1-Conv -> Affine Coupling."""
    def __init__(self, c):
        super().__init__()
        self.actnorm  = Actnorm(c)
        self.inv1x1   = Invertible1x1Conv(c)
        self.coupling = AffineCoupling(c // 2)

    def forward(self, x):
        x, ld1 = self.actnorm(x)
        x, ld2 = self.inv1x1(x)
        x, ld3 = self.coupling(x)
        return x, ld1 + ld2 + ld3

c, B, H = 8, 4, 8
step = GlowStep(c)
x = torch.randn(B, c, H, H)
z, log_det = step.forward(x)
print(f"x: {x.shape} -> z: {z.shape}  log_det.mean={log_det.mean():.3f}")
```

## Multi-Scale Architecture

Glow uses a multi-scale design where, after every L steps, half the channels are factored out: z_factored = x[:, :c//2], x = x[:, c//2:]. The factored-out channels are combined with the output at the end. This reduces spatial resolution and channel count as depth increases, keeping memory and computation tractable. The factored-out portions form independent Gaussian factors; the final log-likelihood sums over all levels.

- Level 0: K flow steps on full (C, H, W) feature map, factor out C//2 channels.
- Level 1: K flow steps on (C//2, H//2, W//2) after squeeze, factor out half again.
- Level L-1: final level processes smallest spatial resolution, all channels retained.
- Squeeze operation: reshape (C, H, W) -> (4C, H/2, W/2) before each new level.
- At generation: sample each factored tensor from N(0, σ²), run all inverse flows.

## Latent Space Manipulation

Because Glow learns an exact invertible mapping, attribute manipulation is precise: encode a dataset of images, separate by attribute label, compute the mean z-vector for each class, and the difference δ = z_pos_mean - z_neg_mean is an attribute direction. Adding αδ to any latent code moves the image along that attribute while preserving other features. This works for smile, age, gender, and other CelebA attributes.

```python
import torch
import numpy as np

def compute_attribute_direction(z_pos_list, z_neg_list):
    """Mean difference in z-space between positive and negative attribute examples."""
    z_pos = torch.cat(z_pos_list).mean(0)
    z_neg = torch.cat(z_neg_list).mean(0)
    delta = z_pos - z_neg
    return delta / delta.norm()   # unit direction vector

def apply_attribute(model_inv, z, attr_vec, strengths=(-2, -1, 0, 1, 2)):
    """Traverse latent space along attribute direction at multiple strengths."""
    results = {}
    with torch.no_grad():
        for alpha in strengths:
            z_edit = z + alpha * attr_vec.to(z.device)
            results[alpha] = model_inv(z_edit)
    return results

torch.manual_seed(42)
d_z = 512
z_pos = [torch.randn(32, d_z) + 0.5 for _ in range(3)]
z_neg = [torch.randn(32, d_z) - 0.5 for _ in range(3)]
attr_smile = compute_attribute_direction(z_pos, z_neg)

z_test = torch.randn(1, d_z)
for alpha in [-2.0, 0.0, 2.0]:
    z_edit = z_test + alpha * attr_smile
    dist = (z_edit - z_test).norm().item()
    print(f"alpha={alpha:+.1f}  ||z_edit - z||={dist:.3f}  mean={z_edit.mean():.3f}")
print("Linear interpolation in z-space corresponds to smooth attribute morphing")
```

> **Temperature Scaling at Synthesis**: Sampling z ~ N(0, σ²) with σ < 1 (e.g. σ=0.7) produces sharper, more realistic images at the cost of diversity. The model was trained with σ=1 but inference benefits from lower temperature. This is because the model learns to assign low-likelihood regions to unlikely but still plausible data; sampling from a tighter distribution avoids these artifacts.

## RealNVP vs Glow Comparison

| Property | RealNVP | Glow |
| --- | --- | --- |
| Channel permutation | Fixed reverse or shuffle | Learnable 1×1 conv (W = PLU) |
| Normalization | Batch Norm (batch-dependent) | Actnorm (data-init, no batch dep.) |
| Log-det cost | O(1) — coupling only | O(c) — diagonal of U in LU decomp |
| Bits/dim on CelebA 256 | ~3.49 | ~3.35 (improved by learnable perm) |
| Latent manipulation | Approximate (fixed permutation) | Precise arithmetic in z-space |
| Multi-scale | Yes (factor out half per level) | Yes (same pattern, more levels) |

## Synthesis and Interpolation

To generate an image: sample z ~ N(0, σ²I) and pass through the inverse flow f⁻¹(z). For interpolation between two images x₁, x₂: encode both to z₁ = f(x₁), z₂ = f(x₂), then decode z(λ) = (1-λ)z₁ + λz₂ for λ ∈ [0,1]. Interpolation in z-space is linear; the resulting images smoothly transition. This works better than pixel-space interpolation because z-space has a structured Gaussian geometry.

