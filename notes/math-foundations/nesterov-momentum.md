---
title: "Nesterov Accelerated Gradient (NAG)"
slug: "nesterov-momentum"
description: "Derivation of Nesterov accelerated gradient from the lookahead correction, convergence rate analysis achieving O(1/T²), the variable substitution implementation trick, and connection to Adam's Nesterov variant."
tags: ["optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTmVzdGVyb3YgQWNjZWxlcmF0ZWQgR3JhZGllbnQgaXMgdGhlIHRoZW9yZXRpY2FsbHkgb3B0aW1hbCBmaXJzdC1vcmRlciBtZXRob2QgZm9yIGNvbnZleCBzbW9vdGggb3B0aW1pemF0aW9uLCBhY2hpZXZpbmcgdGhlIE8oMS9UwrIpIGNvbnZlcmdlbmNlIHJhdGUgdGhhdCBtYXRjaGVzIGluZm9ybWF0aW9uLXRoZW9yZXRpYyBsb3dlciBib3VuZHMgZm9yIHRoaXMgZnVuY3Rpb24gY2xhc3MuIFRoZSBrZXkgaW5zaWdodCDigJQgZXZhbHVhdGUgdGhlIGdyYWRpZW50IGF0IHRoZSBhbnRpY2lwYXRlZCBmdXR1cmUgcG9zaXRpb24gKM64IOKIkiDOsnYpIHJhdGhlciB0aGFuIHRoZSBjdXJyZW50IHBvc2l0aW9uIM64IOKAlCBwcm9kdWNlcyBhIGNvcnJlY3Rpb24gdGhhdCBkcmFtYXRpY2FsbHkgcmVkdWNlcyBvdmVyc2hvb3QgYW5kIGFjaGlldmVzIG9wdGltYWwgY29udmVyZ2VuY2UuIEJleW9uZCBpdHMgdGhlb3JldGljYWwgZWxlZ2FuY2UsIE5BRyBpcyBwcmFjdGljYWxseSBpbXBvcnRhbnQ6IFB5VG9yY2gncyBTR0Qgd2l0aCBuZXN0ZXJvdj1UcnVlIHVzZXMgaXQ7IHRoZSBOZXN0ZXJvdi1zdHlsZSBtb21lbnR1bSBjb3JyZWN0aW9uIGFsc28gYXBwZWFycyBpbiBBZGFtLWJhc2VkIHZhcmlhbnRzIGxpa2UgTmFkYW0uIFVuZGVyc3RhbmRpbmcgTkFHJ3MgY29udmVyZ2VuY2UgcHJvb2YgKHZpYSBwb3RlbnRpYWwgZnVuY3Rpb25zIGFuZCBlbmVyZ3kgYXJndW1lbnRzKSByZXZlYWxzIHdoeSB0aGUgc3BlY2lmaWMgdXBkYXRlIG9yZGVyIG1hdHRlcnMgYW5kIHdoeSB0aGUgbG9va2FoZWFkIGdyYWRpZW50IHByb3ZpZGVzIHN0cmljdGx5IG1vcmUgaW5mb3JtYXRpb24gdGhhbiB0aGUgY3VycmVudC1wb3NpdGlvbiBncmFkaWVudC4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJDb3JlIERlZmluaXRpb246IFRoZSBMb29rYWhlYWQgQ29ycmVjdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkhlYXZ5IGJhbGwgKGNsYXNzaWNhbCBtb21lbnR1bSk6IHbigpwgPSDOsnbigpzigovigoEgKyDOt2cozrjigpwpOyDOuOKCnOKCiuKCgSA9IM644oKcIOKIkiB24oKcLiBOZXN0ZXJvdidzIGNvcnJlY3Rpb246IGV2YWx1YXRlIHRoZSBncmFkaWVudCBhdCB0aGUgYW50aWNpcGF0ZWQgcG9zaXRpb24gzrjigpwg4oiSIM6yduKCnOKCi+KCgSAod2hlcmUgd2Ugd2lsbCBsYW5kIGFmdGVyIGFwcGx5aW5nIHRoZSBjdXJyZW50IHZlbG9jaXR5KSByYXRoZXIgdGhhbiBhdCDOuOKCnCBpdHNlbGYuIFVwZGF0ZTogduKCnCA9IM6yduKCnOKCi+KCgSArIM634oiHZijOuOKCnCDiiJIgzrJ24oKc4oKL4oKBKTsgzrjigpzigorigoEgPSDOuOKCnCDiiJIgduKCnC4gVGhlIGxvb2thaGVhZCBwb3NpdGlvbiDOuOKCnCDiiJIgzrJ24oKc4oKL4oKBIGlzIGEgZmlyc3Qtb3JkZXIgcHJlZGljdGlvbiBvZiB3aGVyZSDOuOKCnOKCiuKCgSB3b3VsZCBsYW5kIHdpdGggdGhlIGN1cnJlbnQgdmVsb2NpdHkgYWxvbmUuIEV2YWx1YXRpbmcgdGhlIGdyYWRpZW50IHRoZXJlIGluc3RlYWQgb2YgYXQgzrjigpwgcHJvdmlkZXMgYSBjb3JyZWN0aW9uIHRoYXQgYWNjb3VudHMgZm9yIG1vbWVudHVtOiBpZiB0aGUgZ3JhZGllbnQgYXQgdGhlIGxvb2thaGVhZCBwb3NpdGlvbiBvcHBvc2VzIHRoZSB2ZWxvY2l0eSwgTkFHIGJyYWtlcyBlYXJseSwgcHJldmVudGluZyBvdmVyc2hvb3QuIFRoaXMgbG9va2FoZWFkIGNvcnJlY3Rpb24gaXMgd2h5IE5BRyBhY2hpZXZlcyBPKDEvVMKyKSBmb3IgZ2VuZXJhbCBjb252ZXggZnVuY3Rpb25zLCB3aGlsZSBoZWF2eSBiYWxsIG9ubHkgYWNoaWV2ZXMgTygxL1TCsikgZm9yIHF1YWRyYXRpY3Mgc3BlY2lmaWNhbGx5LiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG5lc3Rlcm92X2FnKGdyYWRfZiwgdGhldGEwLCBsciwgYmV0YSwgbl9zdGVwcywgZj1Ob25lKTpcbiAgICBcIlwiXCJcbiAgICBOZXN0ZXJvdiBBY2NlbGVyYXRlZCBHcmFkaWVudC5cbiAgICBFdmFsdWF0ZXMgZ3JhZGllbnQgYXQgbG9vay1haGVhZCBwb3NpdGlvbjogdGhldGEgLSBiZXRhICogdi5cbiAgICBcIlwiXCJcbiAgICB0aGV0YSA9IG5wLmFycmF5KHRoZXRhMCwgZHR5cGU9bnAuZmxvYXQ2NClcbiAgICB2ID0gbnAuemVyb3NfbGlrZSh0aGV0YSlcbiAgICBsb3NzZXMgPSBbZih0aGV0YSldIGlmIGYgZWxzZSBbXVxuXG4gICAgZm9yIHQgaW4gcmFuZ2Uobl9zdGVwcyk6XG4gICAgICAgICMgS2V5IGRpZmZlcmVuY2UgZnJvbSBoZWF2eSBiYWxsOiBncmFkaWVudCBhdCBsb29rYWhlYWQgcG9zaXRpb25cbiAgICAgICAgbG9va2FoZWFkID0gdGhldGEgLSBiZXRhICogdlxuICAgICAgICBnID0gZ3JhZF9mKGxvb2thaGVhZClcbiAgICAgICAgdiA9IGJldGEgKiB2ICsgbHIgKiBnXG4gICAgICAgIHRoZXRhID0gdGhldGEgLSB2XG4gICAgICAgIGlmIGY6IGxvc3Nlcy5hcHBlbmQoZih0aGV0YSkpXG5cbiAgICByZXR1cm4gbG9zc2VzXG5cbmRlZiBoZWF2eV9iYWxsKGdyYWRfZiwgdGhldGEwLCBsciwgYmV0YSwgbl9zdGVwcywgZj1Ob25lKTpcbiAgICBcIlwiXCJDbGFzc2ljYWwgbW9tZW50dW0gKGhlYXZ5IGJhbGwpOiBncmFkaWVudCBhdCBjdXJyZW50IHBvc2l0aW9uLlwiXCJcIlxuICAgIHRoZXRhID0gbnAuYXJyYXkodGhldGEwLCBkdHlwZT1ucC5mbG9hdDY0KVxuICAgIHYgPSBucC56ZXJvc19saWtlKHRoZXRhKVxuICAgIGxvc3NlcyA9IFtmKHRoZXRhKV0gaWYgZiBlbHNlIFtdXG5cbiAgICBmb3IgdCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgZyA9IGdyYWRfZih0aGV0YSkgICMgZ3JhZGllbnQgYXQgY3VycmVudCBwb3NpdGlvbiAobm90IGxvb2thaGVhZClcbiAgICAgICAgdiA9IGJldGEgKiB2ICsgbHIgKiBnXG4gICAgICAgIHRoZXRhID0gdGhldGEgLSB2XG4gICAgICAgIGlmIGY6IGxvc3Nlcy5hcHBlbmQoZih0aGV0YSkpXG5cbiAgICByZXR1cm4gbG9zc2VzXG5cbiMgQ29tcGFyZSBvbiBpbGwtY29uZGl0aW9uZWQgcXVhZHJhdGljOiBmKHgseSkgPSAwLjUqKHheMiArIDEwMCp5XjIpXG5mID0gbGFtYmRhIHg6IDAuNSAqICh4WzBdKioyICsgMTAwKnhbMV0qKjIpXG5ncmFkX2YgPSBsYW1iZGEgeDogbnAuYXJyYXkoW3hbMF0sIDEwMCp4WzFdXSlcbngwID0gbnAuYXJyYXkoWzEwLjAsIDEuMF0pXG5cbkwsIG11ID0gMTAwLjAsIDEuMFxuYmV0YV9vcHQgPSAobnAuc3FydChMKSAtIG5wLnNxcnQobXUpKSAvIChucC5zcXJ0KEwpICsgbnAuc3FydChtdSkpXG5scl9vcHQgPSAoMSAvIChucC5zcXJ0KEwpICsgbnAuc3FydChtdSkpKSoqMiAqIDQgICMgYXBwcm94IG9wdGltYWwgZm9yIE5BR1xuXG5sb3NzZXNfbmFnID0gbmVzdGVyb3ZfYWcoZ3JhZF9mLCB4MCwgbHI9bHJfb3B0LCBiZXRhPWJldGFfb3B0LCBuX3N0ZXBzPTIwMCwgZj1mKVxubG9zc2VzX2hiID0gaGVhdnlfYmFsbChncmFkX2YsIHgwLCBscj1scl9vcHQsIGJldGE9YmV0YV9vcHQsIG5fc3RlcHM9MjAwLCBmPWYpXG5cbmRlZiBzdGVwc190byhsb3NzZXMsIHRocmVzaG9sZD0xZS00KTpcbiAgICByZXR1cm4gbmV4dCgoaSBmb3IgaSwgbCBpbiBlbnVtZXJhdGUobG9zc2VzKSBpZiBsIDwgdGhyZXNob2xkKSwgbGVuKGxvc3NlcykpXG5cbnByaW50KGZcImJldGFfb3B0ID0ge2JldGFfb3B0Oi40Zn1cIilcbnByaW50KGZcIk5BRzoge3N0ZXBzX3RvKGxvc3Nlc19uYWcpfSBzdGVwcyB0byAxZS00XCIpXG5wcmludChmXCJIZWF2eSBiYWxsOiB7c3RlcHNfdG8obG9zc2VzX2hiKX0gc3RlcHMgdG8gMWUtNFwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlZhcmlhYmxlIFN1YnN0aXR1dGlvbjogVGhlIEVmZmljaWVudCBJbXBsZW1lbnRhdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIk5haXZlbHkgaW1wbGVtZW50aW5nIE5BRyByZXF1aXJlcyBjb21wdXRpbmcgdGhlIGdyYWRpZW50IGF0IHR3byBwb2ludHMgcGVyIHN0ZXAgKM644oKcIGFuZCDOuOKCnCDiiJIgzrJ24oKc4oKL4oKBKS4gVGhlIHZhcmlhYmxlIHN1YnN0aXR1dGlvbiDPhuKCnCA9IM644oKcIOKIkiDOsnbigpzigovigoEgKGRlZmluZSB0aGUgbG9va2FoZWFkIHBvc2l0aW9uIGFzIGEgbmV3IHZhcmlhYmxlKSBlbGltaW5hdGVzIHRoaXMgb3ZlcmhlYWQuIEluIHRlcm1zIG9mIM+G4oKcLCBhZnRlciBhbGdlYnJhaWMgbWFuaXB1bGF0aW9uIG9mIHRoZSBvcmlnaW5hbCB1cGRhdGUgZXF1YXRpb25zLCB0aGUgdXBkYXRlIHNpbXBsaWZpZXMgdG86IM+G4oKc4oKK4oKBID0gz4bigpwgKyDOsijPhuKCnCDiiJIgz4bigpzigovigoEpIOKIkiDOt+KIh2Yoz4bigpwpLiBJbiB0aGlzIGZvcm0sIHRoZSBncmFkaWVudCBpcyBhbHdheXMgZXZhbHVhdGVkIGF0IM+G4oKcICh0aGUgY3VycmVudCBwb2ludCksIGFuZCB0aGUgbW9tZW50dW0gdGVybSBpcyB0aGUgZGlzcGxhY2VtZW50IM+G4oKcIOKIkiDPhuKCnOKCi+KCgSBmcm9tIHRoZSBwcmV2aW91cyBzdGVwLiBUaGlzIHJlcXVpcmVzIG9ubHkgb25lIGdyYWRpZW50IGV2YWx1YXRpb24gcGVyIHN0ZXAg4oCUIHRoZSBzYW1lIGNvc3QgYXMgdmFuaWxsYSBHRCBvciBoZWF2eSBiYWxsLiBQeVRvcmNoJ3MgU0dEIHdpdGggbmVzdGVyb3Y9VHJ1ZSB1c2VzIHRoaXMgZXF1aXZhbGVudCBzaW5nbGUtdmFyaWFibGUgZm9ybSBpbnRlcm5hbGx5LCBzdG9yaW5nIGEgbW9tZW50dW0gYnVmZmVyIGJ1ZiBhbmQgY29tcHV0aW5nIHRoZSBOZXN0ZXJvdi1jb3JyZWN0ZWQgZ3JhZGllbnQgYXMgZyArIM6ywrdidWYuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbmVzdGVyb3Zfc2luZ2xlX3ZhcmlhYmxlKGdyYWRfZiwgcGhpMCwgbHIsIGJldGEsIG5fc3RlcHMsIGY9Tm9uZSk6XG4gICAgXCJcIlwiXG4gICAgTkFHIHVzaW5nIHRoZSBwaGktdmFyaWFibGUgc3Vic3RpdHV0aW9uLlxuICAgIHBoaV97dCsxfSA9IHBoaV90ICsgYmV0YSoocGhpX3QgLSBwaGlfe3QtMX0pIC0gZXRhKmdyYWQoZikocGhpX3QpXG4gICAgT25seSBPTkUgZ3JhZGllbnQgZXZhbHVhdGlvbiBwZXIgc3RlcCAoYXQgY3VycmVudCBwaGkpLlxuICAgIE1hdGhlbWF0aWNhbGx5IGVxdWl2YWxlbnQgdG8gdGhlIGxvb2thaGVhZCBmb3JtdWxhdGlvbi5cbiAgICBcIlwiXCJcbiAgICBwaGkgPSBucC5hcnJheShwaGkwLCBkdHlwZT1ucC5mbG9hdDY0KVxuICAgIHBoaV9wcmV2ID0gcGhpLmNvcHkoKVxuICAgIGxvc3NlcyA9IFtmKHBoaSldIGlmIGYgZWxzZSBbXVxuXG4gICAgZm9yIHQgaW4gcmFuZ2Uobl9zdGVwcyk6XG4gICAgICAgIGcgPSBncmFkX2YocGhpKVxuICAgICAgICBwaGlfbmV3ID0gcGhpICsgYmV0YSAqIChwaGkgLSBwaGlfcHJldikgLSBsciAqIGdcbiAgICAgICAgcGhpX3ByZXYgPSBwaGlcbiAgICAgICAgcGhpID0gcGhpX25ld1xuICAgICAgICBpZiBmOiBsb3NzZXMuYXBwZW5kKGYocGhpKSlcblxuICAgIHJldHVybiBsb3NzZXNcblxuZGVmIG5lc3Rlcm92X3B5dG9yY2hfc3R5bGUoZ3JhZF9mLCB0aGV0YTAsIGxyLCBiZXRhLCBuX3N0ZXBzLCBmPU5vbmUpOlxuICAgIFwiXCJcIlxuICAgIFB5VG9yY2gncyBTR0QgbmVzdGVyb3Y9VHJ1ZSBpbXBsZW1lbnRhdGlvbi5cbiAgICBTdG9yZXMgYnVmIChtb21lbnR1bSBidWZmZXIpIGFuZCB1cGRhdGVzIHdpdGggTmVzdGVyb3YgY29ycmVjdGlvbi5cbiAgICBcIlwiXCJcbiAgICB0aGV0YSA9IG5wLmFycmF5KHRoZXRhMCwgZHR5cGU9bnAuZmxvYXQ2NClcbiAgICBidWYgPSBucC56ZXJvc19saWtlKHRoZXRhKVxuICAgIGxvc3NlcyA9IFtmKHRoZXRhKV0gaWYgZiBlbHNlIFtdXG5cbiAgICBmb3IgdCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgZyA9IGdyYWRfZih0aGV0YSlcbiAgICAgICAgYnVmID0gYmV0YSAqIGJ1ZiArIGcgICAgICAgICAgICAgICAgICAgICMgbW9tZW50dW0gYnVmZmVyXG4gICAgICAgICMgTmVzdGVyb3Y6IGFkZCBiZXRhICogYnVmIHRvIGdyYWRpZW50IGJlZm9yZSBzdGVwcGluZ1xuICAgICAgICBnX25lc3Rlcm92ID0gZyArIGJldGEgKiBidWZcbiAgICAgICAgdGhldGEgPSB0aGV0YSAtIGxyICogZ19uZXN0ZXJvdlxuICAgICAgICBpZiBmOiBsb3NzZXMuYXBwZW5kKGYodGhldGEpKVxuXG4gICAgcmV0dXJuIGxvc3Nlc1xuXG4jIFZlcmlmeSBib3RoIGZvcm11bGF0aW9ucyBnaXZlIHNhbWUgY29udmVyZ2VuY2VcbmYgPSBsYW1iZGEgeDogMC41ICogKHhbMF0qKjIgKyAxMDAqeFsxXSoqMilcbmdyYWRfZiA9IGxhbWJkYSB4OiBucC5hcnJheShbeFswXSwgMTAwKnhbMV1dKVxueDAgPSBucC5hcnJheShbMTAuMCwgMS4wXSlcblxubG9zc2VzX3N2ID0gbmVzdGVyb3Zfc2luZ2xlX3ZhcmlhYmxlKGdyYWRfZiwgeDAuY29weSgpLCBscj0wLjAwMiwgYmV0YT0wLjgxLCBuX3N0ZXBzPTIwMCwgZj1mKVxubG9zc2VzX3B0ID0gbmVzdGVyb3ZfcHl0b3JjaF9zdHlsZShncmFkX2YsIHgwLmNvcHkoKSwgbHI9MC4wMDIsIGJldGE9MC44MSwgbl9zdGVwcz0yMDAsIGY9ZilcblxucHJpbnQoZlwiU2luZ2xlLXZhcmlhYmxlIE5BRzogIGZpbmFsIGxvc3MgPSB7bG9zc2VzX3N2Wy0xXTouNmZ9XCIpXG5wcmludChmXCJQeVRvcmNoLXN0eWxlIE5BRzogICAgZmluYWwgbG9zcyA9IHtsb3NzZXNfcHRbLTFdOi42Zn1cIilcbnByaW50KGZcIkJvdGggZm9ybXVsYXRpb25zIG1hdGNoOiB7YWJzKGxvc3Nlc19zdlstMV0gLSBsb3NzZXNfcHRbLTFdKSA8IDFlLTZ9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29udmVyZ2VuY2UgUmF0ZTogTygxL1TCsikgZm9yIENvbnZleCBTbW9vdGggRnVuY3Rpb25zIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTmVzdGVyb3YncyBjb252ZXJnZW5jZSB0aGVvcmVtOiBmb3IgTC1zbW9vdGggY29udmV4IGYsIE5BRyBhY2hpZXZlcyBmKM644oKcKeKIkmYqIOKJpCAyTOKAls644oKA4oiSzrgq4oCWwrIvKHQrMSnCsiA9IE8oMS9UwrIpLiBUaGlzIGlzIGEgZmFjdG9yIG9mIFQgaW1wcm92ZW1lbnQgb3ZlciBHRCdzIE8oMS9UKS4gVGhlIHByb29mIHVzZXMgYSBwb3RlbnRpYWwgKEx5YXB1bm92KSBmdW5jdGlvbiBF4oKcID0gdMKyKGYozrjigpwp4oiSZiopICsgKDEvMinigJYuLi7igJbCsiB0aGF0IGRlY3JlYXNlcyBtb25vdG9uaWNhbGx5IGFsb25nIHRoZSBpdGVyYXRlcy4gVGhlIHNwZWNpZmljIGNob2ljZSBvZiBtb21lbnR1bSBzZXF1ZW5jZSDOsuKCnCAobm90IG5lY2Vzc2FyaWx5IGNvbnN0YW50KSBpcyBkZXJpdmVkIGZyb20gdGhlIGNvbnZlcmdlbmNlIHByb29mOiDOsuKCnCA9ICgx4oiSYeKCnCkvYeKCnOKCiuKCgSB3aGVyZSBh4oKcID0gKDEr4oiaKDErNGHCsuKCnOKCi+KCgSkpLzIsIHdpdGggdGhpcyBzZXF1ZW5jZSBzYXRpc2Z5aW5nIGHigpwg4omIIHQvMiBhc3ltcHRvdGljYWxseS4gRm9yIHN0cm9uZ2x5IGNvbnZleCBwcm9ibGVtczogTkFHIGFjaGlldmVzIGxpbmVhciByYXRlIE8oKDHiiJLiiJoozrwvTCkp4bWAKSDigJQgz4EgPSAx4oiSMS/iiJrOuiB2cyDPgSA9IDHiiJIxL866IGZvciBHRC4gTkFHIG5lZWRzIE8o4oiazropIGl0ZXJhdGlvbnMgdnMgTyjOuikgZm9yIEdELCBhIHNxdWFyZS1yb290IGltcHJvdmVtZW50IGluIHRoZSBjb25kaXRpb24tbnVtYmVyIGRlcGVuZGVuY2UgdGhhdCBpcyBjcml0aWNhbCBmb3IgaGlnaGx5IGlsbC1jb25kaXRpb25lZCBwcm9ibGVtcy4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNTCBDb25uZWN0aW9ucyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIk5lc3Rlcm92IG1vbWVudHVtIGlzIHVzZWQgYWNyb3NzIG11bHRpcGxlIE1MIGZyYW1ld29ya3M6ICgxKSB0b3JjaC5vcHRpbS5TR0Qgd2l0aCBuZXN0ZXJvdj1UcnVlIGlzIHRoZSBkZWZhdWx0IGZvciBtYW55IGltYWdlIGNsYXNzaWZpY2F0aW9uIHRyYWluaW5nIHJlY2lwZXMgaW5jbHVkaW5nIFJlc05ldCBvbiBJbWFnZU5ldDsgKDIpIEFkYW0gdmFyaWFudHMgbGlrZSBOYWRhbSAoRG96YXQgMjAxNikgaW5jb3Jwb3JhdGUgdGhlIE5lc3Rlcm92IGNvcnJlY3Rpb24gaW50byBBZGFtJ3MgdXBkYXRlOiBpbnN0ZWFkIG9mIHVzaW5nIHRoZSBleHBvbmVudGlhbCBtb3ZpbmcgYXZlcmFnZSBt4oKcIGFzIHRoZSB1cGRhdGUgZGlyZWN0aW9uLCBOYWRhbSB1c2VzIGEgYmlhcy1jb3JyZWN0ZWQgZXN0aW1hdGUgb2YgdGhlIG5leHQgZ3JhZGllbnQgbeKCnOKCiuKCgSwgcHJvdmlkaW5nIGEgbG9va2FoZWFkIGNvcnJlY3Rpb24gd2l0aGluIHRoZSBhZGFwdGl2ZSBsZWFybmluZyByYXRlIGZyYW1ld29yay4gKDMpIEluIG1ldGEtbGVhcm5pbmcgKE1BTUwpOiB0aGUgaW5uZXIgbG9vcCB1c2VzIEdEIGZvciB0YXNrIGFkYXB0YXRpb24sIGJ1dCB0aGUgb3V0ZXIgbG9vcCB1cGRhdGUgZGlmZmVyZW50aWF0ZXMgdGhyb3VnaCB0aGUgaW5uZXIgbG9vcCBhbmQgY2FuIHVzZSBOQUcgZm9yIGZhc3RlciBjb252ZXJnZW5jZSBvZiB0aGUgbWV0YS1vYmplY3RpdmUgYWNyb3NzIHRhc2tzLiAoNCkgTC1CRkdTIHVzZXMgYSBxdWFzaS1OZXd0b24gZGlyZWN0aW9uIHRoYXQgaW5jb3Jwb3JhdGVzIGdyYWRpZW50IGhpc3RvcnkgaW4gYSBtYW5uZXIgYW5hbG9nb3VzIHRvIG1vbWVudHVtLCBidXQgd2l0aCBhIHNlY29uZC1vcmRlciBhcHByb3hpbWF0aW9uIG9mIHRoZSBjdXJ2YXR1cmUuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBjb21wYXJlX3NnZF92YXJpYW50cyhuX3N0ZXBzPTUwMCk6XG4gICAgXCJcIlwiXG4gICAgQ29tcGFyZSBTR0QsIFNHRCtNb21lbnR1bSwgYW5kIFNHRCtOZXN0ZXJvdiBvbiBhIHNpbXBsZSByZWdyZXNzaW9uIHRhc2suXG4gICAgXCJcIlwiXG4gICAgdG9yY2gubWFudWFsX3NlZWQoNDIpXG5cbiAgICAjIFN5bnRoZXRpYyByZWdyZXNzaW9uOiA1MCBmZWF0dXJlcywgaWxsLWNvbmRpdGlvbmVkXG4gICAgWCA9IHRvcmNoLnJhbmRuKDIwMCwgNTApXG4gICAgIyBDcmVhdGUgaWxsLWNvbmRpdGlvbmluZyBieSBzY2FsaW5nIGZlYXR1cmVzXG4gICAgc2NhbGUgPSB0b3JjaC5sb2dzcGFjZSgwLCAyLCA1MCkgICMgZmVhdHVyZXMgc2NhbGVkIDF4IHRvIDEwMHhcbiAgICBYID0gWCAqIHNjYWxlLnVuc3F1ZWV6ZSgwKVxuICAgIHdfdHJ1ZSA9IHRvcmNoLnJhbmRuKDUwKVxuICAgIHkgPSBYIEAgd190cnVlICsgMC4xICogdG9yY2gucmFuZG4oMjAwKVxuXG4gICAgZGVmIG1ha2VfbW9kZWwoKTpcbiAgICAgICAgcmV0dXJuIG5uLkxpbmVhcig1MCwgMSwgYmlhcz1GYWxzZSlcblxuICAgIGRlZiBydW4ob3B0X25hbWUsIG9wdGltaXplcik6XG4gICAgICAgIG1vZGVsID0gbWFrZV9tb2RlbCgpXG4gICAgICAgIGNyaXRlcmlvbiA9IG5uLk1TRUxvc3MoKVxuICAgICAgICBsb3NzZXMgPSBbXVxuICAgICAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgICAgICAgICAgbG9zcyA9IGNyaXRlcmlvbihtb2RlbChYKS5zcXVlZXplKCksIHkpXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgICAgIGxvc3Nlcy5hcHBlbmQobG9zcy5pdGVtKCkpXG4gICAgICAgIHJldHVybiBsb3NzZXNcblxuICAgIG1vZGVsX2dkID0gbWFrZV9tb2RlbCgpXG4gICAgbW9kZWxfbW9tID0gbWFrZV9tb2RlbCgpXG4gICAgbW9kZWxfbmFnID0gbWFrZV9tb2RlbCgpXG5cbiAgICBsb3NzZXNfZ2QgPSBydW4oJ0dEJywgdG9yY2gub3B0aW0uU0dEKG1vZGVsX2dkLnBhcmFtZXRlcnMoKSwgbHI9MC4wMDEpKVxuICAgIGxvc3Nlc19tb20gPSBydW4oJ01vbScsIHRvcmNoLm9wdGltLlNHRChtb2RlbF9tb20ucGFyYW1ldGVycygpLCBscj0wLjAwMSwgbW9tZW50dW09MC45KSlcbiAgICBsb3NzZXNfbmFnID0gcnVuKCdOQUcnLCB0b3JjaC5vcHRpbS5TR0QobW9kZWxfbmFnLnBhcmFtZXRlcnMoKSwgbHI9MC4wMDEsIG1vbWVudHVtPTAuOSwgbmVzdGVyb3Y9VHJ1ZSkpXG5cbiAgICBmb3IgbmFtZSwgbG9zc2VzIGluIFsoJ0dEJywgbG9zc2VzX2dkKSwgKCdNb21lbnR1bScsIGxvc3Nlc19tb20pLCAoJ05lc3Rlcm92JywgbG9zc2VzX25hZyldOlxuICAgICAgICBmaW5hbCA9IGxvc3Nlc1stMV1cbiAgICAgICAgc3RlcHNfMXBjdCA9IG5leHQoKGkgZm9yIGksIGwgaW4gZW51bWVyYXRlKGxvc3NlcykgaWYgbCA8IGxvc3Nlc1swXSowLjAxKSwgbl9zdGVwcylcbiAgICAgICAgcHJpbnQoZlwie25hbWU6MTB9OiBmaW5hbF9sb3NzPXtmaW5hbDouNGZ9LCBzdGVwcyB0byAxJSBvZiBpbml0aWFsOiB7c3RlcHNfMXBjdH1cIilcblxuY29tcGFyZV9zZ2RfdmFyaWFudHMoKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk5BRyB2cyBDbGFzc2ljYWwgTW9tZW50dW06IEdlb21ldHJpYyBJbnR1aXRpb24ifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgZ2VvbWV0cmljIGRpZmZlcmVuY2UgYmV0d2VlbiB0aGUgdHdvIG1ldGhvZHMgaXMgc3VidGxlIGJ1dCBjb25zZXF1ZW50aWFsLiBIZWF2eSBiYWxsIGNvbXB1dGVzIHRoZSBncmFkaWVudCBhdCB0aGUgY3VycmVudCBwb3NpdGlvbiDOuOKCnCwgdGhlbiBhcHBsaWVzIHRoZSBncmFkaWVudCB0byB1cGRhdGUgdGhlIHZlbG9jaXR5LCBhbmQgZmluYWxseSBtb3Zlcy4gVGhlIG1vbWVudHVtIGNhcnJpZXMgdGhlIG9wdGltaXplciB0byBhIG5ldyBwb3NpdGlvbiDOuOKCnOKCiuKCgS4gSWYgdGhlIGdyYWRpZW50IGF0IM644oKc4oKK4oKBIHdvdWxkIGJlIHplcm8gKHdlIGFyZSBhdCB0aGUgbWluaW11bSksIGhlYXZ5IGJhbGwgc3RpbGwgb3ZlcnNob290cyBiZWNhdXNlIHRoZSB2ZWxvY2l0eSB0ZXJtIGNhcnJpZXMgaXQgcGFzdC4gTkFHIGNvbXB1dGVzIHRoZSBncmFkaWVudCBhdCB0aGUgYW50aWNpcGF0ZWQgcG9zaXRpb24gzrjigpwg4oiSIM6yduKCnOKCi+KCgSwgcmVjZWl2aW5nIGVhcmx5IHdhcm5pbmcgYWJvdXQgdGhlIGdyYWRpZW50IGluIHRoZSBkaXJlY3Rpb24gb2YgdHJhdmVsLiBJZiB0aGUgZ3JhZGllbnQgYXQgdGhlIGxvb2thaGVhZCBpcyBkZWNlbGVyYXRpbmcgKG9wcG9zaW5nIHRoZSB2ZWxvY2l0eSksIE5BRyByZWR1Y2VzIHRoZSBzdGVwIGJlZm9yZSBvdmVyc2hvb3RpbmcsIHdoaWxlIGhlYXZ5IGJhbGwgb25seSByZWFjdHMgYXQgdGhlIG5leHQgc3RlcC4gVGhpcyBjb3JyZWN0aW9uIGlzIGVzcGVjaWFsbHkgaW1wb3J0YW50IG5lYXIgdGhlIG1pbmltdW0gd2hlcmUgdGhlIGxvc3MgZnVuY3Rpb24gaXMgc3Ryb25nbHkgY3VydmVkIGFuZCB0aGUgY29zdCBvZiBvdmVyc2hvb3QgY29tcG91bmRzIGFjcm9zcyBtYW55IGl0ZXJhdGlvbnMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiSW1wbGVtZW50YXRpb24gUGl0ZmFsbHMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgbW9zdCBjb21tb24gTkFHIHBpdGZhbGw6IGNvbmZ1c2luZyB0aGUgbG9va2FoZWFkIGZvcm11bGF0aW9uIHdpdGggdGhlIHNpbmdsZS12YXJpYWJsZSBmb3JtdWxhdGlvbiBhbmQgaW1wbGVtZW50aW5nIG5laXRoZXIgY29ycmVjdGx5LiBQeVRvcmNoJ3MgU0dEIHdpdGggbmVzdGVyb3Y9VHJ1ZSB1c2VzIHRoZSBidWYgZm9ybXVsYXRpb246IGNvbXB1dGVzIGJ1ZiA9IM6ywrdidWYgKyBnLCB0aGVuIHVwZGF0ZXMgzrggd2l0aCB0aGUgTmVzdGVyb3YtY29ycmVjdGVkIGdyYWRpZW50IGcgKyDOssK3YnVmLiBUaGlzIGlzIG1hdGhlbWF0aWNhbGx5IGVxdWl2YWxlbnQgdG8gdGhlIGxvb2thaGVhZCBmb3JtIGJ1dCByZXF1aXJlcyBvbmx5IG9uZSBncmFkaWVudCBldmFsdWF0aW9uLiBDb21tb24gcGl0ZmFsbDogdXNpbmcgbmVzdGVyb3Y9VHJ1ZSB3aXRob3V0IG1vbWVudHVtICjOsj0wKSBzaW1wbHkgcmVjb3ZlcnMgdmFuaWxsYSBHRCDigJQgTmVzdGVyb3YgcmVxdWlyZXMgzrIgPiAwIHRvIHByb3ZpZGUgYW55IGJlbmVmaXQuIFNlY29uZCBwaXRmYWxsOiBhcHBseWluZyBncmFkaWVudCBjbGlwcGluZyBpbmNvcnJlY3RseSB3aXRoIE5BRy4gQ2xpcCB0aGUgTmVzdGVyb3YtY29ycmVjdGVkIGdyYWRpZW50IGdfbmVzdGVyb3YgPSBnICsgzrLCt2J1Ziwgbm90IHRoZSByYXcgZ3JhZGllbnQgZyBhbG9uZSwgdG8gbWFpbnRhaW4gdGhlIGNvcnJlY3QgZWZmZWN0aXZlIHVwZGF0ZSBtYWduaXR1ZGUuIENsaXBwaW5nIG9ubHkgdGhlIHJhdyBncmFkaWVudCB1bmRlcmVzdGltYXRlcyB0aGUgdHJ1ZSB1cGRhdGUgc2l6ZSBieSBhIGZhY3RvciBvZiBhcHByb3hpbWF0ZWx5IDEvKDHiiJLOsikuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUHJhY3RpY2FsIEd1aWRhbmNlIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVXNlIG5lc3Rlcm92PVRydWUgd2hlbmV2ZXIgdXNpbmcgU0dEIHdpdGggbW9tZW50dW0g4oCUIGl0IGlzIHN0cmljdGx5IGJldHRlciBpbiB0aGVvcnkgYW5kIGVtcGlyaWNhbGx5IG1hdGNoZXMgb3IgZXhjZWVkcyBoZWF2eSBiYWxsIG9uIG1vc3QgdGFza3MgYXQgemVybyBhZGRpdGlvbmFsIGNvbXB1dGF0aW9uYWwgY29zdC4gU3RhbmRhcmQgcmVjaXBlIGZvciBpbWFnZSBjbGFzc2lmaWNhdGlvbjogU0dEIHdpdGggbW9tZW50dW09MC45LCBuZXN0ZXJvdj1UcnVlLCBMUiBzdGFydGluZyBhdCAwLjEgd2l0aCBjb3NpbmUgZGVjYXkgb3ZlciA5MC0yMDAgZXBvY2hzLCB3ZWlnaHQgZGVjYXkgMWUtNC4gRm9yIEFkYW0tYmFzZWQgdHJhaW5pbmcgd2hlcmUgTmVzdGVyb3YgY29ycmVjdGlvbiBpcyBkZXNpcmVkLCB1c2UgTmFkYW0gKGF2YWlsYWJsZSBpbiBUZW5zb3JGbG93IG5hdGl2ZWx5OyBpbiBQeVRvcmNoIGltcGxlbWVudCB2aWEgdGhlIGV4cGxpY2l0IE5lc3Rlcm92LWNvcnJlY3RlZCBBZGFtIHVwZGF0ZSBydWxlKS4gTW9uaXRvciBjb252ZXJnZW5jZTogTkFHIHNob3VsZCByZWFjaCBsb3dlciBsb3NzIGluIGZld2VyIHN0ZXBzIHRoYW4gaGVhdnkgYmFsbCBvbiB0aGUgc2FtZSBMUiBhbmQgYmV0YSBzZXR0aW5ncyBmb3IgY29udmV4IG9yIG5lYXJseS1jb252ZXggcHJvYmxlbXMuIElmIGhlYXZ5IGJhbGwgb3V0cGVyZm9ybXMgTkFHLCB0aGUgbG9zcyBsYW5kc2NhcGUgaXMgc3Ryb25nbHkgbm9uLWNvbnZleCBhbmQgdGhlIHRoZW9yZXRpY2FsIGd1YXJhbnRlZXMgZm9yIE5BRyBkbyBub3QgYXBwbHkgZGlyZWN0bHkgdG8gdGhlIGN1cnJlbnQgcHJvYmxlbS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG5lc3Rlcm92X2NvbnZlcmdlbmNlX3JhdGVfcGxvdChuX3N0ZXBzPTMwMCk6XG4gICAgXCJcIlwiRW1waXJpY2FsbHkgdmVyaWZ5IE8oMS9UXjIpIHZzIE8oMS9UKSBjb252ZXJnZW5jZSByYXRlcy5cIlwiXCJcblxuICAgICMgUHVyZSBxdWFkcmF0aWM6IGYodGhldGEpID0gMC41ICogdGhldGFeVCAqIEEgKiB0aGV0YVxuICAgICMgTCA9IDEwLCBtdSA9IDEgKGNvbmRpdGlvbiBudW1iZXIgMTApXG4gICAgQSA9IHRvcmNoLmRpYWcodG9yY2gudGVuc29yKFsxLjAsIDIuMCwgNC4wLCA2LjAsIDguMCwgMTAuMF0pKVxuICAgIGYgPSBsYW1iZGEgdGhldGE6IDAuNSAqIHRoZXRhIEAgQSBAIHRoZXRhXG4gICAgZ3JhZF9mID0gbGFtYmRhIHRoZXRhOiBBIEAgdGhldGFcblxuICAgIHRoZXRhMCA9IHRvcmNoLm9uZXMoNikgKiA1LjBcbiAgICBMLCBtdSA9IDEwLjAsIDEuMFxuICAgIGV0YV9nZCA9IDEuMCAvIExcbiAgICBldGFfbmFnID0gMS4wIC8gTFxuICAgIGJldGFfbmFnID0gKG5wLnNxcnQoTCkgLSBucC5zcXJ0KG11KSkgLyAobnAuc3FydChMKSArIG5wLnNxcnQobXUpKVxuXG4gICAgIyBSdW4gR0QgYW5kIE5BR1xuICAgIHRoZXRhX2dkID0gdGhldGEwLmNsb25lKClcbiAgICBwaGlfcHJldiA9IHRoZXRhMC5jbG9uZSgpXG4gICAgcGhpID0gdGhldGEwLmNsb25lKClcblxuICAgIGxvc3Nlc19nZCwgbG9zc2VzX25hZyA9IFtdLCBbXVxuICAgIGZvciB0IGluIHJhbmdlKG5fc3RlcHMpOlxuICAgICAgICBsb3NzZXNfZ2QuYXBwZW5kKGYodGhldGFfZ2QpLml0ZW0oKSlcbiAgICAgICAgbG9zc2VzX25hZy5hcHBlbmQoZihwaGkpLml0ZW0oKSlcblxuICAgICAgICB0aGV0YV9nZCA9IHRoZXRhX2dkIC0gZXRhX2dkICogZ3JhZF9mKHRoZXRhX2dkKVxuICAgICAgICBwaGlfbmV3ID0gcGhpICsgYmV0YV9uYWcgKiAocGhpIC0gcGhpX3ByZXYpIC0gZXRhX25hZyAqIGdyYWRfZihwaGkpXG4gICAgICAgIHBoaV9wcmV2LCBwaGkgPSBwaGksIHBoaV9uZXdcblxuICAgICMgQ2hlY2sgcmF0ZXM6IEdEIHNob3VsZCBmb2xsb3cgMS9ULCBOQUcgc2hvdWxkIGZvbGxvdyAxL1ReMlxuICAgIHQgPSBucC5hcmFuZ2UoMSwgbl9zdGVwcyArIDEsIGR0eXBlPWZsb2F0KVxuICAgIGNvcnJfZ2QgPSBucC5jb3JyY29lZihucC5sb2codCksIG5wLmxvZyhucC5tYXhpbXVtKGxvc3Nlc19nZCwgMWUtMTIpKSlbMCwgMV1cbiAgICBjb3JyX25hZyA9IG5wLmNvcnJjb2VmKG5wLmxvZyh0KioyKSwgbnAubG9nKG5wLm1heGltdW0obG9zc2VzX25hZywgMWUtMTIpKSlbMCwgMV1cbiAgICBwcmludChmXCJHRCBsb2ctbG9nIGNvcnJlbGF0aW9uIHdpdGggMS9UOiAgIHtjb3JyX2dkOi4zZn0gKGV4cGVjdCB+LTEgZm9yIE8oMS9UKSlcIilcbiAgICBwcmludChmXCJOQUcgbG9nLWxvZyBjb3JyZWxhdGlvbiB3aXRoIDEvVF4yOiB7Y29ycl9uYWc6LjNmfSAoZXhwZWN0IH4tMSBmb3IgTygxL1ReMikpXCIpXG5cbm5lc3Rlcm92X2NvbnZlcmdlbmNlX3JhdGVfcGxvdCgpIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInRpdGxlIjogIk5BRyBHdWFyYW50ZWVzIEFwcGx5IE9ubHkgdG8gQ29udmV4IEZ1bmN0aW9ucyIsICJjb250ZW50IjogIk5lc3Rlcm92J3MgTygxL1ReMikgY29udmVyZ2VuY2UgdGhlb3JlbSByZXF1aXJlcyBjb252ZXhpdHkuIEZvciBub24tY29udmV4IGZ1bmN0aW9ucyAobmV1cmFsIG5ldHdvcmtzKSwgTkFHIGhhcyBubyB0aGVvcmV0aWNhbCBndWFyYW50ZWUgb3ZlciBoZWF2eSBiYWxsIOKAlCBib3RoIGNvbnZlcmdlIHRvIHN0YXRpb25hcnkgcG9pbnRzIGF0IE8oMS9UKSByYXRlIGluIHRlcm1zIG9mIHx8Z3JhZChmKXx8XjIuIEluIHByYWN0aWNlLCBOZXN0ZXJvdiBvZnRlbiBwZXJmb3JtcyBzaW1pbGFybHkgdG8gb3Igc2xpZ2h0bHkgYmV0dGVyIHRoYW4gaGVhdnkgYmFsbCBmb3IgbmV1cmFsIG5ldHdvcmtzLCB3aGljaCBpcyB3aHkgUHlUb3JjaCBpbmNsdWRlcyBuZXN0ZXJvdj1UcnVlIGFzIGFuIG9wdGlvbi4gQnV0IGlmIHlvdSBzZWUgaGVhdnkgYmFsbCBvdXRwZXJmb3JtaW5nIE5BRyBvbiBhIHNwZWNpZmljIHRhc2ssIHRoaXMgaXMgY29uc2lzdGVudCB3aXRoIHRoZW9yeSDigJQgTkFHJ3MgYWR2YW50YWdlIGlzIHByb3ZhYmx5IHJlc3RyaWN0ZWQgdG8gdGhlIGNvbnZleCBjYXNlLiJ9LCB7InR5cGUiOiAidGFibGUiLCAiaGVhZGVycyI6IFsiTWV0aG9kIiwgIkdyYWRpZW50IEV2YWwiLCAiQ29udmV4IFJhdGUiLCAiU3Ryb25nbHkgQ29udmV4IFJhdGUiLCAiUHlUb3JjaCJdLCAicm93cyI6IFtbIkdEIiwgImF0IHRoZXRhX3QiLCAiTygxL1QpIiwgIk8oKDEtbXUvTCleVCkiLCAiU0dEKG1vbWVudHVtPTApIl0sIFsiSGVhdnkgYmFsbCIsICJhdCB0aGV0YV90IiwgIk8oMS9UXjIpIHF1YWRyYXRpYyBvbmx5IiwgIk8oKDEtc3FydChtdS9MKSleVCkgcXVhZHJhdGljIiwgIlNHRChtb21lbnR1bT1iZXRhKSJdLCBbIk5lc3Rlcm92IChOQUcpIiwgImF0IHRoZXRhX3QgLSBiZXRhKnZfe3QtMX0iLCAiTygxL1ReMikgZ2VuZXJhbCIsICJPKCgxLXNxcnQobXUvTCkpXlQpIiwgIlNHRChtb21lbnR1bT1iZXRhLCBuZXN0ZXJvdj1UcnVlKSJdLCBbIk5hZGFtIiwgImF0IHBoaV90IChBZGFtK05BRykiLCAiTi9BIChhZGFwdGl2ZSkiLCAiTi9BIiwgIk5vdCBpbiBQeVRvcmNoIG5hdGl2ZWx5Il0sIFsiTC1CRkdTIiwgImF0IHRoZXRhX3QgKGxpbmUgc2VhcmNoKSIsICJTdXBlcmxpbmVhciIsICJRdWFkcmF0aWMiLCAiTEJGR1Mgb3B0aW1pemVyIl1dfSwgeyJ0eXBlIjogImRpdmlkZXIifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJLZXkgVGFrZWF3YXlzIn0sIHsidHlwZSI6ICJsaXN0IiwgIml0ZW1zIjogWyJOQUcgZXZhbHVhdGVzIGdyYWRpZW50IGF0IHRoZSBsb29rYWhlYWQgcG9zaXRpb24gdGhldGFfdCAtIGJldGEqdl97dC0xfSwgZ2l2aW5nIGVhcmx5IHdhcm5pbmcgYWJvdXQgdGhlIGdyYWRpZW50IGF0IHRoZSBkZXN0aW5hdGlvbiBhbmQgcHJldmVudGluZyBvdmVyc2hvb3QuIiwgIkNvbnZlcmdlbmNlOiBOQUcgYWNoaWV2ZXMgTygxL1ReMikgZm9yIGNvbnZleCBzbW9vdGggZnVuY3Rpb25zIHZzIE8oMS9UKSBmb3IgR0QuIEZvciBzdHJvbmdseSBjb252ZXg6IE8oZXhwKC1UKnNxcnQobXUvTCkpKSB2cyBPKGV4cCgtVCptdS9MKSkg4oCUIHNxdWFyZS1yb290IGltcHJvdmVtZW50IGluIGNvbmRpdGlvbiBudW1iZXIgZGVwZW5kZW5jZS4iLCAiVGhlIHNpbmdsZS12YXJpYWJsZSBmb3JtIHBoaV97dCsxfSA9IHBoaV90ICsgYmV0YSoocGhpX3QgLSBwaGlfe3QtMX0pIC0gZXRhKmdyYWQoZikocGhpX3QpIHJlcXVpcmVzIG9ubHkgb25lIGdyYWRpZW50IGV2YWx1YXRpb24gcGVyIHN0ZXAuIiwgIlB5VG9yY2ggaW1wbGVtZW50cyBOQUcgYXM6IGJ1ZiA9IGJldGEqYnVmICsgZywgdGhlbiBzdGVwIHdpdGggZyArIGJldGEqYnVmIChOZXN0ZXJvdi1jb3JyZWN0ZWQgZ3JhZGllbnQpLiBUaGlzIGlzIGVxdWl2YWxlbnQgdG8gdGhlIGxvb2thaGVhZCBmb3JtdWxhdGlvbi4iLCAiRm9yIG5vbi1jb252ZXggbmV1cmFsIG5ldHdvcmtzLCBOQUcgb2ZmZXJzIG5vIHRoZW9yZXRpY2FsIGd1YXJhbnRlZSBvdmVyIGhlYXZ5IGJhbGwgYnV0IG9mdGVuIG1hdGNoZXMgb3Igc2xpZ2h0bHkgZXhjZWVkcyBpdCBlbXBpcmljYWxseS4iLCAiQWx3YXlzIHVzZSBuZXN0ZXJvdj1UcnVlIHdoZW4gdXNpbmcgU0dEIHdpdGggbW9tZW50dW0gaW4gUHlUb3JjaCDigJQgaXQgaXMgc3RyaWN0bHkgYmV0dGVyIGZvciBjb252ZXggb2JqZWN0aXZlcyBhbmQgY29zdHMgbm90aGluZyBleHRyYS4iLCAiQ2xpcCBncmFkaWVudHMgdXNpbmcgdGhlIE5lc3Rlcm92LWNvcnJlY3RlZCBncmFkaWVudCBnICsgYmV0YSpidWYsIG5vdCB0aGUgcmF3IGdyYWRpZW50IGcsIHRvIG1haW50YWluIGNvcnJlY3QgdXBkYXRlIG1hZ25pdHVkZS4iXX1d"
---

# Nesterov Accelerated Gradient (NAG)

Nesterov Accelerated Gradient is the theoretically optimal first-order method for convex smooth optimization, achieving the O(1/T²) convergence rate that matches information-theoretic lower bounds for this function class. The key insight — evaluate the gradient at the anticipated future position (θ − βv) rather than the current position θ — produces a correction that dramatically reduces overshoot and achieves optimal convergence. Beyond its theoretical elegance, NAG is practically important: PyTorch's SGD with nesterov=True uses it; the Nesterov-style momentum correction also appears in Adam-based variants like Nadam. Understanding NAG's convergence proof (via potential functions and energy arguments) reveals why the specific update order matters and why the lookahead gradient provides strictly more information than the current-position gradient.

## Core Definition: The Lookahead Correction

Heavy ball (classical momentum): vₜ = βvₜ₋₁ + ηg(θₜ); θₜ₊₁ = θₜ − vₜ. Nesterov's correction: evaluate the gradient at the anticipated position θₜ − βvₜ₋₁ (where we will land after applying the current velocity) rather than at θₜ itself. Update: vₜ = βvₜ₋₁ + η∇f(θₜ − βvₜ₋₁); θₜ₊₁ = θₜ − vₜ. The lookahead position θₜ − βvₜ₋₁ is a first-order prediction of where θₜ₊₁ would land with the current velocity alone. Evaluating the gradient there instead of at θₜ provides a correction that accounts for momentum: if the gradient at the lookahead position opposes the velocity, NAG brakes early, preventing overshoot. This lookahead correction is why NAG achieves O(1/T²) for general convex functions, while heavy ball only achieves O(1/T²) for quadratics specifically.

```python
import numpy as np

def nesterov_ag(grad_f, theta0, lr, beta, n_steps, f=None):
    """
    Nesterov Accelerated Gradient.
    Evaluates gradient at look-ahead position: theta - beta * v.
    """
    theta = np.array(theta0, dtype=np.float64)
    v = np.zeros_like(theta)
    losses = [f(theta)] if f else []

    for t in range(n_steps):
        # Key difference from heavy ball: gradient at lookahead position
        lookahead = theta - beta * v
        g = grad_f(lookahead)
        v = beta * v + lr * g
        theta = theta - v
        if f: losses.append(f(theta))

    return losses

def heavy_ball(grad_f, theta0, lr, beta, n_steps, f=None):
    """Classical momentum (heavy ball): gradient at current position."""
    theta = np.array(theta0, dtype=np.float64)
    v = np.zeros_like(theta)
    losses = [f(theta)] if f else []

    for t in range(n_steps):
        g = grad_f(theta)  # gradient at current position (not lookahead)
        v = beta * v + lr * g
        theta = theta - v
        if f: losses.append(f(theta))

    return losses

# Compare on ill-conditioned quadratic: f(x,y) = 0.5*(x^2 + 100*y^2)
f = lambda x: 0.5 * (x[0]**2 + 100*x[1]**2)
grad_f = lambda x: np.array([x[0], 100*x[1]])
x0 = np.array([10.0, 1.0])

L, mu = 100.0, 1.0
beta_opt = (np.sqrt(L) - np.sqrt(mu)) / (np.sqrt(L) + np.sqrt(mu))
lr_opt = (1 / (np.sqrt(L) + np.sqrt(mu)))**2 * 4  # approx optimal for NAG

losses_nag = nesterov_ag(grad_f, x0, lr=lr_opt, beta=beta_opt, n_steps=200, f=f)
losses_hb = heavy_ball(grad_f, x0, lr=lr_opt, beta=beta_opt, n_steps=200, f=f)

def steps_to(losses, threshold=1e-4):
    return next((i for i, l in enumerate(losses) if l < threshold), len(losses))

print(f"beta_opt = {beta_opt:.4f}")
print(f"NAG: {steps_to(losses_nag)} steps to 1e-4")
print(f"Heavy ball: {steps_to(losses_hb)} steps to 1e-4")
```

## Variable Substitution: The Efficient Implementation

Naively implementing NAG requires computing the gradient at two points per step (θₜ and θₜ − βvₜ₋₁). The variable substitution φₜ = θₜ − βvₜ₋₁ (define the lookahead position as a new variable) eliminates this overhead. In terms of φₜ, after algebraic manipulation of the original update equations, the update simplifies to: φₜ₊₁ = φₜ + β(φₜ − φₜ₋₁) − η∇f(φₜ). In this form, the gradient is always evaluated at φₜ (the current point), and the momentum term is the displacement φₜ − φₜ₋₁ from the previous step. This requires only one gradient evaluation per step — the same cost as vanilla GD or heavy ball. PyTorch's SGD with nesterov=True uses this equivalent single-variable form internally, storing a momentum buffer buf and computing the Nesterov-corrected gradient as g + β·buf.

```python
import numpy as np

def nesterov_single_variable(grad_f, phi0, lr, beta, n_steps, f=None):
    """
    NAG using the phi-variable substitution.
    phi_{t+1} = phi_t + beta*(phi_t - phi_{t-1}) - eta*grad(f)(phi_t)
    Only ONE gradient evaluation per step (at current phi).
    Mathematically equivalent to the lookahead formulation.
    """
    phi = np.array(phi0, dtype=np.float64)
    phi_prev = phi.copy()
    losses = [f(phi)] if f else []

    for t in range(n_steps):
        g = grad_f(phi)
        phi_new = phi + beta * (phi - phi_prev) - lr * g
        phi_prev = phi
        phi = phi_new
        if f: losses.append(f(phi))

    return losses

def nesterov_pytorch_style(grad_f, theta0, lr, beta, n_steps, f=None):
    """
    PyTorch's SGD nesterov=True implementation.
    Stores buf (momentum buffer) and updates with Nesterov correction.
    """
    theta = np.array(theta0, dtype=np.float64)
    buf = np.zeros_like(theta)
    losses = [f(theta)] if f else []

    for t in range(n_steps):
        g = grad_f(theta)
        buf = beta * buf + g                    # momentum buffer
        # Nesterov: add beta * buf to gradient before stepping
        g_nesterov = g + beta * buf
        theta = theta - lr * g_nesterov
        if f: losses.append(f(theta))

    return losses

# Verify both formulations give same convergence
f = lambda x: 0.5 * (x[0]**2 + 100*x[1]**2)
grad_f = lambda x: np.array([x[0], 100*x[1]])
x0 = np.array([10.0, 1.0])

losses_sv = nesterov_single_variable(grad_f, x0.copy(), lr=0.002, beta=0.81, n_steps=200, f=f)
losses_pt = nesterov_pytorch_style(grad_f, x0.copy(), lr=0.002, beta=0.81, n_steps=200, f=f)

print(f"Single-variable NAG:  final loss = {losses_sv[-1]:.6f}")
print(f"PyTorch-style NAG:    final loss = {losses_pt[-1]:.6f}")
print(f"Both formulations match: {abs(losses_sv[-1] - losses_pt[-1]) < 1e-6}")
```

## Convergence Rate: O(1/T²) for Convex Smooth Functions

Nesterov's convergence theorem: for L-smooth convex f, NAG achieves f(θₜ)−f* ≤ 2L‖θ₀−θ*‖²/(t+1)² = O(1/T²). This is a factor of T improvement over GD's O(1/T). The proof uses a potential (Lyapunov) function Eₜ = t²(f(θₜ)−f*) + (1/2)‖...‖² that decreases monotonically along the iterates. The specific choice of momentum sequence βₜ (not necessarily constant) is derived from the convergence proof: βₜ = (1−aₜ)/aₜ₊₁ where aₜ = (1+√(1+4a²ₜ₋₁))/2, with this sequence satisfying aₜ ≈ t/2 asymptotically. For strongly convex problems: NAG achieves linear rate O((1−√(μ/L))ᵀ) — ρ = 1−1/√κ vs ρ = 1−1/κ for GD. NAG needs O(√κ) iterations vs O(κ) for GD, a square-root improvement in the condition-number dependence that is critical for highly ill-conditioned problems.

## ML Connections

Nesterov momentum is used across multiple ML frameworks: (1) torch.optim.SGD with nesterov=True is the default for many image classification training recipes including ResNet on ImageNet; (2) Adam variants like Nadam (Dozat 2016) incorporate the Nesterov correction into Adam's update: instead of using the exponential moving average mₜ as the update direction, Nadam uses a bias-corrected estimate of the next gradient mₜ₊₁, providing a lookahead correction within the adaptive learning rate framework. (3) In meta-learning (MAML): the inner loop uses GD for task adaptation, but the outer loop update differentiates through the inner loop and can use NAG for faster convergence of the meta-objective across tasks. (4) L-BFGS uses a quasi-Newton direction that incorporates gradient history in a manner analogous to momentum, but with a second-order approximation of the curvature.

```python
import torch
import torch.nn as nn

def compare_sgd_variants(n_steps=500):
    """
    Compare SGD, SGD+Momentum, and SGD+Nesterov on a simple regression task.
    """
    torch.manual_seed(42)

    # Synthetic regression: 50 features, ill-conditioned
    X = torch.randn(200, 50)
    # Create ill-conditioning by scaling features
    scale = torch.logspace(0, 2, 50)  # features scaled 1x to 100x
    X = X * scale.unsqueeze(0)
    w_true = torch.randn(50)
    y = X @ w_true + 0.1 * torch.randn(200)

    def make_model():
        return nn.Linear(50, 1, bias=False)

    def run(opt_name, optimizer):
        model = make_model()
        criterion = nn.MSELoss()
        losses = []
        for step in range(n_steps):
            optimizer.zero_grad()
            loss = criterion(model(X).squeeze(), y)
            loss.backward()
            optimizer.step()
            losses.append(loss.item())
        return losses

    model_gd = make_model()
    model_mom = make_model()
    model_nag = make_model()

    losses_gd = run('GD', torch.optim.SGD(model_gd.parameters(), lr=0.001))
    losses_mom = run('Mom', torch.optim.SGD(model_mom.parameters(), lr=0.001, momentum=0.9))
    losses_nag = run('NAG', torch.optim.SGD(model_nag.parameters(), lr=0.001, momentum=0.9, nesterov=True))

    for name, losses in [('GD', losses_gd), ('Momentum', losses_mom), ('Nesterov', losses_nag)]:
        final = losses[-1]
        steps_1pct = next((i for i, l in enumerate(losses) if l < losses[0]*0.01), n_steps)
        print(f"{name:10}: final_loss={final:.4f}, steps to 1% of initial: {steps_1pct}")

compare_sgd_variants()
```

## NAG vs Classical Momentum: Geometric Intuition

The geometric difference between the two methods is subtle but consequential. Heavy ball computes the gradient at the current position θₜ, then applies the gradient to update the velocity, and finally moves. The momentum carries the optimizer to a new position θₜ₊₁. If the gradient at θₜ₊₁ would be zero (we are at the minimum), heavy ball still overshoots because the velocity term carries it past. NAG computes the gradient at the anticipated position θₜ − βvₜ₋₁, receiving early warning about the gradient in the direction of travel. If the gradient at the lookahead is decelerating (opposing the velocity), NAG reduces the step before overshooting, while heavy ball only reacts at the next step. This correction is especially important near the minimum where the loss function is strongly curved and the cost of overshoot compounds across many iterations.

## Implementation Pitfalls

The most common NAG pitfall: confusing the lookahead formulation with the single-variable formulation and implementing neither correctly. PyTorch's SGD with nesterov=True uses the buf formulation: computes buf = β·buf + g, then updates θ with the Nesterov-corrected gradient g + β·buf. This is mathematically equivalent to the lookahead form but requires only one gradient evaluation. Common pitfall: using nesterov=True without momentum (β=0) simply recovers vanilla GD — Nesterov requires β > 0 to provide any benefit. Second pitfall: applying gradient clipping incorrectly with NAG. Clip the Nesterov-corrected gradient g_nesterov = g + β·buf, not the raw gradient g alone, to maintain the correct effective update magnitude. Clipping only the raw gradient underestimates the true update size by a factor of approximately 1/(1−β).

## Practical Guidance

Use nesterov=True whenever using SGD with momentum — it is strictly better in theory and empirically matches or exceeds heavy ball on most tasks at zero additional computational cost. Standard recipe for image classification: SGD with momentum=0.9, nesterov=True, LR starting at 0.1 with cosine decay over 90-200 epochs, weight decay 1e-4. For Adam-based training where Nesterov correction is desired, use Nadam (available in TensorFlow natively; in PyTorch implement via the explicit Nesterov-corrected Adam update rule). Monitor convergence: NAG should reach lower loss in fewer steps than heavy ball on the same LR and beta settings for convex or nearly-convex problems. If heavy ball outperforms NAG, the loss landscape is strongly non-convex and the theoretical guarantees for NAG do not apply directly to the current problem.

```python
import torch
import numpy as np

def nesterov_convergence_rate_plot(n_steps=300):
    """Empirically verify O(1/T^2) vs O(1/T) convergence rates."""

    # Pure quadratic: f(theta) = 0.5 * theta^T * A * theta
    # L = 10, mu = 1 (condition number 10)
    A = torch.diag(torch.tensor([1.0, 2.0, 4.0, 6.0, 8.0, 10.0]))
    f = lambda theta: 0.5 * theta @ A @ theta
    grad_f = lambda theta: A @ theta

    theta0 = torch.ones(6) * 5.0
    L, mu = 10.0, 1.0
    eta_gd = 1.0 / L
    eta_nag = 1.0 / L
    beta_nag = (np.sqrt(L) - np.sqrt(mu)) / (np.sqrt(L) + np.sqrt(mu))

    # Run GD and NAG
    theta_gd = theta0.clone()
    phi_prev = theta0.clone()
    phi = theta0.clone()

    losses_gd, losses_nag = [], []
    for t in range(n_steps):
        losses_gd.append(f(theta_gd).item())
        losses_nag.append(f(phi).item())

        theta_gd = theta_gd - eta_gd * grad_f(theta_gd)
        phi_new = phi + beta_nag * (phi - phi_prev) - eta_nag * grad_f(phi)
        phi_prev, phi = phi, phi_new

    # Check rates: GD should follow 1/T, NAG should follow 1/T^2
    t = np.arange(1, n_steps + 1, dtype=float)
    corr_gd = np.corrcoef(np.log(t), np.log(np.maximum(losses_gd, 1e-12)))[0, 1]
    corr_nag = np.corrcoef(np.log(t**2), np.log(np.maximum(losses_nag, 1e-12)))[0, 1]
    print(f"GD log-log correlation with 1/T:   {corr_gd:.3f} (expect ~-1 for O(1/T))")
    print(f"NAG log-log correlation with 1/T^2: {corr_nag:.3f} (expect ~-1 for O(1/T^2))")

nesterov_convergence_rate_plot()
```

> **NAG Guarantees Apply Only to Convex Functions**: Nesterov's O(1/T^2) convergence theorem requires convexity. For non-convex functions (neural networks), NAG has no theoretical guarantee over heavy ball — both converge to stationary points at O(1/T) rate in terms of ||grad(f)||^2. In practice, Nesterov often performs similarly to or slightly better than heavy ball for neural networks, which is why PyTorch includes nesterov=True as an option. But if you see heavy ball outperforming NAG on a specific task, this is consistent with theory — NAG's advantage is provably restricted to the convex case.

| Method | Gradient Eval | Convex Rate | Strongly Convex Rate | PyTorch |
|---|---|---|---|---|
| GD | at theta_t | O(1/T) | O((1-mu/L)^T) | SGD(momentum=0) |
| Heavy ball | at theta_t | O(1/T^2) quadratic only | O((1-sqrt(mu/L))^T) quadratic | SGD(momentum=beta) |
| Nesterov (NAG) | at theta_t - beta*v_{t-1} | O(1/T^2) general | O((1-sqrt(mu/L))^T) | SGD(momentum=beta, nesterov=True) |
| Nadam | at phi_t (Adam+NAG) | N/A (adaptive) | N/A | Not in PyTorch natively |
| L-BFGS | at theta_t (line search) | Superlinear | Quadratic | LBFGS optimizer |

---

## Key Takeaways

- NAG evaluates gradient at the lookahead position theta_t - beta*v_{t-1}, giving early warning about the gradient at the destination and preventing overshoot.
- Convergence: NAG achieves O(1/T^2) for convex smooth functions vs O(1/T) for GD. For strongly convex: O(exp(-T*sqrt(mu/L))) vs O(exp(-T*mu/L)) — square-root improvement in condition number dependence.
- The single-variable form phi_{t+1} = phi_t + beta*(phi_t - phi_{t-1}) - eta*grad(f)(phi_t) requires only one gradient evaluation per step.
- PyTorch implements NAG as: buf = beta*buf + g, then step with g + beta*buf (Nesterov-corrected gradient). This is equivalent to the lookahead formulation.
- For non-convex neural networks, NAG offers no theoretical guarantee over heavy ball but often matches or slightly exceeds it empirically.
- Always use nesterov=True when using SGD with momentum in PyTorch — it is strictly better for convex objectives and costs nothing extra.
- Clip gradients using the Nesterov-corrected gradient g + beta*buf, not the raw gradient g, to maintain correct update magnitude.

