---
title: "One-Class SVM — Hypersphere in Feature Space"
slug: "one-class-svm"
description: "Learn OCSVM's hyperplane formulation in feature space, understand the nu parameter's dual role as outlier fraction bound, visualise decision boundaries, and compare with Isolation Forest in high dimensions."
tags: ["anomaly-detection", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT25lLUNsYXNzIFNWTSAoU2Now7Zsa29wZiBldCBhbC4sIDIwMDEpIG1hcHMgdHJhaW5pbmcgZGF0YSBpbnRvIGEgaGlnaC1kaW1lbnNpb25hbCBmZWF0dXJlIHNwYWNlIHZpYSBhIGtlcm5lbCDPhiBhbmQgZmluZHMgdGhlIG1heGltdW0tbWFyZ2luIGh5cGVycGxhbmUgc2VwYXJhdGluZyB0aGUgZGF0YSBmcm9tIHRoZSBvcmlnaW4uIEluIGZlYXR1cmUgc3BhY2UsIHRoZSBkZWNpc2lvbiBib3VuZGFyeSB3cmFwcyB0aWdodGx5IGFyb3VuZCB0aGUgbm9ybWFsIGRhdGEuIFBvaW50cyBvbiB0aGUgb3JpZ2luIHNpZGUgb2YgdGhlIGh5cGVycGxhbmUgYXJlIGNsYXNzaWZpZWQgYXMgYW5vbWFsaWVzLiBUaGUga2VybmVsIHRyaWNrIGF2b2lkcyBleHBsaWNpdCBjb21wdXRhdGlvbiBvZiDPhiDigJQgb25seSBkb3QgcHJvZHVjdHMgayh44bWiLHjisbwpID0gz4YoeOG1oinCt8+GKHjisbwpIGFyZSBuZWVkZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJpbWFsIEZvcm11bGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgT0NTVk0gcHJpbWFsIHByb2JsZW0gZmluZHMgYSBoeXBlcnBsYW5lIHfhtYDPhih4KSA9IM+BIGluIGZlYXR1cmUgc3BhY2Ugd2l0aCBtYXhpbXVtIG1hcmdpbiBmcm9tIHRoZSBvcmlnaW4sIHN1YmplY3QgdG8gc2xhY2sgdmFyaWFibGVzIM6+4bWiIOKJpSAwLiBUaGUgcGFyYW1ldGVyIM69IOKIiCAoMCwxXSBpcyBhIHJlZ3VsYXJpc2F0aW9uIGNvbnN0YW50IHRoYXQgc2ltdWx0YW5lb3VzbHkgdXBwZXItYm91bmRzIHRoZSBmcmFjdGlvbiBvZiBvdXRsaWVycyBpbiB0cmFpbmluZyBkYXRhIGFuZCBsb3dlci1ib3VuZHMgdGhlIGZyYWN0aW9uIG9mIHN1cHBvcnQgdmVjdG9ycy4gQSBzbWFsbCDOvSBjcmVhdGVzIGEgdGlnaHQgYm91bmRhcnkgd2l0aCBmZXcgc3VwcG9ydCB2ZWN0b3JzOyBsYXJnZSDOvSBjcmVhdGVzIGEgbG9vc2UgYm91bmRhcnkgYWNjZXB0aW5nIG1vcmUgdHJhaW5pbmcgcG9pbnRzIG91dHNpZGUuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJcXG1pbl97dyxcXHJobyxcXHhpfSBcXGZyYWN7MX17Mn1cXHx3XFx8XjIgLSBcXHJobyArIFxcZnJhY3sxfXtcXG51IG59XFxzdW1faSBcXHhpX2kgXFxxdWFkIFxcdGV4dHtzLnQufSBcXHF1YWQgd15cXHRvcCBcXHBoaSh4X2kpIFxcZ2VxIFxccmhvIC0gXFx4aV9pLCBcXHF1YWQgXFx4aV9pIFxcZ2VxIDAifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEdWFsIEZvcm11bGF0aW9uIGFuZCBLZXJuZWwgVHJpY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBkdWFsIGZvcm0gbWFrZXMgdGhlIGtlcm5lbCB0cmljayBleHBsaWNpdDogdGhlIGRlY2lzaW9uIGZ1bmN0aW9uIGYoeCkgPSBzZ24ozqPhtaIgzrHhtaJrKHjhtaIseCkg4oiSIM+BKSBkZXBlbmRzIG9ubHkgb24ga2VybmVsIGV2YWx1YXRpb25zLiBTdXBwb3J0IHZlY3RvcnMgYXJlIHRyYWluaW5nIHBvaW50cyB3aXRoIM6x4bWiIFx1MDAzZSAwOyB0aGV5IGxpZSBleGFjdGx5IG9uIG9yIG91dHNpZGUgdGhlIGJvdW5kYXJ5LiBBdCB0aGUgc29sdXRpb24sIM+BIGNhbiBiZSBjb21wdXRlZCBmcm9tIGFueSBzdXBwb3J0IHZlY3RvciBvbiB0aGUgYm91bmRhcnkgKDAgXHUwMDNjIM6x4bWiIFx1MDAzYyAxL869bikuIFRoZSBSQkYga2VybmVsIGsoeCx5KSA9IGV4cCjiiJLOs+KAlnjiiJJ54oCWwrIpIG1hcHMgYWxsIHBvaW50cyB0byBhIHVuaXQgaHlwZXJzcGhlcmUg4oCUIM6zIGNvbnRyb2xzIGhvdyBxdWlja2x5IHNpbWlsYXJpdHkgZGVjYXlzIHdpdGggZGlzdGFuY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgT25lQ2xhc3NTVk1cblxubnAucmFuZG9tLnNlZWQoNDIpXG5YX3RyYWluID0gbnAucmFuZG9tLm5vcm1hbCgwLCAxLCAoMTAwLCAyKSlcblxuZGVmIHJiZl9rZXJuZWwoWCwgWSwgZ2FtbWE9MC41KTpcbiAgICBzcSA9IG5wLnN1bSgoWFs6LCBOb25lXSAtIFlbTm9uZV0pKioyLCBheGlzPTIpXG4gICAgcmV0dXJuIG5wLmV4cCgtZ2FtbWEgKiBzcSlcblxuZ2FtbWEgPSAwLjVcbm9jc3ZtID0gT25lQ2xhc3NTVk0oa2VybmVsPVx1MDAyN3JiZlx1MDAyNywgZ2FtbWE9Z2FtbWEsIG51PTAuMDUpXG5vY3N2bS5maXQoWF90cmFpbilcblxuc3YgICAgID0gb2Nzdm0uc3VwcG9ydF92ZWN0b3JzX1xuYWxwaGFzID0gb2Nzdm0uZHVhbF9jb2VmXy5yYXZlbCgpXG5yaG8gICAgPSBvY3N2bS5vZmZzZXRfWzBdXG5cbnByaW50KGZcdTAwMjdTdXBwb3J0IHZlY3RvcnM6IHtsZW4oc3YpfSAgKG51PTAuMDUsIG49MTAwKVx1MDAyNylcbnByaW50KGZcdTAwMjdyaG8gKHRocmVzaG9sZCk6IHtyaG86LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdGcmFjdGlvbiBTVnM6ICAgIHtsZW4oc3YpL2xlbihYX3RyYWluKTouMiV9XHUwMDI3KVxuXG5YX3Rlc3QgPSBucC5hcnJheShbWzAuNSwgMC41XSwgWzUuMCwgNS4wXSwgWy0wLjIsIDAuM11dKVxuS190ZXN0ID0gcmJmX2tlcm5lbChYX3Rlc3QsIHN2LCBnYW1tYSlcbnNjb3Jlc19tYW51YWwgID0gS190ZXN0IEAgYWxwaGFzICsgcmhvXG5zY29yZXNfc2tsZWFybiA9IG9jc3ZtLmRlY2lzaW9uX2Z1bmN0aW9uKFhfdGVzdClcbnByaW50KFx1MDAyN01hbnVhbCB2cyBza2xlYXJuIGRlY2lzaW9uIGZ1bmN0aW9uOlx1MDAyNylcbmZvciBpLCAoc20sIHNzKSBpbiBlbnVtZXJhdGUoemlwKHNjb3Jlc19tYW51YWwsIHNjb3Jlc19za2xlYXJuKSk6XG4gICAgcHJpbnQoZlx1MDAyNyAgUG9pbnQge2l9OiBtYW51YWw9e3NtOi41Zn0gIHNrbGVhcm49e3NzOi41Zn0gIGRpZmY9e2FicyhzbS1zcyk6LjJlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJza2xlYXJuIE9uZUNsYXNzU1ZNIOKAlCBEZWNpc2lvbiBCb3VuZGFyeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmlzdWFsaXNpbmcgdGhlIGRlY2lzaW9uIGJvdW5kYXJ5IHJldmVhbHMgdGhlIGtlcm5lbFx1MDAyN3MgZWZmZWN0OiBSQkYga2VybmVscyBjcmVhdGUgc21vb3RoLCBibG9iLXNoYXBlZCBib3VuZGFyaWVzIGFyb3VuZCB0aGUgdHJhaW5pbmcgZGF0YS4gVGhlIGJvdW5kYXJ5IGNvbnRyYWN0cyBhcyDOvSBkZWNyZWFzZXMgKHRpZ2h0ZXIgZml0KSBhbmQgZXhwYW5kcyBhcyDOvSBpbmNyZWFzZXMuIFRoZSBnYW1tYSBwYXJhbWV0ZXIgY29udHJvbHMgYm91bmRhcnkgc21vb3RobmVzczogaGlnaCDOsyBjcmVhdGVzIGEgY29tcGxleCwgamFnZ2VkIGJvdW5kYXJ5IHRoYXQgZml0cyBjbG9zZWx5IHRvIGV2ZXJ5IHRyYWluaW5nIHBvaW50OyBsb3cgzrMgY3JlYXRlcyBhIGJyb2FkLCBzbW9vdGggYm91bmRhcnkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgT25lQ2xhc3NTVk1cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ucC5yYW5kb20uc2VlZCg0MilcblhfdHJhaW4gPSBucC5yYW5kb20ubm9ybWFsKDAsIDEsICgyMDAsIDIpKVxuWF90ZXN0ICA9IG5wLnJhbmRvbS5ub3JtYWwoMCwgMSwgKDUwLCAyKSlcblhfYW5vbSAgPSBucC5yYW5kb20udW5pZm9ybSgtNSwgNSwgKDIwLCAyKSlcblxuc2NhbGVyID0gU3RhbmRhcmRTY2FsZXIoKVxuWF90ciA9IHNjYWxlci5maXRfdHJhbnNmb3JtKFhfdHJhaW4pXG5YX3RlID0gc2NhbGVyLnRyYW5zZm9ybShYX3Rlc3QpXG5YX2FuID0gc2NhbGVyLnRyYW5zZm9ybShYX2Fub20pXG5cbmNsZiA9IE9uZUNsYXNzU1ZNKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPVx1MDAyN2F1dG9cdTAwMjcsIG51PTAuMDUpXG5jbGYuZml0KFhfdHIpXG5cbnh4LCB5eSA9IG5wLm1lc2hncmlkKG5wLmxpbnNwYWNlKC00LCA0LCAxNTApLCBucC5saW5zcGFjZSgtNCwgNCwgMTUwKSlcblogPSBjbGYuZGVjaXNpb25fZnVuY3Rpb24obnAuY19beHgucmF2ZWwoKSwgeXkucmF2ZWwoKV0pLnJlc2hhcGUoeHguc2hhcGUpXG5cbmZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oOCwgNikpXG5heC5jb250b3VyZih4eCwgeXksIFosIGxldmVscz0yMCwgY21hcD1cdTAwMjdjb29sd2FybVx1MDAyNywgYWxwaGE9MC41KVxuYXguY29udG91cih4eCwgeXksIFosIGxldmVscz1bMF0sIGNvbG9ycz1cdTAwMjdibGFja1x1MDAyNywgbGluZXdpZHRocz0yKVxuYXguc2NhdHRlcihYX3RyWzosMF0sIFhfdHJbOiwxXSwgcz04LCBjPVx1MDAyN2JsdWVcdTAwMjcsIGFscGhhPTAuMywgbGFiZWw9XHUwMDI3VHJhaW4gKG5vcm1hbClcdTAwMjcpXG5wYW4gPSBjbGYucHJlZGljdChYX2FuKVxuYXguc2NhdHRlcihYX2FuW3Bhbj09LTEsMF0sIFhfYW5bcGFuPT0tMSwxXSwgYz1cdTAwMjdyZWRcdTAwMjcsIG1hcmtlcj1cdTAwMjd4XHUwMDI3LCBzPTYwLCBsYWJlbD1cdTAwMjdBbm9tYWx5XHUwMDI3KVxuYXgubGVnZW5kKClcbmF4LnNldF90aXRsZShcdTAwMjdPbmUtQ2xhc3MgU1ZNIERlY2lzaW9uIEJvdW5kYXJ5IChudT0wLjA1LCBSQkYpXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdvY3N2bV9ib3VuZGFyeS5wbmdcdTAwMjcsIGRwaT0xMDApIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIG51IFBhcmFtZXRlciDigJQgRHVhbCBSb2xlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgzr0gcGFyYW1ldGVyIGhhcyBhIHByZWNpc2UgbWVhbmluZyBpbiB0aGUgT0NTVk0gZm9ybXVsYXRpb246IGl0IHNpbXVsdGFuZW91c2x5ICgxKSB1cHBlci1ib3VuZHMgdGhlIGZyYWN0aW9uIG9mIHRyYWluaW5nIHBvaW50cyBvdXRzaWRlIHRoZSBib3VuZGFyeSAob3V0bGllciBmcmFjdGlvbikgYW5kICgyKSBsb3dlci1ib3VuZHMgdGhlIGZyYWN0aW9uIG9mIHRyYWluaW5nIHBvaW50cyB0aGF0IGFyZSBzdXBwb3J0IHZlY3RvcnMuIFNldHRpbmcgzr09MC4wNSBtZWFucyBhdCBtb3N0IDUlIG9mIHRyYWluaW5nIHBvaW50cyB3aWxsIGJlIGNsYXNzaWZpZWQgYXMgb3V0bGllcnMgYW5kIGF0IGxlYXN0IDUlIHdpbGwgYmUgc3VwcG9ydCB2ZWN0b3JzLiBUaGlzIG1ha2VzIM69IHRoZSBwcmltYXJ5IGtub2IgZm9yIGNvbnRyb2xsaW5nIGJvdW5kYXJ5IHRpZ2h0bmVzcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uc3ZtIGltcG9ydCBPbmVDbGFzc1NWTVxuXG5ucC5yYW5kb20uc2VlZCg0MilcblggPSBucC5yYW5kb20ubm9ybWFsKDAsIDEsICgyMDAsIDIpKVxuXG5udV92YWx1ZXMgPSBbMC4wMSwgMC4wNSwgMC4xMCwgMC4yMCwgMC40MF1cbnByaW50KGZcdTAwMjd7XCJudVwiOlx1MDAzZTZ9IHtcIlNWc1wiOlx1MDAzZTZ9IHtcIlRyYWluIG91dGxpZXJzXCI6XHUwMDNlMTZ9IHtcIkZsYWdnZWQgZnJhY3Rpb25cIjpcdTAwM2UxOH1cdTAwMjcpXG5mb3IgbnUgaW4gbnVfdmFsdWVzOlxuICAgIGNsZiA9IE9uZUNsYXNzU1ZNKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTAuNSwgbnU9bnUpLmZpdChYKVxuICAgIHByZWRzID0gY2xmLnByZWRpY3QoWClcbiAgICBuX3N2ICA9IGxlbihjbGYuc3VwcG9ydF92ZWN0b3JzXylcbiAgICBuX291dCA9IChwcmVkcyA9PSAtMSkuc3VtKClcbiAgICBwcmludChmXHUwMDI3e251Olx1MDAzZTYuMmZ9IHtuX3N2Olx1MDAzZTZ9IHtuX291dDpcdTAwM2UxNn0ge25fb3V0L2xlbihYKTpcdTAwM2UxOC4yJX1cdTAwMjcpXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMiwgNSkpXG5mb3IgYXgsIG51IGluIHppcChheGVzLCBbMC4wMSwgMC4zMF0pOlxuICAgIGNsZiA9IE9uZUNsYXNzU1ZNKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTAuNSwgbnU9bnUpLmZpdChYKVxuICAgIHh4LCB5eSA9IG5wLm1lc2hncmlkKG5wLmxpbnNwYWNlKC00LCA0LCA4MCksIG5wLmxpbnNwYWNlKC00LCA0LCA4MCkpXG4gICAgWiA9IGNsZi5kZWNpc2lvbl9mdW5jdGlvbihucC5jX1t4eC5yYXZlbCgpLCB5eS5yYXZlbCgpXSkucmVzaGFwZSh4eC5zaGFwZSlcbiAgICBheC5jb250b3VyZih4eCwgeXksIFosIGxldmVscz0xNSwgY21hcD1cdTAwMjdjb29sd2FybVx1MDAyNywgYWxwaGE9MC42KVxuICAgIGF4LnNjYXR0ZXIoWFs6LDBdLCBYWzosMV0sIHM9OCwgYz1cdTAwMjdrXHUwMDI3LCBhbHBoYT0wLjMpXG4gICAgYXguc2V0X3RpdGxlKGZcdTAwMjdudT17bnV9XHUwMDI3KVxucGx0LnN1cHRpdGxlKFx1MDAyN0VmZmVjdCBvZiBudSBvbiBPQ1NWTSBCb3VuZGFyeVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3b2Nzdm1fbnUucG5nXHUwMDI3LCBkcGk9MTAwKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9DU1ZNIHZzIElzb2xhdGlvbiBGb3Jlc3QgaW4gSGlnaCBEaW1lbnNpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPQ1NWTSB3aXRoIFJCRiBrZXJuZWwgc2NhbGVzIGFzIE8obsKyIMK3IGQpIGZvciBrZXJuZWwgZXZhbHVhdGlvbiwgbWFraW5nIGl0IGV4cGVuc2l2ZSBmb3IgbGFyZ2UgbiBvciBoaWdoIGQuIElzb2xhdGlvbiBGb3Jlc3Qgc2NhbGVzIGFzIE8obiBsb2cgbikgd2l0aCBzdWItc2FtcGxpbmcuIEluIGhpZ2ggZGltZW5zaW9ucywgUkJGIGtlcm5lbCBkaXN0YW5jZXMgY29uY2VudHJhdGUgYW5kIGdhbW1hIHR1bmluZyBiZWNvbWVzIGNyaXRpY2FsIOKAlCBhIG1pc3R1bmVkIM6zIGNhbiBtYWtlIGFsbCBwb2ludHMgYXBwZWFyIGVxdWlkaXN0YW50LiBJc29sYXRpb24gRm9yZXN0IG1haW50YWlucyBzdGFibGUgcGVyZm9ybWFuY2UgYWNyb3NzIGRpbWVuc2lvbnMgYW5kIGlzIGdlbmVyYWxseSBwcmVmZXJyZWQgZm9yIGQgXHUwMDNlIDIwLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5zdm0gaW1wb3J0IE9uZUNsYXNzU1ZNXG5mcm9tIHNrbGVhcm4uZW5zZW1ibGUgaW1wb3J0IElzb2xhdGlvbkZvcmVzdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IHJvY19hdWNfc2NvcmVcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ucC5yYW5kb20uc2VlZCg0MilcbmZvciBkIGluIFsyLCAxMCwgMzAsIDEwMF06XG4gICAgWF90cmFpbiA9IG5wLnJhbmRvbS5ub3JtYWwoMCwgMSwgKDMwMCwgZCkpXG4gICAgWF90ZXN0ICA9IG5wLnZzdGFjayhbXG4gICAgICAgIG5wLnJhbmRvbS5ub3JtYWwoMCwgMSwgKDIwMCwgZCkpLFxuICAgICAgICBucC5yYW5kb20udW5pZm9ybSgtNCwgNCwgKDUwLCBkKSlcbiAgICBdKVxuICAgIHlfdGVzdCA9IG5wLmFycmF5KFswXSoyMDAgKyBbMV0qNTApXG5cbiAgICBzY2FsZXIgPSBTdGFuZGFyZFNjYWxlcigpXG4gICAgWHRyX3MgID0gc2NhbGVyLmZpdF90cmFuc2Zvcm0oWF90cmFpbilcbiAgICBYdGVfcyAgPSBzY2FsZXIudHJhbnNmb3JtKFhfdGVzdClcblxuICAgIG9jc3ZtID0gT25lQ2xhc3NTVk0oa2VybmVsPVx1MDAyN3JiZlx1MDAyNywgZ2FtbWE9XHUwMDI3c2NhbGVcdTAwMjcsIG51PTAuMSkuZml0KFh0cl9zKVxuICAgIGlzb2ZvID0gSXNvbGF0aW9uRm9yZXN0KG5fZXN0aW1hdG9ycz0xMDAsIGNvbnRhbWluYXRpb249MC4yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICByYW5kb21fc3RhdGU9NDIpLmZpdChYdHJfcylcblxuICAgIGF1Y19vID0gcm9jX2F1Y19zY29yZSh5X3Rlc3QsIC1vY3N2bS5kZWNpc2lvbl9mdW5jdGlvbihYdGVfcykpXG4gICAgYXVjX2kgPSByb2NfYXVjX3Njb3JlKHlfdGVzdCwgLWlzb2ZvLnNjb3JlX3NhbXBsZXMoWHRlX3MpKVxuICAgIHByaW50KGZcdTAwMjdkPXtkOjNkfTogT0NTVk0gQVVDPXthdWNfbzouM2Z9ICBJc29GIEFVQz17YXVjX2k6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZXRob2QgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJCb3VuZGFyeSBzaGFwZSIsIktlcm5lbCIsIm51L0MgcGFyYW0iLCJIaWdoLWRpbSIsIlRyYWluaW5nIGNvc3QiXSwicm93cyI6W1siT0NTVk0iLCJIeXBlcnBsYW5lIGluIGtlcm5lbCBzcGFjZSIsIlllcyAoUkJGLCBwb2x5KSIsIm51OiBvdXRsaWVyIHVwcGVyIGJvdW5kIiwiUG9vciBmb3IgbGFyZ2UgZCIsIk8obsKywrdkKSJdLFsiU1ZERCIsIkh5cGVyc3BoZXJlIGluIGtlcm5lbCBzcGFjZSIsIlllcyAoUkJGKSIsIkM6IDEvKG5mKSBmcmFjdGlvbiIsIlBvb3IgZm9yIGxhcmdlIGQiLCJPKG7CssK3ZCkiXSxbIklzb2xhdGlvbiBGb3Jlc3QiLCJObyBleHBsaWNpdCBib3VuZGFyeSIsIk5vIiwiY29udGFtaW5hdGlvbiIsIkV4Y2VsbGVudCIsIk8obiBsb2cgbikiXSxbIkxPRiIsIkltcGxpY2l0IHZpYSBkZW5zaXR5IHJhdGlvIiwiTm8gKHVzZXMgZGlzdGFuY2VzKSIsIms6IG5laWdoYm91cmhvb2Qgc2l6ZSIsIlBvb3IiLCJPKG7CssK3aykiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiU1ZERC1PQ1NWTSBFcXVpdmFsZW5jZSBmb3IgUkJGIiwiY29udGVudCI6IkZvciB0aGUgUkJGIGtlcm5lbCwgU1ZERCAoU3VwcG9ydCBWZWN0b3IgRGF0YSBEZXNjcmlwdGlvbiwgVGF4IFx1MDAyNiBEdWluIDIwMDQpIGFuZCBPQ1NWTSBhcmUgbWF0aGVtYXRpY2FsbHkgZXF1aXZhbGVudC4gVGhlIFJCRiBrZXJuZWwgbWFwcyBldmVyeSBwb2ludCB0byBhIHVuaXQgaHlwZXJzcGhlcmUgaW4gZmVhdHVyZSBzcGFjZSwgc28gc2VwYXJhdGluZyBmcm9tIHRoZSBvcmlnaW4gaXMgaWRlbnRpY2FsIHRvIGZpbmRpbmcgdGhlIG1pbmltdW0tZW5jbG9zaW5nIHNwaGVyZS4gVGhlIGRlY2lzaW9uIGZ1bmN0aW9ucyBwcm9kdWNlIGlkZW50aWNhbCBzY29yZXMgZm9yIHRoZSBzYW1lIGdhbW1hIGFuZCBDPTEvKG51wrduKS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Iktlcm5lbCBzZWxlY3Rpb24gaXMgdGhlIG1vc3QgaW1wYWN0ZnVsIGRlc2lnbiBkZWNpc2lvbiBmb3IgT0NTVk0uIFRoZSBSQkYga2VybmVsIHdvcmtzIHdlbGwgZm9yIGRlbnNlLCBibG9iLXNoYXBlZCBub3JtYWwgcmVnaW9ucyBhbmQgaXMgdGhlIHN0YW5kYXJkIGRlZmF1bHQuIFRoZSBwb2x5bm9taWFsIGtlcm5lbCAoZGVncmVlPTIgb3IgMykgY2FuIGNhcHR1cmUgc3RydWN0dXJlZCBkYXRhIGxpa2UgaW1hZ2VzLiBMaW5lYXIga2VybmVsIE9DU1ZNIGlzIGVxdWl2YWxlbnQgdG8gUENBLWJhc2VkIG5vdmVsdHkgZGV0ZWN0aW9uIGFuZCBpcyBhcHByb3ByaWF0ZSB3aGVuIHRoZSBub3JtYWwgZGF0YSBsaWVzIGluIGEgbGluZWFyIHN1YnNwYWNlLiBTaWdtb2lkIGFuZCBjdXN0b20ga2VybmVscyBhcmUgcmFyZWx5IHVzZWQgaW4gcHJhY3RpY2UuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJBbHdheXMgc3RhbmRhcmRpc2UgZmVhdHVyZXMgYmVmb3JlIGZpdHRpbmcgT0NTVk0g4oCUIGtlcm5lbCBkaXN0YW5jZXMgZGVwZW5kIG9uIHNjYWxlIiwiVXNlIGdhbW1hPVx1MDAyN3NjYWxlXHUwMDI3ICgxLyhkwrdWYXIpKSBhcyBkZWZhdWx0OyB0dW5lIHZpYSBncmlkIHNlYXJjaCBvbiBhIGxhYmVsbGVkIHZhbGlkYXRpb24gc2V0IiwiRm9yIG4gXHUwMDNlIDEwLDAwMCwgdXNlIFNHRE9uZUNsYXNzU1ZNIChsaW5lYXIgYXBwcm94aW1hdGlvbikgb3Igc3dpdGNoIHRvIElzb2xhdGlvbiBGb3Jlc3QiLCJPQ1NWTSBpcyBtb3N0IHVzZWZ1bCB3aGVuIHRoZSBub3JtYWwgZGF0YSBoYXMgYSBjb21wbGV4LCBub24tR2F1c3NpYW4gc2hhcGUiLCJTZXQgbnUgdG8gdGhlIGV4cGVjdGVkIGNvbnRhbWluYXRpb24gZnJhY3Rpb24gaWYga25vd24iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgbGFyZ2Utc2NhbGUgZGVwbG95bWVudCwgc2tsZWFyblx1MDAyN3MgU0dET25lQ2xhc3NTVk0gcHJvdmlkZXMgYW4gb25saW5lIGFwcHJveGltYXRlIE9DU1ZNIHVzaW5nIHN0b2NoYXN0aWMgZ3JhZGllbnQgZGVzY2VudCBvbiB0aGUgZHVhbCB3aXRoIHJhbmRvbSBGb3VyaWVyIGZlYXR1cmVzIGFwcHJveGltYXRpbmcgdGhlIFJCRiBrZXJuZWwuIEl0IHRyYWlucyBpbiBPKG7Ct2QpIHJhdGhlciB0aGFuIE8obsKywrdkKSwgbWFraW5nIGl0IGZlYXNpYmxlIGZvciBtaWxsaW9ucyBvZiBzYW1wbGVzIHdoaWxlIHJldGFpbmluZyBtb3N0IG9mIHRoZSBkZWNpc2lvbiBxdWFsaXR5IG9mIHRoZSBleGFjdCBPQ1NWTS4ifV0="
---
# One-Class SVM — Hypersphere in Feature Space

One-Class SVM (Schölkopf et al., 2001) maps training data into a high-dimensional feature space via a kernel φ and finds the maximum-margin hyperplane separating the data from the origin. In feature space, the decision boundary wraps tightly around the normal data. Points on the origin side of the hyperplane are classified as anomalies. The kernel trick avoids explicit computation of φ — only dot products k(xᵢ,xⱼ) = φ(xᵢ)·φ(xⱼ) are needed.

## Primal Formulation

The OCSVM primal problem finds a hyperplane wᵀφ(x) = ρ in feature space with maximum margin from the origin, subject to slack variables ξᵢ ≥ 0. The parameter ν ∈ (0,1] is a regularisation constant that simultaneously upper-bounds the fraction of outliers in training data and lower-bounds the fraction of support vectors. A small ν creates a tight boundary with few support vectors; large ν creates a loose boundary accepting more training points outside.

$$\min_{w,\rho,\xi} \frac{1}{2}\|w\|^2 - \rho + \frac{1}{\nu n}\sum_i \xi_i \quad \text{s.t.} \quad w^\top \phi(x_i) \geq \rho - \xi_i, \quad \xi_i \geq 0$$

## Dual Formulation and Kernel Trick

The dual form makes the kernel trick explicit: the decision function f(x) = sgn(Σᵢ αᵢk(xᵢ,x) − ρ) depends only on kernel evaluations. Support vectors are training points with αᵢ > 0; they lie exactly on or outside the boundary. At the solution, ρ can be computed from any support vector on the boundary (0 < αᵢ < 1/νn). The RBF kernel k(x,y) = exp(−γ‖x−y‖²) maps all points to a unit hypersphere — γ controls how quickly similarity decays with distance.

```python
import numpy as np
from sklearn.svm import OneClassSVM

np.random.seed(42)
X_train = np.random.normal(0, 1, (100, 2))

def rbf_kernel(X, Y, gamma=0.5):
    sq = np.sum((X[:, None] - Y[None])**2, axis=2)
    return np.exp(-gamma * sq)

gamma = 0.5
ocsvm = OneClassSVM(kernel='rbf', gamma=gamma, nu=0.05)
ocsvm.fit(X_train)

sv     = ocsvm.support_vectors_
alphas = ocsvm.dual_coef_.ravel()
rho    = ocsvm.offset_[0]

print(f'Support vectors: {len(sv)}  (nu=0.05, n=100)')
print(f'rho (threshold): {rho:.4f}')
print(f'Fraction SVs:    {len(sv)/len(X_train):.2%}')

X_test = np.array([[0.5, 0.5], [5.0, 5.0], [-0.2, 0.3]])
K_test = rbf_kernel(X_test, sv, gamma)
scores_manual  = K_test @ alphas + rho
scores_sklearn = ocsvm.decision_function(X_test)
print('Manual vs sklearn decision function:')
for i, (sm, ss) in enumerate(zip(scores_manual, scores_sklearn)):
    print(f'  Point {i}: manual={sm:.5f}  sklearn={ss:.5f}  diff={abs(sm-ss):.2e}')
```

## sklearn OneClassSVM — Decision Boundary

Visualising the decision boundary reveals the kernel's effect: RBF kernels create smooth, blob-shaped boundaries around the training data. The boundary contracts as ν decreases (tighter fit) and expands as ν increases. The gamma parameter controls boundary smoothness: high γ creates a complex, jagged boundary that fits closely to every training point; low γ creates a broad, smooth boundary.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X_train = np.random.normal(0, 1, (200, 2))
X_test  = np.random.normal(0, 1, (50, 2))
X_anom  = np.random.uniform(-5, 5, (20, 2))

scaler = StandardScaler()
X_tr = scaler.fit_transform(X_train)
X_te = scaler.transform(X_test)
X_an = scaler.transform(X_anom)

clf = OneClassSVM(kernel='rbf', gamma='auto', nu=0.05)
clf.fit(X_tr)

xx, yy = np.meshgrid(np.linspace(-4, 4, 150), np.linspace(-4, 4, 150))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

fig, ax = plt.subplots(figsize=(8, 6))
ax.contourf(xx, yy, Z, levels=20, cmap='coolwarm', alpha=0.5)
ax.contour(xx, yy, Z, levels=[0], colors='black', linewidths=2)
ax.scatter(X_tr[:,0], X_tr[:,1], s=8, c='blue', alpha=0.3, label='Train (normal)')
pan = clf.predict(X_an)
ax.scatter(X_an[pan==-1,0], X_an[pan==-1,1], c='red', marker='x', s=60, label='Anomaly')
ax.legend()
ax.set_title('One-Class SVM Decision Boundary (nu=0.05, RBF)')
plt.tight_layout()
plt.savefig('ocsvm_boundary.png', dpi=100)
```

## The nu Parameter — Dual Role

The ν parameter has a precise meaning in the OCSVM formulation: it simultaneously (1) upper-bounds the fraction of training points outside the boundary (outlier fraction) and (2) lower-bounds the fraction of training points that are support vectors. Setting ν=0.05 means at most 5% of training points will be classified as outliers and at least 5% will be support vectors. This makes ν the primary knob for controlling boundary tightness.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM

np.random.seed(42)
X = np.random.normal(0, 1, (200, 2))

nu_values = [0.01, 0.05, 0.10, 0.20, 0.40]
print(f'{"nu":>6} {"SVs":>6} {"Train outliers":>16} {"Flagged fraction":>18}')
for nu in nu_values:
    clf = OneClassSVM(kernel='rbf', gamma=0.5, nu=nu).fit(X)
    preds = clf.predict(X)
    n_sv  = len(clf.support_vectors_)
    n_out = (preds == -1).sum()
    print(f'{nu:>6.2f} {n_sv:>6} {n_out:>16} {n_out/len(X):>18.2%}')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for ax, nu in zip(axes, [0.01, 0.30]):
    clf = OneClassSVM(kernel='rbf', gamma=0.5, nu=nu).fit(X)
    xx, yy = np.meshgrid(np.linspace(-4, 4, 80), np.linspace(-4, 4, 80))
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, levels=15, cmap='coolwarm', alpha=0.6)
    ax.scatter(X[:,0], X[:,1], s=8, c='k', alpha=0.3)
    ax.set_title(f'nu={nu}')
plt.suptitle('Effect of nu on OCSVM Boundary')
plt.tight_layout()
plt.savefig('ocsvm_nu.png', dpi=100)
```

## OCSVM vs Isolation Forest in High Dimensions

OCSVM with RBF kernel scales as O(n² · d) for kernel evaluation, making it expensive for large n or high d. Isolation Forest scales as O(n log n) with sub-sampling. In high dimensions, RBF kernel distances concentrate and gamma tuning becomes critical — a mistuned γ can make all points appear equidistant. Isolation Forest maintains stable performance across dimensions and is generally preferred for d > 20.

```python
import numpy as np
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
for d in [2, 10, 30, 100]:
    X_train = np.random.normal(0, 1, (300, d))
    X_test  = np.vstack([
        np.random.normal(0, 1, (200, d)),
        np.random.uniform(-4, 4, (50, d))
    ])
    y_test = np.array([0]*200 + [1]*50)

    scaler = StandardScaler()
    Xtr_s  = scaler.fit_transform(X_train)
    Xte_s  = scaler.transform(X_test)

    ocsvm = OneClassSVM(kernel='rbf', gamma='scale', nu=0.1).fit(Xtr_s)
    isofo = IsolationForest(n_estimators=100, contamination=0.2,
                             random_state=42).fit(Xtr_s)

    auc_o = roc_auc_score(y_test, -ocsvm.decision_function(Xte_s))
    auc_i = roc_auc_score(y_test, -isofo.score_samples(Xte_s))
    print(f'd={d:3d}: OCSVM AUC={auc_o:.3f}  IsoF AUC={auc_i:.3f}')
```

## Method Comparison

| Method | Boundary shape | Kernel | nu/C param | High-dim | Training cost |
| --- | --- | --- | --- | --- | --- |
| OCSVM | Hyperplane in kernel space | Yes (RBF, poly) | nu: outlier upper bound | Poor for large d | O(n²·d) |
| SVDD | Hypersphere in kernel space | Yes (RBF) | C: 1/(nf) fraction | Poor for large d | O(n²·d) |
| Isolation Forest | No explicit boundary | No | contamination | Excellent | O(n log n) |
| LOF | Implicit via density ratio | No (uses distances) | k: neighbourhood size | Poor | O(n²·k) |

> **SVDD-OCSVM Equivalence for RBF**: For the RBF kernel, SVDD (Support Vector Data Description, Tax & Duin 2004) and OCSVM are mathematically equivalent. The RBF kernel maps every point to a unit hypersphere in feature space, so separating from the origin is identical to finding the minimum-enclosing sphere. The decision functions produce identical scores for the same gamma and C=1/(nu·n).

Kernel selection is the most impactful design decision for OCSVM. The RBF kernel works well for dense, blob-shaped normal regions and is the standard default. The polynomial kernel (degree=2 or 3) can capture structured data like images. Linear kernel OCSVM is equivalent to PCA-based novelty detection and is appropriate when the normal data lies in a linear subspace. Sigmoid and custom kernels are rarely used in practice.

- Always standardise features before fitting OCSVM — kernel distances depend on scale
- Use gamma='scale' (1/(d·Var)) as default; tune via grid search on a labelled validation set
- For n > 10,000, use SGDOneClassSVM (linear approximation) or switch to Isolation Forest
- OCSVM is most useful when the normal data has a complex, non-Gaussian shape
- Set nu to the expected contamination fraction if known

For large-scale deployment, sklearn's SGDOneClassSVM provides an online approximate OCSVM using stochastic gradient descent on the dual with random Fourier features approximating the RBF kernel. It trains in O(n·d) rather than O(n²·d), making it feasible for millions of samples while retaining most of the decision quality of the exact OCSVM.

