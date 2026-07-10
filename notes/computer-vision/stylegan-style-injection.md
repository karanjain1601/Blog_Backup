---
title: "StyleGAN: Disentangled Style Injection and AdaIN"
slug: "stylegan-style-injection"
description: ""
tags: ["stylegan", "generative-models", "adain", "disentanglement", "computer-vision"]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImgyIiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdHlsZUdBTiwgaW50cm9kdWNlZCBieSBLYXJyYXMgZXQgYWwuIGF0IE5WSURJQSwgcmVzdHJ1Y3R1cmVzIHRoZSB0cmFkaXRpb25hbCBHQU4gZ2VuZXJhdG9yIGJ5IHNlcGFyYXRpbmcgc3R5bGUgZnJvbSBjb250ZW50LiBSYXRoZXIgdGhhbiBmZWVkaW5nIG5vaXNlIHogZGlyZWN0bHkgdG8gdGhlIGdlbmVyYXRvciwgaXQgZmlyc3QgbWFwcyB6IHRocm91Z2ggYSBsZWFybmVkIG1hcHBpbmcgbmV0d29yayB0byBhbiBpbnRlcm1lZGlhdGUgbGF0ZW50IHcsIHdoaWNoIHRoZW4gaW5qZWN0cyBzdHlsZSBhdCBlYWNoIHJlc29sdXRpb24gbGV2ZWwgdmlhIEFkYXB0aXZlIEluc3RhbmNlIE5vcm1hbGl6YXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGlzIGFyY2hpdGVjdHVyZSB5aWVsZHMgYSBoaWdobHkgZGlzZW50YW5nbGVkIGxhdGVudCBzcGFjZSB3aGVyZSBkaWZmZXJlbnQgc3R5bGUgc2NhbGVz4oCUY29hcnNlIChwb3NlLCBmYWNlIHNoYXBlKSwgbWVkaXVtIChmYWNpYWwgZmVhdHVyZXMpLCBhbmQgZmluZSAoY29sb3IsIHRleHR1cmUp4oCUYXJlIGNvbnRyb2xsZWQgaW5kZXBlbmRlbnRseS4gU3R5bGVHQU4gc2V0IGEgbmV3IEZJRCByZWNvcmQgb24gRkZIUS0xMDI0IGFuZCByZW1haW5zIGZvdW5kYXRpb25hbCBmb3IgY29udHJvbGxhYmxlIGltYWdlIGdlbmVyYXRpb24gcmVzZWFyY2guIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiTWFwcGluZyBOZXR3b3JrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbWFwcGluZyBuZXR3b3JrIGlzIGFuIDgtbGF5ZXIgTUxQIHRoYXQgdHJhbnNmb3JtcyB0aGUgaW5pdGlhbCBub2lzZSB6IOKIiCBSXjUxMiBpbnRvIGFuIGludGVybWVkaWF0ZSBsYXRlbnQgdyDiiIggUl41MTIuIEVhY2ggbGF5ZXIgYXBwbGllcyBhIGxpbmVhciB0cmFuc2Zvcm1hdGlvbiBmb2xsb3dlZCBieSBhIExlYWt5UmVMVS4gVGhlIG5ldHdvcmsgbGVhcm5zIHRvIFx1MDAyN3VuZW50YW5nbGVcdTAwMjcgdGhlIGxhdGVudCBmYWN0b3JzIHNvIHRoYXQgdy1zcGFjZSBoYXMgYmV0dGVyIGRpc2VudGFuZ2xlbWVudCBwcm9wZXJ0aWVzIHRoYW4gei1zcGFjZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgTWFwcGluZ05ldHdvcmsobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgel9kaW09NTEyLCB3X2RpbT01MTIsIG5fbGF5ZXJzPTgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgbGF5ZXJzID0gW11cbiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uobl9sYXllcnMpOlxuICAgICAgICAgICAgaW5fZCAgPSB6X2RpbSBpZiBpID09IDAgZWxzZSB3X2RpbVxuICAgICAgICAgICAgbGF5ZXJzICs9IFtubi5MaW5lYXIoaW5fZCwgd19kaW0pLCBubi5MZWFreVJlTFUoMC4yKV1cbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKCpsYXllcnMpXG4gICAgICAgIHNlbGYubl9zdHlsZV9ibG9ja3MgPSAxOCAgICMgbG9nMigxMDI0KSAqIDJcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB6KTpcbiAgICAgICAgdyA9IHNlbGYubmV0KHopICAgICAgICAgICAgIyAoQiwgd19kaW0pXG4gICAgICAgIHJldHVybiB3LnVuc3F1ZWV6ZSgxKS5yZXBlYXQoMSwgc2VsZi5uX3N0eWxlX2Jsb2NrcywgMSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB3IHZlY3RvciBpcyByZXBlYXRlZCAob3IgYnJvYWRjYXN0KSB0byBwcm9kdWNlIG9uZSBzdHlsZSB2ZWN0b3IgcGVyIHN5bnRoZXNpcyBibG9jay4gSW4gU3R5bGVHQU4yLCBtaXhpbmcgcmVndWxhcml6YXRpb24gaXMgYXBwbGllZDogZHVyaW5nIHRyYWluaW5nLCB0d28gZGlmZmVyZW50IHcgdmVjdG9ycyBhcmUgc29tZXRpbWVzIHVzZWTigJRvbmUgZm9yIGNvYXJzZSBsYXllcnMgYW5kIG9uZSBmb3IgZmluZSBsYXllcnPigJRlbmNvdXJhZ2luZyB0aGUgbmV0d29yayB0byBrZWVwIHN0eWxlIHNjYWxlcyBzZXBhcmF0ZS4ifSx7InR5cGUiOiJoMiIsImNvbnRlbnQiOiJBZGFJTiBTdHlsZSBJbmplY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFkYXB0aXZlIEluc3RhbmNlIE5vcm1hbGl6YXRpb24gKEFkYUlOKSBpcyB0aGUgbWVjaGFuaXNtIGJ5IHdoaWNoIHN0eWxlIHcgY29udHJvbHMgZWFjaCBzeW50aGVzaXMgbGF5ZXIuIFRoZSBmZWF0dXJlIG1hcCBpcyBmaXJzdCBub3JtYWxpemVkIHRvIHplcm8gbWVhbiBhbmQgdW5pdCB2YXJpYW5jZSBwZXIgY2hhbm5lbCwgdGhlbiByZXNjYWxlZCBhbmQgc2hpZnRlZCBieSBsZWFybmVkIGFmZmluZSBwYXJhbWV0ZXJzIGRlcml2ZWQgZnJvbSB3LiBUaGlzIGFsbG93cyB3IHRvIHNldCB0aGUgXHUwMDI3c3R5bGVcdTAwMjcgb2YgZWFjaCBsYXllciBpbmRlcGVuZGVudGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIEFkYUlOKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHdfZGltLCBjaGFubmVscyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnN0eWxlX2xpbmVhciA9IG5uLkxpbmVhcih3X2RpbSwgY2hhbm5lbHMgKiAyKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIHcpOlxuICAgICAgICAjIHg6IChCLCBDLCBILCBXKSAgdzogKEIsIHdfZGltKVxuICAgICAgICB5ICA9IHNlbGYuc3R5bGVfbGluZWFyKHcpICAgICAgICAgICMgKEIsIDJDKVxuICAgICAgICB5X3MsIHlfYiA9IHkuY2h1bmsoMiwgZGltPTEpICAgICAgIyBlYWNoIChCLCBDKVxuICAgICAgICB5X3MgPSB5X3MudW5zcXVlZXplKC0xKS51bnNxdWVlemUoLTEpXG4gICAgICAgIHlfYiA9IHlfYi51bnNxdWVlemUoLTEpLnVuc3F1ZWV6ZSgtMSlcbiAgICAgICAgbWVhbiA9IHgubWVhbihkaW09WzIsIDNdLCBrZWVwZGltPVRydWUpXG4gICAgICAgIHN0ZCAgPSB4LnN0ZChkaW09WzIsIDNdLCBrZWVwZGltPVRydWUpICsgMWUtOFxuICAgICAgICB4X25vcm0gPSAoeCAtIG1lYW4pIC8gc3RkXG4gICAgICAgIHJldHVybiB5X3MgKiB4X25vcm0gKyB5X2IifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJlY2F1c2UgQWRhSU4gbm9ybWFsaXplcyB0aGUgY29udGVudCBvZiBlYWNoIGZlYXR1cmUgbWFwIGJlZm9yZSBhcHBseWluZyBzdHlsZSwgdGhlIGdlbmVyYXRvclx1MDAyN3MgbGVhcm5lZCBjb25zdGFudCAoYSBmaXhlZCA0eDQgbGVhcm5lZCB0ZW5zb3IpIGNhcnJpZXMgc3BhdGlhbCBzdHJ1Y3R1cmUgd2hpbGUgdyBjYXJyaWVzIG9ubHkgc3R5bGUgaW5mb3JtYXRpb24uIFRoaXMgY2xlYW4gc2VwYXJhdGlvbiBpcyB3aGF0IGdpdmVzIFN0eWxlR0FOIGl0cyBzdXBlcmlvciBkaXNlbnRhbmdsZW1lbnQgY29tcGFyZWQgdG8gZWFybGllciBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IlN0b2NoYXN0aWMgTm9pc2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0eWxlR0FOIGFkZHMgcGVyLXBpeGVsIHN0b2NoYXN0aWMgbm9pc2UgdG8gZWFjaCBzeW50aGVzaXMgbGF5ZXIsIGRpc3RpbmN0IGZyb20gdGhlIGxhdGVudCB6LiBUaGlzIG5vaXNlIGNhcHR1cmVzIGZpbmUtZ3JhaW5lZCBzdG9jaGFzdGljIHZhcmlhdGlvbuKAlGhhaXIgc3RyYW5kIHBsYWNlbWVudCwgc2tpbiBwb3JlIGRldGFpbCwgYmFja2dyb3VuZCB0ZXh0dXJl4oCUdGhhdCBkb2VzIG5vdCBuZWVkIHRvIGJlIGdsb2JhbGx5IGNvbnNpc3RlbnQuIFRoZSBub2lzZSBpcyBzY2FsZWQgYnkgYSBsZWFybmVkIHBlci1jaGFubmVsIHNjYWxhciBiZWZvcmUgYmVpbmcgYWRkZWQgdG8gdGhlIGZlYXR1cmUgbWFwLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE5vaXNlSW5qZWN0aW9uKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNoYW5uZWxzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYud2VpZ2h0ID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKDEsIGNoYW5uZWxzLCAxLCAxKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBub2lzZT1Ob25lKTpcbiAgICAgICAgaWYgbm9pc2UgaXMgTm9uZTpcbiAgICAgICAgICAgIEIsIEMsIEgsIFcgPSB4LnNoYXBlXG4gICAgICAgICAgICBub2lzZSA9IHRvcmNoLnJhbmRuKEIsIDEsIEgsIFcsIGRldmljZT14LmRldmljZSlcbiAgICAgICAgcmV0dXJuIHggKyBzZWxmLndlaWdodCAqIG5vaXNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUbyBnZW5lcmF0ZSBhIG5ldyBzdG9jaGFzdGljIHZhcmlhbnQgb2YgdGhlIHNhbWUgZmFjZSAoc2FtZSBpZGVudGl0eSwgc2FtZSBwb3NlLCBkaWZmZXJlbnQgaGFpciB3aXNwcyksIGhvbGQgdyBjb25zdGFudCBidXQgcmVzYW1wbGUgdGhlIG5vaXNlIHRlbnNvcnMgaW5qZWN0ZWQgYXQgZWFjaCBsYXllci4gVGhpcyBzZXBhcmF0ZXMgaGlnaC1sZXZlbCBzZW1hbnRpYyBjb250cm9sICh3KSBmcm9tIGxvdy1sZXZlbCBzdG9jaGFzdGljIHRleHR1cmUgKG5vaXNlKSwgYSBkZXNpZ24gdGhhdCBzdHJvbmdseSBpbmZsdWVuY2VkIHN1YnNlcXVlbnQgYXJjaGl0ZWN0dXJlcy4ifSx7InR5cGUiOiJoMiIsImNvbnRlbnQiOiJQcm9ncmVzc2l2ZSBHcm93aW5nIHZzIE1TRyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3R5bGVHQU4gdjEgdXNlZCBwcm9ncmVzc2l2ZSBncm93aW5nIChQcm9HQU4pOiB0cmFpbmluZyBzdGFydHMgYXQgNHg0IGFuZCBuZXcgbGF5ZXJzIGFyZSBmYWRlZCBpbiBhcyByZXNvbHV0aW9uIGRvdWJsZXMuIFdoaWxlIGVmZmVjdGl2ZSwgdGhpcyBjYXVzZWQgdGV4dHVyZS1zdHJ1Y3R1cmUgYXJ0aWZhY3RzLiBTdHlsZUdBTjIgcmVwbGFjZWQgcHJvZ3Jlc3NpdmUgZ3Jvd2luZyB3aXRoIG11bHRpLXNjYWxlIGdyYWRpZW50cyAoTVNHKSBhbmQgcGF0aC1sZW5ndGggcmVndWxhcml6YXRpb24sIGFjaGlldmluZyBiZXR0ZXIgZ2xvYmFsIGNvbnNpc3RlbmN5IGFuZCBzaWduaWZpY2FudGx5IGxvd2VyIEZJRC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIHRydW5jYXRpb25fdHJpY2sodywgd19iYXIsIHBzaT0wLjcpOlxuICAgIFwiXCJcIkFwcGx5IHRydW5jYXRpb24gdG8gdyB2ZWN0b3JzIGZvciBxdWFsaXR5L2RpdmVyc2l0eSB0cmFkZW9mZi5cbiAgICB3ICAgIDogKEIsIG5fYmxvY2tzLCB3X2RpbSkg4oCUIHNhbXBsZWQgaW50ZXJtZWRpYXRlIGxhdGVudHNcbiAgICB3X2JhcjogKDEsIG5fYmxvY2tzLCB3X2RpbSkg4oCUIEVNQSBvZiB3IG92ZXIgdHJhaW5pbmcgKG1lYW4gZmFjZSlcbiAgICBwc2kgIDogdHJ1bmNhdGlvbiBzdHJlbmd0aCBpbiBbMC41LCAwLjldOyBsb3dlciA9IGhpZ2hlciBxdWFsaXR5XG4gICAgXCJcIlwiXG4gICAgcmV0dXJuIHdfYmFyICsgcHNpICogKHcgLSB3X2JhcilcblxuIyBVcGRhdGUgd19iYXIgZHVyaW5nIHRyYWluaW5nIHdpdGggRU1BXG4jIHdfYmFyID0gMC45OTUgKiB3X2JhciArIDAuMDA1ICogdy5tZWFuKDAsIGtlZXBkaW09VHJ1ZSkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmVyc2lvbiIsIk1heCBSZXNvbHV0aW9uIiwiRklEIChGRkhRKSIsIktleSBJbm5vdmF0aW9uIl0sInJvd3MiOltbIlN0eWxlR0FOIHYxIiwiMTAyNHgxMDI0IiwiNC40MCIsIk1hcHBpbmcgbmV0d29yayArIEFkYUlOICsgc3RvY2hhc3RpYyBub2lzZSJdLFsiU3R5bGVHQU4yIiwiMTAyNHgxMDI0IiwiMi44NCIsIldlaWdodCBkZW1vZHVsYXRpb24sIG5vIHByb2cuIGdyb3dpbmcsIHBhdGgtbGVuZ3RoIHJlZyJdLFsiU3R5bGVHQU4zIiwiMTAyNHgxMDI0IiwiMi43OSIsIkFsaWFzLWZyZWUgc3ludGhlc2lzLCBlcXVpdmFyaWFudCB0byB0cmFuc2xhdGlvbi9yb3RhdGlvbiJdLFsiU3R5bGVHQU4tWEwiLCIxMDI0eDEwMjQiLCIyLjMwIiwiQ2xhc3MtY29uZGl0aW9uYWwsIHByb2plY3RlZCBkaXNjcmltaW5hdG9yLCBtdWx0aS1zY2FsZSJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwiY29udGVudCI6IlRoZSB3LXNwYWNlIChpbnRlcm1lZGlhdGUgbGF0ZW50KSBpcyBtb3JlIGRpc2VudGFuZ2xlZCB0aGFuIHotc3BhY2UgYmVjYXVzZSB0aGUgbWFwcGluZyBuZXR3b3JrIGxlYXJucyB0byBzcHJlYWQgc3R5bGVzLiBFZGl0aW5nIGluIHctc3BhY2UgKGUuZy4gYWdlLCBleHByZXNzaW9uKSBwcm9kdWNlcyBjbGVhbmVyIHNlbWFudGljIGNoYW5nZXMgdGhhbiBlZGl0aW5nIHogZGlyZWN0bHkuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3R5bGVHQU5cdTAwMjdzIG1hcHBpbmcgbmV0d29yayArIEFkYUlOIGRlc2lnbiBjbGVhbmx5IHNlcGFyYXRlcyBpZGVudGl0eSAodykgZnJvbSBzdG9jaGFzdGljIHRleHR1cmUgKG5vaXNlKSwgZW5hYmxpbmcgcHJlY2lzZSBzZW1hbnRpYyBlZGl0aW5nIGluIHctc3BhY2UuIFRoaXMgaGFzIG1hZGUgU3R5bGVHQU4gdGhlIGRlZmF1bHQgYmFja2JvbmUgZm9yIEdBTi1iYXNlZCBmYWNlIGVkaXRpbmcsIGludmVyc2lvbiwgYW5kIGludGVycG9sYXRpb24gcmVzZWFyY2guIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdHlsZUdBTjIgaXMgdGhlIHByYWN0aWNhbCB3b3JraG9yc2U6IHdlaWdodCBkZW1vZHVsYXRpb24gZml4ZXMgd2F0ZXItZHJvcGxldCBhcnRpZmFjdHMgZnJvbSBBZGFJTiwgYW5kIHJlbW92aW5nIHByb2dyZXNzaXZlIGdyb3dpbmcgc2ltcGxpZmllcyB0cmFpbmluZy4gU3R5bGVHQU4zIGZ1cnRoZXIgZWxpbWluYXRlcyB0ZXh0dXJlIHN0aWNraW5nIGJ5IGVuc3VyaW5nIHRoZSBzeW50aGVzaXMgbmV0d29yayBpcyBlcXVpdmFyaWFudCB0byBzdWJwaXhlbCB0cmFuc2xhdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBwcm9kdWN0aW9uIHVzZSwgcHJlZmVyIFN0eWxlR0FOMi1BREEgKGFkYXB0aXZlIGRpc2NyaW1pbmF0b3IgYXVnbWVudGF0aW9uKSwgd2hpY2ggYWNoaWV2ZXMgc3Ryb25nIHBlcmZvcm1hbmNlIHdpdGggYXMgZmV3IGFzIDEsMDAwIHRyYWluaW5nIGltYWdlcyBieSBhdWdtZW50aW5nIGRpc2NyaW1pbmF0b3IgaW5wdXRzIGluIGEgd2F5IHRoYXQgZG9lcyBub3QgbGVhayBhdWdtZW50YXRpb24gaW50byBnZW5lcmF0ZWQgc2FtcGxlcy4ifV0="
---
# StyleGAN: Disentangled Style Injection and AdaIN

StyleGAN, introduced by Karras et al. at NVIDIA, restructures the traditional GAN generator by separating style from content. Rather than feeding noise z directly to the generator, it first maps z through a learned mapping network to an intermediate latent w, which then injects style at each resolution level via Adaptive Instance Normalization.

This architecture yields a highly disentangled latent space where different style scales—coarse (pose, face shape), medium (facial features), and fine (color, texture)—are controlled independently. StyleGAN set a new FID record on FFHQ-1024 and remains foundational for controllable image generation research.

The mapping network is an 8-layer MLP that transforms the initial noise z ∈ R^512 into an intermediate latent w ∈ R^512. Each layer applies a linear transformation followed by a LeakyReLU. The network learns to 'unentangle' the latent factors so that w-space has better disentanglement properties than z-space.

```
import torch.nn as nn

class MappingNetwork(nn.Module):
    def __init__(self, z_dim=512, w_dim=512, n_layers=8):
        super().__init__()
        layers = []
        for i in range(n_layers):
            in_d  = z_dim if i == 0 else w_dim
            layers += [nn.Linear(in_d, w_dim), nn.LeakyReLU(0.2)]
        self.net = nn.Sequential(*layers)
        self.n_style_blocks = 18   # log2(1024) * 2
    def forward(self, z):
        w = self.net(z)            # (B, w_dim)
        return w.unsqueeze(1).repeat(1, self.n_style_blocks, 1)
```

The w vector is repeated (or broadcast) to produce one style vector per synthesis block. In StyleGAN2, mixing regularization is applied: during training, two different w vectors are sometimes used—one for coarse layers and one for fine layers—encouraging the network to keep style scales separate.

Adaptive Instance Normalization (AdaIN) is the mechanism by which style w controls each synthesis layer. The feature map is first normalized to zero mean and unit variance per channel, then rescaled and shifted by learned affine parameters derived from w. This allows w to set the 'style' of each layer independently.

```
import torch
import torch.nn as nn

class AdaIN(nn.Module):
    def __init__(self, w_dim, channels):
        super().__init__()
        self.style_linear = nn.Linear(w_dim, channels * 2)
    def forward(self, x, w):
        # x: (B, C, H, W)  w: (B, w_dim)
        y  = self.style_linear(w)          # (B, 2C)
        y_s, y_b = y.chunk(2, dim=1)      # each (B, C)
        y_s = y_s.unsqueeze(-1).unsqueeze(-1)
        y_b = y_b.unsqueeze(-1).unsqueeze(-1)
        mean = x.mean(dim=[2, 3], keepdim=True)
        std  = x.std(dim=[2, 3], keepdim=True) + 1e-8
        x_norm = (x - mean) / std
        return y_s * x_norm + y_b
```

Because AdaIN normalizes the content of each feature map before applying style, the generator's learned constant (a fixed 4x4 learned tensor) carries spatial structure while w carries only style information. This clean separation is what gives StyleGAN its superior disentanglement compared to earlier architectures.

StyleGAN adds per-pixel stochastic noise to each synthesis layer, distinct from the latent z. This noise captures fine-grained stochastic variation—hair strand placement, skin pore detail, background texture—that does not need to be globally consistent. The noise is scaled by a learned per-channel scalar before being added to the feature map.

```
import torch
import torch.nn as nn

class NoiseInjection(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.weight = nn.Parameter(torch.zeros(1, channels, 1, 1))
    def forward(self, x, noise=None):
        if noise is None:
            B, C, H, W = x.shape
            noise = torch.randn(B, 1, H, W, device=x.device)
        return x + self.weight * noise
```

To generate a new stochastic variant of the same face (same identity, same pose, different hair wisps), hold w constant but resample the noise tensors injected at each layer. This separates high-level semantic control (w) from low-level stochastic texture (noise), a design that strongly influenced subsequent architectures.

StyleGAN v1 used progressive growing (ProGAN): training starts at 4x4 and new layers are faded in as resolution doubles. While effective, this caused texture-structure artifacts. StyleGAN2 replaced progressive growing with multi-scale gradients (MSG) and path-length regularization, achieving better global consistency and significantly lower FID.

```
import torch

def truncation_trick(w, w_bar, psi=0.7):
    """Apply truncation to w vectors for quality/diversity tradeoff.
    w    : (B, n_blocks, w_dim) — sampled intermediate latents
    w_bar: (1, n_blocks, w_dim) — EMA of w over training (mean face)
    psi  : truncation strength in [0.5, 0.9]; lower = higher quality
    """
    return w_bar + psi * (w - w_bar)

# Update w_bar during training with EMA
# w_bar = 0.995 * w_bar + 0.005 * w.mean(0, keepdim=True)
```

| Version | Max Resolution | FID (FFHQ) | Key Innovation |
| --- | --- | --- | --- |
| StyleGAN v1 | 1024x1024 | 4.40 | Mapping network + AdaIN + stochastic noise |
| StyleGAN2 | 1024x1024 | 2.84 | Weight demodulation, no prog. growing, path-length reg |
| StyleGAN3 | 1024x1024 | 2.79 | Alias-free synthesis, equivariant to translation/rotation |
| StyleGAN-XL | 1024x1024 | 2.30 | Class-conditional, projected discriminator, multi-scale |

> **info**: The w-space (intermediate latent) is more disentangled than z-space because the mapping network learns to spread styles. Editing in w-space (e.g. age, expression) produces cleaner semantic changes than editing z directly.

StyleGAN's mapping network + AdaIN design cleanly separates identity (w) from stochastic texture (noise), enabling precise semantic editing in w-space. This has made StyleGAN the default backbone for GAN-based face editing, inversion, and interpolation research.

StyleGAN2 is the practical workhorse: weight demodulation fixes water-droplet artifacts from AdaIN, and removing progressive growing simplifies training. StyleGAN3 further eliminates texture sticking by ensuring the synthesis network is equivariant to subpixel translation.

For production use, prefer StyleGAN2-ADA (adaptive discriminator augmentation), which achieves strong performance with as few as 1,000 training images by augmenting discriminator inputs in a way that does not leak augmentation into generated samples.

