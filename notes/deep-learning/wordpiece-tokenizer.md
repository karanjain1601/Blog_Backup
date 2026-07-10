---
title: "WordPiece — BERT’s Likelihood-Based Subword Tokenizer"
slug: "wordpiece-tokenizer"
description: "How WordPiece builds BERT's vocabulary using a likelihood-based merge criterion, the ## continuation marker, special tokens, cased vs uncased variants, fast Rust tokenizers, and token alignment for span tasks."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiV29yZFBpZWNlIGlzIHRoZSB0b2tlbml6YXRpb24gYWxnb3JpdGhtIHVzZWQgYnkgQkVSVCwgRGlzdGlsQkVSVCwgRUxFQ1RSQSwgYW5kIG90aGVyIGVuY29kZXItb25seSBtb2RlbHMuIExpa2UgQlBFLCBpdCBzdGFydHMgZnJvbSBhIGNoYXJhY3RlciB2b2NhYnVsYXJ5IGFuZCBpdGVyYXRpdmVseSBtZXJnZXMgcGFpcnMsIGJ1dCBpdCB1c2VzIGEgZGlmZmVyZW50IG1lcmdlIGNyaXRlcmlvbjogaW5zdGVhZCBvZiBzZWxlY3RpbmcgdGhlIHBhaXIgd2l0aCB0aGUgaGlnaGVzdCByYXcgZnJlcXVlbmN5IGNvdW50LCBXb3JkUGllY2Ugc2VsZWN0cyB0aGUgcGFpciB0aGF0IG1heGltaXNlcyB0aGUgbGlrZWxpaG9vZCByYXRpbyBwKGFiKSAvIFtwKGEpIMOXIHAoYildLiBUaGlzIGxpa2VsaWhvb2QtYmFzZWQgY3JpdGVyaW9uIGZhdm91cnMgbWVyZ2VzIHRoYXQgcmVkdWNlIHRoZSBjb3JwdXMgcGVycGxleGl0eSBtb3N04oCUaXQgd2lsbCBwcmVmZXIgdG8gbWVyZ2UgcmFyZSBwYWlycyB0aGF0IGFsbW9zdCBhbHdheXMgYXBwZWFyIHRvZ2V0aGVyIG92ZXIgZnJlcXVlbnQgcGFpcnMgdGhhdCBlYWNoIG9jY3VyIGluZGVwZW5kZW50bHkuIFRoZSByZXN1bHRpbmcgdm9jYWJ1bGFyeSB1c2VzIGEgIyMgcHJlZml4ICh0d28gaGFzaCBzeW1ib2xzKSBmb3IgY29udGludWF0aW9uIHN1YndvcmRz4oCUdG9rZW5zIHRoYXQgYXBwZWFyIG1pZC13b3JkIHJhdGhlciB0aGFuIGF0IHRoZSBzdGFydC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnRyb2R1Y3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJFUlQtYmFzZSB1c2VzIGEgMzAsNTIyLXRva2VuIFdvcmRQaWVjZSB2b2NhYnVsYXJ5LiBUaGUgZml4ZWQgdm9jYWJ1bGFyeSB3YXMgYnVpbHQgb24gdGhlIEJvb2tzQ29ycHVzICsgRW5nbGlzaCBXaWtpcGVkaWEgdHJhaW5pbmcgY29ycHVzIGFuZCBpcyBzaGFyZWQgYWNyb3NzIGFsbCBCRVJUIGNoZWNrcG9pbnRzIG9mIHRoZSBzYW1lIGxhbmd1YWdlIGFuZCBjYXNlIGNvbmZpZ3VyYXRpb24uIFNwZWNpYWwgdG9rZW5zIFtQQURdPTAsIFtVTktdPTEwMCwgW0NMU109MTAxLCBbU0VQXT0xMDIsIFtNQVNLXT0xMDMgYXJlIHJlc2VydmVkIGF0IGZpeGVkIElEcy4gVGhlICMjIHByZWZpeCBkaXN0aW5ndWlzaGVzIGNvbnRpbnVhdGlvbiBzdWJ3b3JkcyBmcm9tIHdvcmQtc3RhcnQgc3Vid29yZHM6IFx1MDAyN3J1bm5pbmdcdTAwMjcgaXMgdG9rZW5pemVkIGFzIFtcdTAwMjdydW5uaW5nXHUwMDI3XSBpZiBpdCBpcyBhIHNpbmdsZSB0b2tlbiwgb3IgW1x1MDAyN3J1blx1MDAyNywgXHUwMDI3IyNuaW5nXHUwMDI3XSBpZiBzcGxpdC4gVGhpcyBleHBsaWNpdCBtYXJraW5nIGFsbG93cyB0aGUgbW9kZWwgdG8gbGVhcm4gbW9ycGhvbG9naWNhbCBwYXR0ZXJuczogIyNpbmcsICMjZWQsICMjZXIsICMjbHkgYXBwZWFyIGluIHRoZSB2b2NhYnVsYXJ5IGFzIGRpc3RpbmN0IHRva2VucywgZ2l2aW5nIFdvcmRQaWVjZSBhbiBleHBsaWNpdCByZXByZXNlbnRhdGlvbiBvZiBzdWZmaXhlcyB0aGF0IEJQRSBsYWNrcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaWtlbGlob29kLUJhc2VkIE1lcmdlIENyaXRlcmlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFdvcmRQaWVjZSBzY29yZSBmb3IgbWVyZ2luZyB0b2tlbnMgYSBhbmQgYiBpczogc2NvcmUoYSwgYikgPSBmcmVxKGFiKSAvIFtmcmVxKGEpIMOXIGZyZXEoYildLiBUaGlzIGlzIHByb3BvcnRpb25hbCB0byB0aGUgcG9pbnR3aXNlIG11dHVhbCBpbmZvcm1hdGlvbiAoUE1JKSBvZiB0aGUgcGFpci4gQSBwYWlyIHdpdGggc2NvcmUgXHUwMDNlXHUwMDNlIDEgYWxtb3N0IGFsd2F5cyBjby1vY2N1cnPigJRtZXJnaW5nIGl0IHJlZHVjZXMgZGVzY3JpcHRpb24gbGVuZ3RoIHNpZ25pZmljYW50bHkuIEEgcGFpciB3aXRoIHNjb3JlIOKJiCAxIG9jY3VycyBhdCBjaGFuY2XigJRtZXJnaW5nIGl0IGRvZXNuXHUwMDI3dCBoZWxwLiBDb250cmFzdCB3aXRoIEJQRSB3aGljaCB1c2VzIHJhdyBjb3VudCBmcmVxKGFiKTogQlBFIHdvdWxkIHByZWZlciBcdTAwMjd0aFx1MDAyNyAodmVyeSBmcmVxdWVudCBwYWlyKSBvdmVyIFx1MDAyN3F1XHUwMDI3IChuZWFybHkgYWx3YXlzIHBhaXJlZCksIHdoaWxlIFdvcmRQaWVjZSB3b3VsZCBzY29yZSBcdTAwMjdxdVx1MDAyNyBoaWdoZXIgYmVjYXVzZSBmcmVxKHEpIGlzIGxvdyBhbmQgcSBhbG1vc3QgYWx3YXlzIHByZWNlZGVzIHUuIFRoZSBsaWtlbGlob29kIGNyaXRlcmlvbiBwcm9kdWNlcyBhIG1vcmUgc2VtYW50aWNhbGx5IGNvaGVyZW50IHZvY2FidWxhcnkgZm9yIG1vcnBob2xvZ2ljYWxseSByaWNoIHRleHQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXJcblxuZGVmIGNvbXB1dGVfd3Bfc2NvcmUocGFpcl9mcmVxLCB0b2tfZnJlcSk6XG4gICAgXCJcIlwiV29yZFBpZWNlIGxpa2VsaWhvb2Qgc2NvcmU6IGZyZXEoYWIpIC8gKGZyZXEoYSkgKiBmcmVxKGIpKS5cIlwiXCJcbiAgICBhLCBiID0gcGFpcl9mcmVxXG4gICAgZmEgPSB0b2tfZnJlcS5nZXQoYSwgMSlcbiAgICBmYiA9IHRva19mcmVxLmdldChiLCAxKVxuICAgIHJldHVybiBwYWlyX2ZyZXEgLyAoZmEgKiBmYikgaWYgZmEgKiBmYiBcdTAwM2UgMCBlbHNlIDAuMFxuXG5kZWYgYnVpbGRfd29yZHBpZWNlX3ZvY2FiKGNvcnB1cywgbnVtX21lcmdlcyk6XG4gICAgd29yZHMgPSBjb3JwdXMubG93ZXIoKS5zcGxpdCgpXG4gICAgd29yZF9mcmVxID0gQ291bnRlcih3b3JkcylcbiAgICAjIEluaXRpYWwgdm9jYWI6IGZpcnN0IGNoYXIgaXMgYmFyZSwgcmVzdCBnZXQgIyMgcHJlZml4XG4gICAgdm9jYWIgPSB7fVxuICAgIHRva19mcmVxID0gQ291bnRlcigpXG4gICAgZm9yIHcsIGZyZXEgaW4gd29yZF9mcmVxLml0ZW1zKCk6XG4gICAgICAgIGNoYXJzID0gW3dbMF1dICsgW1x1MDAyNyMjXHUwMDI3ICsgYyBmb3IgYyBpbiB3WzE6XV1cbiAgICAgICAga2V5ID0gXHUwMDI3IFx1MDAyNy5qb2luKGNoYXJzKVxuICAgICAgICB2b2NhYltrZXldID0gZnJlcVxuICAgICAgICBmb3IgY2ggaW4gY2hhcnM6XG4gICAgICAgICAgICB0b2tfZnJlcVtjaF0gKz0gZnJlcVxuXG4gICAgZm9yIG1lcmdlX3N0ZXAgaW4gcmFuZ2UobnVtX21lcmdlcyk6XG4gICAgICAgIHBhaXJfY291bnRzID0gQ291bnRlcigpXG4gICAgICAgIGZvciB3b3JkLCBmcmVxIGluIHZvY2FiLml0ZW1zKCk6XG4gICAgICAgICAgICBzeW1zID0gd29yZC5zcGxpdCgpXG4gICAgICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4oc3ltcykgLSAxKTpcbiAgICAgICAgICAgICAgICBwYWlyX2NvdW50c1soc3ltc1tpXSwgc3ltc1tpKzFdKV0gKz0gZnJlcVxuICAgICAgICBpZiBub3QgcGFpcl9jb3VudHM6XG4gICAgICAgICAgICBicmVha1xuICAgICAgICAjIFdvcmRQaWVjZTogc2NvcmUgYnkgbGlrZWxpaG9vZCByYXRpbywgbm90IHJhdyBjb3VudFxuICAgICAgICBiZXN0ID0gbWF4KHBhaXJfY291bnRzLCBrZXk9bGFtYmRhIHA6IHBhaXJfY291bnRzW3BdIC8gKHRva19mcmVxW3BbMF1dICogdG9rX2ZyZXFbcFsxXV0gKyAxZS05KSlcbiAgICAgICAgc2NvcmUgPSBwYWlyX2NvdW50c1tiZXN0XSAvICh0b2tfZnJlcVtiZXN0WzBdXSAqIHRva19mcmVxW2Jlc3RbMV1dICsgMWUtOSlcbiAgICAgICAgbWVyZ2VkID0gYmVzdFswXSArIGJlc3RbMV0ubHN0cmlwKFx1MDAyNyNcdTAwMjcpXG4gICAgICAgICMgVXBkYXRlIHZvY2FiXG4gICAgICAgIGltcG9ydCByZVxuICAgICAgICBwYXQgPSByZS5jb21waWxlKHJcdTAwMjcoP1x1MDAzYyFcXFMpXHUwMDI3ICsgcmUuZXNjYXBlKGJlc3RbMF0gKyBcdTAwMjcgXHUwMDI3ICsgYmVzdFsxXSkgKyByXHUwMDI3KD8hXFxTKVx1MDAyNylcbiAgICAgICAgdm9jYWIgPSB7cGF0LnN1YihtZXJnZWQsIHcpOiBmIGZvciB3LCBmIGluIHZvY2FiLml0ZW1zKCl9XG4gICAgICAgIHRva19mcmVxW21lcmdlZF0gKz0gcGFpcl9jb3VudHNbYmVzdF1cbiAgICAgICAgcHJpbnQoZlx1MDAyNyAgU3RlcCB7bWVyZ2Vfc3RlcCsxOjJkfToge2Jlc3RbMF19ICsge2Jlc3RbMV19IC1cdTAwM2Uge21lcmdlZH0gKHNjb3JlPXtzY29yZTouNWZ9KVx1MDAyNylcblxuY29ycHVzID0gXHUwMDI3cGxheWluZyBwbGF5ZWQgcGxheXMgcGxheWVyIGxvd2VyIGxvd2VzdCBydW5uaW5nIHJ1bm5lciBydW5zIHF1aWNrbHkgcXVpY2tcdTAwMjdcbnByaW50KFx1MDAyN1dvcmRQaWVjZSBsaWtlbGlob29kLWJhc2VkIG1lcmdlcyAodnMgQlBFIGNvdW50LWJhc2VkKTpcdTAwMjcpXG5idWlsZF93b3JkcGllY2Vfdm9jYWIoY29ycHVzLCBudW1fbWVyZ2VzPTEwKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZvY2FidWxhcnkgQ29uc3RydWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCRVJUXHUwMDI3cyAzMEsgdm9jYWJ1bGFyeSB3YXMgYnVpbHQgYnkgcnVubmluZyBXb3JkUGllY2Ugb24gYSBsYXJnZSBFbmdsaXNoIGNvcnB1cyB3aXRoIHRhcmdldCBzaXplIDMwLDUyMi4gVGhlIHZvY2FidWxhcnkgaW5jbHVkZXM6IHNpbmdsZSBjaGFyYWN0ZXJzIChh4oCTeiwgQeKAk1osIDDigJM5LCBwdW5jdHVhdGlvbiksIGNvbW1vbiB3aG9sZSB3b3JkcywgYW5kIGEgbGFyZ2Ugc2V0IG9mICMjIGNvbnRpbnVhdGlvbiBzdWJ3b3JkcyBjb3ZlcmluZyBjb21tb24gc3VmZml4ZXMgKCMjaW5nLCAjI2VkLCAjI2VyLCAjI2x5LCAjI3Rpb24sICMjYWwpLiBDYXNlZCBCRVJUIHByZXNlcnZlcyBjYXNlIGFuZCBhY2NlbnQgbWFya3M7IHVuY2FzZWQgQkVSVCBsb3dlcmNhc2VzIGFsbCB0ZXh0IGFuZCBzdHJpcHMgYWNjZW50IGNoYXJhY3RlcnMgKGUuZy4sIMOpIOKGkiBlKSBiZWZvcmUgdG9rZW5pemF0aW9uLiBUaGUgdW5jYXNlZCB2b2NhYnVsYXJ5IGlzIHNtYWxsZXIgYmVjYXVzZSBsb3dlcmNhc2UgbGV0dGVycyBjb3ZlciBtb3JlIHRleHQuIE91dC1vZi12b2NhYnVsYXJ5IGNoYXJhY3RlcnMgKHRob3NlIG5vdCBpbiB0aGUgaW5pdGlhbCBjaGFyYWN0ZXIgdm9jYWJ1bGFyeSkgY2F1c2UgdGhlIGVudGlyZSB3b3JkIHRvIGJlIHRva2VuaXplZCBhcyBbVU5LXeKAlHVubGlrZSBCUEUgd2hpY2ggYWx3YXlzIGhhcyBhIGJ5dGUgZmFsbGJhY2suIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiB3b3JkcGllY2VfZW5jb2RlKHdvcmQsIHZvY2FiX3NldCwgdW5rX3Rva2VuPVx1MDAyN1tVTktdXHUwMDI3KTpcbiAgICBcIlwiXCJHcmVlZHkgbG9uZ2VzdC1tYXRjaCBXb3JkUGllY2UgZW5jb2Rpbmcgd2l0aCAjIyBwcmVmaXguXCJcIlwiXG4gICAgaWYgd29yZCBpbiB2b2NhYl9zZXQ6XG4gICAgICAgIHJldHVybiBbd29yZF1cbiAgICB0b2tlbnMgPSBbXVxuICAgIHN0YXJ0ID0gMFxuICAgIHdoaWxlIHN0YXJ0IFx1MDAzYyBsZW4od29yZCk6XG4gICAgICAgIGVuZCA9IGxlbih3b3JkKVxuICAgICAgICBjdXJfc3Vic3RyID0gTm9uZVxuICAgICAgICB3aGlsZSBzdGFydCBcdTAwM2MgZW5kOlxuICAgICAgICAgICAgc3Vic3RyID0gd29yZFtzdGFydDplbmRdXG4gICAgICAgICAgICBpZiBzdGFydCBcdTAwM2UgMDpcbiAgICAgICAgICAgICAgICBzdWJzdHIgPSBcdTAwMjcjI1x1MDAyNyArIHN1YnN0clxuICAgICAgICAgICAgaWYgc3Vic3RyIGluIHZvY2FiX3NldDpcbiAgICAgICAgICAgICAgICBjdXJfc3Vic3RyID0gc3Vic3RyXG4gICAgICAgICAgICAgICAgYnJlYWtcbiAgICAgICAgICAgIGVuZCAtPSAxXG4gICAgICAgIGlmIGN1cl9zdWJzdHIgaXMgTm9uZTpcbiAgICAgICAgICAgIHJldHVybiBbdW5rX3Rva2VuXSAgIyBlbnRpcmUgd29yZCAtXHUwMDNlIFtVTktdXG4gICAgICAgIHRva2Vucy5hcHBlbmQoY3VyX3N1YnN0cilcbiAgICAgICAgc3RhcnQgPSBlbmRcbiAgICByZXR1cm4gdG9rZW5zXG5cbiMgU2ltdWxhdGUgYSBzbWFsbCBXb3JkUGllY2Ugdm9jYWJ1bGFyeVxuc21hbGxfdm9jYWIgPSB7XG4gICAgXHUwMDI3cGxheVx1MDAyNywgXHUwMDI3IyNpbmdcdTAwMjcsIFx1MDAyNyMjZWRcdTAwMjcsIFx1MDAyNyMjZXJcdTAwMjcsIFx1MDAyNyMjc1x1MDAyNywgXHUwMDI3IyNseVx1MDAyNyxcbiAgICBcdTAwMjdydW5cdTAwMjcsIFx1MDAyN2xvd1x1MDAyNywgXHUwMDI3IyNlc3RcdTAwMjcsIFx1MDAyNyMjZXJcdTAwMjcsIFx1MDAyN3F1aWNrXHUwMDI3LCBcdTAwMjd0aGVcdTAwMjcsIFx1MDAyN2FcdTAwMjcsXG4gICAgXHUwMDI3cFx1MDAyNywgXHUwMDI3bFx1MDAyNywgXHUwMDI3YVx1MDAyNywgXHUwMDI3eVx1MDAyNywgXHUwMDI3clx1MDAyNywgXHUwMDI3dVx1MDAyNywgXHUwMDI3blx1MDAyNywgXHUwMDI3ZVx1MDAyNywgXHUwMDI3cVx1MDAyNywgXHUwMDI3aVx1MDAyNywgXHUwMDI3Y1x1MDAyNywgXHUwMDI3a1x1MDAyNyxcbiAgICBcdTAwMjdbVU5LXVx1MDAyNywgXHUwMDI3W0NMU11cdTAwMjcsIFx1MDAyN1tTRVBdXHUwMDI3LCBcdTAwMjdbUEFEXVx1MDAyNywgXHUwMDI3W01BU0tdXHUwMDI3LFxufVxudGVzdF93b3JkcyA9IFtcdTAwMjdwbGF5aW5nXHUwMDI3LCBcdTAwMjdwbGF5ZWRcdTAwMjcsIFx1MDAyN3BsYXllclx1MDAyNywgXHUwMDI3cnVubmluZ1x1MDAyNywgXHUwMDI3bG93ZXN0XHUwMDI3LCBcdTAwMjd6eXhcdTAwMjddXG5wcmludChmXHUwMDI3e1wiV29yZFwiOlx1MDAzYzEyfSB7XCJXb3JkUGllY2UgVG9rZW5zXCJ9XHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDQ1KVxuZm9yIHcgaW4gdGVzdF93b3JkczpcbiAgICB0b2tzID0gd29yZHBpZWNlX2VuY29kZSh3LCBzbWFsbF92b2NhYilcbiAgICBwcmludChmXHUwMDI3e3c6XHUwMDNjMTJ9IHt0b2tzfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTcGVjaWFsIFRva2VucyBhbmQgRm9ybWF0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkVSVCB1c2VzIGZvdXIgc3BlY2lhbCB0b2tlbnMgaW4gZXZlcnkgaW5wdXQ6IFtDTFNdIChJRCAxMDEpIHByZXBlbmRlZCB0byBldmVyeSBzZXF1ZW5jZSwgdXNlZCBhcyB0aGUgc2VxdWVuY2UgY2xhc3NpZmljYXRpb24gdG9rZW47IFtTRVBdIChJRCAxMDIpIGFwcGVuZGVkIGFmdGVyIGVhY2ggc2VudGVuY2U7IFtQQURdIChJRCAwKSBmb3IgcGFkZGluZyB0byB1bmlmb3JtIGxlbmd0aDsgW01BU0tdIChJRCAxMDMpIGZvciBtYXNrZWQgbGFuZ3VhZ2UgbW9kZWwgcHJlLXRyYWluaW5nLiBGb3Igc2VudGVuY2UgcGFpcnMgKGUuZy4sIE5MSSwgUUEpLCB0aGUgZm9ybWF0IGlzIFtDTFNdIHNlbnRlbmNlX0EgW1NFUF0gc2VudGVuY2VfQiBbU0VQXS4gVGhlIHRva2VuX3R5cGVfaWRzIHRlbnNvciBpbmRpY2F0ZXMgd2hpY2ggc2VudGVuY2UgZWFjaCB0b2tlbiBiZWxvbmdzIHRvOiAwIGZvciBzZW50ZW5jZSBBIChpbmNsdWRpbmcgW0NMU10gYW5kIGZpcnN0IFtTRVBdKSBhbmQgMSBmb3Igc2VudGVuY2UgQiAoaW5jbHVkaW5nIHNlY29uZCBbU0VQXSkuIFRoZSBhdHRlbnRpb25fbWFzayB0ZW5zb3IgbWFza3MgcGFkZGluZyB0b2tlbnMgZnJvbSBzZWxmLWF0dGVudGlvbjogMSBmb3IgcmVhbCB0b2tlbnMsIDAgZm9yIFtQQURdLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIlZhbHVlIC8gRGV0YWlsIl0sInJvd3MiOltbIkNvbnRpbnVhdGlvbiBtYXJrZXIiLCIjIyBwcmVmaXggb24gbWlkLXdvcmQgc3Vid29yZHMgKGUuZy4sICMjaW5nLCAjI2VkKSJdLFsiU3BlY2lhbCB0b2tlbnMiLCJbUEFEXT0wLCBbVU5LXT0xMDAsIFtDTFNdPTEwMSwgW1NFUF09MTAyLCBbTUFTS109MTAzIl0sWyJQcmUtdG9rZW5pemF0aW9uIiwiV2hpdGVzcGFjZSBzcGxpdCDihpIgcHVuY3R1YXRpb24gc3BsaXQg4oaSIFdvcmRQaWVjZSJdLFsiT09WIGhhbmRsaW5nIiwiQW55IGNoYXIgbm90IGluIGNoYXJhY3RlciB2b2NhYiDihpIgZW50aXJlIHdvcmQgYmVjb21lcyBbVU5LXSJdLFsiVm9jYWIgc2l6ZSAoQkVSVC1iYXNlKSIsIjMwLDUyMiB0b2tlbnMgKGNhc2VkIGFuZCB1bmNhc2VkIG1vZGVscykiXSxbIkNhc2UgaGFuZGxpbmciLCJDYXNlZDogcHJlc2VydmVzIGNhc2UgKyBhY2NlbnRzOyBVbmNhc2VkOiBsb3dlcmNhc2UgKyBhY2NlbnQgc3RyaXAiXSxbIkZhc3QgdG9rZW5pemVyIiwiUnVzdCBpbXBsZW1lbnRhdGlvbiB2aWEgSHVnZ2luZ0ZhY2UgdG9rZW5pemVycyBsaWJyYXJ5Il1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFbmNvZGluZyBNZWNoYW5pY3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJFUlRcdTAwMjdzIHRva2VuaXphdGlvbiBwaXBlbGluZSBoYXMgdGhyZWUgc3RhZ2VzOiAoMSkgd2hpdGVzcGFjZSB0b2tlbml6YXRpb24gc3BsaXRzIG9uIGFueSB3aGl0ZXNwYWNlIGNoYXJhY3RlcjsgKDIpIHB1bmN0dWF0aW9uIHRva2VuaXphdGlvbiBmdXJ0aGVyIHNwbGl0cyB0b2tlbnMgb24gcHVuY3R1YXRpb24gYm91bmRhcmllcyAoc28gXHUwMDI3ZW5kLlx1MDAyNyBiZWNvbWVzIFtcdTAwMjdlbmRcdTAwMjcsIFx1MDAyNy5cdTAwMjddKTsgKDMpIFdvcmRQaWVjZSB0b2tlbml6YXRpb24gYXBwbGllcyB0aGUgZ3JlZWR5IGxvbmdlc3QtbWF0Y2ggYWxnb3JpdGhtIHdpdGggIyMgcHJlZml4ZXMuIFRoZSBlbmNvZGVfcGx1cyBtZXRob2QgcmV0dXJucyBhIGRpY3Rpb25hcnkgd2l0aCBpbnB1dF9pZHMsIHRva2VuX3R5cGVfaWRzLCBhbmQgYXR0ZW50aW9uX21hc2suIFNldHRpbmcgcmV0dXJuX29mZnNldHNfbWFwcGluZz1UcnVlIGFkZHMgYSBtYXBwaW5nIGZyb20gZWFjaCB0b2tlbiBwb3NpdGlvbiB0byBpdHMgY2hhcmFjdGVyIHNwYW4gaW4gdGhlIG9yaWdpbmFsIHN0cmluZ+KAlGVzc2VudGlhbCBmb3IgTkVSIGFuZCBzcGFuIGV4dHJhY3Rpb24gdGFza3Mgd2hlcmUgdGhlIG1vZGVsIG11c3QgcHJlZGljdCBjaGFyYWN0ZXItbGV2ZWwgbGFiZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQmVydFRva2VuaXplckZhc3RcblxudG9rZW5pemVyID0gQmVydFRva2VuaXplckZhc3QuZnJvbV9wcmV0cmFpbmVkKFx1MDAyN2JlcnQtYmFzZS11bmNhc2VkXHUwMDI3KVxuXG4jIFNpbmdsZSBzZW50ZW5jZVxudGV4dCA9IFx1MDAyN1RoZSBxdWljayBicm93biBmb3gganVtcHMgb3ZlciB0aGUgbGF6eSBkb2cuXHUwMDI3XG5lbmMgPSB0b2tlbml6ZXIodGV4dCwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcsIHJldHVybl9vZmZzZXRzX21hcHBpbmc9VHJ1ZSlcbnByaW50KFx1MDAyN1NpbmdsZSBzZW50ZW5jZSBlbmNvZGluZzpcdTAwMjcpXG5wcmludChmXHUwMDI3ICBpbnB1dF9pZHMgICA6IHtlbmNbXCJpbnB1dF9pZHNcIl1bMF0udG9saXN0KCl9XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgdG9rZW5zICAgICAgOiB7dG9rZW5pemVyLmNvbnZlcnRfaWRzX3RvX3Rva2VucyhlbmNbXCJpbnB1dF9pZHNcIl1bMF0udG9saXN0KCkpfVx1MDAyNylcbnByaW50KGZcdTAwMjcgIGF0dG5fbWFzayAgIDoge2VuY1tcImF0dGVudGlvbl9tYXNrXCJdWzBdLnRvbGlzdCgpfVx1MDAyNylcbnByaW50KGZcdTAwMjcgIG9mZnNldHMgICAgIDoge2VuY1tcIm9mZnNldF9tYXBwaW5nXCJdWzBdLnRvbGlzdCgpfVx1MDAyNylcbnByaW50KClcblxuIyBTZW50ZW5jZSBwYWlyIChOTEkgZm9ybWF0KVxuc2VudEEgPSBcdTAwMjdUaGUgY2F0IHNhdCBvbiB0aGUgbWF0Llx1MDAyN1xuc2VudEIgPSBcdTAwMjdBIGZlbGluZSByZXN0ZWQgb24gYSBydWcuXHUwMDI3XG5lbmMyID0gdG9rZW5pemVyKHNlbnRBLCBzZW50QiwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcsIHBhZGRpbmc9VHJ1ZSwgdHJ1bmNhdGlvbj1UcnVlKVxucHJpbnQoXHUwMDI3U2VudGVuY2UgcGFpciBlbmNvZGluZzpcdTAwMjcpXG5wcmludChmXHUwMDI3ICB0b2tlbnMgICAgICA6IHt0b2tlbml6ZXIuY29udmVydF9pZHNfdG9fdG9rZW5zKGVuYzJbXCJpbnB1dF9pZHNcIl1bMF0udG9saXN0KCkpfVx1MDAyNylcbnByaW50KGZcdTAwMjcgIHR5cGVfaWRzICAgIDoge2VuYzJbXCJ0b2tlbl90eXBlX2lkc1wiXVswXS50b2xpc3QoKX1cdTAwMjcpXG5wcmludChmXHUwMDI3ICBGb3JtYXQ6IFtDTFNdIHNlbnRBIFtTRVBdIHNlbnRCIFtTRVBdXHUwMDI3KVxucHJpbnQoKVxucHJpbnQoZlx1MDAyN1ZvY2FiIHNpemU6IHt0b2tlbml6ZXIudm9jYWJfc2l6ZX1cdTAwMjcpXG5wcmludChmXHUwMDI3U3BlY2lhbCB0b2tlbnM6IHt0b2tlbml6ZXIuYWxsX3NwZWNpYWxfdG9rZW5zfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDYXNlZCB2cyBVbmNhc2VkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCRVJULWJhc2UtdW5jYXNlZCBsb3dlcmNhc2VzIGFsbCBpbnB1dCBhbmQgc3RyaXBzIFVuaWNvZGUgYWNjZW50IGNoYXJhY3RlcnMgYmVmb3JlIFdvcmRQaWVjZSB0b2tlbml6YXRpb246IFx1MDAyN8OJdHVkZVx1MDAyNyBiZWNvbWVzIFx1MDAyN2V0dWRlXHUwMDI3LiBUaGlzIHJlZHVjZXMgdm9jYWJ1bGFyeSBkaXZlcnNpdHkgYW5kIGltcHJvdmVzIGNvdmVyYWdlIG9mIGNvbW1vbiB3b3JkcywgYnV0IGxvc2VzIGNhc2UgYW5kIGRpYWNyaXRpYyBpbmZvcm1hdGlvbi4gQkVSVC1iYXNlLWNhc2VkIHByZXNlcnZlcyBjYXNlIGFuZCBhY2NlbnRzLCBtYWtpbmcgaXQgYmV0dGVyIGZvciB0YXNrcyB3aGVyZSBjYXNlIGNhcnJpZXMgc2VtYW50aWMgbWVhbmluZzogbmFtZWQgZW50aXR5IHJlY29nbml0aW9uIChkaWZmZXJlbnRpYXRpbmcgXHUwMDI3YXBwbGVcdTAwMjcgdGhlIGZydWl0IGZyb20gXHUwMDI3QXBwbGVcdTAwMjcgdGhlIGNvbXBhbnkpLCBhbmQgbGFuZ3VhZ2VzIHdoZXJlIGRpYWNyaXRpY3MgY2hhbmdlIHdvcmQgbWVhbmluZyAoRnJlbmNoLCBHZXJtYW4sIFNwYW5pc2gpLiBGb3IgbW9zdCBFbmdsaXNoIGNsYXNzaWZpY2F0aW9uIHRhc2tzLCB1bmNhc2VkIHBlcmZvcm1zIGNvbXBhcmFibHkgb3IgYmV0dGVyIGR1ZSB0byBpbXByb3ZlZCBnZW5lcmFsaXNhdGlvbiBhY3Jvc3MgY2FzZSB2YXJpYW50cy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkNvbnRpbnVhdGlvbiBNYXJrZXIgU2VtYW50aWNzIiwiY29udGVudCI6IldvcmRQaWVjZVx1MDAyN3MgIyMgY29udGludWF0aW9uIG1hcmtlciBtZWFucyB2b2NhYnVsYXJ5IHN0YXRpc3RpY3MgZGlmZmVyIGZyb20gQlBFIOKAlCBcdTAwMjdydW5uaW5nXHUwMDI3IGFuZCBcdTAwMjcjI3J1bm5pbmdcdTAwMjcgYXJlIGRpc3RpbmN0IHRva2Vucy4gVGhpcyBnaXZlcyBXb3JkUGllY2UgYW4gZXhwbGljaXQgcmVwcmVzZW50YXRpb24gb2YgbW9ycGhvbG9naWNhbCBzdWZmaXhlczogIyNpbmcsICMjZWQsICMjZXIsICMjbHksICMjdGlvbiBhcmUgYWxsIGhpZ2gtZnJlcXVlbmN5IHZvY2FidWxhcnkgZW50cmllcyBlbmNvZGluZyBzdWZmaXggc2VtYW50aWNzLiBCUEUgbWVyZ2VzIHRoZXNlIGludG8gdGhlIHByZWNlZGluZyBzdWJ3b3JkIHdpdGhvdXQgbWFya2luZyB0aGUgYm91bmRhcnksIHNvIFx1MDAyN3J1blx1MDAyNyBhbmQgXHUwMDI3cnVubmluZ1x1MDAyNyBzaGFyZSBubyBleHBsaWNpdCBzdWJ3b3JkLiBGb3IgbW9ycGhvbG9naWNhbGx5IHJpY2ggbGFuZ3VhZ2VzIChGaW5uaXNoLCBUdXJraXNoLCBIdW5nYXJpYW4pLCBXb3JkUGllY2VcdTAwMjdzIGV4cGxpY2l0IHN1ZmZpeCByZXByZXNlbnRhdGlvbiBjYW4gcHJvdmlkZSBjbGVhbmVyIG1vcnBob2xvZ2ljYWwgc2lnbmFsIHRvIHRoZSBtb2RlbC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUb2tlbiBBbGlnbm1lbnQgZm9yIFNwYW4gVGFza3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNwYW4tZXh0cmFjdGlvbiB0YXNrcyAoTkVSLCBRQSwgY29yZWZlcmVuY2UpIHJlcXVpcmUgbWFwcGluZyBtb2RlbCBwcmVkaWN0aW9ucyBmcm9tIHRva2VuIHNwYWNlIGJhY2sgdG8gY2hhcmFjdGVyIG9mZnNldHMgaW4gdGhlIG9yaWdpbmFsIHRleHQuIFRoZSBvZmZzZXRfbWFwcGluZyByZXR1cm4gdmFsdWUgcHJvdmlkZXMgZXhhY3RseSB0aGlzOiBlYWNoIHRva2VuIGdldHMgYSAoc3RhcnQsIGVuZCkgY2hhcmFjdGVyIHNwYW4uIFRva2VucyBzcGxpdCBieSBXb3JkUGllY2UgaGF2ZSBjb25zZWN1dGl2ZSBvdmVybGFwcGluZyBzcGFuczogXHUwMDI3cnVubmluZ1x1MDAyNyBzcGxpdCBhcyBbXHUwMDI3cnVuXHUwMDI3LCBcdTAwMjcjI25pbmdcdTAwMjddIGdldHMgb2Zmc2V0cyBbKDAsMyksICgzLDcpXS4gW0NMU10gYW5kIFtTRVBdIHNwZWNpYWwgdG9rZW5zIGdldCBvZmZzZXQgKDAsIDApLiBXaGVuIGFsaWduaW5nIGxhYmVscyBmb3IgTkVSIHRyYWluaW5nLCB1c2UgdGhlIHdvcmRfaWRzKCkgbWV0aG9kIHRvIGdldCB0aGUgd29yZCBpbmRleCBmb3IgZWFjaCB0b2tlbiwgdGhlbiBhc3NpZ24gdGhlIGxhYmVsIG9mIHRoZSBvcmlnaW5hbCB3b3JkIHRvIGl0cyBmaXJzdCBzdWJ3b3JkIChhbmQgYSBzcGVjaWFsIGlnbm9yZSBsYWJlbCwgdHlwaWNhbGx5IC0xMDAsIHRvIGFsbCBjb250aW51YXRpb24gc3Vid29yZHMpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG4jIENyb3NzLXRva2VuaXplciBjb21wYXJpc29uIG9uIHRoZSBzYW1lIHNlbnRlbmNlc1xuc2VudGVuY2VzID0gW1xuICAgIFx1MDAyN3J1bm5pbmcgcXVpY2tseVx1MDAyNyxcbiAgICBcdTAwMjd0b2tlbml6YXRpb24gc3BsaXRzIHRleHRcdTAwMjcsXG4gICAgXHUwMDI3c3VwZXJjYWxpZnJhZ2lsaXN0aWNcdTAwMjcsXG4gICAgXHUwMDI3dGhlIHF1aWNrIGJyb3duIGZveFx1MDAyNyxcbiAgICBcdTAwMjdHUFQtNCBvdXRwZXJmb3JtcyBlYXJsaWVyIG1vZGVsc1x1MDAyNyxcbl1cblxubW9kZWxzID0gW1xuICAgIChcdTAwMjdCUEUgKEdQVC0yKVx1MDAyNywgICAgICBcdTAwMjdncHQyXHUwMDI3KSxcbiAgICAoXHUwMDI3V29yZFBpZWNlIChCRVJUKVx1MDAyNywgXHUwMDI3YmVydC1iYXNlLXVuY2FzZWRcdTAwMjcpLFxuICAgIChcdTAwMjdVbmlncmFtIChUNSlcdTAwMjcsICAgICBcdTAwMjd0NS1zbWFsbFx1MDAyNyksXG5dXG5mb3IgbW9kZWxfbmFtZSwgbW9kZWxfaWQgaW4gbW9kZWxzOlxuICAgIHByaW50KGZcdTAwMjdcXG4tLS0ge21vZGVsX25hbWV9IC0tLVx1MDAyNylcbiAgICB0b2sgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9pZClcbiAgICBmb3Igc2VudCBpbiBzZW50ZW5jZXM6XG4gICAgICAgIHRva2VucyA9IHRvay50b2tlbml6ZShzZW50KVxuICAgICAgICBwcmludChmXHUwMDI3ICB7c2VudCFyOlx1MDAzYzM1fSAtXHUwMDNlIHtsZW4odG9rZW5zKToyZH0gdG9rZW5zOiB7dG9rZW5zfVx1MDAyNylcblxucHJpbnQoXHUwMDI3XFxuS2V5IGRpZmZlcmVuY2VzOlx1MDAyNylcbnByaW50KFx1MDAyNyAgQlBFIChHUFQtMikgIDogbm8gY29udGludWF0aW9uIG1hcmtlciwgc3BhY2UgZW5jb2RlZCBhcyBHLWRvdCBwcmVmaXhcdTAwMjcpXG5wcmludChcdTAwMjcgIFdvcmRQaWVjZSAgICA6ICMjIHByZWZpeCBmb3IgbWlkLXdvcmQgc3Vid29yZHMgKGV4cGxpY2l0IHN1ZmZpeCBtYXJraW5nKVx1MDAyNylcbnByaW50KFx1MDAyNyAgVW5pZ3JhbSAoVDUpIDogXyBwcmVmaXggZm9yIHdvcmQtc3RhcnQgc3Vid29yZHMgKGxpa2UgU2VudGVuY2VQaWVjZSlcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiV29yZFBpZWNlIHVzZXMgYSBsaWtlbGlob29kIHJhdGlvIG1lcmdlIGNyaXRlcmlvbiAoc2NvcmUgPSBmcmVxKGFiKSAvIFtmcmVxKGEpIMOXIGZyZXEoYildKSByYXRoZXIgdGhhbiBCUEVcdTAwMjdzIHJhdyBmcmVxdWVuY3kgY291bnQuIiwiVGhlICMjIHByZWZpeCBtYXJrcyBjb250aW51YXRpb24gc3Vid29yZHM6IFx1MDAyN3J1bm5pbmdcdTAwMjcg4oaSIFtcdTAwMjdydW5cdTAwMjcsIFx1MDAyNyMjbmluZ1x1MDAyN10gZ2l2ZXMgZXhwbGljaXQgbW9ycGhvbG9naWNhbCBzdWZmaXggcmVwcmVzZW50YXRpb24uIiwiQkVSVCB1c2VzIDMwLDUyMiB0b2tlbnMgd2l0aCBmaXhlZCBzcGVjaWFsIElEczogW1BBRF09MCwgW1VOS109MTAwLCBbQ0xTXT0xMDEsIFtTRVBdPTEwMiwgW01BU0tdPTEwMy4iLCJJbnB1dCBmb3JtYXQgZm9yIHNlbnRlbmNlIHBhaXJzOiBbQ0xTXSBzZW50QSBbU0VQXSBzZW50QiBbU0VQXTsgdG9rZW5fdHlwZV9pZHM9MCBmb3Igc2VudEEsIDEgZm9yIHNlbnRCLiIsIlVuY2FzZWQgQkVSVCBzdHJpcHMgYWNjZW50cyBhbmQgbG93ZXJjYXNlczsgY2FzZWQgQkVSVCBwcmVzZXJ2ZXMgY2FzZS4gVXNlIGNhc2VkIGZvciBORVIsIHVuY2FzZWQgZm9yIGNsYXNzaWZpY2F0aW9uLiIsIlVzZSBCZXJ0VG9rZW5pemVyRmFzdCAoUnVzdCBiYWNrZW5kKSBmb3IgcHJvZHVjdGlvbjsgaXQgaXMgMTDigJMxMDDDlyBmYXN0ZXIgYW5kIHN1cHBvcnRzIG9mZnNldF9tYXBwaW5nLiIsIkZvciBORVIvc3BhbiB0YXNrcywgdXNlIHdvcmRfaWRzKCkgdG8gYWxpZ24gV29yZFBpZWNlIHRva2VucyB0byBvcmlnaW5hbCB3b3JkczsgYXNzaWduIC0xMDAgdG8gY29udGludWF0aW9uIHN1YndvcmQgbGFiZWxzLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# WordPiece — BERT’s Likelihood-Based Subword Tokenizer

WordPiece is the tokenization algorithm used by BERT, DistilBERT, ELECTRA, and other encoder-only models. Like BPE, it starts from a character vocabulary and iteratively merges pairs, but it uses a different merge criterion: instead of selecting the pair with the highest raw frequency count, WordPiece selects the pair that maximises the likelihood ratio p(ab) / [p(a) × p(b)]. This likelihood-based criterion favours merges that reduce the corpus perplexity most—it will prefer to merge rare pairs that almost always appear together over frequent pairs that each occur independently. The resulting vocabulary uses a ## prefix (two hash symbols) for continuation subwords—tokens that appear mid-word rather than at the start.

## Introduction

BERT-base uses a 30,522-token WordPiece vocabulary. The fixed vocabulary was built on the BooksCorpus + English Wikipedia training corpus and is shared across all BERT checkpoints of the same language and case configuration. Special tokens [PAD]=0, [UNK]=100, [CLS]=101, [SEP]=102, [MASK]=103 are reserved at fixed IDs. The ## prefix distinguishes continuation subwords from word-start subwords: 'running' is tokenized as ['running'] if it is a single token, or ['run', '##ning'] if split. This explicit marking allows the model to learn morphological patterns: ##ing, ##ed, ##er, ##ly appear in the vocabulary as distinct tokens, giving WordPiece an explicit representation of suffixes that BPE lacks.

## Likelihood-Based Merge Criterion

The WordPiece score for merging tokens a and b is: score(a, b) = freq(ab) / [freq(a) × freq(b)]. This is proportional to the pointwise mutual information (PMI) of the pair. A pair with score >> 1 almost always co-occurs—merging it reduces description length significantly. A pair with score ≈ 1 occurs at chance—merging it doesn't help. Contrast with BPE which uses raw count freq(ab): BPE would prefer 'th' (very frequent pair) over 'qu' (nearly always paired), while WordPiece would score 'qu' higher because freq(q) is low and q almost always precedes u. The likelihood criterion produces a more semantically coherent vocabulary for morphologically rich text.

```python
from collections import Counter

def compute_wp_score(pair_freq, tok_freq):
    """WordPiece likelihood score: freq(ab) / (freq(a) * freq(b))."""
    a, b = pair_freq
    fa = tok_freq.get(a, 1)
    fb = tok_freq.get(b, 1)
    return pair_freq / (fa * fb) if fa * fb > 0 else 0.0

def build_wordpiece_vocab(corpus, num_merges):
    words = corpus.lower().split()
    word_freq = Counter(words)
    # Initial vocab: first char is bare, rest get ## prefix
    vocab = {}
    tok_freq = Counter()
    for w, freq in word_freq.items():
        chars = [w[0]] + ['##' + c for c in w[1:]]
        key = ' '.join(chars)
        vocab[key] = freq
        for ch in chars:
            tok_freq[ch] += freq

    for merge_step in range(num_merges):
        pair_counts = Counter()
        for word, freq in vocab.items():
            syms = word.split()
            for i in range(len(syms) - 1):
                pair_counts[(syms[i], syms[i+1])] += freq
        if not pair_counts:
            break
        # WordPiece: score by likelihood ratio, not raw count
        best = max(pair_counts, key=lambda p: pair_counts[p] / (tok_freq[p[0]] * tok_freq[p[1]] + 1e-9))
        score = pair_counts[best] / (tok_freq[best[0]] * tok_freq[best[1]] + 1e-9)
        merged = best[0] + best[1].lstrip('#')
        # Update vocab
        import re
        pat = re.compile(r'(?<!\S)' + re.escape(best[0] + ' ' + best[1]) + r'(?!\S)')
        vocab = {pat.sub(merged, w): f for w, f in vocab.items()}
        tok_freq[merged] += pair_counts[best]
        print(f'  Step {merge_step+1:2d}: {best[0]} + {best[1]} -> {merged} (score={score:.5f})')

corpus = 'playing played plays player lower lowest running runner runs quickly quick'
print('WordPiece likelihood-based merges (vs BPE count-based):')
build_wordpiece_vocab(corpus, num_merges=10)
```

## Vocabulary Construction

BERT's 30K vocabulary was built by running WordPiece on a large English corpus with target size 30,522. The vocabulary includes: single characters (a–z, A–Z, 0–9, punctuation), common whole words, and a large set of ## continuation subwords covering common suffixes (##ing, ##ed, ##er, ##ly, ##tion, ##al). Cased BERT preserves case and accent marks; uncased BERT lowercases all text and strips accent characters (e.g., é → e) before tokenization. The uncased vocabulary is smaller because lowercase letters cover more text. Out-of-vocabulary characters (those not in the initial character vocabulary) cause the entire word to be tokenized as [UNK]—unlike BPE which always has a byte fallback.

```python
def wordpiece_encode(word, vocab_set, unk_token='[UNK]'):
    """Greedy longest-match WordPiece encoding with ## prefix."""
    if word in vocab_set:
        return [word]
    tokens = []
    start = 0
    while start < len(word):
        end = len(word)
        cur_substr = None
        while start < end:
            substr = word[start:end]
            if start > 0:
                substr = '##' + substr
            if substr in vocab_set:
                cur_substr = substr
                break
            end -= 1
        if cur_substr is None:
            return [unk_token]  # entire word -> [UNK]
        tokens.append(cur_substr)
        start = end
    return tokens

# Simulate a small WordPiece vocabulary
small_vocab = {
    'play', '##ing', '##ed', '##er', '##s', '##ly',
    'run', 'low', '##est', '##er', 'quick', 'the', 'a',
    'p', 'l', 'a', 'y', 'r', 'u', 'n', 'e', 'q', 'i', 'c', 'k',
    '[UNK]', '[CLS]', '[SEP]', '[PAD]', '[MASK]',
}
test_words = ['playing', 'played', 'player', 'running', 'lowest', 'zyx']
print(f'{"Word":<12} {"WordPiece Tokens"}')
print('-' * 45)
for w in test_words:
    toks = wordpiece_encode(w, small_vocab)
    print(f'{w:<12} {toks}')
```

## Special Tokens and Formats

BERT uses four special tokens in every input: [CLS] (ID 101) prepended to every sequence, used as the sequence classification token; [SEP] (ID 102) appended after each sentence; [PAD] (ID 0) for padding to uniform length; [MASK] (ID 103) for masked language model pre-training. For sentence pairs (e.g., NLI, QA), the format is [CLS] sentence_A [SEP] sentence_B [SEP]. The token_type_ids tensor indicates which sentence each token belongs to: 0 for sentence A (including [CLS] and first [SEP]) and 1 for sentence B (including second [SEP]). The attention_mask tensor masks padding tokens from self-attention: 1 for real tokens, 0 for [PAD].

| Property | Value / Detail |
| --- | --- |
| Continuation marker | ## prefix on mid-word subwords (e.g., ##ing, ##ed) |
| Special tokens | [PAD]=0, [UNK]=100, [CLS]=101, [SEP]=102, [MASK]=103 |
| Pre-tokenization | Whitespace split → punctuation split → WordPiece |
| OOV handling | Any char not in character vocab → entire word becomes [UNK] |
| Vocab size (BERT-base) | 30,522 tokens (cased and uncased models) |
| Case handling | Cased: preserves case + accents; Uncased: lowercase + accent strip |
| Fast tokenizer | Rust implementation via HuggingFace tokenizers library |

## Encoding Mechanics

BERT's tokenization pipeline has three stages: (1) whitespace tokenization splits on any whitespace character; (2) punctuation tokenization further splits tokens on punctuation boundaries (so 'end.' becomes ['end', '.']); (3) WordPiece tokenization applies the greedy longest-match algorithm with ## prefixes. The encode_plus method returns a dictionary with input_ids, token_type_ids, and attention_mask. Setting return_offsets_mapping=True adds a mapping from each token position to its character span in the original string—essential for NER and span extraction tasks where the model must predict character-level labels.

```python
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

# Single sentence
text = 'The quick brown fox jumps over the lazy dog.'
enc = tokenizer(text, return_tensors='pt', return_offsets_mapping=True)
print('Single sentence encoding:')
print(f'  input_ids   : {enc["input_ids"][0].tolist()}')
print(f'  tokens      : {tokenizer.convert_ids_to_tokens(enc["input_ids"][0].tolist())}')
print(f'  attn_mask   : {enc["attention_mask"][0].tolist()}')
print(f'  offsets     : {enc["offset_mapping"][0].tolist()}')
print()

# Sentence pair (NLI format)
sentA = 'The cat sat on the mat.'
sentB = 'A feline rested on a rug.'
enc2 = tokenizer(sentA, sentB, return_tensors='pt', padding=True, truncation=True)
print('Sentence pair encoding:')
print(f'  tokens      : {tokenizer.convert_ids_to_tokens(enc2["input_ids"][0].tolist())}')
print(f'  type_ids    : {enc2["token_type_ids"][0].tolist()}')
print(f'  Format: [CLS] sentA [SEP] sentB [SEP]')
print()
print(f'Vocab size: {tokenizer.vocab_size}')
print(f'Special tokens: {tokenizer.all_special_tokens}')
```

## Cased vs Uncased

BERT-base-uncased lowercases all input and strips Unicode accent characters before WordPiece tokenization: 'Étude' becomes 'etude'. This reduces vocabulary diversity and improves coverage of common words, but loses case and diacritic information. BERT-base-cased preserves case and accents, making it better for tasks where case carries semantic meaning: named entity recognition (differentiating 'apple' the fruit from 'Apple' the company), and languages where diacritics change word meaning (French, German, Spanish). For most English classification tasks, uncased performs comparably or better due to improved generalisation across case variants.

> **Continuation Marker Semantics**: WordPiece's ## continuation marker means vocabulary statistics differ from BPE — 'running' and '##running' are distinct tokens. This gives WordPiece an explicit representation of morphological suffixes: ##ing, ##ed, ##er, ##ly, ##tion are all high-frequency vocabulary entries encoding suffix semantics. BPE merges these into the preceding subword without marking the boundary, so 'run' and 'running' share no explicit subword. For morphologically rich languages (Finnish, Turkish, Hungarian), WordPiece's explicit suffix representation can provide cleaner morphological signal to the model.

## Token Alignment for Span Tasks

Span-extraction tasks (NER, QA, coreference) require mapping model predictions from token space back to character offsets in the original text. The offset_mapping return value provides exactly this: each token gets a (start, end) character span. Tokens split by WordPiece have consecutive overlapping spans: 'running' split as ['run', '##ning'] gets offsets [(0,3), (3,7)]. [CLS] and [SEP] special tokens get offset (0, 0). When aligning labels for NER training, use the word_ids() method to get the word index for each token, then assign the label of the original word to its first subword (and a special ignore label, typically -100, to all continuation subwords).

```python
from transformers import AutoTokenizer

# Cross-tokenizer comparison on the same sentences
sentences = [
    'running quickly',
    'tokenization splits text',
    'supercalifragilistic',
    'the quick brown fox',
    'GPT-4 outperforms earlier models',
]

models = [
    ('BPE (GPT-2)',      'gpt2'),
    ('WordPiece (BERT)', 'bert-base-uncased'),
    ('Unigram (T5)',     't5-small'),
]
for model_name, model_id in models:
    print(f'\n--- {model_name} ---')
    tok = AutoTokenizer.from_pretrained(model_id)
    for sent in sentences:
        tokens = tok.tokenize(sent)
        print(f'  {sent!r:<35} -> {len(tokens):2d} tokens: {tokens}')

print('\nKey differences:')
print('  BPE (GPT-2)  : no continuation marker, space encoded as G-dot prefix')
print('  WordPiece    : ## prefix for mid-word subwords (explicit suffix marking)')
print('  Unigram (T5) : _ prefix for word-start subwords (like SentencePiece)')
```

## Key Takeaways

- WordPiece uses a likelihood ratio merge criterion (score = freq(ab) / [freq(a) × freq(b)]) rather than BPE's raw frequency count.
- The ## prefix marks continuation subwords: 'running' → ['run', '##ning'] gives explicit morphological suffix representation.
- BERT uses 30,522 tokens with fixed special IDs: [PAD]=0, [UNK]=100, [CLS]=101, [SEP]=102, [MASK]=103.
- Input format for sentence pairs: [CLS] sentA [SEP] sentB [SEP]; token_type_ids=0 for sentA, 1 for sentB.
- Uncased BERT strips accents and lowercases; cased BERT preserves case. Use cased for NER, uncased for classification.
- Use BertTokenizerFast (Rust backend) for production; it is 10–100× faster and supports offset_mapping.
- For NER/span tasks, use word_ids() to align WordPiece tokens to original words; assign -100 to continuation subword labels.

---

