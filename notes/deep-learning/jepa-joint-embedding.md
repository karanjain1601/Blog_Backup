---
title: "JEPA — Joint-Embedding Predictive Architecture"
slug: "jepa-joint-embedding"
description: "JEPA (LeCun 2022; I-JEPA He et al. 2023) predicts representations of masked target regions in embedding space rather than pixel space, producing semantic features without augmentation-induced biases and outperforming MAE on linear probe benchmarks."
tags: ["deep-learning", "self-supervised-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSkVQQSAoSm9pbnQtRW1iZWRkaW5nIFByZWRpY3RpdmUgQXJjaGl0ZWN0dXJlLCBMZUN1biAyMDIyKSBhcmd1ZXMgdGhhdCB0aGUgcmlnaHQgb2JqZWN0aXZlIGZvciBzZWxmLXN1cGVydmlzZWQgbGVhcm5pbmcgaXMgdG8gcHJlZGljdCBhYnN0cmFjdCByZXByZXNlbnRhdGlvbnMgb2YgdGhlIHdvcmxkLCBub3QgbG93LWxldmVsIHNlbnNvcnkgZGV0YWlscy4gSW5zdGVhZCBvZiBhc2tpbmcgYSBtb2RlbCB0byByZWNvbnN0cnVjdCBwaXhlbHMgKE1BRSkgb3IgbWF0Y2ggYXVnbWVudGVkIHZpZXdzIChTaW1DTFIsIERJTk8pLCBhIEpFUEEgbW9kZWwgbGVhcm5zIHRvIHByZWRpY3QgdGhlIHJlcHJlc2VudGF0aW9uIG9mIGEgbWFza2VkIG9yIGZ1dHVyZSByZWdpb24gZnJvbSB0aGUgY29udGV4dC4gVGhlIGNydWNpYWwgZGlmZmVyZW5jZSBpcyB3aGVyZSBwcmVkaWN0aW9uIGhhcHBlbnM6IGluIGVtYmVkZGluZyBzcGFjZSwgbm90IHBpeGVsIHNwYWNlLiBUaGlzIGZyZWVzIHRoZSBtb2RlbCBmcm9tIGxlYXJuaW5nIHRvIHJlY29uc3RydWN0IGlycmVsZXZhbnQgdGV4dHVyZSBhbmQgbm9pc2UsIGZvY3VzaW5nIHRoZSBjYXBhY2l0eSBvbiBzZW1hbnRpYyBjb250ZW50LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiSS1KRVBBIChIZSBldCBhbC4gMjAyMyk6IHByZWRpY3QgcGF0Y2gtbGV2ZWwgcmVwcmVzZW50YXRpb25zIG9mIG1hc2tlZCB0YXJnZXQgYmxvY2tzIGZyb20gY29udGV4dCBlbmNvZGVyIG91dHB1dC4iLCJUYXJnZXQgZW5jb2RlcjogRU1BIG9mIGNvbnRleHQgZW5jb2RlciDigJQgc2xvd2x5IGV2b2x2aW5nIHN0YWJsZSB0YXJnZXRzLCBwcmV2ZW50cyBtb2RlIGNvbGxhcHNlLiIsIlByZWRpY3RvcjogbmFycm93IFRyYW5zZm9ybWVyIHdpdGggcG9zaXRpb25hbCBjb25kaXRpb25pbmcg4oCUIHByZWRpY3RzIGFic3RyYWN0IGNvbnRlbnQsIG5ldmVyIHJhdyBwaXhlbHMuIiwiTm8gYXVnbWVudGF0aW9uIGVuZ2luZWVyaW5nOiB0aGUgbWFza2luZyBzdHJhdGVneSBhbG9uZSBjcmVhdGVzIHRoZSBzZWxmLXN1cGVydmlzZWQgc2lnbmFsLiIsIlYtSkVQQSAoQmFyZGVzIGV0IGFsLiAyMDI0KTogdGVtcG9yYWwgZXh0ZW5zaW9uIOKAlCBwcmVkaWN0IGZ1dHVyZSBmcmFtZSByZXByZXNlbnRhdGlvbnMgZnJvbSBwYXN0IGNvbnRleHQuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZWRpY3Rpb24gaW4gRW1iZWRkaW5nIFNwYWNlIHZzIFBpeGVsIFNwYWNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNQUUgcmVjb25zdHJ1Y3RzIHBpeGVsIHZhbHVlcyBvZiBtYXNrZWQgcGF0Y2hlcy4gVGhpcyBmb3JjZXMgdGhlIGVuY29kZXIgdG8gY2FwdHVyZSBib3RoIHNlbWFudGljIGNvbnRlbnQgYW5kIGxvdy1sZXZlbCBhcHBlYXJhbmNlICh0ZXh0dXJlLCBjb2xvciwgbm9pc2UpIOKAlCBzaW5jZSB0aGUgZGVjb2RlciBtdXN0IHJlY292ZXIgcGl4ZWwtYWNjdXJhdGUgdmFsdWVzLiBJLUpFUEEgaW5zdGVhZCBhc2tzOiBnaXZlbiB0aGUgcmVwcmVzZW50YXRpb24gb2YgdGhlIHZpc2libGUgY29udGV4dCwgcHJlZGljdCB0aGUgcmVwcmVzZW50YXRpb24gb2YgdGhlIG1hc2tlZCB0YXJnZXQgYXMgY29tcHV0ZWQgYnkgYSB0YXJnZXQgZW5jb2Rlci4gVGhlIHByZWRpY3RvciBuZXZlciBzZWVzIHBpeGVscyBvZiB0aGUgdGFyZ2V0OyBpdCBvbmx5IHNlZXMgdGhlIHBvc2l0aW9uIG9mIHRoZSB0YXJnZXQgYmxvY2sgYW5kIHRoZSBjb250ZXh0IHJlcHJlc2VudGF0aW9uLiBUaGlzIG1ha2VzIHRoZSBwcm9ibGVtIHN0cmljdGx5IHNlbWFudGljIOKAlCB0aGVyZSBpcyBubyBncmFkaWVudCBzaWduYWwgZm9yIHBpeGVsIG5vaXNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkktSkVQQSBNYXNraW5nIFN0cmF0ZWd5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJLUpFUEEgKEltYWdlIEpvaW50LUVtYmVkZGluZyBQcmVkaWN0aXZlIEFyY2hpdGVjdHVyZSwgSGUgZXQgYWwuIDIwMjMpIHVzZXMgYSBjYXJlZnVsbHkgZGVzaWduZWQgbWFza2luZyBzdHJhdGVneSB0byBjcmVhdGUgYSBjaGFsbGVuZ2luZyBidXQgc29sdmFibGUgcHJlZGljdGl2ZSB0YXNrLiBUaGUgaW1hZ2UgaXMgZGl2aWRlZCBpbnRvIHBhdGNoZXMuIEEgY29udGV4dCByZWdpb24gaXMgc2VsZWN0ZWQgKGEgcmFuZG9tIGJsb2NrIGNvdmVyaW5nIHJvdWdobHkgODUlIG9mIHRoZSBpbWFnZSB3aXRoIHNvbWUgZXhjbHVzaW9ucykuIFNldmVyYWwgdGFyZ2V0IGJsb2NrcyAoNCBvbiBhdmVyYWdlKSBhcmUgc2FtcGxlZCBmcm9tIHRoZSByZW1haW5pbmcgcG9zaXRpb25zIOKAlCB0aGVzZSBhcmUgdGhlIHJlZ2lvbnMgdGhlIHByZWRpY3RvciBtdXN0IHJlY29uc3RydWN0IGluIGVtYmVkZGluZyBzcGFjZS4gVGhlIHByZWRpY3RvciByZWNlaXZlczogKDEpIHRoZSBjb250ZXh0IGVuY29kZXIgb3V0cHV0LCBhbmQgKDIpIHRoZSBwb3NpdGlvbmFsIGVuY29kaW5nIG9mIGVhY2ggdGFyZ2V0IGJsb2NrLiBJdCBtdXN0IG91dHB1dCBhIHJlcHJlc2VudGF0aW9uIHRoYXQgbWF0Y2hlcyB0aGUgdGFyZ2V0IGVuY29kZXJcdTAwMjdzIHJlcHJlc2VudGF0aW9uIGF0IHRob3NlIHBvc2l0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgcmFuZG9tXG5cblxuZGVmIHNhbXBsZV9ibG9jayhncmlkX2g6IGludCwgZ3JpZF93OiBpbnQsIG1pbl9zY2FsZTogZmxvYXQsIG1heF9zY2FsZTogZmxvYXQsXG4gICAgICAgICAgICAgICAgIGFzcGVjdF9taW46IGZsb2F0ID0gMC43NSwgYXNwZWN0X21heDogZmxvYXQgPSAxLjUpOlxuICAgIFwiXCJcIlNhbXBsZSBhIHJhbmRvbSByZWN0YW5ndWxhciBibG9jayBvbiB0aGUgcGF0Y2ggZ3JpZC5cIlwiXCJcbiAgICBzY2FsZSA9IHJhbmRvbS51bmlmb3JtKG1pbl9zY2FsZSwgbWF4X3NjYWxlKVxuICAgIGFyZWEgPSBpbnQoZ3JpZF9oICogZ3JpZF93ICogc2NhbGUpXG4gICAgYXNwZWN0ID0gcmFuZG9tLnVuaWZvcm0oYXNwZWN0X21pbiwgYXNwZWN0X21heClcbiAgICBoID0gaW50KChhcmVhICogYXNwZWN0KSAqKiAwLjUpXG4gICAgdyA9IGludChhcmVhIC8gbWF4KGgsIDEpKVxuICAgIGgsIHcgPSBtaW4oaCwgZ3JpZF9oKSwgbWluKHcsIGdyaWRfdylcbiAgICB0b3AgID0gcmFuZG9tLnJhbmRpbnQoMCwgZ3JpZF9oIC0gaClcbiAgICBsZWZ0ID0gcmFuZG9tLnJhbmRpbnQoMCwgZ3JpZF93IC0gdylcbiAgICBpbmRpY2VzID0gW11cbiAgICBmb3IgciBpbiByYW5nZSh0b3AsIHRvcCArIGgpOlxuICAgICAgICBmb3IgYyBpbiByYW5nZShsZWZ0LCBsZWZ0ICsgdyk6XG4gICAgICAgICAgICBpbmRpY2VzLmFwcGVuZChyICogZ3JpZF93ICsgYylcbiAgICByZXR1cm4gc29ydGVkKHNldChpbmRpY2VzKSlcblxuXG5kZWYgaWplcGFfbWFza3MoZ3JpZF9oPTE0LCBncmlkX3c9MTQsIG5fdGFyZ2V0cz00LFxuICAgICAgICAgICAgICAgIGN0eF9zY2FsZT0oMC44NSwgMS4wKSwgdGd0X3NjYWxlPSgwLjE1LCAwLjIpKTpcbiAgICBcIlwiXCJSZXR1cm4gY29udGV4dF9tYXNrIGFuZCBsaXN0IG9mIHRhcmdldF9tYXNrcyAocGF0Y2ggaW5kaWNlcykuXCJcIlwiXG4gICAgYWxsX3BhdGNoZXMgPSBsaXN0KHJhbmdlKGdyaWRfaCAqIGdyaWRfdykpXG4gICAgY3R4X2Jsb2NrICAgPSBzYW1wbGVfYmxvY2soZ3JpZF9oLCBncmlkX3csICpjdHhfc2NhbGUpXG4gICAgIyBDb250ZXh0OiBhbGwgcGF0Y2hlcyBOT1QgZXhjbHVkZWQgYnkgYW55IHRhcmdldCBibG9ja1xuICAgIHRhcmdldF9tYXNrcyA9IFtdXG4gICAgZXhjbHVkZWQgPSBzZXQoKVxuICAgIGZvciBfIGluIHJhbmdlKG5fdGFyZ2V0cyk6XG4gICAgICAgIHRndCA9IHNhbXBsZV9ibG9jayhncmlkX2gsIGdyaWRfdywgKnRndF9zY2FsZSlcbiAgICAgICAgdGFyZ2V0X21hc2tzLmFwcGVuZCh0Z3QpXG4gICAgICAgIGV4Y2x1ZGVkLnVwZGF0ZSh0Z3QpXG4gICAgY29udGV4dF9tYXNrID0gW3AgZm9yIHAgaW4gY3R4X2Jsb2NrIGlmIHAgbm90IGluIGV4Y2x1ZGVkXVxuICAgIHJldHVybiBjb250ZXh0X21hc2ssIHRhcmdldF9tYXNrc1xuXG5cbmN0eCwgdGFyZ2V0cyA9IGlqZXBhX21hc2tzKClcbnByaW50KGZcdTAwMjdDb250ZXh0IHBhdGNoZXM6IHtsZW4oY3R4KX0gIHwgIFRhcmdldCBibG9ja3M6IHtsZW4odGFyZ2V0cyl9XHUwMDI3KVxuZm9yIGksIHQgaW4gZW51bWVyYXRlKHRhcmdldHMpOlxuICAgIHByaW50KGZcdTAwMjcgIFRhcmdldCB7aX06IHtsZW4odCl9IHBhdGNoZXMsIGZpcnN0PXt0WzBdfSwgbGFzdD17dFstMV19XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZWRpY3RvciB3aXRoIFBvc2l0aW9uYWwgQ29uZGl0aW9uaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcHJlZGljdG9yIGluIEktSkVQQSBpcyBhIG5hcnJvdyBUcmFuc2Zvcm1lciB0aGF0IHRha2VzIHR3byBpbnB1dHM6ICgxKSB0aGUgY29udGV4dCBlbmNvZGVyXHUwMDI3cyBvdXRwdXQgdG9rZW5zIChDTFMgKyBjb250ZXh0IHBhdGNoIHRva2VucyksIGFuZCAoMikgYSBzZXQgb2YgbGVhcm5hYmxlIG1hc2sgdG9rZW5zLCBvbmUgcGVyIHRhcmdldCBwYXRjaCwgd2l0aCBwb3NpdGlvbmFsIGVtYmVkZGluZ3MgaW5qZWN0ZWQgYXQgdGhlIHRhcmdldCBwb3NpdGlvbnMuIFRoZSBwcmVkaWN0b3IgbXVzdCBhdHRlbmQgZnJvbSBlYWNoIG1hc2sgdG9rZW4gdG8gdGhlIGNvbnRleHQgdG9rZW5zIGFuZCBwcm9kdWNlIGEgcHJlZGljdGlvbiB0aGF0IG1hdGNoZXMgdGhlIHRhcmdldCBlbmNvZGVyIHJlcHJlc2VudGF0aW9uIGF0IHRoYXQgcG9zaXRpb24uIFRoZSBwcmVkaWN0b3IgaXMgaW50ZW50aW9uYWxseSBzaGFsbG93ICg0IFRyYW5zZm9ybWVyIGJsb2Nrcykg4oCUIGl0IHNob3VsZCBub3QgYmUgc28gcG93ZXJmdWwgdGhhdCBpdCBjYW4gc29sdmUgdGhlIHRhc2sgd2l0aG91dCBsZWFybmluZyBnb29kIGNvbnRleHQgcmVwcmVzZW50YXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5cbmNsYXNzIElKRVBBUHJlZGljdG9yKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTmFycm93IFRyYW5zZm9ybWVyIHByZWRpY3RvcjogY29udGV4dCB0b2tlbnMgKyB0YXJnZXQgcG9zaXRpb25zIC1cdTAwM2UgdGFyZ2V0IHJlcHJlc2VudGF0aW9ucy5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBlbWJlZF9kaW06IGludCA9IDc2OCwgcHJlZF9kaW06IGludCA9IDM4NCxcbiAgICAgICAgICAgICAgICAgZGVwdGg6IGludCA9IDQsIG51bV9oZWFkczogaW50ID0gNik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnByb2pfaW4gID0gbm4uTGluZWFyKGVtYmVkX2RpbSwgcHJlZF9kaW0pICAgIyBwcm9qZWN0IGNvbnRleHQgdG8gcHJlZF9kaW1cbiAgICAgICAgc2VsZi5tYXNrX3RvayA9IG5uLlBhcmFtZXRlcih0b3JjaC5yYW5kbigxLCAxLCBwcmVkX2RpbSkgKiAwLjAyKVxuICAgICAgICBlbmNvZGVyX2xheWVyID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyTGF5ZXIoXG4gICAgICAgICAgICBkX21vZGVsPXByZWRfZGltLCBuaGVhZD1udW1faGVhZHMsXG4gICAgICAgICAgICBkaW1fZmVlZGZvcndhcmQ9cHJlZF9kaW0gKiA0LCBkcm9wb3V0PTAuMCwgYmF0Y2hfZmlyc3Q9VHJ1ZSxcbiAgICAgICAgKVxuICAgICAgICBzZWxmLnRyYW5zZm9ybWVyID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyKGVuY29kZXJfbGF5ZXIsIG51bV9sYXllcnM9ZGVwdGgpXG4gICAgICAgIHNlbGYucHJval9vdXQgPSBubi5MaW5lYXIocHJlZF9kaW0sIGVtYmVkX2RpbSkgICAjIGJhY2sgdG8gdGFyZ2V0IHNwYWNlXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBjdHhfdG9rZW5zOiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgdGFyZ2V0X3Bvc19lbWI6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIFwiXCJcImN0eF90b2tlbnM6IChCLCBOX2N0eCwgRCkgIHRhcmdldF9wb3NfZW1iOiAoQiwgTl90Z3QsIEQpXG4gICAgICAgIFJldHVybnMgcHJlZGljdGlvbnM6IChCLCBOX3RndCwgRCkgaW4gdGFyZ2V0IGVuY29kZXIgc3BhY2UuXG4gICAgICAgIFwiXCJcIlxuICAgICAgICBCLCBOX3RndCwgXyA9IHRhcmdldF9wb3NfZW1iLnNoYXBlXG4gICAgICAgIGN0eCA9IHNlbGYucHJval9pbihjdHhfdG9rZW5zKSAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIE5fY3R4LCBwcmVkX2RpbSlcbiAgICAgICAgIyBNYXNrIHRva2VucyBpbml0aWFsaXNlZCBpZGVudGljYWxseSArIHBvc2l0aW9uYWwgb2Zmc2V0XG4gICAgICAgIG1hc2tfdG9rcyA9IHNlbGYubWFza190b2suZXhwYW5kKEIsIE5fdGd0LCAtMSlcbiAgICAgICAgbWFza190b2tzID0gbWFza190b2tzICsgc2VsZi5wcm9qX2luKHRhcmdldF9wb3NfZW1iKSAgIyBpbmplY3QgdGFyZ2V0IHBvc2l0aW9uXG4gICAgICAgIHRva2VucyA9IHRvcmNoLmNhdChbY3R4LCBtYXNrX3Rva3NdLCBkaW09MSkgICAgICAgICAgICMgKEIsIE5fY3R4K05fdGd0LCBwcmVkX2RpbSlcbiAgICAgICAgb3V0ICAgID0gc2VsZi50cmFuc2Zvcm1lcih0b2tlbnMpICAgICAgICAgICAgICAgICAgICAgICMgKEIsIE5fY3R4K05fdGd0LCBwcmVkX2RpbSlcbiAgICAgICAgcHJlZHMgID0gc2VsZi5wcm9qX291dChvdXRbOiwgLU5fdGd0OiwgOl0pICAgICAgICAgICAgIyAoQiwgTl90Z3QsIEQpXG4gICAgICAgIHJldHVybiBwcmVkc1xuXG5cbnByZWQgPSBJSkVQQVByZWRpY3RvcihlbWJlZF9kaW09NzY4LCBwcmVkX2RpbT0zODQpXG5jdHggID0gdG9yY2gucmFuZG4oMiwgMTIwLCA3NjgpXG50Z3RfcG9zID0gdG9yY2gucmFuZG4oMiwgMzAsIDc2OClcbm91dCA9IHByZWQoY3R4LCB0Z3RfcG9zKVxucHJpbnQoXHUwMDI3UHJlZGljdG9yIG91dHB1dCBzaGFwZTpcdTAwMjcsIG91dC5zaGFwZSkgICAjICgyLCAzMCwgNzY4KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkktSkVQQSBUcmFpbmluZyBMb29wIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdHJhaW5pbmcgbG9vcCBoYXMgdGhyZWUgY29tcG9uZW50czogYSBjb250ZXh0IGVuY29kZXIgKHVwZGF0ZWQgYnkgZ3JhZGllbnQpLCBhIHRhcmdldCBlbmNvZGVyIChFTUEgb2YgY29udGV4dCBlbmNvZGVyLCBubyBncmFkaWVudCksIGFuZCB0aGUgcHJlZGljdG9yLiBUaGUgY29udGV4dCBlbmNvZGVyIHByb2Nlc3NlcyBvbmx5IHRoZSB1bm1hc2tlZCBjb250ZXh0IHBhdGNoZXMuIFRoZSB0YXJnZXQgZW5jb2RlciBwcm9jZXNzZXMgdGhlIGZ1bGwgaW1hZ2UgYW5kIHByb3ZpZGVzIHRoZSB0YXJnZXQgcmVwcmVzZW50YXRpb25zLiBUaGUgcHJlZGljdG9yIHRha2VzIGNvbnRleHQgZW5jb2RlciBvdXRwdXQgKyB0YXJnZXQgcG9zaXRpb24gZW1iZWRkaW5ncyBhbmQgcHJvZHVjZXMgcHJlZGljdGlvbnMuIFRoZSBsb3NzIGlzIE1TRSBiZXR3ZWVuIHRoZSBwcmVkaWN0b3Igb3V0cHV0IGFuZCB0aGUgdGFyZ2V0IGVuY29kZXJcdTAwMjdzIHBhdGNoIHRva2VucyBhdCB0aGUgdGFyZ2V0IHBvc2l0aW9ucy4gVGhlIEVNQSBtb21lbnR1bSBpbmNyZWFzZXMgZnJvbSAwLjk5NiB0byAxLjAgb3ZlciB0cmFpbmluZyAoY29zaW5lIHNjaGVkdWxlKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBjb3B5XG5cblxuZGVmIGJ1aWxkX2lqZXBhKGVuY29kZXJfY2xzLCBlbWJlZF9kaW09NzY4LCBwcmVkX2RpbT0zODQsIG1vbWVudHVtPTAuOTk2KTpcbiAgICBjdHhfZW5jb2RlciA9IGVuY29kZXJfY2xzKClcbiAgICB0Z3RfZW5jb2RlciA9IGNvcHkuZGVlcGNvcHkoY3R4X2VuY29kZXIpXG4gICAgZm9yIHAgaW4gdGd0X2VuY29kZXIucGFyYW1ldGVycygpOlxuICAgICAgICBwLnJlcXVpcmVzX2dyYWRfKEZhbHNlKVxuICAgIHByZWRpY3RvciA9IElKRVBBUHJlZGljdG9yKGVtYmVkX2RpbT1lbWJlZF9kaW0sIHByZWRfZGltPXByZWRfZGltKVxuICAgIHJldHVybiBjdHhfZW5jb2RlciwgdGd0X2VuY29kZXIsIHByZWRpY3RvclxuXG5cbkB0b3JjaC5ub19ncmFkKClcbmRlZiBlbWFfdXBkYXRlKGN0eF9lbmMsIHRndF9lbmMsIG1vbWVudHVtPTAuOTk2KTpcbiAgICBmb3IgcF9jLCBwX3QgaW4gemlwKGN0eF9lbmMucGFyYW1ldGVycygpLCB0Z3RfZW5jLnBhcmFtZXRlcnMoKSk6XG4gICAgICAgIHBfdC5kYXRhID0gbW9tZW50dW0gKiBwX3QuZGF0YSArICgxIC0gbW9tZW50dW0pICogcF9jLmRhdGFcblxuXG5kZWYgaWplcGFfc3RlcChjdHhfZW5jLCB0Z3RfZW5jLCBwcmVkaWN0b3IsIG9wdGltaXplciwgaW1ncyxcbiAgICAgICAgICAgICAgIGN0eF9tYXNrLCB0YXJnZXRfbWFza3MsIHBvc19lbWJlZCk6XG4gICAgXCJcIlwiU2luZ2xlIEktSkVQQSB0cmFpbmluZyBzdGVwLlxuICAgIGltZ3M6IChCLCAzLCBILCBXKSAgY3R4X21hc2s6IGxpc3Qgb2YgcGF0Y2ggaW5kaWNlcyAoY29udGV4dClcbiAgICB0YXJnZXRfbWFza3M6IGxpc3Qgb2YgbGlzdHMgb2YgcGF0Y2ggaW5kaWNlcyAodGFyZ2V0cylcbiAgICBwb3NfZW1iZWQ6ICgxLCBOX3BhdGNoZXMsIEQpIHBvc2l0aW9uYWwgZW1iZWRkaW5nc1xuICAgIFwiXCJcIlxuICAgICMgQ29udGV4dCBlbmNvZGVyIOKAlCBvbmx5IGNvbnRleHQgcGF0Y2hlc1xuICAgIGN0eF90b2tlbnMgPSBjdHhfZW5jKGltZ3MsIG1hc2s9Y3R4X21hc2spICAgICAgICAgICAjIChCLCBOX2N0eCwgRClcblxuICAgICMgVGFyZ2V0IGVuY29kZXIg4oCUIGZ1bGwgaW1hZ2UsIG5vIGdyYWRcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgYWxsX3RhcmdldF90b2tlbnMgPSB0Z3RfZW5jKGltZ3MpICAgICAgICAgICAgICAgIyAoQiwgTl9hbGwsIEQpXG5cbiAgICAjIFByZWRpY3RvclxuICAgIHRvdGFsX2xvc3MgPSAwLjBcbiAgICBmb3IgdGd0X2lkeCBpbiB0YXJnZXRfbWFza3M6XG4gICAgICAgIHRndF9wb3MgID0gcG9zX2VtYmVkWzosIHRndF9pZHgsIDpdICAgICAgICAgICAgICMgKDEsIE5fdGd0LCBEKVxuICAgICAgICB0Z3RfcG9zICA9IHRndF9wb3MuZXhwYW5kKGltZ3Muc2l6ZSgwKSwgLTEsIC0xKVxuICAgICAgICBwcmVkcyAgICA9IHByZWRpY3RvcihjdHhfdG9rZW5zLCB0Z3RfcG9zKSAgICAgICAgIyAoQiwgTl90Z3QsIEQpXG4gICAgICAgIHRhcmdldHMgID0gYWxsX3RhcmdldF90b2tlbnNbOiwgdGd0X2lkeCwgOl0uZGV0YWNoKClcbiAgICAgICAgdG90YWxfbG9zcyArPSBGLm1zZV9sb3NzKHByZWRzLCB0YXJnZXRzKVxuXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgdG90YWxfbG9zcy5iYWNrd2FyZCgpXG4gICAgb3B0aW1pemVyLnN0ZXAoKVxuICAgIGVtYV91cGRhdGUoY3R4X2VuYywgdGd0X2VuYylcbiAgICByZXR1cm4gdG90YWxfbG9zcy5pdGVtKClcblxuXG5wcmludChcdTAwMjdJLUpFUEE6IGNvbnRleHQgZW5jb2RlciArIEVNQSB0YXJnZXQgZW5jb2RlciArIG5hcnJvdyBwcmVkaWN0b3IuXHUwMDI3KVxucHJpbnQoXHUwMDI3TG9zczogTVNFIGJldHdlZW4gcHJlZGljdG9yIG91dHB1dCBhbmQgdGFyZ2V0IGVuY29kZXIgcGF0Y2ggdG9rZW5zLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWaWRlby1KRVBBIGFuZCBFeHRlbnNpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWLUpFUEEgKEJhcmRlcyBldCBhbC4gMjAyNCkgZXh0ZW5kcyBJLUpFUEEgdG8gdmlkZW8gYnkgcHJlZGljdGluZyBmdXR1cmUgZnJhbWUgcmVwcmVzZW50YXRpb25zIGluIGVtYmVkZGluZyBzcGFjZS4gQSBjb250ZXh0IGNsaXAgKHZpc2libGUgZnJhbWVzKSBpcyBlbmNvZGVkOyB0aGUgcHJlZGljdG9yIG11c3QgcHJvZHVjZSByZXByZXNlbnRhdGlvbnMgb2YgZnV0dXJlIGZyYW1lcyBnaXZlbiB0aGVpciB0ZW1wb3JhbCBwb3NpdGlvbi4gVGhpcyBhcHByb2FjaCBsZWFybnMgdGVtcG9yYWwgZHluYW1pY3Mgd2l0aG91dCByZXF1aXJpbmcgb3B0aWNhbCBmbG93IHN1cGVydmlzaW9uLCBmcmFtZSByZWNvbnN0cnVjdGlvbiwgb3IgY29udHJhc3RpdmUgbmVnYXRpdmVzLiBWLUpFUEEgZmVhdHVyZXMgZ2VuZXJhbGlzZSB3ZWxsIHRvIGFjdGlvbiByZWNvZ25pdGlvbiBiZW5jaG1hcmtzLiBXb3JsZC1KRVBBIChwcm9wb3NlZCBkaXJlY3Rpb24pIGV4dGVuZHMgdGhpcyBwcmluY2lwbGUgdG8gbXVsdGktbW9kYWwgam9pbnQgZW1iZWRkaW5nIGZvciByb2JvdGljcyDigJQgcHJlZGljdCBmdXR1cmUgc3RhdGUgcmVwcmVzZW50YXRpb25zIGZyb20gYWN0aW9ucyBhbmQgb2JzZXJ2YXRpb25zLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5zaWdodCIsInRpdGxlIjoiSkVQQSB2cyBNQUUg4oCUIEFic3RyYWN0IHZzIENvbmNyZXRlIFByZWRpY3Rpb24iLCJjb250ZW50IjoiTUFFXHUwMDI3cyBwaXhlbCByZWNvbnN0cnVjdGlvbiBvYmplY3RpdmUgZm9yY2VzIHRoZSBtb2RlbCB0byBsZWFybiBib3RoIHNlbWFudGljIGNvbnRlbnQgKHdoaWNoIHNjZW5lIGlzIHRoaXM/KSBhbmQgbG93LWxldmVsIGFwcGVhcmFuY2UgKHdoYXQgY29sb3IgaXMgZWFjaCBwaXhlbD8pLiBKRVBBXHUwMDI3cyBlbWJlZGRpbmctc3BhY2UgcHJlZGljdGlvbiBmb3JjZXMgb25seSBzZW1hbnRpYyBjb250ZW50IOKAlCB0aGUgcHJlZGljdG9yIGhhcyBubyBhY2Nlc3MgdG8gcmF3IHRhcmdldCBwaXhlbHMuIE9uIGxpbmVhciBwcm9iZSAod2hpY2ggbWVhc3VyZXMgc2VtYW50aWMgcXVhbGl0eSBvZiBmcm96ZW4gZmVhdHVyZXMpLCBJLUpFUEEgZXhjZWVkcyBNQUUtVmlULUwgYnkgfjMlIG9uIEltYWdlTmV0LiBPbiBmaW5lLXR1bmluZywgYm90aCBtZXRob2RzIHJlYWNoIHNpbWlsYXIgYWNjdXJhY3ksIHNpbmNlIGZpbmUtdHVuaW5nIGNvcnJlY3RzIHJlcHJlc2VudGF0aW9uIGRlZmljaWVuY2llcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIOKAlCBJLUpFUEEgdnMgTUFFIHZzIERJTk8gdnMgVi1KRVBBIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBwYW5kYXMgYXMgcGRcblxuIyBSZXBvcnRlZCBiZW5jaG1hcmsgbnVtYmVycyBmcm9tIHJlc3BlY3RpdmUgcGFwZXJzXG5yZXN1bHRzID0gW1xuICAgIHtcdTAwMjdNZXRob2RcdTAwMjc6IFx1MDAyN01BRSBWaVQtTFx1MDAyNywgICBcdTAwMjdQcmVkaWN0aW9uIFRhcmdldFx1MDAyNzogXHUwMDI3UGl4ZWxzXHUwMDI3LCAgICAgICAgIFx1MDAyN0F1Z21lbnRhdGlvblx1MDAyNzogXHUwMDI3Tm9uZVx1MDAyNyxcbiAgICAgXHUwMDI3TWFza2luZ1x1MDAyNzogXHUwMDI3NzUlIHJhbmRvbVx1MDAyNywgXHUwMDI3TGluZWFyIFByb2JlXHUwMDI3OiA3NS44LCBcdTAwMjdGaW5lLXR1bmVcdTAwMjc6IDg1Ljl9LFxuICAgIHtcdTAwMjdNZXRob2RcdTAwMjc6IFx1MDAyN0ktSkVQQSBWaVQtTFx1MDAyNyxcdTAwMjdQcmVkaWN0aW9uIFRhcmdldFx1MDAyNzogXHUwMDI3RW1iZWRkaW5nc1x1MDAyNywgICAgIFx1MDAyN0F1Z21lbnRhdGlvblx1MDAyNzogXHUwMDI3Tm9uZVx1MDAyNyxcbiAgICAgXHUwMDI3TWFza2luZ1x1MDAyNzogXHUwMDI3QmxvY2sgKDE1LTIwJSlcdTAwMjcsIFx1MDAyN0xpbmVhciBQcm9iZVx1MDAyNzogNzkuMywgXHUwMDI3RmluZS10dW5lXHUwMDI3OiA4Ni43fSxcbiAgICB7XHUwMDI3TWV0aG9kXHUwMDI3OiBcdTAwMjdESU5PIFZpVC1CXHUwMDI3LCAgXHUwMDI3UHJlZGljdGlvbiBUYXJnZXRcdTAwMjc6IFx1MDAyN0NMUyB0b2tlblx1MDAyNywgICAgICBcdTAwMjdBdWdtZW50YXRpb25cdTAwMjc6IFx1MDAyN1N0cm9uZ1x1MDAyNyxcbiAgICAgXHUwMDI3TWFza2luZ1x1MDAyNzogXHUwMDI3Tm9uZVx1MDAyNywgICAgICAgXHUwMDI3TGluZWFyIFByb2JlXHUwMDI3OiA3OC4yLCBcdTAwMjdGaW5lLXR1bmVcdTAwMjc6IDgyLjh9LFxuICAgIHtcdTAwMjdNZXRob2RcdTAwMjc6IFx1MDAyN1YtSkVQQSBWaVQtSFx1MDAyNyxcdTAwMjdQcmVkaWN0aW9uIFRhcmdldFx1MDAyNzogXHUwMDI3VmlkZW8gZW1iZWRkaW5nc1x1MDAyNyxcdTAwMjdBdWdtZW50YXRpb25cdTAwMjc6IFx1MDAyN05vbmVcdTAwMjcsXG4gICAgIFx1MDAyN01hc2tpbmdcdTAwMjc6IFx1MDAyN1NwYXRpby10ZW1wb3JhbFx1MDAyNywgXHUwMDI3TGluZWFyIFByb2JlXHUwMDI3OiA4MS45LCBcdTAwMjdGaW5lLXR1bmVcdTAwMjc6IDg4LjF9LFxuXVxuXG5kZiA9IHBkLkRhdGFGcmFtZShyZXN1bHRzKVxucHJpbnQoZGYudG9fc3RyaW5nKGluZGV4PUZhbHNlKSlcbnByaW50KFx1MDAyN1xcbktleTogSS1KRVBBIGJlYXRzIE1BRSBvbiBsaW5lYXIgcHJvYmUgKCszLjUlKSB3aXRob3V0IGFueSBhdWdtZW50YXRpb24uXHUwMDI3KVxucHJpbnQoXHUwMDI3RmluZS10dW5lIG51bWJlcnMgYXJlIGNsb3NlciDigJQgZnJvemVuIHF1YWxpdHkgaXMgd2hlcmUgdGhlIGdhcCBpcyBsYXJnZXN0Llx1MDAyNykifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiUHJlZGljdGlvbiBUYXJnZXQiLCJBdWdtZW50YXRpb24iLCJNYXNraW5nIiwiTGluZWFyIFByb2JlIiwiU2VtYW50aWMgUXVhbGl0eSJdLCJyb3dzIjpbWyJNQUUgVmlULUwiLCJQaXhlbHMgKHBpeGVsIHNwYWNlKSIsIk5vbmUiLCI3NSUgcmFuZG9tIHBhdGNoZXMiLCI3NS44JSIsIkxvdyAoZmluZS10dW5lIG5lZWRlZCkiXSxbIkktSkVQQSBWaVQtTCIsIlBhdGNoIGVtYmVkZGluZ3MiLCJOb25lIiwiQmxvY2sgdGFyZ2V0cyAoMTUtMjAlKSIsIjc5LjMlIiwiSGlnaCAoZnJvemVuIHVzYWJsZSkiXSxbIkRJTk8gVmlULUIiLCJDTFMgdG9rZW4gKGdsb2JhbCkiLCJTdHJvbmcgKGNyb3BzLCBqaXR0ZXIpIiwiTm9uZSIsIjc4LjIlIiwiSGlnaCAoc2VtYW50aWMgY2x1c3RlcnMpIl0sWyJWLUpFUEEgVmlULUgiLCJWaWRlbyBmcmFtZSBlbWJlZGRpbmdzIiwiTm9uZSIsIlNwYXRpby10ZW1wb3JhbCBibG9jayIsIjgxLjklIiwiSGlnaCAodGVtcG9yYWwgZHluYW1pY3MpIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkktSkVQQSBhY2hpZXZlcyBoaWdoLXF1YWxpdHkgZnJvemVuIHJlcHJlc2VudGF0aW9ucyB3aXRob3V0IHRoZSBhdWdtZW50YXRpb24gZW5naW5lZXJpbmcgcmVxdWlyZWQgYnkgY29udHJhc3RpdmUgbWV0aG9kcy4gSXQgaXMgcGFydGljdWxhcmx5IGF0dHJhY3RpdmUgd2hlbiBhdWdtZW50YXRpb24gZGVzaWduIGlzIGRpZmZpY3VsdCDigJQgZm9yIGV4YW1wbGUsIG1lZGljYWwgaW1hZ2VzIHdoZXJlIGNvbG9yIGppdHRlciBhbmQgcmFuZG9tIGNyb3BwaW5nIG1heSBjaGFuZ2UgY2xpbmljYWwgbWVhbmluZy4gVGhlIHByZWRpY3Rpb24taW4tZW1iZWRkaW5nLXNwYWNlIHByaW5jaXBsZSBpcyBnZW5lcmFsIGFuZCBhcHBsaWVzIHRvIGFueSBtb2RhbGl0eSB3aGVyZSBhIHRhcmdldCBlbmNvZGVyIGNhbiBwcm92aWRlIG1lYW5pbmdmdWwgYWJzdHJhY3QgcmVwcmVzZW50YXRpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBDb25zaWRlcmF0aW9ucyBhbmQgTGltaXRhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkktSkVQQVx1MDAyN3MgbWFza2luZyBzdHJhdGVneSBpcyBzZW5zaXRpdmUgdG8gYmxvY2sgc2l6ZSBhbmQgbnVtYmVyIG9mIHRhcmdldCBibG9ja3MuIFRvbyBmZXcgdGFyZ2V0cyBtYWtlIHRoZSB0YXNrIGVhc3k7IHRvbyBtYW55IGxlYXZlIHRvbyBsaXR0bGUgY29udGV4dCBmb3IgdGhlIHByZWRpY3Rvci4gVGhlIHByZWRpY3RvciBkZXB0aCBpcyBhIGNyaXRpY2FsIGh5cGVycGFyYW1ldGVyOiB0b28gZGVlcCBhIHByZWRpY3RvciBjYW4gcmVjb25zdHJ1Y3QgdGFyZ2V0cyBmcm9tIGNvbnRleHQgd2l0aG91dCBmb3JjaW5nIHRoZSBlbmNvZGVyIHRvIGxlYXJuIGdvb2QgcmVwcmVzZW50YXRpb25zLiBUaGUgRU1BIG1vbWVudHVtIHNjaGVkdWxlICgwLjk5NiDihpIgMS4wLCBjb3NpbmUpIGVuc3VyZXMgdGhlIHRhcmdldCBlbmNvZGVyIHJlbWFpbnMgc3RhYmxlLiBPbmUgcHJhY3RpY2FsIGxpbWl0YXRpb246IEktSkVQQSByZXF1aXJlcyB0aGUgdGFyZ2V0IGVuY29kZXIgdG8gcHJvY2VzcyB0aGUgZnVsbCB1bm1hc2tlZCBpbWFnZSBhdCBldmVyeSBzdGVwLCBkb3VibGluZyB0aGUgZm9yd2FyZCBwYXNzIGNvc3QgY29tcGFyZWQgdG8gTUFFLCB3aGljaCBlbmNvZGVzIG9ubHkgdmlzaWJsZSBwYXRjaGVzLiBBdCBWaVQtSCBzY2FsZSwgdGhpcyBtYWtlcyBJLUpFUEEgcm91Z2hseSAyw5cgbW9yZSBjb21wdXRlLWludGVuc2l2ZSBwZXIgc3RlcCB0aGFuIE1BRSBhdCBlcXVhbCBiYXRjaCBzaXplLiJ9XQ=="
---
# JEPA — Joint-Embedding Predictive Architecture

JEPA (Joint-Embedding Predictive Architecture, LeCun 2022) argues that the right objective for self-supervised learning is to predict abstract representations of the world, not low-level sensory details. Instead of asking a model to reconstruct pixels (MAE) or match augmented views (SimCLR, DINO), a JEPA model learns to predict the representation of a masked or future region from the context. The crucial difference is where prediction happens: in embedding space, not pixel space. This frees the model from learning to reconstruct irrelevant texture and noise, focusing the capacity on semantic content.

- I-JEPA (He et al. 2023): predict patch-level representations of masked target blocks from context encoder output.
- Target encoder: EMA of context encoder — slowly evolving stable targets, prevents mode collapse.
- Predictor: narrow Transformer with positional conditioning — predicts abstract content, never raw pixels.
- No augmentation engineering: the masking strategy alone creates the self-supervised signal.
- V-JEPA (Bardes et al. 2024): temporal extension — predict future frame representations from past context.

## Prediction in Embedding Space vs Pixel Space

MAE reconstructs pixel values of masked patches. This forces the encoder to capture both semantic content and low-level appearance (texture, color, noise) — since the decoder must recover pixel-accurate values. I-JEPA instead asks: given the representation of the visible context, predict the representation of the masked target as computed by a target encoder. The predictor never sees pixels of the target; it only sees the position of the target block and the context representation. This makes the problem strictly semantic — there is no gradient signal for pixel noise.

## I-JEPA Masking Strategy

I-JEPA (Image Joint-Embedding Predictive Architecture, He et al. 2023) uses a carefully designed masking strategy to create a challenging but solvable predictive task. The image is divided into patches. A context region is selected (a random block covering roughly 85% of the image with some exclusions). Several target blocks (4 on average) are sampled from the remaining positions — these are the regions the predictor must reconstruct in embedding space. The predictor receives: (1) the context encoder output, and (2) the positional encoding of each target block. It must output a representation that matches the target encoder's representation at those positions.

```python
import torch
import random


def sample_block(grid_h: int, grid_w: int, min_scale: float, max_scale: float,
                 aspect_min: float = 0.75, aspect_max: float = 1.5):
    """Sample a random rectangular block on the patch grid."""
    scale = random.uniform(min_scale, max_scale)
    area = int(grid_h * grid_w * scale)
    aspect = random.uniform(aspect_min, aspect_max)
    h = int((area * aspect) ** 0.5)
    w = int(area / max(h, 1))
    h, w = min(h, grid_h), min(w, grid_w)
    top  = random.randint(0, grid_h - h)
    left = random.randint(0, grid_w - w)
    indices = []
    for r in range(top, top + h):
        for c in range(left, left + w):
            indices.append(r * grid_w + c)
    return sorted(set(indices))


def ijepa_masks(grid_h=14, grid_w=14, n_targets=4,
                ctx_scale=(0.85, 1.0), tgt_scale=(0.15, 0.2)):
    """Return context_mask and list of target_masks (patch indices)."""
    all_patches = list(range(grid_h * grid_w))
    ctx_block   = sample_block(grid_h, grid_w, *ctx_scale)
    # Context: all patches NOT excluded by any target block
    target_masks = []
    excluded = set()
    for _ in range(n_targets):
        tgt = sample_block(grid_h, grid_w, *tgt_scale)
        target_masks.append(tgt)
        excluded.update(tgt)
    context_mask = [p for p in ctx_block if p not in excluded]
    return context_mask, target_masks


ctx, targets = ijepa_masks()
print(f'Context patches: {len(ctx)}  |  Target blocks: {len(targets)}')
for i, t in enumerate(targets):
    print(f'  Target {i}: {len(t)} patches, first={t[0]}, last={t[-1]}')
```

## Predictor with Positional Conditioning

The predictor in I-JEPA is a narrow Transformer that takes two inputs: (1) the context encoder's output tokens (CLS + context patch tokens), and (2) a set of learnable mask tokens, one per target patch, with positional embeddings injected at the target positions. The predictor must attend from each mask token to the context tokens and produce a prediction that matches the target encoder representation at that position. The predictor is intentionally shallow (4 Transformer blocks) — it should not be so powerful that it can solve the task without learning good context representations.

```python
import torch
import torch.nn as nn


class IJEPAPredictor(nn.Module):
    """Narrow Transformer predictor: context tokens + target positions -> target representations."""

    def __init__(self, embed_dim: int = 768, pred_dim: int = 384,
                 depth: int = 4, num_heads: int = 6):
        super().__init__()
        self.proj_in  = nn.Linear(embed_dim, pred_dim)   # project context to pred_dim
        self.mask_tok = nn.Parameter(torch.randn(1, 1, pred_dim) * 0.02)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=pred_dim, nhead=num_heads,
            dim_feedforward=pred_dim * 4, dropout=0.0, batch_first=True,
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=depth)
        self.proj_out = nn.Linear(pred_dim, embed_dim)   # back to target space

    def forward(self, ctx_tokens: torch.Tensor,
                target_pos_emb: torch.Tensor) -> torch.Tensor:
        """ctx_tokens: (B, N_ctx, D)  target_pos_emb: (B, N_tgt, D)
        Returns predictions: (B, N_tgt, D) in target encoder space.
        """
        B, N_tgt, _ = target_pos_emb.shape
        ctx = self.proj_in(ctx_tokens)                        # (B, N_ctx, pred_dim)
        # Mask tokens initialised identically + positional offset
        mask_toks = self.mask_tok.expand(B, N_tgt, -1)
        mask_toks = mask_toks + self.proj_in(target_pos_emb)  # inject target position
        tokens = torch.cat([ctx, mask_toks], dim=1)           # (B, N_ctx+N_tgt, pred_dim)
        out    = self.transformer(tokens)                      # (B, N_ctx+N_tgt, pred_dim)
        preds  = self.proj_out(out[:, -N_tgt:, :])            # (B, N_tgt, D)
        return preds


pred = IJEPAPredictor(embed_dim=768, pred_dim=384)
ctx  = torch.randn(2, 120, 768)
tgt_pos = torch.randn(2, 30, 768)
out = pred(ctx, tgt_pos)
print('Predictor output shape:', out.shape)   # (2, 30, 768)
```

## I-JEPA Training Loop

The training loop has three components: a context encoder (updated by gradient), a target encoder (EMA of context encoder, no gradient), and the predictor. The context encoder processes only the unmasked context patches. The target encoder processes the full image and provides the target representations. The predictor takes context encoder output + target position embeddings and produces predictions. The loss is MSE between the predictor output and the target encoder's patch tokens at the target positions. The EMA momentum increases from 0.996 to 1.0 over training (cosine schedule).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import copy


def build_ijepa(encoder_cls, embed_dim=768, pred_dim=384, momentum=0.996):
    ctx_encoder = encoder_cls()
    tgt_encoder = copy.deepcopy(ctx_encoder)
    for p in tgt_encoder.parameters():
        p.requires_grad_(False)
    predictor = IJEPAPredictor(embed_dim=embed_dim, pred_dim=pred_dim)
    return ctx_encoder, tgt_encoder, predictor


@torch.no_grad()
def ema_update(ctx_enc, tgt_enc, momentum=0.996):
    for p_c, p_t in zip(ctx_enc.parameters(), tgt_enc.parameters()):
        p_t.data = momentum * p_t.data + (1 - momentum) * p_c.data


def ijepa_step(ctx_enc, tgt_enc, predictor, optimizer, imgs,
               ctx_mask, target_masks, pos_embed):
    """Single I-JEPA training step.
    imgs: (B, 3, H, W)  ctx_mask: list of patch indices (context)
    target_masks: list of lists of patch indices (targets)
    pos_embed: (1, N_patches, D) positional embeddings
    """
    # Context encoder — only context patches
    ctx_tokens = ctx_enc(imgs, mask=ctx_mask)           # (B, N_ctx, D)

    # Target encoder — full image, no grad
    with torch.no_grad():
        all_target_tokens = tgt_enc(imgs)               # (B, N_all, D)

    # Predictor
    total_loss = 0.0
    for tgt_idx in target_masks:
        tgt_pos  = pos_embed[:, tgt_idx, :]             # (1, N_tgt, D)
        tgt_pos  = tgt_pos.expand(imgs.size(0), -1, -1)
        preds    = predictor(ctx_tokens, tgt_pos)        # (B, N_tgt, D)
        targets  = all_target_tokens[:, tgt_idx, :].detach()
        total_loss += F.mse_loss(preds, targets)

    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()
    ema_update(ctx_enc, tgt_enc)
    return total_loss.item()


print('I-JEPA: context encoder + EMA target encoder + narrow predictor.')
print('Loss: MSE between predictor output and target encoder patch tokens.')
```

## Video-JEPA and Extensions

V-JEPA (Bardes et al. 2024) extends I-JEPA to video by predicting future frame representations in embedding space. A context clip (visible frames) is encoded; the predictor must produce representations of future frames given their temporal position. This approach learns temporal dynamics without requiring optical flow supervision, frame reconstruction, or contrastive negatives. V-JEPA features generalise well to action recognition benchmarks. World-JEPA (proposed direction) extends this principle to multi-modal joint embedding for robotics — predict future state representations from actions and observations.

> **JEPA vs MAE — Abstract vs Concrete Prediction**: MAE's pixel reconstruction objective forces the model to learn both semantic content (which scene is this?) and low-level appearance (what color is each pixel?). JEPA's embedding-space prediction forces only semantic content — the predictor has no access to raw target pixels. On linear probe (which measures semantic quality of frozen features), I-JEPA exceeds MAE-ViT-L by ~3% on ImageNet. On fine-tuning, both methods reach similar accuracy, since fine-tuning corrects representation deficiencies.

## Comparison — I-JEPA vs MAE vs DINO vs V-JEPA

```python
import pandas as pd

# Reported benchmark numbers from respective papers
results = [
    {'Method': 'MAE ViT-L',   'Prediction Target': 'Pixels',         'Augmentation': 'None',
     'Masking': '75% random', 'Linear Probe': 75.8, 'Fine-tune': 85.9},
    {'Method': 'I-JEPA ViT-L','Prediction Target': 'Embeddings',     'Augmentation': 'None',
     'Masking': 'Block (15-20%)', 'Linear Probe': 79.3, 'Fine-tune': 86.7},
    {'Method': 'DINO ViT-B',  'Prediction Target': 'CLS token',      'Augmentation': 'Strong',
     'Masking': 'None',       'Linear Probe': 78.2, 'Fine-tune': 82.8},
    {'Method': 'V-JEPA ViT-H','Prediction Target': 'Video embeddings','Augmentation': 'None',
     'Masking': 'Spatio-temporal', 'Linear Probe': 81.9, 'Fine-tune': 88.1},
]

df = pd.DataFrame(results)
print(df.to_string(index=False))
print('\nKey: I-JEPA beats MAE on linear probe (+3.5%) without any augmentation.')
print('Fine-tune numbers are closer — frozen quality is where the gap is largest.')
```

| Method | Prediction Target | Augmentation | Masking | Linear Probe | Semantic Quality |
| --- | --- | --- | --- | --- | --- |
| MAE ViT-L | Pixels (pixel space) | None | 75% random patches | 75.8% | Low (fine-tune needed) |
| I-JEPA ViT-L | Patch embeddings | None | Block targets (15-20%) | 79.3% | High (frozen usable) |
| DINO ViT-B | CLS token (global) | Strong (crops, jitter) | None | 78.2% | High (semantic clusters) |
| V-JEPA ViT-H | Video frame embeddings | None | Spatio-temporal block | 81.9% | High (temporal dynamics) |

I-JEPA achieves high-quality frozen representations without the augmentation engineering required by contrastive methods. It is particularly attractive when augmentation design is difficult — for example, medical images where color jitter and random cropping may change clinical meaning. The prediction-in-embedding-space principle is general and applies to any modality where a target encoder can provide meaningful abstract representations.

## Practical Considerations and Limitations

I-JEPA's masking strategy is sensitive to block size and number of target blocks. Too few targets make the task easy; too many leave too little context for the predictor. The predictor depth is a critical hyperparameter: too deep a predictor can reconstruct targets from context without forcing the encoder to learn good representations. The EMA momentum schedule (0.996 → 1.0, cosine) ensures the target encoder remains stable. One practical limitation: I-JEPA requires the target encoder to process the full unmasked image at every step, doubling the forward pass cost compared to MAE, which encodes only visible patches. At ViT-H scale, this makes I-JEPA roughly 2× more compute-intensive per step than MAE at equal batch size.

