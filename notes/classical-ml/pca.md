---
title: "PCA — SVD Derivation, Explained Variance, and Reconstruction"
slug: "pca"
description: "Principal Component Analysis from the ground up: SVD decomposition, explained variance ratio, k selection, reconstruction error, whitening, and randomized SVD for large sparse matrices."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUENBIGlzIHRoZSB3b3JraG9yc2Ugb2YgbGluZWFyIGRpbWVuc2lvbmFsaXR5IHJlZHVjdGlvbiwgdXNlZCBldmVyeXdoZXJlIGZyb20gZGF0YSBleHBsb3JhdGlvbiB0byBwcmVwcm9jZXNzaW5nIGZvciBkb3duc3RyZWFtIG1vZGVscy4gVW5kZXJzdGFuZGluZyBpdCB0aHJvdWdoIHRoZSBsZW5zIG9mIFNWRCByYXRoZXIgdGhhbiBqdXN0IGVpZ2VuZGVjb21wb3NpdGlvbiB1bmxvY2tzIGludHVpdGlvbiBhYm91dCByZWNvbnN0cnVjdGlvbiwgbm9pc2UsIGFuZCBhcHByb3hpbWF0aW9uIHF1YWxpdHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29yZSBJZGVhOiBEaXJlY3Rpb25zIG9mIE1heGltdW0gVmFyaWFuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdpdmVuIGEgY2VudGVyZWQgZGF0YSBtYXRyaXggWCDiiIgg4oSd4oG/y6PhtYgsIFBDQSBzZWVrcyBhbiBvcmRlcmVkIHNldCBvZiBvcnRob2dvbmFsIGRpcmVjdGlvbnMgdGhhdCBjYXB0dXJlIG1heGltdW0gdmFyaWFuY2UuIFRoZSBmaXJzdCBwcmluY2lwYWwgY29tcG9uZW50IHfigoEgbWF4aW1pc2VzIFZhcihYd+KCgSkgPSB34bWAWOG1gFh3L24gc3ViamVjdCB0byDigJZ34oCWPTEuIFRoZSBzb2x1dGlvbiBpcyB0aGUgdG9wIGVpZ2VudmVjdG9yIG9mIHRoZSBzYW1wbGUgY292YXJpYW5jZSBY4bWAWC8obi0xKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTVkQgRGVyaXZhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHNpbmd1bGFyIHZhbHVlIGRlY29tcG9zaXRpb24gWCA9IFXOo1bhtYAgZGVjb21wb3NlcyBYIGludG8gbGVmdCBzaW5ndWxhciB2ZWN0b3JzIFUg4oiIIOKEneKBv8uj4oG/LCBzaW5ndWxhciB2YWx1ZXMgzqMgPSBkaWFnKM+D4oKBLOKApizPg+KCmSksIGFuZCByaWdodCBzaW5ndWxhciB2ZWN0b3JzIFYg4oiIIOKEneG1iMuj4bWILiBUaGUgY29sdW1ucyBvZiBWIGFyZSB0aGUgcHJpbmNpcGFsIGNvbXBvbmVudHMuIFByb2plY3Rpbmcgb250byBrIGNvbXBvbmVudHM6IFogPSBYVuKCli4gQ292YXJpYW5jZSBjb25uZWN0aW9uOiBY4bWAWCA9IFbOo8KyVuG1gCwgc28gZWlnZW52YWx1ZXMgzrvhtaIgPSDPg+G1osKyLyhuLTEpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9pcmlzXG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgUENBXG5cbiMgTG9hZCBhbmQgY2VudGVyIGRhdGFcbmRhdGEgPSBsb2FkX2lyaXMoKVxuWCA9IGRhdGEuZGF0YS5hc3R5cGUoZmxvYXQpXG5YX2NlbnRlcmVkID0gWCAtIFgubWVhbihheGlzPTApXG5cbiMgRnVsbCBTVkQ6IFggPSBVICogU2lnbWEgKiBWdFxuVSwgc2lnbWEsIFZ0ID0gbnAubGluYWxnLnN2ZChYX2NlbnRlcmVkLCBmdWxsX21hdHJpY2VzPUZhbHNlKVxuIyBSb3dzIG9mIFZ0IGFyZSBwcmluY2lwYWwgY29tcG9uZW50cyAoY29sdW1ucyBvZiBWKVxuXG4jIFByb2plY3Qgb250byBrPTIgcHJpbmNpcGFsIGNvbXBvbmVudHNcbmsgPSAyXG5YX3BjYSA9IFhfY2VudGVyZWQgQCBWdFs6a10uVCAgIyBzaGFwZSAobl9zYW1wbGVzLCBrKVxuXG4jIFZlcmlmeSBhZ2FpbnN0IHNrbGVhcm4gKG1heSBkaWZmZXIgb25seSBpbiBzaWduKVxuc2twY2EgPSBQQ0Eobl9jb21wb25lbnRzPWspXG5YX3NrID0gc2twY2EuZml0X3RyYW5zZm9ybShYX2NlbnRlcmVkKVxuZGlmZiA9IG5wLmFicyhucC5hYnMoWF9wY2EpIC0gbnAuYWJzKFhfc2spKS5tYXgoKVxucHJpbnQoZlx1MDAyN01heCBkZXZpYXRpb24gZnJvbSBza2xlYXJuOiB7ZGlmZjouMmV9XHUwMDI3KVxuXG4jIEV4cGxhaW5lZCB2YXJpYW5jZSBmcm9tIHNpbmd1bGFyIHZhbHVlc1xuZXhwbGFpbmVkX3ZhciA9IChzaWdtYSAqKiAyKSAvIChsZW4oWCkgLSAxKVxuZXhwbGFpbmVkX3JhdGlvID0gZXhwbGFpbmVkX3ZhciAvIGV4cGxhaW5lZF92YXIuc3VtKClcbnByaW50KFx1MDAyN0V4cGxhaW5lZCB2YXJpYW5jZSByYXRpbzpcdTAwMjcsIG5wLnJvdW5kKGV4cGxhaW5lZF9yYXRpbywgMykpXG5wcmludChcdTAwMjdDdW11bGF0aXZlOlx1MDAyNywgbnAucm91bmQobnAuY3Vtc3VtKGV4cGxhaW5lZF9yYXRpbyksIDMpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4cGxhaW5lZCBWYXJpYW5jZSBSYXRpbyBhbmQgQ2hvb3NpbmcgayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGV4cGxhaW5lZCB2YXJpYW5jZSByYXRpbyBmb3IgY29tcG9uZW50IGkgaXMgz4PhtaLCsi/Oo+KxvM+D4rG8wrIuIEEgc2NyZWUgcGxvdCBzaG93cyB0aGUgZWxib3cgd2hlcmUgbWFyZ2luYWwgZ2FpbnMgZGltaW5pc2guIFRoZSBjdW11bGF0aXZlIGN1cnZlIGxldHMgeW91IGNob29zZSBrIHRvIHJldGFpbiBhIHRhcmdldCBmcmFjdGlvbiAoZS5nLiA5NSUpLiBUaGVyZSBpcyBubyB1bml2ZXJzYWxseSBjb3JyZWN0IGsg4oCUIGl0IGRlcGVuZHMgb24gdGhlIGRvd25zdHJlYW0gdGFza1x1MDAyN3Mgbm9pc2UgdG9sZXJhbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgZmV0Y2hfb3Blbm1sXG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgUENBXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuIyBNTklTVCBzdWJzZXQg4oCUIDUwMDAgc2FtcGxlc1xubW5pc3QgPSBmZXRjaF9vcGVubWwoXHUwMDI3bW5pc3RfNzg0XHUwMDI3LCB2ZXJzaW9uPTEsIGFzX2ZyYW1lPUZhbHNlKVxuWCA9IG1uaXN0LmRhdGFbOjUwMDBdLmFzdHlwZShmbG9hdClcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxucGNhID0gUENBKClcbnBjYS5maXQoWClcbmV2ciA9IHBjYS5leHBsYWluZWRfdmFyaWFuY2VfcmF0aW9fXG5jdW11bGF0aXZlID0gbnAuY3Vtc3VtKGV2cilcblxuIyBrIGZvciA5NSUgYW5kIDk5JSB2YXJpYW5jZVxua185NSA9IG5wLmFyZ21heChjdW11bGF0aXZlIFx1MDAzZT0gMC45NSkgKyAxXG5rXzk5ID0gbnAuYXJnbWF4KGN1bXVsYXRpdmUgXHUwMDNlPSAwLjk5KSArIDFcbnByaW50KGZcdTAwMjdrIGZvciA5NSUgdmFyaWFuY2U6IHtrXzk1fSwgIGsgZm9yIDk5JToge2tfOTl9XHUwMDI3KVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMSwgMiwgZmlnc2l6ZT0oMTIsIDQpKVxuYXhlc1swXS5wbG90KHJhbmdlKDEsIDUxKSwgZXZyWzo1MF0sIFx1MDAyN28tXHUwMDI3LCBtcz00KVxuYXhlc1swXS5zZXQoeGxhYmVsPVx1MDAyN0NvbXBvbmVudFx1MDAyNywgeWxhYmVsPVx1MDAyN0V4cGxhaW5lZCBWYXJpYW5jZSBSYXRpb1x1MDAyNywgdGl0bGU9XHUwMDI3U2NyZWUgUGxvdFx1MDAyNylcblxuYXhlc1sxXS5wbG90KHJhbmdlKDEsIGxlbihjdW11bGF0aXZlKSArIDEpLCBjdW11bGF0aXZlKVxuYXhlc1sxXS5heGhsaW5lKDAuOTUsIGNvbG9yPVx1MDAyN3JlZFx1MDAyNywgbHM9XHUwMDI3LS1cdTAwMjcsIGxhYmVsPVx1MDAyNzk1JVx1MDAyNylcbmF4ZXNbMV0uYXhobGluZSgwLjk5LCBjb2xvcj1cdTAwMjdvcmFuZ2VcdTAwMjcsIGxzPVx1MDAyNy0tXHUwMDI3LCBsYWJlbD1cdTAwMjc5OSVcdTAwMjcpXG5heGVzWzFdLmF4dmxpbmUoa185NSwgY29sb3I9XHUwMDI3cmVkXHUwMDI3LCBscz1cdTAwMjc6XHUwMDI3LCBhbHBoYT0wLjUpXG5heGVzWzFdLnNldCh4bGFiZWw9XHUwMDI3a1x1MDAyNywgeWxhYmVsPVx1MDAyN0N1bXVsYXRpdmUgRXhwbGFpbmVkIFZhcmlhbmNlXHUwMDI3KVxuYXhlc1sxXS5sZWdlbmQoKVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2hvdygpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJTY2FsZSBTZW5zaXRpdml0eSIsImNvbnRlbnQiOiJQQ0EgaXMgbm90IHNjYWxlLWludmFyaWFudC4gRmVhdHVyZXMgd2l0aCBsYXJnZSBtYWduaXR1ZGVzIGRvbWluYXRlIHRoZSBwcmluY2lwYWwgY29tcG9uZW50cy4gQWx3YXlzIHN0YW5kYXJkaXNlICh6ZXJvIG1lYW4sIHVuaXQgdmFyaWFuY2UpIGJlZm9yZSBhcHBseWluZyBQQ0EgdW5sZXNzIHRoZSBmZWF0dXJlcyBhcmUgZ2VudWluZWx5IG9uIHRoZSBzYW1lIHNjYWxlIHdpdGggbWVhbmluZ2Z1bCB2YXJpYW5jZSBkaWZmZXJlbmNlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZWNvbnN0cnVjdGlvbiBhbmQgUmVjb25zdHJ1Y3Rpb24gRXJyb3IifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlY29uc3RydWN0aW9uIHByb2plY3RzIGJhY2sgZnJvbSB0aGUgay1kaW1lbnNpb25hbCBzdWJzcGFjZTogeMyCID0gVuKCllbigpbhtYAoeCAtIM68KSArIM68LiBUaGlzIGlzIHRoZSBiZXN0IHJhbmstayBhcHByb3hpbWF0aW9uIGluIEZyb2Jlbml1cyBub3JtIChFY2thcnQtWW91bmcgdGhlb3JlbSkuIFJlY29uc3RydWN0aW9uIGVycm9yIGVxdWFscyB2YXJpYW5jZSBpbiBkaXNjYXJkZWQgZGltZW5zaW9uczogzqPhtaLigozigpbigorigoHhtYggz4PhtaLCsi8obi0xKS4gTG93ZXIgayBtZWFucyBtb3JlIGNvbXByZXNzaW9uIGFuZCBoaWdoZXIgcmVjb25zdHJ1Y3Rpb24gZXJyb3IuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2RpZ2l0c1xuZnJvbSBza2xlYXJuLmRlY29tcG9zaXRpb24gaW1wb3J0IFBDQVxuXG5YLCB5ID0gbG9hZF9kaWdpdHMocmV0dXJuX1hfeT1UcnVlKVxuWCA9IFggLyAxNi4wICAjIHNjYWxlIHRvIFswLCAxXVxubXUgPSBYLm1lYW4oYXhpcz0wKVxuXG5rcyA9IFsyLCA1LCAxMCwgMjAsIDQwLCA2NF1cbmVycm9ycyA9IFtdXG5mb3IgayBpbiBrczpcbiAgICBwY2EgPSBQQ0Eobl9jb21wb25lbnRzPWspXG4gICAgWF9yID0gcGNhLmZpdF90cmFuc2Zvcm0oWClcbiAgICBYX2hhdCA9IHBjYS5pbnZlcnNlX3RyYW5zZm9ybShYX3IpXG4gICAgZXJyb3JzLmFwcGVuZChucC5tZWFuKChYIC0gWF9oYXQpICoqIDIpKVxuXG5wbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKVxucGx0LnBsb3Qoa3MsIGVycm9ycywgXHUwMDI3by1cdTAwMjcpXG5wbHQueGxhYmVsKFx1MDAyN051bWJlciBvZiBDb21wb25lbnRzIGtcdTAwMjcpXG5wbHQueWxhYmVsKFx1MDAyN01lYW4gU3F1YXJlZCBSZWNvbnN0cnVjdGlvbiBFcnJvclx1MDAyNylcbnBsdC50aXRsZShcdTAwMjdQQ0EgUmVjb25zdHJ1Y3Rpb24gRXJyb3IgdnMga1x1MDAyNylcbnBsdC5ncmlkKFRydWUsIGFscGhhPTAuMylcbnBsdC5zaG93KClcblxuIyBNYW51YWwgcHJvamVjdGlvbjogeF9oYXQgPSBWay5UIEAgKFZrIEAgKHggLSBtdSkpICsgbXVcbnBjYTEwID0gUENBKG5fY29tcG9uZW50cz0xMCkuZml0KFgpXG5WayA9IHBjYTEwLmNvbXBvbmVudHNfICAjIChrLCBkKVxueCA9IFhbMF1cbnogPSBWayBAICh4IC0gbXUpICAgICAgICAjIGVuY29kZSB0byBsYXRlbnQgc3BhY2VcbnhfaGF0ID0gVmsuVCBAIHogKyBtdSAgICAjIGRlY29kZSBiYWNrIHRvIHBpeGVsIHNwYWNlXG5wcmludChmXHUwMDI3TWFudWFsIHJlY29uc3RydWN0aW9uIE1TRToge25wLm1lYW4oKHggLSB4X2hhdCkgKiogMik6LjZmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaGl0ZW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoaXRlbmluZyB0cmFuc2Zvcm1zIHByb2plY3RlZCBkYXRhIHRvIGlkZW50aXR5IGNvdmFyaWFuY2U6IHpfd2hpdGUgPSDOo+KCluKBu8K5VeKCluG1gHguIFRoaXMgc3RhbmRhcmRpc2VzIGVhY2ggUEMgdG8gdW5pdCB2YXJpYW5jZS4gUmVxdWlyZWQgYmVmb3JlIEZhc3RJQ0EgKHdoaWNoIGFzc3VtZXMgdW5jb3JyZWxhdGVkLCBlcXVhbC12YXJpYW5jZSBpbnB1dHMpLiBaQ0Egd2hpdGVuaW5nICg9IFXOo+KBu8K5VeG1gHgpIHByZXNlcnZlcyB0aGUgb3JpZ2luYWwgZmVhdHVyZSBzcGFjZSBvcmllbnRhdGlvbiB3aGlsZSBkZWNvcnJlbGF0aW5nIOKAlCB1c2VmdWwgZm9yIHByZXNlcnZpbmcgc3BhdGlhbCBzdHJ1Y3R1cmUgaW4gaW1hZ2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBDQSBhcyBNYXRyaXggRmFjdG9yaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUENBIHByb2R1Y2VzIHRoZSBiZXN0IHJhbmstayBhcHByb3hpbWF0aW9uIFgg4omIIFXigpbOo+KCllbigpbhtYAgPSBX4oKWSOKCliwgd2hlcmUgV+KCliA9IFXigpbOo+KCliBhcmUgdGhlIHNjb3JlcyBhbmQgSOKCliA9IFbigpbhtYAgYXJlIHRoZSBsb2FkaW5ncy4gTm8gb3RoZXIgcmFuay1rIG1hdHJpeCBhY2hpZXZlcyBhIHNtYWxsZXIgRnJvYmVuaXVzIG5vcm0gcmVzaWR1YWwuIE5NRiBhbmQgU3BhcnNlIFBDQSByZWxheCBvcnRob2dvbmFsaXR5IGFuZCBhZGQgbm9uLW5lZ2F0aXZpdHkgb3Igc3BhcnNpdHkgY29uc3RyYWludHMsIHlpZWxkaW5nIG1vcmUgaW50ZXJwcmV0YWJsZSBidXQgc3ViLW9wdGltYWwgZmFjdG9yaXphdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmFuZG9taXplZCBTVkQgZm9yIExhcmdlIE1hdHJpY2VzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGdWxsIFNWRCBjb3N0cyBPKG1pbihuwrJkLCBuZMKyKSksIHByb2hpYml0aXZlIGZvciBsYXJnZSBzcGFyc2UgbWF0cmljZXMuIFJhbmRvbWl6ZWQgU1ZEIHVzZXMgcmFuZG9tIHByb2plY3Rpb25zIHRvIGFwcHJveGltYXRlIHRoZSBrLWRpbWVuc2lvbmFsIHJhbmdlIG9mIFggaW4gTyhuZGsgKyAobitkKWvCsikg4oCUIG9yZGVycyBvZiBtYWduaXR1ZGUgZmFzdGVyIHdoZW4gayDiiaogbWluKG4sZCkuIHNrbGVhcm5cdTAwMjdzIFRydW5jYXRlZFNWRCBpbXBsZW1lbnRzIHRoaXMgbmF0aXZlbHkgZm9yIHNwYXJzZSBpbnB1dHMgYW5kIGlzIHRoZSBiYXNpcyBmb3IgTGF0ZW50IFNlbWFudGljIEFuYWx5c2lzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBUcnVuY2F0ZWRTVkRcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgZmV0Y2hfMjBuZXdzZ3JvdXBzXG5mcm9tIHNrbGVhcm4uZmVhdHVyZV9leHRyYWN0aW9uLnRleHQgaW1wb3J0IFRmaWRmVmVjdG9yaXplclxuaW1wb3J0IHRpbWVcblxubmV3cyA9IGZldGNoXzIwbmV3c2dyb3VwcyhzdWJzZXQ9XHUwMDI3dHJhaW5cdTAwMjcsIHJlbW92ZT0oXHUwMDI3aGVhZGVyc1x1MDAyNywgXHUwMDI3Zm9vdGVyc1x1MDAyNywgXHUwMDI3cXVvdGVzXHUwMDI3KSlcbnZlYyA9IFRmaWRmVmVjdG9yaXplcihtYXhfZmVhdHVyZXM9MjAwMDAsIHN0b3Bfd29yZHM9XHUwMDI3ZW5nbGlzaFx1MDAyNywgbWluX2RmPTUpXG5YX3NwYXJzZSA9IHZlYy5maXRfdHJhbnNmb3JtKG5ld3MuZGF0YSlcbnByaW50KGZcdTAwMjdNYXRyaXg6IHtYX3NwYXJzZS5zaGFwZX0sIG5uejoge1hfc3BhcnNlLm5uen1cdTAwMjcpXG5cbiMgUmFuZG9taXplZCBTVkQg4oCUIExhdGVudCBTZW1hbnRpYyBBbmFseXNpc1xuayA9IDEwMFxudDAgPSB0aW1lLnRpbWUoKVxuc3ZkID0gVHJ1bmNhdGVkU1ZEKG5fY29tcG9uZW50cz1rLCBhbGdvcml0aG09XHUwMDI3cmFuZG9taXplZFx1MDAyNywgcmFuZG9tX3N0YXRlPTQyLCBuX2l0ZXI9NSlcblhfbHNhID0gc3ZkLmZpdF90cmFuc2Zvcm0oWF9zcGFyc2UpXG5wcmludChmXHUwMDI3VHJ1bmNhdGVkU1ZEOiB7dGltZS50aW1lKCkgLSB0MDouMmZ9c1x1MDAyNylcbnByaW50KGZcdTAwMjdFeHBsYWluZWQgdmFyaWFuY2U6IHtzdmQuZXhwbGFpbmVkX3ZhcmlhbmNlX3JhdGlvXy5zdW0oKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JlZHVjZWQgc2hhcGU6IHtYX2xzYS5zaGFwZX1cdTAwMjcpXG5cbiMgVG9wIHdvcmRzIHBlciBsYXRlbnQgdG9waWNcbnRlcm1zID0gbnAuYXJyYXkodmVjLmdldF9mZWF0dXJlX25hbWVzX291dCgpKVxuZm9yIGkgaW4gcmFuZ2UoMyk6XG4gICAgdG9wX2lkeCA9IG5wLmFyZ3NvcnQoc3ZkLmNvbXBvbmVudHNfW2ldKVstMTA6XVs6Oi0xXVxuICAgIHRvcF9zdHIgPSBcdTAwMjcgXHUwMDI3LmpvaW4odGVybXNbdG9wX2lkeF0pXG4gICAgcHJpbnQoZlx1MDAyN1RvcGljIHtpfToge3RvcF9zdHJ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbWl0YXRpb25zIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMaW5lYXIgb25seSDigJQgY2Fubm90IGNhcHR1cmUgbm9ubGluZWFyIG1hbmlmb2xkcyAodXNlIEtlcm5lbCBQQ0EsIFVNQVAsIG9yIGF1dG9lbmNvZGVycykiLCJTY2FsZS1zZW5zaXRpdmUg4oCUIG11c3Qgc3RhbmRhcmRpc2UgYmVmb3JlIGFwcGx5aW5nIiwiTWF4aW1pc2luZyB2YXJpYW5jZSBpcyBub3QgYWx3YXlzIHRoZSByaWdodCBvYmplY3RpdmU7IElDQSBtYXhpbWlzZXMgaW5kZXBlbmRlbmNlLCBOTUYgbWF4aW1pc2VzIHBhcnRzLWJhc2VkIHN0cnVjdHVyZSIsIkRpc2NhcmRzIGNvcnJlbGF0ZWQgbm9pc2UgYWxvbmcgd2l0aCBzaWduYWwgd2hlbiB0cnVuY2F0aW5nIiwiUHJpbmNpcGFsIGNvbXBvbmVudHMgbWF5IG5vdCBiZSBpbnRlcnByZXRhYmxlIOKAlCBTcGFyc2UgUENBIG9yIElDQSBwcm9kdWNlIHNwYXJzZXIsIG1vcmUgbWVhbmluZ2Z1bCBjb21wb25lbnRzIiwiU2Vuc2l0aXZlIHRvIG91dGxpZXJzIOKAlCBhIHNpbmdsZSBvdXRsaWVyIGNhbiByb3RhdGUgYSBwcmluY2lwYWwgY29tcG9uZW50IHNpZ25pZmljYW50bHkiXX0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkxpbmVhciIsIkludGVycHJldGFibGUiLCJOb24tbmVnYXRpdmUiLCJSb2J1c3QgdG8gT3V0bGllcnMiLCJSZWNvbnN0cnVjdGlvbiJdLCJyb3dzIjpbWyJQQ0EiLCJZZXMiLCJNb2RlcmF0ZSIsIk5vIiwiTm8iLCJPcHRpbWFsIChGcm9iZW5pdXMpIl0sWyJJQ0EiLCJZZXMiLCJZZXMgKGluZGVwZW5kZW50KSIsIk5vIiwiTm8iLCJOb3QgdGhlIGdvYWwiXSxbIk5NRiIsIlllcyIsIlllcyAocGFydHMtYmFzZWQpIiwiWWVzIiwiTW9kZXJhdGUiLCJHb29kIl0sWyJBdXRvZW5jb2RlciIsIk5vIiwiTm8iLCJObyIsIlllcyAoZGVub2lzaW5nKSIsIkV4Y2VsbGVudCJdXX0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUENBIHJlbWFpbnMgdGhlIGZpcnN0IHRvb2wgdG8gcmVhY2ggZm9yIHdoZW4gZXhwbG9yaW5nIGhpZ2gtZGltZW5zaW9uYWwgZGF0YS4gSXRzIGNsb3NlZC1mb3JtIHNvbHV0aW9uLCBvcHRpbWFsaXR5IGd1YXJhbnRlZXMsIGFuZCBjb21wdXRhdGlvbmFsIGVmZmljaWVuY3kgYXJlIHVubWF0Y2hlZCBhbW9uZyBsaW5lYXIgbWV0aG9kcy4gRm9yIG5vbmxpbmVhciBzdHJ1Y3R1cmUsIEtlcm5lbCBQQ0Egb3IgVU1BUCBhcmUgbmF0dXJhbCBleHRlbnNpb25zOyBmb3IgaW50ZXJwcmV0YWJpbGl0eSwgU3BhcnNlIFBDQSBvciBJQ0EgcHJvdmlkZSBzcGFyc2VyLCBtb3JlIG1lYW5pbmdmdWwgZGVjb21wb3NpdGlvbnMuIn1d"
---
# PCA — SVD Derivation, Explained Variance, and Reconstruction

PCA is the workhorse of linear dimensionality reduction, used everywhere from data exploration to preprocessing for downstream models. Understanding it through the lens of SVD rather than just eigendecomposition unlocks intuition about reconstruction, noise, and approximation quality.

## Core Idea: Directions of Maximum Variance

Given a centered data matrix X ∈ ℝⁿˣᵈ, PCA seeks an ordered set of orthogonal directions that capture maximum variance. The first principal component w₁ maximises Var(Xw₁) = wᵀXᵀXw/n subject to ‖w‖=1. The solution is the top eigenvector of the sample covariance XᵀX/(n-1).

## SVD Derivation

The singular value decomposition X = UΣVᵀ decomposes X into left singular vectors U ∈ ℝⁿˣⁿ, singular values Σ = diag(σ₁,…,σₙ), and right singular vectors V ∈ ℝᵈˣᵈ. The columns of V are the principal components. Projecting onto k components: Z = XVₖ. Covariance connection: XᵀX = VΣ²Vᵀ, so eigenvalues λᵢ = σᵢ²/(n-1).

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load and center data
data = load_iris()
X = data.data.astype(float)
X_centered = X - X.mean(axis=0)

# Full SVD: X = U * Sigma * Vt
U, sigma, Vt = np.linalg.svd(X_centered, full_matrices=False)
# Rows of Vt are principal components (columns of V)

# Project onto k=2 principal components
k = 2
X_pca = X_centered @ Vt[:k].T  # shape (n_samples, k)

# Verify against sklearn (may differ only in sign)
skpca = PCA(n_components=k)
X_sk = skpca.fit_transform(X_centered)
diff = np.abs(np.abs(X_pca) - np.abs(X_sk)).max()
print(f'Max deviation from sklearn: {diff:.2e}')

# Explained variance from singular values
explained_var = (sigma ** 2) / (len(X) - 1)
explained_ratio = explained_var / explained_var.sum()
print('Explained variance ratio:', np.round(explained_ratio, 3))
print('Cumulative:', np.round(np.cumsum(explained_ratio), 3))
```

## Explained Variance Ratio and Choosing k

The explained variance ratio for component i is σᵢ²/Σⱼσⱼ². A scree plot shows the elbow where marginal gains diminish. The cumulative curve lets you choose k to retain a target fraction (e.g. 95%). There is no universally correct k — it depends on the downstream task's noise tolerance.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# MNIST subset — 5000 samples
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X = mnist.data[:5000].astype(float)
X = StandardScaler().fit_transform(X)

pca = PCA()
pca.fit(X)
evr = pca.explained_variance_ratio_
cumulative = np.cumsum(evr)

# k for 95% and 99% variance
k_95 = np.argmax(cumulative >= 0.95) + 1
k_99 = np.argmax(cumulative >= 0.99) + 1
print(f'k for 95% variance: {k_95},  k for 99%: {k_99}')

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(range(1, 51), evr[:50], 'o-', ms=4)
axes[0].set(xlabel='Component', ylabel='Explained Variance Ratio', title='Scree Plot')

axes[1].plot(range(1, len(cumulative) + 1), cumulative)
axes[1].axhline(0.95, color='red', ls='--', label='95%')
axes[1].axhline(0.99, color='orange', ls='--', label='99%')
axes[1].axvline(k_95, color='red', ls=':', alpha=0.5)
axes[1].set(xlabel='k', ylabel='Cumulative Explained Variance')
axes[1].legend()
plt.tight_layout()
plt.show()
```

> **Scale Sensitivity**: PCA is not scale-invariant. Features with large magnitudes dominate the principal components. Always standardise (zero mean, unit variance) before applying PCA unless the features are genuinely on the same scale with meaningful variance differences.

## Reconstruction and Reconstruction Error

Reconstruction projects back from the k-dimensional subspace: x̂ = VₖVₖᵀ(x - μ) + μ. This is the best rank-k approximation in Frobenius norm (Eckart-Young theorem). Reconstruction error equals variance in discarded dimensions: Σᵢ₌ₖ₊₁ᵈ σᵢ²/(n-1). Lower k means more compression and higher reconstruction error.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

X, y = load_digits(return_X_y=True)
X = X / 16.0  # scale to [0, 1]
mu = X.mean(axis=0)

ks = [2, 5, 10, 20, 40, 64]
errors = []
for k in ks:
    pca = PCA(n_components=k)
    X_r = pca.fit_transform(X)
    X_hat = pca.inverse_transform(X_r)
    errors.append(np.mean((X - X_hat) ** 2))

plt.figure(figsize=(8, 4))
plt.plot(ks, errors, 'o-')
plt.xlabel('Number of Components k')
plt.ylabel('Mean Squared Reconstruction Error')
plt.title('PCA Reconstruction Error vs k')
plt.grid(True, alpha=0.3)
plt.show()

# Manual projection: x_hat = Vk.T @ (Vk @ (x - mu)) + mu
pca10 = PCA(n_components=10).fit(X)
Vk = pca10.components_  # (k, d)
x = X[0]
z = Vk @ (x - mu)        # encode to latent space
x_hat = Vk.T @ z + mu    # decode back to pixel space
print(f'Manual reconstruction MSE: {np.mean((x - x_hat) ** 2):.6f}')
```

## Whitening

Whitening transforms projected data to identity covariance: z_white = Σₖ⁻¹Uₖᵀx. This standardises each PC to unit variance. Required before FastICA (which assumes uncorrelated, equal-variance inputs). ZCA whitening (= UΣ⁻¹Uᵀx) preserves the original feature space orientation while decorrelating — useful for preserving spatial structure in images.

## PCA as Matrix Factorization

PCA produces the best rank-k approximation X ≈ UₖΣₖVₖᵀ = WₖHₖ, where Wₖ = UₖΣₖ are the scores and Hₖ = Vₖᵀ are the loadings. No other rank-k matrix achieves a smaller Frobenius norm residual. NMF and Sparse PCA relax orthogonality and add non-negativity or sparsity constraints, yielding more interpretable but sub-optimal factorizations.

## Randomized SVD for Large Matrices

Full SVD costs O(min(n²d, nd²)), prohibitive for large sparse matrices. Randomized SVD uses random projections to approximate the k-dimensional range of X in O(ndk + (n+d)k²) — orders of magnitude faster when k ≪ min(n,d). sklearn's TruncatedSVD implements this natively for sparse inputs and is the basis for Latent Semantic Analysis.

```python
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import time

news = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
vec = TfidfVectorizer(max_features=20000, stop_words='english', min_df=5)
X_sparse = vec.fit_transform(news.data)
print(f'Matrix: {X_sparse.shape}, nnz: {X_sparse.nnz}')

# Randomized SVD — Latent Semantic Analysis
k = 100
t0 = time.time()
svd = TruncatedSVD(n_components=k, algorithm='randomized', random_state=42, n_iter=5)
X_lsa = svd.fit_transform(X_sparse)
print(f'TruncatedSVD: {time.time() - t0:.2f}s')
print(f'Explained variance: {svd.explained_variance_ratio_.sum():.3f}')
print(f'Reduced shape: {X_lsa.shape}')

# Top words per latent topic
terms = np.array(vec.get_feature_names_out())
for i in range(3):
    top_idx = np.argsort(svd.components_[i])[-10:][::-1]
    top_str = ' '.join(terms[top_idx])
    print(f'Topic {i}: {top_str}')
```

## Limitations

- Linear only — cannot capture nonlinear manifolds (use Kernel PCA, UMAP, or autoencoders)
- Scale-sensitive — must standardise before applying
- Maximising variance is not always the right objective; ICA maximises independence, NMF maximises parts-based structure
- Discards correlated noise along with signal when truncating
- Principal components may not be interpretable — Sparse PCA or ICA produce sparser, more meaningful components
- Sensitive to outliers — a single outlier can rotate a principal component significantly

| Method | Linear | Interpretable | Non-negative | Robust to Outliers | Reconstruction |
| --- | --- | --- | --- | --- | --- |
| PCA | Yes | Moderate | No | No | Optimal (Frobenius) |
| ICA | Yes | Yes (independent) | No | No | Not the goal |
| NMF | Yes | Yes (parts-based) | Yes | Moderate | Good |
| Autoencoder | No | No | No | Yes (denoising) | Excellent |

---

PCA remains the first tool to reach for when exploring high-dimensional data. Its closed-form solution, optimality guarantees, and computational efficiency are unmatched among linear methods. For nonlinear structure, Kernel PCA or UMAP are natural extensions; for interpretability, Sparse PCA or ICA provide sparser, more meaningful decompositions.

