---
title: "Sinusoidal Positional Encoding — Vaswani et al. Design"
slug: "sinusoidal-positional-encoding"
description: "Derive Vaswani et al.'s sinusoidal PE formula, prove the linear-shift property, analyse the multi-frequency design, and compare sinusoidal encoding with learned, RoPE, ALiBi, and NoPE variants."
tags: ["deep-learning", "transformers", "attention"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSB2YW5pbGxhIFRyYW5zZm9ybWVyIGlzIHBlcm11dGF0aW9uIGVxdWl2YXJpYW50OiBzd2FwcGluZyB0d28gdG9rZW5zIGluIHRoZSBpbnB1dCBwcm9kdWNlcyB0aGUgc2FtZSBvdXRwdXQgd2l0aCB0aG9zZSB0d28gdG9rZW5zIHN3YXBwZWQuIFRoaXMgaXMgYmVjYXVzZSBkb3QtcHJvZHVjdCBhdHRlbnRpb24gdHJlYXRzIHBvc2l0aW9ucyBzeW1tZXRyaWNhbGx5IOKAlCB0aGVyZSBpcyBubyBub3Rpb24gb2YgXHUwMDI3cG9zaXRpb24gMyBjb21lcyBiZWZvcmUgcG9zaXRpb24gN1x1MDAyNy4gUG9zaXRpb25hbCBlbmNvZGluZyBpbmplY3RzIHBvc2l0aW9uIGluZm9ybWF0aW9uIGJ5IGFkZGluZyBhIHBvc2l0aW9uLWRlcGVuZGVudCB2ZWN0b3IgdG8gdGhlIHRva2VuIGVtYmVkZGluZyBiZWZvcmUgaXQgZW50ZXJzIHRoZSBUcmFuc2Zvcm1lciBzdGFjay4gVmFzd2FuaSBldCBhbC4gY2hvc2UgYSBkZXRlcm1pbmlzdGljIHNpbnVzb2lkYWwgZW5jb2Rpbmcgd2l0aCBzcGVjaWZpYyBtYXRoZW1hdGljYWwgcHJvcGVydGllcyB0aGF0IG1vdGl2YXRlZCB0aGUgZGVzaWduIG9mIGFsbCBzdWJzZXF1ZW50IHBvc2l0aW9uYWwgZW5jb2Rpbmcgc2NoZW1lcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgUGVybXV0YXRpb24gRXF1aXZhcmlhbmNlIFByb2JsZW0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvcm1hbGx5LCBsZXQgZiBiZSBhIFRyYW5zZm9ybWVyIGxheWVyLiBJdCBpcyBwZXJtdXRhdGlvbiBlcXVpdmFyaWFudCBpZiBmKFB4KSA9IFBmKHgpIGZvciBhbnkgcGVybXV0YXRpb24gbWF0cml4IFAuIFRoaXMgaG9sZHMgYmVjYXVzZSBhdHRlbnRpb24gd2VpZ2h0cyBB4bWi4rG8ID0gc29mdG1heChx4bWiwrdr4rG8L+KImmTigpYpIGRlcGVuZCBvbmx5IG9uIHRoZSBjb250ZW50IG9mIHBvc2l0aW9ucyBpIGFuZCBqLCBub3Qgb24gdGhlaXIgaW5kaWNlcy4gQ29uc2VxdWVudGx5LCB0aGUgVHJhbnNmb3JtZXIgY2Fubm90IGRpc3Rpbmd1aXNoIFx1MDAyN3RoZSBjYXQgYXRlIHRoZSBmaXNoXHUwMDI3IGZyb20gXHUwMDI3dGhlIGZpc2ggYXRlIHRoZSBjYXRcdTAwMjcgd2l0aG91dCBwb3NpdGlvbmFsIGluZm9ybWF0aW9uLiBQb3NpdGlvbmFsIGVuY29kaW5nIGJyZWFrcyB0aGlzIHN5bW1ldHJ5IGJ5IG1ha2luZyB0b2tlbiBlbWJlZGRpbmdzIHBvc2l0aW9uLWRlcGVuZGVudCBiZWZvcmUgdGhleSBhcmUgZmVkIHRvIHRoZSBmaXJzdCBsYXllci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaW51c29pZGFsIFBFIEZvcm11bGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZhc3dhbmkgZXQgYWwuIDIwMTcgZGVmaW5lZCB0aGUgcG9zaXRpb25hbCBlbmNvZGluZyBQRSDiiIgg4oSdXnttYXhfbGVuw5dkX21vZGVsfSBieSBwYWlycyBvZiBzaW5lIGFuZCBjb3NpbmUgZnVuY3Rpb25zIGF0IGdlb21ldHJpY2FsbHkgc3BhY2VkIGZyZXF1ZW5jaWVzLiBGb3IgcG9zaXRpb24gcG9zIOKIiCB7MCwuLi4sbWF4X2xlbuKIkjF9IGFuZCBkaW1lbnNpb24gaW5kZXggaSDiiIggezAsLi4uLGRfbW9kZWwvMuKIkjF9OiBQRShwb3MsIDJpKSA9IHNpbihwb3MgLyAxMDAwMF57MmkvZF9tb2RlbH0pIGFuZCBQRShwb3MsIDJpKzEpID0gY29zKHBvcyAvIDEwMDAwXnsyaS9kX21vZGVsfSkuIFRoZSBkaXZpc29yIDEwMDAwXnsyaS9kX21vZGVsfSBjcmVhdGVzIGEgZ2VvbWV0cmljIHByb2dyZXNzaW9uIG9mIHdhdmVsZW5ndGhzIGZyb20gMs+AIChhdCBpPTAsIGhpZ2hlc3QgZnJlcXVlbmN5KSB0byAxMDAwMMK3Ms+AIChhdCBpPWRfbW9kZWwvMuKIkjEsIGxvd2VzdCBmcmVxdWVuY3kpLiBUaGUgUEUgaXMgYWRkZWQgKG5vdCBjb25jYXRlbmF0ZWQpIHRvIHRoZSB0b2tlbiBlbWJlZGRpbmc6IHggPSBlbWJlZCh0b2tlbikgKyBQRVtwb3NdLiJ9LHsidHlwZSI6Im1hdGgiLCJjb250ZW50IjoiUEUocG9zLCAyaSkgPSBcXHNpblxcIVxcbGVmdChcXGZyYWN7cG9zfXsxMDAwMF57MmkvZF97XFx0ZXh0e21vZGVsfX19fVxccmlnaHQpLCBcXHFxdWFkIFBFKHBvcywgMmkrMSkgPSBcXGNvc1xcIVxcbGVmdChcXGZyYWN7cG9zfXsxMDAwMF57MmkvZF97XFx0ZXh0e21vZGVsfX19fVxccmlnaHQpIiwiZGlzcGxheSI6dHJ1ZX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc2ludXNvaWRhbF9wZShtYXhfbGVuLCBkX21vZGVsKTpcbiAgICAjIFJldHVybnMgUEUgbWF0cml4OiAobWF4X2xlbiwgZF9tb2RlbClcbiAgICBQRSA9IG5wLnplcm9zKChtYXhfbGVuLCBkX21vZGVsKSlcbiAgICBwb3MgPSBucC5hcmFuZ2UobWF4X2xlbilbOiwgbnAubmV3YXhpc10gICAgICAgICAgIyAobWF4X2xlbiwgMSlcbiAgICBpICAgPSBucC5hcmFuZ2UoMCwgZF9tb2RlbCwgMilbbnAubmV3YXhpcywgOl0gICAjICgxLCBkX21vZGVsLzIpXG4gICAgZGl2ID0gbnAucG93ZXIoMTAwMDAuMCwgaSAvIGRfbW9kZWwpXG4gICAgUEVbOiwgMDo6Ml0gPSBucC5zaW4ocG9zIC8gZGl2KSAgICAjIGV2ZW4gZGltczogc2luXG4gICAgUEVbOiwgMTo6Ml0gPSBucC5jb3MocG9zIC8gZGl2KSAgICAjIG9kZCAgZGltczogY29zXG4gICAgcmV0dXJuIFBFXG5cbnBlID0gc2ludXNvaWRhbF9wZSg1MCwgMTI4KVxucHJpbnQoXHUwMDI3UEUgc2hhcGU6XHUwMDI3LCBwZS5zaGFwZSlcbnByaW50KFx1MDAyN1BFIHZhbHVlcyBib3VuZGVkIGluIFstMSwgMV06XHUwMDI3LCBwZS5taW4oKS5yb3VuZCgzKSwgXHUwMDI3dG9cdTAwMjcsIHBlLm1heCgpLnJvdW5kKDMpKVxucHJpbnQoXHUwMDI3UEVbcG9zPTAsIDo0XTpcdTAwMjcsIHBlWzAsIDo0XS5yb3VuZCg0KSlcbnByaW50KFx1MDAyN1BFW3Bvcz0xLCA6NF06XHUwMDI3LCBwZVsxLCA6NF0ucm91bmQoNCkpXG5wcmludChcdTAwMjdQRVtwb3M9MTAsOjRdOlx1MDAyNywgcGVbMTAsIDo0XS5yb3VuZCg0KSlcblxuIyBUZXh0IGhlYXRtYXAgb2YgUEUgdmFsdWVzIGFjcm9zcyBwb3NpdGlvbnMgeCBzZWxlY3RlZCBkaW1lbnNpb25zXG5wcmludChcdTAwMjdcXG5IZWF0bWFwICgrIHBvcywgLiBuZWFyLXplcm8sIC0gbmVnKSByb3dzPXBvcywgY29scz1kaW06XHUwMDI3KVxuc2VsX2RpbXMgPSBbMCwgOCwgMTYsIDMyLCA2NCwgOTYsIDEyNl1cbnByaW50KFx1MDAyN3Bvc1x1MDAyNyArIFx1MDAyN1x1MDAyNy5qb2luKFx1MDAyNyBkezpcdTAwM2UzfVx1MDAyNy5mb3JtYXQoZCkgZm9yIGQgaW4gc2VsX2RpbXMpKVxuZm9yIHBvcyBpbiBbMCwgNSwgMTAsIDIwLCAzMCwgNDAsIDQ5XTpcbiAgICByb3cgPSBcdTAwMjcgIHs6XHUwMDNlMn06XHUwMDI3LmZvcm1hdChwb3MpXG4gICAgZm9yIGQgaW4gc2VsX2RpbXM6XG4gICAgICAgIHYgPSBwZVtwb3MsIGRdXG4gICAgICAgIHJvdyArPSBcdTAwMjcgICsrK1x1MDAyNyBpZiB2IFx1MDAzZSAwLjUgZWxzZSBcdTAwMjcgICsgIFx1MDAyNyBpZiB2IFx1MDAzZSAwLjEgZWxzZSBcdTAwMjcgIC4gIFx1MDAyNyBpZiBhYnModikgXHUwMDNjIDAuMSBlbHNlIFx1MDAyNyAgLSAgXHUwMDI3IGlmIHYgXHUwMDNlIC0wLjUgZWxzZSBcdTAwMjcgIC0tLVx1MDAyN1xuICAgIHByaW50KHJvdykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGb3VyIEtleSBQcm9wZXJ0aWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2ludXNvaWRhbCBQRSBkZXNpZ24gc2F0aXNmaWVzIGZvdXIgcHJvcGVydGllcyB0aGF0IGd1aWRlZCB0aGUgY2hvaWNlIG92ZXIgc2ltcGxlciBhbHRlcm5hdGl2ZXMgbGlrZSBpbnRlZ2VyIGVuY29kaW5nIG9yIGxlYXJuZWQgZW1iZWRkaW5ncy4gRWFjaCBwb3NpdGlvbiBnZXRzIGEgdW5pcXVlIHZlY3Rvci4gVGhlIGVuY29kaW5nIGdlbmVyYWxpc2VzIGRldGVybWluaXN0aWNhbGx5IHRvIHBvc2l0aW9ucyBiZXlvbmQgdGhlIHRyYWluaW5nIHNlcXVlbmNlIGxlbmd0aC4gUmVsYXRpdmUgZGlzdGFuY2VzIGFyZSByZWNvdmVyYWJsZSBmcm9tIHRoZSBlbmNvZGluZ3MgdmlhIGxpbmVhciBjb21iaW5hdGlvbiAocHJvdmVuIGJlbG93KS4gQW5kIHRoZSBlbmNvZGluZyB2YWx1ZXMgYXJlIGJvdW5kZWQgaW4gW+KIkjEsIDFdLCBwcmV2ZW50aW5nIHRoZW0gZnJvbSBkb21pbmF0aW5nIHRoZSB0b2tlbiBlbWJlZGRpbmcgc2lnbmFsIHJlZ2FyZGxlc3Mgb2Ygc2VxdWVuY2UgbGVuZ3RoLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjp0cnVlLCJpdGVtcyI6WyJVbmlxdWVuZXNzOiBldmVyeSBwb3NpdGlvbiBwb3MgaGFzIGEgdW5pcXVlIFBFIHZlY3RvciDigJQgcHJvdmVuIGJlY2F1c2UgdGhlIHNldCBvZiBmcmVxdWVuY2llcyBpcyBpbmNvbW1lbnN1cmF0ZSAobm8gdHdvIGZyZXF1ZW5jaWVzIGFyZSByYXRpb25hbCBtdWx0aXBsZXMgb2YgZWFjaCBvdGhlciBmb3IgdHlwaWNhbCBkX21vZGVsIGFuZCBtYXhfbGVuIHZhbHVlcykiLCJHZW5lcmFsaXNhdGlvbjogdGhlIGZvcm11bGEgaXMgZGVmaW5lZCBmb3IgYW55IHBvcyDiiaUgMDsgcG9zaXRpb25zIGJleW9uZCBtYXhfbGVuIGR1cmluZyB0cmFpbmluZyBnZXQgZW5jb2RpbmdzIHRoYXQgYXJlIHNtb290aCBjb250aW51YXRpb25zIG9mIHRoZSB0cmFpbmVkIHJhbmdlIiwiTGluZWFyLXNoaWZ0IHByb3BlcnR5OiBQRShwb3MraykgY2FuIGJlIGV4cHJlc3NlZCBhcyBhIGZpeGVkIGxpbmVhciAocm90YXRpb24pIGZ1bmN0aW9uIG9mIFBFKHBvcykgZm9yIGFueSBvZmZzZXQgayDigJQgdGhpcyBhbGxvd3MgdGhlIG1vZGVsIHRvIHJlYXNvbiBhYm91dCByZWxhdGl2ZSBwb3NpdGlvbnMgdmlhIGxlYXJuZWQgbGluZWFyIG9wZXJhdGlvbnMiLCJCb3VuZGVkIG1hZ25pdHVkZTogYWxsIFBFIHZhbHVlcyBsaWUgaW4gW+KIkjEsIDFdLCBzbyB0aGUgYWRkZWQgcG9zaXRpb25hbCBzaWduYWwgaGFzIHRoZSBzYW1lIHNjYWxlIHJlZ2FyZGxlc3Mgb2YgcG9zIOKAlCBubyBwb3NpdGlvbiByZWNlaXZlcyBhIGRpc3Byb3BvcnRpb25hdGVseSBsYXJnZSBlbmNvZGluZyJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiV2h5IEFkZGl0aW9uLCBOb3QgQ29uY2F0ZW5hdGlvbj8iLCJjb250ZW50IjoiQ29uY2F0ZW5hdGluZyB0aGUgUEUgdG8gdGhlIGVtYmVkZGluZyB3b3VsZCBkb3VibGUgdGhlIGlucHV0IGRpbWVuc2lvbiB0byAywrdkX21vZGVsLCBkb3VibGluZyB0aGUgY29zdCBvZiBldmVyeSBwcm9qZWN0aW9uIG1hdHJpeC4gQWRkaW5nIGluc3RlYWQga2VlcHMgZGltZW5zaW9uIGRfbW9kZWwgd2hpbGUgYWxsb3dpbmcgdGhlIG5ldHdvcmsgdG8gbGVhcm4gdG8gc2VwYXJhdGUgdGhlIHNlbWFudGljIGNvbnRlbnQgKHByaW1hcmlseSBlbmNvZGVkIGluIHRva2VuIGVtYmVkZGluZyBkaXJlY3Rpb25zKSBhbmQgcG9zaXRpb25hbCBpbmZvcm1hdGlvbiAoZW5jb2RlZCBpbiBQRSBkaXJlY3Rpb25zKSB1c2luZyB0aGUgcHJvamVjdGlvbiBtYXRyaWNlcy4gSW4gcHJhY3RpY2UgdGhlIG5ldHdvcmsgbGVhcm5zIHRvIHVzZSBkaWZmZXJlbnQgZGltZW5zaW9ucyBvZiBkX21vZGVsIGZvciBjb250ZW50IHZzIHBvc2l0aW9uLCBhY2hpZXZpbmcgdGhlIHNhbWUgZXhwcmVzc2l2ZW5lc3MgYXMgY29uY2F0ZW5hdGlvbiB3aXRob3V0IHRoZSBleHRyYSBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbmVhci1TaGlmdCBQcm9wZXJ0eSDigJQgUHJvb2YifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBkaW1lbnNpb24gcGFpciAoMmksIDJpKzEpIHdpdGggZnJlcXVlbmN5IGbhtaIgPSAxLzEwMDAwXnsyaS9kX21vZGVsfSwgdGhlIGVuY29kaW5ncyBhcmUgc2luKHBvc8K3ZuG1oikgYW5kIGNvcyhwb3PCt2bhtaIpLiBGb3IgYSBmaXhlZCBvZmZzZXQgazogc2luKChwb3MraynCt2bhtaIpID0gc2luKHBvc8K3ZuG1oiljb3Moa8K3ZuG1oikgKyBjb3MocG9zwrdm4bWiKXNpbihrwrdm4bWiKSBhbmQgY29zKChwb3MraynCt2bhtaIpID0gY29zKHBvc8K3ZuG1oiljb3Moa8K3ZuG1oikg4oiSIHNpbihwb3PCt2bhtaIpc2luKGvCt2bhtaIpLiBUaGlzIGlzIGEgMsOXMiByb3RhdGlvbiBtYXRyaXggYXBwbGllZCB0byBbc2luKHBvc8K3ZuG1oiksIGNvcyhwb3PCt2bhtaIpXeG1gCB3aXRoIHJvdGF0aW9uIGFuZ2xlIGvCt2bhtaIuIFN0YWNraW5nIG92ZXIgYWxsIGRfbW9kZWwvMiBmcmVxdWVuY3kgcGFpcnMsIFBFKHBvcytrKSA9IE1fayDCtyBQRShwb3MpIHdoZXJlIE1fayBpcyBhIGJsb2NrLWRpYWdvbmFsIHJvdGF0aW9uIG1hdHJpeCB0aGF0IGRlcGVuZHMgb25seSBvbiBrLCBub3Qgb24gcG9zLiBUaGlzIG1lYW5zIFBFKHBvcytrKSBpcyBhbiBleGFjdCBsaW5lYXIgZnVuY3Rpb24gb2YgUEUocG9zKSBmb3IgYW55IGZpeGVkIG9mZnNldCBrLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHNpbnVzb2lkYWxfcGUobWF4X2xlbiwgZF9tb2RlbCk6XG4gICAgUEUgPSBucC56ZXJvcygobWF4X2xlbiwgZF9tb2RlbCkpXG4gICAgcG9zID0gbnAuYXJhbmdlKG1heF9sZW4pWzosIG5wLm5ld2F4aXNdXG4gICAgaSAgID0gbnAuYXJhbmdlKDAsIGRfbW9kZWwsIDIpW25wLm5ld2F4aXMsIDpdXG4gICAgZGl2ID0gbnAucG93ZXIoMTAwMDAuMCwgaSAvIGRfbW9kZWwpXG4gICAgUEVbOiwgMDo6Ml0gPSBucC5zaW4ocG9zIC8gZGl2KVxuICAgIFBFWzosIDE6OjJdID0gbnAuY29zKHBvcyAvIGRpdilcbiAgICByZXR1cm4gUEVcblxuZGVmIGxpbmVhcl9zaGlmdF9tYXRyaXgoaywgZF9tb2RlbCk6XG4gICAgIyBCbG9jay1kaWFnb25hbCByb3RhdGlvbiBtYXRyaXggTV9rIHN1Y2ggdGhhdCBQRShwb3MraykgPSBNX2sgQCBQRShwb3MpXG4gICAgTSA9IG5wLnplcm9zKChkX21vZGVsLCBkX21vZGVsKSlcbiAgICBmb3IgaWR4IGluIHJhbmdlKDAsIGRfbW9kZWwsIDIpOlxuICAgICAgICBmcmVxID0gMTAwMDAgKiogKGlkeCAvIGRfbW9kZWwpXG4gICAgICAgIGMsIHMgPSBucC5jb3MoayAvIGZyZXEpLCBucC5zaW4oayAvIGZyZXEpXG4gICAgICAgIE1baWR4LCAgIGlkeF0gICA9ICBjOyAgTVtpZHgsICAgaWR4KzFdID0gc1xuICAgICAgICBNW2lkeCsxLCBpZHhdICAgPSAtczsgIE1baWR4KzEsIGlkeCsxXSA9IGNcbiAgICByZXR1cm4gTVxuXG5wZSA9IHNpbnVzb2lkYWxfcGUoMjAwLCA2NClcbnByaW50KFx1MDAyN1ZlcmlmeWluZzogUEUocG9zK2spID0gTV9rIEAgUEUocG9zKVx1MDAyNylcbmZvciBwb3MsIGsgaW4gWyg1LCAzKSwgKDIwLCA3KSwgKDUwLCAxMyksICgxMDAsIDI1KV06XG4gICAgTV9rICAgICAgID0gbGluZWFyX3NoaWZ0X21hdHJpeChrLCA2NClcbiAgICBwcmVkaWN0ZWQgPSBNX2sgQCBwZVtwb3NdXG4gICAgYWN0dWFsICAgID0gcGVbcG9zICsga11cbiAgICBlcnIgPSBucC5hYnMocHJlZGljdGVkIC0gYWN0dWFsKS5tYXgoKVxuICAgIHN0YXR1cyA9IFx1MDAyN1BBU1NcdTAwMjcgaWYgZXJyIFx1MDAzYyAxZS0xMCBlbHNlIFx1MDAyN0ZBSUxcdTAwMjdcbiAgICBwcmludChcdTAwMjcgIFBFKHs6XHUwMDNlM30rezpcdTAwM2UyfSkgPSBNX3t9IEAgUEUoezpcdTAwM2UzfSk6IG1heF9lcnI9ezouMmV9ICB7fVx1MDAyNy5mb3JtYXQoXG4gICAgICAgIHBvcywgaywgaywgcG9zLCBlcnIsIHN0YXR1cykpXG5wcmludChcdTAwMjdQRShwb3MraykgaXMgYW4gZXhhY3QgbGluZWFyIGZ1bmN0aW9uIG9mIFBFKHBvcykgZm9yIGFueSBrLlx1MDAyNylcbnByaW50KFx1MDAyN1RoZSBtb2RlbCBjYW4gbGVhcm4gdG8gZGVjb2RlIHJlbGF0aXZlIG9mZnNldHMgdmlhIGxpbmVhciBhdHRlbnRpb24gb3BzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGcmVxdWVuY3kgQW5hbHlzaXMg4oCUIExvdyB2cyBIaWdoIERpbWVuc2lvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsb3dlc3QtaW5kZXhlZCBkaW1lbnNpb25zIChpPTAsMSkgdXNlIHRoZSBoaWdoZXN0IGZyZXF1ZW5jeSBm4bWiPTEgKHdhdmVsZW5ndGggMs+AIOKJiCA2LjMgdG9rZW5zKTogdGhlc2UgZGltZW5zaW9ucyBvc2NpbGxhdGUgcmFwaWRseSwgY2hhbmdpbmcgc3Vic3RhbnRpYWxseSBiZXR3ZWVuIGFkamFjZW50IHBvc2l0aW9ucy4gVGhlIGhpZ2hlc3QtaW5kZXhlZCBkaW1lbnNpb25zIChp4omIZF9tb2RlbC8yKSB1c2UgdGhlIGxvd2VzdCBmcmVxdWVuY3kgZuG1oiDiiYggMS8xMDAwMCAod2F2ZWxlbmd0aCDiiYggNjIsODAwIHRva2Vucyk6IHRoZXNlIGRpbWVuc2lvbnMgY2hhbmdlIHZlcnkgc2xvd2x5LCBlbmNvZGluZyBjb2Fyc2UgcG9zaXRpb24gYXQgdGhlIHNlcXVlbmNlIGxldmVsLiBUaGUgY29tYmluZWQgbXVsdGktc2NhbGUgcmVwcmVzZW50YXRpb24gcmVzZW1ibGVzIGEgYmluYXJ5IGNvdW50ZXIgZ2VuZXJhbGlzZWQgdG8gc2ludXNvaWRhbCBiYXNlczogbG93IGRpbWVuc2lvbnMgZW5jb2RlIGZpbmUtZ3JhaW5lZCBwb3NpdGlvbiwgaGlnaCBkaW1lbnNpb25zIGVuY29kZSBjb2Fyc2UgcG9zaXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR2VuZXJhbGlzYXRpb24gdG8gTG9uZ2VyIFNlcXVlbmNlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVjYXVzZSB0aGUgUEUgZm9ybXVsYSBpcyBkZXRlcm1pbmlzdGljIGFuZCBub3QgbGVhcm5lZCwgaXQgcHJvZHVjZXMgd2VsbC1kZWZpbmVkIHZhbHVlcyBmb3IgYW55IHBvc2l0aW9uIHBvcyByZWdhcmRsZXNzIG9mIHRoZSBtYXhpbXVtIGxlbmd0aCBzZWVuIGR1cmluZyB0cmFpbmluZy4gVGhlIGVuY29kaW5nIGF0IHBvc2l0aW9ucyBiZXlvbmQgbWF4X2xlbl90cmFpbiBhcmUgc21vb3RoIGNvbnRpbnVhdGlvbnMgb2YgdGhlIHNhbWUgc2ludXNvaWRhbCBjdXJ2ZXMuIEluIHByYWN0aWNlLCBtb2RlbHMgdHJhaW5lZCB3aXRoIHNpbnVzb2lkYWwgUEUgY2FuIG9mdGVuIHByb2Nlc3Mgc2VxdWVuY2VzIHVwIHRvIDLDlyB0aGUgdHJhaW5pbmcgbGVuZ3RoIHdpdGhvdXQgc2lnbmlmaWNhbnQgZGVncmFkYXRpb24sIHRob3VnaCBhY2N1cmFjeSBkb2VzIGRlY2xpbmUgYmVjYXVzZSB0aGUgYXR0ZW50aW9uIGxheWVycyBoYXZlIG5vdCBzZWVuIHN1Y2ggcG9zaXRpb25zIGR1cmluZyB0cmFpbmluZy4gTGVhcm5lZCBwb3NpdGlvbmFsIGVtYmVkZGluZ3MsIGJ5IGNvbnRyYXN0LCBhcmUgdW5kZWZpbmVkIGJleW9uZCB0aGUgdHJhaW5pbmcgdm9jYWJ1bGFyeSBhbmQgcmVxdWlyZSBpbnRlcnBvbGF0aW9uIG9yIGV4dHJhcG9sYXRpb24gaGV1cmlzdGljcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBzaW51c29pZGFsX3BlKG1heF9sZW4sIGRfbW9kZWwpOlxuICAgIFBFID0gbnAuemVyb3MoKG1heF9sZW4sIGRfbW9kZWwpKVxuICAgIHBvcyA9IG5wLmFyYW5nZShtYXhfbGVuKVs6LCBucC5uZXdheGlzXVxuICAgIGkgICA9IG5wLmFyYW5nZSgwLCBkX21vZGVsLCAyKVtucC5uZXdheGlzLCA6XVxuICAgIFBFWzosIDA6OjJdID0gbnAuc2luKHBvcyAvIG5wLnBvd2VyKDEwMDAwLjAsIGkgLyBkX21vZGVsKSlcbiAgICBQRVs6LCAxOjoyXSA9IG5wLmNvcyhwb3MgLyBucC5wb3dlcigxMDAwMC4wLCBpIC8gZF9tb2RlbCkpXG4gICAgcmV0dXJuIFBFXG5cbnRyYWluX2xlbiwgZF9tb2RlbCA9IDEyOCwgNjRcbnBlX3RyYWluID0gc2ludXNvaWRhbF9wZSh0cmFpbl9sZW4sIGRfbW9kZWwpXG5wZV9sb25nICA9IHNpbnVzb2lkYWxfcGUodHJhaW5fbGVuICogMiwgZF9tb2RlbCkgICAgIyAyeCBsb25nZXIgYXQgdGVzdCB0aW1lXG5cbmFzc2VydCBucC5hbGxjbG9zZShwZV90cmFpbiwgcGVfbG9uZ1s6dHJhaW5fbGVuXSksIFx1MDAyN1BFIHdpdGhpbiB0cmFpbiByYW5nZSBtdXN0IG1hdGNoIVx1MDAyN1xucHJpbnQoXHUwMDI3UEVbMDp7OmR9XSBpZGVudGljYWwgaW4gdHJhaW4gYW5kIGxvbmcgY29udGV4dDogUEFTU1x1MDAyNy5mb3JtYXQodHJhaW5fbGVuKSlcblxuZGVsdGFfdHJhaW4gPSBucC5kaWZmKHBlX3RyYWluLCBheGlzPTApXG5kZWx0YV9leHRyYSA9IG5wLmRpZmYocGVfbG9uZ1t0cmFpbl9sZW46XSwgYXhpcz0wKVxucHJpbnQoXHUwMDI3TWVhbiB8ZGVsdGF8IGluIHRyYWluIHJlZ2lvbjogezouNGZ9XHUwMDI3LmZvcm1hdChucC5hYnMoZGVsdGFfdHJhaW4pLm1lYW4oKSkpXG5wcmludChcdTAwMjdNZWFuIHxkZWx0YXwgaW4gZXh0cmEgcmVnaW9uOiB7Oi40Zn1cdTAwMjcuZm9ybWF0KG5wLmFicyhkZWx0YV9leHRyYSkubWVhbigpKSlcbnByaW50KFx1MDAyN1NpbWlsYXIgLVx1MDAzZSBzbW9vdGggY29udGludWF0aW9uIGJleW9uZCB0cmFpbiBsZW5ndGguXHUwMDI3KVxuXG5wZV90ZXN0ID0gcGVfbG9uZ1xubm9ybXMgPSBucC5saW5hbGcubm9ybShwZV90ZXN0LCBheGlzPTEsIGtlZXBkaW1zPVRydWUpICsgMWUtOVxuY29zX3NpbSA9IChwZV90ZXN0IC8gbm9ybXMpIEAgKHBlX3Rlc3QgLyBub3JtcykuVFxubnAuZmlsbF9kaWFnb25hbChjb3Nfc2ltLCAwKVxucHJpbnQoXHUwMDI3TWF4IG9mZi1kaWFnb25hbCBjb3Mgc2ltaWxhcml0eSAoYWxsIHBvc2l0aW9ucyk6IHs6LjRmfVx1MDAyNy5mb3JtYXQoY29zX3NpbS5tYXgoKSkpXG5wcmludChcdTAwMjdMb3cgLVx1MDAzZSB1bmlxdWUgZW5jb2RpbmcgZXZlbiBiZXlvbmQgdHJhaW5pbmcgbGVuZ3RoLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaXRoIHZzIFdpdGhvdXQgUG9zaXRpb25hbCBFbmNvZGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aG91dCBwb3NpdGlvbmFsIGVuY29kaW5nLCB0aGUgVHJhbnNmb3JtZXIgdHJlYXRzIGl0cyBpbnB1dCBhcyBhIHNldCByYXRoZXIgdGhhbiBhIHNlcXVlbmNlLiBGb3IgYW55IHRhc2sgd2hlcmUgdGhlIG91dHB1dCBkZXBlbmRzIG9uIHRva2VuIG9yZGVyICh0cmFuc2xhdGlvbiwgbGFuZ3VhZ2UgbW9kZWxsaW5nLCBzZXF1ZW5jZSBjbGFzc2lmaWNhdGlvbiBiYXNlZCBvbiB3b3JkIG9yZGVyKSwgcmVtb3ZpbmcgUEUgY2F1c2VzIHNpZ25pZmljYW50IGRlZ3JhZGF0aW9uLiBUaGUgZGVncmFkYXRpb24gaXMgdG90YWwgZm9yIHRhc2tzIHdoZXJlIHR3byBkaWZmZXJlbnQgb3JkZXJpbmdzIG1hcCB0byBjb21wbGV0ZWx5IGRpZmZlcmVudCBzZW1hbnRpY3MgKGUuZy4sIFx1MDAyN21hbiBiaXRlcyBkb2dcdTAwMjcgdnMgXHUwMDI3ZG9nIGJpdGVzIG1hblx1MDAyNykuIEZvciBiYWctb2Ytd29yZHMgdGFza3MgKHNlbnRpbWVudCBjbGFzc2lmaWNhdGlvbiBvZiBzaG9ydCB0ZXh0KSB0aGUgZWZmZWN0IGlzIG1pbGQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc29mdG1heChTKTpcbiAgICBTID0gUyAtIFMubWF4KGF4aXM9LTEsIGtlZXBkaW1zPVRydWUpXG4gICAgZSA9IG5wLmV4cChTKTsgcmV0dXJuIGUgLyBlLnN1bShheGlzPS0xLCBrZWVwZGltcz1UcnVlKVxuXG5kZWYgc2RwX2F0dG4oUSwgSywgVik6XG4gICAgQSA9IHNvZnRtYXgoUSBAIEsuVCAvIG5wLnNxcnQoUS5zaGFwZVstMV0pKVxuICAgIHJldHVybiBBIEAgVlxuXG5kZWYgc2ludXNvaWRhbF9wZShuLCBkKTpcbiAgICBQRSA9IG5wLnplcm9zKChuLCBkKSlcbiAgICBwb3MgPSBucC5hcmFuZ2UobilbOiwgbnAubmV3YXhpc11cbiAgICBpICAgPSBucC5hcmFuZ2UoMCwgZCwgMilbbnAubmV3YXhpcywgOl1cbiAgICBQRVs6LCAwOjoyXSA9IG5wLnNpbihwb3MgLyBucC5wb3dlcigxMDAwMC4wLCBpIC8gZCkpXG4gICAgUEVbOiwgMTo6Ml0gPSBucC5jb3MocG9zIC8gbnAucG93ZXIoMTAwMDAuMCwgaSAvIGQpKVxuICAgIHJldHVybiBQRVxuXG5ucC5yYW5kb20uc2VlZCgwKVxubiwgZCA9IDgsIDMyXG5XID0gbnAucmFuZG9tLnJhbmRuKGQsIGQpICogMC4xXG5YID0gbnAucmFuZG9tLnJhbmRuKG4sIGQpXG5YX3BlID0gWCArIHNpbnVzb2lkYWxfcGUobiwgZClcblxuIyBUZXN0OiBpcyB0aGUgb3V0cHV0IHBlcm11dGF0aW9uIGVxdWl2YXJpYW50IHdpdGhvdXQgUEU/XG5wZXJtID0gbnAucmFuZG9tLnBlcm11dGF0aW9uKG4pXG5vdXRfbm9fcGUgICAgICAgID0gc2RwX2F0dG4oWCBAIFcsIFggQCBXLCBYKVxub3V0X3Blcm1fbm9fcGUgICA9IHNkcF9hdHRuKChYW3Blcm1dIEAgVyksIChYW3Blcm1dIEAgVyksIFhbcGVybV0pXG5ub19wZV9lcXVpdiA9IG5wLmFsbGNsb3NlKG91dF9ub19wZVtwZXJtXSwgb3V0X3Blcm1fbm9fcGUsIGF0b2w9MWUtMTApXG5wcmludChcdTAwMjdObyBQRSAg4oCUIHBlcm11dGF0aW9uIGVxdWl2YXJpYW50IChvdXRwdXQgcmVvcmRlcnMgd2l0aCBpbnB1dCk6XHUwMDI3LCBub19wZV9lcXVpdilcblxub3V0X3BlICAgICAgICAgICA9IHNkcF9hdHRuKFhfcGUgQCBXLCBYX3BlIEAgVywgWF9wZSlcblhfcGVfcGVybSA9IFhbcGVybV0gKyBzaW51c29pZGFsX3BlKG4sIGQpXG5vdXRfcGVybV9wZSAgICAgID0gc2RwX2F0dG4oWF9wZV9wZXJtIEAgVywgWF9wZV9wZXJtIEAgVywgWF9wZV9wZXJtKVxucGVfZXF1aXYgPSBucC5hbGxjbG9zZShvdXRfcGVbcGVybV0sIG91dF9wZXJtX3BlLCBhdG9sPTFlLTUpXG5wcmludChcdTAwMjdXaXRoIFBFIOKAlCBwZXJtdXRhdGlvbiBlcXVpdmFyaWFudDpcdTAwMjcsIHBlX2VxdWl2KVxucHJpbnQoXHUwMDI3UEUgYnJlYWtzIHBlcm11dGF0aW9uIHN5bW1ldHJ5OiBtb2RlbCBkaXN0aW5ndWlzaGVzIHRva2VuIG9yZGVyLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIG9mIFBvc2l0aW9uYWwgRW5jb2RpbmdzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW51c29pZGFsIFBFIHdhcyB0aGUgc3RhbmRhcmQgdW50aWwgbGVhcm5lZCBwb3NpdGlvbmFsIGVtYmVkZGluZ3MgKEJFUlQsIEdQVC0yKSBzaG93ZWQgdGhhdCBkYXRhLWRyaXZlbiBwb3NpdGlvbnMgaW1wcm92ZSBkb3duc3RyZWFtIHRhc2sgcGVyZm9ybWFuY2UgYXQgdGhlIGNvc3Qgb2YgZXh0cmFwb2xhdGlvbiBhYmlsaXR5LiBSb1BFIGFuZCBBTGlCaSBsYXRlciByZXN0b3JlZCBsZW5ndGggZ2VuZXJhbGlzYXRpb24gd2l0aCBkaWZmZXJlbnQgbWVjaGFuaXNtczogUm9QRSByb3RhdGVzIFEgYW5kIEsgZGlyZWN0bHkgaW4gdGhlIGNvbXBsZXggcGxhbmUgKGludHJvZHVjaW5nIHJlbGF0aXZlIHBvc2l0aW9uIGludG8gdGhlIGF0dGVudGlvbiBzY29yZSksIHdoaWxlIEFMaUJpIHN1YnRyYWN0cyBhIGxpbmVhciBwb3NpdGlvbiBiaWFzIGZyb20gYXR0ZW50aW9uIHNjb3JlcyB3aXRob3V0IG1vZGlmeWluZyBRIG9yIEsuIEN1cnJlbnQgYmVzdCBwcmFjdGljZSBmb3IgbW9kZWxzIHRoYXQgbmVlZCB0byBleHRlbmQgdG8gbG9uZyBjb250ZXh0cyBpcyBSb1BFIHdpdGggZnJlcXVlbmN5IGludGVycG9sYXRpb24gKFlhUk4sIExvbmdSb1BFKS4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRW5jb2RpbmciLCJFeHRyYXBvbGF0ZXMgQmV5b25kIFRyYWluIExlbiIsIlJlbGF0aXZlIFBvc2l0aW9uIEluZm8iLCJMZWFybmFibGUgUGFyYW1zIiwiVXNlZCBJbiJdLCJyb3dzIjpbWyJTaW51c29pZGFsIChWYXN3YW5pIDIwMTcpIiwiWWVzIOKAlCBmb3JtdWxhIGV4dHJhcG9sYXRlcyBzbW9vdGhseSIsIkltcGxpY2l0IHZpYSBsaW5lYXItc2hpZnQgcHJvcGVydHkiLCJOb25lIiwiT3JpZ2luYWwgVHJhbnNmb3JtZXIsIHNvbWUgZW5jb2Rlci1kZWNvZGVyIG1vZGVscyJdLFsiTGVhcm5lZCBhYnNvbHV0ZSIsIk5vIOKAlCB1bmRlZmluZWQgYmV5b25kIHZvY2FiIHNpemUiLCJOb25lIGV4cGxpY2l0IiwibWF4X2xlbiDDlyBkX21vZGVsIiwiQkVSVCwgR1BULTIsIFZpVCJdLFsiUm9QRSAoU3UgZXQgYWwuIDIwMjEpIiwiWWVzIHdpdGggZnJlcXVlbmN5IHNjYWxpbmciLCJZZXMg4oCUIGV4cGxpY2l0IHJvdGF0aW9uIGJ5IHJlbGF0aXZlIGFuZ2xlIiwiTm9uZSIsIkxMYU1BLCBNaXN0cmFsLCBGYWxjb24sIEdlbW1hLCBQYUxNIDIiXSxbIkFMaUJpIChQcmVzcyBldCBhbC4gMjAyMikiLCJZZXMg4oCUIGxpbmVhciBiaWFzIGV4dHJhcG9sYXRlcyIsIlllcyDigJQgbGluZWFyIGRpc3RhbmNlIHBlbmFsdHkgcGVyIGhlYWQiLCJoIGxlYXJuYWJsZSBzbG9wZXMgKG9yIGZpeGVkKSIsIkJMT09NLCBNUFQsIHNvbWUgT1BUIHZhcmlhbnRzIl0sWyJOb1BFIChubyBQRSkiLCJZZXMgKG5vIHBvc2l0aW9uIGF0IGFsbCkiLCJOb25lIOKAlCBiYWctb2Ytd29yZHMiLCJOb25lIiwiU29tZSBlbmNvZGVyLW9ubHkgbW9kZWxzOyByZWxhdGl2ZSBQRSBpbiBUNSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgbmV3IGFyY2hpdGVjdHVyZXMgaW50ZW5kZWQgdG8gaGFuZGxlIHZhcmlhYmxlIG9yIGxvbmcgY29udGV4dCwgUm9QRSB3aXRoIHJvcGVfdGhldGEgdHVuaW5nIChpbmNyZWFzaW5nIDEwMDAwIHRvIDUwMCwwMDAgZm9yIGNvbnRleHQgZXh0ZW5zaW9uKSBpcyB0aGUgY3VycmVudCBkZWZhdWx0LiBBTGlCaSBvZmZlcnMgc2ltcGxlciBpbXBsZW1lbnRhdGlvbiBhbmQgc3Ryb25nIGxlbmd0aCBnZW5lcmFsaXNhdGlvbiBidXQgbGFja3MgdGhlIHJlbGF0aXZlLXBvc2l0aW9uIGV4cHJlc3NpdmVuZXNzIG9mIFJvUEUuIFNpbnVzb2lkYWwgUEUgcmVtYWlucyB2YWx1YWJsZSBmb3IgdW5kZXJzdGFuZGluZyDigJQgaXRzIGxpbmVhci1zaGlmdCBwcm9wZXJ0eSBpcyB0aGUgY29uY2VwdHVhbCBhbmNlc3RvciBvZiBSb1BFXHUwMDI3cyByb3RhdGlvbiBtZWNoYW5pc20uIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Sinusoidal Positional Encoding — Vaswani et al. Design

A vanilla Transformer is permutation equivariant: swapping two tokens in the input produces the same output with those two tokens swapped. This is because dot-product attention treats positions symmetrically — there is no notion of 'position 3 comes before position 7'. Positional encoding injects position information by adding a position-dependent vector to the token embedding before it enters the Transformer stack. Vaswani et al. chose a deterministic sinusoidal encoding with specific mathematical properties that motivated the design of all subsequent positional encoding schemes.

## The Permutation Equivariance Problem

Formally, let f be a Transformer layer. It is permutation equivariant if f(Px) = Pf(x) for any permutation matrix P. This holds because attention weights Aᵢⱼ = softmax(qᵢ·kⱼ/√dₖ) depend only on the content of positions i and j, not on their indices. Consequently, the Transformer cannot distinguish 'the cat ate the fish' from 'the fish ate the cat' without positional information. Positional encoding breaks this symmetry by making token embeddings position-dependent before they are fed to the first layer.

## Sinusoidal PE Formula

Vaswani et al. 2017 defined the positional encoding PE ∈ ℝ^{max_len×d_model} by pairs of sine and cosine functions at geometrically spaced frequencies. For position pos ∈ {0,...,max_len−1} and dimension index i ∈ {0,...,d_model/2−1}: PE(pos, 2i) = sin(pos / 10000^{2i/d_model}) and PE(pos, 2i+1) = cos(pos / 10000^{2i/d_model}). The divisor 10000^{2i/d_model} creates a geometric progression of wavelengths from 2π (at i=0, highest frequency) to 10000·2π (at i=d_model/2−1, lowest frequency). The PE is added (not concatenated) to the token embedding: x = embed(token) + PE[pos].

$$PE(pos, 2i) = \sin\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right), \qquad PE(pos, 2i+1) = \cos\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$

```python
import numpy as np

def sinusoidal_pe(max_len, d_model):
    # Returns PE matrix: (max_len, d_model)
    PE = np.zeros((max_len, d_model))
    pos = np.arange(max_len)[:, np.newaxis]          # (max_len, 1)
    i   = np.arange(0, d_model, 2)[np.newaxis, :]   # (1, d_model/2)
    div = np.power(10000.0, i / d_model)
    PE[:, 0::2] = np.sin(pos / div)    # even dims: sin
    PE[:, 1::2] = np.cos(pos / div)    # odd  dims: cos
    return PE

pe = sinusoidal_pe(50, 128)
print('PE shape:', pe.shape)
print('PE values bounded in [-1, 1]:', pe.min().round(3), 'to', pe.max().round(3))
print('PE[pos=0, :4]:', pe[0, :4].round(4))
print('PE[pos=1, :4]:', pe[1, :4].round(4))
print('PE[pos=10,:4]:', pe[10, :4].round(4))

# Text heatmap of PE values across positions x selected dimensions
print('\nHeatmap (+ pos, . near-zero, - neg) rows=pos, cols=dim:')
sel_dims = [0, 8, 16, 32, 64, 96, 126]
print('pos' + ''.join(' d{:>3}'.format(d) for d in sel_dims))
for pos in [0, 5, 10, 20, 30, 40, 49]:
    row = '  {:>2}:'.format(pos)
    for d in sel_dims:
        v = pe[pos, d]
        row += '  +++' if v > 0.5 else '  +  ' if v > 0.1 else '  .  ' if abs(v) < 0.1 else '  -  ' if v > -0.5 else '  ---'
    print(row)
```

## Four Key Properties

The sinusoidal PE design satisfies four properties that guided the choice over simpler alternatives like integer encoding or learned embeddings. Each position gets a unique vector. The encoding generalises deterministically to positions beyond the training sequence length. Relative distances are recoverable from the encodings via linear combination (proven below). And the encoding values are bounded in [−1, 1], preventing them from dominating the token embedding signal regardless of sequence length.

1. Uniqueness: every position pos has a unique PE vector — proven because the set of frequencies is incommensurate (no two frequencies are rational multiples of each other for typical d_model and max_len values)
2. Generalisation: the formula is defined for any pos ≥ 0; positions beyond max_len during training get encodings that are smooth continuations of the trained range
3. Linear-shift property: PE(pos+k) can be expressed as a fixed linear (rotation) function of PE(pos) for any offset k — this allows the model to reason about relative positions via learned linear operations
4. Bounded magnitude: all PE values lie in [−1, 1], so the added positional signal has the same scale regardless of pos — no position receives a disproportionately large encoding

> **Why Addition, Not Concatenation?**: Concatenating the PE to the embedding would double the input dimension to 2·d_model, doubling the cost of every projection matrix. Adding instead keeps dimension d_model while allowing the network to learn to separate the semantic content (primarily encoded in token embedding directions) and positional information (encoded in PE directions) using the projection matrices. In practice the network learns to use different dimensions of d_model for content vs position, achieving the same expressiveness as concatenation without the extra parameters.

## Linear-Shift Property — Proof

For dimension pair (2i, 2i+1) with frequency fᵢ = 1/10000^{2i/d_model}, the encodings are sin(pos·fᵢ) and cos(pos·fᵢ). For a fixed offset k: sin((pos+k)·fᵢ) = sin(pos·fᵢ)cos(k·fᵢ) + cos(pos·fᵢ)sin(k·fᵢ) and cos((pos+k)·fᵢ) = cos(pos·fᵢ)cos(k·fᵢ) − sin(pos·fᵢ)sin(k·fᵢ). This is a 2×2 rotation matrix applied to [sin(pos·fᵢ), cos(pos·fᵢ)]ᵀ with rotation angle k·fᵢ. Stacking over all d_model/2 frequency pairs, PE(pos+k) = M_k · PE(pos) where M_k is a block-diagonal rotation matrix that depends only on k, not on pos. This means PE(pos+k) is an exact linear function of PE(pos) for any fixed offset k.

```python
import numpy as np

def sinusoidal_pe(max_len, d_model):
    PE = np.zeros((max_len, d_model))
    pos = np.arange(max_len)[:, np.newaxis]
    i   = np.arange(0, d_model, 2)[np.newaxis, :]
    div = np.power(10000.0, i / d_model)
    PE[:, 0::2] = np.sin(pos / div)
    PE[:, 1::2] = np.cos(pos / div)
    return PE

def linear_shift_matrix(k, d_model):
    # Block-diagonal rotation matrix M_k such that PE(pos+k) = M_k @ PE(pos)
    M = np.zeros((d_model, d_model))
    for idx in range(0, d_model, 2):
        freq = 10000 ** (idx / d_model)
        c, s = np.cos(k / freq), np.sin(k / freq)
        M[idx,   idx]   =  c;  M[idx,   idx+1] = s
        M[idx+1, idx]   = -s;  M[idx+1, idx+1] = c
    return M

pe = sinusoidal_pe(200, 64)
print('Verifying: PE(pos+k) = M_k @ PE(pos)')
for pos, k in [(5, 3), (20, 7), (50, 13), (100, 25)]:
    M_k       = linear_shift_matrix(k, 64)
    predicted = M_k @ pe[pos]
    actual    = pe[pos + k]
    err = np.abs(predicted - actual).max()
    status = 'PASS' if err < 1e-10 else 'FAIL'
    print('  PE({:>3}+{:>2}) = M_{} @ PE({:>3}): max_err={:.2e}  {}'.format(
        pos, k, k, pos, err, status))
print('PE(pos+k) is an exact linear function of PE(pos) for any k.')
print('The model can learn to decode relative offsets via linear attention ops.')
```

## Frequency Analysis — Low vs High Dimensions

The lowest-indexed dimensions (i=0,1) use the highest frequency fᵢ=1 (wavelength 2π ≈ 6.3 tokens): these dimensions oscillate rapidly, changing substantially between adjacent positions. The highest-indexed dimensions (i≈d_model/2) use the lowest frequency fᵢ ≈ 1/10000 (wavelength ≈ 62,800 tokens): these dimensions change very slowly, encoding coarse position at the sequence level. The combined multi-scale representation resembles a binary counter generalised to sinusoidal bases: low dimensions encode fine-grained position, high dimensions encode coarse position.

## Generalisation to Longer Sequences

Because the PE formula is deterministic and not learned, it produces well-defined values for any position pos regardless of the maximum length seen during training. The encoding at positions beyond max_len_train are smooth continuations of the same sinusoidal curves. In practice, models trained with sinusoidal PE can often process sequences up to 2× the training length without significant degradation, though accuracy does decline because the attention layers have not seen such positions during training. Learned positional embeddings, by contrast, are undefined beyond the training vocabulary and require interpolation or extrapolation heuristics.

```python
import numpy as np

def sinusoidal_pe(max_len, d_model):
    PE = np.zeros((max_len, d_model))
    pos = np.arange(max_len)[:, np.newaxis]
    i   = np.arange(0, d_model, 2)[np.newaxis, :]
    PE[:, 0::2] = np.sin(pos / np.power(10000.0, i / d_model))
    PE[:, 1::2] = np.cos(pos / np.power(10000.0, i / d_model))
    return PE

train_len, d_model = 128, 64
pe_train = sinusoidal_pe(train_len, d_model)
pe_long  = sinusoidal_pe(train_len * 2, d_model)    # 2x longer at test time

assert np.allclose(pe_train, pe_long[:train_len]), 'PE within train range must match!'
print('PE[0:{:d}] identical in train and long context: PASS'.format(train_len))

delta_train = np.diff(pe_train, axis=0)
delta_extra = np.diff(pe_long[train_len:], axis=0)
print('Mean |delta| in train region: {:.4f}'.format(np.abs(delta_train).mean()))
print('Mean |delta| in extra region: {:.4f}'.format(np.abs(delta_extra).mean()))
print('Similar -> smooth continuation beyond train length.')

pe_test = pe_long
norms = np.linalg.norm(pe_test, axis=1, keepdims=True) + 1e-9
cos_sim = (pe_test / norms) @ (pe_test / norms).T
np.fill_diagonal(cos_sim, 0)
print('Max off-diagonal cos similarity (all positions): {:.4f}'.format(cos_sim.max()))
print('Low -> unique encoding even beyond training length.')
```

## With vs Without Positional Encoding

Without positional encoding, the Transformer treats its input as a set rather than a sequence. For any task where the output depends on token order (translation, language modelling, sequence classification based on word order), removing PE causes significant degradation. The degradation is total for tasks where two different orderings map to completely different semantics (e.g., 'man bites dog' vs 'dog bites man'). For bag-of-words tasks (sentiment classification of short text) the effect is mild.

```python
import numpy as np

def softmax(S):
    S = S - S.max(axis=-1, keepdims=True)
    e = np.exp(S); return e / e.sum(axis=-1, keepdims=True)

def sdp_attn(Q, K, V):
    A = softmax(Q @ K.T / np.sqrt(Q.shape[-1]))
    return A @ V

def sinusoidal_pe(n, d):
    PE = np.zeros((n, d))
    pos = np.arange(n)[:, np.newaxis]
    i   = np.arange(0, d, 2)[np.newaxis, :]
    PE[:, 0::2] = np.sin(pos / np.power(10000.0, i / d))
    PE[:, 1::2] = np.cos(pos / np.power(10000.0, i / d))
    return PE

np.random.seed(0)
n, d = 8, 32
W = np.random.randn(d, d) * 0.1
X = np.random.randn(n, d)
X_pe = X + sinusoidal_pe(n, d)

# Test: is the output permutation equivariant without PE?
perm = np.random.permutation(n)
out_no_pe        = sdp_attn(X @ W, X @ W, X)
out_perm_no_pe   = sdp_attn((X[perm] @ W), (X[perm] @ W), X[perm])
no_pe_equiv = np.allclose(out_no_pe[perm], out_perm_no_pe, atol=1e-10)
print('No PE  — permutation equivariant (output reorders with input):', no_pe_equiv)

out_pe           = sdp_attn(X_pe @ W, X_pe @ W, X_pe)
X_pe_perm = X[perm] + sinusoidal_pe(n, d)
out_perm_pe      = sdp_attn(X_pe_perm @ W, X_pe_perm @ W, X_pe_perm)
pe_equiv = np.allclose(out_pe[perm], out_perm_pe, atol=1e-5)
print('With PE — permutation equivariant:', pe_equiv)
print('PE breaks permutation symmetry: model distinguishes token order.')
```

## Comparison of Positional Encodings

Sinusoidal PE was the standard until learned positional embeddings (BERT, GPT-2) showed that data-driven positions improve downstream task performance at the cost of extrapolation ability. RoPE and ALiBi later restored length generalisation with different mechanisms: RoPE rotates Q and K directly in the complex plane (introducing relative position into the attention score), while ALiBi subtracts a linear position bias from attention scores without modifying Q or K. Current best practice for models that need to extend to long contexts is RoPE with frequency interpolation (YaRN, LongRoPE).

| Encoding | Extrapolates Beyond Train Len | Relative Position Info | Learnable Params | Used In |
| --- | --- | --- | --- | --- |
| Sinusoidal (Vaswani 2017) | Yes — formula extrapolates smoothly | Implicit via linear-shift property | None | Original Transformer, some encoder-decoder models |
| Learned absolute | No — undefined beyond vocab size | None explicit | max_len × d_model | BERT, GPT-2, ViT |
| RoPE (Su et al. 2021) | Yes with frequency scaling | Yes — explicit rotation by relative angle | None | LLaMA, Mistral, Falcon, Gemma, PaLM 2 |
| ALiBi (Press et al. 2022) | Yes — linear bias extrapolates | Yes — linear distance penalty per head | h learnable slopes (or fixed) | BLOOM, MPT, some OPT variants |
| NoPE (no PE) | Yes (no position at all) | None — bag-of-words | None | Some encoder-only models; relative PE in T5 |

For new architectures intended to handle variable or long context, RoPE with rope_theta tuning (increasing 10000 to 500,000 for context extension) is the current default. ALiBi offers simpler implementation and strong length generalisation but lacks the relative-position expressiveness of RoPE. Sinusoidal PE remains valuable for understanding — its linear-shift property is the conceptual ancestor of RoPE's rotation mechanism.

---

