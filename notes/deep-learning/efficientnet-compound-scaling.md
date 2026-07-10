---
title: "EfficientNet — Compound Scaling and NAS Design"
slug: "efficientnet-compound-scaling"
description: "EfficientNet (Tan & Le 2019): systematically scale depth, width, and resolution together using compound coefficient φ. Covers NAS-derived B0 baseline, MBConv with Squeeze-Excitation, compound scaling B0→B7, EfficientNetV2 progressive learning, and EfficientDet."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWZmaWNpZW50TmV0IChUYW4gXHUwMDI2IExlLCBOZXVySVBTIDIwMTkpIHJldm9sdXRpb25pemVkIENOTiBkZXNpZ24gYnkgYXNraW5nIGEgZnVuZGFtZW50YWwgcXVlc3Rpb246IGdpdmVuIGEgZml4ZWQgY29tcHV0ZSBidWRnZXQsIGhvdyBzaG91bGQgeW91IHNjYWxlIG5ldHdvcmsgZGVwdGgsIHdpZHRoLCBhbmQgaW5wdXQgcmVzb2x1dGlvbiB0b2dldGhlcj8gVGhlIGFuc3dlciDigJQgY29tcG91bmQgc2NhbGluZyDigJQgeWllbGRzIGEgZmFtaWx5IG9mIG1vZGVscyBmcm9tIEIwICg1LjNNIHBhcmFtcykgdG8gQjcgKDY2TSBwYXJhbXMpIHRoYXQgb3V0cGVyZm9ybWVkIGV2ZXJ5IHByaW9yIENOTiBhdCB0aGUgdGltZSBvZiBwdWJsaWNhdGlvbi4gRWZmaWNpZW50TmV0IG1vZGVscyBhcmUgZGVyaXZlZCBmcm9tIGEgTkFTLWZvdW5kIEIwIGJhc2VsaW5lIGFuZCBzeXN0ZW1hdGljYWxseSBzY2FsZWQsIG1ha2luZyB0aGVtIGJvdGggcHJpbmNpcGxlZCBhbmQgaGlnaGx5IGVmZmljaWVudC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaGF0IElzIEVmZmljaWVudE5ldD8ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVmZmljaWVudE5ldCBpcyBhIGZhbWlseSBvZiBDTk5zIHdob3NlIGFyY2hpdGVjdHVyZSBhbmQgc2NhbGluZyBzdHJhdGVneSB3ZXJlIGNvLWRlc2lnbmVkIGJ5IE5ldXJhbCBBcmNoaXRlY3R1cmUgU2VhcmNoIChOQVMpLiBUaGUgTkFTIHByb2Nlc3Mgb3B0aW1pemVkIGZvciBhY2N1cmFjeSBhbmQgRkxPUHMgc2ltdWx0YW5lb3VzbHkgb24gYSBzbWFsbCBwcm94eSB0YXNrLCB5aWVsZGluZyB0aGUgQjAgYmFzZWxpbmUgYXJjaGl0ZWN0dXJlLiBCMCB1c2VzIE1vYmlsZSBJbnZlcnRlZCBCb3R0bGVuZWNrIENvbnZvbHV0aW9ucyAoTUJDb252KSB3aXRoIFNxdWVlemUtRXhjaXRhdGlvbiBhdHRlbnRpb24gYXMgdGhlIGNvcmUgYmxvY2suIEZyb20gQjAsIHRoZSBCMeKAk0I3IHZhcmlhbnRzIGFyZSBvYnRhaW5lZCBieSBpbmNyZWFzaW5nIGEgY29tcG91bmQgY29lZmZpY2llbnQgz4YgdGhhdCBqb2ludGx5IHNjYWxlcyBkZXB0aCwgd2lkdGgsIGFuZCByZXNvbHV0aW9uLiBBdCBlcXVhbCBhY2N1cmFjeSwgRWZmaWNpZW50TmV0IHVzZWQgdXAgdG8gOC40w5cgZmV3ZXIgcGFyYW1ldGVycyBhbmQgMTbDlyBmZXdlciBGTE9QcyB0aGFuIHRoZSBiZXN0IGNvbXBldGluZyBtb2RlbHMgc3VjaCBhcyBHUGlwZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wb3VuZCBTY2FsaW5nIOKAlCBEZXB0aCwgV2lkdGgsIGFuZCBSZXNvbHV0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOYWl2ZWx5IHNjYWxpbmcgYW55IHNpbmdsZSBkaW1lbnNpb24gKGRlcHRoIG9ubHksIHdpZHRoIG9ubHksIG9yIHJlc29sdXRpb24gb25seSkgcXVpY2tseSBoaXRzIGRpbWluaXNoaW5nIHJldHVybnMuIFRhbiBcdTAwMjYgTGUgcHJvcG9zZSBzY2FsaW5nIGFsbCB0aHJlZSBzaW11bHRhbmVvdXNseSB1c2luZyBhIGNvbXBvdW5kIGNvZWZmaWNpZW50IM+GLiBCYXNlbGluZSBtdWx0aXBsaWVycyDOsSAoZGVwdGgpLCDOsiAod2lkdGgpLCDOsyAocmVzb2x1dGlvbikgYXJlIGZvdW5kIGJ5IGdyaWQgc2VhcmNoIGF0IM+GPTEgc3ViamVjdCB0byB0aGUgY29uc3RyYWludCDOscK3zrLCssK3zrPCsuKJiDIsIHNvIHRoYXQgZG91Ymxpbmcgz4Ygcm91Z2hseSBkb3VibGVzIEZMT1BzLiBUaGUgc2NhbGVkIG1vZGVsIGF0IGNvZWZmaWNpZW50IM+GIGhhczogZGVwdGggZCA9IM6xXs+GLCB3aWR0aCB3ID0gzrJez4YsIHJlc29sdXRpb24gciA9IM6zXs+GLiBGb3IgRWZmaWNpZW50TmV0LCDOsT0xLjIsIM6yPTEuMSwgzrM9MS4xNSDigJQgZ2l2aW5nIM6xwrfOssKywrfOs8KyIOKJiCAxLjLDlzEuMjHDlzEuMzIyNSDiiYggMS45MiDiiYggMi4gVGhpcyBtZWFucyBvbmUgdW5pdCBvZiDPhiBjb3N0cyBhcHByb3hpbWF0ZWx5IDLDlyB0aGUgRkxPUHMgb2YgdGhlIHByZXZpb3VzIHN0ZXAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3F1ZWV6ZS1FeGNpdGF0aW9uIEJsb2NrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFNFIGJsb2NrIChIdSBldCBhbC4sIDIwMTgpIHJld2VpZ2h0cyBjaGFubmVscyBhZGFwdGl2ZWx5IHVzaW5nIGdsb2JhbCBjb250ZXh0LiBJdCBoYXMgdGhyZWUgc3RlcHM6ICgxKSBTcXVlZXplIOKAlCBnbG9iYWwgYXZlcmFnZSBwb29sIGFjcm9zcyBzcGF0aWFsIGRpbWVuc2lvbnMsIHlpZWxkaW5nIGEgKEIsIEMpIGRlc2NyaXB0b3I7ICgyKSBFeGNpdGF0aW9uIOKAlCB0d28gZnVsbHktY29ubmVjdGVkIGxheWVycyB3aXRoIFJlTFUgYW5kIFNpZ21vaWQsIGZvcm1pbmcgYSBib3R0bGVuZWNrIEMg4oaSIEMvciDihpIgQyB0aGF0IGxlYXJucyBjaGFubmVsIGltcG9ydGFuY2Ugd2VpZ2h0czsgKDMpIFNjYWxlIOKAlCBtdWx0aXBseSB0aGUgZmVhdHVyZSBtYXAgY2hhbm5lbC13aXNlIGJ5IHRoZSBsZWFybmVkIHdlaWdodHMg4oiIICgwLCAxKS4gVGhlIFNFIGJsb2NrIGFkZHMgYXBwcm94aW1hdGVseSAywrdDwrIvciBwYXJhbWV0ZXJzIChyPTQgdHlwaWNhbCksIGEgc21hbGwgb3ZlcmhlYWQgdGhhdCBjb25zaXN0ZW50bHkgcHJvdmlkZXMgKzHigJMyJSBhY2N1cmFjeS4gRWZmaWNpZW50TmV0IHBsYWNlcyBvbmUgU0UgYmxvY2sgaW5zaWRlIGV2ZXJ5IE1CQ29udiBibG9jay4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Imluc2lnaHQiLCJ0aXRsZSI6IldoeSBTRSBCbG9ja3MgV29yayIsImNvbnRlbnQiOiJUaGUgU0UgYmxvY2sgaXMgYSBsaWdodHdlaWdodCBjaGFubmVsIGF0dGVudGlvbiBtZWNoYW5pc20uIFRoZSBnbG9iYWwgYXZlcmFnZSBwb29sIHNxdWVlemVzIHNwYXRpYWwgaW5mb3JtYXRpb24gaW50byBhIGNoYW5uZWwgZGVzY3JpcHRvcjsgdGhlIEZDIGJvdHRsZW5lY2sgZXhjaXRlcyBpbmZvcm1hdGl2ZSBjaGFubmVscyBhbmQgc3VwcHJlc3NlcyBsZXNzIHVzZWZ1bCBvbmVzLiBCZWNhdXNlIHRoZSBsZWFybmVkIHdlaWdodHMgZGVwZW5kIG9uIGdsb2JhbCBpbWFnZSBjb250ZW50IChub3QgbG9jYWwgcGF0Y2hlcyksIHRoZSBuZXR3b3JrIGNhbiBzZWxlY3RpdmVseSBzdXBwcmVzcyBiYWNrZ3JvdW5kLWFjdGl2YXRlZCBjaGFubmVscyBldmVuIHdoZW4gdGhvc2UgY2hhbm5lbHMgZmlyZSBzdHJvbmdseSBsb2NhbGx5LiBTRSBhZGRzIFx1MDAzYzElIHBhcmFtZXRlciBvdmVyaGVhZCB3aGlsZSBjb25zaXN0ZW50bHkgaW1wcm92aW5nIGFjY3VyYWN5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1CQ29udiDigJQgTW9iaWxlIEludmVydGVkIEJvdHRsZW5lY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1CQ29udiAoYWxzbyB1c2VkIGluIE1vYmlsZU5ldFYyIGFuZCBWMykgaXMgYW4gaW52ZXJ0ZWQgYm90dGxlbmVjazogY2hhbm5lbHMgYXJlIGZpcnN0IGV4cGFuZGVkIChieSBmYWN0b3IgZXhwYW5kX3JhdGlvPTYpIHRoZW4gcmVkdWNlZCDigJQgb3Bwb3NpdGUgdG8gdGhlIGNsYXNzaWMgYm90dGxlbmVjay4gRWZmaWNpZW50TmV0XHUwMDI3cyBNQkNvbnYgYmxvY2s6ICgxKSBwb2ludHdpc2UgZXhwYW5zaW9uIGNvbnYgKGluIOKGkiBpbsOXZXhwYW5kKSwgKDIpIGRlcHRod2lzZSAzw5czIG9yIDXDlzUgY29udiB3aXRoIHN0cmlkZSwgKDMpIFNxdWVlemUtRXhjaXRhdGlvbiwgKDQpIHBvaW50d2lzZSBwcm9qZWN0aW9uIGNvbnYgKGluw5dleHBhbmQg4oaSIG91dCksICg1KSBza2lwIGNvbm5lY3Rpb24gd2hlbiBzdHJpZGU9MSBhbmQgaW5fY2hhbm5lbHM9b3V0X2NoYW5uZWxzLiBUaGUgZGVwdGh3aXNlIHNlcGFyYWJsZSBzdHJ1Y3R1cmUgZHJhbWF0aWNhbGx5IHJlZHVjZXMgRkxPUHMgdmVyc3VzIHN0YW5kYXJkIGNvbnZvbHV0aW9uOiBhIGvDl2sgZGVwdGh3aXNlICsgMcOXMSBwb2ludHdpc2UgdXNlcyBrwrIgKyBDX291dCB0aW1lcyBmZXdlciBGTE9QcyB0aGFuIGEga8OXayBzdGFuZGFyZCBjb252LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgRXhhbXBsZXMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgU3F1ZWV6ZUV4Y2l0YXRpb24obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTRSBibG9jazogZ2xvYmFsIGF2ZyBwb29sIC1cdTAwM2UgRkMgLVx1MDAzZSBSZUxVIC1cdTAwM2UgRkMgLVx1MDAzZSBTaWdtb2lkIC1cdTAwM2UgY2hhbm5lbCBzY2FsaW5nLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaGFubmVscywgcmVkdWN0aW9uX3JhdGlvPTQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgcmVkdWNlZCA9IG1heCgxLCBpbl9jaGFubmVscyAvLyByZWR1Y3Rpb25fcmF0aW8pXG4gICAgICAgIHNlbGYuZ2FwICA9IG5uLkFkYXB0aXZlQXZnUG9vbDJkKDEpXG4gICAgICAgIHNlbGYuZmMxICA9IG5uLkxpbmVhcihpbl9jaGFubmVscywgcmVkdWNlZClcbiAgICAgICAgc2VsZi5mYzIgID0gbm4uTGluZWFyKHJlZHVjZWQsIGluX2NoYW5uZWxzKVxuICAgICAgICBzZWxmLnJlbHUgPSBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcbiAgICAgICAgc2VsZi5zaWcgID0gbm4uU2lnbW9pZCgpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcyA9IHNlbGYuZ2FwKHgpLmZsYXR0ZW4oMSkgICAgICAgICAgICMgKEIsIEMpOiBzcXVlZXplXG4gICAgICAgIHMgPSBzZWxmLnJlbHUoc2VsZi5mYzEocykpICAgICAgICAgICAjIEZDIC1cdTAwM2UgUmVMVVxuICAgICAgICBzID0gc2VsZi5zaWcoc2VsZi5mYzIocykpICAgICAgICAgICAgIyBGQyAtXHUwMDNlIFNpZ21vaWQ6IHdlaWdodHMgaW4gKDAsMSlcbiAgICAgICAgcmV0dXJuIHggKiBzLnVuc3F1ZWV6ZSgtMSkudW5zcXVlZXplKC0xKSAgIyBjaGFubmVsLXdpc2Ugc2NhbGVcblxuc2UgPSBTcXVlZXplRXhjaXRhdGlvbig2NCwgcmVkdWN0aW9uX3JhdGlvPTQpXG54ICA9IHRvcmNoLnJhbmRuKDIsIDY0LCAyOCwgMjgpXG5vdXQgPSBzZSh4KVxucHJpbnQoZlwiSW5wdXQ6ICB7eC5zaGFwZX1cIilcbnByaW50KGZcIk91dHB1dDoge291dC5zaGFwZX0gIChzYW1lIHNoYXBlLCBjaGFubmVscyByZS13ZWlnaHRlZClcIilcbnByaW50KGZcIlNFIHBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gc2UucGFyYW1ldGVycygpKTosfVwiKVxucHJpbnQoXCJyZWR1Y3Rpb25fcmF0aW89NCAtXHUwMDNlIGJvdHRsZW5lY2s6IDY0LVx1MDAzZTE2LVx1MDAzZTY0OyBzbWFsbCBvdmVyaGVhZCwgbGFyZ2UgZ2FpblwiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBNQkNvbnYobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJNb2JpbGUgSW52ZXJ0ZWQgQm90dGxlbmVjayArIFNFIGJsb2NrIChFZmZpY2llbnROZXQgY29yZSBidWlsZGluZyBibG9jaykuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBvdXRfY2gsIGV4cGFuZD02LCBzdHJpZGU9MSwgc2VfcmF0aW89MC4yNSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBtaWQsIHNlX2NoID0gaW5fY2ggKiBleHBhbmQsIG1heCgxLCBpbnQoaW5fY2ggKiBzZV9yYXRpbykpXG4gICAgICAgIHNlbGYuc2tpcCAgPSAoc3RyaWRlID09IDEgYW5kIGluX2NoID09IG91dF9jaClcbiAgICAgICAgc2VsZi5leHBhbmQgPSBubi5TZXF1ZW50aWFsKG5uLkNvbnYyZChpbl9jaCwgbWlkLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG1pZCksIG5uLlNpTFUoKSlcbiAgICAgICAgc2VsZi5kdyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQobWlkLCBtaWQsIDMsIHN0cmlkZT1zdHJpZGUsIHBhZGRpbmc9MSwgZ3JvdXBzPW1pZCwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0yZChtaWQpLCBubi5TaUxVKCkpXG4gICAgICAgIHNlbGYuc2VfcG9vbCA9IG5uLkFkYXB0aXZlQXZnUG9vbDJkKDEpXG4gICAgICAgIHNlbGYuc2VfZmMgICA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKG1pZCwgc2VfY2gpLCBubi5SZUxVKCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbm4uTGluZWFyKHNlX2NoLCBtaWQpLCBubi5TaWdtb2lkKCkpXG4gICAgICAgIHNlbGYucHJvaiA9IG5uLlNlcXVlbnRpYWwobm4uQ29udjJkKG1pZCwgb3V0X2NoLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBubi5CYXRjaE5vcm0yZChvdXRfY2gpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGggPSBzZWxmLmV4cGFuZCh4KVxuICAgICAgICBoID0gc2VsZi5kdyhoKVxuICAgICAgICBoID0gaCAqIHNlbGYuc2VfZmMoc2VsZi5zZV9wb29sKGgpLmZsYXR0ZW4oMSkpLnZpZXcoaC5zaXplKDApLCBoLnNpemUoMSksIDEsIDEpXG4gICAgICAgIGggPSBzZWxmLnByb2ooaClcbiAgICAgICAgcmV0dXJuIGggKyB4IGlmIHNlbGYuc2tpcCBlbHNlIGhcblxubSA9IE1CQ29udigzMiwgMzIsIGV4cGFuZD02LCBzdHJpZGU9MSlcbnggPSB0b3JjaC5yYW5kbigyLCAzMiwgMjgsIDI4KVxucHJpbnQoZlwiT3V0cHV0OiB7bSh4KS5zaGFwZX0sIFBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gbS5wYXJhbWV0ZXJzKCkpOix9XCIpXG5wcmludChcIlBhdHRlcm46IGV4cGFuZChwdykgLVx1MDAzZSBkZXB0aHdpc2UgLVx1MDAzZSBTRSAtXHUwMDNlIHByb2plY3QocHcpICsgc2tpcFwiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIEVmZmljaWVudE5ldCBjb21wb3VuZCBzY2FsaW5nOiBkZXB0aD1hbHBoYV5waGksIHdpZHRoPWJldGFecGhpLCByZXNvbHV0aW9uPWdhbW1hXnBoaVxuQUxQSEEsIEJFVEEsIEdBTU1BID0gMS4yLCAxLjEsIDEuMTVcbkIwX1BBUkFNU19NLCBCMF9GTE9QU19CLCBCMF9SRVMgPSA1LjMsIDAuMzksIDIyNFxuXG5wcmludChmXCJDb25zdHJhaW50OiBhbHBoYSpiZXRhKioyKmdhbW1hKioyID0ge0FMUEhBICogQkVUQSoqMiAqIEdBTU1BKioyOi40Zn0gKHRhcmdldCB+MilcIilcblxuZGVmIGNvbXBvdW5kX3NjYWxlKHBoaSk6XG4gICAgZCA9IEFMUEhBICoqIHBoaVxuICAgIHcgPSBCRVRBICAqKiBwaGlcbiAgICByID0gR0FNTUEgKiogcGhpXG4gICAgcmV0dXJuIChkLCB3LCByLFxuICAgICAgICAgICAgQjBfUEFSQU1TX00gKiBkICogdyoqMixcbiAgICAgICAgICAgIEIwX0ZMT1BTX0IgICogZCAqIHcqKjIgKiByKioyLFxuICAgICAgICAgICAgaW50KEIwX1JFUyAqIHIgLyAzMikgKiAzMilcblxubmFtZXMgPSBbXHUwMDI3QjBcdTAwMjcsIFx1MDAyN0IxXHUwMDI3LCBcdTAwMjdCMlx1MDAyNywgXHUwMDI3QjNcdTAwMjcsIFx1MDAyN0I0XHUwMDI3LCBcdTAwMjdCNVx1MDAyNywgXHUwMDI3QjZcdTAwMjcsIFx1MDAyN0I3XHUwMDI3XVxuaGVhZGVyID0gZlwie1x1MDAyN01vZGVsXHUwMDI3Olx1MDAzYzh9IHtcdTAwMjdwaGlcdTAwMjc6XHUwMDNlM30gIHtcdTAwMjdkZXB0aFx1MDAyNzpcdTAwM2U2fSAge1x1MDAyN3dpZHRoXHUwMDI3Olx1MDAzZTZ9ICB7XHUwMDI3cmVzXHUwMDI3Olx1MDAzZTV9ICB7XHUwMDI3UGFyYW1zKE0pXHUwMDI3Olx1MDAzZTl9ICB7XHUwMDI3R0ZMT1BzXHUwMDI3Olx1MDAzZTd9XCJcbnByaW50KGhlYWRlcilcbnByaW50KFx1MDAyNy1cdTAwMjcgKiBsZW4oaGVhZGVyKSlcbmZvciBwaGksIG5hbWUgaW4gZW51bWVyYXRlKG5hbWVzKTpcbiAgICBkLCB3LCByLCBwLCBmLCByZXMgPSBjb21wb3VuZF9zY2FsZShwaGkpXG4gICAgcHJpbnQoZlwie25hbWU6XHUwMDNjOH0ge3BoaTpcdTAwM2UzfSAge2Q6XHUwMDNlNi4yZn0gIHt3Olx1MDAzZTYuMmZ9ICB7cmVzOlx1MDAzZTV9ICB7cDpcdTAwM2U5LjFmfSAge2Y6XHUwMDNlNy4yZn1cIilcbnByaW50KClcbnByaW50KFwiQ29tcG91bmQgc2NhbGluZyBpcyBtb3JlIEZMT1BzLWVmZmljaWVudCB0aGFuIHNpbmdsZS1kaW1lbnNpb24gc2NhbGluZy5cIilcbnByaW50KFwiQjAtXHUwMDNlQjcgaW5jcmVhc2VzIEZMT1BzIGJ5IH45NXg7IGFjY3VyYWN5IHJpc2VzIGZyb20gNzcuMyUgdG8gODQuNCUuXCIpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNodmlzaW9uIGltcG9ydCBtb2RlbHMsIHRyYW5zZm9ybXNcblxubW9kZWwgPSBtb2RlbHMuZWZmaWNpZW50bmV0X2IwKHdlaWdodHM9bW9kZWxzLkVmZmljaWVudE5ldF9CMF9XZWlnaHRzLklNQUdFTkVUMUtfVjEpXG5cbiMgRnJlZXplIGVudGlyZSBiYWNrYm9uZVxuZm9yIHBhcmFtIGluIG1vZGVsLnBhcmFtZXRlcnMoKTpcbiAgICBwYXJhbS5yZXF1aXJlc19ncmFkID0gRmFsc2VcblxuIyBSZXBsYWNlIGNsYXNzaWZpY2F0aW9uIGhlYWQgKGluX2ZlYXR1cmVzPTEyODAgZm9yIEIwKVxubnVtX2NsYXNzZXMgPSAxMFxubW9kZWwuY2xhc3NpZmllciA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uRHJvcG91dChwPTAuMiwgaW5wbGFjZT1UcnVlKSxcbiAgICBubi5MaW5lYXIobW9kZWwuY2xhc3NpZmllclsxXS5pbl9mZWF0dXJlcywgbnVtX2NsYXNzZXMpXG4pXG5cbnRyYWluYWJsZSA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZClcbnRvdGFsICAgICA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKVxucHJpbnQoZlwiVHJhaW5hYmxlOiB7dHJhaW5hYmxlOix9IC8ge3RvdGFsOix9ICh7MTAwKnRyYWluYWJsZS90b3RhbDouMmZ9JSlcIilcblxub3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5jbGFzc2lmaWVyLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbmNyaXRlcmlvbiA9IG5uLkNyb3NzRW50cm9weUxvc3MoKVxuXG4jIFN0YW5kYXJkIEVmZmljaWVudE5ldC1CMCBwcmVwcm9jZXNzaW5nXG50cmFuc2Zvcm0gPSB0cmFuc2Zvcm1zLkNvbXBvc2UoW1xuICAgIHRyYW5zZm9ybXMuUmVzaXplKDI1NiksXG4gICAgdHJhbnNmb3Jtcy5DZW50ZXJDcm9wKDIyNCksXG4gICAgdHJhbnNmb3Jtcy5Ub1RlbnNvcigpLFxuICAgIHRyYW5zZm9ybXMuTm9ybWFsaXplKFswLjQ4NSwgMC40NTYsIDAuNDA2XSwgWzAuMjI5LCAwLjIyNCwgMC4yMjVdKSxcbl0pXG5wcmludChcIlRvIGZpbmUtdHVuZSBtb3JlIGxheWVyczogc2V0IHBhcmFtLnJlcXVpcmVzX2dyYWQ9VHJ1ZSBmb3IgbW9kZWwuZmVhdHVyZXNbLTM6XVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmljaWVudE5ldFYyIGFuZCBQcm9ncmVzc2l2ZSBMZWFybmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWZmaWNpZW50TmV0VjIgKFRhbiBcdTAwMjYgTGUsIDIwMjEpIHJldmlzaXRlZCB0aGUgZGVzaWduIHdpdGggdGhyZWUgaW1wcm92ZW1lbnRzOiAoMSkgRnVzZWQtTUJDb252IHJlcGxhY2VzIHRoZSBleHBhbmQrZGVwdGh3aXNlIGNvbWJpbmF0aW9uIGluIGVhcmx5IGxheWVycyB3aXRoIGEgc2luZ2xlIHJlZ3VsYXIgM8OXMyBjb252b2x1dGlvbiDigJQgZmFzdGVyIG9uIGFjY2VsZXJhdG9ycyAoVFBVL0dQVSkgZGVzcGl0ZSBtb3JlIEZMT1BzIGJlY2F1c2UgZnVzZWQgb3BzIGhhdmUgYmV0dGVyIGhhcmR3YXJlIHV0aWxpemF0aW9uOyAoMikgUHJvZ3Jlc3NpdmUgbGVhcm5pbmc6IHRyYWluaW5nIHN0YXJ0cyB3aXRoIHNtYWxsIGltYWdlcyAoZS5nLiwgMTI4cHgpIGFuZCB3ZWFrIGF1Z21lbnRhdGlvbiwgdGhlbiBncmFkdWFsbHkgaW5jcmVhc2VzIGJvdGggdG8gdGhlIGZ1bGwgcmVzb2x1dGlvbiDigJQgY3V0cyB0cmFpbmluZyB0aW1lIGJ5IH40w5cgdmVyc3VzIHRyYWluaW5nIG9uIGxhcmdlIGltYWdlcyB0aHJvdWdob3V0OyAoMykgSW1wcm92ZWQgc2NhbGluZzogUy9NL0wvWEwgdmFyaWFudHMgcmVwbGFjZSBCMC1CNywgYWNoaWV2aW5nIDg1LjclIG9uIEltYWdlTmV0IGZvciBFZmZpY2llbnROZXRWMi1MIHdpdGggMy4xw5cgZmFzdGVyIHRyYWluaW5nIHRoYW4gRWZmaWNpZW50TmV0LUI3LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmljaWVudERldCDigJQgQ29tcG91bmQgU2NhbGluZyBmb3IgRGV0ZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFZmZpY2llbnREZXQgYXBwbGllcyBjb21wb3VuZCBzY2FsaW5nIHRvIG9iamVjdCBkZXRlY3Rpb24uIFRoZSBiYWNrYm9uZSBpcyBFZmZpY2llbnROZXQtQs+GOyB0aGUgbmVjayBpcyBCaUZQTiAoYmlkaXJlY3Rpb25hbCBmZWF0dXJlIHB5cmFtaWQgbmV0d29yaykgc2NhbGVkIGJ5IGRlcHRoIGFuZCBjaGFubmVsIGNvdW50OyB0aGUgZGV0ZWN0aW9uIGhlYWQgaXMgYWxzbyBzY2FsZWQgd2l0aCDPhi4gQmlGUE4gYXBwbGllcyB3ZWlnaHRlZCBiaWRpcmVjdGlvbmFsIGZlYXR1cmUgZnVzaW9uIGFjcm9zcyBQM+KAk1A3IHNjYWxlcywgbGVhcm5pbmcgYSBzb2Z0bWF4IGltcG9ydGFuY2Ugd2VpZ2h0IGF0IGVhY2ggY29ubmVjdGlvbi4gVGhlIGNvbXBvdW5kIHNjYWxpbmcgY29lZmZpY2llbnQgz4YgY29udHJvbHMgYWxsIHRocmVlIGNvbXBvbmVudHMgc2ltdWx0YW5lb3VzbHkuIEVmZmljaWVudERldCBEMOKAk0Q3IHNldCBuZXcgZWZmaWNpZW5jeSByZWNvcmRzIG9uIENPQ08g4oCUIEVmZmljaWVudERldC1ENyBhY2hpZXZlcyA1NS4xIEFQIGF0IDUyTSBwYXJhbWV0ZXJzIHZlcnN1cyBBbW9lYmFOZXQrTkFTLUZQTiBhdCA1NS43IEFQIHdpdGggMTY3TSBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkIw4oCTQjcgU2NhbGluZyBSZWZlcmVuY2UifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCLPhiIsIklucHV0IFJlcyIsIlBhcmFtcyAoTSkiLCJHRkxPUHMiLCJUb3AtMSBBY2MgKCUpIl0sInJvd3MiOltbIkIwIiwiMCIsIjIyNCIsIjUuMyIsIjAuMzkiLCI3Ny4zIl0sWyJCMSIsIjEiLCIyNDAiLCI3LjgiLCIwLjcwIiwiNzkuMiJdLFsiQjIiLCIyIiwiMjYwIiwiOS4yIiwiMS4wIiwiODAuMyJdLFsiQjMiLCIzIiwiMzAwIiwiMTIuMCIsIjEuOCIsIjgxLjciXSxbIkI0IiwiNCIsIjM4MCIsIjE5LjAiLCI0LjIiLCI4My4wIl0sWyJCNSIsIjUiLCI0NTYiLCIzMC4wIiwiOS45IiwiODMuNyJdLFsiQjYiLCI2IiwiNTI4IiwiNDMuMCIsIjE5LjAiLCI4NC4xIl0sWyJCNyIsIjciLCI2MDAiLCI2Ni4wIiwiMzcuMCIsIjg0LjQiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlc2lnbiBDb25jbHVzaW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNlbnRyYWwgY29udHJpYnV0aW9uIG9mIEVmZmljaWVudE5ldCBpcyB0aGUgY29tcG91bmQgc2NhbGluZyBtZXRob2RvbG9neSwgbm90IHRoZSBCMCBhcmNoaXRlY3R1cmUgaXRzZWxmLiBCeSBjb25zdHJhaW5pbmcgzrHCt86ywrLCt86zwrLiiYgyLCBzY2FsaW5nIGJlY29tZXMgY2FsaWJyYXRlZDogZWFjaCB1bml0IG9mIM+GIGNvc3RzIGEgcHJlZGljdGFibGUgMsOXIGluIEZMT1BzLiBUaGUgZ3JpZCBzZWFyY2ggZm9yIM6xLCDOsiwgzrMgaXMgY2hlYXAgKHJ1biBhdCDPhj0xIG9uIGEgc21hbGwgZGF0YXNldCkgYW5kIHRoZSByZXN1bHQgaXMgYSBjbGVhbiBzY2FsaW5nIGxhdyBmcm9tIEIwIHRvIEI3LiBUaGlzIG1ldGhvZG9sb2d5IGlzIGFyY2hpdGVjdHVyZS1hZ25vc3RpYyBhbmQgaGFzIGluZmx1ZW5jZWQgbWFueSBzdWJzZXF1ZW50IG1vZGVscyDigJQgRWZmaWNpZW50RGV0LCBFZmZpY2llbnROZXRWMiwgYW5kIG1hbnkgZGV0ZWN0aW9uL3NlZ21lbnRhdGlvbiBiYWNrYm9uZXMgYWxsIGFkb3B0IHRoZSBzYW1lIHByaW5jaXBsZS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIk5BUyBmaW5kcyBCMCBiYXNlbGluZTsgY29tcG91bmQgc2NhbGluZyB3aXRoIM+GIG11bHRpcGxpZXMgaXQgaW50byBCMS1CNy4iLCJDb25zdHJhaW50IM6xwrfOssKywrfOs8Ky4omIMiBlbnN1cmVzIGRvdWJsaW5nIM+GIGRvdWJsZXMgRkxPUHMgKGNsZWFuIHNjYWxpbmcgbGF3KS4iLCJNQkNvbnY6IGV4cGFuZCAocG9pbnR3aXNlKSAtXHUwMDNlIGRlcHRod2lzZSAtXHUwMDNlIFNFIC1cdTAwM2UgcHJvamVjdCAocG9pbnR3aXNlKSArIHNraXAuIiwiU0UgYmxvY2s6IGdsb2JhbCBhdmcgcG9vbCAtXHUwMDNlIEZDIGJvdHRsZW5lY2sgLVx1MDAzZSBTaWdtb2lkIC1cdTAwM2UgY2hhbm5lbC13aXNlIHNjYWxlLiIsIkVmZmljaWVudE5ldFYyOiBGdXNlZC1NQkNvbnYgZm9yIGVhcmx5IGxheWVycywgcHJvZ3Jlc3NpdmUgaW1hZ2Ugc2l6ZSB0cmFpbmluZy4iLCJBdCBlcXVhbCBhY2N1cmFjeSwgRWZmaWNpZW50TmV0IHVzZXMgdXAgdG8gOC40w5cgZmV3ZXIgcGFyYW1ldGVycyB0aGFuIHByaW9yIENOTnMuIl19XQ=="
---
# EfficientNet — Compound Scaling and NAS Design

EfficientNet (Tan & Le, NeurIPS 2019) revolutionized CNN design by asking a fundamental question: given a fixed compute budget, how should you scale network depth, width, and input resolution together? The answer — compound scaling — yields a family of models from B0 (5.3M params) to B7 (66M params) that outperformed every prior CNN at the time of publication. EfficientNet models are derived from a NAS-found B0 baseline and systematically scaled, making them both principled and highly efficient.

## What Is EfficientNet?

EfficientNet is a family of CNNs whose architecture and scaling strategy were co-designed by Neural Architecture Search (NAS). The NAS process optimized for accuracy and FLOPs simultaneously on a small proxy task, yielding the B0 baseline architecture. B0 uses Mobile Inverted Bottleneck Convolutions (MBConv) with Squeeze-Excitation attention as the core block. From B0, the B1–B7 variants are obtained by increasing a compound coefficient φ that jointly scales depth, width, and resolution. At equal accuracy, EfficientNet used up to 8.4× fewer parameters and 16× fewer FLOPs than the best competing models such as GPipe.

## Compound Scaling — Depth, Width, and Resolution

Naively scaling any single dimension (depth only, width only, or resolution only) quickly hits diminishing returns. Tan & Le propose scaling all three simultaneously using a compound coefficient φ. Baseline multipliers α (depth), β (width), γ (resolution) are found by grid search at φ=1 subject to the constraint α·β²·γ²≈2, so that doubling φ roughly doubles FLOPs. The scaled model at coefficient φ has: depth d = α^φ, width w = β^φ, resolution r = γ^φ. For EfficientNet, α=1.2, β=1.1, γ=1.15 — giving α·β²·γ² ≈ 1.2×1.21×1.3225 ≈ 1.92 ≈ 2. This means one unit of φ costs approximately 2× the FLOPs of the previous step.

## Squeeze-Excitation Blocks

The SE block (Hu et al., 2018) reweights channels adaptively using global context. It has three steps: (1) Squeeze — global average pool across spatial dimensions, yielding a (B, C) descriptor; (2) Excitation — two fully-connected layers with ReLU and Sigmoid, forming a bottleneck C → C/r → C that learns channel importance weights; (3) Scale — multiply the feature map channel-wise by the learned weights ∈ (0, 1). The SE block adds approximately 2·C²/r parameters (r=4 typical), a small overhead that consistently provides +1–2% accuracy. EfficientNet places one SE block inside every MBConv block.

> **Why SE Blocks Work**: The SE block is a lightweight channel attention mechanism. The global average pool squeezes spatial information into a channel descriptor; the FC bottleneck excites informative channels and suppresses less useful ones. Because the learned weights depend on global image content (not local patches), the network can selectively suppress background-activated channels even when those channels fire strongly locally. SE adds <1% parameter overhead while consistently improving accuracy.

## MBConv — Mobile Inverted Bottleneck

MBConv (also used in MobileNetV2 and V3) is an inverted bottleneck: channels are first expanded (by factor expand_ratio=6) then reduced — opposite to the classic bottleneck. EfficientNet's MBConv block: (1) pointwise expansion conv (in → in×expand), (2) depthwise 3×3 or 5×5 conv with stride, (3) Squeeze-Excitation, (4) pointwise projection conv (in×expand → out), (5) skip connection when stride=1 and in_channels=out_channels. The depthwise separable structure dramatically reduces FLOPs versus standard convolution: a k×k depthwise + 1×1 pointwise uses k² + C_out times fewer FLOPs than a k×k standard conv.

## Code Examples

```python
import torch
import torch.nn as nn

class SqueezeExcitation(nn.Module):
    """SE block: global avg pool -> FC -> ReLU -> FC -> Sigmoid -> channel scaling."""
    def __init__(self, in_channels, reduction_ratio=4):
        super().__init__()
        reduced = max(1, in_channels // reduction_ratio)
        self.gap  = nn.AdaptiveAvgPool2d(1)
        self.fc1  = nn.Linear(in_channels, reduced)
        self.fc2  = nn.Linear(reduced, in_channels)
        self.relu = nn.ReLU(inplace=True)
        self.sig  = nn.Sigmoid()

    def forward(self, x):
        s = self.gap(x).flatten(1)           # (B, C): squeeze
        s = self.relu(self.fc1(s))           # FC -> ReLU
        s = self.sig(self.fc2(s))            # FC -> Sigmoid: weights in (0,1)
        return x * s.unsqueeze(-1).unsqueeze(-1)  # channel-wise scale

se = SqueezeExcitation(64, reduction_ratio=4)
x  = torch.randn(2, 64, 28, 28)
out = se(x)
print(f"Input:  {x.shape}")
print(f"Output: {out.shape}  (same shape, channels re-weighted)")
print(f"SE params: {sum(p.numel() for p in se.parameters()):,}")
print("reduction_ratio=4 -> bottleneck: 64->16->64; small overhead, large gain")
```

```python
import torch
import torch.nn as nn

class MBConv(nn.Module):
    """Mobile Inverted Bottleneck + SE block (EfficientNet core building block)."""
    def __init__(self, in_ch, out_ch, expand=6, stride=1, se_ratio=0.25):
        super().__init__()
        mid, se_ch = in_ch * expand, max(1, int(in_ch * se_ratio))
        self.skip  = (stride == 1 and in_ch == out_ch)
        self.expand = nn.Sequential(nn.Conv2d(in_ch, mid, 1, bias=False),
                                    nn.BatchNorm2d(mid), nn.SiLU())
        self.dw = nn.Sequential(
            nn.Conv2d(mid, mid, 3, stride=stride, padding=1, groups=mid, bias=False),
            nn.BatchNorm2d(mid), nn.SiLU())
        self.se_pool = nn.AdaptiveAvgPool2d(1)
        self.se_fc   = nn.Sequential(nn.Linear(mid, se_ch), nn.ReLU(),
                                     nn.Linear(se_ch, mid), nn.Sigmoid())
        self.proj = nn.Sequential(nn.Conv2d(mid, out_ch, 1, bias=False),
                                  nn.BatchNorm2d(out_ch))

    def forward(self, x):
        h = self.expand(x)
        h = self.dw(h)
        h = h * self.se_fc(self.se_pool(h).flatten(1)).view(h.size(0), h.size(1), 1, 1)
        h = self.proj(h)
        return h + x if self.skip else h

m = MBConv(32, 32, expand=6, stride=1)
x = torch.randn(2, 32, 28, 28)
print(f"Output: {m(x).shape}, Params: {sum(p.numel() for p in m.parameters()):,}")
print("Pattern: expand(pw) -> depthwise -> SE -> project(pw) + skip")
```

```python
# EfficientNet compound scaling: depth=alpha^phi, width=beta^phi, resolution=gamma^phi
ALPHA, BETA, GAMMA = 1.2, 1.1, 1.15
B0_PARAMS_M, B0_FLOPS_B, B0_RES = 5.3, 0.39, 224

print(f"Constraint: alpha*beta**2*gamma**2 = {ALPHA * BETA**2 * GAMMA**2:.4f} (target ~2)")

def compound_scale(phi):
    d = ALPHA ** phi
    w = BETA  ** phi
    r = GAMMA ** phi
    return (d, w, r,
            B0_PARAMS_M * d * w**2,
            B0_FLOPS_B  * d * w**2 * r**2,
            int(B0_RES * r / 32) * 32)

names = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
header = f"{'Model':<8} {'phi':>3}  {'depth':>6}  {'width':>6}  {'res':>5}  {'Params(M)':>9}  {'GFLOPs':>7}"
print(header)
print('-' * len(header))
for phi, name in enumerate(names):
    d, w, r, p, f, res = compound_scale(phi)
    print(f"{name:<8} {phi:>3}  {d:>6.2f}  {w:>6.2f}  {res:>5}  {p:>9.1f}  {f:>7.2f}")
print()
print("Compound scaling is more FLOPs-efficient than single-dimension scaling.")
print("B0->B7 increases FLOPs by ~95x; accuracy rises from 77.3% to 84.4%.")
```

```python
import torch
import torch.nn as nn
from torchvision import models, transforms

model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.IMAGENET1K_V1)

# Freeze entire backbone
for param in model.parameters():
    param.requires_grad = False

# Replace classification head (in_features=1280 for B0)
num_classes = 10
model.classifier = nn.Sequential(
    nn.Dropout(p=0.2, inplace=True),
    nn.Linear(model.classifier[1].in_features, num_classes)
)

trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
total     = sum(p.numel() for p in model.parameters())
print(f"Trainable: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)")

optimizer = torch.optim.Adam(model.classifier.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

# Standard EfficientNet-B0 preprocessing
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
print("To fine-tune more layers: set param.requires_grad=True for model.features[-3:]")
```

## EfficientNetV2 and Progressive Learning

EfficientNetV2 (Tan & Le, 2021) revisited the design with three improvements: (1) Fused-MBConv replaces the expand+depthwise combination in early layers with a single regular 3×3 convolution — faster on accelerators (TPU/GPU) despite more FLOPs because fused ops have better hardware utilization; (2) Progressive learning: training starts with small images (e.g., 128px) and weak augmentation, then gradually increases both to the full resolution — cuts training time by ~4× versus training on large images throughout; (3) Improved scaling: S/M/L/XL variants replace B0-B7, achieving 85.7% on ImageNet for EfficientNetV2-L with 3.1× faster training than EfficientNet-B7.

## EfficientDet — Compound Scaling for Detection

EfficientDet applies compound scaling to object detection. The backbone is EfficientNet-Bφ; the neck is BiFPN (bidirectional feature pyramid network) scaled by depth and channel count; the detection head is also scaled with φ. BiFPN applies weighted bidirectional feature fusion across P3–P7 scales, learning a softmax importance weight at each connection. The compound scaling coefficient φ controls all three components simultaneously. EfficientDet D0–D7 set new efficiency records on COCO — EfficientDet-D7 achieves 55.1 AP at 52M parameters versus AmoebaNet+NAS-FPN at 55.7 AP with 167M parameters.

## B0–B7 Scaling Reference

| Model | φ | Input Res | Params (M) | GFLOPs | Top-1 Acc (%) |
| --- | --- | --- | --- | --- | --- |
| B0 | 0 | 224 | 5.3 | 0.39 | 77.3 |
| B1 | 1 | 240 | 7.8 | 0.70 | 79.2 |
| B2 | 2 | 260 | 9.2 | 1.0 | 80.3 |
| B3 | 3 | 300 | 12.0 | 1.8 | 81.7 |
| B4 | 4 | 380 | 19.0 | 4.2 | 83.0 |
| B5 | 5 | 456 | 30.0 | 9.9 | 83.7 |
| B6 | 6 | 528 | 43.0 | 19.0 | 84.1 |
| B7 | 7 | 600 | 66.0 | 37.0 | 84.4 |

## Design Conclusions

The central contribution of EfficientNet is the compound scaling methodology, not the B0 architecture itself. By constraining α·β²·γ²≈2, scaling becomes calibrated: each unit of φ costs a predictable 2× in FLOPs. The grid search for α, β, γ is cheap (run at φ=1 on a small dataset) and the result is a clean scaling law from B0 to B7. This methodology is architecture-agnostic and has influenced many subsequent models — EfficientDet, EfficientNetV2, and many detection/segmentation backbones all adopt the same principle.

- NAS finds B0 baseline; compound scaling with φ multiplies it into B1-B7.
- Constraint α·β²·γ²≈2 ensures doubling φ doubles FLOPs (clean scaling law).
- MBConv: expand (pointwise) -> depthwise -> SE -> project (pointwise) + skip.
- SE block: global avg pool -> FC bottleneck -> Sigmoid -> channel-wise scale.
- EfficientNetV2: Fused-MBConv for early layers, progressive image size training.
- At equal accuracy, EfficientNet uses up to 8.4× fewer parameters than prior CNNs.

