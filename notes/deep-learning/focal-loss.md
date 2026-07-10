---
title: "Focal Loss — Hard Example Mining for Class Imbalance"
slug: "focal-loss"
description: "Derive focal loss from binary cross-entropy, visualize the γ focusing effect, implement RetinaNet-style detection loss, and compare CE vs OHEM vs focal vs ASL for imbalanced training."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2xhc3MgaW1iYWxhbmNlIGlzIGEgZnVuZGFtZW50YWwgY2hhbGxlbmdlIGluIG9iamVjdCBkZXRlY3Rpb246IGEgc2luZ2xlIGltYWdlIG1heSBjb250YWluIDHigJMxMCBmb3JlZ3JvdW5kIG9iamVjdHMgYnV0IDEwLDAwMOKAkzEwMCwwMDAgYmFja2dyb3VuZCBhbmNob3IgYm94ZXMuIFN0YW5kYXJkIGNyb3NzLWVudHJvcHkgbG9zcyBpcyBvdmVyd2hlbG1lZCBieSBlYXN5IG5lZ2F0aXZlIGV4YW1wbGVzIOKAlCBlYWNoIGluZGl2aWR1YWwgZWFzeSBuZWdhdGl2ZSBjb250cmlidXRlcyBhIHRpbnkgbG9zcywgYnV0IHRoZWlyIHNoZWVyIG51bWJlciBkb21pbmF0ZXMgdHJhaW5pbmcuIE9ubGluZSBIYXJkIEV4YW1wbGUgTWluaW5nIChPSEVNKSBhZGRyZXNzZXMgdGhpcyBieSBzYW1wbGluZyBvbmx5IHRoZSBoaWdoZXN0LWxvc3MgZXhhbXBsZXMsIGJ1dCBpdCByZXF1aXJlcyBjb21wbGV4IHNhbXBsaW5nIGxvZ2ljLiBGb2NhbCBMb3NzIChMaW4gZXQgYWwuIDIwMTcpIHNvbHZlcyB0aGUgc2FtZSBwcm9ibGVtIGVsZWdhbnRseSBieSByZXdlaWdodGluZyBlYWNoIGV4YW1wbGVcdTAwMjdzIGxvc3MgYmFzZWQgb24gaXRzIGNsYXNzaWZpY2F0aW9uIGNvbmZpZGVuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2xhc3MgSW1iYWxhbmNlIGluIE9iamVjdCBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlR3by1zdGFnZSBkZXRlY3RvcnMgKEZhc3RlciBSLUNOTikgdXNlIGEgcmVnaW9uIHByb3Bvc2FsIG5ldHdvcmsgdG8gZmlsdGVyIG1vc3QgYmFja2dyb3VuZCBhbmNob3JzIGJlZm9yZSB0aGUgY2xhc3NpZmljYXRpb24gc3RhZ2Ug4oCUIHRoZSBjbGFzcyBpbWJhbGFuY2UgcmF0aW8gaW4gdGhlIHNlY29uZCBzdGFnZSBpcyBtYW5hZ2VhYmxlIChyb3VnaGx5IDE6MyBmb3JlZ3JvdW5kIHRvIGJhY2tncm91bmQpLiBPbmUtc3RhZ2UgZGV0ZWN0b3JzIChTU0QsIFlPTE8sIFJldGluYU5ldCkgY2xhc3NpZnkgYWxsIGFuY2hvcnMgc2ltdWx0YW5lb3VzbHksIGZhY2luZyByYXRpb3Mgb2YgMToxMDAwIG9yIHdvcnNlLiBPSEVNIChPbmxpbmUgSGFyZCBFeGFtcGxlIE1pbmluZykgc2VsZWN0cyB0aGUgdG9wLWsgaGlnaGVzdC1sb3NzIGFuY2hvcnMgcGVyIGltYWdlIGR1cmluZyB0cmFpbmluZywgZGlzY2FyZGluZyBlYXN5IG5lZ2F0aXZlcy4gQnV0IE9IRU0gcmVxdWlyZXMgc29ydGluZyBhbGwgYW5jaG9yIGxvc3NlcyBhbmQgaXMgc2Vuc2l0aXZlIHRvIHRoZSBtaW5pbmcgcmF0aW8gaHlwZXJwYXJhbWV0ZXIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRm9jYWwgTG9zcyBGb3JtdWxhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb2NhbCBMb3NzIG1vZGlmaWVzIGJpbmFyeSBjcm9zcy1lbnRyb3B5IGJ5IGFkZGluZyBhIG1vZHVsYXRpbmcgZmFjdG9yLiBEZWZpbmUgcOKCnCA9IHAgaWYgeT0xIGVsc2UgKDHiiJJwKSDigJQgdGhlIHByZWRpY3RlZCBwcm9iYWJpbGl0eSBmb3IgdGhlIHRydWUgY2xhc3MuIFN0YW5kYXJkIEJDRTogQ0UocOKCnCkgPSDiiJJsb2cocOKCnCkuIEZvY2FsIExvc3M6IEZMKHDigpwpID0g4oiSKDHiiJJw4oKcKV7OsyDCtyBsb2cocOKCnCkuIFRoZSBtb2R1bGF0aW5nIGZhY3RvciAoMeKIknDigpwpXs6zOiB3aGVuIHRoZSBleGFtcGxlIGlzIGVhc3kgKHDigpwg4oaSIDEpLCAoMeKIknDigpwpXs6zIOKGkiAwLCBzdXBwcmVzc2luZyB0aGUgbG9zcyBjb250cmlidXRpb24uIFdoZW4gdGhlIGV4YW1wbGUgaXMgaGFyZCAocOKCnCDihpIgMCksICgx4oiScOKCnClezrMg4oaSIDEsIGtlZXBpbmcgZnVsbCBsb3NzIHdlaWdodC4gzrM9MiBpcyB0aGUgc3RhbmRhcmQgY2hvaWNlLiBOb3RlIHRoYXQgQ0UgaXMgZm9jYWwgbG9zcyB3aXRoIM6zPTAuIFRoZSBjbGFzcy1iYWxhbmNlZCB2ZXJzaW9uIGFkZHMgzrE6IEZMKHDigpwpID0g4oiSzrHigpwoMeKIknDigpwpXs6zIGxvZyhw4oKcKSB3aGVyZSDOseKCnCA9IM6xIGlmIHk9MSBlbHNlICgx4oiSzrEpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGZvY2FsX2xvc3NfYmluYXJ5KGxvZ2l0cywgdGFyZ2V0cywgZ2FtbWE9Mi4wLCBhbHBoYT0wLjI1LCByZWR1Y3Rpb249XHUwMDI3bWVhblx1MDAyNyk6XG4gICAgIyBCaW5hcnkgZm9jYWwgbG9zcyAoc2lnbW9pZC1iYXNlZCkgZm9yIHNpbmdsZS1jbGFzcyBkZXRlY3Rpb25cbiAgICBwcm9icyA9IHRvcmNoLnNpZ21vaWQobG9naXRzKVxuICAgICMgcF90OiBwcmVkaWN0ZWQgcHJvYmFiaWxpdHkgZm9yIHRoZSB0cnVlIGNsYXNzXG4gICAgcF90ID0gdG9yY2gud2hlcmUodGFyZ2V0cyA9PSAxLCBwcm9icywgMSAtIHByb2JzKVxuICAgICMgYWxwaGFfdDogY2xhc3Mgd2VpZ2h0XG4gICAgYWxwaGFfdCA9IHRvcmNoLndoZXJlKHRhcmdldHMgPT0gMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgdG9yY2guZnVsbF9saWtlKHByb2JzLCBhbHBoYSksXG4gICAgICAgICAgICAgICAgICAgICAgICAgIHRvcmNoLmZ1bGxfbGlrZShwcm9icywgMSAtIGFscGhhKSlcbiAgICAjIEZvY2FsIG1vZHVsYXRpb246IHN1cHByZXNzIGVhc3kgZXhhbXBsZXNcbiAgICBmb2NhbF93ZWlnaHQgPSAoMSAtIHBfdCkucG93KGdhbW1hKVxuICAgICMgQkNFIHdpdGggbnVtZXJpY2FsbHkgc3RhYmxlIGxvZ1xuICAgIGJjZSA9IEYuYmluYXJ5X2Nyb3NzX2VudHJvcHlfd2l0aF9sb2dpdHMoXG4gICAgICAgIGxvZ2l0cywgdGFyZ2V0cy5mbG9hdCgpLCByZWR1Y3Rpb249XHUwMDI3bm9uZVx1MDAyNylcbiAgICBsb3NzID0gYWxwaGFfdCAqIGZvY2FsX3dlaWdodCAqIGJjZVxuICAgIGlmIHJlZHVjdGlvbiA9PSBcdTAwMjdtZWFuXHUwMDI3OlxuICAgICAgICByZXR1cm4gbG9zcy5tZWFuKClcbiAgICBlbGlmIHJlZHVjdGlvbiA9PSBcdTAwMjdzdW1cdTAwMjc6XG4gICAgICAgIHJldHVybiBsb3NzLnN1bSgpXG4gICAgcmV0dXJuIGxvc3NcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG4jIFNpbXVsYXRlOiAxMCBwb3NpdGl2ZSBhbmNob3JzLCA5OTkwIG5lZ2F0aXZlIGFuY2hvcnNcbmxvZ2l0cyA9IHRvcmNoLmNhdChbdG9yY2gucmFuZG4oMTApICsgMS4wLCAgICMgcG9zaXRpdmVzXG4gICAgICAgICAgICAgICAgICAgIHRvcmNoLnJhbmRuKDk5OTApIC0gMi4wXSkgICMgZWFzeSBuZWdhdGl2ZXNcbnRhcmdldHMgPSB0b3JjaC5jYXQoW3RvcmNoLm9uZXMoMTApLCB0b3JjaC56ZXJvcyg5OTkwKV0pXG5cbmZsID0gZm9jYWxfbG9zc19iaW5hcnkobG9naXRzLCB0YXJnZXRzLCBnYW1tYT0yLjAsIGFscGhhPTAuMjUpXG5jZSA9IEYuYmluYXJ5X2Nyb3NzX2VudHJvcHlfd2l0aF9sb2dpdHMobG9naXRzLCB0YXJnZXRzLmZsb2F0KCkpXG5wcmludChmXHUwMDI3Q3Jvc3MtZW50cm9weSBsb3NzOiB7Y2UuaXRlbSgpOi42Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3Rm9jYWwgbG9zcyAoZz0yKTogICB7ZmwuaXRlbSgpOi42Zn1cdTAwMjcpXG5wcmludChcdTAwMjdGb2NhbCBsb3NzIGlzIG11Y2ggbG93ZXIgYmVjYXVzZSBlYXN5IG5lZ2F0aXZlcyBhcmUgc3VwcHJlc3NlZC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWZmZWN0IG9mIHRoZSBGb2N1c2luZyBQYXJhbWV0ZXIgzrMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBwYXJhbWV0ZXIgzrMgY29udHJvbHMgaG93IGFnZ3Jlc3NpdmVseSBlYXN5IGV4YW1wbGVzIGFyZSBkb3duLXdlaWdodGVkLiBBdCDOsz0wLCBGTCA9IENFIChubyBzdXBwcmVzc2lvbikuIEF0IM6zPTEsIGVhc3kgZXhhbXBsZXMgKHDigpw9MC45KSByZWNlaXZlIHdlaWdodCAoMeKIkjAuOSleMSA9IDAuMSDigJQgMTAlIG9mIHRoZWlyIENFIGxvc3MuIEF0IM6zPTIgKHN0YW5kYXJkKSwgdGhleSByZWNlaXZlICgx4oiSMC45KV4yID0gMC4wMSDigJQgMSUgb2YgdGhlaXIgQ0UgbG9zcy4gQXQgzrM9NSwgdGhleSByZWNlaXZlICgx4oiSMC45KV41IOKJiCAwLjAwMDAxIOKAlCBlZmZlY3RpdmVseSB6ZXJvLiBIYXJkIGV4YW1wbGVzIChw4oKcPTAuMikgcmVjZWl2ZTogzrM9MSDihpIgMC44w5csIM6zPTIg4oaSIDAuNjTDlywgzrM9NSDihpIgMC4zM8OXLiBUaGUgcmF0aW8gb2YgaGFyZC10by1lYXN5IHdlaWdodGluZyBncm93cyByYXBpZGx5IHdpdGggzrMsIGNvbmNlbnRyYXRpbmcgdHJhaW5pbmcgb24gdGhlIGhhcmRlc3QgZXhhbXBsZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5cbmRlZiBmb2NhbF93ZWlnaHQocF90LCBnYW1tYSk6XG4gICAgcmV0dXJuICgxIC0gcF90KSAqKiBnYW1tYVxuXG5wX3ZhbHVlcyA9IG5wLmxpbnNwYWNlKDAuMDEsIDAuOTksIDEwMClcbnByaW50KGZcdTAwMjd7XCJwX3RcIjpcdTAwM2U2fSB7XCJDRVwiOlx1MDAzYzEwfSB7XCJGTChnPTEpXCI6XHUwMDNjMTJ9IHtcIkZMKGc9MilcIjpcdTAwM2MxMn0ge1wiRkwoZz01KVwiOlx1MDAzYzEyfVx1MDAyNylcbmZvciBwIGluIFswLjEsIDAuMywgMC41LCAwLjcsIDAuOSwgMC45OV06XG4gICAgY2UgICA9IC1ucC5sb2cocClcbiAgICBmbDEgID0gZm9jYWxfd2VpZ2h0KHAsIDEpICogY2VcbiAgICBmbDIgID0gZm9jYWxfd2VpZ2h0KHAsIDIpICogY2VcbiAgICBmbDUgID0gZm9jYWxfd2VpZ2h0KHAsIDUpICogY2VcbiAgICBwcmludChmXHUwMDI3e3A6XHUwMDNlNi4yZn0ge2NlOlx1MDAzYzEwLjRmfSB7ZmwxOlx1MDAzYzEyLjRmfSB7ZmwyOlx1MDAzYzEyLjRmfSB7Zmw1Olx1MDAzYzEyLjRmfVx1MDAyNylcblxucHJpbnQoXHUwMDI3XFxuLS0tIEhhcmQgKHA9MC4xKSB2cyBFYXN5IChwPTAuOSkgbG9zcyByYXRpbyBieSBnYW1tYSAtLS1cdTAwMjcpXG5mb3IgZyBpbiBbMCwgMSwgMiwgNV06XG4gICAgcmF0aW8gPSAoZm9jYWxfd2VpZ2h0KDAuMSwgZykgKiAoLW5wLmxvZygwLjEpKSkgLyBcXFxuICAgICAgICAgICAgKGZvY2FsX3dlaWdodCgwLjksIGcpICogKC1ucC5sb2coMC45KSkpXG4gICAgcHJpbnQoZlx1MDAyNyAgZ2FtbWE9e2d9OiBoYXJkL2Vhc3kgcmF0aW8gPSB7cmF0aW86LjFmfXhcdTAwMjcpXG5wcmludChcdTAwMjdcXG5IaWdoZXIgZ2FtbWEgLVx1MDAzZSBoYXJkZXIgZXhhbXBsZXMgZG9taW5hdGUgdHJhaW5pbmcgbW9yZSBzdHJvbmdseS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRm9jYWwgTG9zcyBpbiBPYmplY3QgRGV0ZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBSZXRpbmFOZXQsIHRoZSBjbGFzc2lmaWNhdGlvbiBzdWJuZXQgb3V0cHV0cyBCIMOXIEEgw5cgQyBzaWdtb2lkIGxvZ2l0cyAobm90IHNvZnRtYXgpLCB0cmVhdGluZyBlYWNoIGNsYXNzIGFzIGFuIGluZGVwZW5kZW50IGJpbmFyeSBjbGFzc2lmaWNhdGlvbi4gRm9jYWwgbG9zcyBpcyBhcHBsaWVkIHRvIGVhY2ggKGFuY2hvciwgY2xhc3MpIHBhaXIuIEFuY2hvcnMgd2l0aCBJb1Ug4omlIDAuNSB3aXRoIGFueSBncm91bmQtdHJ1dGggYm94IGFyZSBwb3NpdGl2ZTsgYW5jaG9ycyB3aXRoIElvVSBcdTAwM2MgMC40IGFyZSBuZWdhdGl2ZTsgYW5jaG9ycyBpbiB0aGUgYW1iaWd1b3VzIHJhbmdlIFswLjQsIDAuNSkgYXJlIGlnbm9yZWQgKHRhcmdldD0tMSkuIE9ubHkgcG9zaXRpdmUgYW5kIG5lZ2F0aXZlIGFuY2hvcnMgY29udHJpYnV0ZSB0byB0aGUgZm9jYWwgbG9zczsgaWdub3JlZCBhbmNob3JzIGFyZSBtYXNrZWQgb3V0LiBUaGUgdG90YWwgbG9zcyBpcyBub3JtYWxpemVkIGJ5IHRoZSBudW1iZXIgb2YgZm9yZWdyb3VuZCBhbmNob3JzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBSZXRpbmFOZXRGb2NhbExvc3Mobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZ2FtbWE9Mi4wLCBhbHBoYT0wLjI1KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZ2FtbWEgPSBnYW1tYVxuICAgICAgICBzZWxmLmFscGhhID0gYWxwaGFcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGNsc19sb2dpdHMsIGNsc190YXJnZXRzKTpcbiAgICAgICAgIyBjbHNfbG9naXRzOiAgKEIsIEEsIEMpIOKAlCBsb2dpdHMgcGVyIGFuY2hvciBwZXIgY2xhc3NcbiAgICAgICAgIyBjbHNfdGFyZ2V0czogKEIsIEEpICAgIOKAlCAtMT1pZ25vcmUsIDA9YmFja2dyb3VuZCwgMS4uQz1jbGFzc1xuICAgICAgICBCLCBBLCBDID0gY2xzX2xvZ2l0cy5zaGFwZVxuICAgICAgICBwcm9icyA9IHRvcmNoLnNpZ21vaWQoY2xzX2xvZ2l0cylcbiAgICAgICAgIyBCdWlsZCBvbmUtaG90IHRhcmdldHMgKGJhY2tncm91bmQgaGFzIGFsbC16ZXJvIHRhcmdldClcbiAgICAgICAgZmdfbWFzayA9IGNsc190YXJnZXRzIFx1MDAzZSAwXG4gICAgICAgIGJnX21hc2sgPSBjbHNfdGFyZ2V0cyA9PSAwXG4gICAgICAgIG9uZV9ob3QgPSB0b3JjaC56ZXJvcyhCLCBBLCBDLCBkZXZpY2U9Y2xzX2xvZ2l0cy5kZXZpY2UpXG4gICAgICAgIGZvciBjIGluIHJhbmdlKDEsIEMgKyAxKTpcbiAgICAgICAgICAgIG9uZV9ob3RbOiwgOiwgYy0xXSA9IChjbHNfdGFyZ2V0cyA9PSBjKS5mbG9hdCgpXG4gICAgICAgICMgQ29tcHV0ZSBmb2NhbCBsb3NzIG9ubHkgZm9yIG5vbi1pZ25vcmVkIGFuY2hvcnNcbiAgICAgICAgdmFsaWQgPSBjbHNfdGFyZ2V0cyBcdTAwM2U9IDAgICMgaWdub3JlIGFuY2hvcnMgd2l0aCB0YXJnZXQ9LTFcbiAgICAgICAgcF90ID0gdG9yY2gud2hlcmUob25lX2hvdC5ib29sKCksIHByb2JzLCAxIC0gcHJvYnMpXG4gICAgICAgIGFscGhhX3QgPSB0b3JjaC53aGVyZShvbmVfaG90LmJvb2woKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvcmNoLmZ1bGxfbGlrZShwcm9icywgc2VsZi5hbHBoYSksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b3JjaC5mdWxsX2xpa2UocHJvYnMsIDEgLSBzZWxmLmFscGhhKSlcbiAgICAgICAgYmNlID0gRi5iaW5hcnlfY3Jvc3NfZW50cm9weV93aXRoX2xvZ2l0cyhcbiAgICAgICAgICAgIGNsc19sb2dpdHMsIG9uZV9ob3QsIHJlZHVjdGlvbj1cdTAwMjdub25lXHUwMDI3KVxuICAgICAgICBmb2NhbCA9IGFscGhhX3QgKiAoMSAtIHBfdCkucG93KHNlbGYuZ2FtbWEpICogYmNlXG4gICAgICAgIG5fZmcgPSBmZ19tYXNrLnN1bSgpLmNsYW1wKG1pbj0xKVxuICAgICAgICByZXR1cm4gZm9jYWxbdmFsaWRdLnN1bSgpIC8gbl9mZ1xuXG5CLCBBLCBDID0gMiwgMTAwMCwgODBcbmNsc19sb2dpdHMgID0gdG9yY2gucmFuZG4oQiwgQSwgQylcbmNsc190YXJnZXRzID0gdG9yY2guZnVsbCgoQiwgQSksIC0xLCBkdHlwZT10b3JjaC5sb25nKVxuY2xzX3RhcmdldHNbOiwgOjEwXSA9IHRvcmNoLnJhbmRpbnQoMSwgODEsIChCLCAxMCkpXG5jbHNfdGFyZ2V0c1s6LCAxMDo1MDBdID0gMFxubG9zc19mbiA9IFJldGluYU5ldEZvY2FsTG9zcygpXG5sb3NzID0gbG9zc19mbihjbHNfbG9naXRzLCBjbHNfdGFyZ2V0cylcbnByaW50KGZcdTAwMjdGb2NhbCBsb3NzIChSZXRpbmFOZXQgc3R5bGUpOiB7bG9zcy5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlJldGluYU5ldCBBY2hpZXZlZCBPbmUtU3RhZ2UgUGFyaXR5IiwiY29udGVudCI6IlJldGluYU5ldCAoTGluIGV0IGFsLiAyMDE3KSB3YXMgdGhlIGZpcnN0IG9uZS1zdGFnZSBkZXRlY3RvciB0byBtYXRjaCB0d28tc3RhZ2UgRmFzdGVyIFItQ05OIGFjY3VyYWN5IG9uIENPQ08uIFRoZSBrZXkgd2FzIGZvY2FsIGxvc3Mg4oCUIHdpdGhvdXQgaXQsIHRoZSBvbmUtc3RhZ2UgbW9kZWwgd2FzIGRvbWluYXRlZCBieSBlYXN5IGJhY2tncm91bmQgYW5jaG9ycyBhbmQgcGVyZm9ybWVkIDEwKyBBUCBwb2ludHMgd29yc2UuIFdpdGggZm9jYWwgbG9zcyBhbmQgYSBSZXNOZXQtNTAgRlBOIGJhY2tib25lLCBSZXRpbmFOZXQgYWNoaWV2ZWQgMzcuOCBBUCB2cyBGYXN0ZXIgUi1DTk5cdTAwMjdzIDM2LjggQVAsIHdpdGggaGlnaGVyIGluZmVyZW5jZSBzcGVlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDRSB2cyBGb2NhbCBvbiBJbWJhbGFuY2VkIENsYXNzaWZpY2F0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGF2ZXJhZ2VfcHJlY2lzaW9uX3Njb3JlXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihuX3NhbXBsZXM9NTAwMCwgbl9mZWF0dXJlcz0yMCwgbl9pbmZvcm1hdGl2ZT0xNSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3ZWlnaHRzPVswLjk1LCAwLjA1XSwgcmFuZG9tX3N0YXRlPTQyKVxuWCA9IHRvcmNoLnRlbnNvcihYLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxueSA9IHRvcmNoLnRlbnNvcih5LCBkdHlwZT10b3JjaC5sb25nKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMywgc3RyYXRpZnk9eSwgcmFuZG9tX3N0YXRlPTApXG5cbmRlZiB0cmFpbl9ldmFsKGxvc3NfZm4sIGVwb2Nocz04MCk6XG4gICAgbmV0ID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMjAsIDY0KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoNjQsIDIpKVxuICAgIG9wdCA9IHRvcmNoLm9wdGltLkFkYW0obmV0LnBhcmFtZXRlcnMoKSwgbHI9M2UtMywgd2VpZ2h0X2RlY2F5PTFlLTQpXG4gICAgZm9yIF8gaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgbmV0LnRyYWluKClcbiAgICAgICAgbG9zcyA9IGxvc3NfZm4obmV0KFhfdHIpLCB5X3RyKVxuICAgICAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgIG5ldC5ldmFsKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgcHJvYnMgPSBGLnNvZnRtYXgobmV0KFhfdGUpLCBkaW09LTEpWzosIDFdLm51bXB5KClcbiAgICByZXR1cm4gYXZlcmFnZV9wcmVjaXNpb25fc2NvcmUoeV90ZS5udW1weSgpLCBwcm9icylcblxuIyBTdGFuZGFyZCBDRVxuYXBfY2UgPSB0cmFpbl9ldmFsKG5uLkNyb3NzRW50cm9weUxvc3MoKSlcbnByaW50KGZcdTAwMjdDcm9zcy1lbnRyb3B5ICAgICAgQVA6IHthcF9jZTouNGZ9XHUwMDI3KVxuXG4jIEZvY2FsLXN0eWxlIHZpYSBjbGFzcyB3ZWlnaHRzXG53ZWlnaHRzID0gdG9yY2gudGVuc29yKFswLjA1LCAwLjk1XSkgICMgaW52ZXJzZSBmcmVxdWVuY3lcbmFwX3dlaWdodGVkID0gdHJhaW5fZXZhbChubi5Dcm9zc0VudHJvcHlMb3NzKHdlaWdodD13ZWlnaHRzKSlcbnByaW50KGZcdTAwMjdXZWlnaHRlZCBDRSAgICAgICAgQVA6IHthcF93ZWlnaHRlZDouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFzeW1tZXRyaWMgTG9zcyBmb3IgTXVsdGktTGFiZWwgQ2xhc3NpZmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFzeW1tZXRyaWMgTG9zcyAoQVNMLCBSaWRuaWsgZXQgYWwuIDIwMjEpIGV4dGVuZHMgZm9jYWwgbG9zcyBmb3IgbXVsdGktbGFiZWwgc2V0dGluZ3Mgd2hlcmUgdGhlIHBvc2l0aXZlL25lZ2F0aXZlIGltYmFsYW5jZSBpcyBleHRyZW1lLiBBU0wgdXNlcyBkaWZmZXJlbnQgzrMgZm9yIHBvc2l0aXZlcyBhbmQgbmVnYXRpdmVzOiBGTF9wb3MgPSAoMeKIknDigpwpXs6z4oG6IMK3IGxvZyhw4oKcKSBhbmQgRkxfbmVnID0gcOKCnF7Os+KBuyDCtyBsb2coMeKIknDigpwpIHdpdGggzrPigbsgXHUwMDNlIM6z4oG6LiBUeXBpY2FsbHkgzrPigbs9NCwgzrPigbo9MCAobm8gZm9jdXNpbmcgZm9yIHBvc2l0aXZlcywgc3Ryb25nIGZvY3VzaW5nIGZvciBuZWdhdGl2ZXMpLiBBZGRpdGlvbmFsbHksIEFTTCBpbmNsdWRlcyBwcm9iYWJpbGl0eSBzaGlmdGluZzogc3VidHJhY3QgbWFyZ2luIG0gZnJvbSBuZWdhdGl2ZSBwcm9iYWJpbGl0aWVzIGJlZm9yZSBjb21wdXRpbmcgbG9zcywgaGFyZC10aHJlc2hvbGRpbmcgdmVyeSBlYXN5IG5lZ2F0aXZlcy4gQVNMIGFjaGlldmVzIHN0YXRlLW9mLXRoZS1hcnQgb24gTVMtQ09DTyBtdWx0aS1sYWJlbCBjbGFzc2lmaWNhdGlvbiAoOTAuNCBtQVAgd2l0aCBUUmVzTmV0LUwpLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsizrM9MiwgzrE9MC4yNSBhcmUgdGhlIHN0YW5kYXJkIFJldGluYU5ldCBkZWZhdWx0cyDigJQgdGhlc2Ugd2VyZSBmb3VuZCB2aWEgZ3JpZCBzZWFyY2ggb24gQ09DTy4iLCJGb3IgZXh0cmVtZSBpbWJhbGFuY2UgKDE6MTAwMDApLCBpbmNyZWFzZSDOsyB0byAz4oCTNSB0byBzdXBwcmVzcyBlYXN5IG5lZ2F0aXZlcyBtb3JlIGFnZ3Jlc3NpdmVseS4iLCJWYXJpRm9jYWxMb3NzIChWRkwpOiB1c2VzIHRoZSBJb1Ugc2NvcmUgYXMgdGhlIHRhcmdldCBwcm9iYWJpbGl0eSBpbnN0ZWFkIG9mIGEgYmluYXJ5IGxhYmVsIOKAlCBiZXR0ZXIgZm9yIGRldGVjdGlvbiBxdWFsaXR5IHNjb3JpbmcuIiwiUUZvY2FsTG9zcyAoUUZMKTogZ2VuZXJhbGl6ZXMgZm9jYWwgbG9zcyB0byBjb250aW51b3VzIHRhcmdldHMgZm9yIHByZWRpY3RpbmcgZGlzdHJpYnV0aW9uIG9mIGJvdW5kaW5nIGJveCBjb29yZGluYXRlcy4iLCJGb2NhbCBsb3NzIHJlcXVpcmVzIHNpZ21vaWQgb3V0cHV0cyAobm90IHNvZnRtYXgpIGZvciBtdWx0aS1jbGFzcyBkZXRlY3Rpb24g4oCUIGVhY2ggY2xhc3MgaXMgdHJlYXRlZCBhcyBhIGJpbmFyeSBwcm9ibGVtIGluZGVwZW5kZW50bHkuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikxvc3MgRnVuY3Rpb24gQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJMb3NzIiwiQ2xhc3MgSW1iYWxhbmNlIiwiRm9jdXNpbmcgUGFyYW1zIiwiRGV0ZWN0aW9uIFVzZSIsIk11bHRpLUxhYmVsIiwiQ29tcGxleGl0eSJdLCJyb3dzIjpbWyJDcm9zcy1FbnRyb3B5IiwiRG9taW5hdGVkIGJ5IGVhc3kgZXhhbXBsZXMiLCJOb25lIiwiVHdvLXN0YWdlICh3aXRoIE9IRU0pIiwiTm8gKHVzZSBCQ0UpIiwiTG93IOKAlCBzdGFuZGFyZCBiYXNlbGluZSJdLFsiV2VpZ2h0ZWQgQ0UiLCJQYXJ0aWFsIOKAlCBmaXhlZCBjbGFzcyB3ZWlnaHRzIiwizrEgcGVyIGNsYXNzIiwiTGltaXRlZCIsIk5vIiwiTG93IOKAlCBhZGQgd2VpZ2h0IHZlY3RvciJdLFsiT0hFTSIsIkdvb2Qg4oCUIHNlbGVjdHMgaGFyZCBleGFtcGxlcyIsIk1pbmluZyByYXRpbyBrIiwiVHdvLXN0YWdlIGRldGVjdG9ycyIsIk5vIiwiTWVkaXVtIOKAlCByZXF1aXJlcyBzb3J0aW5nIGxvc3NlcyJdLFsiRm9jYWwgTG9zcyAozrM9MikiLCJFeGNlbGxlbnQg4oCUIGNvbnRpbnVvdXMgd2VpZ2h0aW5nIiwizrMsIM6xIiwiT25lLXN0YWdlIChSZXRpbmFOZXQsIEZDT1MpIiwiWWVzIChiaW5hcnkpIiwiTG93IOKAlCBzaW5nbGUgbW9kdWxhdGlvbiB0ZXJtIl0sWyJBc3ltbWV0cmljIExvc3MiLCJCZXN0IGZvciBleHRyZW1lIGltYmFsYW5jZSIsIs6z4oG6LCDOs+KBuywgbWFyZ2luIG0iLCJNdWx0aS1sYWJlbCBkZXRlY3Rpb24iLCJZZXMiLCJNZWRpdW0g4oCUIHNlcGFyYXRlIHBvcy9uZWcgaGFuZGxpbmciXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9jYWwgbG9zcyB3aXRoIM6zPTIgYW5kIM6xPTAuMjUgaXMgdGhlIHJlY29tbWVuZGVkIGRlZmF1bHQgZm9yIGFueSBvbmUtc3RhZ2Ugb2JqZWN0IGRldGVjdG9yLiBGb3IgbXVsdGktbGFiZWwgY2xhc3NpZmljYXRpb24gd2l0aCBleHRyZW1lIHBvc2l0aXZlL25lZ2F0aXZlIGltYmFsYW5jZSAoZS5nLiwgaW1hZ2UgdGFnZ2luZyB3aXRoIHRob3VzYW5kcyBvZiBjbGFzc2VzKSwgdXNlIEFzeW1tZXRyaWMgTG9zcyB3aXRoIM6z4oG7PTQsIM6z4oG6PTAuIEZvciB0d28tc3RhZ2UgZGV0ZWN0b3JzIHdoZXJlIE9IRU0gaXMgYWxyZWFkeSBpbXBsZW1lbnRlZCwgdGhlIGFkZGl0aW9uYWwgYmVuZWZpdCBvZiBmb2NhbCBsb3NzIGlzIG1hcmdpbmFsIOKAlCB3ZWlnaHRlZCBDRSB3aXRoIM6xPTAuMjUgaXMgc3VmZmljaWVudC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Focal Loss — Hard Example Mining for Class Imbalance

Class imbalance is a fundamental challenge in object detection: a single image may contain 1–10 foreground objects but 10,000–100,000 background anchor boxes. Standard cross-entropy loss is overwhelmed by easy negative examples — each individual easy negative contributes a tiny loss, but their sheer number dominates training. Online Hard Example Mining (OHEM) addresses this by sampling only the highest-loss examples, but it requires complex sampling logic. Focal Loss (Lin et al. 2017) solves the same problem elegantly by reweighting each example's loss based on its classification confidence.

## Class Imbalance in Object Detection

Two-stage detectors (Faster R-CNN) use a region proposal network to filter most background anchors before the classification stage — the class imbalance ratio in the second stage is manageable (roughly 1:3 foreground to background). One-stage detectors (SSD, YOLO, RetinaNet) classify all anchors simultaneously, facing ratios of 1:1000 or worse. OHEM (Online Hard Example Mining) selects the top-k highest-loss anchors per image during training, discarding easy negatives. But OHEM requires sorting all anchor losses and is sensitive to the mining ratio hyperparameter.

## Focal Loss Formula

Focal Loss modifies binary cross-entropy by adding a modulating factor. Define pₜ = p if y=1 else (1−p) — the predicted probability for the true class. Standard BCE: CE(pₜ) = −log(pₜ). Focal Loss: FL(pₜ) = −(1−pₜ)^γ · log(pₜ). The modulating factor (1−pₜ)^γ: when the example is easy (pₜ → 1), (1−pₜ)^γ → 0, suppressing the loss contribution. When the example is hard (pₜ → 0), (1−pₜ)^γ → 1, keeping full loss weight. γ=2 is the standard choice. Note that CE is focal loss with γ=0. The class-balanced version adds α: FL(pₜ) = −αₜ(1−pₜ)^γ log(pₜ) where αₜ = α if y=1 else (1−α).

```python
import torch
import torch.nn.functional as F

def focal_loss_binary(logits, targets, gamma=2.0, alpha=0.25, reduction='mean'):
    # Binary focal loss (sigmoid-based) for single-class detection
    probs = torch.sigmoid(logits)
    # p_t: predicted probability for the true class
    p_t = torch.where(targets == 1, probs, 1 - probs)
    # alpha_t: class weight
    alpha_t = torch.where(targets == 1,
                          torch.full_like(probs, alpha),
                          torch.full_like(probs, 1 - alpha))
    # Focal modulation: suppress easy examples
    focal_weight = (1 - p_t).pow(gamma)
    # BCE with numerically stable log
    bce = F.binary_cross_entropy_with_logits(
        logits, targets.float(), reduction='none')
    loss = alpha_t * focal_weight * bce
    if reduction == 'mean':
        return loss.mean()
    elif reduction == 'sum':
        return loss.sum()
    return loss

torch.manual_seed(42)
# Simulate: 10 positive anchors, 9990 negative anchors
logits = torch.cat([torch.randn(10) + 1.0,   # positives
                    torch.randn(9990) - 2.0])  # easy negatives
targets = torch.cat([torch.ones(10), torch.zeros(9990)])

fl = focal_loss_binary(logits, targets, gamma=2.0, alpha=0.25)
ce = F.binary_cross_entropy_with_logits(logits, targets.float())
print(f'Cross-entropy loss: {ce.item():.6f}')
print(f'Focal loss (g=2):   {fl.item():.6f}')
print('Focal loss is much lower because easy negatives are suppressed.')
```

## Effect of the Focusing Parameter γ

The parameter γ controls how aggressively easy examples are down-weighted. At γ=0, FL = CE (no suppression). At γ=1, easy examples (pₜ=0.9) receive weight (1−0.9)^1 = 0.1 — 10% of their CE loss. At γ=2 (standard), they receive (1−0.9)^2 = 0.01 — 1% of their CE loss. At γ=5, they receive (1−0.9)^5 ≈ 0.00001 — effectively zero. Hard examples (pₜ=0.2) receive: γ=1 → 0.8×, γ=2 → 0.64×, γ=5 → 0.33×. The ratio of hard-to-easy weighting grows rapidly with γ, concentrating training on the hardest examples.

```python
import numpy as np
import torch

def focal_weight(p_t, gamma):
    return (1 - p_t) ** gamma

p_values = np.linspace(0.01, 0.99, 100)
print(f'{"p_t":>6} {"CE":<10} {"FL(g=1)":<12} {"FL(g=2)":<12} {"FL(g=5)":<12}')
for p in [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
    ce   = -np.log(p)
    fl1  = focal_weight(p, 1) * ce
    fl2  = focal_weight(p, 2) * ce
    fl5  = focal_weight(p, 5) * ce
    print(f'{p:>6.2f} {ce:<10.4f} {fl1:<12.4f} {fl2:<12.4f} {fl5:<12.4f}')

print('\n--- Hard (p=0.1) vs Easy (p=0.9) loss ratio by gamma ---')
for g in [0, 1, 2, 5]:
    ratio = (focal_weight(0.1, g) * (-np.log(0.1))) / \
            (focal_weight(0.9, g) * (-np.log(0.9)))
    print(f'  gamma={g}: hard/easy ratio = {ratio:.1f}x')
print('\nHigher gamma -> harder examples dominate training more strongly.')
```

## Focal Loss in Object Detection

In RetinaNet, the classification subnet outputs B × A × C sigmoid logits (not softmax), treating each class as an independent binary classification. Focal loss is applied to each (anchor, class) pair. Anchors with IoU ≥ 0.5 with any ground-truth box are positive; anchors with IoU < 0.4 are negative; anchors in the ambiguous range [0.4, 0.5) are ignored (target=-1). Only positive and negative anchors contribute to the focal loss; ignored anchors are masked out. The total loss is normalized by the number of foreground anchors.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class RetinaNetFocalLoss(nn.Module):
    def __init__(self, gamma=2.0, alpha=0.25):
        super().__init__()
        self.gamma = gamma
        self.alpha = alpha

    def forward(self, cls_logits, cls_targets):
        # cls_logits:  (B, A, C) — logits per anchor per class
        # cls_targets: (B, A)    — -1=ignore, 0=background, 1..C=class
        B, A, C = cls_logits.shape
        probs = torch.sigmoid(cls_logits)
        # Build one-hot targets (background has all-zero target)
        fg_mask = cls_targets > 0
        bg_mask = cls_targets == 0
        one_hot = torch.zeros(B, A, C, device=cls_logits.device)
        for c in range(1, C + 1):
            one_hot[:, :, c-1] = (cls_targets == c).float()
        # Compute focal loss only for non-ignored anchors
        valid = cls_targets >= 0  # ignore anchors with target=-1
        p_t = torch.where(one_hot.bool(), probs, 1 - probs)
        alpha_t = torch.where(one_hot.bool(),
                              torch.full_like(probs, self.alpha),
                              torch.full_like(probs, 1 - self.alpha))
        bce = F.binary_cross_entropy_with_logits(
            cls_logits, one_hot, reduction='none')
        focal = alpha_t * (1 - p_t).pow(self.gamma) * bce
        n_fg = fg_mask.sum().clamp(min=1)
        return focal[valid].sum() / n_fg

B, A, C = 2, 1000, 80
cls_logits  = torch.randn(B, A, C)
cls_targets = torch.full((B, A), -1, dtype=torch.long)
cls_targets[:, :10] = torch.randint(1, 81, (B, 10))
cls_targets[:, 10:500] = 0
loss_fn = RetinaNetFocalLoss()
loss = loss_fn(cls_logits, cls_targets)
print(f'Focal loss (RetinaNet style): {loss.item():.4f}')
```

> **RetinaNet Achieved One-Stage Parity**: RetinaNet (Lin et al. 2017) was the first one-stage detector to match two-stage Faster R-CNN accuracy on COCO. The key was focal loss — without it, the one-stage model was dominated by easy background anchors and performed 10+ AP points worse. With focal loss and a ResNet-50 FPN backbone, RetinaNet achieved 37.8 AP vs Faster R-CNN's 36.8 AP, with higher inference speed.

## CE vs Focal on Imbalanced Classification

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score

np.random.seed(42)
torch.manual_seed(42)
X, y = make_classification(n_samples=5000, n_features=20, n_informative=15,
                            weights=[0.95, 0.05], random_state=42)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)

def train_eval(loss_fn, epochs=80):
    net = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Linear(64, 2))
    opt = torch.optim.Adam(net.parameters(), lr=3e-3, weight_decay=1e-4)
    for _ in range(epochs):
        net.train()
        loss = loss_fn(net(X_tr), y_tr)
        opt.zero_grad(); loss.backward(); opt.step()
    net.eval()
    with torch.no_grad():
        probs = F.softmax(net(X_te), dim=-1)[:, 1].numpy()
    return average_precision_score(y_te.numpy(), probs)

# Standard CE
ap_ce = train_eval(nn.CrossEntropyLoss())
print(f'Cross-entropy      AP: {ap_ce:.4f}')

# Focal-style via class weights
weights = torch.tensor([0.05, 0.95])  # inverse frequency
ap_weighted = train_eval(nn.CrossEntropyLoss(weight=weights))
print(f'Weighted CE        AP: {ap_weighted:.4f}')
```

## Asymmetric Loss for Multi-Label Classification

Asymmetric Loss (ASL, Ridnik et al. 2021) extends focal loss for multi-label settings where the positive/negative imbalance is extreme. ASL uses different γ for positives and negatives: FL_pos = (1−pₜ)^γ⁺ · log(pₜ) and FL_neg = pₜ^γ⁻ · log(1−pₜ) with γ⁻ > γ⁺. Typically γ⁻=4, γ⁺=0 (no focusing for positives, strong focusing for negatives). Additionally, ASL includes probability shifting: subtract margin m from negative probabilities before computing loss, hard-thresholding very easy negatives. ASL achieves state-of-the-art on MS-COCO multi-label classification (90.4 mAP with TResNet-L).

- γ=2, α=0.25 are the standard RetinaNet defaults — these were found via grid search on COCO.
- For extreme imbalance (1:10000), increase γ to 3–5 to suppress easy negatives more aggressively.
- VariFocalLoss (VFL): uses the IoU score as the target probability instead of a binary label — better for detection quality scoring.
- QFocalLoss (QFL): generalizes focal loss to continuous targets for predicting distribution of bounding box coordinates.
- Focal loss requires sigmoid outputs (not softmax) for multi-class detection — each class is treated as a binary problem independently.

## Loss Function Comparison

| Loss | Class Imbalance | Focusing Params | Detection Use | Multi-Label | Complexity |
| --- | --- | --- | --- | --- | --- |
| Cross-Entropy | Dominated by easy examples | None | Two-stage (with OHEM) | No (use BCE) | Low — standard baseline |
| Weighted CE | Partial — fixed class weights | α per class | Limited | No | Low — add weight vector |
| OHEM | Good — selects hard examples | Mining ratio k | Two-stage detectors | No | Medium — requires sorting losses |
| Focal Loss (γ=2) | Excellent — continuous weighting | γ, α | One-stage (RetinaNet, FCOS) | Yes (binary) | Low — single modulation term |
| Asymmetric Loss | Best for extreme imbalance | γ⁺, γ⁻, margin m | Multi-label detection | Yes | Medium — separate pos/neg handling |

Focal loss with γ=2 and α=0.25 is the recommended default for any one-stage object detector. For multi-label classification with extreme positive/negative imbalance (e.g., image tagging with thousands of classes), use Asymmetric Loss with γ⁻=4, γ⁺=0. For two-stage detectors where OHEM is already implemented, the additional benefit of focal loss is marginal — weighted CE with α=0.25 is sufficient.

---

