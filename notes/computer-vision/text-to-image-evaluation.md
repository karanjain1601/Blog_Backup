---
title: "Evaluating Text-to-Image Models: FID, CLIP Score, and Human Eval"
slug: "text-to-image-evaluation"
description: "A practical guide to the metrics that matter for T2I models — what each measures, its failure modes, and how to combine them for reliable benchmarking."
tags: ["evaluation", "FID", "CLIP-score", "text-to-image", "metrics"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFdmFsdWF0aW5nIHRleHQtdG8taW1hZ2UgKFQySSkgbW9kZWxzIGlzIHVuaXF1ZWx5IGRpZmZpY3VsdDogb3V0cHV0cyBtdXN0IHNpbXVsdGFuZW91c2x5IHNhdGlzZnkgZGlzdHJpYnV0aW9uYWwgcmVhbGlzbSAoZG8gaW1hZ2VzIGxvb2sgbGlrZSByZWFsIHBob3Rvcz8pIGFuZCBzZW1hbnRpYyBhbGlnbm1lbnQgKGRvZXMgdGhlIGltYWdlIG1hdGNoIHRoZSBwcm9tcHQ/KS4gTm8gc2luZ2xlIG1ldHJpYyBjYXB0dXJlcyBib3RoLCBzbyBjb21wcmVoZW5zaXZlIGV2YWx1YXRpb24gcmVxdWlyZXMgYSBzdWl0ZSBvZiBjb21wbGVtZW50YXJ5IG1lYXN1cmVzIHVzZWQgdG9nZXRoZXIuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZmllbGQgaGFzIGV2b2x2ZWQgdGhyb3VnaCB0aHJlZSBnZW5lcmF0aW9uczogZGlzdHJpYnV0aW9uLWJhc2VkIG1ldHJpY3MgKEZJRCwgSVMpLCBlbWJlZGRpbmcgYWxpZ25tZW50IChDTElQIFNjb3JlKSwgYW5kIGxlYXJuZWQgcHJlZmVyZW5jZSBtb2RlbHMgKFBpY2tTY29yZSwgSFBTdjIsIEltYWdlUmV3YXJkKS4gSHVtYW4gZXZhbHVhdGlvbiByZW1haW5zIHRoZSBnb2xkIHN0YW5kYXJkIGJ1dCBpcyBleHBlbnNpdmUgYW5kIGhhcmQgdG8gcmVwcm9kdWNlIOKAlCBtb2Rlcm4gYmVuY2htYXJrcyBjb21iaW5lIGF1dG9tYXRlZCBtZXRyaWNzIHdpdGggc3RydWN0dXJlZCBodW1hbiBwcmVmZXJlbmNlIHN0dWRpZXMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwiY29udGVudCI6IkZJRCBtZWFzdXJlcyBkaXN0cmlidXRpb25hbCBzaW1pbGFyaXR5IHVzaW5nIEluY2VwdGlvbi12MyBmZWF0dXJlcyB0dW5lZCBvbiBJbWFnZU5ldCDigJQgaXQgY2FuIHJhdGUgcGhvdG9yZWFsaXN0aWMgYnV0IHNlbWFudGljYWxseSB3cm9uZyBpbWFnZXMgaGlnaGx5LiBBbHdheXMgcGFpciBGSUQgd2l0aCBhIHRleHQtYWxpZ25tZW50IG1ldHJpYyAoQ0xJUCBzY29yZSkgZm9yIFQySSBldmFsdWF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZJRCBhbmQgSW5jZXB0aW9uIFNjb3JlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGcmVjaGV0IEluY2VwdGlvbiBEaXN0YW5jZSAoRklEKSBjb21wYXJlcyByZWFsIGFuZCBnZW5lcmF0ZWQgaW1hZ2UgZGlzdHJpYnV0aW9ucyBpbiBJbmNlcHRpb24tdjMgZmVhdHVyZSBzcGFjZSwgY29tcHV0aW5nIHRoZSBGcmVjaGV0IGRpc3RhbmNlIGJldHdlZW4gdHdvIG11bHRpdmFyaWF0ZSBHYXVzc2lhbnMgZml0IHRvIGVhY2ggc2V0LiBMb3dlciBpcyBiZXR0ZXIuIEZJRCByZXF1aXJlcyBhdCBsZWFzdCAxMEsgc2FtcGxlcyBmb3Igc3RhYmxlIGVzdGltYXRlcyDigJQgdXNpbmcgZmV3ZXIgc2FtcGxlcyBpbnRyb2R1Y2VzIGhpZ2ggdmFyaWFuY2UgdGhhdCBjYW4gb2JzY3VyZSByZWFsIGRpZmZlcmVuY2VzIGJldHdlZW4gbW9kZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIEZJRCB3aXRoIHRvcmNobWV0cmljc1xuZnJvbSB0b3JjaG1ldHJpY3MuaW1hZ2UuZmlkIGltcG9ydCBGcmVjaGV0SW5jZXB0aW9uRGlzdGFuY2VcbmltcG9ydCB0b3JjaFxuXG5maWQgPSBGcmVjaGV0SW5jZXB0aW9uRGlzdGFuY2UoZmVhdHVyZT0yMDQ4KS50byhcdTAwMjdjdWRhXHUwMDI3KVxuXG4jIEltYWdlcyBtdXN0IGJlIHVpbnQ4LCByYW5nZSAwLTI1NVxuZmlkLnVwZGF0ZShyZWFsX2ltZ3MudG8oXHUwMDI3Y3VkYVx1MDAyNyksICByZWFsPVRydWUpXG5maWQudXBkYXRlKGZha2VfaW1ncy50byhcdTAwMjdjdWRhXHUwMDI3KSwgIHJlYWw9RmFsc2UpXG5cbnNjb3JlID0gZmlkLmNvbXB1dGUoKVxucHJpbnQoZlwiRklEOiB7c2NvcmU6LjJmfVwiKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRklEIGlzIHNlbnNpdGl2ZSB0byBwcmVwcm9jZXNzaW5nOiBpbWFnZSByZXNpemluZyBtZXRob2QgKGJpY3ViaWMgdnMuIGJpbGluZWFyKSwgY2VudGVyIGNyb3AgdnMuIHJlc2l6ZSwgYW5kIGNvbG9yIG5vcm1hbGl6YXRpb24gYWxsIGFmZmVjdCBzY29yZXMgYnkgc2V2ZXJhbCBwb2ludHMuIEFsd2F5cyByZXBvcnQgdGhlIGV4YWN0IHByZXByb2Nlc3NpbmcgcGlwZWxpbmUuIEluY2VwdGlvbiBTY29yZSAoSVMpIG1lYXN1cmVzIHF1YWxpdHkgYW5kIGRpdmVyc2l0eSBqb2ludGx5IGJ1dCBpcyBibGluZCB0byBwcm9tcHQgYWxpZ25tZW50IOKAlCBhdm9pZCB1c2luZyBJUyBhcyBhIHByaW1hcnkgbWV0cmljIGZvciBUMkkgZXZhbHVhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDTElQIFNjb3JlIGFuZCBBbGlnbm1lbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNMSVAgU2NvcmUgbWVhc3VyZXMgc2VtYW50aWMgYWxpZ25tZW50IGJldHdlZW4gZ2VuZXJhdGVkIGltYWdlcyBhbmQgdGhlaXIgcHJvbXB0cyBieSBjb21wdXRpbmcgY29zaW5lIHNpbWlsYXJpdHkgYmV0d2VlbiBDTElQIGltYWdlIGFuZCB0ZXh0IGVtYmVkZGluZ3MuIFVubGlrZSBGSUQsIGl0IHJlcXVpcmVzIG5vIHJlZmVyZW5jZSBkYXRhc2V0IOKAlCBqdXN0IHRoZSBnZW5lcmF0ZWQgaW1hZ2UgYW5kIHByb21wdC4gSGlnaGVyIGlzIGJldHRlcjsgdHlwaWNhbCB2YWx1ZXMgcmFuZ2UgZnJvbSAwLjIwLTAuMzUgZGVwZW5kaW5nIG9uIHRoZSBDTElQIG1vZGVsIHZhcmlhbnQgYW5kIGltYWdlIGRvbWFpbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBDTElQIFNjb3JlIGZvciB0ZXh0LWltYWdlIGFsaWdubWVudFxuaW1wb3J0IGNsaXAsIHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRldmljZSA9IFx1MDAyN2N1ZGFcdTAwMjdcbm1vZGVsLCBwcmVwcm9jZXNzID0gY2xpcC5sb2FkKFwiVmlULUIvMzJcIiwgZGV2aWNlPWRldmljZSlcblxuZGVmIGNsaXBfc2NvcmUoaW1nX3BpbCwgcHJvbXB0X3N0cik6XG4gICAgaW1nID0gcHJlcHJvY2VzcyhpbWdfcGlsKS51bnNxdWVlemUoMCkudG8oZGV2aWNlKVxuICAgIHRvayA9IGNsaXAudG9rZW5pemUoW3Byb21wdF9zdHJdKS50byhkZXZpY2UpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGkgPSBtb2RlbC5lbmNvZGVfaW1hZ2UoaW1nKVxuICAgICAgICB0ID0gbW9kZWwuZW5jb2RlX3RleHQodG9rKVxuICAgIHJldHVybiBGLmNvc2luZV9zaW1pbGFyaXR5KGksIHQpLml0ZW0oKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ0xJUCBTY29yZSBoYXMga25vd24gZmFpbHVyZSBtb2RlczogaXQgdXNlcyBhIGZpeGVkIHZvY2FidWxhcnksIHN0cnVnZ2xlcyB3aXRoIHNwYXRpYWwgcmVsYXRpb25zaGlwcyAobGVmdC9yaWdodCwgYWJvdmUvYmVsb3cpLCBjb3VudHMgcG9vcmx5LCBhbmQgbWlzc2VzIGZpbmUtZ3JhaW5lZCBhdHRyaWJ1dGVzLiBWUUEtYmFzZWQgYWxpZ25tZW50IG1ldHJpY3MgKEJMSVAtVlFBLCBMTGFWQS1zY29yZSkgb2ZmZXIgY29tcGxlbWVudGFyeSBzaWduYWwgYnkgYW5zd2VyaW5nIHN0cnVjdHVyZWQgeWVzL25vIHF1ZXN0aW9ucyBkZXJpdmVkIGZyb20gdGhlIHByb21wdCBhYm91dCB0aGUgZ2VuZXJhdGVkIGltYWdlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikh1bWFuIFByZWZlcmVuY2UgU3R1ZGllcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSHVtYW4gZXZhbHVhdGlvbiB2aWEgcGFpcndpc2UgY29tcGFyaXNvbnMgKEEgdnMuIEIgZ2l2ZW4gcHJvbXB0KSBpcyB0aGUgbW9zdCByZWxpYWJsZSBtZXRob2QuIEFubm90YXRvcnMganVkZ2UgcXVhbGl0eSwgcHJvbXB0IGFkaGVyZW5jZSwgYW5kIG92ZXJhbGwgcHJlZmVyZW5jZS4gRUxPIHJhdGluZ3MgYWdncmVnYXRlIHBhaXJ3aXNlIHdpbnMgaW50byBhIGdsb2JhbCByYW5raW5nLiBBcnRpZmljaWFsIGludGVsbGlnZW5jZSBmZWVkYmFjayAoQUlGKSBmcm9tIExMTSBqdWRnZXMgKEdQVC00ViwgTExhVkEpIGlzIG5vdyBzdGFuZGFyZCBhcyBhIHNjYWxhYmxlLCByZXByb2R1Y2libGUgcHJveHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6IiMgTExNLWFzLWp1ZGdlIHdpbnJhdGUgb3ZlciBOIHByb21wdC1pbWFnZSBwYWlyc1xuaW1wb3J0IG9wZW5haSwgYmFzZTY0XG5mcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxuZGVmIGxsbV93aW5yYXRlKGltZ19hLCBpbWdfYiwgcHJvbXB0LCBuX3BhaXJzPTUwMCk6XG4gICAgd2lucyA9IDBcbiAgICBmb3IgXyBpbiByYW5nZShuX3BhaXJzKTpcbiAgICAgICAgYTY0ID0gYmFzZTY0LmI2NGVuY29kZShQYXRoKGltZ19hKS5yZWFkX2J5dGVzKCkpLmRlY29kZSgpXG4gICAgICAgIGI2NCA9IGJhc2U2NC5iNjRlbmNvZGUoUGF0aChpbWdfYikucmVhZF9ieXRlcygpKS5kZWNvZGUoKVxuICAgICAgICByZXNwID0gb3BlbmFpLmNoYXQuY29tcGxldGlvbnMuY3JlYXRlKFxuICAgICAgICAgICAgbW9kZWw9XCJncHQtNG9cIixcbiAgICAgICAgICAgIG1lc3NhZ2VzPVt7XCJyb2xlXCI6XCJ1c2VyXCIsXCJjb250ZW50XCI6W1xuICAgICAgICAgICAgICAgIHtcInR5cGVcIjpcInRleHRcIixcInRleHRcIjpmXCJQcm9tcHQ6IHtwcm9tcHR9XFxuV2hpY2ggaW1hZ2UgYmV0dGVyIG1hdGNoZXM/IFJlcGx5IEEgb3IgQi5cIn0sXG4gICAgICAgICAgICAgICAge1widHlwZVwiOlwiaW1hZ2VfdXJsXCIsXCJpbWFnZV91cmxcIjp7XCJ1cmxcIjpmXCJkYXRhOmltYWdlL3BuZztiYXNlNjQse2E2NH1cIn19LFxuICAgICAgICAgICAgICAgIHtcInR5cGVcIjpcImltYWdlX3VybFwiLFwiaW1hZ2VfdXJsXCI6e1widXJsXCI6ZlwiZGF0YTppbWFnZS9wbmc7YmFzZTY0LHtiNjR9XCJ9fVxuICAgICAgICAgICAgXX1dKVxuICAgICAgICBpZiByZXNwLmNob2ljZXNbMF0ubWVzc2FnZS5jb250ZW50LnN0cmlwKCkudXBwZXIoKSA9PSBcdTAwMjdBXHUwMDI3OiB3aW5zICs9IDFcbiAgICByZXR1cm4gd2lucyAvIG5fcGFpcnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxlYXJuZWQgcHJlZmVyZW5jZSBtb2RlbHMgKFBpY2tTY29yZSwgSFBTdjIsIEltYWdlUmV3YXJkKSBhcmUgdHJhaW5lZCBvbiBsYXJnZSBodW1hbiBwcmVmZXJlbmNlIGRhdGFzZXRzIGFuZCBwcmVkaWN0IHByZWZlcmVuY2Ugc2NvcmVzIGRpcmVjdGx5IGZyb20gaW1hZ2UgKyBwcm9tcHQuIFRoZXkgY29ycmVsYXRlIGJldHRlciB3aXRoIGh1bWFuIGp1ZGdtZW50IHRoYW4gRklEIG9yIENMSVAgU2NvcmUgYWxvbmUsIGFuZCBhcmUgb3JkZXJzIG9mIG1hZ25pdHVkZSBjaGVhcGVyIHRoYW4gcnVubmluZyBhbm5vdGF0aW9uIHN0dWRpZXMuIFVzZSB0aGVtIGZvciBtb2RlbCBzZWxlY3Rpb24gZHVyaW5nIHRyYWluaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJlbmNobWFyayBEYXRhc2V0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRHJhd0JlbmNoICgyMDAgcHJvbXB0cyksIFBhcnRpUHJvbXB0cyAoMTYwMCBwcm9tcHRzIGFjcm9zcyAxMiBjYXRlZ29yaWVzKSwgYW5kIFQySS1Db21wQmVuY2ggZm9jdXMgb24gY29tcG9zaXRpb25hbCwgc3BhdGlhbCwgYW5kIGF0dHJpYnV0ZS1iaW5kaW5nIGNoYWxsZW5nZXMgd2hlcmUgVDJJIG1vZGVscyBzdGlsbCBzdHJ1Z2dsZS4gQ09DTyBjYXB0aW9ucyBhcmUgdGhlIHN0YW5kYXJkIGZvciBGSUQgbWVhc3VyZW1lbnQuIEdlbkFJLUJlbmNoIHRlc3RzIGNvbXBsZXggbXVsdGktY29uY2VwdCBwcm9tcHRzIHdpdGggY291bnRpbmcsIG5lZ2F0aW9uLCBhbmQgYXR0cmlidXRlIGJpbmRpbmcuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldHJpYyIsIk1lYXN1cmVzIiwiTmVlZHMgUmVmZXJlbmNlPyIsIkNvbXB1dGUgQ29zdCIsIkNvcnJlbGF0aW9uIHRvIEh1bWFuIl0sInJvd3MiOltbIkZJRCIsIkRpc3RyaWJ1dGlvbmFsIHJlYWxpc20iLCJZZXMgKHJlYWwgaW1hZ2VzKSIsIkhpZ2ggKDUwSyBzYW1wbGVzKSIsIk1vZGVyYXRlIl0sWyJJUyIsIlF1YWxpdHkgKyBkaXZlcnNpdHkiLCJObyIsIk1lZGl1bSIsIkxvdyJdLFsiQ0xJUCBTY29yZSIsIlRleHQtaW1hZ2UgYWxpZ25tZW50IiwiTm8iLCJMb3ciLCJNb2RlcmF0ZSJdLFsiRElOTyBGRCIsIlJlYWxpc20gKFZpVCBmZWF0dXJlcykiLCJZZXMgKHJlYWwgaW1hZ2VzKSIsIkhpZ2giLCJIaWdoZXIgdGhhbiBGSUQiXSxbIlBpY2tTY29yZSIsIkh1bWFuIHByZWZlcmVuY2UiLCJObyIsIkxvdyAoaW5mZXJlbmNlIG9ubHkpIiwiSGlnaCJdLFsiSHVtYW4gRUxPIiwiVHJ1ZSBwcmVmZXJlbmNlIiwiTm8iLCJWZXJ5IGhpZ2ggKGFubm90YXRvcnMpIiwiR3JvdW5kIHRydXRoIl1dfSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiIyBESU5PLWJhc2VkIHJlYWxpc20gdmlhIE1heGltdW0gTWVhbiBEaXNjcmVwYW5jeVxuaW1wb3J0IHRvcmNoXG5mcm9tIHNrbGVhcm4ubWV0cmljcy5wYWlyd2lzZSBpbXBvcnQgcmJmX2tlcm5lbFxuXG5kZWYgY29tcHV0ZV9tbWQocmVhbF9mLCBnZW5fZiwgZ2FtbWE9MS4wKTpcbiAgICBcIlwiXCJBdm9pZHMgSW5jZXB0aW9uIGJpYXMg4oCUIHVzZSBESU5PdjIgZmVhdHVyZXMgaW5zdGVhZC5cIlwiXCJcbiAgICBYWCA9IHJiZl9rZXJuZWwocmVhbF9mLCByZWFsX2YsIGdhbW1hKVxuICAgIFlZID0gcmJmX2tlcm5lbChnZW5fZiwgIGdlbl9mLCAgZ2FtbWEpXG4gICAgWFkgPSByYmZfa2VybmVsKHJlYWxfZiwgZ2VuX2YsICBnYW1tYSlcbiAgICByZXR1cm4gWFgubWVhbigpICsgWVkubWVhbigpIC0gMiAqIFhZLm1lYW4oKVxuXG5kaW5vID0gdG9yY2guaHViLmxvYWQoXHUwMDI3ZmFjZWJvb2tyZXNlYXJjaC9kaW5vdjJcdTAwMjcsIFx1MDAyN2Rpbm92Ml92aXRiMTRcdTAwMjcpXG5yZWFsX2YgPSBleHRyYWN0X2ZlYXR1cmVzKGRpbm8sIHJlYWxfaW1hZ2VzKVxuZ2VuX2YgID0gZXh0cmFjdF9mZWF0dXJlcyhkaW5vLCBnZW5lcmF0ZWRfaW1hZ2VzKVxubW1kID0gY29tcHV0ZV9tbWQocmVhbF9mLm51bXB5KCksIGdlbl9mLm51bXB5KCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm8gc2luZ2xlIG1ldHJpYyBmdWxseSBjYXB0dXJlcyBUMkkgcXVhbGl0eS4gVGhlIHJlY29tbWVuZGVkIHN0YWNrOiBGSUQgb24gQ09DTyAocmVhbGlzbSBiYXNlbGluZSksIENMSVAgU2NvcmUgb24gYmVuY2htYXJrIHByb21wdHMgKGFsaWdubWVudCksIFBpY2tTY29yZSBvciBIUFN2MiAoaHVtYW4gcHJlZmVyZW5jZSBwcm94eSksIGFuZCBhIFZRQS1iYXNlZCBtZXRyaWMgZm9yIGNvbXBvc2l0aW9uYWwgcmVhc29uaW5nLiBSZXBvcnQgYWxsIGZvdXIgdG8gZ2l2ZSBhIGNvbXBsZXRlLCBub24tZ2FtZWFibGUgcGljdHVyZSBvZiBtb2RlbCBxdWFsaXR5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2FtcGxlIGNvdW50IG1hdHRlcnMgZW5vcm1vdXNseSBmb3IgRklEIHN0YWJpbGl0eS4gV2l0aCAxSyBzYW1wbGVzLCBGSUQgdmFyaWFuY2UgaXMgwrE1LTEwIHBvaW50czsgd2l0aCAzMEsgc2FtcGxlcyBpdCBkcm9wcyB0byDCsTAuNS4gVXNlIGF0IGxlYXN0IDEwSyBnZW5lcmF0ZWQgaW1hZ2VzIGZvciBwdWJsaXNoZWQgcmVzdWx0cy4gRm9yIENMSVAgU2NvcmUsIDVLIHByb21wdC1pbWFnZSBwYWlycyBpcyB0eXBpY2FsbHkgc3VmZmljaWVudCBmb3Igc3RhYmxlIGVzdGltYXRlcyB3aXRoIGxlc3MgdGhhbiAwLjAwMiBzdGFuZGFyZCBkZXZpYXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZmllbGQgaXMgbW92aW5nIHRvd2FyZCBMTE0tanVkZ2UgZXZhbHVhdGlvbiBmcmFtZXdvcmtzIChMTGFWQS1ldmFsLCBHUFQtNFYtZXZhbCkgdGhhdCBhc3Nlc3MgbnVhbmNlZCBhdHRyaWJ1dGVzOiBjb3VudGluZywgc3BhdGlhbCByZWxhdGlvbnMsIHRleHQgcmVuZGVyaW5nLCBhbmQgc3R5bGUgZmlkZWxpdHkuIFRoZXNlIHdpbGwgbGlrZWx5IHJlcGxhY2UgQ0xJUCBTY29yZSBhcyB0aGUgcHJpbWFyeSBhbGlnbm1lbnQgbWV0cmljIGFzIG11bHRpbW9kYWwgTExNcyBiZWNvbWUgbW9yZSBjYXBhYmxlIGFuZCBjb3N0LWVmZmVjdGl2ZSBmb3IgZXZhbHVhdGlvbiBwaXBlbGluZXMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbHdheXMgZXZhbHVhdGUgb24gcHJvbXB0cyBvdXRzaWRlIHlvdXIgdHJhaW5pbmcgZGlzdHJpYnV0aW9uLiBNb2RlbHMgdHVuZWQgb24gc3BlY2lmaWMgcHJvbXB0IHN0eWxlcyAoc2hvcnQgdnMuIGRldGFpbGVkLCBMQUlPTi1zdHlsZSB2cy4gcHJvZmVzc2lvbmFsIHBob3RvZ3JhcGh5KSBjYW4gc2hvdyBpbmZsYXRlZCBzY29yZXMgb24gaW4tZGlzdHJpYnV0aW9uIGJlbmNobWFya3MuIEFkdmVyc2FyaWFsIHByb21wdCBzZXRzIChUMkktQ29tcEJlbmNoIGhhcmQgc3BsaXQsIFdpbm9ncm91bmQpIGFyZSBiZXR0ZXIgZGlzY3JpbWluYXRvcnMgb2YgdHJ1ZSBnZW5lcmFsaXphdGlvbi4ifV0="
---
# Evaluating Text-to-Image Models: FID, CLIP Score, and Human Eval

## Overview

Evaluating text-to-image (T2I) models is uniquely difficult: outputs must simultaneously satisfy distributional realism (do images look like real photos?) and semantic alignment (does the image match the prompt?). No single metric captures both, so comprehensive evaluation requires a suite of complementary measures used together.

The field has evolved through three generations: distribution-based metrics (FID, IS), embedding alignment (CLIP Score), and learned preference models (PickScore, HPSv2, ImageReward). Human evaluation remains the gold standard but is expensive and hard to reproduce — modern benchmarks combine automated metrics with structured human preference studies.

> **warning**: FID measures distributional similarity using Inception-v3 features tuned on ImageNet — it can rate photorealistic but semantically wrong images highly. Always pair FID with a text-alignment metric (CLIP score) for T2I evaluation.

## FID and Inception Score

Frechet Inception Distance (FID) compares real and generated image distributions in Inception-v3 feature space, computing the Frechet distance between two multivariate Gaussians fit to each set. Lower is better. FID requires at least 10K samples for stable estimates — using fewer samples introduces high variance that can obscure real differences between models.

```python
# FID with torchmetrics
from torchmetrics.image.fid import FrechetInceptionDistance
import torch

fid = FrechetInceptionDistance(feature=2048).to('cuda')

# Images must be uint8, range 0-255
fid.update(real_imgs.to('cuda'),  real=True)
fid.update(fake_imgs.to('cuda'),  real=False)

score = fid.compute()
print(f"FID: {score:.2f}")
```

FID is sensitive to preprocessing: image resizing method (bicubic vs. bilinear), center crop vs. resize, and color normalization all affect scores by several points. Always report the exact preprocessing pipeline. Inception Score (IS) measures quality and diversity jointly but is blind to prompt alignment — avoid using IS as a primary metric for T2I evaluation.

## CLIP Score and Alignment

CLIP Score measures semantic alignment between generated images and their prompts by computing cosine similarity between CLIP image and text embeddings. Unlike FID, it requires no reference dataset — just the generated image and prompt. Higher is better; typical values range from 0.20-0.35 depending on the CLIP model variant and image domain.

```python
# CLIP Score for text-image alignment
import clip, torch
import torch.nn.functional as F

device = 'cuda'
model, preprocess = clip.load("ViT-B/32", device=device)

def clip_score(img_pil, prompt_str):
    img = preprocess(img_pil).unsqueeze(0).to(device)
    tok = clip.tokenize([prompt_str]).to(device)
    with torch.no_grad():
        i = model.encode_image(img)
        t = model.encode_text(tok)
    return F.cosine_similarity(i, t).item()
```

CLIP Score has known failure modes: it uses a fixed vocabulary, struggles with spatial relationships (left/right, above/below), counts poorly, and misses fine-grained attributes. VQA-based alignment metrics (BLIP-VQA, LLaVA-score) offer complementary signal by answering structured yes/no questions derived from the prompt about the generated image.

## Human Preference Studies

Human evaluation via pairwise comparisons (A vs. B given prompt) is the most reliable method. Annotators judge quality, prompt adherence, and overall preference. ELO ratings aggregate pairwise wins into a global ranking. Artificial intelligence feedback (AIF) from LLM judges (GPT-4V, LLaVA) is now standard as a scalable, reproducible proxy.

```python
# LLM-as-judge winrate over N prompt-image pairs
import openai, base64
from pathlib import Path

def llm_winrate(img_a, img_b, prompt, n_pairs=500):
    wins = 0
    for _ in range(n_pairs):
        a64 = base64.b64encode(Path(img_a).read_bytes()).decode()
        b64 = base64.b64encode(Path(img_b).read_bytes()).decode()
        resp = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role":"user","content":[
                {"type":"text","text":f"Prompt: {prompt}\nWhich image better matches? Reply A or B."},
                {"type":"image_url","image_url":{"url":f"data:image/png;base64,{a64}"}},
                {"type":"image_url","image_url":{"url":f"data:image/png;base64,{b64}"}}
            ]}])
        if resp.choices[0].message.content.strip().upper() == 'A': wins += 1
    return wins / n_pairs
```

Learned preference models (PickScore, HPSv2, ImageReward) are trained on large human preference datasets and predict preference scores directly from image + prompt. They correlate better with human judgment than FID or CLIP Score alone, and are orders of magnitude cheaper than running annotation studies. Use them for model selection during training.

## Benchmark Datasets

DrawBench (200 prompts), PartiPrompts (1600 prompts across 12 categories), and T2I-CompBench focus on compositional, spatial, and attribute-binding challenges where T2I models still struggle. COCO captions are the standard for FID measurement. GenAI-Bench tests complex multi-concept prompts with counting, negation, and attribute binding.

| Metric | Measures | Needs Reference? | Compute Cost | Correlation to Human |
| --- | --- | --- | --- | --- |
| FID | Distributional realism | Yes (real images) | High (50K samples) | Moderate |
| IS | Quality + diversity | No | Medium | Low |
| CLIP Score | Text-image alignment | No | Low | Moderate |
| DINO FD | Realism (ViT features) | Yes (real images) | High | Higher than FID |
| PickScore | Human preference | No | Low (inference only) | High |
| Human ELO | True preference | No | Very high (annotators) | Ground truth |

```python
# DINO-based realism via Maximum Mean Discrepancy
import torch
from sklearn.metrics.pairwise import rbf_kernel

def compute_mmd(real_f, gen_f, gamma=1.0):
    """Avoids Inception bias — use DINOv2 features instead."""
    XX = rbf_kernel(real_f, real_f, gamma)
    YY = rbf_kernel(gen_f,  gen_f,  gamma)
    XY = rbf_kernel(real_f, gen_f,  gamma)
    return XX.mean() + YY.mean() - 2 * XY.mean()

dino = torch.hub.load('facebookresearch/dinov2', 'dinov2_vitb14')
real_f = extract_features(dino, real_images)
gen_f  = extract_features(dino, generated_images)
mmd = compute_mmd(real_f.numpy(), gen_f.numpy())
```

## Key Takeaways

No single metric fully captures T2I quality. The recommended stack: FID on COCO (realism baseline), CLIP Score on benchmark prompts (alignment), PickScore or HPSv2 (human preference proxy), and a VQA-based metric for compositional reasoning. Report all four to give a complete, non-gameable picture of model quality.

Sample count matters enormously for FID stability. With 1K samples, FID variance is ±5-10 points; with 30K samples it drops to ±0.5. Use at least 10K generated images for published results. For CLIP Score, 5K prompt-image pairs is typically sufficient for stable estimates with less than 0.002 standard deviation.

The field is moving toward LLM-judge evaluation frameworks (LLaVA-eval, GPT-4V-eval) that assess nuanced attributes: counting, spatial relations, text rendering, and style fidelity. These will likely replace CLIP Score as the primary alignment metric as multimodal LLMs become more capable and cost-effective for evaluation pipelines.

Always evaluate on prompts outside your training distribution. Models tuned on specific prompt styles (short vs. detailed, LAION-style vs. professional photography) can show inflated scores on in-distribution benchmarks. Adversarial prompt sets (T2I-CompBench hard split, Winoground) are better discriminators of true generalization.

