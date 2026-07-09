---
title: "Cross-Entropy as a Loss Function and Its MLE Connection"
slug: "cross-entropy-mle"
description: "Cross-entropy definition, its decomposition into entropy plus KL divergence, equivalence with MLE, and practical implications for classifier training and calibration."
tags: ["information-theory","math","foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ3Jvc3MtZW50cm9weSBicmlkZ2VzIGluZm9ybWF0aW9uIHRoZW9yeSBhbmQgbWF4aW11bSBsaWtlbGlob29kIGVzdGltYXRpb24sIHByb3ZpZGluZyBib3RoIHRoZSBsb3NzIGZ1bmN0aW9uIHVzZWQgdG8gdHJhaW4gdmlydHVhbGx5IGV2ZXJ5IG1vZGVybiBjbGFzc2lmaWVyIGFuZCBhIHJpZ29yb3VzIHByb2JhYmlsaXN0aWMganVzdGlmaWNhdGlvbiBmb3Igd2h5IHRoYXQgbG9zcyBpcyBzdGF0aXN0aWNhbGx5IG9wdGltYWwuIFVuZGVyc3RhbmRpbmcgdGhlIHByZWNpc2UgcmVsYXRpb25zaGlwIGJldHdlZW4gY3Jvc3MtZW50cm9weSBIKHAscSksIEtMIGRpdmVyZ2VuY2UgS0wocHx8cSksIGFuZCBNTEUgaXMgZXNzZW50aWFsIGZvciByZWFzb25pbmcgYWJvdXQgdHJhaW5pbmcgZHluYW1pY3MsIGNhbGlicmF0aW9uIGZhaWx1cmVzLCBsYWJlbCBzbW9vdGhpbmcsIHRlbXBlcmF0dXJlIHNjYWxpbmcsIGFuZCBwZXJwbGV4aXR5LiBUaGlzIG5vdGUgY292ZXJzIHRoZSBmdWxsIGNoYWluIGZyb20gZGVmaW5pdGlvbiB0byBwcmFjdGljYWwgUHlUb3JjaCBpbXBsZW1lbnRhdGlvbi4ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb3JlIERlZmluaXRpb24ifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdpdmVuIHRydWUgZGlzdHJpYnV0aW9uIHAgYW5kIG1vZGVsIGRpc3RyaWJ1dGlvbiBxIG92ZXIgdGhlIHNhbWUgYWxwaGFiZXQsIGNyb3NzLWVudHJvcHkgaXMgSChwLHEpID0gLXN1bV94IHAoeCkgbG9nIHEoeCkgPSBFX3BbLWxvZyBxKFgpXS4gVGhpcyBtZWFzdXJlcyB0aGUgYXZlcmFnZSBiaXRzIG5lZWRlZCB0byBlbmNvZGUgc2FtcGxlcyBmcm9tIHAgdXNpbmcgYSBjb2RlIG9wdGltaXplZCBmb3IgcS4gVW5saWtlIEgocCkgd2hpY2ggdXNlcyB0aGUgb3B0aW1hbCBjb2RlIGZvciBwLCBIKHAscSkgdXNlcyB0aGUgd3JvbmcgZGlzdHJpYnV0aW9uIHEsIGluY3VycmluZyBleHRyYSBiaXRzIGVxdWFsIHRvIEtMKHB8fHEpLiBUaGVyZWZvcmUgSChwLHEpID49IEgocCkgYWx3YXlzLCB3aXRoIGVxdWFsaXR5IGlmZiBwPXEgZXZlcnl3aGVyZS4gRm9yIG9uZS1ob3QgdGFyZ2V0cyBwPWRlbHRhX3t4PWN9LCBjcm9zcy1lbnRyb3B5IHJlZHVjZXMgdG8gLWxvZyBxKGMpOiB0aGUgbmVnYXRpdmUgbG9nLXByb2JhYmlsaXR5IGFzc2lnbmVkIHRvIHRoZSBjb3JyZWN0IGNsYXNzLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgYmNlX21hbnVhbCh5LCBxKTpcbiAgICAjIEJpbmFyeSBjcm9zcy1lbnRyb3B5IGZyb20gZmlyc3QgcHJpbmNpcGxlc1xuICAgIHEgPSB0b3JjaC5jbGFtcChxLCAxZS03LCAxIC0gMWUtNylcbiAgICByZXR1cm4gLSh5ICogcS5sb2coKSArICgxIC0geSkgKiAoMSAtIHEpLmxvZygpKS5tZWFuKClcblxuZGVmIGNjZV9tYW51YWwobG9nX3Byb2JzLCB0YXJnZXRzKTpcbiAgICAjIENhdGVnb3JpY2FsIENFOiAtbG9nIHFfYyBhdmVyYWdlZCBvdmVyIGJhdGNoXG4gICAgcmV0dXJuIC1sb2dfcHJvYnNbdG9yY2guYXJhbmdlKGxlbih0YXJnZXRzKSksIHRhcmdldHNdLm1lYW4oKVxuXG55ID0gdG9yY2gudGVuc29yKFsxLjAsIDAuMCwgMS4wLCAwLjBdKVxucSA9IHRvcmNoLnRlbnNvcihbMC45LCAwLjIsIDAuNywgMC4xXSlcbnByaW50KGYnQkNFIG1hbnVhbCA9IHtiY2VfbWFudWFsKHksIHEpLml0ZW0oKTouNGZ9JylcbnByaW50KGYnQkNFIEYuZnVuYyA9IHtGLmJpbmFyeV9jcm9zc19lbnRyb3B5KHEsIHkpLml0ZW0oKTouNGZ9JylcblxubG9naXRzICA9IHRvcmNoLnRlbnNvcihbWzIuMCwgMS4wLCAwLjVdLCBbMC41LCAyLjUsIDAuMF1dKVxudGFyZ2V0cyA9IHRvcmNoLnRlbnNvcihbMCwgMV0pXG5sb2dfcCAgID0gRi5sb2dfc29mdG1heChsb2dpdHMsIGRpbT0xKVxucHJpbnQoZidDQ0UgbWFudWFsID0ge2NjZV9tYW51YWwobG9nX3AsIHRhcmdldHMpLml0ZW0oKTouNGZ9JylcbnByaW50KGYnQ0NFIEYuZnVuYyA9IHtGLmNyb3NzX2VudHJvcHkobG9naXRzLCB0YXJnZXRzKS5pdGVtKCk6LjRmfScpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWF0aGVtYXRpY2FsIFByb3BlcnRpZXM6IERlY29tcG9zaXRpb24gYW5kIE1MRSBFcXVpdmFsZW5jZSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBkZWNvbXBvc2l0aW9uOiBIKHAscSkgPSBIKHApICsgS0wocHx8cSkuIFByb29mOiBleHBhbmQgS0wocHx8cSkgPSBzdW1feCBwKHgpIGxvZyhwKHgpL3EoeCkpID0gLUgocCkgKyBIKHAscSkgYW5kIHJlYXJyYW5nZS4gVHJhaW5pbmcgaW1wbGljYXRpb25zOiBIKHApIGlzIGZpeGVkIGJ5IHRoZSBkYXRhIOKAlCB0aGUgaXJyZWR1Y2libGUgZmxvb3IgcmVnYXJkbGVzcyBvZiBtb2RlbCBzaXplLiBLTChwfHxxKSBpcyB3aGF0IHRyYWluaW5nIGNhbiByZWR1Y2UuIE1pbmltaXppbmcgSChwLHEpIG92ZXIgbW9kZWwgcGFyYW1ldGVycyBpcyBpZGVudGljYWwgdG8gbWluaW1pemluZyBLTChwfHxxKSwgd2hpY2ggZXF1YWxzIE1MRTogYXJnbWF4X3RoZXRhIHByb2RfaSBxX3RoZXRhKHhpKSA9IGFyZ21pbl90aGV0YSBzdW1faSAtbG9nIHFfdGhldGEoeGkpID0gYXJnbWluX3RoZXRhIEgocF9oYXQsIHFfdGhldGEpIHdoZXJlIHBfaGF0IGlzIHRoZSBlbXBpcmljYWwgZGlzdHJpYnV0aW9uIG92ZXIgdHJhaW5pbmcgc2FtcGxlcy4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGxvZ2lzdGljX25sbCh3LCBYLCB5KTpcbiAgICAjIE5MTCA9IGNyb3NzLWVudHJvcHkgbG9zcyBmb3IgbG9naXN0aWMgcmVncmVzc2lvblxuICAgIGxvZ2l0cyAgICA9IFggQCB3XG4gICAgbG9nX3NpZyAgID0gLXRvcmNoLmxvZzFwKHRvcmNoLmV4cCgtbG9naXRzKSkgICAgIyBsb2cgc2lnbWEobG9naXQpXG4gICAgbG9nXzFzaWcgID0gLXRvcmNoLmxvZzFwKHRvcmNoLmV4cChsb2dpdHMpKSAgICAgIyBsb2coMS1zaWdtYSlcbiAgICByZXR1cm4gLSh5ICogbG9nX3NpZyArICgxIC0geSkgKiBsb2dfMXNpZykubWVhbigpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxubiwgZCA9IDIwMCwgNFxuWCAgICAgID0gdG9yY2gucmFuZG4obiwgZClcbndfdHJ1ZSA9IHRvcmNoLnRlbnNvcihbMS4wLCAtMC41LCAwLjMsIC0wLjJdKVxueSAgICAgID0gdG9yY2guYmVybm91bGxpKHRvcmNoLnNpZ21vaWQoWCBAIHdfdHJ1ZSkpXG5cbiMgR3JhZGllbnQgZGVzY2VudCBvbiBOTEwgPT0gbWluaW1pemluZyBjcm9zcy1lbnRyb3B5XG53ID0gdG9yY2guemVyb3MoZCwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxub3B0ID0gdG9yY2gub3B0aW0uU0dEKFt3XSwgbHI9MC41KVxuZm9yIHN0ZXAgaW4gcmFuZ2UoMjAxKTpcbiAgICBsb3NzID0gbG9naXN0aWNfbmxsKHcsIFgsIHkpXG4gICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgb3B0LnN0ZXAoKVxuICAgIGlmIHN0ZXAgJSA1MCA9PSAwOlxuICAgICAgICBwcmludChmJ1N0ZXAge3N0ZXA6M2R9OiBOTEwgKENFKSA9IHtsb3NzLml0ZW0oKTouNGZ9JylcbnByaW50KGYnVHJ1ZSB3OiAgICAgIHt3X3RydWUubnVtcHkoKX0nKVxucHJpbnQoZidFc3RpbWF0ZWQgdzoge3cuZGF0YS5udW1weSgpLnJvdW5kKDMpfScpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVmFyaWFudHMgYW5kIFNwZWNpYWwgQ2FzZXMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJpbmFyeSBjcm9zcy1lbnRyb3B5IChCQ0UpOiBIKHAscSkgPSAteSBsb2cgcSAtICgxLXkpIGxvZygxLXEpIGZvciBiaW5hcnkgdGFyZ2V0cyB5IGluIHswLDF9LiBDYXRlZ29yaWNhbCBDRSB3aXRoIG9uZS1ob3QgdGFyZ2V0czogSCA9IC1sb2cgcV9jIHdoZXJlIGMgaXMgdGhlIHRydWUgY2xhc3MgaW5kZXguIExhYmVsIHNtb290aGluZzogcmVwbGFjZSBvbmUtaG90IHAgd2l0aCBwX3Ntb290aChrKSA9ICgxLWVwcykqMVtrPWNdICsgZXBzL0ssIHJhaXNpbmcgSChwKSBmcm9tIDAgdG8gYXBwcm94aW1hdGVseSBlcHMqbG9nKEspIG5hdHMsIHdoaWNoIGRpc2NvdXJhZ2VzIG92ZXJjb25maWRlbmNlLiBUZW1wZXJhdHVyZSBzY2FsaW5nOiBxX1QoeCkgPSBzb2Z0bWF4KGxvZ2l0cy9UKSDigJQgVD4xIHNwcmVhZHMgcHJvYmFiaWxpdHkgbWFzcyAoaGlnaGVyIGVudHJvcHkpLCBUPDEgY29uY2VudHJhdGVzIGl0IChsb3dlciBlbnRyb3B5LCBzaGFycGVyIHByZWRpY3Rpb25zKS4gUGVycGxleGl0eTogUFBMID0gZXhwKEgocCxxKSkgaW4gbmF0cywgaW50ZXJwcmV0YWJsZSBhcyB0aGUgYXZlcmFnZSBicmFuY2hpbmcgZmFjdG9yIHRoZSBtb2RlbCBmYWNlcyBhdCBlYWNoIHRva2VuLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1MIGFuZCBBSSBDb25uZWN0aW9ucyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ3Jvc3MtZW50cm9weSBiZWF0cyBNU0UgZm9yIGNsYXNzaWZpY2F0aW9uIG9uIHRocmVlIGdyb3VuZHM6IGdyYWRpZW50IGJlaGF2aW9yLCBwcm9iYWJpbGlzdGljIG1lYW5pbmcsIGFuZCBzdGF0aXN0aWNhbCBvcHRpbWFsaXR5LiBUaGUgQ0UgZ3JhZGllbnQgd2l0aCByZXNwZWN0IHRvIGxvZ2l0cyBpcyAocS15KSDigJQgbmV2ZXIgc2F0dXJhdGVzLiBUaGUgTVNFIGdyYWRpZW50IGlzIChxLXkpKnEqKDEtcSksIHdoaWNoIHZhbmlzaGVzIGFzIHEgYXBwcm9hY2hlcyAwIG9yIDEsIGV4YWN0bHkgdGhlIHJlZ2ltZXMgd2hlcmUgc3Ryb25nIGNvcnJlY3Rpb25zIGFyZSBuZWVkZWQuIENFIGRpcmVjdGx5IG9wdGltaXplcyB0aGUgcHJvYmFiaWxpdHkgYXNzaWduZWQgdG8gdGhlIGNvcnJlY3QgY2xhc3MsIG1ha2luZyBjYWxpYnJhdGlvbiBhIG5hdHVyYWwgYnlwcm9kdWN0LiBDRSB3aXRoIHNvZnRtYXggb3V0cHV0IGlzIGNvbnZleCBwZXIgZXhhbXBsZSwgd2hpbGUgTVNFIHdpdGggc2lnbW9pZCBpcyBub3QuIE1pbmltaXppbmcgQ0UgaXMgTUxFIOKAlCBpbmhlcml0aW5nIGNvbnNpc3RlbmN5LCBhc3ltcHRvdGljIGVmZmljaWVuY3ksIGFuZCBDcmFtZXItUmFvIGJvdW5kIHByb3BlcnRpZXMgZnJvbSBjbGFzc2ljYWwgZXN0aW1hdGlvbiB0aGVvcnkuIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgbGFiZWxfc21vb3RoX2NlKGxvZ2l0cywgdGFyZ2V0cywgZXBzPTAuMSk6XG4gICAgIyBMYWJlbC1zbW9vdGhlZCBjcm9zcy1lbnRyb3B5XG4gICAgSyAgICAgICAgPSBsb2dpdHMuc2hhcGVbLTFdXG4gICAgbG9nX3AgICAgPSBGLmxvZ19zb2Z0bWF4KGxvZ2l0cywgZGltPS0xKVxuICAgIGNlX2hhcmQgID0gRi5jcm9zc19lbnRyb3B5KGxvZ2l0cywgdGFyZ2V0cywgcmVkdWN0aW9uPSdub25lJylcbiAgICBjZV91bmlmICA9IC1sb2dfcC5tZWFuKGRpbT0tMSkgICMgdW5pZm9ybSBzbW9vdGhpbmcgdGVybVxuICAgIHJldHVybiAoKDEgLSBlcHMpICogY2VfaGFyZCArIGVwcyAqIGNlX3VuaWYpLm1lYW4oKVxuXG4jIENvbXBhcmUgaGFyZCB2cyBzbW9vdGhlZCBDRSBvbiBvdmVyY29uZmlkZW50IGxvZ2l0c1xubG9naXRzICA9IHRvcmNoLnRlbnNvcihbWzEwLjAsIDAuMCwgMC4wXSwgWzAuMCwgMTAuMCwgMC4wXV0pXG50YXJnZXRzID0gdG9yY2gudGVuc29yKFswLCAxXSlcblxuY2VfaGFyZCAgID0gRi5jcm9zc19lbnRyb3B5KGxvZ2l0cywgdGFyZ2V0cylcbmNlX3Ntb290aCA9IGxhYmVsX3Ntb290aF9jZShsb2dpdHMsIHRhcmdldHMsIGVwcz0wLjEpXG5wcmludChmJ0hhcmQgQ0UgICAgID0ge2NlX2hhcmQuaXRlbSgpOi40Zn0gbmF0cycpXG5wcmludChmJ1Ntb290aCBDRSAgID0ge2NlX3Ntb290aC5pdGVtKCk6LjRmfSBuYXRzJylcblxuIyBUaGUgbmV3IGlycmVkdWNpYmxlIGZsb29yIGFmdGVyIHNtb290aGluZ1xuSyAgICA9IDNcbmVwcyAgPSAwLjFcbnBfcyAgPSB0b3JjaC50ZW5zb3IoWygxLWVwcykgKyBlcHMvSywgZXBzL0ssIGVwcy9LXSkgICMgc21vb3RoZWQgdGFyZ2V0XG5oX3BzID0gLShwX3MgKiBwX3MubG9nKCkpLnN1bSgpXG5wcmludChmJ0gocF9zbW9vdGgpID0ge2hfcHMuaXRlbSgpOi40Zn0gbmF0cyAobmV3IGZsb29yLCB3YXMgMCB3aXRoIGhhcmQgbGFiZWxzKScpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW1wbGVtZW50YXRpb24gUGl0ZmFsbHMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5ldmVyIGNvbXB1dGUgc29mdG1heCB0aGVuIGxvZyBtYW51YWxseTogbG9nKHNvZnRtYXgoeCkpIGxvc2VzIHByZWNpc2lvbiBmb3IgbGFyZ2UgbG9naXRzIGJlY2F1c2UgZXhwIG92ZXJmbG93cyBiZWZvcmUgZGl2aXNpb24uIEFsd2F5cyB1c2UgRi5sb2dfc29mdG1heCBvciBGLmNyb3NzX2VudHJvcHkgd2hpY2ggYXBwbHkgdGhlIGxvZy1zdW0tZXhwIHRyaWNrIGludGVybmFsbHkuIEZvciBCQ0Ugd2l0aCByYXcgcHJvYmFiaWxpdGllcywgY2xhbXAgdG8gWzFlLTcsIDEtMWUtN10gYmVmb3JlIHRha2luZyBsb2cgdG8gcHJldmVudCAtaW5mIGdyYWRpZW50cy4gRG8gbm90IHVzZSBNU0Ugb24gc2lnbW9pZCBvdXRwdXRzIGZvciBjbGFzc2lmaWNhdGlvbiDigJQgZ3JhZGllbnRzIHNhdHVyYXRlIGF0IHByZWRpY3Rpb25zIG5lYXIgMCBvciAxLCB0aGUgZXhhY3Qgc2FtcGxlcyB0aGF0IG5lZWQgdGhlIHN0cm9uZ2VzdCBjb3JyZWN0aW9ucy4gQ2xhc3Mgd2VpZ2h0cyBpbiBGLmNyb3NzX2VudHJvcHkgbXVzdCBzdW0gdG8gYSBtZWFuaW5nZnVsIHNjYWxlIOKAlCB1c2luZyByYXcgY2xhc3MgZnJlcXVlbmNpZXMgaXMgY29ycmVjdCwgYnV0IGRvdWJsZS1jaGVjayB0aGF0IGxvc3MgbWFnbml0dWRlIGRvZXMgbm90IHNoaWZ0IGFjcm9zcyBleHBlcmltZW50cyB3aGVuIHdlaWdodHMgY2hhbmdlLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBHdWlkYW5jZSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVXNlIEYuY3Jvc3NfZW50cm9weSBhcyB0aGUgY2Fub25pY2FsIGZ1bmN0aW9uIGZvciBtdWx0aS1jbGFzcyB0YXNrcyDigJQgaXQgaXMgbnVtZXJpY2FsbHkgc3RhYmxlIGFuZCBzdXBwb3J0cyBjbGFzcyB3ZWlnaHRzIGRpcmVjdGx5LiBBZGQgbGFiZWwgc21vb3RoaW5nIChlcHM9MC4xKSBhcyBhIGRlZmF1bHQgcmVndWxhcml6ZXIgZm9yIGNsYXNzaWZpY2F0aW9uIHByb2JsZW1zIHdpdGggbW9yZSB0aGFuIDIgY2xhc3NlczogaXQgcmFyZWx5IGh1cnRzIGFjY3VyYWN5IGFuZCBjb25zaXN0ZW50bHkgaW1wcm92ZXMgRXhwZWN0ZWQgQ2FsaWJyYXRpb24gRXJyb3IuIEZvciBMTE0gZXZhbHVhdGlvbiwgYWx3YXlzIHJlcG9ydCBwZXJwbGV4aXR5IGFzIGV4cChtZWFuIHRva2VuIENFIGluIG5hdHMpIHdpdGggdm9jYWJ1bGFyeSBzaXplIGFuZCB0b2tlbml6ZXIgY2xlYXJseSBzcGVjaWZpZWQuIFVzZSB0ZW1wZXJhdHVyZSBzY2FsaW5nIHBvc3QtaG9jIChjYWxpYnJhdGUgVCBvbiBhIHZhbGlkYXRpb24gc2V0KSB0byBpbXByb3ZlIGNhbGlicmF0aW9uIG9mIGFuIGFscmVhZHktdHJhaW5lZCBjbGFzc2lmaWVyIHdpdGhvdXQgcmV0cmFpbmluZy4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiB0ZW1wZXJhdHVyZV9jZShsb2dpdHMsIHRhcmdldHMsIFQ9MS4wKTpcbiAgICAjIFRlbXBlcmF0dXJlLXNjYWxlZCBjcm9zcy1lbnRyb3B5OiBUPjEgc29mdGVucywgVDwxIHNoYXJwZW5zXG4gICAgcmV0dXJuIEYuY3Jvc3NfZW50cm9weShsb2dpdHMgLyBULCB0YXJnZXRzKVxuXG5kZWYgcGVycGxleGl0eV9uYXRzKGxvZ2l0cywgdGFyZ2V0cyk6XG4gICAgIyBQZXJwbGV4aXR5IGZyb20gQ0UgaW4gbmF0c1xuICAgIGNlID0gRi5jcm9zc19lbnRyb3B5KGxvZ2l0cywgdGFyZ2V0cykgICMgbmF0cyAobmF0dXJhbCBsb2cpXG4gICAgcmV0dXJuIHRvcmNoLmV4cChjZSkuaXRlbSgpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5sb2dpdHMgID0gdG9yY2gucmFuZG4oMTYsIDEwMCkgICAjIGJhdGNoPTE2LCB2b2NhYj0xMDBcbnRhcmdldHMgPSB0b3JjaC5yYW5kaW50KDAsIDEwMCwgKDE2LCkpXG5cbmZvciBUIGluIFswLjUsIDEuMCwgMi4wXTpcbiAgICBjZSAgPSB0ZW1wZXJhdHVyZV9jZShsb2dpdHMsIHRhcmdldHMsIFQ9VClcbiAgICBwcGwgPSB0b3JjaC5leHAoY2UpLml0ZW0oKVxuICAgIHByaW50KGYnVD17VDouMWZ9OiBDRT17Y2UuaXRlbSgpOi40Zn0gbmF0cyAgUFBMPXtwcGw6LjJmfScpXG5cbiMgQ3Jvc3MtZW50cm9weSBkZWNvbXBvc2l0aW9uOiBIKHAscSkgPSBIKHApICsgS0wocHx8cSlcbnFfbG9nID0gRi5sb2dfc29mdG1heChsb2dpdHMsIGRpbT0tMSlcbiMgRm9yIG9uZS1ob3QgcCwgSChwKT0wIGFuZCBIKHAscSkgPSBLTChwfHxxKSA9IC1sb2cgcV9jXG5jZV92YWwgPSBGLmNyb3NzX2VudHJvcHkobG9naXRzLCB0YXJnZXRzKS5pdGVtKClcbnByaW50KGYnSChwLHEpID0ge2NlX3ZhbDouNGZ9IG5hdHMgIFtvbmUtaG90OiBIKHApPTAsIHNvIGFsbCBpcyBLTF0nKSJ9LAogIHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJNTEUgRXF1aXZhbGVuY2UgSXMgdGhlIENvcmUgSW5zaWdodCIsImNvbnRlbnQiOiJNaW5pbWl6aW5nIEgocF9kYXRhLCBxX21vZGVsKSBvdmVyIG1vZGVsIHBhcmFtZXRlcnMgaXMgZXhhY3RseSBtYXhpbXVtIGxpa2VsaWhvb2QgZXN0aW1hdGlvbi4gVGhpcyBlcXVpdmFsZW5jZSBtZWFucyBldmVyeSByZXN1bHQgZnJvbSBNTEUgdGhlb3J5IOKAlCBjb25zaXN0ZW5jeSwgYXN5bXB0b3RpYyBlZmZpY2llbmN5LCBDcmFtZXItUmFvIGxvd2VyIGJvdW5kIOKAlCBhcHBsaWVzIGRpcmVjdGx5IHRvIGNyb3NzLWVudHJvcHkgdHJhaW5pbmcuIFRoZSBjcm9zcy1lbnRyb3B5IGxvc3MgaXMgbm90IGFuIGFyYml0cmFyeSBlbmdpbmVlcmluZyBjaG9pY2U6IGl0IGlzIHRoZSBzdGF0aXN0aWNhbGx5IG9wdGltYWwgbG9zcyBmdW5jdGlvbiBmb3IgbGVhcm5pbmcgYSBkaXN0cmlidXRpb24gZnJvbSBpLmkuZC4gc2FtcGxlcywgYW5kIGl0cyBncmFkaWVudCBoYXMgdGhlIGNsZWFuZXN0IGZvcm0gb2YgYW55IHByb2JhYmlsaXN0aWMgbG9zcy4ifSwKICB7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTG9zcyBWYXJpYW50IiwiRm9ybXVsYSIsIldoZW4gdG8gVXNlIl0sInJvd3MiOltbIkJpbmFyeSBDRSIsIi15IGxvZyBxIC0gKDEteSkgbG9nKDEtcSkiLCJCaW5hcnkgY2xhc3NpZmljYXRpb24sIG11bHRpLWxhYmVsIl0sWyJDYXRlZ29yaWNhbCBDRSIsIi1sb2cgcV9jIChvbmUtaG90IHRhcmdldHMpIiwiU2luZ2xlLWxhYmVsIEstY2xhc3MgY2xhc3NpZmljYXRpb24iXSxbIkxhYmVsLVNtb290aGVkIENFIiwiLSgxLWVwcykgbG9nIHFfYyAtIChlcHMvSykgc3VtIGxvZyBxX2siLCJPdmVyY29uZmlkZW5jZSBwcmV2ZW50aW9uLCBjYWxpYnJhdGlvbiJdLFsiV2VpZ2h0ZWQgQ0UiLCItd19jIGxvZyBxX2MiLCJDbGFzcyBpbWJhbGFuY2UgY29ycmVjdGlvbiJdLFsiRm9jYWwgTG9zcyIsIi0oMS1xX2MpXmdhbW1hIGxvZyBxX2MiLCJIYXJkIGV4YW1wbGUgbWluaW5nLCBvYmplY3QgZGV0ZWN0aW9uIl1dfSwKICB7InR5cGUiOiJkaXZpZGVyIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LAogIHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiSChwLHEpID0gLUVfcFtsb2cgcShYKV0g4oCUIGNyb3NzLWVudHJvcHkgbWVhc3VyZXMgZW5jb2RpbmcgY29zdCB1c2luZyB0aGUgd3JvbmcgKG1vZGVsKSBkaXN0cmlidXRpb24iLCJIKHAscSkgPSBIKHApICsgS0wocHx8cSk6IHRyYWluaW5nIHJlZHVjZXMgb25seSBLTDsgSChwKSBpcyB0aGUgaXJyZWR1Y2libGUgZmxvb3IgZml4ZWQgYnkgdGhlIGRhdGEgZGlzdHJpYnV0aW9uIiwiTWluaW1pemluZyBjcm9zcy1lbnRyb3B5IGlzIGV4YWN0bHkgTUxFIOKAlCBhbGwgTUxFIGd1YXJhbnRlZXMgKGNvbnNpc3RlbmN5LCBhc3ltcHRvdGljIGVmZmljaWVuY3kpIGFwcGx5IGRpcmVjdGx5IiwiQ0UgZ3JhZGllbnQgZm9yIHNpZ21vaWQtb3V0cHV0IGNsYXNzaWZpZXJzIGlzIChxLXkpLCBuZXZlciBzYXR1cmF0aW5nOyBNU0UgZ3JhZGllbnQgKHEteSkqcSooMS1xKSBzYXR1cmF0ZXMgbmVhciAwIGFuZCAxIiwiTGFiZWwgc21vb3RoaW5nIHJhaXNlcyBIKHApIGZyb20gMCB0byB+ZXBzKmxvZyhLKSwgcHJldmVudGluZyBvdmVyY29uZmlkZW5jZSBhbmQgaW1wcm92aW5nIGNhbGlicmF0aW9uIGF0IG5vIGFjY3VyYWN5IGNvc3QiLCJUZW1wZXJhdHVyZSBUPjEgaW5jcmVhc2VzIHByZWRpY3RpdmUgZW50cm9weTsgVDwxIGRlY3JlYXNlcyBpdCDigJQgcG9zdC1ob2MgdGVtcGVyYXR1cmUgY2FsaWJyYXRpb24gbmVlZHMgbm8gcmV0cmFpbmluZyIsIlBlcnBsZXhpdHkgPSBleHAoQ0UgaW4gbmF0cyk6IGludGVycHJldGFibGUgYXMgdGhlIGF2ZXJhZ2UgZWZmZWN0aXZlIGJyYW5jaGluZyBmYWN0b3I7IGxvd2VyIG1lYW5zIGJldHRlciBjb21wcmVzc2lvbiBvZiB0aGUgZGF0YSJdfQpdCg=="
---
# Cross-Entropy as a Loss Function and Its MLE Connection

Cross-entropy bridges information theory and maximum likelihood estimation, providing both the loss function used to train virtually every modern classifier and a rigorous probabilistic justification for why that loss is statistically optimal. Understanding the precise relationship between cross-entropy H(p,q), KL divergence KL(p||q), and MLE is essential for reasoning about training dynamics, calibration failures, label smoothing, temperature scaling, and perplexity. This note covers the full chain from definition to practical PyTorch implementation.

## Core Definition

Given true distribution p and model distribution q over the same alphabet, cross-entropy is H(p,q) = -sum_x p(x) log q(x) = E_p[-log q(X)]. This measures the average bits needed to encode samples from p using a code optimized for q. Unlike H(p) which uses the optimal code for p, H(p,q) uses the wrong distribution q, incurring extra bits equal to KL(p||q). Therefore H(p,q) >= H(p) always, with equality iff p=q everywhere. For one-hot targets p=delta_{x=c}, cross-entropy reduces to -log q(c): the negative log-probability assigned to the correct class.

```python
import torch
import torch.nn.functional as F
import numpy as np

def bce_manual(y, q):
    # Binary cross-entropy from first principles
    q = torch.clamp(q, 1e-7, 1 - 1e-7)
    return -(y * q.log() + (1 - y) * (1 - q).log()).mean()

def cce_manual(log_probs, targets):
    # Categorical CE: -log q_c averaged over batch
    return -log_probs[torch.arange(len(targets)), targets].mean()

y = torch.tensor([1.0, 0.0, 1.0, 0.0])
q = torch.tensor([0.9, 0.2, 0.7, 0.1])
print(f'BCE manual = {bce_manual(y, q).item():.4f}')
print(f'BCE F.func = {F.binary_cross_entropy(q, y).item():.4f}')

logits  = torch.tensor([[2.0, 1.0, 0.5], [0.5, 2.5, 0.0]])
targets = torch.tensor([0, 1])
log_p   = F.log_softmax(logits, dim=1)
print(f'CCE manual = {cce_manual(log_p, targets).item():.4f}')
print(f'CCE F.func = {F.cross_entropy(logits, targets).item():.4f}')
```

## Mathematical Properties: Decomposition and MLE Equivalence

The key decomposition: H(p,q) = H(p) + KL(p||q). Proof: expand KL(p||q) = sum_x p(x) log(p(x)/q(x)) = -H(p) + H(p,q) and rearrange. Training implications: H(p) is fixed by the data — the irreducible floor regardless of model size. KL(p||q) is what training can reduce. Minimizing H(p,q) over model parameters is identical to minimizing KL(p||q), which equals MLE: argmax_theta prod_i q_theta(xi) = argmin_theta sum_i -log q_theta(xi) = argmin_theta H(p_hat, q_theta) where p_hat is the empirical distribution over training samples.

```python
import torch
import numpy as np

def logistic_nll(w, X, y):
    # NLL = cross-entropy loss for logistic regression
    logits    = X @ w
    log_sig   = -torch.log1p(torch.exp(-logits))    # log sigma(logit)
    log_1sig  = -torch.log1p(torch.exp(logits))     # log(1-sigma)
    return -(y * log_sig + (1 - y) * log_1sig).mean()

torch.manual_seed(42)
n, d = 200, 4
X      = torch.randn(n, d)
w_true = torch.tensor([1.0, -0.5, 0.3, -0.2])
y      = torch.bernoulli(torch.sigmoid(X @ w_true))

# Gradient descent on NLL == minimizing cross-entropy
w = torch.zeros(d, requires_grad=True)
opt = torch.optim.SGD([w], lr=0.5)
for step in range(201):
    loss = logistic_nll(w, X, y)
    opt.zero_grad()
    loss.backward()
    opt.step()
    if step % 50 == 0:
        print(f'Step {step:3d}: NLL (CE) = {loss.item():.4f}')
print(f'True w:      {w_true.numpy()}')
print(f'Estimated w: {w.data.numpy().round(3)}')
```

## Variants and Special Cases

Binary cross-entropy (BCE): H(p,q) = -y log q - (1-y) log(1-q) for binary targets y in {0,1}. Categorical CE with one-hot targets: H = -log q_c where c is the true class index. Label smoothing: replace one-hot p with p_smooth(k) = (1-eps)*1[k=c] + eps/K, raising H(p) from 0 to approximately eps*log(K) nats, which discourages overconfidence. Temperature scaling: q_T(x) = softmax(logits/T) — T>1 spreads probability mass (higher entropy), T<1 concentrates it (lower entropy, sharper predictions). Perplexity: PPL = exp(H(p,q)) in nats, interpretable as the average branching factor the model faces at each token.

## ML and AI Connections

Cross-entropy beats MSE for classification on three grounds: gradient behavior, probabilistic meaning, and statistical optimality. The CE gradient with respect to logits is (q-y) — never saturates. The MSE gradient is (q-y)*q*(1-q), which vanishes as q approaches 0 or 1, exactly the regimes where strong corrections are needed. CE directly optimizes the probability assigned to the correct class, making calibration a natural byproduct. CE with softmax output is convex per example, while MSE with sigmoid is not. Minimizing CE is MLE — inheriting consistency, asymptotic efficiency, and Cramer-Rao bound properties from classical estimation theory.

```python
import torch
import torch.nn.functional as F

def label_smooth_ce(logits, targets, eps=0.1):
    # Label-smoothed cross-entropy
    K        = logits.shape[-1]
    log_p    = F.log_softmax(logits, dim=-1)
    ce_hard  = F.cross_entropy(logits, targets, reduction='none')
    ce_unif  = -log_p.mean(dim=-1)  # uniform smoothing term
    return ((1 - eps) * ce_hard + eps * ce_unif).mean()

# Compare hard vs smoothed CE on overconfident logits
logits  = torch.tensor([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0]])
targets = torch.tensor([0, 1])

ce_hard   = F.cross_entropy(logits, targets)
ce_smooth = label_smooth_ce(logits, targets, eps=0.1)
print(f'Hard CE     = {ce_hard.item():.4f} nats')
print(f'Smooth CE   = {ce_smooth.item():.4f} nats')

# The new irreducible floor after smoothing
K    = 3
eps  = 0.1
p_s  = torch.tensor([(1-eps) + eps/K, eps/K, eps/K])  # smoothed target
h_ps = -(p_s * p_s.log()).sum()
print(f'H(p_smooth) = {h_ps.item():.4f} nats (new floor, was 0 with hard labels)')
```

## Implementation Pitfalls

Never compute softmax then log manually: log(softmax(x)) loses precision for large logits because exp overflows before division. Always use F.log_softmax or F.cross_entropy which apply the log-sum-exp trick internally. For BCE with raw probabilities, clamp to [1e-7, 1-1e-7] before taking log to prevent -inf gradients. Do not use MSE on sigmoid outputs for classification — gradients saturate at predictions near 0 or 1, the exact samples that need the strongest corrections. Class weights in F.cross_entropy must sum to a meaningful scale — using raw class frequencies is correct, but double-check that loss magnitude does not shift across experiments when weights change.

## Practical Guidance

Use F.cross_entropy as the canonical function for multi-class tasks — it is numerically stable and supports class weights directly. Add label smoothing (eps=0.1) as a default regularizer for classification problems with more than 2 classes: it rarely hurts accuracy and consistently improves Expected Calibration Error. For LLM evaluation, always report perplexity as exp(mean token CE in nats) with vocabulary size and tokenizer clearly specified. Use temperature scaling post-hoc (calibrate T on a validation set) to improve calibration of an already-trained classifier without retraining.

```python
import torch
import torch.nn.functional as F

def temperature_ce(logits, targets, T=1.0):
    # Temperature-scaled cross-entropy: T>1 softens, T<1 sharpens
    return F.cross_entropy(logits / T, targets)

def perplexity_nats(logits, targets):
    # Perplexity from CE in nats
    ce = F.cross_entropy(logits, targets)  # nats (natural log)
    return torch.exp(ce).item()

torch.manual_seed(0)
logits  = torch.randn(16, 100)   # batch=16, vocab=100
targets = torch.randint(0, 100, (16,))

for T in [0.5, 1.0, 2.0]:
    ce  = temperature_ce(logits, targets, T=T)
    ppl = torch.exp(ce).item()
    print(f'T={T:.1f}: CE={ce.item():.4f} nats  PPL={ppl:.2f}')

# Cross-entropy decomposition: H(p,q) = H(p) + KL(p||q)
ce_val = F.cross_entropy(logits, targets).item()
print(f'H(p,q) = {ce_val:.4f} nats  [one-hot: H(p)=0, so all is KL]')
```

> **TIP: MLE Equivalence Is the Core Insight**
> Minimizing H(p_data, q_model) over model parameters is exactly maximum likelihood estimation. This equivalence means every result from MLE theory — consistency, asymptotic efficiency, Cramer-Rao lower bound — applies directly to cross-entropy training. The cross-entropy loss is not an arbitrary engineering choice: it is the statistically optimal loss function for learning a distribution from i.i.d. samples.

| Loss Variant | Formula | When to Use |
|---|---|---|
| Binary CE | -y log q - (1-y) log(1-q) | Binary classification, multi-label |
| Categorical CE | -log q_c (one-hot targets) | Single-label K-class classification |
| Label-Smoothed CE | -(1-eps) log q_c - (eps/K) sum log q_k | Overconfidence prevention, calibration |
| Weighted CE | -w_c log q_c | Class imbalance correction |
| Focal Loss | -(1-q_c)^gamma log q_c | Hard example mining, object detection |

---

## Key Takeaways

- H(p,q) = -E_p[log q(X)] — cross-entropy measures encoding cost using the wrong (model) distribution
- H(p,q) = H(p) + KL(p||q): training reduces only KL; H(p) is the irreducible floor fixed by the data distribution
- Minimizing cross-entropy is exactly MLE — all MLE guarantees (consistency, asymptotic efficiency) apply directly
- CE gradient for sigmoid-output classifiers is (q-y), never saturating; MSE gradient (q-y)*q*(1-q) saturates near 0 and 1
- Label smoothing raises H(p) from 0 to ~eps*log(K), preventing overconfidence and improving calibration at no accuracy cost
- Temperature T>1 increases predictive entropy; T<1 decreases it — post-hoc temperature calibration needs no retraining
- Perplexity = exp(CE in nats): interpretable as the average effective branching factor; lower means better compression of the data