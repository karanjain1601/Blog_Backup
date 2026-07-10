---
title: "Hinton Knowledge Distillation — Soft Targets and Temperature"
slug: "hinton-distillation"
description: "Compress a large teacher into a small student by training on soft probability targets. Covers temperature scaling, the T-squared gradient compensation, the combined distillation loss, dark knowledge, born-again networks, and when distillation helps vs hurts."
tags: ["deep-learning", "model-compression", "knowledge-distillation"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiS25vd2xlZGdlIGRpc3RpbGxhdGlvbiAoSGludG9uIGV0IGFsLiAyMDE1KSB0cmFuc2ZlcnMga25vd2xlZGdlIGZyb20gYSBsYXJnZSwgYWNjdXJhdGUgdGVhY2hlciBuZXR3b3JrIGludG8gYSBzbWFsbCwgZmFzdCBzdHVkZW50LiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCBhIHRlYWNoZXJcdTAwMjdzIGZ1bGwgb3V0cHV0IGRpc3RyaWJ1dGlvbiBvdmVyIGFsbCBjbGFzc2VzIGVuY29kZXMgcmljaCBzdHJ1Y3R1cmFsIGluZm9ybWF0aW9uIGxlYXJuZWQgZnJvbSBkYXRhIOKAlCBpbmZvcm1hdGlvbiB0aGF0IG9uZS1ob3QgaGFyZCBsYWJlbHMgZGlzY2FyZCBlbnRpcmVseS4gVHJhaW5pbmcgdGhlIHN0dWRlbnQgdG8gbWF0Y2ggdGhpcyBzb2Z0IGRpc3RyaWJ1dGlvbiB0cmFuc2ZlcnMgaW50ZXItY2xhc3MgcmVsYXRpb25zaGlwcywgbm90IGp1c3QgdGhlIGlkZW50aXR5IG9mIHRoZSBjb3JyZWN0IGNsYXNzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhhcmQgTGFiZWxzIHZzIFNvZnQgVGFyZ2V0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBoYXJkIGxhYmVsIGZvciBjbGFzcyBcdTAwMjdjYXRcdTAwMjcgaXMgdGhlIG9uZS1ob3QgdmVjdG9yIFswLCAwLCAxLCAwLCDigKZdLCBwcm92aWRpbmcgZXhhY3RseSBvbmUgYml0IG9mIGluZm9ybWF0aW9uOiB3aGljaCBjbGFzcyBpcyBjb3JyZWN0LiBBIHRlYWNoZXJcdTAwMjdzIG91dHB1dCBhdCBzdGFuZGFyZCB0ZW1wZXJhdHVyZSBtaWdodCBiZSBbMC4wMiwgMC4wNSwgMC44OCwgMC4wMSwgMC4wNCwg4oCmXSwgcmV2ZWFsaW5nIHRoYXQgaXQgY29uc2lkZXJzIFx1MDAyN2RvZ1x1MDAyNyBhbmQgXHUwMDI3bHlueFx1MDAyNyByZWxhdGVkIHRvIFx1MDAyN2NhdFx1MDAyNy4gQXQgdGVtcGVyYXR1cmUgVD00IHRoaXMgc29mdGVucyBmdXJ0aGVyIHRvIFswLjA4LCAwLjEyLCAwLjQ1LCAwLjA1LCAwLjExLCDigKZdLCBtYWtpbmcgaW50ZXItY2xhc3Mgc2ltaWxhcml0aWVzIGV2ZW4gbW9yZSB2aXNpYmxlLiBUaGUgc29mdCB0YXJnZXRzIGNhcnJ5IHN0cnVjdHVyYWwga25vd2xlZGdlIHRoYXQgaGFyZCBsYWJlbHMgdGhyb3cgYXdheS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW1wZXJhdHVyZSBTY2FsaW5nIGFuZCBTb2Z0IFRhcmdldHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzb2Z0bWF4IGF0IHRlbXBlcmF0dXJlIFQgaXMgz4Moel9pIC8gVCkgPSBleHAoel9pIC8gVCkgLyDOo19qIGV4cCh6X2ogLyBUKS4gQXQgVD0xIHRoaXMgaXMgdGhlIHN0YW5kYXJkIHNvZnRtYXguIEFzIFQgaW5jcmVhc2VzLCB0aGUgZGlzdHJpYnV0aW9uIGJlY29tZXMgbW9yZSB1bmlmb3JtIGFuZCBpbnRlci1jbGFzcyBsb2dpdCBkaWZmZXJlbmNlcyBiZWNvbWUgbW9yZSB2aXNpYmxlLiBCb3RoIHRlYWNoZXIgYW5kIHN0dWRlbnQgdXNlIHRoZSBzYW1lIHRlbXBlcmF0dXJlIFQgZHVyaW5nIGRpc3RpbGxhdGlvbiwgc28gdGhlIHN0dWRlbnQgbGVhcm5zIHRvIHJlcHJvZHVjZSB0aGUgdGVhY2hlclx1MDAyN3MgcmVsYXRpdmUgY29uZmlkZW5jZSBzdHJ1Y3R1cmUuIEF0IGluZmVyZW5jZSwgVCBpcyByZXNldCB0byAxLiBUeXBpY2FsIHNldHRpbmc6IFQ9NCwgzrE9MC4xLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgc29mdF9kaXN0aWxsYXRpb25fbG9zcyhzdHVkZW50X2xvZ2l0cywgdGVhY2hlcl9sb2dpdHMsIGxhYmVscyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0ZW1wZXJhdHVyZT00LjAsIGFscGhhPTAuMSk6XG4gICAgXCJcIlwiXG4gICAgSGludG9uIGRpc3RpbGxhdGlvbjogTCA9IGFscGhhKkNFKGhhcmQpICsgKDEtYWxwaGEpKlReMipLTChzb2Z0X3RlYWNoZXJ8fHNvZnRfc3R1ZGVudClcbiAgICBCb3RoIHRlYWNoZXIgYW5kIHN0dWRlbnQgc29mdG1heCB1c2UgdGVtcGVyYXR1cmUgVC4gVD0xIGF0IGluZmVyZW5jZS5cbiAgICBcIlwiXCJcbiAgICBoYXJkX2xvc3MgPSBGLmNyb3NzX2VudHJvcHkoc3R1ZGVudF9sb2dpdHMsIGxhYmVscylcblxuICAgICMgU29mdCBkaXN0cmlidXRpb25zIGF0IHRlbXBlcmF0dXJlIFRcbiAgICBzb2Z0X3RlYWNoZXIgPSBGLnNvZnRtYXgodGVhY2hlcl9sb2dpdHMgLyB0ZW1wZXJhdHVyZSwgZGltPS0xKVxuICAgIHNvZnRfc3R1ZGVudCA9IEYubG9nX3NvZnRtYXgoc3R1ZGVudF9sb2dpdHMgLyB0ZW1wZXJhdHVyZSwgZGltPS0xKVxuICAgICMgS0wodGVhY2hlciB8fCBzdHVkZW50KTogdGVhY2hlciBpcyB0YXJnZXQsIHN0dWRlbnQgaXMgcHJlZGljdGlvblxuICAgIGtsX2xvc3MgPSBGLmtsX2Rpdihzb2Z0X3N0dWRlbnQsIHNvZnRfdGVhY2hlciwgcmVkdWN0aW9uPVx1MDAyN2JhdGNobWVhblx1MDAyNylcblxuICAgICMgU2NhbGUgYnkgVF4yOiBjb21wZW5zYXRlcyBmb3IgdGhlIDEvVF4yIGdyYWRpZW50IHNocmlua2FnZSBhdCBoaWdoIFRcbiAgICBkaXN0aWxsX2xvc3MgPSAodGVtcGVyYXR1cmUgKiogMikgKiBrbF9sb3NzXG4gICAgdG90YWwgPSBhbHBoYSAqIGhhcmRfbG9zcyArICgxLjAgLSBhbHBoYSkgKiBkaXN0aWxsX2xvc3NcbiAgICByZXR1cm4gdG90YWwsIGhhcmRfbG9zcy5pdGVtKCksIGRpc3RpbGxfbG9zcy5pdGVtKClcblxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxudGVhY2hlcl9sb2dpdHMgPSB0b3JjaC5yYW5kbig4LCAxMCkgKiAzLjBcbnN0dWRlbnRfbG9naXRzID0gdG9yY2gucmFuZG4oOCwgMTApXG5sYWJlbHMgPSB0b3JjaC5yYW5kaW50KDAsIDEwLCAoOCwpKVxuXG5mb3IgVCBpbiBbMS4wLCA0LjAsIDEwLjBdOlxuICAgIGxvc3MsIGhhcmQsIGtkID0gc29mdF9kaXN0aWxsYXRpb25fbG9zcyhcbiAgICAgICAgc3R1ZGVudF9sb2dpdHMsIHRlYWNoZXJfbG9naXRzLCBsYWJlbHMsIHRlbXBlcmF0dXJlPVQpXG4gICAgcHJpbnQoZlx1MDAyN1Q9e1Q6LjBmfTogdG90YWw9e2xvc3MuaXRlbSgpOi40Zn0gIGhhcmQ9e2hhcmQ6LjRmfSAga2Q9e2tkOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIFTCsiBTY2FsZSBGYWN0b3IgYW5kIEdyYWRpZW50IENvbXBlbnNhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiB0ZW1wZXJhdHVyZSBUIGlzIGFwcGxpZWQsIHRoZSBncmFkaWVudHMgb2YgdGhlIEtMIHRlcm0gd2l0aCByZXNwZWN0IHRvIHRoZSBzdHVkZW50IGxvZ2l0cyBzaHJpbmsgYnkgYSBmYWN0b3Igb2YgMS9UwrIuIFdpdGhvdXQgY29tcGVuc2F0aW9uLCBoaWdoZXIgdGVtcGVyYXR1cmVzIHByb2R1Y2UgbmVnbGlnaWJseSBzbWFsbCBLTCBncmFkaWVudHMsIG1ha2luZyB0aGUgZGlzdGlsbGF0aW9uIHNpZ25hbCBkaXNhcHBlYXIuIE11bHRpcGx5aW5nIHRoZSBLTCBsb3NzIGJ5IFTCsiByZXN0b3JlcyB0aGUgZ3JhZGllbnQgbWFnbml0dWRlIHRvIHRoZSBzYW1lIHNjYWxlIGFzIFQ9MSwgZW5zdXJpbmcgdGhlIGRpc3RpbGxhdGlvbiBzaWduYWwgaXMgbm90IG92ZXJ3aGVsbWVkIGJ5IHRoZSBoYXJkLWxhYmVsIGNyb3NzLWVudHJvcHkgcmVnYXJkbGVzcyBvZiB0ZW1wZXJhdHVyZSBjaG9pY2UuIFRoaXMgaXMgd2h5IHRoZSBjb21iaW5lZCBsb3NzIHVzZXMgKDEtzrEpVMKywrdLTCjPgyh6X3QvVCksIM+DKHpfcy9UKSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgc2hvd190ZW1wZXJhdHVyZV9lZmZlY3QobG9naXRzLCB0ZW1wZXJhdHVyZXM9KDEsIDQsIDEwLCAyMCkpOlxuICAgIFwiXCJcIlNob3cgaG93IHRlbXBlcmF0dXJlIFQgc29mdGVucyB0aGUgb3V0cHV0IGRpc3RyaWJ1dGlvbi5cIlwiXCJcbiAgICBwcmludChmXHUwMDI3e1wiVFwiOlx1MDAzZTR9ICB7XCJNYXggUFwiOlx1MDAzZTh9ICB7XCJFbnRyb3B5XCI6XHUwMDNlOX0gIHtcIjJuZCBQXCI6XHUwMDNlOH0gIHtcIlNoYXBlXCJ9XHUwMDI3KVxuICAgIHByaW50KFx1MDAyNy1cdTAwMjcgKiA1MilcbiAgICBmb3IgVCBpbiB0ZW1wZXJhdHVyZXM6XG4gICAgICAgIHAgPSBGLnNvZnRtYXgobG9naXRzIC8gVCwgZGltPTApXG4gICAgICAgIHNvcnRlZF9wID0gcC5zb3J0KGRlc2NlbmRpbmc9VHJ1ZSkudmFsdWVzXG4gICAgICAgIGVudHJvcHkgPSAtKHAgKiAocCArIDFlLTkpLmxvZygpKS5zdW0oKS5pdGVtKClcbiAgICAgICAgc2hhcGUgPSBcdTAwMjdzaGFycFx1MDAyNyBpZiBUIFx1MDAzYz0gMSBlbHNlIFx1MDAyN21vZGVyYXRlXHUwMDI3IGlmIFQgXHUwMDNjPSA0IGVsc2UgXHUwMDI3c29mdFx1MDAyN1xuICAgICAgICBwcmludChmXHUwMDI3e1Q6XHUwMDNlNH0gIHtzb3J0ZWRfcFswXS5pdGVtKCk6XHUwMDNlOC40Zn0gIHtlbnRyb3B5Olx1MDAzZTkuNGZ9ICBcdTAwMjdcbiAgICAgICAgICAgICAgZlx1MDAyN3tzb3J0ZWRfcFsxXS5pdGVtKCk6XHUwMDNlOC40Zn0gIHtzaGFwZX1cdTAwMjcpXG5cbiMgU2ltdWxhdGVkIHRlYWNoZXIgbG9naXRzOiBjbGFzcyAyIGlzIGNvcnJlY3QsIGNsYXNzIDAgaXMgc3RydWN0dXJhbGx5IHNpbWlsYXJcbmxvZ2l0cyA9IHRvcmNoLnRlbnNvcihbMS41LCAwLjQsIDQuMiwgLTAuOCwgMC4xLCAtMC41LCAwLjMsIC0xLjAsIDAuNiwgLTAuMl0pXG5zaG93X3RlbXBlcmF0dXJlX2VmZmVjdChsb2dpdHMpXG5cbnBfdDEgID0gRi5zb2Z0bWF4KGxvZ2l0cyAvIDEsICBkaW09MClcbnBfdDEwID0gRi5zb2Z0bWF4KGxvZ2l0cyAvIDEwLCBkaW09MClcbnByaW50KGZcdTAwMjdDbGFzcy0wIHByb2I6IFQ9MSAtXHUwMDNlIHtwX3QxWzBdLml0ZW0oKTouNGZ9LCAgVD0xMCAtXHUwMDNlIHtwX3QxMFswXS5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN0hpZ2ggVCByZXZlYWxzIHN0cnVjdHVyYWwgc2ltaWxhcml0eSDigJQgZG9nIGlzIG1vcmUgbGlrZSBjYXQgdGhhbiBjYXIuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZ1bGwgRGlzdGlsbGF0aW9uIFRyYWluaW5nIExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkR1cmluZyBkaXN0aWxsYXRpb24gdGhlIHRlYWNoZXIgaXMgZnJvemVuIOKAlCBpdHMgd2VpZ2h0cyBkbyBub3QgY2hhbmdlLiBPbmx5IHN0dWRlbnQgd2VpZ2h0cyBhcmUgdXBkYXRlZC4gVGhlIGNvbWJpbmVkIGxvc3MgYmxlbmRzIGhhcmQgY3Jvc3MtZW50cm9weSAozrEgPSAwLjEgdHlwaWNhbGx5LCBzbyAxMCUgb2YgdGhlIGxvc3MpIHdpdGggdGhlIHNjYWxlZCBLTCBkaXN0aWxsYXRpb24gdGVybSAoOTAlKS4gVXNpbmcgYSBzbWFsbCDOsSBnaXZlcyBtb3N0IHdlaWdodCB0byB0aGUgdGVhY2hlclx1MDAyN3Mgc29mdCB0YXJnZXRzLiBBZnRlciB0cmFpbmluZywgdGhlIGFkYXB0ZXIgbGF5ZXIgKHVzZWQgb25seSB0byBtYXRjaCBsb2dpdCBkaW1lbnNpb25zIGlmIHRlYWNoZXIgYW5kIHN0dWRlbnQgaGF2ZSBkaWZmZXJlbnQgb3V0cHV0IHNpemVzKSBpcyBkaXNjYXJkZWQ7IHRoZSBzdHVkZW50IGhlYWQgaXMgdGhlIG9ubHkgb3V0cHV0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuXG5kZWYgdHJhaW5fd2l0aF9kaXN0aWxsYXRpb24odGVhY2hlciwgc3R1ZGVudCwgdHJhaW5fbG9hZGVyLCBkZXZpY2UsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRlbXBlcmF0dXJlPTQuMCwgYWxwaGE9MC4xLCBlcG9jaHM9MywgbHI9MWUtMyk6XG4gICAgXCJcIlwiVGVhY2hlciBmcm96ZW47IHN0dWRlbnQgdHJhaW5lZCBvbiBDRSArIHNjYWxlZCBLRCBsb3NzLlwiXCJcIlxuICAgIHRlYWNoZXIuZXZhbCgpXG4gICAgZm9yIHAgaW4gdGVhY2hlci5wYXJhbWV0ZXJzKCk6XG4gICAgICAgIHAucmVxdWlyZXNfZ3JhZF8oRmFsc2UpXG4gICAgb3B0aW1pemVyID0gb3B0aW0uQWRhbShzdHVkZW50LnBhcmFtZXRlcnMoKSwgbHI9bHIpXG4gICAgVCA9IHRlbXBlcmF0dXJlXG4gICAgZm9yIGVwb2NoIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIHN0dWRlbnQudHJhaW4oKVxuICAgICAgICB0b3RhbCwgY29ycmVjdCwgbiA9IDAuMCwgMCwgMFxuICAgICAgICBmb3IgWCwgeSBpbiB0cmFpbl9sb2FkZXI6XG4gICAgICAgICAgICBYLCB5ID0gWC50byhkZXZpY2UpLCB5LnRvKGRldmljZSlcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIHRfbG9naXRzID0gdGVhY2hlcihYKVxuICAgICAgICAgICAgc19sb2dpdHMgPSBzdHVkZW50KFgpXG4gICAgICAgICAgICBoYXJkID0gRi5jcm9zc19lbnRyb3B5KHNfbG9naXRzLCB5KVxuICAgICAgICAgICAgc29mdF90ID0gRi5zb2Z0bWF4KHRfbG9naXRzIC8gVCwgZGltPS0xKVxuICAgICAgICAgICAgc29mdF9zID0gRi5sb2dfc29mdG1heChzX2xvZ2l0cyAvIFQsIGRpbT0tMSlcbiAgICAgICAgICAgIGtkID0gRi5rbF9kaXYoc29mdF9zLCBzb2Z0X3QsIHJlZHVjdGlvbj1cdTAwMjdiYXRjaG1lYW5cdTAwMjcpICogVCAqKiAyXG4gICAgICAgICAgICBsb3NzID0gYWxwaGEgKiBoYXJkICsgKDEgLSBhbHBoYSkgKiBrZFxuICAgICAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgICAgIHRvdGFsICs9IGxvc3MuaXRlbSgpXG4gICAgICAgICAgICBjb3JyZWN0ICs9IChzX2xvZ2l0cy5hcmdtYXgoMSkgPT0geSkuc3VtKCkuaXRlbSgpXG4gICAgICAgICAgICBuICs9IHkuc2l6ZSgwKVxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NoKzF9OiBsb3NzPXt0b3RhbC9sZW4odHJhaW5fbG9hZGVyKTouNGZ9ICBhY2M9e2NvcnJlY3QvbjouM2Z9XHUwMDI3KVxuXG5wcmludChcdTAwMjdUeXBpY2FsOiB0ZW1wZXJhdHVyZT00LCBhbHBoYT0wLjEgKDEwJSBoYXJkIENFLCA5MCUgc29mdCBLRCkuXHUwMDI3KVxucHJpbnQoXHUwMDI3VGVhY2hlciBpcyBmcm96ZW4gdGhyb3VnaG91dDsgb25seSBzdHVkZW50IHdlaWdodHMgYXJlIHVwZGF0ZWQuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRhcmsgS25vd2xlZGdlIGFuZCBJbnRlci1DbGFzcyBTaW1pbGFyaXRpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkhpbnRvbiBjb2luZWQgdGhlIHRlcm0gXHUwMDI3ZGFyayBrbm93bGVkZ2VcdTAwMjcgZm9yIHRoZSBpbmZvcm1hdGlvbiBlbmNvZGVkIGluIHRoZSB0ZWFjaGVyXHUwMDI3cyBub24tbWF4aW11bSBwcm9iYWJpbGl0aWVzLiBBIHRlYWNoZXIgdHJhaW5lZCBvbiBJbWFnZU5ldCB0aGF0IGdpdmVzIGNhdDowLjcwLCBkb2c6MC4yMCwgbGlvbjowLjA1IGlzIGVuY29kaW5nIHRoZSBnZW9tZXRyaWMgZmFjdCB0aGF0IGNhdHMgYW5kIGRvZ3MgYXJlIG1vcmUgc2ltaWxhciB0byBlYWNoIG90aGVyIHRoYW4gZWl0aGVyIGlzIHRvIGEgY2FyLiBUaGlzIHNpbWlsYXJpdHkgc3RydWN0dXJlIHdhcyBsZWFybmVkIGZyb20gZGF0YTogdGhlIHRlYWNoZXIgc2F3IG1hbnkgYW1iaWd1b3VzIGNhdC1kb2cgaW1hZ2VzIGR1cmluZyB0cmFpbmluZyBhbmQgaW50ZXJuYWxpemVkIHRob3NlIHJlbGF0aW9uc2hpcHMgaW4gaXRzIGxvZ2l0cy4gSGFyZCBsYWJlbHMgZXJhc2UgdGhpczsgc29mdCB0YXJnZXRzIHByZXNlcnZlIGl0LiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiRGFyayBLbm93bGVkZ2UgSHlwb3RoZXNpcyIsImNvbnRlbnQiOiJUaGUgc29mdCB0YXJnZXRzIGNhcnJ5IG1vcmUgaW5mb3JtYXRpb24gcGVyIHNhbXBsZSB0aGFuIGhhcmQgbGFiZWxzIGJlY2F1c2UgZWFjaCBvdXRwdXQgdmVjdG9yIGVuY29kZXMgYSBmdWxsIHJhbmtpbmcgb3ZlciBhbGwgY2xhc3Nlcy4gRW1waXJpY2FsbHksIGRpc3RpbGxpbmcgd2l0aCBldmVuIGEgc21hbGwgYW1vdW50IG9mIHJlYWwgZGF0YSBhbmQgYSBsYXJnZSBhbW91bnQgb2YgdW5sYWJlbGVkIGRhdGEgY2FuIG91dHBlcmZvcm0gdHJhaW5pbmcgb24gdGhlIGZ1bGwgbGFiZWxlZCBkYXRhc2V0IOKAlCB0aGUgdGVhY2hlclx1MDAyN3Mgc29mdCBvdXRwdXRzIHN1YnN0aXR1dGUgZm9yIGxhYmVscyBvbiB0aGUgdW5sYWJlbGVkIHBvcnRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2hlbiBEaXN0aWxsYXRpb24gSGVscHMgYW5kIFdoZW4gSXQgRG9lcyBOb3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Iktub3dsZWRnZSBkaXN0aWxsYXRpb24gaXMgbm90IHVuaXZlcnNhbGx5IGJlbmVmaWNpYWwuIEl0IHdvcmtzIGJlc3Qgd2hlbiB0aGUgdGVhY2hlciBpcyB3ZWxsLWNhbGlicmF0ZWQgYW5kIHNpZ25pZmljYW50bHkgbW9yZSBjYXBhYmxlIHRoYW4gdGhlIHN0dWRlbnQsIHRoZSBkYXRhc2V0IGlzIHNtYWxsIG9yIG1lZGl1bS1zaXplZCAoc28gc29mdCB0YXJnZXRzIGFkZCBtZWFuaW5nZnVsIHNpZ25hbCBiZXlvbmQgd2hhdCB0aGUgZGF0YSBwcm92aWRlcyksIGFuZCB0aGUgdGVhY2hlciBhbmQgc3R1ZGVudCBvcGVyYXRlIG9uIHRoZSBzYW1lIGRvbWFpbiBhbmQgdGFzay4gSXQgZGVncmFkZXMgd2hlbiB0aGUgdGVhY2hlciBpcyBwb29ybHkgY2FsaWJyYXRlZCAoaXRzIHNvZnQgdGFyZ2V0cyBhcmUgbWlzbGVhZGluZyksIHRoZXJlIGlzIGEgZG9tYWluIG1pc21hdGNoIGJldHdlZW4gdGVhY2hlciBwcmV0cmFpbmluZyBhbmQgc3R1ZGVudCBmaW5lLXR1bmluZywgb3IgdGhlIHN0dWRlbnQgaXMgYWxyZWFkeSBuZWFyIHRoZSB0ZWFjaGVyXHUwMDI3cyBjYXBhY2l0eS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkhlbHBzOiBsYXJnZSB0ZWFjaGVyLXN0dWRlbnQgY2FwYWNpdHkgZ2FwIOKAlCBzdHVkZW50IGNhbm5vdCBpbmRlcGVuZGVudGx5IGxlYXJuIHRoZSBkZWNpc2lvbiBib3VuZGFyeS4iLCJIZWxwczogbGltaXRlZCBsYWJlbGVkIGRhdGEg4oCUIHNvZnQgdGFyZ2V0cyBlZmZlY3RpdmVseSBhdWdtZW50IHN1cGVydmlzaW9uIHdpdGggY2xhc3Mgc3RydWN0dXJlLiIsIkhlbHBzOiBib3JuLWFnYWluIG5ldHdvcmtzIOKAlCBzYW1lIGNhcGFjaXR5IHN0dWRlbnQgYmVuZWZpdHMgZnJvbSBzb2Z0IHRhcmdldHMgKEZ1cmxhbmVsbG8gMjAxOCkuIiwiRG9lcyBOT1QgaGVscDogdGVhY2hlciBpcyBiYWRseSBjYWxpYnJhdGVkIChvdmVyY29uZmlkZW50IG9yIHVuZGVyY29uZmlkZW50IG9uIHNvZnQgY2xhc3NlcykuIiwiRG9lcyBOT1QgaGVscDogZG9tYWluIG1pc21hdGNoIGJldHdlZW4gdGVhY2hlciB0cmFpbmluZyBkaXN0cmlidXRpb24gYW5kIHN0dWRlbnQgdGFyZ2V0IHRhc2suIiwiRG9lcyBOT1QgaGVscDogdmVyeSBsYXJnZSBkYXRhc2V0cyB3aGVyZSB0aGUgc3R1ZGVudCBjYW4gbGVhcm4gY2xhc3Mgc3RydWN0dXJlIGZyb20gZGF0YSBhbG9uZS4iLCJNYXJnaW5hbDogc3R1ZGVudCBtdWNoIHNtYWxsZXIgdGhhbiB0ZWFjaGVyIChjYXBhY2l0eSBnYXAgdG9vIGxhcmdlOyBpbnRlcm1lZGlhdGUgZGlzdGlsbGF0aW9uIGhlbHBzIG1vcmUpLiJdfSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgSWxsdXN0cmF0aXZlIENJRkFSLTEwIGFjY3VyYWN5OiBzYW1lIHN0dWRlbnQgYXJjaGl0ZWN0dXJlLCBzYW1lIHRyYWluaW5nIGJ1ZGdldFxuIyBUZWFjaGVyOiBSZXNOZXQtNTYgKDkzLjAlIHRvcC0xKS4gQWxsIHN0dWRlbnRzOiBzYW1lIENOTiwgZGlmZmVyZW50IHN1cGVydmlzaW9uLlxuY29uZmlncyA9IFtcbiAgICAoXHUwMDI3UmVzTmV0LTggIChoYXJkIGxhYmVscylcdTAwMjcsICAgODUuMiksXG4gICAgKFx1MDAyN1Jlc05ldC04ICAoc29mdCBUPTQpXHUwMDI3LCAgICAgIDg3LjgpLFxuICAgIChcdTAwMjdSZXNOZXQtMTQgKGhhcmQgbGFiZWxzKVx1MDAyNywgIDg5LjEpLFxuICAgIChcdTAwMjdSZXNOZXQtMTQgKHNvZnQgVD00KVx1MDAyNywgICAgIDkxLjMpLFxuICAgIChcdTAwMjdSZXNOZXQtMjAgKGhhcmQgbGFiZWxzKVx1MDAyNywgIDkxLjQpLFxuICAgIChcdTAwMjdSZXNOZXQtMjAgKHNvZnQgVD00KVx1MDAyNywgICAgIDkzLjApLFxuICAgIChcdTAwMjdSZXNOZXQtMjAgYm9ybi1hZ2Fpblx1MDAyNywgICAgIDkyLjcpLCAgIyBzYW1lLWNhcGFjaXR5IHRlYWNoZXIgLVx1MDAzZSBzdHVkZW50XG5dXG5cbnByaW50KGZcdTAwMjd7XCJDb25maWd1cmF0aW9uXCI6XHUwMDNjMjh9IHtcIkFjYyAoJSlcIjpcdTAwM2U4fVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiAzOClcbmZvciBuYW1lLCBhY2MgaW4gY29uZmlnczpcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMjh9IHthY2M6XHUwMDNlOC4xZn1cdTAwMjcpXG5cbnBhaXJzID0gWyhjb25maWdzWzBdWzFdLCBjb25maWdzWzFdWzFdKSxcbiAgICAgICAgIChjb25maWdzWzJdWzFdLCBjb25maWdzWzNdWzFdKSxcbiAgICAgICAgIChjb25maWdzWzRdWzFdLCBjb25maWdzWzVdWzFdKV1cbmdhaW5zID0gW3MgLSBoIGZvciBoLCBzIGluIHBhaXJzXVxucHJpbnQoZlx1MDAyN0F2ZXJhZ2UgZ2FpbiBmcm9tIHNvZnQgdGFyZ2V0czogK3tucC5tZWFuKGdhaW5zKTouMmZ9JVx1MDAyNylcbnByaW50KGZcdTAwMjdCb3JuLWFnYWluIGdhaW46ICt7Y29uZmlnc1s2XVsxXSAtIGNvbmZpZ3NbNF1bMV06LjFmfSUgKHNhbWUgY2FwYWNpdHksIHNvZnQgdGFyZ2V0cyBvbmx5KVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCb3JuLUFnYWluIE5ldHdvcmtzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCb3JuLWFnYWluIG5ldHdvcmtzIChGdXJsYW5lbGxvIGV0IGFsLiAyMDE4KSBzaG93IHRoYXQgZGlzdGlsbGluZyBhIG1vZGVsIGludG8gYSBzdHVkZW50IG9mIGlkZW50aWNhbCBhcmNoaXRlY3R1cmUgc3RpbGwgaW1wcm92ZXMgYWNjdXJhY3kuIFRoZSBzdHVkZW50IHRyYWluZWQgd2l0aCBzb2Z0IHRhcmdldHMgZnJvbSBhIHNhbWUtY2FwYWNpdHkgdGVhY2hlciBvdXRwZXJmb3JtcyB0aGUgdGVhY2hlciB0cmFpbmVkIHdpdGggaGFyZCBsYWJlbHMgYWxvbmUuIFRoaXMgZGVtb25zdHJhdGVzIHRoYXQgdGhlIGJlbmVmaXQgb2YgZGlzdGlsbGF0aW9uIGlzIG5vdCBwdXJlbHkgYWJvdXQgY29tcHJlc3NpbmcgYSBsYXJnZXIgbW9kZWwg4oCUIHRoZSBzb2Z0IHRhcmdldHMgdGhlbXNlbHZlcyBhcmUgYSBiZXR0ZXIgdHJhaW5pbmcgc2lnbmFsLCBpbmRlcGVuZGVudCBvZiBjYXBhY2l0eSB0cmFuc2Zlci4gRW5zZW1ibGluZyBtdWx0aXBsZSBib3JuLWFnYWluIGdlbmVyYXRpb25zIGZ1cnRoZXIgaW1wcm92ZXMgcGVyZm9ybWFuY2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlRlbXBlcmF0dXJlIiwiTWF4IFByb2JhYmlsaXR5IiwiRW50cm9weSIsIkludGVyLWNsYXNzIEluZm8iLCJHcmFkaWVudCBTY2FsZSIsIlR5cGljYWwgQWNjIEdhaW4iXSwicm93cyI6W1siVD0xIChoYXJkKSIsIn4wLjk1IChzaGFycCkiLCJMb3ciLCJNaW5pbWFsIOKAlCBuZWFyIG9uZS1ob3QiLCIxw5cgKGJhc2VsaW5lKSIsIkJhc2VsaW5lIl0sWyJUPTQgKHR5cGljYWwpIiwifjAuNDUgKG1vZGVyYXRlKSIsIk1lZGl1bSIsIlJpY2gg4oCUIHNpbWlsYXJpdGllcyB2aXNpYmxlIiwiVMKyPTE2w5ciLCIrMS414oCTMi41JSJdLFsiVD0xMCAoc29mdCkiLCJ+MC4yNSAoc29mdCkiLCJIaWdoIiwiVmVyeSByaWNoIOKAlCBzdHJ1Y3R1cmUgd2VsbCBleHBvc2VkIiwiVMKyPTEwMMOXIiwiKzIuMOKAkzMuMCUiXSxbIlQ9MjAgKHZlcnkgc29mdCkiLCJ+MC4xNSAobmVhciB1bmlmb3JtKSIsIlZlcnkgaGlnaCIsIk1heGltdW0g4oCUIG5lYXJseSB1bmlmb3JtIiwiVMKyPTQwMMOXIChtYXkgZGVzdGFiaWxpemUpIiwiT2Z0ZW4gZGVncmFkZXMiXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Hinton Knowledge Distillation — Soft Targets and Temperature

Knowledge distillation (Hinton et al. 2015) transfers knowledge from a large, accurate teacher network into a small, fast student. The key insight is that a teacher's full output distribution over all classes encodes rich structural information learned from data — information that one-hot hard labels discard entirely. Training the student to match this soft distribution transfers inter-class relationships, not just the identity of the correct class.

## Hard Labels vs Soft Targets

A hard label for class 'cat' is the one-hot vector [0, 0, 1, 0, …], providing exactly one bit of information: which class is correct. A teacher's output at standard temperature might be [0.02, 0.05, 0.88, 0.01, 0.04, …], revealing that it considers 'dog' and 'lynx' related to 'cat'. At temperature T=4 this softens further to [0.08, 0.12, 0.45, 0.05, 0.11, …], making inter-class similarities even more visible. The soft targets carry structural knowledge that hard labels throw away.

## Temperature Scaling and Soft Targets

The softmax at temperature T is σ(z_i / T) = exp(z_i / T) / Σ_j exp(z_j / T). At T=1 this is the standard softmax. As T increases, the distribution becomes more uniform and inter-class logit differences become more visible. Both teacher and student use the same temperature T during distillation, so the student learns to reproduce the teacher's relative confidence structure. At inference, T is reset to 1. Typical setting: T=4, α=0.1.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def soft_distillation_loss(student_logits, teacher_logits, labels,
                            temperature=4.0, alpha=0.1):
    """
    Hinton distillation: L = alpha*CE(hard) + (1-alpha)*T^2*KL(soft_teacher||soft_student)
    Both teacher and student softmax use temperature T. T=1 at inference.
    """
    hard_loss = F.cross_entropy(student_logits, labels)

    # Soft distributions at temperature T
    soft_teacher = F.softmax(teacher_logits / temperature, dim=-1)
    soft_student = F.log_softmax(student_logits / temperature, dim=-1)
    # KL(teacher || student): teacher is target, student is prediction
    kl_loss = F.kl_div(soft_student, soft_teacher, reduction='batchmean')

    # Scale by T^2: compensates for the 1/T^2 gradient shrinkage at high T
    distill_loss = (temperature ** 2) * kl_loss
    total = alpha * hard_loss + (1.0 - alpha) * distill_loss
    return total, hard_loss.item(), distill_loss.item()


torch.manual_seed(0)
teacher_logits = torch.randn(8, 10) * 3.0
student_logits = torch.randn(8, 10)
labels = torch.randint(0, 10, (8,))

for T in [1.0, 4.0, 10.0]:
    loss, hard, kd = soft_distillation_loss(
        student_logits, teacher_logits, labels, temperature=T)
    print(f'T={T:.0f}: total={loss.item():.4f}  hard={hard:.4f}  kd={kd:.4f}')
```

## The T² Scale Factor and Gradient Compensation

When temperature T is applied, the gradients of the KL term with respect to the student logits shrink by a factor of 1/T². Without compensation, higher temperatures produce negligibly small KL gradients, making the distillation signal disappear. Multiplying the KL loss by T² restores the gradient magnitude to the same scale as T=1, ensuring the distillation signal is not overwhelmed by the hard-label cross-entropy regardless of temperature choice. This is why the combined loss uses (1-α)T²·KL(σ(z_t/T), σ(z_s/T)).

```python
import torch
import torch.nn.functional as F

def show_temperature_effect(logits, temperatures=(1, 4, 10, 20)):
    """Show how temperature T softens the output distribution."""
    print(f'{"T":>4}  {"Max P":>8}  {"Entropy":>9}  {"2nd P":>8}  {"Shape"}')
    print('-' * 52)
    for T in temperatures:
        p = F.softmax(logits / T, dim=0)
        sorted_p = p.sort(descending=True).values
        entropy = -(p * (p + 1e-9).log()).sum().item()
        shape = 'sharp' if T <= 1 else 'moderate' if T <= 4 else 'soft'
        print(f'{T:>4}  {sorted_p[0].item():>8.4f}  {entropy:>9.4f}  '
              f'{sorted_p[1].item():>8.4f}  {shape}')

# Simulated teacher logits: class 2 is correct, class 0 is structurally similar
logits = torch.tensor([1.5, 0.4, 4.2, -0.8, 0.1, -0.5, 0.3, -1.0, 0.6, -0.2])
show_temperature_effect(logits)

p_t1  = F.softmax(logits / 1,  dim=0)
p_t10 = F.softmax(logits / 10, dim=0)
print(f'Class-0 prob: T=1 -> {p_t1[0].item():.4f},  T=10 -> {p_t10[0].item():.4f}')
print('High T reveals structural similarity — dog is more like cat than car.')
```

## Full Distillation Training Loop

During distillation the teacher is frozen — its weights do not change. Only student weights are updated. The combined loss blends hard cross-entropy (α = 0.1 typically, so 10% of the loss) with the scaled KL distillation term (90%). Using a small α gives most weight to the teacher's soft targets. After training, the adapter layer (used only to match logit dimensions if teacher and student have different output sizes) is discarded; the student head is the only output.

```python
import torch
import torch.nn.functional as F
import torch.optim as optim

def train_with_distillation(teacher, student, train_loader, device,
                             temperature=4.0, alpha=0.1, epochs=3, lr=1e-3):
    """Teacher frozen; student trained on CE + scaled KD loss."""
    teacher.eval()
    for p in teacher.parameters():
        p.requires_grad_(False)
    optimizer = optim.Adam(student.parameters(), lr=lr)
    T = temperature
    for epoch in range(epochs):
        student.train()
        total, correct, n = 0.0, 0, 0
        for X, y in train_loader:
            X, y = X.to(device), y.to(device)
            with torch.no_grad():
                t_logits = teacher(X)
            s_logits = student(X)
            hard = F.cross_entropy(s_logits, y)
            soft_t = F.softmax(t_logits / T, dim=-1)
            soft_s = F.log_softmax(s_logits / T, dim=-1)
            kd = F.kl_div(soft_s, soft_t, reduction='batchmean') * T ** 2
            loss = alpha * hard + (1 - alpha) * kd
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total += loss.item()
            correct += (s_logits.argmax(1) == y).sum().item()
            n += y.size(0)
        print(f'Epoch {epoch+1}: loss={total/len(train_loader):.4f}  acc={correct/n:.3f}')

print('Typical: temperature=4, alpha=0.1 (10% hard CE, 90% soft KD).')
print('Teacher is frozen throughout; only student weights are updated.')
```

## Dark Knowledge and Inter-Class Similarities

Hinton coined the term 'dark knowledge' for the information encoded in the teacher's non-maximum probabilities. A teacher trained on ImageNet that gives cat:0.70, dog:0.20, lion:0.05 is encoding the geometric fact that cats and dogs are more similar to each other than either is to a car. This similarity structure was learned from data: the teacher saw many ambiguous cat-dog images during training and internalized those relationships in its logits. Hard labels erase this; soft targets preserve it.

> **Dark Knowledge Hypothesis**: The soft targets carry more information per sample than hard labels because each output vector encodes a full ranking over all classes. Empirically, distilling with even a small amount of real data and a large amount of unlabeled data can outperform training on the full labeled dataset — the teacher's soft outputs substitute for labels on the unlabeled portion.

## When Distillation Helps and When It Does Not

Knowledge distillation is not universally beneficial. It works best when the teacher is well-calibrated and significantly more capable than the student, the dataset is small or medium-sized (so soft targets add meaningful signal beyond what the data provides), and the teacher and student operate on the same domain and task. It degrades when the teacher is poorly calibrated (its soft targets are misleading), there is a domain mismatch between teacher pretraining and student fine-tuning, or the student is already near the teacher's capacity.

- Helps: large teacher-student capacity gap — student cannot independently learn the decision boundary.
- Helps: limited labeled data — soft targets effectively augment supervision with class structure.
- Helps: born-again networks — same capacity student benefits from soft targets (Furlanello 2018).
- Does NOT help: teacher is badly calibrated (overconfident or underconfident on soft classes).
- Does NOT help: domain mismatch between teacher training distribution and student target task.
- Does NOT help: very large datasets where the student can learn class structure from data alone.
- Marginal: student much smaller than teacher (capacity gap too large; intermediate distillation helps more).

```python
import numpy as np

# Illustrative CIFAR-10 accuracy: same student architecture, same training budget
# Teacher: ResNet-56 (93.0% top-1). All students: same CNN, different supervision.
configs = [
    ('ResNet-8  (hard labels)',   85.2),
    ('ResNet-8  (soft T=4)',      87.8),
    ('ResNet-14 (hard labels)',  89.1),
    ('ResNet-14 (soft T=4)',     91.3),
    ('ResNet-20 (hard labels)',  91.4),
    ('ResNet-20 (soft T=4)',     93.0),
    ('ResNet-20 born-again',     92.7),  # same-capacity teacher -> student
]

print(f'{"Configuration":<28} {"Acc (%)":>8}')
print('-' * 38)
for name, acc in configs:
    print(f'{name:<28} {acc:>8.1f}')

pairs = [(configs[0][1], configs[1][1]),
         (configs[2][1], configs[3][1]),
         (configs[4][1], configs[5][1])]
gains = [s - h for h, s in pairs]
print(f'Average gain from soft targets: +{np.mean(gains):.2f}%')
print(f'Born-again gain: +{configs[6][1] - configs[4][1]:.1f}% (same capacity, soft targets only)')
```

## Born-Again Networks

Born-again networks (Furlanello et al. 2018) show that distilling a model into a student of identical architecture still improves accuracy. The student trained with soft targets from a same-capacity teacher outperforms the teacher trained with hard labels alone. This demonstrates that the benefit of distillation is not purely about compressing a larger model — the soft targets themselves are a better training signal, independent of capacity transfer. Ensembling multiple born-again generations further improves performance.

| Temperature | Max Probability | Entropy | Inter-class Info | Gradient Scale | Typical Acc Gain |
| --- | --- | --- | --- | --- | --- |
| T=1 (hard) | ~0.95 (sharp) | Low | Minimal — near one-hot | 1× (baseline) | Baseline |
| T=4 (typical) | ~0.45 (moderate) | Medium | Rich — similarities visible | T²=16× | +1.5–2.5% |
| T=10 (soft) | ~0.25 (soft) | High | Very rich — structure well exposed | T²=100× | +2.0–3.0% |
| T=20 (very soft) | ~0.15 (near uniform) | Very high | Maximum — nearly uniform | T²=400× (may destabilize) | Often degrades |

---

