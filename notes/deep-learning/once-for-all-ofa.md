---
title: "Once-for-All — Train Once, Deploy Many Architectures"
slug: "once-for-all-ofa"
description: "OFA trains a single supernet with elastic kernel, depth, and width so any subnet can be extracted for any hardware target without retraining. Covers progressive shrinking, in-place distillation, elastic kernel sharing, subnet search with latency lookup tables, and comparison with MobileNetV3 and DARTS."
tags: ["deep-learning", "model-compression", "pruning", "quantization"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgTkFTIGZpbmRzIG9uZSBhcmNoaXRlY3R1cmUgcGVyIGhhcmR3YXJlIHRhcmdldC4gRGVwbG95aW5nIGEgbW9kZWwgdG8gMTAgZGlmZmVyZW50IGRldmljZXMgKHBob25lLCB0YWJsZXQsIHNlcnZlciwgSW9UKSByZXF1aXJlcyAxMCBzZXBhcmF0ZSBOQVMgcnVucywgZWFjaCBwb3RlbnRpYWxseSBkYXlzIG9mIGNvbXB1dGUuIE9uY2UtZm9yLUFsbCAoT0ZBLCBDYWkgZXQgYWwuIDIwMjApIGRlY291cGxlcyB0cmFpbmluZyBmcm9tIHNlYXJjaDogYSBzaW5nbGUgc3VwZXJuZXQgaXMgdHJhaW5lZCBvbmNlLCBhbmQgYXJiaXRyYXJ5IHN1Ym5ldHMg4oCUIGRlZmluZWQgYnkgZGVwdGgsIHdpZHRoLCBrZXJuZWwgc2l6ZSwgYW5kIHJlc29sdXRpb24g4oCUIGNhbiBiZSBleHRyYWN0ZWQgYW5kIGRlcGxveWVkIHdpdGhvdXQgYW55IHJldHJhaW5pbmcuIEVhY2ggc3VibmV0IGFjaGlldmVzIGFjY3VyYWN5IGNsb3NlIHRvIHRoZSBlcXVpdmFsZW50IHN0YW5kYWxvbmUgbW9kZWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT0ZBIFNlYXJjaCBTcGFjZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIE9GQSBzdXBlcm5ldCBpcyBidWlsdCBmcm9tIE1vYmlsZU5ldFYzLWxpa2UgaW52ZXJ0ZWQgcmVzaWR1YWwgYmxvY2tzLiBUaGUgZWxhc3RpYyBkaW1lbnNpb25zIGFyZTogKDEpIGtlcm5lbCBzaXplIHBlciBsYXllciDiiIggezMsIDUsIDd9LCAoMikgZGVwdGggKG51bWJlciBvZiBibG9ja3MgcGVyIHN0YWdlKSDiiIggezIsIDMsIDR9LCAoMykgZXhwYW5kIHJhdGlvICh3aWR0aCBtdWx0aXBsaWVyIGluc2lkZSBibG9ja3MpIOKIiCB7MywgNCwgNn0sIGFuZCAoNCkgaW5wdXQgcmVzb2x1dGlvbiDiiIggezEyOCwgMTYwLCAxOTIsIDIyNH0uIFRoZSB0b3RhbCBudW1iZXIgb2YgcG9zc2libGUgc3VibmV0cyBleGNlZWRzIDEwXjE5LCBjb3ZlcmluZyBhIGNvbnRpbnVvdXMgUGFyZXRvIGZyb250aWVyIGZyb20gMTUwTSB0byA2MDBNIEZMT1BzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVsYXN0aWMgS2VybmVsIFNoYXJpbmcifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgRWxhc3RpY0tlcm5lbENvbnYobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJcbiAgICBBIHNpbmdsZSBjb252IHdlaWdodCBvZiBzaXplIDd4NyB0aGF0IGNhbiBhY3QgYXMgN3g3LCA1eDUsIG9yIDN4M1xuICAgIGJ5IGV4dHJhY3RpbmcgdGhlIGNlbnRlciBzdWIta2VybmVsIChzaGFyZWQgd2VpZ2h0cykuXG4gICAgXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2hhbm5lbHM6IGludCwgb3V0X2NoYW5uZWxzOiBpbnQsIG1heF9rZXJuZWw6IGludCA9IDcpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgYXNzZXJ0IG1heF9rZXJuZWwgaW4gKDcsIDUsIDMpLCBcdTAwMjdtYXhfa2VybmVsIG11c3QgYmUgNywgNSwgb3IgM1x1MDAyN1xuICAgICAgICBzZWxmLm1heF9rZXJuZWwgPSBtYXhfa2VybmVsXG4gICAgICAgICMgQWxsIGtlcm5lbCBzaXplcyBzaGFyZSBmcm9tIHRoaXMgc2luZ2xlIHdlaWdodCB0ZW5zb3JcbiAgICAgICAgc2VsZi53ZWlnaHQgPSBubi5QYXJhbWV0ZXIoXG4gICAgICAgICAgICB0b3JjaC5yYW5kbihvdXRfY2hhbm5lbHMsIGluX2NoYW5uZWxzLCBtYXhfa2VybmVsLCBtYXhfa2VybmVsKVxuICAgICAgICAgICAgKiAoMiAvIChpbl9jaGFubmVscyAqIG1heF9rZXJuZWwgKiogMikpICoqIDAuNVxuICAgICAgICApXG4gICAgICAgIHNlbGYuYmlhcyA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcyhvdXRfY2hhbm5lbHMpKVxuICAgICAgICAjIExlYXJuYWJsZSB0cmFuc2Zvcm1hdGlvbiBtYXRyaWNlcyB0byBhZGFwdCBjZW50ZXIga2VybmVsIGZvciBzbWFsbGVyIHNpemVzXG4gICAgICAgIHNlbGYudHJhbnNmb3JtcyA9IG5uLlBhcmFtZXRlckRpY3QoKVxuICAgICAgICBmb3Iga3MgaW4gW2sgZm9yIGsgaW4gWzMsIDUsIDddIGlmIGsgXHUwMDNjIG1heF9rZXJuZWxdOlxuICAgICAgICAgICAgc2VsZi50cmFuc2Zvcm1zW3N0cihrcyldID0gbm4uUGFyYW1ldGVyKHRvcmNoLmV5ZShrcyAqIGtzKSlcblxuICAgIGRlZiBfZXh0cmFjdF9zdWJfa2VybmVsKHNlbGYsIGtlcm5lbF9zaXplOiBpbnQpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBpZiBrZXJuZWxfc2l6ZSA9PSBzZWxmLm1heF9rZXJuZWw6XG4gICAgICAgICAgICByZXR1cm4gc2VsZi53ZWlnaHRcbiAgICAgICAgIyBFeHRyYWN0IGNlbnRlciBjcm9wXG4gICAgICAgIHN0YXJ0ID0gKHNlbGYubWF4X2tlcm5lbCAtIGtlcm5lbF9zaXplKSAvLyAyXG4gICAgICAgIHN1YiA9IHNlbGYud2VpZ2h0WzosIDosIHN0YXJ0OnN0YXJ0K2tlcm5lbF9zaXplLCBzdGFydDpzdGFydCtrZXJuZWxfc2l6ZV1cbiAgICAgICAgIyBBcHBseSBsZWFybmVkIGxpbmVhciB0cmFuc2Zvcm1hdGlvbiAoc2hhcGUtcHJlc2VydmluZylcbiAgICAgICAgQ19vdXQsIENfaW4gPSBzdWIuc2hhcGVbOjJdXG4gICAgICAgIHN1Yl9mbGF0ID0gc3ViLnJlc2hhcGUoQ19vdXQgKiBDX2luLCAtMSkgICMgKC4uLiwga3Mqa3MpXG4gICAgICAgIFQgPSBzZWxmLnRyYW5zZm9ybXNbc3RyKGtlcm5lbF9zaXplKV0gICAgICAjIChrcyprcywga3Mqa3MpXG4gICAgICAgIHN1Yl90cmFuc2Zvcm1lZCA9IChzdWJfZmxhdCBAIFQpLnJlc2hhcGUoQ19vdXQsIENfaW4sIGtlcm5lbF9zaXplLCBrZXJuZWxfc2l6ZSlcbiAgICAgICAgcmV0dXJuIHN1Yl90cmFuc2Zvcm1lZFxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yLCBrZXJuZWxfc2l6ZTogaW50ID0gTm9uZSkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIGlmIGtlcm5lbF9zaXplIGlzIE5vbmU6XG4gICAgICAgICAgICBrZXJuZWxfc2l6ZSA9IHNlbGYubWF4X2tlcm5lbFxuICAgICAgICBXID0gc2VsZi5fZXh0cmFjdF9zdWJfa2VybmVsKGtlcm5lbF9zaXplKVxuICAgICAgICBwYWQgPSBrZXJuZWxfc2l6ZSAvLyAyXG4gICAgICAgIHJldHVybiBGLmNvbnYyZCh4LCBXLCBzZWxmLmJpYXMsIHBhZGRpbmc9cGFkKVxuXG4jIERlbW86IHNhbWUgd2VpZ2h0cywgZGlmZmVyZW50IGtlcm5lbCBzaXplc1xuZWxhc3RpY19jb252ID0gRWxhc3RpY0tlcm5lbENvbnYoMTYsIDMyLCBtYXhfa2VybmVsPTcpXG54ID0gdG9yY2gucmFuZG4oMiwgMTYsIDgsIDgpXG5mb3Iga3MgaW4gWzMsIDUsIDddOlxuICAgIG91dCA9IGVsYXN0aWNfY29udih4LCBrZXJuZWxfc2l6ZT1rcylcbiAgICBwcmludChmXHUwMDI3a2VybmVsX3NpemU9e2tzfTogaW5wdXQge3guc2hhcGV9IC1cdTAwM2Ugb3V0cHV0IHtvdXQuc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByb2dyZXNzaXZlIFNocmlua2luZyBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhaW5pbmcgdGhlIGZ1bGwgc3VwZXJuZXQgZnJvbSBzY3JhdGNoIGlzIGRpZmZpY3VsdDogYWxsIHN1Ym5ldHMgc2hhcmUgd2VpZ2h0cywgYW5kIHNtYWxsIHN1Ym5ldHMgaW50ZXJmZXJlIHdpdGggbGFyZ2Ugb25lcy4gUHJvZ3Jlc3NpdmUgc2hyaW5raW5nIHNvbHZlcyB0aGlzIGJ5IHRyYWluaW5nIGluIHN0YWdlczogKDEpIHRyYWluIHRoZSBmdWxsIG5ldHdvcmsgKGxhcmdlc3Qga2VybmVsLCBtb3N0IGxheWVycywgd2lkZXN0IGV4cGFuZCByYXRpbykgdG8gY29udmVyZ2VuY2U7ICgyKSBhZGQgZWxhc3RpYyBrZXJuZWwgYnkgdHJhaW5pbmcgd2l0aCByYW5kb21seSBzYW1wbGVkIGtlcm5lbCBzaXplcyB3aGlsZSBkaXN0aWxsaW5nIGZyb20gdGhlIGZ1bGwta2VybmVsIHN1Ym5ldDsgKDMpIGFkZCBlbGFzdGljIGRlcHRoIGJ5IHJhbmRvbWx5IGRyb3BwaW5nIGxheWVyczsgKDQpIGFkZCBlbGFzdGljIHdpZHRoLiBFYWNoIHN0YWdlIHVzZXMgaW4tcGxhY2Uga25vd2xlZGdlIGRpc3RpbGxhdGlvbjogdGhlIHRlYWNoZXIgaXMgdGhlIHNhbWUgc3VwZXJuZXQgZXZhbHVhdGVkIHdpdGggdGhlIGN1cnJlbnQgc3RhZ2VcdTAwMjdzIG1heGltdW0gY29uZmlndXJhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCByYW5kb21cblxuZGVmIHByb2dyZXNzaXZlX3Nocmlua2luZ19zdGVwKHN1cGVybmV0LCB4LCB5X3RydWUsIGNyaXRlcmlvbixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdGFnZT1cdTAwMjdrZXJuZWxcdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAga2VybmVsX2Nob2ljZXM9KDMsIDUsIDcpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRlcHRoX2Nob2ljZXM9KDIsIDMsIDQpKTpcbiAgICBcIlwiXCJcbiAgICBPbmUgdHJhaW5pbmcgc3RlcCB3aXRoIHByb2dyZXNzaXZlIHNocmlua2luZyBhbmQgaW4tcGxhY2UgZGlzdGlsbGF0aW9uLlxuICAgIFRlYWNoZXI6IHN1cGVybmV0IHdpdGggbWF4IGNvbmZpZy4gU3R1ZGVudDogcmFuZG9tIHNtYWxsZXIgY29uZmlnLlxuICAgIFwiXCJcIlxuICAgIHN1cGVybmV0LmV2YWwoKVxuICAgICMgVGVhY2hlciBmb3J3YXJkOiBhbHdheXMgbWF4IGNvbmZpZ1xuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICB0ZWFjaGVyX2xvZ2l0cyA9IHN1cGVybmV0KHgsIGtlcm5lbF9zaXplPW1heChrZXJuZWxfY2hvaWNlcyksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGVwdGg9bWF4KGRlcHRoX2Nob2ljZXMpKVxuICAgICAgICB0ZWFjaGVyX3Byb2JzID0gRi5zb2Z0bWF4KHRlYWNoZXJfbG9naXRzIC8gNC4wLCBkaW09LTEpICAjIFQ9NCB0ZW1wZXJhdHVyZVxuXG4gICAgc3VwZXJuZXQudHJhaW4oKVxuICAgICMgU3R1ZGVudCBmb3J3YXJkOiByYW5kb20gc21hbGxlciBjb25maWdcbiAgICBpZiBzdGFnZSA9PSBcdTAwMjdrZXJuZWxcdTAwMjc6XG4gICAgICAgIGtzID0gcmFuZG9tLmNob2ljZShrZXJuZWxfY2hvaWNlcylcbiAgICAgICAgc3R1ZGVudF9sb2dpdHMgPSBzdXBlcm5ldCh4LCBrZXJuZWxfc2l6ZT1rcywgZGVwdGg9bWF4KGRlcHRoX2Nob2ljZXMpKVxuICAgIGVsaWYgc3RhZ2UgPT0gXHUwMDI3ZGVwdGhcdTAwMjc6XG4gICAgICAgIGtzID0gcmFuZG9tLmNob2ljZShrZXJuZWxfY2hvaWNlcylcbiAgICAgICAgZCA9IHJhbmRvbS5jaG9pY2UoZGVwdGhfY2hvaWNlcylcbiAgICAgICAgc3R1ZGVudF9sb2dpdHMgPSBzdXBlcm5ldCh4LCBrZXJuZWxfc2l6ZT1rcywgZGVwdGg9ZClcbiAgICBlbHNlOlxuICAgICAgICBzdHVkZW50X2xvZ2l0cyA9IHN1cGVybmV0KHgsIGtlcm5lbF9zaXplPW1heChrZXJuZWxfY2hvaWNlcyksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGVwdGg9bWF4KGRlcHRoX2Nob2ljZXMpKVxuXG4gICAgIyBDb21iaW5lZCBsb3NzOiB0YXNrIGxvc3MgKyBLRCBsb3NzIGZyb20gdGVhY2hlclxuICAgIHRhc2tfbG9zcyA9IGNyaXRlcmlvbihzdHVkZW50X2xvZ2l0cywgeV90cnVlKVxuICAgIGtkX2xvc3MgPSBGLmtsX2RpdihcbiAgICAgICAgRi5sb2dfc29mdG1heChzdHVkZW50X2xvZ2l0cyAvIDQuMCwgZGltPS0xKSxcbiAgICAgICAgdGVhY2hlcl9wcm9icyxcbiAgICAgICAgcmVkdWN0aW9uPVx1MDAyN2JhdGNobWVhblx1MDAyN1xuICAgICkgKiAoNC4wICoqIDIpICAjIHNjYWxlIGJ5IFReMlxuXG4gICAgdG90YWxfbG9zcyA9IDAuNSAqIHRhc2tfbG9zcyArIDAuNSAqIGtkX2xvc3NcbiAgICByZXR1cm4gdG90YWxfbG9zcywgdGFza19sb3NzLml0ZW0oKSwga2RfbG9zcy5pdGVtKClcblxucHJpbnQoXHUwMDI3UHJvZ3Jlc3NpdmUgc2hyaW5raW5nOiBmdWxsIC1cdTAwM2UgZWxhc3RpYyBrZXJuZWwgLVx1MDAzZSBlbGFzdGljIGRlcHRoIC1cdTAwM2UgZWxhc3RpYyB3aWR0aFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdWJuZXQgU2VhcmNoIHdpdGggTGF0ZW5jeSBMb29rdXAifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgcmFuZG9tXG5mcm9tIGl0ZXJ0b29scyBpbXBvcnQgcHJvZHVjdFxuXG4jIFByZWNvbXB1dGVkIGxhdGVuY3kgbG9va3VwIHRhYmxlIChtcykgZm9yIGVhY2ggb3Agb24gdGFyZ2V0IGRldmljZVxuIyBJbiBwcmFjdGljZSwgbWVhc3VyZWQgYnkgcHJvZmlsaW5nIGVhY2ggb3AgaW5kZXBlbmRlbnRseVxuTEFURU5DWV9MVVQgPSB7XG4gICAgKFx1MDAyN2NvbnYzXHUwMDI3LCAyKTogMS4yLCAoXHUwMDI3Y29udjNcdTAwMjcsIDMpOiAxLjgsIChcdTAwMjdjb252M1x1MDAyNywgNCk6IDIuNCxcbiAgICAoXHUwMDI3Y29udjVcdTAwMjcsIDIpOiAyLjEsIChcdTAwMjdjb252NVx1MDAyNywgMyk6IDMuMiwgKFx1MDAyN2NvbnY1XHUwMDI3LCA0KTogNC4zLFxuICAgIChcdTAwMjdjb252N1x1MDAyNywgMik6IDMuNSwgKFx1MDAyN2NvbnY3XHUwMDI3LCAzKTogNS4yLCAoXHUwMDI3Y29udjdcdTAwMjcsIDQpOiA2LjksXG59XG5cbmRlZiBlc3RpbWF0ZV9sYXRlbmN5KHN1Ym5ldF9jb25maWc6IGRpY3QpIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiRXN0aW1hdGUgbGF0ZW5jeSBmcm9tIGxvb2t1cCB0YWJsZSB3aXRob3V0IHJ1bm5pbmcgdGhlIG1vZGVsLlwiXCJcIlxuICAgIHRvdGFsID0gMC4wXG4gICAgZm9yIHN0YWdlX2lkeCwgKGtlcm5lbCwgZGVwdGgpIGluIGVudW1lcmF0ZShcbiAgICAgICAgemlwKHN1Ym5ldF9jb25maWdbXHUwMDI3a2VybmVsc1x1MDAyN10sIHN1Ym5ldF9jb25maWdbXHUwMDI3ZGVwdGhzXHUwMDI3XSlcbiAgICApOlxuICAgICAgICBrZXkgPSAoZlx1MDAyN2NvbnZ7a2VybmVsfVx1MDAyNywgZGVwdGgpXG4gICAgICAgIHRvdGFsICs9IExBVEVOQ1lfTFVULmdldChrZXksIDMuMCkgICMgZGVmYXVsdCAzbXMgaWYgbm90IGluIHRhYmxlXG4gICAgcmV0dXJuIHRvdGFsXG5cbmRlZiBldm9sdXRpb25hcnlfc3VibmV0X3NlYXJjaChuX2l0ZXJhdGlvbnM9MTAwLCBsYXRlbmN5X2J1ZGdldF9tcz0xMi4wLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBvcHVsYXRpb25fc2l6ZT01MCk6XG4gICAgXCJcIlwiU2ltcGxlIGV2b2x1dGlvbmFyeSBzZWFyY2ggb3ZlciBzdWJuZXQgY29uZmlndXJhdGlvbnMuXCJcIlwiXG4gICAga2VybmVsX2Nob2ljZXMgPSBbMywgNSwgN11cbiAgICBkZXB0aF9jaG9pY2VzID0gWzIsIDMsIDRdXG4gICAgbl9zdGFnZXMgPSA1XG5cbiAgICBkZWYgcmFuZG9tX3N1Ym5ldCgpOlxuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgXHUwMDI3a2VybmVsc1x1MDAyNzogW3JhbmRvbS5jaG9pY2Uoa2VybmVsX2Nob2ljZXMpIGZvciBfIGluIHJhbmdlKG5fc3RhZ2VzKV0sXG4gICAgICAgICAgICBcdTAwMjdkZXB0aHNcdTAwMjc6IFtyYW5kb20uY2hvaWNlKGRlcHRoX2Nob2ljZXMpIGZvciBfIGluIHJhbmdlKG5fc3RhZ2VzKV0sXG4gICAgICAgIH1cblxuICAgICMgSW5pdGlhbGl6ZSBwb3B1bGF0aW9uIHdpdGggdmFsaWQgKHdpdGhpbiBidWRnZXQpIHN1Ym5ldHNcbiAgICBwb3B1bGF0aW9uID0gW2MgZm9yIF8gaW4gcmFuZ2Uobl9pdGVyYXRpb25zKVxuICAgICAgICAgICAgICAgICAgaWYgKGMgOj0gcmFuZG9tX3N1Ym5ldCgpKSBhbmQgZXN0aW1hdGVfbGF0ZW5jeShjKSBcdTAwM2M9IGxhdGVuY3lfYnVkZ2V0X21zXVxuXG4gICAgcHJpbnQoZlx1MDAyN0ZvdW5kIHtsZW4ocG9wdWxhdGlvbil9IHZhbGlkIHN1Ym5ldHMgd2l0aGluIHtsYXRlbmN5X2J1ZGdldF9tc31tcyBidWRnZXRcdTAwMjcpXG4gICAgaWYgcG9wdWxhdGlvbjpcbiAgICAgICAgbGF0cyA9IFtlc3RpbWF0ZV9sYXRlbmN5KGMpIGZvciBjIGluIHBvcHVsYXRpb25bOjVdXVxuICAgICAgICBwcmludChmXHUwMDI3U2FtcGxlIGxhdGVuY2llcyAobXMpOiB7W3JvdW5kKGwsMikgZm9yIGwgaW4gbGF0c119XHUwMDI3KVxuICAgIHJldHVybiBwb3B1bGF0aW9uXG5cbnJlc3VsdHMgPSBldm9sdXRpb25hcnlfc3VibmV0X3NlYXJjaChuX2l0ZXJhdGlvbnM9MjAwLCBsYXRlbmN5X2J1ZGdldF9tcz0xMi4wKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9GQSBEZXBsb3ltZW50IOKAlCBNb2JpbGUgdnMgU2VydmVyIFN1Ym5ldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWZ0ZXIgdHJhaW5pbmcgdGhlIE9GQSBzdXBlcm5ldCBvbmNlLCBzZWxlY3RpbmcgYSBzdWJuZXQgZm9yIGEgbmV3IGhhcmR3YXJlIHRhcmdldCB0YWtlcyBtaW51dGVzOiBtZWFzdXJlIHRoZSBsYXRlbmN5IG9mIGluZGl2aWR1YWwgb3BlcmF0aW9ucyBvbiB0aGUgdGFyZ2V0IGRldmljZSwgYnVpbGQgYSBsb29rdXAgdGFibGUsIHJ1biBhbiBldm9sdXRpb25hcnkgc2VhcmNoIG92ZXIgc3VibmV0IGNvbmZpZ3VyYXRpb25zLCBhbmQgZXh0cmFjdCB0aGUgYmVzdCBzdWJuZXQuIE5vIGdyYWRpZW50IGNvbXB1dGF0aW9uIG9yIHdlaWdodCB1cGRhdGVzIGFyZSBuZWVkZWQuIFRoZSBleHRyYWN0ZWQgc3VibmV0IGlzIGV2YWx1YXRlZCBieSBmb3J3YXJkIHBhc3MgdGhyb3VnaCB0aGUgc3VwZXJuZXQgd2l0aCB0aGUgZml4ZWQgY29uZmlndXJhdGlvbi4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiT0ZBIHZzIE5BUy1SZXRyYWluIFRyYWRlLW9mZiIsImNvbnRlbnQiOiJUcmFpbmluZyB0aGUgT0ZBIHN1cGVybmV0IHRha2VzIHJvdWdobHkgMTIwMCBHUFUtaG91cnMg4oCUIG1vcmUgdGhhbiB0cmFpbmluZyBhIHNpbmdsZSBFZmZpY2llbnROZXQuIEhvd2V2ZXIsIG9uY2UgdHJhaW5lZCwgZXh0cmFjdGluZyBhbmQgZXZhbHVhdGluZyAxMCBzdWJuZXRzIGZvciAxMCBkaWZmZXJlbnQgaGFyZHdhcmUgdGFyZ2V0cyBjb3N0cyBuZWFyIHplcm8uIFRoZSBicmVhay1ldmVuIGlzIGFwcHJveGltYXRlbHkgMyBoYXJkd2FyZSB0YXJnZXRzOiBpZiB5b3UgYXJlIGRlcGxveWluZyB0byAzIG9yIG1vcmUgZGV2aWNlcywgT0ZBXHUwMDI3cyBvbmUtdGltZSB0cmFpbmluZyBjb3N0IGlzIG9mZnNldCBieSB0aGUgZWxpbWluYXRpb24gb2YgcmVwZWF0ZWQgTkFTIHJ1bnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiB3aXRoIENvbXBldGluZyBBcHByb2FjaGVzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlNlYXJjaCBDb3N0IiwiRGVwbG95bWVudCBGbGV4aWJpbGl0eSIsIkFjY3VyYWN5L0xhdGVuY3kgUGFyZXRvIiwiSGFyZHdhcmUgQ29uc3RyYWludCBTdXBwb3J0IiwiUmV0cmFpbiBBZnRlciBTZWFyY2giXSwicm93cyI6W1siTW9iaWxlTmV0VjMiLCJ+NzUgR1BVLWRheXMgKHBsYXRmb3JtLXNwZWNpZmljKSIsIlNpbmdsZSB0YXJnZXQgcGVyIHNlYXJjaCIsIkdvb2QgKG1hbnVhbGx5IHR1bmVkKSIsIk1vYmlsZS1zcGVjaWZpYyIsIk4vQSDigJQgZml4ZWQgYXJjaCJdLFsiREFSVFMiLCI0IEdQVS1kYXlzIiwiU2luZ2xlIGFyY2hpdGVjdHVyZSIsIk1vZGVyYXRlIiwiTm8gZXhwbGljaXQgY29uc3RyYWludCIsIlllcyDigJQgcmUtdHJhaW4gZnJvbSBzY3JhdGNoIl0sWyJQcm94eWxlc3NOQVMvRkJOZXQiLCJ+OSBHUFUtZGF5cyBwZXIgdGFyZ2V0IiwiU2luZ2xlIHRhcmdldCBwZXIgc2VhcmNoIiwiVmVyeSBnb29kIiwiTGF0ZW5jeSB0YWJsZSBwZXIgZGV2aWNlIiwiTm8g4oCUIGZpbmUtdHVuZSBvbmx5Il0sWyJPRkEiLCJ+MTIwMCBHUFUtaG91cnMgKG9uZSB0aW1lKSIsIkFueSBzdWJuZXQgZnJvbSAxMF4xOSBzcGFjZSIsIlN0YXRlIG9mIHRoZSBhcnQgUGFyZXRvIiwiQW55IGRldmljZSB3aXRoIExVVCIsIk5vIOKAlCBkaXJlY3QgZXh0cmFjdGlvbiJdLFsiRWZmaWNpZW50TmV0LU5BUyIsIn4zNjAwIEdQVS1kYXlzIiwiRml4ZWQgY29tcG91bmQgc2NhbGUiLCJTdGF0ZSBvZiBhcnQgKHNpbmdsZSB0YXJnZXQpIiwiR2VuZXJpYyAoVFBVLXR1bmVkKSIsIk4vQSDigJQgZml4ZWQgYXJjaCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWxhc3RpYyBXaWR0aCDigJQgQ2hhbm5lbCBJbXBvcnRhbmNlIFNvcnRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVsYXN0aWMgd2lkdGggbWVhbnMgYW55IHN1YnNldCBvZiBjaGFubmVscyBjYW4gYmUgc2VsZWN0ZWQgd2l0aGluIGVhY2ggbGF5ZXIuIEZvciB0aGlzIHRvIHdvcmsgd2l0aCBzaGFyZWQgd2VpZ2h0cywgY2hhbm5lbHMgbXVzdCBiZSBzb3J0ZWQgYnkgaW1wb3J0YW5jZSBiZWZvcmUgdHJhaW5pbmcuIE9GQSBzb3J0cyBjaGFubmVscyBieSB0aGVpciBMMS1ub3JtIG9mIHdlaWdodHMgKG1vc3QgaW1wb3J0YW50IGZpcnN0KSwgdGhlbiBhbnkgc3VibmV0IHNpbXBseSB0YWtlcyB0aGUgdG9wLWsgY2hhbm5lbHMuIFRoaXMgb3JkZXJpbmcgaXMgbGVhcm5lZCBwcm9ncmVzc2l2ZWx5IGR1cmluZyB0cmFpbmluZzogdGhlIG5ldHdvcmsgaXMgcGVyaW9kaWNhbGx5IHJlLXNvcnRlZCBhZnRlciBlYWNoIGVsYXN0aWMtd2lkdGggc3RhZ2Ugc28gdGhhdCB0aGUgZmlyc3QgayBjaGFubmVscyBhbHdheXMgcmVwcmVzZW50IHRoZSBiZXN0IGsgY2hhbm5lbHMgZm9yIGFueSBrLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgc29ydF9jaGFubmVsc19ieV9pbXBvcnRhbmNlKGNvbnY6IG5uLkNvbnYyZCwgYm46IG5uLkJhdGNoTm9ybTJkKTpcbiAgICBcIlwiXCJcbiAgICBTb3J0IG91dHB1dCBjaGFubmVscyBieSBMMSBub3JtIG9mIGNvbnYgd2VpZ2h0cyAoZGVzY2VuZGluZykuXG4gICAgTW9zdCBpbXBvcnRhbnQgY2hhbm5lbHMgZmlyc3Qgc28gdG9wLWsgc2xpY2luZyBhbHdheXMgZ2l2ZXMgYmVzdCBrLlxuICAgIFJldHVybnMgbmV3IGNvbnYgYW5kIGJuIHdpdGggcmVvcmRlcmVkIGNoYW5uZWxzLlxuICAgIFwiXCJcIlxuICAgIGltcG9ydCBjb3B5XG4gICAgVyA9IGNvbnYud2VpZ2h0LmRhdGEgICMgKENfb3V0LCBDX2luLCBrSCwga1cpXG4gICAgaW1wb3J0YW5jZSA9IFcuYWJzKCkuc3VtKGRpbT0oMSwgMiwgMykpICAjIChDX291dCwpXG4gICAgc29ydGVkX2lkeCA9IGltcG9ydGFuY2UuYXJnc29ydChkZXNjZW5kaW5nPVRydWUpICAjIG1vc3QgaW1wb3J0YW50IGZpcnN0XG5cbiAgICBuZXdfY29udiA9IGNvcHkuZGVlcGNvcHkoY29udilcbiAgICBuZXdfY29udi53ZWlnaHQuZGF0YSA9IFdbc29ydGVkX2lkeF1cbiAgICBpZiBjb252LmJpYXMgaXMgbm90IE5vbmU6XG4gICAgICAgIG5ld19jb252LmJpYXMuZGF0YSA9IGNvbnYuYmlhcy5kYXRhW3NvcnRlZF9pZHhdXG5cbiAgICBuZXdfYm4gPSBjb3B5LmRlZXBjb3B5KGJuKVxuICAgIG5ld19ibi53ZWlnaHQuZGF0YSA9IGJuLndlaWdodC5kYXRhW3NvcnRlZF9pZHhdXG4gICAgbmV3X2JuLmJpYXMuZGF0YSA9IGJuLmJpYXMuZGF0YVtzb3J0ZWRfaWR4XVxuICAgIG5ld19ibi5ydW5uaW5nX21lYW4gPSBibi5ydW5uaW5nX21lYW5bc29ydGVkX2lkeF1cbiAgICBuZXdfYm4ucnVubmluZ192YXIgPSBibi5ydW5uaW5nX3Zhcltzb3J0ZWRfaWR4XVxuXG4gICAgcHJpbnQoZlx1MDAyN1NvcnRlZCB7Vy5zaGFwZVswXX0gY2hhbm5lbHMuIFRvcC01IGltcG9ydGFuY2U6IFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjd7aW1wb3J0YW5jZVtzb3J0ZWRfaWR4Wzo1XV0ucm91bmQoZGVjaW1hbHM9MikudG9saXN0KCl9XHUwMDI3KVxuICAgIHJldHVybiBuZXdfY29udiwgbmV3X2JuXG5cbmNvbnYgPSBubi5Db252MmQoMywgMzIsIDMsIHBhZGRpbmc9MSlcbmJuID0gbm4uQmF0Y2hOb3JtMmQoMzIpXG5uZXdfY29udiwgbmV3X2JuID0gc29ydF9jaGFubmVsc19ieV9pbXBvcnRhbmNlKGNvbnYsIGJuKVxuIyBOb3c6IG5ld19jb252LndlaWdodFs6a10gZ2l2ZXMgdGhlIGJlc3QgayBvdXRwdXQgY2hhbm5lbHMgZm9yIGFueSBrXG5mb3IgayBpbiBbOCwgMTYsIDI0LCAzMl06XG4gICAgc3ViX3dlaWdodCA9IG5ld19jb252LndlaWdodC5kYXRhWzprXVxuICAgIHByaW50KGZcdTAwMjdUb3Ate2t9IGNoYW5uZWxzIHdlaWdodCBub3JtOiB7c3ViX3dlaWdodC5ub3JtKCkuaXRlbSgpOi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBY2N1cmFjeSByZXN1bHRzIGZyb20gdGhlIE9GQSBwYXBlciAoSW1hZ2VOZXQpOiBvbiBhIFBpeGVsMiBwaG9uZSB3aXRoIGEgNThtcyBsYXRlbmN5IGJ1ZGdldCwgT0ZBIGZpbmRzIGEgc3VibmV0IHdpdGggNzYuMCUgdG9wLTEgYWNjdXJhY3kuIE1vYmlsZU5ldFYzLUxhcmdlIHdpdGggdGhlIHNhbWUgbGF0ZW5jeSBhY2hpZXZlcyA3NS4yJS4gT24gYSBOb3RlMTAgR1BVIHdpdGggYSAxMm1zIGJ1ZGdldCwgT0ZBIGFjaGlldmVzIDgwLjAlIHZzIDc5LjglIGZvciBNb2JpbGVOZXRWMy4gVGhlIGFjY3VyYWN5IGdhaW5zIGFyZSBtb2Rlc3QgYnV0IHRoZSBkZXBsb3ltZW50IGZsZXhpYmlsaXR5IChubyBOQVMgcmUtcnVuKSBpcyB0aGUgcHJpbWFyeSBhZHZhbnRhZ2UuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQcm9ncmVzc2l2ZSBzaHJpbmtpbmcgb3JkZXI6IGZ1bGwg4oaSIGVsYXN0aWMga2VybmVsIOKGkiBlbGFzdGljIGRlcHRoIOKGkiBlbGFzdGljIHdpZHRoIChlYWNoIHN0YWdlIGFkZHMgb25lIGVsYXN0aWMgZGltKS4iLCJJbi1wbGFjZSBLRDogdGVhY2hlciA9IHNhbWUgc3VwZXJuZXQgYXQgbWF4IGNvbmZpZzsgc3R1ZGVudCA9IHJhbmRvbSBzbWFsbGVyIGNvbmZpZzsgbm8gZXh0ZXJuYWwgdGVhY2hlciBuZWVkZWQuIiwiRWxhc3RpYyBrZXJuZWwgdHJhbnNmb3JtIG1hdHJpeDogbGVhcm5lZCBsaW5lYXIgbWFwIGFkYXB0cyAzw5czIGNlbnRlciBjcm9wIGZyb20gN8OXNyB3ZWlnaHRzIOKAlCBub3QganVzdCBhIHNsaWNlLiIsIlN1Ym5ldCBhY2N1cmFjeSBwcm94eTogdHJhaW4gYSBzbWFsbCBhY2N1cmFjeSBwcmVkaWN0b3IgKE1MUCBvbiBzdWJuZXQgY29uZmlnKSB0byByYW5rIHN1Ym5ldHMgd2l0aG91dCBmb3J3YXJkIHBhc3MuIiwiUmVzb2x1dGlvbiBlbGFzdGljaXR5OiB0cmFpbmluZyB3aXRoIHJhbmRvbSBpbnB1dCBjcm9wcyBbMTI4LDIyNF0gdGVhY2hlcyB0aGUgc3VwZXJuZXQgdG8gaGFuZGxlIHZhcnlpbmcgcmVzb2x1dGlvbnMuIiwiRGVwbG95bWVudDogc3VibmV0IGV4dHJhY3Rpb24gaXMgYSBmb3J3YXJkIHBhc3Mgd2l0aCBmaXhlZCBjb25maWcg4oCUIHRha2VzIG1pbGxpc2Vjb25kcywgbm8gR1BVIGdyYWRpZW50IGNvbXB1dGF0aW9uLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBPRkEgYWNjdXJhY3kgcHJlZGljdG9yIGlzIGEgc21hbGwgTUxQICgzIGxheWVycywgNDAwIGhpZGRlbiB1bml0cykgdHJhaW5lZCBvbiAoc3VibmV0X2NvbmZpZyDihpIgdG9wLTFfYWNjdXJhY3kpIHBhaXJzIGNvbGxlY3RlZCBieSBzYW1wbGluZyB+MTYsMDAwIHJhbmRvbSBzdWJuZXRzIGFuZCBldmFsdWF0aW5nIHRoZW0gb24gYSAxMCwwMDAtaW1hZ2UgdmFsaWRhdGlvbiBzdWJzZXQuIE9uY2UgdHJhaW5lZCwgdGhlIHByZWRpY3RvciByYW5rcyBzdWJuZXRzIGluIG1pY3Jvc2Vjb25kcywgZW5hYmxpbmcgZXZvbHV0aW9uYXJ5IHNlYXJjaCBvdmVyIG1pbGxpb25zIG9mIGNhbmRpZGF0ZXMgd2l0aG91dCBhbnkgR1BVIGZvcndhcmQgcGFzc2VzLiBUaGUgcHJlZGljdG9yXHUwMDI3cyByYW5raW5nIGFjY3VyYWN5IChTcGVhcm1hbiBjb3JyZWxhdGlvbiB3aXRoIHRydWUgYWNjdXJhY3kpIGlzIHR5cGljYWxseSAwLjk1KywgbWFraW5nIGl0IGEgcmVsaWFibGUgcHJveHkgZm9yIHRoZSBmdWxsIGV2YWx1YXRpb24uIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Once-for-All — Train Once, Deploy Many Architectures

Standard NAS finds one architecture per hardware target. Deploying a model to 10 different devices (phone, tablet, server, IoT) requires 10 separate NAS runs, each potentially days of compute. Once-for-All (OFA, Cai et al. 2020) decouples training from search: a single supernet is trained once, and arbitrary subnets — defined by depth, width, kernel size, and resolution — can be extracted and deployed without any retraining. Each subnet achieves accuracy close to the equivalent standalone model.

## OFA Search Space

The OFA supernet is built from MobileNetV3-like inverted residual blocks. The elastic dimensions are: (1) kernel size per layer ∈ {3, 5, 7}, (2) depth (number of blocks per stage) ∈ {2, 3, 4}, (3) expand ratio (width multiplier inside blocks) ∈ {3, 4, 6}, and (4) input resolution ∈ {128, 160, 192, 224}. The total number of possible subnets exceeds 10^19, covering a continuous Pareto frontier from 150M to 600M FLOPs.

## Elastic Kernel Sharing

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ElasticKernelConv(nn.Module):
    """
    A single conv weight of size 7x7 that can act as 7x7, 5x5, or 3x3
    by extracting the center sub-kernel (shared weights).
    """

    def __init__(self, in_channels: int, out_channels: int, max_kernel: int = 7):
        super().__init__()
        assert max_kernel in (7, 5, 3), 'max_kernel must be 7, 5, or 3'
        self.max_kernel = max_kernel
        # All kernel sizes share from this single weight tensor
        self.weight = nn.Parameter(
            torch.randn(out_channels, in_channels, max_kernel, max_kernel)
            * (2 / (in_channels * max_kernel ** 2)) ** 0.5
        )
        self.bias = nn.Parameter(torch.zeros(out_channels))
        # Learnable transformation matrices to adapt center kernel for smaller sizes
        self.transforms = nn.ParameterDict()
        for ks in [k for k in [3, 5, 7] if k < max_kernel]:
            self.transforms[str(ks)] = nn.Parameter(torch.eye(ks * ks))

    def _extract_sub_kernel(self, kernel_size: int) -> torch.Tensor:
        if kernel_size == self.max_kernel:
            return self.weight
        # Extract center crop
        start = (self.max_kernel - kernel_size) // 2
        sub = self.weight[:, :, start:start+kernel_size, start:start+kernel_size]
        # Apply learned linear transformation (shape-preserving)
        C_out, C_in = sub.shape[:2]
        sub_flat = sub.reshape(C_out * C_in, -1)  # (..., ks*ks)
        T = self.transforms[str(kernel_size)]      # (ks*ks, ks*ks)
        sub_transformed = (sub_flat @ T).reshape(C_out, C_in, kernel_size, kernel_size)
        return sub_transformed

    def forward(self, x: torch.Tensor, kernel_size: int = None) -> torch.Tensor:
        if kernel_size is None:
            kernel_size = self.max_kernel
        W = self._extract_sub_kernel(kernel_size)
        pad = kernel_size // 2
        return F.conv2d(x, W, self.bias, padding=pad)

# Demo: same weights, different kernel sizes
elastic_conv = ElasticKernelConv(16, 32, max_kernel=7)
x = torch.randn(2, 16, 8, 8)
for ks in [3, 5, 7]:
    out = elastic_conv(x, kernel_size=ks)
    print(f'kernel_size={ks}: input {x.shape} -> output {out.shape}')
```

## Progressive Shrinking Training

Training the full supernet from scratch is difficult: all subnets share weights, and small subnets interfere with large ones. Progressive shrinking solves this by training in stages: (1) train the full network (largest kernel, most layers, widest expand ratio) to convergence; (2) add elastic kernel by training with randomly sampled kernel sizes while distilling from the full-kernel subnet; (3) add elastic depth by randomly dropping layers; (4) add elastic width. Each stage uses in-place knowledge distillation: the teacher is the same supernet evaluated with the current stage's maximum configuration.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import random

def progressive_shrinking_step(supernet, x, y_true, criterion,
                               stage='kernel',
                               kernel_choices=(3, 5, 7),
                               depth_choices=(2, 3, 4)):
    """
    One training step with progressive shrinking and in-place distillation.
    Teacher: supernet with max config. Student: random smaller config.
    """
    supernet.eval()
    # Teacher forward: always max config
    with torch.no_grad():
        teacher_logits = supernet(x, kernel_size=max(kernel_choices),
                                  depth=max(depth_choices))
        teacher_probs = F.softmax(teacher_logits / 4.0, dim=-1)  # T=4 temperature

    supernet.train()
    # Student forward: random smaller config
    if stage == 'kernel':
        ks = random.choice(kernel_choices)
        student_logits = supernet(x, kernel_size=ks, depth=max(depth_choices))
    elif stage == 'depth':
        ks = random.choice(kernel_choices)
        d = random.choice(depth_choices)
        student_logits = supernet(x, kernel_size=ks, depth=d)
    else:
        student_logits = supernet(x, kernel_size=max(kernel_choices),
                                  depth=max(depth_choices))

    # Combined loss: task loss + KD loss from teacher
    task_loss = criterion(student_logits, y_true)
    kd_loss = F.kl_div(
        F.log_softmax(student_logits / 4.0, dim=-1),
        teacher_probs,
        reduction='batchmean'
    ) * (4.0 ** 2)  # scale by T^2

    total_loss = 0.5 * task_loss + 0.5 * kd_loss
    return total_loss, task_loss.item(), kd_loss.item()

print('Progressive shrinking: full -> elastic kernel -> elastic depth -> elastic width')
```

## Subnet Search with Latency Lookup

```python
import torch
import random
from itertools import product

# Precomputed latency lookup table (ms) for each op on target device
# In practice, measured by profiling each op independently
LATENCY_LUT = {
    ('conv3', 2): 1.2, ('conv3', 3): 1.8, ('conv3', 4): 2.4,
    ('conv5', 2): 2.1, ('conv5', 3): 3.2, ('conv5', 4): 4.3,
    ('conv7', 2): 3.5, ('conv7', 3): 5.2, ('conv7', 4): 6.9,
}

def estimate_latency(subnet_config: dict) -> float:
    """Estimate latency from lookup table without running the model."""
    total = 0.0
    for stage_idx, (kernel, depth) in enumerate(
        zip(subnet_config['kernels'], subnet_config['depths'])
    ):
        key = (f'conv{kernel}', depth)
        total += LATENCY_LUT.get(key, 3.0)  # default 3ms if not in table
    return total

def evolutionary_subnet_search(n_iterations=100, latency_budget_ms=12.0,
                               population_size=50):
    """Simple evolutionary search over subnet configurations."""
    kernel_choices = [3, 5, 7]
    depth_choices = [2, 3, 4]
    n_stages = 5

    def random_subnet():
        return {
            'kernels': [random.choice(kernel_choices) for _ in range(n_stages)],
            'depths': [random.choice(depth_choices) for _ in range(n_stages)],
        }

    # Initialize population with valid (within budget) subnets
    population = [c for _ in range(n_iterations)
                  if (c := random_subnet()) and estimate_latency(c) <= latency_budget_ms]

    print(f'Found {len(population)} valid subnets within {latency_budget_ms}ms budget')
    if population:
        lats = [estimate_latency(c) for c in population[:5]]
        print(f'Sample latencies (ms): {[round(l,2) for l in lats]}')
    return population

results = evolutionary_subnet_search(n_iterations=200, latency_budget_ms=12.0)
```

## OFA Deployment — Mobile vs Server Subnet

After training the OFA supernet once, selecting a subnet for a new hardware target takes minutes: measure the latency of individual operations on the target device, build a lookup table, run an evolutionary search over subnet configurations, and extract the best subnet. No gradient computation or weight updates are needed. The extracted subnet is evaluated by forward pass through the supernet with the fixed configuration.

> **OFA vs NAS-Retrain Trade-off**: Training the OFA supernet takes roughly 1200 GPU-hours — more than training a single EfficientNet. However, once trained, extracting and evaluating 10 subnets for 10 different hardware targets costs near zero. The break-even is approximately 3 hardware targets: if you are deploying to 3 or more devices, OFA's one-time training cost is offset by the elimination of repeated NAS runs.

## Comparison with Competing Approaches

| Method | Search Cost | Deployment Flexibility | Accuracy/Latency Pareto | Hardware Constraint Support | Retrain After Search |
| --- | --- | --- | --- | --- | --- |
| MobileNetV3 | ~75 GPU-days (platform-specific) | Single target per search | Good (manually tuned) | Mobile-specific | N/A — fixed arch |
| DARTS | 4 GPU-days | Single architecture | Moderate | No explicit constraint | Yes — re-train from scratch |
| ProxylessNAS/FBNet | ~9 GPU-days per target | Single target per search | Very good | Latency table per device | No — fine-tune only |
| OFA | ~1200 GPU-hours (one time) | Any subnet from 10^19 space | State of the art Pareto | Any device with LUT | No — direct extraction |
| EfficientNet-NAS | ~3600 GPU-days | Fixed compound scale | State of art (single target) | Generic (TPU-tuned) | N/A — fixed arch |

## Elastic Width — Channel Importance Sorting

Elastic width means any subset of channels can be selected within each layer. For this to work with shared weights, channels must be sorted by importance before training. OFA sorts channels by their L1-norm of weights (most important first), then any subnet simply takes the top-k channels. This ordering is learned progressively during training: the network is periodically re-sorted after each elastic-width stage so that the first k channels always represent the best k channels for any k.

```python
import torch
import torch.nn as nn

def sort_channels_by_importance(conv: nn.Conv2d, bn: nn.BatchNorm2d):
    """
    Sort output channels by L1 norm of conv weights (descending).
    Most important channels first so top-k slicing always gives best k.
    Returns new conv and bn with reordered channels.
    """
    import copy
    W = conv.weight.data  # (C_out, C_in, kH, kW)
    importance = W.abs().sum(dim=(1, 2, 3))  # (C_out,)
    sorted_idx = importance.argsort(descending=True)  # most important first

    new_conv = copy.deepcopy(conv)
    new_conv.weight.data = W[sorted_idx]
    if conv.bias is not None:
        new_conv.bias.data = conv.bias.data[sorted_idx]

    new_bn = copy.deepcopy(bn)
    new_bn.weight.data = bn.weight.data[sorted_idx]
    new_bn.bias.data = bn.bias.data[sorted_idx]
    new_bn.running_mean = bn.running_mean[sorted_idx]
    new_bn.running_var = bn.running_var[sorted_idx]

    print(f'Sorted {W.shape[0]} channels. Top-5 importance: '
          f'{importance[sorted_idx[:5]].round(decimals=2).tolist()}')
    return new_conv, new_bn

conv = nn.Conv2d(3, 32, 3, padding=1)
bn = nn.BatchNorm2d(32)
new_conv, new_bn = sort_channels_by_importance(conv, bn)
# Now: new_conv.weight[:k] gives the best k output channels for any k
for k in [8, 16, 24, 32]:
    sub_weight = new_conv.weight.data[:k]
    print(f'Top-{k} channels weight norm: {sub_weight.norm().item():.3f}')
```

Accuracy results from the OFA paper (ImageNet): on a Pixel2 phone with a 58ms latency budget, OFA finds a subnet with 76.0% top-1 accuracy. MobileNetV3-Large with the same latency achieves 75.2%. On a Note10 GPU with a 12ms budget, OFA achieves 80.0% vs 79.8% for MobileNetV3. The accuracy gains are modest but the deployment flexibility (no NAS re-run) is the primary advantage.

- Progressive shrinking order: full → elastic kernel → elastic depth → elastic width (each stage adds one elastic dim).
- In-place KD: teacher = same supernet at max config; student = random smaller config; no external teacher needed.
- Elastic kernel transform matrix: learned linear map adapts 3×3 center crop from 7×7 weights — not just a slice.
- Subnet accuracy proxy: train a small accuracy predictor (MLP on subnet config) to rank subnets without forward pass.
- Resolution elasticity: training with random input crops [128,224] teaches the supernet to handle varying resolutions.
- Deployment: subnet extraction is a forward pass with fixed config — takes milliseconds, no GPU gradient computation.

The OFA accuracy predictor is a small MLP (3 layers, 400 hidden units) trained on (subnet_config → top-1_accuracy) pairs collected by sampling ~16,000 random subnets and evaluating them on a 10,000-image validation subset. Once trained, the predictor ranks subnets in microseconds, enabling evolutionary search over millions of candidates without any GPU forward passes. The predictor's ranking accuracy (Spearman correlation with true accuracy) is typically 0.95+, making it a reliable proxy for the full evaluation.

---

