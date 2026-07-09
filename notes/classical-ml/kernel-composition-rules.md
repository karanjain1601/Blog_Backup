---
title: "Kernel Composition Rules"
slug: "kernel-composition-rules"
description: "How to build complex kernels from simple ones using sum, product, exponentiation, and composition rules. Covers automatic relevance determination (ARD), additive kernels, spectral mixture kernels, and how composition affects the RKHS function space."
tags: ["kernel-methods", "gaussian-processes", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT25lIG9mIHRoZSBtb3N0IHBvd2VyZnVsIGFzcGVjdHMgb2Yga2VybmVsIG1ldGhvZHMgaXMgdGhhdCB2YWxpZCBrZXJuZWxzIGFyZSBjbG9zZWQgdW5kZXIgYSByaWNoIHNldCBvZiBjb21wb3NpdGlvbiBvcGVyYXRpb25zLiBTdGFydGluZyBmcm9tIHNpbXBsZSBiYXNlIGtlcm5lbHMgKFJCRiwgcG9seW5vbWlhbCwgbGluZWFyKSwgeW91IGNhbiBidWlsZCBzb3BoaXN0aWNhdGVkIGtlcm5lbHMgZW5jb2RpbmcgcGVyaW9kaWNpdHksIG11bHRpcGxlIGxlbmd0aC1zY2FsZXMsIGFkZGl0aXZlIHN0cnVjdHVyZSwgYW5kIGludGVyYWN0aW9uIGVmZmVjdHMuIEVhY2ggY29tcG9zaXRpb24gcnVsZSBoYXMgYSBjbGVhciBpbnRlcnByZXRhdGlvbiBpbiB0ZXJtcyBvZiB0aGUgUktIUyBmZWF0dXJlIHNwYWNlLCBtYWtpbmcga2VybmVsIGRlc2lnbiBhIHByaW5jaXBsZWQgZW5naW5lZXJpbmcgYWN0aXZpdHkgcmF0aGVyIHRoYW4gdHJpYWwtYW5kLWVycm9yLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBDb21wb3NpdGlvbiBSdWxlcyBNYXR0ZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEga2VybmVsIGsgOiBYIMOXIFgg4oaSIOKEnSBpcyB2YWxpZCBpZiBhbmQgb25seSBpZiBpdCBpcyBzeW1tZXRyaWMgYW5kIHBvc2l0aXZlIHNlbWktZGVmaW5pdGUgKFBTRCkuIFRoZSBjb21wb3NpdGlvbiBydWxlcyBiZWxvdyBndWFyYW50ZWUgdGhhdCBpZiBr4oKBIGFuZCBr4oKCIGFyZSB2YWxpZCBrZXJuZWxzLCB0aGUgcmVzdWx0IG9mIGVhY2ggb3BlcmF0aW9uIGlzIGFsc28gYSB2YWxpZCBrZXJuZWwg4oCUIHByZXNlcnZpbmcgdGhlIFBTRCBwcm9wZXJ0eS4gVGhpcyBtZWFucyB5b3UgY2FuIGZyZWVseSBjb21iaW5lIGtlcm5lbHMgd2l0aG91dCBuZWVkaW5nIHRvIHZlcmlmeSB0aGUgTWVyY2VyIGNvbmRpdGlvbiBmb3IgdGhlIHJlc3VsdC4gVGhlIHJ1bGVzIGFsc28gaGF2ZSBpbnRlcnByZXRhdGlvbnMgaW4gdGVybXMgb2YgZmVhdHVyZSBzcGFjZXMgYW5kIFJLSFMgc3RydWN0dXJlLCBwcm92aWRpbmcgaW50dWl0aW9uIGZvciB3aGF0IGZ1bmN0aW9uIGNsYXNzIHRoZSBjb21wb3NlZCBrZXJuZWwgcmVwcmVzZW50cy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlN1bSBr4oKBK2vigoI6IFJLSFMgPSBkaXJlY3Qgc3VtIEhfazEg4oqVIEhfazIg4oCUIGZ1bmN0aW9uIGNsYXNzIGlzIHRoZSB1bmlvbi4iLCJQcm9kdWN0IGvigoHCt2vigoI6IFJLSFMgPSB0ZW5zb3IgcHJvZHVjdCBIX2sxIOKKlyBIX2syIOKAlCBjYXB0dXJlcyBpbnRlcmFjdGlvbnMuIiwiU2NhbGFyIGPCt2sgKGMgXHUwMDNlIDApOiByZXNjYWxlZCBSS0hTIEhfayDigJQgYWRqdXN0cyBzaWduYWwgdmFyaWFuY2UuIiwiZXhwKGspOiBSS0hTID0gc3VtIG92ZXIgYWxsIHRlbnNvciBwb3dlcnMg4oCUIGluZmluaXRlLW9yZGVyIGludGVyYWN0aW9ucy4iLCJmKHgpwrdrKHgseinCt2Yoeik6IHJlLXdlaWdodGVkIFJLSFMg4oCUIGRvd24td2VpZ2h0cyByZWdpb25zIHdoZXJlIHxmfCBpcyBzbWFsbC4iLCJrKM+GKHgpLCDPhih6KSk6IGNvbXBvc2VkIHdpdGggaW5wdXQgbWFwIM+GIOKAlCBhcHBsaWVzIGtlcm5lbCBhZnRlciBmZWF0dXJlIHRyYW5zZm9ybS4iLCJBUkQ6IHBlci1kaW1lbnNpb24gbGVuZ3RoLXNjYWxlcyDigJQgZWZmZWN0aXZlbHkgbGVhcm5zIGZlYXR1cmUgaW1wb3J0YW5jZS4iLCJBZGRpdGl2ZSDOo+KClyBr4oKXKHjigpcsIHrigpcpOiBzdW0gb2YgMUQga2VybmVscyDigJQgaW50ZXJwcmV0YWJsZSwgYWRkaXRpdmUgc3RydWN0dXJlLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdW0gYW5kIFByb2R1Y3Qgb2YgS2VybmVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3VtIGFuZCBwcm9kdWN0IGFyZSB0aGUgdHdvIG1vc3QgZnVuZGFtZW50YWwgY29tcG9zaXRpb24gcnVsZXMuIFRoZSBzdW0ga+KCgStr4oKCIGlzIHRoZSBjb3ZhcmlhbmNlIG9mIGEgR1AgcHJpb3IgdGhhdCBpcyB0aGUgc3VtIG9mIHR3byBpbmRlcGVuZGVudCBHUHMg4oCUIGl0IGJlbG9uZ3MgdG8gYm90aCBmdW5jdGlvbiBjbGFzc2VzIHNpbXVsdGFuZW91c2x5LiBUaGUgcHJvZHVjdCBr4oKBwrdr4oKCIGNyZWF0ZXMgYSBrZXJuZWwgd2hlcmUgdHdvIGZ1bmN0aW9ucyBtdXN0IGJlIHNpbWlsYXIgaW4gYm90aCBzZW5zZXMgc2ltdWx0YW5lb3VzbHk7IGdlb21ldHJpY2FsbHksIHRoZSBmZWF0dXJlIG1hcCBpcyB0aGUgdGVuc29yIHByb2R1Y3Qgz4YoeCniipfPiCh4KSwgZW5jb2RpbmcgYWxsIHBhaXJ3aXNlIGludGVyYWN0aW9ucyBiZXR3ZWVuIHRoZSB0d28gZmVhdHVyZSBzcGFjZXMuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJrX3tcXHRleHR7c3VtfX0oeCx6KSA9IGtfMSh4LHopICsga18yKHgseikgXFxpbXBsaWVzIEhfe2tfe1xcdGV4dHtzdW19fX0gPSBIX3trXzF9IFxcb3BsdXMgSF97a18yfSJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50Ijoia197XFx0ZXh0e3Byb2R9fSh4LHopID0ga18xKHgseikgXFxjZG90IGtfMih4LHopIFxcaW1wbGllcyBIX3trX3tcXHRleHR7cHJvZH19fSBcXHN1cHNldGVxIEhfe2tfMX0gXFxvdGltZXMgSF97a18yfSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4cG9uZW50aWFsIGFuZCBGdW5jdGlvbiBXZWlnaHRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBleHBvbmVudGlhbCBvZiBhIHZhbGlkIGtlcm5lbCBleHAoayh4LHopKSBpcyBhbHNvIHZhbGlkLiBUaGlzIGZvbGxvd3MgZnJvbSB0aGUgVGF5bG9yIGV4cGFuc2lvbjogZXhwKGspID0gzqPigpkga15uL24hLCB3aGljaCBpcyBhbiBpbmZpbml0ZSBzdW0gb2YgcHJvZHVjdHMgb2YgdmFsaWQga2VybmVscyAoZWFjaCBrXm4gaXMgdmFsaWQgYnkgdGhlIHByb2R1Y3QgcnVsZSkuIFRoZSByZXN1bHRpbmcgUktIUyBjb250YWlucyBhbGwgZmluaXRlLWRlZ3JlZSBwb2x5bm9taWFsIGludGVyYWN0aW9ucyBvZiB0aGUgb3JpZ2luYWwgZmVhdHVyZXMuIEZ1bmN0aW9uIHdlaWdodGluZyBmKHgpwrdrKHgseinCt2YoeikgZm9yIGFueSBzY2FsYXIgZnVuY3Rpb24gZiBpcyB2YWxpZCBiZWNhdXNlIGl0IHNpbXBseSByZS1zY2FsZXMgdGhlIGZlYXR1cmUgbWFwOiDPhsyDKHgpID0gZih4KcK3z4YoeCksIHdoaWNoIHByZXNlcnZlcyB0aGUgaW5uZXIgcHJvZHVjdCBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJcXGV4cChrKHgseikpID0gXFxzdW1fe249MH1ee1xcaW5mdHl9IFxcZnJhY3trKHgseilebn17biF9IFxccXVhZCBcXHRleHR7KGluZmluaXRlIHN1bSBvZiB2YWxpZCBrZXJuZWxzKX0ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkNsb3N1cmUgUHJvcGVydGllcyBTdW1tYXJ5IiwiY29udGVudCI6IlZhbGlkIGtlcm5lbHMgYXJlIGNsb3NlZCB1bmRlcjogYWRkaXRpb24sIG11bHRpcGxpY2F0aW9uLCBwb3NpdGl2ZSBzY2FsYXIgbXVsdGlwbGljYXRpb24sIGV4cG9uZW50aWF0aW9uLCBjb21wb3NpdGlvbiB3aXRoIGEgZml4ZWQgaW5wdXQgbWFwIM+GLCBhbmQgbXVsdGlwbGljYXRpb24gYnkgZih4KWYoeikgZm9yIGFueSBmdW5jdGlvbiBmLiBUaGlzIG1lYW5zIGFueSBmaW5pdGUgY29tYmluYXRpb24gb2YgYmFzZSBrZXJuZWxzIHVzaW5nIHRoZXNlIG9wZXJhdGlvbnMgaXMgYXV0b21hdGljYWxseSBhIHZhbGlkIE1lcmNlciBrZXJuZWwg4oCUIG5vIG5lZWQgdG8gcmUtdmVyaWZ5IHRoZSBQU0QgY29uZGl0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1dG9tYXRpYyBSZWxldmFuY2UgRGV0ZXJtaW5hdGlvbiAoQVJEKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEFSRCBrZXJuZWwgZXh0ZW5kcyB0aGUgaXNvdHJvcGljIFJCRiBieSBhc3NpZ25pbmcgYW4gaW5kZXBlbmRlbnQgbGVuZ3RoLXNjYWxlIOKEk+G1oiB0byBlYWNoIGlucHV0IGRpbWVuc2lvbi4gRGltZW5zaW9ucyB3aXRoIGxhcmdlIOKEk+G1oiBjb250cmlidXRlIGxpdHRsZSB0byBrZXJuZWwgc2ltaWxhcml0eSAodGhleSBhcmUgZWZmZWN0aXZlbHkgaWdub3JlZCksIHdoaWxlIGRpbWVuc2lvbnMgd2l0aCBzbWFsbCDihJPhtaIgaGF2ZSBzdHJvbmcgaW5mbHVlbmNlLiBXaGVuIOKEk+G1oiBpcyBsZWFybmVkIHZpYSBtYXJnaW5hbCBsaWtlbGlob29kIG1heGltaXphdGlvbiwgdGhlIEFSRCBrZXJuZWwgYXV0b21hdGljYWxseSBwZXJmb3JtcyBmZWF0dXJlIHNlbGVjdGlvbjogaXJyZWxldmFudCBmZWF0dXJlcyBnZXQgcHVzaGVkIHRvIGluZmluaXR5LCBtYWtpbmcgdGhlbSBpbnZpc2libGUgdG8gdGhlIG1vZGVsLiBUaGlzIG1ha2VzIEFSRCBrZXJuZWxzIHBvd2VyZnVsIGZvciBoaWdoLWRpbWVuc2lvbmFsIHJlZ3Jlc3Npb24gd2l0aCBzcGFyc2UgcmVsZXZhbmNlLiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50Ijoia197XFx0ZXh0e0FSRH19KHgsIHopID0gXFxzaWdtYV4yIFxcZXhwXFwhXFxsZWZ0KC1cXHN1bV97aT0xfV5wIFxcZnJhY3soeF9pIC0gel9pKV4yfXsyXFxlbGxfaV4yfVxccmlnaHQpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWRkaXRpdmUgS2VybmVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWRkaXRpdmUga2VybmVscyBrKHgseikgPSDOo+KClyBr4oKXKHjigpcsIHrigpcpIGRlY29tcG9zZSB0aGUgZnVuY3Rpb24gYXMgYSBzdW0gb2YgcGVyLWZlYXR1cmUgY29udHJpYnV0aW9uczogZih4KSA9IM6j4oKXIGbigpcoeOKClykuIFRoaXMgYWRkaXRpdmUgc3RydWN0dXJlIGlzIGludGVycHJldGFibGUg4oCUIHlvdSBjYW4gZXhhbWluZSBm4oKXIGluZGl2aWR1YWxseSB0byB1bmRlcnN0YW5kIGhvdyBlYWNoIGZlYXR1cmUgYWZmZWN0cyB0aGUgb3V0cHV0LiBJdCBhbHNvIGF2b2lkcyB0aGUgY3Vyc2Ugb2YgZGltZW5zaW9uYWxpdHkgc2luY2UgZWFjaCBm4oKXIGlzIGZpdCBpbiAxRC4gQWRkaXRpdmUga2VybmVscyBjb21iaW5lIHdlbGwgd2l0aCBwb2x5bm9taWFsIG9yIGludGVyYWN0aW9uIHRlcm1zOiBrID0gzqPigpcga+KClyh44oKXLHrigpcpICsgzqPigpdcdTAwM2Pigpgga+KCl8K3a+KCmCBnaXZlcyB1cCB0byBkZWdyZWUtMiBpbnRlcmFjdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3BlY3RyYWwgYW5kIFRlbnNvci1Qcm9kdWN0IEtlcm5lbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzcGVjdHJhbCBtaXh0dXJlIGtlcm5lbCAoV2lsc29uIFx1MDAyNiBBZGFtcywgMjAxMykgcmVwcmVzZW50cyB0aGUga2VybmVsIGFzIGEgbWl4dHVyZSBvZiBSQkYga2VybmVscyBpbiB0aGUgc3BlY3RyYWwgKGZyZXF1ZW5jeSkgZG9tYWluOiBrKM+EKSA9IM6jcSB3cSBleHAo4oiSMs+AwrLPhMKydnEpIGNvcygyz4DPhM68cSkuIEVhY2ggY29tcG9uZW50IGNhcHR1cmVzIG9zY2lsbGF0aW9ucyBhdCBmcmVxdWVuY3kgzrxxIHdpdGggYmFuZHdpZHRoIHZxLiBUaGlzIGFsbG93cyB0aGUgbW9kZWwgdG8gYXV0b21hdGljYWxseSBkaXNjb3ZlciBwZXJpb2RpYyBzdHJ1Y3R1cmUgZnJvbSBkYXRhIHdpdGhvdXQgc3BlY2lmeWluZyB0aGUgcGVyaW9kIGluIGFkdmFuY2UuIFNwZWN0cmFsIG1peHR1cmUga2VybmVscyBhcmUgYW1vbmcgdGhlIG1vc3QgZXhwcmVzc2l2ZSBzdGF0aW9uYXJ5IGtlcm5lbHMgYW5kIGNhbiBhcHByb3hpbWF0ZSBhbnkgc3RhdGlvbmFyeSBrZXJuZWwgZ2l2ZW4gZW5vdWdoIGNvbXBvbmVudHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSBFeGFtcGxlcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGlzX3BzZChLLCB0b2w9MWUtOSk6XG4gICAgcmV0dXJuIG5wLmFsbChucC5saW5hbGcuZWlndmFsc2goSykgXHUwMDNlPSAtdG9sKVxuXG5kZWYgcmJmX2dyYW0oWCwgZWxsPTEuMCk6XG4gICAgZGlmZiA9IFhbOiwgTm9uZSwgOl0gLSBYW05vbmUsIDosIDpdXG4gICAgcmV0dXJuIG5wLmV4cCgtbnAuc3VtKGRpZmYqKjIsIGF4aXM9LTEpIC8gKDIgKiBlbGwqKjIpKVxuXG5kZWYgcG9seV9ncmFtKFgsIGQ9MiwgYz0xLjApOlxuICAgIHJldHVybiAoWCBAIFguVCArIGMpICoqIGRcblxucm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKDApXG5YID0gcm5nLnJhbmRuKDI1LCAzKVxuXG5LMSA9IHJiZl9ncmFtKFgsIGVsbD0xLjApXG5LMiA9IHBvbHlfZ3JhbShYLCBkPTIpXG5cbiMgUnVsZSAxOiBTdW0gb2YgdmFsaWQga2VybmVsc1xuS19zdW0gPSBLMSArIEsyXG5wcmludChmXHUwMDI3azEgKyBrMiBQU0Q6IHtpc19wc2QoS19zdW0pfVx1MDAyNylcblxuIyBSdWxlIDI6IFByb2R1Y3Qgb2YgdmFsaWQga2VybmVsc1xuS19wcm9kID0gSzEgKiBLMlxucHJpbnQoZlx1MDAyN2sxICogazIgUFNEOiB7aXNfcHNkKEtfcHJvZCl9XHUwMDI3KVxuXG4jIFJ1bGUgMzogUG9zaXRpdmUgc2NhbGFyIG11bHRpcGxlXG5LX3NjYWxlZCA9IDMuMCAqIEsxXG5wcmludChmXHUwMDI3My4wICogazEgUFNEOiB7aXNfcHNkKEtfc2NhbGVkKX1cdTAwMjcpXG5cbiMgUnVsZSA0OiBleHAoaykgaXMgdmFsaWRcbktfZXhwID0gbnAuZXhwKEsxKVxucHJpbnQoZlx1MDAyN2V4cChrMSkgUFNEOiB7aXNfcHNkKEtfZXhwKX1cdTAwMjcpXG5cbiMgUnVsZSA1OiBmKHgpKmsoeCx6KSpmKHopIHdlaWdodGluZ1xudyA9IG5wLmFicyhybmcucmFuZG4oMjUpKSArIDAuMVxuS193ZWlnaHRlZCA9IG5wLm91dGVyKHcsIHcpICogSzFcbnByaW50KGZcdTAwMjd3KHgpKmsxKncoeikgUFNEOiB7aXNfcHNkKEtfd2VpZ2h0ZWQpfVx1MDAyNykifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFsbCBjb21wb3NpdGlvbiBydWxlcyBwcmVzZXJ2ZSB0aGUgUFNEIHByb3BlcnR5LiBUaGUgcHJvZHVjdCBydWxlIHVzZXMgZWxlbWVudHdpc2UgbXVsdGlwbGljYXRpb24gb2YgdGhlIEdyYW0gbWF0cmljZXMsIHdoaWNoIGNvcnJlc3BvbmRzIHRvIHRoZSB0ZW5zb3IgcHJvZHVjdCBvZiBmZWF0dXJlIG1hcHMuIFRoZSBleHAgcnVsZSBjcmVhdGVzIGFuIGluZmluaXRlIHNlcmllcyBvZiBpbnRlcmFjdGlvbnMg4oCUIHRoZSByZXN1bHRpbmcga2VybmVsIGlzIGV2ZW4gbW9yZSBleHByZXNzaXZlIHRoYW4gdGhlIG9yaWdpbmFsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5cbmRlZiBhcmRfa2VybmVsKFgxLCBYMiwgbGVuZ3RoX3NjYWxlcywgc2lnbWEyPTEuMCk6XG4gICAgIyBBUkQgUkJGOiBwZXItZGltZW5zaW9uIGxlbmd0aCBzY2FsZXNcbiAgICBkaWZmID0gWDFbOiwgTm9uZSwgOl0gLSBYMltOb25lLCA6LCA6XVxuICAgIHNjYWxlZCA9IGRpZmYgLyBsZW5ndGhfc2NhbGVzW05vbmUsIE5vbmUsIDpdXG4gICAgcmV0dXJuIHNpZ21hMiAqIG5wLmV4cCgtMC41ICogbnAuc3VtKHNjYWxlZCoqMiwgYXhpcz0tMSkpXG5cbmRlZiBuZWdfbG9nX21hcmdpbmFsX2xpa2VsaWhvb2QobG9nX3BhcmFtcywgWCwgeSwgbm9pc2U9MWUtMyk6XG4gICAgZCA9IFguc2hhcGVbMV1cbiAgICBlbGwgPSBucC5leHAobG9nX3BhcmFtc1s6ZF0pXG4gICAgc2lnbWEyID0gbnAuZXhwKGxvZ19wYXJhbXNbZF0pXG4gICAgSyA9IGFyZF9rZXJuZWwoWCwgWCwgZWxsLCBzaWdtYTIpICsgbm9pc2UgKiBucC5leWUobGVuKFgpKVxuICAgIHRyeTpcbiAgICAgICAgTCA9IG5wLmxpbmFsZy5jaG9sZXNreShLKVxuICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJyb3I6XG4gICAgICAgIHJldHVybiAxZTEwXG4gICAgYWxwaGEgPSBucC5saW5hbGcuc29sdmUoTC5ULCBucC5saW5hbGcuc29sdmUoTCwgeSkpXG4gICAgbG9nX2RldCA9IDIgKiBucC5zdW0obnAubG9nKG5wLmRpYWcoTCkpKVxuICAgIHJldHVybiAwLjUgKiAoeSBAIGFscGhhICsgbG9nX2RldCArIGxlbih5KSAqIG5wLmxvZygyICogbnAucGkpKVxuXG5ybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoMSlcblggPSBybmcucmFuZG4oNjAsIDQpXG4jIE9ubHkgZGltcyAwIGFuZCAyIGFyZSByZWxldmFudFxueSA9IDIgKiBYWzosIDBdICsgMC41ICogWFs6LCAyXSArIHJuZy5yYW5kbig2MCkgKiAwLjFcblxueDAgPSBucC56ZXJvcyg1KSAgIyA0IGxlbmd0aC1zY2FsZXMgKyAxIHZhcmlhbmNlXG5yZXN1bHQgPSBtaW5pbWl6ZShuZWdfbG9nX21hcmdpbmFsX2xpa2VsaWhvb2QsIHgwLCBhcmdzPShYLCB5KSwgbWV0aG9kPVx1MDAyN0wtQkZHUy1CXHUwMDI3KVxubGVhcm5lZF9lbGwgPSBucC5leHAocmVzdWx0LnhbOjRdKVxucHJpbnQoZlx1MDAyN0xlYXJuZWQgbGVuZ3RoLXNjYWxlczoge2xlYXJuZWRfZWxsLnJvdW5kKDMpfVx1MDAyNylcbnByaW50KFx1MDAyN1NtYWxsIGVsbCA9IHJlbGV2YW50IGZlYXR1cmU7IGxhcmdlIGVsbCA9IGlycmVsZXZhbnQgZmVhdHVyZVx1MDAyNykifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiByYmZfMWQoeDEsIHgyLCBlbGw9MS4wKTpcbiAgICBkaWZmID0gbnAuc3VidHJhY3Qub3V0ZXIoeDEsIHgyKVxuICAgIHJldHVybiBucC5leHAoLWRpZmYqKjIgLyAoMiAqIGVsbCoqMikpXG5cbmRlZiBhZGRpdGl2ZV9rZXJuZWwoWDEsIFgyLCBlbGxzPU5vbmUpOlxuICAgICMgQWRkaXRpdmU6IHN1bSBvZiAxRCBSQkYga2VybmVscyBvdmVyIGVhY2ggZGltZW5zaW9uXG4gICAgZCA9IFgxLnNoYXBlWzFdXG4gICAgaWYgZWxscyBpcyBOb25lOlxuICAgICAgICBlbGxzID0gbnAub25lcyhkKVxuICAgIEsgPSBucC56ZXJvcygobGVuKFgxKSwgbGVuKFgyKSkpXG4gICAgZm9yIGogaW4gcmFuZ2UoZCk6XG4gICAgICAgIEsgKz0gcmJmXzFkKFgxWzosIGpdLCBYMls6LCBqXSwgZWxsc1tqXSlcbiAgICByZXR1cm4gS1xuXG5ybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoNDIpXG5YX3RyYWluID0gcm5nLnJhbmRuKDUwLCAzKVxuIyBBZGRpdGl2ZSBncm91bmQgdHJ1dGg6IHNpbih4MCkgKyB4MV4yICsgMC41KngyXG55X3RyYWluID0gbnAuc2luKFhfdHJhaW5bOiwgMF0pICsgWF90cmFpbls6LCAxXSoqMiArIDAuNSAqIFhfdHJhaW5bOiwgMl1cblxubGFtID0gMC4wMVxuSyA9IGFkZGl0aXZlX2tlcm5lbChYX3RyYWluLCBYX3RyYWluKSArIGxhbSAqIG5wLmV5ZSg1MClcbmFscGhhID0gbnAubGluYWxnLnNvbHZlKEssIHlfdHJhaW4pXG5cblhfdGVzdCA9IHJuZy5yYW5kbigyMCwgMylcbktfc3RhciA9IGFkZGl0aXZlX2tlcm5lbChYX3Rlc3QsIFhfdHJhaW4pXG55X3ByZWQgPSBLX3N0YXIgQCBhbHBoYVxueV90cnVlID0gbnAuc2luKFhfdGVzdFs6LCAwXSkgKyBYX3Rlc3RbOiwgMV0qKjIgKyAwLjUgKiBYX3Rlc3RbOiwgMl1cbnIyID0gMSAtIG5wLnZhcih5X3RydWUgLSB5X3ByZWQpIC8gbnAudmFyKHlfdHJ1ZSlcbnByaW50KGZcdTAwMjdBZGRpdGl2ZSBrZXJuZWwgcmlkZ2UgcmVncmVzc2lvbiBSMjoge3IyOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdrKHgseikgPSBzdW1faiBrX2ooeF9qLCB6X2opIGRlY29tcG9zZXMgaW50byBpbnRlcnByZXRhYmxlIDFEIHRlcm1zXHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCByMl9zY29yZVxuXG5kZWYgc3BlY3RyYWxfbWl4dHVyZV9rZXJuZWxfMWQoeDEsIHgyLCB3ZWlnaHRzLCBtZWFucywgdmFyaWFuY2VzKTpcbiAgICAjIFNwZWN0cmFsIG1peHR1cmUga2VybmVsIChXaWxzb24gXHUwMDI2IEFkYW1zLCAyMDEzKVxuICAgICMgayh0YXUpID0gc3VtX3Egd19xIGV4cCgtMnBpXjIgdGF1XjIgdl9xKSBjb3MoMnBpIHRhdSBtdV9xKVxuICAgIHRhdSA9IG5wLnN1YnRyYWN0Lm91dGVyKHgxLCB4MilcbiAgICBLID0gbnAuemVyb3NfbGlrZSh0YXUsIGR0eXBlPWZsb2F0KVxuICAgIGZvciB3LCBtdSwgdiBpbiB6aXAod2VpZ2h0cywgbWVhbnMsIHZhcmlhbmNlcyk6XG4gICAgICAgIEsgKz0gdyAqIG5wLmV4cCgtMiAqIG5wLnBpKioyICogdGF1KioyICogdikgKiBucC5jb3MoMiAqIG5wLnBpICogdGF1ICogbXUpXG4gICAgcmV0dXJuIEtcblxuIyBTaWduYWwgd2l0aCB0d28gcGVyaW9kaWMgY29tcG9uZW50c1xucm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKDcpXG54ID0gbnAubGluc3BhY2UoMCwgMTAsIDIwMClcbnkgPSBucC5zaW4oMiAqIG5wLnBpICogeCAvIDMpICsgMC41ICogbnAuc2luKDIgKiBucC5waSAqIHggLyAxLjUpICsgcm5nLnJhbmRuKDIwMCkgKiAwLjA1XG5cbiMgVGhyZWUtY29tcG9uZW50IHNwZWN0cmFsIG1peHR1cmVcbksgPSBzcGVjdHJhbF9taXh0dXJlX2tlcm5lbF8xZChcbiAgICB4LCB4LFxuICAgIHdlaWdodHM9WzEuMCwgMC41LCAwLjNdLFxuICAgIG1lYW5zPVsxLzMsIDIvMywgMS4wXSxcbiAgICB2YXJpYW5jZXM9WzAuMDEsIDAuMDEsIDAuMDFdXG4pXG5LICs9IDFlLTYgKiBucC5leWUobGVuKHgpKVxuYWxwaGEgPSBucC5saW5hbGcuc29sdmUoSywgeSlcbnlfcHJlZCA9IEsgQCBhbHBoYVxucHJpbnQoZlx1MDAyN1NwZWN0cmFsIG1peHR1cmUga2VybmVsIGZpdCBSMjoge3IyX3Njb3JlKHksIHlfcHJlZCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN1NwZWN0cmFsIG1peHR1cmUga2VybmVscyBsZWFybiBwZXJpb2RpYyBzdHJ1Y3R1cmUgYXV0b21hdGljYWxseSBmcm9tIGRhdGEuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBvc2l0aW9uIFJ1bGVzIFJlZmVyZW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDb21wb3NpdGlvbiBSdWxlIiwiTmV3IEtlcm5lbCBFeHByZXNzaW9uIiwiUktIUyAvIEZlYXR1cmUgU3BhY2UiLCJQcmFjdGljYWwgVXNlIENhc2UiXSwicm93cyI6W1siU3VtIGvigoEra+KCgiIsImsoeCx6KSA9IGvigoEoeCx6KSArIGvigoIoeCx6KSIsIkRpcmVjdCBzdW0gSOKCgSDiipUgSOKCgiIsIkNvbWJpbmluZyBSQkYgdHJlbmQgKyBwZXJpb2RpYyBzZWFzb25hbGl0eSJdLFsiUHJvZHVjdCBr4oKBwrdr4oKCIiwiayh4LHopID0ga+KCgSh4LHopIMOXIGvigoIoeCx6KSIsIlRlbnNvciBwcm9kdWN0IEjigoEg4oqXIEjigoIiLCJMb2NhbGl6ZWQgcGVyaW9kaWM6IFJCRiDDlyBwZXJpb2RpYyJdLFsiU2NhbGFyIGPCt2sgKGNcdTAwM2UwKSIsImsoeCx6KSA9IGMgwrcga+KCgSh4LHopIiwiUmVzY2FsZWQgSOKCgSIsIkFkanVzdGluZyBzaWduYWwgdmFyaWFuY2UgYW1wbGl0dWRlIl0sWyJFeHBvbmVudGlhdGlvbiBleHAoaykiLCJrKHgseikgPSBleHAoa+KCgSh4LHopKSIsIkFsbCB0ZW5zb3IgcG93ZXJzIG9mIEjigoEiLCJOb25saW5lYXIgZmVhdHVyZSBlbmhhbmNlbWVudCJdLFsiQVJEIGtlcm5lbCIsImsoeCx6KSA9IGV4cCjiiJLOo+G1oih44bWi4oiSeuG1oinCsi8y4oST4bWiwrIpIiwiQW5pc290cm9waWMgUkJGIGZlYXR1cmUgc3BhY2UiLCJBdXRvbWF0aWMgZmVhdHVyZSBzZWxlY3Rpb24gdmlhIOKEk+G1oiDihpIg4oieIl0sWyJBZGRpdGl2ZSDOo+KClyBr4oKXIiwiayh4LHopID0gzqPigpcga+KClyh44oKXLCB64oKXKSIsIlN1bSBvZiAxRCBmZWF0dXJlIHNwYWNlcyIsIkludGVycHJldGFibGUgZGVjb21wb3NpdGlvbiBieSBmZWF0dXJlIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Iktlcm5lbCBjb21wb3NpdGlvbiBpcyB0aGUgcHJpbWFyeSB0b29sIGZvciBlbmNvZGluZyBkb21haW4ga25vd2xlZGdlIGludG8ga2VybmVsIG1ldGhvZHMgYW5kIEdQcy4gQnkgY29tYmluaW5nIGJhc2Uga2VybmVscyB3aXRoIHRoZXNlIHJ1bGVzLCB5b3UgY2FuIGNhcHR1cmUgbXVsdGktc2NhbGUgc3RydWN0dXJlLCBwZXJpb2RpY2l0eSwgYWRkaXRpdmUgZGVjb21wb3NpdGlvbnMsIGFuZCBmZWF0dXJlIGludGVyYWN0aW9ucyDigJQgYWxsIHdoaWxlIGd1YXJhbnRlZWluZyB0aGUgcmVzdWx0IGlzIGEgdmFsaWQgTWVyY2VyIGtlcm5lbC4gVGhlIGxlYXJuZWQgaHlwZXJwYXJhbWV0ZXJzIChsZW5ndGgtc2NhbGVzLCB3ZWlnaHRzKSBwcm92aWRlIGludGVycHJldGFibGUgbWVhc3VyZXMgb2YgZmVhdHVyZSBpbXBvcnRhbmNlIGFuZCBzaWduYWwgc3RydWN0dXJlLiJ9XQ=="
---
# Kernel Composition Rules

One of the most powerful aspects of kernel methods is that valid kernels are closed under a rich set of composition operations. Starting from simple base kernels (RBF, polynomial, linear), you can build sophisticated kernels encoding periodicity, multiple length-scales, additive structure, and interaction effects. Each composition rule has a clear interpretation in terms of the RKHS feature space, making kernel design a principled engineering activity rather than trial-and-error.

## Why Composition Rules Matter

A kernel k : X × X → ℝ is valid if and only if it is symmetric and positive semi-definite (PSD). The composition rules below guarantee that if k₁ and k₂ are valid kernels, the result of each operation is also a valid kernel — preserving the PSD property. This means you can freely combine kernels without needing to verify the Mercer condition for the result. The rules also have interpretations in terms of feature spaces and RKHS structure, providing intuition for what function class the composed kernel represents.

- Sum k₁+k₂: RKHS = direct sum H_k1 ⊕ H_k2 — function class is the union.
- Product k₁·k₂: RKHS = tensor product H_k1 ⊗ H_k2 — captures interactions.
- Scalar c·k (c > 0): rescaled RKHS H_k — adjusts signal variance.
- exp(k): RKHS = sum over all tensor powers — infinite-order interactions.
- f(x)·k(x,z)·f(z): re-weighted RKHS — down-weights regions where |f| is small.
- k(φ(x), φ(z)): composed with input map φ — applies kernel after feature transform.
- ARD: per-dimension length-scales — effectively learns feature importance.
- Additive Σₗ kₗ(xₗ, zₗ): sum of 1D kernels — interpretable, additive structure.

## Sum and Product of Kernels

Sum and product are the two most fundamental composition rules. The sum k₁+k₂ is the covariance of a GP prior that is the sum of two independent GPs — it belongs to both function classes simultaneously. The product k₁·k₂ creates a kernel where two functions must be similar in both senses simultaneously; geometrically, the feature map is the tensor product φ(x)⊗ψ(x), encoding all pairwise interactions between the two feature spaces.

$$k_{\text{sum}}(x,z) = k_1(x,z) + k_2(x,z) \implies H_{k_{\text{sum}}} = H_{k_1} \oplus H_{k_2}$$

$$k_{\text{prod}}(x,z) = k_1(x,z) \cdot k_2(x,z) \implies H_{k_{\text{prod}}} \supseteq H_{k_1} \otimes H_{k_2}$$

## Exponential and Function Weighting

The exponential of a valid kernel exp(k(x,z)) is also valid. This follows from the Taylor expansion: exp(k) = Σₙ k^n/n!, which is an infinite sum of products of valid kernels (each k^n is valid by the product rule). The resulting RKHS contains all finite-degree polynomial interactions of the original features. Function weighting f(x)·k(x,z)·f(z) for any scalar function f is valid because it simply re-scales the feature map: φ̃(x) = f(x)·φ(x), which preserves the inner product structure.

$$\exp(k(x,z)) = \sum_{n=0}^{\infty} \frac{k(x,z)^n}{n!} \quad \text{(infinite sum of valid kernels)}$$

> **Closure Properties Summary**: Valid kernels are closed under: addition, multiplication, positive scalar multiplication, exponentiation, composition with a fixed input map φ, and multiplication by f(x)f(z) for any function f. This means any finite combination of base kernels using these operations is automatically a valid Mercer kernel — no need to re-verify the PSD condition.

## Automatic Relevance Determination (ARD)

The ARD kernel extends the isotropic RBF by assigning an independent length-scale ℓᵢ to each input dimension. Dimensions with large ℓᵢ contribute little to kernel similarity (they are effectively ignored), while dimensions with small ℓᵢ have strong influence. When ℓᵢ is learned via marginal likelihood maximization, the ARD kernel automatically performs feature selection: irrelevant features get pushed to infinity, making them invisible to the model. This makes ARD kernels powerful for high-dimensional regression with sparse relevance.

$$k_{\text{ARD}}(x, z) = \sigma^2 \exp\!\left(-\sum_{i=1}^p \frac{(x_i - z_i)^2}{2\ell_i^2}\right)$$

## Additive Kernels

Additive kernels k(x,z) = Σₗ kₗ(xₗ, zₗ) decompose the function as a sum of per-feature contributions: f(x) = Σₗ fₗ(xₗ). This additive structure is interpretable — you can examine fₗ individually to understand how each feature affects the output. It also avoids the curse of dimensionality since each fₗ is fit in 1D. Additive kernels combine well with polynomial or interaction terms: k = Σₗ kₗ(xₗ,zₗ) + Σₗ<ₘ kₗ·kₘ gives up to degree-2 interactions.

## Spectral and Tensor-Product Kernels

The spectral mixture kernel (Wilson & Adams, 2013) represents the kernel as a mixture of RBF kernels in the spectral (frequency) domain: k(τ) = Σq wq exp(−2π²τ²vq) cos(2πτμq). Each component captures oscillations at frequency μq with bandwidth vq. This allows the model to automatically discover periodic structure from data without specifying the period in advance. Spectral mixture kernels are among the most expressive stationary kernels and can approximate any stationary kernel given enough components.

## Code Examples

```python
import numpy as np

def is_psd(K, tol=1e-9):
    return np.all(np.linalg.eigvalsh(K) >= -tol)

def rbf_gram(X, ell=1.0):
    diff = X[:, None, :] - X[None, :, :]
    return np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

def poly_gram(X, d=2, c=1.0):
    return (X @ X.T + c) ** d

rng = np.random.RandomState(0)
X = rng.randn(25, 3)

K1 = rbf_gram(X, ell=1.0)
K2 = poly_gram(X, d=2)

# Rule 1: Sum of valid kernels
K_sum = K1 + K2
print(f'k1 + k2 PSD: {is_psd(K_sum)}')

# Rule 2: Product of valid kernels
K_prod = K1 * K2
print(f'k1 * k2 PSD: {is_psd(K_prod)}')

# Rule 3: Positive scalar multiple
K_scaled = 3.0 * K1
print(f'3.0 * k1 PSD: {is_psd(K_scaled)}')

# Rule 4: exp(k) is valid
K_exp = np.exp(K1)
print(f'exp(k1) PSD: {is_psd(K_exp)}')

# Rule 5: f(x)*k(x,z)*f(z) weighting
w = np.abs(rng.randn(25)) + 0.1
K_weighted = np.outer(w, w) * K1
print(f'w(x)*k1*w(z) PSD: {is_psd(K_weighted)}')
```

All composition rules preserve the PSD property. The product rule uses elementwise multiplication of the Gram matrices, which corresponds to the tensor product of feature maps. The exp rule creates an infinite series of interactions — the resulting kernel is even more expressive than the original.

```python
import numpy as np
from scipy.optimize import minimize

def ard_kernel(X1, X2, length_scales, sigma2=1.0):
    # ARD RBF: per-dimension length scales
    diff = X1[:, None, :] - X2[None, :, :]
    scaled = diff / length_scales[None, None, :]
    return sigma2 * np.exp(-0.5 * np.sum(scaled**2, axis=-1))

def neg_log_marginal_likelihood(log_params, X, y, noise=1e-3):
    d = X.shape[1]
    ell = np.exp(log_params[:d])
    sigma2 = np.exp(log_params[d])
    K = ard_kernel(X, X, ell, sigma2) + noise * np.eye(len(X))
    try:
        L = np.linalg.cholesky(K)
    except np.linalg.LinAlgError:
        return 1e10
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, y))
    log_det = 2 * np.sum(np.log(np.diag(L)))
    return 0.5 * (y @ alpha + log_det + len(y) * np.log(2 * np.pi))

rng = np.random.RandomState(1)
X = rng.randn(60, 4)
# Only dims 0 and 2 are relevant
y = 2 * X[:, 0] + 0.5 * X[:, 2] + rng.randn(60) * 0.1

x0 = np.zeros(5)  # 4 length-scales + 1 variance
result = minimize(neg_log_marginal_likelihood, x0, args=(X, y), method='L-BFGS-B')
learned_ell = np.exp(result.x[:4])
print(f'Learned length-scales: {learned_ell.round(3)}')
print('Small ell = relevant feature; large ell = irrelevant feature')
```

```python
import numpy as np

def rbf_1d(x1, x2, ell=1.0):
    diff = np.subtract.outer(x1, x2)
    return np.exp(-diff**2 / (2 * ell**2))

def additive_kernel(X1, X2, ells=None):
    # Additive: sum of 1D RBF kernels over each dimension
    d = X1.shape[1]
    if ells is None:
        ells = np.ones(d)
    K = np.zeros((len(X1), len(X2)))
    for j in range(d):
        K += rbf_1d(X1[:, j], X2[:, j], ells[j])
    return K

rng = np.random.RandomState(42)
X_train = rng.randn(50, 3)
# Additive ground truth: sin(x0) + x1^2 + 0.5*x2
y_train = np.sin(X_train[:, 0]) + X_train[:, 1]**2 + 0.5 * X_train[:, 2]

lam = 0.01
K = additive_kernel(X_train, X_train) + lam * np.eye(50)
alpha = np.linalg.solve(K, y_train)

X_test = rng.randn(20, 3)
K_star = additive_kernel(X_test, X_train)
y_pred = K_star @ alpha
y_true = np.sin(X_test[:, 0]) + X_test[:, 1]**2 + 0.5 * X_test[:, 2]
r2 = 1 - np.var(y_true - y_pred) / np.var(y_true)
print(f'Additive kernel ridge regression R2: {r2:.4f}')
print('k(x,z) = sum_j k_j(x_j, z_j) decomposes into interpretable 1D terms')
```

```python
import numpy as np
from sklearn.metrics import r2_score

def spectral_mixture_kernel_1d(x1, x2, weights, means, variances):
    # Spectral mixture kernel (Wilson & Adams, 2013)
    # k(tau) = sum_q w_q exp(-2pi^2 tau^2 v_q) cos(2pi tau mu_q)
    tau = np.subtract.outer(x1, x2)
    K = np.zeros_like(tau, dtype=float)
    for w, mu, v in zip(weights, means, variances):
        K += w * np.exp(-2 * np.pi**2 * tau**2 * v) * np.cos(2 * np.pi * tau * mu)
    return K

# Signal with two periodic components
rng = np.random.RandomState(7)
x = np.linspace(0, 10, 200)
y = np.sin(2 * np.pi * x / 3) + 0.5 * np.sin(2 * np.pi * x / 1.5) + rng.randn(200) * 0.05

# Three-component spectral mixture
K = spectral_mixture_kernel_1d(
    x, x,
    weights=[1.0, 0.5, 0.3],
    means=[1/3, 2/3, 1.0],
    variances=[0.01, 0.01, 0.01]
)
K += 1e-6 * np.eye(len(x))
alpha = np.linalg.solve(K, y)
y_pred = K @ alpha
print(f'Spectral mixture kernel fit R2: {r2_score(y, y_pred):.4f}')
print('Spectral mixture kernels learn periodic structure automatically from data.')
```

## Composition Rules Reference

| Composition Rule | New Kernel Expression | RKHS / Feature Space | Practical Use Case |
| --- | --- | --- | --- |
| Sum k₁+k₂ | k(x,z) = k₁(x,z) + k₂(x,z) | Direct sum H₁ ⊕ H₂ | Combining RBF trend + periodic seasonality |
| Product k₁·k₂ | k(x,z) = k₁(x,z) × k₂(x,z) | Tensor product H₁ ⊗ H₂ | Localized periodic: RBF × periodic |
| Scalar c·k (c>0) | k(x,z) = c · k₁(x,z) | Rescaled H₁ | Adjusting signal variance amplitude |
| Exponentiation exp(k) | k(x,z) = exp(k₁(x,z)) | All tensor powers of H₁ | Nonlinear feature enhancement |
| ARD kernel | k(x,z) = exp(−Σᵢ(xᵢ−zᵢ)²/2ℓᵢ²) | Anisotropic RBF feature space | Automatic feature selection via ℓᵢ → ∞ |
| Additive Σₗ kₗ | k(x,z) = Σₗ kₗ(xₗ, zₗ) | Sum of 1D feature spaces | Interpretable decomposition by feature |

Kernel composition is the primary tool for encoding domain knowledge into kernel methods and GPs. By combining base kernels with these rules, you can capture multi-scale structure, periodicity, additive decompositions, and feature interactions — all while guaranteeing the result is a valid Mercer kernel. The learned hyperparameters (length-scales, weights) provide interpretable measures of feature importance and signal structure.

