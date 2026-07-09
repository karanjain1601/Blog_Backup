---
title: "Shannon Entropy"
slug: "shannon-entropy"
description: "Entropy definition, units, bounds, and its role as the information-theoretic foundation of compression and ML loss functions."
tags: ["information-theory","math","foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2hhbm5vbiBlbnRyb3B5LCBpbnRyb2R1Y2VkIGJ5IENsYXVkZSBTaGFubm9uIGluIDE5NDgsIGlzIHRoZSBmb3VuZGF0aW9uYWwgbWVhc3VyZSBvZiB1bmNlcnRhaW50eSBpbiBpbmZvcm1hdGlvbiB0aGVvcnkuIEl0IHF1YW50aWZpZXMgdGhlIGF2ZXJhZ2UgbnVtYmVyIG9mIGJpdHMgcmVxdWlyZWQgdG8gZW5jb2RlIG91dGNvbWVzIG9mIGEgcmFuZG9tIHZhcmlhYmxlIGFuZCBzZXRzIHRoZSB0aGVvcmV0aWNhbCBmbG9vciBmb3IgbG9zc2xlc3MgY29tcHJlc3Npb24uIEV2ZXJ5IGNyb3NzLWVudHJvcHkgbG9zcywgcGVycGxleGl0eSBtZXRyaWMsIGFuZCBtdXR1YWwgaW5mb3JtYXRpb24gY2FsY3VsYXRpb24gaW4gTUwgdHJhY2VzIGRpcmVjdGx5IGJhY2sgdG8gSChYKSA9IC1zdW0gcCh4KSBsb2cgcCh4KS4gVW5kZXJzdGFuZGluZyBlbnRyb3B5IG1lYW5zIHVuZGVyc3RhbmRpbmcgd2h5IHRyYWluaW5nIGxvc3MgZmxvb3JzIGV4aXN0LCB3aHkgbGFiZWwgc21vb3RoaW5nIHdvcmtzLCBhbmQgd2hhdCBwZXJwbGV4aXR5IGFjdHVhbGx5IG1lYXN1cmVzLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvcmUgRGVmaW5pdGlvbiJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgZGlzY3JldGUgcmFuZG9tIHZhcmlhYmxlIFggd2l0aCBQTUYgcCh4KSBvdmVyIGFscGhhYmV0IFgsIFNoYW5ub24gZW50cm9weSBpcyBIKFgpID0gLXN1bV97eH0gcCh4KSBsb2cgcCh4KSA9IEVbLWxvZyBwKFgpXS4gVGhlIHRlcm0gLWxvZyBwKHgpIGlzIHRoZSBzZWxmLWluZm9ybWF0aW9uIG9mIGV2ZW50IHg6IHJhcmUgZXZlbnRzIGNhcnJ5IGxhcmdlIHNlbGYtaW5mb3JtYXRpb24sIGNlcnRhaW4gZXZlbnRzIGNhcnJ5IHplcm8uIEVudHJvcHkgaXMgdGhlcmVmb3JlIHRoZSBleHBlY3RlZCBzdXJwcmlzZSBvZiB0aGUgZGlzdHJpYnV0aW9uLiBDb252ZW50aW9uOiAwICogbG9nIDAgPSAwIChqdXN0aWZpZWQgYnkgY29udGludWl0eSkuIExvZyBiYXNlIGRldGVybWluZXMgdW5pdHM6IGJhc2UtMiBnaXZlcyBiaXRzLCBuYXR1cmFsIGxvZyBnaXZlcyBuYXRzIChQeVRvcmNoIGRlZmF1bHQpLCBiYXNlLTEwIGdpdmVzIGhhcnRsZXlzLiBDb252ZXJzaW9uOiAxIG5hdCA9IGxvZzIoZSkgYXBwcm94aW1hdGVseSAxLjQ0MjcgYml0cy4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBlbnRyb3B5IGFzIHNjaXB5X2VudHJvcHlcblxuZGVmIGVudHJvcHlfYml0cyhwcm9icyk6XG4gICAgIyBTaGFubm9uIGVudHJvcHkgaW4gYml0czsgMCpsb2coMCk9MCBieSBjb252ZW50aW9uXG4gICAgcCA9IG5wLmFzYXJyYXkocHJvYnMsIGR0eXBlPW5wLmZsb2F0NjQpXG4gICAgbWFzayA9IHAgPiAwXG4gICAgcmV0dXJuIGZsb2F0KC1ucC5zdW0ocFttYXNrXSAqIG5wLmxvZzIocFttYXNrXSkpKVxuXG5kZWYgc29mdG1heF9lbnRyb3B5X2JpdHMobG9naXRzKTpcbiAgICAjIEVudHJvcHkgb2Ygc29mdG1heCBkaXN0cmlidXRpb24gKGluIGJpdHMpXG4gICAgbG9naXRzID0gbnAuYXJyYXkobG9naXRzLCBkdHlwZT1mbG9hdClcbiAgICBsb2dpdHMgLT0gbG9naXRzLm1heCgpICAjIG51bWVyaWMgc3RhYmlsaXR5XG4gICAgcHJvYnMgPSBucC5leHAobG9naXRzKSAvIG5wLmV4cChsb2dpdHMpLnN1bSgpXG4gICAgcmV0dXJuIGVudHJvcHlfYml0cyhwcm9icylcblxucHJpbnQoZW50cm9weV9iaXRzKFswLjI1LCAwLjI1LCAwLjI1LCAwLjI1XSkpICAgIyAyLjAwMCAgdW5pZm9ybSA0LWNsYXNzXG5wcmludChlbnRyb3B5X2JpdHMoWzEuMCwgMC4wLCAwLjAsIDAuMF0pKSAgICAgICAgIyAwLjAwMCAgZGV0ZXJtaW5pc3RpY1xucHJpbnQoZW50cm9weV9iaXRzKFswLjksIDAuMV0pKSAgICAgICAgICAgICAgICAgICAjIDAuNDY5ICBCZXJub3VsbGkoMC45KVxucHJpbnQoc2NpcHlfZW50cm9weShbMC4yNV0qNCkgLyBucC5sb2coMikpICAgICAgICAjIDIuMDAwICBzY2lweSBuYXRzIHRvIGJpdHNcbnByaW50KHNvZnRtYXhfZW50cm9weV9iaXRzKFsxMC4wLCAwLjAsIDAuMF0pKSAgICAgIyB+MC4wMDUgY29uZmlkZW50XG5wcmludChzb2Z0bWF4X2VudHJvcHlfYml0cyhbMC4xLCAwLjAsIC0wLjFdKSkgICAgICMgfjEuNTg1IHVuY2VydGFpbiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1hdGhlbWF0aWNhbCBQcm9wZXJ0aWVzIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOb24tbmVnYXRpdml0eTogSChYKSA+PSAwOyBlcXVhbGl0eSBpZmYgWCBpcyBkZXRlcm1pbmlzdGljIChvbmUgb3V0Y29tZSBoYXMgcD0xKS4gTWF4aW11bSBlbnRyb3B5OiBIKFgpIDw9IGxvZ3xYfCwgYWNoaWV2ZWQgdW5pcXVlbHkgYnkgdGhlIHVuaWZvcm0gZGlzdHJpYnV0aW9uLiBDb25jYXZpdHk6IEggaXMgY29uY2F2ZSBpbiB0aGUgcHJvYmFiaWxpdHkgdmVjdG9yLCBzbyBtaXhpbmcgZGlzdHJpYnV0aW9ucyBpbmNyZWFzZXMgZW50cm9weS4gQmluYXJ5IGVudHJvcHkgSF9iKHApID0gLXAgbG9nIHAgLSAoMS1wKSBsb2coMS1wKSBpcyBjb25jYXZlIGFuZCBzeW1tZXRyaWMsIHBlYWtzIGF0IDEgYml0IGZvciBwPTAuNSwgdmFuaXNoZXMgYXQgcCBpbiB7MCwxfS4gU2hhbm5vbiBheGlvbWF0aWMgZGVyaXZhdGlvbiAoMTk0OCk6IGVudHJvcHkgaXMgdGhlIHVuaXF1ZSBmdW5jdGlvbiBzYXRpc2Z5aW5nIGNvbnRpbnVpdHkgaW4gYWxsIHBfaSwgc3ltbWV0cnkgdW5kZXIgb3V0Y29tZSBwZXJtdXRhdGlvbiwgbWF4aW1hbGl0eSBhdCB1bmlmb3JtLCBhbmQgdGhlIGNoYWluIHJ1bGUgSChYLFkpPUgoWCkrSChZfFgpLiBTdWJhZGRpdGl2aXR5OiBIKFgsWSkgPD0gSChYKStIKFkpIHdpdGggZXF1YWxpdHkgaWZmIFggYW5kIFkgYXJlIGluZGVwZW5kZW50LiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGJpbmFyeV9lbnRyb3B5KHApOlxuICAgICMgSF9iKHApIGluIGJpdHMgZm9yIEJlcm5vdWxsaShwKVxuICAgIHAgPSBucC5jbGlwKHAsIDFlLTE1LCAxIC0gMWUtMTUpXG4gICAgcmV0dXJuIC0ocCAqIG5wLmxvZzIocCkgKyAoMS1wKSAqIG5wLmxvZzIoMS1wKSlcblxuZGVmIGVudHJvcHlfYml0cyhwcm9icyk6XG4gICAgcCA9IG5wLmFzYXJyYXkocHJvYnMsIGR0eXBlPWZsb2F0KVxuICAgIG1hc2sgPSBwID4gMFxuICAgIHJldHVybiBmbG9hdCgtbnAuc3VtKHBbbWFza10gKiBucC5sb2cyKHBbbWFza10pKSlcblxuIyBCaW5hcnkgZW50cm9weSBmdW5jdGlvbiBwcm9wZXJ0aWVzXG5wcyA9IG5wLmxpbnNwYWNlKDAuMDAxLCAwLjk5OSwgMTAwMClcbmhicyA9IGJpbmFyeV9lbnRyb3B5KHBzKVxucHJpbnQoZidNYXggSF9iID0ge2hicy5tYXgoKTouNGZ9IGJpdHMgYXQgcCA9IHtwc1toYnMuYXJnbWF4KCldOi40Zn0nKVxucHJpbnQoZidIX2IoMC4xKSA9IHtiaW5hcnlfZW50cm9weSgwLjEpOi40Zn0gYml0cycpXG5wcmludChmJ0hfYigwLjUpID0ge2JpbmFyeV9lbnRyb3B5KDAuNSk6LjRmfSBiaXRzJylcblxuIyBVbmlmb3JtIG1heGltaXplcyBlbnRyb3B5OiBjb21wYXJlIHVuaWZvcm0gdnMgc2tld2VkIGRpc3RyaWJ1dGlvbnNcbmZvciBrIGluIFsyLCA0LCA4LCAxNl06XG4gICAgcF91bmkgID0gbnAub25lcyhrKSAvIGtcbiAgICBwX3NrZXcgPSBucC5hcnJheShbMC45XSArIFswLjEvKGstMSldKihrLTEpKVxuICAgIGhfdW5pICA9IGVudHJvcHlfYml0cyhwX3VuaSlcbiAgICBoX3NrZXcgPSBlbnRyb3B5X2JpdHMocF9za2V3KVxuICAgIHByaW50KGYnaz17azoyZH06IEgodW5pZm9ybSk9e2hfdW5pOi4zZn0gIEgoc2tld2VkKT17aF9za2V3Oi4zZn0nKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZhcmlhbnRzIGFuZCBTcGVjaWFsIENhc2VzIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaWZmZXJlbnRpYWwgZW50cm9weSBoKFgpID0gLWludGVncmFsIGYoeCkgbG9nIGYoeCkgZHggZXh0ZW5kcyBlbnRyb3B5IHRvIGNvbnRpbnVvdXMgZGlzdHJpYnV0aW9ucyBidXQgY2FuIGJlIG5lZ2F0aXZlOiBoKFVuaWZvcm1bMCwgZXBzXSkgPSBsb2coZXBzKSBnb2VzIHRvIC1pbmYgYXMgZXBzIGFwcHJvYWNoZXMgMC4gSXQgaXMgbm90IHJlcGFyYW1ldHJpemF0aW9uLWludmFyaWFudDogaChhWCkgPSBoKFgpICsgbG9nfGF8LiBPbmx5IGRpZmZlcmVuY2VzIGxpa2UgbXV0dWFsIGluZm9ybWF0aW9uIGNhcnJ5IGFic29sdXRlIG1lYW5pbmcuIEdhdXNzaWFuIE4obXUsIHNpZ21hXjIpIG1heGltaXplcyBoIGZvciBmaXhlZCB2YXJpYW5jZTogaCA9IDAuNSAqIGxvZygyKnBpKmUqc2lnbWFeMikuIEVudHJvcHkgcmF0ZSBoID0gbGltIEgoWDEsLi4uLFhuKS9uIGNoYXJhY3Rlcml6ZXMgc3RhdGlvbmFyeSBwcm9jZXNzZXM7IGVtcGlyaWNhbGx5IEVuZ2xpc2ggdGV4dCBydW5zIGF0IGFib3V0IDEuMC0xLjUgYml0cyBwZXIgY2hhcmFjdGVyIHZlcnN1cyBhIHRoZW9yZXRpY2FsIG1heGltdW0gb2YgbG9nMigyNykgfj0gNC43NSBiaXRzIHBlciBjaGFyYWN0ZXIuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTUwgYW5kIEFJIENvbm5lY3Rpb25zIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaGFubm9uIHNvdXJjZSBjb2RpbmcgdGhlb3JlbTogbm8gbG9zc2xlc3MgY29kZSBhdmVyYWdlcyBmZXdlciB0aGFuIEgoWCkgYml0cyBwZXIgc3ltYm9sOyBIdWZmbWFuIGNvZGVzIGFjaGlldmUgTCA8IEgoWCkrMS4gVGhlIGNyb3NzLWVudHJvcHkgZGVjb21wb3NpdGlvbiBIKHAscSkgPSBIKHApICsgS0wocHx8cSkgc3BsaXRzIHRyYWluaW5nIGxvc3MgaW50byBhbiBpcnJlZHVjaWJsZSBmbG9vciBzZXQgYnkgZGF0YSBub2lzZSBhbmQgYSByZWR1Y2libGUgS0wgdGVybS4gRm9yIG5vaXN5IGxhYmVscyB0aGUgZmxvb3IgaXMgcG9zaXRpdmUgcmVnYXJkbGVzcyBvZiBtb2RlbCBjYXBhY2l0eS4gUGVycGxleGl0eSBQUEwgPSBleHAoSChwLHEpKSBlc3RpbWF0ZXMgdGhlIGVmZmVjdGl2ZSBicmFuY2hpbmcgZmFjdG9yOyB0eXBpY2FsIExMTXMgYWNoaWV2ZSBQUEwgNS0yMC4gUHJlZGljdGl2ZSBlbnRyb3B5IHNlcnZlcyBhcyBhbiB1bmNlcnRhaW50eSBzaWduYWwgZm9yIGFjdGl2ZSBsZWFybmluZyBhbmQgT09EIGRldGVjdGlvbjogaGlnaCBlbnRyb3B5IHByZWRpY3Rpb25zIGZsYWcgbW9kZWwgdW5jZXJ0YWludHkuIEVudHJvcHkgYWxzbyBkcml2ZXMgZGVjaXNpb24gdHJlZSBpbmZvcm1hdGlvbiBnYWluIGFuZCB2YXJpYXRpb25hbCBhdXRvZW5jb2RlciBLTCByZWd1bGFyaXphdGlvbi4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHByZWRpY3RpdmVfZW50cm9weV9uYXRzKGxvZ2l0cyk6XG4gICAgIyBQcmVkaWN0aXZlIGVudHJvcHkgaW4gbmF0cyBmcm9tIGxvZ2l0IHRlbnNvciAoQiwgSylcbiAgICBwcm9icyAgPSBGLnNvZnRtYXgobG9naXRzLCBkaW09LTEpXG4gICAgbG9nX3AgID0gRi5sb2dfc29mdG1heChsb2dpdHMsIGRpbT0tMSlcbiAgICByZXR1cm4gLShwcm9icyAqIGxvZ19wKS5zdW0oZGltPS0xKSAgIyAoQiwpXG5cbmRlZiBjcm9zc19lbnRyb3B5X2RlY29tcG9zaXRpb24odHJ1ZV9wcm9icywgbW9kZWxfbG9nX3Byb2JzKTpcbiAgICAjIEgocCxxKSA9IEgocCkgKyBLTChwfHxxKVxuICAgIHAgICAgID0gdG9yY2gudGVuc29yKHRydWVfcHJvYnMsIGR0eXBlPXRvcmNoLmZsb2F0NjQpXG4gICAgbG9nX3EgPSB0b3JjaC50ZW5zb3IobW9kZWxfbG9nX3Byb2JzLCBkdHlwZT10b3JjaC5mbG9hdDY0KVxuICAgIEhfcCAgID0gLShwICogdG9yY2gubG9nKHAgKyAxZS0xMCkpLnN1bSgpLml0ZW0oKVxuICAgIEtMICAgID0gKHAgKiAodG9yY2gubG9nKHAgKyAxZS0xMCkgLSBsb2dfcSkpLnN1bSgpLml0ZW0oKVxuICAgIHJldHVybiBIX3AsIEtMLCBIX3AgKyBLTFxuXG4jIFZhcnlpbmcgY29uZmlkZW5jZTogY29uZmlkZW50LCB1bmlmb3JtLCBtaWxkXG5sb2dpdHMgPSB0b3JjaC50ZW5zb3IoW1sxMC4wLCAwLjEsIDAuMV0sIFsxLjAsIDEuMCwgMS4wXSwgWzMuMCwgMi41LCAyLjBdXSlcbkggPSBwcmVkaWN0aXZlX2VudHJvcHlfbmF0cyhsb2dpdHMpXG5mb3IgaSwgaCBpbiBlbnVtZXJhdGUoSCk6XG4gICAgcHJpbnQoZidTYW1wbGUge2l9OiBIID0ge2guaXRlbSgpOi40Zn0gbmF0cycpXG5cbiMgTm9pc3ktbGFiZWwgZmxvb3I6IDgwJSBjbGFzcyAwLCAyMCUgY2xhc3MgMVxuSF9wLCBLTCwgSF9wcSA9IGNyb3NzX2VudHJvcHlfZGVjb21wb3NpdGlvbihbMC44LCAwLjJdLCBbLTAuMjIsIC0xLjYxXSlcbnByaW50KGYnSXJyZWR1Y2libGUgbG9zcyBmbG9vciBIKHApID0ge0hfcDouNGZ9IG5hdHMnKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkltcGxlbWVudGF0aW9uIFBpdGZhbGxzIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIYW5kbGUgMCpsb2coMCk9MCBleHBsaWNpdGx5OiBtYXNraW5nIHplcm8tcHJvYmFiaWxpdHkgZW50cmllcyBiZWZvcmUgY29tcHV0aW5nIHAqbG9nKHApIGF2b2lkcyAtaW5mLiBOZXZlciBjb21wdXRlIHNvZnRtYXggdGhlbiBsb2cgc2VwYXJhdGVseSDigJQgdGhlIGNvbWJpbmF0aW9uIGxvc2VzIHByZWNpc2lvbiBmb3IgbGFyZ2UgbG9naXRzOyB1c2UgRi5sb2dfc29mdG1heCBvciBGLmNyb3NzX2VudHJvcHkgd2hpY2ggYXBwbHkgdGhlIGxvZy1zdW0tZXhwIHRyaWNrIGludGVybmFsbHkuIExvZyBiYXNlIGNvbmZ1c2lvbjogc2NpcHkuc3RhdHMuZW50cm9weSB1c2VzIG5hdHMgYnkgZGVmYXVsdDsgZGl2aWRlIGJ5IG5wLmxvZygyKSB0byBjb252ZXJ0IHRvIGJpdHMuIEVtcGlyaWNhbCBlbnRyb3B5IGZyb20gc21hbGwgc2FtcGxlcyBpcyBiaWFzZWQgdXB3YXJkIGJlY2F1c2UgcmFyZSBldmVudHMgYXJlIHVuZGVycmVwcmVzZW50ZWQg4oCUIGFwcGx5IHRoZSBNaWxsZXItTWFkb3cgY29ycmVjdGlvbiBIX2hhdCArIChtLTEpLygyTikgd2hlcmUgbSBpcyB0aGUgbnVtYmVyIG9mIG9ic2VydmVkIGJpbnMgYW5kIE4gaXMgdG90YWwgc2FtcGxlIGNvdW50LiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBHdWlkYW5jZSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVXNlIHByZWRpY3RpdmUgZW50cm9weSB0byBmbGFnIHVuY2VydGFpbiBzYW1wbGVzIGR1cmluZyBpbmZlcmVuY2U6IHRocmVzaG9sZCBhdCAwLjUgKiBsb2cyKEspIGJpdHMgdG8gY2F0Y2ggbmVhci11bmlmb3JtIHByZWRpY3Rpb25zLiBUcmFjayB0cmFpbmluZyBjcm9zcy1lbnRyb3B5IG1pbnVzIHRoZSB0aGVvcmV0aWNhbCBIKHApIGZsb29yIHRvIG1lYXN1cmUgYWN0dWFsIGxlYXJuaW5nIHByb2dyZXNzIHJhdGhlciB0aGFuIGFic29sdXRlIGxvc3MgdmFsdWVzLiBGb3IgY2xhc3MtaW1iYWxhbmNlZCBkYXRhc2V0cywgY29tcHV0ZSBwZXItY2xhc3MgZW50cm9weSB0byB2ZXJpZnkgd2hldGhlciB0aGUgbW9kZWwgaGFzIGxlYXJuZWQgbWlub3JpdHkgY2xhc3NlcyBvciBjb2xsYXBzZWQgdG8gdGhlIG1ham9yaXR5LiBBbHdheXMgdmFsaWRhdGUgZW50cm9weSBpbXBsZW1lbnRhdGlvbnMgYnkgY2hlY2tpbmcgdGhhdCBlbnRyb3B5X2JpdHMoWzEvS10qSykgcmV0dXJucyBsb2cyKEspIGJlZm9yZSB1c2luZyBpbiBwcm9kdWN0aW9uIGNvZGUuIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZW50cm9weV9iaXRzX3NhZmUocHJvYnMsIGJhc2U9Mik6XG4gICAgIyBQcm9kdWN0aW9uLXNhZmU6IHZhbGlkYXRlcyBpbnB1dHMsIGhhbmRsZXMgemVybyBwcm9iYWJpbGl0aWVzXG4gICAgcCA9IG5wLmFzYXJyYXkocHJvYnMsIGR0eXBlPW5wLmZsb2F0NjQpXG4gICAgaWYgbm90IG5wLmFsbGNsb3NlKHAuc3VtKCksIDEuMCwgYXRvbD0xZS02KTpcbiAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihmJ1Byb2JzIHN1bSB0byB7cC5zdW0oKTouNmZ9LCBleHBlY3RlZCAxLjAnKVxuICAgIGlmIG5wLmFueShwIDwgMCk6XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ05lZ2F0aXZlIHByb2JhYmlsaXRpZXMgZGV0ZWN0ZWQnKVxuICAgIG1hc2sgPSBwID4gMFxuICAgIHJhdyA9IC1ucC5zdW0ocFttYXNrXSAqIG5wLmxvZyhwW21hc2tdKSlcbiAgICByZXR1cm4gZmxvYXQocmF3IC8gbnAubG9nKGJhc2UpKVxuXG5kZWYgb29kX2ZsYWcobG9naXRzLCBrX2NsYXNzZXMsIHRocmVzaG9sZD0wLjUpOlxuICAgICMgRmxhZyBPT0QgaWYgcHJlZGljdGl2ZSBlbnRyb3B5ID4gdGhyZXNob2xkICogbWF4X2VudHJvcHlcbiAgICBsb2dpdHMgPSBucC5hc2FycmF5KGxvZ2l0cywgZHR5cGU9ZmxvYXQpXG4gICAgbG9naXRzIC09IGxvZ2l0cy5tYXgoKVxuICAgIHByb2JzID0gbnAuZXhwKGxvZ2l0cykgLyBucC5leHAobG9naXRzKS5zdW0oKVxuICAgIGggPSBlbnRyb3B5X2JpdHNfc2FmZShwcm9icylcbiAgICBtYXhfaCA9IG5wLmxvZzIoa19jbGFzc2VzKVxuICAgIHJldHVybiBoID4gdGhyZXNob2xkICogbWF4X2gsIHJvdW5kKGgsIDQpXG5cbnByaW50KG9vZF9mbGFnKFs4LjAsIDAuMCwgMC4wXSwga19jbGFzc2VzPTMpKSAgICMgKEZhbHNlLCBsb3cgZW50cm9weSlcbnByaW50KG9vZF9mbGFnKFsxLjEsIDEuMCwgMC45XSwga19jbGFzc2VzPTMpKSAgICMgKFRydWUsICBoaWdoIGVudHJvcHkpIn0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJFbnRyb3B5IEZsb29yIElzIElycmVkdWNpYmxlIiwiY29udGVudCI6IkgocCxxKSA9IEgocCkgKyBLTChwfHxxKS4gVGhlIEgocCkgdGVybSBpcyBmaXhlZCBieSB0aGUgZGF0YSBkaXN0cmlidXRpb24gYW5kIGNhbm5vdCBiZSByZWR1Y2VkIGJ5IGFueSBtb2RlbCByZWdhcmRsZXNzIG9mIHNpemUgb3IgdHJhaW5pbmcgZHVyYXRpb24uIEZvciBkYXRhc2V0cyB3aXRoIGxhYmVsIG5vaXNlIG9yIGluaGVyZW50IGNsYXNzIGFtYmlndWl0eSwgdHJhaW5pbmcgbG9zcyB3aWxsIHBsYXRlYXUgYWJvdmUgemVyby4gQmVmb3JlIGF0dHJpYnV0aW5nIGEgdHJhaW5pbmcgcGxhdGVhdSB0byB1bmRlcmZpdHRpbmcsIGNvbXB1dGUgSChwX2VtcGlyaWNhbCkgZnJvbSB5b3VyIGxhYmVsIGRpc3RyaWJ1dGlvbiB0byBkZXRlcm1pbmUgd2hldGhlciB0aGUgZmxvb3IgaXMgaXJyZWR1Y2libGUgbm9pc2Ugb3IgYSBnZW51aW5lIGNhcGFjaXR5IHByb2JsZW0uIn0sCiAgeyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRpc3RyaWJ1dGlvbiIsIkggKGJpdHMpIiwiSW50ZXJwcmV0YXRpb24iXSwicm93cyI6W1siRGV0ZXJtaW5pc3RpYyIsIjAuMDAiLCJQZXJmZWN0IGNlcnRhaW50eSwgbm8gc3VycHJpc2UiXSxbIkJlcm5vdWxsaSgwLjkpIiwiMC40NyIsIkltYmFsYW5jZWQgYmluYXJ5IG91dGNvbWUiXSxbIkZhaXIgY29pbiIsIjEuMDAiLCJNYXhpbXVtIDEtYml0IHVuY2VydGFpbnR5Il0sWyJVbmlmb3JtIDgtY2xhc3MiLCIzLjAwIiwiOC1jbGFzcyBjbGFzc2lmaWNhdGlvbiBjZWlsaW5nIl0sWyJVbmlmb3JtIDUwayB2b2NhYiIsIn4xNS42IiwiTExNIHRva2VuIHVwcGVyIGJvdW5kIl0sWyJFbmdsaXNoIGNoYXJhY3RlcnMgKGVtcGlyaWNhbCkiLCJ+MS4yIiwiU2hhbm5vbiAxOTUxIGVzdGltYXRlIl1dfSwKICB7InR5cGUiOiJkaXZpZGVyIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LAogIHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiSChYKSA9IEVbLWxvZyBwKFgpXSDigJQgZW50cm9weSBpcyBhdmVyYWdlIHN1cnByaXNlOyBiYXNlLTIgbG9nIGdpdmVzIGJpdHMsIG5hdHVyYWwgbG9nIGdpdmVzIG5hdHMiLCJVbmlmb3JtIGRpc3RyaWJ1dGlvbiB1bmlxdWVseSBtYXhpbWl6ZXMgZW50cm9weSBmb3IgYSBmaXhlZCBhbHBoYWJldCBzaXplOyBkZXRlcm1pbmlzdGljIGRpc3RyaWJ1dGlvbnMgZ2l2ZSBIPTAiLCJTaGFubm9uIHNvdXJjZSBjb2RpbmcgdGhlb3JlbTogSChYKSBpcyB0aGUgdGlnaHQgbG93ZXIgYm91bmQgb24gYXZlcmFnZSBjb2RlIGxlbmd0aCBmb3IgYW55IGxvc3NsZXNzIGNvbXByZXNzaW9uIHNjaGVtZSIsIkNyb3NzLWVudHJvcHkgSChwLHEpID0gSChwKSArIEtMKHB8fHEpOiB0cmFpbmluZyBvbmx5IHJlZHVjZXMgS0w7IEgocCkgaXMgdGhlIGlycmVkdWNpYmxlIGZsb29yIHNldCBieSBkYXRhIiwiRGlmZmVyZW50aWFsIGVudHJvcHkgY2FuIGJlIG5lZ2F0aXZlIGFuZCBpcyBub3QgcmVwYXJhbWV0cml6YXRpb24taW52YXJpYW50IOKAlCBvbmx5IGRpZmZlcmVuY2VzIGxpa2UgbXV0dWFsIGluZm9ybWF0aW9uIGFyZSBtZWFuaW5nZnVsIiwiUHJlZGljdGl2ZSBlbnRyb3B5IGlzIGEgcHJpbmNpcGxlZCB1bmNlcnRhaW50eSBzaWduYWwgZm9yIE9PRCBkZXRlY3Rpb24sIGFjdGl2ZSBsZWFybmluZywgYW5kIGNhbGlicmF0aW9uIG1vbml0b3JpbmciLCJBbHdheXMgY2hlY2sgbG9nIGJhc2UgYmVmb3JlIGNvbXBhcmluZyBlbnRyb3B5IHZhbHVlcyBhY3Jvc3MgbGlicmFyaWVzIG9yIHBhcGVycyDigJQgbmF0cyBhbmQgYml0cyBkaWZmZXIgYnkgZmFjdG9yIGxvZzIoZSkiXX0KXQo="
---
# Shannon Entropy

Shannon entropy, introduced by Claude Shannon in 1948, is the foundational measure of uncertainty in information theory. It quantifies the average number of bits required to encode outcomes of a random variable and sets the theoretical floor for lossless compression. Every cross-entropy loss, perplexity metric, and mutual information calculation in ML traces directly back to H(X) = -sum p(x) log p(x). Understanding entropy means understanding why training loss floors exist, why label smoothing works, and what perplexity actually measures.

## Core Definition

For a discrete random variable X with PMF p(x) over alphabet X, Shannon entropy is H(X) = -sum_{x} p(x) log p(x) = E[-log p(X)]. The term -log p(x) is the self-information of event x: rare events carry large self-information, certain events carry zero. Entropy is therefore the expected surprise of the distribution. Convention: 0 * log 0 = 0 (justified by continuity). Log base determines units: base-2 gives bits, natural log gives nats (PyTorch default), base-10 gives hartleys. Conversion: 1 nat = log2(e) approximately 1.4427 bits.

```python
import numpy as np
from scipy.stats import entropy as scipy_entropy

def entropy_bits(probs):
    # Shannon entropy in bits; 0*log(0)=0 by convention
    p = np.asarray(probs, dtype=np.float64)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

def softmax_entropy_bits(logits):
    # Entropy of softmax distribution (in bits)
    logits = np.array(logits, dtype=float)
    logits -= logits.max()  # numeric stability
    probs = np.exp(logits) / np.exp(logits).sum()
    return entropy_bits(probs)

print(entropy_bits([0.25, 0.25, 0.25, 0.25]))   # 2.000  uniform 4-class
print(entropy_bits([1.0, 0.0, 0.0, 0.0]))        # 0.000  deterministic
print(entropy_bits([0.9, 0.1]))                   # 0.469  Bernoulli(0.9)
print(scipy_entropy([0.25]*4) / np.log(2))        # 2.000  scipy nats to bits
print(softmax_entropy_bits([10.0, 0.0, 0.0]))     # ~0.005 confident
print(softmax_entropy_bits([0.1, 0.0, -0.1]))     # ~1.585 uncertain
```

## Mathematical Properties

Non-negativity: H(X) >= 0; equality iff X is deterministic (one outcome has p=1). Maximum entropy: H(X) <= log|X|, achieved uniquely by the uniform distribution. Concavity: H is concave in the probability vector, so mixing distributions increases entropy. Binary entropy H_b(p) = -p log p - (1-p) log(1-p) is concave and symmetric, peaks at 1 bit for p=0.5, vanishes at p in {0,1}. Shannon axiomatic derivation (1948): entropy is the unique function satisfying continuity in all p_i, symmetry under outcome permutation, maximality at uniform, and the chain rule H(X,Y)=H(X)+H(Y|X). Subadditivity: H(X,Y) <= H(X)+H(Y) with equality iff X and Y are independent.

```python
import numpy as np

def binary_entropy(p):
    # H_b(p) in bits for Bernoulli(p)
    p = np.clip(p, 1e-15, 1 - 1e-15)
    return -(p * np.log2(p) + (1-p) * np.log2(1-p))

def entropy_bits(probs):
    p = np.asarray(probs, dtype=float)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

# Binary entropy function properties
ps = np.linspace(0.001, 0.999, 1000)
hbs = binary_entropy(ps)
print(f'Max H_b = {hbs.max():.4f} bits at p = {ps[hbs.argmax()]:.4f}')
print(f'H_b(0.1) = {binary_entropy(0.1):.4f} bits')
print(f'H_b(0.5) = {binary_entropy(0.5):.4f} bits')

# Uniform maximizes entropy: compare uniform vs skewed distributions
for k in [2, 4, 8, 16]:
    p_uni  = np.ones(k) / k
    p_skew = np.array([0.9] + [0.1/(k-1)]*(k-1))
    h_uni  = entropy_bits(p_uni)
    h_skew = entropy_bits(p_skew)
    print(f'k={k:2d}: H(uniform)={h_uni:.3f}  H(skewed)={h_skew:.3f}')
```

## Variants and Special Cases

Differential entropy h(X) = -integral f(x) log f(x) dx extends entropy to continuous distributions but can be negative: h(Uniform[0, eps]) = log(eps) goes to -inf as eps approaches 0. It is not reparametrization-invariant: h(aX) = h(X) + log|a|. Only differences like mutual information carry absolute meaning. Gaussian N(mu, sigma^2) maximizes h for fixed variance: h = 0.5 * log(2*pi*e*sigma^2). Entropy rate h = lim H(X1,...,Xn)/n characterizes stationary processes; empirically English text runs at about 1.0-1.5 bits per character versus a theoretical maximum of log2(27) ~= 4.75 bits per character.

## ML and AI Connections

Shannon source coding theorem: no lossless code averages fewer than H(X) bits per symbol; Huffman codes achieve L < H(X)+1. The cross-entropy decomposition H(p,q) = H(p) + KL(p||q) splits training loss into an irreducible floor set by data noise and a reducible KL term. For noisy labels the floor is positive regardless of model capacity. Perplexity PPL = exp(H(p,q)) estimates the effective branching factor; typical LLMs achieve PPL 5-20. Predictive entropy serves as an uncertainty signal for active learning and OOD detection: high entropy predictions flag model uncertainty. Entropy also drives decision tree information gain and variational autoencoder KL regularization.

```python
import torch
import torch.nn.functional as F
import numpy as np

def predictive_entropy_nats(logits):
    # Predictive entropy in nats from logit tensor (B, K)
    probs  = F.softmax(logits, dim=-1)
    log_p  = F.log_softmax(logits, dim=-1)
    return -(probs * log_p).sum(dim=-1)  # (B,)

def cross_entropy_decomposition(true_probs, model_log_probs):
    # H(p,q) = H(p) + KL(p||q)
    p     = torch.tensor(true_probs, dtype=torch.float64)
    log_q = torch.tensor(model_log_probs, dtype=torch.float64)
    H_p   = -(p * torch.log(p + 1e-10)).sum().item()
    KL    = (p * (torch.log(p + 1e-10) - log_q)).sum().item()
    return H_p, KL, H_p + KL

# Varying confidence: confident, uniform, mild
logits = torch.tensor([[10.0, 0.1, 0.1], [1.0, 1.0, 1.0], [3.0, 2.5, 2.0]])
H = predictive_entropy_nats(logits)
for i, h in enumerate(H):
    print(f'Sample {i}: H = {h.item():.4f} nats')

# Noisy-label floor: 80% class 0, 20% class 1
H_p, KL, H_pq = cross_entropy_decomposition([0.8, 0.2], [-0.22, -1.61])
print(f'Irreducible loss floor H(p) = {H_p:.4f} nats')
```

## Implementation Pitfalls

Handle 0*log(0)=0 explicitly: masking zero-probability entries before computing p*log(p) avoids -inf. Never compute softmax then log separately — the combination loses precision for large logits; use F.log_softmax or F.cross_entropy which apply the log-sum-exp trick internally. Log base confusion: scipy.stats.entropy uses nats by default; divide by np.log(2) to convert to bits. Empirical entropy from small samples is biased upward because rare events are underrepresented — apply the Miller-Madow correction H_hat + (m-1)/(2N) where m is the number of observed bins and N is total sample count.

## Practical Guidance

Use predictive entropy to flag uncertain samples during inference: threshold at 0.5 * log2(K) bits to catch near-uniform predictions. Track training cross-entropy minus the theoretical H(p) floor to measure actual learning progress rather than absolute loss values. For class-imbalanced datasets, compute per-class entropy to verify whether the model has learned minority classes or collapsed to the majority. Always validate entropy implementations by checking that entropy_bits([1/K]*K) returns log2(K) before using in production code.

```python
import numpy as np

def entropy_bits_safe(probs, base=2):
    # Production-safe: validates inputs, handles zero probabilities
    p = np.asarray(probs, dtype=np.float64)
    if not np.allclose(p.sum(), 1.0, atol=1e-6):
        raise ValueError(f'Probs sum to {p.sum():.6f}, expected 1.0')
    if np.any(p < 0):
        raise ValueError('Negative probabilities detected')
    mask = p > 0
    raw = -np.sum(p[mask] * np.log(p[mask]))
    return float(raw / np.log(base))

def ood_flag(logits, k_classes, threshold=0.5):
    # Flag OOD if predictive entropy > threshold * max_entropy
    logits = np.asarray(logits, dtype=float)
    logits -= logits.max()
    probs = np.exp(logits) / np.exp(logits).sum()
    h = entropy_bits_safe(probs)
    max_h = np.log2(k_classes)
    return h > threshold * max_h, round(h, 4)

print(ood_flag([8.0, 0.0, 0.0], k_classes=3))   # (False, low entropy)
print(ood_flag([1.1, 1.0, 0.9], k_classes=3))   # (True,  high entropy)
```

> **WARNING: Entropy Floor Is Irreducible**
> H(p,q) = H(p) + KL(p||q). The H(p) term is fixed by the data distribution and cannot be reduced by any model regardless of size or training duration. For datasets with label noise or inherent class ambiguity, training loss will plateau above zero. Before attributing a training plateau to underfitting, compute H(p_empirical) from your label distribution to determine whether the floor is irreducible noise or a genuine capacity problem.

| Distribution | H (bits) | Interpretation |
|---|---|---|
| Deterministic | 0.00 | Perfect certainty, no surprise |
| Bernoulli(0.9) | 0.47 | Imbalanced binary outcome |
| Fair coin | 1.00 | Maximum 1-bit uncertainty |
| Uniform 8-class | 3.00 | 8-class classification ceiling |
| Uniform 50k vocab | ~15.6 | LLM token upper bound |
| English characters (empirical) | ~1.2 | Shannon 1951 estimate |

---

## Key Takeaways

- H(X) = E[-log p(X)] — entropy is average surprise; base-2 log gives bits, natural log gives nats
- Uniform distribution uniquely maximizes entropy for a fixed alphabet size; deterministic distributions give H=0
- Shannon source coding theorem: H(X) is the tight lower bound on average code length for any lossless compression scheme
- Cross-entropy H(p,q) = H(p) + KL(p||q): training only reduces KL; H(p) is the irreducible floor set by data
- Differential entropy can be negative and is not reparametrization-invariant — only differences like mutual information are meaningful
- Predictive entropy is a principled uncertainty signal for OOD detection, active learning, and calibration monitoring
- Always check log base before comparing entropy values across libraries or papers — nats and bits differ by factor log2(e)