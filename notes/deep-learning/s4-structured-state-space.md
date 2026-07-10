---
title: "S4 — Structured State Space Sequence Models"
slug: "s4-structured-state-space"
description: "S4 structured state space models — continuous-time SSMs, HiPPO polynomial approximation, and efficient O(L log L) training via global convolution and the Cauchy kernel."
tags: ["deep-learning", "rnns", "sequence-models", "state-space-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhdGUgc3BhY2UgbW9kZWxzIChTU01zKSBoYXZlIGEgbG9uZyBoaXN0b3J5IGluIGNvbnRyb2wgdGhlb3J5IGFuZCBzaWduYWwgcHJvY2Vzc2luZywgYnV0IGFwcGx5aW5nIHRoZW0gdG8gZGVlcCBzZXF1ZW5jZSBtb2RlbGluZyByZXF1aXJlZCBzb2x2aW5nIHRocmVlIGhhcmQgcHJvYmxlbXMgc2ltdWx0YW5lb3VzbHk6IGhvdyB0byBpbml0aWFsaXplIHRoZSBzdGF0ZSBtYXRyaXggQSB0byBjYXB0dXJlIGxvbmctcmFuZ2UgZGVwZW5kZW5jaWVzLCBob3cgdG8gdHJhaW4gZWZmaWNpZW50bHkgd2l0aG91dCBzZXF1ZW50aWFsIHJlY3VycmVuY2UsIGFuZCBob3cgdG8gaGFuZGxlIHZlcnkgbG9uZyBzZXF1ZW5jZXMgKEwgPSAxNiwwMDArKSB3aGVyZSB0cmFuc2Zvcm1lcnMgYXJlIHByb2hpYml0aXZlbHkgZXhwZW5zaXZlLiBTNCAoR3UgZXQgYWwuLCAyMDIxKSBzb2x2ZWQgYWxsIHRocmVlIGJ5IGNvbWJpbmluZyB0aGUgSGlQUE8gZnJhbWV3b3JrIGZvciBBIGluaXRpYWxpemF0aW9uIHdpdGggYSBzdHJ1Y3R1cmVkIG5vcm1hbCBwbHVzIGxvdy1yYW5rIChOUExSKSByZXByZXNlbnRhdGlvbiB0aGF0IGFkbWl0cyBhbiBPKEwgbG9nIEwpIGNvbnZvbHV0aW9uYWwgY29tcHV0YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RhdGUgU3BhY2UgTW9kZWxzIOKAlCBUaGUgQ29udGludW91cy1UaW1lIEZvdW5kYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgbGluZWFyIHRpbWUtaW52YXJpYW50IFNTTSBtYXBzIGlucHV0IHUodCkgdG8gb3V0cHV0IHkodCkgdGhyb3VnaCBhIGxhdGVudCBzdGF0ZSB4KHQpIOKIiCDihJ3htLouIFRoZSBjb250aW51b3VzLXRpbWUgZXF1YXRpb25zIGFyZSB4XHUwMDI3KHQpID0gQXgodCkgKyBCdSh0KSBhbmQgeSh0KSA9IEN4KHQpICsgRHUodCksIHdoZXJlIEEg4oiIIOKEnV57TsOXTn0sIEIg4oiIIOKEnV57TsOXMX0sIEMg4oiIIOKEnV57McOXTn0sIEQg4oiIIOKEnS4gRm9yIGRpc2NyZXRlIHNlcXVlbmNlcywgdGhlIHN5c3RlbSBpcyBkaXNjcmV0aXplZCB1c2luZyB6ZXJvLW9yZGVyIGhvbGQgKFpPSCk6IMSAID0gZXhwKM6UQSksIELMhCA9ICjEgCAtIEkpQeKBu8K5QiwgZ2l2aW5nIHRoZSByZWN1cnJlbmNlIHjigpkgPSDEgHjigpnigovigoEgKyBCzIR14oKZIGFuZCB54oKZID0gQ3jigpkgKyBEdeKCmS4gVGhlIHN0ZXAgc2l6ZSDOlCBjb250cm9scyB0aGUgdGltZSByZXNvbHV0aW9uIGFuZCBpcyBhIGxlYXJuYWJsZSBwYXJhbWV0ZXIuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJOID0gc3RhdGUgZGltZW5zaW9uICh0eXBpY2FsbHkgNjTigJMyNTYpOiBjb250cm9scyBtZW1vcnkgY2FwYWNpdHkgb2YgdGhlIFNTTSIsIsSAIOKIiCDihJ1ee07Dl059OiBkaXNjcmV0aXplZCBzdGF0ZSB0cmFuc2l0aW9uIOKAlCBkZXRlcm1pbmVzIHdoYXQgdGhlIHN0YXRlIHJlbWVtYmVycyIsIkLMhCDiiIgg4oSdXntOw5cxfTogaW5wdXQgcHJvamVjdGlvbiDigJQgaG93IG5ldyBpbnB1dCBtb2RpZmllcyB0aGUgc3RhdGUiLCJDIOKIiCDihJ1eezHDl059OiBvdXRwdXQgcHJvamVjdGlvbiDigJQgaG93IHN0YXRlIG1hcHMgdG8gc2NhbGFyIG91dHB1dCIsIlJlY3VycmVudCBtb2RlOiBPKE4pIHBlciBzdGVwIGZvciBpbmZlcmVuY2U7IENvbnZvbHV0aW9uYWwgbW9kZTogTyhMIGxvZyBMKSBmb3IgdHJhaW5pbmciXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEhpUFBPIEZyYW1ld29yayBmb3IgTG9uZy1SYW5nZSBNZW1vcnkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrZXkgaW5zaWdodCBiZWhpbmQgUzQgaXMgdGhhdCBuYWl2ZSByYW5kb20gaW5pdGlhbGl6YXRpb24gb2YgQSBsZWFkcyB0byBwb29yIGxvbmctcmFuZ2UgbWVtb3J5IOKAlCB0aGUgc3RhdGUgcmFwaWRseSBmb3JnZXRzIGRpc3RhbnQgaW5wdXRzLiBIaVBQTyAoSGlnaC1vcmRlciBQb2x5bm9taWFsIFByb2plY3Rpb24gT3BlcmF0b3JzLCBHdSBldCBhbC4gMjAyMCkgcHJvdmlkZXMgYSBwcmluY2lwbGVkIGluaXRpYWxpemF0aW9uOiBBIGlzIGNob3NlbiBzbyB0aGF0IHRoZSBoaWRkZW4gc3RhdGUgeCh0KSBhdCBhbnkgdGltZSB0IGlzIHRoZSBvcHRpbWFsIHBvbHlub21pYWwgYXBwcm94aW1hdGlvbiBvZiB0aGUgaW5wdXQgaGlzdG9yeSB1KDA6dCkgaW4gYSBMZWdlbmRyZSBwb2x5bm9taWFsIGJhc2lzLiBIaVBQTy1MZWdUIHNldHMgQVtuLGtdID0gLSgybisxKV57MC41fSgyaysxKV57MC41fSBmb3IgayDiiaQgbi4gVGhpcyBtYXRyaXggaGFzIGEgc3RydWN0dXJlZCBza2V3LUhlcm1pdGlhbiBwbHVzIGRpYWdvbmFsIGZvcm0gdGhhdCBjYW4gYmUgZGlhZ29uYWxpemVkIGVmZmljaWVudGx5LCBlbmFibGluZyBPKEwgbG9nIEwpIGNvbnZvbHV0aW9uIHZpYSBDYXVjaHkga2VybmVsIGNvbXB1dGF0aW9uLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IHRoZSBBIE1hdHJpeCBNYXR0ZXJzIiwiY29udGVudCI6IkZvciBhbiBTU00gdG8gbGVhcm4gbG9uZy1yYW5nZSBkZXBlbmRlbmNpZXMsIHRoZSBzdGF0ZSB0cmFuc2l0aW9uIMSAIG11c3QgcHJlc2VydmUgaW5mb3JtYXRpb24gZnJvbSBmYXItZGlzdGFudCBpbnB1dHMuIFJhbmRvbSBBIG1hdHJpY2VzIGhhdmUgZWlnZW52YWx1ZXMgd2l0aCBsYXJnZSBuZWdhdGl2ZSByZWFsIHBhcnRzIOKAlCB0aGUgc3RhdGUgZGVjYXlzIGV4cG9uZW50aWFsbHkgZmFzdC4gSGlQUE8gaW5pdGlhbGl6ZXMgQSBzbyBpdHMgZWlnZW52YWx1ZXMgY2x1c3RlciBuZWFyIHRoZSBpbWFnaW5hcnkgYXhpcywgZW5hYmxpbmcgdGhlIHN0YXRlIHRvIG1haW50YWluIHBvbHlub21pYWwgYXBwcm94aW1hdGlvbnMgb2YgdGhlIGVudGlyZSBpbnB1dCBoaXN0b3J5IHdpdGhvdXQgZXhwb25lbnRpYWwgZm9yZ2V0dGluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIERpc2NyZXRlIFNTTSBpbiBSZWN1cnJlbnQgTW9kZSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkubGluYWxnIGltcG9ydCBleHBtXG5cbmRlZiBkaXNjcmV0aXplX3pvaChBLCBCLCBkZWx0YSk6XG4gICAgXCJcIlwiWmVyby1vcmRlciBob2xkIGRpc2NyZXRpemF0aW9uOiBBYmFyPWV4cChkZWx0YSpBKSwgQmJhcj0oQWJhci1JKUFeey0xfUIuXCJcIlwiXG4gICAgTiA9IEEuc2hhcGVbMF1cbiAgICBBX2JhciA9IGV4cG0oZGVsdGEgKiBBKVxuICAgIEJfYmFyID0gbnAubGluYWxnLnNvbHZlKEEsIChBX2JhciAtIG5wLmV5ZShOKSkgQCBCKVxuICAgIHJldHVybiBBX2JhciwgQl9iYXJcblxuZGVmIHNzbV9yZWN1cnJlbnQoQV9iYXIsIEJfYmFyLCBDLCB1X3NlcSk6XG4gICAgXCJcIlwiXG4gICAgUnVuIGRpc2NyZXRlIFNTTSBpbiByZWN1cnJlbnQgbW9kZTogTyhOKSBwZXIgc3RlcC5cbiAgICBBX2JhcjogKE4sTiksIEJfYmFyOiAoTiwxKSwgQzogKDEsTiksIHVfc2VxOiAoTCwpXG4gICAgUmV0dXJucyB5OiAoTCwpXG4gICAgXCJcIlwiXG4gICAgTiA9IEFfYmFyLnNoYXBlWzBdXG4gICAgeCA9IG5wLnplcm9zKE4pXG4gICAgeSA9IFtdXG4gICAgZm9yIHUgaW4gdV9zZXE6XG4gICAgICAgIHggPSBBX2JhciBAIHggKyBCX2Jhci5yYXZlbCgpICogdSAgICMgc3RhdGUgdXBkYXRlXG4gICAgICAgIHkuYXBwZW5kKChDIEAgeCkuaXRlbSgpKSAgICAgICAgICAgICAjIG91dHB1dFxuICAgIHJldHVybiBucC5hcnJheSh5KVxuXG4jIDQtc3RhdGUgc3RhYmxlIGRpYWdvbmFsIHN5c3RlbVxubnAucmFuZG9tLnNlZWQoNDIpXG5OID0gNFxuQSA9IC1ucC5kaWFnKG5wLmFyYW5nZSgxLCBOKzEsIGR0eXBlPWZsb2F0KSkgICAjIHN0YWJsZTogYWxsIGVpZ2VudmFsdWVzIG5lZ2F0aXZlIHJlYWxcbkIgPSBucC5vbmVzKChOLCAxKSlcbkMgPSBucC5yYW5kb20ucmFuZG4oMSwgTikgKiAwLjFcbmRlbHRhID0gMC4wMVxuQV9iYXIsIEJfYmFyID0gZGlzY3JldGl6ZV96b2goQSwgQiwgZGVsdGEpXG5MID0gMjAwXG51ID0gbnAuc2luKG5wLmxpbnNwYWNlKDAsIDQgKiBucC5waSwgTCkpXG55ID0gc3NtX3JlY3VycmVudChBX2JhciwgQl9iYXIsIEMsIHUpXG5wcmludChmXCJJbnB1dDoge3Uuc2hhcGV9LCBPdXRwdXQ6IHt5LnNoYXBlfVwiKVxucHJpbnQoZlwiT3V0cHV0IHJhbmdlOiBbe3kubWluKCk6LjRmfSwge3kubWF4KCk6LjRmfV1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIFNTTSBpbiBDb252b2x1dGlvbmFsIE1vZGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBTU00gY2FuIGFsc28gYmUgdmlld2VkIGFzIGEgZ2xvYmFsIGNvbnZvbHV0aW9uYWwgZmlsdGVyOiB0aGUgaW1wdWxzZSByZXNwb25zZSBLW2xdID0gQ8K3xIDLocK3QsyEIGdpdmVzIHRoZSBjb252b2x1dGlvbiBrZXJuZWwsIGFuZCB0aGUgb3V0cHV0IHkgPSBLICogdS4gVGhpcyBpcyBiZWNhdXNlIHRoZSByZWN1cnJlbmNlIHVucm9sbHMgYXMgeeKCmSA9IM6j4oKXIEPCt8SAy6HCt0LMhMK3deKCmeKCi+KClyDigJQgZXhhY3RseSBhIChjYXVzYWwpIGNvbnZvbHV0aW9uLiBUaGUga2VybmVsIGhhcyBsZW5ndGggTCAoc2FtZSBhcyB0aGUgc2VxdWVuY2UpLCBtYWtpbmcgaXQgYSBnbG9iYWwgY29udm9sdXRpb24uIENvbXB1dGluZyBpdCBuYWl2ZWx5IGNvc3RzIE8oTMK3TsKyKSBkdWUgdG8gdGhlIG1hdHJpeCBwb3dlcnMsIGJ1dCBTNCB1c2VzIHRoZSBmYWN0IHRoYXQgdGhlIGRpYWdvbmFsaXplZCBBIGVuYWJsZXMgZmFzdCBDYXVjaHkga2VybmVsIGNvbXB1dGF0aW9uLiBJbiBwcmFjdGljZSwgRkZULWJhc2VkIGNvbnZvbHV0aW9uIHJ1bnMgaW4gTyhMIGxvZyBMKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBzc21fa2VybmVsKEFfYmFyLCBCX2JhciwgQywgTCk6XG4gICAgXCJcIlwiQ29tcHV0ZSBnbG9iYWwgU1NNIGNvbnZvbHV0aW9uIGtlcm5lbCBLW2xdID0gQyBAIEFfYmFyXmwgQCBCX2Jhci5cIlwiXCJcbiAgICBOID0gQV9iYXIuc2hhcGVbMF1cbiAgICBLID0gbnAuemVyb3MoTClcbiAgICBBX3BvdyA9IG5wLmV5ZShOKVxuICAgIGZvciBsIGluIHJhbmdlKEwpOlxuICAgICAgICBLW2xdID0gKEMgQCBBX3BvdyBAIEJfYmFyKS5pdGVtKClcbiAgICAgICAgQV9wb3cgPSBBX3BvdyBAIEFfYmFyXG4gICAgcmV0dXJuIEtcblxuZGVmIHNzbV9jb252X2ZvcndhcmQoSywgdSk6XG4gICAgXCJcIlwiQXBwbHkgU1NNIGFzIGNhdXNhbCBjb252b2x1dGlvbjogeSA9IEsgKiB1IChvdXRwdXQgbGVuZ3RoID0gTCkuXCJcIlwiXG4gICAgcmV0dXJuIG5wLmNvbnZvbHZlKEssIHUpWzpsZW4odSldXG5cbmRlZiBzc21fY29udl9mZnQoSywgdSk6XG4gICAgXCJcIlwiRkZULWJhc2VkIGNvbnZvbHV0aW9uOiBPKEwgbG9nIEwpIOKAlCBtYXRjaGVzIGNhdXNhbCBjb252IHJlc3VsdC5cIlwiXCJcbiAgICBMID0gbGVuKHUpXG4gICAgS19mZnQgPSBucC5mZnQucmZmdChLLCBuPTIqTClcbiAgICB1X2ZmdCA9IG5wLmZmdC5yZmZ0KHUsIG49MipMKVxuICAgIHJldHVybiBucC5mZnQuaXJmZnQoS19mZnQgKiB1X2ZmdCwgbj0yKkwpWzpMXVxuXG4jIEV1bGVyIGRpc2NyZXRpemF0aW9uIGZvciBzaW1wbGljaXR5IChyZXBsYWNlIHdpdGggWk9IIGluIHByYWN0aWNlKVxuTiwgTCA9IDQsIDEyOFxuQSA9IC1ucC5kaWFnKG5wLmFyYW5nZSgxLCBOKzEsIGR0eXBlPWZsb2F0KSlcbkIsIEMgID0gbnAub25lcygoTiwgMSkpLCBucC5yYW5kb20ucmFuZG4oMSwgTikgKiAwLjFcbkFfYmFyID0gbnAuZXllKE4pICsgMC4wMSAqIEFcbkJfYmFyID0gMC4wMSAqIEJcbksgPSBzc21fa2VybmVsKEFfYmFyLCBCX2JhciwgQywgTClcbnUgPSBucC5zaW4obnAubGluc3BhY2UoMCwgNCpucC5waSwgTCkpXG55X2RpcmVjdCA9IHNzbV9jb252X2ZvcndhcmQoSywgdSlcbnlfZmZ0ICAgID0gc3NtX2NvbnZfZmZ0KEssIHUpXG5wcmludChmXCJLZXJuZWw6IHtLLnNoYXBlfSwgZmlyc3QgMzoge0tbOjNdfVwiKVxucHJpbnQoZlwiRGlyZWN0IHZzIEZGVCBtYXggZGlmZjoge25wLmFicyh5X2RpcmVjdCAtIHlfZmZ0KS5tYXgoKTouMmV9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAzIOKAlCBIaVBQTyBNYXRyaXggSW5pdGlhbGl6YXRpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiBoaXBwb19sZWd0X21hdHJpeChOKTpcbiAgICBcIlwiXCJIaVBQTy1MZWdUIEEgbWF0cml4OiBvcHRpbWFsIHBvbHlub21pYWwgYXBwcm94aW1hdGlvbiBvZiBpbnB1dCBoaXN0b3J5LlwiXCJcIlxuICAgIEEgPSBucC56ZXJvcygoTiwgTikpXG4gICAgZm9yIG4gaW4gcmFuZ2UoTik6XG4gICAgICAgIGZvciBrIGluIHJhbmdlKE4pOlxuICAgICAgICAgICAgaWYgayBcdTAwM2M9IG46XG4gICAgICAgICAgICAgICAgQVtuLCBrXSA9IC1ucC5zcXJ0KDIqbisxKSAqIG5wLnNxcnQoMiprKzEpXG4gICAgcmV0dXJuIEFcblxuZGVmIGhpcHBvX2JfdmVjdG9yKE4pOlxuICAgIFwiXCJcIkhpUFBPIEIgdmVjdG9yOiBiW25dID0gc3FydCgybisxKS5cIlwiXCJcbiAgICByZXR1cm4gbnAuc3FydChucC5hcmFuZ2UoMSwgMipOLCAyLCBkdHlwZT1mbG9hdCkpLnJlc2hhcGUoTiwgMSlcblxuTiA9IDMyXG5BX2hpcHBvID0gaGlwcG9fbGVndF9tYXRyaXgoTilcbkJfaGlwcG8gPSBoaXBwb19iX3ZlY3RvcihOKVxuZWlnZW52YWx1ZXMgPSBucC5saW5hbGcuZWlndmFscyhBX2hpcHBvKVxucHJpbnQoZlwiSGlQUE8tTGVnVCBBIHNoYXBlOiB7QV9oaXBwby5zaGFwZX1cIilcbnByaW50KGZcIkVpZ2VudmFsdWUgcmVhbCByYW5nZTogW3tlaWdlbnZhbHVlcy5yZWFsLm1pbigpOi4xZn0sIHtlaWdlbnZhbHVlcy5yZWFsLm1heCgpOi4xZn1dXCIpXG5wcmludChmXCJBbGwgZWlnZW52YWx1ZXMgbm9uLXBvc2l0aXZlIHJlYWw6IHsoZWlnZW52YWx1ZXMucmVhbCBcdTAwM2M9IDFlLTgpLmFsbCgpfVwiKVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMSwgMiwgZmlnc2l6ZT0oMTIsIDQpKVxuYXhlc1swXS5pbXNob3coQV9oaXBwbywgY21hcD1cdTAwMjdSZEJ1XHUwMDI3LCBhc3BlY3Q9XHUwMDI3YXV0b1x1MDAyNylcbmF4ZXNbMF0uc2V0X3RpdGxlKGZcdTAwMjdIaVBQTy1MZWdUIEEgKE49e059KVx1MDAyNylcbmF4ZXNbMF0uc2V0X3hsYWJlbChcdTAwMjdrXHUwMDI3KTsgYXhlc1swXS5zZXRfeWxhYmVsKFx1MDAyN25cdTAwMjcpXG5heGVzWzFdLnNjYXR0ZXIoZWlnZW52YWx1ZXMucmVhbCwgZWlnZW52YWx1ZXMuaW1hZywgYz1cdTAwMjdzdGVlbGJsdWVcdTAwMjcsIHM9NTApXG5heGVzWzFdLmF4dmxpbmUoMCwgY29sb3I9XHUwMDI3cmVkXHUwMDI3LCBsaW5lc3R5bGU9XHUwMDI3LS1cdTAwMjcsIGxhYmVsPVx1MDAyN3N0YWJpbGl0eSBib3VuZGFyeVx1MDAyNylcbmF4ZXNbMV0uc2V0X3RpdGxlKFx1MDAyN0VpZ2VudmFsdWUgc3BlY3RydW0gKHN0YWJsZSBpZiByZWFsIFx1MDAzYyAwKVx1MDAyNylcbmF4ZXNbMV0uc2V0X3hsYWJlbChcdTAwMjdSZWFsXHUwMDI3KTsgYXhlc1sxXS5zZXRfeWxhYmVsKFx1MDAyN0ltYWdpbmFyeVx1MDAyNylcbmF4ZXNbMV0ubGVnZW5kKClcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3aGlwcG9fbWF0cml4LnBuZ1x1MDAyNywgZHBpPTEyMClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDQg4oCUIFM0IG9uIExvbmctU2VxdWVuY2UgQ2xhc3NpZmljYXRpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgUzRMYXllcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlNpbXBsaWZpZWQgUzQgbGF5ZXIgdXNpbmcgbGVhcm5lZCBnbG9iYWwgY29udm9sdXRpb24ga2VybmVsIHZpYSBGRlQuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWwsIHNlcV9sZW4pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5kX21vZGVsID0gZF9tb2RlbFxuICAgICAgICBzZWxmLnNlcV9sZW4gPSBzZXFfbGVuXG4gICAgICAgICMgTGVhcm5hYmxlIGNvbnZvbHV0aW9uIGtlcm5lbCAocmVwbGFjZXMgc3RydWN0dXJlZCBTU00ga2VybmVsIGluIGZ1bGwgUzQpXG4gICAgICAgIHNlbGYua2VybmVsID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKGRfbW9kZWwsIHNlcV9sZW4pICogMC4wMSlcbiAgICAgICAgc2VsZi5EICAgICAgPSBubi5QYXJhbWV0ZXIodG9yY2gub25lcyhkX21vZGVsKSkgICAjIHNraXAgY29ubmVjdGlvblxuICAgICAgICBzZWxmLm5vcm0gICA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgdSk6XG4gICAgICAgICMgdTogKEIsIEwsIGRfbW9kZWwpIC1cdTAwM2UgeTogKEIsIEwsIGRfbW9kZWwpXG4gICAgICAgIEIsIEwsIGQgPSB1LnNoYXBlXG4gICAgICAgIHkgPSB0b3JjaC56ZXJvc19saWtlKHUpXG4gICAgICAgIGZvciBpIGluIHJhbmdlKGQpOlxuICAgICAgICAgICAgayAgICAgID0gc2VsZi5rZXJuZWxbaSwgOkxdXG4gICAgICAgICAgICBrX2ZmdCAgPSB0b3JjaC5mZnQucmZmdChrLCBuPTIqTClcbiAgICAgICAgICAgIHVfZmZ0ICA9IHRvcmNoLmZmdC5yZmZ0KHVbLi4uLCBpXSwgbj0yKkwpXG4gICAgICAgICAgICB5Wy4uLiwgaV0gPSB0b3JjaC5mZnQuaXJmZnQoa19mZnQgKiB1X2ZmdCwgbj0yKkwpWzosIDpMXVxuICAgICAgICB5ID0geSArIHNlbGYuRCAqIHUgICAgICAgICAgIyBza2lwIChEIHRlcm0gaW4gU1NNKVxuICAgICAgICByZXR1cm4gc2VsZi5ub3JtKHkpXG5cbiMgVG95IGxvbmctcmFuZ2UgY2xhc3NpZmljYXRpb24gdGFza1xudG9yY2gubWFudWFsX3NlZWQoNDIpXG5MLCBkLCBCID0gMTAyNCwgMzIsIDhcbm1vZGVsID0gbm4uU2VxdWVudGlhbChcbiAgICBTNExheWVyKGQsIEwpLFxuICAgIG5uLkxpbmVhcihkLCA2NCksXG4gICAgbm4uR0VMVSgpLFxuICAgIG5uLkxpbmVhcig2NCwgMilcbilcbmR1bW15X3ggPSB0b3JjaC5yYW5kbihCLCBMLCBkKVxubG9naXRzICA9IG1vZGVsKGR1bW15X3gpLm1lYW4oZGltPTEpICAgICAgIyBnbG9iYWwgYXZlcmFnZSBwb29saW5nXG5sb3NzICAgID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpKGxvZ2l0cywgdG9yY2gucmFuZGludCgwLCAyLCAoQiwpKSlcbnByaW50KGZcIlM0IG91dHB1dDoge2xvZ2l0cy5zaGFwZX0sIExvc3M6IHtsb3NzLml0ZW0oKTouNGZ9XCIpXG5wcmludChmXCJQYXJhbXM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSk6LH1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTNCBWYXJpYW50cyBhbmQgUmVsYXRlZCBXb3JrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgUzQgcGFwZXIgc3Bhd25lZCBhIGZhbWlseSBvZiBzaW1wbGlmaWVkIHZhcmlhbnRzLiBTNEQgKGRpYWdvbmFsIFM0KSByZXN0cmljdHMgQSB0byBiZSBkaWFnb25hbCwgZWxpbWluYXRpbmcgdGhlIG5lZWQgZm9yIHRoZSBOUExSIGRlY29tcG9zaXRpb24gYW5kIG1ha2luZyB0aGUgbW9kZWwgZWFzaWVyIHRvIGltcGxlbWVudCB3aGlsZSByZXRhaW5pbmcgbW9zdCBwZXJmb3JtYW5jZS4gRFNTIChEaWFnb25hbCBTdGF0ZSBTcGFjZXMpIGluZGVwZW5kZW50bHkgcHJvcG9zZWQgZGlhZ29uYWwgQS4gUzUgKFNpbXBsaWZpZWQgUzQpIHVzZXMgYSBtdWx0aS1pbnB1dCBtdWx0aS1vdXRwdXQgKE1JTU8pIFNTTSB3aXRoIGRpYWdvbmFsIEEgYW5kIGEgcGFyYWxsZWwgc2NhbiBmb3IgdHJhaW5pbmcuIExpcXVpZCBTNCBjb21iaW5lcyBTU01zIHdpdGggbGlxdWlkIHRpbWUtY29uc3RhbnQgbmV0d29ya3MgZm9yIGFkYXB0aXZlIGR5bmFtaWNzLiBBbGwgdmFyaWFudHMgaW5oZXJpdCBTNFx1MDAyN3Mga2V5IGFkdmFudGFnZTogdGhleSBjYW4gc3dpdGNoIGJldHdlZW4gcmVjdXJyZW50IG1vZGUgKE8oMSkgcGVyIHN0ZXAsIGlkZWFsIGZvciBpbmZlcmVuY2UpIGFuZCBjb252b2x1dGlvbmFsIG1vZGUgKE8oTCBsb2cgTCksIGlkZWFsIGZvciB0cmFpbmluZykuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTNEQ6IGRpYWdvbmFsIEEg4oCUIHNpbXBsZXIsIG5lYXJseSBpZGVudGljYWwgTFJBIHBlcmZvcm1hbmNlIHRvIGZ1bGwgUzQiLCJEU1M6IGluZGVwZW5kZW50bHkgZGVyaXZlZCBkaWFnb25hbCBTU00gd2l0aCBzaW1pbGFyIGZvcm11bGF0aW9uIiwiUzU6IE1JTU8gU1NNIHdpdGggcGFyYWxsZWwgc2NhbiDigJQgdmVjdG9yaXplZCBhY3Jvc3MgZF9tb2RlbCBjaGFubmVscyIsIkxpcXVpZCBTNDogdGltZS12YXJ5aW5nIHN0YXRlIHRyYW5zaXRpb25zIGZyb20gbGlxdWlkIG5ldHdvcmtzIiwiTWFtYmE6IGV4dGVuZHMgUzQgd2l0aCBpbnB1dC1kZXBlbmRlbnQgKHNlbGVjdGl2ZSkgdHJhbnNpdGlvbnMg4oCUIHNlZSBtYW1iYS1zZWxlY3RpdmUtc3NtIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJOTiB2cyBUcmFuc2Zvcm1lciB2cyBTNCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTNCBvY2N1cGllcyBhIHVuaXF1ZSBwb3NpdGlvbiBpbiB0aGUgc2VxdWVuY2UgbW9kZWxpbmcgbGFuZHNjYXBlLiBVbmxpa2UgUk5OcyBpdCB0cmFpbnMgaW4gcGFyYWxsZWwgKHZpYSBnbG9iYWwgY29udm9sdXRpb24pLCBhbmQgdW5saWtlIFRyYW5zZm9ybWVycyBpdHMgaW5mZXJlbmNlIGlzIE8oMSkgcGVyIHN0ZXAgd2l0aCBhIGZpeGVkLXNpemUgc3RhdGUg4oCUIG5vIEtWIGNhY2hlIHRoYXQgZ3Jvd3Mgd2l0aCBzZXF1ZW5jZSBsZW5ndGguIFRoZSBMb25nIFJhbmdlIEFyZW5hIChMUkEpIGJlbmNobWFyaywgd2hpY2ggdGVzdHMgb24gc2VxdWVuY2VzIHVwIHRvIGxlbmd0aCAxNiwzODQsIHNob3dlZCB0aGF0IFM0IHdhcyB0aGUgZmlyc3QgbW9kZWwgdG8gbWF0Y2ggb3IgZXhjZWVkIGF0dGVudGlvbiBvbiBhbGwgc2l4IHRhc2tzIGluY2x1ZGluZyB0aGUgbm90b3Jpb3VzbHkgZGlmZmljdWx0IFBhdGgtWCB0YXNrIChzZXF1ZW5jZXMgb2YgMTYsMzg0IHBpeGVscyBmb3JtaW5nIHBhdGhzIHRvIGNsYXNzaWZ5KSwgd2hlcmUgdHJhbnNmb3JtZXJzIHNjb3JlZCBhdCBjaGFuY2UgbGV2ZWwuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiUk5OIChMU1RNL0dSVSkiLCJUcmFuc2Zvcm1lciIsIlM0IiwiTWFtYmEiXSwicm93cyI6W1siVHJhaW5pbmcgcGFyYWxsZWxpc20iLCJTZXF1ZW50aWFsIChzbG93KSIsIkZ1bGx5IHBhcmFsbGVsIiwiTyhMIGxvZyBMKSBjb252IiwiUGFyYWxsZWwgc2NhbiJdLFsiSW5mZXJlbmNlIHBlciBzdGVwIiwiTyhOKSIsIk8oTMK3ZCkiLCJPKE4pIiwiTyhOKSJdLFsiTG9uZy1yYW5nZSBtb2RlbGluZyIsIlBvb3IgKHZhbmlzaGluZyBncmFkKSIsIlN0cm9uZyAoZnVsbCBhdHRlbnRpb24pIiwiU3Ryb25nIChIaVBQTykiLCJTdHJvbmcgKHNlbGVjdGl2ZSkiXSxbIktWIGNhY2hlIGF0IGluZmVyZW5jZSIsIk5vIChmaXhlZCBzdGF0ZSkiLCJPKEwpIGdyb3dzIiwiTm8gKGZpeGVkIHN0YXRlKSIsIk5vIChmaXhlZCBzdGF0ZSkiXSxbIlR5cGljYWwgbWF4IGxlbmd0aCIsIjFL4oCTMTBLIiwiNTEy4oCTOEsiLCIxNksrIiwiMTZLKyJdLFsiTFJBIFBhdGgtWCBhY2N1cmFjeSIsIn41MCUgKGNoYW5jZSkiLCJ+NTAlIChjaGFuY2UpIiwifjk2JSIsIn45OCUiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUzQgZGVtb25zdHJhdGVkIHRoYXQgdGhlIGxvbmctc3RhbmRpbmcgZGljaG90b215IGJldHdlZW4gcGFyYWxsZWxpemFibGUgdHJhaW5pbmcgKFRyYW5zZm9ybWVyKSBhbmQgZWZmaWNpZW50IHJlY3VycmVudCBpbmZlcmVuY2UgKFJOTikgY291bGQgYmUgcmVzb2x2ZWQuIFRoZSBzdHJ1Y3R1cmVkIFNTTSBmcmFtZXdvcmsgcHJvdmlkZXMgdGhlIGJlc3Qgb2YgYm90aDogdHJhaW4gbGlrZSBhIENOTiAoZnVsbHkgcGFyYWxsZWwgY29udm9sdXRpb25hbCBwYXNzKSwgaW5mZXIgbGlrZSBhbiBSTk4gKGNvbnN0YW50LW1lbW9yeSByZWN1cnJlbmNlKS4gVGhpcyBpbnNpZ2h0IHNwYXJrZWQgYSB3YXZlIG9mIFNTTS1iYXNlZCBhcmNoaXRlY3R1cmVzLCBjdWxtaW5hdGluZyBpbiBNYW1iYSBhbmQgUmV0TmV0LCB3aGljaCBmdXJ0aGVyIGFkZHJlc3MgY29udGVudC1zZWxlY3Rpdml0eSBhbmQgbGFuZ3VhZ2UgbW9kZWxpbmcgcmVzcGVjdGl2ZWx5LiJ9XQ=="
---
# S4 — Structured State Space Sequence Models

State space models (SSMs) have a long history in control theory and signal processing, but applying them to deep sequence modeling required solving three hard problems simultaneously: how to initialize the state matrix A to capture long-range dependencies, how to train efficiently without sequential recurrence, and how to handle very long sequences (L = 16,000+) where transformers are prohibitively expensive. S4 (Gu et al., 2021) solved all three by combining the HiPPO framework for A initialization with a structured normal plus low-rank (NPLR) representation that admits an O(L log L) convolutional computation.

## State Space Models — The Continuous-Time Foundation

A linear time-invariant SSM maps input u(t) to output y(t) through a latent state x(t) ∈ ℝᴺ. The continuous-time equations are x'(t) = Ax(t) + Bu(t) and y(t) = Cx(t) + Du(t), where A ∈ ℝ^{N×N}, B ∈ ℝ^{N×1}, C ∈ ℝ^{1×N}, D ∈ ℝ. For discrete sequences, the system is discretized using zero-order hold (ZOH): Ā = exp(ΔA), B̄ = (Ā - I)A⁻¹B, giving the recurrence xₙ = Āxₙ₋₁ + B̄uₙ and yₙ = Cxₙ + Duₙ. The step size Δ controls the time resolution and is a learnable parameter.

- N = state dimension (typically 64–256): controls memory capacity of the SSM
- Ā ∈ ℝ^{N×N}: discretized state transition — determines what the state remembers
- B̄ ∈ ℝ^{N×1}: input projection — how new input modifies the state
- C ∈ ℝ^{1×N}: output projection — how state maps to scalar output
- Recurrent mode: O(N) per step for inference; Convolutional mode: O(L log L) for training

## The HiPPO Framework for Long-Range Memory

The key insight behind S4 is that naive random initialization of A leads to poor long-range memory — the state rapidly forgets distant inputs. HiPPO (High-order Polynomial Projection Operators, Gu et al. 2020) provides a principled initialization: A is chosen so that the hidden state x(t) at any time t is the optimal polynomial approximation of the input history u(0:t) in a Legendre polynomial basis. HiPPO-LegT sets A[n,k] = -(2n+1)^{0.5}(2k+1)^{0.5} for k ≤ n. This matrix has a structured skew-Hermitian plus diagonal form that can be diagonalized efficiently, enabling O(L log L) convolution via Cauchy kernel computation.

> **Why the A Matrix Matters**: For an SSM to learn long-range dependencies, the state transition Ā must preserve information from far-distant inputs. Random A matrices have eigenvalues with large negative real parts — the state decays exponentially fast. HiPPO initializes A so its eigenvalues cluster near the imaginary axis, enabling the state to maintain polynomial approximations of the entire input history without exponential forgetting.

## Code 1 — Discrete SSM in Recurrent Mode

```python
import numpy as np
from scipy.linalg import expm

def discretize_zoh(A, B, delta):
    """Zero-order hold discretization: Abar=exp(delta*A), Bbar=(Abar-I)A^{-1}B."""
    N = A.shape[0]
    A_bar = expm(delta * A)
    B_bar = np.linalg.solve(A, (A_bar - np.eye(N)) @ B)
    return A_bar, B_bar

def ssm_recurrent(A_bar, B_bar, C, u_seq):
    """
    Run discrete SSM in recurrent mode: O(N) per step.
    A_bar: (N,N), B_bar: (N,1), C: (1,N), u_seq: (L,)
    Returns y: (L,)
    """
    N = A_bar.shape[0]
    x = np.zeros(N)
    y = []
    for u in u_seq:
        x = A_bar @ x + B_bar.ravel() * u   # state update
        y.append((C @ x).item())             # output
    return np.array(y)

# 4-state stable diagonal system
np.random.seed(42)
N = 4
A = -np.diag(np.arange(1, N+1, dtype=float))   # stable: all eigenvalues negative real
B = np.ones((N, 1))
C = np.random.randn(1, N) * 0.1
delta = 0.01
A_bar, B_bar = discretize_zoh(A, B, delta)
L = 200
u = np.sin(np.linspace(0, 4 * np.pi, L))
y = ssm_recurrent(A_bar, B_bar, C, u)
print(f"Input: {u.shape}, Output: {y.shape}")
print(f"Output range: [{y.min():.4f}, {y.max():.4f}]")
```

## Code 2 — SSM in Convolutional Mode

The SSM can also be viewed as a global convolutional filter: the impulse response K[l] = C·Āˡ·B̄ gives the convolution kernel, and the output y = K * u. This is because the recurrence unrolls as yₙ = Σₗ C·Āˡ·B̄·uₙ₋ₗ — exactly a (causal) convolution. The kernel has length L (same as the sequence), making it a global convolution. Computing it naively costs O(L·N²) due to the matrix powers, but S4 uses the fact that the diagonalized A enables fast Cauchy kernel computation. In practice, FFT-based convolution runs in O(L log L).

```python
import numpy as np

def ssm_kernel(A_bar, B_bar, C, L):
    """Compute global SSM convolution kernel K[l] = C @ A_bar^l @ B_bar."""
    N = A_bar.shape[0]
    K = np.zeros(L)
    A_pow = np.eye(N)
    for l in range(L):
        K[l] = (C @ A_pow @ B_bar).item()
        A_pow = A_pow @ A_bar
    return K

def ssm_conv_forward(K, u):
    """Apply SSM as causal convolution: y = K * u (output length = L)."""
    return np.convolve(K, u)[:len(u)]

def ssm_conv_fft(K, u):
    """FFT-based convolution: O(L log L) — matches causal conv result."""
    L = len(u)
    K_fft = np.fft.rfft(K, n=2*L)
    u_fft = np.fft.rfft(u, n=2*L)
    return np.fft.irfft(K_fft * u_fft, n=2*L)[:L]

# Euler discretization for simplicity (replace with ZOH in practice)
N, L = 4, 128
A = -np.diag(np.arange(1, N+1, dtype=float))
B, C  = np.ones((N, 1)), np.random.randn(1, N) * 0.1
A_bar = np.eye(N) + 0.01 * A
B_bar = 0.01 * B
K = ssm_kernel(A_bar, B_bar, C, L)
u = np.sin(np.linspace(0, 4*np.pi, L))
y_direct = ssm_conv_forward(K, u)
y_fft    = ssm_conv_fft(K, u)
print(f"Kernel: {K.shape}, first 3: {K[:3]}")
print(f"Direct vs FFT max diff: {np.abs(y_direct - y_fft).max():.2e}")
```

## Code 3 — HiPPO Matrix Initialization

```python
import numpy as np
import matplotlib.pyplot as plt

def hippo_legt_matrix(N):
    """HiPPO-LegT A matrix: optimal polynomial approximation of input history."""
    A = np.zeros((N, N))
    for n in range(N):
        for k in range(N):
            if k <= n:
                A[n, k] = -np.sqrt(2*n+1) * np.sqrt(2*k+1)
    return A

def hippo_b_vector(N):
    """HiPPO B vector: b[n] = sqrt(2n+1)."""
    return np.sqrt(np.arange(1, 2*N, 2, dtype=float)).reshape(N, 1)

N = 32
A_hippo = hippo_legt_matrix(N)
B_hippo = hippo_b_vector(N)
eigenvalues = np.linalg.eigvals(A_hippo)
print(f"HiPPO-LegT A shape: {A_hippo.shape}")
print(f"Eigenvalue real range: [{eigenvalues.real.min():.1f}, {eigenvalues.real.max():.1f}]")
print(f"All eigenvalues non-positive real: {(eigenvalues.real <= 1e-8).all()}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].imshow(A_hippo, cmap='RdBu', aspect='auto')
axes[0].set_title(f'HiPPO-LegT A (N={N})')
axes[0].set_xlabel('k'); axes[0].set_ylabel('n')
axes[1].scatter(eigenvalues.real, eigenvalues.imag, c='steelblue', s=50)
axes[1].axvline(0, color='red', linestyle='--', label='stability boundary')
axes[1].set_title('Eigenvalue spectrum (stable if real < 0)')
axes[1].set_xlabel('Real'); axes[1].set_ylabel('Imaginary')
axes[1].legend()
plt.tight_layout()
plt.savefig('hippo_matrix.png', dpi=120)
plt.show()
```

## Code 4 — S4 on Long-Sequence Classification

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class S4Layer(nn.Module):
    """Simplified S4 layer using learned global convolution kernel via FFT."""
    def __init__(self, d_model, seq_len):
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len
        # Learnable convolution kernel (replaces structured SSM kernel in full S4)
        self.kernel = nn.Parameter(torch.randn(d_model, seq_len) * 0.01)
        self.D      = nn.Parameter(torch.ones(d_model))   # skip connection
        self.norm   = nn.LayerNorm(d_model)

    def forward(self, u):
        # u: (B, L, d_model) -> y: (B, L, d_model)
        B, L, d = u.shape
        y = torch.zeros_like(u)
        for i in range(d):
            k      = self.kernel[i, :L]
            k_fft  = torch.fft.rfft(k, n=2*L)
            u_fft  = torch.fft.rfft(u[..., i], n=2*L)
            y[..., i] = torch.fft.irfft(k_fft * u_fft, n=2*L)[:, :L]
        y = y + self.D * u          # skip (D term in SSM)
        return self.norm(y)

# Toy long-range classification task
torch.manual_seed(42)
L, d, B = 1024, 32, 8
model = nn.Sequential(
    S4Layer(d, L),
    nn.Linear(d, 64),
    nn.GELU(),
    nn.Linear(64, 2)
)
dummy_x = torch.randn(B, L, d)
logits  = model(dummy_x).mean(dim=1)      # global average pooling
loss    = nn.CrossEntropyLoss()(logits, torch.randint(0, 2, (B,)))
print(f"S4 output: {logits.shape}, Loss: {loss.item():.4f}")
print(f"Params: {sum(p.numel() for p in model.parameters()):,}")
```

## S4 Variants and Related Work

The S4 paper spawned a family of simplified variants. S4D (diagonal S4) restricts A to be diagonal, eliminating the need for the NPLR decomposition and making the model easier to implement while retaining most performance. DSS (Diagonal State Spaces) independently proposed diagonal A. S5 (Simplified S4) uses a multi-input multi-output (MIMO) SSM with diagonal A and a parallel scan for training. Liquid S4 combines SSMs with liquid time-constant networks for adaptive dynamics. All variants inherit S4's key advantage: they can switch between recurrent mode (O(1) per step, ideal for inference) and convolutional mode (O(L log L), ideal for training).

- S4D: diagonal A — simpler, nearly identical LRA performance to full S4
- DSS: independently derived diagonal SSM with similar formulation
- S5: MIMO SSM with parallel scan — vectorized across d_model channels
- Liquid S4: time-varying state transitions from liquid networks
- Mamba: extends S4 with input-dependent (selective) transitions — see mamba-selective-ssm

## RNN vs Transformer vs S4 Comparison

S4 occupies a unique position in the sequence modeling landscape. Unlike RNNs it trains in parallel (via global convolution), and unlike Transformers its inference is O(1) per step with a fixed-size state — no KV cache that grows with sequence length. The Long Range Arena (LRA) benchmark, which tests on sequences up to length 16,384, showed that S4 was the first model to match or exceed attention on all six tasks including the notoriously difficult Path-X task (sequences of 16,384 pixels forming paths to classify), where transformers scored at chance level.

| Property | RNN (LSTM/GRU) | Transformer | S4 | Mamba |
| --- | --- | --- | --- | --- |
| Training parallelism | Sequential (slow) | Fully parallel | O(L log L) conv | Parallel scan |
| Inference per step | O(N) | O(L·d) | O(N) | O(N) |
| Long-range modeling | Poor (vanishing grad) | Strong (full attention) | Strong (HiPPO) | Strong (selective) |
| KV cache at inference | No (fixed state) | O(L) grows | No (fixed state) | No (fixed state) |
| Typical max length | 1K–10K | 512–8K | 16K+ | 16K+ |
| LRA Path-X accuracy | ~50% (chance) | ~50% (chance) | ~96% | ~98% |

S4 demonstrated that the long-standing dichotomy between parallelizable training (Transformer) and efficient recurrent inference (RNN) could be resolved. The structured SSM framework provides the best of both: train like a CNN (fully parallel convolutional pass), infer like an RNN (constant-memory recurrence). This insight sparked a wave of SSM-based architectures, culminating in Mamba and RetNet, which further address content-selectivity and language modeling respectively.

