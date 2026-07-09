---
title: "Temporal Train/Val/Test Split — No Random Shuffling"
slug: "temporal-train-val-test-split"
description: "Learn why random shuffling destroys time-series structure, implement correct chronological splits, handle gaps to prevent feature leakage, and apply Lopez de Prado purging and embargo for financial panel data."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNhcmRpbmFsIHJ1bGUgZm9yIHRpbWUtc2VyaWVzIG1vZGVsbGluZyBpcyBuZXZlciBzaHVmZmxlIHRoZSBkYXRhIGJlZm9yZSBzcGxpdHRpbmcuIFJhbmRvbSBzaHVmZmxpbmcgYnJlYWtzIHRlbXBvcmFsIG9yZGVyaW5nLCBhbGxvd2luZyBmdXR1cmUgb2JzZXJ2YXRpb25zIGludG8gdGhlIHRyYWluaW5nIHNldCAobGVha2FnZSkgYW5kIGJyZWFraW5nIGF1dG9jb3JyZWxhdGlvbiBzdHJ1Y3R1cmUgdGhhdCB0aGUgbW9kZWwgc2hvdWxkIGxlYXJuLiBUaGUgY29ycmVjdCBhcHByb2FjaCBpcyBhIGNocm9ub2xvZ2ljYWwgc3BsaXQ6IHRyYWluIG9uIHRoZSBlYXJsaWVzdCBzZWdtZW50LCB2YWxpZGF0ZSBvbiB0aGUgbmV4dCBzZWdtZW50LCBhbmQgdGVzdCBvbiB0aGUgaGVsZC1vdXQgZmluYWwgc2VnbWVudCDigJQgd2l0aCBubyBvdmVybGFwIGFuZCwgd2hlcmUgbmVlZGVkLCBhIGdhcCBiZXR3ZWVuIHNlZ21lbnRzIHRvIHByZXZlbnQgZmVhdHVyZSBjb250YW1pbmF0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVHJhaW4g4oaSIFZhbGlkYXRpb24g4oaSIFRlc3Q6IGFsd2F5cyBpbiBjaHJvbm9sb2dpY2FsIG9yZGVyLCBuZXZlciBzaHVmZmxlZC4iLCJUZXN0IHNldDogbGFzdCAxNeKAkzIwJSBvZiBvYnNlcnZhdGlvbnMgKG9yIGxhc3QgMsOXIHNlYXNvbmFsIHBlcmlvZCBtLCB3aGljaGV2ZXIgaXMgbGFyZ2VyKS4iLCJWYWxpZGF0aW9uIHNldDogaW1tZWRpYXRlbHkgYmVmb3JlIHRlc3Qgc2V0OyB1c2VkIG9ubHkgZm9yIGh5cGVycGFyYW1ldGVyIHR1bmluZy4iLCJHYXA6IGluc2VydCBnIOKJpSBtYXggcm9sbGluZyB3aW5kb3cgbGVuZ3RoIG9ic2VydmF0aW9ucyBiZXR3ZWVuIGVhY2ggcGFpciBvZiBzZWdtZW50cy4iLCJQYW5lbCBkYXRhOiBhcHBseSB0aGUgc2FtZSB0ZW1wb3JhbCBjdXRvZmYgdG8gYWxsIHNlcmllcyDigJQgbmV2ZXIgc3BsaXQgZGlmZmVyZW50IHNlcmllcyBhdCBkaWZmZXJlbnQgdGltZSBwb2ludHMuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBSYW5kb20gU2h1ZmZsZSBGYWlscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSWYgYSB0aW1lIHNlcmllcyBpcyBhdXRvY29ycmVsYXRlZCBhdCBsYWcgMSB3aXRoIM+B4oKBID0gMC45IGFuZCB5b3UgcmFuZG9tbHkgc2h1ZmZsZSByb3dzLCBvYnNlcnZhdGlvbnMgaW4gdGhlIHRlc3QgZm9sZCBpbmNsdWRlIHZhbHVlcyBmcm9tIHRocm91Z2hvdXQgdGhlIHNlcmllcy4gVGhlIHRyYWluaW5nIHNldCB0aGVuIGNvbnRhaW5zIG9ic2VydmF0aW9ucyBmcm9tIHQrMSwgdCsyLCAuLi4gZm9yIGFueSB0ZXN0IHBvaW50IHQuIFR3byBwcm9ibGVtcyBhcmlzZTogKDEpIGZ1dHVyZSBsZWFrYWdlIOKAlCB0aGUgbW9kZWwgdHJhaW5zIG9uIGRhdGEgaXQgd291bGQgbm90IGhhdmUgYXZhaWxhYmxlIGF0IHByZWRpY3Rpb24gdGltZTsgKDIpIGF1dG9jb3JyZWxhdGlvbiBpbmZsYXRpb24g4oCUIHRyYWluaW5nIHBvaW50cyBhZGphY2VudCBpbiB0aW1lIHRvIGEgdGVzdCBwb2ludCBhcmUgbmVhcmx5IGlkZW50aWNhbCB0byBpdCwgcHJvZHVjaW5nIHVucmVhbGlzdGljYWxseSBnb29kIGNyb3NzLXZhbGlkYXRpb24gc2NvcmVzLiBUaGUgcmVwb3J0ZWQgQ1YgUk1TRSBjYW4gYmUgMzDigJM1MCUgbG93ZXIgdGhhbiB0cnVlIG91dC1vZi1zYW1wbGUgUk1TRS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBSaWRnZVxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgS0ZvbGQsIFRpbWVTZXJpZXNTcGxpdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IG1lYW5fc3F1YXJlZF9lcnJvclxuXG5ucC5yYW5kb20uc2VlZCg0MilcblQgPSAzMDBcbnkgPSBucC56ZXJvcyhUKVxuZm9yIHQgaW4gcmFuZ2UoMSwgVCk6ICAgICAgICAgICAgIyBBUigxKSB3aXRoIHJobz0wLjlcbiAgICB5W3RdID0gMC45ICogeVt0LTFdICsgbnAucmFuZG9tLnJhbmRuKClcblxubGFncyA9IDVcblggPSBucC5jb2x1bW5fc3RhY2soW25wLnJvbGwoeSwgaykgZm9yIGsgaW4gcmFuZ2UoMSwgbGFncyArIDEpXSlbbGFnczpdXG55X2EgPSB5W2xhZ3M6XVxuXG4jIFdyb25nOiByYW5kb20gay1mb2xkXG5rZl9zY29yZXMgPSBbXVxuZm9yIHRyLCB0ZSBpbiBLRm9sZChuX3NwbGl0cz01LCBzaHVmZmxlPVRydWUsIHJhbmRvbV9zdGF0ZT0wKS5zcGxpdChYKTpcbiAgICBtID0gUmlkZ2UoKS5maXQoWFt0cl0sIHlfYVt0cl0pXG4gICAga2Zfc2NvcmVzLmFwcGVuZChucC5zcXJ0KG1lYW5fc3F1YXJlZF9lcnJvcih5X2FbdGVdLCBtLnByZWRpY3QoWFt0ZV0pKSkpXG5cbiMgQ29ycmVjdDogVGltZVNlcmllc1NwbGl0XG50c19zY29yZXMgPSBbXVxuZm9yIHRyLCB0ZSBpbiBUaW1lU2VyaWVzU3BsaXQobl9zcGxpdHM9NSkuc3BsaXQoWCk6XG4gICAgbSA9IFJpZGdlKCkuZml0KFhbdHJdLCB5X2FbdHJdKVxuICAgIHRzX3Njb3Jlcy5hcHBlbmQobnAuc3FydChtZWFuX3NxdWFyZWRfZXJyb3IoeV9hW3RlXSwgbS5wcmVkaWN0KFhbdGVdKSkpKVxuXG5wcmludChmXHUwMDI3UmFuZG9tIGstZm9sZCBSTVNFIDoge25wLm1lYW4oa2Zfc2NvcmVzKTouNGZ9ICAob3B0aW1pc3RpY2FsbHkgYmlhc2VkKVx1MDAyNylcbnByaW50KGZcdTAwMjdUaW1lU2VyaWVzU3BsaXQgUk1TRToge25wLm1lYW4odHNfc2NvcmVzKTouNGZ9ICAodW5iaWFzZWQpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvcnJlY3QgQ2hyb25vbG9naWNhbCBTcGxpdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNocm9ub2xvZ2ljYWwgc3BsaXQgZGl2aWRlcyB0aGUgc2VyaWVzIGluIHRlbXBvcmFsIG9yZGVyOiB0cmFpbiBbMCwgdOKCgSksIHZhbGlkYXRpb24gW3TigoEsIHTigoIpLCB0ZXN0IFt04oKCLCBUKS4gU3RhbmRhcmQgcHJvcG9ydGlvbnM6IGxhc3QgMTXigJMyMCUgb2YgdGhlIHNlcmllcyBmb3IgdGVzdCwgbGFzdCAxMOKAkzE1JSBiZWZvcmUgdGVzdCBmb3IgdmFsaWRhdGlvbiwgcmVtYWluZGVyIGZvciB0cmFpbmluZy4gVGhlIHZhbGlkYXRpb24gc2V0IGlzIHVzZWQgdG8gdHVuZSBoeXBlcnBhcmFtZXRlcnMgYW5kIGVhcmx5LXN0b3A7IHRoZSB0ZXN0IHNldCBpcyB0b3VjaGVkIGV4YWN0bHkgb25jZSBmb3IgZmluYWwgcmVwb3J0aW5nLiBGb3Igc2Vhc29uYWwgc2VyaWVzLCBlbnN1cmUgZWFjaCBzcGxpdCBjb250YWlucyBhdCBsZWFzdCBvbmUgZnVsbCBzZWFzb25hbCBjeWNsZSDigJQgYSB0ZXN0IHNldCBzaG9ydGVyIHRoYW4gdGhlIHNlYXNvbmFsIHBlcmlvZCBtIGNhbm5vdCBhc3Nlc3Mgc2Vhc29uYWwgYWNjdXJhY3kuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHBhbmRhcyBhcyBwZFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUmlkZ2VcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBtZWFuX2Fic29sdXRlX2Vycm9yXG5cbm5wLnJhbmRvbS5zZWVkKDApXG5UID0gNTAwXG50ID0gbnAuYXJhbmdlKFQpXG55ID0gNTAgKyAwLjEgKiB0ICsgMTAgKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDUyKSArIG5wLnJhbmRvbS5yYW5kbihUKSAqIDNcbmRhdGVzID0gcGQuZGF0ZV9yYW5nZShcdTAwMjcyMDE1LTAxLTAxXHUwMDI3LCBwZXJpb2RzPVQsIGZyZXE9XHUwMDI3V1x1MDAyNylcbmRmID0gcGQuRGF0YUZyYW1lKHtcdTAwMjdkYXRlXHUwMDI3OiBkYXRlcywgXHUwMDI3eVx1MDAyNzogeX0pLnNldF9pbmRleChcdTAwMjdkYXRlXHUwMDI3KVxuXG4jIENocm9ub2xvZ2ljYWwgc3BsaXQ6IDcwIC8gMTUgLyAxNVxubl90ZXN0ID0gaW50KDAuMTUgKiBUKVxubl92YWwgID0gaW50KDAuMTUgKiBUKVxubl90cmFpbiA9IFQgLSBuX3ZhbCAtIG5fdGVzdFxuXG50cmFpbl9kZiA9IGRmLmlsb2NbOm5fdHJhaW5dXG52YWxfZGYgICA9IGRmLmlsb2Nbbl90cmFpbjpuX3RyYWluICsgbl92YWxdXG50ZXN0X2RmICA9IGRmLmlsb2Nbbl90cmFpbiArIG5fdmFsOl1cblxucHJpbnQoZlx1MDAyN1RyYWluOiB7dHJhaW5fZGYuaW5kZXhbMF0uZGF0ZSgpfSB0byB7dHJhaW5fZGYuaW5kZXhbLTFdLmRhdGUoKX0gICh7bGVuKHRyYWluX2RmKX0gb2JzKVx1MDAyNylcbnByaW50KGZcdTAwMjdWYWw6ICAge3ZhbF9kZi5pbmRleFswXS5kYXRlKCl9IHRvIHt2YWxfZGYuaW5kZXhbLTFdLmRhdGUoKX0gICh7bGVuKHZhbF9kZil9IG9icylcdTAwMjcpXG5wcmludChmXHUwMDI3VGVzdDogIHt0ZXN0X2RmLmluZGV4WzBdLmRhdGUoKX0gdG8ge3Rlc3RfZGYuaW5kZXhbLTFdLmRhdGUoKX0gICh7bGVuKHRlc3RfZGYpfSBvYnMpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdhcCBCZXR3ZWVuIFNwbGl0cyB0byBQcmV2ZW50IExlYWthZ2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJvbGxpbmcgZmVhdHVyZXMgY29tcHV0ZWQgb24gb2JzZXJ2YXRpb24gdCBpbmNsdWRlIG9ic2VydmF0aW9ucyB0LXcrMSB0aHJvdWdoIHQuIElmIHRoZSBsYXN0IHRyYWluaW5nIHBvaW50IGlzIHTigoEgYW5kIHRoZSBmaXJzdCB2YWxpZGF0aW9uIHBvaW50IGlzIHTigoErMSwgdGhlIHZhbGlkYXRpb24gZmVhdHVyZXMgZm9yIHTigoErMSB1c2Ugb2JzZXJ2YXRpb25zIHVwIHRvIHTigoEg4oCUIG5vIGxlYWthZ2UuIEhvd2V2ZXIsIGlmIHJvbGxpbmcgZmVhdHVyZXMgaGF2ZSBhIGxhcmdlIHdpbmRvdyB3IGFuZCB0aGUgbW9kZWwgdXNlcyB0aGVzZSBmZWF0dXJlcyBhdCBwcmVkaWN0aW9uIHRpbWUsIGluc2VydGluZyBhIGdhcCBvZiBnIOKJpSB3LTEgb2JzZXJ2YXRpb25zIGJldHdlZW4gdHJhaW4gZW5kIGFuZCB2YWwgc3RhcnQgZW5zdXJlcyB0aGUgdmFsaWRhdGlvbiBmZWF0dXJlcyBhcmUgY29tcHV0ZWQgZW50aXJlbHkgZnJvbSBwcmUtdHJhaW5pbmctY3V0b2ZmIGRhdGEuIFRoaXMgbWF0dGVycyBtb3N0IGZvciBtb2RlbHMgdHJhaW5lZCB3aXRoIGdsb2JhbCByb2xsaW5nIG1lYW5zIG92ZXIgbG9uZyB3aW5kb3dzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlB1cmdpbmcgYW5kIEVtYmFyZ28gZm9yIEZpbmFuY2lhbCBEYXRhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBmaW5hbmNpYWwgTUwgKExvcGV6IGRlIFByYWRvLCBBZHZhbmNlcyBpbiBGaW5hbmNpYWwgTWFjaGluZSBMZWFybmluZyksIGxhYmVscyBvZnRlbiBzcGFuIG11bHRpcGxlIHRpbWUgc3RlcHMg4oCUIGUuZy4sIGEgdHJpcGxlLWJhcnJpZXIgbGFiZWwgZm9yIHRyYWRlIHQgY292ZXJzIFt04oKR4oKZ4oKc4bWj4bWnLCB04oKR4oKT4bWi4oKcXS4gSWYgdOKCkeKCk+G1ouKCnCBvZiBhIHRyYWluaW5nIHNhbXBsZSBmYWxscyBhZnRlciB0aGUgdGVzdCBvYnNlcnZhdGlvbiBlbnRyeSB0aW1lLCBpbmZvcm1hdGlvbiBmcm9tIHRoZSB0ZXN0IHBlcmlvZCBjb250YW1pbmF0ZXMgdHJhaW5pbmcuIFB1cmdpbmcgcmVtb3ZlcyB0cmFpbmluZyBzYW1wbGVzIHdob3NlIGxhYmVsIHNwYW5zIG92ZXJsYXAgd2l0aCBhbnkgdGVzdCBwZXJpb2QuIEVtYmFyZ28gYWRkcyBhIGJ1ZmZlciBvZiBFIGJhcnMgYWZ0ZXIgZWFjaCB0ZXN0IGJsb2NrIHRvIGVsaW1pbmF0ZSByZXNpZHVhbCBhdXRvY29ycmVsYXRpb24gbGVha2FnZSwgcHJldmVudGluZyB0aGUgbW9kZWwgZnJvbSBsZWFybmluZyBwYXR0ZXJucyB0aGF0IGJyaWRnZSB0aGUgdHJhaW4vdGVzdCBib3VuZGFyeSB0aHJvdWdoIG92ZXJsYXBwaW5nIHdpbmRvd3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHBhbmRhcyBhcyBwZFxuXG5kZWYgcHVyZ2VfYW5kX2VtYmFyZ28odHJhaW5faWR4LCB0ZXN0X2lkeCwgbGFiZWxfZW5kX3RpbWVzLCBlbWJhcmdvX3BlcmlvZHM9NSk6XG4gICAgXCJcIlwiXG4gICAgUmVtb3ZlIHRyYWluaW5nIHNhbXBsZXMgd2hvc2UgbGFiZWwgZW5kIHRpbWUgb3ZlcmxhcHMgd2l0aCB0aGUgdGVzdCBwZXJpb2QsXG4gICAgdGhlbiBhZGQgYW4gZW1iYXJnbyBidWZmZXIgYWZ0ZXIgdGhlIHRlc3QgYmxvY2suXG4gICAgdHJhaW5faWR4LCB0ZXN0X2lkeDogYXJyYXktbGlrZSBpbnRlZ2VyIGluZGljZXNcbiAgICBsYWJlbF9lbmRfdGltZXM6IGFycmF5IG9mIGxhYmVsIGVuZCB0aW1lcyAoc2FtZSBpbmRleCBzcGFjZSBhcyBzZXJpZXMpXG4gICAgXCJcIlwiXG4gICAgdGVzdF9zdGFydCA9IHRlc3RfaWR4Lm1pbigpXG4gICAgdGVzdF9lbmQgICA9IHRlc3RfaWR4Lm1heCgpXG4gICAgZW1iYXJnb19lbmQgPSB0ZXN0X2VuZCArIGVtYmFyZ29fcGVyaW9kc1xuXG4gICAgIyBQdXJnZTogcmVtb3ZlIHRyYWluIHNhbXBsZXMgd2hvc2UgbGFiZWwgZW5kcyBkdXJpbmcgb3IgYWZ0ZXIgdGVzdCBzdGFydFxuICAgIHB1cmdlZF9tYXNrID0gbnAuYXJyYXkoW1xuICAgICAgICBsYWJlbF9lbmRfdGltZXNbaV0gXHUwMDNjIHRlc3Rfc3RhcnQgZm9yIGkgaW4gdHJhaW5faWR4XG4gICAgXSlcbiAgICBwdXJnZWRfdHJhaW4gPSB0cmFpbl9pZHhbcHVyZ2VkX21hc2tdXG5cbiAgICAjIEVtYmFyZ286IHJlbW92ZSB0cmFpbiBzYW1wbGVzIHRoYXQgZmFsbCBpbiB0aGUgZW1iYXJnbyB3aW5kb3cgYWZ0ZXIgdGVzdFxuICAgIGVtYmFyZ29fbWFzayA9IHB1cmdlZF90cmFpbiBcdTAwM2M9IGVtYmFyZ29fZW5kXG4gICAgZmluYWxfdHJhaW4gID0gcHVyZ2VkX3RyYWluW35lbWJhcmdvX21hc2sgfCAocHVyZ2VkX3RyYWluIFx1MDAzYyB0ZXN0X3N0YXJ0KV1cbiAgICByZXR1cm4gZmluYWxfdHJhaW5cblxubnAucmFuZG9tLnNlZWQoNDIpXG5UID0gMjAwXG5sYWJlbF9lbmQgPSBucC5hcmFuZ2UoVCkgKyBucC5yYW5kb20ucmFuZGludCgxLCAxMCwgVCkgICMgbGFiZWxzIGVuZCAxLTkgYmFycyBsYXRlclxudHJhaW5faWR4ID0gbnAuYXJhbmdlKDAsIDE1MClcbnRlc3RfaWR4ICA9IG5wLmFyYW5nZSgxNTAsIDE4MClcbmZpbmFsX3RyYWluID0gcHVyZ2VfYW5kX2VtYmFyZ28odHJhaW5faWR4LCB0ZXN0X2lkeCwgbGFiZWxfZW5kLCBlbWJhcmdvX3BlcmlvZHM9NSlcbnByaW50KGZcdTAwMjdPcmlnaW5hbCB0cmFpbiBzaXplIDoge2xlbih0cmFpbl9pZHgpfVx1MDAyNylcbnByaW50KGZcdTAwMjdBZnRlciBwdXJnZStlbWJhcmdvIDoge2xlbihmaW5hbF90cmFpbil9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JlbW92ZWQ6IHtsZW4odHJhaW5faWR4KSAtIGxlbihmaW5hbF90cmFpbil9IHNhbXBsZXNcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlNlYXNvbmFsIFRlc3QgU2V0IExlbmd0aCIsImNvbnRlbnQiOiJFbnN1cmUgdGhlIHRlc3Qgc2V0IGNvbnRhaW5zIGF0IGxlYXN0IG9uZSBmdWxsIHNlYXNvbmFsIGN5Y2xlIChtIHBlcmlvZHMpLiBGb3Igd2Vla2x5IGRhdGEgd2l0aCBhbm51YWwgc2Vhc29uYWxpdHkgKG09NTIpLCBhIHRlc3Qgc2V0IHNob3J0ZXIgdGhhbiA1MiB3ZWVrcyBjYW5ub3QgbWVhc3VyZSBzZWFzb25hbCBhY2N1cmFjeS4gQSBjb21tb24gcnVsZTogdGVzdCA9IG1heCgyMCUgb2YgdG90YWwsIDLCt20pIGFuZCB2YWxpZGF0ZSA9IG1heCgxNSUgb2YgdG90YWwsIG0pLCB3aXRoIHRoZSByZW1haW5kZXIgZm9yIHRyYWluaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik11bHRpLVNlcmllcyBEYXRhc2V0IFNwbGl0dGluZyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBwYW5kYXMgYXMgcGRcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgbWVhbl9hYnNvbHV0ZV9lcnJvclxuXG5ucC5yYW5kb20uc2VlZCgxKVxubl9zZXJpZXMgPSAyMFxuVCA9IDIwMFxuYWxsX3NlcmllcyA9IFtdXG5mb3IgaSBpbiByYW5nZShuX3Nlcmllcyk6XG4gICAgdCA9IG5wLmFyYW5nZShUKVxuICAgIHkgPSBucC5yYW5kb20udW5pZm9ybSgyMCwgODApICsgMC4xICogdCArIDggKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDEyICsgbnAucmFuZG9tLnJhbmQoKSlcbiAgICB5ICs9IG5wLnJhbmRvbS5yYW5kbihUKSAqIDNcbiAgICBkZiA9IHBkLkRhdGFGcmFtZSh7XHUwMDI3c2VyaWVzX2lkXHUwMDI3OiBpLCBcdTAwMjd0aW1lXHUwMDI3OiB0LCBcdTAwMjd5XHUwMDI3OiB5fSlcbiAgICBhbGxfc2VyaWVzLmFwcGVuZChkZilcblxucGFuZWwgPSBwZC5jb25jYXQoYWxsX3NlcmllcywgaWdub3JlX2luZGV4PVRydWUpXG5cbiMgR2xvYmFsIHRlbXBvcmFsIHNwbGl0OiBsYXN0IDIwJSBvZiB0aW1lIHN0ZXBzIOKGkiB0ZXN0XG5zcGxpdF90ID0gaW50KDAuOCAqIFQpXG50cmFpbl9wYW5lbCA9IHBhbmVsW3BhbmVsW1x1MDAyN3RpbWVcdTAwMjddIFx1MDAzYyAgc3BsaXRfdF1cbnRlc3RfcGFuZWwgID0gcGFuZWxbcGFuZWxbXHUwMDI3dGltZVx1MDAyN10gXHUwMDNlPSBzcGxpdF90XVxuXG4jIExhZyBmZWF0dXJlcyBwZXIgc2VyaWVzXG5kZWYgbWFrZV9sYWdzKGRmLCBsYWdzPTMpOlxuICAgIGRmID0gZGYuc29ydF92YWx1ZXMoXHUwMDI3dGltZVx1MDAyNykuY29weSgpXG4gICAgZm9yIGsgaW4gcmFuZ2UoMSwgbGFncyArIDEpOlxuICAgICAgICBkZltmXHUwMDI3bGFnX3trfVx1MDAyN10gPSBkZltcdTAwMjd5XHUwMDI3XS5zaGlmdChrKVxuICAgIHJldHVybiBkZi5kcm9wbmEoKVxuXG50cmFpbl9mZWF0ID0gdHJhaW5fcGFuZWwuZ3JvdXBieShcdTAwMjdzZXJpZXNfaWRcdTAwMjcsIGdyb3VwX2tleXM9RmFsc2UpLmFwcGx5KG1ha2VfbGFncylcbnRlc3RfZmVhdCAgPSB0ZXN0X3BhbmVsLmdyb3VwYnkoXHUwMDI3c2VyaWVzX2lkXHUwMDI3LCBncm91cF9rZXlzPUZhbHNlKS5hcHBseShtYWtlX2xhZ3MpXG5cbmZlYXRfY29scyA9IFtjIGZvciBjIGluIHRyYWluX2ZlYXQuY29sdW1ucyBpZiBjLnN0YXJ0c3dpdGgoXHUwMDI3bGFnXHUwMDI3KV1cbm1vZGVsID0gUmlkZ2UoKS5maXQodHJhaW5fZmVhdFtmZWF0X2NvbHNdLCB0cmFpbl9mZWF0W1x1MDAyN3lcdTAwMjddKVxucHJlZCAgPSBtb2RlbC5wcmVkaWN0KHRlc3RfZmVhdFtmZWF0X2NvbHNdKVxucHJpbnQoZlx1MDAyN1BhbmVsIHRlc3QgTUFFOiB7bWVhbl9hYnNvbHV0ZV9lcnJvcih0ZXN0X2ZlYXRbXCJ5XCJdLCBwcmVkKTouM2Z9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwbGl0IFN0cmF0ZWd5IFJlZmVyZW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJTdHJhdGVneSIsIlRyYWluIFNpemUiLCJUZXN0IFdpbmRvdyIsIkxlYWthZ2UiLCJDb21wdXRlIiwiTm90ZXMiXSwicm93cyI6W1siU2luZ2xlIGhvbGRvdXQgKGNocm9ub2xvZ2ljYWwpIiwiRml4ZWQgZWFybHkgcG9ydGlvbiIsIkZpeGVkIGZpbmFsIHBvcnRpb24iLCJOb25lIiwiVmVyeSBsb3ciLCJIaWdoIHZhcmlhbmNlIGVzdGltYXRlOyB1c2UgZm9yIHZlcnkgbGFyZ2UgbiJdLFsiRXhwYW5kaW5nIHdhbGstZm9yd2FyZCIsIkdyb3dzIGVhY2ggZm9sZCIsIkZpeGVkIGhvcml6b24gSCIsIk5vbmUiLCJNZWRpdW0iLCJQcmVmZXJyZWQgZm9yIHN0YXRpb25hcnkgc2VyaWVzIl0sWyJSb2xsaW5nIHdhbGstZm9yd2FyZCIsIkZpeGVkIHdpbmRvdyBXIiwiRml4ZWQgaG9yaXpvbiBIIiwiTm9uZSIsIk1lZGl1bSIsIlByZWZlcnJlZCBmb3Igbm9uLXN0YXRpb25hcnkgLyByZWdpbWUgY2hhbmdlIl0sWyJBbmNob3JlZCB3YWxrLWZvcndhcmQiLCJGaXhlZCBzdGFydCwgZ3Jvd3MiLCJGaXhlZCBob3Jpem9uIEgiLCJOb25lIiwiTWVkaXVtIiwiU2FtZSBhcyBleHBhbmRpbmcgd2luZG93Il0sWyJQdXJnZSArIGVtYmFyZ28gKGZpbmFuY2lhbCkiLCJWYXJpZXMgYnkgbGFiZWwgc3BhbiIsIkZpeGVkIGhvcml6b24gSCIsIk5vbmUiLCJNZWRpdW0taGlnaCIsIlJlcXVpcmVkIGZvciBvdmVybGFwcGluZyBmaW5hbmNpYWwgbGFiZWxzIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIk5ldmVyIHVzZSByYW5kb20gc2h1ZmZsaW5nIG9yIHN0cmF0aWZpY2F0aW9uIGJ5IHRhcmdldCBmb3IgdGltZS1zZXJpZXMgc3BsaXRzLiIsIkZvciBwYW5lbCBkYXRhIChtdWx0aXBsZSBzZXJpZXMpLCBhcHBseSB0aGUgc2FtZSB0ZW1wb3JhbCBjdXRvZmYgdG8gYWxsIHNlcmllcyB0byBhdm9pZCBjb2xkLXN0YXJ0IGJpYXMuIiwiVGhlIHZhbGlkYXRpb24gc2V0IHNlcnZlcyBvbmx5IGZvciBoeXBlcnBhcmFtZXRlciB0dW5pbmcg4oCUIHJlcG9ydCBmaW5hbCBhY2N1cmFjeSBvbiB0aGUgdGVzdCBzZXQgb25seS4iLCJVc2UgcHVyZ2luZyBhbmQgZW1iYXJnbyB3aGVuZXZlciBsYWJlbCBjb25zdHJ1Y3Rpb24gc3BhbnMgbXVsdGlwbGUgdGltZSBzdGVwcyAoZmluYW5jaWFsIGV2ZW50cywgY3VtdWxhdGl2ZSByZXR1cm5zKS4iLCJXaGVuIHRoZSBzZXJpZXMgaXMgdmVyeSBzaG9ydCAoVCBcdTAwM2MgMTAwKSwgc2luZ2xlIGhvbGRvdXQgbWF5IGJlIG1vcmUgcmVsaWFibGUgdGhhbiB3YWxrLWZvcndhcmQgZHVlIHRvIGhpZ2ggZm9sZC10by1mb2xkIHZhcmlhbmNlLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgY29tbW9uIG1pc3Rha2UgaW4gdGltZS1zZXJpZXMgcHJvamVjdHMgaXMgdG8gbm9ybWFsaXNlIG9yIHN0YW5kYXJkaXNlIHRoZSBlbnRpcmUgZGF0YXNldCBiZWZvcmUgc3BsaXR0aW5nLiBDb21wdXRpbmcgdGhlIG1lYW4gYW5kIHN0YW5kYXJkIGRldmlhdGlvbiBvdmVyIGFsbCBUIG9ic2VydmF0aW9ucyAoaW5jbHVkaW5nIHRoZSB0ZXN0IHNldCkgbGVha3Mgc3VtbWFyeSBzdGF0aXN0aWNzIGZyb20gdGhlIGZ1dHVyZSBpbnRvIHRoZSB0cmFpbmluZyBwaXBlbGluZS4gVGhlIGNvcnJlY3QgYXBwcm9hY2g6IGZpdCB0aGUgc2NhbGVyIG9ubHkgb24gdGhlIHRyYWluaW5nIHNldCwgdGhlbiBhcHBseSB0aGUgc2FtZSB0cmFuc2Zvcm0gdG8gdGhlIHZhbGlkYXRpb24gYW5kIHRlc3Qgc2V0cyDigJQgZXhhY3RseSBhcyB5b3Ugd291bGQgd2l0aCBhIHRhYnVsYXIgZGF0YXNldC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciB2ZXJ5IGxvbmcgc2VyaWVzIChUIOKJpSAxMCwwMDApIHdoZXJlIGEgZml4ZWQgaG9sZG91dCB0ZXN0IHNldCBpcyB1c2VkLCB0aGUgdGVzdCBzZXQgcmVwcmVzZW50YXRpdmVuZXNzIHJpc2sgaW5jcmVhc2VzOiBpZiB0aGUgc2VyaWVzIGhhcyBzdHJ1Y3R1cmFsIGJyZWFrcyAocG9saWN5IGNoYW5nZSwgQ09WSUQtMTkgZGVtYW5kIHNoaWZ0KSwgdGhlIHRlc3QgcGVyaW9kIG1heSBiZSBmdW5kYW1lbnRhbGx5IGRpZmZlcmVudCBmcm9tIHRoZSB0cmFpbmluZyBwZXJpb2QuIFN0cmF0aWZpZWQgdGVtcG9yYWwgaG9sZG91dCDigJQgZW5zdXJpbmcgZWFjaCBzZWFzb24gYW5kIHJlZ2ltZSBhcHBlYXJzIHByb3BvcnRpb25hbGx5IGluIHRyYWluL3Rlc3Qg4oCUIGlzIG9uZSBtaXRpZ2F0aW9uLCBidXQgdGhlIHNhZmVzdCBhcHByb2FjaCBmb3Igbm9uLXN0YXRpb25hcnkgc2VyaWVzIGlzIHdhbGstZm9yd2FyZCBldmFsdWF0aW9uIHdpdGggYSByb2xsaW5nIHdpbmRvdyB0aGF0IHRyYWNrcyByZWNlbnQgYmVoYXZpb3VyLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Temporal Train/Val/Test Split — No Random Shuffling

The cardinal rule for time-series modelling is never shuffle the data before splitting. Random shuffling breaks temporal ordering, allowing future observations into the training set (leakage) and breaking autocorrelation structure that the model should learn. The correct approach is a chronological split: train on the earliest segment, validate on the next segment, and test on the held-out final segment — with no overlap and, where needed, a gap between segments to prevent feature contamination.

- Train → Validation → Test: always in chronological order, never shuffled.
- Test set: last 15–20% of observations (or last 2× seasonal period m, whichever is larger).
- Validation set: immediately before test set; used only for hyperparameter tuning.
- Gap: insert g ≥ max rolling window length observations between each pair of segments.
- Panel data: apply the same temporal cutoff to all series — never split different series at different time points.

## Why Random Shuffle Fails

If a time series is autocorrelated at lag 1 with ρ₁ = 0.9 and you randomly shuffle rows, observations in the test fold include values from throughout the series. The training set then contains observations from t+1, t+2, ... for any test point t. Two problems arise: (1) future leakage — the model trains on data it would not have available at prediction time; (2) autocorrelation inflation — training points adjacent in time to a test point are nearly identical to it, producing unrealistically good cross-validation scores. The reported CV RMSE can be 30–50% lower than true out-of-sample RMSE.

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, TimeSeriesSplit
from sklearn.metrics import mean_squared_error

np.random.seed(42)
T = 300
y = np.zeros(T)
for t in range(1, T):            # AR(1) with rho=0.9
    y[t] = 0.9 * y[t-1] + np.random.randn()

lags = 5
X = np.column_stack([np.roll(y, k) for k in range(1, lags + 1)])[lags:]
y_a = y[lags:]

# Wrong: random k-fold
kf_scores = []
for tr, te in KFold(n_splits=5, shuffle=True, random_state=0).split(X):
    m = Ridge().fit(X[tr], y_a[tr])
    kf_scores.append(np.sqrt(mean_squared_error(y_a[te], m.predict(X[te]))))

# Correct: TimeSeriesSplit
ts_scores = []
for tr, te in TimeSeriesSplit(n_splits=5).split(X):
    m = Ridge().fit(X[tr], y_a[tr])
    ts_scores.append(np.sqrt(mean_squared_error(y_a[te], m.predict(X[te]))))

print(f'Random k-fold RMSE : {np.mean(kf_scores):.4f}  (optimistically biased)')
print(f'TimeSeriesSplit RMSE: {np.mean(ts_scores):.4f}  (unbiased)')
```

## Correct Chronological Split

The chronological split divides the series in temporal order: train [0, t₁), validation [t₁, t₂), test [t₂, T). Standard proportions: last 15–20% of the series for test, last 10–15% before test for validation, remainder for training. The validation set is used to tune hyperparameters and early-stop; the test set is touched exactly once for final reporting. For seasonal series, ensure each split contains at least one full seasonal cycle — a test set shorter than the seasonal period m cannot assess seasonal accuracy.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

np.random.seed(0)
T = 500
t = np.arange(T)
y = 50 + 0.1 * t + 10 * np.sin(2 * np.pi * t / 52) + np.random.randn(T) * 3
dates = pd.date_range('2015-01-01', periods=T, freq='W')
df = pd.DataFrame({'date': dates, 'y': y}).set_index('date')

# Chronological split: 70 / 15 / 15
n_test = int(0.15 * T)
n_val  = int(0.15 * T)
n_train = T - n_val - n_test

train_df = df.iloc[:n_train]
val_df   = df.iloc[n_train:n_train + n_val]
test_df  = df.iloc[n_train + n_val:]

print(f'Train: {train_df.index[0].date()} to {train_df.index[-1].date()}  ({len(train_df)} obs)')
print(f'Val:   {val_df.index[0].date()} to {val_df.index[-1].date()}  ({len(val_df)} obs)')
print(f'Test:  {test_df.index[0].date()} to {test_df.index[-1].date()}  ({len(test_df)} obs)')
```

## Gap Between Splits to Prevent Leakage

Rolling features computed on observation t include observations t-w+1 through t. If the last training point is t₁ and the first validation point is t₁+1, the validation features for t₁+1 use observations up to t₁ — no leakage. However, if rolling features have a large window w and the model uses these features at prediction time, inserting a gap of g ≥ w-1 observations between train end and val start ensures the validation features are computed entirely from pre-training-cutoff data. This matters most for models trained with global rolling means over long windows.

## Purging and Embargo for Financial Data

In financial ML (Lopez de Prado, Advances in Financial Machine Learning), labels often span multiple time steps — e.g., a triple-barrier label for trade t covers [tₑₙₜᵣᵧ, tₑₓᵢₜ]. If tₑₓᵢₜ of a training sample falls after the test observation entry time, information from the test period contaminates training. Purging removes training samples whose label spans overlap with any test period. Embargo adds a buffer of E bars after each test block to eliminate residual autocorrelation leakage, preventing the model from learning patterns that bridge the train/test boundary through overlapping windows.

```python
import numpy as np
import pandas as pd

def purge_and_embargo(train_idx, test_idx, label_end_times, embargo_periods=5):
    """
    Remove training samples whose label end time overlaps with the test period,
    then add an embargo buffer after the test block.
    train_idx, test_idx: array-like integer indices
    label_end_times: array of label end times (same index space as series)
    """
    test_start = test_idx.min()
    test_end   = test_idx.max()
    embargo_end = test_end + embargo_periods

    # Purge: remove train samples whose label ends during or after test start
    purged_mask = np.array([
        label_end_times[i] < test_start for i in train_idx
    ])
    purged_train = train_idx[purged_mask]

    # Embargo: remove train samples that fall in the embargo window after test
    embargo_mask = purged_train <= embargo_end
    final_train  = purged_train[~embargo_mask | (purged_train < test_start)]
    return final_train

np.random.seed(42)
T = 200
label_end = np.arange(T) + np.random.randint(1, 10, T)  # labels end 1-9 bars later
train_idx = np.arange(0, 150)
test_idx  = np.arange(150, 180)
final_train = purge_and_embargo(train_idx, test_idx, label_end, embargo_periods=5)
print(f'Original train size : {len(train_idx)}')
print(f'After purge+embargo : {len(final_train)}')
print(f'Removed: {len(train_idx) - len(final_train)} samples')
```

> **Seasonal Test Set Length**: Ensure the test set contains at least one full seasonal cycle (m periods). For weekly data with annual seasonality (m=52), a test set shorter than 52 weeks cannot measure seasonal accuracy. A common rule: test = max(20% of total, 2·m) and validate = max(15% of total, m), with the remainder for training.

## Multi-Series Dataset Splitting

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

np.random.seed(1)
n_series = 20
T = 200
all_series = []
for i in range(n_series):
    t = np.arange(T)
    y = np.random.uniform(20, 80) + 0.1 * t + 8 * np.sin(2 * np.pi * t / 12 + np.random.rand())
    y += np.random.randn(T) * 3
    df = pd.DataFrame({'series_id': i, 'time': t, 'y': y})
    all_series.append(df)

panel = pd.concat(all_series, ignore_index=True)

# Global temporal split: last 20% of time steps → test
split_t = int(0.8 * T)
train_panel = panel[panel['time'] <  split_t]
test_panel  = panel[panel['time'] >= split_t]

# Lag features per series
def make_lags(df, lags=3):
    df = df.sort_values('time').copy()
    for k in range(1, lags + 1):
        df[f'lag_{k}'] = df['y'].shift(k)
    return df.dropna()

train_feat = train_panel.groupby('series_id', group_keys=False).apply(make_lags)
test_feat  = test_panel.groupby('series_id', group_keys=False).apply(make_lags)

feat_cols = [c for c in train_feat.columns if c.startswith('lag')]
model = Ridge().fit(train_feat[feat_cols], train_feat['y'])
pred  = model.predict(test_feat[feat_cols])
print(f'Panel test MAE: {mean_absolute_error(test_feat["y"], pred):.3f}')
```

## Split Strategy Reference

| Strategy | Train Size | Test Window | Leakage | Compute | Notes |
| --- | --- | --- | --- | --- | --- |
| Single holdout (chronological) | Fixed early portion | Fixed final portion | None | Very low | High variance estimate; use for very large n |
| Expanding walk-forward | Grows each fold | Fixed horizon H | None | Medium | Preferred for stationary series |
| Rolling walk-forward | Fixed window W | Fixed horizon H | None | Medium | Preferred for non-stationary / regime change |
| Anchored walk-forward | Fixed start, grows | Fixed horizon H | None | Medium | Same as expanding window |
| Purge + embargo (financial) | Varies by label span | Fixed horizon H | None | Medium-high | Required for overlapping financial labels |

- Never use random shuffling or stratification by target for time-series splits.
- For panel data (multiple series), apply the same temporal cutoff to all series to avoid cold-start bias.
- The validation set serves only for hyperparameter tuning — report final accuracy on the test set only.
- Use purging and embargo whenever label construction spans multiple time steps (financial events, cumulative returns).
- When the series is very short (T < 100), single holdout may be more reliable than walk-forward due to high fold-to-fold variance.

A common mistake in time-series projects is to normalise or standardise the entire dataset before splitting. Computing the mean and standard deviation over all T observations (including the test set) leaks summary statistics from the future into the training pipeline. The correct approach: fit the scaler only on the training set, then apply the same transform to the validation and test sets — exactly as you would with a tabular dataset.

For very long series (T ≥ 10,000) where a fixed holdout test set is used, the test set representativeness risk increases: if the series has structural breaks (policy change, COVID-19 demand shift), the test period may be fundamentally different from the training period. Stratified temporal holdout — ensuring each season and regime appears proportionally in train/test — is one mitigation, but the safest approach for non-stationary series is walk-forward evaluation with a rolling window that tracks recent behaviour.

---

