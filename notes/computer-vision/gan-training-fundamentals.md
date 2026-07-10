---
title: "GAN Training Fundamentals: Minimax Objective and Stability"
slug: "gan-training-fundamentals"
description: ""
tags: ["gan", "generative-models", "deep-learning", "computer-vision"]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImgyIiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHZW5lcmF0aXZlIEFkdmVyc2FyaWFsIE5ldHdvcmtzIHBpdCB0d28gbmV1cmFsIG5ldHdvcmtzIGFnYWluc3QgZWFjaCBvdGhlcjogYSBnZW5lcmF0b3IgdGhhdCBzeW50aGVzaXplcyBmYWtlIHNhbXBsZXMgYW5kIGEgZGlzY3JpbWluYXRvciB0aGF0IHRyaWVzIHRvIHRlbGwgcmVhbCBmcm9tIGZha2UuIFRoZSBpbnRlcnBsYXkgYmV0d2VlbiB0aGVtIGRyaXZlcyBib3RoIG5ldHdvcmtzIHRvIGltcHJvdmUsIHVsdGltYXRlbHkgcHJvZHVjaW5nIGEgZ2VuZXJhdG9yIGNhcGFibGUgb2YgY3JlYXRpbmcgaGlnaGx5IHJlYWxpc3RpYyBpbWFnZXMgaW5kaXN0aW5ndWlzaGFibGUgZnJvbSByZWFsIGRhdGEuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHQU5zIGhhdmUgYmVjb21lIGEgY29ybmVyc3RvbmUgb2YgZ2VuZXJhdGl2ZSB2aXNpb24gcmVzZWFyY2gsIGVuYWJsaW5nIHRhc2tzIGxpa2UgaW1hZ2Ugc3ludGhlc2lzLCBzdHlsZSB0cmFuc2Zlciwgc3VwZXItcmVzb2x1dGlvbiwgYW5kIGRhdGEgYXVnbWVudGF0aW9uLiBVbmRlcnN0YW5kaW5nIHRoZSBtaW5pbWF4IG9iamVjdGl2ZSBhbmQgdHJhaW5pbmcgZHluYW1pY3MgaXMgZXNzZW50aWFsIGJlZm9yZSB3b3JraW5nIHdpdGggYW55IEdBTiB2YXJpYW50IGluIHByYWN0aWNlLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6Ik1pbmltYXggT2JqZWN0aXZlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgR0FOIG9iamVjdGl2ZSBpcyBhIG1pbmltYXggZ2FtZTogdGhlIGRpc2NyaW1pbmF0b3IgRCBtYXhpbWl6ZXMgaXRzIGFiaWxpdHkgdG8gZGlzdGluZ3Vpc2ggcmVhbCBmcm9tIGZha2UsIHdoaWxlIHRoZSBnZW5lcmF0b3IgRyBtaW5pbWl6ZXMgdGhlIGRpc2NyaW1pbmF0b3JcdTAwMjdzIHN1Y2Nlc3MuIEZvcm1hbGx5LCBtaW5fRyBtYXhfRCBFW2xvZyBEKHgpXSArIEVbbG9nKDEgLSBEKEcoeikpKV0sIHdoZXJlIHggaXMgcmVhbCBkYXRhIGFuZCB6IGlzIHJhbmRvbSBub2lzZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGdhbl9sb3NzZXMoRCwgRywgcmVhbCwgeik6XG4gICAgb25lcyAgPSB0b3JjaC5vbmVzKHJlYWwuc2l6ZSgwKSwgMSwgZGV2aWNlPXJlYWwuZGV2aWNlKVxuICAgIHplcm9zID0gdG9yY2guemVyb3MocmVhbC5zaXplKDApLCAxLCBkZXZpY2U9cmVhbC5kZXZpY2UpXG4gICAgZmFrZSAgPSBHKHopLmRldGFjaCgpXG4gICAgRF9sb3NzID0gRi5iaW5hcnlfY3Jvc3NfZW50cm9weShEKHJlYWwpLCBvbmVzKSBcXFxuICAgICAgICAgICArIEYuYmluYXJ5X2Nyb3NzX2VudHJvcHkoRChmYWtlKSwgemVyb3MpXG4gICAgR19sb3NzID0gRi5iaW5hcnlfY3Jvc3NfZW50cm9weShEKEcoeikpLCBvbmVzKVxuICAgIHJldHVybiBEX2xvc3MsIEdfbG9zcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIE5hc2ggZXF1aWxpYnJpdW0gb2YgdGhpcyBnYW1lIGlzIHJlYWNoZWQgd2hlbiB0aGUgZ2VuZXJhdG9yIHBlcmZlY3RseSByZXBsaWNhdGVzIHRoZSByZWFsIGRpc3RyaWJ1dGlvbiBhbmQgdGhlIGRpc2NyaW1pbmF0b3Igb3V0cHV0cyAwLjUgZXZlcnl3aGVyZS4gSW4gcHJhY3RpY2UsIHRyYWluaW5nIHJhcmVseSByZWFjaGVzIHRoaXMgaWRlYWwgZXF1aWxpYnJpdW0gYW5kIG9zY2lsbGF0ZXMgb3IgZGl2ZXJnZXMsIHdoaWNoIG1vdGl2YXRlcyB0aGUgbWFueSBzdGFiaWxpdHkgaW1wcm92ZW1lbnRzIGRldmVsb3BlZCBvdmVyIHRoZSB5ZWFycy4ifSx7InR5cGUiOiJoMiIsImNvbnRlbnQiOiJHZW5lcmF0b3IgYW5kIERpc2NyaW1pbmF0b3IifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIERDR0FOLCB0aGUgZ2VuZXJhdG9yIHVzZXMgYSBzZXJpZXMgb2YgdHJhbnNwb3NlZCBjb252b2x1dGlvbnMgKHN0cmlkZWQgdXBzYW1wbGluZykgdG8gZ3JvdyBhIHNwYXRpYWwgZmVhdHVyZSBtYXAgZnJvbSBhIDR4NCBzZWVkIHVwIHRvIHRoZSBmdWxsIG91dHB1dCByZXNvbHV0aW9uLiBCYXRjaCBub3JtYWxpemF0aW9uIGFuZCBSZUxVIGFjdGl2YXRpb25zIGFyZSBhcHBsaWVkIGFmdGVyIGVhY2ggbGF5ZXIsIHdpdGggYSBmaW5hbCBUYW5oIHRvIGJvdW5kIG91dHB1dCBwaXhlbCB2YWx1ZXMgdG8gWy0xLCAxXS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgRENHQU5HZW5lcmF0b3Iobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbno9MTAwLCBuZ2Y9NjQsIG5jPTMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKG56LCAgbmdmKjE2LCA0LCAxLCAwLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQobmdmKjE2KSwgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZChuZ2YqMTYsIG5nZio4LCA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQobmdmKjgpLCAgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZChuZ2YqOCwgIG5nZio0LCA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQobmdmKjQpLCAgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZChuZ2YqNCwgIG5nZioyLCA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQobmdmKjIpLCAgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZChuZ2YqMiwgIG5nZiwgICA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQobmdmKSwgICAgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZChuZ2YsICAgIG5jLCAgICA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgbm4uVGFuaCgpXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB6KTogcmV0dXJuIHNlbGYubmV0KHoudmlldyh6LnNpemUoMCksIC0xLCAxLCAxKSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBkaXNjcmltaW5hdG9yIG1pcnJvcnMgdGhpcyBzdHJ1Y3R1cmUgd2l0aCByZWd1bGFyIGNvbnZvbHV0aW9ucyBhbmQgTGVha3kgUmVMVSBhY3RpdmF0aW9ucywgcHJvZ3Jlc3NpdmVseSBoYWx2aW5nIHRoZSBzcGF0aWFsIGRpbWVuc2lvbnMuIEJhdGNoIG5vcm1hbGl6YXRpb24gaXMgb21pdHRlZCBpbiB0aGUgZmlyc3QgbGF5ZXIgb2YgRCwgYW5kIHNwZWN0cmFsIG5vcm1hbGl6YXRpb24gY2FuIHJlcGxhY2UgYmF0Y2ggbm9ybSB0byBlbmZvcmNlIGEgTGlwc2NoaXR6IGNvbnN0cmFpbnQgd2l0aG91dCBiYXRjaCBzdGF0aXN0aWNzLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IlRyYWluaW5nIExvb3AgYW5kIE1vZGUgQ29sbGFwc2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIEdBTiB0cmFpbmluZyBhbHRlcm5hdGVzOiB1cGRhdGUgRCBvbiBhIGJhdGNoIG9mIHJlYWwgYW5kIGZha2Ugc2FtcGxlcywgdGhlbiB1cGRhdGUgRyB1c2luZyB0aGUgdXBkYXRlZCBELiBUaGUgcmF0aW8gb2YgRCB0byBHIHVwZGF0ZXMgKG9mdGVuIDE6MSBvciA1OjEgZm9yIFdHQU4pIG1hdHRlcnMuIFdoZW4gRCBnZXRzIHRvbyBzdHJvbmcgdG9vIGZhc3QsIEcgcmVjZWl2ZXMgdmFuaXNoaW5nIGdyYWRpZW50cyBhbmQgc3RvcHMgbGVhcm5pbmcuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwiY29udGVudCI6Ik1vZGUgY29sbGFwc2UgaXMgdGhlIEdBTiBwYXRob2xvZ3kgd2hlcmUgdGhlIGdlbmVyYXRvciBtYXBzIGFsbCBub2lzZSB2ZWN0b3JzIHRvIGEgaGFuZGZ1bCBvZiBtb2Rlcy4gU3ltcHRvbXM6IGxvdyBzYW1wbGUgZGl2ZXJzaXR5LCBkaXNjcmltaW5hdG9yIGxvc3Mg4oaSIDAuIEZpeDogdXNlIFdHQU4tR1Agb3Igc3BlY3RyYWwgbm9ybWFsaXphdGlvbiBvbiBELiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5AdG9yY2gubm9fZ3JhZCgpXG5kZWYgZGV0ZWN0X21vZGVfY29sbGFwc2UoRywgel9kaW0sIG49NjQsIHRocmVzaG9sZD0wLjksIGRldmljZT1cdTAwMjdjdWRhXHUwMDI3KTpcbiAgICBHLmV2YWwoKVxuICAgIHogPSB0b3JjaC5yYW5kbihuLCB6X2RpbSwgZGV2aWNlPWRldmljZSlcbiAgICBzYW1wbGVzID0gRyh6KS5mbGF0dGVuKDEpICAgICAgICAgICAgICAgICAgICAgICAgICAjIChuLCBkKVxuICAgIG5vcm1zICAgPSBzYW1wbGVzIC8gKHNhbXBsZXMubm9ybShkaW09MSwga2VlcGRpbT1UcnVlKSArIDFlLTgpXG4gICAgc2ltX21hdCA9IG5vcm1zIEAgbm9ybXMuVCAgICAgICAgICAgICAgICAgICAgICAgICAgIyAobiwgbikgY29zaW5lIHNpbXNcbiAgICBtYXNrICAgID0gfnRvcmNoLmV5ZShuLCBkdHlwZT10b3JjaC5ib29sLCBkZXZpY2U9ZGV2aWNlKVxuICAgIG1lYW5fc2ltID0gc2ltX21hdFttYXNrXS5tZWFuKCkuaXRlbSgpXG4gICAgY29sbGFwc2VkID0gbWVhbl9zaW0gXHUwMDNlIHRocmVzaG9sZFxuICAgIHJldHVybiBjb2xsYXBzZWQsIG1lYW5fc2ltIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiUHJhY3RpY2FsIFN0YWJpbGl0eSBUcmlja3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldHQU4gcmVwbGFjZXMgdGhlIEJDRSBsb3NzIHdpdGggdGhlIFdhc3NlcnN0ZWluLTEgZGlzdGFuY2UsIHdoaWNoIHByb3ZpZGVzIHNtb290aGVyIGdyYWRpZW50cyBhbmQgYSBtZWFuaW5nZnVsIGxvc3MgbWV0cmljIGNvcnJlbGF0ZWQgd2l0aCBzYW1wbGUgcXVhbGl0eS4gVGhlIGRpc2NyaW1pbmF0b3IgKGNhbGxlZCBjcml0aWMgaW4gV0dBTikgaXMgbm8gbG9uZ2VyIGNvbnN0cmFpbmVkIHRvIFswLDFdOyBpbnN0ZWFkIGl0cyBvdXRwdXRzIGFyZSB1bmJvdW5kZWQgcmVhbCBzY29yZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiZGVmIHdnYW5fZ3BfcGVuYWx0eShELCByZWFsLCBmYWtlLCBsYW09MTAsIGRldmljZT1cdTAwMjdjdWRhXHUwMDI3KTpcbiAgICBCID0gcmVhbC5zaXplKDApXG4gICAgYWxwaGEgPSB0b3JjaC5yYW5kKEIsIDEsIDEsIDEsIGRldmljZT1kZXZpY2UpXG4gICAgaW50ZXJwID0gKGFscGhhICogcmVhbCArICgxIC0gYWxwaGEpICogZmFrZSkucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICBkX2ludGVycCA9IEQoaW50ZXJwKVxuICAgIGdyYWRzID0gdG9yY2guYXV0b2dyYWQuZ3JhZChcbiAgICAgICAgb3V0cHV0cz1kX2ludGVycCwgaW5wdXRzPWludGVycCxcbiAgICAgICAgZ3JhZF9vdXRwdXRzPXRvcmNoLm9uZXNfbGlrZShkX2ludGVycCksXG4gICAgICAgIGNyZWF0ZV9ncmFwaD1UcnVlLCByZXRhaW5fZ3JhcGg9VHJ1ZVxuICAgIClbMF1cbiAgICBncmFkX25vcm0gPSBncmFkcy5mbGF0dGVuKDEpLm5vcm0oMiwgZGltPTEpXG4gICAgcGVuYWx0eSA9IGxhbSAqICgoZ3JhZF9ub3JtIC0gMSkgKiogMikubWVhbigpXG4gICAgcmV0dXJuIHBlbmFsdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFkZGl0aW9uYWwgc3RhYmlsaXR5IHRyaWNrcyBpbmNsdWRlOiB0d28tdGltZXNjYWxlIHVwZGF0ZSBydWxlcyAoVFRVUikgd2l0aCBkaWZmZXJlbnQgbGVhcm5pbmcgcmF0ZXMgZm9yIEcgYW5kIEQ7IGxhYmVsIHNtb290aGluZyBmb3IgdGhlIGRpc2NyaW1pbmF0b3IgdGFyZ2V0czsgYWRkaW5nIEdhdXNzaWFuIG5vaXNlIHRvIHJlYWwgaW1hZ2VzOyBzcGVjdHJhbCBub3JtYWxpemF0aW9uIG9mIEQgd2VpZ2h0czsgYW5kIGV4cG9uZW50aWFsIG1vdmluZyBhdmVyYWdlIG9mIEcgd2VpZ2h0cyBmb3IgaW5mZXJlbmNlLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJHQU4gVmFyaWFudCIsIkxvc3MiLCJHcmFkaWVudCBQZW5hbHR5IiwiVHJhaW5pbmcgU3RhYmlsaXR5IiwiU2FtcGxlIFF1YWxpdHkiLCJNb2RlIENvbGxhcHNlIFJpc2siXSwicm93cyI6W1siVmFuaWxsYSBHQU4iLCJCQ0UiLCJObyIsIkxvdyIsIkxvdyIsIkhpZ2giXSxbIkRDR0FOIiwiQkNFIiwiTm8iLCJNZWRpdW0iLCJNZWRpdW0iLCJNZWRpdW0iXSxbIldHQU4iLCJXYXNzZXJzdGVpbiIsIldlaWdodCBjbGlwcGluZyIsIk1lZGl1bS1IaWdoIiwiTWVkaXVtLUhpZ2giLCJMb3ctTWVkaXVtIl0sWyJXR0FOLUdQIiwiV2Fzc2Vyc3RlaW4iLCJHUCAoaW50ZXJwb2xhdGVkKSIsIkhpZ2giLCJIaWdoIiwiTG93Il0sWyJTTkdBTiIsIkhpbmdlIiwiU3BlY3RyYWwgTm9ybSIsIkhpZ2giLCJIaWdoIiwiTG93Il1dfSx7InR5cGUiOiJoMiIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbWluaW1heCBvYmplY3RpdmUgY3JlYXRlcyBhIGRlbGljYXRlIHNhZGRsZS1wb2ludCBvcHRpbWl6YXRpb24uIFZhbmlsbGEgR0FOcyBzdWZmZXIgZnJvbSB2YW5pc2hpbmcgZ3JhZGllbnRzIGFuZCBtb2RlIGNvbGxhcHNlLiBXR0FOLUdQIGFuZCBzcGVjdHJhbCBub3JtYWxpemF0aW9uIGFyZSB0aGUgbW9zdCByZWxpYWJsZSBmaXhlcyBmb3IgbW9kZXJuIEdBTiB0cmFpbmluZyBwaXBlbGluZXMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEQ0dBTlx1MDAyN3MgYXJjaGl0ZWN0dXJhbCBndWlkZWxpbmVzIChzdHJpZGVkIGNvbnZvbHV0aW9ucywgYmF0Y2ggbm9ybSwgTGVha3lSZUxVIGluIEQsIFJlTFUgaW4gRywgVGFuaCBvdXRwdXQpIHJlbWFpbiBzb3VuZCBzdGFydGluZyBwb2ludHMuIFdoZW4gYnVpbGRpbmcgYSBjdXN0b20gR0FOLCBzdGFydCB3aXRoIFdHQU4tR1AgbG9zcywgc3BlY3RyYWwgbm9ybSBvbiBELCBhbmQgZ3JhZGllbnQgY2xpcHBpbmcgb24gRyB0byBtaW5pbWl6ZSBpbnN0YWJpbGl0eS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vbml0b3IgYm90aCBEIGFuZCBHIGxvc3NlcyB0b2dldGhlcjogaWYgRF9sb3NzIOKGkiAwIGFuZCBHX2xvc3Mgc3Bpa2VzLCBtb2RlIGNvbGxhcHNlIG9yIHRyYWluaW5nIGluc3RhYmlsaXR5IGlzIG9jY3VycmluZy4gVXNlIHRoZSBwYWlyd2lzZSBjb3NpbmUgc2ltaWxhcml0eSBkaWFnbm9zdGljIG9uIGdlbmVyYXRlZCBzYW1wbGVzIGFzIGEgcXVpY2sgcXVhbnRpdGF0aXZlIGNoZWNrIGZvciBkaXZlcnNpdHkgY29sbGFwc2UgZHVyaW5nIHRyYWluaW5nIHJ1bnMuIn1d"
---
# GAN Training Fundamentals: Minimax Objective and Stability

Generative Adversarial Networks pit two neural networks against each other: a generator that synthesizes fake samples and a discriminator that tries to tell real from fake. The interplay between them drives both networks to improve, ultimately producing a generator capable of creating highly realistic images indistinguishable from real data.

GANs have become a cornerstone of generative vision research, enabling tasks like image synthesis, style transfer, super-resolution, and data augmentation. Understanding the minimax objective and training dynamics is essential before working with any GAN variant in practice.

The GAN objective is a minimax game: the discriminator D maximizes its ability to distinguish real from fake, while the generator G minimizes the discriminator's success. Formally, min_G max_D E[log D(x)] + E[log(1 - D(G(z)))], where x is real data and z is random noise.

```
import torch
import torch.nn.functional as F

def gan_losses(D, G, real, z):
    ones  = torch.ones(real.size(0), 1, device=real.device)
    zeros = torch.zeros(real.size(0), 1, device=real.device)
    fake  = G(z).detach()
    D_loss = F.binary_cross_entropy(D(real), ones) \
           + F.binary_cross_entropy(D(fake), zeros)
    G_loss = F.binary_cross_entropy(D(G(z)), ones)
    return D_loss, G_loss
```

The Nash equilibrium of this game is reached when the generator perfectly replicates the real distribution and the discriminator outputs 0.5 everywhere. In practice, training rarely reaches this ideal equilibrium and oscillates or diverges, which motivates the many stability improvements developed over the years.

In DCGAN, the generator uses a series of transposed convolutions (strided upsampling) to grow a spatial feature map from a 4x4 seed up to the full output resolution. Batch normalization and ReLU activations are applied after each layer, with a final Tanh to bound output pixel values to [-1, 1].

```
import torch.nn as nn

class DCGANGenerator(nn.Module):
    def __init__(self, nz=100, ngf=64, nc=3):
        super().__init__()
        self.net = nn.Sequential(
            nn.ConvTranspose2d(nz,  ngf*16, 4, 1, 0, bias=False), nn.BatchNorm2d(ngf*16), nn.ReLU(True),
            nn.ConvTranspose2d(ngf*16, ngf*8, 4, 2, 1, bias=False), nn.BatchNorm2d(ngf*8),  nn.ReLU(True),
            nn.ConvTranspose2d(ngf*8,  ngf*4, 4, 2, 1, bias=False), nn.BatchNorm2d(ngf*4),  nn.ReLU(True),
            nn.ConvTranspose2d(ngf*4,  ngf*2, 4, 2, 1, bias=False), nn.BatchNorm2d(ngf*2),  nn.ReLU(True),
            nn.ConvTranspose2d(ngf*2,  ngf,   4, 2, 1, bias=False), nn.BatchNorm2d(ngf),    nn.ReLU(True),
            nn.ConvTranspose2d(ngf,    nc,    4, 2, 1, bias=False), nn.Tanh()
        )
    def forward(self, z): return self.net(z.view(z.size(0), -1, 1, 1))
```

The discriminator mirrors this structure with regular convolutions and Leaky ReLU activations, progressively halving the spatial dimensions. Batch normalization is omitted in the first layer of D, and spectral normalization can replace batch norm to enforce a Lipschitz constraint without batch statistics.

Standard GAN training alternates: update D on a batch of real and fake samples, then update G using the updated D. The ratio of D to G updates (often 1:1 or 5:1 for WGAN) matters. When D gets too strong too fast, G receives vanishing gradients and stops learning.

> **warning**: Mode collapse is the GAN pathology where the generator maps all noise vectors to a handful of modes. Symptoms: low sample diversity, discriminator loss → 0. Fix: use WGAN-GP or spectral normalization on D.

```
import torch
import torch.nn.functional as F

@torch.no_grad()
def detect_mode_collapse(G, z_dim, n=64, threshold=0.9, device='cuda'):
    G.eval()
    z = torch.randn(n, z_dim, device=device)
    samples = G(z).flatten(1)                          # (n, d)
    norms   = samples / (samples.norm(dim=1, keepdim=True) + 1e-8)
    sim_mat = norms @ norms.T                          # (n, n) cosine sims
    mask    = ~torch.eye(n, dtype=torch.bool, device=device)
    mean_sim = sim_mat[mask].mean().item()
    collapsed = mean_sim > threshold
    return collapsed, mean_sim
```

WGAN replaces the BCE loss with the Wasserstein-1 distance, which provides smoother gradients and a meaningful loss metric correlated with sample quality. The discriminator (called critic in WGAN) is no longer constrained to [0,1]; instead its outputs are unbounded real scores.

```
def wgan_gp_penalty(D, real, fake, lam=10, device='cuda'):
    B = real.size(0)
    alpha = torch.rand(B, 1, 1, 1, device=device)
    interp = (alpha * real + (1 - alpha) * fake).requires_grad_(True)
    d_interp = D(interp)
    grads = torch.autograd.grad(
        outputs=d_interp, inputs=interp,
        grad_outputs=torch.ones_like(d_interp),
        create_graph=True, retain_graph=True
    )[0]
    grad_norm = grads.flatten(1).norm(2, dim=1)
    penalty = lam * ((grad_norm - 1) ** 2).mean()
    return penalty
```

Additional stability tricks include: two-timescale update rules (TTUR) with different learning rates for G and D; label smoothing for the discriminator targets; adding Gaussian noise to real images; spectral normalization of D weights; and exponential moving average of G weights for inference.

| GAN Variant | Loss | Gradient Penalty | Training Stability | Sample Quality | Mode Collapse Risk |
| --- | --- | --- | --- | --- | --- |
| Vanilla GAN | BCE | No | Low | Low | High |
| DCGAN | BCE | No | Medium | Medium | Medium |
| WGAN | Wasserstein | Weight clipping | Medium-High | Medium-High | Low-Medium |
| WGAN-GP | Wasserstein | GP (interpolated) | High | High | Low |
| SNGAN | Hinge | Spectral Norm | High | High | Low |

The minimax objective creates a delicate saddle-point optimization. Vanilla GANs suffer from vanishing gradients and mode collapse. WGAN-GP and spectral normalization are the most reliable fixes for modern GAN training pipelines.

DCGAN's architectural guidelines (strided convolutions, batch norm, LeakyReLU in D, ReLU in G, Tanh output) remain sound starting points. When building a custom GAN, start with WGAN-GP loss, spectral norm on D, and gradient clipping on G to minimize instability.

Monitor both D and G losses together: if D_loss → 0 and G_loss spikes, mode collapse or training instability is occurring. Use the pairwise cosine similarity diagnostic on generated samples as a quick quantitative check for diversity collapse during training runs.

