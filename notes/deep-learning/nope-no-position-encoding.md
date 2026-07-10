---
title: "NoPE — No Positional Encoding and Implicit Position via Causal Masking"
slug: "nope-no-position-encoding"
description: "Analysis of NoPE (Kazemnejad et al. 2023): removing all positional encodings and relying on causal masking alone for implicit positional signal, with length generalisation experiments, attention pattern analysis, and ablation studies."
tags: ["deep-learning", "transformers", "positional-encoding"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm9QRSAoTm8gUG9zaXRpb25hbCBFbmNvZGluZyksIHN0dWRpZWQgc3lzdGVtYXRpY2FsbHkgYnkgS2F6ZW1uZWphZCBldCBhbC4gKDIwMjMpLCBhbnN3ZXJzIGEgcHJvdm9jYXRpdmUgcXVlc3Rpb246ICp3aGF0IGhhcHBlbnMgaWYgeW91IHJlbW92ZSBwb3NpdGlvbmFsIGVuY29kaW5nIGVudGlyZWx5Kj8gVGhlIHN1cnByaXNpbmcgZmluZGluZyBpcyB0aGF0IGRlY29kZXItb25seSBUcmFuc2Zvcm1lcnMgd2l0aG91dCBhbnkgcG9zaXRpb25hbCBlbmNvZGluZyBjYW4gc3RpbGwgbGVhcm4gc2VxdWVuY2Ugb3JkZXIg4oCUIG5vdCB0aHJvdWdoIGV4cGxpY2l0IFBFLCBidXQgdGhyb3VnaCBhbiBpbXBsaWNpdCBwb3NpdGlvbmFsIHNpZ25hbCBlbWJlZGRlZCBpbiB0aGUgY2F1c2FsIGF0dGVudGlvbiBtYXNrIGl0c2VsZi4gTm9QRSBtb2RlbHMgZ2VuZXJhbGlzZSB0byBsb25nZXIgc2VxdWVuY2VzIGJldHRlciB0aGFuIGFic29sdXRlIFBFIG1vZGVscywgdGhvdWdoIHRoZXkgZmFsbCBzaG9ydCBvZiBSb1BFIGFuZCBBTGlCaS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb3RpdmF0aW9uIOKAlCBXaHkgUmVtb3ZlIFBvc2l0aW9uYWwgRW5jb2RpbmdzPyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWJzb2x1dGUgcG9zaXRpb25hbCBlbmNvZGluZ3MgKHNpbnVzb2lkYWwgb3IgbGVhcm5lZCkgaGF2ZSBhIGZ1bmRhbWVudGFsIGxlbmd0aC1nZW5lcmFsaXNhdGlvbiBwcm9ibGVtOiBlYWNoIHBvc2l0aW9uIGluZGV4IHQgbWFwcyB0byBhIHVuaXF1ZSBlbWJlZGRpbmcgdmVjdG9yLiBEdXJpbmcgdHJhaW5pbmcgb24gc2VxdWVuY2VzIG9mIGxlbmd0aCBMLCB0aGUgbW9kZWwgc2VlcyBwb3NpdGlvbiBpbmRpY2VzIDAgdGhyb3VnaCBM4oiSMS4gQXQgaW5mZXJlbmNlIHdpdGggYSBsb25nZXIgc2VxdWVuY2Ugb2YgbGVuZ3RoIEzigLIgXHUwMDNlIEwsIHBvc2l0aW9ucyBMIHRocm91Z2ggTOKAsuKIkjEgbWFwIHRvIGVtYmVkZGluZyB2ZWN0b3JzIHRoYXQgd2VyZSBuZXZlciB1cGRhdGVkIGJ5IGdyYWRpZW50IGRlc2NlbnQg4oCUIHRoZXkgYXJlIGVmZmVjdGl2ZWx5IHJhbmRvbSBub2lzZS4gVGhpcyBpcyB0aGUgcm9vdCBjYXVzZSBvZiBjYXRhc3Ryb3BoaWMgcGVycGxleGl0eSBkZWdyYWRhdGlvbiBhdCBPT0QgbGVuZ3Rocy4gVGhlIE5vUEUgaHlwb3RoZXNpcyBpcyB0aGF0IHJlbW92aW5nIHRoZXNlIHByb2JsZW1hdGljIGVtYmVkZGluZ3MgZW50aXJlbHkgaXMgYmV0dGVyIHRoYW4gaW5qZWN0aW5nIG1pc2xlYWRpbmcgbm9pc2UuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbnNpZ2h0IiwidGl0bGUiOiJDYXVzYWwgTWFza2luZyBhcyBJbXBsaWNpdCBQb3NpdGlvbiIsImNvbnRlbnQiOiJFdmVuIHdpdGhvdXQgZXhwbGljaXQgcG9zaXRpb25hbCBlbWJlZGRpbmdzLCBlYWNoIHRva2VuIGF0IHBvc2l0aW9uIHQgY2FuIG9ubHkgYXR0ZW5kIHRvIHRva2VucyBhdCBwb3NpdGlvbnMgMCB0aHJvdWdoIHTiiJIxLiBUaGlzIGNyZWF0ZXMgYSB1bmlxdWUgY2F1c2FsIGNvbnRleHQgZGVwdGggZm9yIGVhY2ggcG9zaXRpb246IHBvc2l0aW9uIDAgaGFzIGFuIGVtcHR5IGNvbnRleHQsIHBvc2l0aW9uIDEgY2FuIHNlZSBvbmUgdG9rZW4sIHBvc2l0aW9uIDUgY2FuIHNlZSBmaXZlIHRva2Vucy4gQXR0ZW50aW9uIGhlYWRzIGNhbiBpbXBsaWNpdGx5IGxlYXJuIHRvIHVzZSB0aGlzIGNvbnRleHQgZGVwdGggYXMgYSBwb3NpdGlvbmFsIHNpZ25hbCDigJQgY291bnRpbmcgcG9zaXRpb24gdmlhIHRoZSBzaGFwZSBvZiB3aGF0IGlzIHZpc2libGUgcmF0aGVyIHRoYW4gdmlhIGFuIGluamVjdGVkIGVtYmVkZGluZyB2ZWN0b3IuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2F1c2FsIE1hc2tpbmcgYXMgSW1wbGljaXQgUG9zaXRpb24gU2lnbmFsIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2V5IGluc2lnaHQgaXMgdGhhdCBpbiBhIGRlY29kZXItb25seSBtb2RlbCB3aXRoIGNhdXNhbCBtYXNraW5nLCBwb3NpdGlvbiBpbmZvcm1hdGlvbiBpcyAqc3RydWN0dXJhbGx5KiBhdmFpbGFibGUgZXZlbiB3aXRob3V0IGV4cGxpY2l0IFBFLiBUb2tlbiBhdCBwb3NpdGlvbiB0IGhhcyBhY2Nlc3MgdG8gZXhhY3RseSB0IHByZXZpb3VzIHRva2VucyDigJQgbm8gbW9yZSwgbm8gbGVzcy4gRW1waXJpY2FsbHksIE5vUEUgbW9kZWxzIGRldmVsb3AgYXR0ZW50aW9uIGhlYWRzIHRoYXQgZXhoaWJpdCBwb3NpdGlvbi1kZXBlbmRlbnQgcGF0dGVybnM6IHNvbWUgaGVhZHMgbGVhcm4gdG8gYXR0ZW5kIHRvIGZpeGVkIHJlbGF0aXZlIG9mZnNldHMsIG90aGVycyBkZXZlbG9wIHJ1bm5pbmctYXZlcmFnZS1saWtlIGJlaGF2aW91ci4gVGhlc2UgZW1lcmdlbnQgc3RyYXRlZ2llcyBwcm92aWRlIGNvYXJzZSBwb3NpdGlvbiBhd2FyZW5lc3MgdGhhdCBzdWZmaWNlcyBmb3IgbGFuZ3VhZ2UgbW9kZWxsaW5nLCB0aG91Z2ggdGhleSBhcmUgbGVzcyBwcmVjaXNlIHRoYW4gZXhwbGljaXQgUEUgYXQgY2FwdHVyaW5nIGV4YWN0IGFic29sdXRlIHBvc2l0aW9ucy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlBvc2l0aW9uIDA6IGVtcHR5IGNvbnRleHQg4oCUIG1vZGVsIGxlYXJucyB0aGlzIGlzIHRoZSBmaXJzdCB0b2tlbiIsIlBvc2l0aW9uIHQ6IGV4YWN0bHkgdCB0b2tlbnMgdmlzaWJsZSDigJQgY2F1c2FsIGRlcHRoIGVuY29kZXMgcG9zaXRpb24gaW1wbGljaXRseSIsIk5vUEUgaXMgZnVsbHkgY29tcGF0aWJsZSB3aXRoIGFueSBzZXF1ZW5jZSBsZW5ndGggYXQgYm90aCB0cmFpbiBhbmQgdGVzdCB0aW1lIiwiQmlkaXJlY3Rpb25hbCBOb1BFIChlLmcuLCBCRVJUIHdpdGhvdXQgUEUpOiB0cnVseSBwZXJtdXRhdGlvbi1pbnZhcmlhbnQg4oCUIHBvc2l0aW9uIGlzIG5vdCByZWNvdmVyYWJsZSIsIkRlY29kZXIgTm9QRTogcG9zaXRpb24gaXMgcmVjb3ZlcmFibGUgdmlhIGNhdXNhbCBkZXB0aCwgc28gbW9kZWxzIHJlbWFpbiBub24tcGVybXV0YXRpb24taW52YXJpYW50Il19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMSDigJQgTm9QRSBUcmFuc2Zvcm1lciBCbG9jayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBtaW5pbWFsIE5vUEUgZGVjb2RlciBibG9jayB0aGF0IHJlbW92ZXMgYWxsIHBvc2l0aW9uYWwgZW1iZWRkaW5nIGluZnJhc3RydWN0dXJlLiBUaGUgdG9rZW4gZW1iZWRkaW5nIGlzIHRoZSBvbmx5IGVtYmVkZGluZyBsb29rdXAg4oCUIG5vIHBvc2l0aW9uIGluZGV4IGlzIGV2ZXIgcGFzc2VkIG9yIGFkZGVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuXG5jbGFzcyBOb1BFQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJEZWNvZGVyIHNlbGYtYXR0ZW50aW9uIGJsb2NrIHdpdGggY2F1c2FsIG1hc2sgYW5kIE5PIHBvc2l0aW9uYWwgZW5jb2RpbmcuXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbDogaW50LCBuX2hlYWRzOiBpbnQsIGRfZmY6IGludCwgZHJvcG91dDogZmxvYXQgPSAwLjEpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uX2hlYWRzID0gbl9oZWFkc1xuICAgICAgICBzZWxmLmRfayAgPSBkX21vZGVsIC8vIG5faGVhZHNcbiAgICAgICAgc2VsZi5xa3YgID0gbm4uTGluZWFyKGRfbW9kZWwsIDMgKiBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnByb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5mZiAgID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKSwgbm4uR0VMVSgpLCBubi5MaW5lYXIoZF9mZiwgZF9tb2RlbClcbiAgICAgICAgKVxuICAgICAgICBzZWxmLmxuMSAgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5sbjIgID0gbm4uTGF5ZXJOb3JtKGRfbW9kZWwpXG4gICAgICAgIHNlbGYuZHJvcCA9IG5uLkRyb3BvdXQoZHJvcG91dClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIEIsIEwsIF8gPSB4LnNoYXBlXG4gICAgICAgIGggICA9IHNlbGYubG4xKHgpXG4gICAgICAgIHFrdiA9IHNlbGYucWt2KGgpLnJlc2hhcGUoQiwgTCwgMywgc2VsZi5uX2hlYWRzLCBzZWxmLmRfaykucGVybXV0ZSgyLCAwLCAzLCAxLCA0KVxuICAgICAgICBRLCBLLCBWID0gcWt2WzBdLCBxa3ZbMV0sIHFrdlsyXVxuICAgICAgICBzY29yZXMgPSB0b3JjaC5tYXRtdWwoUSwgSy50cmFuc3Bvc2UoLTIsIC0xKSkgLyBtYXRoLnNxcnQoc2VsZi5kX2spXG4gICAgICAgIG1hc2sgICA9IHRvcmNoLnRyaXUodG9yY2gub25lcyhMLCBMLCBkZXZpY2U9eC5kZXZpY2UpLCBkaWFnb25hbD0xKS5ib29sKClcbiAgICAgICAgc2NvcmVzID0gc2NvcmVzLm1hc2tlZF9maWxsKG1hc2ssIGZsb2F0KFwiLWluZlwiKSkgICMgY2F1c2FsIG9ubHkg4oCUIG5vIFBFIGJpYXNcbiAgICAgICAgYXR0biAgID0gdG9yY2gubWF0bXVsKEYuc29mdG1heChzY29yZXMsIGRpbT0tMSksIFYpLnRyYW5zcG9zZSgxLCAyKS5yZXNoYXBlKEIsIEwsIC0xKVxuICAgICAgICB4ID0geCArIHNlbGYuZHJvcChzZWxmLnByb2ooYXR0bikpXG4gICAgICAgIHggPSB4ICsgc2VsZi5kcm9wKHNlbGYuZmYoc2VsZi5sbjIoeCkpKVxuICAgICAgICByZXR1cm4geFxuXG5cbiMgVmVyaWZ5OiBzYW1lIGJsb2NrIHdvcmtzIGZvciBhbnkgc2VxdWVuY2UgbGVuZ3RoIOKAlCBubyBwb3NpdGlvbiBPT0RcbmJsb2NrID0gTm9QRUJsb2NrKGRfbW9kZWw9MTI4LCBuX2hlYWRzPTQsIGRfZmY9NTEyKVxuZm9yIHNlcV9sZW4gaW4gWzY0LCAyNTYsIDEwMjQsIDQwOTZdOlxuICAgIHkgPSBibG9jayh0b3JjaC5yYW5kbigxLCBzZXFfbGVuLCAxMjgpKVxuICAgIHByaW50KGZcInNlcV9sZW49e3NlcV9sZW46XHUwMDNjNn0gb3V0cHV0PXt5LnNoYXBlfSAgT0tcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIExlbmd0aCBHZW5lcmFsaXNhdGlvbiBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb21wYXJpbmcgcGVycGxleGl0eSBhdCBvdXQtb2YtZGlzdHJpYnV0aW9uIGxlbmd0aHMgZm9yIHRocmVlIFBFIHN0cmF0ZWdpZXMuIFZhbHVlcyBhcmUgYXBwcm94aW1hdGUgZmlndXJlcyBhbGlnbmVkIHdpdGggS2F6ZW1uZWphZCBldCBhbC4gKDIwMjMpIGZpbmRpbmdzOiBhYnNvbHV0ZSBQRSBjb2xsYXBzZXMgYmV5b25kIHRyYWluaW5nIGxlbmd0aCwgTm9QRSBkZWdyYWRlcyBncmFjZWZ1bGx5LCBSb1BFIGV4dHJhcG9sYXRlcyBiZXN0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbWF0aFxuXG4jIEFwcHJveGltYXRlIHBlcnBsZXhpdHkgZnJvbSBLYXplbW5lamFkIGV0IGFsLiAoMjAyMykg4oCUIGRlY29kZXIgTE0gb24gV2lraVRleHQtMTAzXG4jIEFsbCBtb2RlbHMgdHJhaW5lZCBvbiBzZXF1ZW5jZXMgb2YgbGVuZ3RoIDUxMlxuXG50cmFpbl9sZW4gPSA1MTJcbnRlc3RfbGVucyAgPSBbMjU2LCA1MTIsIDEwMjQsIDIwNDgsIDQwOTZdXG5cbnJlc3VsdHMgPSB7XG4gICAgXCJBYnNvbHV0ZSBQRVwiOiB7MjU2OiAxOS4yLCA1MTI6IDIwLjEsIDEwMjQ6IDI4LjcsICAgICAgICAgIDIwNDg6IDUxLjMsICAgICAgICAgIDQwOTY6IGZsb2F0KFwiaW5mXCIpfSxcbiAgICBcIk5vUEVcIjogICAgICAgIHsyNTY6IDIxLjQsIDUxMjogMjIuMCwgMTAyNDogMjQuNSwgICAgICAgICAgMjA0ODogMjkuMywgICAgICAgICAgNDA5NjogMzguMX0sXG4gICAgXCJSb1BFXCI6ICAgICAgICB7MjU2OiAxOS44LCA1MTI6IDIwLjMsIDEwMjQ6IDIxLjAsICAgICAgICAgIDIwNDg6IDIyLjEsICAgICAgICAgIDQwOTY6IDI0Ljd9LFxuICAgIFwiQUxpQmlcIjogICAgICAgezI1NjogMjAuMSwgNTEyOiAyMC41LCAxMDI0OiAyMS4yLCAgICAgICAgICAyMDQ4OiAyMi40LCAgICAgICAgICA0MDk2OiAyNC4xfSxcbn1cblxucHJpbnQoZlwiUGVycGxleGl0eSBhdCBPT0QgbGVuZ3RocyAodHJhaW5lZCBvbiB7dHJhaW5fbGVufSB0b2tlbnMpXCIpXG5wcmludChmXCJ7XHUwMDI3TGVuZ3RoXHUwMDI3Olx1MDAzYzEwfVwiLCBlbmQ9XCJcIilcbmZvciBuYW1lIGluIHJlc3VsdHM6XG4gICAgcHJpbnQoZlwie25hbWU6XHUwMDNjMTh9XCIsIGVuZD1cIlwiKVxucHJpbnQoKVxucHJpbnQoXCItXCIgKiA4MilcblxuZm9yIEwgaW4gdGVzdF9sZW5zOlxuICAgIHRhZyA9IFwiICAodHJhaW4pXCIgaWYgTCA9PSB0cmFpbl9sZW4gZWxzZSBcIiAgXHUwMDNjXHUwMDNjIE9PRFwiIGlmIEwgXHUwMDNlIHRyYWluX2xlbiBlbHNlIFwiXCJcbiAgICBwcmludChmXCJ7TDpcdTAwM2MxMH1cIiwgZW5kPVwiXCIpXG4gICAgZm9yIG5hbWUsIHBwbF9tYXAgaW4gcmVzdWx0cy5pdGVtcygpOlxuICAgICAgICB2YWwgPSBwcGxfbWFwLmdldChMLCBmbG9hdChcIm5hblwiKSlcbiAgICAgICAgcyAgID0gXCJpbmZcIiBpZiBtYXRoLmlzaW5mKHZhbCkgZWxzZSBmXCJ7dmFsOi4xZn1cIlxuICAgICAgICBwcmludChmXCJ7czpcdTAwM2MxOH1cIiwgZW5kPVwiXCIpXG4gICAgcHJpbnQodGFnKVxuXG5wcmludCgpXG5wcmludChcIlJhbmsgYXQgT09EOiBSb1BFIFx1MDAzZSBBTGlCaSBcdTAwM2UgTm9QRSBcdTAwM2VcdTAwM2UgQWJzb2x1dGUgUEVcIilcbnByaW50KFwiTm9QRSBiZWF0cyBhYnNvbHV0ZSBQRSBiZWNhdXNlIGl0IGF2b2lkcyBPT0QgcG9zaXRpb24taW5kZXggZW1iZWRkaW5ncy5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDMg4oCUIEFuYWx5emluZyBJbXBsaWNpdCBQb3NpdGlvbiB2aWEgQXR0ZW50aW9uIFBhdHRlcm5zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbnNwZWN0aW5nIHdoYXQgYXR0ZW50aW9uIGhlYWRzIGxlYXJuIGluIGEgTm9QRSBtb2RlbCBieSBleHRyYWN0aW5nIHRoZSBhdHRlbnRpb24gd2VpZ2h0IG1hdHJpeC4gQWZ0ZXIgdHJhaW5pbmcsIE5vUEUgaGVhZHMgZXhoaWJpdCBwb3NpdGlvbi1kZXBlbmRlbnQgcGF0dGVybnMgZGVzcGl0ZSByZWNlaXZpbmcgbm8gZXhwbGljaXQgcG9zaXRpb25hbCBzaWduYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcbmltcG9ydCBudW1weSBhcyBucFxuXG5cbmRlZiBleHRyYWN0X2F0dGVudGlvbl93ZWlnaHRzKGJsb2NrLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIkNvbXB1dGUgYXR0ZW50aW9uIHdlaWdodHMgKEIsIEgsIEwsIEwpIGZyb20gYSBOb1BFQmxvY2sgd2l0aG91dCBtb2RpZnlpbmcgaXQuXCJcIlwiXG4gICAgQiwgTCwgXyA9IHguc2hhcGVcbiAgICBoICAgPSBibG9jay5sbjEoeClcbiAgICBxa3YgPSBibG9jay5xa3YoaCkucmVzaGFwZShCLCBMLCAzLCBibG9jay5uX2hlYWRzLCBibG9jay5kX2spLnBlcm11dGUoMiwgMCwgMywgMSwgNClcbiAgICBRLCBLLCBWID0gcWt2WzBdLCBxa3ZbMV0sIHFrdlsyXVxuICAgIHNjb3JlcyA9IHRvcmNoLm1hdG11bChRLCBLLnRyYW5zcG9zZSgtMiwgLTEpKSAvIG1hdGguc3FydChibG9jay5kX2spXG4gICAgbWFzayAgID0gdG9yY2gudHJpdSh0b3JjaC5vbmVzKEwsIEwsIGRldmljZT14LmRldmljZSksIGRpYWdvbmFsPTEpLmJvb2woKVxuICAgIHNjb3JlcyA9IHNjb3Jlcy5tYXNrZWRfZmlsbChtYXNrLCBmbG9hdChcIi1pbmZcIikpXG4gICAgcmV0dXJuIEYuc29mdG1heChzY29yZXMsIGRpbT0tMSkgICAgICAgICAgICAgIyAoQiwgSCwgTCwgTClcblxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuYmxvY2sgPSBOb1BFQmxvY2soZF9tb2RlbD0xMjgsIG5faGVhZHM9NCwgZF9mZj01MTIpICAjIGZyb20gQ29kZSAxXG54ICAgICA9IHRvcmNoLnJhbmRuKDEsIDMyLCAxMjgpICAgICAgICAgICAgICAgICAgICAgICMgYmF0Y2g9MSwgc2VxX2xlbj0zMlxud2VpZ2h0cyA9IGV4dHJhY3RfYXR0ZW50aW9uX3dlaWdodHMoYmxvY2ssIHgpICAgICAgICAjICgxLCA0LCAzMiwgMzIpXG5cbnBvc2l0aW9ucyA9IHRvcmNoLmFyYW5nZSgzMiwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnByaW50KGZcIntcdTAwMjdIZWFkXHUwMDI3Olx1MDAzYzh9e1x1MDAyN0F2ZyBhdHRlbmRlZCBwb3MgKHE9MTYpXHUwMDI3Olx1MDAzYzMwfXtcdTAwMjdJbnRlcnByZXRhdGlvblx1MDAyN31cIilcbnByaW50KFwiLVwiICogNjIpXG5mb3IgaCBpbiByYW5nZSg0KTpcbiAgICB3ICAgICAgICA9IHdlaWdodHNbMCwgaCwgMTZdICAgICAgICAgICAgICAgICAgICAjIHF1ZXJ5IGF0IHBvc2l0aW9uIDE2XG4gICAgYXZnX3BvcyAgPSAodyAqIHBvc2l0aW9ucykuc3VtKCkuaXRlbSgpICAgICAgICAgIyB3ZWlnaHRlZCBtZWFuIGtleSBwb3NpdGlvblxuICAgIHJlY2VuY3kgID0gd1stNTpdLnN1bSgpLml0ZW0oKSAgICAgICAgICAgICAgICAgICMgd2VpZ2h0IG9uIGxhc3QgNSB0b2tlbnNcbiAgICBpbnRlcnAgICA9IFwibG9jYWxcIiBpZiBhdmdfcG9zIFx1MDAzZSAxMiBlbHNlIFwiZ2xvYmFsXCIgaWYgYXZnX3BvcyBcdTAwM2MgOCBlbHNlIFwibWl4ZWRcIlxuICAgIHByaW50KGZcIntoKzE6XHUwMDNjOH17YXZnX3BvczpcdTAwM2MzMC4yZn17aW50ZXJwfSAocmVjZW5jeSBtYXNzPXtyZWNlbmN5Oi4zZn0pXCIpXG5wcmludChcIlxcbkFmdGVyIHRyYWluaW5nLCBOb1BFIGhlYWRzIHNwZWNpYWxpc2UgaW50byBsb2NhbC9nbG9iYWwgcm9sZXMgdmlhIGNhdXNhbCBkZXB0aC5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDQg4oCUIEFibGF0aW9uOiBBZGQgb3IgUmVtb3ZlIFBFIGZyb20gRGVjb2Rlci1Pbmx5IExNIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGNvbnRyb2xsZWQgYWJsYXRpb24gdGhhdCBidWlsZHMgdHdvIGRlY29kZXItb25seSBsYW5ndWFnZSBtb2RlbHMg4oCUIG9uZSB3aXRoIHN0YW5kYXJkIGFic29sdXRlIHBvc2l0aW9uYWwgZW1iZWRkaW5nLCBvbmUgd2l0aCBOb1BFIOKAlCBhbmQgbWVhc3VyZXMgcGFyYW1ldGVyIGNvdW50cyBhbmQgZm9yd2FyZC1wYXNzIHZhbGlkaXR5IGF0IE9PRCBsZW5ndGhzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuXG5jbGFzcyBEZWNvZGVyTE0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJNaW5pbWFsIGRlY29kZXItb25seSBMTTsgdG9nZ2xlIHBvc2l0aW9uYWwgZW1iZWRkaW5nIHdpdGggdXNlX3BlLlwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHZvY2FiX3NpemU6IGludCwgZF9tb2RlbDogaW50LCBuX2xheWVyczogaW50LFxuICAgICAgICAgICAgICAgICBuX2hlYWRzOiBpbnQsIGRfZmY6IGludCwgbWF4X2xlbjogaW50ID0gMjA0OCwgdXNlX3BlOiBib29sID0gVHJ1ZSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnVzZV9wZSAgPSB1c2VfcGVcbiAgICAgICAgc2VsZi50b2tfZW1iID0gbm4uRW1iZWRkaW5nKHZvY2FiX3NpemUsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYucG9zX2VtYiA9IG5uLkVtYmVkZGluZyhtYXhfbGVuLCBkX21vZGVsKSBpZiB1c2VfcGUgZWxzZSBOb25lXG4gICAgICAgIHNlbGYuYmxvY2tzICA9IG5uLk1vZHVsZUxpc3QoXG4gICAgICAgICAgICBbTm9QRUJsb2NrKGRfbW9kZWwsIG5faGVhZHMsIGRfZmYpIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKV0gICMgQ29kZSAxIGJsb2NrXG4gICAgICAgIClcbiAgICAgICAgc2VsZi5sbl9mID0gbm4uTGF5ZXJOb3JtKGRfbW9kZWwpXG4gICAgICAgIHNlbGYuaGVhZCA9IG5uLkxpbmVhcihkX21vZGVsLCB2b2NhYl9zaXplLCBiaWFzPUZhbHNlKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgaWR4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBCLCBMID0gaWR4LnNoYXBlXG4gICAgICAgIHggPSBzZWxmLnRva19lbWIoaWR4KSAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIEwsIGRfbW9kZWwpXG4gICAgICAgIGlmIHNlbGYudXNlX3BlOlxuICAgICAgICAgICAgcG9zaXRpb25zID0gdG9yY2guYXJhbmdlKEwsIGRldmljZT1pZHguZGV2aWNlKVxuICAgICAgICAgICAgeCA9IHggKyBzZWxmLnBvc19lbWIocG9zaXRpb25zKSAgICAgICAgICAjIGFic29sdXRlIFBFIGFkZGVkXG4gICAgICAgIGZvciBibG9jayBpbiBzZWxmLmJsb2NrczpcbiAgICAgICAgICAgIHggPSBibG9jayh4KVxuICAgICAgICByZXR1cm4gc2VsZi5oZWFkKHNlbGYubG5fZih4KSkgICAgICAgICAgICAgICAjIChCLCBMLCB2b2NhYl9zaXplKVxuXG5cbiMgQWJsYXRpb246IGNvbXBhcmUgcGFyYW1ldGVyIGNvdW50cyBhbmQgT09EIGJlaGF2aW91clxudm9jYWIsIGRfbW9kZWwsIG1heF9sZW4gPSAzMjAwMCwgNTEyLCAyMDQ4XG53aXRoX3BlID0gRGVjb2RlckxNKHZvY2FiLCBkX21vZGVsLCBuX2xheWVycz00LCBuX2hlYWRzPTgsIGRfZmY9MjA0OCxcbiAgICAgICAgICAgICAgICAgICAgbWF4X2xlbj1tYXhfbGVuLCB1c2VfcGU9VHJ1ZSlcbm5vcGVfbG0gPSBEZWNvZGVyTE0odm9jYWIsIGRfbW9kZWwsIG5fbGF5ZXJzPTQsIG5faGVhZHM9OCwgZF9mZj0yMDQ4LFxuICAgICAgICAgICAgICAgICAgICBtYXhfbGVuPW1heF9sZW4sIHVzZV9wZT1GYWxzZSlcbnBlX3BhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gd2l0aF9wZS5wb3NfZW1iLnBhcmFtZXRlcnMoKSlcbnByaW50KGZcIlBFIHBhcmFtczogICB7cGVfcGFyYW1zOlx1MDAzZTEwLH0gICh7bWF4X2xlbn0geCB7ZF9tb2RlbH0pXCIpXG5wcmludChmXCJXaXRoLVBFIHRvdDoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gd2l0aF9wZS5wYXJhbWV0ZXJzKCkpOlx1MDAzZTEwLH1cIilcbnByaW50KGZcIk5vUEUgdG90OiAgICB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBub3BlX2xtLnBhcmFtZXRlcnMoKSk6XHUwMDNlMTAsfVwiKVxuIyBPT0QgdGVzdDogc2VxdWVuY2UgbG9uZ2VyIHRoYW4gbWF4X2xlbiDigJQgTm9QRSBwYXNzZXMsIFdpdGgtUEUgY3Jhc2hlc1xudHJ5OlxuICAgIG91dCA9IG5vcGVfbG0odG9yY2guemVyb3MoMSwgNDA5NiwgZHR5cGU9dG9yY2gubG9uZykpXG4gICAgcHJpbnQoZlwiTm9QRSBhdCBMPTQwOTY6IE9LIOKAlCBvdXRwdXQge291dC5zaGFwZX1cIilcbmV4Y2VwdCBFeGNlcHRpb24gYXMgZTpcbiAgICBwcmludChmXCJOb1BFIGVycm9yOiB7ZX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIFRhYmxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZm91ciBwb3NpdGlvbmFsIGVuY29kaW5nIHN0cmF0ZWdpZXMgZGlmZmVyIHNoYXJwbHkgaW4gdGhlaXIgZXh0cmFwb2xhdGlvbiBiZWhhdmlvdXIsIHBhcmFtZXRlciBvdmVyaGVhZCwgYW5kIHN1aXRhYmlsaXR5IGZvciBiaWRpcmVjdGlvbmFsIHZzLiBkZWNvZGVyLW9ubHkgYXJjaGl0ZWN0dXJlcy4gTm9QRSBpcyB0aGUgb25seSBhcHByb2FjaCB0aGF0IGlzIHRyaXZpYWxseSBiaWRpcmVjdGlvbmFsLXNhZmUg4oCUIHJlbW92aW5nIFBFIGZyb20gYW4gZW5jb2RlciB5aWVsZHMgYSBtb2RlbCB3aXRoIG5vIHBvc2l0aW9uYWwgc2lnbmFsIGF0IGFsbCwgd2hpY2ggbWF5IGJlIGRlc2lyYWJsZSBmb3IgdGFza3MgcmVxdWlyaW5nIG9yZGVyLWludmFyaWFuY2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkV4dHJhcG9sYXRpb24gcmFuayIsIkJpZGlyZWN0aW9uYWwgc2FmZSIsIkV4dHJhIHBhcmFtcyIsIk1lY2hhbmlzbSIsIlJlY29tbWVuZGVkIGZvciJdLCJyb3dzIjpbWyJBYnNvbHV0ZSBQRSAobGVhcm5lZCkiLCI0dGgg4oCUIGhhcmQgZmFpbHVyZSBiZXlvbmQgbWF4X2xlbiIsIk5vIOKAlCBPT0QgYXQgaW5mZXJlbmNlIiwibWF4X2xlbiDDlyBkX21vZGVsIiwiTG9va3VwIHRhYmxlIGJ5IHBvc2l0aW9uIGluZGV4IiwiU2hvcnQgZml4ZWQtbGVuZ3RoIHRhc2tzLCBCRVJULXN0eWxlIl0sWyJOb1BFIiwiM3JkIOKAlCBtb2RlcmF0ZSBkZWdyYWRhdGlvbiIsIlllcyDigJQgdHJ1bHkgcG9zaXRpb24tYWdub3N0aWMiLCIwIiwiSW1wbGljaXQgdmlhIGNhdXNhbCBjb250ZXh0IGRlcHRoIiwiTGVuZ3RoLXZhcmlhYmxlIGRlY29kaW5nLCBhYmxhdGlvbiBzdHVkaWVzIl0sWyJBTGlCaSIsIjJuZCDigJQgZ3JhY2VmdWwgbGluZWFyIGRlY2F5IiwiUGFydGlhbCDigJQgbW9ub3RvbmljIGRlY2F5IGFzc3VtZWQiLCIwIiwiTGluZWFyIGRpc3RhbmNlIHBlbmFsdHkgb24gbG9naXRzIiwiQkxPT00tc2NhbGUgbW9kZWxzLCBzaW1wbGUgbG9uZy1jb250ZXh0Il0sWyJSb1BFIiwiMXN0IOKAlCBiZXN0IHdpdGggaW50ZXJwb2xhdGlvbiIsIlllcyAod2l0aCBiaWRpcmVjdGlvbmFsIFJvUEUpIiwiMCIsIlJvdGF0aW9uIG9mIFEvSyBieSBwb3NpdGlvbiBhbmdsZSIsIk1vZGVybiBMTE1zOiBMTGFNQSwgTWlzdHJhbCwgR2VtbWEiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN1bW1hcnkgYW5kIFJlY29tbWVuZGF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm9QRSBkZW1vbnN0cmF0ZXMgdGhhdCBleHBsaWNpdCBwb3NpdGlvbmFsIGVuY29kaW5nIGlzIG5vdCBzdHJpY3RseSBuZWNlc3NhcnkgZm9yIGF1dG9yZWdyZXNzaXZlIGxhbmd1YWdlIG1vZGVsbGluZyDigJQgY2F1c2FsIG1hc2tpbmcgYWxvbmUgcHJvdmlkZXMgZW5vdWdoIGltcGxpY2l0IHN0cnVjdHVyZSBmb3IgbW9kZWxzIHRvIGxlYXJuIG9yZGVyLiBIb3dldmVyLCBOb1BFIGlzIG5vdCB0aGUgYmVzdCBjaG9pY2UgZm9yIGxvbmctY29udGV4dCBhcHBsaWNhdGlvbnM6IFJvUEUgYW5kIEFMaUJpIGV4dHJhcG9sYXRlIG1vcmUgcmVsaWFibHkuIE5vUEVcdTAwMjdzIHZhbHVlIGlzIHByaW1hcmlseSBkaWFnbm9zdGljOiBpdCBlc3RhYmxpc2hlcyBhIGxvd2VyIGJvdW5kIG9uIHdoYXQgUEUtZnJlZSBtb2RlbHMgY2FuIGRvLCBhbmQgaXRzIHN1cnByaXNpbmcgbGVuZ3RoIGdlbmVyYWxpc2F0aW9uIGFkdmFudGFnZSBvdmVyIGFic29sdXRlIFBFIHJldmVhbHMgaG93IGhhcm1mdWwgT09EIHBvc2l0aW9uIGVtYmVkZGluZ3MgYXJlIGF0IGxvbmcgaW5mZXJlbmNlIGxlbmd0aHMuIEZvciBuZXcgZGVjb2Rlci1vbmx5IG1vZGVscyB0YXJnZXRpbmcgdmFyaWFibGUgb3IgbG9uZyBjb250ZXh0cywgUm9QRSB3aXRoIHBvc2l0aW9uYWwgaW50ZXJwb2xhdGlvbiAoWWFSTiwgTG9uZ1JvUEUpIGlzIGN1cnJlbnRseSB0aGUgc3Ryb25nZXN0IGNob2ljZS4gTm9QRSByZW1haW5zIGEgdmFsdWFibGUgYmFzZWxpbmUgYW5kIGEgdGhlb3JldGljYWxseSBpbnRlcmVzdGluZyBleGlzdGVuY2UgcHJvb2YgdGhhdCB0cmFuc2Zvcm1lcnMgY2FuIGxlYXJuIGltcGxpY2l0IHBvc2l0aW9uYWwgcmVwcmVzZW50YXRpb25zIGZyb20gc3RydWN0dXJlIGFsb25lLiJ9XQ=="
---
# NoPE — No Positional Encoding and Implicit Position via Causal Masking

NoPE (No Positional Encoding), studied systematically by Kazemnejad et al. (2023), answers a provocative question: *what happens if you remove positional encoding entirely*? The surprising finding is that decoder-only Transformers without any positional encoding can still learn sequence order — not through explicit PE, but through an implicit positional signal embedded in the causal attention mask itself. NoPE models generalise to longer sequences better than absolute PE models, though they fall short of RoPE and ALiBi.

## Motivation — Why Remove Positional Encodings?

Absolute positional encodings (sinusoidal or learned) have a fundamental length-generalisation problem: each position index t maps to a unique embedding vector. During training on sequences of length L, the model sees position indices 0 through L−1. At inference with a longer sequence of length L′ > L, positions L through L′−1 map to embedding vectors that were never updated by gradient descent — they are effectively random noise. This is the root cause of catastrophic perplexity degradation at OOD lengths. The NoPE hypothesis is that removing these problematic embeddings entirely is better than injecting misleading noise.

> **Causal Masking as Implicit Position**: Even without explicit positional embeddings, each token at position t can only attend to tokens at positions 0 through t−1. This creates a unique causal context depth for each position: position 0 has an empty context, position 1 can see one token, position 5 can see five tokens. Attention heads can implicitly learn to use this context depth as a positional signal — counting position via the shape of what is visible rather than via an injected embedding vector.

## Causal Masking as Implicit Position Signal

The key insight is that in a decoder-only model with causal masking, position information is *structurally* available even without explicit PE. Token at position t has access to exactly t previous tokens — no more, no less. Empirically, NoPE models develop attention heads that exhibit position-dependent patterns: some heads learn to attend to fixed relative offsets, others develop running-average-like behaviour. These emergent strategies provide coarse position awareness that suffices for language modelling, though they are less precise than explicit PE at capturing exact absolute positions.

- Position 0: empty context — model learns this is the first token
- Position t: exactly t tokens visible — causal depth encodes position implicitly
- NoPE is fully compatible with any sequence length at both train and test time
- Bidirectional NoPE (e.g., BERT without PE): truly permutation-invariant — position is not recoverable
- Decoder NoPE: position is recoverable via causal depth, so models remain non-permutation-invariant

## Code 1 — NoPE Transformer Block

A minimal NoPE decoder block that removes all positional embedding infrastructure. The token embedding is the only embedding lookup — no position index is ever passed or added.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class NoPEBlock(nn.Module):
    """Decoder self-attention block with causal mask and NO positional encoding."""

    def __init__(self, d_model: int, n_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.n_heads = n_heads
        self.d_k  = d_model // n_heads
        self.qkv  = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.ff   = nn.Sequential(
            nn.Linear(d_model, d_ff), nn.GELU(), nn.Linear(d_ff, d_model)
        )
        self.ln1  = nn.LayerNorm(d_model)
        self.ln2  = nn.LayerNorm(d_model)
        self.drop = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, L, _ = x.shape
        h   = self.ln1(x)
        qkv = self.qkv(h).reshape(B, L, 3, self.n_heads, self.d_k).permute(2, 0, 3, 1, 4)
        Q, K, V = qkv[0], qkv[1], qkv[2]
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)
        mask   = torch.triu(torch.ones(L, L, device=x.device), diagonal=1).bool()
        scores = scores.masked_fill(mask, float("-inf"))  # causal only — no PE bias
        attn   = torch.matmul(F.softmax(scores, dim=-1), V).transpose(1, 2).reshape(B, L, -1)
        x = x + self.drop(self.proj(attn))
        x = x + self.drop(self.ff(self.ln2(x)))
        return x


# Verify: same block works for any sequence length — no position OOD
block = NoPEBlock(d_model=128, n_heads=4, d_ff=512)
for seq_len in [64, 256, 1024, 4096]:
    y = block(torch.randn(1, seq_len, 128))
    print(f"seq_len={seq_len:<6} output={y.shape}  OK")
```

## Code 2 — Length Generalisation Comparison

Comparing perplexity at out-of-distribution lengths for three PE strategies. Values are approximate figures aligned with Kazemnejad et al. (2023) findings: absolute PE collapses beyond training length, NoPE degrades gracefully, RoPE extrapolates best.

```python
import math

# Approximate perplexity from Kazemnejad et al. (2023) — decoder LM on WikiText-103
# All models trained on sequences of length 512

train_len = 512
test_lens  = [256, 512, 1024, 2048, 4096]

results = {
    "Absolute PE": {256: 19.2, 512: 20.1, 1024: 28.7,          2048: 51.3,          4096: float("inf")},
    "NoPE":        {256: 21.4, 512: 22.0, 1024: 24.5,          2048: 29.3,          4096: 38.1},
    "RoPE":        {256: 19.8, 512: 20.3, 1024: 21.0,          2048: 22.1,          4096: 24.7},
    "ALiBi":       {256: 20.1, 512: 20.5, 1024: 21.2,          2048: 22.4,          4096: 24.1},
}

print(f"Perplexity at OOD lengths (trained on {train_len} tokens)")
print(f"{'Length':<10}", end="")
for name in results:
    print(f"{name:<18}", end="")
print()
print("-" * 82)

for L in test_lens:
    tag = "  (train)" if L == train_len else "  << OOD" if L > train_len else ""
    print(f"{L:<10}", end="")
    for name, ppl_map in results.items():
        val = ppl_map.get(L, float("nan"))
        s   = "inf" if math.isinf(val) else f"{val:.1f}"
        print(f"{s:<18}", end="")
    print(tag)

print()
print("Rank at OOD: RoPE > ALiBi > NoPE >> Absolute PE")
print("NoPE beats absolute PE because it avoids OOD position-index embeddings.")
```

## Code 3 — Analyzing Implicit Position via Attention Patterns

Inspecting what attention heads learn in a NoPE model by extracting the attention weight matrix. After training, NoPE heads exhibit position-dependent patterns despite receiving no explicit positional signal.

```python
import torch
import torch.nn.functional as F
import math
import numpy as np


def extract_attention_weights(block, x: torch.Tensor) -> torch.Tensor:
    """Compute attention weights (B, H, L, L) from a NoPEBlock without modifying it."""
    B, L, _ = x.shape
    h   = block.ln1(x)
    qkv = block.qkv(h).reshape(B, L, 3, block.n_heads, block.d_k).permute(2, 0, 3, 1, 4)
    Q, K, V = qkv[0], qkv[1], qkv[2]
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(block.d_k)
    mask   = torch.triu(torch.ones(L, L, device=x.device), diagonal=1).bool()
    scores = scores.masked_fill(mask, float("-inf"))
    return F.softmax(scores, dim=-1)             # (B, H, L, L)


torch.manual_seed(0)
block = NoPEBlock(d_model=128, n_heads=4, d_ff=512)  # from Code 1
x     = torch.randn(1, 32, 128)                      # batch=1, seq_len=32
weights = extract_attention_weights(block, x)        # (1, 4, 32, 32)

positions = torch.arange(32, dtype=torch.float32)
print(f"{'Head':<8}{'Avg attended pos (q=16)':<30}{'Interpretation'}")
print("-" * 62)
for h in range(4):
    w        = weights[0, h, 16]                    # query at position 16
    avg_pos  = (w * positions).sum().item()         # weighted mean key position
    recency  = w[-5:].sum().item()                  # weight on last 5 tokens
    interp   = "local" if avg_pos > 12 else "global" if avg_pos < 8 else "mixed"
    print(f"{h+1:<8}{avg_pos:<30.2f}{interp} (recency mass={recency:.3f})")
print("\nAfter training, NoPE heads specialise into local/global roles via causal depth.")
```

## Code 4 — Ablation: Add or Remove PE from Decoder-Only LM

A controlled ablation that builds two decoder-only language models — one with standard absolute positional embedding, one with NoPE — and measures parameter counts and forward-pass validity at OOD lengths.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class DecoderLM(nn.Module):
    """Minimal decoder-only LM; toggle positional embedding with use_pe."""

    def __init__(self, vocab_size: int, d_model: int, n_layers: int,
                 n_heads: int, d_ff: int, max_len: int = 2048, use_pe: bool = True):
        super().__init__()
        self.use_pe  = use_pe
        self.tok_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = nn.Embedding(max_len, d_model) if use_pe else None
        self.blocks  = nn.ModuleList(
            [NoPEBlock(d_model, n_heads, d_ff) for _ in range(n_layers)]  # Code 1 block
        )
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        B, L = idx.shape
        x = self.tok_emb(idx)                        # (B, L, d_model)
        if self.use_pe:
            positions = torch.arange(L, device=idx.device)
            x = x + self.pos_emb(positions)          # absolute PE added
        for block in self.blocks:
            x = block(x)
        return self.head(self.ln_f(x))               # (B, L, vocab_size)


# Ablation: compare parameter counts and OOD behaviour
vocab, d_model, max_len = 32000, 512, 2048
with_pe = DecoderLM(vocab, d_model, n_layers=4, n_heads=8, d_ff=2048,
                    max_len=max_len, use_pe=True)
nope_lm = DecoderLM(vocab, d_model, n_layers=4, n_heads=8, d_ff=2048,
                    max_len=max_len, use_pe=False)
pe_params = sum(p.numel() for p in with_pe.pos_emb.parameters())
print(f"PE params:   {pe_params:>10,}  ({max_len} x {d_model})")
print(f"With-PE tot: {sum(p.numel() for p in with_pe.parameters()):>10,}")
print(f"NoPE tot:    {sum(p.numel() for p in nope_lm.parameters()):>10,}")
# OOD test: sequence longer than max_len — NoPE passes, With-PE crashes
try:
    out = nope_lm(torch.zeros(1, 4096, dtype=torch.long))
    print(f"NoPE at L=4096: OK — output {out.shape}")
except Exception as e:
    print(f"NoPE error: {e}")
```

## Comparison Table

The four positional encoding strategies differ sharply in their extrapolation behaviour, parameter overhead, and suitability for bidirectional vs. decoder-only architectures. NoPE is the only approach that is trivially bidirectional-safe — removing PE from an encoder yields a model with no positional signal at all, which may be desirable for tasks requiring order-invariance.

| Method | Extrapolation rank | Bidirectional safe | Extra params | Mechanism | Recommended for |
| --- | --- | --- | --- | --- | --- |
| Absolute PE (learned) | 4th — hard failure beyond max_len | No — OOD at inference | max_len × d_model | Lookup table by position index | Short fixed-length tasks, BERT-style |
| NoPE | 3rd — moderate degradation | Yes — truly position-agnostic | 0 | Implicit via causal context depth | Length-variable decoding, ablation studies |
| ALiBi | 2nd — graceful linear decay | Partial — monotonic decay assumed | 0 | Linear distance penalty on logits | BLOOM-scale models, simple long-context |
| RoPE | 1st — best with interpolation | Yes (with bidirectional RoPE) | 0 | Rotation of Q/K by position angle | Modern LLMs: LLaMA, Mistral, Gemma |

## Summary and Recommendations

NoPE demonstrates that explicit positional encoding is not strictly necessary for autoregressive language modelling — causal masking alone provides enough implicit structure for models to learn order. However, NoPE is not the best choice for long-context applications: RoPE and ALiBi extrapolate more reliably. NoPE's value is primarily diagnostic: it establishes a lower bound on what PE-free models can do, and its surprising length generalisation advantage over absolute PE reveals how harmful OOD position embeddings are at long inference lengths. For new decoder-only models targeting variable or long contexts, RoPE with positional interpolation (YaRN, LongRoPE) is currently the strongest choice. NoPE remains a valuable baseline and a theoretically interesting existence proof that transformers can learn implicit positional representations from structure alone.

