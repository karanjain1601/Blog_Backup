---
title: "Prefix Tuning — Virtual Token Prepending to Each Layer's KV Cache"
slug: "prefix-tuning"
description: "Prefix tuning (Li & Liang, 2021) prepends learned virtual token vectors to the key and value tensors at every transformer attention layer, giving each layer independent task conditioning while freezing all base model weights."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJvbXB0IHR1bmluZyBwcmVwZW5kcyBsZWFybmVkIHRva2VucyB0byB0aGUgaW5wdXQgZW1iZWRkaW5nIGxheWVyIG9ubHkg4oCUIHRoZXNlIHNvZnQgdG9rZW5zIG11c3QgcHJvcGFnYXRlIHRoZWlyIGluZmx1ZW5jZSB0aHJvdWdoIGFsbCBhdHRlbnRpb24gbGF5ZXJzIHZpYSB0aGUgcmVzaWR1YWwgc3RyZWFtLiBQcmVmaXggdHVuaW5nIChMaSBcdTAwMjYgTGlhbmcsIDIwMjEpIGlzIG1vcmUgZGlyZWN0OiBpdCBwcmVwZW5kcyBsZWFybmVkIHByZWZpeCB2ZWN0b3JzIFBfS15sIGFuZCBQX1ZebCBkaXJlY3RseSB0byB0aGUga2V5IGFuZCB2YWx1ZSBtYXRyaWNlcyBhdCBldmVyeSB0cmFuc2Zvcm1lciBsYXllciBsLiBUaGlzIGdpdmVzIGV2ZXJ5IGxheWVyIGluZGVwZW5kZW50LCBkaXJlY3QgY29udHJvbCBvdmVyIGF0dGVudGlvbiBwYXR0ZXJucyByZWdhcmRsZXNzIG9mIGhvdyBpbmZvcm1hdGlvbiBmbG93cyB0aHJvdWdoIGludGVybWVkaWF0ZSBsYXllcnMuIFRoZSBwcmVmaXggdmVjdG9ycyBhcmUgdGhlIG9ubHkgdHJhaW5hYmxlIHBhcmFtZXRlcnM7IGFsbCB0cmFuc2Zvcm1lciB3ZWlnaHRzIHJlbWFpbiBmcm96ZW4uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJlZml4IHZzIFByb21wdCBUdW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByb21wdCB0dW5pbmcgYWRkcyBQIHRva2VucyB0byB0aGUgaW5wdXQgZW1iZWRkaW5nLiBUaGVzZSB0b2tlbnMgYXR0ZW5kIHRvIGFjdHVhbCBjb250ZW50IHRva2VucyBidXQgYXJlIHRoZW1zZWx2ZXMgYXR0ZW5kZWQgdG8gb25seSBhdCBsYXRlciBsYXllcnMgdGhyb3VnaCB0aGUgcmVzaWR1YWwuIFByZWZpeCB0dW5pbmcgYWRkcyBQX0sgYW5kIFBfViB2ZWN0b3JzIGRpcmVjdGx5IHRvIHRoZSBLIGFuZCBWIG1hdHJpY2VzIG9mIGV2ZXJ5IGF0dGVudGlvbiBsYXllci4gVGhlIGNvbnRlbnQgdG9rZW5zIGNhbiBhdHRlbmQgdG8gdGhlIHByZWZpeCBhdCBldmVyeSBsYXllciDigJQgbXVjaCBzdHJvbmdlciBhbmQgbW9yZSBkaXJlY3QgY29uZGl0aW9uaW5nLiBUaGUgY29zdCBpcyBwcm9wb3J0aW9uYWxseSBtb3JlIHBhcmFtZXRlcnMgKG9uZSBwcmVmaXggcGFpciBwZXIgbGF5ZXIgdnMgb25lIGVtYmVkZGluZyBibG9jaykgYW5kIFAgY29uc3VtZWQgY29udGV4dCBwb3NpdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJlZml4IFR1bmluZyBGb3J3YXJkIFBhc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhbiBhdHRlbnRpb24gbGF5ZXIgd2l0aCBoZWFkIGRpbWVuc2lvbiBkX2hlYWQgYW5kIFAgcHJlZml4IHRva2VucywgdGhlIGtleSBtYXRyaXggYmVjb21lcyBLID0gY29uY2F0KFtQX0ssIEtfaW5wdXRdKSDiiIgg4oSdXnsoUCtUKcOXZF9oZWFkfSBhbmQgc2ltaWxhcmx5IFYgPSBjb25jYXQoW1BfViwgVl9pbnB1dF0pIOKIiCDihJ1eeyhQK1Qpw5dkX2hlYWR9LCB3aGVyZSBUIGlzIHRoZSBzZXF1ZW5jZSBsZW5ndGguIFRoZSBxdWVyeSBRIOKIiCDihJ1ee1TDl2RfaGVhZH0gYXR0ZW5kcyBvdmVyIGFsbCBQK1QgcG9zaXRpb25zLiBDYXVzYWwgbWFza2luZyBpcyBhcHBsaWVkIG9ubHkgdG8gdGhlIGlucHV0IHRva2VuIHBvc2l0aW9uczsgcHJlZml4IHRva2VucyBhcmUgYWx3YXlzIHZpc2libGUgdG8gYWxsIGlucHV0IHBvc2l0aW9ucyAobGlrZSBhIHByZWZpeCB0aGF0IHByZWRhdGVzIHRoZSBzZXF1ZW5jZSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5jbGFzcyBQcmVmaXhBdHRlbnRpb25MYXllcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlNpbmdsZSBtdWx0aS1oZWFkIGF0dGVudGlvbiBsYXllciB3aXRoIHByZWZpeCB0dW5pbmcuXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbDogaW50LCBuX2hlYWRzOiBpbnQsIHByZWZpeF9sZW46IGludCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5faGVhZHMgPSBuX2hlYWRzXG4gICAgICAgIHNlbGYuZF9oZWFkID0gZF9tb2RlbCAvLyBuX2hlYWRzXG4gICAgICAgIHNlbGYucHJlZml4X2xlbiA9IHByZWZpeF9sZW5cbiAgICAgICAgc2VsZi5XX3EgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XX2sgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XX3YgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XX28gPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgIyBMZWFybmFibGUgcHJlZml4IGtleSBhbmQgdmFsdWUgdmVjdG9ycyAob25lIHBlciBoZWFkKVxuICAgICAgICBzZWxmLnByZWZpeF9rID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKDEsIHByZWZpeF9sZW4sIGRfbW9kZWwpICogMC4wMilcbiAgICAgICAgc2VsZi5wcmVmaXhfdiA9IG5uLlBhcmFtZXRlcih0b3JjaC5yYW5kbigxLCBwcmVmaXhfbGVuLCBkX21vZGVsKSAqIDAuMDIpXG4gICAgICAgICMgRnJlZXplIGFsbCBub24tcHJlZml4IHBhcmFtc1xuICAgICAgICBmb3IgcCBpbiBbc2VsZi5XX3Eud2VpZ2h0LCBzZWxmLldfay53ZWlnaHQsIHNlbGYuV192LndlaWdodCwgc2VsZi5XX28ud2VpZ2h0XTpcbiAgICAgICAgICAgIHAucmVxdWlyZXNfZ3JhZF8oRmFsc2UpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBCLCBULCBEID0geC5zaGFwZVxuICAgICAgICBRID0gc2VsZi5XX3EoeCkucmVzaGFwZShCLCBULCBzZWxmLm5faGVhZHMsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgS19pbnB1dCA9IHNlbGYuV19rKHgpLnJlc2hhcGUoQiwgVCwgc2VsZi5uX2hlYWRzLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIFZfaW5wdXQgPSBzZWxmLldfdih4KS5yZXNoYXBlKEIsIFQsIHNlbGYubl9oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICAjIEV4cGFuZCBwcmVmaXggSyBhbmQgViB0byBtYXRjaCBiYXRjaCBhbmQgcmVzaGFwZSBmb3IgaGVhZHNcbiAgICAgICAgUF9LID0gc2VsZi5XX2soc2VsZi5wcmVmaXhfay5leHBhbmQoQiwgLTEsIC0xKSkucmVzaGFwZShCLCBzZWxmLnByZWZpeF9sZW4sIHNlbGYubl9oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICBQX1YgPSBzZWxmLldfdihzZWxmLnByZWZpeF92LmV4cGFuZChCLCAtMSwgLTEpKS5yZXNoYXBlKEIsIHNlbGYucHJlZml4X2xlbiwgc2VsZi5uX2hlYWRzLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIEsgPSB0b3JjaC5jYXQoW1BfSywgS19pbnB1dF0sIGRpbT0yKSAgIyAoQiwgSCwgUCtULCBkX2hlYWQpXG4gICAgICAgIFYgPSB0b3JjaC5jYXQoW1BfViwgVl9pbnB1dF0sIGRpbT0yKVxuICAgICAgICBzY2FsZSA9IG1hdGguc3FydChzZWxmLmRfaGVhZClcbiAgICAgICAgYXR0biA9IHRvcmNoLnNvZnRtYXgoUSBAIEsudHJhbnNwb3NlKC0yLCAtMSkgLyBzY2FsZSwgZGltPS0xKVxuICAgICAgICBvdXQgPSAoYXR0biBAIFYpLnRyYW5zcG9zZSgxLCAyKS5yZXNoYXBlKEIsIFQsIEQpXG4gICAgICAgIHJldHVybiBzZWxmLldfbyhvdXQpXG5cbmxheWVyID0gUHJlZml4QXR0ZW50aW9uTGF5ZXIoZF9tb2RlbD02NCwgbl9oZWFkcz00LCBwcmVmaXhfbGVuPTEwKVxueCA9IHRvcmNoLnJhbmRuKDIsIDgsIDY0KVxucHJpbnQoZlx1MDAyN091dHB1dCBzaGFwZToge2xheWVyKHgpLnNoYXBlfVx1MDAyNylcbnRyYWluYWJsZSA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbGF5ZXIucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZClcbnByaW50KGZcdTAwMjdUcmFpbmFibGUgcHJlZml4IHBhcmFtczoge3RyYWluYWJsZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTUxQIFJlcGFyYW1ldGVyaXphdGlvbiBmb3IgVHJhaW5pbmcgU3RhYmlsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMaSBcdTAwMjYgTGlhbmcgZm91bmQgdGhhdCBkaXJlY3RseSBvcHRpbWl6aW5nIHRoZSBwcmVmaXggdmVjdG9ycyBQX0sgYW5kIFBfViBpcyB1bnN0YWJsZSDigJQgdGhlIHByZWZpeCB0ZW5kcyB0byBjb2xsYXBzZSB0byBhIGRlZ2VuZXJhdGUgc29sdXRpb24gaW4gZWFybHkgdHJhaW5pbmcuIFRvIHN0YWJpbGl6ZSwgdGhleSBwcm9wb3NlIHJlcGFyYW1ldGVyaXphdGlvbjogdGhlIGFjdHVhbCBwcmVmaXggdmVjdG9ycyBhcmUgcHJvZHVjZWQgYnkgYSBzbWFsbCBNTFAgdGhhdCB0YWtlcyBhIGNvbXBhY3Qgc2V0IG9mIGZyZWUgcGFyYW1ldGVycyBhcyBpbnB1dC4gQWZ0ZXIgdHJhaW5pbmcsIHRoZSBNTFAgaXMgZGlzY2FyZGVkIGFuZCBvbmx5IHRoZSBvdXRwdXQgcHJlZml4IHZlY3RvcnMgKHRoZSBmaXhlZC1wb2ludCBvZiB0aGUgTUxQKSBhcmUgc3RvcmVkLiBUaGlzIHJlcGFyYW1ldGVyaXphdGlvbiBpcyB1c2VkIG9ubHkgZHVyaW5nIHRyYWluaW5nOyBhdCBpbmZlcmVuY2UsIHRoZSBwcmVmaXggdmVjdG9ycyBhcmUgbWF0ZXJpYWxpemVkIGFuZCBjYWNoZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cblxuY2xhc3MgUHJlZml4TUxQKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTUxQIHJlcGFyYW1ldGVyaXphdGlvbiBmb3IgcHJlZml4IHR1bmluZyAodXNlZCBvbmx5IGR1cmluZyB0cmFpbmluZykuXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgcHJlZml4X2xlbjogaW50LCBkX21vZGVsOiBpbnQsIG5fbGF5ZXJzOiBpbnQsXG4gICAgICAgICAgICAgICAgIGJvdHRsZW5lY2tfZGltOiBpbnQgPSA1MTIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5wcmVmaXhfbGVuID0gcHJlZml4X2xlblxuICAgICAgICBzZWxmLmRfbW9kZWwgPSBkX21vZGVsXG4gICAgICAgIHNlbGYubl9sYXllcnMgPSBuX2xheWVyc1xuICAgICAgICAjIEZyZWUgcGFyYW1ldGVyczogY29tcGFjdCBlbWJlZGRpbmcgZm9yIGVhY2ggcHJlZml4IHBvc2l0aW9uXG4gICAgICAgIHNlbGYuZnJlZV9wYXJhbXMgPSBubi5QYXJhbWV0ZXIoXG4gICAgICAgICAgICB0b3JjaC5yYW5kbihwcmVmaXhfbGVuLCBib3R0bGVuZWNrX2RpbSkgKiAwLjAxXG4gICAgICAgIClcbiAgICAgICAgIyBNTFAgdGhhdCBleHBhbmRzIGZyZWUgcGFyYW1zIHRvIGZ1bGwgcHJlZml4IEsgYW5kIFYgZm9yIGVhY2ggbGF5ZXJcbiAgICAgICAgc2VsZi5tbHAgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGJvdHRsZW5lY2tfZGltLCBib3R0bGVuZWNrX2RpbSAqIDIpLFxuICAgICAgICAgICAgbm4uVGFuaCgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGJvdHRsZW5lY2tfZGltICogMiwgbl9sYXllcnMgKiAyICogZF9tb2RlbCksICAjIEsgYW5kIFYgcGVyIGxheWVyXG4gICAgICAgIClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBcIlwiXCJSZXR1cm5zIHByZWZpeCB0ZW5zb3Igb2Ygc2hhcGUgKG5fbGF5ZXJzLCAyLCBwcmVmaXhfbGVuLCBkX21vZGVsKS5cIlwiXCJcbiAgICAgICAgb3V0ID0gc2VsZi5tbHAoc2VsZi5mcmVlX3BhcmFtcykgICMgKHByZWZpeF9sZW4sIG5fbGF5ZXJzKjIqZF9tb2RlbClcbiAgICAgICAgb3V0ID0gb3V0LnZpZXcoc2VsZi5wcmVmaXhfbGVuLCBzZWxmLm5fbGF5ZXJzLCAyLCBzZWxmLmRfbW9kZWwpXG4gICAgICAgIHJldHVybiBvdXQucGVybXV0ZSgxLCAyLCAwLCAzKSAgIyAobl9sYXllcnMsIDIsIHByZWZpeF9sZW4sIGRfbW9kZWwpXG5cbiAgICBkZWYgbWF0ZXJpYWxpemUoc2VsZikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIFwiXCJcIkNhbGwgYWZ0ZXIgdHJhaW5pbmcgdG8gZXh0cmFjdCBmaXhlZCBwcmVmaXggKE1MUCBubyBsb25nZXIgbmVlZGVkKS5cIlwiXCJcbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICByZXR1cm4gc2VsZigpXG5cbiMgVHJhaW5pbmcgc2V0dXBcbnByZWZpeF9tbHAgPSBQcmVmaXhNTFAocHJlZml4X2xlbj0yMCwgZF9tb2RlbD03NjgsIG5fbGF5ZXJzPTEyLCBib3R0bGVuZWNrX2RpbT0yNTYpXG5vcHRpbWl6ZXIgPSBvcHRpbS5BZGFtVyhwcmVmaXhfbWxwLnBhcmFtZXRlcnMoKSwgbHI9NWUtMylcbnByZWZpeGVzID0gcHJlZml4X21scCgpXG5wcmludChmXHUwMDI3UHJlZml4IHRlbnNvciBzaGFwZToge3ByZWZpeGVzLnNoYXBlfVx1MDAyNykgICMgKDEyIGxheWVycywgMiBmb3IgSy9WLCAyMCB0b2tlbnMsIDc2OCBkaW0pXG5wcmludChmXHUwMDI3TUxQIHRyYWluYWJsZSBwYXJhbXM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIHByZWZpeF9tbHAucGFyYW1ldGVycygpKTosfVx1MDAyNylcbm1hdGVyaWFsaXplZCA9IHByZWZpeF9tbHAubWF0ZXJpYWxpemUoKVxucHJpbnQoZlx1MDAyN01hdGVyaWFsaXplZCBwcmVmaXg6IHttYXRlcmlhbGl6ZWQuc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZ1bGwgTW9kZWwgd2l0aCBQcmVmaXggSW5qZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGNvbXBsZXRlIHByZWZpeC10dW5lZCBMTE0gd3JhcHMgdGhlIGJhc2UgdHJhbnNmb3JtZXIgdG8gaW50ZXJjZXB0IGVhY2ggYXR0ZW50aW9uIGxheWVyXHUwMDI3cyBrZXkgYW5kIHZhbHVlIGNvbXB1dGF0aW9uLiBUaGUgd3JhcHBlciBzdG9yZXMgcHJlZml4IHZlY3RvcnMgaW5kZXhlZCBieSBsYXllciBudW1iZXIgYW5kIGluamVjdHMgdGhlbSBkdXJpbmcgdGhlIGZvcndhcmQgcGFzcy4gQWxsIGJhc2UgbW9kZWwgcGFyYW1ldGVycyBoYXZlIHJlcXVpcmVzX2dyYWQ9RmFsc2U7IG9ubHkgdGhlIHByZWZpeCBwYXJhbWV0ZXJzIGFyZSBvcHRpbWl6ZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHR5cGluZyBpbXBvcnQgT3B0aW9uYWxcblxuY2xhc3MgUHJlZml4VHVuZWRNb2RlbChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIldyYXBzIGEgdHJhbnNmb3JtZXIgdG8gaW5qZWN0IHBlci1sYXllciBwcmVmaXggdmVjdG9ycy5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBiYXNlX21vZGVsOiBubi5Nb2R1bGUsIG5fbGF5ZXJzOiBpbnQsXG4gICAgICAgICAgICAgICAgIGRfbW9kZWw6IGludCwgcHJlZml4X2xlbjogaW50ID0gMjApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5iYXNlID0gYmFzZV9tb2RlbFxuICAgICAgICBzZWxmLnByZWZpeF9sZW4gPSBwcmVmaXhfbGVuXG4gICAgICAgICMgRnJlZXplIGFsbCBiYXNlIG1vZGVsIHBhcmFtZXRlcnNcbiAgICAgICAgZm9yIHBhcmFtIGluIHNlbGYuYmFzZS5wYXJhbWV0ZXJzKCk6XG4gICAgICAgICAgICBwYXJhbS5yZXF1aXJlc19ncmFkXyhGYWxzZSlcbiAgICAgICAgIyBMZWFybmFibGUgcHJlZml4IEsgYW5kIFYgZm9yIGV2ZXJ5IGxheWVyIChzaGFwZTogW25fbGF5ZXJzLCAyLCBQLCBkX21vZGVsXSlcbiAgICAgICAgc2VsZi5wcmVmaXggPSBubi5QYXJhbWV0ZXIoXG4gICAgICAgICAgICB0b3JjaC56ZXJvcyhuX2xheWVycywgMiwgcHJlZml4X2xlbiwgZF9tb2RlbClcbiAgICAgICAgKVxuICAgICAgICBubi5pbml0Lm5vcm1hbF8oc2VsZi5wcmVmaXgsIHN0ZD0wLjAyKVxuXG4gICAgZGVmIGdldF9wcmVmaXhfa3Yoc2VsZiwgbGF5ZXJfaWR4OiBpbnQpOlxuICAgICAgICBcIlwiXCJSZXR1cm4gKHByZWZpeF9LLCBwcmVmaXhfVikgZm9yIGEgZ2l2ZW4gbGF5ZXIuXCJcIlwiXG4gICAgICAgIHJldHVybiBzZWxmLnByZWZpeFtsYXllcl9pZHgsIDBdLCBzZWxmLnByZWZpeFtsYXllcl9pZHgsIDFdXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBpbnB1dF9pZHM6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICBhdHRlbnRpb25fbWFzazogT3B0aW9uYWxbdG9yY2guVGVuc29yXSA9IE5vbmUpOlxuICAgICAgICAjIFByZXBlbmQgcHJlZml4IGF0dGVudGlvbiBtYXNrIChhbGwgb25lcyDigJQgcHJlZml4IGlzIGFsd2F5cyB2aXNpYmxlKVxuICAgICAgICBCID0gaW5wdXRfaWRzLnNoYXBlWzBdXG4gICAgICAgIGlmIGF0dGVudGlvbl9tYXNrIGlzIG5vdCBOb25lOlxuICAgICAgICAgICAgcHJlZml4X21hc2sgPSB0b3JjaC5vbmVzKEIsIHNlbGYucHJlZml4X2xlbiwgZGV2aWNlPWlucHV0X2lkcy5kZXZpY2UpXG4gICAgICAgICAgICBhdHRlbnRpb25fbWFzayA9IHRvcmNoLmNhdChbcHJlZml4X21hc2ssIGF0dGVudGlvbl9tYXNrXSwgZGltPTEpXG4gICAgICAgIHJldHVybiBzZWxmLmJhc2UoaW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzaz1hdHRlbnRpb25fbWFzayxcbiAgICAgICAgICAgICAgICAgICAgICAgICBwYXN0X2tleV92YWx1ZXM9Tm9uZSlcblxuIyBUcmFpbmFibGUgcGFyYW1ldGVyIGNvdW50XG5uX2xheWVycywgZF9tb2RlbCwgcHJlZml4X2xlbiA9IDEyLCA3NjgsIDIwXG5wYXJhbXMgPSBuX2xheWVycyAqIDIgKiBwcmVmaXhfbGVuICogZF9tb2RlbFxucHJpbnQoZlx1MDAyN1ByZWZpeCB0cmFpbmFibGUgcGFyYW1zOiB7cGFyYW1zOix9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0FwcHJveC4gZm9yIEdQVDItbWVkaXVtICgyNCBsYXllcnMsIGQ9MTAyNCwgUD0xMDApOiBcdTAwMjdcbiAgICAgIGZcdTAwMjd7MjQqMioxMDAqMTAyNDosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1UYXNrIFByZWZpeCBTdG9yYWdlIGFuZCBSb3V0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW5jZSBwcmVmaXggdHVuaW5nIG9ubHkgYWRkcyBhIHNtYWxsIHRlbnNvciBwZXIgdGFzaywgbXVsdGlwbGUgdGFza3MgY2FuIGJlIHNlcnZlZCBmcm9tIGEgc2luZ2xlIGZyb3plbiBiYXNlIG1vZGVsIGJ5IHN0b3Jpbmcgb25lIHByZWZpeCBwZXIgdGFzayBhbmQgbG9hZGluZyB0aGUgYXBwcm9wcmlhdGUgcHJlZml4IGF0IGluZmVyZW5jZSB0aW1lLiBUaGlzIGlzIGEgZm9ybSBvZiB0YXNrLWNvbmRpdGlvbmFsIGNvbXB1dGF0aW9uOiB0aGUgc2FtZSBtb2RlbCB3ZWlnaHRzIHByb2R1Y2UgZGlmZmVyZW50IGJlaGF2aW9ycyBiYXNlZCBwdXJlbHkgb24gd2hpY2ggcHJlZml4IGlzIHByZXBlbmRlZCB0byB0aGUgS1YgY2FjaGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxuY2xhc3MgUHJlZml4U3RvcmU6XG4gICAgXCJcIlwiU3RvcmUgYW5kIGxvYWQgdGFzay1zcGVjaWZpYyBwcmVmaXhlcyBmb3IgbXVsdGktdGFzayBpbmZlcmVuY2Ugcm91dGluZy5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBzYXZlX2Rpcjogc3RyKTpcbiAgICAgICAgc2VsZi5zYXZlX2RpciA9IFBhdGgoc2F2ZV9kaXIpXG4gICAgICAgIHNlbGYuc2F2ZV9kaXIubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKVxuICAgICAgICBzZWxmLl9jYWNoZTogZGljdCA9IHt9XG5cbiAgICBkZWYgc2F2ZV9wcmVmaXgoc2VsZiwgdGFza19uYW1lOiBzdHIsIHByZWZpeDogdG9yY2guVGVuc29yKTpcbiAgICAgICAgcGF0aCA9IHNlbGYuc2F2ZV9kaXIgLyBmXHUwMDI3e3Rhc2tfbmFtZX1fcHJlZml4LnB0XHUwMDI3XG4gICAgICAgIHRvcmNoLnNhdmUocHJlZml4LmRldGFjaCgpLmNwdSgpLCBwYXRoKVxuICAgICAgICBzZWxmLl9jYWNoZVt0YXNrX25hbWVdID0gcHJlZml4LmRldGFjaCgpLmNwdSgpXG4gICAgICAgIHByaW50KGZcdTAwMjdTYXZlZCBwcmVmaXggZm9yIHRhc2sgXCJ7dGFza19uYW1lfVwiOiB7cHJlZml4LnNoYXBlfSAtXHUwMDNlIHtwYXRofVx1MDAyNylcblxuICAgIGRlZiBsb2FkX3ByZWZpeChzZWxmLCB0YXNrX25hbWU6IHN0ciwgZGV2aWNlOiBzdHIgPSBcdTAwMjdjcHVcdTAwMjcpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBpZiB0YXNrX25hbWUgaW4gc2VsZi5fY2FjaGU6XG4gICAgICAgICAgICByZXR1cm4gc2VsZi5fY2FjaGVbdGFza19uYW1lXS50byhkZXZpY2UpXG4gICAgICAgIHBhdGggPSBzZWxmLnNhdmVfZGlyIC8gZlx1MDAyN3t0YXNrX25hbWV9X3ByZWZpeC5wdFx1MDAyN1xuICAgICAgICBwcmVmaXggPSB0b3JjaC5sb2FkKHBhdGgsIG1hcF9sb2NhdGlvbj1kZXZpY2UpXG4gICAgICAgIHNlbGYuX2NhY2hlW3Rhc2tfbmFtZV0gPSBwcmVmaXhcbiAgICAgICAgcmV0dXJuIHByZWZpeFxuXG4gICAgZGVmIGxpc3RfdGFza3Moc2VsZik6XG4gICAgICAgIHJldHVybiBbcC5zdGVtLnJlcGxhY2UoXHUwMDI3X3ByZWZpeFx1MDAyNywgXHUwMDI3XHUwMDI3KSBmb3IgcCBpbiBzZWxmLnNhdmVfZGlyLmdsb2IoXHUwMDI3Kl9wcmVmaXgucHRcdTAwMjcpXVxuXG4jIERlbW86IHNhdmUgcHJlZml4ZXMgZm9yIHR3byB0YXNrc1xuc3RvcmUgPSBQcmVmaXhTdG9yZShcdTAwMjcvdG1wL3ByZWZpeF9zdG9yZVx1MDAyNylcbmZvciB0YXNrIGluIFtcdTAwMjdzdW1tYXJpemF0aW9uXHUwMDI3LCBcdTAwMjdxYVx1MDAyNywgXHUwMDI3dHJhbnNsYXRpb25cdTAwMjddOlxuICAgIHByZWZpeCA9IHRvcmNoLnJhbmRuKDEyLCAyLCAyMCwgNzY4KSAgIyAobl9sYXllcnMsIEtWLCBQLCBkKVxuICAgIHN0b3JlLnNhdmVfcHJlZml4KHRhc2ssIHByZWZpeClcblxucHJpbnQoZlx1MDAyN1N0b3JlZCB0YXNrczoge3N0b3JlLmxpc3RfdGFza3MoKX1cdTAwMjcpXG5sb2FkZWQgPSBzdG9yZS5sb2FkX3ByZWZpeChcdTAwMjdxYVx1MDAyNylcbnByaW50KGZcdTAwMjdMb2FkZWQgUUEgcHJlZml4OiB7bG9hZGVkLnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXJhbWV0ZXIgQ291bnQgYW5kIENvbnRleHQgQ29zdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgbW9kZWwgd2l0aCBMIGxheWVycywgcHJlZml4IGxlbmd0aCBQLCBhbmQgaGlkZGVuIGRpbWVuc2lvbiBkOiB0cmFpbmFibGUgcGFyYW1ldGVycyA9IEwgw5cgMiDDlyBQIMOXIGQgKGZhY3RvciBvZiAyIGZvciBLIGFuZCBWKS4gRm9yIEdQVC0yIG1lZGl1bSAoTD0yNCwgZD0xMDI0LCBQPTEwMCk6IDI0IMOXIDIgw5cgMTAwIMOXIDEwMjQgPSA0LjlNIHBhcmFtZXRlcnMg4oCUIHRpbnkgY29tcGFyZWQgdG8gMzU0TSB0b3RhbC4gQ29udGV4dCBjb3N0OiBQIHBvc2l0aW9ucyBhcmUgY29uc3VtZWQgcGVyIHJlcXVlc3QsIHJlZHVjaW5nIHVzYWJsZSBzZXF1ZW5jZSBsZW5ndGggZnJvbSBtYXhfbGVuIHRvIG1heF9sZW4gLSBQLiBGb3IgbG9uZy1jb250ZXh0IHRhc2tzIHdpdGggbWF4X2xlbj0yMDQ4LCBQPTEwMCByZWR1Y2VzIHVzYWJsZSBjb250ZXh0IGJ5IDUlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZWZpeCBUdW5pbmcgdnMgT3RoZXIgUEVGVCBNZXRob2RzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIldoZXJlIEFkYXB0YXRpb24gSGFwcGVucyIsIlRyYWluYWJsZSBQYXJhbXMiLCJDb250ZXh0IENvbnN1bWVkIiwiVHJhaW5pbmcgU3RhYmlsaXR5IiwiVHlwaWNhbCBQZXJmb3JtYW5jZSBHYXAiXSwicm93cyI6W1siRnVsbCBGaW5lLVR1bmluZyIsIkFsbCB3ZWlnaHRzIHVwZGF0ZWQiLCIxMDAlIG9mIG1vZGVsIiwiTm9uZSIsIkhpZ2giLCJCYXNlbGluZSJdLFsiUHJlZml4IFR1bmluZyIsIktWIGF0IGV2ZXJ5IGF0dGVudGlvbiBsYXllciIsIkzDlzLDl1DDl2QgKH41TSkiLCJQIHRva2VucyBwZXIgbGF5ZXIiLCJOZWVkcyBNTFAgcmVwYXJhbSIsIi0yIHRvIC00JSB2cyBGVCJdLFsiUHJvbXB0IFR1bmluZyIsIklucHV0IGVtYmVkZGluZyBvbmx5IiwiUMOXZCAofjAuMU0pIiwiUCB0b2tlbnMgKGlucHV0IG9ubHkpIiwiSGlnaCAoc2ltcGxlcikiLCItNCB0byAtOCUgdnMgRlQiXSxbIkFkYXB0ZXIiLCJGRk4gYWZ0ZXIgZWFjaCBhdHRlbnRpb24iLCIyw5dMw5dyw5dkICh+N00pIiwiTm9uZSIsIkhpZ2giLCItMSB0byAtMyUgdnMgRlQiXSxbIkxvUkEgcj0xNiIsIlEgYW5kIFYgd2VpZ2h0IG1hdHJpY2VzIiwiNMOXTMOXcsOXZCAofjg0TSBmb3IgN0IpIiwiTm9uZSIsIkhpZ2giLCItMSB0byAtMiUgdnMgRlQiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGkgXHUwMDI2IExpYW5nICgyMDIxKSBldmFsdWF0ZSBwcmVmaXggdHVuaW5nIG9uIHRhYmxlLXRvLXRleHQgZ2VuZXJhdGlvbiAoRTJFLCBXZWJOTEcsIERBUlQpIGFuZCBzdW1tYXJpemF0aW9uIChYU1VNKS4gV2l0aCBQPTEwMCBwcmVmaXggdG9rZW5zLCBwcmVmaXggdHVuaW5nIG1hdGNoZXMgb3IgZXhjZWVkcyBmdWxsIGZpbmUtdHVuaW5nIG9uIEUyRSBhbmQgV2ViTkxHIGRlc3BpdGUgb25seSAwLjElIG9mIHRvdGFsIHBhcmFtZXRlcnMuIE9uIFhTVU0gc3VtbWFyaXphdGlvbiwgcHJlZml4IHR1bmluZyBmYWxscyB+MSBST1VHRSBwb2ludCBzaG9ydC4gVGhlc2UgcmVzdWx0cyBzdWdnZXN0IHByZWZpeCB0dW5pbmcgaXMgbW9zdCBlZmZlY3RpdmUgb24gZ2VuZXJhdGlvbiB0YXNrcyB3aXRoIGEgY2xlYXIgZm9ybWF0IHN0cnVjdHVyZSB0aGF0IHRoZSBwcmVmaXggY2FuIGVuY29kZSBhcyBhIHByaW9yLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiUHJlZml4IHRva2VucyByZWR1Y2UgZWZmZWN0aXZlIGNvbnRleHQgd2luZG93IiwiY29udGVudCI6IlByZWZpeCB0dW5pbmcgY29uc3VtZXMgUCBwb3NpdGlvbnMgZnJvbSB0aGUgZWZmZWN0aXZlIGNvbnRleHQgd2luZG93IGF0IGVhY2ggbGF5ZXIg4oCUIHVzaW5nIFA9MTAwIHByZWZpeCB0b2tlbnMgcmVkdWNlcyB1c2FibGUgY29udGV4dCBieSAxMDAgdG9rZW5zLCB3aGljaCBtYXR0ZXJzIGZvciBsb25nLWNvbnRleHQgdGFza3MgYW5kIG11c3QgYmUgYWNjb3VudGVkIGZvciBpbiBtYXhfbGVuZ3RoIHNldHRpbmdzLiBGb3IgbW9kZWxzIGFscmVhZHkgbmVhciB0aGVpciBjb250ZXh0IGxpbWl0IChlLmcuLCBzdW1tYXJpemluZyAxOTAwLXRva2VuIGRvY3VtZW50cyB3aXRoIG1heF9sZW49MjA0OCksIHJlZHVjaW5nIHRvIDE5NDggdXNhYmxlIHBvc2l0aW9ucyBtYXkgY2F1c2UgdHJ1bmNhdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIk1MUCByZXBhcmFtZXRlcml6YXRpb24gaXMgbmVlZGVkIG9ubHkgZHVyaW5nIHRyYWluaW5nOyBtYXRlcmlhbGl6ZSBhbmQgZGlzY2FyZCB0aGUgTUxQIGJlZm9yZSBpbmZlcmVuY2UgZGVwbG95bWVudC4iLCJQcmVmaXggbGVuZ3RoIFAgaXMgYSBoeXBlcnBhcmFtZXRlcjogUD0xMCBmb3Igc2ltcGxlIHRhc2tzLCBQPTUw4oCTMTAwIGZvciBjb21wbGV4IHN0cnVjdHVyZWQgZ2VuZXJhdGlvbi4iLCJDYXVzYWwgTE1zOiBwcmVmaXggdG9rZW5zIHNob3VsZCBub3QgYmUgY2F1c2FsbHkgbWFza2VkIOKAlCB1c2UgYmlkaXJlY3Rpb25hbCBhdHRlbnRpb24gZm9yIHByZWZpeCBwb3NpdGlvbnMuIiwiTXVsdGktdGFzazogb25lIGZyb3plbiBiYXNlIG1vZGVsICsgTiBzbWFsbCBwcmVmaXggZmlsZXMgaXMgbW9yZSBzdG9yYWdlLWVmZmljaWVudCB0aGFuIE4gZnVsbCBmaW5lLXR1bmVkIG1vZGVscy4iLCJQcmVmaXggdnMgTG9SQTogcHJlZml4IHR1bmluZyBpcyBzdHJvbmdlciBmb3IgZ2VuZXJhdGlvbiBmb3JtYXQgY29udHJvbDsgTG9SQSBpcyBzdHJvbmdlciBmb3Iga25vd2xlZGdlIGluamVjdGlvbi4iLCJDb21iaW5lIHdpdGggcXVhbnRpemF0aW9uOiBwcmVmaXggdmVjdG9ycyBhcmUgc21hbGwgZW5vdWdoIHRvIHN0b3JlIGluIEZQMzIgZXZlbiB3aGVuIHRoZSBiYXNlIG1vZGVsIGlzIGluIElOVDQuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Prefix Tuning — Virtual Token Prepending to Each Layer's KV Cache

Prompt tuning prepends learned tokens to the input embedding layer only — these soft tokens must propagate their influence through all attention layers via the residual stream. Prefix tuning (Li & Liang, 2021) is more direct: it prepends learned prefix vectors P_K^l and P_V^l directly to the key and value matrices at every transformer layer l. This gives every layer independent, direct control over attention patterns regardless of how information flows through intermediate layers. The prefix vectors are the only trainable parameters; all transformer weights remain frozen.

## Prefix vs Prompt Tuning

Prompt tuning adds P tokens to the input embedding. These tokens attend to actual content tokens but are themselves attended to only at later layers through the residual. Prefix tuning adds P_K and P_V vectors directly to the K and V matrices of every attention layer. The content tokens can attend to the prefix at every layer — much stronger and more direct conditioning. The cost is proportionally more parameters (one prefix pair per layer vs one embedding block) and P consumed context positions.

## Prefix Tuning Forward Pass

For an attention layer with head dimension d_head and P prefix tokens, the key matrix becomes K = concat([P_K, K_input]) ∈ ℝ^{(P+T)×d_head} and similarly V = concat([P_V, V_input]) ∈ ℝ^{(P+T)×d_head}, where T is the sequence length. The query Q ∈ ℝ^{T×d_head} attends over all P+T positions. Causal masking is applied only to the input token positions; prefix tokens are always visible to all input positions (like a prefix that predates the sequence).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class PrefixAttentionLayer(nn.Module):
    """Single multi-head attention layer with prefix tuning."""

    def __init__(self, d_model: int, n_heads: int, prefix_len: int):
        super().__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.prefix_len = prefix_len
        self.W_q = nn.Linear(d_model, d_model, bias=False)
        self.W_k = nn.Linear(d_model, d_model, bias=False)
        self.W_v = nn.Linear(d_model, d_model, bias=False)
        self.W_o = nn.Linear(d_model, d_model, bias=False)
        # Learnable prefix key and value vectors (one per head)
        self.prefix_k = nn.Parameter(torch.randn(1, prefix_len, d_model) * 0.02)
        self.prefix_v = nn.Parameter(torch.randn(1, prefix_len, d_model) * 0.02)
        # Freeze all non-prefix params
        for p in [self.W_q.weight, self.W_k.weight, self.W_v.weight, self.W_o.weight]:
            p.requires_grad_(False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, D = x.shape
        Q = self.W_q(x).reshape(B, T, self.n_heads, self.d_head).transpose(1, 2)
        K_input = self.W_k(x).reshape(B, T, self.n_heads, self.d_head).transpose(1, 2)
        V_input = self.W_v(x).reshape(B, T, self.n_heads, self.d_head).transpose(1, 2)
        # Expand prefix K and V to match batch and reshape for heads
        P_K = self.W_k(self.prefix_k.expand(B, -1, -1)).reshape(B, self.prefix_len, self.n_heads, self.d_head).transpose(1, 2)
        P_V = self.W_v(self.prefix_v.expand(B, -1, -1)).reshape(B, self.prefix_len, self.n_heads, self.d_head).transpose(1, 2)
        K = torch.cat([P_K, K_input], dim=2)  # (B, H, P+T, d_head)
        V = torch.cat([P_V, V_input], dim=2)
        scale = math.sqrt(self.d_head)
        attn = torch.softmax(Q @ K.transpose(-2, -1) / scale, dim=-1)
        out = (attn @ V).transpose(1, 2).reshape(B, T, D)
        return self.W_o(out)

layer = PrefixAttentionLayer(d_model=64, n_heads=4, prefix_len=10)
x = torch.randn(2, 8, 64)
print(f'Output shape: {layer(x).shape}')
trainable = sum(p.numel() for p in layer.parameters() if p.requires_grad)
print(f'Trainable prefix params: {trainable}')
```

## MLP Reparameterization for Training Stability

Li & Liang found that directly optimizing the prefix vectors P_K and P_V is unstable — the prefix tends to collapse to a degenerate solution in early training. To stabilize, they propose reparameterization: the actual prefix vectors are produced by a small MLP that takes a compact set of free parameters as input. After training, the MLP is discarded and only the output prefix vectors (the fixed-point of the MLP) are stored. This reparameterization is used only during training; at inference, the prefix vectors are materialized and cached.

```python
import torch
import torch.nn as nn
import torch.optim as optim

class PrefixMLP(nn.Module):
    """MLP reparameterization for prefix tuning (used only during training)."""

    def __init__(self, prefix_len: int, d_model: int, n_layers: int,
                 bottleneck_dim: int = 512):
        super().__init__()
        self.prefix_len = prefix_len
        self.d_model = d_model
        self.n_layers = n_layers
        # Free parameters: compact embedding for each prefix position
        self.free_params = nn.Parameter(
            torch.randn(prefix_len, bottleneck_dim) * 0.01
        )
        # MLP that expands free params to full prefix K and V for each layer
        self.mlp = nn.Sequential(
            nn.Linear(bottleneck_dim, bottleneck_dim * 2),
            nn.Tanh(),
            nn.Linear(bottleneck_dim * 2, n_layers * 2 * d_model),  # K and V per layer
        )

    def forward(self) -> torch.Tensor:
        """Returns prefix tensor of shape (n_layers, 2, prefix_len, d_model)."""
        out = self.mlp(self.free_params)  # (prefix_len, n_layers*2*d_model)
        out = out.view(self.prefix_len, self.n_layers, 2, self.d_model)
        return out.permute(1, 2, 0, 3)  # (n_layers, 2, prefix_len, d_model)

    def materialize(self) -> torch.Tensor:
        """Call after training to extract fixed prefix (MLP no longer needed)."""
        with torch.no_grad():
            return self()

# Training setup
prefix_mlp = PrefixMLP(prefix_len=20, d_model=768, n_layers=12, bottleneck_dim=256)
optimizer = optim.AdamW(prefix_mlp.parameters(), lr=5e-3)
prefixes = prefix_mlp()
print(f'Prefix tensor shape: {prefixes.shape}')  # (12 layers, 2 for K/V, 20 tokens, 768 dim)
print(f'MLP trainable params: {sum(p.numel() for p in prefix_mlp.parameters()):,}')
materialized = prefix_mlp.materialize()
print(f'Materialized prefix: {materialized.shape}')
```

## Full Model with Prefix Injection

A complete prefix-tuned LLM wraps the base transformer to intercept each attention layer's key and value computation. The wrapper stores prefix vectors indexed by layer number and injects them during the forward pass. All base model parameters have requires_grad=False; only the prefix parameters are optimized.

```python
import torch
import torch.nn as nn
from typing import Optional

class PrefixTunedModel(nn.Module):
    """Wraps a transformer to inject per-layer prefix vectors."""

    def __init__(self, base_model: nn.Module, n_layers: int,
                 d_model: int, prefix_len: int = 20):
        super().__init__()
        self.base = base_model
        self.prefix_len = prefix_len
        # Freeze all base model parameters
        for param in self.base.parameters():
            param.requires_grad_(False)
        # Learnable prefix K and V for every layer (shape: [n_layers, 2, P, d_model])
        self.prefix = nn.Parameter(
            torch.zeros(n_layers, 2, prefix_len, d_model)
        )
        nn.init.normal_(self.prefix, std=0.02)

    def get_prefix_kv(self, layer_idx: int):
        """Return (prefix_K, prefix_V) for a given layer."""
        return self.prefix[layer_idx, 0], self.prefix[layer_idx, 1]

    def forward(self, input_ids: torch.Tensor,
                attention_mask: Optional[torch.Tensor] = None):
        # Prepend prefix attention mask (all ones — prefix is always visible)
        B = input_ids.shape[0]
        if attention_mask is not None:
            prefix_mask = torch.ones(B, self.prefix_len, device=input_ids.device)
            attention_mask = torch.cat([prefix_mask, attention_mask], dim=1)
        return self.base(input_ids, attention_mask=attention_mask,
                         past_key_values=None)

# Trainable parameter count
n_layers, d_model, prefix_len = 12, 768, 20
params = n_layers * 2 * prefix_len * d_model
print(f'Prefix trainable params: {params:,}')
print(f'Approx. for GPT2-medium (24 layers, d=1024, P=100): '
      f'{24*2*100*1024:,}')
```

## Multi-Task Prefix Storage and Routing

Since prefix tuning only adds a small tensor per task, multiple tasks can be served from a single frozen base model by storing one prefix per task and loading the appropriate prefix at inference time. This is a form of task-conditional computation: the same model weights produce different behaviors based purely on which prefix is prepended to the KV cache.

```python
import torch
import torch.nn as nn
from pathlib import Path

class PrefixStore:
    """Store and load task-specific prefixes for multi-task inference routing."""

    def __init__(self, save_dir: str):
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self._cache: dict = {}

    def save_prefix(self, task_name: str, prefix: torch.Tensor):
        path = self.save_dir / f'{task_name}_prefix.pt'
        torch.save(prefix.detach().cpu(), path)
        self._cache[task_name] = prefix.detach().cpu()
        print(f'Saved prefix for task "{task_name}": {prefix.shape} -> {path}')

    def load_prefix(self, task_name: str, device: str = 'cpu') -> torch.Tensor:
        if task_name in self._cache:
            return self._cache[task_name].to(device)
        path = self.save_dir / f'{task_name}_prefix.pt'
        prefix = torch.load(path, map_location=device)
        self._cache[task_name] = prefix
        return prefix

    def list_tasks(self):
        return [p.stem.replace('_prefix', '') for p in self.save_dir.glob('*_prefix.pt')]

# Demo: save prefixes for two tasks
store = PrefixStore('/tmp/prefix_store')
for task in ['summarization', 'qa', 'translation']:
    prefix = torch.randn(12, 2, 20, 768)  # (n_layers, KV, P, d)
    store.save_prefix(task, prefix)

print(f'Stored tasks: {store.list_tasks()}')
loaded = store.load_prefix('qa')
print(f'Loaded QA prefix: {loaded.shape}')
```

## Parameter Count and Context Cost

For a model with L layers, prefix length P, and hidden dimension d: trainable parameters = L × 2 × P × d (factor of 2 for K and V). For GPT-2 medium (L=24, d=1024, P=100): 24 × 2 × 100 × 1024 = 4.9M parameters — tiny compared to 354M total. Context cost: P positions are consumed per request, reducing usable sequence length from max_len to max_len - P. For long-context tasks with max_len=2048, P=100 reduces usable context by 5%.

## Prefix Tuning vs Other PEFT Methods

| Method | Where Adaptation Happens | Trainable Params | Context Consumed | Training Stability | Typical Performance Gap |
| --- | --- | --- | --- | --- | --- |
| Full Fine-Tuning | All weights updated | 100% of model | None | High | Baseline |
| Prefix Tuning | KV at every attention layer | L×2×P×d (~5M) | P tokens per layer | Needs MLP reparam | -2 to -4% vs FT |
| Prompt Tuning | Input embedding only | P×d (~0.1M) | P tokens (input only) | High (simpler) | -4 to -8% vs FT |
| Adapter | FFN after each attention | 2×L×r×d (~7M) | None | High | -1 to -3% vs FT |
| LoRA r=16 | Q and V weight matrices | 4×L×r×d (~84M for 7B) | None | High | -1 to -2% vs FT |

Li & Liang (2021) evaluate prefix tuning on table-to-text generation (E2E, WebNLG, DART) and summarization (XSUM). With P=100 prefix tokens, prefix tuning matches or exceeds full fine-tuning on E2E and WebNLG despite only 0.1% of total parameters. On XSUM summarization, prefix tuning falls ~1 ROUGE point short. These results suggest prefix tuning is most effective on generation tasks with a clear format structure that the prefix can encode as a prior.

> **Prefix tokens reduce effective context window**: Prefix tuning consumes P positions from the effective context window at each layer — using P=100 prefix tokens reduces usable context by 100 tokens, which matters for long-context tasks and must be accounted for in max_length settings. For models already near their context limit (e.g., summarizing 1900-token documents with max_len=2048), reducing to 1948 usable positions may cause truncation.

- MLP reparameterization is needed only during training; materialize and discard the MLP before inference deployment.
- Prefix length P is a hyperparameter: P=10 for simple tasks, P=50–100 for complex structured generation.
- Causal LMs: prefix tokens should not be causally masked — use bidirectional attention for prefix positions.
- Multi-task: one frozen base model + N small prefix files is more storage-efficient than N full fine-tuned models.
- Prefix vs LoRA: prefix tuning is stronger for generation format control; LoRA is stronger for knowledge injection.
- Combine with quantization: prefix vectors are small enough to store in FP32 even when the base model is in INT4.

---

