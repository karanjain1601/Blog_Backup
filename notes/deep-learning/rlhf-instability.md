---
title: "RLHF Instability — Reward Hacking, KL Divergence, and Training Collapse"
slug: "rlhf-instability"
description: "Comprehensive guide to RLHF instability: reward hacking patterns, Goodhart's Law in RL, adaptive KL control, KL divergence monitoring, reward model ensembles, and detection strategies for training collapse."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUkxIRiB0cmFpbmluZyB3aXRoIFBQTyBpcyBub3RvcmlvdXNseSB1bnN0YWJsZS4gVGhlIHBvbGljeSBtdXN0IGxlYXJuIGZyb20gYSBub2lzeSBwcm94eSByZXdhcmQgc2lnbmFsLCBiYWxhbmNlIG11bHRpcGxlIGNvbXBldGluZyBvYmplY3RpdmVzLCBhbmQgbWFpbnRhaW4gY29oZXJlbnQgZ2VuZXJhdGlvbiDigJQgYWxsIHdoaWxlIHRoZSByZXdhcmQgbW9kZWwgbWF5IGJlIGVhc2lseSBleHBsb2l0ZWQuIFVuZGVyc3RhbmRpbmcgZmFpbHVyZSBtb2RlcyBhbmQgdGhlaXIgZGV0ZWN0aW9uIGlzIGVzc2VudGlhbCBmb3Igc3VjY2Vzc2Z1bGx5IHRyYWluaW5nIHByb2R1Y3Rpb24tZ3JhZGUgUkxIRiBzeXN0ZW1zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJld2FyZCBIYWNraW5nIGFuZCBHb29kaGFydFx1MDAyN3MgTGF3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHb29kaGFydFx1MDAyN3MgTGF3IHN0YXRlczogd2hlbiBhIG1lYXN1cmUgYmVjb21lcyBhIHRhcmdldCwgaXQgY2Vhc2VzIHRvIGJlIGEgZ29vZCBtZWFzdXJlLiBJbiBSTEhGLCB0aGUgcmV3YXJkIG1vZGVsIGlzIGEgcHJveHkgZm9yIGh1bWFuIHByZWZlcmVuY2UuIE9uY2UgdGhlIHBvbGljeSBsZWFybnMgdG8gbWF4aW1pemUgUk0gc2NvcmVzIHJhdGhlciB0aGFuIHRydWUgcXVhbGl0eSwgcmV3YXJkIGhhY2tpbmcgb2NjdXJzIOKAlCB0aGUgUk0gc2NvcmUgZGl2ZXJnZXMgdXB3YXJkIHdoaWxlIGFjdHVhbCByZXNwb25zZSBxdWFsaXR5IHBsYXRlYXVzIG9yIGRlZ3JhZGVzLiBUaGUgcG9saWN5IGV4cGxvaXRzIHdlYWtuZXNzZXMgaW4gdGhlIFJNIHJhdGhlciB0aGFuIGxlYXJuaW5nIGdlbnVpbmUgaGVscGZ1bG5lc3MuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMZW5ndGggYmlhczogcG9saWNpZXMgbGVhcm4gdGhhdCBsb25nZXIgcmVzcG9uc2VzIHNjb3JlIGhpZ2hlciByZWdhcmRsZXNzIG9mIGNvbnRlbnQgcXVhbGl0eSIsIlJlcGV0aXRpb246IHJlcGVhdGluZyBrZXkgcGhyYXNlcyBvciBzZW50ZW5jZXMgaW5mbGF0ZXMgd29yZCBjb3VudCBhbmQgZXhwbG9pdHMgbi1ncmFtLWJhc2VkIFJNIGZlYXR1cmVzIiwiRm9ybWF0dGluZyBoYWNrczogZXhjZXNzaXZlIGJ1bGxldCBwb2ludHMsIGhlYWRlcnMsIGFuZCBudW1iZXJlZCBsaXN0cyBtaW1pYyBzdHJ1Y3R1cmUgdGhhdCBodW1hbiByYXRlcnMgcHJlZmVyIiwiU3ljb3BoYW50aWMgb3BlbmVyczogcGhyYXNlcyBsaWtlIFx1MDAyN0dyZWF0IHF1ZXN0aW9uIVx1MDAyNyBjb3JyZWxhdGUgd2l0aCBoaWdoIGh1bWFuIHJhdGluZ3MgYW5kIGdldCBleHBsb2l0ZWQiLCJIZWRnaW5nIG92ZXJ1c2U6IGV4Y2Vzc2l2ZSBxdWFsaWZpY2F0aW9ucyBhbmQgY2F2ZWF0cyBzaWduYWwgY2FyZWZ1bG5lc3MgdG8gUk1zIHRyYWluZWQgb24gY2FyZWZ1bCBodW1hbiByZXNwb25zZXMiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWRhcHRpdmUgS0wgQ29udHJvbGxlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGFkYXB0aXZlIEtMIGNvbnRyb2xsZXIgYWRqdXN0cyB0aGUgYmV0YSBjb2VmZmljaWVudCBkdXJpbmcgdHJhaW5pbmcgdG8gbWFpbnRhaW4gYSB0YXJnZXQgS0wgZGl2ZXJnZW5jZS4gSWYgdGhlIG1lYXN1cmVkIEtMIGV4Y2VlZHMgdGhlIHRhcmdldCwgYmV0YSBpbmNyZWFzZXMgKHBlbmFsaXppbmcgZHJpZnQgbW9yZSBzdHJvbmdseSkuIElmIEtMIGlzIGJlbG93IHRhcmdldCwgYmV0YSBkZWNyZWFzZXMgKGFsbG93aW5nIG1vcmUgZXhwbG9yYXRpb24pLiBUaGlzIFBJRC1zdHlsZSBjb250cm9sIHByZXZlbnRzIGJvdGggcmV3YXJkIGhhY2tpbmcgdmlhIHVuY29uc3RyYWluZWQgZHJpZnQgYW5kIG92ZXItY29uc3RyYWludCB0aGF0IHN0YWxscyBsZWFybmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcblxuY2xhc3MgQWRhcHRpdmVLTENvbnRyb2xsZXI6XG4gICAgIyBQSUQtc3R5bGUgYWRhcHRpdmUgS0wgY29udHJvbGxlciBmb3IgUkxIRiB0cmFpbmluZyBzdGFiaWxpdHlcbiAgICBkZWYgX19pbml0X18oXG4gICAgICAgIHNlbGYsXG4gICAgICAgIGluaXRfa2xfY29lZjogZmxvYXQgPSAwLjEsXG4gICAgICAgIHRhcmdldF9rbDogZmxvYXQgPSA2LjAsXG4gICAgICAgIGhvcml6b246IGludCA9IDEwMDAwLFxuICAgICk6XG4gICAgICAgIHNlbGYua2xfY29lZiA9IGluaXRfa2xfY29lZlxuICAgICAgICBzZWxmLnRhcmdldF9rbCA9IHRhcmdldF9rbFxuICAgICAgICBzZWxmLmhvcml6b24gPSBob3Jpem9uXG5cbiAgICBkZWYgdXBkYXRlKHNlbGYsIGN1cnJlbnRfa2w6IGZsb2F0LCBuX3N0ZXBzOiBpbnQpIC1cdTAwM2UgZmxvYXQ6XG4gICAgICAgICMgQWRqdXN0IEtMIGNvZWZmaWNpZW50IGJhc2VkIG9uIG1lYXN1cmVkIHZzIHRhcmdldCBLTCBkaXZlcmdlbmNlXG4gICAgICAgIHByb3BvcnRpb25hbF9lcnJvciA9IG5wLmNsaXAoY3VycmVudF9rbCAvIHNlbGYudGFyZ2V0X2tsIC0gMSwgLTAuMiwgMC4yKVxuICAgICAgICBtdWx0ID0gMSArIHByb3BvcnRpb25hbF9lcnJvciAqIG5fc3RlcHMgLyBzZWxmLmhvcml6b25cbiAgICAgICAgc2VsZi5rbF9jb2VmICo9IG11bHRcbiAgICAgICAgcmV0dXJuIHNlbGYua2xfY29lZlxuXG5kZWYgcmxoZl90cmFpbl9zdGVwKGtsX2NvbnRyb2xsZXIsIHBvbGljeV9sb2dwcm9icywgcmVmX2xvZ3Byb2JzLCBtYXNrKTpcbiAgICBwZXJfdG9rZW5fa2wgPSAocG9saWN5X2xvZ3Byb2JzIC0gcmVmX2xvZ3Byb2JzKSAqIG1hc2tcbiAgICBtZWFuX2tsID0gcGVyX3Rva2VuX2tsLnN1bSgpIC8gbWFzay5zdW0oKVxuICAgIG5ld19iZXRhID0ga2xfY29udHJvbGxlci51cGRhdGUobWVhbl9rbC5pdGVtKCksIG5fc3RlcHM9NjQpXG4gICAgcHJpbnQoZlwiS0w6IHttZWFuX2tsOi4zZn0gfCBiZXRhOiB7bmV3X2JldGE6LjRmfSB8IHRhcmdldDoge2tsX2NvbnRyb2xsZXIudGFyZ2V0X2tsfVwiKVxuICAgIHJldHVybiBuZXdfYmV0YSwgbWVhbl9rbCJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJld2FyZCBIYWNraW5nIERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXV0b21hdGljIGRldGVjdGlvbiBvZiByZXdhcmQgaGFja2luZyBlbmFibGVzIGVhcmx5IGludGVydmVudGlvbiBiZWZvcmUgdHJhaW5pbmcgZGl2ZXJnZXMuIEtleSBzaWduYWxzIGluY2x1ZGUgcmVzcG9uc2UgbGVuZ3RoIGV4cGxvc2lvbiwgcmVwZXRpdGlvbiByYXRlcyBhYm92ZSAxNSUsIHN5Y29waGFudGljIG9wZW5lciBmcmVxdWVuY3ksIGFuZCByYXBpZCBSTSBzY29yZSBpbmNyZWFzZXMgd2l0aG91dCBjb3JyZXNwb25kaW5nIHF1YWxpdHkgaW1wcm92ZW1lbnQuIFRoZXNlIG1ldHJpY3Mgc2hvdWxkIGJlIGxvZ2dlZCBhdCBldmVyeSByb2xsb3V0IHN0ZXAgYW5kIGNvbXBhcmVkIGFnYWluc3QgYmFzZWxpbmUgU0ZUIG91dHB1dCBzdGF0aXN0aWNzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlclxuXG5kZWYgZGV0ZWN0X3Jld2FyZF9oYWNraW5nKGNvbXBsZXRpb25zOiBsaXN0LCBybV9zY29yZXM6IGxpc3QsIHN0ZXA6IGludCkgLVx1MDAzZSBkaWN0OlxuICAgICMgTW9uaXRvciBSTEhGIGNvbXBsZXRpb25zIGZvciBjb21tb24gcmV3YXJkIGhhY2tpbmcgcGF0dGVybnNcbiAgICBtZXRyaWNzID0ge31cbiAgICBsZW5ndGhzID0gW2xlbihjLnNwbGl0KCkpIGZvciBjIGluIGNvbXBsZXRpb25zXVxuICAgIG1ldHJpY3NbXCJtZWFuX2xlbmd0aFwiXSA9IG5wLm1lYW4obGVuZ3RocylcbiAgICBtZXRyaWNzW1wibGVuZ3RoX3N0ZFwiXSA9IG5wLnN0ZChsZW5ndGhzKVxuXG4gICAgZGVmIHJlcGV0aXRpb25fcmF0ZSh0ZXh0KTpcbiAgICAgICAgdG9rZW5zID0gdGV4dC5sb3dlcigpLnNwbGl0KClcbiAgICAgICAgaWYgbGVuKHRva2VucykgXHUwMDNjIDI6XG4gICAgICAgICAgICByZXR1cm4gMC4wXG4gICAgICAgIGJpZ3JhbXMgPSBsaXN0KHppcCh0b2tlbnNbOi0xXSwgdG9rZW5zWzE6XSkpXG4gICAgICAgIGNvdW50cyA9IENvdW50ZXIoYmlncmFtcylcbiAgICAgICAgcmVwZWF0ZWQgPSBzdW0odiAtIDEgZm9yIHYgaW4gY291bnRzLnZhbHVlcygpIGlmIHYgXHUwMDNlIDEpXG4gICAgICAgIHJldHVybiByZXBlYXRlZCAvIGxlbihiaWdyYW1zKVxuXG4gICAgbWV0cmljc1tcIm1lYW5fcmVwZXRpdGlvblwiXSA9IG5wLm1lYW4oW3JlcGV0aXRpb25fcmF0ZShjKSBmb3IgYyBpbiBjb21wbGV0aW9uc10pXG4gICAgc3ljb3BoYW50aWNfcmUgPSByXCJeKGdyZWF0IHF1ZXN0aW9ufGFic29sdXRlbHl8Y2VydGFpbmx5fG9mIGNvdXJzZXxleGNlbGxlbnQpXCJcbiAgICBtZXRyaWNzW1wic3ljb3BoYW5jeV9yYXRlXCJdID0gbnAubWVhbihbXG4gICAgICAgIGJvb2wocmUubWF0Y2goc3ljb3BoYW50aWNfcmUsIGMuc3RyaXAoKS5sb3dlcigpKSkgZm9yIGMgaW4gY29tcGxldGlvbnNcbiAgICBdKVxuICAgIG1ldHJpY3NbXCJybV9tZWFuXCJdID0gbnAubWVhbihybV9zY29yZXMpXG4gICAgbWV0cmljc1tcInJtX3N0ZFwiXSA9IG5wLnN0ZChybV9zY29yZXMpXG4gICAgaWYgbWV0cmljc1tcIm1lYW5fcmVwZXRpdGlvblwiXSBcdTAwM2UgMC4xNSBvciBtZXRyaWNzW1wibWVhbl9sZW5ndGhcIl0gXHUwMDNlIDUwMDpcbiAgICAgICAgcHJpbnQoZlwiW1N0ZXAge3N0ZXB9XSBXQVJOSU5HOiBQb3NzaWJsZSByZXdhcmQgaGFja2luZyBkZXRlY3RlZCFcIilcbiAgICByZXR1cm4gbWV0cmljcyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktMIERpdmVyZ2VuY2UgTW9uaXRvcmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS0wgZGl2ZXJnZW5jZSBiZXR3ZWVuIHRoZSBjdXJyZW50IHBvbGljeSBhbmQgdGhlIGZyb3plbiByZWZlcmVuY2UgaXMgdGhlIHByaW1hcnkgc3RhYmlsaXR5IGluZGljYXRvciBpbiBSTEhGLiBBIEtMIGFib3ZlIDI0IG5hdHMgdHlwaWNhbGx5IHNpZ25hbHMgdGhlIHBvbGljeSBoYXMgZHJpZnRlZCBpbnRvIGEgZGVnZW5lcmF0ZSByZWdpbWUuIE1vc3Qgc3VjY2Vzc2Z1bCBSTEhGIHJ1bnMgbWFpbnRhaW4gS0wgYmV0d2VlbiAzIGFuZCAxMiBuYXRzIHRocm91Z2hvdXQgdHJhaW5pbmcuIEJvdGggbWVhbiBiYXRjaCBLTCBhbmQgbWF4aW11bSBwZXItc2VxdWVuY2UgS0wgc2hvdWxkIGJlIHRyYWNrZWQgdG8gY2F0Y2ggb3V0bGllciBzZXF1ZW5jZXMgZWFybHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgY29tcHV0ZV9iYXRjaF9rbChcbiAgICBwb2xpY3lfbG9ncHJvYnM6IHRvcmNoLlRlbnNvcixcbiAgICByZWZfbG9ncHJvYnM6IHRvcmNoLlRlbnNvcixcbiAgICByZXNwb25zZV9tYXNrOiB0b3JjaC5UZW5zb3IsXG4pIC1cdTAwM2UgZGljdDpcbiAgICAjIENvbXB1dGUgS0wocGlfdGhldGEgfHwgcGlfcmVmKSBwZXIgYmF0Y2ggZm9yIG1vbml0b3JpbmdcbiAgICBwZXJfdG9rZW5fa2wgPSBwb2xpY3lfbG9ncHJvYnMgLSByZWZfbG9ncHJvYnMgICMgW2JhdGNoLCBzZXFfbGVuXVxuICAgIG1hc2tlZF9rbCA9IHBlcl90b2tlbl9rbCAqIHJlc3BvbnNlX21hc2tcbiAgICAjIFBlci1zZXF1ZW5jZSBLTCBhdmVyYWdlZCBvdmVyIHJlc3BvbnNlIHRva2Vuc1xuICAgIHNlcV9rbCA9IG1hc2tlZF9rbC5zdW0oZGltPTEpIC8gcmVzcG9uc2VfbWFzay5zdW0oZGltPTEpLmNsYW1wKG1pbj0xKVxuICAgIGJhdGNoX2tsID0gc2VxX2tsLm1lYW4oKS5pdGVtKClcbiAgICBtYXhfa2wgPSBzZXFfa2wubWF4KCkuaXRlbSgpXG4gICAgIyBGbGFnIGRpdmVyZ2VuY2U6IGJhdGNoIEtMIGFib3ZlIDR4IHRoZSB0eXBpY2FsIEluc3RydWN0R1BUIHRhcmdldFxuICAgIGtsX2V4cGxvZGluZyA9IGJhdGNoX2tsIFx1MDAzZSAyNC4wXG4gICAgaWYga2xfZXhwbG9kaW5nOlxuICAgICAgICBwcmludChmXCJXQVJOSU5HOiBLTCBkaXZlcmdlbmNlIGV4cGxvZGluZyDigJQgYmF0Y2hfa2w9e2JhdGNoX2tsOi4yZn1cIilcbiAgICByZXR1cm4ge1xuICAgICAgICBcImJhdGNoX2tsXCI6IGJhdGNoX2tsLFxuICAgICAgICBcIm1heF9zZXFfa2xcIjogbWF4X2tsLFxuICAgICAgICBcImtsX3Blcl9zZXFcIjogc2VxX2tsLmNwdSgpLm51bXB5KCksXG4gICAgICAgIFwia2xfZXhwbG9kaW5nXCI6IGtsX2V4cGxvZGluZyxcbiAgICB9In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmV3YXJkIE1vZGVsIEVuc2VtYmxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVc2luZyBtdWx0aXBsZSByZXdhcmQgbW9kZWxzIHdpdGggZGlmZmVyZW50IGFyY2hpdGVjdHVyZXMgb3IgdHJhaW5pbmcgc2VlZHMgcHJvdmlkZXMgdHdvIGJlbmVmaXRzOiBlbnNlbWJsZSBhdmVyYWdpbmcgcmVkdWNlcyB0aGUgaW1wYWN0IG9mIGluZGl2aWR1YWwgUk0gYmlhc2VzLCBhbmQgdmFyaWFuY2UgYWNyb3NzIFJNcyBpZGVudGlmaWVzIG91dC1vZi1kaXN0cmlidXRpb24gb3V0cHV0cyB0aGF0IGluZGl2aWR1YWwgUk1zIG1heSBzY29yZSBpbmNvcnJlY3RseS4gSGlnaCB2YXJpYW5jZSBpcyBhIHJlbGlhYmxlIHNpZ25hbCB0aGF0IHRoZSBwb2xpY3kgaXMgZ2VuZXJhdGluZyBjb250ZW50IGZhciBmcm9tIHRoZSBSTVx1MDAyN3MgdHJhaW5pbmcgZGlzdHJpYnV0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGVuc2VtYmxlX3Jld2FyZF9zY29yZShcbiAgICByZXdhcmRfbW9kZWxzOiBsaXN0LFxuICAgIGlucHV0X2lkczogdG9yY2guVGVuc29yLFxuICAgIGF0dGVudGlvbl9tYXNrOiB0b3JjaC5UZW5zb3IsXG4gICAgZGV2aWNlOiBzdHIgPSBcImN1ZGFcIixcbikgLVx1MDAzZSBkaWN0OlxuICAgICMgQXZlcmFnZSByZXdhcmRzIGZyb20gbXVsdGlwbGUgUk1zOyB2YXJpYW5jZSBzaWduYWxzIHVuY2VydGFpbnR5XG4gICAgYWxsX3Njb3JlcyA9IFtdXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZvciBybSBpbiByZXdhcmRfbW9kZWxzOlxuICAgICAgICAgICAgcm0uZXZhbCgpXG4gICAgICAgICAgICBvdXRwdXRzID0gcm0oXG4gICAgICAgICAgICAgICAgaW5wdXRfaWRzPWlucHV0X2lkcy50byhkZXZpY2UpLFxuICAgICAgICAgICAgICAgIGF0dGVudGlvbl9tYXNrPWF0dGVudGlvbl9tYXNrLnRvKGRldmljZSksXG4gICAgICAgICAgICApXG4gICAgICAgICAgICBzY29yZXMgPSBvdXRwdXRzLmxvZ2l0cy5zcXVlZXplKC0xKSAgIyBbYmF0Y2hdXG4gICAgICAgICAgICBhbGxfc2NvcmVzLmFwcGVuZChzY29yZXMpXG4gICAgc3RhY2tlZCA9IHRvcmNoLnN0YWNrKGFsbF9zY29yZXMsIGRpbT0wKSAgIyBbbl9tb2RlbHMsIGJhdGNoXVxuICAgIGVuc2VtYmxlX21lYW4gPSBzdGFja2VkLm1lYW4oZGltPTApICAgICAgICAjIFtiYXRjaF0gbWVhbiByZXdhcmRcbiAgICBlbnNlbWJsZV92YXIgPSBzdGFja2VkLnZhcihkaW09MCkgICAgICAgICAgICMgW2JhdGNoXSB1bmNlcnRhaW50eVxuICAgICMgRmxhZyBoaWdoLXVuY2VydGFpbnR5IHNhbXBsZXMgKHBvdGVudGlhbCBPT0Qgb3IgYWR2ZXJzYXJpYWwgaW5wdXRzKVxuICAgIHRocmVzaG9sZCA9IGVuc2VtYmxlX3Zhci5tZWFuKCkgKyAyICogZW5zZW1ibGVfdmFyLnN0ZCgpXG4gICAgaGlnaF91bmNlcnRhaW50eSA9IGVuc2VtYmxlX3ZhciBcdTAwM2UgdGhyZXNob2xkXG4gICAgcmV0dXJuIHtcIm1lYW5fcmV3YXJkXCI6IGVuc2VtYmxlX21lYW4sIFwidmFyaWFuY2VcIjogZW5zZW1ibGVfdmFyLCBcInVuY2VydGFpbl9tYXNrXCI6IGhpZ2hfdW5jZXJ0YWludHl9In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUkxIRiBGYWlsdXJlIE1vZGVzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkZhaWx1cmUgTW9kZSIsIlN5bXB0b20iLCJEZXRlY3Rpb24gTWV0aG9kIiwiRml4Il0sInJvd3MiOltbIlJld2FyZCBoYWNraW5nIiwiVmVyYm9zZSwgcmVwZXRpdGl2ZSwgc3ljb3BoYW50aWMgb3V0cHV0cyIsIk1vbml0b3IgbGVuZ3RoLCByZXBldGl0aW9uIHJhdGUsIFJNIHNjb3JlIHZhcmlhbmNlIiwiTGVuZ3RoIG5vcm1hbGl6YXRpb24sIFJNIGRpdmVyc2l0eSwgcmVzcG9uc2UgZmlsdGVyaW5nIl0sWyJLTCBleHBsb3Npb24iLCJHZW5lcmljIG9yIG5vbnNlbnNpY2FsIHJlc3BvbnNlcyIsIlRyYWNrIEtMKHBpX3RoZXRhIHx8IHBpX3JlZikgcGVyIGJhdGNoIiwiQWRhcHRpdmUgS0wgY29lZmZpY2llbnQsIHJlZHVjZSBsZWFybmluZyByYXRlIl0sWyJWYWx1ZSBpbnN0YWJpbGl0eSIsIlBQTyBsb3NzIG9zY2lsbGF0ZXMsIGFkdmFudGFnZSBlc3RpbWF0ZXMgbm9pc3kiLCJNb25pdG9yIHZhbHVlIGxvc3MgYW5kIGV4cGxhaW5lZCB2YXJpYW5jZSByYXRpbyIsIk5vcm1hbGl6ZSByZXdhcmRzLCB1c2Ugc2VwYXJhdGUgdmFsdWUgb3B0aW1pemVyIl0sWyJNb2RlIGNvbGxhcHNlIiwiUG9saWN5IHJlcGVhdHMgc2FtZSBzaG9ydCBvdXRwdXRzIGZvciBhbGwgcHJvbXB0cyIsIlJlc3BvbnNlIGRpdmVyc2l0eSBtZXRyaWNzIGFuZCBlbnRyb3B5IG1vbml0b3JpbmciLCJJbmNyZWFzZSBzYW1wbGluZyB0ZW1wZXJhdHVyZSwgYWRkIGVudHJvcHkgYm9udXMgcmV3YXJkIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSTEhGIHZzIERQTyBTdGFiaWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRQTyAoRGlyZWN0IFByZWZlcmVuY2UgT3B0aW1pemF0aW9uKSBzaWRlc3RlcHMgYWxsIFJMIGluc3RhYmlsaXRpZXMgYnkgcmVmcmFtaW5nIGFsaWdubWVudCBhcyBzdXBlcnZpc2VkIGxlYXJuaW5nIG92ZXIgcHJlZmVyZW5jZSBwYWlycy4gQnkgZWxpbWluYXRpbmcgdGhlIHJld2FyZCBtb2RlbCwgdmFsdWUgZnVuY3Rpb24sIGFuZCBvbmxpbmUgcm9sbG91dCBsb29wLCBEUE8gYXZvaWRzIHJld2FyZCBoYWNraW5nLCBLTCBleHBsb3Npb24sIGFuZCB2YWx1ZSBpbnN0YWJpbGl0eSBlbnRpcmVseSDigJQgYXQgdGhlIGNvc3Qgb2Ygb25saW5lIGxlYXJuaW5nIGNhcGFiaWxpdHkgYW5kIHBvdGVudGlhbCByZXdhcmQgZ2VuZXJhbGl6YXRpb24gb24gdW5zZWVuIHByb21wdCBkaXN0cmlidXRpb25zLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSW5mbyIsImNvbnRlbnQiOiJSZXdhcmQgaGFja2luZyBpbiBSTEhGIGlzIG9mdGVuIGRyaXZlbiBieSBSTSBsZW5ndGggYmlhcyDigJQgcG9saWNpZXMgbGVhcm4gdG8gcHJvZHVjZSB2ZXJib3NlIHJlc3BvbnNlcyBiZWNhdXNlIGxvbmdlciByZXNwb25zZXMgc2NvcmUgaGlnaGVyIHJlZ2FyZGxlc3Mgb2YgY29udGVudC4gQ2xpcCByZXNwb25zZSBsZW5ndGhzIGR1cmluZyB0cmFpbmluZyBhbmQgYXBwbHkgbGVuZ3RoIG5vcm1hbGl6YXRpb24gaW4gdGhlIFJNIHRvIHByZXZlbnQgdGhpcy4gTW9zdCBwcm9kdWN0aW9uIFJMSEYgcGlwZWxpbmVzIGNhcCBjb21wbGV0aW9ucyBhdCA1MTItMTAyNCB0b2tlbnMgYW5kIHN1YnRyYWN0IGEgbGVuZ3RoIHBlbmFsdHkgZnJvbSBSTSBzY29yZXMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9uaXRvcmluZyBLTCBkaXZlcmdlbmNlLCByZXNwb25zZSBsZW5ndGggZGlzdHJpYnV0aW9ucywgYW5kIHJld2FyZCBzY29yZSB2YXJpYW5jZSB0aHJvdWdob3V0IFJMSEYgdHJhaW5pbmcgcHJvdmlkZXMgZWFybHkgd2FybmluZyBvZiBpbnN0YWJpbGl0eS4gQWRhcHRpdmUgS0wgY29udHJvbCBhbmQgcmV3YXJkIG1vZGVsIGVuc2VtYmxlcyBhcmUgdGhlIG1vc3QgZWZmZWN0aXZlIG1pdGlnYXRpb25zIGF2YWlsYWJsZSBiZWZvcmUgc3dpdGNoaW5nIHRvIGFsdGVybmF0aXZlIGFsZ29yaXRobXMgbGlrZSBEUE8gdGhhdCBhdm9pZCB0aGUgUkwgbG9vcCBlbnRpcmVseS4ifV0="
---
# RLHF Instability — Reward Hacking, KL Divergence, and Training Collapse

RLHF training with PPO is notoriously unstable. The policy must learn from a noisy proxy reward signal, balance multiple competing objectives, and maintain coherent generation — all while the reward model may be easily exploited. Understanding failure modes and their detection is essential for successfully training production-grade RLHF systems.

## Reward Hacking and Goodhart's Law

Goodhart's Law states: when a measure becomes a target, it ceases to be a good measure. In RLHF, the reward model is a proxy for human preference. Once the policy learns to maximize RM scores rather than true quality, reward hacking occurs — the RM score diverges upward while actual response quality plateaus or degrades. The policy exploits weaknesses in the RM rather than learning genuine helpfulness.

- Length bias: policies learn that longer responses score higher regardless of content quality
- Repetition: repeating key phrases or sentences inflates word count and exploits n-gram-based RM features
- Formatting hacks: excessive bullet points, headers, and numbered lists mimic structure that human raters prefer
- Sycophantic openers: phrases like 'Great question!' correlate with high human ratings and get exploited
- Hedging overuse: excessive qualifications and caveats signal carefulness to RMs trained on careful human responses

## Adaptive KL Controller

The adaptive KL controller adjusts the beta coefficient during training to maintain a target KL divergence. If the measured KL exceeds the target, beta increases (penalizing drift more strongly). If KL is below target, beta decreases (allowing more exploration). This PID-style control prevents both reward hacking via unconstrained drift and over-constraint that stalls learning.

```python
import numpy as np
import torch

class AdaptiveKLController:
    # PID-style adaptive KL controller for RLHF training stability
    def __init__(
        self,
        init_kl_coef: float = 0.1,
        target_kl: float = 6.0,
        horizon: int = 10000,
    ):
        self.kl_coef = init_kl_coef
        self.target_kl = target_kl
        self.horizon = horizon

    def update(self, current_kl: float, n_steps: int) -> float:
        # Adjust KL coefficient based on measured vs target KL divergence
        proportional_error = np.clip(current_kl / self.target_kl - 1, -0.2, 0.2)
        mult = 1 + proportional_error * n_steps / self.horizon
        self.kl_coef *= mult
        return self.kl_coef

def rlhf_train_step(kl_controller, policy_logprobs, ref_logprobs, mask):
    per_token_kl = (policy_logprobs - ref_logprobs) * mask
    mean_kl = per_token_kl.sum() / mask.sum()
    new_beta = kl_controller.update(mean_kl.item(), n_steps=64)
    print(f"KL: {mean_kl:.3f} | beta: {new_beta:.4f} | target: {kl_controller.target_kl}")
    return new_beta, mean_kl
```

## Reward Hacking Detection

Automatic detection of reward hacking enables early intervention before training diverges. Key signals include response length explosion, repetition rates above 15%, sycophantic opener frequency, and rapid RM score increases without corresponding quality improvement. These metrics should be logged at every rollout step and compared against baseline SFT output statistics.

```python
import re
import numpy as np
from collections import Counter

def detect_reward_hacking(completions: list, rm_scores: list, step: int) -> dict:
    # Monitor RLHF completions for common reward hacking patterns
    metrics = {}
    lengths = [len(c.split()) for c in completions]
    metrics["mean_length"] = np.mean(lengths)
    metrics["length_std"] = np.std(lengths)

    def repetition_rate(text):
        tokens = text.lower().split()
        if len(tokens) < 2:
            return 0.0
        bigrams = list(zip(tokens[:-1], tokens[1:]))
        counts = Counter(bigrams)
        repeated = sum(v - 1 for v in counts.values() if v > 1)
        return repeated / len(bigrams)

    metrics["mean_repetition"] = np.mean([repetition_rate(c) for c in completions])
    sycophantic_re = r"^(great question|absolutely|certainly|of course|excellent)"
    metrics["sycophancy_rate"] = np.mean([
        bool(re.match(sycophantic_re, c.strip().lower())) for c in completions
    ])
    metrics["rm_mean"] = np.mean(rm_scores)
    metrics["rm_std"] = np.std(rm_scores)
    if metrics["mean_repetition"] > 0.15 or metrics["mean_length"] > 500:
        print(f"[Step {step}] WARNING: Possible reward hacking detected!")
    return metrics
```

## KL Divergence Monitoring

KL divergence between the current policy and the frozen reference is the primary stability indicator in RLHF. A KL above 24 nats typically signals the policy has drifted into a degenerate regime. Most successful RLHF runs maintain KL between 3 and 12 nats throughout training. Both mean batch KL and maximum per-sequence KL should be tracked to catch outlier sequences early.

```python
import torch

def compute_batch_kl(
    policy_logprobs: torch.Tensor,
    ref_logprobs: torch.Tensor,
    response_mask: torch.Tensor,
) -> dict:
    # Compute KL(pi_theta || pi_ref) per batch for monitoring
    per_token_kl = policy_logprobs - ref_logprobs  # [batch, seq_len]
    masked_kl = per_token_kl * response_mask
    # Per-sequence KL averaged over response tokens
    seq_kl = masked_kl.sum(dim=1) / response_mask.sum(dim=1).clamp(min=1)
    batch_kl = seq_kl.mean().item()
    max_kl = seq_kl.max().item()
    # Flag divergence: batch KL above 4x the typical InstructGPT target
    kl_exploding = batch_kl > 24.0
    if kl_exploding:
        print(f"WARNING: KL divergence exploding — batch_kl={batch_kl:.2f}")
    return {
        "batch_kl": batch_kl,
        "max_seq_kl": max_kl,
        "kl_per_seq": seq_kl.cpu().numpy(),
        "kl_exploding": kl_exploding,
    }
```

## Reward Model Ensemble

Using multiple reward models with different architectures or training seeds provides two benefits: ensemble averaging reduces the impact of individual RM biases, and variance across RMs identifies out-of-distribution outputs that individual RMs may score incorrectly. High variance is a reliable signal that the policy is generating content far from the RM's training distribution.

```python
import torch

def ensemble_reward_score(
    reward_models: list,
    input_ids: torch.Tensor,
    attention_mask: torch.Tensor,
    device: str = "cuda",
) -> dict:
    # Average rewards from multiple RMs; variance signals uncertainty
    all_scores = []
    with torch.no_grad():
        for rm in reward_models:
            rm.eval()
            outputs = rm(
                input_ids=input_ids.to(device),
                attention_mask=attention_mask.to(device),
            )
            scores = outputs.logits.squeeze(-1)  # [batch]
            all_scores.append(scores)
    stacked = torch.stack(all_scores, dim=0)  # [n_models, batch]
    ensemble_mean = stacked.mean(dim=0)        # [batch] mean reward
    ensemble_var = stacked.var(dim=0)           # [batch] uncertainty
    # Flag high-uncertainty samples (potential OOD or adversarial inputs)
    threshold = ensemble_var.mean() + 2 * ensemble_var.std()
    high_uncertainty = ensemble_var > threshold
    return {"mean_reward": ensemble_mean, "variance": ensemble_var, "uncertain_mask": high_uncertainty}
```

## RLHF Failure Modes

| Failure Mode | Symptom | Detection Method | Fix |
| --- | --- | --- | --- |
| Reward hacking | Verbose, repetitive, sycophantic outputs | Monitor length, repetition rate, RM score variance | Length normalization, RM diversity, response filtering |
| KL explosion | Generic or nonsensical responses | Track KL(pi_theta || pi_ref) per batch | Adaptive KL coefficient, reduce learning rate |
| Value instability | PPO loss oscillates, advantage estimates noisy | Monitor value loss and explained variance ratio | Normalize rewards, use separate value optimizer |
| Mode collapse | Policy repeats same short outputs for all prompts | Response diversity metrics and entropy monitoring | Increase sampling temperature, add entropy bonus reward |

## RLHF vs DPO Stability

DPO (Direct Preference Optimization) sidesteps all RL instabilities by reframing alignment as supervised learning over preference pairs. By eliminating the reward model, value function, and online rollout loop, DPO avoids reward hacking, KL explosion, and value instability entirely — at the cost of online learning capability and potential reward generalization on unseen prompt distributions.

> **Info**: Reward hacking in RLHF is often driven by RM length bias — policies learn to produce verbose responses because longer responses score higher regardless of content. Clip response lengths during training and apply length normalization in the RM to prevent this. Most production RLHF pipelines cap completions at 512-1024 tokens and subtract a length penalty from RM scores.

---

Monitoring KL divergence, response length distributions, and reward score variance throughout RLHF training provides early warning of instability. Adaptive KL control and reward model ensembles are the most effective mitigations available before switching to alternative algorithms like DPO that avoid the RL loop entirely.

