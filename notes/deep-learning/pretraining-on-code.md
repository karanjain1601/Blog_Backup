---
title: "Pretraining on Code — Code Understanding, Math Reasoning, and Transfer Benefits"
slug: "pretraining-on-code"
description: "How including code in LLM pretraining improves reasoning, structured generation, and math benchmarks — covering quality filtering, language distribution, mixed training strategies, and transfer evidence."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT25lIG9mIHRoZSBtb3N0IHN1cnByaXNpbmcgZmluZGluZ3MgaW4gTExNIHJlc2VhcmNoIGlzIHRoYXQgcHJldHJhaW5pbmcgb24gY29kZSBkcmFtYXRpY2FsbHkgaW1wcm92ZXMgcGVyZm9ybWFuY2Ugb24gdGFza3MgdGhhdCBoYXZlIG5vdGhpbmcgdG8gZG8gd2l0aCBwcm9ncmFtbWluZyDigJQgbWF0aGVtYXRpY2FsIHJlYXNvbmluZywgbXVsdGktc3RlcCBsb2dpYywgYW5kIHN0cnVjdHVyZWQgaW5zdHJ1Y3Rpb24gZm9sbG93aW5nLiBHUFQtNCwgTExhTUEtMywgYW5kIERlZXBTZWVrIGFsbCBpbmNsdWRlIHN1YnN0YW50aWFsIGNvZGUgaW4gdGhlaXIgcHJldHJhaW5pbmcgbWl4dHVyZXMsIGFuZCBhYmxhdGlvbiBzdHVkaWVzIGNvbnNpc3RlbnRseSBzaG93IHRoYXQgcmVtb3ZpbmcgY29kZSBodXJ0cyBOTCByZWFzb25pbmcgYmVuY2htYXJrcy4gUGhpLTIsIGEgMi43QiBwYXJhbWV0ZXIgbW9kZWwgdHJhaW5lZCBhbG1vc3QgZW50aXJlbHkgb24gY29kZSBhbmQgc3ludGhldGljIHRleHRib29rIGRhdGEsIG91dHBlcmZvcm1lZCAxM0IgbW9kZWxzIHRyYWluZWQgb24gbmF0dXJhbCBsYW5ndWFnZSBhdCB0aGUgdGltZSBvZiBpdHMgcmVsZWFzZS4gVW5kZXJzdGFuZGluZyB3aHkgY29kZSBoZWxwcyDigJQgYW5kIGhvdyB0byBpbmNvcnBvcmF0ZSBpdCBlZmZlY3RpdmVseSDigJQgaXMgZXNzZW50aWFsIGZvciBwcmV0cmFpbmluZyBwcmFjdGl0aW9uZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBDb2RlIFByZXRyYWluaW5nIEltcHJvdmVzIFJlYXNvbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29kZSBoYXMgc3RydWN0dXJhbCBwcm9wZXJ0aWVzIHRoYXQgbmF0dXJhbCBsYW5ndWFnZSBsYWNrcy4gRXZlcnkgZnVuY3Rpb24gaGFzIGFuIGV4cGxpY2l0IGlucHV0LW91dHB1dCBjb250cmFjdCBlbmZvcmNlZCBieSBleGVjdXRpb24uIENvbnRyb2wgZmxvdyAobG9vcHMsIGNvbmRpdGlvbmFscywgcmVjdXJzaW9uKSB0ZWFjaGVzIHRoZSBtb2RlbCB0byByZWFzb24gYWJvdXQgc3RhdGUgYWNyb3NzIG11bHRpcGxlIHN0ZXBzLiBUeXBlIHN5c3RlbXMgZW5mb3JjZSBwcmVjaXNpb24gYWJvdXQgd2hhdCBvcGVyYXRpb25zIGFyZSB2YWxpZC4gQ29tbWVudHMgZXhwbGFpbiB0aGUgcmVhc29uaW5nIGJlaGluZCB0aGUgY29kZSwgbm90IGp1c3Qgd2hhdCBpdCBkb2VzIOKAlCB0ZWFjaGluZyB0aGUgbW9kZWwgdG8gYXJ0aWN1bGF0ZSBpbnRlcm1lZGlhdGUgcmVhc29uaW5nIHN0ZXBzLiBUaGVzZSBwcm9wZXJ0aWVzIGFsaWduIGNsb3NlbHkgd2l0aCB3aGF0IGlzIG5lZWRlZCBmb3IgY2hhaW4tb2YtdGhvdWdodCByZWFzb25pbmcgb24gbWF0aCBhbmQgbG9naWMgcHJvYmxlbXM6IHByZWNpc2Ugc3RlcCBzZXF1ZW5jaW5nLCBzdGF0ZSB0cmFja2luZywgYW5kIGV4cGxpY2l0IGludGVybWVkaWF0ZSBjb21wdXRhdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlByZWNpc2Ugc3ludGF4OiBleGFjdCB0b2tlbiBzZXF1ZW5jZXMgcmVxdWlyZWQgZm9yIHZhbGlkIHByb2dyYW1zIOKAlCBmb3JjZXMgc3RydWN0dXJlZCBnZW5lcmF0aW9uIiwiU3RlcC1ieS1zdGVwIGNvbXB1dGF0aW9uOiBsb29wcyBhbmQgcmVjdXJzaW9uIHRlYWNoIG11bHRpLXN0ZXAgc3RhdGUgdHJhY2tpbmciLCJDb21tZW50cyBhbmQgZG9jc3RyaW5nczogbW9kZWxzIGxlYXJuIHRvIGV4cGxhaW4gbG9naWMgaW4gbmF0dXJhbCBsYW5ndWFnZSBhZGphY2VudCB0byBjb2RlIiwiRnVuY3Rpb24gc2lnbmF0dXJlczogdGVhY2ggYWJzdHJhY3Rpb24g4oCUIHNlcGFyYXRpbmcgaW50ZXJmYWNlIGZyb20gaW1wbGVtZW50YXRpb24iLCJUZXN0IGNhc2VzOiBleGFtcGxlcyBvZiBpbnB1dC1vdXRwdXQgcGFpcnMgdGhhdCBkZW1vbnN0cmF0ZSBpbnRlbmRlZCBiZWhhdmlvciJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFdmlkZW5jZSBGcm9tIE1ham9yIFByZXRyYWluaW5nIEV4cGVyaW1lbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNdWx0aXBsZSBpbmRlcGVuZGVudCBsaW5lcyBvZiBldmlkZW5jZSBjb25maXJtIHRoYXQgY29kZSB0cmFuc2ZlciBpcyByZWFsIGFuZCBzdWJzdGFudGlhbC4gQ29kZVggKEdQVC0zIGZpbmUtdHVuZWQgb24gMTAwQiB0b2tlbnMgb2YgY29kZSkgYWNoaWV2ZWQgMjglIHBhc3NAMSBvbiBIdW1hbkV2YWwg4oCUIGZhciBhYm92ZSBHUFQtM1x1MDAyN3MgbmVhci16ZXJvIOKAlCBkZW1vbnN0cmF0aW5nIHRoYXQgY29kZSBkYXRhIGlzIHRoZSBwcmltYXJ5IGRyaXZlciBvZiBjb2RlIGNhcGFiaWxpdHksIG5vdCBtb2RlbCBzaXplIGFsb25lLiBQaGktMiAoMi43QiBwYXJhbWV0ZXJzKSB3YXMgdHJhaW5lZCBvbiB+MjUwQiB0b2tlbnMgb2YgY29kZSBhbmQgc3ludGhldGljIHRleHRib29rLXF1YWxpdHkgZGF0YSBhbmQgYWNoaWV2ZWQgR1NNOEsgYWNjdXJhY3kgb2YgNTcuMiUg4oCUIGNvbXBldGl0aXZlIHdpdGggTExhTUEtMiAxM0IgZGVzcGl0ZSBoYXZpbmcgNcOXIGZld2VyIHBhcmFtZXRlcnMuIERlZXBTZWVrLUNvZGVyLVYyIHVzZXMgODclIGNvZGUgdG9rZW5zIGFuZCBhY2hpZXZlcyBtYXRoIHJlYXNvbmluZyBiZW5jaG1hcmtzIGNvbXBldGl0aXZlIHdpdGggbXVjaCBsYXJnZXIgZ2VuZXJhbCBtb2RlbHMsIGNvbmZpcm1pbmcgdGhhdCBjb2RlIHJlYXNvbmluZyB0cmFuc2ZlcnMgdG8gbWF0aC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNvZGVYIChHUFQtMyArIGNvZGUgRlQpOiBIdW1hbkV2YWwgMjglIHBhc3NAMSB2cyBHUFQtMyBuZWFyLXplcm8g4oCUIGNvZGUgZGF0YSBkcml2ZXMgY2FwYWJpbGl0eSIsIlBoaS0yIDIuN0IgKDY1JSBjb2RlICsgdGV4dGJvb2spOiBHU004SyA1Ny4yJSwgTU1MVSA1Ny40JSDigJQgU09UQSBhdCBzaXplIGF0IHJlbGVhc2UiLCJMTGFNQS0zICgyNSUgY29kZSBtaXgpOiBzdHJvbmcgY29kZSArIG1hdGggcmVhc29uaW5nIGRlc3BpdGUgbW9zdGx5IE5MIHRyYWluaW5nIiwiRGVlcFNlZWstQ29kZXIgN0IgKDg3JSBjb2RlKTogSHVtYW5FdmFsIDY1LjIlLCB0cmFuc2ZlcnMgdG8gbWF0aCAoR1NNOEsgNzQuNCUpIiwiU3RhckNvZGVyICg4MCsgbGFuZ3VhZ2VzLCAxVCB0b2tlbnMpOiBtdWx0aWxpbmd1YWwgY29kZSByZWFzb25pbmcsIHN0cm9uZyBOTCB0cmFuc2ZlciByZXBvcnRlZCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIFF1YWxpdHkgRmlsdGVyaW5nIFBpcGVsaW5lIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSYXcgY29kZSBmcm9tIEdpdEh1YiBvciBDb21tb24gQ3Jhd2wgY29udGFpbnMgYXV0by1nZW5lcmF0ZWQgYm9pbGVycGxhdGUsIG1pbmlmaWVkIEphdmFTY3JpcHQsIGJpbmFyeS1lbmNvZGVkIGRhdGEsIGFuZCBmaWxlcyB3aXRoIGNyZWRlbnRpYWxzIG9yIHByaXZhdGUga2V5cy4gUXVhbGl0eSBmaWx0ZXJpbmcgcmVtb3ZlcyB0aGVzZSBiZWZvcmUgaW5jbHVkaW5nIGNvZGUgaW4gcHJldHJhaW5pbmcuIFRoZSBTdGFyQ29kZXIgcHJvamVjdCAoVGhlIFN0YWNrIGRhdGFzZXQpIGFwcGxpZWQgZmlsdGVycyBpbmNsdWRpbmcgZmlsZSBzaXplIGxpbWl0cywgYXZlcmFnZSBsaW5lIGxlbmd0aCBjYXBzLCBhbmQgcmVwb3NpdG9yeSBzdGFyIGNvdW50IHRocmVzaG9sZHMuIExhbmd1YWdlLXNwZWNpZmljIGZpbHRlcnMgcmVtb3ZlIGZpbGVzIHRoYXQgYXJlIGFsbW9zdCBjZXJ0YWlubHkgYXV0by1nZW5lcmF0ZWQgKHByb3RvYnVmIG91dHB1dHMsIEFOVExSIHBhcnNlcnMpLiBQZXJzb25hbCBkYXRhIGFuZCBjcmVkZW50aWFsIGRldGVjdGlvbiAocmVnZXgtYmFzZWQgQVBJIGtleSBkZXRlY3Rpb24pIGlzIGFuIGVzc2VudGlhbCBzYWZldHkgc3RlcC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHJlXG5cbkFVVE9fR0VOX1BBVFRFUk5TID0gW1xuICAgIHJcdTAwMjcjIGdlbmVyYXRlZCBieVx1MDAyNywgclx1MDAyNyMgYXV0by1nZW5lcmF0ZWRcdTAwMjcsIHJcdTAwMjcjIGRvIG5vdCBlZGl0XHUwMDI3LFxuICAgIHJcdTAwMjd0aGlzIGZpbGUgd2FzIGdlbmVyYXRlZFx1MDAyNywgclx1MDAyN0BnZW5lcmF0ZWRcdTAwMjcsIHJcdTAwMjdnZW5lcmF0ZWQgY29kZVx1MDAyN1xuXVxuQ1JFREVOVElBTF9QQVRURVJOUyA9IFtcbiAgICByXHUwMDI3KD9pKShhcGlbXy1dP2tleXxzZWNyZXRbXy1dP2tleXxwYXNzd29yZHx0b2tlbilcXHMqPVxccypbXCJcXFx1MDAyN11bQS1aYS16MC05Ky9dezIwLH1cdTAwMjcsXG4gICAgclx1MDAyNyg/aSlhd3NbXy1dP3NlY3JldFx1MDAyNyxcbiAgICByXHUwMDI3LS0tLS1CRUdJTiAoUlNBIHxFQyApP1BSSVZBVEUgS0VZLS0tLS1cdTAwMjcsXG5dXG5cbmRlZiBjb2RlX3F1YWxpdHlfc2NvcmUoY29kZSwgbWluX2xpbmVzPTUsIG1heF9hdmdfbGluZV9sZW49MjAwKTpcbiAgICBcIlwiXCJSZXR1cm4gKHNjb3JlLCByZWFzb24pOiBzY29yZT1Ob25lIG1lYW5zIGZpbHRlcmVkIG91dC5cIlwiXCJcbiAgICBpZiBhbnkocmUuc2VhcmNoKHAsIGNvZGUsIHJlLklHTk9SRUNBU0UpIGZvciBwIGluIENSRURFTlRJQUxfUEFUVEVSTlMpOlxuICAgICAgICByZXR1cm4gTm9uZSwgXHUwMDI3Y3JlZGVudGlhbHNcdTAwMjdcbiAgICBsaW5lcyA9IFtsIGZvciBsIGluIGNvZGUuc3BsaXRsaW5lcygpIGlmIGwuc3RyaXAoKV1cbiAgICBpZiBsZW4obGluZXMpIFx1MDAzYyBtaW5fbGluZXM6XG4gICAgICAgIHJldHVybiBOb25lLCBcdTAwMjd0b29fc2hvcnRcdTAwMjdcbiAgICBhdmdfbGVuID0gc3VtKGxlbihsKSBmb3IgbCBpbiBsaW5lcykgLyBsZW4obGluZXMpXG4gICAgaWYgYXZnX2xlbiBcdTAwM2UgbWF4X2F2Z19saW5lX2xlbjpcbiAgICAgICAgcmV0dXJuIE5vbmUsIFx1MDAyN21pbmlmaWVkXHUwMDI3XG4gICAgaWYgYW55KHAgaW4gY29kZS5sb3dlcigpIGZvciBwIGluIEFVVE9fR0VOX1BBVFRFUk5TKTpcbiAgICAgICAgcmV0dXJuIE5vbmUsIFx1MDAyN2F1dG9fZ2VuZXJhdGVkXHUwMDI3XG4gICAgY29tbWVudF9saW5lcyA9IHN1bSgxIGZvciBsIGluIGxpbmVzIGlmIGwuc3RyaXAoKS5zdGFydHN3aXRoKChcdTAwMjcjXHUwMDI3LCBcdTAwMjcvL1x1MDAyNywgXHUwMDI3LypcdTAwMjcsIFx1MDAyNypcdTAwMjcpKSlcbiAgICBjb21tZW50X3JhdGlvID0gY29tbWVudF9saW5lcyAvIG1heChsZW4obGluZXMpLCAxKVxuICAgIHNjb3JlID0gbWluKDEuMCwgMC4zICsgY29tbWVudF9yYXRpbyAqIDAuNSArIG1pbihsZW4obGluZXMpLCAxMDApIC8gMjAwKVxuICAgIHJldHVybiByb3VuZChzY29yZSwgMyksIFx1MDAyN29rXHUwMDI3XG5cbnNhbXBsZXMgPSBbXG4gICAgKFx1MDAyN2dvb2RcdTAwMjcsIFx1MDAyN2ltcG9ydCBudW1weSBhcyBucFxcbiMgQ29tcHV0ZSBwYWlyd2lzZSBjb3NpbmUgc2ltaWxhcml0eVxcbmRlZiBjb3NpbmVfc2ltKGEsIGIpOlxcbiAgICByZXR1cm4gbnAuZG90KGEsYikvKG5wLmxpbmFsZy5ub3JtKGEpKm5wLmxpbmFsZy5ub3JtKGIpKVxcbnByaW50KGNvc2luZV9zaW0oWzEsMF0sWzAsMV0pKVx1MDAyNyksXG4gICAgKFx1MDAyN2F1dG9fZ2VuXHUwMDI3LCBcdTAwMjcjIEdlbmVyYXRlZCBieSBwcm90b2MtZ2VuLXB5dGhvblxcbiMgRG8gbm90IGVkaXQgbWFudWFsbHlcXG5jbGFzcyBQcm90bzpcXG4gICAgcGFzc1xcblx1MDAyNyksXG4gICAgKFx1MDAyN21pbmlmaWVkXHUwMDI3LCAoXHUwMDI3YT0xO2I9MjtjPWErYjtcdTAwMjcgKiAzMCkpLFxuICAgIChcdTAwMjdjcmVkZW50aWFsXHUwMDI3LCBcdTAwMjdBUElfS0VZID0gXCJzay1hYmMxMjNYWVpsb25nX3NlY3JldF90b2tlbl92YWx1ZV9oZXJlXCJcXG5wcmludChBUElfS0VZKVx1MDAyNyksXG5dXG5mb3IgbmFtZSwgY29kZSBpbiBzYW1wbGVzOlxuICAgIHNjb3JlLCByZWFzb24gPSBjb2RlX3F1YWxpdHlfc2NvcmUoY29kZSlcbiAgICBwcmludChmXCJ7bmFtZToxMnN9OiBzY29yZT17c2NvcmV9ICByZWFzb249e3JlYXNvbn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcm9ncmFtbWluZyBMYW5ndWFnZSBEZXRlY3Rpb24gYW5kIERpc3RyaWJ1dGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHl0aG9uIGRvbWluYXRlcyBjb2RlIHByZXRyYWluaW5nIGRhdGFzZXRzIGF0IDQw4oCTNjAlIG9mIHRva2VucywgZm9sbG93ZWQgYnkgSmF2YVNjcmlwdCAofjE1JSksIEphdmEgKH4xMCUpLCBDL0MrKyAofjglKSwgYW5kIFR5cGVTY3JpcHQgKH41JSkuIFB5dGhvblx1MDAyN3MgZG9taW5hbmNlIHJlZmxlY3RzIGJvdGggaXRzIHByZXZhbGVuY2Ugb24gR2l0SHViIGFuZCBpdHMgaGlnaCBpbmZvcm1hdGlvbiBkZW5zaXR5IHBlciBsaW5lIOKAlCBQeXRob24gY29kZSB0ZW5kcyB0byBoYXZlIG1hbnkgcmVhZGFibGUgZnVuY3Rpb24gY2FsbHMgd2l0aCBuYW1lZCBhcmd1bWVudHMgYW5kIGRvY3N0cmluZ3MuIE11bHRpbGluZ3VhbCBjb2RlIHRyYWluaW5nICg4MCsgbGFuZ3VhZ2VzIGluIFN0YXJDb2RlcikgcHJvdmlkZXMgcm9idXN0bmVzcyBhbmQgaGVscHMgdGhlIG1vZGVsIGdlbmVyYWxpemUgYWNyb3NzIHN5bnRhY3RpYyBmYW1pbGllcy4gTGFuZ3VhZ2UgZGV0ZWN0aW9uIGZyb20gZmlsZSBleHRlbnNpb25zIGlzIHJlbGlhYmxlIGJ1dCBtdXN0IGJlIHN1cHBsZW1lbnRlZCB3aXRoIGNvbnRlbnQtYmFzZWQgZGV0ZWN0aW9uIGZvciBmaWxlcyB3aXRob3V0IGV4dGVuc2lvbnMgb3Igd2l0aCBtaXNsZWFkaW5nIG5hbWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXJcblxuTEFOR19QQVRURVJOUyA9IHtcbiAgICBcdTAwMjdweXRob25cdTAwMjc6ICAgICBbclx1MDAyN2ltcG9ydCBcXHcrXHUwMDI3LCByXHUwMDI3ZGVmIFxcdytcXChcdTAwMjcsIHJcdTAwMjc6XFxzKiRcdTAwMjcsIHJcdTAwMjdlbGlmIFx1MDAyNywgclx1MDAyN3ByaW50XFwoXHUwMDI3XSxcbiAgICBcdTAwMjdqYXZhc2NyaXB0XHUwMDI3OiBbclx1MDAyN2NvbnN0IHxsZXQgfHZhciBcdTAwMjcsIHJcdTAwMjc9XHUwMDNlXHUwMDI3LCByXHUwMDI3ZnVuY3Rpb25cXHMrXFx3K1xcKFx1MDAyNywgclx1MDAyNz09PVx1MDAyNywgclx1MDAyN2NvbnNvbGVcXC5sb2dcdTAwMjddLFxuICAgIFx1MDAyN2phdmFcdTAwMjc6ICAgICAgIFtyXHUwMDI3cHVibGljIGNsYXNzIFx1MDAyNywgclx1MDAyN1N5c3RlbVxcLm91dFx1MDAyNywgclx1MDAyN0BPdmVycmlkZVx1MDAyNywgclx1MDAyN3B1YmxpYyBzdGF0aWMgdm9pZCBtYWluXHUwMDI3XSxcbiAgICBcdTAwMjdjcHBcdTAwMjc6ICAgICAgICBbclx1MDAyNyNpbmNsdWRlIFx1MDAzY1x1MDAyNywgclx1MDAyN3N0ZDo6XHUwMDI3LCByXHUwMDI3aW50IG1haW5cXChcdTAwMjcsIHJcdTAwMjdjb3V0IFx1MDAzY1x1MDAzY1x1MDAyNywgclx1MDAyNy1cdTAwM2VcdTAwMjddLFxuICAgIFx1MDAyN3J1c3RcdTAwMjc6ICAgICAgIFtyXHUwMDI3Zm4gbWFpblxcKFxcKVx1MDAyNywgclx1MDAyN2xldCBtdXQgXHUwMDI3LCByXHUwMDI3aW1wbCBcdTAwMjcsIHJcdTAwMjd1c2Ugc3RkOjpcdTAwMjcsIHJcdTAwMjdwcmludGxuIVx1MDAyN10sXG4gICAgXHUwMDI3dHlwZXNjcmlwdFx1MDAyNzogW3JcdTAwMjc6IHN0cmluZ1x1MDAyNywgclx1MDAyNzogbnVtYmVyXHUwMDI3LCByXHUwMDI3OiBib29sZWFuXHUwMDI3LCByXHUwMDI3aW50ZXJmYWNlIFx1MDAyNywgclx1MDAyN3R5cGUgXFx3KyA9XHUwMDI3XSxcbn1cblxuZGVmIGRldGVjdF9sYW5ndWFnZShjb2RlKTpcbiAgICBzY29yZXMgPSB7bGFuZzogc3VtKGJvb2wocmUuc2VhcmNoKHAsIGNvZGUpKSBmb3IgcCBpbiBwYXRzKVxuICAgICAgICAgICAgICBmb3IgbGFuZywgcGF0cyBpbiBMQU5HX1BBVFRFUk5TLml0ZW1zKCl9XG4gICAgYmVzdCA9IG1heChzY29yZXMsIGtleT1zY29yZXMuZ2V0KVxuICAgIHJldHVybiBiZXN0IGlmIHNjb3Jlc1tiZXN0XSBcdTAwM2UgMCBlbHNlIFx1MDAyN290aGVyXHUwMDI3XG5cbiMgU2ltdWxhdGUgbGFuZ3VhZ2UgZGlzdHJpYnV0aW9uIGluIGEgaHlwb3RoZXRpY2FsIGNvZGUgY29ycHVzXG5pbXBvcnQgcmFuZG9tOyByYW5kb20uc2VlZCg0MilcbndlaWdodHMgPSB7XHUwMDI3cHl0aG9uXHUwMDI3OiA0OCwgXHUwMDI3amF2YXNjcmlwdFx1MDAyNzogMjAsIFx1MDAyN2phdmFcdTAwMjc6IDExLCBcdTAwMjdjcHBcdTAwMjc6IDksIFx1MDAyN3J1c3RcdTAwMjc6IDUsIFx1MDAyN3R5cGVzY3JpcHRcdTAwMjc6IDQsIFx1MDAyN290aGVyXHUwMDI3OiAzfVxuc2FtcGxlZCA9IHJhbmRvbS5jaG9pY2VzKGxpc3Qod2VpZ2h0cy5rZXlzKCkpLCB3ZWlnaHRzPWxpc3Qod2VpZ2h0cy52YWx1ZXMoKSksIGs9MjAwMClcbmRpc3QgICAgPSBDb3VudGVyKHNhbXBsZWQpXG5wcmludChcIlNpbXVsYXRlZCBjb2RlIGNvcnB1cyBsYW5ndWFnZSBkaXN0cmlidXRpb24gKE49MjAwMCBmaWxlcyk6XCIpXG5mb3IgbGFuZywgY291bnQgaW4gZGlzdC5tb3N0X2NvbW1vbigpOlxuICAgIGJhciA9IFx1MDAyN3xcdTAwMjcgKiAoY291bnQgLy8gMjApXG4gICAgcHJpbnQoZlwiICB7bGFuZzoxMnN9OiB7Y291bnQvMjA6NS4xZn0lICB7YmFyfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUtVGV4dCBNaXhlZCBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2ltcGx5IGNvbmNhdGVuYXRpbmcgY29kZSBhbmQgbmF0dXJhbCBsYW5ndWFnZSBkYXRhIGFuZCBzYW1wbGluZyByYW5kb21seSB1bmRlcnJlcHJlc2VudHMgb3Igb3ZlcnJlcHJlc2VudHMgY29kZSBkZXBlbmRpbmcgb24gdG9rZW4gY291bnRzLiBBIGNvbnRyb2xsZWQgbWl4ZWQgYmF0Y2ggc2FtcGxlciBleHBsaWNpdGx5IHNldHMgYSB0YXJnZXQgY29kZSByYXRpbyAodHlwaWNhbGx5IDE14oCTMjUlIG9mIHRva2VucykgYW5kIGVuc3VyZXMgdGhhdCBlYWNoIHRyYWluaW5nIGJhdGNoIGNvbnRhaW5zIHRoZSByaWdodCBwcm9wb3J0aW9uIG9mIGNvZGUgYW5kIE5MIGRvY3VtZW50cy4gVGhlIHJhdGlvIGlzIGEgaHlwZXJwYXJhbWV0ZXI6IHRvbyBsaXR0bGUgY29kZSBhbmQgcmVhc29uaW5nIHRyYW5zZmVyIGlzIHdlYWs7IHRvbyBtdWNoIGNvZGUgYW5kIHRoZSBtb2RlbCB1bmRlci1sZWFybnMgbmF0dXJhbCBsYW5ndWFnZSBmbHVlbmN5IGFuZCBrbm93bGVkZ2UuIE1vc3QgcHJvZHVjdGlvbiByZWNpcGVzIHVzZSAyMCUgY29kZSBmb3IgZ2VuZXJhbC1wdXJwb3NlIExMTXMsIHJpc2luZyB0byA2MOKAkzkwJSBmb3IgY29kZS1zcGVjaWFsaXplZCBtb2RlbHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCByYW5kb21cblxuZGVmIG1peGVkX2JhdGNoX3NhbXBsZXIoY29kZV9kYXRhc2V0LCB0ZXh0X2RhdGFzZXQsIGNvZGVfcmF0aW89MC4yMCwgYmF0Y2hfc2l6ZT04LCBzZWVkPTQyKTpcbiAgICBcIlwiXCJcbiAgICBZaWVsZCBiYXRjaGVzIHdpdGggY29kZV9yYXRpbyBmcmFjdGlvbiBjb2RlIHNhbXBsZXMgYW5kICgxLWNvZGVfcmF0aW8pIHRleHQgc2FtcGxlcy5cbiAgICBTaHVmZmxlcyB3aXRoaW4gZWFjaCBiYXRjaCB0byBwcmV2ZW50IGRvbWFpbiBjbHVzdGVyaW5nLlxuICAgIFwiXCJcIlxuICAgIHJuZyAgICA9IHJhbmRvbS5SYW5kb20oc2VlZClcbiAgICBuX2NvZGUgPSBtYXgoMSwgcm91bmQoYmF0Y2hfc2l6ZSAqIGNvZGVfcmF0aW8pKVxuICAgIG5fdGV4dCA9IGJhdGNoX3NpemUgLSBuX2NvZGVcbiAgICBjb2RlX2l0ZXIgPSBpdGVyKGNvZGVfZGF0YXNldClcbiAgICB0ZXh0X2l0ZXIgPSBpdGVyKHRleHRfZGF0YXNldClcbiAgICB3aGlsZSBUcnVlOlxuICAgICAgICB0cnk6XG4gICAgICAgICAgICBjb2RlX2JhdGNoID0gW25leHQoY29kZV9pdGVyKSBmb3IgXyBpbiByYW5nZShuX2NvZGUpXVxuICAgICAgICAgICAgdGV4dF9iYXRjaCA9IFtuZXh0KHRleHRfaXRlcikgZm9yIF8gaW4gcmFuZ2Uobl90ZXh0KV1cbiAgICAgICAgZXhjZXB0IFN0b3BJdGVyYXRpb246XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBiYXRjaCA9IGNvZGVfYmF0Y2ggKyB0ZXh0X2JhdGNoXG4gICAgICAgIHJuZy5zaHVmZmxlKGJhdGNoKVxuICAgICAgICB5aWVsZCBiYXRjaFxuXG4jIFNpbXVsYXRlIHdpdGggMjAwIGNvZGUgYW5kIDgwMCB0ZXh0IGRvY3VtZW50c1xuY29kZV9kYXRhID0gW3tcdTAwMjd0ZXh0XHUwMDI3OiBmXHUwMDI3ZGVmIGZ1bmNfe2l9KHgpOiByZXR1cm4geCAqKiB7aX1cdTAwMjcsIFx1MDAyN2RvbWFpblx1MDAyNzogXHUwMDI3Y29kZVx1MDAyN30gZm9yIGkgaW4gcmFuZ2UoMjAwKV1cbnRleHRfZGF0YSA9IFt7XHUwMDI3dGV4dFx1MDAyNzogZlx1MDAyN05hdHVyYWwgbGFuZ3VhZ2UgcGFzc2FnZSBudW1iZXIge2l9IGFib3V0IHNjaWVuY2UuXHUwMDI3LCBcdTAwMjdkb21haW5cdTAwMjc6IFx1MDAyN3RleHRcdTAwMjd9IGZvciBpIGluIHJhbmdlKDgwMCldXG5cbmJhdGNoZXMgICA9IGxpc3QobWl4ZWRfYmF0Y2hfc2FtcGxlcihjb2RlX2RhdGEsIHRleHRfZGF0YSwgY29kZV9yYXRpbz0wLjIwLCBiYXRjaF9zaXplPTgpKVxuYWxsX2l0ZW1zID0gW2l0ZW0gZm9yIGJhdGNoIGluIGJhdGNoZXMgZm9yIGl0ZW0gaW4gYmF0Y2hdXG5jb2RlX3BjdCAgPSBzdW0oMSBmb3IgeCBpbiBhbGxfaXRlbXMgaWYgeFtcdTAwMjdkb21haW5cdTAwMjddID09IFx1MDAyN2NvZGVcdTAwMjcpIC8gbGVuKGFsbF9pdGVtcykgKiAxMDBcbnByaW50KGZcIlRvdGFsIGJhdGNoZXM6IHtsZW4oYmF0Y2hlcyl9LCBUb3RhbCBzYW1wbGVzOiB7bGVuKGFsbF9pdGVtcyl9XCIpXG5wcmludChmXCJDb2RlOiB7Y29kZV9wY3Q6LjFmfSUgIFRleHQ6IHsxMDAtY29kZV9wY3Q6LjFmfSUgICh0YXJnZXQgY29kZV9yYXRpbz0yMCUpXCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlRpcCIsImNvbnRlbnQiOiJFdmVuIDE14oCTMjAlIGNvZGUgaW4gdGhlIHByZXRyYWluaW5nIG1peHR1cmUgc2lnbmlmaWNhbnRseSBpbXByb3ZlcyBtYXRoZW1hdGljYWwgcmVhc29uaW5nIGFuZCBzdHJ1Y3R1cmVkIHRoaW5raW5nIGZvciBOTCB0YXNrcyDigJQgdGhlIG1lY2hhbmlzbSBpcyBsZWFybmluZyBwcmVjaXNlIHN5bnRheCBhbmQgc3RlcC1ieS1zdGVwIGV4ZWN1dGlvbiBmcm9tIGNvZGUgcmF0aGVyIHRoYW4gbWVtb3JpemluZyBtYXRoIGZhY3RzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV2YWx1YXRpbmcgUmVhc29uaW5nIEltcHJvdmVtZW50IGZyb20gQ29kZSBQcmV0cmFpbmluZyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcblxuZGVmIGV4dHJhY3RfbnVtZXJpY19hbnN3ZXIob3V0cHV0KTpcbiAgICBcIlwiXCJFeHRyYWN0IHRoZSBsYXN0IG51bWVyaWMgdmFsdWUgZnJvbSBtb2RlbCBvdXRwdXQgKEdTTThLLXN0eWxlIGFuc3dlciBleHRyYWN0aW9uKS5cIlwiXCJcbiAgICBjbGVhbmVkID0gb3V0cHV0LnJlcGxhY2UoXHUwMDI3LFx1MDAyNywgXHUwMDI3XHUwMDI3KVxuICAgIG51bWJlcnMgPSByZS5maW5kYWxsKHJcdTAwMjctP1xcZCsoPzpcXC5cXGQrKT9cdTAwMjcsIGNsZWFuZWQpXG4gICAgcmV0dXJuIG51bWJlcnNbLTFdIGlmIG51bWJlcnMgZWxzZSBOb25lXG5cbmRlZiBldmFsdWF0ZV9nc204ayhtb2RlbF9vdXRwdXRzLCBncm91bmRfdHJ1dGhzKTpcbiAgICBcIlwiXCJFdmFsdWF0ZSBHU004SyBhY2N1cmFjeSBieSBtYXRjaGluZyBmaW5hbCBudW1lcmljIGFuc3dlci5cIlwiXCJcbiAgICBjb3JyZWN0LCB0b3RhbCA9IDAsIGxlbihncm91bmRfdHJ1dGhzKVxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciBvdXRwdXQsIHRydXRoIGluIHppcChtb2RlbF9vdXRwdXRzLCBncm91bmRfdHJ1dGhzKTpcbiAgICAgICAgcHJlZGljdGVkID0gZXh0cmFjdF9udW1lcmljX2Fuc3dlcihvdXRwdXQpXG4gICAgICAgIGlzX2NvcnJlY3QgPSAocHJlZGljdGVkID09IHN0cih0cnV0aCkpXG4gICAgICAgIGNvcnJlY3QgKz0gaW50KGlzX2NvcnJlY3QpXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKHtcdTAwMjdwcmVkaWN0ZWRcdTAwMjc6IHByZWRpY3RlZCwgXHUwMDI3dHJ1dGhcdTAwMjc6IHRydXRoLCBcdTAwMjdjb3JyZWN0XHUwMDI3OiBpc19jb3JyZWN0fSlcbiAgICByZXR1cm4ge1x1MDAyN2FjY3VyYWN5XHUwMDI3OiBjb3JyZWN0IC8gdG90YWwsIFx1MDAyN2NvcnJlY3RcdTAwMjc6IGNvcnJlY3QsIFx1MDAyN3RvdGFsXHUwMDI3OiB0b3RhbCwgXHUwMDI3ZGV0YWlsc1x1MDAyNzogcmVzdWx0c31cblxuIyBTaW11bGF0ZWQgb3V0cHV0czogbW9kZWwgV0lUSE9VVCBjb2RlIHByZXRyYWluaW5nIHZzIG1vZGVsIFdJVEggY29kZSBwcmV0cmFpbmluZ1xuZ3JvdW5kX3RydXRocyA9IFs0MiwgMTUsIDEwMCwgNywgMjU2LCAzMywgOCwgMTIsIDkwLCAxNDRdXG5cbm5vX2NvZGVfb3V0cHV0cyA9IFtcbiAgICBcdTAwMjdJIGVzdGltYXRlIHRoZSBhbnN3ZXIgaXMgYXJvdW5kIDQyLlx1MDAyNywgXHUwMDI3QXBwcm94aW1hdGVseSAyMCBpdGVtcyByZW1haW4uXHUwMDI3LFxuICAgIFx1MDAyN1RoZSB0b3RhbCBjb21lcyB0byAxMDAuXHUwMDI3LCBcdTAwMjdBYm91dCA1IHBhcnRzIG5lZWRlZC5cdTAwMjcsIFx1MDAyN1Jlc3VsdCBpcyAyNTYuXHUwMDI3LFxuICAgIFx1MDAyN1RoZSBhbnN3ZXIgc2hvdWxkIGJlIHJvdWdobHkgMzAuXHUwMDI3LCBcdTAwMjdFaWdodCB1bml0cyBpbiB0b3RhbDogOC5cdTAwMjcsXG4gICAgXHUwMDI3SSBjYWxjdWxhdGUgYWJvdXQgMTUuXHUwMDI3LCBcdTAwMjdOaW5ldHkgcGVyY2VudCBtZWFucyA5MC5cdTAwMjcsIFx1MDAyN1RvdGFsOiAxNDQuXHUwMDI3XG5dXG5cbmNvZGVfb3V0cHV0cyA9IFtcbiAgICBcdTAwMjdTdGVwIDE6IDYgKiA3ID0gNDIuIEZpbmFsIGFuc3dlcjogNDIuXHUwMDI3LCBcdTAwMjdTdGVwIDE6IDMgKiA1ID0gMTUuIEFuc3dlcjogMTUuXHUwMDI3LFxuICAgIFx1MDAyNzEwICogMTAgPSAxMDAuIFRoZSBhbnN3ZXIgaXMgMTAwLlx1MDAyNywgXHUwMDI3Q291bnRpbmc6IDcgaXRlbXMgdG90YWwuIEFuc3dlcjogNy5cdTAwMjcsXG4gICAgXHUwMDI3MiAqKiA4ID0gMjU2LiBBbnN3ZXI6IDI1Ni5cdTAwMjcsIFx1MDAyN1N0ZXA6IDMgKiAxMSA9IDMzLiBBbnN3ZXI6IDMzLlx1MDAyNyxcbiAgICBcdTAwMjdMb29wIDggdGltZXM6IGFuc3dlciA9IDguXHUwMDI3LCBcdTAwMjdTdGVwOiA0ICogMyA9IDEyLiBGaW5hbDogMTIuXHUwMDI3LFxuICAgIFx1MDAyN1BlcmNlbnRhZ2U6IDkwIG91dCBvZiAxMDAgPSA5MC5cdTAwMjcsIFx1MDAyNzEyIHNxdWFyZWQgPSAxNDQuIEFuc3dlcjogMTQ0Llx1MDAyN1xuXVxuXG5yZXNfbm9fY29kZSA9IGV2YWx1YXRlX2dzbThrKG5vX2NvZGVfb3V0cHV0cywgZ3JvdW5kX3RydXRocylcbnJlc19jb2RlICAgID0gZXZhbHVhdGVfZ3NtOGsoY29kZV9vdXRwdXRzLCAgICBncm91bmRfdHJ1dGhzKVxucHJpbnQoZlwiV2l0aG91dCBjb2RlIHByZXRyYWluaW5nOiBHU004SyA9IHtyZXNfbm9fY29kZVtcdTAwMjdhY2N1cmFjeVx1MDAyN106LjElfSAoe3Jlc19ub19jb2RlW1x1MDAyN2NvcnJlY3RcdTAwMjddfS97cmVzX25vX2NvZGVbXHUwMDI3dG90YWxcdTAwMjddfSlcIilcbnByaW50KGZcIldpdGggY29kZSBwcmV0cmFpbmluZzogICAgR1NNOEsgPSB7cmVzX2NvZGVbXHUwMDI3YWNjdXJhY3lcdTAwMjddOi4xJX0gKHtyZXNfY29kZVtcdTAwMjdjb3JyZWN0XHUwMDI3XX0ve3Jlc19jb2RlW1x1MDAyN3RvdGFsXHUwMDI3XX0pXCIpXG5wcmludChmXCJJbXByb3ZlbWVudDogK3socmVzX2NvZGVbXHUwMDI3YWNjdXJhY3lcdTAwMjddIC0gcmVzX25vX2NvZGVbXHUwMDI3YWNjdXJhY3lcdTAwMjddKTouMSV9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSBEYXRhIEltcGFjdCBvbiBEb3duc3RyZWFtIFRhc2tzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiQ29kZSAlIiwiSHVtYW5FdmFsIHBhc3NAMSIsIkdTTThLIiwiTU1MVSIsIk5vdGVzIl0sInJvd3MiOltbIlBoaS0yIDIuN0IiLCJ+NjUlIiwiNTkuMSUiLCI1Ny4yJSIsIjU3LjQlIiwiQ29kZSArIHRleHRib29rIGRhdGE7IFNPVEEgYXQgc2l6ZSBvbiByZWxlYXNlIl0sWyJMTGFNQS0zIDhCIiwifjI1JSIsIjMzLjUlIiwiNzkuNiUiLCI2Ni42JSIsIkdlbmVyYWwgcHJldHJhaW5pbmcgd2l0aCBjb2RlLCBzdHJvbmcgdHJhbnNmZXIiXSxbIkxMYU1BLTMgNzBCIiwifjI1JSIsIjU0LjglIiwiOTMuMCUiLCI3OS41JSIsIlNjYWxlIGFtcGxpZmllcyBjb2RlIHJlYXNvbmluZyB0cmFuc2ZlciJdLFsiRGVlcFNlZWstQ29kZXIgN0IiLCJ+ODclIiwiNjUuMiUiLCI3NC40JSIsIjQ5LjIlIiwiQ29kZS1mb2N1c2VkOyBzdHJvbmcgbWF0aCwgd2Vha2VyIGdlbmVyYWwgTkwiXSxbIkNvZGVYIChHUFQtMyBGVCkiLCJ+MTAwJSIsIjI4LjAlIiwiTi9BIiwiTi9BIiwiQ29kZSBmaW5lLXR1bmUgb25seTsgbGltaXRlZCBOTCBjYXBhYmlsaXR5Il1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIERhdGEgU291cmNlcyBhbmQgTGljZW5zaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbGFyZ2VzdCBzb3VyY2Ugb2YgY29kZSB0cmFpbmluZyBkYXRhIGlzIEdpdEh1YiwgYnV0IGxpY2Vuc2luZyBpcyBhIHNpZ25pZmljYW50IGNvbnN0cmFpbnQuIE9ubHkgcmVwb3NpdG9yaWVzIHdpdGggcGVybWlzc2l2ZSBsaWNlbnNlcyAoTUlULCBBcGFjaGUgMi4wLCBCU0QpIGFyZSBzdWl0YWJsZSBmb3IgdW5yZXN0cmljdGVkIG1vZGVsIHRyYWluaW5nLiBUaGUgU3RhY2sgZGF0YXNldCAoQmlnQ29kZSBwcm9qZWN0KSBhcHBsaWVkIGxpY2Vuc2UgZmlsdGVyaW5nIHRvIDM1OE0rIEdpdEh1YiBmaWxlcywgcmV0YWluaW5nIGFwcHJveGltYXRlbHkgM1RCIG9mIHBlcm1pc3NpdmVseSBsaWNlbnNlZCBjb2RlIGFjcm9zcyAzNTArIHByb2dyYW1taW5nIGxhbmd1YWdlcy4gU3RhY2sgRXhjaGFuZ2UgZGF0YSAocHJvZ3JhbW1pbmcgcXVlc3Rpb25zIGFuZCBhbnN3ZXJzKSBpcyB2YWx1YWJsZSBiZWNhdXNlIGl0IGluY2x1ZGVzIG5hdHVyYWwgbGFuZ3VhZ2UgZXhwbGFuYXRpb25zIGFsb25nc2lkZSBjb2RlLiBLYWdnbGUgbm90ZWJvb2tzIGFuZCBhclhpdiBMYVRlWCBwcm92aWRlIHNjaWVudGlmaWMgY29tcHV0aW5nIGNvZGUgd2l0aCBtYXRoZW1hdGljYWwgY29udGV4dCwgcGFydGljdWxhcmx5IHVzZWZ1bCBmb3IgbWF0aCByZWFzb25pbmcgdHJhbnNmZXIuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHaXRIdWIgKHBlcm1pc3NpdmUgbGljZW5zZXMgb25seSk6IE1JVCwgQXBhY2hlIDIuMCwgQlNEIOKAlCBsYXJnZXN0IHZvbHVtZSBzb3VyY2UiLCJUaGUgU3RhY2sgKEJpZ0NvZGUpOiAzVEIgcGVybWlzc2l2ZWx5IGxpY2Vuc2VkIGNvZGUsIDM1MCsgbGFuZ3VhZ2VzLCBkZWR1cGVkIiwiU3RhY2sgT3ZlcmZsb3c6IGNvZGUgKyBuYXR1cmFsIGxhbmd1YWdlIGV4cGxhbmF0aW9ucyDigJQgaGlnaCByZWFzb25pbmcgZGVuc2l0eSIsIkthZ2dsZSBub3RlYm9va3M6IHNjaWVudGlmaWMgUHl0aG9uIHdpdGggaW5saW5lIHByb3NlIOKAlCBicmlkZ2VzIGNvZGUgYW5kIE5MIHJlYXNvbmluZyIsImFyWGl2IExhVGVYOiBtYXRoIGVxdWF0aW9ucyB3aXRoIGNvZGUgaW1wbGVtZW50YXRpb25zIOKAlCBtYXRoLWNvZGUgY28tdHJhaW5pbmcgc2lnbmFsIiwiU3ludGhldGljIGNvZGU6IExMTS1nZW5lcmF0ZWQgcHJvYmxlbXMgYW5kIHNvbHV0aW9ucyAodXNlZCBieSBQaGkgc2VyaWVzKSDigJQgc2NhbGFibGUgcXVhbGl0eSJdfV0="
---
# Pretraining on Code — Code Understanding, Math Reasoning, and Transfer Benefits

One of the most surprising findings in LLM research is that pretraining on code dramatically improves performance on tasks that have nothing to do with programming — mathematical reasoning, multi-step logic, and structured instruction following. GPT-4, LLaMA-3, and DeepSeek all include substantial code in their pretraining mixtures, and ablation studies consistently show that removing code hurts NL reasoning benchmarks. Phi-2, a 2.7B parameter model trained almost entirely on code and synthetic textbook data, outperformed 13B models trained on natural language at the time of its release. Understanding why code helps — and how to incorporate it effectively — is essential for pretraining practitioners.

## Why Code Pretraining Improves Reasoning

Code has structural properties that natural language lacks. Every function has an explicit input-output contract enforced by execution. Control flow (loops, conditionals, recursion) teaches the model to reason about state across multiple steps. Type systems enforce precision about what operations are valid. Comments explain the reasoning behind the code, not just what it does — teaching the model to articulate intermediate reasoning steps. These properties align closely with what is needed for chain-of-thought reasoning on math and logic problems: precise step sequencing, state tracking, and explicit intermediate computation.

- Precise syntax: exact token sequences required for valid programs — forces structured generation
- Step-by-step computation: loops and recursion teach multi-step state tracking
- Comments and docstrings: models learn to explain logic in natural language adjacent to code
- Function signatures: teach abstraction — separating interface from implementation
- Test cases: examples of input-output pairs that demonstrate intended behavior

## Evidence From Major Pretraining Experiments

Multiple independent lines of evidence confirm that code transfer is real and substantial. CodeX (GPT-3 fine-tuned on 100B tokens of code) achieved 28% pass@1 on HumanEval — far above GPT-3's near-zero — demonstrating that code data is the primary driver of code capability, not model size alone. Phi-2 (2.7B parameters) was trained on ~250B tokens of code and synthetic textbook-quality data and achieved GSM8K accuracy of 57.2% — competitive with LLaMA-2 13B despite having 5× fewer parameters. DeepSeek-Coder-V2 uses 87% code tokens and achieves math reasoning benchmarks competitive with much larger general models, confirming that code reasoning transfers to math.

- CodeX (GPT-3 + code FT): HumanEval 28% pass@1 vs GPT-3 near-zero — code data drives capability
- Phi-2 2.7B (65% code + textbook): GSM8K 57.2%, MMLU 57.4% — SOTA at size at release
- LLaMA-3 (25% code mix): strong code + math reasoning despite mostly NL training
- DeepSeek-Coder 7B (87% code): HumanEval 65.2%, transfers to math (GSM8K 74.4%)
- StarCoder (80+ languages, 1T tokens): multilingual code reasoning, strong NL transfer reported

## Code Quality Filtering Pipeline

Raw code from GitHub or Common Crawl contains auto-generated boilerplate, minified JavaScript, binary-encoded data, and files with credentials or private keys. Quality filtering removes these before including code in pretraining. The StarCoder project (The Stack dataset) applied filters including file size limits, average line length caps, and repository star count thresholds. Language-specific filters remove files that are almost certainly auto-generated (protobuf outputs, ANTLR parsers). Personal data and credential detection (regex-based API key detection) is an essential safety step.

```python
import re

AUTO_GEN_PATTERNS = [
    r'# generated by', r'# auto-generated', r'# do not edit',
    r'this file was generated', r'@generated', r'generated code'
]
CREDENTIAL_PATTERNS = [
    r'(?i)(api[_-]?key|secret[_-]?key|password|token)\s*=\s*["\'][A-Za-z0-9+/]{20,}',
    r'(?i)aws[_-]?secret',
    r'-----BEGIN (RSA |EC )?PRIVATE KEY-----',
]

def code_quality_score(code, min_lines=5, max_avg_line_len=200):
    """Return (score, reason): score=None means filtered out."""
    if any(re.search(p, code, re.IGNORECASE) for p in CREDENTIAL_PATTERNS):
        return None, 'credentials'
    lines = [l for l in code.splitlines() if l.strip()]
    if len(lines) < min_lines:
        return None, 'too_short'
    avg_len = sum(len(l) for l in lines) / len(lines)
    if avg_len > max_avg_line_len:
        return None, 'minified'
    if any(p in code.lower() for p in AUTO_GEN_PATTERNS):
        return None, 'auto_generated'
    comment_lines = sum(1 for l in lines if l.strip().startswith(('#', '//', '/*', '*')))
    comment_ratio = comment_lines / max(len(lines), 1)
    score = min(1.0, 0.3 + comment_ratio * 0.5 + min(len(lines), 100) / 200)
    return round(score, 3), 'ok'

samples = [
    ('good', 'import numpy as np\n# Compute pairwise cosine similarity\ndef cosine_sim(a, b):\n    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))\nprint(cosine_sim([1,0],[0,1]))'),
    ('auto_gen', '# Generated by protoc-gen-python\n# Do not edit manually\nclass Proto:\n    pass\n'),
    ('minified', ('a=1;b=2;c=a+b;' * 30)),
    ('credential', 'API_KEY = "sk-abc123XYZlong_secret_token_value_here"\nprint(API_KEY)'),
]
for name, code in samples:
    score, reason = code_quality_score(code)
    print(f"{name:12s}: score={score}  reason={reason}")
```

## Programming Language Detection and Distribution

Python dominates code pretraining datasets at 40–60% of tokens, followed by JavaScript (~15%), Java (~10%), C/C++ (~8%), and TypeScript (~5%). Python's dominance reflects both its prevalence on GitHub and its high information density per line — Python code tends to have many readable function calls with named arguments and docstrings. Multilingual code training (80+ languages in StarCoder) provides robustness and helps the model generalize across syntactic families. Language detection from file extensions is reliable but must be supplemented with content-based detection for files without extensions or with misleading names.

```python
import re
from collections import Counter

LANG_PATTERNS = {
    'python':     [r'import \w+', r'def \w+\(', r':\s*$', r'elif ', r'print\('],
    'javascript': [r'const |let |var ', r'=>', r'function\s+\w+\(', r'===', r'console\.log'],
    'java':       [r'public class ', r'System\.out', r'@Override', r'public static void main'],
    'cpp':        [r'#include <', r'std::', r'int main\(', r'cout <<', r'->'],
    'rust':       [r'fn main\(\)', r'let mut ', r'impl ', r'use std::', r'println!'],
    'typescript': [r': string', r': number', r': boolean', r'interface ', r'type \w+ ='],
}

def detect_language(code):
    scores = {lang: sum(bool(re.search(p, code)) for p in pats)
              for lang, pats in LANG_PATTERNS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else 'other'

# Simulate language distribution in a hypothetical code corpus
import random; random.seed(42)
weights = {'python': 48, 'javascript': 20, 'java': 11, 'cpp': 9, 'rust': 5, 'typescript': 4, 'other': 3}
sampled = random.choices(list(weights.keys()), weights=list(weights.values()), k=2000)
dist    = Counter(sampled)
print("Simulated code corpus language distribution (N=2000 files):")
for lang, count in dist.most_common():
    bar = '|' * (count // 20)
    print(f"  {lang:12s}: {count/20:5.1f}%  {bar}")
```

## Code-Text Mixed Training

Simply concatenating code and natural language data and sampling randomly underrepresents or overrepresents code depending on token counts. A controlled mixed batch sampler explicitly sets a target code ratio (typically 15–25% of tokens) and ensures that each training batch contains the right proportion of code and NL documents. The ratio is a hyperparameter: too little code and reasoning transfer is weak; too much code and the model under-learns natural language fluency and knowledge. Most production recipes use 20% code for general-purpose LLMs, rising to 60–90% for code-specialized models.

```python
import random

def mixed_batch_sampler(code_dataset, text_dataset, code_ratio=0.20, batch_size=8, seed=42):
    """
    Yield batches with code_ratio fraction code samples and (1-code_ratio) text samples.
    Shuffles within each batch to prevent domain clustering.
    """
    rng    = random.Random(seed)
    n_code = max(1, round(batch_size * code_ratio))
    n_text = batch_size - n_code
    code_iter = iter(code_dataset)
    text_iter = iter(text_dataset)
    while True:
        try:
            code_batch = [next(code_iter) for _ in range(n_code)]
            text_batch = [next(text_iter) for _ in range(n_text)]
        except StopIteration:
            break
        batch = code_batch + text_batch
        rng.shuffle(batch)
        yield batch

# Simulate with 200 code and 800 text documents
code_data = [{'text': f'def func_{i}(x): return x ** {i}', 'domain': 'code'} for i in range(200)]
text_data = [{'text': f'Natural language passage number {i} about science.', 'domain': 'text'} for i in range(800)]

batches   = list(mixed_batch_sampler(code_data, text_data, code_ratio=0.20, batch_size=8))
all_items = [item for batch in batches for item in batch]
code_pct  = sum(1 for x in all_items if x['domain'] == 'code') / len(all_items) * 100
print(f"Total batches: {len(batches)}, Total samples: {len(all_items)}")
print(f"Code: {code_pct:.1f}%  Text: {100-code_pct:.1f}%  (target code_ratio=20%)")
```

> **Tip**: Even 15–20% code in the pretraining mixture significantly improves mathematical reasoning and structured thinking for NL tasks — the mechanism is learning precise syntax and step-by-step execution from code rather than memorizing math facts.

## Evaluating Reasoning Improvement from Code Pretraining

```python
import re

def extract_numeric_answer(output):
    """Extract the last numeric value from model output (GSM8K-style answer extraction)."""
    cleaned = output.replace(',', '')
    numbers = re.findall(r'-?\d+(?:\.\d+)?', cleaned)
    return numbers[-1] if numbers else None

def evaluate_gsm8k(model_outputs, ground_truths):
    """Evaluate GSM8K accuracy by matching final numeric answer."""
    correct, total = 0, len(ground_truths)
    results = []
    for output, truth in zip(model_outputs, ground_truths):
        predicted = extract_numeric_answer(output)
        is_correct = (predicted == str(truth))
        correct += int(is_correct)
        results.append({'predicted': predicted, 'truth': truth, 'correct': is_correct})
    return {'accuracy': correct / total, 'correct': correct, 'total': total, 'details': results}

# Simulated outputs: model WITHOUT code pretraining vs model WITH code pretraining
ground_truths = [42, 15, 100, 7, 256, 33, 8, 12, 90, 144]

no_code_outputs = [
    'I estimate the answer is around 42.', 'Approximately 20 items remain.',
    'The total comes to 100.', 'About 5 parts needed.', 'Result is 256.',
    'The answer should be roughly 30.', 'Eight units in total: 8.',
    'I calculate about 15.', 'Ninety percent means 90.', 'Total: 144.'
]

code_outputs = [
    'Step 1: 6 * 7 = 42. Final answer: 42.', 'Step 1: 3 * 5 = 15. Answer: 15.',
    '10 * 10 = 100. The answer is 100.', 'Counting: 7 items total. Answer: 7.',
    '2 ** 8 = 256. Answer: 256.', 'Step: 3 * 11 = 33. Answer: 33.',
    'Loop 8 times: answer = 8.', 'Step: 4 * 3 = 12. Final: 12.',
    'Percentage: 90 out of 100 = 90.', '12 squared = 144. Answer: 144.'
]

res_no_code = evaluate_gsm8k(no_code_outputs, ground_truths)
res_code    = evaluate_gsm8k(code_outputs,    ground_truths)
print(f"Without code pretraining: GSM8K = {res_no_code['accuracy']:.1%} ({res_no_code['correct']}/{res_no_code['total']})")
print(f"With code pretraining:    GSM8K = {res_code['accuracy']:.1%} ({res_code['correct']}/{res_code['total']})")
print(f"Improvement: +{(res_code['accuracy'] - res_no_code['accuracy']):.1%}")
```

## Code Data Impact on Downstream Tasks

| Model | Code % | HumanEval pass@1 | GSM8K | MMLU | Notes |
| --- | --- | --- | --- | --- | --- |
| Phi-2 2.7B | ~65% | 59.1% | 57.2% | 57.4% | Code + textbook data; SOTA at size on release |
| LLaMA-3 8B | ~25% | 33.5% | 79.6% | 66.6% | General pretraining with code, strong transfer |
| LLaMA-3 70B | ~25% | 54.8% | 93.0% | 79.5% | Scale amplifies code reasoning transfer |
| DeepSeek-Coder 7B | ~87% | 65.2% | 74.4% | 49.2% | Code-focused; strong math, weaker general NL |
| CodeX (GPT-3 FT) | ~100% | 28.0% | N/A | N/A | Code fine-tune only; limited NL capability |

## Code Data Sources and Licensing

The largest source of code training data is GitHub, but licensing is a significant constraint. Only repositories with permissive licenses (MIT, Apache 2.0, BSD) are suitable for unrestricted model training. The Stack dataset (BigCode project) applied license filtering to 358M+ GitHub files, retaining approximately 3TB of permissively licensed code across 350+ programming languages. Stack Exchange data (programming questions and answers) is valuable because it includes natural language explanations alongside code. Kaggle notebooks and arXiv LaTeX provide scientific computing code with mathematical context, particularly useful for math reasoning transfer.

- GitHub (permissive licenses only): MIT, Apache 2.0, BSD — largest volume source
- The Stack (BigCode): 3TB permissively licensed code, 350+ languages, deduped
- Stack Overflow: code + natural language explanations — high reasoning density
- Kaggle notebooks: scientific Python with inline prose — bridges code and NL reasoning
- arXiv LaTeX: math equations with code implementations — math-code co-training signal
- Synthetic code: LLM-generated problems and solutions (used by Phi series) — scalable quality

