---
title: "Stationarity — Unit Root Tests (ADF, KPSS)"
slug: "stationarity-unit-root-tests"
description: "Derive strict and weak stationarity from first principles, understand the unit root as a random walk, and apply ADF, KPSS, and PP tests to diagnose and correct non-stationarity via differencing and log transforms."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhdGlvbmFyaXR5IGlzIHRoZSBjb3JuZXJzdG9uZSBhc3N1bXB0aW9uIG9mIGNsYXNzaWNhbCB0aW1lLXNlcmllcyBtb2RlbGxpbmcuIEEgc3RhdGlvbmFyeSBwcm9jZXNzIGhhcyBzdGF0aXN0aWNhbCBwcm9wZXJ0aWVzIHRoYXQgZG8gbm90IGNoYW5nZSBvdmVyIHRpbWUsIGFsbG93aW5nIG1vZGVscyB0byBleHBsb2l0IHBhc3QgcGF0dGVybnMgdG8gZm9yZWNhc3QgdGhlIGZ1dHVyZS4gTm9uLXN0YXRpb25hcnkgc2VyaWVzIOKAlCB0aG9zZSB3aXRoIHRyZW5kcywgdW5pdCByb290cywgb3IgdGltZS12YXJ5aW5nIHZhcmlhbmNlIOKAlCB2aW9sYXRlIHRoZSBhc3N1bXB0aW9ucyBiZWhpbmQgQVJJTUEsIGF1dG9jb3JyZWxhdGlvbiBlc3RpbWF0aW9uLCBhbmQgbW9zdCBoeXBvdGhlc2lzIHRlc3RzLiBCZWZvcmUgZml0dGluZyBhbnkgbW9kZWwsIGRpYWdub3NpbmcgYW5kIGNvcnJlY3Rpbmcgbm9uLXN0YXRpb25hcml0eSBpcyBtYW5kYXRvcnkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RyaWN0IGFuZCBXZWFrIFN0YXRpb25hcml0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RyaWN0IChzdHJvbmcpIHN0YXRpb25hcml0eSByZXF1aXJlcyB0aGF0IHRoZSBlbnRpcmUgam9pbnQgZGlzdHJpYnV0aW9uIG9mICh54oKc4oKBLCB54oKc4oKCLCDigKYsIHnigpzigpYpIGlzIGlkZW50aWNhbCB0byAoeeKCnOKCgeKCis+ELCB54oKc4oKC4oKKz4QsIOKApiwgeeKCnOKCluKCis+EKSBmb3IgYWxsIGxhZ3Mgz4QgYW5kIGFsbCBrLiBUaGlzIGlzIGEgdmVyeSBzdHJvbmcgY29uZGl0aW9uIHRoYXQgaXMgcmFyZWx5IHZlcmlmaWFibGUgZW1waXJpY2FsbHkuIFdlYWsgKGNvdmFyaWFuY2UpIHN0YXRpb25hcml0eSByZXF1aXJlcyBvbmx5IHR3byBjb25kaXRpb25zOiBhIGNvbnN0YW50IG1lYW4gRVt54oKcXSA9IM68IGZvciBhbGwgdCwgYW5kIGFuIGF1dG9jb3ZhcmlhbmNlIENvdih54oKcLCB54oKc4oKK4oKWKSA9IM6zKGspIHRoYXQgZGVwZW5kcyBvbmx5IG9uIGxhZyBrLCBub3Qgb24gdGltZSB0LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2VhayBzdGF0aW9uYXJpdHkgaW1wbGllcyB0aGF0IHRoZSB2YXJpYW5jZSBWYXIoeeKCnCkgPSDOsygwKSBpcyBhbHNvIGNvbnN0YW50LiBTdHJpY3Qgc3RhdGlvbmFyaXR5IHdpdGggZmluaXRlIHNlY29uZCBtb21lbnRzIGltcGxpZXMgd2VhayBzdGF0aW9uYXJpdHksIGJ1dCBub3QgdmljZSB2ZXJzYSDigJQgYSB0LWRpc3RyaWJ1dGlvbiBwcm9jZXNzIGNhbiBiZSB3ZWFrbHkgc3RhdGlvbmFyeSB3aXRob3V0IGJlaW5nIHN0cmljdGx5IHN0YXRpb25hcnkuIEZvciBwcmFjdGljYWwgZm9yZWNhc3RpbmcsIHdlYWsgc3RhdGlvbmFyaXR5IGlzIHN1ZmZpY2llbnQgYW5kIGlzIHdoYXQgQVJJTUEgbW9kZWxzIHJlcXVpcmUgYWZ0ZXIgZCBkaWZmZXJlbmNlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaHkgU3RhdGlvbmFyaXR5IE1hdHRlcnMgZm9yIEZvcmVjYXN0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBUklNQSBmb3JlY2FzdGluZyByZWxpZXMgb24gYXV0b2NvdmFyaWFuY2VzIHRoYXQgYXJlIHN0YWJsZSBhY3Jvc3MgdGltZS4gSWYgzrMoaykgY2hhbmdlcyB3aXRoIHQsIHRoZSBhdXRvY29ycmVsYXRpb24gZnVuY3Rpb24gZXN0aW1hdGVkIGZyb20gaGlzdG9yaWNhbCBkYXRhIGRvZXMgbm90IGFwcGx5IHRvIHRoZSBmdXR1cmUuIFNwdXJpb3VzIHJlZ3Jlc3Npb24gaXMgYW5vdGhlciBkYW5nZXI6IHJlZ3Jlc3NpbmcgdHdvIGluZGVwZW5kZW50IHJhbmRvbSB3YWxrcyBvbiBlYWNoIG90aGVyIHlpZWxkcyBSwrIgY2xvc2UgdG8gMSBhbmQgc2lnbmlmaWNhbnQgdC1zdGF0aXN0aWNzIHB1cmVseSBieSBjaGFuY2UsIGJlY2F1c2UgYm90aCBzaGFyZSBhIGNvbW1vbiBzdG9jaGFzdGljIHRyZW5kLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQVJJTUEgbW9kZWxzIHJlcXVpcmUgc3RhdGlvbmFyaXR5IGFmdGVyIGQgZGlmZmVyZW5jZXMg4oCUIHRoZSBkIHBhcmFtZXRlciBpcyB0aGUgbnVtYmVyIG9mIHVuaXQgcm9vdHMuIiwiQXV0b2NvcnJlbGF0aW9uIGVzdGltYXRlcyDOs8yCKGspIGFyZSBpbmNvbnNpc3RlbnQgZm9yIG5vbi1zdGF0aW9uYXJ5IHNlcmllcyDigJQgdGhleSBkbyBub3QgY29udmVyZ2UgdG8gdHJ1ZSB2YWx1ZXMuIiwiU3B1cmlvdXMgcmVncmVzc2lvbjogdHdvIGluZGVwZW5kZW50IHJhbmRvbSB3YWxrcyBtYXkgYXBwZWFyIGNvcnJlbGF0ZWQgKHQtc3RhdCBzaWduaWZpY2FudCwgUsKy4omIMSkgd2l0aCBubyByZWFsIHJlbGF0aW9uc2hpcC4iLCJHcmFuZ2VyIGNhdXNhbGl0eSB0ZXN0cyBhbmQgVkFSIG1vZGVscyByZXF1aXJlIGFsbCB2YXJpYWJsZXMgdG8gYmUgc3RhdGlvbmFyeSBvciBjby1pbnRlZ3JhdGVkLiIsIlByZWRpY3Rpb24gaW50ZXJ2YWxzIGdyb3cgY29ycmVjdGx5IG9ubHkgd2hlbiB0aGUgZGlmZmVyZW5jZWQgc2VyaWVzIGlzIHN0YXRpb25hcnkuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuaXQgUm9vdCDigJQgVGhlIFJhbmRvbSBXYWxrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2ltcGxlc3Qgbm9uLXN0YXRpb25hcnkgcHJvY2VzcyBpcyB0aGUgcmFuZG9tIHdhbGsgeeKCnCA9IHnigpzigovigoEgKyDOteKCnCwgd2hpY2ggaXMgYW4gQVIoMSkgd2l0aCBjb2VmZmljaWVudCDPgSA9IDEuIFRoZSBjaGFyYWN0ZXJpc3RpYyByb290IGVxdWFscyAxICh0aGUgdW5pdCBjaXJjbGUgcm9vdCkuIFZhcmlhbmNlIGdyb3dzIGxpbmVhcmx5OiBWYXIoeeKCnCkgPSB0wrfPg8KyLCBzbyB0aGUgcHJvY2VzcyBkcmlmdHMgd2l0aG91dCBib3VuZC4gTW9yZSBnZW5lcmFsbHksIHnigpwgPSDPgXnigpzigovigoEgKyDOteKCnCBpcyBzdGF0aW9uYXJ5IHdoZW4gfM+BfCBcdTAwM2MgMSAocm9vdHMgb2YgMSDiiJIgz4FCID0gMCBsaWUgb3V0c2lkZSB0aGUgdW5pdCBjaXJjbGUpIGFuZCBub24tc3RhdGlvbmFyeSB3aGVuIM+BID0gMS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0dG9vbHMgaW1wb3J0IGFkZnVsbGVyXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubiA9IDMwMFxuXG4jIFN0YXRpb25hcnkgQVIoMSkgd2l0aCB8cGhpfCBcdTAwM2MgMVxucGhpID0gMC43XG5lcHMgPSBucC5yYW5kb20ucmFuZG4obilcbnlfYXIgPSBucC56ZXJvcyhuKVxuZm9yIHQgaW4gcmFuZ2UoMSwgbik6XG4gICAgeV9hclt0XSA9IHBoaSAqIHlfYXJbdC0xXSArIGVwc1t0XVxuXG4jIE5vbi1zdGF0aW9uYXJ5OiB1bml0LXJvb3QgcmFuZG9tIHdhbGsgKHBoaSA9IDEpXG55X3J3ID0gbnAuY3Vtc3VtKG5wLnJhbmRvbS5yYW5kbihuKSlcblxuIyBDb21wYXJlIHZhcmlhbmNlIGdyb3d0aFxuZm9yIGhhbGYgaW4gWzc1LCAxNTAsIDIyNSwgMzAwXTpcbiAgICBzdGRfYXIgPSB5X2FyWzpoYWxmXS5zdGQoKVxuICAgIHN0ZF9ydyA9IHlfcndbOmhhbGZdLnN0ZCgpXG4gICAgcHJpbnQoZlwibj17aGFsZjozZH0gIEFSKDEpIHN0ZD17c3RkX2FyOi4zZn0gIFJXIHN0ZD17c3RkX3J3Oi4zZn1cIilcblxuYWRmX2FyID0gYWRmdWxsZXIoeV9hciwgYXV0b2xhZz1cdTAwMjdBSUNcdTAwMjcpWzFdXG5hZGZfcncgPSBhZGZ1bGxlcih5X3J3LCBhdXRvbGFnPVx1MDAyN0FJQ1x1MDAyNylbMV1cbnByaW50KGZcIlxcbkFERiBwOiBBUigxKT17YWRmX2FyOi40Zn0gKHN0YXRpb25hcnkpICBSVz17YWRmX3J3Oi40Zn0gKG5vbi1zdGF0aW9uYXJ5KVwiKVxucHJpbnQoXCJBUigxKSBzdGQgc3RheXMgYm91bmRlZDsgUlcgc3RkIGdyb3dzIOKAlCBrZXkgZGlhZ25vc3RpYyBkaWZmZXJlbmNlXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXVnbWVudGVkIERpY2tleS1GdWxsZXIgKEFERikgVGVzdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEFERiB0ZXN0IHJlZ3Jlc3NlcyDOlHnigpwgb24geeKCnOKCi+KCgSBhbmQgbGFnZ2VkIGRpZmZlcmVuY2VzIM6UeeKCnOKCi+KCgSwg4oCmLCDOlHnigpzigovigpYgdG8gcmVtb3ZlIHNlcmlhbCBjb3JyZWxhdGlvbiBmcm9tIHJlc2lkdWFscy4gVGhlIHQtc3RhdGlzdGljIG9uIHRoZSB54oKc4oKL4oKBIGNvZWZmaWNpZW50IHRlc3RzIEjigoA6IM+BID0gMSAodW5pdCByb290LCBub24tc3RhdGlvbmFyeSkgYWdhaW5zdCBI4oKBOiDPgSBcdTAwM2MgMSAoc3RhdGlvbmFyeSkuIENyaXRpY2FsIHZhbHVlcyBhcmUgbm9uLXN0YW5kYXJkIChtb3JlIG5lZ2F0aXZlIHRoYW4gbm9ybWFsIHQtZGlzdHJpYnV0aW9uKSBiZWNhdXNlIHRoZSB0ZXN0IHN0YXRpc3RpYyBpcyBub3QgYXN5bXB0b3RpY2FsbHkgbm9ybWFsIHVuZGVyIEjigoAuIFJlamVjdGluZyBI4oKAIGF0IHRoZSA1JSBsZXZlbCBtZWFucyB0aGUgc2VyaWVzIGlzIHN0YXRpb25hcnkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2Euc3RhdHRvb2xzIGltcG9ydCBhZGZ1bGxlclxuXG5ucC5yYW5kb20uc2VlZCgwKVxubiA9IDI1MFxuXG55X3N0YXQgPSBucC56ZXJvcyhuKVxuZm9yIHQgaW4gcmFuZ2UoMSwgbik6XG4gICAgeV9zdGF0W3RdID0gMC42ICogeV9zdGF0W3QtMV0gKyBucC5yYW5kb20ucmFuZG4oKVxuXG55X3J3ID0gbnAuY3Vtc3VtKG5wLnJhbmRvbS5yYW5kbihuKSlcblxuZGVmIGFkZl9yZXBvcnQoc2VyaWVzLCBsYWJlbCwgcmVncmVzc2lvbj1cdTAwMjdjXHUwMDI3KTpcbiAgICBzdGF0LCBwLCBsYWdzLCBub2JzLCBjcml0LCBfID0gYWRmdWxsZXIoc2VyaWVzLCBhdXRvbGFnPVx1MDAyN0FJQ1x1MDAyNywgcmVncmVzc2lvbj1yZWdyZXNzaW9uKVxuICAgIGRlY2lzaW9uID0gXCJTVEFUSU9OQVJZXCIgaWYgcCBcdTAwM2MgMC4wNSBlbHNlIFwiTk9OLVNUQVRJT05BUllcIlxuICAgIHByaW50KGZcIlxcbntsYWJlbH1cIilcbiAgICBwcmludChmXCIgIEFERiBzdGF0aXN0aWMgPSB7c3RhdDouNGZ9XCIpXG4gICAgcHJpbnQoZlwiICBwLXZhbHVlICAgICAgID0ge3A6LjRmfSAgPVx1MDAzZSB7ZGVjaXNpb259XCIpXG4gICAgcHJpbnQoZlwiICBMYWdzIHVzZWQgICAgID0ge2xhZ3N9XCIpXG4gICAgcHJpbnQoZlwiICBDcml0aWNhbCB2YWxzOiAxJT17Y3JpdFtcdTAwMjcxJVx1MDAyN106LjNmfSAgNSU9e2NyaXRbXHUwMDI3NSVcdTAwMjddOi4zZn0gIDEwJT17Y3JpdFtcdTAwMjcxMCVcdTAwMjddOi4zZn1cIilcblxuYWRmX3JlcG9ydCh5X3N0YXQsIFwiQVIoMSkgcGhpPTAuNiAgW2V4cGVjdDogU1RBVElPTkFSWV1cIilcbmFkZl9yZXBvcnQoeV9ydywgICBcIlJhbmRvbSBXYWxrICAgIFtleHBlY3Q6IE5PTi1TVEFUSU9OQVJZXVwiKVxuYWRmX3JlcG9ydCh5X3J3LCAgIFwiUmFuZG9tIFdhbGsgKHdpdGggdHJlbmQgcmVncmVzc2lvbilcIiwgcmVncmVzc2lvbj1cdTAwMjdjdFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLUFNTIFRlc3QgYW5kIFJlY29uY2lsaW5nIHdpdGggQURGIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgS1BTUyAoS3dpYXRrb3dza2ktUGhpbGxpcHMtU2NobWlkdC1TaGluKSB0ZXN0IGhhcyB0aGUgb3Bwb3NpdGUgbnVsbCBoeXBvdGhlc2lzOiBI4oKAOiB0aGUgc2VyaWVzIGlzIHN0YXRpb25hcnkgKGxldmVsIG9yIHRyZW5kLXN0YXRpb25hcnkpLiBSZWplY3RpbmcgSOKCgCBtZWFucyB0aGUgc2VyaWVzIGhhcyBhIHVuaXQgcm9vdC4gVXNpbmcgQURGIGFuZCBLUFNTIHRvZ2V0aGVyIHJlc29sdmVzIGFtYmlndWl0eTogaWYgQURGIHJlamVjdHMgSOKCgCAoc3RhdGlvbmFyeSkgYW5kIEtQU1MgZG9lcyBub3QgcmVqZWN0IChzdGF0aW9uYXJ5KSwgYm90aCB0ZXN0cyBhZ3JlZSB0aGUgc2VyaWVzIGlzIHN0YXRpb25hcnkuIElmIGJvdGggdGVzdHMgcmVqZWN0IHRoZWlyIHJlc3BlY3RpdmUgbnVsbHMsIHRoZSBldmlkZW5jZSBwb2ludHMgdG8gbm9uLXN0YXRpb25hcml0eS4gRGlzYWdyZWVtZW50IHN1Z2dlc3RzIHBvc3NpYmxlIHRyZW5kLXN0YXRpb25hcml0eSBvciBuZWFyLXVuaXQtcm9vdCBiZWhhdmlvdXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2Euc3RhdHRvb2xzIGltcG9ydCBhZGZ1bGxlciwga3Bzc1xuaW1wb3J0IHdhcm5pbmdzXG5cbm5wLnJhbmRvbS5zZWVkKDcpXG5uID0gMzAwXG5cbmFyMSA9IG5wLnplcm9zKG4pXG5mb3IgdCBpbiByYW5nZSgxLCBuKTpcbiAgICBhcjFbdF0gPSAwLjUgKiBhcjFbdC0xXSArIG5wLnJhbmRvbS5yYW5kbigpXG5cbnJ3ID0gbnAuY3Vtc3VtKG5wLnJhbmRvbS5yYW5kbihuKSlcbnRyZW5kX3N0YXQgPSBucC5saW5zcGFjZSgwLCA2LCBuKSArIDAuNSAqIG5wLnJhbmRvbS5yYW5kbihuKVxuXG5wcmludChmXCJ7XHUwMDI3U2VyaWVzXHUwMDI3OjIyc30ge1x1MDAyN0FERi1wXHUwMDI3OjdzfSB7XHUwMDI3QURGIHZlcmRpY3RcdTAwMjc6MTJzfSB7XHUwMDI3S1BTUy1wXHUwMDI3OjhzfSB7XHUwMDI3S1BTUyB2ZXJkaWN0XHUwMDI3OjE0c31cIilcbnByaW50KFwiLVwiICogNjgpXG5cbmZvciBsYWJlbCwgeSBpbiBbKFwiQVIoMSkgcGhpPTAuNVwiLCBhcjEpLCAoXCJSYW5kb20gV2Fsa1wiLCBydyksIChcIlRyZW5kLXN0YXRpb25hcnlcIiwgdHJlbmRfc3RhdCldOlxuICAgIGFkZl9wID0gYWRmdWxsZXIoeSwgYXV0b2xhZz1cdTAwMjdBSUNcdTAwMjcpWzFdXG4gICAgd2l0aCB3YXJuaW5ncy5jYXRjaF93YXJuaW5ncygpOlxuICAgICAgICB3YXJuaW5ncy5zaW1wbGVmaWx0ZXIoXCJpZ25vcmVcIilcbiAgICAgICAga3Bzc19wID0ga3Bzcyh5LCByZWdyZXNzaW9uPVx1MDAyN2NcdTAwMjcsIG5sYWdzPVx1MDAyN2F1dG9cdTAwMjcpWzFdXG4gICAgYWRmX3YgID0gXCJzdGF0aW9uYXJ5XCIgICAgIGlmIGFkZl9wICBcdTAwM2MgMC4wNSBlbHNlIFwibm9uLXN0YXRpb25hcnlcIlxuICAgIGtwc3NfdiA9IFwic3RhdGlvbmFyeVwiICAgICBpZiBrcHNzX3AgXHUwMDNlIDAuMDUgZWxzZSBcIm5vbi1zdGF0aW9uYXJ5XCJcbiAgICBwcmludChmXCJ7bGFiZWw6MjJzfSB7YWRmX3A6Ny4zZn0ge2FkZl92OjEyc30ge2twc3NfcDo4LjNmfSB7a3Bzc192OjE0c31cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEaWZmZXJlbmNpbmcgYW5kIExvZyBUcmFuc2Zvcm1hdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmlyc3QgZGlmZmVyZW5jaW5nIM6UeeKCnCA9IHnigpwg4oiSIHnigpzigovigoEgcmVtb3ZlcyBhIHNpbmdsZSBzdG9jaGFzdGljIHRyZW5kICh1bml0IHJvb3QpLiBUaGUgZCBwYXJhbWV0ZXIgaW4gQVJJTUEocCxkLHEpIGNvdW50cyBob3cgbWFueSBkaWZmZXJlbmNlcyBhcmUgbmVlZGVkIGZvciBzdGF0aW9uYXJpdHkg4oCUIHR5cGljYWxseSBkID0gMCwgMSwgb3IgMi4gT3Zlci1kaWZmZXJlbmNpbmcgaW50cm9kdWNlcyB1bm5lY2Vzc2FyeSBNQSBzdHJ1Y3R1cmUgKG92ZXItZGlmZmVyZW5jZWQgc2VyaWVzIGhhcyBBQ0Ygc3Bpa2UgYXQgbGFnIDEpLiBGb3Igc2VyaWVzIHdpdGggbXVsdGlwbGljYXRpdmUgc2Vhc29uYWxpdHkgb3IgZXhwb25lbnRpYWwgZ3Jvd3RoLCB0aGUgbG9nIHRyYW5zZm9ybWF0aW9uIGNvbnZlcnRzIG11bHRpcGxpY2F0aXZlIHN0cnVjdHVyZSB0byBhZGRpdGl2ZSwgYW5kIHRoZSBkaWZmZXJlbmNlZCBsb2cgaXMgdGhlIGNvbnRpbnVvdXNseSBjb21wb3VuZGVkIHJldHVybi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0dG9vbHMgaW1wb3J0IGFkZnVsbGVyXG5pbXBvcnQgd2FybmluZ3NcblxubnAucmFuZG9tLnNlZWQoNDIpXG5uID0gMjAwXG5cbiMgU3RvY2hhc3RpYyB0cmVuZDogcmFuZG9tIHdhbGtcbnJ3ID0gbnAuY3Vtc3VtKG5wLnJhbmRvbS5yYW5kbihuKSlcbmRpZmYxID0gbnAuZGlmZihydylcblxuIyBNdWx0aXBsaWNhdGl2ZSBzZXJpZXM6IGV4cG9uZW50aWFsIHRyZW5kICsgc2Vhc29uYWwgcGF0dGVyblxudCA9IG5wLmFyYW5nZShuKVxueV9tdWx0ID0gMTAuMCAqIG5wLmV4cCgwLjAxNSAqIHQgKyAwLjMgKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDEyKSArIDAuMSAqIG5wLnJhbmRvbS5yYW5kbihuKSlcbmxvZ195ICAgID0gbnAubG9nKHlfbXVsdClcbmxvZ19kaWZmID0gbnAuZGlmZihsb2dfeSlcblxuZGVmIGFkZl9wKHgpOlxuICAgIHdpdGggd2FybmluZ3MuY2F0Y2hfd2FybmluZ3MoKTpcbiAgICAgICAgd2FybmluZ3Muc2ltcGxlZmlsdGVyKFwiaWdub3JlXCIpXG4gICAgICAgIHJldHVybiBhZGZ1bGxlcih4LCBhdXRvbGFnPVx1MDAyN0FJQ1x1MDAyNylbMV1cblxucmVzdWx0cyA9IFtcbiAgICAoXCJSYW5kb20gd2Fsa1wiLCAgICAgICAgICAgICAgcncpLFxuICAgIChcIkZpcnN0LWRpZmZlcmVuY2VkIFJXXCIsICAgICBkaWZmMSksXG4gICAgKFwiTXVsdGlwbGljYXRpdmUgc2VyaWVzXCIsICAgIHlfbXVsdCksXG4gICAgKFwibG9nKHkpXCIsICAgICAgICAgICAgICAgICAgIGxvZ195KSxcbiAgICAoXCJkaWZmKGxvZyh5KSlcIiwgICAgICAgICAgICAgbG9nX2RpZmYpLFxuXVxucHJpbnQoZlwie1x1MDAyN1Nlcmllc1x1MDAyNzoyNnN9ICB7XHUwMDI3QURGIHBcdTAwMjc6OHN9ICB7XHUwMDI3RGVjaXNpb25cdTAwMjd9XCIpXG5wcmludChcIi1cIiAqIDU1KVxuZm9yIGxhYmVsLCB5IGluIHJlc3VsdHM6XG4gICAgcCA9IGFkZl9wKHkpXG4gICAgZGVjID0gXCJzdGF0aW9uYXJ5XCIgaWYgcCBcdTAwM2MgMC4wNSBlbHNlIFwiTk9OLVNUQVRJT05BUllcIlxuICAgIHByaW50KGZcIntsYWJlbDoyNnN9ICB7cDouNGZ9ICAgIHtkZWN9XCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJDaG9vc2luZyB0aGUgTnVtYmVyIG9mIERpZmZlcmVuY2VzIiwiY29udGVudCI6IkFwcGx5IHRoZSBBREYgdGVzdCBhZnRlciBlYWNoIGRpZmZlcmVuY2UuIFN0b3AgZGlmZmVyZW5jaW5nIHdoZW4gdGhlIHNlcmllcyBpcyBzdGF0aW9uYXJ5IChBREYgcCBcdTAwM2MgMC4wNSkuIE92ZXItZGlmZmVyZW5jaW5nIChkIHRvbyBsYXJnZSkgaW50cm9kdWNlcyBhbiBpbnZlcnRpYmxlIE1BIHVuaXQgcm9vdCwgaW5mbGF0ZXMgZm9yZWNhc3QgdmFyaWFuY2UsIGFuZCBpcyBkZXRlY3RhYmxlIGJ5IGEgbGFyZ2UgbmVnYXRpdmUgQUNGIHNwaWtlIGF0IGxhZyAxLiBJZiBBREYgYmFyZWx5IHJlamVjdHMgYXQgcCDiiYggMC4wNCwgY2hlY2sgS1BTUyBmb3IgY29uZmlybWF0aW9uIGJlZm9yZSBhc3N1bWluZyBkIGlzIHN1ZmZpY2llbnQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2Vhc29uYWwgVW5pdCBSb290cyBhbmQgdGhlIEhFR1kgVGVzdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9udGhseSBvciBxdWFydGVybHkgZGF0YSBtYXkgaGF2ZSBzZWFzb25hbCB1bml0IHJvb3RzIGF0IGZyZXF1ZW5jaWVzIG90aGVyIHRoYW4gemVyby4gVGhlIEhFR1kgKEh5bGxlYmVyZy1FbmdsZS1HcmFuZ2VyLVlvbykgdGVzdCBkZWNvbXBvc2VzIHRoZSBzZWFzb25hbCBkaWZmZXJlbmNpbmcgb3BlcmF0b3IgKDEg4oiSIELLoikgaW50byB1bml0IHJvb3RzIGF0IGVhY2ggc2Vhc29uYWwgZnJlcXVlbmN5LiBGb3IgbW9udGhseSBkYXRhIChTID0gMTIpLCB0aGVyZSBhcmUgdW5pdCByb290cyBhdCBmcmVxdWVuY2llcyAwLCDPgC82LCDPgC8zLCDPgC8yLCAyz4AvMywgNc+ALzYsIGFuZCDPgC4gU2Vhc29uYWwgZGlmZmVyZW5jaW5nIM6U4oKbeeKCnCA9IHnigpwg4oiSIHnigpzigovigpsgcmVtb3ZlcyBhbGwgc2Vhc29uYWwgdW5pdCByb290cyBzaW11bHRhbmVvdXNseSwgYnV0IHRoaXMgbWF5IG92ZXItZGlmZmVyZW5jZSBpZiBvbmx5IHNvbWUgc2Vhc29uYWwgZnJlcXVlbmNpZXMgYXJlIG5vbi1zdGF0aW9uYXJ5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuaXQgUm9vdCBUZXN0IENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVGVzdCIsIk51bGwgSHlwb3RoZXNpcyIsIkFsdGVybmF0aXZlIiwiV2hlbiB0byBVc2UiLCJLZXkgTGltaXRhdGlvbiJdLCJyb3dzIjpbWyJBREYgKEF1Z21lbnRlZCBEaWNrZXktRnVsbGVyKSIsIlVuaXQgcm9vdCAobm9uLXN0YXRpb25hcnkpIiwiU3RhdGlvbmFyeSAofM+BfFx1MDAzYzEpIiwiRGVmYXVsdCBmaXJzdCB0ZXN0OyBoYW5kbGVzIHNlcmlhbCBjb3JyZWxhdGlvbiB2aWEgbGFncyIsIkxvdyBwb3dlciBmb3IgbmVhci11bml0LXJvb3QgKM+BPTAuOTcpOyBsYWcgc2VsZWN0aW9uIG1hdHRlcnMiXSxbIktQU1MiLCJMZXZlbC90cmVuZCBzdGF0aW9uYXJ5IiwiVW5pdCByb290IiwiQ29tcGxlbWVudCB0byBBREY7IGNvbmZpcm1zIHN0YXRpb25hcml0eSIsIlNlbnNpdGl2ZSB0byBsYWcgdHJ1bmNhdGlvbjsgY2FuIG92ZXItcmVqZWN0IGZvciBwZXJzaXN0ZW50IHNlcmllcyJdLFsiUFAgKFBoaWxsaXBzLVBlcnJvbikiLCJVbml0IHJvb3QiLCJTdGF0aW9uYXJ5IiwiTm9uLXBhcmFtZXRyaWMgY29ycmVjdGlvbiBmb3Igc2VyaWFsIGNvcnJlbGF0aW9uOyBubyBsYWdzIG5lZWRlZCIsIlBvb3Igc21hbGwtc2FtcGxlIHByb3BlcnRpZXM7IHNpemUgZGlzdG9ydGlvbnMgd2l0aCBoZXRlcm9zY2VkYXN0aWMgZXJyb3JzIl0sWyJIRUdZIiwiU2Vhc29uYWwgdW5pdCByb290IGF0IGVhY2ggZnJlcXVlbmN5IiwiU3RhdGlvbmFyeSBhdCB0aGF0IGZyZXF1ZW5jeSIsIlRlc3Rpbmcgc3BlY2lmaWMgc2Vhc29uYWwgZnJlcXVlbmNpZXMgc2VwYXJhdGVseSIsIlJlcXVpcmVzIHNwZWNpZnlpbmcgc2Vhc29uYWwgcGVyaW9kIFM7IGNvbXBsaWNhdGVkIGZvciBoaWdoLWZyZXF1ZW5jeSBkYXRhIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFsd2F5cyB0ZXN0IEFERiArIEtQU1MgdG9nZXRoZXIg4oCUIGFncmVlbWVudCBiZXR3ZWVuIHRoZSB0d28gaXMgbXVjaCBzdHJvbmdlciBldmlkZW5jZSB0aGFuIGVpdGhlciBhbG9uZS4iLCJDaGVjayByZXNpZHVhbCBwbG90cyBhbmQgQUNGIG9mIHRoZSBkaWZmZXJlbmNlZCBzZXJpZXMgdG8gY29uZmlybSB3aGl0ZSBub2lzZSBiZWZvcmUgcHJvY2VlZGluZy4iLCJGb3IgbG9uZyBzZXJpZXMgKG4gXHUwMDNlIDUwMCkgQURGIGhhcyBoaWdoIHBvd2VyOyBmb3Igc2hvcnQgc2VyaWVzIChuIFx1MDAzYyAxMDApIGNvbnNpZGVyIFBQIG9yIGNvbmZpcm0gdmlzdWFsbHkuIiwiVGhlIHJlZ3Jlc3Npb24gdHlwZSAoY29uc3RhbnQsIGNvbnN0YW50K3RyZW5kLCBub25lKSBpbiBBREYgbXVzdCBtYXRjaCB0aGUgdHJ1ZSBkYXRhLWdlbmVyYXRpbmcgcHJvY2Vzcy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Stationarity — Unit Root Tests (ADF, KPSS)

Stationarity is the cornerstone assumption of classical time-series modelling. A stationary process has statistical properties that do not change over time, allowing models to exploit past patterns to forecast the future. Non-stationary series — those with trends, unit roots, or time-varying variance — violate the assumptions behind ARIMA, autocorrelation estimation, and most hypothesis tests. Before fitting any model, diagnosing and correcting non-stationarity is mandatory.

## Strict and Weak Stationarity

Strict (strong) stationarity requires that the entire joint distribution of (yₜ₁, yₜ₂, …, yₜₖ) is identical to (yₜ₁₊τ, yₜ₂₊τ, …, yₜₖ₊τ) for all lags τ and all k. This is a very strong condition that is rarely verifiable empirically. Weak (covariance) stationarity requires only two conditions: a constant mean E[yₜ] = μ for all t, and an autocovariance Cov(yₜ, yₜ₊ₖ) = γ(k) that depends only on lag k, not on time t.

Weak stationarity implies that the variance Var(yₜ) = γ(0) is also constant. Strict stationarity with finite second moments implies weak stationarity, but not vice versa — a t-distribution process can be weakly stationary without being strictly stationary. For practical forecasting, weak stationarity is sufficient and is what ARIMA models require after d differences.

## Why Stationarity Matters for Forecasting

ARIMA forecasting relies on autocovariances that are stable across time. If γ(k) changes with t, the autocorrelation function estimated from historical data does not apply to the future. Spurious regression is another danger: regressing two independent random walks on each other yields R² close to 1 and significant t-statistics purely by chance, because both share a common stochastic trend.

- ARIMA models require stationarity after d differences — the d parameter is the number of unit roots.
- Autocorrelation estimates γ̂(k) are inconsistent for non-stationary series — they do not converge to true values.
- Spurious regression: two independent random walks may appear correlated (t-stat significant, R²≈1) with no real relationship.
- Granger causality tests and VAR models require all variables to be stationary or co-integrated.
- Prediction intervals grow correctly only when the differenced series is stationary.

## Unit Root — The Random Walk

The simplest non-stationary process is the random walk yₜ = yₜ₋₁ + εₜ, which is an AR(1) with coefficient ρ = 1. The characteristic root equals 1 (the unit circle root). Variance grows linearly: Var(yₜ) = t·σ², so the process drifts without bound. More generally, yₜ = ρyₜ₋₁ + εₜ is stationary when |ρ| < 1 (roots of 1 − ρB = 0 lie outside the unit circle) and non-stationary when ρ = 1.

```python
import numpy as np
from statsmodels.tsa.stattools import adfuller

np.random.seed(42)
n = 300

# Stationary AR(1) with |phi| < 1
phi = 0.7
eps = np.random.randn(n)
y_ar = np.zeros(n)
for t in range(1, n):
    y_ar[t] = phi * y_ar[t-1] + eps[t]

# Non-stationary: unit-root random walk (phi = 1)
y_rw = np.cumsum(np.random.randn(n))

# Compare variance growth
for half in [75, 150, 225, 300]:
    std_ar = y_ar[:half].std()
    std_rw = y_rw[:half].std()
    print(f"n={half:3d}  AR(1) std={std_ar:.3f}  RW std={std_rw:.3f}")

adf_ar = adfuller(y_ar, autolag='AIC')[1]
adf_rw = adfuller(y_rw, autolag='AIC')[1]
print(f"\nADF p: AR(1)={adf_ar:.4f} (stationary)  RW={adf_rw:.4f} (non-stationary)")
print("AR(1) std stays bounded; RW std grows — key diagnostic difference")
```

## Augmented Dickey-Fuller (ADF) Test

The ADF test regresses Δyₜ on yₜ₋₁ and lagged differences Δyₜ₋₁, …, Δyₜ₋ₖ to remove serial correlation from residuals. The t-statistic on the yₜ₋₁ coefficient tests H₀: ρ = 1 (unit root, non-stationary) against H₁: ρ < 1 (stationary). Critical values are non-standard (more negative than normal t-distribution) because the test statistic is not asymptotically normal under H₀. Rejecting H₀ at the 5% level means the series is stationary.

```python
import numpy as np
from statsmodels.tsa.stattools import adfuller

np.random.seed(0)
n = 250

y_stat = np.zeros(n)
for t in range(1, n):
    y_stat[t] = 0.6 * y_stat[t-1] + np.random.randn()

y_rw = np.cumsum(np.random.randn(n))

def adf_report(series, label, regression='c'):
    stat, p, lags, nobs, crit, _ = adfuller(series, autolag='AIC', regression=regression)
    decision = "STATIONARY" if p < 0.05 else "NON-STATIONARY"
    print(f"\n{label}")
    print(f"  ADF statistic = {stat:.4f}")
    print(f"  p-value       = {p:.4f}  => {decision}")
    print(f"  Lags used     = {lags}")
    print(f"  Critical vals: 1%={crit['1%']:.3f}  5%={crit['5%']:.3f}  10%={crit['10%']:.3f}")

adf_report(y_stat, "AR(1) phi=0.6  [expect: STATIONARY]")
adf_report(y_rw,   "Random Walk    [expect: NON-STATIONARY]")
adf_report(y_rw,   "Random Walk (with trend regression)", regression='ct')
```

## KPSS Test and Reconciling with ADF

The KPSS (Kwiatkowski-Phillips-Schmidt-Shin) test has the opposite null hypothesis: H₀: the series is stationary (level or trend-stationary). Rejecting H₀ means the series has a unit root. Using ADF and KPSS together resolves ambiguity: if ADF rejects H₀ (stationary) and KPSS does not reject (stationary), both tests agree the series is stationary. If both tests reject their respective nulls, the evidence points to non-stationarity. Disagreement suggests possible trend-stationarity or near-unit-root behaviour.

```python
import numpy as np
from statsmodels.tsa.stattools import adfuller, kpss
import warnings

np.random.seed(7)
n = 300

ar1 = np.zeros(n)
for t in range(1, n):
    ar1[t] = 0.5 * ar1[t-1] + np.random.randn()

rw = np.cumsum(np.random.randn(n))
trend_stat = np.linspace(0, 6, n) + 0.5 * np.random.randn(n)

print(f"{'Series':22s} {'ADF-p':7s} {'ADF verdict':12s} {'KPSS-p':8s} {'KPSS verdict':14s}")
print("-" * 68)

for label, y in [("AR(1) phi=0.5", ar1), ("Random Walk", rw), ("Trend-stationary", trend_stat)]:
    adf_p = adfuller(y, autolag='AIC')[1]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        kpss_p = kpss(y, regression='c', nlags='auto')[1]
    adf_v  = "stationary"     if adf_p  < 0.05 else "non-stationary"
    kpss_v = "stationary"     if kpss_p > 0.05 else "non-stationary"
    print(f"{label:22s} {adf_p:7.3f} {adf_v:12s} {kpss_p:8.3f} {kpss_v:14s}")
```

## Differencing and Log Transformation

First differencing Δyₜ = yₜ − yₜ₋₁ removes a single stochastic trend (unit root). The d parameter in ARIMA(p,d,q) counts how many differences are needed for stationarity — typically d = 0, 1, or 2. Over-differencing introduces unnecessary MA structure (over-differenced series has ACF spike at lag 1). For series with multiplicative seasonality or exponential growth, the log transformation converts multiplicative structure to additive, and the differenced log is the continuously compounded return.

```python
import numpy as np
from statsmodels.tsa.stattools import adfuller
import warnings

np.random.seed(42)
n = 200

# Stochastic trend: random walk
rw = np.cumsum(np.random.randn(n))
diff1 = np.diff(rw)

# Multiplicative series: exponential trend + seasonal pattern
t = np.arange(n)
y_mult = 10.0 * np.exp(0.015 * t + 0.3 * np.sin(2 * np.pi * t / 12) + 0.1 * np.random.randn(n))
log_y    = np.log(y_mult)
log_diff = np.diff(log_y)

def adf_p(x):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return adfuller(x, autolag='AIC')[1]

results = [
    ("Random walk",              rw),
    ("First-differenced RW",     diff1),
    ("Multiplicative series",    y_mult),
    ("log(y)",                   log_y),
    ("diff(log(y))",             log_diff),
]
print(f"{'Series':26s}  {'ADF p':8s}  {'Decision'}")
print("-" * 55)
for label, y in results:
    p = adf_p(y)
    dec = "stationary" if p < 0.05 else "NON-STATIONARY"
    print(f"{label:26s}  {p:.4f}    {dec}")
```

> **Choosing the Number of Differences**: Apply the ADF test after each difference. Stop differencing when the series is stationary (ADF p < 0.05). Over-differencing (d too large) introduces an invertible MA unit root, inflates forecast variance, and is detectable by a large negative ACF spike at lag 1. If ADF barely rejects at p ≈ 0.04, check KPSS for confirmation before assuming d is sufficient.

## Seasonal Unit Roots and the HEGY Test

Monthly or quarterly data may have seasonal unit roots at frequencies other than zero. The HEGY (Hylleberg-Engle-Granger-Yoo) test decomposes the seasonal differencing operator (1 − Bˢ) into unit roots at each seasonal frequency. For monthly data (S = 12), there are unit roots at frequencies 0, π/6, π/3, π/2, 2π/3, 5π/6, and π. Seasonal differencing Δₛyₜ = yₜ − yₜ₋ₛ removes all seasonal unit roots simultaneously, but this may over-difference if only some seasonal frequencies are non-stationary.

## Unit Root Test Comparison

| Test | Null Hypothesis | Alternative | When to Use | Key Limitation |
| --- | --- | --- | --- | --- |
| ADF (Augmented Dickey-Fuller) | Unit root (non-stationary) | Stationary (|ρ|<1) | Default first test; handles serial correlation via lags | Low power for near-unit-root (ρ=0.97); lag selection matters |
| KPSS | Level/trend stationary | Unit root | Complement to ADF; confirms stationarity | Sensitive to lag truncation; can over-reject for persistent series |
| PP (Phillips-Perron) | Unit root | Stationary | Non-parametric correction for serial correlation; no lags needed | Poor small-sample properties; size distortions with heteroscedastic errors |
| HEGY | Seasonal unit root at each frequency | Stationary at that frequency | Testing specific seasonal frequencies separately | Requires specifying seasonal period S; complicated for high-frequency data |

- Always test ADF + KPSS together — agreement between the two is much stronger evidence than either alone.
- Check residual plots and ACF of the differenced series to confirm white noise before proceeding.
- For long series (n > 500) ADF has high power; for short series (n < 100) consider PP or confirm visually.
- The regression type (constant, constant+trend, none) in ADF must match the true data-generating process.

---

