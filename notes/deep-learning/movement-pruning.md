---
title: "Movement Pruning — Learning Which Weights to Prune"
slug: "movement-pruning"
description: "Movement pruning (Sanh et al. 2020) trains importance scores via gradient descent, pruning weights that move toward zero during fine-tuning. Covers score initialization, straight-through estimator, soft movement pruning, and comparison with magnitude and gradient-based criteria for BERT."
tags: ["deep-learning", "model-compression", "pruning", "quantization"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWFnbml0dWRlIHBydW5pbmcgcmVtb3ZlcyB0aGUgc21hbGxlc3Qgd2VpZ2h0cyBieSBhYnNvbHV0ZSB2YWx1ZS4gVGhpcyB3b3JrcyB3ZWxsIGZvciBtb2RlbHMgdHJhaW5lZCBmcm9tIHNjcmF0Y2ggYnV0IGlzIHBvb3JseSBzdWl0ZWQgdG8gZmluZS10dW5lZCBtb2RlbHM6IGR1cmluZyB0YXNrLXNwZWNpZmljIGZpbmUtdHVuaW5nLCB0aGUgd2VpZ2h0cyB0aGF0IG1hdHRlciBtb3N0IGZvciB0aGUgdGFzayBtYXkgYmUgc21hbGwgaW4gbWFnbml0dWRlIGJ1dCBtb3Zpbmcgc3Ryb25nbHkgYXdheSBmcm9tIHplcm8sIHdoaWxlIGxhcmdlIHByZS10cmFpbmVkIHdlaWdodHMgdGhhdCBhcmUgaXJyZWxldmFudCB0byB0aGUgdGFzayByZW1haW4gbGFyZ2UgYnV0IGJlY29tZSB1bmltcG9ydGFudC4gTW92ZW1lbnQgcHJ1bmluZyBhZGRyZXNzZXMgdGhpcyBieSBwcnVuaW5nIHdlaWdodHMgdGhhdCBtb3ZlIHRvd2FyZCB6ZXJvIGR1cmluZyBmaW5lLXR1bmluZywgbGVhcm5pbmcgd2hpY2ggd2VpZ2h0cyB0byBrZWVwIGpvaW50bHkgd2l0aCB0aGUgdGFzayBvYmplY3RpdmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIE1vdmVtZW50IFBydW5pbmcgT2JqZWN0aXZlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb3ZlbWVudCBwcnVuaW5nIChTYW5oIGV0IGFsLiAyMDIwKSBpbnRyb2R1Y2VzIGEgcmVhbC12YWx1ZWQgc2NvcmUgU19pIGZvciBlYWNoIHdlaWdodCBXX2ksIGluaXRpYWxpemVkIHRvIHplcm8uIER1cmluZyB0cmFpbmluZywgYSBiaW5hcnkgbWFzayBpcyBkZXJpdmVkIGJ5IGtlZXBpbmcgdGhlIHRvcC1rIHdlaWdodHMgYnkgc2NvcmU6IE0gPSB0b3Atayh8U3wpLiBUaGUgZm9yd2FyZCBwYXNzIHVzZXMgVyDiipkgTSAobWFza2VkIHdlaWdodHMpLiBUaGUgZ3JhZGllbnQgb2YgdGhlIHRhc2sgbG9zcyDiiIJML+KIglMgZmxvd3MgdGhyb3VnaCB0aGUgc3RyYWlnaHQtdGhyb3VnaCBlc3RpbWF0b3IsIGFsbG93aW5nIHRoZSBzY29yZXMgdG8gYmUgdHJhaW5lZCBldmVuIHRob3VnaCB0aGUgbWFza2luZyBvcGVyYXRpb24gaXMgZGlzY3JldGUuIEEgcG9zaXRpdmUgc2NvcmUgZ3JhZGllbnQgbWVhbnMgdGhlIHdlaWdodCBpcyBiZWNvbWluZyBtb3JlIGltcG9ydGFudDsgYSBuZWdhdGl2ZSBncmFkaWVudCBkcml2ZXMgdGhlIHNjb3JlIHRvd2FyZCB6ZXJvLCBldmVudHVhbGx5IHBydW5pbmcgdGhlIHdlaWdodC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY29yZSBDb21wdXRhdGlvbiBhbmQgTWFzayBHZW5lcmF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE1vdmVtZW50UHJ1bmluZ0xpbmVhcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkxpbmVhciBsYXllciB3aXRoIGxlYXJuYWJsZSBtb3ZlbWVudCBwcnVuaW5nIHNjb3Jlcy5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9mZWF0dXJlczogaW50LCBvdXRfZmVhdHVyZXM6IGludCwgc3BhcnNpdHk6IGZsb2F0ID0gMC44KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYud2VpZ2h0ID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKG91dF9mZWF0dXJlcywgaW5fZmVhdHVyZXMpICogMC4wMilcbiAgICAgICAgc2VsZi5iaWFzID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKG91dF9mZWF0dXJlcykpXG4gICAgICAgIHNlbGYuc2NvcmVzID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zX2xpa2Uoc2VsZi53ZWlnaHQpKSAgIyBTX2kgPSAwIGluaXRpYWxseVxuICAgICAgICBzZWxmLnNwYXJzaXR5ID0gc3BhcnNpdHlcblxuICAgIGRlZiBfZ2V0X21hc2soc2VsZikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIG5fa2VlcCA9IG1heCgxLCBpbnQoc2VsZi53ZWlnaHQubnVtZWwoKSAqICgxIC0gc2VsZi5zcGFyc2l0eSkpKVxuICAgICAgICAjIFRvcC1rIGJ5IGFic29sdXRlIHNjb3JlIHZhbHVlXG4gICAgICAgIHRocmVzaG9sZCA9IHNlbGYuc2NvcmVzLmFicygpLmZsYXR0ZW4oKS50b3BrKG5fa2VlcCkudmFsdWVzLm1pbigpXG4gICAgICAgIHJldHVybiAoc2VsZi5zY29yZXMuYWJzKCkgXHUwMDNlPSB0aHJlc2hvbGQpLmZsb2F0KClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIG1hc2sgPSBzZWxmLl9nZXRfbWFzaygpICAjIGJpbmFyeSwgbm9uLWRpZmZlcmVudGlhYmxlXG4gICAgICAgIG1hc2tlZF93ZWlnaHQgPSBzZWxmLndlaWdodCAqIG1hc2sgICMgc2NvcmVzIGdyYWRpZW50IHZpYSBTVEUgKHNlZSBuZXh0IGJsb2NrKVxuICAgICAgICByZXR1cm4gbm4uZnVuY3Rpb25hbC5saW5lYXIoeCwgbWFza2VkX3dlaWdodCwgc2VsZi5iaWFzKVxuXG4jIFZlcmlmeSBzY29yZSBzaGFwZXNcbmxheWVyID0gTW92ZW1lbnRQcnVuaW5nTGluZWFyKDEyOCwgNjQsIHNwYXJzaXR5PTAuOClcbnggPSB0b3JjaC5yYW5kbig4LCAxMjgpXG5vdXQgPSBsYXllcih4KVxucHJpbnQoZlx1MDAyN091dHB1dCBzaGFwZToge291dC5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3U2NvcmUgc2hhcGU6IHtsYXllci5zY29yZXMuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0FjdGl2ZSB3ZWlnaHRzOiB7bGF5ZXIuX2dldF9tYXNrKCkuc3VtKCkuaXRlbSgpOi4wZn0ve2xheWVyLndlaWdodC5udW1lbCgpfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdHJhaWdodC1UaHJvdWdoIEVzdGltYXRvciBmb3IgRGlzY3JldGUgTWFza3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0b3AtayBtYXNraW5nIG9wZXJhdGlvbiBoYXMgemVybyBncmFkaWVudCBhbG1vc3QgZXZlcnl3aGVyZS4gVGhlIHN0cmFpZ2h0LXRocm91Z2ggZXN0aW1hdG9yIChTVEUpIGJ5cGFzc2VzIHRoaXMgYnkgcGFzc2luZyB0aGUgdXBzdHJlYW0gZ3JhZGllbnQgdGhyb3VnaCB0aGUgbWFza2luZyBvcGVyYXRpb24gdW5jaGFuZ2VkIGR1cmluZyB0aGUgYmFja3dhcmQgcGFzczog4oiCTC/iiIJTIOKJiCDiiIJML+KIgihX4oqZTSkuIEluIHByYWN0aWNlIHRoaXMgaXMgaW1wbGVtZW50ZWQgYnkgY29tcHV0aW5nIHRoZSBtYXNrIGluIHRoZSBmb3J3YXJkIHBhc3Mgd2l0aG91dCB0cmFja2luZyBpdCBpbiB0aGUgYXV0b2dyYWQgZ3JhcGgsIHRoZW4gbXVsdGlwbHlpbmcgdGhlIHdlaWdodCBieSB0aGUgZGV0YWNoZWQgbWFzay4gVGhlIHNjb3JlIGdyYWRpZW50IHRoZW4gZXF1YWxzIHRoZSBncmFkaWVudCB0aHJvdWdoIHRoZSB3ZWlnaHQgdGltZXMgdGhlIG1hc2sgaW5kaWNhdG9yLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaC5hdXRvZ3JhZCBpbXBvcnQgRnVuY3Rpb25cblxuY2xhc3MgVG9wS1NURShGdW5jdGlvbik6XG4gICAgXCJcIlwiU3RyYWlnaHQtdGhyb3VnaCBlc3RpbWF0b3IgZm9yIHRvcC1rIG1hc2tpbmcuXCJcIlwiXG5cbiAgICBAc3RhdGljbWV0aG9kXG4gICAgZGVmIGZvcndhcmQoY3R4LCBzY29yZXM6IHRvcmNoLlRlbnNvciwgc3BhcnNpdHk6IGZsb2F0KTpcbiAgICAgICAgbl9rZWVwID0gbWF4KDEsIGludChzY29yZXMubnVtZWwoKSAqICgxIC0gc3BhcnNpdHkpKSlcbiAgICAgICAgdGhyZXNob2xkID0gc2NvcmVzLmFicygpLmZsYXR0ZW4oKS50b3BrKG5fa2VlcCkudmFsdWVzLm1pbigpXG4gICAgICAgIG1hc2sgPSAoc2NvcmVzLmFicygpIFx1MDAzZT0gdGhyZXNob2xkKS5mbG9hdCgpXG4gICAgICAgIGN0eC5zYXZlX2Zvcl9iYWNrd2FyZChtYXNrKVxuICAgICAgICByZXR1cm4gbWFza1xuXG4gICAgQHN0YXRpY21ldGhvZFxuICAgIGRlZiBiYWNrd2FyZChjdHgsIGdyYWRfb3V0cHV0KTpcbiAgICAgICAgIyBTVEU6IHBhc3MgZ3JhZGllbnQgc3RyYWlnaHQgdGhyb3VnaCB0aGUgbWFza2luZyBvcGVyYXRpb25cbiAgICAgICAgbWFzaywgPSBjdHguc2F2ZWRfdGVuc29yc1xuICAgICAgICByZXR1cm4gZ3JhZF9vdXRwdXQgKiBtYXNrLCBOb25lICAjIE5vbmUgZm9yIHNwYXJzaXR5IChub3QgYSB0ZW5zb3IpXG5cbmNsYXNzIE1vdmVtZW50UHJ1bmluZ0xpbmVhclNURShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9mZWF0dXJlcywgb3V0X2ZlYXR1cmVzLCBzcGFyc2l0eT0wLjgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi53ZWlnaHQgPSBubi5QYXJhbWV0ZXIodG9yY2gucmFuZG4ob3V0X2ZlYXR1cmVzLCBpbl9mZWF0dXJlcykgKiAwLjAyKVxuICAgICAgICBzZWxmLmJpYXMgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2ZlYXR1cmVzKSlcbiAgICAgICAgc2VsZi5zY29yZXMgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2ZlYXR1cmVzLCBpbl9mZWF0dXJlcykpXG4gICAgICAgIHNlbGYuc3BhcnNpdHkgPSBzcGFyc2l0eVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG1hc2sgPSBUb3BLU1RFLmFwcGx5KHNlbGYuc2NvcmVzLCBzZWxmLnNwYXJzaXR5KVxuICAgICAgICByZXR1cm4gbm4uZnVuY3Rpb25hbC5saW5lYXIoeCAqIDEuMCwgc2VsZi53ZWlnaHQgKiBtYXNrLCBzZWxmLmJpYXMpXG5cbiMgVGVzdCBncmFkaWVudCBmbG93cyB0byBzY29yZXNcbmxheWVyID0gTW92ZW1lbnRQcnVuaW5nTGluZWFyU1RFKDMyLCAxNiwgc3BhcnNpdHk9MC43KVxueCA9IHRvcmNoLnJhbmRuKDQsIDMyKVxubG9zcyA9IGxheWVyKHgpLnN1bSgpXG5sb3NzLmJhY2t3YXJkKClcbnByaW50KGZcdTAwMjdzY29yZXMuZ3JhZCBpcyBOb25lOiB7bGF5ZXIuc2NvcmVzLmdyYWQgaXMgTm9uZX1cdTAwMjcpXG5wcmludChmXHUwMDI3c2NvcmVzLmdyYWQgbm9ybToge2xheWVyLnNjb3Jlcy5ncmFkLm5vcm0oKS5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb3ZlbWVudCB2cyBNYWduaXR1ZGUg4oCUIEJFUlQtUUEgQWNjdXJhY3kifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYlxubWF0cGxvdGxpYi51c2UoXHUwMDI3QWdnXHUwMDI3KVxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG4jIFJlcHJvZHVjZWQgZnJvbSBTYW5oIGV0IGFsLiAyMDIwIChTUXVBRCB2MS4xIEYxIGF0IHZhcnlpbmcgc3BhcnNpdHkpXG5zcGFyc2l0eV9sZXZlbHMgPSBbMC4wLCAwLjUsIDAuNywgMC44LCAwLjg1LCAwLjkwLCAwLjk1XVxuXG4jIEFwcHJveGltYXRlIEYxIHNjb3JlcyBmcm9tIHBhcGVyIChCRVJULWJhc2UgZmluZS10dW5lZCBvbiBTUXVBRClcbm1hZ25pdHVkZV9mMSA9IFs4OC41LCA4Ny45LCA4Ni4xLCA4Mi40LCA3OC4zLCA2OC4yLCA0NS4xXVxubW92ZW1lbnRfZjEgID0gWzg4LjUsIDg4LjIsIDg3LjYsIDg2LjgsIDg1LjEsIDgyLjQsIDc0LjNdXG5cbnByaW50KGZcdTAwMjd7XCJTcGFyc2l0eVwiOlx1MDAzZTEwfSAge1wiTWFnbml0dWRlIEYxXCI6XHUwMDNlMTR9ICB7XCJNb3ZlbWVudCBGMVwiOlx1MDAzZTEyfSAge1wiRGVsdGFcIjpcdTAwM2U4fVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA1MilcbmZvciBzLCBtLCBtdiBpbiB6aXAoc3BhcnNpdHlfbGV2ZWxzLCBtYWduaXR1ZGVfZjEsIG1vdmVtZW50X2YxKTpcbiAgICBwcmludChmXHUwMDI3e3M6XHUwMDNlMTAuMCV9ICB7bTpcdTAwM2UxNC4xZn0gIHttdjpcdTAwM2UxMi4xZn0gIHttdi1tOlx1MDAzZSs4LjFmfVx1MDAyNylcblxuIyBGaW5kIGNyb3Nzb3ZlcjogYXQgd2hhdCBzcGFyc2l0eSBkb2VzIG1vdmVtZW50IHBydW5pbmcgZ2FpbiBcdTAwM2UyIEYxIHBvaW50cz9cbmNyb3Nzb3ZlciA9IFsocywgbXYtbSkgZm9yIHMsIG0sIG12IGluIHppcChzcGFyc2l0eV9sZXZlbHMsIG1hZ25pdHVkZV9mMSwgbW92ZW1lbnRfZjEpXG4gICAgICAgICAgICAgaWYgbXYgLSBtIFx1MDAzZSAyXVxuaWYgY3Jvc3NvdmVyOlxuICAgIHByaW50KGZcdTAwMjdcXG5Nb3ZlbWVudCBwcnVuaW5nIGdhaW5zIFx1MDAzZTIgRjEgYXQgc3BhcnNpdHkgXHUwMDNlPSB7Y3Jvc3NvdmVyWzBdWzBdOi4wJX1cdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN01heCBnYWluOiAre21heChkIGZvciBfLGQgaW4gY3Jvc3NvdmVyKTouMWZ9IEYxIGF0IGhpZ2hlc3Qgc3BhcnNpdHlcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU29mdCBNb3ZlbWVudCBQcnVuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIYXJkIG1vdmVtZW50IHBydW5pbmcgdXNlcyBhIGRpc2NyZXRlIHRvcC1rIG1hc2suIFNvZnQgbW92ZW1lbnQgcHJ1bmluZyByZWxheGVzIHRoaXM6IGluc3RlYWQgb2YgZW5mb3JjaW5nIGV4YWN0IHNwYXJzaXR5IHZpYSB0b3AtaywgaXQgYWRkcyBhbiBMMSByZWd1bGFyaXphdGlvbiB0ZXJtIG9uIHRoZSBzY29yZXM6IExfdG90YWwgPSBMX3Rhc2sgKyDOuyDCtyDigJZT4oCW4oKBLiBUaGlzIGRyaXZlcyBtb3N0IHNjb3JlcyB0b3dhcmQgemVybyB3aGlsZSBhbGxvd2luZyB0aGUgbW9kZWwgdG8gY2hvb3NlIHdoaWNoIG9uZXMgcmVtYWluIG5vbnplcm8uIFRoZXJlIGlzIG5vIGhhcmQgc3BhcnNpdHkgY29uc3RyYWludDsgdGhlIHJlZ3VsYXJpemF0aW9uIHN0cmVuZ3RoIM67IGNvbnRyb2xzIHRoZSB0cmFkZS1vZmYuIEF0IGNvbnZlcmdlbmNlLCByZW1haW5pbmcgbm9uemVybyBzY29yZXMgZGVmaW5lIHRoZSBzdXJ2aXZpbmcgd2VpZ2h0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuXG5jbGFzcyBTb2Z0TW92ZW1lbnRQcnVuaW5nTGluZWFyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2ZlYXR1cmVzLCBvdXRfZmVhdHVyZXMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi53ZWlnaHQgPSBubi5QYXJhbWV0ZXIodG9yY2gucmFuZG4ob3V0X2ZlYXR1cmVzLCBpbl9mZWF0dXJlcykgKiAwLjAyKVxuICAgICAgICBzZWxmLmJpYXMgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2ZlYXR1cmVzKSlcbiAgICAgICAgc2VsZi5zY29yZXMgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2ZlYXR1cmVzLCBpbl9mZWF0dXJlcykpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgIyBVc2Ugc2lnbW9pZCB0byBnZXQgc29mdCBbMCwxXSBtYXNrIChubyBkaXNjcmV0ZSB0b3AtaylcbiAgICAgICAgc29mdF9tYXNrID0gdG9yY2guc2lnbW9pZChzZWxmLnNjb3JlcyAqIDEwKSAgIyBzaGFycCBzaWdtb2lkXG4gICAgICAgIHJldHVybiBubi5mdW5jdGlvbmFsLmxpbmVhcih4LCBzZWxmLndlaWdodCAqIHNvZnRfbWFzaywgc2VsZi5iaWFzKVxuXG4gICAgZGVmIGwxX3Njb3JlX2xvc3Moc2VsZik6XG4gICAgICAgIHJldHVybiBzZWxmLnNjb3Jlcy5hYnMoKS5tZWFuKClcblxuZGVmIHRyYWluX3dpdGhfc29mdF9tb3ZlbWVudChtb2RlbCwgbG9hZGVyLCBjcml0ZXJpb24sIGVwb2Nocz0zLCBsYW09MWUtNCk6XG4gICAgb3B0aW1pemVyID0gb3B0aW0uQWRhbVcobW9kZWwucGFyYW1ldGVycygpLCBscj0yZS00KVxuICAgIGZvciBlcG9jaCBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICB0b3RhbF90YXNrLCB0b3RhbF9yZWcgPSAwLjAsIDAuMFxuICAgICAgICBmb3IgWCwgeSBpbiBsb2FkZXI6XG4gICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgICAgIHRhc2tfbG9zcyA9IGNyaXRlcmlvbihtb2RlbChYKSwgeSlcbiAgICAgICAgICAgICMgTDEgcmVndWxhcml6YXRpb24gb24gYWxsIHNjb3JlIHRlbnNvcnNcbiAgICAgICAgICAgIHJlZ19sb3NzID0gc3VtKG0ubDFfc2NvcmVfbG9zcygpIGZvciBtIGluIG1vZGVsLm1vZHVsZXMoKVxuICAgICAgICAgICAgICAgICAgICAgICAgICBpZiBpc2luc3RhbmNlKG0sIFNvZnRNb3ZlbWVudFBydW5pbmdMaW5lYXIpKVxuICAgICAgICAgICAgbG9zcyA9IHRhc2tfbG9zcyArIGxhbSAqIHJlZ19sb3NzXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgICAgIHRvdGFsX3Rhc2sgKz0gdGFza19sb3NzLml0ZW0oKVxuICAgICAgICAgICAgdG90YWxfcmVnICs9IHJlZ19sb3NzLml0ZW0oKVxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NoKzF9OiB0YXNrPXt0b3RhbF90YXNrL2xlbihsb2FkZXIpOi40Zn0gIHJlZz17dG90YWxfcmVnL2xlbihsb2FkZXIpOi40Zn1cdTAwMjcpXG5cbnByaW50KFx1MDAyN1NvZnQgbW92ZW1lbnQgcHJ1bmluZzogc2NvcmVzIGRyaXZlbiB0byB6ZXJvIHZpYSBMMSwgbm8gZGlzY3JldGUgbWFzayBuZWVkZWQuXHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2hlbiB0byBDaG9vc2UgTW92ZW1lbnQgUHJ1bmluZyIsImNvbnRlbnQiOiJNb3ZlbWVudCBwcnVuaW5nIGlzIHNwZWNpZmljYWxseSBkZXNpZ25lZCBmb3IgZmluZS10dW5pbmcgcHJldHJhaW5lZCBtb2RlbHMgbGlrZSBCRVJULiBJZiB5b3UgYXJlIHRyYWluaW5nIGZyb20gc2NyYXRjaCwgbWFnbml0dWRlIHBydW5pbmcgb3IgVGF5bG9yIHBydW5pbmcgaXMgZXF1YWxseSBlZmZlY3RpdmUuIE1vdmVtZW50IHBydW5pbmdcdTAwMjdzIGFkdmFudGFnZSBlbWVyZ2VzIGJlY2F1c2UgcHJlLXRyYWluZWQgd2VpZ2h0cyB0aGF0IHdlcmUgbGFyZ2UgaW4gdGhlIG9yaWdpbmFsIG1vZGVsIG1heSBiZWNvbWUgaXJyZWxldmFudCBhZnRlciB0YXNrLXNwZWNpZmljIGZpbmUtdHVuaW5nIOKAlCBtYWduaXR1ZGUgcHJ1bmluZyB3b3VsZCBrZWVwIHRoZW0sIHdoaWxlIG1vdmVtZW50IHBydW5pbmcgY29ycmVjdGx5IGlkZW50aWZpZXMgYW5kIHJlbW92ZXMgdGhlbS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaW5uaW5nIFRpY2tldHMgYXQgVGFzay1TcGVjaWZpYyBMZXZlbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGxvdHRlcnkgdGlja2V0IGh5cG90aGVzaXMgc3RhdGVzIHRoYXQgbGFyZ2UgbmV0d29ya3MgY29udGFpbiBzcGFyc2Ugc3VibmV0d29ya3MgKHdpbm5pbmcgdGlja2V0cykgdGhhdCwgd2hlbiB0cmFpbmVkIGZyb20gaW5pdGlhbGl6YXRpb24sIG1hdGNoIHRoZSBmdWxsIG5ldHdvcmtcdTAwMjdzIGFjY3VyYWN5LiBNb3ZlbWVudCBwcnVuaW5nIGZpbmRzIHdpbm5pbmcgdGlja2V0cyBhdCB0aGUgZmluZS10dW5pbmcgbGV2ZWw6IHRoZSBzcGFyc2UgbWFzayBmb3VuZCBieSBtb3ZlbWVudCBwcnVuaW5nIG9uIGEgZmluZS10dW5lZCBCRVJUIGlzIHRhc2stc3BlY2lmaWMgYW5kIGRvZXMgbm90IGdlbmVyYWxpemUgYWNyb3NzIHRhc2tzLiBUaGlzIGlzIGV2aWRlbmNlIHRoYXQgdGhlIGxvdHRlcnkgdGlja2V0IHN0cnVjdHVyZSBpcyBkb3duc3RyZWFtIG9mIHRoZSB0YXNrLCBub3QganVzdCBvZiB0aGUgcHJlLXRyYWluaW5nLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU2NvcmVzIFMgaW5pdGlhbGl6ZWQgdG8gMCBhdCB0aGUgc3RhcnQgb2YgZmluZS10dW5pbmcg4oCUIG1vdmVtZW50IGZyb20gemVybyBzaWduYWxzIGltcG9ydGFuY2UuIiwiVG9wLWsgbWFza2luZzogZXhhY3RseSAoMS1rKSUgb2Ygd2VpZ2h0cyBhcmUgcHJ1bmVkOyBrIGlzIHRoZSB0YXJnZXQgZGVuc2l0eS4iLCJTVEUgcHJvcGFnYXRlcyBncmFkaWVudHMgdGhyb3VnaCBkaXNjcmV0ZSBtYXNrOiBzY29yZSBncmFkaWVudCDiiYggd2VpZ2h0IGdyYWRpZW50IMOXIG1hc2suIiwiU29mdCB2YXJpYW50OiBMMSBwZW5hbHR5IG9uIHNjb3JlcyBhdm9pZHMgZGlzY3JldGUgdG9wLWssIHNtb290aGVyIG9wdGltaXphdGlvbiBsYW5kc2NhcGUuIiwiQXQgODDigJM5MCUgc3BhcnNpdHksIG1vdmVtZW50IHBydW5pbmcgcmV0YWlucyA04oCTMTQgRjEgcG9pbnRzIG1vcmUgdGhhbiBtYWduaXR1ZGUgcHJ1bmluZyBvbiBTUXVBRC4iLCJUYXNrLXNwZWNpZmljIHRpY2tldHM6IHRoZSB3aW5uaW5nIHN1Ym5ldHdvcmsgaXMgZGlmZmVyZW50IGZvciBRQSB2cyBOTEkgdnMgc2VudGltZW50IHRhc2tzLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcnVuaW5nIENyaXRlcmlhIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiV2hlbiBTY29yZXMgQ29tcHV0ZWQiLCJDcml0ZXJpYSIsIkJFUlQgU1F1QUQgRjEgQCA5MCUiLCJTdXBwb3J0cyBTdHJ1Y3R1cmUiXSwicm93cyI6W1siTWFnbml0dWRlIHBydW5pbmciLCJQb3N0LXRyYWluaW5nLCBubyBncmFkaWVudCIsInxXX2l8IOKAlCBzdGF0aWMgd2VpZ2h0IHNpemUiLCJ+NjggRjEiLCJZZXMgKGZpbHRlciBMMSkiXSxbIk1vdmVtZW50IHBydW5pbmciLCJEdXJpbmcgZmluZS10dW5pbmcsIGdyYWRpZW50IiwiU2NvcmUgU19pIHRyYWluZWQgYnkg4oiCTC/iiIJTIiwifjgyIEYxIiwiTm8g4oCUIHVuc3RydWN0dXJlZCJdLFsiU29mdCBtb3ZlbWVudCIsIkR1cmluZyBmaW5lLXR1bmluZywgZ3JhZGllbnQiLCJMMShTKSByZWd1bGFyaXphdGlvbiwgc2lnbW9pZCBtYXNrIiwifjgxIEYxIiwiTm8g4oCUIHVuc3RydWN0dXJlZCJdLFsiU05JUCIsIkJlZm9yZSB0cmFpbmluZyAoc2luZ2xlIHBhc3MpIiwifOKIgkwv4oiCV19pIMK3IFdfaXwgYXQgaW5pdCIsIn43MiBGMSIsIlllcyB3aXRoIGV4dGVuc2lvbiJdLFsiR3JhU1AiLCJCZWZvcmUgdHJhaW5pbmcgKEhlc3NpYW4gYXBwcm94KSIsIi1I4bWAZyDCtyBXIGF0IGluaXQgKGdyYWRpZW50IGZsb3cpIiwifjc0IEYxIiwiTGltaXRlZCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIFJlY29tbWVuZGF0aW9ucyBmb3IgQkVSVCBQcnVuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZmluZS10dW5lZCBCRVJUIG1vZGVscywgYXBwbHkgbW92ZW1lbnQgcHJ1bmluZyByYXRoZXIgdGhhbiBtYWduaXR1ZGUgcHJ1bmluZyB3aGVuZXZlciBzcGFyc2l0eSBleGNlZWRzIDYwJS4gVXNlIGEgbGluZWFyIHNwYXJzaXR5IHNjaGVkdWxlOiBzdGFydCBhdCAwJSBhbmQgcmFtcCB0byB0aGUgdGFyZ2V0IG92ZXIgdGhlIGZpcnN0IDgwJSBvZiBmaW5lLXR1bmluZyBzdGVwcywgdGhlbiBob2xkIHRoZSBtYXNrIGZpeGVkIGZvciB0aGUgcmVtYWluaW5nIDIwJS4gVGhpcyB3YXJtLXVwIGF2b2lkcyByZW1vdmluZyB3ZWlnaHRzIGJlZm9yZSB0aGUgbW9kZWwgaGFzIGFkYXB0ZWQgdG8gdGhlIHRhc2suIExlYXJuaW5nIHJhdGUgZm9yIHNjb3JlcyBzaG91bGQgYmUgMTDigJMxMDDDlyBsb3dlciB0aGFuIHRoZSBsZWFybmluZyByYXRlIGZvciB3ZWlnaHRzOyBvdGhlcndpc2Ugc2NvcmVzIGNvbnZlcmdlIHRvbyBmYXN0IGFuZCBmcmVlemUgYmVmb3JlIHRoZSBtb2RlbCBmaW5kcyB0aGUgYmVzdCBzcGFyc2Ugc3VibmV0d29yay4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlN0YXJ0IGZpbmUtdHVuaW5nIHdpdGggbWFnbml0dWRlIHBydW5pbmcgd2FybS11cCAoMOKGkjIwJSBzcGFyc2l0eSkgYmVmb3JlIHN3aXRjaGluZyB0byBtb3ZlbWVudCBzY29yZXMuIiwiU2NvcmUgbGVhcm5pbmcgcmF0ZTogMWUtMiB0byAxZS0xIChtdWNoIGhpZ2hlciB0aGFuIHdlaWdodCBMUiAyZS01KSB3b3JrcyB3ZWxsIGVtcGlyaWNhbGx5LiIsIk1vbml0b3IgZ3JhZGllbnQgbm9ybXMgb2Ygc2NvcmVzIOKAlCBpZiB0aGV5IHZhbmlzaCwgdGhlIHRlbXBlcmF0dXJlIG9yIExSIG5lZWRzIGFkanVzdG1lbnQuIiwiQWZ0ZXIgcmVhY2hpbmcgdGFyZ2V0IHNwYXJzaXR5LCBmcmVlemUgdGhlIG1hc2sgYW5kIGZpbmUtdHVuZSB3ZWlnaHRzIG9ubHkgZm9yIDEwJSBtb3JlIHN0ZXBzLiIsIkZvciBleHRyZW1lIHNwYXJzaXR5IChcdTAwM2U5NSUpLCBjb21iaW5lIG1vdmVtZW50IHBydW5pbmcgd2l0aCBkaXN0aWxsYXRpb24gZnJvbSB0aGUgZGVuc2UgdGVhY2hlci4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Movement Pruning — Learning Which Weights to Prune

Magnitude pruning removes the smallest weights by absolute value. This works well for models trained from scratch but is poorly suited to fine-tuned models: during task-specific fine-tuning, the weights that matter most for the task may be small in magnitude but moving strongly away from zero, while large pre-trained weights that are irrelevant to the task remain large but become unimportant. Movement pruning addresses this by pruning weights that move toward zero during fine-tuning, learning which weights to keep jointly with the task objective.

## The Movement Pruning Objective

Movement pruning (Sanh et al. 2020) introduces a real-valued score S_i for each weight W_i, initialized to zero. During training, a binary mask is derived by keeping the top-k weights by score: M = top-k(|S|). The forward pass uses W ⊙ M (masked weights). The gradient of the task loss ∂L/∂S flows through the straight-through estimator, allowing the scores to be trained even though the masking operation is discrete. A positive score gradient means the weight is becoming more important; a negative gradient drives the score toward zero, eventually pruning the weight.

## Score Computation and Mask Generation

```python
import torch
import torch.nn as nn

class MovementPruningLinear(nn.Module):
    """Linear layer with learnable movement pruning scores."""

    def __init__(self, in_features: int, out_features: int, sparsity: float = 0.8):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.02)
        self.bias = nn.Parameter(torch.zeros(out_features))
        self.scores = nn.Parameter(torch.zeros_like(self.weight))  # S_i = 0 initially
        self.sparsity = sparsity

    def _get_mask(self) -> torch.Tensor:
        n_keep = max(1, int(self.weight.numel() * (1 - self.sparsity)))
        # Top-k by absolute score value
        threshold = self.scores.abs().flatten().topk(n_keep).values.min()
        return (self.scores.abs() >= threshold).float()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        mask = self._get_mask()  # binary, non-differentiable
        masked_weight = self.weight * mask  # scores gradient via STE (see next block)
        return nn.functional.linear(x, masked_weight, self.bias)

# Verify score shapes
layer = MovementPruningLinear(128, 64, sparsity=0.8)
x = torch.randn(8, 128)
out = layer(x)
print(f'Output shape: {out.shape}')
print(f'Score shape: {layer.scores.shape}')
print(f'Active weights: {layer._get_mask().sum().item():.0f}/{layer.weight.numel()}')
```

## Straight-Through Estimator for Discrete Masks

The top-k masking operation has zero gradient almost everywhere. The straight-through estimator (STE) bypasses this by passing the upstream gradient through the masking operation unchanged during the backward pass: ∂L/∂S ≈ ∂L/∂(W⊙M). In practice this is implemented by computing the mask in the forward pass without tracking it in the autograd graph, then multiplying the weight by the detached mask. The score gradient then equals the gradient through the weight times the mask indicator.

```python
import torch
import torch.nn as nn
from torch.autograd import Function

class TopKSTE(Function):
    """Straight-through estimator for top-k masking."""

    @staticmethod
    def forward(ctx, scores: torch.Tensor, sparsity: float):
        n_keep = max(1, int(scores.numel() * (1 - sparsity)))
        threshold = scores.abs().flatten().topk(n_keep).values.min()
        mask = (scores.abs() >= threshold).float()
        ctx.save_for_backward(mask)
        return mask

    @staticmethod
    def backward(ctx, grad_output):
        # STE: pass gradient straight through the masking operation
        mask, = ctx.saved_tensors
        return grad_output * mask, None  # None for sparsity (not a tensor)

class MovementPruningLinearSTE(nn.Module):
    def __init__(self, in_features, out_features, sparsity=0.8):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.02)
        self.bias = nn.Parameter(torch.zeros(out_features))
        self.scores = nn.Parameter(torch.zeros(out_features, in_features))
        self.sparsity = sparsity

    def forward(self, x):
        mask = TopKSTE.apply(self.scores, self.sparsity)
        return nn.functional.linear(x * 1.0, self.weight * mask, self.bias)

# Test gradient flows to scores
layer = MovementPruningLinearSTE(32, 16, sparsity=0.7)
x = torch.randn(4, 32)
loss = layer(x).sum()
loss.backward()
print(f'scores.grad is None: {layer.scores.grad is None}')
print(f'scores.grad norm: {layer.scores.grad.norm().item():.4f}')
```

## Movement vs Magnitude — BERT-QA Accuracy

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Reproduced from Sanh et al. 2020 (SQuAD v1.1 F1 at varying sparsity)
sparsity_levels = [0.0, 0.5, 0.7, 0.8, 0.85, 0.90, 0.95]

# Approximate F1 scores from paper (BERT-base fine-tuned on SQuAD)
magnitude_f1 = [88.5, 87.9, 86.1, 82.4, 78.3, 68.2, 45.1]
movement_f1  = [88.5, 88.2, 87.6, 86.8, 85.1, 82.4, 74.3]

print(f'{"Sparsity":>10}  {"Magnitude F1":>14}  {"Movement F1":>12}  {"Delta":>8}')
print('-' * 52)
for s, m, mv in zip(sparsity_levels, magnitude_f1, movement_f1):
    print(f'{s:>10.0%}  {m:>14.1f}  {mv:>12.1f}  {mv-m:>+8.1f}')

# Find crossover: at what sparsity does movement pruning gain >2 F1 points?
crossover = [(s, mv-m) for s, m, mv in zip(sparsity_levels, magnitude_f1, movement_f1)
             if mv - m > 2]
if crossover:
    print(f'\nMovement pruning gains >2 F1 at sparsity >= {crossover[0][0]:.0%}')
    print(f'Max gain: +{max(d for _,d in crossover):.1f} F1 at highest sparsity')
```

## Soft Movement Pruning

Hard movement pruning uses a discrete top-k mask. Soft movement pruning relaxes this: instead of enforcing exact sparsity via top-k, it adds an L1 regularization term on the scores: L_total = L_task + λ · ‖S‖₁. This drives most scores toward zero while allowing the model to choose which ones remain nonzero. There is no hard sparsity constraint; the regularization strength λ controls the trade-off. At convergence, remaining nonzero scores define the surviving weights.

```python
import torch
import torch.nn as nn
import torch.optim as optim

class SoftMovementPruningLinear(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.02)
        self.bias = nn.Parameter(torch.zeros(out_features))
        self.scores = nn.Parameter(torch.zeros(out_features, in_features))

    def forward(self, x):
        # Use sigmoid to get soft [0,1] mask (no discrete top-k)
        soft_mask = torch.sigmoid(self.scores * 10)  # sharp sigmoid
        return nn.functional.linear(x, self.weight * soft_mask, self.bias)

    def l1_score_loss(self):
        return self.scores.abs().mean()

def train_with_soft_movement(model, loader, criterion, epochs=3, lam=1e-4):
    optimizer = optim.AdamW(model.parameters(), lr=2e-4)
    for epoch in range(epochs):
        total_task, total_reg = 0.0, 0.0
        for X, y in loader:
            optimizer.zero_grad()
            task_loss = criterion(model(X), y)
            # L1 regularization on all score tensors
            reg_loss = sum(m.l1_score_loss() for m in model.modules()
                          if isinstance(m, SoftMovementPruningLinear))
            loss = task_loss + lam * reg_loss
            loss.backward()
            optimizer.step()
            total_task += task_loss.item()
            total_reg += reg_loss.item()
        print(f'Epoch {epoch+1}: task={total_task/len(loader):.4f}  reg={total_reg/len(loader):.4f}')

print('Soft movement pruning: scores driven to zero via L1, no discrete mask needed.')
```

> **When to Choose Movement Pruning**: Movement pruning is specifically designed for fine-tuning pretrained models like BERT. If you are training from scratch, magnitude pruning or Taylor pruning is equally effective. Movement pruning's advantage emerges because pre-trained weights that were large in the original model may become irrelevant after task-specific fine-tuning — magnitude pruning would keep them, while movement pruning correctly identifies and removes them.

## Winning Tickets at Task-Specific Level

The lottery ticket hypothesis states that large networks contain sparse subnetworks (winning tickets) that, when trained from initialization, match the full network's accuracy. Movement pruning finds winning tickets at the fine-tuning level: the sparse mask found by movement pruning on a fine-tuned BERT is task-specific and does not generalize across tasks. This is evidence that the lottery ticket structure is downstream of the task, not just of the pre-training.

- Scores S initialized to 0 at the start of fine-tuning — movement from zero signals importance.
- Top-k masking: exactly (1-k)% of weights are pruned; k is the target density.
- STE propagates gradients through discrete mask: score gradient ≈ weight gradient × mask.
- Soft variant: L1 penalty on scores avoids discrete top-k, smoother optimization landscape.
- At 80–90% sparsity, movement pruning retains 4–14 F1 points more than magnitude pruning on SQuAD.
- Task-specific tickets: the winning subnetwork is different for QA vs NLI vs sentiment tasks.

## Pruning Criteria Comparison

| Method | When Scores Computed | Criteria | BERT SQuAD F1 @ 90% | Supports Structure |
| --- | --- | --- | --- | --- |
| Magnitude pruning | Post-training, no gradient | |W_i| — static weight size | ~68 F1 | Yes (filter L1) |
| Movement pruning | During fine-tuning, gradient | Score S_i trained by ∂L/∂S | ~82 F1 | No — unstructured |
| Soft movement | During fine-tuning, gradient | L1(S) regularization, sigmoid mask | ~81 F1 | No — unstructured |
| SNIP | Before training (single pass) | |∂L/∂W_i · W_i| at init | ~72 F1 | Yes with extension |
| GraSP | Before training (Hessian approx) | -Hᵀg · W at init (gradient flow) | ~74 F1 | Limited |

## Practical Recommendations for BERT Pruning

For fine-tuned BERT models, apply movement pruning rather than magnitude pruning whenever sparsity exceeds 60%. Use a linear sparsity schedule: start at 0% and ramp to the target over the first 80% of fine-tuning steps, then hold the mask fixed for the remaining 20%. This warm-up avoids removing weights before the model has adapted to the task. Learning rate for scores should be 10–100× lower than the learning rate for weights; otherwise scores converge too fast and freeze before the model finds the best sparse subnetwork.

- Start fine-tuning with magnitude pruning warm-up (0→20% sparsity) before switching to movement scores.
- Score learning rate: 1e-2 to 1e-1 (much higher than weight LR 2e-5) works well empirically.
- Monitor gradient norms of scores — if they vanish, the temperature or LR needs adjustment.
- After reaching target sparsity, freeze the mask and fine-tune weights only for 10% more steps.
- For extreme sparsity (>95%), combine movement pruning with distillation from the dense teacher.

---

