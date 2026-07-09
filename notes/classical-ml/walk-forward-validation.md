---
title: "Walk-Forward Validation — Preventing Data Leakage Through Time"
slug: "walk-forward-validation"
description: "Understand why standard k-fold cross-validation is invalid for time series and implement expanding-window and rolling-window walk-forward validation to obtain unbiased out-of-sample performance estimates."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgay1mb2xkIGNyb3NzLXZhbGlkYXRpb24gcmFuZG9tbHkgYXNzaWducyBvYnNlcnZhdGlvbnMgdG8gZm9sZHMsIGFsbG93aW5nIGZ1dHVyZSBvYnNlcnZhdGlvbnMgdG8gYXBwZWFyIGluIHRoZSB0cmFpbmluZyBzZXQuIEZvciB0aW1lIHNlcmllcyB0aGlzIGNvbnN0aXR1dGVzIGRhdGEgbGVha2FnZTogdGhlIG1vZGVsIHNlZXMgZnV0dXJlIGluZm9ybWF0aW9uIGR1cmluZyB0cmFpbmluZywgYW5kIGluLXNhbXBsZSBlcnJvciBtZXRyaWNzIHNldmVyZWx5IHVuZGVyZXN0aW1hdGUgdHJ1ZSB0ZXN0IGVycm9yLiBXYWxrLWZvcndhcmQgdmFsaWRhdGlvbiAoYWxzbyBjYWxsZWQgcm9sbGluZy1vcmlnaW4gZXZhbHVhdGlvbikgcmVzcGVjdHMgdGhlIHRlbXBvcmFsIG9yZGVyaW5nIOKAlCB0aGUgbW9kZWwgaXMgYWx3YXlzIHRyYWluZWQgb24gcGFzdCBkYXRhIGFuZCBldmFsdWF0ZWQgb24gZnV0dXJlIGRhdGEg4oCUIHByb2R1Y2luZyB1bmJpYXNlZCBlc3RpbWF0ZXMgb2YgZm9yZWNhc3QgYWNjdXJhY3kgYXQgdGhlIGRlc2lyZWQgaG9yaXpvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIldhbGstZm9yd2FyZCBldmFsdWF0aW9uIGFsd2F5cyB0cmFpbnMgb24gcGFzdCBkYXRhIGFuZCB0ZXN0cyBvbiBmdXR1cmUgZGF0YSDigJQgbm8gc2h1ZmZsaW5nLiIsIkV4cGFuZGluZyB3aW5kb3c6IHRyYWluaW5nIHNldCBncm93cyBlYWNoIGZvbGQ7IGJlc3QgZm9yIHN0YXRpb25hcnkgc2VyaWVzIHdpdGggbGltaXRlZCBkYXRhLiIsIlJvbGxpbmcgd2luZG93OiBmaXhlZCB0cmFpbmluZyBzaXplIHNsaWRlcyBmb3J3YXJkOyBiZXN0IGZvciBub24tc3RhdGlvbmFyeSBvciByZWdpbWUtY2hhbmdpbmcgc2VyaWVzLiIsIkdhcDogYnVmZmVyIHBlcmlvZHMgYmV0d2VlbiB0cmFpbiBlbmQgYW5kIHRlc3Qgc3RhcnQgcHJldmVudCBmZWF0dXJlIHdpbmRvdyBjb250YW1pbmF0aW9uLiIsIk5lc3RlZCBDVjogdXNlIGFuIGlubmVyIHdhbGstZm9yd2FyZCBsb29wIGZvciBoeXBlcnBhcmFtZXRlciB0dW5pbmcgd2l0aGluIGVhY2ggb3V0ZXIgdHJhaW5pbmcgZm9sZC4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IGstRm9sZCBGYWlscyBmb3IgVGltZSBTZXJpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRpbWUgc2VyaWVzIG9ic2VydmF0aW9ucyBhcmUgYXV0b2NvcnJlbGF0ZWQ6IHnigpwgZGVwZW5kcyBvbiB54oKc4oKL4oKBLCB54oKc4oKL4oKCLCBldGMuIFdoZW4gay1mb2xkIGFzc2lnbnMgZm9sZCBrIHRvIHRoZSB0ZXN0IHNldCBhbmQgdGhlIHJlbWFpbmluZyBmb2xkcyB0byB0cmFpbmluZywgb2JzZXJ2YXRpb25zIGZyb20gdCsxLCB0KzIsIC4uLiBhcmUgaW5jbHVkZWQgaW4gdGhlIHRyYWluaW5nIHNldCBldmVuIHRob3VnaCB0aGV5IG9jY3VyIGFmdGVyIHRlc3QgcG9pbnQgdC4gVGhpcyBpcyBmdXR1cmUgbGVha2FnZS4gQWRkaXRpb25hbGx5LCBhdXRvY29ycmVsYXRpb24gbWVhbnMgdGhhdCB0cmFpbmluZyBwb2ludHMganVzdCBiZWZvcmUgb3IgYWZ0ZXIgYSB0ZXN0IHBvaW50IGFyZSBuZWFybHkgaWRlbnRpY2FsIHRvIGl0LCBpbmZsYXRpbmcgYXBwYXJlbnQgYWNjdXJhY3kuIFRoZSBleHBlY3RlZCB2YWx1ZSBvZiB0aGUgay1mb2xkIE1TRSBlc3RpbWF0b3IgaXMgYmlhc2VkIGRvd253YXJkIHJlbGF0aXZlIHRvIHRoZSB0cnVlIG91dC1vZi1zYW1wbGUgTVNFIGZvciBhbnkgaG9yaXpvbiBoIOKJpSAxLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgbWVhbl9zcXVhcmVkX2Vycm9yXG5cbmRlZiB3YWxrX2ZvcndhcmRfZXhwYW5kaW5nKFgsIHksIG1pbl90cmFpbj02MCwgaG9yaXpvbj0xKTpcbiAgICBcIlwiXCJcbiAgICBFeHBhbmRpbmctd2luZG93IHdhbGstZm9yd2FyZCB2YWxpZGF0aW9uLlxuICAgIFRyYWluIG9uIFswLi50XSwgcHJlZGljdCB5W3QrMS4udCtob3Jpem9uXSwgYWR2YW5jZSBieSBob3Jpem9uLlxuICAgIFJldHVybnMgbGlzdCBvZiAoeV90cnVlLCB5X3ByZWQpIGFycmF5cy5cbiAgICBcIlwiXCJcbiAgICBuID0gbGVuKFgpXG4gICAgcmVzdWx0cyA9IFtdXG4gICAgdCA9IG1pbl90cmFpblxuICAgIHdoaWxlIHQgKyBob3Jpem9uIFx1MDAzYz0gbjpcbiAgICAgICAgWF90cmFpbiwgeV90cmFpbiA9IFhbOnRdLCB5Wzp0XVxuICAgICAgICBYX3Rlc3QsICB5X3RydWUgID0gWFt0OnQgKyBob3Jpem9uXSwgeVt0OnQgKyBob3Jpem9uXVxuICAgICAgICBtb2RlbCA9IFJpZGdlKGFscGhhPTEuMCkuZml0KFhfdHJhaW4sIHlfdHJhaW4pXG4gICAgICAgIHlfcHJlZCA9IG1vZGVsLnByZWRpY3QoWF90ZXN0KVxuICAgICAgICByZXN1bHRzLmFwcGVuZCgoeV90cnVlLCB5X3ByZWQpKVxuICAgICAgICB0ICs9IGhvcml6b25cbiAgICByZXR1cm4gcmVzdWx0c1xuXG5ucC5yYW5kb20uc2VlZCg0MilcblQgPSAyMDBcbnRfaWR4ID0gbnAuYXJhbmdlKFQpXG55ID0gMC42ICogbnAucm9sbCh0X2lkeCAqIDAsIDEpICsgbnAuY3Vtc3VtKG5wLnJhbmRvbS5yYW5kbihUKSkgKyA1MFxuWCA9IG5wLmNvbHVtbl9zdGFjayhbbnAucm9sbCh5LCBrKSBmb3IgayBpbiByYW5nZSgxLCA2KV0pWzU6XVxueV9hbGlnbmVkID0geVs1Ol1cblxucmVzdWx0cyA9IHdhbGtfZm9yd2FyZF9leHBhbmRpbmcoWCwgeV9hbGlnbmVkLCBtaW5fdHJhaW49NjAsIGhvcml6b249MSlcbmFsbF90cnVlID0gbnAuY29uY2F0ZW5hdGUoW3JbMF0gZm9yIHIgaW4gcmVzdWx0c10pXG5hbGxfcHJlZCA9IG5wLmNvbmNhdGVuYXRlKFtyWzFdIGZvciByIGluIHJlc3VsdHNdKVxucm1zZSA9IG5wLnNxcnQobWVhbl9zcXVhcmVkX2Vycm9yKGFsbF90cnVlLCBhbGxfcHJlZCkpXG5wcmludChmXHUwMDI3V2Fsay1mb3J3YXJkIFJNU0UgKGV4cGFuZGluZywgaD0xKToge3Jtc2U6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdGb2xkcyBldmFsdWF0ZWQ6IHtsZW4ocmVzdWx0cyl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6InNrbGVhcm4gVGltZVNlcmllc1NwbGl0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJzY2lraXQtbGVhcm5cdTAwMjdzIFRpbWVTZXJpZXNTcGxpdCBpbXBsZW1lbnRzIGV4cGFuZGluZy13aW5kb3cgdmFsaWRhdGlvbiB3aXRoIG5fc3BsaXRzIGZvbGRzLiBFYWNoIGZvbGQgYWRkcyByb3VnaGx5IGxlbihzZXJpZXMpL25fc3BsaXRzIG5ldyB0cmFpbmluZyBvYnNlcnZhdGlvbnMuIFRoZSB0ZXN0IHdpbmRvdyBpcyBmaXhlZCBhdCB0aGUgc2FtZSBsZW5ndGggYWNyb3NzIGZvbGRzLiBUaW1lU2VyaWVzU3BsaXQgaW50ZWdyYXRlcyB3aXRoIEdyaWRTZWFyY2hDViBhbmQgY3Jvc3NfdmFsX3Njb3JlLCBlbmFibGluZyBzdGFuZGFyZCBoeXBlcnBhcmFtZXRlciB0dW5pbmcgcGlwZWxpbmVzLiBVc2Ugbl9zcGxpdHMg4omlIDUgZm9yIHN0YWJsZSBhY2N1cmFjeSBlc3RpbWF0ZXMuIEZvciBtb2RlbHMgd2l0aCByb2xsaW5nIGZlYXR1cmVzLCBwYXNzIHRoZSBmdWxsIGRhdGFzZXQgaW5jbHVkaW5nIGxhZyBjb2x1bW5zIOKAlCB0aGUgc3BsaXQgdGFrZXMgY2FyZSBvZiB0ZW1wb3JhbCBvcmRlcmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgcGFuZGFzIGFzIHBkXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBSaWRnZVxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgVGltZVNlcmllc1NwbGl0LCBjcm9zc192YWxfc2NvcmVcbmZyb20gc2tsZWFybi5waXBlbGluZSBpbXBvcnQgUGlwZWxpbmVcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ucC5yYW5kb20uc2VlZCgwKVxuVCA9IDMwMFxudF9pZHggPSBucC5hcmFuZ2UoVClcbnkgPSBucC5zaW4oMiAqIG5wLnBpICogdF9pZHggLyAzMCkgKyAwLjUgKiBucC5jdW1zdW0obnAucmFuZG9tLnJhbmRuKFQpICogMC4xKVxuXG4jIExhZyBmZWF0dXJlc1xubGFncyA9IDEwXG5YID0gbnAuY29sdW1uX3N0YWNrKFtucC5yb2xsKHksIGspIGZvciBrIGluIHJhbmdlKDEsIGxhZ3MgKyAxKV0pW2xhZ3M6XVxueV9hbGlnbmVkID0geVtsYWdzOl1cblxudHNjdiA9IFRpbWVTZXJpZXNTcGxpdChuX3NwbGl0cz01KVxucGlwZSA9IFBpcGVsaW5lKFsoXHUwMDI3c2NhbGVyXHUwMDI3LCBTdGFuZGFyZFNjYWxlcigpKSwgKFx1MDAyN21vZGVsXHUwMDI3LCBSaWRnZShhbHBoYT0xLjApKV0pXG5cbnNjb3JlcyA9IGNyb3NzX3ZhbF9zY29yZShwaXBlLCBYLCB5X2FsaWduZWQsIGN2PXRzY3YsXG4gICAgICAgICAgICAgICAgICAgICAgICAgIHNjb3Jpbmc9XHUwMDI3bmVnX3Jvb3RfbWVhbl9zcXVhcmVkX2Vycm9yXHUwMDI3KVxuXG5wcmludChcdTAwMjdUaW1lU2VyaWVzU3BsaXQgUk1TRSBwZXIgZm9sZDpcdTAwMjcpXG5mb3IgaSwgcyBpbiBlbnVtZXJhdGUoc2NvcmVzLCAxKTpcbiAgICBwcmludChmXHUwMDI3ICBGb2xkIHtpfTogUk1TRSA9IHstczouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01lYW4gUk1TRSA9IHstc2NvcmVzLm1lYW4oKTouNGZ9IMKxIHtzY29yZXMuc3RkKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSb2xsaW5nIHZzIEV4cGFuZGluZyBXaW5kb3cifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV4cGFuZGluZyB3aW5kb3c6IHRyYWluaW5nIHNldCBncm93cyB3aXRoIGVhY2ggZm9sZCAoYWxsIHBhc3QgZGF0YSB1c2VkKS4gQWR2YW50YWdlOiBtYXhpbXVtIHRyYWluaW5nIGRhdGEgaW4gbGF0ZXIgZm9sZHM7IGRpc2FkdmFudGFnZTogZWFybHkgZGF0YSBtYXkgYmUgbm9uLXN0YXRpb25hcnkgb3IgZm9sbG93IGEgZGlmZmVyZW50IHJlZ2ltZS4gUm9sbGluZyB3aW5kb3c6IHRyYWluaW5nIHNldCBzaXplIGlzIGZpeGVkIGF0IFcgb2JzZXJ2YXRpb25zIGFuZCBzbGlkZXMgZm9yd2FyZCB3aXRoIGVhY2ggZm9sZC4gQWR2YW50YWdlOiB0cmFpbmluZyBkaXN0cmlidXRpb24gaXMgbW9yZSBob21vZ2VuZW91czsgZGlzYWR2YW50YWdlOiBkaXNjYXJkcyB1c2VmdWwgb2xkZXIgZGF0YS4gUm9sbGluZyBpcyBwcmVmZXJyZWQgd2hlbiB0aGUgc2VyaWVzIGhhcyBzdHJ1Y3R1cmFsIGJyZWFrcyBvciByZWdpbWUgY2hhbmdlczsgZXhwYW5kaW5nIGlzIHByZWZlcnJlZCB3aGVuIHRoZSBzZXJpZXMgaXMgc3RhdGlvbmFyeSBhbmQgZGF0YSBpcyBzY2FyY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUmlkZ2VcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBtZWFuX3NxdWFyZWRfZXJyb3JcblxuZGVmIHdhbGtfZm9yd2FyZChYLCB5LCBtaW5fdHJhaW49NjAsIGhvcml6b249MSwgd2luZG93PU5vbmUpOlxuICAgIFwiXCJcIldhbGstZm9yd2FyZCB2YWxpZGF0aW9uLiB3aW5kb3c9Tm9uZSDihpIgZXhwYW5kaW5nOyB3aW5kb3c9aW50IOKGkiByb2xsaW5nLlwiXCJcIlxuICAgIG4gPSBsZW4oWClcbiAgICBybXNlcyA9IFtdXG4gICAgdCA9IG1pbl90cmFpblxuICAgIHdoaWxlIHQgKyBob3Jpem9uIFx1MDAzYz0gbjpcbiAgICAgICAgc3RhcnQgPSAwIGlmIHdpbmRvdyBpcyBOb25lIGVsc2UgbWF4KDAsIHQgLSB3aW5kb3cpXG4gICAgICAgIFhfdHJhaW4sIHlfdHJhaW4gPSBYW3N0YXJ0OnRdLCB5W3N0YXJ0OnRdXG4gICAgICAgIFhfdGVzdCwgIHlfdHJ1ZSAgPSBYW3Q6dCArIGhvcml6b25dLCB5W3Q6dCArIGhvcml6b25dXG4gICAgICAgIHlfcHJlZCA9IFJpZGdlKGFscGhhPTEuMCkuZml0KFhfdHJhaW4sIHlfdHJhaW4pLnByZWRpY3QoWF90ZXN0KVxuICAgICAgICBybXNlcy5hcHBlbmQobnAuc3FydChtZWFuX3NxdWFyZWRfZXJyb3IoeV90cnVlLCB5X3ByZWQpKSlcbiAgICAgICAgdCArPSBob3Jpem9uXG4gICAgcmV0dXJuIHJtc2VzXG5cbm5wLnJhbmRvbS5zZWVkKDEpXG5UID0gMjUwXG55ID0gbnAuc2luKG5wLmFyYW5nZShUKSAqIDAuMykgKyBucC5jdW1zdW0obnAucmFuZG9tLnJhbmRuKFQpICogMC4xNSlcblggPSBucC5jb2x1bW5fc3RhY2soW25wLnJvbGwoeSwgaykgZm9yIGsgaW4gcmFuZ2UoMSwgOCldKVs3Ol1cbnlfYSA9IHlbNzpdXG5cbmV4cF9ybXNlcyAgPSB3YWxrX2ZvcndhcmQoWCwgeV9hLCB3aW5kb3c9Tm9uZSlcbnJvbGxfcm1zZXMgPSB3YWxrX2ZvcndhcmQoWCwgeV9hLCB3aW5kb3c9NjApXG5wcmludChmXHUwMDI3RXhwYW5kaW5nIHdpbmRvdzogbWVhbiBSTVNFID0ge25wLm1lYW4oZXhwX3Jtc2VzKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JvbGxpbmcgd2luZG93IDYwOiBtZWFuIFJNU0UgPSB7bnAubWVhbihyb2xsX3Jtc2VzKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdhcCBQYXJhbWV0ZXIgdG8gUHJldmVudCBGZWF0dXJlIExlYWthZ2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gdXNpbmcgcm9sbGluZyBmZWF0dXJlcyAocm9sbGluZyBtZWFuLCByb2xsaW5nIHN0ZCkgd2l0aCB3aW5kb3cgdywgdGhlIGZlYXR1cmUgZm9yIG9ic2VydmF0aW9uIHQgaW5jbHVkZXMgb2JzZXJ2YXRpb25zIHVwIHRvIHQtMS4gSWYgdHJhaW5pbmcgZW5kcyBhdCB0IGFuZCB0aGUgdGVzdCBwb2ludCBpcyB0KzEsIHRoZXJlIGlzIG5vIHByb2JsZW0uIEJ1dCBpZiByb2xsaW5nIGZlYXR1cmVzIGZvciB0aGUgdGVzdCBwb2ludCBpbmNsdWRlIG9ic2VydmF0aW9ucyBmcm9tIHZlcnkgY2xvc2UgdG8gdGhlIHRyYWluL3Rlc3QgYm91bmRhcnksIGFueSBsYWcgc2hvcnRlciB0aGFuIHRoZSBmZWF0dXJlIHdpbmRvdyBjYW4gaW50cm9kdWNlIGxlYWthZ2UuIEEgZ2FwIG9mIGcgcGVyaW9kcyBiZXR3ZWVuIHRoZSBsYXN0IHRyYWluaW5nIHBvaW50IGFuZCB0aGUgZmlyc3QgdGVzdCBwb2ludCBlbnN1cmVzIGFsbCBvdmVybGFwcGluZyB3aW5kb3dzIGFyZSBzYWZlbHkgaW4gdGhlIHBhc3QsIGVsaW1pbmF0aW5nIHRoaXMgc3VidGxlIGxlYWthZ2UgY2hhbm5lbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBSaWRnZVxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IG1lYW5fc3F1YXJlZF9lcnJvclxuXG5kZWYgd2Fsa19mb3J3YXJkX3dpdGhfZ2FwKFgsIHksIG1pbl90cmFpbj02MCwgaG9yaXpvbj0xLCBnYXA9MCk6XG4gICAgXCJcIlwiV2Fsay1mb3J3YXJkIHZhbGlkYXRpb24gd2l0aCBhIGdhcCBiZXR3ZWVuIHRyYWluIGVuZCBhbmQgdGVzdCBzdGFydC5cIlwiXCJcbiAgICBuID0gbGVuKFgpXG4gICAgcmVzdWx0cyA9IFtdXG4gICAgdCA9IG1pbl90cmFpblxuICAgIHdoaWxlIHQgKyBnYXAgKyBob3Jpem9uIFx1MDAzYz0gbjpcbiAgICAgICAgWF90cmFpbiwgeV90cmFpbiA9IFhbOnRdLCAgICAgICAgICAgICAgeVs6dF1cbiAgICAgICAgWF90ZXN0LCAgeV90cnVlICA9IFhbdCtnYXA6dCtnYXAraG9yaXpvbl0sIHlbdCtnYXA6dCtnYXAraG9yaXpvbl1cbiAgICAgICAgeV9wcmVkID0gUmlkZ2UoYWxwaGE9MS4wKS5maXQoWF90cmFpbiwgeV90cmFpbikucHJlZGljdChYX3Rlc3QpXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKG5wLnNxcnQobWVhbl9zcXVhcmVkX2Vycm9yKHlfdHJ1ZSwgeV9wcmVkKSkpXG4gICAgICAgIHQgKz0gaG9yaXpvblxuICAgIHJldHVybiByZXN1bHRzXG5cbm5wLnJhbmRvbS5zZWVkKDIpXG5UID0gMzAwXG55ID0gbnAuY3Vtc3VtKG5wLnJhbmRvbS5yYW5kbihUKSkgKyA1MFxuWCA9IG5wLmNvbHVtbl9zdGFjayhbbnAucm9sbCh5LCBrKSBmb3IgayBpbiByYW5nZSgxLCA4KV0pWzc6XVxueV9hID0geVs3Ol1cblxuZm9yIGdhcCBpbiBbMCwgMywgNywgMTRdOlxuICAgIHJtc2VzID0gd2Fsa19mb3J3YXJkX3dpdGhfZ2FwKFgsIHlfYSwgZ2FwPWdhcClcbiAgICBwcmludChmXHUwMDI3R2FwPXtnYXA6MmR9ICBtZWFuIFJNU0U9e25wLm1lYW4ocm1zZXMpOi40Zn0gIGZvbGRzPXtsZW4ocm1zZXMpfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6Ik5lc3RlZCBDViBmb3IgSHlwZXJwYXJhbWV0ZXIgVHVuaW5nIiwiY29udGVudCI6IkRvIG5vdCB0dW5lIGh5cGVycGFyYW1ldGVycyB1c2luZyB0aGUgc2FtZSB3YWxrLWZvcndhcmQgbG9vcCB1c2VkIGZvciBmaW5hbCBldmFsdWF0aW9uIOKAlCB0aGlzIGludHJvZHVjZXMgb3B0aW1pc3RpYyBiaWFzLiBVc2UgbmVzdGVkIENWOiBhbiBvdXRlciB3YWxrLWZvcndhcmQgbG9vcCBmb3IgdW5iaWFzZWQgYWNjdXJhY3kgZXN0aW1hdGlvbiwgYW5kIGFuIGlubmVyIFRpbWVTZXJpZXNTcGxpdCBmb3IgaHlwZXJwYXJhbWV0ZXIgc2VhcmNoIHdpdGhpbiBlYWNoIG91dGVyIHRyYWluaW5nIGZvbGQuIE9ubHkgdGhlIG91dGVyIGxvb3AgUk1TRSBzaG91bGQgYmUgcmVwb3J0ZWQgYXMgdGhlIG1vZGVsXHUwMDI3cyBleHBlY3RlZCBhY2N1cmFjeS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gZXZhbHVhdGluZyBtdWx0aS1zdGVwIG1vZGVscywgdGhlIHdhbGstZm9yd2FyZCBsb29wIHNob3VsZCBzdHJpZGUgYnkgSCAodGhlIGZ1bGwgZm9yZWNhc3QgaG9yaXpvbikgcmF0aGVyIHRoYW4gMSwgc28gZWFjaCB0ZXN0IGJsb2NrIGNvdmVycyBleGFjdGx5IG9uZSBub24tb3ZlcmxhcHBpbmcgSC1zdGVwIHdpbmRvdy4gU3RyaWRpbmcgYnkgMSBjcmVhdGVzIG92ZXJsYXBwaW5nIHdpbmRvd3MgdGhhdCBpbmZsYXRlIHRoZSBudW1iZXIgb2YgZm9sZHMgYW5kIGludHJvZHVjZSBjb3JyZWxhdGlvbiBiZXR3ZWVuIGZvbGQgZXJyb3JzLCBtYWtpbmcgdGhlIG1lYW4gUk1TRSBhcnRpZmljaWFsbHkgcHJlY2lzZS4gU3RyaWRlID0gSCBnaXZlcyBpbmRlcGVuZGVudCBldmFsdWF0aW9uIHdpbmRvd3Mgd2hvc2UgUk1TRSBlc3RpbWF0ZXMgYXJlIGFzeW1wdG90aWNhbGx5IHVuY29ycmVsYXRlZCBhcyB0aGUgc2VyaWVzIGdyb3dzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZhbGlkYXRpb24gU3RyYXRlZ3kgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJTdHJhdGVneSIsIkxlYWthZ2UiLCJWYXJpYW5jZSIsIkNvbXB1dGUiLCJIeXBlci1UdW5pbmciLCJCZXN0IEZvciJdLCJyb3dzIjpbWyJrLUZvbGQgKHJhbmRvbSkiLCJIaWdoIOKAlCBmdXR1cmUgaW4gdHJhaW4iLCJMb3ciLCJMb3ciLCJTdGFuZGFyZCBDViIsIk5vbi10ZW1wb3JhbCBkYXRhIG9ubHkiXSxbIlNpbmdsZSBob2xkb3V0IiwiTm9uZSIsIkhpZ2giLCJWZXJ5IGxvdyIsIk5vbmUiLCJWZXJ5IGxhcmdlIGRhdGFzZXRzIl0sWyJFeHBhbmRpbmcgd2Fsay1mb3J3YXJkIiwiTm9uZSIsIk1lZGl1bSIsIk1lZGl1bSIsIk5lc3RlZCBpbm5lciBDViIsIlN0YXRpb25hcnkgc2VyaWVzIl0sWyJSb2xsaW5nIHdhbGstZm9yd2FyZCIsIk5vbmUiLCJNZWRpdW0iLCJNZWRpdW0iLCJOZXN0ZWQgaW5uZXIgQ1YiLCJOb24tc3RhdGlvbmFyeSAvIHJlZ2ltZSBjaGFuZ2UiXSxbIldhbGstZm9yd2FyZCArIGdhcCIsIk5vbmUiLCJTbGlnaHRseSBoaWdoZXIiLCJNZWRpdW0iLCJOZXN0ZWQgaW5uZXIgQ1YiLCJTZXJpZXMgd2l0aCBsb25nIHJvbGxpbmcgZmVhdHVyZXMiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTmV2ZXIgdXNlIHNrbGVhcm5cdTAwMjdzIEtGb2xkIG9yIFN0cmF0aWZpZWRLRm9sZCBmb3IgdGltZS1zZXJpZXMgQ1Yg4oCUIHVzZSBUaW1lU2VyaWVzU3BsaXQgb3IgYSBjdXN0b20gd2Fsay1mb3J3YXJkIGxvb3AuIiwiU2V0IHRoZSBnYXAgZXF1YWwgdG8gdGhlIG1heGltdW0gcm9sbGluZyB3aW5kb3cgc2l6ZSB0byBlbGltaW5hdGUgZmVhdHVyZSBsZWFrYWdlIGFjcm9zcyBmb2xkcy4iLCJVc2UgYXQgbGVhc3QgNSBmb2xkcyBmb3Igc3RhYmxlIFJNU0UgZXN0aW1hdGVzIOKAlCBmZXdlciBmb2xkcyBwcm9kdWNlIGhpZ2gtdmFyaWFuY2UgYWNjdXJhY3kgbnVtYmVycy4iLCJSZXBvcnQgYWNjdXJhY3kgYXMgbWVhbiDCsSBzdGQgYWNyb3NzIGZvbGRzOyBhIGhpZ2ggc3RkIGluZGljYXRlcyB0aGUgbW9kZWwgaXMgc2Vuc2l0aXZlIHRvIHRoZSB0cmFpbmluZyBwZXJpb2QuIiwiRm9yIG11bHRpLXN0ZXAgZm9yZWNhc3RpbmcsIGFsaWduIHRoZSB0ZXN0IHdpbmRvdyB3aXRoIHRoZSBmb3JlY2FzdCBob3Jpem9uIGggdG8gZXZhbHVhdGUgYWNjdXJhY3kgYXQgdGhlIGhvcml6b24gb2YgaW50ZXJlc3QuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2Fsay1mb3J3YXJkIHZhbGlkYXRpb24gZ2VuZXJhbGlzZXMgbmF0dXJhbGx5IHRvIHBhbmVsIChtdWx0aS1zZXJpZXMpIGRhdGFzZXRzLiBGb3IgTiBzZXJpZXMgd2l0aCBhIHNoYXJlZCB0ZW1wb3JhbCBpbmRleCwgYXBwbHkgdGhlIHNhbWUgdGVtcG9yYWwgY3V0b2ZmIGFjcm9zcyBhbGwgc2VyaWVzIHNpbXVsdGFuZW91c2x5IOKAlCBuZXZlciBhbGxvdyBzb21lIHNlcmllcyB0byBjb250cmlidXRlIHBvc3QtY3V0b2ZmIG9ic2VydmF0aW9ucyB0byB0aGUgdHJhaW5pbmcgZm9sZHMgZm9yIG90aGVyIHNlcmllcy4gVGhlIGZvbGQtbGV2ZWwgUk1TRSBiZWNvbWVzIGFuIGF2ZXJhZ2Ugb3ZlciBhbGwgTiBzZXJpZXMgaW4gdGhlIHRlc3Qgd2luZG93LCBwcm92aWRpbmcgYSBnbG9iYWwgYWNjdXJhY3kgZXN0aW1hdGUgdGhhdCBhY2NvdW50cyBmb3IgY3Jvc3Mtc2VyaWVzIHZhcmlhYmlsaXR5IGluIGRpZmZpY3VsdHkgYW5kIHNjYWxlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gcHJvZHVjdGlvbiBmb3JlY2FzdGluZyBwaXBlbGluZXMsIGltcGxlbWVudCB0aGUgd2Fsay1mb3J3YXJkIGxvb3AgdG8gbWF0Y2ggdGhlIHJlYWwgZGVwbG95bWVudCBjYWRlbmNlLiBJZiB0aGUgbW9kZWwgaXMgcmV0cmFpbmVkIHdlZWtseSBhbmQgZm9yZWNhc3RzIDQgd2Vla3MgYWhlYWQsIHRoZSB2YWxpZGF0aW9uIGxvb3Agc2hvdWxkIHN0cmlkZSBieSAxIHdlZWssIHVzZSBhIGhvcml6b24gb2YgNCB3ZWVrcywgYW5kIGFwcGx5IHRoZSBzYW1lIGZlYXR1cmUgY29tcHV0YXRpb24gcGlwZWxpbmUgdGhhdCB3aWxsIGJlIHVzZWQgaW4gcHJvZHVjdGlvbiDigJQgaW5jbHVkaW5nIGFueSBkYXRhIGNsZWFuaW5nLCBvdXRsaWVyIGhhbmRsaW5nLCBhbmQgY2FsZW5kYXIgZmVhdHVyZSBnZW5lcmF0aW9uIHN0ZXBzLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Walk-Forward Validation — Preventing Data Leakage Through Time

Standard k-fold cross-validation randomly assigns observations to folds, allowing future observations to appear in the training set. For time series this constitutes data leakage: the model sees future information during training, and in-sample error metrics severely underestimate true test error. Walk-forward validation (also called rolling-origin evaluation) respects the temporal ordering — the model is always trained on past data and evaluated on future data — producing unbiased estimates of forecast accuracy at the desired horizon.

- Walk-forward evaluation always trains on past data and tests on future data — no shuffling.
- Expanding window: training set grows each fold; best for stationary series with limited data.
- Rolling window: fixed training size slides forward; best for non-stationary or regime-changing series.
- Gap: buffer periods between train end and test start prevent feature window contamination.
- Nested CV: use an inner walk-forward loop for hyperparameter tuning within each outer training fold.

## Why k-Fold Fails for Time Series

Time series observations are autocorrelated: yₜ depends on yₜ₋₁, yₜ₋₂, etc. When k-fold assigns fold k to the test set and the remaining folds to training, observations from t+1, t+2, ... are included in the training set even though they occur after test point t. This is future leakage. Additionally, autocorrelation means that training points just before or after a test point are nearly identical to it, inflating apparent accuracy. The expected value of the k-fold MSE estimator is biased downward relative to the true out-of-sample MSE for any horizon h ≥ 1.

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def walk_forward_expanding(X, y, min_train=60, horizon=1):
    """
    Expanding-window walk-forward validation.
    Train on [0..t], predict y[t+1..t+horizon], advance by horizon.
    Returns list of (y_true, y_pred) arrays.
    """
    n = len(X)
    results = []
    t = min_train
    while t + horizon <= n:
        X_train, y_train = X[:t], y[:t]
        X_test,  y_true  = X[t:t + horizon], y[t:t + horizon]
        model = Ridge(alpha=1.0).fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results.append((y_true, y_pred))
        t += horizon
    return results

np.random.seed(42)
T = 200
t_idx = np.arange(T)
y = 0.6 * np.roll(t_idx * 0, 1) + np.cumsum(np.random.randn(T)) + 50
X = np.column_stack([np.roll(y, k) for k in range(1, 6)])[5:]
y_aligned = y[5:]

results = walk_forward_expanding(X, y_aligned, min_train=60, horizon=1)
all_true = np.concatenate([r[0] for r in results])
all_pred = np.concatenate([r[1] for r in results])
rmse = np.sqrt(mean_squared_error(all_true, all_pred))
print(f'Walk-forward RMSE (expanding, h=1): {rmse:.4f}')
print(f'Folds evaluated: {len(results)}')
```

## sklearn TimeSeriesSplit

scikit-learn's TimeSeriesSplit implements expanding-window validation with n_splits folds. Each fold adds roughly len(series)/n_splits new training observations. The test window is fixed at the same length across folds. TimeSeriesSplit integrates with GridSearchCV and cross_val_score, enabling standard hyperparameter tuning pipelines. Use n_splits ≥ 5 for stable accuracy estimates. For models with rolling features, pass the full dataset including lag columns — the split takes care of temporal ordering.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(0)
T = 300
t_idx = np.arange(T)
y = np.sin(2 * np.pi * t_idx / 30) + 0.5 * np.cumsum(np.random.randn(T) * 0.1)

# Lag features
lags = 10
X = np.column_stack([np.roll(y, k) for k in range(1, lags + 1)])[lags:]
y_aligned = y[lags:]

tscv = TimeSeriesSplit(n_splits=5)
pipe = Pipeline([('scaler', StandardScaler()), ('model', Ridge(alpha=1.0))])

scores = cross_val_score(pipe, X, y_aligned, cv=tscv,
                          scoring='neg_root_mean_squared_error')

print('TimeSeriesSplit RMSE per fold:')
for i, s in enumerate(scores, 1):
    print(f'  Fold {i}: RMSE = {-s:.4f}')
print(f'Mean RMSE = {-scores.mean():.4f} ± {scores.std():.4f}')
```

## Rolling vs Expanding Window

Expanding window: training set grows with each fold (all past data used). Advantage: maximum training data in later folds; disadvantage: early data may be non-stationary or follow a different regime. Rolling window: training set size is fixed at W observations and slides forward with each fold. Advantage: training distribution is more homogeneous; disadvantage: discards useful older data. Rolling is preferred when the series has structural breaks or regime changes; expanding is preferred when the series is stationary and data is scarce.

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def walk_forward(X, y, min_train=60, horizon=1, window=None):
    """Walk-forward validation. window=None → expanding; window=int → rolling."""
    n = len(X)
    rmses = []
    t = min_train
    while t + horizon <= n:
        start = 0 if window is None else max(0, t - window)
        X_train, y_train = X[start:t], y[start:t]
        X_test,  y_true  = X[t:t + horizon], y[t:t + horizon]
        y_pred = Ridge(alpha=1.0).fit(X_train, y_train).predict(X_test)
        rmses.append(np.sqrt(mean_squared_error(y_true, y_pred)))
        t += horizon
    return rmses

np.random.seed(1)
T = 250
y = np.sin(np.arange(T) * 0.3) + np.cumsum(np.random.randn(T) * 0.15)
X = np.column_stack([np.roll(y, k) for k in range(1, 8)])[7:]
y_a = y[7:]

exp_rmses  = walk_forward(X, y_a, window=None)
roll_rmses = walk_forward(X, y_a, window=60)
print(f'Expanding window: mean RMSE = {np.mean(exp_rmses):.4f}')
print(f'Rolling window 60: mean RMSE = {np.mean(roll_rmses):.4f}')
```

## Gap Parameter to Prevent Feature Leakage

When using rolling features (rolling mean, rolling std) with window w, the feature for observation t includes observations up to t-1. If training ends at t and the test point is t+1, there is no problem. But if rolling features for the test point include observations from very close to the train/test boundary, any lag shorter than the feature window can introduce leakage. A gap of g periods between the last training point and the first test point ensures all overlapping windows are safely in the past, eliminating this subtle leakage channel.

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def walk_forward_with_gap(X, y, min_train=60, horizon=1, gap=0):
    """Walk-forward validation with a gap between train end and test start."""
    n = len(X)
    results = []
    t = min_train
    while t + gap + horizon <= n:
        X_train, y_train = X[:t],              y[:t]
        X_test,  y_true  = X[t+gap:t+gap+horizon], y[t+gap:t+gap+horizon]
        y_pred = Ridge(alpha=1.0).fit(X_train, y_train).predict(X_test)
        results.append(np.sqrt(mean_squared_error(y_true, y_pred)))
        t += horizon
    return results

np.random.seed(2)
T = 300
y = np.cumsum(np.random.randn(T)) + 50
X = np.column_stack([np.roll(y, k) for k in range(1, 8)])[7:]
y_a = y[7:]

for gap in [0, 3, 7, 14]:
    rmses = walk_forward_with_gap(X, y_a, gap=gap)
    print(f'Gap={gap:2d}  mean RMSE={np.mean(rmses):.4f}  folds={len(rmses)}')
```

> **Nested CV for Hyperparameter Tuning**: Do not tune hyperparameters using the same walk-forward loop used for final evaluation — this introduces optimistic bias. Use nested CV: an outer walk-forward loop for unbiased accuracy estimation, and an inner TimeSeriesSplit for hyperparameter search within each outer training fold. Only the outer loop RMSE should be reported as the model's expected accuracy.

When evaluating multi-step models, the walk-forward loop should stride by H (the full forecast horizon) rather than 1, so each test block covers exactly one non-overlapping H-step window. Striding by 1 creates overlapping windows that inflate the number of folds and introduce correlation between fold errors, making the mean RMSE artificially precise. Stride = H gives independent evaluation windows whose RMSE estimates are asymptotically uncorrelated as the series grows.

## Validation Strategy Comparison

| Strategy | Leakage | Variance | Compute | Hyper-Tuning | Best For |
| --- | --- | --- | --- | --- | --- |
| k-Fold (random) | High — future in train | Low | Low | Standard CV | Non-temporal data only |
| Single holdout | None | High | Very low | None | Very large datasets |
| Expanding walk-forward | None | Medium | Medium | Nested inner CV | Stationary series |
| Rolling walk-forward | None | Medium | Medium | Nested inner CV | Non-stationary / regime change |
| Walk-forward + gap | None | Slightly higher | Medium | Nested inner CV | Series with long rolling features |

- Never use sklearn's KFold or StratifiedKFold for time-series CV — use TimeSeriesSplit or a custom walk-forward loop.
- Set the gap equal to the maximum rolling window size to eliminate feature leakage across folds.
- Use at least 5 folds for stable RMSE estimates — fewer folds produce high-variance accuracy numbers.
- Report accuracy as mean ± std across folds; a high std indicates the model is sensitive to the training period.
- For multi-step forecasting, align the test window with the forecast horizon h to evaluate accuracy at the horizon of interest.

Walk-forward validation generalises naturally to panel (multi-series) datasets. For N series with a shared temporal index, apply the same temporal cutoff across all series simultaneously — never allow some series to contribute post-cutoff observations to the training folds for other series. The fold-level RMSE becomes an average over all N series in the test window, providing a global accuracy estimate that accounts for cross-series variability in difficulty and scale.

In production forecasting pipelines, implement the walk-forward loop to match the real deployment cadence. If the model is retrained weekly and forecasts 4 weeks ahead, the validation loop should stride by 1 week, use a horizon of 4 weeks, and apply the same feature computation pipeline that will be used in production — including any data cleaning, outlier handling, and calendar feature generation steps.

---

