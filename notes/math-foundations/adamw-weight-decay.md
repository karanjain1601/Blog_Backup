---
title: "AdamW — Decoupled Weight Decay"
slug: "adamw-weight-decay"
description: "Why adding L2 regularization to Adam is not equivalent to weight decay (the effective regularization is parameter-dependent), how AdamW decouples weight decay from the gradient update to achieve uniform regularization, and why this matters for transformer pretraining."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBQcm9ibGVtIHdpdGggQWRhbSArIEwyIFJlZ3VsYXJpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbmFpdmUgYXBwcm9hY2ggdG8gcmVndWxhcml6YXRpb24gd2l0aCBBZGFtIGlzIHRvIGFkZCDOu+KAls644oCWwrIgdG8gdGhlIGxvc3MsIHdoaWNoIGFkZHMgzrvOuCB0byB0aGUgZ3JhZGllbnQuIEFkYW0gdGhlbiBzY2FsZXMgdGhpcyBtb2RpZmllZCBncmFkaWVudCBieSAxL+KImnbMgiwgc28gdGhlIGVmZmVjdGl2ZSByZWd1bGFyaXphdGlvbiBmb3IgcGFyYW1ldGVyIGkgaXMgzrvOuF9pIC8g4oiadsyCX2kuIFBhcmFtZXRlcnMgd2l0aCBsYXJnZSBncmFkaWVudCB2YXJpYW5jZSAobGFyZ2UgdsyCKSByZWNlaXZlIHdlYWtlciByZWd1bGFyaXphdGlvbiB0aGFuIGludGVuZGVkLCB3aGlsZSBwYXJhbWV0ZXJzIHdpdGggc21hbGwgZ3JhZGllbnQgdmFyaWFuY2UgcmVjZWl2ZSBzdHJvbmdlciByZWd1bGFyaXphdGlvbi4gVGhpcyBub24tdW5pZm9ybSBlZmZlY3RpdmUgcmVndWxhcml6YXRpb24gZGVmZWF0cyB0aGUgcHVycG9zZSBvZiBMMiBhbmQgbGVhZHMgdG8gd29yc2UgZ2VuZXJhbGl6YXRpb24sIGVzcGVjaWFsbHkgZm9yIHBhcmFtZXRlcnMgaW4gZGVuc2UgbGF5ZXJzIHZzLiBzcGFyc2UgZW1iZWRkaW5nIGxheWVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcblxuIyBEZW1vbnN0cmF0ZSB0aGF0IEFkYW0rTDIgIT0gd2VpZ2h0IGRlY2F5XG4jIEZvciBBZGFtOiBlZmZlY3RpdmUgTDIgb24gcGFyYW0gaSA9IGxhbWJkYSAvIHNxcnQodl9oYXRfaSlcbiMgRm9yIEFkYW1XOiBlZmZlY3RpdmUgd2VpZ2h0IGRlY2F5ID0gbGFtYmRhICh1bmlmb3JtKVxuXG5ucC5yYW5kb20uc2VlZCg0MilcbiMgU2ltdWxhdGUgdHdvIHBhcmFtZXRlcnM6IG9uZSB3aXRoIGhpZ2ggZ3JhZGllbnQgdmFyaWFuY2UsIG9uZSB3aXRoIGxvd1xuVCA9IDEwMFxubGFtYmRhX3dkID0gMC4wMVxuYmV0YTIsIGVwcyA9IDAuOTk5LCAxZS04XG5cbnZfaGlnaCA9IDAuMCAgICMgdHJhY2tzIHYgZm9yIGhpZ2gtdmFyaWFuY2UgcGFyYW1cbnZfbG93ID0gMC4wICAgICMgdHJhY2tzIHYgZm9yIGxvdy12YXJpYW5jZSBwYXJhbVxuZWZmX2wyX2hpZ2gsIGVmZl9sMl9sb3cgPSBbXSwgW11cblxuZm9yIHQgaW4gcmFuZ2UoMSwgVCArIDEpOlxuICAgIGdfaGlnaCA9IDEwLjAgKiBucC5yYW5kb20ucmFuZG4oKSAgICMgaGlnaCBncmFkaWVudCB2YXJpYW5jZVxuICAgIGdfbG93ID0gMC4wMSAqIG5wLnJhbmRvbS5yYW5kbigpICAgICMgbG93IGdyYWRpZW50IHZhcmlhbmNlXG4gICAgdl9oaWdoID0gYmV0YTIgKiB2X2hpZ2ggKyAoMSAtIGJldGEyKSAqIGdfaGlnaCoqMlxuICAgIHZfbG93ICA9IGJldGEyICogdl9sb3cgICsgKDEgLSBiZXRhMikgKiBnX2xvdyoqMlxuICAgIHZfaGF0X2hpZ2ggPSB2X2hpZ2ggLyAoMSAtIGJldGEyKip0KVxuICAgIHZfaGF0X2xvdyAgPSB2X2xvdyAgLyAoMSAtIGJldGEyKip0KVxuICAgICMgRWZmZWN0aXZlIEwyID0gbGFtYmRhIC8gc3FydCh2X2hhdCk6IHNtYWxsZXIgZm9yIGhpZ2gtdmFyaWFuY2UgcGFyYW1zXG4gICAgZWZmX2wyX2hpZ2guYXBwZW5kKGxhbWJkYV93ZCAvIChucC5zcXJ0KHZfaGF0X2hpZ2gpICsgZXBzKSlcbiAgICBlZmZfbDJfbG93LmFwcGVuZChsYW1iZGFfd2QgLyAobnAuc3FydCh2X2hhdF9sb3cpICsgZXBzKSlcblxucHJpbnQoZlx1MDAyN0VmZmVjdGl2ZSBMMiAoaGlnaC12YXIgcGFyYW0pOiB7bnAubWVhbihlZmZfbDJfaGlnaFs1MDpdKTouNmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0VmZmVjdGl2ZSBMMiAobG93LXZhciAgcGFyYW0pOiB7bnAubWVhbihlZmZfbDJfbG93WzUwOl0pOi42Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3QWRhbVcgd2VpZ2h0IGRlY2F5ICh1bmlmb3JtKTogIHtsYW1iZGFfd2Q6LjZmfVx1MDAyNylcbnByaW50KFx1MDAyN0FkYW0rTDIgcmVndWxhcml6YXRpb24gaXMgTk9OLVVOSUZPUk07IEFkYW1XIGlzIFVOSUZPUk1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVjb3VwbGVkIFdlaWdodCBEZWNheSBpbiBBZGFtVyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWRhbVcgKExvc2hjaGlsb3YgXHUwMDI2IEh1dHRlciwgMjAxOSkgZGVjb3VwbGVzIHdlaWdodCBkZWNheSBmcm9tIHRoZSBncmFkaWVudCB1cGRhdGU6IM64X3t0KzF9ID0gKDEg4oiSIM63zrspIM64X3Qg4oiSIM63IG3Mgl90IC8gKOKImnbMgl90ICsgzrUpLiBUaGUgd2VpZ2h0IGRlY2F5IHRlcm0gKDEg4oiSIM63zrspIGlzIGFwcGxpZWQgZGlyZWN0bHkgdG8gdGhlIHBhcmFtZXRlcnMsIGluZGVwZW5kZW50bHkgb2YgdGhlIGdyYWRpZW50IG1hZ25pdHVkZS4gVGhpcyBnaXZlcyBldmVyeSBwYXJhbWV0ZXIgdGhlIHNhbWUgZnJhY3Rpb25hbCBzaHJpbmthZ2UgzrfOuyBwZXIgc3RlcCwgcmVnYXJkbGVzcyBvZiBpdHMgZ3JhZGllbnQgaGlzdG9yeS4gVGhlIGdyYWRpZW50IHVwZGF0ZSBtzIIvKOKImnbMgivOtSkgaXMgdW5jaGFuZ2VkIGZyb20gQWRhbSBhbmQgaGFuZGxlcyB0aGUgYWRhcHRpdmUgc2NhbGluZy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkFkYW1XIGlzIE5vdyB0aGUgU3RhbmRhcmQiLCJjb250ZW50IjoiQWRhbVcgaXMgdGhlIGRlZmF1bHQgb3B0aW1pemVyIGZvciB2aXJ0dWFsbHkgYWxsIGxhcmdlIHRyYW5zZm9ybWVyIG1vZGVsczogR1BULTIvMy80LCBCRVJULCBUNSwgTExhTUEsIGFuZCBtb3N0IG1vZGVybiB2aXNpb24gdHJhbnNmb3JtZXJzIHVzZSBBZGFtVyB3aXRoIGxyfjNlLTQgYW5kIHdlaWdodCBkZWNheX4wLjEuIFRoZSBkaWZmZXJlbmNlIGZyb20gQWRhbStMMiBpcyBlc3BlY2lhbGx5IHByb25vdW5jZWQgZm9yIGVtYmVkZGluZyBsYXllcnMsIHdoaWNoIGhhdmUgc3BhcnNlIGdyYWRpZW50cyBhbmQgbGFyZ2UgdsyCIOKAlCBMMiBiYXJlbHkgYWZmZWN0cyB0aGVtLCB3aGlsZSBBZGFtV1x1MDAyN3MgZGVjb3VwbGVkIGRlY2F5IHJlZ3VsYXJpemVzIHRoZW0gcHJvcGVybHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWRhbVcgSW1wbGVtZW50YXRpb24gZnJvbSBTY3JhdGNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZGFtVyBkaWZmZXJzIGZyb20gQWRhbSBpbiBleGFjdGx5IG9uZSBsaW5lOiBiZWZvcmUgdGhlIGdyYWRpZW50IHVwZGF0ZSwgdGhlIHBhcmFtZXRlcnMgYXJlIHNocnVuayBieSB0aGUgd2VpZ2h0IGRlY2F5IGZhY3Rvci4gVGhlIHJlc3Qgb2YgdGhlIGFsZ29yaXRobSAobW9tZW50IHVwZGF0ZXMsIGJpYXMgY29ycmVjdGlvbiwgYWRhcHRpdmUgc2NhbGluZykgaXMgaWRlbnRpY2FsIHRvIEFkYW0uIFRoaXMgbWluaW1hbCBjaGFuZ2UgZ2l2ZXMgc2lnbmlmaWNhbnRseSBiZXR0ZXIgZ2VuZXJhbGl6YXRpb24gaW4gcHJhY3RpY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgYWRhbXcoZ3JhZF9mbiwgeDAsIGxyPTAuMDAxLCBiZXRhMT0wLjksIGJldGEyPTAuOTk5LFxuICAgICAgICAgIGVwcz0xZS04LCB3ZWlnaHRfZGVjYXk9MC4wMSwgbl9zdGVwcz01MDApOlxuICAgIHggPSBucC5hcnJheSh4MCwgZHR5cGU9ZmxvYXQpXG4gICAgbSA9IG5wLnplcm9zX2xpa2UoeClcbiAgICB2ID0gbnAuemVyb3NfbGlrZSh4KVxuICAgIGxvc3NlcyA9IFt4WzBdKioyICsgeFsxXSoqMl0gICAjIHRveSBsb3NzID0gfHx4fHxeMlxuICAgIGZvciB0IGluIHJhbmdlKDEsIG5fc3RlcHMgKyAxKTpcbiAgICAgICAgZyA9IGdyYWRfZm4oeClcbiAgICAgICAgbSA9IGJldGExICogbSArICgxIC0gYmV0YTEpICogZ1xuICAgICAgICB2ID0gYmV0YTIgKiB2ICsgKDEgLSBiZXRhMikgKiBnKioyXG4gICAgICAgIG1faGF0ID0gbSAvICgxIC0gYmV0YTEqKnQpXG4gICAgICAgIHZfaGF0ID0gdiAvICgxIC0gYmV0YTIqKnQpXG4gICAgICAgICMgRGVjb3VwbGVkIHdlaWdodCBkZWNheTogYXBwbGllZCBkaXJlY3RseSB0byBwYXJhbXMgKG5vdCB2aWEgZ3JhZGllbnQpXG4gICAgICAgIHggPSB4ICogKDEgLSBsciAqIHdlaWdodF9kZWNheSlcbiAgICAgICAgeCA9IHggLSBsciAqIG1faGF0IC8gKG5wLnNxcnQodl9oYXQpICsgZXBzKVxuICAgICAgICBsb3NzZXMuYXBwZW5kKHhbMF0qKjIgKyB4WzFdKioyKVxuICAgIHJldHVybiB4LCBsb3NzZXNcblxuZGVmIGFkYW1fbDIoZ3JhZF9mbl9iYXNlLCB4MCwgbHI9MC4wMDEsIGJldGExPTAuOSwgYmV0YTI9MC45OTksXG4gICAgICAgICAgICBlcHM9MWUtOCwgd2VpZ2h0X2RlY2F5PTAuMDEsIG5fc3RlcHM9NTAwKTpcbiAgICB4ID0gbnAuYXJyYXkoeDAsIGR0eXBlPWZsb2F0KVxuICAgIG0sIHYgPSBucC56ZXJvc19saWtlKHgpLCBucC56ZXJvc19saWtlKHgpXG4gICAgbG9zc2VzID0gW3hbMF0qKjIgKyB4WzFdKioyXVxuICAgIGZvciB0IGluIHJhbmdlKDEsIG5fc3RlcHMgKyAxKTpcbiAgICAgICAgIyBMMiBhZGRzIHdkKnggdG8gZ3JhZGllbnQgKGNvdXBsZWQgdG8gYWRhcHRpdmUgc2NhbGluZylcbiAgICAgICAgZyA9IGdyYWRfZm5fYmFzZSh4KSArIHdlaWdodF9kZWNheSAqIHhcbiAgICAgICAgbSA9IGJldGExICogbSArICgxIC0gYmV0YTEpICogZ1xuICAgICAgICB2ID0gYmV0YTIgKiB2ICsgKDEgLSBiZXRhMikgKiBnKioyXG4gICAgICAgIG1faGF0ID0gbSAvICgxIC0gYmV0YTEqKnQpXG4gICAgICAgIHZfaGF0ID0gdiAvICgxIC0gYmV0YTIqKnQpXG4gICAgICAgIHggPSB4IC0gbHIgKiBtX2hhdCAvIChucC5zcXJ0KHZfaGF0KSArIGVwcylcbiAgICAgICAgbG9zc2VzLmFwcGVuZCh4WzBdKioyICsgeFsxXSoqMilcbiAgICByZXR1cm4geCwgbG9zc2VzXG5cbmdyYWRfZm4gPSBsYW1iZGEgeDogbnAuYXJyYXkoWzIqeFswXSwgMTAwKnhbMV1dKSAgIyBpbGwtY29uZGl0aW9uZWRcbnhfYWRhbXcsIGxfYWRhbXcgPSBhZGFtdyhncmFkX2ZuLCBbMy4wLCAyLjBdLCBscj0wLjA1LCB3ZWlnaHRfZGVjYXk9MC4xKVxueF9hZGFtMiwgbF9hZGFtMiA9IGFkYW1fbDIoZ3JhZF9mbiwgWzMuMCwgMi4wXSwgbHI9MC4wNSwgd2VpZ2h0X2RlY2F5PTAuMSlcbnBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgMykpXG5wbHQuc2VtaWxvZ3kobF9hZGFtdywgbGFiZWw9XHUwMDI3QWRhbVcgKGRlY291cGxlZCBXRClcdTAwMjcpXG5wbHQuc2VtaWxvZ3kobF9hZGFtMiwgbGFiZWw9XHUwMDI3QWRhbSArIEwyIChjb3VwbGVkIFdEKVx1MDAyNylcbnBsdC54bGFiZWwoXHUwMDI3U3RlcFx1MDAyNyk7IHBsdC55bGFiZWwoXHUwMDI3fHx4fHxeMlx1MDAyNyk7IHBsdC5sZWdlbmQoKVxucGx0LnRpdGxlKFx1MDAyN0FkYW1XIHZzIEFkYW0rTDI6IERlY291cGxlZCB2cyBDb3VwbGVkIFdlaWdodCBEZWNheVx1MDAyNylcbnBsdC5ncmlkKFRydWUsIGFscGhhPTAuMyk7IHBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3YWRhbXdfdnNfYWRhbS5wbmdcdTAwMjcsIGRwaT0xNTApOyBwbHQuc2hvdygpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFRoaXMgTWF0dGVycyBpbiBQcmFjdGljZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW1waXJpY2FsbHksIEFkYW1XIG91dHBlcmZvcm1zIEFkYW0rTDIgb24gbGFuZ3VhZ2UgbW9kZWwgcHJldHJhaW5pbmcgYnkgMeKAkzIgcGVycGxleGl0eSBwb2ludHMgd2l0aCB0aGUgc2FtZSBoeXBlcnBhcmFtZXRlcnMsIGFuZCB0aGUgZGlmZmVyZW5jZSBncm93cyB3aXRoIG1vZGVsIHNjYWxlLiBUaGUga2V5IGFmZmVjdGVkIHBhcmFtZXRlcnMgYXJlOiAoMSkgZW1iZWRkaW5nIGxheWVycyDigJQgc3BhcnNlIGdyYWRpZW50cyBnaXZlIGxhcmdlIHbMgiwgc28gTDIgaXMgbmVhcmx5IHplcm8gZm9yIHRoZW07ICgyKSBMYXllck5vcm0gZ2FpbnMgYW5kIGJpYXNlcyDigJQgc21hbGwgZ3JhZGllbnRzLCBzbyBBZGFtK0wyIG92ZXItcmVndWxhcml6ZXMgdGhlbS4gU3RhbmRhcmQgcHJhY3RpY2U6IGFwcGx5IHdlaWdodCBkZWNheSB0byBhbGwgcGFyYW1ldGVycyBleGNlcHQgTGF5ZXJOb3JtLCBiaWFzZXMsIGFuZCBlbWJlZGRpbmcgbm9ybXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2VpZ2h0IERlY2F5IGFzIEdhdXNzaWFuIFByaW9yIChNQVAgUGVyc3BlY3RpdmUpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXZWlnaHQgZGVjYXkgaGFzIGEgQmF5ZXNpYW4gaW50ZXJwcmV0YXRpb246IG1pbmltaXppbmcgTCjOuCkgKyAozrsvMinigJbOuOKAlsKyIGlzIGVxdWl2YWxlbnQgdG8gTWF4aW11bSBBIFBvc3RlcmlvcmkgKE1BUCkgZXN0aW1hdGlvbiB3aXRoIGEgR2F1c3NpYW4gcHJpb3IgzrggfiBOKDAsIDEvzrsg4ouFIEkpLiBUaGUgTDIgcGVuYWx0eSBzaHJpbmtzIHdlaWdodHMgdG93YXJkIHplcm8sIHdoaWNoIHJlZ3VsYXJpemVzIGJ5IHByZWZlcnJpbmcgc21hbGxlciB3ZWlnaHRzLiBUaGlzIE1BUCBpbnRlcnByZXRhdGlvbiBtYWtlcyBpdCBjbGVhciB0aGF0IHdlaWdodCBkZWNheSAobm90IEwyIHJlZ3VsYXJpemF0aW9uIGNvdXBsZWQgaW50byB0aGUgZ3JhZGllbnQpIGlzIHRoZSBwcmluY2lwbGVkIHJlZ3VsYXJpemVyIGZvciBCYXllc2lhbiBkZWVwIGxlYXJuaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlR5cGljYWwgSHlwZXJwYXJhbWV0ZXJzIGZvciBUcmFuc2Zvcm1lcnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIEFkYW1XIHNldHRpbmdzIGZvciB0cmFuc2Zvcm1lciBwcmV0cmFpbmluZzogbHI9M2UtNCAod2l0aCBjb3NpbmUgZGVjYXkpLCDOsuKCgT0wLjksIM6y4oKCPTAuOTUgKHNsaWdodGx5IGxvd2VyIHRoYW4gZGVmYXVsdCAwLjk5OSBmb3IgYmV0dGVyIGFkYXB0YXRpb24gdG8gZ3JhZGllbnQgY2hhbmdlcyksIM61PTFlLTgsIHdlaWdodF9kZWNheT0wLjEuIFdlaWdodCBkZWNheT0wLjEgaXMgbXVjaCBsYXJnZXIgdGhhbiB0aGUgTDIgcGVuYWx0eSB0eXBpY2FsbHkgdXNlZCB3aXRoIFNHRCAoMC4wMDAx4oCTMC4wMDEpIGJlY2F1c2UgQWRhbVdcdTAwMjdzIGRlY291cGxlZCBkZWNheSBkb2VzIG5vdCBpbnRlcmFjdCB3aXRoIHRoZSBhZGFwdGl2ZSBzY2FsaW5nLiBTb21lIHJlY2lwZXMgdXNlIHdlaWdodF9kZWNheT0wLjAxIGZvciBzbWFsbGVyIG1vZGVscy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiU2V0dGluZyIsIkFkYW0gKyBMMiBsb3NzIiwiQWRhbVcgKGRlY291cGxlZCBXRCkiLCJSZWNvbW1lbmRhdGlvbiJdLCJyb3dzIjpbWyJEZW5zZSBsYXllciB3ZWlnaHRzIiwiTDIgc2NhbGVkIGJ5IDEvc3FydCh2zIIpIOKAlCBuZWFyLXVuaWZvcm0gZm9yIGRlbnNlIGdyYWRzIiwiVW5pZm9ybSBkZWNheSDOu863IHBlciBzdGVwIiwiVXNlIEFkYW1XOyBkZW5zZSBwYXJhbXMgYmVuZWZpdCBlcXVhbGx5Il0sWyJFbWJlZGRpbmcgd2VpZ2h0cyAoc3BhcnNlKSIsIlZlcnkgd2VhayBMMiAobGFyZ2UgdsyCIGZyb20gb2NjYXNpb25hbCBsYXJnZSBncmFkcykiLCJVbmlmb3JtIGRlY2F5IM67zrcgcGVyIHN0ZXAiLCJBZGFtVyBjcml0aWNhbDsgTDIgYmFyZWx5IHJlZ3VsYXJpemVzIHRoZXNlIl0sWyJMYXllck5vcm0gLyBiaWFzZXMiLCJMMiBhcHBsaWVkOyBzbWFsbCB2zIIg4oaSIG92ZXItcmVndWxhcml6ZWQiLCJTaG91bGQgYmUgZXhjbHVkZWQgZnJvbSBXRCIsIkV4Y2x1ZGUgZnJvbSBXRCBpbiBib3RoOyBBZGFtVyBtYWtlcyBleGNsdXNpb24gY3JpdGljYWwiXSxbIk91dHB1dCBwcm9qZWN0aW9uIiwiTDIgc2NhbGVkIGJ5IGdyYWRpZW50IG1hZ25pdHVkZSBoaXN0b3J5IiwiVW5pZm9ybSBkZWNheSIsIlVzZSBBZGFtVyBmb3IgY29uc2lzdGVudCByZWd1bGFyaXphdGlvbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhaW5pbmcgYSBUcmFuc2Zvcm1lciBCbG9jayB3aXRoIEFkYW1XIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIHVzaW5nIEFkYW1XIGZvciB0cmFuc2Zvcm1lciB0cmFpbmluZywgaXRcdTAwMjdzIGltcG9ydGFudCB0byBleGNsdWRlIGNlcnRhaW4gcGFyYW1ldGVyIGdyb3VwcyBmcm9tIHdlaWdodCBkZWNheS4gTGF5ZXJOb3JtIHBhcmFtZXRlcnMsIGJpYXNlcywgYW5kIHNvbWV0aW1lcyBwb3NpdGlvbiBlbWJlZGRpbmdzIHNob3VsZCBoYXZlIHdlaWdodF9kZWNheT0wLjAgdG8gYXZvaWQgb3Zlci1yZWd1bGFyaXppbmcgdGhlbS4gUHlUb3JjaCBtYWtlcyB0aGlzIGVhc3kgd2l0aCBwYXJhbWV0ZXIgZ3JvdXBzIGluIHRoZSBvcHRpbWl6ZXIuIEJlbG93IGlzIGEgcHJhY3RpY2FsIHNldHVwIGZvciBhIHNpbXBsZSB0cmFuc2Zvcm1lciBibG9jay4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcblxuY2xhc3MgVHJhbnNmb3JtZXJCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsPTY0LCBuX2hlYWRzPTQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5hdHRuID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZmYgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkX21vZGVsLCAyNTYpLCBubi5HRUxVKCksIG5uLkxpbmVhcigyNTYsIGRfbW9kZWwpKVxuICAgICAgICBzZWxmLmxuMSA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmxuMiA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHggPSB4ICsgc2VsZi5hdHRuKHNlbGYubG4xKHgpLCBzZWxmLmxuMSh4KSwgc2VsZi5sbjEoeCkpWzBdXG4gICAgICAgIHggPSB4ICsgc2VsZi5mZihzZWxmLmxuMih4KSlcbiAgICAgICAgcmV0dXJuIHhcblxubW9kZWwgPSBUcmFuc2Zvcm1lckJsb2NrKClcbiMgU2VwYXJhdGUgcGFyYW0gZ3JvdXBzOiBubyBXRCBmb3IgTE4gcGFyYW1zIGFuZCBiaWFzZXNcbm5vX2RlY2F5ID0gW1x1MDAyN2JpYXNcdTAwMjcsIFx1MDAyN3dlaWdodFx1MDAyN10gaWYgRmFsc2UgZWxzZSBbXVxuZGVjYXlfcGFyYW1zID0gW3AgZm9yIG4sIHAgaW4gbW9kZWwubmFtZWRfcGFyYW1ldGVycygpIGlmIG5vdCBhbnkobmQgaW4gbiBmb3IgbmQgaW4gW1x1MDAyN2xuXHUwMDI3LCBcdTAwMjdiaWFzXHUwMDI3XSldXG5ub19kZWNheV9wYXJhbXMgPSBbcCBmb3IgbiwgcCBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCkgaWYgYW55KG5kIGluIG4gZm9yIG5kIGluIFtcdTAwMjdsblx1MDAyNywgXHUwMDI3Ymlhc1x1MDAyN10pXVxub3B0aW1pemVyID0gb3B0aW0uQWRhbVcoW1xuICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IGRlY2F5X3BhcmFtcywgXHUwMDI3d2VpZ2h0X2RlY2F5XHUwMDI3OiAwLjF9LFxuICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IG5vX2RlY2F5X3BhcmFtcywgXHUwMDI3d2VpZ2h0X2RlY2F5XHUwMDI3OiAwLjB9XG5dLCBscj0zZS00LCBiZXRhcz0oMC45LCAwLjk1KSwgZXBzPTFlLTgpXG5cblggPSB0b3JjaC5yYW5kbig4LCAxNiwgNjQpICAjIGJhdGNoPTgsIHNlcV9sZW49MTYsIGRfbW9kZWw9NjRcbmxvc3NlcyA9IFtdXG5mb3Igc3RlcCBpbiByYW5nZSgxMDApOlxuICAgIG91dCA9IG1vZGVsKFgpXG4gICAgbG9zcyA9IG91dC5wb3coMikubWVhbigpICAjIHRveSBsb3NzXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdGltaXplci5zdGVwKClcbiAgICBsb3NzZXMuYXBwZW5kKGxvc3MuaXRlbSgpKVxucHJpbnQoZlx1MDAyN0RlY2F5IHBhcmFtczoge2xlbihkZWNheV9wYXJhbXMpfSwgTm8tZGVjYXkgcGFyYW1zOiB7bGVuKG5vX2RlY2F5X3BhcmFtcyl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0ZpbmFsIGxvc3M6IHtsb3NzZXNbLTFdOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tYmluZWQgTFIgYW5kIFdlaWdodCBEZWNheSBTY2hlZHVsZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9kZXJuIHRyYW5zZm9ybWVyIHRyYWluaW5nIHVzZXMgY29zaW5lIGxlYXJuaW5nIHJhdGUgZGVjYXkgd2l0aCBsaW5lYXIgd2FybXVwLCBjb21iaW5lZCB3aXRoIGNvbnN0YW50IHdlaWdodCBkZWNheS4gU29tZSByZWNpcGVzIGFsc28gYXBwbHkgY29zaW5lIGRlY2F5IHRvIHRoZSB3ZWlnaHQgZGVjYXkgaXRzZWxmIChzdGFydGluZyBoaWdoIGFuZCBlbmRpbmcgbG93KS4gVGhlIHdhcm11cCBwZXJpb2QgKHR5cGljYWxseSAx4oCTNSUgb2YgdG90YWwgc3RlcHMpIHByZXZlbnRzIGluc3RhYmlsaXR5IGZyb20gQWRhbVx1MDAyN3MgdW5yZWxpYWJsZSBzZWNvbmQgbW9tZW50IGVzdGltYXRlIGF0IGluaXRpYWxpemF0aW9uLiBBZnRlciB3YXJtdXAsIHRoZSBjb3NpbmUgZGVjYXkgc21vb3RobHkgcmVkdWNlcyB0aGUgbGVhcm5pbmcgcmF0ZSB0byBhIG1pbmltdW0gKHR5cGljYWxseSBscl9taW4gPSBscl9tYXgvMTApLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuaW1wb3J0IG1hdGhcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5tb2RlbCA9IHRvcmNoLm5uLkxpbmVhcig2NCwgNjQpXG5vcHRpbWl6ZXIgPSBvcHRpbS5BZGFtVyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTNlLTQsIHdlaWdodF9kZWNheT0wLjEsIGJldGFzPSgwLjksIDAuOTUpKVxuXG50b3RhbF9zdGVwcyA9IDEwMDBcbndhcm11cF9zdGVwcyA9IDEwMFxubHJfbWF4ID0gM2UtNFxubHJfbWluID0gM2UtNVxuXG5kZWYgZ2V0X2xyKHN0ZXApOlxuICAgIGlmIHN0ZXAgXHUwMDNjIHdhcm11cF9zdGVwczpcbiAgICAgICAgcmV0dXJuIGxyX21heCAqIHN0ZXAgLyB3YXJtdXBfc3RlcHMgICMgbGluZWFyIHdhcm11cFxuICAgIHByb2dyZXNzID0gKHN0ZXAgLSB3YXJtdXBfc3RlcHMpIC8gKHRvdGFsX3N0ZXBzIC0gd2FybXVwX3N0ZXBzKVxuICAgIHJldHVybiBscl9taW4gKyAwLjUgKiAobHJfbWF4IC0gbHJfbWluKSAqICgxICsgbWF0aC5jb3MobWF0aC5waSAqIHByb2dyZXNzKSlcblxubHJfc2NoZWR1bGUgPSBbZ2V0X2xyKHMpIGZvciBzIGluIHJhbmdlKHRvdGFsX3N0ZXBzKV1cbmxvc3NlcyA9IFtdXG5mb3Igc3RlcCBpbiByYW5nZSh0b3RhbF9zdGVwcyk6XG4gICAgbHIgPSBnZXRfbHIoc3RlcClcbiAgICBmb3IgcGcgaW4gb3B0aW1pemVyLnBhcmFtX2dyb3VwczpcbiAgICAgICAgcGdbXHUwMDI3bHJcdTAwMjddID0gbHJcbiAgICB4ID0gdG9yY2gucmFuZG4oMTYsIDY0KVxuICAgIGxvc3MgPSBtb2RlbCh4KS5wb3coMikubWVhbigpXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdGltaXplci5zdGVwKClcbiAgICBsb3NzZXMuYXBwZW5kKGxvc3MuaXRlbSgpKVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMSwgMiwgZmlnc2l6ZT0oMTEsIDMpKVxuYXhlc1swXS5wbG90KGxyX3NjaGVkdWxlKTsgYXhlc1swXS5zZXRfdGl0bGUoXHUwMDI3TFIgU2NoZWR1bGU6IFdhcm11cCArIENvc2luZSBEZWNheVx1MDAyNylcbmF4ZXNbMF0uc2V0X3hsYWJlbChcdTAwMjdTdGVwXHUwMDI3KTsgYXhlc1swXS5zZXRfeWxhYmVsKFx1MDAyN0xlYXJuaW5nIFJhdGVcdTAwMjcpXG5heGVzWzFdLnBsb3QobG9zc2VzKTsgYXhlc1sxXS5zZXRfdGl0bGUoXHUwMDI3VHJhaW5pbmcgTG9zc1x1MDAyNylcbmF4ZXNbMV0uc2V0X3hsYWJlbChcdTAwMjdTdGVwXHUwMDI3KTsgYXhlc1sxXS5zZXRfeWxhYmVsKFx1MDAyN0xvc3NcdTAwMjcpXG5wbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zYXZlZmlnKFx1MDAyN2FkYW13X3NjaGVkdWxlLnBuZ1x1MDAyNywgZHBpPTE1MCk7IHBsdC5zaG93KCkifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFkYW0rTDIgZ2l2ZXMgbm9uLXVuaWZvcm0gZWZmZWN0aXZlIHJlZ3VsYXJpemF0aW9uOiDOu864X2kgLyBzcXJ0KHbMgl9pKSIsIkFkYW1XIGRlY291cGxlczogYXBwbGllcyAoMS3Ot867KSBzaHJpbmthZ2UgZGlyZWN0bHkgdG8gcGFyYW1zLCBpbmRlcGVuZGVudCBvZiB2zIIiLCJVbmlmb3JtIM67IGZvciBhbGwgcGFyYW1zLCByZWdhcmRsZXNzIG9mIGdyYWRpZW50IG1hZ25pdHVkZSBoaXN0b3J5IiwiRXhjbHVkZSBMYXllck5vcm0gd2VpZ2h0cyBhbmQgYmlhc2VzIGZyb20gd2VpZ2h0IGRlY2F5IChwYXJhbSBncm91cHMpIiwiVXNlIHdlaWdodF9kZWNheT0wLjEgZm9yIHRyYW5zZm9ybWVycyB3aXRoIEFkYW1XIChtdWNoIGhpZ2hlciB0aGFuIFNHRCBMMiBzZXR0aW5nKSJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQWRhbVcgUmVjaXBlIGZvciBUcmFuc2Zvcm1lcnMiLCJjb250ZW50IjoiVXNlIEFkYW1XIHdpdGggbHI9M2UtNCwgzrLigoE9MC45LCDOsuKCgj0wLjk1IChub3QgMC45OTkpLCBlcHM9MWUtOCwgd2VpZ2h0X2RlY2F5PTAuMS4gVXNlIGxpbmVhciB3YXJtdXAgZm9yIDHigJMyJSBvZiB0b3RhbCBzdGVwcyB0aGVuIGNvc2luZSBkZWNheS4gRXhjbHVkZSBiaWFzZXMgYW5kIExheWVyTm9ybSBwYXJhbWV0ZXJzIGZyb20gd2VpZ2h0IGRlY2F5LiBHcmFkaWVudCBjbGlwIHRvIG1heCBub3JtIDEuMC4gVGhlc2Ugc2V0dGluZ3Mgd29yayB3ZWxsIGZvciBHUFQtc3R5bGUgbW9kZWxzIGZyb20gMTAwTSB0byA3QiBwYXJhbWV0ZXJzIHdpdGhvdXQgc2lnbmlmaWNhbnQgdHVuaW5nLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# AdamW — Decoupled Weight Decay

## The Problem with Adam + L2 Regularization

The naive approach to regularization with Adam is to add λ‖θ‖² to the loss, which adds λθ to the gradient. Adam then scales this modified gradient by 1/√v̂, so the effective regularization for parameter i is λθ_i / √v̂_i. Parameters with large gradient variance (large v̂) receive weaker regularization than intended, while parameters with small gradient variance receive stronger regularization. This non-uniform effective regularization defeats the purpose of L2 and leads to worse generalization, especially for parameters in dense layers vs. sparse embedding layers.

```python
import numpy as np
import torch

# Demonstrate that Adam+L2 != weight decay
# For Adam: effective L2 on param i = lambda / sqrt(v_hat_i)
# For AdamW: effective weight decay = lambda (uniform)

np.random.seed(42)
# Simulate two parameters: one with high gradient variance, one with low
T = 100
lambda_wd = 0.01
beta2, eps = 0.999, 1e-8

v_high = 0.0   # tracks v for high-variance param
v_low = 0.0    # tracks v for low-variance param
eff_l2_high, eff_l2_low = [], []

for t in range(1, T + 1):
    g_high = 10.0 * np.random.randn()   # high gradient variance
    g_low = 0.01 * np.random.randn()    # low gradient variance
    v_high = beta2 * v_high + (1 - beta2) * g_high**2
    v_low  = beta2 * v_low  + (1 - beta2) * g_low**2
    v_hat_high = v_high / (1 - beta2**t)
    v_hat_low  = v_low  / (1 - beta2**t)
    # Effective L2 = lambda / sqrt(v_hat): smaller for high-variance params
    eff_l2_high.append(lambda_wd / (np.sqrt(v_hat_high) + eps))
    eff_l2_low.append(lambda_wd / (np.sqrt(v_hat_low) + eps))

print(f'Effective L2 (high-var param): {np.mean(eff_l2_high[50:]):.6f}')
print(f'Effective L2 (low-var  param): {np.mean(eff_l2_low[50:]):.6f}')
print(f'AdamW weight decay (uniform):  {lambda_wd:.6f}')
print('Adam+L2 regularization is NON-UNIFORM; AdamW is UNIFORM')
```

## Decoupled Weight Decay in AdamW

AdamW (Loshchilov & Hutter, 2019) decouples weight decay from the gradient update: θ_{t+1} = (1 − ηλ) θ_t − η m̂_t / (√v̂_t + ε). The weight decay term (1 − ηλ) is applied directly to the parameters, independently of the gradient magnitude. This gives every parameter the same fractional shrinkage ηλ per step, regardless of its gradient history. The gradient update m̂/(√v̂+ε) is unchanged from Adam and handles the adaptive scaling.

> **AdamW is Now the Standard**: AdamW is the default optimizer for virtually all large transformer models: GPT-2/3/4, BERT, T5, LLaMA, and most modern vision transformers use AdamW with lr~3e-4 and weight decay~0.1. The difference from Adam+L2 is especially pronounced for embedding layers, which have sparse gradients and large v̂ — L2 barely affects them, while AdamW's decoupled decay regularizes them properly.

## AdamW Implementation from Scratch

AdamW differs from Adam in exactly one line: before the gradient update, the parameters are shrunk by the weight decay factor. The rest of the algorithm (moment updates, bias correction, adaptive scaling) is identical to Adam. This minimal change gives significantly better generalization in practice.

```python
import numpy as np
import matplotlib.pyplot as plt

def adamw(grad_fn, x0, lr=0.001, beta1=0.9, beta2=0.999,
          eps=1e-8, weight_decay=0.01, n_steps=500):
    x = np.array(x0, dtype=float)
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    losses = [x[0]**2 + x[1]**2]   # toy loss = ||x||^2
    for t in range(1, n_steps + 1):
        g = grad_fn(x)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g**2
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        # Decoupled weight decay: applied directly to params (not via gradient)
        x = x * (1 - lr * weight_decay)
        x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
        losses.append(x[0]**2 + x[1]**2)
    return x, losses

def adam_l2(grad_fn_base, x0, lr=0.001, beta1=0.9, beta2=0.999,
            eps=1e-8, weight_decay=0.01, n_steps=500):
    x = np.array(x0, dtype=float)
    m, v = np.zeros_like(x), np.zeros_like(x)
    losses = [x[0]**2 + x[1]**2]
    for t in range(1, n_steps + 1):
        # L2 adds wd*x to gradient (coupled to adaptive scaling)
        g = grad_fn_base(x) + weight_decay * x
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g**2
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
        losses.append(x[0]**2 + x[1]**2)
    return x, losses

grad_fn = lambda x: np.array([2*x[0], 100*x[1]])  # ill-conditioned
x_adamw, l_adamw = adamw(grad_fn, [3.0, 2.0], lr=0.05, weight_decay=0.1)
x_adam2, l_adam2 = adam_l2(grad_fn, [3.0, 2.0], lr=0.05, weight_decay=0.1)
plt.figure(figsize=(8, 3))
plt.semilogy(l_adamw, label='AdamW (decoupled WD)')
plt.semilogy(l_adam2, label='Adam + L2 (coupled WD)')
plt.xlabel('Step'); plt.ylabel('||x||^2'); plt.legend()
plt.title('AdamW vs Adam+L2: Decoupled vs Coupled Weight Decay')
plt.grid(True, alpha=0.3); plt.tight_layout()
plt.savefig('adamw_vs_adam.png', dpi=150); plt.show()
```

## Why This Matters in Practice

Empirically, AdamW outperforms Adam+L2 on language model pretraining by 1–2 perplexity points with the same hyperparameters, and the difference grows with model scale. The key affected parameters are: (1) embedding layers — sparse gradients give large v̂, so L2 is nearly zero for them; (2) LayerNorm gains and biases — small gradients, so Adam+L2 over-regularizes them. Standard practice: apply weight decay to all parameters except LayerNorm, biases, and embedding norms.

## Weight Decay as Gaussian Prior (MAP Perspective)

Weight decay has a Bayesian interpretation: minimizing L(θ) + (λ/2)‖θ‖² is equivalent to Maximum A Posteriori (MAP) estimation with a Gaussian prior θ ~ N(0, 1/λ ⋅ I). The L2 penalty shrinks weights toward zero, which regularizes by preferring smaller weights. This MAP interpretation makes it clear that weight decay (not L2 regularization coupled into the gradient) is the principled regularizer for Bayesian deep learning.

## Typical Hyperparameters for Transformers

Standard AdamW settings for transformer pretraining: lr=3e-4 (with cosine decay), β₁=0.9, β₂=0.95 (slightly lower than default 0.999 for better adaptation to gradient changes), ε=1e-8, weight_decay=0.1. Weight decay=0.1 is much larger than the L2 penalty typically used with SGD (0.0001–0.001) because AdamW's decoupled decay does not interact with the adaptive scaling. Some recipes use weight_decay=0.01 for smaller models.

| Setting | Adam + L2 loss | AdamW (decoupled WD) | Recommendation |
| --- | --- | --- | --- |
| Dense layer weights | L2 scaled by 1/sqrt(v̂) — near-uniform for dense grads | Uniform decay λη per step | Use AdamW; dense params benefit equally |
| Embedding weights (sparse) | Very weak L2 (large v̂ from occasional large grads) | Uniform decay λη per step | AdamW critical; L2 barely regularizes these |
| LayerNorm / biases | L2 applied; small v̂ → over-regularized | Should be excluded from WD | Exclude from WD in both; AdamW makes exclusion critical |
| Output projection | L2 scaled by gradient magnitude history | Uniform decay | Use AdamW for consistent regularization |

## Training a Transformer Block with AdamW

When using AdamW for transformer training, it's important to exclude certain parameter groups from weight decay. LayerNorm parameters, biases, and sometimes position embeddings should have weight_decay=0.0 to avoid over-regularizing them. PyTorch makes this easy with parameter groups in the optimizer. Below is a practical setup for a simple transformer block.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

torch.manual_seed(42)

class TransformerBlock(nn.Module):
    def __init__(self, d_model=64, n_heads=4):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.ff = nn.Sequential(nn.Linear(d_model, 256), nn.GELU(), nn.Linear(256, d_model))
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)

    def forward(self, x):
        x = x + self.attn(self.ln1(x), self.ln1(x), self.ln1(x))[0]
        x = x + self.ff(self.ln2(x))
        return x

model = TransformerBlock()
# Separate param groups: no WD for LN params and biases
no_decay = ['bias', 'weight'] if False else []
decay_params = [p for n, p in model.named_parameters() if not any(nd in n for nd in ['ln', 'bias'])]
no_decay_params = [p for n, p in model.named_parameters() if any(nd in n for nd in ['ln', 'bias'])]
optimizer = optim.AdamW([
    {'params': decay_params, 'weight_decay': 0.1},
    {'params': no_decay_params, 'weight_decay': 0.0}
], lr=3e-4, betas=(0.9, 0.95), eps=1e-8)

X = torch.randn(8, 16, 64)  # batch=8, seq_len=16, d_model=64
losses = []
for step in range(100):
    out = model(X)
    loss = out.pow(2).mean()  # toy loss
    optimizer.zero_grad(); loss.backward(); optimizer.step()
    losses.append(loss.item())
print(f'Decay params: {len(decay_params)}, No-decay params: {len(no_decay_params)}')
print(f'Final loss: {losses[-1]:.4f}')
```

## Combined LR and Weight Decay Schedule

Modern transformer training uses cosine learning rate decay with linear warmup, combined with constant weight decay. Some recipes also apply cosine decay to the weight decay itself (starting high and ending low). The warmup period (typically 1–5% of total steps) prevents instability from Adam's unreliable second moment estimate at initialization. After warmup, the cosine decay smoothly reduces the learning rate to a minimum (typically lr_min = lr_max/10).

```python
import torch
import torch.optim as optim
import math
import matplotlib.pyplot as plt

torch.manual_seed(42)
model = torch.nn.Linear(64, 64)
optimizer = optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.1, betas=(0.9, 0.95))

total_steps = 1000
warmup_steps = 100
lr_max = 3e-4
lr_min = 3e-5

def get_lr(step):
    if step < warmup_steps:
        return lr_max * step / warmup_steps  # linear warmup
    progress = (step - warmup_steps) / (total_steps - warmup_steps)
    return lr_min + 0.5 * (lr_max - lr_min) * (1 + math.cos(math.pi * progress))

lr_schedule = [get_lr(s) for s in range(total_steps)]
losses = []
for step in range(total_steps):
    lr = get_lr(step)
    for pg in optimizer.param_groups:
        pg['lr'] = lr
    x = torch.randn(16, 64)
    loss = model(x).pow(2).mean()
    optimizer.zero_grad(); loss.backward(); optimizer.step()
    losses.append(loss.item())

fig, axes = plt.subplots(1, 2, figsize=(11, 3))
axes[0].plot(lr_schedule); axes[0].set_title('LR Schedule: Warmup + Cosine Decay')
axes[0].set_xlabel('Step'); axes[0].set_ylabel('Learning Rate')
axes[1].plot(losses); axes[1].set_title('Training Loss')
axes[1].set_xlabel('Step'); axes[1].set_ylabel('Loss')
plt.tight_layout(); plt.savefig('adamw_schedule.png', dpi=150); plt.show()
```

- Adam+L2 gives non-uniform effective regularization: λθ_i / sqrt(v̂_i)
- AdamW decouples: applies (1-ηλ) shrinkage directly to params, independent of v̂
- Uniform λ for all params, regardless of gradient magnitude history
- Exclude LayerNorm weights and biases from weight decay (param groups)
- Use weight_decay=0.1 for transformers with AdamW (much higher than SGD L2 setting)

> **AdamW Recipe for Transformers**: Use AdamW with lr=3e-4, β₁=0.9, β₂=0.95 (not 0.999), eps=1e-8, weight_decay=0.1. Use linear warmup for 1–2% of total steps then cosine decay. Exclude biases and LayerNorm parameters from weight decay. Gradient clip to max norm 1.0. These settings work well for GPT-style models from 100M to 7B parameters without significant tuning.

---

