---
title: "Seq2Seq — Encoder, Decoder, and the Attention Bottleneck"
slug: "seq2seq-attention-bridge"
description: "Seq2Seq (Sutskever et al. 2014) encodes a variable-length input into a fixed context vector c = hN then decodes output autoregressively. Covers encoder-decoder LSTM construction, information bottleneck problem, teacher forcing vs scheduled sampling, beam search decoding, BLEU degradation with source length, and coverage mechanism."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2VxdWVuY2UtdG8tc2VxdWVuY2UgKFNlcTJTZXEsIFN1dHNrZXZlciBldCBhbC4gMjAxNCkgbW9kZWxzIG1hcCBhIHZhcmlhYmxlLWxlbmd0aCBpbnB1dCBzZXF1ZW5jZSB4MS4uLnhOIHRvIGEgdmFyaWFibGUtbGVuZ3RoIG91dHB1dCBzZXF1ZW5jZSB5MS4uLnlNLCB3aGVyZSBOIGFuZCBNIGNhbiBkaWZmZXIuIFRoZSBlbmNvZGVyIExTVE0gcmVhZHMgdGhlIHNvdXJjZSBhbmQgY29tcHJlc3NlcyBpdCBpbnRvIGEgZml4ZWQtc2l6ZSBjb250ZXh0IHZlY3RvciBjID0gaE4gKHRoZSBmaW5hbCBoaWRkZW4gc3RhdGUpLiBUaGUgZGVjb2RlciBMU1RNIGdlbmVyYXRlcyB0aGUgdGFyZ2V0IGF1dG9yZWdyZXNzaXZlbHksIGNvbmRpdGlvbmluZyBlYWNoIHN0ZXAgb24gdGhlIGNvbnRleHQgdmVjdG9yIGFuZCBhbGwgcHJldmlvdXNseSBnZW5lcmF0ZWQgdG9rZW5zLiBUaGlzIGZyYW1ld29yayB1bmlmaWVkIG1hY2hpbmUgdHJhbnNsYXRpb24sIHN1bW1hcml6YXRpb24sIGRpYWxvZ3VlLCBhbmQgY29kZSBnZW5lcmF0aW9uIHVuZGVyIG9uZSBhcmNoaXRlY3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRW5jb2Rlci1EZWNvZGVyIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGVuY29kZXIgcHJvY2Vzc2VzIHRoZSBzb3VyY2Ugc2VxdWVuY2UgYW5kIHByb2R1Y2VzIGEgY29udGV4dCB2ZWN0b3I6IChoLCBjKSA9IExTVE1fZW5jKHgxLi4ueE4pLiBUaGUgZGVjb2RlciBpcyBpbml0aWFsaXplZCB3aXRoIHRoaXMgY29udGV4dCDigJQgczAgPSBoLCBjZWxsMCA9IGMg4oCUIGFuZCBnZW5lcmF0ZXMgb3V0cHV0IHRva2VucyBvbmUgYXQgYSB0aW1lOiBhdCBlYWNoIHN0ZXAgdCwgdGhlIGRlY29kZXIgY29tcHV0ZXMgc3QgPSBMU1RNX2RlYyhzdC0xLCB5dC0xLCBjb250ZXh0KSBhbmQgcHJvZHVjZXMgYSBkaXN0cmlidXRpb24gb3ZlciB0aGUgdGFyZ2V0IHZvY2FidWxhcnkgdmlhIGEgbGluZWFyICsgc29mdG1heCBsYXllci4gVGhlIGNvbnRleHQgdmVjdG9yIHRocmVhZHMgdGhyb3VnaCB0aGUgZW50aXJlIGRlY29kZXIgYXMgdGhlIGNvbXByZXNzZWQgcmVwcmVzZW50YXRpb24gb2YgdGhlIHNvdXJjZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgRW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB2b2NhYiwgZW1iLCBoaWQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbWJlZCA9IG5uLkVtYmVkZGluZyh2b2NhYiwgZW1iLCBwYWRkaW5nX2lkeD0wKVxuICAgICAgICBzZWxmLmxzdG0gID0gbm4uTFNUTShlbWIsIGhpZCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCBzcmMpOlxuICAgICAgICBfLCAoaCwgYykgPSBzZWxmLmxzdG0oc2VsZi5lbWJlZChzcmMpKVxuICAgICAgICByZXR1cm4gaCwgYyAgIyBjb250ZXh0OiBmaW5hbCBoaWRkZW4gYW5kIGNlbGwgc3RhdGVcblxuY2xhc3MgRGVjb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB2b2NhYiwgZW1iLCBoaWQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbWJlZCA9IG5uLkVtYmVkZGluZyh2b2NhYiwgZW1iLCBwYWRkaW5nX2lkeD0wKVxuICAgICAgICBzZWxmLmxzdG0gID0gbm4uTFNUTShlbWIsIGhpZCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5mYyAgICA9IG5uLkxpbmVhcihoaWQsIHZvY2FiKVxuICAgIGRlZiBzdGVwKHNlbGYsIHRvaywgaCwgYyk6XG4gICAgICAgIG91dCwgKGgsIGMpID0gc2VsZi5sc3RtKHNlbGYuZW1iZWQodG9rLnVuc3F1ZWV6ZSgxKSksIChoLCBjKSlcbiAgICAgICAgcmV0dXJuIHNlbGYuZmMob3V0LnNxdWVlemUoMSkpLCBoLCBjXG5cbmNsYXNzIFNlcTJTZXEobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgc3YsIHR2LCBlbWIsIGhpZCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVuYyA9IEVuY29kZXIoc3YsIGVtYiwgaGlkKVxuICAgICAgICBzZWxmLmRlYyA9IERlY29kZXIodHYsIGVtYiwgaGlkKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHNyYywgdGd0LCB0Zl9yYXRpbz0wLjUpOlxuICAgICAgICBCLCBUID0gdGd0LnNoYXBlXG4gICAgICAgIFYgPSBzZWxmLmRlYy5mYy5vdXRfZmVhdHVyZXNcbiAgICAgICAgb3V0cyA9IHRvcmNoLnplcm9zKEIsIFQsIFYpXG4gICAgICAgIGgsIGMgPSBzZWxmLmVuYyhzcmMpXG4gICAgICAgIHRvayAgPSB0Z3RbOiwgMF1cbiAgICAgICAgZm9yIHQgaW4gcmFuZ2UoMSwgVCk6XG4gICAgICAgICAgICBsb2dpdCwgaCwgYyA9IHNlbGYuZGVjLnN0ZXAodG9rLCBoLCBjKVxuICAgICAgICAgICAgb3V0c1s6LCB0XSAgPSBsb2dpdFxuICAgICAgICAgICAgdG9rID0gdGd0WzosIHRdIGlmIHRvcmNoLnJhbmQoMSkuaXRlbSgpIFx1MDAzYyB0Zl9yYXRpbyBlbHNlIGxvZ2l0LmFyZ21heCgxKVxuICAgICAgICByZXR1cm4gb3V0c1xuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubW9kZWwgPSBTZXEyU2VxKHN2PTUwMCwgdHY9NTAwLCBlbWI9MzIsIGhpZD02NClcbnNyYyA9IHRvcmNoLnJhbmRpbnQoMSwgNTAwLCAoOCwgMTUpKVxudGd0ID0gdG9yY2gucmFuZGludCgxLCA1MDAsICg4LCAxMikpXG5vdXQgPSBtb2RlbChzcmMsIHRndClcbmhfY3R4LCBjX2N0eCA9IG1vZGVsLmVuYyhzcmMpXG5wcmludChcdTAwMjdTZXEyU2VxIGVuY29kZXItZGVjb2RlcjpcdTAwMjcpXG5wcmludChcdTAwMjcgIHNyYzoge30gIC1cdTAwM2UgY29udGV4dCBoOiB7fSAgYzoge31cdTAwMjcuZm9ybWF0KHR1cGxlKHNyYy5zaGFwZSksIHR1cGxlKGhfY3R4LnNoYXBlKSwgdHVwbGUoY19jdHguc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgdGd0OiB7fSAgLVx1MDAzZSBvdXRwdXQgbG9naXRzOiB7fVx1MDAyNy5mb3JtYXQodHVwbGUodGd0LnNoYXBlKSwgdHVwbGUob3V0LnNoYXBlKSkpXG5wcmludChcdTAwMjcgIFBhcmFtczogezosfVx1MDAyNy5mb3JtYXQoc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgSW5mb3JtYXRpb24gQm90dGxlbmVjayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvbnRleHQgdmVjdG9yIGMgPSBoTiBpcyBhIGZpeGVkLXNpemUgcmVwcmVzZW50YXRpb24gb2YgSCBmbG9hdHMgcmVnYXJkbGVzcyBvZiB0aGUgc291cmNlIGxlbmd0aCBOLiBGb3Igc2hvcnQgc2VxdWVuY2VzIChOIFx1MDAzYyAxNSksIGEgd2VsbC10cmFpbmVkIExTVE0gY2FuIHBhY2sgc3VmZmljaWVudCBpbmZvcm1hdGlvbiBpbnRvIGMuIEZvciBsb25nIHNlcXVlbmNlcyAoTiBcdTAwM2UgMzDigJM1MCksIGNyaXRpY2FsIGluZm9ybWF0aW9uIGlzIGluZXZpdGFibHkgbG9zdCDigJQgdGhlIG1vZGVsIG11c3QgY2hvb3NlIHdoYXQgdG8gY29tcHJlc3MgYW5kIHdoYXQgdG8gZHJvcC4gVGhpcyBib3R0bGVuZWNrIGNhdXNlcyBCTEVVIHNjb3JlIHRvIGRlZ3JhZGUgc2lnbmlmaWNhbnRseSB3aXRoIHNvdXJjZSBsZW5ndGggZm9yIGF0dGVudGlvbi1mcmVlIHNlcTJzZXEgbW9kZWxzLiBCYWhkYW5hdSBhdHRlbnRpb24gKDIwMTUpIHdhcyBpbnRyb2R1Y2VkIHNwZWNpZmljYWxseSB0byBhZGRyZXNzIHRoaXMgYm90dGxlbmVjayBieSBhbGxvd2luZyB0aGUgZGVjb2RlciB0byBkaXJlY3RseSBhY2Nlc3MgZW5jb2RlciBoaWRkZW4gc3RhdGVzIGF0IGVhY2ggZGVjb2Rpbmcgc3RlcC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZWFjaGVyIEZvcmNpbmcgYW5kIFNjaGVkdWxlZCBTYW1wbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRHVyaW5nIHRyYWluaW5nLCB0ZWFjaGVyIGZvcmNpbmcgZmVlZHMgdGhlIGdvbGQgdGFyZ2V0IHRva2VuIHl0LTEgYXMgaW5wdXQgYXQgZWFjaCBkZWNvZGVyIHN0ZXAg4oCUIGV2ZW4gaWYgdGhlIG1vZGVsIHdvdWxkIGhhdmUgcHJlZGljdGVkIGEgZGlmZmVyZW50IHRva2VuLiBUaGlzIHByb3ZpZGVzIGNsZWFuIGdyYWRpZW50cyBhbmQgZmFzdCBjb252ZXJnZW5jZSwgYnV0IGNyZWF0ZXMgYSB0cmFpbi1pbmZlcmVuY2UgbWlzbWF0Y2g6IGF0IGluZmVyZW5jZSwgdGhlIG1vZGVsIHJlY2VpdmVzIGl0cyBvd24gKHBvdGVudGlhbGx5IHdyb25nKSBwcmV2aW91cyBwcmVkaWN0aW9ucy4gVGhpcyBleHBvc3VyZSBiaWFzIGNhdXNlcyBjb21wb3VuZGluZyBlcnJvcnM6IGEgd3JvbmcgcHJlZGljdGlvbiBhdCBzdGVwIHQgY2F1c2VzIHdvcnNlIGlucHV0IGF0IHN0ZXAgdCsxLiBTY2hlZHVsZWQgc2FtcGxpbmcgKEJlbmdpbyBldCBhbC4gMjAxNSkgYnJpZGdlcyB0aGlzIGdhcCBieSBncmFkdWFsbHkgbWl4aW5nIHRlYWNoZXItZm9yY2VkIGFuZCBmcmVlLXJ1bm5pbmcgaW5wdXRzIGR1cmluZyB0cmFpbmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuXG5kZWYgdHJhaW5fc3RyYXRlZ3koc3RyYXRlZ3k9XHUwMDI3dGVhY2hlcl9mb3JjaW5nXHUwMDI3LCBlcG9jaHM9MjUsIFQ9MTIsIFY9MjAsIEg9MzIsIE49MTI4KTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZCg0MilcbiAgICBlbWIgID0gbm4uRW1iZWRkaW5nKFYsIEgpXG4gICAgbHN0bSA9IG5uLkxTVE0oSCwgSCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICBmYyAgID0gbm4uTGluZWFyKEgsIFYpXG4gICAgcGFyYW1zID0gbGlzdChlbWIucGFyYW1ldGVycygpKSArIGxpc3QobHN0bS5wYXJhbWV0ZXJzKCkpICsgbGlzdChmYy5wYXJhbWV0ZXJzKCkpXG4gICAgb3B0ID0gb3B0aW0uQWRhbShwYXJhbXMsIGxyPTFlLTMpXG4gICAgeCA9IHRvcmNoLnJhbmRpbnQoMCwgViwgKE4sIFQpKVxuICAgIHkgPSB0b3JjaC5yYW5kaW50KDAsIFYsIChOLCBUKSlcbiAgICBmb3IgZXAgaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgdGYgPSAoMS4wIGlmIHN0cmF0ZWd5ID09IFx1MDAyN3RlYWNoZXJfZm9yY2luZ1x1MDAyNyBlbHNlXG4gICAgICAgICAgICAgIG1heCgwLjAsIDEuMCAtIGVwIC8gZXBvY2hzKSBpZiBzdHJhdGVneSA9PSBcdTAwMjdzY2hlZHVsZWRfc2FtcGxpbmdcdTAwMjcgZWxzZSAwLjApXG4gICAgICAgIGggPSBjID0gdG9yY2guemVyb3MoMSwgTiwgSClcbiAgICAgICAgdG90YWxfbG9zcyA9IDAuMFxuICAgICAgICBpbnAgPSBlbWIoeFs6LCAwXSlcbiAgICAgICAgZm9yIHQgaW4gcmFuZ2UoVCAtIDEpOlxuICAgICAgICAgICAgb3V0LCAoaCwgYykgPSBsc3RtKGlucC51bnNxdWVlemUoMSksIChoLCBjKSlcbiAgICAgICAgICAgIGxvZ2l0ID0gZmMob3V0LnNxdWVlemUoMSkpXG4gICAgICAgICAgICB0b3RhbF9sb3NzICs9IG5uLkNyb3NzRW50cm9weUxvc3MoKShsb2dpdCwgeVs6LCB0KzFdKVxuICAgICAgICAgICAgaW5wID0gZW1iKHlbOiwgdCsxXSBpZiB0b3JjaC5yYW5kKDEpIFx1MDAzYyB0ZiBlbHNlIGxvZ2l0LmFyZ21heCgxKS5kZXRhY2goKSlcbiAgICAgICAgbG9zcyA9IHRvdGFsX2xvc3MgLyAoVCAtIDEpXG4gICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBoID0gaC5kZXRhY2goKTsgYyA9IGMuZGV0YWNoKCk7IG9wdC5zdGVwKClcbiAgICByZXR1cm4gbG9zcy5pdGVtKClcblxucHJpbnQoXHUwMDI3RGVjb2Rpbmcgc3RyYXRlZ3kgY29tcGFyaXNvbiAoZmluYWwgdHJhaW5pbmcgbG9zcyk6XHUwMDI3KVxuZm9yIHMgaW4gW1x1MDAyN3RlYWNoZXJfZm9yY2luZ1x1MDAyNywgXHUwMDI3c2NoZWR1bGVkX3NhbXBsaW5nXHUwMDI3LCBcdTAwMjdmcmVlX3J1bm5pbmdcdTAwMjddOlxuICAgIHByaW50KFx1MDAyNyAge306IHs6LjRmfVx1MDAyNy5mb3JtYXQocywgdHJhaW5fc3RyYXRlZ3kocykpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJlYW0gU2VhcmNoIERlY29kaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHcmVlZHkgZGVjb2RpbmcgcGlja3MgdGhlIGhpZ2hlc3QtcHJvYmFiaWxpdHkgdG9rZW4gYXQgZWFjaCBzdGVwLiBUaGlzIGlzIG15b3BpYyDigJQgYSBoaWdoLXByb2JhYmlsaXR5IHRva2VuIGF0IHN0ZXAgdCBtYXkgbGVhZCB0byBsb3ctcHJvYmFiaWxpdHkgdG9rZW5zIGF0IGxhdGVyIHN0ZXBzLiBCZWFtIHNlYXJjaCBtYWludGFpbnMgYmVhbV93aWR0aCBjb21wbGV0ZSBoeXBvdGhlc2VzIGF0IGVhY2ggc3RlcCwgZXhwYW5kaW5nIGVhY2ggYW5kIGtlZXBpbmcgdGhlIHRvcC1rIGJ5IGN1bXVsYXRpdmUgbG9nLXByb2JhYmlsaXR5LiBUaGlzIGFwcHJveGltYXRlcyB0aGUgZ2xvYmFsbHkgbW9zdCBwcm9iYWJsZSBzZXF1ZW5jZSB3aXRob3V0IHRoZSBleHBvbmVudGlhbCBjb3N0IG9mIGV4YWN0IHNlYXJjaC4gVHlwaWNhbCBiZWFtIHdpZHRocyBhcmUgNOKAkzEwIGZvciB0cmFuc2xhdGlvbi4gTGVuZ3RoIG5vcm1hbGl6YXRpb24g4oCUIGRpdmlkaW5nIHNjb3JlIGJ5IHNlcXVlbmNlIGxlbmd0aCDigJQgcHJldmVudHMgc2hvcnQgc2VxdWVuY2VzIGZyb20gYmVpbmcgdW5mYWlybHkgcHJlZmVycmVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGJlYW1fc2VhcmNoKHNjb3JlX2ZuLCBzdGFydF90b2ssIGVuZF90b2ssIGJlYW1fd2lkdGg9MywgbWF4X3N0ZXBzPTE1KTpcbiAgICBcIlwiXCJCZWFtIHNlYXJjaDogbWFpbnRhaW4gdG9wLWsgaHlwb3RoZXNlcyBhdCBlYWNoIGRlY29kaW5nIHN0ZXAuXG5cbiAgICBzY29yZV9mbihzZXF1ZW5jZSkgLVx1MDAzZSBsb2ctcHJvYmFiaWxpdHkgdGVuc29yIG92ZXIgdm9jYWJ1bGFyeS5cbiAgICBSZXR1cm5zIChiZXN0X2xvZ19wcm9iLCBiZXN0X3Rva2VuX3NlcXVlbmNlKS5cbiAgICBcIlwiXCJcbiAgICBiZWFtcyA9IFsoMC4wLCBbc3RhcnRfdG9rXSldXG4gICAgY29tcGxldGVkID0gW11cblxuICAgIGZvciBzdGVwIGluIHJhbmdlKG1heF9zdGVwcyk6XG4gICAgICAgIGNhbmRpZGF0ZXMgPSBbXVxuICAgICAgICBmb3IgbG9nX3Byb2IsIHNlcSBpbiBiZWFtczpcbiAgICAgICAgICAgIGlmIHNlcVstMV0gPT0gZW5kX3RvazpcbiAgICAgICAgICAgICAgICBjb21wbGV0ZWQuYXBwZW5kKChsb2dfcHJvYiwgc2VxKSlcbiAgICAgICAgICAgICAgICBjb250aW51ZVxuICAgICAgICAgICAgbmV4dF9scHMgPSBzY29yZV9mbihzZXEpICAgICAgICAgICAgICAgICAgICAgICAgIyAodm9jYWJfc2l6ZSwpIGxvZy1wcm9ic1xuICAgICAgICAgICAgdG9wa192YWxzLCB0b3BrX2lkcyA9IHRvcmNoLnRvcGsobmV4dF9scHMsIGJlYW1fd2lkdGgpXG4gICAgICAgICAgICBmb3IgbHAsIHRvayBpbiB6aXAodG9wa192YWxzLnRvbGlzdCgpLCB0b3BrX2lkcy50b2xpc3QoKSk6XG4gICAgICAgICAgICAgICAgY2FuZGlkYXRlcy5hcHBlbmQoKGxvZ19wcm9iICsgbHAsIHNlcSArIFt0b2tdKSlcbiAgICAgICAgaWYgbm90IGNhbmRpZGF0ZXM6XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYW5kaWRhdGVzLnNvcnQoa2V5PWxhbWJkYSB4OiB4WzBdLCByZXZlcnNlPVRydWUpXG4gICAgICAgIGJlYW1zID0gY2FuZGlkYXRlc1s6YmVhbV93aWR0aF1cblxuICAgIGFsbF9oeXBzID0gY29tcGxldGVkICsgYmVhbXNcbiAgICAjIExlbmd0aC1ub3JtYWxpemU6IGRpdmlkZSBhY2N1bXVsYXRlZCBzY29yZSBieSBzZXF1ZW5jZSBsZW5ndGhcbiAgICBhbGxfaHlwcy5zb3J0KGtleT1sYW1iZGEgeDogeFswXSAvIG1heChsZW4oeFsxXSksIDEpLCByZXZlcnNlPVRydWUpXG4gICAgcmV0dXJuIGFsbF9oeXBzWzBdXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5kZWYgbW9ja19zY29yZXIoc2VxKTpcbiAgICByZXR1cm4gdG9yY2gubG9nX3NvZnRtYXgodG9yY2gucmFuZG4oMTApLCBkaW09MClcblxuYmVzdF9zY29yZSwgYmVzdF9zZXEgPSBiZWFtX3NlYXJjaChtb2NrX3Njb3Jlciwgc3RhcnRfdG9rPTEsIGVuZF90b2s9MiwgYmVhbV93aWR0aD0zKVxucHJpbnQoXHUwMDI3QmVhbSBzZWFyY2ggKHdpZHRoPTMsIG1heF9zdGVwcz0xNSk6XHUwMDI3KVxucHJpbnQoXHUwMDI3ICBCZXN0IHNlcXVlbmNlOiB7fVx1MDAyNy5mb3JtYXQoYmVzdF9zZXEpKVxucHJpbnQoXHUwMDI3ICBMb2ctcHJvYjogezouM2Z9ICBsZW5ndGgtbm9ybSBzY29yZTogezouM2Z9XHUwMDI3LmZvcm1hdChcbiAgICBiZXN0X3Njb3JlLCBiZXN0X3Njb3JlIC8gbWF4KGxlbihiZXN0X3NlcSksIDEpKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCTEVVIFNjb3JlIHZzIFNvdXJjZSBMZW5ndGggQW5hbHlzaXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrIG1hbmlmZXN0cyBlbXBpcmljYWxseSBhcyBhIGRlZ3JhZGF0aW9uIGluIEJMRVUgc2NvcmUgYXMgc291cmNlIGxlbmd0aCBpbmNyZWFzZXMuIEZvciBzaG9ydCBzb3VyY2Ugc2VxdWVuY2VzIChcdTAwM2MgMTUgdG9rZW5zKSB0aGUgZml4ZWQgY29udGV4dCB2ZWN0b3IgY2FwdHVyZXMgdGhlIHNvdXJjZSBhZGVxdWF0ZWx5OyBmb3IgbG9uZ2VyIHNlcXVlbmNlcyAoXHUwMDNlIDMwIHRva2VucykgY3JpdGljYWwgaW5mb3JtYXRpb24gaXMgbG9zdCBkdXJpbmcgY29tcHJlc3Npb24sIGFuZCBCTEVVIGRyb3BzIHNoYXJwbHkuIEJhaGRhbmF1IGF0dGVudGlvbiBlbGltaW5hdGVzIHRoZSBmaXhlZCBib3R0bGVuZWNrIOKAlCBCTEVVIGRlZ3JhZGVzIG11Y2ggbW9yZSBzbG93bHkgd2l0aCBzb3VyY2UgbGVuZ3RoIGJlY2F1c2UgdGhlIGRlY29kZXIgY2FuIGRpcmVjdGx5IHF1ZXJ5IGVuY29kZXIgc3RhdGVzIGF0IGFueSBwb3NpdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBzaW11bGF0ZV9ibGV1X3ZzX2xlbmd0aChuX2J1Y2tldHM9OCwgc2VlZD00Mik6XG4gICAgXCJcIlwiU2ltdWxhdGUgQkxFVSBkZWdyYWRhdGlvbiB3aXRoIHNvdXJjZSBsZW5ndGggZm9yIGF0dGVudGlvbi1mcmVlIHZzIGF0dGVudGlvbiBzZXEyc2VxLlwiXCJcIlxuICAgIHJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyhzZWVkKVxuICAgIGxlbmd0aHMgPSBucC5saW5zcGFjZSg1LCA4MCwgbl9idWNrZXRzKS5hc3R5cGUoaW50KVxuICAgIG5vX2F0dG5fc2NvcmVzID0gW11cbiAgICB3aXRoX2F0dG5fc2NvcmVzID0gW11cblxuICAgIHByaW50KFx1MDAyN1NvdXJjZSBsZW5ndGggdnMgQkxFVSBzY29yZSAoc2ltdWxhdGVkIGJvdHRsZW5lY2sgZWZmZWN0KTpcdTAwMjcpXG4gICAgcHJpbnQoXHUwMDI3ezpcdTAwM2U5fSB7Olx1MDAzZTE2fSB7Olx1MDAzZTE2fSB7Olx1MDAzZTEwfVx1MDAyNy5mb3JtYXQoXHUwMDI3U3JjIGxlblx1MDAyNywgXHUwMDI3Tm8gQXR0ZW50aW9uXHUwMDI3LCBcdTAwMjdXaXRoIEF0dGVudGlvblx1MDAyNywgXHUwMDI3QXR0biBHYWluXHUwMDI3KSlcbiAgICBmb3Igc3JjX2xlbiBpbiBsZW5ndGhzOlxuICAgICAgICBub19hdHRuICAgPSBtYXgoMC4wMywgMC40NSAtIDAuMDA1ICogc3JjX2xlbiArIHJuZy5ub3JtYWwoMCwgMC4wMikpXG4gICAgICAgIHdpdGhfYXR0biA9IG1heCgwLjIwLCAwLjQ1IC0gMC4wMDEgKiBzcmNfbGVuICsgcm5nLm5vcm1hbCgwLCAwLjAyKSlcbiAgICAgICAgbm9fYXR0bl9zY29yZXMuYXBwZW5kKG5vX2F0dG4pXG4gICAgICAgIHdpdGhfYXR0bl9zY29yZXMuYXBwZW5kKHdpdGhfYXR0bilcbiAgICAgICAgcHJpbnQoXHUwMDI3ezpcdTAwM2U5fSB7Olx1MDAzZTE2LjNmfSB7Olx1MDAzZTE2LjNmfSB7Olx1MDAzZSsxMC4zZn1cdTAwMjcuZm9ybWF0KFxuICAgICAgICAgICAgc3JjX2xlbiwgbm9fYXR0biwgd2l0aF9hdHRuLCB3aXRoX2F0dG4gLSBub19hdHRuKSlcblxuICAgIHNob3J0X2F2ZyA9IG5wLm1lYW4obm9fYXR0bl9zY29yZXNbOjNdKVxuICAgIGxvbmdfYXZnICA9IG5wLm1lYW4obm9fYXR0bl9zY29yZXNbLTM6XSlcbiAgICBwcmludChcdTAwMjdcXG5Oby1hdHRuOiBzaG9ydD17Oi4zZn0gbG9uZz17Oi4zZn0gIGRlZ3JhZGF0aW9uPXs6LjJmfXhcdTAwMjcuZm9ybWF0KFxuICAgICAgICBzaG9ydF9hdmcsIGxvbmdfYXZnLCBzaG9ydF9hdmcgLyBtYXgobG9uZ19hdmcsIDAuMDAxKSkpXG5cbnNpbXVsYXRlX2JsZXVfdnNfbGVuZ3RoKCkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkNvdmVyYWdlIE1lY2hhbmlzbSBQcmV2ZW50cyBPdmVyLUF0dGVudGlvbiIsImNvbnRlbnQiOiJCYXNpYyBhdHRlbnRpb24gY2FuIGF0dGVuZCByZXBlYXRlZGx5IHRvIHRoZSBzYW1lIHNvdXJjZSBwb3NpdGlvbnMgd2hpbGUgaWdub3Jpbmcgb3RoZXJzIOKAlCBhIHByb2JsZW0gY2FsbGVkIG92ZXItYXR0ZW50aW9uIG9yIHVuZGVyLWNvdmVyYWdlLiBUaGUgY292ZXJhZ2UgbWVjaGFuaXNtIChUdSBldCBhbC4gMjAxNikgYWRkcyBhIGNvdmVyYWdlIHZlY3RvciB0aGF0IGFjY3VtdWxhdGVzIGF0dGVudGlvbiB3ZWlnaHRzIGFjcm9zcyBhbGwgcHJldmlvdXMgZGVjb2RlciBzdGVwcyBhbmQgcGVuYWxpemVzIHJlLWF0dGVuZGluZyB0byBhbHJlYWR5LWNvdmVyZWQgcG9zaXRpb25zLiBUaGlzIHByb2R1Y2VzIG1vcmUgdW5pZm9ybSBhdHRlbnRpb24gZGlzdHJpYnV0aW9ucyBhbmQgaXMgZXNwZWNpYWxseSBpbXBvcnRhbnQgZm9yIGxvbmcgZG9jdW1lbnRzIHdoZXJlIGV2ZXJ5IHNvdXJjZSBwb3NpdGlvbiBzaG91bGQgY29udHJpYnV0ZSB0byB0aGUgb3V0cHV0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlcTJTZXEgVmFyaWFudHMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG9yaWdpbmFsIHNlcTJzZXEgbW9kZWwgKFN1dHNrZXZlciAyMDE0KSB1c2VkIDQtbGF5ZXIgTFNUTSBlbmNvZGVycyBhbmQgZGVjb2RlcnMgd2l0aCBmaXhlZCBjb250ZXh0IHZlY3RvcnMuIEJhaGRhbmF1IGF0dGVudGlvbiAoMjAxNSkgYWRkZWQgZHluYW1pYyBjb250ZXh0IHZlY3RvcnMgY29tcHV0ZWQgYXQgZWFjaCBkZWNvZGVyIHN0ZXAg4oCUIHRoZSBmaXJzdCBtYWpvciBpbXByb3ZlbWVudC4gTHVvbmcgYXR0ZW50aW9uICgyMDE1KSBzaW1wbGlmaWVkIHRoZSBhdHRlbnRpb24gY29tcHV0YXRpb24gd2l0aCBkb3QtcHJvZHVjdCBzY29yaW5nLiBUaGUgVHJhbnNmb3JtZXIgKDIwMTcpIHJlcGxhY2VkIHJlY3VycmVuY2UgZW50aXJlbHkgd2l0aCBzZWxmLWF0dGVudGlvbiwgZW5hYmxpbmcgZnVsbCBwYXJhbGxlbGl6YXRpb24gYW5kIGJldHRlciBsb25nLXJhbmdlIG1vZGVsaW5nLiBUNSAoMjAyMCkgdW5pZmllZCBhbGwgdGV4dCB0YXNrcyB1bmRlciBhIHRleHQtdG8tdGV4dCBzZXEyc2VxIGZyYW1ld29yay4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJDb250ZXh0IiwiTG9uZyBTZXF1ZW5jZSIsIlBhcmFsbGVsaXphYmxlIiwiVHlwaWNhbCBVc2UiXSwicm93cyI6W1siQmFzaWMgU2VxMlNlcSAoMjAxNCkiLCJGaXhlZCB2ZWN0b3IgYz1oTiIsIlBvb3Ig4oCUIGJvdHRsZW5lY2sgZGVncmFkZXMgQkxFVSBzaGFycGx5IiwiTm8g4oCUIHNlcXVlbnRpYWwiLCJTaG9ydCB0cmFuc2xhdGlvbiwgcHJvb2Ygb2YgY29uY2VwdCJdLFsiQmFoZGFuYXUgQXR0ZW50aW9uICgyMDE1KSIsIkR5bmFtaWMg4oCUIHF1ZXJ5IGVuY29kZXIgYXQgZWFjaCBzdGVwIiwiR29vZCDigJQgbm8gZml4ZWQgYm90dGxlbmVjayIsIk5vIOKAlCBzZXF1ZW50aWFsIGRlY29kZXIiLCJOTVQsIHN1bW1hcml6YXRpb24sIFRUUyJdLFsiTHVvbmcgQXR0ZW50aW9uICgyMDE1KSIsIkRvdC1wcm9kdWN0IGF0dGVudGlvbiBvdmVyIGVuY29kZXIiLCJHb29kIOKAlCBzaW1wbGVyIGNvbXB1dGF0aW9uIiwiTm8g4oCUIHNlcXVlbnRpYWwgZGVjb2RlciIsIk5NVCBiYXNlbGluZSwgZmFzdGVyIHRoYW4gQmFoZGFuYXUiXSxbIlRyYW5zZm9ybWVyICgyMDE3KSIsIlNlbGYtYXR0ZW50aW9uIG92ZXIgYWxsIHBvc2l0aW9ucyIsIlZlcnkgZ29vZCDigJQgTyhuwrIpIGF0dGVudGlvbiIsIlllcyDigJQgZnVsbHkgcGFyYWxsZWwiLCJBbGwgc2VxMnNlcSB0YXNrcywgc3RhbmRhcmQgc2luY2UgMjAxOCJdLFsiVDUgLyBCQVJUICgyMDIwKSIsIkZ1bGwgZW5jb2Rlci1kZWNvZGVyIFRyYW5zZm9ybWVyIiwiVmVyeSBnb29kIHdpdGggcG9zaXRpb24gZW5jb2RpbmciLCJZZXMg4oCUIHBhcmFsbGVsIGVuY29kZXIsIHNlcmlhbCBkZWNvZGVyIiwiVW5pZmllZCB0ZXh0LXRvLXRleHQsIHN1bW1hcml6YXRpb24sIFFBIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFeHBvc3VyZSBCaWFzIGFuZCBDb3ZlcmFnZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXhwb3N1cmUgYmlhcyDigJQgdGhlIG1pc21hdGNoIGJldHdlZW4gdGVhY2hlci1mb3JjZWQgdHJhaW5pbmcgYW5kIGZyZWUtcnVubmluZyBpbmZlcmVuY2Ug4oCUIHJlbWFpbnMgYW4gdW5zb2x2ZWQgcHJvYmxlbSBldmVuIGluIG1vZGVybiBzZXEyc2VxIHN5c3RlbXMuIFNjaGVkdWxlZCBzYW1wbGluZyBtaXRpZ2F0ZXMgYnV0IGRvZXMgbm90IGVsaW1pbmF0ZSBpdC4gU2VxdWVuY2UtbGV2ZWwgdHJhaW5pbmcgb2JqZWN0aXZlcyAoUkVJTkZPUkNFIHdpdGggQkxFVSByZXdhcmQsIG1pbmltdW0gcmlzayB0cmFpbmluZykgZGlyZWN0bHkgb3B0aW1pemUgZm9yIGluZmVyZW5jZS10aW1lIHF1YWxpdHkgYnV0IHN1ZmZlciBmcm9tIGhpZ2ggdmFyaWFuY2UuIEluIHByYWN0aWNlLCB0ZWFjaGVyIGZvcmNpbmcgd2l0aCBiZWFtIHNlYXJjaCBhdCBpbmZlcmVuY2UgcmVtYWlucyB0aGUgc3RhbmRhcmQgcmVjaXBlIGRlc3BpdGUgdGhlIGJpYXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUZWFjaGVyIGZvcmNpbmc6IGZhc3QgY29udmVyZ2VuY2UgYnV0IGV4cG9zdXJlIGJpYXMg4oCUIG1vZGVsIHNlZXMgZ29sZCBoaXN0b3J5LCBub3QgaXRzIG93biBlcnJvcnMuIiwiU2NoZWR1bGVkIHNhbXBsaW5nOiBjdXJyaWN1bHVtIGZyb20gVEYgdG8gZnJlZS1ydW5uaW5nIOKAlCByZWR1Y2VzIGJpYXMgYnV0IGludHJvZHVjZXMgaW5zdGFiaWxpdHkuIiwiUkVJTkZPUkNFOiBvcHRpbWl6ZSBCTEVVIGRpcmVjdGx5IOKAlCB1bmJpYXNlZCBidXQgaGlnaCB2YXJpYW5jZSwgcmVxdWlyZXMgY2FyZWZ1bCBiYXNlbGluZXMuIiwiQmVhbSBzZWFyY2g6IHdpZHRoIDQtMTAgaXMgc3RhbmRhcmQ7IHdpZGVyIGJlYW1zIG9jY2FzaW9uYWxseSBodXJ0IGR1ZSB0byBsYWJlbCBiaWFzLiIsIkxlbmd0aCBwZW5hbHR5OiBhbHBoYT0wLjYtMC44IGluIGxlbmd0aCBub3JtYWxpemF0aW9uIGlzIHN0YW5kYXJkIGZvciB0cmFuc2xhdGlvbi4iLCJDb3ZlcmFnZSBwZW5hbHR5OiBhZGQgbmVnYXRpdmUgbG9nIHN1bSBvZiBhdHRlbnRpb24gd2VpZ2h0cyBiZWxvdyB0aHJlc2hvbGQgdG8gYmVhbSBzY29yZS4iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2VxMnNlcSBmcmFtZXdvcmsgZXN0YWJsaXNoZWQgdGhlIGVuY29kZXItZGVjb2RlciBwYXJhZGlnbSB0aGF0IHVuZGVybGllcyBtb2Rlcm4gbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzLiBUaGUga2V5IGVuZ2luZWVyaW5nIGluc2lnaHQg4oCUIGVuY29kZSBpbnRvIGEgbGF0ZW50IHJlcHJlc2VudGF0aW9uLCBkZWNvZGUgYXV0b3JlZ3Jlc3NpdmVseSBjb25kaXRpb25lZCBvbiB0aGF0IHJlcHJlc2VudGF0aW9uIOKAlCBhcHBlYXJzIGluIEdQVCAoZGVjb2RlciBvbmx5KSwgQkVSVCAoZW5jb2RlciBvbmx5KSwgVDUgYW5kIEJBUlQgKGZ1bGwgZW5jb2Rlci1kZWNvZGVyKS4gVW5kZXJzdGFuZGluZyB0aGUgZml4ZWQtdmVjdG9yIGJvdHRsZW5lY2sgYW5kIGhvdyBhdHRlbnRpb24gcmVzb2x2ZXMgaXQgaXMgZXNzZW50aWFsIGJhY2tncm91bmQgZm9yIHVuZGVyc3RhbmRpbmcgd2h5IHNlbGYtYXR0ZW50aW9uIGJlY2FtZSB0aGUgZG9taW5hbnQgYXJjaGl0ZWN0dXJhbCBwcmltaXRpdmUuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Seq2Seq — Encoder, Decoder, and the Attention Bottleneck

Sequence-to-sequence (Seq2Seq, Sutskever et al. 2014) models map a variable-length input sequence x1...xN to a variable-length output sequence y1...yM, where N and M can differ. The encoder LSTM reads the source and compresses it into a fixed-size context vector c = hN (the final hidden state). The decoder LSTM generates the target autoregressively, conditioning each step on the context vector and all previously generated tokens. This framework unified machine translation, summarization, dialogue, and code generation under one architecture.

## Encoder-Decoder Architecture

The encoder processes the source sequence and produces a context vector: (h, c) = LSTM_enc(x1...xN). The decoder is initialized with this context — s0 = h, cell0 = c — and generates output tokens one at a time: at each step t, the decoder computes st = LSTM_dec(st-1, yt-1, context) and produces a distribution over the target vocabulary via a linear + softmax layer. The context vector threads through the entire decoder as the compressed representation of the source.

```python
import torch
import torch.nn as nn

class Encoder(nn.Module):
    def __init__(self, vocab, emb, hid):
        super().__init__()
        self.embed = nn.Embedding(vocab, emb, padding_idx=0)
        self.lstm  = nn.LSTM(emb, hid, batch_first=True)
    def forward(self, src):
        _, (h, c) = self.lstm(self.embed(src))
        return h, c  # context: final hidden and cell state

class Decoder(nn.Module):
    def __init__(self, vocab, emb, hid):
        super().__init__()
        self.embed = nn.Embedding(vocab, emb, padding_idx=0)
        self.lstm  = nn.LSTM(emb, hid, batch_first=True)
        self.fc    = nn.Linear(hid, vocab)
    def step(self, tok, h, c):
        out, (h, c) = self.lstm(self.embed(tok.unsqueeze(1)), (h, c))
        return self.fc(out.squeeze(1)), h, c

class Seq2Seq(nn.Module):
    def __init__(self, sv, tv, emb, hid):
        super().__init__()
        self.enc = Encoder(sv, emb, hid)
        self.dec = Decoder(tv, emb, hid)
    def forward(self, src, tgt, tf_ratio=0.5):
        B, T = tgt.shape
        V = self.dec.fc.out_features
        outs = torch.zeros(B, T, V)
        h, c = self.enc(src)
        tok  = tgt[:, 0]
        for t in range(1, T):
            logit, h, c = self.dec.step(tok, h, c)
            outs[:, t]  = logit
            tok = tgt[:, t] if torch.rand(1).item() < tf_ratio else logit.argmax(1)
        return outs

torch.manual_seed(0)
model = Seq2Seq(sv=500, tv=500, emb=32, hid=64)
src = torch.randint(1, 500, (8, 15))
tgt = torch.randint(1, 500, (8, 12))
out = model(src, tgt)
h_ctx, c_ctx = model.enc(src)
print('Seq2Seq encoder-decoder:')
print('  src: {}  -> context h: {}  c: {}'.format(tuple(src.shape), tuple(h_ctx.shape), tuple(c_ctx.shape)))
print('  tgt: {}  -> output logits: {}'.format(tuple(tgt.shape), tuple(out.shape)))
print('  Params: {:,}'.format(sum(p.numel() for p in model.parameters())))
```

## The Information Bottleneck

The context vector c = hN is a fixed-size representation of H floats regardless of the source length N. For short sequences (N < 15), a well-trained LSTM can pack sufficient information into c. For long sequences (N > 30–50), critical information is inevitably lost — the model must choose what to compress and what to drop. This bottleneck causes BLEU score to degrade significantly with source length for attention-free seq2seq models. Bahdanau attention (2015) was introduced specifically to address this bottleneck by allowing the decoder to directly access encoder hidden states at each decoding step.

## Teacher Forcing and Scheduled Sampling

During training, teacher forcing feeds the gold target token yt-1 as input at each decoder step — even if the model would have predicted a different token. This provides clean gradients and fast convergence, but creates a train-inference mismatch: at inference, the model receives its own (potentially wrong) previous predictions. This exposure bias causes compounding errors: a wrong prediction at step t causes worse input at step t+1. Scheduled sampling (Bengio et al. 2015) bridges this gap by gradually mixing teacher-forced and free-running inputs during training.

```python
import torch
import torch.nn as nn
import torch.optim as optim

def train_strategy(strategy='teacher_forcing', epochs=25, T=12, V=20, H=32, N=128):
    torch.manual_seed(42)
    emb  = nn.Embedding(V, H)
    lstm = nn.LSTM(H, H, batch_first=True)
    fc   = nn.Linear(H, V)
    params = list(emb.parameters()) + list(lstm.parameters()) + list(fc.parameters())
    opt = optim.Adam(params, lr=1e-3)
    x = torch.randint(0, V, (N, T))
    y = torch.randint(0, V, (N, T))
    for ep in range(epochs):
        tf = (1.0 if strategy == 'teacher_forcing' else
              max(0.0, 1.0 - ep / epochs) if strategy == 'scheduled_sampling' else 0.0)
        h = c = torch.zeros(1, N, H)
        total_loss = 0.0
        inp = emb(x[:, 0])
        for t in range(T - 1):
            out, (h, c) = lstm(inp.unsqueeze(1), (h, c))
            logit = fc(out.squeeze(1))
            total_loss += nn.CrossEntropyLoss()(logit, y[:, t+1])
            inp = emb(y[:, t+1] if torch.rand(1) < tf else logit.argmax(1).detach())
        loss = total_loss / (T - 1)
        opt.zero_grad(); loss.backward(); h = h.detach(); c = c.detach(); opt.step()
    return loss.item()

print('Decoding strategy comparison (final training loss):')
for s in ['teacher_forcing', 'scheduled_sampling', 'free_running']:
    print('  {}: {:.4f}'.format(s, train_strategy(s)))
```

## Beam Search Decoding

Greedy decoding picks the highest-probability token at each step. This is myopic — a high-probability token at step t may lead to low-probability tokens at later steps. Beam search maintains beam_width complete hypotheses at each step, expanding each and keeping the top-k by cumulative log-probability. This approximates the globally most probable sequence without the exponential cost of exact search. Typical beam widths are 4–10 for translation. Length normalization — dividing score by sequence length — prevents short sequences from being unfairly preferred.

```python
import torch

def beam_search(score_fn, start_tok, end_tok, beam_width=3, max_steps=15):
    """Beam search: maintain top-k hypotheses at each decoding step.

    score_fn(sequence) -> log-probability tensor over vocabulary.
    Returns (best_log_prob, best_token_sequence).
    """
    beams = [(0.0, [start_tok])]
    completed = []

    for step in range(max_steps):
        candidates = []
        for log_prob, seq in beams:
            if seq[-1] == end_tok:
                completed.append((log_prob, seq))
                continue
            next_lps = score_fn(seq)                        # (vocab_size,) log-probs
            topk_vals, topk_ids = torch.topk(next_lps, beam_width)
            for lp, tok in zip(topk_vals.tolist(), topk_ids.tolist()):
                candidates.append((log_prob + lp, seq + [tok]))
        if not candidates:
            break
        candidates.sort(key=lambda x: x[0], reverse=True)
        beams = candidates[:beam_width]

    all_hyps = completed + beams
    # Length-normalize: divide accumulated score by sequence length
    all_hyps.sort(key=lambda x: x[0] / max(len(x[1]), 1), reverse=True)
    return all_hyps[0]

torch.manual_seed(0)
def mock_scorer(seq):
    return torch.log_softmax(torch.randn(10), dim=0)

best_score, best_seq = beam_search(mock_scorer, start_tok=1, end_tok=2, beam_width=3)
print('Beam search (width=3, max_steps=15):')
print('  Best sequence: {}'.format(best_seq))
print('  Log-prob: {:.3f}  length-norm score: {:.3f}'.format(
    best_score, best_score / max(len(best_seq), 1)))
```

## BLEU Score vs Source Length Analysis

The information bottleneck manifests empirically as a degradation in BLEU score as source length increases. For short source sequences (< 15 tokens) the fixed context vector captures the source adequately; for longer sequences (> 30 tokens) critical information is lost during compression, and BLEU drops sharply. Bahdanau attention eliminates the fixed bottleneck — BLEU degrades much more slowly with source length because the decoder can directly query encoder states at any position.

```python
import numpy as np

def simulate_bleu_vs_length(n_buckets=8, seed=42):
    """Simulate BLEU degradation with source length for attention-free vs attention seq2seq."""
    rng = np.random.default_rng(seed)
    lengths = np.linspace(5, 80, n_buckets).astype(int)
    no_attn_scores = []
    with_attn_scores = []

    print('Source length vs BLEU score (simulated bottleneck effect):')
    print('{:>9} {:>16} {:>16} {:>10}'.format('Src len', 'No Attention', 'With Attention', 'Attn Gain'))
    for src_len in lengths:
        no_attn   = max(0.03, 0.45 - 0.005 * src_len + rng.normal(0, 0.02))
        with_attn = max(0.20, 0.45 - 0.001 * src_len + rng.normal(0, 0.02))
        no_attn_scores.append(no_attn)
        with_attn_scores.append(with_attn)
        print('{:>9} {:>16.3f} {:>16.3f} {:>+10.3f}'.format(
            src_len, no_attn, with_attn, with_attn - no_attn))

    short_avg = np.mean(no_attn_scores[:3])
    long_avg  = np.mean(no_attn_scores[-3:])
    print('\nNo-attn: short={:.3f} long={:.3f}  degradation={:.2f}x'.format(
        short_avg, long_avg, short_avg / max(long_avg, 0.001)))

simulate_bleu_vs_length()
```

> **Coverage Mechanism Prevents Over-Attention**: Basic attention can attend repeatedly to the same source positions while ignoring others — a problem called over-attention or under-coverage. The coverage mechanism (Tu et al. 2016) adds a coverage vector that accumulates attention weights across all previous decoder steps and penalizes re-attending to already-covered positions. This produces more uniform attention distributions and is especially important for long documents where every source position should contribute to the output.

## Seq2Seq Variants Comparison

The original seq2seq model (Sutskever 2014) used 4-layer LSTM encoders and decoders with fixed context vectors. Bahdanau attention (2015) added dynamic context vectors computed at each decoder step — the first major improvement. Luong attention (2015) simplified the attention computation with dot-product scoring. The Transformer (2017) replaced recurrence entirely with self-attention, enabling full parallelization and better long-range modeling. T5 (2020) unified all text tasks under a text-to-text seq2seq framework.

| Model | Context | Long Sequence | Parallelizable | Typical Use |
| --- | --- | --- | --- | --- |
| Basic Seq2Seq (2014) | Fixed vector c=hN | Poor — bottleneck degrades BLEU sharply | No — sequential | Short translation, proof of concept |
| Bahdanau Attention (2015) | Dynamic — query encoder at each step | Good — no fixed bottleneck | No — sequential decoder | NMT, summarization, TTS |
| Luong Attention (2015) | Dot-product attention over encoder | Good — simpler computation | No — sequential decoder | NMT baseline, faster than Bahdanau |
| Transformer (2017) | Self-attention over all positions | Very good — O(n²) attention | Yes — fully parallel | All seq2seq tasks, standard since 2018 |
| T5 / BART (2020) | Full encoder-decoder Transformer | Very good with position encoding | Yes — parallel encoder, serial decoder | Unified text-to-text, summarization, QA |

## Exposure Bias and Coverage

Exposure bias — the mismatch between teacher-forced training and free-running inference — remains an unsolved problem even in modern seq2seq systems. Scheduled sampling mitigates but does not eliminate it. Sequence-level training objectives (REINFORCE with BLEU reward, minimum risk training) directly optimize for inference-time quality but suffer from high variance. In practice, teacher forcing with beam search at inference remains the standard recipe despite the bias.

- Teacher forcing: fast convergence but exposure bias — model sees gold history, not its own errors.
- Scheduled sampling: curriculum from TF to free-running — reduces bias but introduces instability.
- REINFORCE: optimize BLEU directly — unbiased but high variance, requires careful baselines.
- Beam search: width 4-10 is standard; wider beams occasionally hurt due to label bias.
- Length penalty: alpha=0.6-0.8 in length normalization is standard for translation.
- Coverage penalty: add negative log sum of attention weights below threshold to beam score.

The seq2seq framework established the encoder-decoder paradigm that underlies modern large language models. The key engineering insight — encode into a latent representation, decode autoregressively conditioned on that representation — appears in GPT (decoder only), BERT (encoder only), T5 and BART (full encoder-decoder). Understanding the fixed-vector bottleneck and how attention resolves it is essential background for understanding why self-attention became the dominant architectural primitive.

---

