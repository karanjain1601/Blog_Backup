---
title: "Multi-Head Attention — Parallel Heads and Projection"
slug: "multi-head-attention"
description: "Unpack the MHA formula head by head: projection matrices, parallel scaled dot-product attention, concatenation, output projection, parameter count, and the efficient reshape trick."
tags: ["deep-learning", "transformers", "attention"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGktSGVhZCBBdHRlbnRpb24gKE1IQSkgcnVucyBoIGluZGVwZW5kZW50IHNjYWxlZCBkb3QtcHJvZHVjdCBhdHRlbnRpb24gb3BlcmF0aW9ucyBpbiBwYXJhbGxlbCwgZWFjaCBvbiBhIGxvd2VyLWRpbWVuc2lvbmFsIHByb2plY3Rpb24gb2YgdGhlIGlucHV0LiBUaGUgb3V0cHV0cyBhcmUgY29uY2F0ZW5hdGVkIGFuZCBwcm9qZWN0ZWQgYmFjayB0byB0aGUgbW9kZWwgZGltZW5zaW9uLiBUaGlzIGFsbG93cyB0aGUgbW9kZWwgdG8gam9pbnRseSBhdHRlbmQgdG8gaW5mb3JtYXRpb24gZnJvbSBoIGRpZmZlcmVudCByZXByZXNlbnRhdGlvbiBzdWJzcGFjZXMg4oCUIGEgcmljaGVyIGFuZCBtb3JlIGV4cHJlc3NpdmUgb3BlcmF0aW9uIHRoYW4gYSBzaW5nbGUgbGFyZ2UgYXR0ZW50aW9uIGhlYWQgb3BlcmF0aW5nIG9uIHRoZSBmdWxsIGRpbWVuc2lvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNSEEgRm9ybXVsYSBhbmQgU3RydWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgaGVhZCBpLCB0aGUgcXVlcnksIGtleSwgYW5kIHZhbHVlIHByb2plY3Rpb25zIGFyZSBR4bWiID0gUVfhtaJRLCBL4bWiID0gS1fhtaJLLCBW4bWiID0gVlfhtaJWIHdoZXJlIFfhtaJRLCBX4bWiSyDiiIgg4oSdXntkX21vZGVsw5dk4oKWfSBhbmQgV+G1olYg4oiIIOKEnV57ZF9tb2RlbMOXZHZ9LiBFYWNoIGhlYWQgY29tcHV0ZXMgaGVhZOG1oiA9IEF0dGVudGlvbihR4bWiLCBL4bWiLCBW4bWiKSDiiIgg4oSdXntuccOXZHZ9LiBUaGUgaCBoZWFkIG91dHB1dHMgYXJlIGNvbmNhdGVuYXRlZCBhbG9uZyB0aGUgbGFzdCBheGlzIHRvIGdldCDihJ1ee25xw5coaMK3ZHYpfSwgdGhlbiBwcm9qZWN0ZWQgYnkgV+G0vCDiiIgg4oSdXnsoaMK3ZHYpw5dkX21vZGVsfS4gV2l0aCB0aGUgc3RhbmRhcmQgY2hvaWNlIGg9OCwgZOKClj1kdj1kX21vZGVsL2g9NjQsIHRoZSB0b3RhbCBwYXJhbWV0ZXIgY291bnQgaW4gdGhlIGZvdXIgcHJvamVjdGlvbiBtYXRyaWNlcyBpcyA0wrdkX21vZGVswrIuIn0seyJ0eXBlIjoibWF0aCIsImNvbnRlbnQiOiJcXHRleHR7TXVsdGlIZWFkfShRLEssVikgPSBcXHRleHR7Q29uY2F0fShcXHRleHR7aGVhZH1fMSxcXGxkb3RzLFxcdGV4dHtoZWFkfV9oKVdeTywgXFxxdWFkIFxcdGV4dHtoZWFkfV9pID0gXFx0ZXh0e0F0dGVudGlvbn0oUVdfaV5RLFxcLCBLV19pXkssXFwsIFZXX2leVikiLCJkaXNwbGF5Ijp0cnVlfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcm9qZWN0aW9uIE1hdHJpY2VzIOKAlCBXaHkgVGhleSBNYXR0ZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldpdGhvdXQgcHJvamVjdGlvbiBtYXRyaWNlcywgTUhBIHdvdWxkIHNpbXBseSBzcGxpdCBRLCBLLCBWIGFsb25nIHRoZSBmZWF0dXJlIGF4aXMgYW5kIHJ1biBhdHRlbnRpb24gb24gZWFjaCBjaHVuay4gVGhlIHByb2plY3Rpb25zIGFsbG93IGVhY2ggaGVhZCB0byBsZWFybiBpdHMgb3duIHRyYW5zZm9ybWF0aW9uIG9mIHRoZSBpbnB1dCBiZWZvcmUgY29tcHV0aW5nIHNpbWlsYXJpdGllcyDigJQgaGVhZCBpIGNhbiBsZWFybiB0byBleHRyYWN0IHN5bnRhY3RpYyBmZWF0dXJlcywgaGVhZCBqIHNlbWFudGljIGZlYXR1cmVzLCB3aXRob3V0IGludGVyZmVyZW5jZS4gVGhlIG91dHB1dCBwcm9qZWN0aW9uIFfhtLwgbWl4ZXMgdGhlIGggaGVhZCBvdXRwdXRzIGFuZCBtYXBzIGJhY2sgdG8gZF9tb2RlbCBzbyB0aGUgcmVzaWR1YWwgYWRkaXRpb24geCArIE1IQSh4KSByZW1haW5zIHNoYXBlLXByZXNlcnZpbmcuIEluaXRpYWxpc2luZyBwcm9qZWN0aW9ucyB3aXRoIHNtYWxsIHJhbmRvbSB2YWx1ZXMgKHNjYWxlIH4gMS/iiJpkX21vZGVsKSBpcyBjcnVjaWFsIGZvciBzdGFibGUgdHJhaW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc2RwKFEsIEssIFYpOlxuICAgIGRrID0gUS5zaGFwZVstMV1cbiAgICBTID0gUSBAIEsuVCAvIG5wLnNxcnQoZGspXG4gICAgUyAtPSBTLm1heChheGlzPS0xLCBrZWVwZGltcz1UcnVlKVxuICAgIEEgPSBucC5leHAoUyk7IEEgLz0gQS5zdW0oYXhpcz0tMSwga2VlcGRpbXM9VHJ1ZSlcbiAgICByZXR1cm4gQSBAIFZcblxuY2xhc3MgTXVsdGlIZWFkQXR0ZW50aW9uOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsLCBoLCBzZWVkPTApOlxuICAgICAgICBzZWxmLmggPSBoXG4gICAgICAgIHNlbGYuZGsgPSBzZWxmLmR2ID0gZF9tb2RlbCAvLyBoXG4gICAgICAgIHJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZShzZWVkKVxuICAgICAgICBzY2FsZSA9IG5wLnNxcnQoMi4wIC8gZF9tb2RlbClcbiAgICAgICAgc2VsZi5XUSA9IHJuZy5yYW5kbihoLCBkX21vZGVsLCBzZWxmLmRrKSAqIHNjYWxlXG4gICAgICAgIHNlbGYuV0sgPSBybmcucmFuZG4oaCwgZF9tb2RlbCwgc2VsZi5kaykgKiBzY2FsZVxuICAgICAgICBzZWxmLldWID0gcm5nLnJhbmRuKGgsIGRfbW9kZWwsIHNlbGYuZHYpICogc2NhbGVcbiAgICAgICAgc2VsZi5XTyA9IHJuZy5yYW5kbihoICogc2VsZi5kdiwgZF9tb2RlbCkgKiBzY2FsZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgUSwgSywgVik6XG4gICAgICAgIGhlYWRzID0gW11cbiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uoc2VsZi5oKTpcbiAgICAgICAgICAgIFFpID0gUSBAIHNlbGYuV1FbaV0gICAjIChucSwgZGspXG4gICAgICAgICAgICBLaSA9IEsgQCBzZWxmLldLW2ldICAgIyAobmssIGRrKVxuICAgICAgICAgICAgVmkgPSBWIEAgc2VsZi5XVltpXSAgICMgKG5rLCBkdilcbiAgICAgICAgICAgIGhlYWRzLmFwcGVuZChzZHAoUWksIEtpLCBWaSkpICAgICMgKG5xLCBkdilcbiAgICAgICAgY29uY2F0ID0gbnAuY29uY2F0ZW5hdGUoaGVhZHMsIGF4aXM9LTEpICAjIChucSwgaCpkdilcbiAgICAgICAgcmV0dXJuIGNvbmNhdCBAIHNlbGYuV08gICAgICAgICAgICAgICAgICAjIChucSwgZF9tb2RlbClcblxubnAucmFuZG9tLnNlZWQoNDIpXG5kX21vZGVsLCBoLCBuID0gNTEyLCA4LCAxMFxubWhhID0gTXVsdGlIZWFkQXR0ZW50aW9uKGRfbW9kZWwsIGgpXG54ID0gbnAucmFuZG9tLnJhbmRuKG4sIGRfbW9kZWwpXG5vdXQgPSBtaGEuZm9yd2FyZCh4LCB4LCB4KVxucHJpbnQoXHUwMDI3SW5wdXQ6IFx1MDAyNywgeC5zaGFwZSwgXHUwMDI3LVx1MDAzZSBPdXRwdXQ6XHUwMDI3LCBvdXQuc2hhcGUpXG5wYXJhbXMgPSBoICogKGRfbW9kZWwgKiAoZF9tb2RlbC8vaCkgKiAzKSArIChoICogKGRfbW9kZWwvL2gpKSAqIGRfbW9kZWxcbnByaW50KFx1MDAyN1RvdGFsIHBhcmFtczogezosfSA9PSA0KmRfbW9kZWxeMjogezosfVx1MDAyNy5mb3JtYXQocGFyYW1zLCA0ICogZF9tb2RlbCoqMikpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHlUb3JjaCBubi5NdWx0aWhlYWRBdHRlbnRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlB5VG9yY2ggZnVzZXMgdGhlIHRocmVlIGlucHV0IHByb2plY3Rpb24gbWF0cmljZXMgV1EsIFdLLCBXViBpbnRvIGEgc2luZ2xlIGluX3Byb2pfd2VpZ2h0IG9mIHNoYXBlICgzwrdkX21vZGVsLCBkX21vZGVsKSBmb3IgZWZmaWNpZW5jeSDigJQgYSBzaW5nbGUgR0VNTSByZXBsYWNlcyB0aHJlZS4gVGhlIGJhdGNoX2ZpcnN0PVRydWUgZmxhZyBzZWxlY3RzIHRoZSAoYmF0Y2gsIHNlcSwgZF9tb2RlbCkgY29udmVudGlvbjsgdGhlIGRlZmF1bHQgaXMgKHNlcSwgYmF0Y2gsIGRfbW9kZWwpLiBGb3IgY3Jvc3MtYXR0ZW50aW9uLCBwYXNzIHRoZSBkZWNvZGVyIHN0YXRlcyBhcyBxdWVyeSBhbmQgdGhlIGVuY29kZXIgb3V0cHV0IGFzIGtleSBhbmQgdmFsdWUuIFRoZSByZXR1cm5lZCBhdHRuX3dlaWdodHMgdGVuc29yIGF2ZXJhZ2VzIGF0dGVudGlvbiB3ZWlnaHRzIGFjcm9zcyBoZWFkcyBieSBkZWZhdWx0OyBwYXNzIGF2ZXJhZ2VfYXR0bl93ZWlnaHRzPUZhbHNlIHRvIGdldCBwZXItaGVhZCB3ZWlnaHRzIChQeVRvcmNoIOKJpSAxLjEzKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5kX21vZGVsLCBoLCBzZXFfbGVuLCBiYXRjaCA9IDUxMiwgOCwgMTAsIDJcblxubWhhID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKFxuICAgIGVtYmVkX2RpbT1kX21vZGVsLFxuICAgIG51bV9oZWFkcz1oLFxuICAgIGJhdGNoX2ZpcnN0PVRydWUsXG4gICAgZHJvcG91dD0wLjBcbilcblxuIyBTZWxmLWF0dGVudGlvbjogUSA9IEsgPSBWID0geFxueCA9IHRvcmNoLnJhbmRuKGJhdGNoLCBzZXFfbGVuLCBkX21vZGVsKVxub3V0LCBhdHRuX3cgPSBtaGEoeCwgeCwgeClcbnByaW50KFx1MDAyN0lucHV0Olx1MDAyNywgdHVwbGUoeC5zaGFwZSkpXG5wcmludChcdTAwMjdPdXRwdXQ6XHUwMDI3LCB0dXBsZShvdXQuc2hhcGUpKVxucHJpbnQoXHUwMDI3QXR0biB3ZWlnaHRzIChhdmcgYWNyb3NzIGhlYWRzKTpcdTAwMjcsIHR1cGxlKGF0dG5fdy5zaGFwZSkpXG5wcmludChcdTAwMjdSb3cgc3VtczpcdTAwMjcsIGF0dG5fd1swXS5zdW0oZGltPS0xKS5yb3VuZChkZWNpbWFscz00KSlcblxuIyBDcm9zcy1hdHRlbnRpb246IGRlY29kZXIgcXVlcmllcyBhdHRlbmQgdG8gZW5jb2RlciBrZXktdmFsdWVcbmRlY19sZW4sIGVuY19sZW4gPSA2LCAxNVxucSAgID0gdG9yY2gucmFuZG4oYmF0Y2gsIGRlY19sZW4sIGRfbW9kZWwpXG5rdiAgPSB0b3JjaC5yYW5kbihiYXRjaCwgZW5jX2xlbiwgZF9tb2RlbClcbm91dF9jcm9zcywgY3Jvc3NfdyA9IG1oYShxLCBrdiwga3YpXG5wcmludChcdTAwMjdDcm9zcy1hdHRuIG91dHB1dDpcdTAwMjcsIHR1cGxlKG91dF9jcm9zcy5zaGFwZSkpXG5wcmludChcdTAwMjdDcm9zcy1hdHRuIHdlaWdodHM6XHUwMDI3LCB0dXBsZShjcm9zc193LnNoYXBlKSwgXHUwMDI3KGRlY19sZW4geCBlbmNfbGVuKVx1MDAyNylcblxudG90YWxfcGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtaGEucGFyYW1ldGVycygpKVxucHJpbnQoXHUwMDI3VG90YWwgTUhBIHBhcmFtczogezosfSAgPT89IDQqZF4yOiB7Oix9XHUwMDI3LmZvcm1hdCh0b3RhbF9wYXJhbXMsIDQqZF9tb2RlbCoqMikpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWZmaWNpZW50IEJhdGNoZWQgSGVhZCBDb21wdXRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFB5dGhvbiBsb29wIG92ZXIgaCBoZWFkcyAob25lIGF0dGVudGlvbiBjYWxsIHBlciBoZWFkKSBpcyBjb3JyZWN0IGJ1dCBzbG93LiBUaGUgc3RhbmRhcmQgdHJpY2sgaXMgdG8gcmVzaGFwZSB0aGUgcHJvamVjdGVkIFEsIEssIFYgdGVuc29ycyBmcm9tIChiYXRjaCwgc2VxLCBkX21vZGVsKSB0byAoYmF0Y2gsIGgsIHNlcSwgZOKClikgYW5kIGV4ZWN1dGUgYSBzaW5nbGUgYmF0Y2hlZCBtYXRyaXggbXVsdGlwbHkgYWNyb3NzIGFsbCBoZWFkcyBzaW11bHRhbmVvdXNseS4gVGhpcyBrZWVwcyBHUFUgdXRpbGlzYXRpb24gaGlnaCBhbmQgYXZvaWRzIGggc2VwYXJhdGUga2VybmVsIGxhdW5jaGVzLiBUaGUgcmVzaGFwZSBpcyBPKDEpIOKAlCBpdCByZWludGVycHJldHMgdGhlIG1lbW9yeSBsYXlvdXQgd2l0aG91dCBjb3B5aW5nLiBBZnRlciB0aGUgYmF0Y2hlZCBhdHRlbnRpb24sIHRoZSBoZWFkIG91dHB1dHMgYXJlIHRyYW5zcG9zZWQgYmFjayBhbmQgcmVzaGFwZWQgdG8gKGJhdGNoLCBzZXEsIGjCt2R2KSBiZWZvcmUgdGhlIG91dHB1dCBwcm9qZWN0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG1oYV9iYXRjaGVkKFEsIEssIFYsIFdRLCBXSywgV1YsIFdPLCBoKTpcbiAgICAjIFEsIEssIFY6IChuLCBkX21vZGVsKTsgcmV0dXJucyAobiwgZF9tb2RlbClcbiAgICBuLCBkID0gUS5zaGFwZVxuICAgIGRrID0gZCAvLyBoXG4gICAgIyBQcm9qZWN0IGFuZCBzcGxpdCBpbnRvIGhlYWRzOiAobiwgZCkgLVx1MDAzZSAobiwgaCwgZGspIC1cdTAwM2UgKGgsIG4sIGRrKVxuICAgIFFoID0gKFEgQCBXUSkucmVzaGFwZShuLCBoLCBkaykudHJhbnNwb3NlKDEsIDAsIDIpICAjIChoLCBuLCBkaylcbiAgICBLaCA9IChLIEAgV0spLnJlc2hhcGUobiwgaCwgZGspLnRyYW5zcG9zZSgxLCAwLCAyKVxuICAgIFZoID0gKFYgQCBXVikucmVzaGFwZShuLCBoLCBkaykudHJhbnNwb3NlKDEsIDAsIDIpXG4gICAgIyBCYXRjaGVkIHNjYWxlZCBkb3QtcHJvZHVjdDogKGgsIG4sIGRrKSB4IChoLCBkaywgbikgLVx1MDAzZSAoaCwgbiwgbilcbiAgICBTID0gUWggQCBLaC50cmFuc3Bvc2UoMCwgMiwgMSkgLyBucC5zcXJ0KGRrKVxuICAgIFMgLT0gUy5tYXgoYXhpcz0tMSwga2VlcGRpbXM9VHJ1ZSlcbiAgICBBID0gbnAuZXhwKFMpOyBBIC89IEEuc3VtKGF4aXM9LTEsIGtlZXBkaW1zPVRydWUpICAjIChoLCBuLCBuKVxuICAgICMgVmFsdWUgYWdncmVnYXRpb246IChoLCBuLCBuKSB4IChoLCBuLCBkaykgLVx1MDAzZSAoaCwgbiwgZGspXG4gICAgTyA9IEEgQCBWaCAgICAgICAgICAgICAgICAgICAgICAgICMgKGgsIG4sIGRrKVxuICAgIE8gPSBPLnRyYW5zcG9zZSgxLCAwLCAyKSAgICAgICAgICAjIChuLCBoLCBkaylcbiAgICBPID0gTy5yZXNoYXBlKG4sIGggKiBkaykgICAgICAgICAgIyAobiwgaCpkayA9IGRfbW9kZWwpXG4gICAgcmV0dXJuIE8gQCBXTyAgICAgICAgICAgICAgICAgICAgICMgKG4sIGRfbW9kZWwpXG5cbm5wLnJhbmRvbS5zZWVkKDUpXG5kX21vZGVsLCBoLCBuID0gMjU2LCA4LCAxMlxuV1EgPSBucC5yYW5kb20ucmFuZG4oZF9tb2RlbCwgZF9tb2RlbCkgKiAwLjAyXG5XSyA9IG5wLnJhbmRvbS5yYW5kbihkX21vZGVsLCBkX21vZGVsKSAqIDAuMDJcbldWID0gbnAucmFuZG9tLnJhbmRuKGRfbW9kZWwsIGRfbW9kZWwpICogMC4wMlxuV08gPSBucC5yYW5kb20ucmFuZG4oZF9tb2RlbCwgZF9tb2RlbCkgKiAwLjAyXG54ID0gbnAucmFuZG9tLnJhbmRuKG4sIGRfbW9kZWwpXG5vdXQgPSBtaGFfYmF0Y2hlZCh4LCB4LCB4LCBXUSwgV0ssIFdWLCBXTywgaClcbnByaW50KFx1MDAyN0lucHV0Olx1MDAyNywgeC5zaGFwZSwgXHUwMDI3LVx1MDAzZSBPdXRwdXQ6XHUwMDI3LCBvdXQuc2hhcGUpXG5wcmludChcdTAwMjdObyBQeXRob24gaGVhZCBsb29wIOKAlCBzaW5nbGUgYmF0Y2hlZCBtYXRtdWwgYWNyb3NzIGFsbFx1MDAyNywgaCwgXHUwMDI3aGVhZHMuXHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IHRoZSBSZXNoYXBlIFRyaWNrIFdvcmtzIiwiY29udGVudCI6IkFmdGVyIHByb2plY3RpbmcgUSB0byBzaGFwZSAobiwgZF9tb2RlbCksIHJlc2hhcGluZyB0byAobiwgaCwgZOKClikgYW5kIHRyYW5zcG9zaW5nIHRvIChoLCBuLCBk4oKWKSByZWFycmFuZ2VzIG1lbW9yeSBzdWNoIHRoYXQgZWFjaCBzbGljZSBbaSwgOiwgOl0gYWxvbmcgdGhlIGZpcnN0IGF4aXMgY29ycmVzcG9uZHMgZXhhY3RseSB0byBoZWFkIGlcdTAwMjdzIHByb2plY3RlZCBxdWVyaWVzLiBOdW1QeSBhbmQgUHlUb3JjaFx1MDAyN3MgYmF0Y2hlZCBtYXRtdWwgdGhlbiBwcm9jZXNzZXMgYWxsIGggc2xpY2VzIGluIG9uZSBHUFUga2VybmVsIGNhbGwsIHJlcGxhY2luZyBoIHNlcGFyYXRlIGF0dGVudGlvbiBrZXJuZWxzIHdpdGggYSBzaW5nbGUgb25lIOKAlCB0aGUgc2FtZSBGTE9QIGNvdW50IGJ1dCBmYXIgYmV0dGVyIGhhcmR3YXJlIHV0aWxpc2F0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhlYWQgU3BlY2lhbGlzYXRpb24gVmlzdWFsaXNhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlmZmVyZW50IGF0dGVudGlvbiBoZWFkcyB0ZW5kIHRvIGxlYXJuIHF1YWxpdGF0aXZlbHkgZGlmZmVyZW50IHBhdHRlcm5zLiBBIGhlYWQgd2l0aCBoaWdoIGRpYWdvbmFsIG1lYW4gYXR0ZW5kcyBzdHJvbmdseSB0byB0aGUgcXVlcnkgdG9rZW4gaXRzZWxmIChzZWxmLWZvY3VzKS4gQSBoZWFkIHdpdGggbG93IGVudHJvcHkgYXR0ZW5kcyB0byBhIHNtYWxsIGZpeGVkIHNldCBvZiBwb3NpdGlvbnMgKHNlbGVjdGl2ZSByZXRyaWV2YWwpLiBBIGhlYWQgd2l0aCBuZWFyLXVuaWZvcm0gd2VpZ2h0cyBhZ2dyZWdhdGVzIGNvbnRleHR1YWwgaW5mb3JtYXRpb24gYnJvYWRseS4gUXVhbnRpZnlpbmcgdGhlc2UgcGVyLWhlYWQgc3RhdGlzdGljcyDigJQgZGlhZ29uYWwgY29uY2VudHJhdGlvbiwgZW50cm9weSwgYW5kIG9mZi1kaWFnb25hbCBkaXN0cmlidXRpb24g4oCUIGlzIGEgbGlnaHR3ZWlnaHQgZGlhZ25vc3RpYyBmb3IgdW5kZXJzdGFuZGluZyB3aGF0IGEgdHJhaW5lZCBUcmFuc2Zvcm1lciBoYXMgbGVhcm5lZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuZF9tb2RlbCwgaCwgc2VxX2xlbiA9IDI1NiwgOCwgMTJcbm1oYSA9IG5uLk11bHRpaGVhZEF0dGVudGlvbihkX21vZGVsLCBoLCBiYXRjaF9maXJzdD1UcnVlKVxuV1EsIFdLLCBXViA9IG1oYS5pbl9wcm9qX3dlaWdodC5jaHVuaygzLCBkaW09MClcbmRrID0gZF9tb2RlbCAvLyBoXG5cbmRlZiBoZWFkX2F0dGVudGlvbl93ZWlnaHRzKHhfZmxhdCwgaGVhZF9pZHgpOlxuICAgICMgeF9mbGF0OiAoc2VxLCBkX21vZGVsKSDigJQgc2luZ2xlIHNhbXBsZVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBRID0gKHhfZmxhdCBAIFdRLlQpWzosIGhlYWRfaWR4KmRrOihoZWFkX2lkeCsxKSpka11cbiAgICAgICAgSyA9ICh4X2ZsYXQgQCBXSy5UKVs6LCBoZWFkX2lkeCpkazooaGVhZF9pZHgrMSkqZGtdXG4gICAgICAgIFMgPSAoUSBAIEsuVCAvIGRrKiowLjUpLm51bXB5KClcbiAgICBTIC09IFMubWF4KDEsIGtlZXBkaW1zPVRydWUpXG4gICAgQSA9IG5wLmV4cChTKTsgQSAvPSBBLnN1bSgxLCBrZWVwZGltcz1UcnVlKVxuICAgIHJldHVybiBBXG5cbnggPSB0b3JjaC5yYW5kbigxLCBzZXFfbGVuLCBkX21vZGVsKVxueF9mbGF0ID0geC5zcXVlZXplKDApXG5wcmludChcdTAwMjd7Olx1MDAzZTZ9IHs6XHUwMDNlMTB9IHs6XHUwMDNlMTN9IHs6XHUwMDNlMTB9XHUwMDI3LmZvcm1hdChcdTAwMjdIZWFkXHUwMDI3LCBcdTAwMjdEaWFnTWVhblx1MDAyNywgXHUwMDI3T2ZmRGlhZ01lYW5cdTAwMjcsIFx1MDAyN0VudHJvcHlcdTAwMjcpKVxuZm9yIGkgaW4gcmFuZ2UoaCk6XG4gICAgQSA9IGhlYWRfYXR0ZW50aW9uX3dlaWdodHMoeF9mbGF0LCBpKVxuICAgIGRpYWcgPSBucC5kaWFnKEEpLm1lYW4oKVxuICAgIG9mZiAgPSAoQS5zdW0oKSAtIG5wLnRyYWNlKEEpKSAvIChzZXFfbGVuICogKHNlcV9sZW4gLSAxKSlcbiAgICBlbnQgID0gLShBICogbnAubG9nKEEgKyAxZS05KSkuc3VtKDEpLm1lYW4oKVxuICAgIHByaW50KFx1MDAyN3s6XHUwMDNlNn0gezpcdTAwM2UxMC40Zn0gezpcdTAwM2UxMy40Zn0gezpcdTAwM2UxMC40Zn1cdTAwMjcuZm9ybWF0KGksIGRpYWcsIG9mZiwgZW50KSlcbnByaW50KFx1MDAyN0hpZ2ggRGlhZ01lYW4gPSBzZWxmLWZvY3VzZWQgaGVhZC4gTG93IGVudHJvcHkgPSBzZWxlY3RpdmUgaGVhZC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGFyYW1ldGVyIENvdW50IGFuZCBIeXBlcnBhcmFtZXRlciBEZXNpZ24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldpdGggZF9tb2RlbCBhbmQgaCBoZWFkcywgZWFjaCBoZWFkIGhhcyBX4bWiUSwgV+G1oksg4oiIIOKEnV57ZF9tb2RlbMOXZOKCln0gYW5kIFfhtaJWIOKIiCDihJ1ee2RfbW9kZWzDl2R2fS4gU3VtbWluZyBvdmVyIGggaGVhZHMgYW5kIGFkZGluZyBX4bS8OiB0b3RhbCA9IGjCt2RfbW9kZWzCt2TigpYgKyBowrdkX21vZGVswrdk4oKWICsgaMK3ZF9tb2RlbMK3ZHYgKyAoaMK3ZHYpwrdkX21vZGVsID0gNMK3ZF9tb2RlbMKyIHdoZW4gZOKClj1kdj1kX21vZGVsL2guIFRoaXMgbWVhbnMgdGhlIHBhcmFtZXRlciBjb3VudCBpcyBpbmRlcGVuZGVudCBvZiB0aGUgbnVtYmVyIG9mIGhlYWRzIOKAlCBhbiA4LWhlYWQgYW5kIDE2LWhlYWQgTUhBIHdpdGggdGhlIHNhbWUgZF9tb2RlbCBoYXZlIHRoZSBzYW1lIHBhcmFtZXRlciBidWRnZXQuIEluY3JlYXNpbmcgaCByZWRpc3RyaWJ1dGVzIHBhcmFtZXRlcnMgaW50byBtb3JlLCBuYXJyb3dlciBwcm9qZWN0aW9uIG1hdHJpY2VzIHJhdGhlciB0aGFuIGFkZGluZyBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJIeXBlcnBhcmFtZXRlciIsIkdQVC0yIFNtYWxsIiwiQkVSVC1CYXNlIChvcmlnaW5hbCkiLCJHUFQtMyAxNzVCIChwZXIgbGF5ZXIpIiwiUm9sZSJdLCJyb3dzIjpbWyJkX21vZGVsIiwiNzY4IiwiNTEyIiwiMTIyODgiLCJSZXNpZHVhbCBzdHJlYW0gZGltZW5zaW9uIl0sWyJoIChoZWFkcykiLCIxMiIsIjgiLCI5NiIsIk51bWJlciBvZiBhdHRlbnRpb24gaGVhZHMiXSxbImTigpYgPSBkdiA9IGRfbW9kZWwvaCIsIjY0IiwiNjQiLCIxMjgiLCJQZXItaGVhZCBrZXkvdmFsdWUgZGltZW5zaW9uIl0sWyJUb3RhbCBNSEEgcGFyYW1zIiwi4omIMi40TSIsIuKJiDEuME0iLCLiiYg2MDNNIiwiQWx3YXlzIDQgw5cgZF9tb2RlbMKyIl0sWyJNYXggc2VxdWVuY2UgbGVuZ3RoIiwiMTAyNCIsIjUxMiIsIjIwNDgiLCJEZXRlcm1pbmVzIE8obsKyZCkgY29zdCJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJoIG11c3QgZXZlbmx5IGRpdmlkZSBkX21vZGVsIHNvIGVhY2ggaGVhZCBnZXRzIGRpbWVuc2lvbiBkX21vZGVsL2giLCJMYXJnZXIgaCB3aXRoIHNhbWUgZF9tb2RlbDogbW9yZSBoZWFkcyB3aXRoIG5hcnJvd2VyIHByb2plY3Rpb25zIOKAlCBtb3JlIGRpdmVyc2UgcGF0dGVybnMgYnV0IGxlc3MgY2FwYWNpdHkgcGVyIGhlYWQiLCJFbXBpcmljYWwgc3dlZXQgc3BvdDogZOKCliDiiaUgMzIgcGVyIGhlYWQ7IGJlbG93IHRoaXMgaGVhZHMgYXJlIHRvbyBuYXJyb3cgdG8gYmUgZXhwcmVzc2l2ZSIsIldlaWdodCB0eWluZzogc29tZSBhcmNoaXRlY3R1cmVzIChUNSkgc2hhcmUgV1EgYW5kIFdLIGFjcm9zcyBoZWFkcyBvciBsYXllcnMgdG8gc2F2ZSBwYXJhbWV0ZXJzIiwiR3JvdXBlZCBRdWVyeSBBdHRlbnRpb24gKEdRQSwgQWluc2xpZSBldCBhbC4gMjAyMyk6IGggcXVlcnkgaGVhZHMgc2hhcmUgZyBcdTAwM2MgaCBrZXktdmFsdWUgaGVhZCBwYWlycyB0byByZWR1Y2UgS1YgY2FjaGUgc2l6ZSBhdCBpbmZlcmVuY2UgdGltZSJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Multi-Head Attention — Parallel Heads and Projection

Multi-Head Attention (MHA) runs h independent scaled dot-product attention operations in parallel, each on a lower-dimensional projection of the input. The outputs are concatenated and projected back to the model dimension. This allows the model to jointly attend to information from h different representation subspaces — a richer and more expressive operation than a single large attention head operating on the full dimension.

## MHA Formula and Structure

For head i, the query, key, and value projections are Qᵢ = QWᵢQ, Kᵢ = KWᵢK, Vᵢ = VWᵢV where WᵢQ, WᵢK ∈ ℝ^{d_model×dₖ} and WᵢV ∈ ℝ^{d_model×dv}. Each head computes headᵢ = Attention(Qᵢ, Kᵢ, Vᵢ) ∈ ℝ^{nq×dv}. The h head outputs are concatenated along the last axis to get ℝ^{nq×(h·dv)}, then projected by Wᴼ ∈ ℝ^{(h·dv)×d_model}. With the standard choice h=8, dₖ=dv=d_model/h=64, the total parameter count in the four projection matrices is 4·d_model².

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,\ldots,\text{head}_h)W^O, \quad \text{head}_i = \text{Attention}(QW_i^Q,\, KW_i^K,\, VW_i^V)$$

## Projection Matrices — Why They Matter

Without projection matrices, MHA would simply split Q, K, V along the feature axis and run attention on each chunk. The projections allow each head to learn its own transformation of the input before computing similarities — head i can learn to extract syntactic features, head j semantic features, without interference. The output projection Wᴼ mixes the h head outputs and maps back to d_model so the residual addition x + MHA(x) remains shape-preserving. Initialising projections with small random values (scale ~ 1/√d_model) is crucial for stable training.

```python
import numpy as np

def sdp(Q, K, V):
    dk = Q.shape[-1]
    S = Q @ K.T / np.sqrt(dk)
    S -= S.max(axis=-1, keepdims=True)
    A = np.exp(S); A /= A.sum(axis=-1, keepdims=True)
    return A @ V

class MultiHeadAttention:
    def __init__(self, d_model, h, seed=0):
        self.h = h
        self.dk = self.dv = d_model // h
        rng = np.random.RandomState(seed)
        scale = np.sqrt(2.0 / d_model)
        self.WQ = rng.randn(h, d_model, self.dk) * scale
        self.WK = rng.randn(h, d_model, self.dk) * scale
        self.WV = rng.randn(h, d_model, self.dv) * scale
        self.WO = rng.randn(h * self.dv, d_model) * scale

    def forward(self, Q, K, V):
        heads = []
        for i in range(self.h):
            Qi = Q @ self.WQ[i]   # (nq, dk)
            Ki = K @ self.WK[i]   # (nk, dk)
            Vi = V @ self.WV[i]   # (nk, dv)
            heads.append(sdp(Qi, Ki, Vi))    # (nq, dv)
        concat = np.concatenate(heads, axis=-1)  # (nq, h*dv)
        return concat @ self.WO                  # (nq, d_model)

np.random.seed(42)
d_model, h, n = 512, 8, 10
mha = MultiHeadAttention(d_model, h)
x = np.random.randn(n, d_model)
out = mha.forward(x, x, x)
print('Input: ', x.shape, '-> Output:', out.shape)
params = h * (d_model * (d_model//h) * 3) + (h * (d_model//h)) * d_model
print('Total params: {:,} == 4*d_model^2: {:,}'.format(params, 4 * d_model**2))
```

## PyTorch nn.MultiheadAttention

PyTorch fuses the three input projection matrices WQ, WK, WV into a single in_proj_weight of shape (3·d_model, d_model) for efficiency — a single GEMM replaces three. The batch_first=True flag selects the (batch, seq, d_model) convention; the default is (seq, batch, d_model). For cross-attention, pass the decoder states as query and the encoder output as key and value. The returned attn_weights tensor averages attention weights across heads by default; pass average_attn_weights=False to get per-head weights (PyTorch ≥ 1.13).

```python
import torch
import torch.nn as nn

torch.manual_seed(42)
d_model, h, seq_len, batch = 512, 8, 10, 2

mha = nn.MultiheadAttention(
    embed_dim=d_model,
    num_heads=h,
    batch_first=True,
    dropout=0.0
)

# Self-attention: Q = K = V = x
x = torch.randn(batch, seq_len, d_model)
out, attn_w = mha(x, x, x)
print('Input:', tuple(x.shape))
print('Output:', tuple(out.shape))
print('Attn weights (avg across heads):', tuple(attn_w.shape))
print('Row sums:', attn_w[0].sum(dim=-1).round(decimals=4))

# Cross-attention: decoder queries attend to encoder key-value
dec_len, enc_len = 6, 15
q   = torch.randn(batch, dec_len, d_model)
kv  = torch.randn(batch, enc_len, d_model)
out_cross, cross_w = mha(q, kv, kv)
print('Cross-attn output:', tuple(out_cross.shape))
print('Cross-attn weights:', tuple(cross_w.shape), '(dec_len x enc_len)')

total_params = sum(p.numel() for p in mha.parameters())
print('Total MHA params: {:,}  =?= 4*d^2: {:,}'.format(total_params, 4*d_model**2))
```

## Efficient Batched Head Computation

The Python loop over h heads (one attention call per head) is correct but slow. The standard trick is to reshape the projected Q, K, V tensors from (batch, seq, d_model) to (batch, h, seq, dₖ) and execute a single batched matrix multiply across all heads simultaneously. This keeps GPU utilisation high and avoids h separate kernel launches. The reshape is O(1) — it reinterprets the memory layout without copying. After the batched attention, the head outputs are transposed back and reshaped to (batch, seq, h·dv) before the output projection.

```python
import numpy as np

def mha_batched(Q, K, V, WQ, WK, WV, WO, h):
    # Q, K, V: (n, d_model); returns (n, d_model)
    n, d = Q.shape
    dk = d // h
    # Project and split into heads: (n, d) -> (n, h, dk) -> (h, n, dk)
    Qh = (Q @ WQ).reshape(n, h, dk).transpose(1, 0, 2)  # (h, n, dk)
    Kh = (K @ WK).reshape(n, h, dk).transpose(1, 0, 2)
    Vh = (V @ WV).reshape(n, h, dk).transpose(1, 0, 2)
    # Batched scaled dot-product: (h, n, dk) x (h, dk, n) -> (h, n, n)
    S = Qh @ Kh.transpose(0, 2, 1) / np.sqrt(dk)
    S -= S.max(axis=-1, keepdims=True)
    A = np.exp(S); A /= A.sum(axis=-1, keepdims=True)  # (h, n, n)
    # Value aggregation: (h, n, n) x (h, n, dk) -> (h, n, dk)
    O = A @ Vh                        # (h, n, dk)
    O = O.transpose(1, 0, 2)          # (n, h, dk)
    O = O.reshape(n, h * dk)          # (n, h*dk = d_model)
    return O @ WO                     # (n, d_model)

np.random.seed(5)
d_model, h, n = 256, 8, 12
WQ = np.random.randn(d_model, d_model) * 0.02
WK = np.random.randn(d_model, d_model) * 0.02
WV = np.random.randn(d_model, d_model) * 0.02
WO = np.random.randn(d_model, d_model) * 0.02
x = np.random.randn(n, d_model)
out = mha_batched(x, x, x, WQ, WK, WV, WO, h)
print('Input:', x.shape, '-> Output:', out.shape)
print('No Python head loop — single batched matmul across all', h, 'heads.')
```

> **Why the Reshape Trick Works**: After projecting Q to shape (n, d_model), reshaping to (n, h, dₖ) and transposing to (h, n, dₖ) rearranges memory such that each slice [i, :, :] along the first axis corresponds exactly to head i's projected queries. NumPy and PyTorch's batched matmul then processes all h slices in one GPU kernel call, replacing h separate attention kernels with a single one — the same FLOP count but far better hardware utilisation.

## Head Specialisation Visualisation

Different attention heads tend to learn qualitatively different patterns. A head with high diagonal mean attends strongly to the query token itself (self-focus). A head with low entropy attends to a small fixed set of positions (selective retrieval). A head with near-uniform weights aggregates contextual information broadly. Quantifying these per-head statistics — diagonal concentration, entropy, and off-diagonal distribution — is a lightweight diagnostic for understanding what a trained Transformer has learned.

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(0)
d_model, h, seq_len = 256, 8, 12
mha = nn.MultiheadAttention(d_model, h, batch_first=True)
WQ, WK, WV = mha.in_proj_weight.chunk(3, dim=0)
dk = d_model // h

def head_attention_weights(x_flat, head_idx):
    # x_flat: (seq, d_model) — single sample
    with torch.no_grad():
        Q = (x_flat @ WQ.T)[:, head_idx*dk:(head_idx+1)*dk]
        K = (x_flat @ WK.T)[:, head_idx*dk:(head_idx+1)*dk]
        S = (Q @ K.T / dk**0.5).numpy()
    S -= S.max(1, keepdims=True)
    A = np.exp(S); A /= A.sum(1, keepdims=True)
    return A

x = torch.randn(1, seq_len, d_model)
x_flat = x.squeeze(0)
print('{:>6} {:>10} {:>13} {:>10}'.format('Head', 'DiagMean', 'OffDiagMean', 'Entropy'))
for i in range(h):
    A = head_attention_weights(x_flat, i)
    diag = np.diag(A).mean()
    off  = (A.sum() - np.trace(A)) / (seq_len * (seq_len - 1))
    ent  = -(A * np.log(A + 1e-9)).sum(1).mean()
    print('{:>6} {:>10.4f} {:>13.4f} {:>10.4f}'.format(i, diag, off, ent))
print('High DiagMean = self-focused head. Low entropy = selective head.')
```

## Parameter Count and Hyperparameter Design

With d_model and h heads, each head has WᵢQ, WᵢK ∈ ℝ^{d_model×dₖ} and WᵢV ∈ ℝ^{d_model×dv}. Summing over h heads and adding Wᴼ: total = h·d_model·dₖ + h·d_model·dₖ + h·d_model·dv + (h·dv)·d_model = 4·d_model² when dₖ=dv=d_model/h. This means the parameter count is independent of the number of heads — an 8-head and 16-head MHA with the same d_model have the same parameter budget. Increasing h redistributes parameters into more, narrower projection matrices rather than adding parameters.

| Hyperparameter | GPT-2 Small | BERT-Base (original) | GPT-3 175B (per layer) | Role |
| --- | --- | --- | --- | --- |
| d_model | 768 | 512 | 12288 | Residual stream dimension |
| h (heads) | 12 | 8 | 96 | Number of attention heads |
| dₖ = dv = d_model/h | 64 | 64 | 128 | Per-head key/value dimension |
| Total MHA params | ≈2.4M | ≈1.0M | ≈603M | Always 4 × d_model² |
| Max sequence length | 1024 | 512 | 2048 | Determines O(n²d) cost |

- h must evenly divide d_model so each head gets dimension d_model/h
- Larger h with same d_model: more heads with narrower projections — more diverse patterns but less capacity per head
- Empirical sweet spot: dₖ ≥ 32 per head; below this heads are too narrow to be expressive
- Weight tying: some architectures (T5) share WQ and WK across heads or layers to save parameters
- Grouped Query Attention (GQA, Ainslie et al. 2023): h query heads share g < h key-value head pairs to reduce KV cache size at inference time

---

