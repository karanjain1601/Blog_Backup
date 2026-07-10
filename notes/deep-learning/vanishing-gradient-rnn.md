---
title: "Vanishing Gradient in RNNs — Mathematical Derivation"
slug: "vanishing-gradient-rnn"
description: "Derive the vanishing gradient analytically, plot gradient norm vs time lag, compare vanilla RNN to LSTM on long-range tasks, and analyse orthogonal initialisation as a mitigation strategy."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHZhbmlzaGluZyBncmFkaWVudCBwcm9ibGVtIGluIFJOTnMgaXMgbm90IGEgbnVtZXJpY2FsIGlzc3VlIOKAlCBpdCBpcyBhIGNvbnNlcXVlbmNlIG9mIHRoZSBtYXRoZW1hdGljYWwgc3RydWN0dXJlIG9mIGdyYWRpZW50IGJhY2twcm9wYWdhdGlvbiB0aHJvdWdoIHRpbWUuIFRoZSBncmFkaWVudCBvZiB0aGUgbG9zcyBhdCBzdGVwIFQgd2l0aCByZXNwZWN0IHRvIHRoZSBoaWRkZW4gc3RhdGUgYXQgc3RlcCBrIGlzOiBkTOKCnC9kaOKCliA9IChkTOKCnC9kaOKCnCkgwrcgzqDisbzigozigpbigorigoHhtYAgKGRo4rG8L2Ro4rG84oKL4oKBKS4gRWFjaCBKYWNvYmlhbiBmYWN0b3Ig4oiCaOKxvC/iiIJo4rG84oKL4oKBID0gV+KCleKCleG1gCDCtyBkaWFnKHRhbmhcdTAwMjcoaOKxvCkpIHdoZXJlIHRhbmhcdTAwMjcoeCkgPSAxIOKIkiB0YW5oKHgpwrIg4oiIIFswLDFdLiBJZiB0aGUgbGFyZ2VzdCBzaW5ndWxhciB2YWx1ZSBvZiBX4oKV4oKVIGlzIGxlc3MgdGhhbiAxIChvciB0YW5oIHNhdHVyYXRlcyksIHRoZSBwcm9kdWN0IGRlY2F5cyBleHBvbmVudGlhbGx5IHdpdGggVOKIkmsuIFRoaXMgbWVhbnMgdGhlIFJOTiBncmFkaWVudCBmb3IgYSBkZXBlbmRlbmN5IGF0IGxhZyA1MCBpcyB0eXBpY2FsbHkgMTDigbvCueKBtSB0aW1lcyBzbWFsbGVyIHRoYW4gdGhlIGdyYWRpZW50IGZvciBhIGRlcGVuZGVuY3kgYXQgbGFnIDEg4oCUIG51bWVyaWNhbGx5IHplcm8gaW4gZmxvYXQzMi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYXRoZW1hdGljYWwgRGVyaXZhdGlvbiBvZiBWYW5pc2hpbmcgR3JhZGllbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZmluZSB0aGUgSmFjb2JpYW4gb2YgaOKxvCB3aXRoIHJlc3BlY3QgdG8gaOKxvOKCi+KCgTogSuKxvCA9IOKIgmjisbwv4oiCaOKxvOKCi+KCgSA9IFfigpXigpXhtYAgwrcgZGlhZygxIOKIkiBo4rG8wrIpLiBUaGUgZ3JhZGllbnQgb2YgdGhlIGxvc3MgYXQgdGltZSB0IHdpdGggcmVzcGVjdCB0byBo4oKWIGlzOiBkTOKCnC9kaOKCliA9IChkTOKCnC9kaOKCnCkgwrcgSuKCnCDCtyBK4oKc4oKL4oKBIMK3IC4uLiDCtyBK4oKW4oKK4oKBIChhIHByb2R1Y3Qgb2YgdOKIkmsgbWF0cmljZXMpLiBCeSB0aGUgc3ViLW11bHRpcGxpY2F0aXZpdHkgb2YgbWF0cml4IG5vcm1zOiDigJbOoOKxvCBK4rG84oCWIOKJpCDOoOKxvCDigJZK4rG84oCWLiBTaW5jZSDigJZK4rG84oCWIOKJpCDPg19tYXgoV+KCleKClSkgwrcg4oCWZGlhZyh0YW5oXHUwMDI3KeKAliDiiaQgz4NfbWF4KFfigpXigpUpLCBpZiDPg19tYXgoV+KCleKClSkgXHUwMDNjIDEgdGhlbiDigJZkTOKCnC9kaOKCluKAliDiiaQg4oCWZEzigpwvZGjigpzigJYgwrcgz4NfbWF4KFfigpXigpUpXih04oiSaykg4oaSIDAgZXhwb25lbnRpYWxseS4gVGhpcyBpcyBub3QgYW4gaW1wbGVtZW50YXRpb24gYnVnIOKAlCBpdCBpcyB0aGUgZnVuZGFtZW50YWwgcmVhc29uIHBsYWluIFJOTnMgY2Fubm90IGxlYXJuIGxvbmctcmFuZ2UgZGVwZW5kZW5jaWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxubnAucmFuZG9tLnNlZWQoNDIpXG5ULCBILCBJID0gNTAsIDE2LCA0XG5cbmRlZiBncmFkaWVudF9ub3JtX3ZzX2xhZyhXaGhfc2NhbGUsIFQ9NTAsIEg9MTYsIEk9NCwgc2VlZD0wKTpcbiAgICBybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoc2VlZClcbiAgICBXeGggPSBybmcucmFuZG4oSCwgSSkgKiAwLjFcbiAgICBXaGggPSBybmcucmFuZG4oSCwgSCkgKiBXaGhfc2NhbGUgLyBucC5zcXJ0KEgpXG4gICAgYmggID0gbnAuemVyb3MoKEgsIDEpKVxuICAgIHhzICA9IFtybmcucmFuZG4oSSwgMSkgZm9yIF8gaW4gcmFuZ2UoVCldXG4gICAgaHMgID0gey0xOiBucC56ZXJvcygoSCwgMSkpfVxuICAgIGZvciB0IGluIHJhbmdlKFQpOlxuICAgICAgICBoc1t0XSA9IG5wLnRhbmgoV3hoIEAgeHNbdF0gKyBXaGggQCBoc1t0LTFdICsgYmgpXG4gICAgZGggPSBucC5vbmVzKChILCAxKSkgLyBIICAjIHVuaXQgZ3JhZGllbnQgYXQgdCA9IFQtMVxuICAgIG5vcm1zID0ge31cbiAgICBmb3IgdCBpbiByZXZlcnNlZChyYW5nZShUKSk6XG4gICAgICAgIG5vcm1zW3RdID0gZmxvYXQobnAubGluYWxnLm5vcm0oZGgpKVxuICAgICAgICBkdGFuaCAgICA9ICgxIC0gaHNbdF0qKjIpICogZGhcbiAgICAgICAgZGggICAgICAgPSBXaGguVCBAIGR0YW5oXG4gICAgcmV0dXJuIFtub3Jtc1t0XSBmb3IgdCBpbiByYW5nZShUKV1cblxucHJpbnQoZlx1MDAyN3tcIlNjYWxlXCI6XHUwMDNlOH0ge1widD1ULTFcIjpcdTAwM2UxMn0ge1widD1ULzJcIjpcdTAwM2UxMn0ge1widD0wXCI6XHUwMDNlMTJ9IHtcIlJlZ2ltZVwiOlx1MDAzZTEyfVx1MDAyNylcbmZvciBzY2FsZSwgbGFiZWwgaW4gWygwLjUsIFx1MDAyN3ZhbmlzaGluZ1x1MDAyNyksICgxLjAsIFx1MDAyN21hcmdpbmFsXHUwMDI3KSwgKDIuMCwgXHUwMDI3ZXhwbG9kaW5nXHUwMDI3KV06XG4gICAgbm9ybXMgPSBncmFkaWVudF9ub3JtX3ZzX2xhZyhzY2FsZSlcbiAgICBtaWQgICA9IFQgLy8gMlxuICAgIHByaW50KGZcdTAwMjd7c2NhbGU6XHUwMDNlOC4xZn0ge25vcm1zW1QtMV06XHUwMDNlMTIuNGV9IHtub3Jtc1ttaWRdOlx1MDAzZTEyLjRlfSBcdTAwMjdcbiAgICAgICAgICBmXHUwMDI3e25vcm1zWzBdOlx1MDAzZTEyLjRlfSB7bGFiZWw6XHUwMDNlMTJ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0ZvciBzY2FsZT0wLjU6IHJhdGlvIG5vcm1zW3Q9MF0vbm9ybXNbdD1ULTFdIH4gKDAuNS9zcXJ0KEgpKV57VH0gfiAwXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IjFEIFJOTiBBbmFseXRpY2FsIEdyYWRpZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSAxRCBSTk4gKEg9MSksIHRoZSBncmFkaWVudCBoYXMgYSBjbG9zZWQgZm9ybSB0aGF0IG1ha2VzIHRoZSBkZWNheSBleHBsaWNpdC4gV2l0aCBoX3QgPSB0YW5oKHdfaGggwrcgaF97dC0xfSArIHdfeGggwrcgeF90ICsgYiksIHRoZSBncmFkaWVudCBkTC9kaF9rID0gZEwvZGhfVCDCtyDOoOKxvOKCjOKCluKCiuKCgeG1gCAod19oaCDCtyAoMSDiiJIgaF9qwrIpKS4gSWYgd19oaCA9IDAuOSBhbmQgdGFuaFx1MDAyNyho4rG8KSDiiYggMC45IChuZWFyIHplcm8pLCBlYWNoIGZhY3RvciBpcyB+MC44MSwgYW5kIGFmdGVyIDUwIHN0ZXBzIHRoZSBncmFkaWVudCBpcyB+MC44MeKBteKBsCDiiYggMS44w5cxMOKBu+KBtS4gVGhpcyAxRCBhbmFseXNpcyBtYWtlcyB0aGUgZXhwb25lbnRpYWwgZGVjYXkgdHJhbnNwYXJlbnQgYW5kIGdlbmVyYWxpc2VzIHRvIGhpZ2hlciBkaW1lbnNpb25zIHdoZXJlIM+DX21heChX4oKV4oKVKSBwbGF5cyB0aGUgcm9sZSBvZiB3X2hoLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuXCJcIlwiXG4xRCBSTk46IGhfdCA9IHRhbmgod19oaCAqIGhfe3QtMX0gKyB3X3hoICogeF90ICsgYilcbkdyYWRpZW50OiBkTC9kaF9rID0gZEwvZGhfVCAqIHByb2Rfe2o9aysxfV57VH0gW3dfaGggKiAoMSAtIGhfal4yKV1cblwiXCJcIlxuXG5ucC5yYW5kb20uc2VlZCgwKVxuXG5kZWYgYW5hbHl0aWNhbF9ncmFkXzFkKHdfaGgsIFQ9MzAsIHdfeGg9MC4xLCBiPTAuMCwgc2VlZD0wKTpcbiAgICBybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoc2VlZClcbiAgICB4cyAgPSBybmcucmFuZG4oVCkgKiAwLjVcbiAgICBocyAgPSBbMC4wXVxuICAgIGZvciB0IGluIHJhbmdlKFQpOlxuICAgICAgICBocy5hcHBlbmQobnAudGFuaCh3X2hoICogaHNbLTFdICsgd194aCAqIHhzW3RdICsgYikpXG4gICAgIyBDb21wdXRlIGRML2RoX2sgZm9yIGVhY2ggayBnaXZlbiB1bml0IGdyYWRpZW50IGF0IFQtMVxuICAgIGRMX2RoayA9IFswLjBdICogVFxuICAgIGRMX2Roa1stMV0gPSAxLjBcbiAgICBmb3IgayBpbiByYW5nZShUIC0gMiwgLTEsIC0xKTpcbiAgICAgICAgcHJvZHVjdCA9IDEuMFxuICAgICAgICBmb3IgaiBpbiByYW5nZShrICsgMSwgVCk6XG4gICAgICAgICAgICB0YW5oX3ByaW1lID0gMS4wIC0gaHNbaiArIDFdICoqIDJcbiAgICAgICAgICAgIHByb2R1Y3QgICAqPSB3X2hoICogdGFuaF9wcmltZVxuICAgICAgICBkTF9kaGtba10gPSBwcm9kdWN0XG4gICAgcmV0dXJuIGhzWzE6XSwgZExfZGhrXG5cbnByaW50KGZcdTAwMjd7XCJ3X2hoXCI6XHUwMDNlOH0ge1wibGFnXCI6XHUwMDNlNX0ge1wiZEwvZGhfa1wiOlx1MDAzZTE0fSB7XCJBbmFseXNpc1wifVx1MDAyNylcbmZvciB3X2hoIGluIFswLjUsIDAuOSwgMS4wLCAxLjVdOlxuICAgIF8sIGdyYWRzID0gYW5hbHl0aWNhbF9ncmFkXzFkKHdfaGgpXG4gICAgVCA9IGxlbihncmFkcylcbiAgICBmb3IgbGFnIGluIFsxLCA1LCAxNSwgMjldOlxuICAgICAgICBrID0gVCAtIDEgLSBsYWdcbiAgICAgICAgZyA9IGFicyhncmFkc1trXSlcbiAgICAgICAgcmVnaW1lID0gXHUwMDI3dmFuaXNoaW5nXHUwMDI3IGlmIGcgXHUwMDNjIDFlLTMgZWxzZSAoXHUwMDI3ZXhwbG9kaW5nXHUwMDI3IGlmIGcgXHUwMDNlIDFlMyBlbHNlIFx1MDAyN3N0YWJsZVx1MDAyNylcbiAgICAgICAgcHJpbnQoZlx1MDAyN3t3X2hoOlx1MDAzZTguMWZ9IHtsYWc6XHUwMDNlNX0ge2c6XHUwMDNlMTQuNGV9IHtyZWdpbWV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IE5vcm0gdnMgVGltZSBMYWcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBsb3R0aW5nIGdyYWRpZW50IG5vcm0gYWdhaW5zdCB0aW1lIGxhZyAoZGlzdGFuY2UgZnJvbSBsb3NzIHRvIGhpZGRlbiBzdGF0ZSkgcmV2ZWFscyB0aGUgcmVnaW1lIGNsZWFybHk6IGV4cG9uZW50aWFsIGRlY2F5IGZvciBzbWFsbCBX4oKV4oKVLCBuZWFyLWNvbnN0YW50IGZvciBvcnRob2dvbmFsIFfigpXigpUsIGV4cG9uZW50aWFsIGdyb3d0aCBmb3IgbGFyZ2UgV+KCleKClS4gSW4gcHJhY3RpY2UsIGV2ZW4gd2VsbC1pbml0aWFsaXNlZCBSTk5zIHRyYW5zaXRpb24gdG8gdmFuaXNoaW5nIHdpdGhpbiAyMOKAkzUwIHN0ZXBzIGFzIHRhbmggc2F0dXJhdGlvbiBhY2N1bXVsYXRlcy4gVGhlIExTVE0gc29sdmVzIHRoaXMgd2l0aCBhbiBhZGRpdGl2ZSBjZWxsIHN0YXRlIHVwZGF0ZSAoQ+KCnCA9IGbigpziiplD4oKc4oKL4oKBICsgaeKCnOKKmUPMg+KCnCkg4oCUIHRoZSBmb3JnZXQgZ2F0ZSBhbGxvd3MgZ3JhZGllbnQgdG8gZmxvdyB0aHJvdWdoIHRoZSBjZWxsIHN0YXRlIHdpdGggb25seSBlbGVtZW50d2lzZSBtdWx0aXBsaWNhdGlvbiBieSBm4oKcLCBhdm9pZGluZyB0aGUgcmVwZWF0ZWQgbWF0cml4IG11bHRpcGxpY2F0aW9uIGJ5IFfigpXigpXhtYAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTFNUTSBhbmQgR1JVIGFzIFNvbHV0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIExTVE0gaW50cm9kdWNlcyBhIGNlbGwgc3RhdGUgQ+KCnCB0aGF0IGlzIHVwZGF0ZWQgYWRkaXRpdmVseTogQ+KCnCA9IGbigpziiplD4oKc4oKL4oKBICsgaeKCnOKKmUPMg+KCnC4gVGhlIGdyYWRpZW50IG9mIHRoZSBsb3NzIHdpdGggcmVzcGVjdCB0byB0aGUgY2VsbCBzdGF0ZSBhdCB0aW1lIGsgZmxvd3MgYmFjayB0aHJvdWdoIHRoZSBmb3JnZXQgZ2F0ZSBvbmx5OiDiiIJD4oKcL+KIgkPigpzigovigoEgPSBkaWFnKGbigpwpLiBTaW5jZSBm4oKcIOKIiCAoMCwxKeG0tCAoZWxlbWVudC13aXNlIHNpZ21vaWQpLCB0aGlzIGlzIGEgZGlhZ29uYWwgbWF0cml4IOKAlCBubyByZXBlYXRlZCBtYXRyaXggbXVsdGlwbGljYXRpb24gYnkgV+KCleKClS4gV2l0aCBmb3JnZXQgZ2F0ZXMgaW5pdGlhbGlzZWQgbmVhciAxIChiaWFzID0gMSksIHRoZSBncmFkaWVudCBjYW4gZmxvdyB0aHJvdWdoIGh1bmRyZWRzIG9mIHN0ZXBzIHdpdGhvdXQgZXhwb25lbnRpYWwgZGVjYXkuIFRoZSBHUlUgdXNlcyBhIHNpbXBsZXIgdHdvLWdhdGUgZGVzaWduIHRoYXQgYWNoaWV2ZXMgc2ltaWxhciBsb25nLXJhbmdlIGdyYWRpZW50IGZsb3cuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuXG5kZWYgbWFrZV9jb3B5X2JhdGNoKEI9NjQsIFQ9NTAsIG5fY2xhc3Nlcz04KTpcbiAgICBcIlwiXCJDb3B5IHRhc2s6IHJlbWVtYmVyIGl0ZW0gZnJvbSB0PTAgYWZ0ZXIgVCBmaWxsZXIgc3RlcHMuXCJcIlwiXG4gICAgdGFyZ2V0ID0gdG9yY2gucmFuZGludChuX2NsYXNzZXMsIChCLCkpXG4gICAgeCA9IHRvcmNoLnplcm9zKEIsIFQgKyAxLCBuX2NsYXNzZXMgKyAxKVxuICAgIHhbOiwgMCwgOm5fY2xhc3Nlc10gPSBubi5mdW5jdGlvbmFsLm9uZV9ob3QodGFyZ2V0LCBuX2NsYXNzZXMpLmZsb2F0KClcbiAgICB4WzosIDE6LCBuX2NsYXNzZXNdID0gMS4wICAjIGZpbGxlciBzaWduYWxcbiAgICByZXR1cm4geCwgdGFyZ2V0XG5cbmNsYXNzIFNlcUNsYXNzaWZpZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgY2VsbF90eXBlLCBpbnAsIGhpZCwgbl9jbGFzc2VzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIFJOTkNsYXNzID0gbm4uUk5OIGlmIGNlbGxfdHlwZSA9PSBcdTAwMjdybm5cdTAwMjcgZWxzZSBubi5MU1RNXG4gICAgICAgIHNlbGYucm5uICA9IFJOTkNsYXNzKGlucCwgaGlkLCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLmZjICAgPSBubi5MaW5lYXIoaGlkLCBuX2NsYXNzZXMpXG4gICAgICAgIHNlbGYuaXNfbHN0bSA9IChjZWxsX3R5cGUgPT0gXHUwMDI3bHN0bVx1MDAyNylcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgb3V0ID0gc2VsZi5ybm4oeClbMF0gICMgKEIsIFQsIEgpXG4gICAgICAgIHJldHVybiBzZWxmLmZjKG91dFs6LCAtMSwgOl0pXG5cbm5fY2xhc3NlcywgSCwgQiwgZXBvY2hzLCBUX2xhZyA9IDgsIDY0LCA2NCwgMzAwLCA1MFxuZm9yIGNlbGwgaW4gW1x1MDAyN3Jublx1MDAyNywgXHUwMDI3bHN0bVx1MDAyN106XG4gICAgbW9kZWwgPSBTZXFDbGFzc2lmaWVyKGNlbGwsIG5fY2xhc3NlcyArIDEsIEgsIG5fY2xhc3NlcylcbiAgICBvcHQgICA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0zKVxuICAgIGZvciBlcCBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICB4LCB5ID0gbWFrZV9jb3B5X2JhdGNoKEIsIFRfbGFnLCBuX2NsYXNzZXMpXG4gICAgICAgIGxvc3MgPSBubi5mdW5jdGlvbmFsLmNyb3NzX2VudHJvcHkobW9kZWwoeCksIHkpXG4gICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHgsIHkgID0gbWFrZV9jb3B5X2JhdGNoKDUxMiwgVF9sYWcsIG5fY2xhc3NlcylcbiAgICAgICAgYWNjICAgPSAobW9kZWwoeCkuYXJnbWF4KDEpID09IHkpLmZsb2F0KCkubWVhbigpLml0ZW0oKVxuICAgIHByaW50KGZcdTAwMjd7Y2VsbC51cHBlcigpOjRzfSBUX2xhZz17VF9sYWd9OiBhY2M9e2FjYzouNGZ9IChjaGFuY2U9ezEvbl9jbGFzc2VzOi40Zn0pXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9ydGhvZ29uYWwgSW5pdGlhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9ydGhvZ29uYWwgaW5pdGlhbGlzYXRpb24gc2V0cyBX4oKV4oKVIHRvIGFuIG9ydGhvZ29uYWwgbWF0cml4IChX4oKV4oKV4bWAV+KCleKClSA9IEkpLCBnaXZpbmcgc3BlY3RyYWwgcmFkaXVzIGV4YWN0bHkgMSBhdCBpbml0aWFsaXNhdGlvbi4gVGhpcyBtZWFucyBhbGwgZWlnZW52YWx1ZXMgbGllIG9uIHRoZSB1bml0IGNpcmNsZTogbm8gdmFuaXNoaW5nIG9yIGV4cGxvZGluZyBhdCBpbml0aWFsaXNhdGlvbi4gQXMgdHJhaW5pbmcgcHJvY2VlZHMsIFfigpXigpUgbW92ZXMgYXdheSBmcm9tIG9ydGhvZ29uYWxpdHksIGJ1dCB0aGUgY2FyZWZ1bCBzdGFydCBkZWxheXMgdGhlIG9uc2V0IG9mIHZhbmlzaGluZy4gT3J0aG9nb25hbCBpbml0IGhlbHBzIGJ1dCBkb2VzIG5vdCBzb2x2ZSB0aGUgbG9uZy10ZXJtIHByb2JsZW0g4oCUIGFmdGVyIG1hbnkgdHJhaW5pbmcgc3RlcHMsIHRoZSBzcGVjdHJhbCByYWRpdXMgY2FuIGRyaWZ0LiBJdCBpcyBtb3N0IHVzZWZ1bCBjb21iaW5lZCB3aXRoIG90aGVyIHRlY2huaXF1ZXMgKExTVE0sIGdyYWRpZW50IGNsaXBwaW5nLCBjYXJlZnVsIGxlYXJuaW5nIHJhdGVzKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5ucC5yYW5kb20uc2VlZCg0Mik7IHRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuSCA9IDMyXG5cbmRlZiBzcGVjdHJhbF9hbmFseXNpcyhXLCBsYWJlbCk6XG4gICAgZWlndmFscyA9IG5wLmxpbmFsZy5laWd2YWxzKFcpXG4gICAgbWFncyAgICA9IG5wLmFicyhlaWd2YWxzKVxuICAgIHByaW50KGZcdTAwMjd7bGFiZWx9Olx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBzcGVjdHJhbCByYWRpdXMgPSB7bWFncy5tYXgoKTouNGZ9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIG1pbiB8bGFtYmRhfCA9IHttYWdzLm1pbigpOi40Zn0sIGZyYWN0aW9uIFx1MDAzYyAxID0geyhtYWdzIFx1MDAzYyAxKS5tZWFuKCk6LjJmfVx1MDAyNylcbiAgICByZXR1cm4gbWFncy5tYXgoKVxuXG4jIFJhbmRvbSBub3JtYWwgaW5pdGlhbGl6YXRpb25cbldfcmFuZCA9IG5wLnJhbmRvbS5yYW5kbihILCBIKSAqIDAuMVxucmhvX3JhbmQgPSBzcGVjdHJhbF9hbmFseXNpcyhXX3JhbmQsIFx1MDAyN1JhbmRvbSBub3JtYWwgKHNjYWxlPTAuMSlcdTAwMjcpXG5cbiMgT3J0aG9nb25hbCBpbml0aWFsaXphdGlvblxuV190ID0gdG9yY2guZW1wdHkoSCwgSClcbm5uLmluaXQub3J0aG9nb25hbF8oV190KVxuV19vcnRoID0gV190Lm51bXB5KClcbnJob19vcnRoID0gc3BlY3RyYWxfYW5hbHlzaXMoV19vcnRoLCBcdTAwMjdPcnRob2dvbmFsIGluaXRcdTAwMjcpXG5cbiMgSWRlbnRpdHkgaW5pdGlhbGl6YXRpb25cbldfaWQgPSBucC5leWUoSClcbnJob19pZCA9IHNwZWN0cmFsX2FuYWx5c2lzKFdfaWQsIFx1MDAyN0lkZW50aXR5IGluaXRcdTAwMjcpXG5cbiMgRXN0aW1hdGVkIGdyYWRpZW50IGRlY2F5IGFmdGVyIFQgc3RlcHNcblQgPSA0MFxucHJpbnQoZlx1MDAyN0VzdGltYXRlZCBncmFkaWVudCBtYWduaXR1ZGUgYWZ0ZXIgVD17VH0gc3RlcHMgKHJob15UKTpcdTAwMjcpXG5mb3IgcmhvLCBsYWJlbCBpbiBbKHJob19yYW5kLCBcdTAwMjdSYW5kb21cdTAwMjcpLCAocmhvX29ydGgsIFx1MDAyN09ydGhvZ29uYWxcdTAwMjcpLCAocmhvX2lkLCBcdTAwMjdJZGVudGl0eVx1MDAyNyldOlxuICAgIHByaW50KGZcdTAwMjcgIHtsYWJlbH06IHJobz17cmhvOi40Zn0sIHJob157VH0gPSB7cmhvKipUOi40ZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uc2VxdWVuY2UgZm9yIFRyYWluaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdmFuaXNoaW5nIGdyYWRpZW50IGlzIHNwZWNpZmljYWxseSBhIHRyYWluaW5nIHByb2JsZW0sIG5vdCBhbiBpbmZlcmVuY2UgcHJvYmxlbS4gQXQgaW5mZXJlbmNlLCBhbiBSTk4gY2FuIGNhcnJ5IGluZm9ybWF0aW9uIGZvcndhcmQgdGhyb3VnaCBpdHMgaGlkZGVuIHN0YXRlIGZvciBhbnkgbnVtYmVyIG9mIHN0ZXBzIOKAlCB0aGUgaW5mb3JtYXRpb24gaXMgdGhlcmUsIGJ1dCB0aGUgbW9kZWwgd2FzIG5vdCBhYmxlIHRvIGxlYXJuIHRvIHVzZSBpdCBiZWNhdXNlIHRoZSB0cmFpbmluZyBzaWduYWwgY291bGQgbm90IHByb3BhZ2F0ZSBiYWNrIHRvIHRoZSBwYXJhbWV0ZXJzIHJlc3BvbnNpYmxlLiBFcXVpdmFsZW50bHk6IGlmIHlvdSBjb3VsZCBzb21laG93IHRyYWluIHRoZSBtb2RlbCB0byB1c2UgbG9uZy1yYW5nZSBwYXR0ZXJucywgaXQgd291bGQgd29yayBhdCBpbmZlcmVuY2UuIFRoZSBjaGFsbGVuZ2UgaXMgdGhhdCBncmFkaWVudCBkZXNjZW50IGNhbm5vdCBmaW5kIHRob3NlIHBhcmFtZXRlcnMgYmVjYXVzZSB0aGUgbG9zcyBzdXJmYWNlIHByb3ZpZGVzIG5vIGdyYWRpZW50IHNpZ25hbCBmb3IgbG9uZy1yYW5nZSB3ZWlnaHRzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiVmFuaXNoaW5nIEdyYWRpZW50IElzIGEgVHJhaW5pbmcgUHJvYmxlbSIsImNvbnRlbnQiOiJBIHRyYWluZWQgTFNUTSB3aXRoIGZvcmdldCBnYXRlcyBzZXQgdG8gMSBjYW4gcHJlc2VydmUgaW5mb3JtYXRpb24gZm9yIHRob3VzYW5kcyBvZiBzdGVwcyBhdCBpbmZlcmVuY2UuIFRoZSB2YW5pc2hpbmcgZ3JhZGllbnQgcHJvYmxlbSBwcmV2ZW50cyBncmFkaWVudCBkZXNjZW50IGZyb20gbGVhcm5pbmcgdG8gc2V0IHRob3NlIGZvcmdldCBnYXRlcyBhcHByb3ByaWF0ZWx5LiBHcmFkaWVudCBjbGlwcGluZyBoZWxwcyB3aXRoIGV4cGxvZGluZyBidXQgbm90IHZhbmlzaGluZy4gVGhlIGFyY2hpdGVjdHVyYWwgZml4IChMU1RNL0dSVSBhZGRpdGl2ZSBjZWxsIHN0YXRlKSBpcyB0aGUgb25seSByZWxpYWJsZSBzb2x1dGlvbjsgb3J0aG9nb25hbCBpbml0IGFuZCBiYXRjaCBub3JtIGFyZSBwYXJ0aWFsIG1pdGlnYXRpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNvbHV0aW9ucyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkdyYWRpZW50IFBhdGgiLCJMb25nLVJhbmdlIEFiaWxpdHkiLCJFeHRyYSBQYXJhbXMgdnMgUk5OIiwiVHJhaW5pbmcgQ29tcGxleGl0eSJdLCJyb3dzIjpbWyJWYW5pbGxhIFJOTiIsIlRocm91Z2ggV+KCleKCleG1gCBhdCBlYWNoIHN0ZXAgKHByb2R1Y3Qgb2YgbWF0cmljZXMpIiwiUG9vciDigJQgZXhwb25lbnRpYWwgZGVjYXkgaW4gVOKIkmsiLCJOb25lIOKAlCBiYXNlbGluZSIsIlNpbXBsZTsgZ3JhZGllbnQgY2xpcHBpbmcgcmVxdWlyZWQiXSxbIkxTVE0iLCJUaHJvdWdoIGNlbGwgc3RhdGUgQ+KCnCAoYWRkaXRpdmUgdXBkYXRlLCBkaWFnb25hbCBnYXRlKSIsIkdvb2Qg4oCUIGxpbmVhciBncmFkaWVudCBoaWdod2F5IiwiNHggKDQgZ2F0ZXMgaW5zdGVhZCBvZiAxKSIsIk1vZGVyYXRlOyBmb3JnZXQgZ2F0ZSBiaWFzIGluaXQgPSAxIl0sWyJHUlUiLCJUaHJvdWdoIHVwZGF0ZSBnYXRlIChjb252ZXggY29tYmluYXRpb24gb2YgaF9wcmV2IGFuZCBjYW5kaWRhdGUpIiwiR29vZCDigJQgc2ltaWxhciB0byBMU1RNIiwiM3ggKDMgZ2F0ZXMpIiwiU2ltcGxlciB0aGFuIExTVE07IG9mdGVuIGNvbXBhcmFibGUgcGVyZm9ybWFuY2UiXSxbIk9ydGhvZ29uYWwgaW5pdCIsIlN0aWxsIHRocm91Z2ggV+KCleKCleG1gCDigJQgYnV0IHNwZWN0cmFsIHJhZGl1cyA9IDEgYXQgaW5pdCIsIk1vZGVyYXRlIOKAlCBkZWxheXMgb25zZXQgb2YgdmFuaXNoaW5nIiwiTm9uZSDigJQgaW5pdCBjaGFuZ2Ugb25seSIsIlNhbWUgYXMgUk5OOyBlZmZlY3QgZGltaW5pc2hlcyBhZnRlciBlYXJseSB0cmFpbmluZyJdLFsiQ2hyb25vIGluaXQgKGZvcmdldCBiaWFzPTEpIiwiTFNUTSB3aXRoIGZvcmdldCBnYXRlIGluaXRpYWxpc2VkIG5lYXIgb3BlbiAoMSkiLCJHb29kIOKAlCBMU1RNIGJlbmVmaXQgKyBiZXR0ZXIgaW5pdCIsIlNhbWUgYXMgTFNUTSIsIkVhc3kgdG8gYXBwbHk7IHJlY29tbWVuZGVkIGRlZmF1bHQgZm9yIExTVE0gdHJhaW5pbmciXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVmFuaXNoaW5nIGdyYWRpZW50OiDigJZkTHQvZGhr4oCWIH4gc2lnbWFfbWF4KFdoaCleKHQtaykgLS0gZXhwb25lbnRpYWwgaW4gbGFnLiIsIkV4cGxvZGluZyBncmFkaWVudDogc2FtZSBmb3JtdWxhIHdpdGggc2lnbWFfbWF4IFx1MDAzZSAxOyBmaXggd2l0aCBncmFkaWVudCBjbGlwcGluZy4iLCJMU1RNIHNvbHV0aW9uOiBhZGRpdGl2ZSBjZWxsIHVwZGF0ZSBDdCA9IGZ0KkN0LTEgKyBpdCpDX3RpbGRlIGF2b2lkcyByZXBlYXRlZCBXaGggbXVsdGlwbGljYXRpb24uIiwiR1JVIHNvbHV0aW9uOiB1cGRhdGUgZ2F0ZSB6dCA9IHNpZ21hKFd6W2h0LTEsIHh0XSk7IGh0ID0gKDEtenQpKmh0LTEgKyB6dCpoX3RpbGRlLiIsIk9ydGhvZ29uYWwgaW5pdDogV2hoVCBXaGggPSBJIGF0IGluaXQ7IHNwZWN0cmFsIHJhZGl1cyA9IDE7IHVzZSBubi5pbml0Lm9ydGhvZ29uYWxfLiIsIlByYWN0aWNhbDogdXNlIExTVE0vR1JVIGZvciBhbnkgdGFzayB3aXRoIGRlcGVuZGVuY2llcyBcdTAwM2UgMjAgc3RlcHM7IHBsYWluIFJOTiBvbmx5IGZvciBzaG9ydCBzZXF1ZW5jZXMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Vanishing Gradient in RNNs — Mathematical Derivation

The vanishing gradient problem in RNNs is not a numerical issue — it is a consequence of the mathematical structure of gradient backpropagation through time. The gradient of the loss at step T with respect to the hidden state at step k is: dLₜ/dhₖ = (dLₜ/dhₜ) · Πⱼ₌ₖ₊₁ᵀ (dhⱼ/dhⱼ₋₁). Each Jacobian factor ∂hⱼ/∂hⱼ₋₁ = Wₕₕᵀ · diag(tanh'(hⱼ)) where tanh'(x) = 1 − tanh(x)² ∈ [0,1]. If the largest singular value of Wₕₕ is less than 1 (or tanh saturates), the product decays exponentially with T−k. This means the RNN gradient for a dependency at lag 50 is typically 10⁻¹⁵ times smaller than the gradient for a dependency at lag 1 — numerically zero in float32.

## Mathematical Derivation of Vanishing Gradient

Define the Jacobian of hⱼ with respect to hⱼ₋₁: Jⱼ = ∂hⱼ/∂hⱼ₋₁ = Wₕₕᵀ · diag(1 − hⱼ²). The gradient of the loss at time t with respect to hₖ is: dLₜ/dhₖ = (dLₜ/dhₜ) · Jₜ · Jₜ₋₁ · ... · Jₖ₊₁ (a product of t−k matrices). By the sub-multiplicativity of matrix norms: ‖Πⱼ Jⱼ‖ ≤ Πⱼ ‖Jⱼ‖. Since ‖Jⱼ‖ ≤ σ_max(Wₕₕ) · ‖diag(tanh')‖ ≤ σ_max(Wₕₕ), if σ_max(Wₕₕ) < 1 then ‖dLₜ/dhₖ‖ ≤ ‖dLₜ/dhₜ‖ · σ_max(Wₕₕ)^(t−k) → 0 exponentially. This is not an implementation bug — it is the fundamental reason plain RNNs cannot learn long-range dependencies.

```python
import numpy as np

np.random.seed(42)
T, H, I = 50, 16, 4

def gradient_norm_vs_lag(Whh_scale, T=50, H=16, I=4, seed=0):
    rng = np.random.RandomState(seed)
    Wxh = rng.randn(H, I) * 0.1
    Whh = rng.randn(H, H) * Whh_scale / np.sqrt(H)
    bh  = np.zeros((H, 1))
    xs  = [rng.randn(I, 1) for _ in range(T)]
    hs  = {-1: np.zeros((H, 1))}
    for t in range(T):
        hs[t] = np.tanh(Wxh @ xs[t] + Whh @ hs[t-1] + bh)
    dh = np.ones((H, 1)) / H  # unit gradient at t = T-1
    norms = {}
    for t in reversed(range(T)):
        norms[t] = float(np.linalg.norm(dh))
        dtanh    = (1 - hs[t]**2) * dh
        dh       = Whh.T @ dtanh
    return [norms[t] for t in range(T)]

print(f'{"Scale":>8} {"t=T-1":>12} {"t=T/2":>12} {"t=0":>12} {"Regime":>12}')
for scale, label in [(0.5, 'vanishing'), (1.0, 'marginal'), (2.0, 'exploding')]:
    norms = gradient_norm_vs_lag(scale)
    mid   = T // 2
    print(f'{scale:>8.1f} {norms[T-1]:>12.4e} {norms[mid]:>12.4e} '
          f'{norms[0]:>12.4e} {label:>12}')
print(f'For scale=0.5: ratio norms[t=0]/norms[t=T-1] ~ (0.5/sqrt(H))^{T} ~ 0')
```

## 1D RNN Analytical Gradient

For a 1D RNN (H=1), the gradient has a closed form that makes the decay explicit. With h_t = tanh(w_hh · h_{t-1} + w_xh · x_t + b), the gradient dL/dh_k = dL/dh_T · Πⱼ₌ₖ₊₁ᵀ (w_hh · (1 − h_j²)). If w_hh = 0.9 and tanh'(hⱼ) ≈ 0.9 (near zero), each factor is ~0.81, and after 50 steps the gradient is ~0.81⁵⁰ ≈ 1.8×10⁻⁵. This 1D analysis makes the exponential decay transparent and generalises to higher dimensions where σ_max(Wₕₕ) plays the role of w_hh.

```python
import numpy as np

"""
1D RNN: h_t = tanh(w_hh * h_{t-1} + w_xh * x_t + b)
Gradient: dL/dh_k = dL/dh_T * prod_{j=k+1}^{T} [w_hh * (1 - h_j^2)]
"""

np.random.seed(0)

def analytical_grad_1d(w_hh, T=30, w_xh=0.1, b=0.0, seed=0):
    rng = np.random.RandomState(seed)
    xs  = rng.randn(T) * 0.5
    hs  = [0.0]
    for t in range(T):
        hs.append(np.tanh(w_hh * hs[-1] + w_xh * xs[t] + b))
    # Compute dL/dh_k for each k given unit gradient at T-1
    dL_dhk = [0.0] * T
    dL_dhk[-1] = 1.0
    for k in range(T - 2, -1, -1):
        product = 1.0
        for j in range(k + 1, T):
            tanh_prime = 1.0 - hs[j + 1] ** 2
            product   *= w_hh * tanh_prime
        dL_dhk[k] = product
    return hs[1:], dL_dhk

print(f'{"w_hh":>8} {"lag":>5} {"dL/dh_k":>14} {"Analysis"}')
for w_hh in [0.5, 0.9, 1.0, 1.5]:
    _, grads = analytical_grad_1d(w_hh)
    T = len(grads)
    for lag in [1, 5, 15, 29]:
        k = T - 1 - lag
        g = abs(grads[k])
        regime = 'vanishing' if g < 1e-3 else ('exploding' if g > 1e3 else 'stable')
        print(f'{w_hh:>8.1f} {lag:>5} {g:>14.4e} {regime}')
```

## Gradient Norm vs Time Lag

Plotting gradient norm against time lag (distance from loss to hidden state) reveals the regime clearly: exponential decay for small Wₕₕ, near-constant for orthogonal Wₕₕ, exponential growth for large Wₕₕ. In practice, even well-initialised RNNs transition to vanishing within 20–50 steps as tanh saturation accumulates. The LSTM solves this with an additive cell state update (Cₜ = fₜ⊙Cₜ₋₁ + iₜ⊙C̃ₜ) — the forget gate allows gradient to flow through the cell state with only elementwise multiplication by fₜ, avoiding the repeated matrix multiplication by Wₕₕᵀ.

## LSTM and GRU as Solutions

The LSTM introduces a cell state Cₜ that is updated additively: Cₜ = fₜ⊙Cₜ₋₁ + iₜ⊙C̃ₜ. The gradient of the loss with respect to the cell state at time k flows back through the forget gate only: ∂Cₜ/∂Cₜ₋₁ = diag(fₜ). Since fₜ ∈ (0,1)ᴴ (element-wise sigmoid), this is a diagonal matrix — no repeated matrix multiplication by Wₕₕ. With forget gates initialised near 1 (bias = 1), the gradient can flow through hundreds of steps without exponential decay. The GRU uses a simpler two-gate design that achieves similar long-range gradient flow.

```python
import torch
import torch.nn as nn

torch.manual_seed(42)

def make_copy_batch(B=64, T=50, n_classes=8):
    """Copy task: remember item from t=0 after T filler steps."""
    target = torch.randint(n_classes, (B,))
    x = torch.zeros(B, T + 1, n_classes + 1)
    x[:, 0, :n_classes] = nn.functional.one_hot(target, n_classes).float()
    x[:, 1:, n_classes] = 1.0  # filler signal
    return x, target

class SeqClassifier(nn.Module):
    def __init__(self, cell_type, inp, hid, n_classes):
        super().__init__()
        RNNClass = nn.RNN if cell_type == 'rnn' else nn.LSTM
        self.rnn  = RNNClass(inp, hid, batch_first=True)
        self.fc   = nn.Linear(hid, n_classes)
        self.is_lstm = (cell_type == 'lstm')
    def forward(self, x):
        out = self.rnn(x)[0]  # (B, T, H)
        return self.fc(out[:, -1, :])

n_classes, H, B, epochs, T_lag = 8, 64, 64, 300, 50
for cell in ['rnn', 'lstm']:
    model = SeqClassifier(cell, n_classes + 1, H, n_classes)
    opt   = torch.optim.Adam(model.parameters(), lr=1e-3)
    for ep in range(epochs):
        x, y = make_copy_batch(B, T_lag, n_classes)
        loss = nn.functional.cross_entropy(model(x), y)
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        x, y  = make_copy_batch(512, T_lag, n_classes)
        acc   = (model(x).argmax(1) == y).float().mean().item()
    print(f'{cell.upper():4s} T_lag={T_lag}: acc={acc:.4f} (chance={1/n_classes:.4f})')
```

## Orthogonal Initialization

Orthogonal initialisation sets Wₕₕ to an orthogonal matrix (WₕₕᵀWₕₕ = I), giving spectral radius exactly 1 at initialisation. This means all eigenvalues lie on the unit circle: no vanishing or exploding at initialisation. As training proceeds, Wₕₕ moves away from orthogonality, but the careful start delays the onset of vanishing. Orthogonal init helps but does not solve the long-term problem — after many training steps, the spectral radius can drift. It is most useful combined with other techniques (LSTM, gradient clipping, careful learning rates).

```python
import numpy as np
import torch
import torch.nn as nn

np.random.seed(42); torch.manual_seed(42)
H = 32

def spectral_analysis(W, label):
    eigvals = np.linalg.eigvals(W)
    mags    = np.abs(eigvals)
    print(f'{label}:')
    print(f'  spectral radius = {mags.max():.4f}')
    print(f'  min |lambda| = {mags.min():.4f}, fraction < 1 = {(mags < 1).mean():.2f}')
    return mags.max()

# Random normal initialization
W_rand = np.random.randn(H, H) * 0.1
rho_rand = spectral_analysis(W_rand, 'Random normal (scale=0.1)')

# Orthogonal initialization
W_t = torch.empty(H, H)
nn.init.orthogonal_(W_t)
W_orth = W_t.numpy()
rho_orth = spectral_analysis(W_orth, 'Orthogonal init')

# Identity initialization
W_id = np.eye(H)
rho_id = spectral_analysis(W_id, 'Identity init')

# Estimated gradient decay after T steps
T = 40
print(f'Estimated gradient magnitude after T={T} steps (rho^T):')
for rho, label in [(rho_rand, 'Random'), (rho_orth, 'Orthogonal'), (rho_id, 'Identity')]:
    print(f'  {label}: rho={rho:.4f}, rho^{T} = {rho**T:.4e}')
```

## Consequence for Training

The vanishing gradient is specifically a training problem, not an inference problem. At inference, an RNN can carry information forward through its hidden state for any number of steps — the information is there, but the model was not able to learn to use it because the training signal could not propagate back to the parameters responsible. Equivalently: if you could somehow train the model to use long-range patterns, it would work at inference. The challenge is that gradient descent cannot find those parameters because the loss surface provides no gradient signal for long-range weights.

> **Vanishing Gradient Is a Training Problem**: A trained LSTM with forget gates set to 1 can preserve information for thousands of steps at inference. The vanishing gradient problem prevents gradient descent from learning to set those forget gates appropriately. Gradient clipping helps with exploding but not vanishing. The architectural fix (LSTM/GRU additive cell state) is the only reliable solution; orthogonal init and batch norm are partial mitigations.

## Solutions Comparison

| Method | Gradient Path | Long-Range Ability | Extra Params vs RNN | Training Complexity |
| --- | --- | --- | --- | --- |
| Vanilla RNN | Through Wₕₕᵀ at each step (product of matrices) | Poor — exponential decay in T−k | None — baseline | Simple; gradient clipping required |
| LSTM | Through cell state Cₜ (additive update, diagonal gate) | Good — linear gradient highway | 4x (4 gates instead of 1) | Moderate; forget gate bias init = 1 |
| GRU | Through update gate (convex combination of h_prev and candidate) | Good — similar to LSTM | 3x (3 gates) | Simpler than LSTM; often comparable performance |
| Orthogonal init | Still through Wₕₕᵀ — but spectral radius = 1 at init | Moderate — delays onset of vanishing | None — init change only | Same as RNN; effect diminishes after early training |
| Chrono init (forget bias=1) | LSTM with forget gate initialised near open (1) | Good — LSTM benefit + better init | Same as LSTM | Easy to apply; recommended default for LSTM training |

- Vanishing gradient: ‖dLt/dhk‖ ~ sigma_max(Whh)^(t-k) -- exponential in lag.
- Exploding gradient: same formula with sigma_max > 1; fix with gradient clipping.
- LSTM solution: additive cell update Ct = ft*Ct-1 + it*C_tilde avoids repeated Whh multiplication.
- GRU solution: update gate zt = sigma(Wz[ht-1, xt]); ht = (1-zt)*ht-1 + zt*h_tilde.
- Orthogonal init: WhhT Whh = I at init; spectral radius = 1; use nn.init.orthogonal_.
- Practical: use LSTM/GRU for any task with dependencies > 20 steps; plain RNN only for short sequences.

---

