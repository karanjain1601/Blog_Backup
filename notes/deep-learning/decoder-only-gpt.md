---
title: "Decoder-Only Transformers — GPT Architecture and Autoregressive LMs"
slug: "decoder-only-gpt"
description: "Deep dive into decoder-only transformer architecture: causal self-attention, GPT-1/2/3 evolution, weight tying, KV cache, and autoregressive sampling strategies."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVjb2Rlci1vbmx5IHRyYW5zZm9ybWVycyBmb3JtIHRoZSBiYWNrYm9uZSBvZiBtb2Rlcm4gbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzLiBVbmxpa2UgZW5jb2Rlci1kZWNvZGVyIGFyY2hpdGVjdHVyZXMsIHRoZXkgcmVseSBzb2xlbHkgb24gY2F1c2FsIChtYXNrZWQpIHNlbGYtYXR0ZW50aW9uIOKAlCBlYWNoIHBvc2l0aW9uIGF0dGVuZHMgb25seSB0byBpdHNlbGYgYW5kIHBvc2l0aW9ucyB0byBpdHMgbGVmdC4gVGhpcyBjb25zdHJhaW50IG1ha2VzIHRoZW0gbmF0dXJhbGx5IHN1aXRlZCBmb3IgYXV0b3JlZ3Jlc3NpdmUgZ2VuZXJhdGlvbjogcHJlZGljdCB0aGUgbmV4dCB0b2tlbiBnaXZlbiBhbGwgcHJldmlvdXMgdG9rZW5zLiBUaGUgR1BUIGZhbWlseSBkZW1vbnN0cmF0ZWQgdGhhdCB0aGlzIHNpbXBsZSBhcmNoaXRlY3R1cmUsIHdoZW4gc2NhbGVkLCBwcm9kdWNlcyBlbWVyZ2VudCBjYXBhYmlsaXRpZXMgcmFuZ2luZyBmcm9tIGNvaGVyZW50IHRleHQgZ2VuZXJhdGlvbiB0byBmZXctc2hvdCBpbi1jb250ZXh0IGxlYXJuaW5nIHdpdGhvdXQgYW55IHRhc2stc3BlY2lmaWMgZmluZS10dW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVjb2Rlci1Pbmx5IEFyY2hpdGVjdHVyZSBPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBkZWNvZGVyLW9ubHkgdHJhbnNmb3JtZXIgZmlyc3QgbWFwcyBlYWNoIHRva2VuIHRvIGEgZGVuc2UgdmVjdG9yIHZpYSBhIHRva2VuIGVtYmVkZGluZyBtYXRyaXggRSDiiIgg4oSdXntWw5dkfSwgdGhlbiBhZGRzIHBvc2l0aW9uYWwgZW1iZWRkaW5ncyBQIOKIiCDihJ1ee1TDl2R9LiBUaGlzIGNvbWJpbmVkIHJlcHJlc2VudGF0aW9uIHBhc3NlcyB0aHJvdWdoIEwgaWRlbnRpY2FsIGJsb2NrcywgZWFjaCBjb250YWluaW5nOiBMYXllck5vcm0g4oaSIENhdXNhbCBNdWx0aS1IZWFkIEF0dGVudGlvbiDihpIgcmVzaWR1YWwgYWRkIOKGkiBMYXllck5vcm0g4oaSIEZlZWQtRm9yd2FyZCBOZXR3b3JrIOKGkiByZXNpZHVhbCBhZGQuIEFmdGVyIEwgYmxvY2tzLCBhIGZpbmFsIExheWVyTm9ybSBwcm9qZWN0cyB0aHJvdWdoIGFuIG91dHB1dCBtYXRyaXggKG9mdGVuIHRpZWQgdG8gRV5UKSB0byBsb2dpdHMgb3ZlciB0aGUgdm9jYWJ1bGFyeS4gUHJlLW5vcm0gcGxhY2VtZW50IChMYXllck5vcm0gYmVmb3JlIGVhY2ggc3VibGF5ZXIpIGlzIHVuaXZlcnNhbCBpbiBtb2Rlcm4gaW1wbGVtZW50YXRpb25zIGZvciB0cmFpbmluZyBzdGFiaWxpdHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR1BUIEZhbWlseTogR1BULTEsIEdQVC0yLCBHUFQtMyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIlBhcmFtcyIsIkxheWVycyIsImRfbW9kZWwiLCJIZWFkcyIsIlRyYWluZWQgVG9rZW5zIiwiQ2FwYWJpbGl0eSBNaWxlc3RvbmUiXSwicm93cyI6W1siR1BULTEgKDIwMTgpIiwiMTE3TSIsIjEyIiwiNzY4IiwiMTIiLCJ+MUIgKEJvb2tzQ29ycHVzKSIsIlN1cGVydmlzZWQgZmluZS10dW5pbmcgYmFzZWxpbmU7IHRyYW5zZmVyIGxlYXJuaW5nIGZvciBOTFAiXSxbIkdQVC0yIHNtYWxsICgyMDE5KSIsIjExN00iLCIxMiIsIjc2OCIsIjEyIiwifjEwQiAoV2ViVGV4dCkiLCJDb2hlcmVudCBtdWx0aS1wYXJhZ3JhcGggZ2VuZXJhdGlvbjsgaW5pdGlhbGx5IHdpdGhoZWxkIl0sWyJHUFQtMiBYTCAoMjAxOSkiLCIxLjVCIiwiNDgiLCIxNjAwIiwiMjUiLCJ+MTBCIChXZWJUZXh0KSIsIlplcm8tc2hvdCB0YXNrIHBlcmZvcm1hbmNlOyBzY2FsaW5nIGRlbW8iXSxbIkdQVC0zICgyMDIwKSIsIjE3NUIiLCI5NiIsIjEyMjg4IiwiOTYiLCJ+MzAwQiB0b2tlbnMiLCJJbi1jb250ZXh0IGxlYXJuaW5nOyBmZXctc2hvdCBwcm9tcHRpbmcgZW1lcmdlcyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhbnNmb3JtZXIgQmxvY2s6IFByZS1Ob3JtIGFuZCBDYXVzYWwgTUhBIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDYXVzYWwgYXR0ZW50aW9uIGVuZm9yY2VzIHRoZSBhdXRvcmVncmVzc2l2ZSBjb25zdHJhaW50IHZpYSBhbiB1cHBlci10cmlhbmd1bGFyIG1hc2s6IHRoZSBhdHRlbnRpb24gd2VpZ2h0IGZyb20gcG9zaXRpb24gaSB0byBwb3NpdGlvbiBqIGlzIHNldCB0byDiiJLiiJ4gYmVmb3JlIHNvZnRtYXggd2hlbmV2ZXIgaiBcdTAwM2UgaS4gQ29tYmluZWQgd2l0aCBwcmUtbm9ybSwgZWFjaCBibG9jayBjb21wdXRlcyB4IOKGkCB4ICsgQXR0bihMTih4KSkgdGhlbiB4IOKGkCB4ICsgRkZOKExOKHgpKS4gVGhlIEZGTiB0eXBpY2FsbHkgdXNlcyBhIDTDlyBleHBhbnNpb24gcmF0aW8gKGRfZmZuID0gNGQpIHdpdGggR0VMVSBhY3RpdmF0aW9uLiBTd2lHTFUgcmVwbGFjZXMgR0VMVSBpbiBMTGFNQSBhbmQgUGFMTTogRkZOKHgpID0gKHhX4oKBIOKKmSBTaUxVKHhXX2dhdGUpKSBX4oKCLCB0cmFkaW5nIG9uZSBtYXRyaXggbXVsdGlwbHkgZm9yIGltcHJvdmVkIHF1YWxpdHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIENhdXNhbFNlbGZBdHRlbnRpb24obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgbl9oZWFkcywgbWF4X2xlbj01MTIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uX2hlYWRzID0gbl9oZWFkc1xuICAgICAgICBzZWxmLmRfaGVhZCA9IGRfbW9kZWwgLy8gbl9oZWFkc1xuICAgICAgICBzZWxmLnFrdiA9IG5uLkxpbmVhcihkX21vZGVsLCAzICogZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFx1MDAyN21hc2tcdTAwMjcsIHRvcmNoLnRyaWwodG9yY2gub25lcyhtYXhfbGVuLCBtYXhfbGVuKSkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgQiwgVCwgQyA9IHguc2hhcGVcbiAgICAgICAgcSwgaywgdiA9IHNlbGYucWt2KHgpLnNwbGl0KEMsIGRpbT0tMSlcbiAgICAgICAgZGVmIHJlc2hhcGUodCk6IHJldHVybiB0LnZpZXcoQiwgVCwgc2VsZi5uX2hlYWRzLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIHEsIGssIHYgPSByZXNoYXBlKHEpLCByZXNoYXBlKGspLCByZXNoYXBlKHYpXG4gICAgICAgIGF0dCA9IChxIEAgay50cmFuc3Bvc2UoLTIsIC0xKSkgKiBzZWxmLmRfaGVhZCAqKiAtMC41XG4gICAgICAgIGF0dCA9IGF0dC5tYXNrZWRfZmlsbChzZWxmLm1hc2tbOlQsIDpUXSA9PSAwLCBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSlcbiAgICAgICAgb3V0ID0gRi5zb2Z0bWF4KGF0dCwgZGltPS0xKSBAIHZcbiAgICAgICAgcmV0dXJuIHNlbGYucHJvaihvdXQudHJhbnNwb3NlKDEsIDIpLmNvbnRpZ3VvdXMoKS52aWV3KEIsIFQsIEMpKVxuXG5jbGFzcyBHUFRCbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsPTc2OCwgbl9oZWFkcz0xMiwgZmZuX211bHQ9NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmxuMSwgc2VsZi5sbjIgPSBubi5MYXllck5vcm0oZF9tb2RlbCksIG5uLkxheWVyTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmF0dG4gPSBDYXVzYWxTZWxmQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMpXG4gICAgICAgIHNlbGYuZmZuID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsICogZmZuX211bHQpLCBubi5HRUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9tb2RlbCAqIGZmbl9tdWx0LCBkX21vZGVsKVxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHggPSB4ICsgc2VsZi5hdHRuKHNlbGYubG4xKHgpKVxuICAgICAgICByZXR1cm4geCArIHNlbGYuZmZuKHNlbGYubG4yKHgpKVxuXG5ibG9jayA9IEdQVEJsb2NrKClcbnggPSB0b3JjaC5yYW5kbigyLCAzMiwgNzY4KVxucHJpbnQoZlx1MDAyN091dHB1dDoge2Jsb2NrKHgpLnNoYXBlfVx1MDAyNykgICMgdG9yY2guU2l6ZShbMiwgMzIsIDc2OF0pXG5wcmludChmXHUwMDI3QmxvY2sgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBibG9jay5wYXJhbWV0ZXJzKCkpOix9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldlaWdodCBUeWluZzogU2hhcmVkIEVtYmVkZGluZyBhbmQgT3V0cHV0IFByb2plY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldlaWdodCB0eWluZyBzZXRzIHRoZSBvdXRwdXQgcHJvamVjdGlvbiBtYXRyaXggZXF1YWwgdG8gdGhlIHRyYW5zcG9zZSBvZiB0aGUgdG9rZW4gZW1iZWRkaW5nIG1hdHJpeDogV19vdXQgPSBFXlQsIHNvIHRoYXQgdGhlIHNhbWUgcGFyYW1ldGVycyBnb3Zlcm4gYm90aCB0b2tlbiBsb29rdXAgYW5kIHZvY2FidWxhcnkgcHJlZGljdGlvbi4gVGhpcyByZWR1Y2VzIHBhcmFtZXRlciBjb3VudCBieSBWw5dkICjiiYgzOE0gZm9yIEdQVC0yIHNtYWxsIHdpdGggVj01MDI1NywgZD03NjgpIGFuZCBlbnN1cmVzIHRoYXQgdGhlIGdlb21ldHJpYyBkaXN0YW5jZXMgaW4gZW1iZWRkaW5nIHNwYWNlIGFyZSBjb25zaXN0ZW50IGJldHdlZW4gaW5wdXQgYW5kIG91dHB1dC4gSXQgYWxzbyByZWd1bGFyaXplcyB0aGUgbW9kZWw6IHRva2VucyB0aGF0IGFwcGVhciBpbiBzaW1pbGFyIGNvbnRleHRzIHdpbGwgaGF2ZSBzaW1pbGFyIGVtYmVkZGluZ3MgYW5kIHNpbWlsYXIgb3V0cHV0IHByb2JhYmlsaXRpZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFRpZWRHUFQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdm9jYWJfc2l6ZT01MDI1NywgZF9tb2RlbD03NjgsIG5fbGF5ZXJzPTEyLFxuICAgICAgICAgICAgICAgICBuX2hlYWRzPTEyLCBtYXhfbGVuPTEwMjQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi50b2tfZW1iID0gbm4uRW1iZWRkaW5nKHZvY2FiX3NpemUsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYucG9zX2VtYiA9IG5uLkVtYmVkZGluZyhtYXhfbGVuLCBkX21vZGVsKVxuICAgICAgICBzZWxmLmJsb2NrcyA9IG5uLk1vZHVsZUxpc3QoW0dQVEJsb2NrKGRfbW9kZWwsIG5faGVhZHMpIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKV0pXG4gICAgICAgIHNlbGYubG5fZiA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmhlYWQgPSBubi5MaW5lYXIoZF9tb2RlbCwgdm9jYWJfc2l6ZSwgYmlhcz1GYWxzZSlcbiAgICAgICAgIyBXZWlnaHQgdHlpbmc6IG91dHB1dCBoZWFkIHNoYXJlcyB3ZWlnaHRzIHdpdGggdG9rZW4gZW1iZWRkaW5nXG4gICAgICAgIHNlbGYuaGVhZC53ZWlnaHQgPSBzZWxmLnRva19lbWIud2VpZ2h0XG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBpZHgpOlxuICAgICAgICBCLCBUID0gaWR4LnNoYXBlXG4gICAgICAgIHBvcyA9IHRvcmNoLmFyYW5nZShULCBkZXZpY2U9aWR4LmRldmljZSlcbiAgICAgICAgeCA9IHNlbGYudG9rX2VtYihpZHgpICsgc2VsZi5wb3NfZW1iKHBvcylcbiAgICAgICAgZm9yIGJsb2NrIGluIHNlbGYuYmxvY2tzOlxuICAgICAgICAgICAgeCA9IGJsb2NrKHgpXG4gICAgICAgIHJldHVybiBzZWxmLmhlYWQoc2VsZi5sbl9mKHgpKSAgIyAoQiwgVCwgdm9jYWJfc2l6ZSlcblxubW9kZWwgPSBUaWVkR1BUKG5fbGF5ZXJzPTIpICAjIHNoYWxsb3cgZm9yIGRlbW9cbnRvdGFsID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpXG51bnRpZWRfdG90YWwgPSB0b3RhbCArIG1vZGVsLnRva19lbWIud2VpZ2h0Lm51bWVsKClcbnByaW50KGZcdTAwMjdQYXJhbXMgd2l0aCB0eWluZzogICAge3RvdGFsOix9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1BhcmFtcyB3aXRob3V0IHR5aW5nOiB7dW50aWVkX3RvdGFsOix9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1NhdmluZ3M6IHt1bnRpZWRfdG90YWwgLSB0b3RhbDosfSAoezEwMCoodW50aWVkX3RvdGFsLXRvdGFsKS91bnRpZWRfdG90YWw6LjFmfSUpXHUwMDI3KVxuYXNzZXJ0IG1vZGVsLmhlYWQud2VpZ2h0LmRhdGFfcHRyKCkgPT0gbW9kZWwudG9rX2VtYi53ZWlnaHQuZGF0YV9wdHIoKSwgXHUwMDI3V2VpZ2h0cyBub3QgdGllZCFcdTAwMjcifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYW5ndWFnZSBNb2RlbGluZyBPYmplY3RpdmUgYW5kIFRyYWluaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdHJhaW5pbmcgb2JqZWN0aXZlIGlzIG5leHQtdG9rZW4gcHJlZGljdGlvbiB2aWEgY3Jvc3MtZW50cm9weSBsb3NzIGFwcGxpZWQgYXQgZXZlcnkgcG9zaXRpb24gc2ltdWx0YW5lb3VzbHkuIEZvciBhIHNlcXVlbmNlIFt44oKBLCB44oKCLCAuLi4sIHhfVF0sIHRoZSBtb2RlbCBwcmVkaWN0cyBQKHjigpwgfCB44oKBLC4uLix44oKc4oKL4oKBKSBmb3IgYWxsIHQgaW4gYSBzaW5nbGUgZm9yd2FyZCBwYXNzICh0ZWFjaGVyIGZvcmNpbmcpLiBUaGUgbG9zcyBpcyBMID0g4oiSKDEvVCkgzqPigpwgbG9nIFAoeOKCnCB8IHhcdTAwM2N0KS4gVGhpcyBwYXJhbGxlbGlzbSBvdmVyIHNlcXVlbmNlIHBvc2l0aW9ucyBpcyBhIGZ1bmRhbWVudGFsIGFkdmFudGFnZSBvdmVyIFJOTnM6IHRoZSBlbnRpcmUgc2VxdWVuY2UgaXMgcHJvY2Vzc2VkIGluIG9uZSBmb3J3YXJkLWJhY2t3YXJkIHBhc3MuIFBlcnBsZXhpdHkgPSBleHAoTCkgaXMgdGhlIHByaW1hcnkgZXZhbHVhdGlvbiBtZXRyaWMg4oCUIGxvd2VyIGlzIGJldHRlciwgd2l0aCB3ZWxsLXRyYWluZWQgbW9kZWxzIGFjaGlldmluZyBwZXJwbGV4aXRpZXMgaW4gdGhlIHNpbmdsZSBkaWdpdHMgb24gaGVsZC1vdXQgZGF0YS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlByZS1Ob3JtIHZzIFBvc3QtTm9ybSIsImNvbnRlbnQiOiJPcmlnaW5hbCBhdHRlbnRpb24gKFZhc3dhbmkgMjAxNykgdXNlZCBwb3N0LW5vcm1hbGl6YXRpb246IHN1YmxheWVyIG91dHB1dCDihpIgcmVzaWR1YWwgYWRkIOKGkiBMYXllck5vcm0uIEdQVC0yIGFuZCBuZWFybHkgYWxsIG1vZGVybiBMTE1zIHN3aXRjaGVkIHRvIHByZS1ub3JtYWxpemF0aW9uOiBMYXllck5vcm0g4oaSIHN1YmxheWVyIOKGkiByZXNpZHVhbCBhZGQuIFByZS1ub3JtIGFsbG93cyBsYXJnZXIgbGVhcm5pbmcgcmF0ZXMgYW5kIHNjYWxlcyBtb3JlIHN0YWJseSB0byBodW5kcmVkcyBvZiBsYXllcnMgYmVjYXVzZSBncmFkaWVudHMgYnlwYXNzIExheWVyTm9ybSB0aHJvdWdoIHRoZSByZXNpZHVhbCBzdHJlYW0uIFBvc3Qtbm9ybSBjYW4gYWNoaWV2ZSBtYXJnaW5hbGx5IGJldHRlciBmaW5hbCBwZXJwbGV4aXR5IGF0IHNtYWxsIHNjYWxlIGJ1dCBkaXZlcmdlcyBtb3JlIGVhc2lseS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBdXRvcmVncmVzc2l2ZSBJbmZlcmVuY2U6IFNhbXBsaW5nIFN0cmF0ZWdpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkR1cmluZyBpbmZlcmVuY2UsIHRoZSBtb2RlbCBnZW5lcmF0ZXMgb25lIHRva2VuIHBlciBzdGVwLiBUaGUgbG9naXRzIHog4oiIIOKEnV5WIGFyZSBjb252ZXJ0ZWQgdG8gcHJvYmFiaWxpdGllcyB2aWEgc29mdG1heCh6L8+EKSB3aGVyZSDPhCBpcyB0ZW1wZXJhdHVyZS4gR3JlZWR5IGRlY29kaW5nIChhcmdtYXgpIGlzIGRldGVybWluaXN0aWMgYnV0IG9mdGVuIHByb2R1Y2VzIHJlcGV0aXRpdmUgdGV4dC4gVG9wLWsgc2FtcGxpbmcgdHJ1bmNhdGVzIHRvIHRoZSBrIGhpZ2hlc3QtcHJvYmFiaWxpdHkgdG9rZW5zOyB0b3AtcCAobnVjbGV1cykgc2FtcGxpbmcgcGlja3MgdGhlIHNtYWxsZXN0IHRva2VuIHNldCB3aG9zZSBjdW11bGF0aXZlIHByb2JhYmlsaXR5IGV4Y2VlZHMgcCDigJQgbW9yZSBhZGFwdGl2ZSB0aGFuIHRvcC1rIHNpbmNlIGl0IHZhcmllcyBzZXQgc2l6ZSBiYXNlZCBvbiB0aGUgZGlzdHJpYnV0aW9uIHNoYXBlLiBCZXN0IHByYWN0aWNlIGlzIHRvcC1wPTAuOSB3aXRoIHRlbXBlcmF0dXJlIGFyb3VuZCAwLjggZm9yIG9wZW4tZW5kZWQgZ2VuZXJhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiB0b3BfcF9maWx0ZXIobG9naXRzLCB0b3BfcD0wLjkpOlxuICAgIHNvcnRlZF9sb2dpdHMsIHNvcnRlZF9pZHggPSB0b3JjaC5zb3J0KGxvZ2l0cywgZGVzY2VuZGluZz1UcnVlKVxuICAgIGN1bV9wcm9icyA9IHNvcnRlZF9sb2dpdHMuc29mdG1heChkaW09LTEpLmN1bXN1bShkaW09LTEpXG4gICAgIyBSZW1vdmUgdG9rZW5zIG9uY2UgY3VtdWxhdGl2ZSBwcm9iYWJpbGl0eSBleGNlZWRzIHRvcF9wXG4gICAgcmVtb3ZlX21hc2sgPSBjdW1fcHJvYnMgLSBzb3J0ZWRfbG9naXRzLnNvZnRtYXgoZGltPS0xKSBcdTAwM2UgdG9wX3BcbiAgICBzb3J0ZWRfbG9naXRzW3JlbW92ZV9tYXNrXSA9IGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpXG4gICAgcmV0dXJuIHRvcmNoLnplcm9zX2xpa2UobG9naXRzKS5zY2F0dGVyXygtMSwgc29ydGVkX2lkeCwgc29ydGVkX2xvZ2l0cylcblxuZGVmIHNhbXBsZV90b2tlbihsb2dpdHMsIHRlbXBlcmF0dXJlPTAuOCwgdG9wX2s9NTAsIHRvcF9wPTAuOSk6XG4gICAgbG9naXRzID0gbG9naXRzLmZsb2F0KCkgLyBtYXgodGVtcGVyYXR1cmUsIDFlLTgpXG4gICAgaWYgdG9wX2sgXHUwMDNlIDA6XG4gICAgICAgIGt0aF92YWwgPSB0b3JjaC50b3BrKGxvZ2l0cywgbWluKHRvcF9rLCBsb2dpdHMuc2l6ZSgtMSkpKVswXVsuLi4sIC0xLCBOb25lXVxuICAgICAgICBsb2dpdHMgPSBsb2dpdHMubWFza2VkX2ZpbGwobG9naXRzIFx1MDAzYyBrdGhfdmFsLCBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSlcbiAgICBpZiB0b3BfcCBcdTAwM2MgMS4wOlxuICAgICAgICBsb2dpdHMgPSB0b3BfcF9maWx0ZXIobG9naXRzLCB0b3BfcClcbiAgICByZXR1cm4gdG9yY2gubXVsdGlub21pYWwoRi5zb2Z0bWF4KGxvZ2l0cywgZGltPS0xKSwgbnVtX3NhbXBsZXM9MSlcblxuIyBDb21wYXJlIGVudHJvcHkgdW5kZXIgZGlmZmVyZW50IHRlbXBlcmF0dXJlc1xudG9yY2gubWFudWFsX3NlZWQoMClcbnZvY2FiX3NpemUsIHNlcV9sZW4gPSAyMDAsIDEwXG5sb2dpdHMgPSB0b3JjaC5yYW5kbih2b2NhYl9zaXplKVxucHJpbnQoZlx1MDAyN3tcdTAwMjdUZW1wXHUwMDI3Olx1MDAzZTZ9ICB7XHUwMDI3RW50cm9weVx1MDAyNzpcdTAwM2U4fSAge1x1MDAyN01heCBQcm9iXHUwMDI3Olx1MDAzZTEwfSAge1x1MDAyN0VmZmVjdGl2ZSBWb2NhYlx1MDAyNzpcdTAwM2UxNX1cdTAwMjcpXG5mb3IgdGVtcCBpbiBbMC4zLCAwLjcsIDEuMCwgMS41LCAyLjBdOlxuICAgIHAgPSBGLnNvZnRtYXgobG9naXRzIC8gdGVtcCwgZGltPS0xKVxuICAgIGVudCA9IC0ocCAqIHAubG9nKCkpLnN1bSgpLml0ZW0oKVxuICAgIGVmZiA9IHRvcmNoLmV4cCh0b3JjaC50ZW5zb3IoZW50KSkuaXRlbSgpXG4gICAgcHJpbnQoZlx1MDAyN3t0ZW1wOlx1MDAzZTYuMWZ9ICB7ZW50Olx1MDAzZTguM2Z9ICB7cC5tYXgoKS5pdGVtKCk6XHUwMDNlMTAuNGZ9ICB7ZWZmOlx1MDAzZTE1LjFmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLViBDYWNoZSBmb3IgRmFzdCBJbmZlcmVuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldpdGhvdXQgYSBjYWNoZSwgZ2VuZXJhdGluZyBUIHRva2VucyByZXF1aXJlcyBPKFTCsikgYXR0ZW50aW9uIGNvbXB1dGF0aW9ucyB0b3RhbC4gV2l0aCBhIEtWIGNhY2hlLCBwcmV2aW91c2x5IGNvbXB1dGVkIEsgYW5kIFYgcHJvamVjdGlvbnMgYXJlIHN0b3JlZCBhbmQgcmV1c2VkOiBlYWNoIG5ldyBzdGVwIGFwcGVuZHMgb25lIHJvdyB0byB0aGUgY2FjaGUgYW5kIHJ1bnMgYXR0ZW50aW9uIG92ZXIgdGhlIGZ1bGwgaGlzdG9yeS4gUGVyLXN0ZXAgY29tcHV0YXRpb24gZHJvcHMgZnJvbSBPKFTDl2QpIHRvIE8oZCkgZm9yIHRoZSBhdHRlbnRpb24g4oCUIHRoZSBib3R0bGVuZWNrIGJlY29tZXMgbWVtb3J5IGJhbmR3aWR0aCByYXRoZXIgdGhhbiBGTE9Qcy4gQ2FjaGUgbWVtb3J5IHBlciBsYXllciBpcyAyIMOXIFQgw5cgZF9tb2RlbCBieXRlcyAoZmxvYXQxNik7IGZvciBhIDE3NUIgbW9kZWwgd2l0aCBUPTQwOTYgdGhhdCBpcyAyIMOXIDQwOTYgw5cgMTIyODggw5cgOTYgbGF5ZXJzIMOXIDIgYnl0ZXMg4omIIDE4IEdCIGp1c3QgZm9yIEtWIGNhY2hlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBLVkNhY2hlQXR0ZW50aW9uKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw9NTEyLCBuX2hlYWRzPTgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uX2hlYWRzID0gbl9oZWFkc1xuICAgICAgICBzZWxmLmRfaGVhZCA9IGRfbW9kZWwgLy8gbl9oZWFkc1xuICAgICAgICBzZWxmLnFrdiA9IG5uLkxpbmVhcihkX21vZGVsLCAzICogZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYua19jYWNoZSA9IHNlbGYudl9jYWNoZSA9IE5vbmVcblxuICAgIGRlZiByZXNldF9jYWNoZShzZWxmKTogc2VsZi5rX2NhY2hlID0gc2VsZi52X2NhY2hlID0gTm9uZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgdXNlX2NhY2hlPUZhbHNlKTpcbiAgICAgICAgQiwgVCwgQyA9IHguc2hhcGVcbiAgICAgICAgcSwgaywgdiA9IHNlbGYucWt2KHgpLnNwbGl0KEMsIGRpbT0tMSlcbiAgICAgICAgZGVmIHNwbGl0KHQpOiByZXR1cm4gdC52aWV3KEIsIFQsIHNlbGYubl9oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICBxLCBrLCB2ID0gc3BsaXQocSksIHNwbGl0KGspLCBzcGxpdCh2KVxuICAgICAgICBpZiB1c2VfY2FjaGUgYW5kIHNlbGYua19jYWNoZSBpcyBub3QgTm9uZTpcbiAgICAgICAgICAgIGsgPSB0b3JjaC5jYXQoW3NlbGYua19jYWNoZSwga10sIGRpbT0yKSAgIyAoQiwgSCwgVF9wYXN0K1QsIGRfaGVhZClcbiAgICAgICAgICAgIHYgPSB0b3JjaC5jYXQoW3NlbGYudl9jYWNoZSwgdl0sIGRpbT0yKVxuICAgICAgICBpZiB1c2VfY2FjaGU6XG4gICAgICAgICAgICBzZWxmLmtfY2FjaGUsIHNlbGYudl9jYWNoZSA9IGsuZGV0YWNoKCksIHYuZGV0YWNoKClcbiAgICAgICAgYXR0ID0gRi5zb2Z0bWF4KChxIEAgay50cmFuc3Bvc2UoLTIsIC0xKSkgKiBzZWxmLmRfaGVhZCAqKiAtMC41LCBkaW09LTEpXG4gICAgICAgIHJldHVybiBzZWxmLnByb2ooKGF0dCBAIHYpLnRyYW5zcG9zZSgxLCAyKS5jb250aWd1b3VzKCkudmlldyhCLCBULCBDKSlcblxuYXR0biA9IEtWQ2FjaGVBdHRlbnRpb24oKVxueF9wcm9tcHQgPSB0b3JjaC5yYW5kbigxLCA4LCA1MTIpICAgIyBwcm9tcHQgb2YgbGVuZ3RoIDhcbmF0dG4oeF9wcm9tcHQsIHVzZV9jYWNoZT1UcnVlKVxucHJpbnQoZlx1MDAyN0NhY2hlIGFmdGVyIHByb21wdDogIGs9e2F0dG4ua19jYWNoZS5zaGFwZX1cdTAwMjcpICAjICgxLCA4LCA4LCA2NClcbmZvciBzdGVwIGluIHJhbmdlKDMpOlxuICAgIGF0dG4odG9yY2gucmFuZG4oMSwgMSwgNTEyKSwgdXNlX2NhY2hlPVRydWUpICAjIGdlbmVyYXRlIG9uZSB0b2tlblxucHJpbnQoZlx1MDAyN0NhY2hlIGFmdGVyIDMgc3RlcHM6IGs9e2F0dG4ua19jYWNoZS5zaGFwZX1cdTAwMjcpICAjICgxLCA4LCAxMSwgNjQpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IERlY29kZXItT25seSBEb21pbmF0ZXMgTW9kZXJuIExMTXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVuY29kZXItZGVjb2RlciBhcmNoaXRlY3R1cmVzIHJlcXVpcmUgc2VwYXJhdGUgZW5jb2RlciBhbmQgZGVjb2RlciBzdGFja3Mg4oCUIG5lYXJseSBkb3VibGUgdGhlIHBhcmFtZXRlcnMgZm9yIHNpbWlsYXIgY2FwYWJpbGl0eS4gRW5jb2Rlci1vbmx5IG1vZGVscyAoQkVSVCkgY2Fubm90IGdlbmVyYXRlIHRleHQgYXV0b3JlZ3Jlc3NpdmVseS4gRGVjb2Rlci1vbmx5IGlzIHRoZSBzaW1wbGVzdCB1bmlmaWVkIGFyY2hpdGVjdHVyZSB3aGVyZSB0aGUgc2FtZSBtb2RlbCBoYW5kbGVzIHByZXRyYWluaW5nLCBzdXBlcnZpc2VkIGZpbmUtdHVuaW5nLCBSTEhGLCBhbmQgemVyby9mZXctc2hvdCBpbmZlcmVuY2UuIEF0IHNjYWxlLCBpbi1jb250ZXh0IGxlYXJuaW5nIGVsaW1pbmF0ZXMgdGhlIG5lZWQgZm9yIHRhc2stc3BlY2lmaWMgZmluZS10dW5pbmcgZm9yIG1hbnkgYXBwbGljYXRpb25zLiBFbXBpcmljYWxseSwgZGVjb2Rlci1vbmx5IG1vZGVscyBjb25zaXN0ZW50bHkgbWF0Y2ggb3IgZXhjZWVkIGVuY29kZXItZGVjb2RlciBtb2RlbHMgYXQgY29tcGFyYWJsZSBjb21wdXRlIG9uY2Ugc2NhbGVkIHBhc3Qgcm91Z2hseSAxMEIgcGFyYW1ldGVycy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNpbmdsZSB1bmlmaWVkIGFyY2hpdGVjdHVyZTogcHJldHJhaW5pbmcsIFNGVCwgUkxIRiwgYW5kIGluZmVyZW5jZSB1c2UgdGhlIHNhbWUgZm9yd2FyZCBwYXNzLiIsIkluLWNvbnRleHQgbGVhcm5pbmc6IEdQVC0zIHNob3dlZCB0aGF0IHRhc2sgc3BlY2lmaWNhdGlvbiB2aWEgcHJvbXB0cyByZXBsYWNlcyBmaW5lLXR1bmluZyBmb3IgbWFueSB0YXNrcy4iLCJTaW1wbGVyIHRyYWluaW5nOiBvbmUgbG9zcyBmdW5jdGlvbiAoTkxMIG92ZXIgYWxsIHBvc2l0aW9ucyksIG5vIGNyb3NzLWF0dGVudGlvbiwgbm8gZW5jb2Rlci1kZWNvZGVyIGFsaWdubWVudC4iLCJLViBjYWNoZSBlZmZpY2llbmN5OiBjYXVzYWwgYXR0ZW50aW9uIGNhY2hlcyBuYXR1cmFsbHkg4oCUIGJpZGlyZWN0aW9uYWwgYXR0ZW50aW9uIChCRVJULXN0eWxlKSBjYW5ub3QuIiwiUHJlZGljdGFibGUgc2NhbGluZzogS2FwbGFuIGFuZCBDaGluY2hpbGxhIHNjYWxpbmcgbGF3cyBhcmUgYmVzdCBjaGFyYWN0ZXJpemVkIGZvciBkZWNvZGVyLW9ubHkgbW9kZWxzLiIsIkluc3RydWN0aW9uIGZvbGxvd2luZzogUkxIRiArIGRlY29kZXItb25seSBpcyBub3cgdGhlIHN0YW5kYXJkIHJlY2lwZSBmb3IgYWxpZ25lZCBMTE1zIChHUFQtNCwgQ2xhdWRlLCBHZW1pbmkpLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Decoder-Only Transformers — GPT Architecture and Autoregressive LMs

Decoder-only transformers form the backbone of modern large language models. Unlike encoder-decoder architectures, they rely solely on causal (masked) self-attention — each position attends only to itself and positions to its left. This constraint makes them naturally suited for autoregressive generation: predict the next token given all previous tokens. The GPT family demonstrated that this simple architecture, when scaled, produces emergent capabilities ranging from coherent text generation to few-shot in-context learning without any task-specific fine-tuning.

## Decoder-Only Architecture Overview

A decoder-only transformer first maps each token to a dense vector via a token embedding matrix E ∈ ℝ^{V×d}, then adds positional embeddings P ∈ ℝ^{T×d}. This combined representation passes through L identical blocks, each containing: LayerNorm → Causal Multi-Head Attention → residual add → LayerNorm → Feed-Forward Network → residual add. After L blocks, a final LayerNorm projects through an output matrix (often tied to E^T) to logits over the vocabulary. Pre-norm placement (LayerNorm before each sublayer) is universal in modern implementations for training stability.

## GPT Family: GPT-1, GPT-2, GPT-3

| Model | Params | Layers | d_model | Heads | Trained Tokens | Capability Milestone |
| --- | --- | --- | --- | --- | --- | --- |
| GPT-1 (2018) | 117M | 12 | 768 | 12 | ~1B (BooksCorpus) | Supervised fine-tuning baseline; transfer learning for NLP |
| GPT-2 small (2019) | 117M | 12 | 768 | 12 | ~10B (WebText) | Coherent multi-paragraph generation; initially withheld |
| GPT-2 XL (2019) | 1.5B | 48 | 1600 | 25 | ~10B (WebText) | Zero-shot task performance; scaling demo |
| GPT-3 (2020) | 175B | 96 | 12288 | 96 | ~300B tokens | In-context learning; few-shot prompting emerges |

## Transformer Block: Pre-Norm and Causal MHA

Causal attention enforces the autoregressive constraint via an upper-triangular mask: the attention weight from position i to position j is set to −∞ before softmax whenever j > i. Combined with pre-norm, each block computes x ← x + Attn(LN(x)) then x ← x + FFN(LN(x)). The FFN typically uses a 4× expansion ratio (d_ffn = 4d) with GELU activation. SwiGLU replaces GELU in LLaMA and PaLM: FFN(x) = (xW₁ ⊙ SiLU(xW_gate)) W₂, trading one matrix multiply for improved quality.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CausalSelfAttention(nn.Module):
    def __init__(self, d_model, n_heads, max_len=512):
        super().__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.register_buffer('mask', torch.tril(torch.ones(max_len, max_len)))

    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=-1)
        def reshape(t): return t.view(B, T, self.n_heads, self.d_head).transpose(1, 2)
        q, k, v = reshape(q), reshape(k), reshape(v)
        att = (q @ k.transpose(-2, -1)) * self.d_head ** -0.5
        att = att.masked_fill(self.mask[:T, :T] == 0, float('-inf'))
        out = F.softmax(att, dim=-1) @ v
        return self.proj(out.transpose(1, 2).contiguous().view(B, T, C))

class GPTBlock(nn.Module):
    def __init__(self, d_model=768, n_heads=12, ffn_mult=4):
        super().__init__()
        self.ln1, self.ln2 = nn.LayerNorm(d_model), nn.LayerNorm(d_model)
        self.attn = CausalSelfAttention(d_model, n_heads)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_model * ffn_mult), nn.GELU(),
            nn.Linear(d_model * ffn_mult, d_model)
        )
    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        return x + self.ffn(self.ln2(x))

block = GPTBlock()
x = torch.randn(2, 32, 768)
print(f'Output: {block(x).shape}')  # torch.Size([2, 32, 768])
print(f'Block params: {sum(p.numel() for p in block.parameters()):,}')
```

## Weight Tying: Shared Embedding and Output Projection

Weight tying sets the output projection matrix equal to the transpose of the token embedding matrix: W_out = E^T, so that the same parameters govern both token lookup and vocabulary prediction. This reduces parameter count by V×d (≈38M for GPT-2 small with V=50257, d=768) and ensures that the geometric distances in embedding space are consistent between input and output. It also regularizes the model: tokens that appear in similar contexts will have similar embeddings and similar output probabilities.

```python
import torch
import torch.nn as nn

class TiedGPT(nn.Module):
    def __init__(self, vocab_size=50257, d_model=768, n_layers=12,
                 n_heads=12, max_len=1024):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = nn.Embedding(max_len, d_model)
        self.blocks = nn.ModuleList([GPTBlock(d_model, n_heads) for _ in range(n_layers)])
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)
        # Weight tying: output head shares weights with token embedding
        self.head.weight = self.tok_emb.weight

    def forward(self, idx):
        B, T = idx.shape
        pos = torch.arange(T, device=idx.device)
        x = self.tok_emb(idx) + self.pos_emb(pos)
        for block in self.blocks:
            x = block(x)
        return self.head(self.ln_f(x))  # (B, T, vocab_size)

model = TiedGPT(n_layers=2)  # shallow for demo
total = sum(p.numel() for p in model.parameters())
untied_total = total + model.tok_emb.weight.numel()
print(f'Params with tying:    {total:,}')
print(f'Params without tying: {untied_total:,}')
print(f'Savings: {untied_total - total:,} ({100*(untied_total-total)/untied_total:.1f}%)')
assert model.head.weight.data_ptr() == model.tok_emb.weight.data_ptr(), 'Weights not tied!'
```

## Language Modeling Objective and Training

The training objective is next-token prediction via cross-entropy loss applied at every position simultaneously. For a sequence [x₁, x₂, ..., x_T], the model predicts P(xₜ | x₁,...,xₜ₋₁) for all t in a single forward pass (teacher forcing). The loss is L = −(1/T) Σₜ log P(xₜ | x<t). This parallelism over sequence positions is a fundamental advantage over RNNs: the entire sequence is processed in one forward-backward pass. Perplexity = exp(L) is the primary evaluation metric — lower is better, with well-trained models achieving perplexities in the single digits on held-out data.

> **Pre-Norm vs Post-Norm**: Original attention (Vaswani 2017) used post-normalization: sublayer output → residual add → LayerNorm. GPT-2 and nearly all modern LLMs switched to pre-normalization: LayerNorm → sublayer → residual add. Pre-norm allows larger learning rates and scales more stably to hundreds of layers because gradients bypass LayerNorm through the residual stream. Post-norm can achieve marginally better final perplexity at small scale but diverges more easily.

## Autoregressive Inference: Sampling Strategies

During inference, the model generates one token per step. The logits z ∈ ℝ^V are converted to probabilities via softmax(z/τ) where τ is temperature. Greedy decoding (argmax) is deterministic but often produces repetitive text. Top-k sampling truncates to the k highest-probability tokens; top-p (nucleus) sampling picks the smallest token set whose cumulative probability exceeds p — more adaptive than top-k since it varies set size based on the distribution shape. Best practice is top-p=0.9 with temperature around 0.8 for open-ended generation.

```python
import torch
import torch.nn.functional as F

def top_p_filter(logits, top_p=0.9):
    sorted_logits, sorted_idx = torch.sort(logits, descending=True)
    cum_probs = sorted_logits.softmax(dim=-1).cumsum(dim=-1)
    # Remove tokens once cumulative probability exceeds top_p
    remove_mask = cum_probs - sorted_logits.softmax(dim=-1) > top_p
    sorted_logits[remove_mask] = float('-inf')
    return torch.zeros_like(logits).scatter_(-1, sorted_idx, sorted_logits)

def sample_token(logits, temperature=0.8, top_k=50, top_p=0.9):
    logits = logits.float() / max(temperature, 1e-8)
    if top_k > 0:
        kth_val = torch.topk(logits, min(top_k, logits.size(-1)))[0][..., -1, None]
        logits = logits.masked_fill(logits < kth_val, float('-inf'))
    if top_p < 1.0:
        logits = top_p_filter(logits, top_p)
    return torch.multinomial(F.softmax(logits, dim=-1), num_samples=1)

# Compare entropy under different temperatures
torch.manual_seed(0)
vocab_size, seq_len = 200, 10
logits = torch.randn(vocab_size)
print(f'{'Temp':>6}  {'Entropy':>8}  {'Max Prob':>10}  {'Effective Vocab':>15}')
for temp in [0.3, 0.7, 1.0, 1.5, 2.0]:
    p = F.softmax(logits / temp, dim=-1)
    ent = -(p * p.log()).sum().item()
    eff = torch.exp(torch.tensor(ent)).item()
    print(f'{temp:>6.1f}  {ent:>8.3f}  {p.max().item():>10.4f}  {eff:>15.1f}')
```

## KV Cache for Fast Inference

Without a cache, generating T tokens requires O(T²) attention computations total. With a KV cache, previously computed K and V projections are stored and reused: each new step appends one row to the cache and runs attention over the full history. Per-step computation drops from O(T×d) to O(d) for the attention — the bottleneck becomes memory bandwidth rather than FLOPs. Cache memory per layer is 2 × T × d_model bytes (float16); for a 175B model with T=4096 that is 2 × 4096 × 12288 × 96 layers × 2 bytes ≈ 18 GB just for KV cache.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class KVCacheAttention(nn.Module):
    def __init__(self, d_model=512, n_heads=8):
        super().__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.k_cache = self.v_cache = None

    def reset_cache(self): self.k_cache = self.v_cache = None

    def forward(self, x, use_cache=False):
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=-1)
        def split(t): return t.view(B, T, self.n_heads, self.d_head).transpose(1, 2)
        q, k, v = split(q), split(k), split(v)
        if use_cache and self.k_cache is not None:
            k = torch.cat([self.k_cache, k], dim=2)  # (B, H, T_past+T, d_head)
            v = torch.cat([self.v_cache, v], dim=2)
        if use_cache:
            self.k_cache, self.v_cache = k.detach(), v.detach()
        att = F.softmax((q @ k.transpose(-2, -1)) * self.d_head ** -0.5, dim=-1)
        return self.proj((att @ v).transpose(1, 2).contiguous().view(B, T, C))

attn = KVCacheAttention()
x_prompt = torch.randn(1, 8, 512)   # prompt of length 8
attn(x_prompt, use_cache=True)
print(f'Cache after prompt:  k={attn.k_cache.shape}')  # (1, 8, 8, 64)
for step in range(3):
    attn(torch.randn(1, 1, 512), use_cache=True)  # generate one token
print(f'Cache after 3 steps: k={attn.k_cache.shape}')  # (1, 8, 11, 64)
```

## Why Decoder-Only Dominates Modern LLMs

Encoder-decoder architectures require separate encoder and decoder stacks — nearly double the parameters for similar capability. Encoder-only models (BERT) cannot generate text autoregressively. Decoder-only is the simplest unified architecture where the same model handles pretraining, supervised fine-tuning, RLHF, and zero/few-shot inference. At scale, in-context learning eliminates the need for task-specific fine-tuning for many applications. Empirically, decoder-only models consistently match or exceed encoder-decoder models at comparable compute once scaled past roughly 10B parameters.

- Single unified architecture: pretraining, SFT, RLHF, and inference use the same forward pass.
- In-context learning: GPT-3 showed that task specification via prompts replaces fine-tuning for many tasks.
- Simpler training: one loss function (NLL over all positions), no cross-attention, no encoder-decoder alignment.
- KV cache efficiency: causal attention caches naturally — bidirectional attention (BERT-style) cannot.
- Predictable scaling: Kaplan and Chinchilla scaling laws are best characterized for decoder-only models.
- Instruction following: RLHF + decoder-only is now the standard recipe for aligned LLMs (GPT-4, Claude, Gemini).

---

