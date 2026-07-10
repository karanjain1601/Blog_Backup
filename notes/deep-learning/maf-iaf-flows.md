---
title: "MAF and IAF — Autoregressive Normalizing Flows"
slug: "maf-iaf-flows"
description: "MAF (Masked Autoregressive Flow) evaluates density in O(1) using MADE but samples in O(d). IAF reverses the trade-off: O(1) sampling, O(d) density. Covers MADE masking, forward/inverse passes, and when to use each (density estimation vs VAE posteriors)."
tags: ["deep-learning", "generative-models", "diffusion-models", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXV0b3JlZ3Jlc3NpdmUgbW9kZWxzIGZhY3Rvcml6ZSBwKHgpID0gzqAgcCh4X2kgfCB4X3tcdTAwM2NpfSkuIE1BRiAoUGFwYW1ha2FyaW9zIGV0IGFsLiwgMjAxNykgcmVmcmFtZXMgdGhpcyBhcyBhIG5vcm1hbGl6aW5nIGZsb3cgd2hlcmUgZWFjaCBjb25kaXRpb25hbCBpcyBhIEdhdXNzaWFuOiBwKHhfaSB8IHhfe1x1MDAzY2l9KSA9IE4ozrxfaSh4X3tcdTAwM2NpfSksIM+DX2koeF97XHUwMDNjaX0pKS4gVGhlIHJlc3VsdGluZyB0cmFuc2Zvcm1hdGlvbiB5X2kgPSAoeF9pIC0gzrxfaSkgLyDPg19pIGlzIGFuIGludmVydGlibGUgYWZmaW5lIG1hcC4gQmVjYXVzZSBNQURFIGNvbXB1dGVzIGFsbCDOvF9pLCDPg19pIGluIGEgc2luZ2xlIGZvcndhcmQgcGFzcywgZGVuc2l0eSBldmFsdWF0aW9uIGlzIE8oMSkuIFNhbXBsaW5nIHJlcXVpcmVzIGludmVydGluZyB0aGUgYXV0b3JlZ3Jlc3NpdmUgc3RydWN0dXJlIHNlcXVlbnRpYWxseSwgbWFraW5nIGl0IE8oZCkuIElBRiAoS2luZ21hIGV0IGFsLiwgMjAxNikgcmV2ZXJzZXMgdGhlIHBhcmFtZXRlcml6YXRpb24gdG8gZ2V0IGZhc3Qgc2FtcGxpbmcgYXQgdGhlIGNvc3Qgb2Ygc2xvdyBkZW5zaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1dG9yZWdyZXNzaXZlIE1vZGVscyBhcyBOb3JtYWxpemluZyBGbG93cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBub3JtYWxpemluZyBmbG93IHJlcXVpcmVzIGEgYmlqZWN0aXZlIG1hcHBpbmcgZjogeCDihpIgeiB3aXRoIHRyYWN0YWJsZSBKYWNvYmlhbiBkZXRlcm1pbmFudC4gQW4gYXV0b3JlZ3Jlc3NpdmUgbW9kZWwgd2hlcmUgeV9pID0gKHhfaSAtIM68X2koeF97XHUwMDNjaX0pKSAvIM+DX2koeF97XHUwMDNjaX0pIGlzIGV4YWN0bHkgdGhpczogdGhlIEphY29iaWFuIGlzIGxvd2VyLXRyaWFuZ3VsYXIgKG91dHB1dCB5X2kgZGVwZW5kcyBvbiB4X3viiaRpfSBidXQgdGhlIHRyYW5zZm9ybWF0aW9uIG9mIHhfaSBkZXBlbmRzIG9ubHkgb24geF97XHUwMDNjaX0pLCBzbyBpdHMgZGV0ZXJtaW5hbnQgaXMgdGhlIHByb2R1Y3Qgb2YgZGlhZ29uYWwgZWxlbWVudHM6IGRldCBKID0gzqBfaSAoMS/Pg19pKS4gVGhlIGxvZy1kZXRlcm1pbmFudCBpcyAtzqNfaSBsb2cgz4NfaS4gVGhpcyBzdHJ1Y3R1cmUg4oCUIGxvd2VyLXRyaWFuZ3VsYXIgSmFjb2JpYW4sIHVuaXQtZGlhZ29uYWwgb3IgZGlhZ29uYWwg4oCUIGlzIHRoZSBrZXkgdGhhdCBsaW5rcyBhdXRvcmVncmVzc2l2ZSBtb2RlbHMgdG8gbm9ybWFsaXppbmcgZmxvd3MgYW5kIGp1c3RpZmllcyB1c2luZyBNQURFIGFzIHRoZSBiYWNrYm9uZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNQURFIOKAlCBNYXNrZWQgQXV0b2VuY29kZXIgZm9yIERpc3RyaWJ1dGlvbiBFc3RpbWF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNQURFIChHZXJtYWluIGV0IGFsLiwgMjAxNSkgaW1wbGVtZW50cyBhIG1hc2tlZCBNTFAgdGhhdCBjb21wdXRlcyBhbGwgY29uZGl0aW9uYWxzIHAoeF9pIHwgeF97XHUwMDNjaX0pIGluIGEgc2luZ2xlIGZvcndhcmQgcGFzcy4gRWFjaCBoaWRkZW4gdW5pdCBpcyBhc3NpZ25lZCBhIGRlZ3JlZSBtIOKIiCB7MCwgLi4uLCBkLTF9OyBjb25uZWN0aW9ucyBhcmUgbWFza2VkIHNvIHRoYXQgdW5pdCBqIGluIGxheWVyIGwgY2FuIG9ubHkgcmVjZWl2ZSBpbnB1dCBmcm9tIHVuaXRzIGluIGxheWVyIGwtMSB3aXRoIGRlZ3JlZSDiiaQgbV9qLiBUaGUgb3V0cHV0IGZvciB4X2kgdXNlcyBvbmx5IGhpZGRlbiB1bml0cyB3aXRoIGRlZ3JlZSBcdTAwM2MgaSwgZW5mb3JjaW5nIHRoZSBhdXRvcmVncmVzc2l2ZSBwcm9wZXJ0eS4gVGhlIG1hc2sgbWF0cmljZXMgYXJlIGZpeGVkIGF0IGluaXRpYWxpemF0aW9uOyB0aGUgd2VpZ2h0cyBhcmUgbGVhcm5lZCBub3JtYWxseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgTUFERShubi5Nb2R1bGUpOlxuICAgIFwiXCJcIk1hc2tlZCBBdXRvZW5jb2RlciBmb3IgRGlzdHJpYnV0aW9uIEVzdGltYXRpb24gKEdlcm1haW4gZXQgYWwuIDIwMTUpLlxuICAgIEVuZm9yY2VzIG91dHB1dF9pIGRlcGVuZHMgb25seSBvbiBpbnB1dHMgMC4uaS0xIHZpYSBzdGF0aWMgbWFza3MuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGQsIGhpZGRlbj0xMjgsIG5fb3V0PTIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5kLCBzZWxmLm5fb3V0ID0gZCwgbl9vdXRcbiAgICAgICAgbV9pbiAgPSB0b3JjaC5hcmFuZ2UoZClcbiAgICAgICAgbV9oICAgPSB0b3JjaC5yYW5kaW50KDAsIGQgLSAxLCAoaGlkZGVuLCkpXG4gICAgICAgIG1fb3V0ID0gdG9yY2guYXJhbmdlKGQpLnJlcGVhdChuX291dClcbiAgICAgICAgIyBtYXNrW2ksal09MSBpZmYgaGlkZGVuIHVuaXQgaSBjYW4gc2VlIGlucHV0IGpcbiAgICAgICAgc2VsZi5tYXNrMSA9IChtX2gudW5zcXVlZXplKDEpIFx1MDAzZT0gbV9pbi51bnNxdWVlemUoMCkpLmZsb2F0KCkgICAjIChoLCBkKVxuICAgICAgICAjIG1hc2tbaSxqXT0xIGlmZiBvdXRwdXQgaSBjYW4gc2VlIGhpZGRlbiB1bml0IGogKHN0cmljdCBpbmVxdWFsaXR5KVxuICAgICAgICBzZWxmLm1hc2syID0gKG1fb3V0LnVuc3F1ZWV6ZSgxKSBcdTAwM2UgbV9oLnVuc3F1ZWV6ZSgwKSkuZmxvYXQoKSAgICMgKGQqbiwgaClcbiAgICAgICAgc2VsZi5mYzEgPSBubi5MaW5lYXIoZCwgaGlkZGVuKVxuICAgICAgICBzZWxmLmZjMiA9IG5uLkxpbmVhcihoaWRkZW4sIGQgKiBuX291dClcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3X20xXHUwMDI3LCBzZWxmLm1hc2sxKVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdfbTJcdTAwMjcsIHNlbGYubWFzazIpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgaCA9IEYucmVsdShGLmxpbmVhcih4LCBzZWxmLmZjMS53ZWlnaHQgKiBzZWxmLl9tMSwgc2VsZi5mYzEuYmlhcykpXG4gICAgICAgIG8gPSBGLmxpbmVhcihoLCBzZWxmLmZjMi53ZWlnaHQgKiBzZWxmLl9tMiwgc2VsZi5mYzIuYmlhcylcbiAgICAgICAgcmV0dXJuIG8udmlldyh4LnNoYXBlWzBdLCBzZWxmLmQsIHNlbGYubl9vdXQpXG5cbmQsIEIgPSA4LCAxNlxubWFkZSA9IE1BREUoZCwgaGlkZGVuPTY0KVxueCA9IHRvcmNoLnJhbmRuKEIsIGQpXG5vdXQgPSBtYWRlKHgpXG5wcmludChmXCJPdXRwdXQgc2hhcGU6IHtvdXQuc2hhcGV9ICAoYmF0Y2g9e0J9LCBkPXtkfSwgMiBwYXJhbXMgcGVyIGRpbSlcIilcbnByaW50KFwiTUFERTogYWxsIGNvbmRpdGlvbmFscyBjb21wdXRlZCBpbiBPTkUgZm9yd2FyZCBwYXNzIC1cdTAwM2UgTygxKSBkZW5zaXR5IGV2YWxcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNQUYg4oCUIEZvcndhcmQgUGFzcyAoRGVuc2l0eSBFdmFsdWF0aW9uKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gTUFGIHRoZSB0cmFuc2Zvcm1hdGlvbiBpcyB5X2kgPSAoeF9pIC0gzrxfaSh4X3tcdTAwM2NpfSkpIMOXIGV4cCgtzrFfaSh4X3tcdTAwM2NpfSkpLiBNQURFIGNvbXB1dGVzIGFsbCAozrxfaSwgzrFfaSkgaW4gb25lIHBhc3MgZnJvbSB4LCBzbyB0aGUgZm9yd2FyZCB0cmFuc2Zvcm1hdGlvbiAoeCDihpIgeSwgdXNlZCBmb3IgZGVuc2l0eSBldmFsdWF0aW9uKSBpcyBPKDEpLiBUaGUgbG9nLWRldGVybWluYW50IGlzIGRpYWdvbmFsOiBsb2d8ZGV0IEp8ID0gLc6jX2kgzrFfaSh4X3tcdTAwM2NpfSksIHdoaWNoIGNvbWVzIG91dCBvZiB0aGUgc2FtZSBNQURFIHBhc3MuIFRyYWluaW5nIGEgc3RhY2sgb2YgTUFGIGxheWVycyBieSBtYXhpbXVtIGxpa2VsaWhvb2QgaXMgdGhlcmVmb3JlIGVmZmljaWVudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgTUFGTGF5ZXIobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTaW5nbGUgTUFGIGxheWVyLiBGb3J3YXJkIChkZW5zaXR5KSBpcyBPKDEpOyBpbnZlcnNlIChzYW1wbGUpIGlzIE8oZCkuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGQsIGhpZGRlbj0xMjgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5tYWRlID0gTUFERShkLCBoaWRkZW49aGlkZGVuLCBuX291dD0yKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIFwiXCJcIkRlbnNpdHkgZXZhbDogb25lIE1BREUgcGFzcyBjb21wdXRlcyBhbGwgKG11X2ksIGxvZ19zaWdtYV9pKS5cIlwiXCJcbiAgICAgICAgcGFyYW1zICA9IHNlbGYubWFkZSh4KSAgICAgICAgICAgICAgIyAoQiwgZCwgMilcbiAgICAgICAgbXUgICAgICA9IHBhcmFtc1suLi4sIDBdXG4gICAgICAgIGxvZ19zaWcgPSBwYXJhbXNbLi4uLCAxXVxuICAgICAgICB5ICAgICAgID0gKHggLSBtdSkgKiAoLWxvZ19zaWcpLmV4cCgpXG4gICAgICAgIGxvZ19kZXQgPSAtbG9nX3NpZy5zdW0oZGltPS0xKSAgICAgIyAoQiwpXG4gICAgICAgIHJldHVybiB5LCBsb2dfZGV0XG5cbiAgICBkZWYgbG9nX3Byb2Ioc2VsZiwgeCk6XG4gICAgICAgIHksIGxvZ19kZXQgPSBzZWxmLmZvcndhcmQoeClcbiAgICAgICAgbG9nX3B6ID0gLTAuNSAqICh5ICoqIDIgKyB0b3JjaC5sb2codG9yY2gudGVuc29yKDIgKiB0b3JjaC5waSkpKS5zdW0oLTEpXG4gICAgICAgIHJldHVybiBsb2dfcHogKyBsb2dfZGV0XG5cbmQsIEIgPSA4LCAzMlxubGF5ZXIgPSBNQUZMYXllcihkKVxueCA9IHRvcmNoLnJhbmRuKEIsIGQpXG55LCBsZCA9IGxheWVyLmZvcndhcmQoeClcbmxwICAgPSBsYXllci5sb2dfcHJvYih4KVxucHJpbnQoZlwieDoge3guc2hhcGV9IC1cdTAwM2UgeToge3kuc2hhcGV9XCIpXG5wcmludChmXCJsb2dfZGV0IHJhbmdlOiBbe2xkLm1pbigpOi4yZn0sIHtsZC5tYXgoKTouMmZ9XVwiKVxucHJpbnQoZlwibG9nX3Byb2IgcmFuZ2U6IFt7bHAubWluKCk6LjJmfSwge2xwLm1heCgpOi4yZn1dXCIpXG5wcmludChcIkZvcndhcmQgKGRlbnNpdHkpOiAxIE1BREUgcGFzcyBmb3IgZW50aXJlIGJhdGNoIC1cdTAwM2UgTygxKVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1BRiDigJQgSW52ZXJzZSBQYXNzIChTYW1wbGluZykifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIHNhbXBsZSBmcm9tIE1BRjogZHJhdyB5IH4gTigwLEkpLCB0aGVuIGludmVydCB5X2kgPSAoeF9pIC0gzrxfaSkgLyDPg19pIHRvIGdldCB4X2kgPSB5X2kgw5cgz4NfaSh4X3tcdTAwM2NpfSkgKyDOvF9pKHhfe1x1MDAzY2l9KS4gQ29tcHV0aW5nIHhfaSByZXF1aXJlcyB4X3tcdTAwM2NpfSwgc28gdGhlIGludmVyc2lvbiBpcyBpbmhlcmVudGx5IHNlcXVlbnRpYWw6IGNvbXB1dGUgeF8xLCB0aGVuIHhfMiAodXNpbmcgeF8xKSwg4oCmLCB4X2QgKHVzaW5nIHhfezE6ZC0xfSkuIEVhY2ggc3RlcCBjYWxscyBNQURFIG9uY2UsIHlpZWxkaW5nIE8oZCkgZXZhbHVhdGlvbnMgdG90YWwuIFRoaXMgbWFrZXMgTUFGIGltcHJhY3RpY2FsIGFzIGEgZGVjb2RlciBvciBwb3N0ZXJpb3IgaW4gYSBWQUUgd2hlcmUgc2FtcGxpbmcgc3BlZWQgbWF0dGVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdGltZVxuXG5kZWYgbWFmX2ludmVyc2UobGF5ZXIsIHksIGQpOlxuICAgIFwiXCJcIkludmVydCBNQUY6IHhfaSA9IHlfaSAqIGV4cChsb2dfc19pKHhfe1x1MDAzY2l9KSkgKyBtdV9pKHhfe1x1MDAzY2l9KS5cbiAgICBSZXF1aXJlcyBkIHNlcXVlbnRpYWwgTUFERSBldmFsdWF0aW9ucy5cIlwiXCJcbiAgICB4ID0gdG9yY2guemVyb3NfbGlrZSh5KVxuICAgIGZvciBpIGluIHJhbmdlKGQpOlxuICAgICAgICBwYXJhbXMgID0gbGF5ZXIubWFkZSh4KSAgICAgICAjIGZ1bGwgTUFERSBwYXNzLCBidXQgb25seSBvdXRwdXQgaSB1c2VkXG4gICAgICAgIG11X2kgICAgPSBwYXJhbXNbOiwgaSwgMF1cbiAgICAgICAgbG9nX3NpICA9IHBhcmFtc1s6LCBpLCAxXVxuICAgICAgICB4WzosIGldID0geVs6LCBpXSAqIGxvZ19zaS5leHAoKSArIG11X2lcbiAgICByZXR1cm4geFxuXG5kLCBCID0gOCwgMTZcbmxheWVyICA9IE1BRkxheWVyKGQpXG54X29yaWcgPSB0b3JjaC5yYW5kbihCLCBkKVxueSwgXyAgID0gbGF5ZXIuZm9yd2FyZCh4X29yaWcpXG5cbnQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxueF9yZWMgPSBtYWZfaW52ZXJzZShsYXllciwgeSwgZClcbm1zX3NhbXBsZSA9ICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApICogMTAwMFxuXG50MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbl8sIF8gPSBsYXllci5mb3J3YXJkKHhfb3JpZylcbm1zX2RlbnNpdHkgPSAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAqIDEwMDBcblxucHJpbnQoZlwiUmVjb25zdHJ1Y3Rpb24gZXJyb3I6IHsoeF9vcmlnIC0geF9yZWMpLmFicygpLm1heCgpOi4yZX1cIilcbnByaW50KGZcIkRlbnNpdHkgZXZhbDogIHttc19kZW5zaXR5Oi4zZn0gbXMgIFsxIE1BREUgcGFzc11cIilcbnByaW50KGZcIlNhbXBsaW5nOiAgICAgIHttc19zYW1wbGU6LjNmfSBtcyAgW3tkfSBNQURFIHBhc3Nlc11cIilcbnByaW50KGZcIlNsb3dkb3duOiB+e21zX3NhbXBsZS9tYXgobXNfZGVuc2l0eSwwLjAwMSk6LjFmfXggIChzY2FsZXMgYXMgTyhkKSlcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJQUYg4oCUIEludmVyc2UgQXV0b3JlZ3Jlc3NpdmUgRmxvdyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSUFGIChLaW5nbWEgZXQgYWwuLCAyMDE2KSByZXZlcnNlcyB0aGUgTUFGIHBhcmFtZXRlcml6YXRpb246IHRoZSB0cmFuc2Zvcm1hdGlvbiBpcyB6X2kgPSDOvF9pKHpfe1x1MDAzY2l9KSArIM+DX2koel97XHUwMDNjaX0pIMOXIM61X2kgd2hlcmUgzrUgfiBOKDAsSSkuIE5vdyB0aGUgZm9yd2FyZCBwYXNzIChzYW1wbGluZykgaXMgeCDihpIgeiwgd2hpY2ggaXMgTygxKSBzaW5jZSBhbGwgKM68X2ksIM+DX2kpIGFyZSBmdW5jdGlvbnMgb2Ygel97XHUwMDNjaX0gdGhhdCBjYW4gYmUgY29tcHV0ZWQgdmlhIE1BREUgaW4gb25lIHBhc3MgZnJvbSB6LiBCdXQgZGVuc2l0eSBldmFsdWF0aW9uIHJlcXVpcmVzIGludmVydGluZzogel9pID0gKHhfaSAtIM68X2koel97XHUwMDNjaX0pKSAvIM+DX2koel97XHUwMDNjaX0pLCB3aGljaCBpcyBzZXF1ZW50aWFsIGluIHpfe1x1MDAzY2l9IOKAlCBPKGQpIHBhc3Nlcy4gSUFGIGlzIHRoZXJlZm9yZSBpZGVhbCBhcyBhIGZsZXhpYmxlIHBvc3RlcmlvciBhcHByb3hpbWF0aW9uIGluIFZBRXMgKGZhc3Qgc2FtcGxpbmcgZHVyaW5nIHRyYWluaW5nKSwgYnV0IG5vdCBmb3Igc3RhbmRhbG9uZSBkZW5zaXR5IGVzdGltYXRpb24uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6Ik1BRiB2cyBJQUYgVXNlIENhc2VzIiwiY29udGVudCI6IlVzZSBNQUYgd2hlbiB5b3UgbmVlZCBmYXN0IGRlbnNpdHkgZXZhbHVhdGlvbiBhbmQgY2FuIHRvbGVyYXRlIHNsb3cgc2FtcGxpbmc6IHRyYWluaW5nIGEgZ2VuZXJhdGl2ZSBmbG93IG9uIGxvZy1saWtlbGlob29kLCBvciBhcyBhIHByaW9yLiBVc2UgSUFGIHdoZW4geW91IG5lZWQgZmFzdCBzYW1wbGluZyBhbmQgY2FuIHRvbGVyYXRlIHNsb3cgZGVuc2l0eTogYXMgYSBmbGV4aWJsZSB2YXJpYXRpb25hbCBwb3N0ZXJpb3IgcSh6fHgpIGluIGEgVkFFLCB3aGVyZSB5b3Ugc2FtcGxlIHogYXQgZXZlcnkgdHJhaW5pbmcgc3RlcCBidXQgcmFyZWx5IGV2YWx1YXRlIGl0cyBleGFjdCBkZW5zaXR5LiBQYXJhbGxlbCBXYXZlTmV0IHVzZXMgSUFGIGFzIGEgZmFzdCBzdHVkZW50IGRpc3RpbGxlZCBmcm9tIGFuIGF1dG9yZWdyZXNzaXZlIFdhdmVOZXQgdGVhY2hlci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZW5zaXR5IHZzIFNhbXBsaW5nIFNwZWVkIEJlbmNobWFyayJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0aW1lXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGZsb3dfYmVuY2htYXJrKGQ9MTYsIEI9MjU2LCBuX2xheWVycz00LCBuX3RyaWFscz0zMCk6XG4gICAgXCJcIlwiV2FsbC1jbG9jayBjb21wYXJpc29uOiBkZW5zaXR5IGV2YWwgdnMgc2FtcGxpbmcgaW4gTUFGLlwiXCJcIlxuICAgIGR1bW15ID0gdG9yY2guemVyb3MoQiwgZCwgMilcbiAgICB0aW1pbmdzID0ge31cblxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGZvciBfIGluIHJhbmdlKG5fdHJpYWxzKTpcbiAgICAgICAgeCA9IHRvcmNoLnJhbmRuKEIsIGQpXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKTpcbiAgICAgICAgICAgIG11LCBsb2dfcyA9IGR1bW15Wy4uLiwgMF0sIGR1bW15Wy4uLiwgMV1cbiAgICAgICAgICAgIHggPSAoeCAtIG11KSAqICgtbG9nX3MpLmV4cCgpXG4gICAgdGltaW5nc1tcdTAwMjdkZW5zaXR5XHUwMDI3XSA9ICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApIC8gbl90cmlhbHMgKiAxMDAwXG5cbiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICBmb3IgXyBpbiByYW5nZShuX3RyaWFscyk6XG4gICAgICAgIHogPSB0b3JjaC5yYW5kbihCLCBkKVxuICAgICAgICBmb3IgXyBpbiByYW5nZShuX2xheWVycyk6XG4gICAgICAgICAgICB4X291dCA9IHRvcmNoLnplcm9zX2xpa2UoeilcbiAgICAgICAgICAgIGZvciBpIGluIHJhbmdlKGQpOlxuICAgICAgICAgICAgICAgIHhfb3V0WzosIGldID0gels6LCBpXSAgICMgcGxhY2Vob2xkZXIgc2VxdWVudGlhbCBzdGVwXG4gICAgICAgICAgICB6ID0geF9vdXRcbiAgICB0aW1pbmdzW1x1MDAyN3NhbXBsZVx1MDAyN10gPSAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAvIG5fdHJpYWxzICogMTAwMFxuXG4gICAgcHJpbnQoZlwiQmVuY2htYXJrOiBkPXtkfSwgQj17Qn0sIGxheWVycz17bl9sYXllcnN9XCIpXG4gICAgcHJpbnQoZlwiICBEZW5zaXR5IGV2YWw6IHt0aW1pbmdzW1x1MDAyN2RlbnNpdHlcdTAwMjddOjYuMmZ9IG1zICAoTygxKS9sYXllciwgcGFyYWxsZWwgb3ZlciBkKVwiKVxuICAgIHByaW50KGZcIiAgU2FtcGxpbmc6ICAgICB7dGltaW5nc1tcdTAwMjdzYW1wbGVcdTAwMjddOjYuMmZ9IG1zICAoTyhkKS9sYXllciwgc2VyaWFsKVwiKVxuICAgIHByaW50KGZcIiAgUmF0aW86ICAgICAgICB7dGltaW5nc1tcdTAwMjdzYW1wbGVcdTAwMjddL21heCh0aW1pbmdzW1x1MDAyN2RlbnNpdHlcdTAwMjddLDAuMDAxKTouMWZ9eFwiKVxuICAgIHByaW50KFwiICBJQUYgcmV2ZXJzZXM6IHNhbXBsaW5nIE8oMSksIGRlbnNpdHkgTyhkKVwiKVxuICAgIHByaW50KFwiICBVc2UgTUFGIGZvciBORiB0cmFpbmluZzsgSUFGIGZvciBWQUUgcG9zdGVyaW9yXCIpXG5cbmZsb3dfYmVuY2htYXJrKGQ9MTYpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmxvdyBNb2RlbCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiRm9yd2FyZCAoZGVuc2l0eSkiLCJJbnZlcnNlIChzYW1wbGUpIiwiRXhwcmVzc2l2aXR5IiwiUGFyYWxsZWwgdHJhaW4iLCJQYXJhbGxlbCBzYW1wbGUiXSwicm93cyI6W1siTklDRSIsIk8oMSkiLCJPKDEpIiwiTG93IChhZGRpdGl2ZSBvbmx5KSIsIlllcyIsIlllcyJdLFsiUmVhbE5WUCIsIk8oMSkiLCJPKDEpIiwiTWVkaXVtIChhZmZpbmUgY291cGxpbmcpIiwiWWVzIiwiWWVzIl0sWyJNQUYiLCJPKDEpIHZpYSBNQURFIiwiTyhkKSBzZXF1ZW50aWFsIiwiSGlnaCAoYXV0b3JlZ3Jlc3NpdmUpIiwiWWVzIiwiTm8iXSxbIklBRiIsIk8oZCkgc2VxdWVudGlhbCIsIk8oMSkgdmlhIE1BREUiLCJIaWdoIChhdXRvcmVncmVzc2l2ZSkiLCJObyAoZGVuc2l0eSBuZWVkZWQpIiwiWWVzIl0sWyJHbG93IiwiTygxKSIsIk8oMSkiLCJIaWdoIChsZWFybmFibGUgcGVybSkiLCJZZXMiLCJZZXMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5ldXJhbCBTcGxpbmUgRmxvd3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5ldXJhbCBTcGxpbmUgRmxvd3MgKER1cmthbiBldCBhbC4sIDIwMTkpIHJlcGxhY2UgdGhlIGFmZmluZSBjb3VwbGluZyAoc2NhbGUgKyBzaGlmdCkgd2l0aCBhIG1vbm90b25lIHJhdGlvbmFsLXF1YWRyYXRpYyBzcGxpbmUsIGdyZWF0bHkgaW5jcmVhc2luZyBleHByZXNzaXZpdHkgd2l0aG91dCBzYWNyaWZpY2luZyBpbnZlcnRpYmlsaXR5IG9yIE8oMSkgbG9nLWRldC4gVGhlIHNwbGluZSBpcyBwYXJhbWV0ZXJpemVkIGJ5IEsga25vdCBwb3NpdGlvbnMgYW5kIGRlcml2YXRpdmVzOyB0aGUgaW52ZXJzZSBpcyBjb21wdXRlZCBhbmFseXRpY2FsbHkuIE5TRiBhY2hpZXZlcyBzaWduaWZpY2FudGx5IGJldHRlciBiaXRzL2RpbSB0aGFuIGFmZmluZS1iYXNlZCBmbG93cyBvbiBpbWFnZSBiZW5jaG1hcmtzIGFuZCBpcyBub3cgd2lkZWx5IHVzZWQgaW4gcGh5c2ljcy1pbnNwaXJlZCBnZW5lcmF0aXZlIG1vZGVscy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFmZmluZSBjb3VwbGluZzogeSA9IHggKiBleHAocykgKyB0IOKAlCBsaW5lYXIsIGxpbWl0ZWQgZXhwcmVzc2l2aXR5IGluIGVhY2ggbGF5ZXIuIiwiU3BsaW5lIGNvdXBsaW5nOiB5ID0gc3BsaW5lKHg7IFcsIEgsIEQpIOKAlCBub25saW5lYXIgbW9ub3RvbmUsIG11Y2ggbW9yZSBleHByZXNzaXZlLiIsIkludmVyc2U6IGFuYWx5dGljIChzb2x2ZSBxdWFkcmF0aWMgZm9yIHJhdGlvbmFsLXF1YWRyYXRpYyBzcGxpbmUpIOKAlCBubyBzZXF1ZW50aWFsIHN0ZXBzLiIsIkxvZy1kZXQ6IGRlcml2YXRpdmUgb2Ygc3BsaW5lIOKAlCBzdGlsbCBPKDEpIGFuZCBudW1lcmljYWxseSBzdGFibGUuIiwiVHJhZGUtb2ZmOiBtb3JlIGNvbXB1dGUgcGVyIGxheWVyIGJ1dCBmZXdlciBsYXllcnMgbmVlZGVkIGZvciBlcXVpdmFsZW50IHF1YWxpdHkuIl19XQ=="
---
# MAF and IAF — Autoregressive Normalizing Flows

Autoregressive models factorize p(x) = Π p(x_i | x_{<i}). MAF (Papamakarios et al., 2017) reframes this as a normalizing flow where each conditional is a Gaussian: p(x_i | x_{<i}) = N(μ_i(x_{<i}), σ_i(x_{<i})). The resulting transformation y_i = (x_i - μ_i) / σ_i is an invertible affine map. Because MADE computes all μ_i, σ_i in a single forward pass, density evaluation is O(1). Sampling requires inverting the autoregressive structure sequentially, making it O(d). IAF (Kingma et al., 2016) reverses the parameterization to get fast sampling at the cost of slow density.

## Autoregressive Models as Normalizing Flows

A normalizing flow requires a bijective mapping f: x → z with tractable Jacobian determinant. An autoregressive model where y_i = (x_i - μ_i(x_{<i})) / σ_i(x_{<i}) is exactly this: the Jacobian is lower-triangular (output y_i depends on x_{≤i} but the transformation of x_i depends only on x_{<i}), so its determinant is the product of diagonal elements: det J = Π_i (1/σ_i). The log-determinant is -Σ_i log σ_i. This structure — lower-triangular Jacobian, unit-diagonal or diagonal — is the key that links autoregressive models to normalizing flows and justifies using MADE as the backbone.

## MADE — Masked Autoencoder for Distribution Estimation

MADE (Germain et al., 2015) implements a masked MLP that computes all conditionals p(x_i | x_{<i}) in a single forward pass. Each hidden unit is assigned a degree m ∈ {0, ..., d-1}; connections are masked so that unit j in layer l can only receive input from units in layer l-1 with degree ≤ m_j. The output for x_i uses only hidden units with degree < i, enforcing the autoregressive property. The mask matrices are fixed at initialization; the weights are learned normally.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MADE(nn.Module):
    """Masked Autoencoder for Distribution Estimation (Germain et al. 2015).
    Enforces output_i depends only on inputs 0..i-1 via static masks."""
    def __init__(self, d, hidden=128, n_out=2):
        super().__init__()
        self.d, self.n_out = d, n_out
        m_in  = torch.arange(d)
        m_h   = torch.randint(0, d - 1, (hidden,))
        m_out = torch.arange(d).repeat(n_out)
        # mask[i,j]=1 iff hidden unit i can see input j
        self.mask1 = (m_h.unsqueeze(1) >= m_in.unsqueeze(0)).float()   # (h, d)
        # mask[i,j]=1 iff output i can see hidden unit j (strict inequality)
        self.mask2 = (m_out.unsqueeze(1) > m_h.unsqueeze(0)).float()   # (d*n, h)
        self.fc1 = nn.Linear(d, hidden)
        self.fc2 = nn.Linear(hidden, d * n_out)
        self.register_buffer('_m1', self.mask1)
        self.register_buffer('_m2', self.mask2)

    def forward(self, x):
        h = F.relu(F.linear(x, self.fc1.weight * self._m1, self.fc1.bias))
        o = F.linear(h, self.fc2.weight * self._m2, self.fc2.bias)
        return o.view(x.shape[0], self.d, self.n_out)

d, B = 8, 16
made = MADE(d, hidden=64)
x = torch.randn(B, d)
out = made(x)
print(f"Output shape: {out.shape}  (batch={B}, d={d}, 2 params per dim)")
print("MADE: all conditionals computed in ONE forward pass -> O(1) density eval")
```

## MAF — Forward Pass (Density Evaluation)

In MAF the transformation is y_i = (x_i - μ_i(x_{<i})) × exp(-α_i(x_{<i})). MADE computes all (μ_i, α_i) in one pass from x, so the forward transformation (x → y, used for density evaluation) is O(1). The log-determinant is diagonal: log|det J| = -Σ_i α_i(x_{<i}), which comes out of the same MADE pass. Training a stack of MAF layers by maximum likelihood is therefore efficient.

```python
import torch
import torch.nn as nn

class MAFLayer(nn.Module):
    """Single MAF layer. Forward (density) is O(1); inverse (sample) is O(d)."""
    def __init__(self, d, hidden=128):
        super().__init__()
        self.made = MADE(d, hidden=hidden, n_out=2)

    def forward(self, x):
        """Density eval: one MADE pass computes all (mu_i, log_sigma_i)."""
        params  = self.made(x)              # (B, d, 2)
        mu      = params[..., 0]
        log_sig = params[..., 1]
        y       = (x - mu) * (-log_sig).exp()
        log_det = -log_sig.sum(dim=-1)     # (B,)
        return y, log_det

    def log_prob(self, x):
        y, log_det = self.forward(x)
        log_pz = -0.5 * (y ** 2 + torch.log(torch.tensor(2 * torch.pi))).sum(-1)
        return log_pz + log_det

d, B = 8, 32
layer = MAFLayer(d)
x = torch.randn(B, d)
y, ld = layer.forward(x)
lp   = layer.log_prob(x)
print(f"x: {x.shape} -> y: {y.shape}")
print(f"log_det range: [{ld.min():.2f}, {ld.max():.2f}]")
print(f"log_prob range: [{lp.min():.2f}, {lp.max():.2f}]")
print("Forward (density): 1 MADE pass for entire batch -> O(1)")
```

## MAF — Inverse Pass (Sampling)

To sample from MAF: draw y ~ N(0,I), then invert y_i = (x_i - μ_i) / σ_i to get x_i = y_i × σ_i(x_{<i}) + μ_i(x_{<i}). Computing x_i requires x_{<i}, so the inversion is inherently sequential: compute x_1, then x_2 (using x_1), …, x_d (using x_{1:d-1}). Each step calls MADE once, yielding O(d) evaluations total. This makes MAF impractical as a decoder or posterior in a VAE where sampling speed matters.

```python
import torch
import time

def maf_inverse(layer, y, d):
    """Invert MAF: x_i = y_i * exp(log_s_i(x_{<i})) + mu_i(x_{<i}).
    Requires d sequential MADE evaluations."""
    x = torch.zeros_like(y)
    for i in range(d):
        params  = layer.made(x)       # full MADE pass, but only output i used
        mu_i    = params[:, i, 0]
        log_si  = params[:, i, 1]
        x[:, i] = y[:, i] * log_si.exp() + mu_i
    return x

d, B = 8, 16
layer  = MAFLayer(d)
x_orig = torch.randn(B, d)
y, _   = layer.forward(x_orig)

t0 = time.perf_counter()
x_rec = maf_inverse(layer, y, d)
ms_sample = (time.perf_counter() - t0) * 1000

t0 = time.perf_counter()
_, _ = layer.forward(x_orig)
ms_density = (time.perf_counter() - t0) * 1000

print(f"Reconstruction error: {(x_orig - x_rec).abs().max():.2e}")
print(f"Density eval:  {ms_density:.3f} ms  [1 MADE pass]")
print(f"Sampling:      {ms_sample:.3f} ms  [{d} MADE passes]")
print(f"Slowdown: ~{ms_sample/max(ms_density,0.001):.1f}x  (scales as O(d))")
```

## IAF — Inverse Autoregressive Flow

IAF (Kingma et al., 2016) reverses the MAF parameterization: the transformation is z_i = μ_i(z_{<i}) + σ_i(z_{<i}) × ε_i where ε ~ N(0,I). Now the forward pass (sampling) is x → z, which is O(1) since all (μ_i, σ_i) are functions of z_{<i} that can be computed via MADE in one pass from z. But density evaluation requires inverting: z_i = (x_i - μ_i(z_{<i})) / σ_i(z_{<i}), which is sequential in z_{<i} — O(d) passes. IAF is therefore ideal as a flexible posterior approximation in VAEs (fast sampling during training), but not for standalone density estimation.

> **MAF vs IAF Use Cases**: Use MAF when you need fast density evaluation and can tolerate slow sampling: training a generative flow on log-likelihood, or as a prior. Use IAF when you need fast sampling and can tolerate slow density: as a flexible variational posterior q(z|x) in a VAE, where you sample z at every training step but rarely evaluate its exact density. Parallel WaveNet uses IAF as a fast student distilled from an autoregressive WaveNet teacher.

## Density vs Sampling Speed Benchmark

```python
import torch
import time
import numpy as np

def flow_benchmark(d=16, B=256, n_layers=4, n_trials=30):
    """Wall-clock comparison: density eval vs sampling in MAF."""
    dummy = torch.zeros(B, d, 2)
    timings = {}

    t0 = time.perf_counter()
    for _ in range(n_trials):
        x = torch.randn(B, d)
        for _ in range(n_layers):
            mu, log_s = dummy[..., 0], dummy[..., 1]
            x = (x - mu) * (-log_s).exp()
    timings['density'] = (time.perf_counter() - t0) / n_trials * 1000

    t0 = time.perf_counter()
    for _ in range(n_trials):
        z = torch.randn(B, d)
        for _ in range(n_layers):
            x_out = torch.zeros_like(z)
            for i in range(d):
                x_out[:, i] = z[:, i]   # placeholder sequential step
            z = x_out
    timings['sample'] = (time.perf_counter() - t0) / n_trials * 1000

    print(f"Benchmark: d={d}, B={B}, layers={n_layers}")
    print(f"  Density eval: {timings['density']:6.2f} ms  (O(1)/layer, parallel over d)")
    print(f"  Sampling:     {timings['sample']:6.2f} ms  (O(d)/layer, serial)")
    print(f"  Ratio:        {timings['sample']/max(timings['density'],0.001):.1f}x")
    print("  IAF reverses: sampling O(1), density O(d)")
    print("  Use MAF for NF training; IAF for VAE posterior")

flow_benchmark(d=16)
```

## Flow Model Comparison

| Model | Forward (density) | Inverse (sample) | Expressivity | Parallel train | Parallel sample |
| --- | --- | --- | --- | --- | --- |
| NICE | O(1) | O(1) | Low (additive only) | Yes | Yes |
| RealNVP | O(1) | O(1) | Medium (affine coupling) | Yes | Yes |
| MAF | O(1) via MADE | O(d) sequential | High (autoregressive) | Yes | No |
| IAF | O(d) sequential | O(1) via MADE | High (autoregressive) | No (density needed) | Yes |
| Glow | O(1) | O(1) | High (learnable perm) | Yes | Yes |

## Neural Spline Flows

Neural Spline Flows (Durkan et al., 2019) replace the affine coupling (scale + shift) with a monotone rational-quadratic spline, greatly increasing expressivity without sacrificing invertibility or O(1) log-det. The spline is parameterized by K knot positions and derivatives; the inverse is computed analytically. NSF achieves significantly better bits/dim than affine-based flows on image benchmarks and is now widely used in physics-inspired generative models.

- Affine coupling: y = x * exp(s) + t — linear, limited expressivity in each layer.
- Spline coupling: y = spline(x; W, H, D) — nonlinear monotone, much more expressive.
- Inverse: analytic (solve quadratic for rational-quadratic spline) — no sequential steps.
- Log-det: derivative of spline — still O(1) and numerically stable.
- Trade-off: more compute per layer but fewer layers needed for equivalent quality.

