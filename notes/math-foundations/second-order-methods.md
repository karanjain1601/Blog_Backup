---
title: "Second-Order Methods — Newton's Method and L-BFGS"
slug: "second-order-methods"
description: "Newton's method quadratic convergence, practical infeasibility for deep learning, quasi-Newton and L-BFGS algorithm, Gauss-Newton approximation, K-FAC, and when second-order methods beat Adam."
tags: ["optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU2Vjb25kLW9yZGVyIG9wdGltaXphdGlvbiBtZXRob2RzIHVzZSBjdXJ2YXR1cmUgaW5mb3JtYXRpb24gKHRoZSBIZXNzaWFuIG1hdHJpeCkgaW4gYWRkaXRpb24gdG8gZ3JhZGllbnQgaW5mb3JtYXRpb24gdG8gY29tcHV0ZSBiZXR0ZXIgdXBkYXRlIGRpcmVjdGlvbnMuIFRoZW9yZXRpY2FsbHksIHRoZXkgYXJlIGRyYW1hdGljYWxseSBzdXBlcmlvcjogd2hpbGUgZ3JhZGllbnQgZGVzY2VudCBjb252ZXJnZXMgYXQgYSBsaW5lYXIgcmF0ZSBPKDEvdCkgZm9yIHN0cm9uZ2x5IGNvbnZleCBmdW5jdGlvbnMsIE5ld3RvbidzIG1ldGhvZCBjb252ZXJnZXMgcXVhZHJhdGljYWxseSAobnVtYmVyIG9mIGNvcnJlY3QgZGlnaXRzIGRvdWJsZXMgcGVyIGl0ZXJhdGlvbikgYW5kIHJlYWNoZXMgaGlnaCBwcmVjaXNpb24gaW4gdmVyeSBmZXcgc3RlcHMuIEluIHByYWN0aWNlLCBob3dldmVyLCBzZWNvbmQtb3JkZXIgbWV0aG9kcyBhcmUgcmFyZWx5IHVzZWQgZm9yIGRlZXAgbGVhcm5pbmcgYmVjYXVzZSB0aGUgSGVzc2lhbiBvZiBhbiBuLXBhcmFtZXRlciBtb2RlbCByZXF1aXJlcyBPKG7Csikgc3RvcmFnZSBhbmQgTyhuwrMpIGludmVyc2lvbiDigJQgcHJvaGliaXRpdmUgZm9yIG4gPSAxMOKBtyBvciBtb3JlLiBUaGlzIG5vdGUgY292ZXJzIE5ld3RvbidzIG1ldGhvZCBhbmQgaXRzIGNvbnZlcmdlbmNlIGd1YXJhbnRlZXMsIHRoZSBCRkdTIGFuZCBMLUJGR1MgcXVhc2ktTmV3dG9uIGFwcHJveGltYXRpb25zLCB0aGUgR2F1c3MtTmV3dG9uIGFwcHJveGltYXRpb24gZm9yIGxlYXN0IHNxdWFyZXMsIGFuZCBLLUZBQyBhcyB0aGUgc3RhdGUtb2YtdGhlLWFydCBwcmFjdGljYWwgc2Vjb25kLW9yZGVyIG1ldGhvZCBmb3IgbmV1cmFsIG5ldHdvcmtzLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk5ld3RvbidzIE1ldGhvZCJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIk5ld3RvbidzIHVwZGF0ZSBpcyB4IOKGkCB4IOKIkiBI4oG7wrniiIdmLCB3aGVyZSBIID0g4oiHwrJmIGlzIHRoZSBIZXNzaWFuLiBUaGUgaW50dWl0aW9uOiB0aGUgc2Vjb25kLW9yZGVyIFRheWxvciBleHBhbnNpb24gZih4K860KSDiiYggZih4KSArIOKIh2bhtYDOtCArIMK9zrThtYBIzrQgaXMgYSBxdWFkcmF0aWMgaW4gzrQ7IG1pbmltaXppbmcgb3ZlciDOtCBnaXZlcyDOtCogPSDiiJJI4oG7wrniiIdmLCB3aGljaCBpcyB0aGUgTmV3dG9uIGRpcmVjdGlvbi4gRm9yIGEgcXVhZHJhdGljIG9iamVjdGl2ZSwgdGhpcyBzdGVwIGhpdHMgdGhlIG1pbmltdW0gZXhhY3RseSBpbiBvbmUgaXRlcmF0aW9uICh0aGUgcXVhZHJhdGljIG1vZGVsIGlzIGV4YWN0KS4gTmVhciBhIG1pbmltdW0sIE5ld3RvbidzIG1ldGhvZCBleGhpYml0cyBxdWFkcmF0aWMgY29udmVyZ2VuY2U6IGlmIM61X3QgPSDigJZ4X3Qg4oiSIHgq4oCWLCB0aGVuIM61X3t0KzF9IOKJpCBDwrfOtV90wrIuIFRoaXMgbWVhbnMgaWYgeW91IGFyZSB3aXRoaW4gMC4xIG9mIHRoZSBzb2x1dGlvbiwgYWZ0ZXIgb25lIHN0ZXAgeW91IGFyZSB3aXRoaW4gMC4wMTsgYWZ0ZXIgdHdvIHN0ZXBzLCAwLjAwMDEuIFJlcXVpcmVtZW50czogSCBtdXN0IGJlIHBvc2l0aXZlIGRlZmluaXRlIChQRCkgdG8gZ3VhcmFudGVlIGEgZGVzY2VudCBkaXJlY3Rpb24uIE5lYXIgYSBzYWRkbGUgcG9pbnQgKEggaXMgaW5kZWZpbml0ZSksIEjigbvCueKIh2YgbWF5IHBvaW50IHVwaGlsbC4gRml4OiBkYW1wZWQgTmV3dG9uIHVzZXMgKEggKyDOu0kp4oG7wrniiIdmIHdpdGggzrsgPiAwIGxhcmdlIGVub3VnaCB0byBtYWtlIEggKyDOu0kgUEQgKHRydXN0LXJlZ2lvbiByZWd1bGFyaXphdGlvbikuIENvc3Q6IE8obsKyKSB0byBzdG9yZSB0aGUgSGVzc2lhbiwgTyhuwrMpIHRvIGNvbXB1dGUgaXRzIGludmVyc2Ug4oCUIGNvbXBsZXRlbHkgaW5mZWFzaWJsZSBmb3IgbiA9IDEw4oG2KyBwYXJhbWV0ZXIgbW9kZWxzLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBOZXd0b24ncyBtZXRob2Qgb24gMkQgcXVhZHJhdGljIGYgPSB4XjIgKyA1eV4yIChjb252ZXJnZXMgaW4gMSBzdGVwKVxuIyBhbmQgUm9zZW5icm9jayBmID0gKDEteCleMiArIDEwMCh5LXheMileMiAoc2hvd3MgcXVhZHJhdGljIGNvbnZlcmdlbmNlKVxuZGVmIHJvc2VuYnJvY2soeHkpOlxuICAgIHgsIHkgPSB4eVxuICAgIHJldHVybiAoMSAtIHgpKioyICsgMTAwICogKHkgLSB4KioyKSoqMlxuXG5kZWYgcm9zZW5icm9ja19ncmFkKHh5KTpcbiAgICB4LCB5ID0geHlcbiAgICByZXR1cm4gbnAuYXJyYXkoWy0yKigxLXgpIC0gNDAwKngqKHkteCoqMiksXG4gICAgICAgICAgICAgICAgICAgICAgMjAwKih5LXgqKjIpXSlcblxuZGVmIHJvc2VuYnJvY2tfaGVzcyh4eSk6XG4gICAgeCwgeSA9IHh5XG4gICAgcmV0dXJuIG5wLmFycmF5KFtbMiAtIDQwMCooeS14KioyKSArIDgwMCp4KioyLCAtNDAwKnhdLFxuICAgICAgICAgICAgICAgICAgICAgWy00MDAqeCwgMjAwLjBdXSlcblxuZGVmIG5ld3Rvbl9tZXRob2QoZiwgZ3JhZF9mLCBoZXNzX2YsIHgwLCBtYXhfaXRlcj0yMCwgdG9sPTFlLTEwKTpcbiAgICB4ID0geDAuY29weSgpXG4gICAgaGlzdG9yeSA9IFtdXG4gICAgZm9yIGkgaW4gcmFuZ2UobWF4X2l0ZXIpOlxuICAgICAgICBnID0gZ3JhZF9mKHgpXG4gICAgICAgIEggPSBoZXNzX2YoeClcbiAgICAgICAgSF9yZWcgPSBIICsgMWUtNiAqIG5wLmV5ZShsZW4oeCkpICAjIGRhbXBpbmcgZm9yIG51bWVyaWNhbCBzdGFiaWxpdHlcbiAgICAgICAgZGVsdGEgPSBucC5saW5hbGcuc29sdmUoSF9yZWcsIGcpXG4gICAgICAgIHggPSB4IC0gZGVsdGFcbiAgICAgICAgZXJyID0gbnAubGluYWxnLm5vcm0oZylcbiAgICAgICAgaGlzdG9yeS5hcHBlbmQoZXJyKVxuICAgICAgICBpZiBlcnIgPCB0b2w6IGJyZWFrXG4gICAgICAgIHByaW50KGZcIiAgaXRlciB7aSsxfTog4oCW4oiHZuKAliA9IHtlcnI6LjJlfVwiKVxuICAgIHJldHVybiB4LCBoaXN0b3J5XG5cbnByaW50KFwiTmV3dG9uIG9uIFJvc2VuYnJvY2s6XCIpXG54X29wdCwgaGlzdCA9IG5ld3Rvbl9tZXRob2Qocm9zZW5icm9jaywgcm9zZW5icm9ja19ncmFkLCByb3NlbmJyb2NrX2hlc3MsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIHgwPW5wLmFycmF5KFstMS4wLCAxLjBdKSlcbnByaW50KGZcIlNvbHV0aW9uOiB7eF9vcHQucm91bmQoNil9IChleHBlY3RlZCBbMSwgMV0pXCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQkZHUzogUXVhc2ktTmV3dG9uIEFwcHJveGltYXRpb24ifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJCRkdTIChCcm95ZGVuLUZsZXRjaGVyLUdvbGRmYXJiLVNoYW5ubywgMTk3MCkgYXBwcm94aW1hdGVzIHRoZSBpbnZlcnNlIEhlc3NpYW4gZnJvbSBncmFkaWVudCBkaWZmZXJlbmNlcywgYXZvaWRpbmcgdGhlIE8obsKyKSBjb3N0IG9mIGNvbXB1dGluZyB0aGUgdHJ1ZSBIZXNzaWFuLiBBZnRlciBzdGVwIHQsIGRlZmluZSBz4oKcID0gzrjigpwg4oiSIM644oKc4oKL4oKBIChwYXJhbWV0ZXIgY2hhbmdlKSBhbmQgeeKCnCA9IOKIh2YozrjigpwpIOKIkiDiiIdmKM644oKc4oKL4oKBKSAoZ3JhZGllbnQgY2hhbmdlKS4gQkZHUyBwZXJmb3JtcyBhIHJhbmstMiB1cGRhdGU6IELigpzigorigoHigbvCuSA9IChJIOKIkiDPgeKCnHPigpx54oKc4bWAKULigpzigbvCuShJIOKIkiDPgeKCnHnigpxz4oKc4bWAKSArIM+B4oKcc+KCnHPigpzhtYAgd2hlcmUgz4HigpwgPSAxLyh54oKc4bWAc+KCnCkuIFRoZSB1cGRhdGUgc2F0aXNmaWVzIHRoZSBzZWNhbnQgY29uZGl0aW9uOiBC4oKc4oKK4oKBc+KCnCA9IHnigpwgKHRoZSBhcHByb3hpbWF0ZSBIZXNzaWFuIHRpbWVzIHRoZSBzdGVwIGVxdWFscyB0aGUgZ3JhZGllbnQgY2hhbmdlIOKAlCBsaWtlIGEgZGlzY3JldGUgc2Vjb25kIGRlcml2YXRpdmUpLiBCRkdTIGFjaGlldmVzIHN1cGVybGluZWFyIGNvbnZlcmdlbmNlOiDigJZ4X3t0KzF9IOKIkiB4KuKAliAvIOKAlnjigpwg4oiSIHgq4oCWIOKGkiAwLCBmYXN0ZXIgdGhhbiBsaW5lYXIgYnV0IHNsb3dlciB0aGFuIHF1YWRyYXRpYy4gTWVtb3J5OiBPKG7CsikgZm9yIHRoZSBmdWxsIGludmVyc2UgSGVzc2lhbiBhcHByb3hpbWF0aW9uIOKAlCBzdGlsbCBpbXByYWN0aWNhbCBmb3IgbGFyZ2UgbiwgbW90aXZhdGluZyB0aGUgbGltaXRlZC1tZW1vcnkgdmFyaWFudCBMLUJGR1MuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5vcHRpbWl6ZSBpbXBvcnQgbWluaW1pemVcbmltcG9ydCB0aW1lXG5cbmRlZiBjb252ZXhfb2JqZWN0aXZlKHcsIFgsIHkpOlxuICAgIFwiXCJcIkxvZ2lzdGljIHJlZ3Jlc3Npb24gbG9zcyAoY29udmV4LCBzbW9vdGgg4oCUIGdvb2QgZm9yIEwtQkZHUykuXCJcIlwiXG4gICAgbG9naXRzID0gWCBAIHdcbiAgICByZXR1cm4gbnAubWVhbihucC5sb2coMSArIG5wLmV4cCgteSAqIGxvZ2l0cykpKSArIDAuMDEgKiBucC5kb3QodywgdylcblxuZGVmIGNvbnZleF9ncmFkKHcsIFgsIHkpOlxuICAgIGxvZ2l0cyA9IFggQCB3XG4gICAgc2lnID0gMSAvICgxICsgbnAuZXhwKHkgKiBsb2dpdHMpKVxuICAgIHJldHVybiAtbnAubWVhbih5WzosIE5vbmVdICogWCAqIHNpZ1s6LCBOb25lXSwgYXhpcz0wKSArIDAuMDIgKiB3XG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubiwgZCA9IDUwMCwgNTBcblggPSBucC5yYW5kb20ucmFuZG4obiwgZClcbndfdHJ1ZSA9IG5wLnJhbmRvbS5yYW5kbihkKSAqIDAuNVxueSA9IG5wLnNpZ24oWCBAIHdfdHJ1ZSArIDAuMSAqIG5wLnJhbmRvbS5yYW5kbihuKSlcbncwID0gbnAuemVyb3MoZClcblxuIyBHRCBiYXNlbGluZVxuZGVmIHJ1bl9nZChzdGVwcz01MDAsIGxyPTAuMSk6XG4gICAgdyA9IHcwLmNvcHkoKVxuICAgIGxvc3NlcyA9IFtdXG4gICAgZm9yIF8gaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICBnID0gY29udmV4X2dyYWQodywgWCwgeSlcbiAgICAgICAgdyAtPSBsciAqIGdcbiAgICAgICAgbG9zc2VzLmFwcGVuZChjb252ZXhfb2JqZWN0aXZlKHcsIFgsIHkpKVxuICAgIHJldHVybiBsb3NzZXNbLTFdLCBsZW4obG9zc2VzKVxuXG4jIEwtQkZHUyB2aWEgc2NpcHlcbnQwID0gdGltZS50aW1lKClcbnJlc19sYmZncyA9IG1pbmltaXplKGNvbnZleF9vYmplY3RpdmUsIHcwLCBqYWM9Y29udmV4X2dyYWQsIGFyZ3M9KFgsIHkpLCBtZXRob2Q9J0wtQkZHUy1CJylcbnRfbGJmZ3MgPSB0aW1lLnRpbWUoKSAtIHQwXG5nZF9maW5hbCwgZ2RfaXRlcnMgPSBydW5fZ2QoKVxucHJpbnQoZlwiR0QgKDUwMCBpdGVycyk6IGZpbmFsIGxvc3MgPSB7Z2RfZmluYWw6LjZmfVwiKVxucHJpbnQoZlwiTC1CRkdTICh7cmVzX2xiZmdzLm5pdH0gaXRlcnMpOiBmaW5hbCBsb3NzID0ge3Jlc19sYmZncy5mdW46LjZmfSwgdGltZSA9IHt0X2xiZmdzOi4zZn1zXCIpXG5wcmludChmXCJMLUJGR1MgaXMge2dkX2l0ZXJzIC8vIHJlc19sYmZncy5uaXR9eCBtb3JlIGl0ZXJhdGlvbi1lZmZpY2llbnRcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJMLUJGR1M6IExpbWl0ZWQgTWVtb3J5IFZhcmlhbnQifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJMLUJGR1MgKExpdSBhbmQgTm9jZWRhbCwgMTk4OSkgc3RvcmVzIG9ubHkgdGhlIGxhc3QgbSA9IDEwIHRvIDIwIChz4oKcLCB54oKcKSBwYWlycyBpbnN0ZWFkIG9mIHRoZSBmdWxsIGludmVyc2UgSGVzc2lhbiBhcHByb3hpbWF0aW9uLiBUaGUgSGVzc2lhbi12ZWN0b3IgcHJvZHVjdCBC4oKc4oG7wrnCt2cgaXMgY29tcHV0ZWQgdmlhIHRoZSB0d28tbG9vcCByZWN1cnNpb24g4oCUIGEgc2VxdWVudGlhbCBhbGdvcml0aG0gb3ZlciB0aGUgc3RvcmVkIHBhaXJzIOKAlCBpbiBPKG1uKSB0aW1lIHBlciBpdGVyYXRpb24gaW5zdGVhZCBvZiBPKG7CsikuIFRvdGFsIG1lbW9yeTogTyhtbikgaW5zdGVhZCBvZiBPKG7CsikuIEZvciBtID0gMjAgYW5kIG4gPSAxMOKBtiwgdGhpcyBpcyAyMCDDlyAxMOKBtiBmbG9hdHMgKDE2MCBNQikgdmVyc3VzIDEwwrnCsiBmbG9hdHMgZm9yIHRoZSBmdWxsIEhlc3NpYW4g4oCUIGEgbWlsbGlvbi1mb2xkIHJlZHVjdGlvbi4gTC1CRkdTIGlzIHRoZSBzdGFuZGFyZCBvcHRpbWl6ZXIgZm9yIGxhcmdlLXNjYWxlIGNvbnZleCBvcHRpbWl6YXRpb24gb3V0c2lkZSBkZWVwIGxlYXJuaW5nOiBMaWJMaW5lYXIgdXNlcyBMLUJGR1MgZm9yIGxvZ2lzdGljIHJlZ3Jlc3Npb24sIHNjaWtpdC1sZWFybidzIExvZ2lzdGljUmVncmVzc2lvbiB3aXRoIHNvbHZlcj0nbGJmZ3MnIHVzZXMgaXQsIGFuZCBtb3N0IHNjaWVudGlmaWMgY29tcHV0aW5nIGxpYnJhcmllcyBwcm92aWRlIEwtQkZHUy1CICh3aXRoIGJveCBjb25zdHJhaW50cykuIEluIFB5VG9yY2g6IHRvcmNoLm9wdGltLkxCRkdTIHJlcXVpcmVzIGEgY2xvc3VyZSB0aGF0IHJlLWV2YWx1YXRlcyBhbmQgcmV0dXJucyB0aGUgbG9zcyAobmVlZGVkIGZvciBsaW5lIHNlYXJjaCk7IGl0IGRvZXMgTk9UIHdvcmsgd2VsbCB3aXRoIG1pbmktYmF0Y2hlcyBiZWNhdXNlIHRoZSBzZWNhbnQgY29uZGl0aW9uIHnigpzhtYBz4oKcID4gMCByZXF1aXJlcyBjb25zaXN0ZW50IGdyYWRpZW50IGVzdGltYXRlcywgd2hpY2ggcmFuZG9tIG1pbmktYmF0Y2hlcyB2aW9sYXRlLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkdhdXNzLU5ld3RvbiBhbmQgSy1GQUMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJGb3IgbGVhc3Qgc3F1YXJlcyBmID0gwr3igJZyKM64KeKAlsKyIHdoZXJlIHIozrgpIGlzIGEgcmVzaWR1YWwgdmVjdG9yLCB0aGUgSGVzc2lhbiBpcyBIID0gSuG1gEogKyDOo+G1oiBy4bWi4oiHwrJy4bWiIOKJiCBK4bWASiAoR2F1c3MtTmV3dG9uIGFwcHJveGltYXRpb24sIGRyb3BwaW5nIHRoZSBzZWNvbmQtZGVyaXZhdGl2ZSB0ZXJtcykuIFRoZSBHYXVzcy1OZXd0b24gdXBkYXRlIM64IOKGkCDOuCDiiJIgKErhtYBKKeKBu8K5SuG1gHIgaXMgZXF1aXZhbGVudCB0byBzb2x2aW5nIGEgbG9jYWwgbGluZWFyaXplZCBsZWFzdCBzcXVhcmVzIHByb2JsZW0uIErhtYBKIGlzIFBTRCBieSBjb25zdHJ1Y3Rpb24gKG5vIGluZGVmaW5pdGUgSCBpc3N1ZXMpLCBhbmQgZm9yIHNtYWxsIHJlc2lkdWFscyB0aGUgYXBwcm94aW1hdGlvbiBpcyB0aWdodC4gSy1GQUMgKEtyb25lY2tlci1GYWN0b3JlZCBBcHByb3hpbWF0ZSBDdXJ2YXR1cmUsIE1hcnRlbnMgYW5kIEdyb3NzZSAyMDE1KSBhcHByb3hpbWF0ZXMgdGhlIEZpc2hlciBpbmZvcm1hdGlvbiBtYXRyaXggRiAod2hpY2ggZXF1YWxzIHRoZSBIZXNzaWFuIGZvciBjcm9zcy1lbnRyb3B5IGxvc3MgdW5kZXIgdGhlIG1vZGVsJ3Mgb3duIGRpc3RyaWJ1dGlvbikgdXNpbmcgdGhlIEtyb25lY2tlciBzdHJ1Y3R1cmUgb2YgbGluZWFyIGxheWVycy4gRm9yIGEgbGluZWFyIGxheWVyIHkgPSBXeCB3aXRoIGlucHV0IHggYW5kIG91dHB1dCBncmFkaWVudCDOtCwgSy1GQUMgYXBwcm94aW1hdGVzIEZfVyDiiYggQSDiipcgRyB3aGVyZSBBID0gRVt4eOG1gF0gKGlucHV0IGNvdmFyaWFuY2UsIHNpemUgZF9pbiDDlyBkX2luKSBhbmQgRyA9IEVbzrTOtOG1gF0gKG91dHB1dCBncmFkaWVudCBjb3ZhcmlhbmNlLCBzaXplIGRfb3V0IMOXIGRfb3V0KS4gVGhlIGludmVyc2UgRl9X4oG7wrkg4omIIEHigbvCuSDiipcgR+KBu8K5IHZpYSB0aGUgS3JvbmVja2VyIHByb2R1Y3QgcnVsZSAoQeKKl0Ip4oG7wrkgPSBB4oG7wrniipdC4oG7wrkuIFRoaXMgZ2l2ZXMgTyhkX2luwrIgKyBkX291dMKyKSBwZXIgbGF5ZXIgaW5zdGVhZCBvZiBPKChkX2luwrdkX291dCnCsiksIG1ha2luZyBLLUZBQyBwcmFjdGljYWwgZm9yIG5ldHdvcmtzIHdpdGggbW9kZXJhdGUtd2lkdGggbGF5ZXJzLiBLLUZBQyBhY2hpZXZlcyBBZGFtLWNvbXBhcmFibGUgY29udmVyZ2VuY2Ugd2l0aCBmZXdlciBzdGVwcywgYXQgdGhlIGNvc3Qgb2YgbW9yZSBjb21wdXRlIHBlciBzdGVwLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0aW1lXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5uLCBkX2luLCBkX291dCA9IDIwMCwgMjAsIDFcblggPSB0b3JjaC5yYW5kbihuLCBkX2luKVxudHJ1ZV93ID0gdG9yY2gucmFuZG4oZF9pbiwgZF9vdXQpXG55ID0gWCBAIHRydWVfdyArIDAuMSAqIHRvcmNoLnJhbmRuKG4sIGRfb3V0KVxuXG5kZWYgbWFrZV9tb2RlbCgpOlxuICAgIHJldHVybiBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkX2luLCAxMCksIG5uLlRhbmgoKSwgbm4uTGluZWFyKDEwLCBkX291dCkpXG5cbmRlZiB0cmFpbl9sYmZncyhtb2RlbCwgWCwgeSwgbWF4X2l0ZXI9MTAwKTpcbiAgICBvcHRpbWl6ZXIgPSBvcHRpbS5MQkZHUyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTAuNSwgbWF4X2l0ZXI9bWF4X2l0ZXIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxpbmVfc2VhcmNoX2ZuPSdzdHJvbmdfd29sZmUnKVxuICAgIGxvc3NfZm4gPSBubi5NU0VMb3NzKClcbiAgICBkZWYgY2xvc3VyZSgpOlxuICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgbG9zcyA9IGxvc3NfZm4obW9kZWwoWCksIHkpXG4gICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICByZXR1cm4gbG9zc1xuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBvcHRpbWl6ZXIuc3RlcChjbG9zdXJlKVxuICAgIHJldHVybiBsb3NzX2ZuKG1vZGVsKFgpLCB5KS5pdGVtKCksIHRpbWUudGltZSgpIC0gdDBcblxuZGVmIHRyYWluX2FkYW0obW9kZWwsIFgsIHksIHN0ZXBzPTUwMCk6XG4gICAgb3B0aW1pemVyID0gb3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTAuMDEpXG4gICAgbG9zc19mbiA9IG5uLk1TRUxvc3MoKVxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBmb3IgXyBpbiByYW5nZShzdGVwcyk6XG4gICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgICAgICBsb3NzX2ZuKG1vZGVsKFgpLCB5KS5iYWNrd2FyZCgpXG4gICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICByZXR1cm4gbG9zc19mbihtb2RlbChYKSwgeSkuaXRlbSgpLCB0aW1lLnRpbWUoKSAtIHQwXG5cbmxiZmdzX2xvc3MsIGxiZmdzX3RpbWUgPSB0cmFpbl9sYmZncyhtYWtlX21vZGVsKCksIFgsIHkpXG5hZGFtX2xvc3MsIGFkYW1fdGltZSA9IHRyYWluX2FkYW0obWFrZV9tb2RlbCgpLCBYLCB5KVxucHJpbnQoZlwiTC1CRkdTOiBsb3NzPXtsYmZnc19sb3NzOi42Zn0sIHRpbWU9e2xiZmdzX3RpbWU6LjNmfXNcIilcbnByaW50KGZcIkFkYW0gKDUwMCBzdGVwcyk6IGxvc3M9e2FkYW1fbG9zczouNmZ9LCB0aW1lPXthZGFtX3RpbWU6LjNmfXNcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNTCBDb25uZWN0aW9uczogV2hlbiBTZWNvbmQtT3JkZXIgQmVhdHMgQWRhbSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlNlY29uZC1vcmRlciBtZXRob2RzIGJlYXQgQWRhbSBpbiBzcGVjaWZpYyBzY2VuYXJpb3Mgd2hlcmUgdGhlaXIgYXNzdW1wdGlvbnMgaG9sZC4gRnVsbC1iYXRjaCB0cmFpbmluZzogd2hlbiB0aGUgZnVsbCBkYXRhc2V0IGZpdHMgaW4gbWVtb3J5IGFuZCBjb25zaXN0ZW50IGdyYWRpZW50cyBhcmUgYXZhaWxhYmxlLCBMLUJGR1MncyBzZWNhbnQgY29uZGl0aW9uIGlzIHNhdGlzZmllZCBhbmQgc3VwZXJsaW5lYXIgY29udmVyZ2VuY2UgYXBwbGllcy4gVGhpcyBjb3ZlcnMgc21hbGwgZGF0YXNldCBmaW5lLXR1bmluZywgc2NpZW50aWZpYyBNTCAocGh5c2ljcy1pbmZvcm1lZCBuZXVyYWwgbmV0d29ya3MpLCBhbmQgbmV1cmFsIG5ldHdvcmsgdmVyaWZpY2F0aW9uLiBDb252ZXggb3IgbmVhcmx5IGNvbnZleCBvYmplY3RpdmVzOiBsb2dpc3RpYyByZWdyZXNzaW9uLCBsaW5lYXIgU1ZNLCBsYXN0LWxheWVyIGZpbmUtdHVuaW5nIHdpdGggZnJvemVuIHJlcHJlc2VudGF0aW9ucyDigJQgdGhlIHF1YWRyYXRpYyBjb252ZXJnZW5jZSByZWdpbWUgaXMgYWNjZXNzaWJsZS4gU21hbGwgbW9kZWxzICh1bmRlciAxME0gcGFyYW1ldGVycyk6IHRoZSBIZXNzaWFuIG9yIGl0cyBmYWN0b3JlZCBhcHByb3hpbWF0aW9uIGlzIGNvbXB1dGFibGU7IEstRkFDIGlzIHByYWN0aWNhbCBmb3IgbW9kZWxzIHdpdGggbGF5ZXJzIHVwIHRvIHdpZHRoIDEwMDAtMjAwMC4gTmF0dXJhbCBwb2xpY3kgZ3JhZGllbnQgaW4gUkw6IEstRkFDIGFwcHJveGltYXRlcyB0aGUgRmlzaGVyIGluZm9ybWF0aW9uIG1hdHJpeCwgZ2l2aW5nIGEgcHJpbmNpcGxlZCBuYXR1cmFsIGdyYWRpZW50IHN0ZXAgdGhhdCBpcyBpbnZhcmlhbnQgdG8gcGFyYW1ldGVyIHJlcGFyYW1ldGVyaXphdGlvbiDigJQgY3JpdGljYWwgZm9yIHN0YWJsZSBwb2xpY3kgb3B0aW1pemF0aW9uLiBJbiBjb250cmFzdCwgQWRhbSBhcHByb3hpbWF0ZXMgc2Vjb25kLW9yZGVyIGluZm9ybWF0aW9uIHVzaW5nIG9ubHkgdGhlIGRpYWdvbmFsIG9mIHRoZSBGaXNoZXIgKHBlci1wYXJhbWV0ZXIgYWRhcHRpdmUgbGVhcm5pbmcgcmF0ZXMpLCBtaXNzaW5nIG9mZi1kaWFnb25hbCBjdXJ2YXR1cmUgc3RydWN0dXJlIHRoYXQgSy1GQUMgY2FwdHVyZXMuIEZvciBMTE0gcHJlLXRyYWluaW5nIHdpdGggbiA9IDfDlzEw4oG5IHBhcmFtZXRlcnMgYW5kIHN0b2NoYXN0aWMgZ3JhZGllbnRzLCBzZWNvbmQtb3JkZXIgbWV0aG9kcyByZW1haW4gaW1wcmFjdGljYWw6IGV2ZW4gSy1GQUMncyBwZXItbGF5ZXIgY29zdCBleGNlZWRzIEdQVSBtZW1vcnksIGFuZCBtaW5pLWJhdGNoIGdyYWRpZW50cyB2aW9sYXRlIHRoZSBzZWNhbnQgY29uZGl0aW9uLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5pbXBvcnQgdGltZVxuXG5ucC5yYW5kb20uc2VlZCgxKVxubl9zYW1wbGVzLCBuX2ZlYXR1cmVzID0gMTAwMCwgMzBcblhfbnAgPSBucC5yYW5kb20ucmFuZG4obl9zYW1wbGVzLCBuX2ZlYXR1cmVzKVxud190cnVlID0gbnAucmFuZG9tLnJhbmRuKG5fZmVhdHVyZXMpXG55X25wID0gWF9ucCBAIHdfdHJ1ZSArIDAuMSAqIG5wLnJhbmRvbS5yYW5kbihuX3NhbXBsZXMpXG5cbmRlZiBtc2VfbG9zcyh3KTogcmV0dXJuIDAuNSAqIG5wLm1lYW4oKFhfbnAgQCB3IC0geV9ucCkqKjIpICsgMC4wMSAqIG5wLmRvdCh3LCB3KVxuZGVmIG1zZV9ncmFkKHcpOiByZXR1cm4gWF9ucC5UIEAgKFhfbnAgQCB3IC0geV9ucCkgLyBuX3NhbXBsZXMgKyAwLjAyICogd1xuXG4jIEdyYWRpZW50IGRlc2NlbnRcbmRlZiBydW5fZ2RfbnAobHI9MC4xLCBzdGVwcz0xMDAwKTpcbiAgICB3ID0gbnAuemVyb3Mobl9mZWF0dXJlcylcbiAgICBsb3NzZXMgPSBbbXNlX2xvc3ModyldXG4gICAgZm9yIF8gaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICB3IC09IGxyICogbXNlX2dyYWQodylcbiAgICAgICAgbG9zc2VzLmFwcGVuZChtc2VfbG9zcyh3KSlcbiAgICByZXR1cm4gdywgbG9zc2VzXG5cbnQwID0gdGltZS50aW1lKCk7IHdfZ2QsIGxvc3Nlc19nZCA9IHJ1bl9nZF9ucCgpOyB0X2dkID0gdGltZS50aW1lKCkgLSB0MFxuXG4jIEwtQkZHU1xudDAgPSB0aW1lLnRpbWUoKVxucmVzID0gbWluaW1pemUobXNlX2xvc3MsIG5wLnplcm9zKG5fZmVhdHVyZXMpLCBqYWM9bXNlX2dyYWQsIG1ldGhvZD0nTC1CRkdTLUInKVxudF9sYmZncyA9IHRpbWUudGltZSgpIC0gdDBcblxucHJpbnQoZlwiR0QgKDEwMDAgc3RlcHMpOiBmaW5hbCBsb3NzID0ge2xvc3Nlc19nZFstMV06LjZmfSwgdGltZSA9IHt0X2dkOi4zZn1zXCIpXG5wcmludChmXCJMLUJGR1MgKHtyZXMubml0fSBpdGVycyk6IGZpbmFsIGxvc3MgPSB7cmVzLmZ1bjouNmZ9LCB0aW1lID0ge3RfbGJmZ3M6LjNmfXNcIilcbnByaW50KGZcIlNvbHV0aW9uIHF1YWxpdHkg4oCUIEdEOiB7bnAubGluYWxnLm5vcm0od19nZCAtIHdfdHJ1ZSk6LjRmfSwgXCJcbiAgICAgIGZcIkwtQkZHUzoge25wLmxpbmFsZy5ub3JtKHJlcy54IC0gd190cnVlKTouNGZ9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiSW1wbGVtZW50YXRpb24gUGl0ZmFsbHMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJGb3VyIGNyaXRpY2FsIHBpdGZhbGxzIHdpdGggc2Vjb25kLW9yZGVyIG1ldGhvZHMgaW4gcHJhY3RpY2UuIEZpcnN0LCB1c2luZyBMLUJGR1Mgd2l0aCBtaW5pLWJhdGNoZXM6IHRoZSBzZWNhbnQgY29uZGl0aW9uIHJlcXVpcmVzIHnigpzhtYBz4oKcID4gMCAocG9zaXRpdmUgY3VydmF0dXJlIGFsb25nIHRoZSBzdGVwKS4gV2hlbiBncmFkaWVudHMgYXJlIGNvbXB1dGVkIG9uIGRpZmZlcmVudCByYW5kb20gbWluaS1iYXRjaGVzIGF0IHN1Y2Nlc3NpdmUgc3RlcHMsIHnigpwgYW5kIHPigpwgYXJlIGNvbXB1dGVkIGZyb20gZGlmZmVyZW50IGRhdGEgZGlzdHJpYnV0aW9ucywgY2F1c2luZyB54oKc4bWAc+KCnCA8IDAgZnJlcXVlbnRseSDigJQgdGhlIGludmVyc2UgSGVzc2lhbiBhcHByb3hpbWF0aW9uIGJlY29tZXMgaW5kZWZpbml0ZSwgYW5kIEwtQkZHUyBkaXZlcmdlcyBvciBtYWtlcyB2ZXJ5IHBvb3IgdXBkYXRlcy4gQWx3YXlzIHVzZSBMLUJGR1Mgd2l0aCBmdWxsLWJhdGNoIG9yIHZlcnkgbGFyZ2UgYmF0Y2hlcyBvbmx5LiBTZWNvbmQsIGZvcmdldHRpbmcgdGhlIGNsb3N1cmUgaW4gUHlUb3JjaDogdG9yY2gub3B0aW0uTEJGR1MgcmVxdWlyZXMgYSBjbG9zdXJlIGZ1bmN0aW9uIHRoYXQgemVyb2VzIGdyYWRpZW50cywgcGVyZm9ybXMgdGhlIGZvcndhcmQgcGFzcywgYW5kIHJldHVybnMgdGhlIGxvc3Mg4oCUIHdpdGhvdXQgdGhpcywgdGhlIGxpbmUgc2VhcmNoIGhhcyBubyB3YXkgdG8gZXZhbHVhdGUgdGhlIG9iamVjdGl2ZSBhbmQgd2lsbCB1c2UgYSBmaXhlZCBzdGVwIHNpemUgKGRlZ3JhZGluZyB0byBHRCkuIFRoaXJkLCBtZW1vcnkgb3ZlcmZsb3cgd2l0aCBtIHRvbyBsYXJnZTogc2V0dGluZyBtYXhfaGlzdG9yeSAobSkgdG8gMTAwIG9yIDIwMCB1c2VzIDEwMC0yMDAgdGltZXMgbW9yZSBtZW1vcnkgdGhhbiBhIHNpbmdsZSBncmFkaWVudCB2ZWN0b3Ig4oCUIGtlZXAgbSBiZXR3ZWVuIDEwIGFuZCAzMC4gRm91cnRoLCBpZ25vcmluZyBIJ3MgaW5kZWZpbml0ZW5lc3MgbmVhciBzYWRkbGVzOiBpZiDOu19taW4oSCkgPCAwLCBI4oG7wrniiIdmIG1heSBwb2ludCB0byBhIGhpZ2hlciBmdW5jdGlvbiB2YWx1ZS4gQWRkIGRhbXBpbmc6IHVzZSAoSCArIM67SSnigbvCueKIh2Ygd2l0aCDOuyA9IG1heCgwLCDiiJLOu19taW4oSCkpICsgzrUuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUHJhY3RpY2FsIEd1aWRhbmNlIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiRGVjaXNpb24gZ3VpZGUgZm9yIHNlY29uZC1vcmRlciBtZXRob2RzIGluIHByYWN0aWNlLiBVc2UgTC1CRkdTIHdoZW46ICgxKSB0aGUgZGF0YXNldCBmaXRzIGVudGlyZWx5IGluIG1lbW9yeSAobiDiiaQgMTDigbYgc2FtcGxlcyk7ICgyKSB0aGUgb2JqZWN0aXZlIGlzIHNtb290aCBhbmQgY29udmV4IG9yIG5lYXJseSBjb252ZXg7ICgzKSB5b3UgbmVlZCBoaWdoIHByZWNpc2lvbiAoc2NpZW50aWZpYyBjb21wdXRpbmcsIG5ldXJhbCBuZXR3b3JrIHZlcmlmaWNhdGlvbik7ICg0KSB5b3UgYXJlIGRvaW5nIGZ1bGwtYmF0Y2ggZmluZS10dW5pbmcgb2YgdGhlIGxhc3QgbGF5ZXIgb25seS4gVXNlIEstRkFDIHdoZW46IHRyYWluaW5nIGEgbW9kZXJhdGVseS1zaXplZCBtb2RlbCAoMTBNLTEwME0gcGFyYW1ldGVycykgd2hlcmUgSy1GQUMncyBwZXItbGF5ZXIgZmFjdG9yZWQgRmlzaGVyIGlzIGNvbXB1dGFibGUsIGFuZCB5b3Ugd2FudCBmYXN0ZXIgY29udmVyZ2VuY2UgdGhhbiBBZGFtIHdpdGggZmV3ZXIgdG90YWwgc3RlcHMgKGFjY2VwdGluZyBtb3JlIGNvbXB1dGUgcGVyIHN0ZXApLiBVc2UgQWRhbSBldmVyeXdoZXJlIGVsc2U6IHN0b2NoYXN0aWMgdHJhaW5pbmcsIGxhcmdlIG1vZGVscywgbm9uLXNtb290aCBvYmplY3RpdmVzLiBXaGVuIHVzaW5nIHRvcmNoLm9wdGltLkxCRkdTIGluIFB5VG9yY2gsIHNldCBsaW5lX3NlYXJjaF9mbj0nc3Ryb25nX3dvbGZlJyBmb3IgYXV0b21hdGljIHN0ZXAgc2l6ZSBzZWxlY3Rpb24sIGFuZCBzZXQgaGlzdG9yeV9zaXplPTIwICh0aGUgbSBwYXJhbWV0ZXIpLiBNb25pdG9yIHRoZSBjbG9zdXJlIGJlaW5nIGNhbGxlZCBtdWx0aXBsZSB0aW1lcyBwZXIgc3RlcCAodGhpcyBpcyBub3JtYWwg4oCUIEwtQkZHUydzIGxpbmUgc2VhcmNoIG1ha2VzIG11bHRpcGxlIGZ1bmN0aW9uIGV2YWx1YXRpb25zIHRvIGZpbmQgdGhlIG9wdGltYWwgc3RlcCBzaXplIGFsb25nIHRoZSBOZXd0b24gZGlyZWN0aW9uKS4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidGl0bGUiOiAiV2FybmluZyIsICJjb250ZW50IjogIkwtQkZHUyByZXF1aXJlcyBhIGNsb3N1cmUgdGhhdCByZS1ldmFsdWF0ZXMgdGhlIGxvc3MsIGFuZCB0aGUgbG9zcyBtdXN0IGJlIGNvbXB1dGVkIG9uIHRoZSBTQU1FIGRhdGEgZXZlcnkgdGltZSAobm8gcmFuZG9tIHNhbXBsaW5nIHdpdGhpbiB0aGUgY2xvc3VyZSkuIFVzaW5nIHJhbmRvbSBtaW5pLWJhdGNoZXMgaW4gdGhlIGNsb3N1cmUgY2F1c2VzIHRoZSBzZWNhbnQgY29uZGl0aW9uIHnigpzhtYBz4oKcID4gMCB0byBmYWlsLCBwcm9kdWNpbmcgbmVnYXRpdmUgY3VydmF0dXJlIGVzdGltYXRlcyBhbmQgZGl2ZXJnZW5jZSBvciB3aWxkbHkgaW5jb3JyZWN0IHVwZGF0ZXMuIEZvciBtaW5pLWJhdGNoIHRyYWluaW5nLCBhbHdheXMgdXNlIEFkYW0gb3IgU0dEIHdpdGggbW9tZW50dW0uIE9ubHkgc3dpdGNoIHRvIEwtQkZHUyBmb3IgZnVsbC1iYXRjaCBmaW5lLXR1bmluZywgc21hbGwgZGF0YXNldCBwcm9ibGVtcywgb3IgYWZ0ZXIgdHJhaW5pbmcgd2l0aCBBZGFtIHdoZW4geW91IHdhbnQgdG8gc3F1ZWV6ZSBvdXQgdGhlIGxhc3QgcHJlY2lzaW9uIGltcHJvdmVtZW50LiJ9LCB7InR5cGUiOiAidGFibGUiLCAiaGVhZGVycyI6IFsiTWV0aG9kIiwgIkNvbnZlcmdlbmNlIFJhdGUiLCAiTWVtb3J5IiwgIlR5cGljYWwgSXRlcmF0aW9ucyIsICJCZXN0IEZvciJdLCAicm93cyI6IFtbIkdEIiwgIkxpbmVhciBPKM66IGxvZyAxL861KSIsICJPKG4pIiwgIjEwMDAtMTAwMDAiLCAiUHJvdG90eXBlLCBiYXNlbGluZSJdLCBbIlNHRCArIE1vbWVudHVtIiwgIk8oMS90KSBzdG9jaGFzdGljIiwgIk8obikiLCAiMTAtMTAwIGVwb2NocyIsICJETCwgc3RvY2hhc3RpYyBzZXR0aW5ncyJdLCBbIkFkYW0gLyBBZGFtVyIsICJPKDEv4oiadCkgYWRhcHRpdmUiLCAiTygzbikgKHBhcmFtcyArIDIgbW9tZW50cykiLCAiMTAtNTAgZXBvY2hzIiwgIkRlZmF1bHQgREwgY2hvaWNlIl0sIFsiQkZHUyIsICJTdXBlcmxpbmVhciIsICJPKG7CsikiLCAiMjAtMTAwIiwgIk1lZGl1bSBuLCBmdWxsIGJhdGNoIl0sIFsiTC1CRkdTIiwgIlN1cGVybGluZWFyIiwgIk8obW4pLCBt4omIMjAiLCAiNTAtNTAwIiwgIkxhcmdlIG4sIGZ1bGwgYmF0Y2gsIGNvbnZleCJdLCBbIk5ld3RvbiIsICJRdWFkcmF0aWMiLCAiTyhuwrIpICsgTyhuwrMpIGludmVydCIsICI1LTIwIiwgIm4gPCAxMDAwLCBoaWdoIHByZWNpc2lvbiJdLCBbIkstRkFDIiwgIk5lYXItcXVhZHJhdGljIHBlciBsYXllciIsICJPKM6jKGRfaW7CsiArIGRfb3V0wrIpKSIsICIyLTXDlyBmZXdlciB0aGFuIEFkYW0iLCAiTW9kZXJhdGUgREwgbW9kZWxzLCBSTCJdXX0sIHsidHlwZSI6ICJkaXZpZGVyIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2V5IFRha2Vhd2F5cyJ9LCB7InR5cGUiOiAibGlzdCIsICJpdGVtcyI6IFsiTmV3dG9uJ3MgbWV0aG9kIHVwZGF0ZSB4IOKGkCB4IOKIkiBI4oG7wrniiIdmIGNvbnZlcmdlcyBxdWFkcmF0aWNhbGx5IG5lYXIgYSBtaW5pbXVtOiB0aGUgZXJyb3IgzrUgc2F0aXNmaWVzIM61X3t0KzF9IOKJpCBDwrfOtV90wrIsIGRvdWJsaW5nIHRoZSBudW1iZXIgb2YgY29ycmVjdCBkaWdpdHMgcGVyIHN0ZXAuIiwgIk5ld3RvbiByZXF1aXJlcyBPKG7CsikgbWVtb3J5IGFuZCBPKG7CsykgaW52ZXJzaW9uIOKAlCBpbmZlYXNpYmxlIGZvciBuID4gMTDigbU7IGRhbXBlZCBOZXd0b24gYWRkcyDOu0kgdG8gSCBmb3Igc3RhYmlsaXR5IG5lYXIgc2FkZGxlcy4iLCAiQkZHUyBhcHByb3hpbWF0ZXMgdGhlIGludmVyc2UgSGVzc2lhbiB1c2luZyByYW5rLTIgdXBkYXRlcyBmcm9tIGdyYWRpZW50IGRpZmZlcmVuY2VzIChz4oKcLCB54oKcKSwgYWNoaWV2aW5nIHN1cGVybGluZWFyIGNvbnZlcmdlbmNlIHdpdGggTyhuwrIpIG1lbW9yeS4iLCAiTC1CRkdTIHN0b3JlcyBvbmx5IHRoZSBsYXN0IG09MTAtMjAgKHPigpwsIHnigpwpIHBhaXJzLCBjb21wdXRpbmcgSGVzc2lhbi12ZWN0b3IgcHJvZHVjdHMgdmlhIHRoZSB0d28tbG9vcCByZWN1cnNpb24gaW4gTyhtbikg4oCUIHByYWN0aWNhbCBmb3IgbGFyZ2Utc2NhbGUgY29udmV4IHByb2JsZW1zLiIsICJMLUJGR1MgRkFJTFMgd2l0aCBtaW5pLWJhdGNoZXMgYmVjYXVzZSByYW5kb20gZ3JhZGllbnRzIHZpb2xhdGUgdGhlIHNlY2FudCBjb25kaXRpb24geeKCnOG1gHPigpwgPiAwOyB1c2Ugb25seSB3aXRoIGZ1bGwtYmF0Y2ggb3IgY29uc2lzdGVudCBncmFkaWVudHMuIiwgIkstRkFDIGFwcHJveGltYXRlcyB0aGUgRmlzaGVyIGluZm9ybWF0aW9uIHVzaW5nIEtyb25lY2tlciBzdHJ1Y3R1cmU6IEZfVyDiiYggQeKKl0csIGludmVydGVkIGFzIEHigbvCueKKl0figbvCuSwgcmVkdWNpbmcgcGVyLWxheWVyIGNvc3QgZnJvbSBPKChkX2luwrdkX291dCnCsikgdG8gTyhkX2luwrIgKyBkX291dMKyKS4iLCAiU2Vjb25kLW9yZGVyIG1ldGhvZHMgYmVhdCBBZGFtIGZvciBzbWFsbC10by1tZWRpdW0gc2NhbGUgZnVsbC1iYXRjaCBwcm9ibGVtczsgQWRhbSB3aW5zIGZvciBzdG9jaGFzdGljIGxhcmdlLXNjYWxlIGRlZXAgbGVhcm5pbmcuIl19XQ=="
---

# Second-Order Methods — Newton's Method and L-BFGS

Second-order optimization methods use curvature information (the Hessian matrix) in addition to gradient information to compute better update directions. Theoretically, they are dramatically superior: while gradient descent converges at a linear rate O(1/t) for strongly convex functions, Newton's method converges quadratically (number of correct digits doubles per iteration) and reaches high precision in very few steps. In practice, however, second-order methods are rarely used for deep learning because the Hessian of an n-parameter model requires O(n²) storage and O(n³) inversion — prohibitive for n = 10⁷ or more. This note covers Newton's method and its convergence guarantees, the BFGS and L-BFGS quasi-Newton approximations, the Gauss-Newton approximation for least squares, and K-FAC as the state-of-the-art practical second-order method for neural networks.

## Newton's Method

Newton's update is x ← x − H⁻¹∇f, where H = ∇²f is the Hessian. The intuition: the second-order Taylor expansion f(x+δ) ≈ f(x) + ∇fᵀδ + ½δᵀHδ is a quadratic in δ; minimizing over δ gives δ* = −H⁻¹∇f, which is the Newton direction. For a quadratic objective, this step hits the minimum exactly in one iteration (the quadratic model is exact). Near a minimum, Newton's method exhibits quadratic convergence: if ε_t = ‖x_t − x*‖, then ε_{t+1} ≤ C·ε_t². This means if you are within 0.1 of the solution, after one step you are within 0.01; after two steps, 0.0001. Requirements: H must be positive definite (PD) to guarantee a descent direction. Near a saddle point (H is indefinite), H⁻¹∇f may point uphill. Fix: damped Newton uses (H + λI)⁻¹∇f with λ > 0 large enough to make H + λI PD (trust-region regularization). Cost: O(n²) to store the Hessian, O(n³) to compute its inverse — completely infeasible for n = 10⁶+ parameter models.

```python
import numpy as np

# Newton's method on 2D quadratic f = x^2 + 5y^2 (converges in 1 step)
# and Rosenbrock f = (1-x)^2 + 100(y-x^2)^2 (shows quadratic convergence)
def rosenbrock(xy):
    x, y = xy
    return (1 - x)**2 + 100 * (y - x**2)**2

def rosenbrock_grad(xy):
    x, y = xy
    return np.array([-2*(1-x) - 400*x*(y-x**2),
                      200*(y-x**2)])

def rosenbrock_hess(xy):
    x, y = xy
    return np.array([[2 - 400*(y-x**2) + 800*x**2, -400*x],
                     [-400*x, 200.0]])

def newton_method(f, grad_f, hess_f, x0, max_iter=20, tol=1e-10):
    x = x0.copy()
    history = []
    for i in range(max_iter):
        g = grad_f(x)
        H = hess_f(x)
        H_reg = H + 1e-6 * np.eye(len(x))  # damping for numerical stability
        delta = np.linalg.solve(H_reg, g)
        x = x - delta
        err = np.linalg.norm(g)
        history.append(err)
        if err < tol: break
        print(f"  iter {i+1}: ‖∇f‖ = {err:.2e}")
    return x, history

print("Newton on Rosenbrock:")
x_opt, hist = newton_method(rosenbrock, rosenbrock_grad, rosenbrock_hess,
                             x0=np.array([-1.0, 1.0]))
print(f"Solution: {x_opt.round(6)} (expected [1, 1])")
```

## BFGS: Quasi-Newton Approximation

BFGS (Broyden-Fletcher-Goldfarb-Shanno, 1970) approximates the inverse Hessian from gradient differences, avoiding the O(n²) cost of computing the true Hessian. After step t, define sₜ = θₜ − θₜ₋₁ (parameter change) and yₜ = ∇f(θₜ) − ∇f(θₜ₋₁) (gradient change). BFGS performs a rank-2 update: Bₜ₊₁⁻¹ = (I − ρₜsₜyₜᵀ)Bₜ⁻¹(I − ρₜyₜsₜᵀ) + ρₜsₜsₜᵀ where ρₜ = 1/(yₜᵀsₜ). The update satisfies the secant condition: Bₜ₊₁sₜ = yₜ (the approximate Hessian times the step equals the gradient change — like a discrete second derivative). BFGS achieves superlinear convergence: ‖x_{t+1} − x*‖ / ‖xₜ − x*‖ → 0, faster than linear but slower than quadratic. Memory: O(n²) for the full inverse Hessian approximation — still impractical for large n, motivating the limited-memory variant L-BFGS.

```python
import numpy as np
from scipy.optimize import minimize
import time

def convex_objective(w, X, y):
    """Logistic regression loss (convex, smooth — good for L-BFGS)."""
    logits = X @ w
    return np.mean(np.log(1 + np.exp(-y * logits))) + 0.01 * np.dot(w, w)

def convex_grad(w, X, y):
    logits = X @ w
    sig = 1 / (1 + np.exp(y * logits))
    return -np.mean(y[:, None] * X * sig[:, None], axis=0) + 0.02 * w

np.random.seed(42)
n, d = 500, 50
X = np.random.randn(n, d)
w_true = np.random.randn(d) * 0.5
y = np.sign(X @ w_true + 0.1 * np.random.randn(n))
w0 = np.zeros(d)

# GD baseline
def run_gd(steps=500, lr=0.1):
    w = w0.copy()
    losses = []
    for _ in range(steps):
        g = convex_grad(w, X, y)
        w -= lr * g
        losses.append(convex_objective(w, X, y))
    return losses[-1], len(losses)

# L-BFGS via scipy
t0 = time.time()
res_lbfgs = minimize(convex_objective, w0, jac=convex_grad, args=(X, y), method='L-BFGS-B')
t_lbfgs = time.time() - t0
gd_final, gd_iters = run_gd()
print(f"GD (500 iters): final loss = {gd_final:.6f}")
print(f"L-BFGS ({res_lbfgs.nit} iters): final loss = {res_lbfgs.fun:.6f}, time = {t_lbfgs:.3f}s")
print(f"L-BFGS is {gd_iters // res_lbfgs.nit}x more iteration-efficient")
```

## L-BFGS: Limited Memory Variant

L-BFGS (Liu and Nocedal, 1989) stores only the last m = 10 to 20 (sₜ, yₜ) pairs instead of the full inverse Hessian approximation. The Hessian-vector product Bₜ⁻¹·g is computed via the two-loop recursion — a sequential algorithm over the stored pairs — in O(mn) time per iteration instead of O(n²). Total memory: O(mn) instead of O(n²). For m = 20 and n = 10⁶, this is 20 × 10⁶ floats (160 MB) versus 10¹² floats for the full Hessian — a million-fold reduction. L-BFGS is the standard optimizer for large-scale convex optimization outside deep learning: LibLinear uses L-BFGS for logistic regression, scikit-learn's LogisticRegression with solver='lbfgs' uses it, and most scientific computing libraries provide L-BFGS-B (with box constraints). In PyTorch: torch.optim.LBFGS requires a closure that re-evaluates and returns the loss (needed for line search); it does NOT work well with mini-batches because the secant condition yₜᵀsₜ > 0 requires consistent gradient estimates, which random mini-batches violate.

## Gauss-Newton and K-FAC

For least squares f = ½‖r(θ)‖² where r(θ) is a residual vector, the Hessian is H = JᵀJ + Σᵢ rᵢ∇²rᵢ ≈ JᵀJ (Gauss-Newton approximation, dropping the second-derivative terms). The Gauss-Newton update θ ← θ − (JᵀJ)⁻¹Jᵀr is equivalent to solving a local linearized least squares problem. JᵀJ is PSD by construction (no indefinite H issues), and for small residuals the approximation is tight. K-FAC (Kronecker-Factored Approximate Curvature, Martens and Grosse 2015) approximates the Fisher information matrix F (which equals the Hessian for cross-entropy loss under the model's own distribution) using the Kronecker structure of linear layers. For a linear layer y = Wx with input x and output gradient δ, K-FAC approximates F_W ≈ A ⊗ G where A = E[xxᵀ] (input covariance, size d_in × d_in) and G = E[δδᵀ] (output gradient covariance, size d_out × d_out). The inverse F_W⁻¹ ≈ A⁻¹ ⊗ G⁻¹ via the Kronecker product rule (A⊗B)⁻¹ = A⁻¹⊗B⁻¹. This gives O(d_in² + d_out²) per layer instead of O((d_in·d_out)²), making K-FAC practical for networks with moderate-width layers. K-FAC achieves Adam-comparable convergence with fewer steps, at the cost of more compute per step.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import time

torch.manual_seed(0)
n, d_in, d_out = 200, 20, 1
X = torch.randn(n, d_in)
true_w = torch.randn(d_in, d_out)
y = X @ true_w + 0.1 * torch.randn(n, d_out)

def make_model():
    return nn.Sequential(nn.Linear(d_in, 10), nn.Tanh(), nn.Linear(10, d_out))

def train_lbfgs(model, X, y, max_iter=100):
    optimizer = optim.LBFGS(model.parameters(), lr=0.5, max_iter=max_iter,
                             line_search_fn='strong_wolfe')
    loss_fn = nn.MSELoss()
    def closure():
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        return loss
    t0 = time.time()
    optimizer.step(closure)
    return loss_fn(model(X), y).item(), time.time() - t0

def train_adam(model, X, y, steps=500):
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()
    t0 = time.time()
    for _ in range(steps):
        optimizer.zero_grad()
        loss_fn(model(X), y).backward()
        optimizer.step()
    return loss_fn(model(X), y).item(), time.time() - t0

lbfgs_loss, lbfgs_time = train_lbfgs(make_model(), X, y)
adam_loss, adam_time = train_adam(make_model(), X, y)
print(f"L-BFGS: loss={lbfgs_loss:.6f}, time={lbfgs_time:.3f}s")
print(f"Adam (500 steps): loss={adam_loss:.6f}, time={adam_time:.3f}s")
```

## ML Connections: When Second-Order Beats Adam

Second-order methods beat Adam in specific scenarios where their assumptions hold. Full-batch training: when the full dataset fits in memory and consistent gradients are available, L-BFGS's secant condition is satisfied and superlinear convergence applies. This covers small dataset fine-tuning, scientific ML (physics-informed neural networks), and neural network verification. Convex or nearly convex objectives: logistic regression, linear SVM, last-layer fine-tuning with frozen representations — the quadratic convergence regime is accessible. Small models (under 10M parameters): the Hessian or its factored approximation is computable; K-FAC is practical for models with layers up to width 1000-2000. Natural policy gradient in RL: K-FAC approximates the Fisher information matrix, giving a principled natural gradient step that is invariant to parameter reparameterization — critical for stable policy optimization. In contrast, Adam approximates second-order information using only the diagonal of the Fisher (per-parameter adaptive learning rates), missing off-diagonal curvature structure that K-FAC captures. For LLM pre-training with n = 7×10⁹ parameters and stochastic gradients, second-order methods remain impractical: even K-FAC's per-layer cost exceeds GPU memory, and mini-batch gradients violate the secant condition.

```python
import numpy as np
from scipy.optimize import minimize
import time

np.random.seed(1)
n_samples, n_features = 1000, 30
X_np = np.random.randn(n_samples, n_features)
w_true = np.random.randn(n_features)
y_np = X_np @ w_true + 0.1 * np.random.randn(n_samples)

def mse_loss(w): return 0.5 * np.mean((X_np @ w - y_np)**2) + 0.01 * np.dot(w, w)
def mse_grad(w): return X_np.T @ (X_np @ w - y_np) / n_samples + 0.02 * w

# Gradient descent
def run_gd_np(lr=0.1, steps=1000):
    w = np.zeros(n_features)
    losses = [mse_loss(w)]
    for _ in range(steps):
        w -= lr * mse_grad(w)
        losses.append(mse_loss(w))
    return w, losses

t0 = time.time(); w_gd, losses_gd = run_gd_np(); t_gd = time.time() - t0

# L-BFGS
t0 = time.time()
res = minimize(mse_loss, np.zeros(n_features), jac=mse_grad, method='L-BFGS-B')
t_lbfgs = time.time() - t0

print(f"GD (1000 steps): final loss = {losses_gd[-1]:.6f}, time = {t_gd:.3f}s")
print(f"L-BFGS ({res.nit} iters): final loss = {res.fun:.6f}, time = {t_lbfgs:.3f}s")
print(f"Solution quality — GD: {np.linalg.norm(w_gd - w_true):.4f}, "
      f"L-BFGS: {np.linalg.norm(res.x - w_true):.4f}")
```

## Implementation Pitfalls

Four critical pitfalls with second-order methods in practice. First, using L-BFGS with mini-batches: the secant condition requires yₜᵀsₜ > 0 (positive curvature along the step). When gradients are computed on different random mini-batches at successive steps, yₜ and sₜ are computed from different data distributions, causing yₜᵀsₜ < 0 frequently — the inverse Hessian approximation becomes indefinite, and L-BFGS diverges or makes very poor updates. Always use L-BFGS with full-batch or very large batches only. Second, forgetting the closure in PyTorch: torch.optim.LBFGS requires a closure function that zeroes gradients, performs the forward pass, and returns the loss — without this, the line search has no way to evaluate the objective and will use a fixed step size (degrading to GD). Third, memory overflow with m too large: setting max_history (m) to 100 or 200 uses 100-200 times more memory than a single gradient vector — keep m between 10 and 30. Fourth, ignoring H's indefiniteness near saddles: if λ_min(H) < 0, H⁻¹∇f may point to a higher function value. Add damping: use (H + λI)⁻¹∇f with λ = max(0, −λ_min(H)) + ε.

## Practical Guidance

Decision guide for second-order methods in practice. Use L-BFGS when: (1) the dataset fits entirely in memory (n ≤ 10⁶ samples); (2) the objective is smooth and convex or nearly convex; (3) you need high precision (scientific computing, neural network verification); (4) you are doing full-batch fine-tuning of the last layer only. Use K-FAC when: training a moderately-sized model (10M-100M parameters) where K-FAC's per-layer factored Fisher is computable, and you want faster convergence than Adam with fewer total steps (accepting more compute per step). Use Adam everywhere else: stochastic training, large models, non-smooth objectives. When using torch.optim.LBFGS in PyTorch, set line_search_fn='strong_wolfe' for automatic step size selection, and set history_size=20 (the m parameter). Monitor the closure being called multiple times per step (this is normal — L-BFGS's line search makes multiple function evaluations to find the optimal step size along the Newton direction).

> **Warning**: L-BFGS requires a closure that re-evaluates the loss, and the loss must be computed on the SAME data every time (no random sampling within the closure). Using random mini-batches in the closure causes the secant condition yₜᵀsₜ > 0 to fail, producing negative curvature estimates and divergence or wildly incorrect updates. For mini-batch training, always use Adam or SGD with momentum. Only switch to L-BFGS for full-batch fine-tuning, small dataset problems, or after training with Adam when you want to squeeze out the last precision improvement.

| Method | Convergence Rate | Memory | Typical Iterations | Best For |
|---|---|---|---|---|
| GD | Linear O(κ log 1/ε) | O(n) | 1000-10000 | Prototype, baseline |
| SGD + Momentum | O(1/t) stochastic | O(n) | 10-100 epochs | DL, stochastic settings |
| Adam / AdamW | O(1/√t) adaptive | O(3n) (params + 2 moments) | 10-50 epochs | Default DL choice |
| BFGS | Superlinear | O(n²) | 20-100 | Medium n, full batch |
| L-BFGS | Superlinear | O(mn), m≈20 | 50-500 | Large n, full batch, convex |
| Newton | Quadratic | O(n²) + O(n³) invert | 5-20 | n < 1000, high precision |
| K-FAC | Near-quadratic per layer | O(Σ(d_in² + d_out²)) | 2-5× fewer than Adam | Moderate DL models, RL |

---

## Key Takeaways

- Newton's method update x ← x − H⁻¹∇f converges quadratically near a minimum: the error ε satisfies ε_{t+1} ≤ C·ε_t², doubling the number of correct digits per step.
- Newton requires O(n²) memory and O(n³) inversion — infeasible for n > 10⁵; damped Newton adds λI to H for stability near saddles.
- BFGS approximates the inverse Hessian using rank-2 updates from gradient differences (sₜ, yₜ), achieving superlinear convergence with O(n²) memory.
- L-BFGS stores only the last m=10-20 (sₜ, yₜ) pairs, computing Hessian-vector products via the two-loop recursion in O(mn) — practical for large-scale convex problems.
- L-BFGS FAILS with mini-batches because random gradients violate the secant condition yₜᵀsₜ > 0; use only with full-batch or consistent gradients.
- K-FAC approximates the Fisher information using Kronecker structure: F_W ≈ A⊗G, inverted as A⁻¹⊗G⁻¹, reducing per-layer cost from O((d_in·d_out)²) to O(d_in² + d_out²).
- Second-order methods beat Adam for small-to-medium scale full-batch problems; Adam wins for stochastic large-scale deep learning.

