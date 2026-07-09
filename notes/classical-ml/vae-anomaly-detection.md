---
title: "VAE Anomaly Detection — ELBO-Based Scoring"
slug: "vae-anomaly-detection"
description: "Understand how Variational Autoencoders detect anomalies using the ELBO as a scoring function: reconstruction probability, KL divergence, Monte Carlo importance-sampling estimates of log p(x), and why ELBO outperforms pure reconstruction error for out-of-distribution detection."
tags: ["anomaly-detection", "density-estimation", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmFyaWF0aW9uYWwgQXV0b2VuY29kZXJzIGxlYXJuIGEgcHJvYmFiaWxpc3RpYyBnZW5lcmF0aXZlIG1vZGVsIHAoeCkgYnkgbWF4aW1pc2luZyBhIGxvd2VyIGJvdW5kIG9uIHRoZSBsb2ctbGlrZWxpaG9vZC4gQXQgaW5mZXJlbmNlIHRpbWUgdGhpcyBzYW1lIGJvdW5kIOKAlCB0aGUgRUxCTyDigJQgYmVjb21lcyBhIG5hdHVyYWwgYW5vbWFseSBzY29yZTogbm9ybWFsIHBvaW50cyBhY2hpZXZlIGhpZ2ggRUxCTyB3aGlsZSBvdXQtb2YtZGlzdHJpYnV0aW9uIGlucHV0cyBkbyBub3QuIFVuZGVyc3RhbmRpbmcgdGhlIEVMQk8gZGVjb21wb3NpdGlvbiBpcyBrZXkgdG8gY2hvb3NpbmcgdGhlIHJpZ2h0IHNjb3JpbmcgdmFyaWFudCBhbmQgc2V0dGluZyByZWxpYWJsZSB0aHJlc2hvbGRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBWQUUgR2VuZXJhdGl2ZSBNb2RlbCBhbmQgRUxCTyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFZBRSBtb2RlbHMgZGF0YSBhcyB4IH4gcCh4fHopLCB6IH4gcCh6KSB3aXRoIHAoeik9TigwLEkpLiBCZWNhdXNlIHRoZSB0cnVlIHBvc3RlcmlvciBwKHp8eCkgaXMgaW50cmFjdGFibGUsIHdlIGludHJvZHVjZSBhIHZhcmlhdGlvbmFsIGFwcHJveGltYXRpb24gcSh6fHgpID0gTijOvCh4KSwgz4PCsih4KSkgYW5kIG1heGltaXNlIHRoZSBFdmlkZW5jZSBMb3dlciBCT3VuZDogRUxCTyA9IEVfcVtsb2cgcCh4fHopXSDiiJIgS0wocSh6fHgpIOKAliBwKHopKS4gVGhlIGZpcnN0IHRlcm0gaXMgdGhlIHJlY29uc3RydWN0aW9uIHF1YWxpdHk7IHRoZSBzZWNvbmQgdGVybSBwZW5hbGlzZXMgdGhlIGFwcHJveGltYXRlIHBvc3RlcmlvciBmb3IgZGV2aWF0aW5nIGZyb20gdGhlIHByaW9yLiBUaGUgbmVnYXRpdmUgRUxCTyBpcyB0aGUgdHJhaW5pbmcgbG9zcyBhbmQgYWxzbyB0aGUgYW5vbWFseSBzY29yZTogaGlnaCDiiJJFTEJPIG1lYW5zIHRoZSBwb2ludCBpcyBwb29ybHkgZXhwbGFpbmVkIGJ5IHRoZSBtb2RlbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuXG5jbGFzcyBWQUUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9pbiwgZF9sYXQ9OCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVuYyA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKGRfaW4sIDY0KSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5uLkxpbmVhcig2NCwgMzIpLCBubi5SZUxVKCkpXG4gICAgICAgIHNlbGYubXVfaCA9IG5uLkxpbmVhcigzMiwgZF9sYXQpXG4gICAgICAgIHNlbGYubHZfaCA9IG5uLkxpbmVhcigzMiwgZF9sYXQpXG4gICAgICAgIHNlbGYuZGVjID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoZF9sYXQsIDMyKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5uLkxpbmVhcigzMiwgNjQpLCBubi5SZUxVKCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbm4uTGluZWFyKDY0LCBkX2luKSlcblxuICAgIGRlZiBlbmNvZGUoc2VsZiwgeCk6XG4gICAgICAgIGggPSBzZWxmLmVuYyh4KVxuICAgICAgICByZXR1cm4gc2VsZi5tdV9oKGgpLCBzZWxmLmx2X2goaClcblxuICAgIGRlZiByZXBhcmFtZXRlcml6ZShzZWxmLCBtdSwgbHYpOlxuICAgICAgICByZXR1cm4gbXUgKyB0b3JjaC5leHAoMC41ICogbHYpICogdG9yY2gucmFuZG5fbGlrZShtdSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBtdSwgbHYgPSBzZWxmLmVuY29kZSh4KVxuICAgICAgICByZXR1cm4gc2VsZi5kZWMoc2VsZi5yZXBhcmFtZXRlcml6ZShtdSwgbHYpKSwgbXUsIGx2XG5cbmRlZiBlbGJvX2xvc3MoeCwgeF9oYXQsIG11LCBsdik6XG4gICAgcmVjb24gPSBubi5mdW5jdGlvbmFsLm1zZV9sb3NzKHhfaGF0LCB4LCByZWR1Y3Rpb249XHUwMDI3c3VtXHUwMDI3KVxuICAgIGtsID0gLTAuNSAqIHRvcmNoLnN1bSgxICsgbHYgLSBtdS5wb3coMikgLSBsdi5leHAoKSlcbiAgICByZXR1cm4gcmVjb24gKyBrbCAgIyBuZWdhdGl2ZSBFTEJPXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5YX25vcm1hbCA9IHRvcmNoLnJhbmRuKDgwMCwgMjApXG52YWUgPSBWQUUoZF9pbj0yMClcbm9wdCA9IG9wdGltLkFkYW0odmFlLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbmZvciBlcG9jaCBpbiByYW5nZSgyMCk6XG4gICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgeF9oYXQsIG11LCBsdiA9IHZhZShYX25vcm1hbClcbiAgICBsb3NzID0gZWxib19sb3NzKFhfbm9ybWFsLCB4X2hhdCwgbXUsIGx2KVxuICAgIGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgIGlmIChlcG9jaCArIDEpICUgNSA9PSAwOlxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NoKzE6MmR9IHwgLUVMQk8vbjoge2xvc3MuaXRlbSgpL2xlbihYX25vcm1hbCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFTEJPLUJhc2VkIEFub21hbHkgU2NvcmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXQgaW5mZXJlbmNlIHRoZSBhbm9tYWx5IHNjb3JlIGZvciBwb2ludCB4IGlzIOKIkkVMQk8oeCkgPSBFW+KAlnjiiJJ4zILigJbCsl0gKyBLTChxKHp8eCnigJZwKHopKS4gVGhlIEtMIHRlcm0gbWVhc3VyZXMgd2hldGhlciB0aGUgZW5jb2RlciBtYXBzIHggdG8gYSByZWdpb24gb2YgdGhlIHByaW9yOyBhbm9tYWxpZXMgb2Z0ZW4gcHJvZHVjZSB1bnVzdWFsIGxhdGVudCBjb2RlcyBldmVuIHdoZW4gdGhlIGRlY29kZXIgcmVjb25zdHJ1Y3RzIHRoZW0gcGxhdXNpYmx5LiBBdmVyYWdpbmcgdGhlIHJlY29uc3RydWN0aW9uIGxvc3Mgb3ZlciBtdWx0aXBsZSBwb3N0ZXJpb3Igc2FtcGxlcyByZWR1Y2VzIHZhcmlhbmNlLiBUaGUgcGVyLXNhbXBsZSBFTEJPIHNjb3JlIGNhbiB0aGVuIGJlIHRocmVzaG9sZGVkIHVzaW5nIHRoZSA5NXRoIG9yIDk5dGggcGVyY2VudGlsZSBvZiBzY29yZXMgb24gaGVsZC1vdXQgbm9ybWFsIGRhdGEuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBlbGJvX3Njb3JlKHZhZSwgeCwgbl9zYW1wbGVzPTMwKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdBbm9tYWx5IHNjb3JlID0gcmVjb25zdHJ1Y3Rpb24gZXJyb3IgKyBLTCBkaXZlcmdlbmNlIChuZWdhdGl2ZSBFTEJPKS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICB2YWUuZXZhbCgpXG4gICAgeF90ID0gdG9yY2gudGVuc29yKHgsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG11LCBsdiA9IHZhZS5lbmNvZGUoeF90KVxuICAgICAgICByZWNvbl9zdW0gPSB0b3JjaC56ZXJvcyhsZW4oeF90KSlcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9zYW1wbGVzKTpcbiAgICAgICAgICAgIHogPSB2YWUucmVwYXJhbWV0ZXJpemUobXUsIGx2KVxuICAgICAgICAgICAgeF9oYXQgPSB2YWUuZGVjKHopXG4gICAgICAgICAgICByZWNvbl9zdW0gKz0gKCh4X3QgLSB4X2hhdCkgKiogMikuc3VtKGRpbT0xKVxuICAgICAgICByZWNvbiA9IChyZWNvbl9zdW0gLyBuX3NhbXBsZXMpLm51bXB5KClcbiAgICAgICAga2wgPSAoLTAuNSAqICgxICsgbHYgLSBtdS5wb3coMikgLSBsdi5leHAoKSkuc3VtKGRpbT0xKSkubnVtcHkoKVxuICAgIHJldHVybiByZWNvbiArIGtsXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWF9ub3JtID0gbnAucmFuZG9tLnJhbmRuKDEwMCwgMjApLmFzdHlwZShcdTAwMjdmbG9hdDMyXHUwMDI3KVxuWF9hbm9tID0gKG5wLnJhbmRvbS5yYW5kbigyMCwgMjApICogMyArIDQpLmFzdHlwZShcdTAwMjdmbG9hdDMyXHUwMDI3KVxuc19ub3JtID0gZWxib19zY29yZSh2YWUsIFhfbm9ybSlcbnNfYW5vbSA9IGVsYm9fc2NvcmUodmFlLCBYX2Fub20pXG50aHIgPSBucC5wZXJjZW50aWxlKHNfbm9ybSwgOTUpXG5wcmludChmXHUwMDI3Tm9ybWFsICBtZWFuPXtzX25vcm0ubWVhbigpOi4yZn0gIHA5NT17dGhyOi4yZn1cdTAwMjcpXG5wcmludChmXHUwMDI3QW5vbWFseSBtZWFuPXtzX2Fub20ubWVhbigpOi4yZn0gIGRldGVjdGVkPXsoc19hbm9tIFx1MDAzZSB0aHIpLnN1bSgpfS97bGVuKHNfYW5vbSl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vbnRlIENhcmxvIExvZy1MaWtlbGlob29kIHZpYSBJbXBvcnRhbmNlIFNhbXBsaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgRUxCTyBpcyBhIGxvd2VyIGJvdW5kIG9uIGxvZyBwKHgpLiBBIHRpZ2h0ZXIgZXN0aW1hdGUgdXNlcyBpbXBvcnRhbmNlIHNhbXBsaW5nIChJV0FFKTogbG9nIHAoeCkg4omIIGxvZygxL0sgzqPigpYgd19rKSB3aGVyZSBsb2cgd+KCliA9IGxvZyBwKHh8euKClikgKyBsb2cgcCh64oKWKSDiiJIgbG9nIHEoeuKClnx4KSBhbmQgeuKCliB+IHEoenx4KS4gQXMgS+KGkuKIniB0aGlzIGNvbnZlcmdlcyB0byB0aGUgdHJ1ZSBsb2cgcCh4KS4gVGhlIGFub21hbHkgc2NvcmUgYmVjb21lcyDiiJJsb2cgcCh4KSDigJQgYSBwcmluY2lwbGVkIGxpa2VsaWhvb2QtYmFzZWQgc2NvcmUgdGhhdCBhdm9pZHMgdGhlIEVMQk9cdTAwMjdzIGFwcHJveGltYXRpb24gZXJyb3IsIGF0IHRoZSBjb3N0IG9mIEsgZm9yd2FyZCBwYXNzZXMgcGVyIHBvaW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbWNfbG9nX3B4KHZhZSwgeCwgbl9zYW1wbGVzPTIwMCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3RXN0aW1hdGUgbG9nIHAoeCkgdmlhIGltcG9ydGFuY2Utd2VpZ2h0ZWQgc2FtcGxpbmcuXG4gICAgbG9nIHAoeCkg4omIIGxvZ3N1bWV4cChsb2cgd18xLC4uLixsb2cgd19LKSAtIGxvZyBLXG4gICAgbG9nIHdfayA9IGxvZyBwKHh8el9rKSArIGxvZyBwKHpfaykgLSBsb2cgcSh6X2t8eClcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdcbiAgICB2YWUuZXZhbCgpXG4gICAgeF90ID0gdG9yY2gudGVuc29yKHgsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG11LCBsdiA9IHZhZS5lbmNvZGUoeF90KVxuICAgICAgICBzdGQgPSB0b3JjaC5leHAoMC41ICogbHYpXG4gICAgICAgIGxvZ193cyA9IFtdXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fc2FtcGxlcyk6XG4gICAgICAgICAgICB6ID0gbXUgKyBzdGQgKiB0b3JjaC5yYW5kbl9saWtlKG11KVxuICAgICAgICAgICAgeF9oYXQgPSB2YWUuZGVjKHopXG4gICAgICAgICAgICBsb2dfcHhfeiA9IC0wLjUgKiAoKHhfdCAtIHhfaGF0KSAqKiAyKS5zdW0oZGltPTEpXG4gICAgICAgICAgICBsb2dfcHogICA9IC0wLjUgKiAoeiAqKiAyKS5zdW0oZGltPTEpXG4gICAgICAgICAgICBsb2dfcXpfeCA9IC0wLjUgKiAoKCh6IC0gbXUpIC8gKHN0ZCArIDFlLTgpKSAqKiAyXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICsgMiAqIHRvcmNoLmxvZyhzdGQgKyAxZS04KSkuc3VtKGRpbT0xKVxuICAgICAgICAgICAgbG9nX3dzLmFwcGVuZCgobG9nX3B4X3ogKyBsb2dfcHogLSBsb2dfcXpfeCkudW5zcXVlZXplKDApKVxuICAgICAgICBsb2dfd19zdGFjayA9IHRvcmNoLmNhdChsb2dfd3MsIGRpbT0wKVxuICAgICAgICBsb2dfcHggPSB0b3JjaC5sb2dzdW1leHAobG9nX3dfc3RhY2ssIGRpbT0wKSAtIG5wLmxvZyhuX3NhbXBsZXMpXG4gICAgcmV0dXJuIGxvZ19weC5udW1weSgpXG5cbnNhbXBsZV9uID0gbnAucmFuZG9tLnJhbmRuKDMsIDIwKS5hc3R5cGUoXHUwMDI3ZmxvYXQzMlx1MDAyNylcbnNhbXBsZV9hID0gKG5wLnJhbmRvbS5yYW5kbigzLCAyMCkgKiAzICsgNCkuYXN0eXBlKFx1MDAyN2Zsb2F0MzJcdTAwMjcpXG5scF9uID0gbWNfbG9nX3B4KHZhZSwgc2FtcGxlX24sIG5fc2FtcGxlcz0xMDApXG5scF9hID0gbWNfbG9nX3B4KHZhZSwgc2FtcGxlX2EsIG5fc2FtcGxlcz0xMDApXG5wcmludChcdTAwMjdOb3JtYWwgIGxvZyBwKHgpOlx1MDAyNywgbHBfbi5yb3VuZCgyKSlcbnByaW50KFx1MDAyN0Fub21hbHkgbG9nIHAoeCk6XHUwMDI3LCBscF9hLnJvdW5kKDIpKVxucHJpbnQoXHUwMDI3QW5vbWFseSBzY29yZSAoLWxvZyBwKHgpKTpcdTAwMjcsICgtbHBfYSkucm91bmQoMikpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRUxCTyBTY29yZSB2cyBQdXJlIFJlY29uc3RydWN0aW9uIEVycm9yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQdXJlIHJlY29uc3RydWN0aW9uIGVycm9yIOKAlnjiiJJ4zILigJbCsiBpZ25vcmVzIHRoZSBLTCB0ZXJtIGFuZCB0aGVyZWZvcmUgY2Fubm90IGRldGVjdCBhbm9tYWxpZXMgdGhhdCBoYXBwZW4gdG8gcmVjb25zdHJ1Y3Qgd2VsbCDigJQgYSBjb21tb24gZmFpbHVyZSBtb2RlIHdoZW4gdGhlIGRlY29kZXIgaXMgZXhwcmVzc2l2ZS4gVGhlIEVMQk8gYWxzbyBwZW5hbGlzZXMgdW51c3VhbCBsYXRlbnQgY29kZXMuIEFuIGFub21hbHkgdGhhdCBsaWVzIG91dHNpZGUgdGhlIHByaW9yIHN1cHBvcnQgcHJvZHVjZXMgbGFyZ2UgS0wgZXZlbiB3aXRoIHNtYWxsIHJlY29uc3RydWN0aW9uIGVycm9yLiBFbXBpcmljYWxseSB0aGUgRUxCTyBzY29yZSB5aWVsZHMgaGlnaGVyIEFVUk9DIHRoYW4gcmVjb25zdHJ1Y3Rpb24tb25seSBzY29yaW5nIGFjcm9zcyBtb3N0IGJlbmNobWFya3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuXG5kZWYgcmVjb25fc2NvcmUodmFlLCB4KTpcbiAgICB2YWUuZXZhbCgpXG4gICAgeF90ID0gdG9yY2gudGVuc29yKHgsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG11LCBsdiA9IHZhZS5lbmNvZGUoeF90KVxuICAgICAgICB4X2hhdCA9IHZhZS5kZWMobXUpICAjIHVzZSBwb3N0ZXJpb3IgbWVhblxuICAgIHJldHVybiAoKHhfdCAtIHhfaGF0KSAqKiAyKS5zdW0oZGltPTEpLm51bXB5KClcblxubnAucmFuZG9tLnNlZWQoMClcbm5fbiwgbl9hID0gMjAwLCA1MFxuWF9uID0gbnAucmFuZG9tLnJhbmRuKG5fbiwgMjApLmFzdHlwZShcdTAwMjdmbG9hdDMyXHUwMDI3KVxuWF9hID0gKG5wLnJhbmRvbS5yYW5kbihuX2EsIDIwKSAqIDIuNSArIDMpLmFzdHlwZShcdTAwMjdmbG9hdDMyXHUwMDI3KVxuWF9hbGwgPSBucC52c3RhY2soW1hfbiwgWF9hXSlcbnkgPSBucC5hcnJheShbMF0gKiBuX24gKyBbMV0gKiBuX2EpXG5cbnNfZWxibyAgPSBlbGJvX3Njb3JlKHZhZSwgWF9hbGwsIG5fc2FtcGxlcz0yMClcbnNfcmVjb24gPSByZWNvbl9zY29yZSh2YWUsIFhfYWxsKVxuYXVjX2UgPSByb2NfYXVjX3Njb3JlKHksIHNfZWxibylcbmF1Y19yID0gcm9jX2F1Y19zY29yZSh5LCBzX3JlY29uKVxucHJpbnQoZlx1MDAyN0FVUk9DIEVMQk8gc2NvcmU6ICB7YXVjX2U6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdBVVJPQyBSZWNvbiBvbmx5OiAge2F1Y19yOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3SW1wcm92ZW1lbnQ6ICAgICAgIHthdWNfZSAtIGF1Y19yOisuNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3S0wgdGVybSBjYXRjaGVzIGFub21hbGllcyB3aG9zZSBsYXRlbnQgY29kZXMgZGV2aWF0ZSBmcm9tIHRoZSBwcmlvci5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhyZXNob2xkIFNlbGVjdGlvbiBhbmQgQ2FsaWJyYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNldCB0aGUgYW5vbWFseSB0aHJlc2hvbGQgdXNpbmcgdGhlIGVtcGlyaWNhbCBkaXN0cmlidXRpb24gb2YgRUxCTyBzY29yZXMgb24gYSBoZWxkLW91dCBub3JtYWwgdmFsaWRhdGlvbiBzZXQuIENvbW1vbiBzdHJhdGVnaWVzOiAoMSkgRml4ZWQgcGVyY2VudGlsZSDigJQgZmxhZyBwb2ludHMgYWJvdmUgdGhlIDk1dGggb3IgOTl0aCBwZXJjZW50aWxlIG9mIHZhbGlkYXRpb24gc2NvcmVzOyBjb250cm9scyBmYWxzZS1wb3NpdGl2ZSByYXRlIGRpcmVjdGx5LiAoMikgM8+DIHJ1bGUg4oCUIGZpdCBhIEdhdXNzaWFuIHRvIHZhbGlkYXRpb24gc2NvcmVzIGFuZCBmbGFnIHBvaW50cyBtb3JlIHRoYW4gMyBzdGFuZGFyZCBkZXZpYXRpb25zIGFib3ZlIHRoZSBtZWFuLiAoMykgRXh0cmVtZS12YWx1ZSB0aGVvcnkg4oCUIGZpdCBhIEdQRCB0byB0aGUgdGFpbCBvZiB0aGUgc2NvcmUgZGlzdHJpYnV0aW9uIGZvciBwcmluY2lwbGVkIGV4dHJhcG9sYXRpb24gaW50byBsb3ctZGVuc2l0eSByZWdpb25zLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJDaG9vc2luZyB0aGUgUmlnaHQgU2NvcmUiLCJjb250ZW50IjoiVXNlIOKIkkVMQk8gd2hlbiBzcGVlZCBtYXR0ZXJzIGFuZCBkYXRhIGRpbWVuc2lvbmFsaXR5IGlzIG1vZGVyYXRlLiBVc2UgdGhlIE1DIGltcG9ydGFuY2Utc2FtcGxpbmcgZXN0aW1hdGUgKElXQUUsIEs9MjAwKSB3aGVuIHlvdSBuZWVkIHRoZSB0aWdodGVzdCBwb3NzaWJsZSBib3VuZCBhbmQgY2FuIGFmZm9yZCBLIGZvcndhcmQgcGFzc2VzIHBlciBwb2ludC4gSWYgdGhlIGRlY29kZXIgaXMgdmVyeSBwb3dlcmZ1bCwgd2VpZ2h0IHRoZSBLTCB0ZXJtIG1vcmUgaGVhdmlseSBieSBzZXR0aW5nIM6yIFx1MDAzZSAxIGluIHRoZSDOsi1WQUUgb2JqZWN0aXZlIHRvIHByZXZlbnQgdGhlIHJlY29uc3RydWN0aW9uIHRlcm0gZnJvbSBkb21pbmF0aW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZhcmlhbnRzOiBET05VVCBhbmQgT0MtVkFFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJET05VVCAoWHUgZXQgYWwuLCAyMDE4KSBpcyBhIFZBRS1iYXNlZCBLUEkgYW5vbWFseSBkZXRlY3RvciBmb3IgdGltZS1zZXJpZXM6IGl0IHVzZXMgYSBjb25kaXRpb25hbCBWQUUgb3ZlciBzbGlkaW5nIHdpbmRvd3MgYW5kIHNjb3JlcyBhbm9tYWxpZXMgdmlhIGEgbW9kaWZpZWQgcmVjb25zdHJ1Y3Rpb24gcHJvYmFiaWxpdHkgdGhhdCBhY2NvdW50cyBmb3IgbWlzc2luZyB2YWx1ZXMuIE9DLVZBRSBhZGRzIGEgb25lLWNsYXNzIG9iamVjdGl2ZSB0byB0aGUgRUxCTzogYSBoeXBlcnNwaGVyZSBjb25zdHJhaW50IG9uIHRoZSBsYXRlbnQgc3BhY2UgZm9yY2VzIG5vcm1hbCBkYXRhIHRvIGNsdXN0ZXIgYXJvdW5kIGEgY2VudGVyIGMsIG1ha2luZyB0aGUgbGF0ZW50IEtMIGRpc3RhbmNlIGEgbW9yZSBkaXNjcmltaW5hdGl2ZSBhbm9tYWx5IHNjb3JlLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRE9OVVQ6IGNvbmRpdGlvbmFsIFZBRSBvdmVyIHRpbWUgd2luZG93czsgcmVjb25zdHJ1Y3Rpb24gcHJvYmFiaWxpdHkgYXMgc2NvcmU7IGhhbmRsZXMgbWlzc2luZyB2YWx1ZXMgZXhwbGljaXRseSBkdXJpbmcgdHJhaW5pbmcuIiwiT0MtVkFFOiBhZGRzIOKAls68KHgp4oiSY+KAlsKyIHBlbmFsdHkgdG8gRUxCTzsgbGF0ZW50IGRpc3RhbmNlIGZyb20gYyBiZWNvbWVzIGEgY29tcGxlbWVudGFyeSBhbm9tYWx5IHNjb3JlLiIsIs6yLVZBRSAozrJcdTAwM2UxKTogZGlzZW50YW5nbGVzIGxhdGVudCBmYWN0b3JzIGFuZCBmb3JjZXMgYSB0aWdodGVyIHByaW9yIG1hdGNoOyBjYW4gaW1wcm92ZSBhbm9tYWx5IHNlcGFyYXRpb24gYXQgdGhlIGNvc3Qgb2YgcmVjb25zdHJ1Y3Rpb24gcXVhbGl0eS4iLCJJV0FFOiB0aWdodGVyIEVMQk8gdmlhIGltcG9ydGFuY2Utd2VpZ2h0ZWQgc2FtcGxlczsgYW5vbWFseSBzY29yZSBpcyDiiJJsb2cgcMyCKHgpIHJhdGhlciB0aGFuIOKIkkVMQk87IGNvbXB1dGF0aW9uYWxseSBoZWF2aWVyLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWQUUgQW5vbWFseSBTY29yZSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlNjb3JlIiwiRm9ybXVsYSIsIldoYXQgSXQgQ2FwdHVyZXMiLCJUaHJlc2hvbGQgRWFzZSIsIlJvYnVzdG5lc3MiXSwicm93cyI6W1siUmVjb25zdHJ1Y3Rpb24gZXJyb3IiLCLigJZ44oiSeMyC4oCWwrIiLCJEZWNvZGVyIG1pc21hdGNoIG9ubHkiLCJFYXN5IOKAlCBNU0Ugc2NhbGUiLCJGYWlscyBpZiBkZWNvZGVyIG92ZXJmaXRzIl0sWyJLTCBkaXZlcmdlbmNlIG9ubHkiLCJLTChx4oCWcCkiLCJMYXRlbnQgaXJyZWd1bGFyaXR5IG9ubHkiLCJNb2RlcmF0ZSIsIk1pc3NlcyBzdXJmYWNlIGFub21hbGllcyJdLFsiTmVnYXRpdmUgRUxCTyIsIlJlY29uICsgS0wiLCJCb3RoIHN1cmZhY2UgYW5kIGxhdGVudCIsIkVhc3kg4oCUIHNpbmdsZSBzY2FsYXIiLCJHb29kIGdlbmVyYWwgZGVmYXVsdCJdLFsiUmVjb25zdHJ1Y3Rpb24gcHJvYmFiaWxpdHkiLCJFX3FbbG9nIHAoeHx6KV0iLCJQcm9iYWJpbGlzdGljIHJlY29uIHF1YWxpdHkiLCJSZXF1aXJlcyBub2lzZSBtb2RlbCIsIkJldHRlciBmb3IgaW1hZ2UgZGF0YSJdLFsiTUMgbG9nIHAoeCkgKElXQUUpIiwi4oiSbG9nIHDMgih4KSB2aWEgSVMiLCJUaWdodGVzdCBsaWtlbGlob29kIGJvdW5kIiwiUHJpbmNpcGxlZCBidXQgc2xvdyIsIkJlc3QgYWNjdXJhY3ksIEvDl2Nvc3QiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gcHJhY3RpY2Ugc3RhcnQgd2l0aCB0aGUgbmVnYXRpdmUgRUxCTy4gSWYgcmVjb25zdHJ1Y3Rpb24tcXVhbGl0eSBhbm9tYWxpZXMgZG9taW5hdGUsIHVwd2VpZ2h0IHRoZSByZWNvbnN0cnVjdGlvbiB0ZXJtLiBJZiBsYXRlbnQtc3BhY2UgaXJyZWd1bGFyaXRpZXMgbWF0dGVyIG1vcmUgKGUuZy4sIHNlbWFudGljIE9PRCksIHVwd2VpZ2h0IHRoZSBLTCB0ZXJtIG9yIHVzZSBPQy1WQUUuIFJlc2VydmUgdGhlIElXQUUgZXN0aW1hdGUgZm9yIGhpZ2gtc3Rha2VzIGFwcGxpY2F0aW9ucyB3aGVyZSBhY2N1cmFjeSBqdXN0aWZpZXMgdGhlIGNvbXB1dGF0aW9uYWwgY29zdC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# VAE Anomaly Detection — ELBO-Based Scoring

Variational Autoencoders learn a probabilistic generative model p(x) by maximising a lower bound on the log-likelihood. At inference time this same bound — the ELBO — becomes a natural anomaly score: normal points achieve high ELBO while out-of-distribution inputs do not. Understanding the ELBO decomposition is key to choosing the right scoring variant and setting reliable thresholds.

## The VAE Generative Model and ELBO

The VAE models data as x ~ p(x|z), z ~ p(z) with p(z)=N(0,I). Because the true posterior p(z|x) is intractable, we introduce a variational approximation q(z|x) = N(μ(x), σ²(x)) and maximise the Evidence Lower BOund: ELBO = E_q[log p(x|z)] − KL(q(z|x) ‖ p(z)). The first term is the reconstruction quality; the second term penalises the approximate posterior for deviating from the prior. The negative ELBO is the training loss and also the anomaly score: high −ELBO means the point is poorly explained by the model.

```python
import torch
import torch.nn as nn
import torch.optim as optim

class VAE(nn.Module):
    def __init__(self, d_in, d_lat=8):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(d_in, 64), nn.ReLU(),
                                  nn.Linear(64, 32), nn.ReLU())
        self.mu_h = nn.Linear(32, d_lat)
        self.lv_h = nn.Linear(32, d_lat)
        self.dec = nn.Sequential(nn.Linear(d_lat, 32), nn.ReLU(),
                                  nn.Linear(32, 64), nn.ReLU(),
                                  nn.Linear(64, d_in))

    def encode(self, x):
        h = self.enc(x)
        return self.mu_h(h), self.lv_h(h)

    def reparameterize(self, mu, lv):
        return mu + torch.exp(0.5 * lv) * torch.randn_like(mu)

    def forward(self, x):
        mu, lv = self.encode(x)
        return self.dec(self.reparameterize(mu, lv)), mu, lv

def elbo_loss(x, x_hat, mu, lv):
    recon = nn.functional.mse_loss(x_hat, x, reduction='sum')
    kl = -0.5 * torch.sum(1 + lv - mu.pow(2) - lv.exp())
    return recon + kl  # negative ELBO

torch.manual_seed(0)
X_normal = torch.randn(800, 20)
vae = VAE(d_in=20)
opt = optim.Adam(vae.parameters(), lr=1e-3)
for epoch in range(20):
    opt.zero_grad()
    x_hat, mu, lv = vae(X_normal)
    loss = elbo_loss(X_normal, x_hat, mu, lv)
    loss.backward(); opt.step()
    if (epoch + 1) % 5 == 0:
        print(f'Epoch {epoch+1:2d} | -ELBO/n: {loss.item()/len(X_normal):.4f}')
```

## ELBO-Based Anomaly Scoring

At inference the anomaly score for point x is −ELBO(x) = E[‖x−x̂‖²] + KL(q(z|x)‖p(z)). The KL term measures whether the encoder maps x to a region of the prior; anomalies often produce unusual latent codes even when the decoder reconstructs them plausibly. Averaging the reconstruction loss over multiple posterior samples reduces variance. The per-sample ELBO score can then be thresholded using the 95th or 99th percentile of scores on held-out normal data.

```python
import torch
import numpy as np

def elbo_score(vae, x, n_samples=30):
    '''Anomaly score = reconstruction error + KL divergence (negative ELBO).'''
    vae.eval()
    x_t = torch.tensor(x, dtype=torch.float32)
    with torch.no_grad():
        mu, lv = vae.encode(x_t)
        recon_sum = torch.zeros(len(x_t))
        for _ in range(n_samples):
            z = vae.reparameterize(mu, lv)
            x_hat = vae.dec(z)
            recon_sum += ((x_t - x_hat) ** 2).sum(dim=1)
        recon = (recon_sum / n_samples).numpy()
        kl = (-0.5 * (1 + lv - mu.pow(2) - lv.exp()).sum(dim=1)).numpy()
    return recon + kl

np.random.seed(42)
X_norm = np.random.randn(100, 20).astype('float32')
X_anom = (np.random.randn(20, 20) * 3 + 4).astype('float32')
s_norm = elbo_score(vae, X_norm)
s_anom = elbo_score(vae, X_anom)
thr = np.percentile(s_norm, 95)
print(f'Normal  mean={s_norm.mean():.2f}  p95={thr:.2f}')
print(f'Anomaly mean={s_anom.mean():.2f}  detected={(s_anom > thr).sum()}/{len(s_anom)}')
```

## Monte Carlo Log-Likelihood via Importance Sampling

The ELBO is a lower bound on log p(x). A tighter estimate uses importance sampling (IWAE): log p(x) ≈ log(1/K Σₖ w_k) where log wₖ = log p(x|zₖ) + log p(zₖ) − log q(zₖ|x) and zₖ ~ q(z|x). As K→∞ this converges to the true log p(x). The anomaly score becomes −log p(x) — a principled likelihood-based score that avoids the ELBO's approximation error, at the cost of K forward passes per point.

```python
import torch
import numpy as np

def mc_log_px(vae, x, n_samples=200):
    '''Estimate log p(x) via importance-weighted sampling.
    log p(x) ≈ logsumexp(log w_1,...,log w_K) - log K
    log w_k = log p(x|z_k) + log p(z_k) - log q(z_k|x)
    '''
    vae.eval()
    x_t = torch.tensor(x, dtype=torch.float32)
    with torch.no_grad():
        mu, lv = vae.encode(x_t)
        std = torch.exp(0.5 * lv)
        log_ws = []
        for _ in range(n_samples):
            z = mu + std * torch.randn_like(mu)
            x_hat = vae.dec(z)
            log_px_z = -0.5 * ((x_t - x_hat) ** 2).sum(dim=1)
            log_pz   = -0.5 * (z ** 2).sum(dim=1)
            log_qz_x = -0.5 * (((z - mu) / (std + 1e-8)) ** 2
                                + 2 * torch.log(std + 1e-8)).sum(dim=1)
            log_ws.append((log_px_z + log_pz - log_qz_x).unsqueeze(0))
        log_w_stack = torch.cat(log_ws, dim=0)
        log_px = torch.logsumexp(log_w_stack, dim=0) - np.log(n_samples)
    return log_px.numpy()

sample_n = np.random.randn(3, 20).astype('float32')
sample_a = (np.random.randn(3, 20) * 3 + 4).astype('float32')
lp_n = mc_log_px(vae, sample_n, n_samples=100)
lp_a = mc_log_px(vae, sample_a, n_samples=100)
print('Normal  log p(x):', lp_n.round(2))
print('Anomaly log p(x):', lp_a.round(2))
print('Anomaly score (-log p(x)):', (-lp_a).round(2))
```

## ELBO Score vs Pure Reconstruction Error

Pure reconstruction error ‖x−x̂‖² ignores the KL term and therefore cannot detect anomalies that happen to reconstruct well — a common failure mode when the decoder is expressive. The ELBO also penalises unusual latent codes. An anomaly that lies outside the prior support produces large KL even with small reconstruction error. Empirically the ELBO score yields higher AUROC than reconstruction-only scoring across most benchmarks.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score

def recon_score(vae, x):
    vae.eval()
    x_t = torch.tensor(x, dtype=torch.float32)
    with torch.no_grad():
        mu, lv = vae.encode(x_t)
        x_hat = vae.dec(mu)  # use posterior mean
    return ((x_t - x_hat) ** 2).sum(dim=1).numpy()

np.random.seed(0)
n_n, n_a = 200, 50
X_n = np.random.randn(n_n, 20).astype('float32')
X_a = (np.random.randn(n_a, 20) * 2.5 + 3).astype('float32')
X_all = np.vstack([X_n, X_a])
y = np.array([0] * n_n + [1] * n_a)

s_elbo  = elbo_score(vae, X_all, n_samples=20)
s_recon = recon_score(vae, X_all)
auc_e = roc_auc_score(y, s_elbo)
auc_r = roc_auc_score(y, s_recon)
print(f'AUROC ELBO score:  {auc_e:.4f}')
print(f'AUROC Recon only:  {auc_r:.4f}')
print(f'Improvement:       {auc_e - auc_r:+.4f}')
print('KL term catches anomalies whose latent codes deviate from the prior.')
```

## Threshold Selection and Calibration

Set the anomaly threshold using the empirical distribution of ELBO scores on a held-out normal validation set. Common strategies: (1) Fixed percentile — flag points above the 95th or 99th percentile of validation scores; controls false-positive rate directly. (2) 3σ rule — fit a Gaussian to validation scores and flag points more than 3 standard deviations above the mean. (3) Extreme-value theory — fit a GPD to the tail of the score distribution for principled extrapolation into low-density regions.

> **Choosing the Right Score**: Use −ELBO when speed matters and data dimensionality is moderate. Use the MC importance-sampling estimate (IWAE, K=200) when you need the tightest possible bound and can afford K forward passes per point. If the decoder is very powerful, weight the KL term more heavily by setting β > 1 in the β-VAE objective to prevent the reconstruction term from dominating.

## Variants: DONUT and OC-VAE

DONUT (Xu et al., 2018) is a VAE-based KPI anomaly detector for time-series: it uses a conditional VAE over sliding windows and scores anomalies via a modified reconstruction probability that accounts for missing values. OC-VAE adds a one-class objective to the ELBO: a hypersphere constraint on the latent space forces normal data to cluster around a center c, making the latent KL distance a more discriminative anomaly score.

- DONUT: conditional VAE over time windows; reconstruction probability as score; handles missing values explicitly during training.
- OC-VAE: adds ‖μ(x)−c‖² penalty to ELBO; latent distance from c becomes a complementary anomaly score.
- β-VAE (β>1): disentangles latent factors and forces a tighter prior match; can improve anomaly separation at the cost of reconstruction quality.
- IWAE: tighter ELBO via importance-weighted samples; anomaly score is −log p̂(x) rather than −ELBO; computationally heavier.

## VAE Anomaly Score Comparison

| Score | Formula | What It Captures | Threshold Ease | Robustness |
| --- | --- | --- | --- | --- |
| Reconstruction error | ‖x−x̂‖² | Decoder mismatch only | Easy — MSE scale | Fails if decoder overfits |
| KL divergence only | KL(q‖p) | Latent irregularity only | Moderate | Misses surface anomalies |
| Negative ELBO | Recon + KL | Both surface and latent | Easy — single scalar | Good general default |
| Reconstruction probability | E_q[log p(x|z)] | Probabilistic recon quality | Requires noise model | Better for image data |
| MC log p(x) (IWAE) | −log p̂(x) via IS | Tightest likelihood bound | Principled but slow | Best accuracy, K×cost |

In practice start with the negative ELBO. If reconstruction-quality anomalies dominate, upweight the reconstruction term. If latent-space irregularities matter more (e.g., semantic OOD), upweight the KL term or use OC-VAE. Reserve the IWAE estimate for high-stakes applications where accuracy justifies the computational cost.

---

