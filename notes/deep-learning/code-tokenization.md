---
title: "Code Tokenization — Whitespace, Indentation, and Programming Language Fertility"
slug: "code-tokenization"
description: "Code imposes unique challenges for BPE tokenizers: whitespace is semantic in Python, operators split unexpectedly, and identifier naming conventions affect token counts. Covers GPT-2/GPT-4 BPE artifacts in code, indentation encoding, operator splitting, and cross-language fertility differences."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29kZSB0b2tlbml6YXRpb24gZGlmZmVycyBmdW5kYW1lbnRhbGx5IGZyb20gbmF0dXJhbCBsYW5ndWFnZSB0b2tlbml6YXRpb24uIEluIFB5dGhvbiwgd2hpdGVzcGFjZSBlbmNvZGVzIHByb2dyYW0gc2VtYW50aWNzIOKAlCBmb3VyIHNwYWNlcyBvZiBpbmRlbnRhdGlvbiBpcyBub3Qgc3R5bGlzdGljIGJ1dCBzdHJ1Y3R1cmFsLiBPcGVyYXRvcnMgbGlrZSA9PSBvciAtXHUwMDNlIGNhcnJ5IHByZWNpc2UgbWVhbmluZyBidXQgbWF5IHRva2VuaXplIGFzIG9uZSBvciB0d28gdG9rZW5zIGRlcGVuZGluZyBvbiB0aGUgdm9jYWJ1bGFyeS4gSWRlbnRpZmllciBuYW1pbmcgY29udmVudGlvbnMgKGNhbWVsQ2FzZSwgc25ha2VfY2FzZSwgUGFzY2FsQ2FzZSkgYWZmZWN0IGhvdyBpZGVudGlmaWVycyBzcGxpdCBhY3Jvc3MgdG9rZW4gYm91bmRhcmllcy4gVW5kZXJzdGFuZGluZyB0aGVzZSBhcnRpZmFjdHMgaXMgY3JpdGljYWwgZm9yIGNvZGUgbW9kZWwgZmluZS10dW5pbmcsIHRva2VuIGJ1ZGdldCBlc3RpbWF0aW9uLCBhbmQgc3Bhbi1sZXZlbCBjb2RlIGhpZ2hsaWdodGluZyBpbiBJREUgdG9vbGluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHUFQtMi9HUFQtNCBCUEUgQXJ0aWZhY3RzIGluIENvZGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdQVC0yIGFuZCBHUFQtNCBCUEUgdG9rZW5pemVycyB1c2Ugc3BlY2lhbCBVbmljb2RlIG1hcmtlcnMgdG8gZW5jb2RlIHdoaXRlc3BhY2UuIEEgc3BhY2UgYmVmb3JlIGEgd29yZCBpcyByZXByZXNlbnRlZCBieSB0aGUgxKAgcHJlZml4IChVbmljb2RlIFUrMDEyMCksIHNvIFx1MDAyNyBkZWZcdTAwMjcgYmVjb21lcyBcdTAwMjfEoGRlZlx1MDAyNy4gTmV3bGluZXMgYXJlIGVuY29kZWQgYXMgxIogKFUrMDEwQSkuIENvbnNlY3V0aXZlIHNwYWNlcyBnZXQgdGhlaXIgb3duIG1lcmdlZCB0b2tlbnM6IFx1MDAyNyAgICBcdTAwMjcgKGZvdXIgc3BhY2VzKSBtYXkgdG9rZW5pemUgYXMgYSBzaW5nbGUgXHUwMDI3xKAgICBcdTAwMjcgdG9rZW4gb3IgYXMgZm91ciBpbmRpdmlkdWFsIHNwYWNlIHRva2VucyBkZXBlbmRpbmcgb24gdm9jYWJ1bGFyeSBmcmVxdWVuY3kuIFRoaXMgbWVhbnMgUHl0aG9uIGluZGVudGF0aW9uIHRva2VucyBhcmUgaGlnaGx5IHRva2VuaXplci1zcGVjaWZpYyDigJQgdGhlIHNhbWUgaW5kZW50ZWQgYmxvY2sgbWF5IGNvbnN1bWUgMSBvciA0IHRva2VucyBkZXBlbmRpbmcgb24gdHJhaW5pbmcgY29ycHVzIGNvbXBvc2l0aW9uLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29kZUJFUlQgYW5kIFN0YXJDb2RlciB1c2UgY29kZS1zcGVjaWZpYyB2b2NhYnVsYXJpZXMgcHJlLXRyYWluZWQgb24gR2l0SHViIHJlcG9zaXRvcmllcy4gVGhlaXIgdm9jYWJ1bGFyaWVzIGluY2x1ZGUgY29tbW9uIHByb2dyYW1taW5nIHRva2VucyBsaWtlIFx1MDAyN2RlZlx1MDAyNywgXHUwMDI3cmV0dXJuXHUwMDI3LCBcdTAwMjdpbXBvcnRcdTAwMjcsIFx1MDAyN2NsYXNzXHUwMDI3LCBhbmQgY29tbW9uIG9wZXJhdG9ycyBhcyBzaW5nbGUgdG9rZW5zLiBUaGlzIGdpdmVzIHRoZW0gbG93ZXIgZmVydGlsaXR5IG9uIGNvZGUgdGhhbiBnZW5lcmFsLXB1cnBvc2UgdG9rZW5pemVycywgYnV0IGhpZ2hlciBmZXJ0aWxpdHkgb24gbmF0dXJhbCBsYW5ndWFnZSBkZXNjcmlwdGlvbnMgYW5kIGRvY3N0cmluZ3MuIFRoZSB0cmFkZW9mZiBpcyBkZWxpYmVyYXRlOiBjb2RlIG1vZGVscyBvcHRpbWlzZSB0aGVpciB0b2tlbiBidWRnZXQgZm9yIHRoZSBkb21haW4gdGhleSB3aWxsIHByaW1hcmlseSBwcm9jZXNzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgVG9rZW5pemF0aW9uIEFuYWx5c2lzIEFjcm9zcyBMYW5ndWFnZXMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRpa3Rva2VuXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG5kZWYgdG9rZW5pemVfYWxnb3JpdGhtKGFsZ29fdGV4dCwgdG9rZW5pemVyX2ZuLCB0b2tlbml6ZXJfbmFtZSk6XG4gICAgdG9rZW5zID0gdG9rZW5pemVyX2ZuKGFsZ29fdGV4dClcbiAgICByZXR1cm4ge1x1MDAyN25cdTAwMjc6IGxlbih0b2tlbnMpLCBcdTAwMjduYW1lXHUwMDI3OiB0b2tlbml6ZXJfbmFtZX1cblxuIyBTYW1lIGJ1YmJsZSBzb3J0IGFsZ29yaXRobSBpbiB0aHJlZSBsYW5ndWFnZXNcbmFsZ29yaXRobXMgPSB7XG4gICAgXHUwMDI3cHl0aG9uXHUwMDI3OiBcdTAwMjdkZWYgYnViYmxlX3NvcnQoYXJyKTpcXG4gICAgbiA9IGxlbihhcnIpXFxuICAgIGZvciBpIGluIHJhbmdlKG4pOlxcbiAgICAgICAgZm9yIGogaW4gcmFuZ2UobiAtIGkgLSAxKTpcXG4gICAgICAgICAgICBpZiBhcnJbal0gXHUwMDNlIGFycltqICsgMV06XFxuICAgICAgICAgICAgICAgIGFycltqXSwgYXJyW2ogKyAxXSA9IGFycltqICsgMV0sIGFycltqXVxcbiAgICByZXR1cm4gYXJyXHUwMDI3LFxuICAgIFx1MDAyN2phdmFzY3JpcHRcdTAwMjc6IFx1MDAyN2Z1bmN0aW9uIGJ1YmJsZVNvcnQoYXJyKSB7XFxuICBjb25zdCBuID0gYXJyLmxlbmd0aDtcXG4gIGZvciAobGV0IGkgPSAwOyBpIFx1MDAzYyBuOyBpKyspIHtcXG4gICAgZm9yIChsZXQgaiA9IDA7IGogXHUwMDNjIG4gLSBpIC0gMTsgaisrKSB7XFxuICAgICAgaWYgKGFycltqXSBcdTAwM2UgYXJyW2ogKyAxXSkge1xcbiAgICAgICAgW2FycltqXSwgYXJyW2ogKyAxXV0gPSBbYXJyW2ogKyAxXSwgYXJyW2pdXTtcXG4gICAgICB9XFxuICAgIH1cXG4gIH1cXG4gIHJldHVybiBhcnI7XFxufVx1MDAyNyxcbiAgICBcdTAwMjdqYXZhXHUwMDI3OiBcdTAwMjdwdWJsaWMgc3RhdGljIHZvaWQgYnViYmxlU29ydChpbnRbXSBhcnIpIHtcXG4gICAgaW50IG4gPSBhcnIubGVuZ3RoO1xcbiAgICBmb3IgKGludCBpID0gMDsgaSBcdTAwM2MgbiAtIDE7IGkrKykge1xcbiAgICAgICAgZm9yIChpbnQgaiA9IDA7IGogXHUwMDNjIG4gLSBpIC0gMTsgaisrKSB7XFxuICAgICAgICAgICAgaWYgKGFycltqXSBcdTAwM2UgYXJyW2ogKyAxXSkge1xcbiAgICAgICAgICAgICAgICBpbnQgdG1wID0gYXJyW2pdO1xcbiAgICAgICAgICAgICAgICBhcnJbal0gPSBhcnJbaiArIDFdO1xcbiAgICAgICAgICAgICAgICBhcnJbaiArIDFdID0gdG1wO1xcbiAgICAgICAgICAgIH1cXG4gICAgICAgIH1cXG4gICAgfVxcbn1cdTAwMjcsXG59XG5lbmNfZ3B0NCA9IHRpa3Rva2VuLmdldF9lbmNvZGluZyhcdTAwMjdjbDEwMGtfYmFzZVx1MDAyNylcbmVuY19ncHQyID0gdGlrdG9rZW4uZ2V0X2VuY29kaW5nKFx1MDAyN2dwdDJcdTAwMjcpXG5zdGFyY29kZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcdTAwMjdiaWdjb2RlL3N0YXJjb2Rlclx1MDAyNylcbmZvciBsYW5nLCBjb2RlIGluIGFsZ29yaXRobXMuaXRlbXMoKTpcbiAgICBuX2dwdDQgPSBsZW4oZW5jX2dwdDQuZW5jb2RlKGNvZGUpKVxuICAgIG5fZ3B0MiA9IGxlbihlbmNfZ3B0Mi5lbmNvZGUoY29kZSkpXG4gICAgbl9zdGFyID0gbGVuKHN0YXJjb2Rlci5lbmNvZGUoY29kZSkpXG4gICAgcHJpbnQoZlx1MDAyN3tsYW5nOlx1MDAzYzEyfTogZ3B0ND17bl9ncHQ0Olx1MDAzZTR9ICBncHQyPXtuX2dwdDI6XHUwMDNlNH0gIHN0YXJjb2Rlcj17bl9zdGFyOlx1MDAzZTR9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkluZGVudGF0aW9uIFRva2VuIEFuYWx5c2lzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQeXRob24gaW5kZW50YXRpb24gaXMgc2VtYW50aWNhbGx5IGNyaXRpY2FsIOKAlCBzdHJpcHBpbmcgb3IgbW9kaWZ5aW5nIGl0IGNoYW5nZXMgcHJvZ3JhbSBtZWFuaW5nLiBBIHN0YW5kYXJkIDQtc3BhY2UgaW5kZW50IHRva2VuaXplcyBkaWZmZXJlbnRseSBhY3Jvc3MgdG9rZW5pemVyczogR1BULTQgKGNsMTAwa19iYXNlKSBtZXJnZXMgY29uc2VjdXRpdmUgc3BhY2VzIGludG8gYSBzaW5nbGUgdG9rZW4gZm9yIGNvbW1vbiBpbmRlbnQgd2lkdGhzLCB3aGlsZSBHUFQtMiBtYXkgc3BsaXQgdGhlbSBpbnRvIGluZGl2aWR1YWwgc3BhY2UgdG9rZW5zLiBUYWIgY2hhcmFjdGVycyAoXFx0KSB0eXBpY2FsbHkgdG9rZW5pemUgYXMgYSBzaW5nbGUgdG9rZW4uIE5lc3RlZCBpbmRlbnRhdGlvbiAoOCBvciAxMiBzcGFjZXMgZm9yIGRvdWJseSBvciB0cmlwbHkgbmVzdGVkIGJsb2NrcykgZnVydGhlciBjb21wb3VuZHMgdGhlIHRva2VuIGNvdW50LCBtYWtpbmcgZGVlcGx5IG5lc3RlZCBQeXRob24gY29kZSBkaXNwcm9wb3J0aW9uYXRlbHkgZXhwZW5zaXZlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdGlrdG9rZW5cblxuZGVmIGFuYWx5emVfaW5kZW50YXRpb24odG9rZW5pemVyX25hbWU9XHUwMDI3Y2wxMDBrX2Jhc2VcdTAwMjcpOlxuICAgIGVuYyA9IHRpa3Rva2VuLmdldF9lbmNvZGluZyh0b2tlbml6ZXJfbmFtZSlcbiAgICBpbmRlbnRfc3R5bGVzID0ge1xuICAgICAgICBcdTAwMjcyLXNwYWNlIGluZGVudFx1MDAyNzogICBcdTAwMjcgIHggPSAxXHUwMDI3LFxuICAgICAgICBcdTAwMjc0LXNwYWNlIGluZGVudFx1MDAyNzogICBcdTAwMjcgICAgeCA9IDFcdTAwMjcsXG4gICAgICAgIFx1MDAyNzgtc3BhY2UgaW5kZW50XHUwMDI3OiAgIFx1MDAyNyAgICAgICAgeCA9IDFcdTAwMjcsXG4gICAgICAgIFx1MDAyNzEyLXNwYWNlIGluZGVudFx1MDAyNzogIFx1MDAyNyAgICAgICAgICAgIHggPSAxXHUwMDI3LFxuICAgICAgICBcdTAwMjd0YWIgaW5kZW50XHUwMDI3OiAgICAgICBcdTAwMjdcXHR4ID0gMVx1MDAyNyxcbiAgICAgICAgXHUwMDI3dGFiKzQgaW5kZW50XHUwMDI3OiAgICAgXHUwMDI3XFx0ICAgIHggPSAxXHUwMDI3LFxuICAgIH1cbiAgICBwcmludChmXHUwMDI3VG9rZW5pemVyOiB7dG9rZW5pemVyX25hbWV9XHUwMDI3KVxuICAgIGZvciBsYWJlbCwgdGV4dCBpbiBpbmRlbnRfc3R5bGVzLml0ZW1zKCk6XG4gICAgICAgIHRva2VucyA9IGVuYy5lbmNvZGUodGV4dClcbiAgICAgICAgZGVjb2RlZCA9IFtlbmMuZGVjb2RlKFt0XSkgZm9yIHQgaW4gdG9rZW5zXVxuICAgICAgICBkaXNwbGF5ID0gW3JlcHIoZCkgZm9yIGQgaW4gZGVjb2RlZF1cbiAgICAgICAgcHJpbnQoZlx1MDAyNyAge2xhYmVsOlx1MDAzYzIwfToge2xlbih0b2tlbnMpfSB0b2tlbnMgIHtkaXNwbGF5fVx1MDAyNylcblxuYW5hbHl6ZV9pbmRlbnRhdGlvbihcdTAwMjdjbDEwMGtfYmFzZVx1MDAyNylcbnByaW50KClcbmFuYWx5emVfaW5kZW50YXRpb24oXHUwMDI3Z3B0Mlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPcGVyYXRvciBhbmQgSWRlbnRpZmllciBUb2tlbml6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IklkZW50aWZpZXIgbmFtaW5nIGNvbnZlbnRpb25zIGludGVyYWN0IHN0cm9uZ2x5IHdpdGggQlBFIHRva2VuaXphdGlvbi4gQSBzbmFrZV9jYXNlIGlkZW50aWZpZXIgbGlrZSBcdTAwMjdjYWxjdWxhdGVfZ3JhZGllbnRfbm9ybVx1MDAyNyB0eXBpY2FsbHkgc3BsaXRzIGF0IHVuZGVyc2NvcmVzLCBwcm9kdWNpbmcgM+KAkzQgdG9rZW5zLiBBIGNhbWVsQ2FzZSBpZGVudGlmaWVyIGxpa2UgXHUwMDI3Y2FsY3VsYXRlR3JhZGllbnROb3JtXHUwMDI3IG1heSBzcGxpdCBhdCBjYXNlIGJvdW5kYXJpZXMgKHNvbWUgdG9rZW5pemVycyB0cmVhdCB1cHBlcmNhc2UgbGV0dGVycyBhcyBzcGxpdCBwb2ludHMpIG9yIHJlbWFpbiBtZXJnZWQgaWYgdGhlIHdob2xlIGlkZW50aWZpZXIgYXBwZWFycyBpbiB0cmFpbmluZyBkYXRhLiBPcGVyYXRvcnMgbGlrZSA9PSB1c3VhbGx5IHRva2VuaXplIGFzIGEgc2luZ2xlIHRva2VuIGluIGNvZGUtYXdhcmUgdm9jYWJ1bGFyaWVzLCB3aGlsZSAtXHUwMDNlIGFuZCA9XHUwMDNlIG1heSBiZSBvbmUgb3IgdHdvIHRva2VucyBkZXBlbmRpbmcgb24gdGhlIHRyYWluaW5nIGNvcnB1cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRpa3Rva2VuXG5cbmRlZiBhbmFseXplX2lkZW50aWZpZXJzX2FuZF9vcHModG9rZW5pemVyX25hbWU9XHUwMDI3Y2wxMDBrX2Jhc2VcdTAwMjcpOlxuICAgIGVuYyA9IHRpa3Rva2VuLmdldF9lbmNvZGluZyh0b2tlbml6ZXJfbmFtZSlcbiAgICBzYW1wbGVzID0ge1xuICAgICAgICBcdTAwMjdjYW1lbENhc2VcdTAwMjc6ICAgIFx1MDAyN2NhbGN1bGF0ZUdyYWRpZW50Tm9ybVx1MDAyNyxcbiAgICAgICAgXHUwMDI3c25ha2VfY2FzZVx1MDAyNzogICBcdTAwMjdjYWxjdWxhdGVfZ3JhZGllbnRfbm9ybVx1MDAyNyxcbiAgICAgICAgXHUwMDI3UGFzY2FsQ2FzZVx1MDAyNzogICBcdTAwMjdDYWxjdWxhdGVHcmFkaWVudE5vcm1cdTAwMjcsXG4gICAgICAgIFx1MDAyN1NDUkVBTUlOR1x1MDAyNzogICAgXHUwMDI3TUFYX0dSQURJRU5UX05PUk1cdTAwMjcsXG4gICAgICAgIFx1MDAyN2VxIG9wZXJhdG9yXHUwMDI3OiAgXHUwMDI3PT1cdTAwMjcsXG4gICAgICAgIFx1MDAyN25lIG9wZXJhdG9yXHUwMDI3OiAgXHUwMDI3IT1cdTAwMjcsXG4gICAgICAgIFx1MDAyN2Fycm93IChDKyspXHUwMDI3OiAgXHUwMDI3LVx1MDAzZVx1MDAyNyxcbiAgICAgICAgXHUwMDI3ZmF0IGFycm93XHUwMDI3OiAgICBcdTAwMjc9XHUwMDNlXHUwMDI3LFxuICAgICAgICBcdTAwMjd3YWxydXNcdTAwMjc6ICAgICAgIFx1MDAyNzo9XHUwMDI3LFxuICAgICAgICBcdTAwMjd0eXBlIGhpbnRcdTAwMjc6ICAgIFx1MDAyN2xpc3RbaW50XVx1MDAyNyxcbiAgICAgICAgXHUwMDI3ZGVjb3JhdG9yXHUwMDI3OiAgICBcdTAwMjdAdG9yY2gubm9fZ3JhZCgpXHUwMDI3LFxuICAgIH1cbiAgICBwcmludChmXHUwMDI3T3BlcmF0b3IvaWRlbnRpZmllciB0b2tlbml6YXRpb24gKHt0b2tlbml6ZXJfbmFtZX0pXHUwMDI3KVxuICAgIGZvciBsYWJlbCwgdGV4dCBpbiBzYW1wbGVzLml0ZW1zKCk6XG4gICAgICAgIHRva2VucyA9IGVuYy5lbmNvZGUodGV4dClcbiAgICAgICAgcGllY2VzID0gW2VuYy5kZWNvZGUoW3RdKSBmb3IgdCBpbiB0b2tlbnNdXG4gICAgICAgIHByaW50KGZcdTAwMjcgIHtsYWJlbDpcdTAwM2MxNn06IHtsZW4odG9rZW5zKX0gdG9rICB7cGllY2VzfVx1MDAyNylcblxuYW5hbHl6ZV9pZGVudGlmaWVyc19hbmRfb3BzKFx1MDAyN2NsMTAwa19iYXNlXHUwMDI3KVxucHJpbnQoKVxuYW5hbHl6ZV9pZGVudGlmaWVyc19hbmRfb3BzKFx1MDAyN2dwdDJcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtTGFuZ3VhZ2UgRmVydGlsaXR5In0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0aWt0b2tlblxuXG5kZWYgdG9rZW5zX3Blcl9saW5lKGNvZGVfc25pcHBldCwgZW5jKTpcbiAgICBsaW5lcyA9IFtsIGZvciBsIGluIGNvZGVfc25pcHBldC5zcGxpdChcdTAwMjdcXG5cdTAwMjcpIGlmIGwuc3RyaXAoKV1cbiAgICBpZiBub3QgbGluZXM6XG4gICAgICAgIHJldHVybiAwLjBcbiAgICB0b3RhbCA9IHN1bShsZW4oZW5jLmVuY29kZShsKSkgZm9yIGwgaW4gbGluZXMpXG4gICAgcmV0dXJuIHRvdGFsIC8gbGVuKGxpbmVzKVxuXG5lbmMgPSB0aWt0b2tlbi5nZXRfZW5jb2RpbmcoXHUwMDI3Y2wxMDBrX2Jhc2VcdTAwMjcpXG5zbmlwcGV0cyA9IHtcbiAgICBcdTAwMjdQeXRob25cdTAwMjc6ICAgICBcdTAwMjdkZWYgYWRkKGEsIGIpOlxcbiAgICByZXR1cm4gYSArIGJcXG5yZXN1bHQgPSBhZGQoMSwgMilcdTAwMjcsXG4gICAgXHUwMDI3SmF2YVNjcmlwdFx1MDAyNzogXHUwMDI3Y29uc3QgYWRkID0gKGEsIGIpID1cdTAwM2UgYSArIGI7XFxuY29uc3QgcmVzdWx0ID0gYWRkKDEsIDIpO1x1MDAyNyxcbiAgICBcdTAwMjdKYXZhXHUwMDI3OiAgICAgICBcdTAwMjdwdWJsaWMgaW50IGFkZChpbnQgYSwgaW50IGIpIHsgcmV0dXJuIGEgKyBiOyB9XFxuaW50IHJlc3VsdCA9IGFkZCgxLCAyKTtcdTAwMjcsXG4gICAgXHUwMDI3U1FMXHUwMDI3OiAgICAgICAgXHUwMDI3U0VMRUNUIGlkLCBuYW1lIEZST00gdXNlcnMgV0hFUkUgYWN0aXZlID0gMSBPUkRFUiBCWSBuYW1lIEFTQztcdTAwMjcsXG4gICAgXHUwMDI3TGFUZVhcdTAwMjc6ICAgICAgXHUwMDI3XFxcXGZyYWN7XFxcXHBhcnRpYWwgTH17XFxcXHBhcnRpYWwgd30gPSBcXFxcc3VtX3tpPTF9XntufSB4X2kgKHlfaSAtIFxcXFxoYXR7eX1faSlcdTAwMjcsXG4gICAgXHUwMDI3SlNPTlx1MDAyNzogICAgICAgXHUwMDI3e1wibW9kZWxcIjogXCJncHQtNFwiLCBcInRlbXBlcmF0dXJlXCI6IDAuNywgXCJtYXhfdG9rZW5zXCI6IDUxMn1cdTAwMjcsXG4gICAgXHUwMDI3UmVnZXhcdTAwMjc6ICAgICAgXHUwMDI3Xig/OlswLTldezEsM31cXFxcLil7M31bMC05XXsxLDN9JFx1MDAyNyxcbiAgICBcdTAwMjdCYXNoXHUwMDI3OiAgICAgICBcdTAwMjdmb3IgZiBpbiAqLnB5OyBkbyBweXRob24gJGYgLS1vdXRwdXQgcmVzdWx0cy87IGRvbmVcdTAwMjcsXG59XG5wcmludChmXHUwMDI3e1wiTGFuZ3VhZ2VcIjpcdTAwM2MxNH0ge1wiVG9rL0xpbmVcIjpcdTAwM2UxMH0ge1wiVG90YWwgVG9rXCI6XHUwMDNlMTB9XHUwMDI3KVxuZm9yIGxhbmcsIGNvZGUgaW4gc25pcHBldHMuaXRlbXMoKTpcbiAgICB0cGwgPSB0b2tlbnNfcGVyX2xpbmUoY29kZSwgZW5jKVxuICAgIHRvdGFsID0gbGVuKGVuYy5lbmNvZGUoY29kZSkpXG4gICAgcHJpbnQoZlx1MDAyN3tsYW5nOlx1MDAzYzE0fSB7dHBsOlx1MDAzZTEwLjJmfSB7dG90YWw6XHUwMDNlMTB9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgVG9rZW5pemF0aW9uIENoYXJhY3RlcmlzdGljcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJMYW5ndWFnZSIsIkF2ZyBUb2tlbnMvTGluZSIsIktleSBUb2tlbml6YXRpb24gQXJ0aWZhY3QiLCJJbmRlbnRhdGlvbiBIYW5kbGluZyIsIk9wZXJhdG9yIFNwbGl0dGluZyJdLCJyb3dzIjpbWyJQeXRob24iLCI24oCTMTAiLCLEoCBwcmVmaXggb24gc3BhY2UgdG9rZW5zOyBtZXJnZWQgaW5kZW50IGJsb2NrcyIsIjQgc3BhY2VzIOKGkiAx4oCTNCB0b2tlbnMgKHRva2VuaXplci1kZXBlbmRlbnQpIiwiPT0gYXMgMSB0b2tlbjsgLy8gYXMgMiB0b2tlbnMgdXN1YWxseSJdLFsiSmF2YVNjcmlwdCIsIjXigJM5IiwieyB9IG1lcmdlIHdpdGggcHJlY2VkaW5nIHRva2VuOyA9XHUwMDNlIHNwbGl0IiwiQnJhY2VzIG5vdCBpbmRlbnRlZDsgc3BhY2UgYWZ0ZXIgeyBpcyBzZXBhcmF0ZSIsIj1cdTAwM2UgbWF5IGJlIDHigJMyIHRva2VuczsgPT09IGlzIDLigJMzIHRva2VucyJdLFsiSmF2YSIsIjfigJMxMiIsIkxvbmcgY2xhc3MvbWV0aG9kIG5hbWVzIHNwbGl0IGF0IGNhc2UgYm91bmRhcmllcyIsIkJyYWNlcyBvbiBzYW1lIG9yIG5leHQgbGluZTsgaW5kZW50YXRpb24gbGVzcyBzZW1hbnRpYyIsIi1cdTAwM2UgbGFtYmRhIGFycm93OiAx4oCTMiB0b2tlbnMiXSxbIlNRTCIsIjTigJM4IiwiVVBQRVJDQVNFIGtleXdvcmRzIG9mdGVuIHNpbmdsZSB0b2tlbnM7IGxvd2VyY2FzZSB2YXJpYW50cyBzcGxpdCIsIk5vIGluZGVudGF0aW9uIHNlbWFudGljcyIsIiE9IGFuZCBcdTAwM2NcdTAwM2UgYm90aCB0b2tlbml6ZSBhcyAyIHRva2VucyJdLFsiTGFUZVgiLCI44oCTMTUiLCJCYWNrc2xhc2ggc2VxdWVuY2VzOiBcXFxcZnJhYyBzcGxpdHMgaW50byAy4oCTMyB0b2tlbnMiLCJObyBpbmRlbnRhdGlvbjsgaGVhdnkgdXNlIG9mIHsgfSBicmFjZXMiLCJfIGFuZCBeIGFzIHNpbmdsZSB0b2tlbnM7IHN1YnNjcmlwdHMgc3BsaXQiXSxbIkpTT04iLCIz4oCTNiIsIkNvbG9uIGFuZCBxdW90ZXMgb2Z0ZW4gbWVyZ2Ugd2l0aCBrZXkgdG9rZW5zIiwiTm8gc2VtYW50aWMgaW5kZW50YXRpb24iLCI6IHVzdWFsbHkgMSB0b2tlbjsge30gYW5kIFtdIGFzIDEgdG9rZW4gZWFjaCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVG9rZW4gQWxpZ25tZW50IHRvIFNvdXJjZSBDb2RlIExpbmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJREUgdG9vbGluZyBmb3IgY29kZSBtb2RlbHMg4oCUIGlubGluZSBjb21wbGV0aW9ucywgZXJyb3IgZXhwbGFuYXRpb25zLCBzcGFuIGhpZ2hsaWdodGluZyDigJQgcmVxdWlyZXMgbWFwcGluZyB0b2tlbiBpbmRpY2VzIGJhY2sgdG8gc291cmNlIGxpbmUgYW5kIGNvbHVtbiBwb3NpdGlvbnMuIEJQRSB0b2tlbnMgZG8gbm90IGFsaWduIHRvIGxpbmUgYm91bmRhcmllczogYSB0b2tlbiBtYXkgc3BhbiBhIG5ld2xpbmUgY2hhcmFjdGVyLCBhbmQgYSBzaW5nbGUgbG9naWNhbCBsaW5lIG1heSBwcm9kdWNlIGRvemVucyBvZiB0b2tlbnMuIFRvIGJ1aWxkIHRoZSB0b2tlbi10by1saW5lIG1hcHBpbmcsIHJlY29uc3RydWN0IHRoZSBjaGFyYWN0ZXIgb2Zmc2V0IG9mIGVhY2ggdG9rZW4gYnkgZGVjb2RpbmcgcHJlZml4IHRva2VuIHNlcXVlbmNlcywgdGhlbiBiaW5hcnktc2VhcmNoIGFnYWluc3QgdGhlIG5ld2xpbmUgcG9zaXRpb25zIG9mIHRoZSBvcmlnaW5hbCBzb3VyY2Ugc3RyaW5nLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEh1bWFuRXZhbCBiZW5jaG1hcmsgdXNlcyBjb2RlIGluIGEgc3BlY2lmaWMgZm9ybWF0OiBmdW5jdGlvbiBzaWduYXR1cmUgZm9sbG93ZWQgYnkgZG9jc3RyaW5nIGZvbGxvd2VkIGJ5IGltcGxlbWVudGF0aW9uLiBUb2tlbml6aW5nIHRoaXMgZm9ybWF0IHdpdGggZGlmZmVyZW50IHRva2VuaXplcnMgcHJvZHVjZXMgZGlmZmVyZW50IHByb21wdCBsZW5ndGhzLCBhZmZlY3RpbmcgdGhlIG51bWJlciBvZiBjb21wbGV0aW9uIHRva2VucyBhdmFpbGFibGUgd2l0aGluIHRoZSBtb2RlbFx1MDAyN3MgY29udGV4dCB3aW5kb3cuIENvZGUgbW9kZWxzIGZpbmUtdHVuZWQgd2l0aCBhIHNwZWNpZmljIHRva2VuaXplciBtdXN0IHVzZSB0aGF0IHNhbWUgdG9rZW5pemVyIGF0IGluZmVyZW5jZSB0aW1lIOKAlCBjcm9zcy10b2tlbml6ZXIgZXZhbHVhdGlvbiBpbnZhbGlkYXRlcyB0b2tlbiBjb3VudCBjb21wYXJpc29ucyBhY3Jvc3MgcGFwZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZpbmUtVHVuaW5nIENvZGUgTW9kZWxzIOKAlCBUb2tlbml6ZXIgSW1wbGljYXRpb25zIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkNoZWNrIE9wZXJhdG9yIE1lcmdpbmcgQmVmb3JlIEZpbmUtVHVuaW5nIiwiY29udGVudCI6IldoZW4gZmluZS10dW5pbmcgY29kZSBtb2RlbHMsIGNoZWNrIHRoYXQgdGhlIHRva2VuaXplciBjb3JyZWN0bHkgbWVyZ2VzIGNvbW1vbiBvcGVyYXRvcnMgaW4geW91ciB0YXJnZXQgbGFuZ3VhZ2Ug4oCUIHNvbWUgdG9rZW5pemVycyBzcGxpdCBcdTAwMjctXHUwMDNlXHUwMDI3IGludG8gMiB0b2tlbnMgYW5kIFx1MDAyNz1cdTAwM2VcdTAwMjcgaW50byAyIHRva2VucywgYWZmZWN0aW5nIHRva2VuIGJ1ZGdldCBwcmVkaWN0aW9ucyBieSAxMOKAkzIwJS4gUnVuIHRoZSBpbmRlbnRhdGlvbiBhbmQgb3BlcmF0b3IgYW5hbHlzaXMgb24gYSByZXByZXNlbnRhdGl2ZSBzYW1wbGUgb2YgeW91ciB0cmFpbmluZyBjb2RlIGJlZm9yZSBjb21taXR0aW5nIHRvIGEgdG9rZW5pemVyLCBhbmQgcHJlZmVyIGNvZGUtc3BlY2lmaWMgdm9jYWJ1bGFyaWVzIChTdGFyQ29kZXIsIENvZGVMbGFtYSkgZm9yIGNvZGUtaGVhdnkgd29ya2xvYWRzIHRvIG1pbmltaXNlIGZlcnRpbGl0eSBhbmQgbWF4aW1pc2UgZWZmZWN0aXZlIGNvbnRleHQgd2luZG93IHVzYWdlLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIGNvZGUtc3BlY2lmaWMgdG9rZW5pemVycyAoU3RhckNvZGVyLCBDb2RlTGxhbWEpIGZvciBjb2RlLWhlYXZ5IHRhc2tzIOKAlCAxNeKAkzMwJSBsb3dlciBmZXJ0aWxpdHkgdGhhbiBHUFQtMi4iLCJJbmRlbnRhdGlvbiBpcyBzZW1hbnRpYyBpbiBQeXRob246IG5vcm1hbGlzZSB0byBzcGFjZXMgYmVmb3JlIHRva2VuaXppbmcgdG8gYXZvaWQgdGFiL3NwYWNlIGZlcnRpbGl0eSBkaWZmZXJlbmNlcy4iLCJPcGVyYXRvciBzcGxpdHRpbmcgYWZmZWN0cyB0b2tlbiBidWRnZXQ6IHRlc3QgPT0sICE9LCAtXHUwMDNlLCA9XHUwMDNlLCA6PSBvbiB5b3VyIHRhcmdldCB0b2tlbml6ZXIgYmVmb3JlIGVzdGltYXRpbmcgY29zdHMuIiwiY2FtZWxDYXNlIGlkZW50aWZpZXJzIG1heSB0b2tlbml6ZSBhcyAxIHRva2VuIGlmIHRoZXkgYXBwZWFyIGZyZXF1ZW50bHkgaW4gdHJhaW5pbmc7IHJhcmUgaWRlbnRpZmllcnMgYWx3YXlzIHNwbGl0LiIsIlNRTCBVUFBFUkNBU0Uga2V5d29yZHMgdG9rZW5pemUgYmV0dGVyIHRoYW4gbG93ZXJjYXNlIHZhcmlhbnRzIGluIHRva2VuaXplcnMgdHJhaW5lZCBvbiBtaXhlZC1jYXNlIGNvcnBvcmEuIiwiSHVtYW5FdmFsIGV2YWx1YXRpb25zIG11c3QgbWF0Y2ggdHJhaW5pbmcgdG9rZW5pemVyIGV4YWN0bHkg4oCUIGNyb3NzLXRva2VuaXplciBjb21wYXJpc29ucyBhcmUgaW52YWxpZC4iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHByYWN0aWNhbCBjb2RlIHRva2VuaXphdGlvbiB3b3JrZmxvdzogKDEpIHNhbXBsZSAxMDAwIGxpbmVzIG9mIHByb2R1Y3Rpb24gY29kZSBpbiB5b3VyIHRhcmdldCBsYW5ndWFnZSwgKDIpIHRva2VuaXplIHdpdGggZWFjaCBjYW5kaWRhdGUgdG9rZW5pemVyIGFuZCBjb21wdXRlIG1lYW4gdG9rZW5zIHBlciBsaW5lLCAoMykgc2VsZWN0IHRoZSB0b2tlbml6ZXIgd2l0aCBsb3dlc3QgZmVydGlsaXR5IGZvciB5b3VyIGRvbWluYW50IGxhbmd1YWdlLCAoNCkgdmVyaWZ5IG9wZXJhdG9yIGFuZCBpZGVudGlmaWVyIHNwbGl0dGluZyBmb3IgdGhlIDIwIG1vc3QgY29tbW9uIGNvbnN0cnVjdHMgaW4geW91ciBjb2RlYmFzZSwgKDUpIG1lYXN1cmUgY29udGV4dCB3aW5kb3cgaGVhZHJvb20gd2l0aCB5b3VyIHR5cGljYWwgcHJvbXB0IHRlbXBsYXRlLiBUaGlzIGFuYWx5c2lzIHR5cGljYWxseSB0YWtlcyB1bmRlciBhbiBob3VyIGFuZCBwcmV2ZW50cyBjb3N0bHkgbWlzLWVzdGltYXRlcyBhdCBwcm9kdWN0aW9uIHNjYWxlLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Code Tokenization — Whitespace, Indentation, and Programming Language Fertility

Code tokenization differs fundamentally from natural language tokenization. In Python, whitespace encodes program semantics — four spaces of indentation is not stylistic but structural. Operators like == or -> carry precise meaning but may tokenize as one or two tokens depending on the vocabulary. Identifier naming conventions (camelCase, snake_case, PascalCase) affect how identifiers split across token boundaries. Understanding these artifacts is critical for code model fine-tuning, token budget estimation, and span-level code highlighting in IDE tooling.

## GPT-2/GPT-4 BPE Artifacts in Code

GPT-2 and GPT-4 BPE tokenizers use special Unicode markers to encode whitespace. A space before a word is represented by the Ġ prefix (Unicode U+0120), so ' def' becomes 'Ġdef'. Newlines are encoded as Ċ (U+010A). Consecutive spaces get their own merged tokens: '    ' (four spaces) may tokenize as a single 'Ġ   ' token or as four individual space tokens depending on vocabulary frequency. This means Python indentation tokens are highly tokenizer-specific — the same indented block may consume 1 or 4 tokens depending on training corpus composition.

CodeBERT and StarCoder use code-specific vocabularies pre-trained on GitHub repositories. Their vocabularies include common programming tokens like 'def', 'return', 'import', 'class', and common operators as single tokens. This gives them lower fertility on code than general-purpose tokenizers, but higher fertility on natural language descriptions and docstrings. The tradeoff is deliberate: code models optimise their token budget for the domain they will primarily process.

## Code Tokenization Analysis Across Languages

```python
import tiktoken
from transformers import AutoTokenizer

def tokenize_algorithm(algo_text, tokenizer_fn, tokenizer_name):
    tokens = tokenizer_fn(algo_text)
    return {'n': len(tokens), 'name': tokenizer_name}

# Same bubble sort algorithm in three languages
algorithms = {
    'python': 'def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(n - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n    return arr',
    'javascript': 'function bubbleSort(arr) {\n  const n = arr.length;\n  for (let i = 0; i < n; i++) {\n    for (let j = 0; j < n - i - 1; j++) {\n      if (arr[j] > arr[j + 1]) {\n        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];\n      }\n    }\n  }\n  return arr;\n}',
    'java': 'public static void bubbleSort(int[] arr) {\n    int n = arr.length;\n    for (int i = 0; i < n - 1; i++) {\n        for (int j = 0; j < n - i - 1; j++) {\n            if (arr[j] > arr[j + 1]) {\n                int tmp = arr[j];\n                arr[j] = arr[j + 1];\n                arr[j + 1] = tmp;\n            }\n        }\n    }\n}',
}
enc_gpt4 = tiktoken.get_encoding('cl100k_base')
enc_gpt2 = tiktoken.get_encoding('gpt2')
starcoder = AutoTokenizer.from_pretrained('bigcode/starcoder')
for lang, code in algorithms.items():
    n_gpt4 = len(enc_gpt4.encode(code))
    n_gpt2 = len(enc_gpt2.encode(code))
    n_star = len(starcoder.encode(code))
    print(f'{lang:<12}: gpt4={n_gpt4:>4}  gpt2={n_gpt2:>4}  starcoder={n_star:>4}')
```

## Indentation Token Analysis

Python indentation is semantically critical — stripping or modifying it changes program meaning. A standard 4-space indent tokenizes differently across tokenizers: GPT-4 (cl100k_base) merges consecutive spaces into a single token for common indent widths, while GPT-2 may split them into individual space tokens. Tab characters (\t) typically tokenize as a single token. Nested indentation (8 or 12 spaces for doubly or triply nested blocks) further compounds the token count, making deeply nested Python code disproportionately expensive.

```python
import tiktoken

def analyze_indentation(tokenizer_name='cl100k_base'):
    enc = tiktoken.get_encoding(tokenizer_name)
    indent_styles = {
        '2-space indent':   '  x = 1',
        '4-space indent':   '    x = 1',
        '8-space indent':   '        x = 1',
        '12-space indent':  '            x = 1',
        'tab indent':       '\tx = 1',
        'tab+4 indent':     '\t    x = 1',
    }
    print(f'Tokenizer: {tokenizer_name}')
    for label, text in indent_styles.items():
        tokens = enc.encode(text)
        decoded = [enc.decode([t]) for t in tokens]
        display = [repr(d) for d in decoded]
        print(f'  {label:<20}: {len(tokens)} tokens  {display}')

analyze_indentation('cl100k_base')
print()
analyze_indentation('gpt2')
```

## Operator and Identifier Tokenization

Identifier naming conventions interact strongly with BPE tokenization. A snake_case identifier like 'calculate_gradient_norm' typically splits at underscores, producing 3–4 tokens. A camelCase identifier like 'calculateGradientNorm' may split at case boundaries (some tokenizers treat uppercase letters as split points) or remain merged if the whole identifier appears in training data. Operators like == usually tokenize as a single token in code-aware vocabularies, while -> and => may be one or two tokens depending on the training corpus.

```python
import tiktoken

def analyze_identifiers_and_ops(tokenizer_name='cl100k_base'):
    enc = tiktoken.get_encoding(tokenizer_name)
    samples = {
        'camelCase':    'calculateGradientNorm',
        'snake_case':   'calculate_gradient_norm',
        'PascalCase':   'CalculateGradientNorm',
        'SCREAMING':    'MAX_GRADIENT_NORM',
        'eq operator':  '==',
        'ne operator':  '!=',
        'arrow (C++)':  '->',
        'fat arrow':    '=>',
        'walrus':       ':=',
        'type hint':    'list[int]',
        'decorator':    '@torch.no_grad()',
    }
    print(f'Operator/identifier tokenization ({tokenizer_name})')
    for label, text in samples.items():
        tokens = enc.encode(text)
        pieces = [enc.decode([t]) for t in tokens]
        print(f'  {label:<16}: {len(tokens)} tok  {pieces}')

analyze_identifiers_and_ops('cl100k_base')
print()
analyze_identifiers_and_ops('gpt2')
```

## Cross-Language Fertility

```python
import tiktoken

def tokens_per_line(code_snippet, enc):
    lines = [l for l in code_snippet.split('\n') if l.strip()]
    if not lines:
        return 0.0
    total = sum(len(enc.encode(l)) for l in lines)
    return total / len(lines)

enc = tiktoken.get_encoding('cl100k_base')
snippets = {
    'Python':     'def add(a, b):\n    return a + b\nresult = add(1, 2)',
    'JavaScript': 'const add = (a, b) => a + b;\nconst result = add(1, 2);',
    'Java':       'public int add(int a, int b) { return a + b; }\nint result = add(1, 2);',
    'SQL':        'SELECT id, name FROM users WHERE active = 1 ORDER BY name ASC;',
    'LaTeX':      '\\frac{\\partial L}{\\partial w} = \\sum_{i=1}^{n} x_i (y_i - \\hat{y}_i)',
    'JSON':       '{"model": "gpt-4", "temperature": 0.7, "max_tokens": 512}',
    'Regex':      '^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$',
    'Bash':       'for f in *.py; do python $f --output results/; done',
}
print(f'{"Language":<14} {"Tok/Line":>10} {"Total Tok":>10}')
for lang, code in snippets.items():
    tpl = tokens_per_line(code, enc)
    total = len(enc.encode(code))
    print(f'{lang:<14} {tpl:>10.2f} {total:>10}')
```

## Code Tokenization Characteristics

| Language | Avg Tokens/Line | Key Tokenization Artifact | Indentation Handling | Operator Splitting |
| --- | --- | --- | --- | --- |
| Python | 6–10 | Ġ prefix on space tokens; merged indent blocks | 4 spaces → 1–4 tokens (tokenizer-dependent) | == as 1 token; // as 2 tokens usually |
| JavaScript | 5–9 | { } merge with preceding token; => split | Braces not indented; space after { is separate | => may be 1–2 tokens; === is 2–3 tokens |
| Java | 7–12 | Long class/method names split at case boundaries | Braces on same or next line; indentation less semantic | -> lambda arrow: 1–2 tokens |
| SQL | 4–8 | UPPERCASE keywords often single tokens; lowercase variants split | No indentation semantics | != and <> both tokenize as 2 tokens |
| LaTeX | 8–15 | Backslash sequences: \\frac splits into 2–3 tokens | No indentation; heavy use of { } braces | _ and ^ as single tokens; subscripts split |
| JSON | 3–6 | Colon and quotes often merge with key tokens | No semantic indentation | : usually 1 token; {} and [] as 1 token each |

## Token Alignment to Source Code Lines

IDE tooling for code models — inline completions, error explanations, span highlighting — requires mapping token indices back to source line and column positions. BPE tokens do not align to line boundaries: a token may span a newline character, and a single logical line may produce dozens of tokens. To build the token-to-line mapping, reconstruct the character offset of each token by decoding prefix token sequences, then binary-search against the newline positions of the original source string.

The HumanEval benchmark uses code in a specific format: function signature followed by docstring followed by implementation. Tokenizing this format with different tokenizers produces different prompt lengths, affecting the number of completion tokens available within the model's context window. Code models fine-tuned with a specific tokenizer must use that same tokenizer at inference time — cross-tokenizer evaluation invalidates token count comparisons across papers.

## Fine-Tuning Code Models — Tokenizer Implications

> **Check Operator Merging Before Fine-Tuning**: When fine-tuning code models, check that the tokenizer correctly merges common operators in your target language — some tokenizers split '->' into 2 tokens and '=>' into 2 tokens, affecting token budget predictions by 10–20%. Run the indentation and operator analysis on a representative sample of your training code before committing to a tokenizer, and prefer code-specific vocabularies (StarCoder, CodeLlama) for code-heavy workloads to minimise fertility and maximise effective context window usage.

- Use code-specific tokenizers (StarCoder, CodeLlama) for code-heavy tasks — 15–30% lower fertility than GPT-2.
- Indentation is semantic in Python: normalise to spaces before tokenizing to avoid tab/space fertility differences.
- Operator splitting affects token budget: test ==, !=, ->, =>, := on your target tokenizer before estimating costs.
- camelCase identifiers may tokenize as 1 token if they appear frequently in training; rare identifiers always split.
- SQL UPPERCASE keywords tokenize better than lowercase variants in tokenizers trained on mixed-case corpora.
- HumanEval evaluations must match training tokenizer exactly — cross-tokenizer comparisons are invalid.

A practical code tokenization workflow: (1) sample 1000 lines of production code in your target language, (2) tokenize with each candidate tokenizer and compute mean tokens per line, (3) select the tokenizer with lowest fertility for your dominant language, (4) verify operator and identifier splitting for the 20 most common constructs in your codebase, (5) measure context window headroom with your typical prompt template. This analysis typically takes under an hour and prevents costly mis-estimates at production scale.

---

