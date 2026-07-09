---
title: "Sharp vs Flat Minima and Generalization"
slug: "sharp-flat-minima-generalization"
description: "Theoretical and empirical analysis of sharpness measures, PAC-Bayes generalization bounds, SAM optimizer, and why SGD noise biases training toward flat minima with better test performance."
tags: ["optimization", "generalization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTm90IGFsbCBtaW5pbWEgb2YgYSBuZXVyYWwgbmV0d29yaydzIHRyYWluaW5nIGxvc3MgYXJlIGNyZWF0ZWQgZXF1YWw6IHNvbWUgZ2VuZXJhbGl6ZSB3ZWxsIHRvIGhlbGQtb3V0IGRhdGEsIG90aGVycyBtZW1vcml6ZSB0aGUgdHJhaW5pbmcgc2V0LiBUaGUgZ2VvbWV0cnkgb2YgdGhlIG1pbmltdW0g4oCUIHNwZWNpZmljYWxseSBpdHMgc2hhcnBuZXNzIChjdXJ2YXR1cmUpIOKAlCBwcmVkaWN0cyB0aGlzIGRpZmZlcmVuY2UuIEEgZmxhdCBtaW5pbXVtIGlzIG9uZSB3aGVyZSB0aGUgbG9zcyBjaGFuZ2VzIHNsb3dseSBhcyB3ZWlnaHRzIG1vdmUgaW4gYW55IGRpcmVjdGlvbjsgYSBzaGFycCBtaW5pbXVtIGhhcyBkaXJlY3Rpb25zIG9mIGhpZ2ggY3VydmF0dXJlIHdoZXJlIHNtYWxsIHdlaWdodCBwZXJ0dXJiYXRpb25zIGNhdXNlIGxhcmdlIGxvc3Mgc3Bpa2VzLiBUaGlzIG5vdGUgYnVpbGRzIGZyb20gZm9ybWFsIHNoYXJwbmVzcyBtZWFzdXJlcyB0aHJvdWdoIHRoZSBQQUMtQmF5ZXMgYm91bmQgdGhhdCBleHBsYWlucyB3aHkgZmxhdCBtaW5pbWEgZ2VuZXJhbGl6ZSBiZXR0ZXIsIHRvIHRoZSBTQU0gb3B0aW1pemVyIHRoYXQgZXhwbGljaXRseSB0YXJnZXRzIGZsYXQgbWluaW1hLCBhbmQgdGhlIGNvbm5lY3Rpb24gYmV0d2VlbiBTR0Qgbm9pc2UgYW5kIGltcGxpY2l0IHJlZ3VsYXJpemF0aW9uIHRvd2FyZCBmbGF0IHJlZ2lvbnMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTWVhc3VyaW5nIFNoYXJwbmVzcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBsYXJnZXN0IEhlc3NpYW4gZWlnZW52YWx1ZSDOu19tYXggbWVhc3VyZXMgc2hhcnBuZXNzIGluIHRoZSB3b3JzdC1jYXNlIGRpcmVjdGlvbjogZXZlbiBvbmUgZGlyZWN0aW9uIG9mIGhpZ2ggY3VydmF0dXJlIG1ha2VzIGEgbWluaW11bSBzaGFycC4gVGhlIEhlc3NpYW4gdHJhY2UgdHIoSCkgPSDOo8674bWiIG1lYXN1cmVzIGF2ZXJhZ2UgY3VydmF0dXJlIG92ZXIgYWxsIGRpcmVjdGlvbnMg4oCUIGNoZWFwZXIgdG8gZXN0aW1hdGUgdGhhbiDOu19tYXggKEh1dGNoaW5zb24ncyBlc3RpbWF0b3IgdXNlcyB0cihIKSDiiYggReG1pVt24bWASHZdIHdpdGggcmFuZG9tIMKxMSB2ZWN0b3JzIHYpLiBUaGUgc2hhcnBuZXNzIHJhdGlvIM+BX3NoYXJwID0gbWF4X3vigJbOtOKAluKJpM+BfSBbTCjOuCvOtCkg4oiSIEwozrgpXSBhc2tzOiBob3cgbXVjaCBkb2VzIGxvc3MgaW5jcmVhc2UgaWYgd2UgcGVydHVyYiB3ZWlnaHRzIGJ5IGF0IG1vc3Qgz4EgaW4gYW55IGRpcmVjdGlvbj8gSG9jaHJlaXRlciBhbmQgU2NobWlkaHViZXIgKDE5OTcpIGdhdmUgYSBNaW5pbXVtIERlc2NyaXB0aW9uIExlbmd0aCBhcmd1bWVudDogYSBmbGF0IG1pbmltdW0gY2FuIGJlIGVuY29kZWQgd2l0aCBsb3dlciB3ZWlnaHQgcHJlY2lzaW9uIChmZXdlciBiaXRzKSBiZWNhdXNlIHNtYWxsIHF1YW50aXphdGlvbiBlcnJvcnMgbGVhdmUgdGhlIGxvc3MgdW5jaGFuZ2VkOyBmZXdlciBiaXRzIOKGkiBzaG9ydGVyIGRlc2NyaXB0aW9uIOKGkiBiZXR0ZXIgZ2VuZXJhbGl6YXRpb24gYnkgTURML09jY2FtJ3MgcmF6b3IuIFByYWN0aWNhbGx5OiB0d28gbW9kZWxzIHdpdGggdGhlIHNhbWUgdHJhaW5pbmcgbG9zcyBidXQgZGlmZmVyZW50IHNoYXJwbmVzcyB3aWxsIGhhdmUgZGlmZmVyZW50IHRlc3QgbG9zczsgdGhlIGZsYXR0ZXIgbW9kZWwgZ2VuZXJhbGl6ZXMgYmV0dGVyIGJ5IGFuIGFtb3VudCBwcmVkaWN0ZWQgYnkgdGhlIFBBQy1CYXllcyBib3VuZC4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaC5hdXRvZ3JhZC5mdW5jdGlvbmFsIGltcG9ydCBodnBcblxuZGVmIGh1dGNoaW5zb25fdHJhY2UobW9kZWwsIGxvc3NfZm4sIFgsIHksIG5fc2FtcGxlcz0yMCk6XG4gICAgXCJcIlwiRXN0aW1hdGUgSGVzc2lhbiB0cmFjZSB2aWEgSHV0Y2hpbnNvbidzIG1ldGhvZC5cIlwiXCJcbiAgICBsb3NzID0gbG9zc19mbihtb2RlbChYKSwgeSlcbiAgICBwYXJhbXMgPSBbcCBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkgaWYgcC5yZXF1aXJlc19ncmFkXVxuICAgIGdyYWRzID0gdG9yY2guYXV0b2dyYWQuZ3JhZChsb3NzLCBwYXJhbXMsIGNyZWF0ZV9ncmFwaD1UcnVlKVxuICAgIGdyYWRfdmVjID0gdG9yY2guY2F0KFtnLmZsYXR0ZW4oKSBmb3IgZyBpbiBncmFkc10pXG4gICAgdHJhY2VfZXN0ID0gMC4wXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl9zYW1wbGVzKTpcbiAgICAgICAgdiA9IHRvcmNoLnJhbmRpbnQoMCwgMiwgZ3JhZF92ZWMuc2hhcGUpLmZsb2F0KCkgKiAyIC0gMVxuICAgICAgICBIdiA9IHRvcmNoLmF1dG9ncmFkLmdyYWQoZ3JhZF92ZWMgQCB2LmRldGFjaCgpLCBwYXJhbXMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcmV0YWluX2dyYXBoPVRydWUpXG4gICAgICAgIEh2X2ZsYXQgPSB0b3JjaC5jYXQoW2guZmxhdHRlbigpIGZvciBoIGluIEh2XSlcbiAgICAgICAgdHJhY2VfZXN0ICs9ICh2ICogSHZfZmxhdCkuc3VtKCkuaXRlbSgpXG4gICAgcmV0dXJuIHRyYWNlX2VzdCAvIG5fc2FtcGxlc1xuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuWCA9IHRvcmNoLnJhbmRuKDY0LCAxMClcbnkgPSB0b3JjaC5yYW5kbig2NCwgMSlcbm1vZGVsX3NoYXJwID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMTAsIDQpLCBubi5SZUxVKCksIG5uLkxpbmVhcig0LCAxKSlcbm1vZGVsX2ZsYXQgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcigxMCwgNCksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDQsIDEpKVxubm4uaW5pdC5ub3JtYWxfKGxpc3QobW9kZWxfc2hhcnAucGFyYW1ldGVycygpKVswXSwgc3RkPTIuMClcbmxvc3NfZm4gPSBubi5NU0VMb3NzKClcbnRyYWNlX3NoYXJwID0gaHV0Y2hpbnNvbl90cmFjZShtb2RlbF9zaGFycCwgbG9zc19mbiwgWCwgeSlcbnRyYWNlX2ZsYXQgPSBodXRjaGluc29uX3RyYWNlKG1vZGVsX2ZsYXQsIGxvc3NfZm4sIFgsIHkpXG5wcmludChmXCJTaGFycCBtb2RlbCBIZXNzaWFuIHRyYWNlIGVzdGltYXRlOiB7dHJhY2Vfc2hhcnA6LjJmfVwiKVxucHJpbnQoZlwiRmxhdCBtb2RlbCBIZXNzaWFuIHRyYWNlIGVzdGltYXRlOiAge3RyYWNlX2ZsYXQ6LjJmfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlBBQy1CYXllcyBCb3VuZCBhbmQgU2hhcnBuZXNzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiUEFDLUJheWVzIHRoZW9yZW0gKE1jQWxsZXN0ZXIgMTk5OSk6IGZvciBhbnkgcHJpb3IgUCBhbmQgcG9zdGVyaW9yIFEgb3ZlciBoeXBvdGhlc2VzLCB3aXRoIHByb2JhYmlsaXR5IGF0IGxlYXN0IDHiiJLOtCBvdmVyIHNhbXBsZXMgb2Ygc2l6ZSBuOiBMX3Rlc3QoUSkg4omkIExfdHJhaW4oUSkgKyBzcXJ0KChLTChRfHxQKSArIGxvZygxL860KSkgLyAoMm4pKS4gU2V0dGluZyBRID0gTijOuCosIM+DwrJJKSAoR2F1c3NpYW4gcG9zdGVyaW9yIGFyb3VuZCB0aGUgc29sdXRpb24pIGFuZCBQID0gTigwLCDPg8KySSkgKHN0YW5kYXJkIHByaW9yKSwgdGhlIEtMIGRpdmVyZ2VuY2UgS0woUXx8UCkg4omIIOKAls64KuKAlsKyLygyz4PCsikuIEZvcmV0IGV0IGFsLiAoMjAyMSkgaW50ZXJwcmV0IHRoZSBzaGFycG5lc3MtYXdhcmUgb2JqZWN0aXZlIGFzIG1pbmltaXppbmcgYW4gdXBwZXIgYm91bmQgZnJvbSB0aGlzIHRoZW9yZW06IG1heGltaXppbmcgz4MgKGFsbG93ZWQgcGVydHVyYmF0aW9uIHJhZGl1cykgdG8ga2VlcCB0aGUgbG9zcyBzdGFibGUgaXMgZXF1aXZhbGVudCB0byBtaW5pbWl6aW5nIHRoZSBtYXhpbXVtIGxvc3MgaW4gYSBiYWxsIG9mIHJhZGl1cyDPgSBhcm91bmQgzrgqLiBUaGUgU0FNIG9iamVjdGl2ZSBtYXhfe+KAls614oCW4omkz4F9IEwozrgrzrUpIGRpcmVjdGx5IG1lYXN1cmVzIHRoZSB3b3JzdC1jYXNlIHBlcnR1cmJhdGlvbiBsb3NzLCBhbmQgbWluaW1pemluZyBpdCBzaW11bHRhbmVvdXNseSBwdXNoZXMgZG93biB0cmFpbmluZyBsb3NzIGFuZCB0aGUgS0wgdGVybSBpbiB0aGUgUEFDLUJheWVzIGJvdW5kLCBnaXZpbmcgYSB0aGVvcmV0aWNhbCBndWFyYW50ZWUgb2YgYmV0dGVyIGdlbmVyYWxpemF0aW9uLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IFRlbnNvckRhdGFzZXQsIERhdGFMb2FkZXJcblxuY2xhc3MgU0FNKG9wdGltLk9wdGltaXplcik6XG4gICAgXCJcIlwiU2hhcnBuZXNzLUF3YXJlIE1pbmltaXphdGlvbiBvcHRpbWl6ZXIgKEZvcmV0IGV0IGFsLiAyMDIxKS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgcGFyYW1zLCBiYXNlX29wdGltaXplciwgcmhvPTAuMDUsICoqa3dhcmdzKTpcbiAgICAgICAgZGVmYXVsdHMgPSBkaWN0KHJobz1yaG8sICoqa3dhcmdzKVxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHBhcmFtcywgZGVmYXVsdHMpXG4gICAgICAgIHNlbGYuYmFzZV9vcHRpbWl6ZXIgPSBiYXNlX29wdGltaXplcihzZWxmLnBhcmFtX2dyb3VwcywgKiprd2FyZ3MpXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIGZpcnN0X3N0ZXAoc2VsZiwgemVyb19ncmFkPUZhbHNlKTpcbiAgICAgICAgXCJcIlwiUGVydHVyYiB3ZWlnaHRzOiB3zIMgPSB3ICsgcmhvICogZ3JhZC98fGdyYWR8fC5cIlwiXCJcbiAgICAgICAgZ3JhZF9ub3JtID0gdG9yY2guc3RhY2soW3AuZ3JhZC5ub3JtKClcbiAgICAgICAgICAgIGZvciBncm91cCBpbiBzZWxmLnBhcmFtX2dyb3Vwc1xuICAgICAgICAgICAgZm9yIHAgaW4gZ3JvdXBbJ3BhcmFtcyddIGlmIHAuZ3JhZCBpcyBub3QgTm9uZV0pLm5vcm0oKVxuICAgICAgICBmb3IgZ3JvdXAgaW4gc2VsZi5wYXJhbV9ncm91cHM6XG4gICAgICAgICAgICBzY2FsZSA9IGdyb3VwWydyaG8nXSAvIChncmFkX25vcm0gKyAxZS0xMilcbiAgICAgICAgICAgIGZvciBwIGluIGdyb3VwWydwYXJhbXMnXTpcbiAgICAgICAgICAgICAgICBpZiBwLmdyYWQgaXMgTm9uZTogY29udGludWVcbiAgICAgICAgICAgICAgICBlX3cgPSBwLmdyYWQgKiBzY2FsZVxuICAgICAgICAgICAgICAgIHAuYWRkXyhlX3cpXG4gICAgICAgICAgICAgICAgc2VsZi5zdGF0ZVtwXVsnZV93J10gPSBlX3dcbiAgICAgICAgaWYgemVyb19ncmFkOiBzZWxmLnplcm9fZ3JhZCgpXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIHNlY29uZF9zdGVwKHNlbGYsIHplcm9fZ3JhZD1GYWxzZSk6XG4gICAgICAgIFwiXCJcIlJlc3RvcmUgd2VpZ2h0cyBhbmQgYXBwbHkgdXBkYXRlIHVzaW5nIHBlcnR1cmJlZCBncmFkaWVudC5cIlwiXCJcbiAgICAgICAgZm9yIGdyb3VwIGluIHNlbGYucGFyYW1fZ3JvdXBzOlxuICAgICAgICAgICAgZm9yIHAgaW4gZ3JvdXBbJ3BhcmFtcyddOlxuICAgICAgICAgICAgICAgIGlmIHAuZ3JhZCBpcyBOb25lOiBjb250aW51ZVxuICAgICAgICAgICAgICAgIHAuc3ViXyhzZWxmLnN0YXRlW3BdWydlX3cnXSkgICMgcmVzdG9yZVxuICAgICAgICBzZWxmLmJhc2Vfb3B0aW1pemVyLnN0ZXAoKVxuICAgICAgICBpZiB6ZXJvX2dyYWQ6IHNlbGYuemVyb19ncmFkKClcblxudG9yY2gubWFudWFsX3NlZWQoMSlcbnByaW50KFwiU0FNIG9wdGltaXplciBpbXBsZW1lbnRlZCDigJQgcmVhZHkgZm9yIHRyYWluaW5nIGxvb3BcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJXaHkgU0dEIEZpbmRzIEZsYXQgTWluaW1hIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU0dEIHdpdGggbGVhcm5pbmcgcmF0ZSDOtyBhbmQgYmF0Y2ggc2l6ZSBCIGdlbmVyYXRlcyBncmFkaWVudCBub2lzZSB3aG9zZSBjb3ZhcmlhbmNlIGlzIHByb3BvcnRpb25hbCB0byDOt0MvQiwgd2hlcmUgQyBpcyB0aGUgZW1waXJpY2FsIGdyYWRpZW50IGNvdmFyaWFuY2UgKEZpc2hlciBpbmZvcm1hdGlvbiBtYXRyaXgpLiBUaGlzIG5vaXNlIGFjdHMgYXMgYW4gaW1wbGljaXQgcmVndWxhcml6ZXI6IHRoZSBzdGF0aW9uYXJ5IGRpc3RyaWJ1dGlvbiBvZiBTR0QncyBzdG9jaGFzdGljIHByb2Nlc3MgaXMgbm90IHRoZSBtaW5pbWl6ZXIgb2YgTCjOuCkgaXRzZWxmLCBidXQgb2YgYSBwZW5hbGl6ZWQgb2JqZWN0aXZlIEwozrgpICsgKM63LzRCKcK3dHIoSCjOuCkpLiBUaGUgcGVuYWx0eSB0ZXJtIHRyKEgpIGlzIHRoZSBIZXNzaWFuIHRyYWNlIOKAlCBwcmVjaXNlbHkgdGhlIGF2ZXJhZ2Ugc2hhcnBuZXNzIG1lYXN1cmUuIFRoZXJlZm9yZTogc21hbGxlciBiYXRjaCBzaXplIEIg4oaSIGxhcmdlciBwZW5hbHR5IGNvZWZmaWNpZW50IOKGkiBzdHJvbmdlciBwcmVmZXJlbmNlIGZvciBmbGF0IG1pbmltYS4gVGhpcyBwcmVkaWN0aW9uIG1hdGNoZXMgZW1waXJpY2FsIG9ic2VydmF0aW9ucyBwcmVjaXNlbHk6IGxhcmdlLWJhdGNoIFNHRCBmaW5kcyBzaGFycGVyIG1pbmltYSAoS2Vza2FyIGV0IGFsLiAyMDE3KSwgZ2VuZXJhbGl6ZXMgd29yc2UgYXQgdGhlIHNhbWUgdHJhaW5pbmcgbG9zcywgYW5kIHJlcXVpcmVzIGxlYXJuaW5nIHJhdGUgc2NhbGluZyBvciBTQU0gdG8gY29tcGVuc2F0ZS4gVGhlIGltcGxpY2F0aW9uIGZvciBwcmFjdGl0aW9uZXJzIGlzIHRoYXQgdGhlIGJhdGNoIHNpemUgYW5kIGxlYXJuaW5nIHJhdGUgam9pbnRseSBjb250cm9sIGFuIGltcGxpY2l0IHJlZ3VsYXJpemF0aW9uIHN0cmVuZ3RoIOKAlCB0aGUgJ2xpbmVhciBzY2FsaW5nIHJ1bGUnIChMUiDiiJ0gQikgYXR0ZW1wdHMgdG8ga2VlcCB0aGlzIGltcGxpY2l0IHJlZ3VsYXJpemF0aW9uIGNvbnN0YW50LCBidXQgaXQgb25seSBob2xkcyBhcHByb3hpbWF0ZWx5IGluIHRoZSBsaW5lYXIgcmVnaW1lIGFuZCBicmVha3MgZm9yIHZlcnkgbGFyZ2UgYmF0Y2ggc2l6ZXMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiU0FNIE9wdGltaXplcjogU2hhcnBuZXNzLUF3YXJlIE1pbmltaXphdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlNBTSAoRm9yZXQgZXQgYWwuIDIwMjEpIGltcGxlbWVudHMgdHdvLXN0ZXAgdXBkYXRlcyB0aGF0IGV4cGxpY2l0bHkgbWluaW1pemUgd29yc3QtY2FzZSBwZXJ0dXJiYXRpb24gbG9zcy4gU3RlcCAxIChwZXJ0dXJiYXRpb24pOiBjb21wdXRlIM61zIIgPSDPgcK34oiHTCjOuCkv4oCW4oiHTCjOuCnigJYgYW5kIHNldCB3zIMgPSDOuCArIM61zIIgKHBlcnR1cmIgd2VpZ2h0cyBpbiB0aGUgZ3JhZGllbnQgZGlyZWN0aW9uIGJ5IM+BLCB0eXBpY2FsbHkgMC4wNSkuIFN0ZXAgMiAodXBkYXRlKTogY29tcHV0ZSBncmFkaWVudCBhdCB0aGUgcGVydHVyYmVkIHBvaW50IOKIh0wod8yDKSwgdGhlbiB1cGRhdGUgZnJvbSB0aGUgT1JJR0lOQUwgzrg6IM64IOKGkCDOuCDiiJIgzrfCt+KIh0wod8yDKS4gVGhpcyBjb3N0cyB0d2ljZSB0aGUgY29tcHV0ZSBvZiBTR0QgKHR3byBmb3J3YXJkLWJhY2t3YXJkIHBhc3NlcyBwZXIgc3RlcCkgYnV0IHRhcmdldHMgdGhlIGZsYXQtbWluaW1hIG9iamVjdGl2ZSBkaXJlY3RseS4gQVNBTSAoQWRhcHRpdmUgU0FNKSBzY2FsZXMgdGhlIHBlcnR1cmJhdGlvbiBwZXIgcGFyYW1ldGVyOiDOtcyCID0gz4HCt3zOuHzCt+KIh0wv4oCWfM64fMK34oiHTOKAliwgbWFraW5nIHRoZSBwZXJ0dXJiYXRpb24gc2NhbGUtaW52YXJpYW50IGFuZCBtb3JlIGVmZmVjdGl2ZSBmb3IgcGFyYW1ldGVycyB3aXRoIGRpZmZlcmVudCBtYWduaXR1ZGVzLiBQcmFjdGljYWwgdmFyaWFudHM6IEdTQU0gKGdyYWRpZW50IG1hZ25pdHVkZS1iYXNlZCBTQU0pLCBtU0FNIChtaW5pLWJhdGNoIFNBTSB3aXRoIGdyYWRpZW50IGFjY3VtdWxhdGlvbiwgaGFsdmluZyBjb21wdXRlIG92ZXJoZWFkKSwgU0FNIHdpdGggRU1BLiBPbiBJbWFnZU5ldCB3aXRoIFJlc05ldC01MCwgU0FNIGltcHJvdmVzIHRvcC0xIGFjY3VyYWN5IGJ5IDAuNS0xLjUlIGRlcGVuZGluZyBvbiBkYXRhIGF1Z21lbnRhdGlvbjsgb24gQ0lGQVItMTAwLCBpbXByb3ZlbWVudHMgb2YgMS0zJSBhcmUgY29tbW9uLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IFRlbnNvckRhdGFzZXQsIERhdGFMb2FkZXJcblxuZGVmIHNhbV90cmFpbmluZ19zdGVwKG1vZGVsLCBzYW1fb3B0aW1pemVyLCBkYXRhLCB0YXJnZXQsIGxvc3NfZm4pOlxuICAgIFwiXCJcIkNvbXBsZXRlIFNBTSB0d28tc3RlcCB1cGRhdGUuXCJcIlwiXG4gICAgIyBGaXJzdCBmb3J3YXJkLWJhY2t3YXJkOiBjb21wdXRlIGdyYWRpZW50IGF0IGN1cnJlbnQgd2VpZ2h0c1xuICAgIHNhbV9vcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBvdXRwdXQgPSBtb2RlbChkYXRhKVxuICAgIGxvc3MgPSBsb3NzX2ZuKG91dHB1dCwgdGFyZ2V0KVxuICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICMgRmlyc3Qgc3RlcDogcGVydHVyYiB3ZWlnaHRzXG4gICAgc2FtX29wdGltaXplci5maXJzdF9zdGVwKHplcm9fZ3JhZD1UcnVlKVxuICAgICMgU2Vjb25kIGZvcndhcmQtYmFja3dhcmQ6IGNvbXB1dGUgZ3JhZGllbnQgYXQgcGVydHVyYmVkIHdlaWdodHNcbiAgICBsb3NzX2ZuKG1vZGVsKGRhdGEpLCB0YXJnZXQpLmJhY2t3YXJkKClcbiAgICAjIFNlY29uZCBzdGVwOiByZXN0b3JlIHdlaWdodHMsIGFwcGx5IHVwZGF0ZVxuICAgIHNhbV9vcHRpbWl6ZXIuc2Vjb25kX3N0ZXAoemVyb19ncmFkPVRydWUpXG4gICAgcmV0dXJuIGxvc3MuaXRlbSgpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuWCA9IHRvcmNoLnJhbmRuKDIwMCwgOClcbnkgPSAoWFs6LCAwXSArIFhbOiwgMV0gPiAwKS5sb25nKClcbmRhdGFzZXQgPSBUZW5zb3JEYXRhc2V0KFgsIHkpXG5sb2FkZXIgPSBEYXRhTG9hZGVyKGRhdGFzZXQsIGJhdGNoX3NpemU9MzIsIHNodWZmbGU9VHJ1ZSlcbm1vZGVsID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoOCwgMTYpLCBubi5SZUxVKCksIG5uLkxpbmVhcigxNiwgMikpXG5iYXNlX29wdCA9IG9wdGltLlNHRFxuc2FtX29wdCA9IFNBTShtb2RlbC5wYXJhbWV0ZXJzKCksIGJhc2Vfb3B0LCBscj0wLjAxLCBtb21lbnR1bT0wLjksIHJobz0wLjA1KVxubG9zc19mbiA9IG5uLkNyb3NzRW50cm9weUxvc3MoKVxuZm9yIGVwb2NoIGluIHJhbmdlKDMpOlxuICAgIHRvdGFsID0gc3VtKHNhbV90cmFpbmluZ19zdGVwKG1vZGVsLCBzYW1fb3B0LCB4YiwgeWIsIGxvc3NfZm4pXG4gICAgICAgICAgICAgICAgZm9yIHhiLCB5YiBpbiBsb2FkZXIpXG4gICAgcHJpbnQoZlwiRXBvY2gge2Vwb2NoKzF9OiBhdmcgbG9zcyB7dG90YWwvbGVuKGxvYWRlcik6LjRmfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk1MIENvbm5lY3Rpb25zOiBCYXRjaCBTaXplLCBMUiwgYW5kIEZsYXRuZXNzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIGZsYXQgbWluaW1hIGNvbm5lY3Rpb24gdW5pZmllcyBzZXZlcmFsIGVtcGlyaWNhbCBvYnNlcnZhdGlvbnMgdGhhdCBwcmV2aW91c2x5IHNlZW1lZCB1bnJlbGF0ZWQuIEZpcnN0LCBsYXJnZS1iYXRjaCB0cmFpbmluZyBmaW5kcyBzaGFycGVyIG1pbmltYSBiZWNhdXNlIHRoZSBub2lzZSBjb3ZhcmlhbmNlIM63wrdDL0IgaXMgc21hbGxlciBhdCBsYXJnZSBCLCB3ZWFrZW5pbmcgdGhlIGltcGxpY2l0IGZsYXQtbWluaW1hIHJlZ3VsYXJpemF0aW9uIOKAlCB0aGlzIGlzIHdoeSBuYWl2ZSBsYXJnZS1iYXRjaCB0cmFpbmluZyBnZW5lcmFsaXplcyB3b3JzZSBhbmQgd2h5IFNBTSBpcyBlc3BlY2lhbGx5IGVmZmVjdGl2ZSB3aGVuIGNvbWJpbmVkIHdpdGggbGFyZ2UgYmF0Y2hlcy4gU2Vjb25kLCBhIGhpZ2hlciBsZWFybmluZyByYXRlIM63IGluY3JlYXNlcyBub2lzZSwgYmlhc2luZyB0b3dhcmQgZmxhdHRlciBtaW5pbWEgd2l0aGluIHRoZSBzdGFibGUgdHJhaW5pbmcgcmFuZ2Ug4oCUIHRoaXMgaXMgd2h5IHRoZSAnbGluZWFyIHNjYWxpbmcgcnVsZScgKGRvdWJsZSBMUiB3aGVuIGRvdWJsaW5nIGJhdGNoIHNpemUpIGFwcHJveGltYXRlbHkgcHJlc2VydmVzIGdlbmVyYWxpemF0aW9uLiBUaGlyZCwgZHJvcG91dCBpcyBhbm90aGVyIG5vaXNlIHNvdXJjZSB0aGF0IGltcGxpY2l0bHkgZW5jb3VyYWdlcyBmbGF0IG1pbmltYSBieSBtYWtpbmcgdGhlIG1vZGVsIHJvYnVzdCB0byByYW5kb20gdW5pdCBkZWFjdGl2YXRpb24sIGFuYWxvZ291cyB0byB3ZWlnaHQgcGVydHVyYmF0aW9uLiBGb3VydGgsIG1vZGVsIHNvdXBzIChXb3J0c21hbiBldCBhbC4gMjAyMikgYW5kIFNXQSB3b3JrIGJlY2F1c2UgYXZlcmFnaW5nIG11bHRpcGxlIGNoZWNrcG9pbnRzIG1vdmVzIHRoZSBlZmZlY3RpdmUgd2VpZ2h0cyB0b3dhcmQgdGhlIGdlb21ldHJpYyBjZW50ZXIgb2YgYSBmbGF0IHZhbGxleSwgZ2l2aW5nIGJldHRlciBjYWxpYnJhdGlvbiBhbmQgZ2VuZXJhbGl6YXRpb24gdGhhbiBhbnkgc2luZ2xlIGNoZWNrcG9pbnQuIEZpZnRoLCBpbiBzZWxmLXN1cGVydmlzZWQgbGVhcm5pbmcsIHRoZSBtb21lbnR1bSBlbmNvZGVyIGluIEJZT0wvRElOTyB0cmFja3MgYW4gZXhwb25lbnRpYWwgbW92aW5nIGF2ZXJhZ2Ugb2YgdGhlIG9ubGluZSBlbmNvZGVyLCB3aGljaCBpbXBsaWNpdGx5IHNhbXBsZXMgZnJvbSBhIGZsYXQgcmVnaW9uIG9mIHdlaWdodCBzcGFjZSBhbmQgcHJvdmlkZXMgbW9yZSBzdGFibGUgdGFyZ2V0cyBmb3IgcmVwcmVzZW50YXRpb24gbGVhcm5pbmcuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuZnJvbSB0b3JjaC51dGlscy5kYXRhIGltcG9ydCBUZW5zb3JEYXRhc2V0LCBEYXRhTG9hZGVyXG5cbmRlZiBtYWtlX2RhdGEobj0zMDAsIHNlZWQ9MCk6XG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICBYID0gdG9yY2gucmFuZG4obiwgNilcbiAgICB5ID0gKFhbOiwgMF0gLSBYWzosIDFdICsgMC41ICogWFs6LCAyXSA+IDApLmxvbmcoKVxuICAgIHJldHVybiBYLCB5XG5cbmRlZiB0cmFpbl9tb2RlbChYLCB5LCBiYXRjaF9zaXplLCBsciwgdXNlX3NhbT1GYWxzZSwgZXBvY2hzPTIwKTpcbiAgICBtb2RlbCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDYsIDEyKSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoMTIsIDIpKVxuICAgIGxvYWRlciA9IERhdGFMb2FkZXIoVGVuc29yRGF0YXNldChYWzoyNDBdLCB5WzoyNDBdKSwgYmF0Y2hfc2l6ZT1iYXRjaF9zaXplKVxuICAgIGlmIHVzZV9zYW06XG4gICAgICAgIG9wdCA9IFNBTShtb2RlbC5wYXJhbWV0ZXJzKCksIG9wdGltLlNHRCwgbHI9bHIsIHJobz0wLjA1KVxuICAgIGVsc2U6XG4gICAgICAgIG9wdCA9IG9wdGltLlNHRChtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPWxyKVxuICAgIGxvc3NfZm4gPSBubi5Dcm9zc0VudHJvcHlMb3NzKClcbiAgICBmb3IgXyBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICBmb3IgeGIsIHliIGluIGxvYWRlcjpcbiAgICAgICAgICAgIGlmIHVzZV9zYW06XG4gICAgICAgICAgICAgICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgICAgICAgICAgICAgbG9zc19mbihtb2RlbCh4YiksIHliKS5iYWNrd2FyZCgpXG4gICAgICAgICAgICAgICAgb3B0LmZpcnN0X3N0ZXAoemVyb19ncmFkPVRydWUpXG4gICAgICAgICAgICAgICAgbG9zc19mbihtb2RlbCh4YiksIHliKS5iYWNrd2FyZCgpXG4gICAgICAgICAgICAgICAgb3B0LnNlY29uZF9zdGVwKHplcm9fZ3JhZD1UcnVlKVxuICAgICAgICAgICAgZWxzZTpcbiAgICAgICAgICAgICAgICBvcHQuemVyb19ncmFkKClcbiAgICAgICAgICAgICAgICBsb3NzX2ZuKG1vZGVsKHhiKSwgeWIpLmJhY2t3YXJkKClcbiAgICAgICAgICAgICAgICBvcHQuc3RlcCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHByZWRzID0gbW9kZWwoWFsyNDA6XSkuYXJnbWF4KDEpXG4gICAgICAgIHJldHVybiAocHJlZHMgPT0geVsyNDA6XSkuZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG5cblgsIHkgPSBtYWtlX2RhdGEoKVxucHJpbnQoZlwiU0dEIHNtYWxsIGJhdGNoIChCPTE2KTogIHRlc3QgYWNjID0ge3RyYWluX21vZGVsKFgsIHksIDE2LCAwLjA1KTouM2Z9XCIpXG5wcmludChmXCJTR0QgbGFyZ2UgYmF0Y2ggKEI9MTI4KTogdGVzdCBhY2MgPSB7dHJhaW5fbW9kZWwoWCwgeSwgMTI4LCAwLjA1KTouM2Z9XCIpXG5wcmludChmXCJTQU0gbGFyZ2UgYmF0Y2ggKEI9MTI4KTogdGVzdCBhY2MgPSB7dHJhaW5fbW9kZWwoWCwgeSwgMTI4LCAwLjA1LCB1c2Vfc2FtPVRydWUpOi4zZn1cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJJbXBsZW1lbnRhdGlvbiBQaXRmYWxscyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZvdXIgcGl0ZmFsbHMgd2hlbiBpbXBsZW1lbnRpbmcgU0FNIGFuZCBmbGF0LW1pbmltYSB0ZWNobmlxdWVzLiBGaXJzdCwgZm9yZ2V0dGluZyB0byByZXN0b3JlIHdlaWdodHMgYWZ0ZXIgdGhlIGZpcnN0IHN0ZXA6IGlmIHRoZSBtb2RlbCBwYXJhbWV0ZXJzIGFyZSBub3QgcmVzdG9yZWQgYmVmb3JlIHRoZSBzZWNvbmQgZ3JhZGllbnQgY29tcHV0YXRpb24sIHRoZSBzZWNvbmQgZ3JhZGllbnQgaXMgY29tcHV0ZWQgYXQgdGhlIHBlcnR1cmJlZCBwb2ludCBidXQgdGhlIHVwZGF0ZSBpcyBhbHNvIGFwcGxpZWQgYXQgdGhlIHBlcnR1cmJlZCBwb2ludCDigJQgbG9zaW5nIHRoZSBmbGF0LW1pbmltYSBvYmplY3RpdmUgZW50aXJlbHkuIEFsd2F5cyBzYXZlIGFuZCByZXN0b3JlIG9yaWdpbmFsIHBhcmFtZXRlcnMuIFNlY29uZCwgdXNpbmcgU0FNIHdpdGggZ3JhZGllbnQgYWNjdW11bGF0aW9uIHdpdGhvdXQgcmVkdWNpbmcgcGVyLXN0ZXAgbG9zcyBieSB0aGUgYWNjdW11bGF0aW9uIGZhY3RvcjogYWNjdW11bGF0aW9uIGluZmxhdGVzIGdyYWRpZW50IG5vcm1zLCBtYWtpbmcgdGhlIHBlcnR1cmJhdGlvbiByYWRpdXMgZWZmZWN0aXZlbHkgbGFyZ2VyIHRoYW4gaW50ZW5kZWQuIFRoaXJkLCBtb25pdG9yaW5nIG9ubHkgdHJhaW5pbmcgbG9zczogU0FNIHNvbWV0aW1lcyBjYXVzZXMgdHJhaW5pbmcgbG9zcyB0byBwbGF0ZWF1IHdoaWxlIHRlc3QgbG9zcyBjb250aW51ZXMgdG8gaW1wcm92ZSDigJQgdGhpcyBpcyBhIGZlYXR1cmUsIG5vdCBhIGJ1ZywgYnV0IGNhbiBiZSBtaXNpbnRlcnByZXRlZCBhcyBsYWNrIG9mIHByb2dyZXNzLiBGb3VydGgsIHVzaW5nIFNBTSB3aGVuIHRoZSBnZW5lcmFsaXphdGlvbiBnYXAgaXMgc21hbGw6IGlmIHRyYWluIGFuZCB0ZXN0IGFjY3VyYWN5IGFyZSBhbHJlYWR5IHdpdGhpbiAxJSwgU0FNIGFkZHMgY29tcHV0ZSBvdmVyaGVhZCB3aXRob3V0IG1lYW5pbmdmdWwgYmVuZWZpdC4gUHJvZmlsZSB0aGUgZ2VuZXJhbGl6YXRpb24gZ2FwIGJlZm9yZSBhZGRpbmcgU0FNLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlByYWN0aWNhbCBHdWlkYW5jZSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlByYWN0aWNhbCBndWlkZWxpbmVzIGZvciBhcHBseWluZyBmbGF0LW1pbmltYSBpbnNpZ2h0cy4gQ2hvb3NlIGJhdGNoIHNpemUgYW5kIGxlYXJuaW5nIHJhdGUgdG9nZXRoZXI6IHVzZSB0aGUgbGFyZ2VzdCBiYXRjaCBzaXplIHRoYXQgZml0cyBpbiBtZW1vcnksIHRoZW4gc2NhbGUgTFIgcHJvcG9ydGlvbmFsbHkgKGxpbmVhciBzY2FsaW5nIHJ1bGU6IExSID0gYmFzZV9MUiDDlyBCLzI1NiksIGFuZCBhZGQgU0FNIGlmIHRoZSBnZW5lcmFsaXphdGlvbiBnYXAgaXMgc3RpbGwgbGFyZ2VyIHRoYW4gZXhwZWN0ZWQuIEZvciBtb25pdG9yaW5nIHNoYXJwbmVzcyBjaGVhcGx5OiBsb2cgdGhlIGdyYWRpZW50IG5vcm0gYWZ0ZXIgYmFja3dhcmQoKSBiZWZvcmUgY2xpcHBpbmcg4oCUIGdyYWRpZW50IG5vcm0gYXQgY3JpdGljYWwgcG9pbnRzIGNvcnJlbGF0ZXMgd2l0aCBzaGFycG5lc3MgKGhpZ2hlciBncmFkaWVudCBub3JtIOKGkiBzaGFycGVyIGN1cnZhdHVyZSBhbG9uZyB0aGUgdHJhamVjdG9yeSkuIFVzZSBTV0EgYXMgYSBmcmVlIGltcHJvdmVtZW50OiBhZnRlciB0aGUgbWFpbiB0cmFpbmluZyBzY2hlZHVsZSwgcnVuIDEwLTIwIG1vcmUgZXBvY2hzIHdpdGggYSBjeWNsaWMgTFIgc2NoZWR1bGUgKFNXQS1zdHlsZSkgYW5kIGF2ZXJhZ2UgdGhlIGNoZWNrcG9pbnRzOyB0aGlzIHR5cGljYWxseSBnYWlucyAwLjMtMC41JSBhY2N1cmFjeSB3aXRoIG5vIGFyY2hpdGVjdHVyZSBjaGFuZ2VzLiBGb3IgZmluZS10dW5pbmcgcHJlLXRyYWluZWQgbW9kZWxzLCBzdGFydCB3aXRoIGxvd2VyIM+BIChlLmcuLCAwLjAxIGluc3RlYWQgb2YgMC4wNSkgaW4gU0FNIHRvIGF2b2lkIGRpc3J1cHRpbmcgdGhlIHByZS10cmFpbmVkIGZlYXR1cmVzLCBhbmQgaW5jcmVhc2Ugz4Egb25seSBpZiB0aGUgZ2VuZXJhbGl6YXRpb24gZ2FwIHdhcnJhbnRzIGl0LiJ9LCB7InR5cGUiOiAiY2FsbG91dCIsICJ0aXRsZSI6ICJXYXJuaW5nIiwgImNvbnRlbnQiOiAiU0FNIGRvdWJsZXMgY29tcHV0ZSBjb3N0IOKAlCBvbmx5IHVzZSBpdCB3aGVuIHRoZSBnZW5lcmFsaXphdGlvbiBnYXAgKHRyYWluIGFjY3VyYWN5IG1pbnVzIHRlc3QgYWNjdXJhY3kpIGV4Y2VlZHMgMiUuIE1vbml0b3IgdHJhaW4gYW5kIHRlc3QgbG9zcyBzZXBhcmF0ZWx5IHRocm91Z2hvdXQgU0FNIHRyYWluaW5nOiBpZiBib3RoIGRlY3JlYXNlIHRvZ2V0aGVyLCBTQU0gaXMgd29ya2luZyBhcyBleHBlY3RlZC4gSWYgdHJhaW4gbG9zcyBzdG9wcyBkZWNyZWFzaW5nIGJ1dCB0ZXN0IGxvc3Mga2VlcHMgaW1wcm92aW5nLCB0aGUgbW9kZWwgaGFzIGZvdW5kIGEgZmxhdCBtaW5pbXVtIGFuZCB5b3UgbWF5IHNhZmVseSByZWR1Y2Ugz4EgdG8gYWNjZWxlcmF0ZSBjb252ZXJnZW5jZS4gTmV2ZXIgdXNlIFNBTSBhcyBhIHN1YnN0aXR1dGUgZm9yIHByb3BlciByZWd1bGFyaXphdGlvbiAod2VpZ2h0IGRlY2F5LCBkcm9wb3V0LCBkYXRhIGF1Z21lbnRhdGlvbikg4oCUIHRob3NlIHNob3VsZCBiZSBpbiBwbGFjZSBmaXJzdC4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIk9wdGltaXplciIsICJTaGFycG5lc3MiLCAiR2VuZXJhbGl6YXRpb24iLCAiQ29tcHV0ZSBPdmVyaGVhZCIsICJNZW1vcnkgT3ZlcmhlYWQiXSwgInJvd3MiOiBbWyJTR0Qgc21hbGwgYmF0Y2ggKELiiaQzMikiLCAiTG93IChmbGF0KSIsICJCZXN0IiwgIjHDlyIsICIxw5ciXSwgWyJTR0QgbGFyZ2UgYmF0Y2ggKELiiaU1MTIpIiwgIkhpZ2ggKHNoYXJwKSIsICJXb3JzZSBhdCBzYW1lIExSIiwgIjHDlyAoZmFzdCBzdGVwcykiLCAiMcOXIl0sIFsiQWRhbSIsICJNZWRpdW0taGlnaCIsICJHb29kIChhZGFwdGl2ZSBMUikiLCAiMS4zw5cgKG1vbWVudCBidWZmZXJzKSIsICIyw5cgKG0sIHYgYnVmZmVycykiXSwgWyJTQU0gKyBTR0QiLCAiTG93IChleHBsaWNpdCkiLCAiQmVzdCBpbiBjbGFzcyIsICIyw5cgKHR3byBwYXNzZXMpIiwgIjHDlyArIGVfdyBidWZmZXIiXSwgWyJTV0EiLCAiTG93IChjZW50ZXIgb2YgdmFsbGV5KSIsICJWZXJ5IGdvb2QiLCAiMcOXICsgYXZlcmFnaW5nIHN0ZXAiLCAiMsOXIChtb2RlbCArIFNXQSBtb2RlbCkiXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAiaXRlbXMiOiBbIlNoYXJwbmVzcyBpcyBtZWFzdXJlZCBieSDOu19tYXggKGxhcmdlc3QgSGVzc2lhbiBlaWdlbnZhbHVlLCB3b3JzdC1jYXNlIGN1cnZhdHVyZSkgb3IgdHIoSCkgKGF2ZXJhZ2UgY3VydmF0dXJlLCBjaGVhcGVyIHZpYSBIdXRjaGluc29uJ3MgZXN0aW1hdG9yKS4iLCAiUEFDLUJheWVzIHRoZW9yZW0gZm9ybWFsaXplcyB3aHkgZmxhdCBtaW5pbWEgZ2VuZXJhbGl6ZSBiZXR0ZXI6IHRoZSBnZW5lcmFsaXphdGlvbiBib3VuZCBpcyBjb250cm9sbGVkIGJ5IEtMKFF8fFApLCB3aGljaCBpcyBzbWFsbGVyIHdoZW4gdGhlIG1vZGVsIGlzIHJvYnVzdCB0byB3ZWlnaHQgcGVydHVyYmF0aW9ucy4iLCAiU0FNIG1pbmltaXplcyBtYXhfe+KAls614oCW4omkz4F9IEwozrgrzrUpOiBwZXJ0dXJiIHdlaWdodHMgaW4gZ3JhZGllbnQgZGlyZWN0aW9uLCBjb21wdXRlIGdyYWRpZW50IGF0IHBlcnR1cmJlZCBwb2ludCwgdXBkYXRlIGZyb20gb3JpZ2luYWwgd2VpZ2h0cyDigJQgZXhwbGljaXRseSB0YXJnZXRpbmcgdGhlIFBBQy1CYXllcyBib3VuZC4iLCAiU0dEIGltcGxpY2l0bHkgYmlhc2VzIHRvd2FyZCBmbGF0IG1pbmltYSB2aWEgZ3JhZGllbnQgbm9pc2Ugd2l0aCBzY2FsZSDOty9COyBsYXJnZSBiYXRjaCBzaXplIHdlYWtlbnMgdGhpcyBiaWFzLCBleHBsYWluaW5nIHRoZSBnZW5lcmFsaXphdGlvbiBnYXAgb2YgbGFyZ2UtYmF0Y2ggdHJhaW5pbmcuIiwgIlNXQSAoU3RvY2hhc3RpYyBXZWlnaHQgQXZlcmFnaW5nKSBwbGFjZXMgdGhlIG1vZGVsIGF0IHRoZSBmbGF0IGdlb21ldHJpYyBjZW50ZXIgb2YgYSBsb3NzIHZhbGxleSBieSBhdmVyYWdpbmcgbGF0ZS10cmFpbmluZyBjaGVja3BvaW50cyDigJQgZnJlZSAwLjMtMC41JSBpbXByb3ZlbWVudC4iLCAiVXNlIFNBTSBvbmx5IHdoZW4gdGhlIGdlbmVyYWxpemF0aW9uIGdhcCBleGNlZWRzIDIlOyBwcm9maWxlIHRyYWluL3Rlc3QgbG9zcyBzZXBhcmF0ZWx5IGFuZCByZWR1Y2Ugz4Egd2hlbiBib3RoIGxvc3NlcyBhbGlnbi4iLCAiVGhlIGxpbmVhciBzY2FsaW5nIHJ1bGUgKExSIOKInSBCKSBhcHByb3hpbWF0ZWx5IHByZXNlcnZlcyB0aGUgaW1wbGljaXQgZmxhdC1taW5pbWEgcmVndWxhcml6YXRpb24gd2hlbiBzY2FsaW5nIGJhdGNoIHNpemUsIGJ1dCBicmVha3MgYXQgdmVyeSBsYXJnZSBiYXRjaGVzIHdoZXJlIHRoZSBub2lzZSBpcyBubyBsb25nZXIgd2VsbC1tb2RlbGVkIGFzIEdhdXNzaWFuLiJdfV0="
---

# Sharp vs Flat Minima and Generalization

Not all minima of a neural network's training loss are created equal: some generalize well to held-out data, others memorize the training set. The geometry of the minimum — specifically its sharpness (curvature) — predicts this difference. A flat minimum is one where the loss changes slowly as weights move in any direction; a sharp minimum has directions of high curvature where small weight perturbations cause large loss spikes. This note builds from formal sharpness measures through the PAC-Bayes bound that explains why flat minima generalize better, to the SAM optimizer that explicitly targets flat minima, and the connection between SGD noise and implicit regularization toward flat regions.

## Measuring Sharpness

The largest Hessian eigenvalue λ_max measures sharpness in the worst-case direction: even one direction of high curvature makes a minimum sharp. The Hessian trace tr(H) = Σλᵢ measures average curvature over all directions — cheaper to estimate than λ_max (Hutchinson's estimator uses tr(H) ≈ Eᵥ[vᵀHv] with random ±1 vectors v). The sharpness ratio ρ_sharp = max_{‖δ‖≤ρ} [L(θ+δ) − L(θ)] asks: how much does loss increase if we perturb weights by at most ρ in any direction? Hochreiter and Schmidhuber (1997) gave a Minimum Description Length argument: a flat minimum can be encoded with lower weight precision (fewer bits) because small quantization errors leave the loss unchanged; fewer bits → shorter description → better generalization by MDL/Occam's razor. Practically: two models with the same training loss but different sharpness will have different test loss; the flatter model generalizes better by an amount predicted by the PAC-Bayes bound.

```python
import numpy as np
import torch
import torch.nn as nn
from torch.autograd.functional import hvp

def hutchinson_trace(model, loss_fn, X, y, n_samples=20):
    """Estimate Hessian trace via Hutchinson's method."""
    loss = loss_fn(model(X), y)
    params = [p for p in model.parameters() if p.requires_grad]
    grads = torch.autograd.grad(loss, params, create_graph=True)
    grad_vec = torch.cat([g.flatten() for g in grads])
    trace_est = 0.0
    for _ in range(n_samples):
        v = torch.randint(0, 2, grad_vec.shape).float() * 2 - 1
        Hv = torch.autograd.grad(grad_vec @ v.detach(), params,
                                  retain_graph=True)
        Hv_flat = torch.cat([h.flatten() for h in Hv])
        trace_est += (v * Hv_flat).sum().item()
    return trace_est / n_samples

torch.manual_seed(0)
X = torch.randn(64, 10)
y = torch.randn(64, 1)
model_sharp = nn.Sequential(nn.Linear(10, 4), nn.ReLU(), nn.Linear(4, 1))
model_flat = nn.Sequential(nn.Linear(10, 4), nn.ReLU(), nn.Linear(4, 1))
nn.init.normal_(list(model_sharp.parameters())[0], std=2.0)
loss_fn = nn.MSELoss()
trace_sharp = hutchinson_trace(model_sharp, loss_fn, X, y)
trace_flat = hutchinson_trace(model_flat, loss_fn, X, y)
print(f"Sharp model Hessian trace estimate: {trace_sharp:.2f}")
print(f"Flat model Hessian trace estimate:  {trace_flat:.2f}")
```

## PAC-Bayes Bound and Sharpness

PAC-Bayes theorem (McAllester 1999): for any prior P and posterior Q over hypotheses, with probability at least 1−δ over samples of size n: L_test(Q) ≤ L_train(Q) + sqrt((KL(Q||P) + log(1/δ)) / (2n)). Setting Q = N(θ*, σ²I) (Gaussian posterior around the solution) and P = N(0, σ²I) (standard prior), the KL divergence KL(Q||P) ≈ ‖θ*‖²/(2σ²). Foret et al. (2021) interpret the sharpness-aware objective as minimizing an upper bound from this theorem: maximizing σ (allowed perturbation radius) to keep the loss stable is equivalent to minimizing the maximum loss in a ball of radius ρ around θ*. The SAM objective max_{‖ε‖≤ρ} L(θ+ε) directly measures the worst-case perturbation loss, and minimizing it simultaneously pushes down training loss and the KL term in the PAC-Bayes bound, giving a theoretical guarantee of better generalization.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

class SAM(optim.Optimizer):
    """Sharpness-Aware Minimization optimizer (Foret et al. 2021)."""
    def __init__(self, params, base_optimizer, rho=0.05, **kwargs):
        defaults = dict(rho=rho, **kwargs)
        super().__init__(params, defaults)
        self.base_optimizer = base_optimizer(self.param_groups, **kwargs)

    @torch.no_grad()
    def first_step(self, zero_grad=False):
        """Perturb weights: w̃ = w + rho * grad/||grad||."""
        grad_norm = torch.stack([p.grad.norm()
            for group in self.param_groups
            for p in group['params'] if p.grad is not None]).norm()
        for group in self.param_groups:
            scale = group['rho'] / (grad_norm + 1e-12)
            for p in group['params']:
                if p.grad is None: continue
                e_w = p.grad * scale
                p.add_(e_w)
                self.state[p]['e_w'] = e_w
        if zero_grad: self.zero_grad()

    @torch.no_grad()
    def second_step(self, zero_grad=False):
        """Restore weights and apply update using perturbed gradient."""
        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None: continue
                p.sub_(self.state[p]['e_w'])  # restore
        self.base_optimizer.step()
        if zero_grad: self.zero_grad()

torch.manual_seed(1)
print("SAM optimizer implemented — ready for training loop")
```

## Why SGD Finds Flat Minima

SGD with learning rate η and batch size B generates gradient noise whose covariance is proportional to ηC/B, where C is the empirical gradient covariance (Fisher information matrix). This noise acts as an implicit regularizer: the stationary distribution of SGD's stochastic process is not the minimizer of L(θ) itself, but of a penalized objective L(θ) + (η/4B)·tr(H(θ)). The penalty term tr(H) is the Hessian trace — precisely the average sharpness measure. Therefore: smaller batch size B → larger penalty coefficient → stronger preference for flat minima. This prediction matches empirical observations precisely: large-batch SGD finds sharper minima (Keskar et al. 2017), generalizes worse at the same training loss, and requires learning rate scaling or SAM to compensate. The implication for practitioners is that the batch size and learning rate jointly control an implicit regularization strength — the 'linear scaling rule' (LR ∝ B) attempts to keep this implicit regularization constant, but it only holds approximately in the linear regime and breaks for very large batch sizes.

## SAM Optimizer: Sharpness-Aware Minimization

SAM (Foret et al. 2021) implements two-step updates that explicitly minimize worst-case perturbation loss. Step 1 (perturbation): compute ε̂ = ρ·∇L(θ)/‖∇L(θ)‖ and set w̃ = θ + ε̂ (perturb weights in the gradient direction by ρ, typically 0.05). Step 2 (update): compute gradient at the perturbed point ∇L(w̃), then update from the ORIGINAL θ: θ ← θ − η·∇L(w̃). This costs twice the compute of SGD (two forward-backward passes per step) but targets the flat-minima objective directly. ASAM (Adaptive SAM) scales the perturbation per parameter: ε̂ = ρ·|θ|·∇L/‖|θ|·∇L‖, making the perturbation scale-invariant and more effective for parameters with different magnitudes. Practical variants: GSAM (gradient magnitude-based SAM), mSAM (mini-batch SAM with gradient accumulation, halving compute overhead), SAM with EMA. On ImageNet with ResNet-50, SAM improves top-1 accuracy by 0.5-1.5% depending on data augmentation; on CIFAR-100, improvements of 1-3% are common.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

def sam_training_step(model, sam_optimizer, data, target, loss_fn):
    """Complete SAM two-step update."""
    # First forward-backward: compute gradient at current weights
    sam_optimizer.zero_grad()
    output = model(data)
    loss = loss_fn(output, target)
    loss.backward()
    # First step: perturb weights
    sam_optimizer.first_step(zero_grad=True)
    # Second forward-backward: compute gradient at perturbed weights
    loss_fn(model(data), target).backward()
    # Second step: restore weights, apply update
    sam_optimizer.second_step(zero_grad=True)
    return loss.item()

torch.manual_seed(42)
X = torch.randn(200, 8)
y = (X[:, 0] + X[:, 1] > 0).long()
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=32, shuffle=True)
model = nn.Sequential(nn.Linear(8, 16), nn.ReLU(), nn.Linear(16, 2))
base_opt = optim.SGD
sam_opt = SAM(model.parameters(), base_opt, lr=0.01, momentum=0.9, rho=0.05)
loss_fn = nn.CrossEntropyLoss()
for epoch in range(3):
    total = sum(sam_training_step(model, sam_opt, xb, yb, loss_fn)
                for xb, yb in loader)
    print(f"Epoch {epoch+1}: avg loss {total/len(loader):.4f}")
```

## ML Connections: Batch Size, LR, and Flatness

The flat minima connection unifies several empirical observations that previously seemed unrelated. First, large-batch training finds sharper minima because the noise covariance η·C/B is smaller at large B, weakening the implicit flat-minima regularization — this is why naive large-batch training generalizes worse and why SAM is especially effective when combined with large batches. Second, a higher learning rate η increases noise, biasing toward flatter minima within the stable training range — this is why the 'linear scaling rule' (double LR when doubling batch size) approximately preserves generalization. Third, dropout is another noise source that implicitly encourages flat minima by making the model robust to random unit deactivation, analogous to weight perturbation. Fourth, model soups (Wortsman et al. 2022) and SWA work because averaging multiple checkpoints moves the effective weights toward the geometric center of a flat valley, giving better calibration and generalization than any single checkpoint. Fifth, in self-supervised learning, the momentum encoder in BYOL/DINO tracks an exponential moving average of the online encoder, which implicitly samples from a flat region of weight space and provides more stable targets for representation learning.

```python
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

def make_data(n=300, seed=0):
    torch.manual_seed(seed)
    X = torch.randn(n, 6)
    y = (X[:, 0] - X[:, 1] + 0.5 * X[:, 2] > 0).long()
    return X, y

def train_model(X, y, batch_size, lr, use_sam=False, epochs=20):
    model = nn.Sequential(nn.Linear(6, 12), nn.ReLU(), nn.Linear(12, 2))
    loader = DataLoader(TensorDataset(X[:240], y[:240]), batch_size=batch_size)
    if use_sam:
        opt = SAM(model.parameters(), optim.SGD, lr=lr, rho=0.05)
    else:
        opt = optim.SGD(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()
    for _ in range(epochs):
        for xb, yb in loader:
            if use_sam:
                opt.zero_grad()
                loss_fn(model(xb), yb).backward()
                opt.first_step(zero_grad=True)
                loss_fn(model(xb), yb).backward()
                opt.second_step(zero_grad=True)
            else:
                opt.zero_grad()
                loss_fn(model(xb), yb).backward()
                opt.step()
    with torch.no_grad():
        preds = model(X[240:]).argmax(1)
        return (preds == y[240:]).float().mean().item()

X, y = make_data()
print(f"SGD small batch (B=16):  test acc = {train_model(X, y, 16, 0.05):.3f}")
print(f"SGD large batch (B=128): test acc = {train_model(X, y, 128, 0.05):.3f}")
print(f"SAM large batch (B=128): test acc = {train_model(X, y, 128, 0.05, use_sam=True):.3f}")
```

## Implementation Pitfalls

Four pitfalls when implementing SAM and flat-minima techniques. First, forgetting to restore weights after the first step: if the model parameters are not restored before the second gradient computation, the second gradient is computed at the perturbed point but the update is also applied at the perturbed point — losing the flat-minima objective entirely. Always save and restore original parameters. Second, using SAM with gradient accumulation without reducing per-step loss by the accumulation factor: accumulation inflates gradient norms, making the perturbation radius effectively larger than intended. Third, monitoring only training loss: SAM sometimes causes training loss to plateau while test loss continues to improve — this is a feature, not a bug, but can be misinterpreted as lack of progress. Fourth, using SAM when the generalization gap is small: if train and test accuracy are already within 1%, SAM adds compute overhead without meaningful benefit. Profile the generalization gap before adding SAM.

## Practical Guidance

Practical guidelines for applying flat-minima insights. Choose batch size and learning rate together: use the largest batch size that fits in memory, then scale LR proportionally (linear scaling rule: LR = base_LR × B/256), and add SAM if the generalization gap is still larger than expected. For monitoring sharpness cheaply: log the gradient norm after backward() before clipping — gradient norm at critical points correlates with sharpness (higher gradient norm → sharper curvature along the trajectory). Use SWA as a free improvement: after the main training schedule, run 10-20 more epochs with a cyclic LR schedule (SWA-style) and average the checkpoints; this typically gains 0.3-0.5% accuracy with no architecture changes. For fine-tuning pre-trained models, start with lower ρ (e.g., 0.01 instead of 0.05) in SAM to avoid disrupting the pre-trained features, and increase ρ only if the generalization gap warrants it.

> **Warning**: SAM doubles compute cost — only use it when the generalization gap (train accuracy minus test accuracy) exceeds 2%. Monitor train and test loss separately throughout SAM training: if both decrease together, SAM is working as expected. If train loss stops decreasing but test loss keeps improving, the model has found a flat minimum and you may safely reduce ρ to accelerate convergence. Never use SAM as a substitute for proper regularization (weight decay, dropout, data augmentation) — those should be in place first.

| Optimizer | Sharpness | Generalization | Compute Overhead | Memory Overhead |
|---|---|---|---|---|
| SGD small batch (B≤32) | Low (flat) | Best | 1× | 1× |
| SGD large batch (B≥512) | High (sharp) | Worse at same LR | 1× (fast steps) | 1× |
| Adam | Medium-high | Good (adaptive LR) | 1.3× (moment buffers) | 2× (m, v buffers) |
| SAM + SGD | Low (explicit) | Best in class | 2× (two passes) | 1× + e_w buffer |
| SWA | Low (center of valley) | Very good | 1× + averaging step | 2× (model + SWA model) |

---

## Key Takeaways

- Sharpness is measured by λ_max (largest Hessian eigenvalue, worst-case curvature) or tr(H) (average curvature, cheaper via Hutchinson's estimator).
- PAC-Bayes theorem formalizes why flat minima generalize better: the generalization bound is controlled by KL(Q||P), which is smaller when the model is robust to weight perturbations.
- SAM minimizes max_{‖ε‖≤ρ} L(θ+ε): perturb weights in gradient direction, compute gradient at perturbed point, update from original weights — explicitly targeting the PAC-Bayes bound.
- SGD implicitly biases toward flat minima via gradient noise with scale η/B; large batch size weakens this bias, explaining the generalization gap of large-batch training.
- SWA (Stochastic Weight Averaging) places the model at the flat geometric center of a loss valley by averaging late-training checkpoints — free 0.3-0.5% improvement.
- Use SAM only when the generalization gap exceeds 2%; profile train/test loss separately and reduce ρ when both losses align.
- The linear scaling rule (LR ∝ B) approximately preserves the implicit flat-minima regularization when scaling batch size, but breaks at very large batches where the noise is no longer well-modeled as Gaussian.

