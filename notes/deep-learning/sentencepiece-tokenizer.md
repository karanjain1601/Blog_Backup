---
title: "SentencePiece — Unigram Language Model Tokenizer and Byte Fallback"
slug: "sentencepiece-tokenizer"
description: "How SentencePiece processes raw Unicode without pre-tokenization, the Unigram LM algorithm with EM training and pruning, byte fallback for rare characters, and subword regularization."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2VudGVuY2VQaWVjZSBpcyBhIGxhbmd1YWdlLWluZGVwZW5kZW50IHRva2VuaXplciB1c2VkIGJ5IExMYU1BLCBHZW1tYSwgTWlzdHJhbCwgVDUsIGFuZCBBTEJFUlQuIFVubGlrZSBCUEUgaW1wbGVtZW50YXRpb25zIHRoYXQgZmlyc3Qgc3BsaXQgdGV4dCBvbiB3aGl0ZXNwYWNlLCBTZW50ZW5jZVBpZWNlIHRyZWF0cyB0aGUgaW5wdXQgYXMgYSByYXcgVW5pY29kZSBieXRlIHN0cmVhbeKAlHdoaXRlc3BhY2UgaXMganVzdCBhbm90aGVyIGNoYXJhY3Rlci4gV29yZHMgYXJlIG5vdCBhc3N1bWVkIHRvIGJlIHNlcGFyYXRlZCBieSBzcGFjZXMsIG1ha2luZyB0aGUgdG9rZW5pemVyIHN1aXRhYmxlIGZvciBDaGluZXNlLCBKYXBhbmVzZSwgVGhhaSwgYW5kIG90aGVyIGxhbmd1YWdlcyB3aXRob3V0IHNwYWNlLWRlbGltaXRlZCB3b3Jkcy4gU2VudGVuY2VQaWVjZSBzdXBwb3J0cyB0d28gYWxnb3JpdGhtczogQlBFIG1vZGUgKGlkZW50aWNhbCBpbiBwcmluY2lwbGUgdG8gR1BULTIgQlBFKSBhbmQgVW5pZ3JhbSBMYW5ndWFnZSBNb2RlbCBtb2RlLiBUaGUgVW5pZ3JhbSBMTSBtb2RlIGlzIHRoZSBkZWZhdWx0IGZvciBtb3N0IG1vZGVybiBtb2RlbHM7IGl0IHByb2R1Y2VzIGEgcHJvYmFiaWxpc3RpYyB2b2NhYnVsYXJ5IGFuZCBzdXBwb3J0cyBzdWJ3b3JkIHJlZ3VsYXJpemF0aW9uIGR1cmluZyB0cmFpbmluZ+KAlHNhbXBsaW5nIG11bHRpcGxlIHZhbGlkIHRva2VuaXphdGlvbnMgb2YgdGhlIHNhbWUgdGV4dCB0byBpbXByb3ZlIG1vZGVsIHJvYnVzdG5lc3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW50cm9kdWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZW50ZW5jZVBpZWNlXHUwMDI3cyBzZWxmLWNvbnRhaW5lZCAubW9kZWwgZmlsZSBlbmNvZGVzIHRoZSBmdWxsIHZvY2FidWxhcnksIGFsZ29yaXRobSwgYW5kIHNwZWNpYWwgdG9rZW4gY29uZmlndXJhdGlvbiwgbWFraW5nIHRva2VuaXphdGlvbiBkZXRlcm1pbmlzdGljIGFuZCBwb3J0YWJsZSBhY3Jvc3MgZnJhbWV3b3JrcyBhbmQgbGFuZ3VhZ2VzLiBUaGUgXyBwcmVmaXggKFUrMjU4MSBMT1dFUiBPTkUgRUlHSFRIIEJMT0NLKSBtYXJrcyB0aGUgYmVnaW5uaW5nIG9mIGEgd29yZCBpbiBwbGFjZSBvZiBHUFQtMlx1MDAyN3MgR8yHIGJ5dGUtbGV2ZWwgc3BhY2UgZW5jb2RpbmcuIEEgc2VxdWVuY2UgbGlrZSBcdTAwMjfiloFoZWxsb+KWgXdvcmxkXHUwMDI3IHRva2VuaXplZCBhcyBbXHUwMDI34paBaGVsbG9cdTAwMjcsIFx1MDAyN+KWgXdvcmxkXHUwMDI3XSBwcmVzZXJ2ZXMgdGhlIGxlYWRpbmctc3BhY2UgaW5mb3JtYXRpb24gbmVlZGVkIHRvIHJlY29uc3RydWN0IHRoZSBvcmlnaW5hbCB0ZXh0LiBMTGFNQS0xIHVzZXMgYSAzMksgU2VudGVuY2VQaWVjZSBVbmlncmFtIHZvY2FidWxhcnk7IExMYU1BLTMgc3dpdGNoZWQgdG8gdGlrdG9rZW4gQlBFIGF0IDEyOEsgdG9rZW5zOyBHZW1tYSByZXRhaW5zIFNlbnRlbmNlUGllY2Ugd2l0aCAyNTZLIHZvY2FidWxhcnkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmF3IFVuaWNvZGUgUHJvY2Vzc2luZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVjYXVzZSBTZW50ZW5jZVBpZWNlIHByb2Nlc3NlcyByYXcgVW5pY29kZSB3aXRob3V0IHByZS10b2tlbml6YXRpb24sIGEgc3BhY2UgYXQgcG9zaXRpb24gaSBpcyB0cmVhdGVkIGlkZW50aWNhbGx5IHRvIGFueSBvdGhlciBjaGFyYWN0ZXIuIFRoaXMgbWVhbnMgXHUwMDI3aGVsbG8gd29ybGRcdTAwMjcgYW5kIFx1MDAyN2hlbGxvd29ybGRcdTAwMjcgcHJvZHVjZSBkaWZmZXJlbnQgdG9rZW4gc2VxdWVuY2VzLCBhbmQgdGhlIHRva2VuaXplciBjYW4gbGVhcm4gdGhhdCBcdTAwMjfiloFcdTAwMjcgKHNwYWNlKSBpcyBhIG1lYW5pbmdmdWwgYm91bmRhcnkgc2lnbmFsIHdpdGhvdXQgYmVpbmcgZXhwbGljaXRseSBwcm9ncmFtbWVkIHRvIHNwbGl0IG9uIHdoaXRlc3BhY2UuIFNlbnRlbmNlUGllY2Ugbm9ybWFsaXNlcyBpbnB1dCB1c2luZyBVbmljb2RlIE5GS0MgYnkgZGVmYXVsdCwgd2hpY2ggbWFwcyBjb21wYXRpYmlsaXR5IGNoYXJhY3RlcnMgdG8gdGhlaXIgY2Fub25pY2FsIGZvcm1zIChlLmcuLCBmdWxsLXdpZHRoIGRpZ2l0cyB0byBBU0NJSSBkaWdpdHMpLiBUaGlzIG5vcm1hbGlzYXRpb24gY2FuIGJlIGRpc2FibGVkIHdpdGggbm9ybWFsaXphdGlvbl9ydWxlX25hbWU9XHUwMDI3aWRlbnRpdHlcdTAwMjcgd2hlbiB0aGUgbW9kZWwgbXVzdCBoYW5kbGUgcmF3IHRleHQgZXhhY3RseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHNlbnRlbmNlcGllY2UgYXMgc3BtXG5pbXBvcnQgb3MsIHRlbXBmaWxlXG5cbiMgQnVpbGQgYSBzbWFsbCB0cmFpbmluZyBjb3JwdXNcbmxpbmVzID0gW1xuICAgIFx1MDAyN1RoZSBxdWljayBicm93biBmb3gganVtcHMgb3ZlciB0aGUgbGF6eSBkb2cuXHUwMDI3LFxuICAgIFx1MDAyN05hdHVyYWwgbGFuZ3VhZ2UgcHJvY2Vzc2luZyBlbmFibGVzIG1hY2hpbmVzIHRvIHVuZGVyc3RhbmQgdGV4dC5cdTAwMjcsXG4gICAgXHUwMDI3U3Vid29yZCB0b2tlbml6YXRpb24gYmFsYW5jZXMgdm9jYWJ1bGFyeSBzaXplIGFuZCBzZXF1ZW5jZSBsZW5ndGguXHUwMDI3LFxuICAgIFx1MDAyN0J5dGUtcGFpciBlbmNvZGluZyBhbmQgdW5pZ3JhbSBtb2RlbHMgYXJlIHRoZSB0d28gbWFpbiBhbGdvcml0aG1zLlx1MDAyNyxcbiAgICBcdTAwMjdTZW50ZW5jZVBpZWNlIHByb2Nlc3NlcyByYXcgVW5pY29kZSB3aXRob3V0IHdoaXRlc3BhY2UgcHJlLXNwbGl0dGluZy5cdTAwMjcsXG5dICogNjAgICMgcmVwZWF0IHRvIHByb2R1Y2UgZW5vdWdoIHRyYWluaW5nIGRhdGFcblxud2l0aCB0ZW1wZmlsZS5OYW1lZFRlbXBvcmFyeUZpbGUobW9kZT1cdTAwMjd3XHUwMDI3LCBzdWZmaXg9XHUwMDI3LnR4dFx1MDAyNywgZGVsZXRlPUZhbHNlLCBlbmNvZGluZz1cdTAwMjd1dGYtOFx1MDAyNykgYXMgZjpcbiAgICBmLndyaXRlKFx1MDAyN1xcblx1MDAyNy5qb2luKGxpbmVzKSlcbiAgICBjb3JwdXNfZmlsZSA9IGYubmFtZVxuXG5tb2RlbF9wcmVmaXggPSB0ZW1wZmlsZS5ta3RlbXAoKVxuc3BtLlNlbnRlbmNlUGllY2VUcmFpbmVyLnRyYWluKFxuICAgIGlucHV0PWNvcnB1c19maWxlLFxuICAgIG1vZGVsX3ByZWZpeD1tb2RlbF9wcmVmaXgsXG4gICAgdm9jYWJfc2l6ZT0zMDAsXG4gICAgbW9kZWxfdHlwZT1cdTAwMjd1bmlncmFtXHUwMDI3LFxuICAgIGNoYXJhY3Rlcl9jb3ZlcmFnZT0wLjk5OTUsXG4gICAgcGFkX2lkPTAsIHVua19pZD0xLCBib3NfaWQ9MiwgZW9zX2lkPTMsXG4pXG5zcCA9IHNwbS5TZW50ZW5jZVBpZWNlUHJvY2Vzc29yKG1vZGVsX2ZpbGU9bW9kZWxfcHJlZml4ICsgXHUwMDI3Lm1vZGVsXHUwMDI3KVxuXG50ZXN0ID0gXHUwMDI3VGhlIHF1aWNrIGJyb3duIGZveFx1MDAyN1xucHJpbnQoZlx1MDAyN1RleHQgICA6IHt0ZXN0fVx1MDAyNylcbnByaW50KGZcdTAwMjdUb2tlbnMgOiB7c3AuZW5jb2RlKHRlc3QsIG91dF90eXBlPXN0cil9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0lEcyAgICA6IHtzcC5lbmNvZGUodGVzdCwgb3V0X3R5cGU9aW50KX1cdTAwMjcpXG5wcmludChmXHUwMDI3Vm9jYWIgc2l6ZToge3NwLmdldF9waWVjZV9zaXplKCl9XHUwMDI3KVxucHJpbnQoXHUwMDI3XFxuVG9wIDE1IHZvY2FidWxhcnkgcGllY2VzOlx1MDAyNylcbmZvciBpIGluIHJhbmdlKDE1KTpcbiAgICBwcmludChmXHUwMDI3ICBbe2k6M2R9XSB7c3AuaWRfdG9fcGllY2UoaSkhcjpcdTAwM2MyMH0gc2NvcmU9e3NwLmdldF9zY29yZShpKTouNGZ9XHUwMDI3KVxub3MudW5saW5rKGNvcnB1c19maWxlKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuaWdyYW0gTGFuZ3VhZ2UgTW9kZWwgQWxnb3JpdGhtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgVW5pZ3JhbSBMTSB0b2tlbml6ZXIgYXNzaWducyBhIGxvZy1wcm9iYWJpbGl0eSBzY29yZSBwKHQpIHRvIGVhY2ggdG9rZW4gdCBpbiB0aGUgdm9jYWJ1bGFyeS4gVGhlIHByb2JhYmlsaXR5IG9mIGEgc2VnbWVudGF0aW9uICh04oKBLCB04oKCLCDigKYsIHRfaykgb2YgYSB3b3JkIGlzIHAodOKCgSkgw5cgcCh04oKCKSDDlyDigKYgw5cgcCh0X2spLiBUaGUgY29ycHVzIGxvZy1saWtlbGlob29kIGlzIHRoZSBzdW0gb2YgbG9nIHAoYmVzdCBzZWdtZW50YXRpb24pIG92ZXIgYWxsIHdvcmRzLiBUcmFpbmluZyBzdGFydHMgd2l0aCBhIGxhcmdlIGluaXRpYWwgdm9jYWJ1bGFyeSAo4oi8M8OXIHRoZSB0YXJnZXQgc2l6ZSwgYnVpbHQgZnJvbSBmcmVxdWVudCBzdWJzdHJpbmdzKSwgdGhlbiBpdGVyYXRpdmVseSBwcnVuZXMgaXQuIEF0IGVhY2ggRU0gaXRlcmF0aW9uOiAoMSkgRS1zdGVwOiB1c2UgdGhlIFZpdGVyYmkgYWxnb3JpdGhtIHRvIGZpbmQgdGhlIGJlc3Qgc2VnbWVudGF0aW9uIG9mIGVhY2ggd29yZCBnaXZlbiB0aGUgY3VycmVudCBwcm9iYWJpbGl0aWVzOyAoMikgTS1zdGVwOiB1cGRhdGUgdG9rZW4gcHJvYmFiaWxpdGllcyB1c2luZyB0aGUgc2VnbWVudGF0aW9uIGNvdW50czsgKDMpIHBydW5lIHRva2VucyB3aG9zZSByZW1vdmFsIGRlY3JlYXNlcyBjb3JwdXMgbG9nLWxpa2VsaWhvb2QgbGVhc3QsIHR5cGljYWxseSByZW1vdmluZyAxMOKAkzIwJSBvZiB0b2tlbnMgcGVyIHJvdW5kLiBSZXBlYXQgdW50aWwgdGhlIHZvY2FidWxhcnkgcmVhY2hlcyB0aGUgdGFyZ2V0IHNpemUgVi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG1hdGhcblxuZGVmIHZpdGVyYmlfc2VnbWVudCh3b3JkLCB1bmlncmFtX2xvZ19wcm9icywgbWF4X3BpZWNlX2xlbj04KTpcbiAgICBcIlwiXCJWaXRlcmJpIGJlc3QtcGF0aCBzZWdtZW50YXRpb24gZ2l2ZW4gdW5pZ3JhbSBsb2ctcHJvYmFiaWxpdGllcy5cIlwiXCJcbiAgICBuID0gbGVuKHdvcmQpXG4gICAgYmVzdCA9IFstbWF0aC5pbmZdICogKG4gKyAxKVxuICAgIGJhY2sgPSBbTm9uZV0gKiAobiArIDEpXG4gICAgYmVzdFswXSA9IDAuMFxuICAgIGZvciBpIGluIHJhbmdlKDEsIG4gKyAxKTpcbiAgICAgICAgZm9yIGogaW4gcmFuZ2UobWF4KDAsIGkgLSBtYXhfcGllY2VfbGVuKSwgaSk6XG4gICAgICAgICAgICBwaWVjZSA9IHdvcmRbajppXVxuICAgICAgICAgICAgbHAgPSB1bmlncmFtX2xvZ19wcm9icy5nZXQocGllY2UsIC1tYXRoLmluZilcbiAgICAgICAgICAgIHNjb3JlID0gYmVzdFtqXSArIGxwXG4gICAgICAgICAgICBpZiBzY29yZSBcdTAwM2UgYmVzdFtpXTpcbiAgICAgICAgICAgICAgICBiZXN0W2ldID0gc2NvcmVcbiAgICAgICAgICAgICAgICBiYWNrW2ldID0galxuICAgIGlmIGJlc3Rbbl0gPT0gLW1hdGguaW5mOlxuICAgICAgICByZXR1cm4gW3dvcmRdICAjIGZhbGxiYWNrOiB1bmtub3duIHdvcmRcbiAgICB0b2tlbnMsIGkgPSBbXSwgblxuICAgIHdoaWxlIGkgXHUwMDNlIDA6XG4gICAgICAgIGogPSBiYWNrW2ldXG4gICAgICAgIHRva2Vucy5hcHBlbmQod29yZFtqOmldKVxuICAgICAgICBpID0galxuICAgIHJldHVybiBsaXN0KHJldmVyc2VkKHRva2VucykpXG5cbiMgU21hbGwgZXhhbXBsZSB1bmlncmFtIHZvY2FidWxhcnkgd2l0aCBsb2ctcHJvYmFiaWxpdGllc1xudW5pZ3JhbV9scCA9IHtcbiAgICBcdTAwMjdsb3dcdTAwMjc6IG1hdGgubG9nKDAuMTApLCBcdTAwMjdlclx1MDAyNzogbWF0aC5sb2coMC4wOCksIFx1MDAyN2VzdFx1MDAyNzogbWF0aC5sb2coMC4wNyksXG4gICAgXHUwMDI3bmV3XHUwMDI3OiBtYXRoLmxvZygwLjA5KSwgXHUwMDI3d2lkZVx1MDAyNzogbWF0aC5sb2coMC4wNiksIFx1MDAyN3J1blx1MDAyNzogbWF0aC5sb2coMC4wOCksXG4gICAgXHUwMDI3bG9cdTAwMjc6IG1hdGgubG9nKDAuMDMpLCBcdTAwMjd3XHUwMDI3OiBtYXRoLmxvZygwLjAyKSwgXHUwMDI3clx1MDAyNzogbWF0aC5sb2coMC4wNCksXG4gICAgXHUwMDI3blx1MDAyNzogbWF0aC5sb2coMC4wMiksIFx1MDAyN2VcdTAwMjc6IG1hdGgubG9nKDAuMDUpLCBcdTAwMjdzXHUwMDI3OiBtYXRoLmxvZygwLjAzKSxcbiAgICBcdTAwMjd0XHUwMDI3OiBtYXRoLmxvZygwLjAzKSwgXHUwMDI3aVx1MDAyNzogbWF0aC5sb2coMC4wMiksIFx1MDAyN2RcdTAwMjc6IG1hdGgubG9nKDAuMDIpLFxufVxud29yZHMgPSBbXHUwMDI3bG93ZXJcdTAwMjcsIFx1MDAyN25ld2VzdFx1MDAyNywgXHUwMDI3d2lkZXJcdTAwMjcsIFx1MDAyN3J1bm5lclx1MDAyNywgXHUwMDI3bG93ZXN0XHUwMDI3XVxucHJpbnQoZlx1MDAyN3tcIldvcmRcIjpcdTAwM2MxMn0ge1wiVml0ZXJiaSBTZWdtZW50YXRpb25cIn1cdTAwMjcpXG5mb3IgdyBpbiB3b3JkczpcbiAgICBzZWdzID0gdml0ZXJiaV9zZWdtZW50KHcsIHVuaWdyYW1fbHApXG4gICAgcHJpbnQoZlx1MDAyN3t3Olx1MDAzYzEyfSB7c2Vnc31cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRU0gVHJhaW5pbmcgYW5kIFBydW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVNIHRyYWluaW5nIGFsdGVybmF0ZXMgYmV0d2VlbiBjb21wdXRpbmcgdGhlIGJlc3QgKG9yIGV4cGVjdGVkKSBzZWdtZW50YXRpb24gb2YgdGhlIGNvcnB1cyAoRS1zdGVwKSBhbmQgcmUtZXN0aW1hdGluZyB0b2tlbiBsb2ctcHJvYmFiaWxpdGllcyBmcm9tIHNlZ21lbnRhdGlvbiBjb3VudHMgKE0tc3RlcCkuIFRvIHBydW5lLCBlYWNoIHRva2VuIHQgaXMgcmVtb3ZlZCBmcm9tIHRoZSB2b2NhYnVsYXJ5IGFuZCB0aGUgbG9zcyBpbiBjb3JwdXMgbG9nLWxpa2VsaWhvb2QgaXMgY29tcHV0ZWQ6IHRva2VucyB3aXRoIHRoZSBzbWFsbGVzdCBsb3NzIGltcGFjdCBhcmUgcHJ1bmVkLiBBIHBydW5pbmcgcmF0ZSBvZiAxMOKAkzIwJSBwZXIgcm91bmQgbWVhbnMgdGhhdCBmcm9tIGFuIGluaXRpYWwgdm9jYWJ1bGFyeSBvZiAxMDBLLCByZWFjaGluZyBhIHRhcmdldCBvZiAzMksgdGFrZXMgcm91Z2hseSA14oCTOCByb3VuZHMgb2YgRU0gKyBwcnVuaW5nLiBVbmxpa2UgQlBFICh3aGljaCBhZGRzIHRva2VucyBvbmUgYnkgb25lKSwgdGhlIFVuaWdyYW0gTE0gYXBwcm9hY2ggd29ya3MgdG9wLWRvd24gYnkgcmVtb3ZpbmcgdG9rZW5zLCBnaXZpbmcgaXQgbW9yZSBnbG9iYWwgY29udHJvbCBvdmVyIHRoZSBmaW5hbCB2b2NhYnVsYXJ5IGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCeXRlIEZhbGxiYWNrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZW50ZW5jZVBpZWNlXHUwMDI3cyBieXRlIGZhbGxiYWNrIGZlYXR1cmUgaGFuZGxlcyBjaGFyYWN0ZXJzIG5vdCBjb3ZlcmVkIGJ5IHRoZSB2b2NhYnVsYXJ5OiBhbnkgY2hhcmFjdGVyIHRoYXQgY2Fubm90IGJlIHRva2VuaXplZCBpcyBzcGxpdCBpbnRvIGl0cyBVVEYtOCBieXRlcywgZWFjaCBlbmNvZGVkIGFzIGEgc3BlY2lhbCB0b2tlbiBpbiB0aGUgZm9ybSBcdTAwM2MweEhIXHUwMDNlIHdoZXJlIEhIIGlzIHRoZSBoZXggYnl0ZSB2YWx1ZS4gVGhpcyBndWFyYW50ZWVzIHRoYXQgZXZlbiByYXJlIENKSyBjaGFyYWN0ZXJzLCBlbW9qaSwgb3IgdW51c3VhbCBVbmljb2RlIGNhbiBiZSBlbmNvZGVkIHdpdGhvdXQgW1VOS10uIExMYU1BLTFcdTAwMjdzIHRva2VuaXplciBoYXMgMjU2IHJlc2VydmVkIGJ5dGUgZmFsbGJhY2sgdG9rZW5zIChcdTAwM2MweDAwXHUwMDNlIHRocm91Z2ggXHUwMDNjMHhGRlx1MDAzZSkuIFRoZSBieXRlIGZhbGxiYWNrIHZvY2FidWxhcnkgc2xvdHMgY29zdCBvbmx5IDI1NiBlbnRyaWVzIGJ1dCBlbmFibGUgY29tcGxldGUgVW5pY29kZSBjb3ZlcmFnZS4gQnl0ZSB0b2tlbnMgaGF2ZSB2ZXJ5IGxvdyBwcm9iYWJpbGl0eSBzY29yZXMgYW5kIGFyZSBwcnVuZWQgbGFzdCBkdXJpbmcgVW5pZ3JhbSBMTSB0cmFpbmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBEZW1vbnN0cmF0ZSBieXRlIGZhbGxiYWNrIGVuY29kaW5nIGZvciByYXJlIFVuaWNvZGUgY2hhcmFjdGVyc1xuIyAod2l0aG91dCByZXF1aXJpbmcgYSB0cmFpbmVkIG1vZGVsKVxuXG5kZWYgdXRmOF9ieXRlX3Rva2VucyhjaGFyKTpcbiAgICBcIlwiXCJSZXR1cm4gU2VudGVuY2VQaWVjZS1zdHlsZSBieXRlIGZhbGxiYWNrIHRva2VucyBmb3IgYSBjaGFyYWN0ZXIuXCJcIlwiXG4gICAgcmV0dXJuIFtmXHUwMDI3XHUwMDNjMHh7YjowMlh9XHUwMDNlXHUwMDI3IGZvciBiIGluIGNoYXIuZW5jb2RlKFx1MDAyN3V0Zi04XHUwMDI3KV1cblxucmFyZV9jaGFycyA9IFtcbiAgICAoXHUwMDI3XFxVMDAwMUY2MDBcdTAwMjcsIFx1MDAyN2Vtb2ppIChVKzFGNjAwKVx1MDAyNyksXG4gICAgKFx1MDAyN1xcdTRlMmRcdTAwMjcsICAgICBcdTAwMjdDSksgXFx1NGUyZCAoVSs0RTJEKVx1MDAyNyksXG4gICAgKFx1MDAyN1xcdTAzYjFcdTAwMjcsICAgICBcdTAwMjdHcmVlayBcXHUwM2IxIChVKzAzQjEpXHUwMDI3KSxcbiAgICAoXHUwMDI3XFx1MjE5Mlx1MDAyNywgICAgIFx1MDAyN0Fycm93IFxcdTIxOTIgKFUrMjE5MilcdTAwMjcpLFxuICAgIChcdTAwMjdcXHUwMGYxXHUwMDI3LCAgICAgXHUwMDI3TGF0aW4gXFx1MDBmMSAoVSswMEYxKVx1MDAyNyksXG4gICAgKFx1MDAyN1xcdTA0MzZcdTAwMjcsICAgICBcdTAwMjdDeXJpbGxpYyBcXHUwNDM2IChVKzA0MzYpXHUwMDI3KSxcbl1cbnByaW50KFx1MDAyN0J5dGUgZmFsbGJhY2sgZW5jb2RpbmcgZm9yIHJhcmUgVW5pY29kZSBjaGFyYWN0ZXJzOlx1MDAyNylcbnByaW50KGZcdTAwMjd7XCJDaGFyXCI6XHUwMDNjOH0ge1wiVW5pY29kZVwiOlx1MDAzYzIyfSB7XCJVVEYtOCBieXRlc1wiOlx1MDAzYzIwfSB7XCJGYWxsYmFjayB0b2tlbnNcIn1cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNzUpXG5mb3IgY2hhciwgbGFiZWwgaW4gcmFyZV9jaGFyczpcbiAgICB1dGY4ID0gbGlzdChjaGFyLmVuY29kZShcdTAwMjd1dGYtOFx1MDAyNykpXG4gICAgdG9rZW5zID0gdXRmOF9ieXRlX3Rva2VucyhjaGFyKVxuICAgIHByaW50KGZcdTAwMjd7cmVwcihjaGFyKTpcdTAwM2M4fSB7bGFiZWw6XHUwMDNjMjJ9IHtzdHIodXRmOCk6XHUwMDNjMjB9IHt0b2tlbnN9XHUwMDI3KVxuXG5wcmludChcdTAwMjdcXG5CeXRlIGZhbGxiYWNrIHVzZXMgMjU2IHJlc2VydmVkIHRva2VuIHNsb3RzIFx1MDAzYzB4MDBcdTAwM2UuLi5cdTAwM2MweEZGXHUwMDNlLlx1MDAyNylcbnByaW50KFx1MDAyN0FueSBVbmljb2RlIGNoYXJhY3RlciBkZWNvbXBvc2VzIGludG8gYXQgbW9zdCA0IGJ5dGUgdG9rZW5zLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdWJ3b3JkIFJlZ3VsYXJpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEdXJpbmcgdHJhaW5pbmcsIHN1YndvcmQgcmVndWxhcml6YXRpb24gc2FtcGxlcyBmcm9tIHRoZSBkaXN0cmlidXRpb24gb2YgdmFsaWQgdG9rZW5pemF0aW9ucyByYXRoZXIgdGhhbiBhbHdheXMgdXNpbmcgdGhlIFZpdGVyYmktYmVzdCBzZWdtZW50YXRpb24uIEZvciBhIHdvcmQgd2l0aCBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb24gb3ZlciB2YWxpZCB0b2tlbiBzZXF1ZW5jZXMsIHRoZSBFLXN0ZXAgY2FuIHNhbXBsZSBpbnN0ZWFkIG9mIHRha2luZyB0aGUgYXJnbWF4LCBleHBvc2luZyB0aGUgbW9kZWwgdG8gbXVsdGlwbGUgdmFsaWQgdG9rZW5pemF0aW9ucyBvZiB0aGUgc2FtZSB0ZXh0LiBBdCBpbmZlcmVuY2UgdGltZSwgdGhlIGJlc3QgKFZpdGVyYmkpIHRva2VuaXphdGlvbiBpcyB1c2VkLiBTdWJ3b3JkIHJlZ3VsYXJpemF0aW9uIGlzIGNvbnRyb2xsZWQgYnkgdHdvIHBhcmFtZXRlcnM6IG5iZXN0X3NpemUgKG51bWJlciBvZiBjYW5kaWRhdGUgdG9rZW5pemF0aW9ucyB0byBzYW1wbGUgZnJvbTsgLTEgPSBmdWxsIGxhdHRpY2UpIGFuZCBhbHBoYSAoZmxhdG5lc3Mgb2YgdGhlIHNhbXBsaW5nIGRpc3RyaWJ1dGlvbjsgMCA9IHVuaWZvcm0sIDEgPSBwcm9wb3J0aW9uYWwgdG8gcHJvYmFiaWxpdHkpLiBJdCBhY3RzIGFzIGEgZGF0YSBhdWdtZW50YXRpb24gdGVjaG5pcXVlIHRoYXQgaW1wcm92ZXMgcm9idXN0bmVzcyB0byB0b2tlbml6YXRpb24gYXJ0aWZhY3RzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgc2VudGVuY2VwaWVjZSBhcyBzcG1cblxuIyBSZXVzZSBtb2RlbCB0cmFpbmVkIGluIHRoZSBmaXJzdCBjb2RlIGJsb2NrXG5zcCA9IHNwbS5TZW50ZW5jZVBpZWNlUHJvY2Vzc29yKG1vZGVsX2ZpbGU9bW9kZWxfcHJlZml4ICsgXHUwMDI3Lm1vZGVsXHUwMDI3KVxuXG50ZXh0ID0gXHUwMDI3bmF0dXJhbCBsYW5ndWFnZSBwcm9jZXNzaW5nXHUwMDI3XG5wcmludChmXHUwMDI3VGV4dDoge3JlcHIodGV4dCl9XHUwMDI3KVxucHJpbnQoKVxuXG4jIERldGVybWluaXN0aWMgYmVzdCBzZWdtZW50YXRpb25cbmJlc3QgPSBzcC5lbmNvZGUodGV4dCwgb3V0X3R5cGU9c3RyKVxucHJpbnQoZlx1MDAyN0Jlc3QgKFZpdGVyYmkpOiB7YmVzdH1cdTAwMjcpXG5wcmludCgpXG5cbiMgU2FtcGxlIG11bHRpcGxlIHRva2VuaXphdGlvbnMgKHN1YndvcmQgcmVndWxhcml6YXRpb24pXG5wcmludChcdTAwMjdTYW1wbGVkIHRva2VuaXphdGlvbnMgKG5iZXN0X3NpemU9LTEsIGFscGhhPTAuMSk6XHUwMDI3KVxuc2VlbiA9IHNldCgpXG5mb3IgXyBpbiByYW5nZSg1MCk6XG4gICAgc2FtcGxlZCA9IHNwLnNhbXBsZV9lbmNvZGUodGV4dCwgLTEsIDAuMSwgb3V0X3R5cGU9c3RyKVxuICAgIGtleSA9IFx1MDAyN3xcdTAwMjcuam9pbihzYW1wbGVkKVxuICAgIGlmIGtleSBub3QgaW4gc2VlbjpcbiAgICAgICAgc2Vlbi5hZGQoa2V5KVxuICAgICAgICBwcmludChmXHUwMDI3ICB7c2FtcGxlZH1cdTAwMjcpXG4gICAgaWYgbGVuKHNlZW4pIFx1MDAzZT0gNjpcbiAgICAgICAgYnJlYWtcblxucHJpbnQoKVxucHJpbnQoZlx1MDAyN1VuaXF1ZSBzZWdtZW50YXRpb25zIGZvdW5kOiB7bGVuKHNlZW4pfVx1MDAyNylcbnByaW50KFx1MDAyN1VzZSBzYW1wbGVfZW5jb2RlIGR1cmluZyB0cmFpbmluZyB0byBleHBvc2UgbW9kZWwgdG8gdG9rZW5pemF0aW9uIHZhcmlhbnRzLlx1MDAyNylcbnByaW50KFx1MDAyN0F0IGluZmVyZW5jZSBhbHdheXMgdXNlIGVuY29kZSAoVml0ZXJiaS1iZXN0KSBmb3IgZGV0ZXJtaW5pc3RpYyBvdXRwdXQuXHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJTdWJ3b3JkIFJlZ3VsYXJpemF0aW9uIGZvciBUcmFpbmluZyBSb2J1c3RuZXNzIiwiY29udGVudCI6IlVuaWdyYW0gTE0gdG9rZW5pemVyIHN1cHBvcnRzIHN1YndvcmQgcmVndWxhcml6YXRpb24gKHNhbXBsZV9lbmNvZGUgd2l0aCBuYmVzdF9zaXplPS0xKSBkdXJpbmcgdHJhaW5pbmcg4oCUIHRoaXMgZXhwb3NlcyB0aGUgbW9kZWwgdG8gbXVsdGlwbGUgdmFsaWQgdG9rZW5pemF0aW9ucyBvZiB0aGUgc2FtZSB0ZXh0LCBpbXByb3Zpbmcgcm9idXN0bmVzcyB0byB0b2tlbml6YXRpb24gYXJ0aWZhY3RzIGF0IGluZmVyZW5jZS4gSW4gcHJhY3RpY2UsIHVzZSBhbHBoYT0wLjHigJMwLjIgKGxvdyBhbHBoYSA9IG5lYXItYmVzdCBzZWdtZW50YXRpb247IGhpZ2ggYWxwaGEgPSB1bmlmb3JtIHJhbmRvbSkuIEFsd2F5cyBzd2l0Y2ggdG8gZGV0ZXJtaW5pc3RpYyBWaXRlcmJpIGVuY29kaW5nIChzcC5lbmNvZGUpIGF0IGluZmVyZW5jZSB0aW1lIHRvIGVuc3VyZSBjb25zaXN0ZW50IHRva2VuIHNlcXVlbmNlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgVXNhZ2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxvYWQgYSBTZW50ZW5jZVBpZWNlIG1vZGVsIGluIFB5dGhvbiB3aXRoIHNlbnRlbmNlcGllY2UuU2VudGVuY2VQaWVjZVByb2Nlc3Nvcihtb2RlbF9maWxlPVx1MDAyN3BhdGgubW9kZWxcdTAwMjcpLiBUaGUgLm1vZGVsIGJpbmFyeSBmaWxlIGlzIGZ1bGx5IHNlbGYtY29udGFpbmVkOiBubyBhZGRpdGlvbmFsIHZvY2FidWxhcnkgZmlsZXMgYXJlIG5lZWRlZC4gSHVnZ2luZ0ZhY2Ugd3JhcHMgU2VudGVuY2VQaWVjZSBiZWhpbmQgdGhlIExsYW1hVG9rZW5pemVyIGFuZCBUNVRva2VuaXplciBjbGFzc2VzLCB3aGljaCBhZGQgc3BlY2lhbCB0b2tlbiBoYW5kbGluZyBhbmQgdGhlIEh1Z2dpbmdGYWNlIHRva2VuaXplciBBUEkuIFdoZW4gd29ya2luZyB3aXRoIExMYU1BLTIsIHRoZSBCT1MgdG9rZW4gKElEIDEpIG11c3QgYmUgcHJlcGVuZGVkIG1hbnVhbGx5IGlmIHVzaW5nIHRoZSByYXcgU2VudGVuY2VQaWVjZSBBUEksIGFzIHRoZSBtb2RlbCBleHBlY3RzIGl0OyBIdWdnaW5nRmFjZVx1MDAyN3MgTGxhbWFUb2tlbml6ZXIgYWRkcyBpdCBhdXRvbWF0aWNhbGx5IHZpYSBhZGRfc3BlY2lhbF90b2tlbnM9VHJ1ZS4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJCUEUgTW9kZSIsIlVuaWdyYW0gTE0gTW9kZSJdLCJyb3dzIjpbWyJUcmFpbmluZyBkaXJlY3Rpb24iLCJCb3R0b20tdXA6IG1lcmdlIGNoYXJhY3RlcnMiLCJUb3AtZG93bjogcHJ1bmUgZnJvbSBsYXJnZSB2b2NhYiJdLFsiTWVyZ2UgY3JpdGVyaW9uIiwiSGlnaGVzdCBmcmVxdWVuY3kgY291bnQiLCJMb3dlc3QgbG9nLWxpa2VsaWhvb2QgbG9zcyBvbiByZW1vdmFsIl0sWyJTZWdtZW50YXRpb24iLCJEZXRlcm1pbmlzdGljIChtZXJnZSBvcmRlcikiLCJQcm9iYWJpbGlzdGljIChWaXRlcmJpLWJlc3Qgb3Igc2FtcGxlZCkiXSxbIkhhbmRsZXMgcmFyZSBjaGFycyIsIkJ5dGUtbGV2ZWwgQlBFIG9ubHkiLCJZZXMsIHZpYSBieXRlIGZhbGxiYWNrIHRva2VucyJdLFsiVm9jYWJ1bGFyeSBjb250cm9sIiwiRXhhY3QgKG9uZSBzbG90IHBlciBtZXJnZSkiLCJBcHByb3hpbWF0ZSAocHJ1bmluZyByYXRlKSJdLFsiU3Vid29yZCByZWd1bGFyaXphdGlvbiIsIk5vIG5hdGl2ZSBzdXBwb3J0IiwiWWVzOiBzYW1wbGVfZW5jb2RlIEFQSSJdLFsiVXNlZCBieSIsIkdQVC0yLzMvNCwgUm9CRVJUYSIsIlQ1LCBtVDUsIExMYU1BLTEvMiwgR2VtbWEsIE1pc3RyYWwiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNlbnRlbmNlUGllY2UgdHJlYXRzIHdoaXRlc3BhY2UgYXMgYSByZWd1bGFyIGNoYXJhY3RlciAobWFya2VkIHdpdGgg4paBKSwgZW5hYmxpbmcgbGFuZ3VhZ2UtYWdub3N0aWMgdG9rZW5pemF0aW9uIHdpdGhvdXQgcHJlLXNwbGl0dGluZy4iLCJVbmlncmFtIExNIHRyYWluaW5nIHN0YXJ0cyB3aXRoIGEgbGFyZ2Ugdm9jYWJ1bGFyeSBhbmQgcHJ1bmVzIGl0ZXJhdGl2ZWx5IHVzaW5nIEVNOyB1bmxpa2UgQlBFIGl0IG9wZXJhdGVzIHRvcC1kb3duLiIsIlZpdGVyYmkgZGVjb2RpbmcgZmluZHMgdGhlIHNlZ21lbnRhdGlvbiB0aGF0IG1heGltaXNlcyB0aGUgcHJvZHVjdCBvZiB1bmlncmFtIHRva2VuIHByb2JhYmlsaXRpZXMuIiwiQnl0ZSBmYWxsYmFjayBlbmNvZGVzIGFueSBVbmljb2RlIGNoYXJhY3RlciB2aWEgaXRzIFVURi04IGJ5dGVzIGFzIFx1MDAzYzB4SEhcdTAwM2UgdG9rZW5zLCBndWFyYW50ZWVpbmcgemVybyBPT1Ygd2l0aCBvbmx5IDI1NiBleHRyYSBzbG90cy4iLCJTdWJ3b3JkIHJlZ3VsYXJpemF0aW9uIChzYW1wbGVfZW5jb2RlKSBzYW1wbGVzIGZyb20gdGhlIHRva2VuaXphdGlvbiBkaXN0cmlidXRpb24gZHVyaW5nIHRyYWluaW5nLCBpbXByb3ZpbmcgbW9kZWwgcm9idXN0bmVzcy4iLCJUaGUgLm1vZGVsIGZpbGUgaXMgc2VsZi1jb250YWluZWQ7IHRoZSAudm9jYWIgZmlsZSBpcyBvcHRpb25hbCBtZXRhZGF0YS4gU2hpcCBvbmx5IHRoZSAubW9kZWwgZmlsZSBmb3IgaW5mZXJlbmNlLiIsIkxMYU1BLTEvMiB1c2UgYSAzMksgU2VudGVuY2VQaWVjZSB2b2NhYnVsYXJ5OyBHZW1tYSB1c2VzIDI1NksuIExhcmdlciB2b2NhYnVsYXJ5IHJlZHVjZXMgZmVydGlsaXR5IGJ1dCByZXF1aXJlcyBtb3JlIGVtYmVkZGluZyBwYXJhbWV0ZXJzLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# SentencePiece — Unigram Language Model Tokenizer and Byte Fallback

SentencePiece is a language-independent tokenizer used by LLaMA, Gemma, Mistral, T5, and ALBERT. Unlike BPE implementations that first split text on whitespace, SentencePiece treats the input as a raw Unicode byte stream—whitespace is just another character. Words are not assumed to be separated by spaces, making the tokenizer suitable for Chinese, Japanese, Thai, and other languages without space-delimited words. SentencePiece supports two algorithms: BPE mode (identical in principle to GPT-2 BPE) and Unigram Language Model mode. The Unigram LM mode is the default for most modern models; it produces a probabilistic vocabulary and supports subword regularization during training—sampling multiple valid tokenizations of the same text to improve model robustness.

## Introduction

SentencePiece's self-contained .model file encodes the full vocabulary, algorithm, and special token configuration, making tokenization deterministic and portable across frameworks and languages. The _ prefix (U+2581 LOWER ONE EIGHTH BLOCK) marks the beginning of a word in place of GPT-2's Ġ byte-level space encoding. A sequence like '▁hello▁world' tokenized as ['▁hello', '▁world'] preserves the leading-space information needed to reconstruct the original text. LLaMA-1 uses a 32K SentencePiece Unigram vocabulary; LLaMA-3 switched to tiktoken BPE at 128K tokens; Gemma retains SentencePiece with 256K vocabulary.

## Raw Unicode Processing

Because SentencePiece processes raw Unicode without pre-tokenization, a space at position i is treated identically to any other character. This means 'hello world' and 'helloworld' produce different token sequences, and the tokenizer can learn that '▁' (space) is a meaningful boundary signal without being explicitly programmed to split on whitespace. SentencePiece normalises input using Unicode NFKC by default, which maps compatibility characters to their canonical forms (e.g., full-width digits to ASCII digits). This normalisation can be disabled with normalization_rule_name='identity' when the model must handle raw text exactly.

```python
import sentencepiece as spm
import os, tempfile

# Build a small training corpus
lines = [
    'The quick brown fox jumps over the lazy dog.',
    'Natural language processing enables machines to understand text.',
    'Subword tokenization balances vocabulary size and sequence length.',
    'Byte-pair encoding and unigram models are the two main algorithms.',
    'SentencePiece processes raw Unicode without whitespace pre-splitting.',
] * 60  # repeat to produce enough training data

with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
    f.write('\n'.join(lines))
    corpus_file = f.name

model_prefix = tempfile.mktemp()
spm.SentencePieceTrainer.train(
    input=corpus_file,
    model_prefix=model_prefix,
    vocab_size=300,
    model_type='unigram',
    character_coverage=0.9995,
    pad_id=0, unk_id=1, bos_id=2, eos_id=3,
)
sp = spm.SentencePieceProcessor(model_file=model_prefix + '.model')

test = 'The quick brown fox'
print(f'Text   : {test}')
print(f'Tokens : {sp.encode(test, out_type=str)}')
print(f'IDs    : {sp.encode(test, out_type=int)}')
print(f'Vocab size: {sp.get_piece_size()}')
print('\nTop 15 vocabulary pieces:')
for i in range(15):
    print(f'  [{i:3d}] {sp.id_to_piece(i)!r:<20} score={sp.get_score(i):.4f}')
os.unlink(corpus_file)
```

## Unigram Language Model Algorithm

The Unigram LM tokenizer assigns a log-probability score p(t) to each token t in the vocabulary. The probability of a segmentation (t₁, t₂, …, t_k) of a word is p(t₁) × p(t₂) × … × p(t_k). The corpus log-likelihood is the sum of log p(best segmentation) over all words. Training starts with a large initial vocabulary (∼3× the target size, built from frequent substrings), then iteratively prunes it. At each EM iteration: (1) E-step: use the Viterbi algorithm to find the best segmentation of each word given the current probabilities; (2) M-step: update token probabilities using the segmentation counts; (3) prune tokens whose removal decreases corpus log-likelihood least, typically removing 10–20% of tokens per round. Repeat until the vocabulary reaches the target size V.

```python
import math

def viterbi_segment(word, unigram_log_probs, max_piece_len=8):
    """Viterbi best-path segmentation given unigram log-probabilities."""
    n = len(word)
    best = [-math.inf] * (n + 1)
    back = [None] * (n + 1)
    best[0] = 0.0
    for i in range(1, n + 1):
        for j in range(max(0, i - max_piece_len), i):
            piece = word[j:i]
            lp = unigram_log_probs.get(piece, -math.inf)
            score = best[j] + lp
            if score > best[i]:
                best[i] = score
                back[i] = j
    if best[n] == -math.inf:
        return [word]  # fallback: unknown word
    tokens, i = [], n
    while i > 0:
        j = back[i]
        tokens.append(word[j:i])
        i = j
    return list(reversed(tokens))

# Small example unigram vocabulary with log-probabilities
unigram_lp = {
    'low': math.log(0.10), 'er': math.log(0.08), 'est': math.log(0.07),
    'new': math.log(0.09), 'wide': math.log(0.06), 'run': math.log(0.08),
    'lo': math.log(0.03), 'w': math.log(0.02), 'r': math.log(0.04),
    'n': math.log(0.02), 'e': math.log(0.05), 's': math.log(0.03),
    't': math.log(0.03), 'i': math.log(0.02), 'd': math.log(0.02),
}
words = ['lower', 'newest', 'wider', 'runner', 'lowest']
print(f'{"Word":<12} {"Viterbi Segmentation"}')
for w in words:
    segs = viterbi_segment(w, unigram_lp)
    print(f'{w:<12} {segs}')
```

## EM Training and Pruning

EM training alternates between computing the best (or expected) segmentation of the corpus (E-step) and re-estimating token log-probabilities from segmentation counts (M-step). To prune, each token t is removed from the vocabulary and the loss in corpus log-likelihood is computed: tokens with the smallest loss impact are pruned. A pruning rate of 10–20% per round means that from an initial vocabulary of 100K, reaching a target of 32K takes roughly 5–8 rounds of EM + pruning. Unlike BPE (which adds tokens one by one), the Unigram LM approach works top-down by removing tokens, giving it more global control over the final vocabulary distribution.

## Byte Fallback

SentencePiece's byte fallback feature handles characters not covered by the vocabulary: any character that cannot be tokenized is split into its UTF-8 bytes, each encoded as a special token in the form <0xHH> where HH is the hex byte value. This guarantees that even rare CJK characters, emoji, or unusual Unicode can be encoded without [UNK]. LLaMA-1's tokenizer has 256 reserved byte fallback tokens (<0x00> through <0xFF>). The byte fallback vocabulary slots cost only 256 entries but enable complete Unicode coverage. Byte tokens have very low probability scores and are pruned last during Unigram LM training.

```python
# Demonstrate byte fallback encoding for rare Unicode characters
# (without requiring a trained model)

def utf8_byte_tokens(char):
    """Return SentencePiece-style byte fallback tokens for a character."""
    return [f'<0x{b:02X}>' for b in char.encode('utf-8')]

rare_chars = [
    ('\U0001F600', 'emoji (U+1F600)'),
    ('\u4e2d',     'CJK \u4e2d (U+4E2D)'),
    ('\u03b1',     'Greek \u03b1 (U+03B1)'),
    ('\u2192',     'Arrow \u2192 (U+2192)'),
    ('\u00f1',     'Latin \u00f1 (U+00F1)'),
    ('\u0436',     'Cyrillic \u0436 (U+0436)'),
]
print('Byte fallback encoding for rare Unicode characters:')
print(f'{"Char":<8} {"Unicode":<22} {"UTF-8 bytes":<20} {"Fallback tokens"}')
print('-' * 75)
for char, label in rare_chars:
    utf8 = list(char.encode('utf-8'))
    tokens = utf8_byte_tokens(char)
    print(f'{repr(char):<8} {label:<22} {str(utf8):<20} {tokens}')

print('\nByte fallback uses 256 reserved token slots <0x00>...<0xFF>.')
print('Any Unicode character decomposes into at most 4 byte tokens.')
```

## Subword Regularization

During training, subword regularization samples from the distribution of valid tokenizations rather than always using the Viterbi-best segmentation. For a word with probability distribution over valid token sequences, the E-step can sample instead of taking the argmax, exposing the model to multiple valid tokenizations of the same text. At inference time, the best (Viterbi) tokenization is used. Subword regularization is controlled by two parameters: nbest_size (number of candidate tokenizations to sample from; -1 = full lattice) and alpha (flatness of the sampling distribution; 0 = uniform, 1 = proportional to probability). It acts as a data augmentation technique that improves robustness to tokenization artifacts.

```python
import sentencepiece as spm

# Reuse model trained in the first code block
sp = spm.SentencePieceProcessor(model_file=model_prefix + '.model')

text = 'natural language processing'
print(f'Text: {repr(text)}')
print()

# Deterministic best segmentation
best = sp.encode(text, out_type=str)
print(f'Best (Viterbi): {best}')
print()

# Sample multiple tokenizations (subword regularization)
print('Sampled tokenizations (nbest_size=-1, alpha=0.1):')
seen = set()
for _ in range(50):
    sampled = sp.sample_encode(text, -1, 0.1, out_type=str)
    key = '|'.join(sampled)
    if key not in seen:
        seen.add(key)
        print(f'  {sampled}')
    if len(seen) >= 6:
        break

print()
print(f'Unique segmentations found: {len(seen)}')
print('Use sample_encode during training to expose model to tokenization variants.')
print('At inference always use encode (Viterbi-best) for deterministic output.')
```

> **Subword Regularization for Training Robustness**: Unigram LM tokenizer supports subword regularization (sample_encode with nbest_size=-1) during training — this exposes the model to multiple valid tokenizations of the same text, improving robustness to tokenization artifacts at inference. In practice, use alpha=0.1–0.2 (low alpha = near-best segmentation; high alpha = uniform random). Always switch to deterministic Viterbi encoding (sp.encode) at inference time to ensure consistent token sequences.

## Practical Usage

Load a SentencePiece model in Python with sentencepiece.SentencePieceProcessor(model_file='path.model'). The .model binary file is fully self-contained: no additional vocabulary files are needed. HuggingFace wraps SentencePiece behind the LlamaTokenizer and T5Tokenizer classes, which add special token handling and the HuggingFace tokenizer API. When working with LLaMA-2, the BOS token (ID 1) must be prepended manually if using the raw SentencePiece API, as the model expects it; HuggingFace's LlamaTokenizer adds it automatically via add_special_tokens=True.

| Property | BPE Mode | Unigram LM Mode |
| --- | --- | --- |
| Training direction | Bottom-up: merge characters | Top-down: prune from large vocab |
| Merge criterion | Highest frequency count | Lowest log-likelihood loss on removal |
| Segmentation | Deterministic (merge order) | Probabilistic (Viterbi-best or sampled) |
| Handles rare chars | Byte-level BPE only | Yes, via byte fallback tokens |
| Vocabulary control | Exact (one slot per merge) | Approximate (pruning rate) |
| Subword regularization | No native support | Yes: sample_encode API |
| Used by | GPT-2/3/4, RoBERTa | T5, mT5, LLaMA-1/2, Gemma, Mistral |

## Key Takeaways

- SentencePiece treats whitespace as a regular character (marked with ▁), enabling language-agnostic tokenization without pre-splitting.
- Unigram LM training starts with a large vocabulary and prunes iteratively using EM; unlike BPE it operates top-down.
- Viterbi decoding finds the segmentation that maximises the product of unigram token probabilities.
- Byte fallback encodes any Unicode character via its UTF-8 bytes as <0xHH> tokens, guaranteeing zero OOV with only 256 extra slots.
- Subword regularization (sample_encode) samples from the tokenization distribution during training, improving model robustness.
- The .model file is self-contained; the .vocab file is optional metadata. Ship only the .model file for inference.
- LLaMA-1/2 use a 32K SentencePiece vocabulary; Gemma uses 256K. Larger vocabulary reduces fertility but requires more embedding parameters.

---

