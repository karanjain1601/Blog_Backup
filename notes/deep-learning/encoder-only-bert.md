---
title: "Encoder-Only Transformers — BERT, RoBERTa, and DeBERTa"
slug: "encoder-only-bert"
description: "Encoder-only Transformers with bidirectional attention — BERT's masked language modelling, fine-tuning for classification, and the improvements in RoBERTa, ELECTRA, and DeBERTa."
tags: ["deep-learning", "transformers"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW5jb2Rlci1vbmx5IFRyYW5zZm9ybWVycyB1c2UgYmlkaXJlY3Rpb25hbCBzZWxmLWF0dGVudGlvbjogZXZlcnkgdG9rZW4gY2FuIGF0dGVuZCB0byBldmVyeSBvdGhlciB0b2tlbiBpbiBib3RoIGRpcmVjdGlvbnMgc2ltdWx0YW5lb3VzbHkuIFRoZXJlIGlzIG5vIGNhdXNhbCBtYXNrLiBUaGlzIG1ha2VzIGVuY29kZXIgbW9kZWxzIGlkZWFsIGZvciB0YXNrcyB0aGF0IHJlcXVpcmUgdW5kZXJzdGFuZGluZyB0aGUgZnVsbCBjb250ZXh0IG9mIGFuIGlucHV0IOKAlCBjbGFzc2lmaWNhdGlvbiwgbmFtZWQgZW50aXR5IHJlY29nbml0aW9uLCBxdWVzdGlvbiBhbnN3ZXJpbmcsIGFuZCBuYXR1cmFsIGxhbmd1YWdlIGluZmVyZW5jZSDigJQgYnV0IHRoZXkgY2Fubm90IGdlbmVyYXRlIHRleHQgYXV0b3JlZ3Jlc3NpdmVseS4gQkVSVCAoRGV2bGluIGV0IGFsLiAyMDE4KSBlc3RhYmxpc2hlZCB0aGUgZW5jb2Rlci1vbmx5IHBhcmFkaWdtIGFuZCBzZXQgb2ZmIGEgd2F2ZSBvZiBpbXByb3ZlbWVudHM6IFJvQkVSVGEsIEVMRUNUUkEsIERlQkVSVGEsIGFuZCBtYW55IG90aGVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCaWRpcmVjdGlvbmFsIEF0dGVudGlvbiDigJQgU2VlaW5nIEFsbCBUb2tlbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIGEgc3RhbmRhcmQgZW5jb2RlciBzZWxmLWF0dGVudGlvbiBsYXllciwgdGhlIGF0dGVudGlvbiBzY29yZSBtYXRyaXggUyA9IFFL4bWAIC8g4oiaZF9rIGhhcyBubyBtYXNrIGFwcGxpZWQg4oCUIGFsbCBMw5dMIGVudHJpZXMgYXJlIHVzZWQuIFRoaXMgbWVhbnMgZXZlcnkgcG9zaXRpb24gY2FuIGRyYXcgaW5mb3JtYXRpb24gZnJvbSBldmVyeSBvdGhlciBwb3NpdGlvbiwgaW5jbHVkaW5nIGZ1dHVyZSB0b2tlbnMuIFRoZSBhdHRlbnRpb24gd2VpZ2h0cyBmb3JtIGEgZGVuc2UgTMOXTCBtYXRyaXggYWZ0ZXIgc29mdG1heC4gQmlkaXJlY3Rpb25hbGl0eSBpcyB3aGF0IG1ha2VzIGVuY29kZXJzIHBvd2VyZnVsIGZvciB1bmRlcnN0YW5kaW5nIHRhc2tzOiB0aGUgcmVwcmVzZW50YXRpb24gb2YgdGhlIHdvcmQgXHUwMDI3YmFua1x1MDAyNyBjYW4gc2ltdWx0YW5lb3VzbHkgbG9vayBsZWZ0IGF0IFx1MDAyN3JpdmVyXHUwMDI3IGFuZCByaWdodCBhdCBcdTAwMjdkZXBvc2l0XHUwMDI3IHRvIHJlc29sdmUgaXRzIG1lYW5pbmcuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJFbmNvZGVyOiBhbGwgcG9zaXRpb25zIGF0dGVuZCB0byBhbGwgb3RoZXJzIOKAlCBmdWxsIEzDl0wgYXR0ZW50aW9uIG1hdHJpeCIsIkRlY29kZXIgKGNhdXNhbCk6IHBvc2l0aW9uIGkgYXR0ZW5kcyBvbmx5IHRvIGog4omkIGkg4oCUIGxvd2VyLXRyaWFuZ3VsYXIgbWF0cml4IiwiRW5jb2RlciBpbnB1dDogW0NMU10gdG9rZW4gKyByZWFsIHRva2VucyArIFtTRVBdIHRva2VuIChXb3JkUGllY2UgdG9rZW5pc2VkKSIsIltDTFNdIHJlcHJlc2VudGF0aW9uIGFnZ3JlZ2F0ZXMgdGhlIHdob2xlLXNlcXVlbmNlIG1lYW5pbmcg4oCUIHVzZWQgZm9yIGNsYXNzaWZpY2F0aW9uIiwiUGFkZGluZyBtYXNrIHN0aWxsIGFwcGxpZWQ6IFBBRCB0b2tlbnMgYmxvY2tlZCBmcm9tIHJlY2VpdmluZyBhdHRlbnRpb24gKGtleV9wYWRkaW5nX21hc2spIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IEVuY29kZXJzIENhbm5vdCBHZW5lcmF0ZSBUZXh0IiwiY29udGVudCI6IkR1cmluZyBpbmZlcmVuY2UsIGFuIGF1dG9yZWdyZXNzaXZlIGdlbmVyYXRvciBtdXN0IHByZWRpY3QgdG9rZW4gdCBnaXZlbiB0b2tlbnMgMCB0aHJvdWdoIHQtMSB3aXRob3V0IHNlZWluZyB0KzEsIHQrMiwg4oCmIEVuY29kZXItb25seSBtb2RlbHMgaGF2ZSBubyBzdWNoIGNvbnN0cmFpbnQg4oCUIHRoZXkgYWx3YXlzIHNlZSB0aGUgZW50aXJlIGlucHV0IHNlcXVlbmNlLiBUaGlzIG1ha2VzIHRoZW0gZXhjZWxsZW50IHVuZGVyc3RhbmRlcnMgYnV0IGluY2FwYWJsZSBvZiBzZXF1ZW50aWFsIGdlbmVyYXRpb24gd2l0aG91dCBtb2RpZmljYXRpb24gKGUuZy4sIGFkZGluZyBhIGNhdXNhbCBkZWNvZGVyIG9yIHVzaW5nIG1hc2tlZC10b2tlbiBwcmVkaWN0aW9uIGl0ZXJhdGl2ZWx5KS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYXNrZWQgTGFuZ3VhZ2UgTW9kZWxsaW5nIOKAlCBCRVJUXHUwMDI3cyBQcmV0cmFpbmluZyBPYmplY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJFUlQgaXMgcHJldHJhaW5lZCB3aXRoIE1hc2tlZCBMYW5ndWFnZSBNb2RlbGxpbmcgKE1MTSk6IDE1JSBvZiBpbnB1dCB0b2tlbnMgYXJlIHJhbmRvbWx5IHNlbGVjdGVkLiBPZiB0aG9zZSwgODAlIGFyZSByZXBsYWNlZCB3aXRoIHRoZSBzcGVjaWFsIFtNQVNLXSB0b2tlbiwgMTAlIGFyZSByZXBsYWNlZCB3aXRoIGEgcmFuZG9tIHRva2VuIGZyb20gdGhlIHZvY2FidWxhcnksIGFuZCAxMCUgYXJlIGxlZnQgdW5jaGFuZ2VkLiBUaGUgbW9kZWwgaXMgdHJhaW5lZCB0byBwcmVkaWN0IHRoZSBvcmlnaW5hbCB0b2tlbiBhdCBlYWNoIG1hc2tlZCBwb3NpdGlvbiB1c2luZyBjcm9zcy1lbnRyb3B5IGxvc3MuIFRoaXMgZm9yY2VzIHRoZSBtb2RlbCB0byBidWlsZCByaWNoIGNvbnRleHR1YWwgcmVwcmVzZW50YXRpb25zIGJlY2F1c2UgcHJlZGljdGluZyBhIG1hc2tlZCB3b3JkIHJlcXVpcmVzIHVuZGVyc3RhbmRpbmcgaXRzIGxlZnQgYW5kIHJpZ2h0IGNvbnRleHQgc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQkVSVCBBcmNoaXRlY3R1cmUgYW5kIEZpbmUtVHVuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCRVJULWJhc2U6IDEyIGxheWVycywgMTIgYXR0ZW50aW9uIGhlYWRzLCBkX21vZGVsPTc2OCwgZF9mZj0zMDcyLCAxMTBNIHBhcmFtZXRlcnMuIEJFUlQtbGFyZ2U6IDI0IGxheWVycywgMTYgaGVhZHMsIGRfbW9kZWw9MTAyNCwgZF9mZj00MDk2LCAzNDBNIHBhcmFtZXRlcnMuIEZpbmUtdHVuaW5nIGFkZHMgYSB0YXNrLXNwZWNpZmljIGhlYWQgb24gdG9wIG9mIHRoZSBwcmV0cmFpbmVkIGVuY29kZXIuIEZvciBzZW50ZW5jZSBjbGFzc2lmaWNhdGlvbiwgYSBsaW5lYXIgbGF5ZXIgbWFwcyB0aGUgW0NMU10gdG9rZW4gcmVwcmVzZW50YXRpb24gKHNoYXBlIGRfbW9kZWwpIHRvIHRoZSBudW1iZXIgb2YgY2xhc3Nlcy4gRm9yIHRva2VuLWxldmVsIHRhc2tzIChORVIsIFBPUyB0YWdnaW5nKSwgYSBsaW5lYXIgaGVhZCBpcyBhcHBsaWVkIHRvIGV2ZXJ5IHRva2VuXHUwMDI3cyByZXByZXNlbnRhdGlvbi4gQkVSVCBwb3B1bGFyaXNlZCB0aGUgcHJldHJhaW4tdGhlbi1maW5ldHVuZSBwYXJhZGlnbSB0aGF0IG5vdyBkb21pbmF0ZXMgTkxQLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMSDigJQgRW5jb2Rlci1Pbmx5IFRyYW5zZm9ybWVyIEJsb2NrIGZyb20gU2NyYXRjaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBiaWRpcmVjdGlvbmFsIChubyBjYXVzYWwgbWFzaykgVHJhbnNmb3JtZXIgZW5jb2RlciBibG9jaywgc2hvd2luZyB0aGF0IGFsbCBMw5dMIGF0dGVudGlvbiB3ZWlnaHQgZW50cmllcyBhcmUgbm9uLXplcm8uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIEVuY29kZXJCbG9jayhubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkVuY29kZXItb25seSBUcmFuc2Zvcm1lciBibG9jazogYmlkaXJlY3Rpb25hbCBzZWxmLWF0dGVudGlvbiwgbm8gY2F1c2FsIG1hc2suXG4gICAgUHJlLW5vcm0gbGF5b3V0IChtb2Rlcm4gdmFyaWFudCkuXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgbl9oZWFkczogaW50LCBkX2ZmOiBpbnQsXG4gICAgICAgICAgICAgICAgIGRyb3BvdXQ6IGZsb2F0ID0gMC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubm9ybTEgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5ub3JtMiA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmF0dG4gID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRyb3BvdXQ9ZHJvcG91dCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5mZjEgICA9IG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKVxuICAgICAgICBzZWxmLmZmMiAgID0gbm4uTGluZWFyKGRfZmYsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYuYWN0ICAgPSBubi5HRUxVKClcbiAgICAgICAgc2VsZi5kcm9wICA9IG5uLkRyb3BvdXQoZHJvcG91dClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICBrZXlfcGFkZGluZ19tYXNrOiB0b3JjaC5UZW5zb3IgPSBOb25lKTpcbiAgICAgICAgIyBObyBhdHRuX21hc2sgcGFzc2VkIC1cdTAwM2UgYmlkaXJlY3Rpb25hbCAoYWxsIHBvc2l0aW9ucyBhdHRlbmQgdG8gYWxsKVxuICAgICAgICBuID0gc2VsZi5ub3JtMSh4KVxuICAgICAgICBhLCB3ZWlnaHRzID0gc2VsZi5hdHRuKG4sIG4sIG4sIGtleV9wYWRkaW5nX21hc2s9a2V5X3BhZGRpbmdfbWFzaylcbiAgICAgICAgeCA9IHggKyBzZWxmLmRyb3AoYSlcbiAgICAgICAgeCA9IHggKyBzZWxmLmRyb3Aoc2VsZi5mZjIoc2VsZi5hY3Qoc2VsZi5mZjEoc2VsZi5ub3JtMih4KSkpKSlcbiAgICAgICAgcmV0dXJuIHgsIHdlaWdodHNcblxuIyBCRVJULWJhc2UgZGltZW5zaW9uc1xuYmxvY2sgPSBFbmNvZGVyQmxvY2soZF9tb2RlbD03NjgsIG5faGVhZHM9MTIsIGRfZmY9MzA3MilcbnggPSB0b3JjaC5yYW5kbigyLCAxMiwgNzY4KVxub3V0LCBhdHRuID0gYmxvY2soeClcbnByaW50KFx1MDAyN0VuY29kZXIgb3V0cHV0Olx1MDAyNywgb3V0LnNoYXBlKSAgICAgICAgICAjICgyLCAxMiwgNzY4KVxucHJpbnQoXHUwMDI3QXR0ZW50aW9uIHdlaWdodHM6XHUwMDI3LCBhdHRuLnNoYXBlKSAgICAgICMgKDIsIDEyLCAxMilcbnByaW50KFx1MDAyN05vbi16ZXJvIHdlaWdodHM6XHUwMDI3LCAoYXR0biBcdTAwM2UgMWUtNikuc3VtKCkuaXRlbSgpLCBcdTAwMjcoYWxsIHBvc2l0aW9ucyBhdHRlbmQgYWxsKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIE1MTSBEYXRhIFByZXBhcmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbXBsZW1lbnRpbmcgdGhlIEJFUlQgbWFza2luZyBzdHJhdGVneTogMTUlIG9mIHRva2VucyBzZWxlY3RlZCwgODAlIHJlcGxhY2VkIHdpdGggW01BU0tdLCAxMCUgcmFuZG9tLCAxMCUgdW5jaGFuZ2VkLiBMYWJlbHMgb2YgLTEwMCBhdCBub24tbWFza2VkIHBvc2l0aW9ucyBhcmUgaWdub3JlZCBieSBDcm9zc0VudHJvcHlMb3NzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCByYW5kb21cblxuZGVmIHByZXBhcmVfbWxtX2JhdGNoKHRva2VuX2lkczogbGlzdCwgdm9jYWJfc2l6ZTogaW50LFxuICAgICAgICAgICAgICAgICAgICAgICBtYXNrX3Rva2VuX2lkOiBpbnQsIG1hc2tfcHJvYjogZmxvYXQgPSAwLjE1LFxuICAgICAgICAgICAgICAgICAgICAgICBwYWRfaWQ6IGludCA9IDApOlxuICAgIFwiXCJcIkJFUlQtc3R5bGUgTUxNIG1hc2tpbmcuXG4gICAgT2Ygc2VsZWN0ZWQgcG9zaXRpb25zOiA4MCUgLVx1MDAzZSBbTUFTS10sIDEwJSAtXHUwMDNlIHJhbmRvbSwgMTAlIC1cdTAwM2UgdW5jaGFuZ2VkLlxuICAgIFJldHVybnMgKGlucHV0X2lkcywgbGFiZWxzLCBhdHRlbnRpb25fbWFzaykgYXMgdGVuc29ycy5cbiAgICBsYWJlbHNbYiwgcG9zXSA9IC0xMDAgKGlnbm9yZWQpIGZvciBub24tbWFza2VkIHBvc2l0aW9ucy5cbiAgICBcIlwiXCJcbiAgICBtYXhfbGVuID0gbWF4KGxlbihzKSBmb3IgcyBpbiB0b2tlbl9pZHMpXG4gICAgaW5wdXRzLCBsYWJlbHMsIGF0dF9tYXNrcyA9IFtdLCBbXSwgW11cbiAgICBmb3Igc2VxIGluIHRva2VuX2lkczpcbiAgICAgICAgaWRzICAgPSBsaXN0KHNlcSlcbiAgICAgICAgbGFiZWwgPSBbLTEwMF0gKiBtYXhfbGVuXG4gICAgICAgIGFtICAgID0gWzFdICogbGVuKHNlcSkgKyBbMF0gKiAobWF4X2xlbiAtIGxlbihzZXEpKVxuICAgICAgICBpZHMgICs9IFtwYWRfaWRdICogKG1heF9sZW4gLSBsZW4oc2VxKSlcbiAgICAgICAgZm9yIHBvcyBpbiByYW5nZShsZW4oc2VxKSk6XG4gICAgICAgICAgICBpZiByYW5kb20ucmFuZG9tKCkgXHUwMDNjIG1hc2tfcHJvYjpcbiAgICAgICAgICAgICAgICBsYWJlbFtwb3NdID0gaWRzW3Bvc10gICAgICAgICAgIyBzdG9yZSBvcmlnaW5hbCB0b2tlbiBhcyB0YXJnZXRcbiAgICAgICAgICAgICAgICByID0gcmFuZG9tLnJhbmRvbSgpXG4gICAgICAgICAgICAgICAgaWYgciBcdTAwM2MgMC44MDogICAgICAgICAgICAgICAgICAgIyA4MCU6IHJlcGxhY2Ugd2l0aCBbTUFTS11cbiAgICAgICAgICAgICAgICAgICAgaWRzW3Bvc10gPSBtYXNrX3Rva2VuX2lkXG4gICAgICAgICAgICAgICAgZWxpZiByIFx1MDAzYyAwLjkwOiAgICAgICAgICAgICAgICAgIyAxMCU6IHJlcGxhY2Ugd2l0aCByYW5kb20gdG9rZW5cbiAgICAgICAgICAgICAgICAgICAgaWRzW3Bvc10gPSByYW5kb20ucmFuZGludCg1LCB2b2NhYl9zaXplIC0gMSlcbiAgICAgICAgICAgICAgICAjIDEwJTogbGVhdmUgdW5jaGFuZ2VkXG4gICAgICAgIGlucHV0cy5hcHBlbmQoaWRzKTsgbGFiZWxzLmFwcGVuZChsYWJlbCk7IGF0dF9tYXNrcy5hcHBlbmQoYW0pXG4gICAgcmV0dXJuIHRvcmNoLnRlbnNvcihpbnB1dHMpLCB0b3JjaC50ZW5zb3IobGFiZWxzKSwgdG9yY2gudGVuc29yKGF0dF9tYXNrcylcblxucmFuZG9tLnNlZWQoNDIpXG5zZXFzICAgPSBbWzEwMSwgMjA1NCwgMjAwMywgMTk5NiwgMzAwNywgMTAyXSwgWzEwMSwgNDA2NywgMjAyNCwgNDY1OCwgMTAyXV1cbmlucCwgbGJsLCBhbSA9IHByZXBhcmVfbWxtX2JhdGNoKHNlcXMsIHZvY2FiX3NpemU9MzAwMDAsIG1hc2tfdG9rZW5faWQ9MTAzKVxucHJpbnQoXHUwMDI3SW5wdXQgSURzOlx1MDAyNylcbnByaW50KGlucClcbnByaW50KFx1MDAyN0xhYmVscyAoLTEwMCA9IG5vdCBtYXNrZWQpOlx1MDAyNylcbnByaW50KGxibCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDMg4oCUIEJFUlQgRmluZS1UdW5pbmcgZm9yIENsYXNzaWZpY2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVc2luZyBIdWdnaW5nRmFjZSB0cmFuc2Zvcm1lcnMgdG8gZmluZS10dW5lIEJFUlQgZm9yIGJpbmFyeSBjbGFzc2lmaWNhdGlvbjogYSBsaW5lYXIgaGVhZCBvbiB0aGUgW0NMU10gdG9rZW4gcmVwcmVzZW50YXRpb24gd2l0aCBBZGFtVyBvcHRpbWlzZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQmVydE1vZGVsLCBCZXJ0VG9rZW5pemVyXG5mcm9tIHRvcmNoLm9wdGltIGltcG9ydCBBZGFtV1xuXG5jbGFzcyBCZXJ0Rm9yU2VudGltZW50KG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiQkVSVCBlbmNvZGVyICsgbGluZWFyIGNsYXNzaWZpY2F0aW9uIGhlYWQgb24gdGhlIFtDTFNdIHRva2VuLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2NsYXNzZXM6IGludCA9IDIsIGRyb3BvdXQ6IGZsb2F0ID0gMC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmVydCAgICAgICA9IEJlcnRNb2RlbC5mcm9tX3ByZXRyYWluZWQoXHUwMDI3YmVydC1iYXNlLXVuY2FzZWRcdTAwMjcpXG4gICAgICAgIHNlbGYuZHJvcG91dCAgICA9IG5uLkRyb3BvdXQoZHJvcG91dClcbiAgICAgICAgc2VsZi5jbGFzc2lmaWVyID0gbm4uTGluZWFyKDc2OCwgbl9jbGFzc2VzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgaW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzaywgdG9rZW5fdHlwZV9pZHM9Tm9uZSk6XG4gICAgICAgIG91dCA9IHNlbGYuYmVydChpbnB1dF9pZHM9aW5wdXRfaWRzLFxuICAgICAgICAgICAgICAgICAgICAgICAgYXR0ZW50aW9uX21hc2s9YXR0ZW50aW9uX21hc2ssXG4gICAgICAgICAgICAgICAgICAgICAgICB0b2tlbl90eXBlX2lkcz10b2tlbl90eXBlX2lkcylcbiAgICAgICAgY2xzX3JlcCA9IG91dC5sYXN0X2hpZGRlbl9zdGF0ZVs6LCAwLCA6XSAgICMgW0NMU10gdG9rZW4gYXQgcG9zaXRpb24gMFxuICAgICAgICByZXR1cm4gc2VsZi5jbGFzc2lmaWVyKHNlbGYuZHJvcG91dChjbHNfcmVwKSlcblxuIyBUb2tlbmlzZSBhbmQgcnVuIG9uZSB0cmFpbmluZyBzdGVwXG50b2tlbml6ZXIgPSBCZXJ0VG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcdTAwMjdiZXJ0LWJhc2UtdW5jYXNlZFx1MDAyNylcbnRleHRzICAgICA9IFtcdTAwMjdJIGxvdmUgdGhpcyBmaWxtIVx1MDAyNywgXHUwMDI3VGhlIG1vdmllIHdhcyB0ZXJyaWJsZS5cdTAwMjddXG5sYWJlbHMgICAgPSB0b3JjaC50ZW5zb3IoWzEsIDBdKVxuZW5jICAgICAgID0gdG9rZW5pemVyKHRleHRzLCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNywgcGFkZGluZz1UcnVlLCB0cnVuY2F0aW9uPVRydWUpXG5cbm1vZGVsICAgPSBCZXJ0Rm9yU2VudGltZW50KClcbm9wdGltciAgPSBBZGFtVyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTJlLTUsIHdlaWdodF9kZWNheT0wLjAxKVxubG9zc19mbiA9IG5uLkNyb3NzRW50cm9weUxvc3MoKVxuXG5tb2RlbC50cmFpbigpXG5sb2dpdHMgPSBtb2RlbChlbmNbXHUwMDI3aW5wdXRfaWRzXHUwMDI3XSwgZW5jW1x1MDAyN2F0dGVudGlvbl9tYXNrXHUwMDI3XSlcbmxvc3MgICA9IGxvc3NfZm4obG9naXRzLCBsYWJlbHMpXG5sb3NzLmJhY2t3YXJkKClcbm9wdGltci5zdGVwKClcbnByaW50KFx1MDAyN0xvZ2l0czpcdTAwMjcsIGxvZ2l0cy5kZXRhY2goKSlcbnByaW50KFx1MDAyN0xvc3M6ICBcdTAwMjcsIHJvdW5kKGxvc3MuaXRlbSgpLCA0KSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDQg4oCUIEVMRUNUUkEgUmVwbGFjZWQgVG9rZW4gRGV0ZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFTEVDVFJBIChDbGFyayBldCBhbC4gMjAyMCkgcmVwbGFjZXMgTUxNIHdpdGggYSBkaXNjcmltaW5hdGl2ZSBvYmplY3RpdmU6IGEgc21hbGwgZ2VuZXJhdG9yIGNvcnJ1cHRzIHRva2VucywgYW5kIHRoZSBkaXNjcmltaW5hdG9yIG11c3QgY2xhc3NpZnkgZWFjaCB0b2tlbiBhcyByZWFsIG9yIHJlcGxhY2VkLiBNb3JlIHNhbXBsZS1lZmZpY2llbnQgdGhhbiBNTE0gYmVjYXVzZSB0aGUgbG9zcyBzaWduYWwgY292ZXJzIGFsbCB0b2tlbnMsIG5vdCBqdXN0IHRoZSAxNSUgbWFza2VkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHJhbmRvbVxuXG5kZWYgc2ltdWxhdGVfcnRkKHRva2VuX2lkczogdG9yY2guVGVuc29yLCBnZW5fbG9naXRzOiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgIHJlcGxhY2VfcHJvYjogZmxvYXQgPSAwLjE1KTpcbiAgICBcIlwiXCJTaW11bGF0ZSBFTEVDVFJBIHJlcGxhY2VkIHRva2VuIGRldGVjdGlvbiBkYXRhIGNyZWF0aW9uLlxuICAgIGdlbl9sb2dpdHM6IChCLCBMLCBWKSDigJQgZ2VuZXJhdG9yXHUwMDI3cyB0b2tlbiBkaXN0cmlidXRpb24gYXQgZWFjaCBwb3NpdGlvbi5cbiAgICBSZXR1cm5zIChjb3JydXB0ZWRfaWRzLCBydGRfbGFiZWxzKSB3aGVyZSBydGRfbGFiZWxzOiAwPXJlYWwsIDE9cmVwbGFjZWQuXG4gICAgXCJcIlwiXG4gICAgQiwgTCA9IHRva2VuX2lkcy5zaGFwZVxuICAgIGNvcnJ1cHRlZCA9IHRva2VuX2lkcy5jbG9uZSgpXG4gICAgcnRkX2xhYmVscyA9IHRvcmNoLnplcm9zKEIsIEwsIGR0eXBlPXRvcmNoLmZsb2F0KVxuICAgIHByb2JzID0gdG9yY2guc29mdG1heChnZW5fbG9naXRzLCBkaW09LTEpXG4gICAgZm9yIGIgaW4gcmFuZ2UoQik6XG4gICAgICAgIGZvciBwb3MgaW4gcmFuZ2UoTCk6XG4gICAgICAgICAgICBpZiByYW5kb20ucmFuZG9tKCkgXHUwMDNjIHJlcGxhY2VfcHJvYjpcbiAgICAgICAgICAgICAgICBvcmlnICAgICAgICA9IHRva2VuX2lkc1tiLCBwb3NdLml0ZW0oKVxuICAgICAgICAgICAgICAgIHJlcGxhY2VtZW50ID0gdG9yY2gubXVsdGlub21pYWwocHJvYnNbYiwgcG9zXSwgMSkuaXRlbSgpXG4gICAgICAgICAgICAgICAgaWYgcmVwbGFjZW1lbnQgIT0gb3JpZzpcbiAgICAgICAgICAgICAgICAgICAgY29ycnVwdGVkW2IsIHBvc10gID0gcmVwbGFjZW1lbnRcbiAgICAgICAgICAgICAgICAgICAgcnRkX2xhYmVsc1tiLCBwb3NdID0gMS4wICAgIyBtYXJrIGFzIHJlcGxhY2VkXG4gICAgcmV0dXJuIGNvcnJ1cHRlZCwgcnRkX2xhYmVsc1xuXG5jbGFzcyBSVERIZWFkKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiRGlzY3JpbWluYXRvciBoZWFkOiBiaW5hcnkgY2xhc3NpZmljYXRpb24gYXQgZXZlcnkgdG9rZW4gcG9zaXRpb24uXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmxpbmVhciA9IG5uLkxpbmVhcihkX21vZGVsLCAxKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGhpZGRlbik6IHJldHVybiBzZWxmLmxpbmVhcihoaWRkZW4pLnNxdWVlemUoLTEpICAjIChCLCBMKVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKTsgcmFuZG9tLnNlZWQoMClcbkIsIEwsIFYsIGQgPSAyLCA4LCAxMDAwLCAyNTZcbnRva2VuX2lkcyAgPSB0b3JjaC5yYW5kaW50KDUsIFYsIChCLCBMKSlcbmdlbl9sb2dpdHMgPSB0b3JjaC5yYW5kbihCLCBMLCBWKVxuY29ycnVwdCwgcnRkX2xibCA9IHNpbXVsYXRlX3J0ZCh0b2tlbl9pZHMsIGdlbl9sb2dpdHMpXG5wcmludChcdTAwMjdPcmlnaW5hbDogXHUwMDI3LCB0b2tlbl9pZHNbMF0udG9saXN0KCkpXG5wcmludChcdTAwMjdDb3JydXB0ZWQ6XHUwMDI3LCBjb3JydXB0WzBdLnRvbGlzdCgpKVxucHJpbnQoXHUwMDI3UlREIGxhYmVscyAoMT1yZXBsYWNlZCk6XHUwMDI3LCBydGRfbGJsWzBdLnRvbGlzdCgpKVxuaGVhZCAgICA9IFJUREhlYWQoZClcbmhpZGRlbiAgPSB0b3JjaC5yYW5kbihCLCBMLCBkKVxucnRkX291dCA9IGhlYWQoaGlkZGVuKVxubG9zcyAgICA9IG5uLkJDRVdpdGhMb2dpdHNMb3NzKCkocnRkX291dCwgcnRkX2xibClcbnByaW50KGZcdTAwMjdSVEQgZGlzY3JpbWluYXRvciBsb3NzOiB7bG9zcy5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFbmNvZGVyIE1vZGVscyBDb21wYXJlZCJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIlByZXRyYWluaW5nIE9iamVjdGl2ZSIsIlBhcmFtcyIsIlRva2VucyBTZWVuIiwiR0xVRSBTY29yZSIsIktleSBJbm5vdmF0aW9uIl0sInJvd3MiOltbIkJFUlQtYmFzZSIsIk1MTSArIE5TUCIsIjExME0iLCIxNkIiLCI4MC41IiwiQmlkaXJlY3Rpb25hbCBwcmV0cmFpbiBvbiBsYXJnZSBjb3JwdXMiXSxbIkJFUlQtbGFyZ2UiLCJNTE0gKyBOU1AiLCIzNDBNIiwiMTZCIiwiODIuMSIsIlNjYWxlOiBtb3JlIGxheWVycywgd2lkZXIgbW9kZWwiXSxbIlJvQkVSVGEiLCJNTE0gb25seSAobm8gTlNQKSIsIjEyNU0iLCJ+MlQiLCI4OC41IiwiTG9uZ2VyIHRyYWluaW5nLCBsYXJnZXIgYmF0Y2hlcywgbW9yZSBkYXRhIl0sWyJFTEVDVFJBLWJhc2UiLCJSZXBsYWNlZCBUb2tlbiBEZXRlY3Rpb24iLCIxMTBNIiwiMTI4QiIsIjg4LjgiLCJTYW1wbGUtZWZmaWNpZW50IGRpc2NyaW1pbmF0aXZlIG9iamVjdGl2ZSJdLFsiRGVCRVJUYS1iYXNlIiwiTUxNICsgZGlzZW50YW5nbGVkIGF0dG4iLCIxNDBNIiwiNzhCIiwiOTAuMyIsIlNlcGFyYXRlIHBvc2l0aW9uIGFuZCBjb250ZW50IGF0dGVudGlvbiBrZXlzIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVuY29kZXItb25seSBtb2RlbHMgcmVtYWluIHRoZSB0b3AgY2hvaWNlIGZvciBOTFUgdGFza3Mg4oCUIHRleHQgY2xhc3NpZmljYXRpb24sIE5FUiwgZXh0cmFjdGl2ZSBRQSDigJQgd2hlcmUgdGhlIGZ1bGwgaW5wdXQgaXMga25vd24gYXQgaW5mZXJlbmNlIHRpbWUuIFJvQkVSVGEgaXMgdGhlIHByYWN0aWNhbCBkZWZhdWx0OiBpdCBzaWduaWZpY2FudGx5IG91dHBlcmZvcm1zIG9yaWdpbmFsIEJFUlQgd2l0aCBvbmx5IGEgdHJhaW5pbmcgcmVjaXBlIGNoYW5nZSwgbm8gYXJjaGl0ZWN0dXJlIG1vZGlmaWNhdGlvbi4gRUxFQ1RSQSBpcyB0aGUgYmVzdCBjaG9pY2Ugd2hlbiBjb21wdXRlIGJ1ZGdldCBpcyB0aWdodCwgc2luY2UgaXRzIHNhbXBsZSBlZmZpY2llbmN5IG1lYW5zIGl0IHJlYWNoZXMgUm9CRVJUYS1sZXZlbCBxdWFsaXR5IHdpdGggZmFyIGxlc3MgcHJldHJhaW5pbmcuIERlQkVSVGEgY3VycmVudGx5IGhvbGRzIHRoZSBoaWdoZXN0IEdMVUUgYW5kIFN1cGVyR0xVRSBzY29yZXMgYW1vbmcgZW5jb2Rlci1vbmx5IG1vZGVscywgb3dpbmcgdG8gaXRzIGRpc2VudGFuZ2xlZCBwb3NpdGlvbiBhbmQgY29udGVudCBhdHRlbnRpb24uIn1d"
---
# Encoder-Only Transformers — BERT, RoBERTa, and DeBERTa

Encoder-only Transformers use bidirectional self-attention: every token can attend to every other token in both directions simultaneously. There is no causal mask. This makes encoder models ideal for tasks that require understanding the full context of an input — classification, named entity recognition, question answering, and natural language inference — but they cannot generate text autoregressively. BERT (Devlin et al. 2018) established the encoder-only paradigm and set off a wave of improvements: RoBERTa, ELECTRA, DeBERTa, and many others.

## Bidirectional Attention — Seeing All Tokens

In a standard encoder self-attention layer, the attention score matrix S = QKᵀ / √d_k has no mask applied — all L×L entries are used. This means every position can draw information from every other position, including future tokens. The attention weights form a dense L×L matrix after softmax. Bidirectionality is what makes encoders powerful for understanding tasks: the representation of the word 'bank' can simultaneously look left at 'river' and right at 'deposit' to resolve its meaning.

- Encoder: all positions attend to all others — full L×L attention matrix
- Decoder (causal): position i attends only to j ≤ i — lower-triangular matrix
- Encoder input: [CLS] token + real tokens + [SEP] token (WordPiece tokenised)
- [CLS] representation aggregates the whole-sequence meaning — used for classification
- Padding mask still applied: PAD tokens blocked from receiving attention (key_padding_mask)

> **Why Encoders Cannot Generate Text**: During inference, an autoregressive generator must predict token t given tokens 0 through t-1 without seeing t+1, t+2, … Encoder-only models have no such constraint — they always see the entire input sequence. This makes them excellent understanders but incapable of sequential generation without modification (e.g., adding a causal decoder or using masked-token prediction iteratively).

## Masked Language Modelling — BERT's Pretraining Objective

BERT is pretrained with Masked Language Modelling (MLM): 15% of input tokens are randomly selected. Of those, 80% are replaced with the special [MASK] token, 10% are replaced with a random token from the vocabulary, and 10% are left unchanged. The model is trained to predict the original token at each masked position using cross-entropy loss. This forces the model to build rich contextual representations because predicting a masked word requires understanding its left and right context simultaneously.

## BERT Architecture and Fine-Tuning

BERT-base: 12 layers, 12 attention heads, d_model=768, d_ff=3072, 110M parameters. BERT-large: 24 layers, 16 heads, d_model=1024, d_ff=4096, 340M parameters. Fine-tuning adds a task-specific head on top of the pretrained encoder. For sentence classification, a linear layer maps the [CLS] token representation (shape d_model) to the number of classes. For token-level tasks (NER, POS tagging), a linear head is applied to every token's representation. BERT popularised the pretrain-then-finetune paradigm that now dominates NLP.

## Code 1 — Encoder-Only Transformer Block from Scratch

A bidirectional (no causal mask) Transformer encoder block, showing that all L×L attention weight entries are non-zero.

```python
import torch
import torch.nn as nn

class EncoderBlock(nn.Module):
    """Encoder-only Transformer block: bidirectional self-attention, no causal mask.
    Pre-norm layout (modern variant).
    """
    def __init__(self, d_model: int, n_heads: int, d_ff: int,
                 dropout: float = 0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.attn  = nn.MultiheadAttention(d_model, n_heads,
                                            dropout=dropout, batch_first=True)
        self.ff1   = nn.Linear(d_model, d_ff)
        self.ff2   = nn.Linear(d_ff, d_model)
        self.act   = nn.GELU()
        self.drop  = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor,
                key_padding_mask: torch.Tensor = None):
        # No attn_mask passed -> bidirectional (all positions attend to all)
        n = self.norm1(x)
        a, weights = self.attn(n, n, n, key_padding_mask=key_padding_mask)
        x = x + self.drop(a)
        x = x + self.drop(self.ff2(self.act(self.ff1(self.norm2(x)))))
        return x, weights

# BERT-base dimensions
block = EncoderBlock(d_model=768, n_heads=12, d_ff=3072)
x = torch.randn(2, 12, 768)
out, attn = block(x)
print('Encoder output:', out.shape)          # (2, 12, 768)
print('Attention weights:', attn.shape)      # (2, 12, 12)
print('Non-zero weights:', (attn > 1e-6).sum().item(), '(all positions attend all)')
```

## Code 2 — MLM Data Preparation

Implementing the BERT masking strategy: 15% of tokens selected, 80% replaced with [MASK], 10% random, 10% unchanged. Labels of -100 at non-masked positions are ignored by CrossEntropyLoss.

```python
import torch
import random

def prepare_mlm_batch(token_ids: list, vocab_size: int,
                       mask_token_id: int, mask_prob: float = 0.15,
                       pad_id: int = 0):
    """BERT-style MLM masking.
    Of selected positions: 80% -> [MASK], 10% -> random, 10% -> unchanged.
    Returns (input_ids, labels, attention_mask) as tensors.
    labels[b, pos] = -100 (ignored) for non-masked positions.
    """
    max_len = max(len(s) for s in token_ids)
    inputs, labels, att_masks = [], [], []
    for seq in token_ids:
        ids   = list(seq)
        label = [-100] * max_len
        am    = [1] * len(seq) + [0] * (max_len - len(seq))
        ids  += [pad_id] * (max_len - len(seq))
        for pos in range(len(seq)):
            if random.random() < mask_prob:
                label[pos] = ids[pos]          # store original token as target
                r = random.random()
                if r < 0.80:                   # 80%: replace with [MASK]
                    ids[pos] = mask_token_id
                elif r < 0.90:                 # 10%: replace with random token
                    ids[pos] = random.randint(5, vocab_size - 1)
                # 10%: leave unchanged
        inputs.append(ids); labels.append(label); att_masks.append(am)
    return torch.tensor(inputs), torch.tensor(labels), torch.tensor(att_masks)

random.seed(42)
seqs   = [[101, 2054, 2003, 1996, 3007, 102], [101, 4067, 2024, 4658, 102]]
inp, lbl, am = prepare_mlm_batch(seqs, vocab_size=30000, mask_token_id=103)
print('Input IDs:')
print(inp)
print('Labels (-100 = not masked):')
print(lbl)
```

## Code 3 — BERT Fine-Tuning for Classification

Using HuggingFace transformers to fine-tune BERT for binary classification: a linear head on the [CLS] token representation with AdamW optimiser.

```python
import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer
from torch.optim import AdamW

class BertForSentiment(nn.Module):
    """BERT encoder + linear classification head on the [CLS] token."""
    def __init__(self, n_classes: int = 2, dropout: float = 0.1):
        super().__init__()
        self.bert       = BertModel.from_pretrained('bert-base-uncased')
        self.dropout    = nn.Dropout(dropout)
        self.classifier = nn.Linear(768, n_classes)

    def forward(self, input_ids, attention_mask, token_type_ids=None):
        out = self.bert(input_ids=input_ids,
                        attention_mask=attention_mask,
                        token_type_ids=token_type_ids)
        cls_rep = out.last_hidden_state[:, 0, :]   # [CLS] token at position 0
        return self.classifier(self.dropout(cls_rep))

# Tokenise and run one training step
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
texts     = ['I love this film!', 'The movie was terrible.']
labels    = torch.tensor([1, 0])
enc       = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)

model   = BertForSentiment()
optimr  = AdamW(model.parameters(), lr=2e-5, weight_decay=0.01)
loss_fn = nn.CrossEntropyLoss()

model.train()
logits = model(enc['input_ids'], enc['attention_mask'])
loss   = loss_fn(logits, labels)
loss.backward()
optimr.step()
print('Logits:', logits.detach())
print('Loss:  ', round(loss.item(), 4))
```

## Code 4 — ELECTRA Replaced Token Detection

ELECTRA (Clark et al. 2020) replaces MLM with a discriminative objective: a small generator corrupts tokens, and the discriminator must classify each token as real or replaced. More sample-efficient than MLM because the loss signal covers all tokens, not just the 15% masked.

```python
import torch
import torch.nn as nn
import random

def simulate_rtd(token_ids: torch.Tensor, gen_logits: torch.Tensor,
                 replace_prob: float = 0.15):
    """Simulate ELECTRA replaced token detection data creation.
    gen_logits: (B, L, V) — generator's token distribution at each position.
    Returns (corrupted_ids, rtd_labels) where rtd_labels: 0=real, 1=replaced.
    """
    B, L = token_ids.shape
    corrupted = token_ids.clone()
    rtd_labels = torch.zeros(B, L, dtype=torch.float)
    probs = torch.softmax(gen_logits, dim=-1)
    for b in range(B):
        for pos in range(L):
            if random.random() < replace_prob:
                orig        = token_ids[b, pos].item()
                replacement = torch.multinomial(probs[b, pos], 1).item()
                if replacement != orig:
                    corrupted[b, pos]  = replacement
                    rtd_labels[b, pos] = 1.0   # mark as replaced
    return corrupted, rtd_labels

class RTDHead(nn.Module):
    """Discriminator head: binary classification at every token position."""
    def __init__(self, d_model: int):
        super().__init__()
        self.linear = nn.Linear(d_model, 1)
    def forward(self, hidden): return self.linear(hidden).squeeze(-1)  # (B, L)

torch.manual_seed(0); random.seed(0)
B, L, V, d = 2, 8, 1000, 256
token_ids  = torch.randint(5, V, (B, L))
gen_logits = torch.randn(B, L, V)
corrupt, rtd_lbl = simulate_rtd(token_ids, gen_logits)
print('Original: ', token_ids[0].tolist())
print('Corrupted:', corrupt[0].tolist())
print('RTD labels (1=replaced):', rtd_lbl[0].tolist())
head    = RTDHead(d)
hidden  = torch.randn(B, L, d)
rtd_out = head(hidden)
loss    = nn.BCEWithLogitsLoss()(rtd_out, rtd_lbl)
print(f'RTD discriminator loss: {loss.item():.4f}')
```

## Encoder Models Compared

| Model | Pretraining Objective | Params | Tokens Seen | GLUE Score | Key Innovation |
| --- | --- | --- | --- | --- | --- |
| BERT-base | MLM + NSP | 110M | 16B | 80.5 | Bidirectional pretrain on large corpus |
| BERT-large | MLM + NSP | 340M | 16B | 82.1 | Scale: more layers, wider model |
| RoBERTa | MLM only (no NSP) | 125M | ~2T | 88.5 | Longer training, larger batches, more data |
| ELECTRA-base | Replaced Token Detection | 110M | 128B | 88.8 | Sample-efficient discriminative objective |
| DeBERTa-base | MLM + disentangled attn | 140M | 78B | 90.3 | Separate position and content attention keys |

Encoder-only models remain the top choice for NLU tasks — text classification, NER, extractive QA — where the full input is known at inference time. RoBERTa is the practical default: it significantly outperforms original BERT with only a training recipe change, no architecture modification. ELECTRA is the best choice when compute budget is tight, since its sample efficiency means it reaches RoBERTa-level quality with far less pretraining. DeBERTa currently holds the highest GLUE and SuperGLUE scores among encoder-only models, owing to its disentangled position and content attention.

