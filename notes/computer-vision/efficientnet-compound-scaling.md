---
title: "EfficientNet: Compound Scaling of CNNs"
slug: "efficientnet-compound-scaling"
description: "Neural architecture search baseline (EfficientNet-B0) and compound scaling — simultaneously scaling width, depth, and resolution with coefficient φ for efficient accuracy gains."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFZmZpY2llbnROZXQgKFRhbiBcdTAwMjYgTGUsIDIwMTkpIGludHJvZHVjZWQgYSBwcmluY2lwbGVkIGFwcHJvYWNoIHRvIENOTiBzY2FsaW5nLiBJbnN0ZWFkIG9mIGFyYml0cmFyaWx5IGluY3JlYXNpbmcgd2lkdGgsIGRlcHRoLCBvciByZXNvbHV0aW9uLCBpdCB1c2VzIE5ldXJhbCBBcmNoaXRlY3R1cmUgU2VhcmNoIHRvIGZpbmQgYSBiYXNlbGluZSAoQjApIGFuZCB0aGVuIGEgY29tcG91bmQgc2NhbGluZyBtZXRob2QgdG8gZGVyaXZlIEIx4oCTQjcsIGFjaGlldmluZyBzdGF0ZS1vZi10aGUtYXJ0IGFjY3VyYWN5IHdpdGggZmFyIGZld2VyIHBhcmFtZXRlcnMgdGhhbiBwcmlvciBtb2RlbHMgbGlrZSBSZXNOZXQgb3IgRGVuc2VOZXQuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY29yZSBpbnNpZ2h0IGlzIHRoYXQgd2lkdGgsIGRlcHRoLCBhbmQgcmVzb2x1dGlvbiBhcmUgbm90IGluZGVwZW5kZW50IOKAlCBzY2FsaW5nIGFsbCB0aHJlZSB0b2dldGhlciBpbiBhIGZpeGVkIHJhdGlvLCBjb250cm9sbGVkIGJ5IGEgc2luZ2xlIGNvZWZmaWNpZW50IM+GLCBwcm9kdWNlcyBiZXR0ZXIgcmVzdWx0cyB0aGFuIHNjYWxpbmcgYW55IG9uZSBkaW1lbnNpb24gYWxvbmUuIEVmZmljaWVudE5ldC1CNyBhY2hpZXZlcyA4NC4zJSB0b3AtMSBvbiBJbWFnZU5ldCB1c2luZyA4LjTDlyBmZXdlciBwYXJhbWV0ZXJzIHRoYW4gdGhlIGJlc3QgY29udGVtcG9yYXJ5IG1vZGVscy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFZmZpY2llbnROZXQtQjAgQmFzZWxpbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBCMCBiYXNlbGluZSBpcyBmb3VuZCB2aWEgTmV1cmFsIEFyY2hpdGVjdHVyZSBTZWFyY2ggb3B0aW1pemluZyBhIG11bHRpLW9iamVjdGl2ZSByZXdhcmQ6IEFDQyhtKSDDlyBbRkxPUFMobSkvVF1edyB3aGVyZSB3PeKIkjAuMDcuIFRoZSBzZWFyY2ggc3BhY2UgaW5jbHVkZXMgTUJDb252IGJsb2NrcyB3aXRoIHNxdWVlemUtYW5kLWV4Y2l0YXRpb24sIHZhcnlpbmcgZXhwYW5zaW9uIHJhdGlvcyAoMSBvciA2KSwga2VybmVsIHNpemVzICgzw5czIG9yIDXDlzUpLCBhbmQgbnVtYmVyIG9mIGxheWVycyBwZXIgc3RhZ2UgYWNyb3NzIDkgc3RhZ2VzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWZmaWNpZW50TmV0LUIwIGhhcyA1LjNNIHBhcmFtZXRlcnMgYW5kIGFjaGlldmVzIDc3LjElIHRvcC0xIGFjY3VyYWN5IGF0IDIyNMOXMjI0IHJlc29sdXRpb24uIEl0IHVzZXMgNyBNQkNvbnYgc3RhZ2VzIHdpdGggdmFyeWluZyBjaGFubmVsIHdpZHRocyAoMTbihpIzMjApIGFuZCBleHBhbnNpb24gcmF0aW9zLCBwbHVzIGFuIGluaXRpYWwgc3RlbSBjb252IGFuZCBhIGZpbmFsIGhlYWQgd2l0aCAxMjgwIGNoYW5uZWxzLiBUaGlzIGNvbXBhY3QgYmFzZWxpbmUgaXMgdGhlIGZvdW5kYXRpb24gZm9yIGFsbCBFZmZpY2llbnROZXQtQjEgdGhyb3VnaCBCNyB2YXJpYW50cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wb3VuZCBTY2FsaW5nIEVxdWF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29tcG91bmQgc2NhbGluZyB1c2VzIGEgc2luZ2xlIHVzZXItZGVmaW5lZCBjb2VmZmljaWVudCDPhiB0byB1bmlmb3JtbHkgc2NhbGUgbmV0d29yayB3aWR0aCwgZGVwdGgsIGFuZCBpbnB1dCByZXNvbHV0aW9uLiBUaGlzIGNvbnRyYXN0cyB3aXRoIGFkLWhvYyBzY2FsaW5nIHdoZXJlIHByYWN0aXRpb25lcnMgaW5kZXBlbmRlbnRseSB0dW5lIGVhY2ggZGltZW5zaW9uLiBUaGUgbWV0aG9kIGlzIGdyb3VuZGVkIGluIHRoZSBvYnNlcnZhdGlvbiB0aGF0IGxhcmdlciBpbnB1dHMgbmVlZCBkZWVwZXIgbmV0d29ya3MgKG1vcmUgcmVjZXB0aXZlIGZpZWxkKSBhbmQgd2lkZXIgbmV0d29ya3MgKG1vcmUgZmluZS1ncmFpbmVkIGZlYXR1cmVzKSB0byBjYXB0dXJlIHJpY2hlciBwYXR0ZXJucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBDb21wb3VuZCBzY2FsaW5nIGNvZWZmaWNpZW50cyAoVGFuIFx1MDAyNiBMZSAyMDE5KVxuIyBDb25zdHJhaW50OiBhbHBoYSAqIGJldGFeMiAqIGdhbW1hXjIg4omIIDJcbiMgRm91bmQgdmlhIGdyaWQgc2VhcmNoIG9uIEIwOiBhbHBoYT0xLjIsIGJldGE9MS4xLCBnYW1tYT0xLjE1XG4jIHBoaSBpcyB0aGUgdXNlci1jaG9zZW4gc2NhbGluZyBjb2VmZmljaWVudFxuXG5hbHBoYSwgYmV0YSwgZ2FtbWEgPSAxLjIsIDEuMSwgMS4xNVxuXG5kZWYgY29tcG91bmRfc2NhbGUocGhpKTpcbiAgICBkZXB0aF9tdWx0ICA9IGFscGhhICoqIHBoaSAgICAgICAgIyBzY2FsZXMgbnVtYmVyIG9mIGxheWVyc1xuICAgIHdpZHRoX211bHQgID0gYmV0YSAgKiogcGhpICAgICAgICAjIHNjYWxlcyBjaGFubmVsIHdpZHRoc1xuICAgIHJlc29sdXRpb24gID0gZ2FtbWEgKiogcGhpICAgICAgICAjIHNjYWxlcyBpbnB1dCByZXNvbHV0aW9uXG4gICAgIyBGTE9QIGNvc3Qg4omIIGFscGhhICogYmV0YV4yICogZ2FtbWFeMiDiiYggMl5waGlcbiAgICByZXR1cm4gZGVwdGhfbXVsdCwgd2lkdGhfbXVsdCwgcmVzb2x1dGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvbnN0cmFpbnQgzrHCt86ywrLCt86zwrIg4omIIDIgZW5zdXJlcyB0aGF0IHRvdGFsIEZMT1BzIGdyb3cgYnkgYXBwcm94aW1hdGVseSAyXs+GIHdpdGggZWFjaCB1bml0IGluY3JlYXNlIGluIM+GLiBTaW5jZSBGTE9QcyBzY2FsZSBxdWFkcmF0aWNhbGx5IHdpdGggcmVzb2x1dGlvbiBhbmQgd2lkdGggYnV0IGxpbmVhcmx5IHdpdGggZGVwdGgsIHRoZSBzcXVhcmluZyBvZiDOsiBhbmQgzrMgYWNjb3VudHMgZm9yIHRoaXMgYXN5bW1ldHJ5IGFuZCBrZWVwcyBjb21wdXRlIGJ1ZGdldHMgcHJlZGljdGFibGUgYWNyb3NzIHRoZSBlbnRpcmUgRWZmaWNpZW50TmV0IHNjYWxpbmcgZmFtaWx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1CQ29udiBCbG9jayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIE1CQ29udiAoTW9iaWxlIEludmVydGVkIEJvdHRsZW5lY2sgQ29udm9sdXRpb24pIGJsb2NrIGlzIHRoZSBjb3JlIGJ1aWxkaW5nIGJsb2NrIG9mIEVmZmljaWVudE5ldCwgaW5oZXJpdGVkIGZyb20gTW9iaWxlTmV0VjIgd2l0aCBhbiBhZGRlZCBTcXVlZXplLWFuZC1FeGNpdGF0aW9uIChTRSkgbW9kdWxlLiBFYWNoIGJsb2NrIGV4cGFuZHMgY2hhbm5lbHMgYnkgYSBmYWN0b3IgKDHDlyBvciA2w5cpLCBhcHBsaWVzIGEgZGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbiwgYXBwbGllcyBjaGFubmVsIGF0dGVudGlvbiB2aWEgU0UsIHRoZW4gcHJvamVjdHMgYmFjayB0byB0aGUgb3V0cHV0IGNoYW5uZWwgY291bnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBNQkNvbnYobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wLCBvdXAsIHN0cmlkZSwgZXhwYW5kX3JhdGlvLCBzZV9yYXRpbz0wLjI1KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIG1pZCA9IGlucCAqIGV4cGFuZF9yYXRpb1xuICAgICAgICBzZWxmLnNraXAgPSAoc3RyaWRlID09IDEgYW5kIGlucCA9PSBvdXApXG4gICAgICAgIHNlbGYuY29udiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW5wLCBtaWQsIDEsIGJpYXM9RmFsc2UpLCBubi5CYXRjaE5vcm0yZChtaWQpLCBubi5TaUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQobWlkLCBtaWQsIDMsIHN0cmlkZSwgMSwgZ3JvdXBzPW1pZCwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTJkKG1pZCksIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIFNFQmxvY2sobWlkLCBpbnQoaW5wICogc2VfcmF0aW8pKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChtaWQsIG91cCwgMSwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTJkKG91cCksXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHggKyBzZWxmLmNvbnYoeCkgaWYgc2VsZi5za2lwIGVsc2Ugc2VsZi5jb252KHgpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgU2lMVSAoU3dpc2gpIGFjdGl2YXRpb24g4oCUIGYoeCk9eMK3z4MoeCkg4oCUIHJlcGxhY2VzIFJlTFUgdGhyb3VnaG91dCBFZmZpY2llbnROZXQgYW5kIGNvbnRyaWJ1dGVzIG1lYXN1cmFibHkgdG8gYWNjdXJhY3kuIFRoZSBTRSBibG9jayBwZXJmb3JtcyBnbG9iYWwgYXZlcmFnZSBwb29saW5nIHRoZW4gdHdvIEZDIGxheWVycyB0byBwcm9kdWNlIHBlci1jaGFubmVsIGF0dGVudGlvbiB3ZWlnaHRzIGluIFswLDFdLCBsZXR0aW5nIHRoZSBuZXR3b3JrIHJlY2FsaWJyYXRlIGZlYXR1cmUgbWFwcy4gU2tpcCBjb25uZWN0aW9ucyBhcmUgYXBwbGllZCB3aGVuIHN0cmlkZT0xIGFuZCBpbnB1dC9vdXRwdXQgY2hhbm5lbCBjb3VudHMgbWF0Y2ggZXhhY3RseS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsaW5nIGZyb20gQjAgdG8gQjcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVmZmljaWVudE5ldC1CMSB0aHJvdWdoIEI3IGFyZSBvYnRhaW5lZCBieSBhcHBseWluZyBjb21wb3VuZCBzY2FsaW5nIHdpdGggz4Y9MSB0aHJvdWdoIDcgdG8gdGhlIEIwIGJhc2VsaW5lLiBSZXNvbHV0aW9uIGluY3JlYXNlcyBmcm9tIDIyNHB4IChCMCkgdG8gNjAwcHggKEI3KSwgd2hpbGUgZGVwdGggYW5kIHdpZHRoIHNjYWxlIHByb3BvcnRpb25hbGx5LiBFYWNoIGluY3JlbWVudCBvZiDPhiByb3VnaGx5IGRvdWJsZXMgRkxPUHMgYnV0IGltcHJvdmVzIGFjY3VyYWN5IGJ5IDAuNeKAkzEuNSUgdG9wLTEsIG1ha2luZyB0aGUgdHJhZGVvZmYgY3VydmUgZmFyIG1vcmUgZmF2b3JhYmxlIHRoYW4gc2NhbGluZyBhbnkgc2luZ2xlIGRpbWVuc2lvbiBhbG9uZS4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJJbnB1dCBSZXMiLCJXaWR0aCDDlyBEZXB0aCBNdWx0IiwiVG9wLTEgJSIsIlBhcmFtcyAoTSkiLCJGTE9QcyAoRykiXSwicm93cyI6W1siQjAiLCIyMjQiLCIxLjAgw5cgMS4wIiwiNzcuMSIsIjUuMyIsIjAuMzkiXSxbIkIxIiwiMjQwIiwiMS4wIMOXIDEuMSIsIjc5LjEiLCI3LjgiLCIwLjcwIl0sWyJCMiIsIjI2MCIsIjEuMSDDlyAxLjIiLCI4MC4xIiwiOS4yIiwiMS4wIl0sWyJCMyIsIjMwMCIsIjEuMiDDlyAxLjQiLCI4MS42IiwiMTIiLCIxLjgiXSxbIkI0IiwiMzgwIiwiMS40IMOXIDEuOCIsIjgyLjkiLCIxOSIsIjQuMiJdLFsiQjUiLCI0NTYiLCIxLjYgw5cgMi4yIiwiODMuNiIsIjMwIiwiOS45Il0sWyJCNiIsIjUyOCIsIjEuOCDDlyAyLjYiLCI4NC4wIiwiNDMiLCIxOSJdLFsiQjciLCI2MDAiLCIyLjAgw5cgMy4xIiwiODQuMyIsIjY2IiwiMzciXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFdpZHRoIMOXIERlcHRoIG11bHRpcGxpZXJzIGFyZSBhcHBsaWVkIHRvIEIwIGNoYW5uZWwgY291bnRzIGFuZCBsYXllciBjb3VudHMgcGVyIHN0YWdlLiBOb3RlIHRoYXQgRkxPUHMgZ3JvdyBzdXBlci1saW5lYXJseSB3aXRoIG1vZGVsIGluZGV4IOKAlCBCNyB1c2VzIH45NcOXIG1vcmUgRkxPUHMgdGhhbiBCMCBmb3Igb25seSA3LjIlIGhpZ2hlciBhY2N1cmFjeS4gVGhpcyBpbGx1c3RyYXRlcyB3aHkgQjQgaXMgb2Z0ZW4gdGhlIHByYWN0aWNhbCBjZWlsaW5nLCBhbmQgd2h5IEVmZmljaWVudE5ldFYyIHJlZGVzaWduZWQgbGFyZ2UgbW9kZWwgc3RhZ2VzIHRvIHJlZHVjZSB0aGlzIG92ZXJoZWFkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2h2aXNpb24ubW9kZWxzIGFzIG1vZGVsc1xuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbiMgTG9hZCBwcmV0cmFpbmVkIEVmZmljaWVudE5ldC1CMDsgc3dhcCBjbGFzc2lmaWVyIGZvciBjdXN0b20gdGFza1xubW9kZWwgPSBtb2RlbHMuZWZmaWNpZW50bmV0X2IwKHdlaWdodHM9bW9kZWxzLkVmZmljaWVudE5ldF9CMF9XZWlnaHRzLklNQUdFTkVUMUtfVjEpXG5cbm51bV9jbGFzc2VzID0gMTBcbmluX2ZlYXR1cmVzID0gbW9kZWwuY2xhc3NpZmllclsxXS5pbl9mZWF0dXJlc1xubW9kZWwuY2xhc3NpZmllclsxXSA9IG5uLkxpbmVhcihpbl9mZWF0dXJlcywgbnVtX2NsYXNzZXMpXG5cbnRvdGFsID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpXG50cmFpbmFibGUgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWQpXG5wcmludChmXCJUb3RhbCBwYXJhbXM6IHt0b3RhbC8xZTY6LjJmfU0gfCBUcmFpbmFibGU6IHt0cmFpbmFibGUvMWU2Oi4yZn1NXCIpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGZpbmUtdHVuaW5nIEVmZmljaWVudE5ldCwgZnJlZXplIHRoZSBzdGVtIGFuZCBlYXJseSBzdGFnZXMgYW5kIHRyYWluIG9ubHkgbGF0ZXIgc3RhZ2VzIHBsdXMgdGhlIGNsYXNzaWZpZXIgaGVhZC4gVGhpcyB0eXBpY2FsbHkgeWllbGRzIDkwJSsgb2YgZnVsbCBmaW5lLXR1bmUgYWNjdXJhY3kgd2l0aCAz4oCTNcOXIGZhc3RlciBjb252ZXJnZW5jZS4gVXNlIGlucHV0IHNpemVzIG1hdGNoaW5nIHRoZSB2YXJpYW50ICgyMjQgZm9yIEIwLCAzODAgZm9yIEI0KSBhbmQgYXBwbHkgSW1hZ2VOZXQgbm9ybWFsaXphdGlvbiAobWVhbj1bMC40ODUsMC40NTYsMC40MDZdLCBzdGQ9WzAuMjI5LDAuMjI0LDAuMjI1XSkgY29uc2lzdGVudGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRob3AgaW1wb3J0IHByb2ZpbGVcbmltcG9ydCB0b3JjaCwgdG9yY2h2aXNpb24ubW9kZWxzIGFzIE1cblxucmVzdWx0cyA9IHt9XG5mb3IgbmFtZSwgY2xzLCByZXMgaW4gW1xuICAgIChcIkIwXCIsIE0uZWZmaWNpZW50bmV0X2IwLCAyMjQpLCAoXCJCMVwiLCBNLmVmZmljaWVudG5ldF9iMSwgMjQwKSxcbiAgICAoXCJCMlwiLCBNLmVmZmljaWVudG5ldF9iMiwgMjYwKSwgKFwiQjNcIiwgTS5lZmZpY2llbnRuZXRfYjMsIDMwMCksXG4gICAgKFwiQjRcIiwgTS5lZmZpY2llbnRuZXRfYjQsIDM4MCksXG5dOlxuICAgIG0gPSBjbHMod2VpZ2h0cz1Ob25lKVxuICAgIHggPSB0b3JjaC5yYW5kbigxLCAzLCByZXMsIHJlcylcbiAgICBmbG9wcywgcGFyYW1zID0gcHJvZmlsZShtLCBpbnB1dHM9KHgsKSwgdmVyYm9zZT1GYWxzZSlcbiAgICByZXN1bHRzW25hbWVdID0ge1wiZ2Zsb3BzXCI6IGZsb3BzLzFlOSwgXCJwYXJhbXNfbVwiOiBwYXJhbXMvMWU2fVxuICAgIHByaW50KGZcIntuYW1lfSAoe3Jlc31weCk6IHtmbG9wcy8xZTk6LjJmfSBHRkxPUHMsIHtwYXJhbXMvMWU2Oi4xZn1NIHBhcmFtc1wiKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRkxPUHMgcm91Z2hseSBkb3VibGUgd2l0aCBlYWNoIHN0ZXAgZnJvbSBCMCB0byBCMywgdGhlbiBpbmNyZWFzZSBtb3JlIHN0ZWVwbHkgYXMgcmVzb2x1dGlvbiBncm93cy4gUGxvdHRpbmcgYWNjdXJhY3kgdnMuIEZMT1BzIG9uIGEgbG9nIHNjYWxlIHNob3dzIEVmZmljaWVudE5ldCBvbiBhIFBhcmV0byBmcm9udGllciBhYm92ZSBSZXNOZXQgYW5kIFZHRyBhdCBhbGwgY29tcHV0ZSBwb2ludHMuIEZvciBiYXRjaCBpbmZlcmVuY2Ugb24gVjEwMCwgQjAgYWNoaWV2ZXMgfjI1MDAgaW1hZ2VzL3NlYyB3aGlsZSBCNCBhY2hpZXZlcyB+MzUwIGltYWdlcy9zZWMg4oCUIGEgN8OXIHRocm91Z2hwdXQgZ2FwIGZvciA1LjglIGFjY3VyYWN5IGdhaW4uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwiY29udGVudCI6IkVmZmljaWVudE5ldC1CNCAoMzgwcHgsIDE5TSBwYXJhbXMpIGlzIHVzdWFsbHkgdGhlIGJlc3QgdHJhZGVvZmYg4oCUIEI1KyBnaXZlIGRpbWluaXNoaW5nIHJldHVybnMgYXQgbXVjaCBoaWdoZXIgY29zdC4gVXNlIEIwIGZvciBlZGdlL21vYmlsZSBhbmQgQjQgZm9yIHNlcnZlciBpbmZlcmVuY2UuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFZmZpY2llbnROZXQgc2hvd2VkIHRoYXQgY29tcG91bmQgc2NhbGluZyBiZWF0cyBhZC1ob2Mgc2luZ2xlLWF4aXMgc2NhbGluZy4gVGhlIHBhdHRlcm4gZ2VuZXJhbGl6ZXM6IEVmZmljaWVudERldCBhcHBsaWVzIGl0IHRvIGRldGVjdGlvbiBiYWNrYm9uZXMsIEVmZmljaWVudE5ldFYyIHN3YXBzIGVhcmx5IE1CQ29udjYgZm9yIEZ1c2VkLU1CQ29udiBhbmQgYWRkcyBwcm9ncmVzc2l2ZSB0cmFpbmluZy4gQ29yZSBsZXNzb246IGpvaW50bHkgb3B0aW1pemluZyB3aWR0aCwgZGVwdGgsIGFuZCByZXNvbHV0aW9uIHVuZGVyIGEgZml4ZWQgY29tcHV0ZSBidWRnZXQgeWllbGRzIG1vZGVscyB0aGF0IHRyYW5zZmVyIGV4Y2VwdGlvbmFsbHkgd2VsbCB3aXRoIG1pbmltYWwgZmluZS10dW5pbmcgZWZmb3J0LiJ9XQ=="
---
# EfficientNet: Compound Scaling of CNNs

## Overview

EfficientNet (Tan & Le, 2019) introduced a principled approach to CNN scaling. Instead of arbitrarily increasing width, depth, or resolution, it uses Neural Architecture Search to find a baseline (B0) and then a compound scaling method to derive B1–B7, achieving state-of-the-art accuracy with far fewer parameters than prior models like ResNet or DenseNet.

The core insight is that width, depth, and resolution are not independent — scaling all three together in a fixed ratio, controlled by a single coefficient φ, produces better results than scaling any one dimension alone. EfficientNet-B7 achieves 84.3% top-1 on ImageNet using 8.4× fewer parameters than the best contemporary models.

## EfficientNet-B0 Baseline

The B0 baseline is found via Neural Architecture Search optimizing a multi-objective reward: ACC(m) × [FLOPS(m)/T]^w where w=−0.07. The search space includes MBConv blocks with squeeze-and-excitation, varying expansion ratios (1 or 6), kernel sizes (3×3 or 5×5), and number of layers per stage across 9 stages.

EfficientNet-B0 has 5.3M parameters and achieves 77.1% top-1 accuracy at 224×224 resolution. It uses 7 MBConv stages with varying channel widths (16→320) and expansion ratios, plus an initial stem conv and a final head with 1280 channels. This compact baseline is the foundation for all EfficientNet-B1 through B7 variants.

## Compound Scaling Equations

Compound scaling uses a single user-defined coefficient φ to uniformly scale network width, depth, and input resolution. This contrasts with ad-hoc scaling where practitioners independently tune each dimension. The method is grounded in the observation that larger inputs need deeper networks (more receptive field) and wider networks (more fine-grained features) to capture richer patterns.

```python
# Compound scaling coefficients (Tan & Le 2019)
# Constraint: alpha * beta^2 * gamma^2 ≈ 2
# Found via grid search on B0: alpha=1.2, beta=1.1, gamma=1.15
# phi is the user-chosen scaling coefficient

alpha, beta, gamma = 1.2, 1.1, 1.15

def compound_scale(phi):
    depth_mult  = alpha ** phi        # scales number of layers
    width_mult  = beta  ** phi        # scales channel widths
    resolution  = gamma ** phi        # scales input resolution
    # FLOP cost ≈ alpha * beta^2 * gamma^2 ≈ 2^phi
    return depth_mult, width_mult, resolution
```

The constraint α·β²·γ² ≈ 2 ensures that total FLOPs grow by approximately 2^φ with each unit increase in φ. Since FLOPs scale quadratically with resolution and width but linearly with depth, the squaring of β and γ accounts for this asymmetry and keeps compute budgets predictable across the entire EfficientNet scaling family.

## MBConv Block

The MBConv (Mobile Inverted Bottleneck Convolution) block is the core building block of EfficientNet, inherited from MobileNetV2 with an added Squeeze-and-Excitation (SE) module. Each block expands channels by a factor (1× or 6×), applies a depthwise separable convolution, applies channel attention via SE, then projects back to the output channel count.

```python
import torch.nn as nn

class MBConv(nn.Module):
    def __init__(self, inp, oup, stride, expand_ratio, se_ratio=0.25):
        super().__init__()
        mid = inp * expand_ratio
        self.skip = (stride == 1 and inp == oup)
        self.conv = nn.Sequential(
            nn.Conv2d(inp, mid, 1, bias=False), nn.BatchNorm2d(mid), nn.SiLU(),
            nn.Conv2d(mid, mid, 3, stride, 1, groups=mid, bias=False), nn.BatchNorm2d(mid), nn.SiLU(),
            SEBlock(mid, int(inp * se_ratio)),
            nn.Conv2d(mid, oup, 1, bias=False), nn.BatchNorm2d(oup),
        )
    def forward(self, x):
        return x + self.conv(x) if self.skip else self.conv(x)
```

The SiLU (Swish) activation — f(x)=x·σ(x) — replaces ReLU throughout EfficientNet and contributes measurably to accuracy. The SE block performs global average pooling then two FC layers to produce per-channel attention weights in [0,1], letting the network recalibrate feature maps. Skip connections are applied when stride=1 and input/output channel counts match exactly.

## Scaling from B0 to B7

EfficientNet-B1 through B7 are obtained by applying compound scaling with φ=1 through 7 to the B0 baseline. Resolution increases from 224px (B0) to 600px (B7), while depth and width scale proportionally. Each increment of φ roughly doubles FLOPs but improves accuracy by 0.5–1.5% top-1, making the tradeoff curve far more favorable than scaling any single dimension alone.

| Model | Input Res | Width × Depth Mult | Top-1 % | Params (M) | FLOPs (G) |
| --- | --- | --- | --- | --- | --- |
| B0 | 224 | 1.0 × 1.0 | 77.1 | 5.3 | 0.39 |
| B1 | 240 | 1.0 × 1.1 | 79.1 | 7.8 | 0.70 |
| B2 | 260 | 1.1 × 1.2 | 80.1 | 9.2 | 1.0 |
| B3 | 300 | 1.2 × 1.4 | 81.6 | 12 | 1.8 |
| B4 | 380 | 1.4 × 1.8 | 82.9 | 19 | 4.2 |
| B5 | 456 | 1.6 × 2.2 | 83.6 | 30 | 9.9 |
| B6 | 528 | 1.8 × 2.6 | 84.0 | 43 | 19 |
| B7 | 600 | 2.0 × 3.1 | 84.3 | 66 | 37 |

The Width × Depth multipliers are applied to B0 channel counts and layer counts per stage. Note that FLOPs grow super-linearly with model index — B7 uses ~95× more FLOPs than B0 for only 7.2% higher accuracy. This illustrates why B4 is often the practical ceiling, and why EfficientNetV2 redesigned large model stages to reduce this overhead.

```python
import torchvision.models as models
import torch.nn as nn

# Load pretrained EfficientNet-B0; swap classifier for custom task
model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.IMAGENET1K_V1)

num_classes = 10
in_features = model.classifier[1].in_features
model.classifier[1] = nn.Linear(in_features, num_classes)

total = sum(p.numel() for p in model.parameters())
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Total params: {total/1e6:.2f}M | Trainable: {trainable/1e6:.2f}M")
```

When fine-tuning EfficientNet, freeze the stem and early stages and train only later stages plus the classifier head. This typically yields 90%+ of full fine-tune accuracy with 3–5× faster convergence. Use input sizes matching the variant (224 for B0, 380 for B4) and apply ImageNet normalization (mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225]) consistently.

```python
from thop import profile
import torch, torchvision.models as M

results = {}
for name, cls, res in [
    ("B0", M.efficientnet_b0, 224), ("B1", M.efficientnet_b1, 240),
    ("B2", M.efficientnet_b2, 260), ("B3", M.efficientnet_b3, 300),
    ("B4", M.efficientnet_b4, 380),
]:
    m = cls(weights=None)
    x = torch.randn(1, 3, res, res)
    flops, params = profile(m, inputs=(x,), verbose=False)
    results[name] = {"gflops": flops/1e9, "params_m": params/1e6}
    print(f"{name} ({res}px): {flops/1e9:.2f} GFLOPs, {params/1e6:.1f}M params")
```

FLOPs roughly double with each step from B0 to B3, then increase more steeply as resolution grows. Plotting accuracy vs. FLOPs on a log scale shows EfficientNet on a Pareto frontier above ResNet and VGG at all compute points. For batch inference on V100, B0 achieves ~2500 images/sec while B4 achieves ~350 images/sec — a 7× throughput gap for 5.8% accuracy gain.

## Key Takeaways

> **tip**: EfficientNet-B4 (380px, 19M params) is usually the best tradeoff — B5+ give diminishing returns at much higher cost. Use B0 for edge/mobile and B4 for server inference.

EfficientNet showed that compound scaling beats ad-hoc single-axis scaling. The pattern generalizes: EfficientDet applies it to detection backbones, EfficientNetV2 swaps early MBConv6 for Fused-MBConv and adds progressive training. Core lesson: jointly optimizing width, depth, and resolution under a fixed compute budget yields models that transfer exceptionally well with minimal fine-tuning effort.

