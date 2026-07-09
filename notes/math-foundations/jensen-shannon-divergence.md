---
title: "Jensen-Shannon Divergence"
slug: "jensen-shannon-divergence"
description: "JSD(P,Q) = (1/2)KL(P‖M) + (1/2)KL(Q‖M) is the symmetric, bounded sibling of KL divergence. Covers its derivation from KL, the metric property of √JSD, the GAN connection, why disjoint supports break GAN training, the Wasserstein fix, and practical dataset comparison."
tags: ["information-theory", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEplbnNlbi1TaGFubm9uIGRpdmVyZ2VuY2UgYWRkcmVzc2VzIHR3byBjcml0aWNhbCBsaW1pdGF0aW9ucyBvZiBLTCBkaXZlcmdlbmNlOiBhc3ltbWV0cnkgYW5kIHVuYm91bmRlZG5lc3MuIEJ5IHN5bW1ldHJpemluZyB2aWEgdGhlIG1peHR1cmUgZGlzdHJpYnV0aW9uIE09KFArUSkvMiwgSlNEIGlzIHN5bW1ldHJpYywgYWx3YXlzIGZpbml0ZSAoZXZlbiBmb3IgZGlzdHJpYnV0aW9ucyB3aXRoIGRpc2pvaW50IHN1cHBvcnRzKSwgYW5kIGl0cyBzcXVhcmUgcm9vdCBpcyBhIHByb3BlciBtZXRyaWMuIFRoZXNlIHByb3BlcnRpZXMgbWFrZSBpdCB0aGUgbmF0dXJhbCBjaG9pY2UgZm9yIGNvbXBhcmluZyBkYXRhc2V0cyBhbmQgdW5kZXJzdGFuZGluZyBHQU4gdHJhaW5pbmcgZHluYW1pY3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVmaW5pdGlvbiBhbmQgRGVyaXZhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEplbnNlbi1TaGFubm9uIGRpdmVyZ2VuY2UgYmV0d2VlbiBQIGFuZCBRIGlzIEpTRChQ4oCWUSkgPSAoMS8yKcK3S0woUOKAlk0pICsgKDEvMinCt0tMKFHigJZNKSwgd2hlcmUgTSA9IChQK1EpLzIgaXMgdGhlIG1peHR1cmUgKG1pZHBvaW50KSBkaXN0cmlidXRpb24uIEV4cGFuZGluZzogSlNEKFAsUSkgPSBIKE0pIC0gKDEvMilIKFApIC0gKDEvMilIKFEpLCB3aGVyZSBIIGRlbm90ZXMgU2hhbm5vbiBlbnRyb3B5LiBUaGlzIHNob3dzIEpTRCBhcyB0aGUgZXhjZXNzIGVudHJvcHkgb2YgdGhlIG1peHR1cmUgb3ZlciB0aGUgYXZlcmFnZSBlbnRyb3B5IG9mIHRoZSBjb21wb25lbnRzIOKAlCBhIG1lYXN1cmUgb2YgaG93IFx1MDAyN2RpZmZlcmVudFx1MDAyNyBQIGFuZCBRIGFyZS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkpTRCBCb3VuZHMiLCJjb250ZW50IjoiMCDiiaQgSlNEKFAsUSkg4omkIGxvZyAyIG5hdHMgKG9yIDAg4omkIEpTRCDiiaQgMSBiaXQgd2hlbiB1c2luZyBsb2cgYmFzZSAyKS4gSlNEID0gMCBpZmYgUCA9IFEgZXZlcnl3aGVyZS4gSlNEID0gbG9nIDIgbmF0cyAoPSAxIGJpdCkgaWZmIFAgYW5kIFEgaGF2ZSBjb21wbGV0ZWx5IGRpc2pvaW50IHN1cHBvcnRzLiBUaGVzZSB0aWdodCBib3VuZHMgbWFrZSBKU0QgaW50ZXJwcmV0YWJsZSBhcyBhIGZyYWN0aW9uIG9mIG1heGltdW0gcG9zc2libGUgZGl2ZXJnZW5jZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBlbnRyb3B5IGFzIHNjaXB5X2VudHJvcHlcblxuZGVmIGpzZChwLCBxLCBiYXNlPTIpOlxuICAgIFwiXCJcIlxuICAgIEplbnNlbi1TaGFubm9uIGRpdmVyZ2VuY2UuXG4gICAgUmV0dXJucyB2YWx1ZSBpbiBiaXRzIChiYXNlPTIpIG9yIG5hdHMgKGJhc2U9ZSkuXG4gICAgSlNEKFAsUSkgPSAwLjUgKiBLTChQfHxNKSArIDAuNSAqIEtMKFF8fE0pICB3aGVyZSBNID0gKFArUSkvMlxuICAgIFwiXCJcIlxuICAgIHAgPSBucC5hc2FycmF5KHAsIGR0eXBlPWZsb2F0KVxuICAgIHEgPSBucC5hc2FycmF5KHEsIGR0eXBlPWZsb2F0KVxuICAgIHAgPSBwIC8gcC5zdW0oKVxuICAgIHEgPSBxIC8gcS5zdW0oKVxuICAgIG0gPSAwLjUgKiAocCArIHEpXG4gICAgIyBzY2lweSBlbnRyb3B5IGNvbXB1dGVzIEtMKFB8fFEpID0gc3VtIHAgbG9nKHAvcSkgaW4gbmF0c1xuICAgIGtsX3BtID0gc2NpcHlfZW50cm9weShwLCBtKVxuICAgIGtsX3FtID0gc2NpcHlfZW50cm9weShxLCBtKVxuICAgIGpzZF9uYXRzID0gMC41ICoga2xfcG0gKyAwLjUgKiBrbF9xbVxuICAgIGlmIGJhc2UgPT0gMjpcbiAgICAgICAgcmV0dXJuIGpzZF9uYXRzIC8gbnAubG9nKDIpXG4gICAgcmV0dXJuIGpzZF9uYXRzXG5cbiMgVmVyaWZ5IHN5bW1ldHJ5XG5wID0gbnAuYXJyYXkoWzAuNSwgMC4zLCAwLjE1LCAwLjA1XSlcbnEgPSBucC5hcnJheShbMC4xLCAwLjQsIDAuNCwgIDAuMV0pXG5cbmpzZF9wcSA9IGpzZChwLCBxKVxuanNkX3FwID0ganNkKHEsIHApXG5wcmludChmXCJKU0QoUCxRKSA9IHtqc2RfcHE6LjZmfSBiaXRzXCIpXG5wcmludChmXCJKU0QoUSxQKSA9IHtqc2RfcXA6LjZmfSBiaXRzXCIpXG5wcmludChmXCJTeW1tZXRyaWM6IHtucC5pc2Nsb3NlKGpzZF9wcSwganNkX3FwKX1cIilcbnByaW50KGZcIkJvdW5kZWQgWzAsMV06IHswIFx1MDAzYz0ganNkX3BxIFx1MDAzYz0gMX1cIilcbnByaW50KGZcInNxcnQoSlNEKSA9IHtucC5zcXJ0KGpzZF9wcSk6LjRmfSAgKGEgdmFsaWQgbWV0cmljKVwiKVxuXG4jIEpTRCA9IDEgYml0IGZvciBjb21wbGV0ZWx5IGRpc2pvaW50IHN1cHBvcnRzXG5wX2Rpc2ogPSBucC5hcnJheShbMS4wLCAwLjBdKVxucV9kaXNqID0gbnAuYXJyYXkoWzAuMCwgMS4wXSlcbnByaW50KGZcIlxcbkRpc2pvaW50IHN1cHBvcnRzOiBKU0QgPSB7anNkKHBfZGlzaiwgcV9kaXNqKTouNGZ9IGJpdHMgIChzaG91bGQgYmUgMS4wKVwiKVxucHJpbnQoZlwiSWRlbnRpY2FsOiAgICAgICAgICBKU0QgPSB7anNkKHAsIHApOi40Zn0gYml0cyAgKHNob3VsZCBiZSAwLjApXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSlNEIGlzIEZpbml0ZSBmb3IgRGlzam9pbnQgU3VwcG9ydHMg4oCUIFVubGlrZSBLTCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS0wgZGl2ZXJnZW5jZSBibG93cyB1cCB0byBpbmZpbml0eSB3aGVuIHRoZSBkaXN0cmlidXRpb25zIGhhdmUgbm9uLW92ZXJsYXBwaW5nIHN1cHBvcnRzOiBpZiBQKHgpXHUwMDNlMCBidXQgUSh4KT0wLCB0aGVuIGxvZyhQKHgpL1EoeCkpID0gK+KIni4gSlNEIGlzIGltbXVuZSB0byB0aGlzIGJlY2F1c2UgdGhlIG1peHR1cmUgTT0oUCtRKS8yIGFsd2F5cyBoYXMgc3VwcG9ydCBjb3ZlcmluZyBib3RoIFAgYW5kIFEsIHNvIE0oeClcdTAwM2UwIHdoZXJldmVyIGVpdGhlciBQKHgpXHUwMDNlMCBvciBRKHgpXHUwMDNlMC4gVGhpcyBtYWtlcyBKU0QgbnVtZXJpY2FsbHkgc3RhYmxlIGFuZCBtZWFuaW5nZnVsIGV2ZW4gZm9yIGRpc3RyaWJ1dGlvbnMgY29uY2VudHJhdGVkIG9uIGVudGlyZWx5IHNlcGFyYXRlIHBhcnRzIG9mIHRoZSBzcGFjZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBlbnRyb3B5IGFzIHNjaXB5X2VudHJvcHlcblxuZGVmIGtsX3NhZmUocCwgcSk6XG4gICAgXCJcIlwiS0woUOKAllEpID0gK2luZiBpZiBRIGhhcyB6ZXJvcyB3aGVyZSBQIGhhcyBtYXNzLlwiXCJcIlxuICAgIHAgPSBucC5hc2FycmF5KHAsIGR0eXBlPWZsb2F0KVxuICAgIHEgPSBucC5hc2FycmF5KHEsIGR0eXBlPWZsb2F0KVxuICAgIG1hc2sgPSBwIFx1MDAzZSAwXG4gICAgaWYgbnAuYW55KHFbbWFza10gPT0gMCk6XG4gICAgICAgIHJldHVybiBmbG9hdChcdTAwMjdpbmZcdTAwMjcpXG4gICAgcmV0dXJuIHNjaXB5X2VudHJvcHkocCwgcSlcblxuZGVmIGpzZChwLCBxKTpcbiAgICBwID0gbnAuYXNhcnJheShwLCBkdHlwZT1mbG9hdCkgLyBucC5zdW0ocClcbiAgICBxID0gbnAuYXNhcnJheShxLCBkdHlwZT1mbG9hdCkgLyBucC5zdW0ocSlcbiAgICBtID0gMC41ICogKHAgKyBxKVxuICAgIHJldHVybiAwLjUgKiBzY2lweV9lbnRyb3B5KHAsIG0pICsgMC41ICogc2NpcHlfZW50cm9weShxLCBtKVxuXG4jIFRocmVlIHRlc3QgY2FzZXMgd2l0aCBpbmNyZWFzaW5nIHN1cHBvcnQgb3ZlcmxhcFxuY2FzZXMgPSBbXG4gICAgKFwiSWRlbnRpY2FsICAgICAgXCIsIFswLjQsMC4zLDAuMiwwLjFdLCBbMC40LDAuMywwLjIsMC4xXSksXG4gICAgKFwiUGFydGlhbCBvdmVybGFwXCIsIFswLjUsMC40LDAuMSwwLjBdLCBbMC4wLDAuMywwLjQsMC4zXSksXG4gICAgKFwiRGlzam9pbnQgICAgICAgXCIsIFswLjYsMC40LDAuMCwwLjBdLCBbMC4wLDAuMCwwLjcsMC4zXSksXG5dXG5cbnByaW50KGZcIntcdTAwMjdDYXNlXHUwMDI3Olx1MDAzYzE4fSB7XHUwMDI3S0woUOKAllEpXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3S0woUeKAllApXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3SlNEXHUwMDI3Olx1MDAzZTEwfVwiKVxucHJpbnQoXCItXCIgKiA1NilcbmZvciBuYW1lLCBwLCBxIGluIGNhc2VzOlxuICAgIGtsX2Z3ZCA9IGtsX3NhZmUocCwgcSlcbiAgICBrbF9yZXYgPSBrbF9zYWZlKHEsIHApXG4gICAgaiA9IGpzZChwLCBxKSAvIG5wLmxvZygyKSAgIyBjb252ZXJ0IHRvIGJpdHNcbiAgICBrbF9md2RfcyA9IGZcIntrbF9md2Q6LjRmfVwiIGlmIGtsX2Z3ZCAhPSBmbG9hdChcdTAwMjdpbmZcdTAwMjcpIGVsc2UgXCIgICAgaW5mXCJcbiAgICBrbF9yZXZfcyA9IGZcIntrbF9yZXY6LjRmfVwiIGlmIGtsX3JldiAhPSBmbG9hdChcdTAwMjdpbmZcdTAwMjcpIGVsc2UgXCIgICAgaW5mXCJcbiAgICBwcmludChmXCJ7bmFtZTpcdTAwM2MxOH0ge2tsX2Z3ZF9zOlx1MDAzZTEyfSB7a2xfcmV2X3M6XHUwMDNlMTJ9IHtqOlx1MDAzZTEwLjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdBTiBUcmFpbmluZyBNaW5pbWl6ZXMgSlNEIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHb29kZmVsbG93IGV0IGFsLiAoMjAxNCkgc2hvd2VkIHRoYXQgdGhlIG9yaWdpbmFsIEdBTiBtaW5pbWF4IGdhbWUg4oCUIHdpdGggYW4gb3B0aW1hbCBkaXNjcmltaW5hdG9yIOKAlCBpcyBlcXVpdmFsZW50IHRvIG1pbmltaXppbmcgSlNEKFBfcmVhbCDigJYgUF9nZW4pICsgbG9nIDQgKGEgY29uc3RhbnQpLiBUaGUgZ2VuZXJhdG9yIG1pbmltaXplcyBKU0QgYmV0d2VlbiB0aGUgcmVhbCBkYXRhIGRpc3RyaWJ1dGlvbiBhbmQgdGhlIGdlbmVyYXRlZCBkaXN0cmlidXRpb24uIFRoaXMgdGhlb3JldGljYWwgaW5zaWdodCBpbGx1bWluYXRlZCB3aHkgR0FOcyB3b3JrLCBidXQgYWxzbyByZXZlYWxlZCBhIGZ1bmRhbWVudGFsIGZsYXc6IHdoZW4gUF9yZWFsIGFuZCBQX2dlbiBoYXZlIGRpc2pvaW50IHN1cHBvcnRzIChjb21tb24gZWFybHkgaW4gdHJhaW5pbmcpLCBKU0QgPSBsb2cgMiA9IGNvbnN0YW50LCBhbmQgdGhlIGdlbmVyYXRvciByZWNlaXZlcyB6ZXJvIGdyYWRpZW50LiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiRGlzam9pbnQgU3VwcG9ydHMgPSBaZXJvIEdBTiBHcmFkaWVudCIsImNvbnRlbnQiOiJXaGVuIHRoZSByZWFsIGFuZCBnZW5lcmF0ZWQgZGlzdHJpYnV0aW9ucyBkb25cdTAwMjd0IG92ZXJsYXAgKGUuZy4sIHJlYWwgaW1hZ2VzIGxpZSBvbiBhIGxvdy1kaW1lbnNpb25hbCBtYW5pZm9sZCBmYXIgZnJvbSBlYXJseSBnZW5lcmF0b3Igb3V0cHV0cyksIEpTRCByZWFjaGVzIGl0cyBtYXhpbXVtIG9mIGxvZyAyIG5hdHMgYW5kIGl0cyBncmFkaWVudCB3aXRoIHJlc3BlY3QgdG8gdGhlIGdlbmVyYXRvciBpcyB6ZXJvLiBUcmFpbmluZyBzdGFsbHMuIFRoaXMgaXMgd2h5IEdBTiB0cmFpbmluZyBpcyBub3RvcmlvdXNseSB1bnN0YWJsZSBhdCB0aGUgYmVnaW5uaW5nIGFuZCB3aHkgV2Fzc2Vyc3RlaW4gR0FOIChXR0FOKSB3YXMgZGV2ZWxvcGVkIGFzIGEgZml4LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IGVudHJvcHkgYXMgc2NpcHlfZW50cm9weVxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYganNkX2JpdHMocCwgcSk6XG4gICAgcCA9IG5wLmFzYXJyYXkocCwgZHR5cGU9ZmxvYXQpIC8gbnAuc3VtKHApXG4gICAgcSA9IG5wLmFzYXJyYXkocSwgZHR5cGU9ZmxvYXQpIC8gbnAuc3VtKHEpXG4gICAgbSA9IDAuNSAqIChwICsgcSlcbiAgICByZXR1cm4gKDAuNSAqIHNjaXB5X2VudHJvcHkocCwgbSkgKyAwLjUgKiBzY2lweV9lbnRyb3B5KHEsIG0pKSAvIG5wLmxvZygyKVxuXG5kZWYga2xfYml0c19zYWZlKHAsIHEpOlxuICAgIHAgPSBucC5hc2FycmF5KHAsIGR0eXBlPWZsb2F0KSAvIG5wLnN1bShwKVxuICAgIHEgPSBucC5hc2FycmF5KHEsIGR0eXBlPWZsb2F0KSAvIG5wLnN1bShxKVxuICAgIG1hc2sgPSBwIFx1MDAzZSAwXG4gICAgaWYgbnAuYW55KHFbbWFza10gPT0gMCk6XG4gICAgICAgIHJldHVybiBmbG9hdChcdTAwMjdpbmZcdTAwMjcpXG4gICAgcmV0dXJuIHNjaXB5X2VudHJvcHkocCwgcSkgLyBucC5sb2coMilcblxuIyBTaW11bGF0ZSBHQU4gdHJhaW5pbmc6IGdlbmVyYXRlZCBkaXN0cmlidXRpb24gZ3JhZHVhbGx5IHNoaWZ0cyB0b3dhcmQgcmVhbFxueCA9IG5wLmFyYW5nZSgyMCkgICMgZGlzY3JldGUgc3BhY2VcbnBfcmVhbCA9IG5wLnplcm9zKDIwKTsgcF9yZWFsWzE0OjE4XSA9IFswLjIsIDAuNCwgMC4zLCAwLjFdICAjIHJlYWw6IG1vZGVzIGF0IDE0LTE3XG5cbmpzZF92YWxzLCBrbF92YWxzID0gW10sIFtdXG5zaGlmdHMgPSBucC5saW5zcGFjZSgwLCAxNCwgNTApICAjIGdlbmVyYXRvciBzaGlmdHMgZnJvbSBsZWZ0IHRvIHJpZ2h0XG5cbmZvciBzaGlmdCBpbiBzaGlmdHM6XG4gICAgY2VudGVyID0gaW50KHNoaWZ0KVxuICAgIHBfZ2VuID0gbnAuemVyb3MoMjApXG4gICAgZm9yIGksIHcgaW4gemlwKFtjZW50ZXIsIGNlbnRlcisxLCBjZW50ZXIrMl0sIFswLjMsIDAuNSwgMC4yXSk6XG4gICAgICAgIGlmIDAgXHUwMDNjPSBpIFx1MDAzYyAyMDpcbiAgICAgICAgICAgIHBfZ2VuW2ldICs9IHdcbiAgICBwX2dlbiA9IHBfZ2VuIC8gcF9nZW4uc3VtKClcbiAgICBqc2RfdmFscy5hcHBlbmQoanNkX2JpdHMocF9yZWFsLCBwX2dlbikpXG4gICAga2xfdmFscy5hcHBlbmQoa2xfYml0c19zYWZlKHBfcmVhbCwgcF9nZW4pKVxuXG5wbHQuZmlndXJlKGZpZ3NpemU9KDgsNCkpXG5wbHQucGxvdChzaGlmdHMsIGpzZF92YWxzLCBsYWJlbD1cdTAwMjdKU0QgKGJpdHMpXHUwMDI3LCBjb2xvcj1cdTAwMjdzdGVlbGJsdWVcdTAwMjcpXG5wbHQucGxvdChzaGlmdHMsIFttaW4odiwgNSkgZm9yIHYgaW4ga2xfdmFsc10sIGxhYmVsPVx1MDAyN0tMKFBfcmVhbOKAllBfZ2VuKSBbY2xpcHBlZF1cdTAwMjcsIGNvbG9yPVx1MDAyN3RvbWF0b1x1MDAyNywgbGluZXN0eWxlPVx1MDAyNy0tXHUwMDI3KVxucGx0LmF4aGxpbmUoMS4wLCBjb2xvcj1cdTAwMjdncmF5XHUwMDI3LCBsaW5lc3R5bGU9XHUwMDI3Olx1MDAyNywgYWxwaGE9MC41LCBsYWJlbD1cdTAwMjdKU0QgbWF4ID0gMSBiaXRcdTAwMjcpXG5wbHQueGxhYmVsKFx1MDAyN0dlbmVyYXRvciBtZWFuIHNoaWZ0IHRvd2FyZCByZWFsIGRhdGFcdTAwMjcpXG5wbHQueWxhYmVsKFx1MDAyN0RpdmVyZ2VuY2UgKGJpdHMpXHUwMDI3KTsgcGx0LnRpdGxlKFx1MDAyN0pTRCB2cyBLTCBEdXJpbmcgR0FOIFRyYWluaW5nIFNpbXVsYXRpb25cdTAwMjcpXG5wbHQubGVnZW5kKCk7IHBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNhdmVmaWcoXHUwMDI3Z2FuX2pzZC5wbmdcdTAwMjcsIGRwaT0xNTApXG5wcmludChmXCJKU0QgYXQgZnVsbCBvdmVybGFwIChkaXNqb2ludOKGkm92ZXJsYXApOiB7anNkX3ZhbHNbMF06LjNmfSDihpIge2pzZF92YWxzWy0xXTouM2Z9IGJpdHNcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEYXRhc2V0IFNpbWlsYXJpdHkgTWVhc3VyZW1lbnQgd2l0aCBKU0QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkpTRCBwcm92aWRlcyBhIHByaW5jaXBsZWQgd2F5IHRvIG1lYXN1cmUgaG93IHNpbWlsYXIgdHdvIGRhdGFzZXRzIGFyZSwgd2l0aG91dCByZXF1aXJpbmcgdGhlaXIgc3VwcG9ydHMgdG8gbWF0Y2guIEdpdmVuIGVtcGlyaWNhbCBkaXN0cmlidXRpb25zIFBfQSBhbmQgUF9CIChlLmcuLCB0b2tlbiBmcmVxdWVuY3kgZGlzdHJpYnV0aW9ucywgbGFiZWwgZGlzdHJpYnV0aW9ucywgZmVhdHVyZSBoaXN0b2dyYW1zKSwgSlNEKFBfQSwgUF9CKSDiiIggWzAsIDEgYml0XSBxdWFudGlmaWVzIGRpdmVyZ2VuY2UuIOKImkpTRCDiiIggWzAsIDFdIGlzIGEgdHJ1ZSBtZXRyaWMuIFRoaXMgaXMgdXNlZCBmb3IgZGF0YXNldCBzaGlmdCBkZXRlY3Rpb24sIGRvbWFpbiBhZGFwdGF0aW9uIGV2YWx1YXRpb24sIGFuZCBOTFAgY29ycHVzIGNvbXBhcmlzb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgZW50cm9weSBhcyBzY2lweV9lbnRyb3B5XG5mcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyXG5cbmRlZiBqc2RfYml0cyhwLCBxKTpcbiAgICBwID0gbnAuYXNhcnJheShwLCBkdHlwZT1mbG9hdClcbiAgICBxID0gbnAuYXNhcnJheShxLCBkdHlwZT1mbG9hdClcbiAgICAjIEFsaWduIHN1cHBvcnRzXG4gICAgYXNzZXJ0IGxlbihwKSA9PSBsZW4ocSlcbiAgICBwID0gcCAvIHAuc3VtKCk7IHEgPSBxIC8gcS5zdW0oKVxuICAgIG0gPSAwLjUgKiAocCArIHEpXG4gICAgcmV0dXJuICgwLjUgKiBzY2lweV9lbnRyb3B5KHAsIG0pICsgMC41ICogc2NpcHlfZW50cm9weShxLCBtKSkgLyBucC5sb2coMilcblxuZGVmIHRleHRfZGlzdHJpYnV0aW9uKHRleHQsIHZvY2FiX3NpemU9MjYpOlxuICAgIFwiXCJcIkxldHRlciBmcmVxdWVuY3kgZGlzdHJpYnV0aW9uIG92ZXIgYS16LlwiXCJcIlxuICAgIGNvdW50cyA9IG5wLnplcm9zKHZvY2FiX3NpemUpXG4gICAgZm9yIGMgaW4gdGV4dC5sb3dlcigpOlxuICAgICAgICBpZiBcdTAwMjdhXHUwMDI3IFx1MDAzYz0gYyBcdTAwM2M9IFx1MDAyN3pcdTAwMjc6XG4gICAgICAgICAgICBjb3VudHNbb3JkKGMpIC0gb3JkKFx1MDAyN2FcdTAwMjcpXSArPSAxXG4gICAgcmV0dXJuIGNvdW50cyAvIGNvdW50cy5zdW0oKSBpZiBjb3VudHMuc3VtKCkgXHUwMDNlIDAgZWxzZSBjb3VudHNcblxuIyBDb21wYXJlIGxldHRlciBkaXN0cmlidXRpb25zIG9mIGRpZmZlcmVudCB0ZXh0IGRvbWFpbnNcbmNvcnB1cyA9IHtcbiAgICBcIkVuZ2xpc2ggcHJvc2VcIjogXCJ0aGUgcXVpY2sgYnJvd24gZm94IGp1bXBzIG92ZXIgdGhlIGxhenkgZG9nIGFuZCB0aGUgY2F0IHNhdCBvbiB0aGUgbWF0XCIsXG4gICAgXCJTY2llbnRpZmljIHRleHRcIjogXCJxdWFudHVtIGVudGFuZ2xlbWVudCBlbnRyb3B5IGVpZ2VudmFsdWUgbWF0cml4IHByb2JhYmlsaXR5IGRpc3RyaWJ1dGlvblwiLFxuICAgIFwiR2VybWFuIHRleHRcIjogICBcImRpZSBzY2huZWxsZSBicmF1bmUgZnVjaHMgc3ByaW5ndCB1ZWJlciBkZW4gZmF1bGVuIGh1bmQgdW5kIGRpZSBrYXR6ZVwiLFxuICAgIFwiUmFuZG9tIGxldHRlcnNcIjogXCJ6cXh2d2tqenF4dndranpxeHZ3a2p6cXh2d2tqenF4dndranpxeHZ3a2pcIixcbn1cblxuZGlzdHMgPSB7bmFtZTogdGV4dF9kaXN0cmlidXRpb24odGV4dCkgZm9yIG5hbWUsIHRleHQgaW4gY29ycHVzLml0ZW1zKCl9XG5uYW1lcyA9IGxpc3QoZGlzdHMua2V5cygpKVxuXG5wcmludChcIkpTRCAoYml0cykgYmV0d2VlbiB0ZXh0IGNvcnBvcmE6XCIpXG5wcmludChmXCJ7XHUwMDI3XHUwMDI3OjI1fVwiLCBlbmQ9XCJcIilcbmZvciBuIGluIG5hbWVzOiBwcmludChmXCJ7bls6MTVdOlx1MDAzZTE3fVwiLCBlbmQ9XCJcIilcbnByaW50KClcbmZvciBuMSBpbiBuYW1lczpcbiAgICBwcmludChmXCJ7bjFbOjI1XTpcdTAwM2MyNX1cIiwgZW5kPVwiXCIpXG4gICAgZm9yIG4yIGluIG5hbWVzOlxuICAgICAgICBqID0ganNkX2JpdHMoZGlzdHNbbjFdLCBkaXN0c1tuMl0pXG4gICAgICAgIHByaW50KGZcIntqOlx1MDAzZTE3LjRmfVwiLCBlbmQ9XCJcIilcbiAgICBwcmludCgpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1lYXN1cmUiLCJTeW1tZXRyaWMiLCJCb3VuZGVkIiwiVHJpYW5nbGUgSW5lcS4iLCJHcmFkaWVudCB3LyBEaXNqb2ludCBTdXBwb3J0cyIsIlR5cGljYWwgVXNlIl0sInJvd3MiOltbIktMKFDigJZRKSIsIk5vIiwiTm8gKDAgdG8g4oieKSIsIk5vIiwiVW5kZWZpbmVkICgr4oieKSIsIk1MRSwgY3Jvc3MtZW50cm9weSwgRUxCTyJdLFsiSlNEKFAsUSkiLCJZZXMiLCJZZXMgKDAgdG8gMSBiaXQpIiwiTm8gKEpTRCBpdHNlbGYpIiwiWmVybyAoY29uc3RhbnQgPSBsb2cgMikiLCJHQU4gb3JpZ2luYWwsIGRhdGFzZXQgY29tcGFyaXNvbiJdLFsi4oiaSlNEKFAsUSkiLCJZZXMiLCJZZXMgKDAgdG8gMSkiLCJZZXMgKHByb3BlciBtZXRyaWMpIiwiWmVybyIsIkRhdGFzZXQgZGlzdGFuY2UgbWV0cmljIl0sWyJXYXNzZXJzdGVpbiBX4oKBIiwiWWVzIiwiTm8gKDAgdG8g4oieKSIsIlllcyIsIk5vbi16ZXJvLCBpbmZvcm1hdGl2ZSIsIldHQU4sIG9wdGltYWwgdHJhbnNwb3J0Il0sWyJNTUQiLCJZZXMiLCJObyAoMCB0byDiiJ4pIiwiWWVzIiwiTm9uLXplcm8gKGtlcm5lbC1iYXNlZCkiLCJUd28tc2FtcGxlIHRlc3RzLCBnZW5lcmF0aXZlIG1vZGVscyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2Fzc2Vyc3RlaW4gRGlzdGFuY2UgYXMgdGhlIEZpeCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXJqb3Zza3kgZXQgYWwuICgyMDE3KSBwcm9wb3NlZCBXYXNzZXJzdGVpbiBHQU4gdG8gc29sdmUgdGhlIHplcm8tZ3JhZGllbnQgcHJvYmxlbS4gVGhlIFdhc3NlcnN0ZWluLTEgZGlzdGFuY2UgV+KCgShQLFEpID0gaW5mX3vOs+KIiM6gKFAsUSl9IEVfeyh4LHkpfs6zfVvigJZ4LXnigJZdIGlzIGZpbml0ZSBhbmQgaGFzIG5vbi16ZXJvIGdyYWRpZW50cyBldmVuIHdoZW4gUCBhbmQgUSBoYXZlIGRpc2pvaW50IHN1cHBvcnRzLCBiZWNhdXNlIGl0IG1lYXN1cmVzIHRoZSBjb3N0IG9mIFx1MDAyN3RyYW5zcG9ydGluZ1x1MDAyNyBtYXNzIGZyb20gb25lIGRpc3RyaWJ1dGlvbiB0byBhbm90aGVyLiBXR0FOIHRyYWlucyBhIExpcHNjaGl0ei1jb25zdHJhaW5lZCBjcml0aWMgdG8gZXN0aW1hdGUgV+KCgSBpbnN0ZWFkIG9mIGEgcHJvYmFiaWxpdHktZXN0aW1hdGluZyBkaXNjcmltaW5hdG9yLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJXaGVuIHRvIFVzZSBKU0QgdnMgS0wgdnMgV2Fzc2Vyc3RlaW4iLCJjb250ZW50IjoiVXNlIEtMIHdoZW4gY29tcGFyaW5nIGRpc3RyaWJ1dGlvbnMgd2l0aCBvdmVybGFwcGluZyBzdXBwb3J0IGZvciBNTEUgb3IgdmFyaWF0aW9uYWwgaW5mZXJlbmNlLiBVc2UgSlNEIHdoZW4geW91IG5lZWQgYSBzeW1tZXRyaWMsIGJvdW5kZWQgbWVhc3VyZSAoZGF0YXNldCBzaW1pbGFyaXR5LCBldmFsdWF0aW9uKS4gVXNlIFdhc3NlcnN0ZWluIHdoZW4gZGlzdHJpYnV0aW9ucyBtYXkgYmUgZGlzam9pbnQgYW5kIHlvdSBuZWVkIG1lYW5pbmdmdWwgZ3JhZGllbnRzIChHQU4gdHJhaW5pbmcsIG9wdGltYWwgdHJhbnNwb3J0KS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdW1tYXJ5In0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJKU0QoUCxRKSA9IEgoKFArUSkvMikgLSAoMS8yKUgoUCkgLSAoMS8yKUgoUSk6IGV4Y2VzcyBlbnRyb3B5IG9mIHRoZSBtaXh0dXJlIiwiU3ltbWV0cmljOiBKU0QoUCxRKSA9IEpTRChRLFApIGFsd2F5cyIsIkJvdW5kZWQ6IDAg4omkIEpTRCDiiaQgbG9nIDIgbmF0cyAoPSAxIGJpdCB3aXRoIGxvZyBiYXNlIDIpIiwiQWx3YXlzIGZpbml0ZTogZXZlbiBmb3IgZGlzam9pbnQgc3VwcG9ydHMgKEpTRCA9IDEgYml0IG1heGltdW0pIiwi4oiaSlNEIGlzIGEgcHJvcGVyIG1ldHJpYyBzYXRpc2Z5aW5nIHRoZSB0cmlhbmdsZSBpbmVxdWFsaXR5IiwiT3JpZ2luYWwgR0FOIG1pbmltaXplcyBKU0Qg4oCUIGdyYWRpZW50IGlzIHplcm8gZm9yIGRpc2pvaW50IHN1cHBvcnRzIiwiV0dBTiBmaXhlcyB0aGlzIGJ5IHJlcGxhY2luZyBKU0QvS0wgd2l0aCBXYXNzZXJzdGVpbiBkaXN0YW5jZSIsIlByYWN0aWNhbCB1c2VzOiBkYXRhc2V0IHNoaWZ0IGRldGVjdGlvbiwgZG9tYWluIGNvbXBhcmlzb24sIE5MUCBjb3JwdXMgYW5hbHlzaXMiXX0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSmVuc2VuLVNoYW5ub24gZGl2ZXJnZW5jZSBicmlkZ2VzIHB1cmUgaW5mb3JtYXRpb24gdGhlb3J5IGFuZCBtb2Rlcm4gZGVlcCBsZWFybmluZy4gSXRzIHJvbGUgaW4gdGhlIEdBTiBvYmplY3RpdmUgbW90aXZhdGVkIHRoZSBkZXZlbG9wbWVudCBvZiBvcHRpbWFsIHRyYW5zcG9ydCBtZXRob2RzIGZvciBnZW5lcmF0aXZlIG1vZGVscywgYW5kIGl0cyBtZXRyaWMgcHJvcGVydGllcyAodmlhIOKImkpTRCkgbWFrZSBpdCB0aGUgcHJpbmNpcGxlZCBjaG9pY2UgZm9yIG1lYXN1cmluZyBkaXN0cmlidXRpb25hbCBzaW1pbGFyaXR5IGluIHByYWN0aWNlLiBVbmRlcnN0YW5kaW5nIEpTRCBjbGFyaWZpZXMgbm90IGp1c3QgR0FOcyBidXQgdGhlIGJyb2FkZXIgbGFuZHNjYXBlIG9mIGRpdmVyZ2VuY2UgbWVhc3VyZXMgdXNlZCB0aHJvdWdob3V0IG1hY2hpbmUgbGVhcm5pbmcuIn1d"
---
# Jensen-Shannon Divergence

The Jensen-Shannon divergence addresses two critical limitations of KL divergence: asymmetry and unboundedness. By symmetrizing via the mixture distribution M=(P+Q)/2, JSD is symmetric, always finite (even for distributions with disjoint supports), and its square root is a proper metric. These properties make it the natural choice for comparing datasets and understanding GAN training dynamics.

## Definition and Derivation

The Jensen-Shannon divergence between P and Q is JSD(P‖Q) = (1/2)·KL(P‖M) + (1/2)·KL(Q‖M), where M = (P+Q)/2 is the mixture (midpoint) distribution. Expanding: JSD(P,Q) = H(M) - (1/2)H(P) - (1/2)H(Q), where H denotes Shannon entropy. This shows JSD as the excess entropy of the mixture over the average entropy of the components — a measure of how 'different' P and Q are.

> **JSD Bounds**: 0 ≤ JSD(P,Q) ≤ log 2 nats (or 0 ≤ JSD ≤ 1 bit when using log base 2). JSD = 0 iff P = Q everywhere. JSD = log 2 nats (= 1 bit) iff P and Q have completely disjoint supports. These tight bounds make JSD interpretable as a fraction of maximum possible divergence.

```python
import numpy as np
from scipy.stats import entropy as scipy_entropy

def jsd(p, q, base=2):
    """
    Jensen-Shannon divergence.
    Returns value in bits (base=2) or nats (base=e).
    JSD(P,Q) = 0.5 * KL(P||M) + 0.5 * KL(Q||M)  where M = (P+Q)/2
    """
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    p = p / p.sum()
    q = q / q.sum()
    m = 0.5 * (p + q)
    # scipy entropy computes KL(P||Q) = sum p log(p/q) in nats
    kl_pm = scipy_entropy(p, m)
    kl_qm = scipy_entropy(q, m)
    jsd_nats = 0.5 * kl_pm + 0.5 * kl_qm
    if base == 2:
        return jsd_nats / np.log(2)
    return jsd_nats

# Verify symmetry
p = np.array([0.5, 0.3, 0.15, 0.05])
q = np.array([0.1, 0.4, 0.4,  0.1])

jsd_pq = jsd(p, q)
jsd_qp = jsd(q, p)
print(f"JSD(P,Q) = {jsd_pq:.6f} bits")
print(f"JSD(Q,P) = {jsd_qp:.6f} bits")
print(f"Symmetric: {np.isclose(jsd_pq, jsd_qp)}")
print(f"Bounded [0,1]: {0 <= jsd_pq <= 1}")
print(f"sqrt(JSD) = {np.sqrt(jsd_pq):.4f}  (a valid metric)")

# JSD = 1 bit for completely disjoint supports
p_disj = np.array([1.0, 0.0])
q_disj = np.array([0.0, 1.0])
print(f"\nDisjoint supports: JSD = {jsd(p_disj, q_disj):.4f} bits  (should be 1.0)")
print(f"Identical:          JSD = {jsd(p, p):.4f} bits  (should be 0.0)")
```

## JSD is Finite for Disjoint Supports — Unlike KL

KL divergence blows up to infinity when the distributions have non-overlapping supports: if P(x)>0 but Q(x)=0, then log(P(x)/Q(x)) = +∞. JSD is immune to this because the mixture M=(P+Q)/2 always has support covering both P and Q, so M(x)>0 wherever either P(x)>0 or Q(x)>0. This makes JSD numerically stable and meaningful even for distributions concentrated on entirely separate parts of the space.

```python
import numpy as np
from scipy.stats import entropy as scipy_entropy

def kl_safe(p, q):
    """KL(P‖Q) = +inf if Q has zeros where P has mass."""
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    mask = p > 0
    if np.any(q[mask] == 0):
        return float('inf')
    return scipy_entropy(p, q)

def jsd(p, q):
    p = np.asarray(p, dtype=float) / np.sum(p)
    q = np.asarray(q, dtype=float) / np.sum(q)
    m = 0.5 * (p + q)
    return 0.5 * scipy_entropy(p, m) + 0.5 * scipy_entropy(q, m)

# Three test cases with increasing support overlap
cases = [
    ("Identical      ", [0.4,0.3,0.2,0.1], [0.4,0.3,0.2,0.1]),
    ("Partial overlap", [0.5,0.4,0.1,0.0], [0.0,0.3,0.4,0.3]),
    ("Disjoint       ", [0.6,0.4,0.0,0.0], [0.0,0.0,0.7,0.3]),
]

print(f"{'Case':<18} {'KL(P‖Q)':>12} {'KL(Q‖P)':>12} {'JSD':>10}")
print("-" * 56)
for name, p, q in cases:
    kl_fwd = kl_safe(p, q)
    kl_rev = kl_safe(q, p)
    j = jsd(p, q) / np.log(2)  # convert to bits
    kl_fwd_s = f"{kl_fwd:.4f}" if kl_fwd != float('inf') else "    inf"
    kl_rev_s = f"{kl_rev:.4f}" if kl_rev != float('inf') else "    inf"
    print(f"{name:<18} {kl_fwd_s:>12} {kl_rev_s:>12} {j:>10.4f}")
```

## GAN Training Minimizes JSD

Goodfellow et al. (2014) showed that the original GAN minimax game — with an optimal discriminator — is equivalent to minimizing JSD(P_real ‖ P_gen) + log 4 (a constant). The generator minimizes JSD between the real data distribution and the generated distribution. This theoretical insight illuminated why GANs work, but also revealed a fundamental flaw: when P_real and P_gen have disjoint supports (common early in training), JSD = log 2 = constant, and the generator receives zero gradient.

> **Disjoint Supports = Zero GAN Gradient**: When the real and generated distributions don't overlap (e.g., real images lie on a low-dimensional manifold far from early generator outputs), JSD reaches its maximum of log 2 nats and its gradient with respect to the generator is zero. Training stalls. This is why GAN training is notoriously unstable at the beginning and why Wasserstein GAN (WGAN) was developed as a fix.

```python
import numpy as np
from scipy.stats import entropy as scipy_entropy
import matplotlib.pyplot as plt

def jsd_bits(p, q):
    p = np.asarray(p, dtype=float) / np.sum(p)
    q = np.asarray(q, dtype=float) / np.sum(q)
    m = 0.5 * (p + q)
    return (0.5 * scipy_entropy(p, m) + 0.5 * scipy_entropy(q, m)) / np.log(2)

def kl_bits_safe(p, q):
    p = np.asarray(p, dtype=float) / np.sum(p)
    q = np.asarray(q, dtype=float) / np.sum(q)
    mask = p > 0
    if np.any(q[mask] == 0):
        return float('inf')
    return scipy_entropy(p, q) / np.log(2)

# Simulate GAN training: generated distribution gradually shifts toward real
x = np.arange(20)  # discrete space
p_real = np.zeros(20); p_real[14:18] = [0.2, 0.4, 0.3, 0.1]  # real: modes at 14-17

jsd_vals, kl_vals = [], []
shifts = np.linspace(0, 14, 50)  # generator shifts from left to right

for shift in shifts:
    center = int(shift)
    p_gen = np.zeros(20)
    for i, w in zip([center, center+1, center+2], [0.3, 0.5, 0.2]):
        if 0 <= i < 20:
            p_gen[i] += w
    p_gen = p_gen / p_gen.sum()
    jsd_vals.append(jsd_bits(p_real, p_gen))
    kl_vals.append(kl_bits_safe(p_real, p_gen))

plt.figure(figsize=(8,4))
plt.plot(shifts, jsd_vals, label='JSD (bits)', color='steelblue')
plt.plot(shifts, [min(v, 5) for v in kl_vals], label='KL(P_real‖P_gen) [clipped]', color='tomato', linestyle='--')
plt.axhline(1.0, color='gray', linestyle=':', alpha=0.5, label='JSD max = 1 bit')
plt.xlabel('Generator mean shift toward real data')
plt.ylabel('Divergence (bits)'); plt.title('JSD vs KL During GAN Training Simulation')
plt.legend(); plt.tight_layout(); plt.savefig('gan_jsd.png', dpi=150)
print(f"JSD at full overlap (disjoint→overlap): {jsd_vals[0]:.3f} → {jsd_vals[-1]:.3f} bits")
```

## Dataset Similarity Measurement with JSD

JSD provides a principled way to measure how similar two datasets are, without requiring their supports to match. Given empirical distributions P_A and P_B (e.g., token frequency distributions, label distributions, feature histograms), JSD(P_A, P_B) ∈ [0, 1 bit] quantifies divergence. √JSD ∈ [0, 1] is a true metric. This is used for dataset shift detection, domain adaptation evaluation, and NLP corpus comparison.

```python
import numpy as np
from scipy.stats import entropy as scipy_entropy
from collections import Counter

def jsd_bits(p, q):
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    # Align supports
    assert len(p) == len(q)
    p = p / p.sum(); q = q / q.sum()
    m = 0.5 * (p + q)
    return (0.5 * scipy_entropy(p, m) + 0.5 * scipy_entropy(q, m)) / np.log(2)

def text_distribution(text, vocab_size=26):
    """Letter frequency distribution over a-z."""
    counts = np.zeros(vocab_size)
    for c in text.lower():
        if 'a' <= c <= 'z':
            counts[ord(c) - ord('a')] += 1
    return counts / counts.sum() if counts.sum() > 0 else counts

# Compare letter distributions of different text domains
corpus = {
    "English prose": "the quick brown fox jumps over the lazy dog and the cat sat on the mat",
    "Scientific text": "quantum entanglement entropy eigenvalue matrix probability distribution",
    "German text":   "die schnelle braune fuchs springt ueber den faulen hund und die katze",
    "Random letters": "zqxvwkjzqxvwkjzqxvwkjzqxvwkjzqxvwkjzqxvwkj",
}

dists = {name: text_distribution(text) for name, text in corpus.items()}
names = list(dists.keys())

print("JSD (bits) between text corpora:")
print(f"{'':25}", end="")
for n in names: print(f"{n[:15]:>17}", end="")
print()
for n1 in names:
    print(f"{n1[:25]:<25}", end="")
    for n2 in names:
        j = jsd_bits(dists[n1], dists[n2])
        print(f"{j:>17.4f}", end="")
    print()
```

| Measure | Symmetric | Bounded | Triangle Ineq. | Gradient w/ Disjoint Supports | Typical Use |
| --- | --- | --- | --- | --- | --- |
| KL(P‖Q) | No | No (0 to ∞) | No | Undefined (+∞) | MLE, cross-entropy, ELBO |
| JSD(P,Q) | Yes | Yes (0 to 1 bit) | No (JSD itself) | Zero (constant = log 2) | GAN original, dataset comparison |
| √JSD(P,Q) | Yes | Yes (0 to 1) | Yes (proper metric) | Zero | Dataset distance metric |
| Wasserstein W₁ | Yes | No (0 to ∞) | Yes | Non-zero, informative | WGAN, optimal transport |
| MMD | Yes | No (0 to ∞) | Yes | Non-zero (kernel-based) | Two-sample tests, generative models |

## Wasserstein Distance as the Fix

Arjovsky et al. (2017) proposed Wasserstein GAN to solve the zero-gradient problem. The Wasserstein-1 distance W₁(P,Q) = inf_{γ∈Π(P,Q)} E_{(x,y)~γ}[‖x-y‖] is finite and has non-zero gradients even when P and Q have disjoint supports, because it measures the cost of 'transporting' mass from one distribution to another. WGAN trains a Lipschitz-constrained critic to estimate W₁ instead of a probability-estimating discriminator.

> **When to Use JSD vs KL vs Wasserstein**: Use KL when comparing distributions with overlapping support for MLE or variational inference. Use JSD when you need a symmetric, bounded measure (dataset similarity, evaluation). Use Wasserstein when distributions may be disjoint and you need meaningful gradients (GAN training, optimal transport).

## Summary

- JSD(P,Q) = H((P+Q)/2) - (1/2)H(P) - (1/2)H(Q): excess entropy of the mixture
- Symmetric: JSD(P,Q) = JSD(Q,P) always
- Bounded: 0 ≤ JSD ≤ log 2 nats (= 1 bit with log base 2)
- Always finite: even for disjoint supports (JSD = 1 bit maximum)
- √JSD is a proper metric satisfying the triangle inequality
- Original GAN minimizes JSD — gradient is zero for disjoint supports
- WGAN fixes this by replacing JSD/KL with Wasserstein distance
- Practical uses: dataset shift detection, domain comparison, NLP corpus analysis

---

Jensen-Shannon divergence bridges pure information theory and modern deep learning. Its role in the GAN objective motivated the development of optimal transport methods for generative models, and its metric properties (via √JSD) make it the principled choice for measuring distributional similarity in practice. Understanding JSD clarifies not just GANs but the broader landscape of divergence measures used throughout machine learning.

