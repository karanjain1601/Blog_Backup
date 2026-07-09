---
title: "Time-Series Evaluation — MAE, MAPE, SMAPE, CRPS, and Calibration"
slug: "timeseries-evaluation"
description: "Master forecasting evaluation: MAE, RMSE, MAPE, sMAPE, MASE for point forecasts; CRPS and WQL for probabilistic forecasts; calibration checks for prediction intervals; and a backtesting framework for comparing models across multiple metrics."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2hvb3NpbmcgdGhlIHJpZ2h0IGV2YWx1YXRpb24gbWV0cmljIGlzIGFzIGltcG9ydGFudCBhcyBjaG9vc2luZyB0aGUgcmlnaHQgbW9kZWwuIEEgbWV0cmljIHRoYXQgaXMgc2NhbGUtZGVwZW5kZW50IGNhbm5vdCBjb21wYXJlIG1vZGVscyBhY3Jvc3MgZGlmZmVyZW50IHNlcmllcy4gQSBtZXRyaWMgdW5kZWZpbmVkIGF0IHplcm8gdmFsdWVzIChNQVBFKSBtaXNsZWFkcyBvbiBpbnRlcm1pdHRlbnQgZGVtYW5kIGRhdGEuIEEgcG9pbnQgbWV0cmljIGlnbm9yZXMgZm9yZWNhc3QgdW5jZXJ0YWludHkgZW50aXJlbHkuIFRoaXMgbm90ZSBjb3ZlcnMgdGhlIGZ1bGwgaGllcmFyY2h5IG9mIHRpbWUtc2VyaWVzIGV2YWx1YXRpb24gbWV0cmljcywgZXhwbGFpbnMgd2hlbiBlYWNoIGlzIGFwcHJvcHJpYXRlLCBhbmQgYnVpbGRzIGEgcHJpbmNpcGxlZCBiYWNrdGVzdGluZyBmcmFtZXdvcmsgdGhhdCBjb21wdXRlcyBhbGwgbWV0cmljcyBzaW11bHRhbmVvdXNseS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsZS1EZXBlbmRlbnQgTWV0cmljcyDigJQgTUFFIGFuZCBSTVNFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNQUUgPSAoMS9IKc6jfHlfdCAtIMW3X3R8IGlzIHJvYnVzdCwgaW50ZXJwcmV0YWJsZSwgYW5kIGluIHRoZSBzYW1lIHVuaXRzIGFzIHRoZSBzZXJpZXMuIEl0IGlzIHRoZSBtaW5pbXVtIGV4cGVjdGVkIGxvc3MgdW5kZXIgYW4gYXN5bW1ldHJpYyBMMSBsb3NzIGFuZCB0aGUgYXBwcm9wcmlhdGUgbWV0cmljIHdoZW4gbGFyZ2UgZXJyb3JzIGFyZSBub3QgZGlzcHJvcG9ydGlvbmF0ZWx5IG1vcmUgY29zdGx5LiBNU0UgPSAoMS9IKc6jKHlfdCAtIMW3X3QpwrIgcGVuYWxpc2VzIGxhcmdlIGVycm9ycyBxdWFkcmF0aWNhbGx5IGFuZCBpcyBkaWZmZXJlbnRpYWJsZS4gUk1TRSA9IOKImk1TRSByZXN0b3JlcyB1bml0cy4gVGhlc2UgYXJlIHNjYWxlLWRlcGVuZGVudDogYSBSTVNFIG9mIDEwMCB1bml0cyBpcyBtZWFuaW5nbGVzcyB3aXRob3V0IGtub3dpbmcgdGhlIHNlcmllcyBzY2FsZSwgbWFraW5nIGNyb3NzLXNlcmllcyBjb21wYXJpc29uIGltcG9zc2libGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbWFlKHlfdHJ1ZSwgeV9wcmVkKTpcbiAgICByZXR1cm4gbnAubWVhbihucC5hYnMoeV90cnVlIC0geV9wcmVkKSlcblxuZGVmIHJtc2UoeV90cnVlLCB5X3ByZWQpOlxuICAgIHJldHVybiBucC5zcXJ0KG5wLm1lYW4oKHlfdHJ1ZSAtIHlfcHJlZCkqKjIpKVxuXG5kZWYgbWFwZSh5X3RydWUsIHlfcHJlZCwgZXBzPTFlLTgpOlxuICAgIFwiXCJcIk1BUEU6IHVuZGVmaW5lZC91bnN0YWJsZSB3aGVuIHlfdHJ1ZSB+IDA7IHVzZSBlcHMgZ3VhcmQuXCJcIlwiXG4gICAgcmV0dXJuIDEwMCAqIG5wLm1lYW4obnAuYWJzKCh5X3RydWUgLSB5X3ByZWQpIC8gKG5wLmFicyh5X3RydWUpICsgZXBzKSkpXG5cbmRlZiBzbWFwZSh5X3RydWUsIHlfcHJlZCwgZXBzPTFlLTgpOlxuICAgIFwiXCJcIlN5bW1ldHJpYyBNQVBFOiBib3VuZGVkIGluIFswLCAyMDBdIGJ1dCBzdGlsbCBwcm9ibGVtYXRpYyBuZWFyIHplcm8uXCJcIlwiXG4gICAgbnVtID0gbnAuYWJzKHlfdHJ1ZSAtIHlfcHJlZClcbiAgICBkZW4gPSAobnAuYWJzKHlfdHJ1ZSkgKyBucC5hYnMoeV9wcmVkKSkgLyAyICsgZXBzXG4gICAgcmV0dXJuIDEwMCAqIG5wLm1lYW4obnVtIC8gZGVuKVxuXG5kZWYgbWFzZSh5X3RydWUsIHlfcHJlZCwgeV90cmFpbiwgc2Vhc29uYWxpdHk9MSk6XG4gICAgXCJcIlwiTUFTRTogTUFFIHNjYWxlZCBieSBpbi1zYW1wbGUgc2Vhc29uYWwgbmFpdmUgTUFFLlwiXCJcIlxuICAgIG5haXZlX2Vycm9ycyA9IG5wLmFicyh5X3RyYWluW3NlYXNvbmFsaXR5Ol0gLSB5X3RyYWluWzotc2Vhc29uYWxpdHldKVxuICAgIHNjYWxlID0gbmFpdmVfZXJyb3JzLm1lYW4oKVxuICAgIHJldHVybiBtYWUoeV90cnVlLCB5X3ByZWQpIC8gKHNjYWxlICsgMWUtOClcblxubnAucmFuZG9tLnNlZWQoNDIpXG55X3RydWUgID0gbnAuYXJyYXkoWzEwMCwgMTEwLCA5NSwgMTIwLCAxMzAsIDExNSwgMTA1LCAxMjUsIDExOCwgMTA4XSwgZHR5cGU9ZmxvYXQpXG55X3ByZWQgID0gbnAuYXJyYXkoWzEwMiwgMTA4LCA5NywgMTE4LCAxMzIsIDExMywgMTA3LCAxMjMsIDEyMCwgMTEwXSwgZHR5cGU9ZmxvYXQpXG55X3RyYWluID0gbnAucmFuZG9tLnJhbmRuKDEwMCkgKiAxMCArIDEwMFxuXG5wcmludChmXHUwMDI3TUFFOiAgIHttYWUoeV90cnVlLCB5X3ByZWQpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3Uk1TRTogIHtybXNlKHlfdHJ1ZSwgeV9wcmVkKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01BUEU6ICB7bWFwZSh5X3RydWUsIHlfcHJlZCk6LjRmfSVcdTAwMjcpXG5wcmludChmXHUwMDI3c01BUEU6IHtzbWFwZSh5X3RydWUsIHlfcHJlZCk6LjRmfSVcdTAwMjcpXG5wcmludChmXHUwMDI3TUFTRTogIHttYXNlKHlfdHJ1ZSwgeV9wcmVkLCB5X3RyYWluLCBzZWFzb25hbGl0eT0xKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNjYWxlLUZyZWUgTWV0cmljcyDigJQgTUFQRSwgc01BUEUsIGFuZCBNQVNFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNQVBFIGlzIHVuZGVmaW5lZCB3aGVuIHlfdCA9IDAgYW5kIGFzeW1tZXRyaWM6IGEgcHJlZGljdGlvbiBvZiAxMjAgZm9yIGFjdHVhbCAxMDAgZ2l2ZXMgTUFQRT0yMCUsIGJ1dCBhIHByZWRpY3Rpb24gb2YgODAgZm9yIGFjdHVhbCAxMDAgZ2l2ZXMgTUFQRT0yMCUgdG9vIChidXQgdGhleSBhcmUgbm90IGVxdWl2YWxlbnQgZXJyb3JzKS4gc01BUEUgdXNlcyAofHl8ICsgfMW3fCkvMiBpbiB0aGUgZGVub21pbmF0b3IsIG1ha2luZyBpdCBzeW1tZXRyaWMsIGJ1dCBpdCBzdGlsbCBoYXMgcGF0aG9sb2dpY2FsIGJlaGF2aW91ciB3aGVuIGJvdGggeSBhbmQgxbcgYXBwcm9hY2ggMC4gTUFTRSAoSHluZG1hbiBcdTAwMjYgS29laGxlciwgMjAwNikgc2NhbGVzIGJ5IHRoZSBpbi1zYW1wbGUgc2Vhc29uYWwgbmFpdmUgTUFFOiBNQVNFID0gTUFFIC8gTUFFX25haXZlLiBNQVNFID0gMS4wIG1lYW5zIHRoZSBtb2RlbCBwZXJmb3JtcyBhdCBuYWl2ZS1zZWFzb25hbCBsZXZlbDsgTUFTRSBcdTAwM2MgMSBpcyBiZXR0ZXIgdGhhbiBuYWl2ZS4gTUFTRSBpcyB3ZWxsLWRlZmluZWQsIHNjYWxlLWZyZWUsIGFuZCBzdWl0YWJsZSBmb3IgY3Jvc3Mtc2VyaWVzIGNvbXBhcmlzb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ1JQUyBmb3IgUHJvYmFiaWxpc3RpYyBGb3JlY2FzdHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNSUFMgKENvbnRpbnVvdXMgUmFua2VkIFByb2JhYmlsaXR5IFNjb3JlKSBpcyBhIHByb3BlciBzY29yaW5nIHJ1bGUgZm9yIGRpc3RyaWJ1dGlvbmFsIGZvcmVjYXN0cy4gRm9yIGVuc2VtYmxlIHNhbXBsZXMge3hfMSwuLi4seF9NfTogQ1JQUyA9ICgxL00pzqN8eF9tIC0geXwgLSAoMS8yTcKyKc6jfHhfbSAtIHhfe21cdTAwMjd9fC4gTG93ZXIgaXMgYmV0dGVyLiBDUlBTIHJlZHVjZXMgdG8gTUFFIGZvciBhIHBvaW50IGZvcmVjYXN0IChkZWx0YSBkaXN0cmlidXRpb24pLiBXUUwgKFdlaWdodGVkIFF1YW50aWxlIExvc3MpIGlzIHRoZSBNNSBjb21wZXRpdGlvbiBwcm9iYWJpbGlzdGljIG1ldHJpYzogV1FMID0gKDIvSM6jfHlfdHwpIM6jX8+EIM6jX3QgTF/PhCh5X3QsIHFfe3Qsz4R9KSB3aGVyZSBMX8+EIGlzIHRoZSBwaW5iYWxsIGxvc3MuIEJvdGggQ1JQUyBhbmQgV1FMIGFyZSBwcm9wZXI6IHRoZSB0cnVlIGRpc3RyaWJ1dGlvbiBtaW5pbWlzZXMgZXhwZWN0ZWQgc2NvcmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybVxuXG5kZWYgY3Jwc19nYXVzc2lhbihtdSwgc2lnbWEsIHkpOlxuICAgIFwiXCJcIkFuYWx5dGljYWwgQ1JQUyBmb3IgR2F1c3NpYW4gcHJlZGljdGl2ZSBkaXN0cmlidXRpb24uXCJcIlwiXG4gICAgeiAgID0gKHkgLSBtdSkgLyBzaWdtYVxuICAgIHBoaSA9IG5vcm0ucGRmKHopXG4gICAgUGhpID0gbm9ybS5jZGYoeilcbiAgICByZXR1cm4gc2lnbWEgKiAoeiAqICgyKlBoaSAtIDEpICsgMipwaGkgLSAxL25wLnNxcnQobnAucGkpKVxuXG5kZWYgY3Jwc19lbnNlbWJsZShzYW1wbGVzLCB5KTpcbiAgICBcIlwiXCJDUlBTIGZyb20gTSBlbnNlbWJsZSBzYW1wbGVzLlwiXCJcIlxuICAgIE0gPSBzYW1wbGVzLnNoYXBlWzBdXG4gICAgdGVybTEgPSBucC5tZWFuKG5wLmFicyhzYW1wbGVzIC0geSkpXG4gICAgdGVybTIgPSBucC5tZWFuKG5wLmFicyhzYW1wbGVzWzosIE5vbmVdIC0gc2FtcGxlc1tOb25lLCA6XSkpXG4gICAgcmV0dXJuIHRlcm0xIC0gMC41ICogdGVybTJcblxuZGVmIHdxbCh5X3RydWUsIHF1YW50aWxlX2ZvcmVjYXN0cywgcXVhbnRpbGVfbGV2ZWxzKTpcbiAgICBcIlwiXCJXZWlnaHRlZCBRdWFudGlsZSBMb3NzIChNNSBtZXRyaWMpLlwiXCJcIlxuICAgIHRvdGFsLCBzY2FsZSA9IDAuMCwgbnAuYWJzKHlfdHJ1ZSkubWVhbigpICogMiArIDFlLThcbiAgICBmb3IgcSwgcWYgaW4gemlwKHF1YW50aWxlX2xldmVscywgcXVhbnRpbGVfZm9yZWNhc3RzLlQpOlxuICAgICAgICBlcnIgPSB5X3RydWUgLSBxZlxuICAgICAgICBsb3NzID0gbnAud2hlcmUoZXJyIFx1MDAzZT0gMCwgcSAqIGVyciwgKHEgLSAxKSAqIGVycilcbiAgICAgICAgdG90YWwgKz0gbG9zcy5tZWFuKClcbiAgICByZXR1cm4gdG90YWwgLyAoc2NhbGUgKiBsZW4ocXVhbnRpbGVfbGV2ZWxzKSlcblxubnAucmFuZG9tLnNlZWQoMClcbnkgPSBucC5yYW5kb20ucmFuZG4oMjAwKSAqIDIgKyA1XG5tdSwgc2lnbWEgPSA1LjAsIDIuMFxuY3Jwc192YWxzID0gY3Jwc19nYXVzc2lhbihtdSAqIG5wLm9uZXMoMjAwKSwgc2lnbWEgKiBucC5vbmVzKDIwMCksIHkpXG5wcmludChmXHUwMDI3TWVhbiBDUlBTIChHYXVzc2lhbiwgY29ycmVjdCBzaWdtYT0yKToge2NycHNfdmFscy5tZWFuKCk6LjRmfVx1MDAyNylcbmNycHNfd2lkZSA9IGNycHNfZ2F1c3NpYW4obXUgKiBucC5vbmVzKDIwMCksIDQuMCAqIG5wLm9uZXMoMjAwKSwgeSlcbnByaW50KGZcdTAwMjdNZWFuIENSUFMgKHRvbyB3aWRlIHNpZ21hPTQpOiAgICAgICAgICB7Y3Jwc193aWRlLm1lYW4oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNhbGlicmF0aW9uIOKAlCBDb3ZlcmFnZSBvZiBQcmVkaWN0aW9uIEludGVydmFscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBjYWxpYnJhdGVkIHByb2JhYmlsaXN0aWMgZm9yZWNhc3Qgc2F0aXNmaWVzOiBlbXBpcmljYWwgY292ZXJhZ2UgYXQgbm9taW5hbCBsZXZlbCDOsSDiiYggzrEuIFRoYXQgaXMsIDgwJSBwcmVkaWN0aW9uIGludGVydmFscyBzaG91bGQgY29udGFpbiB0aGUgdHJ1ZSB2YWx1ZSA4MCUgb2YgdGhlIHRpbWUuIENhbGlicmF0aW9uIGlzIGFzc2Vzc2VkIGJ5IGNvbXB1dGluZyBjb3ZlcmFnZSBhdCBtdWx0aXBsZSBsZXZlbHMgKDUwJSwgODAlLCA5MCUpIGFuZCBwbG90dGluZyBub21pbmFsIHZzIGVtcGlyaWNhbCBjb3ZlcmFnZSDigJQgYSBjYWxpYnJhdGlvbiBjdXJ2ZS4gQSBwZXJmZWN0bHkgY2FsaWJyYXRlZCBtb2RlbCBsaWVzIG9uIHRoZSBkaWFnb25hbC4gVW5kZXItY292ZXJhZ2UgKGVtcGlyaWNhbCBcdTAwM2Mgbm9taW5hbCkgbWVhbnMgaW50ZXJ2YWxzIGFyZSB0b28gbmFycm93OyBvdmVyLWNvdmVyYWdlIChlbXBpcmljYWwgXHUwMDNlIG5vbWluYWwpIG1lYW5zIGludGVydmFscyBhcmUgdG9vIHdpZGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybVxuXG5kZWYgY2hlY2tfY2FsaWJyYXRpb24oeV90cnVlLCBtdV9wcmVkLCBzaWdtYV9wcmVkLCBsZXZlbHM9Tm9uZSk6XG4gICAgXCJcIlwiXG4gICAgQ2hlY2sgY2FsaWJyYXRpb24gb2YgR2F1c3NpYW4gcHJlZGljdGlvbiBpbnRlcnZhbHMuXG4gICAgUmV0dXJucyBkaWN0IG9mIHtub21pbmFsX2xldmVsOiBlbXBpcmljYWxfY292ZXJhZ2V9LlxuICAgIFwiXCJcIlxuICAgIGlmIGxldmVscyBpcyBOb25lOlxuICAgICAgICBsZXZlbHMgPSBbMC41MCwgMC44MCwgMC45MCwgMC45NV1cbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgbGV2ZWwgaW4gbGV2ZWxzOlxuICAgICAgICBhbHBoYSA9IDEgLSBsZXZlbFxuICAgICAgICB6ID0gbm9ybS5wcGYoMSAtIGFscGhhIC8gMilcbiAgICAgICAgbG93ZXIgPSBtdV9wcmVkIC0geiAqIHNpZ21hX3ByZWRcbiAgICAgICAgdXBwZXIgPSBtdV9wcmVkICsgeiAqIHNpZ21hX3ByZWRcbiAgICAgICAgY292ZXJhZ2UgPSBucC5tZWFuKCh5X3RydWUgXHUwMDNlPSBsb3dlcikgXHUwMDI2ICh5X3RydWUgXHUwMDNjPSB1cHBlcikpXG4gICAgICAgIHJlc3VsdHNbbGV2ZWxdID0gY292ZXJhZ2VcbiAgICByZXR1cm4gcmVzdWx0c1xuXG5ucC5yYW5kb20uc2VlZCg0Milcbm4gPSA1MDBcbnlfdHJ1ZSAgICAgPSBucC5yYW5kb20ucmFuZG4obikgKiAyICsgM1xubXVfcHJlZCAgICA9IDMuMCAqIG5wLm9uZXMobilcbnNpZ21hX2dvb2QgPSAyLjAgKiBucC5vbmVzKG4pICAgIyBjb3JyZWN0bHkgY2FsaWJyYXRlZFxuc2lnbWFfYmFkICA9IDAuOCAqIG5wLm9uZXMobikgICAjIHVuZGVyLWRpc3BlcnNlZCAodG9vIG5hcnJvdylcblxuY2FsX2dvb2QgPSBjaGVja19jYWxpYnJhdGlvbih5X3RydWUsIG11X3ByZWQsIHNpZ21hX2dvb2QpXG5jYWxfYmFkICA9IGNoZWNrX2NhbGlicmF0aW9uKHlfdHJ1ZSwgbXVfcHJlZCwgc2lnbWFfYmFkKVxuXG5wcmludChcdTAwMjdOb21pbmFsICB8ICBHb29kIG1vZGVsICB8ICBOYXJyb3cgbW9kZWxcdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNDUpXG5mb3IgbHZsIGluIFswLjUwLCAwLjgwLCAwLjkwLCAwLjk1XTpcbiAgICBwcmludChmXHUwMDI3e2x2bDouMCV9ICAgICAgfCAge2NhbF9nb29kW2x2bF06LjNmfSAgICAgICB8ICB7Y2FsX2JhZFtsdmxdOi4zZn1cdTAwMjcpXG5wcmludChcdTAwMjdHb29kIG1vZGVsIGVtcGlyaWNhbCBjb3ZlcmFnZSDiiYggbm9taW5hbDsgbmFycm93IG1vZGVsIHVuZGVyLWNvdmVycy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmFja3Rlc3RpbmcgRnJhbWV3b3JrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHJvYnVzdCBiYWNrdGVzdGluZyBmcmFtZXdvcmsgdXNlcyByb2xsaW5nIG9yIGV4cGFuZGluZyB3aW5kb3cgY3Jvc3MtdmFsaWRhdGlvbiB0byBldmFsdWF0ZSBmb3JlY2FzdGluZyBtb2RlbHMgb24gbXVsdGlwbGUgaGVsZC1vdXQgdGVzdCB3aW5kb3dzLiBUaGlzIGF2b2lkcyBsdWNreSBvciB1bmx1Y2t5IHNpbmdsZSB0ZXN0IHNwbGl0cyBhbmQgcHJvdmlkZXMgY29uZmlkZW5jZSBpbnRlcnZhbHMgb24gbWV0cmljIGVzdGltYXRlcy4gVGhlIGZyYW1ld29yayBzaG91bGQ6ICgxKSBnZW5lcmF0ZSBtdWx0aXBsZSAodHJhaW4sIHRlc3QpIHNwbGl0cywgKDIpIGZpdCBlYWNoIG1vZGVsIG9uIGVhY2ggdHJhaW4gc3BsaXQsICgzKSBjb21wdXRlIGFsbCByZWxldmFudCBtZXRyaWNzIG9uIGVhY2ggdGVzdCB3aW5kb3csICg0KSBhZ2dyZWdhdGUgd2l0aCBtZWFuIGFuZCBzdGQgYWNyb3NzIHNwbGl0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBSaWRnZVxuXG5kZWYgbGFnX2ZlYXR1cmVzKHksIG5fbGFncz0xMik6XG4gICAgWCA9IG5wLnN0YWNrKFt5W2k6bGVuKHkpLW5fbGFncytpXSBmb3IgaSBpbiByYW5nZShuX2xhZ3MpXSwgYXhpcz0xKVxuICAgIHJldHVybiBYWzotMV0sIHlbbl9sYWdzOl1cblxuZGVmIHJvbGxpbmdfY3YoeSwgaG9yaXpvbj0xMiwgbl9zcGxpdHM9NSwgbWluX3RyYWluPTEwMCk6XG4gICAgXCJcIlwiUm9sbGluZyB3aW5kb3cgY3Jvc3MtdmFsaWRhdGlvbiBmb3IgdGltZSBzZXJpZXMuXCJcIlwiXG4gICAgbiA9IGxlbih5KVxuICAgIHJlc3VsdHMgPSBbXVxuICAgIHN0ZXAgPSAobiAtIG1pbl90cmFpbiAtIGhvcml6b24pIC8vIG5fc3BsaXRzXG4gICAgZm9yIGkgaW4gcmFuZ2Uobl9zcGxpdHMpOlxuICAgICAgICBzcGxpdCA9IG1pbl90cmFpbiArIGkgKiBzdGVwXG4gICAgICAgIHlfdHJhaW4gPSB5WzpzcGxpdF1cbiAgICAgICAgeV90ZXN0ICA9IHlbc3BsaXQ6c3BsaXQgKyBob3Jpem9uXVxuICAgICAgICBYX2FsbCwgeV9mZWF0ID0gbGFnX2ZlYXR1cmVzKHlbOnNwbGl0ICsgaG9yaXpvbl0pXG4gICAgICAgIFhfdHIsIHlfdHIgPSBYX2FsbFs6c3BsaXQgLSAxMl0sIHlfZmVhdFs6c3BsaXQgLSAxMl1cbiAgICAgICAgWF90ZSwgeV90ZSA9IFhfYWxsW3NwbGl0IC0gMTI6c3BsaXQgLSAxMiArIGhvcml6b25dLCB5X2ZlYXRbc3BsaXQgLSAxMjpzcGxpdCAtIDEyICsgaG9yaXpvbl1cbiAgICAgICAgbW9kZWwgPSBSaWRnZShhbHBoYT0xLjApLmZpdChYX3RyLCB5X3RyKVxuICAgICAgICB5X2hhdCA9IG1vZGVsLnByZWRpY3QoWF90ZSlcbiAgICAgICAgbWFlX3ZhbCAgPSBucC5hYnMoeV90ZSAtIHlfaGF0KS5tZWFuKClcbiAgICAgICAgcm1zZV92YWwgPSBucC5zcXJ0KCgoeV90ZSAtIHlfaGF0KSoqMikubWVhbigpKVxuICAgICAgICBtYXBlX3ZhbCA9IChucC5hYnMoKHlfdGUgLSB5X2hhdCkgLyAobnAuYWJzKHlfdGUpICsgMWUtOCkpICogMTAwKS5tZWFuKClcbiAgICAgICAgcmVzdWx0cy5hcHBlbmQoe1x1MDAyN3NwbGl0XHUwMDI3OiBpLCBcdTAwMjdtYWVcdTAwMjc6IG1hZV92YWwsIFx1MDAyN3Jtc2VcdTAwMjc6IHJtc2VfdmFsLCBcdTAwMjdtYXBlXHUwMDI3OiBtYXBlX3ZhbH0pXG4gICAgcmV0dXJuIHJlc3VsdHNcblxubnAucmFuZG9tLnNlZWQoNDIpXG55ID0gbnAuY3Vtc3VtKG5wLnJhbmRvbS5yYW5kbigzMDApKSArIDUwXG5yZXN1bHRzID0gcm9sbGluZ19jdih5LCBob3Jpem9uPTEyLCBuX3NwbGl0cz01KVxuZm9yIHIgaW4gcmVzdWx0czpcbiAgICBwcmludChmXHUwMDI3U3BsaXQge3JbXCJzcGxpdFwiXX06IE1BRT17cltcIm1hZVwiXTouM2Z9LCBSTVNFPXtyW1wicm1zZVwiXTouM2Z9LCBNQVBFPXtyW1wibWFwZVwiXTouMmZ9JVx1MDAyNylcbm1hZXMgPSBbcltcdTAwMjdtYWVcdTAwMjddIGZvciByIGluIHJlc3VsdHNdXG5wcmludChmXHUwMDI3TWVhbiBNQUU6IHtucC5tZWFuKG1hZXMpOi4zZn0gKy8tIHtucC5zdGQobWFlcyk6LjNmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6Ik5ldmVyIEV2YWx1YXRlIG9uIGEgU2luZ2xlIFRlc3QgV2luZG93IiwiY29udGVudCI6IkEgc2luZ2xlIHRyYWluLXRlc3Qgc3BsaXQgY2FuIGJlIG1pc2xlYWRpbmc6IHRoZSB0ZXN0IHBlcmlvZCBtYXkgYmUgdW51c3VhbGx5IGVhc3kgKGxvdyB2b2xhdGlsaXR5KSBvciBoYXJkIChhbiBvdXRsaWVyIGV2ZW50KS4gUm9sbGluZyBjcm9zcy12YWxpZGF0aW9uIHdpdGggNeKAkzEwIHRlc3Qgd2luZG93cyBwcm92aWRlcyBhIG1vcmUgcmVsaWFibGUgZXN0aW1hdGUgb2Ygb3V0LW9mLXNhbXBsZSBwZXJmb3JtYW5jZSBhbmQgZW5hYmxlcyBjb25maWRlbmNlIGludGVydmFscyBvbiBtZXRyaWMgZGlmZmVyZW5jZXMgYmV0d2VlbiBtb2RlbHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXZhbHVhdGlvbiBNZXRyaWMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRyaWMiLCJUeXBlIiwiU2NhbGUtRnJlZSIsIlplcm8tU2FmZSIsIkNyb3NzLVNlcmllcyIsIlByb3BlciBTY29yaW5nIFJ1bGUiXSwicm93cyI6W1siTUFFIiwiUG9pbnQiLCJObyIsIlllcyIsIk5vIiwiTi9BIl0sWyJSTVNFIiwiUG9pbnQiLCJObyIsIlllcyIsIk5vIiwiTi9BIl0sWyJNQVBFIiwiUG9pbnQiLCJZZXMiLCJObyAodW5kZWZpbmVkIGF0IDApIiwiWWVzIiwiTi9BIl0sWyJzTUFQRSIsIlBvaW50IiwiWWVzIiwiTm8gKHVuc3RhYmxlIG5lYXIgMCkiLCJZZXMiLCJOL0EiXSxbIk1BU0UiLCJQb2ludCIsIlllcyIsIlllcyIsIlllcyAoYmVzdCBmb3IgTSBjb21wcykiLCJOL0EiXSxbIkNSUFMiLCJQcm9iYWJpbGlzdGljIiwiTm8gKHNhbWUgdW5pdHMgYXMgc2VyaWVzKSIsIlllcyIsIk5vIiwiWWVzIl0sWyJXUUwiLCJQcm9iYWJpbGlzdGljIChxdWFudGlsZSkiLCJZZXMgKG5vcm1hbGlzZWQpIiwiWWVzIiwiWWVzIiwiWWVzIChwaW5iYWxsKSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtU2VyaWVzIENvbXBhcmlzb24gd2l0aCBNQVNFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNQVNFIGlzIHRoZSByZWNvbW1lbmRlZCBtZXRyaWMgZm9yIGNvbXBhcmluZyBtb2RlbHMgYWNyb3NzIG11bHRpcGxlIHNlcmllcyBvZiBkaWZmZXJlbnQgc2NhbGVzLCBhcyB1c2VkIGluIHRoZSBNMeKAk001IGNvbXBldGl0aW9ucy4gVGhlIG5haXZlIHNlYXNvbmFsIGJhc2VsaW5lIGRpdmlkZXMgZWFjaCBzZXJpZXPigJkgc2NhbGUgYnkgTUFFIG9mIHRoZSBpbi1zYW1wbGUgc2Vhc29uYWwgcmFuZG9tIHdhbGs6IMW3X3QgPSB5X3t0LW19IHdoZXJlIG0gaXMgdGhlIHNlYXNvbmFsIHBlcmlvZC4gQSBtb2RlbCB3aXRoIE1BU0UgXHUwMDNjIDEgYmVhdHMgdGhlIHNlYXNvbmFsIG5haXZlLiBXUk1TU0UgKE01KSBleHRlbmRzIE1BU0UgdG8gd2VpZ2h0ZWQgcm9vdCBtZWFuIHNxdWFyZWQgZm9ybSB3aXRoIGhpZXJhcmNoaWNhbCBhZ2dyZWdhdGlvbiB3ZWlnaHRzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIE1BRSBmb3Igb3BlcmF0aW9uYWwgZGFzaGJvYXJkcyB3aGVyZSBpbnRlcnByZXRhYmlsaXR5IGluIG9yaWdpbmFsIHVuaXRzIG1hdHRlcnMuIiwiVXNlIE1BU0UgZm9yIE0tY29tcGV0aXRpb24tc3R5bGUgY3Jvc3Mtc2VyaWVzIGNvbXBhcmlzb24gYW5kIGFjYWRlbWljIGJlbmNobWFya3MuIiwiQXZvaWQgTUFQRSBvbiBpbnRlcm1pdHRlbnQgZGVtYW5kIHNlcmllcyAocmV0YWlsIFNLVSBsZXZlbCkg4oCUIHVzZSBNQVNFIG9yIHNNQVBFIGluc3RlYWQuIiwiQWx3YXlzIHJlcG9ydCBDUlBTIGFsb25nc2lkZSBNQUUgZm9yIHByb2JhYmlsaXN0aWMgZm9yZWNhc3RzOyBDUlBTIGlzIHRoZSBnb2xkIHN0YW5kYXJkLiIsIkNhbGlicmF0aW9uIGNoZWNrOiBjb21wdXRlIFBJIGNvdmVyYWdlIGF0IDUwJSwgODAlLCBhbmQgOTAlIGxldmVscyBhbmQgY29tcGFyZSB0byBub21pbmFsLiIsIlJvbGxpbmcgQ1Y6IHVzZSBhdCBsZWFzdCA1IHRlc3Qgd2luZG93czsgcmVwb3J0IG1lYW4gYW5kIHN0YW5kYXJkIGRldmlhdGlvbiBvZiBlYWNoIG1ldHJpYy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Time-Series Evaluation — MAE, MAPE, SMAPE, CRPS, and Calibration

Choosing the right evaluation metric is as important as choosing the right model. A metric that is scale-dependent cannot compare models across different series. A metric undefined at zero values (MAPE) misleads on intermittent demand data. A point metric ignores forecast uncertainty entirely. This note covers the full hierarchy of time-series evaluation metrics, explains when each is appropriate, and builds a principled backtesting framework that computes all metrics simultaneously.

## Scale-Dependent Metrics — MAE and RMSE

MAE = (1/H)Σ|y_t - ŷ_t| is robust, interpretable, and in the same units as the series. It is the minimum expected loss under an asymmetric L1 loss and the appropriate metric when large errors are not disproportionately more costly. MSE = (1/H)Σ(y_t - ŷ_t)² penalises large errors quadratically and is differentiable. RMSE = √MSE restores units. These are scale-dependent: a RMSE of 100 units is meaningless without knowing the series scale, making cross-series comparison impossible.

```python
import numpy as np

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred)**2))

def mape(y_true, y_pred, eps=1e-8):
    """MAPE: undefined/unstable when y_true ~ 0; use eps guard."""
    return 100 * np.mean(np.abs((y_true - y_pred) / (np.abs(y_true) + eps)))

def smape(y_true, y_pred, eps=1e-8):
    """Symmetric MAPE: bounded in [0, 200] but still problematic near zero."""
    num = np.abs(y_true - y_pred)
    den = (np.abs(y_true) + np.abs(y_pred)) / 2 + eps
    return 100 * np.mean(num / den)

def mase(y_true, y_pred, y_train, seasonality=1):
    """MASE: MAE scaled by in-sample seasonal naive MAE."""
    naive_errors = np.abs(y_train[seasonality:] - y_train[:-seasonality])
    scale = naive_errors.mean()
    return mae(y_true, y_pred) / (scale + 1e-8)

np.random.seed(42)
y_true  = np.array([100, 110, 95, 120, 130, 115, 105, 125, 118, 108], dtype=float)
y_pred  = np.array([102, 108, 97, 118, 132, 113, 107, 123, 120, 110], dtype=float)
y_train = np.random.randn(100) * 10 + 100

print(f'MAE:   {mae(y_true, y_pred):.4f}')
print(f'RMSE:  {rmse(y_true, y_pred):.4f}')
print(f'MAPE:  {mape(y_true, y_pred):.4f}%')
print(f'sMAPE: {smape(y_true, y_pred):.4f}%')
print(f'MASE:  {mase(y_true, y_pred, y_train, seasonality=1):.4f}')
```

## Scale-Free Metrics — MAPE, sMAPE, and MASE

MAPE is undefined when y_t = 0 and asymmetric: a prediction of 120 for actual 100 gives MAPE=20%, but a prediction of 80 for actual 100 gives MAPE=20% too (but they are not equivalent errors). sMAPE uses (|y| + |ŷ|)/2 in the denominator, making it symmetric, but it still has pathological behaviour when both y and ŷ approach 0. MASE (Hyndman & Koehler, 2006) scales by the in-sample seasonal naive MAE: MASE = MAE / MAE_naive. MASE = 1.0 means the model performs at naive-seasonal level; MASE < 1 is better than naive. MASE is well-defined, scale-free, and suitable for cross-series comparison.

## CRPS for Probabilistic Forecasts

CRPS (Continuous Ranked Probability Score) is a proper scoring rule for distributional forecasts. For ensemble samples {x_1,...,x_M}: CRPS = (1/M)Σ|x_m - y| - (1/2M²)Σ|x_m - x_{m'}|. Lower is better. CRPS reduces to MAE for a point forecast (delta distribution). WQL (Weighted Quantile Loss) is the M5 competition probabilistic metric: WQL = (2/HΣ|y_t|) Σ_τ Σ_t L_τ(y_t, q_{t,τ}) where L_τ is the pinball loss. Both CRPS and WQL are proper: the true distribution minimises expected score.

```python
import numpy as np
from scipy.stats import norm

def crps_gaussian(mu, sigma, y):
    """Analytical CRPS for Gaussian predictive distribution."""
    z   = (y - mu) / sigma
    phi = norm.pdf(z)
    Phi = norm.cdf(z)
    return sigma * (z * (2*Phi - 1) + 2*phi - 1/np.sqrt(np.pi))

def crps_ensemble(samples, y):
    """CRPS from M ensemble samples."""
    M = samples.shape[0]
    term1 = np.mean(np.abs(samples - y))
    term2 = np.mean(np.abs(samples[:, None] - samples[None, :]))
    return term1 - 0.5 * term2

def wql(y_true, quantile_forecasts, quantile_levels):
    """Weighted Quantile Loss (M5 metric)."""
    total, scale = 0.0, np.abs(y_true).mean() * 2 + 1e-8
    for q, qf in zip(quantile_levels, quantile_forecasts.T):
        err = y_true - qf
        loss = np.where(err >= 0, q * err, (q - 1) * err)
        total += loss.mean()
    return total / (scale * len(quantile_levels))

np.random.seed(0)
y = np.random.randn(200) * 2 + 5
mu, sigma = 5.0, 2.0
crps_vals = crps_gaussian(mu * np.ones(200), sigma * np.ones(200), y)
print(f'Mean CRPS (Gaussian, correct sigma=2): {crps_vals.mean():.4f}')
crps_wide = crps_gaussian(mu * np.ones(200), 4.0 * np.ones(200), y)
print(f'Mean CRPS (too wide sigma=4):          {crps_wide.mean():.4f}')
```

## Calibration — Coverage of Prediction Intervals

A calibrated probabilistic forecast satisfies: empirical coverage at nominal level α ≈ α. That is, 80% prediction intervals should contain the true value 80% of the time. Calibration is assessed by computing coverage at multiple levels (50%, 80%, 90%) and plotting nominal vs empirical coverage — a calibration curve. A perfectly calibrated model lies on the diagonal. Under-coverage (empirical < nominal) means intervals are too narrow; over-coverage (empirical > nominal) means intervals are too wide.

```python
import numpy as np
from scipy.stats import norm

def check_calibration(y_true, mu_pred, sigma_pred, levels=None):
    """
    Check calibration of Gaussian prediction intervals.
    Returns dict of {nominal_level: empirical_coverage}.
    """
    if levels is None:
        levels = [0.50, 0.80, 0.90, 0.95]
    results = {}
    for level in levels:
        alpha = 1 - level
        z = norm.ppf(1 - alpha / 2)
        lower = mu_pred - z * sigma_pred
        upper = mu_pred + z * sigma_pred
        coverage = np.mean((y_true >= lower) & (y_true <= upper))
        results[level] = coverage
    return results

np.random.seed(42)
n = 500
y_true     = np.random.randn(n) * 2 + 3
mu_pred    = 3.0 * np.ones(n)
sigma_good = 2.0 * np.ones(n)   # correctly calibrated
sigma_bad  = 0.8 * np.ones(n)   # under-dispersed (too narrow)

cal_good = check_calibration(y_true, mu_pred, sigma_good)
cal_bad  = check_calibration(y_true, mu_pred, sigma_bad)

print('Nominal  |  Good model  |  Narrow model')
print('-' * 45)
for lvl in [0.50, 0.80, 0.90, 0.95]:
    print(f'{lvl:.0%}      |  {cal_good[lvl]:.3f}       |  {cal_bad[lvl]:.3f}')
print('Good model empirical coverage ≈ nominal; narrow model under-covers.')
```

## Backtesting Framework

A robust backtesting framework uses rolling or expanding window cross-validation to evaluate forecasting models on multiple held-out test windows. This avoids lucky or unlucky single test splits and provides confidence intervals on metric estimates. The framework should: (1) generate multiple (train, test) splits, (2) fit each model on each train split, (3) compute all relevant metrics on each test window, (4) aggregate with mean and std across splits.

```python
import numpy as np
from sklearn.linear_model import Ridge

def lag_features(y, n_lags=12):
    X = np.stack([y[i:len(y)-n_lags+i] for i in range(n_lags)], axis=1)
    return X[:-1], y[n_lags:]

def rolling_cv(y, horizon=12, n_splits=5, min_train=100):
    """Rolling window cross-validation for time series."""
    n = len(y)
    results = []
    step = (n - min_train - horizon) // n_splits
    for i in range(n_splits):
        split = min_train + i * step
        y_train = y[:split]
        y_test  = y[split:split + horizon]
        X_all, y_feat = lag_features(y[:split + horizon])
        X_tr, y_tr = X_all[:split - 12], y_feat[:split - 12]
        X_te, y_te = X_all[split - 12:split - 12 + horizon], y_feat[split - 12:split - 12 + horizon]
        model = Ridge(alpha=1.0).fit(X_tr, y_tr)
        y_hat = model.predict(X_te)
        mae_val  = np.abs(y_te - y_hat).mean()
        rmse_val = np.sqrt(((y_te - y_hat)**2).mean())
        mape_val = (np.abs((y_te - y_hat) / (np.abs(y_te) + 1e-8)) * 100).mean()
        results.append({'split': i, 'mae': mae_val, 'rmse': rmse_val, 'mape': mape_val})
    return results

np.random.seed(42)
y = np.cumsum(np.random.randn(300)) + 50
results = rolling_cv(y, horizon=12, n_splits=5)
for r in results:
    print(f'Split {r["split"]}: MAE={r["mae"]:.3f}, RMSE={r["rmse"]:.3f}, MAPE={r["mape"]:.2f}%')
maes = [r['mae'] for r in results]
print(f'Mean MAE: {np.mean(maes):.3f} +/- {np.std(maes):.3f}')
```

> **Never Evaluate on a Single Test Window**: A single train-test split can be misleading: the test period may be unusually easy (low volatility) or hard (an outlier event). Rolling cross-validation with 5–10 test windows provides a more reliable estimate of out-of-sample performance and enables confidence intervals on metric differences between models.

## Evaluation Metric Comparison

| Metric | Type | Scale-Free | Zero-Safe | Cross-Series | Proper Scoring Rule |
| --- | --- | --- | --- | --- | --- |
| MAE | Point | No | Yes | No | N/A |
| RMSE | Point | No | Yes | No | N/A |
| MAPE | Point | Yes | No (undefined at 0) | Yes | N/A |
| sMAPE | Point | Yes | No (unstable near 0) | Yes | N/A |
| MASE | Point | Yes | Yes | Yes (best for M comps) | N/A |
| CRPS | Probabilistic | No (same units as series) | Yes | No | Yes |
| WQL | Probabilistic (quantile) | Yes (normalised) | Yes | Yes | Yes (pinball) |

## Cross-Series Comparison with MASE

MASE is the recommended metric for comparing models across multiple series of different scales, as used in the M1–M5 competitions. The naive seasonal baseline divides each series’ scale by MAE of the in-sample seasonal random walk: ŷ_t = y_{t-m} where m is the seasonal period. A model with MASE < 1 beats the seasonal naive. WRMSSE (M5) extends MASE to weighted root mean squared form with hierarchical aggregation weights.

- Use MAE for operational dashboards where interpretability in original units matters.
- Use MASE for M-competition-style cross-series comparison and academic benchmarks.
- Avoid MAPE on intermittent demand series (retail SKU level) — use MASE or sMAPE instead.
- Always report CRPS alongside MAE for probabilistic forecasts; CRPS is the gold standard.
- Calibration check: compute PI coverage at 50%, 80%, and 90% levels and compare to nominal.
- Rolling CV: use at least 5 test windows; report mean and standard deviation of each metric.

---

