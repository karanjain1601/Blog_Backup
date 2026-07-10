---
title: "PPO for RLHF — Policy Optimization with Reward Model and KL Penalty"
slug: "ppo-rlhf"
description: "Deep dive into PPO-RLHF: four-model architecture, per-token KL penalty, clipped surrogate objective, GAE advantage estimation, and the rollout training loop from InstructGPT."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUFBPLVJMSEYgKFByb3hpbWFsIFBvbGljeSBPcHRpbWl6YXRpb24gZm9yIFJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBIdW1hbiBGZWVkYmFjaykgaXMgdGhlIHRyYWluaW5nIGFsZ29yaXRobSBiZWhpbmQgSW5zdHJ1Y3RHUFQgYW5kIGVhcmx5IENoYXRHUFQuIEl0IGZpbmUtdHVuZXMgYSBsYW5ndWFnZSBtb2RlbCB1c2luZyBodW1hbiBwcmVmZXJlbmNlIHNpZ25hbHMgYnkgZm9ybXVsYXRpbmcgYWxpZ25tZW50IGFzIGEgcmVpbmZvcmNlbWVudCBsZWFybmluZyBwcm9ibGVtIG92ZXIgdG9rZW4gc2VxdWVuY2VzLiBUaGUga2V5IGluc2lnaHQgaXMgdG8gbWF4aW1pemUgZXhwZWN0ZWQgcmV3YXJkIHdoaWxlIHByZXZlbnRpbmcgdGhlIHBvbGljeSBmcm9tIGRldmlhdGluZyB0b28gZmFyIGZyb20gYSBzdXBlcnZpc2VkIGZpbmUtdHVuZWQgYmFzZWxpbmUgdXNpbmcgYSBLTCBkaXZlcmdlbmNlIHBlbmFsdHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEZvdXIgTW9kZWxzIGluIFBQTy1STEhGIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3VyIGRpc3RpbmN0IG5ldXJhbCBuZXR3b3JrcyBvcGVyYXRlIHNpbXVsdGFuZW91c2x5IGR1cmluZyBQUE8tUkxIRiB0cmFpbmluZywgZWFjaCB3aXRoIGEgc3BlY2lmaWMgcm9sZS4gQXQgN0IgcGFyYW1ldGVyIHNjYWxlLCB0aGlzIHJlcXVpcmVzIHJvdWdobHkgNHggdGhlIEdQVSBtZW1vcnkgb2YgaW5mZXJlbmNlIGFsb25lLCBtYWtpbmcgbXVsdGktR1BVIHNldHVwcyBvciBMb1JBIGFkYXB0ZXJzIG9uIHRoZSBwb2xpY3kgYW5kIHZhbHVlIGhlYWRzIGEgcHJhY3RpY2FsIG5lY2Vzc2l0eS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlBvbGljeSBwaV90aGV0YTogdGhlIExMTSBiZWluZyB0cmFpbmVkLCBpbml0aWFsaXplZCBmcm9tIHRoZSBTRlQgY2hlY2twb2ludCwgdXBkYXRlZCBieSBQUE8gZ3JhZGllbnRzIGVhY2ggaXRlcmF0aW9uIiwiUmVmZXJlbmNlIHBvbGljeSBwaV9yZWY6IGZyb3plbiBjb3B5IG9mIHRoZSBTRlQgbW9kZWwsIHByb3ZpZGVzIHRoZSBLTCBhbmNob3IgdGhhdCBwcmV2ZW50cyByZXdhcmQgaGFja2luZyBhbmQgZGVnZW5lcmF0ZSBvdXRwdXRzIiwiUmV3YXJkIG1vZGVsIHJfcGhpOiB0cmFpbmVkIG9uIGh1bWFuIHByZWZlcmVuY2UgY29tcGFyaXNvbnMsIHNjb3JlcyAocHJvbXB0LCBjb21wbGV0aW9uKSBwYWlycyB3aXRoIGEgc2NhbGFyIHJld2FyZCBzaWduYWwiLCJWYWx1ZSBtb2RlbCBWX3BzaTogcHJlZGljdHMgZXhwZWN0ZWQgZnV0dXJlIHJldHVybiBmcm9tIGVhY2ggdG9rZW4gcG9zaXRpb24sIHVzZWQgZm9yIEdBRSBhZHZhbnRhZ2UgZXN0aW1hdGlvbiBkdXJpbmcgUFBPIHVwZGF0ZXMiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT2JqZWN0aXZlIEZ1bmN0aW9uIGFuZCBLTCBQZW5hbHR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgUkxIRiBvYmplY3RpdmUgbWF4aW1pemVzIEVbcih4LHkpXSAtIGJldGEgKiBLTFtwaV90aGV0YSB8fCBwaV9yZWZdLCB3aGVyZSByKHgseSkgaXMgdGhlIHJld2FyZCBtb2RlbCBzY29yZSwgYmV0YSBjb250cm9scyB0aGUgS0wgcGVuYWx0eSBzdHJlbmd0aCwgcGlfdGhldGEgaXMgdGhlIHBvbGljeSBiZWluZyB0cmFpbmVkLCBhbmQgcGlfcmVmIGlzIHRoZSBmcm96ZW4gU0ZUIHJlZmVyZW5jZS4gVGhlIEtMIHRlcm0gcHJldmVudHMgdGhlIHBvbGljeSBmcm9tIGV4cGxvaXRpbmcgcmV3YXJkIG1vZGVsIHdlYWtuZXNzZXMgYnkgY29uc3RyYWluaW5nIGl0IHRvIHN0YXkgY2xvc2UgdG8gaHVtYW4tbGlrZSBvdXRwdXRzLiBJbnN0cnVjdEdQVCBzdGFydHMgd2l0aCBiZXRhPTAuMDIgYW5kIHVzZXMgYW4gYWRhcHRpdmUgY29udHJvbGxlciB0YXJnZXRpbmcgNiBuYXRzIG9mIGRpdmVyZ2VuY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGVyLVRva2VuIEtMIGFuZCBTaGFwZWQgUmV3YXJkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQUE8tUkxIRiBhcHBsaWVzIGEgcGVyLXRva2VuIEtMIHBlbmFsdHkgYXQgZWFjaCBwb3NpdGlvbiB0OiBLTF90ID0gbG9nIHBpX3RoZXRhKGFfdHxzX3QpIC0gbG9nIHBpX3JlZihhX3R8c190KS4gVGhlIHNoYXBlZCByZXdhcmQgc2lnbmFsIGlzIFJfdCA9IHIoeCx5KSAqIDFbdD1UXSAtIGJldGEgKiBLTF90IOKAlCB0aGUgdGVybWluYWwgcmV3YXJkIG1vZGVsIHNjb3JlIG1pbnVzIG9uZ29pbmcgS0wgcGVuYWx0aWVzIGF0IGV2ZXJ5IHRva2VuIHBvc2l0aW9uLiBUaGlzIGRlbnNlIHJld2FyZCBzaWduYWwgc3BlZWRzIHVwIGNyZWRpdCBhc3NpZ25tZW50IGNvbXBhcmVkIHRvIGEgcHVyZWx5IHRlcm1pbmFsIHJld2FyZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHR5cGluZyBpbXBvcnQgVHVwbGVcblxuZGVmIGNvbXB1dGVfcHBvX3JsaGZfcmV3YXJkKFxuICAgIHBvbGljeV9sb2dwcm9iczogdG9yY2guVGVuc29yLFxuICAgIHJlZl9sb2dwcm9iczogdG9yY2guVGVuc29yLFxuICAgIHJtX3Njb3JlczogdG9yY2guVGVuc29yLFxuICAgIGJldGE6IGZsb2F0ID0gMC4xLFxuICAgIHJlc3BvbnNlX21hc2s6IHRvcmNoLlRlbnNvciA9IE5vbmUsXG4pIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICMgUGVyLXRva2VuIEtMOiBLTF90ID0gbG9nIHBpX3RoZXRhKGFfdCkgLSBsb2cgcGlfcmVmKGFfdClcbiAgICBwZXJfdG9rZW5fa2wgPSBwb2xpY3lfbG9ncHJvYnMgLSByZWZfbG9ncHJvYnMgICMgW2JhdGNoLCBzZXFfbGVuXVxuICAgICMgSW5pdGlhbGl6ZSByZXdhcmQgdGVuc29yIHdpdGggS0wgcGVuYWx0eSBhdCBldmVyeSB0b2tlbiBwb3NpdGlvblxuICAgIHJld2FyZHMgPSAtYmV0YSAqIHBlcl90b2tlbl9rbCAgIyBbYmF0Y2gsIHNlcV9sZW5dXG4gICAgIyBBZGQgdGVybWluYWwgUk0gcmV3YXJkIGF0IHRoZSBsYXN0IHJlc3BvbnNlIHRva2VuXG4gICAgaWYgcmVzcG9uc2VfbWFzayBpcyBub3QgTm9uZTpcbiAgICAgICAgbGFzdF90b2tlbl9pZHggPSByZXNwb25zZV9tYXNrLnN1bShkaW09MSkubG9uZygpIC0gMVxuICAgIGVsc2U6XG4gICAgICAgIGxhc3RfdG9rZW5faWR4ID0gdG9yY2guZnVsbChcbiAgICAgICAgICAgIChyZXdhcmRzLnNpemUoMCksKSwgcmV3YXJkcy5zaXplKDEpIC0gMSwgZHR5cGU9dG9yY2gubG9uZ1xuICAgICAgICApXG4gICAgZm9yIGksIGlkeCBpbiBlbnVtZXJhdGUobGFzdF90b2tlbl9pZHgpOlxuICAgICAgICByZXdhcmRzW2ksIGlkeF0gKz0gcm1fc2NvcmVzW2ldXG4gICAgIyBaZXJvIG91dCBwYWRkaW5nIHBvc2l0aW9uc1xuICAgIGlmIHJlc3BvbnNlX21hc2sgaXMgbm90IE5vbmU6XG4gICAgICAgIHJld2FyZHMgPSByZXdhcmRzICogcmVzcG9uc2VfbWFza1xuICAgIHJldHVybiByZXdhcmRzICAjIFtiYXRjaCwgc2VxX2xlbl0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQUE8gQ2xpcHBlZCBPYmplY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBQTyB1c2VzIGEgY2xpcHBlZCBzdXJyb2dhdGUgb2JqZWN0aXZlIHRvIHByZXZlbnQgZGVzdHJ1Y3RpdmVseSBsYXJnZSBwb2xpY3kgdXBkYXRlcy4gVGhlIGltcG9ydGFuY2UgcmF0aW8gcl90ID0gcGlfdGhldGEoYV90KSAvIHBpX29sZChhX3QpIG1lYXN1cmVzIHBvbGljeSBkcmlmdCBmcm9tIHRoZSByb2xsb3V0IHBvbGljeS4gQ2xpcHBpbmcgcl90IHRvIFsxLWVwcywgMStlcHNdIGJvdW5kcyB0aGUgZ3JhZGllbnQgc3RlcC4gVGhlIExfQ0xJUCBvYmplY3RpdmUgdGFrZXMgdGhlIHBlc3NpbWlzdGljIG1pbmltdW06IG1pbihyX3QgKiBBX3QsIGNsaXAocl90LCAxLWVwcywgMStlcHMpICogQV90KSwgcHJldmVudGluZyB1cGRhdGVzIHRoYXQgZXhwbG9pdCBvdXRsaWVyIGFkdmFudGFnZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuZnJvbSB0eXBpbmcgaW1wb3J0IFR1cGxlXG5cbmRlZiBwcG9fY2xpcHBlZF9sb3NzKFxuICAgIG9sZF9sb2dwcm9iczogdG9yY2guVGVuc29yLFxuICAgIG5ld19sb2dwcm9iczogdG9yY2guVGVuc29yLFxuICAgIGFkdmFudGFnZXM6IHRvcmNoLlRlbnNvcixcbiAgICByZXNwb25zZV9tYXNrOiB0b3JjaC5UZW5zb3IsXG4gICAgY2xpcF9lcHM6IGZsb2F0ID0gMC4yLFxuKSAtXHUwMDNlIFR1cGxlW3RvcmNoLlRlbnNvciwgZGljdF06XG4gICAgIyBJbXBvcnRhbmNlIHNhbXBsaW5nIHJhdGlvOiByX3QgPSBwaV90aGV0YSAvIHBpX29sZFxuICAgIGxvZ19yYXRpbyA9IG5ld19sb2dwcm9icyAtIG9sZF9sb2dwcm9ic1xuICAgIHJhdGlvID0gbG9nX3JhdGlvLmV4cCgpICAjIFtiYXRjaCwgc2VxX2xlbl1cbiAgICAjIENsaXBwZWQgc3Vycm9nYXRlOiBtaW4ocl90ICogQV90LCBjbGlwKHJfdCwgMS1lcHMsIDErZXBzKSAqIEFfdClcbiAgICB1bmNsaXBwZWQgPSByYXRpbyAqIGFkdmFudGFnZXNcbiAgICBjbGlwcGVkID0gcmF0aW8uY2xhbXAoMSAtIGNsaXBfZXBzLCAxICsgY2xpcF9lcHMpICogYWR2YW50YWdlc1xuICAgIHBvbGljeV9sb3NzID0gLXRvcmNoLm1pbih1bmNsaXBwZWQsIGNsaXBwZWQpXG4gICAgIyBBdmVyYWdlIGxvc3Mgb3ZlciB2YWxpZCByZXNwb25zZSB0b2tlbnMgb25seVxuICAgIG1hc2tlZF9sb3NzID0gKHBvbGljeV9sb3NzICogcmVzcG9uc2VfbWFzaykuc3VtKCkgLyByZXNwb25zZV9tYXNrLnN1bSgpXG4gICAgY2xpcF9mcmFjID0gKChyYXRpbyAtIDEuMCkuYWJzKCkgXHUwMDNlIGNsaXBfZXBzKS5mbG9hdCgpLm1lYW4oKS5pdGVtKClcbiAgICBhcHByb3hfa2wgPSAobG9nX3JhdGlvICogcmVzcG9uc2VfbWFzaykuc3VtKCkgLyByZXNwb25zZV9tYXNrLnN1bSgpXG4gICAgcmV0dXJuIG1hc2tlZF9sb3NzLCB7XCJjbGlwX2ZyYWNcIjogY2xpcF9mcmFjLCBcImFwcHJveF9rbFwiOiBhcHByb3hfa2wuaXRlbSgpfSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZhbHVlIEZ1bmN0aW9uIGFuZCBHQUUgRXN0aW1hdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHZhbHVlIG1vZGVsIFZfcHNpIGVzdGltYXRlcyBleHBlY3RlZCBmdXR1cmUgcmV0dXJuIGZyb20gZWFjaCB0b2tlbiBwb3NpdGlvbiwgZW5hYmxpbmcgR2VuZXJhbGl6ZWQgQWR2YW50YWdlIEVzdGltYXRpb24gKEdBRSkuIFdpdGggbGFtYmRhPTAuOTUsIEdBRSBjb21wdXRlcyBhZHZhbnRhZ2VzIGFzIGV4cG9uZW50aWFsbHkgd2VpZ2h0ZWQgVEQgZXJyb3JzOiBBX3QgPSBzdW0oKGdhbW1hKmxhbWJkYSlebCAqIGRlbHRhX3t0K2x9KSB3aGVyZSBkZWx0YV90ID0gcl90ICsgZ2FtbWEgKiBWKHNfe3QrMX0pIC0gVihzX3QpLiBSZXR1cm5zLCB3aGljaCBzZXJ2ZSBhcyB2YWx1ZSB0cmFpbmluZyB0YXJnZXRzLCBhcmUgY29tcHV0ZWQgYXMgYWR2YW50YWdlcyBwbHVzIHZhbHVlIGVzdGltYXRlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHR5cGluZyBpbXBvcnQgVHVwbGVcblxuZGVmIGNvbXB1dGVfZ2FlX3JldHVybnMoXG4gICAgcmV3YXJkczogdG9yY2guVGVuc29yLFxuICAgIHZhbHVlczogdG9yY2guVGVuc29yLFxuICAgIHJlc3BvbnNlX21hc2s6IHRvcmNoLlRlbnNvcixcbiAgICBnYW1tYTogZmxvYXQgPSAxLjAsXG4gICAgbGFtOiBmbG9hdCA9IDAuOTUsXG4pIC1cdTAwM2UgVHVwbGVbdG9yY2guVGVuc29yLCB0b3JjaC5UZW5zb3JdOlxuICAgICMgQ29tcHV0ZSBHQUUgYWR2YW50YWdlcyBhbmQgcmV0dXJucyBmb3IgUFBPLVJMSEYgdmFsdWUgdHJhaW5pbmdcbiAgICBiYXRjaCwgc2VxX2xlbiA9IHJld2FyZHMuc2hhcGVcbiAgICBhZHZhbnRhZ2VzID0gdG9yY2guemVyb3NfbGlrZShyZXdhcmRzKVxuICAgIGxhc3RfZ2FlID0gdG9yY2guemVyb3MoYmF0Y2gsIGRldmljZT1yZXdhcmRzLmRldmljZSlcbiAgICBmb3IgdCBpbiByZXZlcnNlZChyYW5nZShzZXFfbGVuKSk6XG4gICAgICAgIG1hc2tfdCA9IHJlc3BvbnNlX21hc2tbOiwgdF1cbiAgICAgICAgaWYgdCBcdTAwM2Mgc2VxX2xlbiAtIDE6XG4gICAgICAgICAgICBuZXh0X3ZhbCA9IHZhbHVlc1s6LCB0ICsgMV1cbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIG5leHRfdmFsID0gdG9yY2guemVyb3MoYmF0Y2gsIGRldmljZT12YWx1ZXMuZGV2aWNlKVxuICAgICAgICBkZWx0YSA9IHJld2FyZHNbOiwgdF0gKyBnYW1tYSAqIG5leHRfdmFsIC0gdmFsdWVzWzosIHRdXG4gICAgICAgIGxhc3RfZ2FlID0gZGVsdGEgKyBnYW1tYSAqIGxhbSAqIGxhc3RfZ2FlXG4gICAgICAgIGFkdmFudGFnZXNbOiwgdF0gPSBsYXN0X2dhZSAqIG1hc2tfdFxuICAgICMgUmV0dXJucyA9IGFkdmFudGFnZXMgKyB2YWx1ZXMgKHRhcmdldHMgZm9yIHZhbHVlIGZ1bmN0aW9uIHRyYWluaW5nKVxuICAgIHJldHVybnMgPSBhZHZhbnRhZ2VzICsgdmFsdWVzXG4gICAgIyBOb3JtYWxpemUgYWR2YW50YWdlcyBvdmVyIHZhbGlkIHJlc3BvbnNlIHBvc2l0aW9uc1xuICAgIGFkdl9mbGF0ID0gYWR2YW50YWdlc1tyZXNwb25zZV9tYXNrLmJvb2woKV1cbiAgICBhZHZhbnRhZ2VzID0gKGFkdmFudGFnZXMgLSBhZHZfZmxhdC5tZWFuKCkpIC8gKGFkdl9mbGF0LnN0ZCgpICsgMWUtOClcbiAgICByZXR1cm4gYWR2YW50YWdlcywgcmV0dXJucyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJMSEYgUm9sbG91dCBMb29wIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFYWNoIFBQTyBpdGVyYXRpb24gYmVnaW5zIHdpdGggYSByb2xsb3V0IHBoYXNlOiBzYW1wbGUgcHJvbXB0cyBmcm9tIHRoZSBkYXRhc2V0LCBnZW5lcmF0ZSBjb21wbGV0aW9ucyB3aXRoIHRoZSBjdXJyZW50IHBvbGljeSB1c2luZyB0ZW1wZXJhdHVyZSBzYW1wbGluZywgc2NvcmUgd2l0aCB0aGUgcmV3YXJkIG1vZGVsLCBjb21wdXRlIHBlci10b2tlbiBLTCB3aXRoIHRoZSBmcm96ZW4gcmVmZXJlbmNlLCB0aGVuIHVzZSBHQUUgdG8gcHJvZHVjZSBhZHZhbnRhZ2UgZXN0aW1hdGVzLiBNdWx0aXBsZSBQUE8gZXBvY2hzIHRoZW4gdXBkYXRlIHRoZSBwb2xpY3kgYW5kIHZhbHVlIGhlYWQgdXNpbmcgbWluaS1iYXRjaGVzIGZyb20gdGhlIHJvbGxvdXQgYnVmZmVyLiBUeXBpY2FsIHNldHVwcyB1c2UgNTEyIHJvbGxvdXRzIHBlciBpdGVyYXRpb24gd2l0aCA0IFBQTyBlcG9jaHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvVG9rZW5pemVyXG5cbmRlZiBjb2xsZWN0X3JsaGZfcm9sbG91dHMoXG4gICAgcG9saWN5X21vZGVsOiBBdXRvTW9kZWxGb3JDYXVzYWxMTSxcbiAgICByZXdhcmRfbW9kZWwsXG4gICAgdG9rZW5pemVyOiBBdXRvVG9rZW5pemVyLFxuICAgIHByb21wdHM6IGxpc3QsXG4gICAgbWF4X25ld190b2tlbnM6IGludCA9IDI1NixcbiAgICBkZXZpY2U6IHN0ciA9IFwiY3VkYVwiLFxuKSAtXHUwMDNlIGRpY3Q6XG4gICAgIyBHZW5lcmF0ZSBjb21wbGV0aW9ucyBhbmQgc2NvcmUgd2l0aCByZXdhcmQgbW9kZWxcbiAgICBwb2xpY3lfbW9kZWwuZXZhbCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGlucHV0cyA9IHRva2VuaXplcihcbiAgICAgICAgICAgIHByb21wdHMsIHJldHVybl90ZW5zb3JzPVwicHRcIiwgcGFkZGluZz1UcnVlLCB0cnVuY2F0aW9uPVRydWVcbiAgICAgICAgKS50byhkZXZpY2UpXG4gICAgICAgIG91dHB1dHMgPSBwb2xpY3lfbW9kZWwuZ2VuZXJhdGUoXG4gICAgICAgICAgICAqKmlucHV0cyxcbiAgICAgICAgICAgIG1heF9uZXdfdG9rZW5zPW1heF9uZXdfdG9rZW5zLFxuICAgICAgICAgICAgZG9fc2FtcGxlPVRydWUsXG4gICAgICAgICAgICB0ZW1wZXJhdHVyZT0wLjksXG4gICAgICAgICAgICB0b3BfcD0wLjk1LFxuICAgICAgICAgICAgcmV0dXJuX2RpY3RfaW5fZ2VuZXJhdGU9VHJ1ZSxcbiAgICAgICAgKVxuICAgICAgICByZXNwb25zZV9pZHMgPSBvdXRwdXRzLnNlcXVlbmNlc1s6LCBpbnB1dHNbXCJpbnB1dF9pZHNcIl0uc2hhcGVbMV06XVxuICAgICAgICBjb21wbGV0aW9ucyA9IHRva2VuaXplci5iYXRjaF9kZWNvZGUocmVzcG9uc2VfaWRzLCBza2lwX3NwZWNpYWxfdG9rZW5zPVRydWUpXG4gICAgICAgIHJtX2lucHV0cyA9IHRva2VuaXplcihcbiAgICAgICAgICAgIHByb21wdHMsIGNvbXBsZXRpb25zLCByZXR1cm5fdGVuc29ycz1cInB0XCIsIHBhZGRpbmc9VHJ1ZVxuICAgICAgICApLnRvKGRldmljZSlcbiAgICAgICAgcm1fc2NvcmVzID0gcmV3YXJkX21vZGVsKCoqcm1faW5wdXRzKS5sb2dpdHMuc3F1ZWV6ZSgtMSlcbiAgICByZXR1cm4ge1wiY29tcGxldGlvbnNcIjogY29tcGxldGlvbnMsIFwicm1fc2NvcmVzXCI6IHJtX3Njb3JlcywgXCJyZXNwb25zZV9pZHNcIjogcmVzcG9uc2VfaWRzfSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBQTyBIeXBlcnBhcmFtZXRlcnMgZm9yIFJMSEYifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiSHlwZXJwYXJhbWV0ZXIiLCJTeW1ib2wiLCJJbnN0cnVjdEdQVCBWYWx1ZSIsIkVmZmVjdCBvZiBJbmNyZWFzaW5nIl0sInJvd3MiOltbIktMIGNvZWZmaWNpZW50IiwiYmV0YSIsIjAuMDIgKGFkYXB0aXZlKSIsIlN0cm9uZ2VyIGRyaWZ0IHBlbmFsdHksIHNsb3dlciBsZWFybmluZywgbGVzcyByZXdhcmQgaGFja2luZyJdLFsiQ2xpcCBlcHNpbG9uIiwiZXBzIiwiMC4yIiwiV2lkZXIgdHJ1c3QgcmVnaW9uLCBub2lzaWVyIHVwZGF0ZXMsIGhpZ2hlciBjbGlwIGZyYWN0aW9uIl0sWyJHQUUgbGFtYmRhIiwibGFtYmRhIiwiMC45NSIsIk1vcmUgYmlhcywgbGVzcyB2YXJpYW5jZSBpbiBhZHZhbnRhZ2UgZXN0aW1hdGVzIl0sWyJSb2xsb3V0IGJhdGNoIHNpemUiLCJCIiwiNTEyIHNlcXVlbmNlcyIsIk1vcmUgZGl2ZXJzZSBleHBlcmllbmNlLCBzbG93ZXIgcGVyLWl0ZXJhdGlvbiB3YWxsIHRpbWUiXSxbIlBQTyBtaW5pLWJhdGNoIHNpemUiLCJNIiwiNjQgc2VxdWVuY2VzIiwiTm9pc2llciBncmFkaWVudHMgYnV0IGZhc3RlciBzdGVwcyBwZXIgcm9sbG91dCBidWZmZXIiXSxbIlBQTyBlcG9jaHMgcGVyIHJvbGxvdXQiLCJFIiwiNCIsIk1vcmUgZ3JhZGllbnQgcmV1c2UgcGVyIHJvbGxvdXQsIHJpc2sgb2Ygb3ZlcmZpdCB0byBzdGFsZSBhZHZhbnRhZ2VzIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBLTCBjb2VmZmljaWVudCBiZXRhIGlzIHRoZSBtb3N0IHNlbnNpdGl2ZSBoeXBlcnBhcmFtZXRlciBpbiBQUE8tUkxIRi4gVG9vIHNtYWxsIGFuZCB0aGUgcG9saWN5IHJld2FyZCBoYWNrczsgdG9vIGxhcmdlIGFuZCBsZWFybmluZyBzdGFsbHMuIEluc3RydWN0R1BUIHVzZXMgYW4gYWRhcHRpdmUgY29udHJvbGxlciB0aGF0IGluY3JlYXNlcyBiZXRhIHdoZW4gS0wgZXhjZWVkcyB0aGUgdGFyZ2V0IGFuZCBkZWNyZWFzZXMgaXQgd2hlbiBiZWxvdywgbWFpbnRhaW5pbmcgcm91Z2hseSA2IG5hdHMgb2YgZGl2ZXJnZW5jZSB0aHJvdWdob3V0IHRyYWluaW5nLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiV2FybmluZyIsImNvbnRlbnQiOiJQUE8gZm9yIFJMSEYgcmVxdWlyZXMgNCBtb2RlbHMgc2ltdWx0YW5lb3VzbHkgaW4gR1BVIG1lbW9yeSAocG9saWN5LCByZWZlcmVuY2UsIHJld2FyZCwgdmFsdWUpIOKAlCB0eXBpY2FsIDdCIHNjYWxlIFJMSEYgbmVlZHMgNHggdGhlIG1lbW9yeSBvZiBpbmZlcmVuY2UsIHJlcXVpcmluZyBtdWx0aS1HUFUgb3IgTG9SQSBvbiBwb2xpY3kvdmFsdWUgaGVhZHMuIFdpdGggZnVsbC1wcmVjaXNpb24gN0IgbW9kZWxzIGVhY2ggcmVxdWlyaW5nIH4xNEdCIFZSQU0sIGEgc2luZ2xlIDgwR0IgQTEwMCBpcyBpbnN1ZmZpY2llbnQgZm9yIG5haXZlIGZ1bGwtcGFyYW1ldGVyIFJMSEYgYXQgdGhpcyBzY2FsZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBQTy1STEhGIHJlbWFpbnMgdGhlIGdvbGQgc3RhbmRhcmQgZm9yIGFsaWduaW5nIGxhcmdlIGxhbmd1YWdlIG1vZGVscyB3aXRoIGh1bWFuIHByZWZlcmVuY2VzIGF0IHNjYWxlLiBJdHMgZm91ci1tb2RlbCBhcmNoaXRlY3R1cmUsIHBlci10b2tlbiBLTCBwZW5hbHRpZXMsIGFuZCBjbGlwcGVkIHN1cnJvZ2F0ZSBvYmplY3RpdmUgd29yayB0b2dldGhlciB0byBwcm9kdWNlIGhlbHBmdWwgYW5kIGhhcm1sZXNzIG91dHB1dHMg4oCUIGJ1dCB0aGUgZW5naW5lZXJpbmcgY29tcGxleGl0eSBhbmQgbWVtb3J5IHJlcXVpcmVtZW50cyBoYXZlIGRyaXZlbiB0aGUgY29tbXVuaXR5IHRvd2FyZCBzaW1wbGVyIGFsdGVybmF0aXZlcyBsaWtlIERQTyBmb3Igc21hbGxlci1zY2FsZSBleHBlcmltZW50cy4ifV0="
---
# PPO for RLHF — Policy Optimization with Reward Model and KL Penalty

PPO-RLHF (Proximal Policy Optimization for Reinforcement Learning from Human Feedback) is the training algorithm behind InstructGPT and early ChatGPT. It fine-tunes a language model using human preference signals by formulating alignment as a reinforcement learning problem over token sequences. The key insight is to maximize expected reward while preventing the policy from deviating too far from a supervised fine-tuned baseline using a KL divergence penalty.

## The Four Models in PPO-RLHF

Four distinct neural networks operate simultaneously during PPO-RLHF training, each with a specific role. At 7B parameter scale, this requires roughly 4x the GPU memory of inference alone, making multi-GPU setups or LoRA adapters on the policy and value heads a practical necessity.

- Policy pi_theta: the LLM being trained, initialized from the SFT checkpoint, updated by PPO gradients each iteration
- Reference policy pi_ref: frozen copy of the SFT model, provides the KL anchor that prevents reward hacking and degenerate outputs
- Reward model r_phi: trained on human preference comparisons, scores (prompt, completion) pairs with a scalar reward signal
- Value model V_psi: predicts expected future return from each token position, used for GAE advantage estimation during PPO updates

## Objective Function and KL Penalty

The RLHF objective maximizes E[r(x,y)] - beta * KL[pi_theta || pi_ref], where r(x,y) is the reward model score, beta controls the KL penalty strength, pi_theta is the policy being trained, and pi_ref is the frozen SFT reference. The KL term prevents the policy from exploiting reward model weaknesses by constraining it to stay close to human-like outputs. InstructGPT starts with beta=0.02 and uses an adaptive controller targeting 6 nats of divergence.

## Per-Token KL and Shaped Reward

PPO-RLHF applies a per-token KL penalty at each position t: KL_t = log pi_theta(a_t|s_t) - log pi_ref(a_t|s_t). The shaped reward signal is R_t = r(x,y) * 1[t=T] - beta * KL_t — the terminal reward model score minus ongoing KL penalties at every token position. This dense reward signal speeds up credit assignment compared to a purely terminal reward.

```python
import torch
import torch.nn.functional as F
from typing import Tuple

def compute_ppo_rlhf_reward(
    policy_logprobs: torch.Tensor,
    ref_logprobs: torch.Tensor,
    rm_scores: torch.Tensor,
    beta: float = 0.1,
    response_mask: torch.Tensor = None,
) -> torch.Tensor:
    # Per-token KL: KL_t = log pi_theta(a_t) - log pi_ref(a_t)
    per_token_kl = policy_logprobs - ref_logprobs  # [batch, seq_len]
    # Initialize reward tensor with KL penalty at every token position
    rewards = -beta * per_token_kl  # [batch, seq_len]
    # Add terminal RM reward at the last response token
    if response_mask is not None:
        last_token_idx = response_mask.sum(dim=1).long() - 1
    else:
        last_token_idx = torch.full(
            (rewards.size(0),), rewards.size(1) - 1, dtype=torch.long
        )
    for i, idx in enumerate(last_token_idx):
        rewards[i, idx] += rm_scores[i]
    # Zero out padding positions
    if response_mask is not None:
        rewards = rewards * response_mask
    return rewards  # [batch, seq_len]
```

## PPO Clipped Objective

PPO uses a clipped surrogate objective to prevent destructively large policy updates. The importance ratio r_t = pi_theta(a_t) / pi_old(a_t) measures policy drift from the rollout policy. Clipping r_t to [1-eps, 1+eps] bounds the gradient step. The L_CLIP objective takes the pessimistic minimum: min(r_t * A_t, clip(r_t, 1-eps, 1+eps) * A_t), preventing updates that exploit outlier advantages.

```python
import torch
import torch.nn.functional as F
from typing import Tuple

def ppo_clipped_loss(
    old_logprobs: torch.Tensor,
    new_logprobs: torch.Tensor,
    advantages: torch.Tensor,
    response_mask: torch.Tensor,
    clip_eps: float = 0.2,
) -> Tuple[torch.Tensor, dict]:
    # Importance sampling ratio: r_t = pi_theta / pi_old
    log_ratio = new_logprobs - old_logprobs
    ratio = log_ratio.exp()  # [batch, seq_len]
    # Clipped surrogate: min(r_t * A_t, clip(r_t, 1-eps, 1+eps) * A_t)
    unclipped = ratio * advantages
    clipped = ratio.clamp(1 - clip_eps, 1 + clip_eps) * advantages
    policy_loss = -torch.min(unclipped, clipped)
    # Average loss over valid response tokens only
    masked_loss = (policy_loss * response_mask).sum() / response_mask.sum()
    clip_frac = ((ratio - 1.0).abs() > clip_eps).float().mean().item()
    approx_kl = (log_ratio * response_mask).sum() / response_mask.sum()
    return masked_loss, {"clip_frac": clip_frac, "approx_kl": approx_kl.item()}
```

## Value Function and GAE Estimation

The value model V_psi estimates expected future return from each token position, enabling Generalized Advantage Estimation (GAE). With lambda=0.95, GAE computes advantages as exponentially weighted TD errors: A_t = sum((gamma*lambda)^l * delta_{t+l}) where delta_t = r_t + gamma * V(s_{t+1}) - V(s_t). Returns, which serve as value training targets, are computed as advantages plus value estimates.

```python
import torch
from typing import Tuple

def compute_gae_returns(
    rewards: torch.Tensor,
    values: torch.Tensor,
    response_mask: torch.Tensor,
    gamma: float = 1.0,
    lam: float = 0.95,
) -> Tuple[torch.Tensor, torch.Tensor]:
    # Compute GAE advantages and returns for PPO-RLHF value training
    batch, seq_len = rewards.shape
    advantages = torch.zeros_like(rewards)
    last_gae = torch.zeros(batch, device=rewards.device)
    for t in reversed(range(seq_len)):
        mask_t = response_mask[:, t]
        if t < seq_len - 1:
            next_val = values[:, t + 1]
        else:
            next_val = torch.zeros(batch, device=values.device)
        delta = rewards[:, t] + gamma * next_val - values[:, t]
        last_gae = delta + gamma * lam * last_gae
        advantages[:, t] = last_gae * mask_t
    # Returns = advantages + values (targets for value function training)
    returns = advantages + values
    # Normalize advantages over valid response positions
    adv_flat = advantages[response_mask.bool()]
    advantages = (advantages - adv_flat.mean()) / (adv_flat.std() + 1e-8)
    return advantages, returns
```

## RLHF Rollout Loop

Each PPO iteration begins with a rollout phase: sample prompts from the dataset, generate completions with the current policy using temperature sampling, score with the reward model, compute per-token KL with the frozen reference, then use GAE to produce advantage estimates. Multiple PPO epochs then update the policy and value head using mini-batches from the rollout buffer. Typical setups use 512 rollouts per iteration with 4 PPO epochs.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def collect_rlhf_rollouts(
    policy_model: AutoModelForCausalLM,
    reward_model,
    tokenizer: AutoTokenizer,
    prompts: list,
    max_new_tokens: int = 256,
    device: str = "cuda",
) -> dict:
    # Generate completions and score with reward model
    policy_model.eval()
    with torch.no_grad():
        inputs = tokenizer(
            prompts, return_tensors="pt", padding=True, truncation=True
        ).to(device)
        outputs = policy_model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.9,
            top_p=0.95,
            return_dict_in_generate=True,
        )
        response_ids = outputs.sequences[:, inputs["input_ids"].shape[1]:]
        completions = tokenizer.batch_decode(response_ids, skip_special_tokens=True)
        rm_inputs = tokenizer(
            prompts, completions, return_tensors="pt", padding=True
        ).to(device)
        rm_scores = reward_model(**rm_inputs).logits.squeeze(-1)
    return {"completions": completions, "rm_scores": rm_scores, "response_ids": response_ids}
```

## PPO Hyperparameters for RLHF

| Hyperparameter | Symbol | InstructGPT Value | Effect of Increasing |
| --- | --- | --- | --- |
| KL coefficient | beta | 0.02 (adaptive) | Stronger drift penalty, slower learning, less reward hacking |
| Clip epsilon | eps | 0.2 | Wider trust region, noisier updates, higher clip fraction |
| GAE lambda | lambda | 0.95 | More bias, less variance in advantage estimates |
| Rollout batch size | B | 512 sequences | More diverse experience, slower per-iteration wall time |
| PPO mini-batch size | M | 64 sequences | Noisier gradients but faster steps per rollout buffer |
| PPO epochs per rollout | E | 4 | More gradient reuse per rollout, risk of overfit to stale advantages |

The KL coefficient beta is the most sensitive hyperparameter in PPO-RLHF. Too small and the policy reward hacks; too large and learning stalls. InstructGPT uses an adaptive controller that increases beta when KL exceeds the target and decreases it when below, maintaining roughly 6 nats of divergence throughout training.

> **Warning**: PPO for RLHF requires 4 models simultaneously in GPU memory (policy, reference, reward, value) — typical 7B scale RLHF needs 4x the memory of inference, requiring multi-GPU or LoRA on policy/value heads. With full-precision 7B models each requiring ~14GB VRAM, a single 80GB A100 is insufficient for naive full-parameter RLHF at this scale.

PPO-RLHF remains the gold standard for aligning large language models with human preferences at scale. Its four-model architecture, per-token KL penalties, and clipped surrogate objective work together to produce helpful and harmless outputs — but the engineering complexity and memory requirements have driven the community toward simpler alternatives like DPO for smaller-scale experiments.

