---
title: "ORPO — Odds Ratio Preference Optimization Without a Reference Model"
slug: "orpo-odds-ratio"
description: "ORPO (Hong et al., 2024) eliminates the reference model entirely by combining supervised fine-tuning and preference alignment into a single training stage, using an odds ratio loss that directly contrasts chosen and rejected sequences through probability ratios rather than log-ratio differences."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT1JQTyAoT2RkcyBSYXRpbyBQcmVmZXJlbmNlIE9wdGltaXphdGlvbiwgSG9uZyBldCBhbC4gMjAyNCkgdGFrZXMgYSBmdW5kYW1lbnRhbGx5IGRpZmZlcmVudCBhcHByb2FjaCB0byBMTE0gYWxpZ25tZW50OiBpdCByZW1vdmVzIHRoZSByZWZlcmVuY2UgbW9kZWwgZW50aXJlbHkgYW5kIGNvbWJpbmVzIHN1cGVydmlzZWQgZmluZS10dW5pbmcgKFNGVCkgd2l0aCBwcmVmZXJlbmNlIGxlYXJuaW5nIGludG8gYSBzaW5nbGUgdHJhaW5pbmcgc3RhZ2UuIFByZXZpb3VzIG1ldGhvZHMg4oCUIFBQTywgRFBPLCBJUE8g4oCUIGFsbCByZXF1aXJlIGEgZnJvemVuIHJlZmVyZW5jZSBwb2xpY3kgcGlfcmVmIHRvIGFuY2hvciB0aGUgb3B0aW1pemF0aW9uIHZpYSBhIEtMIGRpdmVyZ2VuY2UgY29uc3RyYWludC4gVGhpcyByZWZlcmVuY2UgbW9kZWwgZG91YmxlcyAob3IgcXVhZHJ1cGxlcywgaW4gUFBPXHUwMDI3cyBjYXNlKSB0aGUgR1BVIG1lbW9yeSByZXF1aXJlbWVudC4gT1JQT1x1MDAyN3MgaW5zaWdodCBpcyB0aGF0IHRoZSBTRlQgbG9zcyBpdHNlbGYgcHJvdmlkZXMgdGhlIHJlZmVyZW5jZSBzaWduYWw6IGJ5IGpvaW50bHkgbWF4aW1pemluZyBjaG9zZW4gcmVzcG9uc2UgbGlrZWxpaG9vZCBhbmQgdGhlIG9kZHMgcmF0aW8gYmV0d2VlbiBjaG9zZW4gYW5kIHJlamVjdGVkIHJlc3BvbnNlcywgdGhlIG1vZGVsIGxlYXJucyBib3RoIHRhc2sgY29tcGV0ZW5jZSBhbmQgcHJlZmVyZW5jZSBhbGlnbm1lbnQgc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWxpbWluYXRpbmcgdGhlIFJlZmVyZW5jZSBNb2RlbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRFBPIGFuZCBJUE8gdXNlIHRoZSByZWZlcmVuY2UgbW9kZWwgcGlfcmVmIGFzIGEgYmFzZWxpbmU6IHRoZSBwb2xpY3kgaXMgcmV3YXJkZWQgZm9yIGluY3JlYXNpbmcgaXRzIHByb2JhYmlsaXR5IHJhdGlvIHJlbGF0aXZlIHRvIHdoYXQgcGlfcmVmIGFzc2lnbnMuIFRoaXMgS0wgYW5jaG9yaW5nIHByZXZlbnRzIHRoZSBwb2xpY3kgZnJvbSBkaXZlcmdpbmcgYXJiaXRyYXJpbHkuIE9SUE8gcmVwbGFjZXMgdGhpcyBleHRlcm5hbCBiYXNlbGluZSB3aXRoIHRoZSBTRlQgbG9zczogYnkgZGlyZWN0bHkgbWF4aW1pemluZyBsb2cgcGlfdGhldGEoeV93fHgpLCB0aGUgbW9kZWwgaXMgcHJldmVudGVkIGZyb20gY29sbGFwc2luZyB0byBkZWdlbmVyYXRlIGJlaGF2aW9yLiBUaGUgU0ZUIGNvbXBvbmVudCBrZWVwcyB0aGUgcG9saWN5IG5lYXIgYSBjb21wZXRlbnQgbGFuZ3VhZ2UgbW9kZWw7IHRoZSBvZGRzIHJhdGlvIGNvbXBvbmVudCBwdXNoZXMgaXQgdG8gcHJlZmVyIGNob3NlbiBvdmVyIHJlamVjdGVkIHNlcXVlbmNlcy4gVG9nZXRoZXIsIHRoZXkgcHJvdmlkZSB0aGUgc2FtZSBhbGlnbm1lbnQgc3RhYmlsaXR5IGFzIGEgcmVmZXJlbmNlIG1vZGVsIHdpdGhvdXQgcmVxdWlyaW5nIG9uZSB0byBiZSBzdG9yZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT1JQTyBMb3NzOiBDb21iaW5lZCBTRlQgYW5kIE9kZHMgUmF0aW8ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBPUlBPIHRvdGFsIGxvc3MgaXM6IExfT1JQTyA9IExfU0ZUICsgbGFtYmRhICogTF9PUiB3aGVyZSBMX1NGVCA9IC1sb2cgcGlfdGhldGEoeV93fHgpIChzdGFuZGFyZCBjYXVzYWwgbGFuZ3VhZ2UgbW9kZWwgbG9zcyBvbiBjaG9zZW4gc2VxdWVuY2VzKSBhbmQgTF9PUiA9IC1sb2cgc2lnbWEobG9nIFtvZGRzX3RoZXRhKHlfd3x4KSAvIG9kZHNfdGhldGEoeV9sfHgpXSkgd2hlcmUgb2Rkcyh5fHgpID0gUCh5fHgpLygxLVAoeXx4KSkuIFRoZSBsb2cgb2RkcyByYXRpbyBsb2dbb2Rkc193L29kZHNfbF0gPSBsb2dbUCh5X3d8eCkvKDEtUCh5X3d8eCkpXSAtIGxvZ1tQKHlfbHx4KS8oMS1QKHlfbHx4KSldLiBJbiBsb2cgc3BhY2U6IGxvZ19vZGRzKHl8eCkgPSBsb2cgUCh5fHgpIC0gbG9nKDEgLSBQKHl8eCkpID0gbG9ncCh5fHgpIC0gbG9nMXAoLWV4cChsb2dwKHl8eCkpKS4gVGhlIGh5cGVycGFyYW1ldGVyIGxhbWJkYSBiYWxhbmNlcyBTRlQgYW5kIGFsaWdubWVudDsgdHlwaWNhbCB2YWx1ZXMgYXJlIDAuMSB0byAxLjAuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgb2RkcyByYXRpbyBpcyBjaG9zZW4gb3ZlciB0aGUgcHJvYmFiaWxpdHkgcmF0aW8gZm9yIGEgdGhlb3JldGljYWwgcmVhc29uOiBmb3IgbG9uZyBzZXF1ZW5jZXMgd2hlcmUgUCh5fHgpIGlzIHZlcnkgc21hbGwgKHdoaWNoIGlzIHR5cGljYWwg4oCUIGEgMTAwLXRva2VuIHNlcXVlbmNlIHdpdGggcGVyLXRva2VuIGF2ZXJhZ2UgbG9nLXByb2IgLTEuMiBoYXMgdG90YWwgcHJvYmFiaWxpdHkgZXhwKC0xMjApIH4gMTBeey01Mn0pLCB0aGUgb2RkcyByYXRpbyBhbmQgcHJvYmFiaWxpdHkgcmF0aW8gYXJlIG51bWVyaWNhbGx5IGVxdWl2YWxlbnQuIFRoaXMgbWVhbnMgT1JQT1x1MDAyN3MgTF9PUiBpcyBhcHByb3hpbWF0ZWx5IGVxdWl2YWxlbnQgdG8gYSBsb2ctcHJvYmFiaWxpdHkgcmF0aW8gbG9zcyB3aGVuIGFwcGxpZWQgdG8gcmVhbGlzdGljIGxhbmd1YWdlIG1vZGVsIG91dHB1dHMsIHdoaWxlIGJlaW5nIG1vcmUgdGhlb3JldGljYWxseSBncm91bmRlZCBhbmQgbnVtZXJpY2FsbHkgc3RhYmxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9SUE8gTG9zcyBJbXBsZW1lbnRhdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIG9ycG9fbG9zcyhwb2xpY3lfY2hvc2VuX2xvZ3BzLCBwb2xpY3lfcmVqZWN0ZWRfbG9ncHMsIGxhbT0wLjEpOlxuICAgICMgT1JQTyAoSG9uZyBldCBhbC4sIDIwMjQpOiBMX1NGVCArIGxhbWJkYSAqIExfT1IsIG5vIHJlZmVyZW5jZSBtb2RlbCBuZWVkZWRcbiAgICBzZnRfbG9zcyA9IC1wb2xpY3lfY2hvc2VuX2xvZ3BzLm1lYW4oKVxuICAgICMgbG9nX29kZHMoeXx4KSA9IGxvZ3AgLSBsb2coMSAtIGV4cChsb2dwKSk7IGNsYW1wIGZvciBudW1lcmljYWwgc3RhYmlsaXR5XG4gICAgbG9nX29kZHNfYyA9IHBvbGljeV9jaG9zZW5fbG9ncHMgICAtIHRvcmNoLmxvZzFwKC1wb2xpY3lfY2hvc2VuX2xvZ3BzLmV4cCgpLmNsYW1wKG1heD0wLjk5OTkpKVxuICAgIGxvZ19vZGRzX3IgPSBwb2xpY3lfcmVqZWN0ZWRfbG9ncHMgLSB0b3JjaC5sb2cxcCgtcG9saWN5X3JlamVjdGVkX2xvZ3BzLmV4cCgpLmNsYW1wKG1heD0wLjk5OTkpKVxuICAgIGxvZ19vZGRzX3JhdGlvID0gbG9nX29kZHNfYyAtIGxvZ19vZGRzX3JcbiAgICBvcl9sb3NzID0gLUYubG9nc2lnbW9pZChsb2dfb2Rkc19yYXRpbykubWVhbigpXG4gICAgdG90YWwgPSBzZnRfbG9zcyArIGxhbSAqIG9yX2xvc3NcbiAgICByZXR1cm4gdG90YWwsIHNmdF9sb3NzLmRldGFjaCgpLCBvcl9sb3NzLmRldGFjaCgpXG5cbmJzeiA9IDhcbmNob3Nlbl9sb2dwcyAgID0gdG9yY2guZnVsbCgoYnN6LCksIC0xLjIpICsgdG9yY2gucmFuZG4oYnN6KSAqIDAuMVxucmVqZWN0ZWRfbG9ncHMgPSB0b3JjaC5mdWxsKChic3osKSwgLTEuOCkgKyB0b3JjaC5yYW5kbihic3opICogMC4xXG5sb3NzLCBzZnQsIG9yYXRpbyA9IG9ycG9fbG9zcyhjaG9zZW5fbG9ncHMsIHJlamVjdGVkX2xvZ3BzLCBsYW09MC4xKVxucHJpbnQoZlx1MDAyN09SUE8gdG90YWw6IHtsb3NzOi40Zn0gICBTRlQ6IHtzZnQ6LjRmfSAgIE9SOiB7b3JhdGlvOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3TW9kZWxzIGluIEdQVTogMSAoT1JQTykgdnMgMiAoRFBPKSB2cyA0IChQUE8pXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9kZHMgUmF0aW8gdnMgUHJvYmFiaWxpdHkgUmF0aW8gZm9yIExvbmcgU2VxdWVuY2VzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZXF1aXZhbGVuY2Ugb2Ygb2RkcyByYXRpbyBhbmQgcHJvYmFiaWxpdHkgcmF0aW8gaW4gdGhlIHNtYWxsLXByb2JhYmlsaXR5IHJlZ2ltZSBpcyBjcnVjaWFsIGZvciBPUlBPXHUwMDI3cyBwcmFjdGljYWwgdmFsaWRpdHkuIEZvciBhIHNlcXVlbmNlIG9mIGxlbmd0aCBMIHdpdGggcGVyLXRva2VuIGF2ZXJhZ2UgbG9nLXByb2IgbXUsIHRoZSBzZXF1ZW5jZSBwcm9iYWJpbGl0eSBpcyBleHAoTCptdSkuIEZvciBMPTEwMCBhbmQgbXU9LTEuMCwgUCh5fHgpID0gZXhwKC0xMDApIOKJiCAzLjfDlzEwXnstNDR9LiBJbiB0aGlzIHJlZ2ltZSwgb2Rkcyh5fHgpID0gUC8oMS1QKSDiiYggUCBzaW5jZSAxLVAg4omIIDEuIFRoZXJlZm9yZSB0aGUgb2RkcyByYXRpbyDiiYggcHJvYmFiaWxpdHkgcmF0aW8sIGFuZCBPUlBPXHUwMDI3cyBMX09SIOKJiCAtbG9nIHNpZ21hKGxvZyBwaV90aGV0YSh5X3d8eCkvcGlfdGhldGEoeV9sfHgpKSwgd2hpY2ggaXMgYSBjb250cmFzdGl2ZSBsb3NzIHdpdGhvdXQgYSByZWZlcmVuY2UgbW9kZWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgb2Rkc19mcm9tX2xvZ3AobG9ncCk6XG4gICAgIyBvZGRzID0gUCh5fHgpIC8gKDEgLSBQKHl8eCkpXG4gICAgcCA9IGxvZ3AuZXhwKClcbiAgICByZXR1cm4gcCAvICgxLjAgLSBwICsgMWUtMTUpXG5cbiMgRm9yIHJlYWxpc3RpYyBzZXF1ZW5jZSBwcm9iYWJpbGl0aWVzICh2ZXJ5IHNtYWxsKSwgb2RkcyDiiYggcHJvYmFiaWxpdHlcbmxvZ3BzICA9IHRvcmNoLmxpbnNwYWNlKC04LjAsIC0wLjUsIDEwKVxucHJvYnMgID0gbG9ncHMuZXhwKClcbm9kZHMgICA9IG9kZHNfZnJvbV9sb2dwKGxvZ3BzKVxucHJpbnQoZlx1MDAyNyAgbG9ncCAgICAgcHJvYiAgICAgICAgICAgb2RkcyAgICAgICAgICAgYWJzX2RpZmZcdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNTYpXG5mb3IgbHAsIHAsIG8gaW4gemlwKGxvZ3BzLCBwcm9icywgb2Rkcyk6XG4gICAgZGlmZiA9IGFicyhwLml0ZW0oKSAtIG8uaXRlbSgpKVxuICAgIHByaW50KGZcdTAwMjcgIHtscDouMmZ9ICB7cC5pdGVtKCk6LjhmfSAgIHtvLml0ZW0oKTouOGZ9ICAge2RpZmY6LjJlfVx1MDAyNylcbnByaW50KClcbnByaW50KFx1MDAyN0NvbmNsdXNpb246IGZvciBsb2dwIFx1MDAzYyAtMS4wICh0eXBpY2FsIHNlcXVlbmNlcyksIG9kZHMg4omIIHByb2IgdG8gXHUwMDNjMSUgZXJyb3JcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT1JQTyBTaW5nbGUtTW9kZWwgVHJhaW5pbmcgTG9vcCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT1JQT1x1MDAyN3MgdHJhaW5pbmcgbG9vcCBpcyBzaW1wbGVyIHRoYW4gRFBPXHUwMDI3cyBiZWNhdXNlIHRoZXJlIGlzIG5vIG5lZWQgdG8gcnVuIGEgc2Vjb25kIGZvcndhcmQgcGFzcyB0aHJvdWdoIGEgZnJvemVuIHJlZmVyZW5jZSBtb2RlbC4gQm90aCBjaG9zZW4gYW5kIHJlamVjdGVkIHNlcXVlbmNlcyBhcmUgcHJvY2Vzc2VkIHRocm91Z2ggdGhlIHNhbWUgcG9saWN5IG1vZGVsIGluIGEgc2luZ2xlIGZvcndhcmQgcGFzcyAob3IgdHdvIGZvcndhcmQgcGFzc2VzIHRocm91Z2ggdGhlIHNhbWUgbW9kZWwpLiBUaGUgZ3JhZGllbnQgYWNjdW11bGF0ZXMgZnJvbSBib3RoIHRoZSBTRlQgbG9zcyAob3ZlciBjaG9zZW4gdG9rZW5zKSBhbmQgdGhlIG9kZHMgcmF0aW8gbG9zcyAoY29tcGFyaW5nIGNob3NlbiB2cyByZWplY3RlZCkuIFRoaXMgaGFsdmVzIHBlYWsgR1BVIG1lbW9yeSBjb21wYXJlZCB0byBEUE8gYW5kIGVsaW1pbmF0ZXMgdGhlIG5lZWQgdG8gc3luY2hyb25pemUgdHdvIG1vZGVsIGNvcGllcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHRvcmNoLm9wdGltIGltcG9ydCBBZGFtV1xuXG5kZWYgY29tcHV0ZV9tZWFuX2xvZ3AobW9kZWwsIGlucHV0X2lkcywgYXR0ZW50aW9uX21hc2spOlxuICAgICMgRm9yd2FyZCBwYXNzIGFuZCBjb21wdXRlIG1lYW4gcGVyLXRva2VuIGxvZy1wcm9iYWJpbGl0eVxuICAgIG91dHB1dHMgPSBtb2RlbChpbnB1dF9pZHM9aW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzaz1hdHRlbnRpb25fbWFzaylcbiAgICBsb2dpdHMgID0gb3V0cHV0cy5sb2dpdHNbOiwgOi0xXS5jb250aWd1b3VzKClcbiAgICBsYWJlbHMgID0gaW5wdXRfaWRzWzosIDE6XS5jb250aWd1b3VzKClcbiAgICBscCAgICAgID0gRi5sb2dfc29mdG1heChsb2dpdHMsIGRpbT0tMSlcbiAgICB0b2tfbHAgID0gbHAuZ2F0aGVyKDIsIGxhYmVscy51bnNxdWVlemUoLTEpKS5zcXVlZXplKC0xKVxuICAgIG1hc2sgICAgPSBhdHRlbnRpb25fbWFza1s6LCAxOl0uZmxvYXQoKVxuICAgIHJldHVybiAodG9rX2xwICogbWFzaykuc3VtKGRpbT0xKSAvIChtYXNrLnN1bShkaW09MSkgKyAxZS05KVxuXG5kZWYgb3Jwb190cmFpbl9zdGVwKG1vZGVsLCBvcHRpbWl6ZXIsIGNob3Nlbl9pZHMsIHJlamVjdGVkX2lkcywgY19tYXNrLCByX21hc2ssIGxhbT0wLjEpOlxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgIGxvZ3BfYyA9IGNvbXB1dGVfbWVhbl9sb2dwKG1vZGVsLCBjaG9zZW5faWRzLCAgIGNfbWFzaylcbiAgICBsb2dwX3IgPSBjb21wdXRlX21lYW5fbG9ncChtb2RlbCwgcmVqZWN0ZWRfaWRzLCByX21hc2spXG4gICAgc2Z0X2xvc3MgICAgPSAtbG9ncF9jLm1lYW4oKVxuICAgIGxvZ19vZGRzX2MgID0gbG9ncF9jIC0gdG9yY2gubG9nMXAoLWxvZ3BfYy5leHAoKS5jbGFtcChtYXg9MC45OTk5KSlcbiAgICBsb2dfb2Rkc19yICA9IGxvZ3BfciAtIHRvcmNoLmxvZzFwKC1sb2dwX3IuZXhwKCkuY2xhbXAobWF4PTAuOTk5OSkpXG4gICAgb3JfbG9zcyAgICAgPSAtRi5sb2dzaWdtb2lkKGxvZ19vZGRzX2MgLSBsb2dfb2Rkc19yKS5tZWFuKClcbiAgICB0b3RhbF9sb3NzICA9IHNmdF9sb3NzICsgbGFtICogb3JfbG9zc1xuICAgIHRvdGFsX2xvc3MuYmFja3dhcmQoKVxuICAgIG9wdGltaXplci5zdGVwKClcbiAgICByZXR1cm4gdG90YWxfbG9zcy5pdGVtKCksIHNmdF9sb3NzLml0ZW0oKSwgb3JfbG9zcy5pdGVtKClcblxucHJpbnQoXHUwMDI3T1JQTyBzdGVwOiBvbmUgbW9kZWwsIHR3byBmb3J3YXJkIHBhc3Nlcywgbm8gZnJvemVuIHJlZmVyZW5jZSwgam9pbnQgU0ZUK2FsaWdubWVudFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcnkgRm9vdHByaW50IEFjcm9zcyBBbGlnbm1lbnQgTWV0aG9kcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIG1vZGVsX21lbW9yeV9nYihwYXJhbXNfQiwgYml0cz0xNik6XG4gICAgIyBXZWlnaHRzIG9ubHk7IG9wdGltaXplciBzdGF0ZXMgKEFkYW0gfjJ4KSBub3QgaW5jbHVkZWRcbiAgICByZXR1cm4gcGFyYW1zX0IgKiAxZTkgKiAoYml0cyAvIDgpIC8gMWU5XG5cbnNpemVzID0gWzcuMCwgMTMuMCwgMzQuMCwgNzAuMF1cbnByaW50KGZcdTAwMjcgIFNpemUoQikgICBQUE8oNCBtZGxzKSAgRFBPL0lQTygyKSAgT1JQTy9TaW1QTygxKSAgU2F2aW5nX3ZzX0RQT1x1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA3MClcbmZvciBzIGluIHNpemVzOlxuICAgIHBlciAgPSBtb2RlbF9tZW1vcnlfZ2IocywgMTYpICAgICAjIGJmbG9hdDE2XG4gICAgcHBvICA9IHBlciAqIDRcbiAgICBkcG8gID0gcGVyICogMlxuICAgIG9ycG8gPSBwZXIgKiAxXG4gICAgc2F2ZSA9IChkcG8gLSBvcnBvKSAvIGRwbyAqIDEwMFxuICAgIHByaW50KGZcdTAwMjcgIHtzOlx1MDAzZTcuMGZ9ICAge3BwbzpcdTAwM2U4LjFmfSBHQiAge2RwbzpcdTAwM2U3LjFmfSBHQiAgIHtvcnBvOlx1MDAzZTguMWZ9IEdCICB7c2F2ZTpcdTAwM2U4LjBmfSVcdTAwMjcpXG5wcmludCgpXG5wcmludChcdTAwMjdBZGFtIG9wdGltaXplciBzdGF0ZXMgYWRkIH4yeCBwZXIgdHJhaW5hYmxlIG1vZGVsIChub3Qgc2hvd24gYWJvdmUpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlZmVyZW5jZSBNb2RlbCBVc2FnZSBpbiBBbGlnbm1lbnQgTWV0aG9kcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJSZWZlcmVuY2UgTW9kZWwiLCJNb2RlbHMgaW4gR1BVIiwiU0ZUIFNlcGFyYXRlIiwiTWVtb3J5IDdCIGJmMTYiLCJOb3RlcyJdLCJyb3dzIjpbWyJQUE8iLCJZZXMgKGZyb3plbikiLCI0IChwb2xpY3ksIHJlZiwgcmV3YXJkLCB2YWx1ZSkiLCJZZXMiLCJ+NTYgR0IiLCJGdWxsIFJMIGxvb3AiXSxbIkRQTyIsIlllcyAoZnJvemVuKSIsIjIgKHBvbGljeSArIHJlZikiLCJZZXMiLCJ+MjggR0IiLCJPZmZsaW5lLCBwYWlyd2lzZSJdLFsiSVBPIiwiWWVzIChmcm96ZW4pIiwiMiAocG9saWN5ICsgcmVmKSIsIlllcyIsIn4yOCBHQiIsIlF1YWRyYXRpYyBsb3NzIl0sWyJPUlBPIiwiTm8iLCIxIChwb2xpY3kgb25seSkiLCJObyAoam9pbnQpIiwifjE0IEdCIiwiU0ZUICsgYWxpZ25tZW50Il0sWyJTaW1QTyIsIk5vIiwiMSAocG9saWN5IG9ubHkpIiwiWWVzIiwifjE0IEdCIiwiTGVuZ3RoIG5vcm1hbGl6ZWQiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJPUlBPIE1lbW9yeSBTYXZpbmdzIiwiY29udGVudCI6Ik9SUE9cdTAwMjdzIHNpbmdsZS1tb2RlbCBkZXNpZ24gbWFrZXMgaXQgaWRlYWwgZm9yIHJlc291cmNlLWNvbnN0cmFpbmVkIGZpbmUtdHVuaW5nIOKAlCB0aGUgZWxpbWluYXRlZCByZWZlcmVuY2UgbW9kZWwgc2F2ZXMgfjUwJSBHUFUgbWVtb3J5IGNvbXBhcmVkIHRvIERQTywgbWFraW5nIDdCIG1vZGVsIGFsaWdubWVudCBmZWFzaWJsZSBvbiBhIHNpbmdsZSA4MEdCIEExMDAuIENvbWJpbmVkIHdpdGggTG9SQSAod2hlcmUgb25seSBhZGFwdGVyIHdlaWdodHMgYXJlIHRyYWluZWQpLCBPUlBPIGNhbiBhbGlnbiBhIDdCIG1vZGVsIHVzaW5nIGxlc3MgdGhhbiAyMCBHQiBvZiBHUFUgbWVtb3J5IHdoaWxlIG1haW50YWluaW5nIGNvbXBldGl0aXZlIGFsaWdubWVudCBxdWFsaXR5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT1JQT1x1MDAyN3MgbGltaXRhdGlvbnMgc2hvdWxkIGJlIGNvbnNpZGVyZWQgd2hlbiBjaG9vc2luZyBpdCBvdmVyIERQTyBvciBJUE86ICgxKSB0aGUgU0ZUIGFuZCBwcmVmZXJlbmNlIHNpZ25hbHMgYXJlIGVudGFuZ2xlZCDigJQgaXQgaXMgaGFyZGVyIHRvIGRpYWdub3NlIHdoZXRoZXIgcG9vciBhbGlnbm1lbnQgY29tZXMgZnJvbSBpbnN1ZmZpY2llbnQgU0ZUIHF1YWxpdHkgb3IgYSBtaXNjYWxpYnJhdGVkIGxhbWJkYTsgKDIpIGFibGF0aW9uIHN0dWRpZXMgc2hvdyB0aGF0IHJlbW92aW5nIExfU0ZUICh1c2luZyBMX09SIGFsb25lKSBkcmFtYXRpY2FsbHkgaHVydHMgcGVyZm9ybWFuY2UsIGNvbmZpcm1pbmcgdGhhdCB0aGUgU0ZUIGxvc3MgaXMgZG9pbmcgcmVhbCB3b3JrIGFzIGEgcmVmZXJlbmNlIHByb3h5LCBub3QgbWVyZWx5IGEgcmVndWxhcml6ZXI7ICgzKSBPUlBPIGlzIGxlc3Mgd2VsbC1zdHVkaWVkIHRoYW4gRFBPIG9uIHZlcnkgbGFyZ2UgbW9kZWxzICg3MEIrKSB3aGVyZSB0aGUgU0ZULWFsaWdubWVudCBpbnRlcmFjdGlvbiBtYXkgZGlmZmVyLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiB0byB1c2UgT1JQTzogKDEpIHlvdSBoYXZlIGEgc2luZ2xlIEdQVSBvciBtZW1vcnktY29uc3RyYWluZWQgc2V0dXA7ICgyKSB5b3Ugd2FudCB0byBjb21iaW5lIGluc3RydWN0aW9uIHR1bmluZyBhbmQgcHJlZmVyZW5jZSBhbGlnbm1lbnQgaW4gb25lIHN0YWdlOyAoMykgeW91ciBwcmVmZXJlbmNlIGRhdGEgaXMgcmVsaWFibGUgYW5kIHRoZSBsYW1iZGEgaHlwZXJwYXJhbWV0ZXIgY2FuIGJlIHR1bmVkIG9uIGEgc21hbGwgaGVsZC1vdXQgc2V0LiBGb3IgaGlnaC1xdWFsaXR5IHByZWZlcmVuY2UgZGF0YSB3aGVyZSBtYXhpbWl6aW5nIGFsaWdubWVudCBpcyBjcml0aWNhbCwgRFBPIG9yIElQTyB3aXRoIGEgd2VsbC10cmFpbmVkIHJlZmVyZW5jZSBtb2RlbCBtYXkgb3V0cGVyZm9ybSBPUlBPIGRlc3BpdGUgdGhlIGFkZGVkIG1lbW9yeSBjb3N0LiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9SUE8gcmVwcmVzZW50cyBhIHByYWN0aWNhbCBlbmdpbmVlcmluZyBhZHZhbmNlIGluIExMTSBhbGlnbm1lbnQg4oCUIHRoZSBlbGltaW5hdGlvbiBvZiB0aGUgcmVmZXJlbmNlIG1vZGVsIGlzIG5vdCBtZXJlbHkgYSBtZW1vcnkgc2F2aW5nIGJ1dCBhIGNvbmNlcHR1YWwgc2ltcGxpZmljYXRpb24gdGhhdCBtYWtlcyBhbGlnbm1lbnQgbW9yZSBhY2Nlc3NpYmxlLiBCeSBjb21iaW5pbmcgU0ZUIGFuZCBwcmVmZXJlbmNlIGxlYXJuaW5nIGludG8gYSBzaW5nbGUgbG9zcywgT1JQTyByZWR1Y2VzIHRoZSBudW1iZXIgb2YgdHJhaW5pbmcgc3RhZ2VzIGZyb20gdHdvIHRvIG9uZSwgbG93ZXJzIEdQVSByZXF1aXJlbWVudHMgYnkgNTAlIGNvbXBhcmVkIHRvIERQTywgYW5kIHByb2R1Y2VzIGFsaWdubWVudCBxdWFsaXR5IGNvbXBldGl0aXZlIHdpdGggcmVmZXJlbmNlLW1vZGVsLWJhc2VkIG1ldGhvZHMgb24gc3RhbmRhcmQgYmVuY2htYXJrcy4gVW5kZXJzdGFuZGluZyBpdHMgb2RkcyByYXRpbyBmb3JtdWxhdGlvbiBhbmQgdGhlIGNvbmRpdGlvbnMgdW5kZXIgd2hpY2ggaXQgYXBwcm94aW1hdGVzIGEgcHJvYmFiaWxpdHkgcmF0aW8gaXMgZXNzZW50aWFsIGZvciBwcmFjdGl0aW9uZXJzIGFwcGx5aW5nIGl0IHRvIHJlYWwtd29ybGQgYWxpZ25tZW50IHRhc2tzLiJ9XQ=="
---
# ORPO — Odds Ratio Preference Optimization Without a Reference Model

ORPO (Odds Ratio Preference Optimization, Hong et al. 2024) takes a fundamentally different approach to LLM alignment: it removes the reference model entirely and combines supervised fine-tuning (SFT) with preference learning into a single training stage. Previous methods — PPO, DPO, IPO — all require a frozen reference policy pi_ref to anchor the optimization via a KL divergence constraint. This reference model doubles (or quadruples, in PPO's case) the GPU memory requirement. ORPO's insight is that the SFT loss itself provides the reference signal: by jointly maximizing chosen response likelihood and the odds ratio between chosen and rejected responses, the model learns both task competence and preference alignment simultaneously.

## Eliminating the Reference Model

DPO and IPO use the reference model pi_ref as a baseline: the policy is rewarded for increasing its probability ratio relative to what pi_ref assigns. This KL anchoring prevents the policy from diverging arbitrarily. ORPO replaces this external baseline with the SFT loss: by directly maximizing log pi_theta(y_w|x), the model is prevented from collapsing to degenerate behavior. The SFT component keeps the policy near a competent language model; the odds ratio component pushes it to prefer chosen over rejected sequences. Together, they provide the same alignment stability as a reference model without requiring one to be stored.

## ORPO Loss: Combined SFT and Odds Ratio

The ORPO total loss is: L_ORPO = L_SFT + lambda * L_OR where L_SFT = -log pi_theta(y_w|x) (standard causal language model loss on chosen sequences) and L_OR = -log sigma(log [odds_theta(y_w|x) / odds_theta(y_l|x)]) where odds(y|x) = P(y|x)/(1-P(y|x)). The log odds ratio log[odds_w/odds_l] = log[P(y_w|x)/(1-P(y_w|x))] - log[P(y_l|x)/(1-P(y_l|x))]. In log space: log_odds(y|x) = log P(y|x) - log(1 - P(y|x)) = logp(y|x) - log1p(-exp(logp(y|x))). The hyperparameter lambda balances SFT and alignment; typical values are 0.1 to 1.0.

The odds ratio is chosen over the probability ratio for a theoretical reason: for long sequences where P(y|x) is very small (which is typical — a 100-token sequence with per-token average log-prob -1.2 has total probability exp(-120) ~ 10^{-52}), the odds ratio and probability ratio are numerically equivalent. This means ORPO's L_OR is approximately equivalent to a log-probability ratio loss when applied to realistic language model outputs, while being more theoretically grounded and numerically stable.

## ORPO Loss Implementation

```python
import torch
import torch.nn.functional as F

def orpo_loss(policy_chosen_logps, policy_rejected_logps, lam=0.1):
    # ORPO (Hong et al., 2024): L_SFT + lambda * L_OR, no reference model needed
    sft_loss = -policy_chosen_logps.mean()
    # log_odds(y|x) = logp - log(1 - exp(logp)); clamp for numerical stability
    log_odds_c = policy_chosen_logps   - torch.log1p(-policy_chosen_logps.exp().clamp(max=0.9999))
    log_odds_r = policy_rejected_logps - torch.log1p(-policy_rejected_logps.exp().clamp(max=0.9999))
    log_odds_ratio = log_odds_c - log_odds_r
    or_loss = -F.logsigmoid(log_odds_ratio).mean()
    total = sft_loss + lam * or_loss
    return total, sft_loss.detach(), or_loss.detach()

bsz = 8
chosen_logps   = torch.full((bsz,), -1.2) + torch.randn(bsz) * 0.1
rejected_logps = torch.full((bsz,), -1.8) + torch.randn(bsz) * 0.1
loss, sft, oratio = orpo_loss(chosen_logps, rejected_logps, lam=0.1)
print(f'ORPO total: {loss:.4f}   SFT: {sft:.4f}   OR: {oratio:.4f}')
print(f'Models in GPU: 1 (ORPO) vs 2 (DPO) vs 4 (PPO)')
```

## Odds Ratio vs Probability Ratio for Long Sequences

The equivalence of odds ratio and probability ratio in the small-probability regime is crucial for ORPO's practical validity. For a sequence of length L with per-token average log-prob mu, the sequence probability is exp(L*mu). For L=100 and mu=-1.0, P(y|x) = exp(-100) ≈ 3.7×10^{-44}. In this regime, odds(y|x) = P/(1-P) ≈ P since 1-P ≈ 1. Therefore the odds ratio ≈ probability ratio, and ORPO's L_OR ≈ -log sigma(log pi_theta(y_w|x)/pi_theta(y_l|x)), which is a contrastive loss without a reference model.

```python
import torch

def odds_from_logp(logp):
    # odds = P(y|x) / (1 - P(y|x))
    p = logp.exp()
    return p / (1.0 - p + 1e-15)

# For realistic sequence probabilities (very small), odds ≈ probability
logps  = torch.linspace(-8.0, -0.5, 10)
probs  = logps.exp()
odds   = odds_from_logp(logps)
print(f'  logp     prob           odds           abs_diff')
print('-' * 56)
for lp, p, o in zip(logps, probs, odds):
    diff = abs(p.item() - o.item())
    print(f'  {lp:.2f}  {p.item():.8f}   {o.item():.8f}   {diff:.2e}')
print()
print('Conclusion: for logp < -1.0 (typical sequences), odds ≈ prob to <1% error')
```

## ORPO Single-Model Training Loop

ORPO's training loop is simpler than DPO's because there is no need to run a second forward pass through a frozen reference model. Both chosen and rejected sequences are processed through the same policy model in a single forward pass (or two forward passes through the same model). The gradient accumulates from both the SFT loss (over chosen tokens) and the odds ratio loss (comparing chosen vs rejected). This halves peak GPU memory compared to DPO and eliminates the need to synchronize two model copies.

```python
import torch
import torch.nn.functional as F
from torch.optim import AdamW

def compute_mean_logp(model, input_ids, attention_mask):
    # Forward pass and compute mean per-token log-probability
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    logits  = outputs.logits[:, :-1].contiguous()
    labels  = input_ids[:, 1:].contiguous()
    lp      = F.log_softmax(logits, dim=-1)
    tok_lp  = lp.gather(2, labels.unsqueeze(-1)).squeeze(-1)
    mask    = attention_mask[:, 1:].float()
    return (tok_lp * mask).sum(dim=1) / (mask.sum(dim=1) + 1e-9)

def orpo_train_step(model, optimizer, chosen_ids, rejected_ids, c_mask, r_mask, lam=0.1):
    optimizer.zero_grad()
    logp_c = compute_mean_logp(model, chosen_ids,   c_mask)
    logp_r = compute_mean_logp(model, rejected_ids, r_mask)
    sft_loss    = -logp_c.mean()
    log_odds_c  = logp_c - torch.log1p(-logp_c.exp().clamp(max=0.9999))
    log_odds_r  = logp_r - torch.log1p(-logp_r.exp().clamp(max=0.9999))
    or_loss     = -F.logsigmoid(log_odds_c - log_odds_r).mean()
    total_loss  = sft_loss + lam * or_loss
    total_loss.backward()
    optimizer.step()
    return total_loss.item(), sft_loss.item(), or_loss.item()

print('ORPO step: one model, two forward passes, no frozen reference, joint SFT+alignment')
```

## Memory Footprint Across Alignment Methods

```python
import torch

def model_memory_gb(params_B, bits=16):
    # Weights only; optimizer states (Adam ~2x) not included
    return params_B * 1e9 * (bits / 8) / 1e9

sizes = [7.0, 13.0, 34.0, 70.0]
print(f'  Size(B)   PPO(4 mdls)  DPO/IPO(2)  ORPO/SimPO(1)  Saving_vs_DPO')
print('-' * 70)
for s in sizes:
    per  = model_memory_gb(s, 16)     # bfloat16
    ppo  = per * 4
    dpo  = per * 2
    orpo = per * 1
    save = (dpo - orpo) / dpo * 100
    print(f'  {s:>7.0f}   {ppo:>8.1f} GB  {dpo:>7.1f} GB   {orpo:>8.1f} GB  {save:>8.0f}%')
print()
print('Adam optimizer states add ~2x per trainable model (not shown above)')
```

## Reference Model Usage in Alignment Methods

| Method | Reference Model | Models in GPU | SFT Separate | Memory 7B bf16 | Notes |
| --- | --- | --- | --- | --- | --- |
| PPO | Yes (frozen) | 4 (policy, ref, reward, value) | Yes | ~56 GB | Full RL loop |
| DPO | Yes (frozen) | 2 (policy + ref) | Yes | ~28 GB | Offline, pairwise |
| IPO | Yes (frozen) | 2 (policy + ref) | Yes | ~28 GB | Quadratic loss |
| ORPO | No | 1 (policy only) | No (joint) | ~14 GB | SFT + alignment |
| SimPO | No | 1 (policy only) | Yes | ~14 GB | Length normalized |

> **ORPO Memory Savings**: ORPO's single-model design makes it ideal for resource-constrained fine-tuning — the eliminated reference model saves ~50% GPU memory compared to DPO, making 7B model alignment feasible on a single 80GB A100. Combined with LoRA (where only adapter weights are trained), ORPO can align a 7B model using less than 20 GB of GPU memory while maintaining competitive alignment quality.

ORPO's limitations should be considered when choosing it over DPO or IPO: (1) the SFT and preference signals are entangled — it is harder to diagnose whether poor alignment comes from insufficient SFT quality or a miscalibrated lambda; (2) ablation studies show that removing L_SFT (using L_OR alone) dramatically hurts performance, confirming that the SFT loss is doing real work as a reference proxy, not merely a regularizer; (3) ORPO is less well-studied than DPO on very large models (70B+) where the SFT-alignment interaction may differ.

When to use ORPO: (1) you have a single GPU or memory-constrained setup; (2) you want to combine instruction tuning and preference alignment in one stage; (3) your preference data is reliable and the lambda hyperparameter can be tuned on a small held-out set. For high-quality preference data where maximizing alignment is critical, DPO or IPO with a well-trained reference model may outperform ORPO despite the added memory cost.

---

ORPO represents a practical engineering advance in LLM alignment — the elimination of the reference model is not merely a memory saving but a conceptual simplification that makes alignment more accessible. By combining SFT and preference learning into a single loss, ORPO reduces the number of training stages from two to one, lowers GPU requirements by 50% compared to DPO, and produces alignment quality competitive with reference-model-based methods on standard benchmarks. Understanding its odds ratio formulation and the conditions under which it approximates a probability ratio is essential for practitioners applying it to real-world alignment tasks.

