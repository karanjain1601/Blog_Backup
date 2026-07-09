---
title: "Second-Order Methods — Newton and L-BFGS"
slug: "second-order-methods"
description: "Newton's method, quasi-Newton BFGS, L-BFGS with two-loop recursion, Wolfe line search, and when second-order methods beat first-order methods in practice."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmlyc3Qtb3JkZXIgbWV0aG9kcyAoU0dELCBBZGFtKSB1c2Ugb25seSBncmFkaWVudCBpbmZvcm1hdGlvbiBhbmQgdHJlYXQgYWxsIGRpcmVjdGlvbnMgYXMgZXF1YWxseSBpbXBvcnRhbnQuIFNlY29uZC1vcmRlciBtZXRob2RzIGluY29ycG9yYXRlIGN1cnZhdHVyZSBpbmZvcm1hdGlvbiB2aWEgdGhlIEhlc3NpYW4sIHdoaWNoIHJlc2NhbGVzIHRoZSBncmFkaWVudCB0byBhY2NvdW50IGZvciBkaWZmZXJlbnQgY3VydmF0dXJlcyBpbiBkaWZmZXJlbnQgZGlyZWN0aW9ucy4gVGhlIHJlc3VsdDogZmFyIGZld2VyIGl0ZXJhdGlvbnMgdG8gY29udmVyZ2VuY2UsIGF0IHRoZSBjb3N0IG9mIGNvbXB1dGluZywgc3RvcmluZywgb3IgYXBwcm94aW1hdGluZyB0aGUgSGVzc2lhbi4gRm9yIGRlZXAgbGVhcm5pbmcgd2l0aCBiaWxsaW9ucyBvZiBwYXJhbWV0ZXJzIHRoZSBmdWxsIEhlc3NpYW4gaXMgaW5mZWFzaWJsZSwgYnV0IGFwcHJveGltYXRlIHNlY29uZC1vcmRlciBtZXRob2RzIGFyZSBhbiBhY3RpdmUgcmVzZWFyY2ggYXJlYS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOZXd0b25cdTAwMjdzIE1ldGhvZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmV3dG9uXHUwMDI3cyB1cGRhdGUgaXMgeCDihpAgeCDiiJIgSOKBu8K54oiHZih4KSB3aGVyZSBIID0g4oiHwrJmKHgpLiBUaGlzIGlzIGRlcml2ZWQgZnJvbSB0aGUgc2Vjb25kLW9yZGVyIFRheWxvciBleHBhbnNpb246IGYoeCvOtCkg4omIIGYoeCkgKyDiiIdmKHgp4bWAzrQgKyAoMS8yKc604bWASM60LiBTZXR0aW5nIHRoZSBncmFkaWVudCBvZiB0aGlzIHF1YWRyYXRpYyB0byB6ZXJvIGdpdmVzIM60ID0g4oiSSOKBu8K54oiHZiDigJQgdGhlIGV4YWN0IG1pbmltaXplciBvZiB0aGUgbG9jYWwgcXVhZHJhdGljIGFwcHJveGltYXRpb24uIEZvciBzdHJpY3RseSBjb252ZXggcXVhZHJhdGljcyBOZXd0b24gY29udmVyZ2VzIGluIGV4YWN0bHkgb25lIHN0ZXA7IGZvciBnZW5lcmFsIHNtb290aCBmdW5jdGlvbnMgaXQgYWNoaWV2ZXMgcXVhZHJhdGljIGNvbnZlcmdlbmNlIG5lYXIgdGhlIG1pbmltdW0gKHRoZSBudW1iZXIgb2YgY29ycmVjdCBkZWNpbWFsIGRpZ2l0cyByb3VnaGx5IGRvdWJsZXMgZWFjaCBpdGVyYXRpb24pLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUXVhZHJhdGljIENvbnZlcmdlbmNlIiwiY29udGVudCI6Ik5ld3Rvblx1MDAyN3MgbWV0aG9kIGNvbnZlcmdlcyBxdWFkcmF0aWNhbGx5OiDigJZ4X3trKzF9IOKIkiB4KuKAliDiiaQgQ8K34oCWeOKCliDiiJIgeCrigJbCsi4gSWYgdGhlIGN1cnJlbnQgZXJyb3IgaXMgzrUsIHRoZSBuZXh0IGVycm9yIGlzIE8ozrXCsikuIFN0YXJ0aW5nIGZyb20gZXJyb3IgMC4xOiBuZXh0IHN0ZXBzIGFyZSB+MC4wMSwgfjAuMDAwMSwgfjEw4oG74oG4LiBUaGlzIGlzIGV4cG9uZW50aWFsbHkgZmFzdGVyIHRoYW4gZ3JhZGllbnQgZGVzY2VudFx1MDAyN3MgbGluZWFyIGNvbnZlcmdlbmNlIOKAlnjigpbigorigoHiiJJ4KuKAliDiiaQgKDHiiJLOvC9MKeKAlnjigpbiiJJ4KuKAli4gSW4gcHJhY3RpY2UgTmV3dG9uIG5lZWRzIG9ubHkgNeKAkzIwIGl0ZXJhdGlvbnMgd2hlcmUgR0QgbmVlZHMgdGhvdXNhbmRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG5ld3RvbnNfbWV0aG9kKGYsIGdyYWRfZiwgaGVzc19mLCB4MCwgdG9sPTFlLTEwLCBtYXhfaXRlcj0yNSk6XG4gICAgXCJcIlwiTmV3dG9uXHUwMDI3cyBtZXRob2Q6IHhfe2srMX0gPSB4X2sgLSBIKHhfayleey0xfSAqIGdyYWRfZih4X2spLlwiXCJcIlxuICAgIHggPSB4MC5jb3B5KClcbiAgICBoaXN0b3J5ID0gW11cbiAgICBmb3IgayBpbiByYW5nZShtYXhfaXRlcik6XG4gICAgICAgIGcgPSBncmFkX2YoeClcbiAgICAgICAgSCA9IGhlc3NfZih4KVxuICAgICAgICBzdGVwID0gbnAubGluYWxnLnNvbHZlKEgsIGcpICAjIG1vcmUgc3RhYmxlIHRoYW4gSF57LTF9IEAgZ1xuICAgICAgICB4ID0geCAtIHN0ZXBcbiAgICAgICAgZ3JhZF9ub3JtID0gbnAubGluYWxnLm5vcm0oZ3JhZF9mKHgpKVxuICAgICAgICBoaXN0b3J5LmFwcGVuZCh7XHUwMDI3aXRlclx1MDAyNzogaysxLCBcdTAwMjdmXHUwMDI3OiBmKHgpLCBcdTAwMjdncmFkX25vcm1cdTAwMjc6IGdyYWRfbm9ybX0pXG4gICAgICAgIGlmIGdyYWRfbm9ybSBcdTAwM2MgdG9sOlxuICAgICAgICAgICAgYnJlYWtcbiAgICByZXR1cm4geCwgaGlzdG9yeVxuXG4jIGYoeCx5KSA9IDJ4XjIgKyB4eSArIDN5XjIgLSA0eCAtIDZ5ICAoc3RyaWN0bHkgY29udmV4IHF1YWRyYXRpYylcbmRlZiBmKHYpOiAgICAgIHJldHVybiAyKnZbMF0qKjIgKyB2WzBdKnZbMV0gKyAzKnZbMV0qKjIgLSA0KnZbMF0gLSA2KnZbMV1cbmRlZiBncmFkX2Yodik6IHJldHVybiBucC5hcnJheShbNCp2WzBdK3ZbMV0tNCwgdlswXSs2KnZbMV0tNl0pXG5kZWYgaGVzc19mKHYpOiByZXR1cm4gbnAuYXJyYXkoW1s0LjAsIDEuMF0sIFsxLjAsIDYuMF1dKVxuXG54MCA9IG5wLmFycmF5KFs0LjAsIDQuMF0pXG54X29wdCwgaGlzdCA9IG5ld3RvbnNfbWV0aG9kKGYsIGdyYWRfZiwgaGVzc19mLCB4MClcblxucHJpbnQoZlwiTmV3dG9uXHUwMDI3cyBtZXRob2Qgb24gMkQgcXVhZHJhdGljIChzdGFydDoge3gwfSlcIilcbnByaW50KGZcIntcdTAwMjdJdGVyXHUwMDI3Olx1MDAzYzZ9IHtcdTAwMjdmKHgpXHUwMDI3Olx1MDAzZTE0fSB7XHUwMDI3fHxncmFkfHxcdTAwMjc6XHUwMDNlMTR9XCIpXG5mb3IgaCBpbiBoaXN0OlxuICAgIHByaW50KGZcIntoW1x1MDAyN2l0ZXJcdTAwMjddOlx1MDAzYzZ9IHtoW1x1MDAyN2ZcdTAwMjddOlx1MDAzZTE0LjhmfSB7aFtcdTAwMjdncmFkX25vcm1cdTAwMjddOlx1MDAzZTE0LjJlfVwiKVxucHJpbnQoZlwiXFxuT3B0aW11bToge3hfb3B0fVwiKVxucHJpbnQoXCJRdWFkcmF0aWMgY29udmVyZ2VuY2U6IGVycm9yIHNxdWFyZWQgZWFjaCBzdGVwLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBOZXd0b24gSXMgSW1wcmFjdGljYWwgZm9yIERlZXAgTGVhcm5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIG1vZGVsIHdpdGggbiBwYXJhbWV0ZXJzLCB0aGUgSGVzc2lhbiBpcyBhbiBuw5duIG1hdHJpeC4gV2l0aCBuPTEw4oG4IChhIG1lZGl1bS1zaXplZCBuZXVyYWwgbmV0d29yayksIHN0b3JpbmcgdGhlIEhlc3NpYW4gcmVxdWlyZXMgMTDCueKBtiBieXRlcyDigJQgdmFzdGx5IG1vcmUgdGhhbiBhbnkgR1BVIG1lbW9yeS4gRXZlbiBjb21wdXRpbmcgSGVzc2lhbi12ZWN0b3IgcHJvZHVjdHMgKHdoaWNoIGF2b2lkIGV4cGxpY2l0IHN0b3JhZ2UpIHJlcXVpcmVzIG9uZSBiYWNrd2FyZCBwYXNzIHBlciB2ZWN0b3IgYW5kIHlvdSBuZWVkIE8obikgc3VjaCBwcm9kdWN0cyBmb3IgTGFuY3pvcy4gSW52ZXJ0aW5nIG9yIGZhY3RvcmluZyB0aGUgSGVzc2lhbiBpcyBPKG7Csykg4oCUIGNvbXBsZXRlbHkgaW5mZWFzaWJsZS4gVGhlc2UgYmFycmllcnMgbW90aXZhdGUgcXVhc2ktTmV3dG9uIG1ldGhvZHMgdGhhdCBhcHByb3hpbWF0ZSBI4oG7wrkgY2hlYXBseS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkhlc3NpYW4gc3RvcmFnZTogTyhuwrIpIOKAlCAxMOKBuCBwYXJhbXMg4oaSIDEwwrnigbYgYnl0ZXMgKDEwIHBldGFieXRlcykiLCJIZXNzaWFuIGNvbXB1dGF0aW9uOiBPKG7CsikgZm9yd2FyZC9iYWNrd2FyZCBwYXNzZXMgaW4gbmFpdmUgaW1wbGVtZW50YXRpb24iLCJIZXNzaWFuLXZlY3RvciBwcm9kdWN0OiBPKG4pIHZpYSBhdXRvZGlmZiDigJQgb25lIGJhY2t3YXJkIHBhc3MgcGVyIHZlY3RvciIsIkhlc3NpYW4gaW52ZXJzaW9uOiBPKG7Csykg4oCUIGluZmVhc2libGUgZXZlbiBmb3Igbj0xMOKBtCIsIk1pbmktYmF0Y2ggZ3JhZGllbnRzIGFyZSBub2lzeTogc2Vjb25kLW9yZGVyIG1ldGhvZHMgYXNzdW1lIGFjY3VyYXRlIGdyYWRpZW50LCBicmVhayB1bmRlciBub2lzZSIsIk5vbi1jb252ZXggbGFuZHNjYXBlczogSCBtYXkgYmUgaW5kZWZpbml0ZSAoc2FkZGxlKSwgY2F1c2luZyBOZXd0b24gdG8gYXNjZW5kIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlF1YXNpLU5ld3RvbiBhbmQgdGhlIFNlY2FudCBFcXVhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUXVhc2ktTmV3dG9uIG1ldGhvZHMgYnVpbGQgdXAgYW4gYXBwcm94aW1hdGlvbiBC4oKWIOKJiCBIKHjigpYpIChvciBpdHMgaW52ZXJzZSBI4oKWIOKJiCBI4oG7wrkpIGZyb20gZ3JhZGllbnQgZGlmZmVyZW5jZXMuIFRoZSBzZWNhbnQgZXF1YXRpb24gcmVxdWlyZXM6IELigpbigorigoHCt3PigpYgPSB54oKWIHdoZXJlIHPigpYgPSB44oKW4oKK4oKB4oiSeOKCliAoc3RlcCkgYW5kIHnigpYgPSDiiIdmKHjigpbigorigoEp4oiS4oiHZih44oKWKSAoZ3JhZGllbnQgZGlmZmVyZW5jZSkuIFRoaXMgc2F5cyB0aGUgYXBwcm94aW1hdGUgSGVzc2lhbiBzaG91bGQgc2F0aXNmeSB0aGUgZmlyc3Qtb3JkZXIgY29uZGl0aW9uOiB0aGUgcXVhZHJhdGljIG1vZGVsIG1hdGNoZXMgdGhlIG9ic2VydmVkIGdyYWRpZW50IGNoYW5nZS4gQkZHUyBhcHBsaWVzIGEgcmFuay0yIHVwZGF0ZSB0byB0aGUgaW52ZXJzZSBIZXNzaWFuIHRoYXQgc2F0aXNmaWVzIHRoZSBzZWNhbnQgZXF1YXRpb24gYW5kIG1haW50YWlucyBwb3NpdGl2ZSBkZWZpbml0ZW5lc3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTC1CRkdTOiBMaW1pdGVkIE1lbW9yeSBCRkdTIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMLUJGR1MgKE5vY2VkYWwgMTk4MCkgYXZvaWRzIHN0b3JpbmcgdGhlIGZ1bGwgbsOXbiBpbnZlcnNlIEhlc3NpYW4gYXBwcm94aW1hdGlvbiBieSBrZWVwaW5nIG9ubHkgdGhlIGxhc3QgbSBwYWlycyB7KHPigpYsIHnigpYpfSBvZiBzdGVwIGFuZCBncmFkaWVudC1kaWZmZXJlbmNlIHZlY3RvcnMuIFRoZSBtYXRyaXgtdmVjdG9yIHByb2R1Y3QgSOKClsK3cSBpcyBjb21wdXRlZCBpbXBsaWNpdGx5IHVzaW5nIHRoZSB0d28tbG9vcCByZWN1cnNpb246IGl0IHRha2VzIE8obW4pIHRpbWUgYW5kIE8obW4pIG1lbW9yeSDigJQgZHJhbWF0aWNhbGx5IGJldHRlciB0aGFuIE8obsKyKS4gV2l0aCBtPTEw4oCTMjAsIEwtQkZHUyBhY2hpZXZlcyBuZWFyLUJGR1MgY29udmVyZ2VuY2Ugb24gc21vb3RoIG9iamVjdGl2ZXMuIEl0IHJlcXVpcmVzIGZ1bGwtYmF0Y2ggKG9yIHZlcnkgbGFyZ2UtYmF0Y2gpIGdyYWRpZW50czsgbm9pc3kgbWluaS1iYXRjaCBncmFkaWVudHMgY2F1c2UgdGhlIHNlY2FudCBjb25kaXRpb24gdG8gYmUgcG9vcmx5IHNhdGlzZmllZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6dHJ1ZSwiaXRlbXMiOlsiU3RvcmUgbGFzdCBtIHBhaXJzOiBz4oKWID0geOKCluKCiuKCgeKIknjigpYsIHnigpYgPSDiiIdmKHjigpbigorigoEp4oiS4oiHZih44oKWKSIsIlR3by1sb29wIHJlY3Vyc2lvbjogY29tcHV0ZSBI4oKWwrdnIHdpdGhvdXQgZm9ybWluZyBI4oKWIGV4cGxpY2l0bHkgaW4gTyhtbikiLCJEaXJlY3Rpb246IHDigpYgPSDiiJJI4oKWwrfiiIdmKHjigpYpIChhcHByb3hpbWF0ZSBOZXd0b24gc3RlcCkiLCJMaW5lIHNlYXJjaDogZmluZCDOseKCliBzYXRpc2Z5aW5nIFdvbGZlIGNvbmRpdGlvbnMgKHN1ZmZpY2llbnQgZGVjcmVhc2UgKyBjdXJ2YXR1cmUgY29uZGl0aW9uKSIsIlVwZGF0ZTogeOKCluKCiuKCgSA9IHjigpYgKyDOseKClsK3cOKCljsgc3RvcmUgbmV3IChzLCB5KSBwYWlyOyBkaXNjYXJkIG9sZGVzdCBpZiBidWZmZXIgZnVsbCJdfSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiTWVtb3J5IiwiQ29udmVyZ2VuY2UgUmF0ZSIsIk5vaXN5IEdyYWRpZW50cyIsIlR5cGljYWwgVXNlIl0sInJvd3MiOltbIkdyYWRpZW50IERlc2NlbnQiLCJPKG4pIiwiTGluZWFyOiAoMS3OvC9MKeG1jyIsIlJvYnVzdCAoU0dEKSIsIkxhcmdlLXNjYWxlIERMIG1pbmktYmF0Y2giXSxbIk5ld3RvbiIsIk8obsKyKSIsIlF1YWRyYXRpYyBuZWFyIHgqIiwiVmVyeSBzZW5zaXRpdmUiLCJUaW55IG4sIHdlbGwtY29uZGl0aW9uZWQiXSxbIkJGR1MiLCJPKG7CsikiLCJTdXBlcmxpbmVhciIsIlNlbnNpdGl2ZSIsIk1lZGl1bSBuIGZ1bGwtYmF0Y2giXSxbIkwtQkZHUyIsIk8obW4pIiwiU3VwZXJsaW5lYXIgKG5lYXIgQkZHUykiLCJTZW5zaXRpdmUiLCJNb2RlcmF0ZSBuLCBmdWxsL2xhcmdlIGJhdGNoIl0sWyJBZGFtIiwiTyhuKSIsIkFkYXB0aXZlLCBwcmFjdGljYWwiLCJSb2J1c3QiLCJMYXJnZS1zY2FsZSBETCwgbWluaS1iYXRjaCJdLFsiSy1GQUMiLCJPKG4gKyBsYXllcsKyKSIsIk5lYXItcXVhZHJhdGljIChGaXNoZXIpIiwiTW9kZXJhdGUiLCJETCB3aXRoIEtyb25lY2tlciBhcHByb3giXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5pbXBvcnQgdGltZVxuXG5kZWYgcm9zZW5icm9jayh4KTpcbiAgICByZXR1cm4gc3VtKDEwMCooeFtpKzFdLXhbaV0qKjIpKioyICsgKDEteFtpXSkqKjIgZm9yIGkgaW4gcmFuZ2UobGVuKHgpLTEpKVxuXG5kZWYgcm9zZW5icm9ja19ncmFkKHgpOlxuICAgIGcgPSBucC56ZXJvc19saWtlKHgpXG4gICAgZm9yIGkgaW4gcmFuZ2UobGVuKHgpLTEpOlxuICAgICAgICBnW2ldICAgKz0gLTQwMCp4W2ldKih4W2krMV0teFtpXSoqMikgLSAyKigxLXhbaV0pXG4gICAgICAgIGdbaSsxXSArPSAyMDAqKHhbaSsxXS14W2ldKioyKVxuICAgIHJldHVybiBnXG5cbm5wLnJhbmRvbS5zZWVkKDcpXG5uID0gNDBcbngwID0gbnAucmFuZG9tLnJhbmRuKG4pICogMC41XG5cbmNvbmZpZ3MgPSBbXG4gICAgKFx1MDAyN0wtQkZHUy1CXHUwMDI3LCBkaWN0KG1ldGhvZD1cdTAwMjdMLUJGR1MtQlx1MDAyNywgamFjPXJvc2VuYnJvY2tfZ3JhZCxcbiAgICAgICAgICAgICAgICAgICAgICBvcHRpb25zPXtcdTAwMjdtYXhpdGVyXHUwMDI3OiAyMDAwLCBcdTAwMjdmdG9sXHUwMDI3OjFlLTE1LCBcdTAwMjdndG9sXHUwMDI3OjFlLTEwfSkpLFxuICAgIChcdTAwMjdDR1x1MDAyNywgICAgICAgZGljdChtZXRob2Q9XHUwMDI3Q0dcdTAwMjcsIGphYz1yb3NlbmJyb2NrX2dyYWQsXG4gICAgICAgICAgICAgICAgICAgICAgb3B0aW9ucz17XHUwMDI3bWF4aXRlclx1MDAyNzogNTAwMCwgXHUwMDI3Z3RvbFx1MDAyNzoxZS0xMH0pKSxcbiAgICAoXHUwMDI3TmVsZGVyLU1lYWRcdTAwMjcsIGRpY3QobWV0aG9kPVx1MDAyN05lbGRlci1NZWFkXHUwMDI3LFxuICAgICAgICAgICAgICAgICAgICAgICAgIG9wdGlvbnM9e1x1MDAyN21heGl0ZXJcdTAwMjc6IDUwMDAwLCBcdTAwMjd4YXRvbFx1MDAyNzoxZS04fSkpLFxuXVxuXG5wcmludChmXCJSb3NlbmJyb2NrIChuPXtufSkgIGdsb2JhbCBtaW4gPSAwLjBcIilcbnByaW50KGZcIntcdTAwMjdNZXRob2RcdTAwMjc6XHUwMDNjMTR9IHtcdTAwMjdGaW5hbCBmXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3SXRlcnNcdTAwMjc6XHUwMDNlOH0ge1x1MDAyN1RpbWUocylcdTAwMjc6XHUwMDNlOX1cIilcbmZvciBuYW1lLCBrd2FyZ3MgaW4gY29uZmlnczpcbiAgICB0MCA9IHRpbWUudGltZSgpXG4gICAgcmVzID0gbWluaW1pemUocm9zZW5icm9jaywgeDAuY29weSgpLCAqKmt3YXJncylcbiAgICBwcmludChmXCJ7bmFtZTpcdTAwM2MxNH0ge3Jlcy5mdW46XHUwMDNlMTIuMmV9IHtyZXMubml0Olx1MDAzZTh9IHt0aW1lLnRpbWUoKS10MDpcdTAwM2U5LjNmfVwiKVxucHJpbnQoXCJcXG5MLUJGR1MtQiB1c2VzIGxhc3QgbT0xMCBncmFkaWVudCBwYWlyczsgTyhtbikgbWVtb3J5IHZzIE8obsKyKSBmb3IgZnVsbCBCRkdTLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkwtQkZHUyBpbiBQeVRvcmNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQeVRvcmNoIHByb3ZpZGVzIHRvcmNoLm9wdGltLkxCRkdTIHdoaWNoIHJlcXVpcmVzIGEgY2xvc3VyZSDigJQgYSBjYWxsYWJsZSB0aGF0IHJlY29tcHV0ZXMgYW5kIHJldHVybnMgdGhlIGxvc3MuIFRoaXMgaXMgbmVjZXNzYXJ5IGJlY2F1c2UgTC1CRkdTIHBlcmZvcm1zIGludGVybmFsIGxpbmUgc2VhcmNoIHdpdGggbXVsdGlwbGUgZnVuY3Rpb24gZXZhbHVhdGlvbnMgcGVyIHN0ZXAuIFRoZSBzdHJvbmcgV29sZmUgbGluZSBzZWFyY2ggKGN1cnZhdHVyZSBjb25kaXRpb24pIGVuc3VyZXMgdGhlIHN0ZXAgc2F0aXNmaWVzIHRoZSBzZWNhbnQgZXF1YXRpb24gd2VsbCwgd2hpY2ggaXMgY3JpdGljYWwgZm9yIGJ1aWxkaW5nIGEgZ29vZCBIZXNzaWFuIGFwcHJveGltYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFNtYWxsTmV0KG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfaW49OCwgaGlkZGVuPTI0LCBkX291dD0xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkX2luLCBoaWRkZW4pLCBubi5UYW5oKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCBoaWRkZW4pLCBubi5UYW5oKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCBkX291dClcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbm1vZGVsID0gU21hbGxOZXQoKVxub3B0aW1pemVyID0gdG9yY2gub3B0aW0uTEJGR1MoXG4gICAgbW9kZWwucGFyYW1ldGVycygpLFxuICAgIGxyPTAuMSxcbiAgICBtYXhfaXRlcj0yMCwgICAgICAgICAgICMgaW5uZXIgQ0cgaXRlcmF0aW9ucyBwZXIgb3B0aW1pemVyLnN0ZXAoKVxuICAgIG1heF9ldmFsPTI1LCAgICAgICAgICAgIyBtYXggZnVuY3Rpb24gZXZhbHVhdGlvbnMgcGVyIHN0ZXBcbiAgICBoaXN0b3J5X3NpemU9MTAsICAgICAgICMgbTogbnVtYmVyIG9mIChzLHkpIHBhaXJzIHN0b3JlZFxuICAgIGxpbmVfc2VhcmNoX2ZuPVx1MDAyN3N0cm9uZ193b2xmZVx1MDAyN1xuKVxuXG5YID0gdG9yY2gucmFuZG4oMTI4LCA4KVxueV90cnVlID0gdG9yY2guc2luKFhbOiwgOjFdKSArIDAuMSAqIHRvcmNoLnJhbmRuKDEyOCwgMSlcbmxvc3NfZm4gPSBubi5NU0VMb3NzKClcblxuZGVmIGNsb3N1cmUoKTpcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzID0gbG9zc19mbihtb2RlbChYKSwgeV90cnVlKVxuICAgIGxvc3MuYmFja3dhcmQoKVxuICAgIHJldHVybiBsb3NzXG5cbnByaW50KFwiTC1CRkdTIHRyYWluaW5nIHdpdGggc3Ryb25nIFdvbGZlIGxpbmUgc2VhcmNoOlwiKVxubG9zc2VzID0gW11cbmZvciBzdGVwIGluIHJhbmdlKDI1KTpcbiAgICBsb3NzID0gb3B0aW1pemVyLnN0ZXAoY2xvc3VyZSlcbiAgICBsb3NzZXMuYXBwZW5kKGxvc3MuaXRlbSgpKVxuICAgIGlmIHN0ZXAgJSA1ID09IDA6XG4gICAgICAgIHByaW50KGZcIiAgU3RlcCB7c3RlcDozZH06IGxvc3M9e2xvc3MuaXRlbSgpOi42Zn1cIilcbnByaW50KGZcIlxcbkZpbmFsIGxvc3M6IHtsb3NzZXNbLTFdOi42Zn1cIilcbnByaW50KGZcIlJlZHVjdGlvbjoge2xvc3Nlc1swXS9sb3NzZXNbLTFdOi4xZn14IGluIDI1IHN0ZXBzXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udmVyZ2VuY2UgUmF0ZSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPbiBxdWFkcmF0aWMgcHJvYmxlbXMsIHRoZSBjb252ZXJnZW5jZSBhZHZhbnRhZ2Ugb2YgTmV3dG9uIG92ZXIgZ3JhZGllbnQgZGVzY2VudCBpcyBtb3N0IGNsZWFybHkgdmlzaWJsZTogTmV3dG9uIGNvbnZlcmdlcyBpbiBhIG51bWJlciBvZiBzdGVwcyBlcXVhbCB0byB0aGUgbnVtYmVyIG9mIGRpc3RpbmN0IGVpZ2VudmFsdWVzIG9mIHRoZSBIZXNzaWFuIChhdCBtb3N0IG4gc3RlcHMgZm9yIG7Dl24gSCksIHdoaWxlIGdyYWRpZW50IGRlc2NlbnQgbmVlZHMgTyjOusK3bG9nKDEvzrUpKSBzdGVwcyB3aGVyZSDOuj1ML868IGlzIHRoZSBjb25kaXRpb24gbnVtYmVyLiBGb3IgaWxsLWNvbmRpdGlvbmVkIHByb2JsZW1zIChsYXJnZSDOuiksIGdyYWRpZW50IGRlc2NlbnQgaXMgb3JkZXJzIG9mIG1hZ25pdHVkZSBzbG93ZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbWFrZV9xdWFkcmF0aWMobj0yMCwgY29uZD0yMDAsIHNlZWQ9NDIpOlxuICAgIFwiXCJcIlJhbmRvbSBjb252ZXggcXVhZHJhdGljIHdpdGggY29udHJvbGxlZCBjb25kaXRpb24gbnVtYmVyLlwiXCJcIlxuICAgIG5wLnJhbmRvbS5zZWVkKHNlZWQpXG4gICAgZWlndmFscyA9IG5wLmxpbnNwYWNlKDEsIGNvbmQsIG4pXG4gICAgUSwgXyA9IG5wLmxpbmFsZy5xcihucC5yYW5kb20ucmFuZG4obiwgbikpXG4gICAgQSA9IFEgQCBucC5kaWFnKGVpZ3ZhbHMpIEAgUS5UXG4gICAgYiA9IG5wLnJhbmRvbS5yYW5kbihuKVxuICAgIHhfc3RhciA9IG5wLmxpbmFsZy5zb2x2ZShBLCBiKVxuICAgIHJldHVybiBBLCBiLCB4X3N0YXJcblxuZGVmIGdkX2Vycm9ycyhBLCBiLCB4X3N0YXIsIHN0ZXBzPTMwMCk6XG4gICAgTCA9IG5wLmxpbmFsZy5laWd2YWxzaChBKS5tYXgoKVxuICAgIHgsIGVycm9ycyA9IG5wLnplcm9zX2xpa2UoYiksIFtdXG4gICAgZm9yIF8gaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICB4ID0geCAtICgxLjAvTCkgKiAoQSBAIHggLSBiKVxuICAgICAgICBlcnJvcnMuYXBwZW5kKG5wLmxpbmFsZy5ub3JtKHggLSB4X3N0YXIpKVxuICAgIHJldHVybiBlcnJvcnNcblxuZGVmIG5ld3Rvbl9lcnJvcnMoQSwgYiwgeF9zdGFyLCBzdGVwcz0xNSk6XG4gICAgQV9pbnYgPSBucC5saW5hbGcuaW52KEEpXG4gICAgeCwgZXJyb3JzID0gbnAuemVyb3NfbGlrZShiKSwgW11cbiAgICBmb3IgXyBpbiByYW5nZShzdGVwcyk6XG4gICAgICAgIHggPSB4IC0gQV9pbnYgQCAoQSBAIHggLSBiKVxuICAgICAgICBlcnJvcnMuYXBwZW5kKG5wLmxpbmFsZy5ub3JtKHggLSB4X3N0YXIpKVxuICAgIHJldHVybiBlcnJvcnNcblxuQSwgYiwgeF9zdGFyID0gbWFrZV9xdWFkcmF0aWMobj0yMCwgY29uZD0yMDApXG5nZF9lcnIgPSBnZF9lcnJvcnMoQSwgYiwgeF9zdGFyKVxubmV3dG9uX2VyciA9IG5ld3Rvbl9lcnJvcnMoQSwgYiwgeF9zdGFyKVxuXG5kZWYgc3RlcHNfdG8oZXJyb3JzLCB0b2w9MWUtNik6XG4gICAgZm9yIGksIGUgaW4gZW51bWVyYXRlKGVycm9ycyk6XG4gICAgICAgIGlmIGUgXHUwMDNjIHRvbDogcmV0dXJuIGlcbiAgICByZXR1cm4gbGVuKGVycm9ycylcblxucHJpbnQoZlwiQ29udmVyZ2VuY2Ugb24gcXVhZHJhdGljIChuPTIwLCBjb25kaXRpb24gbnVtYmVyPTIwMClcIilcbnByaW50KGZcIntcdTAwMjdNZXRob2RcdTAwMjc6XHUwMDNjMTB9IHtcdTAwMjdTdGVwcyB0byAxZS02XHUwMDI3Olx1MDAzZTE1fSB7XHUwMDI3U3RlcHMgdG8gMWUtMTBcdTAwMjc6XHUwMDNlMTV9XCIpXG5wcmludChmXCJ7XHUwMDI3R0RcdTAwMjc6XHUwMDNjMTB9IHtzdGVwc190byhnZF9lcnIsMWUtNik6XHUwMDNlMTV9IHtzdGVwc190byhnZF9lcnIsMWUtMTApOlx1MDAzZTE1fVwiKVxucHJpbnQoZlwie1x1MDAyN05ld3Rvblx1MDAyNzpcdTAwM2MxMH0ge3N0ZXBzX3RvKG5ld3Rvbl9lcnIsMWUtNik6XHUwMDNlMTV9IHtzdGVwc190byhuZXd0b25fZXJyLDFlLTEwKTpcdTAwM2UxNX1cIilcbnByaW50KFwiXFxuR0QgZXZlcnkgNTAgc3RlcHM6XCIpXG5mb3IgaSBpbiByYW5nZSgwLCAyMDAsIDUwKTpcbiAgICBwcmludChmXCIgIFN0ZXAge2k6M2R9OiB7Z2RfZXJyW2ldOi4yZX1cIilcbnByaW50KFwiTmV3dG9uIGV2ZXJ5IHN0ZXA6XCIpXG5mb3IgaSwgZSBpbiBlbnVtZXJhdGUobmV3dG9uX2Vycls6OF0pOlxuICAgIHByaW50KGZcIiAgU3RlcCB7aTozZH06IHtlOi4yZX1cIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiV2hlbiB0byBVc2UgTC1CRkdTIHZzIEFkYW0iLCJjb250ZW50IjoiTC1CRkdTIGlzIHRoZSByaWdodCBjaG9pY2Ugd2hlbjogKDEpIHlvdSBjYW4gYWZmb3JkIGZ1bGwtYmF0Y2ggZ3JhZGllbnRzIChzbWFsbC9tZWRpdW0gZGF0YXNldCksICgyKSB0aGUgb2JqZWN0aXZlIGlzIHNtb290aCBhbmQgdGhlIEhlc3NpYW4gaXMgd2VsbC1jb25kaXRpb25lZCwgKDMpIHlvdSBuZWVkIGhpZ2gtcHJlY2lzaW9uIHNvbHV0aW9ucyAocGh5c2ljcyBzaW11bGF0aW9ucywgc2NpZW50aWZpYyBjb21wdXRpbmcpLiBBZGFtIGlzIGJldHRlciB3aGVuOiAoMSkgbWluaS1iYXRjaCBncmFkaWVudHMgYXJlIHJlcXVpcmVkIChsYXJnZSBkYXRhc2V0cyksICgyKSB0aGUgbGFuZHNjYXBlIGlzIGhpZ2hseSBub24tY29udmV4IChkZWVwIG5ldHdvcmtzKSwgKDMpIHRyYWluaW5nIG11c3QgYmUgcm9idXN0IHRvIGdyYWRpZW50IG5vaXNlLiBNYW55IHByYWN0aXRpb25lcnMgdXNlIEFkYW0gZm9yIERMIHByZXRyYWluaW5nIGFuZCBMLUJGR1MgZm9yIGZpbmUtdHVuaW5nIG9yIHNtYWxsIHN1Yi1wcm9ibGVtcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcHByb3hpbWF0ZSBTZWNvbmQtT3JkZXIgTWV0aG9kcyBmb3IgRGVlcCBMZWFybmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2V2ZXJhbCBtZXRob2RzIGFwcHJveGltYXRlIGN1cnZhdHVyZSBpbiBkZWVwIG5ldHdvcmtzIGF0IHRyYWN0YWJsZSBjb3N0LiBLLUZBQyAoS3JvbmVja2VyLUZhY3RvcmVkIEFwcHJveGltYXRlIEN1cnZhdHVyZSkgYXBwcm94aW1hdGVzIHRoZSBGaXNoZXIgaW5mb3JtYXRpb24gbWF0cml4IGFzIGEgS3JvbmVja2VyIHByb2R1Y3Qgb2Ygc21hbGxlciBtYXRyaWNlcyDigJQgb25lIHBlciBsYXllci4gVGhpcyBicmluZ3MgdGhlIHBlci1sYXllciBjb3N0IHRvIE8oZF9pbsKyICsgZF9vdXTCsikgaW5zdGVhZCBvZiBPKChkX2luwrdkX291dCnCsikuIFNoYW1wb28gc2ltaWxhcmx5IHVzZXMgS3JvbmVja2VyIHN0cnVjdHVyZSB3aXRoIGdyYWRpZW50IHNlY29uZC1tb21lbnQgbWF0cmljZXMuIFNvcGhpYSAoc2Vjb25kLW9yZGVyIGNsaXBwZWQgc3RvY2hhc3RpYyBvcHRpbWl6YXRpb24pIGNsaXBzIHRoZSBIZXNzaWFuIGRpYWdvbmFsIHRvIHByZXZlbnQgbGFyZ2Ugc3RlcHMgaW4gc2hhcnAgZGlyZWN0aW9ucy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkstRkFDOiBGaXNoZXIgYXBwcm94aW1hdGVkIGFzIEtyb25lY2tlciBwcm9kdWN0IG9mIGlucHV0IGNvdmFyaWFuY2UgYW5kIG91dHB1dCBncmFkaWVudCBjb3ZhcmlhbmNlIiwiU2hhbXBvbzogZnVsbC1tYXRyaXggQWRhR3JhZCB3aXRoIEtyb25lY2tlciBmYWN0b3IgcHJlY29uZGl0aW9uaW5nLCBPKGTCsy9tKSBwZXIgc3RlcCIsIkdhdXNzLU5ld3RvbjogYXBwcm94aW1hdGVzIEhlc3NpYW4gYXMgSuG1gEogZm9yIGxlYXN0LXNxdWFyZXMgcHJvYmxlbXMg4oCUIGFsd2F5cyBQU0QiLCJTb3BoaWE6IGNsaXBzIHBlci1wYXJhbWV0ZXIgSGVzc2lhbiBkaWFnb25hbCBlc3RpbWF0ZSB0byBib3VuZCBzdGVwIHNpemUg4oCUIHN0YWJsZSBmb3IgTExNcyIsIkFkYW0gYXMgYXBwcm94aW1hdGUgc2Vjb25kLW9yZGVyOiBkaWFnb25hbCBIZXNzaWFuIGFwcHJveGltYXRpb24gdmlhIGdyYWRpZW50IHNlY29uZCBtb21lbnRzIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Second-Order Methods — Newton and L-BFGS

First-order methods (SGD, Adam) use only gradient information and treat all directions as equally important. Second-order methods incorporate curvature information via the Hessian, which rescales the gradient to account for different curvatures in different directions. The result: far fewer iterations to convergence, at the cost of computing, storing, or approximating the Hessian. For deep learning with billions of parameters the full Hessian is infeasible, but approximate second-order methods are an active research area.

## Newton's Method

Newton's update is x ← x − H⁻¹∇f(x) where H = ∇²f(x). This is derived from the second-order Taylor expansion: f(x+δ) ≈ f(x) + ∇f(x)ᵀδ + (1/2)δᵀHδ. Setting the gradient of this quadratic to zero gives δ = −H⁻¹∇f — the exact minimizer of the local quadratic approximation. For strictly convex quadratics Newton converges in exactly one step; for general smooth functions it achieves quadratic convergence near the minimum (the number of correct decimal digits roughly doubles each iteration).

> **Quadratic Convergence**: Newton's method converges quadratically: ‖x_{k+1} − x*‖ ≤ C·‖xₖ − x*‖². If the current error is ε, the next error is O(ε²). Starting from error 0.1: next steps are ~0.01, ~0.0001, ~10⁻⁸. This is exponentially faster than gradient descent's linear convergence ‖xₖ₊₁−x*‖ ≤ (1−μ/L)‖xₖ−x*‖. In practice Newton needs only 5–20 iterations where GD needs thousands.

```python
import numpy as np

def newtons_method(f, grad_f, hess_f, x0, tol=1e-10, max_iter=25):
    """Newton's method: x_{k+1} = x_k - H(x_k)^{-1} * grad_f(x_k)."""
    x = x0.copy()
    history = []
    for k in range(max_iter):
        g = grad_f(x)
        H = hess_f(x)
        step = np.linalg.solve(H, g)  # more stable than H^{-1} @ g
        x = x - step
        grad_norm = np.linalg.norm(grad_f(x))
        history.append({'iter': k+1, 'f': f(x), 'grad_norm': grad_norm})
        if grad_norm < tol:
            break
    return x, history

# f(x,y) = 2x^2 + xy + 3y^2 - 4x - 6y  (strictly convex quadratic)
def f(v):      return 2*v[0]**2 + v[0]*v[1] + 3*v[1]**2 - 4*v[0] - 6*v[1]
def grad_f(v): return np.array([4*v[0]+v[1]-4, v[0]+6*v[1]-6])
def hess_f(v): return np.array([[4.0, 1.0], [1.0, 6.0]])

x0 = np.array([4.0, 4.0])
x_opt, hist = newtons_method(f, grad_f, hess_f, x0)

print(f"Newton's method on 2D quadratic (start: {x0})")
print(f"{'Iter':<6} {'f(x)':>14} {'||grad||':>14}")
for h in hist:
    print(f"{h['iter']:<6} {h['f']:>14.8f} {h['grad_norm']:>14.2e}")
print(f"\nOptimum: {x_opt}")
print("Quadratic convergence: error squared each step.")
```

## Why Newton Is Impractical for Deep Learning

For a model with n parameters, the Hessian is an n×n matrix. With n=10⁸ (a medium-sized neural network), storing the Hessian requires 10¹⁶ bytes — vastly more than any GPU memory. Even computing Hessian-vector products (which avoid explicit storage) requires one backward pass per vector and you need O(n) such products for Lanczos. Inverting or factoring the Hessian is O(n³) — completely infeasible. These barriers motivate quasi-Newton methods that approximate H⁻¹ cheaply.

- Hessian storage: O(n²) — 10⁸ params → 10¹⁶ bytes (10 petabytes)
- Hessian computation: O(n²) forward/backward passes in naive implementation
- Hessian-vector product: O(n) via autodiff — one backward pass per vector
- Hessian inversion: O(n³) — infeasible even for n=10⁴
- Mini-batch gradients are noisy: second-order methods assume accurate gradient, break under noise
- Non-convex landscapes: H may be indefinite (saddle), causing Newton to ascend

## Quasi-Newton and the Secant Equation

Quasi-Newton methods build up an approximation Bₖ ≈ H(xₖ) (or its inverse Hₖ ≈ H⁻¹) from gradient differences. The secant equation requires: Bₖ₊₁·sₖ = yₖ where sₖ = xₖ₊₁−xₖ (step) and yₖ = ∇f(xₖ₊₁)−∇f(xₖ) (gradient difference). This says the approximate Hessian should satisfy the first-order condition: the quadratic model matches the observed gradient change. BFGS applies a rank-2 update to the inverse Hessian that satisfies the secant equation and maintains positive definiteness.

## L-BFGS: Limited Memory BFGS

L-BFGS (Nocedal 1980) avoids storing the full n×n inverse Hessian approximation by keeping only the last m pairs {(sₖ, yₖ)} of step and gradient-difference vectors. The matrix-vector product Hₖ·q is computed implicitly using the two-loop recursion: it takes O(mn) time and O(mn) memory — dramatically better than O(n²). With m=10–20, L-BFGS achieves near-BFGS convergence on smooth objectives. It requires full-batch (or very large-batch) gradients; noisy mini-batch gradients cause the secant condition to be poorly satisfied.

1. Store last m pairs: sₖ = xₖ₊₁−xₖ, yₖ = ∇f(xₖ₊₁)−∇f(xₖ)
2. Two-loop recursion: compute Hₖ·g without forming Hₖ explicitly in O(mn)
3. Direction: pₖ = −Hₖ·∇f(xₖ) (approximate Newton step)
4. Line search: find αₖ satisfying Wolfe conditions (sufficient decrease + curvature condition)
5. Update: xₖ₊₁ = xₖ + αₖ·pₖ; store new (s, y) pair; discard oldest if buffer full

| Method | Memory | Convergence Rate | Noisy Gradients | Typical Use |
| --- | --- | --- | --- | --- |
| Gradient Descent | O(n) | Linear: (1-μ/L)ᵏ | Robust (SGD) | Large-scale DL mini-batch |
| Newton | O(n²) | Quadratic near x* | Very sensitive | Tiny n, well-conditioned |
| BFGS | O(n²) | Superlinear | Sensitive | Medium n full-batch |
| L-BFGS | O(mn) | Superlinear (near BFGS) | Sensitive | Moderate n, full/large batch |
| Adam | O(n) | Adaptive, practical | Robust | Large-scale DL, mini-batch |
| K-FAC | O(n + layer²) | Near-quadratic (Fisher) | Moderate | DL with Kronecker approx |

```python
import numpy as np
from scipy.optimize import minimize
import time

def rosenbrock(x):
    return sum(100*(x[i+1]-x[i]**2)**2 + (1-x[i])**2 for i in range(len(x)-1))

def rosenbrock_grad(x):
    g = np.zeros_like(x)
    for i in range(len(x)-1):
        g[i]   += -400*x[i]*(x[i+1]-x[i]**2) - 2*(1-x[i])
        g[i+1] += 200*(x[i+1]-x[i]**2)
    return g

np.random.seed(7)
n = 40
x0 = np.random.randn(n) * 0.5

configs = [
    ('L-BFGS-B', dict(method='L-BFGS-B', jac=rosenbrock_grad,
                      options={'maxiter': 2000, 'ftol':1e-15, 'gtol':1e-10})),
    ('CG',       dict(method='CG', jac=rosenbrock_grad,
                      options={'maxiter': 5000, 'gtol':1e-10})),
    ('Nelder-Mead', dict(method='Nelder-Mead',
                         options={'maxiter': 50000, 'xatol':1e-8})),
]

print(f"Rosenbrock (n={n})  global min = 0.0")
print(f"{'Method':<14} {'Final f':>12} {'Iters':>8} {'Time(s)':>9}")
for name, kwargs in configs:
    t0 = time.time()
    res = minimize(rosenbrock, x0.copy(), **kwargs)
    print(f"{name:<14} {res.fun:>12.2e} {res.nit:>8} {time.time()-t0:>9.3f}")
print("\nL-BFGS-B uses last m=10 gradient pairs; O(mn) memory vs O(n²) for full BFGS.")
```

## L-BFGS in PyTorch

PyTorch provides torch.optim.LBFGS which requires a closure — a callable that recomputes and returns the loss. This is necessary because L-BFGS performs internal line search with multiple function evaluations per step. The strong Wolfe line search (curvature condition) ensures the step satisfies the secant equation well, which is critical for building a good Hessian approximation.

```python
import torch
import torch.nn as nn

class SmallNet(nn.Module):
    def __init__(self, d_in=8, hidden=24, d_out=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_in, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, d_out)
        )
    def forward(self, x):
        return self.net(x)

torch.manual_seed(0)
model = SmallNet()
optimizer = torch.optim.LBFGS(
    model.parameters(),
    lr=0.1,
    max_iter=20,           # inner CG iterations per optimizer.step()
    max_eval=25,           # max function evaluations per step
    history_size=10,       # m: number of (s,y) pairs stored
    line_search_fn='strong_wolfe'
)

X = torch.randn(128, 8)
y_true = torch.sin(X[:, :1]) + 0.1 * torch.randn(128, 1)
loss_fn = nn.MSELoss()

def closure():
    optimizer.zero_grad()
    loss = loss_fn(model(X), y_true)
    loss.backward()
    return loss

print("L-BFGS training with strong Wolfe line search:")
losses = []
for step in range(25):
    loss = optimizer.step(closure)
    losses.append(loss.item())
    if step % 5 == 0:
        print(f"  Step {step:3d}: loss={loss.item():.6f}")
print(f"\nFinal loss: {losses[-1]:.6f}")
print(f"Reduction: {losses[0]/losses[-1]:.1f}x in 25 steps")
```

## Convergence Rate Comparison

On quadratic problems, the convergence advantage of Newton over gradient descent is most clearly visible: Newton converges in a number of steps equal to the number of distinct eigenvalues of the Hessian (at most n steps for n×n H), while gradient descent needs O(κ·log(1/ε)) steps where κ=L/μ is the condition number. For ill-conditioned problems (large κ), gradient descent is orders of magnitude slower.

```python
import numpy as np

def make_quadratic(n=20, cond=200, seed=42):
    """Random convex quadratic with controlled condition number."""
    np.random.seed(seed)
    eigvals = np.linspace(1, cond, n)
    Q, _ = np.linalg.qr(np.random.randn(n, n))
    A = Q @ np.diag(eigvals) @ Q.T
    b = np.random.randn(n)
    x_star = np.linalg.solve(A, b)
    return A, b, x_star

def gd_errors(A, b, x_star, steps=300):
    L = np.linalg.eigvalsh(A).max()
    x, errors = np.zeros_like(b), []
    for _ in range(steps):
        x = x - (1.0/L) * (A @ x - b)
        errors.append(np.linalg.norm(x - x_star))
    return errors

def newton_errors(A, b, x_star, steps=15):
    A_inv = np.linalg.inv(A)
    x, errors = np.zeros_like(b), []
    for _ in range(steps):
        x = x - A_inv @ (A @ x - b)
        errors.append(np.linalg.norm(x - x_star))
    return errors

A, b, x_star = make_quadratic(n=20, cond=200)
gd_err = gd_errors(A, b, x_star)
newton_err = newton_errors(A, b, x_star)

def steps_to(errors, tol=1e-6):
    for i, e in enumerate(errors):
        if e < tol: return i
    return len(errors)

print(f"Convergence on quadratic (n=20, condition number=200)")
print(f"{'Method':<10} {'Steps to 1e-6':>15} {'Steps to 1e-10':>15}")
print(f"{'GD':<10} {steps_to(gd_err,1e-6):>15} {steps_to(gd_err,1e-10):>15}")
print(f"{'Newton':<10} {steps_to(newton_err,1e-6):>15} {steps_to(newton_err,1e-10):>15}")
print("\nGD every 50 steps:")
for i in range(0, 200, 50):
    print(f"  Step {i:3d}: {gd_err[i]:.2e}")
print("Newton every step:")
for i, e in enumerate(newton_err[:8]):
    print(f"  Step {i:3d}: {e:.2e}")
```

> **When to Use L-BFGS vs Adam**: L-BFGS is the right choice when: (1) you can afford full-batch gradients (small/medium dataset), (2) the objective is smooth and the Hessian is well-conditioned, (3) you need high-precision solutions (physics simulations, scientific computing). Adam is better when: (1) mini-batch gradients are required (large datasets), (2) the landscape is highly non-convex (deep networks), (3) training must be robust to gradient noise. Many practitioners use Adam for DL pretraining and L-BFGS for fine-tuning or small sub-problems.

## Approximate Second-Order Methods for Deep Learning

Several methods approximate curvature in deep networks at tractable cost. K-FAC (Kronecker-Factored Approximate Curvature) approximates the Fisher information matrix as a Kronecker product of smaller matrices — one per layer. This brings the per-layer cost to O(d_in² + d_out²) instead of O((d_in·d_out)²). Shampoo similarly uses Kronecker structure with gradient second-moment matrices. Sophia (second-order clipped stochastic optimization) clips the Hessian diagonal to prevent large steps in sharp directions.

- K-FAC: Fisher approximated as Kronecker product of input covariance and output gradient covariance
- Shampoo: full-matrix AdaGrad with Kronecker factor preconditioning, O(d³/m) per step
- Gauss-Newton: approximates Hessian as JᵀJ for least-squares problems — always PSD
- Sophia: clips per-parameter Hessian diagonal estimate to bound step size — stable for LLMs
- Adam as approximate second-order: diagonal Hessian approximation via gradient second moments

---

