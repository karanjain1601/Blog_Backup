---
title: "Speculative Decoding"
slug: "speculative-decoding"
description: "Using a small draft model to propose multiple tokens that the large target model verifies in parallel, reducing wall-clock generation time without changing output distribution."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BlY3VsYXRpdmUgZGVjb2RpbmcgKENoZW4gZXQgYWwuLCAyMDIzOyBMZXZpYXRoYW4gZXQgYWwuLCAyMDIzKSBpcyBhIGxvc3NsZXNzIGluZmVyZW5jZSBhY2NlbGVyYXRpb24gdGVjaG5pcXVlIHRoYXQgZGVjb3VwbGVzIHRva2VuIHByb3Bvc2FsIGZyb20gdG9rZW4gdmVyaWZpY2F0aW9uLiBBIHNtYWxsLCBmYXN0IGRyYWZ0IG1vZGVsIGF1dG9yZWdyZXNzaXZlbHkgZ2VuZXJhdGVzIGsgY2FuZGlkYXRlIHRva2VucyBpbiBzZXF1ZW5jZS4gVGhlIGxhcmdlIHRhcmdldCBtb2RlbCB0aGVuIGV2YWx1YXRlcyBhbGwgaysxIHBvc2l0aW9ucyBpbiBhIHNpbmdsZSBmb3J3YXJkIHBhc3Mg4oCUIHByb2R1Y2luZyBpdHMgb3duIHByb2JhYmlsaXR5IGRpc3RyaWJ1dGlvbnMgYXQgZWFjaCBwb3NpdGlvbi4gQSByZWplY3Rpb24tc2FtcGxpbmcgcHJvY2VkdXJlIGFjY2VwdHMgb3IgcmVqZWN0cyBlYWNoIGRyYWZ0IHRva2VuIHdoaWxlIHByb3ZhYmx5IHByZXNlcnZpbmcgdGhlIHRhcmdldCBtb2RlbFx1MDAyN3Mgb3V0cHV0IGRpc3RyaWJ1dGlvbi4gVGhlIG5ldCBlZmZlY3Q6IHRoZSB0YXJnZXQgbW9kZWwgcHJvY2Vzc2VzIG11bHRpcGxlIHRva2VucyBwZXIgZm9yd2FyZCBwYXNzIGluc3RlYWQgb2Ygb25lLCByZWR1Y2luZyB0aGUgdG90YWwgbnVtYmVyIG9mIGV4cGVuc2l2ZSB0YXJnZXQgZm9yd2FyZCBwYXNzZXMgbmVlZGVkIHRvIGdlbmVyYXRlIGEgc2VxdWVuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vZGVybiBsYXJnZSBsYW5ndWFnZSBtb2RlbCBpbmZlcmVuY2UgaXMgbWVtb3J5LWJhbmR3aWR0aCBib3VuZCwgbm90IGNvbXB1dGUgYm91bmQuIEF0IGJhdGNoIHNpemUgMSwgdGhlIEdQVSBzcGVuZHMgbW9zdCBvZiBpdHMgdGltZSBsb2FkaW5nIDcw4oCTMTQwIEdCIG9mIG1vZGVsIHdlaWdodHMgZnJvbSBIQk0gdG8gU1JBTSBmb3IgZWFjaCBmb3J3YXJkIHBhc3Mg4oCUIHRoZSBhY3R1YWwgbWF0cml4IG11bHRpcGxpY2F0aW9uIGlzIHNlY29uZGFyeS4gU3BlY3VsYXRpdmUgZGVjb2RpbmcgZXhwbG9pdHMgdGhpcyBhc3ltbWV0cnk6IHNpbmNlIHRoZSB0YXJnZXQgbW9kZWxcdTAwMjdzIGZvcndhcmQgcGFzcyBpcyBsYXRlbmN5LWRvbWluYXRlZCBieSBtZW1vcnkgdHJhbnNmZXJzIHJhdGhlciB0aGFuIEZMT1BzLCB2ZXJpZnlpbmcgayB0b2tlbnMgaW4gb25lIHBhc3MgdGFrZXMgb25seSBtYXJnaW5hbGx5IG1vcmUgdGltZSB0aGFuIHZlcmlmeWluZyAxLiBNZWFud2hpbGUsIHRoZSBkcmFmdCBtb2RlbCBpcyAxMOKAkzEwMHggc21hbGxlciBhbmQgY2FuIHByb2R1Y2UgayBwcm9wb3NhbHMgaW4gYSBmcmFjdGlvbiBvZiB0aGUgdGltZSBhIHNpbmdsZSB0YXJnZXQgZm9yd2FyZCBwYXNzIHRha2VzLiBJZiB0aGUgZHJhZnQgbW9kZWxcdTAwMjdzIHByb3Bvc2FscyBhcmUgYWNjZXB0ZWQgYXQgcmF0ZSBhbHBoYSwgdGhlIGV4cGVjdGVkIHRva2VucyBwcm9kdWNlZCBwZXIgdGFyZ2V0IGZvcndhcmQgcGFzcyBpcyAoMSAtIGFscGhhXihrKzEpKSAvICgxIC0gYWxwaGEpLCBnaXZpbmcgYSB0aGVvcmV0aWNhbCBzcGVlZHVwIG9mIHRoYXQgcXVhbnRpdHkgZGl2aWRlZCBieSAxIChncmVlZHkgYmFzZWxpbmUpLiBBdCBhbHBoYT0wLjggYW5kIGs9NSwgdGhpcyBpcyByb3VnaGx5IDMuNSB0b2tlbnMgcGVyIHRhcmdldCBwYXNzIOKAlCBhIDMuNXggdGhyb3VnaHB1dCBnYWluLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRyYWZ0LVZlcmlmeSBNZWNoYW5pc20ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBkcmFmdC12ZXJpZnkgbG9vcCBwcm9jZWVkcyBhcyBmb2xsb3dzLiBHaXZlbiBpbnB1dCBjb250ZXh0IHhfezE6dH0sIHRoZSBkcmFmdCBtb2RlbCBnZW5lcmF0ZXMgayB0b2tlbnMgYXV0b3JlZ3Jlc3NpdmVseTogZm9yIGVhY2ggc3RlcCBpIGluIDEuLmssIGl0IHNhbXBsZXMgeF97dCtpfSB+IHEoLiB8IHhfezE6dCtpLTF9KSB3aGVyZSBxIGlzIHRoZSBkcmFmdCBtb2RlbFx1MDAyN3MgZGlzdHJpYnV0aW9uLiBUaGlzIHByb2R1Y2VzIGEgc2VxdWVuY2Ugb2YgayBkcmFmdCB0b2tlbnMgYW5kIHRoZWlyIGFzc29jaWF0ZWQgZHJhZnQgcHJvYmFiaWxpdGllcyBxX2kgPSBxKHhfe3QraX0gfCB4X3sxOnQraS0xfSkuIE5leHQsIHRoZSB0YXJnZXQgbW9kZWwgaXMgY2FsbGVkIG9uY2Ugd2l0aCB0aGUgZnVsbCBjYW5kaWRhdGUgc2VxdWVuY2UgeF97MTp0K2t9IGFuZCByZXR1cm5zIGxvZ2l0cyBmb3IgYWxsIHQrayBwb3NpdGlvbnMgc2ltdWx0YW5lb3VzbHkuIFRoZSB0YXJnZXQgcHJvYmFiaWxpdGllcyBhdCBlYWNoIGRyYWZ0IHBvc2l0aW9uIGFyZSBwX2kgPSBwKHhfe3QraX0gfCB4X3sxOnQraS0xfSkuIFRoZSByZWplY3Rpb24gc2FtcGxpbmcgbG9vcCB0aGVuIGl0ZXJhdGVzIGkgZnJvbSAxIHRvIGs6IGlmIHBfaSAvIHFfaSBcdTAwM2U9IDEsIHRva2VuIGkgaXMgYWx3YXlzIGFjY2VwdGVkOyBvdGhlcndpc2UgdG9rZW4gaSBpcyBhY2NlcHRlZCB3aXRoIHByb2JhYmlsaXR5IHBfaSAvIHFfaSBhbmQgcmVqZWN0ZWQgd2l0aCBwcm9iYWJpbGl0eSAxIC0gcF9pIC8gcV9pLiBPbiByZWplY3Rpb24sIGEgY29ycmVjdGVkIHRva2VuIGlzIHNhbXBsZWQgZnJvbSB0aGUgcmVzaWR1YWwgZGlzdHJpYnV0aW9uIG1heCgwLCBwX2kgLSBxX2kpIC8gWi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsRm9yQ2F1c2FsTE1cbmZyb20gdHlwaW5nIGltcG9ydCBUdXBsZSwgTGlzdFxuXG5kZWYgc3BlY3VsYXRpdmVfZGVjb2RlKFxuICAgIHRhcmdldF9tb2RlbCwgZHJhZnRfbW9kZWwsIGlucHV0X2lkczogdG9yY2guVGVuc29yLFxuICAgIGs6IGludCA9IDUsIHRlbXBlcmF0dXJlOiBmbG9hdCA9IDEuMFxuKSAtXHUwMDNlIFR1cGxlW3RvcmNoLlRlbnNvciwgZmxvYXRdOlxuICAgIFwiXCJcIkRyYWZ0IHByb3Bvc2VzIGsgdG9rZW5zOyB0YXJnZXQgdmVyaWZpZXMgYWxsIGluIG9uZSBmb3J3YXJkIHBhc3MuXCJcIlwiXG4gICAgZHJhZnRfaW5wdXQgPSBpbnB1dF9pZHMuY2xvbmUoKVxuICAgIGRyYWZ0X3Rva2VuczogTGlzdFt0b3JjaC5UZW5zb3JdID0gW11cbiAgICBkcmFmdF9wcm9iczogTGlzdFtmbG9hdF0gPSBbXVxuICAgIGZvciBfIGluIHJhbmdlKGspOlxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIGxvZ2l0cyA9IGRyYWZ0X21vZGVsKGRyYWZ0X2lucHV0KS5sb2dpdHNbOiwgLTEsIDpdIC8gdGVtcGVyYXR1cmVcbiAgICAgICAgICAgIHByb2JzID0gRi5zb2Z0bWF4KGxvZ2l0cywgZGltPS0xKVxuICAgICAgICAgICAgdG9rID0gdG9yY2gubXVsdGlub21pYWwocHJvYnMsIDEpXG4gICAgICAgICAgICBkcmFmdF90b2tlbnMuYXBwZW5kKHRvaylcbiAgICAgICAgICAgIGRyYWZ0X3Byb2JzLmFwcGVuZChwcm9ic1swLCB0b2suaXRlbSgpXS5pdGVtKCkpXG4gICAgICAgICAgICBkcmFmdF9pbnB1dCA9IHRvcmNoLmNhdChbZHJhZnRfaW5wdXQsIHRva10sIGRpbT0tMSlcbiAgICBjYW5kaWRhdGVfaWRzID0gdG9yY2guY2F0KFtpbnB1dF9pZHNdICsgZHJhZnRfdG9rZW5zLCBkaW09LTEpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHRhcmdldF9sb2dpdHMgPSB0YXJnZXRfbW9kZWwoY2FuZGlkYXRlX2lkcykubG9naXRzXG4gICAgYWNjZXB0ZWQ6IExpc3RbdG9yY2guVGVuc29yXSA9IFtdXG4gICAgbiA9IGxlbihpbnB1dF9pZHNbMF0pXG4gICAgZm9yIGksICh0b2ssIHFfaSkgaW4gZW51bWVyYXRlKHppcChkcmFmdF90b2tlbnMsIGRyYWZ0X3Byb2JzKSk6XG4gICAgICAgIHRfcHJvYnMgPSBGLnNvZnRtYXgodGFyZ2V0X2xvZ2l0c1swLCBuIC0gMSArIGldIC8gdGVtcGVyYXR1cmUsIGRpbT0tMSlcbiAgICAgICAgYWNjZXB0X3Byb2IgPSBtaW4oMS4wLCB0X3Byb2JzW3Rvay5pdGVtKCldLml0ZW0oKSAvIChxX2kgKyAxZS05KSlcbiAgICAgICAgaWYgdG9yY2gucmFuZCgxKS5pdGVtKCkgXHUwMDNjIGFjY2VwdF9wcm9iOlxuICAgICAgICAgICAgYWNjZXB0ZWQuYXBwZW5kKHRvaylcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgICMgU2FtcGxlIGZyb20gcmVzaWR1YWwgKGNvcnJlY3RlZCkgZGlzdHJpYnV0aW9uXG4gICAgICAgICAgICBxX2Rpc3QgPSBGLnNvZnRtYXgodGFyZ2V0X2xvZ2l0c1swLCBuIC0gMSArIGldIC8gdGVtcGVyYXR1cmUsIGRpbT0tMSlcbiAgICAgICAgICAgIGFkaiA9ICh0X3Byb2JzIC0gcV9kaXN0ICogcV9pKS5jbGFtcChtaW49MClcbiAgICAgICAgICAgIGZhbGxiYWNrID0gdG9yY2gubXVsdGlub21pYWwoYWRqIC8gKGFkai5zdW0oKSArIDFlLTkpLCAxKS51bnNxdWVlemUoMClcbiAgICAgICAgICAgIGFjY2VwdGVkLmFwcGVuZChmYWxsYmFjaylcbiAgICAgICAgICAgIGJyZWFrICAjIHN0b3AgYWNjZXB0aW5nIGFmdGVyIGZpcnN0IHJlamVjdGlvblxuICAgIHJldHVybiB0b3JjaC5jYXQoW2lucHV0X2lkc10gKyBhY2NlcHRlZCwgZGltPS0xKSwgbGVuKGFjY2VwdGVkKSAvIGsifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBY2NlcHRhbmNlIENyaXRlcmlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGFjY2VwdGFuY2UgcHJvYmFiaWxpdHkgZm9yIGRyYWZ0IHRva2VuIHhfe3QraX0gaXMgbWluKDEsIHAoeF97dCtpfSB8IGNvbnRleHQpIC8gcSh4X3t0K2l9IHwgY29udGV4dCkpLiBUaGlzIGlzIHRoZSBzYW1lIGNyaXRlcmlvbiB1c2VkIGluIGltcG9ydGFuY2Ugc2FtcGxpbmcgYW5kIHRoZSBNZXRyb3BvbGlzLUhhc3RpbmdzIGFsZ29yaXRobS4gV2hlbiB0aGUgZHJhZnQgbW9kZWwgaXMgd2VsbC1hbGlnbmVkIHdpdGggdGhlIHRhcmdldCAoaS5lLiwgcSDiiYggcCksIGFjY2VwdGFuY2UgcmF0ZSBhbHBoYSBhcHByb2FjaGVzIDEuIFdoZW4gdGhleSBkaXZlcmdlIChlLmcuLCBkcmFmdCBwcmVkaWN0cyBhIGRpZmZlcmVudCB0b2tlbiBkaXN0cmlidXRpb24gZm9yIHRlY2huaWNhbCBjb250ZW50KSwgYWxwaGEgZHJvcHMuIFRoZSBjb3JyZWN0ZWQgZGlzdHJpYnV0aW9uIG9uIHJlamVjdGlvbiBpcyB0aGUgbm9ybWFsaXplZCBwb3NpdGl2ZSBwYXJ0IG9mIChwIC0gcSk6IHdlIHN1YnRyYWN0IHRoZSBkcmFmdFx1MDAyN3MgY29udHJpYnV0aW9uIGFuZCByZS1ub3JtYWxpemUuIFRoaXMgZW5zdXJlcyB0aGF0IHRoZSBtYXJnaW5hbCBkaXN0cmlidXRpb24gb3ZlciBhY2NlcHRlZCB0b2tlbnMgZXhhY3RseSBtYXRjaGVzIHAg4oCUIHRoZSBndWFyYW50ZWUgdGhhdCBzcGVjdWxhdGl2ZSBkZWNvZGluZyBpcyBsb3NzbGVzcy4gVW5saWtlIHF1YW50aXphdGlvbiBvciBrbm93bGVkZ2UgZGlzdGlsbGF0aW9uLCB0aGVyZSBpcyB6ZXJvIGFjY3VyYWN5IHRyYWRlb2ZmOiB0aGUgb3V0cHV0IGRpc3RyaWJ1dGlvbiBpcyBpZGVudGljYWwgdG8gZ3JlZWR5IG9yIHNhbXBsZWQgZGVjb2RpbmcgZnJvbSB0aGUgdGFyZ2V0IGFsb25lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwZWN1bGF0aXZlIFNhbXBsaW5nIE1hdGgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxldCBwKHh8YykgYmUgdGhlIHRhcmdldCBkaXN0cmlidXRpb24gYW5kIHEoeHxjKSBiZSB0aGUgZHJhZnQgZGlzdHJpYnV0aW9uIG92ZXIgdGhlIG5leHQgdG9rZW4gZ2l2ZW4gY29udGV4dCBjLiBEZWZpbmUgdGhlIGFjY2VwdGFuY2UgcHJvYmFiaWxpdHkgYSh4KSA9IG1pbigxLCBwKHh8YykgLyBxKHh8YykpLiBUaGUgZXhwZWN0ZWQgbnVtYmVyIG9mIHRva2VucyBhY2NlcHRlZCBwZXIgc3BlY3VsYXRpdmUgc3RlcCBpcyBFW2FjY2VwdGVkXSA9IHN1bV94IHEoeCkgKiBhKHgpID0gc3VtX3ggbWluKHEoeCksIHAoeCkpID0gMSAtIFRWKHAsIHEpIHdoZXJlIFRWIGlzIHRvdGFsIHZhcmlhdGlvbiBkaXN0YW5jZS4gV2hlbiBwID0gcSBleGFjdGx5IChwZXJmZWN0IGRyYWZ0KSwgYWxsIGsgdG9rZW5zIGFyZSBhbHdheXMgYWNjZXB0ZWQuIFRoZSBleHBlY3RlZCBzcGVlZHVwIHJlbGF0aXZlIHRvIGdyZWVkeSBkZWNvZGluZyAoMSB0YXJnZXQgY2FsbCBwZXIgdG9rZW4pIGlzOiBzcGVlZHVwIOKJiCAoMSAtIGFscGhhXihrKzEpKSAvICgoMSAtIGFscGhhKSAqIENfZHJhZnQpIHdoZXJlIGFscGhhID0gRVthKHgpXSBhbmQgQ19kcmFmdCBpcyB0aGUgcmVsYXRpdmUgY29zdCBvZiBvbmUgZHJhZnQgZm9yd2FyZCBwYXNzIGFzIGEgZnJhY3Rpb24gb2YgdGhlIHRhcmdldCBjb3N0LiBGb3IgYSA2OE0gZHJhZnQgYWdhaW5zdCBhIDdCIHRhcmdldCwgQ19kcmFmdCDiiYggMC4wMeKAkzAuMDUsIG1ha2luZyB0aGUgZHJhZnQgb3ZlcmhlYWQgbmVnbGlnaWJsZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdGltZVxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvVG9rZW5pemVyXG5cbmRlZiBiZW5jaG1hcmtfc3BlY3VsYXRpdmVfZGVjb2RpbmcoXG4gICAgdGFyZ2V0X25hbWU6IHN0ciA9IFwibWV0YS1sbGFtYS9MbGFtYS0yLTdiLWhmXCIsXG4gICAgZHJhZnRfbmFtZTogc3RyID0gXCJKYWNrRnJhbS9sbGFtYS02OG1cIixcbiAgICBuX3Byb21wdHM6IGludCA9IDUwLFxuICAgIG1heF9uZXdfdG9rZW5zOiBpbnQgPSAxMjgsXG4gICAgazogaW50ID0gNVxuKSAtXHUwMDNlIGRpY3Q6XG4gICAgXCJcIlwiTWVhc3VyZSBhY2NlcHRhbmNlIHJhdGUgYW5kIHdhbGwtY2xvY2sgc3BlZWR1cCB2cyBncmVlZHkgYmFzZWxpbmUuXCJcIlwiXG4gICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQodGFyZ2V0X25hbWUpXG4gICAgdGFyZ2V0ID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKFxuICAgICAgICB0YXJnZXRfbmFtZSwgdG9yY2hfZHR5cGU9dG9yY2guZmxvYXQxNiwgZGV2aWNlX21hcD1cImF1dG9cIilcbiAgICBkcmFmdCA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcbiAgICAgICAgZHJhZnRfbmFtZSwgdG9yY2hfZHR5cGU9dG9yY2guZmxvYXQxNiwgZGV2aWNlX21hcD1cImF1dG9cIilcbiAgICBwcm9tcHRzID0gW1wiRGVzY3JpYmUgdGhlIGFyY2hpdGVjdHVyZSBvZiBhIHRyYW5zZm9ybWVyIG1vZGVsIGluIGRldGFpbC5cIl0gKiBuX3Byb21wdHNcbiAgICBpbnB1dHMgPSB0b2tlbml6ZXIocHJvbXB0c1swXSwgcmV0dXJuX3RlbnNvcnM9XCJwdFwiKS50byhcImN1ZGFcIilcbiAgICAjIEdyZWVkeSBiYXNlbGluZVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGZvciBfIGluIHJhbmdlKG5fcHJvbXB0cyk6XG4gICAgICAgIHRhcmdldC5nZW5lcmF0ZSgqKmlucHV0cywgbWF4X25ld190b2tlbnM9bWF4X25ld190b2tlbnMsIGRvX3NhbXBsZT1GYWxzZSlcbiAgICBncmVlZHlfdGltZSA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgICMgU3BlY3VsYXRpdmUgZGVjb2RpbmdcbiAgICBhY2NlcHRhbmNlX3JhdGVzID0gW11cbiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICBmb3IgXyBpbiByYW5nZShuX3Byb21wdHMpOlxuICAgICAgICBfLCBhbHBoYSA9IHNwZWN1bGF0aXZlX2RlY29kZSh0YXJnZXQsIGRyYWZ0LCBpbnB1dHMuaW5wdXRfaWRzLCBrPWspXG4gICAgICAgIGFjY2VwdGFuY2VfcmF0ZXMuYXBwZW5kKGFscGhhKVxuICAgIHNwZWNfdGltZSA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgIHNwZWVkdXAgPSBncmVlZHlfdGltZSAvIHNwZWNfdGltZVxuICAgIG1lYW5fYWxwaGEgPSBzdW0oYWNjZXB0YW5jZV9yYXRlcykgLyBsZW4oYWNjZXB0YW5jZV9yYXRlcylcbiAgICBwcmludChmXCJHcmVlZHk6ICAgICAge2dyZWVkeV90aW1lOi4yZn1zIHRvdGFsXCIpXG4gICAgcHJpbnQoZlwiU3BlY3VsYXRpdmU6IHtzcGVjX3RpbWU6LjJmfXMgdG90YWwgIChzcGVlZHVwPXtzcGVlZHVwOi4yZn14KVwiKVxuICAgIHByaW50KGZcIk1lYW4gYWNjZXB0YW5jZSByYXRlIGFscGhhOiB7bWVhbl9hbHBoYTouM2Z9XCIpXG4gICAgcHJpbnQoZlwiRXhwZWN0ZWQgc3BlZWR1cCBmcm9tIGZvcm11bGE6IHsoMSAtIG1lYW5fYWxwaGEqKihrKzEpKSAvICgxIC0gbWVhbl9hbHBoYSArIDFlLTkpOi4yZn14XCIpXG4gICAgcmV0dXJuIHtcInNwZWVkdXBcIjogc3BlZWR1cCwgXCJhbHBoYVwiOiBtZWFuX2FscGhhfSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNob29zaW5nIHRoZSBEcmFmdCBNb2RlbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRyYWZ0IG1vZGVsIG11c3Qgc2F0aXNmeSB0d28gY29tcGV0aW5nIHJlcXVpcmVtZW50czogaXQgbXVzdCBiZSBmYXN0IGVub3VnaCB0aGF0IGl0cyBrIGZvcndhcmQgcGFzc2VzIGNvc3QgbGVzcyB0aGFuIHRoZSB0YXJnZXQgcGFzcyBpdCByZXBsYWNlcywgYW5kIGl0IG11c3QgYmUgYWNjdXJhdGUgZW5vdWdoIHRoYXQgYWNjZXB0YW5jZSByYXRlIGFscGhhIHN0YXlzIGhpZ2guIFRoZSBrZXkgcHJhY3RpY2FsIGNvbnN0cmFpbnQgaXMgdGhhdCB0aGUgZHJhZnQgYW5kIHRhcmdldCBtdXN0IHNoYXJlIHRoZSBzYW1lIHRva2VuaXplciB2b2NhYnVsYXJ5IOKAlCB0aGUgdG9rZW5zIHByb3Bvc2VkIGJ5IHRoZSBkcmFmdCBtdXN0IGJlIHZhbGlkIHRva2VucyBmcm9tIHRoZSB0YXJnZXRcdTAwMjdzIHZvY2FidWxhcnkgZm9yIHRoZSByZWplY3Rpb24gc2FtcGxpbmcgbWF0aCB0byB3b3JrLiBUaGUgYmVzdCBkcmFmdCBtb2RlbHMgYXJlIHNtYWxsZXIgbWVtYmVycyBvZiB0aGUgc2FtZSBtb2RlbCBmYW1pbHkgdHJhaW5lZCB3aXRoIHRoZSBzYW1lIGRhdGEgZGlzdHJpYnV0aW9uOiBmb3IgTExhTUEtMi03MEIsIHVzZSBMTGFNQS0yLTdCIG9yIFRpbnlMTGFNQS0xLjFCIGFzIHRoZSBkcmFmdC4gRHJhZnQgbW9kZWxzIGZyb20gdW5yZWxhdGVkIGZhbWlsaWVzIChlLmcuLCBHUFQtMiBhcyBkcmFmdCBmb3IgTExhTUEpIHRlbmQgdG8gaGF2ZSBwb29yIGFsaWdubWVudCBhbmQgbG93IGFscGhhLiBTZWxmLWRyYWZ0aW5nIOKAlCB1c2luZyBlYXJseSBleGl0IGxheWVycyBvZiB0aGUgdGFyZ2V0IG1vZGVsIGl0c2VsZiDigJQgYXZvaWRzIHRoaXMgcHJvYmxlbSBieSBzaGFyaW5nIHRoZSBmdWxsIGVtYmVkZGluZyBzcGFjZSwgYnV0IHJlcXVpcmVzIG1vZGVsIHN1cmdlcnkuIE1lZHVzYSBhZGRzIG11bHRpcGxlIHByZWRpY3Rpb24gaGVhZHMgdG8gdGhlIHRhcmdldCBtb2RlbCBpdHNlbGYsIHRyYWluZWQgdG8gcHJlZGljdCBwb3NpdGlvbnMgMiwgMywgLi4uIGsgYWhlYWQgc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRyYWZ0IE1vZGVsIiwiQWNjZXB0YW5jZSBSYXRlIChhbHBoYSkiLCJFZmZlY3RpdmUgU3BlZWR1cCIsIkV4dHJhIE1lbW9yeSAoR0IpIiwiTGF0ZW5jeSBSZWR1Y3Rpb24iXSwicm93cyI6W1siTExhTUEtNjhNIiwiMC42NeKAkzAuNzAiLCIxLjjigJMyLjJ4IiwiKzAuMSBHQiIsIjQw4oCTNTAlIl0sWyJMTGFNQS0xNjBNIiwiMC43MOKAkzAuNzUiLCIyLjDigJMyLjV4IiwiKzAuMyBHQiIsIjQ14oCTNTUlIl0sWyJMTGFNQS0xQiIsIjAuNzjigJMwLjgzIiwiMi414oCTMy4weCIsIisyIEdCIiwiNTXigJM2NSUiXSxbIkxMYU1BLTNCIiwiMC44MuKAkzAuODciLCIyLjjigJMzLjR4IiwiKzYgR0IiLCI2MOKAkzcwJSJdLFsiU2VsZi1kcmFmdCAoTWVkdXNhKSIsIjAuNzXigJMwLjg4IiwiMi4y4oCTMy41eCIsIiswLjA1IEdCIChoZWFkcyBvbmx5KSIsIjU14oCTNzAlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTZWxmLVNwZWN1bGF0aXZlIGFuZCBNZWR1c2EgVmFyaWFudHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1lZHVzYSAoQ2FpIGV0IGFsLiwgMjAyNCkgYXR0YWNoZXMgayBhZGRpdGlvbmFsIExNIGhlYWRzIHRvIHRoZSBmaW5hbCBoaWRkZW4gc3RhdGUgb2YgdGhlIHRhcmdldCBtb2RlbC4gRWFjaCBNZWR1c2EgaGVhZCBpIHByZWRpY3RzIHRoZSB0b2tlbiBhdCBwb3NpdGlvbiB0K2krMSBnaXZlbiB0aGUgY3VycmVudCBoaWRkZW4gc3RhdGUg4oCUIGFsbCBoZWFkcyBydW4gaW4gcGFyYWxsZWwgZHVyaW5nIG9uZSB0YXJnZXQgZm9yd2FyZCBwYXNzLiBBIHRyZWUtc3RydWN0dXJlZCB2ZXJpZmljYXRpb24gdGhlbiBhY2NlcHRzIGNvbnNpc3RlbnQgY2FuZGlkYXRlIHBhdGhzLiBVbmxpa2Ugc3RhbmRhcmQgc3BlY3VsYXRpdmUgZGVjb2RpbmcsIE1lZHVzYSByZXF1aXJlcyBubyBzZXBhcmF0ZSBkcmFmdCBtb2RlbCBhbmQgYWRkcyBvbmx5IGEgc21hbGwgZnJhY3Rpb24gb2YgcGFyYW1ldGVycyAodGhlIGV4dHJhIGhlYWRzKS4gVGhlIHRyYWRlb2ZmIGlzIHRoYXQgTWVkdXNhIGhlYWRzIG11c3QgYmUgdHJhaW5lZCwgd2hlcmVhcyBzdGFuZGFyZCBzcGVjdWxhdGl2ZSBkZWNvZGluZyB3b3JrcyBvdXQtb2YtdGhlLWJveCB3aXRoIGFueSBjb21wYXRpYmxlIGRyYWZ0IG1vZGVsLiBFQUdMRSAoTGkgZXQgYWwuLCAyMDI0KSBpcyBhIGZ1cnRoZXIgcmVmaW5lbWVudCB3aGVyZSB0aGUgZHJhZnQgbW9kZWwgaXMgYW4gYXV0by1yZWdyZXNzaXZlIG1vZGVsIHRoYXQgb3BlcmF0ZXMgb24gdGFyZ2V0IGhpZGRlbiBzdGF0ZXMgcmF0aGVyIHRoYW4gcmF3IHRva2VucywgYWNoaWV2aW5nIGFjY2VwdGFuY2UgcmF0ZXMgb2YgMC44NeKAkzAuOTAgYnkgZGlyZWN0bHkgbW9kZWxpbmcgdGhlIHRhcmdldFx1MDAyN3MgcmVwcmVzZW50YXRpb24gc3BhY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRpbWVcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplclxuXG5kZWYgaGZfYXNzaXN0ZWRfZ2VuZXJhdGlvbl9iZW5jaG1hcmsoXG4gICAgdGFyZ2V0X25hbWU6IHN0ciA9IFwibWV0YS1sbGFtYS9MbGFtYS0yLTdiLWhmXCIsXG4gICAgZHJhZnRfbmFtZTogc3RyID0gXCJKYWNrRnJhbS9sbGFtYS02OG1cIixcbiAgICBtYXhfbmV3X3Rva2VuczogaW50ID0gMjAwXG4pIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiVXNlIEh1Z2dpbmdGYWNlIGJ1aWx0LWluIGFzc2lzdGVkIGdlbmVyYXRpb24gKHNwZWN1bGF0aXZlIGRlY29kaW5nKS5cIlwiXCJcbiAgICB0b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZCh0YXJnZXRfbmFtZSlcbiAgICB0YXJnZXQgPSBBdXRvTW9kZWxGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQoXG4gICAgICAgIHRhcmdldF9uYW1lLCB0b3JjaF9kdHlwZT10b3JjaC5mbG9hdDE2LCBkZXZpY2VfbWFwPVwiYXV0b1wiKVxuICAgIGRyYWZ0ID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKFxuICAgICAgICBkcmFmdF9uYW1lLCB0b3JjaF9kdHlwZT10b3JjaC5mbG9hdDE2LCBkZXZpY2VfbWFwPVwiYXV0b1wiKVxuICAgIHByb21wdCA9IFwiVGhlIGZ1bmRhbWVudGFsIHRoZW9yZW0gb2YgY2FsY3VsdXMgc3RhdGVzIHRoYXRcIlxuICAgIGlucHV0cyA9IHRva2VuaXplcihwcm9tcHQsIHJldHVybl90ZW5zb3JzPVwicHRcIikudG8oXCJjdWRhXCIpXG4gICAgIyBHcmVlZHkgYmFzZWxpbmVcbiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICBvdXRfZ3JlZWR5ID0gdGFyZ2V0LmdlbmVyYXRlKCoqaW5wdXRzLCBtYXhfbmV3X3Rva2Vucz1tYXhfbmV3X3Rva2VucywgZG9fc2FtcGxlPUZhbHNlKVxuICAgIHRfYmFzZSA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgICMgQXNzaXN0ZWQgZ2VuZXJhdGlvbjogSHVnZ2luZ0ZhY2UgcnVucyBzcGVjdWxhdGl2ZSBkZWNvZGluZyBpbnRlcm5hbGx5XG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgb3V0X3NwZWMgPSB0YXJnZXQuZ2VuZXJhdGUoKippbnB1dHMsIG1heF9uZXdfdG9rZW5zPW1heF9uZXdfdG9rZW5zLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb19zYW1wbGU9RmFsc2UsIGFzc2lzdGFudF9tb2RlbD1kcmFmdClcbiAgICB0X3NwZWMgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gdDBcbiAgICBzcGVlZHVwID0gdF9iYXNlIC8gdF9zcGVjXG4gICAgcHJpbnQoZlwiR3JlZWR5OiAgICB7dF9iYXNlOi4yZn1zICAgQXNzaXN0ZWQ6IHt0X3NwZWM6LjJmfXMgICBTcGVlZHVwOiB7c3BlZWR1cDouMmZ9eFwiKVxuICAgICMgVmVyaWZ5IGlkZW50aWNhbCBvdXRwdXRzIChzcGVjdWxhdGl2ZSBkZWNvZGluZyBpcyBsb3NzbGVzcylcbiAgICBhc3NlcnQgb3V0X2dyZWVkeVswXS50b2xpc3QoKSA9PSBvdXRfc3BlY1swXS50b2xpc3QoKSwgXCJPdXRwdXQgbWlzbWF0Y2gg4oCUIGJ1ZyFcIlxuICAgIHByaW50KFwiT3V0cHV0IGRpc3RyaWJ1dGlvbnMgbWF0Y2g6IHZlcmlmaWVkIGxvc3NsZXNzLlwiKVxuICAgIHJldHVybiBzcGVlZHVwIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhyb3VnaHB1dCBHYWlucyBpbiBQcmFjdGljZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVhbC13b3JsZCBzcGVlZHVwcyBkZXBlbmQgaGVhdmlseSBvbiB0YXNrIHR5cGUgYW5kIG91dHB1dCBsZW5ndGguIFNwZWN1bGF0aXZlIGRlY29kaW5nIHByb3ZpZGVzIHRoZSBsYXJnZXN0IGdhaW5zIG9uIHRhc2tzIHdoZXJlIHRoZSBvdXRwdXQgaXMgcHJlZGljdGFibGUgYW5kIHRoZSBkcmFmdCBtb2RlbCBhbGlnbnMgd2VsbDogY29kZSBjb21wbGV0aW9uICh3aGVyZSB0b2tlbiBzZXF1ZW5jZXMgZm9sbG93IHN0cm9uZyBzeW50YWN0aWMgcGF0dGVybnMpLCBzdW1tYXJpemF0aW9uLCBhbmQgdHJhbnNsYXRpb24uIEl0IHByb3ZpZGVzIHNtYWxsZXIgZ2FpbnMgb24gaGlnaGx5IGNyZWF0aXZlIG9yIHN0b2NoYXN0aWMgdGFza3Mgd2hlcmUgdGhlIHRhcmdldCBtb2RlbCBkaXZlcmdlcyBmcmVxdWVudGx5IGZyb20gdGhlIGRyYWZ0LiBJbiBwcm9kdWN0aW9uIGRlcGxveW1lbnRzIGF0IGJhdGNoIHNpemUgMSAodGhlIGxhdGVuY3ktY3JpdGljYWwgc2VydmluZyByZWdpbWUpLCBzcGVlZHVwcyBvZiAy4oCTM3ggYXJlIHR5cGljYWwgd2l0aCBhIHdlbGwtbWF0Y2hlZCBkcmFmdCBtb2RlbC4gQXQgaGlnaGVyIGJhdGNoIHNpemVzLCB0aGUgdGFyZ2V0IG1vZGVsIGJlY29tZXMgbW9yZSBjb21wdXRlLWJvdW5kIChyYXRoZXIgdGhhbiBiYW5kd2lkdGgtYm91bmQpLCByZWR1Y2luZyB0aGUgcmVsYXRpdmUgYmVuZWZpdCBvZiBzcGVjdWxhdGl2ZSBkZWNvZGluZy4gTW9zdCBwcm9kdWN0aW9uIGluZmVyZW5jZSBzZXJ2ZXJzIChUR0ksIHZMTE0sIFRlbnNvclJULUxMTSkgaW1wbGVtZW50IHNwZWN1bGF0aXZlIGRlY29kaW5nIHdpdGggYXV0b21hdGljIGRyYWZ0IG1vZGVsIGxvYWRpbmcgYW5kIGNvbmZpZ3VyYWJsZSBrLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSB0eXBpbmcgaW1wb3J0IERpY3RcblxuZGVmIHN3ZWVwX2tfZm9yX29wdGltYWxfYWNjZXB0YW5jZShcbiAgICB0YXJnZXQsIGRyYWZ0LCBpbnB1dF9pZHM6IHRvcmNoLlRlbnNvcixcbiAgICBrX3ZhbHVlcz1yYW5nZSgxLCAxMSksIG5fcnVuczogaW50ID0gMzBcbikgLVx1MDAzZSBEaWN0W2ludCwgZGljdF06XG4gICAgXCJcIlwiU3dlZXAgZHJhZnQgc3RlcHMgayBmcm9tIDEgdG8gMTA7IGZpbmQgb3B0aW1hbCBrIGZvciB0aGlzIGRyYWZ0L3RhcmdldCBwYWlyLlwiXCJcIlxuICAgIHJlc3VsdHMgPSB7fVxuICAgIGRyYWZ0X2Nvc3RfZnJhY3Rpb24gPSAwLjA0ICAjIGRyYWZ0IGlzIH40JSBjb3N0IG9mIHRhcmdldCBmb3J3YXJkIHBhc3NcbiAgICBmb3IgayBpbiBrX3ZhbHVlczpcbiAgICAgICAgYWxwaGFzID0gW11cbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9ydW5zKTpcbiAgICAgICAgICAgIF8sIGFscGhhID0gc3BlY3VsYXRpdmVfZGVjb2RlKHRhcmdldCwgZHJhZnQsIGlucHV0X2lkcywgaz1rKVxuICAgICAgICAgICAgYWxwaGFzLmFwcGVuZChhbHBoYSlcbiAgICAgICAgbWVhbl9hbHBoYSA9IGZsb2F0KG5wLm1lYW4oYWxwaGFzKSlcbiAgICAgICAgIyBUaGVvcmV0aWNhbCBlZmZlY3RpdmUgc3BlZWR1cCBmb3JtdWxhXG4gICAgICAgIGlmIG1lYW5fYWxwaGEgXHUwMDNjIDEuMDpcbiAgICAgICAgICAgIGVmZl90b2tzID0gKDEgLSBtZWFuX2FscGhhICoqIChrICsgMSkpIC8gKDEgLSBtZWFuX2FscGhhKVxuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgZWZmX3Rva3MgPSBrICsgMVxuICAgICAgICBlZmZfc3BlZWR1cCA9IGVmZl90b2tzIC8gKDEgKyBrICogZHJhZnRfY29zdF9mcmFjdGlvbilcbiAgICAgICAgcmVzdWx0c1trXSA9IHtcImFscGhhXCI6IG1lYW5fYWxwaGEsIFwiZWZmX3Rva2Vuc1wiOiBlZmZfdG9rcywgXCJzcGVlZHVwXCI6IGVmZl9zcGVlZHVwfVxuICAgICAgICBwcmludChmXCJrPXtrOjJkfTogYWxwaGE9e21lYW5fYWxwaGE6LjNmfSAgZWZmX3Rva2Vucz17ZWZmX3Rva3M6LjJmfSAgc3BlZWR1cD17ZWZmX3NwZWVkdXA6LjJmfXhcIilcbiAgICBvcHRpbWFsX2sgPSBtYXgocmVzdWx0cywga2V5PWxhbWJkYSB4OiByZXN1bHRzW3hdW1wic3BlZWR1cFwiXSlcbiAgICBwcmludChmXCJcXG5PcHRpbWFsIGs9e29wdGltYWxfa30gLVx1MDAzZSBzcGVlZHVwPXtyZXN1bHRzW29wdGltYWxfa11bXHUwMDI3c3BlZWR1cFx1MDAyN106LjJmfXhcIilcbiAgICByZXR1cm4gcmVzdWx0cyJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTG9zc2xlc3MgU3BlZWR1cCBHdWFyYW50ZWUiLCJjb250ZW50IjoiU3BlY3VsYXRpdmUgZGVjb2RpbmcgaXMgbWF0aGVtYXRpY2FsbHkgZ3VhcmFudGVlZCB0byBwcm9kdWNlIHRoZSBzYW1lIG91dHB1dCBkaXN0cmlidXRpb24gYXMgdGhlIHRhcmdldCBtb2RlbCBhbG9uZSDigJQgaXQgaXMgYSBwdXJlIHNwZWVkdXAgd2l0aCBubyBhY2N1cmFjeSB0cmFkZW9mZiwgdW5saWtlIHF1YW50aXphdGlvbiBvciBwcnVuaW5nLiBUaGUgcmVqZWN0aW9uIHNhbXBsaW5nIGNyaXRlcmlvbiBlbnN1cmVzIHRoYXQgdGhlIG1hcmdpbmFsIGRpc3RyaWJ1dGlvbiBvdmVyIGV2ZXJ5IGFjY2VwdGVkIHRva2VuIGV4YWN0bHkgZXF1YWxzIHRoZSB0YXJnZXRcdTAwMjdzIGNvbmRpdGlvbmFsIGRpc3RyaWJ1dGlvbiBhdCB0aGF0IHBvc2l0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNwZWN1bGF0aXZlIGRlY29kaW5nIGV4cGxvaXRzIG1lbW9yeS1iYW5kd2lkdGggYm90dGxlbmVjazogYXQgYmF0Y2ggc2l6ZSAxLCB0aGUgdGFyZ2V0IG1vZGVsIGNhbiB2ZXJpZnkgayB0b2tlbnMgaW4gb25lIHBhc3MgZm9yIG5lYXJseSB0aGUgc2FtZSBjb3N0IGFzIHZlcmlmeWluZyAxLiIsIkRyYWZ0IG1vZGVsIG11c3Qgc2hhcmUgdGhlIHNhbWUgdG9rZW5pemVyIGFzIHRoZSB0YXJnZXQ7IHNhbWUtZmFtaWx5IHNtYWxsZXIgbW9kZWxzIChlLmcuLCBMTGFNQS02OE0gZm9yIExMYU1BLTdCKSB5aWVsZCB0aGUgaGlnaGVzdCBhY2NlcHRhbmNlIHJhdGVzLiIsIk9wdGltYWwgayBpcyB0eXBpY2FsbHkgNOKAkzg7IGJleW9uZCBrPTgsIHJlamVjdGlvbiByYXRlIGdyb3dzIGZhc3RlciB0aGFuIHRoZSBiZW5lZml0IG9mIHBhcmFsbGVsIHZlcmlmaWNhdGlvbiBmb3IgbW9zdCBkcmFmdC90YXJnZXQgcGFpcnMuIiwiQWNjZXB0YW5jZSByYXRlIGFscGhhIG9mIDAuNzXigJMwLjg1IGlzIHJlYWxpc3RpYyBmb3Igd2VsbC1tYXRjaGVkIHBhaXJzIG9uIG5hdHVyYWwgbGFuZ3VhZ2UgdGFza3M7IGNvZGUgdGFza3Mgb2Z0ZW4gYWNoaWV2ZSAwLjg14oCTMC45Mi4iLCJIdWdnaW5nRmFjZSB0cmFuc2Zvcm1lcnMgc3VwcG9ydHMgYXNzaXN0ZWQgZ2VuZXJhdGlvbiBuYXRpdmVseSB2aWEgYXNzaXN0YW50X21vZGVsPSBwYXJhbWV0ZXIg4oCUIHplcm8gY29kZSBiZXlvbmQgbW9kZWwgbG9hZGluZy4iLCJNZWR1c2EgYW5kIEVBR0xFIHZhcmlhbnRzIGVsaW1pbmF0ZSB0aGUgbmVlZCBmb3IgYSBzZXBhcmF0ZSBkcmFmdCBtb2RlbCBieSBhdHRhY2hpbmcgcHJlZGljdGlvbiBoZWFkcyB0byB0aGUgdGFyZ2V0LCBhdCB0aGUgY29zdCBvZiBhIGJyaWVmIHRyYWluaW5nIHN0ZXAuIiwiU3BlY3VsYXRpdmUgZGVjb2RpbmcgaXMgbW9zdCBpbXBhY3RmdWwgYXQgYmF0Y2ggc2l6ZSAxOyBmb3IgbGFyZ2UgYmF0Y2ggc2VydmluZywgY29udGludW91cyBiYXRjaGluZyBhbmQgcGFnZWQgYXR0ZW50aW9uIHR5cGljYWxseSBkb21pbmF0ZS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Speculative Decoding

Speculative decoding (Chen et al., 2023; Leviathan et al., 2023) is a lossless inference acceleration technique that decouples token proposal from token verification. A small, fast draft model autoregressively generates k candidate tokens in sequence. The large target model then evaluates all k+1 positions in a single forward pass — producing its own probability distributions at each position. A rejection-sampling procedure accepts or rejects each draft token while provably preserving the target model's output distribution. The net effect: the target model processes multiple tokens per forward pass instead of one, reducing the total number of expensive target forward passes needed to generate a sequence.

## Overview

Modern large language model inference is memory-bandwidth bound, not compute bound. At batch size 1, the GPU spends most of its time loading 70–140 GB of model weights from HBM to SRAM for each forward pass — the actual matrix multiplication is secondary. Speculative decoding exploits this asymmetry: since the target model's forward pass is latency-dominated by memory transfers rather than FLOPs, verifying k tokens in one pass takes only marginally more time than verifying 1. Meanwhile, the draft model is 10–100x smaller and can produce k proposals in a fraction of the time a single target forward pass takes. If the draft model's proposals are accepted at rate alpha, the expected tokens produced per target forward pass is (1 - alpha^(k+1)) / (1 - alpha), giving a theoretical speedup of that quantity divided by 1 (greedy baseline). At alpha=0.8 and k=5, this is roughly 3.5 tokens per target pass — a 3.5x throughput gain.

## Draft-Verify Mechanism

The draft-verify loop proceeds as follows. Given input context x_{1:t}, the draft model generates k tokens autoregressively: for each step i in 1..k, it samples x_{t+i} ~ q(. | x_{1:t+i-1}) where q is the draft model's distribution. This produces a sequence of k draft tokens and their associated draft probabilities q_i = q(x_{t+i} | x_{1:t+i-1}). Next, the target model is called once with the full candidate sequence x_{1:t+k} and returns logits for all t+k positions simultaneously. The target probabilities at each draft position are p_i = p(x_{t+i} | x_{1:t+i-1}). The rejection sampling loop then iterates i from 1 to k: if p_i / q_i >= 1, token i is always accepted; otherwise token i is accepted with probability p_i / q_i and rejected with probability 1 - p_i / q_i. On rejection, a corrected token is sampled from the residual distribution max(0, p_i - q_i) / Z.

```python
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM
from typing import Tuple, List

def speculative_decode(
    target_model, draft_model, input_ids: torch.Tensor,
    k: int = 5, temperature: float = 1.0
) -> Tuple[torch.Tensor, float]:
    """Draft proposes k tokens; target verifies all in one forward pass."""
    draft_input = input_ids.clone()
    draft_tokens: List[torch.Tensor] = []
    draft_probs: List[float] = []
    for _ in range(k):
        with torch.no_grad():
            logits = draft_model(draft_input).logits[:, -1, :] / temperature
            probs = F.softmax(logits, dim=-1)
            tok = torch.multinomial(probs, 1)
            draft_tokens.append(tok)
            draft_probs.append(probs[0, tok.item()].item())
            draft_input = torch.cat([draft_input, tok], dim=-1)
    candidate_ids = torch.cat([input_ids] + draft_tokens, dim=-1)
    with torch.no_grad():
        target_logits = target_model(candidate_ids).logits
    accepted: List[torch.Tensor] = []
    n = len(input_ids[0])
    for i, (tok, q_i) in enumerate(zip(draft_tokens, draft_probs)):
        t_probs = F.softmax(target_logits[0, n - 1 + i] / temperature, dim=-1)
        accept_prob = min(1.0, t_probs[tok.item()].item() / (q_i + 1e-9))
        if torch.rand(1).item() < accept_prob:
            accepted.append(tok)
        else:
            # Sample from residual (corrected) distribution
            q_dist = F.softmax(target_logits[0, n - 1 + i] / temperature, dim=-1)
            adj = (t_probs - q_dist * q_i).clamp(min=0)
            fallback = torch.multinomial(adj / (adj.sum() + 1e-9), 1).unsqueeze(0)
            accepted.append(fallback)
            break  # stop accepting after first rejection
    return torch.cat([input_ids] + accepted, dim=-1), len(accepted) / k
```

## Acceptance Criterion

The acceptance probability for draft token x_{t+i} is min(1, p(x_{t+i} | context) / q(x_{t+i} | context)). This is the same criterion used in importance sampling and the Metropolis-Hastings algorithm. When the draft model is well-aligned with the target (i.e., q ≈ p), acceptance rate alpha approaches 1. When they diverge (e.g., draft predicts a different token distribution for technical content), alpha drops. The corrected distribution on rejection is the normalized positive part of (p - q): we subtract the draft's contribution and re-normalize. This ensures that the marginal distribution over accepted tokens exactly matches p — the guarantee that speculative decoding is lossless. Unlike quantization or knowledge distillation, there is zero accuracy tradeoff: the output distribution is identical to greedy or sampled decoding from the target alone.

## Speculative Sampling Math

Let p(x|c) be the target distribution and q(x|c) be the draft distribution over the next token given context c. Define the acceptance probability a(x) = min(1, p(x|c) / q(x|c)). The expected number of tokens accepted per speculative step is E[accepted] = sum_x q(x) * a(x) = sum_x min(q(x), p(x)) = 1 - TV(p, q) where TV is total variation distance. When p = q exactly (perfect draft), all k tokens are always accepted. The expected speedup relative to greedy decoding (1 target call per token) is: speedup ≈ (1 - alpha^(k+1)) / ((1 - alpha) * C_draft) where alpha = E[a(x)] and C_draft is the relative cost of one draft forward pass as a fraction of the target cost. For a 68M draft against a 7B target, C_draft ≈ 0.01–0.05, making the draft overhead negligible.

```python
import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer

def benchmark_speculative_decoding(
    target_name: str = "meta-llama/Llama-2-7b-hf",
    draft_name: str = "JackFram/llama-68m",
    n_prompts: int = 50,
    max_new_tokens: int = 128,
    k: int = 5
) -> dict:
    """Measure acceptance rate and wall-clock speedup vs greedy baseline."""
    tokenizer = AutoTokenizer.from_pretrained(target_name)
    target = AutoModelForCausalLM.from_pretrained(
        target_name, torch_dtype=torch.float16, device_map="auto")
    draft = AutoModelForCausalLM.from_pretrained(
        draft_name, torch_dtype=torch.float16, device_map="auto")
    prompts = ["Describe the architecture of a transformer model in detail."] * n_prompts
    inputs = tokenizer(prompts[0], return_tensors="pt").to("cuda")
    # Greedy baseline
    t0 = time.perf_counter()
    for _ in range(n_prompts):
        target.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    greedy_time = time.perf_counter() - t0
    # Speculative decoding
    acceptance_rates = []
    t0 = time.perf_counter()
    for _ in range(n_prompts):
        _, alpha = speculative_decode(target, draft, inputs.input_ids, k=k)
        acceptance_rates.append(alpha)
    spec_time = time.perf_counter() - t0
    speedup = greedy_time / spec_time
    mean_alpha = sum(acceptance_rates) / len(acceptance_rates)
    print(f"Greedy:      {greedy_time:.2f}s total")
    print(f"Speculative: {spec_time:.2f}s total  (speedup={speedup:.2f}x)")
    print(f"Mean acceptance rate alpha: {mean_alpha:.3f}")
    print(f"Expected speedup from formula: {(1 - mean_alpha**(k+1)) / (1 - mean_alpha + 1e-9):.2f}x")
    return {"speedup": speedup, "alpha": mean_alpha}
```

## Choosing the Draft Model

The draft model must satisfy two competing requirements: it must be fast enough that its k forward passes cost less than the target pass it replaces, and it must be accurate enough that acceptance rate alpha stays high. The key practical constraint is that the draft and target must share the same tokenizer vocabulary — the tokens proposed by the draft must be valid tokens from the target's vocabulary for the rejection sampling math to work. The best draft models are smaller members of the same model family trained with the same data distribution: for LLaMA-2-70B, use LLaMA-2-7B or TinyLLaMA-1.1B as the draft. Draft models from unrelated families (e.g., GPT-2 as draft for LLaMA) tend to have poor alignment and low alpha. Self-drafting — using early exit layers of the target model itself — avoids this problem by sharing the full embedding space, but requires model surgery. Medusa adds multiple prediction heads to the target model itself, trained to predict positions 2, 3, ... k ahead simultaneously.

| Draft Model | Acceptance Rate (alpha) | Effective Speedup | Extra Memory (GB) | Latency Reduction |
| --- | --- | --- | --- | --- |
| LLaMA-68M | 0.65–0.70 | 1.8–2.2x | +0.1 GB | 40–50% |
| LLaMA-160M | 0.70–0.75 | 2.0–2.5x | +0.3 GB | 45–55% |
| LLaMA-1B | 0.78–0.83 | 2.5–3.0x | +2 GB | 55–65% |
| LLaMA-3B | 0.82–0.87 | 2.8–3.4x | +6 GB | 60–70% |
| Self-draft (Medusa) | 0.75–0.88 | 2.2–3.5x | +0.05 GB (heads only) | 55–70% |

## Self-Speculative and Medusa Variants

Medusa (Cai et al., 2024) attaches k additional LM heads to the final hidden state of the target model. Each Medusa head i predicts the token at position t+i+1 given the current hidden state — all heads run in parallel during one target forward pass. A tree-structured verification then accepts consistent candidate paths. Unlike standard speculative decoding, Medusa requires no separate draft model and adds only a small fraction of parameters (the extra heads). The tradeoff is that Medusa heads must be trained, whereas standard speculative decoding works out-of-the-box with any compatible draft model. EAGLE (Li et al., 2024) is a further refinement where the draft model is an auto-regressive model that operates on target hidden states rather than raw tokens, achieving acceptance rates of 0.85–0.90 by directly modeling the target's representation space.

```python
import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer

def hf_assisted_generation_benchmark(
    target_name: str = "meta-llama/Llama-2-7b-hf",
    draft_name: str = "JackFram/llama-68m",
    max_new_tokens: int = 200
) -> float:
    """Use HuggingFace built-in assisted generation (speculative decoding)."""
    tokenizer = AutoTokenizer.from_pretrained(target_name)
    target = AutoModelForCausalLM.from_pretrained(
        target_name, torch_dtype=torch.float16, device_map="auto")
    draft = AutoModelForCausalLM.from_pretrained(
        draft_name, torch_dtype=torch.float16, device_map="auto")
    prompt = "The fundamental theorem of calculus states that"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    # Greedy baseline
    t0 = time.perf_counter()
    out_greedy = target.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    t_base = time.perf_counter() - t0
    # Assisted generation: HuggingFace runs speculative decoding internally
    t0 = time.perf_counter()
    out_spec = target.generate(**inputs, max_new_tokens=max_new_tokens,
                                do_sample=False, assistant_model=draft)
    t_spec = time.perf_counter() - t0
    speedup = t_base / t_spec
    print(f"Greedy:    {t_base:.2f}s   Assisted: {t_spec:.2f}s   Speedup: {speedup:.2f}x")
    # Verify identical outputs (speculative decoding is lossless)
    assert out_greedy[0].tolist() == out_spec[0].tolist(), "Output mismatch — bug!"
    print("Output distributions match: verified lossless.")
    return speedup
```

## Throughput Gains in Practice

Real-world speedups depend heavily on task type and output length. Speculative decoding provides the largest gains on tasks where the output is predictable and the draft model aligns well: code completion (where token sequences follow strong syntactic patterns), summarization, and translation. It provides smaller gains on highly creative or stochastic tasks where the target model diverges frequently from the draft. In production deployments at batch size 1 (the latency-critical serving regime), speedups of 2–3x are typical with a well-matched draft model. At higher batch sizes, the target model becomes more compute-bound (rather than bandwidth-bound), reducing the relative benefit of speculative decoding. Most production inference servers (TGI, vLLM, TensorRT-LLM) implement speculative decoding with automatic draft model loading and configurable k.

```python
import torch
import numpy as np
from typing import Dict

def sweep_k_for_optimal_acceptance(
    target, draft, input_ids: torch.Tensor,
    k_values=range(1, 11), n_runs: int = 30
) -> Dict[int, dict]:
    """Sweep draft steps k from 1 to 10; find optimal k for this draft/target pair."""
    results = {}
    draft_cost_fraction = 0.04  # draft is ~4% cost of target forward pass
    for k in k_values:
        alphas = []
        for _ in range(n_runs):
            _, alpha = speculative_decode(target, draft, input_ids, k=k)
            alphas.append(alpha)
        mean_alpha = float(np.mean(alphas))
        # Theoretical effective speedup formula
        if mean_alpha < 1.0:
            eff_toks = (1 - mean_alpha ** (k + 1)) / (1 - mean_alpha)
        else:
            eff_toks = k + 1
        eff_speedup = eff_toks / (1 + k * draft_cost_fraction)
        results[k] = {"alpha": mean_alpha, "eff_tokens": eff_toks, "speedup": eff_speedup}
        print(f"k={k:2d}: alpha={mean_alpha:.3f}  eff_tokens={eff_toks:.2f}  speedup={eff_speedup:.2f}x")
    optimal_k = max(results, key=lambda x: results[x]["speedup"])
    print(f"\nOptimal k={optimal_k} -> speedup={results[optimal_k]['speedup']:.2f}x")
    return results
```

> **Lossless Speedup Guarantee**: Speculative decoding is mathematically guaranteed to produce the same output distribution as the target model alone — it is a pure speedup with no accuracy tradeoff, unlike quantization or pruning. The rejection sampling criterion ensures that the marginal distribution over every accepted token exactly equals the target's conditional distribution at that position.

## Key Takeaways

- Speculative decoding exploits memory-bandwidth bottleneck: at batch size 1, the target model can verify k tokens in one pass for nearly the same cost as verifying 1.
- Draft model must share the same tokenizer as the target; same-family smaller models (e.g., LLaMA-68M for LLaMA-7B) yield the highest acceptance rates.
- Optimal k is typically 4–8; beyond k=8, rejection rate grows faster than the benefit of parallel verification for most draft/target pairs.
- Acceptance rate alpha of 0.75–0.85 is realistic for well-matched pairs on natural language tasks; code tasks often achieve 0.85–0.92.
- HuggingFace transformers supports assisted generation natively via assistant_model= parameter — zero code beyond model loading.
- Medusa and EAGLE variants eliminate the need for a separate draft model by attaching prediction heads to the target, at the cost of a brief training step.
- Speculative decoding is most impactful at batch size 1; for large batch serving, continuous batching and paged attention typically dominate.

---

