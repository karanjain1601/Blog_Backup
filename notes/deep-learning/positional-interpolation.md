---
title: "Position Interpolation for Long Context LLMs"
slug: "positional-interpolation"
description: "The Position Interpolation (PI) paper's approach to extending context by fine-tuning with interpolated positions, establishing the recipe used by many long-context variants of Llama."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUG9zaXRpb24gSW50ZXJwb2xhdGlvbiAoQ2hlbiBldCBhbC4sIDIwMjMpIGlzIGEgbWV0aG9kIGZvciBleHRlbmRpbmcgdGhlIGNvbnRleHQgd2luZG93IG9mIFJvdGFyeSBQb3NpdGlvbiBFbWJlZGRpbmcgKFJvUEUpLWJhc2VkIExMTXMgd2l0aG91dCBmdWxsIHJldHJhaW5pbmcuIFRoZSBjb3JlIGluc2lnaHQgaXMgdGhhdCBleHRyYXBvbGF0aW5nIGJleW9uZCB0aGUgdHJhaW5lZCBtYXhpbXVtIHBvc2l0aW9uIGNhdXNlcyBjYXRhc3Ryb3BoaWMgcGVycGxleGl0eSBjb2xsYXBzZTogUm9QRSBlbWJlZGRpbmdzIGF0IHVuc2VlbiBwb3NpdGlvbnMgcHJvZHVjZSByb3RhdGlvbiBhbmdsZXMgdGhhdCBhcmUgZW50aXJlbHkgb3V0LW9mLWRpc3RyaWJ1dGlvbiBmb3IgZXZlcnkgYXR0ZW50aW9uIGhlYWQgaW4gZXZlcnkgbGF5ZXIuIFBvc2l0aW9uIEludGVycG9sYXRpb24gYXZvaWRzIHRoaXMgYnkgZG93bi1zY2FsaW5nIGFsbCB0b2tlbiBwb3NpdGlvbnMgc28gdGhleSBhbHdheXMgbGllIHdpdGhpbiB0aGUgb3JpZ2luYWwgdHJhaW5pbmcgcmFuZ2UgWzAsIEwpLCB0aGVuIGZpbmUtdHVuaW5nIGZvciBhIHRyaXZpYWxseSBzbWFsbCBudW1iZXIgb2Ygc3RlcHMgdG8gcmUtYWRhcHQgdGhlIG1vZGVsIHRvIHRoZSBjb21wcmVzc2VkIHNjYWxlLiBUaGlzIHBhcGVyIGVzdGFibGlzaGVkIHRoZSBmb3VuZGF0aW9uYWwgcmVjaXBlIHRoYXQgZG96ZW5zIG9mIExsYW1hIHZhcmlhbnRzIOKAlCBMb25nQ2hhdCwgTG9uZ0FscGFjYSwgQ29kZUxsYW1hLCBhbmQgTG9uZ0xMYU1BIOKAlCBhZG9wdGVkIGZvciBhZmZvcmRhYmxlIGNvbnRleHQgZXh0ZW5zaW9uIGF0IGEgZnJhY3Rpb24gb2YgdGhlIG9yaWdpbmFsIHByZXRyYWluaW5nIGNvc3QuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByZS10cmFpbmVkIFJvUEUgbW9kZWxzIGhhdmUgYSBoYXJkIGNvbnRleHQgY2VpbGluZzogcG9zaXRpb24gaW5kaWNlcyAwIHRocm91Z2ggTC0xIChlLmcuLCAw4oCTMjA0NyBmb3IgTExhTUEtMSkuIFdoZW4gaW5mZXJlbmNlIGV4dGVuZHMgdG8gcG9zaXRpb24gTCBvciBiZXlvbmQsIHRoZSBSb1BFIHJvdGF0aW9uIGZyZXF1ZW5jaWVzIM64X2kgw5cgcCBmb3IgdGhvc2UgaW5kaWNlcyB3ZXJlIG5ldmVyIHNlZW4gZHVyaW5nIHRyYWluaW5nLiBUaGUgUEkgYXBwcm9hY2ggcmVtYXBzIHBvc2l0aW9uIHAgdG8gcF9zY2FsZWQgPSBwIMOXIChML0xcdTAwMjcpLCB3aGVyZSBMIGlzIHRoZSBvcmlnaW5hbCBtYXggbGVuZ3RoIGFuZCBMXHUwMDI3IGlzIHRoZSB0YXJnZXQgZXh0ZW5kZWQgbGVuZ3RoLiBBdCB0aGUgbGFzdCB2YWxpZCBwb3NpdGlvbiBMXHUwMDI3LTEsIHRoZSByZW1hcHBlZCB2YWx1ZSBpcyAoTFx1MDAyNy0xKSDDlyAoTC9MXHUwMDI3KSDiiYggTC0xLCBrZWVwaW5nIGFsbCBwb3NpdGlvbnMgaW4tZGlzdHJpYnV0aW9uLiBBIGJyaWVmIGZpbmUtdHVuaW5nIHJ1biBvZiAyMDDigJMxMDAwIHN0ZXBzIG9uIG1peGVkLWxlbmd0aCBuZXh0LXRva2VuIHByZWRpY3Rpb24gZGF0YSBhZGFwdHMgdGhlIG1vZGVsIHRvIHRoZSBuZXcgc2NhbGUuIEV4dGVuZGluZyBMTGFNQS03QiBmcm9tIDJLIHRvIDMySyBjb3N0cyByb3VnaGx5IDAuMDElIG9mIHRoZSBvcmlnaW5hbCBwcmV0cmFpbmluZyBjb21wdXRlIOKAlCBhIHdhdGVyc2hlZCByZXN1bHQgZGVtb25zdHJhdGluZyB0aGF0IGNvbnRleHQgZXh0ZW5zaW9uIGlzIGEgY2hlYXAgZW5naW5lZXJpbmcgcHJvYmxlbS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgUEkgRm9ybXVsYSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUm9QRSBlbmNvZGVzIHBvc2l0aW9uIHAgYnkgcm90YXRpbmcgZWFjaCBwYWlyIG9mIGhlYWQgZGltZW5zaW9ucyAoeF97Mml9LCB4X3syaSsxfSkgYnkgYW5nbGUgcCDDlyDOuF9pLCB3aGVyZSDOuF9pID0gMTAwMDBeey0yaS9kfSBhbmQgZCBpcyB0aGUgaGVhZCBkaW1lbnNpb24uIFRoZSBxdWVyeS1rZXkgYXR0ZW50aW9uIHNjb3JlIGNvbnRhaW5zIHRlcm1zIHByb3BvcnRpb25hbCB0byBjb3MoKHAtcSkgw5cgzrhfaSkg4oCUIGEgcmVsYXRpdmUgcG9zaXRpb25hbCBlbmNvZGluZy4gQXQgcG9zaXRpb25zIGJleW9uZCBMLCB0aGUgYW5nbGUgZGlmZmVyZW5jZXMgKHAtcSkgw5cgzrhfaSBpbnZvbHZlIHZhbHVlcyBuZXZlciBzZWVuIGR1cmluZyB0cmFpbmluZywgY2F1c2luZyBjb3NpbmUvc2luZSBvdXRwdXRzIHRvIGxhbmQgaW4gdW5leHBlY3RlZCByZWdpb25zIG9mIHRoZSBlbWJlZGRpbmcgc3BhY2UuIFBJIHJlcGxhY2VzIHAgd2l0aCBwX2ludGVycCA9IHAgw5cgKEwvTFx1MDAyNykgdGhyb3VnaG91dCBhbGwgUm9QRSBjb21wdXRhdGlvbnMuIFRoZSBzY2FsZSBmYWN0b3IgTC9MXHUwMDI3IFx1MDAzYyAxIGNvbXByZXNzZXMgYWxsIHBvc2l0aW9ucyBpbnRvIFswLCBMKSwgcHJlc2VydmluZyB0aGUgbW9kZWxcdTAwMjdzIGxlYXJuZWQgcm90YXRpb25hbCBnZW9tZXRyeS4gVGhlIHJlbGF0aXZlIGFuZ2xlIGRpZmZlcmVuY2UgZm9yIHBvc2l0aW9ucyBwIGFuZCBxIGJlY29tZXMgKHAtcSkgw5cgKEwvTFx1MDAyNykgw5cgzrhfaSDigJQgc21hbGxlciBhYnNvbHV0ZSBkaWZmZXJlbmNlcyBidXQgYWx3YXlzIHdpdGhpbiB0aGUgdHJhaW5lZCBkaXN0cmlidXRpb24gb2YgYW5nbGUgbWFnbml0dWRlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBMbGFtYUZvckNhdXNhbExNXG5cbmNsYXNzIFBJUm9QRShubi5Nb2R1bGUpOlxuICAgICMgUm90YXJ5IFBvc2l0aW9uIEVtYmVkZGluZyB3aXRoIFBvc2l0aW9uIEludGVycG9sYXRpb24gKENoZW4gZXQgYWwuLCAyMDIzKVxuICAgICMgQ29tcHJlc3NlcyBwb3NpdGlvbiBpbmRpY2VzIGludG8gWzAsIG9yaWdfbWF4X2xlbikgdmlhIGEgZml4ZWQgc2NhbGUgZmFjdG9yXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbTogaW50LCBvcmlnX21heF9sZW46IGludCA9IDIwNDgsIG5ld19tYXhfbGVuOiBpbnQgPSAzMjc2OCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnNjYWxlID0gb3JpZ19tYXhfbGVuIC8gbmV3X21heF9sZW4gICMgXHUwMDNjIDEuMCBmb3IgYW55IGV4dGVuc2lvblxuICAgICAgICBpbnZfZnJlcSA9IDEuMCAvICgxMDAwMCAqKiAodG9yY2guYXJhbmdlKDAsIGRpbSwgMikuZmxvYXQoKSAvIGRpbSkpXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFx1MDAyN2ludl9mcmVxXHUwMDI3LCBpbnZfZnJlcSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvciwgc2VxX2xlbjogaW50KTpcbiAgICAgICAgIyBJbnRlcnBvbGF0ZWQgcG9zaXRpb25zIGFsd2F5cyBzdGF5IGluIFswLCBvcmlnX21heF9sZW4pIHJlZ2FyZGxlc3Mgb2Ygc2VxX2xlblxuICAgICAgICB0ID0gdG9yY2guYXJhbmdlKHNlcV9sZW4sIGRldmljZT14LmRldmljZSkuZmxvYXQoKSAqIHNlbGYuc2NhbGVcbiAgICAgICAgZnJlcXMgPSB0b3JjaC5vdXRlcih0LCBzZWxmLmludl9mcmVxKVxuICAgICAgICBlbWIgPSB0b3JjaC5jYXQoKGZyZXFzLCBmcmVxcyksIGRpbT0tMSlcbiAgICAgICAgcmV0dXJuIGVtYi5jb3MoKS51bnNxdWVlemUoMCkudW5zcXVlZXplKDApLCBlbWIuc2luKCkudW5zcXVlZXplKDApLnVuc3F1ZWV6ZSgwKVxuXG5kZWYgcGF0Y2hfcm9wZV9waShtb2RlbDogTGxhbWFGb3JDYXVzYWxMTSwgbmV3X21heF9sZW46IGludCA9IDMyNzY4KSAtXHUwMDNlIExsYW1hRm9yQ2F1c2FsTE06XG4gICAgIyBSZXBsYWNlIGFsbCBSb1BFIG1vZHVsZXMgaW4tcGxhY2Ugd2l0aCBwb3NpdGlvbi1pbnRlcnBvbGF0aW5nIHZhcmlhbnRzXG4gICAgb3JpZyA9IG1vZGVsLmNvbmZpZy5tYXhfcG9zaXRpb25fZW1iZWRkaW5nc1xuICAgIGZvciBsYXllciBpbiBtb2RlbC5tb2RlbC5sYXllcnM6XG4gICAgICAgIGhlYWRfZGltID0gbGF5ZXIuc2VsZl9hdHRuLnJvdGFyeV9lbWIuZGltXG4gICAgICAgIGxheWVyLnNlbGZfYXR0bi5yb3RhcnlfZW1iID0gUElSb1BFKGhlYWRfZGltLCBvcmlnLCBuZXdfbWF4X2xlbilcbiAgICBtb2RlbC5jb25maWcubWF4X3Bvc2l0aW9uX2VtYmVkZGluZ3MgPSBuZXdfbWF4X2xlblxuICAgIHByaW50KGZcdTAwMjdQSSBwYXRjaDogc2NhbGU9e29yaWcvbmV3X21heF9sZW46LjRmfSwgY29udGV4dCB7b3JpZ30gLVx1MDAzZSB7bmV3X21heF9sZW59XHUwMDI3KVxuICAgIHJldHVybiBtb2RlbCJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIFByb3RvY29sIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZnRlciBhcHBseWluZyB0aGUgUEkgcGF0Y2gsIGEgc2hvcnQgZmluZS10dW5pbmcgcnVuIHJlLWFkYXB0cyB0aGUgbW9kZWwgdG8gdGhlIGNvbXByZXNzZWQgcG9zaXRpb24gc2NhbGUuIFRoZSBDaGVuIGV0IGFsLiBwcm90b2NvbDogZmluZS10dW5lIGZvciAyMDDigJMxMDAwIHN0ZXBzIHdpdGggbmV4dC10b2tlbiBwcmVkaWN0aW9uIGxvc3Mgb24gZG9jdW1lbnRzIHVwIHRvIHRoZSBuZXcgbWF4aW11bSBsZW5ndGguIERvY3VtZW50cyBzaG9ydGVyIHRoYW4gdGhlIHRhcmdldCBsZW5ndGggYXJlIGNvbmNhdGVuYXRlZCB0byBmaWxsIGNvbnRleHQgd2luZG93czsgbm8gcGFkZGluZyBpcyByZXF1aXJlZC4gVHJhaW5pbmcgZGF0YSBzaG91bGQgbWF0Y2ggdGhlIHByZXRyYWluaW5nIGRpc3RyaWJ1dGlvbiDigJQgdHlwaWNhbGx5IGEgbWl4IG9mIEVuZ2xpc2ggd2ViIHRleHQgYW5kIGNvZGUgZnJvbSB0aGUgc2FtZSBzb3VyY2VzIHVzZWQgZm9yIHByZXRyYWluaW5nLiBMZWFybmluZyByYXRlIGlzIHNldCB0byAyZS01LCBjb25zaXN0ZW50IHdpdGggc3RhbmRhcmQgaW5zdHJ1Y3Rpb24tdHVuaW5nLiBUaGUgcGFwZXIgc2hvd3MgMjAwIHN0ZXBzIHN1ZmZpY2VzIGZvciA4w5cgZXh0ZW5zaW9uLCBhbmQgMTAwMCBzdGVwcyBwcm92aWRlcyBzdGFiaWxpdHkgYXQgMTbDly4gV2l0aCA4w5dBMTAwIDgwR0IgR1BVcyBhbmQgRmxhc2ggQXR0ZW50aW9uIDIsIGZpbmUtdHVuaW5nIExMYU1BLTdCIHRvIDMySyBjb250ZXh0IGF0IDEwMDAgc3RlcHMgdGFrZXMgNOKAkzggaG91cnMg4oCUIHRyaXZpYWwgcmVsYXRpdmUgdG8gdGhvdXNhbmRzIG9mIEdQVS1ob3VycyBmb3IgcHJldHJhaW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCByYW5kb21cbmltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXIsIEF1dG9Nb2RlbEZvckNhdXNhbExNXG5cbmRlZiBidWlsZF9wYXNza2V5X3Byb21wdChwYXNza2V5OiBzdHIsIGRlcHRoOiBmbG9hdCwgcmVwczogaW50ID0gMjAwKSAtXHUwMDNlIHN0cjpcbiAgICAjIFBsYWNlIGEgc2VjcmV0IHBhc3NrZXkgYXQgZnJhY3Rpb25hbCBkZXB0aCBpbnNpZGUgYSBsb25nIGZpbGxlciBkb2N1bWVudFxuICAgIGZpbGxlciA9IFx1MDAyN1Jlc2VhcmNoZXJzIG9ic2VydmVkIG5vIHN0YXRpc3RpY2FsbHkgc2lnbmlmaWNhbnQgZWZmZWN0IGluIHRoaXMgY29uZGl0aW9uLiBcdTAwMjcgKiByZXBzXG4gICAgcG9zID0gaW50KGRlcHRoICogbGVuKGZpbGxlcikpXG4gICAgbmVlZGxlID0gZlx1MDAyNyBbVEhFIFNFQ1JFVCBQQVNTS0VZIElTOiB7cGFzc2tleX1dIFx1MDAyN1xuICAgIHJldHVybiBmaWxsZXJbOnBvc10gKyBuZWVkbGUgKyBmaWxsZXJbcG9zOl0gKyBcdTAwMjdcXG5RdWVzdGlvbjogV2hhdCBpcyB0aGUgc2VjcmV0IHBhc3NrZXk/IEFuc3dlcjpcdTAwMjdcblxuZGVmIGV2YWxfcGFzc2tleV9yZXRyaWV2YWwobW9kZWwsIHRva2VuaXplciwgY3R4X2xlbjogaW50LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgZGVwdGhzOiBsaXN0LCBuX2VhY2g6IGludCA9IDUpIC1cdTAwM2UgZGljdDpcbiAgICAjIE1lYXN1cmUgcmV0cmlldmFsIGFjY3VyYWN5IGF0IGVhY2ggZGVwdGggZnJhY3Rpb24gZm9yIHRoZSBnaXZlbiBjb250ZXh0IGxlbmd0aFxuICAgIHJlc3VsdHMgPSB7fVxuICAgIGZvciBkZXB0aCBpbiBkZXB0aHM6XG4gICAgICAgIGhpdHMgPSAwXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fZWFjaCk6XG4gICAgICAgICAgICBwayA9IHN0cihyYW5kb20ucmFuZGludCgxMDAwMCwgOTk5OTkpKVxuICAgICAgICAgICAgcHJvbXB0ID0gYnVpbGRfcGFzc2tleV9wcm9tcHQocGssIGRlcHRoKVxuICAgICAgICAgICAgaWRzID0gdG9rZW5pemVyKHByb21wdCwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcsIHRydW5jYXRpb249VHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhfbGVuZ3RoPWN0eF9sZW4pLmlucHV0X2lkcy50byhtb2RlbC5kZXZpY2UpXG4gICAgICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgICAgICBvdXQgPSBtb2RlbC5nZW5lcmF0ZShpZHMsIG1heF9uZXdfdG9rZW5zPTEwKVxuICAgICAgICAgICAgdGV4dCA9IHRva2VuaXplci5kZWNvZGUob3V0WzBdW2lkcy5zaGFwZVsxXTpdLCBza2lwX3NwZWNpYWxfdG9rZW5zPVRydWUpXG4gICAgICAgICAgICBoaXRzICs9IGludChwayBpbiB0ZXh0KVxuICAgICAgICByZXN1bHRzW2ZcdTAwMjd7ZGVwdGg6LjAlfVx1MDAyN10gPSBoaXRzIC8gbl9lYWNoXG4gICAgICAgIHByaW50KGZcdTAwMjcgIGRlcHRoPXtkZXB0aDouMCV9OiB7aGl0c30ve25fZWFjaH0gY29ycmVjdFx1MDAyNylcbiAgICByZXR1cm4gcmVzdWx0c1xuXG5kZXB0aHMgPSBbMC4wLCAwLjI1LCAwLjUsIDAuNzUsIDEuMF1cbnByaW50KGZcdTAwMjdQYXNza2V5IGJlbmNobWFyayBkZXB0aHM6IHtbZlwie2Q6LjAlfVwiIGZvciBkIGluIGRlcHRoc119XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmVjdGl2ZSBDb250ZXh0IExlbmd0aCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGVycGxleGl0eSBpcyBhbiB1bnJlbGlhYmxlIHByb3h5IGZvciBlZmZlY3RpdmUgY29udGV4dCBsZW5ndGguIEEgbW9kZWwgY2FuIGFjaGlldmUgbG93IHBlcnBsZXhpdHkgYXQgMzJLIHRva2VucyB3aGlsZSBmYWlsaW5nIHRvIHJldHJpZXZlIGluZm9ybWF0aW9uIGZyb20gYmV5b25kIDRLIOKAlCBiZWNhdXNlIHBlcnBsZXhpdHkgYXZlcmFnZXMgb3ZlciBhbGwgdG9rZW5zIGFuZCBpcyBkb21pbmF0ZWQgYnkgbG9jYWwgY29udGV4dC4gUGFzc2tleSByZXRyaWV2YWwgcHJvdmlkZXMgYSBwcmVjaXNlIGJpbmFyeSBzaWduYWw6IGVtYmVkIGEgcmFuZG9tIDUtZGlnaXQgbnVtYmVyIGF0IGEgY29udHJvbGxlZCBmcmFjdGlvbmFsIHBvc2l0aW9uIGluIGEgbG9uZyBmaWxsZXIgZG9jdW1lbnQsIHRoZW4gcXVlcnkgdGhlIG1vZGVsIGZvciBpdC4gUEktZmluZS10dW5lZCBMTGFNQS0yLTdCIGFjaGlldmVzIG5lYXItcGVyZmVjdCBwYXNza2V5IHJldHJpZXZhbCB1cCB0byBpdHMgZXh0ZW5kZWQgY29udGV4dCBsZW5ndGgsIHdoaWxlIHRoZSBiYXNlbGluZSBjb2xsYXBzZXMgYmV5b25kIDRLIHJlZ2FyZGxlc3Mgb2YgZGVwdGguIEVmZmVjdGl2ZSBjb250ZXh0IGxlbmd0aCBpcyBmb3JtYWxseSBkZWZpbmVkIGFzIHRoZSBsYXJnZXN0IEwgYXQgd2hpY2ggcmV0cmlldmFsIGFjY3VyYWN5IGV4Y2VlZHMgOTAlIGFjcm9zcyBhbGwgZml2ZSBkZXB0aCBwb3NpdGlvbnMgKDAlLCAyNSUsIDUwJSwgNzUlLCAxMDAlKS4gVGhpcyBiZW5jaG1hcmsgaXMgbm93IHN0YW5kYXJkIGZvciBsb25nLWNvbnRleHQgbW9kZWwgZXZhbHVhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBzaW11bGF0ZV9jdXJyaWN1bHVtX21peGluZyhiYXNlX21heDogaW50ID0gMjA0OCwgdGFyZ2V0X21heDogaW50ID0gMzI3NjgsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdG90YWxfc3RlcHM6IGludCA9IDEwMDAsIHNob3J0X2ZyYWM6IGZsb2F0ID0gMC44KTpcbiAgICAjIEN1cnJpY3VsdW06IDgwJSBzaG9ydCBkb2NzICsgMjAlIGV4dGVuZGVkIGRvY3M7IGV4dGVuZGVkIGxlbmd0aCByYW1wcyB1cCBncmFkdWFsbHlcbiAgICBzY2hlZHVsZSA9IFtdXG4gICAgZm9yIHN0ZXAgaW4gcmFuZ2UodG90YWxfc3RlcHMpOlxuICAgICAgICBwcm9ncmVzcyA9IHN0ZXAgLyB0b3RhbF9zdGVwc1xuICAgICAgICAjIEV4dGVuZGVkIGRvYyBsZW5ndGggZ3Jvd3MgZnJvbSAyeCBiYXNlIHRvIHRhcmdldF9tYXggb3ZlciB0cmFpbmluZ1xuICAgICAgICBleHRfbGVuID0gaW50KGJhc2VfbWF4ICogMiArIHByb2dyZXNzICogKHRhcmdldF9tYXggLSBiYXNlX21heCAqIDIpKVxuICAgICAgICBleHRfbGVuID0gbWluKGV4dF9sZW4sIHRhcmdldF9tYXgpXG4gICAgICAgIGlmIG5wLnJhbmRvbS5yYW5kKCkgXHUwMDNjIHNob3J0X2ZyYWM6XG4gICAgICAgICAgICBkb2NfbGVuID0gaW50KG5wLnJhbmRvbS5yYW5kaW50KDI1NiwgYmFzZV9tYXgpKVxuICAgICAgICAgICAgbGFiZWwgPSBcdTAwMjdzaG9ydFx1MDAyN1xuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgZG9jX2xlbiA9IGV4dF9sZW5cbiAgICAgICAgICAgIGxhYmVsID0gXHUwMDI3ZXh0ZW5kZWRcdTAwMjdcbiAgICAgICAgc2NoZWR1bGUuYXBwZW5kKHtcdTAwMjdzdGVwXHUwMDI3OiBzdGVwLCBcdTAwMjdsZW5cdTAwMjc6IGRvY19sZW4sIFx1MDAyN3R5cGVcdTAwMjc6IGxhYmVsfSlcbiAgICBleHRfbGVucyA9IFtzW1x1MDAyN2xlblx1MDAyN10gZm9yIHMgaW4gc2NoZWR1bGUgaWYgc1tcdTAwMjd0eXBlXHUwMDI3XSA9PSBcdTAwMjdleHRlbmRlZFx1MDAyN11cbiAgICBzaG9ydF9jdCA9IHN1bSgxIGZvciBzIGluIHNjaGVkdWxlIGlmIHNbXHUwMDI3dHlwZVx1MDAyN10gPT0gXHUwMDI3c2hvcnRcdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN1Nob3J0IHN0ZXBzOiB7c2hvcnRfY3R9LCBFeHRlbmRlZCBzdGVwczoge2xlbihleHRfbGVucyl9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdNZWFuIGV4dGVuZGVkIGxlbmd0aCBhdCBzdGVwIDEwMDA6IHtucC5tZWFuKGV4dF9sZW5zWy0xMDA6XSk6LjBmfSB0b2tlbnNcdTAwMjcpXG4gICAgcmV0dXJuIHNjaGVkdWxlIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXh0ZW5zaW9uIFJhdGlvcyBhbmQgTGltaXRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZXh0ZW5zaW9uIHJhdGlvIGlzIExcdTAwMjcvTCDigJQgdGhlIGZhY3RvciBieSB3aGljaCBjb250ZXh0IGlzIGV4dGVuZGVkLiBQSSBpcyBwcmFjdGljYWxseSB0ZXN0ZWQgYXQgMsOXLCA0w5csIDjDlywgMTbDlywgYW5kIDMyw5cuIFdpdGhvdXQgZmluZS10dW5pbmcsIFBJIGFjaGlldmVzIG9ubHkgbWFyZ2luYWwgcGVycGxleGl0eSBpbXByb3ZlbWVudCBvdmVyIG5haXZlIGV4dHJhcG9sYXRpb24gYXQgcmF0aW9zIOKJpTTDly4gV2l0aCBmaW5lLXR1bmluZywgOMOXIGlzIHN0YWJsZSBhbmQgMTbDlyBzaG93cyBtb2Rlc3QgUFBMIGRlZ3JhZGF0aW9uLiBCZXlvbmQgMzLDlywgdGhlIGludGVycG9sYXRpb24gc2NhbGUgYmVjb21lcyBzbyBzbWFsbCAoc2NhbGUgXHUwMDNjIDAuMDMgZm9yIDMyw5cgZXh0ZW5zaW9uIG9mIGEgMksgbW9kZWwpIHRoYXQgZGlzdGluY3QgcG9zaXRpb25zIHdpdGhpbiB0aGUgZXh0ZW5kZWQgd2luZG93IG1hcCB0byBuZWFybHkgaWRlbnRpY2FsIGFuZ2xlIHZhbHVlcywgbWFraW5nIGl0IGltcG9zc2libGUgZm9yIHRoZSBtb2RlbCB0byBkaXN0aW5ndWlzaCBuZWFyYnkgcG9zaXRpb25zLiBBdCB0aGlzIHBvaW50LCByZXRyaWV2YWwgYWNjdXJhY3kgZHJvcHMgc2hhcnBseSByZWdhcmRsZXNzIG9mIGZpbmUtdHVuaW5nIGJ1ZGdldC4gVGhlIHByYWN0aWNhbCBjZWlsaW5nIGZvciB1bmlmb3JtIFBJIGlzIDE24oCTMzLDlzsgZm9yIGxhcmdlciB3aW5kb3dzLCBZYVJOIG9yIExvbmdSb1BFIHNpZ25pZmljYW50bHkgb3V0cGVyZm9ybSB1bmlmb3JtIFBJLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGV4dGVuc2lvbl9yYXRpb19zd2VlcCgpIC1cdTAwM2UgTm9uZTpcbiAgICAjIEFwcHJveGltYXRlIExMYU1BLTdCIHJlc3VsdHMgZnJvbSBDaGVuIGV0IGFsLiAoMjAyMykgb24gUEcxOSBwZXJwbGV4aXR5XG4gICAgcmF0aW9zICAgICAgICAgID0gWzEsICAgIDIsICAgIDQsICAgIDgsICAgIDE2LCAgICAzMiAgICBdXG4gICAgcHBsX25vX2ZpbmV0dW5lID0gWzcuMiwgIDkuOCwgIDE4LjQsIDQyLjEsIDIxMC4zLCA4NTAwLjBdXG4gICAgcHBsX2ZpbmV0dW5lZCAgID0gWzcuMiwgIDcuNCwgIDcuNywgIDguMSwgIDkuOCwgICAyNC41ICBdXG4gICAgcHBsX2V4dHJhcCAgICAgID0gWzcuMiwgIDE1LjYsIDI4MC40LCA1MjAwLCBOb25lLCAgTm9uZSAgXVxuICAgIHBhc3NrZXlfYWNjICAgICA9IFsxLjAwLCAwLjk4LCAwLjk1LCAwLjkxLCAwLjc0LCAgMC4yMSAgXVxuICAgIHByaW50KGZcdTAwMjd7XCJSYXRpb1wiOlx1MDAzZTd9IHwge1wiTm8tRlQgUFBMXCI6XHUwMDNlMTB9IHwge1wiRlQgUFBMXCI6XHUwMDNlOH0gfCB7XCJQSyBBY2NcIjpcdTAwM2U4fVx1MDAyNylcbiAgICBwcmludChcdTAwMjctXHUwMDI3ICogNDIpXG4gICAgZm9yIHIsIHBubywgcGZ0LCBwayBpbiB6aXAocmF0aW9zLCBwcGxfbm9fZmluZXR1bmUsIHBwbF9maW5ldHVuZWQsIHBhc3NrZXlfYWNjKTpcbiAgICAgICAgcHJpbnQoZlx1MDAyN3tyOlx1MDAzZTZ9eCB8IHtwbm86XHUwMDNlMTAuMWZ9IHwge3BmdDpcdTAwM2U4LjFmfSB8IHtwazpcdTAwM2U4LjJmfVx1MDAyNylcbiAgICBnb29kID0gW3IgZm9yIHIsIHBrIGluIHppcChyYXRpb3MsIHBhc3NrZXlfYWNjKSBpZiBwayBcdTAwM2U9IDAuOTBdXG4gICAgcHJpbnQoZlx1MDAyN1xcblJhdGlvcyB3aXRoIHBhc3NrZXkgYWNjdXJhY3kgXHUwMDNlPSA5MCU6IHtnb29kfVx1MDAyNylcblxuZXh0ZW5zaW9uX3JhdGlvX3N3ZWVwKCkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRXh0ZW5zaW9uIFJhdGlvIiwiRmluZS10dW5lIFN0ZXBzIiwiVHJhaW5pbmcgRGF0YSBNYXggTGVuIiwiUFBMIGF0IDF4IiwiUFBMIGF0IEV4dGVuc2lvbiIsIlBhc3NrZXkgQWNjdXJhY3kiXSwicm93cyI6W1siMnggKDJLIOKGkiA0SykiLCIyMDAiLCI0MDk2IHRva2VucyIsIjcuMiIsIjcuNCIsIjk4JSJdLFsiNHggKDJLIOKGkiA4SykiLCI0MDAiLCI4MTkyIHRva2VucyIsIjcuMiIsIjcuNyIsIjk1JSJdLFsiOHggKDJLIOKGkiAxNkspIiwiODAwIiwiMTYzODQgdG9rZW5zIiwiNy4yIiwiOC4xIiwiOTElIl0sWyIxNnggKDJLIOKGkiAzMkspIiwiMTAwMCIsIjMyNzY4IHRva2VucyIsIjcuMiIsIjkuOCIsIjc0JSJdLFsiMzJ4ICgySyDihpIgNjRLKSIsIjIwMDArIiwiNjU1MzYgdG9rZW5zIiwiNy4yIiwiMjQuNSIsIjIxJSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiB3aXRoIEV4dHJhcG9sYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5haXZlIFJvUEUgZXh0cmFwb2xhdGlvbiB5aWVsZHMgcGVycGxleGl0eSBvZiB+MjgwIGF0IG9ubHkgNMOXIGV4dGVuc2lvbiAodmVyc3VzIDcuNyB3aXRoIFBJIGZpbmUtdHVuaW5nKSBhbmQgZGl2ZXJnZXMgZW50aXJlbHkgYmV5b25kIHRoYXQuIFRoaXMgaXMgYmVjYXVzZSBSb1BFIGZyZXF1ZW5jeSBiYXNpcyBmdW5jdGlvbnMgYXJlIHBlcmlvZGljIOKAlCBhdCBwb3NpdGlvbnMgYmV5b25kIHRoZSB0cmFpbmluZyB3aW5kb3csIHBhdHRlcm5zIHJlcGVhdCB3aXRoIGEgZGlmZmVyZW50IHBoYXNlIHRoYW4gZXhwZWN0ZWQsIGNvcnJ1cHRpbmcgYWxsIGF0dGVudGlvbiBzY29yZXMgc2ltdWx0YW5lb3VzbHkuIEFMaUJpIChBdHRlbnRpb24gd2l0aCBMaW5lYXIgQmlhc2VzLCBQcmVzcyBldCBhbC4sIDIwMjIpIGVuYWJsZXMgZXh0cmFwb2xhdGlvbiBieSByZXBsYWNpbmcgUm9QRSB3aXRoIGEgcG9zaXRpb24taW5kZXBlbmRlbnQgYXR0ZW50aW9uIGJpYXMgbGVhcm5lZCBkdXJpbmcgcHJldHJhaW5pbmc7IGhvd2V2ZXIgQUxpQmkgbXVzdCBiZSBpbmNvcnBvcmF0ZWQgYXQgcHJldHJhaW5pbmcgdGltZSBhbmQgY2Fubm90IGJlIHBhdGNoZWQgaW50byBhbiBleGlzdGluZyBSb1BFIG1vZGVsLiBZYVJOIChQZW5nIGV0IGFsLiwgMjAyMykgYXBwbGllcyBub24tdW5pZm9ybSBpbnRlcnBvbGF0aW9uOiBoaWdoLWZyZXF1ZW5jeSBSb1BFIGNvbXBvbmVudHMgKHNtYWxsIGRpbWVuc2lvbiBpbmRleCBpLCBsYXJnZSDOuF9pKSBhcmUgc2NhbGVkIGxlc3MgYWdncmVzc2l2ZWx5IHRoYW4gbG93LWZyZXF1ZW5jeSBvbmVzLCBwcmVzZXJ2aW5nIHNob3J0LXJhbmdlIHJlbGF0aXZlIHBvc2l0aW9uIHNlbnNpdGl2aXR5IHdoaWxlIGV4dGVuZGluZyBsb25nLXJhbmdlIGNhcGFjaXR5LiBZYVJOIG91dHBlcmZvcm1zIHVuaWZvcm0gUEkgYXQgYWxsIGV4dGVuc2lvbiByYXRpb3MgYW5kIGhhcyBiZWNvbWUgdGhlIGRlLWZhY3RvIHN1Y2Nlc3Nvci4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlBJIFdhcyBhIFdhdGVyc2hlZCBSZXN1bHQiLCJjb250ZW50IjoiVGhlIFBJIHBhcGVyIHNob3dlZCB0aGF0IDEwMDAgZmluZS10dW5pbmcgc3RlcHMgKHRyaXZpYWwgY29tcHV0ZSkgd2l0aCBpbnRlcnBvbGF0ZWQgcG9zaXRpb25zIGNhbiBleHRlbmQgY29udGV4dCBmcm9tIDJLIHRvIDMySyDigJQgdGhpcyB3YXMgYSB3YXRlcnNoZWQgcmVzdWx0IHNob3dpbmcgY29udGV4dCBleHRlbnNpb24gaXMgY2hlYXAgcmVsYXRpdmUgdG8gcHJldHJhaW5pbmcuIE1vc3QgbG9uZy1jb250ZXh0IExsYW1hIGRlcml2YXRpdmVzIChMb25nQ2hhdCwgTG9uZ0FscGFjYSwgQ29kZUxsYW1hKSBhZG9wdGVkIHRoaXMgcmVjaXBlIGRpcmVjdGx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxvbmdMbGFtYSBhbmQgRm9sbG93LW9uIFdvcmsifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxvbmdMTGFNQSAoVHdvcmtvd3NraSBldCBhbC4sIDIwMjMpIGNvbWJpbmVzIFBJIHdpdGggdGhlIEZvY3VzZWQgVHJhbnNmb3JtZXIgKEZvVCkgYXJjaGl0ZWN0dXJlIOKAlCBhIG1lbW9yeSBtZWNoYW5pc20gdGhhdCByZXRyaWV2ZXMgcmVsZXZhbnQgS1YgcGFpcnMgZnJvbSBhIGxhcmdlIGV4dGVybmFsIG1lbW9yeSBzdG9yZSBhdCBlYWNoIGZvcndhcmQgcGFzcyDigJQgYWNoaWV2aW5nIGVmZmVjdGl2ZSBjb250ZXh0cyBvZiAyNTZLIHRva2VucyBvbiBQQVNTS0VZIGJlbmNobWFya3MuIExvbmdDaGF0IChEYWNoZW5nIExpIGV0IGFsLiwgMjAyMykgYXBwbGllZCBQSSB0byBMTGFNQS0xIGF0IDE2SyBhbmQgZXZhbHVhdGVkIG9uIG11bHRpLXR1cm4gY29udmVyc2F0aW9uIHRvcGljIHJldHJpZXZhbCB0YXNrcy4gTG9uZ0FscGFjYSAoQ2hlbiBldCBhbC4sIDIwMjMpIGFkZGVkIFBJIHRvIExMYU1BLTIgd2l0aCBpbnN0cnVjdGlvbi10dW5pbmcgb24gc3VtbWFyaXphdGlvbiBkYXRhLCBkZW1vbnN0cmF0aW5nIHRoYXQgaW5zdHJ1Y3Rpb24tZm9sbG93aW5nIHF1YWxpdHkgaXMgcHJlc2VydmVkLiBDb2RlTGxhbWEgKFJvemnDqHJlIGV0IGFsLiwgMjAyMykgZXh0ZW5kZWQgdG8gMTAwSyBjb250ZXh0IHVzaW5nIFBJIHdpdGggMTZLIGZpbmUtdHVuaW5nIGRhdGEsIGFjaGlldmluZyBzdXBlcmlvciBwZXJmb3JtYW5jZSBvbiByZXBvc2l0b3J5LWxldmVsIGNvZGUgY29tcGxldGlvbi4gWWFSTiBhbmQgTG9uZ1JvUEUgc3Vic2VxdWVudGx5IGltcHJvdmVkIHBvc2l0aW9uIHNjYWxpbmcgd2l0aCBub24tdW5pZm9ybSBhbmQgcGVyLWRpbWVuc2lvbiBtZXRob2RzIHJlc3BlY3RpdmVseS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkxvbmdDaGF0ICgyMDIzKTogUEkgYXBwbGllZCB0byBMTGFNQS0xIGF0IDE2SyB0b2tlbnMsIGV2YWx1YXRlZCBvbiBtdWx0aS10dXJuIHRvcGljIHJldHJpZXZhbC4iLCJMb25nQWxwYWNhICgyMDIzKTogUEkgcGx1cyBpbnN0cnVjdGlvbiB0dW5pbmcgb24gc3VtbWFyaXphdGlvbiBkYXRhIGF0IDMySyB3aXRoIExMYU1BLTIgYmFzZS4iLCJMb25nTExhTUEgKDIwMjMpOiBQSSBjb21iaW5lZCB3aXRoIEZvY3VzZWQgVHJhbnNmb3JtZXIgbWVtb3J5LCBlZmZlY3RpdmUgMjU2SyBjb250ZXh0IG9uIFBBU1NLRVkuIiwiQ29kZUxsYW1hICgyMDIzKTogUEkgdG8gMTAwSyB0b2tlbnMgZm9yIGxvbmctY29kZSBnZW5lcmF0aW9uIG9uIExMYU1BLTIgYmFzZS4iLCJZYVJOICgyMDIzKTogTm9uLXVuaWZvcm0gcG9zaXRpb24gc2NhbGluZzsgaGlnaC1mcmVxdWVuY3kgUm9QRSBjb21wb25lbnRzIHNjYWxlZCBsZXNzIGFnZ3Jlc3NpdmVseS4iLCJMb25nUm9QRSAoMjAyNCk6IExlYXJuZWQgcGVyLWRpbWVuc2lvbiBzY2FsaW5nIGZhY3RvcnMgZm9yIGNvbnRleHQgZXh0ZW5zaW9uIHVwIHRvIDJNIHRva2Vucy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUG9zaXRpb24gSW50ZXJwb2xhdGlvbiBkZW1vbnN0cmF0ZWQgdGhhdCBleHRlbmRpbmcgUm9QRS1iYXNlZCBjb250ZXh0IHdpbmRvd3MgaXMgYSBsb3ctY29zdCBlbmdpbmVlcmluZyBwcm9ibGVtIHdpdGggYSBjbGVhbiBzb2x1dGlvbjogY29tcHJlc3MgcG9zaXRpb25zIGludG8gdGhlIHRyYWluZWQgcmFuZ2UsIHRoZW4gZmluZS10dW5lIGJyaWVmbHkgdG8gcmUtYWRhcHQuIFRoZSBtZXRob2QgcmVxdWlyZXMgbm8gYXJjaGl0ZWN0dXJlIGNoYW5nZXMg4oCUIG9ubHkgdGhlIFJvUEUgZm9yd2FyZCBtZXRob2QgaXMgbW9kaWZpZWQg4oCUIG1ha2luZyBpdCB0cml2aWFsbHkgYXBwbGljYWJsZSB0byBhbnkgcHJldHJhaW5lZCBSb1BFIG1vZGVsLiBJdHMgcHJhY3RpY2FsIGNlaWxpbmcgaXMgMTbigJMzMsOXIGV4dGVuc2lvbiB3aXRoIHVuaWZvcm0gc2NhbGluZzsgWWFSTiBhbmQgTG9uZ1JvUEUgcHJvdmlkZSBiZXR0ZXIgcmVzdWx0cyBiZXlvbmQgdGhhdC4gUEkgcmVtYWlucyB0aGUgbW9zdCB3aWRlbHkgZGVwbG95ZWQgY29udGV4dCBleHRlbnNpb24gdGVjaG5pcXVlIGR1ZSB0byBpdHMgc2ltcGxpY2l0eSwgc3Ryb25nIG9wZW4tc291cmNlIHRvb2xpbmcsIGFuZCB0aGUgYnJvYWQgYXZhaWxhYmlsaXR5IG9mIFBJLWV4dGVuZGVkIGNoZWNrcG9pbnRzIGZvciB0aGUgTExhTUEgbW9kZWwgZmFtaWx5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUEkgZm9ybXVsYTogcG9zX2ludGVycChwKSA9IHAgw5cgKEwvTFx1MDAyNyksIHdoZXJlIEwgaXMgdGhlIG9yaWdpbmFsIG1heCBsZW5ndGggYW5kIExcdTAwMjcgaXMgdGhlIGV4dGVuZGVkIGxlbmd0aC4iLCJGaW5lLXR1bmluZyBpcyBtYW5kYXRvcnk6IFBJIHdpdGhvdXQgZmluZS10dW5pbmcgcHJvdmlkZXMgbWluaW1hbCBpbXByb3ZlbWVudCBvdmVyIHJhdyBleHRyYXBvbGF0aW9uLiIsIjIwMCBzdGVwcyBzdWZmaWNpZW50IGZvciA4eCBleHRlbnNpb247IDEwMDAgc3RlcHMgcmVjb21tZW5kZWQgZm9yIDE2eCBleHRlbnNpb24gc3RhYmlsaXR5LiIsIlVzZSBtaXhlZC1sZW5ndGggdHJhaW5pbmcgZGF0YTogODAlIHNob3J0IGRvY3MgKyAyMCUgZXh0ZW5kZWQgZG9jcyBkdXJpbmcgZmluZS10dW5pbmcuIiwiUGFzc2tleSByZXRyaWV2YWwgYWNjdXJhY3kgaXMgdGhlIGdvbGQgc3RhbmRhcmQgbWV0cmljLCBub3QgcGVycGxleGl0eSwgZm9yIGVmZmVjdGl2ZSBjb250ZXh0IGxlbmd0aC4iLCJGb3IgMzJ4KyBleHRlbnNpb24sIHByZWZlciBZYVJOIChub24tdW5pZm9ybSBzY2FsaW5nKSBvdmVyIHVuaWZvcm0gUEkgZm9yIGJldHRlciByZXRyaWV2YWwgYWNjdXJhY3kuIiwiVGhlIFBJIHBhdGNoIGlzIGFyY2hpdGVjdHVyZS1hZ25vc3RpYzogc3dhcCB0aGUgcm90YXJ5X2VtYiBtb2R1bGUgd2l0aCBQSVJvUEUgdG8gZW5hYmxlIGV4dGVuc2lvbi4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Position Interpolation for Long Context LLMs

Position Interpolation (Chen et al., 2023) is a method for extending the context window of Rotary Position Embedding (RoPE)-based LLMs without full retraining. The core insight is that extrapolating beyond the trained maximum position causes catastrophic perplexity collapse: RoPE embeddings at unseen positions produce rotation angles that are entirely out-of-distribution for every attention head in every layer. Position Interpolation avoids this by down-scaling all token positions so they always lie within the original training range [0, L), then fine-tuning for a trivially small number of steps to re-adapt the model to the compressed scale. This paper established the foundational recipe that dozens of Llama variants — LongChat, LongAlpaca, CodeLlama, and LongLLaMA — adopted for affordable context extension at a fraction of the original pretraining cost.

## Overview

Pre-trained RoPE models have a hard context ceiling: position indices 0 through L-1 (e.g., 0–2047 for LLaMA-1). When inference extends to position L or beyond, the RoPE rotation frequencies θ_i × p for those indices were never seen during training. The PI approach remaps position p to p_scaled = p × (L/L'), where L is the original max length and L' is the target extended length. At the last valid position L'-1, the remapped value is (L'-1) × (L/L') ≈ L-1, keeping all positions in-distribution. A brief fine-tuning run of 200–1000 steps on mixed-length next-token prediction data adapts the model to the new scale. Extending LLaMA-7B from 2K to 32K costs roughly 0.01% of the original pretraining compute — a watershed result demonstrating that context extension is a cheap engineering problem.

## The PI Formula

RoPE encodes position p by rotating each pair of head dimensions (x_{2i}, x_{2i+1}) by angle p × θ_i, where θ_i = 10000^{-2i/d} and d is the head dimension. The query-key attention score contains terms proportional to cos((p-q) × θ_i) — a relative positional encoding. At positions beyond L, the angle differences (p-q) × θ_i involve values never seen during training, causing cosine/sine outputs to land in unexpected regions of the embedding space. PI replaces p with p_interp = p × (L/L') throughout all RoPE computations. The scale factor L/L' < 1 compresses all positions into [0, L), preserving the model's learned rotational geometry. The relative angle difference for positions p and q becomes (p-q) × (L/L') × θ_i — smaller absolute differences but always within the trained distribution of angle magnitudes.

```python
import torch
import torch.nn as nn
from transformers import LlamaForCausalLM

class PIRoPE(nn.Module):
    # Rotary Position Embedding with Position Interpolation (Chen et al., 2023)
    # Compresses position indices into [0, orig_max_len) via a fixed scale factor
    def __init__(self, dim: int, orig_max_len: int = 2048, new_max_len: int = 32768):
        super().__init__()
        self.scale = orig_max_len / new_max_len  # < 1.0 for any extension
        inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer('inv_freq', inv_freq)

    def forward(self, x: torch.Tensor, seq_len: int):
        # Interpolated positions always stay in [0, orig_max_len) regardless of seq_len
        t = torch.arange(seq_len, device=x.device).float() * self.scale
        freqs = torch.outer(t, self.inv_freq)
        emb = torch.cat((freqs, freqs), dim=-1)
        return emb.cos().unsqueeze(0).unsqueeze(0), emb.sin().unsqueeze(0).unsqueeze(0)

def patch_rope_pi(model: LlamaForCausalLM, new_max_len: int = 32768) -> LlamaForCausalLM:
    # Replace all RoPE modules in-place with position-interpolating variants
    orig = model.config.max_position_embeddings
    for layer in model.model.layers:
        head_dim = layer.self_attn.rotary_emb.dim
        layer.self_attn.rotary_emb = PIRoPE(head_dim, orig, new_max_len)
    model.config.max_position_embeddings = new_max_len
    print(f'PI patch: scale={orig/new_max_len:.4f}, context {orig} -> {new_max_len}')
    return model
```

## Training Protocol

After applying the PI patch, a short fine-tuning run re-adapts the model to the compressed position scale. The Chen et al. protocol: fine-tune for 200–1000 steps with next-token prediction loss on documents up to the new maximum length. Documents shorter than the target length are concatenated to fill context windows; no padding is required. Training data should match the pretraining distribution — typically a mix of English web text and code from the same sources used for pretraining. Learning rate is set to 2e-5, consistent with standard instruction-tuning. The paper shows 200 steps suffices for 8× extension, and 1000 steps provides stability at 16×. With 8×A100 80GB GPUs and Flash Attention 2, fine-tuning LLaMA-7B to 32K context at 1000 steps takes 4–8 hours — trivial relative to thousands of GPU-hours for pretraining.

```python
import random
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def build_passkey_prompt(passkey: str, depth: float, reps: int = 200) -> str:
    # Place a secret passkey at fractional depth inside a long filler document
    filler = 'Researchers observed no statistically significant effect in this condition. ' * reps
    pos = int(depth * len(filler))
    needle = f' [THE SECRET PASSKEY IS: {passkey}] '
    return filler[:pos] + needle + filler[pos:] + '\nQuestion: What is the secret passkey? Answer:'

def eval_passkey_retrieval(model, tokenizer, ctx_len: int,
                           depths: list, n_each: int = 5) -> dict:
    # Measure retrieval accuracy at each depth fraction for the given context length
    results = {}
    for depth in depths:
        hits = 0
        for _ in range(n_each):
            pk = str(random.randint(10000, 99999))
            prompt = build_passkey_prompt(pk, depth)
            ids = tokenizer(prompt, return_tensors='pt', truncation=True,
                            max_length=ctx_len).input_ids.to(model.device)
            with torch.no_grad():
                out = model.generate(ids, max_new_tokens=10)
            text = tokenizer.decode(out[0][ids.shape[1]:], skip_special_tokens=True)
            hits += int(pk in text)
        results[f'{depth:.0%}'] = hits / n_each
        print(f'  depth={depth:.0%}: {hits}/{n_each} correct')
    return results

depths = [0.0, 0.25, 0.5, 0.75, 1.0]
print(f'Passkey benchmark depths: {[f"{d:.0%}" for d in depths]}')
```

## Effective Context Length

Perplexity is an unreliable proxy for effective context length. A model can achieve low perplexity at 32K tokens while failing to retrieve information from beyond 4K — because perplexity averages over all tokens and is dominated by local context. Passkey retrieval provides a precise binary signal: embed a random 5-digit number at a controlled fractional position in a long filler document, then query the model for it. PI-fine-tuned LLaMA-2-7B achieves near-perfect passkey retrieval up to its extended context length, while the baseline collapses beyond 4K regardless of depth. Effective context length is formally defined as the largest L at which retrieval accuracy exceeds 90% across all five depth positions (0%, 25%, 50%, 75%, 100%). This benchmark is now standard for long-context model evaluation.

```python
import numpy as np

def simulate_curriculum_mixing(base_max: int = 2048, target_max: int = 32768,
                               total_steps: int = 1000, short_frac: float = 0.8):
    # Curriculum: 80% short docs + 20% extended docs; extended length ramps up gradually
    schedule = []
    for step in range(total_steps):
        progress = step / total_steps
        # Extended doc length grows from 2x base to target_max over training
        ext_len = int(base_max * 2 + progress * (target_max - base_max * 2))
        ext_len = min(ext_len, target_max)
        if np.random.rand() < short_frac:
            doc_len = int(np.random.randint(256, base_max))
            label = 'short'
        else:
            doc_len = ext_len
            label = 'extended'
        schedule.append({'step': step, 'len': doc_len, 'type': label})
    ext_lens = [s['len'] for s in schedule if s['type'] == 'extended']
    short_ct = sum(1 for s in schedule if s['type'] == 'short')
    print(f'Short steps: {short_ct}, Extended steps: {len(ext_lens)}')
    print(f'Mean extended length at step 1000: {np.mean(ext_lens[-100:]):.0f} tokens')
    return schedule
```

## Extension Ratios and Limits

The extension ratio is L'/L — the factor by which context is extended. PI is practically tested at 2×, 4×, 8×, 16×, and 32×. Without fine-tuning, PI achieves only marginal perplexity improvement over naive extrapolation at ratios ≥4×. With fine-tuning, 8× is stable and 16× shows modest PPL degradation. Beyond 32×, the interpolation scale becomes so small (scale < 0.03 for 32× extension of a 2K model) that distinct positions within the extended window map to nearly identical angle values, making it impossible for the model to distinguish nearby positions. At this point, retrieval accuracy drops sharply regardless of fine-tuning budget. The practical ceiling for uniform PI is 16–32×; for larger windows, YaRN or LongRoPE significantly outperform uniform PI.

```python
import numpy as np

def extension_ratio_sweep() -> None:
    # Approximate LLaMA-7B results from Chen et al. (2023) on PG19 perplexity
    ratios          = [1,    2,    4,    8,    16,    32    ]
    ppl_no_finetune = [7.2,  9.8,  18.4, 42.1, 210.3, 8500.0]
    ppl_finetuned   = [7.2,  7.4,  7.7,  8.1,  9.8,   24.5  ]
    ppl_extrap      = [7.2,  15.6, 280.4, 5200, None,  None  ]
    passkey_acc     = [1.00, 0.98, 0.95, 0.91, 0.74,  0.21  ]
    print(f'{"Ratio":>7} | {"No-FT PPL":>10} | {"FT PPL":>8} | {"PK Acc":>8}')
    print('-' * 42)
    for r, pno, pft, pk in zip(ratios, ppl_no_finetune, ppl_finetuned, passkey_acc):
        print(f'{r:>6}x | {pno:>10.1f} | {pft:>8.1f} | {pk:>8.2f}')
    good = [r for r, pk in zip(ratios, passkey_acc) if pk >= 0.90]
    print(f'\nRatios with passkey accuracy >= 90%: {good}')

extension_ratio_sweep()
```

| Extension Ratio | Fine-tune Steps | Training Data Max Len | PPL at 1x | PPL at Extension | Passkey Accuracy |
| --- | --- | --- | --- | --- | --- |
| 2x (2K → 4K) | 200 | 4096 tokens | 7.2 | 7.4 | 98% |
| 4x (2K → 8K) | 400 | 8192 tokens | 7.2 | 7.7 | 95% |
| 8x (2K → 16K) | 800 | 16384 tokens | 7.2 | 8.1 | 91% |
| 16x (2K → 32K) | 1000 | 32768 tokens | 7.2 | 9.8 | 74% |
| 32x (2K → 64K) | 2000+ | 65536 tokens | 7.2 | 24.5 | 21% |

## Comparison with Extrapolation

Naive RoPE extrapolation yields perplexity of ~280 at only 4× extension (versus 7.7 with PI fine-tuning) and diverges entirely beyond that. This is because RoPE frequency basis functions are periodic — at positions beyond the training window, patterns repeat with a different phase than expected, corrupting all attention scores simultaneously. ALiBi (Attention with Linear Biases, Press et al., 2022) enables extrapolation by replacing RoPE with a position-independent attention bias learned during pretraining; however ALiBi must be incorporated at pretraining time and cannot be patched into an existing RoPE model. YaRN (Peng et al., 2023) applies non-uniform interpolation: high-frequency RoPE components (small dimension index i, large θ_i) are scaled less aggressively than low-frequency ones, preserving short-range relative position sensitivity while extending long-range capacity. YaRN outperforms uniform PI at all extension ratios and has become the de-facto successor.

> **PI Was a Watershed Result**: The PI paper showed that 1000 fine-tuning steps (trivial compute) with interpolated positions can extend context from 2K to 32K — this was a watershed result showing context extension is cheap relative to pretraining. Most long-context Llama derivatives (LongChat, LongAlpaca, CodeLlama) adopted this recipe directly.

## LongLlama and Follow-on Work

LongLLaMA (Tworkowski et al., 2023) combines PI with the Focused Transformer (FoT) architecture — a memory mechanism that retrieves relevant KV pairs from a large external memory store at each forward pass — achieving effective contexts of 256K tokens on PASSKEY benchmarks. LongChat (Dacheng Li et al., 2023) applied PI to LLaMA-1 at 16K and evaluated on multi-turn conversation topic retrieval tasks. LongAlpaca (Chen et al., 2023) added PI to LLaMA-2 with instruction-tuning on summarization data, demonstrating that instruction-following quality is preserved. CodeLlama (Rozière et al., 2023) extended to 100K context using PI with 16K fine-tuning data, achieving superior performance on repository-level code completion. YaRN and LongRoPE subsequently improved position scaling with non-uniform and per-dimension methods respectively.

- LongChat (2023): PI applied to LLaMA-1 at 16K tokens, evaluated on multi-turn topic retrieval.
- LongAlpaca (2023): PI plus instruction tuning on summarization data at 32K with LLaMA-2 base.
- LongLLaMA (2023): PI combined with Focused Transformer memory, effective 256K context on PASSKEY.
- CodeLlama (2023): PI to 100K tokens for long-code generation on LLaMA-2 base.
- YaRN (2023): Non-uniform position scaling; high-frequency RoPE components scaled less aggressively.
- LongRoPE (2024): Learned per-dimension scaling factors for context extension up to 2M tokens.

## Key Takeaways

Position Interpolation demonstrated that extending RoPE-based context windows is a low-cost engineering problem with a clean solution: compress positions into the trained range, then fine-tune briefly to re-adapt. The method requires no architecture changes — only the RoPE forward method is modified — making it trivially applicable to any pretrained RoPE model. Its practical ceiling is 16–32× extension with uniform scaling; YaRN and LongRoPE provide better results beyond that. PI remains the most widely deployed context extension technique due to its simplicity, strong open-source tooling, and the broad availability of PI-extended checkpoints for the LLaMA model family.

- PI formula: pos_interp(p) = p × (L/L'), where L is the original max length and L' is the extended length.
- Fine-tuning is mandatory: PI without fine-tuning provides minimal improvement over raw extrapolation.
- 200 steps sufficient for 8x extension; 1000 steps recommended for 16x extension stability.
- Use mixed-length training data: 80% short docs + 20% extended docs during fine-tuning.
- Passkey retrieval accuracy is the gold standard metric, not perplexity, for effective context length.
- For 32x+ extension, prefer YaRN (non-uniform scaling) over uniform PI for better retrieval accuracy.
- The PI patch is architecture-agnostic: swap the rotary_emb module with PIRoPE to enable extension.

---

