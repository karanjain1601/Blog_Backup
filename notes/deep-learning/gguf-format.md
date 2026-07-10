---
title: "GGUF Format and llama.cpp Quantization"
slug: "gguf-format"
description: "The GGUF file format for portable LLM quantization and the quantization types Q2_K through Q8_0 used by llama.cpp for CPU and GPU inference."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR0dVRiAoR1BULUdlbmVyYXRlZCBVbmlmaWVkIEZvcm1hdCkgaXMgdGhlIGJpbmFyeSBmaWxlIGZvcm1hdCB1c2VkIGJ5IGxsYW1hLmNwcCB0byBzdG9yZSBxdWFudGl6ZWQgbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzLiBJbnRyb2R1Y2VkIGluIEF1Z3VzdCAyMDIzIGFzIHRoZSBzdWNjZXNzb3IgdG8gR0dNTCwgR0dVRiByZXNvbHZlcyB0aGUgYmFja3dhcmRzLWNvbXBhdGliaWxpdHkgcHJvYmxlbXMgb2YgaXRzIHByZWRlY2Vzc29yIGJ5IGVtYmVkZGluZyBhbGwgbW9kZWwgbWV0YWRhdGEg4oCUIHRva2VuaXplciB2b2NhYnVsYXJ5LCBoeXBlcnBhcmFtZXRlcnMsIHRlbnNvciBuYW1lcywgYW5kIHF1YW50aXphdGlvbiB0eXBlIOKAlCBkaXJlY3RseSBpbiB0aGUgZmlsZSBoZWFkZXIuIEEgc2luZ2xlIEdHVUYgZmlsZSBpcyBmdWxseSBzZWxmLWNvbnRhaW5lZDogeW91IGNhbiBsb2FkIGl0IG9uIGFueSBwbGF0Zm9ybSBzdXBwb3J0ZWQgYnkgbGxhbWEuY3BwIHdpdGhvdXQgc2VwYXJhdGVseSBkb3dubG9hZGluZyBhIGNvbmZpZyBvciB0b2tlbml6ZXIuIFRoaXMgcG9ydGFiaWxpdHkgaGFzIG1hZGUgR0dVRiB0aGUgZG9taW5hbnQgZm9ybWF0IGZvciBydW5uaW5nIHF1YW50aXplZCBMTE1zIGxvY2FsbHkgb24gY29uc3VtZXIgaGFyZHdhcmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6ImxsYW1hLmNwcCBpbXBsZW1lbnRzIGEgZmFtaWx5IG9mIHF1YW50aXphdGlvbiBzY2hlbWVzIHJhbmdpbmcgZnJvbSAyLWJpdCAoUTJfSykgdG8gOC1iaXQgKFE4XzApLCBlYWNoIHRyYWRpbmcgbW9kZWwgc2l6ZSBhbmQgc3BlZWQgYWdhaW5zdCBwZXJwbGV4aXR5IGRlZ3JhZGF0aW9uLiBUaGUgSy1xdWFudCBmYW1pbHkgKFEyX0ssIFEzX0tfTSwgUTRfS19NLCBRNV9LX00sIFE2X0spIHVzZXMgYSB0d28tbGV2ZWwgc3VwZXItYmxvY2sgc3RydWN0dXJlIGFuZCBtaXhlZC1wcmVjaXNpb24gYmxvY2tzIHRvIGFjaGlldmUgYmV0dGVyIGFjY3VyYWN5IHRoYW4gdGhlIGxlZ2FjeSBpbnRlZ2VyIHF1YW50cyBhdCBzaW1pbGFyIGJpdCByYXRlcy4gVGhlIHR5cGljYWwgd29ya2Zsb3cgaXM6ICgxKSBkb3dubG9hZCBvciB0cmFpbiBhIG1vZGVsIGluIEh1Z2dpbmdGYWNlIGZvcm1hdDsgKDIpIGNvbnZlcnQgdG8gRjE2IEdHVUYgdXNpbmcgY29udmVydF9oZl90b19nZ3VmLnB5OyAoMykgcXVhbnRpemUgdG8gYSB0YXJnZXQgdHlwZSB1c2luZyB0aGUgbGxhbWEtcXVhbnRpemUgYmluYXJ5OyAoNCkgcnVuIGluZmVyZW5jZSB3aXRoIGxsYW1hLWNsaSBvciB2aWEgdGhlIGxsYW1hLWNwcC1weXRob24gUHl0aG9uIGJpbmRpbmdzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdHVUYgRmlsZSBTdHJ1Y3R1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgR0dVRiBmaWxlIHN0YXJ0cyB3aXRoIGEgZml4ZWQgaGVhZGVyOiBhIDQtYnl0ZSBtYWdpYyBudW1iZXIgKDB4NDY1NTQ3NDcsIGkuZS4gXHUwMDI3R0dVRlx1MDAyNyksIGEgdWludDMyIHZlcnNpb24gZmllbGQgKGN1cnJlbnRseSAzKSwgYW5kIGNvdW50cyBvZiB0ZW5zb3JzIGFuZCBrZXktdmFsdWUgbWV0YWRhdGEgZW50cmllcy4gVGhlIG1ldGFkYXRhIHNlY3Rpb24gc3RvcmVzIGFyYml0cmFyeSB0eXBlZCBrZXktdmFsdWUgcGFpcnMg4oCUIG1vZGVsIGFyY2hpdGVjdHVyZSwgY29udGV4dCBsZW5ndGgsIHJvcGUgcGFyYW1ldGVycywgdG9rZW5pemVyIHZvY2FidWxhcnksIHNwZWNpYWwgdG9rZW4gSURzLCBhbmQgbW9yZS4gVGVuc29ycyBhcmUgbGlzdGVkIGluIGEgdGVuc29yIGluZm8gc2VjdGlvbiAobmFtZSwgc2hhcGUsIGR0eXBlLCBieXRlIG9mZnNldCkgYmVmb3JlIHRoZSBhY3R1YWwgdGVuc29yIGRhdGEsIHdoaWNoIGlzIHN0b3JlZCBjb250aWd1b3VzbHkgYW5kIGFsaWduZWQgdG8gMzIgYnl0ZXMuIFRoaXMgYWxpZ25tZW50IGFsbG93cyBtZW1vcnktbWFwcGluZyB0aGUgZmlsZSBkaXJlY3RseSBmb3IgemVyby1jb3B5IGxvYWRpbmcgb24gc3VwcG9ydGVkIHN5c3RlbXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJNYWdpYzogMHg0NjU1NDc0NyAoXHUwMDI3R0dVRlx1MDAyNykg4oCUIGlkZW50aWZpZXMgdGhlIGZpbGUgYXMgR0dVRiByZWdhcmRsZXNzIG9mIGV4dGVuc2lvbi4iLCJWZXJzaW9uOiB1aW50MzIsIGN1cnJlbnRseSAzIOKAlCBHR1VGIHYxL3YyIGZpbGVzIGZyb20gMjAyMyByZXF1aXJlIGNvbnZlcnNpb24gZm9yIG1vZGVybiBsbGFtYS5jcHAuIiwibl90ZW5zb3JzIC8gbl9rdjogY291bnRzIHVzZWQgdG8gcGFyc2UgdGhlIHRlbnNvciBpbmZvIGFuZCBtZXRhZGF0YSBzZWN0aW9ucy4iLCJNZXRhZGF0YSBLViBwYWlyczogZ2VuZXJhbC5hcmNoaXRlY3R1cmUsIGdlbmVyYWwubmFtZSwgbGxhbWEuY29udGV4dF9sZW5ndGgsIHRva2VuaXplci5nZ21sLm1vZGVsLCB0b2tlbml6ZXIuZ2dtbC50b2tlbnMsIHRva2VuaXplci5nZ21sLnNjb3Jlcy4iLCJUZW5zb3IgZGF0YSBzZWN0aW9uOiAzMi1ieXRlIGFsaWduZWQ7IGFtZW5hYmxlIHRvIG1tYXAgZm9yIGZhc3QgbG9hZCBhbmQgcGFydGlhbCBHUFUgb2ZmbG9hZC4iLCJRdWFudGl6YXRpb24gdHlwZSBzdG9yZWQgcGVyIHRlbnNvcjogZWFjaCB0ZW5zb3IgaW5kZXBlbmRlbnRseSByZWNvcmRzIGl0cyBnZ21sX3R5cGUgZW51bSB2YWx1ZS4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUXVhbnRpemF0aW9uIFR5cGVzOiBRNF9LX00gYW5kIEZyaWVuZHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsbGFtYS5jcHAgcXVhbnRpemF0aW9uIHR5cGUgc3lzdGVtIGRpc3Rpbmd1aXNoZXMgbGVnYWN5IHF1YW50cyAoUTRfMCwgUTRfMSwgUTVfMCwgUTVfMSwgUThfMCkgZnJvbSB0aGUgbW9kZXJuIEstcXVhbnRzIChRMl9LLCBRM19LX00vUywgUTRfS19NL1MsIFE1X0tfTS9TLCBRNl9LKS4gTGVnYWN5IHF1YW50cyB1c2UgYSBmbGF0IGJsb2NrIG9mIDMyIHdlaWdodHMgd2l0aCBhIHNpbmdsZSBzY2FsZSBhbmQgb3B0aW9uYWwgYmlhcy4gSy1xdWFudHMgZ3JvdXAgMjU2IHdlaWdodHMgaW50byBhIHN1cGVyLWJsb2NrLCB3aXRoaW4gd2hpY2ggOCBzdWItYmxvY2tzIG9mIDMyIGVhY2ggY2FycnkgdGhlaXIgb3duIHNjYWxlOyB0aGUgc3VwZXItYmxvY2sgc2NhbGVzIGFyZSBzdG9yZWQgYXQgaGlnaGVyIHByZWNpc2lvbi4gVGhpcyBoaWVyYXJjaGljYWwgc3RydWN0dXJlIGNhcHR1cmVzIGxvY2FsIHZhcmlhdGlvbiBpbiB3ZWlnaHQgbWFnbml0dWRlIGJldHRlciB0aGFuIGEgc2luZ2xlIGdsb2JhbCBzY2FsZS4gVGhlIE0vUyBzdWZmaXhlcyAobWVkaXVtL3NtYWxsKSBpbiBLLXF1YW50cyBjb250cm9sIHdoaWNoIHRlbnNvciBsYXllcnMgZ2V0IHRoZSBoaWdoZXItcHJlY2lzaW9uIHF1YW50aXphdGlvbiB0cmVhdG1lbnQ6IE0ga2VlcHMgYXR0ZW50aW9uIGFuZCBmZWVkLWZvcndhcmQgb3V0cHV0IG1hdHJpY2VzIGF0IHNsaWdodGx5IGhpZ2hlciBxdWFsaXR5LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJRdWFudCBUeXBlIiwiQml0cy9XZWlnaHQiLCJTaXplICg3QikiLCJQUEwgSW5jcmVhc2UgdnMgRjE2IiwiVXNlIENhc2UiXSwicm93cyI6W1siUTJfSyIsIjIuNjMiLCJ+Mi43IEdCIiwiKzUuMCDigJMgOC4wIiwiRXh0cmVtZSBjb21wcmVzc2lvbiwgYWNjZXB0YWJsZSBxdWFsaXR5IGxvc3MsIHZlcnkgY29uc3RyYWluZWQgUkFNIl0sWyJRM19LX00iLCIzLjM1IiwifjMuNCBHQiIsIisxLjUg4oCTIDMuMCIsIlJBTS1saW1pdGVkIGRldmljZXMgd2hlcmUgUTQgZG9lcyBub3QgZml0OyBub3RpY2VhYmxlIHF1YWxpdHkgZGVncmFkYXRpb24iXSxbIlE0X0tfTSIsIjQuNTAiLCJ+NC42IEdCIiwiKzAuMSDigJMgMC4yIiwiQ29tbXVuaXR5IGRlZmF1bHQ7IGJlc3QgYWNjdXJhY3kvc2l6ZSB0cmFkZW9mZiBmb3IgbW9zdCA3QuKAkzEzQiBtb2RlbHMiXSxbIlE1X0tfTSIsIjUuNTAiLCJ+NS43IEdCIiwiKzAuMDUg4oCTIDAuMSIsIkhpZ2ggcXVhbGl0eTsgdXNlIHdoZW4gUkFNIHBlcm1pdHMgYW5kIFE0X0tfTSBQUEwgaXMgbWVhc3VyYWJseSB3b3JzZSJdLFsiUTZfSyIsIjYuNTYiLCJ+Ni43IEdCIiwiKzAuMDEg4oCTIDAuMDUiLCJOZWFyLWxvc3NsZXNzOyBqdXN0aWZpZWQgb25seSBvbiB2ZXJ5IGxhcmdlIG1vZGVscyBvciBzZW5zaXRpdmUgdGFza3MiXSxbIlE4XzAiLCI4LjUwIiwifjguNyBHQiIsIn4wLjAiLCJSZWZlcmVuY2UgcXVhbGl0eSBmb3IgYmVuY2htYXJraW5nOyByYXJlbHkgbmVlZGVkIG92ZXIgUTZfSyBpbiBwcmFjdGljZSJdLFsiRjE2IiwiMTYuMDAiLCJ+MTQuMCBHQiIsIjAuMCAoYmFzZWxpbmUpIiwiRnVsbCBwcmVjaXNpb247IEdQVSBpbmZlcmVuY2UsIGZpbmUtdHVuaW5nIHN0YXJ0aW5nIHBvaW50LCBjb252ZXJzaW9uIHNvdXJjZSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSy1RdWFudHMgdnMgTGVnYWN5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMZWdhY3kgcXVhbnRzIChRNF8wLCBRNV8wKSB1c2UgYSBzaW1wbGUgYmxvY2sgc2l6ZSBvZiAzMiB3aXRoIG9uZSBmbG9hdDMyIHNjYWxlIHBlciBibG9jay4gSy1xdWFudHMgdXNlIGEgc3VwZXItYmxvY2sgb2YgMjU2IHdlaWdodHMgc3ViZGl2aWRlZCBpbnRvIDggYmxvY2tzIG9mIDMyLCB3aXRoIHNjYWxlcyBzdG9yZWQgYXQgNi1iaXQgcHJlY2lzaW9uIGluIHRoZSBzdXBlci1ibG9jayBoZWFkZXIuIFRoZSBjcml0aWNhbCBkaWZmZXJlbmNlIGlzIHRoYXQgSy1xdWFudHMgYWxsb3cgdGhlIHF1YW50aXphdGlvbiBncmlkIHRvIGFkYXB0IHRvIGxvY2FsIHdlaWdodCBzdGF0aXN0aWNzIHdpdGhpbiB0aGUgc3VwZXItYmxvY2ssIHJhdGhlciB0aGFuIGFzc3VtaW5nIGEgc2luZ2xlIHNjYWxlIHdvcmtzIGZvciBhbGwgMjU2IHdlaWdodHMuIEVtcGlyaWNhbGx5LCBRNF9LX00gZGVsaXZlcnMgMC4y4oCTMC41IGxvd2VyIHBlcnBsZXhpdHkgdGhhbiBRNF8wIG9uIExsYW1hLTIgN0IgYXQgbmVhcmx5IHRoZSBzYW1lIG1vZGVsIHNpemUuIEZvciBuZXcgR0dVRiBmaWxlcywgbGVnYWN5IHF1YW50cyBleGlzdCBtYWlubHkgZm9yIGNvbXBhdGliaWxpdHkgd2l0aCBvbGRlciBpbmZlcmVuY2UgZW5naW5lczsgdGhlIEstcXVhbnQgdmFyaWFudHMgYXJlIHN0cmljdGx5IGJldHRlciBhbmQgc2hvdWxkIGJlIHRoZSBkZWZhdWx0IGNob2ljZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb252ZXJzaW9uIGZyb20gSHVnZ2luZ0ZhY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnZlcnRpbmcgYSBIdWdnaW5nRmFjZSBjaGVja3BvaW50IHRvIEdHVUYgaXMgYSB0d28tc3RlcCBwcm9jZXNzLiBGaXJzdCwgY29udmVydF9oZl90b19nZ3VmLnB5IChpbiB0aGUgbGxhbWEuY3BwIHJlcG8pIHJlYWRzIHRoZSBIdWdnaW5nRmFjZSBtb2RlbCBkaXJlY3RvcnkgYW5kIHdyaXRlcyBhbiBGMTYgR0dVRiBmaWxlIOKAlCB0aGlzIGlzIGxvc3NsZXNzLiBTZWNvbmQsIHRoZSBsbGFtYS1xdWFudGl6ZSBiaW5hcnkgcmVhZHMgdGhlIEYxNiBHR1VGIGFuZCB3cml0ZXMgYSBxdWFudGl6ZWQgR0dVRiB0byBhIHRhcmdldCBxdWFudCB0eXBlLiBUaGUgcXVhbnRpemUgc3RlcCBpcyBmYXN0IChtaW51dGVzIG9uIENQVSkgYW5kIG9wZXJhdGVzIGVudGlyZWx5IG9uIHRoZSBHR1VGIGZpbGUsIHNvIHRoZSBvcmlnaW5hbCBIdWdnaW5nRmFjZSB3ZWlnaHRzIGNhbiBiZSBkZWxldGVkIGFmdGVyIGNvbnZlcnNpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBzdWJwcm9jZXNzXG5pbXBvcnQgb3NcbmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5kZWYgY29udmVydF9hbmRfcXVhbnRpemUoXG4gICAgaGZfbW9kZWxfZGlyOiBzdHIsXG4gICAgb3V0cHV0X2Rpcjogc3RyLFxuICAgIHF1YW50X3R5cGU6IHN0ciA9IFwiUTRfS19NXCIsXG4gICAgbGxhbWFfY3BwX2Rpcjogc3RyID0gXCIvb3B0L2xsYW1hLmNwcFwiXG4pIC1cdTAwM2Ugc3RyOlxuICAgIFwiXCJcIkNvbnZlcnQgYSBIdWdnaW5nRmFjZSBtb2RlbCB0byBHR1VGIGFuZCBxdWFudGl6ZSB0byB0YXJnZXQgdHlwZS5cIlwiXCJcbiAgICBsbGFtYV9wYXRoID0gUGF0aChsbGFtYV9jcHBfZGlyKVxuICAgIG91dF9wYXRoID0gUGF0aChvdXRwdXRfZGlyKVxuICAgIG91dF9wYXRoLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSlcblxuICAgICMgU3RlcCAxOiBIRiAtXHUwMDNlIEYxNiBHR1VGIChsb3NzbGVzcylcbiAgICBmMTZfZ2d1ZiA9IG91dF9wYXRoIC8gXCJtb2RlbC1mMTYuZ2d1ZlwiXG4gICAgY29udmVydF9zY3JpcHQgPSBsbGFtYV9wYXRoIC8gXCJjb252ZXJ0X2hmX3RvX2dndWYucHlcIlxuICAgIHByaW50KGZcIlsxLzJdIENvbnZlcnRpbmcge2hmX21vZGVsX2Rpcn0gLVx1MDAzZSB7ZjE2X2dndWZ9XCIpXG4gICAgcmVzdWx0ID0gc3VicHJvY2Vzcy5ydW4oXG4gICAgICAgIFtcInB5dGhvbjNcIiwgc3RyKGNvbnZlcnRfc2NyaXB0KSwgaGZfbW9kZWxfZGlyLFxuICAgICAgICAgXCItLW91dGZpbGVcIiwgc3RyKGYxNl9nZ3VmKSwgXCItLW91dHR5cGVcIiwgXCJmMTZcIl0sXG4gICAgICAgIGNhcHR1cmVfb3V0cHV0PVRydWUsIHRleHQ9VHJ1ZSwgY2hlY2s9VHJ1ZVxuICAgIClcbiAgICBmMTZfc2l6ZSA9IGYxNl9nZ3VmLnN0YXQoKS5zdF9zaXplIC8gMWU5XG4gICAgcHJpbnQoZlwiICAgIEYxNiBHR1VGOiB7ZjE2X3NpemU6LjJmfSBHQlwiKVxuXG4gICAgIyBTdGVwIDI6IEYxNiBHR1VGIC1cdTAwM2UgcXVhbnRpemVkIEdHVUZcbiAgICBxdWFudF9nZ3VmID0gb3V0X3BhdGggLyBmXCJtb2RlbC17cXVhbnRfdHlwZX0uZ2d1ZlwiXG4gICAgcXVhbnRpemVfYmluID0gbGxhbWFfcGF0aCAvIFwiYnVpbGRcIiAvIFwiYmluXCIgLyBcImxsYW1hLXF1YW50aXplXCJcbiAgICBwcmludChmXCJbMi8yXSBRdWFudGl6aW5nIHRvIHtxdWFudF90eXBlfSAtXHUwMDNlIHtxdWFudF9nZ3VmfVwiKVxuICAgIHJlc3VsdCA9IHN1YnByb2Nlc3MucnVuKFxuICAgICAgICBbc3RyKHF1YW50aXplX2JpbiksIHN0cihmMTZfZ2d1ZiksIHN0cihxdWFudF9nZ3VmKSwgcXVhbnRfdHlwZV0sXG4gICAgICAgIGNhcHR1cmVfb3V0cHV0PVRydWUsIHRleHQ9VHJ1ZSwgY2hlY2s9VHJ1ZVxuICAgIClcbiAgICBxX3NpemUgPSBxdWFudF9nZ3VmLnN0YXQoKS5zdF9zaXplIC8gMWU5XG4gICAgcmF0aW8gPSBmMTZfc2l6ZSAvIHFfc2l6ZVxuICAgIHByaW50KGZcIiAgICBRdWFudGl6ZWQ6IHtxX3NpemU6LjJmfSBHQiAgKGNvbXByZXNzaW9uIHtyYXRpbzouMWZ9eClcIilcbiAgICByZXR1cm4gc3RyKHF1YW50X2dndWYpXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICBvdXQgPSBjb252ZXJ0X2FuZF9xdWFudGl6ZShcIi4vbWlzdHJhbC03Yi12MC4xXCIsIFwiLi9nZ3VmLW91dFwiLCBcIlE0X0tfTVwiKVxuICAgIHByaW50KGZcIkRvbmU6IHtvdXR9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUnVubmluZyB3aXRoIGxsYW1hLmNwcCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGxsYW1hLWNwcC1weXRob24gcGFja2FnZSBwcm92aWRlcyBQeXRob24gYmluZGluZ3MgZm9yIGxsYW1hLmNwcCwgZW5hYmxpbmcgbG9hZGluZyBHR1VGIG1vZGVscyBkaXJlY3RseSBpbiBQeXRob24uIFRoZSBMbGFtYSBjbGFzcyBhY2NlcHRzIHRoZSBtb2RlbCBwYXRoIHBsdXMgaGFyZHdhcmUgcGFyYW1ldGVyczogbl9ncHVfbGF5ZXJzIGNvbnRyb2xzIGhvdyBtYW55IHRyYW5zZm9ybWVyIGxheWVycyBhcmUgb2ZmbG9hZGVkIHRvIEdQVSAoTWV0YWwgb24gQXBwbGUgU2lsaWNvbiwgQ1VEQSBvbiBOVklESUEpLiBTZXR0aW5nIG5fZ3B1X2xheWVycz0tMSBvZmZsb2FkcyBhbGwgbGF5ZXJzLiBUaGUgbl9jdHggcGFyYW1ldGVyIHNldHMgdGhlIGNvbnRleHQgd2luZG93IHNpemUuIEdlbmVyYXRpb24gcmV0dXJucyB0b2tlbi1ieS10b2tlbiB3aXRoIG9wdGlvbmFsIHN0cmVhbWluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRpbWVcbmZyb20gbGxhbWFfY3BwIGltcG9ydCBMbGFtYVxuXG5kZWYgbG9hZF9hbmRfZ2VuZXJhdGUoXG4gICAgbW9kZWxfcGF0aDogc3RyLFxuICAgIHByb21wdDogc3RyLFxuICAgIG5fZ3B1X2xheWVyczogaW50ID0gMCxcbiAgICBuX2N0eDogaW50ID0gMjA0OCxcbiAgICBtYXhfdG9rZW5zOiBpbnQgPSAxMjhcbikgLVx1MDAzZSBkaWN0OlxuICAgIFwiXCJcIkxvYWQgYSBHR1VGIG1vZGVsIGFuZCBydW4gZ2VuZXJhdGlvbiwgcmVwb3J0aW5nIHRva2Vucy9zZWNvbmQuXCJcIlwiXG4gICAgcHJpbnQoZlwiTG9hZGluZyB7bW9kZWxfcGF0aH0gKG5fZ3B1X2xheWVycz17bl9ncHVfbGF5ZXJzfSkuLi5cIilcbiAgICBsbG0gPSBMbGFtYShcbiAgICAgICAgbW9kZWxfcGF0aD1tb2RlbF9wYXRoLFxuICAgICAgICBuX2dwdV9sYXllcnM9bl9ncHVfbGF5ZXJzLFxuICAgICAgICBuX2N0eD1uX2N0eCxcbiAgICAgICAgdmVyYm9zZT1GYWxzZVxuICAgIClcbiAgICAjIFdhcm11cCBwYXNzXG4gICAgXyA9IGxsbShwcm9tcHQsIG1heF90b2tlbnM9NCwgZWNobz1GYWxzZSlcblxuICAgICMgVGltZWQgZ2VuZXJhdGlvblxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIG91dHB1dCA9IGxsbShwcm9tcHQsIG1heF90b2tlbnM9bWF4X3Rva2VucywgZWNobz1GYWxzZSwgdGVtcGVyYXR1cmU9MC4wKVxuICAgIGVsYXBzZWQgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gdDBcblxuICAgIG5fdG9rZW5zID0gb3V0cHV0W1widXNhZ2VcIl1bXCJjb21wbGV0aW9uX3Rva2Vuc1wiXVxuICAgIHRwcyA9IG5fdG9rZW5zIC8gZWxhcHNlZFxuICAgIHRleHQgPSBvdXRwdXRbXCJjaG9pY2VzXCJdWzBdW1widGV4dFwiXVxuICAgIHByaW50KGZcIkdlbmVyYXRlZCB7bl90b2tlbnN9IHRva2VucyBpbiB7ZWxhcHNlZDouMmZ9cyAoe3RwczouMWZ9IHRvay9zKVwiKVxuICAgIHByaW50KGZcIk91dHB1dDoge3RleHRbOjEyMF19Li4uXCIpXG4gICAgcmV0dXJuIHtcInRva2Vuc19wZXJfc2Vjb25kXCI6IHRwcywgXCJ0ZXh0XCI6IHRleHR9XG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICByZXN1bHQgPSBsb2FkX2FuZF9nZW5lcmF0ZShcbiAgICAgICAgbW9kZWxfcGF0aD1cIi4vZ2d1Zi1vdXQvbW9kZWwtUTRfS19NLmdndWZcIixcbiAgICAgICAgcHJvbXB0PVwiRXhwbGFpbiBxdWFudGl6YXRpb24gaW4gb25lIHBhcmFncmFwaDpcIixcbiAgICAgICAgbl9ncHVfbGF5ZXJzPTM1XG4gICAgKVxuICAgIHByaW50KGZcIlRocm91Z2hwdXQ6IHtyZXN1bHRbXHUwMDI3dG9rZW5zX3Blcl9zZWNvbmRcdTAwMjddOi4xZn0gdG9rL3NcIikifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRpbWVcbmltcG9ydCBtYXRoXG5mcm9tIGxsYW1hX2NwcCBpbXBvcnQgTGxhbWFcblxuIyBCZW5jaG1hcmsgbXVsdGlwbGUgcXVhbnQgdHlwZXMg4oCUIHBlcnBsZXhpdHkgZXN0aW1hdGlvbiB2aWEgbG9nLWxpa2VsaWhvb2RcblFVQU5UX1RZUEVTID0gW1wiUTJfS1wiLCBcIlEzX0tfTVwiLCBcIlE0X0tfTVwiLCBcIlE1X0tfTVwiLCBcIlE4XzBcIl1cbk1PREVMX0RJUiA9IFwiLi9nZ3VmLW91dFwiXG5cblNBTVBMRV9URVhUID0gKFxuICAgIFwiVGhlIHRyYW5zZm9ybWVyIGFyY2hpdGVjdHVyZSByZWxpZXMgb24gc2VsZi1hdHRlbnRpb24gbWVjaGFuaXNtcyBcIlxuICAgIFwidG8gY2FwdHVyZSBsb25nLXJhbmdlIGRlcGVuZGVuY2llcyBpbiBzZXF1ZW5jZXMuIEVhY2ggYXR0ZW50aW9uIGhlYWQgXCJcbiAgICBcImluZGVwZW5kZW50bHkgbGVhcm5zIHRvIGZvY3VzIG9uIGRpZmZlcmVudCBwb3NpdGlvbnMsIGFuZCB0aGVpciBvdXRwdXRzIFwiXG4gICAgXCJhcmUgY29uY2F0ZW5hdGVkIGFuZCBwcm9qZWN0ZWQgYmFjayB0byB0aGUgbW9kZWwgZGltZW5zaW9uLlwiXG4pXG5cbnJlc3VsdHMgPSBbXVxuZm9yIHF0eXBlIGluIFFVQU5UX1RZUEVTOlxuICAgIG1vZGVsX3BhdGggPSBmXCJ7TU9ERUxfRElSfS9tb2RlbC17cXR5cGV9LmdndWZcIlxuICAgIHRyeTpcbiAgICAgICAgbGxtID0gTGxhbWEobW9kZWxfcGF0aD1tb2RlbF9wYXRoLCBuX2N0eD01MTIsIHZlcmJvc2U9RmFsc2UpXG4gICAgICAgICMgTG9nLWxpa2VsaWhvb2Qgb2Ygc2FtcGxlIHRleHQgYXMgUFBMIHByb3h5XG4gICAgICAgIHRva2VucyA9IGxsbS50b2tlbml6ZShTQU1QTEVfVEVYVC5lbmNvZGUoKSlcbiAgICAgICAgbG9nX2xpa2VsaWhvb2QgPSBsbG0uc2NvcmUodG9rZW5zLCBhZGRfYm9zPVRydWUpXG4gICAgICAgIHBwbF9lc3RpbWF0ZSA9IG1hdGguZXhwKC1sb2dfbGlrZWxpaG9vZCAvIG1heChsZW4odG9rZW5zKSAtIDEsIDEpKVxuICAgICAgICAjIE1lYXN1cmUgZ2VuZXJhdGlvbiBzcGVlZFxuICAgICAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgXyA9IGxsbShTQU1QTEVfVEVYVFs6ODBdLCBtYXhfdG9rZW5zPTMyLCBlY2hvPUZhbHNlKVxuICAgICAgICB0cHMgPSAzMiAvICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKChxdHlwZSwgcHBsX2VzdGltYXRlLCB0cHMpKVxuICAgICAgICBwcmludChmXCJ7cXR5cGU6XHUwMDNjMTJ9IFBQTD17cHBsX2VzdGltYXRlOjYuMmZ9ICB7dHBzOjYuMWZ9IHRvay9zXCIpXG4gICAgICAgIGRlbCBsbG1cbiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6XG4gICAgICAgIHByaW50KGZcIntxdHlwZTpcdTAwM2MxMn0gbW9kZWwgbm90IGZvdW5kIGF0IHttb2RlbF9wYXRofVwiKVxuXG5wcmludChcIlxcblN1bW1hcnkgKHNvcnRlZCBieSBQUEwpOlwiKVxuZm9yIHF0eXBlLCBwcGwsIHRwcyBpbiBzb3J0ZWQocmVzdWx0cywga2V5PWxhbWJkYSB4OiB4WzFdKTpcbiAgICBwcmludChmXCIgIHtxdHlwZX06IFBQTD17cHBsOi4yZn0sIHNwZWVkPXt0cHM6LjFmfSB0b2svc1wiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdGltZVxuZnJvbSBsbGFtYV9jcHAgaW1wb3J0IExsYW1hXG5cbmRlZiBiZW5jaG1hcmtfZ3B1X29mZmxvYWQoXG4gICAgbW9kZWxfcGF0aDogc3RyLFxuICAgIHByb21wdDogc3RyID0gXCJUaGUgY2FwaXRhbCBvZiBGcmFuY2UgaXNcIixcbiAgICBtYXhfdG9rZW5zOiBpbnQgPSA2NFxuKTpcbiAgICBcIlwiXCJDb21wYXJlIENQVS1vbmx5LCBwYXJ0aWFsIEdQVSwgYW5kIGZ1bGwgR1BVIG9mZmxvYWQgdGhyb3VnaHB1dC5cIlwiXCJcbiAgICBjb25maWdzID0gW1xuICAgICAgICB7XCJsYWJlbFwiOiBcIkNQVSBvbmx5XCIsICAgICAgXCJuX2dwdV9sYXllcnNcIjogMH0sXG4gICAgICAgIHtcImxhYmVsXCI6IFwiUGFydGlhbCBHUFVcIiwgICBcIm5fZ3B1X2xheWVyc1wiOiAxNn0sXG4gICAgICAgIHtcImxhYmVsXCI6IFwiRnVsbCBHUFVcIiwgICAgICBcIm5fZ3B1X2xheWVyc1wiOiAtMX0sXG4gICAgXVxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciBjZmcgaW4gY29uZmlnczpcbiAgICAgICAgbGxtID0gTGxhbWEoXG4gICAgICAgICAgICBtb2RlbF9wYXRoPW1vZGVsX3BhdGgsXG4gICAgICAgICAgICBuX2dwdV9sYXllcnM9Y2ZnW1wibl9ncHVfbGF5ZXJzXCJdLFxuICAgICAgICAgICAgbl9jdHg9NTEyLCB2ZXJib3NlPUZhbHNlXG4gICAgICAgIClcbiAgICAgICAgIyBXYXJtdXBcbiAgICAgICAgXyA9IGxsbShwcm9tcHQsIG1heF90b2tlbnM9NCwgZWNobz1GYWxzZSlcbiAgICAgICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgICAgIG91dCA9IGxsbShwcm9tcHQsIG1heF90b2tlbnM9bWF4X3Rva2VucywgZWNobz1GYWxzZSwgdGVtcGVyYXR1cmU9MC4wKVxuICAgICAgICBlbGFwc2VkID0gdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwXG4gICAgICAgIG5fdG9rID0gb3V0W1widXNhZ2VcIl1bXCJjb21wbGV0aW9uX3Rva2Vuc1wiXVxuICAgICAgICB0cHMgPSBuX3RvayAvIGVsYXBzZWRcbiAgICAgICAgcmVzdWx0cy5hcHBlbmQoKGNmZ1tcImxhYmVsXCJdLCBjZmdbXCJuX2dwdV9sYXllcnNcIl0sIHRwcykpXG4gICAgICAgIHByaW50KGZcIntjZmdbXHUwMDI3bGFiZWxcdTAwMjddOlx1MDAzYzE0fSBsYXllcnM9e2NmZ1tcdTAwMjduX2dwdV9sYXllcnNcdTAwMjddOlx1MDAzZTN9ICB7dHBzOjYuMWZ9IHRvay9zXCIpXG4gICAgICAgIGRlbCBsbG1cbiAgICBiZXN0ID0gbWF4KHJlc3VsdHMsIGtleT1sYW1iZGEgeDogeFsyXSlcbiAgICBwcmludChmXCJcXG5CZXN0OiB7YmVzdFswXX0gYXQge2Jlc3RbMl06LjFmfSB0b2svc1wiKVxuICAgIHJldHVybiByZXN1bHRzXG5cbmJlbmNobWFya19ncHVfb2ZmbG9hZChcIi4vZ2d1Zi1vdXQvbW9kZWwtUTRfS19NLmdndWZcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcnkgYW5kIFNwZWVkIFRyYWRlb2ZmcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRvbWluYW50IGZhY3RvciBpbiBHR1VGIG1vZGVsIHBlcmZvcm1hbmNlIGlzIHdoZXRoZXIgdGhlIGVudGlyZSBtb2RlbCBmaXRzIGluIEdQVSBWUkFNLiBXaGVuIGFsbCBsYXllcnMgYXJlIG9mZmxvYWRlZCB0byBHUFUsIGluZmVyZW5jZSBydW5zIGF0IEdQVSBtZW1vcnkgYmFuZHdpZHRoICh0eXBpY2FsbHkgNDAw4oCTOTAwIEdCL3Mgb24gbW9kZXJuIGNvbnN1bWVyIEdQVXMpLCBkZWxpdmVyaW5nIDUw4oCTMTUwIHRva2Vucy9zZWNvbmQgZm9yIGEgN0IgbW9kZWwuIFdoZW4gbGF5ZXJzIHNwaWxsIHRvIENQVSBSQU0sIGVhY2ggbGF5ZXIgdHJhbnNpdGlvbiBpbmN1cnMgUENJZSBiYW5kd2lkdGggb3ZlcmhlYWQgKHR5cGljYWxseSAzMuKAkzY0IEdCL3MpLCBkcm9wcGluZyB0aHJvdWdocHV0IHN1YnN0YW50aWFsbHkuIE9uIEFwcGxlIFNpbGljb24sIHRoZSB1bmlmaWVkIG1lbW9yeSBhcmNoaXRlY3R1cmUgZWxpbWluYXRlcyB0aGlzIGRpc3RpbmN0aW9uOiBNZXRhbC1iYWNrZWQgbGxhbWEuY3BwIHJ1bnMgR0dVRiBtb2RlbHMgaW4gdW5pZmllZCBSQU0gd2l0aCBHUFUtbGlrZSBiYW5kd2lkdGguIEZvciBDUFUtb25seSBpbmZlcmVuY2Ugb24geDg2LCBRNF9LX00gaXMgdXN1YWxseSB0aGUgZmFzdGVzdCBxdWFudCB0eXBlIGJlY2F1c2UgaXRzIDQuNS1iaXQgcmVwcmVzZW50YXRpb24gbWF4aW1pc2VzIHRoZSBhbW91bnQgb2YgbW9kZWwgdGhhdCBmaXRzIGluIEwzIGNhY2hlIHJlbGF0aXZlIHRvIGNvbXB1dGUgdGltZS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiUTRfS19NIENvbW11bml0eSBEZWZhdWx0IiwiY29udGVudCI6IlE0X0tfTSBpcyB0aGUgY29tbXVuaXR5IGRlZmF1bHQgZm9yIGdvb2QgcmVhc29uOiBpdCBoaXRzIHRoZSBzd2VldCBzcG90IG9mIDQuNSBiaXRzIHBlciB3ZWlnaHQgb24gYXZlcmFnZSB3aGlsZSBrZWVwaW5nIHBlcnBsZXhpdHkgd2l0aGluIDAuMeKAkzAuMiBvZiBGUDE2IGZvciBtb3N0IG1vZGVscy4gVW5sZXNzIHlvdSBhcmUgc2V2ZXJlbHkgUkFNLWNvbnN0cmFpbmVkICh1c2UgUTNfS19NKSBvciBuZWVkIG5lYXItbG9zc2xlc3MgcXVhbGl0eSAodXNlIFE2X0spLCBRNF9LX00gaXMgdGhlIHJpZ2h0IGNob2ljZSBmb3IgN0IgYW5kIDEzQiBtb2RlbHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiR0dVRiBpcyBzZWxmLWNvbnRhaW5lZDogdG9rZW5pemVyLCBhcmNoaXRlY3R1cmUgbWV0YWRhdGEsIGFuZCBxdWFudGl6ZWQgdGVuc29ycyBhcmUgYWxsIGluIG9uZSBmaWxlIOKAlCBubyBzZXBhcmF0ZSBjb25maWcgZG93bmxvYWQuIiwiQ29udmVyc2lvbiBpcyB0d28gc3RlcHM6IEhGIC1cdTAwM2UgRjE2IEdHVUYgKGNvbnZlcnRfaGZfdG9fZ2d1Zi5weSksIHRoZW4gRjE2IEdHVUYgLVx1MDAzZSBxdWFudGl6ZWQgR0dVRiAobGxhbWEtcXVhbnRpemUpLiIsIkstcXVhbnRzIG91dHBlcmZvcm0gbGVnYWN5IHF1YW50cyBhdCB0aGUgc2FtZSBiaXQgcmF0ZTsgYWx3YXlzIHByZWZlciBRNF9LX00gb3ZlciBRNF8wIGZvciBuZXcgR0dVRiBmaWxlcy4iLCJRNF9LX006IDQuNSBiaXRzL3dlaWdodCwgfjQuNiBHQiBmb3IgN0IgbW9kZWxzLCBQUEwgd2l0aGluIDAuMeKAkzAuMiBvZiBGMTYg4oCUIHRoZSBjb21tdW5pdHkgZGVmYXVsdC4iLCJVc2Ugbl9ncHVfbGF5ZXJzPS0xIGluIGxsYW1hLWNwcC1weXRob24gdG8gb2ZmbG9hZCBhbGwgbGF5ZXJzIHRvIEdQVTsgcGFydGlhbCBvZmZsb2FkIGlzIHVzZWZ1bCB3aGVuIFZSQU0gaXMgaW5zdWZmaWNpZW50LiIsIk9uIEFwcGxlIFNpbGljb24gKE1ldGFsKSwgbGxhbWEuY3BwIHVzZXMgdW5pZmllZCBtZW1vcnkg4oCUIFE0X0tfTSA3QiBtb2RlbHMgcnVuIGF0IDUw4oCTODAgdG9rL3Mgb24gTTEvTTIgd2l0aG91dCBhIGRpc2NyZXRlIEdQVS4iLCJROF8wIGlzIGEgbG9zc2xlc3MtcXVhbGl0eSByZWZlcmVuY2UgcXVhbnQ7IG9ubHkganVzdGlmaWVkIGZvciBiZW5jaG1hcmtpbmcgb3Igd2hlbiBHUFUgVlJBTSBleGNlZWRzIG1vZGVsIHNpemUgaW4gRjE2LiIsIk1vbml0b3IgUkFNIHVzYWdlIHdpdGggbl9jdHg6IGEgN0IgUTRfS19NIG1vZGVsIHVzZXMgfjQuNiBHQiBmb3Igd2VpZ2h0cyBwbHVzIGNvbnRleHQgS1YgY2FjaGUgKH4wLjUgR0IgcGVyIDIwNDggdG9rZW5zIGF0IGZwMTYpLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# GGUF Format and llama.cpp Quantization

GGUF (GPT-Generated Unified Format) is the binary file format used by llama.cpp to store quantized large language models. Introduced in August 2023 as the successor to GGML, GGUF resolves the backwards-compatibility problems of its predecessor by embedding all model metadata — tokenizer vocabulary, hyperparameters, tensor names, and quantization type — directly in the file header. A single GGUF file is fully self-contained: you can load it on any platform supported by llama.cpp without separately downloading a config or tokenizer. This portability has made GGUF the dominant format for running quantized LLMs locally on consumer hardware.

## Overview

llama.cpp implements a family of quantization schemes ranging from 2-bit (Q2_K) to 8-bit (Q8_0), each trading model size and speed against perplexity degradation. The K-quant family (Q2_K, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K) uses a two-level super-block structure and mixed-precision blocks to achieve better accuracy than the legacy integer quants at similar bit rates. The typical workflow is: (1) download or train a model in HuggingFace format; (2) convert to F16 GGUF using convert_hf_to_gguf.py; (3) quantize to a target type using the llama-quantize binary; (4) run inference with llama-cli or via the llama-cpp-python Python bindings.

## GGUF File Structure

A GGUF file starts with a fixed header: a 4-byte magic number (0x46554747, i.e. 'GGUF'), a uint32 version field (currently 3), and counts of tensors and key-value metadata entries. The metadata section stores arbitrary typed key-value pairs — model architecture, context length, rope parameters, tokenizer vocabulary, special token IDs, and more. Tensors are listed in a tensor info section (name, shape, dtype, byte offset) before the actual tensor data, which is stored contiguously and aligned to 32 bytes. This alignment allows memory-mapping the file directly for zero-copy loading on supported systems.

- Magic: 0x46554747 ('GGUF') — identifies the file as GGUF regardless of extension.
- Version: uint32, currently 3 — GGUF v1/v2 files from 2023 require conversion for modern llama.cpp.
- n_tensors / n_kv: counts used to parse the tensor info and metadata sections.
- Metadata KV pairs: general.architecture, general.name, llama.context_length, tokenizer.ggml.model, tokenizer.ggml.tokens, tokenizer.ggml.scores.
- Tensor data section: 32-byte aligned; amenable to mmap for fast load and partial GPU offload.
- Quantization type stored per tensor: each tensor independently records its ggml_type enum value.

## Quantization Types: Q4_K_M and Friends

The llama.cpp quantization type system distinguishes legacy quants (Q4_0, Q4_1, Q5_0, Q5_1, Q8_0) from the modern K-quants (Q2_K, Q3_K_M/S, Q4_K_M/S, Q5_K_M/S, Q6_K). Legacy quants use a flat block of 32 weights with a single scale and optional bias. K-quants group 256 weights into a super-block, within which 8 sub-blocks of 32 each carry their own scale; the super-block scales are stored at higher precision. This hierarchical structure captures local variation in weight magnitude better than a single global scale. The M/S suffixes (medium/small) in K-quants control which tensor layers get the higher-precision quantization treatment: M keeps attention and feed-forward output matrices at slightly higher quality.

| Quant Type | Bits/Weight | Size (7B) | PPL Increase vs F16 | Use Case |
| --- | --- | --- | --- | --- |
| Q2_K | 2.63 | ~2.7 GB | +5.0 – 8.0 | Extreme compression, acceptable quality loss, very constrained RAM |
| Q3_K_M | 3.35 | ~3.4 GB | +1.5 – 3.0 | RAM-limited devices where Q4 does not fit; noticeable quality degradation |
| Q4_K_M | 4.50 | ~4.6 GB | +0.1 – 0.2 | Community default; best accuracy/size tradeoff for most 7B–13B models |
| Q5_K_M | 5.50 | ~5.7 GB | +0.05 – 0.1 | High quality; use when RAM permits and Q4_K_M PPL is measurably worse |
| Q6_K | 6.56 | ~6.7 GB | +0.01 – 0.05 | Near-lossless; justified only on very large models or sensitive tasks |
| Q8_0 | 8.50 | ~8.7 GB | ~0.0 | Reference quality for benchmarking; rarely needed over Q6_K in practice |
| F16 | 16.00 | ~14.0 GB | 0.0 (baseline) | Full precision; GPU inference, fine-tuning starting point, conversion source |

## K-Quants vs Legacy

Legacy quants (Q4_0, Q5_0) use a simple block size of 32 with one float32 scale per block. K-quants use a super-block of 256 weights subdivided into 8 blocks of 32, with scales stored at 6-bit precision in the super-block header. The critical difference is that K-quants allow the quantization grid to adapt to local weight statistics within the super-block, rather than assuming a single scale works for all 256 weights. Empirically, Q4_K_M delivers 0.2–0.5 lower perplexity than Q4_0 on Llama-2 7B at nearly the same model size. For new GGUF files, legacy quants exist mainly for compatibility with older inference engines; the K-quant variants are strictly better and should be the default choice.

## Conversion from HuggingFace

Converting a HuggingFace checkpoint to GGUF is a two-step process. First, convert_hf_to_gguf.py (in the llama.cpp repo) reads the HuggingFace model directory and writes an F16 GGUF file — this is lossless. Second, the llama-quantize binary reads the F16 GGUF and writes a quantized GGUF to a target quant type. The quantize step is fast (minutes on CPU) and operates entirely on the GGUF file, so the original HuggingFace weights can be deleted after conversion.

```python
import subprocess
import os
from pathlib import Path

def convert_and_quantize(
    hf_model_dir: str,
    output_dir: str,
    quant_type: str = "Q4_K_M",
    llama_cpp_dir: str = "/opt/llama.cpp"
) -> str:
    """Convert a HuggingFace model to GGUF and quantize to target type."""
    llama_path = Path(llama_cpp_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Step 1: HF -> F16 GGUF (lossless)
    f16_gguf = out_path / "model-f16.gguf"
    convert_script = llama_path / "convert_hf_to_gguf.py"
    print(f"[1/2] Converting {hf_model_dir} -> {f16_gguf}")
    result = subprocess.run(
        ["python3", str(convert_script), hf_model_dir,
         "--outfile", str(f16_gguf), "--outtype", "f16"],
        capture_output=True, text=True, check=True
    )
    f16_size = f16_gguf.stat().st_size / 1e9
    print(f"    F16 GGUF: {f16_size:.2f} GB")

    # Step 2: F16 GGUF -> quantized GGUF
    quant_gguf = out_path / f"model-{quant_type}.gguf"
    quantize_bin = llama_path / "build" / "bin" / "llama-quantize"
    print(f"[2/2] Quantizing to {quant_type} -> {quant_gguf}")
    result = subprocess.run(
        [str(quantize_bin), str(f16_gguf), str(quant_gguf), quant_type],
        capture_output=True, text=True, check=True
    )
    q_size = quant_gguf.stat().st_size / 1e9
    ratio = f16_size / q_size
    print(f"    Quantized: {q_size:.2f} GB  (compression {ratio:.1f}x)")
    return str(quant_gguf)

if __name__ == "__main__":
    out = convert_and_quantize("./mistral-7b-v0.1", "./gguf-out", "Q4_K_M")
    print(f"Done: {out}")
```

## Running with llama.cpp

The llama-cpp-python package provides Python bindings for llama.cpp, enabling loading GGUF models directly in Python. The Llama class accepts the model path plus hardware parameters: n_gpu_layers controls how many transformer layers are offloaded to GPU (Metal on Apple Silicon, CUDA on NVIDIA). Setting n_gpu_layers=-1 offloads all layers. The n_ctx parameter sets the context window size. Generation returns token-by-token with optional streaming.

```python
import time
from llama_cpp import Llama

def load_and_generate(
    model_path: str,
    prompt: str,
    n_gpu_layers: int = 0,
    n_ctx: int = 2048,
    max_tokens: int = 128
) -> dict:
    """Load a GGUF model and run generation, reporting tokens/second."""
    print(f"Loading {model_path} (n_gpu_layers={n_gpu_layers})...")
    llm = Llama(
        model_path=model_path,
        n_gpu_layers=n_gpu_layers,
        n_ctx=n_ctx,
        verbose=False
    )
    # Warmup pass
    _ = llm(prompt, max_tokens=4, echo=False)

    # Timed generation
    t0 = time.perf_counter()
    output = llm(prompt, max_tokens=max_tokens, echo=False, temperature=0.0)
    elapsed = time.perf_counter() - t0

    n_tokens = output["usage"]["completion_tokens"]
    tps = n_tokens / elapsed
    text = output["choices"][0]["text"]
    print(f"Generated {n_tokens} tokens in {elapsed:.2f}s ({tps:.1f} tok/s)")
    print(f"Output: {text[:120]}...")
    return {"tokens_per_second": tps, "text": text}

if __name__ == "__main__":
    result = load_and_generate(
        model_path="./gguf-out/model-Q4_K_M.gguf",
        prompt="Explain quantization in one paragraph:",
        n_gpu_layers=35
    )
    print(f"Throughput: {result['tokens_per_second']:.1f} tok/s")
```

```python
import time
import math
from llama_cpp import Llama

# Benchmark multiple quant types — perplexity estimation via log-likelihood
QUANT_TYPES = ["Q2_K", "Q3_K_M", "Q4_K_M", "Q5_K_M", "Q8_0"]
MODEL_DIR = "./gguf-out"

SAMPLE_TEXT = (
    "The transformer architecture relies on self-attention mechanisms "
    "to capture long-range dependencies in sequences. Each attention head "
    "independently learns to focus on different positions, and their outputs "
    "are concatenated and projected back to the model dimension."
)

results = []
for qtype in QUANT_TYPES:
    model_path = f"{MODEL_DIR}/model-{qtype}.gguf"
    try:
        llm = Llama(model_path=model_path, n_ctx=512, verbose=False)
        # Log-likelihood of sample text as PPL proxy
        tokens = llm.tokenize(SAMPLE_TEXT.encode())
        log_likelihood = llm.score(tokens, add_bos=True)
        ppl_estimate = math.exp(-log_likelihood / max(len(tokens) - 1, 1))
        # Measure generation speed
        t0 = time.perf_counter()
        _ = llm(SAMPLE_TEXT[:80], max_tokens=32, echo=False)
        tps = 32 / (time.perf_counter() - t0)
        results.append((qtype, ppl_estimate, tps))
        print(f"{qtype:<12} PPL={ppl_estimate:6.2f}  {tps:6.1f} tok/s")
        del llm
    except FileNotFoundError:
        print(f"{qtype:<12} model not found at {model_path}")

print("\nSummary (sorted by PPL):")
for qtype, ppl, tps in sorted(results, key=lambda x: x[1]):
    print(f"  {qtype}: PPL={ppl:.2f}, speed={tps:.1f} tok/s")
```

```python
import time
from llama_cpp import Llama

def benchmark_gpu_offload(
    model_path: str,
    prompt: str = "The capital of France is",
    max_tokens: int = 64
):
    """Compare CPU-only, partial GPU, and full GPU offload throughput."""
    configs = [
        {"label": "CPU only",      "n_gpu_layers": 0},
        {"label": "Partial GPU",   "n_gpu_layers": 16},
        {"label": "Full GPU",      "n_gpu_layers": -1},
    ]
    results = []
    for cfg in configs:
        llm = Llama(
            model_path=model_path,
            n_gpu_layers=cfg["n_gpu_layers"],
            n_ctx=512, verbose=False
        )
        # Warmup
        _ = llm(prompt, max_tokens=4, echo=False)
        t0 = time.perf_counter()
        out = llm(prompt, max_tokens=max_tokens, echo=False, temperature=0.0)
        elapsed = time.perf_counter() - t0
        n_tok = out["usage"]["completion_tokens"]
        tps = n_tok / elapsed
        results.append((cfg["label"], cfg["n_gpu_layers"], tps))
        print(f"{cfg['label']:<14} layers={cfg['n_gpu_layers']:>3}  {tps:6.1f} tok/s")
        del llm
    best = max(results, key=lambda x: x[2])
    print(f"\nBest: {best[0]} at {best[2]:.1f} tok/s")
    return results

benchmark_gpu_offload("./gguf-out/model-Q4_K_M.gguf")
```

## Memory and Speed Tradeoffs

The dominant factor in GGUF model performance is whether the entire model fits in GPU VRAM. When all layers are offloaded to GPU, inference runs at GPU memory bandwidth (typically 400–900 GB/s on modern consumer GPUs), delivering 50–150 tokens/second for a 7B model. When layers spill to CPU RAM, each layer transition incurs PCIe bandwidth overhead (typically 32–64 GB/s), dropping throughput substantially. On Apple Silicon, the unified memory architecture eliminates this distinction: Metal-backed llama.cpp runs GGUF models in unified RAM with GPU-like bandwidth. For CPU-only inference on x86, Q4_K_M is usually the fastest quant type because its 4.5-bit representation maximises the amount of model that fits in L3 cache relative to compute time.

> **Q4_K_M Community Default**: Q4_K_M is the community default for good reason: it hits the sweet spot of 4.5 bits per weight on average while keeping perplexity within 0.1–0.2 of FP16 for most models. Unless you are severely RAM-constrained (use Q3_K_M) or need near-lossless quality (use Q6_K), Q4_K_M is the right choice for 7B and 13B models.

## Key Takeaways

- GGUF is self-contained: tokenizer, architecture metadata, and quantized tensors are all in one file — no separate config download.
- Conversion is two steps: HF -> F16 GGUF (convert_hf_to_gguf.py), then F16 GGUF -> quantized GGUF (llama-quantize).
- K-quants outperform legacy quants at the same bit rate; always prefer Q4_K_M over Q4_0 for new GGUF files.
- Q4_K_M: 4.5 bits/weight, ~4.6 GB for 7B models, PPL within 0.1–0.2 of F16 — the community default.
- Use n_gpu_layers=-1 in llama-cpp-python to offload all layers to GPU; partial offload is useful when VRAM is insufficient.
- On Apple Silicon (Metal), llama.cpp uses unified memory — Q4_K_M 7B models run at 50–80 tok/s on M1/M2 without a discrete GPU.
- Q8_0 is a lossless-quality reference quant; only justified for benchmarking or when GPU VRAM exceeds model size in F16.
- Monitor RAM usage with n_ctx: a 7B Q4_K_M model uses ~4.6 GB for weights plus context KV cache (~0.5 GB per 2048 tokens at fp16).

---

