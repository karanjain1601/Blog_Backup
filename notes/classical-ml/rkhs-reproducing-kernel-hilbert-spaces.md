---
title: "Reproducing Kernel Hilbert Spaces (RKHS)"
slug: "rkhs-reproducing-kernel-hilbert-spaces"
description: "A complete guide to Reproducing Kernel Hilbert Spaces — the mathematical foundation of kernel methods. Covers the reproducing property, Mercer's theorem, the representer theorem, and how the RKHS norm measures function smoothness."
tags: ["kernel-methods", "gaussian-processes", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVwcm9kdWNpbmcgS2VybmVsIEhpbGJlcnQgU3BhY2VzIChSS0hTKSBhcmUgdGhlIG1hdGhlbWF0aWNhbCBiYWNrYm9uZSBvZiBldmVyeSBrZXJuZWwgbWV0aG9kIOKAlCBmcm9tIFNWTXMgYW5kIEdhdXNzaWFuIHByb2Nlc3NlcyB0byBrZXJuZWwgUENBIGFuZCBrZXJuZWwgcmlkZ2UgcmVncmVzc2lvbi4gQW4gUktIUyBpcyBhIEhpbGJlcnQgc3BhY2Ugb2YgZnVuY3Rpb25zIHdoZXJlIHBvaW50IGV2YWx1YXRpb24gaXMgYSBib3VuZGVkIGxpbmVhciBmdW5jdGlvbmFsLCBleHByZXNzZWQgdGhyb3VnaCB0aGUgcmVwcm9kdWNpbmcgcHJvcGVydHkuIFVuZGVyc3RhbmRpbmcgUktIUyB1bmxvY2tzIGEgdW5pZmllZCB2aWV3IG9mIHJlZ3VsYXJpemF0aW9uLCBrZXJuZWwgZGVzaWduLCBhbmQgdGhlIHJlcHJlc2VudGVyIHRoZW9yZW0gdGhhdCBqdXN0aWZpZXMga2VybmVsaXppbmcgYW55IGxpbmVhciBtZXRob2QuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2hhdCBJcyBhIEhpbGJlcnQgU3BhY2Ugb2YgRnVuY3Rpb25zPyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBIaWxiZXJ0IHNwYWNlIEhfayBpcyBhIGNvbXBsZXRlIGlubmVyIHByb2R1Y3Qgc3BhY2UuIFdoZW4gSF9rIGlzIGEgc3BhY2Ugb2YgZnVuY3Rpb25zIGYgOiBYIOKGkiDihJ0sIHRoZSBpbm5lciBwcm9kdWN0IOKfqGYsIGfin6lfayBpbmR1Y2VzIGEgbm9ybSDigJZm4oCWX2sgPSDiiJrin6hmLGbin6lfayB0aGF0IG1lYXN1cmVzIGZ1bmN0aW9uIHNpemUuIFRoZSBzdWJzY3JpcHQgayByZWZlcnMgdG8gdGhlIGtlcm5lbCB0aGF0IGRlZmluZXMgdGhlIGdlb21ldHJ5IG9mIHRoaXMgc3BhY2UuIEluIG1hY2hpbmUgbGVhcm5pbmcsIEhfayBpcyB0aGUgY2xvc3VyZSBvZiB0aGUgc3BhbiBvZiBmdW5jdGlvbnMge2sowrcsIHgpIDogeCDiiIggWH0uIENvbXBsZXRlbmVzcyBtZWFucyBldmVyeSBDYXVjaHkgc2VxdWVuY2UgY29udmVyZ2VzIOKAlCBhIHJlcXVpcmVtZW50IHRoYXQgbWFrZXMgY2FsY3VsdXMgYW5kIG9wdGltaXphdGlvbiB3b3JrIG92ZXIgZnVuY3Rpb24gc3BhY2VzLiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50IjoiXFxsYW5nbGUgZiwgZyBcXHJhbmdsZV97SF9rfSA9IFxcc3VtX3tpLGp9IFxcYWxwaGFfaSBcXGJldGFfaiBrKHhfaSwgeF9qKSwgXFxxcXVhZCBcXHxmXFx8XjJfe0hfa30gPSBcXHN1bV97aSxqfSBcXGFscGhhX2kgXFxhbHBoYV9qIGsoeF9pLCB4X2opIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIFJlcHJvZHVjaW5nIFByb3BlcnR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZGVmaW5pbmcgZmVhdHVyZSBvZiBhbiBSS0hTIGlzIHRoZSByZXByb2R1Y2luZyBwcm9wZXJ0eTogZm9yIGV2ZXJ5IHgg4oiIIFggYW5kIGV2ZXJ5IGYg4oiIIEhfaywgdGhlIGZ1bmN0aW9uIHZhbHVlIGYoeCkgaXMgcmVwcm9kdWNlZCBieSB0aGUgaW5uZXIgcHJvZHVjdCB3aXRoIHRoZSBrZXJuZWwgZnVuY3Rpb24gayjCtywgeCkgYW5jaG9yZWQgYXQgeC4gVGhpcyBtZWFucyBwb2ludCBldmFsdWF0aW9uIOKAlCB3aGljaCBpcyBub3QgYSBib3VuZGVkIG9wZXJhdGlvbiBpbiBnZW5lcmFsIEzigoIgc3BhY2VzIOKAlCBpcyBjb250aW51b3VzIGluIEhfay4gVGhlIGZ1bmN0aW9uIGsowrcsIHgpIGFjdHMgYXMgdGhlIHJlcHJlc2VudGVyIG9mIGV2YWx1YXRpb24gYXQgeC4gRnJvbSB0aGlzLCBrKHgsIHopID0g4p+oayjCtyx4KSwgayjCtyx6KeKfqV9rLCBsaW5raW5nIGtlcm5lbHMgdG8gaW5uZXIgcHJvZHVjdHMgb2YgZmVhdHVyZSBtYXBzIM+GKHgpID0gayjCtywgeCkuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJmKHgpID0gXFxsYW5nbGUgZixcXCwgayhcXGNkb3QsIHgpIFxccmFuZ2xlX3tIX2t9IFxccXVhZCBcXGZvcmFsbFxcLCBmIFxcaW4gSF9rLFxcOyBcXGZvcmFsbFxcLCB4IFxcaW4gWCJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiVGhlIEtlcm5lbCBUcmljayBVbnBhY2tlZCIsImNvbnRlbnQiOiJUaGUgcmVwcm9kdWNpbmcgcHJvcGVydHkgaW1wbGllcyBrKHgsIHopID0g4p+oz4YoeCksIM+GKHop4p+pX2sgd2hlcmUgz4YoeCkgPSBrKMK3LCB4KSDiiIggSF9rLiBFdmVyeSBrZXJuZWwgZXZhbHVhdGlvbiBpcyBhbiBpbm5lciBwcm9kdWN0IGluIHRoZSBSS0hTIGZlYXR1cmUgc3BhY2Ug4oCUIHRoaXMgaXMgdGhlIGtlcm5lbCB0cmljay4gWW91IG5ldmVyIG5lZWQgdG8gY29tcHV0ZSDPhih4KSBleHBsaWNpdGx5OyB0aGUga2VybmVsIGZ1bmN0aW9uIGsgY29tcHV0ZXMgdGhlIGlubmVyIHByb2R1Y3QgZGlyZWN0bHksIGV2ZW4gd2hlbiBIX2sgaXMgaW5maW5pdGUtZGltZW5zaW9uYWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVyY2VyXHUwMDI3cyBUaGVvcmVtIGFuZCBWYWxpZCBLZXJuZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOb3QgZXZlcnkgc3ltbWV0cmljIGZ1bmN0aW9uIGsgOiBYIMOXIFgg4oaSIOKEnSBkZWZpbmVzIGEgdmFsaWQgUktIUy4gTWVyY2VyXHUwMDI3cyB0aGVvcmVtIGNoYXJhY3Rlcml6ZXMgdmFsaWQga2VybmVsczogayBpcyBhIE1lcmNlciBrZXJuZWwgaWYgYW5kIG9ubHkgaWYgdGhlIEdyYW0gbWF0cml4IEsgd2l0aCBLX2lqID0gayh44bWiLCB44rG8KSBpcyBwb3NpdGl2ZSBzZW1pLWRlZmluaXRlIChQU0QpIGZvciBldmVyeSBmaW5pdGUgY29sbGVjdGlvbiBvZiBwb2ludHMuIEVxdWl2YWxlbnRseSwg4oir4oirIGsoeCx6KWYoeClmKHopIGR4IGR6IOKJpSAwIGZvciBhbGwgc3F1YXJlLWludGVncmFibGUgZi4gUkJGLCBwb2x5bm9taWFsIChjIOKJpSAwKSwgYW5kIE1hdMOpcm4ga2VybmVscyBzYXRpc2Z5IHRoaXM7IHRoZSBuZWdhdGl2ZSBzcXVhcmVkIGRpc3RhbmNlIGsoeCx6KSA9IOKIkuKAlnjiiJJ64oCWwrIgZG9lcyBub3QuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJrIFxcdGV4dHsgaXMgYSBNZXJjZXIga2VybmVsfSBcXGlmZiBLX3tpan0gPSBrKHhfaSwgeF9qKSBcXHRleHR7IGlzIFBTRCBmb3IgYWxsIGZpbml0ZSB9IFxce3hfMSxcXGxkb3RzLHhfblxcfSBcXHN1YnNldGVxIFgifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgUmVwcmVzZW50ZXIgVGhlb3JlbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlcHJlc2VudGVyIHRoZW9yZW0gaXMgdGhlIGtleSByZXN1bHQgbWFraW5nIGtlcm5lbCBtZXRob2RzIHRyYWN0YWJsZSBpbiBpbmZpbml0ZS1kaW1lbnNpb25hbCBzcGFjZXMuIEl0IHN0YXRlczogdGhlIG1pbmltaXplciBvZiBhbnkgcmVndWxhcml6ZWQgZW1waXJpY2FsIHJpc2sgTChmKHjigoEpLOKApixmKHjigpkpLHkpICsgzrvigJZm4oCWwrJfayBvdmVyIGYg4oiIIEhfayB0YWtlcyB0aGUgZm9ybSBmKih4KSA9IM6j4bWiIM6x4bWiIGsoeOG1oiwgeCkuIFRoaXMgY29sbGFwc2VzIGluZmluaXRlLWRpbWVuc2lvbmFsIG9wdGltaXphdGlvbiBpbnRvIHNvbHZpbmcgZm9yIG4gZHVhbCBjb2VmZmljaWVudHMuIEZvciBrZXJuZWwgcmlkZ2UgcmVncmVzc2lvbiwgdGhlIGNsb3NlZC1mb3JtIGR1YWwgaXMgzrEgPSAoSyArIM67SSnigbvCuXkuIFByZWRpY3Rpb24gYXQgeCogY29zdHMgTyhuKSBrZXJuZWwgZXZhbHVhdGlvbnMg4oCUIG5vIGV4cGxpY2l0IGZlYXR1cmUgbWFwIHJlcXVpcmVkLiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50IjoiZl4qKHgpID0gXFxzdW1fe2k9MX1ebiBcXGFscGhhX2lcXCwgayh4X2ksIHgpLCBcXHF1YWQgXFxib2xkc3ltYm9se1xcYWxwaGF9ID0gKEsgKyBcXGxhbWJkYSBJKV57LTF9XFxtYXRoYmZ7eX0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb29yZS1Bcm9uc3pham4gVGhlb3JlbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIE1vb3JlLUFyb25zemFqbiB0aGVvcmVtIGVzdGFibGlzaGVzIGEgb25lLXRvLW9uZSBjb3JyZXNwb25kZW5jZSBiZXR3ZWVuIHN5bW1ldHJpYyBQU0Qga2VybmVscyBhbmQgUktIU3M6IGZvciBldmVyeSBNZXJjZXIga2VybmVsIGsgdGhlcmUgZXhpc3RzIGEgdW5pcXVlIFJLSFMgSF9rIHdob3NlIHJlcHJvZHVjaW5nIGtlcm5lbCBpcyBleGFjdGx5IGssIGFuZCBjb252ZXJzZWx5IGV2ZXJ5IFJLSFMgaGFzIGEgdW5pcXVlIHJlcHJvZHVjaW5nIGtlcm5lbC4gVGhpcyBiaWplY3Rpb24gbWVhbnMgY2hvb3NpbmcgYSBrZXJuZWwgaXMgZXF1aXZhbGVudCB0byBjaG9vc2luZyBhIGZ1bmN0aW9uIHNwYWNlIOKAlCB0aGUga2VybmVsIGVuY29kZXMgYWxsIHNtb290aG5lc3MsIHBlcmlvZGljaXR5LCBhbmQgY29tcGxleGl0eSBhc3N1bXB0aW9ucyB5b3UgaW1wb3NlIG9uIGYuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUktIUyBOb3JtIGFzIGEgU21vb3RobmVzcyBNZWFzdXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbm9ybSDigJZm4oCWwrJfayBtZWFzdXJlcyBmdW5jdGlvbiBjb21wbGV4aXR5IHJlbGF0aXZlIHRvIHRoZSBrZXJuZWwuIEZvciBhbiBSQkYga2VybmVsLCDigJZm4oCWwrJfayBwZW5hbGl6ZXMgaGlnaC1mcmVxdWVuY3kgY29tcG9uZW50cyDigJQgZnVuY3Rpb25zIHRoYXQgdmFyeSBmYXN0ZXIgdGhhbiB0aGUgbGVuZ3RoLXNjYWxlIOKEkyBoYXZlIGxhcmdlIFJLSFMgbm9ybS4gRm9yIGEgcG9seW5vbWlhbCBrZXJuZWwgb2YgZGVncmVlIGQsIOKAlmbigJbCsl9rIHBlbmFsaXplcyBoaWdoLWRlZ3JlZSBwb2x5bm9taWFsIGNvZWZmaWNpZW50cy4gUmVndWxhcml6aW5nIHdpdGggzrvigJZm4oCWwrJfayBlbmZvcmNlcyBzbW9vdGhuZXNzIGluIHRoZSBzZW5zZSBkZWZpbmVkIGJ5IGsg4oCUIHRoZSByZWd1bGFyaXplciBhbmQgZnVuY3Rpb24gc3BhY2UgYXJlIGNvLWRlc2lnbmVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgRXhhbXBsZXMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiBjb21wdXRlX2dyYW1fbWF0cml4KFgsIGtlcm5lbF9mbik6XG4gICAgbiA9IGxlbihYKVxuICAgIEsgPSBucC56ZXJvcygobiwgbikpXG4gICAgZm9yIGkgaW4gcmFuZ2Uobik6XG4gICAgICAgIGZvciBqIGluIHJhbmdlKG4pOlxuICAgICAgICAgICAgS1tpLCBqXSA9IGtlcm5lbF9mbihYW2ldLCBYW2pdKVxuICAgIHJldHVybiBLXG5cbmRlZiBpc19wc2QoSywgdG9sPTFlLTEwKTpcbiAgICBlaWdlbnZhbHVlcyA9IG5wLmxpbmFsZy5laWd2YWxzaChLKVxuICAgIHJldHVybiBucC5hbGwoZWlnZW52YWx1ZXMgXHUwMDNlPSAtdG9sKSwgZWlnZW52YWx1ZXNcblxuIyBWYWxpZCBrZXJuZWw6IFJCRiBrKHgseikgPSBleHAoLXx8eC16fHxeMiAvICgyKmVsbF4yKSlcbmRlZiByYmYoeCwgeiwgZWxsPTEuMCk6XG4gICAgcmV0dXJuIG5wLmV4cCgtbnAuc3VtKCh4IC0geikqKjIpIC8gKDIgKiBlbGwqKjIpKVxuXG4jIEludmFsaWQga2VybmVsOiBub3QgcG9zaXRpdmUgc2VtaS1kZWZpbml0ZVxuZGVmIGludmFsaWRfa2VybmVsKHgsIHopOlxuICAgIHJldHVybiAtbnAuc3VtKCh4IC0geikqKjIpXG5cblggPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoNDIpLnJhbmRuKDIwLCAyKVxuS19yYmYgPSBjb21wdXRlX2dyYW1fbWF0cml4KFgsIHJiZilcbktfYmFkID0gY29tcHV0ZV9ncmFtX21hdHJpeChYLCBpbnZhbGlkX2tlcm5lbClcblxucHNkX3JiZiwgZWlnc19yYmYgPSBpc19wc2QoS19yYmYpXG5wc2RfYmFkLCBlaWdzX2JhZCA9IGlzX3BzZChLX2JhZClcblxucHJpbnQoZlx1MDAyN1JCRiBrZXJuZWwgUFNEOiB7cHNkX3JiZn0sIG1pbiBlaWdlbnZhbHVlOiB7ZWlnc19yYmYubWluKCk6LjZmfVx1MDAyNylcbnByaW50KGZcdTAwMjdJbnZhbGlkIGtlcm5lbCBQU0Q6IHtwc2RfYmFkfSwgbWluIGVpZ2VudmFsdWU6IHtlaWdzX2JhZC5taW4oKTouNmZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3TWVyY2VyIGNvbmRpdGlvbjogayBpcyB2YWxpZCBpZmYgR3JhbSBtYXRyaXggaXMgUFNEIGZvciBhbGwgZmluaXRlIHNldHMuXHUwMDI3KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFJCRiBHcmFtIG1hdHJpeCBoYXMgYWxsIG5vbi1uZWdhdGl2ZSBlaWdlbnZhbHVlcyDigJQgaXQgaXMgUFNEIGFuZCBzYXRpc2ZpZXMgdGhlIE1lcmNlciBjb25kaXRpb24uIFRoZSBuZWdhdGl2ZSBzcXVhcmVkIGRpc3RhbmNlIGtlcm5lbCBoYXMgbmVnYXRpdmUgZWlnZW52YWx1ZXMgYW5kIGZhaWxzIE1lcmNlclx1MDAyN3MgY29uZGl0aW9uLCBzbyBpdCBjYW5ub3QgYmUgdXNlZCBhcyBhIGtlcm5lbCBpbiBhbnkga2VybmVsIG1ldGhvZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfcmVncmVzc2lvblxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbmRlZiByYmZfa2VybmVsX21hdHJpeChYMSwgWDIsIGVsbD0xLjApOlxuICAgIGRpZmYgPSBYMVs6LCBOb25lLCA6XSAtIFgyW05vbmUsIDosIDpdXG4gICAgcmV0dXJuIG5wLmV4cCgtbnAuc3VtKGRpZmYqKjIsIGF4aXM9LTEpIC8gKDIgKiBlbGwqKjIpKVxuXG5kZWYga2VybmVsX3JpZGdlX3JlZ3Jlc3Npb24oWF90cmFpbiwgeV90cmFpbiwgWF90ZXN0LCBsYW09MC4xLCBlbGw9MS4wKTpcbiAgICBLID0gcmJmX2tlcm5lbF9tYXRyaXgoWF90cmFpbiwgWF90cmFpbiwgZWxsKVxuICAgIG4gPSBsZW4oeV90cmFpbilcbiAgICBhbHBoYSA9IG5wLmxpbmFsZy5zb2x2ZShLICsgbGFtICogbnAuZXllKG4pLCB5X3RyYWluKVxuICAgIEtfc3RhciA9IHJiZl9rZXJuZWxfbWF0cml4KFhfdGVzdCwgWF90cmFpbiwgZWxsKVxuICAgIHJldHVybiBLX3N0YXIgQCBhbHBoYSwgYWxwaGFcblxuWCwgeSA9IG1ha2VfcmVncmVzc2lvbihuX3NhbXBsZXM9MTAwLCBuX2ZlYXR1cmVzPTUsIG5vaXNlPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxuc2MgPSBTdGFuZGFyZFNjYWxlcigpXG5YID0gc2MuZml0X3RyYW5zZm9ybShYKVxuWF90cmFpbiwgWF90ZXN0ID0gWFs6ODBdLCBYWzgwOl1cbnlfdHJhaW4sIHlfdGVzdCA9IHlbOjgwXSwgeVs4MDpdXG5cbnlfcHJlZCwgYWxwaGEgPSBrZXJuZWxfcmlkZ2VfcmVncmVzc2lvbihYX3RyYWluLCB5X3RyYWluLCBYX3Rlc3QsIGxhbT0wLjAxKVxubXNlID0gbnAubWVhbigoeV9wcmVkIC0geV90ZXN0KSoqMilcbnByaW50KGZcdTAwMjdLUlIgVGVzdCBNU0U6IHttc2U6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdSZXByZXNlbnRlcjoge2xlbihhbHBoYSl9IGR1YWwgY29lZmZpY2llbnRzIGFscGhhX2kgKG9uZSBwZXIgdHJhaW5pbmcgcG9pbnQpXHUwMDI3KVxucHJpbnQoXHUwMDI3ZiooeCopID0gc3VtX2kgYWxwaGFfaSAqIGsoeF9pLCB4KikgLS0gbGl2ZXMgaW4gc3BhbiBvZiB0cmFpbmluZyBrZXJuZWwgZXZhbHVhdGlvbnNcdTAwMjcpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcmVwcmVzZW50ZXIgdGhlb3JlbSBndWFyYW50ZWVzIGYqIGxpZXMgaW4gdGhlIGZpbml0ZS1kaW1lbnNpb25hbCBzcGFuIG9mIG4ga2VybmVsIGV2YWx1YXRpb25zLiBTb2x2aW5nIHRoZSBkdWFsIHN5c3RlbSDOsSA9IChLK867SSnigbvCuXkgaXMgTyhuwrMpIOKAlCBubyBleHBsaWNpdCBoaWdoLWRpbWVuc2lvbmFsIGZlYXR1cmUgdmVjdG9ycyBuZWVkZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgc2FtcGxlX2dwX2Z1bmN0aW9ucyh4LCBrZXJuZWxfZm4sIG5fc2FtcGxlcz01LCBzZWVkPTQyKTpcbiAgICBLID0ga2VybmVsX2ZuKHhbOiwgTm9uZV0sIHhbOiwgTm9uZV0pXG4gICAgSyArPSAxZS04ICogbnAuZXllKGxlbih4KSlcbiAgICBMID0gbnAubGluYWxnLmNob2xlc2t5KEspXG4gICAgcm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKHNlZWQpXG4gICAgcmV0dXJuIFtMIEAgcm5nLnJhbmRuKGxlbih4KSkgZm9yIF8gaW4gcmFuZ2Uobl9zYW1wbGVzKV1cblxuZGVmIHJiZl9rbShYMSwgWDIsIGVsbD0wLjUpOlxuICAgIGRpZmYgPSBYMVs6LCBOb25lLCA6XSAtIFgyW05vbmUsIDosIDpdXG4gICAgcmV0dXJuIG5wLmV4cCgtbnAuc3VtKGRpZmYqKjIsIGF4aXM9LTEpIC8gKDIgKiBlbGwqKjIpKVxuXG5kZWYgbWF0ZXJuMzJfa20oWDEsIFgyLCBlbGw9MS4wKTpcbiAgICByID0gbnAuc3FydChucC5zdW0oKFgxWzosIE5vbmUsIDpdIC0gWDJbTm9uZSwgOiwgOl0pKioyLCBheGlzPS0xKSkgLyBlbGxcbiAgICByZXR1cm4gKDEgKyBucC5zcXJ0KDMpICogcikgKiBucC5leHAoLW5wLnNxcnQoMykgKiByKVxuXG54ID0gbnAubGluc3BhY2UoLTMsIDMsIDIwMClcbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMiwgNCkpXG5mb3IgYXgsIChsYWJlbCwga21fZm4pIGluIHppcChheGVzLCBbXG4gICAgKFx1MDAyN1JCRiBlbGw9MC41IChzbW9vdGggUktIUylcdTAwMjcsIGxhbWJkYSBYMSwgWDI6IHJiZl9rbShYMSwgWDIsIDAuNSkpLFxuICAgIChcdTAwMjdNYXRlcm4tMy8yIGVsbD0xIChyb3VnaGVyIFJLSFMpXHUwMDI3LCBsYW1iZGEgWDEsIFgyOiBtYXRlcm4zMl9rbShYMSwgWDIsIDEuMCkpLFxuXSk6XG4gICAgc2FtcGxlcyA9IHNhbXBsZV9ncF9mdW5jdGlvbnMoeCwga21fZm4pXG4gICAgZm9yIHMgaW4gc2FtcGxlczpcbiAgICAgICAgYXgucGxvdCh4LCBzLCBhbHBoYT0wLjcpXG4gICAgYXguc2V0X3RpdGxlKGxhYmVsKVxuICAgIGF4LnNldF94bGFiZWwoXHUwMDI3eFx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3cmtoc19zYW1wbGVzLnBuZ1x1MDAyNywgZHBpPTEwMClcbnByaW50KFx1MDAyN1NhdmVkIHJraHNfc2FtcGxlcy5wbmdcdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgcmtoc19ub3JtX3NxdWFyZWQoYWxwaGEsIEspOlxuICAgICMgfHxmfHxeMl9rID0gYWxwaGFeVCBLIGFscGhhIGZvciBmKC4pID0gc3VtX2kgYWxwaGFfaSBrKHhfaSwgLilcbiAgICByZXR1cm4gZmxvYXQoYWxwaGEgQCBLIEAgYWxwaGEpXG5cbmRlZiBsMl9ub3JtX3NxdWFyZWQoZl92YWx1ZXMpOlxuICAgICMgQXBwcm94aW1hdGUgfHxmfHxeMl9MMiB2aWEgdHJhcGV6b2lkYWwgaW50ZWdyYXRpb25cbiAgICByZXR1cm4gZmxvYXQobnAudHJhcHooZl92YWx1ZXMqKjIpKVxuXG5kZWYgcmJmX2tlcm5lbF9tYXRyaXgoeCwgZWxsPTEuMCk6XG4gICAgZGlmZiA9IHhbOiwgTm9uZV0gLSB4W05vbmUsIDpdXG4gICAgcmV0dXJuIG5wLmV4cCgtZGlmZioqMiAvICgyICogZWxsKioyKSlcblxueCA9IG5wLmxpbnNwYWNlKC0zLCAzLCAxMDApXG5LID0gcmJmX2tlcm5lbF9tYXRyaXgoeCwgZWxsPTEuMClcbksgKz0gMWUtOCAqIG5wLmV5ZSgxMDApXG5cbnJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZSgwKVxuYWxwaGFfc21vb3RoID0gcm5nLnJhbmRuKDEwMCkgKiAwLjAyICAgIyBzbWFsbCBjb2VmZmljaWVudHMgLVx1MDAzZSBsb3cgUktIUyBub3JtXG5hbHBoYV9yb3VnaCAgPSBybmcucmFuZG4oMTAwKSAqIDAuNTAgICAjIGxhcmdlIGNvZWZmaWNpZW50cyAtXHUwMDNlIGhpZ2ggUktIUyBub3JtXG5cbmZfc21vb3RoID0gSyBAIGFscGhhX3Ntb290aFxuZl9yb3VnaCAgPSBLIEAgYWxwaGFfcm91Z2hcblxucHJpbnQoXHUwMDI3U21vb3RoIGZ1bmN0aW9uOlx1MDAyNylcbnByaW50KGZcdTAwMjcgIFJLSFMgbm9ybV4yIDoge3JraHNfbm9ybV9zcXVhcmVkKGFscGhhX3Ntb290aCwgSyk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjcgIEwyICAgbm9ybV4yIDoge2wyX25vcm1fc3F1YXJlZChmX3Ntb290aCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN1JvdWdoIGZ1bmN0aW9uOlx1MDAyNylcbnByaW50KGZcdTAwMjcgIFJLSFMgbm9ybV4yIDoge3JraHNfbm9ybV9zcXVhcmVkKGFscGhhX3JvdWdoLCBLKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgTDIgICBub3JtXjIgOiB7bDJfbm9ybV9zcXVhcmVkKGZfcm91Z2gpOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdSS0hTIG5vcm0gcGVuYWxpemVzIGNvbXBsZXhpdHkgdy5yLnQuIHRoZSBrZXJuZWwgc3RydWN0dXJlLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXJuZWwgVmFsaWRpdHkgUmVmZXJlbmNlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIktlcm5lbCBrKHgseikiLCJNZXJjZXIgLyBQU0QiLCJGZWF0dXJlIE1hcCBEaW1lbnNpb24iLCJUeXBpY2FsIFVzZSBDYXNlIl0sInJvd3MiOltbIlJCRjogZXhwKC3igJZ4LXrigJbCsi8y4oSTwrIpIiwiWWVzIOKAlCBhbGwgZWlnZW52YWx1ZXMg4omlIDAiLCJJbmZpbml0ZSAodmlhIFRheWxvciBleHBhbnNpb24pIiwiR1AgY292YXJpYW5jZSwgbm9ubGluZWFyIHJlZ3Jlc3Npb24sIFNWTSJdLFsiUG9seW5vbWlhbDogKHjhtYB6K2MpXmQsIGPiiaUwIiwiWWVzIOKAlCBhbGwgZWlnZW52YWx1ZXMg4omlIDAiLCJGaW5pdGU6IEMocCtkLGQpIG1vbm9taWFscyIsIlRleHQga2VybmVscywgcG9seW5vbWlhbCByZWdyZXNzaW9uIl0sWyJMaW5lYXI6IHjhtYB6IiwiWWVzIOKAlCBzdGFuZGFyZCBkb3QgcHJvZHVjdCIsInAgKGlucHV0IGRpbWVuc2lvbikiLCJMaW5lYXIgU1ZNLCBSaWRnZSByZWdyZXNzaW9uIl0sWyJNYXTDqXJuLTUvMiIsIlllcyDigJQgYWxsIGVpZ2VudmFsdWVzIOKJpSAwIiwiSW5maW5pdGUiLCJQaHlzaWNhbCBzeXN0ZW1zLCBHUCB3aXRoIGZpbml0ZSBzbW9vdGhuZXNzIl0sWyIt4oCWeC164oCWwrIgKG5lZ2F0ZWQgc3EuIGRpc3RhbmNlKSIsIk5vIOKAlCBuZWdhdGl2ZSBlaWdlbnZhbHVlcyBleGlzdCIsIk5vIHZhbGlkIGZlYXR1cmUgbWFwIiwiSW52YWxpZCDigJQgZmFpbHMgTWVyY2VyIGNvbmRpdGlvbiJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgUktIUyBmcmFtZXdvcmsgdW5pZmllcyByZWd1bGFyaXphdGlvbiBhbmQgZnVuY3Rpb24tc3BhY2UgZGVzaWduLiBDaG9vc2luZyBhIGtlcm5lbCBpbXBsaWNpdGx5IHNlbGVjdHMgdGhlIGZ1bmN0aW9uIHNwYWNlIGFuZCBzbW9vdGhuZXNzIHByaW9yLiBUaGUgcmVwcmVzZW50ZXIgdGhlb3JlbSB0aGVuIHJlZHVjZXMgaW5maW5pdGUtZGltZW5zaW9uYWwgb3B0aW1pemF0aW9uIHRvIGEgZmluaXRlIG7Dl24gbGluZWFyIHN5c3RlbSDigJQgbWFraW5nIGtlcm5lbCBtZXRob2RzIGNvbXB1dGF0aW9uYWxseSBmZWFzaWJsZSBldmVuIHdpdGggaW5maW5pdGUtZGltZW5zaW9uYWwgZmVhdHVyZSBtYXBzLiJ9XQ=="
---
# Reproducing Kernel Hilbert Spaces (RKHS)

Reproducing Kernel Hilbert Spaces (RKHS) are the mathematical backbone of every kernel method — from SVMs and Gaussian processes to kernel PCA and kernel ridge regression. An RKHS is a Hilbert space of functions where point evaluation is a bounded linear functional, expressed through the reproducing property. Understanding RKHS unlocks a unified view of regularization, kernel design, and the representer theorem that justifies kernelizing any linear method.

## What Is a Hilbert Space of Functions?

A Hilbert space H_k is a complete inner product space. When H_k is a space of functions f : X → ℝ, the inner product ⟨f, g⟩_k induces a norm ‖f‖_k = √⟨f,f⟩_k that measures function size. The subscript k refers to the kernel that defines the geometry of this space. In machine learning, H_k is the closure of the span of functions {k(·, x) : x ∈ X}. Completeness means every Cauchy sequence converges — a requirement that makes calculus and optimization work over function spaces.

$$\langle f, g \rangle_{H_k} = \sum_{i,j} \alpha_i \beta_j k(x_i, x_j), \qquad \|f\|^2_{H_k} = \sum_{i,j} \alpha_i \alpha_j k(x_i, x_j)$$

## The Reproducing Property

The defining feature of an RKHS is the reproducing property: for every x ∈ X and every f ∈ H_k, the function value f(x) is reproduced by the inner product with the kernel function k(·, x) anchored at x. This means point evaluation — which is not a bounded operation in general L₂ spaces — is continuous in H_k. The function k(·, x) acts as the representer of evaluation at x. From this, k(x, z) = ⟨k(·,x), k(·,z)⟩_k, linking kernels to inner products of feature maps φ(x) = k(·, x).

$$f(x) = \langle f,\, k(\cdot, x) \rangle_{H_k} \quad \forall\, f \in H_k,\; \forall\, x \in X$$

> **The Kernel Trick Unpacked**: The reproducing property implies k(x, z) = ⟨φ(x), φ(z)⟩_k where φ(x) = k(·, x) ∈ H_k. Every kernel evaluation is an inner product in the RKHS feature space — this is the kernel trick. You never need to compute φ(x) explicitly; the kernel function k computes the inner product directly, even when H_k is infinite-dimensional.

## Mercer's Theorem and Valid Kernels

Not every symmetric function k : X × X → ℝ defines a valid RKHS. Mercer's theorem characterizes valid kernels: k is a Mercer kernel if and only if the Gram matrix K with K_ij = k(xᵢ, xⱼ) is positive semi-definite (PSD) for every finite collection of points. Equivalently, ∫∫ k(x,z)f(x)f(z) dx dz ≥ 0 for all square-integrable f. RBF, polynomial (c ≥ 0), and Matérn kernels satisfy this; the negative squared distance k(x,z) = −‖x−z‖² does not.

$$k \text{ is a Mercer kernel} \iff K_{ij} = k(x_i, x_j) \text{ is PSD for all finite } \{x_1,\ldots,x_n\} \subseteq X$$

## The Representer Theorem

The representer theorem is the key result making kernel methods tractable in infinite-dimensional spaces. It states: the minimizer of any regularized empirical risk L(f(x₁),…,f(xₙ),y) + λ‖f‖²_k over f ∈ H_k takes the form f*(x) = Σᵢ αᵢ k(xᵢ, x). This collapses infinite-dimensional optimization into solving for n dual coefficients. For kernel ridge regression, the closed-form dual is α = (K + λI)⁻¹y. Prediction at x* costs O(n) kernel evaluations — no explicit feature map required.

$$f^*(x) = \sum_{i=1}^n \alpha_i\, k(x_i, x), \quad \boldsymbol{\alpha} = (K + \lambda I)^{-1}\mathbf{y}$$

## Moore-Aronszajn Theorem

The Moore-Aronszajn theorem establishes a one-to-one correspondence between symmetric PSD kernels and RKHSs: for every Mercer kernel k there exists a unique RKHS H_k whose reproducing kernel is exactly k, and conversely every RKHS has a unique reproducing kernel. This bijection means choosing a kernel is equivalent to choosing a function space — the kernel encodes all smoothness, periodicity, and complexity assumptions you impose on f.

## RKHS Norm as a Smoothness Measure

The norm ‖f‖²_k measures function complexity relative to the kernel. For an RBF kernel, ‖f‖²_k penalizes high-frequency components — functions that vary faster than the length-scale ℓ have large RKHS norm. For a polynomial kernel of degree d, ‖f‖²_k penalizes high-degree polynomial coefficients. Regularizing with λ‖f‖²_k enforces smoothness in the sense defined by k — the regularizer and function space are co-designed.

## Code Examples

```python
import numpy as np
import matplotlib.pyplot as plt

def compute_gram_matrix(X, kernel_fn):
    n = len(X)
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            K[i, j] = kernel_fn(X[i], X[j])
    return K

def is_psd(K, tol=1e-10):
    eigenvalues = np.linalg.eigvalsh(K)
    return np.all(eigenvalues >= -tol), eigenvalues

# Valid kernel: RBF k(x,z) = exp(-||x-z||^2 / (2*ell^2))
def rbf(x, z, ell=1.0):
    return np.exp(-np.sum((x - z)**2) / (2 * ell**2))

# Invalid kernel: not positive semi-definite
def invalid_kernel(x, z):
    return -np.sum((x - z)**2)

X = np.random.RandomState(42).randn(20, 2)
K_rbf = compute_gram_matrix(X, rbf)
K_bad = compute_gram_matrix(X, invalid_kernel)

psd_rbf, eigs_rbf = is_psd(K_rbf)
psd_bad, eigs_bad = is_psd(K_bad)

print(f'RBF kernel PSD: {psd_rbf}, min eigenvalue: {eigs_rbf.min():.6f}')
print(f'Invalid kernel PSD: {psd_bad}, min eigenvalue: {eigs_bad.min():.6f}')
print('Mercer condition: k is valid iff Gram matrix is PSD for all finite sets.')
```

The RBF Gram matrix has all non-negative eigenvalues — it is PSD and satisfies the Mercer condition. The negative squared distance kernel has negative eigenvalues and fails Mercer's condition, so it cannot be used as a kernel in any kernel method.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

def rbf_kernel_matrix(X1, X2, ell=1.0):
    diff = X1[:, None, :] - X2[None, :, :]
    return np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

def kernel_ridge_regression(X_train, y_train, X_test, lam=0.1, ell=1.0):
    K = rbf_kernel_matrix(X_train, X_train, ell)
    n = len(y_train)
    alpha = np.linalg.solve(K + lam * np.eye(n), y_train)
    K_star = rbf_kernel_matrix(X_test, X_train, ell)
    return K_star @ alpha, alpha

X, y = make_regression(n_samples=100, n_features=5, noise=0.2, random_state=42)
sc = StandardScaler()
X = sc.fit_transform(X)
X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]

y_pred, alpha = kernel_ridge_regression(X_train, y_train, X_test, lam=0.01)
mse = np.mean((y_pred - y_test)**2)
print(f'KRR Test MSE: {mse:.4f}')
print(f'Representer: {len(alpha)} dual coefficients alpha_i (one per training point)')
print('f*(x*) = sum_i alpha_i * k(x_i, x*) -- lives in span of training kernel evaluations')
```

The representer theorem guarantees f* lies in the finite-dimensional span of n kernel evaluations. Solving the dual system α = (K+λI)⁻¹y is O(n³) — no explicit high-dimensional feature vectors needed.

```python
import numpy as np
import matplotlib.pyplot as plt

def sample_gp_functions(x, kernel_fn, n_samples=5, seed=42):
    K = kernel_fn(x[:, None], x[:, None])
    K += 1e-8 * np.eye(len(x))
    L = np.linalg.cholesky(K)
    rng = np.random.RandomState(seed)
    return [L @ rng.randn(len(x)) for _ in range(n_samples)]

def rbf_km(X1, X2, ell=0.5):
    diff = X1[:, None, :] - X2[None, :, :]
    return np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

def matern32_km(X1, X2, ell=1.0):
    r = np.sqrt(np.sum((X1[:, None, :] - X2[None, :, :])**2, axis=-1)) / ell
    return (1 + np.sqrt(3) * r) * np.exp(-np.sqrt(3) * r)

x = np.linspace(-3, 3, 200)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for ax, (label, km_fn) in zip(axes, [
    ('RBF ell=0.5 (smooth RKHS)', lambda X1, X2: rbf_km(X1, X2, 0.5)),
    ('Matern-3/2 ell=1 (rougher RKHS)', lambda X1, X2: matern32_km(X1, X2, 1.0)),
]):
    samples = sample_gp_functions(x, km_fn)
    for s in samples:
        ax.plot(x, s, alpha=0.7)
    ax.set_title(label)
    ax.set_xlabel('x')
plt.tight_layout()
plt.savefig('rkhs_samples.png', dpi=100)
print('Saved rkhs_samples.png')
```

```python
import numpy as np

def rkhs_norm_squared(alpha, K):
    # ||f||^2_k = alpha^T K alpha for f(.) = sum_i alpha_i k(x_i, .)
    return float(alpha @ K @ alpha)

def l2_norm_squared(f_values):
    # Approximate ||f||^2_L2 via trapezoidal integration
    return float(np.trapz(f_values**2))

def rbf_kernel_matrix(x, ell=1.0):
    diff = x[:, None] - x[None, :]
    return np.exp(-diff**2 / (2 * ell**2))

x = np.linspace(-3, 3, 100)
K = rbf_kernel_matrix(x, ell=1.0)
K += 1e-8 * np.eye(100)

rng = np.random.RandomState(0)
alpha_smooth = rng.randn(100) * 0.02   # small coefficients -> low RKHS norm
alpha_rough  = rng.randn(100) * 0.50   # large coefficients -> high RKHS norm

f_smooth = K @ alpha_smooth
f_rough  = K @ alpha_rough

print('Smooth function:')
print(f'  RKHS norm^2 : {rkhs_norm_squared(alpha_smooth, K):.4f}')
print(f'  L2   norm^2 : {l2_norm_squared(f_smooth):.4f}')
print('Rough function:')
print(f'  RKHS norm^2 : {rkhs_norm_squared(alpha_rough, K):.4f}')
print(f'  L2   norm^2 : {l2_norm_squared(f_rough):.4f}')
print('RKHS norm penalizes complexity w.r.t. the kernel structure.')
```

## Kernel Validity Reference

| Kernel k(x,z) | Mercer / PSD | Feature Map Dimension | Typical Use Case |
| --- | --- | --- | --- |
| RBF: exp(-‖x-z‖²/2ℓ²) | Yes — all eigenvalues ≥ 0 | Infinite (via Taylor expansion) | GP covariance, nonlinear regression, SVM |
| Polynomial: (xᵀz+c)^d, c≥0 | Yes — all eigenvalues ≥ 0 | Finite: C(p+d,d) monomials | Text kernels, polynomial regression |
| Linear: xᵀz | Yes — standard dot product | p (input dimension) | Linear SVM, Ridge regression |
| Matérn-5/2 | Yes — all eigenvalues ≥ 0 | Infinite | Physical systems, GP with finite smoothness |
| -‖x-z‖² (negated sq. distance) | No — negative eigenvalues exist | No valid feature map | Invalid — fails Mercer condition |

The RKHS framework unifies regularization and function-space design. Choosing a kernel implicitly selects the function space and smoothness prior. The representer theorem then reduces infinite-dimensional optimization to a finite n×n linear system — making kernel methods computationally feasible even with infinite-dimensional feature maps.

