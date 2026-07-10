---
title: "Prompt Versioning and Management"
slug: "prompt-versioning"
description: "Treating prompts as code artifacts with version control, A/B testing, rollback, and evaluation pipelines — prompt registries, eval-driven iteration, and CI/CD for prompts."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJvbXB0cyBhcmUgaHlwZXJwYXJhbWV0ZXJzIOKAlCBhIDUtd29yZCBjaGFuZ2UgY2FuIHNoaWZ0IGFjY3VyYWN5IGJ5IDEwJSBvciBicmVhayBhIHByb2R1Y3Rpb24gd29ya2Zsb3cgZW50aXJlbHkuIFlldCBtb3N0IHRlYW1zIHRyZWF0IHByb21wdCBmaWxlcyBhcyBhZCBob2MgdGV4dCwgb3ZlcndyaXRpbmcgd29ya2luZyB2ZXJzaW9ucyB3aXRob3V0IGhpc3RvcnksIGxvc2luZyBjb250ZXh0LCBhbmQgdW5hYmxlIHRvIHJvbGwgYmFjayB3aGVuIHJlZ3Jlc3Npb25zIGFwcGVhci4gRGlzY2lwbGluZWQgcHJvbXB0IHZlcnNpb25pbmcgY2xvc2VzIHRoZSBnYXAgYmV0d2VlbiBwcm9tcHQgZW5naW5lZXJpbmcgYW5kIHNvZnR3YXJlIGVuZ2luZWVyaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJjb250ZW50IjoiV2h5IFByb21wdHMgTmVlZCBWZXJzaW9uIENvbnRyb2wifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByb21wdHMgZHJpZnQgc2lsZW50bHkg4oCUIG1vZGVsIHVwZGF0ZXMsIEEvQiB0ZXN0IHJlc3VsdHMsIGFuZCB0ZWFtIGVkaXRzIGNvbXBvdW5kIHdpdGhvdXQgYSBoaXN0b3J5IHRyYWlsLiBBIGNoYW5nZSB0aGF0IGltcHJvdmVkIGFjY3VyYWN5IGZvciBvbmUgdGFzayBtYXkgZGVncmFkZSBhbm90aGVyLiBWZXJzaW9uIGNvbnRyb2wgZ2l2ZXMgYXVkaXRhYmlsaXR5ICh3aG8gY2hhbmdlZCB3aGF0IGFuZCB3aGVuKSwgcm9sbGJhY2sgKHJldmVydCB0byBhIGtub3duLWdvb2QgcHJvbXB0IGluIHNlY29uZHMpLCBhbmQgYmxhbWUgKGxpbmsgcHJvZHVjdGlvbiBpbmNpZGVudHMgdG8gc3BlY2lmaWMgcHJvbXB0IGNoYW5nZXMpLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJjb250ZW50IjoiUHJvbXB0IFJlZ2lzdHJ5IERlc2lnbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBwcm9tcHQgcmVnaXN0cnkgc3RvcmVzIG5hbWUtdG8tdmVyc2lvbi10by10ZXh0IG1hcHBpbmdzIHdpdGggcmljaCBtZXRhZGF0YTogYXV0aG9yLCBjcmVhdGlvbiB0aW1lc3RhbXAsIHRhcmdldCBtb2RlbCwgZXZhbCBzY29yZXMsIGFuZCBwcm9tb3Rpb24gaGlzdG9yeS4gVGhlIHJlZ2lzdHJ5IGV4cG9zZXMgYSBtaW5pbWFsIEFQSSDigJQgZ2V0KG5hbWUsIHZlcnNpb24pLCBzZXQobmFtZSwgdGV4dCwgbWV0YWRhdGEpLCBwcm9tb3RlX3RvX3Byb2R1Y3Rpb24obmFtZSwgdmVyc2lvbiksIGFuZCByb2xsYmFjayhuYW1lKSDigJQgYW5kIHBlcnNpc3RzIHN0YXRlIHRvIGEgZGF0YWJhc2Ugb3IgdmVyc2lvbmVkIGZpbGUgc3RvcmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiY2xhc3MgUHJvbXB0UmVnaXN0cnk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLl9zdG9yZSA9IHt9XG4gICAgICAgIHNlbGYuX3Byb2QgPSB7fVxuXG4gICAgZGVmIHNldChzZWxmLCBuYW1lLCB2ZXJzaW9uLCB0ZXh0LCBtZXRhPU5vbmUpOlxuICAgICAgICBzZWxmLl9zdG9yZS5zZXRkZWZhdWx0KG5hbWUsIHt9KVt2ZXJzaW9uXSA9IHtcdTAwMjd0ZXh0XHUwMDI3OiB0ZXh0LCBcdTAwMjdtZXRhXHUwMDI3OiBtZXRhIG9yIHt9fVxuXG4gICAgZGVmIGdldChzZWxmLCBuYW1lLCB2ZXJzaW9uPU5vbmUpOlxuICAgICAgICB2ZXIgPSB2ZXJzaW9uIG9yIHNlbGYuX3Byb2QuZ2V0KG5hbWUpXG4gICAgICAgIHJldHVybiBzZWxmLl9zdG9yZVtuYW1lXVt2ZXJdW1x1MDAyN3RleHRcdTAwMjddXG5cbiAgICBkZWYgcHJvbW90ZShzZWxmLCBuYW1lLCB2ZXJzaW9uKTpcbiAgICAgICAgc2VsZi5fcHJvZFtuYW1lXSA9IHZlcnNpb25cblxuICAgIGRlZiByb2xsYmFjayhzZWxmLCBuYW1lLCBzdGVwcz0xKTpcbiAgICAgICAgdmVyc2lvbnMgPSBsaXN0KHNlbGYuX3N0b3JlW25hbWVdLmtleXMoKSlcbiAgICAgICAgc2VsZi5fcHJvZFtuYW1lXSA9IHZlcnNpb25zW21heCgwLCB2ZXJzaW9ucy5pbmRleChzZWxmLl9wcm9kW25hbWVdKSAtIHN0ZXBzKV0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVzZSBzZW1hbnRpYyB2ZXJzaW9uaW5nIGZvciBwcm9tcHQgbmFtZXMg4oCUIG1ham9yIGJ1bXBzIGZvciBzdHJ1Y3R1cmFsIHJld3JpdGVzLCBtaW5vciBidW1wcyBmb3Igd29yZGluZyB0d2Vha3MsIHBhdGNoIHZlcnNpb25zIGZvciB0eXBvIGZpeGVzLiBUYWcgZXZlcnkgdmVyc2lvbiB3aXRoIHRoZSBtb2RlbCBmYW1pbHkgaXQgdGFyZ2V0czsgYSBwcm9tcHQgdHVuZWQgZm9yIGNsYXVkZS0zLW9wdXMgbWF5IGRlZ3JhZGUgb24gY2xhdWRlLTMtaGFpa3Ugd2l0aG91dCByZXR1bmluZy4gU3RvcmUgZGlmZnMgYmV0d2VlbiB2ZXJzaW9ucyBmb3IgaHVtYW4gcmV2aWV3IGFsb25nc2lkZSB0aGUgZXZhbCBzY29yZXMgdGhhdCBtb3RpdmF0ZWQgZWFjaCBjaGFuZ2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImNvbnRlbnQiOiJFdmFsdWF0aW9uLURyaXZlbiBJdGVyYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5ldmVyIHByb21vdGUgYSBwcm9tcHQgd2l0aG91dCBydW5uaW5nIGV2YWxzLiBBbiBldmFsIGhhcm5lc3MgbWVhc3VyZXMgdGFzay1zcGVjaWZpYyBtZXRyaWNzIOKAlCBleGFjdCBtYXRjaCwgQkxFVSwgUk9VR0UsIG9yIGFuIExMTS1qdWRnZSBzY29yZSDigJQgb24gYSBmaXhlZCBoZWxkLW91dCB0ZXN0IHNldCBiZWZvcmUgYW5kIGFmdGVyIGVhY2ggY2hhbmdlLiBUaGUgZGVsdGEgdGVsbHMgeW91IHdoZXRoZXIgdGhlIGVkaXQgaXMgYW4gaW1wcm92ZW1lbnQgb3IgYSByZWdyZXNzaW9uLCBhbmQgdGhlIGFic29sdXRlIHNjb3JlIHByb3ZpZGVzIGEgZGVwbG95bWVudCB0aHJlc2hvbGQgdG8gZW5mb3JjZSBpbiBDSSBnYXRlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgc3RhdGlzdGljc1xuXG5kZWYgcnVuX2V2YWwocHJvbXB0X3RlbXBsYXRlLCBldmFsX2RhdGFzZXQsIGxsbV9jYWxsLCBqdWRnZV9jYWxsKTpcbiAgICBzY29yZXMgPSBbXVxuICAgIGZvciBpdGVtIGluIGV2YWxfZGF0YXNldDpcbiAgICAgICAgcHJvbXB0ID0gcHJvbXB0X3RlbXBsYXRlLmZvcm1hdCgqKml0ZW1bXHUwMDI3aW5wdXRzXHUwMDI3XSlcbiAgICAgICAgb3V0cHV0ID0gbGxtX2NhbGwocHJvbXB0KVxuICAgICAgICBleGFjdCA9IGludChvdXRwdXQuc3RyaXAoKSA9PSBpdGVtW1x1MDAyN2V4cGVjdGVkXHUwMDI3XS5zdHJpcCgpKVxuICAgICAgICBqdWRnZSA9IGp1ZGdlX2NhbGwob3V0cHV0LCBpdGVtW1x1MDAyN2V4cGVjdGVkXHUwMDI3XSkgICMgMC0xIHNjb3JlXG4gICAgICAgIHNjb3Jlcy5hcHBlbmQoKGV4YWN0ICsganVkZ2UpIC8gMilcbiAgICByZXR1cm4ge1xuICAgICAgICBcdTAwMjdwYXNzX3JhdGVcdTAwMjc6IHN0YXRpc3RpY3MubWVhbihzY29yZXMpLFxuICAgICAgICBcdTAwMjduXHUwMDI3OiBsZW4oc2NvcmVzKSxcbiAgICAgICAgXHUwMDI3c3RkXHUwMDI3OiBzdGF0aXN0aWNzLnN0ZGV2KHNjb3JlcykgaWYgbGVuKHNjb3JlcykgXHUwMDNlIDEgZWxzZSAwXG4gICAgfSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXZhbCB0ZXN0IHNldHMgc2hvdWxkIGJlIGN1cmF0ZWQsIG5vdCBzeW50aGV0aWMuIEluY2x1ZGUgYWR2ZXJzYXJpYWwgaW5wdXRzLCBlZGdlIGNhc2VzLCBhbmQgcmVhbCBmYWlsdXJlIG1vZGVzIGZyb20gcHJvZHVjdGlvbiBsb2dzLiBBaW0gZm9yIDIwMC01MDAgZXhhbXBsZXMgcGVyIHRhc2sg4oCUIGVub3VnaCB0byBkZXRlY3QgYSA1JSBtZXRyaWMgc2hpZnQgd2l0aCA4MCUgc3RhdGlzdGljYWwgcG93ZXIuIEZyZWV6ZSB0aGUgdGVzdCBzZXQ7IG5ldmVyIHR1bmUgYWdhaW5zdCBpdC4gUm90YXRlIGEgc21hbGwgcG9ydGlvbiBtb250aGx5IHRvIGRldGVjdCBkaXN0cmlidXRpb24gZHJpZnQgYW5kIGtlZXAgdGhlIHN1aXRlIHJlbGV2YW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJjb250ZW50IjoiQS9CIFRlc3RpbmcgUHJvbXB0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUm91dGUgYSBzaGFyZSBvZiBwcm9kdWN0aW9uIHRyYWZmaWMgdG8gdGhlIG5ldyBwcm9tcHQsIGxvZyAodXNlcl9pZCwgcHJvbXB0X3ZlcnNpb24sIG91dHB1dCwgb3V0Y29tZSkgZm9yIGV2ZXJ5IHJlcXVlc3QsIHRoZW4gY29tcHV0ZSBzaWduaWZpY2FuY2UgdXNpbmcgYSBjaGktc3F1YXJlIG9yIHQtdGVzdC4gUHJvbW90ZSBvbmx5IHdoZW4gcCBcdTAwM2MgMC4wNSBhbmQgdGhlIHRhcmdldCBtZXRyaWMgaW1wcm92ZXMuIEtlZXAgdGVzdHMgc2hvcnQg4oCUIDQ4LTcyIGhvdXJzIGZvciBoaWdoLXRyYWZmaWMgc3lzdGVtcyDigJQgdG8gbGltaXQgdXNlciBleHBvc3VyZSB0byBwb3RlbnRpYWxseSBkZWdyYWRlZCBvdXRwdXRzIGR1cmluZyB0aGUgdHJpYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGhhc2hsaWJcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IGNoaTJfY29udGluZ2VuY3lcblxuZGVmIGFiX3JvdXRlcih1c2VyX2lkLCB0cmVhdG1lbnRfcGN0PTAuMSk6XG4gICAgZGlnZXN0ID0gaW50KGhhc2hsaWIubWQ1KHVzZXJfaWQuZW5jb2RlKCkpLmhleGRpZ2VzdCgpLCAxNilcbiAgICByZXR1cm4gXHUwMDI3dHJlYXRtZW50XHUwMDI3IGlmIChkaWdlc3QgJSAxMDApIFx1MDAzYyAodHJlYXRtZW50X3BjdCAqIDEwMCkgZWxzZSBcdTAwMjdjb250cm9sXHUwMDI3XG5cbmRlZiBjb21wdXRlX3NpZ25pZmljYW5jZShjb3VudHMpOlxuICAgICMgY291bnRzOiB7XHUwMDI3Y29udHJvbFx1MDAyNzogW3N1Y2Nlc3MsIGZhaWxdLCBcdTAwMjd0cmVhdG1lbnRcdTAwMjc6IFtzdWNjZXNzLCBmYWlsXX1cbiAgICB0YWJsZSA9IFtjb3VudHNbXHUwMDI3Y29udHJvbFx1MDAyN10sIGNvdW50c1tcdTAwMjd0cmVhdG1lbnRcdTAwMjddXVxuICAgIGNoaTIsIHAsIGRvZiwgXyA9IGNoaTJfY29udGluZ2VuY3kodGFibGUpXG4gICAgcmV0dXJuIHtcdTAwMjdjaGkyXHUwMDI3OiByb3VuZChjaGkyLCA0KSwgXHUwMDI3cF92YWx1ZVx1MDAyNzogcm91bmQocCwgNCksXG4gICAgICAgICAgICBcdTAwMjdzaWduaWZpY2FudFx1MDAyNzogcCBcdTAwM2MgMC4wNSxcbiAgICAgICAgICAgIFx1MDAyN2xpZnRcdTAwMjc6IGNvdW50c1tcdTAwMjd0cmVhdG1lbnRcdTAwMjddWzBdIC8gc3VtKGNvdW50c1tcdTAwMjd0cmVhdG1lbnRcdTAwMjddKSAtXG4gICAgICAgICAgICAgICAgICAgIGNvdW50c1tcdTAwMjdjb250cm9sXHUwMDI3XVswXSAvIHN1bShjb3VudHNbXHUwMDI3Y29udHJvbFx1MDAyN10pfSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGxhbiB5b3VyIHNhbXBsZSBzaXplIGJlZm9yZSBsYXVuY2hpbmcgYW4gQS9CIHRlc3QuIEEgNSUgZXhwZWN0ZWQgbGlmdCB3aXRoIDgwJSBwb3dlciBhbmQgYWxwaGEgPSAwLjA1IHJlcXVpcmVzIHJvdWdobHkgMSw1MDAgc2FtcGxlcyBwZXIgYXJtLiBVbmRlci1wb3dlcmVkIHRlc3RzIHByb2R1Y2UgZmFsc2UgbmVnYXRpdmVzIGFuZCBjYXVzZSBnb29kIHByb21wdHMgdG8gYmUgZGlzY2FyZGVkLiBBbHdheXMgbG9nIHRoZSBmdWxsIG91dHB1dCBhbG9uZ3NpZGUgdGhlIGJpbmFyeSBvdXRjb21lIHRvIGVuYWJsZSBwb3N0LWhvYyBxdWFsaXRhdGl2ZSByZXZpZXcgb2YgZmFpbHVyZXMgb25jZSB0aGUgdGVzdCBjb25jbHVkZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImNvbnRlbnQiOiJSZWdyZXNzaW9uIFRlc3RpbmcgYW5kIENJL0NEIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZGQgYSBwcm9tcHQgZXZhbCBzdWl0ZSB0byBDSSDigJQgb24gZXZlcnkgcHVsbCByZXF1ZXN0IHRoYXQgbW9kaWZpZXMgYSBwcm9tcHQgZmlsZSwgdGhlIHBpcGVsaW5lIHJ1bnMgdGhlIGV2YWwgaGFybmVzcyBhbmQgYXNzZXJ0cyBhIG1pbmltdW0gcGFzcyByYXRlLiBCbG9jayB0aGUgbWVyZ2UgaWYgdGhlIHNjb3JlIGRyb3BzIGJlbG93IHRocmVzaG9sZCBvciBmYWxscyBtb3JlIHRoYW4gMyUgcmVsYXRpdmUgdG8gdGhlIGN1cnJlbnQgcHJvZHVjdGlvbiBwcm9tcHQuIEdhdGUgZGVwbG95bWVudHMgdGhlIHNhbWUgd2F5IHlvdSBnYXRlIGNvZGU6IGFsbCB0ZXN0cyBtdXN0IHBhc3MgYmVmb3JlIGFueSBjaGFuZ2VzIHNoaXAgdG8gcHJvZHVjdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgc3lzLCBwYXRobGliXG5cblBST0RfQkFTRUxJTkUgID0gMC44N1xuTUlOX1BBU1NfUkFURSAgPSAwLjg1XG5SRUdSRVNTSU9OX0dBUCA9IDAuMDNcblxuZGVmIGNpX3Byb21wdF9jaGVjayhwcl9wYXRoLCBldmFsX2RhdGFzZXQsIGxsbV9jYWxsLCBqdWRnZV9jYWxsKTpcbiAgICBjYW5kaWRhdGUgPSBwYXRobGliLlBhdGgocHJfcGF0aCkucmVhZF90ZXh0KClcbiAgICByZXN1bHQgPSBydW5fZXZhbChjYW5kaWRhdGUsIGV2YWxfZGF0YXNldCwgbGxtX2NhbGwsIGp1ZGdlX2NhbGwpXG4gICAgZGVsdGEgPSByZXN1bHRbXHUwMDI3cGFzc19yYXRlXHUwMDI3XSAtIFBST0RfQkFTRUxJTkVcbiAgICBwcmludChcdTAwMjdQYXNzIHJhdGU6IHs6LjNmfSAgRGVsdGE6IHs6Ky4zZn1cdTAwMjcuZm9ybWF0KHJlc3VsdFtcdTAwMjdwYXNzX3JhdGVcdTAwMjddLCBkZWx0YSkpXG4gICAgaWYgcmVzdWx0W1x1MDAyN3Bhc3NfcmF0ZVx1MDAyN10gXHUwMDNjIE1JTl9QQVNTX1JBVEU6XG4gICAgICAgIHByaW50KFx1MDAyN0ZBSUw6IGJlbG93IG1pbmltdW0gdGhyZXNob2xkXHUwMDI3KTsgc3lzLmV4aXQoMSlcbiAgICBpZiBkZWx0YSBcdTAwM2MgLVJFR1JFU1NJT05fR0FQOlxuICAgICAgICBwcmludChcdTAwMjdGQUlMOiByZWdyZXNzaW9uIHZzIHByb2QgYmFzZWxpbmVcdTAwMjcpOyBzeXMuZXhpdCgxKVxuICAgIHByaW50KFx1MDAyN1BBU1M6IHByb21wdCBjbGVhcmVkIGZvciBtZXJnZVx1MDAyNykifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vbml0b3IgcHJvbXB0IHF1YWxpdHkgaW4gcHJvZHVjdGlvbiB1c2luZyB0aGUgc2FtZSBzaWduYWxzIGFzIG1vZGVsIHBlcmZvcm1hbmNlOiByZXNwb25zZSBsYXRlbmN5LCB1c2VyIHNhdGlzZmFjdGlvbiBzY29yZXMsIGRvd25zdHJlYW0gdGFzayBzdWNjZXNzIHJhdGVzLCBhbmQgc2FmZXR5IGZpbHRlciB0cmlnZ2VyIHJhdGVzLiBTZXQgYWxlcnRzIG9uIDctZGF5IHJvbGxpbmcgbWV0cmljIHdpbmRvd3MuIFdoZW4gYW4gYWxlcnQgZmlyZXMsIGNoZWNrIHRoZSBwcm9tcHQgY2hhbmdlbG9nIGZpcnN0IOKAlCBhIHJlY2VudCBlZGl0IGlzIG9mdGVuIHRoZSByb290IGNhdXNlLCBhbmQgYSBwcm9tcHQgcm9sbGJhY2sgaXMgZmFzdGVyIHRoYW4gZGVidWdnaW5nLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsImNvbnRlbnQiOiJQcm9tcHRzIGFyZSBoeXBlcnBhcmFtZXRlcnMg4oCUIHRyZWF0IGNoYW5nZXMgd2l0aCB0aGUgc2FtZSByaWdvciBhcyBjb2RlOiBicmFuY2gsIHdyaXRlIGV2YWxzLCByZXZpZXcgdGhlIGRpZmYsIGRlcGxveSBiZWhpbmQgYSBmZWF0dXJlIGZsYWcsIGFuZCBtb25pdG9yIG1ldHJpY3MgYmVmb3JlIGZ1bGwgcm9sbG91dC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1haW50YWluIGEgc3RydWN0dXJlZCBjaGFuZ2UgbG9nIGZvciBldmVyeSBwcm9tcHQgaW4geW91ciByZWdpc3RyeS4gRWFjaCBlbnRyeSByZWNvcmRzIHRoZSB2ZXJzaW9uLCBhdXRob3IsIHRpbWVzdGFtcCwgbW90aXZhdGlvbiAoZS5nLiwgcmVkdWNlZCBoYWxsdWNpbmF0aW9uIHJhdGUgYnkgNCUpLCBsaW5rZWQgZXZhbCBydW4gSUQsIGFuZCBkZXBsb3ltZW50IHN0YXR1cy4gVGhlIGNoYW5nZSBsb2cgaXMgZG9jdW1lbnRhdGlvbiBmb3IgbmV3IHRlYW0gbWVtYmVycyBhbmQgZXZpZGVuY2UgaW4gaW5jaWRlbnQgcG9zdC1tb3J0ZW1zIHdoZW4gYSBwcm9tcHQgY2hhbmdlIGlzIGltcGxpY2F0ZWQgaW4gYSBwcm9kdWN0aW9uIHJlZ3Jlc3Npb24uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByYWN0aWNlIiwiV2l0aG91dCBWZXJzaW9uaW5nIiwiV2l0aCBWZXJzaW9uaW5nIiwiV2h5IEl0IE1hdHRlcnMiXSwicm93cyI6W1siVmVyc2lvbiBjb250cm9sIiwiUHJvbXB0cyBvdmVyd3JpdHRlbiBpbiBwbGFjZSIsIkZ1bGwgaGlzdG9yeSB3aXRoIGRpZmZzIiwiUm9sbGJhY2sgYW5kIGJsYW1lIl0sWyJFdmFsIG9uIGRlcGxveSIsIk1hbnVhbCBzcG90LWNoZWNrIG9yIG5vbmUiLCJBdXRvbWF0ZWQgc2NvcmUgZ2F0ZSIsIkNhdGNoIHJlZ3Jlc3Npb25zIGJlZm9yZSBwcm9kIl0sWyJBL0IgdGVzdGluZyIsIkd1dC1mZWVsIHByb21vdGlvbiIsIlN0YXRpc3RpY2FsIHNpZ25pZmljYW5jZSB0ZXN0IiwiQ29uZmlkZW50IGRlcGxveW1lbnQgZGVjaXNpb25zIl0sWyJSb2xsYmFjayIsIk1hbnVhbGx5IHJlY2FsbCBvbGQgdGV4dCIsIk9uZS1jb21tYW5kIHJldmVydCIsIk1pbnV0ZXMgdG8gcmVjb3ZlciB2cyBob3VycyJdLFsiUmVncmVzc2lvbiBzdWl0ZSIsIkFkIGhvYyB0ZXN0aW5nIGVhY2ggY2hhbmdlIiwiQ0kgYmxvY2tzIGJhZCBtZXJnZXMiLCJDb250aW51b3VzIHF1YWxpdHkgZW5mb3JjZW1lbnQiXSxbIkNoYW5nZSBsb2dnaW5nIiwiU2xhY2sgbWVzc2FnZXMgYW5kIG1lbW9yeSIsIlN0cnVjdHVyZWQgYXVkaXQgdHJhaWwiLCJBY2NvdW50YWJpbGl0eSBhbmQgcG9zdC1tb3J0ZW1zIl1dfSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoiaGVhZGluZyIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIml0ZW1zIjpbIlN0b3JlIHByb21wdHMgaW4gYSByZWdpc3RyeSB3aXRoIG5hbWUtdG8tdmVyc2lvbi10by10ZXh0IG1hcHBpbmdzLCByaWNoIG1ldGFkYXRhLCBhbmQgYSBvbmUtY29tbWFuZCBwcm9tb3RlL3JvbGxiYWNrIEFQSS4iLCJSdW4gYW4gZXZhbCBoYXJuZXNzIG9uIGV2ZXJ5IGNoYW5nZSDigJQgbWVhc3VyZSBleGFjdCBtYXRjaCwgQkxFVSwgb3IgTExNLWp1ZGdlIHNjb3JlcyBvbiBhIGZyb3plbiB0ZXN0IHNldCBiZWZvcmUgcHJvbW90aW5nIGFueSB2ZXJzaW9uIHRvIHByb2R1Y3Rpb24uIiwiQS9CIHRlc3Qgc2lnbmlmaWNhbnQgY2hhbmdlcyBpbiBwcm9kdWN0aW9uOyB1c2UgY2hpLXNxdWFyZSBzaWduaWZpY2FuY2UgdGVzdGluZyBhbmQgZW5mb3JjZSBwIFx1MDAzYyAwLjA1IGJlZm9yZSBjb21taXR0aW5nIHRvIGEgZnVsbCByb2xsb3V0LiIsIkdhdGUgcHJvbXB0IGNoYW5nZXMgaW4gQ0kgZXhhY3RseSBsaWtlIGNvZGUg4oCUIGFzc2VydCBhIG1pbmltdW0gcGFzcyByYXRlIGFuZCBtYXhpbXVtIHJlZ3Jlc3Npb24gZGVsdGEgb24gZXZlcnkgcHVsbCByZXF1ZXN0IHRoYXQgdG91Y2hlcyBhIHByb21wdCBmaWxlLiIsIk1vbml0b3IgcHJvZHVjdGlvbiBwcm9tcHQgcXVhbGl0eSB3aXRoIHJvbGxpbmcgbWV0cmljIHdpbmRvd3MgYW5kIGFsZXJ0czsgYSBwcm9tcHQgcm9sbGJhY2sgaXMgb2Z0ZW4gdGhlIGZhc3Rlc3QgaW5jaWRlbnQgcmVzcG9uc2UgYXZhaWxhYmxlLiIsIlRyZWF0IHByb21wdHMgYXMgZmlyc3QtY2xhc3MgYXJ0aWZhY3RzOiBicmFuY2ggdGhlbSwgcmV2aWV3IGRpZmZzLCBsb2cgZXZlcnkgY2hhbmdlIHdpdGggbW90aXZhdGlvbiBhbmQgZXZhbCBldmlkZW5jZSwgYW5kIHJlcXVpcmUgc2lnbi1vZmYgYmVmb3JlIHByb21vdGlvbi4iXX1d"
---
# Prompt Versioning and Management

Prompts are hyperparameters — a 5-word change can shift accuracy by 10% or break a production workflow entirely. Yet most teams treat prompt files as ad hoc text, overwriting working versions without history, losing context, and unable to roll back when regressions appear. Disciplined prompt versioning closes the gap between prompt engineering and software engineering.

 Why Prompts Need Version Control

Prompts drift silently — model updates, A/B test results, and team edits compound without a history trail. A change that improved accuracy for one task may degrade another. Version control gives auditability (who changed what and when), rollback (revert to a known-good prompt in seconds), and blame (link production incidents to specific prompt changes).

 Prompt Registry Design

A prompt registry stores name-to-version-to-text mappings with rich metadata: author, creation timestamp, target model, eval scores, and promotion history. The registry exposes a minimal API — get(name, version), set(name, text, metadata), promote_to_production(name, version), and rollback(name) — and persists state to a database or versioned file store.

```
class PromptRegistry:
    def __init__(self):
        self._store = {}
        self._prod = {}

    def set(self, name, version, text, meta=None):
        self._store.setdefault(name, {})[version] = {'text': text, 'meta': meta or {}}

    def get(self, name, version=None):
        ver = version or self._prod.get(name)
        return self._store[name][ver]['text']

    def promote(self, name, version):
        self._prod[name] = version

    def rollback(self, name, steps=1):
        versions = list(self._store[name].keys())
        self._prod[name] = versions[max(0, versions.index(self._prod[name]) - steps)]
```

Use semantic versioning for prompt names — major bumps for structural rewrites, minor bumps for wording tweaks, patch versions for typo fixes. Tag every version with the model family it targets; a prompt tuned for claude-3-opus may degrade on claude-3-haiku without retuning. Store diffs between versions for human review alongside the eval scores that motivated each change.

 Evaluation-Driven Iteration

Never promote a prompt without running evals. An eval harness measures task-specific metrics — exact match, BLEU, ROUGE, or an LLM-judge score — on a fixed held-out test set before and after each change. The delta tells you whether the edit is an improvement or a regression, and the absolute score provides a deployment threshold to enforce in CI gates.

```
import statistics

def run_eval(prompt_template, eval_dataset, llm_call, judge_call):
    scores = []
    for item in eval_dataset:
        prompt = prompt_template.format(**item['inputs'])
        output = llm_call(prompt)
        exact = int(output.strip() == item['expected'].strip())
        judge = judge_call(output, item['expected'])  # 0-1 score
        scores.append((exact + judge) / 2)
    return {
        'pass_rate': statistics.mean(scores),
        'n': len(scores),
        'std': statistics.stdev(scores) if len(scores) > 1 else 0
    }
```

Eval test sets should be curated, not synthetic. Include adversarial inputs, edge cases, and real failure modes from production logs. Aim for 200-500 examples per task — enough to detect a 5% metric shift with 80% statistical power. Freeze the test set; never tune against it. Rotate a small portion monthly to detect distribution drift and keep the suite relevant.

 A/B Testing Prompts

Route a share of production traffic to the new prompt, log (user_id, prompt_version, output, outcome) for every request, then compute significance using a chi-square or t-test. Promote only when p < 0.05 and the target metric improves. Keep tests short — 48-72 hours for high-traffic systems — to limit user exposure to potentially degraded outputs during the trial.

```
import hashlib
from scipy.stats import chi2_contingency

def ab_router(user_id, treatment_pct=0.1):
    digest = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
    return 'treatment' if (digest % 100) < (treatment_pct * 100) else 'control'

def compute_significance(counts):
    # counts: {'control': [success, fail], 'treatment': [success, fail]}
    table = [counts['control'], counts['treatment']]
    chi2, p, dof, _ = chi2_contingency(table)
    return {'chi2': round(chi2, 4), 'p_value': round(p, 4),
            'significant': p < 0.05,
            'lift': counts['treatment'][0] / sum(counts['treatment']) -
                    counts['control'][0] / sum(counts['control'])}
```

Plan your sample size before launching an A/B test. A 5% expected lift with 80% power and alpha = 0.05 requires roughly 1,500 samples per arm. Under-powered tests produce false negatives and cause good prompts to be discarded. Always log the full output alongside the binary outcome to enable post-hoc qualitative review of failures once the test concludes.

 Regression Testing and CI/CD

Add a prompt eval suite to CI — on every pull request that modifies a prompt file, the pipeline runs the eval harness and asserts a minimum pass rate. Block the merge if the score drops below threshold or falls more than 3% relative to the current production prompt. Gate deployments the same way you gate code: all tests must pass before any changes ship to production.

```
import sys, pathlib

PROD_BASELINE  = 0.87
MIN_PASS_RATE  = 0.85
REGRESSION_GAP = 0.03

def ci_prompt_check(pr_path, eval_dataset, llm_call, judge_call):
    candidate = pathlib.Path(pr_path).read_text()
    result = run_eval(candidate, eval_dataset, llm_call, judge_call)
    delta = result['pass_rate'] - PROD_BASELINE
    print('Pass rate: {:.3f}  Delta: {:+.3f}'.format(result['pass_rate'], delta))
    if result['pass_rate'] < MIN_PASS_RATE:
        print('FAIL: below minimum threshold'); sys.exit(1)
    if delta < -REGRESSION_GAP:
        print('FAIL: regression vs prod baseline'); sys.exit(1)
    print('PASS: prompt cleared for merge')
```

Monitor prompt quality in production using the same signals as model performance: response latency, user satisfaction scores, downstream task success rates, and safety filter trigger rates. Set alerts on 7-day rolling metric windows. When an alert fires, check the prompt changelog first — a recent edit is often the root cause, and a prompt rollback is faster than debugging.

> **info**: Prompts are hyperparameters — treat changes with the same rigor as code: branch, write evals, review the diff, deploy behind a feature flag, and monitor metrics before full rollout.

Maintain a structured change log for every prompt in your registry. Each entry records the version, author, timestamp, motivation (e.g., reduced hallucination rate by 4%), linked eval run ID, and deployment status. The change log is documentation for new team members and evidence in incident post-mortems when a prompt change is implicated in a production regression.

| Practice | Without Versioning | With Versioning | Why It Matters |
| --- | --- | --- | --- |
| Version control | Prompts overwritten in place | Full history with diffs | Rollback and blame |
| Eval on deploy | Manual spot-check or none | Automated score gate | Catch regressions before prod |
| A/B testing | Gut-feel promotion | Statistical significance test | Confident deployment decisions |
| Rollback | Manually recall old text | One-command revert | Minutes to recover vs hours |
| Regression suite | Ad hoc testing each change | CI blocks bad merges | Continuous quality enforcement |
| Change logging | Slack messages and memory | Structured audit trail | Accountability and post-mortems |

---

 Key Takeaways

- Store prompts in a registry with name-to-version-to-text mappings, rich metadata, and a one-command promote/rollback API.
- Run an eval harness on every change — measure exact match, BLEU, or LLM-judge scores on a frozen test set before promoting any version to production.
- A/B test significant changes in production; use chi-square significance testing and enforce p < 0.05 before committing to a full rollout.
- Gate prompt changes in CI exactly like code — assert a minimum pass rate and maximum regression delta on every pull request that touches a prompt file.
- Monitor production prompt quality with rolling metric windows and alerts; a prompt rollback is often the fastest incident response available.
- Treat prompts as first-class artifacts: branch them, review diffs, log every change with motivation and eval evidence, and require sign-off before promotion.

