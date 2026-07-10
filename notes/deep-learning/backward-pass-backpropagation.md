---
title: "Backward Pass — Chain Rule and Gradient Derivation by Hand"
slug: "backward-pass-backpropagation"
description: "Derive gradients for linear layers, ReLU, sigmoid, and softmax+cross-entropy using the chain rule, verify with finite differences, implement a custom autograd Function, and understand vector-Jacobian products and why reverse-mode AD scales."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFja3Byb3BhZ2F0aW9uIGlzIHRoZSBhbGdvcml0aG0gdGhhdCBjb21wdXRlcyBncmFkaWVudHMgb2YgdGhlIGxvc3Mgd2l0aCByZXNwZWN0IHRvIGV2ZXJ5IHBhcmFtZXRlciBieSBhcHBseWluZyB0aGUgY2hhaW4gcnVsZSBpbiByZXZlcnNlIHRocm91Z2ggdGhlIGNvbXB1dGF0aW9uYWwgZ3JhcGguIFVuZGVyc3RhbmRpbmcgaXQgZnJvbSBmaXJzdCBwcmluY2lwbGVzIOKAlCBkZXJpdmluZyBncmFkaWVudHMgYnkgaGFuZCBmb3IgZWFjaCBsYXllciB0eXBlIOKAlCBkZW15c3RpZmllcyBhdXRvbWF0aWMgZGlmZmVyZW50aWF0aW9uIGFuZCBpcyBlc3NlbnRpYWwgZm9yIGRlYnVnZ2luZyBncmFkaWVudCBmbG93LCBpbXBsZW1lbnRpbmcgY3VzdG9tIG9wZXJhdGlvbnMsIGFuZCByZWFzb25pbmcgYWJvdXQgdHJhaW5pbmcgZHluYW1pY3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hhaW4gUnVsZSBhbmQgQ29tcHV0YXRpb25hbCBHcmFwaCBUcmF2ZXJzYWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIGNvbXBvc2l0aW9uIGYoZyh4KSksIHRoZSBjaGFpbiBydWxlIGdpdmVzIGRmL2R4ID0gKGRmL2RnKShkZy9keCkuIEluIGEgbmV1cmFsIG5ldHdvcmsgd2l0aCBsb3NzIEwsIHRoZSBncmFkaWVudCBmbG93cyBiYWNrd2FyZDogZEwvZHggPSAoZEwvZHkpKGR5L2R4KSB3aGVyZSB5ID0gZih4KS4gSW4gdGhlIGNvbXB1dGF0aW9uYWwgZ3JhcGgsIGVhY2ggbm9kZSBzdG9yZXMgaXRzIGxvY2FsIEphY29iaWFuIGR5L2R4OyBiYWNrcHJvcCBtdWx0aXBsaWVzIHRoZXNlIEphY29iaWFucyBpbiByZXZlcnNlIG9yZGVyIGZyb20gb3V0cHV0IHRvIGlucHV0LiBGb3IgYSBzY2FsYXIgbG9zcyBhbmQgYSB2ZWN0b3IgeCwgZEwvZHggaGFzIHRoZSBzYW1lIHNoYXBlIGFzIHgg4oCUIHRoaXMgaXMgdGhlIHZlY3Rvci1KYWNvYmlhbiBwcm9kdWN0IChWSlApLCB0aGUgY29yZSBvcGVyYXRpb24gaW4gcmV2ZXJzZS1tb2RlIEFELiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IG9mIGEgTGluZWFyIExheWVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgeiA9IFd4ICsgYiB3aXRoIGxvc3MgTDogdGhlIGxvY2FsIEphY29iaWFuIGlzIOKIgnov4oiCeCA9IFcuIFRoZSBncmFkaWVudCBvZiBXIGlzIGRML2RXID0gKGRML2R6KeG1gCB4IChvdXRlciBwcm9kdWN0IGZvciBhIHNpbmdsZSBzYW1wbGUpIG9yIGRML2RXID0gKGRML2R6KeG1gCBYIGZvciBhIGJhdGNoLiBUaGUgZ3JhZGllbnQgb2YgeCBpcyBkTC9keCA9IFfhtYAgKGRML2R6KS4gVGhlIGdyYWRpZW50IG9mIGIgaXMgZEwvZGIgPSBzdW0gb2YgZEwvZHogb3ZlciB0aGUgYmF0Y2ggZGltZW5zaW9uIChiZWNhdXNlIGIgYnJvYWRjYXN0cykuIFNoYXBlIGNoZWNrOiBpZiBkTC9keiBoYXMgc2hhcGUgKG0sIGRfb3V0KSBhbmQgVyBoYXMgc2hhcGUgKGRfb3V0LCBkX2luKSwgdGhlbiBkTC9kVyA9IChkTC9keinhtYAgQCBYIGhhcyBzaGFwZSAoZF9vdXQsIGRfaW4pIOKAlCBtYXRjaGluZyBXIGV4YWN0bHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnRzIG9mIEFjdGl2YXRpb24gRnVuY3Rpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZUxVOiBhID0gbWF4KDAsIHopLCBzbyBkYS9keiA9IPCdn5koeiBcdTAwM2UgMCkg4oCUIGEgYmluYXJ5IG1hc2suIEdyYWRpZW50OiBkTC9keiA9IGRML2RhIOKKmSDwnZ+ZKHogXHUwMDNlIDApLiBTaWdtb2lkOiDPgyh6KSA9IDEvKDErZeKBu+G2uyksIGRlcml2YXRpdmUgz4NcdTAwMjcoeikgPSDPgyh6KSgxLc+DKHopKSDigJQgZWxlZ2FudGx5IGV4cHJlc3NlZCBpbiB0ZXJtcyBvZiB0aGUgb3V0cHV0IGl0c2VsZi4gR3JhZGllbnQ6IGRML2R6ID0gZEwvZGEg4oqZIGEg4oqZICgxLWEpLiBTb2Z0bWF4ICsgY3Jvc3MtZW50cm9weTogd2hlbiBjb21iaW5lZCwgdGhlIGdyYWRpZW50IHdpdGggcmVzcGVjdCB0byB0aGUgbG9naXRzIHogaXMgcmVtYXJrYWJseSBjbGVhbjogZEwvZHogPSAoMS9tKSjFtyAtIHkpIHdoZXJlIHkgaXMgb25lLWhvdC4gVGhpcyBjbGVhbiBncmFkaWVudCBpcyB3aHkgY3Jvc3MtZW50cm9weSBhbmQgc29mdG1heCBhcmUgYWx3YXlzIHVzZWQgdG9nZXRoZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG4jIC0tLS0gRm9yd2FyZCBwYXNzIC0tLS1cbmRlZiByZWx1KHopOiAgICAgcmV0dXJuIG5wLm1heGltdW0oMCwgeilcbmRlZiBzb2Z0bWF4KHopOiAgZSA9IG5wLmV4cCh6IC0gei5tYXgoMSwga2VlcGRpbXM9VHJ1ZSkpOyByZXR1cm4gZSAvIGUuc3VtKDEsIGtlZXBkaW1zPVRydWUpXG5cbmRlZiBmb3J3YXJkKFgsIFcxLCBiMSwgVzIsIGIyKTpcbiAgICB6MSA9IFggQCBXMS5UICsgYjFcbiAgICBhMSA9IHJlbHUoejEpXG4gICAgejIgPSBhMSBAIFcyLlQgKyBiMlxuICAgIHlfaGF0ID0gc29mdG1heCh6MilcbiAgICByZXR1cm4geV9oYXQsIGRpY3QoWD1YLCB6MT16MSwgYTE9YTEsIHoyPXoyLCBXMT1XMSwgVzI9VzIsIGIxPWIxLCBiMj1iMilcblxuZGVmIGNyb3NzX2VudHJvcHkoeV9oYXQsIHkpOlxuICAgIG0gPSB5LnNoYXBlWzBdXG4gICAgcmV0dXJuIC1ucC5sb2coeV9oYXRbbnAuYXJhbmdlKG0pLCB5XSArIDFlLTEyKS5tZWFuKClcblxuIyAtLS0tIEJhY2t3YXJkIHBhc3MgKG1hbnVhbCBjaGFpbiBydWxlKSAtLS0tXG5kZWYgYmFja3dhcmQoeV9oYXQsIHlfdHJ1ZSwgY2FjaGUpOlxuICAgIG0gPSB5X3RydWUuc2hhcGVbMF1cbiAgICBYLCB6MSwgYTEgPSBjYWNoZVtcdTAwMjdYXHUwMDI3XSwgY2FjaGVbXHUwMDI3ejFcdTAwMjddLCBjYWNoZVtcdTAwMjdhMVx1MDAyN11cbiAgICBXMiA9IGNhY2hlW1x1MDAyN1cyXHUwMDI3XVxuICAgICMgR3JhZGllbnQgb2Ygc29mdG1heCArIGNyb3NzLWVudHJvcHkgd3J0IGxvZ2l0cyB6MlxuICAgIGR6MiA9IHlfaGF0LmNvcHkoKVxuICAgIGR6MltucC5hcmFuZ2UobSksIHlfdHJ1ZV0gLT0gMVxuICAgIGR6MiAvPSBtICAgICAgICAgICAgICAgICAgICAgICAgICMgKG0sIGRfb3V0KVxuICAgIGRXMiA9IGR6Mi5UIEAgYTEgICAgICAgICAgICAgICAgICMgKGRfb3V0LCBkX2gpXG4gICAgZGIyID0gZHoyLnN1bShheGlzPTApICAgICAgICAgICAgIyAoZF9vdXQsKVxuICAgIGRhMSA9IGR6MiBAIFcyICAgICAgICAgICAgICAgICAgICMgKG0sIGRfaClcbiAgICBkejEgPSBkYTEgKiAoejEgXHUwMDNlIDApLmFzdHlwZShmbG9hdCkgICMgUmVMVSBtYXNrXG4gICAgZFcxID0gZHoxLlQgQCBYICAgICAgICAgICAgICAgICAgIyAoZF9oLCBkX2luKVxuICAgIGRiMSA9IGR6MS5zdW0oYXhpcz0wKSAgICAgICAgICAgICMgKGRfaCwpXG4gICAgcmV0dXJuIGRpY3QoZFcxPWRXMSwgZGIxPWRiMSwgZFcyPWRXMiwgZGIyPWRiMilcblxubnAucmFuZG9tLnNlZWQoMSlcbm0sIGRfaW4sIGRfaCwgZF9vdXQgPSAxNiwgOCwgMTIsIDNcblggID0gbnAucmFuZG9tLnJhbmRuKG0sIGRfaW4pXG5XMSA9IG5wLnJhbmRvbS5yYW5kbihkX2gsIGRfaW4pICogMC4xXG5iMSA9IG5wLnplcm9zKGRfaClcblcyID0gbnAucmFuZG9tLnJhbmRuKGRfb3V0LCBkX2gpICogMC4xXG5iMiA9IG5wLnplcm9zKGRfb3V0KVxueSAgPSBucC5yYW5kb20ucmFuZGludCgwLCBkX291dCwgbSlcblxueV9oYXQsIGNhY2hlID0gZm9yd2FyZChYLCBXMSwgYjEsIFcyLCBiMilcbmxvc3MgPSBjcm9zc19lbnRyb3B5KHlfaGF0LCB5KVxuZ3JhZHMgPSBiYWNrd2FyZCh5X2hhdCwgeSwgY2FjaGUpXG5wcmludChmXHUwMDI3TG9zczoge2xvc3M6LjRmfVx1MDAyNylcbmZvciBrLCB2IGluIGdyYWRzLml0ZW1zKCk6XG4gICAgcHJpbnQoZlx1MDAyNyAgZHtrfToge3Yuc2hhcGV9ICBub3JtPXtucC5saW5hbGcubm9ybSh2KTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IENoZWNraW5nIHZpYSBGaW5pdGUgRGlmZmVyZW5jZXMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBudW1lcmljYWxfZ3JhZGllbnQobG9zc19mbiwgcGFyYW0sIGVwcz0xZS01KTpcbiAgICBcIlwiXCJDb21wdXRlIG51bWVyaWNhbCBncmFkaWVudCBvZiBsb3NzX2ZuIHdydCBwYXJhbSB1c2luZyBjZW50cmFsIGRpZmZlcmVuY2VzLlwiXCJcIlxuICAgIGdyYWQgPSBucC56ZXJvc19saWtlKHBhcmFtKVxuICAgIGl0ID0gbnAubmRpdGVyKHBhcmFtLCBmbGFncz1bXHUwMDI3bXVsdGlfaW5kZXhcdTAwMjddKVxuICAgIHdoaWxlIG5vdCBpdC5maW5pc2hlZDpcbiAgICAgICAgaWR4ID0gaXQubXVsdGlfaW5kZXhcbiAgICAgICAgb3JpZyA9IHBhcmFtW2lkeF1cbiAgICAgICAgcGFyYW1baWR4XSA9IG9yaWcgKyBlcHNcbiAgICAgICAgbG9zc19wbHVzID0gbG9zc19mbigpXG4gICAgICAgIHBhcmFtW2lkeF0gPSBvcmlnIC0gZXBzXG4gICAgICAgIGxvc3NfbWludXMgPSBsb3NzX2ZuKClcbiAgICAgICAgcGFyYW1baWR4XSA9IG9yaWdcbiAgICAgICAgZ3JhZFtpZHhdID0gKGxvc3NfcGx1cyAtIGxvc3NfbWludXMpIC8gKDIgKiBlcHMpXG4gICAgICAgIGl0Lml0ZXJuZXh0KClcbiAgICByZXR1cm4gZ3JhZFxuXG4jIFJldXNlIFgsIFcxLCBiMSwgVzIsIGIyLCB5IGZyb20gcHJldmlvdXMgY2VsbFxuZGVmIGxvc3NfZm4oKTpcbiAgICB5aCwgXyA9IGZvcndhcmQoWCwgVzEsIGIxLCBXMiwgYjIpXG4gICAgcmV0dXJuIGNyb3NzX2VudHJvcHkoeWgsIHkpXG5cbnloLCBjYWNoZSA9IGZvcndhcmQoWCwgVzEsIGIxLCBXMiwgYjIpXG5ncmFkcyA9IGJhY2t3YXJkKHloLCB5LCBjYWNoZSlcblxubmdyYWRfVzEgPSBudW1lcmljYWxfZ3JhZGllbnQobG9zc19mbiwgVzEpXG5uZ3JhZF9XMiA9IG51bWVyaWNhbF9ncmFkaWVudChsb3NzX2ZuLCBXMilcblxucmVsX2Vycl9XMSA9IG5wLmFicyhncmFkc1tcdTAwMjdkVzFcdTAwMjddIC0gbmdyYWRfVzEpLm1heCgpIC8gKG5wLmFicyhncmFkc1tcdTAwMjdkVzFcdTAwMjddKS5tYXgoKSArIDFlLTgpXG5yZWxfZXJyX1cyID0gbnAuYWJzKGdyYWRzW1x1MDAyN2RXMlx1MDAyN10gLSBuZ3JhZF9XMikubWF4KCkgLyAobnAuYWJzKGdyYWRzW1x1MDAyN2RXMlx1MDAyN10pLm1heCgpICsgMWUtOClcbnByaW50KGZcdTAwMjdSZWxhdGl2ZSBlcnJvciBkVzE6IHtyZWxfZXJyX1cxOi4yZX0gIChzaG91bGQgYmUgXHUwMDNjIDFlLTUpXHUwMDI3KVxucHJpbnQoZlx1MDAyN1JlbGF0aXZlIGVycm9yIGRXMjoge3JlbF9lcnJfVzI6LjJlfSAgKHNob3VsZCBiZSBcdTAwM2MgMWUtNSlcdTAwMjcpXG5wcmludChcdTAwMjdHcmFkaWVudCBjaGVja1x1MDAyNywgXHUwMDI3UEFTU0VEXHUwMDI3IGlmIG1heChyZWxfZXJyX1cxLCByZWxfZXJyX1cyKSBcdTAwM2MgMWUtNCBlbHNlIFx1MDAyN0ZBSUxFRFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQeVRvcmNoIEF1dG9ncmFkIEluc3BlY3Rpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuXG50b3JjaC5tYW51YWxfc2VlZCg0Milcbm0sIGRfaW4sIGRfaCwgZF9vdXQgPSAxNiwgOCwgMTIsIDNcblxubW9kZWwgPSBubi5TZXF1ZW50aWFsKFxuICAgIG5uLkxpbmVhcihkX2luLCBkX2gpLFxuICAgIG5uLlJlTFUoKSxcbiAgICBubi5MaW5lYXIoZF9oLCBkX291dClcbilcblhfdCA9IHRvcmNoLnJhbmRuKG0sIGRfaW4pXG55X3QgPSB0b3JjaC5yYW5kaW50KDAsIGRfb3V0LCAobSwpKVxuXG4jIEZvcndhcmRcbmxvZ2l0cyA9IG1vZGVsKFhfdClcbmxvc3MgPSBubi5Dcm9zc0VudHJvcHlMb3NzKCkobG9naXRzLCB5X3QpXG5wcmludChmXHUwMDI3TG9zczoge2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpXG5cbiMgQmFja3dhcmRcbmxvc3MuYmFja3dhcmQoKVxuXG4jIEluc3BlY3QgZ3JhZGllbnRzXG5mb3IgbmFtZSwgcCBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCk6XG4gICAgcHJpbnQoZlx1MDAyNyAge25hbWV9OiBncmFkLnNoYXBlPXt0dXBsZShwLmdyYWQuc2hhcGUpfSAgXHUwMDI3XG4gICAgICAgICAgZlx1MDAyN2dyYWQubm9ybT17cC5ncmFkLm5vcm0oKS5pdGVtKCk6LjRmfVx1MDAyNylcblxuIyBWZXJpZnkgZ3JhZGllbnQgb2YgejIgPSAoeV9oYXQgLSB5KSAvIG1cbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIHlfaGF0ID0gdG9yY2guc29mdG1heChsb2dpdHMsIGRpbT0xKVxuICAgIGdyYWRfbG9naXRzID0gKHlfaGF0LmNsb25lKCkpXG4gICAgZ3JhZF9sb2dpdHNbdG9yY2guYXJhbmdlKG0pLCB5X3RdIC09IDFcbiAgICBncmFkX2xvZ2l0cyAvPSBtXG5wcmludChmXHUwMDI3XFxuTWFudWFsIGRML2R6MiBub3JtOiB7Z3JhZF9sb2dpdHMubm9ybSgpLml0ZW0oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkN1c3RvbSBBdXRvZ3JhZCBGdW5jdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdG9yY2guYXV0b2dyYWQgaW1wb3J0IEZ1bmN0aW9uXG5cbmNsYXNzIExlYWt5UmVMVUZ1bmN0aW9uKEZ1bmN0aW9uKTpcbiAgICBcIlwiXCJDdXN0b20gYXV0b2dyYWQgRnVuY3Rpb24gZm9yIExlYWt5IFJlTFUgd2l0aCBsZWFybmFibGUgc2xvcGUuXCJcIlwiXG5cbiAgICBAc3RhdGljbWV0aG9kXG4gICAgZGVmIGZvcndhcmQoY3R4LCB4LCBuZWdhdGl2ZV9zbG9wZT0wLjAxKTpcbiAgICAgICAgY3R4LnNhdmVfZm9yX2JhY2t3YXJkKHgpXG4gICAgICAgIGN0eC5uZWdhdGl2ZV9zbG9wZSA9IG5lZ2F0aXZlX3Nsb3BlXG4gICAgICAgIHJldHVybiB0b3JjaC53aGVyZSh4IFx1MDAzZT0gMCwgeCwgbmVnYXRpdmVfc2xvcGUgKiB4KVxuXG4gICAgQHN0YXRpY21ldGhvZFxuICAgIGRlZiBiYWNrd2FyZChjdHgsIGdyYWRfb3V0cHV0KTpcbiAgICAgICAgeCwgPSBjdHguc2F2ZWRfdGVuc29yc1xuICAgICAgICBzbG9wZSA9IGN0eC5uZWdhdGl2ZV9zbG9wZVxuICAgICAgICAjIGRML2R4ID0gZ3JhZF9vdXRwdXQgKiAoMSBpZiB4XHUwMDNlPTAgZWxzZSBzbG9wZSlcbiAgICAgICAgbWFzayA9ICh4IFx1MDAzZT0gMCkuZmxvYXQoKSArIHNsb3BlICogKHggXHUwMDNjIDApLmZsb2F0KClcbiAgICAgICAgZ3JhZF9pbnB1dCA9IGdyYWRfb3V0cHV0ICogbWFza1xuICAgICAgICByZXR1cm4gZ3JhZF9pbnB1dCwgTm9uZSAgIyBOb25lIGZvciBuZWdhdGl2ZV9zbG9wZSAobm90IGEgdGVuc29yKVxuXG4jIFRlc3QgYWdhaW5zdCBQeVRvcmNoIGJ1aWx0LWluXG50b3JjaC5tYW51YWxfc2VlZCgwKVxueCA9IHRvcmNoLnJhbmRuKDQsIDYsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbnNsb3BlID0gMC4wMVxuXG5vdXRfY3VzdG9tID0gTGVha3lSZUxVRnVuY3Rpb24uYXBwbHkoeCwgc2xvcGUpXG5vdXRfY3VzdG9tLnN1bSgpLmJhY2t3YXJkKClcbmdyYWRfY3VzdG9tID0geC5ncmFkLmNsb25lKClcblxueC5ncmFkID0gTm9uZVxub3V0X2J1aWx0aW4gPSB0b3JjaC5ubi5mdW5jdGlvbmFsLmxlYWt5X3JlbHUoeCwgc2xvcGUpXG5vdXRfYnVpbHRpbi5zdW0oKS5iYWNrd2FyZCgpXG5ncmFkX2J1aWx0aW4gPSB4LmdyYWRcblxuZGlmZiA9IChncmFkX2N1c3RvbSAtIGdyYWRfYnVpbHRpbikuYWJzKCkubWF4KCkuaXRlbSgpXG5wcmludChmXHUwMDI3TWF4IGdyYWQgZGlmZmVyZW5jZSAoY3VzdG9tIHZzIGJ1aWx0aW4pOiB7ZGlmZjouMmV9XHUwMDI3KVxucHJpbnQoXHUwMDI3Q3VzdG9tIGF1dG9ncmFkIEZ1bmN0aW9uIGNvcnJlY3Q6XHUwMDI3LCBkaWZmIFx1MDAzYyAxZS02KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUmV2ZXJzZS1Nb2RlIEFEIGlzIE8oRm9yd2FyZCBDb3N0KSIsImNvbnRlbnQiOiJGb3IgYSBzY2FsYXIgbG9zcyBhbmQgbiBwYXJhbWV0ZXJzLCBjb21wdXRpbmcgYWxsIGdyYWRpZW50cyB2aWEgcmV2ZXJzZS1tb2RlIEFEIGNvc3RzIE8oZm9yd2FyZCBwYXNzKSDigJQgbm90IE8obiDDlyBmb3J3YXJkKS4gVGhpcyBpcyBiZWNhdXNlIGVhY2ggYmFja3dhcmQgb3BlcmF0aW9uIGNvbXB1dGVzIGEgdmVjdG9yLUphY29iaWFuIHByb2R1Y3QgKFZKUCkgcmF0aGVyIHRoYW4gdGhlIGZ1bGwgSmFjb2JpYW4gbWF0cml4LiBGb3J3YXJkLW1vZGUgQUQgKGNvbXB1dGluZyBKYWNvYmlhbi12ZWN0b3IgcHJvZHVjdHMpIHdvdWxkIHJlcXVpcmUgb25lIGZvcndhcmQgcGFzcyBwZXIgcGFyYW1ldGVyIOKAlCBPKG4gw5cgZm9yd2FyZCkuIFJldmVyc2UtbW9kZSBpcyB3aGF0IG1ha2VzIHRyYWluaW5nIGJpbGxpb24tcGFyYW1ldGVyIG5ldHdvcmtzIHRyYWN0YWJsZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXllciBHcmFkaWVudCBTdW1tYXJ5In0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkxheWVyIiwiZEwvZFcgZm9ybXVsYSIsImRML2R4IGZvcm11bGEiLCJDb21wdXRhdGlvbmFsIENvc3QiXSwicm93cyI6W1siTGluZWFyIHo9V3grYiIsImRML2R6KeG1gCBAIFggIHNoYXBlIChkX291dCwgZF9pbikiLCJXLlQgQCBkTC9keiAgc2hhcGUgKG0sIGRfaW4pIiwiTyhtIMK3IGRfaW4gwrcgZF9vdXQpIOKAlCBzYW1lIGFzIGZvcndhcmQiXSxbIlJlTFUgYT1tYXgoMCx6KSIsIk5vIHdlaWdodHMiLCJkTC9kYSDiipkg8J2fmSh6XHUwMDNlMCkg4oCUIGVsZW1lbnR3aXNlIG1hc2siLCJPKG4pIOKAlCBjaGVhcCwganVzdCBhIG11bHRpcGx5IGJ5IDAvMSJdLFsiU2lnbW9pZCBhPc+DKHopIiwiTm8gd2VpZ2h0cyIsImRML2RhIOKKmSBhKDEtYSkg4oCUIHVzZXMgY2FjaGVkIG91dHB1dCIsIk8obikg4oCUIHR3byBtdWx0aXBsaWVzIHBlciBlbGVtZW50Il0sWyJTb2Z0bWF4K0NFIChjb21iaW5lZCkiLCJObyB3ZWlnaHRzIGluIHNvZnRtYXgiLCIoxbcgLSB5KS9tIOKAlCBjbGVhbiBjbG9zZWQgZm9ybSIsIk8obSDCtyBDKSDigJQganVzdCBzdWJ0cmFjdCBvbmUtaG90Il0sWyJCYXRjaCBOb3JtIiwiZEwvZM6zID0gzqMgZEwvZHkg4oqZIHjMgiIsIk5vbi10cml2aWFsIOKAlCBjb3VwbGVzIGFsbCBiYXRjaCBzYW1wbGVzIiwiTyhtIMK3IGQpIOKAlCBoYXJkZXIgdGhhbiBvdGhlciBsYXllcnMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkphY29iaWFucyB2cyBHcmFkaWVudHMg4oCUIFZKUHMgaW4gUHJhY3RpY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIHZlY3Rvci12YWx1ZWQgZnVuY3Rpb24geSA9IGYoeCkgd2l0aCB5IOKIiCDihJ1ebSBhbmQgeCDiiIgg4oSdXm4sIHRoZSBmdWxsIEphY29iaWFuIEogPSDiiIJ5L+KIgngg4oiIIOKEnV57bcOXbn0gaXMgZXhwZW5zaXZlIHRvIG1hdGVyaWFsaXNlIGZvciBsYXJnZSBtLG4uIFJldmVyc2UtbW9kZSBBRCBuZXZlciBmb3JtcyBKIGV4cGxpY2l0bHkuIEluc3RlYWQgaXQgY29tcHV0ZXMgdGhlIHZlY3Rvci1KYWNvYmlhbiBwcm9kdWN0IChWSlApOiB24bWASiBmb3IgYSBnaXZlbiByb3cgdmVjdG9yIHYgKHRoZSB1cHN0cmVhbSBncmFkaWVudCkuIEVhY2ggYmFja3dhcmQgcGFzcyBwcm9kdWNlcyBvbmUgVkpQLCB3aGljaCBnaXZlcyB0aGUgZ3JhZGllbnQgb2YgYSBzY2FsYXIgTCB3cnQgeCBzaW5jZSBkTC9keCA9IChkTC9keSnhtYAgSi4gRm9yIGEgc2NhbGFyIGxvc3MgZEwvZHkgaXMganVzdCBhIHNjYWxhciB0aW1lcyBhIHZlY3Rvciwgc28gdGhlIFZKUCBjb2xsYXBzZXMgdG8gdGhlIGdyYWRpZW50LiBGb3J3YXJkLW1vZGUgQUQgY29tcHV0ZXMgSmFjb2JpYW4tdmVjdG9yIHByb2R1Y3RzIEp2LCB3aGljaCBpcyB1c2VmdWwgZm9yIEhlc3NpYW4tdmVjdG9yIHByb2R1Y3RzIGFuZCBzZWNvbmQtb3JkZXIgbWV0aG9kcyBidXQgcmVxdWlyZXMgb25lIGZvcndhcmQgcGFzcyBwZXIgaW5wdXQgZGltZW5zaW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJyb2FkY2FzdGluZyBpbiB0aGUgQmFja3dhcmQgUGFzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiBhIHRlbnNvciBpcyBicm9hZGNhc3QgaW4gdGhlIGZvcndhcmQgcGFzcyAoZS5nLiwgYmlhcyBiIOKIiCDihJ1eZCBhZGRlZCB0byBaIOKIiCDihJ1ee23Dl2R9KSwgdGhlIGJhY2t3YXJkIHBhc3MgbXVzdCBzdW0gdGhlIHVwc3RyZWFtIGdyYWRpZW50IG92ZXIgdGhlIGJyb2FkY2FzdCBkaW1lbnNpb25zLiBGb3IgdGhlIGJpYXM6IGRML2RiID0gZEwvZFouc3VtKGF4aXM9MCksIGJlY2F1c2UgZWFjaCBlbGVtZW50IG9mIGIgYWZmZWN0ZWQgbSBvdXRwdXQgcm93cy4gRm9yZ2V0dGluZyB0aGlzIHN1bSBpcyBhIGNvbW1vbiBidWcg4oCUIGl0IHByb2R1Y2VzIGEgZEwvZGIgb2Ygc2hhcGUgKG0sIGQpIHJhdGhlciB0aGFuIChkLCkgYW5kIHNpbGVudGx5IGNvcnJ1cHRzIHVwZGF0ZXMuIFB5VG9yY2ggaGFuZGxlcyB0aGlzIGF1dG9tYXRpY2FsbHk7IG1hbnVhbCBpbXBsZW1lbnRhdGlvbnMgbXVzdCBleHBsaWNpdGx5IHJlZHVjZSBvdmVyIGFueSBkaW1lbnNpb25zIGFkZGVkIGJ5IGJyb2FkY2FzdGluZy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNoYWluIHJ1bGUgaW4gY29tcHV0YXRpb24gZ3JhcGhzOiBtdWx0aXBseSBsb2NhbCBKYWNvYmlhbnMgaW4gcmV2ZXJzZSBvcmRlciBmcm9tIGxvc3MgdG8gaW5wdXQuIiwiVkpQICh2ZWN0b3ItSmFjb2JpYW4gcHJvZHVjdCkgaXMgdGhlIGZ1bmRhbWVudGFsIG9wZXJhdGlvbiBvZiByZXZlcnNlLW1vZGUgQUQg4oCUIE8oZm9yd2FyZCkgZm9yIHNjYWxhciBsb3NzLiIsIlJlTFUgYmFja3dhcmQ6IHplcm8tb3V0IGdyYWRpZW50IHdoZXJlIGZvcndhcmQgaW5wdXQgd2FzIOKJpCAwIOKAlCBqdXN0IGEgYmluYXJ5IG1hc2sgbXVsdGlwbHkuIiwiU29mdG1heCArIGNyb3NzLWVudHJvcHkgZ3JhZGllbnQgc2ltcGxpZmllcyB0byAoxbcgLSB5KS9tIOKAlCBhbHdheXMgZGVyaXZlIGNvbWJpbmVkLCBuZXZlciBzZXBhcmF0ZS4iLCJCcm9hZGNhc3RpbmcgaW4gZm9yd2FyZDogc3VtIG92ZXIgY29ycmVzcG9uZGluZyBkaW1lbnNpb25zIGluIGJhY2t3YXJkIG9yIHNoYXBlcyB3aWxsIG5vdCBtYXRjaC4iLCJHcmFkaWVudCBjaGVja2luZzogZmluaXRlIGRpZmZlcmVuY2VzIGF0IGVwcz0xZS01IHdpdGggcmVsYXRpdmUgZXJyb3IgXHUwMDNjIDFlLTQgY29uZmlybXMgY29ycmVjdG5lc3MuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Backward Pass — Chain Rule and Gradient Derivation by Hand

Backpropagation is the algorithm that computes gradients of the loss with respect to every parameter by applying the chain rule in reverse through the computational graph. Understanding it from first principles — deriving gradients by hand for each layer type — demystifies automatic differentiation and is essential for debugging gradient flow, implementing custom operations, and reasoning about training dynamics.

## Chain Rule and Computational Graph Traversal

For a composition f(g(x)), the chain rule gives df/dx = (df/dg)(dg/dx). In a neural network with loss L, the gradient flows backward: dL/dx = (dL/dy)(dy/dx) where y = f(x). In the computational graph, each node stores its local Jacobian dy/dx; backprop multiplies these Jacobians in reverse order from output to input. For a scalar loss and a vector x, dL/dx has the same shape as x — this is the vector-Jacobian product (VJP), the core operation in reverse-mode AD.

## Gradient of a Linear Layer

For z = Wx + b with loss L: the local Jacobian is ∂z/∂x = W. The gradient of W is dL/dW = (dL/dz)ᵀ x (outer product for a single sample) or dL/dW = (dL/dz)ᵀ X for a batch. The gradient of x is dL/dx = Wᵀ (dL/dz). The gradient of b is dL/db = sum of dL/dz over the batch dimension (because b broadcasts). Shape check: if dL/dz has shape (m, d_out) and W has shape (d_out, d_in), then dL/dW = (dL/dz)ᵀ @ X has shape (d_out, d_in) — matching W exactly.

## Gradients of Activation Functions

ReLU: a = max(0, z), so da/dz = 𝟙(z > 0) — a binary mask. Gradient: dL/dz = dL/da ⊙ 𝟙(z > 0). Sigmoid: σ(z) = 1/(1+e⁻ᶻ), derivative σ'(z) = σ(z)(1-σ(z)) — elegantly expressed in terms of the output itself. Gradient: dL/dz = dL/da ⊙ a ⊙ (1-a). Softmax + cross-entropy: when combined, the gradient with respect to the logits z is remarkably clean: dL/dz = (1/m)(ŷ - y) where y is one-hot. This clean gradient is why cross-entropy and softmax are always used together.

```python
import numpy as np

# ---- Forward pass ----
def relu(z):     return np.maximum(0, z)
def softmax(z):  e = np.exp(z - z.max(1, keepdims=True)); return e / e.sum(1, keepdims=True)

def forward(X, W1, b1, W2, b2):
    z1 = X @ W1.T + b1
    a1 = relu(z1)
    z2 = a1 @ W2.T + b2
    y_hat = softmax(z2)
    return y_hat, dict(X=X, z1=z1, a1=a1, z2=z2, W1=W1, W2=W2, b1=b1, b2=b2)

def cross_entropy(y_hat, y):
    m = y.shape[0]
    return -np.log(y_hat[np.arange(m), y] + 1e-12).mean()

# ---- Backward pass (manual chain rule) ----
def backward(y_hat, y_true, cache):
    m = y_true.shape[0]
    X, z1, a1 = cache['X'], cache['z1'], cache['a1']
    W2 = cache['W2']
    # Gradient of softmax + cross-entropy wrt logits z2
    dz2 = y_hat.copy()
    dz2[np.arange(m), y_true] -= 1
    dz2 /= m                         # (m, d_out)
    dW2 = dz2.T @ a1                 # (d_out, d_h)
    db2 = dz2.sum(axis=0)            # (d_out,)
    da1 = dz2 @ W2                   # (m, d_h)
    dz1 = da1 * (z1 > 0).astype(float)  # ReLU mask
    dW1 = dz1.T @ X                  # (d_h, d_in)
    db1 = dz1.sum(axis=0)            # (d_h,)
    return dict(dW1=dW1, db1=db1, dW2=dW2, db2=db2)

np.random.seed(1)
m, d_in, d_h, d_out = 16, 8, 12, 3
X  = np.random.randn(m, d_in)
W1 = np.random.randn(d_h, d_in) * 0.1
b1 = np.zeros(d_h)
W2 = np.random.randn(d_out, d_h) * 0.1
b2 = np.zeros(d_out)
y  = np.random.randint(0, d_out, m)

y_hat, cache = forward(X, W1, b1, W2, b2)
loss = cross_entropy(y_hat, y)
grads = backward(y_hat, y, cache)
print(f'Loss: {loss:.4f}')
for k, v in grads.items():
    print(f'  d{k}: {v.shape}  norm={np.linalg.norm(v):.4f}')
```

## Gradient Checking via Finite Differences

```python
import numpy as np

def numerical_gradient(loss_fn, param, eps=1e-5):
    """Compute numerical gradient of loss_fn wrt param using central differences."""
    grad = np.zeros_like(param)
    it = np.nditer(param, flags=['multi_index'])
    while not it.finished:
        idx = it.multi_index
        orig = param[idx]
        param[idx] = orig + eps
        loss_plus = loss_fn()
        param[idx] = orig - eps
        loss_minus = loss_fn()
        param[idx] = orig
        grad[idx] = (loss_plus - loss_minus) / (2 * eps)
        it.iternext()
    return grad

# Reuse X, W1, b1, W2, b2, y from previous cell
def loss_fn():
    yh, _ = forward(X, W1, b1, W2, b2)
    return cross_entropy(yh, y)

yh, cache = forward(X, W1, b1, W2, b2)
grads = backward(yh, y, cache)

ngrad_W1 = numerical_gradient(loss_fn, W1)
ngrad_W2 = numerical_gradient(loss_fn, W2)

rel_err_W1 = np.abs(grads['dW1'] - ngrad_W1).max() / (np.abs(grads['dW1']).max() + 1e-8)
rel_err_W2 = np.abs(grads['dW2'] - ngrad_W2).max() / (np.abs(grads['dW2']).max() + 1e-8)
print(f'Relative error dW1: {rel_err_W1:.2e}  (should be < 1e-5)')
print(f'Relative error dW2: {rel_err_W2:.2e}  (should be < 1e-5)')
print('Gradient check', 'PASSED' if max(rel_err_W1, rel_err_W2) < 1e-4 else 'FAILED')
```

## PyTorch Autograd Inspection

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(42)
m, d_in, d_h, d_out = 16, 8, 12, 3

model = nn.Sequential(
    nn.Linear(d_in, d_h),
    nn.ReLU(),
    nn.Linear(d_h, d_out)
)
X_t = torch.randn(m, d_in)
y_t = torch.randint(0, d_out, (m,))

# Forward
logits = model(X_t)
loss = nn.CrossEntropyLoss()(logits, y_t)
print(f'Loss: {loss.item():.4f}')

# Backward
loss.backward()

# Inspect gradients
for name, p in model.named_parameters():
    print(f'  {name}: grad.shape={tuple(p.grad.shape)}  '
          f'grad.norm={p.grad.norm().item():.4f}')

# Verify gradient of z2 = (y_hat - y) / m
with torch.no_grad():
    y_hat = torch.softmax(logits, dim=1)
    grad_logits = (y_hat.clone())
    grad_logits[torch.arange(m), y_t] -= 1
    grad_logits /= m
print(f'\nManual dL/dz2 norm: {grad_logits.norm().item():.4f}')
```

## Custom Autograd Function

```python
import torch
from torch.autograd import Function

class LeakyReLUFunction(Function):
    """Custom autograd Function for Leaky ReLU with learnable slope."""

    @staticmethod
    def forward(ctx, x, negative_slope=0.01):
        ctx.save_for_backward(x)
        ctx.negative_slope = negative_slope
        return torch.where(x >= 0, x, negative_slope * x)

    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        slope = ctx.negative_slope
        # dL/dx = grad_output * (1 if x>=0 else slope)
        mask = (x >= 0).float() + slope * (x < 0).float()
        grad_input = grad_output * mask
        return grad_input, None  # None for negative_slope (not a tensor)

# Test against PyTorch built-in
torch.manual_seed(0)
x = torch.randn(4, 6, requires_grad=True)
slope = 0.01

out_custom = LeakyReLUFunction.apply(x, slope)
out_custom.sum().backward()
grad_custom = x.grad.clone()

x.grad = None
out_builtin = torch.nn.functional.leaky_relu(x, slope)
out_builtin.sum().backward()
grad_builtin = x.grad

diff = (grad_custom - grad_builtin).abs().max().item()
print(f'Max grad difference (custom vs builtin): {diff:.2e}')
print('Custom autograd Function correct:', diff < 1e-6)
```

> **Reverse-Mode AD is O(Forward Cost)**: For a scalar loss and n parameters, computing all gradients via reverse-mode AD costs O(forward pass) — not O(n × forward). This is because each backward operation computes a vector-Jacobian product (VJP) rather than the full Jacobian matrix. Forward-mode AD (computing Jacobian-vector products) would require one forward pass per parameter — O(n × forward). Reverse-mode is what makes training billion-parameter networks tractable.

## Layer Gradient Summary

| Layer | dL/dW formula | dL/dx formula | Computational Cost |
| --- | --- | --- | --- |
| Linear z=Wx+b | dL/dz)ᵀ @ X  shape (d_out, d_in) | W.T @ dL/dz  shape (m, d_in) | O(m · d_in · d_out) — same as forward |
| ReLU a=max(0,z) | No weights | dL/da ⊙ 𝟙(z>0) — elementwise mask | O(n) — cheap, just a multiply by 0/1 |
| Sigmoid a=σ(z) | No weights | dL/da ⊙ a(1-a) — uses cached output | O(n) — two multiplies per element |
| Softmax+CE (combined) | No weights in softmax | (ŷ - y)/m — clean closed form | O(m · C) — just subtract one-hot |
| Batch Norm | dL/dγ = Σ dL/dy ⊙ x̂ | Non-trivial — couples all batch samples | O(m · d) — harder than other layers |

## Jacobians vs Gradients — VJPs in Practice

For a vector-valued function y = f(x) with y ∈ ℝ^m and x ∈ ℝ^n, the full Jacobian J = ∂y/∂x ∈ ℝ^{m×n} is expensive to materialise for large m,n. Reverse-mode AD never forms J explicitly. Instead it computes the vector-Jacobian product (VJP): vᵀJ for a given row vector v (the upstream gradient). Each backward pass produces one VJP, which gives the gradient of a scalar L wrt x since dL/dx = (dL/dy)ᵀ J. For a scalar loss dL/dy is just a scalar times a vector, so the VJP collapses to the gradient. Forward-mode AD computes Jacobian-vector products Jv, which is useful for Hessian-vector products and second-order methods but requires one forward pass per input dimension.

## Broadcasting in the Backward Pass

When a tensor is broadcast in the forward pass (e.g., bias b ∈ ℝ^d added to Z ∈ ℝ^{m×d}), the backward pass must sum the upstream gradient over the broadcast dimensions. For the bias: dL/db = dL/dZ.sum(axis=0), because each element of b affected m output rows. Forgetting this sum is a common bug — it produces a dL/db of shape (m, d) rather than (d,) and silently corrupts updates. PyTorch handles this automatically; manual implementations must explicitly reduce over any dimensions added by broadcasting.

- Chain rule in computation graphs: multiply local Jacobians in reverse order from loss to input.
- VJP (vector-Jacobian product) is the fundamental operation of reverse-mode AD — O(forward) for scalar loss.
- ReLU backward: zero-out gradient where forward input was ≤ 0 — just a binary mask multiply.
- Softmax + cross-entropy gradient simplifies to (ŷ - y)/m — always derive combined, never separate.
- Broadcasting in forward: sum over corresponding dimensions in backward or shapes will not match.
- Gradient checking: finite differences at eps=1e-5 with relative error < 1e-4 confirms correctness.

---

