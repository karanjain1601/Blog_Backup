---
title: "Encoder-Decoder Transformers — T5, BART, and Seq2Seq"
slug: "encoder-decoder-t5-bart"
description: "Encoder-decoder architecture for seq2seq tasks: bidirectional encoder, autoregressive decoder with cross-attention, T5 text-to-text framing, BART denoising pretraining, and comparison with decoder-only models."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW5jb2Rlci1kZWNvZGVyIHRyYW5zZm9ybWVycyBwcm9jZXNzIGlucHV0IHNlcXVlbmNlcyB3aXRoIGEgYmlkaXJlY3Rpb25hbCBlbmNvZGVyIOKAlCBldmVyeSBwb3NpdGlvbiBjYW4gYXR0ZW5kIHRvIGV2ZXJ5IG90aGVyIHBvc2l0aW9uIOKAlCBhbmQgZ2VuZXJhdGUgb3V0cHV0IHNlcXVlbmNlcyB3aXRoIGEgY2F1c2FsIGRlY29kZXIgdGhhdCBhZGRpdGlvbmFsbHkgYXR0ZW5kcyB0byB0aGUgZW5jb2Rlclx1MDAyN3Mgb3V0cHV0IHZpYSBjcm9zcy1hdHRlbnRpb24uIFRoaXMgYXJjaGl0ZWN0dXJlIGlzIG5hdHVyYWwgZm9yIHRhc2tzIHdoZXJlIHRoZSBpbnB1dCBhbmQgb3V0cHV0IHNlcXVlbmNlcyBoYXZlIGRpZmZlcmVudCBsZW5ndGhzIGFuZCBzdHJ1Y3R1cmVzOiB0cmFuc2xhdGlvbiwgc3VtbWFyaXphdGlvbiwgYW5kIHF1ZXN0aW9uIGFuc3dlcmluZy4gVDUgYW5kIEJBUlQgYXJlIHRoZSBjYW5vbmljYWwgZW5jb2Rlci1kZWNvZGVyIHByZXRyYWluZWQgbGFuZ3VhZ2UgbW9kZWxzIGFuZCByZW1haW4gc3Ryb25nIGJhc2VsaW5lcyBmb3IgbWFueSBzdHJ1Y3R1cmVkIGdlbmVyYXRpb24gdGFza3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRW5jb2Rlci1EZWNvZGVyIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGVuY29kZXIgcmVjZWl2ZXMgdGhlIHNvdXJjZSBzZXF1ZW5jZSwgYXBwbGllcyBMX2VuYyBsYXllcnMgb2YgYmlkaXJlY3Rpb25hbCBzZWxmLWF0dGVudGlvbiBhbmQgRkZOLCBhbmQgb3V0cHV0cyBhIHNlcXVlbmNlIG9mIGNvbnRleHQgdmVjdG9ycyBIX2VuYyDiiIgg4oSdXntTw5dkfS4gVGhlIGRlY29kZXIgcmVjZWl2ZXMgdGhlIHRhcmdldCBwcmVmaXgsIGFwcGxpZXMgTF9kZWMgbGF5ZXJzIG9mIGNhdXNhbCBzZWxmLWF0dGVudGlvbiBmb2xsb3dlZCBieSBjcm9zcy1hdHRlbnRpb24gb3ZlciBIX2VuYywgdGhlbiBGRk4uIENyb3NzLWF0dGVudGlvbiBjb21wdXRlcyBRIGZyb20gdGhlIGRlY29kZXIgaGlkZGVuIHN0YXRlLCBLIGFuZCBWIGZyb20gSF9lbmM6IENyb3NzQXR0bih4X2RlYywgSF9lbmMpID0gc29mdG1heChRS15UL+KImmQpVi4gVGhpcyBhbGxvd3MgdGhlIGRlY29kZXIgdG8gc2VsZWN0aXZlbHkgZm9jdXMgb24gZGlmZmVyZW50IHBhcnRzIG9mIHRoZSBzb3VyY2UgYXQgZWFjaCBnZW5lcmF0aW9uIHN0ZXAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIENyb3NzQXR0ZW50aW9uKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw9NTEyLCBuX2hlYWRzPTgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uX2hlYWRzLCBzZWxmLmRfaGVhZCA9IG5faGVhZHMsIGRfbW9kZWwgLy8gbl9oZWFkc1xuICAgICAgICBzZWxmLnFfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmt2X3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgMiAqIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYub3V0X3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHhfZGVjLCBlbmNfb3V0KTpcbiAgICAgICAgQiwgVF9kZWMsIEMgPSB4X2RlYy5zaGFwZVxuICAgICAgICBUX2VuYyA9IGVuY19vdXQuc2hhcGVbMV1cbiAgICAgICAgcSA9IHNlbGYucV9wcm9qKHhfZGVjKS52aWV3KEIsIFRfZGVjLCBzZWxmLm5faGVhZHMsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgaywgdiA9IHNlbGYua3ZfcHJvaihlbmNfb3V0KS5zcGxpdChDLCBkaW09LTEpXG4gICAgICAgIGsgPSBrLnZpZXcoQiwgVF9lbmMsIHNlbGYubl9oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICB2ID0gdi52aWV3KEIsIFRfZW5jLCBzZWxmLm5faGVhZHMsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgYXR0ID0gRi5zb2Z0bWF4KChxIEAgay50cmFuc3Bvc2UoLTIsIC0xKSkgKiBzZWxmLmRfaGVhZCAqKiAtMC41LCBkaW09LTEpXG4gICAgICAgIG91dCA9IChhdHQgQCB2KS50cmFuc3Bvc2UoMSwgMikuY29udGlndW91cygpLnZpZXcoQiwgVF9kZWMsIEMpXG4gICAgICAgIHJldHVybiBzZWxmLm91dF9wcm9qKG91dClcblxuIyBTaW11bGF0ZSBlbmNvZGVyIG91dHB1dCBhbmQgZGVjb2RlciBxdWVyeVxuZW5jX291dCA9IHRvcmNoLnJhbmRuKDIsIDIwLCA1MTIpICAgIyBzb3VyY2U6IDIwIHRva2Vuc1xuZGVjX3F1ZXJ5ID0gdG9yY2gucmFuZG4oMiwgNSwgNTEyKSAgIyB0YXJnZXQgcHJlZml4OiA1IHRva2Vuc1xuY3Jvc3NfYXR0biA9IENyb3NzQXR0ZW50aW9uKClcbm91dCA9IGNyb3NzX2F0dG4oZGVjX3F1ZXJ5LCBlbmNfb3V0KVxucHJpbnQoZlx1MDAyN0Nyb3NzLWF0dGVudGlvbiBvdXRwdXQ6IHtvdXQuc2hhcGV9XHUwMDI3KSAgIyAoMiwgNSwgNTEyKVxucHJpbnQoZlx1MDAyN0VhY2ggZGVjb2RlciBwb3NpdGlvbiBhdHRlbmRzIHRvIGFsbCB7ZW5jX291dC5zaGFwZVsxXX0gZW5jb2RlciBwb3NpdGlvbnNcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVDU6IFRleHQtdG8tVGV4dCBUcmFuc2ZlciBUcmFuc2Zvcm1lciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVDUgKFJhZmZlbCBldCBhbC4gMjAyMCkgdW5pZmllcyBhbGwgTkxQIHRhc2tzIGJ5IGZyYW1pbmcgdGhlbSBhcyB0ZXh0LXRvLXRleHQ6IHRoZSBpbnB1dCBpcyBhIHRhc2stcHJlZml4ZWQgc3RyaW5nIChlLmcuLCBcdTAwMjdzdW1tYXJpemU6IC4uLlx1MDAyNywgXHUwMDI3dHJhbnNsYXRlIEVuZ2xpc2ggdG8gRnJlbmNoOiAuLi5cdTAwMjcpIGFuZCB0aGUgb3V0cHV0IGlzIGFsd2F5cyBhIHN0cmluZy4gVGhpcyBzaW5nbGUgYXJjaGl0ZWN0dXJlIGhhbmRsZXMgY2xhc3NpZmljYXRpb24gKG91dHB1dCBpcyBhIGNsYXNzIGxhYmVsIHN0cmluZyksIHJlZ3Jlc3Npb24gKG91dHB1dCBpcyBhIG51bWJlciBzdHJpbmcpLCBhbmQgZ2VuZXJhdGlvbiB0YXNrcyB1bmlmb3JtbHkuIFQ1IHJlcGxhY2VzIGFic29sdXRlIHBvc2l0aW9uIGVtYmVkZGluZ3Mgd2l0aCBsZWFybmVkIHJlbGF0aXZlIHBvc2l0aW9uIGJpYXNlcyBhZGRlZCB0byBhdHRlbnRpb24gbG9naXRzOiBhdHRuX2xvZ2l0KGksaikgKz0gYihp4oiSaiksIHdoZXJlIGIgaXMgYSBzY2FsYXIgYmlhcyBpbmRleGVkIGJ5IHJlbGF0aXZlIGRpc3RhbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgVDVGb3JDb25kaXRpb25hbEdlbmVyYXRpb24sIFQ1VG9rZW5pemVyXG5pbXBvcnQgdG9yY2hcblxuIyBUNSB0ZXh0LXRvLXRleHQgZmluZS10dW5pbmcgZXhhbXBsZSAoaWxsdXN0cmF0aXZlKVxudG9rZW5pemVyID0gVDVUb2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFx1MDAyN3Q1LXNtYWxsXHUwMDI3KVxubW9kZWwgPSBUNUZvckNvbmRpdGlvbmFsR2VuZXJhdGlvbi5mcm9tX3ByZXRyYWluZWQoXHUwMDI3dDUtc21hbGxcdTAwMjcpXG5tb2RlbC50cmFpbigpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtVyhtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTNlLTQpXG5cbiMgU2ltdWxhdGUgYSBzdW1tYXJpemF0aW9uIGJhdGNoXG5pbnB1dF90ZXh0cyA9IFtcbiAgICBcdTAwMjdzdW1tYXJpemU6IFRoZSBxdWljayBicm93biBmb3gganVtcHMgb3ZlciB0aGUgbGF6eSBkb2cuIFx1MDAyN1xuICAgIFx1MDAyN0ZveGVzIGFyZSBrbm93biBmb3IgdGhlaXIgYWdpbGl0eSBhbmQgc3BlZWQuXHUwMDI3LFxuICAgIFx1MDAyN3N1bW1hcml6ZTogTmV1cmFsIG5ldHdvcmtzIGxlYXJuIHJlcHJlc2VudGF0aW9ucyBmcm9tIGRhdGEuIFx1MDAyN1xuICAgIFx1MDAyN0RlZXAgbmV0d29ya3Mgc3RhY2sgbXVsdGlwbGUgbGF5ZXJzIG9mIG5vbmxpbmVhciB0cmFuc2Zvcm1hdGlvbnMuXHUwMDI3XG5dXG50YXJnZXRfdGV4dHMgPSBbXHUwMDI3Rm94IGp1bXBzIG92ZXIgZG9nLlx1MDAyNywgXHUwMDI3TmV1cmFsIG5ldHMgbGVhcm4gZnJvbSBkYXRhLlx1MDAyN11cblxuaW5wdXRzID0gdG9rZW5pemVyKGlucHV0X3RleHRzLCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNywgcGFkZGluZz1UcnVlLCB0cnVuY2F0aW9uPVRydWUsIG1heF9sZW5ndGg9MTI4KVxubGFiZWxzID0gdG9rZW5pemVyKHRhcmdldF90ZXh0cywgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcsIHBhZGRpbmc9VHJ1ZSkuaW5wdXRfaWRzXG5sYWJlbHNbbGFiZWxzID09IHRva2VuaXplci5wYWRfdG9rZW5faWRdID0gLTEwMCAgIyBpZ25vcmUgcGFkZGluZyBpbiBsb3NzXG5cbm91dHB1dHMgPSBtb2RlbCgqKmlucHV0cywgbGFiZWxzPWxhYmVscylcbnByaW50KGZcdTAwMjdMb3NzOiB7b3V0cHV0cy5sb3NzLml0ZW0oKTouNGZ9XHUwMDI3KVxub3V0cHV0cy5sb3NzLmJhY2t3YXJkKClcbm9wdGltaXplci5zdGVwKCk7IG9wdGltaXplci56ZXJvX2dyYWQoKVxucHJpbnQoZlx1MDAyN1Q1LXNtYWxsIHBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKTosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCQVJUOiBEZW5vaXNpbmcgQXV0b2VuY29kZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJBUlQgKExld2lzIGV0IGFsLiAyMDIwKSBwcmV0cmFpbmVkIGFuIGVuY29kZXItZGVjb2RlciBieSBjb3JydXB0aW5nIGlucHV0IHRleHQgYW5kIHRyYWluaW5nIHRoZSBtb2RlbCB0byByZWNvbnN0cnVjdCB0aGUgb3JpZ2luYWwuIFRoZSBlbmNvZGVyIGlzIGJpZGlyZWN0aW9uYWwgQkVSVC1zdHlsZTsgdGhlIGRlY29kZXIgaXMgR1BULXN0eWxlIGF1dG9yZWdyZXNzaXZlLiBDb3JydXB0aW9uIHN0cmF0ZWdpZXMgaW5jbHVkZTogdG9rZW4gbWFza2luZyAobGlrZSBCRVJUKSwgdG9rZW4gZGVsZXRpb24sIHRleHQgaW5maWxsaW5nIChyZXBsYWNlIGEgc3BhbiB3aXRoIG9uZSBNQVNLIHRva2VuKSwgc2VudGVuY2UgcGVybXV0YXRpb24sIGFuZCBkb2N1bWVudCByb3RhdGlvbi4gQkFSVFx1MDAyN3MgcHJldHJhaW5pbmcgb2JqZWN0aXZlIG1ha2VzIGl0cyBkZWNvZGVyIHBhcnRpY3VsYXJseSB3ZWxsLXN1aXRlZCBmb3IgZ2VuZXJhdGlvbiB0YXNrcyDigJQgaXQgYWxyZWFkeSBrbm93cyBob3cgdG8gcHJvZHVjZSBmbHVlbnQgdGV4dCBjb25kaXRpb25lZCBvbiBhIG5vaXN5IGlucHV0LiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiQkFSVCB2cyBUNSBUYXNrIFN0cmVuZ3RocyIsImNvbnRlbnQiOiJCQVJUIGV4Y2VscyBhdCBnZW5lcmF0aW9uIHRhc2tzIChzdW1tYXJpemF0aW9uLCBkaWFsb2d1ZSwgdHJhbnNsYXRpb24pIGJlY2F1c2UgaXRzIHByZXRyYWluaW5nIGRpcmVjdGx5IHRyYWlucyB0aGUgZGVjb2RlciB0byBnZW5lcmF0ZSBmbHVlbnQgdGV4dC4gVDVcdTAwMjdzIHRleHQtdG8tdGV4dCBmcmFtaW5nIG1ha2VzIGl0IHN0cm9uZ2VyIG9uIGNsYXNzaWZpY2F0aW9uLXN0eWxlIHRhc2tzIGZyYW1lZCBhcyBnZW5lcmF0aW9uIChlLmcuLCBOTEksIHNlbnRpbWVudCkgYmVjYXVzZSBhbnkgbGFiZWwgY2FuIGJlIGEgdG9rZW4gc3RyaW5nLiBGb3IgUk9VR0Ugc2NvcmVzIG9uIENOTi9EYWlseU1haWwgc3VtbWFyaXphdGlvbiwgQkFSVC1sYXJnZSB0eXBpY2FsbHkgb3V0cGVyZm9ybXMgVDUtbGFyZ2UgYnkgMS0yIFJPVUdFIHBvaW50cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEJhcnRGb3JDb25kaXRpb25hbEdlbmVyYXRpb24sIEJhcnRUb2tlbml6ZXJcbmltcG9ydCB0b3JjaFxuXG50b2tlbml6ZXIgPSBCYXJ0VG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcdTAwMjdmYWNlYm9vay9iYXJ0LWJhc2VcdTAwMjcpXG5tb2RlbCA9IEJhcnRGb3JDb25kaXRpb25hbEdlbmVyYXRpb24uZnJvbV9wcmV0cmFpbmVkKFx1MDAyN2ZhY2Vib29rL2JhcnQtYmFzZVx1MDAyNylcbm1vZGVsLmV2YWwoKVxuXG5hcnRpY2xlID0gKFxuICAgIFx1MDAyN1RyYW5zZm9ybWVyIG1vZGVscyBoYXZlIHJldm9sdXRpb25pemVkIG5hdHVyYWwgbGFuZ3VhZ2UgcHJvY2Vzc2luZy4gXHUwMDI3XG4gICAgXHUwMDI3T3JpZ2luYWxseSBwcm9wb3NlZCBmb3IgbWFjaGluZSB0cmFuc2xhdGlvbiwgdGhleSBub3cgZG9taW5hdGUgdGFza3MgcmFuZ2luZyBcdTAwMjdcbiAgICBcdTAwMjdmcm9tIHRleHQgY2xhc3NpZmljYXRpb24gdG8gb3Blbi1lbmRlZCBnZW5lcmF0aW9uLiBUaGUga2V5IGlubm92YXRpb24gaXMgdGhlIFx1MDAyN1xuICAgIFx1MDAyN2F0dGVudGlvbiBtZWNoYW5pc20sIHdoaWNoIGFsbG93cyBldmVyeSB0b2tlbiB0byBhdHRlbmQgdG8gZXZlcnkgb3RoZXIgdG9rZW4uXHUwMDI3XG4pXG5cbmlucHV0cyA9IHRva2VuaXplcihhcnRpY2xlLCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNywgbWF4X2xlbmd0aD01MTIsIHRydW5jYXRpb249VHJ1ZSlcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIHN1bW1hcnlfaWRzID0gbW9kZWwuZ2VuZXJhdGUoXG4gICAgICAgIGlucHV0c1tcdTAwMjdpbnB1dF9pZHNcdTAwMjddLFxuICAgICAgICBudW1fYmVhbXM9NCxcbiAgICAgICAgbWF4X2xlbmd0aD02MCxcbiAgICAgICAgbWluX2xlbmd0aD0xMCxcbiAgICAgICAgbGVuZ3RoX3BlbmFsdHk9Mi4wLFxuICAgICAgICBlYXJseV9zdG9wcGluZz1UcnVlXG4gICAgKVxuc3VtbWFyeSA9IHRva2VuaXplci5kZWNvZGUoc3VtbWFyeV9pZHNbMF0sIHNraXBfc3BlY2lhbF90b2tlbnM9VHJ1ZSlcbnByaW50KGZcdTAwMjdBcnRpY2xlIGxlbmd0aDoge2xlbihhcnRpY2xlLnNwbGl0KCkpfSB3b3Jkc1x1MDAyNylcbnByaW50KGZcdTAwMjdTdW1tYXJ5OiB7c3VtbWFyeX1cdTAwMjcpXG5wcmludChmXHUwMDI3QkFSVC1iYXNlIHBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKTosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpbmcgQkFSVCB2cyBUNSB2cyBHUFQtMiBvbiBTdW1tYXJpemF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6IiMgU2ltdWxhdGVkIFJPVUdFIGNvbXBhcmlzb24gKHJlcHJlc2VudGF0aXZlIHB1Ymxpc2hlZCBudW1iZXJzKVxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbm1vZGVscyA9IFtcdTAwMjdHUFQtMiAoMTE3TSlcdTAwMjcsIFx1MDAyN1Q1LWJhc2UgKDI1ME0pXHUwMDI3LCBcdTAwMjdUNS1sYXJnZSAoNzcwTSlcdTAwMjcsIFx1MDAyN0JBUlQtYmFzZSAoMTQwTSlcdTAwMjcsIFx1MDAyN0JBUlQtbGFyZ2UgKDQwME0pXHUwMDI3XVxuIyBDTk4vRGFpbHlNYWlsIFJPVUdFLTEsIFJPVUdFLTIsIFJPVUdFLUwgKGFwcHJveGltYXRlIHB1Ymxpc2hlZCB2YWx1ZXMpXG5yZXN1bHRzID0gW1xuICAgIFsyOS4zLCA4LjYsIDI2LjJdLCAgICMgR1BULTIgKGZpbmUtdHVuZWQpXG4gICAgWzQyLjUsIDIwLjksIDM5LjhdLCAgIyBUNS1iYXNlIGZpbmUtdHVuZWRcbiAgICBbNDMuMSwgMjEuNiwgNDAuM10sICAjIFQ1LWxhcmdlIGZpbmUtdHVuZWRcbiAgICBbNDQuMiwgMjEuMywgNDAuOV0sICAjIEJBUlQtYmFzZSBmaW5lLXR1bmVkXG4gICAgWzQ0LjIsIDIxLjMsIDQwLjldLCAgIyBCQVJULWxhcmdlIGZpbmUtdHVuZWRcbl1cblxucHJpbnQoZlx1MDAyN3tcdTAwMjdNb2RlbFx1MDAyNzpcdTAwM2MyNX0ge1x1MDAyN1ItMVx1MDAyNzpcdTAwM2U2fSB7XHUwMDI3Ui0yXHUwMDI3Olx1MDAzZTZ9IHtcdTAwMjdSLUxcdTAwMjc6XHUwMDNlNn1cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNDUpXG5mb3IgbmFtZSwgKHIxLCByMiwgcmwpIGluIHppcChtb2RlbHMsIHJlc3VsdHMpOlxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2MyNX0ge3IxOlx1MDAzZTYuMWZ9IHtyMjpcdTAwM2U2LjFmfSB7cmw6XHUwMDNlNi4xZn1cdTAwMjcpXG5cbmJlc3RfcjFfaWR4ID0gbnAuYXJnbWF4KFtyWzBdIGZvciByIGluIHJlc3VsdHNdKVxucHJpbnQoZlx1MDAyN1xcbkJlc3QgUk9VR0UtMToge21vZGVsc1tiZXN0X3IxX2lkeF19IHdpdGgge3Jlc3VsdHNbYmVzdF9yMV9pZHhdWzBdfVx1MDAyNylcbnByaW50KFx1MDAyN0JBUlQtbGFyZ2UgYW5kIFQ1LWxhcmdlIGFyZSBib3RoIGNvbXBldGl0aXZlOyBCQVJUIHN0cm9uZ2VyIG9uIGdlbiB0YXNrcy5cdTAwMjcpXG5wcmludChcdTAwMjdHUFQtMiBsYWdzIHNpZ25pZmljYW50bHkg4oCUIGRlY29kZXItb25seSB3aXRob3V0IGVuYyBjb250ZXh0IGlzIGRpc2FkdmFudGFnZWQgZm9yIHN1bW1hcml6YXRpb24uXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFyY2hpdGVjdHVyZSBDb21wYXJpc29uOiBFbmNvZGVyIFR5cGVzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkF0dHJpYnV0ZSIsIkVuY29kZXItT25seSAoQkVSVCkiLCJEZWNvZGVyLU9ubHkgKEdQVCkiLCJFbmNvZGVyLURlY29kZXIgKFQ1L0JBUlQpIl0sInJvd3MiOltbIkF0dGVudGlvbiB0eXBlIiwiQmlkaXJlY3Rpb25hbCBzZWxmLWF0dGVudGlvbiIsIkNhdXNhbCBzZWxmLWF0dGVudGlvbiIsIkJpZGlyIGVuY29kZXIgKyBjYXVzYWwgZGVjb2RlciArIGNyb3NzLWF0dG4iXSxbIlByZXRyYWluaW5nIG9iamVjdGl2ZSIsIk1MTSAvIE5TUCIsIkNhdXNhbCBMTSAoTkxMKSIsIlRleHQtdG8tdGV4dCBMTSAvIGRlbm9pc2luZyJdLFsiQXV0b3JlZ3Jlc3NpdmUgZ2VuZXJhdGlvbiIsIk5vIiwiWWVzIiwiWWVzIChkZWNvZGVyIHNpZGUpIl0sWyJJbnB1dCByZXByZXNlbnRhdGlvbiIsIkZ1bGwgY29udGV4dCwgYmVzdCBmb3IgdW5kZXJzdGFuZGluZyIsIkxlZnQtY29udGV4dCBvbmx5IiwiRnVsbCBzb3VyY2UsIGF1dG9yZWdyZXNzaXZlIHRhcmdldCJdLFsiSW5mZXJlbmNlIGNvc3QiLCJPKG4pIOKAlCBzaW5nbGUgZm9yd2FyZCBwYXNzIiwiTyhuKSBwZXIgc3RlcDsgS1YgY2FjaGUgaGVscHMiLCJPKG5fc3JjKSBlbmNvZGVyICsgTyhuX3RndCkgcGVyIHN0ZXAgZGVjb2RlciJdLFsiQmVzdCB0YXNrcyIsIkNsYXNzaWZpY2F0aW9uLCBORVIsIFFBIGV4dHJhY3RpdmUiLCJPcGVuIGdlbmVyYXRpb24sIGNoYXQsIGNvZGUiLCJUcmFuc2xhdGlvbiwgc3VtbWFyaXphdGlvbiwgUUEgYWJzdHJhY3RpdmUiXSxbIkV4YW1wbGVzIiwiQkVSVCwgUm9CRVJUYSwgRGVCRVJUYSIsIkdQVC0yLzMvNCwgTExhTUEsIE1pc3RyYWwiLCJUNSwgQkFSVCwgbVQ1LCBQRUdBU1VTIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUNS1TcGVjaWZpYyBEZXNpZ24gQ2hvaWNlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVDUgZWxpbWluYXRlcyBhbGwgYmlhcyB0ZXJtcyBmcm9tIGxpbmVhciBwcm9qZWN0aW9ucyAobm8gYmlhcyBpbiBRLCBLLCBWLCBGRk4sIG9yIG91dHB1dCBsYXllcnMpLCB3aGljaCByZWR1Y2VzIHBhcmFtZXRlcnMgc2xpZ2h0bHkgYW5kIHdhcyBmb3VuZCBub3QgdG8gaHVydCBwZXJmb3JtYW5jZS4gSW5zdGVhZCBvZiBhYnNvbHV0ZSBwb3NpdGlvbiBlbWJlZGRpbmdzLCBUNSB1c2VzIGxlYXJuZWQgcmVsYXRpdmUgcG9zaXRpb24gYmlhc2VzOiBzY2FsYXIgb2Zmc2V0cyBiKGniiJJqKSBhZGRlZCB0byBhdHRlbnRpb24gbG9naXRzLCBpbmRleGVkIGJ5IHJlbGF0aXZlIGRpc3RhbmNlIGFuZCBjbGlwcGVkIHRvIGEgbWF4aW11bSBvZmZzZXQuIFRoZXNlIGJpYXNlcyBhcmUgc2hhcmVkIGFjcm9zcyBhdHRlbnRpb24gaGVhZHMgYW5kIGFjcm9zcyBsYXllcnMsIG1ha2luZyB0aGVtIGV4dHJlbWVseSBwYXJhbWV0ZXItZWZmaWNpZW50LiBSZWxhdGl2ZSBwb3NpdGlvbiBiaWFzZXMgZ2VuZXJhbGl6ZSBiZXR0ZXIgdG8gc2VxdWVuY2UgbGVuZ3RocyBsb25nZXIgdGhhbiB0aG9zZSBzZWVuIGR1cmluZyB0cmFpbmluZyDigJQgYSBrZXkgYWR2YW50YWdlIG92ZXIgbGVhcm5lZCBhYnNvbHV0ZSBwb3NpdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtQXR0ZW50aW9uIENvbXBsZXhpdHkgYW5kIEluZmVyZW5jZSBDb3N0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDcm9zcy1hdHRlbnRpb24gaGFzIGNvbXBsZXhpdHkgTyhTIMOXIFQpIHdoZXJlIFMgaXMgc291cmNlIGxlbmd0aCBhbmQgVCBpcyB0YXJnZXQgbGVuZ3RoLiBGb3IgbG9uZyBkb2N1bWVudHMgKFM9ODE5Mikgd2l0aCBsb25nIHN1bW1hcmllcyAoVD01MTIpLCB0aGlzIGlzIDRNIGF0dGVudGlvbiBjb21wdXRhdGlvbnMgcGVyIGxheWVyIHBlciBoZWFkIOKAlCBub3QgY2hlYXAuIERlY29kZXItb25seSBtb2RlbHMgYXZvaWQgY3Jvc3MtYXR0ZW50aW9uIGVudGlyZWx5LCB3aGljaCBzaW1wbGlmaWVzIHRoZSBhcmNoaXRlY3R1cmUgYW5kIHJlZHVjZXMgbWVtb3J5IGJhbmR3aWR0aC4gSG93ZXZlciwgZGVjb2Rlci1vbmx5IG1vZGVscyBtdXN0IGZpdCB0aGUgZW50aXJlIHNvdXJjZSBpbnRvIHRoZWlyIGNvbnRleHQgd2luZG93IGFzIHByZWZpeCB0ZXh0LCB3aGljaCBhbHNvIGhhcyBPKG7CsikgYXR0ZW50aW9uIGNvc3QuIEZvciB2ZXJ5IGxvbmcgc291cmNlICsgc2hvcnQgdGFyZ2V0IHRhc2tzLCBlbmNvZGVyLWRlY29kZXIgaXMgY29tcGV0aXRpdmUgYmVjYXVzZSB0aGUgZW5jb2RlciBwcm9jZXNzZXMgc291cmNlIG9uY2UuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUNSByZWxhdGl2ZSBwb3NpdGlvbiBiaWFzOiBiaWFzIGIoaS1qKSBhZGRlZCB0byBhdHRlbnRpb24gbG9naXRzOyBzaGFyZWQgYWNyb3NzIGhlYWRzOyBnZW5lcmFsaXplcyB0byB1bnNlZW4gbGVuZ3Rocy4iLCJCQVJUIHBvc2l0aW9uYWwgZW1iZWRkaW5nczogbGVhcm5lZCBhYnNvbHV0ZSBwb3NpdGlvbnMgKGxpa2UgR1BULTIpLCBtYXggMTAyNCBieSBkZWZhdWx0LiIsIlQ1IHVzZXMgbm8gYmlhcyB0ZXJtcyBpbiBhbnkgbGluZWFyIHByb2plY3Rpb24g4oCUIGEgZGVzaWduIGNob2ljZSB0aGF0IHJlZHVjZXMgcGFyYW1ldGVycyBzbGlnaHRseS4iLCJCQVJUIGVuY29kZXIgdXNlcyBCRVJULXN0eWxlIGFyY2hpdGVjdHVyZSB3aXRoIHByZS10cmFpbmVkIHdlaWdodHM7IGRlY29kZXIgdXNlcyBHUFQtc3R5bGUgY2F1c2FsIG1hc2tpbmcuIiwiQmVhbSBzZWFyY2ggaXMgc3RhbmRhcmQgZm9yIGVuY29kZXItZGVjb2RlciBnZW5lcmF0aW9uOyBkZWNvZGVyLW9ubHkgdHlwaWNhbGx5IHVzZXMgc2FtcGxpbmcgaW5zdGVhZC4iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFbmNvZGVyLWRlY29kZXIgYXJjaGl0ZWN0dXJlcyByZW1haW4gdGhlIHByZWZlcnJlZCBjaG9pY2UgZm9yIHN0cnVjdHVyZWQgZ2VuZXJhdGlvbiB0YXNrcyB3aXRoIGxvbmcgaW5wdXRzIGFuZCBzaG9ydCBvdXRwdXRzIOKAlCBwYXJ0aWN1bGFybHkgZG9jdW1lbnQgc3VtbWFyaXphdGlvbiwgY29udHJvbGxlZCB0cmFuc2xhdGlvbiwgYW5kIGRhdGEtdG8tdGV4dCBnZW5lcmF0aW9uIOKAlCB3aGVyZSB0aGUgYmlkaXJlY3Rpb25hbCBlbmNvZGVyIHByb2R1Y2VzIHJpY2hlciBzb3VyY2UgcmVwcmVzZW50YXRpb25zIHRoYW4gYSBkZWNvZGVyLW9ubHkgcHJlZml4LiBBcyBjb250ZXh0IHdpbmRvd3MgZm9yIGRlY29kZXItb25seSBtb2RlbHMgaGF2ZSBncm93biB0byAxMjhLKyB0b2tlbnMsIHRoZSBhcmNoaXRlY3R1cmFsIGFkdmFudGFnZSBvZiBlbmNvZGVyLWRlY29kZXIgaGFzIG5hcnJvd2VkLCBhbmQgbWFueSBwcmFjdGljYWwgc3lzdGVtcyBub3cgc2ltcGx5IHByZXBlbmQgdGhlIHNvdXJjZSBhcyBjb250ZXh0IGZvciBhIGRlY29kZXItb25seSBtb2RlbC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Encoder-Decoder Transformers — T5, BART, and Seq2Seq

Encoder-decoder transformers process input sequences with a bidirectional encoder — every position can attend to every other position — and generate output sequences with a causal decoder that additionally attends to the encoder's output via cross-attention. This architecture is natural for tasks where the input and output sequences have different lengths and structures: translation, summarization, and question answering. T5 and BART are the canonical encoder-decoder pretrained language models and remain strong baselines for many structured generation tasks.

## Encoder-Decoder Architecture

The encoder receives the source sequence, applies L_enc layers of bidirectional self-attention and FFN, and outputs a sequence of context vectors H_enc ∈ ℝ^{S×d}. The decoder receives the target prefix, applies L_dec layers of causal self-attention followed by cross-attention over H_enc, then FFN. Cross-attention computes Q from the decoder hidden state, K and V from H_enc: CrossAttn(x_dec, H_enc) = softmax(QK^T/√d)V. This allows the decoder to selectively focus on different parts of the source at each generation step.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CrossAttention(nn.Module):
    def __init__(self, d_model=512, n_heads=8):
        super().__init__()
        self.n_heads, self.d_head = n_heads, d_model // n_heads
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.kv_proj = nn.Linear(d_model, 2 * d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x_dec, enc_out):
        B, T_dec, C = x_dec.shape
        T_enc = enc_out.shape[1]
        q = self.q_proj(x_dec).view(B, T_dec, self.n_heads, self.d_head).transpose(1, 2)
        k, v = self.kv_proj(enc_out).split(C, dim=-1)
        k = k.view(B, T_enc, self.n_heads, self.d_head).transpose(1, 2)
        v = v.view(B, T_enc, self.n_heads, self.d_head).transpose(1, 2)
        att = F.softmax((q @ k.transpose(-2, -1)) * self.d_head ** -0.5, dim=-1)
        out = (att @ v).transpose(1, 2).contiguous().view(B, T_dec, C)
        return self.out_proj(out)

# Simulate encoder output and decoder query
enc_out = torch.randn(2, 20, 512)   # source: 20 tokens
dec_query = torch.randn(2, 5, 512)  # target prefix: 5 tokens
cross_attn = CrossAttention()
out = cross_attn(dec_query, enc_out)
print(f'Cross-attention output: {out.shape}')  # (2, 5, 512)
print(f'Each decoder position attends to all {enc_out.shape[1]} encoder positions')
```

## T5: Text-to-Text Transfer Transformer

T5 (Raffel et al. 2020) unifies all NLP tasks by framing them as text-to-text: the input is a task-prefixed string (e.g., 'summarize: ...', 'translate English to French: ...') and the output is always a string. This single architecture handles classification (output is a class label string), regression (output is a number string), and generation tasks uniformly. T5 replaces absolute position embeddings with learned relative position biases added to attention logits: attn_logit(i,j) += b(i−j), where b is a scalar bias indexed by relative distance.

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# T5 text-to-text fine-tuning example (illustrative)
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')
model.train()
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

# Simulate a summarization batch
input_texts = [
    'summarize: The quick brown fox jumps over the lazy dog. '
    'Foxes are known for their agility and speed.',
    'summarize: Neural networks learn representations from data. '
    'Deep networks stack multiple layers of nonlinear transformations.'
]
target_texts = ['Fox jumps over dog.', 'Neural nets learn from data.']

inputs = tokenizer(input_texts, return_tensors='pt', padding=True, truncation=True, max_length=128)
labels = tokenizer(target_texts, return_tensors='pt', padding=True).input_ids
labels[labels == tokenizer.pad_token_id] = -100  # ignore padding in loss

outputs = model(**inputs, labels=labels)
print(f'Loss: {outputs.loss.item():.4f}')
outputs.loss.backward()
optimizer.step(); optimizer.zero_grad()
print(f'T5-small params: {sum(p.numel() for p in model.parameters()):,}')
```

## BART: Denoising Autoencoder

BART (Lewis et al. 2020) pretrained an encoder-decoder by corrupting input text and training the model to reconstruct the original. The encoder is bidirectional BERT-style; the decoder is GPT-style autoregressive. Corruption strategies include: token masking (like BERT), token deletion, text infilling (replace a span with one MASK token), sentence permutation, and document rotation. BART's pretraining objective makes its decoder particularly well-suited for generation tasks — it already knows how to produce fluent text conditioned on a noisy input.

> **BART vs T5 Task Strengths**: BART excels at generation tasks (summarization, dialogue, translation) because its pretraining directly trains the decoder to generate fluent text. T5's text-to-text framing makes it stronger on classification-style tasks framed as generation (e.g., NLI, sentiment) because any label can be a token string. For ROUGE scores on CNN/DailyMail summarization, BART-large typically outperforms T5-large by 1-2 ROUGE points.

```python
from transformers import BartForConditionalGeneration, BartTokenizer
import torch

tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-base')
model.eval()

article = (
    'Transformer models have revolutionized natural language processing. '
    'Originally proposed for machine translation, they now dominate tasks ranging '
    'from text classification to open-ended generation. The key innovation is the '
    'attention mechanism, which allows every token to attend to every other token.'
)

inputs = tokenizer(article, return_tensors='pt', max_length=512, truncation=True)
with torch.no_grad():
    summary_ids = model.generate(
        inputs['input_ids'],
        num_beams=4,
        max_length=60,
        min_length=10,
        length_penalty=2.0,
        early_stopping=True
    )
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(f'Article length: {len(article.split())} words')
print(f'Summary: {summary}')
print(f'BART-base params: {sum(p.numel() for p in model.parameters()):,}')
```

## Comparing BART vs T5 vs GPT-2 on Summarization

```python
# Simulated ROUGE comparison (representative published numbers)
import numpy as np

models = ['GPT-2 (117M)', 'T5-base (250M)', 'T5-large (770M)', 'BART-base (140M)', 'BART-large (400M)']
# CNN/DailyMail ROUGE-1, ROUGE-2, ROUGE-L (approximate published values)
results = [
    [29.3, 8.6, 26.2],   # GPT-2 (fine-tuned)
    [42.5, 20.9, 39.8],  # T5-base fine-tuned
    [43.1, 21.6, 40.3],  # T5-large fine-tuned
    [44.2, 21.3, 40.9],  # BART-base fine-tuned
    [44.2, 21.3, 40.9],  # BART-large fine-tuned
]

print(f'{'Model':<25} {'R-1':>6} {'R-2':>6} {'R-L':>6}')
print('-' * 45)
for name, (r1, r2, rl) in zip(models, results):
    print(f'{name:<25} {r1:>6.1f} {r2:>6.1f} {rl:>6.1f}')

best_r1_idx = np.argmax([r[0] for r in results])
print(f'\nBest ROUGE-1: {models[best_r1_idx]} with {results[best_r1_idx][0]}')
print('BART-large and T5-large are both competitive; BART stronger on gen tasks.')
print('GPT-2 lags significantly — decoder-only without enc context is disadvantaged for summarization.')
```

## Architecture Comparison: Encoder Types

| Attribute | Encoder-Only (BERT) | Decoder-Only (GPT) | Encoder-Decoder (T5/BART) |
| --- | --- | --- | --- |
| Attention type | Bidirectional self-attention | Causal self-attention | Bidir encoder + causal decoder + cross-attn |
| Pretraining objective | MLM / NSP | Causal LM (NLL) | Text-to-text LM / denoising |
| Autoregressive generation | No | Yes | Yes (decoder side) |
| Input representation | Full context, best for understanding | Left-context only | Full source, autoregressive target |
| Inference cost | O(n) — single forward pass | O(n) per step; KV cache helps | O(n_src) encoder + O(n_tgt) per step decoder |
| Best tasks | Classification, NER, QA extractive | Open generation, chat, code | Translation, summarization, QA abstractive |
| Examples | BERT, RoBERTa, DeBERTa | GPT-2/3/4, LLaMA, Mistral | T5, BART, mT5, PEGASUS |

## T5-Specific Design Choices

T5 eliminates all bias terms from linear projections (no bias in Q, K, V, FFN, or output layers), which reduces parameters slightly and was found not to hurt performance. Instead of absolute position embeddings, T5 uses learned relative position biases: scalar offsets b(i−j) added to attention logits, indexed by relative distance and clipped to a maximum offset. These biases are shared across attention heads and across layers, making them extremely parameter-efficient. Relative position biases generalize better to sequence lengths longer than those seen during training — a key advantage over learned absolute positions.

## Cross-Attention Complexity and Inference Cost

Cross-attention has complexity O(S × T) where S is source length and T is target length. For long documents (S=8192) with long summaries (T=512), this is 4M attention computations per layer per head — not cheap. Decoder-only models avoid cross-attention entirely, which simplifies the architecture and reduces memory bandwidth. However, decoder-only models must fit the entire source into their context window as prefix text, which also has O(n²) attention cost. For very long source + short target tasks, encoder-decoder is competitive because the encoder processes source once.

- T5 relative position bias: bias b(i-j) added to attention logits; shared across heads; generalizes to unseen lengths.
- BART positional embeddings: learned absolute positions (like GPT-2), max 1024 by default.
- T5 uses no bias terms in any linear projection — a design choice that reduces parameters slightly.
- BART encoder uses BERT-style architecture with pre-trained weights; decoder uses GPT-style causal masking.
- Beam search is standard for encoder-decoder generation; decoder-only typically uses sampling instead.

Encoder-decoder architectures remain the preferred choice for structured generation tasks with long inputs and short outputs — particularly document summarization, controlled translation, and data-to-text generation — where the bidirectional encoder produces richer source representations than a decoder-only prefix. As context windows for decoder-only models have grown to 128K+ tokens, the architectural advantage of encoder-decoder has narrowed, and many practical systems now simply prepend the source as context for a decoder-only model.

---

