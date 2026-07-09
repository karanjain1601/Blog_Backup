---
title: "KL Divergence — Forward, Reverse, and Asymmetry"
slug: "kl-divergence"
description: "KL divergence definition, non-negativity proof via Jensen, asymmetric forward vs reverse behaviour, connection to MLE and variational inference, and the VAE KL term."
tags: ["information-theory","math","foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS0wgZGl2ZXJnZW5jZSAoS3VsbGJhY2stTGVpYmxlciBkaXZlcmdlbmNlKSBtZWFzdXJlcyB0aGUgaW5mb3JtYXRpb24gbG9zdCB3aGVuIHVzaW5nIGRpc3RyaWJ1dGlvbiBRIHRvIGFwcHJveGltYXRlIGRpc3RyaWJ1dGlvbiBQLiBJdCBpcyBhc3ltbWV0cmljLCBub24tbmVnYXRpdmUsIGFuZCB6ZXJvIGlmZiBQPVEuIEl0cyB0d28gZGlyZWN0aW9ucyDigJQgZm9yd2FyZCBLTCBhbmQgcmV2ZXJzZSBLTCDigJQgaGF2ZSBmdW5kYW1lbnRhbGx5IGRpZmZlcmVudCBiZWhhdmlvdXJzOiBmb3J3YXJkIEtMIGlzIG1vZGUtY292ZXJpbmcgKHVzZWQgaW4gTUxFKSwgcmV2ZXJzZSBLTCBpcyBtb2RlLXNlZWtpbmcgKHVzZWQgaW4gdmFyaWF0aW9uYWwgaW5mZXJlbmNlKS4gQ2hvb3NpbmcgdGhlIHJpZ2h0IGRpcmVjdGlvbiBpcyBvbmUgb2YgdGhlIG1vc3QgY29uc2VxdWVudGlhbCBhcmNoaXRlY3R1cmFsIGRlY2lzaW9ucyBpbiBwcm9iYWJpbGlzdGljIE1MLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlZmluaXRpb24ifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBkaXNjcmV0ZSBkaXN0cmlidXRpb25zIFAgYW5kIFE6XG5cbktMKFB8fFEpID0gc3VtX3ggcCh4KSBsb2cocCh4KS9xKHgpKSA9IEVfUFtsb2coUChYKS9RKFgpKV1cblxuRm9yIGNvbnRpbnVvdXMgZGlzdHJpYnV0aW9uczpcbktMKFB8fFEpID0gaW50ZWdyYWwgcCh4KSBsb2cocCh4KS9xKHgpKSBkeFxuXG5LTCBtZWFzdXJlcyB0aGUgZXhwZWN0ZWQgbnVtYmVyIG9mIGV4dHJhIGJpdHMgaW5jdXJyZWQgd2hlbiBlbmNvZGluZyBzYW1wbGVzIGZyb20gUCB1c2luZyBhIGNvZGUgb3B0aW1pc2VkIGZvciBRIGluc3RlYWQgb2YgUC4gSXQgZXF1YWxzIEgoUCxRKSAtIEgoUCkg4oCUIGNyb3NzLWVudHJvcHkgbWludXMgZW50cm9weS4ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOb24tTmVnYXRpdml0eSDigJQgUHJvb2YgdmlhIEplbnNlbidzIEluZXF1YWxpdHkifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IktMKFB8fFEpID49IDAsIHdpdGggZXF1YWxpdHkgaWZmIFA9USBhbG1vc3QgZXZlcnl3aGVyZS5cblxuUHJvb2Y6IC1LTChQfHxRKSA9IHN1bV94IHAoeCkgbG9nKHEoeCkvcCh4KSkgPSBFX1BbbG9nKFEoWCkvUChYKSldXG48PSBsb2coRV9QW1EoWCkvUChYKV0pIGJ5IEplbnNlbiAobG9nIGlzIGNvbmNhdmUpXG49IGxvZyhzdW1feCBxKHgpKSA9IGxvZygxKSA9IDBcblxuVGhlcmVmb3JlIC1LTCA8PSAwLCBpLmUuIEtMID49IDAuIFRoZSBwcm9vZiByZWxpZXMgb25seSBvbiB0aGUgY29uY2F2aXR5IG9mIGxvZyBhbmQgdGhlIG5vcm1hbGlzYXRpb24gb2YgUS4gVGhpcyBhbHNvIHByb3ZlcyBHaWJicycgaW5lcXVhbGl0eTogSChQLFEpID49IEgoUCkuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXN5bW1ldHJ5IG9mIEtMIERpdmVyZ2VuY2UifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IktMKFB8fFEpICE9IEtMKFF8fFApIGluIGdlbmVyYWwuIFRoZSB0d28gZGlyZWN0aW9ucyBoYXZlIHF1YWxpdGF0aXZlbHkgZGlmZmVyZW50IGJlaGF2aW91cnM6XG5cbkZvcndhcmQgS0wgKEtMKFB8fFEpKTogcGVuYWxpc2VzIHJlZ2lvbnMgd2hlcmUgcCh4KT4wIGJ1dCBxKHgpfjAuIFEgbXVzdCBjb3ZlciBhbGwgbW9kZXMgb2YgUCDigJQgaXQgY2Fubm90IGlnbm9yZSBhbnkgcmVnaW9uIHdpdGggcG9zaXRpdmUgcHJvYmFiaWxpdHkgdW5kZXIgUC4gQ2FsbGVkIGluY2x1c2l2ZSBvciBtZWFuLXNlZWtpbmcuXG5cblJldmVyc2UgS0wgKEtMKFF8fFApKTogcGVuYWxpc2VzIHJlZ2lvbnMgd2hlcmUgcSh4KT4wIGJ1dCBwKHgpfjAuIFEgaXMgcGVuYWxpc2VkIGZvciBwbGFjaW5nIHByb2JhYmlsaXR5IGluIHJlZ2lvbnMgUCBkb2VzIG5vdCBzdXBwb3J0LiBDYWxsZWQgZXhjbHVzaXZlIG9yIG1vZGUtc2Vla2luZyDigJQgUSB3aWxsIGNvbmNlbnRyYXRlIG9uIG9uZSBtb2RlIG9mIFAgcmF0aGVyIHRoYW4gc3ByZWFkIGFjcm9zcyBhbGwgbW9kZXMuIn0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJWaXN1YWwgSW50dWl0aW9uIGZvciBBc3ltbWV0cnkiLCJjb250ZW50IjoiSW1hZ2luZSBQIGlzIGJpbW9kYWwgKHR3byBwZWFrcykgYW5kIFEgaXMgdW5pbW9kYWwgR2F1c3NpYW4uIEZvcndhcmQgS0wgKEtMKFB8fFEpKSBmb3JjZXMgUSB0byBzcHJlYWQgYmV0d2VlbiBib3RoIHBlYWtzIOKAlCBtb2RlIGNvdmVyaW5nLCBoaWdoIHZhcmlhbmNlIHNvbHV0aW9uLiBSZXZlcnNlIEtMIChLTChRfHxQKSkgbGV0cyBRIGNvbGxhcHNlIG9udG8gb25lIHBlYWsg4oCUIG1vZGUgc2Vla2luZywgbG93IHZhcmlhbmNlIHNvbHV0aW9uLiBUaGUgVkFFIGVuY29kZXIgbWluaW1pc2VzIHJldmVyc2UgS0wgKHFfcGhpKHp8eCkgdnMgcCh6fHgpKSwgd2hpY2ggaXMgd2h5IFZBRXMgdGVuZCB0byBoYXZlIGJsdXJyeSByZWNvbnN0cnVjdGlvbnM6IHRoZSBhcHByb3hpbWF0ZSBwb3N0ZXJpb3IgaXMgaW5jZW50aXZpc2VkIHRvIGJlIG1vZGUtc2Vla2luZy4ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGb3J3YXJkIEtMID0gTWF4aW11bSBMaWtlbGlob29kIEVzdGltYXRpb24ifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1pbmltaXNpbmcgS0woUF9kYXRhIHx8IFFfbW9kZWwpIG92ZXIgbW9kZWwgcGFyYW1ldGVycyBpcyBlcXVpdmFsZW50IHRvIE1MRTpcblxuS0woUHx8USkgPSBzdW0gcCh4KSBsb2cgcCh4KSAtIHN1bSBwKHgpIGxvZyBxKHgpID0gLUgoUCkgKyBIKFAsUSlcblxuTWluaW1pc2luZyBvdmVyIFFfbW9kZWw6IHNpbmNlIEgoUCkgaXMgY29uc3RhbnQsIG1pbmltaXNlIEgoUCxRKSA9IEVfUFstbG9nIFEoWCldID0gZXhwZWN0ZWQgbmVnYXRpdmUgbG9nLWxpa2VsaWhvb2QuIE1MRSBtYXhpbWlzZXMgRV9QW2xvZyBRKFgpXSDigJQgaWRlbnRpY2FsIG9wdGltaXNhdGlvbi4gRXZlcnkgZ3JhZGllbnQgZGVzY2VudCB0cmFpbmluZyBydW4gb24gY3Jvc3MtZW50cm9weSBpcyBwZXJmb3JtaW5nIGZvcndhcmQgS0wgbWluaW1pc2F0aW9uIGFnYWluc3QgdGhlIGVtcGlyaWNhbCBkYXRhIGRpc3RyaWJ1dGlvbi4ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXZlcnNlIEtMID0gVmFyaWF0aW9uYWwgSW5mZXJlbmNlIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiB2YXJpYXRpb25hbCBpbmZlcmVuY2UsIHdlIHdhbnQgdG8gYXBwcm94aW1hdGUgYSB0cnVlIHBvc3RlcmlvciBwKHp8eCkgd2l0aCBhIHNpbXBsZXIgZmFtaWx5IHFfcGhpKHp8eCkuIFdlIG1pbmltaXNlIEtMKFF8fFApOlxuXG5LTChxX3BoaSh6fHgpIHx8IHAoenx4KSkgPSBFX3txX3BoaX1bbG9nIHFfcGhpKHp8eCldIC0gRV97cV9waGl9W2xvZyBwKHp8eCldXG49IEVfe3FfcGhpfVtsb2cgcV9waGkoenx4KV0gLSBFX3txX3BoaX1bbG9nIHAoeCx6KV0gKyBsb2cgcCh4KVxuXG5TaW5jZSBsb2cgcCh4KSBpcyBjb25zdGFudCBpbiBwaGksIG1pbmltaXNpbmcgS0woUXx8UCkgPSBtYXhpbWlzaW5nIHRoZSBFTEJPOlxuRUxCTyA9IEVfe3FfcGhpfVtsb2cgcCh4LHopXSAtIEVfe3FfcGhpfVtsb2cgcV9waGkoenx4KV1cblxuVGhpcyBpcyBtb2RlLXNlZWtpbmc6IHEgdGVuZHMgdG8gY29sbGFwc2Ugb250byBhIHNpbmdsZSBtb2RlIG9mIHAoenx4KSwgaWdub3Jpbmcgb3RoZXIgbW9kZXMuIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG4jIEtMIGRpdmVyZ2VuY2UgYmV0d2VlbiB0d28gZGlzY3JldGUgZGlzdHJpYnV0aW9uc1xuZGVmIGtsX2ZvcndhcmQocCwgcSwgZXBzPTFlLTEwKTpcbiAgICBcIlwiXCJLTChQfHxRKSDigJQgZm9yd2FyZCBLTCwgbW9kZS1jb3ZlcmluZy5cIlwiXCJcbiAgICBwLCBxID0gdG9yY2gudGVuc29yKHApK2VwcywgdG9yY2gudGVuc29yKHEpK2Vwc1xuICAgIHAsIHEgPSBwL3Auc3VtKCksIHEvcS5zdW0oKVxuICAgIHJldHVybiAocCAqIChwL3EpLmxvZygpKS5zdW0oKS5pdGVtKClcblxuZGVmIGtsX3JldmVyc2UocCwgcSwgZXBzPTFlLTEwKTpcbiAgICBcIlwiXCJLTChRfHxQKSDigJQgcmV2ZXJzZSBLTCwgbW9kZS1zZWVraW5nLlwiXCJcIlxuICAgIHJldHVybiBrbF9mb3J3YXJkKHEsIHAsIGVwcylcblxuIyBCaW1vZGFsIFAgdnMgdW5pbW9kYWwgUVxucCA9IFswLjQ1LCAwLjA1LCAwLjA1LCAwLjQ1XSAgIyBiaW1vZGFsXG5xID0gWzAuMjUsIDAuMjUsIDAuMjUsIDAuMjVdICAjIHVuaWZvcm0gKHNwcmVhZGluZyBhdHRlbXB0KVxucTI9IFswLjksIDAuMDMzLCAwLjAzMywgMC4wMzNdICMgY29uY2VudHJhdGVkIG9uIG1vZGUgMVxuXG5wcmludChmJ0tMKFB8fHVuaWZvcm0pID0ge2tsX2ZvcndhcmQocCxxKTouNGZ9JykgICAjIGZvcndhcmQ6IHVuaWZvcm0gaXMgb2tcbnByaW50KGYnS0woUHx8bW9kZTEpICAgPSB7a2xfZm9yd2FyZChwLHEyKTouNGZ9JykgICMgZm9yd2FyZDogbWlzc2luZyBtb2RlMlxucHJpbnQoZidLTChtb2RlMXx8UCkgICA9IHtrbF9yZXZlcnNlKHAscTIpOi40Zn0nKSAgIyByZXZlcnNlOiBjb25jZW50cmF0aW5nIGlzIGZpbmVcblxuIyBQeVRvcmNoIEtMIGZvciBjb250aW51b3VzIChlLmcuIHR3byBHYXVzc2lhbnMpXG5mcm9tIHRvcmNoLmRpc3RyaWJ1dGlvbnMgaW1wb3J0IE5vcm1hbCwga2xfZGl2ZXJnZW5jZVxucF9kaXN0ID0gTm9ybWFsKDAuMCwgMS4wKVxucV9kaXN0ID0gTm9ybWFsKDAuNSwgMS4yKVxucHJpbnQoZidLTChOKDAsMSl8fE4oMC41LDEuMikpID0ge2tsX2RpdmVyZ2VuY2UocF9kaXN0LHFfZGlzdCk6LjRmfSBuYXRzJykifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLTCBpbiB0aGUgVkFFIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgVkFFIEVMQk8gaXM6XG5FTEJPID0gRV97cV9waGkoenx4KX1bbG9nIHBfdGhldGEoeHx6KV0gLSBLTChxX3BoaSh6fHgpIHx8IHAoeikpXG5cblRoZSBzZWNvbmQgdGVybSBpcyB0aGUgcmV2ZXJzZSBLTCBiZXR3ZWVuIHRoZSBlbmNvZGVyIGRpc3RyaWJ1dGlvbiBhbmQgdGhlIHByaW9yIHAoeikgPSBOKDAsSSkuIEZvciBhIEdhdXNzaWFuIGVuY29kZXIgcV9waGkgPSBOKG11LCBzaWdtYV4yKkkpOlxuXG5LTChOKG11LCBkaWFnKHNpZ21hXjIpKSB8fCBOKDAsSSkpID0gKDEvMikgKiBzdW1faiBbbXVfal4yICsgc2lnbWFfal4yIC0gMSAtIGxvZyBzaWdtYV9qXjJdXG5cblRoaXMgY2xvc2VkIGZvcm0gbWFrZXMgVkFFIHRyYWluaW5nIHRyYWN0YWJsZS4gVGhlIEtMIHRlcm0gcmVndWxhcmlzZXMgdGhlIGxhdGVudCBzcGFjZSwgcHVzaGluZyBlbmNvZGluZ3MgdG93YXJkIHRoZSBwcmlvciBhbmQgZW5hYmxpbmcgZ2VuZXJhdGlvbiBieSBzYW1wbGluZyB6IH4gTigwLEkpLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkYtRGl2ZXJnZW5jZXMg4oCUIEdlbmVyYWxpc2luZyBLTCJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS0wgYmVsb25ncyB0byB0aGUgZmFtaWx5IG9mIGYtZGl2ZXJnZW5jZXM6XG5cbkRfZihQfHxRKSA9IGludGVncmFsIHEoeCkgZihwKHgpL3EoeCkpIGR4XG5cbndoZXJlIGYgaXMgYSBjb252ZXggZnVuY3Rpb24gd2l0aCBmKDEpPTAuXG5cbi0gS0woUHx8USk6IGYodCkgPSB0IGxvZyB0ICAoZm9yd2FyZCBLTClcbi0gS0woUXx8UCk6IGYodCkgPSAtbG9nIHQgIChyZXZlcnNlIEtMKVxuLSBKZW5zZW4tU2hhbm5vbjogZih0KSA9IHQgbG9nIHQgLSAodCsxKSBsb2coKHQrMSkvMikgIChzeW1tZXRyaWMsIGJvdW5kZWQpXG4tIGNoaS1zcXVhcmVkOiBmKHQpID0gKHQtMSleMlxuLSBUb3RhbCB2YXJpYXRpb246IGYodCkgPSB8dC0xfC8yXG5cbkdBTnMgY2FuIGJlIHNlZW4gYXMgYXBwcm94aW1hdGluZyB2YXJpb3VzIGYtZGl2ZXJnZW5jZXMgZGVwZW5kaW5nIG9uIHRoZSBkaXNjcmltaW5hdG9yIGxvc3MuIn0sCiAgeyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRpcmVjdGlvbiIsIkJlaGF2aW91ciIsIlVzZWQgSW4iLCJQcm9wZXJ0eSJdLCJyb3dzIjpbWyJGb3J3YXJkIEtMKFB8fFEpIiwiTW9kZS1jb3ZlcmluZyIsIk1MRSwgY3Jvc3MtZW50cm9weSBsb3NzIiwiSW5jbHVzaXZlIOKAlCBRIG11c3QgY292ZXIgYWxsIG9mIFAiXSxbIlJldmVyc2UgS0woUXx8UCkiLCJNb2RlLXNlZWtpbmciLCJWYXJpYXRpb25hbCBpbmZlcmVuY2UsIFZBRSBlbmNvZGVyIiwiRXhjbHVzaXZlIOKAlCBRIGlnbm9yZXMgbW9kZXMgb2YgUCJdLFsiSlNEIiwiU3ltbWV0cmljIiwiT3JpZ2luYWwgR0FOIGxvc3MiLCJCb3VuZGVkIFswLCBsbiAyXSJdLFsiS0wocXx8cCkgVkFFIiwiTW9kZS1zZWVraW5nIiwiVkFFIGVuY29kZXIiLCJDbG9zZWQgZm9ybSBmb3IgR2F1c3NpYW5zIl1dfSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiV2hlbiB0byBVc2UgRWFjaCBEaXJlY3Rpb24iLCJjb250ZW50IjoiVXNlIGZvcndhcmQgS0wgKGNyb3NzLWVudHJvcHkvTUxFKSB3aGVuIHlvdSB3YW50IHRoZSBtb2RlbCB0byBjb3ZlciBhbGwgbW9kZXMgb2YgdGhlIGRhdGEg4oCUIHR5cGljYWwgZm9yIGRpc2NyaW1pbmF0aXZlIGNsYXNzaWZpZXJzIGFuZCBsYW5ndWFnZSBtb2RlbHMuIFVzZSByZXZlcnNlIEtMICh2YXJpYXRpb25hbCBpbmZlcmVuY2UpIHdoZW4geW91IHdhbnQgYSB0cmFjdGFibGUgYXBwcm94aW1hdGUgcG9zdGVyaW9yIGFuZCBjYW4gdG9sZXJhdGUgbW9kZS1jb2xsYXBzZSBpbiB0aGUgYXBwcm94aW1hdGlvbi4gRm9yIEdBTnMsIEplbnNlbi1TaGFubm9uIG9yIFdhc3NlcnN0ZWluIGRpc3RhbmNlIGF2b2lkIHRoZSB6ZXJvLWdyYWRpZW50IHByb2JsZW0gdGhhdCBib3RoIEtMIGRpcmVjdGlvbnMgc3VmZmVyIHdoZW4gc3VwcG9ydHMgZG9uJ3Qgb3ZlcmxhcC4ifSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IktMIENhbiBCZSBJbmZpbml0ZSIsImNvbnRlbnQiOiJLTChQfHxRKSA9ICtpbmYgd2hlbmV2ZXIgcCh4KT4wIGJ1dCBxKHgpPTAgZm9yIHNvbWUgeC4gVGhpcyBicmVha3MgdHJhaW5pbmc6IGNyb3NzLWVudHJvcHkgbG9zcyBjYW4gYmUgaW5maW5pdGUgaWYgdGhlIG1vZGVsIGFzc2lnbnMgemVybyBwcm9iYWJpbGl0eSB0byBhIHRyYWluaW5nIGV4YW1wbGUuIFNvbHV0aW9uczogYWRkIGVwc2lsb24gc21vb3RoaW5nIHRvIHByb2JhYmlsaXRpZXMsIHVzZSB0ZW1wZXJhdHVyZS1zY2FsZWQgc29mdG1heCAobmV2ZXIgb3V0cHV0cyBleGFjdCB6ZXJvKSwgdXNlIGxhYmVsIHNtb290aGluZywgb3IgZW5zdXJlIHZvY2FidWxhcnkgY292ZXJhZ2UuIFB5VG9yY2gncyBGLmNyb3NzX2VudHJvcHkgaGFuZGxlcyB0aGlzIHZpYSB0aGUgbG9nLXNvZnRtYXggd2hpY2ggb3V0cHV0cyBsb2coMCk9LWluZiBvbmx5IGluIGRlZ2VuZXJhdGUgY2FzZXMuIn0KXQ=="
---
# KL Divergence — Forward, Reverse, and Asymmetry

KL divergence measures the information lost when using distribution Q to approximate P. Its two directions have fundamentally different behaviours: forward KL is mode-covering (MLE), reverse KL is mode-seeking (variational inference).

## Definition

$$\text{KL}(P\|Q) = \sum_x p(x)\log\frac{p(x)}{q(x)} = \mathbb{E}_P\!\left[\log\frac{P(X)}{Q(X)}\right]$$

Equals $H(P,Q) - H(P)$ — extra bits from using the wrong code.

## Non-Negativity — Proof via Jensen's Inequality

$$-\text{KL}(P\|Q) = \mathbb{E}_P\!\left[\log\frac{Q(X)}{P(X)}\right] \leq \log\mathbb{E}_P\!\left[\frac{Q(X)}{P(X)}\right] = \log 1 = 0$$

Therefore $\text{KL}(P\|Q) \geq 0$, with equality iff $P = Q$ a.e.

## Asymmetry of KL Divergence

**Forward KL** $\text{KL}(P\|Q)$: penalises $q(x)\approx 0$ where $p(x)>0$. Q must cover all modes of P. **Inclusive / mode-covering.**

**Reverse KL** $\text{KL}(Q\|P)$: penalises $q(x)>0$ where $p(x)\approx 0$. Q collapses onto one mode of P. **Exclusive / mode-seeking.**

> **INFO: Visual Intuition for Asymmetry**
> Imagine P is bimodal and Q is unimodal Gaussian. Forward KL forces Q to spread between both peaks. Reverse KL lets Q collapse onto one peak. VAEs use reverse KL for the encoder — which is why they tend to have blurry reconstructions.

## Forward KL = Maximum Likelihood Estimation

$$\text{KL}(P_{\text{data}}\|Q_{\text{model}}) = -H(P) + H(P,Q)$$

Minimising over $Q_{\text{model}}$: $H(P)$ is constant, so minimise $H(P,Q)$ = negative log-likelihood. **Every cross-entropy training run is forward KL minimisation.**

## Reverse KL = Variational Inference

$$\text{KL}(q_\phi(z|x)\|p(z|x)) = -\text{ELBO} + \log p(x)$$

Minimising $\text{KL}(Q\|P)$ is equivalent to maximising the ELBO. Mode-seeking: $q$ collapses onto a single mode of $p(z|x)$.

```python
import torch
from torch.distributions import Normal, kl_divergence

def kl_forward(p, q, eps=1e-10):
    """KL(P||Q) — mode-covering."""
    p, q = torch.tensor(p)+eps, torch.tensor(q)+eps
    p, q = p/p.sum(), q/q.sum()
    return (p * (p/q).log()).sum().item()

# Bimodal P vs various Q
p  = [0.45, 0.05, 0.05, 0.45]
q_uniform = [0.25, 0.25, 0.25, 0.25]
q_mode1   = [0.9,  0.033, 0.033, 0.033]

print(f'KL(P||uniform) = {kl_forward(p, q_uniform):.4f}')  # small: uniform covers all
print(f'KL(P||mode1)   = {kl_forward(p, q_mode1):.4f}')    # large: misses mode 2

# Closed form for Gaussians
p_dist = Normal(0.0, 1.0)
q_dist = Normal(0.5, 1.2)
print(f'KL(N(0,1)||N(0.5,1.2)) = {kl_divergence(p_dist, q_dist):.4f} nats')
```

## KL in the VAE

$$\text{ELBO} = \mathbb{E}_{q_\phi}[\log p_\theta(x|z)] - \text{KL}(q_\phi(z|x)\|p(z))$$

For Gaussian encoder $q_\phi = \mathcal{N}(\mu, \text{diag}(\sigma^2))$:

$$\text{KL} = \frac{1}{2}\sum_j\!\left[\mu_j^2 + \sigma_j^2 - 1 - \log\sigma_j^2\right]$$

Closed form — enables tractable training. KL regularises latent space toward $\mathcal{N}(0,I)$.

## F-Divergences — Generalising KL

$$D_f(P\|Q) = \int q(x)\,f\!\left(\frac{p(x)}{q(x)}\right)dx$$

where $f$ is convex with $f(1)=0$. KL(P‖Q): $f(t)=t\log t$. Reverse KL: $f(t)=-\log t$. Chi-squared: $f(t)=(t-1)^2$.

| Direction | Behaviour | Used In | Property |
|---|---|---|---|
| Forward KL(P‖Q) | Mode-covering | MLE, cross-entropy | Inclusive |
| Reverse KL(Q‖P) | Mode-seeking | Variational inference | Exclusive |
| JSD | Symmetric | Original GAN | Bounded [0, ln 2] |
| KL(q‖p) VAE | Mode-seeking | VAE encoder | Closed form for Gaussians |

> **TIP: When to Use Each Direction**
> Forward KL for discriminative models and LLMs — cover all data modes. Reverse KL for variational inference — tractable approximate posteriors. For GANs, use JSD or Wasserstein to avoid the infinite-divergence problem when supports don't overlap.

> **WARNING: KL Can Be Infinite**
> $\text{KL}(P\|Q) = +\infty$ whenever $p(x)>0$ but $q(x)=0$. Mitigations: label smoothing, softmax temperature, epsilon-clipping, or vocabulary coverage guarantees.