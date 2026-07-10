---
title: "Image Editing with Diffusion Models: Inpainting, Instruct, and SDEdit"
slug: "image-editing-diffusion"
description: "Practical guide to the four main paradigms for diffusion-based image editing: SDEdit, InstructPix2Pix, masked inpainting, and attention manipulation."
tags: ["image-editing", "inpainting", "instructpix2pix", "sdedit", "diffusion"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaWZmdXNpb24gbW9kZWxzIGFyZSBmbGV4aWJsZSBpbWFnZSBlZGl0b3JzIGFzIHdlbGwgYXMgZ2VuZXJhdG9ycy4gVGhlIGNvcmUgaWRlYTogcGVydHVyYiBhbiBleGlzdGluZyBpbWFnZSB3aXRoIG5vaXNlIChmb3J3YXJkIHByb2Nlc3MpLCB0aGVuIGRlbm9pc2Ugd2l0aCBhIG5ldyBjb25kaXRpb25pbmcgc2lnbmFsIChwcm9tcHQsIG1hc2ssIG9yIHJlZmVyZW5jZSBpbWFnZSkuIFRoZSBkZWdyZWUgb2YgcGVydHVyYmF0aW9uIGNvbnRyb2xzIGhvdyBtdWNoIG9yaWdpbmFsIGNvbnRlbnQgaXMgcHJlc2VydmVkIHZlcnN1cyBob3cgZnJlZWx5IHRoZSBtb2RlbCBjYW4gZWRpdC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvdXIgbWFpbiBwYXJhZGlnbXMgZG9taW5hdGUgZGlmZnVzaW9uLWJhc2VkIGVkaXRpbmc6IFNERWRpdCAoYWRkIG5vaXNlLCBkZW5vaXNlIHdpdGggbmV3IHByb21wdCksIEluc3RydWN0UGl4MlBpeCAoZm9sbG93IG5hdHVyYWwgbGFuZ3VhZ2UgZWRpdCBpbnN0cnVjdGlvbnMpLCBtYXNrZWQgaW5wYWludGluZyAocmVwbGFjZSBzcGVjaWZpYyByZWdpb25zKSwgYW5kIGF0dGVudGlvbiBtYW5pcHVsYXRpb24gKHN3YXAgY3Jvc3MtYXR0ZW50aW9uIG1hcHMgdG8gcHJlc2VydmUgc3BhdGlhbCBsYXlvdXQpLiBFYWNoIG1ha2VzIGRpZmZlcmVudCB0cmFkZW9mZnMgYmV0d2VlbiBlZGl0IHN0cmVuZ3RoIGFuZCBzdHJ1Y3R1cmFsIHByZXNlcnZhdGlvbi4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsImNvbnRlbnQiOiJTREVkaXQgc3RyZW5ndGggcGFyYW1ldGVyIGNvbnRyb2xzIHRoZSBlZGl0IG1hZ25pdHVkZTogMC4zLTAuNSBmb3IgY29sb3IvdGV4dHVyZSBjaGFuZ2VzLCAwLjYtMC44IGZvciBzdHJ1Y3R1cmFsIGVkaXRzLiBBYm92ZSAwLjggYW5kIHRoZSBvdXRwdXQgZGl2ZXJnZXMgZnJvbSB0aGUgb3JpZ2luYWwg4oCUIHVzZSBpbnBhaW50aW5nIGZvciBwcmVjaXNlIHJlZ2lvbiBjb250cm9sLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNERWRpdDogTm9pc2UgYW5kIERlbm9pc2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNERWRpdCAoU29uZyBldCBhbC4sIDIwMjIpIGlzIHRoZSBzaW1wbGVzdCBlZGl0aW5nIGFwcHJvYWNoOiBlbmNvZGUgdGhlIHNvdXJjZSBpbWFnZSB0byBsYXRlbnRzLCBhZGQgbm9pc2UgdXAgdG8gdGltZXN0ZXAgdF9zdHJlbmd0aCAocGFydGlhbCBmb3J3YXJkIHByb2Nlc3MpLCB0aGVuIGRlbm9pc2UgZnJvbSB0X3N0cmVuZ3RoIHRvIDAgd2l0aCBhIG5ldyBwcm9tcHQuIEhpZ2hlciBzdHJlbmd0aCBtZWFucyBtb3JlIG5vaXNlLCBtb3JlIGZyZWVkb20gZm9yIGVkaXRzLCBhbmQgbGVzcyBwcmVzZXJ2YXRpb24gb2YgdGhlIG9yaWdpbmFsIGltYWdlIHN0cnVjdHVyZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBTREVkaXQ6IHBhcnRpYWwgbm9pc2UgdGhlbiBkZW5vaXNlIHdpdGggbmV3IHByb21wdFxuZGVmIHNkZWRpdChwaXBlLCBpbWFnZSwgcHJvbXB0LCBzdHJlbmd0aD0wLjYsIHN0ZXBzPTUwKTpcbiAgICBcIlwiXCJcbiAgICBzdHJlbmd0aDogMCA9IG5vIGVkaXQsIDEgPSBmdWxsIHJlZ2VuZXJhdGlvbi5cbiAgICBMb3dlciBzdHJlbmd0aCBwcmVzZXJ2ZXMgbW9yZSBvZiB0aGUgb3JpZ2luYWwuXG4gICAgXCJcIlwiXG4gICAgbGF0ZW50ID0gcGlwZS52YWUuZW5jb2RlKGltYWdlKS5sYXRlbnRfZGlzdC5zYW1wbGUoKVxuICAgIGxhdGVudCA9IGxhdGVudCAqIHBpcGUudmFlLmNvbmZpZy5zY2FsaW5nX2ZhY3RvclxuXG4gICAgdF9zdGFydCA9IGludChzdHJlbmd0aCAqIHN0ZXBzKVxuICAgIG5vaXNlICAgPSB0b3JjaC5yYW5kbl9saWtlKGxhdGVudClcbiAgICBub2lzeSAgID0gcGlwZS5zY2hlZHVsZXIuYWRkX25vaXNlKFxuICAgICAgICBsYXRlbnQsIG5vaXNlLCB0aW1lc3RlcHM9dG9yY2gudGVuc29yKFt0X3N0YXJ0XSkpXG5cbiAgICByZXR1cm4gcGlwZShwcm9tcHQsIGxhdGVudHM9bm9pc3ksXG4gICAgICAgICAgICAgICAgbnVtX2luZmVyZW5jZV9zdGVwcz1zdGVwcyxcbiAgICAgICAgICAgICAgICBzdHJlbmd0aD1zdHJlbmd0aCkuaW1hZ2VzWzBdIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTREVkaXQgd29ya3Mgd2VsbCBmb3IgZ2xvYmFsIHN0eWxlIGNoYW5nZXMgKG9pbCBwYWludGluZywgc2tldGNoLCB3YXRlcmNvbG9yKSwgY29sb3Igc2hpZnRzLCBhbmQgd2VhdGhlciBjaGFuZ2VzLiBJdCBzdHJ1Z2dsZXMgd2l0aCBwcmVjaXNlIGxvY2FsIGVkaXRzIGJlY2F1c2Ugbm9pc2UgcGVydHVyYnMgdGhlIGVudGlyZSBpbWFnZSB1bmlmb3JtbHkuIEZvciB0YXJnZXRlZCBlZGl0cyB0byBzcGVjaWZpYyBvYmplY3RzIG9yIHJlZ2lvbnMsIGlucGFpbnRpbmcgd2l0aCBhbiBleHBsaWNpdCBtYXNrIGlzIG1vcmUgYXBwcm9wcmlhdGUgYW5kIHJlbGlhYmxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByb21wdC1CYXNlZCBFZGl0aW5nIChJbnN0cnVjdFBpeDJQaXgpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbnN0cnVjdFBpeDJQaXggKEJyb29rcyBldCBhbC4sIDIwMjMpIHRyYWlucyBhIG1vZGVsIHRvIGZvbGxvdyBuYXR1cmFsIGxhbmd1YWdlIGVkaXRpbmcgaW5zdHJ1Y3Rpb25zIGRpcmVjdGx5LiBHaXZlbiBhbiBpbWFnZSBhbmQgYW4gaW5zdHJ1Y3Rpb24gbGlrZSBcdTAwMjd0dXJuIHRoZSBza3kgaW50byBhIHN1bnNldFx1MDAyNywgdGhlIG1vZGVsIHByb2R1Y2VzIHRoZSBlZGl0ZWQgcmVzdWx0LiBUcmFpbmluZyBkYXRhIGlzIHN5bnRoZXNpemVkIHVzaW5nIEdQVC00IHRvIGdlbmVyYXRlIGluc3RydWN0aW9uIHBhaXJzIGFuZCBTdGFibGUgRGlmZnVzaW9uIHRvIHByb2R1Y2UgYmVmb3JlL2FmdGVyIGltYWdlIHBhaXJzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGFyY2hpdGVjdHVyZSBleHRlbmRzIGNsYXNzaWZpZXItZnJlZSBndWlkYW5jZSB0byB0d28gY29uZGl0aW9uaW5nIHNpZ25hbHM6IHRoZSBzb3VyY2UgaW1hZ2UgYW5kIHRoZSB0ZXh0IGluc3RydWN0aW9uLiBUaGlzIHJlcXVpcmVzIHR3byBndWlkYW5jZSBzY2FsZXMg4oCUIHNfVCBmb3IgdGV4dCBhZGhlcmVuY2UgYW5kIHNfSSBmb3IgaW1hZ2UgcHJlc2VydmF0aW9uIOKAlCBnaXZpbmcgaW5kZXBlbmRlbnQgY29udHJvbCBvdmVyIGhvdyBjbG9zZWx5IHRoZSBtb2RlbCBmb2xsb3dzIHRoZSBpbnN0cnVjdGlvbiB2cy4gcHJlc2VydmluZyBvcmlnaW5hbCBjb250ZW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIEluc3RydWN0UGl4MlBpeCBkb3VibGUgY2xhc3NpZmllci1mcmVlIGd1aWRhbmNlXG5kZWYgaXAycF9jZmcodW5ldCwgeF90LCB0LCBpbWdfY29uZCwgdHh0X2NvbmQsXG4gICAgICAgICAgICBpbWdfdW5jLCB0eHRfdW5jLCBzX3RleHQ9Ny41LCBzX2ltZz0xLjUpOlxuICAgIFwiXCJcIlxuICAgIHNfdGV4dDogaGlnaGVyID0gbW9yZSBpbnN0cnVjdGlvbi1mb2xsb3dpbmdcbiAgICBzX2ltZzogIGhpZ2hlciA9IGNsb3NlciB0byBzb3VyY2UgaW1hZ2VcbiAgICBcIlwiXCJcbiAgICBlcHNfZnVsbCA9IHVuZXQoeF90LCB0LCBpbWdfY29uZCwgdHh0X2NvbmQpXG4gICAgZXBzX2ltZyAgPSB1bmV0KHhfdCwgdCwgaW1nX2NvbmQsIHR4dF91bmMpXG4gICAgZXBzX25vbmUgPSB1bmV0KHhfdCwgdCwgaW1nX3VuYywgIHR4dF91bmMpXG5cbiAgICByZXR1cm4gKGVwc19ub25lXG4gICAgICAgICAgICArIHNfaW1nICAqIChlcHNfaW1nICAtIGVwc19ub25lKVxuICAgICAgICAgICAgKyBzX3RleHQgKiAoZXBzX2Z1bGwgLSBlcHNfaW1nKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnBhaW50aW5nIHdpdGggTWFza2VkIERpZmZ1c2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW5wYWludGluZyBmaWxscyBhIG1hc2tlZCByZWdpb24gd2hpbGUgcHJlc2VydmluZyB0aGUgcmVzdCBvZiB0aGUgaW1hZ2UgZXhhY3RseS4gQXQgZWFjaCBkZW5vaXNpbmcgc3RlcCwgbGF0ZW50cyBvdXRzaWRlIHRoZSBtYXNrIGFyZSByZXBsYWNlZCB3aXRoIHRoZSBub2lzeSBlbmNvZGVkIG9yaWdpbmFsIOKAlCBlbnN1cmluZyB1bm1hc2tlZCBjb250ZW50IGlzIHBpeGVsLXBlcmZlY3QgYWZ0ZXIgZGVjb2RpbmcuIE9ubHkgdGhlIG1hc2tlZCByZWdpb24gaXMgZnJlZWx5IGdlbmVyYXRlZCBieSB0aGUgZGVub2lzZXIgYmFzZWQgb24gdGhlIHByb21wdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBNYXNrZWQgaW5wYWludGluZzogYW5jaG9yIHVubWFza2VkIHJlZ2lvbiBlYWNoIHN0ZXBcbmRlZiBpbnBhaW50X3N0ZXAoc2NoZWR1bGVyLCB1bmV0LCB4X3QsIHQsXG4gICAgICAgICAgICAgICAgIG9yaWdpbmFsX2xhdGVudCwgbWFzaywgcHJvbXB0X2VtYmVkcyk6XG4gICAgXCJcIlwiXG4gICAgbWFzazogMSA9IGlucGFpbnQgcmVnaW9uLCAwID0ga2VlcCBvcmlnaW5hbCBwaXhlbHNcbiAgICBcIlwiXCJcbiAgICBub2lzZSA9IHRvcmNoLnJhbmRuX2xpa2Uob3JpZ2luYWxfbGF0ZW50KVxuICAgIG5vaXN5X29yaWcgPSBzY2hlZHVsZXIuYWRkX25vaXNlKFxuICAgICAgICBvcmlnaW5hbF9sYXRlbnQsIG5vaXNlLCB0aW1lc3RlcHM9dClcblxuICAgICMgQmxlbmQ6IG1vZGVsIG91dHB1dCBpbnNpZGUgbWFzaywgbm9pc3kgb3JpZ2luYWwgb3V0c2lkZVxuICAgIHhfdCA9IG1hc2sgKiB4X3QgKyAoMSAtIG1hc2spICogbm9pc3lfb3JpZ1xuXG4gICAgb3V0ID0gdW5ldCh4X3QsIHQsIGVuY29kZXJfaGlkZGVuX3N0YXRlcz1wcm9tcHRfZW1iZWRzKVxuICAgIHJldHVybiBzY2hlZHVsZXIuc3RlcChvdXQuc2FtcGxlLCB0LCB4X3QpLnByZXZfc2FtcGxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbnBhaW50aW5nIGhhcyBhIHNlYW0gcHJvYmxlbTogZ2VuZXJhdGVkIHJlZ2lvbnMgbXVzdCBibGVuZCBzZWFtbGVzc2x5IHdpdGggdW5lZGl0ZWQgYXJlYXMuIEZpbmUtdHVuZWQgaW5wYWludGluZyBtb2RlbHMgKFN0YWJsZSBEaWZmdXNpb24gSW5wYWludGluZykgYXJlIHRyYWluZWQgd2l0aCByYW5kb20gbWFza3Mgc28gdGhlIG1vZGVsIGxlYXJucyB0byBwcm9kdWNlIHBsYXVzaWJsZSBib3VuZGFyaWVzLiBGZWF0aGVyaW5nIG1hc2tzIHdpdGggYSBHYXVzc2lhbiBibHVyIHJlZHVjZXMgdmlzaWJsZSBzZWFtIGFydGlmYWN0cyBpbiBjaGFsbGVuZ2luZyBjYXNlcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiUmVxdWlyZXMgTWFzaz8iLCJQcmVzZXJ2ZXMgU3RydWN0dXJlIiwiRWRpdHMgU2VtYW50aWNzIiwiU3BlZWQgKHN0ZXBzKSIsIktleSBQYXBlciJdLCJyb3dzIjpbWyJTREVkaXQiLCJObyIsIlBhcnRpYWwgKHN0cmVuZ3RoLWRlcGVuZGVudCkiLCJZZXMiLCIyMC01MCIsIlNvbmcgZXQgYWwuIDIwMjIiXSxbIkluc3RydWN0UGl4MlBpeCIsIk5vIiwiSGlnaCAodmlhIGltYWdlIENGRykiLCJZZXMgKGluc3RydWN0aW9uLWZvbGxvd2luZykiLCI1MCIsIkJyb29rcyBldCBhbC4gMjAyMyJdLFsiU3RhYmxlIElucGFpbnQiLCJZZXMiLCJFeGFjdCAodW5tYXNrZWQgcmVnaW9uKSIsIlllcyAoaW4gbWFzayBvbmx5KSIsIjIwLTUwIiwiUm9tYmFjaCBldCBhbC4gMjAyMiJdLFsiUHJvbXB0LXRvLVByb21wdCIsIk5vIiwiSGlnaCAoYXR0ZW50aW9uIGluamVjdGlvbikiLCJQYXJ0aWFsICh3b3JkIHN3YXBzKSIsIjUwIiwiSGVydHogZXQgYWwuIDIwMjIiXSxbIkRpZmZFZGl0IiwiQXV0by1nZW5lcmF0ZWQiLCJIaWdoIiwiWWVzIChkaWZmLWJhc2VkIG1hc2spIiwiNTAiLCJDb3VhaXJvbiBldCBhbC4gMjAyMiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXR0ZW50aW9uLUJhc2VkIEVkaXRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByb21wdC10by1Qcm9tcHQgKEhlcnR6IGV0IGFsLiwgMjAyMikgZGlzY292ZXJlZCB0aGF0IGNyb3NzLWF0dGVudGlvbiBtYXBzIGluIFUtTmV0IGxheWVycyBlbmNvZGUgc3BhdGlhbCBsYXlvdXQg4oCUIHdoZXJlIGVhY2ggdG9rZW4gYXR0ZW5kcyBpbiB0aGUgaW1hZ2UuIEJ5IGluamVjdGluZyBjcm9zcy1hdHRlbnRpb24gbWFwcyBmcm9tIGEgc291cmNlIGdlbmVyYXRpb24gaW50byBhIHRhcmdldCBnZW5lcmF0aW9uIHdpdGggYSBtb2RpZmllZCBwcm9tcHQsIHlvdSBjYW4gY2hhbmdlIHNlbWFudGljcyB3aGlsZSBwcmVzZXJ2aW5nIHNwYXRpYWwgc3RydWN0dXJlIHdpdGhvdXQgYW55IGV4cGxpY2l0IG1hc2suIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6IiMgUHJvbXB0LXRvLVByb21wdDogc3RvcmUgc291cmNlIGF0dGVudGlvbiwgaW5qZWN0IGludG8gdGFyZ2V0XG5hdHRuX3N0b3JlID0ge31cblxuZGVmIHN0b3JlX2hvb2sobmFtZSk6XG4gICAgZGVmIF9ob29rKG1vZHVsZSwgaW5wLCBvdXQpOlxuICAgICAgICBhdHRuX3N0b3JlW25hbWVdID0gb3V0LmRldGFjaCgpXG4gICAgcmV0dXJuIF9ob29rXG5cbiMgU3RlcCAxOiBnZW5lcmF0ZSB3aXRoIHNvdXJjZSBwcm9tcHQsIGNvbGxlY3QgbWFwc1xuZm9yIG5hbWUsIGxheWVyIGluIHVuZXQubmFtZWRfbW9kdWxlcygpOlxuICAgIGlmIFx1MDAyN2F0dG4yXHUwMDI3IGluIG5hbWU6ICAjIGNyb3NzLWF0dGVudGlvbiBvbmx5XG4gICAgICAgIGxheWVyLnJlZ2lzdGVyX2ZvcndhcmRfaG9vayhzdG9yZV9ob29rKG5hbWUpKVxuc291cmNlX21hcHMgPSBnZW5lcmF0ZShzb3VyY2VfcHJvbXB0LCB1bmV0KVxuXG4jIFN0ZXAgMjogZ2VuZXJhdGUgdGFyZ2V0LCBpbmplY3Qgc3RvcmVkIHNvdXJjZSBtYXBzXG5kZWYgaW5qZWN0X2hvb2sobmFtZSk6XG4gICAgZGVmIF9ob29rKG1vZHVsZSwgaW5wLCBvdXQpOlxuICAgICAgICByZXR1cm4gYXR0bl9zdG9yZVtuYW1lXSAgIyByZXBsYWNlIHdpdGggc291cmNlXG4gICAgcmV0dXJuIF9ob29rIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdHRlbnRpb24gaW5qZWN0aW9uIHdvcmtzIGJlc3QgZm9yIHdvcmQgc3dhcHMgYW5kIGF0dHJpYnV0ZSBjaGFuZ2VzIChkb2cgdG8gY2F0LCByZWQgdG8gYmx1ZSkuIEZvciBzdHJ1Y3R1cmFsIGNoYW5nZXMsIGluamVjdGlvbiBicmVha3MgYmVjYXVzZSB0aGUgbmV3IHByb21wdCBnZW51aW5lbHkgcmVxdWlyZXMgYSBkaWZmZXJlbnQgbGF5b3V0LiBEaWZmRWRpdCBleHRlbmRzIHRoaXMgYnkgdXNpbmcgdGhlIGRpZmZlcmVuY2UgYmV0d2VlbiBzb3VyY2UgYW5kIHRhcmdldCBhdHRlbnRpb24gbWFwcyB0byBhdXRvbWF0aWNhbGx5IGdlbmVyYXRlIGFuIGVkaXQgbWFzayDigJQgbm8gbWFudWFsIG1hc2tpbmcgcmVxdWlyZWQuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJERElNIGludmVyc2lvbiBpcyBhIHByZXJlcXVpc2l0ZSBmb3IgaGlnaC1maWRlbGl0eSBlZGl0aW5nIGluIGFsbCB0aGVzZSBtZXRob2RzOiBpbnN0ZWFkIG9mIHJhbmRvbSBub2lzZSwgaW52ZXJ0IHRoZSBzb3VyY2UgaW1hZ2UgdGhyb3VnaCB0aGUgcmV2ZXJzZSBPREUgdG8gcmVjb3ZlciBpdHMgYXBwcm94aW1hdGUgbm9pc2UuIFN0YXJ0aW5nIGRlbm9pc2luZyBmcm9tIHRoaXMgaW52ZXJ0ZWQgbm9pc2UgbWVhbnMgdGhlIGVkaXRlZCBpbWFnZSBuYXR1cmFsbHkgcHJlc2VydmVzIG1vcmUgc3RydWN0dXJlIGFuZCBkZXRhaWwgZnJvbSB0aGUgb3JpZ2luYWwgd2l0aG91dCBleHBsaWNpdCBjb25zdHJhaW50cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDaG9vc2UgeW91ciBlZGl0aW5nIHBhcmFkaWdtIGJhc2VkIG9uIHRoZSB0YXNrOiBTREVkaXQgZm9yIGdsb2JhbCBzdHlsZSBjaGFuZ2VzLCBJbnN0cnVjdFBpeDJQaXggZm9yIGluc3RydWN0aW9uLWZvbGxvd2luZyBlZGl0cyB3aXRob3V0IG1hc2tzLCBpbnBhaW50aW5nIGZvciBwcmVjaXNlIHJlZ2lvbiByZXBsYWNlbWVudCwgYW5kIFByb21wdC10by1Qcm9tcHQgZm9yIGxheW91dC1wcmVzZXJ2aW5nIHNlbWFudGljIGNoYW5nZXMuIENvbWJpbmluZyBtZXRob2RzIOKAlCBpbnBhaW50aW5nIGEgcmVnaW9uIHdpdGggU0RFZGl0IGJsZW5kaW5nIGF0IGJvdW5kYXJpZXMg4oCUIG9mdGVuIGdpdmVzIHRoZSBiZXN0IHJlc3VsdHMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZnJvbnRpZXIgaXMgbW92aW5nIHRvd2FyZCB1bmlmaWVkIGVkaXRpbmcgZnJhbWV3b3JrczogbW9kZWxzIGxpa2UgRkxVWC1GaWxsLCBBZG9iZSBGaXJlZmx5LCBhbmQgR29vZ2xlIEltYWdlbiBFZGl0b3IgdHJhaW4gZW5kLXRvLWVuZCBvbiBkaXZlcnNlIGVkaXRpbmcgdGFza3Mgd2l0aCB0YXNrLXNwZWNpZmljIGNvbmRpdGlvbmluZy4gVGhlc2Ugb3V0cGVyZm9ybSBtZXRob2Qtc3BlY2lmaWMgYXBwcm9hY2hlcyBieSBsZXZlcmFnaW5nIGNyb3NzLXRhc2sgZ2VuZXJhbGl6YXRpb24gYW5kIHByb2R1Y2luZyBtb3JlIGNvaGVyZW50IGVkaXRzIGFjcm9zcyBkaXZlcnNlIHByb21wdCB0eXBlcyBhbmQgaW1hZ2UgZG9tYWlucy4ifV0="
---
# Image Editing with Diffusion Models: Inpainting, Instruct, and SDEdit

## Overview

Diffusion models are flexible image editors as well as generators. The core idea: perturb an existing image with noise (forward process), then denoise with a new conditioning signal (prompt, mask, or reference image). The degree of perturbation controls how much original content is preserved versus how freely the model can edit.

Four main paradigms dominate diffusion-based editing: SDEdit (add noise, denoise with new prompt), InstructPix2Pix (follow natural language edit instructions), masked inpainting (replace specific regions), and attention manipulation (swap cross-attention maps to preserve spatial layout). Each makes different tradeoffs between edit strength and structural preservation.

> **tip**: SDEdit strength parameter controls the edit magnitude: 0.3-0.5 for color/texture changes, 0.6-0.8 for structural edits. Above 0.8 and the output diverges from the original — use inpainting for precise region control.

## SDEdit: Noise and Denoise

SDEdit (Song et al., 2022) is the simplest editing approach: encode the source image to latents, add noise up to timestep t_strength (partial forward process), then denoise from t_strength to 0 with a new prompt. Higher strength means more noise, more freedom for edits, and less preservation of the original image structure.

```python
# SDEdit: partial noise then denoise with new prompt
def sdedit(pipe, image, prompt, strength=0.6, steps=50):
    """
    strength: 0 = no edit, 1 = full regeneration.
    Lower strength preserves more of the original.
    """
    latent = pipe.vae.encode(image).latent_dist.sample()
    latent = latent * pipe.vae.config.scaling_factor

    t_start = int(strength * steps)
    noise   = torch.randn_like(latent)
    noisy   = pipe.scheduler.add_noise(
        latent, noise, timesteps=torch.tensor([t_start]))

    return pipe(prompt, latents=noisy,
                num_inference_steps=steps,
                strength=strength).images[0]
```

SDEdit works well for global style changes (oil painting, sketch, watercolor), color shifts, and weather changes. It struggles with precise local edits because noise perturbs the entire image uniformly. For targeted edits to specific objects or regions, inpainting with an explicit mask is more appropriate and reliable.

## Prompt-Based Editing (InstructPix2Pix)

InstructPix2Pix (Brooks et al., 2023) trains a model to follow natural language editing instructions directly. Given an image and an instruction like 'turn the sky into a sunset', the model produces the edited result. Training data is synthesized using GPT-4 to generate instruction pairs and Stable Diffusion to produce before/after image pairs.

The architecture extends classifier-free guidance to two conditioning signals: the source image and the text instruction. This requires two guidance scales — s_T for text adherence and s_I for image preservation — giving independent control over how closely the model follows the instruction vs. preserving original content.

```python
# InstructPix2Pix double classifier-free guidance
def ip2p_cfg(unet, x_t, t, img_cond, txt_cond,
            img_unc, txt_unc, s_text=7.5, s_img=1.5):
    """
    s_text: higher = more instruction-following
    s_img:  higher = closer to source image
    """
    eps_full = unet(x_t, t, img_cond, txt_cond)
    eps_img  = unet(x_t, t, img_cond, txt_unc)
    eps_none = unet(x_t, t, img_unc,  txt_unc)

    return (eps_none
            + s_img  * (eps_img  - eps_none)
            + s_text * (eps_full - eps_img))
```

## Inpainting with Masked Diffusion

Inpainting fills a masked region while preserving the rest of the image exactly. At each denoising step, latents outside the mask are replaced with the noisy encoded original — ensuring unmasked content is pixel-perfect after decoding. Only the masked region is freely generated by the denoiser based on the prompt.

```python
# Masked inpainting: anchor unmasked region each step
def inpaint_step(scheduler, unet, x_t, t,
                 original_latent, mask, prompt_embeds):
    """
    mask: 1 = inpaint region, 0 = keep original pixels
    """
    noise = torch.randn_like(original_latent)
    noisy_orig = scheduler.add_noise(
        original_latent, noise, timesteps=t)

    # Blend: model output inside mask, noisy original outside
    x_t = mask * x_t + (1 - mask) * noisy_orig

    out = unet(x_t, t, encoder_hidden_states=prompt_embeds)
    return scheduler.step(out.sample, t, x_t).prev_sample
```

Inpainting has a seam problem: generated regions must blend seamlessly with unedited areas. Fine-tuned inpainting models (Stable Diffusion Inpainting) are trained with random masks so the model learns to produce plausible boundaries. Feathering masks with a Gaussian blur reduces visible seam artifacts in challenging cases.

| Method | Requires Mask? | Preserves Structure | Edits Semantics | Speed (steps) | Key Paper |
| --- | --- | --- | --- | --- | --- |
| SDEdit | No | Partial (strength-dependent) | Yes | 20-50 | Song et al. 2022 |
| InstructPix2Pix | No | High (via image CFG) | Yes (instruction-following) | 50 | Brooks et al. 2023 |
| Stable Inpaint | Yes | Exact (unmasked region) | Yes (in mask only) | 20-50 | Rombach et al. 2022 |
| Prompt-to-Prompt | No | High (attention injection) | Partial (word swaps) | 50 | Hertz et al. 2022 |
| DiffEdit | Auto-generated | High | Yes (diff-based mask) | 50 | Couairon et al. 2022 |

## Attention-Based Editing

Prompt-to-Prompt (Hertz et al., 2022) discovered that cross-attention maps in U-Net layers encode spatial layout — where each token attends in the image. By injecting cross-attention maps from a source generation into a target generation with a modified prompt, you can change semantics while preserving spatial structure without any explicit mask.

```python
# Prompt-to-Prompt: store source attention, inject into target
attn_store = {}

def store_hook(name):
    def _hook(module, inp, out):
        attn_store[name] = out.detach()
    return _hook

# Step 1: generate with source prompt, collect maps
for name, layer in unet.named_modules():
    if 'attn2' in name:  # cross-attention only
        layer.register_forward_hook(store_hook(name))
source_maps = generate(source_prompt, unet)

# Step 2: generate target, inject stored source maps
def inject_hook(name):
    def _hook(module, inp, out):
        return attn_store[name]  # replace with source
    return _hook
```

Attention injection works best for word swaps and attribute changes (dog to cat, red to blue). For structural changes, injection breaks because the new prompt genuinely requires a different layout. DiffEdit extends this by using the difference between source and target attention maps to automatically generate an edit mask — no manual masking required.

DDIM inversion is a prerequisite for high-fidelity editing in all these methods: instead of random noise, invert the source image through the reverse ODE to recover its approximate noise. Starting denoising from this inverted noise means the edited image naturally preserves more structure and detail from the original without explicit constraints.

## Key Takeaways

Choose your editing paradigm based on the task: SDEdit for global style changes, InstructPix2Pix for instruction-following edits without masks, inpainting for precise region replacement, and Prompt-to-Prompt for layout-preserving semantic changes. Combining methods — inpainting a region with SDEdit blending at boundaries — often gives the best results.

The frontier is moving toward unified editing frameworks: models like FLUX-Fill, Adobe Firefly, and Google Imagen Editor train end-to-end on diverse editing tasks with task-specific conditioning. These outperform method-specific approaches by leveraging cross-task generalization and producing more coherent edits across diverse prompt types and image domains.

