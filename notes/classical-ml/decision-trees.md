---
title: "Decision Trees — Information Gain, Gini, and Pruning"
slug: "decision-trees"
description: "Deep dive into CART, ID3, and C4.5 algorithms: greedy recursive splitting on information gain and Gini impurity, why trees overfit, and how cost-complexity pruning with ccp_alpha controls model complexity."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoYXQgQXJlIERlY2lzaW9uIFRyZWVzPyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBkZWNpc2lvbiB0cmVlIHBhcnRpdGlvbnMgZmVhdHVyZSBzcGFjZSBpbnRvIGF4aXMtYWxpZ25lZCByZWN0YW5ndWxhciByZWdpb25zIHRocm91Z2ggZ3JlZWR5IHJlY3Vyc2l2ZSBiaW5hcnkgc3BsaXRzLiBFYWNoIGludGVybmFsIG5vZGUgdGVzdHMgYSBzaW5nbGUgZmVhdHVyZSBhZ2FpbnN0IGEgdGhyZXNob2xkOyBlYWNoIGxlYWYgcHJlZGljdHMgYSBjbGFzcyBsYWJlbCBvciByZWFsIHZhbHVlLiBUcmVlcyBhcmUgaW50cmluc2ljYWxseSBpbnRlcnByZXRhYmxlIOKAlCBldmVyeSBwcmVkaWN0aW9uIGlzIGEgdHJhY2VhYmxlIGNoYWluIG9mIGlmLXRoZW4gcnVsZXMg4oCUIHlldCB0aGV5IGFsc28gdW5kZXJwaW4gcG93ZXJmdWwgZW5zZW1ibGVzIGxpa2UgUmFuZG9tIEZvcmVzdHMgYW5kIEdyYWRpZW50IEJvb3N0aW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwbGl0dGluZyBDcml0ZXJpYSDigJQgSW5mb3JtYXRpb24gR2FpbiBhbmQgR2luaSBJbXB1cml0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXQgZWFjaCBub2RlIHRoZSBhbGdvcml0aG0gdHJpZXMgZXZlcnkgZmVhdHVyZS10aHJlc2hvbGQgcGFpciBhbmQgcGlja3MgdGhlIG9uZSBtYXhpbWlzaW5nIHB1cml0eSBnYWluLiBJbmZvcm1hdGlvbiBHYWluOiBJRyA9IEgocGFyZW50KSDiiJIgzqMobuKCli9uKSBIKGNoaWxk4oKWKSB3aGVyZSBIKHApID0g4oiSzqMgcOG1oiBsb2figoIocOG1oikgaXMgU2hhbm5vbiBlbnRyb3B5LiBHaW5pIGltcHVyaXR5IGF2b2lkcyB0aGUgbG9nOiBHaW5pID0gMSDiiJIgzqMgcOKClsKyLCByYW5naW5nIGZyb20gMCAocHVyZSkgdG8gKDHiiJIxL0spIGZvciBLIGVxdWFsIGNsYXNzZXMuIEZvciByZWdyZXNzaW9uIENBUlQgdXNlcyBNU0UgaW1wdXJpdHk6ICgxL24pIM6jKHnhtaIg4oiSIMizKcKyLCBzbyB0aGUgYmVzdCBzcGxpdCBtaW5pbWlzZXMgd2VpZ2h0ZWQgY2hpbGQgTVNFLiBHaW5pIGFuZCBlbnRyb3B5IHByb2R1Y2UgbmVhcmx5IGlkZW50aWNhbCBzcGxpdHMgaW4gcHJhY3RpY2U7IEdpbmkgaXMgc2xpZ2h0bHkgZmFzdGVyLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXJcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9pcmlzXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCB0cmFpbl90ZXN0X3NwbGl0XG5cbmRlZiBnaW5pKHkpOlxuICAgIG4gPSBsZW4oeSlcbiAgICBjb3VudHMgPSBDb3VudGVyKHkpXG4gICAgcmV0dXJuIDEuMCAtIHN1bSgoYyAvIG4pICoqIDIgZm9yIGMgaW4gY291bnRzLnZhbHVlcygpKVxuXG5kZWYgYmVzdF9zcGxpdChYLCB5KTpcbiAgICBiZXN0X2dhaW4sIGJlc3RfZmVhdCwgYmVzdF90aHJlc2ggPSAtMSwgTm9uZSwgTm9uZVxuICAgIHBhcmVudF9nID0gZ2luaSh5KVxuICAgIG4gPSBsZW4oeSlcbiAgICBmb3IgZmVhdCBpbiByYW5nZShYLnNoYXBlWzFdKTpcbiAgICAgICAgZm9yIHRocmVzaCBpbiBucC51bmlxdWUoWFs6LCBmZWF0XSk6XG4gICAgICAgICAgICBsZWZ0ID0gWFs6LCBmZWF0XSBcdTAwM2M9IHRocmVzaFxuICAgICAgICAgICAgaWYgbGVmdC5zdW0oKSA9PSAwIG9yICh+bGVmdCkuc3VtKCkgPT0gMDpcbiAgICAgICAgICAgICAgICBjb250aW51ZVxuICAgICAgICAgICAgZ2FpbiA9IHBhcmVudF9nIC0gKFxuICAgICAgICAgICAgICAgIGxlZnQuc3VtKCkgLyBuICogZ2luaSh5W2xlZnRdKSArXG4gICAgICAgICAgICAgICAgKH5sZWZ0KS5zdW0oKSAvIG4gKiBnaW5pKHlbfmxlZnRdKSlcbiAgICAgICAgICAgIGlmIGdhaW4gXHUwMDNlIGJlc3RfZ2FpbjpcbiAgICAgICAgICAgICAgICBiZXN0X2dhaW4sIGJlc3RfZmVhdCwgYmVzdF90aHJlc2ggPSBnYWluLCBmZWF0LCB0aHJlc2hcbiAgICByZXR1cm4gYmVzdF9mZWF0LCBiZXN0X3RocmVzaCwgYmVzdF9nYWluXG5cbmRlZiBidWlsZF90cmVlKFgsIHksIG1heF9kZXB0aD01LCBkZXB0aD0wKTpcbiAgICBpZiBkZXB0aCBcdTAwM2U9IG1heF9kZXB0aCBvciBsZW4oc2V0KHkpKSA9PSAxIG9yIGxlbih5KSBcdTAwM2MgMjpcbiAgICAgICAgcmV0dXJuIENvdW50ZXIoeSkubW9zdF9jb21tb24oMSlbMF1bMF1cbiAgICBmZWF0LCB0aHJlc2gsIGdhaW4gPSBiZXN0X3NwbGl0KFgsIHkpXG4gICAgaWYgZmVhdCBpcyBOb25lIG9yIGdhaW4gXHUwMDNjPSAwOlxuICAgICAgICByZXR1cm4gQ291bnRlcih5KS5tb3N0X2NvbW1vbigxKVswXVswXVxuICAgIG1hc2sgPSBYWzosIGZlYXRdIFx1MDAzYz0gdGhyZXNoXG4gICAgcmV0dXJuIHtcdTAwMjdmZWF0XHUwMDI3OiBmZWF0LCBcdTAwMjd0aHJlc2hcdTAwMjc6IHRocmVzaCxcbiAgICAgICAgICAgIFx1MDAyN2xlZnRcdTAwMjc6ICBidWlsZF90cmVlKFhbbWFza10sICB5W21hc2tdLCAgbWF4X2RlcHRoLCBkZXB0aCArIDEpLFxuICAgICAgICAgICAgXHUwMDI3cmlnaHRcdTAwMjc6IGJ1aWxkX3RyZWUoWFt+bWFza10sIHlbfm1hc2tdLCBtYXhfZGVwdGgsIGRlcHRoICsgMSl9XG5cblgsIHkgPSBsb2FkX2lyaXMocmV0dXJuX1hfeT1UcnVlKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxudHJlZSA9IGJ1aWxkX3RyZWUoWF90ciwgeV90ciwgbWF4X2RlcHRoPTQpXG5wcmludChcdTAwMjdSb290IHNwbGl0IOKAlCBmZWF0dXJlOlx1MDAyNywgdHJlZVtcdTAwMjdmZWF0XHUwMDI3XSwgXHUwMDI3dGhyZXNob2xkOlx1MDAyNywgcm91bmQodHJlZVtcdTAwMjd0aHJlc2hcdTAwMjddLCAyKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBbGdvcml0aG0gQ29tcGFyaXNvbiDigJQgSUQzLCBDNC41LCBhbmQgQ0FSVCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhyZWUgZ2VuZXJhdGlvbnMgb2YgZGVjaXNpb24gdHJlZSBhbGdvcml0aG1zIGRpZmZlciBpbiBpbXB1cml0eSBtZWFzdXJlLCBzcGxpdCB0eXBlLCBhbmQgcHJ1bmluZyBzdXBwb3J0LiBJRDMgKFF1aW5sYW4gMTk4NikgdXNlcyBpbmZvcm1hdGlvbiBnYWluIHdpdGggbXVsdGktd2F5IGNhdGVnb3JpY2FsIHNwbGl0cyBhbmQgbm8gcHJ1bmluZy4gQzQuNSBpbXByb3ZlcyB3aXRoIGdhaW4gcmF0aW8gKGNvcnJlY3RzIGhpZ2gtY2FyZGluYWxpdHkgYmlhcyksIGNvbnRpbnVvdXMgZmVhdHVyZSBiaW5uaW5nLCBtaXNzaW5nLXZhbHVlIGhhbmRsaW5nLCBhbmQgZXJyb3ItYmFzZWQgcG9zdC1wcnVuaW5nLiBDQVJUIChCcmVpbWFuIGV0IGFsLiAxOTg0KSBlbmZvcmNlcyBiaW5hcnkgc3BsaXRzLCBzdXBwb3J0cyBib3RoIEdpbmkvTVNFLCBhbmQgaW1wbGVtZW50cyBjb3N0LWNvbXBsZXhpdHkgcHJ1bmluZyDigJQgdGhpcyBpcyB3aGF0IHNrbGVhcm4gaW1wbGVtZW50cy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQWxnb3JpdGhtIiwiSW1wdXJpdHkgTWVhc3VyZSIsIlNwbGl0IFR5cGUiLCJNdWx0aS13YXkgU3BsaXRzIiwiUHJ1bmluZyIsIlJlZ3Jlc3Npb24iXSwicm93cyI6W1siSUQzIiwiSW5mb3JtYXRpb24gR2FpbiAoZW50cm9weSkiLCJDYXRlZ29yaWNhbCBvbmx5IiwiWWVzIiwiTm9uZSIsIk5vIl0sWyJDNC41IiwiR2FpbiBSYXRpbyAoZW50cm9weSkiLCJDYXRlZ29yaWNhbCArIGNvbnRpbnVvdXMiLCJZZXMiLCJFcnJvci1iYXNlZCBwb3N0LXBydW5pbmciLCJObyJdLFsiQ0FSVCIsIkdpbmkgKGNsYXNzKSAvIE1TRSAocmVnKSIsIkJpbmFyeSBvbmx5IiwiTm8iLCJDb3N0LWNvbXBsZXhpdHkgKGNjcF9hbHBoYSkiLCJZZXMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6InNrbGVhcm4gRGVjaXNpb25UcmVlQ2xhc3NpZmllciB3aXRoIFZpc3VhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6InNrbGVhcm5cdTAwMjdzIERlY2lzaW9uVHJlZUNsYXNzaWZpZXIgaW1wbGVtZW50cyBDQVJULiBtYXhfZGVwdGggaXMgdGhlIG1vc3QgZGlyZWN0IGNvbXBsZXhpdHkgY29udHJvbC4gbWluX3NhbXBsZXNfbGVhZiBwcmV2ZW50cyBzcGxpdHMgdGhhdCBwcm9kdWNlIHRpbnkgbGVhdmVzLCBwcm92aWRpbmcgaW1wbGljaXQgcmVndWxhcmlzYXRpb24uIHBsb3RfdHJlZSByZW5kZXJzIHRoZSBsZWFybmVkIHRyZWUgd2l0aCBjbGFzcyBkaXN0cmlidXRpb25zIGFuZCB0aHJlc2hvbGRzIGF0IGVhY2ggbm9kZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSBza2xlYXJuLnRyZWUgaW1wb3J0IERlY2lzaW9uVHJlZUNsYXNzaWZpZXIsIHBsb3RfdHJlZVxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2lyaXNcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGF0YSA9IGxvYWRfaXJpcygpXG5YLCB5ID0gZGF0YS5kYXRhLCBkYXRhLnRhcmdldFxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxuXG5jbGYgPSBEZWNpc2lvblRyZWVDbGFzc2lmaWVyKFxuICAgIGNyaXRlcmlvbj1cdTAwMjdnaW5pXHUwMDI3LFxuICAgIG1heF9kZXB0aD00LFxuICAgIG1pbl9zYW1wbGVzX3NwbGl0PTEwLFxuICAgIG1pbl9zYW1wbGVzX2xlYWY9NSxcbiAgICByYW5kb21fc3RhdGU9NDJcbilcbmNsZi5maXQoWF90ciwgeV90cilcbnByaW50KGZcdTAwMjdUcmFpbjoge2NsZi5zY29yZShYX3RyLCB5X3RyKTouNGZ9ICBUZXN0OiB7Y2xmLnNjb3JlKFhfdGUsIHlfdGUpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3RGVwdGg6IHtjbGYuZ2V0X2RlcHRoKCl9ICBMZWF2ZXM6IHtjbGYuZ2V0X25fbGVhdmVzKCl9XHUwMDI3KVxuXG5maWcsIGF4ID0gcGx0LnN1YnBsb3RzKGZpZ3NpemU9KDE0LCA3KSlcbnBsb3RfdHJlZShjbGYsIGZlYXR1cmVfbmFtZXM9ZGF0YS5mZWF0dXJlX25hbWVzLFxuICAgICAgICAgIGNsYXNzX25hbWVzPWRhdGEudGFyZ2V0X25hbWVzLCBmaWxsZWQ9VHJ1ZSwgcm91bmRlZD1UcnVlLCBheD1heClcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3ZGVjaXNpb25fdHJlZS5wbmdcdTAwMjcsIGRwaT0xNTApXG5wbHQuc2hvdygpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RvcHBpbmcgQ3JpdGVyaWEgYW5kIFdoeSBUcmVlcyBPdmVyZml0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbiB1bmNvbnN0cmFpbmVkIGRlY2lzaW9uIHRyZWUgZ3Jvd3MgdW50aWwgZXZlcnkgbGVhZiBpcyBwdXJlIOKAlCBhY2hpZXZpbmcgMCB0cmFpbmluZyBlcnJvciBidXQgY2F0YXN0cm9waGljIGdlbmVyYWxpc2F0aW9uLiBUaGlzIGlzIGJlY2F1c2UgdHJlZXMgaGF2ZSB1bmxpbWl0ZWQgcmVwcmVzZW50YXRpb25hbCBjYXBhY2l0eTsgYSBkZXB0aC1rIGJpbmFyeSB0cmVlIGNhbiByZXByZXNlbnQgMl5rIGRpc3RpbmN0IGxlYWYgcHJlZGljdGlvbnMuIERlcHRoIGRpcmVjdGx5IGNvbnRyb2xzIHRoZSBiaWFzLXZhcmlhbmNlIHRyYWRlLW9mZjogc2hhbGxvdyB0cmVlcyBoYXZlIGhpZ2ggYmlhcyBhbmQgbG93IHZhcmlhbmNlOyBkZWVwIHRyZWVzIGhhdmUgbmVhci16ZXJvIGJpYXMgYnV0IGV4dHJlbWUgdmFyaWFuY2UuIEVhY2ggYWRkaXRpb25hbCBsZXZlbCBkb3VibGVzIHRoZSBudW1iZXIgb2YgbGVhZiBub2Rlcy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkRlZmF1bHQgbWF4X2RlcHRoPU5vbmUgQ2F1c2VzIE92ZXJmaXR0aW5nIiwiY29udGVudCI6InNrbGVhcm5cdTAwMjdzIERlY2lzaW9uVHJlZUNsYXNzaWZpZXIgZGVmYXVsdHMgdG8gbWF4X2RlcHRoPU5vbmUsIGdyb3dpbmcgdW50aWwgYWxsIGxlYXZlcyBhcmUgcHVyZSBvciBzbWFsbGVyIHRoYW4gbWluX3NhbXBsZXNfc3BsaXQuIE9uIGFueSBub24tdHJpdmlhbCBkYXRhc2V0IHRoaXMgbWVtb3Jpc2VzIHRoZSB0cmFpbmluZyBkYXRhLiBBbHdheXMgc2V0IG1heF9kZXB0aCwgdXNlIGNjcF9hbHBoYSwgb3Igd3JhcCB0aGUgdHJlZSBpbiBhbiBlbnNlbWJsZS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIm1heF9kZXB0aDogaGFyZCBjZWlsaW5nIG9uIGRlcHRoIOKAlCBtb3N0IGRpcmVjdCByZWd1bGFyaXNhdGlvbiBsZXZlciIsIm1pbl9zYW1wbGVzX3NwbGl0OiByZXF1aXJlIGF0IGxlYXN0IE4gc2FtcGxlcyB0byBhdHRlbXB0IGEgc3BsaXQgKGRlZmF1bHQgMikiLCJtaW5fc2FtcGxlc19sZWFmOiByZXF1aXJlIGF0IGxlYXN0IE4gc2FtcGxlcyBpbiBlYWNoIHJlc3VsdGluZyBsZWFmIiwibWluX2ltcHVyaXR5X2RlY3JlYXNlOiBzcGxpdCBvbmx5IGlmIGltcHVyaXR5IHJlZHVjdGlvbiBleGNlZWRzIHRoaXMgZGVsdGEiLCJtYXhfbGVhZl9ub2RlczogYmVzdC1maXJzdCBncm93dGggbGltaXRlZCB0byBrIGxlYXZlcyAoYWx0ZXJuYXRpdmUgdG8gbWF4X2RlcHRoKSIsIm1heF9mZWF0dXJlczogbGltaXQgZmVhdHVyZXMgZXZhbHVhdGVkIHBlciBzcGxpdCAodXNlZCBpbnNpZGUgUmFuZG9tIEZvcmVzdHMpIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvc3QtQ29tcGxleGl0eSBQcnVuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQb3N0LXBydW5pbmcgdmlhIGNvc3QtY29tcGxleGl0eSAod2Vha2VzdC1saW5rKSBwcnVuaW5nIG1pbmltaXNlcyBSX86xKFQpID0gUihUKSArIM6xfFR8IHdoZXJlIFIoVCkgaXMgbm9kZSBpbXB1cml0eSBhbmQgfFR8IGlzIHRoZSBsZWFmIGNvdW50LiBBcyDOsSBpbmNyZWFzZXMgZnJvbSAwIHRoZSB3ZWFrZXN0IHN1YnRyZWVzIGFyZSBjb2xsYXBzZWQgdW50aWwgb25seSB0aGUgcm9vdCByZW1haW5zLiBjb3N0X2NvbXBsZXhpdHlfcHJ1bmluZ19wYXRoKCkgcmV0dXJucyB0aGUgZnVsbCAoYWxwaGEsIGltcHVyaXR5KSBzZXF1ZW5jZSDigJQgY3Jvc3MtdmFsaWRhdGUgdG8gY2hvb3NlIHRoZSBiZXN0IGFscGhhLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHNrbGVhcm4udHJlZSBpbXBvcnQgRGVjaXNpb25UcmVlQ2xhc3NpZmllclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2JyZWFzdF9jYW5jZXJcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmltcG9ydCBudW1weSBhcyBucFxuXG5YLCB5ID0gbG9hZF9icmVhc3RfY2FuY2VyKHJldHVybl9YX3k9VHJ1ZSlcblhfdHIsIFhfdGUsIHlfdHIsIHlfdGUgPSB0cmFpbl90ZXN0X3NwbGl0KFgsIHksIHRlc3Rfc2l6ZT0wLjIsIHJhbmRvbV9zdGF0ZT00MilcblxuIyBDb21wdXRlIGZ1bGwgcHJ1bmluZyBwYXRoXG5wYXRoID0gRGVjaXNpb25UcmVlQ2xhc3NpZmllcihyYW5kb21fc3RhdGU9NDIpLmNvc3RfY29tcGxleGl0eV9wcnVuaW5nX3BhdGgoWF90ciwgeV90cilcbmFscGhhcyA9IHBhdGguY2NwX2FscGhhc1s6LTFdICAgIyBkcm9wIGxhc3QgdHJpdmlhbCBhbHBoYVxuXG50cmFpbl9zY29yZXMsIHRlc3Rfc2NvcmVzID0gW10sIFtdXG5mb3IgYWxwaGEgaW4gYWxwaGFzOlxuICAgIGR0ID0gRGVjaXNpb25UcmVlQ2xhc3NpZmllcihjY3BfYWxwaGE9YWxwaGEsIHJhbmRvbV9zdGF0ZT00MilcbiAgICBkdC5maXQoWF90ciwgeV90cilcbiAgICB0cmFpbl9zY29yZXMuYXBwZW5kKGR0LnNjb3JlKFhfdHIsIHlfdHIpKVxuICAgIHRlc3Rfc2NvcmVzLmFwcGVuZChkdC5zY29yZShYX3RlLCB5X3RlKSlcblxuYmVzdCA9IGludChucC5hcmdtYXgodGVzdF9zY29yZXMpKVxucHJpbnQoZlx1MDAyN0Jlc3QgY2NwX2FscGhhOiB7YWxwaGFzW2Jlc3RdOi42Zn0gIFRlc3QgYWNjOiB7dGVzdF9zY29yZXNbYmVzdF06LjRmfVx1MDAyNylcblxucGx0LmZpZ3VyZShmaWdzaXplPSg5LCA1KSlcbnBsdC5wbG90KGFscGhhcywgdHJhaW5fc2NvcmVzLCBtYXJrZXI9XHUwMDI3b1x1MDAyNywgbXM9NCwgbGFiZWw9XHUwMDI3VHJhaW5cdTAwMjcpXG5wbHQucGxvdChhbHBoYXMsIHRlc3Rfc2NvcmVzLCAgbWFya2VyPVx1MDAyN29cdTAwMjcsIG1zPTQsIGxhYmVsPVx1MDAyN1Rlc3RcdTAwMjcpXG5wbHQueGxhYmVsKFx1MDAyN2NjcF9hbHBoYVx1MDAyNyk7IHBsdC55bGFiZWwoXHUwMDI3QWNjdXJhY3lcdTAwMjcpXG5wbHQudGl0bGUoXHUwMDI3Q29zdC1Db21wbGV4aXR5IFBydW5pbmcgUGF0aFx1MDAyNyk7IHBsdC5sZWdlbmQoKTsgcGx0LmdyaWQoVHJ1ZSlcbnBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZlYXR1cmUgSW1wb3J0YW5jZSBmcm9tIFRyZWUgU3BsaXRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNZWFuIERlY3JlYXNlIGluIEltcHVyaXR5IChNREkgLyBHaW5pIGltcG9ydGFuY2UpIHN1bXMgZWFjaCBmZWF0dXJlXHUwMDI3cyBpbXB1cml0eSByZWR1Y3Rpb24gYWNyb3NzIGFsbCBub2RlcyB3ZWlnaHRlZCBieSB0aGUgZnJhY3Rpb24gb2Ygc2FtcGxlcyByZWFjaGluZyBlYWNoIHNwbGl0LiBWYWx1ZXMgbm9ybWFsaXNlIHRvIHN1bSB0byAxLiBNREkgaXMgZmFzdCBhbmQgYnVpbHQgaW50byBldmVyeSB0cmVlIG1vZGVsLCBidXQgaXQgaXMgYmlhc2VkIHRvd2FyZCBoaWdoLWNhcmRpbmFsaXR5IGZlYXR1cmVzIGJlY2F1c2UgdGhleSBvZmZlciBtb3JlIGNhbmRpZGF0ZSB0aHJlc2hvbGRzLiBQZXJtdXRhdGlvbiBpbXBvcnRhbmNlIGFuZCBTSEFQIGdpdmUgdW5iaWFzZWQgYWx0ZXJuYXRpdmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHNrbGVhcm4udHJlZSBpbXBvcnQgRGVjaXNpb25UcmVlQ2xhc3NpZmllclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2JyZWFzdF9jYW5jZXJcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmltcG9ydCBudW1weSBhcyBucFxuXG5kYXRhID0gbG9hZF9icmVhc3RfY2FuY2VyKClcblgsIHkgPSBkYXRhLmRhdGEsIGRhdGEudGFyZ2V0XG5cbmNsZiA9IERlY2lzaW9uVHJlZUNsYXNzaWZpZXIobWF4X2RlcHRoPTYsIHJhbmRvbV9zdGF0ZT00MilcbmNsZi5maXQoWCwgeSlcblxuaW1wb3J0YW5jZXMgPSBjbGYuZmVhdHVyZV9pbXBvcnRhbmNlc19cbnRvcF9pZHggPSBucC5hcmdzb3J0KGltcG9ydGFuY2VzKVs6Oi0xXVs6MTBdXG5cbnBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsIDUpKVxucGx0LmJhcihyYW5nZSgxMCksIGltcG9ydGFuY2VzW3RvcF9pZHhdLCBjb2xvcj1cdTAwMjdzdGVlbGJsdWVcdTAwMjcpXG5wbHQueHRpY2tzKHJhbmdlKDEwKSwgW2RhdGEuZmVhdHVyZV9uYW1lc1tpXSBmb3IgaSBpbiB0b3BfaWR4XSxcbiAgICAgICAgICAgcm90YXRpb249NDUsIGhhPVx1MDAyN3JpZ2h0XHUwMDI3KVxucGx0LnRpdGxlKFx1MDAyN0RlY2lzaW9uIFRyZWUgRmVhdHVyZSBJbXBvcnRhbmNlcyAoR2luaSBNREkpXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpOyBwbHQuc2hvdygpXG5cbmZvciBpIGluIHRvcF9pZHhbOjVdOlxuICAgIHByaW50KGZcdTAwMjcgIHtkYXRhLmZlYXR1cmVfbmFtZXNbaV06XHUwMDNjMzVzfSAgaW1wb3J0YW5jZT17aW1wb3J0YW5jZXNbaV06LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb250aW51b3VzIHZzIENhdGVnb3JpY2FsIFNwbGl0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGNvbnRpbnVvdXMgZmVhdHVyZXMgQ0FSVCBldmFsdWF0ZXMgKG7iiJIxKSBtaWRwb2ludHMgYmV0d2VlbiBzb3J0ZWQgdW5pcXVlIHZhbHVlcy4gRm9yIGNhdGVnb3JpY2FsIGZlYXR1cmVzIHdpdGggSyBjYXRlZ29yaWVzIHRoZXJlIGFyZSAyXihL4oiSMSniiJIxIHBvc3NpYmxlIGJpbmFyeSBzdWJzZXRzIOKAlCBleHBvbmVudGlhbCBjb3N0IGF2b2lkZWQgYnk6IHNvcnRpbmcgY2F0ZWdvcmllcyBieSB0YXJnZXQgbWVhbiAoZm9yIHJlZ3Jlc3Npb24vYmluYXJ5KSBhbmQgZXZhbHVhdGluZyBL4oiSMSBvcmRlcmVkIHNwbGl0cywgb3IgdXNpbmcgb25lLWhvdCBlbmNvZGluZy4gSGlnaC1jYXJkaW5hbGl0eSBjYXRlZ29yaWNhbHMgKG1hbnkgdW5pcXVlIHZhbHVlcykgYXJlIGV4cGVuc2l2ZSBhbmQgYmlhcyBNREkgaW1wb3J0YW5jZSDigJQgYWx3YXlzIGVuY29kZSBvciBsaW1pdCBjYXJkaW5hbGl0eS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdpbmkgYW5kIGVudHJvcHkgcHJvZHVjZSBuZWFybHkgaWRlbnRpY2FsIHNwbGl0cyDigJQgY2hvb3NlIEdpbmkgZm9yIHNwZWVkIiwiQ0FSVCB1c2VzIGJpbmFyeSBzcGxpdHM7IElEMy9DNC41IGFsbG93IG11bHRpLXdheSBjYXRlZ29yaWNhbCBzcGxpdHMiLCJBbiB1bmNvbnN0cmFpbmVkIHRyZWUgcGVyZmVjdGx5IG1lbW9yaXNlcyB0cmFpbmluZyBkYXRhIOKAlCBhbHdheXMgcmVndWxhcmlzZSIsIkNvc3QtY29tcGxleGl0eSBwcnVuaW5nIGlzIHRoZSBtb3N0IHByaW5jaXBsZWQgcG9zdC1wcnVuaW5nIG1ldGhvZCBmb3IgQ0FSVCIsIk1ESSBmZWF0dXJlIGltcG9ydGFuY2UgaXMgZmFzdCBidXQgYmlhc2VkIHRvd2FyZCBoaWdoLWNhcmRpbmFsaXR5IGFuZCBjb250aW51b3VzIGZlYXR1cmVzIiwiRGVwdGggY29udHJvbHMgdGhlIGJpYXMtdmFyaWFuY2UgdHJhZGUtb2ZmIG1vcmUgZGlyZWN0bHkgdGhhbiBhbnkgb3RoZXIgcGFyYW1ldGVyIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJQcmFjdGljYWwgUHJ1bmluZyBXb3JrZmxvdyIsImNvbnRlbnQiOiJTdGFydCB3aXRoIG1heF9kZXB0aCAz4oCTOC4gUnVuIGNvc3RfY29tcGxleGl0eV9wcnVuaW5nX3BhdGgoKSBhbmQgcGxvdCB0cmFpbiB2cyB0ZXN0IGFjY3VyYWN5IGFjcm9zcyB0aGUgYWxwaGEgcmFuZ2UuIFNlbGVjdCB0aGUgbGFyZ2VzdCBhbHBoYSB3aGVyZSB0ZXN0IGFjY3VyYWN5IGlzIG5lYXIgaXRzIHBlYWsg4oCUIGdpdmVzIHRoZSBzaW1wbGVzdCB0cmVlIHdpdGggZ29vZCBnZW5lcmFsaXNhdGlvbi4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Decision Trees — Information Gain, Gini, and Pruning

## What Are Decision Trees?

A decision tree partitions feature space into axis-aligned rectangular regions through greedy recursive binary splits. Each internal node tests a single feature against a threshold; each leaf predicts a class label or real value. Trees are intrinsically interpretable — every prediction is a traceable chain of if-then rules — yet they also underpin powerful ensembles like Random Forests and Gradient Boosting.

## Splitting Criteria — Information Gain and Gini Impurity

At each node the algorithm tries every feature-threshold pair and picks the one maximising purity gain. Information Gain: IG = H(parent) − Σ(nₖ/n) H(childₖ) where H(p) = −Σ pᵢ log₂(pᵢ) is Shannon entropy. Gini impurity avoids the log: Gini = 1 − Σ pₖ², ranging from 0 (pure) to (1−1/K) for K equal classes. For regression CART uses MSE impurity: (1/n) Σ(yᵢ − ȳ)², so the best split minimises weighted child MSE. Gini and entropy produce nearly identical splits in practice; Gini is slightly faster.

```python
import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def gini(y):
    n = len(y)
    counts = Counter(y)
    return 1.0 - sum((c / n) ** 2 for c in counts.values())

def best_split(X, y):
    best_gain, best_feat, best_thresh = -1, None, None
    parent_g = gini(y)
    n = len(y)
    for feat in range(X.shape[1]):
        for thresh in np.unique(X[:, feat]):
            left = X[:, feat] <= thresh
            if left.sum() == 0 or (~left).sum() == 0:
                continue
            gain = parent_g - (
                left.sum() / n * gini(y[left]) +
                (~left).sum() / n * gini(y[~left]))
            if gain > best_gain:
                best_gain, best_feat, best_thresh = gain, feat, thresh
    return best_feat, best_thresh, best_gain

def build_tree(X, y, max_depth=5, depth=0):
    if depth >= max_depth or len(set(y)) == 1 or len(y) < 2:
        return Counter(y).most_common(1)[0][0]
    feat, thresh, gain = best_split(X, y)
    if feat is None or gain <= 0:
        return Counter(y).most_common(1)[0][0]
    mask = X[:, feat] <= thresh
    return {'feat': feat, 'thresh': thresh,
            'left':  build_tree(X[mask],  y[mask],  max_depth, depth + 1),
            'right': build_tree(X[~mask], y[~mask], max_depth, depth + 1)}

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
tree = build_tree(X_tr, y_tr, max_depth=4)
print('Root split — feature:', tree['feat'], 'threshold:', round(tree['thresh'], 2))
```

## Algorithm Comparison — ID3, C4.5, and CART

Three generations of decision tree algorithms differ in impurity measure, split type, and pruning support. ID3 (Quinlan 1986) uses information gain with multi-way categorical splits and no pruning. C4.5 improves with gain ratio (corrects high-cardinality bias), continuous feature binning, missing-value handling, and error-based post-pruning. CART (Breiman et al. 1984) enforces binary splits, supports both Gini/MSE, and implements cost-complexity pruning — this is what sklearn implements.

| Algorithm | Impurity Measure | Split Type | Multi-way Splits | Pruning | Regression |
| --- | --- | --- | --- | --- | --- |
| ID3 | Information Gain (entropy) | Categorical only | Yes | None | No |
| C4.5 | Gain Ratio (entropy) | Categorical + continuous | Yes | Error-based post-pruning | No |
| CART | Gini (class) / MSE (reg) | Binary only | No | Cost-complexity (ccp_alpha) | Yes |

## sklearn DecisionTreeClassifier with Visualization

sklearn's DecisionTreeClassifier implements CART. max_depth is the most direct complexity control. min_samples_leaf prevents splits that produce tiny leaves, providing implicit regularisation. plot_tree renders the learned tree with class distributions and thresholds at each node.

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = load_iris()
X, y = data.data, data.target
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)
clf.fit(X_tr, y_tr)
print(f'Train: {clf.score(X_tr, y_tr):.4f}  Test: {clf.score(X_te, y_te):.4f}')
print(f'Depth: {clf.get_depth()}  Leaves: {clf.get_n_leaves()}')

fig, ax = plt.subplots(figsize=(14, 7))
plot_tree(clf, feature_names=data.feature_names,
          class_names=data.target_names, filled=True, rounded=True, ax=ax)
plt.tight_layout()
plt.savefig('decision_tree.png', dpi=150)
plt.show()
```

## Stopping Criteria and Why Trees Overfit

An unconstrained decision tree grows until every leaf is pure — achieving 0 training error but catastrophic generalisation. This is because trees have unlimited representational capacity; a depth-k binary tree can represent 2^k distinct leaf predictions. Depth directly controls the bias-variance trade-off: shallow trees have high bias and low variance; deep trees have near-zero bias but extreme variance. Each additional level doubles the number of leaf nodes.

> **Default max_depth=None Causes Overfitting**: sklearn's DecisionTreeClassifier defaults to max_depth=None, growing until all leaves are pure or smaller than min_samples_split. On any non-trivial dataset this memorises the training data. Always set max_depth, use ccp_alpha, or wrap the tree in an ensemble.

- max_depth: hard ceiling on depth — most direct regularisation lever
- min_samples_split: require at least N samples to attempt a split (default 2)
- min_samples_leaf: require at least N samples in each resulting leaf
- min_impurity_decrease: split only if impurity reduction exceeds this delta
- max_leaf_nodes: best-first growth limited to k leaves (alternative to max_depth)
- max_features: limit features evaluated per split (used inside Random Forests)

## Cost-Complexity Pruning

Post-pruning via cost-complexity (weakest-link) pruning minimises R_α(T) = R(T) + α|T| where R(T) is node impurity and |T| is the leaf count. As α increases from 0 the weakest subtrees are collapsed until only the root remains. cost_complexity_pruning_path() returns the full (alpha, impurity) sequence — cross-validate to choose the best alpha.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

# Compute full pruning path
path = DecisionTreeClassifier(random_state=42).cost_complexity_pruning_path(X_tr, y_tr)
alphas = path.ccp_alphas[:-1]   # drop last trivial alpha

train_scores, test_scores = [], []
for alpha in alphas:
    dt = DecisionTreeClassifier(ccp_alpha=alpha, random_state=42)
    dt.fit(X_tr, y_tr)
    train_scores.append(dt.score(X_tr, y_tr))
    test_scores.append(dt.score(X_te, y_te))

best = int(np.argmax(test_scores))
print(f'Best ccp_alpha: {alphas[best]:.6f}  Test acc: {test_scores[best]:.4f}')

plt.figure(figsize=(9, 5))
plt.plot(alphas, train_scores, marker='o', ms=4, label='Train')
plt.plot(alphas, test_scores,  marker='o', ms=4, label='Test')
plt.xlabel('ccp_alpha'); plt.ylabel('Accuracy')
plt.title('Cost-Complexity Pruning Path'); plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()
```

## Feature Importance from Tree Splits

Mean Decrease in Impurity (MDI / Gini importance) sums each feature's impurity reduction across all nodes weighted by the fraction of samples reaching each split. Values normalise to sum to 1. MDI is fast and built into every tree model, but it is biased toward high-cardinality features because they offer more candidate thresholds. Permutation importance and SHAP give unbiased alternatives.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np

data = load_breast_cancer()
X, y = data.data, data.target

clf = DecisionTreeClassifier(max_depth=6, random_state=42)
clf.fit(X, y)

importances = clf.feature_importances_
top_idx = np.argsort(importances)[::-1][:10]

plt.figure(figsize=(10, 5))
plt.bar(range(10), importances[top_idx], color='steelblue')
plt.xticks(range(10), [data.feature_names[i] for i in top_idx],
           rotation=45, ha='right')
plt.title('Decision Tree Feature Importances (Gini MDI)')
plt.tight_layout(); plt.show()

for i in top_idx[:5]:
    print(f'  {data.feature_names[i]:<35s}  importance={importances[i]:.4f}')
```

## Continuous vs Categorical Splits

For continuous features CART evaluates (n−1) midpoints between sorted unique values. For categorical features with K categories there are 2^(K−1)−1 possible binary subsets — exponential cost avoided by: sorting categories by target mean (for regression/binary) and evaluating K−1 ordered splits, or using one-hot encoding. High-cardinality categoricals (many unique values) are expensive and bias MDI importance — always encode or limit cardinality.

- Gini and entropy produce nearly identical splits — choose Gini for speed
- CART uses binary splits; ID3/C4.5 allow multi-way categorical splits
- An unconstrained tree perfectly memorises training data — always regularise
- Cost-complexity pruning is the most principled post-pruning method for CART
- MDI feature importance is fast but biased toward high-cardinality and continuous features
- Depth controls the bias-variance trade-off more directly than any other parameter

> **Practical Pruning Workflow**: Start with max_depth 3–8. Run cost_complexity_pruning_path() and plot train vs test accuracy across the alpha range. Select the largest alpha where test accuracy is near its peak — gives the simplest tree with good generalisation.

---

