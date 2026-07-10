---
title: "QLoRA — 4-bit NF4 Quantization with LoRA for Memory-Efficient Fine-Tuning"
slug: "qlora"
description: "Complete guide to QLoRA (Dettmers et al., 2023): NF4 information-theoretically optimal 4-bit quantization, double quantization of scaling constants, paged Adam optimizer, and how to fine-tune 70B+ LLMs on a single GPU using bitsandbytes and HuggingFace PEFT."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUUxvUkEgKERldHRtZXJzIGV0IGFsLiwgMjAyMykgY29tYmluZXMgNC1iaXQgTkY0IChOb3JtYWxGbG9hdDQpIHF1YW50aXphdGlvbiBvZiB0aGUgZnJvemVuIGJhc2UgbW9kZWwgd2l0aCBmdWxsLXByZWNpc2lvbiBMb1JBIGFkYXB0ZXJzIHRvIGFjaGlldmUgdW5wcmVjZWRlbnRlZCBtZW1vcnkgZWZmaWNpZW5jeSBmb3IgTExNIGZpbmUtdHVuaW5nLiBBIDY1QiBMTGFNQSBtb2RlbCByZXF1aXJlcyB+MTMwR0IgaW4gZnAxNiDigJQgcmVxdWlyaW5nIG11bHRpcGxlIEExMDAgODBHQiBHUFVzLiBRTG9SQSByZWR1Y2VzIHRoaXMgdG8gfjM1R0IgYnkgcXVhbnRpemluZyBmcm96ZW4gYmFzZSB3ZWlnaHRzIHRvIDQtYml0IE5GNCwgZW5hYmxpbmcgc2luZ2xlLUdQVSBmaW5lLXR1bmluZyBvZiA2NUIgbW9kZWxzIG9uIGFuIEExMDAgODBHQiBhbmQgN0IgZmluZS10dW5pbmcgb24gYSBjb25zdW1lciBSVFggMzA5MCAyNEdCLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBNZW1vcnkgV2FsbCBpbiBMTE0gRmluZS1UdW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxMTSBmaW5lLXR1bmluZyBtZW1vcnkgY29uc3VtcHRpb24gY29tZXMgZnJvbSBmb3VyIHNvdXJjZXM6IG1vZGVsIHdlaWdodHMsIGdyYWRpZW50IHRlbnNvcnMgKHNhbWUgc2l6ZSBhcyB3ZWlnaHRzKSwgQWRhbSBvcHRpbWl6ZXIgc3RhdGVzIChtb21lbnR1bSArIHZhcmlhbmNlLCBlYWNoIGZwMzIgPSAyw5cgd2VpZ2h0IHNpemUpLCBhbmQgYWN0aXZhdGlvbiBtZW1vcnkgZm9yIGJhY2twcm9wYWdhdGlvbi4gRm9yIGEgN0IgbW9kZWwgaW4gZnAxNjogd2VpZ2h0cyA9IDE0R0IsIGdyYWRpZW50cyA9IDE0R0IsIEFkYW0gc3RhdGVzID0gNTZHQiAoZnAzMikg4oCUIHRvdGFsaW5nIH44NEdCIGJlZm9yZSBhY3RpdmF0aW9ucy4gUUxvUkFcdTAwMjdzIGluc2lnaHQ6IHRoZSBiYXNlIHdlaWdodHMgb25seSBuZWVkIGhpZ2ggcHJlY2lzaW9uIGR1cmluZyB0aGUgTG9SQSBhZGFwdGVyIGNvbXB1dGF0aW9uLCBub3QgZm9yIHN0b3JhZ2UuIFN0b3JlIGluIDQtYml0LCBkZXF1YW50aXplIG9uLXRoZS1mbHkgb25seSBmb3IgdGhlIGZvcndhcmQgYW5kIGJhY2t3YXJkIHBhc3MuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJmcDMyIGZ1bGwgZmluZS10dW5lOiB+MjQgYnl0ZXMvcGFyYW0g4oCUIDE2OEdCIGZvciA3QiwgMS43VEIgZm9yIDcwQiIsImZwMTYvYmYxNiBmdWxsIGZpbmUtdHVuZTogfjE2IGJ5dGVzL3BhcmFtIOKAlCAxMTJHQiBmb3IgN0IsIDEuMVRCIGZvciA3MEIiLCJMb1JBIChmcDE2IGJhc2UpOiB+MTRHQiB3ZWlnaHRzICsgfjJHQiBhZGFwdGVyICsgfjRHQiBvcHRpbWl6ZXIgPSB+MjBHQiBmb3IgN0IiLCJRTG9SQSAoTkY0IDQtYml0IGJhc2UpOiB+My41R0Igd2VpZ2h0cyArIH4yR0IgYWRhcHRlciArIH40R0Igb3B0aW1pemVyID0gfjkuNUdCIGZvciA3QiIsIlFMb1JBIHdpdGggZG91YmxlIHF1YW50aXphdGlvbjogfjMuMjVHQiB3ZWlnaHRzICsgYWRhcHRlcnMgKyBvcHRpbWl6ZXIg4omIIDlHQiBmb3IgN0IiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTkY0IOKAlCBJbmZvcm1hdGlvbi1UaGVvcmV0aWNhbGx5IE9wdGltYWwgNC1iaXQgUXVhbnRpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBJTlQ0IHF1YW50aXphdGlvbiBwbGFjZXMgMTYgcXVhbnRpemF0aW9uIGxldmVscyBhdCBlcXVhbCBpbnRlcnZhbHMgaW4gW21pbiwgbWF4XSwgYXNzdW1pbmcgd2VpZ2h0cyBhcmUgdW5pZm9ybWx5IGRpc3RyaWJ1dGVkLiBMTE0gd2VpZ2h0cyBhcmUgbmVhci1HYXVzc2lhbiBOKDAsIM+DwrIpLiBORjQgKE5vcm1hbEZsb2F0NCkgZXhwbG9pdHMgdGhpczogcXVhbnRpemF0aW9uIGxldmVscyBhcmUgcGxhY2VkIGF0IHRoZSBxdWFudGlsZXMgb2YgTigwLDEpLCBzcGFjaW5nIHRoZW0gY2xvc2VyIHRvZ2V0aGVyIHdoZXJlIHRoZSBkZW5zaXR5IGlzIGhpZ2hlc3QgKG5lYXIgemVybykgYW5kIGZ1cnRoZXIgYXBhcnQgaW4gdGhlIHRhaWxzLiBUaGlzIGlzIGluZm9ybWF0aW9uLXRoZW9yZXRpY2FsbHkgb3B0aW1hbCDigJQgZWFjaCA0LWJpdCBjb2Rld29yZCBjYXJyaWVzIGVxdWFsIGluZm9ybWF0aW9uIHVuZGVyIHRoZSBHYXVzc2lhbiBwcmlvci4gVGhlIHJlc3VsdCBpcyBsb3dlciByZWNvbnN0cnVjdGlvbiBlcnJvciB0aGFuIElOVDQgYXQgdGhlIHNhbWUgYml0IHdpZHRoLiJ9LHsidHlwZSI6Im1hdGgiLCJjb250ZW50IjoicV9pID0gUV97TigwLDEpfVxcIVxcbGVmdChcXGZyYWN7aSArIDAuNX17Ml5rfVxccmlnaHQpLFxccXVhZCBpID0gMCwgMSwgXFxsZG90cywgMl5rIC0gMSxcXHF1YWQgayA9IDQiLCJkaXNwbGF5Ijp0cnVlfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJRTG9SQSBTZXR1cCDigJQgNC1iaXQgTkY0IE1vZGVsIHdpdGggTG9SQSBBZGFwdGVycyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplciwgQml0c0FuZEJ5dGVzQ29uZmlnXG5mcm9tIHBlZnQgaW1wb3J0IExvcmFDb25maWcsIGdldF9wZWZ0X21vZGVsLCBUYXNrVHlwZSwgcHJlcGFyZV9tb2RlbF9mb3Jfa2JpdF90cmFpbmluZ1xuXG4jIFN0ZXAgMTogQ29uZmlndXJlIDQtYml0IE5GNCBxdWFudGl6YXRpb24gd2l0aCBkb3VibGUgcXVhbnRpemF0aW9uXG5ibmJfY29uZmlnID0gQml0c0FuZEJ5dGVzQ29uZmlnKFxuICAgIGxvYWRfaW5fNGJpdD1UcnVlLFxuICAgIGJuYl80Yml0X3F1YW50X3R5cGU9XCJuZjRcIiwgICAgICAgICAgICMgTkY0IG9wdGltYWwgZm9yIEdhdXNzaWFuIHdlaWdodHNcbiAgICBibmJfNGJpdF9jb21wdXRlX2R0eXBlPXRvcmNoLmJmbG9hdDE2LCAgIyBEZXF1YW50aXplIHRvIGJmMTYgZm9yIG1hdG11bFxuICAgIGJuYl80Yml0X3VzZV9kb3VibGVfcXVhbnQ9VHJ1ZSwgICAgICAjIFF1YW50aXplIHRoZSBzY2FsaW5nIGNvbnN0YW50cyB0b29cbilcblxuIyBTdGVwIDI6IExvYWQgbW9kZWwgcXVhbnRpemVkIHRvIDQtYml0IE5GNFxubW9kZWwgPSBBdXRvTW9kZWxGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQoXG4gICAgXCJtZXRhLWxsYW1hL0xsYW1hLTItN2ItaGZcIixcbiAgICBxdWFudGl6YXRpb25fY29uZmlnPWJuYl9jb25maWcsXG4gICAgZGV2aWNlX21hcD1cImF1dG9cIixcbilcbnRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFwibWV0YS1sbGFtYS9MbGFtYS0yLTdiLWhmXCIpXG50b2tlbml6ZXIucGFkX3Rva2VuID0gdG9rZW5pemVyLmVvc190b2tlblxuXG4jIFN0ZXAgMzogUHJlcGFyZSBmb3Igay1iaXQgdHJhaW5pbmcg4oCUIGVuYWJsZXMgZ3JhZGllbnQgY2hlY2twb2ludGluZ1xubW9kZWwgPSBwcmVwYXJlX21vZGVsX2Zvcl9rYml0X3RyYWluaW5nKG1vZGVsKVxuXG4jIFN0ZXAgNDogQWRkIExvUkEgYWRhcHRlcnMgaW4gYmYxNiBvbiB0b3Agb2YgZnJvemVuIDQtYml0IGJhc2VcbmxvcmFfY29uZmlnID0gTG9yYUNvbmZpZyhcbiAgICB0YXNrX3R5cGU9VGFza1R5cGUuQ0FVU0FMX0xNLFxuICAgIHI9MTYsIGxvcmFfYWxwaGE9MzIsXG4gICAgdGFyZ2V0X21vZHVsZXM9W1wicV9wcm9qXCIsIFwidl9wcm9qXCIsIFwia19wcm9qXCIsIFwib19wcm9qXCJdLFxuICAgIGxvcmFfZHJvcG91dD0wLjA1LCBiaWFzPVwibm9uZVwiLFxuKVxucGVmdF9tb2RlbCA9IGdldF9wZWZ0X21vZGVsKG1vZGVsLCBsb3JhX2NvbmZpZylcbnBlZnRfbW9kZWwucHJpbnRfdHJhaW5hYmxlX3BhcmFtZXRlcnMoKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRHVyaW5nIHRoZSBmb3J3YXJkIHBhc3MsIGVhY2ggNC1iaXQgTkY0IHdlaWdodCBibG9jayBpcyBkZXF1YW50aXplZCB0byBiZjE2IG9uLXRoZS1mbHksIHRoZSBtYXRyaXggbXVsdGlwbGljYXRpb24gcnVucyBpbiBiZjE2LCBhbmQgdGhlIGRlcXVhbnRpemVkIHZhbHVlcyBhcmUgaW1tZWRpYXRlbHkgZGlzY2FyZGVkLiBPbmx5IHRoZSA0LWJpdCBpbnRlZ2VycyBhbmQgdGhlaXIgc2NhbGluZyBjb25zdGFudHMgcmVtYWluIGluIEdQVSBtZW1vcnkgZm9yIHRoZSBiYXNlIG1vZGVsLiBMb1JBIGFkYXB0ZXIgd2VpZ2h0cyBzdGF5IGluIGJmMTYvZnAzMiB0aHJvdWdob3V0IHRyYWluaW5nLiBHcmFkaWVudHMgZmxvdyBvbmx5IHRocm91Z2ggdGhlIGFkYXB0ZXIgcGFyYW1ldGVycyDigJQgdGhlIHF1YW50aXplZCBiYXNlIHdlaWdodHMgaGF2ZSBubyBncmFkaWVudHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTkY0IFF1YW50aXphdGlvbiBNZWNoYW5pY3MifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IG5vcm1cblxuZGVmIGNvbXB1dGVfbmY0X2xldmVscyhudW1fYml0czogaW50ID0gNCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiQ29tcHV0ZSBORjQgcXVhbnRpemF0aW9uIGxldmVsczogbWlkcG9pbnRzIG9mIGVxdWFsLXByb2IgaW50ZXJ2YWxzIG9mIE4oMCwxKS5cIlwiXCJcbiAgICBudW1fbGV2ZWxzID0gMiAqKiBudW1fYml0cyAgIyAxNiBsZXZlbHMgZm9yIDQtYml0XG4gICAgcXVhbnRpbGVfcG9zID0gbnAubGluc3BhY2UoMCwgMSwgbnVtX2xldmVscyArIDEpXG4gICAgbWlkcG9pbnRzID0gKHF1YW50aWxlX3Bvc1s6LTFdICsgcXVhbnRpbGVfcG9zWzE6XSkgLyAyXG4gICAgbGV2ZWxzID0gdG9yY2gudGVuc29yKG5vcm0ucHBmKG1pZHBvaW50cyksIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgcmV0dXJuIGxldmVscyAvIGxldmVscy5hYnMoKS5tYXgoKSAgIyBub3JtYWxpemUgdG8gWy0xLCAxXVxuXG5kZWYgbmY0X3F1YW50aXplKHdlaWdodDogdG9yY2guVGVuc29yLCBibG9ja19zaXplOiBpbnQgPSA2NCkgLVx1MDAzZSB0dXBsZTpcbiAgICBcIlwiXCJRdWFudGl6ZSB3ZWlnaHQgdGVuc29yIHRvIE5GNCB3aXRoIHBlci1ibG9jayBhYnNtYXggc2NhbGluZy5cIlwiXCJcbiAgICBuZjRfbHZscyA9IGNvbXB1dGVfbmY0X2xldmVscyg0KS50byh3ZWlnaHQuZGV2aWNlKVxuICAgIGJsb2NrcyA9IHdlaWdodC5yZXNoYXBlKC0xLCBibG9ja19zaXplKVxuICAgIHNjYWxlcyA9IGJsb2Nrcy5hYnMoKS5tYXgoZGltPTEsIGtlZXBkaW09VHJ1ZSkudmFsdWVzLmNsYW1wKG1pbj0xZS04KVxuICAgIG5vcm1hbGl6ZWQgPSBibG9ja3MgLyBzY2FsZXNcbiAgICBkaWZmcyA9IChub3JtYWxpemVkLnVuc3F1ZWV6ZSgtMSkgLSBuZjRfbHZscykuYWJzKClcbiAgICBpbmRpY2VzID0gZGlmZnMuYXJnbWluKGRpbT0tMSkudG8odG9yY2gudWludDgpICAjIDQtYml0IGluZGljZXMgKDAtMTUpXG4gICAgcmV0dXJuIGluZGljZXMsIHNjYWxlc1xuXG5kZWYgbmY0X2RlcXVhbnRpemUoaW5kaWNlczogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgIHNjYWxlczogdG9yY2guVGVuc29yLCBibG9ja19zaXplOiBpbnQgPSA2NCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiUmVjb25zdHJ1Y3QgZnAzMiB3ZWlnaHRzIGZyb20gTkY0IGluZGljZXMgYW5kIHBlci1ibG9jayBzY2FsZXMuXCJcIlwiXG4gICAgbmY0X2x2bHMgPSBjb21wdXRlX25mNF9sZXZlbHMoNCkudG8oc2NhbGVzLmRldmljZSlcbiAgICByZWNvbnN0cnVjdGVkID0gbmY0X2x2bHNbaW5kaWNlcy5sb25nKCldXG4gICAgcmV0dXJuIChyZWNvbnN0cnVjdGVkICogc2NhbGVzKS5yZXNoYXBlKC0xKVxudyA9IHRvcmNoLnJhbmRuKDI1NiwgMjU2KVxubmY0X2x2bHMgPSBjb21wdXRlX25mNF9sZXZlbHMoKVxucHJpbnQoZlwiTkY0IGxldmVscyAoY2VudHJhbCA4KToge25mNF9sdmxzWzQ6MTJdLnRvbGlzdCgpfVwiKVxuaWR4LCBzYyA9IG5mNF9xdWFudGl6ZSh3KVxud19yZWNvbiA9IG5mNF9kZXF1YW50aXplKGlkeCwgc2MpLnJlc2hhcGUoMjU2LCAyNTYpXG5ybXNlID0gKHcgLSB3X3JlY29uKS5wb3coMikubWVhbigpLnNxcnQoKS5pdGVtKClcbnByaW50KGZcIk5GNCBSTVNFOiB7cm1zZTouNWZ9ICB8ICBDb21wcmVzc2lvbjoge3cubnVtZWwoKSozMi8oaWR4Lm51bWVsKCkqNCtzYy5udW1lbCgpKjMyKTouMWZ9eFwiKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTkY0IGFsbG9jYXRlcyA4IG9mIGl0cyAxNiBsZXZlbHMgdG8gdGhlIGNlbnRyYWwgcmVnaW9uIHdoZXJlIG1vc3QgTExNIHdlaWdodCBtYXNzIHJlc2lkZXMsIHZzIElOVDQgd2hpY2ggYWxsb2NhdGVzIDQuIEZvciBhIHdlaWdodCBkaXN0cmlidXRpb24gd2l0aCDPgz0wLjAyLCBhcHByb3hpbWF0ZWx5IDY4JSBvZiB2YWx1ZXMgZmFsbCB3aXRoaW4gwrHPgyBvZiB6ZXJvIOKAlCBORjQgY292ZXJzIHRoaXMgZGVuc2UgcmVnaW9uIHdpdGggZG91YmxlIHRoZSByZXNvbHV0aW9uIG9mIElOVDQuIFRoaXMgZGVuc2l0eSBtYXRjaGluZyByZWR1Y2VzIHJlY29uc3RydWN0aW9uIE1TRSBieSAyNeKAkzMwJSBjb21wYXJlZCB0byBJTlQ0IGF0IHRoZSBzYW1lIGJpdCB3aWR0aCwgd2hpY2ggdHJhbnNsYXRlcyB0byBtZWFzdXJhYmxlIHF1YWxpdHkgaW1wcm92ZW1lbnRzIGZvciBkb3duc3RyZWFtIHRhc2sgcGVyZm9ybWFuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRG91YmxlIFF1YW50aXphdGlvbiDigJQgUXVhbnRpemluZyB0aGUgUXVhbnRpemF0aW9uIENvbnN0YW50cyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGRvdWJsZV9xdWFudGl6ZSh3ZWlnaHQ6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgaW5uZXJfYmxvY2s6IGludCA9IDY0LFxuICAgICAgICAgICAgICAgICAgICBvdXRlcl9ibG9jazogaW50ID0gMjU2KSAtXHUwMDNlIGRpY3Q6XG4gICAgXCJcIlwiXG4gICAgVHdvLWxldmVsIHF1YW50aXphdGlvbjogTkY0IGZvciB3ZWlnaHRzICg0IGJpdHMpLCBJTlQ4IGZvciBzY2FsZXMgKDggYml0cykuXG4gICAgUmVkdWNlcyBwZXItd2VpZ2h0IHNjYWxlIG92ZXJoZWFkIGZyb20gMC41IHRvIDAuMTI1IGJpdHMuXG4gICAgXCJcIlwiXG4gICAgIyBMZXZlbCAxOiBwZXItaW5uZXItYmxvY2sgZnAzMiBzY2FsZXMgZm9yIE5GNCBxdWFudGl6YXRpb25cbiAgICBibG9ja3MgPSB3ZWlnaHQucmVzaGFwZSgtMSwgaW5uZXJfYmxvY2spXG4gICAgc2NhbGVzX2ZwMzIgPSBibG9ja3MuYWJzKCkubWF4KGRpbT0xKS52YWx1ZXMgICAgICAgIyBbTl0gZnAzMiwgMzIgYml0cyBlYWNoXG5cbiAgICAjIExldmVsIDI6IHF1YW50aXplIGZwMzIgc2NhbGVzIHRvIElOVDggcGVyIG91dGVyX2Jsb2NrXG4gICAgbl9ncm91cHMgPSAoc2NhbGVzX2ZwMzIubnVtZWwoKSArIG91dGVyX2Jsb2NrIC8vIGlubmVyX2Jsb2NrIC0gMSkgLy8gKG91dGVyX2Jsb2NrIC8vIGlubmVyX2Jsb2NrKVxuICAgIGdyb3VwX3NpemUgPSBvdXRlcl9ibG9jayAvLyBpbm5lcl9ibG9ja1xuICAgIHBhZGRlZCA9IHRvcmNoLmNhdChbc2NhbGVzX2ZwMzIsIHNjYWxlc19mcDMyLm5ld196ZXJvcyhuX2dyb3VwcyAqIGdyb3VwX3NpemUgLSBzY2FsZXNfZnAzMi5udW1lbCgpKV0pXG4gICAgZ3JvdXBzID0gcGFkZGVkLnJlc2hhcGUobl9ncm91cHMsIGdyb3VwX3NpemUpXG4gICAgc3VwZXJfc2NhbGVzID0gZ3JvdXBzLmFicygpLm1heChkaW09MSwga2VlcGRpbT1UcnVlKS52YWx1ZXMuY2xhbXAoMWUtOClcbiAgICBzY2FsZXNfaW50OCA9IChncm91cHMgLyBzdXBlcl9zY2FsZXMgKiAxMjcpLnJvdW5kKCkuY2xhbXAoLTEyNywgMTI3KS50byh0b3JjaC5pbnQ4KVxuXG4gICAgIyBCaXQtY29zdCBhbmFseXNpc1xuICAgIGJpdHNfZnAzMiA9IDMyIC8gaW5uZXJfYmxvY2sgICAgICAgICAgICMgMC41MDAgYml0cy93ZWlnaHQgZm9yIGZwMzIgc2NhbGVzXG4gICAgYml0c19pbnQ4ID0gOCAvIGlubmVyX2Jsb2NrICAgICAgICAgICAgIyAwLjEyNSBiaXRzL3dlaWdodCBmb3IgaW50OCBzY2FsZXNcbiAgICBiaXRzX3N1cGVyID0gMzIgLyBvdXRlcl9ibG9jayAgICAgICAgICAjIDAuMTI1IGJpdHMvd2VpZ2h0IGZvciBzdXBlci1zY2FsZXNcbiAgICBwcmludChmXCJTY2FsZSBvdmVyaGVhZDogZnAzMj17Yml0c19mcDMyOi4zZn0gLVx1MDAzZSBpbnQ4PXtiaXRzX2ludDg6LjNmfSBiaXRzL3dlaWdodFwiKVxuICAgIHByaW50KGZcIlRvdGFsIE5GNCArIGRvdWJsZSBxdWFudDogezQgKyBiaXRzX2ludDggKyBiaXRzX3N1cGVyOi4zZn0gYml0cy93ZWlnaHRcIilcbiAgICByZXR1cm4ge1wic2NhbGVzX2ludDhcIjogc2NhbGVzX2ludDgsIFwic3VwZXJfc2NhbGVzXCI6IHN1cGVyX3NjYWxlc31cblxucmVzdWx0ID0gZG91YmxlX3F1YW50aXplKHRvcmNoLnJhbmRuKDQwOTYsIDQwOTYpKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRG91YmxlIHF1YW50aXphdGlvbiByZWR1Y2VzIHRoZSBzdG9yYWdlIG92ZXJoZWFkIG9mIHF1YW50aXphdGlvbiBjb25zdGFudHMgZnJvbSAwLjUgYml0cy93ZWlnaHQgKGZwMzIgc2NhbGUgcGVyIDY0IHdlaWdodHMpIHRvIGFwcHJveGltYXRlbHkgMC4xMjcgYml0cy93ZWlnaHQgKGludDggc2NhbGUgcGVyIDY0ICsgZnAzMiBzdXBlci1zY2FsZSBwZXIgMjU2KS4gQ29tYmluZWQgd2l0aCBORjRcdTAwMjdzIDQgYml0cyBwZXIgd2VpZ2h0LCB0aGUgdG90YWwgaXMgfjQuMTI3IGJpdHMvd2VpZ2h0LiBGb3IgYSA3MEIgbW9kZWwsIGRvdWJsZSBxdWFudGl6YXRpb24gc2F2ZXMgYXBwcm94aW1hdGVseSAzLjVHQiBvZiBHUFUgbWVtb3J5IOKAlCBlbm91Z2ggdG8gZml0IG9uIGEgNDBHQiBBMTAwIHRoYXQgd291bGQgb3RoZXJ3aXNlIHJlcXVpcmUgYSA4MEdCIHZhcmlhbnQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVtb3J5IFByb2ZpbGluZyDigJQgZnAxNiB2cyBMb1JBIHZzIFFMb1JBIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgZXN0aW1hdGVfdHJhaW5pbmdfbWVtb3J5X2diKG5fcGFyYW1zOiBmbG9hdCwgbW9kZTogc3RyLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhZGFwdGVyX2ZyYWM6IGZsb2F0ID0gMC4wMSkgLVx1MDAzZSBmbG9hdDpcbiAgICBcIlwiXCJFc3RpbWF0ZSBwZWFrIEdQVSB0cmFpbmluZyBtZW1vcnkgKEdCKSBmb3IgYSBtb2RlbCBieSBzaXplIGFuZCBtb2RlLlwiXCJcIlxuICAgIG4gPSBuX3BhcmFtcyAqIDFlOVxuICAgIGlmIG1vZGUgPT0gXCJmcDE2X2Z1bGxcIjpcbiAgICAgICAgIyBXZWlnaHRzIGZwMTYgKyBncmFkcyBmcDE2ICsgQWRhbSBmcDMyIG1vbWVudHVtICsgQWRhbSBmcDMyIHZhcmlhbmNlXG4gICAgICAgIHJldHVybiBuICogKDIgKyAyICsgNCArIDQpIC8gMWU5XG4gICAgZWxpZiBtb2RlID09IFwibG9yYV9mcDE2XCI6XG4gICAgICAgICMgRnJvemVuIGZwMTYgYmFzZSB3ZWlnaHRzICsgYWRhcHRlciBmcDE2ICsgQWRhbSBmcDMyIG9uIGFkYXB0ZXIgb25seVxuICAgICAgICBhZGFwdGVyX24gPSBuICogYWRhcHRlcl9mcmFjXG4gICAgICAgIHJldHVybiAobiAqIDIgKyBhZGFwdGVyX24gKiAyICsgYWRhcHRlcl9uICogKDQgKyA0KSkgLyAxZTlcbiAgICBlbGlmIG1vZGUgPT0gXCJxbG9yYV9uZjRcIjpcbiAgICAgICAgIyBORjQgYmFzZSAoMC41IGJ5dGVzL3BhcmFtKSArIGFkYXB0ZXIgYmYxNiArIEFkYW0gZnAzMiBvbiBhZGFwdGVyIG9ubHlcbiAgICAgICAgYWRhcHRlcl9uID0gbiAqIGFkYXB0ZXJfZnJhY1xuICAgICAgICByZXR1cm4gKG4gKiAwLjUgKyBhZGFwdGVyX24gKiAyICsgYWRhcHRlcl9uICogKDQgKyA0KSkgLyAxZTlcbiAgICByZXR1cm4gMC4wXG5cbnByaW50KGZcIntcdTAwMjdTaXplXHUwMDI3Olx1MDAzYzZ9IHtcdTAwMjdNb2RlXHUwMDI3Olx1MDAzYzE0fSB7XHUwMDI3UGVhayBHUFUgKEdCKVx1MDAyNzpcdTAwM2UxNH1cIilcbnByaW50KFwiLVwiICogMzYpXG5mb3Igbl9iLCBsYWJlbCBpbiBbKDcsIFwiN0JcIiksICgxMywgXCIxM0JcIiksICg3MCwgXCI3MEJcIildOlxuICAgIGZvciBtb2RlIGluIFtcImZwMTZfZnVsbFwiLCBcImxvcmFfZnAxNlwiLCBcInFsb3JhX25mNFwiXTpcbiAgICAgICAgZ2IgPSBlc3RpbWF0ZV90cmFpbmluZ19tZW1vcnlfZ2Iobl9iLCBtb2RlKVxuICAgICAgICBwcmludChmXCJ7bGFiZWw6XHUwMDNjNn0ge21vZGU6XHUwMDNjMTR9IHtnYjpcdTAwM2UxNC4xZn1cIikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVzdGltYXRlZCBwZWFrIEdQVSBtZW1vcnkgb24gQTEwMDogN0IgZnAxNiBmdWxsID0gODRHQiAobmVlZHMgMsOXIEExMDAgODBHQiksIDdCIExvUkEgPSAxOEdCLCA3QiBRTG9SQSA9IDlHQi4gRm9yIDcwQjogZnAxNiBmdWxsID0gODQwR0IgKDExw5cgQTEwMCA4MEdCKSwgTG9SQSA9IDE1NEdCLCBRTG9SQSA9IDgwR0IgKGZpdHMgb24gYSBzaW5nbGUgQTEwMCA4MEdCIHdpdGggc29tZSByb29tIGZvciBhY3RpdmF0aW9ucykuIFFMb1JBIHRocm91Z2hwdXQgaXMgYXBwcm94aW1hdGVseSA3MC03NSUgb2YgTG9SQSBkdWUgdG8gdGhlIG92ZXJoZWFkIG9mIG9uLXRoZS1mbHkgZGVxdWFudGl6YXRpb24gZHVyaW5nIHRoZSBmb3J3YXJkIHBhc3MuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlF1YW50aXphdGlvbiIsIkJpdHMvUGFyYW0iLCJNZW1vcnkgKDdCKSIsIlF1YWxpdHkgdnMgZnAxNiIsIlNwZWVkIHZzIGZwMTYiLCJNYXggTW9kZWwgb24gODBHQiBBMTAwIl0sInJvd3MiOltbImZwMTYgRnVsbCBGVCIsIjE2Iiwifjg0IEdCIiwiQmFzZWxpbmUiLCIxLjAww5ciLCJ+NUIiXSxbIkxvUkEgZnAxNiIsIjE2ICsgYWRhcHRlciIsIn4xOCBHQiIsIuKJiDk5JSIsIjAuOTXDlyIsIn4zMEIiXSxbIjgtYml0IElOVDgiLCI4IiwifjE0IEdCIiwifjk4LTk5JSIsIjAuODXDlyIsIn40NUIiXSxbIjQtYml0IElOVDQiLCI0IiwifjcgR0IiLCJ+OTQtOTYlIiwiMC44MMOXIiwifjEzMEIiXSxbIjQtYml0IE5GNCAoUUxvUkEpIiwifjQuNSIsIn45IEdCIiwifjk4LTk5JSIsIjAuNzXDlyIsIn43MEIiXSxbIk5GNCArIERvdWJsZSBRdWFudCIsIn40LjEzIiwifjguNSBHQiIsIn45OC05OSUiLCIwLjc1w5ciLCJ+NzVCIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYWdlZCBPcHRpbWl6ZXIgYW5kIFRyYWluaW5nIFRpcHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBwYWdlZCBvcHRpbWl6ZXIgaXMgYSBRTG9SQS1zcGVjaWZpYyB0ZWNobmlxdWUgdXNpbmcgTlZJRElBIHVuaWZpZWQgbWVtb3J5IHRvIGF1dG9tYXRpY2FsbHkgcGFnZSBBZGFtIG9wdGltaXplciBzdGF0ZXMgKG1vbWVudHVtIGFuZCB2YXJpYW5jZSB0ZW5zb3JzKSBmcm9tIEdQVSBWUkFNIHRvIENQVSBSQU0gd2hlbiB0aGUgR1BVIHJ1bnMgb3V0IG9mIG1lbW9yeSwgYW5kIHBhZ2UgdGhlbSBiYWNrIHdoZW4gbmVlZGVkIGZvciBncmFkaWVudCB1cGRhdGVzLiBUaGlzIHByZXZlbnRzIE9PTSBjcmFzaGVzIGR1cmluZyBsb25nIHRyYWluaW5nIHJ1bnMgd2l0aG91dCByZXF1aXJpbmcgbWFudWFsIG1lbW9yeSBtYW5hZ2VtZW50LiBVc2UgcGFnZWRfYWRhbXdfOGJpdCBmcm9tIGJpdHNhbmRieXRlcyBmb3IgbWF4aW11bSBzYXZpbmdzOyBwYWdlZF9hZGFtd18zMmJpdCBmb3IgdHJhaW5pbmcgc3RhYmlsaXR5IG9uIHNlbnNpdGl2ZSB0YXNrcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVzZSBwYWdlZF9hZGFtd184Yml0IGZvciBtYXhpbXVtIEdQVSBtZW1vcnkgc2F2aW5nczsgcGFnZWRfYWRhbXdfMzJiaXQgZm9yIG51bWVyaWNhbCBzdGFiaWxpdHkiLCJTZXQgYm5iXzRiaXRfY29tcHV0ZV9kdHlwZT10b3JjaC5iZmxvYXQxNiAobm90IGZsb2F0MTYpIOKAlCBiZjE2IGhhcyBiZXR0ZXIgZHluYW1pYyByYW5nZSBhbmQgYXZvaWRzIE5hTiBpbnN0YWJpbGl0eSIsIkVuYWJsZSBncmFkaWVudCBjaGVja3BvaW50aW5nIHZpYSBwcmVwYXJlX21vZGVsX2Zvcl9rYml0X3RyYWluaW5nKCkg4oCUIHRyYWRlcyAzMCUgdGhyb3VnaHB1dCBmb3IgbGFyZ2UgYWN0aXZhdGlvbiBtZW1vcnkgc2F2aW5ncyIsIlNldCBtYXhfZ3JhZF9ub3JtPTAuMyBhbmQgd2FybXVwX3JhdGlvPTAuMDMgZm9yIHN0YWJsZSBRTG9SQSB0cmFpbmluZyBydW5zIiwiVXNlIHBlcl9kZXZpY2VfdHJhaW5fYmF0Y2hfc2l6ZT0xIG9yIDIgd2l0aCBncmFkaWVudF9hY2N1bXVsYXRpb25fc3RlcHM9MTYgdG8gbWFpbnRhaW4gZWZmZWN0aXZlIGJhdGNoIG9mIDE2LTMyIiwiTG9SQSBhZGFwdGVycyByZW1haW4gaW4gYmYxNi9mcDMyIHRocm91Z2hvdXQgdHJhaW5pbmcg4oCUIG9ubHkgdGhlIGZyb3plbiBiYXNlIG1vZGVsIGlzIGluIDQtYml0IE5GNCJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiTkY0ICsgRG91YmxlIFF1YW50aXphdGlvbiBNZW1vcnkgTWF0aCIsImNvbnRlbnQiOiJRTG9SQSB3aXRoIE5GNCArIGRvdWJsZSBxdWFudGl6YXRpb24gdXNlcyB+MC41IGJpdHMvcGFyYW1ldGVyIGZvciB0aGUgcXVhbnRpemF0aW9uIGNvbnN0YW50cyAodnMgMC4xMjUgYml0cyBmb3IgTkY0IHdlaWdodHMpLCBicmluZ2luZyB0b3RhbCBtZW1vcnkgdG8gfjQuNSBiaXRzL3BhcmFtIOKAlCBhbGxvd2luZyBhIDcwQiBtb2RlbCB0byBmaXQgaW4gYSBzaW5nbGUgNDBHQiBBMTAwIHdpdGggNC1iaXQgcXVhbnRpemF0aW9uLiBTcGVjaWZpY2FsbHk6IDcwQiDDlyA0LjUgYml0cyAvIDggYml0c19wZXJfYnl0ZSA9IDM5LjRHQiBmb3Igd2VpZ2h0cywgbGVhdmluZyByb29tIGZvciBhY3RpdmF0aW9ucyBhbmQgTG9SQSBhZGFwdGVyIHN0YXRlcyB3aXRoaW4gNDBHQiBWUkFNLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUUxvUkEgZGVtb2NyYXRpemVkIExMTSBmaW5lLXR1bmluZyBieSBtYWtpbmcgaXQgZmVhc2libGUgb24gY29uc3VtZXIgaGFyZHdhcmUuIEEgN0IgbW9kZWwgY2FuIGJlIGZpbmUtdHVuZWQgb24gYW4gUlRYIDMwOTAgMjRHQiDigJQgYSB0YXNrIHRoYXQgcHJldmlvdXNseSByZXF1aXJlZCBtdWx0aXBsZSBlbnRlcnByaXNlIEExMDAgR1BVcy4gQ29tYmluZWQgd2l0aCBvcGVuIGRhdGFzZXRzIChBbHBhY2EsIEZMQU4sIE9wZW5Bc3Npc3RhbnQpIGFuZCB0aGUgR3VhbmFjbyB0cmFpbmluZyByZWNpcGUgZnJvbSB0aGUgUUxvUkEgcGFwZXIsIHRoaXMgZW5hYmxlZCBhIGdlbmVyYXRpb24gb2YgY29tcGV0aXRpdmUgb3Blbi1zb3VyY2UgZmluZS10dW5lZCBtb2RlbHMgdHJhaW5lZCBieSBpbmRpdmlkdWFscyBhbmQgc21hbGwgdGVhbXMgd2l0aCBtb2Rlc3QgR1BVIGJ1ZGdldHMuIn1d"
---
# QLoRA — 4-bit NF4 Quantization with LoRA for Memory-Efficient Fine-Tuning

QLoRA (Dettmers et al., 2023) combines 4-bit NF4 (NormalFloat4) quantization of the frozen base model with full-precision LoRA adapters to achieve unprecedented memory efficiency for LLM fine-tuning. A 65B LLaMA model requires ~130GB in fp16 — requiring multiple A100 80GB GPUs. QLoRA reduces this to ~35GB by quantizing frozen base weights to 4-bit NF4, enabling single-GPU fine-tuning of 65B models on an A100 80GB and 7B fine-tuning on a consumer RTX 3090 24GB.

## The Memory Wall in LLM Fine-Tuning

LLM fine-tuning memory consumption comes from four sources: model weights, gradient tensors (same size as weights), Adam optimizer states (momentum + variance, each fp32 = 2× weight size), and activation memory for backpropagation. For a 7B model in fp16: weights = 14GB, gradients = 14GB, Adam states = 56GB (fp32) — totaling ~84GB before activations. QLoRA's insight: the base weights only need high precision during the LoRA adapter computation, not for storage. Store in 4-bit, dequantize on-the-fly only for the forward and backward pass.

- fp32 full fine-tune: ~24 bytes/param — 168GB for 7B, 1.7TB for 70B
- fp16/bf16 full fine-tune: ~16 bytes/param — 112GB for 7B, 1.1TB for 70B
- LoRA (fp16 base): ~14GB weights + ~2GB adapter + ~4GB optimizer = ~20GB for 7B
- QLoRA (NF4 4-bit base): ~3.5GB weights + ~2GB adapter + ~4GB optimizer = ~9.5GB for 7B
- QLoRA with double quantization: ~3.25GB weights + adapters + optimizer ≈ 9GB for 7B

## NF4 — Information-Theoretically Optimal 4-bit Quantization

Standard INT4 quantization places 16 quantization levels at equal intervals in [min, max], assuming weights are uniformly distributed. LLM weights are near-Gaussian N(0, σ²). NF4 (NormalFloat4) exploits this: quantization levels are placed at the quantiles of N(0,1), spacing them closer together where the density is highest (near zero) and further apart in the tails. This is information-theoretically optimal — each 4-bit codeword carries equal information under the Gaussian prior. The result is lower reconstruction error than INT4 at the same bit width.

$$q_i = Q_{N(0,1)}\!\left(\frac{i + 0.5}{2^k}\right),\quad i = 0, 1, \ldots, 2^k - 1,\quad k = 4$$

## QLoRA Setup — 4-bit NF4 Model with LoRA Adapters

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, TaskType, prepare_model_for_kbit_training

# Step 1: Configure 4-bit NF4 quantization with double quantization
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",           # NF4 optimal for Gaussian weights
    bnb_4bit_compute_dtype=torch.bfloat16,  # Dequantize to bf16 for matmul
    bnb_4bit_use_double_quant=True,      # Quantize the scaling constants too
)

# Step 2: Load model quantized to 4-bit NF4
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    quantization_config=bnb_config,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer.pad_token = tokenizer.eos_token

# Step 3: Prepare for k-bit training — enables gradient checkpointing
model = prepare_model_for_kbit_training(model)

# Step 4: Add LoRA adapters in bf16 on top of frozen 4-bit base
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16, lora_alpha=32,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05, bias="none",
)
peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()
```

During the forward pass, each 4-bit NF4 weight block is dequantized to bf16 on-the-fly, the matrix multiplication runs in bf16, and the dequantized values are immediately discarded. Only the 4-bit integers and their scaling constants remain in GPU memory for the base model. LoRA adapter weights stay in bf16/fp32 throughout training. Gradients flow only through the adapter parameters — the quantized base weights have no gradients.

## NF4 Quantization Mechanics

```python
import torch
import numpy as np
from scipy.stats import norm

def compute_nf4_levels(num_bits: int = 4) -> torch.Tensor:
    """Compute NF4 quantization levels: midpoints of equal-prob intervals of N(0,1)."""
    num_levels = 2 ** num_bits  # 16 levels for 4-bit
    quantile_pos = np.linspace(0, 1, num_levels + 1)
    midpoints = (quantile_pos[:-1] + quantile_pos[1:]) / 2
    levels = torch.tensor(norm.ppf(midpoints), dtype=torch.float32)
    return levels / levels.abs().max()  # normalize to [-1, 1]

def nf4_quantize(weight: torch.Tensor, block_size: int = 64) -> tuple:
    """Quantize weight tensor to NF4 with per-block absmax scaling."""
    nf4_lvls = compute_nf4_levels(4).to(weight.device)
    blocks = weight.reshape(-1, block_size)
    scales = blocks.abs().max(dim=1, keepdim=True).values.clamp(min=1e-8)
    normalized = blocks / scales
    diffs = (normalized.unsqueeze(-1) - nf4_lvls).abs()
    indices = diffs.argmin(dim=-1).to(torch.uint8)  # 4-bit indices (0-15)
    return indices, scales

def nf4_dequantize(indices: torch.Tensor,
                   scales: torch.Tensor, block_size: int = 64) -> torch.Tensor:
    """Reconstruct fp32 weights from NF4 indices and per-block scales."""
    nf4_lvls = compute_nf4_levels(4).to(scales.device)
    reconstructed = nf4_lvls[indices.long()]
    return (reconstructed * scales).reshape(-1)
w = torch.randn(256, 256)
nf4_lvls = compute_nf4_levels()
print(f"NF4 levels (central 8): {nf4_lvls[4:12].tolist()}")
idx, sc = nf4_quantize(w)
w_recon = nf4_dequantize(idx, sc).reshape(256, 256)
rmse = (w - w_recon).pow(2).mean().sqrt().item()
print(f"NF4 RMSE: {rmse:.5f}  |  Compression: {w.numel()*32/(idx.numel()*4+sc.numel()*32):.1f}x")
```

NF4 allocates 8 of its 16 levels to the central region where most LLM weight mass resides, vs INT4 which allocates 4. For a weight distribution with σ=0.02, approximately 68% of values fall within ±σ of zero — NF4 covers this dense region with double the resolution of INT4. This density matching reduces reconstruction MSE by 25–30% compared to INT4 at the same bit width, which translates to measurable quality improvements for downstream task performance.

## Double Quantization — Quantizing the Quantization Constants

```python
import torch

def double_quantize(weight: torch.Tensor,
                    inner_block: int = 64,
                    outer_block: int = 256) -> dict:
    """
    Two-level quantization: NF4 for weights (4 bits), INT8 for scales (8 bits).
    Reduces per-weight scale overhead from 0.5 to 0.125 bits.
    """
    # Level 1: per-inner-block fp32 scales for NF4 quantization
    blocks = weight.reshape(-1, inner_block)
    scales_fp32 = blocks.abs().max(dim=1).values       # [N] fp32, 32 bits each

    # Level 2: quantize fp32 scales to INT8 per outer_block
    n_groups = (scales_fp32.numel() + outer_block // inner_block - 1) // (outer_block // inner_block)
    group_size = outer_block // inner_block
    padded = torch.cat([scales_fp32, scales_fp32.new_zeros(n_groups * group_size - scales_fp32.numel())])
    groups = padded.reshape(n_groups, group_size)
    super_scales = groups.abs().max(dim=1, keepdim=True).values.clamp(1e-8)
    scales_int8 = (groups / super_scales * 127).round().clamp(-127, 127).to(torch.int8)

    # Bit-cost analysis
    bits_fp32 = 32 / inner_block           # 0.500 bits/weight for fp32 scales
    bits_int8 = 8 / inner_block            # 0.125 bits/weight for int8 scales
    bits_super = 32 / outer_block          # 0.125 bits/weight for super-scales
    print(f"Scale overhead: fp32={bits_fp32:.3f} -> int8={bits_int8:.3f} bits/weight")
    print(f"Total NF4 + double quant: {4 + bits_int8 + bits_super:.3f} bits/weight")
    return {"scales_int8": scales_int8, "super_scales": super_scales}

result = double_quantize(torch.randn(4096, 4096))
```

Double quantization reduces the storage overhead of quantization constants from 0.5 bits/weight (fp32 scale per 64 weights) to approximately 0.127 bits/weight (int8 scale per 64 + fp32 super-scale per 256). Combined with NF4's 4 bits per weight, the total is ~4.127 bits/weight. For a 70B model, double quantization saves approximately 3.5GB of GPU memory — enough to fit on a 40GB A100 that would otherwise require a 80GB variant.

## Memory Profiling — fp16 vs LoRA vs QLoRA

```python
import torch

def estimate_training_memory_gb(n_params: float, mode: str,
                                adapter_frac: float = 0.01) -> float:
    """Estimate peak GPU training memory (GB) for a model by size and mode."""
    n = n_params * 1e9
    if mode == "fp16_full":
        # Weights fp16 + grads fp16 + Adam fp32 momentum + Adam fp32 variance
        return n * (2 + 2 + 4 + 4) / 1e9
    elif mode == "lora_fp16":
        # Frozen fp16 base weights + adapter fp16 + Adam fp32 on adapter only
        adapter_n = n * adapter_frac
        return (n * 2 + adapter_n * 2 + adapter_n * (4 + 4)) / 1e9
    elif mode == "qlora_nf4":
        # NF4 base (0.5 bytes/param) + adapter bf16 + Adam fp32 on adapter only
        adapter_n = n * adapter_frac
        return (n * 0.5 + adapter_n * 2 + adapter_n * (4 + 4)) / 1e9
    return 0.0

print(f"{'Size':<6} {'Mode':<14} {'Peak GPU (GB)':>14}")
print("-" * 36)
for n_b, label in [(7, "7B"), (13, "13B"), (70, "70B")]:
    for mode in ["fp16_full", "lora_fp16", "qlora_nf4"]:
        gb = estimate_training_memory_gb(n_b, mode)
        print(f"{label:<6} {mode:<14} {gb:>14.1f}")
```

Estimated peak GPU memory on A100: 7B fp16 full = 84GB (needs 2× A100 80GB), 7B LoRA = 18GB, 7B QLoRA = 9GB. For 70B: fp16 full = 840GB (11× A100 80GB), LoRA = 154GB, QLoRA = 80GB (fits on a single A100 80GB with some room for activations). QLoRA throughput is approximately 70-75% of LoRA due to the overhead of on-the-fly dequantization during the forward pass.

| Quantization | Bits/Param | Memory (7B) | Quality vs fp16 | Speed vs fp16 | Max Model on 80GB A100 |
| --- | --- | --- | --- | --- | --- |
| fp16 Full FT | 16 | ~84 GB | Baseline | 1.00× | ~5B |
| LoRA fp16 | 16 + adapter | ~18 GB | ≈99% | 0.95× | ~30B |
| 8-bit INT8 | 8 | ~14 GB | ~98-99% | 0.85× | ~45B |
| 4-bit INT4 | 4 | ~7 GB | ~94-96% | 0.80× | ~130B |
| 4-bit NF4 (QLoRA) | ~4.5 | ~9 GB | ~98-99% | 0.75× | ~70B |
| NF4 + Double Quant | ~4.13 | ~8.5 GB | ~98-99% | 0.75× | ~75B |

## Paged Optimizer and Training Tips

The paged optimizer is a QLoRA-specific technique using NVIDIA unified memory to automatically page Adam optimizer states (momentum and variance tensors) from GPU VRAM to CPU RAM when the GPU runs out of memory, and page them back when needed for gradient updates. This prevents OOM crashes during long training runs without requiring manual memory management. Use paged_adamw_8bit from bitsandbytes for maximum savings; paged_adamw_32bit for training stability on sensitive tasks.

- Use paged_adamw_8bit for maximum GPU memory savings; paged_adamw_32bit for numerical stability
- Set bnb_4bit_compute_dtype=torch.bfloat16 (not float16) — bf16 has better dynamic range and avoids NaN instability
- Enable gradient checkpointing via prepare_model_for_kbit_training() — trades 30% throughput for large activation memory savings
- Set max_grad_norm=0.3 and warmup_ratio=0.03 for stable QLoRA training runs
- Use per_device_train_batch_size=1 or 2 with gradient_accumulation_steps=16 to maintain effective batch of 16-32
- LoRA adapters remain in bf16/fp32 throughout training — only the frozen base model is in 4-bit NF4

> **NF4 + Double Quantization Memory Math**: QLoRA with NF4 + double quantization uses ~0.5 bits/parameter for the quantization constants (vs 0.125 bits for NF4 weights), bringing total memory to ~4.5 bits/param — allowing a 70B model to fit in a single 40GB A100 with 4-bit quantization. Specifically: 70B × 4.5 bits / 8 bits_per_byte = 39.4GB for weights, leaving room for activations and LoRA adapter states within 40GB VRAM.

QLoRA democratized LLM fine-tuning by making it feasible on consumer hardware. A 7B model can be fine-tuned on an RTX 3090 24GB — a task that previously required multiple enterprise A100 GPUs. Combined with open datasets (Alpaca, FLAN, OpenAssistant) and the Guanaco training recipe from the QLoRA paper, this enabled a generation of competitive open-source fine-tuned models trained by individuals and small teams with modest GPU budgets.

