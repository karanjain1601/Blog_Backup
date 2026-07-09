---
title: "Acquisition Functions — EI, UCB, Thompson Sampling, and PI"
slug: "acquisition-functions"
description: "Acquisition functions balance exploration and exploitation in Bayesian optimization to select the next query point."
tags: ["bayesian-optimization", "gaussian-processes", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gQmF5ZXNpYW4gb3B0aW1pemF0aW9uIChCTyksIHRoZSBzdXJyb2dhdGUgbW9kZWwg4oCUIHR5cGljYWxseSBhIEdhdXNzaWFuIHByb2Nlc3Mg4oCUIHByb3ZpZGVzIGEgcG9zdGVyaW9yIGRpc3RyaWJ1dGlvbiBwKGZ8RCkgb3ZlciB0aGUgb2JqZWN0aXZlLiBBZnRlciBlYWNoIG9ic2VydmF0aW9uLCB0aGUgYWNxdWlzaXRpb24gZnVuY3Rpb24gzrEoeCkgbWFwcyB0aGUgR1AgcG9zdGVyaW9yICjOvCh4KSwgz4MoeCkpIHRvIGEgc2NhbGFyIHV0aWxpdHkgcXVhbnRpZnlpbmcgaG93IHZhbHVhYmxlIGl0IHdvdWxkIGJlIHRvIHF1ZXJ5IHggbmV4dC4gQk8gYWx0ZXJuYXRlcyBiZXR3ZWVuIGZpdHRpbmcgdGhlIEdQIGFuZCBtYXhpbWl6aW5nIM6xKHgpIG92ZXIgdGhlIHNlYXJjaCBzcGFjZSB0byBzZWxlY3QgdGhlIG5leHQgZXZhbHVhdGlvbiBwb2ludC4gVGhlIGNob2ljZSBvZiBhY3F1aXNpdGlvbiBmdW5jdGlvbiBkZXRlcm1pbmVzIHRoZSBleHBsb3JhdGlvbuKAk2V4cGxvaXRhdGlvbiB0cmFkZS1vZmYgYW5kIGRpcmVjdGx5IGNvbnRyb2xzIGNvbnZlcmdlbmNlIHNwZWVkIG9uIGV4cGVuc2l2ZSBibGFjay1ib3ggb2JqZWN0aXZlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaGF0IElzIGFuIEFjcXVpc2l0aW9uIEZ1bmN0aW9uPyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGV0IGYqID0gbWF4e2YoeOKCgSksIOKApiwgZih44oKZKX0gYmUgdGhlIGJlc3Qgb2JzZXJ2ZWQgdmFsdWUgYWZ0ZXIgbiBldmFsdWF0aW9ucy4gVGhlIGFjcXVpc2l0aW9uIGZ1bmN0aW9uIM6xIDogWCDihpIg4oSdIGFzc2lnbnMgYSBzY29yZSB0byBlYWNoIGNhbmRpZGF0ZSBwb2ludCB4LCBiYWxhbmNpbmcgZXhwbG9yYXRpb24gKHF1ZXJ5aW5nIHJlZ2lvbnMgd2l0aCBoaWdoIHVuY2VydGFpbnR5IM+DKHgpKSBhbmQgZXhwbG9pdGF0aW9uIChxdWVyeWluZyByZWdpb25zIHdpdGggaGlnaCBwcmVkaWN0ZWQgdmFsdWUgzrwoeCkpLiBUaGUgbmV4dCBxdWVyeSBpcyB4X3tuKzF9ID0gYXJnbWF4X3t44oiIWH0gzrEoeCkuIFNpbmNlIM6xIGludm9sdmVzIG9ubHkgR1AgcHJlZGljdGlvbnMg4oCUIG5vdCB0aGUgZXhwZW5zaXZlIHRydWUgb2JqZWN0aXZlIGYg4oCUIG1heGltaXppbmcgzrEgaXMgY2hlYXAgcmVsYXRpdmUgdG8gZXZhbHVhdGluZyBmLiBUaGUgaW5uZXIgb3B0aW1pemF0aW9uIG92ZXIgzrEgaXMgdHlwaWNhbGx5IHNvbHZlZCB2aWEgbXVsdGktc3RhcnQgZ3JhZGllbnQgZGVzY2VudCwgTC1CRkdTLUIsIG9yIGV2b2x1dGlvbmFyeSBzdHJhdGVnaWVzIG92ZXIgYSBkZW5zZSBjYW5kaWRhdGUgZ3JpZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFeHBlY3RlZCBJbXByb3ZlbWVudCAoRUkpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFeHBlY3RlZCBJbXByb3ZlbWVudCAoRUkpIGlzIHRoZSBtb3N0IHdpZGVseSB1c2VkIGFjcXVpc2l0aW9uIGZ1bmN0aW9uLiBFSSBjb21wdXRlcyB0aGUgZXhwZWN0ZWQgZ2FpbiBvdmVyIHRoZSBjdXJyZW50IGJlc3QgZio6IEVJKHgpID0gRVttYXgoZih4KSDiiJIgZiosIDApXS4gVW5kZXIgYSBHUCBwb3N0ZXJpb3Igd2hlcmUgZih4KSB+IE4ozrwoeCksIM+DwrIoeCkpLCBFSSBoYXMgYSBjbG9zZWQtZm9ybSBleHByZXNzaW9uLiBEZWZpbmUgWiA9ICjOvCh4KSDiiJIgZiopIC8gz4MoeCkuIFRoZW4gRUkoeCkgPSAozrwoeCkg4oiSIGYqKc6mKFopICsgz4MoeCnPhihaKSwgd2hlcmUgzqYgaXMgdGhlIHN0YW5kYXJkIG5vcm1hbCBDREYgYW5kIM+GIGlzIHRoZSBQREYuIFRoZSBmaXJzdCB0ZXJtIHJld2FyZHMgZXhwbG9pdGF0aW9uIChoaWdoIM68KTsgdGhlIHNlY29uZCByZXdhcmRzIGV4cGxvcmF0aW9uIChoaWdoIM+DKS4gRUkgaXMgemVybyB3aGVuIM+DID0gMCAoa25vd24gbG9jYXRpb24pIGFuZCBwcm9wb3J0aW9uYWwgdG8gz4MgaW4gdW5jZXJ0YWluIHJlZ2lvbnMgZmFyIGZyb20gb2JzZXJ2YXRpb25zLiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50IjoiXFx0ZXh0e0VJfSh4KSA9IChcXG11KHgpIC0gZl4qKVxcLFxcUGhpKFopICsgXFxzaWdtYSh4KVxcLFxccGhpKFopLCBcXHF1YWQgWiA9IFxcZnJhY3tcXG11KHgpIC0gZl4qfXtcXHNpZ21hKHgpfSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBqaXR0ZXIgcGFyYW1ldGVyIM6+IOKJpSAwIHNoaWZ0cyBaIHRvICjOvCDiiJIgZiog4oiSIM6+KS/PgywgZW5jb3VyYWdpbmcgbW9yZSBleHBsb3JhdGlvbi4gRUkgaXMgZGlmZmVyZW50aWFibGUgaW4geCB0aHJvdWdoIM68IGFuZCDPgywgc28gZ3JhZGllbnQtYmFzZWQgaW5uZXItbG9vcCBvcHRpbWl6YXRpb24gd29ya3Mgd2VsbC4gVGhlIGNsb3NlZCBmb3JtIG1ha2VzIEVJIE8oMSkgdG8gZXZhbHVhdGUgcGVyIGNhbmRpZGF0ZSBhZnRlciBPKG7CsykgR1AgaW5mZXJlbmNlLiBFSSBoYXMgbm8gZnJlcXVlbnRpc3QgcmVncmV0IGd1YXJhbnRlZXMgYnV0IHBlcmZvcm1zIGV4Y2VsbGVudGx5IGluIHByYWN0aWNlIG9uIHNtb290aCBvYmplY3RpdmVzIGFuZCBpcyB0aGUgZGVmYXVsdCBjaG9pY2UgaW4gbW9zdCBCTyBsaWJyYXJpZXMgKEJvVG9yY2gsIEdQeU9wdCwgU3BlYXJtaW50KS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcm9iYWJpbGl0eSBvZiBJbXByb3ZlbWVudCBhbmQgVUNCIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcm9iYWJpbGl0eSBvZiBJbXByb3ZlbWVudCAoUEkpIGlzIHRoZSBzaW1wbGVzdCBhY3F1aXNpdGlvbiBmdW5jdGlvbjogUEkoeCkgPSBQKGYoeCkgXHUwMDNlIGYqKSA9IM6mKCjOvCh4KSDiiJIgZiopL8+DKHgpKS4gUEkgYXNrcyBvbmx5IHdoZXRoZXIgeCBpbXByb3ZlcyBvdmVyIGYqLCBpZ25vcmluZyB0aGUgbWFnbml0dWRlLiBUaGlzIG1ha2VzIFBJIGdyZWVkeSDigJQgaXQgcHJlZmVycyBhIHBvaW50IHdpdGggYSA1MSUgY2hhbmNlIG9mIGEgdGlueSBpbXByb3ZlbWVudCBvdmVyIG9uZSB3aXRoIGEgNDAlIGNoYW5jZSBvZiBhIGxhcmdlIGdhaW4uIFBJIGNhbiBzdGFsbCBpbiBsb2NhbCBleHBsb2l0YXRpb24gbG9vcHMuIEluIHByYWN0aWNlIFBJIGlzIHJhcmVseSBwcmVmZXJyZWQgb3ZlciBFSSB1bmxlc3MgY29tcHV0YXRpb25hbCBidWRnZXQgaXMgZXh0cmVtZWx5IHRpZ2h0IGFuZCB0aGUgb3ZlcmhlYWQgb2YgdGhlIENERitQREYgY29tcHV0YXRpb24gbWF0dGVycy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVwcGVyIENvbmZpZGVuY2UgQm91bmQgKFVDQikgYXZvaWRzIHRoZSBDREYgZW50aXJlbHk6IFVDQih4KSA9IM68KHgpICsgzrrPgyh4KS4gVGhlIHBhcmFtZXRlciDOuiDiiaUgMCBjb250cm9scyBleHBsb3JhdGlvbjogzrogPSAwIGlzIHB1cmUgZXhwbG9pdGF0aW9uLCDOuiDihpIg4oieIGlzIHB1cmUgZXhwbG9yYXRpb24uIFVDQiBoYXMgdGhlb3JldGljYWwgc3VibGluZWFyIHJlZ3JldCBib3VuZHMgdmlhIHRoZSBHUC1VQ0IgZnJhbWV3b3JrIChTcmluaXZhcyBldCBhbC4sIDIwMTApOiB3aXRoIM66IGNob3NlbiBhcyBzcXJ0KDIgbG9nKHxYfCB0wrIgz4DCsiAvIDbOtCkpLCBjdW11bGF0aXZlIHJlZ3JldCBSX1QgPSBPKHNxcnQoVCDOs19UIGxvZyBUL860KSkgd2hlcmUgzrNfVCBpcyB0aGUgbWF4aW11bSBpbmZvcm1hdGlvbiBnYWluIG9mIHRoZSBrZXJuZWwuIFRoaXMgbWFrZXMgVUNCIHRoZSBtb3N0IHRoZW9yZXRpY2FsbHkganVzdGlmaWVkIGFjcXVpc2l0aW9uIGZ1bmN0aW9uIGZvciBkaXNjcmV0ZSBzZWFyY2ggc3BhY2VzIHdpdGggUkJGIG9yIE1hdMOpcm4ga2VybmVscy4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6IlxcdGV4dHtQSX0oeCkgPSBcXFBoaVxcIVxcbGVmdChcXGZyYWN7XFxtdSh4KS1mXip9e1xcc2lnbWEoeCl9XFxyaWdodCksIFxccXF1YWQgXFx0ZXh0e1VDQn0oeCkgPSBcXG11KHgpICsgXFxrYXBwYVxcLFxcc2lnbWEoeCkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQ2hvb3NpbmcgzrogZm9yIFVDQiIsImNvbnRlbnQiOiJBIHByYWN0aWNhbCBkZWZhdWx0IGlzIM66ID0gMi4wLCBjb3JyZXNwb25kaW5nIHJvdWdobHkgdG8gYSA5NSUgY29uZmlkZW5jZSB1cHBlciBib3VuZC4gRm9yIGhpZ2gtZGltZW5zaW9uYWwgc3BhY2VzIG9yIG5vaXN5IG9iamVjdGl2ZXMsIGluY3JlYXNlIM66IChtb3JlIGV4cGxvcmF0aW9uKS4gQW5uZWFsIM66IGZyb20gYSBsYXJnZSB2YWx1ZSAoZS5nLiwgNS4wKSBkb3duIHRvIDAuMiBvdmVyIHRoZSBvcHRpbWl6YXRpb24gYnVkZ2V0IHRvIHNoaWZ0IGZyb20gZXhwbG9yYXRpb24gZWFybHkgb24gdG8gZXhwbG9pdGF0aW9uIGxhdGUg4oCUIHRoaXMgzrotYW5uZWFsaW5nIHN0cmF0ZWd5IG9mdGVuIG91dHBlcmZvcm1zIGEgZml4ZWQgzrogaW4gcHJhY3RpY2Ugd2l0aG91dCByZXF1aXJpbmcgdGhlIHRoZW9yZXRpY2FsbHkgcHJlc2NyaWJlZCBzY2hlZHVsZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaG9tcHNvbiBTYW1wbGluZyBhbmQgRW50cm9weSBTZWFyY2gifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRob21wc29uIFNhbXBsaW5nIChUUykgdGFrZXMgYSBmdWxseSBCYXllc2lhbiBhcHByb2FjaDogc2FtcGxlIGEgZnVuY3Rpb24gZsyDIGZyb20gdGhlIEdQIHBvc3RlcmlvciwgdGhlbiBjaG9vc2UgeF97bisxfSA9IGFyZ21heCBmzIMoeCkuIFByYWN0aWNhbGx5LCBzYW1wbGUgZsyDIGF0IGEgZmluaXRlIGNhbmRpZGF0ZSBncmlkIGJ5IGRyYXdpbmcgZnJvbSB0aGUgam9pbnQgbXVsdGl2YXJpYXRlIG5vcm1hbCBmzIMgfiBOKM68LCDOoykuIFRTIG5hdHVyYWxseSBleHBsb3JlcyBiZWNhdXNlIHVuY2VydGFpbiByZWdpb25zIGhhdmUgd2lkZSBwb3N0ZXJpb3JzLCBhbmQgc2FtcGxlcyBmcm9tIHRob3NlIHJlZ2lvbnMgY2FuIHRha2UgaGlnaCB2YWx1ZXMuIFRTIGlzIGVtYmFycmFzc2luZ2x5IHBhcmFsbGVsaXphYmxlIOKAlCBkcmF3IEIgaW5kZXBlbmRlbnQgc2FtcGxlcyBhbmQgcXVlcnkgYWxsIEIgYXJnbWF4ZXMgc2ltdWx0YW5lb3VzbHksIGdpdmluZyBhIG5hdHVyYWwgYmF0Y2ggQk8gc3RyYXRlZ3kuIEVudHJvcHkgU2VhcmNoIChFUykgc2VsZWN0cyB4IHRvIG1heGltaXplIHRoZSBleHBlY3RlZCByZWR1Y3Rpb24gaW4gZW50cm9weSBhYm91dCB0aGUgbG9jYXRpb24gb2YgdGhlIGdsb2JhbCBvcHRpbXVtIHgqID0gYXJnbWF4IGYoeCkuIEVTIGlzIHRoZSBtb3N0IHByaW5jaXBsZWQgYWNxdWlzaXRpb24gYnV0IHJlcXVpcmVzIGFwcHJveGltYXRpbmcgYSBkaXN0cmlidXRpb24gb3ZlciB4KiB2aWEgZXhwZWN0YXRpb24gcHJvcGFnYXRpb24gb3IgTW9udGUgQ2FybG8sIG1ha2luZyBpdCBzaWduaWZpY2FudGx5IG1vcmUgZXhwZW5zaXZlIHBlciBpdGVyYXRpb24gdGhhbiBFSSBvciBVQ0IuIFByZWRpY3RpdmUgRW50cm9weSBTZWFyY2ggKFBFUykgb2ZmZXJzIGEgbW9yZSB0cmFjdGFibGUgYXBwcm94aW1hdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQb3J0Zm9saW8gU3RyYXRlZ3kgYW5kIE5vaXN5IEVJIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJObyBzaW5nbGUgYWNxdWlzaXRpb24gZnVuY3Rpb24gZG9taW5hdGVzIGFsbCBwcm9ibGVtIGNsYXNzZXMuIFRoZSBwb3J0Zm9saW8gKGhlZGdlKSBzdHJhdGVneSBtYWludGFpbnMgbXVsdGlwbGUgYWNxdWlzaXRpb25zIOKAlCBFSSwgUEksIFVDQiwgVFMg4oCUIGFuZCBhbGxvY2F0ZXMgY3JlZGl0IHRvIGVhY2ggdXNpbmcgYSBiYW5kaXQgYWxnb3JpdGhtIChlLmcuLCBFeHAzIG9yIFVDQjEgb3ZlciBhY3F1aXNpdGlvbnMpLiBBdCBlYWNoIGl0ZXJhdGlvbiB0aGUgaGVkZ2Ugc2VsZWN0cyBwcm9wb3J0aW9uYWxseSB0byBoaXN0b3JpY2FsIGdhaW5zLCBjb25jZW50cmF0aW5nIG1hc3Mgb24gd2hpY2hldmVyIGFjcXVpc2l0aW9uIGhhcyBwZXJmb3JtZWQgYmVzdCBzbyBmYXIuIEZvciBub2lzeSBvYmplY3RpdmVzIChvYnNlcnZhdGlvbiBub2lzZSDPg19ub2lzZSBcdTAwM2UgMCksIHN0YW5kYXJkIEVJIGlzIG92ZXJvcHRpbWlzdGljIGJlY2F1c2UgZiogaXMgYSBub2lzeSBtYXhpbXVtIHRoYXQgbWF5IGJlIGEgbm9pc2UgYXJ0aWZhY3QuIE5vaXN5IEVJIHJlcGxhY2VzIGYqIHdpdGggdGhlIHByZWRpY3RlZCB2YWx1ZSBhdCB0aGUgYmVzdCBvYnNlcnZlZCBwb2ludDogZipfbm9pc3kgPSDOvCh4X3tiZXN0fSksIGFuZCB1c2VzIHRoZSBmdWxsIG5vaXN5IHByZWRpY3RpdmUgdmFyaWFuY2UuIFRoaXMgcHJldmVudHMgb3Zlci1leHBsb2l0YXRpb24gb2Ygc3B1cmlvdXMgbWF4aW1hIGluIHRoZSB0cmFpbmluZyBkYXRhLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgRXhhbXBsZXMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBub3JtXG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgZWxsPTEuMCk6XG4gICAgZDIgPSBucC5zdW0oKFgxWzosIE5vbmVdIC0gWDJbTm9uZSwgOl0pKioyLCBheGlzPS0xKVxuICAgIHJldHVybiBucC5leHAoLWQyIC8gKDIgKiBlbGwqKjIpKVxuXG5kZWYgZ3BfcG9zdGVyaW9yKFhfdHIsIHlfdHIsIFhfdGUsIG5vaXNlPTFlLTQpOlxuICAgIEsgPSByYmZfa2VybmVsKFhfdHIsIFhfdHIpICsgbm9pc2UgKiBucC5leWUobGVuKFhfdHIpKVxuICAgIEtzLCBLc3MgPSByYmZfa2VybmVsKFhfdHIsIFhfdGUpLCByYmZfa2VybmVsKFhfdGUsIFhfdGUpXG4gICAgTCA9IG5wLmxpbmFsZy5jaG9sZXNreShLKVxuICAgIGFscGhhID0gbnAubGluYWxnLnNvbHZlKEwuVCwgbnAubGluYWxnLnNvbHZlKEwsIHlfdHIpKVxuICAgIHYgPSBucC5saW5hbGcuc29sdmUoTCwgS3MpXG4gICAgcmV0dXJuIEtzLlQgQCBhbHBoYSwgbnAuZGlhZyhLc3MgLSB2LlQgQCB2KVxuXG5kZWYgYWNxX2VpKG11LCBzaWcsIGZfYmVzdCwgeGk9MC4wMSk6XG4gICAgWiA9IChtdSAtIGZfYmVzdCAtIHhpKSAvIChzaWcgKyAxZS05KVxuICAgIHJldHVybiAobXUgLSBmX2Jlc3QgLSB4aSkgKiBub3JtLmNkZihaKSArIHNpZyAqIG5vcm0ucGRmKFopXG5cbmRlZiBhY3FfcGkobXUsIHNpZywgZl9iZXN0LCB4aT0wLjAxKTpcbiAgICByZXR1cm4gbm9ybS5jZGYoKG11IC0gZl9iZXN0IC0geGkpIC8gKHNpZyArIDFlLTkpKVxuXG5kZWYgYWNxX3VjYihtdSwgc2lnLCBrYXBwYT0yLjApOiByZXR1cm4gbXUgKyBrYXBwYSAqIHNpZ1xuZGVmIGFjcV90cyhtdSwgdmFyLCBzZWVkPTQyKTogcmV0dXJuIG5wLnJhbmRvbS5SYW5kb21TdGF0ZShzZWVkKS5ub3JtYWwobXUsIG5wLnNxcnQobnAubWF4aW11bSh2YXIsIDApKSlcblxuWF90ciA9IG5wLmFycmF5KFtbLTIuNV0sIFstMS4wXSwgWzAuM10sIFsxLjhdLCBbMi45XV0pXG55X3RyID0gbnAuc2luKFhfdHIucmF2ZWwoKSk7IGZfYmVzdCA9IHlfdHIubWF4KClcblhfdGUgPSBucC5saW5zcGFjZSgtMywgMywgMjAwKVs6LCBOb25lXVxubXUsIHZhciA9IGdwX3Bvc3RlcmlvcihYX3RyLCB5X3RyLCBYX3RlKVxuc2lnID0gbnAuc3FydChucC5tYXhpbXVtKHZhciwgMCkpXG5hY3FzID0ge1x1MDAyN0VJXHUwMDI3OiBhY3FfZWkobXUsIHNpZywgZl9iZXN0KSwgXHUwMDI3UElcdTAwMjc6IGFjcV9waShtdSwgc2lnLCBmX2Jlc3QpLFxuICAgICAgICBcdTAwMjdVQ0JcdTAwMjc6IGFjcV91Y2IobXUsIHNpZyksIFx1MDAyN1RTXHUwMDI3OiBhY3FfdHMobXUsIHZhcil9XG5mb3IgbmFtZSwgYSBpbiBhY3FzLml0ZW1zKCk6XG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lfTogbmV4dCB4ID0ge1hfdGVbYS5hcmdtYXgoKSwgMF06LjNmfSwgYWNxX21heCA9IHthLm1heCgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybVxuXG5kZWYgcmJmX2tlcm5lbChYMSwgWDIsIGVsbD0xLjApOlxuICAgIGQyID0gbnAuc3VtKChYMVs6LCBOb25lXSAtIFgyW05vbmUsIDpdKSoqMiwgYXhpcz0tMSlcbiAgICByZXR1cm4gbnAuZXhwKC1kMiAvICgyICogZWxsKioyKSlcblxuZGVmIGdwX3Bvc3RlcmlvcihYX3RyLCB5X3RyLCBYX3RlLCBub2lzZT0xZS00KTpcbiAgICBLID0gcmJmX2tlcm5lbChYX3RyLCBYX3RyKSArIG5vaXNlICogbnAuZXllKGxlbihYX3RyKSlcbiAgICBLcywgS3NzID0gcmJmX2tlcm5lbChYX3RyLCBYX3RlKSwgcmJmX2tlcm5lbChYX3RlLCBYX3RlKVxuICAgIEwgPSBucC5saW5hbGcuY2hvbGVza3koSylcbiAgICB2ID0gbnAubGluYWxnLnNvbHZlKEwsIEtzKVxuICAgIHJldHVybiBLcy5UIEAgbnAubGluYWxnLnNvbHZlKEwuVCwgbnAubGluYWxnLnNvbHZlKEwsIHlfdHIpKSwgbnAuZGlhZyhLc3MgLSB2LlQgQCB2KVxuXG5YX3RyID0gbnAuYXJyYXkoW1stMi41XSwgWy0xLjBdLCBbMC4zXSwgWzEuOF0sIFsyLjldXSlcbnlfdHIgPSBucC5zaW4oWF90ci5yYXZlbCgpKVxuWF90ZSA9IG5wLmxpbnNwYWNlKC0zLCAzLCAzMDApWzosIE5vbmVdOyB4ID0gWF90ZS5yYXZlbCgpXG5tdSwgdmFyID0gZ3BfcG9zdGVyaW9yKFhfdHIsIHlfdHIsIFhfdGUpXG5zaWcgPSBucC5zcXJ0KG5wLm1heGltdW0odmFyLCAwKSk7IGZfYmVzdCA9IHlfdHIubWF4KCk7IHhpID0gMC4wMVxuWiA9IChtdSAtIGZfYmVzdCAtIHhpKSAvIChzaWcgKyAxZS05KVxuYWNxcyA9IHtcdTAwMjdFSVx1MDAyNzogKG11LWZfYmVzdC14aSkqbm9ybS5jZGYoWikrc2lnKm5vcm0ucGRmKFopLFxuICAgICAgICBcdTAwMjdQSVx1MDAyNzogbm9ybS5jZGYoWiksIFx1MDAyN1VDQiAoaz0yKVx1MDAyNzogbXUrMipzaWcsXG4gICAgICAgIFx1MDAyN1Rob21wc29uXHUwMDI3OiBucC5yYW5kb20uUmFuZG9tU3RhdGUoMCkubm9ybWFsKG11LCBzaWcpfVxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDIsIDIsIGZpZ3NpemU9KDEyLCA4KSlcbmZvciBheCwgKG5hbWUsIGEpIGluIHppcChheGVzLmZsYXQsIGFjcXMuaXRlbXMoKSk6XG4gICAgYXguZmlsbF9iZXR3ZWVuKHgsIG11LTIqc2lnLCBtdSsyKnNpZywgYWxwaGE9MC4yLCBsYWJlbD1cdTAwMjc5NSUgQ0lcdTAwMjcpXG4gICAgYXgucGxvdCh4LCBtdSwgXHUwMDI3Yi1cdTAwMjcsIGx3PTEuNSk7IGF4LnNjYXR0ZXIoWF90ciwgeV90ciwgYz1cdTAwMjdrXHUwMDI3LCB6b3JkZXI9NSlcbiAgICBheDIgPSBheC50d2lueCgpOyBheDIucGxvdCh4LCBhLCBcdTAwMjdyLS1cdTAwMjcsIGx3PTEuNSlcbiAgICBheDIuYXh2bGluZSh4W2EuYXJnbWF4KCldLCBjb2xvcj1cdTAwMjdyXHUwMDI3LCBscz1cdTAwMjc6XHUwMDI3LCBsYWJlbD1mXHUwMDI3bmV4dCB4PXt4W2EuYXJnbWF4KCldOi4yZn1cdTAwMjcpXG4gICAgYXguc2V0X3RpdGxlKG5hbWUpOyBheDIuc2V0X3lsYWJlbChcdTAwMjdBY3F1aXNpdGlvbiB2YWx1ZVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNhdmVmaWcoXHUwMDI3YWNxdWlzaXRpb25fdml6LnBuZ1x1MDAyNywgZHBpPTEwMClcbnByaW50KFx1MDAyN1NhdmVkIGFjcXVpc2l0aW9uX3Zpei5wbmcgLS0gNC1wYW5lbCBjb21wYXJpc29uIG9mIEVJLCBQSSwgVUNCLCBUaG9tcHNvblx1MDAyNykifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBub3JtXG5cbmRlZiBicmFuaW4oeCk6XG4gICAgeDEsIHgyID0geFswXSoxNSAtIDUsIHhbMV0qMTVcbiAgICByZXR1cm4gKHgyIC0gNS4xKngxKioyLyg0Km5wLnBpKioyKSArIDUqeDEvbnAucGkgLSA2KSoqMiArIDEwKigxLTEvKDgqbnAucGkpKSpucC5jb3MoeDEpKzEwXG5cbmRlZiByYmZfayhYMSwgWDIsIGVsbD0wLjUpOlxuICAgIHJldHVybiBucC5leHAoLW5wLnN1bSgoWDFbOixOb25lXS1YMltOb25lLDpdKSoqMiwgYXhpcz0tMSkvKDIqZWxsKioyKSlcblxuZGVmIGdwX3Bvc3QoWHRyLCB5dHIsIFh0ZSwgbm9pc2U9MC4xKTpcbiAgICBLID0gcmJmX2soWHRyLFh0cikrbm9pc2UqbnAuZXllKGxlbihYdHIpKTsgS3M9cmJmX2soWHRyLFh0ZSlcbiAgICBMPW5wLmxpbmFsZy5jaG9sZXNreShLKTsgdj1ucC5saW5hbGcuc29sdmUoTCxLcylcbiAgICBhbHBoYT1ucC5saW5hbGcuc29sdmUoTC5ULG5wLmxpbmFsZy5zb2x2ZShMLHl0cikpXG4gICAgcmV0dXJuIEtzLlRAYWxwaGEsIG5wLm1heGltdW0oMS1ucC5zdW0odioqMixheGlzPTApLDApXG5cbmRlZiBhY3FfZWkobXUsIHNpZywgZl9iZXN0KTpcbiAgICBaPShmX2Jlc3QtbXUpLyhzaWcrMWUtOSk7IHJldHVybiAoZl9iZXN0LW11KSpub3JtLmNkZihaKStzaWcqbm9ybS5wZGYoWilcblxucm5nPW5wLnJhbmRvbS5SYW5kb21TdGF0ZSgwKVxuWF9vYnM9cm5nLnVuaWZvcm0oMCwxLCg2LDIpKTsgeV9vYnM9bnAuYXJyYXkoW2JyYW5pbih4KSBmb3IgeCBpbiBYX29ic10pXG5jYW5kcz1ybmcudW5pZm9ybSgwLDEsKDQwMCwyKSlcbmJlc3RfZWk9W3lfb2JzLm1pbigpXTsgYmVzdF9yYW5kPVt5X29icy5taW4oKV1cbmZvciBfIGluIHJhbmdlKDIwKTpcbiAgICBtdSx2YXI9Z3BfcG9zdChYX29icywteV9vYnMsY2FuZHMpOyBzaWc9bnAuc3FydCh2YXIpXG4gICAgYng9Y2FuZHNbYWNxX2VpKG11LHNpZywteV9vYnMubWluKCkpLmFyZ21heCgpXVxuICAgIHlfbmV3PWJyYW5pbihieCk7IFhfb2JzPW5wLnZzdGFjayhbWF9vYnMsW2J4XV0pOyB5X29icz1ucC5hcHBlbmQoeV9vYnMseV9uZXcpXG4gICAgYmVzdF9laS5hcHBlbmQoeV9vYnMubWluKCkpOyBiZXN0X3JhbmQuYXBwZW5kKGJyYW5pbihybmcudW5pZm9ybSgwLDEsMikpKVxucmFuZF9iZXN0PW5wLm1pbmltdW0uYWNjdW11bGF0ZShiZXN0X3JhbmQpXG5wcmludChmXHUwMDI3RUkgYmVzdCBCcmFuaW4gICAgPSB7YmVzdF9laVstMV06LjNmfSAgKGdsb2JhbCBtaW4gYXBwcm94IDAuMzk3KVx1MDAyNylcbnByaW50KGZcdTAwMjdSYW5kb20gYmVzdCAgICAgICA9IHtyYW5kX2Jlc3RbLTFdOi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcmJmX2soWDEsIFgyLCBlbGw9MC44KTpcbiAgICByZXR1cm4gbnAuZXhwKC1ucC5zdW0oKFgxWzosTm9uZV0tWDJbTm9uZSw6XSkqKjIsIGF4aXM9LTEpLygyKmVsbCoqMikpXG5cbmRlZiBncF9wb3N0KFh0ciwgeXRyLCBYdGUsIG5vaXNlPTAuMDUpOlxuICAgIEs9cmJmX2soWHRyLFh0cikrbm9pc2UqbnAuZXllKGxlbihYdHIpKTsgS3M9cmJmX2soWHRyLFh0ZSlcbiAgICBMPW5wLmxpbmFsZy5jaG9sZXNreShLKTsgdj1ucC5saW5hbGcuc29sdmUoTCxLcylcbiAgICBhbHBoYT1ucC5saW5hbGcuc29sdmUoTC5ULG5wLmxpbmFsZy5zb2x2ZShMLHl0cikpXG4gICAgcmV0dXJuIEtzLlRAYWxwaGEsIG5wLm1heGltdW0oMS1ucC5zdW0odioqMixheGlzPTApLDApXG5cbmRlZiBrYXBwYV9hbm5lYWwodCwgVCwga19tYXg9NS4wLCBrX21pbj0wLjIpOlxuICAgIHJldHVybiBrX21heCAqIChrX21pbi9rX21heCkqKih0L21heChULTEsMSkpXG5cbnJuZz1ucC5yYW5kb20uUmFuZG9tU3RhdGUoMSlcbmZfdHJ1ZSA9IGxhbWJkYSB4OiBmbG9hdChucC5zaW4oMyp4KSpucC5leHAoLTAuNSp4KSlcblhfb2JzPXJuZy51bmlmb3JtKC0zLDMsKDQsMSkpOyB5X29icz1ucC5hcnJheShbZl90cnVlKHhbMF0pIGZvciB4IGluIFhfb2JzXSlcblhfdGU9bnAubGluc3BhY2UoLTMsMywyMDApWzosTm9uZV07IFQ9MjA7IGthcHBhcz1bXTsgYmVzdHM9W11cbmZvciB0IGluIHJhbmdlKFQpOlxuICAgIGthcHBhPWthcHBhX2FubmVhbCh0LFQpOyBrYXBwYXMuYXBwZW5kKGthcHBhKVxuICAgIG11LHZhcj1ncF9wb3N0KFhfb2JzLHlfb2JzLFhfdGUpXG4gICAgdWNiPW11K2thcHBhKm5wLnNxcnQodmFyKTsgbmV4dF94PVhfdGVbW3VjYi5hcmdtYXgoKV1dXG4gICAgeV9uZXc9Zl90cnVlKG5leHRfeFswLDBdKVxuICAgIFhfb2JzPW5wLnZzdGFjayhbWF9vYnMsbmV4dF94XSk7IHlfb2JzPW5wLmFwcGVuZCh5X29icyx5X25ldyk7IGJlc3RzLmFwcGVuZCh5X29icy5tYXgoKSlcbnByaW50KGZcdTAwMjdVQ0Iga2FwcGEtYW5uZWFsaW5nIG92ZXIge1R9IHN0ZXBzLCBmaW5hbCBiZXN0ID0ge2Jlc3RzWy0xXTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0thcHBhIHNjaGVkdWxlOiB7a2FwcGFzWzBdOi4yZn0gKGV4cGxvcmUpIC1cdTAwM2Uge2thcHBhc1stMV06LjJmfSAoZXhwbG9pdClcdTAwMjcpXG5mb3IgaSBpbiByYW5nZSgwLCBULCA1KTpcbiAgICBwcmludChmXHUwMDI3ICBpdGVyIHtpOjJkfToga2FwcGE9e2thcHBhc1tpXTouMmZ9LCBiZXN0X3NvX2Zhcj17YmVzdHNbaV06LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBY3F1aXNpdGlvbiBGdW5jdGlvbiBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFjcXVpc2l0aW9uIiwiRm9ybXVsYSIsIkV4cGxvcmF0aW9uIiwiQ2xvc2VkIEZvcm0iLCJSZWdyZXQgQm91bmQiLCJDb3N0Il0sInJvd3MiOltbIkVJIiwiKM684oiSZiopzqYoWikrz4PPhihaKSwgWj0ozrziiJJmKikvz4MiLCJNb2RlcmF0ZSAodmlhIM+Dz4YoWikgdGVybSkiLCJZZXMiLCJOb25lIHByb3ZlbiIsIk8obsKzKSBHUCArIE8oMSkgZXZhbCJdLFsiUEkiLCLOpigozrziiJJmKikvz4MpIiwiTG93IChpZ25vcmVzIGltcHJvdmVtZW50IG1hZ25pdHVkZSkiLCJZZXMiLCJOb25lIHByb3ZlbiIsIk8obsKzKSBHUCArIE8oMSkgZXZhbCJdLFsiVUNCIiwizrwoeCkrzrrPgyh4KSIsIkhpZ2ggKM66IHNjYWxlcyBleHBsb3JhdGlvbikiLCJZZXMiLCJTdWJsaW5lYXIgKEdQLVVDQikiLCJPKG7CsykgR1AgKyBPKDEpIGV2YWwiXSxbIlRob21wc29uIFNhbXBsaW5nIiwiYXJnbWF4IG9mIEdQIHBvc3RlcmlvciBzYW1wbGUiLCJOYXR1cmFsIChwb3N0ZXJpb3Igc3ByZWFkKSIsIk5vIChzYW1wbGluZyByZXF1aXJlZCkiLCJOb25lIHByb3ZlbiIsIk8obsKzKSBHUCArIE8obsKyKSBzYW1wbGUiXSxbIkVudHJvcHkgU2VhcmNoIiwibWF4IGluZm9ybWF0aW9uIGdhaW4gYWJvdXQgeCoiLCJQcmluY2lwbGVkIGdsb2JhbCBleHBsb3JhdGlvbiIsIk5vIChFUC9NQyBhcHByb3gpIiwiTm9uZSBpbiBwcmFjdGljZSIsIk8obsKzKSBHUCArIE8oaGVhdnkgYXBwcm94KSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFSSBpcyB0aGUgcHJhY3RpY2FsIGRlZmF1bHQ6IGNsb3NlZC1mb3JtLCBkaWZmZXJlbnRpYWJsZSwgd2VsbC1jYWxpYnJhdGVkIGV4cGxvcmF0aW9uLiBVQ0IgaXMgcHJlZmVycmVkIHdoZW4gdGhlb3JldGljYWwgZ3VhcmFudGVlcyBtYXR0ZXIgb3Igd2hlbiDOuiBjYW4gYmUgdHVuZWQgdmlhIHRoZSBHUC1VQ0Igc2NoZWR1bGUuIFRob21wc29uIFNhbXBsaW5nIHNoaW5lcyBpbiBwYXJhbGxlbCBiYXRjaCBzZXR0aW5ncyDigJQgZHJhdyBCIHNhbXBsZXMsIGV2YWx1YXRlIEIgY2FuZGlkYXRlcyBzaW11bHRhbmVvdXNseS4gRW50cm9weSBTZWFyY2ggaXMgcmVzZXJ2ZWQgZm9yIHByb2JsZW1zIHdoZXJlIHRoZSBidWRnZXQgaXMgdmVyeSBzbWFsbCAoc2luZ2xlLWRpZ2l0IGV2YWx1YXRpb25zKSBhbmQgbWF4aW1hbGx5IGluZm9ybWF0aXZlIHF1ZXJpZXMganVzdGlmeSB0aGUgb3ZlcmhlYWQuIEZvciBub2lzeSBvYmplY3RpdmVzLCByZXBsYWNlIEVJIHdpdGggTm9pc3kgRUkgdXNpbmcgzrwoeF97YmVzdH0pIGluIHBsYWNlIG9mIHRoZSByYXcgZiogbWF4aW11bS4gVGhlIHBvcnRmb2xpbyBoZWRnZSBzdHJhdGVneSBhdm9pZHMgY29tbWl0dGluZyB0byBhIHNpbmdsZSBhY3F1aXNpdGlvbiBhbmQgaXMgYSBzdHJvbmcgYmFzZWxpbmUgd2hlbiB0aGUgcHJvYmxlbSBjbGFzcyBpcyB1bmtub3duLiJ9XQ=="
---
# Acquisition Functions — EI, UCB, Thompson Sampling, and PI

In Bayesian optimization (BO), the surrogate model — typically a Gaussian process — provides a posterior distribution p(f|D) over the objective. After each observation, the acquisition function α(x) maps the GP posterior (μ(x), σ(x)) to a scalar utility quantifying how valuable it would be to query x next. BO alternates between fitting the GP and maximizing α(x) over the search space to select the next evaluation point. The choice of acquisition function determines the exploration–exploitation trade-off and directly controls convergence speed on expensive black-box objectives.

## What Is an Acquisition Function?

Let f* = max{f(x₁), …, f(xₙ)} be the best observed value after n evaluations. The acquisition function α : X → ℝ assigns a score to each candidate point x, balancing exploration (querying regions with high uncertainty σ(x)) and exploitation (querying regions with high predicted value μ(x)). The next query is x_{n+1} = argmax_{x∈X} α(x). Since α involves only GP predictions — not the expensive true objective f — maximizing α is cheap relative to evaluating f. The inner optimization over α is typically solved via multi-start gradient descent, L-BFGS-B, or evolutionary strategies over a dense candidate grid.

## Expected Improvement (EI)

Expected Improvement (EI) is the most widely used acquisition function. EI computes the expected gain over the current best f*: EI(x) = E[max(f(x) − f*, 0)]. Under a GP posterior where f(x) ~ N(μ(x), σ²(x)), EI has a closed-form expression. Define Z = (μ(x) − f*) / σ(x). Then EI(x) = (μ(x) − f*)Φ(Z) + σ(x)φ(Z), where Φ is the standard normal CDF and φ is the PDF. The first term rewards exploitation (high μ); the second rewards exploration (high σ). EI is zero when σ = 0 (known location) and proportional to σ in uncertain regions far from observations.

$$\text{EI}(x) = (\mu(x) - f^*)\,\Phi(Z) + \sigma(x)\,\phi(Z), \quad Z = \frac{\mu(x) - f^*}{\sigma(x)}$$

A jitter parameter ξ ≥ 0 shifts Z to (μ − f* − ξ)/σ, encouraging more exploration. EI is differentiable in x through μ and σ, so gradient-based inner-loop optimization works well. The closed form makes EI O(1) to evaluate per candidate after O(n³) GP inference. EI has no frequentist regret guarantees but performs excellently in practice on smooth objectives and is the default choice in most BO libraries (BoTorch, GPyOpt, Spearmint).

## Probability of Improvement and UCB

Probability of Improvement (PI) is the simplest acquisition function: PI(x) = P(f(x) > f*) = Φ((μ(x) − f*)/σ(x)). PI asks only whether x improves over f*, ignoring the magnitude. This makes PI greedy — it prefers a point with a 51% chance of a tiny improvement over one with a 40% chance of a large gain. PI can stall in local exploitation loops. In practice PI is rarely preferred over EI unless computational budget is extremely tight and the overhead of the CDF+PDF computation matters.

Upper Confidence Bound (UCB) avoids the CDF entirely: UCB(x) = μ(x) + κσ(x). The parameter κ ≥ 0 controls exploration: κ = 0 is pure exploitation, κ → ∞ is pure exploration. UCB has theoretical sublinear regret bounds via the GP-UCB framework (Srinivas et al., 2010): with κ chosen as sqrt(2 log(|X| t² π² / 6δ)), cumulative regret R_T = O(sqrt(T γ_T log T/δ)) where γ_T is the maximum information gain of the kernel. This makes UCB the most theoretically justified acquisition function for discrete search spaces with RBF or Matérn kernels.

$$\text{PI}(x) = \Phi\!\left(\frac{\mu(x)-f^*}{\sigma(x)}\right), \qquad \text{UCB}(x) = \mu(x) + \kappa\,\sigma(x)$$

> **Choosing κ for UCB**: A practical default is κ = 2.0, corresponding roughly to a 95% confidence upper bound. For high-dimensional spaces or noisy objectives, increase κ (more exploration). Anneal κ from a large value (e.g., 5.0) down to 0.2 over the optimization budget to shift from exploration early on to exploitation late — this κ-annealing strategy often outperforms a fixed κ in practice without requiring the theoretically prescribed schedule.

## Thompson Sampling and Entropy Search

Thompson Sampling (TS) takes a fully Bayesian approach: sample a function f̃ from the GP posterior, then choose x_{n+1} = argmax f̃(x). Practically, sample f̃ at a finite candidate grid by drawing from the joint multivariate normal f̃ ~ N(μ, Σ). TS naturally explores because uncertain regions have wide posteriors, and samples from those regions can take high values. TS is embarrassingly parallelizable — draw B independent samples and query all B argmaxes simultaneously, giving a natural batch BO strategy. Entropy Search (ES) selects x to maximize the expected reduction in entropy about the location of the global optimum x* = argmax f(x). ES is the most principled acquisition but requires approximating a distribution over x* via expectation propagation or Monte Carlo, making it significantly more expensive per iteration than EI or UCB. Predictive Entropy Search (PES) offers a more tractable approximation.

## Portfolio Strategy and Noisy EI

No single acquisition function dominates all problem classes. The portfolio (hedge) strategy maintains multiple acquisitions — EI, PI, UCB, TS — and allocates credit to each using a bandit algorithm (e.g., Exp3 or UCB1 over acquisitions). At each iteration the hedge selects proportionally to historical gains, concentrating mass on whichever acquisition has performed best so far. For noisy objectives (observation noise σ_noise > 0), standard EI is overoptimistic because f* is a noisy maximum that may be a noise artifact. Noisy EI replaces f* with the predicted value at the best observed point: f*_noisy = μ(x_{best}), and uses the full noisy predictive variance. This prevents over-exploitation of spurious maxima in the training data.

## Code Examples

```python
import numpy as np
from scipy.stats import norm

def rbf_kernel(X1, X2, ell=1.0):
    d2 = np.sum((X1[:, None] - X2[None, :])**2, axis=-1)
    return np.exp(-d2 / (2 * ell**2))

def gp_posterior(X_tr, y_tr, X_te, noise=1e-4):
    K = rbf_kernel(X_tr, X_tr) + noise * np.eye(len(X_tr))
    Ks, Kss = rbf_kernel(X_tr, X_te), rbf_kernel(X_te, X_te)
    L = np.linalg.cholesky(K)
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, y_tr))
    v = np.linalg.solve(L, Ks)
    return Ks.T @ alpha, np.diag(Kss - v.T @ v)

def acq_ei(mu, sig, f_best, xi=0.01):
    Z = (mu - f_best - xi) / (sig + 1e-9)
    return (mu - f_best - xi) * norm.cdf(Z) + sig * norm.pdf(Z)

def acq_pi(mu, sig, f_best, xi=0.01):
    return norm.cdf((mu - f_best - xi) / (sig + 1e-9))

def acq_ucb(mu, sig, kappa=2.0): return mu + kappa * sig
def acq_ts(mu, var, seed=42): return np.random.RandomState(seed).normal(mu, np.sqrt(np.maximum(var, 0)))

X_tr = np.array([[-2.5], [-1.0], [0.3], [1.8], [2.9]])
y_tr = np.sin(X_tr.ravel()); f_best = y_tr.max()
X_te = np.linspace(-3, 3, 200)[:, None]
mu, var = gp_posterior(X_tr, y_tr, X_te)
sig = np.sqrt(np.maximum(var, 0))
acqs = {'EI': acq_ei(mu, sig, f_best), 'PI': acq_pi(mu, sig, f_best),
        'UCB': acq_ucb(mu, sig), 'TS': acq_ts(mu, var)}
for name, a in acqs.items():
    print(f'{name}: next x = {X_te[a.argmax(), 0]:.3f}, acq_max = {a.max():.4f}')
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def rbf_kernel(X1, X2, ell=1.0):
    d2 = np.sum((X1[:, None] - X2[None, :])**2, axis=-1)
    return np.exp(-d2 / (2 * ell**2))

def gp_posterior(X_tr, y_tr, X_te, noise=1e-4):
    K = rbf_kernel(X_tr, X_tr) + noise * np.eye(len(X_tr))
    Ks, Kss = rbf_kernel(X_tr, X_te), rbf_kernel(X_te, X_te)
    L = np.linalg.cholesky(K)
    v = np.linalg.solve(L, Ks)
    return Ks.T @ np.linalg.solve(L.T, np.linalg.solve(L, y_tr)), np.diag(Kss - v.T @ v)

X_tr = np.array([[-2.5], [-1.0], [0.3], [1.8], [2.9]])
y_tr = np.sin(X_tr.ravel())
X_te = np.linspace(-3, 3, 300)[:, None]; x = X_te.ravel()
mu, var = gp_posterior(X_tr, y_tr, X_te)
sig = np.sqrt(np.maximum(var, 0)); f_best = y_tr.max(); xi = 0.01
Z = (mu - f_best - xi) / (sig + 1e-9)
acqs = {'EI': (mu-f_best-xi)*norm.cdf(Z)+sig*norm.pdf(Z),
        'PI': norm.cdf(Z), 'UCB (k=2)': mu+2*sig,
        'Thompson': np.random.RandomState(0).normal(mu, sig)}
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for ax, (name, a) in zip(axes.flat, acqs.items()):
    ax.fill_between(x, mu-2*sig, mu+2*sig, alpha=0.2, label='95% CI')
    ax.plot(x, mu, 'b-', lw=1.5); ax.scatter(X_tr, y_tr, c='k', zorder=5)
    ax2 = ax.twinx(); ax2.plot(x, a, 'r--', lw=1.5)
    ax2.axvline(x[a.argmax()], color='r', ls=':', label=f'next x={x[a.argmax()]:.2f}')
    ax.set_title(name); ax2.set_ylabel('Acquisition value')
plt.tight_layout(); plt.savefig('acquisition_viz.png', dpi=100)
print('Saved acquisition_viz.png -- 4-panel comparison of EI, PI, UCB, Thompson')
```

```python
import numpy as np
from scipy.stats import norm

def branin(x):
    x1, x2 = x[0]*15 - 5, x[1]*15
    return (x2 - 5.1*x1**2/(4*np.pi**2) + 5*x1/np.pi - 6)**2 + 10*(1-1/(8*np.pi))*np.cos(x1)+10

def rbf_k(X1, X2, ell=0.5):
    return np.exp(-np.sum((X1[:,None]-X2[None,:])**2, axis=-1)/(2*ell**2))

def gp_post(Xtr, ytr, Xte, noise=0.1):
    K = rbf_k(Xtr,Xtr)+noise*np.eye(len(Xtr)); Ks=rbf_k(Xtr,Xte)
    L=np.linalg.cholesky(K); v=np.linalg.solve(L,Ks)
    alpha=np.linalg.solve(L.T,np.linalg.solve(L,ytr))
    return Ks.T@alpha, np.maximum(1-np.sum(v**2,axis=0),0)

def acq_ei(mu, sig, f_best):
    Z=(f_best-mu)/(sig+1e-9); return (f_best-mu)*norm.cdf(Z)+sig*norm.pdf(Z)

rng=np.random.RandomState(0)
X_obs=rng.uniform(0,1,(6,2)); y_obs=np.array([branin(x) for x in X_obs])
cands=rng.uniform(0,1,(400,2))
best_ei=[y_obs.min()]; best_rand=[y_obs.min()]
for _ in range(20):
    mu,var=gp_post(X_obs,-y_obs,cands); sig=np.sqrt(var)
    bx=cands[acq_ei(mu,sig,-y_obs.min()).argmax()]
    y_new=branin(bx); X_obs=np.vstack([X_obs,[bx]]); y_obs=np.append(y_obs,y_new)
    best_ei.append(y_obs.min()); best_rand.append(branin(rng.uniform(0,1,2)))
rand_best=np.minimum.accumulate(best_rand)
print(f'EI best Branin    = {best_ei[-1]:.3f}  (global min approx 0.397)')
print(f'Random best       = {rand_best[-1]:.3f}')
```

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_k(X1, X2, ell=0.8):
    return np.exp(-np.sum((X1[:,None]-X2[None,:])**2, axis=-1)/(2*ell**2))

def gp_post(Xtr, ytr, Xte, noise=0.05):
    K=rbf_k(Xtr,Xtr)+noise*np.eye(len(Xtr)); Ks=rbf_k(Xtr,Xte)
    L=np.linalg.cholesky(K); v=np.linalg.solve(L,Ks)
    alpha=np.linalg.solve(L.T,np.linalg.solve(L,ytr))
    return Ks.T@alpha, np.maximum(1-np.sum(v**2,axis=0),0)

def kappa_anneal(t, T, k_max=5.0, k_min=0.2):
    return k_max * (k_min/k_max)**(t/max(T-1,1))

rng=np.random.RandomState(1)
f_true = lambda x: float(np.sin(3*x)*np.exp(-0.5*x))
X_obs=rng.uniform(-3,3,(4,1)); y_obs=np.array([f_true(x[0]) for x in X_obs])
X_te=np.linspace(-3,3,200)[:,None]; T=20; kappas=[]; bests=[]
for t in range(T):
    kappa=kappa_anneal(t,T); kappas.append(kappa)
    mu,var=gp_post(X_obs,y_obs,X_te)
    ucb=mu+kappa*np.sqrt(var); next_x=X_te[[ucb.argmax()]]
    y_new=f_true(next_x[0,0])
    X_obs=np.vstack([X_obs,next_x]); y_obs=np.append(y_obs,y_new); bests.append(y_obs.max())
print(f'UCB kappa-annealing over {T} steps, final best = {bests[-1]:.4f}')
print(f'Kappa schedule: {kappas[0]:.2f} (explore) -> {kappas[-1]:.2f} (exploit)')
for i in range(0, T, 5):
    print(f'  iter {i:2d}: kappa={kappas[i]:.2f}, best_so_far={bests[i]:.4f}')
```

## Acquisition Function Comparison

| Acquisition | Formula | Exploration | Closed Form | Regret Bound | Cost |
| --- | --- | --- | --- | --- | --- |
| EI | (μ−f*)Φ(Z)+σφ(Z), Z=(μ−f*)/σ | Moderate (via σφ(Z) term) | Yes | None proven | O(n³) GP + O(1) eval |
| PI | Φ((μ−f*)/σ) | Low (ignores improvement magnitude) | Yes | None proven | O(n³) GP + O(1) eval |
| UCB | μ(x)+κσ(x) | High (κ scales exploration) | Yes | Sublinear (GP-UCB) | O(n³) GP + O(1) eval |
| Thompson Sampling | argmax of GP posterior sample | Natural (posterior spread) | No (sampling required) | None proven | O(n³) GP + O(n²) sample |
| Entropy Search | max information gain about x* | Principled global exploration | No (EP/MC approx) | None in practice | O(n³) GP + O(heavy approx) |

EI is the practical default: closed-form, differentiable, well-calibrated exploration. UCB is preferred when theoretical guarantees matter or when κ can be tuned via the GP-UCB schedule. Thompson Sampling shines in parallel batch settings — draw B samples, evaluate B candidates simultaneously. Entropy Search is reserved for problems where the budget is very small (single-digit evaluations) and maximally informative queries justify the overhead. For noisy objectives, replace EI with Noisy EI using μ(x_{best}) in place of the raw f* maximum. The portfolio hedge strategy avoids committing to a single acquisition and is a strong baseline when the problem class is unknown.

