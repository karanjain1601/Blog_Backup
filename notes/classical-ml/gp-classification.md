---
title: "GP Classification — Laplace Approximation and EP"
slug: "gp-classification"
description: "Non-Gaussian likelihoods for binary and multi-class GP classification: Laplace approximation via Newton's method, Expectation Propagation, variational inference, and predictive comparison."
tags: ["gaussian-processes", "kernel-methods", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBHUCBDbGFzc2lmaWNhdGlvbiBJcyBIYXJkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBjbGFzc2lmaWNhdGlvbiB0aGUgbGlrZWxpaG9vZCBwKHl8ZikgPSDPgyh5wrdmKSB3aGVyZSDPgyBpcyB0aGUgc2lnbW9pZCBmdW5jdGlvbiBpcyBub24tR2F1c3NpYW4uIFRoZSBwb3N0ZXJpb3IgcChmfFgseSkg4oidIHAoeXxmKXAoZnxYKSBpcyBubyBsb25nZXIgR2F1c3NpYW4g4oCUIGl0IGhhcyBubyBjbG9zZWQgZm9ybS4gV2UgbmVlZCBhcHByb3hpbWF0aW9ucy4gVGhyZWUgZmFtaWxpZXMgYXJlIHN0YW5kYXJkOiAoMSkgTGFwbGFjZSBhcHByb3hpbWF0aW9uIOKAlCBHYXVzc2lhbiBjZW50cmVkIGF0IHRoZSBNQVAgZXN0aW1hdGU7ICgyKSBFeHBlY3RhdGlvbiBQcm9wYWdhdGlvbiAoRVApIOKAlCBtb21lbnQtbWF0Y2hpbmcgYXBwcm94aW1hdGlvbjsgKDMpIHZhcmlhdGlvbmFsIGluZmVyZW5jZSDigJQgb3B0aW1pc2UgYSBsb3dlciBib3VuZCBvbiB0aGUgbWFyZ2luYWwgbGlrZWxpaG9vZC4gRWFjaCB0cmFkZXMgb2ZmIGFjY3VyYWN5LCBjb3N0LCBhbmQgaW1wbGVtZW50YXRpb24gY29tcGxleGl0eS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdQIHJlZ3Jlc3Npb246IEdhdXNzaWFuIGxpa2VsaWhvb2Qg4oaSIGNsb3NlZC1mb3JtIHBvc3RlcmlvciBHUCIsIkdQIGNsYXNzaWZpY2F0aW9uOiBzaWdtb2lkL3NvZnRtYXggbGlrZWxpaG9vZCDihpIgaW50cmFjdGFibGUgcG9zdGVyaW9yIiwiTGFwbGFjZTogZmFzdGVzdCwgbW9kZS1tYXRjaGluZyBHYXVzc2lhbiBhcHByb3hpbWF0aW9uIGF0IE1BUCIsIkVQOiBtb3JlIGFjY3VyYXRlLCBtb21lbnQtbWF0Y2hpbmcsIGl0ZXJhdGl2ZSBjYXZpdHkgdXBkYXRlcyIsIlZhcmlhdGlvbmFsIChTVkdQKTogc2NhbGFibGUgdG8gbGFyZ2UgbiB2aWEgaW5kdWNpbmcgcG9pbnRzIGFuZCBFTEJPIiwiTUNNQyAoSE1DL05VVFMpOiBnb2xkIHN0YW5kYXJkIGFjY3VyYWN5IGJ1dCB2ZXJ5IGhpZ2ggY29tcHV0YXRpb25hbCBjb3N0Il19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxhcGxhY2UgQXBwcm94aW1hdGlvbiB2aWEgTmV3dG9uXHUwMDI3cyBNZXRob2QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBMYXBsYWNlIGFwcHJveGltYXRpb24gKDEpIGZpbmRzIHRoZSBNQVAgZXN0aW1hdGUgZsyCID0gYXJnbWF4IGxvZyBwKGZ8WCx5KSA9IGFyZ21heCBbbG9nIHAoeXxmKSDiiJIgwr0gZuG1gCBL4oG7wrkgZl0sICgyKSBhcHByb3hpbWF0ZXMgdGhlIHBvc3RlcmlvciB3aXRoIGEgR2F1c3NpYW4gY2VudHJlZCBhdCBmzIIgd2l0aCBjb3ZhcmlhbmNlIChL4oG7wrkgKyBXKeKBu8K5IHdoZXJlIFcgPSDiiJLiiIfiiIcgbG9nIHAoeXxmzIIpIGlzIHRoZSBuZWdhdGl2ZSBIZXNzaWFuIG9mIHRoZSBsb2cgbGlrZWxpaG9vZC4gRm9yIGJpbmFyeSBjbGFzc2lmaWNhdGlvbiBXID0gZGlhZyjPgOG1oigx4oiSz4DhtaIpKSB3aGVyZSDPgOG1oiA9IM+DKGbMguG1oikuIFRoZSBNQVAgb3B0aW1pc2F0aW9uIHVzZXMgTmV3dG9uXHUwMDI3cyBtZXRob2QsIGVxdWl2YWxlbnQgdG8gSXRlcmF0aXZlbHkgUmV3ZWlnaHRlZCBMZWFzdCBTcXVhcmVzIChJUkxTKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnNwZWNpYWwgaW1wb3J0IGV4cGl0IGFzIHNpZ21vaWRcbmZyb20gc2NpcHkubGluYWxnIGltcG9ydCBjaG9fZmFjdG9yLCBjaG9fc29sdmVcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBlbGw9MS4wLCBzZjI9MS4wKTpcbiAgICBYMT1ucC5hdGxlYXN0XzJkKFgxKS5yZXNoYXBlKC0xLDEpOyBYMj1ucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLDEpXG4gICAgcmV0dXJuIHNmMipucC5leHAoLTAuNSooWDEtWDIuVCkqKjIvZWxsKioyKVxuXG5kZWYgbGFwbGFjZV9ncF9jbGFzc2lmeShYX3RyLCB5X3RyLCBYX3RlLCBlbGw9MS4wLCBzZjI9MS4wLCBuX2l0ZXI9MjApOlxuICAgIG4gPSBsZW4oeV90cilcbiAgICBLID0gcmJmX2tlcm5lbChYX3RyLCBYX3RyLCBlbGwsIHNmMilcbiAgICBmID0gbnAuemVyb3MobikgICMgaW5pdGlhbGlzZSBsYXRlbnQgdmFsdWVzIGF0IHplcm9cbiAgICBmb3IgXyBpbiByYW5nZShuX2l0ZXIpOlxuICAgICAgICBwaSAgPSBzaWdtb2lkKGYpICAgICAgICAgICAgICAgICAgICAgICAgIyBjbGFzcyBwcm9iYWJpbGl0aWVzXG4gICAgICAgIFcgICA9IHBpKigxIC0gcGkpICAgICAgICAgICAgICAgICAgICAgICAjIEhlc3NpYW4gZGlhZ29uYWxcbiAgICAgICAgV19zcSA9IG5wLnNxcnQoVylcbiAgICAgICAgQiAgID0gbnAuZXllKG4pICsgV19zcVs6LE5vbmVdKksqV19zcVtOb25lLDpdICAjIEkgKyBXXnsxLzJ9IEsgV157MS8yfVxuICAgICAgICBMICAgPSBucC5saW5hbGcuY2hvbGVza3koQilcbiAgICAgICAgYiAgID0gVypmICsgKHlfdHIrMSkvMiAtIHBpICAgICAgICAgICAgIyBncmFkaWVudCBzdGVwIHRhcmdldFxuICAgICAgICBhICAgPSBiIC0gV19zcSpjaG9fc29sdmUoY2hvX2ZhY3RvcihMKSwgV19zcSooS0BiKSlcbiAgICAgICAgZiAgID0gSyBAIGFcbiAgICBwaSAgPSBzaWdtb2lkKGYpXG4gICAgS19zID0gcmJmX2tlcm5lbChYX3RyLCBYX3RlLCBlbGwsIHNmMilcbiAgICBtdV9zID0gS19zLlQgQCAoKHlfdHIrMSkvMiAtIHNpZ21vaWQoZikpICAgIyBwb3N0ZXJpb3IgbWVhbiBhcHByb3hpbWF0aW9uXG4gICAgcGlfc3RhciA9IHNpZ21vaWQobXVfcylcbiAgICByZXR1cm4gcGlfc3RhciwgbXVfc1xuXG5ucC5yYW5kb20uc2VlZCg0MilcblhfdHIgPSBucC5zb3J0KG5wLnJhbmRvbS51bmlmb3JtKC01LDUsMzApKVxueV90ciA9IG5wLnNpZ24obnAuc2luKFhfdHIpICsgMC4yKm5wLnJhbmRvbS5yYW5kbigzMCkpLmFzdHlwZShpbnQpXG5YX3RlID0gbnAubGluc3BhY2UoLTYsNiwyMDApXG5wcm9iLCBfID0gbGFwbGFjZV9ncF9jbGFzc2lmeShYX3RyLCB5X3RyLCBYX3RlKVxuXG5wbHQuZmlndXJlKGZpZ3NpemU9KDEwLDQpKVxucGx0LnBsb3QoWF90ZSwgcHJvYiwgbHc9MiwgbGFiZWw9XHUwMDI3UCh5PSsxfHgqKVx1MDAyNylcbnBsdC5zY2F0dGVyKFhfdHIsICh5X3RyKzEpLzIsIGM9XHUwMDI3clx1MDAyNywgem9yZGVyPTUsIHM9NTAsIGxhYmVsPVx1MDAyN1RyYWluaW5nIGxhYmVsc1x1MDAyNylcbnBsdC5heGhsaW5lKDAuNSwgbHM9XHUwMDI3LS1cdTAwMjcsIGNvbG9yPVx1MDAyN2dyYXlcdTAwMjcpXG5wbHQudGl0bGUoXHUwMDI3R1AgQ2xhc3NpZmljYXRpb24g4oCUIExhcGxhY2UgQXBwcm94aW1hdGlvblx1MDAyNylcbnBsdC54bGFiZWwoXHUwMDI3eFx1MDAyNyk7IHBsdC55bGFiZWwoXHUwMDI3UHJlZGljdGVkIHByb2JhYmlsaXR5XHUwMDI3KTsgcGx0LmxlZ2VuZCgpOyBwbHQuc2hvdygpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkFwcHJveGltYXRpb24gU3RyYXRlZ3kiLCJBY2N1cmFjeSB2cyBFUCIsIkNvc3QiLCJJbXBsZW1lbnRhdGlvbiJdLCJyb3dzIjpbWyJMYXBsYWNlIiwiR2F1c3NpYW4gYXQgTUFQIChtb2RlLW1hdGNoaW5nKSIsIkxvd2VyIOKAlCBtaXNzZXMgc2tldyIsIk8obsKzKSBOZXd0b24gc3RlcHMiLCJNb2RlcmF0ZSDigJQgTmV3dG9uIElSTFMgbG9vcCJdLFsiRVAiLCJHYXVzc2lhbiBtYXRjaGluZyBtb21lbnRzIGl0ZXJhdGl2ZWx5IiwiQmVzdCBhbW9uZyBhcHByb3hpbWF0aW9ucyIsIk8obsKzKSBwZXIgc3dlZXAiLCJDb21wbGV4IOKAlCBjYXZpdHkgZGlzdHJpYnV0aW9ucyJdLFsiVmFyaWF0aW9uYWwgKFNWR1ApIiwiRUxCTyBsb3dlciBib3VuZCwgaW5kdWNpbmcgcG9pbnRzIiwiTW9kZXJhdGUsIHNjYWxhYmxlIiwiTyhubcKyKSDigJQgc2NhbGFibGUiLCJHUHlUb3JjaCBWYXJpYXRpb25hbEdQIl0sWyJNQ01DIChITUMpIiwiR29sZCBzdGFuZGFyZCDigJQgZXhhY3QgYXN5bXB0b3RpY2FsbHkiLCJIaWdoZXN0IChnaXZlbiBlbm91Z2ggc2FtcGxlcykiLCJWZXJ5IGhpZ2giLCJQeXJvIC8gTnVtUHlybyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR1B5VG9yY2ggR1AgQ2xhc3NpZmllciB3aXRoIFZhcmlhdGlvbmFsIEluZmVyZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIEdQIGNsYXNzaWZpY2F0aW9uIGluIEdQeVRvcmNoLCB0aGUgc3RhbmRhcmQgYXBwcm9hY2ggdXNlcyB2YXJpYXRpb25hbCBpbmZlcmVuY2UgKFZhcmlhdGlvbmFsR1ApIHdpdGggYSBCZXJub3VsbGkgbGlrZWxpaG9vZC4gVGhpcyBhdm9pZHMgdGhlIG5vbi1HYXVzc2lhbiBwb3N0ZXJpb3IgcHJvYmxlbSBieSBvcHRpbWlzaW5nIGEgdmFyaWF0aW9uYWwgbG93ZXIgYm91bmQgRUxCTyA9IEVfcVtsb2cgcCh5fGYpXSDiiJIgS0xbcShmKXx8cChmKV0uIEluZHVjaW5nIHBvaW50cyBhcHByb3hpbWF0ZSB0aGUgZnVsbCBHUCwgZ2l2aW5nIE8obm3CsikgY29zdCB3aXRoIG0gaW5kdWNpbmcgcG9pbnRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBncHl0b3JjaFxuZnJvbSBncHl0b3JjaC5tb2RlbHMgaW1wb3J0IEFwcHJveGltYXRlR1BcbmZyb20gZ3B5dG9yY2gudmFyaWF0aW9uYWwgaW1wb3J0IENob2xlc2t5VmFyaWF0aW9uYWxEaXN0cmlidXRpb24sIFZhcmlhdGlvbmFsU3RyYXRlZ3lcbmltcG9ydCBudW1weSBhcyBucFxuXG5jbGFzcyBHUENsYXNzaWZpZXIoQXBwcm94aW1hdGVHUCk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluZHVjaW5nX3BvaW50cyk6XG4gICAgICAgIHZhcl9kaXN0ID0gQ2hvbGVza3lWYXJpYXRpb25hbERpc3RyaWJ1dGlvbihpbmR1Y2luZ19wb2ludHMuc2l6ZSgwKSlcbiAgICAgICAgdmFyX3N0cmF0ID0gVmFyaWF0aW9uYWxTdHJhdGVneShzZWxmLCBpbmR1Y2luZ19wb2ludHMsIHZhcl9kaXN0LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxlYXJuX2luZHVjaW5nX2xvY2F0aW9ucz1UcnVlKVxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHZhcl9zdHJhdClcbiAgICAgICAgc2VsZi5tZWFuX21vZHVsZSAgPSBncHl0b3JjaC5tZWFucy5aZXJvTWVhbigpXG4gICAgICAgIHNlbGYuY292YXJfbW9kdWxlID0gZ3B5dG9yY2gua2VybmVscy5TY2FsZUtlcm5lbChncHl0b3JjaC5rZXJuZWxzLlJCRktlcm5lbCgpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBncHl0b3JjaC5kaXN0cmlidXRpb25zLk11bHRpdmFyaWF0ZU5vcm1hbChcbiAgICAgICAgICAgIHNlbGYubWVhbl9tb2R1bGUoeCksIHNlbGYuY292YXJfbW9kdWxlKHgpKVxuXG5ucC5yYW5kb20uc2VlZCgwKVxuWF9ucCA9IG5wLnNvcnQobnAucmFuZG9tLnVuaWZvcm0oLTUsNSw4MCkpXG55X25wID0gKG5wLnNpbihYX25wKVx1MDAzZTApLmFzdHlwZShmbG9hdClcbnRyYWluX3ggPSB0b3JjaC50ZW5zb3IoWF9ucCwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnRyYWluX3kgPSB0b3JjaC50ZW5zb3IoeV9ucCwgZHR5cGU9dG9yY2guZmxvYXQzMilcbmluZHVjaW5nID0gdG9yY2gubGluc3BhY2UoLTUsNSwyMClcblxubGlrZWxpaG9vZCA9IGdweXRvcmNoLmxpa2VsaWhvb2RzLkJlcm5vdWxsaUxpa2VsaWhvb2QoKVxubW9kZWwgPSBHUENsYXNzaWZpZXIoaW5kdWNpbmcpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKFt7XHUwMDI3cGFyYW1zXHUwMDI3Om1vZGVsLnBhcmFtZXRlcnMoKX0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAge1x1MDAyN3BhcmFtc1x1MDAyNzpsaWtlbGlob29kLnBhcmFtZXRlcnMoKX1dLCBscj0wLjA1KVxubWxsID0gZ3B5dG9yY2gubWxscy5WYXJpYXRpb25hbEVMQk8obGlrZWxpaG9vZCwgbW9kZWwsIG51bV9kYXRhPWxlbih0cmFpbl95KSlcbm1vZGVsLnRyYWluKCk7IGxpa2VsaWhvb2QudHJhaW4oKVxuZm9yIF8gaW4gcmFuZ2UoMjAwKTpcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKCk7IGxvc3M9LW1sbChtb2RlbCh0cmFpbl94KSx0cmFpbl95KTsgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG5cbm1vZGVsLmV2YWwoKTsgbGlrZWxpaG9vZC5ldmFsKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIHRlc3RfeCA9IHRvcmNoLmxpbnNwYWNlKC02LDYsMjAwKVxuICAgIHByb2JzICA9IGxpa2VsaWhvb2QobW9kZWwodGVzdF94KSkucHJvYnNcbnByaW50KFx1MDAyN1ZhcmlhdGlvbmFsIEdQIENsYXNzaWZpZXIgdHJhaW5lZC4gSW5kdWNpbmcgcG9pbnQgbG9jYXRpb25zIGxlYXJuZWQuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4cGVjdGF0aW9uIFByb3BhZ2F0aW9uIHZzIExhcGxhY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV4cGVjdGF0aW9uIFByb3BhZ2F0aW9uIChFUCkgYXBwcm94aW1hdGVzIGVhY2ggbGlrZWxpaG9vZCBmYWN0b3IgcCh54bWifGbhtaIpIHdpdGggYSBHYXVzc2lhbiB04bWiKGbhtaIpID0gWuG1oiBOKGbhtaI7IM684bWiLCDPg+G1osKyKS4gVGhlIEVQIGFsZ29yaXRobSBpdGVyYXRlczogKDEpIGNvbXB1dGUgdGhlIGNhdml0eSBkaXN0cmlidXRpb24gceKCi+G1oiA9IHEvdOG1oiAocmVtb3ZlIG9uZSBzaXRlKSwgKDIpIHByb2plY3QgdGhlIHByb2R1Y3QgceKCi+G1oiDCtyBwKHnhtaJ8ZuG1oikgb250byBhIEdhdXNzaWFuIGJ5IG1hdGNoaW5nIGZpcnN0IHR3byBtb21lbnRzLCAoMykgdXBkYXRlIHThtaIgYWNjb3JkaW5nbHkuIEVQIGNvbnZlcmdlcyB0byBhIEdhdXNzaWFuIGFwcHJveGltYXRpb24gd2hvc2UgbW9tZW50cyBtYXRjaCB0aGUgdHJ1ZSBwb3N0ZXJpb3JcdTAwMjdzIGxvY2FsIG1vbWVudHMg4oCUIG1vcmUgYWNjdXJhdGUgdGhhbiBMYXBsYWNlLCBlc3BlY2lhbGx5IGZvciB1bmJhbGFuY2VkIGNsYXNzIGRpc3RyaWJ1dGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zcGVjaWFsIGltcG9ydCBleHBpdCBhcyBzaWdtb2lkLCBuZHRyXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBub3JtXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbiMgU2ltcGxlIGNvbXBhcmlzb246IExhcGxhY2UgdnMgR2F1c3NpYW4gQ0RGIGxpa2VsaWhvb2QgKHByb2JpdCkgcHJlZGljdGl2ZVxuZGVmIHByb2JpdF9sYXBsYWNlX3ByZWQoZl90ZXN0X21lYW4sIGZfdGVzdF92YXIpOlxuICAgIFwiXCJcIlByZWRpY3RpdmUgcHJvYmFiaWxpdHkgdXNpbmcgTGFwbGFjZSBhcHByb3ggd2l0aCBwcm9iaXQgbGlrZWxpaG9vZC5cIlwiXCJcbiAgICBrYXBwYSA9IDEuMCAvIG5wLnNxcnQoMS4wICsgbnAucGkgKiBmX3Rlc3RfdmFyIC8gOC4wKVxuICAgIHJldHVybiBuZHRyKGthcHBhICogZl90ZXN0X21lYW4pXG5cbmRlZiBwcm9iaXRfZXBfcHJlZChmX3Rlc3RfbWVhbiwgZl90ZXN0X3Zhcik6XG4gICAgXCJcIlwiRVAgcHJlZGljdGl2ZTogaW50ZWdyYXRlIHByb2JpdCBhZ2FpbnN0IE4oZl90ZXN0X21lYW4sIGZfdGVzdF92YXIpLlwiXCJcIlxuICAgICMgRXhhY3QgZm9yIHByb2JpdDogcCh5PTF8eCopID0gzqYozrwvc3FydCgxK8+DwrIpKVxuICAgIHJldHVybiBuZHRyKGZfdGVzdF9tZWFuIC8gbnAuc3FydCgxLjAgKyBmX3Rlc3RfdmFyKSlcblxubGF0ZW50X21lYW5zID0gbnAubGluc3BhY2UoLTMsIDMsIDIwMClcbmZvciBsYXRlbnRfdmFyIGluIFswLjUsIDEuMCwgMi4wXTpcbiAgICBsYXAgPSBwcm9iaXRfbGFwbGFjZV9wcmVkKGxhdGVudF9tZWFucywgbGF0ZW50X3ZhcilcbiAgICBlcCAgPSBwcm9iaXRfZXBfcHJlZChsYXRlbnRfbWVhbnMsICBsYXRlbnRfdmFyKVxuICAgIGRpZmYgPSBucC5tYXgobnAuYWJzKGxhcCAtIGVwKSlcbiAgICBwcmludChmXHUwMDI3TGF0ZW50IHZhcj17bGF0ZW50X3Zhcn06IG1heHxMYXBsYWNlLUVQfCA9IHtkaWZmOi40Zn1cdTAwMjcpXG5cbmZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oOCw0KSlcbmZvciB2LCBjb2wgaW4gWygwLjUsXHUwMDI3Ymx1ZVx1MDAyNyksKDIuMCxcdTAwMjdyZWRcdTAwMjcpXTpcbiAgICB4ID0gbGF0ZW50X21lYW5zXG4gICAgYXgucGxvdCh4LCBwcm9iaXRfbGFwbGFjZV9wcmVkKHgsdiksIGxzPVx1MDAyNy0tXHUwMDI3LCBjb2xvcj1jb2wsIGxhYmVsPWZcdTAwMjdMYXBsYWNlIM+DwrI9e3Z9XHUwMDI3KVxuICAgIGF4LnBsb3QoeCwgcHJvYml0X2VwX3ByZWQoeCx2KSwgICAgICBscz1cdTAwMjctXHUwMDI3LCAgY29sb3I9Y29sLCBsYWJlbD1mXHUwMDI3RVAgz4PCsj17dn1cdTAwMjcpXG5heC5zZXRfeGxhYmVsKFx1MDAyN0xhdGVudCBtZWFuXHUwMDI3KTsgYXguc2V0X3lsYWJlbChcdTAwMjdQKHk9KzEpXHUwMDI3KVxuYXgubGVnZW5kKG5jb2w9Mik7IGF4LnNldF90aXRsZShcdTAwMjdMYXBsYWNlIHZzIEVQIFByZWRpY3RpdmUgUHJvYmFiaWxpdGllcyAocHJvYml0IGxpa2VsaWhvb2QpXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpOyBwbHQuc2hvdygpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkVQIElzIE1vcmUgQWNjdXJhdGUgVGhhbiBMYXBsYWNlIGZvciBDbGFzc2lmaWNhdGlvbiIsImNvbnRlbnQiOiJMYXBsYWNlIGFwcHJveGltYXRpb24gbWF0Y2hlcyB0aGUgcG9zdGVyaW9yIG1vZGUgKE1BUCkgYW5kIGN1cnZhdHVyZSDigJQgaXQgY2FuIGJlIG92ZXItY29uZmlkZW50IHdoZW4gdGhlIHRydWUgcG9zdGVyaW9yIGlzIHNrZXdlZC4gRVAgbWF0Y2hlcyBmaXJzdCBhbmQgc2Vjb25kIG1vbWVudHMgb2YgdGhlIGxvY2FsIGxpa2VsaWhvb2QgYXBwcm94aW1hdGlvbnMgYW5kIGlzIHR5cGljYWxseSBtb3JlIGFjY3VyYXRlLCBlc3BlY2lhbGx5IGZvciBzbWFsbCBkYXRhc2V0cyBvciBpbWJhbGFuY2VkIGNsYXNzZXMuIEZvciBtb3N0IHByYWN0aWNhbCBHUCBjbGFzc2lmaWNhdGlvbiB0YXNrcywgdXNlIEVQIG9yIHZhcmlhdGlvbmFsIGluZmVyZW5jZSBvdmVyIExhcGxhY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktQ2xhc3MgR1AgQ2xhc3NpZmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBLIFx1MDAzZSAyIGNsYXNzZXMsIHRoZSBsaWtlbGlob29kIHAoeT1rfGYpID0gc29mdG1heChmKV9rIHJlcXVpcmVzIEsgbGF0ZW50IEdQIGZ1bmN0aW9ucyDigJQgb25lIHBlciBjbGFzcy4gVGhlIHBvc3RlcmlvciByZW1haW5zIGludHJhY3RhYmxlLiBDb21tb24gYXBwcm9hY2hlczogKDEpIE9uZS12cy1SZXN0IHdpdGggYmluYXJ5IEdQIGNsYXNzaWZpZXJzIChzaW1wbGUgYnV0IGluY29uc2lzdGVudCBwcm9iYWJpbGl0aWVzKSwgKDIpIFNvZnRtYXggbGlrZWxpaG9vZCB3aXRoIExhcGxhY2Ugb3IgRVAgKGNvbnNpc3RlbnQgYnV0IGNvbXBsZXgpLCAoMykgRGlyaWNobGV0IGxpa2VsaWhvb2QgR1AgKG5hdHVyYWxseSBjb21wb3NpdGlvbmFsKS4gR1B5VG9yY2ggc3VwcG9ydHMgRGlyaWNobGV0Q2xhc3NpZmljYXRpb25MaWtlbGlob29kIGZvciBzY2FsYWJsZSBtdWx0aS1jbGFzcyBHUCBjbGFzc2lmaWNhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgZ3B5dG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2lyaXNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuXG5kYXRhID0gbG9hZF9pcmlzKClcblhfbnAsIHlfbnAgPSBkYXRhLmRhdGFbOiw6Ml0sIGRhdGEudGFyZ2V0ICAjIGZpcnN0IDIgZmVhdHVyZXMgZm9yIHZpelxuc2NhbGVyID0gU3RhbmRhcmRTY2FsZXIoKVxuWF9ucCA9IHNjYWxlci5maXRfdHJhbnNmb3JtKFhfbnApXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYX25wLCB5X25wLCB0ZXN0X3NpemU9MC4yLCByYW5kb21fc3RhdGU9NDIpXG5cbnRyYWluX3ggPSB0b3JjaC50ZW5zb3IoWF90ciwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnRyYWluX3kgPSB0b3JjaC50ZW5zb3IoeV90ciwgZHR5cGU9dG9yY2gubG9uZylcbnRlc3RfeCAgPSB0b3JjaC50ZW5zb3IoWF90ZSwgZHR5cGU9dG9yY2guZmxvYXQzMilcblxubGlrZWxpaG9vZCA9IGdweXRvcmNoLmxpa2VsaWhvb2RzLkRpcmljaGxldENsYXNzaWZpY2F0aW9uTGlrZWxpaG9vZChcbiAgICB0cmFpbl95LCBsZWFybl9hZGRpdGlvbmFsX25vaXNlPVRydWUpXG5cbmNsYXNzIE11bHRpY2xhc3NHUChncHl0b3JjaC5tb2RlbHMuRXhhY3RHUCk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpXG4gICAgICAgIHNlbGYubWVhbl9tb2R1bGUgID0gZ3B5dG9yY2gubWVhbnMuQ29uc3RhbnRNZWFuKGJhdGNoX3NoYXBlPXRvcmNoLlNpemUoWzNdKSlcbiAgICAgICAgc2VsZi5jb3Zhcl9tb2R1bGUgPSBncHl0b3JjaC5rZXJuZWxzLlNjYWxlS2VybmVsKFxuICAgICAgICAgICAgZ3B5dG9yY2gua2VybmVscy5SQkZLZXJuZWwoYmF0Y2hfc2hhcGU9dG9yY2guU2l6ZShbM10pKSxcbiAgICAgICAgICAgIGJhdGNoX3NoYXBlPXRvcmNoLlNpemUoWzNdKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIGdweXRvcmNoLmRpc3RyaWJ1dGlvbnMuTXVsdGl2YXJpYXRlTm9ybWFsKFxuICAgICAgICAgICAgc2VsZi5tZWFuX21vZHVsZSh4KSwgc2VsZi5jb3Zhcl9tb2R1bGUoeCkpXG5cbm1vZGVsID0gTXVsdGljbGFzc0dQKHRyYWluX3gsIGxpa2VsaWhvb2QudHJhbnNmb3JtZWRfdGFyZ2V0cywgbGlrZWxpaG9vZClcbm9wdGltaXplciA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0wLjEpXG5tbGwgPSBncHl0b3JjaC5tbGxzLkV4YWN0TWFyZ2luYWxMb2dMaWtlbGlob29kKGxpa2VsaWhvb2QsIG1vZGVsKVxubW9kZWwudHJhaW4oKTsgbGlrZWxpaG9vZC50cmFpbigpXG5mb3IgXyBpbiByYW5nZSgxMDApOlxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgICgtbWxsKG1vZGVsKHRyYWluX3gpLCBsaWtlbGlob29kLnRyYW5zZm9ybWVkX3RhcmdldHMpKS5iYWNrd2FyZCgpXG4gICAgb3B0aW1pemVyLnN0ZXAoKVxucHJpbnQoXHUwMDI3RGlyaWNobGV0IEdQIG11bHRpLWNsYXNzIG1vZGVsIHRyYWluZWQgb24gSXJpcyAoMyBjbGFzc2VzKS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR1AgY2xhc3NpZmljYXRpb24gcmVxdWlyZXMgYXBwcm94aW1hdGlvbnMgYmVjYXVzZSB0aGUgc2lnbW9pZC9zb2Z0bWF4IGxpa2VsaWhvb2QgbWFrZXMgdGhlIHBvc3RlcmlvciBub24tR2F1c3NpYW4uIExhcGxhY2UgYXBwcm94aW1hdGlvbiBpcyBzaW1wbGUgYW5kIGZhc3Q6IEdhdXNzaWFuIGNlbnRyZWQgYXQgdGhlIE1BUCB3aXRoIGN1cnZhdHVyZSBmcm9tIHRoZSBIZXNzaWFuIFcgPSBkaWFnKM+A4bWiKDHiiJLPgOG1oikpLiBFUCBpdGVyYXRpdmVseSBtYXRjaGVzIG1vbWVudHMgb2YgbG9jYWwgbGlrZWxpaG9vZCBhcHByb3hpbWF0aW9ucyBhbmQgaXMgbW9yZSBhY2N1cmF0ZSB0aGFuIExhcGxhY2UuIFZhcmlhdGlvbmFsIGluZmVyZW5jZSAoU1ZHUCkgc2NhbGVzIHRvIGxhcmdlIGRhdGFzZXRzIHZpYSBpbmR1Y2luZyBwb2ludHMuIE11bHRpLWNsYXNzIGNsYXNzaWZpY2F0aW9uIHVzZXMgSyBsYXRlbnQgR1BzIHdpdGggRGlyaWNobGV0IG9yIHNvZnRtYXggbGlrZWxpaG9vZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdQIGNsYXNzaWZpY2F0aW9uOiBwKHl8Zik9z4MoeWYpIGlzIG5vbi1HYXVzc2lhbiDihpIgYXBwcm94aW1hdGUgcG9zdGVyaW9yIHJlcXVpcmVkIiwiTGFwbGFjZTogR2F1c3NpYW4gYXQgTUFQOyBXPWRpYWcoz4AoMS3PgCkpIGZyb20gc2lnbW9pZDsgSVJMUyBOZXd0b24gc3RlcHMiLCJFUDogY2F2aXR5IGRpc3RyaWJ1dGlvbiB1cGRhdGUsIG1vbWVudC1tYXRjaGluZzsgbW9yZSBhY2N1cmF0ZSB0aGFuIExhcGxhY2UiLCJWYXJpYXRpb25hbCAoU1ZHUCk6IEVMQk8gb3B0aW1pc2F0aW9uIHdpdGggbSBpbmR1Y2luZyBwb2ludHM7IE8obm3CsikgY29zdCIsIk11bHRpLWNsYXNzOiBLIGxhdGVudCBHUHMgKyBzb2Z0bWF4L0RpcmljaGxldCBsaWtlbGlob29kOyBvbmUtdnMtcmVzdCBhcyBiYXNlbGluZSIsIkdQeVRvcmNoOiBEaXJpY2hsZXRDbGFzc2lmaWNhdGlvbkxpa2VsaWhvb2QgZm9yIHNjYWxhYmxlIG11bHRpLWNsYXNzIEdQIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUHJlZGljdGl2ZSBQcm9iYWJpbGl0eSB2cyBMYXRlbnQgTWVhbiIsImNvbnRlbnQiOiJUaGUgR1AgY2xhc3NpZmllciBvdXRwdXRzIGEgbGF0ZW50IG1lYW4gZiooeCkg4oiIIOKEnS4gVGhlIHByZWRpY3RpdmUgcHJvYmFiaWxpdHkgUCh5PSsxfHgqKSByZXF1aXJlcyBpbnRlZ3JhdGluZyDPgyhmKikgb3ZlciB0aGUgcG9zdGVyaW9yIHVuY2VydGFpbnR5IGluIGYqLiBUaGlzIGludGVncmFsIGlzIGFwcHJveGltYXRlZCBhcyDPgyjOusK3zrwqKSB3aGVyZSDOuj0oMSvPgM+DwrIqLzgpXnstMS8yfSBpbiB0aGUgTGFwbGFjZSBjYXNlLiBJZ25vcmluZyBwb3N0ZXJpb3IgdW5jZXJ0YWludHkgYW5kIHVzaW5nIM+DKM68KikgYWxvbmUgcHJvZHVjZXMgb3Zlci1jb25maWRlbnQgcHJvYmFiaWxpdGllcy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# GP Classification — Laplace Approximation and EP

## Why GP Classification Is Harder

For classification the likelihood p(y|f) = σ(y·f) where σ is the sigmoid function is non-Gaussian. The posterior p(f|X,y) ∝ p(y|f)p(f|X) is no longer Gaussian — it has no closed form. We need approximations. Three families are standard: (1) Laplace approximation — Gaussian centred at the MAP estimate; (2) Expectation Propagation (EP) — moment-matching approximation; (3) variational inference — optimise a lower bound on the marginal likelihood. Each trades off accuracy, cost, and implementation complexity.

- GP regression: Gaussian likelihood → closed-form posterior GP
- GP classification: sigmoid/softmax likelihood → intractable posterior
- Laplace: fastest, mode-matching Gaussian approximation at MAP
- EP: more accurate, moment-matching, iterative cavity updates
- Variational (SVGP): scalable to large n via inducing points and ELBO
- MCMC (HMC/NUTS): gold standard accuracy but very high computational cost

## Laplace Approximation via Newton's Method

The Laplace approximation (1) finds the MAP estimate f̂ = argmax log p(f|X,y) = argmax [log p(y|f) − ½ fᵀ K⁻¹ f], (2) approximates the posterior with a Gaussian centred at f̂ with covariance (K⁻¹ + W)⁻¹ where W = −∇∇ log p(y|f̂) is the negative Hessian of the log likelihood. For binary classification W = diag(πᵢ(1−πᵢ)) where πᵢ = σ(f̂ᵢ). The MAP optimisation uses Newton's method, equivalent to Iteratively Reweighted Least Squares (IRLS).

```python
import numpy as np
from scipy.special import expit as sigmoid
from scipy.linalg import cho_factor, cho_solve
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1=np.atleast_2d(X1).reshape(-1,1); X2=np.atleast_2d(X2).reshape(-1,1)
    return sf2*np.exp(-0.5*(X1-X2.T)**2/ell**2)

def laplace_gp_classify(X_tr, y_tr, X_te, ell=1.0, sf2=1.0, n_iter=20):
    n = len(y_tr)
    K = rbf_kernel(X_tr, X_tr, ell, sf2)
    f = np.zeros(n)  # initialise latent values at zero
    for _ in range(n_iter):
        pi  = sigmoid(f)                        # class probabilities
        W   = pi*(1 - pi)                       # Hessian diagonal
        W_sq = np.sqrt(W)
        B   = np.eye(n) + W_sq[:,None]*K*W_sq[None,:]  # I + W^{1/2} K W^{1/2}
        L   = np.linalg.cholesky(B)
        b   = W*f + (y_tr+1)/2 - pi            # gradient step target
        a   = b - W_sq*cho_solve(cho_factor(L), W_sq*(K@b))
        f   = K @ a
    pi  = sigmoid(f)
    K_s = rbf_kernel(X_tr, X_te, ell, sf2)
    mu_s = K_s.T @ ((y_tr+1)/2 - sigmoid(f))   # posterior mean approximation
    pi_star = sigmoid(mu_s)
    return pi_star, mu_s

np.random.seed(42)
X_tr = np.sort(np.random.uniform(-5,5,30))
y_tr = np.sign(np.sin(X_tr) + 0.2*np.random.randn(30)).astype(int)
X_te = np.linspace(-6,6,200)
prob, _ = laplace_gp_classify(X_tr, y_tr, X_te)

plt.figure(figsize=(10,4))
plt.plot(X_te, prob, lw=2, label='P(y=+1|x*)')
plt.scatter(X_tr, (y_tr+1)/2, c='r', zorder=5, s=50, label='Training labels')
plt.axhline(0.5, ls='--', color='gray')
plt.title('GP Classification — Laplace Approximation')
plt.xlabel('x'); plt.ylabel('Predicted probability'); plt.legend(); plt.show()
```

| Method | Approximation Strategy | Accuracy vs EP | Cost | Implementation |
| --- | --- | --- | --- | --- |
| Laplace | Gaussian at MAP (mode-matching) | Lower — misses skew | O(n³) Newton steps | Moderate — Newton IRLS loop |
| EP | Gaussian matching moments iteratively | Best among approximations | O(n³) per sweep | Complex — cavity distributions |
| Variational (SVGP) | ELBO lower bound, inducing points | Moderate, scalable | O(nm²) — scalable | GPyTorch VariationalGP |
| MCMC (HMC) | Gold standard — exact asymptotically | Highest (given enough samples) | Very high | Pyro / NumPyro |

## GPyTorch GP Classifier with Variational Inference

For GP classification in GPyTorch, the standard approach uses variational inference (VariationalGP) with a Bernoulli likelihood. This avoids the non-Gaussian posterior problem by optimising a variational lower bound ELBO = E_q[log p(y|f)] − KL[q(f)||p(f)]. Inducing points approximate the full GP, giving O(nm²) cost with m inducing points.

```python
import torch
import gpytorch
from gpytorch.models import ApproximateGP
from gpytorch.variational import CholeskyVariationalDistribution, VariationalStrategy
import numpy as np

class GPClassifier(ApproximateGP):
    def __init__(self, inducing_points):
        var_dist = CholeskyVariationalDistribution(inducing_points.size(0))
        var_strat = VariationalStrategy(self, inducing_points, var_dist,
                                        learn_inducing_locations=True)
        super().__init__(var_strat)
        self.mean_module  = gpytorch.means.ZeroMean()
        self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())

    def forward(self, x):
        return gpytorch.distributions.MultivariateNormal(
            self.mean_module(x), self.covar_module(x))

np.random.seed(0)
X_np = np.sort(np.random.uniform(-5,5,80))
y_np = (np.sin(X_np)>0).astype(float)
train_x = torch.tensor(X_np, dtype=torch.float32)
train_y = torch.tensor(y_np, dtype=torch.float32)
inducing = torch.linspace(-5,5,20)

likelihood = gpytorch.likelihoods.BernoulliLikelihood()
model = GPClassifier(inducing)
optimizer = torch.optim.Adam([{'params':model.parameters()},
                               {'params':likelihood.parameters()}], lr=0.05)
mll = gpytorch.mlls.VariationalELBO(likelihood, model, num_data=len(train_y))
model.train(); likelihood.train()
for _ in range(200):
    optimizer.zero_grad(); loss=-mll(model(train_x),train_y); loss.backward(); optimizer.step()

model.eval(); likelihood.eval()
with torch.no_grad():
    test_x = torch.linspace(-6,6,200)
    probs  = likelihood(model(test_x)).probs
print('Variational GP Classifier trained. Inducing point locations learned.')
```

## Expectation Propagation vs Laplace

Expectation Propagation (EP) approximates each likelihood factor p(yᵢ|fᵢ) with a Gaussian tᵢ(fᵢ) = Zᵢ N(fᵢ; μᵢ, σᵢ²). The EP algorithm iterates: (1) compute the cavity distribution q₋ᵢ = q/tᵢ (remove one site), (2) project the product q₋ᵢ · p(yᵢ|fᵢ) onto a Gaussian by matching first two moments, (3) update tᵢ accordingly. EP converges to a Gaussian approximation whose moments match the true posterior's local moments — more accurate than Laplace, especially for unbalanced class distributions.

```python
import numpy as np
from scipy.special import expit as sigmoid, ndtr
from scipy.stats import norm
import matplotlib.pyplot as plt

# Simple comparison: Laplace vs Gaussian CDF likelihood (probit) predictive
def probit_laplace_pred(f_test_mean, f_test_var):
    """Predictive probability using Laplace approx with probit likelihood."""
    kappa = 1.0 / np.sqrt(1.0 + np.pi * f_test_var / 8.0)
    return ndtr(kappa * f_test_mean)

def probit_ep_pred(f_test_mean, f_test_var):
    """EP predictive: integrate probit against N(f_test_mean, f_test_var)."""
    # Exact for probit: p(y=1|x*) = Φ(μ/sqrt(1+σ²))
    return ndtr(f_test_mean / np.sqrt(1.0 + f_test_var))

latent_means = np.linspace(-3, 3, 200)
for latent_var in [0.5, 1.0, 2.0]:
    lap = probit_laplace_pred(latent_means, latent_var)
    ep  = probit_ep_pred(latent_means,  latent_var)
    diff = np.max(np.abs(lap - ep))
    print(f'Latent var={latent_var}: max|Laplace-EP| = {diff:.4f}')

fig, ax = plt.subplots(figsize=(8,4))
for v, col in [(0.5,'blue'),(2.0,'red')]:
    x = latent_means
    ax.plot(x, probit_laplace_pred(x,v), ls='--', color=col, label=f'Laplace σ²={v}')
    ax.plot(x, probit_ep_pred(x,v),      ls='-',  color=col, label=f'EP σ²={v}')
ax.set_xlabel('Latent mean'); ax.set_ylabel('P(y=+1)')
ax.legend(ncol=2); ax.set_title('Laplace vs EP Predictive Probabilities (probit likelihood)')
plt.tight_layout(); plt.show()
```

> **EP Is More Accurate Than Laplace for Classification**: Laplace approximation matches the posterior mode (MAP) and curvature — it can be over-confident when the true posterior is skewed. EP matches first and second moments of the local likelihood approximations and is typically more accurate, especially for small datasets or imbalanced classes. For most practical GP classification tasks, use EP or variational inference over Laplace.

## Multi-Class GP Classification

For K > 2 classes, the likelihood p(y=k|f) = softmax(f)_k requires K latent GP functions — one per class. The posterior remains intractable. Common approaches: (1) One-vs-Rest with binary GP classifiers (simple but inconsistent probabilities), (2) Softmax likelihood with Laplace or EP (consistent but complex), (3) Dirichlet likelihood GP (naturally compositional). GPyTorch supports DirichletClassificationLikelihood for scalable multi-class GP classification.

```python
import torch
import gpytorch
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = load_iris()
X_np, y_np = data.data[:,:2], data.target  # first 2 features for viz
scaler = StandardScaler()
X_np = scaler.fit_transform(X_np)
X_tr, X_te, y_tr, y_te = train_test_split(X_np, y_np, test_size=0.2, random_state=42)

train_x = torch.tensor(X_tr, dtype=torch.float32)
train_y = torch.tensor(y_tr, dtype=torch.long)
test_x  = torch.tensor(X_te, dtype=torch.float32)

likelihood = gpytorch.likelihoods.DirichletClassificationLikelihood(
    train_y, learn_additional_noise=True)

class MulticlassGP(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood):
        super().__init__(train_x, train_y, likelihood)
        self.mean_module  = gpytorch.means.ConstantMean(batch_shape=torch.Size([3]))
        self.covar_module = gpytorch.kernels.ScaleKernel(
            gpytorch.kernels.RBFKernel(batch_shape=torch.Size([3])),
            batch_shape=torch.Size([3]))
    def forward(self, x):
        return gpytorch.distributions.MultivariateNormal(
            self.mean_module(x), self.covar_module(x))

model = MulticlassGP(train_x, likelihood.transformed_targets, likelihood)
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
model.train(); likelihood.train()
for _ in range(100):
    optimizer.zero_grad()
    (-mll(model(train_x), likelihood.transformed_targets)).backward()
    optimizer.step()
print('Dirichlet GP multi-class model trained on Iris (3 classes).')
```

## Key Takeaways

GP classification requires approximations because the sigmoid/softmax likelihood makes the posterior non-Gaussian. Laplace approximation is simple and fast: Gaussian centred at the MAP with curvature from the Hessian W = diag(πᵢ(1−πᵢ)). EP iteratively matches moments of local likelihood approximations and is more accurate than Laplace. Variational inference (SVGP) scales to large datasets via inducing points. Multi-class classification uses K latent GPs with Dirichlet or softmax likelihood.

- GP classification: p(y|f)=σ(yf) is non-Gaussian → approximate posterior required
- Laplace: Gaussian at MAP; W=diag(π(1-π)) from sigmoid; IRLS Newton steps
- EP: cavity distribution update, moment-matching; more accurate than Laplace
- Variational (SVGP): ELBO optimisation with m inducing points; O(nm²) cost
- Multi-class: K latent GPs + softmax/Dirichlet likelihood; one-vs-rest as baseline
- GPyTorch: DirichletClassificationLikelihood for scalable multi-class GP

> **Predictive Probability vs Latent Mean**: The GP classifier outputs a latent mean f*(x) ∈ ℝ. The predictive probability P(y=+1|x*) requires integrating σ(f*) over the posterior uncertainty in f*. This integral is approximated as σ(κ·μ*) where κ=(1+πσ²*/8)^{-1/2} in the Laplace case. Ignoring posterior uncertainty and using σ(μ*) alone produces over-confident probabilities.

---

