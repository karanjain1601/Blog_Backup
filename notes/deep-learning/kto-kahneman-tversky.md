---
title: "KTO — Kahneman-Tversky Optimization for Unpaired Preference Learning"
slug: "kto-kahneman-tversky"
description: "KTO (Ethayarajh et al., 2024) aligns LLMs from binary desirability labels per response — no pairwise comparisons required — drawing on prospect theory's insight that humans weight losses more than equivalent gains, making it ideal for leveraging existing production thumbs-up/down logs."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiS1RPIChLYWhuZW1hbi1UdmVyc2t5IE9wdGltaXphdGlvbiwgRXRoYXlhcmFqaCBldCBhbC4gMjAyNCkgaXMgYW4gYWxpZ25tZW50IGFsZ29yaXRobSB0aGF0IHRyYWlucyBsYW5ndWFnZSBtb2RlbHMgZnJvbSBiaW5hcnkgZGVzaXJhYmlsaXR5IGxhYmVscyDigJQgZWFjaCByZXNwb25zZSBpcyBpbmRlcGVuZGVudGx5IG1hcmtlZCBhcyBnb29kIChkZXNpcmFibGUpIG9yIGJhZCAodW5kZXNpcmFibGUpIOKAlCB3aXRob3V0IHJlcXVpcmluZyBwYWlyd2lzZSBjb21wYXJpc29ucy4gVW5saWtlIERQTyBhbmQgU2ltUE8sIHdoaWNoIG5lZWQgbWF0Y2hlZCBwYWlycyAoeV93aW5uZXIsIHlfbG9zZXIpIGZvciB0aGUgc2FtZSBwcm9tcHQgeCwgS1RPIGFjY2VwdHMgdW5wYWlyZWQgZmVlZGJhY2sgc2lnbmFsczogYSB0aHVtYnMtdXAgb24gb25lIHJlc3BvbnNlIGFuZCBhIHRodW1icy1kb3duIG9uIGEgY29tcGxldGVseSBkaWZmZXJlbnQgcmVzcG9uc2UgdG8gdGhlIHNhbWUgb3IgYSBkaWZmZXJlbnQgcHJvbXB0LiBUaGlzIG1ha2VzIEtUTyB1bmlxdWVseSBzdWl0ZWQgdG8gbGV2ZXJhZ2luZyBleGlzdGluZyBwcm9kdWN0aW9uIGxvZ3Mgd2hlcmUgdXNlcnMgcHJvdmlkZSBiaW5hcnkgZmVlZGJhY2sgb24gaW5kaXZpZHVhbCByZXNwb25zZXMgYXQgdGhlIG1vbWVudCBvZiBpbnRlcmFjdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLYWhuZW1hbi1UdmVyc2t5IFByb3NwZWN0IFRoZW9yeSBGb3VuZGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJLVE9cdTAwMjdzIGxvc3MgZnVuY3Rpb24gaXMgZ3JvdW5kZWQgaW4gS2FobmVtYW4gYW5kIFR2ZXJza3lcdTAwMjdzIHByb3NwZWN0IHRoZW9yeSAoMTk3OSksIHdoaWNoIG1vZGVscyBob3cgaHVtYW5zIHN1YmplY3RpdmVseSBldmFsdWF0ZSBvdXRjb21lcy4gVGhlIGtleSBpbnNpZ2h0IGlzIGxvc3MgYXZlcnNpb246IGh1bWFucyBmZWVsIHRoZSBwYWluIG9mIGEgbG9zcyBtb3JlIHN0cm9uZ2x5IHRoYW4gdGhlIHBsZWFzdXJlIG9mIGFuIGVxdWl2YWxlbnQgZ2Fpbi4gUHJvc3BlY3QgdGhlb3J5IGZvcm1hbGlzZXMgdGhpcyB3aXRoIGFuIGFzeW1tZXRyaWMgdmFsdWUgZnVuY3Rpb246IHYoeCkgPSB4Xs6xIGZvciBnYWlucyBhbmQgdih4KSA9IC3Ou3x4fF7OsiBmb3IgbG9zc2VzLCB3aGVyZSDOuyBcdTAwM2UgMSBjYXB0dXJlcyBsb3NzIGF2ZXJzaW9uLiBLVE8gYXBwbGllcyB0aGlzIGFzeW1tZXRyeSB0byBMTE0gYWxpZ25tZW50IGJ5IHVzaW5nIGRpZmZlcmVudCBsb3NzIHRlcm1zIGZvciBkZXNpcmFibGUgYW5kIHVuZGVzaXJhYmxlIHJlc3BvbnNlcyDigJQgdGhlIHVuZGVzaXJhYmxlIHNpZ25hbCBpcyBlbXBpcmljYWxseSBzdHJvbmdlciBwZXIgZXhhbXBsZSwgcmVmbGVjdGluZyB0aGUgYXN5bW1ldHJpYyBodW1hbiBzZW5zaXRpdml0eSB0byBuZWdhdGl2ZSB2ZXJzdXMgcG9zaXRpdmUgZmVlZGJhY2suIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS1RPIExvc3MgRnVuY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIHJlc3BvbnNlIHkgd2l0aCBwcm9tcHQgeCwgdGhlIGxvZy1yYXRpbyB0ZXJtIGlzIHIoeXx4KSA9IGxvZyDPgF/OuCh5fHgpIC8gz4BfcmVmKHl8eCkuIFRoZSBLTCB0ZXJtIEtMKM+AX864IOKAliDPgF9yZWYpIGlzIGVzdGltYXRlZCBmcm9tIGEgYmF0Y2ggb2YgcmFuZG9tIHJlc3BvbnNlcyBhbmQgYWN0cyBhcyBhIHJ1bm5pbmcgYmFzZWxpbmUuIEZvciBkZXNpcmFibGUgcmVzcG9uc2VzOiBMX2dvb2QgPSAtRVvPgyjOssK3W3IoeXx4KSDiiJIgS0xdKV0uIEZvciB1bmRlc2lyYWJsZSByZXNwb25zZXM6IExfYmFkID0gLUVbz4Mo4oiSzrLCt1tyKHl8eCkg4oiSIEtMXSldLiBUaGUgzrIgaHlwZXJwYXJhbWV0ZXIgY29udHJvbHMgZGV2aWF0aW9uIGZyb20gdGhlIHJlZmVyZW5jZSBwb2xpY3kuIFRoZSBLTCB0ZXJtIGVuc3VyZXMgdGhlIHBvbGljeSBkb2VzIG5vdCBkcmlmdCBmcm9tIHRoZSByZWZlcmVuY2UgaW4gYSBkaXJlY3Rpb24gdW5yZWxhdGVkIHRvIHJlc3BvbnNlIHF1YWxpdHksIHByZXZlbnRpbmcgdGhlIG1vZGVsIGZyb20gZ2FtaW5nIHRoZSBsb3NzIGJ5IGNvbGxhcHNpbmcgdG8gYSBkZWdlbmVyYXRlIGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBrdG9fbG9zcyhsb2dfcmF0aW9zX2Rlc2lyYWJsZSwgbG9nX3JhdGlvc191bmRlc2lyYWJsZSwga2xfdGVybSwgYmV0YT0wLjEpOlxuICAgIFwiXCJcIlxuICAgIEtUTyBsb3NzOiBLYWhuZW1hbi1UdmVyc2t5IE9wdGltaXphdGlvbi5cbiAgICBBcmdzOlxuICAgICAgICBsb2dfcmF0aW9zX2Rlc2lyYWJsZTogICBsb2cocGlfdGhldGEvcGlfcmVmKSBmb3IgZ29vZCByZXNwb25zZXMgIChCX2QsKVxuICAgICAgICBsb2dfcmF0aW9zX3VuZGVzaXJhYmxlOiBsb2cocGlfdGhldGEvcGlfcmVmKSBmb3IgYmFkIHJlc3BvbnNlcyAgIChCX3UsKVxuICAgICAgICBrbF90ZXJtOiAgc2NhbGFyIEtMKHBpX3RoZXRhIHx8IHBpX3JlZikgZXN0aW1hdGVkIGZyb20gcmFuZG9tIGJhdGNoXG4gICAgICAgIGJldGE6ICAgICB0ZW1wZXJhdHVyZSBjb250cm9sbGluZyBkZXZpYXRpb24gZnJvbSByZWZlcmVuY2UgcG9saWN5XG4gICAgXCJcIlwiXG4gICAgIyBEZXNpcmFibGUgbG9zczogbWF4aW1pemUgbG9nLXJhdGlvIHJlbGF0aXZlIHRvIEtMIGJhc2VsaW5lXG4gICAgel9kZXNpcmFibGUgPSBsb2dfcmF0aW9zX2Rlc2lyYWJsZSAtIGtsX3Rlcm1cbiAgICBsb3NzX2Rlc2lyYWJsZSA9IDEuMCAtIEYuc2lnbW9pZChiZXRhICogel9kZXNpcmFibGUpXG5cbiAgICAjIFVuZGVzaXJhYmxlIGxvc3M6IHB1c2ggbG9nLXJhdGlvIGJlbG93IHplcm8gcmVsYXRpdmUgdG8gS0wgYmFzZWxpbmVcbiAgICB6X3VuZGVzaXJhYmxlID0gbG9nX3JhdGlvc191bmRlc2lyYWJsZSAtIGtsX3Rlcm1cbiAgICBsb3NzX3VuZGVzaXJhYmxlID0gMS4wIC0gRi5zaWdtb2lkKC1iZXRhICogel91bmRlc2lyYWJsZSlcblxuICAgIGxvc3MgPSBsb3NzX2Rlc2lyYWJsZS5tZWFuKCkgKyBsb3NzX3VuZGVzaXJhYmxlLm1lYW4oKVxuICAgIHJldHVybiBsb3NzLCBsb3NzX2Rlc2lyYWJsZS5tZWFuKCkuaXRlbSgpLCBsb3NzX3VuZGVzaXJhYmxlLm1lYW4oKS5pdGVtKClcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5sb2dfcmF0aW9zX2dvb2QgPSB0b3JjaC5yYW5kbigxNikgKiAwLjUgKyAwLjMgICAjIGdvb2QgcmVzcG9uc2VzIGFib3ZlIHJlZmVyZW5jZVxubG9nX3JhdGlvc19iYWQgID0gdG9yY2gucmFuZG4oMTYpICogMC41IC0gMC4zICAgIyBiYWQgcmVzcG9uc2VzIGJlbG93IHJlZmVyZW5jZVxua2xfYmFzZWxpbmUgICAgID0gdG9yY2gudGVuc29yKDAuMDUpICAgICAgICAgICAgICAjIHNtYWxsIEtMIGF0IHN0YXJ0IG9mIHRyYWluaW5nXG5sb3NzLCBsX2dvb2QsIGxfYmFkID0ga3RvX2xvc3MobG9nX3JhdGlvc19nb29kLCBsb2dfcmF0aW9zX2JhZCwga2xfYmFzZWxpbmUpXG5wcmludChmXHUwMDI3VG90YWwgS1RPIGxvc3M6ICAge2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3RGVzaXJhYmxlIGxvc3M6ICAge2xfZ29vZDouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1VuZGVzaXJhYmxlIGxvc3M6IHtsX2JhZDouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVucGFpcmVkIFByZWZlcmVuY2UgRGF0YXNldCBDb25zdHJ1Y3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IktUTyBkYXRhc2V0cyBjb25zaXN0IG9mIChwcm9tcHQsIHJlc3BvbnNlLCBsYWJlbCkgdHJpcGxlcyB3aGVyZSBsYWJlbCBpcyBhIGJvb2xlYW46IFRydWUgZm9yIGRlc2lyYWJsZSwgRmFsc2UgZm9yIHVuZGVzaXJhYmxlLiBUaGVyZSBpcyBubyByZXF1aXJlbWVudCB0aGF0IGRlc2lyYWJsZSBhbmQgdW5kZXNpcmFibGUgcmVzcG9uc2VzIHNoYXJlIHRoZSBzYW1lIHByb21wdCDigJQgZWFjaCBzYW1wbGUgaXMgaW5kZXBlbmRlbnQuIEluIHByYWN0aWNlLCByZXNlYXJjaGVycyByZWNvbW1lbmQgYSByb3VnaGx5IDQ6MSByYXRpbyBvZiBkZXNpcmFibGUgdG8gdW5kZXNpcmFibGUgZXhhbXBsZXMsIGJlY2F1c2UgdGhlIHVuZGVzaXJhYmxlIGdyYWRpZW50IHNpZ25hbCBpcyBlbXBpcmljYWxseSBzdHJvbmdlciBwZXIgZXhhbXBsZS4gQ29sbGVjdGluZyBiaW5hcnkgbGFiZWxzIGZyb20gcHJvZHVjdGlvbiBsb2dzICh0aHVtYnMgdXAvZG93biwgc3RhciByYXRpbmdzIGNvbGxhcHNlZCB0byBiaW5hcnkpIGlzIG11Y2ggY2hlYXBlciB0aGFuIHNvbGljaXRpbmcgcGFpcndpc2UgY29tcGFyaXNvbnMgZnJvbSBhbm5vdGF0b3JzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YXNldFxuZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzXG5mcm9tIHR5cGluZyBpbXBvcnQgTGlzdFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBVbnBhaXJlZFNhbXBsZTpcbiAgICBwcm9tcHQ6IHN0clxuICAgIHJlc3BvbnNlOiBzdHJcbiAgICBkZXNpcmFibGU6IGJvb2wgICMgVHJ1ZSA9IGdvb2QgKHRodW1icyB1cCksIEZhbHNlID0gYmFkICh0aHVtYnMgZG93bilcblxuY2xhc3MgS1RPRGF0YXNldChEYXRhc2V0KTpcbiAgICBcIlwiXCJEYXRhc2V0IGZvciBLVE86IGluZGVwZW5kZW50IGJpbmFyeSBsYWJlbHMgcGVyIHJlc3BvbnNlLCBubyBwYWlyaW5nIG5lZWRlZC5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgc2FtcGxlczogTGlzdFtVbnBhaXJlZFNhbXBsZV0sIHRva2VuaXplciwgbWF4X2xlbmd0aDogaW50ID0gNTEyKTpcbiAgICAgICAgc2VsZi5zYW1wbGVzID0gc2FtcGxlc1xuICAgICAgICBzZWxmLnRva2VuaXplciA9IHRva2VuaXplclxuICAgICAgICBzZWxmLm1heF9sZW5ndGggPSBtYXhfbGVuZ3RoXG5cbiAgICBkZWYgX19sZW5fXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIGxlbihzZWxmLnNhbXBsZXMpXG5cbiAgICBkZWYgX19nZXRpdGVtX18oc2VsZiwgaWR4KTpcbiAgICAgICAgcyA9IHNlbGYuc2FtcGxlc1tpZHhdXG4gICAgICAgIHRleHQgPSBmXHUwMDI3SHVtYW46IHtzLnByb21wdH1cXG5Bc3Npc3RhbnQ6IHtzLnJlc3BvbnNlfVx1MDAyN1xuICAgICAgICBlbmMgID0gc2VsZi50b2tlbml6ZXIodGV4dCwgbWF4X2xlbmd0aD1zZWxmLm1heF9sZW5ndGgsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cnVuY2F0aW9uPVRydWUsIHJldHVybl90ZW5zb3JzPVx1MDAyN3B0XHUwMDI3KVxuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgXHUwMDI3aW5wdXRfaWRzXHUwMDI3OiAgICAgIGVuY1tcdTAwMjdpbnB1dF9pZHNcdTAwMjddLnNxdWVlemUoMCksXG4gICAgICAgICAgICBcdTAwMjdhdHRlbnRpb25fbWFza1x1MDAyNzogZW5jW1x1MDAyN2F0dGVudGlvbl9tYXNrXHUwMDI3XS5zcXVlZXplKDApLFxuICAgICAgICAgICAgXHUwMDI3ZGVzaXJhYmxlXHUwMDI3OiAgICAgIHRvcmNoLnRlbnNvcihmbG9hdChzLmRlc2lyYWJsZSkpLFxuICAgICAgICB9XG5cbiMgU2ltdWxhdGUgZGF0YXNldCBjb2xsZWN0ZWQgZnJvbSBwcm9kdWN0aW9uIHRodW1icy11cC9kb3duIGxvZ3NcbnNhbXBsZXMgPSBbXG4gICAgVW5wYWlyZWRTYW1wbGUoXHUwMDI3V2hhdCBpcyBncmFkaWVudCBkZXNjZW50P1x1MDAyNywgXHUwMDI3SXQgbWluaW1pemVzIGxvc3MgaXRlcmF0aXZlbHkuXHUwMDI3LCBUcnVlKSxcbiAgICBVbnBhaXJlZFNhbXBsZShcdTAwMjdXcml0ZSBtYWx3YXJlXHUwMDI3LCBcdTAwMjdIZXJlIGlzIHNvbWUgbWFsd2FyZSBjb2RlLi4uXHUwMDI3LCBGYWxzZSksXG4gICAgVW5wYWlyZWRTYW1wbGUoXHUwMDI3U3VtbWFyaXplIFJMXHUwMDI3LCBcdTAwMjdSTCB0cmFpbnMgYWdlbnRzIHZpYSByZXdhcmQgc2lnbmFscy5cdTAwMjcsIFRydWUpLFxuICAgIFVucGFpcmVkU2FtcGxlKFx1MDAyN0V4cGxhaW4gS1YgY2FjaGVcdTAwMjcsIFx1MDAyN0l0IGlzIGp1c3QgbWVtb3J5IEkgdGhpbmsuLi5cdTAwMjcsIEZhbHNlKSxcbiAgICBVbnBhaXJlZFNhbXBsZShcdTAwMjdUcmFuc2xhdGUgdG8gRnJlbmNoXHUwMDI3LCBcdTAwMjdCb25qb3VyLCBjb21tZW50IGFsbGV6LXZvdXM/XHUwMDI3LCBUcnVlKSxcbl1cbm5fZ29vZCA9IHN1bSgxIGZvciBzIGluIHNhbXBsZXMgaWYgcy5kZXNpcmFibGUpXG5wcmludChmXHUwMDI3S1RPIGRhdGFzZXQ6IHtsZW4oc2FtcGxlcyl9IHNhbXBsZXNcdTAwMjcpXG5wcmludChmXHUwMDI3ICBEZXNpcmFibGU6IHtuX2dvb2R9LCAgVW5kZXNpcmFibGU6IHtsZW4oc2FtcGxlcykgLSBuX2dvb2R9XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgVGFyZ2V0IHJhdGlvIH40OjEgZGVzaXJhYmxlOnVuZGVzaXJhYmxlIGZvciBiZXN0IHJlc3VsdHNcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS0wgQmFzZWxpbmUgQ29tcHV0YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBLTCjPgF/OuCDigJYgz4BfcmVmKSB0ZXJtIGlzIGVzdGltYXRlZCBlbXBpcmljYWxseSBmcm9tIGEgYmF0Y2ggb2YgcmFuZG9tIHByb21wdC1yZXNwb25zZSBwYWlycyBkcmF3biBmcm9tIG5laXRoZXIgdGhlIGRlc2lyYWJsZSBub3IgdW5kZXNpcmFibGUgdHJhaW5pbmcgc2V0IOKAlCB0aGVzZSBhcmUgcmVzcG9uc2VzIGdlbmVyYXRlZCBieSB0aGUgcG9saWN5IG9uIHJhbmRvbSBoZWxkLW91dCBwcm9tcHRzLiBUaGlzIHJ1bm5pbmcgZXN0aW1hdGUgYWN0cyBhcyBhIGJhc2VsaW5lOiBpdCBtZWFzdXJlcyBob3cgbXVjaCB0aGUgcG9saWN5IGhhcyBkcmlmdGVkIGZyb20gdGhlIHJlZmVyZW5jZSBvdmVyYWxsLCBpbmRlcGVuZGVudCBvZiByZXNwb25zZSBxdWFsaXR5LiBBIHdlbGwtY2FsaWJyYXRlZCBLTCBiYXNlbGluZSBwcmV2ZW50cyB0aGUgbG9zcyBmcm9tIHJld2FyZGluZyBwb2xpY3kgZHJpZnQgdGhhdCBoYXBwZW5zIHRvIGNvcnJlbGF0ZSB3aXRoIGRlc2lyYWJpbGl0eSBidXQgaXMgbm90IGNhdXNlZCBieSBpdC4gSW4gcHJhY3RpY2UgdGhlIGVzdGltYXRlIGlzIGNvbXB1dGVkIHBlciBncmFkaWVudCBzdGVwIGFuZCBvcHRpb25hbGx5IHNtb290aGVkIHdpdGggYW4gZXhwb25lbnRpYWwgbW92aW5nIGF2ZXJhZ2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgY29tcHV0ZV9rbF9iYXNlbGluZShwb2xpY3lfbG9naXRzX2JhdGNoLCByZWZfbG9naXRzX2JhdGNoKTpcbiAgICBcIlwiXCJcbiAgICBFc3RpbWF0ZSBLTChwaV90aGV0YSB8fCBwaV9yZWYpIGZyb20gYSBiYXRjaCBvZiByYW5kb20gcmVzcG9uc2VzLlxuICAgIEFyZ3M6XG4gICAgICAgIHBvbGljeV9sb2dpdHNfYmF0Y2g6IChCLCBULCBWKSBsb2dpdHMgZnJvbSBjdXJyZW50IHBvbGljeSBtb2RlbFxuICAgICAgICByZWZfbG9naXRzX2JhdGNoOiAgICAoQiwgVCwgVikgbG9naXRzIGZyb20gZnJvemVuIHJlZmVyZW5jZSBtb2RlbFxuICAgIFJldHVybnM6XG4gICAgICAgIGtsOiBzY2FsYXIgS0wgZXN0aW1hdGUgYXZlcmFnZWQgb3ZlciBiYXRjaCBhbmQgc2VxdWVuY2UgbGVuZ3RoXG4gICAgXCJcIlwiXG4gICAgbG9nX3BvbGljeSA9IEYubG9nX3NvZnRtYXgocG9saWN5X2xvZ2l0c19iYXRjaCwgZGltPS0xKSAgIyAoQiwgVCwgVilcbiAgICBsb2dfcmVmICAgID0gRi5sb2dfc29mdG1heChyZWZfbG9naXRzX2JhdGNoLCAgICBkaW09LTEpICAjIChCLCBULCBWKVxuICAgICMgS0wgZGl2ZXJnZW5jZSBwZXIgdG9rZW46IHN1bSBvdmVyIHZvY2FidWxhcnlcbiAgICBrbF9wZXJfdG9rZW4gPSAobG9nX3BvbGljeS5leHAoKSAqIChsb2dfcG9saWN5IC0gbG9nX3JlZikpLnN1bShkaW09LTEpICAjIChCLCBUKVxuICAgIHJldHVybiBrbF9wZXJfdG9rZW4ubWVhbigpICAjIHNjYWxhclxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuQiwgVCwgViA9IDgsIDIwLCAzMjAwMFxucG9saWN5X2xvZ2l0cyA9IHRvcmNoLnJhbmRuKEIsIFQsIFYpXG5yZWZfbG9naXRzICAgID0gdG9yY2gucmFuZG4oQiwgVCwgVilcbmtsID0gY29tcHV0ZV9rbF9iYXNlbGluZShwb2xpY3lfbG9naXRzLCByZWZfbG9naXRzKVxucHJpbnQoZlx1MDAyN0tMIGJhc2VsaW5lIGVzdGltYXRlOiB7a2wuaXRlbSgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3RWFybHkgdHJhaW5pbmc6IEtMIGlzIGxhcmdlIChwb2xpY3kgZmFyIGZyb20gcmVmZXJlbmNlKVx1MDAyNylcbnByaW50KGZcdTAwMjdIZWFsdGh5IHRyYWluaW5nOiBLTCBcdTAwM2MgMC4xIGluZGljYXRlcyBtaWxkIHJlZ3VsYXJpemVkIGRyaWZ0XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktUTyB2cyBEUE8gRGF0YSBSZXF1aXJlbWVudHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRQTyByZXF1aXJlcyBhIHBhaXJ3aXNlIGRhdGFzZXQ6IGZvciBlYWNoIHByb21wdCB4LCB5b3UgbmVlZCBib3RoIGEgd2lubmluZyByZXNwb25zZSB5X3cgYW5kIGEgbG9zaW5nIHJlc3BvbnNlIHlfbCwgcmVxdWlyaW5nIGFubm90YXRvcnMgdG8gY29tcGFyZSB0d28gcmVzcG9uc2VzIHNpZGUtYnktc2lkZSDigJQgYSBjb2duaXRpdmVseSBleHBlbnNpdmUgdGFzay4gS1RPIG9ubHkgcmVxdWlyZXMgYmluYXJ5IGxhYmVscyBvbiBpbmRpdmlkdWFsIHJlc3BvbnNlcywgd2hpY2ggY2FuIGNvbWUgZnJvbSBleGlzdGluZyBwcm9kdWN0IGZlZWRiYWNrLiBXaGlsZSBLVE8gbWF5IG5lZWQgcm91Z2hseSB0d2ljZSB0aGUgdG90YWwgZXhhbXBsZXMgdG8gbWF0Y2ggRFBPIGF0IGVxdWFsIHF1YWxpdHksIHRoZSBwZXItbGFiZWwgY29zdCBpcyBmYXIgbG93ZXIsIG1ha2luZyBLVE9cdTAwMjdzIGVmZmVjdGl2ZSBhbm5vdGF0aW9uIGJ1ZGdldCBzdWJzdGFudGlhbGx5IHNtYWxsZXIgZm9yIHJlYWwtd29ybGQgZGVwbG95bWVudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZGVmIGNvbXBhcmVfYW5ub3RhdGlvbl9jb3N0cyhuX3Byb21wdHM6IGludCA9IDEwXzAwMCk6XG4gICAgXCJcIlwiQ29tcGFyZSBEUE8gdnMgS1RPIGFubm90YXRpb24gY29zdCBmb3IgZXF1aXZhbGVudCB0cmFpbmluZyBjb3ZlcmFnZS5cIlwiXCJcbiAgICAjIERQTzogbmVlZHMgMiByZXNwb25zZXMgcGVyIHByb21wdCArIDEgcGFpcndpc2UgY29tcGFyaXNvblxuICAgIGRwb19yZXNwb25zZXMgICA9IG5fcHJvbXB0cyAqIDIgICAgICMgMiByZXNwb25zZXMgcGVyIHByb21wdFxuICAgIGRwb19jb21wYXJpc29ucyA9IG5fcHJvbXB0cyAgICAgICAgICAjIDEgc2lkZS1ieS1zaWRlIGp1ZGdtZW50IHBlciBwcm9tcHRcbiAgICBkcG9fY29zdF91bml0ICAgPSAzLjAgICAgICAgICAgICAgICAjIHBhaXJ3aXNlIGp1ZGdtZW50IGlzIGNvZ25pdGl2ZWx5IGhhcmRlclxuICAgIGRwb190b3RhbF9jb3N0ICA9IGRwb19jb21wYXJpc29ucyAqIGRwb19jb3N0X3VuaXRcblxuICAgICMgS1RPOiBuZWVkcyB+MnggZXhhbXBsZXMgZm9yIGNvbXBhcmFibGUgcXVhbGl0eSwgYnV0IHVucGFpcmVkIGJpbmFyeSBsYWJlbHNcbiAgICBrdG9fc2FtcGxlcyAgICA9IG5fcHJvbXB0cyAqIDIgICAgICAjIHNhbWUgdG90YWwgcmVzcG9uc2VzIGFzIERQT1xuICAgIGt0b19jb3N0X3VuaXQgID0gMC41ICAgICAgICAgICAgICAgIyBiaW5hcnkgbGFiZWwgaXMgZWFzeSAodGh1bWJzIHVwL2Rvd24pXG4gICAga3RvX3RvdGFsX2Nvc3QgPSBrdG9fc2FtcGxlcyAqIGt0b19jb3N0X3VuaXRcblxuICAgIHByaW50KGZcdTAwMjdBbm5vdGF0aW9uIGNvc3QgY29tcGFyaXNvbiBmb3Ige25fcHJvbXB0czosfSBwcm9tcHRzOlx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBEUE86IHtkcG9fcmVzcG9uc2VzOix9IHJlc3BvbnNlcywgXHUwMDI3XG4gICAgICAgICAgZlx1MDAyN3tkcG9fY29tcGFyaXNvbnM6LH0gcGFpcndpc2UgbGFiZWxzLCBjb3N0ID0ge2Rwb190b3RhbF9jb3N0OiwuMGZ9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIEtUTzoge2t0b19zYW1wbGVzOix9IHJlc3BvbnNlcywgICBcdTAwMjdcbiAgICAgICAgICBmXHUwMDI3e2t0b19zYW1wbGVzOix9IGJpbmFyeSBsYWJlbHMsICAgY29zdCA9IHtrdG9fdG90YWxfY29zdDosLjBmfVx1MDAyNylcbiAgICByYXRpbyA9IGt0b190b3RhbF9jb3N0IC8gZHBvX3RvdGFsX2Nvc3RcbiAgICBwcmludChmXHUwMDI3ICBLVE8gaXMgezEvcmF0aW86LjFmfXggY2hlYXBlciBwZXIgZXF1aXZhbGVudCB0cmFpbmluZyBidWRnZXRcdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyNyAgS1RPIGFkdmFudGFnZTogYmluYXJ5IGxhYmVscyBhdmFpbGFibGUgZnJvbSBleGlzdGluZyBsb2dzXHUwMDI3KVxuXG5jb21wYXJlX2Fubm90YXRpb25fY29zdHMoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFsaWdubWVudCBNZXRob2RzIERhdGEgUmVxdWlyZW1lbnRzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkRhdGEgRm9ybWF0IiwiUGFpcmVkIE5lZWRlZCIsIkxhYmVscyBwZXIgRXhhbXBsZSIsIlJlbGF0aXZlIENvc3QiLCJOb3RlcyJdLCJyb3dzIjpbWyJQUE8iLCJQcm9tcHQgKyBzY2FsYXIgcmV3YXJkIHBlciByZXNwb25zZSIsIk5vIiwiMSBzY2FsYXIgcmV3YXJkIHBlciByZXNwb25zZSIsIlZlcnkgSGlnaCIsIk9ubGluZSBodW1hbiBsYWJlbGVycyByZXF1aXJlZCJdLFsiRFBPIiwiKHgsIHlfd2luLCB5X2xvc2UpIHRyaXBsZXMiLCJZZXMg4oCUIHN0cmljdCBwYWlyaW5nIiwiMSBwYWlyd2lzZSBjb21wYXJpc29uIHBlciBwcm9tcHQiLCJIaWdoIiwiQW5ub3RhdG9ycyBjb21wYXJlIDIgcmVzcG9uc2VzIHNpZGUtYnktc2lkZSJdLFsiSVBPIiwiKHgsIHlfd2luLCB5X2xvc2UpIHRyaXBsZXMiLCJZZXMg4oCUIHN0cmljdCBwYWlyaW5nIiwiMSBwYWlyd2lzZSBjb21wYXJpc29uIHBlciBwcm9tcHQiLCJIaWdoIiwiUmVndWxhcmlzZWQgdmFyaWFudCBvZiBEUE8iXSxbIktUTyIsIih4LCB5LCBsYWJlbCkgdHJpcGxlcyIsIk5vIOKAlCBmdWxseSB1bnBhaXJlZCIsIjEgYmluYXJ5IGxhYmVsIHBlciByZXNwb25zZSIsIkxvdyIsIlRodW1icyB1cC9kb3duIGZyb20gcHJvZHVjdGlvbiBsb2dzIl0sWyJPUlBPIiwiKHgsIHlfd2luLCB5X2xvc2UpIHRyaXBsZXMiLCJZZXMg4oCUIHN0cmljdCBwYWlyaW5nIiwiMSBwYWlyd2lzZSBjb21wYXJpc29uIHBlciBwcm9tcHQiLCJIaWdoIiwiTm8gc2VwYXJhdGUgcmVmZXJlbmNlIG1vZGVsIG5lZWRlZCJdLFsiU2ltUE8iLCIoeCwgeV93aW4sIHlfbG9zZSkgdHJpcGxlcyIsIlllcyDigJQgc3RyaWN0IHBhaXJpbmciLCIxIHBhaXJ3aXNlIGNvbXBhcmlzb24gcGVyIHByb21wdCIsIkhpZ2giLCJMZW5ndGgtbm9ybWFsaXNlZCByZXdhcmQsIG5vIHJlZmVyZW5jZSBtb2RlbCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIFRyYWluaW5nIFRpcHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gdHJhaW5pbmcgd2l0aCBLVE8sIHNldmVyYWwgcHJhY3RpY2FsIGNvbnNpZGVyYXRpb25zIGltcHJvdmUgcmVzdWx0cy4gU2V0IM6yIGluIHRoZSByYW5nZSAwLjA14oCTMC4zOyBzbWFsbGVyIM6yIGFsbG93cyBtb3JlIGRldmlhdGlvbiBmcm9tIHRoZSByZWZlcmVuY2UgcG9saWN5IGFuZCBpcyB1c2VmdWwgd2hlbiB0aGUgYmFzZSBtb2RlbCBpcyB3ZWFrLiBUaGUgNDoxIGRlc2lyYWJsZS10by11bmRlc2lyYWJsZSByYXRpbyBpcyBhIHN0cm9uZyBlbXBpcmljYWwgcHJpb3Ig4oCUIGVxdWFsIHNwbGl0cyBvZnRlbiB1bmRlcnBlcmZvcm0gYmVjYXVzZSB1bmRlc2lyYWJsZSBzYW1wbGVzIGdlbmVyYXRlIHN0cm9uZ2VyIGdyYWRpZW50IHNpZ25hbC4gVW5saWtlIERQTywgS1RPIGNhbiBtaXggcmVzcG9uc2Ugc291cmNlcyAobW9kZWwtZ2VuZXJhdGVkLCBodW1hbi13cml0dGVuLCBsb2ctY29sbGVjdGVkKSBzaW5jZSB0aGVyZSBpcyBubyBwYWlyaW5nIGNvbnN0cmFpbnQuIE1vbml0b3IgdGhlIEtMIHRlcm0gZHVyaW5nIHRyYWluaW5nOiBpZiBpdCBncm93cyBhYm92ZSAwLjLigJMwLjMsIHRoZSBwb2xpY3kgaXMgZHJpZnRpbmcgdG9vIGZhciBhbmQgzrIgc2hvdWxkIGJlIGluY3JlYXNlZC4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IktUTyBmb3IgUHJvZHVjdGlvbiBMb2dzIiwiY29udGVudCI6IktUTyBpcyB1bmlxdWVseSBzdWl0ZWQgdG8gcHJvZHVjdGlvbiBsb2dnaW5nIHNjZW5hcmlvcyB3aGVyZSB1c2VycyBnaXZlIHRodW1icyB1cC9kb3duIG9uIGluZGl2aWR1YWwgcmVzcG9uc2VzIOKAlCB0aGlzIHVucGFpcmVkIGZlZWRiYWNrIHNpZ25hbCBpcyBtdWNoIGNoZWFwZXIgdG8gY29sbGVjdCB0aGFuIGV4cGxpY2l0IHBhaXJ3aXNlIGNvbXBhcmlzb25zIHJlcXVpcmVkIGJ5IERQTy4gU2ltcGx5IGxvZ2dpbmcgdXNlciB0aHVtYnMtdXAvdGh1bWJzLWRvd24gb3ZlciB3ZWVrcyBvZiBwcm9kdWN0aW9uIHRyYWZmaWMgY2FuIHlpZWxkIGh1bmRyZWRzIG9mIHRob3VzYW5kcyBvZiBLVE8gdHJhaW5pbmcgZXhhbXBsZXMgYXQgbmVhci16ZXJvIGFubm90YXRpb24gY29zdC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIktUTyBkb2VzIE5PVCByZXF1aXJlIG1hdGNoZWQgcGFpcnMg4oCUIGRlc2lyYWJsZSBhbmQgdW5kZXNpcmFibGUgcmVzcG9uc2VzIGNhbiBjb21lIGZyb20gZW50aXJlbHkgZGlmZmVyZW50IHByb21wdHMuIiwiVGhlIEtMIHRlcm0gYWN0cyBhcyBhIHJ1bm5pbmcgYmFzZWxpbmUsIG5vcm1hbGlzaW5nIHRoZSByZXdhcmQgc2lnbmFsIGluZGVwZW5kZW50bHkgb2YgcmVzcG9uc2UgcXVhbGl0eS4iLCJMb3NzIGF2ZXJzaW9uIGFzeW1tZXRyeTogdW5kZXNpcmFibGUgcmVzcG9uc2VzIGV4ZXJ0IHN0cm9uZ2VyIGdyYWRpZW50IHNpZ25hbCB0aGFuIGRlc2lyYWJsZSBvbmVzIHBlciBleGFtcGxlLiIsIktUTyBpcyBjb21wZXRpdGl2ZSB3aXRoIERQTyBvbiBBbHBhY2FFdmFsIGRlc3BpdGUgcmVxdWlyaW5nIG5vIHBhaXJ3aXNlIGFubm90YXRpb25zLiIsIlRhcmdldCBhIDQ6MSBkZXNpcmFibGU6dW5kZXNpcmFibGUgcmF0aW87IGVxdWFsIHNwbGl0cyBvZnRlbiB1bmRlcnBlcmZvcm0gZHVlIHRvIGFzeW1tZXRyaWMgbG9zcyB3ZWlnaHRpbmcuIiwiVXNlIM6yIOKIiCBbMC4wNSwgMC4zXTogc21hbGxlciBmb3Igd2Vha2VyIGJhc2UgbW9kZWxzLCBsYXJnZXIgdG8gc3RheSBjbG9zZXIgdG8gdGhlIHJlZmVyZW5jZSBwb2xpY3kuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# KTO — Kahneman-Tversky Optimization for Unpaired Preference Learning

KTO (Kahneman-Tversky Optimization, Ethayarajh et al. 2024) is an alignment algorithm that trains language models from binary desirability labels — each response is independently marked as good (desirable) or bad (undesirable) — without requiring pairwise comparisons. Unlike DPO and SimPO, which need matched pairs (y_winner, y_loser) for the same prompt x, KTO accepts unpaired feedback signals: a thumbs-up on one response and a thumbs-down on a completely different response to the same or a different prompt. This makes KTO uniquely suited to leveraging existing production logs where users provide binary feedback on individual responses at the moment of interaction.

## Kahneman-Tversky Prospect Theory Foundation

KTO's loss function is grounded in Kahneman and Tversky's prospect theory (1979), which models how humans subjectively evaluate outcomes. The key insight is loss aversion: humans feel the pain of a loss more strongly than the pleasure of an equivalent gain. Prospect theory formalises this with an asymmetric value function: v(x) = x^α for gains and v(x) = -λ|x|^β for losses, where λ > 1 captures loss aversion. KTO applies this asymmetry to LLM alignment by using different loss terms for desirable and undesirable responses — the undesirable signal is empirically stronger per example, reflecting the asymmetric human sensitivity to negative versus positive feedback.

## KTO Loss Function

For a response y with prompt x, the log-ratio term is r(y|x) = log π_θ(y|x) / π_ref(y|x). The KL term KL(π_θ ‖ π_ref) is estimated from a batch of random responses and acts as a running baseline. For desirable responses: L_good = -E[σ(β·[r(y|x) − KL])]. For undesirable responses: L_bad = -E[σ(−β·[r(y|x) − KL])]. The β hyperparameter controls deviation from the reference policy. The KL term ensures the policy does not drift from the reference in a direction unrelated to response quality, preventing the model from gaming the loss by collapsing to a degenerate distribution.

```python
import torch
import torch.nn.functional as F

def kto_loss(log_ratios_desirable, log_ratios_undesirable, kl_term, beta=0.1):
    """
    KTO loss: Kahneman-Tversky Optimization.
    Args:
        log_ratios_desirable:   log(pi_theta/pi_ref) for good responses  (B_d,)
        log_ratios_undesirable: log(pi_theta/pi_ref) for bad responses   (B_u,)
        kl_term:  scalar KL(pi_theta || pi_ref) estimated from random batch
        beta:     temperature controlling deviation from reference policy
    """
    # Desirable loss: maximize log-ratio relative to KL baseline
    z_desirable = log_ratios_desirable - kl_term
    loss_desirable = 1.0 - F.sigmoid(beta * z_desirable)

    # Undesirable loss: push log-ratio below zero relative to KL baseline
    z_undesirable = log_ratios_undesirable - kl_term
    loss_undesirable = 1.0 - F.sigmoid(-beta * z_undesirable)

    loss = loss_desirable.mean() + loss_undesirable.mean()
    return loss, loss_desirable.mean().item(), loss_undesirable.mean().item()

torch.manual_seed(42)
log_ratios_good = torch.randn(16) * 0.5 + 0.3   # good responses above reference
log_ratios_bad  = torch.randn(16) * 0.5 - 0.3   # bad responses below reference
kl_baseline     = torch.tensor(0.05)              # small KL at start of training
loss, l_good, l_bad = kto_loss(log_ratios_good, log_ratios_bad, kl_baseline)
print(f'Total KTO loss:   {loss.item():.4f}')
print(f'Desirable loss:   {l_good:.4f}')
print(f'Undesirable loss: {l_bad:.4f}')
```

## Unpaired Preference Dataset Construction

KTO datasets consist of (prompt, response, label) triples where label is a boolean: True for desirable, False for undesirable. There is no requirement that desirable and undesirable responses share the same prompt — each sample is independent. In practice, researchers recommend a roughly 4:1 ratio of desirable to undesirable examples, because the undesirable gradient signal is empirically stronger per example. Collecting binary labels from production logs (thumbs up/down, star ratings collapsed to binary) is much cheaper than soliciting pairwise comparisons from annotators.

```python
import torch
from torch.utils.data import Dataset
from dataclasses import dataclass
from typing import List

@dataclass
class UnpairedSample:
    prompt: str
    response: str
    desirable: bool  # True = good (thumbs up), False = bad (thumbs down)

class KTODataset(Dataset):
    """Dataset for KTO: independent binary labels per response, no pairing needed."""
    def __init__(self, samples: List[UnpairedSample], tokenizer, max_length: int = 512):
        self.samples = samples
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        s = self.samples[idx]
        text = f'Human: {s.prompt}\nAssistant: {s.response}'
        enc  = self.tokenizer(text, max_length=self.max_length,
                              truncation=True, return_tensors='pt')
        return {
            'input_ids':      enc['input_ids'].squeeze(0),
            'attention_mask': enc['attention_mask'].squeeze(0),
            'desirable':      torch.tensor(float(s.desirable)),
        }

# Simulate dataset collected from production thumbs-up/down logs
samples = [
    UnpairedSample('What is gradient descent?', 'It minimizes loss iteratively.', True),
    UnpairedSample('Write malware', 'Here is some malware code...', False),
    UnpairedSample('Summarize RL', 'RL trains agents via reward signals.', True),
    UnpairedSample('Explain KV cache', 'It is just memory I think...', False),
    UnpairedSample('Translate to French', 'Bonjour, comment allez-vous?', True),
]
n_good = sum(1 for s in samples if s.desirable)
print(f'KTO dataset: {len(samples)} samples')
print(f'  Desirable: {n_good},  Undesirable: {len(samples) - n_good}')
print(f'  Target ratio ~4:1 desirable:undesirable for best results')
```

## KL Baseline Computation

The KL(π_θ ‖ π_ref) term is estimated empirically from a batch of random prompt-response pairs drawn from neither the desirable nor undesirable training set — these are responses generated by the policy on random held-out prompts. This running estimate acts as a baseline: it measures how much the policy has drifted from the reference overall, independent of response quality. A well-calibrated KL baseline prevents the loss from rewarding policy drift that happens to correlate with desirability but is not caused by it. In practice the estimate is computed per gradient step and optionally smoothed with an exponential moving average.

```python
import torch
import torch.nn.functional as F

def compute_kl_baseline(policy_logits_batch, ref_logits_batch):
    """
    Estimate KL(pi_theta || pi_ref) from a batch of random responses.
    Args:
        policy_logits_batch: (B, T, V) logits from current policy model
        ref_logits_batch:    (B, T, V) logits from frozen reference model
    Returns:
        kl: scalar KL estimate averaged over batch and sequence length
    """
    log_policy = F.log_softmax(policy_logits_batch, dim=-1)  # (B, T, V)
    log_ref    = F.log_softmax(ref_logits_batch,    dim=-1)  # (B, T, V)
    # KL divergence per token: sum over vocabulary
    kl_per_token = (log_policy.exp() * (log_policy - log_ref)).sum(dim=-1)  # (B, T)
    return kl_per_token.mean()  # scalar

torch.manual_seed(0)
B, T, V = 8, 20, 32000
policy_logits = torch.randn(B, T, V)
ref_logits    = torch.randn(B, T, V)
kl = compute_kl_baseline(policy_logits, ref_logits)
print(f'KL baseline estimate: {kl.item():.4f}')
print(f'Early training: KL is large (policy far from reference)')
print(f'Healthy training: KL < 0.1 indicates mild regularized drift')
```

## KTO vs DPO Data Requirements

DPO requires a pairwise dataset: for each prompt x, you need both a winning response y_w and a losing response y_l, requiring annotators to compare two responses side-by-side — a cognitively expensive task. KTO only requires binary labels on individual responses, which can come from existing product feedback. While KTO may need roughly twice the total examples to match DPO at equal quality, the per-label cost is far lower, making KTO's effective annotation budget substantially smaller for real-world deployment.

```python
def compare_annotation_costs(n_prompts: int = 10_000):
    """Compare DPO vs KTO annotation cost for equivalent training coverage."""
    # DPO: needs 2 responses per prompt + 1 pairwise comparison
    dpo_responses   = n_prompts * 2     # 2 responses per prompt
    dpo_comparisons = n_prompts          # 1 side-by-side judgment per prompt
    dpo_cost_unit   = 3.0               # pairwise judgment is cognitively harder
    dpo_total_cost  = dpo_comparisons * dpo_cost_unit

    # KTO: needs ~2x examples for comparable quality, but unpaired binary labels
    kto_samples    = n_prompts * 2      # same total responses as DPO
    kto_cost_unit  = 0.5               # binary label is easy (thumbs up/down)
    kto_total_cost = kto_samples * kto_cost_unit

    print(f'Annotation cost comparison for {n_prompts:,} prompts:')
    print(f'  DPO: {dpo_responses:,} responses, '
          f'{dpo_comparisons:,} pairwise labels, cost = {dpo_total_cost:,.0f}')
    print(f'  KTO: {kto_samples:,} responses,   '
          f'{kto_samples:,} binary labels,   cost = {kto_total_cost:,.0f}')
    ratio = kto_total_cost / dpo_total_cost
    print(f'  KTO is {1/ratio:.1f}x cheaper per equivalent training budget')
    print(f'  KTO advantage: binary labels available from existing logs')

compare_annotation_costs()
```

## Alignment Methods Data Requirements

| Method | Data Format | Paired Needed | Labels per Example | Relative Cost | Notes |
| --- | --- | --- | --- | --- | --- |
| PPO | Prompt + scalar reward per response | No | 1 scalar reward per response | Very High | Online human labelers required |
| DPO | (x, y_win, y_lose) triples | Yes — strict pairing | 1 pairwise comparison per prompt | High | Annotators compare 2 responses side-by-side |
| IPO | (x, y_win, y_lose) triples | Yes — strict pairing | 1 pairwise comparison per prompt | High | Regularised variant of DPO |
| KTO | (x, y, label) triples | No — fully unpaired | 1 binary label per response | Low | Thumbs up/down from production logs |
| ORPO | (x, y_win, y_lose) triples | Yes — strict pairing | 1 pairwise comparison per prompt | High | No separate reference model needed |
| SimPO | (x, y_win, y_lose) triples | Yes — strict pairing | 1 pairwise comparison per prompt | High | Length-normalised reward, no reference model |

## Practical Training Tips

When training with KTO, several practical considerations improve results. Set β in the range 0.05–0.3; smaller β allows more deviation from the reference policy and is useful when the base model is weak. The 4:1 desirable-to-undesirable ratio is a strong empirical prior — equal splits often underperform because undesirable samples generate stronger gradient signal. Unlike DPO, KTO can mix response sources (model-generated, human-written, log-collected) since there is no pairing constraint. Monitor the KL term during training: if it grows above 0.2–0.3, the policy is drifting too far and β should be increased.

> **KTO for Production Logs**: KTO is uniquely suited to production logging scenarios where users give thumbs up/down on individual responses — this unpaired feedback signal is much cheaper to collect than explicit pairwise comparisons required by DPO. Simply logging user thumbs-up/thumbs-down over weeks of production traffic can yield hundreds of thousands of KTO training examples at near-zero annotation cost.

- KTO does NOT require matched pairs — desirable and undesirable responses can come from entirely different prompts.
- The KL term acts as a running baseline, normalising the reward signal independently of response quality.
- Loss aversion asymmetry: undesirable responses exert stronger gradient signal than desirable ones per example.
- KTO is competitive with DPO on AlpacaEval despite requiring no pairwise annotations.
- Target a 4:1 desirable:undesirable ratio; equal splits often underperform due to asymmetric loss weighting.
- Use β ∈ [0.05, 0.3]: smaller for weaker base models, larger to stay closer to the reference policy.

---

