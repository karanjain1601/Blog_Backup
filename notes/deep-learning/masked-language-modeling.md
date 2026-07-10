---
title: "Masked Language Modeling — BERT-Style Objective and Bidirectional Pretraining"
slug: "masked-language-modeling"
description: "MLM trains encoder-only transformers (BERT, RoBERTa, DeBERTa) to predict randomly masked tokens from full bidirectional context, using a 15% masking rate with an 80/10/10 replacement strategy, enabling rich contextual representations for downstream NLU tasks."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWFza2VkIExhbmd1YWdlIE1vZGVsaW5nIChNTE0pLCBpbnRyb2R1Y2VkIGluIEJFUlQgKERldmxpbiBldCBhbC4sIDIwMTgpLCBsZWFybnMgYmlkaXJlY3Rpb25hbCBjb250ZXh0dWFsIHJlcHJlc2VudGF0aW9ucyBieSBwcmVkaWN0aW5nIHJhbmRvbWx5IG1hc2tlZCB0b2tlbnMgZnJvbSB0aGVpciBmdWxsIHN1cnJvdW5kaW5nIGNvbnRleHQuIFVubGlrZSBDTE0gd2hpY2ggcHJvY2Vzc2VzIHRva2VucyBsZWZ0LXRvLXJpZ2h0LCBNTE0gdXNlcyB1bnJlc3RyaWN0ZWQgYXR0ZW50aW9uIOKAlCBldmVyeSB0b2tlbiBjYW4gYXR0ZW5kIHRvIGV2ZXJ5IG90aGVyIHRva2VuIGluIHRoZSBzZXF1ZW5jZS4gVGhpcyBiaWRpcmVjdGlvbmFsaXR5IHByb2R1Y2VzIHJpY2hlciByZXByZXNlbnRhdGlvbnMgZm9yIHVuZGVyc3RhbmRpbmcgdGFza3M6IHRoZSByZXByZXNlbnRhdGlvbiBvZiB0aGUgd29yZCBcdTAwMjdiYW5rXHUwMDI3IGluIFx1MDAyN3JpdmVyIGJhbmtcdTAwMjcgdnMgXHUwMDI3YmFuayBhY2NvdW50XHUwMDI3IGlzIGRpc2FtYmlndWF0ZWQgYnkgY29udGV4dCBmcm9tIGJvdGggc2lkZXMuIFRoZSB0cmFkZW9mZiBpcyB0aGF0IE1MTSBjYW5ub3QgZ2VuZXJhdGUgdGV4dCBuYXR1cmFsbHksIGFuZCBpdCBvbmx5IHN1cGVydmlzZXMgfjE1JSBvZiB0b2tlbiBwb3NpdGlvbnMgcGVyIGZvcndhcmQgcGFzcywgbWFraW5nIGl0IGxlc3MgY29tcHV0ZS1lZmZpY2llbnQgZm9yIHByZXRyYWluaW5nIHRoYW4gQ0xNLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJFUlQgTWFza2luZyBTdHJhdGVneSDigJQgVGhlIDgwLzEwLzEwIFJ1bGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJFUlQgcmFuZG9tbHkgc2VsZWN0cyAxNSUgb2YgaW5wdXQgdG9rZW5zIGZvciBtYXNraW5nLCB0aGVuIGFwcGxpZXMgYSB0aHJlZS13YXkgc3RyYXRlZ3k6IDgwJSBvZiBzZWxlY3RlZCB0b2tlbnMgYXJlIHJlcGxhY2VkIHdpdGggdGhlIHNwZWNpYWwgW01BU0tdIHRva2VuOyAxMCUgYXJlIHJlcGxhY2VkIHdpdGggYSByYW5kb20gdm9jYWJ1bGFyeSB0b2tlbjsgMTAlIGFyZSBrZXB0IHVuY2hhbmdlZC4gVGhlIDEwJSByYW5kb20gcmVwbGFjZW1lbnQgcHJldmVudHMgdGhlIG1vZGVsIGZyb20gbGVhcm5pbmcgdGhhdCBvbmx5IFtNQVNLXSBwb3NpdGlvbnMgbmVlZCB0byBiZSBwcmVkaWN0ZWQg4oCUIGl0IG11c3QgY2hlY2sgZXZlcnkgdG9rZW4uIFRoZSAxMCUgdW5jaGFuZ2VkIHJhdGUgcHJldmVudHMgYSB0cmFpbi90ZXN0IG1pc21hdGNoIHdoZXJlIFtNQVNLXSB0b2tlbnMgYXBwZWFyIG9ubHkgZHVyaW5nIHByZXRyYWluaW5nIGJ1dCBuZXZlciBhdCBmaW5lLXR1bmluZyB0aW1lLiBUaGUgbG9zcyBpcyBjb21wdXRlZCBvbmx5IG9uIHRoZSAxNSUgbWFza2VkIHBvc2l0aW9ucywgbm90IG9uIHRoZSBmdWxsIHNlcXVlbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBCZXJ0VG9rZW5pemVyXG5cbmRlZiBtbG1fbWFza190b2tlbnMoaW5wdXRfaWRzLCB0b2tlbml6ZXIsIG1sbV9wcm9iPTAuMTUpOlxuICAgIFwiXCJcIkJFUlQgODAvMTAvMTAgbWFza2luZzogODAlIFtNQVNLXSwgMTAlIHJhbmRvbSB0b2tlbiwgMTAlIHVuY2hhbmdlZC5cIlwiXCJcbiAgICBsYWJlbHMgPSBpbnB1dF9pZHMuY2xvbmUoKVxuICAgIHByb2JfbWF0cml4ID0gdG9yY2guZnVsbChsYWJlbHMuc2hhcGUsIG1sbV9wcm9iKVxuICAgIHNwZWNpYWxfaWRzID0gc2V0KHRva2VuaXplci5hbGxfc3BlY2lhbF9pZHMpXG4gICAgZm9yIGksIHJvdyBpbiBlbnVtZXJhdGUoaW5wdXRfaWRzLnRvbGlzdCgpKTpcbiAgICAgICAgZm9yIGosIHRvayBpbiBlbnVtZXJhdGUocm93KTpcbiAgICAgICAgICAgIGlmIHRvayBpbiBzcGVjaWFsX2lkczpcbiAgICAgICAgICAgICAgICBwcm9iX21hdHJpeFtpLCBqXSA9IDAuMCAgIyBuZXZlciBtYXNrIFtDTFNdLCBbU0VQXSwgW1BBRF1cbiAgICBtYXNrZWRfaW5kaWNlcyA9IHRvcmNoLmJlcm5vdWxsaShwcm9iX21hdHJpeCkuYm9vbCgpXG4gICAgbGFiZWxzW35tYXNrZWRfaW5kaWNlc10gPSAtMTAwICAgICAgICAgICMgbG9zcyBvbmx5IG9uIG1hc2tlZCBwb3NpdGlvbnNcbiAgICAjIDgwJTogcmVwbGFjZSB3aXRoIFtNQVNLXVxuICAgIG1hc2tfODAgPSB0b3JjaC5iZXJub3VsbGkodG9yY2guZnVsbChsYWJlbHMuc2hhcGUsIDAuOCkpLmJvb2woKSBcdTAwMjYgbWFza2VkX2luZGljZXNcbiAgICBpbnB1dF9pZHNbbWFza184MF0gPSB0b2tlbml6ZXIubWFza190b2tlbl9pZFxuICAgICMgMTAlOiByZXBsYWNlIHdpdGggcmFuZG9tIHRva2VuIChoYWxmIG9mIHJlbWFpbmluZyAyMCUpXG4gICAgcmFuZF8yMCAgPSAofm1hc2tfODApIFx1MDAyNiBtYXNrZWRfaW5kaWNlc1xuICAgIG1hc2tfMTAgID0gdG9yY2guYmVybm91bGxpKHRvcmNoLmZ1bGwobGFiZWxzLnNoYXBlLCAwLjUpKS5ib29sKCkgXHUwMDI2IHJhbmRfMjBcbiAgICByYW5kb21fdG9rZW5zID0gdG9yY2gucmFuZGludChsZW4odG9rZW5pemVyKSwgbGFiZWxzLnNoYXBlLCBkdHlwZT10b3JjaC5sb25nKVxuICAgIGlucHV0X2lkc1ttYXNrXzEwXSA9IHJhbmRvbV90b2tlbnNbbWFza18xMF1cbiAgICAjIDEwJToga2VlcCB1bmNoYW5nZWQg4oCUIHRoZSBvdGhlciBoYWxmIG9mIHJhbmRfMjAsIG5vIGFjdGlvbiBuZWVkZWRcbiAgICByZXR1cm4gaW5wdXRfaWRzLCBsYWJlbHNcblxudG9rZW5pemVyID0gQmVydFRva2VuaXplci5mcm9tX3ByZXRyYWluZWQoXCJiZXJ0LWJhc2UtdW5jYXNlZFwiKVxudGV4dCA9IFwiVGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZyBhbmQgcnVucyBhd2F5IGZyb20gdGhlIGZhcm1lclwiXG5pZHMgID0gdG9rZW5pemVyKHRleHQsIHJldHVybl90ZW5zb3JzPVwicHRcIiwgbWF4X2xlbmd0aD02NCwgdHJ1bmNhdGlvbj1UcnVlKVtcImlucHV0X2lkc1wiXVxubWFza2VkX2lkcywgbGFiZWxzID0gbWxtX21hc2tfdG9rZW5zKGlkcy5jbG9uZSgpLCB0b2tlbml6ZXIpXG5wcmludChmXCJTZXF1ZW5jZToge2lkcy5zaXplKDEpfSB0b2tlbnMgfCBNYXNrZWQ6IHsobGFiZWxzICE9IC0xMDApLnN1bSgpLml0ZW0oKX0gfCBbTUFTS106IHsobWFza2VkX2lkcyA9PSB0b2tlbml6ZXIubWFza190b2tlbl9pZCkuc3VtKCkuaXRlbSgpfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1MTSBUcmFpbmluZyBGb3J3YXJkIFBhc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBNTE0gdHJhaW5pbmcgbG9vcCBhcHBsaWVzIHRoZSBtYXNraW5nIGNvbGxhdG9yIG9uIHRoZSBmbHkgKGR5bmFtaWMgbWFza2luZykgc28gdGhhdCBlYWNoIGVwb2NoIHNlZXMgZGlmZmVyZW50IG1hc2tlZCBwb3NpdGlvbnMgZm9yIHRoZSBzYW1lIHRleHQg4oCUIHRoaXMgYWN0cyBhcyBpbXBsaWNpdCBkYXRhIGF1Z21lbnRhdGlvbi4gVGhlIG1vZGVsXHUwMDI3cyBsb3NzIGlzIHRoZSBjcm9zcy1lbnRyb3B5IGJldHdlZW4gdGhlIHByZWRpY3RlZCBsb2dpdCBkaXN0cmlidXRpb24gYW5kIHRoZSB0cnVlIHRva2VuIElELCBzdW1tZWQgb25seSBvdmVyIHBvc2l0aW9ucyB3aGVyZSBsYWJlbHMg4omgIC0xMDAuIEh1Z2dpbmdGYWNlXHUwMDI3cyBCZXJ0Rm9yTWFza2VkTE0gaGFuZGxlcyB0aGlzIGF1dG9tYXRpY2FsbHkgd2hlbiBsYWJlbHMgYXJlIHBhc3NlZDogaXQgY2FsbHMgQ3Jvc3NFbnRyb3B5TG9zcyB3aXRoIGlnbm9yZV9pbmRleD0tMTAwIGludGVybmFsbHkuIFR5cGljYWwgaHlwZXJwYXJhbWV0ZXJzOiBsZWFybmluZyByYXRlIDFlLTQsIHdhcm11cCAxMGsgc3RlcHMsIGJhdGNoIHNpemUgMjU2LCBBZGFtVyB3aXRoIHdlaWdodCBkZWNheSAwLjAxLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBCZXJ0Rm9yTWFza2VkTE0sIEJlcnRUb2tlbml6ZXJcblxuZGVmIHRyYWluX21sbV9zdGVwKG1vZGVsLCBiYXRjaCwgdG9rZW5pemVyLCBvcHRpbWl6ZXIsIGRldmljZSk6XG4gICAgXCJcIlwiU2luZ2xlIE1MTSB0cmFpbmluZyBzdGVwOiBhcHBseSBtYXNraW5nLCBmb3J3YXJkIHBhc3MsIGJhY2twcm9wLlwiXCJcIlxuICAgIGlucHV0X2lkcyAgPSBiYXRjaFtcImlucHV0X2lkc1wiXS5jbG9uZSgpLnRvKGRldmljZSlcbiAgICBhdHRuX21hc2sgID0gYmF0Y2hbXCJhdHRlbnRpb25fbWFza1wiXS50byhkZXZpY2UpXG4gICAgbWFza2VkX2lkcywgbGFiZWxzID0gbWxtX21hc2tfdG9rZW5zKGlucHV0X2lkcywgdG9rZW5pemVyKVxuICAgIGxhYmVscyA9IGxhYmVscy50byhkZXZpY2UpXG4gICAgb3V0cHV0cyA9IG1vZGVsKFxuICAgICAgICBpbnB1dF9pZHM9bWFza2VkX2lkcyxcbiAgICAgICAgYXR0ZW50aW9uX21hc2s9YXR0bl9tYXNrLFxuICAgICAgICBsYWJlbHM9bGFiZWxzLCAgICAgICAgICAgICMgQmVydEZvck1hc2tlZExNIGlnbm9yZXMgbGFiZWw9LTEwMCBpbiBsb3NzXG4gICAgKVxuICAgIGxvc3MgICAgID0gb3V0cHV0cy5sb3NzICAgICAgICMgY3Jvc3MtZW50cm9weSBvdmVyIG1hc2tlZCBwb3NpdGlvbnMgb25seVxuICAgIG5fbWFza2VkID0gKGxhYmVscyAhPSAtMTAwKS5zdW0oKS5pdGVtKClcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICB0b3JjaC5ubi51dGlscy5jbGlwX2dyYWRfbm9ybV8obW9kZWwucGFyYW1ldGVycygpLCAxLjApXG4gICAgb3B0aW1pemVyLnN0ZXAoKVxuICAgIHJldHVybiBsb3NzLml0ZW0oKSwgbl9tYXNrZWRcblxuZGV2aWNlICAgID0gXCJjdWRhXCIgaWYgdG9yY2guY3VkYS5pc19hdmFpbGFibGUoKSBlbHNlIFwiY3B1XCJcbm1vZGVsICAgICA9IEJlcnRGb3JNYXNrZWRMTS5mcm9tX3ByZXRyYWluZWQoXCJiZXJ0LWJhc2UtdW5jYXNlZFwiKS50byhkZXZpY2UpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtVyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTQsIHdlaWdodF9kZWNheT0wLjAxKVxubl9wYXJhbXMgID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpIC8gMWU2XG5wcmludChmXCJCRVJULWJhc2UgcGFyYW1ldGVyczoge25fcGFyYW1zOi4wZn1NXCIpXG5wcmludChcIk1MTSBsb3NzIGlzIGF2ZXJhZ2VkIG9ubHkgb3ZlciB+MTUlIG1hc2tlZCBwb3NpdGlvbnMsIG5vdCBhbGwgTiB0b2tlbnMuXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3BhbiBNYXNraW5nIOKAlCBTcGFuQkVSVCBTdHlsZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG9rZW4tbGV2ZWwgbWFza2luZyAoQkVSVCkgbWFza3MgaW5kaXZpZHVhbCBzdWJ3b3JkIHRva2VucyBpbmRlcGVuZGVudGx5LCBidXQgc3BhbiBtYXNraW5nIChTcGFuQkVSVCwgSm9zaGkgZXQgYWwuIDIwMjApIG1hc2tzIGNvbnRpZ3VvdXMgc3BhbnMgb2YgdG9rZW5zIGRyYXduIGZyb20gYSBnZW9tZXRyaWMgZGlzdHJpYnV0aW9uLiBNYXNraW5nIGNvbnRpZ3VvdXMgc3BhbnMgaXMgaGFyZGVyIGJlY2F1c2UgdGhlIG1vZGVsIGNhbm5vdCB1c2UgYWRqYWNlbnQgbWFza2VkIHRva2VucyBhcyBoaW50cyDigJQgaXQgbXVzdCByZWx5IG9uIHRoZSBmdWxsIHN1cnJvdW5kaW5nIGNvbnRleHQuIFNwYW5CRVJUIGFsc28gaW50cm9kdWNlcyB0aGUgU3BhbiBCb3VuZGFyeSBPYmplY3RpdmUgKFNCTyk6IHByZWRpY3QgZWFjaCBtYXNrZWQgdG9rZW4gdXNpbmcgb25seSB0aGUgdHdvIGJvdW5kYXJ5IHRva2VucyBvbiBlaXRoZXIgc2lkZSBvZiB0aGUgc3Bhbiwgd2l0aG91dCBzZWVpbmcgYW55IHRva2VucyBpbnNpZGUgdGhlIHNwYW4uIFRvZ2V0aGVyLCB0aGVzZSBjaGFuZ2VzIHByb2R1Y2Ugc2lnbmlmaWNhbnRseSBiZXR0ZXIgcGVyZm9ybWFuY2Ugb24gc3Bhbi1leHRyYWN0aW9uIHRhc2tzIGxpa2UgU1F1QUQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHJhbmRvbVxuaW1wb3J0IG1hdGhcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBCZXJ0VG9rZW5pemVyXG5cbmRlZiBzcGFuX21hc2tfdG9rZW5zKGlucHV0X2lkcywgdG9rZW5pemVyLCBub2lzZV9kZW5zaXR5PTAuMTUsIG1lYW5fc3Bhbj0zLjApOlxuICAgIFwiXCJcIlNwYW5CRVJULXN0eWxlIGdlb21ldHJpYyBzcGFuIG1hc2tpbmcgb24gYSAxRCB0b2tlbiBzZXF1ZW5jZS5cIlwiXCJcbiAgICBzcGVjaWFsX2lkcyA9IHNldCh0b2tlbml6ZXIuYWxsX3NwZWNpYWxfaWRzKVxuICAgIHNlcSA9IGlucHV0X2lkcy50b2xpc3QoKVxuICAgIG4gICA9IGxlbihzZXEpXG4gICAgdGFyZ2V0X25fbWFza2VkID0gbWF4KDEsIGludChuICogbm9pc2VfZGVuc2l0eSkpXG4gICAgbWFza2VkX3Bvc2l0aW9ucyA9IHNldCgpXG4gICAgd2hpbGUgbGVuKG1hc2tlZF9wb3NpdGlvbnMpIFx1MDAzYyB0YXJnZXRfbl9tYXNrZWQ6XG4gICAgICAgIHNwYW5fbGVuID0gbWF4KDEsIGludCgtbWVhbl9zcGFuICogbWF0aC5sb2cobWF4KHJhbmRvbS5yYW5kb20oKSwgMWUtMTApKSkpXG4gICAgICAgIHN0YXJ0ICAgID0gcmFuZG9tLnJhbmRpbnQoMCwgbiAtIDEpXG4gICAgICAgIGZvciBwIGluIHJhbmdlKHN0YXJ0LCBtaW4oc3RhcnQgKyBzcGFuX2xlbiwgbikpOlxuICAgICAgICAgICAgaWYgc2VxW3BdIG5vdCBpbiBzcGVjaWFsX2lkczpcbiAgICAgICAgICAgICAgICBtYXNrZWRfcG9zaXRpb25zLmFkZChwKVxuICAgIHJlc3VsdCA9IGlucHV0X2lkcy5jbG9uZSgpXG4gICAgbGFiZWxzID0gaW5wdXRfaWRzLmNsb25lKClcbiAgICBmb3IgcCBpbiByYW5nZShuKTpcbiAgICAgICAgaWYgcCBpbiBtYXNrZWRfcG9zaXRpb25zOlxuICAgICAgICAgICAgcmVzdWx0W3BdID0gdG9rZW5pemVyLm1hc2tfdG9rZW5faWRcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIGxhYmVsc1twXSA9IC0xMDBcbiAgICByZXR1cm4gcmVzdWx0LCBsYWJlbHNcblxudG9rZW5pemVyID0gQmVydFRva2VuaXplci5mcm9tX3ByZXRyYWluZWQoXCJiZXJ0LWJhc2UtdW5jYXNlZFwiKVxuaWRzID0gdG9rZW5pemVyLmVuY29kZShcIlNwYW4gbWFza2luZyBzZWxlY3RzIGNvbnRpZ3VvdXMgdG9rZW4gc3BhbnMgZm9yIG1hc2tpbmdcIixcbiAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybl90ZW5zb3JzPVwicHRcIilbMF1cbnJlc3VsdCwgbGFiZWxzID0gc3Bhbl9tYXNrX3Rva2VucyhpZHMsIHRva2VuaXplcilcbnByaW50KGZcIlRva2Vuczoge2xlbihpZHMpfSB8IE1hc2tlZDogeyhsYWJlbHMgIT0gLTEwMCkuc3VtKCkuaXRlbSgpfSBzcGFucyBtYXNrZWRcIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6Ik1MTSBDb21wdXRlIEVmZmljaWVuY3kgdnMgQ0xNIiwiY29udGVudCI6Ik1MTSBsZWFybnMgb25seSAxNSUgb2YgcG9zaXRpb25zIHBlciBmb3J3YXJkIHBhc3MgdnMgMTAwJSBmb3IgQ0xNIOKAlCB0aGlzIG1lYW5zIE1MTSByZXF1aXJlcyBzaWduaWZpY2FudGx5IG1vcmUgZGF0YSBvciBlcG9jaHMgdG8gc2VlIGVhY2ggdG9rZW4gYXMgYSB0YXJnZXQsIG1ha2luZyBpdCBsZXNzIGNvbXB1dGUtZWZmaWNpZW50IHBlciB0b2tlbiBmb3IgcHJldHJhaW5pbmcuIFJvQkVSVGEgYWRkcmVzc2VkIHRoaXMgd2l0aCBkeW5hbWljIG1hc2tpbmcgYW5kIG11Y2ggbGFyZ2VyIGRhdGEgKDE2MEdCIHZzIEJFUlRcdTAwMjdzIDE2R0IpLCBub3QgYSBjaGFuZ2UgdG8gdGhlIG9iamVjdGl2ZSBpdHNlbGYuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQkVSVCBGaW5lLVR1bmluZyBmb3IgQ2xhc3NpZmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1MTSBwcmV0cmFpbmluZyBsZWFybnMgZ2VuZXJhbC1wdXJwb3NlIHJlcHJlc2VudGF0aW9uczsgdGFzay1zcGVjaWZpYyBhZGFwdGF0aW9uIGlzIGRvbmUgYnkgZmluZS10dW5pbmcuIEZvciBjbGFzc2lmaWNhdGlvbiwgYSBsaW5lYXIgaGVhZCBpcyBhZGRlZCBvbiB0b3Agb2YgdGhlIFtDTFNdIHRva2VuIHJlcHJlc2VudGF0aW9uICh0aGUgZmlyc3QgdG9rZW4sIHdoaWNoIGFnZ3JlZ2F0ZXMgc2VxdWVuY2UtbGV2ZWwgaW5mb3JtYXRpb24gdGhyb3VnaCBiaWRpcmVjdGlvbmFsIGF0dGVudGlvbikuIFRoZSBmdWxsIG1vZGVsIChlbmNvZGVyICsgaGVhZCkgaXMgdGhlbiB0cmFpbmVkIGVuZC10by1lbmQgb24gbGFiZWxsZWQgZGF0YSB3aXRoIGEgbXVjaCBzbWFsbGVyIGxlYXJuaW5nIHJhdGUgKDJlLTUgdG8gNWUtNSkuIEZyZWV6aW5nIHRoZSBlbWJlZGRpbmcgbGF5ZXIgd2hpbGUgZmluZS10dW5pbmcgYWxsIHRyYW5zZm9ybWVyIGxheWVycyByZWR1Y2VzIHRoZSBudW1iZXIgb2YgdHJhaW5hYmxlIHBhcmFtZXRlcnMgc2xpZ2h0bHkgYW5kIG9mdGVuIGltcHJvdmVzIHN0YWJpbGl0eSBvbiBzbWFsbCBkYXRhc2V0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBCZXJ0TW9kZWwsIEJlcnRUb2tlbml6ZXJcblxuY2xhc3MgQmVydENsYXNzaWZpZXIobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJCRVJUIGZvciBzZXF1ZW5jZSBjbGFzc2lmaWNhdGlvbiB1c2luZyBbQ0xTXSB0b2tlbiByZXByZXNlbnRhdGlvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbW9kZWxfbmFtZT1cImJlcnQtYmFzZS11bmNhc2VkXCIsIG51bV9sYWJlbHM9MiwgZnJlZXplX2VtYj1UcnVlKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmVydCA9IEJlcnRNb2RlbC5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSlcbiAgICAgICAgaWYgZnJlZXplX2VtYjpcbiAgICAgICAgICAgIGZvciBwIGluIHNlbGYuYmVydC5lbWJlZGRpbmdzLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgICAgICAgICBwLnJlcXVpcmVzX2dyYWRfKEZhbHNlKVxuICAgICAgICBoaWRkZW4gPSBzZWxmLmJlcnQuY29uZmlnLmhpZGRlbl9zaXplICAgIyA3NjggZm9yIEJFUlQtYmFzZVxuICAgICAgICBzZWxmLmNsYXNzaWZpZXIgPSBubi5TZXF1ZW50aWFsKG5uLkRyb3BvdXQoMC4xKSwgbm4uTGluZWFyKGhpZGRlbiwgbnVtX2xhYmVscykpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBpbnB1dF9pZHMsIGF0dGVudGlvbl9tYXNrLCB0b2tlbl90eXBlX2lkcz1Ob25lKTpcbiAgICAgICAgb3V0ICAgICAgPSBzZWxmLmJlcnQoaW5wdXRfaWRzPWlucHV0X2lkcywgYXR0ZW50aW9uX21hc2s9YXR0ZW50aW9uX21hc2ssXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRva2VuX3R5cGVfaWRzPXRva2VuX3R5cGVfaWRzKVxuICAgICAgICBjbHNfcmVwciA9IG91dC5sYXN0X2hpZGRlbl9zdGF0ZVs6LCAwLCA6XSAgICMgW0NMU10gdG9rZW4gYXQgcG9zaXRpb24gMFxuICAgICAgICByZXR1cm4gc2VsZi5jbGFzc2lmaWVyKGNsc19yZXByKVxuXG5kZXZpY2UgPSBcImN1ZGFcIiBpZiB0b3JjaC5jdWRhLmlzX2F2YWlsYWJsZSgpIGVsc2UgXCJjcHVcIlxubW9kZWwgID0gQmVydENsYXNzaWZpZXIobnVtX2xhYmVscz0yKS50byhkZXZpY2UpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtVyhcbiAgICBmaWx0ZXIobGFtYmRhIHA6IHAucmVxdWlyZXNfZ3JhZCwgbW9kZWwucGFyYW1ldGVycygpKSwgbHI9MmUtNVxuKVxudHJhaW5hYmxlID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkgaWYgcC5yZXF1aXJlc19ncmFkKVxucHJpbnQoZlwiVHJhaW5hYmxlIHBhcmFtZXRlcnM6IHt0cmFpbmFibGUgLyAxZTY6LjFmfU0gKGVtYmVkZGluZ3MgZnJvemVuKVwiKVxucHJpbnQoXCJGaW5lLXR1bmUgW0NMU10g4oaSIGxpbmVhciBoZWFkOyBubyBjYXVzYWwgbWFzayDigJQgZnVsbCBiaWRpcmVjdGlvbmFsIGF0dGVudGlvbi5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNTE0gVmFyaWFudHMgQ29tcGFyZWQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvcmlnaW5hbCBCRVJUIHBhcGVyIHNwYXduZWQgYSBmYW1pbHkgb2YgZW5jb2Rlci1vbmx5IG1vZGVscyB0aGF0IHJlZmluZWQgdGhlIG1hc2tpbmcgc3RyYXRlZ3ksIHJlbW92ZWQgb3IgcmVwbGFjZWQgdGhlIE5leHQgU2VudGVuY2UgUHJlZGljdGlvbiAoTlNQKSBhdXhpbGlhcnkgdGFzaywgYW5kIHNjYWxlZCBkYXRhIGFuZCBjb21wdXRlLiBSb0JFUlRhIChMaXUgZXQgYWwuIDIwMTkpIHdhcyB0aGUgZmlyc3QgbWFqb3IgYWJsYXRpb246IGRyb3BwaW5nIE5TUCwgZHluYW1pYyBtYXNraW5nLCBhbmQgdHJhaW5pbmcgMTDDlyBsb25nZXIgb24gMTDDlyBtb3JlIGRhdGEgaW1wcm92ZWQgQkVSVFx1MDAyN3MgR0xVRSBzY29yZSBzdWJzdGFudGlhbGx5IHdpdGhvdXQgYW55IGFyY2hpdGVjdHVyYWwgY2hhbmdlLiBEZUJFUlRhIGludHJvZHVjZWQgZGlzZW50YW5nbGVkIGF0dGVudGlvbiDigJQgc2VwYXJhdGUgZW1iZWRkaW5ncyBmb3IgdG9rZW4gY29udGVudCBhbmQgcmVsYXRpdmUgcG9zaXRpb24g4oCUIHNldHRpbmcgbmV3IFNPVEEgb24gbWFueSBiZW5jaG1hcmtzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIk1hc2tpbmcgU3RyYXRlZ3kiLCJOU1AiLCJNYXNraW5nIFJhdGlvIiwiS2V5IElubm92YXRpb24iXSwicm93cyI6W1siQkVSVCIsIlRva2VuLWxldmVsIDgwLzEwLzEwIiwiWWVzIiwiMTUlIiwiQmlkaXJlY3Rpb25hbCBwcmV0cmFpbmluZyB3aXRoIE1MTSArIE5TUCJdLFsiUm9CRVJUYSIsIkR5bmFtaWMgdG9rZW4gbWFza2luZyIsIk5vIiwiMTUlIiwiTW9yZSBkYXRhLCBsb25nZXIgdHJhaW5pbmcsIG5vIE5TUCDigJQgc3Ryb25nIGJhc2VsaW5lIl0sWyJEZUJFUlRhIiwiVG9rZW4gKyBwb3NpdGlvbiBtYXNraW5nIiwiTm8iLCIxNSUiLCJEaXNlbnRhbmdsZWQgYXR0ZW50aW9uOiBzZXBhcmF0ZSBjb250ZW50IGFuZCBwb3NpdGlvbiJdLFsiU3BhbkJFUlQiLCJDb250aWd1b3VzIHNwYW4gbWFza2luZyIsIk5vIiwiMTUlIiwiU0JPOiBwcmVkaWN0IHNwYW5zIHVzaW5nIGJvdW5kYXJ5IHRva2VuIGNvbnRleHQgb25seSJdLFsiQUxCRVJUIiwiVG9rZW4tbGV2ZWwgKHNoYXJlZCB3ZWlnaHRzKSIsIk5vIChTT1ApIiwiMTUlIiwiQ3Jvc3MtbGF5ZXIgd2VpZ2h0IHNoYXJpbmcgKyBzZW50ZW5jZSBvcmRlciBwcmVkaWN0aW9uIl0sWyJYTE5ldCIsIlBlcm11dGF0aW9uIGxhbmd1YWdlIG1vZGVsaW5nIiwiTm8iLCJBbGwgcG9zaXRpb25zIiwiQVIgb3ZlciByYW5kb20gcGVybXV0YXRpb25zIOKAlCBiaWRpcmVjdGlvbmFsIHdpdGhvdXQgW01BU0tdIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEeW5hbWljIGFuZCBXaG9sZS1Xb3JkIE1hc2tpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YXRpYyBtYXNraW5nIChvcmlnaW5hbCBCRVJUKSBhcHBsaWVzIGEgZml4ZWQgbWFza2luZyBwYXR0ZXJuIHRvIGVhY2ggdHJhaW5pbmcgZXhhbXBsZSBvbmNlIGR1cmluZyBwcmVwcm9jZXNzaW5nIOKAlCB0aGUgbW9kZWwgc2VlcyB0aGUgc2FtZSBtYXNrZWQgdmVyc2lvbiBvZiBlYWNoIHNlbnRlbmNlIGV2ZXJ5IGVwb2NoLiBEeW5hbWljIG1hc2tpbmcgKFJvQkVSVGEpIHJlLWFwcGxpZXMgdGhlIG1hc2tpbmcgZnVuY3Rpb24gYXQgZWFjaCB0cmFpbmluZyBzdGVwLCBzbyB0aGUgbW9kZWwgc2VlcyBkaWZmZXJlbnQgbWFza2VkIHBvc2l0aW9ucyBhY3Jvc3MgZXBvY2hzIGZvciB0aGUgc2FtZSB0ZXh0LiBXaG9sZS13b3JkIG1hc2tpbmcgZW5zdXJlcyB0aGF0IGlmIGEgd29yZCBpcyB0b2tlbmlzZWQgaW50byBtdWx0aXBsZSBzdWJ3b3JkIHBpZWNlcywgYWxsIHBpZWNlcyBhcmUgbWFza2VkIG9yIHVubWFza2VkIHRvZ2V0aGVyIOKAlCBwcmV2ZW50aW5nIHRoZSBtb2RlbCBmcm9tIHRyaXZpYWxseSBwcmVkaWN0aW5nIGEgbWFza2VkIHN1YndvcmQgZnJvbSBhbiBhZGphY2VudCB2aXNpYmxlIHN1YndvcmQgb2YgdGhlIHNhbWUgd29yZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlN0YXRpYyBtYXNraW5nIChCRVJUKTogbWFza2luZyBhcHBsaWVkIG9uY2UgYXQgZGF0YSBwcmVwcm9jZXNzaW5nIOKAlCBlYWNoIGVwb2NoIHNlZXMgdGhlIHNhbWUgbWFza3MuIiwiRHluYW1pYyBtYXNraW5nIChSb0JFUlRhKTogbWFza2luZyByZXNhbXBsZWQgYXQgZWFjaCBzdGVwIOKAlCBlZmZlY3RpdmUgMTDDlyBtb3JlIHZhcmlhdGlvbiBwZXIgdHJhaW5pbmcgZXhhbXBsZS4iLCJXaG9sZS13b3JkIG1hc2tpbmc6IG1hc2sgYWxsIHN1YndvcmRzIG9mIGEgd29yZCB0b2dldGhlciDigJQgcHJldmVudHMgc3Vid29yZCBsZWFrYWdlIChlLmcuIFx1MDAyNyMjaW5nXHUwMDI3IHZpc2libGUgd2hlbiBcdTAwMjdydW5cdTAwMjcgaXMgbWFza2VkKS4iLCJTcGFuIG1hc2tpbmcgKFNwYW5CRVJUKTogbWFzayBjb250aWd1b3VzIHNwYW5zIGZyb20gZ2VvbWV0cmljIGRpc3RyaWJ1dGlvbiB3aXRoIG1lYW4gMy44IHRva2Vucy4iLCJFbnRpdHkvcGhyYXNlIG1hc2tpbmcgKEVSTklFLCBCYWlkdSk6IGFsd2F5cyBtYXNrIGNvbXBsZXRlIG5hbWVkIGVudGl0aWVzIG9yIHBocmFzZXMg4oCUIGJldHRlciBlbnRpdHktbGV2ZWwgcmVwcmVzZW50YXRpb25zLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOU1AgYW5kIEl0cyBSZW1vdmFsIGluIFJvQkVSVGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJFUlQgd2FzIHByZXRyYWluZWQgd2l0aCBhIHNlY29uZCBvYmplY3RpdmU6IE5leHQgU2VudGVuY2UgUHJlZGljdGlvbiAoTlNQKS4gR2l2ZW4gdHdvIHNlbnRlbmNlIHNlZ21lbnRzIEEgYW5kIEIsIHRoZSBtb2RlbCBtdXN0IHByZWRpY3Qgd2hldGhlciBCIG5hdHVyYWxseSBmb2xsb3dzIEEgKDUwJSBwb3NpdGl2ZSwgNTAlIG5lZ2F0aXZlIHdoZXJlIEIgaXMgc2FtcGxlZCBmcm9tIGEgcmFuZG9tIGRvY3VtZW50KS4gVGhlIGlkZWEgd2FzIHRvIGxlYXJuIGludGVyLXNlbnRlbmNlIGNvaGVyZW5jZS4gSG93ZXZlciwgUm9CRVJUYVx1MDAyN3MgYWJsYXRpb24gc3R1ZGllcyBzaG93ZWQgTlNQIHNsaWdodGx5IGh1cnRzIHBlcmZvcm1hbmNlOiB0aGUgdGFzayBpcyB0b28gZWFzeSAocmFuZG9tIG5lZ2F0aXZlcyBhcmUgZGlzdGluZ3Vpc2hhYmxlIGJ5IHRvcGljIGFsb25lKSwgYW5kIGl0IGZvcmNlcyBhcnRpZmljaWFsbHkgc2hvcnQgdHJhaW5pbmcgZG9jdW1lbnRzLiBSZW1vdmluZyBOU1AgYW5kIHRyYWluaW5nIG9uIGZ1bGwgZG9jdW1lbnRzIGltcHJvdmVkIGV2ZXJ5IGRvd25zdHJlYW0gYmVuY2htYXJrLiBMYXRlciBtb2RlbHMgKEFMQkVSVCkgcmVwbGFjZWQgTlNQIHdpdGggU2VudGVuY2UgT3JkZXIgUHJlZGljdGlvbiAoU09QKSwgd2hpY2ggaXMgaGFyZGVyIOKAlCB0aGUgbmVnYXRpdmUgaXMgdGhlIHNhbWUgdHdvIHNlbnRlbmNlcyBpbiByZXZlcnNlIG9yZGVyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJpZGlyZWN0aW9uYWwgQXR0ZW50aW9uIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBhcmNoaXRlY3R1cmFsIGRpZmZlcmVuY2UgYmV0d2VlbiBCRVJUIChlbmNvZGVyKSBhbmQgR1BUIChkZWNvZGVyKSBpcyB0aGUgYXR0ZW50aW9uIG1hc2suIEJFUlQgdXNlcyBmdWxsIGJpZGlyZWN0aW9uYWwgYXR0ZW50aW9uOiBubyBtYXNrIGlzIGFwcGxpZWQsIHNvIGV2ZXJ5IHRva2VuIGF0dGVuZHMgdG8gZXZlcnkgb3RoZXIgdG9rZW4gaW5jbHVkaW5nIGZ1dHVyZSB0b2tlbnMuIFRoaXMgaXMgaW1wbGVtZW50ZWQgaWRlbnRpY2FsbHkgdG8gc3RhbmRhcmQgbXVsdGktaGVhZCBzZWxmLWF0dGVudGlvbiBidXQgd2l0aG91dCB0aGUgbG93ZXItdHJpYW5ndWxhciBtYXNrLiBUaGUgY29uc2VxdWVuY2UgaXMgdGhhdCBCRVJUIGNhbm5vdCBnZW5lcmF0ZSB0ZXh0IGF1dG9yZWdyZXNzaXZlbHkg4oCUIGNvbXB1dGluZyBQKHjigpwgfCB4XHUwMDNj4oKcKSBpcyB1bmRlZmluZWQgdW5kZXIgYmlkaXJlY3Rpb25hbCBhdHRlbnRpb24uIEluc3RlYWQsIEJFUlRcdTAwMjdzIHN0cmVuZ3RoIGlzIHByb2R1Y2luZyBhIHNpbmdsZSBjb250ZXh0dWFsaXNlZCByZXByZXNlbnRhdGlvbiBmb3IgZWFjaCBpbnB1dCB0b2tlbiwgd2hpY2ggc2VydmVzIGFzIGEgZmVhdHVyZSBmb3IgY2xhc3NpZmljYXRpb24sIG5hbWVkIGVudGl0eSByZWNvZ25pdGlvbiwgcXVlc3Rpb24gYW5zd2VyaW5nLCBhbmQgb3RoZXIgdW5kZXJzdGFuZGluZyB0YXNrcy4ifV0="
---
# Masked Language Modeling — BERT-Style Objective and Bidirectional Pretraining

Masked Language Modeling (MLM), introduced in BERT (Devlin et al., 2018), learns bidirectional contextual representations by predicting randomly masked tokens from their full surrounding context. Unlike CLM which processes tokens left-to-right, MLM uses unrestricted attention — every token can attend to every other token in the sequence. This bidirectionality produces richer representations for understanding tasks: the representation of the word 'bank' in 'river bank' vs 'bank account' is disambiguated by context from both sides. The tradeoff is that MLM cannot generate text naturally, and it only supervises ~15% of token positions per forward pass, making it less compute-efficient for pretraining than CLM.

## BERT Masking Strategy — The 80/10/10 Rule

BERT randomly selects 15% of input tokens for masking, then applies a three-way strategy: 80% of selected tokens are replaced with the special [MASK] token; 10% are replaced with a random vocabulary token; 10% are kept unchanged. The 10% random replacement prevents the model from learning that only [MASK] positions need to be predicted — it must check every token. The 10% unchanged rate prevents a train/test mismatch where [MASK] tokens appear only during pretraining but never at fine-tuning time. The loss is computed only on the 15% masked positions, not on the full sequence.

```python
import torch
from transformers import BertTokenizer

def mlm_mask_tokens(input_ids, tokenizer, mlm_prob=0.15):
    """BERT 80/10/10 masking: 80% [MASK], 10% random token, 10% unchanged."""
    labels = input_ids.clone()
    prob_matrix = torch.full(labels.shape, mlm_prob)
    special_ids = set(tokenizer.all_special_ids)
    for i, row in enumerate(input_ids.tolist()):
        for j, tok in enumerate(row):
            if tok in special_ids:
                prob_matrix[i, j] = 0.0  # never mask [CLS], [SEP], [PAD]
    masked_indices = torch.bernoulli(prob_matrix).bool()
    labels[~masked_indices] = -100          # loss only on masked positions
    # 80%: replace with [MASK]
    mask_80 = torch.bernoulli(torch.full(labels.shape, 0.8)).bool() & masked_indices
    input_ids[mask_80] = tokenizer.mask_token_id
    # 10%: replace with random token (half of remaining 20%)
    rand_20  = (~mask_80) & masked_indices
    mask_10  = torch.bernoulli(torch.full(labels.shape, 0.5)).bool() & rand_20
    random_tokens = torch.randint(len(tokenizer), labels.shape, dtype=torch.long)
    input_ids[mask_10] = random_tokens[mask_10]
    # 10%: keep unchanged — the other half of rand_20, no action needed
    return input_ids, labels

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
text = "The quick brown fox jumps over the lazy dog and runs away from the farmer"
ids  = tokenizer(text, return_tensors="pt", max_length=64, truncation=True)["input_ids"]
masked_ids, labels = mlm_mask_tokens(ids.clone(), tokenizer)
print(f"Sequence: {ids.size(1)} tokens | Masked: {(labels != -100).sum().item()} | [MASK]: {(masked_ids == tokenizer.mask_token_id).sum().item()}")
```

## MLM Training Forward Pass

The MLM training loop applies the masking collator on the fly (dynamic masking) so that each epoch sees different masked positions for the same text — this acts as implicit data augmentation. The model's loss is the cross-entropy between the predicted logit distribution and the true token ID, summed only over positions where labels ≠ -100. HuggingFace's BertForMaskedLM handles this automatically when labels are passed: it calls CrossEntropyLoss with ignore_index=-100 internally. Typical hyperparameters: learning rate 1e-4, warmup 10k steps, batch size 256, AdamW with weight decay 0.01.

```python
import torch
from transformers import BertForMaskedLM, BertTokenizer

def train_mlm_step(model, batch, tokenizer, optimizer, device):
    """Single MLM training step: apply masking, forward pass, backprop."""
    input_ids  = batch["input_ids"].clone().to(device)
    attn_mask  = batch["attention_mask"].to(device)
    masked_ids, labels = mlm_mask_tokens(input_ids, tokenizer)
    labels = labels.to(device)
    outputs = model(
        input_ids=masked_ids,
        attention_mask=attn_mask,
        labels=labels,            # BertForMaskedLM ignores label=-100 in loss
    )
    loss     = outputs.loss       # cross-entropy over masked positions only
    n_masked = (labels != -100).sum().item()
    optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()
    return loss.item(), n_masked

device    = "cuda" if torch.cuda.is_available() else "cpu"
model     = BertForMaskedLM.from_pretrained("bert-base-uncased").to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4, weight_decay=0.01)
n_params  = sum(p.numel() for p in model.parameters()) / 1e6
print(f"BERT-base parameters: {n_params:.0f}M")
print("MLM loss is averaged only over ~15% masked positions, not all N tokens.")
```

## Span Masking — SpanBERT Style

Token-level masking (BERT) masks individual subword tokens independently, but span masking (SpanBERT, Joshi et al. 2020) masks contiguous spans of tokens drawn from a geometric distribution. Masking contiguous spans is harder because the model cannot use adjacent masked tokens as hints — it must rely on the full surrounding context. SpanBERT also introduces the Span Boundary Objective (SBO): predict each masked token using only the two boundary tokens on either side of the span, without seeing any tokens inside the span. Together, these changes produce significantly better performance on span-extraction tasks like SQuAD.

```python
import torch
import random
import math
from transformers import BertTokenizer

def span_mask_tokens(input_ids, tokenizer, noise_density=0.15, mean_span=3.0):
    """SpanBERT-style geometric span masking on a 1D token sequence."""
    special_ids = set(tokenizer.all_special_ids)
    seq = input_ids.tolist()
    n   = len(seq)
    target_n_masked = max(1, int(n * noise_density))
    masked_positions = set()
    while len(masked_positions) < target_n_masked:
        span_len = max(1, int(-mean_span * math.log(max(random.random(), 1e-10))))
        start    = random.randint(0, n - 1)
        for p in range(start, min(start + span_len, n)):
            if seq[p] not in special_ids:
                masked_positions.add(p)
    result = input_ids.clone()
    labels = input_ids.clone()
    for p in range(n):
        if p in masked_positions:
            result[p] = tokenizer.mask_token_id
        else:
            labels[p] = -100
    return result, labels

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
ids = tokenizer.encode("Span masking selects contiguous token spans for masking",
                        return_tensors="pt")[0]
result, labels = span_mask_tokens(ids, tokenizer)
print(f"Tokens: {len(ids)} | Masked: {(labels != -100).sum().item()} spans masked")
```

> **MLM Compute Efficiency vs CLM**: MLM learns only 15% of positions per forward pass vs 100% for CLM — this means MLM requires significantly more data or epochs to see each token as a target, making it less compute-efficient per token for pretraining. RoBERTa addressed this with dynamic masking and much larger data (160GB vs BERT's 16GB), not a change to the objective itself.

## BERT Fine-Tuning for Classification

MLM pretraining learns general-purpose representations; task-specific adaptation is done by fine-tuning. For classification, a linear head is added on top of the [CLS] token representation (the first token, which aggregates sequence-level information through bidirectional attention). The full model (encoder + head) is then trained end-to-end on labelled data with a much smaller learning rate (2e-5 to 5e-5). Freezing the embedding layer while fine-tuning all transformer layers reduces the number of trainable parameters slightly and often improves stability on small datasets.

```python
import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

class BertClassifier(nn.Module):
    """BERT for sequence classification using [CLS] token representation."""
    def __init__(self, model_name="bert-base-uncased", num_labels=2, freeze_emb=True):
        super().__init__()
        self.bert = BertModel.from_pretrained(model_name)
        if freeze_emb:
            for p in self.bert.embeddings.parameters():
                p.requires_grad_(False)
        hidden = self.bert.config.hidden_size   # 768 for BERT-base
        self.classifier = nn.Sequential(nn.Dropout(0.1), nn.Linear(hidden, num_labels))

    def forward(self, input_ids, attention_mask, token_type_ids=None):
        out      = self.bert(input_ids=input_ids, attention_mask=attention_mask,
                             token_type_ids=token_type_ids)
        cls_repr = out.last_hidden_state[:, 0, :]   # [CLS] token at position 0
        return self.classifier(cls_repr)

device = "cuda" if torch.cuda.is_available() else "cpu"
model  = BertClassifier(num_labels=2).to(device)
optimizer = torch.optim.AdamW(
    filter(lambda p: p.requires_grad, model.parameters()), lr=2e-5
)
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Trainable parameters: {trainable / 1e6:.1f}M (embeddings frozen)")
print("Fine-tune [CLS] → linear head; no causal mask — full bidirectional attention.")
```

## MLM Variants Compared

The original BERT paper spawned a family of encoder-only models that refined the masking strategy, removed or replaced the Next Sentence Prediction (NSP) auxiliary task, and scaled data and compute. RoBERTa (Liu et al. 2019) was the first major ablation: dropping NSP, dynamic masking, and training 10× longer on 10× more data improved BERT's GLUE score substantially without any architectural change. DeBERTa introduced disentangled attention — separate embeddings for token content and relative position — setting new SOTA on many benchmarks.

| Model | Masking Strategy | NSP | Masking Ratio | Key Innovation |
| --- | --- | --- | --- | --- |
| BERT | Token-level 80/10/10 | Yes | 15% | Bidirectional pretraining with MLM + NSP |
| RoBERTa | Dynamic token masking | No | 15% | More data, longer training, no NSP — strong baseline |
| DeBERTa | Token + position masking | No | 15% | Disentangled attention: separate content and position |
| SpanBERT | Contiguous span masking | No | 15% | SBO: predict spans using boundary token context only |
| ALBERT | Token-level (shared weights) | No (SOP) | 15% | Cross-layer weight sharing + sentence order prediction |
| XLNet | Permutation language modeling | No | All positions | AR over random permutations — bidirectional without [MASK] |

## Dynamic and Whole-Word Masking

Static masking (original BERT) applies a fixed masking pattern to each training example once during preprocessing — the model sees the same masked version of each sentence every epoch. Dynamic masking (RoBERTa) re-applies the masking function at each training step, so the model sees different masked positions across epochs for the same text. Whole-word masking ensures that if a word is tokenised into multiple subword pieces, all pieces are masked or unmasked together — preventing the model from trivially predicting a masked subword from an adjacent visible subword of the same word.

- Static masking (BERT): masking applied once at data preprocessing — each epoch sees the same masks.
- Dynamic masking (RoBERTa): masking resampled at each step — effective 10× more variation per training example.
- Whole-word masking: mask all subwords of a word together — prevents subword leakage (e.g. '##ing' visible when 'run' is masked).
- Span masking (SpanBERT): mask contiguous spans from geometric distribution with mean 3.8 tokens.
- Entity/phrase masking (ERNIE, Baidu): always mask complete named entities or phrases — better entity-level representations.

## NSP and Its Removal in RoBERTa

BERT was pretrained with a second objective: Next Sentence Prediction (NSP). Given two sentence segments A and B, the model must predict whether B naturally follows A (50% positive, 50% negative where B is sampled from a random document). The idea was to learn inter-sentence coherence. However, RoBERTa's ablation studies showed NSP slightly hurts performance: the task is too easy (random negatives are distinguishable by topic alone), and it forces artificially short training documents. Removing NSP and training on full documents improved every downstream benchmark. Later models (ALBERT) replaced NSP with Sentence Order Prediction (SOP), which is harder — the negative is the same two sentences in reverse order.

## Bidirectional Attention Architecture

The key architectural difference between BERT (encoder) and GPT (decoder) is the attention mask. BERT uses full bidirectional attention: no mask is applied, so every token attends to every other token including future tokens. This is implemented identically to standard multi-head self-attention but without the lower-triangular mask. The consequence is that BERT cannot generate text autoregressively — computing P(xₜ | x<ₜ) is undefined under bidirectional attention. Instead, BERT's strength is producing a single contextualised representation for each input token, which serves as a feature for classification, named entity recognition, question answering, and other understanding tasks.

