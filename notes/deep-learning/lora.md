---
title: "LoRA — Low-Rank Adaptation for Parameter-Efficient LLM Fine-Tuning"
slug: "lora"
description: "Deep dive into LoRA (Hu et al., 2021): freeze pretrained weights W0, inject low-rank perturbation ΔW=BA, scale by α/r, and merge at inference for zero overhead. Covers math, scratch implementation, PEFT integration, weight merging, and rank ablation."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9SQSAoTG93LVJhbmsgQWRhcHRhdGlvbiwgSHUgZXQgYWwuIDIwMjEpIGlzIHRoZSBkb21pbmFudCBwYXJhbWV0ZXItZWZmaWNpZW50IGZpbmUtdHVuaW5nIChQRUZUKSBtZXRob2QgZm9yIExMTXMuIEluc3RlYWQgb2YgdXBkYXRpbmcgYWxsIDdCKyBwYXJhbWV0ZXJzIG9mIGEgcHJldHJhaW5lZCBtb2RlbCwgTG9SQSBmcmVlemVzIHRoZSBvcmlnaW5hbCB3ZWlnaHRzIFfigoAgYW5kIGluamVjdHMgYSB0cmFpbmFibGUgbG93LXJhbmsgcGVydHVyYmF0aW9uIM6UVyA9IEJBIGludG8gZWFjaCB0YXJnZXQgbGF5ZXIuIFRoZSBlbnRpcmUgdXBkYXRlIGlzIHBhcmFtZXRlcml6ZWQgYnkgdHdvIHNtYWxsIG1hdHJpY2VzIOKAlCBCIOKIiCDihJ1eKGTDl3IpIGFuZCBBIOKIiCDihJ1eKHLDl2spIOKAlCB3aGVyZSByIOKJqiBtaW4oZCwgaykuIFRoaXMgeWllbGRzIGEgMTAsMDAww5cgcmVkdWN0aW9uIGluIHRyYWluYWJsZSBwYXJhbWV0ZXJzIHdpdGggbmVhci16ZXJvIHF1YWxpdHkgbG9zcyBvbiBtb3N0IHRhc2tzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vdGl2YXRpb24gYW5kIEJhY2tncm91bmQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZ1bGwgZmluZS10dW5pbmcgYSA3QiBtb2RlbCByZXF1aXJlcyBzdG9yaW5nIGEgc2VwYXJhdGUgMTRHQiBjaGVja3BvaW50IHBlciB0YXNrIOKAlCBpbmZlYXNpYmxlIGF0IHNjYWxlLiBMb1JBXHUwMDI3cyBrZXkgaHlwb3RoZXNpcyAoc3VwcG9ydGVkIGJ5IEFnaGFqYW55YW4gZXQgYWwuIDIwMjApIGlzIHRoYXQgd2VpZ2h0IHVwZGF0ZXMgZHVyaW5nIGZpbmUtdHVuaW5nIGhhdmUgYSBsb3cgaW50cmluc2ljIHJhbms6IHRoZSBkZWx0YSDOlFcgbGl2ZXMgaW4gYSBsb3ctZGltZW5zaW9uYWwgc3Vic3BhY2UgZXZlbiB0aG91Z2ggV+KCgCBpcyBoaWdoLWRpbWVuc2lvbmFsLiBMb1JBIG1ha2VzIHRoaXMgZXhwbGljaXQgYnkgY29uc3RyYWluaW5nIM6UVyA9IEJBIHdoZXJlIHJhbmsoQkEpIOKJpCByLiBBdCBpbmZlcmVuY2UsIEJBIGNhbiBiZSBtZXJnZWQgaW50byBX4oKAIGVsaW1pbmF0aW5nIGFsbCBhZGFwdGVyIG92ZXJoZWFkOiBXX21lcmdlZCA9IFfigoAgKyAozrEvcinCt0JBLiJ9LHsidHlwZSI6Im1hdGgiLCJjb250ZW50IjoiaCA9IFdfMCB4ICsgXFxEZWx0YSBXIHggPSBXXzAgeCArIFxcZnJhY3tcXGFscGhhfXtyfSBCIEEgeCxcXHF1YWQgQiBcXGluIFxcbWF0aGJie1J9XntkIFxcdGltZXMgcn0sXFwgQSBcXGluIFxcbWF0aGJie1J9XntyIFxcdGltZXMga30sXFwgciBcXGxsIFxcbWluKGQsaykiLCJkaXNwbGF5Ijp0cnVlfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb1JBIEFyY2hpdGVjdHVyZSBhbmQgS2V5IFBhcmFtZXRlcnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBmb3J3YXJkIHBhc3MgcnVucyB0aGUgZnJvemVuIGJhc2UgV+KCgCBhbmQgdGhlIGxvdy1yYW5rIGJyYW5jaCBCQSBpbiBwYXJhbGxlbCwgdGhlbiBzdW1zIHRoZWlyIG91dHB1dHMgc2NhbGVkIGJ5IM6xL3IuIEluaXRpYWxpemF0aW9uOiBBIH4gTigwLCDPg8KyKSAoS2FpbWluZyB1bmlmb3JtIGluIHByYWN0aWNlKSwgQiA9IDAg4oCUIHNvIM6UVyA9IDAgYXQgdGhlIHN0YXJ0IG9mIHRyYWluaW5nLCBwcmVzZXJ2aW5nIHRoZSBwcmV0cmFpbmVkIG1vZGVsXHUwMDI3cyBiZWhhdmlvciBleGFjdGx5LiBUaGUgc2NhbGluZyDOsS9yIGRlY291cGxlcyByYW5rIGZyb20gZWZmZWN0aXZlIGxlYXJuaW5nIHJhdGU6IGtlZXBpbmcgzrEgZml4ZWQgd2hpbGUgc2VhcmNoaW5nIG92ZXIgciBtYWtlcyByYW5rIGEgcHVyZSBjYXBhY2l0eSBrbm9iLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsicmFuayByOiBleHByZXNzaXZpdHkgb2YgdGhlIGFkYXB0ZXIg4oCUIHI9NCw4LDE2LDMyIGNvdmVyIG1vc3QgdGFza3M7IGRpbWluaXNoaW5nIHJldHVybnMgYWZ0ZXIgcj0zMiIsImFscGhhIM6xOiBzY2FsaW5nIGNvbnN0YW50OyBzZXR0aW5nIM6xPTJyIGtlZXBzIHRoZSBlZmZlY3RpdmUgc3RlcCBzaXplIG9mIM6UVyBjb25zdGFudCBhY3Jvc3MgcmFuayBjaG9pY2VzIiwidGFyZ2V0X21vZHVsZXM6IHdoaWNoIHdlaWdodCBtYXRyaWNlcyB0byBhZGFwdCDigJQgUSBhbmQgViBwcm9qZWN0aW9ucyBhcmUgdGhlIGRlZmF1bHQ7IGFkZGluZyBLLCBPLCB1cCwgZG93biwgZ2F0ZSBpbXByb3ZlcyBwZXJmb3JtYW5jZSBhdCBoaWdoZXIgcGFyYW0gY29zdCIsImxvcmFfZHJvcG91dDogcmVndWxhcml6YXRpb24gYXBwbGllZCB0byBhZGFwdGVyIGlucHV0cyDigJQgMC4wNSB0byAwLjEgaXMgdHlwaWNhbDsgaGVscHMgd2l0aCBzbWFsbGVyIGRhdGFzZXRzIiwiYmlhczogd2hldGhlciB0byB0cmFpbiBiaWFzIHBhcmFtZXRlcnMgYWxvbmdzaWRlIGFkYXB0ZXJzIOKAlCBcdTAwMjdub25lXHUwMDI3IGlzIHRoZSBzdGFuZGFyZCBkZWZhdWx0IGZvciBMb1JBIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxvUkEgTGF5ZXIg4oCUIEltcGxlbWVudGF0aW9uIGZyb20gU2NyYXRjaCJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuY2xhc3MgTG9SQUxheWVyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTG93LVJhbmsgQWRhcHRhdGlvbjogaCA9IFcwIEAgeCArIChhbHBoYS9yKSAqIEIgQCBBIEAgeC5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9mZWF0dXJlczogaW50LCBvdXRfZmVhdHVyZXM6IGludCxcbiAgICAgICAgICAgICAgICAgcmFuazogaW50ID0gNCwgYWxwaGE6IGZsb2F0ID0gMTYuMCwgZHJvcG91dDogZmxvYXQgPSAwLjApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5yYW5rID0gcmFua1xuICAgICAgICBzZWxmLmFscGhhID0gYWxwaGFcbiAgICAgICAgc2VsZi5zY2FsaW5nID0gYWxwaGEgLyByYW5rXG5cbiAgICAgICAgIyBBIH4gS2FpbWluZyB1bmlmb3JtLCBCID0gMCBndWFyYW50ZWVzIGRlbHRhX1cgPSAwIGF0IHRyYWluaW5nIHN0YXJ0XG4gICAgICAgIHNlbGYubG9yYV9BID0gbm4uUGFyYW1ldGVyKHRvcmNoLmVtcHR5KHJhbmssIGluX2ZlYXR1cmVzKSlcbiAgICAgICAgc2VsZi5sb3JhX0IgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2ZlYXR1cmVzLCByYW5rKSlcbiAgICAgICAgc2VsZi5kcm9wb3V0ID0gbm4uRHJvcG91dChwPWRyb3BvdXQpXG4gICAgICAgIG5uLmluaXQua2FpbWluZ191bmlmb3JtXyhzZWxmLmxvcmFfQSwgYT1tYXRoLnNxcnQoNSkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IsIHByZXRyYWluZWRfd2VpZ2h0OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICAjIEZyb3plbiBiYXNlIHBhdGg6IFcwIEAgeFxuICAgICAgICBiYXNlX291dCA9IHggQCBwcmV0cmFpbmVkX3dlaWdodC5UXG4gICAgICAgICMgTG9SQSBicmFuY2g6IChhbHBoYS9yKSAqIEIgQCBBIEAgeFxuICAgICAgICBsb3JhX291dCA9IHNlbGYuZHJvcG91dCh4KSBAIHNlbGYubG9yYV9BLlQgQCBzZWxmLmxvcmFfQi5UXG4gICAgICAgIHJldHVybiBiYXNlX291dCArIHNlbGYuc2NhbGluZyAqIGxvcmFfb3V0XG5cbiMgVGVzdCB3aXRoIGEgdHlwaWNhbCBhdHRlbnRpb24gUS1wcm9qZWN0aW9uIChkX21vZGVsPTc2OClcbmxheWVyID0gTG9SQUxheWVyKGluX2ZlYXR1cmVzPTc2OCwgb3V0X2ZlYXR1cmVzPTc2OCwgcmFuaz04LCBhbHBoYT0xNilcbnggPSB0b3JjaC5yYW5kbigyLCAxMCwgNzY4KSAgIyBiYXRjaD0yLCBzZXFfbGVuPTEwLCBkX21vZGVsPTc2OFxuVzAgPSBubi5MaW5lYXIoNzY4LCA3NjgsIGJpYXM9RmFsc2UpLndlaWdodC5kYXRhXG5vdXRwdXQgPSBsYXllcih4LCBXMClcbnByaW50KGZcIk91dHB1dCBzaGFwZToge291dHB1dC5zaGFwZX1cIilcbnByaW50KGZcIlRyYWluYWJsZSBwYXJhbXM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIGxheWVyLnBhcmFtZXRlcnMoKSk6LH1cIikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkIgPSAwIGF0IGluaXRpYWxpemF0aW9uIGlzIG5vbi1uZWdvdGlhYmxlOiBpdCBlbnN1cmVzIHRoZSBhZGFwdGVkIG1vZGVsIGlzIGlkZW50aWNhbCB0byB0aGUgcHJldHJhaW5lZCBtb2RlbCBiZWZvcmUgYW55IGdyYWRpZW50IHVwZGF0ZXMsIG1ha2luZyB0aGUgZmluZS10dW5pbmcgc3RhYmxlIGFuZCBwcmVkaWN0YWJsZS4gQSBpcyBpbml0aWFsaXplZCB3aXRoIEthaW1pbmcgdW5pZm9ybSByYXRoZXIgdGhhbiBwdXJlIEdhdXNzaWFuIHRvIG1hdGNoIFB5VG9yY2hcdTAwMjdzIExpbmVhciBsYXllciBpbml0aWFsaXphdGlvbiwgd2hpY2ggcHJvdmlkZXMgYmV0dGVyIGdyYWRpZW50IGZsb3cgaW4gZWFybHkgdHJhaW5pbmcgc3RlcHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9SQSB3aXRoIEh1Z2dpbmdGYWNlIFBFRlQifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvVG9rZW5pemVyXG5mcm9tIHBlZnQgaW1wb3J0IExvcmFDb25maWcsIGdldF9wZWZ0X21vZGVsLCBUYXNrVHlwZVxuaW1wb3J0IHRvcmNoXG5cbm1vZGVsX25hbWUgPSBcIm1ldGEtbGxhbWEvTGxhbWEtMi03Yi1oZlwiXG5tb2RlbCA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcbiAgICBtb2RlbF9uYW1lLFxuICAgIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsXG4gICAgZGV2aWNlX21hcD1cImF1dG9cIixcbilcblxuIyBMb1JBIGNvbmZpZ3VyYXRpb24gdGFyZ2V0aW5nIFEsIEssIFYsIE8gYXR0ZW50aW9uIHByb2plY3Rpb25zXG5sb3JhX2NvbmZpZyA9IExvcmFDb25maWcoXG4gICAgdGFza190eXBlPVRhc2tUeXBlLkNBVVNBTF9MTSxcbiAgICByPTE2LCAgICAgICAgICAgICAgICAgICAgIyBSYW5rIG9mIHRoZSB1cGRhdGUgbWF0cmljZXNcbiAgICBsb3JhX2FscGhhPTMyLCAgICAgICAgICAgIyBTY2FsaW5nOiBlZmZlY3RpdmUgZmFjdG9yIGFscGhhL3IgPSAyLjBcbiAgICB0YXJnZXRfbW9kdWxlcz1bXCJxX3Byb2pcIiwgXCJ2X3Byb2pcIiwgXCJrX3Byb2pcIiwgXCJvX3Byb2pcIl0sXG4gICAgbG9yYV9kcm9wb3V0PTAuMDUsXG4gICAgYmlhcz1cIm5vbmVcIixcbilcblxucGVmdF9tb2RlbCA9IGdldF9wZWZ0X21vZGVsKG1vZGVsLCBsb3JhX2NvbmZpZylcblxuIyBSZXBvcnQgcGFyYW1ldGVyIGVmZmljaWVuY3lcbnRvdGFsID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBwZWZ0X21vZGVsLnBhcmFtZXRlcnMoKSlcbnRyYWluYWJsZSA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gcGVmdF9tb2RlbC5wYXJhbWV0ZXJzKCkgaWYgcC5yZXF1aXJlc19ncmFkKVxucHJpbnQoZlwiVG90YWwgcGFyYW1ldGVyczogICAgIHt0b3RhbDosfVwiKVxucHJpbnQoZlwiVHJhaW5hYmxlIHBhcmFtZXRlcnM6IHt0cmFpbmFibGU6LH1cIilcbnByaW50KGZcIlRyYWluYWJsZSBmcmFjdGlvbjogICB7MTAwICogdHJhaW5hYmxlIC8gdG90YWw6LjRmfSVcIilcbnBlZnRfbW9kZWwucHJpbnRfdHJhaW5hYmxlX3BhcmFtZXRlcnMoKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgN0IgTExhTUEgbW9kZWwgd2l0aCByPTE2IHRhcmdldGluZyBRLCBLLCBWLCBPIGFjcm9zcyAzMiB0cmFuc2Zvcm1lciBsYXllcnM6IHRyYWluYWJsZSBwYXJhbXMg4omIIDQgw5cgMiDDlyA0MDk2IMOXIDE2IMOXIDMyID0gMTM0TSwgcm91Z2hseSAxLjklIG9mIDdCIHRvdGFsLiBUYXJnZXRpbmcgb25seSBRIGFuZCBWIGhhbHZlcyB0aGlzIHRvIH42N00gKDAuOTYlKS4gVGhlIFBFRlQgbGlicmFyeSBoYW5kbGVzIGFkYXB0ZXIgaW5qZWN0aW9uLCB3ZWlnaHQgZnJlZXppbmcsIGFuZCBjaGVja3BvaW50IG1hbmFnZW1lbnQgYXV0b21hdGljYWxseSB2aWEgZ2V0X3BlZnRfbW9kZWwoKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXZWlnaHQgTWVyZ2luZyBmb3IgWmVyby1PdmVyaGVhZCBJbmZlcmVuY2UifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHBlZnQgaW1wb3J0IFBlZnRNb2RlbFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvVG9rZW5pemVyXG5cbiMgTG9hZCBiYXNlIG1vZGVsIGFuZCBMb1JBIGFkYXB0ZXIgc2VwYXJhdGVseVxuYmFzZV9tb2RlbCA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcbiAgICBcIm1ldGEtbGxhbWEvTGxhbWEtMi03Yi1oZlwiLFxuICAgIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsXG4gICAgZGV2aWNlX21hcD1cImF1dG9cIixcbilcbnBlZnRfbW9kZWwgPSBQZWZ0TW9kZWwuZnJvbV9wcmV0cmFpbmVkKGJhc2VfbW9kZWwsIFwiLi9sb3JhLWFkYXB0ZXItY2hlY2twb2ludFwiKVxuXG4jIE1lYXN1cmUgb3V0cHV0cyBiZWZvcmUgbWVyZ2luZ1xudG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQoXCJtZXRhLWxsYW1hL0xsYW1hLTItN2ItaGZcIilcbmlucHV0cyA9IHRva2VuaXplcihcIkhlbGxvLCB3b3JsZCFcIiwgcmV0dXJuX3RlbnNvcnM9XCJwdFwiKS50byhcImN1ZGFcIilcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIG91dF9wZWZ0ID0gcGVmdF9tb2RlbCgqKmlucHV0cykubG9naXRzXG5cbiMgTWVyZ2U6IFdfbWVyZ2VkID0gVzAgKyAoYWxwaGEvcikgKiBCIEAgQSAgKGRvbmUgb2ZmbGluZSBvbmNlKVxubWVyZ2VkX21vZGVsID0gcGVmdF9tb2RlbC5tZXJnZV9hbmRfdW5sb2FkKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIG91dF9tZXJnZWQgPSBtZXJnZWRfbW9kZWwoKippbnB1dHMpLmxvZ2l0c1xuXG4jIE91dHB1dHMgYXJlIG51bWVyaWNhbGx5IGlkZW50aWNhbCB3aXRoaW4gZnAxNiByb3VuZGluZ1xuZGlmZiA9IChvdXRfcGVmdCAtIG91dF9tZXJnZWQpLmFicygpLm1heCgpLml0ZW0oKVxucHJpbnQoZlwiTWF4IGxvZ2l0IGRpZmZlcmVuY2UgYWZ0ZXIgbWVyZ2U6IHtkaWZmOi4yZX1cIikgICMgfjFlLTVcbm1lcmdlZF9tb2RlbC5zYXZlX3ByZXRyYWluZWQoXCIuL21lcmdlZC1tb2RlbFwiKVxucHJpbnQoXCJNZXJnZWQgbW9kZWwgc2F2ZWQgLSBpbmZlcmVuY2UgaGFzIHplcm8gTG9SQSBvdmVyaGVhZFwiKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoibWVyZ2VfYW5kX3VubG9hZCgpIGl0ZXJhdGVzIG92ZXIgYWxsIExvUkEgbGF5ZXJzIGFuZCBjb21wdXRlcyBXX21lcmdlZCA9IFfigoAgKyAozrEvcinCt0JBIGluIHBsYWNlLCB0aGVuIHJlbW92ZXMgdGhlIGFkYXB0ZXIgbW9kdWxlcy4gVGhlIHJlc3VsdGluZyBtb2RlbCBoYXMgaWRlbnRpY2FsIGFyY2hpdGVjdHVyZSB0byB0aGUgb3JpZ2luYWwgcHJldHJhaW5lZCBtb2RlbCDigJQgbm8gZXh0cmEgcGFyYW1ldGVycywgbm8gZXh0cmEgY29tcHV0ZSwgbm8gbGF0ZW5jeSBwZW5hbHR5LiBUaGUgfjFlLTUgbWF4aW11bSBsb2dpdCBkaWZmZXJlbmNlIGlzIHB1cmUgZnAxNiByb3VuZGluZyBub2lzZSwgbm90IGEgY29ycmVjdG5lc3MgaXNzdWUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmFuayBBYmxhdGlvbiBTdHVkeSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplclxuZnJvbSBwZWZ0IGltcG9ydCBMb3JhQ29uZmlnLCBnZXRfcGVmdF9tb2RlbCwgVGFza1R5cGVcbmZyb20gZGF0YXNldHMgaW1wb3J0IGxvYWRfZGF0YXNldFxuXG5kZWYgY291bnRfdHJhaW5hYmxlKG1vZGVsKTpcbiAgICByZXR1cm4gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkgaWYgcC5yZXF1aXJlc19ncmFkKVxuXG5kZWYgcnVuX3JhbmtfYWJsYXRpb24oYmFzZV9tb2RlbF9uYW1lOiBzdHIsIHJhbmtzOiBsaXN0KSAtXHUwMDNlIGRpY3Q6XG4gICAgXCJcIlwiVHJhaW4gTG9SQSBhdCBkaWZmZXJlbnQgcmFua3M7IHJlcG9ydCB0cmFpbmFibGUgcGFyYW1zIGFuZCBldmFsIG1ldHJpY3MuXCJcIlwiXG4gICAgcmVzdWx0cyA9IHt9XG4gICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQoYmFzZV9tb2RlbF9uYW1lKVxuICAgIHRva2VuaXplci5wYWRfdG9rZW4gPSB0b2tlbml6ZXIuZW9zX3Rva2VuXG5cbiAgICBmb3IgciBpbiByYW5rczpcbiAgICAgICAgbW9kZWwgPSBBdXRvTW9kZWxGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQoXG4gICAgICAgICAgICBiYXNlX21vZGVsX25hbWUsIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsIGRldmljZV9tYXA9XCJhdXRvXCJcbiAgICAgICAgKVxuICAgICAgICBjb25maWcgPSBMb3JhQ29uZmlnKFxuICAgICAgICAgICAgdGFza190eXBlPVRhc2tUeXBlLkNBVVNBTF9MTSwgcj1yLCBsb3JhX2FscGhhPXIgKiAyLFxuICAgICAgICAgICAgdGFyZ2V0X21vZHVsZXM9W1wicV9wcm9qXCIsIFwidl9wcm9qXCJdLCBsb3JhX2Ryb3BvdXQ9MC4wNSxcbiAgICAgICAgKVxuICAgICAgICBwZWZ0X21vZGVsID0gZ2V0X3BlZnRfbW9kZWwobW9kZWwsIGNvbmZpZylcbiAgICAgICAgdHJhaW5hYmxlID0gY291bnRfdHJhaW5hYmxlKHBlZnRfbW9kZWwpXG4gICAgICAgICMgLi4uIHRyYWluaW5nIGFuZCBldmFsdWF0aW9uIG9uIGRvd25zdHJlYW0gdGFzayBvbWl0dGVkIC4uLlxuICAgICAgICBwcmludChmXCJyYW5rPXtyOjJkfSB8IHRyYWluYWJsZT17dHJhaW5hYmxlOlx1MDAzZTgsfSB8IGV2YWxfbG9zcz1cdTAwM2NydW4gdHJhaW5pbmdcdTAwM2VcIilcbiAgICAgICAgcmVzdWx0c1tyXSA9IHtcInRyYWluYWJsZV9wYXJhbXNcIjogdHJhaW5hYmxlfVxuICAgIHJldHVybiByZXN1bHRzXG5cbnJhbmtzID0gWzEsIDIsIDQsIDgsIDE2LCAzMl1cbnJlc3VsdHMgPSBydW5fcmFua19hYmxhdGlvbihcIm1ldGEtbGxhbWEvTGxhbWEtMi03Yi1oZlwiLCByYW5rcylcbmZvciByLCBpbmZvIGluIHJlc3VsdHMuaXRlbXMoKTpcbiAgICBwcmludChmXCJyPXtyOjJkfToge2luZm9bXHUwMDI3dHJhaW5hYmxlX3BhcmFtc1x1MDAyN106LH0gdHJhaW5hYmxlIHBhcmFtc1wiKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW1waXJpY2FsIGZpbmRpbmdzIGFjcm9zcyBpbnN0cnVjdGlvbi1mb2xsb3dpbmcgYmVuY2htYXJrczogcj0xIGlzIG9mdGVuIHN1ZmZpY2llbnQgZm9yIHNpbXBsZSBzdHlsZSB0cmFuc2ZlciB0YXNrcy4gcj04IHRvIHI9MTYgaXMgdGhlIHN3ZWV0IHNwb3QgZm9yIGdlbmVyYWwgaW5zdHJ1Y3Rpb24gZm9sbG93aW5nLiByPTMyIGhlbHBzIGZvciBjb21wbGV4IHJlYXNvbmluZyAoY29kZSwgbWF0aCkgd2hlcmUgdGhlIHVwZGF0ZSBzdWJzcGFjZSBpcyBsYXJnZXIuIEJleW9uZCByPTY0LCBMb1JBIGFwcHJvYWNoZXMgdGhlIGNvc3Qgb2YgZnVsbCBmaW5lLXR1bmluZyB3aXRoIGRpbWluaXNoaW5nIHJldHVybnMg4oCUIGF0IHRoYXQgcG9pbnQsIGZ1bGwgZmluZS10dW5pbmcgb3IgbGFyZ2UtcmFuayBQRUZUIGFsdGVybmF0aXZlcyBhcmUgd29ydGggY29uc2lkZXJpbmcuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlJhbmsgKHIpIiwiVHJhaW5hYmxlIFBhcmFtcyAoTSkiLCIlIG9mIDdCIFRvdGFsIiwiVHlwaWNhbCBUYXNrIFN1aXRhYmlsaXR5Il0sInJvd3MiOltbIjQiLCI4LjQiLCIwLjEyJSIsIk5hcnJvdyBkb21haW4gYWRhcHRhdGlvbiwgc21hbGwgZGF0YXNldHMgKFx1MDAzYzVLIGV4YW1wbGVzKSJdLFsiOCIsIjE2LjgiLCIwLjI0JSIsIkdlbmVyYWwgaW5zdHJ1Y3Rpb24gZm9sbG93aW5nLCBjaGF0IOKAlCBiYWxhbmNlZCBkZWZhdWx0Il0sWyIxNiIsIjMzLjYiLCIwLjQ4JSIsIk11bHRpLXRhc2ssIGluc3RydWN0aW9uICsgY2hhdCDigJQgcmVjb21tZW5kZWQgc3RhcnRpbmcgcG9pbnQiXSxbIjMyIiwiNjcuMSIsIjAuOTYlIiwiQ29tcGxleCByZWFzb25pbmcsIGNvZGluZywgbWF0aCDigJQgbGFyZ2VyIGRhdGFzZXRzIChcdTAwM2U1MEspIl0sWyI2NCIsIjEzNC4yIiwiMS45MiUiLCJOZWFyLWZ1bGwtZmluZXR1bmUgcXVhbGl0eSDigJQgdXNlIHdpdGggbGFyZ2UgZGF0YXNldHMgKDEwMEsrKSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEd1aWRlbGluZXMgYW5kIEJlc3QgUHJhY3RpY2VzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFydCB3aXRoIHI9MTYsIGFscGhhPTMyLCB0YXJnZXQgUSBhbmQgViBwcm9qZWN0aW9ucywgbGVhcm5pbmcgcmF0ZSAyZS00IHdpdGggY29zaW5lIGRlY2F5LCBhbmQgMyBlcG9jaHMuIElmIHRoZSBtb2RlbCB1bmRlcmZpdHMgKGV2YWwgbG9zcyBwbGF0ZWF1cyBoaWdoKSwgaW5jcmVhc2UgcmFuayBvciBhZGQgSywgTywgYW5kIEZGTiB0YXJnZXQgbW9kdWxlcy4gSWYgaXQgb3ZlcmZpdHMgKHRyYWluIGxvc3MgZmFsbHMgYnV0IGV2YWwgbG9zcyByaXNlcyksIHJlZHVjZSByYW5rIG9yIGFkZCBkcm9wb3V0LiBBbHdheXMgaW5zcGVjdCB0aGUgYWRhcHRlciBjaGVja3BvaW50IHNpemUg4oCUIGl0IHNob3VsZCBiZSB1bmRlciAxMDBNQiBmb3Igcj0xNiBvbiBhIDdCIG1vZGVsLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3RhcnQgc21hbGw6IHI9MTYgY292ZXJzIG1vc3QgdGFza3Mg4oCUIHNjYWxlIHVwIG9ubHkgd2hlbiBkb3duc3RyZWFtIHBlcmZvcm1hbmNlIHBsYXRlYXVzIiwiU2V0IGFscGhhPTIqcmFuayB0byBrZWVwIHRoZSBhZGFwdGVyIHVwZGF0ZSBzY2FsZSBjb25zdGFudCBhY3Jvc3MgcmFuayBzd2VlcHMiLCJVc2UgYSBsZWFybmluZyByYXRlIDUtMTB4IGhpZ2hlciB0aGFuIGZ1bGwgZmluZS10dW5pbmcgKDJlLTQgdnMgMmUtNSkg4oCUIHRoZSBhZGFwdGVyIGlzIHJhbmRvbWx5IGluaXRpYWxpemVkIiwiU2F2ZSBvbmx5IGFkYXB0ZXIgd2VpZ2h0cyB3aXRoIHBlZnRfbW9kZWwuc2F2ZV9wcmV0cmFpbmVkKCkg4oCUIHNhdmVzIH4xMDB4IHN0b3JhZ2UgdnMgZnVsbCBtb2RlbCBjaGVja3BvaW50cyIsIkZvciBtdWx0aS10YXNrIHNlcnZpbmc6IHN0b3JlIHNlcGFyYXRlIExvUkEgYWRhcHRlcnMgKGZldyBNQiBlYWNoKSBhbmQgaG90LXN3YXAgdGhlbSBhdCBpbmZlcmVuY2UgdGltZSIsIk1lcmdlIGFuZCB1bmxvYWQgYmVmb3JlIGRlcGxveW1lbnQgdG8gZWxpbWluYXRlIGFsbCBydW50aW1lIG92ZXJoZWFkIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiQWxwaGEvciBTY2FsaW5nIEluc2lnaHQiLCJjb250ZW50IjoiTG9SQVx1MDAyN3MgzrEvciBzY2FsaW5nIGZhY3RvciBpcyBjcnVjaWFsIOKAlCBrZWVwaW5nIM6xIGNvbnN0YW50IHdoaWxlIHZhcnlpbmcgciBlbnN1cmVzIHRoZSBlZmZlY3RpdmUgbGVhcm5pbmcgcmF0ZSBvZiDOlFcgPSAozrEvcilCQSBzdGF5cyBjb25zaXN0ZW50IHJlZ2FyZGxlc3Mgb2YgcmFuaywgbWFraW5nIHJhbmsgaHlwZXJwYXJhbWV0ZXIgc2VhcmNoZXMgbW9yZSBpbnRlcnByZXRhYmxlLiBGb3IgZXhhbXBsZSwgd2l0aCDOsT0xNjogcj00IOKGkiBzY2FsaW5nPTQuMCwgcj04IOKGkiBzY2FsaW5nPTIuMCwgcj0xNiDihpIgc2NhbGluZz0xLjAuIFVzaW5nIM6xPTJyIGtlZXBzIHNjYWxpbmc9Mi4wIGFjcm9zcyBhbGwgcmFua3MsIGRlY291cGxpbmcgcmFuayBmcm9tIGVmZmVjdGl2ZSBzdGVwIHNpemUgYW5kIG1ha2luZyByYW5rIGEgcHVyZSBjYXBhY2l0eSBrbm9iLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9SQSByZW1haW5zIHRoZSBnb2xkIHN0YW5kYXJkIFBFRlQgbWV0aG9kIGJlY2F1c2Ugb2YgaXRzIHNpbXBsaWNpdHksIHplcm8gaW5mZXJlbmNlIG92ZXJoZWFkIGFmdGVyIG1lcmdpbmcsIGFuZCBzdHJvbmcgZW1waXJpY2FsIHBlcmZvcm1hbmNlIGFjcm9zcyBOTFAgYmVuY2htYXJrcy4gRXh0ZW5zaW9ucyBsaWtlIFFMb1JBICg0LWJpdCBxdWFudGl6YXRpb24gKyBMb1JBKSwgRG9SQSAod2VpZ2h0IGRlY29tcG9zaXRpb24gaW50byBtYWduaXR1ZGUgYW5kIGRpcmVjdGlvbiksIGFuZCBMb1JBKyAoYXN5bW1ldHJpYyBsZWFybmluZyByYXRlcyBmb3IgQSB2cyBCKSBoYXZlIHB1c2hlZCB0aGUgUGFyZXRvIGZyb250aWVyIGZ1cnRoZXIsIGJ1dCB2YW5pbGxhIExvUkEgaXMgc3RpbGwgdGhlIGZpcnN0IHRvb2wgdG8gcmVhY2ggZm9yIHdoZW4gYWRhcHRpbmcgYSBwcmV0cmFpbmVkIExMTSB0byBhIG5ldyB0YXNrLiJ9XQ=="
---
# LoRA — Low-Rank Adaptation for Parameter-Efficient LLM Fine-Tuning

LoRA (Low-Rank Adaptation, Hu et al. 2021) is the dominant parameter-efficient fine-tuning (PEFT) method for LLMs. Instead of updating all 7B+ parameters of a pretrained model, LoRA freezes the original weights W₀ and injects a trainable low-rank perturbation ΔW = BA into each target layer. The entire update is parameterized by two small matrices — B ∈ ℝ^(d×r) and A ∈ ℝ^(r×k) — where r ≪ min(d, k). This yields a 10,000× reduction in trainable parameters with near-zero quality loss on most tasks.

## Motivation and Background

Full fine-tuning a 7B model requires storing a separate 14GB checkpoint per task — infeasible at scale. LoRA's key hypothesis (supported by Aghajanyan et al. 2020) is that weight updates during fine-tuning have a low intrinsic rank: the delta ΔW lives in a low-dimensional subspace even though W₀ is high-dimensional. LoRA makes this explicit by constraining ΔW = BA where rank(BA) ≤ r. At inference, BA can be merged into W₀ eliminating all adapter overhead: W_merged = W₀ + (α/r)·BA.

$$h = W_0 x + \Delta W x = W_0 x + \frac{\alpha}{r} B A x,\quad B \in \mathbb{R}^{d \times r},\ A \in \mathbb{R}^{r \times k},\ r \ll \min(d,k)$$

## LoRA Architecture and Key Parameters

The forward pass runs the frozen base W₀ and the low-rank branch BA in parallel, then sums their outputs scaled by α/r. Initialization: A ~ N(0, σ²) (Kaiming uniform in practice), B = 0 — so ΔW = 0 at the start of training, preserving the pretrained model's behavior exactly. The scaling α/r decouples rank from effective learning rate: keeping α fixed while searching over r makes rank a pure capacity knob.

- rank r: expressivity of the adapter — r=4,8,16,32 cover most tasks; diminishing returns after r=32
- alpha α: scaling constant; setting α=2r keeps the effective step size of ΔW constant across rank choices
- target_modules: which weight matrices to adapt — Q and V projections are the default; adding K, O, up, down, gate improves performance at higher param cost
- lora_dropout: regularization applied to adapter inputs — 0.05 to 0.1 is typical; helps with smaller datasets
- bias: whether to train bias parameters alongside adapters — 'none' is the standard default for LoRA

## LoRA Layer — Implementation from Scratch

```python
import torch
import torch.nn as nn
import math

class LoRALayer(nn.Module):
    """Low-Rank Adaptation: h = W0 @ x + (alpha/r) * B @ A @ x."""

    def __init__(self, in_features: int, out_features: int,
                 rank: int = 4, alpha: float = 16.0, dropout: float = 0.0):
        super().__init__()
        self.rank = rank
        self.alpha = alpha
        self.scaling = alpha / rank

        # A ~ Kaiming uniform, B = 0 guarantees delta_W = 0 at training start
        self.lora_A = nn.Parameter(torch.empty(rank, in_features))
        self.lora_B = nn.Parameter(torch.zeros(out_features, rank))
        self.dropout = nn.Dropout(p=dropout)
        nn.init.kaiming_uniform_(self.lora_A, a=math.sqrt(5))

    def forward(self, x: torch.Tensor, pretrained_weight: torch.Tensor) -> torch.Tensor:
        # Frozen base path: W0 @ x
        base_out = x @ pretrained_weight.T
        # LoRA branch: (alpha/r) * B @ A @ x
        lora_out = self.dropout(x) @ self.lora_A.T @ self.lora_B.T
        return base_out + self.scaling * lora_out

# Test with a typical attention Q-projection (d_model=768)
layer = LoRALayer(in_features=768, out_features=768, rank=8, alpha=16)
x = torch.randn(2, 10, 768)  # batch=2, seq_len=10, d_model=768
W0 = nn.Linear(768, 768, bias=False).weight.data
output = layer(x, W0)
print(f"Output shape: {output.shape}")
print(f"Trainable params: {sum(p.numel() for p in layer.parameters()):,}")
```

B = 0 at initialization is non-negotiable: it ensures the adapted model is identical to the pretrained model before any gradient updates, making the fine-tuning stable and predictable. A is initialized with Kaiming uniform rather than pure Gaussian to match PyTorch's Linear layer initialization, which provides better gradient flow in early training steps.

## LoRA with HuggingFace PEFT

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, TaskType
import torch

model_name = "meta-llama/Llama-2-7b-hf"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)

# LoRA configuration targeting Q, K, V, O attention projections
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,                    # Rank of the update matrices
    lora_alpha=32,           # Scaling: effective factor alpha/r = 2.0
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
)

peft_model = get_peft_model(model, lora_config)

# Report parameter efficiency
total = sum(p.numel() for p in peft_model.parameters())
trainable = sum(p.numel() for p in peft_model.parameters() if p.requires_grad)
print(f"Total parameters:     {total:,}")
print(f"Trainable parameters: {trainable:,}")
print(f"Trainable fraction:   {100 * trainable / total:.4f}%")
peft_model.print_trainable_parameters()
```

For a 7B LLaMA model with r=16 targeting Q, K, V, O across 32 transformer layers: trainable params ≈ 4 × 2 × 4096 × 16 × 32 = 134M, roughly 1.9% of 7B total. Targeting only Q and V halves this to ~67M (0.96%). The PEFT library handles adapter injection, weight freezing, and checkpoint management automatically via get_peft_model().

## Weight Merging for Zero-Overhead Inference

```python
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load base model and LoRA adapter separately
base_model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    torch_dtype=torch.float16,
    device_map="auto",
)
peft_model = PeftModel.from_pretrained(base_model, "./lora-adapter-checkpoint")

# Measure outputs before merging
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
inputs = tokenizer("Hello, world!", return_tensors="pt").to("cuda")
with torch.no_grad():
    out_peft = peft_model(**inputs).logits

# Merge: W_merged = W0 + (alpha/r) * B @ A  (done offline once)
merged_model = peft_model.merge_and_unload()
with torch.no_grad():
    out_merged = merged_model(**inputs).logits

# Outputs are numerically identical within fp16 rounding
diff = (out_peft - out_merged).abs().max().item()
print(f"Max logit difference after merge: {diff:.2e}")  # ~1e-5
merged_model.save_pretrained("./merged-model")
print("Merged model saved - inference has zero LoRA overhead")
```

merge_and_unload() iterates over all LoRA layers and computes W_merged = W₀ + (α/r)·BA in place, then removes the adapter modules. The resulting model has identical architecture to the original pretrained model — no extra parameters, no extra compute, no latency penalty. The ~1e-5 maximum logit difference is pure fp16 rounding noise, not a correctness issue.

## Rank Ablation Study

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, TaskType
from datasets import load_dataset

def count_trainable(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def run_rank_ablation(base_model_name: str, ranks: list) -> dict:
    """Train LoRA at different ranks; report trainable params and eval metrics."""
    results = {}
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    tokenizer.pad_token = tokenizer.eos_token

    for r in ranks:
        model = AutoModelForCausalLM.from_pretrained(
            base_model_name, torch_dtype=torch.float16, device_map="auto"
        )
        config = LoraConfig(
            task_type=TaskType.CAUSAL_LM, r=r, lora_alpha=r * 2,
            target_modules=["q_proj", "v_proj"], lora_dropout=0.05,
        )
        peft_model = get_peft_model(model, config)
        trainable = count_trainable(peft_model)
        # ... training and evaluation on downstream task omitted ...
        print(f"rank={r:2d} | trainable={trainable:>8,} | eval_loss=<run training>")
        results[r] = {"trainable_params": trainable}
    return results

ranks = [1, 2, 4, 8, 16, 32]
results = run_rank_ablation("meta-llama/Llama-2-7b-hf", ranks)
for r, info in results.items():
    print(f"r={r:2d}: {info['trainable_params']:,} trainable params")
```

Empirical findings across instruction-following benchmarks: r=1 is often sufficient for simple style transfer tasks. r=8 to r=16 is the sweet spot for general instruction following. r=32 helps for complex reasoning (code, math) where the update subspace is larger. Beyond r=64, LoRA approaches the cost of full fine-tuning with diminishing returns — at that point, full fine-tuning or large-rank PEFT alternatives are worth considering.

| Rank (r) | Trainable Params (M) | % of 7B Total | Typical Task Suitability |
| --- | --- | --- | --- |
| 4 | 8.4 | 0.12% | Narrow domain adaptation, small datasets (<5K examples) |
| 8 | 16.8 | 0.24% | General instruction following, chat — balanced default |
| 16 | 33.6 | 0.48% | Multi-task, instruction + chat — recommended starting point |
| 32 | 67.1 | 0.96% | Complex reasoning, coding, math — larger datasets (>50K) |
| 64 | 134.2 | 1.92% | Near-full-finetune quality — use with large datasets (100K+) |

## Practical Guidelines and Best Practices

Start with r=16, alpha=32, target Q and V projections, learning rate 2e-4 with cosine decay, and 3 epochs. If the model underfits (eval loss plateaus high), increase rank or add K, O, and FFN target modules. If it overfits (train loss falls but eval loss rises), reduce rank or add dropout. Always inspect the adapter checkpoint size — it should be under 100MB for r=16 on a 7B model.

- Start small: r=16 covers most tasks — scale up only when downstream performance plateaus
- Set alpha=2*rank to keep the adapter update scale constant across rank sweeps
- Use a learning rate 5-10x higher than full fine-tuning (2e-4 vs 2e-5) — the adapter is randomly initialized
- Save only adapter weights with peft_model.save_pretrained() — saves ~100x storage vs full model checkpoints
- For multi-task serving: store separate LoRA adapters (few MB each) and hot-swap them at inference time
- Merge and unload before deployment to eliminate all runtime overhead

> **Alpha/r Scaling Insight**: LoRA's α/r scaling factor is crucial — keeping α constant while varying r ensures the effective learning rate of ΔW = (α/r)BA stays consistent regardless of rank, making rank hyperparameter searches more interpretable. For example, with α=16: r=4 → scaling=4.0, r=8 → scaling=2.0, r=16 → scaling=1.0. Using α=2r keeps scaling=2.0 across all ranks, decoupling rank from effective step size and making rank a pure capacity knob.

LoRA remains the gold standard PEFT method because of its simplicity, zero inference overhead after merging, and strong empirical performance across NLP benchmarks. Extensions like QLoRA (4-bit quantization + LoRA), DoRA (weight decomposition into magnitude and direction), and LoRA+ (asymmetric learning rates for A vs B) have pushed the Pareto frontier further, but vanilla LoRA is still the first tool to reach for when adapting a pretrained LLM to a new task.

