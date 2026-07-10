---
title: "IPO — Identity Preference Optimization and Overcoming DPO Pitfalls"
slug: "ipo-identity-preference"
description: "IPO (Azar et al., 2023) directly optimizes the Psi-preference framework without assuming a Bradley-Terry probability model, using a quadratic loss that prevents DPO's unbounded log-ratio problem and adds implicit L2 regularization on preference margins."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVpbmZvcmNlbWVudCBsZWFybmluZyBmcm9tIGh1bWFuIGZlZWRiYWNrIChSTEhGKSBoYXMgZXZvbHZlZCB0aHJvdWdoIGEgc2VyaWVzIG9mIGFsaWdubWVudCBhbGdvcml0aG1zIOKAlCBmcm9tIFBQT1x1MDAyN3Mgb25saW5lIFJMIHRvIERQT1x1MDAyN3Mgb2ZmbGluZSBjbG9zZWQtZm9ybSBzb2x1dGlvbi4gRWFjaCBzdGVwIGFpbWVkIHRvIHNpbXBsaWZ5IHRyYWluaW5nIHdoaWxlIHByZXNlcnZpbmcgYWxpZ25tZW50IHF1YWxpdHkuIElQTyAoSWRlbnRpdHkgUHJlZmVyZW5jZSBPcHRpbWl6YXRpb24sIEF6YXIgZXQgYWwuIDIwMjMpIGlzIGEgY3JpdGljYWwgcmVmaW5lbWVudCBvZiBEUE8gdGhhdCBmaXhlcyBhIGZ1bmRhbWVudGFsIHRoZW9yZXRpY2FsIGZsYXc6IERQT1x1MDAyN3MgcmVsaWFuY2Ugb24gdGhlIEJyYWRsZXktVGVycnkgcHJlZmVyZW5jZSBtb2RlbCwgd2hpY2ggY2FuIGxlYWQgdG8gdW5ib3VuZGVkIGxvZy1yYXRpbyBncm93dGggYW5kIHByZWZlcmVuY2Ugb3ZlcmZpdHRpbmcgd2hlbiB0cmFpbmluZyBkYXRhIGNvbnRhaW5zIG5vaXN5IG9yIG5lYXItdGllZCBwYWlycy4gSVBPIHJlcGxhY2VzIERQT1x1MDAyN3MgbG9naXN0aWMgbG9zcyB3aXRoIGEgcXVhZHJhdGljIG9iamVjdGl2ZSBkZXJpdmVkIGRpcmVjdGx5IGZyb20gdGhlIFBzaS1wcmVmZXJlbmNlIGZyYW1ld29yaywgcHJvdmlkaW5nIGEgcHJpbmNpcGxlZCByZWd1bGFyaXphdGlvbiB0aGF0IGtlZXBzIHBvbGljeSByYXRpb3MgaW4gYSBib3VuZGVkIHJhbmdlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRQT1x1MDAyN3MgQnJhZGxleS1UZXJyeSBBc3N1bXB0aW9uIGFuZCBJdHMgUGl0ZmFsbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRQTyBkZXJpdmVzIGl0cyBsb3NzIGJ5IGFzc3VtaW5nIGh1bWFuIHByZWZlcmVuY2VzIGZvbGxvdyB0aGUgQnJhZGxleS1UZXJyeSBtb2RlbDogUCh5X3cgXHUwMDNlIHlfbCB8IHgpID0gc2lnbWEocih4LHlfdykgLSByKHgseV9sKSkgd2hlcmUgciBpcyB0aGUgaW1wbGljaXQgcmV3YXJkLiBUaGlzIG1vZGVsIGltcGxpZXMgYSBzdHJpY3QgVGh1cnN0b25lLXR5cGUgcHJlZmVyZW5jZSBvcmRlcmluZyB0aGF0IG1heSBub3QgbWF0Y2ggdGhlIGFjdHVhbCBwcmVmZXJlbmNlIGRhdGEgZGlzdHJpYnV0aW9uLiBUaGUgZGVlcGVyIHByb2JsZW0gaXMgdGhhdCBEUE9cdTAwMjdzIGxvZ2lzdGljIGxvc3MgaGFzIGFuIGFzeW1wdG90ZSBhdCAwIOKAlCBpdCBrZWVwcyBwdXNoaW5nIHRoZSBsb2ctcHJvYiByYXRpbyBvZiBjaG9zZW4gb3ZlciByZWplY3RlZCByZXNwb25zZXMgdG93YXJkICtpbmZpbml0eS4gVGhlIGdyYWRpZW50IG9mIHRoZSBEUE8gbG9zcyBvbmx5IHZhbmlzaGVzIHdoZW4gbG9nKHBpX3RoZXRhKHlfd3x4KS9waV9yZWYoeV93fHgpKSAtIGxvZyhwaV90aGV0YSh5X2x8eCkvcGlfcmVmKHlfbHx4KSkg4oaSICtpbmZpbml0eSwgbWVhbmluZyB0aGUgb3B0aW1pemF0aW9uIGhhcyBubyBuYXR1cmFsIHN0b3BwaW5nIGNyaXRlcmlvbiBiZXlvbmQgdGhlIGZpbml0ZSBkYXRhLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gdGhlb3J5LCBEUE8gZHJpdmVzIHBpX3RoZXRhKHlfdykvcGlfcmVmKHlfdykg4oaSIGluZmluaXR5IHdoaWxlIHNpbXVsdGFuZW91c2x5IHB1c2hpbmcgcGlfdGhldGEoeV9sKS9waV9yZWYoeV9sKSDihpIgMC4gV2l0aCBub2lzeSBwcmVmZXJlbmNlIGxhYmVscyAod2hlcmUgc29tZSBcdTAwMjdyZWplY3RlZFx1MDAyNyByZXNwb25zZXMgYXJlIGFjdHVhbGx5IHJlYXNvbmFibGUpLCB0aGlzIGNhdXNlcyB0aGUgcG9saWN5IHRvIGNhdGFzdHJvcGhpY2FsbHkgc3VwcHJlc3MgdGhvc2UgcmVzcG9uc2VzLiBUaGUgdW5ib3VuZGVkIG5hdHVyZSBhbHNvIG1ha2VzIERQTyBzZW5zaXRpdmUgdG8gdGhlIGNob2ljZSBvZiBiZXRhOiB0b28gc21hbGwgYW5kIHRoZSBwb2xpY3kgZGl2ZXJnZXMgZnJvbSB0aGUgcmVmZXJlbmNlOyB0b28gbGFyZ2UgYW5kIHRoZSBwcmVmZXJlbmNlIHNpZ25hbCBpcyBvdmVyd2hlbG1lZCBieSB0aGUgS0wgcGVuYWx0eS4gSVBPIGFkZHJlc3NlcyBhbGwgb2YgdGhlc2UgZmFpbHVyZSBtb2Rlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJUE8gTG9zcyBGdW5jdGlvbiBhbmQgdGhlIFBzaS1QcmVmZXJlbmNlIEZyYW1ld29yayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSVBPIHdvcmtzIGRpcmVjdGx5IHdpdGggdGhlIGdlbmVyYWwgUHNpLXByZWZlcmVuY2UgZnJhbWV3b3JrIHdpdGhvdXQgc3BlY2lmeWluZyBhIHBhcnRpY3VsYXIgcHJvYmFiaWxpdHkgbW9kZWwgZm9yIHByZWZlcmVuY2VzLiBUaGUgSVBPIGxvc3MgaXM6IExfSVBPID0gRVsoW2xvZyBwaV90aGV0YSh5X3d8eCkvcGlfcmVmKHlfd3x4KSAtIGxvZyBwaV90aGV0YSh5X2x8eCkvcGlfcmVmKHlfbHx4KV0gLSAxLygyKnRhdSkpXjJdIHdoZXJlIHRhdSBpcyBhbiBpbnZlcnNlLXRlbXBlcmF0dXJlIGh5cGVycGFyYW1ldGVyLiBUaGUga2V5IGRpZmZlcmVuY2VzIGZyb20gRFBPOiAoMSkgcXVhZHJhdGljIHZzIGxvZ2lzdGljIGxvc3Mg4oCUIHRoZSBzcXVhcmVkIHRlcm0gcHJvdmlkZXMgYSBuYXR1cmFsIHN0b3BwaW5nIHBvaW50IGF0IGggPSAxLygyKnRhdSkgd2hlcmUgaCBpcyB0aGUgbG9nLXJhdGlvIGRpZmZlcmVuY2U7ICgyKSB0aGUgdGFyZ2V0IDEvKDIqdGF1KSBhY3RzIGFzIGFuIEwyIHJlZ3VsYXJpemF0aW9uIHRhcmdldCDigJQgbmVpdGhlciB0b28gbGFyZ2Ugbm9yIHRvbyBzbWFsbDsgKDMpIHRhdSBpbnRlcnBvbGF0ZXMgYmV0d2VlbiByZWdpbWVzOiBhcyB0YXUg4oaSIDAsIElQTyBjb252ZXJnZXMgdG8gRFBPOyBhcyB0YXUg4oaSIGluZmluaXR5LCBpdCBhcHByb2FjaGVzIFJFSU5GT1JDRS4gVHlwaWNhbCB2YWx1ZXM6IHRhdSA9IDAuMSBnaXZlcyBhIHRhcmdldCBoID0gNS4wLCBwcmV2ZW50aW5nIGV4dHJlbWUgbG9nLXJhdGlvcyB3aGlsZSBtYWludGFpbmluZyBzdHJvbmcgcHJlZmVyZW5jZSBzaWduYWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSVBPIExvc3MgSW1wbGVtZW50YXRpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBpcG9fbG9zcyhcbiAgICBwb2xpY3lfY2hvc2VuX2xvZ3BzLFxuICAgIHBvbGljeV9yZWplY3RlZF9sb2dwcyxcbiAgICByZWZfY2hvc2VuX2xvZ3BzLFxuICAgIHJlZl9yZWplY3RlZF9sb2dwcyxcbiAgICB0YXU9MC4xLFxuKTpcbiAgICAjIElQTyBsb3NzIChBemFyIGV0IGFsLiwgMjAyMykg4oCUIHF1YWRyYXRpYyByZWd1bGFyaXphdGlvbiBvZiBsb2ctcmF0aW9cbiAgICBjaG9zZW5fbG9ncmF0aW9zICAgPSBwb2xpY3lfY2hvc2VuX2xvZ3BzICAgLSByZWZfY2hvc2VuX2xvZ3BzXG4gICAgcmVqZWN0ZWRfbG9ncmF0aW9zID0gcG9saWN5X3JlamVjdGVkX2xvZ3BzIC0gcmVmX3JlamVjdGVkX2xvZ3BzXG4gICAgaCA9IGNob3Nlbl9sb2dyYXRpb3MgLSByZWplY3RlZF9sb2dyYXRpb3MgICMgcHJlZmVyZW5jZSBsb2ctcmF0aW8gZGlmZmVyZW5jZVxuICAgIGxvc3MgPSAoaCAtIDEuMCAvICgyLjAgKiB0YXUpKSAqKiAyICAgICAgICAjIHF1YWRyYXRpYyB2cyBsb2dpc3RpYyBpbiBEUE9cbiAgICByZXR1cm4gbG9zcy5tZWFuKCksIGNob3Nlbl9sb2dyYXRpb3MuZGV0YWNoKCksIHJlamVjdGVkX2xvZ3JhdGlvcy5kZXRhY2goKVxuXG5ic3ogPSA4XG5wb2xfYyA9IHRvcmNoLnJhbmRuKGJzeikgLSAxLjBcbnBvbF9yID0gdG9yY2gucmFuZG4oYnN6KSAtIDEuNVxucmVmX2MgPSB0b3JjaC5yYW5kbihic3opICogMC4zIC0gMS4wXG5yZWZfciA9IHRvcmNoLnJhbmRuKGJzeikgKiAwLjMgLSAxLjVcbmxvc3MsIGNyLCByciA9IGlwb19sb3NzKHBvbF9jLCBwb2xfciwgcmVmX2MsIHJlZl9yLCB0YXU9MC4xKVxucHJpbnQoZlx1MDAyN0lQTyBsb3NzOiB7bG9zczouNGZ9ICBjaG9zZW4gbG9nLXJhdGlvOiB7Y3IubWVhbigpOi4zZn0gIHJlamVjdGVkOiB7cnIubWVhbigpOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3SVBPIHRhcmdldCBoID0gMS8oMip0YXUpID0gezEvKDIqMC4xKTouMWZ9ICDigJQgcXVhZHJhdGljIG9wdGltdW1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRFBPIHZzIElQTzogTG9nLVJhdGlvIERpdmVyZ2VuY2UgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1vc3QgcmV2ZWFsaW5nIGRpZmZlcmVuY2UgYmV0d2VlbiBEUE8gYW5kIElQTyBpcyB3aGF0IGhhcHBlbnMgdG8gdGhlIGNob3NlbiBsb2ctcmF0aW8gZHVyaW5nIGdyYWRpZW50IGRlc2NlbnQgb24gdGhlIHNhbWUgZGF0YS4gRFBPXHUwMDI3cyBsb2dpc3RpYyBsb3NzIHByb2R1Y2VzIGEgZ3JhZGllbnQgdGhhdCBuZXZlciBmdWxseSBzYXR1cmF0ZXMg4oCUIGV2ZW4gd2hlbiB0aGUgbW9kZWwgc3Ryb25nbHkgcHJlZmVycyBjaG9zZW4gb3ZlciByZWplY3RlZCwgdGhlIGdyYWRpZW50IHB1c2hlcyB0aGUgcmF0aW8gaGlnaGVyLiBJUE9cdTAwMjdzIHF1YWRyYXRpYyBsb3NzIHByb2R1Y2VzIGEgZ3JhZGllbnQgdGhhdCBpcyB6ZXJvIGF0IGggPSAxLygyKnRhdSkgYW5kIHJldmVyc2VzIHNpZ24gaWYgaCBleGNlZWRzIHRoZSB0YXJnZXQsIGNyZWF0aW5nIGEgbmF0dXJhbCBhdHRyYWN0b3IgdGhhdCBwcmV2ZW50cyBydW5hd2F5IG9wdGltaXphdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBkcG9fbG9zcyhjaG9zZW5fbHIsIHJlamVjdGVkX2xyLCBiZXRhPTAuMSk6XG4gICAgcmV0dXJuIC1GLmxvZ3NpZ21vaWQoYmV0YSAqIChjaG9zZW5fbHIgLSByZWplY3RlZF9scikpLm1lYW4oKVxuXG5kZWYgaXBvX2xvc3NfZm4oY2hvc2VuX2xyLCByZWplY3RlZF9sciwgdGF1PTAuMSk6XG4gICAgaCA9IGNob3Nlbl9sciAtIHJlamVjdGVkX2xyXG4gICAgcmV0dXJuICgoaCAtIDEuMCAvICgyLjAgKiB0YXUpKSAqKiAyKS5tZWFuKClcblxuIyBTaW11bGF0ZSBncmFkaWVudCB1cGRhdGVzOiBEUE8gZGl2ZXJnZXMsIElQTyBjb252ZXJnZXMgdG8gdGFyZ2V0XG5jcl9kcG8gPSB0b3JjaC50ZW5zb3IoMC4wLCByZXF1aXJlc19ncmFkPVRydWUpXG5jcl9pcG8gPSB0b3JjaC50ZW5zb3IoMC4wLCByZXF1aXJlc19ncmFkPVRydWUpXG5yciA9IHRvcmNoLnRlbnNvcigtMC4yKSAgIyByZWplY3RlZCBzdGF5cyBuZWFyIHJlZmVyZW5jZVxuZm9yIHN0ZXAgaW4gcmFuZ2UoODApOlxuICAgIGxvc3NfZCA9IGRwb19sb3NzKGNyX2RwbywgcnIpXG4gICAgbG9zc19pID0gaXBvX2xvc3NfZm4oY3JfaXBvLCBycilcbiAgICBncmFkX2QgPSB0b3JjaC5hdXRvZ3JhZC5ncmFkKGxvc3NfZCwgY3JfZHBvKVswXVxuICAgIGdyYWRfaSA9IHRvcmNoLmF1dG9ncmFkLmdyYWQobG9zc19pLCBjcl9pcG8pWzBdXG4gICAgY3JfZHBvID0gKGNyX2RwbyAtIDAuMDUgKiBncmFkX2QpLmRldGFjaCgpLnJlcXVpcmVzX2dyYWRfKFRydWUpXG4gICAgY3JfaXBvID0gKGNyX2lwbyAtIDAuMDUgKiBncmFkX2kpLmRldGFjaCgpLnJlcXVpcmVzX2dyYWRfKFRydWUpXG5cbnByaW50KGZcdTAwMjdBZnRlciA4MCBncmFkaWVudCBzdGVwcyAobHI9MC4wNSk6XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgRFBPIGNob3NlbiBsb2ctcmF0aW86IHtjcl9kcG8uaXRlbSgpOi4zZn0gIChncm93cyB0b3dhcmQgK2luZilcdTAwMjcpXG5wcmludChmXHUwMDI3ICBJUE8gY2hvc2VuIGxvZy1yYXRpbzoge2NyX2lwby5pdGVtKCk6LjNmfSAgKHRhcmdldD0xLygyKnRhdSk9ezEvKDIqMC4xKTouMWZ9KVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW1wZXJhdHVyZSBQYXJhbWV0ZXIgdGF1OiBJbnRlcnBvbGF0aW5nIEJldHdlZW4gUkVJTkZPUkNFIGFuZCBEUE8ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0YXUgcGFyYW1ldGVyIGluIElQTyBpcyBub3QganVzdCBhIHNjYWxlIGZhY3RvciDigJQgaXQgZGV0ZXJtaW5lcyB0aGUgZWZmZWN0aXZlIG9wdGltaXphdGlvbiB0YXJnZXQuIEF0IHRhdT0wLjAxLCB0aGUgdGFyZ2V0IGg9NTAsIHdoaWNoIGlzIHNvIGxhcmdlIHRoYXQgYW55IHJlYXNvbmFibGUgdHJhaW5pbmcgcnVuIHdpbGwgYmVoYXZlIGxpa2UgRFBPICh0aGUgcXVhZHJhdGljIGxvc3MgaXMgbmVhcmx5IGxpbmVhciBpbiB0aGUgcmVsZXZhbnQgcmFuZ2UpLiBBdCB0YXU9MTAuMCwgdGhlIHRhcmdldCBoPTAuMDUsIG1lYW5pbmcgSVBPIHByZWZlcnMgb25seSBhIHRpbnkgbWFyZ2luIGJldHdlZW4gY2hvc2VuIGFuZCByZWplY3RlZCDigJQgc2ltaWxhciB0byBSRUlORk9SQ0Ugd2hpY2ggaGFzIG5vIGV4cGxpY2l0IHByZWZlcmVuY2UgbWFyZ2luLiBUaGUgcHJhY3RpY2FsIHN3ZWV0IHNwb3QgaXMgdGF1PTAuMDUgdG8gdGF1PTAuNSwgZ2l2aW5nIHRhcmdldHMgYmV0d2VlbiAxIGFuZCAxMCB0aGF0IHByZXZlbnQgZXh0cmVtZSBkaXZlcmdlbmNlIHdoaWxlIG1haW50YWluaW5nIG1lYW5pbmdmdWwgcHJlZmVyZW5jZSBzaWduYWwuIENyb3NzLXZhbGlkYXRpb24gb24gaGVsZC1vdXQgcHJlZmVyZW5jZXMgaXMgZXNzZW50aWFsIGZvciB0YXUgc2VsZWN0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGlwb19sb3NzX3RhdShwb2xfYywgcG9sX3IsIHJlZl9jLCByZWZfciwgdGF1KTpcbiAgICBjciA9IHBvbF9jIC0gcmVmX2NcbiAgICByciA9IHBvbF9yIC0gcmVmX3JcbiAgICBoICA9IGNyIC0gcnJcbiAgICByZXR1cm4gKChoIC0gMS4wIC8gKDIuMCAqIHRhdSkpICoqIDIpLm1lYW4oKVxuXG50YXVfdmFsdWVzID0gWzAuMDEsIDAuMDUsIDAuMSwgMC41LCAxLjAsIDUuMCwgMTAuMF1cbm4gPSA2NFxucG9sX2MgPSB0b3JjaC5yYW5kbihuKSAtIDAuOFxucG9sX3IgPSB0b3JjaC5yYW5kbihuKSAtIDEuM1xucmVmX2MgPSB0b3JjaC56ZXJvcyhuKVxucmVmX3IgPSB0b3JjaC56ZXJvcyhuKVxuXG5wcmludChmXHUwMDI3ICB0YXUgICAgIHRhcmdldF9oICAgICBsb3NzICAgICAgIHJlZ2ltZVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA1MClcbmZvciB0YXUgaW4gdGF1X3ZhbHVlczpcbiAgICBsb3NzICAgPSBpcG9fbG9zc190YXUocG9sX2MsIHBvbF9yLCByZWZfYywgcmVmX3IsIHRhdSlcbiAgICB0YXJnZXQgPSAxLjAgLyAoMi4wICogdGF1KVxuICAgIHJlZ2ltZSA9IFx1MDAyN0RQTy1saWtlXHUwMDI3IGlmIHRhdSBcdTAwM2MgMC4xIGVsc2UgKFx1MDAyN1JFSU5GT1JDRVx1MDAyNyBpZiB0YXUgXHUwMDNlIDIuMCBlbHNlIFx1MDAyN2JhbGFuY2VkXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIHt0YXU6XHUwMDNlNS4yZn0gICB7dGFyZ2V0Olx1MDAzZTguMmZ9ICAge2xvc3MuaXRlbSgpOlx1MDAzZTguNGZ9ICAge3JlZ2ltZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9uaXRvcmluZyBQcmVmZXJlbmNlIE92ZXJmaXR0aW5nIER1cmluZyBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBwcmFjdGljYWwgZGlhZ25vc3RpYyBmb3IgRFBPIHZzIElQTyB0cmFpbmluZyBpcyB0byBtb25pdG9yIHRoZSBhYnNvbHV0ZSBtYWduaXR1ZGUgb2YgbG9nLXJhdGlvcyB0aHJvdWdob3V0IHRyYWluaW5nLiBXaXRoIERQTywgfGxvZyBwaV90aGV0YSh5X3d8eCkvcGlfcmVmKHlfd3x4KXwgc2hvdWxkIHBsYXRlYXUg4oCUIGlmIGl0IGtlZXBzIGdyb3dpbmcgcGFzdCAzLTUsIHRoZSBtb2RlbCBpcyBvdmVyZml0dGluZyB0byBwcmVmZXJlbmNlIG5vaXNlLiBXaXRoIElQTywgdGhlIGxvZy1yYXRpbyBzaG91bGQgY29udmVyZ2UgbmVhciAxLygyKnRhdSkgZm9yIGNob3NlbiBhbmQgbmVhciAwIGZvciByZWplY3RlZC4gRGl2ZXJnZW5jZSBmcm9tIHRoZXNlIHRhcmdldHMgc2lnbmFscyBtaXNjYWxpYnJhdGlvbiAod3JvbmcgdGF1LCBpbmNvcnJlY3Qgbm9ybWFsaXphdGlvbiwgb3IgZGF0YSBxdWFsaXR5IGlzc3VlcykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVmYXVsdGRpY3RcblxuZGVmIHRyYWNrX2xvZ19yYXRpb3Moc3RlcCwgY2hvc2VuX2xyLCByZWplY3RlZF9sciwgbWV0cmljcywgdGhyZXNob2xkPTMuMCk6XG4gICAgY3JfYWJzID0gY2hvc2VuX2xyLmFicygpLm1lYW4oKS5pdGVtKClcbiAgICBycl9hYnMgPSByZWplY3RlZF9sci5hYnMoKS5tZWFuKCkuaXRlbSgpXG4gICAgbWV0cmljc1tcdTAwMjdjaG9zZW5fYWJzXHUwMDI3XS5hcHBlbmQoY3JfYWJzKVxuICAgIG1ldHJpY3NbXHUwMDI3cmVqZWN0ZWRfYWJzXHUwMDI3XS5hcHBlbmQocnJfYWJzKVxuICAgIGlmIGNyX2FicyBcdTAwM2UgdGhyZXNob2xkIG9yIHJyX2FicyBcdTAwM2UgdGhyZXNob2xkOlxuICAgICAgICBwcmludChmXHUwMDI3ICBTdGVwIHtzdGVwfTogT1ZFUkZJVCB8Y2hvc2VufD17Y3JfYWJzOi4yZn0gfHJlamVjdGVkfD17cnJfYWJzOi4yZn1cdTAwMjcpXG4gICAgcmV0dXJuIGNyX2FicywgcnJfYWJzXG5cbm1ldHJpY3NfZHBvID0gZGVmYXVsdGRpY3QobGlzdClcbm1ldHJpY3NfaXBvID0gZGVmYXVsdGRpY3QobGlzdClcbmZvciBzdGVwIGluIHJhbmdlKDEsIDIxKTpcbiAgICBjcl9kcG8gPSB0b3JjaC5yYW5kbigxNikgKiAoc3RlcCAqIDAuMykgICAgIyBEUE8gcmF0aW9zIGdyb3cgd2l0aG91dCBib3VuZFxuICAgIHJyX2RwbyA9IHRvcmNoLnJhbmRuKDE2KSAqIChzdGVwICogMC4yKVxuICAgIHRyYWNrX2xvZ19yYXRpb3Moc3RlcCwgY3JfZHBvLCBycl9kcG8sIG1ldHJpY3NfZHBvLCB0aHJlc2hvbGQ9My4wKVxuICAgIGNyX2lwbyA9IHRvcmNoLnJhbmRuKDE2KSAqIDAuNSArIDUuMCAgICAgICAjIElQTyBzdGFiaWxpemVzIG5lYXIgMS8oMip0YXUpPTVcbiAgICBycl9pcG8gPSB0b3JjaC5yYW5kbigxNikgKiAwLjMgKyAwLjFcbiAgICB0cmFja19sb2dfcmF0aW9zKHN0ZXAsIGNyX2lwbywgcnJfaXBvLCBtZXRyaWNzX2lwbywgdGhyZXNob2xkPTEwLjApXG5kcG9fZmluYWwgPSBtZXRyaWNzX2Rwb1tcdTAwMjdjaG9zZW5fYWJzXHUwMDI3XVstMV1cbmlwb19maW5hbCA9IG1ldHJpY3NfaXBvW1x1MDAyN2Nob3Nlbl9hYnNcdTAwMjddWy0xXVxucHJpbnQoZlx1MDAyN0RQTyBmaW5hbCB8Y2hvc2VufCBsb2ctcmF0aW86IHtkcG9fZmluYWw6LjJmfVx1MDAyNylcbnByaW50KGZcdTAwMjdJUE8gZmluYWwgfGNob3NlbnwgbG9nLXJhdGlvOiB7aXBvX2ZpbmFsOi4yZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWxpZ25tZW50IE1ldGhvZCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkxvc3MgRnVuY3Rpb24iLCJSZWZlcmVuY2UgTW9kZWwiLCJSZWd1bGFyaXphdGlvbiIsIlByZWYuIEFzc3VtcHRpb24iLCJTdGFiaWxpdHkiXSwicm93cyI6W1siRFBPIiwiLWxvZyBzaWdtYShiZXRhKmgpIiwiWWVzIChmcm96ZW4pIiwiSW1wbGljaXQgS0wgdmlhIGJldGEiLCJCcmFkbGV5LVRlcnJ5IiwiQ2FuIG92ZXJmaXQiXSxbIklQTyIsIihoIC0gMS8ydGF1KV4yIiwiWWVzIChmcm96ZW4pIiwiUXVhZHJhdGljIEwyIHRhcmdldCIsIlBzaS1wcmVmZXJlbmNlIChtb2RlbC1mcmVlKSIsIlN0YWJsZSJdLFsiT1JQTyIsIkxfU0ZUICsgbGFtYmRhKkxfT1IiLCJObyIsIlNGVCBvYmplY3RpdmUgam9pbnQiLCJPZGRzIHJhdGlvIiwiU3RhYmxlIl0sWyJTaW1QTyIsIi1sb2cgc2lnbWEoYmV0YSpEZWx0YV9yIC0gZ2FtbWEpIiwiTm8iLCJMZW5ndGggbm9ybSArIG1hcmdpbiIsIk5vbmUgKGF2ZyBsb2ctcHJvYikiLCJTdGFibGUiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSVBPXHUwMDI3cyBRdWFkcmF0aWMgUmVndWxhcml6YXRpb24iLCJjb250ZW50IjoiSVBPXHUwMDI3cyBxdWFkcmF0aWMgbG9zcyBwcmV2ZW50cyB0aGUgdW5ib3VuZGVkIGxvZy1yYXRpbyBwcm9ibGVtIGluIERQTyDigJQgd2hlcmUgRFBPIGNhbiBkcml2ZSBwaV90aGV0YSh5X3cpL3BpX3JlZih5X3cpIHRvd2FyZCBpbmZpbml0eSwgSVBPXHUwMDI3cyBzcXVhcmVkIHRlcm0gcHJvdmlkZXMgYW4gaW1wbGljaXQgTDIgcmVndWxhcml6YXRpb24gdGhhdCBrZWVwcyByYXRpb3MgaW4gYSByZWFzb25hYmxlIHJhbmdlLiBUaGUgZXF1aWxpYnJpdW0gcG9pbnQgaCA9IDEvKDIqdGF1KSBpcyBhIGdlbnVpbmUgYXR0cmFjdG9yOiBncmFkaWVudHMgcG9pbnQgYXdheSBmcm9tIGl0IGluIGJvdGggZGlyZWN0aW9ucywgZW5zdXJpbmcgc3RhYmxlIGNvbnZlcmdlbmNlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJhY3RpY2FsbHksIElQTyB0cmFpbnMgbW9yZSBjb25zZXJ2YXRpdmVseSB0aGFuIERQTzogaXQgcHJvZHVjZXMgcG9saWNpZXMgd2l0aCBzbWFsbGVyIGxvZy1yYXRpbyBtYWduaXR1ZGVzIGFuZCBtb3JlIG1vZGVyYXRlIGJlaGF2aW9yIG9uIG91dC1vZi1kaXN0cmlidXRpb24gcHJvbXB0cy4gVGhpcyBjb25zZXJ2YXRpc20gaXMgYSBmZWF0dXJlIHdoZW4gcHJlZmVyZW5jZSBsYWJlbHMgYXJlIG5vaXN5IChlLmcuLCBjcm93ZHNvdXJjZWQgYW5ub3RhdGlvbnMgd2l0aCBsb3cgaW50ZXItYW5ub3RhdG9yIGFncmVlbWVudCkgYnV0IGNhbiBiZSBhIGxpbWl0YXRpb24gd2hlbiB0aGUgcHJlZmVyZW5jZSBkYXRhIGlzIGhpZ2ggcXVhbGl0eSBhbmQgeW91IHdhbnQgc3Ryb25nIGFsaWdubWVudCBzaWduYWwuIEluIHRoYXQgY2FzZSwgRFBPIHdpdGggY2FyZWZ1bCBiZXRhIHR1bmluZyBtYXkgb3V0cGVyZm9ybSBJUE8uIFRoZSBjaG9pY2UgYmV0d2VlbiB0aGVtIHNob3VsZCBiZSBndWlkZWQgYnkgaGVsZC1vdXQgcHJlZmVyZW5jZSBhY2N1cmFjeSBhbmQgbG9nLXJhdGlvIG1vbml0b3JpbmcgZHVyaW5nIHRyYWluaW5nLiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IklQTyByZXByZXNlbnRzIGEgcHJpbmNpcGxlZCBmaXggdG8gRFBPXHUwMDI3cyB0aGVvcmV0aWNhbCB3ZWFrbmVzc2VzIHdpdGhvdXQgYWRkaW5nIHNpZ25pZmljYW50IGltcGxlbWVudGF0aW9uIGNvbXBsZXhpdHkg4oCUIHRoZSBsb3NzIGZ1bmN0aW9uIGlzIGEgb25lLWxpbmUgY2hhbmdlLiBUaGUgcXVhZHJhdGljIG9iamVjdGl2ZSwgdGhlIHRhdSB0ZW1wZXJhdHVyZSBwYXJhbWV0ZXIsIGFuZCB0aGUgYm91bmRlZCBsb2ctcmF0aW8gYmVoYXZpb3IgbWFrZSBJUE8gdGhlIHByZWZlcnJlZCBjaG9pY2UgZm9yIGFsaWdubWVudCBzY2VuYXJpb3Mgd2l0aCBub2lzeSBwcmVmZXJlbmNlcywgc21hbGwgZGF0YXNldHMsIG9yIHNpdHVhdGlvbnMgd2hlcmUgcG9saWN5IHN0YWJpbGl0eSBpcyBjcml0aWNhbC4gVW5kZXJzdGFuZGluZyB0aGUgRFBPLUlQTy1PUlBPLVNpbVBPIHByb2dyZXNzaW9uIGlzIGVzc2VudGlhbCBmb3IgY2hvb3NpbmcgdGhlIHJpZ2h0IGFsaWdubWVudCBhbGdvcml0aG0gZm9yIGEgZ2l2ZW4gcmVzb3VyY2UgYW5kIGRhdGEgcXVhbGl0eSBjb25zdHJhaW50LiJ9XQ=="
---
# IPO — Identity Preference Optimization and Overcoming DPO Pitfalls

Reinforcement learning from human feedback (RLHF) has evolved through a series of alignment algorithms — from PPO's online RL to DPO's offline closed-form solution. Each step aimed to simplify training while preserving alignment quality. IPO (Identity Preference Optimization, Azar et al. 2023) is a critical refinement of DPO that fixes a fundamental theoretical flaw: DPO's reliance on the Bradley-Terry preference model, which can lead to unbounded log-ratio growth and preference overfitting when training data contains noisy or near-tied pairs. IPO replaces DPO's logistic loss with a quadratic objective derived directly from the Psi-preference framework, providing a principled regularization that keeps policy ratios in a bounded range.

## DPO's Bradley-Terry Assumption and Its Pitfalls

DPO derives its loss by assuming human preferences follow the Bradley-Terry model: P(y_w > y_l | x) = sigma(r(x,y_w) - r(x,y_l)) where r is the implicit reward. This model implies a strict Thurstone-type preference ordering that may not match the actual preference data distribution. The deeper problem is that DPO's logistic loss has an asymptote at 0 — it keeps pushing the log-prob ratio of chosen over rejected responses toward +infinity. The gradient of the DPO loss only vanishes when log(pi_theta(y_w|x)/pi_ref(y_w|x)) - log(pi_theta(y_l|x)/pi_ref(y_l|x)) → +infinity, meaning the optimization has no natural stopping criterion beyond the finite data.

In theory, DPO drives pi_theta(y_w)/pi_ref(y_w) → infinity while simultaneously pushing pi_theta(y_l)/pi_ref(y_l) → 0. With noisy preference labels (where some 'rejected' responses are actually reasonable), this causes the policy to catastrophically suppress those responses. The unbounded nature also makes DPO sensitive to the choice of beta: too small and the policy diverges from the reference; too large and the preference signal is overwhelmed by the KL penalty. IPO addresses all of these failure modes.

## IPO Loss Function and the Psi-Preference Framework

IPO works directly with the general Psi-preference framework without specifying a particular probability model for preferences. The IPO loss is: L_IPO = E[([log pi_theta(y_w|x)/pi_ref(y_w|x) - log pi_theta(y_l|x)/pi_ref(y_l|x)] - 1/(2*tau))^2] where tau is an inverse-temperature hyperparameter. The key differences from DPO: (1) quadratic vs logistic loss — the squared term provides a natural stopping point at h = 1/(2*tau) where h is the log-ratio difference; (2) the target 1/(2*tau) acts as an L2 regularization target — neither too large nor too small; (3) tau interpolates between regimes: as tau → 0, IPO converges to DPO; as tau → infinity, it approaches REINFORCE. Typical values: tau = 0.1 gives a target h = 5.0, preventing extreme log-ratios while maintaining strong preference signal.

## IPO Loss Implementation

```python
import torch
import torch.nn.functional as F

def ipo_loss(
    policy_chosen_logps,
    policy_rejected_logps,
    ref_chosen_logps,
    ref_rejected_logps,
    tau=0.1,
):
    # IPO loss (Azar et al., 2023) — quadratic regularization of log-ratio
    chosen_logratios   = policy_chosen_logps   - ref_chosen_logps
    rejected_logratios = policy_rejected_logps - ref_rejected_logps
    h = chosen_logratios - rejected_logratios  # preference log-ratio difference
    loss = (h - 1.0 / (2.0 * tau)) ** 2        # quadratic vs logistic in DPO
    return loss.mean(), chosen_logratios.detach(), rejected_logratios.detach()

bsz = 8
pol_c = torch.randn(bsz) - 1.0
pol_r = torch.randn(bsz) - 1.5
ref_c = torch.randn(bsz) * 0.3 - 1.0
ref_r = torch.randn(bsz) * 0.3 - 1.5
loss, cr, rr = ipo_loss(pol_c, pol_r, ref_c, ref_r, tau=0.1)
print(f'IPO loss: {loss:.4f}  chosen log-ratio: {cr.mean():.3f}  rejected: {rr.mean():.3f}')
print(f'IPO target h = 1/(2*tau) = {1/(2*0.1):.1f}  — quadratic optimum')
```

## DPO vs IPO: Log-Ratio Divergence Comparison

The most revealing difference between DPO and IPO is what happens to the chosen log-ratio during gradient descent on the same data. DPO's logistic loss produces a gradient that never fully saturates — even when the model strongly prefers chosen over rejected, the gradient pushes the ratio higher. IPO's quadratic loss produces a gradient that is zero at h = 1/(2*tau) and reverses sign if h exceeds the target, creating a natural attractor that prevents runaway optimization.

```python
import torch
import torch.nn.functional as F

def dpo_loss(chosen_lr, rejected_lr, beta=0.1):
    return -F.logsigmoid(beta * (chosen_lr - rejected_lr)).mean()

def ipo_loss_fn(chosen_lr, rejected_lr, tau=0.1):
    h = chosen_lr - rejected_lr
    return ((h - 1.0 / (2.0 * tau)) ** 2).mean()

# Simulate gradient updates: DPO diverges, IPO converges to target
cr_dpo = torch.tensor(0.0, requires_grad=True)
cr_ipo = torch.tensor(0.0, requires_grad=True)
rr = torch.tensor(-0.2)  # rejected stays near reference
for step in range(80):
    loss_d = dpo_loss(cr_dpo, rr)
    loss_i = ipo_loss_fn(cr_ipo, rr)
    grad_d = torch.autograd.grad(loss_d, cr_dpo)[0]
    grad_i = torch.autograd.grad(loss_i, cr_ipo)[0]
    cr_dpo = (cr_dpo - 0.05 * grad_d).detach().requires_grad_(True)
    cr_ipo = (cr_ipo - 0.05 * grad_i).detach().requires_grad_(True)

print(f'After 80 gradient steps (lr=0.05):')
print(f'  DPO chosen log-ratio: {cr_dpo.item():.3f}  (grows toward +inf)')
print(f'  IPO chosen log-ratio: {cr_ipo.item():.3f}  (target=1/(2*tau)={1/(2*0.1):.1f})')
```

## Temperature Parameter tau: Interpolating Between REINFORCE and DPO

The tau parameter in IPO is not just a scale factor — it determines the effective optimization target. At tau=0.01, the target h=50, which is so large that any reasonable training run will behave like DPO (the quadratic loss is nearly linear in the relevant range). At tau=10.0, the target h=0.05, meaning IPO prefers only a tiny margin between chosen and rejected — similar to REINFORCE which has no explicit preference margin. The practical sweet spot is tau=0.05 to tau=0.5, giving targets between 1 and 10 that prevent extreme divergence while maintaining meaningful preference signal. Cross-validation on held-out preferences is essential for tau selection.

```python
import torch

def ipo_loss_tau(pol_c, pol_r, ref_c, ref_r, tau):
    cr = pol_c - ref_c
    rr = pol_r - ref_r
    h  = cr - rr
    return ((h - 1.0 / (2.0 * tau)) ** 2).mean()

tau_values = [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
n = 64
pol_c = torch.randn(n) - 0.8
pol_r = torch.randn(n) - 1.3
ref_c = torch.zeros(n)
ref_r = torch.zeros(n)

print(f'  tau     target_h     loss       regime')
print('-' * 50)
for tau in tau_values:
    loss   = ipo_loss_tau(pol_c, pol_r, ref_c, ref_r, tau)
    target = 1.0 / (2.0 * tau)
    regime = 'DPO-like' if tau < 0.1 else ('REINFORCE' if tau > 2.0 else 'balanced')
    print(f'  {tau:>5.2f}   {target:>8.2f}   {loss.item():>8.4f}   {regime}')
```

## Monitoring Preference Overfitting During Training

A practical diagnostic for DPO vs IPO training is to monitor the absolute magnitude of log-ratios throughout training. With DPO, |log pi_theta(y_w|x)/pi_ref(y_w|x)| should plateau — if it keeps growing past 3-5, the model is overfitting to preference noise. With IPO, the log-ratio should converge near 1/(2*tau) for chosen and near 0 for rejected. Divergence from these targets signals miscalibration (wrong tau, incorrect normalization, or data quality issues).

```python
import torch
from collections import defaultdict

def track_log_ratios(step, chosen_lr, rejected_lr, metrics, threshold=3.0):
    cr_abs = chosen_lr.abs().mean().item()
    rr_abs = rejected_lr.abs().mean().item()
    metrics['chosen_abs'].append(cr_abs)
    metrics['rejected_abs'].append(rr_abs)
    if cr_abs > threshold or rr_abs > threshold:
        print(f'  Step {step}: OVERFIT |chosen|={cr_abs:.2f} |rejected|={rr_abs:.2f}')
    return cr_abs, rr_abs

metrics_dpo = defaultdict(list)
metrics_ipo = defaultdict(list)
for step in range(1, 21):
    cr_dpo = torch.randn(16) * (step * 0.3)    # DPO ratios grow without bound
    rr_dpo = torch.randn(16) * (step * 0.2)
    track_log_ratios(step, cr_dpo, rr_dpo, metrics_dpo, threshold=3.0)
    cr_ipo = torch.randn(16) * 0.5 + 5.0       # IPO stabilizes near 1/(2*tau)=5
    rr_ipo = torch.randn(16) * 0.3 + 0.1
    track_log_ratios(step, cr_ipo, rr_ipo, metrics_ipo, threshold=10.0)
dpo_final = metrics_dpo['chosen_abs'][-1]
ipo_final = metrics_ipo['chosen_abs'][-1]
print(f'DPO final |chosen| log-ratio: {dpo_final:.2f}')
print(f'IPO final |chosen| log-ratio: {ipo_final:.2f}')
```

## Alignment Method Comparison

| Method | Loss Function | Reference Model | Regularization | Pref. Assumption | Stability |
| --- | --- | --- | --- | --- | --- |
| DPO | -log sigma(beta*h) | Yes (frozen) | Implicit KL via beta | Bradley-Terry | Can overfit |
| IPO | (h - 1/2tau)^2 | Yes (frozen) | Quadratic L2 target | Psi-preference (model-free) | Stable |
| ORPO | L_SFT + lambda*L_OR | No | SFT objective joint | Odds ratio | Stable |
| SimPO | -log sigma(beta*Delta_r - gamma) | No | Length norm + margin | None (avg log-prob) | Stable |

> **IPO's Quadratic Regularization**: IPO's quadratic loss prevents the unbounded log-ratio problem in DPO — where DPO can drive pi_theta(y_w)/pi_ref(y_w) toward infinity, IPO's squared term provides an implicit L2 regularization that keeps ratios in a reasonable range. The equilibrium point h = 1/(2*tau) is a genuine attractor: gradients point away from it in both directions, ensuring stable convergence.

Practically, IPO trains more conservatively than DPO: it produces policies with smaller log-ratio magnitudes and more moderate behavior on out-of-distribution prompts. This conservatism is a feature when preference labels are noisy (e.g., crowdsourced annotations with low inter-annotator agreement) but can be a limitation when the preference data is high quality and you want strong alignment signal. In that case, DPO with careful beta tuning may outperform IPO. The choice between them should be guided by held-out preference accuracy and log-ratio monitoring during training.

---

IPO represents a principled fix to DPO's theoretical weaknesses without adding significant implementation complexity — the loss function is a one-line change. The quadratic objective, the tau temperature parameter, and the bounded log-ratio behavior make IPO the preferred choice for alignment scenarios with noisy preferences, small datasets, or situations where policy stability is critical. Understanding the DPO-IPO-ORPO-SimPO progression is essential for choosing the right alignment algorithm for a given resource and data quality constraint.

