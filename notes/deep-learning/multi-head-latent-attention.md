---
title: "Multi-Head Latent Attention (MLA) — DeepSeek's KV Compression"
slug: "multi-head-latent-attention"
description: "Implement MLA from scratch with low-rank KV compression, build an MLA inference cache storing only latent vectors, compare KV cache memory across MHA/GQA/MLA, and apply decoupled RoPE to the non-cached key component."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGktSGVhZCBMYXRlbnQgQXR0ZW50aW9uIChNTEEpLCBpbnRyb2R1Y2VkIGluIERlZXBTZWVrLVYyICgyMDI0KSwgY29tcHJlc3NlcyB0aGUgS1YgY2FjaGUgaW50byBsb3ctcmFuayBsYXRlbnQgdmVjdG9ycyByYXRoZXIgdGhhbiBncm91cGluZyBoZWFkcyBhcyBHUUEgZG9lcy4gVGhlIGNvcmUgaWRlYTogaW5zdGVhZCBvZiBjYWNoaW5nIEcgw5cgZF9oZWFkIGtleXMgYW5kIHZhbHVlcyBwZXIgdG9rZW4sIE1MQSBkb3duLXByb2plY3RzIHRoZSBoaWRkZW4gc3RhdGUgdG8gYSBzaW5nbGUgY19LVi1kaW1lbnNpb25hbCBsYXRlbnQgdmVjdG9yIGPigpwgPSBXX0RLViBo4oKcIHdoZXJlIGNfS1Yg4omqIGRfbW9kZWwuIEF0IGluZmVyZW5jZSwgSyBhbmQgViBhcmUgcmVjb25zdHJ1Y3RlZCBvbiB0aGUgZmx5IGZyb20gY+KCnCB2aWEgbGVhcm5lZCB1cC1wcm9qZWN0aW9uIG1hdHJpY2VzLiBPbmx5IGPigpwgaXMgc3RvcmVkIGluIHRoZSBjYWNoZSwgYWNoaWV2aW5nIGEgY29tcHJlc3Npb24gcmF0aW8gb2YgY19LViAvICgyIMOXIGggw5cgZF9oZWFkKSDigJQgYXBwcm94aW1hdGVseSA1w5cgdnMgTUhBIGZvciBEZWVwU2Vlay1WMi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdGFuZGFyZCBLViBDYWNoZSBhbmQgSXRzIE1lbW9yeSBDb3N0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBtb2RlbCB3aXRoIGggaGVhZHMgYW5kIGhlYWQgZGltZW5zaW9uIGRfaGVhZCwgdGhlIE1IQSBLViBjYWNoZSBwZXIgdG9rZW4gcGVyIGxheWVyIGlzIDIgw5cgaCDDlyBkX2hlYWQgZmxvYXRzLiBEZWVwU2Vlay1WMiB1c2VzIGg9MTI4IGhlYWRzIHdpdGggZF9oZWFkPTEyOCwgZ2l2aW5nIDIgw5cgMTI4IMOXIDEyOCA9IDMyNzY4IGZsb2F0cyBwZXIgdG9rZW4gcGVyIGxheWVyLiBBdCBMPTEyOEsgdG9rZW5zICh0aGUgdGFyZ2V0IGNvbnRleHQpLCB0aGlzIGlzIDMyNzY4IMOXIDEyOEsgw5cgMiBieXRlcyAoZmxvYXQxNikg4omIIDggR0IgcGVyIGxheWVyLiBNTEEgcmVkdWNlcyB0aGUgY2FjaGUgdG8gY19LViBmbG9hdHMgcGVyIHRva2VuIOKAlCBEZWVwU2Vlay1WMiB1c2VzIGNfS1Y9NTEyLCBzdG9yaW5nIDUxMiBmbG9hdHMgaW5zdGVhZCBvZiAzMjc2ODogYSA2NMOXIHJhdyByZWR1Y3Rpb24gaW4gY2FjaGUgZWxlbWVudHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTUxBOiBMb3ctUmFuayBLViBDb21wcmVzc2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTUxBIHJlcGxhY2VzIHRoZSBzZXBhcmF0ZSBXX0sgYW5kIFdfViBwcm9qZWN0aW9ucyB3aXRoIGEgc2hhcmVkIGRvd24tcHJvamVjdGlvbiBXX0RLViDiiIgg4oSdXntjX0tWIMOXIGRfbW9kZWx9IGZvbGxvd2VkIGJ5IHNlcGFyYXRlIHVwLXByb2plY3Rpb25zIFdfVUsg4oiIIOKEnV57KGggw5cgZF9oZWFkKSDDlyBjX0tWfSBhbmQgV19VViDiiIgg4oSdXnsoaCDDlyBkX2hlYWQpIMOXIGNfS1Z9LiBBdCBlYWNoIHRva2VuIHBvc2l0aW9uIHQ6IGxhdGVudCBj4oKcID0gV19ES1YgaOKCnCAoY19LViBkaW1zKTsgSyA9IFdfVUsgY+KCnCAocmVjb25zdHJ1Y3RlZCwgbm90IGNhY2hlZCk7IFYgPSBXX1VWIGPigpwgKHJlY29uc3RydWN0ZWQsIG5vdCBjYWNoZWQpLiBPbmx5IGPigpwgaXMgYXBwZW5kZWQgdG8gdGhlIGNhY2hlLiBBdCBpbmZlcmVuY2UsIHBhc3QgY+KCnCB2YWx1ZXMgYXJlIHJldHJpZXZlZCBhbmQgSyxWIGFyZSByZWNvbnN0cnVjdGVkIGZvciB0aGUgZnVsbCBjYWNoZWQgc2VxdWVuY2UgYmVmb3JlIGF0dGVudGlvbiBpcyBjb21wdXRlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBtYXRoXG5cbmNsYXNzIE11bHRpSGVhZExhdGVudEF0dGVudGlvbihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsLCBudW1faGVhZHMsIGRfaGVhZCwgY19rdik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmgsIHNlbGYuZCwgc2VsZi5jID0gbnVtX2hlYWRzLCBkX2hlYWQsIGNfa3ZcbiAgICAgICAgc2VsZi5XX3EgID0gbm4uTGluZWFyKGRfbW9kZWwsIG51bV9oZWFkcyAqIGRfaGVhZCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XX2RrdiA9IG5uLkxpbmVhcihkX21vZGVsLCBjX2t2LCBiaWFzPUZhbHNlKSAgICAgICAjIGRvd24tcHJvamVjdCB0byBsYXRlbnRcbiAgICAgICAgc2VsZi5XX3VrICA9IG5uLkxpbmVhcihjX2t2LCBudW1faGVhZHMgKiBkX2hlYWQsIGJpYXM9RmFsc2UpICAjIHVwLXByb2plY3QgdG8gS1xuICAgICAgICBzZWxmLldfdXYgID0gbm4uTGluZWFyKGNfa3YsIG51bV9oZWFkcyAqIGRfaGVhZCwgYmlhcz1GYWxzZSkgICMgdXAtcHJvamVjdCB0byBWXG4gICAgICAgIHNlbGYuV19vICAgPSBubi5MaW5lYXIobnVtX2hlYWRzICogZF9oZWFkLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIEIsIEwsIF8gPSB4LnNoYXBlXG4gICAgICAgIFEgPSBzZWxmLldfcSh4KS52aWV3KEIsIEwsIHNlbGYuaCwgc2VsZi5kKS50cmFuc3Bvc2UoMSwgMikgICMgKEIsaCxMLGQpXG4gICAgICAgIGMgPSBzZWxmLldfZGt2KHgpICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsTCxjX2t2KSAtLSBsYXRlbnRcbiAgICAgICAgSyA9IHNlbGYuV191ayhjKS52aWV3KEIsIEwsIHNlbGYuaCwgc2VsZi5kKS50cmFuc3Bvc2UoMSwgMikgICMgcmVjb25zdHJ1Y3QgS1xuICAgICAgICBWID0gc2VsZi5XX3V2KGMpLnZpZXcoQiwgTCwgc2VsZi5oLCBzZWxmLmQpLnRyYW5zcG9zZSgxLCAyKSAgIyByZWNvbnN0cnVjdCBWXG4gICAgICAgIGF0dG4gPSBGLnNvZnRtYXgoUSBAIEsudHJhbnNwb3NlKC0yLC0xKSAvIG1hdGguc3FydChzZWxmLmQpLCBkaW09LTEpXG4gICAgICAgIG91dCA9IChhdHRuIEAgVikudHJhbnNwb3NlKDEsIDIpLnJlc2hhcGUoQiwgTCwgLTEpXG4gICAgICAgIHJldHVybiBzZWxmLldfbyhvdXQpLCBjICAjIHJldHVybiBsYXRlbnQgZm9yIGNhY2hpbmdcblxuZF9tb2RlbCwgaCwgZF9oZWFkLCBjX2t2ID0gNTEyLCA4LCA2NCwgMTI4XG5tb2RlbCA9IE11bHRpSGVhZExhdGVudEF0dGVudGlvbihkX21vZGVsLCBoLCBkX2hlYWQsIGNfa3YpXG54ID0gdG9yY2gucmFuZG4oMiwgMzIsIGRfbW9kZWwpXG5vdXQsIGxhdGVudCA9IG1vZGVsKHgpXG5wcmludChmXHUwMDI3T3V0cHV0OiB7b3V0LnNoYXBlfSwgTGF0ZW50ICh0byBjYWNoZSk6IHtsYXRlbnQuc2hhcGV9XHUwMDI3KVxua3ZfbWhhICA9IDIgKiBoICogZF9oZWFkICAjIHBlciB0b2tlbiwgcGVyIGxheWVyXG5rdl9tbGEgID0gY19rdlxucHJpbnQoZlx1MDAyN01IQSBLViBwZXIgdG9rZW46IHtrdl9taGF9LCBNTEEgS1YgcGVyIHRva2VuOiB7a3ZfbWxhfSAoe2t2X21oYS9rdl9tbGE6LjFmfXggc21hbGxlcilcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW5mZXJlbmNlIHdpdGggQ29tcHJlc3NlZCBLViBDYWNoZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXQgZ2VuZXJhdGlvbiB0aW1lIE1MQSBjYWNoZXMgb25seSB0aGUgY19LVi1kaW1lbnNpb25hbCBsYXRlbnQgdmVjdG9yIGZvciBlYWNoIHBhc3QgdG9rZW4uIFRvIGNvbXB1dGUgYXR0ZW50aW9uIGZvciB0aGUgY3VycmVudCB0b2tlbjogcmV0cmlldmUgYWxsIHBhc3QgbGF0ZW50cyBmcm9tIHRoZSBjYWNoZSAoc2hhcGU6IExfcGFzdCDDlyBjX0tWIHBlciBsYXllciksIHVwLXByb2plY3QgZWFjaCB0byBnZXQgSyBhbmQgViwgdGhlbiBjb21wdXRlIGF0dGVudGlvbi4gVGhlIHVwLXByb2plY3Rpb25zIFdfVUsgYW5kIFdfVVYgYWRkIGV4dHJhIGNvbXB1dGF0aW9uIGJ1dCB0aGlzIGlzIGJvdW5kZWQgYnkgTyhMIMOXIGNfS1Ygw5cgaCDDlyBkX2hlYWQpIHdoaWNoIGlzIHNtYWxsIGNvbXBhcmVkIHRvIGF0dGVudGlvbiBmb3IgbGFyZ2UgTC4gVGhlIGtleSB0cmFkZTogY29tcHV0ZSAocmVjb25zdHJ1Y3RpbmcgSyxWKSBmb3IgbWVtb3J5IChzdG9yaW5nIG9ubHkgY+KCnCkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5jbGFzcyBNTEFJbmZlcmVuY2VDYWNoZTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbWF4X2xlbiwgY19rdiwgbnVtX2hlYWRzLCBkX2hlYWQsXG4gICAgICAgICAgICAgICAgIFdfdWs6IG5uLkxpbmVhciwgV191djogbm4uTGluZWFyKTpcbiAgICAgICAgc2VsZi5jX2NhY2hlID0gdG9yY2guemVyb3MoMSwgbWF4X2xlbiwgY19rdikgICMgb25seSBsYXRlbnRzIGNhY2hlZFxuICAgICAgICBzZWxmLldfdWssIHNlbGYuV191diA9IFdfdWssIFdfdXZcbiAgICAgICAgc2VsZi5oLCBzZWxmLmQsIHNlbGYudCA9IG51bV9oZWFkcywgZF9oZWFkLCAwXG5cbiAgICBkZWYgc3RlcChzZWxmLCBxLCBjX25ldyk6XG4gICAgICAgIFwiXCJcInE6ICgxLGgsMSxkKSAgY19uZXc6ICgxLDEsY19rdikgbGF0ZW50IGZvciBjdXJyZW50IHRva2VuLlwiXCJcIlxuICAgICAgICBzZWxmLmNfY2FjaGVbOiwgc2VsZi50OnNlbGYudCsxXSA9IGNfbmV3XG4gICAgICAgIHNlbGYudCArPSAxXG4gICAgICAgIGNfcGFzdCA9IHNlbGYuY19jYWNoZVs6LCA6c2VsZi50XSAgICAgICAgIyAoMSx0LGNfa3YpXG4gICAgICAgIEsgPSBzZWxmLldfdWsoY19wYXN0KS52aWV3KDEsIHNlbGYudCwgc2VsZi5oLCBzZWxmLmQpLnRyYW5zcG9zZSgxLDIpICAjICgxLGgsdCxkKVxuICAgICAgICBWID0gc2VsZi5XX3V2KGNfcGFzdCkudmlldygxLCBzZWxmLnQsIHNlbGYuaCwgc2VsZi5kKS50cmFuc3Bvc2UoMSwyKVxuICAgICAgICBzY29yZXMgPSBxIEAgSy50cmFuc3Bvc2UoLTIsLTEpIC8gbWF0aC5zcXJ0KHNlbGYuZClcbiAgICAgICAgcmV0dXJuIEYuc29mdG1heChzY29yZXMsIGRpbT0tMSkgQCBWXG5cbmRfbW9kZWwsIGgsIGRfaGVhZCwgY19rdiwgbWF4X2xlbiA9IDI1NiwgNCwgMzIsIDY0LCAxMjhcbldfdWsgPSBubi5MaW5lYXIoY19rdiwgaCAqIGRfaGVhZCwgYmlhcz1GYWxzZSlcbldfdXYgPSBubi5MaW5lYXIoY19rdiwgaCAqIGRfaGVhZCwgYmlhcz1GYWxzZSlcbldfZGt2ID0gbm4uTGluZWFyKGRfbW9kZWwsIGNfa3YsIGJpYXM9RmFsc2UpXG5XX3EgICA9IG5uLkxpbmVhcihkX21vZGVsLCBoICogZF9oZWFkLCBiaWFzPUZhbHNlKVxuY2FjaGUgPSBNTEFJbmZlcmVuY2VDYWNoZShtYXhfbGVuLCBjX2t2LCBoLCBkX2hlYWQsIFdfdWssIFdfdXYpXG5mb3Igc3RlcCBpbiByYW5nZSgyMCk6XG4gICAgeF90ID0gdG9yY2gucmFuZG4oMSwgMSwgZF9tb2RlbClcbiAgICBxID0gV19xKHhfdCkudmlldygxLCBoLCAxLCBkX2hlYWQpXG4gICAgYyA9IFdfZGt2KHhfdCkgICAgICAgICAgICAgIyAoMSwxLGNfa3YpXG4gICAgb3V0ID0gY2FjaGUuc3RlcChxLCBjKVxucHJpbnQoZlx1MDAyN0FmdGVyIHtjYWNoZS50fSBzdGVwcywgY2FjaGUgaG9sZHMge2NhY2hlLnR9IGxhdGVudHMgb2YgZGltIHtjX2t2fVx1MDAyNylcbnByaW50KGZcdTAwMjdDYWNoZSBieXRlcyAoZmxvYXQzMik6IHtjYWNoZS50ICogY19rdiAqIDR9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0VxdWl2YWxlbnQgTUhBIGNhY2hlIDoge2NhY2hlLnQgKiBoICogZF9oZWFkICogMiAqIDR9IGJ5dGVzICh7MipoKmRfaGVhZC8vY19rdjouMGZ9eCBsYXJnZXIpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktWIENhY2hlIE1lbW9yeTogTUhBIHZzIEdRQSB2cyBNTEEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0aHJlZSBhcHByb2FjaGVzIHJlcHJlc2VudCBhIHNwZWN0cnVtIG9mIEtWIGNhY2hlIGNvbXByZXNzaW9uLiBNSEEgc3RvcmVzIGFsbCBow5dkX2hlYWQga2V5cyBhbmQgdmFsdWVzOyBHUUEgc3RvcmVzIG9ubHkgR8OXZF9oZWFkIChHIFx1MDAzYyBoKTsgTUxBIHN0b3JlcyBhIGNfS1YtZGltZW5zaW9uYWwgbGF0ZW50IGFuZCByZWNvbnN0cnVjdHMgSyxWIG9uIHRoZSBmbHkuIE1MQSBhY2hpZXZlcyB0aGUgc21hbGxlc3QgY2FjaGUgZm9vdHByaW50IGJ1dCBhZGRzIHJlY29uc3RydWN0aW9uIGNvbXB1dGUuIEZvciB2ZXJ5IGxvbmcgc2VxdWVuY2VzIChMIFx1MDAzZSAxMDBLKSwgTUxBXHUwMDI3cyBjYWNoZSBhZHZhbnRhZ2UgaXMgZG9taW5hbnQg4oCUIHJlY29uc3RydWN0aW9uIGNvbXB1dGUgaXMgTyhMIMOXIGNfS1Ygw5cgaCDDlyBkX2hlYWQpIHdoaWNoIHJlbWFpbnMgdHJhY3RhYmxlIHJlbGF0aXZlIHRvIHRoZSBtZW1vcnkgc2F2aW5ncy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBrdl9jYWNoZV9ieXRlcyhtZXRob2QsIGgsIGRfaGVhZCwgRywgY19rdiwgTCwgZHR5cGVfYnl0ZXM9Mik6XG4gICAgXCJcIlwiQ29tcHV0ZSBLViBjYWNoZSBzaXplIGluIGJ5dGVzIGZvciBhIHNpbmdsZSBsYXllciwgTCB0b2tlbnMuXCJcIlwiXG4gICAgaWYgbWV0aG9kID09IFx1MDAyN01IQVx1MDAyNzpcbiAgICAgICAgcmV0dXJuIDIgKiBoICogZF9oZWFkICogTCAqIGR0eXBlX2J5dGVzXG4gICAgZWxpZiBtZXRob2QgPT0gXHUwMDI3R1FBXHUwMDI3OlxuICAgICAgICByZXR1cm4gMiAqIEcgKiBkX2hlYWQgKiBMICogZHR5cGVfYnl0ZXNcbiAgICBlbGlmIG1ldGhvZCA9PSBcdTAwMjdNTEFcdTAwMjc6XG4gICAgICAgIHJldHVybiBjX2t2ICogTCAqIGR0eXBlX2J5dGVzICAjIG9ubHkgbGF0ZW50IGNhY2hlZFxuICAgIHJhaXNlIFZhbHVlRXJyb3IobWV0aG9kKVxuXG5oLCBkX2hlYWQgPSA2NCwgMTI4ICAjIExMYU1BL0RlZXBTZWVrIHNjYWxlXG5HLCBjX2t2ICAgPSA4LCA1MTIgICAjIEdRQSBncm91cHMgYW5kIE1MQSBsYXRlbnQgZGltXG5wcmludChmXCJ7XHUwMDI3TWV0aG9kXHUwMDI3Olx1MDAzZTZ9IHtcdTAwMjdMPTRLXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3TD0zMktcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdMPTEyOEtcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjd2cyBNSEFcdTAwMjc6XHUwMDNlMTB9XCIpXG5mb3IgbWV0aG9kIGluIFtcdTAwMjdNSEFcdTAwMjcsIFx1MDAyN0dRQVx1MDAyNywgXHUwMDI3TUxBXHUwMDI3XTpcbiAgICBzaXplcyA9IFtrdl9jYWNoZV9ieXRlcyhtZXRob2QsIGgsIGRfaGVhZCwgRywgY19rdiwgTCkgZm9yIEwgaW4gWzQwOTYsIDMyNzY4LCAxMzEwNzJdXVxuICAgIG1oYV8xMjhrID0ga3ZfY2FjaGVfYnl0ZXMoXHUwMDI3TUhBXHUwMDI3LCBoLCBkX2hlYWQsIEcsIGNfa3YsIDEzMTA3MilcbiAgICByYXRpbyA9IG1oYV8xMjhrIC8gc2l6ZXNbMl1cbiAgICBzeiA9IFtmXHUwMDI3e3MvMTAyNCoqMjouMWZ9TUJcdTAwMjcgZm9yIHMgaW4gc2l6ZXNdXG4gICAgcHJpbnQoZlx1MDAyN3ttZXRob2Q6XHUwMDNlNn0ge3N6WzBdOlx1MDAzZTEyfSB7c3pbMV06XHUwMDNlMTJ9IHtzelsyXTpcdTAwM2UxMn0ge3JhdGlvOlx1MDAzZTguMWZ9eFx1MDAyNylcbnByaW50KGZcdTAwMjdcXG5EZWVwU2Vlay1WMjogY19rdj17Y19rdn0gdnMgTUhBIHsyKmgqZF9oZWFkfSAtXHUwMDNlIHsyKmgqZF9oZWFkL2Nfa3Y6LjFmfXggcmF3IGNvbXByZXNzaW9uXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlY291cGxlZCBSb1BFIGZvciBQb3NpdGlvbiBFbmNvZGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUm90YXJ5IFBvc2l0aW9uIEVtYmVkZGluZ3MgKFJvUEUpIGFwcGx5IGEgcG9zaXRpb24tZGVwZW5kZW50IHJvdGF0aW9uIHRvIFEgYW5kIEsuIEluIHN0YW5kYXJkIGF0dGVudGlvbiwgYWZ0ZXIgYXBwbHlpbmcgUm9QRSB0byBLLCB0aGUgcm90YXRlZCB2YWx1ZXMgbXVzdCBiZSBjYWNoZWQg4oCUIGJ1dCB0aGUgcm90YXRpb24gZGVwZW5kcyBvbiBwb3NpdGlvbiBhbmQgY2Fubm90IGJlIHVuZG9uZSBmcm9tIHRoZSBsYXRlbnQgY+KCnC4gTUxBXHUwMDI3cyBzb2x1dGlvbjogZGVjb3VwbGUgdGhlIHBvc2l0aW9uYWwgY29tcG9uZW50LiBBIHNlcGFyYXRlIHBvc2l0aW9uYWwga2V5IGteUl90IChub3QgcGFydCBvZiB0aGUgbGF0ZW50KSBpcyBjb21wdXRlZCBmcm9tIHRoZSBoaWRkZW4gc3RhdGUsIFJvUEUtcm90YXRlZCwgYW5kIGNvbmNhdGVuYXRlZCB0byB0aGUgY29udGVudCBrZXkgcmVjb25zdHJ1Y3RlZCBmcm9tIHRoZSBsYXRlbnQuIFRoZSBwb3NpdGlvbmFsIGtleSBrXlJfdCBpcyBjYWNoZWQgc2VwYXJhdGVseSBidXQgaXMgc21hbGwgKGRfUiDiiaogaCDDlyBkX2hlYWQpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuZGVmIGFwcGx5X3JvcGUoeCwgc2VxX2xlbiwgYmFzZT0xMDAwMCk6XG4gICAgXCJcIlwiQXBwbHkgUm90YXJ5IFBvc2l0aW9uIEVtYmVkZGluZ3MgdG8geCBvZiBzaGFwZSAoQiwgaGVhZHMsIEwsIGQpLlwiXCJcIlxuICAgIGQgPSB4LnNoYXBlWy0xXVxuICAgIHBvcyA9IHRvcmNoLmFyYW5nZShzZXFfbGVuLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgIGludl9mcmVxID0gMS4wIC8gKGJhc2UgKiogKHRvcmNoLmFyYW5nZSgwLCBkLCAyKS5mbG9hdCgpIC8gZCkpXG4gICAgc2luID0gdG9yY2guc2luKHRvcmNoLm91dGVyKHBvcywgaW52X2ZyZXEpKSAgIyAoTCwgZC8vMilcbiAgICBjb3MgPSB0b3JjaC5jb3ModG9yY2gub3V0ZXIocG9zLCBpbnZfZnJlcSkpXG4gICAgeDEsIHgyID0geFsuLi4sIDo6Ml0sIHhbLi4uLCAxOjoyXVxuICAgIHJvdGF0ZWQgPSB0b3JjaC5zdGFjayhbeDEgKiBjb3MgLSB4MiAqIHNpbiwgeDEgKiBzaW4gKyB4MiAqIGNvc10sIGRpbT0tMSlcbiAgICByZXR1cm4gcm90YXRlZC5mbGF0dGVuKC0yKVxuXG5jbGFzcyBNTEFEZWNvdXBsZWRSb1BFKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiRGVjb3VwbGVkIFJvUEU6IHNtYWxsIHBvc2l0aW9uYWwga2V5cyBjYWNoZWQgYWxvbmdzaWRlIE1MQSBsYXRlbnQuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWwsIGgsIGRfaGVhZCwgY19rdiwgZF9yb3BlPTMyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuaCwgc2VsZi5kLCBzZWxmLmRyID0gaCwgZF9oZWFkLCBkX3JvcGVcbiAgICAgICAgc2VsZi5XX3Ffbm9wZSA9IG5uLkxpbmVhcihkX21vZGVsLCBoICogZF9oZWFkLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLldfcV9yb3BlID0gbm4uTGluZWFyKGRfbW9kZWwsIGggKiBkX3JvcGUsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuV19ka3YgICAgPSBubi5MaW5lYXIoZF9tb2RlbCwgY19rdiwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XX3VrICAgICA9IG5uLkxpbmVhcihjX2t2LCBoICogZF9oZWFkLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLldfa3IgICAgID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfcm9wZSwgYmlhcz1GYWxzZSkgICMgcG9zaXRpb25hbCBrZXkgKHNoYXJlZClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBCLCBMLCBfID0geC5zaGFwZVxuICAgICAgICBxX25vcGUgPSBzZWxmLldfcV9ub3BlKHgpLnZpZXcoQiwgTCwgc2VsZi5oLCBzZWxmLmQpXG4gICAgICAgIHFfcm9wZSA9IGFwcGx5X3JvcGUoc2VsZi5XX3Ffcm9wZSh4KS52aWV3KEIsIEwsIHNlbGYuaCwgc2VsZi5kcikudHJhbnNwb3NlKDEsMiksIEwpLnRyYW5zcG9zZSgxLDIpXG4gICAgICAgIGMgICA9IHNlbGYuV19ka3YoeCkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBsYXRlbnQgKGNhY2hlIHRoaXMpXG4gICAgICAgIGtfYyA9IHNlbGYuV191ayhjKS52aWV3KEIsIEwsIHNlbGYuaCwgc2VsZi5kKSAgICAgICAgICAgICAjIGNvbnRlbnQga2V5IGZyb20gbGF0ZW50XG4gICAgICAgIGtfciA9IGFwcGx5X3JvcGUoc2VsZi5XX2tyKHgpLnVuc3F1ZWV6ZSgyKS5leHBhbmQoQixMLHNlbGYuaCxzZWxmLmRyKS50cmFuc3Bvc2UoMSwyKSwgTCkudHJhbnNwb3NlKDEsMilcbiAgICAgICAgcmV0dXJuIGMsIGtfciAgIyBjYWNoZTogbGF0ZW50ICsgcG9zaXRpb25hbCBrZXlcblxubW9kZWwgPSBNTEFEZWNvdXBsZWRSb1BFKGRfbW9kZWw9MjU2LCBoPTQsIGRfaGVhZD0zMiwgY19rdj02NCwgZF9yb3BlPTE2KVxueCA9IHRvcmNoLnJhbmRuKDIsIDE2LCAyNTYpXG5jLCBrX3IgPSBtb2RlbCh4KVxucHJpbnQoZlx1MDAyN0xhdGVudCAoY29udGVudCBjYWNoZSk6IHtjLnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdQb3NpdGlvbmFsIGtleSAocm9wZSBjYWNoZSk6IHtrX3Iuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1RvdGFsIGNhY2hlIHBlciB0b2tlbjoge2Muc2hhcGVbLTFdICsga19yLnNoYXBlWy0xXX0gZmxvYXRzICh2cyB7Mio0KjMyfSBmb3IgTUhBKVx1MDAyNykifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQ2FjaGUgcGVyIHRva2VuIChmbG9hdHMpIiwiQ29tcHJlc3Npb24gdnMgTUhBIiwiRXh0cmEgaW5mZXJlbmNlIGNvbXB1dGUiLCJRdWFsaXR5IiwiVXNlZCBpbiJdLCJyb3dzIjpbWyJNSEEiLCIyIMOXIGggw5cgZF9oZWFkIiwiMcOXIChiYXNlbGluZSkiLCJOb25lIiwiQmVzdCIsIkdQVC0yLCBCRVJULCBMTGFNQSAxIl0sWyJHUUEiLCIyIMOXIEcgw5cgZF9oZWFkIiwiaC9Hw5cgKGUuZy4gOMOXKSIsInJlcGVhdF9pbnRlcmxlYXZlIGV4cGFuZCIsIuKJiE1IQSAoR+KJpTQpIiwiTExhTUEgMi8zLCBNaXN0cmFsLCBHZW1tYSJdLFsiTUxBIiwiY19LViAoKyBkX3JvcGUgZm9yIGRlY291cGxlZCkiLCJ+NeKAkzY0w5cgZGVwZW5kaW5nIG9uIGNfS1YiLCJVcC1wcm9qZWN0IFdfVUssIFdfVVYgcGVyIHN0ZXAiLCJNYXRjaGVzIE1IQSIsIkRlZXBTZWVrLVYyLCBEZWVwU2Vlay1WMyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcHJlc3Npb24gUmF0aW8gYW5kIE1vZGVsIFF1YWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZXBTZWVrLVYyIHVzZXMgY19LViA9IDUxMiB3aXRoIGg9MTI4IGhlYWRzIGFuZCBkX2hlYWQ9MTI4LiBUaGUgTUhBIGNhY2hlIHdvdWxkIGJlIDIgw5cgMTI4IMOXIDEyOCA9IDMyNzY4IGZsb2F0cyBwZXIgdG9rZW47IE1MQSBjYWNoZXMgNTEyIGZsb2F0cyDigJQgYSA2NMOXIHJhdyByZWR1Y3Rpb24uIEFmdGVyIGFjY291bnRpbmcgZm9yIHRoZSBzbWFsbCBkZWNvdXBsZWQgUm9QRSBjYWNoZSAoZF9SID0gNjQgcGVyIHRva2VuKSwgdGhlIGVmZmVjdGl2ZSBjYWNoZSBpcyA1NzYgZmxvYXRzIHZzIDMyNzY4OiBhcHByb3hpbWF0ZWx5IDU3w5cgc21hbGxlci4gT24gdGhlIE1NTFUsIEh1bWFuRXZhbCwgYW5kIEdTTThLIGJlbmNobWFya3MsIERlZXBTZWVrLVYyICgyMzZCIE1vRSwgMjFCIGFjdGl2ZSkgb3V0cGVyZm9ybXMgR1BULTQgbGV2ZWwgYmFzZWxpbmVzIHdoaWxlIHVzaW5nIHRoaXMgY29tcHJlc3NlZCBLViBzY2hlbWUgdG8gc2VydmUgMTI4SyBjb250ZXh0IGF0IHNjYWxlLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTUxBIHZzIEdRQSBUcmFkZS1vZmYiLCJjb250ZW50IjoiR1FBIHJlZHVjZXMgY2FjaGUgYnkgZ3JvdXBpbmcgaGVhZHMg4oCUIG5vIGV4dHJhIGNvbXB1dGF0aW9uLCBidXQgbGltaXRlZCBieSBHIOKJpSAxLiBNTEEgcmVkdWNlcyBjYWNoZSBieSBsb3ctcmFuayBjb21wcmVzc2lvbiDigJQgYWRkcyBXX1VLIGFuZCBXX1VWIHJlY29uc3RydWN0aW9uIHBlciBzdGVwLCBidXQgY2FuIGFjaGlldmUgbXVjaCBoaWdoZXIgY29tcHJlc3Npb24gaW5kZXBlbmRlbnRseSBvZiBoZWFkIGNvdW50LiBGb3IgdmVyeSBsb25nIGNvbnRleHRzIChMIFx1MDAzZSA2NEspIHdoZXJlIEtWIGNhY2hlIGRvbWluYXRlcyBtZW1vcnksIE1MQVx1MDAyN3MgYWdncmVzc2l2ZSBjb21wcmVzc2lvbiBvdXR3ZWlnaHMgaXRzIGNvbXB1dGUgb3ZlcmhlYWQuIEdRQSByZW1haW5zIHNpbXBsZXIgYW5kIGxvd2VyLWxhdGVuY3kgZm9yIG1vZGVyYXRlIGNvbnRleHRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlZXBTZWVrLVYyIGFuZCBWMyBBcmNoaXRlY3R1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZXBTZWVrLVYyICgyMDI0KSBpbnRyb2R1Y2VkIE1MQSBpbiBhIDIzNkIgcGFyYW1ldGVyIE1peHR1cmUtb2YtRXhwZXJ0cyBtb2RlbCB3aXRoIDIxQiBwYXJhbWV0ZXJzIGFjdGl2ZSBwZXIgdG9rZW4uIFRoZSBtb2RlbCBhY2hpZXZlcyBjb21wZXRpdGl2ZSBwZXJmb3JtYW5jZSB3aXRoIEdQVC00IGNsYXNzIG1vZGVscyB3aGlsZSBiZWluZyBkZXBsb3lhYmxlIGF0IGxvd2VyIEtWIGNhY2hlIGNvc3QuIERlZXBTZWVrLVYzICgyMDI0KSBzY2FsZWQgdG8gNjcxQiB0b3RhbCAvIDM3QiBhY3RpdmUgcGFyYW1ldGVycyB3aXRoIGZ1cnRoZXIgYXJjaGl0ZWN0dXJhbCByZWZpbmVtZW50cy4gQm90aCBtb2RlbHMgdXNlIE1MQSBpbiBjb25qdW5jdGlvbiB3aXRoIGEgTXVsdGktaGVhZCBMYXRlbnQgUXVlcnkgKE1MUSkg4oCUIGxvdy1yYW5rIFEgY29tcHJlc3Npb24g4oCUIHRob3VnaCBRIGNvbXByZXNzaW9uIGRvZXMgbm90IGFmZmVjdCB0aGUgS1YgY2FjaGUgc2luY2UgUSBpcyBub3QgY2FjaGVkIGR1cmluZyBhdXRvcmVncmVzc2l2ZSBnZW5lcmF0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRGVlcFNlZWstVjI6IDIzNkIgdG90YWwsIDIxQiBhY3RpdmUgKE1vRSksIGNfS1Y9NTEyLCBkX1I9NjQsIDEyOEsgY29udGV4dCB2aWEgTUxBLiIsIkRlZXBTZWVrLVYzOiA2NzFCIHRvdGFsLCAzN0IgYWN0aXZlLCByZWZpbmVkIE1MQSB3aXRoIGltcHJvdmVkIHVwLXByb2plY3Rpb24gaW5pdGlhbGlzYXRpb24uIiwiTUxBIGNhbiBiZSBjb21iaW5lZCB3aXRoIEdRQS1zdHlsZSBncm91cGluZzogZG93bi1wcm9qZWN0IHBlciBncm91cCBmb3IgYWRkaXRpb25hbCBzYXZpbmdzLiIsIlVwLXByb2plY3Rpb24gbWF0cmljZXMgV19VSyBhbmQgV19VViBhcmUgZnVzZWQgaW50byBhIHNpbmdsZSBsaW5lYXIgb3AgYXQgaW5mZXJlbmNlIGZvciBlZmZpY2llbmN5LiIsIkRlY291cGxlZCBSb1BFIChkX1I9NjQpIGFkZHMgb25seSA2NCBjYWNoZWQgZmxvYXRzIHBlciB0b2tlbiB2cyAxNjM4NCBmb3IgZnVsbCBwb3NpdGlvbmFsIGtleXMuIiwiTUxBIHdvcmtzIGJlc3Qgd2hlbiBjX0tWIOKJqiAyIMOXIGggw5cgZF9oZWFkOyB0eXBpY2FsIHJhdGlvIGNfS1YgLyAoMmhkKSBpcyAwLjAy4oCTMC4xMC4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Multi-Head Latent Attention (MLA) — DeepSeek's KV Compression

Multi-Head Latent Attention (MLA), introduced in DeepSeek-V2 (2024), compresses the KV cache into low-rank latent vectors rather than grouping heads as GQA does. The core idea: instead of caching G × d_head keys and values per token, MLA down-projects the hidden state to a single c_KV-dimensional latent vector cₜ = W_DKV hₜ where c_KV ≪ d_model. At inference, K and V are reconstructed on the fly from cₜ via learned up-projection matrices. Only cₜ is stored in the cache, achieving a compression ratio of c_KV / (2 × h × d_head) — approximately 5× vs MHA for DeepSeek-V2.

## Standard KV Cache and Its Memory Cost

For a model with h heads and head dimension d_head, the MHA KV cache per token per layer is 2 × h × d_head floats. DeepSeek-V2 uses h=128 heads with d_head=128, giving 2 × 128 × 128 = 32768 floats per token per layer. At L=128K tokens (the target context), this is 32768 × 128K × 2 bytes (float16) ≈ 8 GB per layer. MLA reduces the cache to c_KV floats per token — DeepSeek-V2 uses c_KV=512, storing 512 floats instead of 32768: a 64× raw reduction in cache elements.

## MLA: Low-Rank KV Compression

MLA replaces the separate W_K and W_V projections with a shared down-projection W_DKV ∈ ℝ^{c_KV × d_model} followed by separate up-projections W_UK ∈ ℝ^{(h × d_head) × c_KV} and W_UV ∈ ℝ^{(h × d_head) × c_KV}. At each token position t: latent cₜ = W_DKV hₜ (c_KV dims); K = W_UK cₜ (reconstructed, not cached); V = W_UV cₜ (reconstructed, not cached). Only cₜ is appended to the cache. At inference, past cₜ values are retrieved and K,V are reconstructed for the full cached sequence before attention is computed.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MultiHeadLatentAttention(nn.Module):
    def __init__(self, d_model, num_heads, d_head, c_kv):
        super().__init__()
        self.h, self.d, self.c = num_heads, d_head, c_kv
        self.W_q  = nn.Linear(d_model, num_heads * d_head, bias=False)
        self.W_dkv = nn.Linear(d_model, c_kv, bias=False)       # down-project to latent
        self.W_uk  = nn.Linear(c_kv, num_heads * d_head, bias=False)  # up-project to K
        self.W_uv  = nn.Linear(c_kv, num_heads * d_head, bias=False)  # up-project to V
        self.W_o   = nn.Linear(num_heads * d_head, d_model, bias=False)

    def forward(self, x):
        B, L, _ = x.shape
        Q = self.W_q(x).view(B, L, self.h, self.d).transpose(1, 2)  # (B,h,L,d)
        c = self.W_dkv(x)                                              # (B,L,c_kv) -- latent
        K = self.W_uk(c).view(B, L, self.h, self.d).transpose(1, 2)  # reconstruct K
        V = self.W_uv(c).view(B, L, self.h, self.d).transpose(1, 2)  # reconstruct V
        attn = F.softmax(Q @ K.transpose(-2,-1) / math.sqrt(self.d), dim=-1)
        out = (attn @ V).transpose(1, 2).reshape(B, L, -1)
        return self.W_o(out), c  # return latent for caching

d_model, h, d_head, c_kv = 512, 8, 64, 128
model = MultiHeadLatentAttention(d_model, h, d_head, c_kv)
x = torch.randn(2, 32, d_model)
out, latent = model(x)
print(f'Output: {out.shape}, Latent (to cache): {latent.shape}')
kv_mha  = 2 * h * d_head  # per token, per layer
kv_mla  = c_kv
print(f'MHA KV per token: {kv_mha}, MLA KV per token: {kv_mla} ({kv_mha/kv_mla:.1f}x smaller)')
```

## Inference with Compressed KV Cache

At generation time MLA caches only the c_KV-dimensional latent vector for each past token. To compute attention for the current token: retrieve all past latents from the cache (shape: L_past × c_KV per layer), up-project each to get K and V, then compute attention. The up-projections W_UK and W_UV add extra computation but this is bounded by O(L × c_KV × h × d_head) which is small compared to attention for large L. The key trade: compute (reconstructing K,V) for memory (storing only cₜ).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MLAInferenceCache:
    def __init__(self, max_len, c_kv, num_heads, d_head,
                 W_uk: nn.Linear, W_uv: nn.Linear):
        self.c_cache = torch.zeros(1, max_len, c_kv)  # only latents cached
        self.W_uk, self.W_uv = W_uk, W_uv
        self.h, self.d, self.t = num_heads, d_head, 0

    def step(self, q, c_new):
        """q: (1,h,1,d)  c_new: (1,1,c_kv) latent for current token."""
        self.c_cache[:, self.t:self.t+1] = c_new
        self.t += 1
        c_past = self.c_cache[:, :self.t]        # (1,t,c_kv)
        K = self.W_uk(c_past).view(1, self.t, self.h, self.d).transpose(1,2)  # (1,h,t,d)
        V = self.W_uv(c_past).view(1, self.t, self.h, self.d).transpose(1,2)
        scores = q @ K.transpose(-2,-1) / math.sqrt(self.d)
        return F.softmax(scores, dim=-1) @ V

d_model, h, d_head, c_kv, max_len = 256, 4, 32, 64, 128
W_uk = nn.Linear(c_kv, h * d_head, bias=False)
W_uv = nn.Linear(c_kv, h * d_head, bias=False)
W_dkv = nn.Linear(d_model, c_kv, bias=False)
W_q   = nn.Linear(d_model, h * d_head, bias=False)
cache = MLAInferenceCache(max_len, c_kv, h, d_head, W_uk, W_uv)
for step in range(20):
    x_t = torch.randn(1, 1, d_model)
    q = W_q(x_t).view(1, h, 1, d_head)
    c = W_dkv(x_t)             # (1,1,c_kv)
    out = cache.step(q, c)
print(f'After {cache.t} steps, cache holds {cache.t} latents of dim {c_kv}')
print(f'Cache bytes (float32): {cache.t * c_kv * 4}')
print(f'Equivalent MHA cache : {cache.t * h * d_head * 2 * 4} bytes ({2*h*d_head//c_kv:.0f}x larger)')
```

## KV Cache Memory: MHA vs GQA vs MLA

The three approaches represent a spectrum of KV cache compression. MHA stores all h×d_head keys and values; GQA stores only G×d_head (G < h); MLA stores a c_KV-dimensional latent and reconstructs K,V on the fly. MLA achieves the smallest cache footprint but adds reconstruction compute. For very long sequences (L > 100K), MLA's cache advantage is dominant — reconstruction compute is O(L × c_KV × h × d_head) which remains tractable relative to the memory savings.

```python
import torch

def kv_cache_bytes(method, h, d_head, G, c_kv, L, dtype_bytes=2):
    """Compute KV cache size in bytes for a single layer, L tokens."""
    if method == 'MHA':
        return 2 * h * d_head * L * dtype_bytes
    elif method == 'GQA':
        return 2 * G * d_head * L * dtype_bytes
    elif method == 'MLA':
        return c_kv * L * dtype_bytes  # only latent cached
    raise ValueError(method)

h, d_head = 64, 128  # LLaMA/DeepSeek scale
G, c_kv   = 8, 512   # GQA groups and MLA latent dim
print(f"{'Method':>6} {'L=4K':>12} {'L=32K':>12} {'L=128K':>12} {'vs MHA':>10}")
for method in ['MHA', 'GQA', 'MLA']:
    sizes = [kv_cache_bytes(method, h, d_head, G, c_kv, L) for L in [4096, 32768, 131072]]
    mha_128k = kv_cache_bytes('MHA', h, d_head, G, c_kv, 131072)
    ratio = mha_128k / sizes[2]
    sz = [f'{s/1024**2:.1f}MB' for s in sizes]
    print(f'{method:>6} {sz[0]:>12} {sz[1]:>12} {sz[2]:>12} {ratio:>8.1f}x')
print(f'\nDeepSeek-V2: c_kv={c_kv} vs MHA {2*h*d_head} -> {2*h*d_head/c_kv:.1f}x raw compression')
```

## Decoupled RoPE for Position Encoding

Rotary Position Embeddings (RoPE) apply a position-dependent rotation to Q and K. In standard attention, after applying RoPE to K, the rotated values must be cached — but the rotation depends on position and cannot be undone from the latent cₜ. MLA's solution: decouple the positional component. A separate positional key k^R_t (not part of the latent) is computed from the hidden state, RoPE-rotated, and concatenated to the content key reconstructed from the latent. The positional key k^R_t is cached separately but is small (d_R ≪ h × d_head).

```python
import torch
import torch.nn as nn
import math

def apply_rope(x, seq_len, base=10000):
    """Apply Rotary Position Embeddings to x of shape (B, heads, L, d)."""
    d = x.shape[-1]
    pos = torch.arange(seq_len, dtype=torch.float32)
    inv_freq = 1.0 / (base ** (torch.arange(0, d, 2).float() / d))
    sin = torch.sin(torch.outer(pos, inv_freq))  # (L, d//2)
    cos = torch.cos(torch.outer(pos, inv_freq))
    x1, x2 = x[..., ::2], x[..., 1::2]
    rotated = torch.stack([x1 * cos - x2 * sin, x1 * sin + x2 * cos], dim=-1)
    return rotated.flatten(-2)

class MLADecoupledRoPE(nn.Module):
    """Decoupled RoPE: small positional keys cached alongside MLA latent."""
    def __init__(self, d_model, h, d_head, c_kv, d_rope=32):
        super().__init__()
        self.h, self.d, self.dr = h, d_head, d_rope
        self.W_q_nope = nn.Linear(d_model, h * d_head, bias=False)
        self.W_q_rope = nn.Linear(d_model, h * d_rope, bias=False)
        self.W_dkv    = nn.Linear(d_model, c_kv, bias=False)
        self.W_uk     = nn.Linear(c_kv, h * d_head, bias=False)
        self.W_kr     = nn.Linear(d_model, d_rope, bias=False)  # positional key (shared)

    def forward(self, x):
        B, L, _ = x.shape
        q_nope = self.W_q_nope(x).view(B, L, self.h, self.d)
        q_rope = apply_rope(self.W_q_rope(x).view(B, L, self.h, self.dr).transpose(1,2), L).transpose(1,2)
        c   = self.W_dkv(x)                                        # latent (cache this)
        k_c = self.W_uk(c).view(B, L, self.h, self.d)             # content key from latent
        k_r = apply_rope(self.W_kr(x).unsqueeze(2).expand(B,L,self.h,self.dr).transpose(1,2), L).transpose(1,2)
        return c, k_r  # cache: latent + positional key

model = MLADecoupledRoPE(d_model=256, h=4, d_head=32, c_kv=64, d_rope=16)
x = torch.randn(2, 16, 256)
c, k_r = model(x)
print(f'Latent (content cache): {c.shape}')
print(f'Positional key (rope cache): {k_r.shape}')
print(f'Total cache per token: {c.shape[-1] + k_r.shape[-1]} floats (vs {2*4*32} for MHA)')
```

| Method | Cache per token (floats) | Compression vs MHA | Extra inference compute | Quality | Used in |
| --- | --- | --- | --- | --- | --- |
| MHA | 2 × h × d_head | 1× (baseline) | None | Best | GPT-2, BERT, LLaMA 1 |
| GQA | 2 × G × d_head | h/G× (e.g. 8×) | repeat_interleave expand | ≈MHA (G≥4) | LLaMA 2/3, Mistral, Gemma |
| MLA | c_KV (+ d_rope for decoupled) | ~5–64× depending on c_KV | Up-project W_UK, W_UV per step | Matches MHA | DeepSeek-V2, DeepSeek-V3 |

## Compression Ratio and Model Quality

DeepSeek-V2 uses c_KV = 512 with h=128 heads and d_head=128. The MHA cache would be 2 × 128 × 128 = 32768 floats per token; MLA caches 512 floats — a 64× raw reduction. After accounting for the small decoupled RoPE cache (d_R = 64 per token), the effective cache is 576 floats vs 32768: approximately 57× smaller. On the MMLU, HumanEval, and GSM8K benchmarks, DeepSeek-V2 (236B MoE, 21B active) outperforms GPT-4 level baselines while using this compressed KV scheme to serve 128K context at scale.

> **MLA vs GQA Trade-off**: GQA reduces cache by grouping heads — no extra computation, but limited by G ≥ 1. MLA reduces cache by low-rank compression — adds W_UK and W_UV reconstruction per step, but can achieve much higher compression independently of head count. For very long contexts (L > 64K) where KV cache dominates memory, MLA's aggressive compression outweighs its compute overhead. GQA remains simpler and lower-latency for moderate contexts.

## DeepSeek-V2 and V3 Architecture

DeepSeek-V2 (2024) introduced MLA in a 236B parameter Mixture-of-Experts model with 21B parameters active per token. The model achieves competitive performance with GPT-4 class models while being deployable at lower KV cache cost. DeepSeek-V3 (2024) scaled to 671B total / 37B active parameters with further architectural refinements. Both models use MLA in conjunction with a Multi-head Latent Query (MLQ) — low-rank Q compression — though Q compression does not affect the KV cache since Q is not cached during autoregressive generation.

- DeepSeek-V2: 236B total, 21B active (MoE), c_KV=512, d_R=64, 128K context via MLA.
- DeepSeek-V3: 671B total, 37B active, refined MLA with improved up-projection initialisation.
- MLA can be combined with GQA-style grouping: down-project per group for additional savings.
- Up-projection matrices W_UK and W_UV are fused into a single linear op at inference for efficiency.
- Decoupled RoPE (d_R=64) adds only 64 cached floats per token vs 16384 for full positional keys.
- MLA works best when c_KV ≪ 2 × h × d_head; typical ratio c_KV / (2hd) is 0.02–0.10.

---

