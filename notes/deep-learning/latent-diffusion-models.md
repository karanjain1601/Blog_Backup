---
title: "Latent Diffusion Models — Compress Then Diffuse"
slug: "latent-diffusion-models"
description: "Understand why pixel-space diffusion is computationally expensive, implement a KL-regularized VAE for image compression, run the diffusion process in 64x64 latent space instead of 512x512 pixel space, build cross-attention conditioning for text, and compare compute costs across diffusion architectures."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGF0ZW50IGRpZmZ1c2lvbiBtb2RlbHMgKExETSwgUm9tYmFjaCBldCBhbC4gMjAyMikgc29sdmUgdGhlIGZ1bmRhbWVudGFsIGNvbXB1dGUgcHJvYmxlbSBvZiBwaXhlbC1zcGFjZSBkaWZmdXNpb246IGF0IDUxMsOXNTEyIHJlc29sdXRpb24sIGVhY2ggVS1OZXQgZm9yd2FyZCBwYXNzIHByb2Nlc3NlcyA3ODYsNDMyIHZhbHVlcy4gQnkgZmlyc3QgY29tcHJlc3NpbmcgdG8gYSA2NMOXNjQgbGF0ZW50ICg0w5cgc3BhdGlhbCBkb3duc2FtcGxpbmcpLCB0aGUgZGlmZnVzaW9uIHByb2Nlc3Mgb3BlcmF0ZXMgb24gMTYsMzg0IHZhbHVlcyDigJQgYSA0OMOXIHJlZHVjdGlvbiBpbiBzcGF0aWFsIGVsZW1lbnRzLiBUaGUgc2VsZi1hdHRlbnRpb24gY29zdCBkcm9wcyBieSA0OMKyID0gMjMwNMOXLiBUaGUgYXV0b2VuY29kZXIgY29tcHJlc3Npb24gaXMgbGVhcm5lZCB0byBiZSBwZXJjZXB0dWFsIOKAlCBwcmVzZXJ2aW5nIHZpc3VhbCBpbmZvcm1hdGlvbiwgbm90IGp1c3QgcGl4ZWwgdmFsdWVzIOKAlCBzbyB0aGUgbGF0ZW50IHNwYWNlIGZhaXRoZnVsbHkgY2FwdHVyZXMgaW1hZ2UgY29udGVudCBhdCBhIGZyYWN0aW9uIG9mIHRoZSBjb21wdXRlIGNvc3QuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFBpeGVsLVNwYWNlIERpZmZ1c2lvbiBpcyBFeHBlbnNpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlUtTmV0IHNlbGYtYXR0ZW50aW9uIGhhcyBPKG7CsikgY29zdCBpbiB0aGUgbnVtYmVyIG9mIHNwYXRpYWwgcG9zaXRpb25zIG4uIEF0IDY0w5c2NCByZXNvbHV0aW9uLCBuPTQwOTY7IGF0IDUxMsOXNTEyLCBuPTI2MjE0NC4gVGhlIGF0dGVudGlvbiBjb3N0IHJhdGlvIGlzICgyNjIxNDQvNDA5NinCsiA9IDQwOTbDlyDigJQgZm91ciB0aG91c2FuZCB0aW1lcyBtb3JlIGV4cGVuc2l2ZSBhdCBmdWxsIHJlc29sdXRpb24uIEZvciBhIFQ9MTAwMCBzdGVwIEREUE0gb24gNTEyw5c1MTIgaW1hZ2VzLCBlYWNoIHRyYWluaW5nIHN0ZXAgcmVxdWlyZXMgYSBmdWxsIFUtTmV0IGZvcndhcmQgYW5kIGJhY2t3YXJkIHBhc3MgYXQgdGhpcyBjb3N0LiBQaXhlbC1zcGFjZSBtb2RlbHMgbGlrZSBEQUxMLUUgMSBhbmQgZWFybHkgRERQTSB3b3JrZWQgYXQgMjU2w5cyNTYgb3IgbG93ZXI7IGdlbmVyYXRpbmcgYXQgNTEyw5c1MTIgb3IgaGlnaGVyIHJlcXVpcmVkIGFyY2hpdGVjdHVyYWwgaW5ub3ZhdGlvbnMg4oCUIHNwZWNpZmljYWxseSwgbW92aW5nIHRvIGxhdGVudCBzcGFjZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMRE0gQXJjaGl0ZWN0dXJlIOKAlCBFbmNvZGUsIERpZmZ1c2UsIERlY29kZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIExETSBwaXBlbGluZSBoYXMgdGhyZWUgc3RhZ2VzOiAoMSkgRW5jb2RlOiBFKHgpIOKGkiB6LCBtYXBwaW5nIGEgNTEyw5c1MTIgaW1hZ2UgdG8gYSA2NMOXNjTDlzQgbGF0ZW50ICg0w5cgc3BhdGlhbCBkb3duc2FtcGxpbmcsIDPihpI0IGNoYW5uZWxzKS4gKDIpIERpZmZ1c2U6IHRyYWluIGEgVS1OZXQgzrVfzrgoel90LCB0LCBjKSBpbiB0aGUgbGF0ZW50IHNwYWNlIHog4oiIIOKEnV57NjTDlzY0w5c0fS4gKDMpIERlY29kZTogRCh6XzApIOKGkiB4LCBtYXBwaW5nIHRoZSBkZW5vaXNlZCBsYXRlbnQgYmFjayB0byBwaXhlbCBzcGFjZS4gVGhlIGF1dG9lbmNvZGVyIChFLCBEKSBpcyB0cmFpbmVkIG9uY2Ugd2l0aCBwZXJjZXB0dWFsIGxvc3MgKyBHQU4gZGlzY3JpbWluYXRvcjsgdGhlIGRpZmZ1c2lvbiBVLU5ldCBpcyB0cmFpbmVkIHNlcGFyYXRlbHkgb24gZW5jb2RlZCBsYXRlbnRzLiBBdCBpbmZlcmVuY2UsIG9ubHkgdGhlIGRpZmZ1c2lvbiBVLU5ldCBhbmQgZGVjb2RlciBhcmUgbmVlZGVkIOKAlCB0aGUgZW5jb2RlciBpcyB1c2VkIG9ubHkgZm9yIGVkaXRpbmcgb3IgaW52ZXJzaW9uIHdvcmtmbG93cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBdXRvZW5jb2RlciDigJQgVlEgYW5kIEtMIFJlZ3VsYXJpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMRE0gdXNlcyB0d28gYXV0b2VuY29kZXIgdmFyaWFudHMuIFZRLXJlZ3VsYXJpemVkIChMRE0tVlEpOiB0aGUgbGF0ZW50IGlzIHF1YW50aXplZCB0byBhIGRpc2NyZXRlIGNvZGVib29rIChWUS1WQUUgc3R5bGUpLCBwcm9kdWNpbmcgYSBzZXF1ZW5jZSBvZiBpbnRlZ2Vycy4gVGhpcyBlbmFibGVzIGF1dG9yZWdyZXNzaXZlIG1vZGVsaW5nIG9mIHRoZSBsYXRlbnQuIEtMLXJlZ3VsYXJpemVkIChMRE0tS0wpOiB0aGUgZW5jb2RlciBvdXRwdXRzIGEgR2F1c3NpYW4gZGlzdHJpYnV0aW9uIHEoenx4KSA9IE4ozrwsIM+DwrIpIHdpdGggYSBLTCBwZW5hbHR5IEtMKHEoenx4KSB8fCBOKDAsSSkpIOKAlCBhIHN0YW5kYXJkIFZBRS4gVGhlIEtMIHdlaWdodCBpcyBrZXB0IHZlcnkgc21hbGwgKGUuZy4gMcOXMTDigbvigbYpIHRvIHByaW9yaXRpemUgcmVjb25zdHJ1Y3Rpb24gcXVhbGl0eSBvdmVyIHJlZ3VsYXJpemF0aW9uLiBTdGFibGUgRGlmZnVzaW9uIHVzZXMgS0wtcmVndWxhcml6YXRpb24gd2l0aCBmPTggZG93bnNhbXBsaW5nICg1MTLihpI2NCkgYW5kIDQgbGF0ZW50IGNoYW5uZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBMRE1BdXRvZW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlNpbXBsaWZpZWQgS0wtcmVndWxhcml6ZWQgYXV0b2VuY29kZXIgZm9yIExETS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW1nX2NoPTMsIGxhdGVudF9jaD00LCBiYXNlX2NoPTMyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW1nX2NoLCBiYXNlX2NoLCA0LCAyLCAxKSwgbm4uU2lMVSgpLCAgIyAyeCBkb3duc2FtcGxlXG4gICAgICAgICAgICBubi5Db252MmQoYmFzZV9jaCwgYmFzZV9jaCoyLCA0LCAyLCAxKSwgbm4uU2lMVSgpLCAgIyA0eCBkb3duXG4gICAgICAgICAgICBubi5Db252MmQoYmFzZV9jaCoyLCBsYXRlbnRfY2gqMiwgMywgMSwgMSkgICMgbXUgYW5kIGxvZ3ZhclxuICAgICAgICApXG4gICAgICAgIHNlbGYuZGVjb2RlciA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQobGF0ZW50X2NoLCBiYXNlX2NoKjIsIDMsIDEsIDEpLCBubi5TaUxVKCksXG4gICAgICAgICAgICBubi5Db252VHJhbnNwb3NlMmQoYmFzZV9jaCoyLCBiYXNlX2NoLCA0LCAyLCAxKSwgbm4uU2lMVSgpLCAgIyAyeCB1cFxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKGJhc2VfY2gsIGltZ19jaCwgNCwgMiwgMSksIG5uLlRhbmgoKSAgIyA0eCB1cFxuICAgICAgICApXG5cbiAgICBkZWYgZW5jb2RlKHNlbGYsIHgpOlxuICAgICAgICBoID0gc2VsZi5lbmNvZGVyKHgpXG4gICAgICAgIG11LCBsb2d2YXIgPSBoLmNodW5rKDIsIGRpbT0xKVxuICAgICAgICByZXR1cm4gbXUsIGxvZ3ZhclxuXG4gICAgZGVmIHJlcGFyYW1ldGVyaXplKHNlbGYsIG11LCBsb2d2YXIpOlxuICAgICAgICBzdGQgPSB0b3JjaC5leHAoMC41ICogbG9ndmFyKVxuICAgICAgICByZXR1cm4gbXUgKyBzdGQgKiB0b3JjaC5yYW5kbl9saWtlKHN0ZClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIGtsX3dlaWdodD0xZS00KTpcbiAgICAgICAgbXUsIGxvZ3ZhciA9IHNlbGYuZW5jb2RlKHgpXG4gICAgICAgIHogPSBzZWxmLnJlcGFyYW1ldGVyaXplKG11LCBsb2d2YXIpXG4gICAgICAgIHJlY29uID0gc2VsZi5kZWNvZGVyKHopXG4gICAgICAgIHJlY29uX2xvc3MgPSBGLm1zZV9sb3NzKHJlY29uLCB4KVxuICAgICAgICBrbF9sb3NzID0gLTAuNSAqICgxICsgbG9ndmFyIC0gbXUucG93KDIpIC0gbG9ndmFyLmV4cCgpKS5tZWFuKClcbiAgICAgICAgcmV0dXJuIHJlY29uLCByZWNvbl9sb3NzICsga2xfd2VpZ2h0ICoga2xfbG9zc1xuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuYXV0b2VuYyA9IExETUF1dG9lbmNvZGVyKClcbnggPSB0b3JjaC5yYW5kbigyLCAzLCAzMiwgMzIpICAjIGJhdGNoIG9mIDMyeDMyIGltYWdlc1xucmVjb24sIGxvc3MgPSBhdXRvZW5jKHgpXG5wcmludChmXHUwMDI3SW5wdXQ6IHt4LnNoYXBlfSwgTGF0ZW50OiB7YXV0b2VuYy5lbmNvZGUoeClbMF0uc2hhcGV9LCBSZWNvbjoge3JlY29uLnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdBRSBsb3NzOiB7bG9zcy5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEaWZmdXNpb24gaW4gTGF0ZW50IFNwYWNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPbmNlIHRoZSBhdXRvZW5jb2RlciBpcyB0cmFpbmVkLCB0aGUgbGF0ZW50IHNwYWNlIHogPSBFKHgpIHJlcGxhY2VzIHRoZSBwaXhlbCBzcGFjZSBmb3IgdGhlIGRpZmZ1c2lvbiBwcm9jZXNzLiBUaGUgbGF0ZW50cyBhcmUgc2NhbGVkIHRvIHVuaXQgdmFyaWFuY2UgYmVmb3JlIGRpZmZ1c2lvbiB0cmFpbmluZyAoel9zY2FsZWQgPSB6IC8gc3RkKHpfdHJhaW4pKSwgd2hpY2ggZW5zdXJlcyB0aGUgbm9pc2Ugc2NoZWR1bGUgaXMgbWVhbmluZ2Z1bC4gVGhlIFUtTmV0IM61X864KHpfdCwgdCwgYykgcHJvY2Vzc2VzIDY0w5c2NMOXNCB0ZW5zb3JzIGluc3RlYWQgb2YgNTEyw5c1MTLDlzMg4oCUIGEgMTbDlyByZWR1Y3Rpb24gaW4gc3BhdGlhbCBhcmVhLiBUaGUgcmVzdWx0aW5nIG1vZGVsIHRyYWlucyA04oCTMTbDlyBmYXN0ZXIgcGVyIHN0ZXAgYW5kIGNhbiBydW4gaW5mZXJlbmNlIGluIHNlY29uZHMgcmF0aGVyIHRoYW4gbWludXRlcy4gQ3J1Y2lhbGx5LCB0aGUgcGVyY2VwdHVhbCBjb21wcmVzc2lvbiBieSB0aGUgYXV0b2VuY29kZXIgbWVhbnMgNjTDlzY0IGxhdGVudHMgY2FwdHVyZSB0aGUgc2FtZSB2aXN1YWwgY29udGVudCBhcyA1MTLDlzUxMiBwaXhlbHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIExhdGVudFVOZXQobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTaW1wbGlmaWVkIFUtTmV0IGZvciBkaWZmdXNpb24gaW4gbGF0ZW50IHNwYWNlIChubyBzcGF0aWFsIGF0dGVudGlvbiBzaG93bikuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGxhdGVudF9jaD00LCBoaWRkZW49NjQsIFQ9MTAwMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnRpbWVfZW1iZWQgPSBubi5FbWJlZGRpbmcoVCwgMzIpXG4gICAgICAgIHNlbGYuZG93bjEgPSBubi5Db252MmQobGF0ZW50X2NoLCBoaWRkZW4sIDMsIDEsIDEpXG4gICAgICAgIHNlbGYuZG93bjIgPSBubi5Db252MmQoaGlkZGVuLCBoaWRkZW4qMiwgNCwgMiwgMSkgICMgMzJ4MzJcbiAgICAgICAgc2VsZi5taWQgICA9IG5uLkNvbnYyZChoaWRkZW4qMiArIDMyLCBoaWRkZW4qMiwgMywgMSwgMSlcbiAgICAgICAgc2VsZi51cDEgICA9IG5uLkNvbnZUcmFuc3Bvc2UyZChoaWRkZW4qMiwgaGlkZGVuLCA0LCAyLCAxKVxuICAgICAgICBzZWxmLm91dCAgID0gbm4uQ29udjJkKGhpZGRlbiArIGhpZGRlbiwgbGF0ZW50X2NoLCAzLCAxLCAxKVxuICAgICAgICBzZWxmLmFjdCAgID0gbm4uU2lMVSgpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB6X3QsIHQpOlxuICAgICAgICBCLCBDLCBILCBXID0gel90LnNoYXBlXG4gICAgICAgIHRfZW1iID0gc2VsZi50aW1lX2VtYmVkKHQpWzosIDosIE5vbmUsIE5vbmVdLmV4cGFuZChCLCAzMiwgSC8vMiwgVy8vMilcbiAgICAgICAgaDEgPSBzZWxmLmFjdChzZWxmLmRvd24xKHpfdCkpICAgICAgICAgICAgICMgKEIsIDY0LCBILCBXKVxuICAgICAgICBoMiA9IHNlbGYuYWN0KHNlbGYuZG93bjIoaDEpKSAgICAgICAgICAgICAgIyAoQiwgMTI4LCBILzIsIFcvMilcbiAgICAgICAgaF9taWQgPSBzZWxmLmFjdChzZWxmLm1pZCh0b3JjaC5jYXQoW2gyLCB0X2VtYl0sIGRpbT0xKSkpXG4gICAgICAgIGhfdXAgPSBzZWxmLmFjdChzZWxmLnVwMShoX21pZCkpICAgICAgICAgICAjIChCLCA2NCwgSCwgVylcbiAgICAgICAgcmV0dXJuIHNlbGYub3V0KHRvcmNoLmNhdChbaF91cCwgaDFdLCBkaW09MSkpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5hbHBoYV9iYXIgPSB0b3JjaC5jdW1wcm9kKDEgLSB0b3JjaC5saW5zcGFjZSgxZS00LCAwLjAyLCAxMDAwKSwgZGltPTApXG51bmV0ID0gTGF0ZW50VU5ldCgpXG56ID0gdG9yY2gucmFuZG4oMiwgNCwgMTYsIDE2KSAgIyBsYXRlbnQgYXQgMTZ4MTYgKHRveSBzY2FsZSlcbnQgPSB0b3JjaC5yYW5kaW50KDAsIDEwMDAsICgyLCkpXG5hYiA9IGFscGhhX2Jhclt0XVs6LCBOb25lLCBOb25lLCBOb25lXVxuZXBzID0gdG9yY2gucmFuZG5fbGlrZSh6KVxuel90ID0gdG9yY2guc3FydChhYikgKiB6ICsgdG9yY2guc3FydCgxIC0gYWIpICogZXBzXG5lcHNfcHJlZCA9IHVuZXQoel90LCB0KVxubG9zcyA9IEYubXNlX2xvc3MoZXBzX3ByZWQsIGVwcylcbnByaW50KGZcdTAwMjdMYXRlbnQgejoge3ouc2hhcGV9LCBOb2lzeSB6X3Q6IHt6X3Quc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0RpZmZ1c2lvbiBsb3NzIGluIGxhdGVudCBzcGFjZToge2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtQXR0ZW50aW9uIENvbmRpdGlvbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTERNIGNvbmRpdGlvbnMgdGhlIFUtTmV0IG9uIHRleHQsIGNsYXNzIGxhYmVscywgb3Igb3RoZXIgc2lnbmFscyB2aWEgY3Jvc3MtYXR0ZW50aW9uLiBBdCBlYWNoIFUtTmV0IHJlc29sdXRpb24sIGltYWdlIGZlYXR1cmUgbWFwcyBhcmUgZmxhdHRlbmVkIHRvIHF1ZXJpZXMgUSA9IFdfUcK3z4Yoel90KSwgYW5kIHRoZSBjb25kaXRpb24gKGUuZy4gQ0xJUCB0ZXh0IGVtYmVkZGluZykgaXMgcHJvamVjdGVkIHRvIGtleXMgSyA9IFdfS8K3z4RfzrgoYykgYW5kIHZhbHVlcyBWID0gV19WwrfPhF/OuChjKS4gVGhlIGF0dGVudGlvbiBvdXRwdXQgQXR0ZW50aW9uKFEsSyxWKSA9IHNvZnRtYXgoUUteVC/iiJpkKcK3ViBpcyBhZGRlZCBiYWNrIHRvIHRoZSBpbWFnZSBmZWF0dXJlcy4gVGhpcyBjcm9zcy1hdHRlbnRpb24gbWVjaGFuaXNtIGlzIHNwYXRpYWw6IGVhY2ggaW1hZ2UgcGF0Y2ggYXR0ZW5kcyB0byB0aGUgZnVsbCB0ZXh0IHNlcXVlbmNlLCBwcm9kdWNpbmcgc3BhdGlhbGx5IHZhcmlhYmxlIGNvbmRpdGlvbmluZy4gVGhlIGF0dGVudGlvbiBtYXBzIGFyZSBpbnRlcnByZXRhYmxlIOKAlCB0aGV5IHNob3cgd2hpY2ggaW1hZ2UgcmVnaW9ucyBlYWNoIHRleHQgdG9rZW4gaW5mbHVlbmNlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgU3BhdGlhbENyb3NzQXR0ZW50aW9uKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiQ3Jvc3MtYXR0ZW50aW9uOiBpbWFnZSBsYXRlbnRzIChRKSBhdHRlbmQgdG8gdGV4dCBmZWF0dXJlcyAoSywgVikuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGxhdGVudF9kaW09NjQsIGNvbnRleHRfZGltPTMyLCBuX2hlYWRzPTQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uX2hlYWRzID0gbl9oZWFkc1xuICAgICAgICBzZWxmLmhlYWRfZGltID0gbGF0ZW50X2RpbSAvLyBuX2hlYWRzXG4gICAgICAgIHNlbGYudG9fcSA9IG5uLkxpbmVhcihsYXRlbnRfZGltLCBsYXRlbnRfZGltKVxuICAgICAgICBzZWxmLnRvX2sgPSBubi5MaW5lYXIoY29udGV4dF9kaW0sIGxhdGVudF9kaW0pXG4gICAgICAgIHNlbGYudG9fdiA9IG5uLkxpbmVhcihjb250ZXh0X2RpbSwgbGF0ZW50X2RpbSlcbiAgICAgICAgc2VsZi50b19vdXQgPSBubi5MaW5lYXIobGF0ZW50X2RpbSwgbGF0ZW50X2RpbSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIGNvbnRleHQpOlxuICAgICAgICBCLCBTLCBEID0geC5zaGFwZVxuICAgICAgICBUX2N0eCA9IGNvbnRleHQuc2hhcGVbMV1cbiAgICAgICAgSCA9IHNlbGYubl9oZWFkc1xuICAgICAgICBkZWYgcmVzaGFwZSh0KTogcmV0dXJuIHQudmlldyhCLCAtMSwgSCwgc2VsZi5oZWFkX2RpbSkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIFEgPSByZXNoYXBlKHNlbGYudG9fcSh4KSlcbiAgICAgICAgSyA9IHJlc2hhcGUoc2VsZi50b19rKGNvbnRleHQpKVxuICAgICAgICBWID0gcmVzaGFwZShzZWxmLnRvX3YoY29udGV4dCkpXG4gICAgICAgIGF0dG4gPSBGLnNvZnRtYXgoUSBAIEsudHJhbnNwb3NlKC0yLC0xKSAvIHNlbGYuaGVhZF9kaW0qKjAuNSwgZGltPS0xKVxuICAgICAgICBvdXQgPSAoYXR0biBAIFYpLnRyYW5zcG9zZSgxLDIpLnJlc2hhcGUoQiwgUywgRClcbiAgICAgICAgcmV0dXJuIHNlbGYudG9fb3V0KG91dCksIGF0dG5cblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIFMsIFRfY3R4ID0gMiwgNjQsIDEyICAjIDIgc2FtcGxlcywgNjQgc3BhdGlhbCB0b2tlbnMsIDEyIHRleHQgdG9rZW5zXG5sYXRlbnRfdG9rZW5zID0gdG9yY2gucmFuZG4oQiwgUywgNjQpXG50ZXh0X2ZlYXRzID0gdG9yY2gucmFuZG4oQiwgVF9jdHgsIDMyKVxueGF0dG4gPSBTcGF0aWFsQ3Jvc3NBdHRlbnRpb24oKVxub3V0LCBhdHRuX21hcHMgPSB4YXR0bihsYXRlbnRfdG9rZW5zLCB0ZXh0X2ZlYXRzKVxucHJpbnQoZlx1MDAyN0xhdGVudCB0b2tlbnM6IHtsYXRlbnRfdG9rZW5zLnNoYXBlfSAtXHUwMDNlIG91dHB1dDoge291dC5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3QXR0ZW50aW9uIG1hcHM6IHthdHRuX21hcHMuc2hhcGV9ICAoQiwgaGVhZHMsIHNwYXRpYWwsIHRleHRfdG9rZW5zKVx1MDAyNylcbnByaW50KGZcdTAwMjdBdHRlbnRpb24gc3VtIG92ZXIgdGV4dDoge2F0dG5fbWFwc1swLCAwLCA6MywgOl0uc3VtKGRpbT0tMSkudG9saXN0KCl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0YWJsZSBEaWZmdXNpb24gYXMgTERNIEluc3RhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFibGUgRGlmZnVzaW9uIChSb21iYWNoIGV0IGFsLiAyMDIyKSBpcyBhbiBMRE0gd2l0aDogKDEpIENMSVAgVmlULUwvMTQgdGV4dCBlbmNvZGVyICg3NjgtZGltIGVtYmVkZGluZ3MsIHVwIHRvIDc3IHRva2Vucyk7ICgyKSBLTC1yZWd1bGFyaXplZCBhdXRvZW5jb2RlciB3aXRoIGY9OCBkb3duc2FtcGxpbmcgKDUxMsOXNTEyIOKGkiA2NMOXNjTDlzQgbGF0ZW50cyk7ICgzKSBVLU5ldCB3aXRoIGNyb3NzLWF0dGVudGlvbiBjb25kaXRpb25pbmcgYXQgMzLDlzMyLCAxNsOXMTYsIGFuZCA4w5c4IHJlc29sdXRpb25zOyAoNCkgQ0ZHIGF0IGluZmVyZW5jZSAod+KJiDcuNSkuIFRyYWluaW5nIHVzZWQgTEFJT04tNUIgKDVCIGltYWdlLXRleHQgcGFpcnMpLiBUaGUgbGF0ZW50IHNwYWNlIGRpbWVuc2lvbmFsaXR5IHJlZHVjdGlvbiAoNjTDlzY0w5c0IHZzIDUxMsOXNTEyw5czKSBlbmFibGVzIHRyYWluaW5nIG9uIGNvbnN1bWVyIEdQVXMgKDI0R0IgVlJBTSBmb3IgYmF0Y2ggc2l6ZSA0KSBhdCBhIGNvc3QgfjUww5cgbG93ZXIgdGhhbiBwaXhlbC1zcGFjZSBlcXVpdmFsZW50cy4gU0QgdjEuNSBoYXMgODYwTSBwYXJhbWV0ZXJzIGluIHRoZSBVLU5ldDsgU0RYTCBoYXMgMi42Qi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQaXhlbC1TcGFjZSB2cyBMYXRlbnQgRGlmZnVzaW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRpbWVcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZXN0aW1hdGVfZmxvcHNfYW5kX3RpbWUocmVzb2x1dGlvbiwgbGF0ZW50X2ZhY3Rvcj0xLCBiYXRjaD0xLCBuX3N0ZXBzPTUwKTpcbiAgICBcIlwiXCJSb3VnaCBlc3RpbWF0ZSBvZiBkaWZmdXNpb24gaW5mZXJlbmNlIGNvc3QgYXQgZGlmZmVyZW50IHJlc29sdXRpb25zLlwiXCJcIlxuICAgIHNwYXRpYWwgPSAocmVzb2x1dGlvbiAvLyBsYXRlbnRfZmFjdG9yKSAqKiAyXG4gICAgIyBTZWxmLWF0dGVudGlvbiBjb3N0IE8oc3BhdGlhbF4yICogY2hhbm5lbHMpXG4gICAgYXR0bl9jb3N0ID0gc3BhdGlhbCAqKiAyICogNjQgICMgcHJvcG9ydGlvbmFsXG4gICAgIyBDb252IGNvc3QgTyhzcGF0aWFsICogY2hhbm5lbHNeMiAqIGtlcm5lbF4yKVxuICAgIGNvbnZfY29zdCA9IHNwYXRpYWwgKiA2NCoqMiAqIDlcbiAgICBzdGVwX2Nvc3QgPSAoYXR0bl9jb3N0ICsgY29udl9jb3N0KSAvIDFlOSAgIyBpbiBHRkxPUHMgKGFwcHJveClcbiAgICB0b3RhbF9nZmxvcHMgPSBzdGVwX2Nvc3QgKiBuX3N0ZXBzICogYmF0Y2hcblxuICAgIG1vZGUgPSBcdTAwMjdwaXhlbC1zcGFjZVx1MDAyNyBpZiBsYXRlbnRfZmFjdG9yID09IDEgZWxzZSBmXHUwMDI3bGF0ZW50IChmPXtsYXRlbnRfZmFjdG9yfSlcdTAwMjdcbiAgICBwcmludChmXHUwMDI3e21vZGU6MjBzfSB8IHJlcz17cmVzb2x1dGlvbi8vbGF0ZW50X2ZhY3RvcjozZH14e3Jlc29sdXRpb24vL2xhdGVudF9mYWN0b3I6M2R9IFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjd8IGF0dG4gY29zdDoge2F0dG5fY29zdC8xZTY6Ny4xZn1NIHwgdG90YWwgR0ZMT1BzOiB7dG90YWxfZ2Zsb3BzOi4xZn1cdTAwMjcpXG4gICAgcmV0dXJuIHRvdGFsX2dmbG9wc1xuXG5wcmludChmXHUwMDI3e1wiTW9kZVwiOjIwc30gfCB7XCJMYXRlbnQgcmVzXCI6MTJzfSB8IHtcIkF0dG4gY29zdFwiOjEzc30gfCB7XCJHRkxPUHMgKDUwIHN0ZXBzKVwifVx1MDAyNyApXG5wcmludChcdTAwMjctXHUwMDI3ICogNzIpXG5mb3IgcmVzLCBmIGluIFsoNTEyLCAxKSwgKDUxMiwgNCksICg1MTIsIDgpLCAoMTAyNCwgOCldOlxuICAgIGVzdGltYXRlX2Zsb3BzX2FuZF90aW1lKHJlcywgbGF0ZW50X2ZhY3Rvcj1mKVxucHJpbnQoKVxucHJpbnQoXHUwMDI3TGF0ZW50IGY9OCByZWR1Y2VzIGF0dGVudGlvbiBjb3N0IGJ5IDY0XjIgPSA0MDk2eCB2cyBwaXhlbC1zcGFjZSBhdCA1MTJ4NTEyXHUwMDI3KSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIkxhdGVudCB0eXBlIiwiUmVzb2x1dGlvbiIsIkxhdGVudCBzaXplIiwiQ29uZGl0aW9uIHR5cGUiLCJUcmFpbmluZyBjb21wdXRlIl0sInJvd3MiOltbIkREUE0gKEhvIGV0IGFsLiAyMDIwKSIsIk5vbmUg4oCUIHBpeGVsIHNwYWNlIiwiMjU2w5cyNTYiLCIyNTbDlzI1NsOXMyBwaXhlbHMiLCJDbGFzcyBsYWJlbCAoZW1iZWQpIiwiSGlnaCDigJQgcGl4ZWwgVS1OZXQiXSxbIkxETSAoUm9tYmFjaCBldCBhbC4gMjAyMikiLCJLTC1WQUUgb3IgVlEtVkFFIiwiMjU24oCTNTEyw5cyNTbigJM1MTIiLCIzMuKAkzY0w5czMuKAkzY0w5c0IiwiVGV4dC9jbGFzcyB2aWEgY3Jvc3MtYXR0biIsIn404oCTMTbDlyBjaGVhcGVyIHRoYW4gcGl4ZWwiXSxbIlN0YWJsZSBEaWZmdXNpb24gMS41IiwiS0wtVkFFIGY9OCIsIjUxMsOXNTEyIiwiNjTDlzY0w5c0IiwiQ0xJUCBWaVQtTC8xNCB0ZXh0IiwifjUww5cgY2hlYXBlciB0aGFuIHBpeGVsIFNEIl0sWyJEQUxMLUUgMyAvIFNEWEwiLCJLTC1WQUUgZj04IiwiMTAyNMOXMTAyNCIsIjEyOMOXMTI4w5c0IiwiVDUgLyBDTElQIGR1YWwgdGV4dCBlbmNvZGVyIiwifjIwMMOXIGNoZWFwZXIgdGhhbiBuYWl2ZSBwaXhlbCJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJXaHkgTGF0ZW50IFNwYWNlIFdvcmtzIGZvciBEaWZmdXNpb24iLCJjb250ZW50IjoiQSBwZXJjZXB0dWFsbHktdHJhaW5lZCBhdXRvZW5jb2RlciAodXNpbmcgTFBJUFMgbG9zcyArIEdBTiBkaXNjcmltaW5hdG9yKSBjb21wcmVzc2VzIGltYWdlcyBpbnRvIGxhdGVudHMgdGhhdCBwcmVzZXJ2ZSBzZW1hbnRpYyBhbmQgc3RydWN0dXJhbCBpbmZvcm1hdGlvbiB3aGlsZSBkaXNjYXJkaW5nIGhpZ2gtZnJlcXVlbmN5IHBpeGVsIG5vaXNlLiBEaWZmdXNpb24gaW4gdGhpcyBwZXJjZXB0dWFsIGxhdGVudCBzcGFjZSBpcyBlZmZpY2llbnQgYmVjYXVzZSB0aGUgbGF0ZW50IHNwYWNlIGlzIHNlbWFudGljYWxseSBzbW9vdGgg4oCUIHNtYWxsIGxhdGVudCBjaGFuZ2VzIGNvcnJlc3BvbmQgdG8gc2VtYW50aWNhbGx5IG1lYW5pbmdmdWwgaW1hZ2UgY2hhbmdlcywgbWFraW5nIHRoZSBzY29yZSBmaWVsZCBlYXNpZXIgdG8gbGVhcm4uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQaXhlbC1zcGFjZSBzZWxmLWF0dGVudGlvbiBhdCA1MTLDlzUxMiBjb3N0cyA0MDk2w5cgbW9yZSB0aGFuIGF0IDY0w5c2NCDigJQgdGhlIHByaW1hcnkgbW90aXZhdGlvbiBmb3IgbGF0ZW50IGRpZmZ1c2lvbi4iLCJLTC1yZWd1bGFyaXplZCBhdXRvZW5jb2Rlcjogc21hbGwgS0wgd2VpZ2h0ICgxZS02KSBwcmlvcml0aXplcyByZWNvbnN0cnVjdGlvbiBmaWRlbGl0eSBvdmVyIHBvc3RlcmlvciByZWd1bGFyaXphdGlvbi4iLCJMYXRlbnQgc2NhbGluZzogZGl2aWRlIGxhdGVudHMgYnkgc3RkIG9mIHRoZSB0cmFpbmluZyBzZXQgYmVmb3JlIGRpZmZ1c2lvbiB0cmFpbmluZyB0byBtYXRjaCB0aGUgbm9pc2Ugc2NoZWR1bGUgYXNzdW1wdGlvbnMuIiwiQ3Jvc3MtYXR0ZW50aW9uIGF0IG11bHRpcGxlIFUtTmV0IHJlc29sdXRpb25zICgzMsOXMzIsIDE2w5cxNiwgOMOXOCkgZW5hYmxlcyBzcGF0aWFsbHktZ3JvdW5kZWQgdGV4dCBjb25kaXRpb25pbmcuIiwiU3RhYmxlIERpZmZ1c2lvbiA9IExETSArIENMSVAgdGV4dCBlbmNvZGVyICsgQ0ZHIOKAlCBlYWNoIGNvbXBvbmVudCBpcyBpbmRlcGVuZGVudGx5IHJlcGxhY2VhYmxlLiIsIlNEWEwgaW1wcm92ZXMgYnkgdXNpbmcgdHdvIENMSVAgZW5jb2RlcnMgKFZpVC1MIGFuZCBWaVQtRyksIGluY3JlYXNpbmcgdGV4dCBjYXBhY2l0eSBmcm9tIDc2OCB0byAyMDQ4IGRpbXMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Latent Diffusion Models — Compress Then Diffuse

Latent diffusion models (LDM, Rombach et al. 2022) solve the fundamental compute problem of pixel-space diffusion: at 512×512 resolution, each U-Net forward pass processes 786,432 values. By first compressing to a 64×64 latent (4× spatial downsampling), the diffusion process operates on 16,384 values — a 48× reduction in spatial elements. The self-attention cost drops by 48² = 2304×. The autoencoder compression is learned to be perceptual — preserving visual information, not just pixel values — so the latent space faithfully captures image content at a fraction of the compute cost.

## Why Pixel-Space Diffusion is Expensive

U-Net self-attention has O(n²) cost in the number of spatial positions n. At 64×64 resolution, n=4096; at 512×512, n=262144. The attention cost ratio is (262144/4096)² = 4096× — four thousand times more expensive at full resolution. For a T=1000 step DDPM on 512×512 images, each training step requires a full U-Net forward and backward pass at this cost. Pixel-space models like DALL-E 1 and early DDPM worked at 256×256 or lower; generating at 512×512 or higher required architectural innovations — specifically, moving to latent space.

## LDM Architecture — Encode, Diffuse, Decode

The LDM pipeline has three stages: (1) Encode: E(x) → z, mapping a 512×512 image to a 64×64×4 latent (4× spatial downsampling, 3→4 channels). (2) Diffuse: train a U-Net ε_θ(z_t, t, c) in the latent space z ∈ ℝ^{64×64×4}. (3) Decode: D(z_0) → x, mapping the denoised latent back to pixel space. The autoencoder (E, D) is trained once with perceptual loss + GAN discriminator; the diffusion U-Net is trained separately on encoded latents. At inference, only the diffusion U-Net and decoder are needed — the encoder is used only for editing or inversion workflows.

## Autoencoder — VQ and KL Regularization

LDM uses two autoencoder variants. VQ-regularized (LDM-VQ): the latent is quantized to a discrete codebook (VQ-VAE style), producing a sequence of integers. This enables autoregressive modeling of the latent. KL-regularized (LDM-KL): the encoder outputs a Gaussian distribution q(z|x) = N(μ, σ²) with a KL penalty KL(q(z|x) || N(0,I)) — a standard VAE. The KL weight is kept very small (e.g. 1×10⁻⁶) to prioritize reconstruction quality over regularization. Stable Diffusion uses KL-regularization with f=8 downsampling (512→64) and 4 latent channels.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LDMAutoencoder(nn.Module):
    """Simplified KL-regularized autoencoder for LDM."""
    def __init__(self, img_ch=3, latent_ch=4, base_ch=32):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(img_ch, base_ch, 4, 2, 1), nn.SiLU(),  # 2x downsample
            nn.Conv2d(base_ch, base_ch*2, 4, 2, 1), nn.SiLU(),  # 4x down
            nn.Conv2d(base_ch*2, latent_ch*2, 3, 1, 1)  # mu and logvar
        )
        self.decoder = nn.Sequential(
            nn.Conv2d(latent_ch, base_ch*2, 3, 1, 1), nn.SiLU(),
            nn.ConvTranspose2d(base_ch*2, base_ch, 4, 2, 1), nn.SiLU(),  # 2x up
            nn.ConvTranspose2d(base_ch, img_ch, 4, 2, 1), nn.Tanh()  # 4x up
        )

    def encode(self, x):
        h = self.encoder(x)
        mu, logvar = h.chunk(2, dim=1)
        return mu, logvar

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        return mu + std * torch.randn_like(std)

    def forward(self, x, kl_weight=1e-4):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        recon = self.decoder(z)
        recon_loss = F.mse_loss(recon, x)
        kl_loss = -0.5 * (1 + logvar - mu.pow(2) - logvar.exp()).mean()
        return recon, recon_loss + kl_weight * kl_loss

torch.manual_seed(0)
autoenc = LDMAutoencoder()
x = torch.randn(2, 3, 32, 32)  # batch of 32x32 images
recon, loss = autoenc(x)
print(f'Input: {x.shape}, Latent: {autoenc.encode(x)[0].shape}, Recon: {recon.shape}')
print(f'AE loss: {loss.item():.4f}')
```

## Diffusion in Latent Space

Once the autoencoder is trained, the latent space z = E(x) replaces the pixel space for the diffusion process. The latents are scaled to unit variance before diffusion training (z_scaled = z / std(z_train)), which ensures the noise schedule is meaningful. The U-Net ε_θ(z_t, t, c) processes 64×64×4 tensors instead of 512×512×3 — a 16× reduction in spatial area. The resulting model trains 4–16× faster per step and can run inference in seconds rather than minutes. Crucially, the perceptual compression by the autoencoder means 64×64 latents capture the same visual content as 512×512 pixels.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LatentUNet(nn.Module):
    """Simplified U-Net for diffusion in latent space (no spatial attention shown)."""
    def __init__(self, latent_ch=4, hidden=64, T=1000):
        super().__init__()
        self.time_embed = nn.Embedding(T, 32)
        self.down1 = nn.Conv2d(latent_ch, hidden, 3, 1, 1)
        self.down2 = nn.Conv2d(hidden, hidden*2, 4, 2, 1)  # 32x32
        self.mid   = nn.Conv2d(hidden*2 + 32, hidden*2, 3, 1, 1)
        self.up1   = nn.ConvTranspose2d(hidden*2, hidden, 4, 2, 1)
        self.out   = nn.Conv2d(hidden + hidden, latent_ch, 3, 1, 1)
        self.act   = nn.SiLU()

    def forward(self, z_t, t):
        B, C, H, W = z_t.shape
        t_emb = self.time_embed(t)[:, :, None, None].expand(B, 32, H//2, W//2)
        h1 = self.act(self.down1(z_t))             # (B, 64, H, W)
        h2 = self.act(self.down2(h1))              # (B, 128, H/2, W/2)
        h_mid = self.act(self.mid(torch.cat([h2, t_emb], dim=1)))
        h_up = self.act(self.up1(h_mid))           # (B, 64, H, W)
        return self.out(torch.cat([h_up, h1], dim=1))

torch.manual_seed(0)
alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
unet = LatentUNet()
z = torch.randn(2, 4, 16, 16)  # latent at 16x16 (toy scale)
t = torch.randint(0, 1000, (2,))
ab = alpha_bar[t][:, None, None, None]
eps = torch.randn_like(z)
z_t = torch.sqrt(ab) * z + torch.sqrt(1 - ab) * eps
eps_pred = unet(z_t, t)
loss = F.mse_loss(eps_pred, eps)
print(f'Latent z: {z.shape}, Noisy z_t: {z_t.shape}')
print(f'Diffusion loss in latent space: {loss.item():.4f}')
```

## Cross-Attention Conditioning

LDM conditions the U-Net on text, class labels, or other signals via cross-attention. At each U-Net resolution, image feature maps are flattened to queries Q = W_Q·φ(z_t), and the condition (e.g. CLIP text embedding) is projected to keys K = W_K·τ_θ(c) and values V = W_V·τ_θ(c). The attention output Attention(Q,K,V) = softmax(QK^T/√d)·V is added back to the image features. This cross-attention mechanism is spatial: each image patch attends to the full text sequence, producing spatially variable conditioning. The attention maps are interpretable — they show which image regions each text token influences.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SpatialCrossAttention(nn.Module):
    """Cross-attention: image latents (Q) attend to text features (K, V)."""
    def __init__(self, latent_dim=64, context_dim=32, n_heads=4):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = latent_dim // n_heads
        self.to_q = nn.Linear(latent_dim, latent_dim)
        self.to_k = nn.Linear(context_dim, latent_dim)
        self.to_v = nn.Linear(context_dim, latent_dim)
        self.to_out = nn.Linear(latent_dim, latent_dim)

    def forward(self, x, context):
        B, S, D = x.shape
        T_ctx = context.shape[1]
        H = self.n_heads
        def reshape(t): return t.view(B, -1, H, self.head_dim).transpose(1, 2)
        Q = reshape(self.to_q(x))
        K = reshape(self.to_k(context))
        V = reshape(self.to_v(context))
        attn = F.softmax(Q @ K.transpose(-2,-1) / self.head_dim**0.5, dim=-1)
        out = (attn @ V).transpose(1,2).reshape(B, S, D)
        return self.to_out(out), attn

torch.manual_seed(0)
B, S, T_ctx = 2, 64, 12  # 2 samples, 64 spatial tokens, 12 text tokens
latent_tokens = torch.randn(B, S, 64)
text_feats = torch.randn(B, T_ctx, 32)
xattn = SpatialCrossAttention()
out, attn_maps = xattn(latent_tokens, text_feats)
print(f'Latent tokens: {latent_tokens.shape} -> output: {out.shape}')
print(f'Attention maps: {attn_maps.shape}  (B, heads, spatial, text_tokens)')
print(f'Attention sum over text: {attn_maps[0, 0, :3, :].sum(dim=-1).tolist()}')
```

## Stable Diffusion as LDM Instance

Stable Diffusion (Rombach et al. 2022) is an LDM with: (1) CLIP ViT-L/14 text encoder (768-dim embeddings, up to 77 tokens); (2) KL-regularized autoencoder with f=8 downsampling (512×512 → 64×64×4 latents); (3) U-Net with cross-attention conditioning at 32×32, 16×16, and 8×8 resolutions; (4) CFG at inference (w≈7.5). Training used LAION-5B (5B image-text pairs). The latent space dimensionality reduction (64×64×4 vs 512×512×3) enables training on consumer GPUs (24GB VRAM for batch size 4) at a cost ~50× lower than pixel-space equivalents. SD v1.5 has 860M parameters in the U-Net; SDXL has 2.6B.

## Pixel-Space vs Latent Diffusion

```python
import torch
import time
import numpy as np

def estimate_flops_and_time(resolution, latent_factor=1, batch=1, n_steps=50):
    """Rough estimate of diffusion inference cost at different resolutions."""
    spatial = (resolution // latent_factor) ** 2
    # Self-attention cost O(spatial^2 * channels)
    attn_cost = spatial ** 2 * 64  # proportional
    # Conv cost O(spatial * channels^2 * kernel^2)
    conv_cost = spatial * 64**2 * 9
    step_cost = (attn_cost + conv_cost) / 1e9  # in GFLOPs (approx)
    total_gflops = step_cost * n_steps * batch

    mode = 'pixel-space' if latent_factor == 1 else f'latent (f={latent_factor})'
    print(f'{mode:20s} | res={resolution//latent_factor:3d}x{resolution//latent_factor:3d} '
          f'| attn cost: {attn_cost/1e6:7.1f}M | total GFLOPs: {total_gflops:.1f}')
    return total_gflops

print(f'{"Mode":20s} | {"Latent res":12s} | {"Attn cost":13s} | {"GFLOPs (50 steps)"}' )
print('-' * 72)
for res, f in [(512, 1), (512, 4), (512, 8), (1024, 8)]:
    estimate_flops_and_time(res, latent_factor=f)
print()
print('Latent f=8 reduces attention cost by 64^2 = 4096x vs pixel-space at 512x512')
```

| Model | Latent type | Resolution | Latent size | Condition type | Training compute |
| --- | --- | --- | --- | --- | --- |
| DDPM (Ho et al. 2020) | None — pixel space | 256×256 | 256×256×3 pixels | Class label (embed) | High — pixel U-Net |
| LDM (Rombach et al. 2022) | KL-VAE or VQ-VAE | 256–512×256–512 | 32–64×32–64×4 | Text/class via cross-attn | ~4–16× cheaper than pixel |
| Stable Diffusion 1.5 | KL-VAE f=8 | 512×512 | 64×64×4 | CLIP ViT-L/14 text | ~50× cheaper than pixel SD |
| DALL-E 3 / SDXL | KL-VAE f=8 | 1024×1024 | 128×128×4 | T5 / CLIP dual text encoder | ~200× cheaper than naive pixel |

> **Why Latent Space Works for Diffusion**: A perceptually-trained autoencoder (using LPIPS loss + GAN discriminator) compresses images into latents that preserve semantic and structural information while discarding high-frequency pixel noise. Diffusion in this perceptual latent space is efficient because the latent space is semantically smooth — small latent changes correspond to semantically meaningful image changes, making the score field easier to learn.

- Pixel-space self-attention at 512×512 costs 4096× more than at 64×64 — the primary motivation for latent diffusion.
- KL-regularized autoencoder: small KL weight (1e-6) prioritizes reconstruction fidelity over posterior regularization.
- Latent scaling: divide latents by std of the training set before diffusion training to match the noise schedule assumptions.
- Cross-attention at multiple U-Net resolutions (32×32, 16×16, 8×8) enables spatially-grounded text conditioning.
- Stable Diffusion = LDM + CLIP text encoder + CFG — each component is independently replaceable.
- SDXL improves by using two CLIP encoders (ViT-L and ViT-G), increasing text capacity from 768 to 2048 dims.

---

