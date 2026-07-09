---
title: "Gaussian Process Definition — Mean and Covariance Functions"
slug: "gaussian-process-definition"
description: "A rigorous introduction to Gaussian processes as distributions over functions. Covers the mean function, covariance function, GP priors, marginalization consistency, connection to RKHS, and the Bayesian model structure of GPs."
tags: ["kernel-methods", "gaussian-processes", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBHYXVzc2lhbiBQcm9jZXNzIChHUCkgaXMgYSBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb24gb3ZlciBmdW5jdGlvbnMuIFJhdGhlciB0aGFuIHBhcmFtZXRlcml6aW5nIGEgZnVuY3Rpb24gYnkgYSBmaW5pdGUgbnVtYmVyIG9mIHdlaWdodHMgKGFzIGluIG5ldXJhbCBuZXR3b3JrcyksIGEgR1AgZGVmaW5lcyBhIGNvbnNpc3RlbnQgZGlzdHJpYnV0aW9uIG92ZXIgYWxsIHBvc3NpYmxlIGZ1bmN0aW9uIHZhbHVlcyBzaW11bHRhbmVvdXNseS4gQW55IGZpbml0ZSBjb2xsZWN0aW9uIG9mIGZ1bmN0aW9uIGV2YWx1YXRpb25zIGZvbGxvd3MgYSBtdWx0aXZhcmlhdGUgR2F1c3NpYW4gZGlzdHJpYnV0aW9uLiBHUHMgYXJlIHRoZSBjYW5vbmljYWwgbm9ucGFyYW1ldHJpYyBCYXllc2lhbiBtb2RlbCBmb3IgcmVncmVzc2lvbjogdGhleSBleHByZXNzIHByaW9yIGJlbGllZnMgdGhyb3VnaCBhIG1lYW4gZnVuY3Rpb24gYW5kIGNvdmFyaWFuY2UgZnVuY3Rpb24sIHVwZGF0ZSB0aG9zZSBiZWxpZWZzIHdpdGggZGF0YSB2aWEgQmF5ZXNcdTAwMjcgcnVsZSwgYW5kIHByb2R1Y2UgY2FsaWJyYXRlZCB1bmNlcnRhaW50eSBlc3RpbWF0ZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRm9ybWFsIERlZmluaXRpb24gb2YgYSBHUCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBHYXVzc2lhbiBQcm9jZXNzIGYgfiBHUChtLCBrKSBpcyBhIGNvbGxlY3Rpb24gb2YgcmFuZG9tIHZhcmlhYmxlcyB7Zih4KSA6IHgg4oiIIFh9IHN1Y2ggdGhhdCBhbnkgZmluaXRlIG1hcmdpbmFsIHtmKHjigoEpLCDigKYsIGYoeOKCmSl9IGlzIGpvaW50bHkgR2F1c3NpYW4gd2l0aCBtZWFuIHZlY3RvciDOvOG1oiA9IG0oeOG1oikgYW5kIGNvdmFyaWFuY2UgbWF0cml4IEvhtaLisbwgPSBrKHjhtaIsIHjisbwpLiBUaGUgZW50aXJlIGRpc3RyaWJ1dGlvbiBpcyBzcGVjaWZpZWQgYnkganVzdCB0d28gZnVuY3Rpb25zOiB0aGUgbWVhbiBmdW5jdGlvbiBtIDogWCDihpIg4oSdIGFuZCB0aGUgY292YXJpYW5jZSBmdW5jdGlvbiAoa2VybmVsKSBrIDogWCDDlyBYIOKGkiDihJ0uIFRoaXMgaW5maW5pdGUtZGltZW5zaW9uYWwgY29uc2lzdGVuY3kgaXMgZ3VhcmFudGVlZCBieSB0aGUgS29sbW9nb3JvdiBleHRlbnNpb24gdGhlb3JlbSwgd2hpY2ggcmVxdWlyZXMgb25seSB0aGF0IGFsbCBmaW5pdGUgbWFyZ2luYWxzIGFyZSBjb25zaXN0ZW50LiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50IjoiZiBcXHNpbSBcXG1hdGhjYWx7R1B9KG0sIGspIFxcaWZmIFxcYmVnaW57cG1hdHJpeH0gZih4XzEpIFxcXFwgXFx2ZG90cyBcXFxcIGYoeF9uKSBcXGVuZHtwbWF0cml4fSBcXHNpbSBcXG1hdGhjYWx7Tn1cXCFcXGxlZnQoXFxiZWdpbntwbWF0cml4fSBtKHhfMSkgXFxcXCBcXHZkb3RzIFxcXFwgbSh4X24pIFxcZW5ke3BtYXRyaXh9LCBcXGJlZ2lue3BtYXRyaXh9IGsoeF8xLHhfMSkgXHUwMDI2IFxcY2RvdHMgXHUwMDI2IGsoeF8xLHhfbikgXFxcXCBcXHZkb3RzIFx1MDAyNiBcXGRkb3RzIFx1MDAyNiBcXHZkb3RzIFxcXFwgayh4X24seF8xKSBcdTAwMjYgXFxjZG90cyBcdTAwMjYgayh4X24seF9uKSBcXGVuZHtwbWF0cml4fVxccmlnaHQpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVhbiBGdW5jdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1lYW4gZnVuY3Rpb24gbSh4KSA9IEVbZih4KV0gc3BlY2lmaWVzIHRoZSBleHBlY3RlZCBmdW5jdGlvbiB2YWx1ZSBhdCBlYWNoIGlucHV0IHguIFRoZSBtb3N0IGNvbW1vbiBjaG9pY2UgaXMgemVybyBtZWFuIG0oeCkgPSAwLCB3aGljaCBpcyBhcHByb3ByaWF0ZSB3aGVuIHRoZSBkYXRhIGlzIGNlbnRlcmVkIGFuZCBubyBzdHJvbmcgcHJpb3IgYWJvdXQgdGhlIGZ1bmN0aW9uXHUwMDI3cyBiYXNlbGluZSBpcyBhdmFpbGFibGUuIExpbmVhciBtZWFuIGZ1bmN0aW9ucyBtKHgpID0gYeG1gHggKyBiIGFyZSB1c2VmdWwgd2hlbiB0aGUgZnVuY3Rpb24gaXMgZXhwZWN0ZWQgdG8gdHJlbmQgbGluZWFybHkgb3V0c2lkZSB0aGUgdHJhaW5pbmcgZG9tYWluLiBQb2x5bm9taWFsIG9yIG5ldXJhbC1uZXR3b3JrLWJhc2VkIG1lYW4gZnVuY3Rpb25zIGFyZSB1c2VkIGZvciBjb21wbGV4IHRyZW5kcy4gVGhlIGNob2ljZSBtYXR0ZXJzIG1vc3QgZm9yIGV4dHJhcG9sYXRpb247IHdpdGhpbiB0aGUgdHJhaW5pbmcgZGF0YSwgdGhlIHBvc3RlcmlvciBhZGFwdHMgcmVnYXJkbGVzcyBvZiB0aGUgcHJpb3IgbWVhbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb3ZhcmlhbmNlIEZ1bmN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY292YXJpYW5jZSBmdW5jdGlvbiAoa2VybmVsKSBrKHgsIHhcdTAwMjcpID0gQ292W2YoeCksIGYoeFx1MDAyNyldID0gRVsoZih4KeKIkm0oeCkpKGYoeFx1MDAyNyniiJJtKHhcdTAwMjcpKV0gY29tcGxldGVseSBkZXRlcm1pbmVzIHRoZSBjb3JyZWxhdGlvbiBzdHJ1Y3R1cmUgb2YgdGhlIHByaW9yLiBIaWdoIGsoeCwgeFx1MDAyNykgbWVhbnMgZih4KSBhbmQgZih4XHUwMDI3KSB0ZW5kIHRvIGJlIGNsb3NlOyBsb3cgayh4LCB4XHUwMDI3KSBtZWFucyB0aGV5IGNhbiB2YXJ5IGluZGVwZW5kZW50bHkuIFRoZSBrZXJuZWwgZW5jb2RlcyBzbW9vdGhuZXNzIChob3cgcXVpY2tseSBjb3JyZWxhdGlvbnMgZGVjYXkgd2l0aCBkaXN0YW5jZSksIHBlcmlvZGljaXR5LCBzdGF0aW9uYXJpdHksIGFuZCBvdGhlciBzdHJ1Y3R1cmFsIGFzc3VtcHRpb25zLiBUaGUga2VybmVsIG11c3QgYmUgYSBNZXJjZXIga2VybmVsIChQU0QpIHNvIHRoYXQgdGhlIGNvdmFyaWFuY2UgbWF0cml4IGlzIGFsd2F5cyB2YWxpZC4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6ImsoeCwgeFx1MDAyNykgPSBcXHRleHR7Q292fVtmKHgpLCBmKHhcdTAwMjcpXSA9IFxcbWF0aGJie0V9XFxiaWdbKGYoeCkgLSBtKHgpKShmKHhcdTAwMjcpIC0gbSh4XHUwMDI3KSlcXGJpZ10ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkdQID0gTm9ucGFyYW1ldHJpYyBCYXllc2lhbiBNb2RlbCIsImNvbnRlbnQiOiJUcmFkaXRpb25hbCBwYXJhbWV0cmljIG1vZGVscyBoYXZlIGEgZml4ZWQgbnVtYmVyIG9mIHBhcmFtZXRlcnMgKGUuZy4sIHdlaWdodHMgaW4gbGluZWFyIHJlZ3Jlc3Npb24pLiBHUHMgYXJlIG5vbnBhcmFtZXRyaWM6IHRoZSBlZmZlY3RpdmUgY29tcGxleGl0eSBncm93cyB3aXRoIHRoZSBkYXRhLiBBZGRpbmcgbW9yZSBvYnNlcnZhdGlvbnMgY2FuIGFsd2F5cyBpbmNyZWFzZSBtb2RlbCBleHByZXNzaXZlbmVzcy4gVGhpcyBtYWtlcyBHUHMgYSBCYXllc2lhbiBtb2RlbCBvdmVyIGZ1bmN0aW9uIHNwYWNlcyByYXRoZXIgdGhhbiBwYXJhbWV0ZXIgc3BhY2VzIOKAlCB0aGUgcHJpb3IgaXMgYSBkaXN0cmlidXRpb24gb3ZlciBmdW5jdGlvbnMsIGFuZCB0aGUgcG9zdGVyaW9yIGlzIHVwZGF0ZWQgY29uc2lzdGVudGx5IHZpYSBCYXllc1x1MDAyNyBydWxlIGFzIGRhdGEgYXJyaXZlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHUCBhcyBhIERpc3RyaWJ1dGlvbiBPdmVyIEZ1bmN0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBHUCBwcmlvciBmIH4gR1AoMCwgaykgZGVmaW5lcyBhIHByb2JhYmlsaXR5IG1lYXN1cmUgb3ZlciB0aGUgc3BhY2Ugb2YgZnVuY3Rpb25zIEMoWCkgKGNvbnRpbnVvdXMgZnVuY3Rpb25zIG9uIFgpLiBEcmF3aW5nIGEgc2FtcGxlIGZyb20gdGhlIHByaW9yIG1lYW5zIGRyYXdpbmcgYSB3aG9sZSBmdW5jdGlvbiBmIDogWCDihpIg4oSdLCBub3QganVzdCBhIGZpbml0ZS1kaW1lbnNpb25hbCB2ZWN0b3IuIFRoZSBzYW1wbGUgZnVuY3Rpb25zIGFyZSBjb250aW51b3VzIGlmIHRoZSBrZXJuZWwgaXMgY29udGludW91cywgYW5kIHRoZWlyIHNtb290aG5lc3MgaXMgZGV0ZXJtaW5lZCBieSB0aGUga2VybmVsOiBSQkYga2VybmVscyBwcm9kdWNlIEPiiJ4gc2FtcGxlczsgTWF0w6lybi3OvSBrZXJuZWxzIHByb2R1Y2Ugc2FtcGxlcyB3aXRoIOKMis694oyLIGNvbnRpbnVvdXMgZGVyaXZhdGl2ZXMuIFRoaXMgaXMgdGhlIHNlbnNlIGluIHdoaWNoIEdQcyBhcmUgaW5maW5pdGUtZGltZW5zaW9uYWwgcHJpb3JzIOKAlCB0aGV5IGFzc2lnbiBwcm9iYWJpbGl0eSB0byBlbnRpcmUgZnVuY3Rpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbm5lY3Rpb24gdG8gUktIUyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBzdWJ0bGUgYnV0IGltcG9ydGFudCBmYWN0OiBHUCBzYW1wbGUgcGF0aHMgYXJlIGFsbW9zdCBzdXJlbHkgTk9UIGluIHRoZSBSS0hTIEhfay4gVGhlIFJLSFMgbm9ybSDigJZm4oCWX2sgb2YgYSB0eXBpY2FsIEdQIHNhbXBsZSBpcyBpbmZpbml0ZS4gSG93ZXZlciwgdGhlIHBvc3RlcmlvciBtZWFuIGZ1bmN0aW9uIChhZnRlciBjb25kaXRpb25pbmcgb24gZGF0YSkgSVMgaW4gSF9rIGFuZCBlcXVhbHMgdGhlIGtlcm5lbCByaWRnZSByZWdyZXNzaW9uIHNvbHV0aW9uLiBUaGlzIGFwcGFyZW50IHBhcmFkb3ggaXMgcmVzb2x2ZWQgYnkgbm90aW5nIHRoYXQgSF9rIGNvbnRhaW5zIHRoZSBcdTAwMjdzbW9vdGhcdTAwMjcgZnVuY3Rpb25zLCB3aGlsZSBHUCBzYW1wbGVzIGluY2x1ZGUgcm91Z2hlciBwYXRocyB3aXRoIHByb2JhYmlsaXR5IDEuIFRoZSBSS0hTIGFuZCBHUCBwcmlvciBhcmUgY29tcGxlbWVudGFyeTogdGhlIFJLSFMgaXMgd2hlcmUgdGhlIHBvc3RlcmlvciBtZWFuIGxpdmVzLCBhbmQgdGhlIEdQIHByaW9yIGdlbmVyYXRlcyB0aGUgZnVsbCBkaXN0cmlidXRpb24gaW5jbHVkaW5nIHVuY2VydGFpbnR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdQIGFzIGEgQmF5ZXNpYW4gTW9kZWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBCYXllc2lhbiBzdHJ1Y3R1cmUgb2YgYSBHUCBpcyBleHBsaWNpdDogdGhlIHByaW9yIGYgfiBHUChtLCBrKSBhc3NpZ25zIHByb2JhYmlsaXR5IHRvIGV2ZXJ5IGZ1bmN0aW9uOyB0aGUgbGlrZWxpaG9vZCBwKHkgfCBmLCBYKSA9IE4oeTsgZihYKSwgz4PCsl9uIEkpIG1vZGVscyBub2lzeSBvYnNlcnZhdGlvbnM7IHRoZSBwb3N0ZXJpb3IgcChmIHwgWCwgeSkg4oidIHAoeSB8IGYsIFgpIHAoZikgaXMgYWdhaW4gYSBHUCAoZHVlIHRvIEdhdXNzaWFuIGNvbmp1Z2FjeSkuIFRoaXMgcG9zdGVyaW9yIGlzIGNvbXB1dGVkIGFuYWx5dGljYWxseSDigJQgbm8gTUNNQyBvciB2YXJpYXRpb25hbCBpbmZlcmVuY2UgbmVlZGVkLiBUaGUgbWFyZ2luYWwgbGlrZWxpaG9vZCBwKHkgfCBYKSA9IOKIqyBwKHl8ZixYKSBwKGYpIGRmIGlzIGFsc28gR2F1c3NpYW4gYW5kIHVzZWQgdG8gb3B0aW1pemUga2VybmVsIGh5cGVycGFyYW1ldGVycy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlByaW9yOiBmIH4gR1AobSwgaykg4oCUIGRpc3RyaWJ1dGlvbiBvdmVyIGZ1bmN0aW9ucyBlbmNvZGluZyBzbW9vdGhuZXNzIGFzc3VtcHRpb25zLiIsIkxpa2VsaWhvb2Q6IHkgfCBmIH4gTihmKFgpLCDPg8KyX24gSSkg4oCUIEdhdXNzaWFuIG9ic2VydmF0aW9uIG5vaXNlIG1vZGVsLiIsIlBvc3RlcmlvcjogZiB8IFgsIHkgfiBHUChtX3Bvc3QsIGtfcG9zdCkg4oCUIHVwZGF0ZWQgZGlzdHJpYnV0aW9uIG92ZXIgZnVuY3Rpb25zIGdpdmVuIGRhdGEuIiwiTWFyZ2luYWwgbGlrZWxpaG9vZDogcCh5IHwgWCwgzrgpIOKAlCB1c2VkIHRvIG9wdGltaXplIGh5cGVycGFyYW1ldGVycyDOuCA9IHvihJMsIM+DwrIsIM+DwrJfbn0gYnkgTUxFLiIsIlByZWRpY3Rpb246IHAoZiogfCB4KiwgWCwgeSkgPSBOKM68Kiwgz4PCsiopIOKAlCBHYXVzc2lhbiBwcmVkaWN0aXZlIGRpc3RyaWJ1dGlvbiBhdCBuZXcgeCouIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgRXhhbXBsZXMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgZWxsPTEuMCwgc2lnbWEyPTEuMCk6XG4gICAgZGlmZiA9IFgxWzosIE5vbmUsIDpdIC0gWDJbTm9uZSwgOiwgOl1cbiAgICByZXR1cm4gc2lnbWEyICogbnAuZXhwKC1ucC5zdW0oZGlmZioqMiwgYXhpcz0tMSkgLyAoMiAqIGVsbCoqMikpXG5cbmRlZiBtYXRlcm41Ml9rZXJuZWwoWDEsIFgyLCBlbGw9MS4wLCBzaWdtYTI9MS4wKTpcbiAgICBkaWZmID0gWDFbOiwgTm9uZSwgOl0gLSBYMltOb25lLCA6LCA6XVxuICAgIHIgPSBucC5zcXJ0KG5wLnN1bShkaWZmKioyLCBheGlzPS0xKSkgLyBlbGxcbiAgICByZXR1cm4gc2lnbWEyICogKDEgKyBucC5zcXJ0KDUpKnIgKyA1KnIqKjIvMykgKiBucC5leHAoLW5wLnNxcnQoNSkqcilcblxuZGVmIHNhbXBsZV9ncF9wcmlvcih4LCBrZXJuZWxfZm4sIG5fc2FtcGxlcz01LCBzZWVkPTApOlxuICAgIFggPSB4WzosIE5vbmVdXG4gICAgSyA9IGtlcm5lbF9mbihYLCBYKSArIDFlLTggKiBucC5leWUobGVuKHgpKVxuICAgIEwgPSBucC5saW5hbGcuY2hvbGVza3koSylcbiAgICBybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoc2VlZClcbiAgICByZXR1cm4gKEwgQCBybmcucmFuZG4obGVuKHgpLCBuX3NhbXBsZXMpKS5UXG5cbnggPSBucC5saW5zcGFjZSgtNSwgNSwgMzAwKVxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDEsIDIsIGZpZ3NpemU9KDEyLCA0KSlcbmZvciBheCwgKG5hbWUsIGtmbikgaW4gemlwKGF4ZXMsIFtcbiAgICAoXHUwMDI3R1AgcHJpb3I6IFJCRiBlbGw9MVx1MDAyNywgbGFtYmRhIFgxLCBYMjogcmJmX2tlcm5lbChYMSwgWDIsIGVsbD0xLjApKSxcbiAgICAoXHUwMDI3R1AgcHJpb3I6IE1hdGVybi01LzIgZWxsPTFcdTAwMjcsIGxhbWJkYSBYMSwgWDI6IG1hdGVybjUyX2tlcm5lbChYMSwgWDIsIGVsbD0xLjApKSxcbl0pOlxuICAgIGZvciBzIGluIHNhbXBsZV9ncF9wcmlvcih4LCBrZm4pOlxuICAgICAgICBheC5wbG90KHgsIHMsIGFscGhhPTAuOClcbiAgICBheC5zZXRfdGl0bGUobmFtZSlcbiAgICBheC5zZXRfeGxhYmVsKFx1MDAyN3hcdTAwMjcpXG4gICAgYXguc2V0X3lsYWJlbChcdTAwMjdmKHgpXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdncF9wcmlvcl9zYW1wbGVzLnBuZ1x1MDAyNywgZHBpPTEwMClcbnByaW50KFx1MDAyN1NhdmVkIGdwX3ByaW9yX3NhbXBsZXMucG5nIC0tIGVhY2ggY3VydmUgaXMgb25lIGZ1bmN0aW9uIGRyYXduIGZyb20gR1AgcHJpb3JcdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcmJmX2tlcm5lbF9tYXRyaXgoWDEsIFgyLCBlbGw9MS4wLCBzaWdtYTI9MS4wKTpcbiAgICBkaWZmID0gWDFbOiwgTm9uZSwgOl0gLSBYMltOb25lLCA6LCA6XVxuICAgIHJldHVybiBzaWdtYTIgKiBucC5leHAoLW5wLnN1bShkaWZmKioyLCBheGlzPS0xKSAvICgyICogZWxsKioyKSlcblxueCA9IG5wLmxpbnNwYWNlKC01LCA1LCAzMDApWzosIE5vbmVdXG5jb25maWdzID0gW1xuICAgICgwLjUsIDEuMCwgXHUwMDI3ZWxsPTAuNSwgc2lnbWEyPTEgKHNob3J0IHJhbmdlKVx1MDAyNyksXG4gICAgKDIuMCwgMS4wLCBcdTAwMjdlbGw9Mi4wLCBzaWdtYTI9MSAobG9uZyByYW5nZSlcdTAwMjcpLFxuICAgICgxLjAsIDAuNSwgXHUwMDI3ZWxsPTEuMCwgc2lnbWEyPTAuNSAobG93IGFtcGxpdHVkZSlcdTAwMjcpLFxuXVxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDEsIDMsIGZpZ3NpemU9KDE0LCA0KSlcbmZvciBheCwgKGVsbCwgc2lnbWEyLCB0aXRsZSkgaW4gemlwKGF4ZXMsIGNvbmZpZ3MpOlxuICAgIEsgPSByYmZfa2VybmVsX21hdHJpeCh4LCB4LCBlbGw9ZWxsLCBzaWdtYTI9c2lnbWEyKVxuICAgIEsgKz0gMWUtOCAqIG5wLmV5ZShsZW4oeCkpXG4gICAgbWVhbiA9IG5wLnplcm9zKGxlbih4KSlcbiAgICBzdGQgPSBucC5zcXJ0KG5wLmRpYWcoSykpXG4gICAgYXguZmlsbF9iZXR3ZWVuKHgucmF2ZWwoKSwgbWVhbiAtIDIqc3RkLCBtZWFuICsgMipzdGQsIGFscGhhPTAuMiwgbGFiZWw9XHUwMDI3Ky8tMnNpZ21hXHUwMDI3KVxuICAgIGF4LmZpbGxfYmV0d2Vlbih4LnJhdmVsKCksIG1lYW4gLSBzdGQsICAgbWVhbiArIHN0ZCwgICBhbHBoYT0wLjMsIGxhYmVsPVx1MDAyNysvLTFzaWdtYVx1MDAyNylcbiAgICBheC5wbG90KHgsIG1lYW4sIFx1MDAyN2stLVx1MDAyNywgbGFiZWw9XHUwMDI3bWVhblx1MDAyNylcbiAgICBMID0gbnAubGluYWxnLmNob2xlc2t5KEspXG4gICAgcm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKDApXG4gICAgZm9yIF8gaW4gcmFuZ2UoMyk6XG4gICAgICAgIGF4LnBsb3QoeCwgTCBAIHJuZy5yYW5kbihsZW4oeCkpLCBhbHBoYT0wLjcpXG4gICAgYXguc2V0X3RpdGxlKHRpdGxlKVxuICAgIGF4LmxlZ2VuZChmb250c2l6ZT03KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdncF9wcmlvcl9iYW5kcy5wbmdcdTAwMjcsIGRwaT0xMDApXG5wcmludChcdTAwMjdTYXZlZCBncF9wcmlvcl9iYW5kcy5wbmdcdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweSBpbXBvcnQgc3RhdHNcblxuZGVmIHJiZl9rZXJuZWxfbWF0cml4KFgxLCBYMiwgZWxsPTEuMCk6XG4gICAgZGlmZiA9IFgxWzosIE5vbmUsIDpdIC0gWDJbTm9uZSwgOiwgOl1cbiAgICByZXR1cm4gbnAuZXhwKC1ucC5zdW0oZGlmZioqMiwgYXhpcz0tMSkgLyAoMiAqIGVsbCoqMikpXG5cbnJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZSg0MilcbnhfZnVsbCA9IG5wLmxpbnNwYWNlKC0zLCAzLCA1MClbOiwgTm9uZV1cbktfZnVsbCA9IHJiZl9rZXJuZWxfbWF0cml4KHhfZnVsbCwgeF9mdWxsKSArIDFlLTggKiBucC5leWUoNTApXG5MID0gbnAubGluYWxnLmNob2xlc2t5KEtfZnVsbClcblxuIyBEcmF3IG1hbnkgc2FtcGxlcyBmcm9tIHRoZSBmdWxsIEdQXG5uX3NhbXBsZXMgPSA1MDAwXG5zYW1wbGVzID0gKEwgQCBybmcucmFuZG4oNTAsIG5fc2FtcGxlcykpLlQgICMgc2hhcGUgKG5fc2FtcGxlcywgNTApXG5cbnByaW50KFx1MDAyN1ZlcmlmeWluZyBHUCBtYXJnaW5hbGl6YXRpb24gY29uc2lzdGVuY3k6XHUwMDI3KVxucHJpbnQoZlx1MDAyN3tcIkluZGV4XCI6XHUwMDNjOH0ge1wiRW1waXJpY2FsIHZhclwiOlx1MDAzYzE2fSB7XCJFeHBlY3RlZCB2YXJcIjpcdTAwM2MxNn0ge1wiS1MgcC12YWx1ZVwifVx1MDAyNylcbmZvciBpZHggaW4gWzEwLCAyNSwgNDBdOlxuICAgIG1hcmdpbmFsX3NhbXBsZXMgPSBzYW1wbGVzWzosIGlkeF1cbiAgICBrX2lpID0gS19mdWxsW2lkeCwgaWR4XVxuICAgIGtzX3N0YXQsIHBfdmFsdWUgPSBzdGF0cy5rc3Rlc3QobWFyZ2luYWxfc2FtcGxlcywgXHUwMDI3bm9ybVx1MDAyNywgYXJncz0oMCwgbnAuc3FydChrX2lpKSkpXG4gICAgcHJpbnQoZlx1MDAyN3tpZHg6XHUwMDNjOH0ge25wLnZhcihtYXJnaW5hbF9zYW1wbGVzKTpcdTAwM2MxNi40Zn0ge2tfaWk6XHUwMDNjMTYuNGZ9IHtwX3ZhbHVlOi4zZn1cdTAwMjcpXG5cbnByaW50KFx1MDAyN0FsbCBwLXZhbHVlcyBcdTAwM2UgMC4wNTogbWFyZ2luYWxzIGFyZSBjb25zaXN0ZW50IEdhdXNzaWFucyBhcyBleHBlY3RlZC5cdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcmJmX2tlcm5lbF9tYXRyaXgoWDEsIFgyLCBlbGw9MS4wLCBzaWdtYTI9MS4wKTpcbiAgICBkaWZmID0gWDFbOiwgTm9uZSwgOl0gLSBYMltOb25lLCA6LCA6XVxuICAgIHJldHVybiBzaWdtYTIgKiBucC5leHAoLW5wLnN1bShkaWZmKioyLCBheGlzPS0xKSAvICgyICogZWxsKioyKSlcblxuZGVmIHBvbHlub21pYWxfbWVhbihYLCBjb2VmZnMpOlxuICAgICMgUG9seW5vbWlhbCBtZWFuOiBtKHgpID0gc3VtX2kgY19pICogeF5pXG4gICAgcmV0dXJuIHN1bShjICogWC5yYXZlbCgpKippIGZvciBpLCBjIGluIGVudW1lcmF0ZShjb2VmZnMpKVxuXG54X3RyYWluID0gbnAubGluc3BhY2UoLTMsIDMsIDIwKVs6LCBOb25lXVxucm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKDUpXG50cnVlX21lYW4gPSAwLjUgKiB4X3RyYWluLnJhdmVsKCkqKjIgLSAxLjBcbnlfdHJhaW4gPSB0cnVlX21lYW4gKyAwLjMgKiBybmcucmFuZG4oMjApXG5cbiMgU3VidHJhY3QgcXVhZHJhdGljIG1lYW4sIGZpdCBHUCByZXNpZHVhbFxubWVhbl90cmFpbiA9IHBvbHlub21pYWxfbWVhbih4X3RyYWluLCBbMCwgMCwgMC41XSlcbnlfY2VudGVyZWQgPSB5X3RyYWluIC0gbWVhbl90cmFpblxuXG5sYW0gPSAwLjA1XG5LID0gcmJmX2tlcm5lbF9tYXRyaXgoeF90cmFpbiwgeF90cmFpbiwgZWxsPTAuOCkgKyBsYW0gKiBucC5leWUoMjApXG5hbHBoYSA9IG5wLmxpbmFsZy5zb2x2ZShLLCB5X2NlbnRlcmVkKVxuXG54X3Rlc3QgPSBucC5saW5zcGFjZSgtNCwgNCwgMjAwKVs6LCBOb25lXVxuS19zdGFyID0gcmJmX2tlcm5lbF9tYXRyaXgoeF90ZXN0LCB4X3RyYWluLCBlbGw9MC44KVxubWVhbl90ZXN0ID0gcG9seW5vbWlhbF9tZWFuKHhfdGVzdCwgWzAsIDAsIDAuNV0pXG55X3ByZWQgPSBtZWFuX3Rlc3QgKyBLX3N0YXIgQCBhbHBoYVxuXG5wbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSlcbnBsdC5zY2F0dGVyKHhfdHJhaW4sIHlfdHJhaW4sIGxhYmVsPVx1MDAyN1RyYWluaW5nIGRhdGFcdTAwMjcsIHpvcmRlcj01LCBzPTQwKVxucGx0LnBsb3QoeF90ZXN0LCB5X3ByZWQsIGxhYmVsPVx1MDAyN0dQIHByZWRpY3Rpb24gKHF1YWRyYXRpYyBtZWFuKVx1MDAyNywgY29sb3I9XHUwMDI3cmVkXHUwMDI3KVxucGx0LnBsb3QoeF90ZXN0LCBtZWFuX3Rlc3QsIFx1MDAyNy0tXHUwMDI3LCBsYWJlbD1cdTAwMjdNZWFuIGZ1bmN0aW9uIG9ubHlcdTAwMjcsIGNvbG9yPVx1MDAyN29yYW5nZVx1MDAyNywgYWxwaGE9MC43KVxucGx0LmxlZ2VuZCgpXG5wbHQudGl0bGUoXHUwMDI3R1Agd2l0aCBOb24tWmVybyBQb2x5bm9taWFsIE1lYW4gRnVuY3Rpb25cdTAwMjcpXG5wbHQuc2F2ZWZpZyhcdTAwMjdncF9ub256ZXJvX21lYW4ucG5nXHUwMDI3LCBkcGk9MTAwKVxucHJpbnQoXHUwMDI3U2F2ZWQgZ3Bfbm9uemVyb19tZWFuLnBuZ1x1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZXNpZ24gQ2hvaWNlcyBSZWZlcmVuY2UifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRGVzaWduIENob2ljZSIsIk9wdGlvbnMiLCJFZmZlY3Qgb24gUHJpb3IiLCJSZWNvbW1lbmRhdGlvbiJdLCJyb3dzIjpbWyJNZWFuIGZ1bmN0aW9uIG0oeCkiLCJaZXJvLCBsaW5lYXIsIHBvbHlub21pYWwsIG5ldXJhbCBuZXQiLCJDZW50ZXJzIHRoZSBwcmlvcjsgYWZmZWN0cyBleHRyYXBvbGF0aW9uIiwiVXNlIHplcm8gbWVhbiB3aXRoaW4gdHJhaW5pbmcgcmFuZ2U7IGxpbmVhci9wb2x5bm9taWFsIGZvciBleHRyYXBvbGF0aW9uIl0sWyJDb3ZhcmlhbmNlIGZ1bmN0aW9uIGsoeCx4XHUwMDI3KSIsIlJCRiwgTWF0w6lybiwgcG9seW5vbWlhbCwgcGVyaW9kaWMsIGNvbXBvc2l0ZSIsIkNvbnRyb2xzIHNtb290aG5lc3MgYW5kIGNvcnJlbGF0aW9uIHJhbmdlIiwiTWF0w6lybi01LzIgYXMgZGVmYXVsdDsgUkJGIGZvciB2ZXJ5IHNtb290aCBmdW5jdGlvbnMiXSxbIkxlbmd0aC1zY2FsZSDihJMiLCJGaXhlZCwgdHVuZWQgYnkgbWFyZ2luYWwgTUxFLCBjcm9zcy12YWxpZGF0ZWQiLCJDb250cm9scyBjb3JyZWxhdGlvbiBkZWNheSByYXRlIiwiTGVhcm4gdmlhIG1hcmdpbmFsIGxpa2VsaWhvb2QgbWF4aW1pemF0aW9uICh0eXBlLUlJIE1MRSkiXSxbIlNpZ25hbCB2YXJpYW5jZSDPg8KyIiwiRml4ZWQsIGxlYXJuZWQgZnJvbSBkYXRhIiwiT3ZlcmFsbCBmdW5jdGlvbiBhbXBsaXR1ZGUiLCJMZWFybiBmcm9tIGRhdGE7IGluaXRpYWxpemUgdG8gdmFyKHkpIl0sWyJOb2lzZSB2YXJpYW5jZSDPg8KyX24iLCJGaXhlZCwgbGVhcm5lZCwgaGV0ZXJvc2NlZGFzdGljIiwiU2VwYXJhdGVzIHNpZ25hbCBmcm9tIG9ic2VydmF0aW9uIG5vaXNlIiwiTGVhcm4gZnJvbSBkYXRhOyB1c2UgaGV0ZXJvc2NlZGFzdGljIG1vZGVsIGZvciB2YXJ5aW5nIG5vaXNlIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgR1AgaXMgZnVsbHkgc3BlY2lmaWVkIGJ5IG0gYW5kIGsuIFRoZSB6ZXJvLW1lYW4gUkJGIEdQIGlzIGEgcmVhc29uYWJsZSBzdGFydGluZyBwb2ludCBmb3IgbW9zdCByZWdyZXNzaW9uIHRhc2tzLiBGb3IgcHJvYmxlbXMgd2l0aCBrbm93biBzdHJ1Y3R1cmUg4oCUIHRyZW5kcywgcGVyaW9kaWNpdHksIGFkZGl0aXZlIGRlY29tcG9zaXRpb25zIOKAlCBlbmNvZGUgdGhhdCBzdHJ1Y3R1cmUgaW4gdGhlIG1lYW4gYW5kIGNvdmFyaWFuY2UgZnVuY3Rpb25zIHJhdGhlciB0aGFuIHJlbHlpbmcgb24gdGhlIGRhdGEgYWxvbmUuIEh5cGVycGFyYW1ldGVycyBhcmUgbGVhcm5lZCBieSBtYXhpbWl6aW5nIHRoZSBsb2cgbWFyZ2luYWwgbGlrZWxpaG9vZCBsb2cgcCh5IHwgWCwgzrgpLCB3aGljaCBhdXRvbWF0aWNhbGx5IGJhbGFuY2VzIGRhdGEgZml0IGFuZCBwcmlvciBjb21wbGV4aXR5LiJ9XQ=="
---
# Gaussian Process Definition — Mean and Covariance Functions

A Gaussian Process (GP) is a probability distribution over functions. Rather than parameterizing a function by a finite number of weights (as in neural networks), a GP defines a consistent distribution over all possible function values simultaneously. Any finite collection of function evaluations follows a multivariate Gaussian distribution. GPs are the canonical nonparametric Bayesian model for regression: they express prior beliefs through a mean function and covariance function, update those beliefs with data via Bayes' rule, and produce calibrated uncertainty estimates.

## Formal Definition of a GP

A Gaussian Process f ~ GP(m, k) is a collection of random variables {f(x) : x ∈ X} such that any finite marginal {f(x₁), …, f(xₙ)} is jointly Gaussian with mean vector μᵢ = m(xᵢ) and covariance matrix Kᵢⱼ = k(xᵢ, xⱼ). The entire distribution is specified by just two functions: the mean function m : X → ℝ and the covariance function (kernel) k : X × X → ℝ. This infinite-dimensional consistency is guaranteed by the Kolmogorov extension theorem, which requires only that all finite marginals are consistent.

$$f \sim \mathcal{GP}(m, k) \iff \begin{pmatrix} f(x_1) \\ \vdots \\ f(x_n) \end{pmatrix} \sim \mathcal{N}\!\left(\begin{pmatrix} m(x_1) \\ \vdots \\ m(x_n) \end{pmatrix}, \begin{pmatrix} k(x_1,x_1) & \cdots & k(x_1,x_n) \\ \vdots & \ddots & \vdots \\ k(x_n,x_1) & \cdots & k(x_n,x_n) \end{pmatrix}\right)$$

## Mean Function

The mean function m(x) = E[f(x)] specifies the expected function value at each input x. The most common choice is zero mean m(x) = 0, which is appropriate when the data is centered and no strong prior about the function's baseline is available. Linear mean functions m(x) = aᵀx + b are useful when the function is expected to trend linearly outside the training domain. Polynomial or neural-network-based mean functions are used for complex trends. The choice matters most for extrapolation; within the training data, the posterior adapts regardless of the prior mean.

## Covariance Function

The covariance function (kernel) k(x, x') = Cov[f(x), f(x')] = E[(f(x)−m(x))(f(x')−m(x'))] completely determines the correlation structure of the prior. High k(x, x') means f(x) and f(x') tend to be close; low k(x, x') means they can vary independently. The kernel encodes smoothness (how quickly correlations decay with distance), periodicity, stationarity, and other structural assumptions. The kernel must be a Mercer kernel (PSD) so that the covariance matrix is always valid.

$$k(x, x') = \text{Cov}[f(x), f(x')] = \mathbb{E}\big[(f(x) - m(x))(f(x') - m(x'))\big]$$

> **GP = Nonparametric Bayesian Model**: Traditional parametric models have a fixed number of parameters (e.g., weights in linear regression). GPs are nonparametric: the effective complexity grows with the data. Adding more observations can always increase model expressiveness. This makes GPs a Bayesian model over function spaces rather than parameter spaces — the prior is a distribution over functions, and the posterior is updated consistently via Bayes' rule as data arrives.

## GP as a Distribution Over Functions

A GP prior f ~ GP(0, k) defines a probability measure over the space of functions C(X) (continuous functions on X). Drawing a sample from the prior means drawing a whole function f : X → ℝ, not just a finite-dimensional vector. The sample functions are continuous if the kernel is continuous, and their smoothness is determined by the kernel: RBF kernels produce C∞ samples; Matérn-ν kernels produce samples with ⌊ν⌋ continuous derivatives. This is the sense in which GPs are infinite-dimensional priors — they assign probability to entire functions.

## Connection to RKHS

A subtle but important fact: GP sample paths are almost surely NOT in the RKHS H_k. The RKHS norm ‖f‖_k of a typical GP sample is infinite. However, the posterior mean function (after conditioning on data) IS in H_k and equals the kernel ridge regression solution. This apparent paradox is resolved by noting that H_k contains the 'smooth' functions, while GP samples include rougher paths with probability 1. The RKHS and GP prior are complementary: the RKHS is where the posterior mean lives, and the GP prior generates the full distribution including uncertainty.

## GP as a Bayesian Model

The Bayesian structure of a GP is explicit: the prior f ~ GP(m, k) assigns probability to every function; the likelihood p(y | f, X) = N(y; f(X), σ²_n I) models noisy observations; the posterior p(f | X, y) ∝ p(y | f, X) p(f) is again a GP (due to Gaussian conjugacy). This posterior is computed analytically — no MCMC or variational inference needed. The marginal likelihood p(y | X) = ∫ p(y|f,X) p(f) df is also Gaussian and used to optimize kernel hyperparameters.

- Prior: f ~ GP(m, k) — distribution over functions encoding smoothness assumptions.
- Likelihood: y | f ~ N(f(X), σ²_n I) — Gaussian observation noise model.
- Posterior: f | X, y ~ GP(m_post, k_post) — updated distribution over functions given data.
- Marginal likelihood: p(y | X, θ) — used to optimize hyperparameters θ = {ℓ, σ², σ²_n} by MLE.
- Prediction: p(f* | x*, X, y) = N(μ*, σ²*) — Gaussian predictive distribution at new x*.

## Code Examples

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sigma2=1.0):
    diff = X1[:, None, :] - X2[None, :, :]
    return sigma2 * np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

def matern52_kernel(X1, X2, ell=1.0, sigma2=1.0):
    diff = X1[:, None, :] - X2[None, :, :]
    r = np.sqrt(np.sum(diff**2, axis=-1)) / ell
    return sigma2 * (1 + np.sqrt(5)*r + 5*r**2/3) * np.exp(-np.sqrt(5)*r)

def sample_gp_prior(x, kernel_fn, n_samples=5, seed=0):
    X = x[:, None]
    K = kernel_fn(X, X) + 1e-8 * np.eye(len(x))
    L = np.linalg.cholesky(K)
    rng = np.random.RandomState(seed)
    return (L @ rng.randn(len(x), n_samples)).T

x = np.linspace(-5, 5, 300)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for ax, (name, kfn) in zip(axes, [
    ('GP prior: RBF ell=1', lambda X1, X2: rbf_kernel(X1, X2, ell=1.0)),
    ('GP prior: Matern-5/2 ell=1', lambda X1, X2: matern52_kernel(X1, X2, ell=1.0)),
]):
    for s in sample_gp_prior(x, kfn):
        ax.plot(x, s, alpha=0.8)
    ax.set_title(name)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
plt.tight_layout()
plt.savefig('gp_prior_samples.png', dpi=100)
print('Saved gp_prior_samples.png -- each curve is one function drawn from GP prior')
```

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel_matrix(X1, X2, ell=1.0, sigma2=1.0):
    diff = X1[:, None, :] - X2[None, :, :]
    return sigma2 * np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

x = np.linspace(-5, 5, 300)[:, None]
configs = [
    (0.5, 1.0, 'ell=0.5, sigma2=1 (short range)'),
    (2.0, 1.0, 'ell=2.0, sigma2=1 (long range)'),
    (1.0, 0.5, 'ell=1.0, sigma2=0.5 (low amplitude)'),
]
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, (ell, sigma2, title) in zip(axes, configs):
    K = rbf_kernel_matrix(x, x, ell=ell, sigma2=sigma2)
    K += 1e-8 * np.eye(len(x))
    mean = np.zeros(len(x))
    std = np.sqrt(np.diag(K))
    ax.fill_between(x.ravel(), mean - 2*std, mean + 2*std, alpha=0.2, label='+/-2sigma')
    ax.fill_between(x.ravel(), mean - std,   mean + std,   alpha=0.3, label='+/-1sigma')
    ax.plot(x, mean, 'k--', label='mean')
    L = np.linalg.cholesky(K)
    rng = np.random.RandomState(0)
    for _ in range(3):
        ax.plot(x, L @ rng.randn(len(x)), alpha=0.7)
    ax.set_title(title)
    ax.legend(fontsize=7)
plt.tight_layout()
plt.savefig('gp_prior_bands.png', dpi=100)
print('Saved gp_prior_bands.png')
```

```python
import numpy as np
from scipy import stats

def rbf_kernel_matrix(X1, X2, ell=1.0):
    diff = X1[:, None, :] - X2[None, :, :]
    return np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

rng = np.random.RandomState(42)
x_full = np.linspace(-3, 3, 50)[:, None]
K_full = rbf_kernel_matrix(x_full, x_full) + 1e-8 * np.eye(50)
L = np.linalg.cholesky(K_full)

# Draw many samples from the full GP
n_samples = 5000
samples = (L @ rng.randn(50, n_samples)).T  # shape (n_samples, 50)

print('Verifying GP marginalization consistency:')
print(f'{"Index":<8} {"Empirical var":<16} {"Expected var":<16} {"KS p-value"}')
for idx in [10, 25, 40]:
    marginal_samples = samples[:, idx]
    k_ii = K_full[idx, idx]
    ks_stat, p_value = stats.kstest(marginal_samples, 'norm', args=(0, np.sqrt(k_ii)))
    print(f'{idx:<8} {np.var(marginal_samples):<16.4f} {k_ii:<16.4f} {p_value:.3f}')

print('All p-values > 0.05: marginals are consistent Gaussians as expected.')
```

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel_matrix(X1, X2, ell=1.0, sigma2=1.0):
    diff = X1[:, None, :] - X2[None, :, :]
    return sigma2 * np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

def polynomial_mean(X, coeffs):
    # Polynomial mean: m(x) = sum_i c_i * x^i
    return sum(c * X.ravel()**i for i, c in enumerate(coeffs))

x_train = np.linspace(-3, 3, 20)[:, None]
rng = np.random.RandomState(5)
true_mean = 0.5 * x_train.ravel()**2 - 1.0
y_train = true_mean + 0.3 * rng.randn(20)

# Subtract quadratic mean, fit GP residual
mean_train = polynomial_mean(x_train, [0, 0, 0.5])
y_centered = y_train - mean_train

lam = 0.05
K = rbf_kernel_matrix(x_train, x_train, ell=0.8) + lam * np.eye(20)
alpha = np.linalg.solve(K, y_centered)

x_test = np.linspace(-4, 4, 200)[:, None]
K_star = rbf_kernel_matrix(x_test, x_train, ell=0.8)
mean_test = polynomial_mean(x_test, [0, 0, 0.5])
y_pred = mean_test + K_star @ alpha

plt.figure(figsize=(10, 4))
plt.scatter(x_train, y_train, label='Training data', zorder=5, s=40)
plt.plot(x_test, y_pred, label='GP prediction (quadratic mean)', color='red')
plt.plot(x_test, mean_test, '--', label='Mean function only', color='orange', alpha=0.7)
plt.legend()
plt.title('GP with Non-Zero Polynomial Mean Function')
plt.savefig('gp_nonzero_mean.png', dpi=100)
print('Saved gp_nonzero_mean.png')
```

## Design Choices Reference

| Design Choice | Options | Effect on Prior | Recommendation |
| --- | --- | --- | --- |
| Mean function m(x) | Zero, linear, polynomial, neural net | Centers the prior; affects extrapolation | Use zero mean within training range; linear/polynomial for extrapolation |
| Covariance function k(x,x') | RBF, Matérn, polynomial, periodic, composite | Controls smoothness and correlation range | Matérn-5/2 as default; RBF for very smooth functions |
| Length-scale ℓ | Fixed, tuned by marginal MLE, cross-validated | Controls correlation decay rate | Learn via marginal likelihood maximization (type-II MLE) |
| Signal variance σ² | Fixed, learned from data | Overall function amplitude | Learn from data; initialize to var(y) |
| Noise variance σ²_n | Fixed, learned, heteroscedastic | Separates signal from observation noise | Learn from data; use heteroscedastic model for varying noise |

A GP is fully specified by m and k. The zero-mean RBF GP is a reasonable starting point for most regression tasks. For problems with known structure — trends, periodicity, additive decompositions — encode that structure in the mean and covariance functions rather than relying on the data alone. Hyperparameters are learned by maximizing the log marginal likelihood log p(y | X, θ), which automatically balances data fit and prior complexity.

