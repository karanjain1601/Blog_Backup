---
title: "Structured Pruning — Filter, Channel, and Layer Removal"
slug: "structured-pruning"
description: "Remove entire filters, channels, or layers to produce dense, hardware-acceleratable models. Covers L1-norm and Taylor expansion criteria, attention head pruning, layer pruning, iterative schedules, and reconstruction-based methods like HRank."
tags: ["deep-learning", "model-compression", "pruning", "quantization"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVW5zdHJ1Y3R1cmVkIHBydW5pbmcgc2V0cyBpbmRpdmlkdWFsIHdlaWdodHMgdG8gemVybywgcHJvZHVjaW5nIHNwYXJzZSB3ZWlnaHQgbWF0cmljZXMuIFdpdGhvdXQgc3BlY2lhbGl6ZWQgc3BhcnNlLW1hdHJpeCBoYXJkd2FyZSwgdGhlc2UgemVybyB3ZWlnaHRzIHN0aWxsIGNvbnN1bWUgbWVtb3J5IGFuZCBwYXJ0aWNpcGF0ZSBpbiBtYXRyaXggbXVsdGlwbGljYXRpb25zIOKAlCB5aWVsZGluZyBubyB3YWxsLWNsb2NrIHNwZWVkdXAgb24gYSBzdGFuZGFyZCBHUFUuIFN0cnVjdHVyZWQgcHJ1bmluZyBzb2x2ZXMgdGhpcyBieSByZW1vdmluZyBlbnRpcmUgZmlsdGVycywgY2hhbm5lbHMsIG9yIGxheWVycy4gVGhlIHJlc3VsdGluZyBtb2RlbCBpcyBkZW5zZSBhbmQgc21hbGxlcjsgc3RhbmRhcmQgQkxBUyByb3V0aW5lcyBhbmQgR1BVIHRlbnNvciBjb3JlcyBpbW1lZGlhdGVseSBhY2NlbGVyYXRlIGl0IHdpdGhvdXQgYW55IHNwZWNpYWwgaGFuZGxpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFN0cnVjdHVyZSBNYXR0ZXJzIGZvciBTcGVlZHVwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGNvbnZvbHV0aW9uYWwgbGF5ZXIgd2l0aCAyNTYgb3V0cHV0IGZpbHRlcnMgYW5kIDUwJSB1bnN0cnVjdHVyZWQgc3BhcnNpdHkgc3RpbGwgcGVyZm9ybXMgMjU2IG91dHB1dC1jaGFubmVsIGRvdCBwcm9kdWN0cyDigJQgaGFsZiB0aGUgRkxPUHMgYXJlIHdhc3RlZCBvbiBtdWx0aXBseWluZyBieSB6ZXJvLCBidXQgdGhlIGxvb3AgY291bnQgaXMgdW5jaGFuZ2VkLiBSZW1vdmUgMTI4IGVudGlyZSBmaWx0ZXJzIGFuZCB0aGUgbGF5ZXIgbm93IHBlcmZvcm1zIDEyOCBkb3QgcHJvZHVjdHMgd2l0aCBubyB6ZXJvIGFyaXRobWV0aWMuIFRoaXMgZ2l2ZXMgYSAyw5cgRkxPUCByZWR1Y3Rpb24gdGhhdCB0cmFuc2xhdGVzIGRpcmVjdGx5IHRvIHRocm91Z2hwdXQgb24gYW55IGhhcmR3YXJlLiBTdHJ1Y3R1cmVkIHBydW5pbmcgdGhlcmVmb3JlIHJlZHVjZXMgRkxPUFMsIG5vdCBqdXN0IHBhcmFtZXRlciBjb3VudC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGaWx0ZXIgUHJ1bmluZyB3aXRoIEwxLU5vcm0gQ3JpdGVyaW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBjb252IGxheWVyIHdpdGggd2VpZ2h0IHRlbnNvciBXIOKIiCDihJ1ee0Nfb3V0IMOXIENfaW4gw5cgayDDlyBrfSwgZWFjaCBvdXRwdXQgZmlsdGVyIGkgaGFzIGltcG9ydGFuY2Ugc2NvcmUgc19pID0g4oCWV19p4oCW4oKBIOKAlCB0aGUgc3VtIG9mIGFic29sdXRlIHZhbHVlcyBhY3Jvc3MgYWxsIGVsZW1lbnRzIG9mIHRoYXQgZmlsdGVyLiBGaWx0ZXJzIHdpdGggbG93IEwxLW5vcm0gY29udHJpYnV0ZSBsaXR0bGUgdG8gdGhlIG91dHB1dCBmZWF0dXJlIG1hcC4gQWZ0ZXIgcmFua2luZyBhbGwgZmlsdGVycyBieSBzX2ksIHRoZSBib3R0b20gcCUgYXJlIHJlbW92ZWQuIFRoZSBzdWJzZXF1ZW50IGxheWVyXHUwMDI3cyBpbnB1dCBjaGFubmVscyBtdXN0IGJlIHBydW5lZCBjb3JyZXNwb25kaW5nbHk6IHJlbW92aW5nIGZpbHRlciBpIGZyb20gbGF5ZXIgbCByZW1vdmVzIGlucHV0IGNoYW5uZWwgaSBmcm9tIGxheWVyIGwrMS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIHBydW5lX2NvbnZfbGF5ZXIoY29udjogbm4uQ29udjJkLCBwcnVuZV9yYXRpbzogZmxvYXQpOlxuICAgIFwiXCJcIlBydW5lIGJvdHRvbSBwcnVuZV9yYXRpbyBmaWx0ZXJzIGJ5IEwxIG5vcm0uIFJldHVybnMgbmV3IENvbnYyZC5cIlwiXCJcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgVyA9IGNvbnYud2VpZ2h0LmRhdGEgICMgKENfb3V0LCBDX2luLCBrSCwga1cpXG4gICAgICAgIHNjb3JlcyA9IFcuYWJzKCkuc3VtKGRpbT0oMSwgMiwgMykpICAjIEwxIG5vcm0gcGVyIGZpbHRlclxuICAgICAgICBuX2tlZXAgPSBtYXgoMSwgaW50KFcuc2hhcGVbMF0gKiAoMSAtIHBydW5lX3JhdGlvKSkpXG4gICAgICAgIGtlZXBfaWR4ID0gc2NvcmVzLnRvcGsobl9rZWVwKS5pbmRpY2VzLnNvcnQoKS52YWx1ZXNcblxuICAgICAgICBuZXdfY29udiA9IG5uLkNvbnYyZChcbiAgICAgICAgICAgIGluX2NoYW5uZWxzPVcuc2hhcGVbMV0sXG4gICAgICAgICAgICBvdXRfY2hhbm5lbHM9bl9rZWVwLFxuICAgICAgICAgICAga2VybmVsX3NpemU9Y29udi5rZXJuZWxfc2l6ZSxcbiAgICAgICAgICAgIHN0cmlkZT1jb252LnN0cmlkZSxcbiAgICAgICAgICAgIHBhZGRpbmc9Y29udi5wYWRkaW5nLFxuICAgICAgICAgICAgYmlhcz1jb252LmJpYXMgaXMgbm90IE5vbmUsXG4gICAgICAgIClcbiAgICAgICAgbmV3X2NvbnYud2VpZ2h0LmRhdGEgPSBXW2tlZXBfaWR4XVxuICAgICAgICBpZiBjb252LmJpYXMgaXMgbm90IE5vbmU6XG4gICAgICAgICAgICBuZXdfY29udi5iaWFzLmRhdGEgPSBjb252LmJpYXMuZGF0YVtrZWVwX2lkeF1cbiAgICByZXR1cm4gbmV3X2NvbnYsIGtlZXBfaWR4XG5cbmRlZiBwcnVuZV9ibl9sYXllcihibjogbm4uQmF0Y2hOb3JtMmQsIGtlZXBfaWR4OiB0b3JjaC5UZW5zb3IpOlxuICAgIG5ld19ibiA9IG5uLkJhdGNoTm9ybTJkKGxlbihrZWVwX2lkeCkpXG4gICAgbmV3X2JuLndlaWdodC5kYXRhID0gYm4ud2VpZ2h0LmRhdGFba2VlcF9pZHhdXG4gICAgbmV3X2JuLmJpYXMuZGF0YSA9IGJuLmJpYXMuZGF0YVtrZWVwX2lkeF1cbiAgICBuZXdfYm4ucnVubmluZ19tZWFuID0gYm4ucnVubmluZ19tZWFuW2tlZXBfaWR4XVxuICAgIG5ld19ibi5ydW5uaW5nX3ZhciA9IGJuLnJ1bm5pbmdfdmFyW2tlZXBfaWR4XVxuICAgIHJldHVybiBuZXdfYm5cblxuIyBEZW1vXG5jb252ID0gbm4uQ29udjJkKDY0LCAxMjgsIDMsIHBhZGRpbmc9MSlcbmNvbnZfcHJ1bmVkLCBrZXB0ID0gcHJ1bmVfY29udl9sYXllcihjb252LCBwcnVuZV9yYXRpbz0wLjQpXG5wcmludChmXHUwMDI3T3JpZ2luYWw6IHtjb252LndlaWdodC5zaGFwZX0gIC1cdTAwM2UgUHJ1bmVkOiB7Y29udl9wcnVuZWQud2VpZ2h0LnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdLZXB0IGZpbHRlciBpbmRpY2VzIChmaXJzdCA1KToge2tlcHRbOjVdLnRvbGlzdCgpfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUYXlsb3IgRXhwYW5zaW9uIEltcG9ydGFuY2UgU2NvcmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBMMS1ub3JtIGNyaXRlcmlvbiBpZ25vcmVzIGdyYWRpZW50IGluZm9ybWF0aW9uLiBBIGZpbHRlciB3aXRoIGxhcmdlIHdlaWdodHMgYnV0IHplcm8gZ3JhZGllbnQgY29udHJpYnV0ZXMgbGl0dGxlIHRvIHRoZSBsb3NzLiBUaGUgVGF5bG9yIGV4cGFuc2lvbiBjcml0ZXJpb24gYXBwcm94aW1hdGVzIHRoZSBjaGFuZ2UgaW4gbG9zcyB3aGVuIGZpbHRlciBpIGlzIHJlbW92ZWQ6IM6UTCDiiYggzqNfaiB8Z19qIMK3IHdfanwgd2hlcmUgZ19qID0g4oiCTC/iiIJ3X2ouIFRoaXMgZmlyc3Qtb3JkZXIgYXBwcm94aW1hdGlvbiBpcyBjb21wdXRlZCBpbiBhIHNpbmdsZSBmb3J3YXJkK2JhY2t3YXJkIHBhc3Mgb3ZlciBhIGNhbGlicmF0aW9uIHNldCBhbmQgY2FwdHVyZXMgaG93IHNlbnNpdGl2ZSB0aGUgbG9zcyBpcyB0byBlYWNoIGZpbHRlclx1MDAyN3Mgd2VpZ2h0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IGRlZmF1bHRkaWN0XG5cbmNsYXNzIFRheWxvclBydW5lcjpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbW9kZWw6IG5uLk1vZHVsZSk6XG4gICAgICAgIHNlbGYubW9kZWwgPSBtb2RlbFxuICAgICAgICBzZWxmLnNjb3JlcyA9IGRlZmF1bHRkaWN0KGZsb2F0KVxuICAgICAgICBzZWxmLl9ob29rcyA9IFtdXG4gICAgICAgIHNlbGYuX3JlZ2lzdGVyX2hvb2tzKClcblxuICAgIGRlZiBfcmVnaXN0ZXJfaG9va3Moc2VsZik6XG4gICAgICAgIGZvciBuYW1lLCBtb2R1bGUgaW4gc2VsZi5tb2RlbC5uYW1lZF9tb2R1bGVzKCk6XG4gICAgICAgICAgICBpZiBpc2luc3RhbmNlKG1vZHVsZSwgbm4uQ29udjJkKTpcbiAgICAgICAgICAgICAgICBoID0gbW9kdWxlLndlaWdodC5yZWdpc3Rlcl9ob29rKFxuICAgICAgICAgICAgICAgICAgICBsYW1iZGEgZ3JhZCwgbj1uYW1lLCBtPW1vZHVsZTogc2VsZi5fYWNjdW11bGF0ZShuLCBncmFkLCBtKVxuICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgICAgICBzZWxmLl9ob29rcy5hcHBlbmQoaClcblxuICAgIGRlZiBfYWNjdW11bGF0ZShzZWxmLCBuYW1lLCBncmFkLCBtb2R1bGUpOlxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgICMgVGF5bG9yIHNjb3JlIHBlciBvdXRwdXQgZmlsdGVyOiBzdW0gfGdyYWQgKiB3ZWlnaHR8IG92ZXIgQ19pbiwga0gsIGtXXG4gICAgICAgICAgICBzY29yZSA9IChncmFkICogbW9kdWxlLndlaWdodC5kYXRhKS5hYnMoKS5zdW0oZGltPSgxLCAyLCAzKSlcbiAgICAgICAgICAgIGlmIG5hbWUgbm90IGluIHNlbGYuc2NvcmVzOlxuICAgICAgICAgICAgICAgIHNlbGYuc2NvcmVzW25hbWVdID0gc2NvcmVcbiAgICAgICAgICAgIGVsc2U6XG4gICAgICAgICAgICAgICAgc2VsZi5zY29yZXNbbmFtZV0gKz0gc2NvcmVcblxuICAgIGRlZiBjb21wdXRlX3JhbmtpbmdzKHNlbGYpOlxuICAgICAgICByYW5raW5ncyA9IHt9XG4gICAgICAgIGZvciBuYW1lLCBzY29yZSBpbiBzZWxmLnNjb3Jlcy5pdGVtcygpOlxuICAgICAgICAgICAgb3JkZXIgPSBzY29yZS5hcmdzb3J0KCkgICMgYXNjZW5kaW5nOiB3ZWFrZXN0IGZpbHRlcnMgZmlyc3RcbiAgICAgICAgICAgIHJhbmtpbmdzW25hbWVdID0gb3JkZXJcbiAgICAgICAgcmV0dXJuIHJhbmtpbmdzXG5cbiAgICBkZWYgcmVtb3ZlX2hvb2tzKHNlbGYpOlxuICAgICAgICBmb3IgaCBpbiBzZWxmLl9ob29rczpcbiAgICAgICAgICAgIGgucmVtb3ZlKClcblxuIyBVc2FnZVxubW9kZWwgPSBubi5TZXF1ZW50aWFsKG5uLkNvbnYyZCgzLCAzMiwgMyksIG5uLlJlTFUoKSwgbm4uQ29udjJkKDMyLCA2NCwgMykpXG5wcnVuZXIgPSBUYXlsb3JQcnVuZXIobW9kZWwpXG54ID0gdG9yY2gucmFuZG4oNCwgMywgMzIsIDMyKVxubG9zcyA9IG1vZGVsKHgpLm1lYW4oKVxubG9zcy5iYWNrd2FyZCgpXG5yYW5raW5ncyA9IHBydW5lci5jb21wdXRlX3JhbmtpbmdzKClcbmZvciBuYW1lLCByYW5rIGluIHJhbmtpbmdzLml0ZW1zKCk6XG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lfTogdG9wLTMgd2Vha2VzdCBmaWx0ZXJzID0ge3JhbmtbOjNdLnRvbGlzdCgpfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBdHRlbnRpb24gSGVhZCBQcnVuaW5nIGluIFRyYW5zZm9ybWVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGktaGVhZCBhdHRlbnRpb24gd2l0aCBIIGhlYWRzIGNvbXB1dGVzIEggcGFyYWxsZWwgYXR0ZW50aW9uIHBhdHRlcm5zIGFuZCBjb25jYXRlbmF0ZXMgcmVzdWx0cy4gTm90IGFsbCBoZWFkcyBhcmUgZXF1YWxseSBpbXBvcnRhbnQg4oCUIHNvbWUgaGVhZHMgYXR0ZW5kIHRvIHN5bnRheCwgb3RoZXJzIHRvIHNlbWFudGljcywgYW5kIHNvbWUgYXJlIG5lYXJseSByZWR1bmRhbnQuIEhlYWQgaW1wb3J0YW5jZSBjYW4gYmUgbWVhc3VyZWQgYnkgdGhlIGV4cGVjdGVkIHNlbnNpdGl2aXR5IOKIgkwv4oiCeiBmb3IgZWFjaCBoZWFkXHUwMDI3cyBjb250cmlidXRpb24gb3IgYnkgYSBzaW1wbGVyIHByb3h5OiB0aGUgTDEgbm9ybSBvZiB0aGUgaGVhZFx1MDAyN3Mgb3V0cHV0IHByb2plY3Rpb24gc2xpY2UuIFJlbW92aW5nIGEgaGVhZCBzZXRzIGl0cyBjb250cmlidXRpb24gdG8gemVybyBhbmQgcmVtb3ZlcyB0aGUgY29ycmVzcG9uZGluZyBjb2x1bW5zIGluIFdfTy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBtYXRoXG5cbmRlZiBjb21wdXRlX2hlYWRfaW1wb3J0YW5jZShhdHRuX291dHB1dF93ZWlnaHRzLCBoZWFkX2RpbSwgbl9oZWFkcyk6XG4gICAgXCJcIlwiXG4gICAgYXR0bl9vdXRwdXRfd2VpZ2h0czogKGJhdGNoLCBuX2hlYWRzLCBzZXEsIHNlcSlcbiAgICBSZXR1cm5zIGltcG9ydGFuY2Ugc2NvcmUgcGVyIGhlYWQgKHZhcmlhbmNlIG9mIGF0dGVudGlvbiBkaXN0cmlidXRpb24pLlxuICAgIFwiXCJcIlxuICAgICMgSGlnaGVyIGVudHJvcHkgPSBtb3JlIHVuaWZvcm0gPSBsZXNzIHNwZWNpYWxpemVkID0gbG93ZXIgaW1wb3J0YW5jZVxuICAgIGVwcyA9IDFlLTlcbiAgICBlbnRyb3B5ID0gLShhdHRuX291dHB1dF93ZWlnaHRzICogKGF0dG5fb3V0cHV0X3dlaWdodHMgKyBlcHMpLmxvZygpKS5zdW0oLTEpICAjIChCLEgsUylcbiAgICAjIExvdyBlbnRyb3B5IGhlYWRzIGFyZSBtb3JlIHNlbGVjdGl2ZSAtXHUwMDNlIGhpZ2hlciBpbXBvcnRhbmNlXG4gICAgaW1wb3J0YW5jZSA9IC1lbnRyb3B5Lm1lYW4oZGltPSgwLCAyKSkgICMgKEgsKVxuICAgIHJldHVybiBpbXBvcnRhbmNlXG5cbmRlZiBwcnVuZV9hdHRlbnRpb25faGVhZHMoV19xLCBXX2ssIFdfdiwgV19vLCBoZWFkX2RpbSwgaGVhZHNfdG9fcHJ1bmUpOlxuICAgIFwiXCJcIlplcm8gb3V0IHNwZWNpZmllZCBhdHRlbnRpb24gaGVhZHMgaW4gV19xLCBXX2ssIFdfdiBhbmQgbWF0Y2hpbmcgV19vIGNvbHVtbnMuXCJcIlwiXG4gICAgbl9oZWFkcyA9IFdfcS5zaGFwZVswXSAvLyBoZWFkX2RpbVxuICAgIG1hc2sgPSB0b3JjaC5vbmVzKG5faGVhZHMsIGR0eXBlPXRvcmNoLmJvb2wpXG4gICAgbWFza1tsaXN0KGhlYWRzX3RvX3BydW5lKV0gPSBGYWxzZVxuICAgIGtlZXAgPSBtYXNrLm5vbnplcm8oYXNfdHVwbGU9VHJ1ZSlbMF1cbiAgICBwcmludChmXHUwMDI3S2VlcGluZyB7a2VlcC5udW1lbCgpfS97bl9oZWFkc30gaGVhZHNcdTAwMjcpXG4gICAgIyBTbGljZSBwcm9qZWN0aW9uIHdlaWdodHNcbiAgICBrZXB0X3Jvd3MgPSB0b3JjaC5jYXQoW3RvcmNoLmFyYW5nZShoKmhlYWRfZGltLCAoaCsxKSpoZWFkX2RpbSkgZm9yIGggaW4ga2VlcC50b2xpc3QoKV0pXG4gICAgV19xX3AgPSBXX3Fba2VwdF9yb3dzXVxuICAgIFdfa19wID0gV19rW2tlcHRfcm93c11cbiAgICBXX3ZfcCA9IFdfdltrZXB0X3Jvd3NdXG4gICAgV19vX3AgPSBXX29bOiwga2VwdF9yb3dzXSAgIyBvdXRwdXQgcHJvamVjdGlvbjogY29scyBjb3JyZXNwb25kIHRvIGhlYWRzXG4gICAgcmV0dXJuIFdfcV9wLCBXX2tfcCwgV192X3AsIFdfb19wXG5cbm5faGVhZHMsIGhlYWRfZGltLCBkX21vZGVsID0gOCwgNjQsIDUxMlxuV19xID0gdG9yY2gucmFuZG4obl9oZWFkcyAqIGhlYWRfZGltLCBkX21vZGVsKVxuV19rID0gdG9yY2gucmFuZG4obl9oZWFkcyAqIGhlYWRfZGltLCBkX21vZGVsKVxuV192ID0gdG9yY2gucmFuZG4obl9oZWFkcyAqIGhlYWRfZGltLCBkX21vZGVsKVxuV19vID0gdG9yY2gucmFuZG4oZF9tb2RlbCwgbl9oZWFkcyAqIGhlYWRfZGltKVxuV3FfcCwgV2tfcCwgV3ZfcCwgV29fcCA9IHBydW5lX2F0dGVudGlvbl9oZWFkcyhXX3EsIFdfaywgV192LCBXX28sIGhlYWRfZGltLCBoZWFkc190b19wcnVuZT17MiwgNX0pXG5wcmludChmXHUwMDI3V19xOiB7V19xLnNoYXBlfSAtXHUwMDNlIHtXcV9wLnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXllciBQcnVuaW5nIGFuZCBEZXB0aCBSZWR1Y3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBUcmFuc2Zvcm1lciBtb2RlbHMsIGVudGlyZSBlbmNvZGVyIG9yIGRlY29kZXIgbGF5ZXJzIGNhbiBiZSByZW1vdmVkIOKAlCBkZXB0aCBwcnVuaW5nLiBMYXllciBpbXBvcnRhbmNlIGlzIG1lYXN1cmVkIGJ5IGNvbXBhcmluZyB0aGUgbW9kZWxcdTAwMjdzIG91dHB1dCBkaXN0cmlidXRpb24gYmVmb3JlIGFuZCBhZnRlciByZW1vdmluZyB0aGUgbGF5ZXIsIG9yIGJ5IHRoZSBjb3NpbmUgc2ltaWxhcml0eSBiZXR3ZWVuIHRoZSBsYXllclx1MDAyN3MgaW5wdXQgYW5kIG91dHB1dCAoaGlnaCBzaW1pbGFyaXR5ID0gbmVhcmx5IGlkZW50aXR5ID0gbG93IGltcG9ydGFuY2UpLiBTaGFsbG93LWxheWVyIHJlbW92YWwgdGVuZHMgdG8gaHVydCBtb3JlIHRoYW4gcmVtb3ZpbmcgdXBwZXIgbGF5ZXJzOyBlbXBpcmljYWxseSwgbWlkZGxlIGxheWVycyBpbiBCRVJUIGVuY29kZXJzIGFyZSBtb3N0IHJlZHVuZGFudC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJdGVyYXRpdmUgUHJ1bmluZyB3aXRoIEZpbmUtVHVuaW5nIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cblxuZGVmIGl0ZXJhdGl2ZV9wcnVuZV9hbmRfZmluZXR1bmUoXG4gICAgbW9kZWwsIHRyYWluX2xvYWRlciwgY3JpdGVyaW9uLCBkZXZpY2UsXG4gICAgcHJ1bmVfc3RlcHM9NSwgdGFyZ2V0X3NwYXJzaXR5PTAuNSxcbiAgICBmaW5ldHVuZV9lcG9jaHM9MiwgbHI9MWUtNFxuKTpcbiAgICBcIlwiXCJcbiAgICBJdGVyYXRpdmVseSBwcnVuZSBwcnVuZV9zdGVwcyB0aW1lcywgZmluZS10dW5pbmcgYmV0d2VlbiBzdGVwcy5cbiAgICBFYWNoIHN0ZXAgcmVtb3ZlcyAodGFyZ2V0X3NwYXJzaXR5IC8gcHJ1bmVfc3RlcHMpIGFkZGl0aW9uYWwgZmlsdGVycy5cbiAgICBcIlwiXCJcbiAgICBzcGFyc2l0eV9wZXJfc3RlcCA9IHRhcmdldF9zcGFyc2l0eSAvIHBydW5lX3N0ZXBzXG4gICAgb3B0aW1pemVyID0gb3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPWxyKVxuXG4gICAgZm9yIHN0ZXAgaW4gcmFuZ2UocHJ1bmVfc3RlcHMpOlxuICAgICAgICBjdXJyZW50X3NwYXJzaXR5ID0gc3BhcnNpdHlfcGVyX3N0ZXAgKiAoc3RlcCArIDEpXG4gICAgICAgIHByaW50KGZcdTAwMjdcXG5TdGVwIHtzdGVwKzF9L3twcnVuZV9zdGVwc306IHBydW5pbmcgdG8ge2N1cnJlbnRfc3BhcnNpdHk6LjAlfSBzcGFyc2l0eVx1MDAyNylcblxuICAgICAgICAjIFBydW5lIGFsbCBDb252MmQgbGF5ZXJzXG4gICAgICAgIGZvciBuYW1lLCBtb2R1bGUgaW4gbGlzdChtb2RlbC5uYW1lZF9tb2R1bGVzKCkpOlxuICAgICAgICAgICAgaWYgaXNpbnN0YW5jZShtb2R1bGUsIG5uLkNvbnYyZCkgYW5kIG1vZHVsZS53ZWlnaHQuc2hhcGVbMF0gXHUwMDNlIDQ6XG4gICAgICAgICAgICAgICAgc2NvcmVzID0gbW9kdWxlLndlaWdodC5kYXRhLmFicygpLnN1bShkaW09KDEsIDIsIDMpKVxuICAgICAgICAgICAgICAgIHRocmVzaG9sZCA9IHNjb3Jlcy5xdWFudGlsZShzcGFyc2l0eV9wZXJfc3RlcClcbiAgICAgICAgICAgICAgICBtYXNrID0gc2NvcmVzIFx1MDAzZT0gdGhyZXNob2xkXG4gICAgICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICAgICAgICAgIG1vZHVsZS53ZWlnaHQuZGF0YVt+bWFza10gPSAwLjAgICMgc29mdCB6ZXJvIChrZWVwIHNoYXBlKVxuXG4gICAgICAgICMgRmluZS10dW5lIGZvciBhIGZldyBlcG9jaHNcbiAgICAgICAgbW9kZWwudHJhaW4oKVxuICAgICAgICBmb3IgZXBvY2ggaW4gcmFuZ2UoZmluZXR1bmVfZXBvY2hzKTpcbiAgICAgICAgICAgIHRvdGFsX2xvc3MgPSAwXG4gICAgICAgICAgICBmb3IgWF9iYXRjaCwgeV9iYXRjaCBpbiB0cmFpbl9sb2FkZXI6XG4gICAgICAgICAgICAgICAgWF9iYXRjaCwgeV9iYXRjaCA9IFhfYmF0Y2gudG8oZGV2aWNlKSwgeV9iYXRjaC50byhkZXZpY2UpXG4gICAgICAgICAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgICAgICAgICAgbG9zcyA9IGNyaXRlcmlvbihtb2RlbChYX2JhdGNoKSwgeV9iYXRjaClcbiAgICAgICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgICAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgICAgICAgICAgdG90YWxfbG9zcyArPSBsb3NzLml0ZW0oKVxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyNyAgRXBvY2gge2Vwb2NoKzF9OiBhdmcgbG9zcyA9IHt0b3RhbF9sb3NzL2xlbih0cmFpbl9sb2FkZXIpOi40Zn1cdTAwMjcpXG5cbiAgICByZXR1cm4gbW9kZWxcblxucHJpbnQoXHUwMDI3SXRlcmF0aXZlIHBydW5pbmc6IHBydW5lIC1cdTAwM2UgZmluZS10dW5lIC1cdTAwM2UgcHJ1bmUgY3ljbGUgZGVmaW5lZC5cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlBydW5lIFRoZW4gRmluZS1UdW5lLCBOb3QgRmluZS1UdW5lIFRoZW4gUHJ1bmUiLCJjb250ZW50IjoiUHJ1bmluZyBhYnJ1cHRseSBsb3dlcnMgYWNjdXJhY3kuIEFsd2F5cyBmaW5lLXR1bmUgYWZ0ZXIgZWFjaCBwcnVuaW5nIHN0ZXAgdG8gcmVjb3ZlciBsb3N0IHBlcmZvcm1hbmNlLiBGb3Igc3RydWN0dXJlZCBwcnVuaW5nIGF0IDUwJSBmaWx0ZXIgcmVtb3ZhbCwgZXZlbiAx4oCTMiBlcG9jaHMgb2YgZmluZS10dW5pbmcgYXQgYSByZWR1Y2VkIGxlYXJuaW5nIHJhdGUgKDEww5cgc21hbGxlciB0aGFuIG9yaWdpbmFsKSB0eXBpY2FsbHkgcmVjb3ZlcnMgd2l0aGluIDElIG9mIHRoZSBiYXNlbGluZS4gTGFyZ2VyIHBydW5pbmcgcmF0aW9zIG5lZWQgbW9yZSByZWNvdmVyeSBzdGVwcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZWNvbnN0cnVjdGlvbi1CYXNlZCBNZXRob2RzIChIUmFuaywgQ0hJUCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikluc3RlYWQgb2Ygd2VpZ2h0LWJhc2VkIHNjb3JlcywgSFJhbmsgbWVhc3VyZXMgdGhlIGF2ZXJhZ2UgcmFuayBvZiB0aGUgZmVhdHVyZSBtYXBzIHByb2R1Y2VkIGJ5IGVhY2ggZmlsdGVyIG92ZXIgYSBiYXRjaCBvZiBpbnB1dHMuIExvdy1yYW5rIGZlYXR1cmUgbWFwcyBjYXJyeSBsZXNzIGluZm9ybWF0aW9uIGFuZCBhcmUgcHJ1bmVkIGZpcnN0LiBDSElQIG1pbmltaXplcyB0aGUgTDIgZGlzdGFuY2UgYmV0d2VlbiB0aGUgb3V0cHV0IGZlYXR1cmUgbWFwcyBvZiB0aGUgcHJ1bmVkIGxheWVyIGFuZCB0aGUgb3JpZ2luYWwgbGF5ZXIsIGZvcm11bGF0ZWQgYXMgYSBsZWFzdC1zcXVhcmVzIGNoYW5uZWwgc2VsZWN0aW9uIHByb2JsZW0uIFRoZXNlIHJlY29uc3RydWN0aW9uLWJhc2VkIGNyaXRlcmlhIGFyZSBtb3JlIGFjY3VyYXRlIHRoYW4gTDEtbm9ybSBidXQgcmVxdWlyZSBhIGNhbGlicmF0aW9uIGZvcndhcmQgcGFzcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkhSYW5rOiBwcnVuZSBmaWx0ZXJzIHByb2R1Y2luZyBsb3ctcmFuayBmZWF0dXJlIG1hcHMgKGhpZ2ggcmFuayA9IHJpY2hlciByZXByZXNlbnRhdGlvbikuIiwiQ0hJUDogc2VsZWN0IHN1YnNldCBvZiBjaGFubmVscyBtaW5pbWlzaW5nIOKAlkZfb3JpZ2luYWwgLSBGX3BydW5lZOKAluKCgiB2aWEgZ3JlZWR5IG9yIE9NUC4iLCJUYXlsb3IgY3JpdGVyaW9uOiBvbmUgYmFja3dhcmQgcGFzcyBvdmVyIGNhbGlicmF0aW9uIGRhdGEsIGNhcHR1cmVzIGdyYWRpZW50IMOXIHdlaWdodCBzZW5zaXRpdml0eS4iLCJBY3RpdmF0aW9uIHN0YXRpc3RpY3M6IHBydW5lIGZpbHRlcnMgd2hvc2UgYWN0aXZhdGlvbnMgYXJlIG5lYXItemVybyBhY3Jvc3MgdGhlIGNhbGlicmF0aW9uIHNldC4iLCJSYW5kb20gcHJ1bmluZyBiYXNlbGluZTogc3VycHJpc2luZ2x5IGNvbXBldGl0aXZlIGF0IGxvdyBzcGFyc2l0eSAoXHUwMDNjMzAlKSwgdXNlZnVsIGFzIHNhbml0eSBjaGVjay4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJ1bmluZyBTdHJhdGVneSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIldoYXQgSXMgUmVtb3ZlZCIsIkdQVSBTcGVlZHVwIiwiQWNjdXJhY3kgSW1wYWN0IiwiSGFyZHdhcmUgRGVwZW5kZW5jeSIsIkltcGxlbWVudGF0aW9uIEVmZm9ydCJdLCJyb3dzIjpbWyJVbnN0cnVjdHVyZWQiLCJJbmRpdmlkdWFsIHdlaWdodHMiLCJOb25lICh3aXRob3V0IFNwTU0gSFcpIiwiTG93IGF0IFx1MDAzYzgwJSBzcGFyc2l0eSIsIlNwYXJzZSB0ZW5zb3IgY29yZXMgKEExMDApIiwiTG93IOKAlCBhcHBseSB0aHJlc2hvbGQgbWFzayJdLFsiRmlsdGVyIHBydW5pbmciLCJFbnRpcmUgb3V0cHV0IGZpbHRlcnMiLCJIaWdoIOKAlCBmZXdlciBjb252IG91dHB1dHMiLCJNZWRpdW0g4oCUIHVwZGF0ZSBuZXh0IGxheWVyIiwiTm9uZSDigJQgZGVuc2UgYWZ0ZXIgcHJ1bmluZyIsIk1lZGl1bSDigJQgcmVzaGFwZSBjb25zZWN1dGl2ZSBsYXllcnMiXSxbIkNoYW5uZWwgcHJ1bmluZyIsIklucHV0K291dHB1dCBjaGFubmVscyBqb2ludGx5IiwiSGlnaCDigJQgbWF0Y2hlcyBmaWx0ZXIgcHJ1bmluZyIsIk1lZGl1bSIsIk5vbmUiLCJIaWdoIOKAlCBib3RoIGxheWVycyBtdXN0IGJlIGNvbnNpc3RlbnQiXSxbIkxheWVyIHBydW5pbmciLCJFbnRpcmUgVHJhbnNmb3JtZXIgYmxvY2tzIiwiVmVyeSBoaWdoIGZvciBsYXJnZSBtb2RlbHMiLCJIaWdoIGlmIHRvbyBhZ2dyZXNzaXZlIiwiTm9uZSIsIkxvdyDigJQgc2tpcCBsYXllcnMgaW4gZm9yd2FyZCJdLFsiSGVhZCBwcnVuaW5nIChUcmFuc2Zvcm1lcnMpIiwiQXR0ZW50aW9uIGhlYWRzIiwiTW9kZXJhdGUgKDEw4oCTMzAlKSIsIkxvdyBhdCBcdTAwM2M1MCUgaGVhZHMgcmVtb3ZlZCIsIk5vbmUiLCJNZWRpdW0g4oCUIHNsaWNlIHByb2plY3Rpb24gbWF0cmljZXMiXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Structured Pruning — Filter, Channel, and Layer Removal

Unstructured pruning sets individual weights to zero, producing sparse weight matrices. Without specialized sparse-matrix hardware, these zero weights still consume memory and participate in matrix multiplications — yielding no wall-clock speedup on a standard GPU. Structured pruning solves this by removing entire filters, channels, or layers. The resulting model is dense and smaller; standard BLAS routines and GPU tensor cores immediately accelerate it without any special handling.

## Why Structure Matters for Speedup

A convolutional layer with 256 output filters and 50% unstructured sparsity still performs 256 output-channel dot products — half the FLOPs are wasted on multiplying by zero, but the loop count is unchanged. Remove 128 entire filters and the layer now performs 128 dot products with no zero arithmetic. This gives a 2× FLOP reduction that translates directly to throughput on any hardware. Structured pruning therefore reduces FLOPS, not just parameter count.

## Filter Pruning with L1-Norm Criterion

For a conv layer with weight tensor W ∈ ℝ^{C_out × C_in × k × k}, each output filter i has importance score s_i = ‖W_i‖₁ — the sum of absolute values across all elements of that filter. Filters with low L1-norm contribute little to the output feature map. After ranking all filters by s_i, the bottom p% are removed. The subsequent layer's input channels must be pruned correspondingly: removing filter i from layer l removes input channel i from layer l+1.

```python
import torch
import torch.nn as nn

def prune_conv_layer(conv: nn.Conv2d, prune_ratio: float):
    """Prune bottom prune_ratio filters by L1 norm. Returns new Conv2d."""
    with torch.no_grad():
        W = conv.weight.data  # (C_out, C_in, kH, kW)
        scores = W.abs().sum(dim=(1, 2, 3))  # L1 norm per filter
        n_keep = max(1, int(W.shape[0] * (1 - prune_ratio)))
        keep_idx = scores.topk(n_keep).indices.sort().values

        new_conv = nn.Conv2d(
            in_channels=W.shape[1],
            out_channels=n_keep,
            kernel_size=conv.kernel_size,
            stride=conv.stride,
            padding=conv.padding,
            bias=conv.bias is not None,
        )
        new_conv.weight.data = W[keep_idx]
        if conv.bias is not None:
            new_conv.bias.data = conv.bias.data[keep_idx]
    return new_conv, keep_idx

def prune_bn_layer(bn: nn.BatchNorm2d, keep_idx: torch.Tensor):
    new_bn = nn.BatchNorm2d(len(keep_idx))
    new_bn.weight.data = bn.weight.data[keep_idx]
    new_bn.bias.data = bn.bias.data[keep_idx]
    new_bn.running_mean = bn.running_mean[keep_idx]
    new_bn.running_var = bn.running_var[keep_idx]
    return new_bn

# Demo
conv = nn.Conv2d(64, 128, 3, padding=1)
conv_pruned, kept = prune_conv_layer(conv, prune_ratio=0.4)
print(f'Original: {conv.weight.shape}  -> Pruned: {conv_pruned.weight.shape}')
print(f'Kept filter indices (first 5): {kept[:5].tolist()}')
```

## Taylor Expansion Importance Score

The L1-norm criterion ignores gradient information. A filter with large weights but zero gradient contributes little to the loss. The Taylor expansion criterion approximates the change in loss when filter i is removed: ΔL ≈ Σ_j |g_j · w_j| where g_j = ∂L/∂w_j. This first-order approximation is computed in a single forward+backward pass over a calibration set and captures how sensitive the loss is to each filter's weights.

```python
import torch
import torch.nn as nn
from collections import defaultdict

class TaylorPruner:
    def __init__(self, model: nn.Module):
        self.model = model
        self.scores = defaultdict(float)
        self._hooks = []
        self._register_hooks()

    def _register_hooks(self):
        for name, module in self.model.named_modules():
            if isinstance(module, nn.Conv2d):
                h = module.weight.register_hook(
                    lambda grad, n=name, m=module: self._accumulate(n, grad, m)
                )
                self._hooks.append(h)

    def _accumulate(self, name, grad, module):
        with torch.no_grad():
            # Taylor score per output filter: sum |grad * weight| over C_in, kH, kW
            score = (grad * module.weight.data).abs().sum(dim=(1, 2, 3))
            if name not in self.scores:
                self.scores[name] = score
            else:
                self.scores[name] += score

    def compute_rankings(self):
        rankings = {}
        for name, score in self.scores.items():
            order = score.argsort()  # ascending: weakest filters first
            rankings[name] = order
        return rankings

    def remove_hooks(self):
        for h in self._hooks:
            h.remove()

# Usage
model = nn.Sequential(nn.Conv2d(3, 32, 3), nn.ReLU(), nn.Conv2d(32, 64, 3))
pruner = TaylorPruner(model)
x = torch.randn(4, 3, 32, 32)
loss = model(x).mean()
loss.backward()
rankings = pruner.compute_rankings()
for name, rank in rankings.items():
    print(f'{name}: top-3 weakest filters = {rank[:3].tolist()}')
```

## Attention Head Pruning in Transformers

Multi-head attention with H heads computes H parallel attention patterns and concatenates results. Not all heads are equally important — some heads attend to syntax, others to semantics, and some are nearly redundant. Head importance can be measured by the expected sensitivity ∂L/∂z for each head's contribution or by a simpler proxy: the L1 norm of the head's output projection slice. Removing a head sets its contribution to zero and removes the corresponding columns in W_O.

```python
import torch
import torch.nn as nn
import math

def compute_head_importance(attn_output_weights, head_dim, n_heads):
    """
    attn_output_weights: (batch, n_heads, seq, seq)
    Returns importance score per head (variance of attention distribution).
    """
    # Higher entropy = more uniform = less specialized = lower importance
    eps = 1e-9
    entropy = -(attn_output_weights * (attn_output_weights + eps).log()).sum(-1)  # (B,H,S)
    # Low entropy heads are more selective -> higher importance
    importance = -entropy.mean(dim=(0, 2))  # (H,)
    return importance

def prune_attention_heads(W_q, W_k, W_v, W_o, head_dim, heads_to_prune):
    """Zero out specified attention heads in W_q, W_k, W_v and matching W_o columns."""
    n_heads = W_q.shape[0] // head_dim
    mask = torch.ones(n_heads, dtype=torch.bool)
    mask[list(heads_to_prune)] = False
    keep = mask.nonzero(as_tuple=True)[0]
    print(f'Keeping {keep.numel()}/{n_heads} heads')
    # Slice projection weights
    kept_rows = torch.cat([torch.arange(h*head_dim, (h+1)*head_dim) for h in keep.tolist()])
    W_q_p = W_q[kept_rows]
    W_k_p = W_k[kept_rows]
    W_v_p = W_v[kept_rows]
    W_o_p = W_o[:, kept_rows]  # output projection: cols correspond to heads
    return W_q_p, W_k_p, W_v_p, W_o_p

n_heads, head_dim, d_model = 8, 64, 512
W_q = torch.randn(n_heads * head_dim, d_model)
W_k = torch.randn(n_heads * head_dim, d_model)
W_v = torch.randn(n_heads * head_dim, d_model)
W_o = torch.randn(d_model, n_heads * head_dim)
Wq_p, Wk_p, Wv_p, Wo_p = prune_attention_heads(W_q, W_k, W_v, W_o, head_dim, heads_to_prune={2, 5})
print(f'W_q: {W_q.shape} -> {Wq_p.shape}')
```

## Layer Pruning and Depth Reduction

For Transformer models, entire encoder or decoder layers can be removed — depth pruning. Layer importance is measured by comparing the model's output distribution before and after removing the layer, or by the cosine similarity between the layer's input and output (high similarity = nearly identity = low importance). Shallow-layer removal tends to hurt more than removing upper layers; empirically, middle layers in BERT encoders are most redundant.

## Iterative Pruning with Fine-Tuning

```python
import torch
import torch.nn as nn
import torch.optim as optim

def iterative_prune_and_finetune(
    model, train_loader, criterion, device,
    prune_steps=5, target_sparsity=0.5,
    finetune_epochs=2, lr=1e-4
):
    """
    Iteratively prune prune_steps times, fine-tuning between steps.
    Each step removes (target_sparsity / prune_steps) additional filters.
    """
    sparsity_per_step = target_sparsity / prune_steps
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for step in range(prune_steps):
        current_sparsity = sparsity_per_step * (step + 1)
        print(f'\nStep {step+1}/{prune_steps}: pruning to {current_sparsity:.0%} sparsity')

        # Prune all Conv2d layers
        for name, module in list(model.named_modules()):
            if isinstance(module, nn.Conv2d) and module.weight.shape[0] > 4:
                scores = module.weight.data.abs().sum(dim=(1, 2, 3))
                threshold = scores.quantile(sparsity_per_step)
                mask = scores >= threshold
                with torch.no_grad():
                    module.weight.data[~mask] = 0.0  # soft zero (keep shape)

        # Fine-tune for a few epochs
        model.train()
        for epoch in range(finetune_epochs):
            total_loss = 0
            for X_batch, y_batch in train_loader:
                X_batch, y_batch = X_batch.to(device), y_batch.to(device)
                optimizer.zero_grad()
                loss = criterion(model(X_batch), y_batch)
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
            print(f'  Epoch {epoch+1}: avg loss = {total_loss/len(train_loader):.4f}')

    return model

print('Iterative pruning: prune -> fine-tune -> prune cycle defined.')
```

> **Prune Then Fine-Tune, Not Fine-Tune Then Prune**: Pruning abruptly lowers accuracy. Always fine-tune after each pruning step to recover lost performance. For structured pruning at 50% filter removal, even 1–2 epochs of fine-tuning at a reduced learning rate (10× smaller than original) typically recovers within 1% of the baseline. Larger pruning ratios need more recovery steps.

## Reconstruction-Based Methods (HRank, CHIP)

Instead of weight-based scores, HRank measures the average rank of the feature maps produced by each filter over a batch of inputs. Low-rank feature maps carry less information and are pruned first. CHIP minimizes the L2 distance between the output feature maps of the pruned layer and the original layer, formulated as a least-squares channel selection problem. These reconstruction-based criteria are more accurate than L1-norm but require a calibration forward pass.

- HRank: prune filters producing low-rank feature maps (high rank = richer representation).
- CHIP: select subset of channels minimising ‖F_original - F_pruned‖₂ via greedy or OMP.
- Taylor criterion: one backward pass over calibration data, captures gradient × weight sensitivity.
- Activation statistics: prune filters whose activations are near-zero across the calibration set.
- Random pruning baseline: surprisingly competitive at low sparsity (<30%), useful as sanity check.

## Pruning Strategy Comparison

| Method | What Is Removed | GPU Speedup | Accuracy Impact | Hardware Dependency | Implementation Effort |
| --- | --- | --- | --- | --- | --- |
| Unstructured | Individual weights | None (without SpMM HW) | Low at <80% sparsity | Sparse tensor cores (A100) | Low — apply threshold mask |
| Filter pruning | Entire output filters | High — fewer conv outputs | Medium — update next layer | None — dense after pruning | Medium — reshape consecutive layers |
| Channel pruning | Input+output channels jointly | High — matches filter pruning | Medium | None | High — both layers must be consistent |
| Layer pruning | Entire Transformer blocks | Very high for large models | High if too aggressive | None | Low — skip layers in forward |
| Head pruning (Transformers) | Attention heads | Moderate (10–30%) | Low at <50% heads removed | None | Medium — slice projection matrices |

---

