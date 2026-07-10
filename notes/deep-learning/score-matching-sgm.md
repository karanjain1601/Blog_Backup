---
title: "Score Matching and Score-Based Generative Models"
slug: "score-matching-sgm"
description: "Derive the score function and score matching objectives, implement denoising score matching from scratch, build a noise-conditional score network (NCSN), run annealed Langevin dynamics, and understand the mathematical equivalence between DDPM epsilon-prediction and score estimation."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2NvcmUtYmFzZWQgZ2VuZXJhdGl2ZSBtb2RlbHMgdHJhaW4gYSBuZXVyYWwgbmV0d29yayB0byBlc3RpbWF0ZSB0aGUgZ3JhZGllbnQgb2YgdGhlIGxvZyBkYXRhIGRlbnNpdHkg4oCUIHRoZSBzY29yZSBmdW5jdGlvbiBzKHgpID0g4oiHX3ggbG9nIHAoeCkuIFRoaXMgc2luZ2xlIHByaW5jaXBsZSB1bmlmaWVzIGRlbm9pc2luZyBzY29yZSBtYXRjaGluZywgbm9pc2UtY29uZGl0aW9uYWwgc2NvcmUgbmV0d29ya3MgKE5DU04pLCBhbmQgRERQTXMuIFJhdGhlciB0aGFuIGFwcHJveGltYXRpbmcgcCh4KSBkaXJlY3RseSAod2hpY2ggcmVxdWlyZXMgYSB0cmFjdGFibGUgbm9ybWFsaXppbmcgY29uc3RhbnQgWiksIHNjb3JlIG1vZGVscyBhcHByb3hpbWF0ZSDiiIdfeCBsb2cgcCh4KSwgd2hpY2ggY2FuY2VscyBaLiBBIGxlYXJuZWQgc2NvcmUgZmllbGQgdGhlbiBkcml2ZXMgaXRlcmF0aXZlIHNhbXBsaW5nIHZpYSBMYW5nZXZpbiBkeW5hbWljcyBvciByZXZlcnNlLXRpbWUgU0RFcywgZW5hYmxpbmcgZ2VuZXJhdGlvbiB3aXRob3V0IGxpa2VsaWhvb2QgZXZhbHVhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgU2NvcmUgRnVuY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIGRpc3RyaWJ1dGlvbiBwKHgpID0gcMyDKHgpL1osIHRoZSBzY29yZSBpcyBzKHgpID0g4oiHX3ggbG9nIHAoeCkgPSDiiIdfeCBsb2cgcMyDKHgpIOKAlCBaIGNhbmNlbHMgaW4gdGhlIGdyYWRpZW50LiBUaGUgc2NvcmUgaXMgYSB2ZWN0b3IgZmllbGQgcG9pbnRpbmcgdG93YXJkIGhpZ2hlci1kZW5zaXR5IHJlZ2lvbnMuIEZvciBhIEdhdXNzaWFuIHAoeCkgPSBOKM68LCDPg8KySSkgdGhlIHNjb3JlIGlzICjOvCDiiJIgeCkvz4PCsiwgYSBsaW5lYXIgcmVzdG9yaW5nIGZvcmNlIHRvd2FyZCB0aGUgbWVhbi4gQSBuZXVyYWwgc2NvcmUgbmV0d29yayBzX864KHgpIGFwcHJveGltYXRlcyB0aGlzIGZpZWxkIGFjcm9zcyB0aGUgZW50aXJlIGRhdGEgZGlzdHJpYnV0aW9uLCBlbmFibGluZyBncmFkaWVudCBhc2NlbnQgb24gbG9nIHAgd2l0aG91dCBldmVyIGNvbXB1dGluZyB0aGUgcGFydGl0aW9uIGZ1bmN0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4cGxpY2l0IFNjb3JlIE1hdGNoaW5nIChIeXbDpHJpbmVuIDIwMDUpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIeXbDpHJpbmVuICgyMDA1KSBzaG93ZWQgdGhlIHNxdWFyZWQtZXJyb3Igb2JqZWN0aXZlIEVb4oCWc1/OuCh4KSDiiJIg4oiHX3ggbG9nIHAoeCnigJbCsl0gZXF1YWxzIEVbdHIo4oiHX3ggc1/OuCh4KSkgKyDCveKAlnNfzrgoeCnigJbCsl0gdmlhIGludGVncmF0aW9uIGJ5IHBhcnRzIOKAlCBubyBwKHgpIG5lZWRlZC4gVGhlIHRyYWNlIHRlcm0gdHIo4oiHX3ggc1/OuCh4KSkgcmVxdWlyZXMgTyhkKSBiYWNrd2FyZCBwYXNzZXMgZm9yIGQtZGltZW5zaW9uYWwgaW5wdXRzLiBBdCBpbWFnZSByZXNvbHV0aW9uIDY0w5c2NCAoZD0xMjI4OCksIHRoaXMgaXMgY29tcHV0YXRpb25hbGx5IGludHJhY3RhYmxlLiBTbGljZWQgc2NvcmUgbWF0Y2hpbmcgKFNvbmcgZXQgYWwuIDIwMjApIHJlZHVjZXMgY29zdCB2aWEgcmFuZG9tIHByb2plY3Rpb25zLCBidXQgZGVub2lzaW5nIHNjb3JlIG1hdGNoaW5nIChEU00pIHByb3ZpZGVzIGEgY2xlYW5lciBzb2x1dGlvbiB3aXRoIGEgY2xvc2VkLWZvcm0gdGFyZ2V0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlbm9pc2luZyBTY29yZSBNYXRjaGluZyAoVmluY2VudCAyMDExKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmluY2VudCAoMjAxMSkgcHJvdmVkIHRoYXQgdHJhaW5pbmcgb24gY29ycnVwdGVkIGlucHV0cyBpcyBlcXVpdmFsZW50IHRvIHNjb3JlIG1hdGNoaW5nLiBHaXZlbiB4zIMgPSB4ICsgz4POtSB3aXRoIM61IH4gTigwLEkpLCB0aGUgY29uZGl0aW9uYWwgc2NvcmUgaXMg4oiHX3t4zIN9IGxvZyBwKHjMg3x4KSA9ICh4IOKIkiB4zIMpL8+DwrIg4oCUIGNvbXB1dGFibGUgd2l0aG91dCBKYWNvYmlhbiB0cmFjZXMuIFRoZSBEU00gbG9zcyBMID0gRVvigJZzX864KHjMgykg4oiSICh44oiSeMyDKS/Pg8Ky4oCWwrJdIHRyYWlucyB0aGUgc2NvcmUgbmV0d29yayB0byBwcmVkaWN0IHRoZSBkaXJlY3Rpb24gZnJvbSBhbnkgbm9pc3kgcG9pbnQgYmFjayB0b3dhcmQgY2xlYW4gZGF0YS4gVGhpcyBpcyBwcmVjaXNlbHkgd2hhdCBERFBNcyBkbzogcHJlZGljdGluZyBub2lzZSDOtV/OuCDiiYggzrUgaXMgZXF1aXZhbGVudCB0byBlc3RpbWF0aW5nIHRoZSBzY29yZSBzX864KHjMgykg4omIIOKIks61L8+DLCBqdXN0IHNjYWxlZCBkaWZmZXJlbnRseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgU2NvcmVOZXQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGF0YV9kaW09MiwgaGlkZGVuPTEyOCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZGF0YV9kaW0sIGhpZGRlbiksIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW4sIGhpZGRlbiksIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW4sIGRhdGFfZGltKVxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldCh4KVxuXG5kZWYgZHNtX2xvc3Moc2NvcmVfbmV0LCB4LCBzaWdtYT0wLjUpOlxuICAgIFwiXCJcIkRTTTogc190aGV0YSh4X3RpbGRlKSBhcHByb3ggKHggLSB4X3RpbGRlKSAvIHNpZ21hXjIuXCJcIlwiXG4gICAgbm9pc2UgPSB0b3JjaC5yYW5kbl9saWtlKHgpICogc2lnbWFcbiAgICB4X3RpbGRlID0geCArIG5vaXNlXG4gICAgdGFyZ2V0ID0gKHggLSB4X3RpbGRlKSAvIChzaWdtYSAqKiAyKVxuICAgIHJldHVybiBGLm1zZV9sb3NzKHNjb3JlX25ldCh4X3RpbGRlKSwgdGFyZ2V0KVxuXG50b3JjaC5tYW51YWxfc2VlZCg0Milcbm5ldCA9IFNjb3JlTmV0KClcbm9wdCA9IHRvcmNoLm9wdGltLkFkYW0obmV0LnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbmRhdGEgPSB0b3JjaC5jYXQoW3RvcmNoLnJhbmRuKDUxMiwgMikgKyAyLjAsIHRvcmNoLnJhbmRuKDUxMiwgMikgLSAyLjBdKVxuZm9yIHN0ZXAgaW4gcmFuZ2UoMzAwKTpcbiAgICB4ID0gZGF0YVt0b3JjaC5yYW5kaW50KGxlbihkYXRhKSwgKDY0LCkpXVxuICAgIGxvc3MgPSBkc21fbG9zcyhuZXQsIHgsIHNpZ21hPTAuNClcbiAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgIGlmIHN0ZXAgJSAxMDAgPT0gMDpcbiAgICAgICAgcHJpbnQoZlx1MDAyN1N0ZXAge3N0ZXB9OiBEU00gbG9zcyA9IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5vaXNlIENvbmRpdGlvbmFsIFNjb3JlIE5ldHdvcmtzIChOQ1NOKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU29uZyBcdTAwMjYgRXJtb24gKDIwMTkpIGV4dGVuZGVkIERTTSB0byBtdWx0aXBsZSBub2lzZSBsZXZlbHMuIE5DU04gdHJhaW5zIHNfzrgoeCwgz4MpIG92ZXIgYSBnZW9tZXRyaWMgc2VxdWVuY2Ugz4NfMSBcdTAwM2UgLi4uIFx1MDAzZSDPg19MIChlLmcuIM+DXzE9MS4wIHRvIM+DX0w9MC4wMSwgTD0xMCkuIFRoZSB3ZWlnaHRlZCBsb3NzIM6jX2wgz4NfbMKyIMK3IEVb4oCWc1/OuCh4zIMsz4NfbCkg4oiSICh44oiSeMyDKS/Pg19swrLigJbCsl0gYmFsYW5jZXMgc2NhbGUgY29udHJpYnV0aW9ucyDigJQgdGhlIM+DX2zCsiB3ZWlnaHQgbWFrZXMgZWFjaCB0ZXJtIGRpbWVuc2lvbmFsbHkgdW5pZm9ybS4gTGFyZ2Ugz4MgZ3VpZGVzIGZyb20gYnJvYWQgbm9pc2U7IHNtYWxsIM+DIHJlZmluZXMgZmluZSBzdHJ1Y3R1cmUuIE11bHRpLXNjYWxlIHRyYWluaW5nIGFsc28gc29sdmVzIHRoZSBzY29yZSBlc3RpbWF0aW9uIHByb2JsZW0gaW4gbG93LWRlbnNpdHkgcmVnaW9ucywgd2hlcmUgc2luZ2xlLc+DIG1ldGhvZHMgcHJvZHVjZSBub2lzeSwgdW5yZWxpYWJsZSBlc3RpbWF0ZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuY2xhc3MgTkNTTlNjb3JlTmV0KG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRhdGFfZGltPTIsIGhpZGRlbj0xMjgsIG5fc2lnbWFzPTEwKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuc2lnbWFfZW1iZWQgPSBubi5FbWJlZGRpbmcobl9zaWdtYXMsIDE2KVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZGF0YV9kaW0gKyAxNiwgaGlkZGVuKSwgbm4uU2lMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuKSwgbm4uU2lMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgZGF0YV9kaW0pXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBzaWdtYV9pZHgpOlxuICAgICAgICBlbWIgPSBzZWxmLnNpZ21hX2VtYmVkKHNpZ21hX2lkeClcbiAgICAgICAgcmV0dXJuIHNlbGYubmV0KHRvcmNoLmNhdChbeCwgZW1iXSwgZGltPS0xKSlcblxuZGVmIG5jc25fbG9zcyhuZXQsIHgsIHNpZ21hcyk6XG4gICAgQiA9IHguc2l6ZSgwKVxuICAgIGlkeCA9IHRvcmNoLnJhbmRpbnQoMCwgbGVuKHNpZ21hcyksIChCLCkpXG4gICAgc2lnID0gc2lnbWFzW2lkeF0udW5zcXVlZXplKDEpXG4gICAgeF90aWxkZSA9IHggKyB0b3JjaC5yYW5kbl9saWtlKHgpICogc2lnXG4gICAgdGFyZ2V0ID0gKHggLSB4X3RpbGRlKSAvIChzaWcgKiogMilcbiAgICBwcmVkID0gbmV0KHhfdGlsZGUsIGlkeClcbiAgICByZXR1cm4gKChzaWcgKiogMikgKiAocHJlZCAtIHRhcmdldCkucG93KDIpKS5tZWFuKClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbnNpZ21hcyA9IHRvcmNoLnRlbnNvcihucC5nZW9tc3BhY2UoMS4wLCAwLjAxLCAxMCksIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG5uY3NubmV0ID0gTkNTTlNjb3JlTmV0KClcbm9wdCA9IHRvcmNoLm9wdGltLkFkYW0obmNzbm5ldC5wYXJhbWV0ZXJzKCksIGxyPTNlLTQpXG5kYXRhID0gdG9yY2guY2F0KFt0b3JjaC5yYW5kbig1MDAsMikqMC4zKzIuMCwgdG9yY2gucmFuZG4oNTAwLDIpKjAuMy0yLjBdKVxuZm9yIHN0ZXAgaW4gcmFuZ2UoNDAwKTpcbiAgICB4ID0gZGF0YVt0b3JjaC5yYW5kaW50KGxlbihkYXRhKSwgKDEyOCwpKV1cbiAgICBsb3NzID0gbmNzbl9sb3NzKG5jc25uZXQsIHgsIHNpZ21hcylcbiAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgIGlmIHN0ZXAgJSAxMDAgPT0gMDpcbiAgICAgICAgcHJpbnQoZlx1MDAyN1N0ZXAge3N0ZXB9OiBOQ1NOIGxvc3MgPSB7bG9zcy5pdGVtKCk6LjVmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYW5nZXZpbiBEeW5hbWljcyBTYW1wbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW5uZWFsZWQgTGFuZ2V2aW4gZHluYW1pY3Mgc2FtcGxlcyBmcm9tIHBfZGF0YSh4KSB1c2luZyB0aGUgc2NvcmUuIFN0YXJ0aW5nIGZyb20geF8wIH4gTigwLCDPg18xwrJJKSwgZm9yIGVhY2ggbGV2ZWwgbCBydW4gSyBzdGVwczogeF97aysxfSA9IHhfayArICjOsV9sLzIpwrdzX864KHhfayzPg19sKSArIOKIms6xX2zCt861X2sgd2hlcmUgzrFfbCA9IM61wrcoz4NfbC/Pg19MKcKyIGtlZXBzIHNpZ25hbC10by1ub2lzZSBjb25zdGFudCBhY3Jvc3MgbGV2ZWxzLiBVbmRlciBjb3JyZWN0IHNjb3JlIGVzdGltYXRpb24sIHRoZSBzdGF0aW9uYXJ5IGRpc3RyaWJ1dGlvbiBhdCBlYWNoIGxldmVsIGlzIHBfe8+DX2x9KHgpIOKAlCBhIHNtb290aGVkIHZlcnNpb24gb2YgcF9kYXRhLiBBcyDPg19sIOKGkiAwIGFjcm9zcyBMIGxldmVscywgdGhlIGNoYWluIGNvbnZlcmdlcyB0byBzYW1wbGVzIGZyb20gcF9kYXRhKHgpLiBUeXBpY2FsIHNldHRpbmdzOiBMPTEwIG5vaXNlIGxldmVscywgSz0xMDAgTGFuZ2V2aW4gc3RlcHMgcGVyIGxldmVsLCDOtT0yw5cxMOKBu+KBtS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuQHRvcmNoLm5vX2dyYWQoKVxuZGVmIGFubmVhbGVkX2xhbmdldmluKHNjb3JlX25ldCwgc2lnbWFzLCBuX3NhbXBsZXM9NjQsXG4gICAgICAgICAgICAgICAgICAgICAgZGF0YV9kaW09MiwgSz01MCwgc3RlcF9scj0yZS01KTpcbiAgICBcIlwiXCJBbm5lYWxlZCBMYW5nZXZpbjogbGFyZ2Ugc2lnbWEgLVx1MDAzZSBzbWFsbCBzaWdtYSwgSyBzdGVwcyBlYWNoLlwiXCJcIlxuICAgIHggPSB0b3JjaC5yYW5kbihuX3NhbXBsZXMsIGRhdGFfZGltKSAqIGZsb2F0KHNpZ21hc1swXSlcbiAgICBmb3IgbCwgc2lnbWEgaW4gZW51bWVyYXRlKHNpZ21hcyk6XG4gICAgICAgIHNpZ21hX2lkeCA9IHRvcmNoLmZ1bGwoKG5fc2FtcGxlcywpLCBsLCBkdHlwZT10b3JjaC5sb25nKVxuICAgICAgICBhbHBoYSA9IHN0ZXBfbHIgKiAoZmxvYXQoc2lnbWEpIC8gZmxvYXQoc2lnbWFzWy0xXSkpICoqIDJcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2UoSyk6XG4gICAgICAgICAgICBzY29yZSA9IHNjb3JlX25ldCh4LCBzaWdtYV9pZHgpXG4gICAgICAgICAgICB4ID0geCArIChhbHBoYSAvIDIpICogc2NvcmUgKyAoYWxwaGEgKiogMC41KSAqIHRvcmNoLnJhbmRuX2xpa2UoeClcbiAgICByZXR1cm4geFxuXG50b3JjaC5tYW51YWxfc2VlZCg3KVxuc2FtcGxlcyA9IGFubmVhbGVkX2xhbmdldmluKG5jc25uZXQsIHNpZ21hcywgbl9zYW1wbGVzPTIwMCwgSz04MClcbm5lYXJfcG9zID0gKHNhbXBsZXNbOiwgMF0gXHUwMDNlIDEuMCkuZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG5uZWFyX25lZyA9IChzYW1wbGVzWzosIDBdIFx1MDAzYyAtMS4wKS5mbG9hdCgpLm1lYW4oKS5pdGVtKClcbnByaW50KGZcdTAwMjdNb2RlIGNvdmVyYWdlOiArMiByZWdpb249e25lYXJfcG9zOi4xJX0sIC0yIHJlZ2lvbj17bmVhcl9uZWc6LjElfVx1MDAyNylcbnByaW50KGZcdTAwMjdTYW1wbGUgbWVhbiB4OiB7c2FtcGxlc1s6LDBdLm1lYW4oKTouM2Z9ICAoZXhwZWN0ZWQgfjAsIGJpbW9kYWwpXHUwMDI3KVxucHJpbnQoZlx1MDAyN1NhbXBsZSBzdGQgIHg6IHtzYW1wbGVzWzosMF0uc3RkKCk6LjNmfSAgIChleHBlY3RlZCB+MiwgdHdvIG1vZGVzIGF0ICstMilcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29ubmVjdGlvbiB0byBERFBNIOKAlCBlcHNpbG9uLVByZWRpY3Rpb24gYXMgU2NvcmUgRXN0aW1hdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gRERQTSwgeF90ID0g4oia4b6xX3TCt3hfMCArIOKImigx4oiS4b6xX3QpwrfOtSB3aXRoIM61IH4gTigwLEkpLiBUaGUgc2NvcmUgb2YgdGhlIG1hcmdpbmFsIHBfdCh4X3QpIGlzIOKIh197eF90fSBsb2cgcF90KHhfdCkgPSDiiJLOtS/iiJooMeKIkuG+sV90KS4gQSBuZXR3b3JrIHRoYXQgcHJlZGljdHMgzrUgZnJvbSB4X3QgdGhlcmVmb3JlIGltcGxpY2l0bHkgZXN0aW1hdGVzIHRoZSBzY29yZTogc1/OuCh4X3QsdCkgPSDiiJLOtV/OuCh4X3QsdCkv4oiaKDHiiJLhvrFfdCkuIFRoZSBERFBNIHNpbXBsZSBsb3NzIOKAls61X864KHhfdCx0KSDiiJIgzrXigJbCsiBpcyBhIERTTSBvYmplY3RpdmUgd2l0aCB0aGUgz4PCsi13ZWlnaHRpbmcgYWJzb3JiZWQgaW50byB0aGUgbm9pc2Ugc2NoZWR1bGUuIEV2ZXJ5IHRyYWluZWQgRERQTSBpcyBzaW11bHRhbmVvdXNseSBhIHNjb3JlIG5ldHdvcmsg4oCUIG5vIGFyY2hpdGVjdHVyYWwgY2hhbmdlIHJlcXVpcmVkIHRvIGFwcGx5IHNjb3JlLWJhc2VkIHNhbXBsZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbWFrZV9hbHBoYV9iYXIoVD0xMDAwLCBiZXRhX3N0YXJ0PTFlLTQsIGJldGFfZW5kPTAuMDIpOlxuICAgIGJldGFzID0gdG9yY2gubGluc3BhY2UoYmV0YV9zdGFydCwgYmV0YV9lbmQsIFQpXG4gICAgcmV0dXJuIHRvcmNoLmN1bXByb2QoMS4wIC0gYmV0YXMsIGRpbT0wKVxuXG5kZWYgZXBzX3RvX3Njb3JlKGVwc19wcmVkLCB0LCBhbHBoYV9iYXIpOlxuICAgIFwiXCJcInNfdGhldGEoeF90LCB0KSA9IC1lcHNfdGhldGEoeF90LCB0KSAvIHNxcnQoMSAtIGFscGhhX2Jhclt0XSlcIlwiXCJcbiAgICBhYnQgPSBhbHBoYV9iYXJbdF0udmlldygtMSwgMSlcbiAgICByZXR1cm4gLWVwc19wcmVkIC8gdG9yY2guc3FydCgxLjAgLSBhYnQpXG5cbmRlZiBzY29yZV90b19lcHMoc2NvcmUsIHQsIGFscGhhX2Jhcik6XG4gICAgYWJ0ID0gYWxwaGFfYmFyW3RdLnZpZXcoLTEsIDEpXG4gICAgcmV0dXJuIC1zY29yZSAqIHRvcmNoLnNxcnQoMS4wIC0gYWJ0KVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuYWxwaGFfYmFyID0gbWFrZV9hbHBoYV9iYXIoVD0xMDAwKVxuQiwgRCA9IDgsIDE2XG50ID0gdG9yY2gucmFuZGludCgwLCAxMDAwLCAoQiwpKVxuZXBzID0gdG9yY2gucmFuZG4oQiwgRClcbnNjb3JlID0gZXBzX3RvX3Njb3JlKGVwcywgdCwgYWxwaGFfYmFyKVxuZXBzX3J0ID0gc2NvcmVfdG9fZXBzKHNjb3JlLCB0LCBhbHBoYV9iYXIpXG5wcmludChmXHUwMDI3Um91bmQtdHJpcCBlcnJvcjogeyhlcHMgLSBlcHNfcnQpLmFicygpLm1heCgpOi4yZX0gIChzaG91bGQgYmUgfjApXHUwMDI3KVxucHJpbnQoXHUwMDI3U2NvcmUgbWFnbml0dWRlIGF0IGRpZmZlcmVudCBub2lzZSBsZXZlbHM6XHUwMDI3KVxuZm9yIHRfdmFsIGluIFs5OTksIDc1MCwgNTAwLCAyNTAsIDUwXTpcbiAgICB0dCA9IHRvcmNoLmZ1bGwoKDEsKSwgdF92YWwpXG4gICAgbWFnID0gZXBzX3RvX3Njb3JlKHRvcmNoLm9uZXMoMSwgRCksIHR0LCBhbHBoYV9iYXIpLm5vcm0oKS5pdGVtKClcbiAgICBwcmludChmXHUwMDI3ICB0PXt0X3ZhbDo0ZH06IHNjb3JlX25vcm0gPSB7bWFnOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU0RFIEZvcm11bGF0aW9uIOKAlCBVbmlmeWluZyBBbGwgRGlmZnVzaW9uIE1vZGVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU29uZyBldCBhbC4gKDIwMjEpIHNob3dlZCBldmVyeSBkaWZmdXNpb24gcHJvY2VzcyBpcyBhIHNwZWNpYWwgY2FzZSBvZiBhIGZvcndhcmQgU0RFOiBkeCA9IGYoeCx0KWR0ICsgZyh0KWRXLiBUaGUgcmV2ZXJzZSBTREUgaXMgZHggPSBbZih4LHQpIOKIkiBnKHQpwrJzX864KHgsdCldZHQgKyBnKHQpZFfMhC4gRERQTSB1c2VzIFZQLVNERSAodmFyaWFuY2UtcHJlc2VydmluZywgbGluZWFyIM6yIHNjaGVkdWxlKTsgTkNTTiB1c2VzIFZFLVNERSAodmFyaWFuY2UtZXhwbG9kaW5nLCBnZW9tZXRyaWMgz4Mgc2VxdWVuY2UpLiBTZXR0aW5nIHRoZSBkaWZmdXNpb24gdGVybSB0byB6ZXJvIGdpdmVzIHRoZSBwcm9iYWJpbGl0eSBmbG93IE9ERSDigJQgYSBkZXRlcm1pbmlzdGljIHNhbXBsZXIgZXF1aXZhbGVudCB0byBERElNLiBBbnkgbnVtZXJpY2FsIE9ERS9TREUgc29sdmVyIGNhbiBiZSBwbHVnZ2VkIGluIG9uY2Ugc1/OuCBpcyBsZWFybmVkLCBlbmFibGluZyBmbGV4aWJsZSBzcGVlZC1xdWFsaXR5IHRyYWRlb2ZmcyB3aXRob3V0IHJldHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2NvcmUgTWF0Y2hpbmcgTWV0aG9kcyBDb21wYXJlZCJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJFc3RpbWFuZCIsIkxvc3MgZm9ybSIsIk5vaXNlIHNjaGVkdWxlIiwiU2FtcGxpbmciXSwicm93cyI6W1siRXhwbGljaXQgU00gKEh5dsOkcmluZW4gMjAwNSkiLCLiiIdfeCBsb2cgcCh4KSIsInRyKOKIh3NfzrgpICsgwr3igJZzX8644oCWwrIgIOKAlCBubyBwKHgpIHJlcXVpcmVkIiwiTm9uZSAoY2xlYW4gZGF0YSkiLCJMYW5nZXZpbiBkeW5hbWljcyJdLFsiRFNNIChWaW5jZW50IDIwMTEpIiwiKHjiiJJ4zIMpL8+DwrIgIOKAlCBjb25kaXRpb25hbCBzY29yZSIsIuKAlnNfzrgoeMyDKSDiiJIgKHjiiJJ4zIMpL8+DwrLigJbCsiAg4oCUIEphY29iaWFuLWZyZWUiLCJTaW5nbGUgZml4ZWQgz4MiLCJMYW5nZXZpbiBkeW5hbWljcyJdLFsiTkNTTiAoU29uZyBcdTAwMjYgRXJtb24gMjAxOSkiLCJzX864KHgsz4NfbCkgYWNyb3NzIEwgbGV2ZWxzIiwiV2VpZ2h0ZWQgRFNNOiDOo19sIM+DX2zCsuKAlnNfzrgoeMyDLGwp4oiSdGFyZ2V04oCWwrIiLCJHZW9tZXRyaWMgz4NfMVx1MDAzZeKAplx1MDAzZc+DX0wiLCJBbm5lYWxlZCBMYW5nZXZpbiAoSyBzdGVwcy9sZXZlbCkiXSxbIkREUE0gKEhvIGV0IGFsLiAyMDIwKSIsIs61X864KHhfdCx0KSDiiaEg4oiSc2NvcmXCt+KImigx4oiS4b6xX3QpIiwiU2ltcGxlOiDigJbOtV/OuCh4X3QsdCniiJLOteKAlsKyIiwiTGluZWFyIM6yIHNjaGVkdWxlLCBUPTEwMDAiLCJBbmNlc3RyYWwgc2FtcGxpbmcgKFQgcmV2ZXJzZSBzdGVwcykiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiU2NvcmUgRXN0aW1hdGlvbiBpcyB0aGUgQ29yZSBvZiBBbGwgRGlmZnVzaW9uIE1vZGVscyIsImNvbnRlbnQiOiJFdmVyeSBtb2Rlcm4gZ2VuZXJhdGl2ZSBkaWZmdXNpb24gc3lzdGVtIOKAlCBERFBNLCBsYXRlbnQgZGlmZnVzaW9uLCBFRE0sIGNvbnNpc3RlbmN5IG1vZGVscyDigJQgbGVhcm5zIGEgc2NvcmUgbmV0d29yayB1bmRlciB0aGUgaG9vZC4gQXJjaGl0ZWN0dXJlcyBkaWZmZXIgKFVOZXQsIERpVCwgVmlUKSBidXQgdGhlIHRyYWluaW5nIHNpZ25hbCBpcyBhbHdheXMgZGVub2lzaW5nLCB3aGljaCBpcyBEU00uIE1hc3RlcmluZyBzY29yZSBtYXRjaGluZyBnaXZlcyB5b3UgYSB1bmlmaWVkIGxlbnMgZm9yIHVuZGVyc3RhbmRpbmcgYW5kIGltcHJvdmluZyBhbnkgZGlmZnVzaW9uLWJhc2VkIGdlbmVyYXRvci4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNjb3JlID0g4oiHX3ggbG9nIHAoeCk6IHRoZSBub3JtYWxpemluZyBjb25zdGFudCBaIGNhbmNlbHMg4oCUIHNjb3JlIGlzIGNvbXB1dGFibGUgd2l0aG91dCBrbm93aW5nIFouIiwiRXhwbGljaXQgU00gcmVxdWlyZXMgYSBKYWNvYmlhbiB0cmFjZSAoTyhkKSBwYXNzZXMpOyBEU00gcmVwbGFjZXMgaXQgd2l0aCB0aGUgY2xvc2VkLWZvcm0gdGFyZ2V0ICh44oiSeMyDKS/Pg8KyLiIsIk5DU04gdHJhaW5zIGF0IEwgbm9pc2UgbGV2ZWxzOyBhbm5lYWxlZCBMYW5nZXZpbiBzd2VlcHMgY29hcnNlLXRvLWZpbmUsIHNvbHZpbmcgbG93LWRlbnNpdHkgZXN0aW1hdGlvbi4iLCJERFBNIGVwc2lsb24tcHJlZGljdGlvbiBpcyBzY29yZSBlc3RpbWF0aW9uIGluIGRpc2d1aXNlOiBzX864ID0g4oiSzrVfzrggLyDiiJooMeKIkuG+sV90KS4iLCJTREUgZnJhbWV3b3JrIHVuaWZpZXMgYWxsIG1ldGhvZHM6IFZQLVNERSAoRERQTSksIFZFLVNERSAoTkNTTiksIHByb2JhYmlsaXR5IGZsb3cgT0RFIChERElNKS4iLCJTbGljZWQgc2NvcmUgbWF0Y2hpbmcgYW5kIGRlbm9pc2luZyBkaWZmdXNpb24gcHJvYmFiaWxpc3RpYyBtb2RlbHMgY29udmVyZ2UgdG8gdGhlIHNhbWUgb2JqZWN0aXZlLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Score Matching and Score-Based Generative Models

Score-based generative models train a neural network to estimate the gradient of the log data density — the score function s(x) = ∇_x log p(x). This single principle unifies denoising score matching, noise-conditional score networks (NCSN), and DDPMs. Rather than approximating p(x) directly (which requires a tractable normalizing constant Z), score models approximate ∇_x log p(x), which cancels Z. A learned score field then drives iterative sampling via Langevin dynamics or reverse-time SDEs, enabling generation without likelihood evaluation.

## The Score Function

For a distribution p(x) = p̃(x)/Z, the score is s(x) = ∇_x log p(x) = ∇_x log p̃(x) — Z cancels in the gradient. The score is a vector field pointing toward higher-density regions. For a Gaussian p(x) = N(μ, σ²I) the score is (μ − x)/σ², a linear restoring force toward the mean. A neural score network s_θ(x) approximates this field across the entire data distribution, enabling gradient ascent on log p without ever computing the partition function.

## Explicit Score Matching (Hyvärinen 2005)

Hyvärinen (2005) showed the squared-error objective E[‖s_θ(x) − ∇_x log p(x)‖²] equals E[tr(∇_x s_θ(x)) + ½‖s_θ(x)‖²] via integration by parts — no p(x) needed. The trace term tr(∇_x s_θ(x)) requires O(d) backward passes for d-dimensional inputs. At image resolution 64×64 (d=12288), this is computationally intractable. Sliced score matching (Song et al. 2020) reduces cost via random projections, but denoising score matching (DSM) provides a cleaner solution with a closed-form target.

## Denoising Score Matching (Vincent 2011)

Vincent (2011) proved that training on corrupted inputs is equivalent to score matching. Given x̃ = x + σε with ε ~ N(0,I), the conditional score is ∇_{x̃} log p(x̃|x) = (x − x̃)/σ² — computable without Jacobian traces. The DSM loss L = E[‖s_θ(x̃) − (x−x̃)/σ²‖²] trains the score network to predict the direction from any noisy point back toward clean data. This is precisely what DDPMs do: predicting noise ε_θ ≈ ε is equivalent to estimating the score s_θ(x̃) ≈ −ε/σ, just scaled differently.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ScoreNet(nn.Module):
    def __init__(self, data_dim=2, hidden=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(data_dim, hidden), nn.SiLU(),
            nn.Linear(hidden, hidden), nn.SiLU(),
            nn.Linear(hidden, data_dim)
        )
    def forward(self, x):
        return self.net(x)

def dsm_loss(score_net, x, sigma=0.5):
    """DSM: s_theta(x_tilde) approx (x - x_tilde) / sigma^2."""
    noise = torch.randn_like(x) * sigma
    x_tilde = x + noise
    target = (x - x_tilde) / (sigma ** 2)
    return F.mse_loss(score_net(x_tilde), target)

torch.manual_seed(42)
net = ScoreNet()
opt = torch.optim.Adam(net.parameters(), lr=1e-3)
data = torch.cat([torch.randn(512, 2) + 2.0, torch.randn(512, 2) - 2.0])
for step in range(300):
    x = data[torch.randint(len(data), (64,))]
    loss = dsm_loss(net, x, sigma=0.4)
    opt.zero_grad(); loss.backward(); opt.step()
    if step % 100 == 0:
        print(f'Step {step}: DSM loss = {loss.item():.4f}')
```

## Noise Conditional Score Networks (NCSN)

Song & Ermon (2019) extended DSM to multiple noise levels. NCSN trains s_θ(x, σ) over a geometric sequence σ_1 > ... > σ_L (e.g. σ_1=1.0 to σ_L=0.01, L=10). The weighted loss Σ_l σ_l² · E[‖s_θ(x̃,σ_l) − (x−x̃)/σ_l²‖²] balances scale contributions — the σ_l² weight makes each term dimensionally uniform. Large σ guides from broad noise; small σ refines fine structure. Multi-scale training also solves the score estimation problem in low-density regions, where single-σ methods produce noisy, unreliable estimates.

```python
import torch
import torch.nn as nn
import numpy as np

class NCSNScoreNet(nn.Module):
    def __init__(self, data_dim=2, hidden=128, n_sigmas=10):
        super().__init__()
        self.sigma_embed = nn.Embedding(n_sigmas, 16)
        self.net = nn.Sequential(
            nn.Linear(data_dim + 16, hidden), nn.SiLU(),
            nn.Linear(hidden, hidden), nn.SiLU(),
            nn.Linear(hidden, data_dim)
        )
    def forward(self, x, sigma_idx):
        emb = self.sigma_embed(sigma_idx)
        return self.net(torch.cat([x, emb], dim=-1))

def ncsn_loss(net, x, sigmas):
    B = x.size(0)
    idx = torch.randint(0, len(sigmas), (B,))
    sig = sigmas[idx].unsqueeze(1)
    x_tilde = x + torch.randn_like(x) * sig
    target = (x - x_tilde) / (sig ** 2)
    pred = net(x_tilde, idx)
    return ((sig ** 2) * (pred - target).pow(2)).mean()

torch.manual_seed(0)
sigmas = torch.tensor(np.geomspace(1.0, 0.01, 10), dtype=torch.float32)
ncsnnet = NCSNScoreNet()
opt = torch.optim.Adam(ncsnnet.parameters(), lr=3e-4)
data = torch.cat([torch.randn(500,2)*0.3+2.0, torch.randn(500,2)*0.3-2.0])
for step in range(400):
    x = data[torch.randint(len(data), (128,))]
    loss = ncsn_loss(ncsnnet, x, sigmas)
    opt.zero_grad(); loss.backward(); opt.step()
    if step % 100 == 0:
        print(f'Step {step}: NCSN loss = {loss.item():.5f}')
```

## Langevin Dynamics Sampling

Annealed Langevin dynamics samples from p_data(x) using the score. Starting from x_0 ~ N(0, σ_1²I), for each level l run K steps: x_{k+1} = x_k + (α_l/2)·s_θ(x_k,σ_l) + √α_l·ε_k where α_l = ε·(σ_l/σ_L)² keeps signal-to-noise constant across levels. Under correct score estimation, the stationary distribution at each level is p_{σ_l}(x) — a smoothed version of p_data. As σ_l → 0 across L levels, the chain converges to samples from p_data(x). Typical settings: L=10 noise levels, K=100 Langevin steps per level, ε=2×10⁻⁵.

```python
import torch
import numpy as np

@torch.no_grad()
def annealed_langevin(score_net, sigmas, n_samples=64,
                      data_dim=2, K=50, step_lr=2e-5):
    """Annealed Langevin: large sigma -> small sigma, K steps each."""
    x = torch.randn(n_samples, data_dim) * float(sigmas[0])
    for l, sigma in enumerate(sigmas):
        sigma_idx = torch.full((n_samples,), l, dtype=torch.long)
        alpha = step_lr * (float(sigma) / float(sigmas[-1])) ** 2
        for _ in range(K):
            score = score_net(x, sigma_idx)
            x = x + (alpha / 2) * score + (alpha ** 0.5) * torch.randn_like(x)
    return x

torch.manual_seed(7)
samples = annealed_langevin(ncsnnet, sigmas, n_samples=200, K=80)
near_pos = (samples[:, 0] > 1.0).float().mean().item()
near_neg = (samples[:, 0] < -1.0).float().mean().item()
print(f'Mode coverage: +2 region={near_pos:.1%}, -2 region={near_neg:.1%}')
print(f'Sample mean x: {samples[:,0].mean():.3f}  (expected ~0, bimodal)')
print(f'Sample std  x: {samples[:,0].std():.3f}   (expected ~2, two modes at +-2)')
```

## Connection to DDPM — epsilon-Prediction as Score Estimation

In DDPM, x_t = √ᾱ_t·x_0 + √(1−ᾱ_t)·ε with ε ~ N(0,I). The score of the marginal p_t(x_t) is ∇_{x_t} log p_t(x_t) = −ε/√(1−ᾱ_t). A network that predicts ε from x_t therefore implicitly estimates the score: s_θ(x_t,t) = −ε_θ(x_t,t)/√(1−ᾱ_t). The DDPM simple loss ‖ε_θ(x_t,t) − ε‖² is a DSM objective with the σ²-weighting absorbed into the noise schedule. Every trained DDPM is simultaneously a score network — no architectural change required to apply score-based samplers.

```python
import torch
import numpy as np

def make_alpha_bar(T=1000, beta_start=1e-4, beta_end=0.02):
    betas = torch.linspace(beta_start, beta_end, T)
    return torch.cumprod(1.0 - betas, dim=0)

def eps_to_score(eps_pred, t, alpha_bar):
    """s_theta(x_t, t) = -eps_theta(x_t, t) / sqrt(1 - alpha_bar[t])"""
    abt = alpha_bar[t].view(-1, 1)
    return -eps_pred / torch.sqrt(1.0 - abt)

def score_to_eps(score, t, alpha_bar):
    abt = alpha_bar[t].view(-1, 1)
    return -score * torch.sqrt(1.0 - abt)

torch.manual_seed(0)
alpha_bar = make_alpha_bar(T=1000)
B, D = 8, 16
t = torch.randint(0, 1000, (B,))
eps = torch.randn(B, D)
score = eps_to_score(eps, t, alpha_bar)
eps_rt = score_to_eps(score, t, alpha_bar)
print(f'Round-trip error: {(eps - eps_rt).abs().max():.2e}  (should be ~0)')
print('Score magnitude at different noise levels:')
for t_val in [999, 750, 500, 250, 50]:
    tt = torch.full((1,), t_val)
    mag = eps_to_score(torch.ones(1, D), tt, alpha_bar).norm().item()
    print(f'  t={t_val:4d}: score_norm = {mag:.4f}')
```

## SDE Formulation — Unifying All Diffusion Models

Song et al. (2021) showed every diffusion process is a special case of a forward SDE: dx = f(x,t)dt + g(t)dW. The reverse SDE is dx = [f(x,t) − g(t)²s_θ(x,t)]dt + g(t)dW̄. DDPM uses VP-SDE (variance-preserving, linear β schedule); NCSN uses VE-SDE (variance-exploding, geometric σ sequence). Setting the diffusion term to zero gives the probability flow ODE — a deterministic sampler equivalent to DDIM. Any numerical ODE/SDE solver can be plugged in once s_θ is learned, enabling flexible speed-quality tradeoffs without retraining.

## Score Matching Methods Compared

| Method | Estimand | Loss form | Noise schedule | Sampling |
| --- | --- | --- | --- | --- |
| Explicit SM (Hyvärinen 2005) | ∇_x log p(x) | tr(∇s_θ) + ½‖s_θ‖²  — no p(x) required | None (clean data) | Langevin dynamics |
| DSM (Vincent 2011) | (x−x̃)/σ²  — conditional score | ‖s_θ(x̃) − (x−x̃)/σ²‖²  — Jacobian-free | Single fixed σ | Langevin dynamics |
| NCSN (Song & Ermon 2019) | s_θ(x,σ_l) across L levels | Weighted DSM: Σ_l σ_l²‖s_θ(x̃,l)−target‖² | Geometric σ_1>…>σ_L | Annealed Langevin (K steps/level) |
| DDPM (Ho et al. 2020) | ε_θ(x_t,t) ≡ −score·√(1−ᾱ_t) | Simple: ‖ε_θ(x_t,t)−ε‖² | Linear β schedule, T=1000 | Ancestral sampling (T reverse steps) |

> **Score Estimation is the Core of All Diffusion Models**: Every modern generative diffusion system — DDPM, latent diffusion, EDM, consistency models — learns a score network under the hood. Architectures differ (UNet, DiT, ViT) but the training signal is always denoising, which is DSM. Mastering score matching gives you a unified lens for understanding and improving any diffusion-based generator.

- Score = ∇_x log p(x): the normalizing constant Z cancels — score is computable without knowing Z.
- Explicit SM requires a Jacobian trace (O(d) passes); DSM replaces it with the closed-form target (x−x̃)/σ².
- NCSN trains at L noise levels; annealed Langevin sweeps coarse-to-fine, solving low-density estimation.
- DDPM epsilon-prediction is score estimation in disguise: s_θ = −ε_θ / √(1−ᾱ_t).
- SDE framework unifies all methods: VP-SDE (DDPM), VE-SDE (NCSN), probability flow ODE (DDIM).
- Sliced score matching and denoising diffusion probabilistic models converge to the same objective.

---

