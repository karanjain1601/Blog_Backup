---
title: "Noisy Channel Model and Shannon's Coding Theorem"
slug: "noisychannel-shannons-theorem"
description: "Shannon's channel coding theorem establishes that reliable communication is possible at any rate below channel capacity C, and impossible above it. Covers BSC, AWGN, capacity bounds, and connections to noisy-label learning."
tags: ["information-theory", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2hhbm5vblx1MDAyN3MgMTk0OCBwYXBlciBcdTAwMjdBIE1hdGhlbWF0aWNhbCBUaGVvcnkgb2YgQ29tbXVuaWNhdGlvblx1MDAyNyBpcyBhcmd1YWJseSB0aGUgbW9zdCBpbXBvcnRhbnQgcGFwZXIgaW4gMjB0aC1jZW50dXJ5IGVuZ2luZWVyaW5nLiBJdHMgY2VudHJhbCByZXN1bHQg4oCUIHRoZSBjaGFubmVsIGNvZGluZyB0aGVvcmVtIOKAlCBzaG93ZWQgdGhhdCByZWxpYWJsZSBjb21tdW5pY2F0aW9uIG92ZXIgYSBub2lzeSBjaGFubmVsIGlzIGFsd2F5cyBwb3NzaWJsZSBhcyBsb25nIGFzIHRoZSBpbmZvcm1hdGlvbiByYXRlIHN0YXlzIGJlbG93IGEgZmluaXRlIHRocmVzaG9sZCBjYWxsZWQgY2hhbm5lbCBjYXBhY2l0eS4gVGhpcyB3YXMgZGVlcGx5IGNvdW50ZXItaW50dWl0aXZlOiBlbmdpbmVlcnMgb2YgdGhlIHRpbWUgYmVsaWV2ZWQgbm9pc2UgZnVuZGFtZW50YWxseSBsaW1pdGVkIHJlbGlhYmlsaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBTaGFubm9uIENvbW11bmljYXRpb24gTW9kZWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNoYW5ub25cdTAwMjdzIG1vZGVsIGhhcyBmaXZlIGNvbXBvbmVudHM6XG4xLiBTb3VyY2Ug4oCUIGdlbmVyYXRlcyBhIG1lc3NhZ2UgTSBmcm9tIGEgbWVzc2FnZSBzZXRcbjIuIEVuY29kZXIg4oCUIG1hcHMgTSB0byBhIGNvZGV3b3JkIHhebiBmcm9tIHRoZSBjaGFubmVsIGFscGhhYmV0XG4zLiBDaGFubmVsIOKAlCBtYXBzIHhebiB0byB5Xm4gd2l0aCBub2lzZSAocHJvYmFiaWxpc3RpYyBtYXBwaW5nIFAoeXx4KSlcbjQuIERlY29kZXIg4oCUIG1hcHMgeV5uIGJhY2sgdG8gYW4gZXN0aW1hdGUgTcyCIG9mIE1cbjUuIFJlY2VpdmVyIOKAlCB1c2VzIE3MglxuXG5UaGUgZ29hbDogY2hvb3NlIGVuY29kZXIvZGVjb2RlciBwYWlycyBzdWNoIHRoYXQgUChNzIIg4omgIE0pIOKGkiAwIGFzIGJsb2NrIGxlbmd0aCBuIOKGkiDiiJ4sIHdoaWxlIHRyYW5zbWl0dGluZyBhcyBtYW55IGJpdHMgcGVyIGNoYW5uZWwgdXNlIGFzIHBvc3NpYmxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNoYW5uZWwgQ2FwYWNpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjaGFubmVsIGNhcGFjaXR5IEMgaXMgdGhlIG1heGltdW0gbXV0dWFsIGluZm9ybWF0aW9uIGJldHdlZW4gaW5wdXQgYW5kIG91dHB1dCwgb3B0aW1pemVkIG92ZXIgYWxsIGlucHV0IGRpc3RyaWJ1dGlvbnM6XG5cbkMgPSBtYXhfe1AoWCl9IEkoWDtZKVxuXG5DYXBhY2l0eSBoYXMgdW5pdHMgb2YgYml0cyBwZXIgY2hhbm5lbCB1c2UuIFRoZSBvcHRpbWl6YXRpb24gaXMgb3ZlciBQKFgpIOKAlCB0aGUgY2hvaWNlIG9mIGlucHV0IGRpc3RyaWJ1dGlvbiDigJQgYmVjYXVzZSB3ZSBjb250cm9sIHdoYXQgd2Ugc2VuZCBidXQgbm90IHRoZSBjaGFubmVsXHUwMDI3cyBub2lzZSBiZWhhdmlvci4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQ2hhbm5lbCBNb2RlbCIsIkRlc2NyaXB0aW9uIiwiQ2FwYWNpdHkgRm9ybXVsYSIsIkV4YW1wbGUgVmFsdWUiXSwicm93cyI6W1siQmluYXJ5IFN5bW1ldHJpYyBDaGFubmVsIChCU0MpIiwiQml0IGZsaXBwZWQgd2l0aCBwcm9iIHAiLCJDID0gMSDiiJIgSF9iKHApIiwicD0wLjE6IEPiiYgwLjUzMSBiaXRzL3VzZSJdLFsiQmluYXJ5IEVyYXN1cmUgQ2hhbm5lbCAoQkVDKSIsIkJpdCBlcmFzZWQgd2l0aCBwcm9iIM61IiwiQyA9IDEg4oiSIM61IiwizrU9MC4yOiBDPTAuOCBiaXRzL3VzZSJdLFsiQVdHTiIsIkdhdXNzaWFuIG5vaXNlIHdpdGggdmFyaWFuY2Ugz4PCsiIsIkMgPSDCvSBsb2figoIoMSArIFAvz4PCsikiLCJTTlI9MTBkQjogQ+KJiDMuNDYgYml0cy91c2UiXSxbIlotQ2hhbm5lbCIsIjDihpIwIGFsd2F5cywgMeKGkjAgd2l0aCBwcm9iIHAiLCJDID0gbG9n4oKCKDEgKyAoMeKIknApwrcyXnviiJJIX2IocC8oMSsoMeKIknApKSl9KSIsIkFzeW1tZXRyaWMsIHVzZWQgaW4gb3B0aWNhbCJdLFsiRGlzY3JldGUgTWVtb3J5bGVzcyAoZ2VuZXJhbCkiLCJBbnkgUCh5fHgpIiwibWF4X3tQKFgpfSBJKFg7WSkiLCJDb21wdXRlZCBudW1lcmljYWxseSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmluYXJ5IFN5bW1ldHJpYyBDaGFubmVsIOKAlCBDYXBhY2l0eSBhbmQgU2ltdWxhdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3BlY2lhbCBpbXBvcnQgZW50clxuXG5kZWYgYmluYXJ5X2VudHJvcHkocDogZmxvYXQpIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiQmluYXJ5IGVudHJvcHkgZnVuY3Rpb24gSF9iKHApID0gLXAgbG9nMihwKSAtICgxLXApIGxvZzIoMS1wKS5cIlwiXCJcbiAgICBpZiBwIFx1MDAzYz0gMCBvciBwIFx1MDAzZT0gMTpcbiAgICAgICAgcmV0dXJuIDAuMFxuICAgIHJldHVybiAtcCAqIG5wLmxvZzIocCkgLSAoMSAtIHApICogbnAubG9nMigxIC0gcClcblxuZGVmIGJzY19jYXBhY2l0eShwOiBmbG9hdCkgLVx1MDAzZSBmbG9hdDpcbiAgICBcIlwiXCJDYXBhY2l0eSBvZiBCaW5hcnkgU3ltbWV0cmljIENoYW5uZWwgd2l0aCBjcm9zc292ZXIgcHJvYmFiaWxpdHkgcC5cIlwiXCJcbiAgICByZXR1cm4gMS4wIC0gYmluYXJ5X2VudHJvcHkocClcblxuZGVmIHNpbXVsYXRlX2JzYyhtZXNzYWdlX2JpdHM6IG5wLm5kYXJyYXksIHA6IGZsb2F0KSAtXHUwMDNlIG5wLm5kYXJyYXk6XG4gICAgXCJcIlwiU2ltdWxhdGUgQlNDOiBmbGlwIGVhY2ggYml0IGluZGVwZW5kZW50bHkgd2l0aCBwcm9iYWJpbGl0eSBwLlwiXCJcIlxuICAgIGZsaXBzID0gbnAucmFuZG9tLmJpbm9taWFsKDEsIHAsIHNpemU9bWVzc2FnZV9iaXRzLnNoYXBlKVxuICAgIHJldHVybiAobWVzc2FnZV9iaXRzICsgZmxpcHMpICUgMiAgIyBYT1JcblxuIyBDYXBhY2l0eSBhdCBrZXkgY3Jvc3NvdmVyIHByb2JhYmlsaXRpZXNcbnByaW50KFwiQlNDIGNhcGFjaXR5IEMgPSAxIC0gSF9iKHApOlwiKVxuZm9yIHAgaW4gWzAuMCwgMC4wMSwgMC4wNSwgMC4xLCAwLjIsIDAuNV06XG4gICAgYyA9IGJzY19jYXBhY2l0eShwKVxuICAgIHByaW50KGZcIiAgcCA9IHtwOi4yZn06IEMgPSB7YzouNGZ9IGJpdHMvdXNlXCIpXG5cbiMgU2hvdyB0aGF0IGNhcGFjaXR5IGlzIG1heGltaXplZCBieSB1bmlmb3JtIGlucHV0IChwKFg9MCkgPSBwKFg9MSkgPSAwLjUpXG5wcmludChcIlxcbkNhcGFjaXR5IGFjaGlldmVkIGF0IHVuaWZvcm0gaW5wdXQgZGlzdHJpYnV0aW9uXCIpXG5wcmludChmXCIgIEF0IHA9MC4xLCBCU0MgY2FwYWNpdHkgPSB7YnNjX2NhcGFjaXR5KDAuMSk6LjRmfSBiaXRzXCIpXG5wcmludChmXCIgIEdhcCBmcm9tIDEgYml0ID0gezEuMCAtIGJzY19jYXBhY2l0eSgwLjEpOi40Zn0gYml0cyAoY29zdCBvZiBub2lzZSlcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXBldGl0aW9uIENvZGVzIHZzIENoYW5uZWwgQ2FwYWNpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzaW1wbGVzdCBlcnJvci1jb3JyZWN0aW5nIGNvZGUgaXMgdGhlIHJlcGV0aXRpb24gY29kZTogc2VuZCBlYWNoIGJpdCBuIHRpbWVzIGFuZCBkZWNvZGUgYnkgbWFqb3JpdHkgdm90ZS4gVGhpcyBzaG93cyBjb25jcmV0ZWx5IGhvdyByYXRlIGFuZCByZWxpYWJpbGl0eSB0cmFkZSBvZmYgYXJvdW5kIGNhcGFjaXR5LiBCZWxvdyBjYXBhY2l0eSAocmF0ZSBSIFx1MDAzYyBDKSwgQkVSIOKGkiAwIGFzIG4gZ3Jvd3MuIEFib3ZlIGNhcGFjaXR5LCBCRVIgc3RheXMgYm91bmRlZCBhd2F5IGZyb20gMC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiByZXBldGl0aW9uX2NvZGVfYmVyKFxuICAgIHBfY2hhbm5lbDogZmxvYXQsXG4gICAgbl9yZXBlYXRzX2xpc3Q6IGxpc3QsXG4gICAgbl90cmlhbHM6IGludCA9IDUwMDAsXG4gICAgbl9iaXRzOiBpbnQgPSAyMDBcbikgLVx1MDAzZSBOb25lOlxuICAgIFwiXCJcIlNpbXVsYXRlIHJlcGV0aXRpb24gY29kZSBwZXJmb3JtYW5jZSB2cyBjaGFubmVsIGNhcGFjaXR5IG9uIEJTQy5cblxuICAgIERlbW9uc3RyYXRlcyBTaGFubm9uXHUwMDI3cyB0aGVvcmVtOiByYXRlIFx1MDAzYyBDIGFjaGlldmVzIGxvdyBCRVI7IHJhdGUgXHUwMDNlIEMgZmFpbHMuXG5cbiAgICBBcmdzOlxuICAgICAgICBwX2NoYW5uZWw6IEJTQyBjcm9zc292ZXIgcHJvYmFiaWxpdHkgKG5vaXNlIGxldmVsKS5cbiAgICAgICAgbl9yZXBlYXRzX2xpc3Q6IExpc3Qgb2YgcmVwZXRpdGlvbiBmYWN0b3JzIHRvIHRlc3QuXG4gICAgICAgIG5fdHJpYWxzOiBOdW1iZXIgb2YgTW9udGUgQ2FybG8gdHJpYWxzLlxuICAgICAgICBuX2JpdHM6IE51bWJlciBvZiBpbmZvcm1hdGlvbiBiaXRzIHBlciB0cmlhbC5cbiAgICBcIlwiXCJcbiAgICBjYXBhY2l0eSA9IDEuMCAtIGJpbmFyeV9lbnRyb3B5KHBfY2hhbm5lbClcbiAgICBwcmludChmXCJDaGFubmVsOiBCU0MocD17cF9jaGFubmVsfSksIENhcGFjaXR5IEMgPSB7Y2FwYWNpdHk6LjRmfSBiaXRzL3VzZVwiKVxuICAgIHByaW50KGZcIlxcbntcdTAwMjduX3JlcGVhdHNcdTAwMjc6XHUwMDNlMTB9IHtcdTAwMjdSYXRlXHUwMDI3Olx1MDAzZTh9IHtcdTAwMjdcdTAwM2MgQz9cdTAwMjc6XHUwMDNlNn0ge1x1MDAyN0JFUlx1MDAyNzpcdTAwM2UxMn0ge1x1MDAyN1JlbGlhYmxlP1x1MDAyNzpcdTAwM2UxMH1cIilcbiAgICBwcmludChcIi1cIiAqIDUwKVxuXG4gICAgZm9yIG5fcmVwZWF0cyBpbiBuX3JlcGVhdHNfbGlzdDpcbiAgICAgICAgcmF0ZSA9IDEuMCAvIG5fcmVwZWF0c1xuICAgICAgICB0b3RhbF9lcnJvcnMgPSAwXG5cbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl90cmlhbHMpOlxuICAgICAgICAgICAgbXNnID0gbnAucmFuZG9tLnJhbmRpbnQoMCwgMiwgbl9iaXRzKVxuICAgICAgICAgICAgZW5jb2RlZCA9IG5wLnJlcGVhdChtc2csIG5fcmVwZWF0cykgICAgICAgICAjIG5fcmVwZWF0cyAqIG5fYml0cyBzeW1ib2xzIHNlbnRcbiAgICAgICAgICAgIGZsaXBzID0gbnAucmFuZG9tLmJpbm9taWFsKDEsIHBfY2hhbm5lbCwgZW5jb2RlZC5zaGFwZSlcbiAgICAgICAgICAgIHJlY2VpdmVkID0gKGVuY29kZWQgKyBmbGlwcykgJSAyXG4gICAgICAgICAgICAjIE1ham9yaXR5IHZvdGU6IHN1bSBvdmVyIHJlcGVhdHMsIHRocmVzaG9sZCBhdCAwLjVcbiAgICAgICAgICAgIGRlY29kZWQgPSAocmVjZWl2ZWQucmVzaGFwZShuX2JpdHMsIG5fcmVwZWF0cykubWVhbihheGlzPTEpIFx1MDAzZSAwLjUpLmFzdHlwZShpbnQpXG4gICAgICAgICAgICB0b3RhbF9lcnJvcnMgKz0gbnAuc3VtKGRlY29kZWQgIT0gbXNnKVxuXG4gICAgICAgIGJlciA9IHRvdGFsX2Vycm9ycyAvIChuX3RyaWFscyAqIG5fYml0cylcbiAgICAgICAgYmVsb3dfY2FwID0gXCJZRVNcIiBpZiByYXRlIFx1MDAzYyBjYXBhY2l0eSBlbHNlIFwiTk8gXCJcbiAgICAgICAgcmVsaWFibGUgPSBcIllFU1wiIGlmIGJlciBcdTAwM2MgMC4wMSBlbHNlIFwiTk8gXCJcbiAgICAgICAgcHJpbnQoZlwie25fcmVwZWF0czpcdTAwM2UxMH0ge3JhdGU6XHUwMDNlOC40Zn0ge2JlbG93X2NhcDpcdTAwM2U2fSB7YmVyOlx1MDAzZTEyLjZmfSB7cmVsaWFibGU6XHUwMDNlMTB9XCIpXG5cbiMgQlNDIHdpdGggcD0wLjEg4oaSIEMg4omIIDAuNTMxIGJpdHMvdXNlXG5yZXBldGl0aW9uX2NvZGVfYmVyKFxuICAgIHBfY2hhbm5lbD0wLjEsXG4gICAgbl9yZXBlYXRzX2xpc3Q9WzEsIDIsIDMsIDUsIDcsIDExLCAyMV1cbikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaGFubm9uXHUwMDI3cyBDaGFubmVsIENvZGluZyBUaGVvcmVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiIqKkFjaGlldmFiaWxpdHkgKFIgXHUwMDNjIEMpOioqIEZvciBhbnkgcmF0ZSBSIFx1MDAzYyBDLCB0aGVyZSBleGlzdHMgYSBzZXF1ZW5jZSBvZiAoMl57blJ9LCBuKSBjb2RlcyBzdWNoIHRoYXQgdGhlIG1heGltdW0gZXJyb3IgcHJvYmFiaWxpdHkgUF9lXnsobil9IOKGkiAwIGFzIG4g4oaSIOKIni4gU2hhbm5vbiBwcm92ZWQgdGhpcyB2aWEgYSByYW5kb20gY29kaW5nIGFyZ3VtZW50OiBhIHJhbmRvbWx5IGNob3NlbiBjb2RlIGFjaGlldmVzIHJlbGlhYmxlIGNvbW11bmljYXRpb24uXG5cbioqQ29udmVyc2UgKFIgXHUwMDNlIEMpOioqIEZvciBhbnkgc2VxdWVuY2Ugb2YgKDJee25SfSwgbikgY29kZXMgd2l0aCBSIFx1MDAzZSBDLCB0aGUgZXJyb3IgcHJvYmFiaWxpdHkgUF9lXnsobil9IOKGkiAxIGFzIG4g4oaSIOKIni4gTm8gZW5jb2Rlci9kZWNvZGVyIHBhaXIgY2FuIHJlbGlhYmx5IGNvbW11bmljYXRlIGFib3ZlIGNhcGFjaXR5LlxuXG5UaGUgcHJvb2Ygb2YgYWNoaWV2YWJpbGl0eSB1c2VzIHRoZSBtZXRob2Qgb2YgKnR5cGljYWwgc2VxdWVuY2VzKjogd2l0aCBoaWdoIHByb2JhYmlsaXR5LCB0aGUgb3V0cHV0IHNlcXVlbmNlIGxpZXMgaW4gYSBzbWFsbCBzZXQgb2Ygam9pbnRseSB0eXBpY2FsIHNlcXVlbmNlcyBkZXRlcm1pbmVkIGJ5IFAoWCxZKSwgYW5kIHRoaXMgc2V0IGNhbiBiZSBkZWNvZGVkIGNvcnJlY3RseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHR5cGluZyBpbXBvcnQgVHVwbGVcblxuZGVmIGRpc2NyZXRlX2NoYW5uZWxfY2FwYWNpdHkoXG4gICAgUF95eDogbnAubmRhcnJheSxcbiAgICBuX2l0ZXI6IGludCA9IDEwMDAsXG4gICAgdG9sOiBmbG9hdCA9IDFlLThcbikgLVx1MDAzZSBUdXBsZVtmbG9hdCwgbnAubmRhcnJheV06XG4gICAgXCJcIlwiQ29tcHV0ZSBjYXBhY2l0eSBvZiBhIGRpc2NyZXRlIG1lbW9yeWxlc3MgY2hhbm5lbCB2aWEgQmxhaHV0LUFyaW1vdG8gYWxnb3JpdGhtLlxuXG4gICAgQXJnczpcbiAgICAgICAgUF95eDogQ29uZGl0aW9uYWwgcHJvYmFiaWxpdHkgUChZPWp8WD1pKSwgc2hhcGUgKHxYfCwgfFl8KS5cbiAgICAgICAgICAgICAgUm93cyBhcmUgaW5wdXQgc3ltYm9scywgY29sdW1ucyBhcmUgb3V0cHV0IHN5bWJvbHMuXG4gICAgICAgIG5faXRlcjogTWF4aW11bSBpdGVyYXRpb25zLlxuICAgICAgICB0b2w6IENvbnZlcmdlbmNlIHRvbGVyYW5jZS5cbiAgICBSZXR1cm5zOlxuICAgICAgICAoY2FwYWNpdHlfYml0cywgb3B0aW1hbF9pbnB1dF9kaXN0cmlidXRpb24pXG4gICAgXCJcIlwiXG4gICAgbl94LCBuX3kgPSBQX3l4LnNoYXBlXG4gICAgcSA9IG5wLm9uZXMobl94KSAvIG5feCAgIyB1bmlmb3JtIGluaXRpYWwgaW5wdXQgZGlzdHJpYnV0aW9uXG5cbiAgICBmb3IgaXRlcmF0aW9uIGluIHJhbmdlKG5faXRlcik6XG4gICAgICAgICMgRS1zdGVwOiBjb21wdXRlIGxvZyBvZiBjKHgpID0gZXhwKM6jX3kgUCh5fHgpIGxvZyBQKHl8eCkvUCh5KSlcbiAgICAgICAgcF95ID0gUF95eC5UIEAgcSAgIyBQKFk9aikgPSDOo+G1oiBxKGkpIFAoWT1qfFg9aSlcbiAgICAgICAgIyBjKHgpIOKInSBleHAoS0woUChZfFg9eCkgfHwgUChZKSkpXG4gICAgICAgIGMgPSBucC5leHAobnAuc3VtKFBfeXggKiBucC5sb2coUF95eCAvIChwX3kgKyAxZS0xMikgKyAxZS0xMiksIGF4aXM9MSkpXG5cbiAgICAgICAgIyBNLXN0ZXA6IHVwZGF0ZSBpbnB1dCBkaXN0cmlidXRpb25cbiAgICAgICAgcV9uZXcgPSBxICogY1xuICAgICAgICBxX25ldyAvPSBxX25ldy5zdW0oKVxuXG4gICAgICAgIGlmIG5wLm1heChucC5hYnMocV9uZXcgLSBxKSkgXHUwMDNjIHRvbDpcbiAgICAgICAgICAgIHEgPSBxX25ld1xuICAgICAgICAgICAgcHJpbnQoZlwiICBDb252ZXJnZWQgYXQgaXRlcmF0aW9uIHtpdGVyYXRpb24rMX1cIilcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIHEgPSBxX25ld1xuXG4gICAgIyBDb21wdXRlIGNhcGFjaXR5IGF0IG9wdGltYWwgcVxuICAgIHBfeSA9IFBfeXguVCBAIHFcbiAgICBtaSA9IDAuMFxuICAgIGZvciBpIGluIHJhbmdlKG5feCk6XG4gICAgICAgIGZvciBqIGluIHJhbmdlKG5feSk6XG4gICAgICAgICAgICBpZiBQX3l4W2ksIGpdIFx1MDAzZSAwIGFuZCBxW2ldIFx1MDAzZSAwOlxuICAgICAgICAgICAgICAgIG1pICs9IHFbaV0gKiBQX3l4W2ksIGpdICogbnAubG9nMihQX3l4W2ksIGpdIC8gcF95W2pdKVxuXG4gICAgcmV0dXJuIG1pLCBxXG5cbiMgQlNDIHdpdGggcD0wLjFcbnAgPSAwLjFcblBfYnNjID0gbnAuYXJyYXkoW1sxLXAsIHBdLCBbcCwgMS1wXV0pXG5jLCBxX29wdCA9IGRpc2NyZXRlX2NoYW5uZWxfY2FwYWNpdHkoUF9ic2MpXG5wcmludChmXCJCU0MgY2FwYWNpdHkgKEJsYWh1dC1Bcmltb3RvKToge2M6LjZmfSBiaXRzXCIpXG5wcmludChmXCJBbmFseXRpYzogezEgLSBiaW5hcnlfZW50cm9weShwKTouNmZ9IGJpdHNcIilcbnByaW50KGZcIk9wdGltYWwgaW5wdXQgZGlzdHJpYnV0aW9uOiB7cV9vcHR9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQVdHTiBDaGFubmVsIGFuZCBTaGFubm9uLUhhcnRsZXkgVGhlb3JlbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEFkZGl0aXZlIFdoaXRlIEdhdXNzaWFuIE5vaXNlIChBV0dOKSBjaGFubmVsIHdpdGggYmFuZHdpZHRoIEIgSHogYW5kIFNOUiA9IFAvTuKCgEIgaGFzIGNhcGFjaXR5OlxuXG5DID0gQiBsb2figoIoMSArIFNOUikgYml0cy9zZWNvbmRcblxuVGhpcyBpcyB0aGUgU2hhbm5vbi1IYXJ0bGV5IHRoZW9yZW0uIEtleSBpbXBsaWNhdGlvbnM6IGRvdWJsaW5nIGJhbmR3aWR0aCBkb3VibGVzIGNhcGFjaXR5OyBkb3VibGluZyBTTlIgYWRkcyBvbmx5IGxvZ+KCgigyKSA9IDEgZXh0cmEgYml0L3MvSHog4oCUIGNhcGFjaXR5IGdyb3dzIGxvZ2FyaXRobWljYWxseSB3aXRoIHBvd2VyLiBNb2Rlcm4gd2lyZWxlc3Mgc3lzdGVtcyAoNUcsIFdpRmkgNikgb3BlcmF0ZSB3aXRoaW4gMS0yIGRCIG9mIHRoaXMgU2hhbm5vbiBsaW1pdCB1c2luZyBMRFBDIG9yIHBvbGFyIGNvZGVzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTW9kZXJuIENvZGVzIEFwcHJvYWNoIENhcGFjaXR5IiwiY29udGVudCI6IlR1cmJvIGNvZGVzICgxOTkzKSBjYW1lIHdpdGhpbiAwLjUgZEIgb2YgdGhlIEFXR04gU2hhbm5vbiBsaW1pdC4gTERQQyBjb2RlcyAocmVkaXNjb3ZlcmVkIDE5OTYpIGNhbiBvcGVyYXRlIHdpdGhpbiAwLjAwNDUgZEIuIFBvbGFyIGNvZGVzIChBcsSxa2FuIDIwMDkpIGFyZSB0aGUgZmlyc3QgcHJvdmFibHkgY2FwYWNpdHktYWNoaWV2aW5nIGZhbWlseSBmb3IgYXJiaXRyYXJ5IGJpbmFyeS1pbnB1dCBjaGFubmVscyBhbmQgYXJlIHVzZWQgaW4gNUcgTlIgc3RhbmRhcmRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbm5lY3Rpb24gdG8gTWFjaGluZSBMZWFybmluZyDigJQgTm9pc3kgTGFiZWwgTGVhcm5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBCU0MgcHJvdmlkZXMgYW4gZXhhY3QgbW9kZWwgZm9yIGxhYmVsIG5vaXNlOiBhIHRydWUgbGFiZWwgeSBpcyBmbGlwcGVkIHRvIGEgY29ycnVwdGVkIGxhYmVsIOG7uSB3aXRoIHByb2JhYmlsaXR5IHAgKHRoZSBub2lzZSByYXRlKS4gVW5kZXIgdGhpcyBtb2RlbCwgdGhlIG11dHVhbCBpbmZvcm1hdGlvbiBiZXR3ZWVuIHRydWUgbGFiZWxzIGFuZCBvYnNlcnZlZCBsYWJlbHMgaXMgSSh5O+G7uSkgPSAxIC0gSF9iKHApID0gQ19CU0MuIFRoaXMgY29uc3RyYWlucyBob3cgbXVjaCBpbmZvcm1hdGlvbiBhYm91dCB5IGlzIHByZXNlcnZlZCBpbiDhu7kg4oCUIGFuZCB0aGVyZWZvcmUgaG93IHdlbGwgYW55IGNsYXNzaWZpZXIgdHJhaW5lZCBvbiDhu7kgY2FuIHJlY292ZXIgeS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExvZ2lzdGljUmVncmVzc2lvblxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFjY3VyYWN5X3Njb3JlXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCB0cmFpbl90ZXN0X3NwbGl0XG5cbmRlZiBhZGRfbGFiZWxfbm9pc2UoeTogbnAubmRhcnJheSwgbm9pc2VfcmF0ZTogZmxvYXQsXG4gICAgICAgICAgICAgICAgICAgbl9jbGFzc2VzOiBpbnQgPSAyKSAtXHUwMDNlIG5wLm5kYXJyYXk6XG4gICAgXCJcIlwiU2ltdWxhdGUgc3ltbWV0cmljIGxhYmVsIG5vaXNlIChCU0MgZm9yIGJpbmFyeSwgdW5pZm9ybSBmb3IgbXVsdGktY2xhc3MpLlwiXCJcIlxuICAgIHlfbm9pc3kgPSB5LmNvcHkoKVxuICAgIG4gPSBsZW4oeSlcbiAgICBmbGlwX21hc2sgPSBucC5yYW5kb20ucmFuZChuKSBcdTAwM2Mgbm9pc2VfcmF0ZVxuXG4gICAgZm9yIGkgaW4gbnAud2hlcmUoZmxpcF9tYXNrKVswXTpcbiAgICAgICAgb3RoZXJfY2xhc3NlcyA9IFtjIGZvciBjIGluIHJhbmdlKG5fY2xhc3NlcykgaWYgYyAhPSB5W2ldXVxuICAgICAgICB5X25vaXN5W2ldID0gbnAucmFuZG9tLmNob2ljZShvdGhlcl9jbGFzc2VzKVxuICAgIHJldHVybiB5X25vaXN5XG5cbmRlZiBub2lzeV9sYWJlbF9leHBlcmltZW50KCk6XG4gICAgXCJcIlwiU2hvdyBob3cgbGFiZWwgbm9pc2UgKEJTQykgZGVncmFkZXMgY2xhc3NpZmljYXRpb24gYWNjdXJhY3kuXG5cbiAgICBUaGUgaW5mb3JtYXRpb24gYm90dGxlbmVjayBwcmVkaWN0czogYWNjdXJhY3kgYm91bmRlZCBieSBCU0MgY2FwYWNpdHkuXG4gICAgXCJcIlwiXG4gICAgWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24oXG4gICAgICAgIG5fc2FtcGxlcz0yMDAwLCBuX2ZlYXR1cmVzPTIwLCBuX2luZm9ybWF0aXZlPTEwLFxuICAgICAgICByYW5kb21fc3RhdGU9NDJcbiAgICApXG4gICAgWF90cmFpbiwgWF90ZXN0LCB5X3RyYWluLCB5X3Rlc3QgPSB0cmFpbl90ZXN0X3NwbGl0KFgsIHksIHRlc3Rfc2l6ZT0wLjMsIHJhbmRvbV9zdGF0ZT00MilcblxuICAgICMgQ2xlYW4gdXBwZXIgYm91bmRcbiAgICBjbGZfY2xlYW4gPSBMb2dpc3RpY1JlZ3Jlc3Npb24obWF4X2l0ZXI9MTAwMCkuZml0KFhfdHJhaW4sIHlfdHJhaW4pXG4gICAgYWNjX2NsZWFuID0gYWNjdXJhY3lfc2NvcmUoeV90ZXN0LCBjbGZfY2xlYW4ucHJlZGljdChYX3Rlc3QpKVxuICAgIHByaW50KGZcIkNsZWFuIGxhYmVscyBhY2N1cmFjeToge2FjY19jbGVhbjouNGZ9XCIpXG5cbiAgICBwcmludChcIlxcbk5vaXNlIHJhdGUgfCBCU0MgQ2FwYWNpdHkgfCBUZXN0IEFjY3VyYWN5IHwgR2FwXCIpXG4gICAgZm9yIHBfbm9pc2UgaW4gWzAuMCwgMC4wNSwgMC4xMCwgMC4yMCwgMC4zMCwgMC40MCwgMC40OV06XG4gICAgICAgIHlfbm9pc3kgPSBhZGRfbGFiZWxfbm9pc2UoeV90cmFpbiwgcF9ub2lzZSlcbiAgICAgICAgY2xmID0gTG9naXN0aWNSZWdyZXNzaW9uKG1heF9pdGVyPTEwMDApLmZpdChYX3RyYWluLCB5X25vaXN5KVxuICAgICAgICBhY2MgPSBhY2N1cmFjeV9zY29yZSh5X3Rlc3QsIGNsZi5wcmVkaWN0KFhfdGVzdCkpXG4gICAgICAgIGNhcGFjaXR5ID0gMS4wIC0gYmluYXJ5X2VudHJvcHkocF9ub2lzZSlcbiAgICAgICAgcHJpbnQoZlwiICBwPXtwX25vaXNlOi4yZn0gICAgIHwge2NhcGFjaXR5Oi40Zn0gICAgICAgfCB7YWNjOi40Zn0gICAgICAgIHwge2FjY19jbGVhbi1hY2M6LjRmfVwiKVxuXG5ub2lzeV9sYWJlbF9leHBlcmltZW50KCkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiU291cmNlLUNoYW5uZWwgU2VwYXJhdGlvbiIsImNvbnRlbnQiOiJTaGFubm9uXHUwMDI3cyBzZXBhcmF0aW9uIHRoZW9yZW0gc2F5czogY29tcHJlc3MgdGhlIHNvdXJjZSB0byBpdHMgZW50cm9weSByYXRlIGZpcnN0IChzb3VyY2UgY29kaW5nKSwgdGhlbiB0cmFuc21pdCBhdCBhbnkgcmF0ZSBiZWxvdyBjaGFubmVsIGNhcGFjaXR5IChjaGFubmVsIGNvZGluZykuIFRoZXNlIHR3byBzdGVwcyBjYW4gYmUgZGVzaWduZWQgaW5kZXBlbmRlbnRseSB3aXRob3V0IGxvc3Mgb2Ygb3B0aW1hbGl0eS4gVGhpcyBqdXN0aWZpZXMgdGhlIG1vZHVsYXIgZGVzaWduIG9mIG1vZGVybiBjb21tdW5pY2F0aW9uIHN5c3RlbXMg4oCUIGNvbXByZXNzaW9uIGNvZGVjcyBhcmUgc2VwYXJhdGUgZnJvbSBmb3J3YXJkIGVycm9yIGNvcnJlY3Rpb24uIn0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2hhbm5vblx1MDAyN3MgY2hhbm5lbCBjb2RpbmcgdGhlb3JlbSBpcyBvbmUgb2YgdGhlIGdyZWF0IGV4aXN0ZW50aWFsIHRoZW9yZW1zIG9mIHNjaWVuY2U6IGl0IHByb3ZlcyB0aGF0IHBlcmZlY3QgcmVsaWFiaWxpdHkgaXMgYWNoaWV2YWJsZSBkZXNwaXRlIGltcGVyZmVjdCBjaGFubmVscywgdXAgdG8gYSBoYXJkIGxpbWl0IEMuIFRoZSB0aGVvcmVtIGlzIG5vbi1jb25zdHJ1Y3RpdmUg4oCUIFNoYW5ub25cdTAwMjdzIHJhbmRvbSBjb2RpbmcgcHJvb2YgZG9lc25cdTAwMjd0IHRlbGwgdXMgKmhvdyogdG8gYnVpbGQgY2FwYWNpdHktYWNoaWV2aW5nIGNvZGVzIOKAlCBidXQgaXQgc2V0IHRoZSBhZ2VuZGEgZm9yIDYwIHllYXJzIG9mIGNvZGluZyB0aGVvcnksIGN1bG1pbmF0aW5nIGluIHR1cmJvLCBMRFBDLCBhbmQgcG9sYXIgY29kZXMgdGhhdCBicmluZyBwcmFjdGljZSB3aXRoaW4gYSBmcmFjdGlvbiBvZiBhIGRCIG9mIHRoZW9yeS4ifV0="
---
# Noisy Channel Model and Shannon's Coding Theorem

Shannon's 1948 paper 'A Mathematical Theory of Communication' is arguably the most important paper in 20th-century engineering. Its central result — the channel coding theorem — showed that reliable communication over a noisy channel is always possible as long as the information rate stays below a finite threshold called channel capacity. This was deeply counter-intuitive: engineers of the time believed noise fundamentally limited reliability.

## The Shannon Communication Model

Shannon's model has five components:
1. Source — generates a message M from a message set
2. Encoder — maps M to a codeword x^n from the channel alphabet
3. Channel — maps x^n to y^n with noise (probabilistic mapping P(y|x))
4. Decoder — maps y^n back to an estimate M̂ of M
5. Receiver — uses M̂

The goal: choose encoder/decoder pairs such that P(M̂ ≠ M) → 0 as block length n → ∞, while transmitting as many bits per channel use as possible.

## Channel Capacity

The channel capacity C is the maximum mutual information between input and output, optimized over all input distributions:

C = max_{P(X)} I(X;Y)

Capacity has units of bits per channel use. The optimization is over P(X) — the choice of input distribution — because we control what we send but not the channel's noise behavior.

| Channel Model | Description | Capacity Formula | Example Value |
| --- | --- | --- | --- |
| Binary Symmetric Channel (BSC) | Bit flipped with prob p | C = 1 − H_b(p) | p=0.1: C≈0.531 bits/use |
| Binary Erasure Channel (BEC) | Bit erased with prob ε | C = 1 − ε | ε=0.2: C=0.8 bits/use |
| AWGN | Gaussian noise with variance σ² | C = ½ log₂(1 + P/σ²) | SNR=10dB: C≈3.46 bits/use |
| Z-Channel | 0→0 always, 1→0 with prob p | C = log₂(1 + (1−p)·2^{−H_b(p/(1+(1−p)))}) | Asymmetric, used in optical |
| Discrete Memoryless (general) | Any P(y|x) | max_{P(X)} I(X;Y) | Computed numerically |

## Binary Symmetric Channel — Capacity and Simulation

```python
import numpy as np
from scipy.special import entr

def binary_entropy(p: float) -> float:
    """Binary entropy function H_b(p) = -p log2(p) - (1-p) log2(1-p)."""
    if p <= 0 or p >= 1:
        return 0.0
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

def bsc_capacity(p: float) -> float:
    """Capacity of Binary Symmetric Channel with crossover probability p."""
    return 1.0 - binary_entropy(p)

def simulate_bsc(message_bits: np.ndarray, p: float) -> np.ndarray:
    """Simulate BSC: flip each bit independently with probability p."""
    flips = np.random.binomial(1, p, size=message_bits.shape)
    return (message_bits + flips) % 2  # XOR

# Capacity at key crossover probabilities
print("BSC capacity C = 1 - H_b(p):")
for p in [0.0, 0.01, 0.05, 0.1, 0.2, 0.5]:
    c = bsc_capacity(p)
    print(f"  p = {p:.2f}: C = {c:.4f} bits/use")

# Show that capacity is maximized by uniform input (p(X=0) = p(X=1) = 0.5)
print("\nCapacity achieved at uniform input distribution")
print(f"  At p=0.1, BSC capacity = {bsc_capacity(0.1):.4f} bits")
print(f"  Gap from 1 bit = {1.0 - bsc_capacity(0.1):.4f} bits (cost of noise)")
```

## Repetition Codes vs Channel Capacity

The simplest error-correcting code is the repetition code: send each bit n times and decode by majority vote. This shows concretely how rate and reliability trade off around capacity. Below capacity (rate R < C), BER → 0 as n grows. Above capacity, BER stays bounded away from 0.

```python
import numpy as np

def repetition_code_ber(
    p_channel: float,
    n_repeats_list: list,
    n_trials: int = 5000,
    n_bits: int = 200
) -> None:
    """Simulate repetition code performance vs channel capacity on BSC.

    Demonstrates Shannon's theorem: rate < C achieves low BER; rate > C fails.

    Args:
        p_channel: BSC crossover probability (noise level).
        n_repeats_list: List of repetition factors to test.
        n_trials: Number of Monte Carlo trials.
        n_bits: Number of information bits per trial.
    """
    capacity = 1.0 - binary_entropy(p_channel)
    print(f"Channel: BSC(p={p_channel}), Capacity C = {capacity:.4f} bits/use")
    print(f"\n{'n_repeats':>10} {'Rate':>8} {'< C?':>6} {'BER':>12} {'Reliable?':>10}")
    print("-" * 50)

    for n_repeats in n_repeats_list:
        rate = 1.0 / n_repeats
        total_errors = 0

        for _ in range(n_trials):
            msg = np.random.randint(0, 2, n_bits)
            encoded = np.repeat(msg, n_repeats)         # n_repeats * n_bits symbols sent
            flips = np.random.binomial(1, p_channel, encoded.shape)
            received = (encoded + flips) % 2
            # Majority vote: sum over repeats, threshold at 0.5
            decoded = (received.reshape(n_bits, n_repeats).mean(axis=1) > 0.5).astype(int)
            total_errors += np.sum(decoded != msg)

        ber = total_errors / (n_trials * n_bits)
        below_cap = "YES" if rate < capacity else "NO "
        reliable = "YES" if ber < 0.01 else "NO "
        print(f"{n_repeats:>10} {rate:>8.4f} {below_cap:>6} {ber:>12.6f} {reliable:>10}")

# BSC with p=0.1 → C ≈ 0.531 bits/use
repetition_code_ber(
    p_channel=0.1,
    n_repeats_list=[1, 2, 3, 5, 7, 11, 21]
)
```

## Shannon's Channel Coding Theorem

**Achievability (R < C):** For any rate R < C, there exists a sequence of (2^{nR}, n) codes such that the maximum error probability P_e^{(n)} → 0 as n → ∞. Shannon proved this via a random coding argument: a randomly chosen code achieves reliable communication.

**Converse (R > C):** For any sequence of (2^{nR}, n) codes with R > C, the error probability P_e^{(n)} → 1 as n → ∞. No encoder/decoder pair can reliably communicate above capacity.

The proof of achievability uses the method of *typical sequences*: with high probability, the output sequence lies in a small set of jointly typical sequences determined by P(X,Y), and this set can be decoded correctly.

```python
import numpy as np
from typing import Tuple

def discrete_channel_capacity(
    P_yx: np.ndarray,
    n_iter: int = 1000,
    tol: float = 1e-8
) -> Tuple[float, np.ndarray]:
    """Compute capacity of a discrete memoryless channel via Blahut-Arimoto algorithm.

    Args:
        P_yx: Conditional probability P(Y=j|X=i), shape (|X|, |Y|).
              Rows are input symbols, columns are output symbols.
        n_iter: Maximum iterations.
        tol: Convergence tolerance.
    Returns:
        (capacity_bits, optimal_input_distribution)
    """
    n_x, n_y = P_yx.shape
    q = np.ones(n_x) / n_x  # uniform initial input distribution

    for iteration in range(n_iter):
        # E-step: compute log of c(x) = exp(Σ_y P(y|x) log P(y|x)/P(y))
        p_y = P_yx.T @ q  # P(Y=j) = Σᵢ q(i) P(Y=j|X=i)
        # c(x) ∝ exp(KL(P(Y|X=x) || P(Y)))
        c = np.exp(np.sum(P_yx * np.log(P_yx / (p_y + 1e-12) + 1e-12), axis=1))

        # M-step: update input distribution
        q_new = q * c
        q_new /= q_new.sum()

        if np.max(np.abs(q_new - q)) < tol:
            q = q_new
            print(f"  Converged at iteration {iteration+1}")
            break
        q = q_new

    # Compute capacity at optimal q
    p_y = P_yx.T @ q
    mi = 0.0
    for i in range(n_x):
        for j in range(n_y):
            if P_yx[i, j] > 0 and q[i] > 0:
                mi += q[i] * P_yx[i, j] * np.log2(P_yx[i, j] / p_y[j])

    return mi, q

# BSC with p=0.1
p = 0.1
P_bsc = np.array([[1-p, p], [p, 1-p]])
c, q_opt = discrete_channel_capacity(P_bsc)
print(f"BSC capacity (Blahut-Arimoto): {c:.6f} bits")
print(f"Analytic: {1 - binary_entropy(p):.6f} bits")
print(f"Optimal input distribution: {q_opt}")
```

## AWGN Channel and Shannon-Hartley Theorem

The Additive White Gaussian Noise (AWGN) channel with bandwidth B Hz and SNR = P/N₀B has capacity:

C = B log₂(1 + SNR) bits/second

This is the Shannon-Hartley theorem. Key implications: doubling bandwidth doubles capacity; doubling SNR adds only log₂(2) = 1 extra bit/s/Hz — capacity grows logarithmically with power. Modern wireless systems (5G, WiFi 6) operate within 1-2 dB of this Shannon limit using LDPC or polar codes.

> **Modern Codes Approach Capacity**: Turbo codes (1993) came within 0.5 dB of the AWGN Shannon limit. LDPC codes (rediscovered 1996) can operate within 0.0045 dB. Polar codes (Arıkan 2009) are the first provably capacity-achieving family for arbitrary binary-input channels and are used in 5G NR standards.

## Connection to Machine Learning — Noisy Label Learning

The BSC provides an exact model for label noise: a true label y is flipped to a corrupted label ỹ with probability p (the noise rate). Under this model, the mutual information between true labels and observed labels is I(y;ỹ) = 1 - H_b(p) = C_BSC. This constrains how much information about y is preserved in ỹ — and therefore how well any classifier trained on ỹ can recover y.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def add_label_noise(y: np.ndarray, noise_rate: float,
                   n_classes: int = 2) -> np.ndarray:
    """Simulate symmetric label noise (BSC for binary, uniform for multi-class)."""
    y_noisy = y.copy()
    n = len(y)
    flip_mask = np.random.rand(n) < noise_rate

    for i in np.where(flip_mask)[0]:
        other_classes = [c for c in range(n_classes) if c != y[i]]
        y_noisy[i] = np.random.choice(other_classes)
    return y_noisy

def noisy_label_experiment():
    """Show how label noise (BSC) degrades classification accuracy.

    The information bottleneck predicts: accuracy bounded by BSC capacity.
    """
    X, y = make_classification(
        n_samples=2000, n_features=20, n_informative=10,
        random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Clean upper bound
    clf_clean = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    acc_clean = accuracy_score(y_test, clf_clean.predict(X_test))
    print(f"Clean labels accuracy: {acc_clean:.4f}")

    print("\nNoise rate | BSC Capacity | Test Accuracy | Gap")
    for p_noise in [0.0, 0.05, 0.10, 0.20, 0.30, 0.40, 0.49]:
        y_noisy = add_label_noise(y_train, p_noise)
        clf = LogisticRegression(max_iter=1000).fit(X_train, y_noisy)
        acc = accuracy_score(y_test, clf.predict(X_test))
        capacity = 1.0 - binary_entropy(p_noise)
        print(f"  p={p_noise:.2f}     | {capacity:.4f}       | {acc:.4f}        | {acc_clean-acc:.4f}")

noisy_label_experiment()
```

> **Source-Channel Separation**: Shannon's separation theorem says: compress the source to its entropy rate first (source coding), then transmit at any rate below channel capacity (channel coding). These two steps can be designed independently without loss of optimality. This justifies the modular design of modern communication systems — compression codecs are separate from forward error correction.

---

Shannon's channel coding theorem is one of the great existential theorems of science: it proves that perfect reliability is achievable despite imperfect channels, up to a hard limit C. The theorem is non-constructive — Shannon's random coding proof doesn't tell us *how* to build capacity-achieving codes — but it set the agenda for 60 years of coding theory, culminating in turbo, LDPC, and polar codes that bring practice within a fraction of a dB of theory.

