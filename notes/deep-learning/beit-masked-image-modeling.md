---
title: "BEiT — Masked Image Modeling with Visual Tokens"
slug: "beit-masked-image-modeling"
description: "How BEiT (Bao et al. 2022) applies BERT-style masked image modeling using discrete visual tokens from a pretrained dVAE tokenizer, block masking strategy, and the evolution to BEiT v2 and BEiT-3."
tags: ["deep-learning", "self-supervised-learning", "masked-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkVpVCAoQkVSVCBQcmUtVHJhaW5pbmcgb2YgSW1hZ2UgVHJhbnNmb3JtZXJzKSBieSBCYW8gZXQgYWwuICgyMDIyKSB3YXMgb25lIG9mIHRoZSBmaXJzdCBtZXRob2RzIHRvIGRpcmVjdGx5IGFwcGx5IEJFUlQtc3R5bGUgbWFza2VkIHByZWRpY3Rpb24gdG8gdmlzaW9uLiBVbmxpa2UgTUFFIHdoaWNoIHJlY29uc3RydWN0cyByYXcgcGl4ZWxzLCBCRWlUIHByZWRpY3RzIGRpc2NyZXRlIHZpc3VhbCB0b2tlbnMg4oCUIHF1YW50aXplZCBzZW1hbnRpYyBjb2RlcyBmcm9tIGEgcHJldHJhaW5lZCBpbWFnZSB0b2tlbml6ZXIg4oCUIG1ha2luZyB0aGUgcHJldGV4dCB0YXNrIG1vcmUgc2VtYW50aWNhbGx5IG1lYW5pbmdmdWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2hhdCBpcyBCRWlUPyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkVpVCBpcyBhIHR3by1zdGFnZSBzZWxmLXN1cGVydmlzZWQgcHJlLXRyYWluaW5nIGZyYW1ld29yayBmb3IgVmlULiBTdGFnZSAxIHRyYWlucyBhIGRpc2NyZXRlIHZhcmlhdGlvbmFsIGF1dG9lbmNvZGVyIChkVkFFLCBib3Jyb3dlZCBmcm9tIERBTEwtRSkgdG8gcHJvZHVjZSBhIHZvY2FidWxhcnkgb2YgODE5MiB2aXN1YWwgdG9rZW5zLiBTdGFnZSAyIHRyYWlucyBhIFZpVCB0byBwcmVkaWN0IHRoZSB2aXN1YWwgdG9rZW4gSURzIGF0IG1hc2tlZCBwb3NpdGlvbnMgdXNpbmcgY3Jvc3MtZW50cm9weSBsb3NzIG92ZXIgdGhlIDgxOTItdG9rZW4gdm9jYWJ1bGFyeSDigJQgZXhhY3RseSBCRVJUXHUwMDI3cyBtYXNrZWQgbGFuZ3VhZ2UgbW9kZWxpbmcgb2JqZWN0aXZlLCBidXQgZm9yIGltYWdlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdGFnZSAxIOKAlCBEaXNjcmV0ZSBJbWFnZSBUb2tlbml6ZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBpbWFnZSB0b2tlbml6ZXIgaXMgYSBWUS1WQUUgKFZlY3RvciBRdWFudGl6ZWQgVkFFKSBvciBkVkFFIHRoYXQgbWFwcyBpbWFnZSBwYXRjaGVzIHRvIGRpc2NyZXRlIGNvZGUgSURzIGZyb20gYSBmaXhlZCB2b2NhYnVsYXJ5LiBHaXZlbiBhbiBpbnB1dCBpbWFnZSwgdGhlIHRva2VuaXplciBwcm9kdWNlcyBhIGdyaWQgb2YgaW50ZWdlciB0b2tlbiBJRHMgKG9uZSBwZXIgcGF0Y2gpLiBUaGVzZSBJRHMgc2VydmUgYXMgdGhlIHByZWRpY3Rpb24gdGFyZ2V0cyBkdXJpbmcgcHJlLXRyYWluaW5nLiBCRWlUIHVzZXMgdGhlIERBTEwtRSBkVkFFIHdpdGggdm9jYWJ1bGFyeSBzaXplIDgxOTIsIG9wZXJhdGluZyBhdCAxNHgxNCA9IDE5NiB0b2tlbnMgZm9yIGEgMjI0cHggaW1hZ2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEltYWdlRW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgICMgU2ltcGxpZmllZCBDTk4gZW5jb2RlciBmb3IgdGhlIFZRIHRva2VuaXplclxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBlbWJlZF9kaW09NTEyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZCgzLCAxMjgsIDQsIDIsIDEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQoMTI4LCAyNTYsIDQsIDIsIDEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQoMjU2LCBlbWJlZF9kaW0sIDEpXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYubmV0KHgpXG5cbmNsYXNzIFZRVkFFVG9rZW5pemVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHZvY2FiX3NpemU9ODE5MiwgZW1iZWRfZGltPTUxMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVuY29kZXIgID0gSW1hZ2VFbmNvZGVyKGVtYmVkX2RpbSlcbiAgICAgICAgc2VsZi5jb2RlYm9vayA9IG5uLkVtYmVkZGluZyh2b2NhYl9zaXplLCBlbWJlZF9kaW0pXG4gICAgICAgIHNlbGYudm9jYWJfc2l6ZSA9IHZvY2FiX3NpemVcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICAjIEVuY29kZSBpbWFnZSB0byBjb250aW51b3VzIGVtYmVkZGluZ3M6IFtCLCBELCBILCBXXVxuICAgICAgICB6ID0gc2VsZi5lbmNvZGVyKHgpXG4gICAgICAgIEIsIEQsIEgsIFcgPSB6LnNoYXBlXG5cbiAgICAgICAgIyBSZXNoYXBlIGZvciBkaXN0YW5jZSBjb21wdXRhdGlvbjogW0IqSCpXLCBEXVxuICAgICAgICB6X2ZsYXQgPSB6LnBlcm11dGUoMCwgMiwgMywgMSkucmVzaGFwZSgtMSwgRClcblxuICAgICAgICAjIENvbXB1dGUgTDIgZGlzdGFuY2VzIHRvIGFsbCBjb2RlYm9vayBlbnRyaWVzXG4gICAgICAgIGRpc3RzID0gKFxuICAgICAgICAgICAgel9mbGF0LnBvdygyKS5zdW0oMSwga2VlcGRpbT1UcnVlKVxuICAgICAgICAgICAgKyBzZWxmLmNvZGVib29rLndlaWdodC5wb3coMikuc3VtKDEpXG4gICAgICAgICAgICAtIDIgKiB6X2ZsYXQgQCBzZWxmLmNvZGVib29rLndlaWdodC5UXG4gICAgICAgIClcbiAgICAgICAgIyBBc3NpZ24gdG8gbmVhcmVzdCBjb2RlYm9vayBlbnRyeSAtXHUwMDNlIGRpc2NyZXRlIHRva2VuIElEc1xuICAgICAgICB0b2tlbl9pZHMgPSBkaXN0cy5hcmdtaW4oMSkucmVzaGFwZShCLCBIICogVylcbiAgICAgICAgcmV0dXJuIHRva2VuX2lkcyAgICMgW0IsIE5dIGludGVnZXIgdG9rZW4gSURzXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIHRva2VuaXplKHNlbGYsIHgpOiByZXR1cm4gc2VsZi5mb3J3YXJkKHgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RhZ2UgMiDigJQgQmxvY2t3aXNlIE1hc2tpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJFaVQgbWFza3MgYXBwcm94aW1hdGVseSA0MCUgb2YgcGF0Y2hlcyB1c2luZyBibG9ja3dpc2UgKGNvbnRpZ3VvdXMgcmVjdGFuZ3VsYXIpIG1hc2tpbmcgcmF0aGVyIHRoYW4gcmFuZG9tIHVuaWZvcm0gbWFza2luZy4gTWFza2luZyBjb250aWd1b3VzIGJsb2NrcyBpcyBoYXJkZXIgdGhhbiBtYXNraW5nIHJhbmRvbSBzY2F0dGVyZWQgcGF0Y2hlcyBiZWNhdXNlIGFkamFjZW50IHZpc2libGUgcGF0Y2hlcyBjYW5ub3QgdHJpdmlhbGx5IGZpbGwgaW4gdGhlIG1pc3NpbmcgcmVnaW9uLiBUaGlzIGluY3JlYXNlcyB0YXNrIGRpZmZpY3VsdHkgYW5kIGVuY291cmFnZXMgdGhlIG1vZGVsIHRvIHJlYXNvbiBhYm91dCBzZW1hbnRpYyBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBibG9ja3dpc2VfbWFza2luZyhOLCBncmlkX3NpemUsIG1hc2tfcmF0aW89MC40MCwgbWluX2Jsb2NrPTQsIG1heF9ibG9jaz0yNSk6XG4gICAgIyBCbG9jay13aXNlIG1hc2tpbmc6IG1hc2sgY29udGlndW91cyByZWN0YW5ndWxhciByZWdpb25zXG4gICAgIyBSZXR1cm5zIGJpbmFyeSBtYXNrIG9mIHNoYXBlIFtOXSwgdmFsdWVzIDE9bWFza2VkIC8gMD12aXNpYmxlXG4gICAgaCA9IHcgPSBncmlkX3NpemVcbiAgICBtYXNrID0gdG9yY2guemVyb3MoaCwgdywgZHR5cGU9dG9yY2guYm9vbClcbiAgICB0YXJnZXQgPSBpbnQoTiAqIG1hc2tfcmF0aW8pXG4gICAgbWFza2VkX2NvdW50ID0gMFxuXG4gICAgd2hpbGUgbWFza2VkX2NvdW50IFx1MDAzYyB0YXJnZXQ6XG4gICAgICAgICMgU2FtcGxlIGEgcmFuZG9tIGJsb2NrIGFzcGVjdCByYXRpbyBhbmQgYXJlYVxuICAgICAgICBhc3BlY3QgICAgICA9IG5wLnJhbmRvbS51bmlmb3JtKDAuMywgMSAvIDAuMylcbiAgICAgICAgYmxvY2tfYXJlYSAgPSBucC5yYW5kb20ucmFuZGludChtaW5fYmxvY2ssIG1heF9ibG9jayArIDEpXG4gICAgICAgIGJoID0gbWF4KDEsIGludChucC5zcXJ0KGJsb2NrX2FyZWEgKiBhc3BlY3QpKSlcbiAgICAgICAgYncgPSBtYXgoMSwgaW50KG5wLnNxcnQoYmxvY2tfYXJlYSAvIGFzcGVjdCkpKVxuICAgICAgICBiaCwgYncgPSBtaW4oYmgsIGgpLCBtaW4oYncsIHcpXG5cbiAgICAgICAgIyBSYW5kb20gdG9wLWxlZnQgY29ybmVyIHdpdGhpbiB2YWxpZCByYW5nZVxuICAgICAgICB0b3AgID0gbnAucmFuZG9tLnJhbmRpbnQoMCwgaCAtIGJoICsgMSlcbiAgICAgICAgbGVmdCA9IG5wLnJhbmRvbS5yYW5kaW50KDAsIHcgLSBidyArIDEpXG4gICAgICAgIG1hc2tbdG9wOnRvcCArIGJoLCBsZWZ0OmxlZnQgKyBid10gPSBUcnVlXG4gICAgICAgIG1hc2tlZF9jb3VudCA9IG1hc2suc3VtKCkuaXRlbSgpXG5cbiAgICAjIFRyaW0gYW55IG92ZXItbWFza2VkIHBhdGNoZXMgdG8gaGl0IHRoZSBleGFjdCByYXRpb1xuICAgIG1hc2tfZmxhdCA9IG1hc2suZmxhdHRlbigpXG4gICAgbWFza2VkX2lkeCA9IG1hc2tfZmxhdC5ub256ZXJvKGFzX3R1cGxlPVRydWUpWzBdXG4gICAgaWYgbGVuKG1hc2tlZF9pZHgpIFx1MDAzZSB0YXJnZXQ6XG4gICAgICAgIG5fZHJvcCA9IGxlbihtYXNrZWRfaWR4KSAtIHRhcmdldFxuICAgICAgICBkcm9wX2lkeCA9IG1hc2tlZF9pZHhbdG9yY2gucmFuZHBlcm0obGVuKG1hc2tlZF9pZHgpKVs6bl9kcm9wXV1cbiAgICAgICAgbWFza19mbGF0W2Ryb3BfaWR4XSA9IEZhbHNlXG5cbiAgICByZXR1cm4gbWFza19mbGF0LmxvbmcoKSAgIyBbTl0sIDE9bWFza2VkLCAwPXZpc2libGUifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCRWlUIFByZS10cmFpbmluZyBPYmplY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0cmFpbmluZyBvYmplY3RpdmUgaXMgY3Jvc3MtZW50cm9weSBvdmVyIHRoZSB2aXN1YWwgdG9rZW4gdm9jYWJ1bGFyeSBhdCBtYXNrZWQgcG9zaXRpb25zLiBUaGUgVmlUIHJlY2VpdmVzIGFsbCBwYXRjaGVzIChpbmNsdWRpbmcgbWFzayB0b2tlbnMgYXQgbWFza2VkIHBvc2l0aW9ucykgYW5kIG11c3QgcHJlZGljdCB0aGUgY29ycmVjdCB0b2tlbiBJRCBmb3IgZWFjaCBtYXNrZWQgcG9zaXRpb24uIFRoaXMgaXMgYSBjbGFzc2lmaWNhdGlvbiB0YXNrIG92ZXIgODE5MiBjbGFzc2VzIHBlciBtYXNrZWQgcGF0Y2gsIG1ha2luZyBpdCBmdW5kYW1lbnRhbGx5IGRpZmZlcmVudCBmcm9tIE1BRVx1MDAyN3MgcmVncmVzc2lvbiBvYmplY3RpdmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEJFaVRNb2RlbChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB2b2NhYl9zaXplPTgxOTIsIHBhdGNoX3NpemU9MTYsIGltZ19zaXplPTIyNCxcbiAgICAgICAgICAgICAgICAgZW1iZWRfZGltPTc2OCwgZGVwdGg9MTIsIG51bV9oZWFkcz0xMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBudW1fcGF0Y2hlcyA9IChpbWdfc2l6ZSAvLyBwYXRjaF9zaXplKSAqKiAyXG4gICAgICAgIHNlbGYucGF0Y2hfZW1iZWQgPSBubi5Db252MmQoMywgZW1iZWRfZGltLCBwYXRjaF9zaXplLCBzdHJpZGU9cGF0Y2hfc2l6ZSlcbiAgICAgICAgc2VsZi5jbHNfdG9rZW4gICA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcygxLCAxLCBlbWJlZF9kaW0pKVxuICAgICAgICBzZWxmLnBvc19lbWJlZCAgID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKDEsIG51bV9wYXRjaGVzICsgMSwgZW1iZWRfZGltKSlcbiAgICAgICAgc2VsZi5tYXNrX3Rva2VuICA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcygxLCAxLCBlbWJlZF9kaW0pKVxuICAgICAgICBzZWxmLmJsb2NrcyA9IG5uLk1vZHVsZUxpc3QoW1RyYW5zZm9ybWVyQmxvY2soZW1iZWRfZGltLCBudW1faGVhZHMpIGZvciBfIGluIHJhbmdlKGRlcHRoKV0pXG4gICAgICAgIHNlbGYubm9ybSA9IG5uLkxheWVyTm9ybShlbWJlZF9kaW0pXG4gICAgICAgIHNlbGYuaGVhZCA9IG5uLkxpbmVhcihlbWJlZF9kaW0sIHZvY2FiX3NpemUpICAjIHByZWRpY3Qgb3ZlciA4MTkyIHZpc3VhbCB0b2tlbnNcblxuZGVmIGJlaXRfZm9yd2FyZChtb2RlbCwgaW1ncywgdG9rZW5faWRzLCBtYXNrKTpcbiAgICAjIG1hc2s6IFtCLCBOXSwgMT1tYXNrZWQgMD12aXNpYmxlXG4gICAgQiA9IGltZ3Muc2hhcGVbMF1cbiAgICB4ID0gbW9kZWwucGF0Y2hfZW1iZWQoaW1ncykuZmxhdHRlbigyKS50cmFuc3Bvc2UoMSwgMikgICMgW0IsIE4sIERdXG4gICAgeCA9IHggKyBtb2RlbC5wb3NfZW1iZWRbOiwgMTosIDpdXG5cbiAgICAjIFN1YnN0aXR1dGUgbWFza2VkIHBhdGNoIGVtYmVkZGluZ3Mgd2l0aCB0aGUgbGVhcm5hYmxlIG1hc2sgdG9rZW5cbiAgICBtYXNrX2V4cGFuZGVkID0gbWFzay51bnNxdWVlemUoLTEpLmZsb2F0KClcbiAgICB4ID0geCAqICgxIC0gbWFza19leHBhbmRlZCkgKyBtb2RlbC5tYXNrX3Rva2VuICogbWFza19leHBhbmRlZFxuXG4gICAgIyBQcmVwZW5kIGNscyB0b2tlbiBhbmQgcnVuIFZpVCBibG9ja3NcbiAgICBjbHMgPSBtb2RlbC5jbHNfdG9rZW4uZXhwYW5kKEIsIC0xLCAtMSlcbiAgICB4ICAgPSB0b3JjaC5jYXQoW2NscywgeF0sIGRpbT0xKVxuICAgIGZvciBibG9jayBpbiBtb2RlbC5ibG9ja3M6XG4gICAgICAgIHggPSBibG9jayh4KVxuICAgIGxvZ2l0cyA9IG1vZGVsLmhlYWQobW9kZWwubm9ybSh4KVs6LCAxOiwgOl0pICAgIyBbQiwgTiwgODE5Ml1cblxuICAgICMgQ3Jvc3MtZW50cm9weSBvbmx5IG9uIG1hc2tlZCBwb3NpdGlvbnNcbiAgICBsb3NzID0gRi5jcm9zc19lbnRyb3B5KGxvZ2l0c1ttYXNrLmJvb2woKV0sIHRva2VuX2lkc1ttYXNrLmJvb2woKV0pXG4gICAgcmV0dXJuIGxvc3MsIGxvZ2l0cyJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiU2VtYW50aWMgdnMgUGl4ZWwgVGFyZ2V0cyIsImNvbnRlbnQiOiJCRWlUXHUwMDI3cyBkaXNjcmV0ZSB0b2tlbiB0YXJnZXRzIGZpbHRlciBvdXQgaGlnaC1mcmVxdWVuY3kgcGl4ZWwgbm9pc2UgYW5kIGZvY3VzIHByZWRpY3Rpb24gb24gc2VtYW50aWMgY29udGVudC4gQSBwYXRjaCBzaG93aW5nIGEgY2F0XHUwMDI3cyBleWUgYW5kIGEgcGF0Y2ggc2hvd2luZyByYW5kb20gdGV4dHVyZSBtYXkgbG9vayBzaW1pbGFyIGluIHJhdyBwaXhlbHMgYnV0IGhhdmUgdmVyeSBkaWZmZXJlbnQgdG9rZW4gSURzLiBUaGlzIHNlbWFudGljIGRpc2NyZXRpemF0aW9uIGlzIEJFaVRcdTAwMjdzIG1haW4gYWR2YW50YWdlIG92ZXIgTUFFLXN0eWxlIHBpeGVsIHByZWRpY3Rpb24sIHRob3VnaCBpdCBjb21lcyBhdCB0aGUgY29zdCBvZiByZXF1aXJpbmcgYSBwcmUtdHJhaW5lZCB0b2tlbml6ZXIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXZhbHVhdGlvbiDigJQgTGluZWFyIFByb2JlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMaW5lYXIgcHJvYmluZyAodHJhaW5pbmcgb25seSBhIGxpbmVhciBjbGFzc2lmaWVyIG9uIGZyb3plbiBmZWF0dXJlcykgaXMgYSBzdGFuZGFyZCB3YXkgdG8gZXZhbHVhdGUgdGhlIHF1YWxpdHkgb2Ygc2VsZi1zdXBlcnZpc2VkIHJlcHJlc2VudGF0aW9ucy4gVW5saWtlIGZpbmUtdHVuaW5nIHdoaWNoIGFkYXB0cyBhbGwgd2VpZ2h0cywgbGluZWFyIHByb2JpbmcgZGlyZWN0bHkgbWVhc3VyZXMgaG93IGxpbmVhcmx5IHNlcGFyYWJsZSB0aGUgbGVhcm5lZCBmZWF0dXJlcyBhcmUuIFRoZSBmb2xsb3dpbmcgY29kZSBleHRyYWN0cyBDTFMgdG9rZW4gZmVhdHVyZXMgYW5kIHRyYWlucyBhIGxvZ2lzdGljIHJlZ3Jlc3Npb24gY2xhc3NpZmllciBmb3IgY29tcGFyaXNvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExvZ2lzdGljUmVncmVzc2lvblxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFjY3VyYWN5X3Njb3JlXG5cbmRlZiBleHRyYWN0X2Nsc19mZWF0dXJlcyhtb2RlbCwgZGF0YWxvYWRlciwgZGV2aWNlPVx1MDAyN2N1ZGFcdTAwMjcpOlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIGZlYXR1cmVzLCBsYWJlbHMgPSBbXSwgW11cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZm9yIGltZ3MsIGxibHMgaW4gZGF0YWxvYWRlcjpcbiAgICAgICAgICAgIGltZ3MgPSBpbWdzLnRvKGRldmljZSlcbiAgICAgICAgICAgICMgRm9yd2FyZCBwYXNzIHRocm91Z2ggZnJvemVuIGJhY2tib25lIOKAlCB1c2UgQ0xTIHRva2VuIGFzIGZlYXR1cmVzXG4gICAgICAgICAgICB4ID0gbW9kZWwucGF0Y2hfZW1iZWQoaW1ncykuZmxhdHRlbigyKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgICAgIHggPSB4ICsgbW9kZWwucG9zX2VtYmVkWzosIDE6LCA6XVxuICAgICAgICAgICAgY2xzID0gbW9kZWwuY2xzX3Rva2VuLmV4cGFuZChpbWdzLnNoYXBlWzBdLCAtMSwgLTEpXG4gICAgICAgICAgICB4ICAgPSB0b3JjaC5jYXQoW2NscywgeF0sIGRpbT0xKVxuICAgICAgICAgICAgZm9yIGJsb2NrIGluIG1vZGVsLmJsb2NrczpcbiAgICAgICAgICAgICAgICB4ID0gYmxvY2soeClcbiAgICAgICAgICAgIGZlYXRzID0gbW9kZWwubm9ybSh4KVs6LCAwXS5jcHUoKS5udW1weSgpICAjIENMUyB0b2tlblxuICAgICAgICAgICAgZmVhdHVyZXMuYXBwZW5kKGZlYXRzKVxuICAgICAgICAgICAgbGFiZWxzLmFwcGVuZChsYmxzLm51bXB5KCkpXG4gICAgcmV0dXJuIG5wLmNvbmNhdGVuYXRlKGZlYXR1cmVzKSwgbnAuY29uY2F0ZW5hdGUobGFiZWxzKVxuXG5kZWYgbGluZWFyX3Byb2JlKG1vZGVsLCB0cmFpbl9sb2FkZXIsIHZhbF9sb2FkZXIsIGRldmljZT1cdTAwMjdjdWRhXHUwMDI3KTpcbiAgICBwcmludChcdTAwMjdFeHRyYWN0aW5nIHRyYWluIGZlYXR1cmVzLi4uXHUwMDI3KVxuICAgIFhfdHIsIHlfdHIgPSBleHRyYWN0X2Nsc19mZWF0dXJlcyhtb2RlbCwgdHJhaW5fbG9hZGVyLCBkZXZpY2UpXG4gICAgcHJpbnQoXHUwMDI3RXh0cmFjdGluZyB2YWwgZmVhdHVyZXMuLi5cdTAwMjcpXG4gICAgWF92YWwsIHlfdmFsID0gZXh0cmFjdF9jbHNfZmVhdHVyZXMobW9kZWwsIHZhbF9sb2FkZXIsIGRldmljZSlcblxuICAgICMgTDIgbm9ybWFsaXplIChzdGFuZGFyZCBwcmFjdGljZSBmb3IgVmlUIGZlYXR1cmVzKVxuICAgIFhfdHIgID0gWF90ciAgLyAobnAubGluYWxnLm5vcm0oWF90ciwgIGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSkgKyAxZS04KVxuICAgIFhfdmFsID0gWF92YWwgLyAobnAubGluYWxnLm5vcm0oWF92YWwsIGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSkgKyAxZS04KVxuXG4gICAgY2xmID0gTG9naXN0aWNSZWdyZXNzaW9uKG1heF9pdGVyPTEwMDAsIEM9MS4wKVxuICAgIGNsZi5maXQoWF90ciwgeV90cilcbiAgICBhY2MgPSBhY2N1cmFjeV9zY29yZSh5X3ZhbCwgY2xmLnByZWRpY3QoWF92YWwpKVxuICAgIHByaW50KGZcdTAwMjdMaW5lYXIgcHJvYmUgdG9wLTE6IHthY2MgKiAxMDA6LjJmfSVcdTAwMjcpXG4gICAgcmV0dXJuIGFjYyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJFaVQgdjIgYW5kIEJFaVQtMyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkVpVCB2MiByZXBsYWNlcyB0aGUgREFMTC1FIGRWQUUgdG9rZW5pemVyIHdpdGggVlEtS0QgdG9rZW5zIGRpc3RpbGxlZCBmcm9tIGEgQ0xJUCBtb2RlbCwgcHJvZHVjaW5nIG1vcmUgc2VtYW50aWNhbGx5IG1lYW5pbmdmdWwgdGFyZ2V0cy4gQkVpVC0zIHVuaWZpZXMgdmlzaW9uLWxhbmd1YWdlIHByZXRyYWluaW5nIGJ5IHRyZWF0aW5nIGltYWdlIHBhdGNoZXMgYW5kIHRleHQgdG9rZW5zIHVuaWZvcm1seSDigJQgYm90aCBtYXNrZWQgd2l0aCB0aGUgc2FtZSBvYmplY3RpdmUg4oCUIGVuYWJsaW5nIGEgc2luZ2xlIG1vZGVsIHRvIGhhbmRsZSBpbWFnZSBjbGFzc2lmaWNhdGlvbiwgY2FwdGlvbmluZywgVlFBLCBhbmQgcmV0cmlldmFsLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQkVpVCAoMjAyMik6IGRWQUUgdG9rZW5zIGZyb20gREFMTC1FLCBibG9jayBtYXNraW5nIDQwJSwgVmlULUwgcmVhY2hlcyA4Ni4zJSBJbWFnZU5ldCB0b3AtMSIsIkJFaVQgdjIgKDIwMjIpOiBWUS1LRCB0b2tlbnMgZnJvbSBDTElQIHRlYWNoZXIsIG1vcmUgc2VtYW50aWMgdGFyZ2V0cywgaW1wcm92ZWQgbGluZWFyIHByb2JpbmciLCJCRWlULTMgKDIwMjIpOiBtdWx0aW1vZGFsIGZvdW5kYXRpb24gbW9kZWwsIHRyZWF0cyBpbWFnZSBwYXRjaGVzIGFuZCB0ZXh0IHRva2VucyB1bmlmb3JtbHkiLCJBbGwgdmFyaWFudHMgcmVxdWlyZSBhIHByZS10cmFpbmVkIHRva2VuaXplciDigJQgdW5saWtlIE1BRSB3aGljaCBuZWVkcyBub3RoaW5nIGJleW9uZCBpbWFnZSBkYXRhIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gVGFibGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0YWJsZSBiZWxvdyBjb21wYXJlcyBCRWlUIHZhcmlhbnRzIGFnYWluc3QgTUFFIGFuZCBpR1BUIChhdXRvcmVncmVzc2l2ZSBwaXhlbCBwcmVkaWN0aW9uKSBhY3Jvc3Mga2V5IGRlc2lnbiBkaW1lbnNpb25zLiBOb3RlIHRoZSB0cmFkZS1vZmYgYmV0d2VlbiB0b2tlbml6ZXIgcmVxdWlyZW1lbnQgYW5kIHJlcHJlc2VudGF0aW9uIHF1YWxpdHkuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlByZWRpY3Rpb24gVGFyZ2V0IiwiTWFzayBSYXRpbyIsIlRva2VuaXplciBOZWVkZWQiLCJNYXNraW5nIFN0cmF0ZWd5IiwiSU4tMUsgRmluZS10dW5lIFRvcC0xIl0sInJvd3MiOltbIkJFaVQiLCJkVkFFIHZpc3VhbCB0b2tlbnMiLCI0MCUiLCJZZXMgKERBTEwtRSBkVkFFKSIsIkJsb2NrIG1hc2tpbmciLCI4Ni4zJSAoVmlULUwpIl0sWyJCRWlUIHYyIiwiVlEtS0QgKENMSVApIHRva2VucyIsIjQwJSIsIlllcyAoQ0xJUCB0ZWFjaGVyKSIsIkJsb2NrIG1hc2tpbmciLCI4Ny4zJSAoVmlULUwpIl0sWyJNQUUiLCJOb3JtYWxpemVkIHBpeGVscyIsIjc1JSIsIk5vIiwiUmFuZG9tIG1hc2tpbmciLCI4Ny44JSAoVmlULUgpIl0sWyJpR1BUIiwiUXVhbnRpemVkIFJHQiBjbHVzdGVycyIsIk4vQSAoYXV0b3JlZ3Jlc3NpdmUpIiwiWWVzIChrLW1lYW5zIGNvbG9ycykiLCJOb25lIChhdXRvcmVncmVzc2l2ZSkiLCI3Mi4wJSAoaUdQVC1MKSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCRWlUXHUwMDI3cyB0b2tlbml6ZXIgZGVwZW5kZW5jeSBpcyBib3RoIGl0cyBtYWluIGNvc3QgYW5kIGl0cyBtYWluIGFkdmFudGFnZTogdGhlIHByZS10cmFpbmVkIHRva2VuaXplciBjb25zdHJhaW5zIHRoZSBtb2RlbCB0byBwcmVkaWN0IHN0cnVjdHVyZWQgc2VtYW50aWMgY29kZXMgcmF0aGVyIHRoYW4gbm9pc3kgcGl4ZWwgdmFsdWVzLCBwcm9kdWNpbmcgZmVhdHVyZXMgdGhhdCBnZW5lcmFsaXplIGJldHRlciB0byBzZW1hbnRpYyBkb3duc3RyZWFtIHRhc2tzIGxpa2Ugb2JqZWN0IGRldGVjdGlvbiBhbmQgZGVuc2UgcHJlZGljdGlvbi4ifV0="
---
# BEiT — Masked Image Modeling with Visual Tokens

BEiT (BERT Pre-Training of Image Transformers) by Bao et al. (2022) was one of the first methods to directly apply BERT-style masked prediction to vision. Unlike MAE which reconstructs raw pixels, BEiT predicts discrete visual tokens — quantized semantic codes from a pretrained image tokenizer — making the pretext task more semantically meaningful.

## What is BEiT?

BEiT is a two-stage self-supervised pre-training framework for ViT. Stage 1 trains a discrete variational autoencoder (dVAE, borrowed from DALL-E) to produce a vocabulary of 8192 visual tokens. Stage 2 trains a ViT to predict the visual token IDs at masked positions using cross-entropy loss over the 8192-token vocabulary — exactly BERT's masked language modeling objective, but for images.

## Stage 1 — Discrete Image Tokenizer

The image tokenizer is a VQ-VAE (Vector Quantized VAE) or dVAE that maps image patches to discrete code IDs from a fixed vocabulary. Given an input image, the tokenizer produces a grid of integer token IDs (one per patch). These IDs serve as the prediction targets during pre-training. BEiT uses the DALL-E dVAE with vocabulary size 8192, operating at 14x14 = 196 tokens for a 224px image.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ImageEncoder(nn.Module):
    # Simplified CNN encoder for the VQ tokenizer
    def __init__(self, embed_dim=512):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 128, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(128, 256, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(256, embed_dim, 1)
        )
    def forward(self, x): return self.net(x)

class VQVAETokenizer(nn.Module):
    def __init__(self, vocab_size=8192, embed_dim=512):
        super().__init__()
        self.encoder  = ImageEncoder(embed_dim)
        self.codebook = nn.Embedding(vocab_size, embed_dim)
        self.vocab_size = vocab_size

    def forward(self, x):
        # Encode image to continuous embeddings: [B, D, H, W]
        z = self.encoder(x)
        B, D, H, W = z.shape

        # Reshape for distance computation: [B*H*W, D]
        z_flat = z.permute(0, 2, 3, 1).reshape(-1, D)

        # Compute L2 distances to all codebook entries
        dists = (
            z_flat.pow(2).sum(1, keepdim=True)
            + self.codebook.weight.pow(2).sum(1)
            - 2 * z_flat @ self.codebook.weight.T
        )
        # Assign to nearest codebook entry -> discrete token IDs
        token_ids = dists.argmin(1).reshape(B, H * W)
        return token_ids   # [B, N] integer token IDs

    @torch.no_grad()
    def tokenize(self, x): return self.forward(x)
```

## Stage 2 — Blockwise Masking

BEiT masks approximately 40% of patches using blockwise (contiguous rectangular) masking rather than random uniform masking. Masking contiguous blocks is harder than masking random scattered patches because adjacent visible patches cannot trivially fill in the missing region. This increases task difficulty and encourages the model to reason about semantic structure.

```python
import torch
import numpy as np

def blockwise_masking(N, grid_size, mask_ratio=0.40, min_block=4, max_block=25):
    # Block-wise masking: mask contiguous rectangular regions
    # Returns binary mask of shape [N], values 1=masked / 0=visible
    h = w = grid_size
    mask = torch.zeros(h, w, dtype=torch.bool)
    target = int(N * mask_ratio)
    masked_count = 0

    while masked_count < target:
        # Sample a random block aspect ratio and area
        aspect      = np.random.uniform(0.3, 1 / 0.3)
        block_area  = np.random.randint(min_block, max_block + 1)
        bh = max(1, int(np.sqrt(block_area * aspect)))
        bw = max(1, int(np.sqrt(block_area / aspect)))
        bh, bw = min(bh, h), min(bw, w)

        # Random top-left corner within valid range
        top  = np.random.randint(0, h - bh + 1)
        left = np.random.randint(0, w - bw + 1)
        mask[top:top + bh, left:left + bw] = True
        masked_count = mask.sum().item()

    # Trim any over-masked patches to hit the exact ratio
    mask_flat = mask.flatten()
    masked_idx = mask_flat.nonzero(as_tuple=True)[0]
    if len(masked_idx) > target:
        n_drop = len(masked_idx) - target
        drop_idx = masked_idx[torch.randperm(len(masked_idx))[:n_drop]]
        mask_flat[drop_idx] = False

    return mask_flat.long()  # [N], 1=masked, 0=visible
```

## BEiT Pre-training Objective

The training objective is cross-entropy over the visual token vocabulary at masked positions. The ViT receives all patches (including mask tokens at masked positions) and must predict the correct token ID for each masked position. This is a classification task over 8192 classes per masked patch, making it fundamentally different from MAE's regression objective.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class BEiTModel(nn.Module):
    def __init__(self, vocab_size=8192, patch_size=16, img_size=224,
                 embed_dim=768, depth=12, num_heads=12):
        super().__init__()
        num_patches = (img_size // patch_size) ** 2
        self.patch_embed = nn.Conv2d(3, embed_dim, patch_size, stride=patch_size)
        self.cls_token   = nn.Parameter(torch.zeros(1, 1, embed_dim))
        self.pos_embed   = nn.Parameter(torch.zeros(1, num_patches + 1, embed_dim))
        self.mask_token  = nn.Parameter(torch.zeros(1, 1, embed_dim))
        self.blocks = nn.ModuleList([TransformerBlock(embed_dim, num_heads) for _ in range(depth)])
        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, vocab_size)  # predict over 8192 visual tokens

def beit_forward(model, imgs, token_ids, mask):
    # mask: [B, N], 1=masked 0=visible
    B = imgs.shape[0]
    x = model.patch_embed(imgs).flatten(2).transpose(1, 2)  # [B, N, D]
    x = x + model.pos_embed[:, 1:, :]

    # Substitute masked patch embeddings with the learnable mask token
    mask_expanded = mask.unsqueeze(-1).float()
    x = x * (1 - mask_expanded) + model.mask_token * mask_expanded

    # Prepend cls token and run ViT blocks
    cls = model.cls_token.expand(B, -1, -1)
    x   = torch.cat([cls, x], dim=1)
    for block in model.blocks:
        x = block(x)
    logits = model.head(model.norm(x)[:, 1:, :])   # [B, N, 8192]

    # Cross-entropy only on masked positions
    loss = F.cross_entropy(logits[mask.bool()], token_ids[mask.bool()])
    return loss, logits
```

> **Semantic vs Pixel Targets**: BEiT's discrete token targets filter out high-frequency pixel noise and focus prediction on semantic content. A patch showing a cat's eye and a patch showing random texture may look similar in raw pixels but have very different token IDs. This semantic discretization is BEiT's main advantage over MAE-style pixel prediction, though it comes at the cost of requiring a pre-trained tokenizer.

## Evaluation — Linear Probe

Linear probing (training only a linear classifier on frozen features) is a standard way to evaluate the quality of self-supervised representations. Unlike fine-tuning which adapts all weights, linear probing directly measures how linearly separable the learned features are. The following code extracts CLS token features and trains a logistic regression classifier for comparison.

```python
import torch
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def extract_cls_features(model, dataloader, device='cuda'):
    model.eval()
    features, labels = [], []
    with torch.no_grad():
        for imgs, lbls in dataloader:
            imgs = imgs.to(device)
            # Forward pass through frozen backbone — use CLS token as features
            x = model.patch_embed(imgs).flatten(2).transpose(1, 2)
            x = x + model.pos_embed[:, 1:, :]
            cls = model.cls_token.expand(imgs.shape[0], -1, -1)
            x   = torch.cat([cls, x], dim=1)
            for block in model.blocks:
                x = block(x)
            feats = model.norm(x)[:, 0].cpu().numpy()  # CLS token
            features.append(feats)
            labels.append(lbls.numpy())
    return np.concatenate(features), np.concatenate(labels)

def linear_probe(model, train_loader, val_loader, device='cuda'):
    print('Extracting train features...')
    X_tr, y_tr = extract_cls_features(model, train_loader, device)
    print('Extracting val features...')
    X_val, y_val = extract_cls_features(model, val_loader, device)

    # L2 normalize (standard practice for ViT features)
    X_tr  = X_tr  / (np.linalg.norm(X_tr,  axis=1, keepdims=True) + 1e-8)
    X_val = X_val / (np.linalg.norm(X_val, axis=1, keepdims=True) + 1e-8)

    clf = LogisticRegression(max_iter=1000, C=1.0)
    clf.fit(X_tr, y_tr)
    acc = accuracy_score(y_val, clf.predict(X_val))
    print(f'Linear probe top-1: {acc * 100:.2f}%')
    return acc
```

## BEiT v2 and BEiT-3

BEiT v2 replaces the DALL-E dVAE tokenizer with VQ-KD tokens distilled from a CLIP model, producing more semantically meaningful targets. BEiT-3 unifies vision-language pretraining by treating image patches and text tokens uniformly — both masked with the same objective — enabling a single model to handle image classification, captioning, VQA, and retrieval.

- BEiT (2022): dVAE tokens from DALL-E, block masking 40%, ViT-L reaches 86.3% ImageNet top-1
- BEiT v2 (2022): VQ-KD tokens from CLIP teacher, more semantic targets, improved linear probing
- BEiT-3 (2022): multimodal foundation model, treats image patches and text tokens uniformly
- All variants require a pre-trained tokenizer — unlike MAE which needs nothing beyond image data

## Comparison Table

The table below compares BEiT variants against MAE and iGPT (autoregressive pixel prediction) across key design dimensions. Note the trade-off between tokenizer requirement and representation quality.

| Method | Prediction Target | Mask Ratio | Tokenizer Needed | Masking Strategy | IN-1K Fine-tune Top-1 |
| --- | --- | --- | --- | --- | --- |
| BEiT | dVAE visual tokens | 40% | Yes (DALL-E dVAE) | Block masking | 86.3% (ViT-L) |
| BEiT v2 | VQ-KD (CLIP) tokens | 40% | Yes (CLIP teacher) | Block masking | 87.3% (ViT-L) |
| MAE | Normalized pixels | 75% | No | Random masking | 87.8% (ViT-H) |
| iGPT | Quantized RGB clusters | N/A (autoregressive) | Yes (k-means colors) | None (autoregressive) | 72.0% (iGPT-L) |

BEiT's tokenizer dependency is both its main cost and its main advantage: the pre-trained tokenizer constrains the model to predict structured semantic codes rather than noisy pixel values, producing features that generalize better to semantic downstream tasks like object detection and dense prediction.

