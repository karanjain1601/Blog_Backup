---
title: "Multilingual Tokenization — Token Fertility Across Scripts and Languages"
slug: "multilingual-tokenization"
description: "Token fertility measures how many subword tokens a tokenizer produces per word across languages. Covers fertility imbalances between English and non-Latin scripts, mBERT/XLM vocabulary allocation, alpha-sampling for low-resource upsampling, and practical API cost implications."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG9rZW4gZmVydGlsaXR5IGlzIHRoZSBhdmVyYWdlIG51bWJlciBvZiBzdWJ3b3JkIHRva2VucyBhIHRva2VuaXplciBwcm9kdWNlcyBwZXIgd29yZC4gRm9yIEVuZ2xpc2gsIHZvY2FidWxhcmllcyB0cmFpbmVkIHByZWRvbWluYW50bHkgb24gRW5nbGlzaCB0ZXh0IGFjaGlldmUgZmVydGlsaXR5IG5lYXIgMS4w4oCTMS4zIHRva2VucyBwZXIgd29yZCDigJQgbW9zdCBjb21tb24gd29yZHMgYXBwZWFyIGRpcmVjdGx5IGluIHRoZSB2b2NhYnVsYXJ5LiBGb3IgbGFuZ3VhZ2VzIHdpdGggY29tcGxleCBtb3JwaG9sb2d5IG9yIG5vbi1MYXRpbiBzY3JpcHRzLCB0aGUgc2FtZSB0b2tlbml6ZXIgY2FuIHByb2R1Y2UgMuKAkzXDlyBtb3JlIHRva2VucyBmb3IgZXF1aXZhbGVudCBzZW1hbnRpYyBjb250ZW50LiBUaGlzIGltYmFsYW5jZSBkcml2ZXMgdXAgaW5mZXJlbmNlIGNvc3RzLCBjb25zdW1lcyBtb3JlIGNvbnRleHQgd2luZG93LCBhbmQgZGVncmFkZXMgbW9kZWwgcXVhbGl0eSBmb3IgbG93LXJlc291cmNlIGxhbmd1YWdlcyBpbiBwcm9kdWN0aW9uIGRlcGxveW1lbnRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRva2VuIEZlcnRpbGl0eSDigJQgRW5nbGlzaCBCYXNlbGluZSBhbmQgU2NyaXB0IENvbXBhcmlzb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZlcnRpbGl0eSBpcyBmb3JtYWxseSBkZWZpbmVkIGFzIHRva2VucyBwcm9kdWNlZCBwZXIgd29yZC4gRW5nbGlzaCBhY2hpZXZlcyBuZWFyLWJhc2VsaW5lIGZlcnRpbGl0eSBiZWNhdXNlIGl0cyBtb3JwaG9sb2d5IGlzIHNpbXBsZSBhbmQgY29ycHVzIGRvbWluYW5jZSBlbnN1cmVzIHJpY2ggdm9jYWJ1bGFyeSBjb3ZlcmFnZS4gVGhhaSBsYWNrcyB3b3JkIGJvdW5kYXJpZXMgYW5kIHVzZXMgY29tcG91bmQgY2hhcmFjdGVycywgcmVhY2hpbmcgM+KAkzXDlyBFbmdsaXNoIGZlcnRpbGl0eS4gQXJhYmljXHUwMDI3cyByaWNoIG1vcnBob2xvZ3kgYW5kIHJpZ2h0LXRvLWxlZnQgc2NyaXB0IHByb2R1Y2Ugcm91Z2hseSAyw5cgZmVydGlsaXR5LiBGaW5uaXNoXHUwMDI3cyBhZ2dsdXRpbmF0aXZlIG1vcnBob2xvZ3kgY2F1c2VzIGNvbW1vbiBjb21wb3VuZCB3b3JkcyB0byBzcGxpdCBpbnRvIDPigJM0IHRva2VucyBkZXNwaXRlIHVzaW5nIHRoZSBMYXRpbiBhbHBoYWJldC4gQ2hpbmVzZSBhbmQgSmFwYW5lc2UgdHlwaWNhbGx5IHlpZWxkIDLigJMzw5cgZmVydGlsaXR5IHNpbmNlIGluZGl2aWR1YWwgY2hhcmFjdGVycyBlbmNvZGUgbW9yZSBtZWFuaW5nIHBlciBzbG90IHRoYW4gRW5nbGlzaCB3b3JkcywgeWV0IHJlcXVpcmUgMuKAkzMgdG9rZW5zIGVhY2ggaW4gbW9zdCBCUEUgdm9jYWJ1bGFyaWVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNyb3NzLUxpbmd1YWwgRmVydGlsaXR5IEFuYWx5c2lzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0aWt0b2tlblxuXG5kZWYgY29tcHV0ZV9mZXJ0aWxpdHkoZW5jb2RlX2ZuLCB0ZXh0c19ieV9sYW5nKTpcbiAgICAjIGF2ZyB0b2tlbnMgcGVyIGNoYXJhY3RlciBmb3IgZWFjaCBsYW5ndWFnZVxuICAgIHJlc3VsdHMgPSB7fVxuICAgIGZvciBsYW5nLCB0ZXh0cyBpbiB0ZXh0c19ieV9sYW5nLml0ZW1zKCk6XG4gICAgICAgIHRvdGFsX3Rva2VucyA9IHN1bShsZW4oZW5jb2RlX2ZuKHQpKSBmb3IgdCBpbiB0ZXh0cylcbiAgICAgICAgdG90YWxfY2hhcnMgPSBzdW0obGVuKHQpIGZvciB0IGluIHRleHRzKVxuICAgICAgICByZXN1bHRzW2xhbmddID0gdG90YWxfdG9rZW5zIC8gbWF4KHRvdGFsX2NoYXJzLCAxKVxuICAgIHJldHVybiByZXN1bHRzXG5cbmVuYyA9IHRpa3Rva2VuLmdldF9lbmNvZGluZyhcdTAwMjdjbDEwMGtfYmFzZVx1MDAyNylcbnNhbXBsZV90ZXh0cyA9IHtcbiAgICBcdTAwMjdlblx1MDAyNzogW1x1MDAyN1RoZSBhdHRlbnRpb24gbWVjaGFuaXNtIHJldm9sdXRpb25pemVkIE5MUC5cdTAwMjcsIFx1MDAyN21hY2hpbmUgbGVhcm5pbmcgbW9kZWxzXHUwMDI3XSxcbiAgICBcdTAwMjd6aFx1MDAyNzogW1x1MDAyN+azqOaEj+WKm+acuuWItuaUueWPmOS6huiHqueEtuivreiogOWkhOeQhuOAglx1MDAyNywgXHUwMDI35py65Zmo5a2m5LmgXHUwMDI3XSxcbiAgICBcdTAwMjdhclx1MDAyNzogW1x1MDAyN9ii2YTZitipINin2YTYp9mG2KrYqNin2Ycg2YHZiiDZhdi52KfZhNis2Kkg2KfZhNmE2LrYqSDYp9mE2LfYqNmK2LnZitipLlx1MDAyN10sXG4gICAgXHUwMDI3dGhcdTAwMjc6IFtcdTAwMjfguIHguKXguYTguIHguITguKfguLLguKHguKrguJnguYPguIjguIHguLLguKPguJvguKPguLDguKHguKfguKXguJzguKXguKDguLLguKnguLLguJjguKPguKPguKHguIrguLLguJXguLRcdTAwMjddLFxuICAgIFx1MDAyN2ZpXHUwMDI3OiBbXHUwMDI3SHVvbWlva3lreSBtdWxsaXN0aSBsdW9ubm9sbGlzZW4ga2llbGVuIGthc2l0dGVseW4uXHUwMDI3LCBcdTAwMjdrb25lb3BwaW1pc21hbGxpdFx1MDAyN10sXG4gICAgXHUwMDI3aGlcdTAwMjc6IFtcdTAwMjfgpKfgpY3gpK/gpL7gpKgg4KSk4KSC4KSk4KWN4KSwIOCkqOClhyDgpI/gpKjgpI/gpLLgpKrgpYAg4KSu4KWH4KSCIOCkleCljeCksOCkvuCkguCkpOCkvyDgpLLgpL4g4KSm4KWA4KWkXHUwMDI3XSxcbiAgICBcdTAwMjdrb1x1MDAyNzogW1x1MDAyN+yjvOydmCDrqZTsu6Tri4jsppjsnbQg7J6Q7Jew7Ja0IOyymOumrOulvCDtmIHsi6DtlojsirXri4jri6QuXHUwMDI3XSxcbiAgICBcdTAwMjdkZVx1MDAyNzogW1x1MDAyN0RlciBBdWZtZXJrc2Fta2VpdHNtZWNoYW5pc211cyByZXZvbHV0aW9uaWVydGUgTkxQLUZvcnNjaHVuZy5cdTAwMjddLFxuICAgIFx1MDAyN2phXHUwMDI3OiBbXHUwMDI35rOo5oSP5qmf5qeL44Gv6Ieq54S26KiA6Kqe5Yem55CG44Gr6Z2p5ZG944KS44KC44Gf44KJ44GX44Gf44CCXHUwMDI3XSxcbiAgICBcdTAwMjdydVx1MDAyNzogW1x1MDAyN9Cc0LXRhdCw0L3QuNC30Lwg0LLQvdC40LzQsNC90LjRjyDQv9GA0L7QuNC30LLRkdC7INGA0LXQstC+0LvRjtGG0LjRjiDQsiDQvtCx0YDQsNCx0L7RgtC60LUg0Y/Qt9GL0LrQsC5cdTAwMjddLFxufVxuZmVydGlsaXR5ID0gY29tcHV0ZV9mZXJ0aWxpdHkoZW5jLmVuY29kZSwgc2FtcGxlX3RleHRzKVxuZW5fcmF0ZSA9IGZlcnRpbGl0eVtcdTAwMjdlblx1MDAyN11cbnByaW50KFx1MDAyN0xhbmd1YWdlICBUb2svQ2hhciAgUmVsYXRpdmVcdTAwMjcpXG5mb3IgbGFuZywgcmF0ZSBpbiBmZXJ0aWxpdHkuaXRlbXMoKTpcbiAgICByZWwgPSByYXRlIC8gZW5fcmF0ZVxuICAgIHByaW50KGZcdTAwMjd7bGFuZzpcdTAwM2MxMH0ge3JhdGU6LjRmfSAgIHtyZWw6LjJmfXhcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVm9jYWJ1bGFyeSBDb3ZlcmFnZSBpbiBNdWx0aWxpbmd1YWwgTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBtQkVSVCBhbmQgWExNLVIsIHRoZSBzaGFyZWQgdm9jYWJ1bGFyeSBpcyBhbGxvY2F0ZWQgcHJvcG9ydGlvbmFsbHkgdG8gY29ycHVzIHNpemUgYWZ0ZXIgYWxwaGEtc21vb3RoaW5nLiBFbmdsaXNoLCBDaGluZXNlLCBhbmQgR2VybWFuIHJlY2VpdmUgdGhlIGxhcmdlc3Qgdm9jYWJ1bGFyeSBzbGljZXMuIExhbmd1YWdlcyBsaWtlIFN3YWhpbGkgb3IgQnVybWVzZSwgd2l0aCBzbWFsbCB3ZWIgY29ycG9yYSwgcmVjZWl2ZSBmYXIgZmV3ZXIgdm9jYWJ1bGFyeSBzbG90cyBhbmQgcmVseSBvbiBieXRlLWZhbGxiYWNrIG9yIGNoYXJhY3Rlci1sZXZlbCB0b2tlbml6YXRpb24uIFRoaXMgY3JlYXRlcyBhIHZvY2FidWxhcnkgY292ZXJhZ2UgZGlzcGFyaXR5OiBlcXVpdmFsZW50IGNvbmNlcHRzIHJlcXVpcmUgbW9yZSB0b2tlbnMgaW4gbG93LXJlc291cmNlIGxhbmd1YWdlcywgZGVncmFkaW5nIG1vZGVsIGNhcGFjaXR5IGFuZCBnZW5lcmF0aW9uIHRocm91Z2hwdXQuIFRoZSBwcm9wb3J0aW9uIG9mIGEgbGFuZ3VhZ2VcdTAwMjdzIHZvY2FidWxhcnkgY292ZXJhZ2UgZGlyZWN0bHkgY29ycmVsYXRlcyB3aXRoIGl0cyBkb3duc3RyZWFtIHRhc2sgcGVyZm9ybWFuY2UgaW4gbXVsdGlsaW5ndWFsIGJlbmNobWFya3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvVG9rZW5pemVyXG5cbmRlZiBhbmFseXplX3ZvY2FiX2NvdmVyYWdlKG1vZGVsX25hbWUsIHRleHRzX2J5X2xhbmcpOlxuICAgIHRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG4gICAgcmVzdWx0cyA9IHt9XG4gICAgZm9yIGxhbmcsIHRleHRzIGluIHRleHRzX2J5X2xhbmcuaXRlbXMoKTpcbiAgICAgICAgYWxsX2lkcyA9IFtdXG4gICAgICAgIGZvciB0ZXh0IGluIHRleHRzOlxuICAgICAgICAgICAgaWRzID0gdG9rZW5pemVyLmVuY29kZSh0ZXh0LCBhZGRfc3BlY2lhbF90b2tlbnM9RmFsc2UpXG4gICAgICAgICAgICBhbGxfaWRzLmV4dGVuZChpZHMpXG4gICAgICAgIHVua19pZCA9IHRva2VuaXplci51bmtfdG9rZW5faWRcbiAgICAgICAgdW5rX2NvdW50ID0gc3VtKDEgZm9yIHQgaW4gYWxsX2lkcyBpZiB0ID09IHVua19pZClcbiAgICAgICAgcmVzdWx0c1tsYW5nXSA9IHtcbiAgICAgICAgICAgIFx1MDAyN3RvdGFsX3Rva2Vuc1x1MDAyNzogbGVuKGFsbF9pZHMpLFxuICAgICAgICAgICAgXHUwMDI3dW5pcXVlX3R5cGVzXHUwMDI3OiBsZW4oc2V0KGFsbF9pZHMpKSxcbiAgICAgICAgICAgIFx1MDAyN3Vua19yYXRlXHUwMDI3OiB1bmtfY291bnQgLyBtYXgobGVuKGFsbF9pZHMpLCAxKSxcbiAgICAgICAgfVxuICAgIHJldHVybiByZXN1bHRzXG5cbm1vZGVsX25hbWUgPSBcdTAwMjd4bG0tcm9iZXJ0YS1iYXNlXHUwMDI3XG50ZXh0cyA9IHtcbiAgICBcdTAwMjdlblx1MDAyNzogW1x1MDAyN1RyYW5zZm9ybWVyIGFyY2hpdGVjdHVyZSB3aXRoIHNlbGYtYXR0ZW50aW9uIGxheWVycy5cdTAwMjddLFxuICAgIFx1MDAyN3poXHUwMDI3OiBbXHUwMDI35YW35pyJ6Ieq5rOo5oSP5Yqb5bGC55qE5Y+Y5o2i5Zmo5p625p6E44CCXHUwMDI3XSxcbiAgICBcdTAwMjdhclx1MDAyNzogW1x1MDAyN9io2YbZitipINin2YTZhdit2YjZhCDZhdi5INi32KjZgtin2Kog2KfZhNin2YbYqtio2KfZhyDYp9mE2LDYp9iq2YouXHUwMDI3XSxcbiAgICBcdTAwMjdzd1x1MDAyNzogW1x1MDAyN011dW5kbyB3YSB0cmFuc2Zvcm1lciBuYSB0YWJha2EgemEga3VqaXppbmdhdGlhLlx1MDAyN10sXG4gICAgXHUwMDI3Z3VcdTAwMjc6IFtcdTAwMjfgqp/gq43gqrDgqr7gqqjgq43gqrjgqqvgq4vgqrDgq43gqq7gqrAg4KqG4Kqw4KuN4KqV4Kq/4Kqf4KuH4KqV4KuN4Kqa4KqwIOCquOCrjeCqtS3gqqfgq43gqq/gqr7gqqgg4Kq44KuN4Kqk4Kqw4KuLIOCquOCqvuCqpeCrhy5cdTAwMjddLFxufVxuY292ZXJhZ2UgPSBhbmFseXplX3ZvY2FiX2NvdmVyYWdlKG1vZGVsX25hbWUsIHRleHRzKVxucHJpbnQoZlx1MDAyN0NvdmVyYWdlOiB7bW9kZWxfbmFtZX1cdTAwMjcpXG5mb3IgbGFuZywgc3RhdHMgaW4gY292ZXJhZ2UuaXRlbXMoKTpcbiAgICB0b3RhbCA9IHN0YXRzW1x1MDAyN3RvdGFsX3Rva2Vuc1x1MDAyN11cbiAgICB1bmsgPSBzdGF0c1tcdTAwMjd1bmtfcmF0ZVx1MDAyN11cbiAgICB1bmlxID0gc3RhdHNbXHUwMDI3dW5pcXVlX3R5cGVzXHUwMDI3XVxuICAgIHByaW50KGZcdTAwMjcgIHtsYW5nfToge3RvdGFsfSB0b2tlbnMsIHVuaXF1ZT17dW5pcX0sIHVua19yYXRlPXt1bms6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW1wZXJhdHVyZS1CYXNlZCBVcHNhbXBsaW5nIGZvciBWb2NhYnVsYXJ5IFRyYWluaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbHBoYS1zYW1wbGluZyBhZGp1c3RzIGhvdyBtYW55IHRva2VucyBlYWNoIGxhbmd1YWdlIGNvbnRyaWJ1dGVzIGR1cmluZyB2b2NhYnVsYXJ5IHRyYWluaW5nLiBXaXRoIGFscGhhPTEuMCwgc2FtcGxpbmcgaXMgcHJvcG9ydGlvbmFsIHRvIGNvcnB1cyBzaXplIOKAlCBsYXJnZSBjb3Jwb3JhIGRvbWluYXRlLiBXaXRoIGFscGhhPTAuNyAoZGVmYXVsdCBpbiBYTE0gYW5kIG1CRVJUKSwgc21hbGwgY29ycG9yYSBhcmUgdXBzYW1wbGVkOiBhIGxhbmd1YWdlIHdpdGggMS8xMDAgdGhlIGRhdGEgb2YgRW5nbGlzaCByZWNlaXZlcyByb3VnaGx5IDEvMTAwXjAuNyDiiYggMS8yMSBvZiB0aGUgcHJvYmFiaWxpdHkgbWFzcyBpbnN0ZWFkIG9mIDEvMTAwLiBUaGlzIGdpdmVzIGxvdy1yZXNvdXJjZSBsYW5ndWFnZXMgbW9yZSB2b2NhYnVsYXJ5IGNvdmVyYWdlIGF0IHRoZSBjb3N0IG9mIHNsaWdodGx5IGxvd2VyIHZvY2FidWxhcnkgZWZmaWNpZW5jeSBmb3IgaGlnaC1yZXNvdXJjZSBsYW5ndWFnZXMuIFRoZSB0eXBpY2FsIHJhbmdlIGlzIGFscGhhPTAuNSB0byAwLjc7IGFscGhhPTEuMCByZXByb2R1Y2VzIHJhdyBwcm9wb3J0aW9uYWwgc2FtcGxpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgYWxwaGFfc2FtcGxpbmdfd2VpZ2h0cyhjb3JwdXNfc2l6ZXMsIGFscGhhPTAuNyk6XG4gICAgIyBhbHBoYT0xLjA6IHByb3BvcnRpb25hbCB0byBjb3JwdXMgc2l6ZSAoZmF2b3VycyBsYXJnZSBjb3Jwb3JhKVxuICAgICMgYWxwaGE9MC4wOiB1bmlmb3JtIGFjcm9zcyBhbGwgbGFuZ3VhZ2VzXG4gICAgIyBhbHBoYT0wLjc6IHR5cGljYWwgbXVsdGlsaW5ndWFsIGNvbXByb21pc2UgdXNlZCBpbiBYTE0vbUJFUlRcbiAgICBsYW5ncyA9IGxpc3QoY29ycHVzX3NpemVzLmtleXMoKSlcbiAgICBzaXplcyA9IG5wLmFycmF5KFtjb3JwdXNfc2l6ZXNbbF0gZm9yIGwgaW4gbGFuZ3NdLCBkdHlwZT1mbG9hdClcbiAgICBzbW9vdGhlZCA9IHNpemVzICoqIGFscGhhXG4gICAgcHJvYnMgPSBzbW9vdGhlZCAvIHNtb290aGVkLnN1bSgpXG4gICAgcmV0dXJuIGRpY3QoemlwKGxhbmdzLCBwcm9icykpXG5cbmNvcnB1c19zaXplcyA9IHtcbiAgICBcdTAwMjdlblx1MDAyNzogNTBfMDAwXzAwMCwgXHUwMDI3emhcdTAwMjc6IDEwXzAwMF8wMDAsIFx1MDAyN2FyXHUwMDI3OiAzXzAwMF8wMDAsXG4gICAgXHUwMDI3c3dcdTAwMjc6IDIwMF8wMDAsICAgIFx1MDAyN215XHUwMDI3OiAxMDBfMDAwLCAgICBcdTAwMjd0aFx1MDAyNzogMV81MDBfMDAwLFxuICAgIFx1MDAyN2ZpXHUwMDI3OiAyXzAwMF8wMDAsICBcdTAwMjdoaVx1MDAyNzogNF8wMDBfMDAwLFxufVxucHJpbnQoXHUwMDI3TGFuZ3VhZ2UgIENvcnB1cyAgICAgICBwKGE9MS4wKSAgcChhPTAuNykgIHAoYT0wLjMpXHUwMDI3KVxuZm9yIGxhbmcsIHNpemUgaW4gY29ycHVzX3NpemVzLml0ZW1zKCk6XG4gICAgcDEwID0gYWxwaGFfc2FtcGxpbmdfd2VpZ2h0cyhjb3JwdXNfc2l6ZXMsIGFscGhhPTEuMClbbGFuZ11cbiAgICBwMDcgPSBhbHBoYV9zYW1wbGluZ193ZWlnaHRzKGNvcnB1c19zaXplcywgYWxwaGE9MC43KVtsYW5nXVxuICAgIHAwMyA9IGFscGhhX3NhbXBsaW5nX3dlaWdodHMoY29ycHVzX3NpemVzLCBhbHBoYT0wLjMpW2xhbmddXG4gICAgcHJpbnQoZlx1MDAyN3tsYW5nOlx1MDAzYzV9ICB7c2l6ZTpcdTAwM2UxMix9ICB7cDEwOi40Zn0gICAge3AwNzouNGZ9ICAgIHtwMDM6LjRmfVx1MDAyNylcbnN3XzEwID0gYWxwaGFfc2FtcGxpbmdfd2VpZ2h0cyhjb3JwdXNfc2l6ZXMsIDEuMClbXHUwMDI3c3dcdTAwMjddXG5zd18wNyA9IGFscGhhX3NhbXBsaW5nX3dlaWdodHMoY29ycHVzX3NpemVzLCAwLjcpW1x1MDAyN3N3XHUwMDI3XVxucHJpbnQoZlx1MDAyN1N3YWhpbGkgdXBzYW1wbGluZyBnYWluIChhPTAuNyB2cyBhPTEuMCk6IHtzd18wNy9zd18xMDouMWZ9eFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aWxpbmd1YWwgVG9rZW5pemVyIFVzYWdlIHdpdGggbVQ1IGFuZCBYTE0tUiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG5kZWYgdG9rZW5pemVfbXVsdGlsaW5ndWFsKHRleHRfYnlfbGFuZywgbW9kZWxfbmFtZSk6XG4gICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSlcbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgbGFuZywgdGV4dCBpbiB0ZXh0X2J5X2xhbmcuaXRlbXMoKTpcbiAgICAgICAgaWRzID0gdG9rZW5pemVyLmVuY29kZSh0ZXh0LCBhZGRfc3BlY2lhbF90b2tlbnM9RmFsc2UpXG4gICAgICAgIHRva2VucyA9IHRva2VuaXplci5jb252ZXJ0X2lkc190b190b2tlbnMoaWRzKVxuICAgICAgICByZXN1bHRzW2xhbmddID0ge1x1MDAyN2lkc1x1MDAyNzogaWRzLCBcdTAwMjd0b2tlbnNcdTAwMjc6IHRva2VucywgXHUwMDI3blx1MDAyNzogbGVuKGlkcyl9XG4gICAgcmV0dXJuIHJlc3VsdHNcblxuc2VudGVuY2UgPSB7XG4gICAgXHUwMDI3ZW5cdTAwMjc6IFx1MDAyN1RoZSB0b2tlbml6ZXIgc3BsaXRzIHRleHQgaW50byBzdWJ3b3JkIHVuaXRzLlx1MDAyNyxcbiAgICBcdTAwMjd6aFx1MDAyNzogXHUwMDI35YiG6K+N5Zmo5bCG5paH5pys5ouG5YiG5Li65a2Q6K+N5Y2V5YWD44CCXHUwMDI3LFxuICAgIFx1MDAyN2FyXHUwMDI3OiBcdTAwMjfZitmC2LPZhSDYp9mE2YXYrdmE2YQg2KfZhNmG2LXZiiDYp9mE2YbYtSDYpdmE2Ykg2YjYrdiv2KfYqiDZg9mE2YXYqSDZgdix2LnZitipLlx1MDAyNyxcbiAgICBcdTAwMjdqYVx1MDAyNzogXHUwMDI344OI44O844Kv44OK44Kk44K244O844Gv44OG44Kt44K544OI44KS44K144OW44Ov44O844OJ5Y2Y5L2N44Gr5YiG5Ymy44GX44G+44GZ44CCXHUwMDI3LFxuICAgIFx1MDAyN2ZpXHUwMDI3OiBcdTAwMjdUb2tlbmlzYWF0dG9yaSBqYWthYSB0ZWtzdGluIGFsaW9zaWluLlx1MDAyNyxcbiAgICBcdTAwMjd0aFx1MDAyNzogXHUwMDI34LiV4Lix4Lin4LmB4Lii4LiB4LiE4Liz4LmB4Lia4LmI4LiH4LiC4LmJ4Lit4LiE4Lin4Liy4Lih4Lit4Lit4LiB4LmA4Lib4LmH4LiZ4Lir4LiZ4LmI4Lin4Lii4Lii4LmI4Lit4LiiXHUwMDI3LFxufVxuZm9yIG1vZGVsIGluIFtcdTAwMjdnb29nbGUvbXQ1LXNtYWxsXHUwMDI3LCBcdTAwMjd4bG0tcm9iZXJ0YS1iYXNlXHUwMDI3XTpcbiAgICBwcmludChmXHUwMDI3TW9kZWw6IHttb2RlbH1cdTAwMjcpXG4gICAgcmVzdWx0cyA9IHRva2VuaXplX211bHRpbGluZ3VhbChzZW50ZW5jZSwgbW9kZWwpXG4gICAgZm9yIGxhbmcsIGluZm8gaW4gcmVzdWx0cy5pdGVtcygpOlxuICAgICAgICBuX3RvayA9IGluZm9bXHUwMDI3blx1MDAyN11cbiAgICAgICAgdG9rcyA9IGluZm9bXHUwMDI3dG9rZW5zXHUwMDI3XVs6Nl1cbiAgICAgICAgcHJpbnQoZlx1MDAyNyAge2xhbmd9OiB7bl90b2t9IHRva2VucyB8IHt0b2tzfVx1MDAyNylcbiAgICBwcmludCgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVG9rZW4gRmVydGlsaXR5IGJ5IExhbmd1YWdlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkxhbmd1YWdlIiwiU2NyaXB0IEZhbWlseSIsIlRva2Vucy9Xb3JkIChhcHByb3gpIiwiUmVsYXRpdmUgdG8gRW5nbGlzaCIsIlRva2VuaXplciBTZW5zaXRpdml0eSJdLCJyb3dzIjpbWyJFbmdsaXNoIiwiTGF0aW4iLCIxLjIiLCIxLjB4IChiYXNlbGluZSkiLCJMb3ciXSxbIlNwYW5pc2giLCJMYXRpbiIsIjEuMyIsIjEuMXgiLCJMb3ciXSxbIkZyZW5jaCIsIkxhdGluIiwiMS40IiwiMS4yeCIsIkxvdyJdLFsiR2VybWFuIiwiTGF0aW4gKGNvbXBvdW5kcykiLCIxLjgiLCIxLjV4IiwiTWVkaXVtIl0sWyJDaGluZXNlIiwiTG9nb2dyYXBoaWMgKENKSykiLCIyLjDigJMyLjUiLCIxLjh4IiwiSGlnaCJdLFsiSmFwYW5lc2UiLCJDSksgKyBLYW5hIiwiMi4w4oCTMy4wIiwiMi4xeCIsIkhpZ2giXSxbIktvcmVhbiIsIkhhbmd1bCAoYWdnbHV0aW5hdGl2ZSkiLCIyLjXigJMzLjUiLCIyLjR4IiwiSGlnaCJdLFsiQXJhYmljIiwiQWJqYWQgKFJUTCkiLCIyLjDigJMyLjUiLCIyLjF4IiwiSGlnaCJdLFsiVGhhaSIsIkFidWdpZGEgKG5vIHNwYWNlcykiLCIzLjDigJM1LjAiLCIzLjV4IiwiVmVyeSBIaWdoIl0sWyJIaW5kaSIsIkRldmFuYWdhcmkiLCIyLjDigJMzLjAiLCIyLjN4IiwiSGlnaCJdLFsiRmlubmlzaCIsIkxhdGluIChhZ2dsdXRpbmF0aXZlKSIsIjEuOOKAkzIuNSIsIjEuN3giLCJNZWRpdW0tSGlnaCJdLFsiQ29kZSAoUHl0aG9uKSIsIkFTQ0lJICsgc3ltYm9scyIsIjEuMOKAkzEuNSIsIjEuMXgiLCJMb3cgKHRva2VuaXplci1kZXBlbmRlbnQpIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJaZXJvLVNob3QgQ3Jvc3MtTGluZ3VhbCBUcmFuc2ZlciBhbmQgQ29kZS1Td2l0Y2hpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ilplcm8tc2hvdCBjcm9zcy1saW5ndWFsIHRyYW5zZmVyIOKAlCB0cmFpbmluZyBvbiBFbmdsaXNoIGFuZCBldmFsdWF0aW5nIG9uIGFub3RoZXIgbGFuZ3VhZ2Ug4oCUIHdvcmtzIHBhcnRseSBiZWNhdXNlIG11bHRpbGluZ3VhbCBtb2RlbHMgc2hhcmUgc3Vid29yZCB0b2tlbnMgZm9yIGNvZ25hdGVzLCB0ZWNobmljYWwgdGVybXMsIG5hbWVkIGVudGl0aWVzLCBhbmQgbnVtZXJhbHMuIEVuZ2xpc2ggXHUwMDI3dHJhbnNmb3JtZXJcdTAwMjcgYW5kIEdlcm1hbiBcdTAwMjdUcmFuc2Zvcm1lclx1MDAyNyBvZnRlbiBtYXAgdG8gaWRlbnRpY2FsIHRva2Vucy4gVVJMcywgY29kZSBpZGVudGlmaWVycywgYW5kIHByb3BlciBub3VucyBhcmUgZnJlcXVlbnRseSBpZGVudGljYWwgYWNyb3NzIGxhbmd1YWdlcywgY3JlYXRpbmcgc3Ryb25nIGNyb3NzLWxpbmd1YWwgYW5jaG9ycyBpbiB0aGUgZW1iZWRkaW5nIHNwYWNlLiBUaGUgcHJvcG9ydGlvbiBvZiBzaGFyZWQgdG9rZW5zIGJldHdlZW4gYSBsYW5ndWFnZSBwYWlyIHN0cm9uZ2x5IGNvcnJlbGF0ZXMgd2l0aCB6ZXJvLXNob3QgdHJhbnNmZXIgcGVyZm9ybWFuY2Ugb24gYmVuY2htYXJrcyBsaWtlIFhUUkVNRSBhbmQgWEdMVUUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb2RlLXN3aXRjaGluZyByZWZlcnMgdG8gbWl4ZWQtbGFuZ3VhZ2Ugc2VxdWVuY2VzIHdoZXJlIHVzZXJzIHN3aXRjaCBsYW5ndWFnZXMgd2l0aGluIGEgc2luZ2xlIHByb21wdC4gU2VudGVuY2VQaWVjZSBoYW5kbGVzIHRoaXMgdmlhIGJ5dGUtZmFsbGJhY2s6IGFueSBjaGFyYWN0ZXIgbm90IGluIHRoZSB0cmFpbmVkIHZvY2FidWxhcnkgaXMgZW5jb2RlZCBhcyBpdHMgaW5kaXZpZHVhbCBVVEYtOCBieXRlcyAoZS5nLiwgXHUwMDNjMHhFNFx1MDAzZVx1MDAzYzB4QjhcdTAwM2VcdTAwM2MweEFEXHUwMDNlKSwgZW5zdXJpbmcgbm8gb3V0LW9mLXZvY2FidWxhcnkgZmFpbHVyZXMgYXQgdGhlIGNvc3Qgb2YgdmVyeSBoaWdoIGZlcnRpbGl0eSBmb3IgcmFyZSBzY3JpcHRzLiBMYW5nSUQgcHJlZml4IHRva2VucyBsaWtlIF9fZW5fXyBvciBfX3poX18gY2FuIGJlIHByZXBlbmRlZCB0byBzaWduYWwgdGhlIHRhcmdldCBsYW5ndWFnZSwgZ3VpZGluZyBtVDUgYW5kIE5MTEIgbW9kZWxzIHRvd2FyZCB0aGUgY29ycmVjdCBnZW5lcmF0aW9uIGxhbmd1YWdlIHdpdGhvdXQgY2hhbmdpbmcgdGhlIHRva2VuaXplclx1MDAyN3Mgdm9jYWJ1bGFyeSBhbGxvY2F0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFQSSBDb3N0IGFuZCBJbmZyYXN0cnVjdHVyZSBJbXBsaWNhdGlvbnMifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkFQSSBDb3N0IFZhcmllcyAz4oCTNXggYnkgTGFuZ3VhZ2UiLCJjb250ZW50IjoiQVBJIGNvc3QgZm9yIG11bHRpbGluZ3VhbCBMTE0gYXBwbGljYXRpb25zIGNhbiB2YXJ5IDPigJM1eCBiYXNlZCBvbiBsYW5ndWFnZSDigJQgYWx3YXlzIGJlbmNobWFyayB0b2tlbiBjb3VudHMgaW4geW91ciB0YXJnZXQgbGFuZ3VhZ2VzIGJlZm9yZSBlc3RpbWF0aW5nIGluZnJhc3RydWN0dXJlIGNvc3RzLiBBIFRoYWkgb3IgQXJhYmljIHJlc3BvbnNlIHdpdGggZXF1aXZhbGVudCBzZW1hbnRpYyBjb250ZW50IHRvIGFuIEVuZ2xpc2ggcmVzcG9uc2UgY29uc3VtZXMgcHJvcG9ydGlvbmFsbHkgbW9yZSB0b2tlbnMsIGRpcmVjdGx5IGluY3JlYXNpbmcgcGVyLXJlcXVlc3QgY29zdCBhbmQgcmVkdWNpbmcgZWZmZWN0aXZlIGNvbnRleHQgd2luZG93IGNhcGFjaXR5LiBVc2UgdGhlIHRva2VuaXplclx1MDAyN3MgZW5jb2RlKCkgbWV0aG9kIG9uIHJlcHJlc2VudGF0aXZlIHByb2R1Y3Rpb24gc2FtcGxlcyBpbiBlYWNoIHRhcmdldCBsYW5ndWFnZSBiZWZvcmUgY29tbWl0dGluZyB0byBhbiBBUEkgcHJpY2luZyB0aWVyLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRmVydGlsaXR5IGFmZmVjdHMgQVBJIHByaWNpbmc6IGNoYXJnZS1wZXItdG9rZW4gQVBJcyBjb3N0IDPigJM1eCBtb3JlIGZvciBoaWdoLWZlcnRpbGl0eSBsYW5ndWFnZXMgYXQgZXF1YWwgY29udGVudC4iLCJDb250ZXh0IHdpbmRvdzogYSA0MDk2LXRva2VuIHdpbmRvdyBob2xkcyBzaWduaWZpY2FudGx5IGxlc3MgY29udGVudCBmb3IgQXJhYmljIG9yIFRoYWkgdGhhbiBmb3IgRW5nbGlzaC4iLCJHZW5lcmF0aW9uIGxhdGVuY3k6IGhpZ2hlciB0b2tlbiBjb3VudHMgaW5jcmVhc2UgYXV0b3JlZ3Jlc3NpdmUgZ2VuZXJhdGlvbiB0aW1lIHByb3BvcnRpb25hbGx5LiIsIkJhdGNoaW5nIGVmZmljaWVuY3k6IG1peGVkLWxhbmd1YWdlIGJhdGNoZXMgaGF2ZSB2YXJpYWJsZSBzZXF1ZW5jZSBsZW5ndGhzLCByZWR1Y2luZyBHUFUgdXRpbGl6YXRpb24uIiwiVm9jYWJ1bGFyeSBhbGxvY2F0aW9uOiByZXNlcnZlIG1pbmltdW0gdm9jYWJ1bGFyeSBzbG90cyBwZXIgc2NyaXB0IHdoZW4gdHJhaW5pbmcgY3VzdG9tIG11bHRpbGluZ3VhbCB0b2tlbml6ZXJzLiIsIkJlbmNobWFyayBmZXJ0aWxpdHkgb24gcmVhbCBwcm9kdWN0aW9uIHNhbXBsZXMg4oCUIHN5bnRoZXRpYyB0ZXN0IHNlbnRlbmNlcyBvZnRlbiB1bmRlcmVzdGltYXRlIHJlYWwtd29ybGQgZmVydGlsaXR5LiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByYWN0aWNhbCBtaXRpZ2F0aW9uIHN0cmF0ZWdpZXMgaW5jbHVkZSB1c2luZyBsYW5ndWFnZS1zcGVjaWZpYyB0b2tlbml6ZXJzIGZvciBzaW5nbGUtbGFuZ3VhZ2UgZGVwbG95bWVudHMgKGFjaGlldmluZyBsb3dlciBmZXJ0aWxpdHkgdGhhbiBtdWx0aWxpbmd1YWwgdG9rZW5pemVycyksIGNvbXByZXNzaW5nIHByb21wdHMgYnkgcmVtb3ZpbmcgcmVkdW5kYW50IHRva2VucyBiZWZvcmUgQVBJIGNhbGxzLCBhbmQgbW9uaXRvcmluZyBwZXItbGFuZ3VhZ2UgdG9rZW4gY291bnRzIGluIHByb2R1Y3Rpb24gb2JzZXJ2YWJpbGl0eSBkYXNoYm9hcmRzLiBGb3IgbVQ1IGFuZCBOTExCLWJhc2VkIGRlcGxveW1lbnRzLCB0aGUgdG9rZW5pemVycyBhcmUgc3BlY2lmaWNhbGx5IGNhbGlicmF0ZWQgZm9yIG11bHRpbGluZ3VhbCBjb3ZlcmFnZSwgYWNoaWV2aW5nIG1hdGVyaWFsbHkgbG93ZXIgZmVydGlsaXR5IGZvciBub24tRW5nbGlzaCBsYW5ndWFnZXMgdGhhbiBHUFQtc2VyaWVzIHRva2VuaXplcnMgdHJhaW5lZCBwcmVkb21pbmFudGx5IG9uIEVuZ2xpc2ggY29ycG9yYS4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Multilingual Tokenization — Token Fertility Across Scripts and Languages

Token fertility is the average number of subword tokens a tokenizer produces per word. For English, vocabularies trained predominantly on English text achieve fertility near 1.0–1.3 tokens per word — most common words appear directly in the vocabulary. For languages with complex morphology or non-Latin scripts, the same tokenizer can produce 2–5× more tokens for equivalent semantic content. This imbalance drives up inference costs, consumes more context window, and degrades model quality for low-resource languages in production deployments.

## Token Fertility — English Baseline and Script Comparison

Fertility is formally defined as tokens produced per word. English achieves near-baseline fertility because its morphology is simple and corpus dominance ensures rich vocabulary coverage. Thai lacks word boundaries and uses compound characters, reaching 3–5× English fertility. Arabic's rich morphology and right-to-left script produce roughly 2× fertility. Finnish's agglutinative morphology causes common compound words to split into 3–4 tokens despite using the Latin alphabet. Chinese and Japanese typically yield 2–3× fertility since individual characters encode more meaning per slot than English words, yet require 2–3 tokens each in most BPE vocabularies.

## Cross-Lingual Fertility Analysis

```python
import tiktoken

def compute_fertility(encode_fn, texts_by_lang):
    # avg tokens per character for each language
    results = {}
    for lang, texts in texts_by_lang.items():
        total_tokens = sum(len(encode_fn(t)) for t in texts)
        total_chars = sum(len(t) for t in texts)
        results[lang] = total_tokens / max(total_chars, 1)
    return results

enc = tiktoken.get_encoding('cl100k_base')
sample_texts = {
    'en': ['The attention mechanism revolutionized NLP.', 'machine learning models'],
    'zh': ['注意力机制改变了自然语言处理。', '机器学习'],
    'ar': ['آلية الانتباه في معالجة اللغة الطبيعية.'],
    'th': ['กลไกความสนใจการประมวลผลภาษาธรรมชาติ'],
    'fi': ['Huomiokyky mullisti luonnollisen kielen kasittelyn.', 'koneoppimismallit'],
    'hi': ['ध्यान तंत्र ने एनएलपी में क्रांति ला दी।'],
    'ko': ['주의 메커니즘이 자연어 처리를 혁신했습니다.'],
    'de': ['Der Aufmerksamkeitsmechanismus revolutionierte NLP-Forschung.'],
    'ja': ['注意機構は自然言語処理に革命をもたらした。'],
    'ru': ['Механизм внимания произвёл революцию в обработке языка.'],
}
fertility = compute_fertility(enc.encode, sample_texts)
en_rate = fertility['en']
print('Language  Tok/Char  Relative')
for lang, rate in fertility.items():
    rel = rate / en_rate
    print(f'{lang:<10} {rate:.4f}   {rel:.2f}x')
```

## Vocabulary Coverage in Multilingual Models

In mBERT and XLM-R, the shared vocabulary is allocated proportionally to corpus size after alpha-smoothing. English, Chinese, and German receive the largest vocabulary slices. Languages like Swahili or Burmese, with small web corpora, receive far fewer vocabulary slots and rely on byte-fallback or character-level tokenization. This creates a vocabulary coverage disparity: equivalent concepts require more tokens in low-resource languages, degrading model capacity and generation throughput. The proportion of a language's vocabulary coverage directly correlates with its downstream task performance in multilingual benchmarks.

```python
from transformers import AutoTokenizer

def analyze_vocab_coverage(model_name, texts_by_lang):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    results = {}
    for lang, texts in texts_by_lang.items():
        all_ids = []
        for text in texts:
            ids = tokenizer.encode(text, add_special_tokens=False)
            all_ids.extend(ids)
        unk_id = tokenizer.unk_token_id
        unk_count = sum(1 for t in all_ids if t == unk_id)
        results[lang] = {
            'total_tokens': len(all_ids),
            'unique_types': len(set(all_ids)),
            'unk_rate': unk_count / max(len(all_ids), 1),
        }
    return results

model_name = 'xlm-roberta-base'
texts = {
    'en': ['Transformer architecture with self-attention layers.'],
    'zh': ['具有自注意力层的变换器架构。'],
    'ar': ['بنية المحول مع طبقات الانتباه الذاتي.'],
    'sw': ['Muundo wa transformer na tabaka za kujizingatia.'],
    'gu': ['ટ્રાન્સફોર્મર આર્કિટેક્ચર સ્વ-ધ્યાન સ્તરો સાથે.'],
}
coverage = analyze_vocab_coverage(model_name, texts)
print(f'Coverage: {model_name}')
for lang, stats in coverage.items():
    total = stats['total_tokens']
    unk = stats['unk_rate']
    uniq = stats['unique_types']
    print(f'  {lang}: {total} tokens, unique={uniq}, unk_rate={unk:.3f}')
```

## Temperature-Based Upsampling for Vocabulary Training

Alpha-sampling adjusts how many tokens each language contributes during vocabulary training. With alpha=1.0, sampling is proportional to corpus size — large corpora dominate. With alpha=0.7 (default in XLM and mBERT), small corpora are upsampled: a language with 1/100 the data of English receives roughly 1/100^0.7 ≈ 1/21 of the probability mass instead of 1/100. This gives low-resource languages more vocabulary coverage at the cost of slightly lower vocabulary efficiency for high-resource languages. The typical range is alpha=0.5 to 0.7; alpha=1.0 reproduces raw proportional sampling.

```python
import numpy as np

def alpha_sampling_weights(corpus_sizes, alpha=0.7):
    # alpha=1.0: proportional to corpus size (favours large corpora)
    # alpha=0.0: uniform across all languages
    # alpha=0.7: typical multilingual compromise used in XLM/mBERT
    langs = list(corpus_sizes.keys())
    sizes = np.array([corpus_sizes[l] for l in langs], dtype=float)
    smoothed = sizes ** alpha
    probs = smoothed / smoothed.sum()
    return dict(zip(langs, probs))

corpus_sizes = {
    'en': 50_000_000, 'zh': 10_000_000, 'ar': 3_000_000,
    'sw': 200_000,    'my': 100_000,    'th': 1_500_000,
    'fi': 2_000_000,  'hi': 4_000_000,
}
print('Language  Corpus       p(a=1.0)  p(a=0.7)  p(a=0.3)')
for lang, size in corpus_sizes.items():
    p10 = alpha_sampling_weights(corpus_sizes, alpha=1.0)[lang]
    p07 = alpha_sampling_weights(corpus_sizes, alpha=0.7)[lang]
    p03 = alpha_sampling_weights(corpus_sizes, alpha=0.3)[lang]
    print(f'{lang:<5}  {size:>12,}  {p10:.4f}    {p07:.4f}    {p03:.4f}')
sw_10 = alpha_sampling_weights(corpus_sizes, 1.0)['sw']
sw_07 = alpha_sampling_weights(corpus_sizes, 0.7)['sw']
print(f'Swahili upsampling gain (a=0.7 vs a=1.0): {sw_07/sw_10:.1f}x')
```

## Multilingual Tokenizer Usage with mT5 and XLM-R

```python
from transformers import AutoTokenizer

def tokenize_multilingual(text_by_lang, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    results = {}
    for lang, text in text_by_lang.items():
        ids = tokenizer.encode(text, add_special_tokens=False)
        tokens = tokenizer.convert_ids_to_tokens(ids)
        results[lang] = {'ids': ids, 'tokens': tokens, 'n': len(ids)}
    return results

sentence = {
    'en': 'The tokenizer splits text into subword units.',
    'zh': '分词器将文本拆分为子词单元。',
    'ar': 'يقسم المحلل النصي النص إلى وحدات كلمة فرعية.',
    'ja': 'トークナイザーはテキストをサブワード単位に分割します。',
    'fi': 'Tokenisaattori jakaa tekstin aliosiin.',
    'th': 'ตัวแยกคำแบ่งข้อความออกเป็นหน่วยย่อย',
}
for model in ['google/mt5-small', 'xlm-roberta-base']:
    print(f'Model: {model}')
    results = tokenize_multilingual(sentence, model)
    for lang, info in results.items():
        n_tok = info['n']
        toks = info['tokens'][:6]
        print(f'  {lang}: {n_tok} tokens | {toks}')
    print()
```

## Token Fertility by Language

| Language | Script Family | Tokens/Word (approx) | Relative to English | Tokenizer Sensitivity |
| --- | --- | --- | --- | --- |
| English | Latin | 1.2 | 1.0x (baseline) | Low |
| Spanish | Latin | 1.3 | 1.1x | Low |
| French | Latin | 1.4 | 1.2x | Low |
| German | Latin (compounds) | 1.8 | 1.5x | Medium |
| Chinese | Logographic (CJK) | 2.0–2.5 | 1.8x | High |
| Japanese | CJK + Kana | 2.0–3.0 | 2.1x | High |
| Korean | Hangul (agglutinative) | 2.5–3.5 | 2.4x | High |
| Arabic | Abjad (RTL) | 2.0–2.5 | 2.1x | High |
| Thai | Abugida (no spaces) | 3.0–5.0 | 3.5x | Very High |
| Hindi | Devanagari | 2.0–3.0 | 2.3x | High |
| Finnish | Latin (agglutinative) | 1.8–2.5 | 1.7x | Medium-High |
| Code (Python) | ASCII + symbols | 1.0–1.5 | 1.1x | Low (tokenizer-dependent) |

## Zero-Shot Cross-Lingual Transfer and Code-Switching

Zero-shot cross-lingual transfer — training on English and evaluating on another language — works partly because multilingual models share subword tokens for cognates, technical terms, named entities, and numerals. English 'transformer' and German 'Transformer' often map to identical tokens. URLs, code identifiers, and proper nouns are frequently identical across languages, creating strong cross-lingual anchors in the embedding space. The proportion of shared tokens between a language pair strongly correlates with zero-shot transfer performance on benchmarks like XTREME and XGLUE.

Code-switching refers to mixed-language sequences where users switch languages within a single prompt. SentencePiece handles this via byte-fallback: any character not in the trained vocabulary is encoded as its individual UTF-8 bytes (e.g., <0xE4><0xB8><0xAD>), ensuring no out-of-vocabulary failures at the cost of very high fertility for rare scripts. LangID prefix tokens like __en__ or __zh__ can be prepended to signal the target language, guiding mT5 and NLLB models toward the correct generation language without changing the tokenizer's vocabulary allocation.

## API Cost and Infrastructure Implications

> **API Cost Varies 3–5x by Language**: API cost for multilingual LLM applications can vary 3–5x based on language — always benchmark token counts in your target languages before estimating infrastructure costs. A Thai or Arabic response with equivalent semantic content to an English response consumes proportionally more tokens, directly increasing per-request cost and reducing effective context window capacity. Use the tokenizer's encode() method on representative production samples in each target language before committing to an API pricing tier.

- Fertility affects API pricing: charge-per-token APIs cost 3–5x more for high-fertility languages at equal content.
- Context window: a 4096-token window holds significantly less content for Arabic or Thai than for English.
- Generation latency: higher token counts increase autoregressive generation time proportionally.
- Batching efficiency: mixed-language batches have variable sequence lengths, reducing GPU utilization.
- Vocabulary allocation: reserve minimum vocabulary slots per script when training custom multilingual tokenizers.
- Benchmark fertility on real production samples — synthetic test sentences often underestimate real-world fertility.

Practical mitigation strategies include using language-specific tokenizers for single-language deployments (achieving lower fertility than multilingual tokenizers), compressing prompts by removing redundant tokens before API calls, and monitoring per-language token counts in production observability dashboards. For mT5 and NLLB-based deployments, the tokenizers are specifically calibrated for multilingual coverage, achieving materially lower fertility for non-English languages than GPT-series tokenizers trained predominantly on English corpora.

---

