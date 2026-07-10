---
title: "Stable Diffusion Architecture — VAE, U-Net, and CLIP"
slug: "stable-diffusion-architecture"
description: "A detailed walkthrough of Stable Diffusion's three core components — the KL-regularized VAE, the CLIP text encoder, and the time-conditioned U-Net denoiser — covering cross-attention conditioning, timestep embeddings, and ControlNet structural conditioning."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhYmxlIERpZmZ1c2lvbiAoUm9tYmFjaCBldCBhbC4gMjAyMikgcGVyZm9ybXMgZGlmZnVzaW9uIGluIGEgY29tcHJlc3NlZCBsYXRlbnQgc3BhY2UgcmF0aGVyIHRoYW4gcGl4ZWwgc3BhY2UsIHJlZHVjaW5nIGNvbXB1dGF0aW9uIGJ5IHJvdWdobHkgNjTDly4gVGhlIGFyY2hpdGVjdHVyZSBjb3VwbGVzIHRocmVlIGluZGVwZW5kZW50bHkgdXBkYXRlYWJsZSBjb21wb25lbnRzOiBhIEtMLXJlZ3VsYXJpemVkIFZBRSB0aGF0IGNvbXByZXNzZXMgaW1hZ2VzIHRvIGEgNC1jaGFubmVsIGxhdGVudCBncmlkIGF0IDEvOCByZXNvbHV0aW9uLCBhIENMSVAgdGV4dCBlbmNvZGVyIHRoYXQgY29udmVydHMgcHJvbXB0cyB0byBzZXF1ZW5jZSBlbWJlZGRpbmdzLCBhbmQgYSB0aW1lLWNvbmRpdGlvbmVkIFUtTmV0IHRoYXQgaXRlcmF0aXZlbHkgZGVub2lzZXMgdGhlIGxhdGVudCB1bmRlciB0ZXh0IGd1aWRhbmNlLiBVbmRlcnN0YW5kaW5nIGhvdyBjcm9zcy1hdHRlbnRpb24gd2lyZXMgdGV4dCBpbnRvIHNwYXRpYWwgZmVhdHVyZXMg4oCUIGFuZCBob3cgQ29udHJvbE5ldCBhZGRzIHN0cnVjdHVyYWwgY29uZGl0aW9uaW5nIOKAlCBpcyBlc3NlbnRpYWwgZm9yIGFkYXB0aW5nIG9yIGV4dGVuZGluZyBTdGFibGUgRGlmZnVzaW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0YWJsZSBEaWZmdXNpb24gQ29tcG9uZW50IE92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgaW5mZXJlbmNlIHBpcGVsaW5lIGZsb3dzOiBlbmNvZGUgcHJvbXB0IHdpdGggQ0xJUCDihpIgc2FtcGxlIEdhdXNzaWFuIG5vaXNlIHpfVCBpbiBsYXRlbnQgc3BhY2Ug4oaSIHJ1biBkZW5vaXNlciBVLU5ldCBmb3IgVCBzdGVwcyB3aXRoIHRleHQgY29uZGl0aW9uaW5nIOKGkiBkZWNvZGUgbGF0ZW50IHpfMCB3aXRoIFZBRSBkZWNvZGVyLiBUaGUgVkFFIGVuY29kZXIgaXMgdXNlZCBvbmx5IGR1cmluZyB0cmFpbmluZywgbm90IGluZmVyZW5jZS4gQ0xJUCBwcm9kdWNlcyBwZXItdG9rZW4gZW1iZWRkaW5ncyAobm90IGEgc2luZ2xlIHBvb2xlZCB2ZWN0b3IpIHNvIHRoYXQgaW5kaXZpZHVhbCB0b2tlbnMgY2FuIGF0dGVuZCB0byBkaWZmZXJlbnQgc3BhdGlhbCByZWdpb25zIHZpYSBjcm9zcy1hdHRlbnRpb24uIFRoZSBVLU5ldCBvcGVyYXRlcyBlbnRpcmVseSBhdCAxLzggcGl4ZWwgcmVzb2x1dGlvbiwgbWFraW5nIDUxMsOXNTEyIGdlbmVyYXRpb24gZmVhc2libGUgb24gY29uc3VtZXIgaGFyZHdhcmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVkFFIEVuY29kZXIgYW5kIERlY29kZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBWQUUgdXNlcyBhIEtMLWRpdmVyZ2VuY2UgcmVndWxhcmlzYXRpb24gdGVybSB3aXRoIGEgc21hbGwgd2VpZ2h0ICjOuz0xZS02KSB0byBrZWVwIHRoZSBsYXRlbnQgZGlzdHJpYnV0aW9uIGNsb3NlIHRvIGEgc3RhbmRhcmQgR2F1c3NpYW4gd2hpbGUgcHJpb3JpdGlzaW5nIHJlY29uc3RydWN0aW9uIHF1YWxpdHkuIFRoZSBlbmNvZGVyIEUgbWFwcyBIw5dXw5czIGltYWdlcyB0byAoSC84KcOXKFcvOCnDlzQgbGF0ZW50czogYSA1MTLDlzUxMiBpbWFnZSBiZWNvbWVzIDY0w5c2NMOXNC4gVGhlIGZvdXIgbGF0ZW50IGNoYW5uZWxzIHByb3ZpZGUgcmljaGVyIHBlci1sb2NhdGlvbiByZXByZXNlbnRhdGlvbiB0aGFuIGEgc2luZ2xlIGNoYW5uZWwuIEF0IGVuY29kZSB0aW1lIM+D4omIMCwgc28gbGF0ZW50cyBhcmUgbmVhcmx5IGRldGVybWluaXN0aWMuIFRoZSBkZWNvZGVyIEQgdXNlcyBzeW1tZXRyaWMgcmVzaWR1YWwgYmxvY2tzIHdpdGggc2VsZi1hdHRlbnRpb24gYXQgdGhlIGJvdHRsZW5lY2sgdG8gdXBzYW1wbGUgNjTDlzY0w5c0IGJhY2sgdG8gNTEyw5c1MTLDlzMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ0xJUCBUZXh0IEVuY29kZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNEIDEueCB1c2VzIE9wZW5BSSBDTElQIFZpVC1MLzE0LCBwcm9kdWNpbmcgNzfDlzc2OCBzZXF1ZW5jZSBlbWJlZGRpbmdzLiBTRCAyLnggdXNlcyBPcGVuQ0xJUCBWaVQtSC8xNCAoNzfDlzEwMjQpLiBTRFhMIGNvbmNhdGVuYXRlcyBlbWJlZGRpbmdzIGZyb20gQ0xJUC1MLzE0IGFuZCBPcGVuQ0xJUC1HLzE0IHRvIHByb2R1Y2UgNzfDlzIwNDggY29uZGl0aW9uaW5nIHdpdGggcmljaGVyIHNlbWFudGljcy4gU0QzIGFuZCBGTFVYIGFkZGl0aW9uYWxseSBpbmNvcnBvcmF0ZSBUNS1YWEwgZm9yIGJldHRlciBsYW5ndWFnZSB1bmRlcnN0YW5kaW5nLiBUaGUgZW50aXJlIHRva2VuIHNlcXVlbmNlIChub3QganVzdCB0aGUgcG9vbGVkIENMUyBlbWJlZGRpbmcpIGlzIHBhc3NlZCB0byBjcm9zcy1hdHRlbnRpb24gc28gZWFjaCB0ZXh0IHRva2VuIGNhbiBpbmZsdWVuY2UgZGlmZmVyZW50IHNwYXRpYWwgcG9zaXRpb25zIGluZGVwZW5kZW50bHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVS1OZXQgRGVub2lzZXIgYW5kIENyb3NzLUF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFUtTmV0IGhhcyB0aHJlZSBwYXRoczogYSBkb3duc2FtcGxpbmcgZW5jb2RlciAoUmVzQmxvY2tzICsgc2VsZi1hdHRlbnRpb24gYXQgbG93ZXIgcmVzb2x1dGlvbnMpLCBhIGJvdHRsZW5lY2sgKHNlbGYgKyBjcm9zcy1hdHRlbnRpb24pLCBhbmQgYW4gdXBzYW1wbGluZyBkZWNvZGVyIHRoYXQgcmVjZWl2ZXMgc2tpcCBjb25uZWN0aW9ucyBmcm9tIHRoZSBlbmNvZGVyLiBDcm9zcy1hdHRlbnRpb24gaW5qZWN0cyB0ZXh0OiBxdWVyaWVzIFEgY29tZSBmcm9tIGZsYXR0ZW5lZCBzcGF0aWFsIGZlYXR1cmVzLCBrZXlzIEsgYW5kIHZhbHVlcyBWIGNvbWUgZnJvbSBDTElQIGVtYmVkZGluZ3MuIEVhY2ggc3BhdGlhbCB0b2tlbiBhdHRlbmRzIHRvIGFsbCA3NyB0ZXh0IHRva2VucywgYWxsb3dpbmcgdGV4dCB0byBjb250cm9sIHdoaWNoIHJlZ2lvbiBzaG93cyB3aGljaCBjb25jZXB0LiBUaGUgc3BhdGlhbCBkaW1lbnNpb24gb2YgdGhlIFUtTmV0IHZhcmllcyBieSByZXNvbHV0aW9uIGxldmVsIOKAlCA2NMOXNjQgYXQgdGhlIGZpcnN0IGxldmVsIHRvIDjDlzggYXQgdGhlIGJvdHRsZW5lY2suIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIENyb3NzQXR0ZW50aW9uQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJRIGZyb20gaW1hZ2UgbGF0ZW50IGZlYXR1cmVzLCBLL1YgZnJvbSBDTElQIHRleHQgZW1iZWRkaW5ncy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltX3EsIGRpbV9rdiwgbl9oZWFkcz04KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubl9oZWFkcyA9IG5faGVhZHNcbiAgICAgICAgc2VsZi5oZWFkX2RpbSA9IGRpbV9xIC8vIG5faGVhZHNcbiAgICAgICAgc2VsZi5zY2FsZSA9IHNlbGYuaGVhZF9kaW0gKiogLTAuNVxuICAgICAgICBzZWxmLnRvX3EgPSBubi5MaW5lYXIoZGltX3EsIGRpbV9xLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnRvX2sgPSBubi5MaW5lYXIoZGltX2t2LCBkaW1fcSwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi50b192ID0gbm4uTGluZWFyKGRpbV9rdiwgZGltX3EsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYucHJvaiA9IG5uLkxpbmVhcihkaW1fcSwgZGltX3EpXG4gICAgICAgIHNlbGYubm9ybV9xID0gbm4uTGF5ZXJOb3JtKGRpbV9xKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgY29udGV4dCk6XG4gICAgICAgIEIsIE4sIEMgPSB4LnNoYXBlICAjIE4gPSBIKlcgc3BhdGlhbCB0b2tlbnNcbiAgICAgICAgcSA9IHNlbGYudG9fcShzZWxmLm5vcm1fcSh4KSkucmVzaGFwZShCLCBOLCBzZWxmLm5faGVhZHMsIHNlbGYuaGVhZF9kaW0pLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICBrID0gc2VsZi50b19rKGNvbnRleHQpLnJlc2hhcGUoQiwgLTEsIHNlbGYubl9oZWFkcywgc2VsZi5oZWFkX2RpbSkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIHYgPSBzZWxmLnRvX3YoY29udGV4dCkucmVzaGFwZShCLCAtMSwgc2VsZi5uX2hlYWRzLCBzZWxmLmhlYWRfZGltKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgYXR0biA9IHRvcmNoLnNvZnRtYXgocSBAIGsudHJhbnNwb3NlKC0yLCAtMSkgKiBzZWxmLnNjYWxlLCBkaW09LTEpXG4gICAgICAgIG91dCA9IChhdHRuIEAgdikudHJhbnNwb3NlKDEsIDIpLnJlc2hhcGUoQiwgTiwgQylcbiAgICAgICAgcmV0dXJuIHggKyBzZWxmLnByb2oob3V0KVxuXG5ibG9jayA9IENyb3NzQXR0ZW50aW9uQmxvY2soZGltX3E9MzIwLCBkaW1fa3Y9NzY4LCBuX2hlYWRzPTgpXG54ICAgPSB0b3JjaC5yYW5kbigyLCA2NCwgMzIwKSAgICAjIDh4OCBzcGF0aWFsIHRva2VucywgVS1OZXQgY2hhbm5lbHNcbmN0eCA9IHRvcmNoLnJhbmRuKDIsIDc3LCA3NjgpICAgIyBDTElQIHRleHQgZW1iZWRkaW5ncyAoU0QgMS54LCA3NjgtZGltKVxucHJpbnQoXHUwMDI3Q3Jvc3MtYXR0biBvdXRwdXQ6XHUwMDI3LCBibG9jayh4LCBjdHgpLnNoYXBlKSAgIyAoMiwgNjQsIDMyMCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaW1lc3RlcCBFbWJlZGRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBVLU5ldCBtdXN0IGtub3cgdGhlIGN1cnJlbnQgbm9pc2UgbGV2ZWwgdCB0byBkZW5vaXNlIGFwcHJvcHJpYXRlbHkuIFRpbWVzdGVwIHQg4oiIIHswLC4uLixUfSBpcyBmaXJzdCBlbmNvZGVkIHdpdGggc2ludXNvaWRhbCBlbWJlZGRpbmdzIChpZGVudGljYWwgdG8gVHJhbnNmb3JtZXIgcG9zaXRpb25hbCBlbmNvZGluZ3MpIHRoZW4gcHJvamVjdGVkIHRocm91Z2ggYSAyLWxheWVyIFNpTFUgTUxQLiBUaGUgcmVzdWx0aW5nIHZlY3RvciBjb25kaXRpb25zIGVhY2ggcmVzaWR1YWwgYmxvY2sgdmlhIEFkYXB0aXZlIEdyb3VwIE5vcm1hbGl6YXRpb24gKEFkYUdOKTogdGhlIHRpbWVzdGVwIE1MUCBwcmVkaWN0cyBwZXItY2hhbm5lbCBzY2FsZSDOsSh0KSBhbmQgc2hpZnQgzrQodCkgdGhhdCBtb2R1bGF0ZSB0aGUgbm9ybWFsaXNlZCBhY3RpdmF0aW9ucyBiZWZvcmUgdGhlIGNvbnZvbHV0aW9uLCBhbGxvd2luZyB0aGUgVS1OZXQgdG8gYmVoYXZlIGRpZmZlcmVudGx5IGF0IGV2ZXJ5IG5vaXNlIGxldmVsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuY2xhc3MgVGltZXN0ZXBFbWJlZGRpbmcobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTaW51c29pZGFsIHBvc2l0aW9uYWwgZW5jb2RpbmcgLVx1MDAzZSBNTFAgLVx1MDAzZSBpbmplY3RlZCBpbnRvIFJlc0Jsb2NrcyB2aWEgQWRhR04uXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbSwgb3V0X2RpbT1Ob25lKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIG91dF9kaW0gPSBvdXRfZGltIG9yIGRpbSAqIDRcbiAgICAgICAgc2VsZi5kaW0gPSBkaW1cbiAgICAgICAgc2VsZi5tbHAgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkaW0sIG91dF9kaW0pLCBubi5TaUxVKCksIG5uLkxpbmVhcihvdXRfZGltLCBvdXRfZGltKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHQpOlxuICAgICAgICBoYWxmID0gc2VsZi5kaW0gLy8gMlxuICAgICAgICBmcmVxcyA9IHRvcmNoLmV4cCgtbWF0aC5sb2coMTAwMDApICogdG9yY2guYXJhbmdlKGhhbGYsIGR0eXBlPXRvcmNoLmZsb2F0MzIsIGRldmljZT10LmRldmljZSkgLyBoYWxmKVxuICAgICAgICBhcmdzID0gdFs6LCBOb25lXS5mbG9hdCgpICogZnJlcXNbTm9uZV1cbiAgICAgICAgcmV0dXJuIHNlbGYubWxwKHRvcmNoLmNhdChbYXJncy5zaW4oKSwgYXJncy5jb3MoKV0sIGRpbT0tMSkpXG5cbmRlZiBhZGFfZ25fZm9yd2FyZCh4LCB0X2VtYiwgbm9ybSwgdGltZV9wcm9qKTpcbiAgICBcIlwiXCJBcHBseSBBZGFwdGl2ZSBHcm91cE5vcm06IHRfZW1iIC1cdTAwM2UgKHNjYWxlLCBzaGlmdCkgbW9kdWxhdGUgbm9ybSBvdXRwdXQuXCJcIlwiXG4gICAgc2NhbGUsIHNoaWZ0ID0gdGltZV9wcm9qKHRfZW1iKS5jaHVuaygyLCBkaW09LTEpXG4gICAgcmV0dXJuIG5vcm0oeCkgKiAoMSArIHNjYWxlWzosIDosIE5vbmUsIE5vbmVdKSArIHNoaWZ0WzosIDosIE5vbmUsIE5vbmVdXG5cbnRzID0gVGltZXN0ZXBFbWJlZGRpbmcoZGltPTEyOCwgb3V0X2RpbT01MTIpXG50ID0gdG9yY2gucmFuZGludCgwLCAxMDAwLCAoNCwpKVxudF9lbWIgPSB0cyh0KVxucHJpbnQoZlx1MDAyN1RpbWVzdGVwIHt0LnRvbGlzdCgpfSAtXHUwMDNlIGVtYmVkZGluZyBzaGFwZToge3RfZW1iLnNoYXBlfVx1MDAyNykgICMgKDQsIDUxMilcblxubm9ybSA9IG5uLkdyb3VwTm9ybSgzMiwgMjU2KVxudGltZV9wcm9qID0gbm4uTGluZWFyKDUxMiwgNTEyKSAgIyBwcmVkaWN0cyBzY2FsZStzaGlmdCBmb3IgMjU2IGNoYW5uZWxzXG54ID0gdG9yY2gucmFuZG4oNCwgMjU2LCAxNiwgMTYpXG54X2NvbmQgPSBhZGFfZ25fZm9yd2FyZCh4LCB0X2VtYiwgbm9ybSwgdGltZV9wcm9qKVxucHJpbnQoZlx1MDAyN0FmdGVyIEFkYUdOOiBtZWFuPXt4X2NvbmQubWVhbigpOi40Zn0gc3RkPXt4X2NvbmQuc3RkKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTRCBJbmZlcmVuY2UgUGlwZWxpbmUifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIGRpZmZ1c2VycyBpbXBvcnQgU3RhYmxlRGlmZnVzaW9uUGlwZWxpbmUsIERESU1TY2hlZHVsZXJcblxuZGVmIHJ1bl9zZF9pbmZlcmVuY2UocHJvbXB0LCBuZWdfcHJvbXB0PVx1MDAyN1x1MDAyNywgbl9zdGVwcz0zMCwgZ3VpZGFuY2Vfc2NhbGU9Ny41LCBzZWVkPTQyKTpcbiAgICBcIlwiXCJSdW4gU0QgMS41OiBlbmNvZGUgcHJvbXB0IC1cdTAwM2UgZGVub2lzZSBsYXRlbnQgLVx1MDAzZSBkZWNvZGUgdG8gaW1hZ2UuXCJcIlwiXG4gICAgZGV2aWNlID0gXHUwMDI3Y3VkYVx1MDAyNyBpZiB0b3JjaC5jdWRhLmlzX2F2YWlsYWJsZSgpIGVsc2UgXHUwMDI3Y3B1XHUwMDI3XG4gICAgZHR5cGUgID0gdG9yY2guZmxvYXQxNiBpZiBkZXZpY2UgPT0gXHUwMDI3Y3VkYVx1MDAyNyBlbHNlIHRvcmNoLmZsb2F0MzJcbiAgICBwaXBlID0gU3RhYmxlRGlmZnVzaW9uUGlwZWxpbmUuZnJvbV9wcmV0cmFpbmVkKFxuICAgICAgICBcdTAwMjdydW53YXltbC9zdGFibGUtZGlmZnVzaW9uLXYxLTVcdTAwMjcsXG4gICAgICAgIHNjaGVkdWxlcj1ERElNU2NoZWR1bGVyLmZyb21fcHJldHJhaW5lZChcbiAgICAgICAgICAgIFx1MDAyN3J1bndheW1sL3N0YWJsZS1kaWZmdXNpb24tdjEtNVx1MDAyNywgc3ViZm9sZGVyPVx1MDAyN3NjaGVkdWxlclx1MDAyNyksXG4gICAgICAgIHRvcmNoX2R0eXBlPWR0eXBlLFxuICAgICkudG8oZGV2aWNlKVxuICAgIHBpcGUuc2FmZXR5X2NoZWNrZXIgPSBOb25lXG4gICAgZ2VuZXJhdG9yID0gdG9yY2guR2VuZXJhdG9yKGRldmljZT1kZXZpY2UpLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgd2l0aCB0b3JjaC5pbmZlcmVuY2VfbW9kZSgpOlxuICAgICAgICByZXN1bHQgPSBwaXBlKFxuICAgICAgICAgICAgcHJvbXB0LCBuZWdhdGl2ZV9wcm9tcHQ9bmVnX3Byb21wdCxcbiAgICAgICAgICAgIG51bV9pbmZlcmVuY2Vfc3RlcHM9bl9zdGVwcyxcbiAgICAgICAgICAgIGd1aWRhbmNlX3NjYWxlPWd1aWRhbmNlX3NjYWxlLFxuICAgICAgICAgICAgZ2VuZXJhdG9yPWdlbmVyYXRvciwgaGVpZ2h0PTUxMiwgd2lkdGg9NTEyLFxuICAgICAgICApXG4gICAgaW1nID0gcmVzdWx0LmltYWdlc1swXVxuICAgIHByaW50KGZcdTAwMjdHZW5lcmF0ZWQge2ltZy5zaXplfSB3aXRoIHtuX3N0ZXBzfSBERElNIHN0ZXBzLCBDRkc9e2d1aWRhbmNlX3NjYWxlfVx1MDAyNylcbiAgICByZXR1cm4gaW1nXG5cbiMgUGlwZWxpbmUgc3RhZ2VzIGluIG9yZGVyOlxucHJpbnQoXHUwMDI3MS4gQ0xJUCBlbmNvZGVzIHByb21wdCAtXHUwMDNlIDc3eDc2OCB0ZXh0IGVtYmVkZGluZ3NcdTAwMjcpXG5wcmludChcdTAwMjcyLiBTYW1wbGUgel9UIH4gTigwLEkpIGluIDY0eDY0eDQgbGF0ZW50IHNwYWNlXHUwMDI3KVxucHJpbnQoXHUwMDI3My4gVS1OZXQgZGVub2lzZXMgel9UIC1cdTAwM2Ugel8wIG92ZXIgMzAgRERJTSBzdGVwcyAoQ0ZHIGRvdWJsZXMgZWFjaCBzdGVwKVx1MDAyNylcbnByaW50KFx1MDAyNzQuIFZBRSBkZWNvZGVyIG1hcHMgel8wICg2NHg2NHg0KSAtXHUwMDNlIGltYWdlICg1MTJ4NTEyeDMpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbnRyb2xOZXQgSW50ZWdyYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnRyb2xOZXQgKFpoYW5nIFx1MDAyNiBBZ3Jhd2FsYSAyMDIzKSBhZGRzIHNwYXRpYWwgY29uZGl0aW9uaW5nIOKAlCBlZGdlIG1hcHMsIGRlcHRoIG1hcHMsIGh1bWFuIHBvc2Ugc2tlbGV0b25zIOKAlCB0byBhIGZyb3plbiBTRCBVLU5ldCB3aXRob3V0IHRvdWNoaW5nIHRoZSBvcmlnaW5hbCB3ZWlnaHRzLiBJdCBjb3BpZXMgdGhlIFUtTmV0IGVuY29kZXIgYmxvY2tzLCBwcm9jZXNzZXMgYSBjb25kaXRpb25pbmcgaW1hZ2UgdGhyb3VnaCB0aG9zZSBjb3BpZWQgYmxvY2tzLCBhbmQgaW5qZWN0cyB0aGUgb3V0cHV0cyBpbnRvIHRoZSBvcmlnaW5hbCBVLU5ldCBkZWNvZGVyIHZpYSBsZWFybmVkIHplcm8gY29udm9sdXRpb25zICgxw5cxIGNvbnYgaW5pdGlhbGlzZWQgdG8gemVybyB3ZWlnaHQgYW5kIGJpYXMpLiBaZXJvIGluaXRpYWxpc2F0aW9uIGVuc3VyZXMgdGhhdCBhdCB0cmFpbmluZyBzdGFydCB0aGUgQ29udHJvbE5ldCBicmFuY2ggY29udHJpYnV0ZXMgbm90aGluZywgcHJlc2VydmluZyB0aGUgYmFzZSBtb2RlbFx1MDAyN3MgYmVoYXZpb3VyIGFuZCBlbmFibGluZyBzdGFibGUgZmluZS10dW5pbmcgZnJvbSB0aGUgcHJldHJhaW5lZCBjaGVja3BvaW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSBkaWZmdXNlcnMgaW1wb3J0IFN0YWJsZURpZmZ1c2lvbkNvbnRyb2xOZXRQaXBlbGluZSwgQ29udHJvbE5ldE1vZGVsLCBVbmlQQ011bHRpc3RlcFNjaGVkdWxlclxuZnJvbSBQSUwgaW1wb3J0IEltYWdlXG5cbmNsYXNzIFplcm9Db252MmQobm4uTW9kdWxlKTpcbiAgICBcIlwiXCIxeDEgY29udiBpbml0aWFsaXNlZCB0byB6ZXJvIOKAlCBDb250cm9sTmV0IGluamVjdGlvbiBsYXllci5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgY2hhbm5lbHMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5jb252ID0gbm4uQ29udjJkKGNoYW5uZWxzLCBjaGFubmVscywgMSlcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5jb252LndlaWdodClcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5jb252LmJpYXMpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLmNvbnYoeClcblxuZGVmIGNvbnRyb2xuZXRfaW5qZWN0aW9uKHVuZXRfZmVhdCwgY3RybF9mZWF0LCB6ZXJvX2NvbnYpOlxuICAgIFwiXCJcIkFkZCBDb250cm9sTmV0IGVuY29kZXIgb3V0cHV0IChhZnRlciB6ZXJvIGNvbnYpIHRvIFUtTmV0IGRlY29kZXIgZmVhdHVyZS5cIlwiXCJcbiAgICByZXR1cm4gdW5ldF9mZWF0ICsgemVyb19jb252KGN0cmxfZmVhdClcblxuIyBEZW1vbnN0cmF0ZSB6ZXJvIGNvbnYgc3RhcnRzIGFzIGlkZW50aXR5IChjb250cmlidXRlcyBub3RoaW5nKVxuemMgPSBaZXJvQ29udjJkKGNoYW5uZWxzPTY0KVxueCA9IHRvcmNoLnJhbmRuKDIsIDY0LCAzMiwgMzIpXG5wcmludChmXHUwMDI3WmVyb0NvbnYgb3V0cHV0IG1heCBhdCBpbml0OiB7emMoeCkuYWJzKCkubWF4KCkuaXRlbSgpOi42Zn1cdTAwMjcpICAjIH4wLjBcblxuIyBDb25jZXB0dWFsIENvbnRyb2xOZXQgcGlwZWxpbmVcbnByaW50KFx1MDAyN0NvbnRyb2xOZXQgcGlwZWxpbmU6XHUwMDI3KVxucHJpbnQoXHUwMDI3ICAxLiBDYW5ueSBlZGdlIGRldGVjdG9yICAtXHUwMDNlIDUxMng1MTIgZWRnZSBtYXBcdTAwMjcpXG5wcmludChcdTAwMjcgIDIuIENvcGllZCBVLU5ldCBlbmNvZGVyIC1cdTAwM2UgaW50ZXJtZWRpYXRlIGZlYXR1cmUgbWFwc1x1MDAyNylcbnByaW50KFx1MDAyNyAgMy4gWmVybyBjb252b2x1dGlvbnMgICAgLVx1MDAzZSBzY2FsZSBmZWF0dXJlcyB0byB6ZXJvIGF0IGluaXRcdTAwMjcpXG5wcmludChcdTAwMjcgIDQuIEFkZCB0byBVLU5ldCBkZWNvZGVyIC1cdTAwM2Ugc3RydWN0dXJhbCBjb25zdHJhaW50IG9uIGdlbmVyYXRpb25cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkNob29zaW5nIHRoZSBSaWdodCBTRCBWZXJzaW9uIiwiY29udGVudCI6IkZvciBnZW5lcmFsIHRleHQtdG8taW1hZ2Ugd2l0aCA4LTE2IEdCIFZSQU06IFNEIDEuNSBydW5zIGF0IDUxMsOXNTEyLCBzdXBwb3J0cyB0aGUgd2lkZXN0IExvUkEvQ29udHJvbE5ldCBlY29zeXN0ZW0sIGFuZCBmaW5lLXR1bmVzIGluIGhvdXJzLiBTRFhMIGdpdmVzIGJlc3QgMTAyNMOXMTAyNCBxdWFsaXR5IHdpdGggYSB0d28tc3RhZ2UgcmVmaW5lciBidXQgbmVlZHMgMTYrIEdCLiBTRDMgYW5kIEZMVVggaGF2ZSBzdXBlcmlvciBwcm9tcHQgYWRoZXJlbmNlIGZvciBjb21wbGV4IHNjZW5lcyBidXQgcmVxdWlyZSAyNCsgR0IgZm9yIGZ1bGwgcXVhbGl0eS4gQWx3YXlzIG1hdGNoIHlvdXIgTG9SQSBvciBDb250cm9sTmV0IGFkYXB0ZXIgdG8gdGhlIGV4YWN0IGJhc2UgbW9kZWwgdmVyc2lvbi4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmVyc2lvbiIsIlRleHQgRW5jb2RlciIsIkxhdGVudCBDaGFubmVscyIsIkJhY2tib25lIFNpemUiLCJEZWZhdWx0IFJlc29sdXRpb24iLCJLZXkgSW1wcm92ZW1lbnQiXSwicm93cyI6W1siU0QgMS54IiwiQ0xJUCBWaVQtTC8xNCAoNzY4LWRpbSwgNzcgdG9rKSIsIjQiLCI4NjBNIFUtTmV0IiwiNTEyw5c1MTIiLCJGb3VuZGF0aW9uIGxhdGVudCBkaWZmdXNpb24gbW9kZWwiXSxbIlNEIDIueCIsIk9wZW5DTElQIFZpVC1IICgxMDI0LWRpbSkiLCI0IiwiODY1TSBVLU5ldCIsIjc2OMOXNzY4IiwiQmV0dGVyIE5TRlcgZmlsdGVyaW5nLCBkZXB0aCBtb2RlbCwgdi1wcmVkaWN0aW9uIl0sWyJTRFhMIiwiQ0xJUC1MICsgT3BlbkNMSVAtRyAoMjA0OC1kaW0pIiwiNCIsIjIuNkIgKGJhc2UrcmVmaW5lcikiLCIxMDI0w5cxMDI0IiwiRHVhbCBlbmNvZGVyLCB0d28tc3RhZ2UgcmVmaW5lciBwaXBlbGluZSJdLFsiU0QzIiwiVDUtWFhMICsgQ0xJUC1MICsgQ0xJUC1HIiwiMTYiLCJNTS1EaVQgMkIiLCIxMDI0w5cxMDI0IiwiRmxvdyBtYXRjaGluZywgbXVsdGktbW9kYWwgRGlULCAxNi1jaGFubmVsIGxhdGVudCJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUaGUgVkFFXHUwMDI3cyA4w5cgc3BhdGlhbCBjb21wcmVzc2lvbiByZWR1Y2VzIFUtTmV0IGNvbXB1dGUgYnkgNjTDlyBjb21wYXJlZCB0byBwaXhlbC1zcGFjZSBkaWZmdXNpb24uIiwiQ3Jvc3MtYXR0ZW50aW9uIGlzIGFzeW1tZXRyaWM6IFEgZGltZW5zaW9uID0gVS1OZXQgY2hhbm5lbHM7IEsvViBkaW1lbnNpb24gPSB0ZXh0IGVuY29kZXIgb3V0cHV0ICg3NjgsIDEwMjQsIG9yIDIwNDgpLiIsIkNsYXNzaWZpZXItRnJlZSBHdWlkYW5jZSBkb3VibGVzIHRoZSBVLU5ldCBmb3J3YXJkIHBhc3M6IGNvbmRpdGlvbmFsIGFuZCB1bmNvbmRpdGlvbmFsIHJ1bnMgY29tYmluZWQgYXMgzrVfY2ZnID0gzrVfdW5jb25kICsgd8K3KM61X2NvbmQg4oiSIM61X3VuY29uZCkuIiwiQ29udHJvbE5ldCB6ZXJvIGNvbnZvbHV0aW9ucyBlbnN1cmUgdGhlIHByZXRyYWluZWQgVS1OZXQgaXMgbm90IHBlcnR1cmJlZCBhdCB0cmFpbmluZyBzdGVwIDAg4oCUIHRoZSBhZGFwdGVyIGJyYW5jaCBzdGFydHMgYXMgYSBuby1vcC4iLCJTRFhMIGNvbmNhdGVuYXRlcyAobm90IGF2ZXJhZ2VzKSB0d28gdGV4dCBlbmNvZGVyIG91dHB1dHMgc28gZWFjaCBlbmNvZGVyIGNvbnRyaWJ1dGVzIGluZGVwZW5kZW50bHkgdG8gdGhlIDIwNDgtZGltIGNvbmRpdGlvbmluZy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Stable Diffusion Architecture — VAE, U-Net, and CLIP

Stable Diffusion (Rombach et al. 2022) performs diffusion in a compressed latent space rather than pixel space, reducing computation by roughly 64×. The architecture couples three independently updateable components: a KL-regularized VAE that compresses images to a 4-channel latent grid at 1/8 resolution, a CLIP text encoder that converts prompts to sequence embeddings, and a time-conditioned U-Net that iteratively denoises the latent under text guidance. Understanding how cross-attention wires text into spatial features — and how ControlNet adds structural conditioning — is essential for adapting or extending Stable Diffusion.

## Stable Diffusion Component Overview

The inference pipeline flows: encode prompt with CLIP → sample Gaussian noise z_T in latent space → run denoiser U-Net for T steps with text conditioning → decode latent z_0 with VAE decoder. The VAE encoder is used only during training, not inference. CLIP produces per-token embeddings (not a single pooled vector) so that individual tokens can attend to different spatial regions via cross-attention. The U-Net operates entirely at 1/8 pixel resolution, making 512×512 generation feasible on consumer hardware.

## VAE Encoder and Decoder

The VAE uses a KL-divergence regularisation term with a small weight (λ=1e-6) to keep the latent distribution close to a standard Gaussian while prioritising reconstruction quality. The encoder E maps H×W×3 images to (H/8)×(W/8)×4 latents: a 512×512 image becomes 64×64×4. The four latent channels provide richer per-location representation than a single channel. At encode time σ≈0, so latents are nearly deterministic. The decoder D uses symmetric residual blocks with self-attention at the bottleneck to upsample 64×64×4 back to 512×512×3.

## CLIP Text Encoder

SD 1.x uses OpenAI CLIP ViT-L/14, producing 77×768 sequence embeddings. SD 2.x uses OpenCLIP ViT-H/14 (77×1024). SDXL concatenates embeddings from CLIP-L/14 and OpenCLIP-G/14 to produce 77×2048 conditioning with richer semantics. SD3 and FLUX additionally incorporate T5-XXL for better language understanding. The entire token sequence (not just the pooled CLS embedding) is passed to cross-attention so each text token can influence different spatial positions independently.

## U-Net Denoiser and Cross-Attention

The U-Net has three paths: a downsampling encoder (ResBlocks + self-attention at lower resolutions), a bottleneck (self + cross-attention), and an upsampling decoder that receives skip connections from the encoder. Cross-attention injects text: queries Q come from flattened spatial features, keys K and values V come from CLIP embeddings. Each spatial token attends to all 77 text tokens, allowing text to control which region shows which concept. The spatial dimension of the U-Net varies by resolution level — 64×64 at the first level to 8×8 at the bottleneck.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CrossAttentionBlock(nn.Module):
    """Q from image latent features, K/V from CLIP text embeddings."""
    def __init__(self, dim_q, dim_kv, n_heads=8):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = dim_q // n_heads
        self.scale = self.head_dim ** -0.5
        self.to_q = nn.Linear(dim_q, dim_q, bias=False)
        self.to_k = nn.Linear(dim_kv, dim_q, bias=False)
        self.to_v = nn.Linear(dim_kv, dim_q, bias=False)
        self.proj = nn.Linear(dim_q, dim_q)
        self.norm_q = nn.LayerNorm(dim_q)

    def forward(self, x, context):
        B, N, C = x.shape  # N = H*W spatial tokens
        q = self.to_q(self.norm_q(x)).reshape(B, N, self.n_heads, self.head_dim).transpose(1, 2)
        k = self.to_k(context).reshape(B, -1, self.n_heads, self.head_dim).transpose(1, 2)
        v = self.to_v(context).reshape(B, -1, self.n_heads, self.head_dim).transpose(1, 2)
        attn = torch.softmax(q @ k.transpose(-2, -1) * self.scale, dim=-1)
        out = (attn @ v).transpose(1, 2).reshape(B, N, C)
        return x + self.proj(out)

block = CrossAttentionBlock(dim_q=320, dim_kv=768, n_heads=8)
x   = torch.randn(2, 64, 320)    # 8x8 spatial tokens, U-Net channels
ctx = torch.randn(2, 77, 768)   # CLIP text embeddings (SD 1.x, 768-dim)
print('Cross-attn output:', block(x, ctx).shape)  # (2, 64, 320)
```

## Timestep Embedding

The U-Net must know the current noise level t to denoise appropriately. Timestep t ∈ {0,...,T} is first encoded with sinusoidal embeddings (identical to Transformer positional encodings) then projected through a 2-layer SiLU MLP. The resulting vector conditions each residual block via Adaptive Group Normalization (AdaGN): the timestep MLP predicts per-channel scale α(t) and shift δ(t) that modulate the normalised activations before the convolution, allowing the U-Net to behave differently at every noise level.

```python
import torch
import torch.nn as nn
import math

class TimestepEmbedding(nn.Module):
    """Sinusoidal positional encoding -> MLP -> injected into ResBlocks via AdaGN."""
    def __init__(self, dim, out_dim=None):
        super().__init__()
        out_dim = out_dim or dim * 4
        self.dim = dim
        self.mlp = nn.Sequential(nn.Linear(dim, out_dim), nn.SiLU(), nn.Linear(out_dim, out_dim))

    def forward(self, t):
        half = self.dim // 2
        freqs = torch.exp(-math.log(10000) * torch.arange(half, dtype=torch.float32, device=t.device) / half)
        args = t[:, None].float() * freqs[None]
        return self.mlp(torch.cat([args.sin(), args.cos()], dim=-1))

def ada_gn_forward(x, t_emb, norm, time_proj):
    """Apply Adaptive GroupNorm: t_emb -> (scale, shift) modulate norm output."""
    scale, shift = time_proj(t_emb).chunk(2, dim=-1)
    return norm(x) * (1 + scale[:, :, None, None]) + shift[:, :, None, None]

ts = TimestepEmbedding(dim=128, out_dim=512)
t = torch.randint(0, 1000, (4,))
t_emb = ts(t)
print(f'Timestep {t.tolist()} -> embedding shape: {t_emb.shape}')  # (4, 512)

norm = nn.GroupNorm(32, 256)
time_proj = nn.Linear(512, 512)  # predicts scale+shift for 256 channels
x = torch.randn(4, 256, 16, 16)
x_cond = ada_gn_forward(x, t_emb, norm, time_proj)
print(f'After AdaGN: mean={x_cond.mean():.4f} std={x_cond.std():.4f}')
```

## SD Inference Pipeline

```python
import torch
from diffusers import StableDiffusionPipeline, DDIMScheduler

def run_sd_inference(prompt, neg_prompt='', n_steps=30, guidance_scale=7.5, seed=42):
    """Run SD 1.5: encode prompt -> denoise latent -> decode to image."""
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    dtype  = torch.float16 if device == 'cuda' else torch.float32
    pipe = StableDiffusionPipeline.from_pretrained(
        'runwayml/stable-diffusion-v1-5',
        scheduler=DDIMScheduler.from_pretrained(
            'runwayml/stable-diffusion-v1-5', subfolder='scheduler'),
        torch_dtype=dtype,
    ).to(device)
    pipe.safety_checker = None
    generator = torch.Generator(device=device).manual_seed(seed)
    with torch.inference_mode():
        result = pipe(
            prompt, negative_prompt=neg_prompt,
            num_inference_steps=n_steps,
            guidance_scale=guidance_scale,
            generator=generator, height=512, width=512,
        )
    img = result.images[0]
    print(f'Generated {img.size} with {n_steps} DDIM steps, CFG={guidance_scale}')
    return img

# Pipeline stages in order:
print('1. CLIP encodes prompt -> 77x768 text embeddings')
print('2. Sample z_T ~ N(0,I) in 64x64x4 latent space')
print('3. U-Net denoises z_T -> z_0 over 30 DDIM steps (CFG doubles each step)')
print('4. VAE decoder maps z_0 (64x64x4) -> image (512x512x3)')
```

## ControlNet Integration

ControlNet (Zhang & Agrawala 2023) adds spatial conditioning — edge maps, depth maps, human pose skeletons — to a frozen SD U-Net without touching the original weights. It copies the U-Net encoder blocks, processes a conditioning image through those copied blocks, and injects the outputs into the original U-Net decoder via learned zero convolutions (1×1 conv initialised to zero weight and bias). Zero initialisation ensures that at training start the ControlNet branch contributes nothing, preserving the base model's behaviour and enabling stable fine-tuning from the pretrained checkpoint.

```python
import torch
import torch.nn as nn
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from PIL import Image

class ZeroConv2d(nn.Module):
    """1x1 conv initialised to zero — ControlNet injection layer."""
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 1)
        nn.init.zeros_(self.conv.weight)
        nn.init.zeros_(self.conv.bias)
    def forward(self, x):
        return self.conv(x)

def controlnet_injection(unet_feat, ctrl_feat, zero_conv):
    """Add ControlNet encoder output (after zero conv) to U-Net decoder feature."""
    return unet_feat + zero_conv(ctrl_feat)

# Demonstrate zero conv starts as identity (contributes nothing)
zc = ZeroConv2d(channels=64)
x = torch.randn(2, 64, 32, 32)
print(f'ZeroConv output max at init: {zc(x).abs().max().item():.6f}')  # ~0.0

# Conceptual ControlNet pipeline
print('ControlNet pipeline:')
print('  1. Canny edge detector  -> 512x512 edge map')
print('  2. Copied U-Net encoder -> intermediate feature maps')
print('  3. Zero convolutions    -> scale features to zero at init')
print('  4. Add to U-Net decoder -> structural constraint on generation')
```

> **Choosing the Right SD Version**: For general text-to-image with 8-16 GB VRAM: SD 1.5 runs at 512×512, supports the widest LoRA/ControlNet ecosystem, and fine-tunes in hours. SDXL gives best 1024×1024 quality with a two-stage refiner but needs 16+ GB. SD3 and FLUX have superior prompt adherence for complex scenes but require 24+ GB for full quality. Always match your LoRA or ControlNet adapter to the exact base model version.

| Version | Text Encoder | Latent Channels | Backbone Size | Default Resolution | Key Improvement |
| --- | --- | --- | --- | --- | --- |
| SD 1.x | CLIP ViT-L/14 (768-dim, 77 tok) | 4 | 860M U-Net | 512×512 | Foundation latent diffusion model |
| SD 2.x | OpenCLIP ViT-H (1024-dim) | 4 | 865M U-Net | 768×768 | Better NSFW filtering, depth model, v-prediction |
| SDXL | CLIP-L + OpenCLIP-G (2048-dim) | 4 | 2.6B (base+refiner) | 1024×1024 | Dual encoder, two-stage refiner pipeline |
| SD3 | T5-XXL + CLIP-L + CLIP-G | 16 | MM-DiT 2B | 1024×1024 | Flow matching, multi-modal DiT, 16-channel latent |

- The VAE's 8× spatial compression reduces U-Net compute by 64× compared to pixel-space diffusion.
- Cross-attention is asymmetric: Q dimension = U-Net channels; K/V dimension = text encoder output (768, 1024, or 2048).
- Classifier-Free Guidance doubles the U-Net forward pass: conditional and unconditional runs combined as ε_cfg = ε_uncond + w·(ε_cond − ε_uncond).
- ControlNet zero convolutions ensure the pretrained U-Net is not perturbed at training step 0 — the adapter branch starts as a no-op.
- SDXL concatenates (not averages) two text encoder outputs so each encoder contributes independently to the 2048-dim conditioning.

---

