---
title: "PEFT Selection Guide — Choosing the Right Method by Task, Data, and Constraints"
slug: "peft-selection-guide"
description: "Decision framework for choosing the right PEFT method. Covers key selection dimensions, a Python decision function, parameter efficiency vs quality benchmarks, inference latency comparison, multi-task adapter serving, and a comprehensive method comparison table for LoRA, QLoRA, DoRA, LoRA+, VeRA, Prefix Tuning, Adapters, and IA3."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aCBhIGdyb3dpbmcgem9vIG9mIFBFRlQgbWV0aG9kcyDigJQgTG9SQSwgUUxvUkEsIERvUkEsIExvUkErLCBWZVJBLCBQcmVmaXggVHVuaW5nLCBBZGFwdGVycywgSUEzIOKAlCBjaG9vc2luZyB0aGUgcmlnaHQgb25lIHJlcXVpcmVzIHJlYXNvbmluZyBhYm91dCBmaXZlIGRpbWVuc2lvbnMgc2ltdWx0YW5lb3VzbHk6IGRhdGEgc2l6ZSwgdGFzayB0eXBlLCBHUFUgbWVtb3J5IGJ1ZGdldCwgaW5mZXJlbmNlIGxhdGVuY3kgcmVxdWlyZW1lbnQsIGFuZCB3aGV0aGVyIHlvdSBuZWVkIHRvIG1lcmdlIG9yIHN3YXAgYWRhcHRlcnMgYXQgcnVudGltZS4gTm8gc2luZ2xlIG1ldGhvZCBkb21pbmF0ZXMgYWxsIGRpbWVuc2lvbnM7IHRoZSByaWdodCBjaG9pY2UgZGVwZW5kcyBvbiB3aGljaCBjb25zdHJhaW50cyBhcmUgYmluZGluZyBpbiB5b3VyIHNldHRpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IERlY2lzaW9uIERpbWVuc2lvbnMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkRhdGEgc2l6ZTogXHUwMDNjIDEwMCBleGFtcGxlcyDihpIgSUEzOyAxMDDigJMxMEsg4oaSIExvUkEgb3IgTG9SQSs7IDEwS+KAkzEwMEsg4oaSIExvUkErL0RvUkE7IFx1MDAzZSAxMDBLIOKGkiBEb1JBIG9yIGZ1bGwgZmluZS10dW5lIHdpdGggTG9SQSByZWd1bGFyaXphdGlvbi4iLCJUYXNrIHR5cGU6IHVuZGVyc3RhbmRpbmcgKGNsYXNzaWZpY2F0aW9uLCBORVIpIOKGkiBMb1JBIHJhbmsgNOKAkzE2OyBnZW5lcmF0aW9uIOKGkiBMb1JBIHJhbmsgMTbigJM2NDsgYWxpZ25tZW50IChSTEhGL0RQTykg4oaSIExvUkEgKyBEUE8gaXMgc3RhbmRhcmQuIiwiR1BVIG1lbW9yeTogXHUwMDNjIDE2IEdCIOKGkiBRTG9SQSAoNC1iaXQgYmFzZSk7IDE24oCTNDAgR0Ig4oaSIExvUkEgb3IgRG9SQSBpbiBiZjE2OyBcdTAwM2UgNDAgR0Ig4oaSIERvUkEgZnVsbCBwcmVjaXNpb24uIiwiSW5mZXJlbmNlIGxhdGVuY3k6IHplcm8gb3ZlcmhlYWQgcmVxdWlyZWQg4oaSIG1lcmdlIExvUkEgaW50byBiYXNlIHdlaWdodHM7IGNhbiB0b2xlcmF0ZSBleHRyYSBsYXllcnMg4oaSIEFkYXB0ZXJzIG9yIFByZWZpeCBUdW5pbmc7IGV4dHJlbWUgZmV3LXNob3Qg4oaSIElBMyAoMyByZXNjYWxpbmcgdmVjdG9ycyBwZXIgbGF5ZXIpLiIsIk11bHRpLXRhc2sgc2VydmluZzogaG90LXN3YXAgd2l0aG91dCByZWxvYWRpbmcg4oaSIEFkYXB0ZXJzIG9yIG5vbi1tZXJnZWQgTG9SQTsgc2luZ2xlIHRhc2sgYXQgYSB0aW1lIOKGkiBtZXJnZSBMb1JBIGZvciB6ZXJvIGxhdGVuY3kuIiwiTWVyZ2luZyAvIHRhc2sgYXJpdGhtZXRpYzogb25seSBMb1JBIGFuZCBEb1JBIHByb2R1Y2UgbWVyZ2VhYmxlIGRlbHRhIG1hdHJpY2VzOyBBZGFwdGVycyBhbmQgUHJlZml4IFR1bmluZyBjYW5ub3QgYmUgbWVyZ2VkIGludG8gYmFzZSB3ZWlnaHRzIGNsZWFubHkuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBFRlQgU2VsZWN0aW9uIERlY2lzaW9uIFRyZWUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc3lzdGVtYXRpYyBkZWNpc2lvbiBmdW5jdGlvbiByZW1vdmVzIHRoZSBndWVzc3dvcmsuIFRoZSB0cmVlIGJlbG93IGNoZWNrcyBiaW5kaW5nIGNvbnN0cmFpbnRzIGluIHByaW9yaXR5IG9yZGVyOiBtZW1vcnkgZmlyc3QgKFFMb1JBKSwgdGhlbiBleHRyZW1lIGZldy1zaG90IChJQTMpLCB0aGVuIG11bHRpLXRhc2sgaW5mZXJlbmNlIChBZGFwdGVycyksIHRoZW4gcXVhbGl0eSBwcmlvcml0eSAoRG9SQSksIGFuZCBkZWZhdWx0cyB0byBMb1JBKyBmb3IgdGhlIGdlbmVyYWwgY2FzZS4gTG9SQSsgaXMgYSBmcmVlIGltcHJvdmVtZW50IG92ZXIgc3RhbmRhcmQgTG9SQSDigJQgaXQgc2V0cyBkaWZmZXJlbnQgbGVhcm5pbmcgcmF0ZXMgZm9yIHRoZSBBIGFuZCBCIG1hdHJpY2VzIOKAlCBhbmQgc2hvdWxkIGFsd2F5cyBiZSBwcmVmZXJyZWQgb3ZlciB2YW5pbGxhIExvUkEgd2hlbiB0aGVyZSBpcyBubyBvdGhlciBjb25zdHJhaW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcbmZyb20gdHlwaW5nIGltcG9ydCBPcHRpb25hbFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBQRUZUUmVjb21tZW5kYXRpb246XG4gICAgbWV0aG9kOiBzdHJcbiAgICByZWFzb246IHN0clxuICAgIGxvcmFfcmFuazogT3B0aW9uYWxbaW50XSA9IE5vbmVcbiAgICBub3Rlczogc3RyID0gXCJcIlxuXG5kZWYgc2VsZWN0X3BlZnRfbWV0aG9kKFxuICAgIGRhdGFfc2l6ZTogaW50LFxuICAgIGdwdV9tZW1vcnlfZ2I6IGZsb2F0LFxuICAgIHRhc2tfdHlwZTogc3RyID0gXCJnZW5lcmF0aW9uXCIsXG4gICAgbXVsdGlfdGFza19pbmZlcmVuY2U6IGJvb2wgPSBGYWxzZSxcbiAgICBuZWVkX21lcmdlOiBib29sID0gRmFsc2UsXG4gICAgcXVhbGl0eV9wcmlvcml0eTogYm9vbCA9IEZhbHNlLFxuKSAtXHUwMDNlIFBFRlRSZWNvbW1lbmRhdGlvbjpcbiAgICBcIlwiXCJSZXR1cm4gdGhlIHJlY29tbWVuZGVkIFBFRlQgbWV0aG9kIGdpdmVuIHRhc2sgY29uc3RyYWludHMuXCJcIlwiXG4gICAgaWYgZGF0YV9zaXplIFx1MDAzYyAxMDA6XG4gICAgICAgIHJldHVybiBQRUZUUmVjb21tZW5kYXRpb24oXCJJQTNcIiwgXCJFeHRyZW1lIGZldy1zaG90OiBJQTMgaGFzIGZld2VzdCB0cmFpbmFibGUgcGFyYW1zXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbm90ZXM9XCJPbmx5IH4zIHZlY3RvcnMgcGVyIGxheWVyOyBubyByYW5rIHRvIHR1bmVcIilcbiAgICBpZiBncHVfbWVtb3J5X2diIFx1MDAzYyAxNjpcbiAgICAgICAgcmV0dXJuIFBFRlRSZWNvbW1lbmRhdGlvbihcIlFMb1JBXCIsIFwiTWVtb3J5IGNvbnN0cmFpbmVkOiA0LWJpdCBiYXNlICsgYmYxNiBhZGFwdGVyc1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxvcmFfcmFuaz0xNiwgbm90ZXM9XCJVc2UgYml0c2FuZGJ5dGVzIE5GNCArIHBhZ2VkIG9wdGltaXplclwiKVxuICAgIGlmIG11bHRpX3Rhc2tfaW5mZXJlbmNlIGFuZCBub3QgbmVlZF9tZXJnZTpcbiAgICAgICAgcmV0dXJuIFBFRlRSZWNvbW1lbmRhdGlvbihcIkFkYXB0ZXJzXCIsIFwiSG90LXN3YXAgYXQgaW5mZXJlbmNlIHdpdGhvdXQgcmVsb2FkaW5nIGJhc2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBub3Rlcz1cIlVzZSBQRUZUIEFkYXB0ZXJIdWI7IHN3YXAgYnkgdGFza19pZFwiKVxuICAgIGlmIG5lZWRfbWVyZ2UgYW5kIHF1YWxpdHlfcHJpb3JpdHk6XG4gICAgICAgIHJldHVybiBQRUZUUmVjb21tZW5kYXRpb24oXCJMb1JBKyArIERvUkFcIiwgXCJCZXN0IHF1YWxpdHksIG1lcmdlcyB0byB6ZXJvIGxhdGVuY3lcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsb3JhX3Jhbms9MzIsIG5vdGVzPVwiRG9SQTogc2VwYXJhdGUgbWFnbml0dWRlL2RpcmVjdGlvbiBsZWFybmluZ1wiKVxuICAgIGlmIG5lZWRfbWVyZ2U6XG4gICAgICAgIHJldHVybiBQRUZUUmVjb21tZW5kYXRpb24oXCJMb1JBK1wiLCBcIk1lcmdlYWJsZSwgZnJlZSBMUiBpbXByb3ZlbWVudCBvdmVyIExvUkFcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsb3JhX3Jhbms9MTYsIG5vdGVzPVwiU2V0IGxyX3JhdGlvPTE2IGZvciBCIG1hdHJpeFwiKVxuICAgIHJldHVybiBQRUZUUmVjb21tZW5kYXRpb24oXCJMb1JBK1wiLCBcIkJlc3QgZ2VuZXJhbC1wdXJwb3NlIGRlZmF1bHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxvcmFfcmFuaz0xNiwgbm90ZXM9XCJTdGFydCBoZXJlOyBhZGQgRG9SQSBpZiBxdWFsaXR5IGlzIGluc3VmZmljaWVudFwiKVxuXG50ZXN0X2Nhc2VzID0gW1xuICAgICg1MCwgICAyNCwgXCJjbGFzc2lmaWNhdGlvblwiLCBGYWxzZSwgRmFsc2UsIEZhbHNlKSxcbiAgICAoNTAwLCAgMTIsIFwiZ2VuZXJhdGlvblwiLCAgICAgRmFsc2UsIFRydWUsICBGYWxzZSksXG4gICAgKDUwMDAsIDI0LCBcImdlbmVyYXRpb25cIiwgICAgIEZhbHNlLCBUcnVlLCAgVHJ1ZSksXG4gICAgKDUwMDAwLDgwLCBcImFsaWdubWVudFwiLCAgICAgIEZhbHNlLCBUcnVlLCAgVHJ1ZSksXG4gICAgKDIwMDAsIDQwLCBcImdlbmVyYXRpb25cIiwgICAgIFRydWUsICBGYWxzZSwgRmFsc2UpLFxuXVxuZm9yIGFyZ3MgaW4gdGVzdF9jYXNlczpcbiAgICByID0gc2VsZWN0X3BlZnRfbWV0aG9kKCphcmdzKVxuICAgIHByaW50KGZcImRhdGE9e2FyZ3NbMF06XHUwMDNlNn0sIGdwdT17YXJnc1sxXTpcdTAwM2UyfUdCIC1cdTAwM2Uge3IubWV0aG9kfToge3IucmVhc29ufVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBhcmFtZXRlciBFZmZpY2llbmN5IHZzIFF1YWxpdHkgVHJhZGVvZmYifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBlZmZpY2llbmN5LXF1YWxpdHkgUGFyZXRvIGZyb250aWVyIHZhcmllcyBieSBtZXRob2QuIElBMyBzaXRzIGF0IHRoZSBleHRyZW1lLWVmZmljaWVuY3kgZW5kIChcdTAwM2MgMC4wMiUgdHJhaW5hYmxlIHBhcmFtZXRlcnMpIGJ1dCByZXF1aXJlcyBsYXJnZSBiYXNlIG1vZGVscyB0byBzaGluZSDigJQgb24gR1BULTMgc2NhbGUgaXQgbWF0Y2hlcyBMb1JBLCBidXQgb24gMUItc2NhbGUgbW9kZWxzIGl0IHVuZGVycGVyZm9ybXMuIExvUkEgYXQgcmFuayAxNiBpcyB0aGUgc3dlZXQgc3BvdCBmb3IgbW9zdCAx4oCTN0IgbW9kZWxzOiBlbm91Z2ggY2FwYWNpdHkgZm9yIGdlbmVyYXRpb24gdGFza3MsIG5lZ2xpZ2libGUgaW5mZXJlbmNlIG92ZXJoZWFkIHdoZW4gbWVyZ2VkLiBEb1JBIGFkZHMgfjElIG92ZXJoZWFkIG92ZXIgTG9SQSBpbiB0cmFpbmluZyB0aW1lIGJ1dCBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybXMgTG9SQSBieSAx4oCTMyUgYWJzb2x1dGUgb24gZ2VuZXJhdGlvbiBiZW5jaG1hcmtzLiBWZVJBIHVzZXMgc2hhcmVkIHJhbmRvbSBtYXRyaWNlcyB3aXRoIGxlYXJuYWJsZSByZXNjYWxpbmcgdmVjdG9ycywgYWNoaWV2aW5nIExvUkEtY29tcGFyYWJsZSBxdWFsaXR5IHdpdGggMTDDlyBmZXdlciB0cmFpbmFibGUgcGFyYW1ldGVycyBidXQgY2Fubm90IGJlIG1lcmdlZCBjbGVhbmx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3MsIGZpZWxkXG5mcm9tIHR5cGluZyBpbXBvcnQgTGlzdFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBCZW5jaG1hcmtSZXN1bHQ6XG4gICAgbWV0aG9kOiBzdHJcbiAgICB0cmFpbmFibGVfcGFyYW1zX3BjdDogZmxvYXRcbiAgICB0cmFpbl90aW1lX3JlbGF0aXZlOiBmbG9hdCAgIyByZWxhdGl2ZSB0byBMb1JBPTEuMFxuICAgIGV2YWxfc2NvcmU6IGZsb2F0ICAgICAgICAgICAjIG5vcm1hbGl6ZWQ6IExvUkE9MC44NzFcbiAgICBwZWFrX21lbW9yeV9nYjogZmxvYXRcbiAgICBtZXJnZV90b19iYXNlOiBib29sXG5cbmRlZiBydW5fcGVmdF9iZW5jaG1hcmsobW9kZWxfcGFyYW1zOiBpbnQgPSA3XzAwMF8wMDBfMDAwKSAtXHUwMDNlIExpc3RbQmVuY2htYXJrUmVzdWx0XTpcbiAgICBcIlwiXCJTaW11bGF0ZWQgYmVuY2htYXJrIHJlc3VsdHMgKGZyb20gcHVibGlzaGVkIHBhcGVycyBhbmQgaW50ZXJuYWwgZXZhbHMpLlwiXCJcIlxuICAgIHJlc3VsdHMgPSBbXG4gICAgICAgIEJlbmNobWFya1Jlc3VsdChcIkxvUkEgcj0xNlwiLCAgICAwLjA1MCwgMS4wMCwgMC44NzEsIDE0LjIsIFRydWUpLFxuICAgICAgICBCZW5jaG1hcmtSZXN1bHQoXCJMb1JBKyByPTE2XCIsICAgMC4wNTAsIDAuOTksIDAuODc2LCAxNC4yLCBUcnVlKSxcbiAgICAgICAgQmVuY2htYXJrUmVzdWx0KFwiRG9SQSByPTE2XCIsICAgIDAuMDUxLCAxLjA0LCAwLjg4MiwgMTQuNiwgVHJ1ZSksXG4gICAgICAgIEJlbmNobWFya1Jlc3VsdChcIlFMb1JBIHI9MTZcIiwgICAwLjA1MCwgMS4xOCwgMC44NjgsICA4LjEsIFRydWUpLFxuICAgICAgICBCZW5jaG1hcmtSZXN1bHQoXCJJQTNcIiwgICAgICAgICAgMC4wMDIsIDAuODAsIDAuODQxLCAxMy44LCBGYWxzZSksXG4gICAgICAgIEJlbmNobWFya1Jlc3VsdChcIkFkYXB0ZXJzXCIsICAgICAwLjEyMCwgMS4xMywgMC44NzQsIDE1LjEsIEZhbHNlKSxcbiAgICAgICAgQmVuY2htYXJrUmVzdWx0KFwiUHJlZml4VHVuaW5nXCIsIDAuMDEwLCAwLjk1LCAwLjg0MywgMTQuMCwgRmFsc2UpLFxuICAgICAgICBCZW5jaG1hcmtSZXN1bHQoXCJWZVJBIHI9MjU2XCIsICAgMC4wMDUsIDEuMDIsIDAuODY5LCAxNC4zLCBGYWxzZSksXG4gICAgXVxuICAgIHJldHVybiByZXN1bHRzXG5cbnJlc3VsdHMgPSBydW5fcGVmdF9iZW5jaG1hcmsoKVxucHJpbnQoZlwie1x1MDAyN01ldGhvZFx1MDAyNzpcdTAwM2UxNn0ge1x1MDAyN1BhcmFtcyVcdTAwMjc6XHUwMDNlOH0ge1x1MDAyN1RpbWVcdTAwMjc6XHUwMDNlNn0ge1x1MDAyN1Njb3JlXHUwMDI3Olx1MDAzZTd9IHtcdTAwMjdNZW0oR0IpXHUwMDI3Olx1MDAzZTh9IHtcdTAwMjdNZXJnZVx1MDAyNzpcdTAwM2U2fVwiKVxucHJpbnQoXCItXCIgKiA1OClcbmZvciByIGluIHJlc3VsdHM6XG4gICAgbWVyZ2Vfc3RyID0gXCJZZXNcIiBpZiByLm1lcmdlX3RvX2Jhc2UgZWxzZSBcIk5vXCJcbiAgICBwcmludChmXCJ7ci5tZXRob2Q6XHUwMDNlMTZ9IHtyLnRyYWluYWJsZV9wYXJhbXNfcGN0Olx1MDAzZTcuM2Z9JSB7ci50cmFpbl90aW1lX3JlbGF0aXZlOlx1MDAzZTYuMmZ9eCBcIlxuICAgICAgICAgIGZcIntyLmV2YWxfc2NvcmU6XHUwMDNlNy4zZn0ge3IucGVha19tZW1vcnlfZ2I6XHUwMDNlOC4xZn0ge21lcmdlX3N0cjpcdTAwM2U2fVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkluZmVyZW5jZSBPdmVyaGVhZCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbmZlcmVuY2UgbGF0ZW5jeSBpcyB3aGVyZSBtZXRob2RzIGRpdmVyZ2UgbW9zdCBzaGFycGx5LiBNZXJnZWQgTG9SQSBpcyBpZGVudGljYWwgdG8gdGhlIGJhc2UgbW9kZWwgYXQgaW5mZXJlbmNlIOKAlCB0aGUgYWRhcHRlciBtYXRyaWNlcyBhcmUgYWJzb3JiZWQgaW50byB0aGUgYmFzZSB3ZWlnaHRzLCBhZGRpbmcgemVybyBsYXRlbmN5LiBOb24tbWVyZ2VkIExvUkEgYWRkcyB0d28gZXh0cmEgbWF0bXVscyAoQXggYW5kIEJ4KSBwZXIgYWRhcHRlZCBsYXllciwgcm91Z2hseSAz4oCTOCUgb3ZlcmhlYWQgb24gR1BVIGZvciByYW5rIDE2LiBBZGFwdGVyIGxheWVycyBpbnNlcnQgYSBib3R0bGVuZWNrIE1MUCAoZG93bi1wcm9qZWN0IOKGkiBhY3RpdmF0aW9uIOKGkiB1cC1wcm9qZWN0KSBhZGRpbmcgNeKAkzE1JSBvdmVyaGVhZCBkZXBlbmRpbmcgb24gcmFuayBhbmQgbW9kZWwgc2l6ZS4gUHJlZml4IFR1bmluZyBwcmVwZW5kcyBrIHZpcnR1YWwgdG9rZW5zIHRvIHRoZSBrZXktdmFsdWUgY2FjaGUsIGluY3JlYXNpbmcgYXR0ZW50aW9uIGNvbXB1dGF0aW9uIGJ5IGsvc2VxX2xlbiDigJQgZm9yIGs9NTAgdG9rZW5zIG9uIGEgNTEyLXRva2VuIHNlcXVlbmNlLCBvdmVyaGVhZCBpcyB+MTAlLiBJQTMgcmVzY2FsZXMgYnkgbGVhcm5lZCB2ZWN0b3JzOiB0aGUgb3ZlcmhlYWQgaXMgYSBzaW5nbGUgZWxlbWVudC13aXNlIG11bHRpcGx5IHBlciBsYXllciwgXHUwMDNjIDElLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRpbWVcblxuZGVmIG1lYXN1cmVfbGF0ZW5jeShtb2RlbDogbm4uTW9kdWxlLCB4OiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgICAgIG5fd2FybXVwOiBpbnQgPSAyMCwgbl9ydW5zOiBpbnQgPSAxMDApIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiUmV0dXJuIGF2ZXJhZ2UgZm9yd2FyZC1wYXNzIGxhdGVuY3kgaW4gbWlsbGlzZWNvbmRzLlwiXCJcIlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgXyBpbiByYW5nZShuX3dhcm11cCk6XG4gICAgICAgICAgICBtb2RlbCh4KVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgXyBpbiByYW5nZShuX3J1bnMpOlxuICAgICAgICAgICAgbW9kZWwoeClcbiAgICByZXR1cm4gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MCkgKiAxMDAwIC8gbl9ydW5zXG5cbkQgPSA1MTJcbiMgTWVyZ2VkIExvUkE6IHNhbWUgYXMgYmFzZSBtb2RlbFxuYmFzZSA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKEQsIEQpLCBubi5SZUxVKCksIG5uLkxpbmVhcihELCBEKSlcbiMgTm9uLW1lcmdlZCBMb1JBOiBleHRyYSBtYXRtdWwgcGVyIGxheWVyIChzaW11bGF0ZWQgYXMgZXh0cmEgc21hbGwgbGluZWFyKVxubm9uX21lcmdlZF9sb3JhID0gbm4uU2VxdWVudGlhbChcbiAgICBubi5MaW5lYXIoRCwgRCksIG5uLlJlTFUoKSwgbm4uTGluZWFyKEQsIEQpLFxuICAgIG5uLkxpbmVhcihELCAxNiwgYmlhcz1GYWxzZSksIG5uLkxpbmVhcigxNiwgRCwgYmlhcz1GYWxzZSkgICMgTG9SQSBBK0JcbilcbiMgQWRhcHRlcjogZXh0cmEgYm90dGxlbmVjayBsYXllcnNcbmFkYXB0ZXIgPSBubi5TZXF1ZW50aWFsKFxuICAgIG5uLkxpbmVhcihELCBEKSwgbm4uUmVMVSgpLFxuICAgIG5uLkxpbmVhcihELCA2NCksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDY0LCBEKSwgICMgYWRhcHRlciBib3R0bGVuZWNrXG4gICAgbm4uTGluZWFyKEQsIEQpXG4pXG54ID0gdG9yY2gucmFuZG4oMTYsIEQpXG5mb3IgbmFtZSwgbW9kZWwgaW4gWyhcIkJhc2UvTWVyZ2VkTG9SQVwiLCBiYXNlKSwgKFwiTm9uTWVyZ2VkTG9SQVwiLCBub25fbWVyZ2VkX2xvcmEpLCAoXCJBZGFwdGVyXCIsIGFkYXB0ZXIpXTpcbiAgICBsYXQgPSBtZWFzdXJlX2xhdGVuY3kobW9kZWwsIHgpXG4gICAgcGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpXG4gICAgcHJpbnQoZlwie25hbWU6XHUwMDNlMTZ9OiB7bGF0Oi4zZn0gbXMvYmF0Y2ggICh7cGFyYW1zOix9IHBhcmFtcylcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1UYXNrIFNlcnZpbmcgd2l0aCBBZGFwdGVyIFN3YXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gc2VydmluZyBtdWx0aXBsZSB0YXNrcyBmcm9tIG9uZSBkZXBsb3ltZW50LCBub24tbWVyZ2VkIGFkYXB0ZXJzIG9mZmVyIGhvdC1zd2FwOiBsb2FkIHRoZSBiYXNlIG1vZGVsIG9uY2UgYW5kIHN3YXAgdGhlIGFkYXB0ZXIgd2VpZ2h0cyBwZXIgcmVxdWVzdCB3aXRob3V0IHJlbG9hZGluZyB0aGUgZnVsbCBtb2RlbC4gVGhpcyBpcyBlZmZpY2llbnQgd2hlbiB0YXNrcyBzaGFyZSBhIGNvbW1vbiBiYXNlIGFuZCBkaWZmZXIgb25seSBpbiB0aGUgYWRhcHRlci4gVGhlIG92ZXJoZWFkIGlzIHRoZSBhZGFwdGVyIGZvcndhcmQgcGFzcyAoNeKAkzE1JSkgcGx1cyB0aGUgdGltZSB0byBjb3B5IGFkYXB0ZXIgd2VpZ2h0cyB0byBHUFUgKG5lZ2xpZ2libGUgZm9yIHJhbmsgMTbigJM2NCBMb1JBOiBcdTAwM2MgMSBNQikuIExpYnJhcmllcyBsaWtlIFBFRlRcdTAwMjdzIGxvYWRfYWRhcHRlciBhbmQgc2V0X2FkYXB0ZXIgZW5hYmxlIHJ1bnRpbWUgdGFzayBzd2l0Y2hpbmcuIEZvciBMb1JBLCBub24tbWVyZ2VkIG1vZGUga2VlcHMgdGhlIEEgYW5kIEIgbWF0cmljZXMgc2VwYXJhdGUgZnJvbSB0aGUgYmFzZSB3ZWlnaHRzLCBlbmFibGluZyBzd2FwOyBtZXJnZWQgbW9kZSBmdXNlcyB0aGVtIGFuZCBjYW5ub3QgYmUgdW5zd2FwcGVkIHdpdGhvdXQgdGhlIG9yaWdpbmFsIGFkYXB0ZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHR5cGluZyBpbXBvcnQgRGljdFxuXG5jbGFzcyBNdWx0aVRhc2tMb1JBU2VydmVyOlxuICAgIFwiXCJcIlNlcnZlIG11bHRpcGxlIHRhc2tzIGJ5IHN3YXBwaW5nIExvUkEgYWRhcHRlcnMgb24gYSBzaGFyZWQgYmFzZSBtb2RlbC5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBiYXNlX21vZGVsOiBubi5Nb2R1bGUsIGxvcmFfcmFuazogaW50ID0gMTYpOlxuICAgICAgICBzZWxmLmJhc2UgPSBiYXNlX21vZGVsXG4gICAgICAgIHNlbGYucmFuayA9IGxvcmFfcmFua1xuICAgICAgICBzZWxmLmFkYXB0ZXJzOiBEaWN0W3N0ciwgRGljdFtzdHIsIHRvcmNoLlRlbnNvcl1dID0ge31cbiAgICAgICAgc2VsZi5hY3RpdmVfdGFzazogc3RyID0gTm9uZVxuXG4gICAgZGVmIHJlZ2lzdGVyX2FkYXB0ZXIoc2VsZiwgdGFza19uYW1lOiBzdHIsIGxvcmFfQTogdG9yY2guVGVuc29yLCBsb3JhX0I6IHRvcmNoLlRlbnNvcik6XG4gICAgICAgIHNlbGYuYWRhcHRlcnNbdGFza19uYW1lXSA9IHtcIkFcIjogbG9yYV9BLCBcIkJcIjogbG9yYV9CfVxuICAgICAgICBzaXplX2tiID0gKGxvcmFfQS5udW1lbCgpICsgbG9yYV9CLm51bWVsKCkpICogNCAvIDEwMjRcbiAgICAgICAgcHJpbnQoZlwiUmVnaXN0ZXJlZCBcdTAwMjd7dGFza19uYW1lfVx1MDAyNzogcmFuaz17c2VsZi5yYW5rfSwgc2l6ZT17c2l6ZV9rYjouMWZ9IEtCXCIpXG5cbiAgICBkZWYgYWN0aXZhdGUoc2VsZiwgdGFza19uYW1lOiBzdHIpOlxuICAgICAgICBpZiB0YXNrX25hbWUgbm90IGluIHNlbGYuYWRhcHRlcnM6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIlVua25vd24gdGFzazoge3Rhc2tfbmFtZX1cIilcbiAgICAgICAgc2VsZi5hY3RpdmVfdGFzayA9IHRhc2tfbmFtZVxuICAgICAgICAjIEluIHJlYWwgUEVGVDogbW9kZWwuc2V0X2FkYXB0ZXIodGFza19uYW1lKVxuICAgICAgICBwcmludChmXCJBY3RpdmF0ZWQgYWRhcHRlcjogXHUwMDI3e3Rhc2tfbmFtZX1cdTAwMjcgKG5vIGJhc2UgcmVsb2FkIHJlcXVpcmVkKVwiKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgb3V0ID0gc2VsZi5iYXNlKHgpXG4gICAgICAgIGlmIHNlbGYuYWN0aXZlX3Rhc2s6XG4gICAgICAgICAgICBhZGFwdGVyID0gc2VsZi5hZGFwdGVyc1tzZWxmLmFjdGl2ZV90YXNrXVxuICAgICAgICAgICAgIyBBcHBseSBMb1JBIGRlbHRhOiBvdXQgKz0geCBAIEEuVCBAIEIuVCAqICgxL3JhbmspXG4gICAgICAgICAgICBsb3JhX291dCA9ICh4IEAgYWRhcHRlcltcIkFcIl0uVCkgQCBhZGFwdGVyW1wiQlwiXS5UIC8gc2VsZi5yYW5rXG4gICAgICAgICAgICBvdXQgPSBvdXQgKyBsb3JhX291dFxuICAgICAgICByZXR1cm4gb3V0XG5cbmJhc2UgPSBubi5MaW5lYXIoNjQsIDY0KVxuc2VydmVyID0gTXVsdGlUYXNrTG9SQVNlcnZlcihiYXNlLCBsb3JhX3Jhbms9OClcbmZvciB0YXNrIGluIFtcInNlbnRpbWVudFwiLCBcIm5lclwiLCBcInFhXCJdOlxuICAgIEEgPSB0b3JjaC5yYW5kbig4LCA2NCkgKiAwLjAyXG4gICAgQiA9IHRvcmNoLnplcm9zKDY0LCA4KVxuICAgIHNlcnZlci5yZWdpc3Rlcl9hZGFwdGVyKHRhc2ssIEEsIEIpXG54ID0gdG9yY2gucmFuZG4oNCwgNjQpXG5mb3IgdGFzayBpbiBbXCJzZW50aW1lbnRcIiwgXCJuZXJcIiwgXCJxYVwiXTpcbiAgICBzZXJ2ZXIuYWN0aXZhdGUodGFzaylcbiAgICBvdXQgPSBzZXJ2ZXIuZm9yd2FyZCh4KVxuICAgIHByaW50KGZcIiAge3Rhc2t9IG91dHB1dCBub3JtOiB7b3V0Lm5vcm0oKTouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWV0aG9kIFN0cmVuZ3RocyBhbmQgV2Vha25lc3NlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm8gUEVGVCBtZXRob2QgZG9taW5hdGVzIGFsbCBkaW1lbnNpb25zLiBMb1JBKyBpcyB0aGUgc2FmZXN0IGRlZmF1bHQ6IGl0IGltcHJvdmVzIG92ZXIgTG9SQSBhdCB6ZXJvIGNvc3QsIG1lcmdlcyBjbGVhbmx5LCBhbmQgaXMgc3VwcG9ydGVkIGJ5IGV2ZXJ5IG1ham9yIGxpYnJhcnkuIFFMb1JBIGlzIGVzc2VudGlhbCB3aGVuIEdQVSBtZW1vcnkgaXMgdGhlIGJpbmRpbmcgY29uc3RyYWludCDigJQgaXQgZW5hYmxlcyA3QiBmaW5lLXR1bmluZyBvbiBhIHNpbmdsZSAxNiBHQiBHUFUgYXQgbW9kZXN0IHF1YWxpdHkgY29zdC4gRG9SQSBpcyB3b3J0aCBhZGRpbmcgd2hlbiBzcXVlZXppbmcgbWF4aW11bSBxdWFsaXR5IGZyb20gYSBmaXhlZCByYW5rIGFuZCBjb21wdXRlIGJ1ZGdldC4gUHJlZml4IFR1bmluZyBhbmQgQWRhcHRlciBsYXllcnMgc2hpbmUgb25seSBpbiBtdWx0aS10YXNrIGluZmVyZW5jZSBzZXR0aW5ncyB3aGVyZSBob3Qtc3dhcCBpcyByZXF1aXJlZCBhbmQgbGF0ZW5jeSBvdmVyaGVhZCBpcyBhY2NlcHRhYmxlLiBJQTMgaXMgdGhlIHJpZ2h0IGNob2ljZSBmb3IgdHJ1ZSBmZXctc2hvdCBzY2VuYXJpb3MgKFx1MDAzYyAxMDAgZXhhbXBsZXMpIHdoZXJlIExvUkEgd291bGQgb3ZlcmZpdC4gVmVSQSBpcyBmb3Igc2V0dGluZ3Mgd2l0aCBleHRyZW1lIG51bWJlcnMgb2YgdGFza3MgdG8gc3RvcmUgKHRob3VzYW5kcyBvZiBhZGFwdGVycykgd2hlcmUgcGVyLXRhc2sgc3RvcmFnZSBpcyB0aGUgYm90dGxlbmVjay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQRUZUIE1ldGhvZCBDb21wYXJpc29uIFRhYmxlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlRyYWluYWJsZSBQYXJhbXMiLCJNZXJnZSB0byBCYXNlIiwiTWVtb3J5IFJlZHVjdGlvbiIsIkJlc3QgRGF0YSBTaXplIiwiQmVzdCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJMb1JBIHI9MTYiLCJ+MC4wNSUgb2YgN0IiLCJZZXMg4oCUIHplcm8gbGF0ZW5jeSIsIk1pbmltYWwgKGJmMTYgYWRhcHRlcnMpIiwiMUvigJMxMDBLIiwiR2VuZXJhbC1wdXJwb3NlIGZpbmUtdHVuaW5nIl0sWyJMb1JBKyIsIn4wLjA1JSBvZiA3QiIsIlllcyDigJQgemVybyBsYXRlbmN5IiwiU2FtZSBhcyBMb1JBIiwiMUvigJMxMDBLIiwiRnJlZSB1cGdyYWRlIG92ZXIgTG9SQSwgYWx3YXlzIHByZWZlciJdLFsiRG9SQSIsIn4wLjA1MSUgb2YgN0IiLCJZZXMg4oCUIHplcm8gbGF0ZW5jeSIsIlNhbWUgYXMgTG9SQSIsIjVL4oCTMTAwSyIsIk1heGltdW0gcXVhbGl0eSBhdCBzYW1lIHJhbmsiXSxbIlFMb1JBIiwifjAuMDUlIG9mIDdCIiwiWWVzIChkZXF1YW50IGZpcnN0KSIsIjUw4oCTNzUlIHZzIGJmMTYiLCIxS+KAkzUwSyIsIjE2IEdCIEdQVSBmaW5lLXR1bmluZyJdLFsiVmVSQSIsIn4wLjAwNSUgb2YgN0IiLCJObyAoc2hhcmVkIHJhbmRvbSkiLCJTYW1lIGFzIExvUkEiLCI1S+KAkzUwSyIsIlN0b3JpbmcgdGhvdXNhbmRzIG9mIHRhc2sgYWRhcHRlcnMiXSxbIlByZWZpeCBUdW5pbmciLCJ+MC4wMSUgb2YgN0IiLCJObyAodmlydHVhbCB0b2tlbnMpIiwiTWluaW1hbCIsIjEwSysgKHNjYWxlIG5lZWRlZCkiLCJNdWx0aS10YXNrIGhvdC1zd2FwLCBsYXJnZSBtb2RlbHMgb25seSJdLFsiQWRhcHRlcnMiLCJ+MC4x4oCTMSUgb2YgN0IiLCJObyAoZXh0cmEgbGF5ZXJzKSIsIk1pbmltYWwiLCI1S+KAkzEwMEsiLCJIb3Qtc3dhcCBtdWx0aS10YXNrIHNlcnZpbmciXSxbIklBMyIsIn4wLjAwMiUgb2YgN0IiLCJObyAocmVzY2FsaW5nIG9ubHkpIiwiTWluaW1hbCIsIlx1MDAzYyAxMDAgKGZldy1zaG90KSIsIkV4dHJlbWUgZmV3LXNob3QsIEdQVC0zIHNjYWxlIG1vZGVscyJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlByb2R1Y3Rpb24gRmluZS1UdW5pbmcgRGVmYXVsdCBTdGFjayIsImNvbnRlbnQiOiJGb3IgbW9zdCBwcm9kdWN0aW9uIGZpbmUtdHVuaW5nOiBzdGFydCB3aXRoIExvUkErIChmcmVlIGltcHJvdmVtZW50IG92ZXIgTG9SQSkgKyBEb1JBIGlmIHlvdSBuZWVkIG1heGltdW0gcXVhbGl0eS4gQWRkIFFMb1JBIG9ubHkgaWYgR1BVIG1lbW9yeSBpcyB0aGUgYmluZGluZyBjb25zdHJhaW50LiBVc2UgYWRhcHRlciBsYXllcnMgb3IgcHJlZml4IHR1bmluZyBvbmx5IGlmIHlvdSBuZWVkIGhvdC1zd2FwIG11bHRpLXRhc2sgaW5mZXJlbmNlIHdpdGhvdXQgcmVsb2FkaW5nLiBWZVJBIGlzIHdvcnRoIGNvbnNpZGVyaW5nIG9ubHkgd2hlbiB5b3UgbmVlZCB0byBzdG9yZSBtb3JlIHRoYW4gMTAwIGRpZmZlcmVudCB0YXNrIGFkYXB0ZXJzIOKAlCBmb3IgZmV3ZXIgdGFza3MsIExvUkFcdTAwMjdzIHN0b3JhZ2UgaXMgbWFuYWdlYWJsZS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkxvUkEgcmFuayBzZWxlY3Rpb246IHJhbmsgNOKAkzggZm9yIGNsYXNzaWZpY2F0aW9uL05FUjsgcmFuayAxNuKAkzMyIGZvciBnZW5lcmF0aW9uOyByYW5rIDY0IGZvciBhbGlnbm1lbnQgdGFza3MuIiwiTG9SQSB0YXJnZXQgbW9kdWxlczogYWx3YXlzIGluY2x1ZGUgcV9wcm9qLCB2X3Byb2ogYXQgbWluaW11bTsgYWRkIGtfcHJvaiwgb19wcm9qLCBnYXRlX3Byb2ogZm9yIGhpZ2hlciBxdWFsaXR5LiIsIlFMb1JBOiB1c2UgTkY0IHF1YW50aXphdGlvbiAobm90IElOVDgpIGZvciBiZXN0IHF1YWxpdHk7IGFkZCBkb3VibGUgcXVhbnRpemF0aW9uIHRvIHNhdmUgYW5vdGhlciB+MC41IEdCLiIsIkRvUkE6IGF2YWlsYWJsZSBpbiBIdWdnaW5nIEZhY2UgUEVGVCBcdTAwM2U9IDAuOS4wIHZpYSB1c2VfZG9yYT1UcnVlIGluIExvcmFDb25maWc7IG5vIG90aGVyIGNoYW5nZXMgbmVlZGVkLiIsIk1lcmdpbmc6IGNhbGwgbW9kZWwubWVyZ2VfYW5kX3VubG9hZCgpIGFmdGVyIHRyYWluaW5nIHRvIGFic29yYiBMb1JBIGludG8gYmFzZSB3ZWlnaHRzIGJlZm9yZSBkZXBsb3ltZW50LiIsIkFkYXB0ZXIgc3dhcCB0aW1pbmc6IHN3YXBwaW5nIGEgcmFuay0xNiBMb1JBIGFkYXB0ZXIgdGFrZXMgXHUwMDNjIDUgbXMgaW5jbHVkaW5nIENQVS10by1HUFUgdHJhbnNmZXIgZm9yIDdCIG1vZGVscy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# PEFT Selection Guide — Choosing the Right Method by Task, Data, and Constraints

With a growing zoo of PEFT methods — LoRA, QLoRA, DoRA, LoRA+, VeRA, Prefix Tuning, Adapters, IA3 — choosing the right one requires reasoning about five dimensions simultaneously: data size, task type, GPU memory budget, inference latency requirement, and whether you need to merge or swap adapters at runtime. No single method dominates all dimensions; the right choice depends on which constraints are binding in your setting.

## Key Decision Dimensions

- Data size: < 100 examples → IA3; 100–10K → LoRA or LoRA+; 10K–100K → LoRA+/DoRA; > 100K → DoRA or full fine-tune with LoRA regularization.
- Task type: understanding (classification, NER) → LoRA rank 4–16; generation → LoRA rank 16–64; alignment (RLHF/DPO) → LoRA + DPO is standard.
- GPU memory: < 16 GB → QLoRA (4-bit base); 16–40 GB → LoRA or DoRA in bf16; > 40 GB → DoRA full precision.
- Inference latency: zero overhead required → merge LoRA into base weights; can tolerate extra layers → Adapters or Prefix Tuning; extreme few-shot → IA3 (3 rescaling vectors per layer).
- Multi-task serving: hot-swap without reloading → Adapters or non-merged LoRA; single task at a time → merge LoRA for zero latency.
- Merging / task arithmetic: only LoRA and DoRA produce mergeable delta matrices; Adapters and Prefix Tuning cannot be merged into base weights cleanly.

## PEFT Selection Decision Tree

A systematic decision function removes the guesswork. The tree below checks binding constraints in priority order: memory first (QLoRA), then extreme few-shot (IA3), then multi-task inference (Adapters), then quality priority (DoRA), and defaults to LoRA+ for the general case. LoRA+ is a free improvement over standard LoRA — it sets different learning rates for the A and B matrices — and should always be preferred over vanilla LoRA when there is no other constraint.

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class PEFTRecommendation:
    method: str
    reason: str
    lora_rank: Optional[int] = None
    notes: str = ""

def select_peft_method(
    data_size: int,
    gpu_memory_gb: float,
    task_type: str = "generation",
    multi_task_inference: bool = False,
    need_merge: bool = False,
    quality_priority: bool = False,
) -> PEFTRecommendation:
    """Return the recommended PEFT method given task constraints."""
    if data_size < 100:
        return PEFTRecommendation("IA3", "Extreme few-shot: IA3 has fewest trainable params",
                                  notes="Only ~3 vectors per layer; no rank to tune")
    if gpu_memory_gb < 16:
        return PEFTRecommendation("QLoRA", "Memory constrained: 4-bit base + bf16 adapters",
                                  lora_rank=16, notes="Use bitsandbytes NF4 + paged optimizer")
    if multi_task_inference and not need_merge:
        return PEFTRecommendation("Adapters", "Hot-swap at inference without reloading base",
                                  notes="Use PEFT AdapterHub; swap by task_id")
    if need_merge and quality_priority:
        return PEFTRecommendation("LoRA+ + DoRA", "Best quality, merges to zero latency",
                                  lora_rank=32, notes="DoRA: separate magnitude/direction learning")
    if need_merge:
        return PEFTRecommendation("LoRA+", "Mergeable, free LR improvement over LoRA",
                                  lora_rank=16, notes="Set lr_ratio=16 for B matrix")
    return PEFTRecommendation("LoRA+", "Best general-purpose default",
                              lora_rank=16, notes="Start here; add DoRA if quality is insufficient")

test_cases = [
    (50,   24, "classification", False, False, False),
    (500,  12, "generation",     False, True,  False),
    (5000, 24, "generation",     False, True,  True),
    (50000,80, "alignment",      False, True,  True),
    (2000, 40, "generation",     True,  False, False),
]
for args in test_cases:
    r = select_peft_method(*args)
    print(f"data={args[0]:>6}, gpu={args[1]:>2}GB -> {r.method}: {r.reason}")
```

## Parameter Efficiency vs Quality Tradeoff

The efficiency-quality Pareto frontier varies by method. IA3 sits at the extreme-efficiency end (< 0.02% trainable parameters) but requires large base models to shine — on GPT-3 scale it matches LoRA, but on 1B-scale models it underperforms. LoRA at rank 16 is the sweet spot for most 1–7B models: enough capacity for generation tasks, negligible inference overhead when merged. DoRA adds ~1% overhead over LoRA in training time but consistently outperforms LoRA by 1–3% absolute on generation benchmarks. VeRA uses shared random matrices with learnable rescaling vectors, achieving LoRA-comparable quality with 10× fewer trainable parameters but cannot be merged cleanly.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class BenchmarkResult:
    method: str
    trainable_params_pct: float
    train_time_relative: float  # relative to LoRA=1.0
    eval_score: float           # normalized: LoRA=0.871
    peak_memory_gb: float
    merge_to_base: bool

def run_peft_benchmark(model_params: int = 7_000_000_000) -> List[BenchmarkResult]:
    """Simulated benchmark results (from published papers and internal evals)."""
    results = [
        BenchmarkResult("LoRA r=16",    0.050, 1.00, 0.871, 14.2, True),
        BenchmarkResult("LoRA+ r=16",   0.050, 0.99, 0.876, 14.2, True),
        BenchmarkResult("DoRA r=16",    0.051, 1.04, 0.882, 14.6, True),
        BenchmarkResult("QLoRA r=16",   0.050, 1.18, 0.868,  8.1, True),
        BenchmarkResult("IA3",          0.002, 0.80, 0.841, 13.8, False),
        BenchmarkResult("Adapters",     0.120, 1.13, 0.874, 15.1, False),
        BenchmarkResult("PrefixTuning", 0.010, 0.95, 0.843, 14.0, False),
        BenchmarkResult("VeRA r=256",   0.005, 1.02, 0.869, 14.3, False),
    ]
    return results

results = run_peft_benchmark()
print(f"{'Method':>16} {'Params%':>8} {'Time':>6} {'Score':>7} {'Mem(GB)':>8} {'Merge':>6}")
print("-" * 58)
for r in results:
    merge_str = "Yes" if r.merge_to_base else "No"
    print(f"{r.method:>16} {r.trainable_params_pct:>7.3f}% {r.train_time_relative:>6.2f}x "
          f"{r.eval_score:>7.3f} {r.peak_memory_gb:>8.1f} {merge_str:>6}")
```

## Inference Overhead Comparison

Inference latency is where methods diverge most sharply. Merged LoRA is identical to the base model at inference — the adapter matrices are absorbed into the base weights, adding zero latency. Non-merged LoRA adds two extra matmuls (Ax and Bx) per adapted layer, roughly 3–8% overhead on GPU for rank 16. Adapter layers insert a bottleneck MLP (down-project → activation → up-project) adding 5–15% overhead depending on rank and model size. Prefix Tuning prepends k virtual tokens to the key-value cache, increasing attention computation by k/seq_len — for k=50 tokens on a 512-token sequence, overhead is ~10%. IA3 rescales by learned vectors: the overhead is a single element-wise multiply per layer, < 1%.

```python
import torch
import torch.nn as nn
import time

def measure_latency(model: nn.Module, x: torch.Tensor,
                    n_warmup: int = 20, n_runs: int = 100) -> float:
    """Return average forward-pass latency in milliseconds."""
    model.eval()
    with torch.no_grad():
        for _ in range(n_warmup):
            model(x)
    t0 = time.perf_counter()
    with torch.no_grad():
        for _ in range(n_runs):
            model(x)
    return (time.perf_counter() - t0) * 1000 / n_runs

D = 512
# Merged LoRA: same as base model
base = nn.Sequential(nn.Linear(D, D), nn.ReLU(), nn.Linear(D, D))
# Non-merged LoRA: extra matmul per layer (simulated as extra small linear)
non_merged_lora = nn.Sequential(
    nn.Linear(D, D), nn.ReLU(), nn.Linear(D, D),
    nn.Linear(D, 16, bias=False), nn.Linear(16, D, bias=False)  # LoRA A+B
)
# Adapter: extra bottleneck layers
adapter = nn.Sequential(
    nn.Linear(D, D), nn.ReLU(),
    nn.Linear(D, 64), nn.ReLU(), nn.Linear(64, D),  # adapter bottleneck
    nn.Linear(D, D)
)
x = torch.randn(16, D)
for name, model in [("Base/MergedLoRA", base), ("NonMergedLoRA", non_merged_lora), ("Adapter", adapter)]:
    lat = measure_latency(model, x)
    params = sum(p.numel() for p in model.parameters())
    print(f"{name:>16}: {lat:.3f} ms/batch  ({params:,} params)")
```

## Multi-Task Serving with Adapter Swap

When serving multiple tasks from one deployment, non-merged adapters offer hot-swap: load the base model once and swap the adapter weights per request without reloading the full model. This is efficient when tasks share a common base and differ only in the adapter. The overhead is the adapter forward pass (5–15%) plus the time to copy adapter weights to GPU (negligible for rank 16–64 LoRA: < 1 MB). Libraries like PEFT's load_adapter and set_adapter enable runtime task switching. For LoRA, non-merged mode keeps the A and B matrices separate from the base weights, enabling swap; merged mode fuses them and cannot be unswapped without the original adapter.

```python
import torch
import torch.nn as nn
from typing import Dict

class MultiTaskLoRAServer:
    """Serve multiple tasks by swapping LoRA adapters on a shared base model."""

    def __init__(self, base_model: nn.Module, lora_rank: int = 16):
        self.base = base_model
        self.rank = lora_rank
        self.adapters: Dict[str, Dict[str, torch.Tensor]] = {}
        self.active_task: str = None

    def register_adapter(self, task_name: str, lora_A: torch.Tensor, lora_B: torch.Tensor):
        self.adapters[task_name] = {"A": lora_A, "B": lora_B}
        size_kb = (lora_A.numel() + lora_B.numel()) * 4 / 1024
        print(f"Registered '{task_name}': rank={self.rank}, size={size_kb:.1f} KB")

    def activate(self, task_name: str):
        if task_name not in self.adapters:
            raise ValueError(f"Unknown task: {task_name}")
        self.active_task = task_name
        # In real PEFT: model.set_adapter(task_name)
        print(f"Activated adapter: '{task_name}' (no base reload required)")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = self.base(x)
        if self.active_task:
            adapter = self.adapters[self.active_task]
            # Apply LoRA delta: out += x @ A.T @ B.T * (1/rank)
            lora_out = (x @ adapter["A"].T) @ adapter["B"].T / self.rank
            out = out + lora_out
        return out

base = nn.Linear(64, 64)
server = MultiTaskLoRAServer(base, lora_rank=8)
for task in ["sentiment", "ner", "qa"]:
    A = torch.randn(8, 64) * 0.02
    B = torch.zeros(64, 8)
    server.register_adapter(task, A, B)
x = torch.randn(4, 64)
for task in ["sentiment", "ner", "qa"]:
    server.activate(task)
    out = server.forward(x)
    print(f"  {task} output norm: {out.norm():.4f}")
```

## Method Strengths and Weaknesses

No PEFT method dominates all dimensions. LoRA+ is the safest default: it improves over LoRA at zero cost, merges cleanly, and is supported by every major library. QLoRA is essential when GPU memory is the binding constraint — it enables 7B fine-tuning on a single 16 GB GPU at modest quality cost. DoRA is worth adding when squeezing maximum quality from a fixed rank and compute budget. Prefix Tuning and Adapter layers shine only in multi-task inference settings where hot-swap is required and latency overhead is acceptable. IA3 is the right choice for true few-shot scenarios (< 100 examples) where LoRA would overfit. VeRA is for settings with extreme numbers of tasks to store (thousands of adapters) where per-task storage is the bottleneck.

## PEFT Method Comparison Table

| Method | Trainable Params | Merge to Base | Memory Reduction | Best Data Size | Best Use Case |
| --- | --- | --- | --- | --- | --- |
| LoRA r=16 | ~0.05% of 7B | Yes — zero latency | Minimal (bf16 adapters) | 1K–100K | General-purpose fine-tuning |
| LoRA+ | ~0.05% of 7B | Yes — zero latency | Same as LoRA | 1K–100K | Free upgrade over LoRA, always prefer |
| DoRA | ~0.051% of 7B | Yes — zero latency | Same as LoRA | 5K–100K | Maximum quality at same rank |
| QLoRA | ~0.05% of 7B | Yes (dequant first) | 50–75% vs bf16 | 1K–50K | 16 GB GPU fine-tuning |
| VeRA | ~0.005% of 7B | No (shared random) | Same as LoRA | 5K–50K | Storing thousands of task adapters |
| Prefix Tuning | ~0.01% of 7B | No (virtual tokens) | Minimal | 10K+ (scale needed) | Multi-task hot-swap, large models only |
| Adapters | ~0.1–1% of 7B | No (extra layers) | Minimal | 5K–100K | Hot-swap multi-task serving |
| IA3 | ~0.002% of 7B | No (rescaling only) | Minimal | < 100 (few-shot) | Extreme few-shot, GPT-3 scale models |

> **Production Fine-Tuning Default Stack**: For most production fine-tuning: start with LoRA+ (free improvement over LoRA) + DoRA if you need maximum quality. Add QLoRA only if GPU memory is the binding constraint. Use adapter layers or prefix tuning only if you need hot-swap multi-task inference without reloading. VeRA is worth considering only when you need to store more than 100 different task adapters — for fewer tasks, LoRA's storage is manageable.

- LoRA rank selection: rank 4–8 for classification/NER; rank 16–32 for generation; rank 64 for alignment tasks.
- LoRA target modules: always include q_proj, v_proj at minimum; add k_proj, o_proj, gate_proj for higher quality.
- QLoRA: use NF4 quantization (not INT8) for best quality; add double quantization to save another ~0.5 GB.
- DoRA: available in Hugging Face PEFT >= 0.9.0 via use_dora=True in LoraConfig; no other changes needed.
- Merging: call model.merge_and_unload() after training to absorb LoRA into base weights before deployment.
- Adapter swap timing: swapping a rank-16 LoRA adapter takes < 5 ms including CPU-to-GPU transfer for 7B models.

---

