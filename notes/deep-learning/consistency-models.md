---
title: "Consistency Models — Single-Step Distillation"
slug: "consistency-models"
description: "Consistency models define a function that maps any point on a diffusion trajectory to the same clean endpoint x_0, enabling single-step generation via consistency training or distillation from a diffusion teacher, with Latent Consistency Models bringing 4-step generation to Stable Diffusion."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uc2lzdGVuY3kgbW9kZWxzIChTb25nIGV0IGFsLiAyMDIzKSBhcmUgYSBuZXcgZmFtaWx5IG9mIGdlbmVyYXRpdmUgbW9kZWxzIHRoYXQgcHJvZHVjZSBoaWdoLXF1YWxpdHkgc2FtcGxlcyBpbiBvbmUgb3IgYSBmZXcgc3RlcHMuIFRoZSBjb3JlIGlkZWEgaXMgdG8gdHJhaW4gYSBjb25zaXN0ZW5jeSBmdW5jdGlvbiBmX864KHhfdCwgdCkgdGhhdCBtYXBzIGFueSBwb2ludCBvbiBhIGRpZmZ1c2lvbiB0cmFqZWN0b3J5IOKAlCByZWdhcmRsZXNzIG9mIHRoZSBub2lzZSBsZXZlbCB0IOKAlCB0byB0aGUgc2FtZSBjbGVhbiBkYXRhIHBvaW50IHhfMC4gT25jZSBzdWNoIGEgZnVuY3Rpb24gZXhpc3RzLCBnZW5lcmF0aW9uIGlzIHRyaXZpYWw6IHNhbXBsZSBHYXVzc2lhbiBub2lzZSwgYXBwbHkgZl/OuCBvbmNlLCBhbmQgb2J0YWluIGEgc2FtcGxlLiBNdWx0aS1zdGVwIHJlZmluZW1lbnQgaXMgYWxzbyBwb3NzaWJsZSBieSBhbHRlcm5hdGluZyBiZXR3ZWVuIGFkZGluZyBzbWFsbCBhbW91bnRzIG9mIG5vaXNlIGFuZCByZS1hcHBseWluZyBmX864LCB0cmFkaW5nIGNvbXB1dGUgZm9yIHF1YWxpdHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uc2lzdGVuY3kgRnVuY3Rpb24gYW5kIEJvdW5kYXJ5IENvbmRpdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvbnNpc3RlbmN5IGZ1bmN0aW9uIGZfzrg6ICh4X3QsIHQpIOKGkiB4XzAgbXVzdCBzYXRpc2Z5IHRoZSBzZWxmLWNvbnNpc3RlbmN5IHByb3BlcnR5OiBmX864KHhfdCwgdCkgPSBmX864KHhfcywgcykgZm9yIGFsbCB0LCBzIG9uIHRoZSBzYW1lIHRyYWplY3Rvcnkgc3RhcnRpbmcgZnJvbSB4XzAuIFRoaXMgbWVhbnMgdGhhdCBkZW5vaXNpbmcgZnJvbSBhbnkgbm9pc2UgbGV2ZWwgcmV0dXJucyB0aGUgc2FtZSBlbmRwb2ludC4gVGhlIGJvdW5kYXJ5IGNvbmRpdGlvbiBmX864KHhfMCwgMCkgPSB4XzAgaXMgZW5mb3JjZWQgYXJjaGl0ZWN0dXJhbGx5IGJ5IHBhcmFtZXRlcmlzaW5nIGZfzrggYXMgYSBza2lwIGNvbm5lY3Rpb246IGZfzrgoeCx0KSA9IGNfc2tpcCh0KcK3eCArIGNfb3V0KHQpwrdGX864KHgsdCksIHdoZXJlIGNfc2tpcCgwKT0xIGFuZCBjX291dCgwKT0wIGZvcmNlIHRoZSBuZXR3b3JrIHRvIGFjdCBhcyBpZGVudGl0eSBhdCB0PTAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uc2lzdGVuY3kgVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnNpc3RlbmN5IFRyYWluaW5nIChDVCkgdHJhaW5zIGZfzrggZnJvbSBzY3JhdGNoIHdpdGhvdXQgYSBkaWZmdXNpb24gdGVhY2hlciBieSB1c2luZyBhIGJvb3RzdHJhcCB0YXJnZXQ6IGFuIGV4cG9uZW50aWFsIG1vdmluZyBhdmVyYWdlIChFTUEpIG9mIHBhc3QgcGFyYW1ldGVycyDOuF4tIGFjdHMgYXMgYSBzbG93LW1vdmluZyB0YXJnZXQgbmV0d29yay4gVGhlIENUIGxvc3MgZW5mb3JjZXMgY29uc2lzdGVuY3kgYmV0d2VlbiBhZGphY2VudCB0aW1lc3RlcCBwYWlyczogTF9DVCA9IEVbZChmX864KHhfe3Rfe24rMX19LCB0X3tuKzF9KSwgZl97zrheLX0oeMyCX3t0X259LCB0X24pKV0gd2hlcmUgeMyCX3t0X259IGlzIG9idGFpbmVkIGJ5IHJ1bm5pbmcgb25lIEV1bGVyIHN0ZXAgYmFja3dhcmQgZnJvbSB4X3t0X3tuKzF9fSB1c2luZyB0aGUgY3VycmVudCBFTUEgbW9kZWwuIFRoZSBFTUEgdXBkYXRlIM64Xi0g4oaQIM68wrfOuF4tICsgKDEtzrwpwrfOuCBwcmV2ZW50cyB0aGUgdGFyZ2V0IGZyb20gYmVpbmcgaWRlbnRpY2FsIHRvIHRoZSBzdHVkZW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IGNvcHlcblxuY2xhc3MgQ29uc2lzdGVuY3lNb2RlbChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlRveSBjb25zaXN0ZW5jeSBtb2RlbCB3aXRoIHNraXAtY29ubmVjdGlvbiBib3VuZGFyeSBjb25kaXRpb24uXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbT0yLCBoaWRkZW49MTI4LCB0X21pbj0wLjAwMiwgdF9tYXg9ODAuMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnRfbWluLCBzZWxmLnRfbWF4ID0gdF9taW4sIHRfbWF4XG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkaW0gKyAxLCBoaWRkZW4pLCBubi5TaUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCBoaWRkZW4pLCBubi5TaUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCBkaW0pXG4gICAgICAgIClcblxuICAgIGRlZiBjX3NraXAoc2VsZiwgdCk6XG4gICAgICAgIHJldHVybiBzZWxmLnRfbWluICoqIDIgLyAodCAqKiAyICsgc2VsZi50X21pbiAqKiAyKVxuXG4gICAgZGVmIGNfb3V0KHNlbGYsIHQpOlxuICAgICAgICByZXR1cm4gdCAqIHNlbGYudF9taW4gLyAodCAqKiAyICsgc2VsZi50X21pbiAqKiAyKSAqKiAwLjVcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIHQpOlxuICAgICAgICB0X2VtYiA9IHRbOiwgTm9uZV0uZXhwYW5kKHguc2hhcGVbMF0sIDEpXG4gICAgICAgIEZfb3V0ID0gc2VsZi5uZXQodG9yY2guY2F0KFt4LCB0X2VtYl0sIGRpbT0tMSkpXG4gICAgICAgIHNraXAgPSBzZWxmLmNfc2tpcCh0KVs6LCBOb25lXSAqIHhcbiAgICAgICAgb3V0ICA9IHNlbGYuY19vdXQodClbOiwgTm9uZV0gKiBGX291dFxuICAgICAgICByZXR1cm4gc2tpcCArIG91dCAgIyBib3VuZGFyeTogYXQgdD10X21pbiB0aGlzIGVxdWFscyB4XG5cbmRlZiBjdF9sb3NzKHN0dWRlbnQsIGVtYV9tb2RlbCwgeDAsIHRfbiwgdF9uMSwgbm9pc2U9Tm9uZSk6XG4gICAgaWYgbm9pc2UgaXMgTm9uZTpcbiAgICAgICAgbm9pc2UgPSB0b3JjaC5yYW5kbl9saWtlKHgwKVxuICAgIHhfdDEgPSB4MCArIHRfbjFbOiwgTm9uZV0gKiBub2lzZSAgICAgICAgICAgIyBub2lzeSBhdCB0X3tuKzF9XG4gICAgeF90MF9oYXQgPSB4X3QxIC0gKHRfbjEgLSB0X24pWzosIE5vbmVdICogbm9pc2UgICMgRXVsZXIgc3RlcCB0byB0X25cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgdGFyZ2V0ID0gZW1hX21vZGVsKHhfdDBfaGF0LmRldGFjaCgpLCB0X24pXG4gICAgcHJlZCA9IHN0dWRlbnQoeF90MSwgdF9uMSlcbiAgICByZXR1cm4gRi5tc2VfbG9zcyhwcmVkLCB0YXJnZXQpXG5cbnByaW50KFx1MDAyN0NUOiB0cmFpbnMgZnJvbSBzY3JhdGNoIHVzaW5nIEVNQSB0YXJnZXQg4oCUIG5vIHRlYWNoZXIgZGlmZnVzaW9uIG1vZGVsIG5lZWRlZFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25zaXN0ZW5jeSBEaXN0aWxsYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnNpc3RlbmN5IERpc3RpbGxhdGlvbiAoQ0QpIGxldmVyYWdlcyBhIHByZXRyYWluZWQgZGlmZnVzaW9uIG1vZGVsIGFzIGEgdGVhY2hlci4gVGhlIHRlYWNoZXJcdTAwMjdzIHNjb3JlIGZ1bmN0aW9uIGlzIHVzZWQgdG8gY29tcHV0ZSBhY2N1cmF0ZSBvbmUtc3RlcCBlc3RpbWF0ZXMgb2YgeF8wIGZyb20gYW55IHhfdC4gVGhlIHN0dWRlbnQgY29uc2lzdGVuY3kgbW9kZWwgaXMgdHJhaW5lZCB0byBtYXRjaCB0aGVzZSB0ZWFjaGVyLWRlcml2ZWQgeF8wIGVzdGltYXRlcyBhdCBhZGphY2VudCB0aW1lIHN0ZXBzLiBDRCB0eXBpY2FsbHkgYWNoaWV2ZXMgaGlnaGVyIHF1YWxpdHkgdGhhbiBDVCBhdCB0aGUgc2FtZSBzcGFyc2l0eSBiZWNhdXNlIHRoZSB0ZWFjaGVyIHByb3ZpZGVzIGJldHRlciB0YXJnZXRzLCBidXQgaXQgcmVxdWlyZXMgYSBwcmV0cmFpbmVkIHNjb3JlIG1vZGVsIGFzIGEgcHJlcmVxdWlzaXRlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgc2NvcmVfdG9feDAoeF90LCB0LCBzY29yZV9wcmVkLCBzaWdtYSk6XG4gICAgXCJcIlwiQ29udmVydCBzY29yZSBwcmVkaWN0aW9uIHRvIHhfMCBlc3RpbWF0ZSAoVHdlZWRpZVx1MDAyN3MgZm9ybXVsYSkuXCJcIlwiXG4gICAgcmV0dXJuIHhfdCArIHNpZ21hWzosIE5vbmVdICoqIDIgKiBzY29yZV9wcmVkXG5cbmRlZiBjZF9sb3NzKHN0dWRlbnQsIHRlYWNoZXJfc2NvcmVfZm4sIHgwLCB0X24sIHRfbjEpOlxuICAgIFwiXCJcIkNvbnNpc3RlbmN5IGRpc3RpbGxhdGlvbjogc3R1ZGVudCBtYXRjaGVzIHRlYWNoZXJcdTAwMjdzIHhfMCBlc3RpbWF0ZS5cIlwiXCJcbiAgICBub2lzZSA9IHRvcmNoLnJhbmRuX2xpa2UoeDApXG4gICAgc2lnbWFfbjEgPSB0X24xXG4gICAgeF90MSA9IHgwICsgc2lnbWFfbjFbOiwgTm9uZV0gKiBub2lzZSAgIyBub2lzeSBzYW1wbGUgYXQgdF97bisxfVxuXG4gICAgIyBUZWFjaGVyIHByZWRpY3RzIHNjb3JlIGF0IHhfdDFcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgc2NvcmUgPSB0ZWFjaGVyX3Njb3JlX2ZuKHhfdDEsIHRfbjEpXG4gICAgICAgIHgwX3RlYWNoZXIgPSBzY29yZV90b194MCh4X3QxLCB0X24xLCBzY29yZSwgc2lnbWFfbjEpXG4gICAgICAgICMgT25lIEV1bGVyIHN0ZXAgdG8gdF9uIHVzaW5nIHRlYWNoZXJcbiAgICAgICAgeF90MCA9IHhfdDEgKyAodF9uWzosIE5vbmVdIC0gdF9uMVs6LCBOb25lXSkgKiBzY29yZVxuICAgICAgICB0YXJnZXQgPSBzdHVkZW50KHhfdDAsIHRfbikuZGV0YWNoKClcblxuICAgIHByZWQgPSBzdHVkZW50KHhfdDEsIHRfbjEpXG4gICAgcmV0dXJuIEYubXNlX2xvc3MocHJlZCwgdGFyZ2V0KSArIDAuMSAqIEYubXNlX2xvc3MocHJlZCwgeDBfdGVhY2hlcilcblxuIyBEZW1vIHRlYWNoZXIgKHJhbmRvbSwgcmVwbGFjZSB3aXRoIHJlYWwgcHJldHJhaW5lZCBzY29yZSBtb2RlbClcbnRlYWNoZXIgPSBsYW1iZGEgeCwgdDogLXggLyAodFs6LCBOb25lXSArIDFlLTMpICAjIHRveSBzY29yZVxuc3R1ZGVudCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDMsIDY0KSwgbm4uU2lMVSgpLCBubi5MaW5lYXIoNjQsIDIpKVxueDAgPSB0b3JjaC5yYW5kbigzMiwgMilcbnRfbiAgPSB0b3JjaC5yYW5kKDMyKSAqIDAuNVxudF9uMSA9IHRfbiArIDAuMVxucHJpbnQoZlx1MDAyN0NEIHJlcXVpcmVzIHRlYWNoZXIgZGlmZnVzaW9uIG1vZGVsIOKAlCBhY2hpZXZlcyBoaWdoZXIgcXVhbGl0eSB0aGFuIENUIGFsb25lXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNhbXBsaW5nIHdpdGggQ29uc2lzdGVuY3kgTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW5nbGUtc3RlcCBnZW5lcmF0aW9uIGlzIHN0cmFpZ2h0Zm9yd2FyZDogc2FtcGxlIHhfVCB+IE4oMCwgVMKySSkgYW5kIGFwcGx5IGZfzrgoeF9ULCBUKSBvbmNlIHRvIGdldCB4XzAuIE11bHRpLXN0ZXAgZ2VuZXJhdGlvbiBhbHRlcm5hdGVzIGJldHdlZW4gZGVub2lzaW5nIGFuZCByZS1ub2lzaW5nOiBhcHBseSBmX864IHRvIGdldCB4XzAgZXN0aW1hdGUsIGFkZCBHYXVzc2lhbiBub2lzZSBhdCBhIGxvd2VyIGxldmVsIHRfe24tMX0sIHRoZW4gYXBwbHkgZl/OuCBhZ2Fpbi4gRWFjaCBhZGRpdGlvbmFsIHN0ZXAgaW1wcm92ZXMgcXVhbGl0eSBieSBhbGxvd2luZyB0aGUgbW9kZWwgdG8gcmVmaW5lIGl0cyBlc3RpbWF0ZS4gVHlwaWNhbGx5IDEtNCBzdGVwcyBhcmUgc3VmZmljaWVudCB0byBtYXRjaCBvciBhcHByb2FjaCB0aGUgcXVhbGl0eSBvZiAxMDAwLXN0ZXAgRERQTS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBjbV9zYW1wbGVfbXVsdGlzdGVwKG1vZGVsLCBuX3NhbXBsZXM9MjU2LCBzdGVwcz1Ob25lLCBkZXZpY2U9XHUwMDI3Y3B1XHUwMDI3LCB0X21heD04MC4wKTpcbiAgICBcIlwiXCJNdWx0aS1zdGVwIGNvbnNpc3RlbmN5IG1vZGVsIHNhbXBsaW5nOiBkZW5vaXNlIC1cdTAwM2UgYWRkIG5vaXNlIC1cdTAwM2UgZGVub2lzZS5cIlwiXCJcbiAgICBpZiBzdGVwcyBpcyBOb25lOlxuICAgICAgICBzdGVwcyA9IFt0X21heCwgMjAuMCwgNS4wLCAxLjBdICAjIGRlY3JlYXNpbmcgbm9pc2Ugc2NoZWR1bGVcbiAgICB4ID0gdG9yY2gucmFuZG4obl9zYW1wbGVzLCAyLCBkZXZpY2U9ZGV2aWNlKSAqIHRfbWF4XG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICMgRmlyc3QgZGVub2lzaW5nIHN0ZXAgZnJvbSB0X21heFxuICAgICAgICB0ID0gdG9yY2guZnVsbCgobl9zYW1wbGVzLCksIHN0ZXBzWzBdLCBkZXZpY2U9ZGV2aWNlKVxuICAgICAgICB4MF9oYXQgPSBtb2RlbCh4LCB0KVxuICAgICAgICBwcmludChmXHUwMDI3U3RlcCAwICh0PXtzdGVwc1swXX0pOiB4MF9oYXQgbWVhbj17eDBfaGF0Lm1lYW4oKTouNGZ9XHUwMDI3KVxuICAgICAgICBmb3IgaSwgdF92YWwgaW4gZW51bWVyYXRlKHN0ZXBzWzE6XSwgMSk6XG4gICAgICAgICAgICAjIEFkZCBub2lzZSBhdCBsZXZlbCB0X3ZhbCwgdGhlbiBkZW5vaXNlIGFnYWluXG4gICAgICAgICAgICBub2lzZSA9IHRvcmNoLnJhbmRuX2xpa2UoeDBfaGF0KVxuICAgICAgICAgICAgeF9ub2lzeSA9IHgwX2hhdCArIHRfdmFsICogbm9pc2VcbiAgICAgICAgICAgIHRfYmF0Y2ggPSB0b3JjaC5mdWxsKChuX3NhbXBsZXMsKSwgdF92YWwsIGRldmljZT1kZXZpY2UpXG4gICAgICAgICAgICB4MF9oYXQgPSBtb2RlbCh4X25vaXN5LCB0X2JhdGNoKVxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyN1N0ZXAge2l9ICh0PXt0X3ZhbH0pOiB4MF9oYXQgbWVhbj17eDBfaGF0Lm1lYW4oKTouNGZ9XHUwMDI3KVxuICAgIHJldHVybiB4MF9oYXRcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5tb2RlbCA9IHRvcmNoLm5uLlNlcXVlbnRpYWwoXG4gICAgdG9yY2gubm4uTGluZWFyKDMsIDY0KSwgdG9yY2gubm4uU2lMVSgpLCB0b3JjaC5ubi5MaW5lYXIoNjQsIDIpXG4pXG5zYW1wbGVzID0gY21fc2FtcGxlX211bHRpc3RlcChtb2RlbCwgbl9zYW1wbGVzPTY0KVxucHJpbnQoZlx1MDAyN0ZpbmFsIHNhbXBsZXMgc2hhcGU6IHtzYW1wbGVzLnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXRlbnQgQ29uc2lzdGVuY3kgTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMYXRlbnQgQ29uc2lzdGVuY3kgTW9kZWxzIChMQ00sIEx1byBldCBhbC4gMjAyMykgYXBwbHkgY29uc2lzdGVuY3kgZGlzdGlsbGF0aW9uIHRvIHRoZSBsYXRlbnQgc3BhY2Ugb2YgU3RhYmxlIERpZmZ1c2lvbiwgaW5oZXJpdGluZyBpdHMgVkFFIGFuZCBDTElQIHRleHQgZW5jb2RlciB3aGlsZSByZXBsYWNpbmcgdGhlIFUtTmV0IGRlbm9pc2luZyBwcm9jZXNzLiBMQ00gZGlzdGlsbHMgYSBwcmV0cmFpbmVkIFNEIG1vZGVsIGludG8gYSBjb25zaXN0ZW5jeSBtb2RlbCB0aGF0IGdlbmVyYXRlcyA1MTLDlzUxMiBpbWFnZXMgaW4gNC04IHN0ZXBzIGluc3RlYWQgb2YgMjUtNTAgRERJTSBzdGVwcywgYWNoaWV2aW5nIGEgNS0xMMOXIHNwZWVkdXAgd2l0aCBtaW5pbWFsIHF1YWxpdHkgbG9zcy4gTENNLUxvUkEgZnVydGhlciByZWR1Y2VzIHRoZSBhZGFwdGVyIHRvIG9ubHkgNjdNIHBhcmFtZXRlcnMsIGVuYWJsaW5nIGVmZmljaWVudCBmaW5lLXR1bmluZyBvbiB0b3Agb2YgYW55IFNEIGNoZWNrcG9pbnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSBkaWZmdXNlcnMgaW1wb3J0IERpZmZ1c2lvblBpcGVsaW5lLCBMQ01TY2hlZHVsZXJcblxuZGVmIHJ1bl9sY21faW5mZXJlbmNlKHByb21wdCwgbl9zdGVwcz00LCBndWlkYW5jZV9zY2FsZT0xLjAsIHNlZWQ9MCk6XG4gICAgXCJcIlwiTENNOiA0LXN0ZXAgbGF0ZW50IGNvbnNpc3RlbmN5IG1vZGVsIGdlbmVyYXRpb24uXCJcIlwiXG4gICAgZGV2aWNlID0gXHUwMDI3Y3VkYVx1MDAyNyBpZiB0b3JjaC5jdWRhLmlzX2F2YWlsYWJsZSgpIGVsc2UgXHUwMDI3Y3B1XHUwMDI3XG4gICAgZHR5cGUgID0gdG9yY2guZmxvYXQxNiBpZiBkZXZpY2UgPT0gXHUwMDI3Y3VkYVx1MDAyNyBlbHNlIHRvcmNoLmZsb2F0MzJcbiAgICBwaXBlID0gRGlmZnVzaW9uUGlwZWxpbmUuZnJvbV9wcmV0cmFpbmVkKFxuICAgICAgICBcdTAwMjdTaW1pYW5MdW8vTENNX0RyZWFtc2hhcGVyX3Y3XHUwMDI3LFxuICAgICAgICB0b3JjaF9kdHlwZT1kdHlwZSxcbiAgICApLnRvKGRldmljZSlcbiAgICBwaXBlLnNjaGVkdWxlciA9IExDTVNjaGVkdWxlci5mcm9tX2NvbmZpZyhwaXBlLnNjaGVkdWxlci5jb25maWcpXG4gICAgZ2VuZXJhdG9yID0gdG9yY2guR2VuZXJhdG9yKGRldmljZT1kZXZpY2UpLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgd2l0aCB0b3JjaC5pbmZlcmVuY2VfbW9kZSgpOlxuICAgICAgICByZXN1bHQgPSBwaXBlKFxuICAgICAgICAgICAgcHJvbXB0LFxuICAgICAgICAgICAgbnVtX2luZmVyZW5jZV9zdGVwcz1uX3N0ZXBzLFxuICAgICAgICAgICAgZ3VpZGFuY2Vfc2NhbGU9Z3VpZGFuY2Vfc2NhbGUsICAjIExDTSB3b3JrcyB3ZWxsIHdpdGggQ0ZHPTEuMFxuICAgICAgICAgICAgZ2VuZXJhdG9yPWdlbmVyYXRvcixcbiAgICAgICAgKVxuICAgIGltZyA9IHJlc3VsdC5pbWFnZXNbMF1cbiAgICBwcmludChmXHUwMDI3TENNIGdlbmVyYXRlZCB7aW1nLnNpemV9IGltYWdlIGluIHtuX3N0ZXBzfSBzdGVwcyAodnMgMjUtNTAgZm9yIERESU0pXHUwMDI3KVxuICAgIHJldHVybiBpbWdcblxucHJpbnQoXHUwMDI3TENNIHBpcGVsaW5lIHN0YWdlczpcdTAwMjcpXG5wcmludChcdTAwMjcgIDEuIFNhbWUgQ0xJUCBlbmNvZGVyICsgVkFFIGFzIFNEIDEuNVx1MDAyNylcbnByaW50KFx1MDAyNyAgMi4gTENNIHNjaGVkdWxlcjogc2tpcHBpbmctc3RlcCBjb25zaXN0ZW5jeSBkaXN0aWxsYXRpb25cdTAwMjcpXG5wcmludChcdTAwMjcgIDMuIDQtc3RlcCBpbmZlcmVuY2U6IHQ9Wzk4MCw3NjAsNDk5LDIzNV0gLVx1MDAzZSBkZWNvZGUgVkFFXHUwMDI3KVxucHJpbnQoXHUwMDI3ICA0LiBDRkc9MS4wIHdvcmtzIHdlbGwg4oCUIG5vIHVuY29uZGl0aW9uYWwgcGFzcyBuZWVkZWRcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSGlzdG9yaWNhbCBDb250ZXh0IGFuZCBJbXBhY3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnNpc3RlbmN5IG1vZGVscyBmaWxsZWQgYSBjcml0aWNhbCBnYXAgaW4gMjAyMyB3aGVuIERESU0gYW5kIERQTS1Tb2x2ZXIgaGFkIHB1c2hlZCBERFBNIHRvIH4yMC01MCBzdGVwcyBidXQgZnVydGhlciByZWR1Y3Rpb24gc2VlbWVkIHRvIHJlcXVpcmUgZnVuZGFtZW50YWxseSBuZXcgdHJhaW5pbmcgb2JqZWN0aXZlcy4gQ00gc2hvd2VkIHRoYXQgc2luZ2xlLXN0ZXAgZ2VuZXJhdGlvbiB3aXRoIG5lYXItRERQTSBxdWFsaXR5IGlzIGFjaGlldmFibGUgdmlhIGEgcHJpbmNpcGxlZCBzZWxmLWNvbnNpc3RlbmN5IG9iamVjdGl2ZS4gVGhpcyBpbnNwaXJlZCBhIHdhdmUgb2YgZGlzdGlsbGF0aW9uIGFwcHJvYWNoZXMg4oCUIEFERCAoQWR2ZXJzYXJpYWwgRGlmZnVzaW9uIERpc3RpbGxhdGlvbiksIERNRCAoRGlzdHJpYnV0aW9uIE1hdGNoaW5nIERpc3RpbGxhdGlvbiksIGFuZCBMaWdodG5pbmcgVDJJIOKAlCBlYWNoIHVzaW5nIGRpZmZlcmVudCBsb3NzIGZ1bmN0aW9ucyBidXQgc2hhcmluZyB0aGUgZ29hbCBvZiByZWR1Y2luZyBORkUgYmVsb3cgMTAuIExDTS1Mb1JBIG1hZGUgdGhpcyBhY2Nlc3NpYmxlIHRvIHRoZSBjb21tdW5pdHkgd2l0aG91dCBmdWxsIHJldHJhaW5pbmcuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJDVCB2cyBDRCBRdWFsaXR5IEdhcCIsImNvbnRlbnQiOiJDb25zaXN0ZW5jeSBUcmFpbmluZyAoQ1QpIHRyYWlucyBmcm9tIHNjcmF0Y2ggYW5kIGF2b2lkcyB0aGUgbmVlZCBmb3IgYSB0ZWFjaGVyIG1vZGVsIGJ1dCB0eXBpY2FsbHkgYWNoaWV2ZXMgaGlnaGVyIEZJRCB0aGFuIENvbnNpc3RlbmN5IERpc3RpbGxhdGlvbiAoQ0QpIGF0IHRoZSBzYW1lIG51bWJlciBvZiBzdGVwcy4gRm9yIHByb2R1Y3Rpb24gdXNlIHdoZXJlIHF1YWxpdHkgaXMgY3JpdGljYWwsIHByZWZlciBDRCBvdmVyIENULiBUaGUgRU1BIHRhcmdldCBxdWFsaXR5IGluIENUIGRlZ3JhZGVzIHdoZW4gdGhlIHRlYWNoZXIgKEVNQSBtb2RlbCkgaXMgdG9vIGZhciBmcm9tIHRoZSBzdHVkZW50IOKAlCB1c2UgYSBzbWFsbCBFTUEgZGVjYXkgKM68PTAuOTktMC45OTk5KSBhbmQgbW9uaXRvciB0aGUgY29uc2lzdGVuY3kgbG9zcyBjYXJlZnVsbHkuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIk5GRSIsIkZJRCAoSW1hZ2VOZXQgNjTDlzY0KSIsIlRyYWluaW5nIiwiUmVxdWlyZXMgVGVhY2hlciIsIk5vdGFibGUgVXNlIl0sInJvd3MiOltbIkREUE0iLCIxMDAwIiwiMy4xNyIsIlNjb3JlIG1hdGNoaW5nIChkZW5vaXNpbmcpIiwiTm8iLCJCYXNlbGluZSBnZW5lcmF0aXZlIG1vZGVsIl0sWyJERElNIiwiNTAiLCI0LjY3IiwiU2FtZSBhcyBERFBNIOKAlCBubyByZXRyYWluaW5nIiwiTm8gKHVzZXMgRERQTSB3ZWlnaHRzKSIsIkZhc3QgaW5mZXJlbmNlIGZyb20gRERQTSJdLFsiQ00gKENELCAxLXN0ZXApIiwiMSIsIjYuMjAiLCJEaXN0aWxsYXRpb24gZnJvbSBERFBNIHRlYWNoZXIiLCJZZXMiLCJGYXN0ZXN0IHNpbmdsZS1zdGVwIGdlbmVyYXRpb24iXSxbIkNNIChDRCwgMi1zdGVwKSIsIjIiLCI0LjcwIiwiRGlzdGlsbGF0aW9uIGZyb20gRERQTSB0ZWFjaGVyIiwiWWVzIiwiTmVhci1ERElNIHF1YWxpdHkgaW4gMiBzdGVwcyJdLFsiTENNIChTRCBsYXRlbnQpIiwiNCIsIn5jb21wYXJhYmxlIHRvIERESU0tMjUiLCJDRCBpbiBsYXRlbnQgc3BhY2UiLCJZZXMgKFNEIFUtTmV0KSIsIkZhc3QgU0QtcXVhbGl0eSBnZW5lcmF0aW9uIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRoZSBib3VuZGFyeSBjb25kaXRpb24gY19za2lwKDApPTEsIGNfb3V0KDApPTAgaXMgYXJjaGl0ZWN0dXJhbCDigJQgaGFyZC1jb2RlZCwgbm90IGxlYXJuZWQuIiwiTXVsdGktc3RlcCBDTSBzYW1wbGluZyB1c2VzIGEgZ2VvbWV0cmljIG5vaXNlIHNjaGVkdWxlOiBzdGFydCBhdCB0X21heCwgYWRkIGRlY3JlYXNpbmcgYW1vdW50cyBvZiBub2lzZSBhdCBlYWNoIHN0ZXAuIiwiTENNLUxvUkEgdHJhaW5zIG9ubHkgNjdNIGV4dHJhIHBhcmFtZXRlcnMgb24gdG9wIG9mIGFueSBTRCBjaGVja3BvaW50IOKAlCBpdCBkb2VzIG5vdCByZXF1aXJlIGEgZnVsbCByZXRyYWluLiIsIkxDTSBndWlkYW5jZSBzY2FsZSBvZiAxLjAtMi4wIHdvcmtzIHdlbGwgYmVjYXVzZSBjb25zaXN0ZW5jeSBkaXN0aWxsYXRpb24gYmFrZXMgQ0ZHIGludG8gdGhlIG1vZGVsIGR1cmluZyB0cmFpbmluZy4iLCJFTUEgZGVjYXkgzrwgaW4gQ1QgaXMgY3JpdGljYWw6IHRvbyBzbWFsbCBjYXVzZXMgaW5zdGFiaWxpdHk7IHRvbyBsYXJnZSBzbG93cyBsZWFybmluZy4gU3RhcnQgd2l0aCDOvD0wLjk5OSBhbmQgaW5jcmVhc2UgdG8gMC45OTk5IGxhdGUgaW4gdHJhaW5pbmcuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlbGF0aW9uIHRvIE90aGVyIEZhc3QgU2FtcGxlcnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRESU0gYW5kIERQTS1Tb2x2ZXIrKyBhY2NlbGVyYXRlIGluZmVyZW5jZSBieSBleHBsb2l0aW5nIHRoZSBPREUgc3RydWN0dXJlIG9mIHRoZSBERFBNIHByb2JhYmlsaXR5IGZsb3cgd2l0aG91dCByZXRyYWluaW5nLiBUaGV5IHJlZHVjZSBORkUgdG8gMjAtNTAgc3RlcHMgYnV0IGNhbm5vdCBhY2hpZXZlIHNpbmdsZS1zdGVwIGdlbmVyYXRpb24uIENvbnNpc3RlbmN5IG1vZGVscywgYnkgY29udHJhc3QsIHJlcXVpcmUgYSBuZXcgdHJhaW5pbmcgb2JqZWN0aXZlIChkaXN0aWxsYXRpb24gb3IgQ1QpIGJ1dCBhY2hpZXZlIDEtNCBORkUuIEFERCAoQWR2ZXJzYXJpYWwgRGlmZnVzaW9uIERpc3RpbGxhdGlvbikgY29tYmluZXMgdGhlIGRpc3RpbGxhdGlvbiBvYmplY3RpdmUgd2l0aCBhIEdBTiBkaXNjcmltaW5hdG9yLCBhY2hpZXZpbmcgU0RYTC1xdWFsaXR5IGluIDQgc3RlcHMuIFByb2dyZXNzaXZlIGRpc3RpbGxhdGlvbiAoU2FsaW1hbnMgXHUwMDI2IEhvIDIwMjIpIGhhbHZlcyB0aGUgcmVxdWlyZWQgc3RlcHMgaXRlcmF0aXZlbHkgYW5kIGlzIGEgcHJlY3Vyc29yIHRvIGZ1bGwgY29uc2lzdGVuY3kgZGlzdGlsbGF0aW9uLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Consistency Models — Single-Step Distillation

Consistency models (Song et al. 2023) are a new family of generative models that produce high-quality samples in one or a few steps. The core idea is to train a consistency function f_θ(x_t, t) that maps any point on a diffusion trajectory — regardless of the noise level t — to the same clean data point x_0. Once such a function exists, generation is trivial: sample Gaussian noise, apply f_θ once, and obtain a sample. Multi-step refinement is also possible by alternating between adding small amounts of noise and re-applying f_θ, trading compute for quality.

## Consistency Function and Boundary Condition

The consistency function f_θ: (x_t, t) → x_0 must satisfy the self-consistency property: f_θ(x_t, t) = f_θ(x_s, s) for all t, s on the same trajectory starting from x_0. This means that denoising from any noise level returns the same endpoint. The boundary condition f_θ(x_0, 0) = x_0 is enforced architecturally by parameterising f_θ as a skip connection: f_θ(x,t) = c_skip(t)·x + c_out(t)·F_θ(x,t), where c_skip(0)=1 and c_out(0)=0 force the network to act as identity at t=0.

## Consistency Training

Consistency Training (CT) trains f_θ from scratch without a diffusion teacher by using a bootstrap target: an exponential moving average (EMA) of past parameters θ^- acts as a slow-moving target network. The CT loss enforces consistency between adjacent timestep pairs: L_CT = E[d(f_θ(x_{t_{n+1}}, t_{n+1}), f_{θ^-}(x̂_{t_n}, t_n))] where x̂_{t_n} is obtained by running one Euler step backward from x_{t_{n+1}} using the current EMA model. The EMA update θ^- ← μ·θ^- + (1-μ)·θ prevents the target from being identical to the student.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import copy

class ConsistencyModel(nn.Module):
    """Toy consistency model with skip-connection boundary condition."""
    def __init__(self, dim=2, hidden=128, t_min=0.002, t_max=80.0):
        super().__init__()
        self.t_min, self.t_max = t_min, t_max
        self.net = nn.Sequential(
            nn.Linear(dim + 1, hidden), nn.SiLU(),
            nn.Linear(hidden, hidden), nn.SiLU(),
            nn.Linear(hidden, dim)
        )

    def c_skip(self, t):
        return self.t_min ** 2 / (t ** 2 + self.t_min ** 2)

    def c_out(self, t):
        return t * self.t_min / (t ** 2 + self.t_min ** 2) ** 0.5

    def forward(self, x, t):
        t_emb = t[:, None].expand(x.shape[0], 1)
        F_out = self.net(torch.cat([x, t_emb], dim=-1))
        skip = self.c_skip(t)[:, None] * x
        out  = self.c_out(t)[:, None] * F_out
        return skip + out  # boundary: at t=t_min this equals x

def ct_loss(student, ema_model, x0, t_n, t_n1, noise=None):
    if noise is None:
        noise = torch.randn_like(x0)
    x_t1 = x0 + t_n1[:, None] * noise           # noisy at t_{n+1}
    x_t0_hat = x_t1 - (t_n1 - t_n)[:, None] * noise  # Euler step to t_n
    with torch.no_grad():
        target = ema_model(x_t0_hat.detach(), t_n)
    pred = student(x_t1, t_n1)
    return F.mse_loss(pred, target)

print('CT: trains from scratch using EMA target — no teacher diffusion model needed')
```

## Consistency Distillation

Consistency Distillation (CD) leverages a pretrained diffusion model as a teacher. The teacher's score function is used to compute accurate one-step estimates of x_0 from any x_t. The student consistency model is trained to match these teacher-derived x_0 estimates at adjacent time steps. CD typically achieves higher quality than CT at the same sparsity because the teacher provides better targets, but it requires a pretrained score model as a prerequisite.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def score_to_x0(x_t, t, score_pred, sigma):
    """Convert score prediction to x_0 estimate (Tweedie's formula)."""
    return x_t + sigma[:, None] ** 2 * score_pred

def cd_loss(student, teacher_score_fn, x0, t_n, t_n1):
    """Consistency distillation: student matches teacher's x_0 estimate."""
    noise = torch.randn_like(x0)
    sigma_n1 = t_n1
    x_t1 = x0 + sigma_n1[:, None] * noise  # noisy sample at t_{n+1}

    # Teacher predicts score at x_t1
    with torch.no_grad():
        score = teacher_score_fn(x_t1, t_n1)
        x0_teacher = score_to_x0(x_t1, t_n1, score, sigma_n1)
        # One Euler step to t_n using teacher
        x_t0 = x_t1 + (t_n[:, None] - t_n1[:, None]) * score
        target = student(x_t0, t_n).detach()

    pred = student(x_t1, t_n1)
    return F.mse_loss(pred, target) + 0.1 * F.mse_loss(pred, x0_teacher)

# Demo teacher (random, replace with real pretrained score model)
teacher = lambda x, t: -x / (t[:, None] + 1e-3)  # toy score
student = nn.Sequential(nn.Linear(3, 64), nn.SiLU(), nn.Linear(64, 2))
x0 = torch.randn(32, 2)
t_n  = torch.rand(32) * 0.5
t_n1 = t_n + 0.1
print(f'CD requires teacher diffusion model — achieves higher quality than CT alone')
```

## Sampling with Consistency Models

Single-step generation is straightforward: sample x_T ~ N(0, T²I) and apply f_θ(x_T, T) once to get x_0. Multi-step generation alternates between denoising and re-noising: apply f_θ to get x_0 estimate, add Gaussian noise at a lower level t_{n-1}, then apply f_θ again. Each additional step improves quality by allowing the model to refine its estimate. Typically 1-4 steps are sufficient to match or approach the quality of 1000-step DDPM.

```python
import torch

def cm_sample_multistep(model, n_samples=256, steps=None, device='cpu', t_max=80.0):
    """Multi-step consistency model sampling: denoise -> add noise -> denoise."""
    if steps is None:
        steps = [t_max, 20.0, 5.0, 1.0]  # decreasing noise schedule
    x = torch.randn(n_samples, 2, device=device) * t_max
    with torch.no_grad():
        # First denoising step from t_max
        t = torch.full((n_samples,), steps[0], device=device)
        x0_hat = model(x, t)
        print(f'Step 0 (t={steps[0]}): x0_hat mean={x0_hat.mean():.4f}')
        for i, t_val in enumerate(steps[1:], 1):
            # Add noise at level t_val, then denoise again
            noise = torch.randn_like(x0_hat)
            x_noisy = x0_hat + t_val * noise
            t_batch = torch.full((n_samples,), t_val, device=device)
            x0_hat = model(x_noisy, t_batch)
            print(f'Step {i} (t={t_val}): x0_hat mean={x0_hat.mean():.4f}')
    return x0_hat

torch.manual_seed(42)
model = torch.nn.Sequential(
    torch.nn.Linear(3, 64), torch.nn.SiLU(), torch.nn.Linear(64, 2)
)
samples = cm_sample_multistep(model, n_samples=64)
print(f'Final samples shape: {samples.shape}')
```

## Latent Consistency Models

Latent Consistency Models (LCM, Luo et al. 2023) apply consistency distillation to the latent space of Stable Diffusion, inheriting its VAE and CLIP text encoder while replacing the U-Net denoising process. LCM distills a pretrained SD model into a consistency model that generates 512×512 images in 4-8 steps instead of 25-50 DDIM steps, achieving a 5-10× speedup with minimal quality loss. LCM-LoRA further reduces the adapter to only 67M parameters, enabling efficient fine-tuning on top of any SD checkpoint.

```python
import torch
from diffusers import DiffusionPipeline, LCMScheduler

def run_lcm_inference(prompt, n_steps=4, guidance_scale=1.0, seed=0):
    """LCM: 4-step latent consistency model generation."""
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    dtype  = torch.float16 if device == 'cuda' else torch.float32
    pipe = DiffusionPipeline.from_pretrained(
        'SimianLuo/LCM_Dreamshaper_v7',
        torch_dtype=dtype,
    ).to(device)
    pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
    generator = torch.Generator(device=device).manual_seed(seed)
    with torch.inference_mode():
        result = pipe(
            prompt,
            num_inference_steps=n_steps,
            guidance_scale=guidance_scale,  # LCM works well with CFG=1.0
            generator=generator,
        )
    img = result.images[0]
    print(f'LCM generated {img.size} image in {n_steps} steps (vs 25-50 for DDIM)')
    return img

print('LCM pipeline stages:')
print('  1. Same CLIP encoder + VAE as SD 1.5')
print('  2. LCM scheduler: skipping-step consistency distillation')
print('  3. 4-step inference: t=[980,760,499,235] -> decode VAE')
print('  4. CFG=1.0 works well — no unconditional pass needed')
```

## Historical Context and Impact

Consistency models filled a critical gap in 2023 when DDIM and DPM-Solver had pushed DDPM to ~20-50 steps but further reduction seemed to require fundamentally new training objectives. CM showed that single-step generation with near-DDPM quality is achievable via a principled self-consistency objective. This inspired a wave of distillation approaches — ADD (Adversarial Diffusion Distillation), DMD (Distribution Matching Distillation), and Lightning T2I — each using different loss functions but sharing the goal of reducing NFE below 10. LCM-LoRA made this accessible to the community without full retraining.

> **CT vs CD Quality Gap**: Consistency Training (CT) trains from scratch and avoids the need for a teacher model but typically achieves higher FID than Consistency Distillation (CD) at the same number of steps. For production use where quality is critical, prefer CD over CT. The EMA target quality in CT degrades when the teacher (EMA model) is too far from the student — use a small EMA decay (μ=0.99-0.9999) and monitor the consistency loss carefully.

| Method | NFE | FID (ImageNet 64×64) | Training | Requires Teacher | Notable Use |
| --- | --- | --- | --- | --- | --- |
| DDPM | 1000 | 3.17 | Score matching (denoising) | No | Baseline generative model |
| DDIM | 50 | 4.67 | Same as DDPM — no retraining | No (uses DDPM weights) | Fast inference from DDPM |
| CM (CD, 1-step) | 1 | 6.20 | Distillation from DDPM teacher | Yes | Fastest single-step generation |
| CM (CD, 2-step) | 2 | 4.70 | Distillation from DDPM teacher | Yes | Near-DDIM quality in 2 steps |
| LCM (SD latent) | 4 | ~comparable to DDIM-25 | CD in latent space | Yes (SD U-Net) | Fast SD-quality generation |

- The boundary condition c_skip(0)=1, c_out(0)=0 is architectural — hard-coded, not learned.
- Multi-step CM sampling uses a geometric noise schedule: start at t_max, add decreasing amounts of noise at each step.
- LCM-LoRA trains only 67M extra parameters on top of any SD checkpoint — it does not require a full retrain.
- LCM guidance scale of 1.0-2.0 works well because consistency distillation bakes CFG into the model during training.
- EMA decay μ in CT is critical: too small causes instability; too large slows learning. Start with μ=0.999 and increase to 0.9999 late in training.

## Relation to Other Fast Samplers

DDIM and DPM-Solver++ accelerate inference by exploiting the ODE structure of the DDPM probability flow without retraining. They reduce NFE to 20-50 steps but cannot achieve single-step generation. Consistency models, by contrast, require a new training objective (distillation or CT) but achieve 1-4 NFE. ADD (Adversarial Diffusion Distillation) combines the distillation objective with a GAN discriminator, achieving SDXL-quality in 4 steps. Progressive distillation (Salimans & Ho 2022) halves the required steps iteratively and is a precursor to full consistency distillation.

---

