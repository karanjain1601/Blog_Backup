---
title: "Kernel Density Estimation (KDE) — Bandwidth Selection"
slug: "kernel-density-estimation"
description: "Master kernel density estimation for anomaly detection: the mathematics of p̂(x)=(1/nh)Σ K((x−xᵢ)/h), Silverman's rule of thumb, cross-validation bandwidth selection, the curse of dimensionality, and how log-density thresholding compares to parametric alternatives."
tags: ["anomaly-detection", "density-estimation", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiS2VybmVsIERlbnNpdHkgRXN0aW1hdGlvbiBpcyBhIG5vbi1wYXJhbWV0cmljIG1ldGhvZCB0aGF0IGVzdGltYXRlcyB0aGUgZGVuc2l0eSBwKHgpIGRpcmVjdGx5IGZyb20gZGF0YSB3aXRob3V0IGFzc3VtaW5nIGEgcGFyYW1ldHJpYyBmb3JtLiBUaGUga2V5IGh5cGVycGFyYW1ldGVyIOKAlCBiYW5kd2lkdGggaCDigJQgY29udHJvbHMgdGhlIGJpYXMtdmFyaWFuY2UgdHJhZGVvZmYuIEFub21hbHkgZGV0ZWN0aW9uIHdpdGggS0RFIGlzIHN0cmFpZ2h0Zm9yd2FyZDogY29tcHV0ZSB0aGUgbG9nLWRlbnNpdHkg4oiSbG9nIHDMgih4KSBmb3IgZWFjaCB0ZXN0IHBvaW50IGFuZCBmbGFnIHRob3NlIGJlbG93IGEgdGhyZXNob2xkLiBVbmRlcnN0YW5kaW5nIGJhbmR3aWR0aCBzZWxlY3Rpb24gYW5kIHRoZSBsaW1pdGF0aW9ucyBpbiBoaWdoIGRpbWVuc2lvbnMgaXMgZXNzZW50aWFsIGZvciByZWxpYWJsZSBkZXBsb3ltZW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktERSBGdW5kYW1lbnRhbHMgYW5kIEtlcm5lbCBGdW5jdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBLREUgZXN0aW1hdGUgYXQgcG9pbnQgeCBpcyBwzIIoeCkgPSAoMS9uaCkgzqPhtaIgSygoeOKIknjhtaIpL2gpIHdoZXJlIEsgaXMgYSBrZXJuZWwgZnVuY3Rpb24gc2F0aXNmeWluZyDiiKtLKHUpZHU9MSwgSyh1KeKJpTAsIEsodSk9SyjiiJJ1KS4gVGhlIEdhdXNzaWFuIGtlcm5lbCBLKHUpPSgxL+KImjLPgClleHAo4oiSdcKyLzIpIGlzIG1vc3QgY29tbW9uIGZvciBzbW9vdGggZGVuc2l0aWVzLiBUaGUgYmFuZHdpZHRoIGggaXMgdGhlIHNpbmdsZSBtb3N0IGltcG9ydGFudCB0dW5pbmcgcGFyYW1ldGVyOiB0b28gc21hbGwgKHVuZGVyc21vb3RoaW5nKSBwcm9kdWNlcyBhIHNwaWt5IGRlbnNpdHkgdGhhdCBtZW1vcmlzZXMgbm9pc2U7IHRvbyBsYXJnZSAob3ZlcnNtb290aGluZykgYmx1cnMgZ2VudWluZSBzdHJ1Y3R1cmUgYW5kIG1pc3NlcyBsb2NhbCBhbm9tYWxpZXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHYXVzc2lhbiBrZXJuZWw6IEsodSkgPSAoMS/iiJoyz4ApZXhwKOKIknXCsi8yKSDigJQgaW5maW5pdGVseSBkaWZmZXJlbnRpYWJsZSwgd2lkZWx5IHVzZWQuIiwiRXBhbmVjaG5pa292IGtlcm5lbDogSyh1KSA9IDAuNzUoMeKIknXCsikxKHx1fOKJpDEpIOKAlCBvcHRpbWFsIGluIG1lYW4gaW50ZWdyYXRlZCBzcXVhcmVkIGVycm9yLCBjb21wYWN0IHN1cHBvcnQuIiwiVG9waGF0ICh1bmlmb3JtKSBrZXJuZWw6IEsodSkgPSAwLjXCtzEofHV84omkMSkg4oCUIHNpbXBsZSBoaXN0b2dyYW0tbGlrZSBlc3RpbWF0ZSwgZGlzY29udGludW91cy4iLCJUcmlhbmd1bGFyIGtlcm5lbDogSyh1KSA9ICgx4oiSfHV8KcK3MSh8dXziiaQxKSDigJQgY29udGludW91cyBidXQgbm90IGRpZmZlcmVudGlhYmxlIGF0IDAuIl19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGdhdXNzaWFuX2tlcm5lbCh1KTpcbiAgICByZXR1cm4gbnAuZXhwKC0wLjUgKiB1ICoqIDIpIC8gbnAuc3FydCgyICogbnAucGkpXG5cbmRlZiBrZGVfZGVuc2l0eShYX3RyYWluLCB4X3F1ZXJ5LCBoKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdLREUgZGVuc2l0eSBlc3RpbWF0ZSBhdCBxdWVyeSBwb2ludHMgdXNpbmcgR2F1c3NpYW4ga2VybmVsLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIG4sIGQgPSBYX3RyYWluLnNoYXBlXG4gICAgc2NvcmVzID0gbnAuemVyb3MobGVuKHhfcXVlcnkpKVxuICAgIGZvciBpLCB4cSBpbiBlbnVtZXJhdGUoeF9xdWVyeSk6XG4gICAgICAgIGRpZmZzID0gKFhfdHJhaW4gLSB4cSkgLyBoICAgICAgICAgICMgKG4sIGQpXG4gICAgICAgIGtfdmFscyA9IG5wLnByb2QoZ2F1c3NpYW5fa2VybmVsKGRpZmZzKSwgYXhpcz0xKSAgIyBwcm9kdWN0IGtlcm5lbFxuICAgICAgICBzY29yZXNbaV0gPSBrX3ZhbHMubWVhbigpIC8gKGggKiogZClcbiAgICByZXR1cm4gc2NvcmVzXG5cbm5wLnJhbmRvbS5zZWVkKDApXG5YX3RyYWluID0gbnAuY29uY2F0ZW5hdGUoW1xuICAgIG5wLnJhbmRvbS5yYW5kbigzMDAsIDIpLFxuICAgIG5wLnJhbmRvbS5yYW5kbigxMDAsIDIpICsgWzQsIDFdXG5dKVxuaF9vcHQgPSAxLjA2ICogWF90cmFpbi5zdGQoKSAqIGxlbihYX3RyYWluKSAqKiAoLTEvNSlcblhfcXVlcnkgPSBucC5hcnJheShbWzAuLCAwLl0sIFs0LiwgMS5dLCBbOC4sIDguXV0pXG5kZW5zaXRpZXMgPSBrZGVfZGVuc2l0eShYX3RyYWluLCBYX3F1ZXJ5LCBoPWhfb3B0KVxuZm9yIHhxLCBkZW5zIGluIHppcChYX3F1ZXJ5LCBkZW5zaXRpZXMpOlxuICAgIHByaW50KGZcdTAwMjd4PXt4cX0gIGRlbnNpdHk9e2RlbnM6LjVmfSAgbG9nLWRlbnNpdHk9e25wLmxvZyhkZW5zKzFlLTEyKTouM2Z9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhbmR3aWR0aCBTZWxlY3Rpb24gTWV0aG9kcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhyZWUgbWFpbiBzdHJhdGVnaWVzIGZvciBzZWxlY3RpbmcgaDogKDEpIFNpbHZlcm1hblx1MDAyN3MgcnVsZSBvZiB0aHVtYjogaCA9IDEuMDbCt8+DwrduXnviiJIxLyhkKzQpfSwgb3B0aW1hbCBmb3IgR2F1c3NpYW4gZGF0YSDigJQgZmFzdCBidXQgb3ZlcnNtb290aHMgbXVsdGltb2RhbCBkaXN0cmlidXRpb25zLiAoMikgU2NvdHRcdTAwMjdzIHJ1bGU6IGggPSBuXnviiJIxLyhkKzQpfSB1c2VzIHRoZSBpZGVudGl0eSBjb3ZhcmlhbmNlIOKAlCBlcXVpdmFsZW50IHRvIFNpbHZlcm1hblx1MDAyN3Mgd2l0aCDPgz0xLiAoMykgQ3Jvc3MtdmFsaWRhdGlvbjogbWF4aW1pc2UgbGVhdmUtb25lLW91dCBsb2ctbGlrZWxpaG9vZCBMKGgpID0gzqPhtaIgbG9nIHDMgl974oiSaX0oeOG1oikgd2hlcmUgcMyCX3viiJJpfSBleGNsdWRlcyBwb2ludCBpIOKAlCB0aGUgbW9zdCByb2J1c3QgbWV0aG9kIGJ1dCBPKG7CsikgY29zdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubmVpZ2hib3JzIGltcG9ydCBLZXJuZWxEZW5zaXR5XG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCBHcmlkU2VhcmNoQ1ZcblxubnAucmFuZG9tLnNlZWQoMSlcblggPSBucC5jb25jYXRlbmF0ZShbXG4gICAgbnAucmFuZG9tLnJhbmRuKDIwMCwgMSksXG4gICAgbnAucmFuZG9tLnJhbmRuKDEwMCwgMSkgKiAwLjUgKyAzLjVcbl0pXG5cbiMgU2lsdmVybWFuIHJ1bGVcbmhfc2lsID0gMS4wNiAqIFguc3RkKCkgKiBsZW4oWCkgKiogKC0wLjIpXG5wcmludChmXHUwMDI3U2lsdmVybWFuIGJhbmR3aWR0aDogaCA9IHtoX3NpbDouNGZ9XHUwMDI3KVxuXG4jIENyb3NzLXZhbGlkYXRpb24gZ3JpZCBzZWFyY2hcbmJhbmR3aWR0aHMgPSBucC5sb2dzcGFjZSgtMiwgMSwgMzApXG5ncmlkID0gR3JpZFNlYXJjaENWKFxuICAgIEtlcm5lbERlbnNpdHkoa2VybmVsPVx1MDAyN2dhdXNzaWFuXHUwMDI3KSxcbiAgICBwYXJhbV9ncmlkPXtcdTAwMjdiYW5kd2lkdGhcdTAwMjc6IGJhbmR3aWR0aHN9LFxuICAgIGN2PTUsIHNjb3Jpbmc9XHUwMDI3bmVnX2xvZ19sb3NzXHUwMDI3XG4pXG5ncmlkLmZpdChYKVxuaF9jdiA9IGdyaWQuYmVzdF9wYXJhbXNfW1x1MDAyN2JhbmR3aWR0aFx1MDAyN11cbnByaW50KGZcdTAwMjdDVi1vcHRpbWFsIGJhbmR3aWR0aDogaCA9IHtoX2N2Oi40Zn1cdTAwMjcpXG5cbmtkZSA9IEtlcm5lbERlbnNpdHkoa2VybmVsPVx1MDAyN2dhdXNzaWFuXHUwMDI3LCBiYW5kd2lkdGg9aF9jdikuZml0KFgpXG5YX3Rlc3QgPSBucC5hcnJheShbWy0yLl0sIFswLl0sIFszLjVdLCBbNi5dXSlcbmxvZ19kZW5zID0ga2RlLnNjb3JlX3NhbXBsZXMoWF90ZXN0KVxuZm9yIHgsIGxkIGluIHppcChYX3Rlc3QucmF2ZWwoKSwgbG9nX2RlbnMpOlxuICAgIHByaW50KGZcdTAwMjcgIHg9e3g6NS4xZn0gIGxvZyBwPXtsZDouM2Z9ICBhbm9tYWx5X3Njb3JlPXstbGQ6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgRWZmZWN0IG9mIEJhbmR3aWR0aCBvbiBEZW5zaXR5IEVzdGltYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJhbmR3aWR0aCBkaXJlY3RseSBjb250cm9scyB0aGUgYmlhcy12YXJpYW5jZSB0cmFkZW9mZi4gU21hbGwgaCBtZW1vcmlzZXMgZWFjaCB0cmFpbmluZyBwb2ludCAodmFyaWFuY2UgZG9taW5hdGVzKTsgbGFyZ2UgaCBwcm9kdWNlcyBhIHVuaWZvcm0tbGlrZSBkZW5zaXR5IChiaWFzIGRvbWluYXRlcykuIFRoZSBvcHRpbWFsIGggbWluaW1pc2VzIHRoZSBNZWFuIEludGVncmF0ZWQgU3F1YXJlZCBFcnJvciAoTUlTRSkgPSBFW+KIqyhwzIIoeCniiJJwKHgpKcKyIGR4XS4gRm9yIEdhdXNzaWFuIGRhdGEgdGhlIE1JU0Utb3B0aW1hbCBoIHNjYWxlcyBhcyBuXnviiJI0LyhkKzQpfSwgd2hpY2ggZGVjYXlzIHZlcnkgc2xvd2x5IGluIGhpZ2ggZGltZW5zaW9ucyDigJQgdGhpcyBpcyB0aGUgY3Vyc2Ugb2YgZGltZW5zaW9uYWxpdHkuIFZpc3VhbGlzaW5nIHRoZSBkZW5zaXR5IGZvciBhIHJhbmdlIG9mIGggdmFsdWVzIHJldmVhbHMgdGhlIHRyYWRlb2ZmLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5uZWlnaGJvcnMgaW1wb3J0IEtlcm5lbERlbnNpdHlcblxubnAucmFuZG9tLnNlZWQoMilcblhfMWQgPSBucC5jb25jYXRlbmF0ZShbbnAucmFuZG9tLnJhbmRuKDE1MCksIG5wLnJhbmRvbS5yYW5kbig1MCkqMC40ICsgM10pLnJlc2hhcGUoLTEsMSlcbnhfZ3JpZCA9IG5wLmxpbnNwYWNlKC00LCA2LCAzMDApLnJlc2hhcGUoLTEsIDEpXG5cbnByaW50KFx1MDAyN0JhbmR3aWR0aCBjb21wYXJpc29uIG9uIDFEIGJpbW9kYWwgbWl4dHVyZTpcdTAwMjcpXG5wcmludChmXHUwMDI3ICB7XCJoXCI6XHUwMDNlNn0gIHtcInBlYWsxX2RlbnNcIjpcdTAwM2UxMn0gIHtcInZhbGxleV9kZW5zXCI6XHUwMDNlMTN9ICB7XCJwZWFrMl9kZW5zXCI6XHUwMDNlMTJ9XHUwMDI3KVxuZm9yIGggaW4gWzAuMDUsIDAuMTUsIDAuNSwgMS41LCA0LjBdOlxuICAgIGtkZSA9IEtlcm5lbERlbnNpdHkoYmFuZHdpZHRoPWgsIGtlcm5lbD1cdTAwMjdnYXVzc2lhblx1MDAyNykuZml0KFhfMWQpXG4gICAgbGQgPSBrZGUuc2NvcmVfc2FtcGxlcyh4X2dyaWQpXG4gICAgZGVucyA9IG5wLmV4cChsZClcbiAgICAjIEV2YWx1YXRlIGF0IGtleSBwb2ludHNcbiAgICBwZWFrMSAgPSBucC5leHAoa2RlLnNjb3JlX3NhbXBsZXMoW1swLjBdXSkpWzBdXG4gICAgdmFsbGV5ID0gbnAuZXhwKGtkZS5zY29yZV9zYW1wbGVzKFtbMS44XV0pKVswXVxuICAgIHBlYWsyICA9IG5wLmV4cChrZGUuc2NvcmVfc2FtcGxlcyhbWzMuMF1dKSlbMF1cbiAgICBwcmludChmXHUwMDI3ICB7aDpcdTAwM2U2LjJmfSAge3BlYWsxOlx1MDAzZTEyLjVmfSAge3ZhbGxleTpcdTAwM2UxMy41Zn0gIHtwZWFrMjpcdTAwM2UxMi41Zn1cdTAwMjcpXG5wcmludCgpXG5wcmludChcdTAwMjdTbWFsbCBoOiBzcGlreSAoaGlnaCB2YXJpYW5jZSkuIExhcmdlIGg6IGZsYXQgKGhpZ2ggYmlhcykuXHUwMDI3KVxucHJpbnQoXHUwMDI3Q1Ytc2VsZWN0ZWQgaCBzaG91bGQgcHJlc2VydmUgYm90aCBtb2Rlcy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS0RFIGZvciBBbm9tYWx5IERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEtERSBhbm9tYWx5IHNjb3JlIGlzIOKIkmxvZyBwzIIoeCkuIFBvaW50cyB3aXRoIHZlcnkgbG93IGVzdGltYXRlZCBkZW5zaXR5IGFyZSBmbGFnZ2VkIGFzIGFub21hbGllcy4gVGhlIHRocmVzaG9sZCBpcyBzZXQgYXMgdGhlIM+ELXRoIHF1YW50aWxlIChlLmcuLCA1dGggcGVyY2VudGlsZSkgb2YgbG9nLWRlbnNpdHkgc2NvcmVzIG9uIG5vcm1hbCB0cmFpbmluZyBkYXRhLiBVbmxpa2UgcGFyYW1ldHJpYyBtb2RlbHMsIEtERSBhZGFwdHMgdG8gdGhlIHNoYXBlIG9mIHRoZSBkYXRhIHdpdGhvdXQgYXNzdW1pbmcgR2F1c3NpYW5pdHkg4oCUIHVzZWZ1bCBmb3IgbXVsdGltb2RhbCBvciBoZWF2eS10YWlsZWQgZGlzdHJpYnV0aW9ucy4gVGhlIG1haW4gbGltaXRhdGlvbiBpcyBzY2FsYWJpbGl0eTogZXZhbHVhdGluZyB0aGUgZGVuc2l0eSBhdCBhIHF1ZXJ5IHBvaW50IGNvc3RzIE8obikgb3BlcmF0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubmVpZ2hib3JzIGltcG9ydCBLZXJuZWxEZW5zaXR5XG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgR3JpZFNlYXJjaENWXG5cbm5wLnJhbmRvbS5zZWVkKDMpXG5YX3RyYWluID0gbnAucmFuZG9tLnJhbmRuKDUwMCwgMikgICMgbm9ybWFsIGNsYXNzXG5YX25vcm1hbF90ZXN0ID0gbnAucmFuZG9tLnJhbmRuKDEwMCwgMilcblhfYW5vbWFseSA9IG5wLnJhbmRvbS51bmlmb3JtKC02LCA2LCAoMzAsIDIpKSAgIyB1bmlmb3JtIGFub21hbGllc1xuXG5id3MgPSBucC5sb2dzcGFjZSgtMSwgMSwgMjApXG5rZGUgPSBLZXJuZWxEZW5zaXR5KGtlcm5lbD1cdTAwMjdnYXVzc2lhblx1MDAyNylcbmJ3X2N2ID0gR3JpZFNlYXJjaENWKGtkZSwge1x1MDAyN2JhbmR3aWR0aFx1MDAyNzogYndzfSwgY3Y9NSkuZml0KFhfdHJhaW4pXG5oX2Jlc3QgPSBid19jdi5iZXN0X3BhcmFtc19bXHUwMDI3YmFuZHdpZHRoXHUwMDI3XVxua2RlX2ZpdCA9IEtlcm5lbERlbnNpdHkoYmFuZHdpZHRoPWhfYmVzdCkuZml0KFhfdHJhaW4pXG5cbmxvZ19kX25vcm0gPSBrZGVfZml0LnNjb3JlX3NhbXBsZXMoWF9ub3JtYWxfdGVzdClcbmxvZ19kX2Fub20gPSBrZGVfZml0LnNjb3JlX3NhbXBsZXMoWF9hbm9tYWx5KVxudGhyZXNob2xkID0gbnAucGVyY2VudGlsZShsb2dfZF9ub3JtLCA1KSAgIyA1dGggcGVyY2VudGlsZSBhcyBsb3ctZGVuc2l0eSBjdXRcblxuWF9hbGwgPSBucC52c3RhY2soW1hfbm9ybWFsX3Rlc3QsIFhfYW5vbWFseV0pXG55X2FsbCA9IG5wLmFycmF5KFswXSoxMDAgKyBbMV0qMzApXG5zY29yZXMgPSAta2RlX2ZpdC5zY29yZV9zYW1wbGVzKFhfYWxsKSAgIyBuZWdhdGU6IGhpZ2ggc2NvcmUgPSBhbm9tYWx5XG5hdXJvYyA9IHJvY19hdWNfc2NvcmUoeV9hbGwsIHNjb3JlcylcbnByaW50KGZcdTAwMjdCYW5kd2lkdGggKENWKToge2hfYmVzdDouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0FVUk9DOiB7YXVyb2M6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdOb3JtYWwgbG9nLWRlbnNpdHkgbWVhbjogIHtsb2dfZF9ub3JtLm1lYW4oKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0Fub21hbHkgbG9nLWRlbnNpdHkgbWVhbjoge2xvZ19kX2Fub20ubWVhbigpOi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGl2YXJpYXRlIEtERSBhbmQgdGhlIEN1cnNlIG9mIERpbWVuc2lvbmFsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZC1kaW1lbnNpb25hbCBkYXRhIHRoZSBwcm9kdWN0IGtlcm5lbCBpcyBwzIIoeCkgPSAoMS9uwrdo4bWIKSDOo+G1oiDOoOKxvCBLKCh44rG84oiSeOG1ouKxvCkvaCkuIFRoZSBNSVNFLW9wdGltYWwgYmFuZHdpZHRoIHNjYWxlcyBhcyBo4piFIH4gbl574oiSMS8oZCs0KX0sIG1lYW5pbmcgdGhlIGNvbnZlcmdlbmNlIHJhdGUgb2YgS0RFIGRldGVyaW9yYXRlcyBleHBvbmVudGlhbGx5IHdpdGggZGltZW5zaW9uLiBGb3IgZD0xIHRoZSByYXRlIGlzIG5eezQvNX07IGZvciBkPTEwIGl0IGlzIG5eezQvMTR9IOKJiCBuXnswLjI4Nn0g4oCUIGZhciBzbG93ZXIuIEluIHByYWN0aWNlIEtERSBiZWNvbWVzIHVucmVsaWFibGUgZm9yIGRcdTAwM2U1IHVubGVzcyB0aGUgZWZmZWN0aXZlIGludHJpbnNpYyBkaW1lbnNpb25hbGl0eSBvZiB0aGUgZGF0YSBpcyBtdWNoIGxvd2VyLiBBbHRlcm5hdGl2ZXMgaW5jbHVkZSBHTU0sIG5vcm1hbGl6aW5nIGZsb3dzLCBhbmQgcmFuZG9tLXN1YnNwYWNlIEtERSBlbnNlbWJsZXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJGb3IgZOKJpDM6IEtERSB3aXRoIENWIGJhbmR3aWR0aCBpcyBoaWdobHkgZWZmZWN0aXZlIGFuZCBpbnRlcnByZXRhYmxlLiIsIkZvciAzXHUwMDNjZOKJpDEwOiBjb25zaWRlciBHTU0gb3IgYSBtaXh0dXJlIG9mIGRpYWdvbmFsIEdhdXNzaWFucyDigJQgcGFyYW1ldHJpYyBidXQgZmFzdGVyLiIsIkZvciBkXHUwMDNlMTA6IHVzZSBub3JtYWxpemluZyBmbG93cyAoZXhhY3QgbGlrZWxpaG9vZCkgb3IgaXNvbGF0aW9uLWZvcmVzdC1iYXNlZCBkZW5zaXR5IHByb3hpZXMuIiwiQmFuZHdpZHRoIGRlY2F5OiBo4piFIH4gbl57LTEvKGQrNCl9IOKAlCBkb3VibGUgdGhlIGRpbWVuc2lvbiwgbmVlZCBleHBvbmVudGlhbGx5IG1vcmUgZGF0YSBmb3IgdGhlIHNhbWUgYWNjdXJhY3kuIiwiUmFuZG9tIHN1YnNwYWNlIEtERTogZml0IDFEIG9yIDJEIEtERSBvbiByYW5kb20gcHJvamVjdGlvbnMgYW5kIGFnZ3JlZ2F0ZSDigJQgc2NhbGVzIGJldHRlciB0aGFuIGZ1bGwtZGltZW5zaW9uYWwgS0RFLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZW5zaXR5IEVzdGltYXRvciBDb21wYXJpc29uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJLREUgU2NhbGFiaWxpdHkiLCJjb250ZW50IjoiS0RFIGRlbnNpdHkgZXZhbHVhdGlvbiBpcyBPKG7Ct2QpIHBlciBxdWVyeSDigJQgZXhwZW5zaXZlIGZvciBsYXJnZSB0cmFpbmluZyBzZXRzLiBVc2UgYSBiYWxsLXRyZWUgb3IgS0QtdHJlZSBpbmRleCAoc2tsZWFybiBLZXJuZWxEZW5zaXR5IHVzZXMgdGhlc2UgYXV0b21hdGljYWxseSkgdG8gcmVkdWNlIHF1ZXJ5IGNvc3QgdG8gTyhkwrdsb2cgbikgZm9yIGxvdyBkaW1lbnNpb25zLiBGb3Igblx1MDAzZTEwMEsgb3IgZFx1MDAzZTEwLCBHTU0gb3Igbm9ybWFsaXppbmcgZmxvd3Mgd2lsbCBiZSBmYXN0ZXIgYW5kIG1vcmUgYWNjdXJhdGUuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlBhcmFtZXRyaWMiLCJIaWdoLWRpbSIsIlRyYWluaW5nIENvc3QiLCJBbm9tYWx5IFNjb3JlIiwiSW50ZXJwcmV0YWJsZSJdLCJyb3dzIjpbWyJLREUiLCJObyIsIlBvb3IgKGRcdTAwM2U1KSIsIk8obsK3ZCkgZml0LCBPKG4pIHF1ZXJ5Iiwi4oiSbG9nIHDMgih4KSIsIlllcyDigJQgZGVuc2l0eSBwbG90Il0sWyJHTU0iLCJZZXMgKG1peHR1cmUpIiwiTW9kZXJhdGUgKGRpYWdvbmFsKSIsIkVNLCBPKG7Ct2vCt2QpIHBlciBpdGVyIiwi4oiSbG9nIHBfR01NKHgpIiwiWWVzIOKAlCBjb21wb25lbnRzIl0sWyJJc29sYXRpb24gRm9yZXN0IiwiTm8gKHRyZWUpIiwiR29vZCIsIk8obsK3bG9nIG4pIiwiTWVhbiBwYXRoIGxlbmd0aCIsIlBhcnRpYWwiXSxbIk9DLVNWTSIsIk5vIChrZXJuZWwpIiwiUG9vciIsIk8obsKyKeKAk08obsKzKSIsIlNpZ25lZCBkaXN0YW5jZSIsIk5vIl0sWyJOb3JtYWxpemluZyBGbG93IiwiU2VtaSAoYmlqZWN0aXZlIE5OKSIsIkdvb2QiLCJPKG7Ct2Vwb2Noc8K3ZCkiLCLiiJJsb2cgcF9mbG93KHgpIiwiTm8g4oCUIGJsYWNrLWJveCJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJLREUgZXhjZWxzIGluIGxvdyB0byBtb2RlcmF0ZSBkaW1lbnNpb25zIHdpdGggc21hbGwgdG8gbWVkaXVtIGRhdGFzZXRzIHdoZXJlIGludGVycHJldGFiaWxpdHkgbWF0dGVycy4gRm9yIHByb2R1Y3Rpb24gYW5vbWFseSBkZXRlY3Rpb24gYXQgc2NhbGUsIGNvbWJpbmUgS0RFLWJhc2VkIHRocmVzaG9sZHMgb24gbG93LWRpbWVuc2lvbmFsIGZlYXR1cmUgcHJvamVjdGlvbnMgd2l0aCBmYXN0ZXIgcGFyYW1ldHJpYyBhbHRlcm5hdGl2ZXMgZm9yIGhpZ2gtZGltZW5zaW9uYWwgcmF3IGlucHV0IHNwYWNlcy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Kernel Density Estimation (KDE) — Bandwidth Selection

Kernel Density Estimation is a non-parametric method that estimates the density p(x) directly from data without assuming a parametric form. The key hyperparameter — bandwidth h — controls the bias-variance tradeoff. Anomaly detection with KDE is straightforward: compute the log-density −log p̂(x) for each test point and flag those below a threshold. Understanding bandwidth selection and the limitations in high dimensions is essential for reliable deployment.

## KDE Fundamentals and Kernel Functions

The KDE estimate at point x is p̂(x) = (1/nh) Σᵢ K((x−xᵢ)/h) where K is a kernel function satisfying ∫K(u)du=1, K(u)≥0, K(u)=K(−u). The Gaussian kernel K(u)=(1/√2π)exp(−u²/2) is most common for smooth densities. The bandwidth h is the single most important tuning parameter: too small (undersmoothing) produces a spiky density that memorises noise; too large (oversmoothing) blurs genuine structure and misses local anomalies.

- Gaussian kernel: K(u) = (1/√2π)exp(−u²/2) — infinitely differentiable, widely used.
- Epanechnikov kernel: K(u) = 0.75(1−u²)1(|u|≤1) — optimal in mean integrated squared error, compact support.
- Tophat (uniform) kernel: K(u) = 0.5·1(|u|≤1) — simple histogram-like estimate, discontinuous.
- Triangular kernel: K(u) = (1−|u|)·1(|u|≤1) — continuous but not differentiable at 0.

```python
import numpy as np

def gaussian_kernel(u):
    return np.exp(-0.5 * u ** 2) / np.sqrt(2 * np.pi)

def kde_density(X_train, x_query, h):
    '''KDE density estimate at query points using Gaussian kernel.'''
    n, d = X_train.shape
    scores = np.zeros(len(x_query))
    for i, xq in enumerate(x_query):
        diffs = (X_train - xq) / h          # (n, d)
        k_vals = np.prod(gaussian_kernel(diffs), axis=1)  # product kernel
        scores[i] = k_vals.mean() / (h ** d)
    return scores

np.random.seed(0)
X_train = np.concatenate([
    np.random.randn(300, 2),
    np.random.randn(100, 2) + [4, 1]
])
h_opt = 1.06 * X_train.std() * len(X_train) ** (-1/5)
X_query = np.array([[0., 0.], [4., 1.], [8., 8.]])
densities = kde_density(X_train, X_query, h=h_opt)
for xq, dens in zip(X_query, densities):
    print(f'x={xq}  density={dens:.5f}  log-density={np.log(dens+1e-12):.3f}')
```

## Bandwidth Selection Methods

Three main strategies for selecting h: (1) Silverman's rule of thumb: h = 1.06·σ·n^{−1/(d+4)}, optimal for Gaussian data — fast but oversmooths multimodal distributions. (2) Scott's rule: h = n^{−1/(d+4)} uses the identity covariance — equivalent to Silverman's with σ=1. (3) Cross-validation: maximise leave-one-out log-likelihood L(h) = Σᵢ log p̂_{−i}(xᵢ) where p̂_{−i} excludes point i — the most robust method but O(n²) cost.

```python
import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

np.random.seed(1)
X = np.concatenate([
    np.random.randn(200, 1),
    np.random.randn(100, 1) * 0.5 + 3.5
])

# Silverman rule
h_sil = 1.06 * X.std() * len(X) ** (-0.2)
print(f'Silverman bandwidth: h = {h_sil:.4f}')

# Cross-validation grid search
bandwidths = np.logspace(-2, 1, 30)
grid = GridSearchCV(
    KernelDensity(kernel='gaussian'),
    param_grid={'bandwidth': bandwidths},
    cv=5, scoring='neg_log_loss'
)
grid.fit(X)
h_cv = grid.best_params_['bandwidth']
print(f'CV-optimal bandwidth: h = {h_cv:.4f}')

kde = KernelDensity(kernel='gaussian', bandwidth=h_cv).fit(X)
X_test = np.array([[-2.], [0.], [3.5], [6.]])
log_dens = kde.score_samples(X_test)
for x, ld in zip(X_test.ravel(), log_dens):
    print(f'  x={x:5.1f}  log p={ld:.3f}  anomaly_score={-ld:.3f}')
```

## The Effect of Bandwidth on Density Estimation

Bandwidth directly controls the bias-variance tradeoff. Small h memorises each training point (variance dominates); large h produces a uniform-like density (bias dominates). The optimal h minimises the Mean Integrated Squared Error (MISE) = E[∫(p̂(x)−p(x))² dx]. For Gaussian data the MISE-optimal h scales as n^{−4/(d+4)}, which decays very slowly in high dimensions — this is the curse of dimensionality. Visualising the density for a range of h values reveals the tradeoff.

```python
import numpy as np
from sklearn.neighbors import KernelDensity

np.random.seed(2)
X_1d = np.concatenate([np.random.randn(150), np.random.randn(50)*0.4 + 3]).reshape(-1,1)
x_grid = np.linspace(-4, 6, 300).reshape(-1, 1)

print('Bandwidth comparison on 1D bimodal mixture:')
print(f'  {"h":>6}  {"peak1_dens":>12}  {"valley_dens":>13}  {"peak2_dens":>12}')
for h in [0.05, 0.15, 0.5, 1.5, 4.0]:
    kde = KernelDensity(bandwidth=h, kernel='gaussian').fit(X_1d)
    ld = kde.score_samples(x_grid)
    dens = np.exp(ld)
    # Evaluate at key points
    peak1  = np.exp(kde.score_samples([[0.0]]))[0]
    valley = np.exp(kde.score_samples([[1.8]]))[0]
    peak2  = np.exp(kde.score_samples([[3.0]]))[0]
    print(f'  {h:>6.2f}  {peak1:>12.5f}  {valley:>13.5f}  {peak2:>12.5f}')
print()
print('Small h: spiky (high variance). Large h: flat (high bias).')
print('CV-selected h should preserve both modes.')
```

## KDE for Anomaly Detection

The KDE anomaly score is −log p̂(x). Points with very low estimated density are flagged as anomalies. The threshold is set as the τ-th quantile (e.g., 5th percentile) of log-density scores on normal training data. Unlike parametric models, KDE adapts to the shape of the data without assuming Gaussianity — useful for multimodal or heavy-tailed distributions. The main limitation is scalability: evaluating the density at a query point costs O(n) operations.

```python
import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV

np.random.seed(3)
X_train = np.random.randn(500, 2)  # normal class
X_normal_test = np.random.randn(100, 2)
X_anomaly = np.random.uniform(-6, 6, (30, 2))  # uniform anomalies

bws = np.logspace(-1, 1, 20)
kde = KernelDensity(kernel='gaussian')
bw_cv = GridSearchCV(kde, {'bandwidth': bws}, cv=5).fit(X_train)
h_best = bw_cv.best_params_['bandwidth']
kde_fit = KernelDensity(bandwidth=h_best).fit(X_train)

log_d_norm = kde_fit.score_samples(X_normal_test)
log_d_anom = kde_fit.score_samples(X_anomaly)
threshold = np.percentile(log_d_norm, 5)  # 5th percentile as low-density cut

X_all = np.vstack([X_normal_test, X_anomaly])
y_all = np.array([0]*100 + [1]*30)
scores = -kde_fit.score_samples(X_all)  # negate: high score = anomaly
auroc = roc_auc_score(y_all, scores)
print(f'Bandwidth (CV): {h_best:.3f}')
print(f'AUROC: {auroc:.4f}')
print(f'Normal log-density mean:  {log_d_norm.mean():.3f}')
print(f'Anomaly log-density mean: {log_d_anom.mean():.3f}')
```

## Multivariate KDE and the Curse of Dimensionality

For d-dimensional data the product kernel is p̂(x) = (1/n·hᵈ) Σᵢ Πⱼ K((xⱼ−xᵢⱼ)/h). The MISE-optimal bandwidth scales as h★ ~ n^{−1/(d+4)}, meaning the convergence rate of KDE deteriorates exponentially with dimension. For d=1 the rate is n^{4/5}; for d=10 it is n^{4/14} ≈ n^{0.286} — far slower. In practice KDE becomes unreliable for d>5 unless the effective intrinsic dimensionality of the data is much lower. Alternatives include GMM, normalizing flows, and random-subspace KDE ensembles.

- For d≤3: KDE with CV bandwidth is highly effective and interpretable.
- For 3<d≤10: consider GMM or a mixture of diagonal Gaussians — parametric but faster.
- For d>10: use normalizing flows (exact likelihood) or isolation-forest-based density proxies.
- Bandwidth decay: h★ ~ n^{-1/(d+4)} — double the dimension, need exponentially more data for the same accuracy.
- Random subspace KDE: fit 1D or 2D KDE on random projections and aggregate — scales better than full-dimensional KDE.

## Density Estimator Comparison

> **KDE Scalability**: KDE density evaluation is O(n·d) per query — expensive for large training sets. Use a ball-tree or KD-tree index (sklearn KernelDensity uses these automatically) to reduce query cost to O(d·log n) for low dimensions. For n>100K or d>10, GMM or normalizing flows will be faster and more accurate.

| Method | Parametric | High-dim | Training Cost | Anomaly Score | Interpretable |
| --- | --- | --- | --- | --- | --- |
| KDE | No | Poor (d>5) | O(n·d) fit, O(n) query | −log p̂(x) | Yes — density plot |
| GMM | Yes (mixture) | Moderate (diagonal) | EM, O(n·k·d) per iter | −log p_GMM(x) | Yes — components |
| Isolation Forest | No (tree) | Good | O(n·log n) | Mean path length | Partial |
| OC-SVM | No (kernel) | Poor | O(n²)–O(n³) | Signed distance | No |
| Normalizing Flow | Semi (bijective NN) | Good | O(n·epochs·d) | −log p_flow(x) | No — black-box |

KDE excels in low to moderate dimensions with small to medium datasets where interpretability matters. For production anomaly detection at scale, combine KDE-based thresholds on low-dimensional feature projections with faster parametric alternatives for high-dimensional raw input spaces.

---

