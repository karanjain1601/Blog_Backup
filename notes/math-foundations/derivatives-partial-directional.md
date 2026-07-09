---
title: "Derivatives, Partial Derivatives, and Directional Derivatives"
slug: "derivatives-partial-directional"
description: "A rigorous treatment of partial derivatives, the gradient vector, directional derivatives, Clairaut's theorem, and the second-order Taylor expansion — with Python and PyTorch examples."
tags: ["calculus", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVyaXZhdGl2ZXMgbWVhc3VyZSByYXRlcyBvZiBjaGFuZ2UuIFdoZW4gYSBmdW5jdGlvbiB0YWtlcyBtdWx0aXBsZSBpbnB1dHMsIHdlIG5lZWQgcmljaGVyIHRvb2xzOiBwYXJ0aWFsIGRlcml2YXRpdmVzIGlzb2xhdGUgb25lIHZhcmlhYmxlIGF0IGEgdGltZSwgdGhlIGdyYWRpZW50IGFzc2VtYmxlcyB0aGVtIGludG8gYSB2ZWN0b3IsIGFuZCBkaXJlY3Rpb25hbCBkZXJpdmF0aXZlcyBhbnN3ZXIgXHUwMDI3aG93IGZhc3QgZG9lcyBmIGNoYW5nZSBpZiBJIG1vdmUgaW4gZGlyZWN0aW9uIHU/XHUwMDI3IFRoZXNlIGlkZWFzIGFyZSB0aGUgYmVkcm9jayBvZiBncmFkaWVudC1iYXNlZCBvcHRpbWl6YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGltaXQgRGVmaW5pdGlvbiBvZiB0aGUgRGVyaXZhdGl2ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG9yZGluYXJ5IGRlcml2YXRpdmUgb2YgZiBhdCB4IGlzIGRlZmluZWQgYXMgdGhlIGxpbWl0IG9mIHRoZSBkaWZmZXJlbmNlIHF1b3RpZW50OiBmXHUwMDI3KHgpID0gbGltX3to4oaSMH0gW2YoeCtoKSAtIGYoeCldIC8gaC4gVGhpcyBjYXB0dXJlcyB0aGUgaW5zdGFudGFuZW91cyByYXRlIG9mIGNoYW5nZS4gSW4gcHJhY3RpY2Ugd2UgdXNlIGZpbml0ZSBkaWZmZXJlbmNlcyAoaCBzbWFsbCBidXQgbm9uemVybykgZm9yIG51bWVyaWNhbCBhcHByb3hpbWF0aW9ucywgd2hpY2ggaW50cm9kdWNlIE8oaCkgZXJyb3IgZm9yIGZvcndhcmQgZGlmZmVyZW5jZXMgYW5kIE8oaMKyKSBmb3IgY2VudHJhbCBkaWZmZXJlbmNlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXJ0aWFsIERlcml2YXRpdmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZjogUuKBvyDihpIgUiwgdGhlIHBhcnRpYWwgZGVyaXZhdGl2ZSDiiIJmL+KIgnjhtaIgaXMgdGhlIG9yZGluYXJ5IGRlcml2YXRpdmUgd2l0aCByZXNwZWN0IHRvIHjhtaIgd2hpbGUgYWxsIG90aGVyIHZhcmlhYmxlcyBhcmUgaGVsZCBmaXhlZC4gTm90YXRpb246IOKIgmYv4oiCeOG1oiBvciBm4oKT4bWiLiBOdW1lcmljYWxseSwgdXNlIGNlbnRyYWwgZGlmZmVyZW5jZXM6IOKIgmYv4oiCeOG1oiDiiYggW2YoeCArIGjCt2XhtaIpIC0gZih4IC0gaMK3ZeG1oildIC8gKDJoKSB3aGVyZSBl4bWiIGlzIHRoZSBpLXRoIHVuaXQgdmVjdG9yLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGYoeCwgeSwgeik6XG4gICAgIyBmKHgseSx6KSA9IHgqKjIgKiB5ICsgc2luKHkqeikgKyBleHAoeilcbiAgICByZXR1cm4geCoqMiAqIHkgKyBucC5zaW4oeSAqIHopICsgbnAuZXhwKHopXG5cbmRlZiBwYXJ0aWFsX2Rlcml2KGZ1bmMsIGFyZ3MsIGlkeCwgaD0xZS01KTpcbiAgICAjIENlbnRyYWwtZGlmZmVyZW5jZTogKGYoeCtoKSAtIGYoeC1oKSkgLyAyaFxuICAgIGZ3ZCA9IGxpc3QoYXJncyk7IGZ3ZFtpZHhdICs9IGhcbiAgICBid2QgPSBsaXN0KGFyZ3MpOyBid2RbaWR4XSAtPSBoXG4gICAgcmV0dXJuIChmdW5jKCpmd2QpIC0gZnVuYygqYndkKSkgLyAoMiAqIGgpXG5cbnBvaW50ID0gKDEuMCwgMi4wLCAwLjUpXG54LCB5LCB6ID0gcG9pbnRcblxuZGZfZHggPSBwYXJ0aWFsX2Rlcml2KGYsIHBvaW50LCAwKVxuZGZfZHkgPSBwYXJ0aWFsX2Rlcml2KGYsIHBvaW50LCAxKVxuZGZfZHogPSBwYXJ0aWFsX2Rlcml2KGYsIHBvaW50LCAyKVxuXG4jIEFuYWx5dGljYWw6IGRmL2R4PTJ4eSwgZGYvZHk9eF4yK3oqY29zKHl6KSwgZGYvZHo9eSpjb3MoeXopK2V4cCh6KVxuZGZfZHhfYSA9IDIgKiB4ICogeVxuZGZfZHlfYSA9IHgqKjIgKyB6ICogbnAuY29zKHkgKiB6KVxuZGZfZHpfYSA9IHkgKiBucC5jb3MoeSAqIHopICsgbnAuZXhwKHopXG5cbnByaW50KFx1MDAyN051bWVyaWNhbDogXHUwMDI3LCBbcm91bmQoZGZfZHgsIDYpLCByb3VuZChkZl9keSwgNiksIHJvdW5kKGRmX2R6LCA2KV0pXG5wcmludChcdTAwMjdBbmFseXRpY2FsOlx1MDAyNywgW3JvdW5kKGRmX2R4X2EsIDYpLCByb3VuZChkZl9keV9hLCA2KSwgcm91bmQoZGZfZHpfYSwgNildKVxuZ3JhZCA9IG5wLmFycmF5KFtkZl9keCwgZGZfZHksIGRmX2R6XSlcbnByaW50KFx1MDAyN0dyYWRpZW50IG1hZ25pdHVkZSB8fG5hYmxhX2Z8fDpcdTAwMjcsIHJvdW5kKG5wLmxpbmFsZy5ub3JtKGdyYWQpLCA2KSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgR3JhZGllbnQgVmVjdG9yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZ3JhZGllbnQg4oiHZih4KSDiiIggUuKBvyBpcyB0aGUgdmVjdG9yIG9mIGFsbCBwYXJ0aWFsIGRlcml2YXRpdmVzOiDiiIdmID0gW+KIgmYv4oiCeOKCgSwgLi4uLCDiiIJmL+KIgnjigpld4bWALiBJdCBwb2ludHMgaW4gdGhlIGRpcmVjdGlvbiBvZiBzdGVlcGVzdCBhc2NlbnQgZnJvbSB4LCBhbmQgaXRzIG1hZ25pdHVkZSDigJbiiIdm4oCWIGdpdmVzIHRoZSBtYXhpbXVtIHJhdGUgb2YgaW5jcmVhc2UuIFRoaXMgaXMgd2h5IGdyYWRpZW50IGRlc2NlbnQgc3VidHJhY3RzIGEgZnJhY3Rpb24gb2Yg4oiHZiBhdCBlYWNoIHN0ZXAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgZl90b3JjaCh4LCB5LCB6KTpcbiAgICAjIGYoeCx5LHopID0geCoqMip5ICsgc2luKHkqeikgKyBleHAoeilcbiAgICByZXR1cm4geCoqMiAqIHkgKyB0b3JjaC5zaW4oeSAqIHopICsgdG9yY2guZXhwKHopXG5cbiMgQ3JlYXRlIHNjYWxhciB0ZW5zb3JzIHdpdGggZ3JhZGllbnQgdHJhY2tpbmdcbnggPSB0b3JjaC50ZW5zb3IoMS4wLCByZXF1aXJlc19ncmFkPVRydWUpXG55ID0gdG9yY2gudGVuc29yKDIuMCwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxueiA9IHRvcmNoLnRlbnNvcigwLjUsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcblxuIyBGb3J3YXJkIHBhc3Ncbm91dCA9IGZfdG9yY2goeCwgeSwgeilcbnByaW50KFx1MDAyN2YoMSwgMiwgMC41KSA9XHUwMDI3LCByb3VuZChvdXQuaXRlbSgpLCA2KSlcblxuIyBCYWNrd2FyZCBwYXNzOiBhbGwgdGhyZWUgcGFydGlhbCBkZXJpdmF0aXZlcyBjb21wdXRlZCBzaW11bHRhbmVvdXNseVxub3V0LmJhY2t3YXJkKClcblxucHJpbnQoXHUwMDI3ZGYvZHggPVx1MDAyNywgcm91bmQoeC5ncmFkLml0ZW0oKSwgNiksIFx1MDAyNyAgKGV4cGVjdGVkOlx1MDAyNywgcm91bmQoMioxLjAqMi4wLCA2KSwgXHUwMDI3KVx1MDAyNylcbnByaW50KFx1MDAyN2RmL2R5ID1cdTAwMjcsIHJvdW5kKHkuZ3JhZC5pdGVtKCksIDYpKVxucHJpbnQoXHUwMDI3ZGYvZHogPVx1MDAyNywgcm91bmQoei5ncmFkLml0ZW0oKSwgNikpXG5cbiMgR3JhZGllbnQgdmVjdG9yIGFuZCBzdGVlcGVzdCBhc2NlbnQgZGlyZWN0aW9uXG5ncmFkX3ZlYyA9IHRvcmNoLnN0YWNrKFt4LmdyYWQsIHkuZ3JhZCwgei5ncmFkXSlcbnN0ZWVwZXN0ID0gZ3JhZF92ZWMgLyB0b3JjaC5ub3JtKGdyYWRfdmVjKVxucHJpbnQoXHUwMDI3R3JhZGllbnQgdmVjdG9yOlx1MDAyNywgW3JvdW5kKHYsIDQpIGZvciB2IGluIGdyYWRfdmVjLnRvbGlzdCgpXSlcbnByaW50KFx1MDAyN1N0ZWVwZXN0IGFzY2VudCB1bml0IHZlY3RvcjpcdTAwMjcsIFtyb3VuZCh2LCA0KSBmb3IgdiBpbiBzdGVlcGVzdC50b2xpc3QoKV0pIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGlyZWN0aW9uYWwgRGVyaXZhdGl2ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBkaXJlY3Rpb25hbCBkZXJpdmF0aXZlIG9mIGYgYXQgeCBpbiBkaXJlY3Rpb24gdSAoYSB1bml0IHZlY3Rvciwg4oCWdeKAlj0xKSBpcyBEX3UgZih4KSA9IGxpbV97aOKGkjB9IFtmKHgraHUpIC0gZih4KV0gLyBoID0g4oiHZih4KSDCtyB1LiBUaGlzIGlzIGp1c3QgdGhlIHByb2plY3Rpb24gb2YgdGhlIGdyYWRpZW50IG9udG8gdS4gQnkgQ2F1Y2h5LVNjaHdhcnosIERfdSBmIOKJpCDigJbiiIdm4oCWIHdpdGggZXF1YWxpdHkgd2hlbiB1ID0g4oiHZi/igJbiiIdm4oCWIOKAlCB0aGUgZ3JhZGllbnQgZGlyZWN0aW9uIG1heGltaXplcyBEX3UgZi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBmMmQoeCwgeSk6XG4gICAgIyBmKHgseSkgPSBzaW4oeCkqY29zKHkpICsgMC4xKih4XjIgKyB5XjIpXG4gICAgcmV0dXJuIG5wLnNpbih4KSAqIG5wLmNvcyh5KSArIDAuMSAqICh4KioyICsgeSoqMilcblxuZGVmIGdyYWRpZW50XzJkKGZ1bmMsIHAsIGg9MWUtNSk6XG4gICAgIyBOdW1lcmljYWwgZ3JhZGllbnQgYXQgcG9pbnQgcCA9IFt4LCB5XVxuICAgIGd4ID0gKGZ1bmMocFswXStoLCBwWzFdKSAtIGZ1bmMocFswXS1oLCBwWzFdKSkgLyAoMipoKVxuICAgIGd5ID0gKGZ1bmMocFswXSwgcFsxXStoKSAtIGZ1bmMocFswXSwgcFsxXS1oKSkgLyAoMipoKVxuICAgIHJldHVybiBucC5hcnJheShbZ3gsIGd5XSlcblxucCA9IG5wLmFycmF5KFsxLjAsIDAuNV0pXG5ncmFkID0gZ3JhZGllbnRfMmQoZjJkLCBwKVxuXG4jIERfdSBmID0gbmFibGFfZiAuIHUgZm9yIGFsbCB1bml0IGRpcmVjdGlvbnNcbmFuZ2xlcyA9IG5wLmxpbnNwYWNlKDAsIDIgKiBucC5waSwgNzIwKVxuZGQgPSBucC5hcnJheShbbnAuZG90KGdyYWQsIG5wLmFycmF5KFtucC5jb3MoYSksIG5wLnNpbihhKV0pKSBmb3IgYSBpbiBhbmdsZXNdKVxuXG5tYXhfaWR4ID0gbnAuYXJnbWF4KGRkKVxubWluX2lkeCA9IG5wLmFyZ21pbihkZClcblxucHJpbnQoXHUwMDI3R3JhZGllbnQgYXRcdTAwMjcsIHAudG9saXN0KCksIFx1MDAyNzpcdTAwMjcsIGdyYWQucm91bmQoNikudG9saXN0KCkpXG5wcmludChcdTAwMjd8fG5hYmxhX2Z8fCA9XHUwMDI3LCByb3VuZChucC5saW5hbGcubm9ybShncmFkKSwgNikpXG5wcmludChcdTAwMjdNYXggRF91IGYgPVx1MDAyNywgcm91bmQoZGRbbWF4X2lkeF0sIDYpLFxuICAgICAgXHUwMDI3YXQgYW5nbGVcdTAwMjcsIHJvdW5kKG5wLmRlZ3JlZXMoYW5nbGVzW21heF9pZHhdKSwgMSksIFx1MDAyN2RlZ1x1MDAyNylcbnByaW50KFx1MDAyN01pbiBEX3UgZiA9XHUwMDI3LCByb3VuZChkZFttaW5faWR4XSwgNiksXG4gICAgICBcdTAwMjdhdCBhbmdsZVx1MDAyNywgcm91bmQobnAuZGVncmVlcyhhbmdsZXNbbWluX2lkeF0pLCAxKSwgXHUwMDI3ZGVnXHUwMDI3KVxucHJpbnQoXHUwMDI3VGhlb3JlbSBjaGVjayAobWF4IERfdSBmIC0gfHxuYWJsYV9mfHwpOlx1MDAyNywgcm91bmQoYWJzKGRkW21heF9pZHhdIC0gbnAubGluYWxnLm5vcm0oZ3JhZCkpLCA4KSkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiR3JhZGllbnQgYXMgU3RlZXBlc3QgQXNjZW50IiwiY29udGVudCI6IkRfdSBmIGlzIG1heGltaXplZCB3aGVuIHUgPSDiiIdmIC8g4oCW4oiHZuKAli4gVGhlcmVmb3JlIHRoZSBncmFkaWVudCBkaXJlY3Rpb24gaXMgYWx3YXlzIHRoZSBkaXJlY3Rpb24gb2Ygc3RlZXBlc3QgYXNjZW50LiBHcmFkaWVudCBkZXNjZW50IG1vdmVzIGluIHRoZSBvcHBvc2l0ZSBkaXJlY3Rpb246IM64IOKGkCDOuCAtIM63wrfiiIdmLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRvdGFsIERlcml2YXRpdmUgdnMgUGFydGlhbCBEZXJpdmF0aXZlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdG90YWwgZGVyaXZhdGl2ZSBhY2NvdW50cyBmb3IgYWxsIGRlcGVuZGVuY2llcy4gSWYgZih4LCB5KSB3aGVyZSB5IGl0c2VsZiBkZXBlbmRzIG9uIHggKGkuZS4sIHkgPSBnKHgpKSwgdGhlbiBkZi9keCA9IOKIgmYv4oiCeCArICjiiIJmL+KIgnkpKGR5L2R4KS4gQSBwYXJ0aWFsIGRlcml2YXRpdmUg4oiCZi/iiIJ4IHRyZWF0cyB5IGFzIGEgY29uc3RhbnQuIFRoaXMgZGlzdGluY3Rpb24gaXMgY3JpdGljYWwgaW4gYmFja3Byb3BhZ2F0aW9uOiB0aGUgY2hhaW4gcnVsZSBzdW1zIGFsbCBwYXRocyBmcm9tIG91dHB1dCB0byBpbnB1dC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVHlwZSIsIk5vdGF0aW9uIiwiRG9tYWluIiwiT3V0cHV0IiwiQ29tcHV0ZWQgVmlhIl0sInJvd3MiOltbIk9yZGluYXJ5IGRlcml2YXRpdmUiLCJmXHUwMDI3KHgpIG9yIGRmL2R4IiwiUiDihpIgUiIsInNjYWxhciIsImxpbWl0IG9yIGZpbml0ZSBkaWZmIl0sWyJQYXJ0aWFsIGRlcml2YXRpdmUiLCLiiIJmL+KIgnjhtaIiLCJS4oG/IOKGkiBSIiwic2NhbGFyIiwiZmluaXRlIGRpZmYgb3IgYXV0b2dyYWQiXSxbIkdyYWRpZW50Iiwi4oiHZiIsIlLigb8g4oaSIFIiLCJuLXZlY3RvciIsIm9uZSBiYWNrd2FyZCBwYXNzIl0sWyJEaXJlY3Rpb25hbCBkZXJpdmF0aXZlIiwiRF91IGYgPSDiiIdmwrd1IiwiUuKBvyDihpIgUiAod2l0aCB1bml0IHUpIiwic2NhbGFyIiwiZG90IHByb2R1Y3Qgd2l0aCBncmFkaWVudCJdLFsiVG90YWwgZGVyaXZhdGl2ZSIsImRmL2R0IGFsb25nIHBhdGgiLCJjdXJ2ZSBpbiBS4oG/Iiwic2NhbGFyIiwiY2hhaW4gcnVsZSBzdW0iXSxbIkphY29iaWFuIiwiSiDiiIggUuG1kMuj4oG/IiwiUuKBvyDihpIgUuG1kCIsIm3Dl24gbWF0cml4IiwibSBiYWNrd2FyZCBwYXNzZXMgb3IgQUQiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNsYWlyYXV0XHUwMDI3cyBUaGVvcmVtIGFuZCBTZWNvbmQtT3JkZXIgUGFydGlhbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzZWNvbmQtb3JkZXIgcGFydGlhbCDiiILCsmYv4oiCeOG1ouKIgnjisbwgbWVhbnM6IGRpZmZlcmVudGlhdGUgZiBmaXJzdCB3aXRoIHJlc3BlY3QgdG8geOKxvCwgdGhlbiB3aXRoIHJlc3BlY3QgdG8geOG1oi4gQ2xhaXJhdXRcdTAwMjdzIHRoZW9yZW0gc3RhdGVzIHRoYXQgaWYgZiBoYXMgY29udGludW91cyBzZWNvbmQtb3JkZXIgcGFydGlhbHMsIHRoZW4gbWl4ZWQgcGFydGlhbHMgY29tbXV0ZTog4oiCwrJmL+KIgnjhtaLiiIJ44rG8ID0g4oiCwrJmL+KIgnjisbziiIJ44bWiLiBUaGlzIGltcGxpZXMgdGhlIEhlc3NpYW4gbWF0cml4IGlzIHN5bW1ldHJpYy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNsYWlyYXV0XHUwMDI3cyB0aGVvcmVtIHJlcXVpcmVzIGNvbnRpbnVpdHkgb2Ygc2Vjb25kLW9yZGVyIHBhcnRpYWxzIGluIGEgbmVpZ2hib3Job29kIiwiVGhlIEhlc3NpYW4gSF97aWp9ID0g4oiCwrJmL+KIgnjhtaLiiIJ44rG8IGlzIHN5bW1ldHJpYyB1bmRlciBDbGFpcmF1dFx1MDAyN3MgY29uZGl0aW9ucyIsIkNvdW50ZXJleGFtcGxlcyBleGlzdCB3aGVuIHBhcnRpYWxzIGFyZSBkaXNjb250aW51b3VzIChyYXJlIGluIE1MIHByYWN0aWNlKSIsIlN5bW1ldHJ5IGhhbHZlcyB0aGUgc3RvcmFnZSBuZWVkZWQ6IHN0b3JlIG9ubHkgdXBwZXIvbG93ZXIgdHJpYW5nbGUgb2YgSCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTZWNvbmQtT3JkZXIgVGF5bG9yIEV4cGFuc2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmVhciBhIHBvaW50IHjigoAsIGEgc21vb3RoIGZ1bmN0aW9uIGlzIGFwcHJveGltYXRlZCBhczogZih44oKAK860KSDiiYggZih44oKAKSArIOKIh2YoeOKCgCnCt860ICsgKDEvMinOtOG1gEgoeOKCgCnOtCArIE8o4oCWzrTigJbCsykuIFRoZSBsaW5lYXIgdGVybSAo4oiHZsK3zrQpIGRyaXZlcyBncmFkaWVudCBkZXNjZW50OyB0aGUgcXVhZHJhdGljIHRlcm0gKM604bWASM60LzIpIGFwcGVhcnMgaW4gTmV3dG9uXHUwMDI3cyBtZXRob2QgYW5kIHRoZSBkZXNjZW50IGxlbW1hICh3aGljaCBib3VuZHMgc3RlcCBzaXplIGZvciBjb252ZXJnZW5jZSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZjJkKHgsIHkpOlxuICAgICMgUXVhZHJhdGljOiBmKHgseSkgPSB4XjIgKyAyKngqeSArIDMqeV4yXG4gICAgcmV0dXJuIHgqKjIgKyAyKngqeSArIDMqeSoqMlxuXG5kZWYgdGF5bG9yMih4MCwgeTAsIGR4LCBkeSk6XG4gICAgIyBmKHgwK2R4LCB5MCtkeSkgYXBwcm94IGYoeDApICsgbmFibGFfZi5kZWx0YSArIDAuNSpkZWx0YV5UKkgqZGVsdGFcbiAgICBmMCA9IGYyZCh4MCwgeTApXG4gICAgZ3JhZCA9IG5wLmFycmF5KFsyKngwICsgMip5MCwgMip4MCArIDYqeTBdKSAgICMgW2RmL2R4LCBkZi9keV1cbiAgICBIID0gbnAuYXJyYXkoW1syLjAsIDIuMF0sIFsyLjAsIDYuMF1dKSAgICAgICAgICAgIyBjb25zdGFudCBIZXNzaWFuXG4gICAgZGVsdGEgPSBucC5hcnJheShbZHgsIGR5XSlcbiAgICByZXR1cm4gZjAgKyBncmFkIEAgZGVsdGEgKyAwLjUgKiAoZGVsdGEgQCBIIEAgZGVsdGEpXG5cbngwLCB5MCA9IDEuMCwgMS4wXG5wcmludChcdTAwMjdFeHBhbmRpbmcgYXJvdW5kICglZywgJWcpLCBmID0gJS40Zlx1MDAyNyAlICh4MCwgeTAsIGYyZCh4MCwgeTApKSlcbnByaW50KFx1MDAyNyUtMTJzICUxMnMgJTE0cyAlMTJzXHUwMDI3ICUgKFx1MDAyN1N0ZXBcdTAwMjcsIFx1MDAyN0V4YWN0XHUwMDI3LCBcdTAwMjdUYXlsb3IgYXBwcm94XHUwMDI3LCBcdTAwMjd8RXJyb3J8XHUwMDI3KSlcblxuZm9yIHMgaW4gWzEuMCwgMC41LCAwLjIsIDAuMSwgMC4wNSwgMC4wMV06XG4gICAgZXhhY3QgID0gZjJkKHgwICsgcywgeTAgKyBzKVxuICAgIGFwcHJveCA9IHRheWxvcjIoeDAsIHkwLCBzLCBzKVxuICAgIGVyciAgICA9IGFicyhleGFjdCAtIGFwcHJveClcbiAgICBzdGVwX3MgPSBcdTAwMjcoJS4yZiwlLjJmKVx1MDAyNyAlIChzLCBzKVxuICAgIHByaW50KFx1MDAyNyUtMTJzICUxMi42ZiAlMTQuNmYgJTEyLjJlXHUwMDI3ICUgKHN0ZXBfcywgZXhhY3QsIGFwcHJveCwgZXJyKSlcblxucHJpbnQoXHUwMDI3XHUwMDI3KVxucHJpbnQoXHUwMDI3UXVhZHJhdGljczogMm5kLW9yZGVyIFRheWxvciBpcyBleGFjdCAoemVybyBlcnJvcikuXHUwMDI3KVxucHJpbnQoXHUwMDI3R2VuZXJhbCBmOiBlcnJvciBpcyBPKHx8ZGVsdGF8fF4zKSAtLSBjdWJpY2FsbHkgc21hbGwgZm9yIHNtYWxsIHN0ZXBzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJKYWNvYmlhbiBmb3IgVmVjdG9yLVZhbHVlZCBGdW5jdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBmOiBS4oG/IOKGkiBS4bWQLCB0aGUgSmFjb2JpYW4gSiDiiIggUuG1kMuj4oG/IGhhcyBKX3tpan0gPSDiiIJm4bWiL+KIgnjisbwuIFJvdyBpIG9mIEogaXMgdGhlIGdyYWRpZW50IG9mIHRoZSBpLXRoIG91dHB1dCBm4bWiLiBUaGUgSmFjb2JpYW4gZ2VuZXJhbGl6ZXMgdGhlIGdyYWRpZW50IChtPTEpIGFuZCBhcmlzZXMgaW4gc2Vuc2l0aXZpdHkgYW5hbHlzaXMsIG5ldXJhbCB0YW5nZW50IGtlcm5lbHMsIGFuZCBjb21wdXRpbmcgaG93IHBlcnR1cmJhdGlvbnMgaW4gaW5wdXRzIHByb3BhZ2F0ZSB0byB2ZWN0b3Igb3V0cHV0cy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkphY29iaWFuIGluIEJhY2twcm9wYWdhdGlvbiIsImNvbnRlbnQiOiJXaGVuIGEgbGF5ZXIgbWFwcyB4IOKIiCBS4oG/IHRvIHkgPSBmKHgpIOKIiCBS4bWQLCB0aGUgbG9jYWwgSmFjb2JpYW4gSiB0ZWxscyB1cyBob3cgdG8gcHJvcGFnYXRlIHVwc3RyZWFtIGdyYWRpZW50czogZEwvZHggPSBK4bWAIChkTC9keSkuIFdlIHJhcmVseSBmb3JtIEogZXhwbGljaXRseSDigJQgd2UgaW1wbGVtZW50IEotdmVjdG9yIHByb2R1Y3RzIGRpcmVjdGx5IGZvciBlZmZpY2llbmN5LiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZXNlIGNvbmNlcHRzIHVuaWZ5IHVuZGVyIG9uZSBwcmluY2lwbGU6IGRlcml2YXRpdmVzIGFyZSBsaW5lYXIgbWFwcy4gVGhlIGdyYWRpZW50LCBKYWNvYmlhbiwgYW5kIEhlc3NpYW4gYXJlIGFsbCByZXByZXNlbnRhdGlvbnMgb2YgZmlyc3QtIG9yIHNlY29uZC1vcmRlciBsaW5lYXIgYXBwcm94aW1hdGlvbnMgdG8gZiBhdCBhIHBvaW50LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUGFydGlhbCBkZXJpdmF0aXZlOiBkaWZmZXJlbnRpYXRlIHcuci50LiBvbmUgdmFyaWFibGUsIGZyZWV6ZSB0aGUgcmVzdCIsIkdyYWRpZW50ID0gdmVjdG9yIG9mIGFsbCBwYXJ0aWFsczsgcG9pbnRzIGluIHN0ZWVwZXN0IGFzY2VudCBkaXJlY3Rpb24iLCJEaXJlY3Rpb25hbCBkZXJpdmF0aXZlIERfdSBmID0g4oiHZiDCtyB1OyBtYXhpbWl6ZWQgd2hlbiB1ID0g4oiHZi/igJbiiIdm4oCWIiwiQ2xhaXJhdXRcdTAwMjdzIHRoZW9yZW06IG1peGVkIHBhcnRpYWxzIGNvbW11dGUg4oaSIEhlc3NpYW4gaXMgc3ltbWV0cmljIiwiU2Vjb25kLW9yZGVyIFRheWxvcjogZih4K860KSDiiYggZih4KSArIOKIh2bCt860ICsgzrThtYBIzrQvMiIsIkphY29iaWFuIGdlbmVyYWxpemVzIGdyYWRpZW50IHRvIHZlY3Rvci12YWx1ZWQgZnVuY3Rpb25zIl19XQ=="
---
# Derivatives, Partial Derivatives, and Directional Derivatives

Derivatives measure rates of change. When a function takes multiple inputs, we need richer tools: partial derivatives isolate one variable at a time, the gradient assembles them into a vector, and directional derivatives answer 'how fast does f change if I move in direction u?' These ideas are the bedrock of gradient-based optimization.

## Limit Definition of the Derivative

The ordinary derivative of f at x is defined as the limit of the difference quotient: f'(x) = lim_{h→0} [f(x+h) - f(x)] / h. This captures the instantaneous rate of change. In practice we use finite differences (h small but nonzero) for numerical approximations, which introduce O(h) error for forward differences and O(h²) for central differences.

## Partial Derivatives

For f: Rⁿ → R, the partial derivative ∂f/∂xᵢ is the ordinary derivative with respect to xᵢ while all other variables are held fixed. Notation: ∂f/∂xᵢ or fₓᵢ. Numerically, use central differences: ∂f/∂xᵢ ≈ [f(x + h·eᵢ) - f(x - h·eᵢ)] / (2h) where eᵢ is the i-th unit vector.

```python
import numpy as np

def f(x, y, z):
    # f(x,y,z) = x**2 * y + sin(y*z) + exp(z)
    return x**2 * y + np.sin(y * z) + np.exp(z)

def partial_deriv(func, args, idx, h=1e-5):
    # Central-difference: (f(x+h) - f(x-h)) / 2h
    fwd = list(args); fwd[idx] += h
    bwd = list(args); bwd[idx] -= h
    return (func(*fwd) - func(*bwd)) / (2 * h)

point = (1.0, 2.0, 0.5)
x, y, z = point

df_dx = partial_deriv(f, point, 0)
df_dy = partial_deriv(f, point, 1)
df_dz = partial_deriv(f, point, 2)

# Analytical: df/dx=2xy, df/dy=x^2+z*cos(yz), df/dz=y*cos(yz)+exp(z)
df_dx_a = 2 * x * y
df_dy_a = x**2 + z * np.cos(y * z)
df_dz_a = y * np.cos(y * z) + np.exp(z)

print('Numerical: ', [round(df_dx, 6), round(df_dy, 6), round(df_dz, 6)])
print('Analytical:', [round(df_dx_a, 6), round(df_dy_a, 6), round(df_dz_a, 6)])
grad = np.array([df_dx, df_dy, df_dz])
print('Gradient magnitude ||nabla_f||:', round(np.linalg.norm(grad), 6))
```

## The Gradient Vector

The gradient ∇f(x) ∈ Rⁿ is the vector of all partial derivatives: ∇f = [∂f/∂x₁, ..., ∂f/∂xₙ]ᵀ. It points in the direction of steepest ascent from x, and its magnitude ‖∇f‖ gives the maximum rate of increase. This is why gradient descent subtracts a fraction of ∇f at each step.

```python
import torch

def f_torch(x, y, z):
    # f(x,y,z) = x**2*y + sin(y*z) + exp(z)
    return x**2 * y + torch.sin(y * z) + torch.exp(z)

# Create scalar tensors with gradient tracking
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)
z = torch.tensor(0.5, requires_grad=True)

# Forward pass
out = f_torch(x, y, z)
print('f(1, 2, 0.5) =', round(out.item(), 6))

# Backward pass: all three partial derivatives computed simultaneously
out.backward()

print('df/dx =', round(x.grad.item(), 6), '  (expected:', round(2*1.0*2.0, 6), ')')
print('df/dy =', round(y.grad.item(), 6))
print('df/dz =', round(z.grad.item(), 6))

# Gradient vector and steepest ascent direction
grad_vec = torch.stack([x.grad, y.grad, z.grad])
steepest = grad_vec / torch.norm(grad_vec)
print('Gradient vector:', [round(v, 4) for v in grad_vec.tolist()])
print('Steepest ascent unit vector:', [round(v, 4) for v in steepest.tolist()])
```

## Directional Derivatives

The directional derivative of f at x in direction u (a unit vector, ‖u‖=1) is D_u f(x) = lim_{h→0} [f(x+hu) - f(x)] / h = ∇f(x) · u. This is just the projection of the gradient onto u. By Cauchy-Schwarz, D_u f ≤ ‖∇f‖ with equality when u = ∇f/‖∇f‖ — the gradient direction maximizes D_u f.

```python
import numpy as np

def f2d(x, y):
    # f(x,y) = sin(x)*cos(y) + 0.1*(x^2 + y^2)
    return np.sin(x) * np.cos(y) + 0.1 * (x**2 + y**2)

def gradient_2d(func, p, h=1e-5):
    # Numerical gradient at point p = [x, y]
    gx = (func(p[0]+h, p[1]) - func(p[0]-h, p[1])) / (2*h)
    gy = (func(p[0], p[1]+h) - func(p[0], p[1]-h)) / (2*h)
    return np.array([gx, gy])

p = np.array([1.0, 0.5])
grad = gradient_2d(f2d, p)

# D_u f = nabla_f . u for all unit directions
angles = np.linspace(0, 2 * np.pi, 720)
dd = np.array([np.dot(grad, np.array([np.cos(a), np.sin(a)])) for a in angles])

max_idx = np.argmax(dd)
min_idx = np.argmin(dd)

print('Gradient at', p.tolist(), ':', grad.round(6).tolist())
print('||nabla_f|| =', round(np.linalg.norm(grad), 6))
print('Max D_u f =', round(dd[max_idx], 6),
      'at angle', round(np.degrees(angles[max_idx]), 1), 'deg')
print('Min D_u f =', round(dd[min_idx], 6),
      'at angle', round(np.degrees(angles[min_idx]), 1), 'deg')
print('Theorem check (max D_u f - ||nabla_f||):', round(abs(dd[max_idx] - np.linalg.norm(grad)), 8))
```

> **Gradient as Steepest Ascent**: D_u f is maximized when u = ∇f / ‖∇f‖. Therefore the gradient direction is always the direction of steepest ascent. Gradient descent moves in the opposite direction: θ ← θ - η·∇f.

## Total Derivative vs Partial Derivative

The total derivative accounts for all dependencies. If f(x, y) where y itself depends on x (i.e., y = g(x)), then df/dx = ∂f/∂x + (∂f/∂y)(dy/dx). A partial derivative ∂f/∂x treats y as a constant. This distinction is critical in backpropagation: the chain rule sums all paths from output to input.

| Type | Notation | Domain | Output | Computed Via |
| --- | --- | --- | --- | --- |
| Ordinary derivative | f'(x) or df/dx | R → R | scalar | limit or finite diff |
| Partial derivative | ∂f/∂xᵢ | Rⁿ → R | scalar | finite diff or autograd |
| Gradient | ∇f | Rⁿ → R | n-vector | one backward pass |
| Directional derivative | D_u f = ∇f·u | Rⁿ → R (with unit u) | scalar | dot product with gradient |
| Total derivative | df/dt along path | curve in Rⁿ | scalar | chain rule sum |
| Jacobian | J ∈ Rᵐˣⁿ | Rⁿ → Rᵐ | m×n matrix | m backward passes or AD |

## Clairaut's Theorem and Second-Order Partials

The second-order partial ∂²f/∂xᵢ∂xⱼ means: differentiate f first with respect to xⱼ, then with respect to xᵢ. Clairaut's theorem states that if f has continuous second-order partials, then mixed partials commute: ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ. This implies the Hessian matrix is symmetric.

- Clairaut's theorem requires continuity of second-order partials in a neighborhood
- The Hessian H_{ij} = ∂²f/∂xᵢ∂xⱼ is symmetric under Clairaut's conditions
- Counterexamples exist when partials are discontinuous (rare in ML practice)
- Symmetry halves the storage needed: store only upper/lower triangle of H

## Second-Order Taylor Expansion

Near a point x₀, a smooth function is approximated as: f(x₀+δ) ≈ f(x₀) + ∇f(x₀)·δ + (1/2)δᵀH(x₀)δ + O(‖δ‖³). The linear term (∇f·δ) drives gradient descent; the quadratic term (δᵀHδ/2) appears in Newton's method and the descent lemma (which bounds step size for convergence).

```python
import numpy as np

def f2d(x, y):
    # Quadratic: f(x,y) = x^2 + 2*x*y + 3*y^2
    return x**2 + 2*x*y + 3*y**2

def taylor2(x0, y0, dx, dy):
    # f(x0+dx, y0+dy) approx f(x0) + nabla_f.delta + 0.5*delta^T*H*delta
    f0 = f2d(x0, y0)
    grad = np.array([2*x0 + 2*y0, 2*x0 + 6*y0])   # [df/dx, df/dy]
    H = np.array([[2.0, 2.0], [2.0, 6.0]])           # constant Hessian
    delta = np.array([dx, dy])
    return f0 + grad @ delta + 0.5 * (delta @ H @ delta)

x0, y0 = 1.0, 1.0
print('Expanding around (%g, %g), f = %.4f' % (x0, y0, f2d(x0, y0)))
print('%-12s %12s %14s %12s' % ('Step', 'Exact', 'Taylor approx', '|Error|'))

for s in [1.0, 0.5, 0.2, 0.1, 0.05, 0.01]:
    exact  = f2d(x0 + s, y0 + s)
    approx = taylor2(x0, y0, s, s)
    err    = abs(exact - approx)
    step_s = '(%.2f,%.2f)' % (s, s)
    print('%-12s %12.6f %14.6f %12.2e' % (step_s, exact, approx, err))

print('')
print('Quadratics: 2nd-order Taylor is exact (zero error).')
print('General f: error is O(||delta||^3) -- cubically small for small steps.')
```

## Jacobian for Vector-Valued Functions

For f: Rⁿ → Rᵐ, the Jacobian J ∈ Rᵐˣⁿ has J_{ij} = ∂fᵢ/∂xⱼ. Row i of J is the gradient of the i-th output fᵢ. The Jacobian generalizes the gradient (m=1) and arises in sensitivity analysis, neural tangent kernels, and computing how perturbations in inputs propagate to vector outputs.

> **Jacobian in Backpropagation**: When a layer maps x ∈ Rⁿ to y = f(x) ∈ Rᵐ, the local Jacobian J tells us how to propagate upstream gradients: dL/dx = Jᵀ (dL/dy). We rarely form J explicitly — we implement J-vector products directly for efficiency.

---

These concepts unify under one principle: derivatives are linear maps. The gradient, Jacobian, and Hessian are all representations of first- or second-order linear approximations to f at a point.

- Partial derivative: differentiate w.r.t. one variable, freeze the rest
- Gradient = vector of all partials; points in steepest ascent direction
- Directional derivative D_u f = ∇f · u; maximized when u = ∇f/‖∇f‖
- Clairaut's theorem: mixed partials commute → Hessian is symmetric
- Second-order Taylor: f(x+δ) ≈ f(x) + ∇f·δ + δᵀHδ/2
- Jacobian generalizes gradient to vector-valued functions

