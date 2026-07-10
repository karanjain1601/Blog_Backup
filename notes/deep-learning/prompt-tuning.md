---
title: "Prompt Tuning — Soft Prompts at Input Embeddings and Scale-Dependent Behavior"
slug: "prompt-tuning"
description: "Prompt tuning (Lester et al., 2021) prepends P learned soft prompt tokens only at the input embedding layer. Covers the embedding math, scale dependence (competitive with full fine-tuning only at 10B+ params), initialization strategies, multi-task inference, and comparison with prefix tuning."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJvbXB0IHR1bmluZyAoTGVzdGVyIGV0IGFsLiwgMjAyMSkgaXMgYSBwYXJhbWV0ZXItZWZmaWNpZW50IGZpbmUtdHVuaW5nIG1ldGhvZCB0aGF0IHByZXBlbmRzIFAgbGVhcm5lZCBzb2Z0IHByb21wdCB0b2tlbiBlbWJlZGRpbmdzIHRvIHRoZSBpbnB1dCBlbWJlZGRpbmcgc2VxdWVuY2UuIFVubGlrZSBkaXNjcmV0ZSBwcm9tcHRzIChtYW51YWxseSB3cml0dGVuIHRleHQpLCBzb2Z0IHByb21wdHMgYXJlIGNvbnRpbnVvdXMgdmVjdG9ycyBpbiB0aGUgZW1iZWRkaW5nIHNwYWNlIHRoYXQgYXJlIG9wdGltaXplZCBkaXJlY3RseSBieSBncmFkaWVudCBkZXNjZW50LiBUaGUgZW50aXJlIHRyYW5zZm9ybWVyIGlzIGZyb3plbjsgb25seSB0aGUgUMOXZF9lbWIgcHJvbXB0IGVtYmVkZGluZyBtYXRyaXggaXMgdHJhaW5lZC4gVGhpcyBtYWtlcyBwcm9tcHQgdHVuaW5nIG9uZSBvZiB0aGUgbW9zdCBtaW5pbWFsIFBFRlQgYXBwcm9hY2hlczogbm8gbmV3IGxheWVycywgbm8gd2VpZ2h0IGRlY29tcG9zaXRpb25zLCBqdXN0IGEgc21hbGwgbGVhcm5lZCBwcmVmaXggYXBwZW5kZWQgdG8gZXZlcnkgaW5wdXQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU29mdCBQcm9tcHQgRW1iZWRkaW5nIE1hdGgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxldCBFX2lucHV0IOKIiCDihJ1eKEzDl2RfZW1iKSBiZSB0aGUgdG9rZW4gZW1iZWRkaW5ncyBmb3IgYW4gaW5wdXQgc2VxdWVuY2Ugb2YgbGVuZ3RoIEwuIFByb21wdCB0dW5pbmcgaW50cm9kdWNlcyBhIGxlYXJuYWJsZSBtYXRyaXggRV9wcm9tcHQg4oiIIOKEnV4oUMOXZF9lbWIpIHdoZXJlIFAgaXMgdGhlIHByb21wdCBsZW5ndGggKHR5cGljYWxseSAx4oCTMTAwIHRva2VucykuIFRoZSBmdWxsIGlucHV0IHRvIHRoZSB0cmFuc2Zvcm1lciBpcyBjb25jYXQoRV9wcm9tcHQsIEVfaW5wdXQpIOKIiCDihJ1eKChQK0wpw5dkX2VtYikuIFRoZSB0cmFuc2Zvcm1lciBwcm9jZXNzZXMgdGhpcyBjb25jYXRlbmF0ZWQgc2VxdWVuY2Ugd2l0aCBpdHMgZnJvemVuIHdlaWdodHMuIEJhY2twcm9wYWdhdGlvbiBmbG93cyB0aHJvdWdoIHRoZSBmcm96ZW4gdHJhbnNmb3JtZXIgbGF5ZXJzIGJhY2sgdG8gRV9wcm9tcHQuIFRoZSBncmFkaWVudCDiiIJML+KIgkVfcHJvbXB0IGlzIHdlbGwtZGVmaW5lZCBhbmQgZGVuc2Ug4oCUIGV2ZXJ5IGZvcndhcmQgcGFzcyB1cGRhdGVzIGFsbCBQw5dkX2VtYiB2YWx1ZXMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmFpbmFibGUgcGFyYW1ldGVyIGNvdW50OiBmb3IgUD0xMDAgYW5kIGRfZW1iPTEwMjQgKFQ1LUxhcmdlKSwgdGhlIHByb21wdCBtYXRyaXggY29udGFpbnMgMTAww5cxMDI0ID0gMTAyLDQwMCBwYXJhbWV0ZXJzIOKAlCByb3VnaGx5IDAuMDElIG9mIFQ1LUxhcmdlXHUwMDI3cyA3NzBNIHBhcmFtZXRlcnMuIFRoaXMgaXMgMTDigJMxMDDDlyBmZXdlciB0cmFpbmFibGUgcGFyYW1ldGVycyB0aGFuIHByZWZpeCB0dW5pbmcsIHdoaWNoIGluc2VydHMgbGVhcm5lZCBrZXktdmFsdWUgcGFpcnMgYXQgZXZlcnkgYXR0ZW50aW9uIGxheWVyLiBQcm9tcHQgdHVuaW5nIGlzIGlucHV0LW9ubHk7IHByZWZpeCB0dW5pbmcgaXMgcGVyLWxheWVyLiBUaGUgcmVkdWN0aW9uIGluIHRyYWluYWJsZSBwYXJhbWV0ZXJzIGNvbWVzIGF0IGEgY29zdDogd2l0aCBvbmx5IGlucHV0LWxheWVyIGluZmx1ZW5jZSwgdGhlIHNvZnQgcHJvbXB0cyBtdXN0IGVuY29kZSBhbGwgdGFzay1zcGVjaWZpYyBpbmZvcm1hdGlvbiB0aHJvdWdoIHRoZSBmcm96ZW4gbW9kZWxcdTAwMjdzIG93biByZXByZXNlbnRhdGlvbmFsIGNhcGFjaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNvZnQgUHJvbXB0IEVtYmVkZGluZyBJbXBsZW1lbnRhdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbCwgQXV0b1Rva2VuaXplclxuXG5jbGFzcyBTb2Z0UHJvbXB0TW9kZWwobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJXcmFwcyBhIGZyb3plbiB0cmFuc2Zvcm1lciB3aXRoIGEgbGVhcm5hYmxlIHNvZnQgcHJvbXB0IHByZWZpeC5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBtb2RlbF9uYW1lOiBzdHIsIHByb21wdF9sZW5ndGg6IGludCA9IDIwKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmFja2JvbmUgPSBBdXRvTW9kZWwuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG4gICAgICAgIGZvciBwYXJhbSBpbiBzZWxmLmJhY2tib25lLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgICAgIHBhcmFtLnJlcXVpcmVzX2dyYWQgPSBGYWxzZVxuICAgICAgICBkX2VtYiA9IHNlbGYuYmFja2JvbmUuY29uZmlnLmhpZGRlbl9zaXplXG4gICAgICAgIHNlbGYucHJvbXB0X2xlbmd0aCA9IHByb21wdF9sZW5ndGhcbiAgICAgICAgIyBMZWFybmFibGUgc29mdCBwcm9tcHQgZW1iZWRkaW5nczogc2hhcGUgKFAsIGRfZW1iKVxuICAgICAgICBzZWxmLnNvZnRfcHJvbXB0ID0gbm4uUGFyYW1ldGVyKFxuICAgICAgICAgICAgdG9yY2gucmFuZG4ocHJvbXB0X2xlbmd0aCwgZF9lbWIpICogMC4wMlxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBpbnB1dF9pZHM6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICBhdHRlbnRpb25fbWFzazogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgYnN6ID0gaW5wdXRfaWRzLnNoYXBlWzBdXG4gICAgICAgIHRva2VuX2VtYmVkcyA9IHNlbGYuYmFja2JvbmUuZ2V0X2lucHV0X2VtYmVkZGluZ3MoKShpbnB1dF9pZHMpXG4gICAgICAgIHByb21wdF9lbWJlZHMgPSBzZWxmLnNvZnRfcHJvbXB0LnVuc3F1ZWV6ZSgwKS5leHBhbmQoYnN6LCAtMSwgLTEpXG4gICAgICAgIGZ1bGxfZW1iZWRzID0gdG9yY2guY2F0KFtwcm9tcHRfZW1iZWRzLCB0b2tlbl9lbWJlZHNdLCBkaW09MSlcbiAgICAgICAgcHJvbXB0X21hc2sgPSB0b3JjaC5vbmVzKGJzeiwgc2VsZi5wcm9tcHRfbGVuZ3RoLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGV2aWNlPWF0dGVudGlvbl9tYXNrLmRldmljZSlcbiAgICAgICAgZnVsbF9tYXNrID0gdG9yY2guY2F0KFtwcm9tcHRfbWFzaywgYXR0ZW50aW9uX21hc2tdLCBkaW09MSlcbiAgICAgICAgb3V0cHV0cyA9IHNlbGYuYmFja2JvbmUoaW5wdXRzX2VtYmVkcz1mdWxsX2VtYmVkcyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYXR0ZW50aW9uX21hc2s9ZnVsbF9tYXNrKVxuICAgICAgICByZXR1cm4gb3V0cHV0cy5sYXN0X2hpZGRlbl9zdGF0ZVxuXG4gICAgZGVmIHRyYWluYWJsZV9wYXJhbXMoc2VsZik6XG4gICAgICAgIHJldHVybiBzdW0ocC5udW1lbCgpIGZvciBwIGluIHNlbGYucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZClcblxubW9kZWwgPSBTb2Z0UHJvbXB0TW9kZWwoXHUwMDI3YmVydC1iYXNlLXVuY2FzZWRcdTAwMjcsIHByb21wdF9sZW5ndGg9MjApXG5wcmludChmXHUwMDI3VHJhaW5hYmxlIHBhcmFtczoge21vZGVsLnRyYWluYWJsZV9wYXJhbXMoKTosfVx1MDAyNykgICMgb25seSBzb2Z0IHByb21wdFxucHJpbnQoZlx1MDAyN1NvZnQgcHJvbXB0IHNoYXBlOiB7bW9kZWwuc29mdF9wcm9tcHQuc2hhcGV9XHUwMDI3KSAgICAjICgyMCwgNzY4KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByb21wdCBUdW5pbmcgd2l0aCBUNSB2aWEgUEVGVCJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBUNUZvckNvbmRpdGlvbmFsR2VuZXJhdGlvbiwgVDVUb2tlbml6ZXJcbmZyb20gcGVmdCBpbXBvcnQgUHJvbXB0VHVuaW5nQ29uZmlnLCBQcm9tcHRUdW5pbmdJbml0LCBnZXRfcGVmdF9tb2RlbCwgVGFza1R5cGVcblxuZGVmIHNldHVwX3Q1X3Byb21wdF90dW5pbmcobW9kZWxfbmFtZTogc3RyID0gXHUwMDI3dDUtbGFyZ2VcdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBudW1fdmlydHVhbF90b2tlbnM6IGludCA9IDEwMCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIGluaXRfdGV4dDogc3RyID0gXHUwMDI3Q2xhc3NpZnkgc2VudGltZW50Olx1MDAyNyk6XG4gICAgXCJcIlwiQ29uZmlndXJlIFQ1IGZvciBwcm9tcHQgdHVuaW5nIG9uIGEgY2xhc3NpZmljYXRpb24gdGFzay5cIlwiXCJcbiAgICBiYXNlX21vZGVsID0gVDVGb3JDb25kaXRpb25hbEdlbmVyYXRpb24uZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG4gICAgcGVmdF9jb25maWcgPSBQcm9tcHRUdW5pbmdDb25maWcoXG4gICAgICAgIHRhc2tfdHlwZT1UYXNrVHlwZS5TRVFfMl9TRVFfTE0sXG4gICAgICAgIHByb21wdF90dW5pbmdfaW5pdD1Qcm9tcHRUdW5pbmdJbml0LlRFWFQsXG4gICAgICAgIG51bV92aXJ0dWFsX3Rva2Vucz1udW1fdmlydHVhbF90b2tlbnMsXG4gICAgICAgIHByb21wdF90dW5pbmdfaW5pdF90ZXh0PWluaXRfdGV4dCxcbiAgICAgICAgdG9rZW5pemVyX25hbWVfb3JfcGF0aD1tb2RlbF9uYW1lLFxuICAgIClcbiAgICBtb2RlbCA9IGdldF9wZWZ0X21vZGVsKGJhc2VfbW9kZWwsIHBlZnRfY29uZmlnKVxuICAgIG1vZGVsLnByaW50X3RyYWluYWJsZV9wYXJhbWV0ZXJzKCkgICMgfjEwMksgLyA3NzBNIGZvciBUNS1MYXJnZVxuICAgIHJldHVybiBtb2RlbFxuXG5kZWYgcnVuX3Byb21wdF90dW5pbmdfZGVtbygpOlxuICAgIG1vZGVsID0gc2V0dXBfdDVfcHJvbXB0X3R1bmluZyhudW1fdmlydHVhbF90b2tlbnM9NTApXG4gICAgdG9rZW5pemVyID0gVDVUb2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFx1MDAyN3Q1LWxhcmdlXHUwMDI3KVxuICAgIHNhbXBsZSA9IFx1MDAyN1RoZSBtb3ZpZSB3YXMgYWJzb2x1dGVseSBmYW50YXN0aWMgYW5kIEkgbG92ZWQgZXZlcnkgbW9tZW50Llx1MDAyN1xuICAgIGlucHV0cyA9IHRva2VuaXplcihzYW1wbGUsIHJldHVybl90ZW5zb3JzPVx1MDAyN3B0XHUwMDI3LCB0cnVuY2F0aW9uPVRydWUsIG1heF9sZW5ndGg9MTI4KVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBvdXRwdXRfaWRzID0gbW9kZWwuZ2VuZXJhdGUoKippbnB1dHMsIG1heF9uZXdfdG9rZW5zPTUpXG4gICAgcHJpbnQoZlx1MDAyN0lucHV0OiB7c2FtcGxlfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3T3V0cHV0OiB7dG9rZW5pemVyLmRlY29kZShvdXRwdXRfaWRzWzBdLCBza2lwX3NwZWNpYWxfdG9rZW5zPVRydWUpfVx1MDAyNylcblxucHJpbnQoXHUwMDI3UHJvbXB0IHR1bmluZyBjb25maWcgcmVhZHkg4oCUIG9ubHkgc29mdF9wcm9tcHQgcGFyYW1zIHJlY2VpdmUgZ3JhZGllbnRzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbml0aWFsaXphdGlvbiBTdHJhdGVnaWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgaW5pdGlhbCB2YWx1ZXMgb2YgRV9wcm9tcHQgc2lnbmlmaWNhbnRseSBhZmZlY3QgY29udmVyZ2VuY2Ugc3BlZWQuIFRocmVlIHN0cmF0ZWdpZXMgYXJlIGNvbXBhcmVkOiAoMSkgcmFuZG9tIGluaXRpYWxpemF0aW9uIGZyb20gTigwLCAwLjAyKSDigJQgaGlnaCB2YXJpYW5jZSBhY3Jvc3MgcnVuczsgKDIpIHZvY2FidWxhcnkgdG9rZW4gaW5pdGlhbGl6YXRpb24g4oCUIHNhbXBsZSBQIHRva2VucyBmcm9tIHRoZSBtb2RlbFx1MDAyN3Mgdm9jYWJ1bGFyeSBlbWJlZGRpbmcgbWF0cml4LCBwcm92aWRpbmcgbWVhbmluZ2Z1bCBzdGFydGluZyBwb2ludHM7ICgzKSBjbGFzcyBsYWJlbCBpbml0aWFsaXphdGlvbiDigJQgZm9yIGNsYXNzaWZpY2F0aW9uIHRhc2tzLCBpbml0aWFsaXplIGZyb20gZW1iZWRkaW5ncyBvZiB0YXJnZXQgY2xhc3MgbGFiZWwgc3RyaW5ncyAoZS5nLiwgXHUwMDI3cG9zaXRpdmVcdTAwMjcsIFx1MDAyN25lZ2F0aXZlXHUwMDI3KS4gQ2xhc3MgbGFiZWwgaW5pdCBjb252ZXJnZXMgZmFzdGVzdCBhbmQgc2hvd3MgbG93ZXN0IHZhcmlhbmNlLCBwYXJ0aWN1bGFybHkgYXQgc3ViLTFCIHNjYWxlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXIsIEF1dG9Nb2RlbFxuXG5kZWYgaW5pdGlhbGl6ZV9zb2Z0X3Byb21wdChtb2RlbF9uYW1lOiBzdHIsIHByb21wdF9sZW5ndGg6IGludCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0cmF0ZWd5OiBzdHIgPSBcdTAwMjdyYW5kb21cdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBjbGFzc19sYWJlbHM6IGxpc3QgPSBOb25lKSAtXHUwMDNlIG5uLlBhcmFtZXRlcjpcbiAgICBcIlwiXCJcbiAgICBJbml0aWFsaXplIHNvZnQgcHJvbXB0IGVtYmVkZGluZ3Mgd2l0aCB0aHJlZSBzdHJhdGVnaWVzLlxuICAgIHN0cmF0ZWd5OiBcdTAwMjdyYW5kb21cdTAwMjcgfCBcdTAwMjd2b2NhYlx1MDAyNyB8IFx1MDAyN2NsYXNzX2xhYmVsXHUwMDI3XG4gICAgXCJcIlwiXG4gICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSlcbiAgICBtb2RlbCA9IEF1dG9Nb2RlbC5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSlcbiAgICBlbWJlZF9sYXllciA9IG1vZGVsLmdldF9pbnB1dF9lbWJlZGRpbmdzKClcbiAgICBkX2VtYiA9IGVtYmVkX2xheWVyLmVtYmVkZGluZ19kaW1cbiAgICB2b2NhYl9lbWJlZGRpbmdzID0gZW1iZWRfbGF5ZXIud2VpZ2h0LmRhdGEgICMgKFYsIGRfZW1iKVxuXG4gICAgaWYgc3RyYXRlZ3kgPT0gXHUwMDI3cmFuZG9tXHUwMDI3OlxuICAgICAgICBpbml0ID0gdG9yY2gucmFuZG4ocHJvbXB0X2xlbmd0aCwgZF9lbWIpICogMC4wMlxuICAgICAgICBwcmludChmXHUwMDI3UmFuZG9tIGluaXQ6IHN0ZD17aW5pdC5zdGQoKS5pdGVtKCk6LjRmfVx1MDAyNylcbiAgICBlbGlmIHN0cmF0ZWd5ID09IFx1MDAyN3ZvY2FiXHUwMDI3OlxuICAgICAgICB2b2NhYl9zaXplID0gdm9jYWJfZW1iZWRkaW5ncy5zaGFwZVswXVxuICAgICAgICBpZHggPSB0b3JjaC5yYW5kaW50KDAsIHZvY2FiX3NpemUsIChwcm9tcHRfbGVuZ3RoLCkpXG4gICAgICAgIGluaXQgPSB2b2NhYl9lbWJlZGRpbmdzW2lkeF0uY2xvbmUoKS5kZXRhY2goKVxuICAgICAgICBwcmludChmXHUwMDI3Vm9jYWIgaW5pdDogc2FtcGxlZCBpbmRpY2VzIHtpZHhbOjVdLnRvbGlzdCgpfVx1MDAyNylcbiAgICBlbGlmIHN0cmF0ZWd5ID09IFx1MDAyN2NsYXNzX2xhYmVsXHUwMDI3OlxuICAgICAgICBhc3NlcnQgY2xhc3NfbGFiZWxzLCBcdTAwMjdQcm92aWRlIGNsYXNzX2xhYmVscyBmb3IgY2xhc3NfbGFiZWwgc3RyYXRlZ3lcdTAwMjdcbiAgICAgICAgbGFiZWxfZW1iZWRzID0gW11cbiAgICAgICAgZm9yIGxhYmVsIGluIGNsYXNzX2xhYmVsczpcbiAgICAgICAgICAgIGlkcyA9IHRva2VuaXplcihsYWJlbCwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcpLmlucHV0X2lkc1swXVxuICAgICAgICAgICAgZW1icyA9IHZvY2FiX2VtYmVkZGluZ3NbaWRzXS5tZWFuKDApXG4gICAgICAgICAgICBsYWJlbF9lbWJlZHMuYXBwZW5kKGVtYnMpXG4gICAgICAgIGJhc2UgPSB0b3JjaC5zdGFjayhsYWJlbF9lbWJlZHMpXG4gICAgICAgIGlkeCA9IHRvcmNoLmFyYW5nZShwcm9tcHRfbGVuZ3RoKSAlIGxlbihjbGFzc19sYWJlbHMpXG4gICAgICAgIGluaXQgPSBiYXNlW2lkeF0uY2xvbmUoKS5kZXRhY2goKVxuICAgICAgICBwcmludChmXHUwMDI3Q2xhc3MgbGFiZWwgaW5pdDoge2NsYXNzX2xhYmVsc30gdGlsZWQgb3ZlciB7cHJvbXB0X2xlbmd0aH0gdG9rZW5zXHUwMDI3KVxuICAgIHJldHVybiBubi5QYXJhbWV0ZXIoaW5pdClcblxuZm9yIHN0cmF0LCBrd2FyZ3MgaW4gWyhcdTAwMjdyYW5kb21cdTAwMjcsIHt9KSwgKFx1MDAyN3ZvY2FiXHUwMDI3LCB7fSksXG4gICAgICAgICAgICAgICAgICAgICAgKFx1MDAyN2NsYXNzX2xhYmVsXHUwMDI3LCB7XHUwMDI3Y2xhc3NfbGFiZWxzXHUwMDI3OiBbXHUwMDI3cG9zaXRpdmVcdTAwMjcsIFx1MDAyN25lZ2F0aXZlXHUwMDI3LCBcdTAwMjduZXV0cmFsXHUwMDI3XX0pXTpcbiAgICBwYXJhbSA9IGluaXRpYWxpemVfc29mdF9wcm9tcHQoXHUwMDI3YmVydC1iYXNlLXVuY2FzZWRcdTAwMjcsIDMwLCBzdHJhdCwgKiprd2FyZ3MpXG4gICAgcHJpbnQoZlx1MDAyNyAgLVx1MDAzZSBzaGFwZT17cGFyYW0uc2hhcGV9LCBub3JtPXtwYXJhbS5kYXRhLm5vcm0oKS5pdGVtKCk6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsZSBTZW5zaXRpdml0eSBBbmFseXNpcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBSZXByb2R1Y2VkIGZyb20gTGVzdGVyIGV0IGFsLiAoMjAyMSkgLS0gU3VwZXJHTFVFIGF2ZXJhZ2Ugc2NvcmUgYnkgbW9kZWwgc2l6ZVxubW9kZWxfc2l6ZXNfQiA9IFswLjA2LCAwLjI1LCAwLjc3LCAzLjAsIDExLjBdICAjIGJpbGxpb25zIG9mIHBhcmFtZXRlcnNcbm1vZGVsX2xhYmVscyAgPSBbXHUwMDI3VDUtU21hbGxcdTAwMjcsIFx1MDAyN1Q1LUJhc2VcdTAwMjcsIFx1MDAyN1Q1LUxhcmdlXHUwMDI3LCBcdTAwMjdUNS1YTFx1MDAyNywgXHUwMDI3VDUtWFhMXHUwMDI3XVxuZnVsbF9mdF9zY29yZSAgICAgPSBbODMuMSwgODYuNCwgODguOSwgOTAuMywgOTEuMl1cbnByb21wdF90dW5lX3Njb3JlID0gWzUzLjIsIDYzLjEsIDcyLjQsIDgxLjUsIDkwLjhdICAjIFA9MTAwIHRva2Vuc1xubW9kZWxfdHVuZV9zY29yZSAgPSBbNzguMywgODIuMSwgODUuNiwgODguMiwgODkuOV0gICMgZnJlZXplIGFsbCwgdHVuZSBoZWFkIG9ubHlcblxucHJpbnQoZlx1MDAyN3tcIk1vZGVsXCI6XHUwMDNjMTJ9IHtcIlBhcmFtcyAoQilcIjpcdTAwM2UxMX0ge1wiRnVsbCBGVFwiOlx1MDAzZTl9IHtcIlByb21wdFwiOlx1MDAzZTl9IHtcIkdhcFwiOlx1MDAzZTl9XHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDU1KVxuZm9yIGxhYmVsLCBzaXplLCBmZnQsIHB0IGluIHppcChtb2RlbF9sYWJlbHMsIG1vZGVsX3NpemVzX0IsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmdWxsX2Z0X3Njb3JlLCBwcm9tcHRfdHVuZV9zY29yZSk6XG4gICAgZ2FwID0gcHQgLSBmZnRcbiAgICBwcmludChmXHUwMDI3e2xhYmVsOlx1MDAzYzEyfSB7c2l6ZTpcdTAwM2UxMS4yZn0ge2ZmdDpcdTAwM2U5LjFmfSB7cHQ6XHUwMDNlOS4xZn0ge2dhcDpcdTAwM2UrOS4xZn1cdTAwMjcpXG5cbnByaW50KClcbmZvciBsYWJlbCwgc2l6ZSwgZmZ0LCBwdCBpbiB6aXAobW9kZWxfbGFiZWxzLCBtb2RlbF9zaXplc19CLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZnVsbF9mdF9zY29yZSwgcHJvbXB0X3R1bmVfc2NvcmUpOlxuICAgIGlmIGFicyhwdCAtIGZmdCkgXHUwMDNjPSAyLjA6XG4gICAgICAgIHByaW50KGZcdTAwMjdQcm9tcHQgdHVuaW5nIHdpdGhpbiAyIHB0cyBvZiBmdWxsIEZUIGF0OiB7bGFiZWx9ICh7c2l6ZX1CIHBhcmFtcylcdTAwMjcpXG4gICAgICAgIGJyZWFrIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJvbXB0IFR1bmluZyB2cyBQcmVmaXggVHVuaW5nIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRpbWVuc2lvbiIsIlByb21wdCBUdW5pbmciLCJQcmVmaXggVHVuaW5nIl0sInJvd3MiOltbIldoZXJlIGFkYXB0YXRpb24gb2NjdXJzIiwiSW5wdXQgZW1iZWRkaW5nIGxheWVyIG9ubHkiLCJFdmVyeSB0cmFuc2Zvcm1lciBsYXllciAoSywgViBwYWlycykiXSxbIkxheWVycyBhZmZlY3RlZCIsIjEgKGVtYmVkZGluZykiLCJBbGwgTiBsYXllcnMiXSxbIlRyYWluYWJsZSBwYXJhbXMgKDEwMC10b2tlbiwgVDUtTGFyZ2UpIiwifjEwMksgKDEwMMOXMTAyNCkiLCJ+MTNNICgxMDDDlzEwMjTDlzLDlzI0IGxheWVycykiXSxbIkNvbnRleHQgbGVuZ3RoIGNvbnN1bWVkIiwiUCB0b2tlbnMgZnJvbSBpbnB1dCBidWRnZXQiLCJQIHRva2VucyBmcm9tIGlucHV0IGJ1ZGdldCBwZXIgbGF5ZXIiXSxbIlNjYWxlIHRocmVzaG9sZCBmb3IgY29tcGV0aXRpdmUgcGVyZiIsIuKJpTEwQiBwYXJhbWV0ZXJzIiwiQ29tcGV0aXRpdmUgYXQgfjFCKyBwYXJhbWV0ZXJzIl0sWyJJbXBsZW1lbnRhdGlvbiBjb21wbGV4aXR5IiwiVmVyeSBzaW1wbGUg4oCUIG9uZSBwYXJhbWV0ZXIgbWF0cml4IiwiTW9kZXJhdGUg4oCUIGhvb2sgaW50byBlYWNoIGF0dGVudGlvbiBsYXllciJdLFsiTXVsdGktdGFzayBpbmZlcmVuY2UiLCJTd2FwIEVfcHJvbXB0IGF0IGluZmVyZW5jZSIsIlN3YXAgcGVyLWxheWVyIEtWIHByZWZpeGVzIGF0IGluZmVyZW5jZSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktVGFzayBJbmZlcmVuY2UgYW5kIEVuc2VtYmxpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9uZSBwcmFjdGljYWwgYWR2YW50YWdlIG9mIHByb21wdCB0dW5pbmcgaXMgbXVsdGktdGFzayBzZXJ2aW5nOiBhIHNpbmdsZSBmcm96ZW4gYmFja2JvbmUgY2FuIHNlcnZlIG11bHRpcGxlIHRhc2tzIHNpbXVsdGFuZW91c2x5IGJ5IHN3YXBwaW5nIHRoZSBzb2Z0IHByb21wdCBtYXRyaXggYXQgaW5mZXJlbmNlLiBFYWNoIHRhc2sgcmVxdWlyZXMgc3RvcmluZyBvbmx5IFDDl2RfZW1iIGZsb2F0cy4gRm9yIFQ1LUxhcmdlIGFuZCBQPTEwMCwgdGhhdCBpcyAxMDJLw5cyIGJ5dGVzID0gMjA0S0IgcGVyIHRhc2sg4oCUIHRyaXZpYWwgY29tcGFyZWQgdG8gdGhlIDNHQiBiYWNrYm9uZS4gQW4gZW5zZW1ibGUgb2Ygc29mdCBwcm9tcHRzIGNhbiBiZSBjb25zdHJ1Y3RlZCBieSBhdmVyYWdpbmcgdGhlaXIgbG9naXRzOiBydW4gdGhlIHNhbWUgaW5wdXQgdGhyb3VnaCB0aGUgYmFja2JvbmUgd2l0aCBLIGRpZmZlcmVudCBzb2Z0IHByb21wdHMgYW5kIGFnZ3JlZ2F0ZSBwcmVkaWN0aW9ucy4gVGhpcyBwcm9tcHQgZW5zZW1ibGUgcmVsaWFibHkgb3V0cGVyZm9ybXMgYSBzaW5nbGUgcHJvbXB0IHdpdGhvdXQgY2hhbmdpbmcgdGhlIGJhY2tib25lLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gcHJvZHVjdGlvbiwgdGhlIHNlcnZpbmcgYXJjaGl0ZWN0dXJlIGlzOiBvbmUgYmFja2JvbmUgaW5zdGFuY2UgbG9hZGVkIGluIEdQVSBtZW1vcnkgKHNoYXJlZCBhY3Jvc3MgdGFza3MpLCBhIHRhc2sgcm91dGVyIHRoYXQgc2VsZWN0cyB0aGUgY29ycmVjdCBzb2Z0IHByb21wdCBtYXRyaXgsIGFuZCBhIHByb21wdC1wcmVwZW5kIHN0ZXAgYmVmb3JlIHRoZSBiYWNrYm9uZSBmb3J3YXJkIHBhc3MuIFN3aXRjaGluZyB0YXNrcyBoYXMgemVybyBsYXRlbmN5IGJleW9uZCB0aGUgdGlueSBwcm9tcHQgZW1iZWRkaW5nIGxvb2t1cC4gVGhpcyBpcyBmdW5kYW1lbnRhbGx5IGRpZmZlcmVudCBmcm9tIGZ1bGwgZmluZS10dW5pbmcsIHdoaWNoIHJlcXVpcmVzIGxvYWRpbmcgYSBzZXBhcmF0ZSBmdWxsIG1vZGVsIGNvcHkgcGVyIHRhc2suIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2NhbGUgRGVwZW5kZW5jZSBhbmQgTWV0aG9kIFNlbGVjdGlvbiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiU2NhbGUgRGVwZW5kZW5jZSIsImNvbnRlbnQiOiJQcm9tcHQgdHVuaW5nIGlzIHNjYWxlLWRlcGVuZGVudCDigJQgaXQgb25seSBtYXRjaGVzIGZ1bGwgZmluZS10dW5pbmcgcXVhbGl0eSBhdCAxMEIrIHBhcmFtZXRlcnMuIEZvciBzbWFsbGVyIG1vZGVscyAoMeKAkzdCKSwgdGhlIHNpZ25hbCBmcm9tIFAgc29mdCB0b2tlbnMgYXQgdGhlIGlucHV0IGNhbm5vdCBzdWZmaWNpZW50bHkgY29uZGl0aW9uIGEgc2hhbGxvd2VyIG5ldHdvcmssIG1ha2luZyBMb1JBIG9yIGFkYXB0ZXJzIHByZWZlcmFibGUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIFJlY29tbWVuZGF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJvbXB0IGxlbmd0aCBQPTEwMCBpcyBhIHJlbGlhYmxlIGRlZmF1bHQ7IGdhaW5zIHBsYXRlYXUgYmV5b25kIDEwMCB0b2tlbnMgYW5kIGxvbmdlciBwcm9tcHRzIGNvbnN1bWUgaW5wdXQgY29udGV4dCBidWRnZXQuIEZvciBtb2RlbHMgYmVsb3cgMUIgcGFyYW1ldGVycywgdGhlIGdhcCBiZXR3ZWVuIHByb21wdCB0dW5pbmcgYW5kIGZ1bGwgZmluZS10dW5pbmcgaXMgdG9vIGxhcmdlIGZvciBwcm9kdWN0aW9uIHVzZSDigJQgTG9SQSAocj04KSBvciBQZmVpZmZlciBhZGFwdGVycyBjbG9zZSB0aGF0IGdhcCBhdCBjb21wYXJhYmxlIHBhcmFtZXRlciBidWRnZXRzLiBGb3IgMTBCKyBtb2RlbHMsIHByb21wdCB0dW5pbmcgaXMgYSBwcmFjdGljYWwgY2hvaWNlIHdoZW4gYmFja2JvbmUgc2hhcmluZyBhY3Jvc3MgdGFza3MgaXMgcmVxdWlyZWQgYW5kIG1lbW9yeSBpcyB0aGUgcHJpbWFyeSBjb25zdHJhaW50LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIHByb21wdCBsZW5ndGggUD0xMDA7IGdhaW5zIGRpbWluaXNoIGJleW9uZCAxMDAgYW5kIGxvbmdlciBwcm9tcHRzIGNvbnN1bWUgaW5wdXQgY29udGV4dCBidWRnZXQuIiwiSW5pdGlhbGl6ZSBmcm9tIGNsYXNzIGxhYmVsIGVtYmVkZGluZ3Mg4oCUIGNvbnZlcmdlcyBmYXN0ZXIgYW5kIHdpdGggbG93ZXIgdmFyaWFuY2UgdGhhbiByYW5kb20gaW5pdC4iLCJGb3IgbW9kZWxzIGJlbG93IDFCIHBhcmFtZXRlcnMsIHByZWZlciBMb1JBIChyPTgpIG9yIFBmZWlmZmVyIGFkYXB0ZXJzIG92ZXIgcHJvbXB0IHR1bmluZy4iLCJBdCBUNS1YWEwgb3IgTExhTUEtMTNCKyBzY2FsZSwgcHJvbXB0IHR1bmluZyBhY2hpZXZlcyBmdWxsIGZpbmUtdHVuaW5nIGFjY3VyYWN5IGF0IGEgZnJhY3Rpb24gb2YgdGhlIGNvbXB1dGUuIiwiRm9yIG11bHRpLXRhc2sgc2VydmluZywgc3RvcmUgb25lIHNvZnQgcHJvbXB0IG1hdHJpeCAo4omkMU1CKSBwZXIgdGFzayDigJQgc3dhcCBhdCBpbmZlcmVuY2Ugd2l0aCB6ZXJvIGJhY2tib25lIHJlbG9hZC4iLCJQcm9tcHQgdHVuaW5nIGlzIGluY29tcGF0aWJsZSB3aXRoIG1vZGVscyB0aGF0IGxhY2sgYSBzdGFuZGFyZCB0b2tlbiBlbWJlZGRpbmcgbG9va3VwIChlLmcuLCBzb21lIHZpc2lvbiBtb2RlbHMpLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Prompt Tuning — Soft Prompts at Input Embeddings and Scale-Dependent Behavior

Prompt tuning (Lester et al., 2021) is a parameter-efficient fine-tuning method that prepends P learned soft prompt token embeddings to the input embedding sequence. Unlike discrete prompts (manually written text), soft prompts are continuous vectors in the embedding space that are optimized directly by gradient descent. The entire transformer is frozen; only the P×d_emb prompt embedding matrix is trained. This makes prompt tuning one of the most minimal PEFT approaches: no new layers, no weight decompositions, just a small learned prefix appended to every input.

## Soft Prompt Embedding Math

Let E_input ∈ ℝ^(L×d_emb) be the token embeddings for an input sequence of length L. Prompt tuning introduces a learnable matrix E_prompt ∈ ℝ^(P×d_emb) where P is the prompt length (typically 1–100 tokens). The full input to the transformer is concat(E_prompt, E_input) ∈ ℝ^((P+L)×d_emb). The transformer processes this concatenated sequence with its frozen weights. Backpropagation flows through the frozen transformer layers back to E_prompt. The gradient ∂L/∂E_prompt is well-defined and dense — every forward pass updates all P×d_emb values.

Trainable parameter count: for P=100 and d_emb=1024 (T5-Large), the prompt matrix contains 100×1024 = 102,400 parameters — roughly 0.01% of T5-Large's 770M parameters. This is 10–100× fewer trainable parameters than prefix tuning, which inserts learned key-value pairs at every attention layer. Prompt tuning is input-only; prefix tuning is per-layer. The reduction in trainable parameters comes at a cost: with only input-layer influence, the soft prompts must encode all task-specific information through the frozen model's own representational capacity.

## Soft Prompt Embedding Implementation

```python
import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer

class SoftPromptModel(nn.Module):
    """Wraps a frozen transformer with a learnable soft prompt prefix."""

    def __init__(self, model_name: str, prompt_length: int = 20):
        super().__init__()
        self.backbone = AutoModel.from_pretrained(model_name)
        for param in self.backbone.parameters():
            param.requires_grad = False
        d_emb = self.backbone.config.hidden_size
        self.prompt_length = prompt_length
        # Learnable soft prompt embeddings: shape (P, d_emb)
        self.soft_prompt = nn.Parameter(
            torch.randn(prompt_length, d_emb) * 0.02
        )

    def forward(self, input_ids: torch.Tensor,
                attention_mask: torch.Tensor) -> torch.Tensor:
        bsz = input_ids.shape[0]
        token_embeds = self.backbone.get_input_embeddings()(input_ids)
        prompt_embeds = self.soft_prompt.unsqueeze(0).expand(bsz, -1, -1)
        full_embeds = torch.cat([prompt_embeds, token_embeds], dim=1)
        prompt_mask = torch.ones(bsz, self.prompt_length,
                                 device=attention_mask.device)
        full_mask = torch.cat([prompt_mask, attention_mask], dim=1)
        outputs = self.backbone(inputs_embeds=full_embeds,
                                attention_mask=full_mask)
        return outputs.last_hidden_state

    def trainable_params(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

model = SoftPromptModel('bert-base-uncased', prompt_length=20)
print(f'Trainable params: {model.trainable_params():,}')  # only soft prompt
print(f'Soft prompt shape: {model.soft_prompt.shape}')    # (20, 768)
```

## Prompt Tuning with T5 via PEFT

```python
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from peft import PromptTuningConfig, PromptTuningInit, get_peft_model, TaskType

def setup_t5_prompt_tuning(model_name: str = 't5-large',
                           num_virtual_tokens: int = 100,
                           init_text: str = 'Classify sentiment:'):
    """Configure T5 for prompt tuning on a classification task."""
    base_model = T5ForConditionalGeneration.from_pretrained(model_name)
    peft_config = PromptTuningConfig(
        task_type=TaskType.SEQ_2_SEQ_LM,
        prompt_tuning_init=PromptTuningInit.TEXT,
        num_virtual_tokens=num_virtual_tokens,
        prompt_tuning_init_text=init_text,
        tokenizer_name_or_path=model_name,
    )
    model = get_peft_model(base_model, peft_config)
    model.print_trainable_parameters()  # ~102K / 770M for T5-Large
    return model

def run_prompt_tuning_demo():
    model = setup_t5_prompt_tuning(num_virtual_tokens=50)
    tokenizer = T5Tokenizer.from_pretrained('t5-large')
    sample = 'The movie was absolutely fantastic and I loved every moment.'
    inputs = tokenizer(sample, return_tensors='pt', truncation=True, max_length=128)
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_new_tokens=5)
    print(f'Input: {sample}')
    print(f'Output: {tokenizer.decode(output_ids[0], skip_special_tokens=True)}')

print('Prompt tuning config ready — only soft_prompt params receive gradients.')
```

## Initialization Strategies

The initial values of E_prompt significantly affect convergence speed. Three strategies are compared: (1) random initialization from N(0, 0.02) — high variance across runs; (2) vocabulary token initialization — sample P tokens from the model's vocabulary embedding matrix, providing meaningful starting points; (3) class label initialization — for classification tasks, initialize from embeddings of target class label strings (e.g., 'positive', 'negative'). Class label init converges fastest and shows lowest variance, particularly at sub-1B scale.

```python
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel

def initialize_soft_prompt(model_name: str, prompt_length: int,
                           strategy: str = 'random',
                           class_labels: list = None) -> nn.Parameter:
    """
    Initialize soft prompt embeddings with three strategies.
    strategy: 'random' | 'vocab' | 'class_label'
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    embed_layer = model.get_input_embeddings()
    d_emb = embed_layer.embedding_dim
    vocab_embeddings = embed_layer.weight.data  # (V, d_emb)

    if strategy == 'random':
        init = torch.randn(prompt_length, d_emb) * 0.02
        print(f'Random init: std={init.std().item():.4f}')
    elif strategy == 'vocab':
        vocab_size = vocab_embeddings.shape[0]
        idx = torch.randint(0, vocab_size, (prompt_length,))
        init = vocab_embeddings[idx].clone().detach()
        print(f'Vocab init: sampled indices {idx[:5].tolist()}')
    elif strategy == 'class_label':
        assert class_labels, 'Provide class_labels for class_label strategy'
        label_embeds = []
        for label in class_labels:
            ids = tokenizer(label, return_tensors='pt').input_ids[0]
            embs = vocab_embeddings[ids].mean(0)
            label_embeds.append(embs)
        base = torch.stack(label_embeds)
        idx = torch.arange(prompt_length) % len(class_labels)
        init = base[idx].clone().detach()
        print(f'Class label init: {class_labels} tiled over {prompt_length} tokens')
    return nn.Parameter(init)

for strat, kwargs in [('random', {}), ('vocab', {}),
                      ('class_label', {'class_labels': ['positive', 'negative', 'neutral']})]:
    param = initialize_soft_prompt('bert-base-uncased', 30, strat, **kwargs)
    print(f'  -> shape={param.shape}, norm={param.data.norm().item():.3f}')
```

## Scale Sensitivity Analysis

```python
import numpy as np

# Reproduced from Lester et al. (2021) -- SuperGLUE average score by model size
model_sizes_B = [0.06, 0.25, 0.77, 3.0, 11.0]  # billions of parameters
model_labels  = ['T5-Small', 'T5-Base', 'T5-Large', 'T5-XL', 'T5-XXL']
full_ft_score     = [83.1, 86.4, 88.9, 90.3, 91.2]
prompt_tune_score = [53.2, 63.1, 72.4, 81.5, 90.8]  # P=100 tokens
model_tune_score  = [78.3, 82.1, 85.6, 88.2, 89.9]  # freeze all, tune head only

print(f'{"Model":<12} {"Params (B)":>11} {"Full FT":>9} {"Prompt":>9} {"Gap":>9}')
print('-' * 55)
for label, size, fft, pt in zip(model_labels, model_sizes_B,
                                 full_ft_score, prompt_tune_score):
    gap = pt - fft
    print(f'{label:<12} {size:>11.2f} {fft:>9.1f} {pt:>9.1f} {gap:>+9.1f}')

print()
for label, size, fft, pt in zip(model_labels, model_sizes_B,
                                 full_ft_score, prompt_tune_score):
    if abs(pt - fft) <= 2.0:
        print(f'Prompt tuning within 2 pts of full FT at: {label} ({size}B params)')
        break
```

## Prompt Tuning vs Prefix Tuning

| Dimension | Prompt Tuning | Prefix Tuning |
| --- | --- | --- |
| Where adaptation occurs | Input embedding layer only | Every transformer layer (K, V pairs) |
| Layers affected | 1 (embedding) | All N layers |
| Trainable params (100-token, T5-Large) | ~102K (100×1024) | ~13M (100×1024×2×24 layers) |
| Context length consumed | P tokens from input budget | P tokens from input budget per layer |
| Scale threshold for competitive perf | ≥10B parameters | Competitive at ~1B+ parameters |
| Implementation complexity | Very simple — one parameter matrix | Moderate — hook into each attention layer |
| Multi-task inference | Swap E_prompt at inference | Swap per-layer KV prefixes at inference |

## Multi-Task Inference and Ensembling

One practical advantage of prompt tuning is multi-task serving: a single frozen backbone can serve multiple tasks simultaneously by swapping the soft prompt matrix at inference. Each task requires storing only P×d_emb floats. For T5-Large and P=100, that is 102K×2 bytes = 204KB per task — trivial compared to the 3GB backbone. An ensemble of soft prompts can be constructed by averaging their logits: run the same input through the backbone with K different soft prompts and aggregate predictions. This prompt ensemble reliably outperforms a single prompt without changing the backbone.

In production, the serving architecture is: one backbone instance loaded in GPU memory (shared across tasks), a task router that selects the correct soft prompt matrix, and a prompt-prepend step before the backbone forward pass. Switching tasks has zero latency beyond the tiny prompt embedding lookup. This is fundamentally different from full fine-tuning, which requires loading a separate full model copy per task.

## Scale Dependence and Method Selection

> **Scale Dependence**: Prompt tuning is scale-dependent — it only matches full fine-tuning quality at 10B+ parameters. For smaller models (1–7B), the signal from P soft tokens at the input cannot sufficiently condition a shallower network, making LoRA or adapters preferable.

## Practical Recommendations

Prompt length P=100 is a reliable default; gains plateau beyond 100 tokens and longer prompts consume input context budget. For models below 1B parameters, the gap between prompt tuning and full fine-tuning is too large for production use — LoRA (r=8) or Pfeiffer adapters close that gap at comparable parameter budgets. For 10B+ models, prompt tuning is a practical choice when backbone sharing across tasks is required and memory is the primary constraint.

- Use prompt length P=100; gains diminish beyond 100 and longer prompts consume input context budget.
- Initialize from class label embeddings — converges faster and with lower variance than random init.
- For models below 1B parameters, prefer LoRA (r=8) or Pfeiffer adapters over prompt tuning.
- At T5-XXL or LLaMA-13B+ scale, prompt tuning achieves full fine-tuning accuracy at a fraction of the compute.
- For multi-task serving, store one soft prompt matrix (≤1MB) per task — swap at inference with zero backbone reload.
- Prompt tuning is incompatible with models that lack a standard token embedding lookup (e.g., some vision models).

---

