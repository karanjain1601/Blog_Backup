---
title: "GAN Evaluation — FID, IS, and Precision/Recall"
slug: "gan-evaluation-fid"
description: "Evaluating generative models is non-trivial because there is no single ground truth. Covers Inception Score (IS), Fréchet Inception Distance (FID), CLIP-FID, and the precision/recall decomposition that separates sample quality from diversity."
tags: ["deep-learning", "generative-models", "gans", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXZhbHVhdGluZyBnZW5lcmF0aXZlIG1vZGVscyBpcyBmdW5kYW1lbnRhbGx5IGhhcmRlciB0aGFuIGRpc2NyaW1pbmF0aXZlIG1vZGVsczogdGhlcmUgaXMgbm8gaGVsZC1vdXQgdGVzdCBzZXQgd2l0aCBsYWJlbHMsIGFuZCB2aXN1YWwgcXVhbGl0eSBpcyBzdWJqZWN0aXZlLiBUaGUgZmllbGQgaGFzIGNvbnZlcmdlZCBvbiBhdXRvbWF0aWMgbWV0cmljcyBjb21wdXRlZCBvdmVyIGxhcmdlIHNhbXBsZSBzZXRzIOKAlCBwcmltYXJpbHkgRklEIGFuZCBJUyDigJQgYnV0IGVhY2ggaGFzIGZhaWx1cmUgbW9kZXMuIFVuZGVyc3RhbmRpbmcgd2hhdCBlYWNoIG1ldHJpYyBtZWFzdXJlcywgd2hhdCBiaWFzZXMgaXQgaGFzLCBhbmQgd2hlbiBpdCBtaXNsZWFkcyBpcyBlc3NlbnRpYWwgZm9yIGNvcnJlY3RseSBpbnRlcnByZXRpbmcgR0FOIHRyYWluaW5nIHByb2dyZXNzIGFuZCBjb21wYXJpbmcgbW9kZWxzIGFjcm9zcyBwYXBlcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW5jZXB0aW9uIFNjb3JlIChJUykifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IklTIChTYWxpbWFucyBldCBhbC4gMjAxNikgbWVhc3VyZXMgdHdvIHByb3BlcnRpZXMgdXNpbmcgYSBwcmV0cmFpbmVkIEluY2VwdGlvbiB2MyBjbGFzc2lmaWVyOiAoMSkgcXVhbGl0eSDigJQgaW5kaXZpZHVhbCBpbWFnZXMgc2hvdWxkIGhhdmUgY29uZmlkZW50IChsb3ctZW50cm9weSkgY2xhc3MgcHJlZGljdGlvbnMgcCh5fHgpOyAoMikgZGl2ZXJzaXR5IOKAlCB0aGUgbWFyZ2luYWwgcCh5KSA9IEVfeFtwKHl8eCldIHNob3VsZCBiZSB1bmlmb3JtIG92ZXIgY2xhc3Nlcy4gSVMgPSBleHAoRV94W0tMKHAoeXx4KSDigJYgcCh5KSldKS4gSGlnaGVyIElTIGlzIGJldHRlci4gUHJvYmxlbXM6IElTIGRvZXMgbm90IGNvbXBhcmUgZ2VuZXJhdGVkIGltYWdlcyB0byByZWFsIGltYWdlcyBhdCBhbGwg4oCUIGEgbW9kZWwgbWVtb3Jpc2luZyB0aGUgdHJhaW5pbmcgc2V0IHdpdGggcGVyZmVjdCBjbGFzcyBiYWxhbmNlIGFjaGlldmVzIG1heGltdW0gSVMuIEl0IGlzIGFsc28gc2Vuc2l0aXZlIHRvIHRoZSBJbmNlcHRpb24gcHJlcHJvY2Vzc2luZyBhbmQga25vd24gdG8gYmUgZ2FtZWFibGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGluY2VwdGlvbl9zY29yZShweXhfYWxsLCBuX3NwbGl0cz0xMCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3SVMgZnJvbSBwcmUtZXh0cmFjdGVkIHAoeXx4KSBzb2Z0bWF4IHByb2JhYmlsaXRpZXMuXG4gICAgcHl4X2FsbDogKE4sIEMpIG51bXB5IGFycmF5IG9mIGNsYXNzIHByb2JhYmlsaXRpZXMuXG4gICAgUmV0dXJucyAobWVhbiBJUywgc3RkIElTKSBhY3Jvc3Mgc3BsaXRzLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIE4sIEMgPSBweXhfYWxsLnNoYXBlXG4gICAgc3BsaXRfc3ogPSBOIC8vIG5fc3BsaXRzXG4gICAgc2NvcmVzID0gW11cbiAgICBmb3IgaSBpbiByYW5nZShuX3NwbGl0cyk6XG4gICAgICAgIHBhcnQgPSBweXhfYWxsW2kqc3BsaXRfc3ogOiAoaSsxKSpzcGxpdF9zel0gICMgKE0sIEMpXG4gICAgICAgIHB5ICAgPSBwYXJ0Lm1lYW4oYXhpcz0wLCBrZWVwZGltcz1UcnVlKSAgICAgICAgIyBtYXJnaW5hbCBwKHkpXG4gICAgICAgIGtsICAgPSBucC5zdW0ocGFydCAqIChucC5sb2cocGFydCArIDFlLTEwKSAtXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICBucC5sb2cocHkgICArIDFlLTEwKSksIGF4aXM9MSkgICMgcGVyLXNhbXBsZSBLTFxuICAgICAgICBzY29yZXMuYXBwZW5kKGZsb2F0KG5wLmV4cChrbC5tZWFuKCkpKSlcbiAgICByZXR1cm4gZmxvYXQobnAubWVhbihzY29yZXMpKSwgZmxvYXQobnAuc3RkKHNjb3JlcykpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuTiwgQyA9IDEwMDAsIDEwXG4jIEhpZ2gtcXVhbGl0eTogcGVha2VkLCBkaXZlcnNlIC1cdTAwM2UgaGlnaCBJU1xucHl4X2dvb2QgPSBucC5leWUoQylbbnAucmFuZG9tLnJhbmRpbnQoMCwgQywgTildICogMC45ICsgMC4wMVxucHl4X2dvb2QgLz0gcHl4X2dvb2Quc3VtKDEsIGtlZXBkaW1zPVRydWUpXG5tZWFuX2lzLCBzdGRfaXMgPSBpbmNlcHRpb25fc2NvcmUocHl4X2dvb2QpXG5wcmludChcdTAwMjdIaWdoLXF1YWxpdHkgSVM6IHs6LjJmfSArLy0gezouMmZ9XHUwMDI3LmZvcm1hdChtZWFuX2lzLCBzdGRfaXMpKVxuIyBMb3ctZGl2ZXJzaXR5OiBhbGwgcHJlZGljdCBjbGFzcyAwXG5weXhfYmFkID0gbnAuemVyb3MoKE4sIEMpKTsgcHl4X2JhZFs6LCAwXSA9IDAuOTk7IHB5eF9iYWRbOiwgMTpdID0gMC4wMS85XG5tZWFuX2IsIHN0ZF9iID0gaW5jZXB0aW9uX3Njb3JlKHB5eF9iYWQpXG5wcmludChcdTAwMjdMb3ctZGl2ZXJzaXR5IElTOiB7Oi4yZn0gKy8tIHs6LjJmfVx1MDAyNy5mb3JtYXQobWVhbl9iLCBzdGRfYikpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRnLDqWNoZXQgSW5jZXB0aW9uIERpc3RhbmNlIChGSUQpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGSUQgKEhldXNlbCBldCBhbC4gMjAxNykgY29tcGFyZXMgdGhlIGRpc3RyaWJ1dGlvbiBvZiByZWFsIGltYWdlcyB0byB0aGF0IG9mIGdlbmVyYXRlZCBpbWFnZXMgdXNpbmcgZmVhdHVyZXMgZXh0cmFjdGVkIGZyb20gSW5jZXB0aW9uIHYzXHUwMDI3cyBwb29sMyBsYXllciAoMjA0OC1kKS4gQm90aCBzZXRzIG9mIGZlYXR1cmVzIGFyZSBtb2RlbGxlZCBhcyBtdWx0aXZhcmlhdGUgR2F1c3NpYW5zOyBGSUQgaXMgdGhlIEZyw6ljaGV0IGRpc3RhbmNlIGJldHdlZW4gdGhlbTogRklEID0g4oCWzrxfciDiiJIgzrxfZ+KAlsKyICsgVHIozqNfciArIM6jX2cg4oiSIDIozqNfcs6jX2cpXnsxLzJ9KS4gTG93ZXIgRklEIG1lYW5zIHRoZSBnZW5lcmF0ZWQgZGlzdHJpYnV0aW9uIGlzIGNsb3NlciB0byByZWFsLiBGSUQgaXMgc2Vuc2l0aXZlIHRvIGJvdGggcXVhbGl0eSAozqMgbWlzbWF0Y2ggZnJvbSBibHVycnkgaW1hZ2VzKSBhbmQgZGl2ZXJzaXR5ICjOvCBtaXNtYXRjaCBmcm9tIG1vZGUgY29sbGFwc2UpLiBTdGFuZGFyZCBwcmFjdGljZTogdXNlIOKJpTEwSyBnZW5lcmF0ZWQgYW5kIOKJpTEwSyByZWFsIHNhbXBsZXMgdG8gc3RhYmlsaXNlIHRoZSBlc3RpbWF0ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LmxpbmFsZyBpbXBvcnQgc3FydG1cblxuZGVmIGZyZWNoZXRfZGlzdGFuY2UobXUxLCBzaWdtYTEsIG11Miwgc2lnbWEyLCBlcHM9MWUtNik6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3RklEID0gfHxtdTEtbXUyfHxeMiArIFRyKHNpZ21hMSArIHNpZ21hMiAtIDIqc3FydG0oc2lnbWExQHNpZ21hMikpLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRpZmYgPSBtdTEgLSBtdTJcbiAgICBjb3ZtZWFuLCBfID0gc3FydG0oc2lnbWExIEAgc2lnbWEyLCBkaXNwPUZhbHNlKVxuICAgIGlmIG5vdCBucC5pc2Zpbml0ZShjb3ZtZWFuKS5hbGwoKTpcbiAgICAgICAgb2Zmc2V0ID0gbnAuZXllKHNpZ21hMS5zaGFwZVswXSkgKiBlcHNcbiAgICAgICAgY292bWVhbiA9IHNxcnRtKChzaWdtYTEgKyBvZmZzZXQpIEAgKHNpZ21hMiArIG9mZnNldCkpXG4gICAgaWYgbnAuaXNjb21wbGV4b2JqKGNvdm1lYW4pOlxuICAgICAgICBjb3ZtZWFuID0gY292bWVhbi5yZWFsXG4gICAgcmV0dXJuIGZsb2F0KGRpZmYgQCBkaWZmICsgbnAudHJhY2Uoc2lnbWExICsgc2lnbWEyIC0gMipjb3ZtZWFuKSlcblxubnAucmFuZG9tLnNlZWQoMClcbmQgPSAyNTYgICAjIHJlZHVjZWQgZnJvbSAyMDQ4IGZvciBkZW1vIHNwZWVkXG5OID0gNTAwXG5yZWFsX2ZlYXRzID0gbnAucmFuZG9tLnJhbmRuKE4sIGQpXG4jIFNhbWUgZGlzdHJpYnV0aW9uIC1cdTAwM2UgRklEIG5lYXIgMFxuZmFrZV9zYW1lID0gbnAucmFuZG9tLnJhbmRuKE4sIGQpXG5tdV9yLCBzaWdfciA9IHJlYWxfZmVhdHMubWVhbigwKSwgbnAuY292KHJlYWxfZmVhdHMsIHJvd3Zhcj1GYWxzZSlcbm11X3MsIHNpZ19zID0gZmFrZV9zYW1lLm1lYW4oMCksICBucC5jb3YoZmFrZV9zYW1lLCAgcm93dmFyPUZhbHNlKVxuZmlkX2dvb2QgPSBmcmVjaGV0X2Rpc3RhbmNlKG11X3IsIHNpZ19yLCBtdV9zLCBzaWdfcylcbnByaW50KFx1MDAyN0ZJRCAoc2FtZSBkaXN0KTogezouMmZ9XHUwMDI3LmZvcm1hdChmaWRfZ29vZCkpXG4jIFNoaWZ0ZWQgZGlzdHJpYnV0aW9uIC1cdTAwM2UgaGlnaGVyIEZJRFxuZmFrZV9zaGlmdCA9IG5wLnJhbmRvbS5yYW5kbihOLCBkKSArIDAuNVxubXVfc2gsIHNpZ19zaCA9IGZha2Vfc2hpZnQubWVhbigwKSwgbnAuY292KGZha2Vfc2hpZnQsIHJvd3Zhcj1GYWxzZSlcbmZpZF9iYWQgPSBmcmVjaGV0X2Rpc3RhbmNlKG11X3IsIHNpZ19yLCBtdV9zaCwgc2lnX3NoKVxucHJpbnQoXHUwMDI3RklEIChzaGlmdGVkKTogICB7Oi4yZn1cdTAwMjcuZm9ybWF0KGZpZF9iYWQpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNMSVAtRklEIGFuZCBTZW1hbnRpYyBGZWF0dXJlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW5jZXB0aW9uIHYzIHdhcyB0cmFpbmVkIG9uIEltYWdlTmV0IGFuZCBpdHMgZmVhdHVyZXMgYXJlIGJpYXNlZCB0b3dhcmQgSW1hZ2VOZXQgY2F0ZWdvcmllcy4gQ0xJUC1GSUQgKEt5bmvDpMOkbm5pZW1pIGV0IGFsLiAyMDIyKSByZXBsYWNlcyB0aGUgSW5jZXB0aW9uIHBvb2wzIGZlYXR1cmVzIHdpdGggQ0xJUCBWaVQtTC8xNCBmZWF0dXJlcywgd2hpY2ggYXJlIG1vcmUgc2VtYW50aWNhbGx5IG1lYW5pbmdmdWwgYW5kIGJldHRlciBhbGlnbmVkIHdpdGggaHVtYW4gcGVyY2VwdGlvbi4gQ0xJUC1GSUQgc2hvd3MgYmV0dGVyIGNvcnJlbGF0aW9uIHdpdGggaHVtYW4ganVkZ2VtZW50LCBlc3BlY2lhbGx5IGZvciB0ZXh0LWNvbmRpdGlvbmFsIG1vZGVscyBhbmQgb3V0LW9mLWRpc3RyaWJ1dGlvbiBpbWFnZXMuIFRoZSBjb21wdXRhdGlvbiBpcyBpZGVudGljYWwgdG8gRklEIOKAlCBvbmx5IHRoZSBmZWF0dXJlIGV4dHJhY3RvciBjaGFuZ2VzLiBGb3IgbW9kZXJuIGRpZmZ1c2lvbiBtb2RlbCBldmFsdWF0aW9uLCBDTElQLUZJRCBpcyBpbmNyZWFzaW5nbHkgcHJlZmVycmVkIG92ZXIgc3RhbmRhcmQgRklELiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZWNpc2lvbiBhbmQgUmVjYWxsIGZvciBHQU5zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcmVjaXNpb24gYW5kIFJlY2FsbCAoS3lua8Okw6RubmllbWkgZXQgYWwuIDIwMTkpIGRlY29tcG9zZSBnZW5lcmF0aW9uIHF1YWxpdHkgaW50byB0d28gb3J0aG9nb25hbCBhc3BlY3RzLiBQcmVjaXNpb24gPSBmcmFjdGlvbiBvZiBnZW5lcmF0ZWQgc2FtcGxlcyB0aGF0IGZhbGwgd2l0aGluIHRoZSByZWFsIGRhdGEgbWFuaWZvbGQgKG1lYXN1cmVzIHNhbXBsZSBxdWFsaXR5IC8gZmlkZWxpdHkpLiBSZWNhbGwgPSBmcmFjdGlvbiBvZiByZWFsIHNhbXBsZXMgdGhhdCBmYWxsIHdpdGhpbiB0aGUgZ2VuZXJhdGVkIG1hbmlmb2xkIChtZWFzdXJlcyBjb3ZlcmFnZSAvIGRpdmVyc2l0eSkuIEEgbW9kZS1kcm9wcGluZyBHQU4gaGFzIGhpZ2ggcHJlY2lzaW9uIGJ1dCBsb3cgcmVjYWxsLiBBIG5vaXN5IEdBTiB0aGF0IGdlbmVyYXRlcyBibHVycnkgYXZlcmFnZXMgaGFzIGxvdyBwcmVjaXNpb24gYnV0IHBvdGVudGlhbGx5IGhpZ2ggcmVjYWxsLiBGSUQgY29uZmxhdGVzIGJvdGg7IFBcdTAwMjZSIHNlcGFyYXRlcyB0aGVtLCBlbmFibGluZyBkaWFnbm9zaXMgb2Ygc3BlY2lmaWMgZmFpbHVyZSBtb2Rlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBwcmVjaXNpb25fcmVjYWxsX21hbmlmb2xkKHJlYWxfZmVhdHMsIGZha2VfZmVhdHMsIGs9Myk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3UHJlY2lzaW9uL1JlY2FsbCB2aWEgay1OTiBtYW5pZm9sZCBlc3RpbWF0aW9uIChLeW5rYWFubmllbWkgMjAxOSkuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIGtubl9yYWRpdXMoZmVhdHMsIGspOlxuICAgICAgICAjIFNxdWFyZWQgcGFpcndpc2UgZGlzdGFuY2VzXG4gICAgICAgIHNxID0gbnAuc3VtKChmZWF0c1s6LCBOb25lXSAtIGZlYXRzW05vbmVdKSAqKiAyLCBheGlzPS0xKVxuICAgICAgICBucC5maWxsX2RpYWdvbmFsKHNxLCBucC5pbmYpXG4gICAgICAgIHJldHVybiBucC5zb3J0KHNxLCBheGlzPTEpWzosIGstMV0gICAjIGt0aC1OTiBzcXVhcmVkIGRpc3RcblxuICAgIHJfcmVhbCA9IGtubl9yYWRpdXMocmVhbF9mZWF0cywgaykgICAjIGVhY2ggcmVhbCBzYW1wbGVcdTAwMjdzIGJhbGwgcmFkaXVzXG4gICAgcl9mYWtlID0ga25uX3JhZGl1cyhmYWtlX2ZlYXRzLCBrKVxuICAgICMgZGlzdCBmcm9tIGVhY2ggZmFrZSB0byBldmVyeSByZWFsXG4gICAgZF9mMnIgID0gbnAuc3VtKChmYWtlX2ZlYXRzWzosIE5vbmVdIC0gcmVhbF9mZWF0c1tOb25lXSkqKjIsIGF4aXM9LTEpXG4gICAgcHJlYyAgID0gbnAubWVhbihucC5hbnkoZF9mMnIgXHUwMDNjIHJfcmVhbFtOb25lXSwgYXhpcz0xKSkgICMgZmFrZSBpbiByZWFsIGJhbGw/XG4gICAgIyBkaXN0IGZyb20gZWFjaCByZWFsIHRvIGV2ZXJ5IGZha2VcbiAgICBkX3IyZiAgPSBkX2Yyci5UXG4gICAgcmVjICAgID0gbnAubWVhbihucC5hbnkoZF9yMmYgXHUwMDNjIHJfZmFrZVtOb25lXSwgYXhpcz0xKSkgICMgcmVhbCBpbiBmYWtlIGJhbGw/XG4gICAgcmV0dXJuIGZsb2F0KHByZWMpLCBmbG9hdChyZWMpXG5cbm5wLnJhbmRvbS5zZWVkKDEpXG5yZWFsX2YgPSBucC5yYW5kb20ucmFuZG4oMzAwLCA2NClcbiMgR29vZCBtb2RlbDogc2FtZSBkaXN0cmlidXRpb25cbmZha2VfZ29vZCA9IG5wLnJhbmRvbS5yYW5kbigzMDAsIDY0KVxucDEsIHIxID0gcHJlY2lzaW9uX3JlY2FsbF9tYW5pZm9sZChyZWFsX2YsIGZha2VfZ29vZClcbnByaW50KFx1MDAyN0dvb2QgbW9kZWwgIC0tIFByZWNpc2lvbjogezouM2Z9ICBSZWNhbGw6IHs6LjNmfVx1MDAyNy5mb3JtYXQocDEsIHIxKSlcbiMgTW9kZSBkcm9wOiBnZW5lcmF0ZSBoYWxmIHRoZSBtb2RlcyBvbmx5XG5mYWtlX2Ryb3AgPSBucC5yYW5kb20ucmFuZG4oMzAwLCA2NCkgKiAwLjUgICAjIG5hcnJvd2VyIGRpc3RyaWJ1dGlvblxucDIsIHIyID0gcHJlY2lzaW9uX3JlY2FsbF9tYW5pZm9sZChyZWFsX2YsIGZha2VfZHJvcClcbnByaW50KFx1MDAyN01vZGUgZHJvcCAgIC0tIFByZWNpc2lvbjogezouM2Z9ICBSZWNhbGw6IHs6LjNmfVx1MDAyNy5mb3JtYXQocDIsIHIyKSkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkZJRCBSZXF1aXJlcyBMYXJnZSBTYW1wbGUgU2l6ZXMiLCJjb250ZW50IjoiRklEIGlzIG5vdG9yaW91c2x5IHVuc3RhYmxlIGF0IHNtYWxsIHNhbXBsZSBjb3VudHMuIFdpdGggTj0xMDAwIHNhbXBsZXMgZnJvbSBpZGVudGljYWwgZGlzdHJpYnV0aW9ucywgRklEIGNhbiByZWFkIDXigJMyMCBkdWUgdG8gZmluaXRlLXNhbXBsZSBub2lzZSBpbiBjb3ZhcmlhbmNlIGVzdGltYXRpb24uIFRoZSBzdGFuZGFyZCByZWNvbW1lbmRhdGlvbiBpcyBO4omlMTAwMDAgZm9yIGVhY2ggb2YgcmVhbCBhbmQgZ2VuZXJhdGVkLiBSZXBvcnRpbmcgRklEIHdpdGggTlx1MDAzYzUwMDAgd2l0aG91dCBjb25maWRlbmNlIGludGVydmFscyBpcyBtaXNsZWFkaW5nLiBUaGUgYmlhcyBvZiBGSUQgYWxzbyBkZXBlbmRzIG9uIHRoZSBmZWF0dXJlIGRpbWVuc2lvbmFsaXR5ICgyMDQ4IGZvciBJbmNlcHRpb24pOiB0aGUgY292YXJpYW5jZSBtYXRyaXggcmVxdWlyZXMgTiBcdTAwM2VcdTAwM2UgMjA0OCBzYW1wbGVzIHRvIGJlIHdlbGwtY29uZGl0aW9uZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWZmZWN0IG9mIFNhbXBsZSBTaXplIG9uIEZJRCBTdGFiaWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZJRCBpbmZsYXRlcyBkcmFtYXRpY2FsbHkgYXQgc21hbGwgTiBiZWNhdXNlIHRoZSBzYW1wbGUgY292YXJpYW5jZSBpcyBhIHBvb3IgZXN0aW1hdGUgb2YgdGhlIHRydWUgY292YXJpYW5jZSB3aGVuIE4gXHUwMDNjIGQgKHVuZGVyc2FtcGxlZCByZWdpbWUpLiBBdCBOPTEwMCB3aXRoIGQ9MjA0OCwgdGhlIGNvdmFyaWFuY2UgbWF0cml4IGlzIHJhbmstZGVmaWNpZW50IGFuZCBGSUQgaXMgZWZmZWN0aXZlbHkgbWVhbmluZ2xlc3MuIEFzIE4gZ3Jvd3MsIEZJRCBjb252ZXJnZXMgdG8gdGhlIHBvcHVsYXRpb24gdmFsdWUuIFBsb3R0aW5nIEZJRCB2cyBOIGZvciB5b3VyIG1vZGVsIGlzIGEgZGlhZ25vc3RpYyB0b29sOiBpZiBGSUQgaXMgc3RpbGwgY2hhbmdpbmcgc2lnbmlmaWNhbnRseSBhdCBOPTEwSywgaW5jcmVhc2UgdGhlIHNhbXBsZSBjb3VudCBiZWZvcmUgcmVwb3J0aW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkubGluYWxnIGltcG9ydCBzcXJ0bVxuXG5kZWYgZmlkX3ZzX24oZD02NCwgbl92YWx1ZXM9Tm9uZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3RklEIGJldHdlZW4gaWRlbnRpY2FsIGRpc3RyaWJ1dGlvbnMgYXQgZGlmZmVyZW50IHNhbXBsZSBzaXplcy5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBpZiBuX3ZhbHVlcyBpcyBOb25lOlxuICAgICAgICBuX3ZhbHVlcyA9IFs1MCwgMTAwLCA1MDAsIDEwMDAsIDUwMDBdXG4gICAgbnAucmFuZG9tLnNlZWQoNDIpXG4gICAgcG9wID0gbnAucmFuZG9tLnJhbmRuKDIwMDAwLCBkKVxuICAgIGZvciBOIGluIG5fdmFsdWVzOlxuICAgICAgICByZWFsX3MgPSBwb3BbOk5dOyBmYWtlX3MgPSBwb3BbTjoyKk5dXG4gICAgICAgIG11X3IsIHNpZ19yID0gcmVhbF9zLm1lYW4oMCksIG5wLmNvdihyZWFsX3MsIHJvd3Zhcj1GYWxzZSlcbiAgICAgICAgbXVfZiwgc2lnX2YgPSBmYWtlX3MubWVhbigwKSwgbnAuY292KGZha2Vfcywgcm93dmFyPUZhbHNlKVxuICAgICAgICBjbSA9IHNxcnRtKHNpZ19yIEAgc2lnX2YpXG4gICAgICAgIGNtID0gY20ucmVhbCBpZiBucC5pc2NvbXBsZXhvYmooY20pIGVsc2UgY21cbiAgICAgICAgZmlkID0gZmxvYXQobnAuZG90KG11X3ItbXVfZiwgbXVfci1tdV9mKSArXG4gICAgICAgICAgICAgICAgICAgIG5wLnRyYWNlKHNpZ19yICsgc2lnX2YgLSAyKmNtKSlcbiAgICAgICAgcHJpbnQoXHUwMDI3Tj17OjZkfSAgRklEPXs6LjFmfVx1MDAyNy5mb3JtYXQoTiwgZmlkKSlcblxuZmlkX3ZzX24oZD02NClcbnByaW50KFx1MDAyN0ZJRCBpbmZsYXRlcyBhdCBzbWFsbCBOIGV2ZW4gd2hlbiByZWFsIGFuZCBmYWtlIGRpc3RyaWJ1dGlvbnMgYXJlIGlkZW50aWNhbCFcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEd1aWRhbmNlIGZvciBHQU4gRXZhbHVhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVXNlIEZJRCBhcyB0aGUgcHJpbWFyeSBtZXRyaWMgYnV0IGFsd2F5cyByZXBvcnQgc2FtcGxlIGNvdW50IGFuZCB3aGV0aGVyIGZlYXR1cmVzIGFyZSBmcm9tIEluY2VwdGlvbiBvciBDTElQLiBSZXBvcnQgcHJlY2lzaW9uIGFuZCByZWNhbGwgd2hlbiBkaWFnbm9zaW5nIG1vZGUgY29sbGFwc2UgdnMgcXVhbGl0eSBpc3N1ZXMuIElTIGlzIGxhcmdlbHkgZGVwcmVjYXRlZCBmb3IgY29uZGl0aW9uYWwgbW9kZWxzIOKAlCBpdCBkb2VzIG5vdCBwZW5hbGlzZSBtZW1vcmlzYXRpb24uIENMSVAtRklEIGlzIHByZWZlcnJlZCBmb3IgdGV4dC1jb25kaXRpb25hbCBtb2RlbHMuIEZvciBwYWlyZWQgdHJhbnNsYXRpb24gKFBpeDJQaXgpLCBwaXhlbC1sZXZlbCBtZXRyaWNzIFBTTlIgYW5kIFNTSU0gYWdhaW5zdCBncm91bmQgdHJ1dGggYXJlIG1vc3QgaW5mb3JtYXRpdmUuIEFsd2F5cyBjb21wdXRlIG1ldHJpY3Mgb24gYSBmaXhlZCBoZWxkLW91dCByZWFsIHNldCB0byBlbmFibGUgZmFpciBjb21wYXJpc29uIGFjcm9zcyBjaGVja3BvaW50cy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZJRDogcHJpbWFyeSBtZXRyaWM7IHVzZSBOXHUwMDNlPTEwMDAwOyBsb3dlciBpcyBiZXR0ZXI7IHJlcXVpcmVzIEluY2VwdGlvbiBvciBDTElQIGZlYXR1cmVzLiIsIklTOiBzZWNvbmRhcnk7IGlnbm9yZXMgcmVhbCBkYXRhOyBnYW1lYWJsZTsgbW9zdGx5IGRlcHJlY2F0ZWQgZm9yIG1vZGVybiBjb25kaXRpb25hbCBtb2RlbHMuIiwiQ0xJUC1GSUQ6IHByZWZlcnJlZCBmb3IgdGV4dC1jb25kaXRpb25hbCBhbmQgb3Blbi12b2NhYnVsYXJ5IGdlbmVyYXRpb24gdGFza3MuIiwiUHJlY2lzaW9uOiBtZWFzdXJlcyBzYW1wbGUgZmlkZWxpdHkg4oCUIGFyZSBnZW5lcmF0ZWQgc2FtcGxlcyBvbiB0aGUgcmVhbCBtYW5pZm9sZD8iLCJSZWNhbGw6IG1lYXN1cmVzIGRpdmVyc2l0eSBjb3ZlcmFnZSDigJQgZG9lcyB0aGUgZ2VuZXJhdGVkIG1hbmlmb2xkIGNvdmVyIHRoZSByZWFsIG1hbmlmb2xkPyIsIlBTTlIvU1NJTTogb25seSBtZWFuaW5nZnVsIGZvciBwYWlyZWQgdHJhbnNsYXRpb24gd2hlcmUgZ3JvdW5kIHRydXRoIGV4aXN0cy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWV0cmljIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0cmljIiwiV2hhdCBJdCBNZWFzdXJlcyIsIkNvbXBhcmVzIHRvIFJlYWwgRGF0YSIsIlNhbXBsZSBTaXplIE5lZWRlZCIsIk1vZGVybiBQcmVmZXJlbmNlIl0sInJvd3MiOltbIklTIiwiUXVhbGl0eSArIGRpdmVyc2l0eSB2aWEgSW5jZXB0aW9uIGxhYmVscyIsIk5vIiwiTlx1MDAzZT01MDAwIiwiTG93IChnYW1lYWJsZSwgbm8gcmVhbCBjb21wYXJpc29uKSJdLFsiRklEIiwiRmVhdHVyZSBkaXN0cmlidXRpb24gZGlzdGFuY2UgKEZyZWNoZXQpIiwiWWVzIiwiTlx1MDAzZT0xMDAwMCIsIkhpZ2gg4oCUIHN0YW5kYXJkIGJlbmNobWFyayJdLFsiQ0xJUC1GSUQiLCJGSUQgd2l0aCBDTElQIGZlYXR1cmVzIChzZW1hbnRpYykiLCJZZXMiLCJOXHUwMDNlPTEwMDAwIiwiSGlnaCBmb3IgdGV4dC1jb25kaXRpb25hbCBtb2RlbHMiXSxbIlByZWNpc2lvbiIsIlNhbXBsZSBmaWRlbGl0eSAoZmFrZSBpbiByZWFsIG1hbmlmb2xkKSIsIlllcyIsIk5cdTAwM2U9NTAwMCIsIk1lZGl1bSDigJQgdXNlIHdpdGggUmVjYWxsIl0sWyJSZWNhbGwiLCJDb3ZlcmFnZSBkaXZlcnNpdHkgKHJlYWwgaW4gZmFrZSBtYW5pZm9sZCkiLCJZZXMiLCJOXHUwMDNlPTUwMDAiLCJNZWRpdW0g4oCUIHVzZSB3aXRoIFByZWNpc2lvbiJdXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# GAN Evaluation — FID, IS, and Precision/Recall

Evaluating generative models is fundamentally harder than discriminative models: there is no held-out test set with labels, and visual quality is subjective. The field has converged on automatic metrics computed over large sample sets — primarily FID and IS — but each has failure modes. Understanding what each metric measures, what biases it has, and when it misleads is essential for correctly interpreting GAN training progress and comparing models across papers.

## Inception Score (IS)

IS (Salimans et al. 2016) measures two properties using a pretrained Inception v3 classifier: (1) quality — individual images should have confident (low-entropy) class predictions p(y|x); (2) diversity — the marginal p(y) = E_x[p(y|x)] should be uniform over classes. IS = exp(E_x[KL(p(y|x) ‖ p(y))]). Higher IS is better. Problems: IS does not compare generated images to real images at all — a model memorising the training set with perfect class balance achieves maximum IS. It is also sensitive to the Inception preprocessing and known to be gameable.

```python
import torch
import torch.nn as nn
import numpy as np

def inception_score(pyx_all, n_splits=10):
    '''IS from pre-extracted p(y|x) softmax probabilities.
    pyx_all: (N, C) numpy array of class probabilities.
    Returns (mean IS, std IS) across splits.'''
    N, C = pyx_all.shape
    split_sz = N // n_splits
    scores = []
    for i in range(n_splits):
        part = pyx_all[i*split_sz : (i+1)*split_sz]  # (M, C)
        py   = part.mean(axis=0, keepdims=True)        # marginal p(y)
        kl   = np.sum(part * (np.log(part + 1e-10) -
                              np.log(py   + 1e-10)), axis=1)  # per-sample KL
        scores.append(float(np.exp(kl.mean())))
    return float(np.mean(scores)), float(np.std(scores))

np.random.seed(42)
N, C = 1000, 10
# High-quality: peaked, diverse -> high IS
pyx_good = np.eye(C)[np.random.randint(0, C, N)] * 0.9 + 0.01
pyx_good /= pyx_good.sum(1, keepdims=True)
mean_is, std_is = inception_score(pyx_good)
print('High-quality IS: {:.2f} +/- {:.2f}'.format(mean_is, std_is))
# Low-diversity: all predict class 0
pyx_bad = np.zeros((N, C)); pyx_bad[:, 0] = 0.99; pyx_bad[:, 1:] = 0.01/9
mean_b, std_b = inception_score(pyx_bad)
print('Low-diversity IS: {:.2f} +/- {:.2f}'.format(mean_b, std_b))
```

## Fréchet Inception Distance (FID)

FID (Heusel et al. 2017) compares the distribution of real images to that of generated images using features extracted from Inception v3's pool3 layer (2048-d). Both sets of features are modelled as multivariate Gaussians; FID is the Fréchet distance between them: FID = ‖μ_r − μ_g‖² + Tr(Σ_r + Σ_g − 2(Σ_rΣ_g)^{1/2}). Lower FID means the generated distribution is closer to real. FID is sensitive to both quality (Σ mismatch from blurry images) and diversity (μ mismatch from mode collapse). Standard practice: use ≥10K generated and ≥10K real samples to stabilise the estimate.

```python
import numpy as np
from scipy.linalg import sqrtm

def frechet_distance(mu1, sigma1, mu2, sigma2, eps=1e-6):
    '''FID = ||mu1-mu2||^2 + Tr(sigma1 + sigma2 - 2*sqrtm(sigma1@sigma2)).'''
    diff = mu1 - mu2
    covmean, _ = sqrtm(sigma1 @ sigma2, disp=False)
    if not np.isfinite(covmean).all():
        offset = np.eye(sigma1.shape[0]) * eps
        covmean = sqrtm((sigma1 + offset) @ (sigma2 + offset))
    if np.iscomplexobj(covmean):
        covmean = covmean.real
    return float(diff @ diff + np.trace(sigma1 + sigma2 - 2*covmean))

np.random.seed(0)
d = 256   # reduced from 2048 for demo speed
N = 500
real_feats = np.random.randn(N, d)
# Same distribution -> FID near 0
fake_same = np.random.randn(N, d)
mu_r, sig_r = real_feats.mean(0), np.cov(real_feats, rowvar=False)
mu_s, sig_s = fake_same.mean(0),  np.cov(fake_same,  rowvar=False)
fid_good = frechet_distance(mu_r, sig_r, mu_s, sig_s)
print('FID (same dist): {:.2f}'.format(fid_good))
# Shifted distribution -> higher FID
fake_shift = np.random.randn(N, d) + 0.5
mu_sh, sig_sh = fake_shift.mean(0), np.cov(fake_shift, rowvar=False)
fid_bad = frechet_distance(mu_r, sig_r, mu_sh, sig_sh)
print('FID (shifted):   {:.2f}'.format(fid_bad))
```

## CLIP-FID and Semantic Features

Inception v3 was trained on ImageNet and its features are biased toward ImageNet categories. CLIP-FID (Kynkäänniemi et al. 2022) replaces the Inception pool3 features with CLIP ViT-L/14 features, which are more semantically meaningful and better aligned with human perception. CLIP-FID shows better correlation with human judgement, especially for text-conditional models and out-of-distribution images. The computation is identical to FID — only the feature extractor changes. For modern diffusion model evaluation, CLIP-FID is increasingly preferred over standard FID.

## Precision and Recall for GANs

Precision and Recall (Kynkäänniemi et al. 2019) decompose generation quality into two orthogonal aspects. Precision = fraction of generated samples that fall within the real data manifold (measures sample quality / fidelity). Recall = fraction of real samples that fall within the generated manifold (measures coverage / diversity). A mode-dropping GAN has high precision but low recall. A noisy GAN that generates blurry averages has low precision but potentially high recall. FID conflates both; P&R separates them, enabling diagnosis of specific failure modes.

```python
import numpy as np

def precision_recall_manifold(real_feats, fake_feats, k=3):
    '''Precision/Recall via k-NN manifold estimation (Kynkaanniemi 2019).'''
    def knn_radius(feats, k):
        # Squared pairwise distances
        sq = np.sum((feats[:, None] - feats[None]) ** 2, axis=-1)
        np.fill_diagonal(sq, np.inf)
        return np.sort(sq, axis=1)[:, k-1]   # kth-NN squared dist

    r_real = knn_radius(real_feats, k)   # each real sample's ball radius
    r_fake = knn_radius(fake_feats, k)
    # dist from each fake to every real
    d_f2r  = np.sum((fake_feats[:, None] - real_feats[None])**2, axis=-1)
    prec   = np.mean(np.any(d_f2r < r_real[None], axis=1))  # fake in real ball?
    # dist from each real to every fake
    d_r2f  = d_f2r.T
    rec    = np.mean(np.any(d_r2f < r_fake[None], axis=1))  # real in fake ball?
    return float(prec), float(rec)

np.random.seed(1)
real_f = np.random.randn(300, 64)
# Good model: same distribution
fake_good = np.random.randn(300, 64)
p1, r1 = precision_recall_manifold(real_f, fake_good)
print('Good model  -- Precision: {:.3f}  Recall: {:.3f}'.format(p1, r1))
# Mode drop: generate half the modes only
fake_drop = np.random.randn(300, 64) * 0.5   # narrower distribution
p2, r2 = precision_recall_manifold(real_f, fake_drop)
print('Mode drop   -- Precision: {:.3f}  Recall: {:.3f}'.format(p2, r2))
```

> **FID Requires Large Sample Sizes**: FID is notoriously unstable at small sample counts. With N=1000 samples from identical distributions, FID can read 5–20 due to finite-sample noise in covariance estimation. The standard recommendation is N≥10000 for each of real and generated. Reporting FID with N<5000 without confidence intervals is misleading. The bias of FID also depends on the feature dimensionality (2048 for Inception): the covariance matrix requires N >> 2048 samples to be well-conditioned.

## Effect of Sample Size on FID Stability

FID inflates dramatically at small N because the sample covariance is a poor estimate of the true covariance when N < d (undersampled regime). At N=100 with d=2048, the covariance matrix is rank-deficient and FID is effectively meaningless. As N grows, FID converges to the population value. Plotting FID vs N for your model is a diagnostic tool: if FID is still changing significantly at N=10K, increase the sample count before reporting.

```python
import numpy as np
from scipy.linalg import sqrtm

def fid_vs_n(d=64, n_values=None):
    '''FID between identical distributions at different sample sizes.'''
    if n_values is None:
        n_values = [50, 100, 500, 1000, 5000]
    np.random.seed(42)
    pop = np.random.randn(20000, d)
    for N in n_values:
        real_s = pop[:N]; fake_s = pop[N:2*N]
        mu_r, sig_r = real_s.mean(0), np.cov(real_s, rowvar=False)
        mu_f, sig_f = fake_s.mean(0), np.cov(fake_s, rowvar=False)
        cm = sqrtm(sig_r @ sig_f)
        cm = cm.real if np.iscomplexobj(cm) else cm
        fid = float(np.dot(mu_r-mu_f, mu_r-mu_f) +
                    np.trace(sig_r + sig_f - 2*cm))
        print('N={:6d}  FID={:.1f}'.format(N, fid))

fid_vs_n(d=64)
print('FID inflates at small N even when real and fake distributions are identical!')
```

## Practical Guidance for GAN Evaluation

Use FID as the primary metric but always report sample count and whether features are from Inception or CLIP. Report precision and recall when diagnosing mode collapse vs quality issues. IS is largely deprecated for conditional models — it does not penalise memorisation. CLIP-FID is preferred for text-conditional models. For paired translation (Pix2Pix), pixel-level metrics PSNR and SSIM against ground truth are most informative. Always compute metrics on a fixed held-out real set to enable fair comparison across checkpoints.

- FID: primary metric; use N>=10000; lower is better; requires Inception or CLIP features.
- IS: secondary; ignores real data; gameable; mostly deprecated for modern conditional models.
- CLIP-FID: preferred for text-conditional and open-vocabulary generation tasks.
- Precision: measures sample fidelity — are generated samples on the real manifold?
- Recall: measures diversity coverage — does the generated manifold cover the real manifold?
- PSNR/SSIM: only meaningful for paired translation where ground truth exists.

## Metric Comparison

| Metric | What It Measures | Compares to Real Data | Sample Size Needed | Modern Preference |
| --- | --- | --- | --- | --- |
| IS | Quality + diversity via Inception labels | No | N>=5000 | Low (gameable, no real comparison) |
| FID | Feature distribution distance (Frechet) | Yes | N>=10000 | High — standard benchmark |
| CLIP-FID | FID with CLIP features (semantic) | Yes | N>=10000 | High for text-conditional models |
| Precision | Sample fidelity (fake in real manifold) | Yes | N>=5000 | Medium — use with Recall |
| Recall | Coverage diversity (real in fake manifold) | Yes | N>=5000 | Medium — use with Precision |

---

