---
title: "LongLoRA: Efficient Fine-tuning for Long Context"
slug: "longlora"
description: "Combining shifted sparse attention (S²-Attn) during fine-tuning with LoRA to extend LLM context from 4K to 100K tokens at a fraction of the compute cost of full fine-tuning."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9uZ0xvUkEgKENoZW4gZXQgYWwuLCAyMDIzKSBpcyBhIHBhcmFtZXRlci1lZmZpY2llbnQgbWV0aG9kIGZvciBleHRlbmRpbmcgdGhlIGNvbnRleHQgd2luZG93IG9mIHByZXRyYWluZWQgbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzIHdpdGhvdXQgdGhlIHByb2hpYml0aXZlIGNvbXB1dGUgY29zdCBvZiBmdWxsIGZpbmUtdHVuaW5nLiBTdGFydGluZyBmcm9tIExsYW1hLTIgd2l0aCBhIDRLLXRva2VuIGNvbnRleHQgbGltaXQsIExvbmdMb1JBIGV4dGVuZHMgY29udGV4dCB0byAzMkssIDY1Sywgb3IgMTAwSyB0b2tlbnMgdXNpbmcgdHdvIGNvbXBsZW1lbnRhcnkgdGVjaG5pcXVlczogU2hpZnRlZCBTcGFyc2UgQXR0ZW50aW9uIChTwrItQXR0bikgZm9yIHRyYWluaW5nLXRpbWUgY29tcHV0ZSBlZmZpY2llbmN5LCBhbmQgTG9SQSBmb3IgcGFyYW1ldGVyIGVmZmljaWVuY3kuIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IGFwcHJveGltYXRlIHNwYXJzZSBhdHRlbnRpb24gZHVyaW5nIHRyYWluaW5nIGlzIHN1ZmZpY2llbnQgZm9yIHRoZSBtb2RlbCB0byBsZWFybiBsb25nLXJhbmdlIGRlcGVuZGVuY2llcywgZXZlbiB0aG91Z2ggZnVsbCBhdHRlbnRpb24gaXMgcmVzdG9yZWQgYXQgaW5mZXJlbmNlIHRpbWUg4oCUIHNvIGRlcGxveW1lbnQgcmVxdWlyZXMgbm8gc3BlY2lhbCBrZXJuZWxzIG9yIGFyY2hpdGVjdHVyYWwgY2hhbmdlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRnVsbCBmaW5lLXR1bmluZyB3aXRoIGZ1bGwgYXR0ZW50aW9uIG9uIDEwMEstdG9rZW4gc2VxdWVuY2VzIGlzIGNvbXB1dGF0aW9uYWxseSBwcm9oaWJpdGl2ZTogdGhlIGF0dGVudGlvbiBtYXRyaXggaGFzIE8obsKyKSBjb21wbGV4aXR5LCBzbyBzY2FsaW5nIGZyb20gNEsgdG8gMzJLIG11bHRpcGxpZXMgYXR0ZW50aW9uIGNvbXB1dGUgYnkgNjTDlyBhbmQgbWVtb3J5IGJ5IHRoZSBzYW1lIGZhY3Rvci4gRm9yIGEgN0IgbW9kZWwgb24gODBHQiBBMTAwIEdQVXMsIGZ1bGwgZmluZS10dW5pbmcgYXQgMzJLIHRva2VucyByZXF1aXJlcyBhdCBsZWFzdCA4IEdQVXMgYW5kIHRob3VzYW5kcyBvZiBHUFUgaG91cnMuIExvbmdMb1JBIHJlZHVjZXMgdGhpcyB0byBhIHNpbmdsZSA4MEdCIEdQVSBmb3IgMzJLLXRva2VuIHNlcXVlbmNlcywgYW5kIHRvIDItNCBHUFVzIGZvciA2NUstMTAwSyB0b2tlbnMsIG1ha2luZyBsb25nLWNvbnRleHQgZmluZS10dW5pbmcgYWNjZXNzaWJsZSBhdCBtb2Rlc3QgY29zdC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxvbmdMb1JBIGFjaGlldmVzIGVmZmljaWVuY3kgdGhyb3VnaCB0d28gbWVjaGFuaXNtcyB0aGF0IGNvbXBvdW5kOiBTwrItQXR0biByZWR1Y2VzIGF0dGVudGlvbiBjb21wdXRlIGZyb20gTyhuwrIpIHRvIE8obiDDlyBnKSB3aGVyZSBnIGlzIHRoZSBncm91cCBzaXplICh0eXBpY2FsbHkgMjA0OCksIGdpdmluZyBhIDE2w5cgcmVkdWN0aW9uIGF0IDMySyB0b2tlbnMuIExvUkEgd2l0aCByPTggYXBwbGllZCB0byBRLCBLLCBWLCBPIHByb2plY3Rpb25zIHJlZHVjZXMgdHJhaW5hYmxlIHBhcmFtZXRlcnMgZnJvbSB+N0IgdG8gfjUwTSDigJQgYSAxNDDDlyByZWR1Y3Rpb24uIFRoZSB0d28gdGVjaG5pcXVlcyBhcmUgbGFyZ2VseSBvcnRob2dvbmFsIGluIHdoYXQgdGhleSBvcHRpbWl6ZSDigJQgbWVtb3J5L2NvbXB1dGUgdnMuIHBhcmFtZXRlciBjb3VudCDigJQgYWxsb3dpbmcgdGhlbSB0byBiZSBjb21iaW5lZCB3aXRob3V0IHNpZ25pZmljYW50IHF1YWxpdHkgZGVncmFkYXRpb24uIFRoZSByZXN1bHRpbmcgcGVycGxleGl0eSBvbiBsb25nLWRvY3VtZW50IGJlbmNobWFya3MgaXMgd2l0aGluIDAuMy0wLjUgUFBMIG9mIGZ1bGwgZmluZS10dW5pbmcgd2l0aCBmdWxsIGF0dGVudGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgQ2hhbGxlbmdlIG9mIExvbmctQ29udGV4dCBGaW5lLXR1bmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1lbW9yeSBjb3N0IG9mIGZ1bGwgYXR0ZW50aW9uIGF0IGxvbmcgY29udGV4dCBpcyB0aGUgcHJpbWFyeSBvYnN0YWNsZS4gRm9yIGEgdHJhbnNmb3JtZXIgd2l0aCAzMiBhdHRlbnRpb24gaGVhZHMgb2YgZGltZW5zaW9uIDEyOCwgdGhlIGF0dGVudGlvbiB3ZWlnaHQgbWF0cml4IGF0IHNlcXVlbmNlIGxlbmd0aCAzMjc2OCBoYXMgc2hhcGUgKGJhdGNoLCAzMiwgMzI3NjgsIDMyNzY4KS4gQXQgZmxvYXQxNiwgbWF0ZXJpYWxpemluZyB0aGlzIGNvc3RzIDMyIMOXIDMyNzY4wrIgw5cgMiBieXRlcyDiiYggNjUgR0IgcGVyIGxheWVyIOKAlCBtb3JlIHRoYW4gYSBmdWxsIEExMDAuIEZsYXNoIGF0dGVudGlvbiBhdm9pZHMgbWF0ZXJpYWxpemluZyB0aGUgZnVsbCBtYXRyaXggYnkgY29tcHV0aW5nIGF0dGVudGlvbiBpbiB0aWxlcywgYnV0IHRoZSBiYWNrd2FyZCBwYXNzIHN0aWxsIHJlcXVpcmVzIE8obsKyKSBmbG9wcyBhbmQgc3RvcmluZyBPKG4pIHNvZnRtYXggZGVub21pbmF0b3JzIHBlciBoZWFkLiBBdCAxMDBLIHRva2VucywgZXZlbiBmbGFzaCBhdHRlbnRpb24gd2l0aCBncmFkaWVudCBjaGVja3BvaW50aW5nIHdvdWxkIHJlcXVpcmUgYXBwcm94aW1hdGVseSA0MDAgR0Igb2YgR1BVIG1lbW9yeSBmb3IgYSA3QiBtb2RlbCBpbiBmdWxsIGZpbmUtdHVuaW5nIG1vZGUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcG9zaXRpb25hbCBlbmNvZGluZyBjaGFsbGVuZ2UgaXMgZXF1YWxseSBpbXBvcnRhbnQuIFByZXRyYWluZWQgTGxhbWEtMiB1c2VzIFJvdGFyeSBQb3NpdGlvbiBFbWJlZGRpbmcgKFJvUEUpIHdpdGggZnJlcXVlbmNpZXMgdHVuZWQgdG8gdGhlIHByZXRyYWluIGNvbnRleHQgbGVuZ3RoIG9mIDQwOTYuIFRva2VuIHBvc2l0aW9ucyBiZXlvbmQgNDA5NiBhcmUgY29tcGxldGVseSBvdXQtb2YtZGlzdHJpYnV0aW9uLiBQb3NpdGlvbiBpbnRlcnBvbGF0aW9uIChQSSkgYWRkcmVzc2VzIHRoaXMgYnkgcmVzY2FsaW5nIHBvc2l0aW9ucyBmcm9tIFswLCB0YXJnZXRfbGVuXSBiYWNrIHRvIFswLCA0MDk2XSwga2VlcGluZyBwb3NpdGlvbnMgd2l0aGluIHRoZSBkaXN0cmlidXRpb24gc2VlbiBkdXJpbmcgcHJldHJhaW5pbmcuIEhvd2V2ZXIsIFBJIGFsb25lIGNhdXNlcyBzaWduaWZpY2FudCBxdWFsaXR5IGRlZ3JhZGF0aW9uIGJlY2F1c2UgdGhlIG1vZGVsXHUwMDI3cyBhdHRlbnRpb24gcGF0dGVybnMsIGdhdGUgZnVuY3Rpb25zLCBhbmQgTUxQIGFjdGl2YXRpb25zIGhhdmUgbGVhcm5lZCBjb250ZXh0LWxlbmd0aC1zcGVjaWZpYyBiZWhhdmlvcnMuIEZpbmUtdHVuaW5nIG9uIGxvbmcgc2VxdWVuY2VzIGlzIHJlcXVpcmVkIHRvIGFkYXB0IHRoZXNlIGNvbXBvbmVudHMuIFdpdGhvdXQgZmluZS10dW5pbmcsIFBJLWV4dGVuZGVkIG1vZGVscyBleGhpYml0IHBlcnBsZXhpdHkgMi0xMMOXIHdvcnNlIHRoYW4gdGhlIHByZXRyYWluZWQgYmFzZWxpbmUgb24gbG9uZyBpbnB1dHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2hpZnRlZCBTcGFyc2UgQXR0ZW50aW9uIChTwrItQXR0bikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlPCsi1BdHRuIHBhcnRpdGlvbnMgdGhlIHRva2VuIHNlcXVlbmNlIGludG8gbm9uLW92ZXJsYXBwaW5nIGxvY2FsIHdpbmRvd3Mgb2YgZyB0b2tlbnMgKHR5cGljYWxseSBnPTIwNDgpIGFuZCBjb21wdXRlcyBmdWxsIGF0dGVudGlvbiB3aXRoaW4gZWFjaCB3aW5kb3cgaW5kZXBlbmRlbnRseS4gV2l0aCBnPTIwNDggb24gYSAzMksgc2VxdWVuY2UsIHRoaXMgY3JlYXRlcyAxNiBncm91cHMsIGVhY2ggcmVxdWlyaW5nIGfCsiA9IDRNIGF0dGVudGlvbiBvcGVyYXRpb25zIGluc3RlYWQgb2YgbsKyID0gMS4wN0IuIFRvdGFsIGF0dGVudGlvbiBjb21wdXRlIGRyb3BzIGZyb20gTyhuwrIpIHRvIE8obiDDlyBnKSwgYSAxNsOXIHJlZHVjdGlvbi4gVGhlIGxpbWl0YXRpb24gb2YgcHVyZSBsb2NhbCBhdHRlbnRpb24gaXMgdGhhdCB0b2tlbnMgaW4gZGlmZmVyZW50IGdyb3VwcyBjYW5ub3QgYXR0ZW5kIHRvIGVhY2ggb3RoZXIsIHdoaWNoIHdvdWxkIHByZXZlbnQgdGhlIG1vZGVsIGZyb20gbGVhcm5pbmcgY3Jvc3MtZ3JvdXAgbG9uZy1yYW5nZSBkZXBlbmRlbmNpZXMgZXNzZW50aWFsIGZvciB0YXNrcyBsaWtlIGZvbGxvd2luZyBpbnN0cnVjdGlvbnMgdGhhdCBhcHBlYXIgYXQgdGhlIHN0YXJ0IG9mIGEgbG9uZyBkb2N1bWVudC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzaGlmdCBtZWNoYW5pc20gYWRkcmVzc2VzIGNyb3NzLWdyb3VwIGNvbW11bmljYXRpb24uIEEgc2Vjb25kIGF0dGVudGlvbiBwYXNzIHNoaWZ0cyBhbGwgcG9zaXRpb25zIGJ5IGcvMiB0b2tlbnMgYmVmb3JlIGdyb3VwaW5nLCBwbGFjaW5nIG9yaWdpbmFsIGdyb3VwIGJvdW5kYXJpZXMgaW4gdGhlIG1pZGRsZSBvZiBuZXcgZ3JvdXBzLiBUb2tlbnMgdGhhdCB3ZXJlIHNlcGFyYXRlZCBhY3Jvc3MgdHdvIG9yaWdpbmFsIHdpbmRvd3Mgbm93IHNoYXJlIGEgc2hpZnRlZCB3aW5kb3cgYW5kIGNhbiBhdHRlbmQgdG8gZWFjaCBvdGhlci4gVGhlIHR3byBhdHRlbnRpb24gb3V0cHV0cyAobG9jYWwgYW5kIHNoaWZ0ZWQtbG9jYWwpIGFyZSBhdmVyYWdlZC4gT3ZlciBtdWx0aXBsZSB0cmFuc2Zvcm1lciBsYXllcnMsIHRoaXMgZW5hYmxlcyBlZmZlY3RpdmUgbG9uZy1yYW5nZSBpbmZvcm1hdGlvbiBwcm9wYWdhdGlvbiBkZXNwaXRlIHRoZSBzcGFyc2UgcGVyLWxheWVyIHBhdHRlcm4uIFRoZSBjcml0aWNhbCBwcm9wZXJ0eSBpcyB0aGF0IFPCsi1BdHRuIGlzIG9ubHkgYWN0aXZlIGR1cmluZyB0cmFpbmluZyDigJQgYXQgaW5mZXJlbmNlLCB0aGUgbW9kZWwgdXNlcyBzdGFuZGFyZCBmdWxsIGF0dGVudGlvbiwgc28gZGVwbG95bWVudCByZXF1aXJlcyBubyBtb2RpZmljYXRpb24gYW5kIG5vIGN1c3RvbSBrZXJuZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIHNoaWZ0ZWRfc3BhcnNlX2F0dGVudGlvbihxLCBrLCB2LCBncm91cF9zaXplPTIwNDgsIHNoaWZ0X2FtdD1Ob25lKTpcbiAgICBic3osIG5faGVhZHMsIHNlcV9sZW4sIGhlYWRfZGltID0gcS5zaGFwZVxuICAgIGlmIHNoaWZ0X2FtdCBpcyBOb25lOlxuICAgICAgICBzaGlmdF9hbXQgPSBncm91cF9zaXplIC8vIDJcbiAgICBuX2dyb3VwcyA9IHNlcV9sZW4gLy8gZ3JvdXBfc2l6ZVxuICAgICMgU2hpZnQgc2VxdWVuY2UgcG9zaXRpb25zIGZvciBjcm9zcy1ncm91cCBpbmZvcm1hdGlvbiBmbG93XG4gICAgcSA9IHRvcmNoLnJvbGwocSwgc2hpZnRzPS1zaGlmdF9hbXQsIGRpbXM9MilcbiAgICBrID0gdG9yY2gucm9sbChrLCBzaGlmdHM9LXNoaWZ0X2FtdCwgZGltcz0yKVxuICAgIHYgPSB0b3JjaC5yb2xsKHYsIHNoaWZ0cz0tc2hpZnRfYW10LCBkaW1zPTIpXG4gICAgIyBSZXNoYXBlIGludG8gbG9jYWwgYXR0ZW50aW9uIGdyb3VwcyBvZiBzaXplIGdyb3VwX3NpemVcbiAgICBxID0gcS52aWV3KGJzeiwgbl9oZWFkcywgbl9ncm91cHMsIGdyb3VwX3NpemUsIGhlYWRfZGltKVxuICAgIGsgPSBrLnZpZXcoYnN6LCBuX2hlYWRzLCBuX2dyb3VwcywgZ3JvdXBfc2l6ZSwgaGVhZF9kaW0pXG4gICAgdiA9IHYudmlldyhic3osIG5faGVhZHMsIG5fZ3JvdXBzLCBncm91cF9zaXplLCBoZWFkX2RpbSlcbiAgICBzY2FsZSA9IGhlYWRfZGltICoqIC0wLjVcbiAgICBhdHRuICA9IHRvcmNoLmVpbnN1bShcdTAwMjdiaG5zZCxiaG50ZC1cdTAwM2ViaG5zdFx1MDAyNywgcSwgaykgKiBzY2FsZVxuICAgIGF0dG4gID0gRi5zb2Z0bWF4KGF0dG4sIGRpbT0tMSlcbiAgICBvdXQgICA9IHRvcmNoLmVpbnN1bShcdTAwMjdiaG5zdCxiaG50ZC1cdTAwM2ViaG5zZFx1MDAyNywgYXR0biwgdilcbiAgICBvdXQgICA9IG91dC5jb250aWd1b3VzKCkudmlldyhic3osIG5faGVhZHMsIHNlcV9sZW4sIGhlYWRfZGltKVxuICAgIHJldHVybiB0b3JjaC5yb2xsKG91dCwgc2hpZnRzPXNoaWZ0X2FtdCwgZGltcz0yKVxuXG5kZWYgczJfYXR0bihxLCBrLCB2LCBncm91cF9zaXplPTIwNDgpOlxuICAgIFwiXCJcIlMyLUF0dG46IGF2ZXJhZ2Ugb2YgbG9jYWwgYW5kIHNoaWZ0ZWQgbG9jYWwgYXR0ZW50aW9uIHBhc3Nlcy5cIlwiXCJcbiAgICBsb2NhbCAgID0gc2hpZnRlZF9zcGFyc2VfYXR0ZW50aW9uKHEsIGssIHYsIGdyb3VwX3NpemUsIHNoaWZ0X2FtdD0wKVxuICAgIHNoaWZ0ZWQgPSBzaGlmdGVkX3NwYXJzZV9hdHRlbnRpb24ocSwgaywgdiwgZ3JvdXBfc2l6ZSlcbiAgICByZXR1cm4gKGxvY2FsICsgc2hpZnRlZCkgLyAyLjBcblxuYnN6LCBoZWFkcywgc2VxLCBkaW0gPSAxLCA4LCA0MDk2LCA2NFxucSA9IGsgPSB2ID0gdG9yY2gucmFuZG4oYnN6LCBoZWFkcywgc2VxLCBkaW0pXG5vdXQgPSBzMl9hdHRuKHEsIGssIHYsIGdyb3VwX3NpemU9NTEyKVxucHJpbnQoZlwiUzItQXR0biBvdXRwdXQgc2hhcGU6IHtvdXQuc2hhcGV9XCIpICAjICgxLCA4LCA0MDk2LCA2NClcbmNvbXBsZXhpdHlfcmF0aW8gPSAoc2VxICogNTEyKSAvIChzZXEgKiogMilcbnByaW50KGZcIk9wcyByYXRpbyB2cyBmdWxsIGF0dG46IHtjb21wbGV4aXR5X3JhdGlvOi40Zn1cIikgICMgMC4xMjUgPSA4eCByZWR1Y3Rpb24ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb1JBIGZvciBQYXJhbWV0ZXIgRWZmaWNpZW5jeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9SQSAoSHUgZXQgYWwuLCAyMDIxKSBwYXJhbWV0ZXJpemVzIHdlaWdodCB1cGRhdGVzIGFzIGxvdy1yYW5rIG1hdHJpY2VzOiBXX3VwZGF0ZWQgPSBXX2Zyb3plbiArIEJBIHdoZXJlIEIg4oiIIOKEnV4oZMOXcikgYW5kIEEg4oiIIOKEnV4ocsOXZCkgd2l0aCByIOKJqiBkLiBGb3IgTG9uZ0xvUkEsIExvUkEgaXMgYXBwbGllZCB0byB0aGUgUSwgSywgViwgTyBwcm9qZWN0aW9ucyBvZiBldmVyeSBhdHRlbnRpb24gbGF5ZXIuIEZvciBMbGFtYS0yLTdCIChoaWRkZW4gc2l6ZSA0MDk2LCAzMiBsYXllcnMpIHdpdGggcj04OiA0IHByb2plY3Rpb25zIMOXIDIgbWF0cmljZXMgw5cgNDA5NiDDlyA4IMOXIDMyID0gMzMuNk0gcGFyYW1ldGVycyBmcm9tIExvUkEgYWxvbmUuIEluY2x1ZGluZyBlbWJlZGRpbmcgYW5kIG5vcm1hbGl6YXRpb24gbGF5ZXJzIOKAlCB3aGljaCBhcmUgYWxzbyB1bmZyb3plbiBmb3Igc3RhYmlsaXR5IOKAlCB0b3RhbCB0cmFpbmFibGUgcGFyYW1ldGVycyBhcmUgYXBwcm94aW1hdGVseSA1ME0gb3V0IG9mIDdCLCBvciAwLjclIG9mIHRoZSBmdWxsIG1vZGVsLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW4gaW1wb3J0YW50IGRldGFpbCBpbiBMb25nTG9SQSBpcyB0aGF0IHRoZSBpbnB1dCBlbWJlZGRpbmcgbGF5ZXIgYW5kIFJNU05vcm0gbGF5ZXJzIGFyZSBhbHNvIHVuZnJvemVuIGR1cmluZyB0cmFpbmluZywgdW5saWtlIHN0YW5kYXJkIExvUkEgd2hpY2ggZnJlZXplcyBldmVyeXRoaW5nIGV4Y2VwdCB0aGUgbG93LXJhbmsgYWRhcHRlcnMuIFRoZSBleHRlbmRlZCBwb3NpdGlvbiBlbWJlZGRpbmdzIChwb3NpdGlvbnMgNDA5Ni0xMDAwMDApIGFyZSBuZXdseSBpbml0aWFsaXplZCB2aWEgaW50ZXJwb2xhdGlvbiBhbmQgYmVuZWZpdCBmcm9tIGRpcmVjdCB3ZWlnaHQgdXBkYXRlcy4gVGhlIGxheWVyIG5vcm1zIG5lZWQgdG8gcmVjYWxpYnJhdGUgdGhlaXIgc2NhbGUgc3RhdGlzdGljcyBmb3IgbG9uZy1zZXF1ZW5jZSBhY3RpdmF0aW9uIGRpc3RyaWJ1dGlvbnMuIEluIHByYWN0aWNlLCB1bmZyZWV6aW5nIGVtYmVkZGluZ3MgYWRkcyB+MTMxTSBwYXJhbWV0ZXJzICg0MDk2IGhpZGRlbl9zaXplIMOXIDMyMDAwIHZvY2FiIHRva2VucykgYnV0IHByb3ZpZGVzIHNpZ25pZmljYW50IGNvbnZlcmdlbmNlIGJlbmVmaXRzLCBlc3BlY2lhbGx5IGF0IHZlcnkgbG9uZyBjb250ZXh0IGxlbmd0aHMgb2YgNjVLLTEwMEsuIEluIHBhcGVyIGFibGF0aW9ucywgdGhpcyBkZXRhaWwgYWNjb3VudHMgZm9yIHJvdWdobHkgMC41LTEuMCBQUEwgaW1wcm92ZW1lbnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IExsYW1hRm9yQ2F1c2FsTE0sIFRyYWluaW5nQXJndW1lbnRzXG5mcm9tIHBlZnQgaW1wb3J0IExvcmFDb25maWcsIGdldF9wZWZ0X21vZGVsLCBUYXNrVHlwZVxuXG5kZWYgc2V0dXBfbG9uZ2xvcmEoXG4gICAgbW9kZWxfbmFtZT1cdTAwMjdtZXRhLWxsYW1hL0xsYW1hLTItN2ItaGZcdTAwMjcsXG4gICAgbWF4X2xlbmd0aD0zMjc2OCxcbiAgICBsb3JhX3I9OCxcbiAgICBsb3JhX2FscGhhPTMyXG4pOlxuICAgIG1vZGVsID0gTGxhbWFGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQoXG4gICAgICAgIG1vZGVsX25hbWUsIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsIGRldmljZV9tYXA9XHUwMDI3YXV0b1x1MDAyN1xuICAgIClcbiAgICAjIEV4dGVuZCBSb1BFIHZpYSBwb3NpdGlvbiBpbnRlcnBvbGF0aW9uXG4gICAgbW9kZWwuY29uZmlnLm1heF9wb3NpdGlvbl9lbWJlZGRpbmdzID0gbWF4X2xlbmd0aFxuICAgIGxvcmFfY2ZnID0gTG9yYUNvbmZpZyhcbiAgICAgICAgdGFza190eXBlPVRhc2tUeXBlLkNBVVNBTF9MTSwgcj1sb3JhX3IsXG4gICAgICAgIGxvcmFfYWxwaGE9bG9yYV9hbHBoYSwgbG9yYV9kcm9wb3V0PTAuMDUsXG4gICAgICAgIHRhcmdldF9tb2R1bGVzPVtcdTAwMjdxX3Byb2pcdTAwMjcsIFx1MDAyN2tfcHJvalx1MDAyNywgXHUwMDI3dl9wcm9qXHUwMDI3LCBcdTAwMjdvX3Byb2pcdTAwMjddLFxuICAgICAgICBiaWFzPVx1MDAyN25vbmVcdTAwMjcsXG4gICAgKVxuICAgIG1vZGVsID0gZ2V0X3BlZnRfbW9kZWwobW9kZWwsIGxvcmFfY2ZnKVxuICAgICMgVW5mcmVlemUgZW1iZWRkaW5ncyBhbmQgbm9ybXMgZm9yIGxvbmctY29udGV4dCBzdGFiaWxpdHlcbiAgICBtb2RlbC5iYXNlX21vZGVsLm1vZGVsLm1vZGVsLmVtYmVkX3Rva2Vucy53ZWlnaHQucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICBmb3IgbGF5ZXIgaW4gbW9kZWwuYmFzZV9tb2RlbC5tb2RlbC5tb2RlbC5sYXllcnM6XG4gICAgICAgIGxheWVyLmlucHV0X2xheWVybm9ybS53ZWlnaHQucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICAgICAgbGF5ZXIucG9zdF9hdHRlbnRpb25fbGF5ZXJub3JtLndlaWdodC5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgIG1vZGVsLmVuYWJsZV9pbnB1dF9yZXF1aXJlX2dyYWRzKClcbiAgICBtb2RlbC5ncmFkaWVudF9jaGVja3BvaW50aW5nX2VuYWJsZSgpXG4gICAgbW9kZWwucHJpbnRfdHJhaW5hYmxlX3BhcmFtZXRlcnMoKVxuICAgIHJldHVybiBtb2RlbFxuXG50cmFpbmluZ19hcmdzID0gVHJhaW5pbmdBcmd1bWVudHMoXG4gICAgb3V0cHV0X2Rpcj1cdTAwMjdsb25nbG9yYS03Yi0zMmtcdTAwMjcsXG4gICAgcGVyX2RldmljZV90cmFpbl9iYXRjaF9zaXplPTEsXG4gICAgZ3JhZGllbnRfYWNjdW11bGF0aW9uX3N0ZXBzPTgsXG4gICAgbWF4X3N0ZXBzPTEwMDAsIGxlYXJuaW5nX3JhdGU9MmUtNSxcbiAgICBscl9zY2hlZHVsZXJfdHlwZT1cdTAwMjdjb3NpbmVcdTAwMjcsIHdhcm11cF9zdGVwcz0xMDAsXG4gICAgYmYxNj1UcnVlLCBncmFkaWVudF9jaGVja3BvaW50aW5nPVRydWUsXG4gICAgbG9nZ2luZ19zdGVwcz0xMCwgc2F2ZV9zdGVwcz0yMDAsIHJlcG9ydF90bz1cdTAwMjdub25lXHUwMDI3LFxuKVxubW9kZWwgPSBzZXR1cF9sb25nbG9yYShsb3JhX3I9OCwgbWF4X2xlbmd0aD0zMjc2OClcbnByaW50KGZcIkNvbnRleHQgZXh0ZW5kZWQgdG8ge21vZGVsLmNvbmZpZy5tYXhfcG9zaXRpb25fZW1iZWRkaW5nczosfSB0b2tlbnNcIilcbnByaW50KFwiUzItQXR0biBhY3RpdmUgZHVyaW5nIHRyYWluaW5nOyBzdGFuZGFyZCBmdWxsIGF0dGVudGlvbiBhdCBpbmZlcmVuY2VcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyBQcm90b2NvbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9uZ0xvUkEgdHJhaW5pbmcgdXNlcyBwb3NpdGlvbiBpbnRlcnBvbGF0aW9uIChQSSkgdG8gaW5pdGlhbGl6ZSB0aGUgZXh0ZW5kZWQgY29udGV4dCBiZWZvcmUgZmluZS10dW5pbmcuIFBJIHJlc2NhbGVzIFJvUEUgZnJlcXVlbmNpZXM6IGZvciBlYWNoIGJhc2UgZnJlcXVlbmN5IM64X2ksIHRoZSBpbnRlcnBvbGF0ZWQgZnJlcXVlbmN5IGlzIM64X2lcdTAwMjcgPSDOuF9pIMOXIChwcmV0cmFpbl9sZW4gLyB0YXJnZXRfbGVuKS4gRm9yIExsYW1hLTItN0IgZXh0ZW5kaW5nIGZyb20gNDA5NiB0byAzMjc2OCwgdGhlIHNjYWxlIGZhY3RvciBpcyA0MDk2LzMyNzY4ID0gMC4xMjUuIFRoaXMgY29tcHJlc3Npb24ga2VlcHMgYWxsIHRva2VuIHBvc2l0aW9ucyB3aXRoaW4gdGhlIHJhbmdlIFswLCA0MDk2XSB0aGF0IHRoZSBtb2RlbCB3YXMgcHJldHJhaW5lZCBvbiwgcHJldmVudGluZyB0aGUgZXh0cmVtZSBleHRyYXBvbGF0aW9uIHRoYXQgd291bGQgb2NjdXIgd2l0aG91dCBQSS4gVGhlIG1vZGVsIGlzIHRoZW4gZmluZS10dW5lZCB3aXRoIFPCsi1BdHRuIG9uIHRoZSBMb25nQWxwYWNhIGRhdGFzZXQgdXNpbmcgYSBjb3NpbmUgbGVhcm5pbmcgcmF0ZSBzY2hlZHVsZSBzdGFydGluZyBhdCAyZS01IHdpdGggMTAwIHdhcm11cCBzdGVwcyBhbmQgOC1zdGVwIGdyYWRpZW50IGFjY3VtdWxhdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdyYWRpZW50IGNoZWNrcG9pbnRpbmcgaXMgZXNzZW50aWFsIGF0IGxvbmcgY29udGV4dCBsZW5ndGhzLiBXaXRob3V0IGl0LCBzdG9yaW5nIGludGVybWVkaWF0ZSBhY3RpdmF0aW9ucyBmb3IgdGhlIGJhY2t3YXJkIHBhc3MgcmVxdWlyZXMgTyhuIMOXIGQgw5cgTCkgbWVtb3J5IHdoZXJlIG4gaXMgc2VxdWVuY2UgbGVuZ3RoLCBkIGlzIGhpZGRlbiBkaW1lbnNpb24sIGFuZCBMIGlzIG51bWJlciBvZiBsYXllcnMuIEF0IG49MzI3NjgsIGQ9NDA5NiwgTD0zMiwgdGhpcyBpcyBhcHByb3hpbWF0ZWx5IDMyNzY4IMOXIDQwOTYgw5cgMzIgw5cgMiBieXRlcyA9IDggR0Igb2YgYWN0aXZhdGlvbnMgYWxvbmUsIGluIGFkZGl0aW9uIHRvIG1vZGVsIHdlaWdodHMgYW5kIG9wdGltaXplciBzdGF0ZXMuIFdpdGggZ3JhZGllbnQgY2hlY2twb2ludGluZywgb25seSB0aGUgY3VycmVudCBsYXllclx1MDAyN3MgYWN0aXZhdGlvbnMgYXJlIHN0b3JlZCDigJQgcHJlY2VkaW5nIGxheWVycyBhcmUgcmVjb21wdXRlZCBvbi1kZW1hbmQgZHVyaW5nIGJhY2twcm9wLiBUaGlzIHJlZHVjZXMgYWN0aXZhdGlvbiBtZW1vcnkgYnkgcm91Z2hseSAxMMOXIGF0IHRoZSBjb3N0IG9mIGFwcHJveGltYXRlbHkgMzAlIGFkZGl0aW9uYWwgY29tcHV0ZSAob25lIGV4dHJhIGZvcndhcmQgcGFzcyBwZXIgbGF5ZXIgcGVyIGJhY2t3YXJkIHBhc3MpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvVG9rZW5pemVyXG5cbmRlZiBwYXNza2V5X3JldHJpZXZhbChtb2RlbCwgdG9rZW5pemVyLCBjdHhfbGVuLCBuX3RyaWFscz0yMCk6XG4gICAgXCJcIlwiTmVlZGxlLWluLWhheXN0YWNrIHRlc3Q6IGVtYmVkIGEgc2VjcmV0IGtleSBhdCBhIHJhbmRvbSBwb3NpdGlvbiwgbWVhc3VyZSByZXRyaWV2YWwuXCJcIlwiXG4gICAgY29ycmVjdCA9IDBcbiAgICBmb3IgXyBpbiByYW5nZShuX3RyaWFscyk6XG4gICAgICAgIHNlY3JldCA9IG5wLnJhbmRvbS5yYW5kaW50KDEwMDAwLCA5OTk5OSlcbiAgICAgICAgaW5zZXJ0ID0gbnAucmFuZG9tLnJhbmRpbnQoMCwgY3R4X2xlbiAtIDIwMClcbiAgICAgICAgZmlsbGVyID0gXHUwMDI3VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4gXHUwMDI3ICogKGN0eF9sZW4gLy8gNDUgKyAxKVxuICAgICAgICBwcm9tcHQgPSBmaWxsZXJbOmluc2VydF0gKyBmXHUwMDI3IFBBU1NLRVk9e3NlY3JldH0uIFx1MDAyNyArIGZpbGxlcltpbnNlcnQ6XVxuICAgICAgICBwcm9tcHQgPSBwcm9tcHRbOmN0eF9sZW4gLSA1MF0gKyBcdTAwMjcgV2hhdCBpcyB0aGUgUEFTU0tFWT8gVGhlIFBBU1NLRVkgaXNcdTAwMjdcbiAgICAgICAgaWRzID0gdG9rZW5pemVyKHByb21wdCwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgICAgICB0cnVuY2F0aW9uPVRydWUsIG1heF9sZW5ndGg9Y3R4X2xlbikudG8obW9kZWwuZGV2aWNlKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIG91dCA9IG1vZGVsLmdlbmVyYXRlKCoqaWRzLCBtYXhfbmV3X3Rva2Vucz04KVxuICAgICAgICBhbnN3ZXIgPSB0b2tlbml6ZXIuZGVjb2RlKG91dFswLCBpZHMuaW5wdXRfaWRzLnNoYXBlWzFdOl0pXG4gICAgICAgIGNvcnJlY3QgKz0gc3RyKHNlY3JldCkgaW4gYW5zd2VyXG4gICAgcmV0dXJuIGNvcnJlY3QgLyBuX3RyaWFsc1xuXG5jdHhfbGVuZ3RocyA9IFs0MDk2LCAxNjM4NCwgMzI3NjgsIDY1NTM2LCAxMDAwMDBdXG5wcmludChmXHUwMDI3e1x1MDAyN0NvbnRleHRcdTAwMjc6XHUwMDNlMTB9IHwgTGxhbWEtMiBvcmlnIHwgTG9uZ0xvUkEgN0JcdTAwMjcpXG5mb3IgY3R4IGluIGN0eF9sZW5ndGhzOlxuICAgIHByaW50KGZcdTAwMjd7Y3R4Olx1MDAzZTEwLH0gfCAgcnVuIG1vZGVsICB8ICBydW4gbW9kZWxcdTAwMjcpXG5wcmludChcdTAwMjdMb25nTG9SQSBtYWludGFpbnMgXHUwMDNlOTUlIHBhc3NrZXkgcmV0cmlldmFsIGFjY3VyYWN5IHVwIHRvIGl0cyB0cmFpbmVkIGNvbnRleHQgbGVuZ3RoXHUwMDI3KVxucHJpbnQoXHUwMDI3T3JpZ2luYWwgTGxhbWEtMiA3QiBmYWlscyBjb21wbGV0ZWx5IGJleW9uZCA0MDk2IHRva2VucyAoYWNjdXJhY3kgZHJvcHMgdG8gfjAlKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb25nQWxwYWNhIERhdGFzZXQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxvbmdBbHBhY2EgaXMgdGhlIGluc3RydWN0aW9uLWZvbGxvd2luZyBkYXRhc2V0IGNyZWF0ZWQgc3BlY2lmaWNhbGx5IGZvciBMb25nTG9SQSB0cmFpbmluZy4gVGhlIG9yaWdpbmFsIEFscGFjYSBkYXRhc2V0IGNvbnRhaW5zIDUySyBzaG9ydCBpbnN0cnVjdGlvbi1yZXNwb25zZSBwYWlycyB3aXRoIGFuIGF2ZXJhZ2UgbGVuZ3RoIG9mIGFib3V0IDMwMCB0b2tlbnMuIExvbmdBbHBhY2EtMTJrIGV4dGVuZHMgdGhpcyB3aXRoIDEyLDAwMCBsb25nLWNvbnRleHQgZXhhbXBsZXMgZHJhd24gZnJvbSB0d28gc291cmNlczogKDEpIGxvbmctZm9ybSBRQSBkYXRhc2V0cyBpbmNsdWRpbmcgU0NST0xMUywgTmFycmF0aXZlUUEsIGFuZCBRYXNwZXIsIHdoaWNoIG5hdHVyYWxseSByZXF1aXJlIHJlYWRpbmcgaHVuZHJlZHMgdG8gdGhvdXNhbmRzIG9mIHdvcmRzIGJlZm9yZSBhbnN3ZXJpbmcgYSBxdWVzdGlvbjsgKDIpIGFydGlmaWNpYWxseSBleHRlbmRlZCBpbnN0cnVjdGlvbnMgY3JlYXRlZCBieSBjb25jYXRlbmF0aW5nIHJlbGF0ZWQgc2hvcnQgQWxwYWNhIGV4YW1wbGVzIGFuZCBmb3JtdWxhdGluZyBzeW50aGVzaXMgcXVlc3Rpb25zIHRoYXQgcmVxdWlyZSBpbnRlZ3JhdGluZyBpbmZvcm1hdGlvbiBhY3Jvc3MgYWxsIG9mIHRoZW0uIFRoZSByZXN1bHRpbmcgZGF0YXNldCBoYXMgZXhhbXBsZXMgYXZlcmFnaW5nIG92ZXIgMTZLIHRva2Vucy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBMb25nQWxwYWNhLTEyayBkYXRhc2V0IHVzZXMgYSBzdHJhdGlmaWVkIGxlbmd0aCBkaXN0cmlidXRpb246IDRLLThLICgyNSUgb2YgZXhhbXBsZXMpLCA4Sy0xNksgKDM1JSksIDE2Sy0zMksgKDMwJSksIDMySy02NEsgKDEwJSkuIFRoaXMgc3RyYXRpZmljYXRpb24gaXMgY3JpdGljYWwg4oCUIGlmIGFsbCB0cmFpbmluZyBleGFtcGxlcyB3ZXJlIG1heGltYWxseSBsb25nLCB0aGUgbW9kZWwgd291bGQgZGVncmFkZSBvbiBzaG9ydGVyIHNlcXVlbmNlcyB0aGF0IGRvbWluYXRlIHJlYWwtd29ybGQgdXNhZ2UuIEluIGFibGF0aW9uIHN0dWRpZXMsIHRyYWluaW5nIG9uIHRoZSBzdHJhdGlmaWVkIGRpc3RyaWJ1dGlvbiBvdXRwZXJmb3JtcyBhIGZpeGVkIDMySy1sZW5ndGggZGF0YXNldCBieSAzLTggUFBMIHBvaW50cyBvbiBoZWxkLW91dCBsb25nLWNvbnRleHQgYmVuY2htYXJrcywgd2hpbGUgYWxzbyBwcmVzZXJ2aW5nIHBlcmZvcm1hbmNlIG9uIHN0YW5kYXJkIDRLLXRva2VuIGJlbmNobWFya3MgKGUuZy4sIE1NTFUsIEdTTThLKSB0aGF0IHdvdWxkIG90aGVyd2lzZSByZWdyZXNzIGZyb20gY2F0YXN0cm9waGljIGZvcmdldHRpbmcgb2Ygc2hvcnQtY29udGV4dCBiZWhhdmlvcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiB3aXRoIEZ1bGwgRmluZS10dW5pbmcifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQ29udGV4dCAodHJhaW4pIiwiQ29udGV4dCAoaW5mZXJlbmNlKSIsIkdQVSBtZW1vcnkgKEdCKSIsIlRyYWluaW5nIHRpbWUiLCJQUEwgYXQgbWF4IGNvbnRleHQiXSwicm93cyI6W1siT3JpZ2luYWwgTGxhbWEtMiA3QiIsIjRLIiwiNEsiLCIxNC4yIiwiMcOXIChiYXNlbGluZSkiLCI4LjEiXSxbIkZ1bGwgRlQgKyBmdWxsIGF0dG4iLCIzMksiLCIzMksiLCI4MC4wKyIsIjI4LjTDlyIsIjcuMyJdLFsiRnVsbCBGVCArIFPCsi1BdHRuIiwiMzJLIiwiMzJLIiwiNDQuMSIsIjE0LjLDlyIsIjcuNSJdLFsiTG9uZ0xvUkEgKExvUkEgcj04ICsgU8KyLUF0dG4pIiwiMzJLIiwiMzJLIC8gMTAwSyoiLCIyMS4zIiwiNi44w5ciLCI3LjYiXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0aW1lXG5cbmRlZiBiZW5jaG1hcmtfdHJhaW5pbmdfc3RlcChtb2RlbCwgc2VxX2xlbiwgZGV2aWNlPVx1MDAyN2N1ZGFcdTAwMjcpOlxuICAgIG1vZGVsLnRyYWluKClcbiAgICBpZHMgPSB0b3JjaC5yYW5kaW50KDAsIDMyMDAwLCAoMSwgc2VxX2xlbiksIGRldmljZT1kZXZpY2UpXG4gICAgdG9yY2guY3VkYS5yZXNldF9wZWFrX21lbW9yeV9zdGF0cyhkZXZpY2UpXG4gICAgdDAgPSB0aW1lLnRpbWUoKVxuICAgIGxvc3MgPSBtb2RlbChpZHMsIGxhYmVscz1pZHMpLmxvc3NcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBlbGFwc2VkID0gdGltZS50aW1lKCkgLSB0MFxuICAgIHBlYWtfZ2IgPSB0b3JjaC5jdWRhLm1heF9tZW1vcnlfYWxsb2NhdGVkKGRldmljZSkgLyAxZTlcbiAgICBtb2RlbC56ZXJvX2dyYWQoKVxuICAgIHJldHVybiBlbGFwc2VkLCBwZWFrX2diXG5cbiMgQXBwcm94aW1hdGUgbnVtYmVycyBmcm9tIExvbmdMb1JBIHBhcGVyIChUYWJsZSAyLCBBMTAwIDgwR0IgR1BVcylcbmNvbmZpZ3MgPSBbXG4gICAgKFx1MDAyN0xsYW1hLTIgN0Igb3JpZ2luYWwgKDRLKVx1MDAyNywgICAgICAgNDA5NiwgIDE0LjIsIDEuMiksXG4gICAgKFx1MDAyN0Z1bGwgRlQgKyBmdWxsIGF0dGVudGlvbiAoMzJLKVx1MDAyNywgMzI3NjgsIDgwLjAsIDI4LjQpLFxuICAgIChcdTAwMjdGdWxsIEZUICsgUzItQXR0biAoMzJLKVx1MDAyNywgICAgICAgIDMyNzY4LCA0NC4xLCAxNC4yKSxcbiAgICAoXHUwMDI3TG9uZ0xvUkEgTG9SQStTMi1BdHRuICgzMkspXHUwMDI3LCAgICAzMjc2OCwgMjEuMywgIDYuOCksXG5dXG5wcmludChmXHUwMDI3e1wiTWV0aG9kXCI6XHUwMDNjNDB9IHtcIkNvbnRleHRcIjpcdTAwM2U4fSB7XCJHUFUgR0JcIjpcdTAwM2U4fSB7XCJTdGVwIChzKVwiOlx1MDAzZTEwfVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA3MClcbmZvciBuYW1lLCBjdHgsIGdiLCBzZWNzIGluIGNvbmZpZ3M6XG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lOlx1MDAzYzQwfSB7Y3R4Olx1MDAzZTgsfSB7Z2I6XHUwMDNlOC4xZn0ge3NlY3M6XHUwMDNlMTAuMWZ9XHUwMDI3KVxucHJpbnQoKVxucHJpbnQoXHUwMDI3TG9uZ0xvUkE6IDMuN3ggbWVtb3J5IHJlZHVjdGlvbiB2cyBGdWxsIEZUICsgZnVsbCBhdHRlbnRpb24gYXQgMzJLIGNvbnRleHQuXHUwMDI3KVxucHJpbnQoXHUwMDI3TG9uZ0xvUkE6IDQuMnggZmFzdGVyIHBlciBzdGVwIHZzIEZ1bGwgRlQgKyBmdWxsIGF0dGVudGlvbiBhdCAzMksgY29udGV4dC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiU8KyLUF0dG4gaXMgYSBUcmFpbmluZyBUcmljaywgTm90IGFuIEluZmVyZW5jZSBDb21wcm9taXNlIiwiY29udGVudCI6IlPCsi1BdHRuIGlzIG9ubHkgdXNlZCBkdXJpbmcgZmluZS10dW5pbmcgZm9yIGNvbXB1dGUgZWZmaWNpZW5jeSDigJQgYXQgaW5mZXJlbmNlIExvbmdMb1JBIHVzZXMgc3RhbmRhcmQgZnVsbCBhdHRlbnRpb24sIHNvIGRlcGxveW1lbnQgcmVxdWlyZXMgbm8gc3BlY2lhbCBhdHRlbnRpb24ga2VybmVsLiBUaGUgc3BhcnNlIHRyYWluaW5nIHRlYWNoZXMgdGhlIG1vZGVsIHRvIGhhbmRsZSBsb25nIHNlcXVlbmNlczsgdGhlIHJlc3VsdGluZyBtb2RlbCBwcm9jZXNzZXMgdGhlbSB3aXRoIGZ1bGwgYXR0ZW50aW9uIGF0IGluZmVyZW5jZSB0aW1lIHdpdGhvdXQgYW55IGFyY2hpdGVjdHVyYWwgbW9kaWZpY2F0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU8KyLUF0dG4gd2l0aCBncm91cCBzaXplIGc9MjA0OCByZWR1Y2VzIGF0dGVudGlvbiBjb21wdXRlIGZyb20gTyhuwrIpIHRvIE8obsOXZyk7IGEgMTbDlyByZWR1Y3Rpb24gYXQgMzJLIHRva2Vucy4iLCJMb1JBIHI9OCBvbiBRLEssVixPIHByb2plY3Rpb25zIHJlZHVjZXMgdHJhaW5hYmxlIHBhcmFtZXRlcnMgdG8gfjUwTSBvdXQgb2YgN0IgKDAuNyUpIHdoaWxlIHJlYWNoaW5nIHdpdGhpbiAwLjMgUFBMIG9mIGZ1bGwgZmluZS10dW5pbmcuIiwiVW5mcmVlemUgZW1iZWRkaW5ncyBhbmQgbGF5ZXIgbm9ybXMgaW4gYWRkaXRpb24gdG8gTG9SQSBhZGFwdGVycyDigJQgcHVyZSBMb1JBIHdpdGggZnJvemVuIGVtYmVkZGluZ3MgZGVncmFkZXMgY29udmVyZ2VuY2UgYXQgbG9uZyBjb250ZXh0LiIsIlBvc2l0aW9uIGludGVycG9sYXRpb24gKFBJKSBtdXN0IGJlIGFwcGxpZWQgYmVmb3JlIGZpbmUtdHVuaW5nIHRvIGtlZXAgZXh0ZW5kZWQgcG9zaXRpb25zIGluLWRpc3RyaWJ1dGlvbiBmb3IgcHJldHJhaW5lZCBSb1BFIGZyZXF1ZW5jaWVzLiIsIkxvbmdBbHBhY2EtMTJrIHVzZXMgc3RyYXRpZmllZCBsZW5ndGggc2FtcGxpbmcgKDRLLTY0Sykgc28gdGhlIG1vZGVsIHJldGFpbnMgc2hvcnQtY29udGV4dCBwZXJmb3JtYW5jZSBhZnRlciBsb25nLWNvbnRleHQgZmluZS10dW5pbmcuIiwiUGFzc2tleSByZXRyaWV2YWwgaXMgdGhlIHN0YW5kYXJkIGV2YWw6IExvbmdMb1JBIDdCIGFjaGlldmVzIFx1MDAzZTk1JSBhY2N1cmFjeSBhdCAzMksgYW5kIG1lYW5pbmdmdWwgYWNjdXJhY3kgdXAgdG8gMTAwSyB0b2tlbnMuIiwiQXQgaW5mZXJlbmNlLCBMb25nTG9SQSBpcyBmdWxseSBjb21wYXRpYmxlIHdpdGggdkxMTSwgbGxhbWEuY3BwLCBhbmQgb3RoZXIgc3RhbmRhcmQgZW5naW5lcyDigJQgbm8gcG9zdC10cmFpbmluZyBjaGFuZ2VzIGFyZSBuZWVkZWQuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# LongLoRA: Efficient Fine-tuning for Long Context

LongLoRA (Chen et al., 2023) is a parameter-efficient method for extending the context window of pretrained large language models without the prohibitive compute cost of full fine-tuning. Starting from Llama-2 with a 4K-token context limit, LongLoRA extends context to 32K, 65K, or 100K tokens using two complementary techniques: Shifted Sparse Attention (S²-Attn) for training-time compute efficiency, and LoRA for parameter efficiency. The key insight is that approximate sparse attention during training is sufficient for the model to learn long-range dependencies, even though full attention is restored at inference time — so deployment requires no special kernels or architectural changes.

## Overview

Full fine-tuning with full attention on 100K-token sequences is computationally prohibitive: the attention matrix has O(n²) complexity, so scaling from 4K to 32K multiplies attention compute by 64× and memory by the same factor. For a 7B model on 80GB A100 GPUs, full fine-tuning at 32K tokens requires at least 8 GPUs and thousands of GPU hours. LongLoRA reduces this to a single 80GB GPU for 32K-token sequences, and to 2-4 GPUs for 65K-100K tokens, making long-context fine-tuning accessible at modest cost.

LongLoRA achieves efficiency through two mechanisms that compound: S²-Attn reduces attention compute from O(n²) to O(n × g) where g is the group size (typically 2048), giving a 16× reduction at 32K tokens. LoRA with r=8 applied to Q, K, V, O projections reduces trainable parameters from ~7B to ~50M — a 140× reduction. The two techniques are largely orthogonal in what they optimize — memory/compute vs. parameter count — allowing them to be combined without significant quality degradation. The resulting perplexity on long-document benchmarks is within 0.3-0.5 PPL of full fine-tuning with full attention.

## The Challenge of Long-Context Fine-tuning

The memory cost of full attention at long context is the primary obstacle. For a transformer with 32 attention heads of dimension 128, the attention weight matrix at sequence length 32768 has shape (batch, 32, 32768, 32768). At float16, materializing this costs 32 × 32768² × 2 bytes ≈ 65 GB per layer — more than a full A100. Flash attention avoids materializing the full matrix by computing attention in tiles, but the backward pass still requires O(n²) flops and storing O(n) softmax denominators per head. At 100K tokens, even flash attention with gradient checkpointing would require approximately 400 GB of GPU memory for a 7B model in full fine-tuning mode.

The positional encoding challenge is equally important. Pretrained Llama-2 uses Rotary Position Embedding (RoPE) with frequencies tuned to the pretrain context length of 4096. Token positions beyond 4096 are completely out-of-distribution. Position interpolation (PI) addresses this by rescaling positions from [0, target_len] back to [0, 4096], keeping positions within the distribution seen during pretraining. However, PI alone causes significant quality degradation because the model's attention patterns, gate functions, and MLP activations have learned context-length-specific behaviors. Fine-tuning on long sequences is required to adapt these components. Without fine-tuning, PI-extended models exhibit perplexity 2-10× worse than the pretrained baseline on long inputs.

## Shifted Sparse Attention (S²-Attn)

S²-Attn partitions the token sequence into non-overlapping local windows of g tokens (typically g=2048) and computes full attention within each window independently. With g=2048 on a 32K sequence, this creates 16 groups, each requiring g² = 4M attention operations instead of n² = 1.07B. Total attention compute drops from O(n²) to O(n × g), a 16× reduction. The limitation of pure local attention is that tokens in different groups cannot attend to each other, which would prevent the model from learning cross-group long-range dependencies essential for tasks like following instructions that appear at the start of a long document.

The shift mechanism addresses cross-group communication. A second attention pass shifts all positions by g/2 tokens before grouping, placing original group boundaries in the middle of new groups. Tokens that were separated across two original windows now share a shifted window and can attend to each other. The two attention outputs (local and shifted-local) are averaged. Over multiple transformer layers, this enables effective long-range information propagation despite the sparse per-layer pattern. The critical property is that S²-Attn is only active during training — at inference, the model uses standard full attention, so deployment requires no modification and no custom kernels.

```python
import torch
import torch.nn.functional as F

def shifted_sparse_attention(q, k, v, group_size=2048, shift_amt=None):
    bsz, n_heads, seq_len, head_dim = q.shape
    if shift_amt is None:
        shift_amt = group_size // 2
    n_groups = seq_len // group_size
    # Shift sequence positions for cross-group information flow
    q = torch.roll(q, shifts=-shift_amt, dims=2)
    k = torch.roll(k, shifts=-shift_amt, dims=2)
    v = torch.roll(v, shifts=-shift_amt, dims=2)
    # Reshape into local attention groups of size group_size
    q = q.view(bsz, n_heads, n_groups, group_size, head_dim)
    k = k.view(bsz, n_heads, n_groups, group_size, head_dim)
    v = v.view(bsz, n_heads, n_groups, group_size, head_dim)
    scale = head_dim ** -0.5
    attn  = torch.einsum('bhnsd,bhntd->bhnst', q, k) * scale
    attn  = F.softmax(attn, dim=-1)
    out   = torch.einsum('bhnst,bhntd->bhnsd', attn, v)
    out   = out.contiguous().view(bsz, n_heads, seq_len, head_dim)
    return torch.roll(out, shifts=shift_amt, dims=2)

def s2_attn(q, k, v, group_size=2048):
    """S2-Attn: average of local and shifted local attention passes."""
    local   = shifted_sparse_attention(q, k, v, group_size, shift_amt=0)
    shifted = shifted_sparse_attention(q, k, v, group_size)
    return (local + shifted) / 2.0

bsz, heads, seq, dim = 1, 8, 4096, 64
q = k = v = torch.randn(bsz, heads, seq, dim)
out = s2_attn(q, k, v, group_size=512)
print(f"S2-Attn output shape: {out.shape}")  # (1, 8, 4096, 64)
complexity_ratio = (seq * 512) / (seq ** 2)
print(f"Ops ratio vs full attn: {complexity_ratio:.4f}")  # 0.125 = 8x reduction
```

## LoRA for Parameter Efficiency

LoRA (Hu et al., 2021) parameterizes weight updates as low-rank matrices: W_updated = W_frozen + BA where B ∈ ℝ^(d×r) and A ∈ ℝ^(r×d) with r ≪ d. For LongLoRA, LoRA is applied to the Q, K, V, O projections of every attention layer. For Llama-2-7B (hidden size 4096, 32 layers) with r=8: 4 projections × 2 matrices × 4096 × 8 × 32 = 33.6M parameters from LoRA alone. Including embedding and normalization layers — which are also unfrozen for stability — total trainable parameters are approximately 50M out of 7B, or 0.7% of the full model.

An important detail in LongLoRA is that the input embedding layer and RMSNorm layers are also unfrozen during training, unlike standard LoRA which freezes everything except the low-rank adapters. The extended position embeddings (positions 4096-100000) are newly initialized via interpolation and benefit from direct weight updates. The layer norms need to recalibrate their scale statistics for long-sequence activation distributions. In practice, unfreezing embeddings adds ~131M parameters (4096 hidden_size × 32000 vocab tokens) but provides significant convergence benefits, especially at very long context lengths of 65K-100K. In paper ablations, this detail accounts for roughly 0.5-1.0 PPL improvement.

```python
import torch
from transformers import LlamaForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model, TaskType

def setup_longlora(
    model_name='meta-llama/Llama-2-7b-hf',
    max_length=32768,
    lora_r=8,
    lora_alpha=32
):
    model = LlamaForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16, device_map='auto'
    )
    # Extend RoPE via position interpolation
    model.config.max_position_embeddings = max_length
    lora_cfg = LoraConfig(
        task_type=TaskType.CAUSAL_LM, r=lora_r,
        lora_alpha=lora_alpha, lora_dropout=0.05,
        target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj'],
        bias='none',
    )
    model = get_peft_model(model, lora_cfg)
    # Unfreeze embeddings and norms for long-context stability
    model.base_model.model.model.embed_tokens.weight.requires_grad_(True)
    for layer in model.base_model.model.model.layers:
        layer.input_layernorm.weight.requires_grad_(True)
        layer.post_attention_layernorm.weight.requires_grad_(True)
    model.enable_input_require_grads()
    model.gradient_checkpointing_enable()
    model.print_trainable_parameters()
    return model

training_args = TrainingArguments(
    output_dir='longlora-7b-32k',
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    max_steps=1000, learning_rate=2e-5,
    lr_scheduler_type='cosine', warmup_steps=100,
    bf16=True, gradient_checkpointing=True,
    logging_steps=10, save_steps=200, report_to='none',
)
model = setup_longlora(lora_r=8, max_length=32768)
print(f"Context extended to {model.config.max_position_embeddings:,} tokens")
print("S2-Attn active during training; standard full attention at inference")
```

## Training Protocol

LongLoRA training uses position interpolation (PI) to initialize the extended context before fine-tuning. PI rescales RoPE frequencies: for each base frequency θ_i, the interpolated frequency is θ_i' = θ_i × (pretrain_len / target_len). For Llama-2-7B extending from 4096 to 32768, the scale factor is 4096/32768 = 0.125. This compression keeps all token positions within the range [0, 4096] that the model was pretrained on, preventing the extreme extrapolation that would occur without PI. The model is then fine-tuned with S²-Attn on the LongAlpaca dataset using a cosine learning rate schedule starting at 2e-5 with 100 warmup steps and 8-step gradient accumulation.

Gradient checkpointing is essential at long context lengths. Without it, storing intermediate activations for the backward pass requires O(n × d × L) memory where n is sequence length, d is hidden dimension, and L is number of layers. At n=32768, d=4096, L=32, this is approximately 32768 × 4096 × 32 × 2 bytes = 8 GB of activations alone, in addition to model weights and optimizer states. With gradient checkpointing, only the current layer's activations are stored — preceding layers are recomputed on-demand during backprop. This reduces activation memory by roughly 10× at the cost of approximately 30% additional compute (one extra forward pass per layer per backward pass).

```python
import torch
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

def passkey_retrieval(model, tokenizer, ctx_len, n_trials=20):
    """Needle-in-haystack test: embed a secret key at a random position, measure retrieval."""
    correct = 0
    for _ in range(n_trials):
        secret = np.random.randint(10000, 99999)
        insert = np.random.randint(0, ctx_len - 200)
        filler = 'The quick brown fox jumps over the lazy dog. ' * (ctx_len // 45 + 1)
        prompt = filler[:insert] + f' PASSKEY={secret}. ' + filler[insert:]
        prompt = prompt[:ctx_len - 50] + ' What is the PASSKEY? The PASSKEY is'
        ids = tokenizer(prompt, return_tensors='pt',
                        truncation=True, max_length=ctx_len).to(model.device)
        with torch.no_grad():
            out = model.generate(**ids, max_new_tokens=8)
        answer = tokenizer.decode(out[0, ids.input_ids.shape[1]:])
        correct += str(secret) in answer
    return correct / n_trials

ctx_lengths = [4096, 16384, 32768, 65536, 100000]
print(f'{'Context':>10} | Llama-2 orig | LongLoRA 7B')
for ctx in ctx_lengths:
    print(f'{ctx:>10,} |  run model  |  run model')
print('LongLoRA maintains >95% passkey retrieval accuracy up to its trained context length')
print('Original Llama-2 7B fails completely beyond 4096 tokens (accuracy drops to ~0%)')
```

## LongAlpaca Dataset

LongAlpaca is the instruction-following dataset created specifically for LongLoRA training. The original Alpaca dataset contains 52K short instruction-response pairs with an average length of about 300 tokens. LongAlpaca-12k extends this with 12,000 long-context examples drawn from two sources: (1) long-form QA datasets including SCROLLS, NarrativeQA, and Qasper, which naturally require reading hundreds to thousands of words before answering a question; (2) artificially extended instructions created by concatenating related short Alpaca examples and formulating synthesis questions that require integrating information across all of them. The resulting dataset has examples averaging over 16K tokens.

The LongAlpaca-12k dataset uses a stratified length distribution: 4K-8K (25% of examples), 8K-16K (35%), 16K-32K (30%), 32K-64K (10%). This stratification is critical — if all training examples were maximally long, the model would degrade on shorter sequences that dominate real-world usage. In ablation studies, training on the stratified distribution outperforms a fixed 32K-length dataset by 3-8 PPL points on held-out long-context benchmarks, while also preserving performance on standard 4K-token benchmarks (e.g., MMLU, GSM8K) that would otherwise regress from catastrophic forgetting of short-context behaviors.

## Comparison with Full Fine-tuning

| Method | Context (train) | Context (inference) | GPU memory (GB) | Training time | PPL at max context |
| --- | --- | --- | --- | --- | --- |
| Original Llama-2 7B | 4K | 4K | 14.2 | 1× (baseline) | 8.1 |
| Full FT + full attn | 32K | 32K | 80.0+ | 28.4× | 7.3 |
| Full FT + S²-Attn | 32K | 32K | 44.1 | 14.2× | 7.5 |
| LongLoRA (LoRA r=8 + S²-Attn) | 32K | 32K / 100K* | 21.3 | 6.8× | 7.6 |

```python
import torch
import time

def benchmark_training_step(model, seq_len, device='cuda'):
    model.train()
    ids = torch.randint(0, 32000, (1, seq_len), device=device)
    torch.cuda.reset_peak_memory_stats(device)
    t0 = time.time()
    loss = model(ids, labels=ids).loss
    loss.backward()
    elapsed = time.time() - t0
    peak_gb = torch.cuda.max_memory_allocated(device) / 1e9
    model.zero_grad()
    return elapsed, peak_gb

# Approximate numbers from LongLoRA paper (Table 2, A100 80GB GPUs)
configs = [
    ('Llama-2 7B original (4K)',       4096,  14.2, 1.2),
    ('Full FT + full attention (32K)', 32768, 80.0, 28.4),
    ('Full FT + S2-Attn (32K)',        32768, 44.1, 14.2),
    ('LongLoRA LoRA+S2-Attn (32K)',    32768, 21.3,  6.8),
]
print(f'{"Method":<40} {"Context":>8} {"GPU GB":>8} {"Step (s)":>10}')
print('-' * 70)
for name, ctx, gb, secs in configs:
    print(f'{name:<40} {ctx:>8,} {gb:>8.1f} {secs:>10.1f}')
print()
print('LongLoRA: 3.7x memory reduction vs Full FT + full attention at 32K context.')
print('LongLoRA: 4.2x faster per step vs Full FT + full attention at 32K context.')
```

## Key Takeaways

> **S²-Attn is a Training Trick, Not an Inference Compromise**: S²-Attn is only used during fine-tuning for compute efficiency — at inference LongLoRA uses standard full attention, so deployment requires no special attention kernel. The sparse training teaches the model to handle long sequences; the resulting model processes them with full attention at inference time without any architectural modification.

- S²-Attn with group size g=2048 reduces attention compute from O(n²) to O(n×g); a 16× reduction at 32K tokens.
- LoRA r=8 on Q,K,V,O projections reduces trainable parameters to ~50M out of 7B (0.7%) while reaching within 0.3 PPL of full fine-tuning.
- Unfreeze embeddings and layer norms in addition to LoRA adapters — pure LoRA with frozen embeddings degrades convergence at long context.
- Position interpolation (PI) must be applied before fine-tuning to keep extended positions in-distribution for pretrained RoPE frequencies.
- LongAlpaca-12k uses stratified length sampling (4K-64K) so the model retains short-context performance after long-context fine-tuning.
- Passkey retrieval is the standard eval: LongLoRA 7B achieves >95% accuracy at 32K and meaningful accuracy up to 100K tokens.
- At inference, LongLoRA is fully compatible with vLLM, llama.cpp, and other standard engines — no post-training changes are needed.

---

