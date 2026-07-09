---
title: "Topic Modeling — LDA, NMF, and BTM"
slug: "topic-modeling"
description: "Latent Dirichlet Allocation from its generative model to Gibbs sampling inference, NMF for topic extraction, BTM for short texts, and topic coherence evaluation with Cv score and NPMI."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG9waWMgbW9kZWxpbmcgZGlzY292ZXJzIHRoZSBsYXRlbnQgdGhlbWF0aWMgc3RydWN0dXJlIGluIGEgY29ycHVzIG9mIGRvY3VtZW50cyB3aXRob3V0IHN1cGVydmlzaW9uLiBHaXZlbiBhIGJhZy1vZi13b3JkcyBtYXRyaXgsIGl0IHJlY292ZXJzIHRvcGljcyAoZGlzdHJpYnV0aW9ucyBvdmVyIHdvcmRzKSBhbmQgZG9jdW1lbnQtdG9waWMgbWl4dHVyZXMuIFRoZSB0d28gZG9taW5hbnQgYXBwcm9hY2hlcyDigJQgTERBIChwcm9iYWJpbGlzdGljKSBhbmQgTk1GIChtYXRyaXggZmFjdG9yaXphdGlvbikg4oCUIGRpZmZlciBpbiB0aGVpciBhc3N1bXB0aW9ucyBidXQgb2Z0ZW4gcHJvZHVjZSBjb21wYXJhYmxlIHJlc3VsdHMgb24gY2xlYW4gY29ycG9yYS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMREEgR2VuZXJhdGl2ZSBNb2RlbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTERBIChCbGVpIGV0IGFsLiAyMDAzKSBhc3N1bWVzIHRoZSBmb2xsb3dpbmcgZ2VuZXJhdGl2ZSBwcm9jZXNzOiBmb3IgZWFjaCBkb2N1bWVudCBkLCBkcmF3IGEgdG9waWMgcHJvcG9ydGlvbiB2ZWN0b3IgzrhfZCB+IERpcijOsSkuIEZvciBlYWNoIHdvcmQgcG9zaXRpb24sIGRyYXcgYSB0b3BpYyB64oKZIH4gQ2F0ZWdvcmljYWwozrhfZCksIHRoZW4gZHJhdyB0aGUgd29yZCB34oKZIH4gQ2F0ZWdvcmljYWwozrJfeikgd2hlcmUgzrJfayBpcyB0aGUgd29yZCBkaXN0cmlidXRpb24gZm9yIHRvcGljIGsgKM6yX2sgfiBEaXIozrcpKS4gVGhlIERpcmljaGxldCBwcmlvciDOsSBjb250cm9scyBkb2N1bWVudCBzcGFyc2l0eSAoc21hbGwgzrEg4oaSIGRvY3VtZW50cyBmb2N1cyBvbiBmZXcgdG9waWNzKTsgzrcgY29udHJvbHMgdG9waWMgc3BhcnNpdHkgKHNtYWxsIM63IOKGkiB0b3BpY3MgZm9jdXMgb24gZmV3IHdvcmRzKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBsZGFfZ2liYnMoY29ycHVzLCB2b2NhYl9zaXplLCBLLCBhbHBoYT0wLjEsIGV0YT0wLjAxLCBuX2l0ZXI9MTAwKTpcbiAgICBcIlwiXCJDb2xsYXBzZWQgR2liYnMgc2FtcGxpbmcgZm9yIExEQSAocGVkYWdvZ2ljYWwgaW1wbGVtZW50YXRpb24pLlwiXCJcIlxuICAgIEQgPSBsZW4oY29ycHVzKVxuICAgIGRvY190b3BpYyA9IG5wLnplcm9zKChELCBLKSwgZHR5cGU9aW50KVxuICAgIHRvcGljX3dvcmQgPSBucC56ZXJvcygoSywgdm9jYWJfc2l6ZSksIGR0eXBlPWludClcbiAgICB0b3BpY190b3RhbCA9IG5wLnplcm9zKEssIGR0eXBlPWludClcblxuICAgICMgUmFuZG9tIGluaXRpYWxpc2F0aW9uXG4gICAgYXNzaWdubWVudHMgPSBbXVxuICAgIGZvciBkLCBkb2MgaW4gZW51bWVyYXRlKGNvcnB1cyk6XG4gICAgICAgIHpfZG9jID0gW11cbiAgICAgICAgZm9yIHcgaW4gZG9jOlxuICAgICAgICAgICAgeiA9IG5wLnJhbmRvbS5yYW5kaW50KEspXG4gICAgICAgICAgICB6X2RvYy5hcHBlbmQoeilcbiAgICAgICAgICAgIGRvY190b3BpY1tkLCB6XSArPSAxXG4gICAgICAgICAgICB0b3BpY193b3JkW3osIHddICs9IDFcbiAgICAgICAgICAgIHRvcGljX3RvdGFsW3pdICs9IDFcbiAgICAgICAgYXNzaWdubWVudHMuYXBwZW5kKHpfZG9jKVxuXG4gICAgIyBHaWJicyBpdGVyYXRpb25zXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl9pdGVyKTpcbiAgICAgICAgZm9yIGQsIGRvYyBpbiBlbnVtZXJhdGUoY29ycHVzKTpcbiAgICAgICAgICAgIGZvciBpLCB3IGluIGVudW1lcmF0ZShkb2MpOlxuICAgICAgICAgICAgICAgIHogPSBhc3NpZ25tZW50c1tkXVtpXVxuICAgICAgICAgICAgICAgIGRvY190b3BpY1tkLCB6XSAtPSAxXG4gICAgICAgICAgICAgICAgdG9waWNfd29yZFt6LCB3XSAtPSAxXG4gICAgICAgICAgICAgICAgdG9waWNfdG90YWxbel0gLT0gMVxuICAgICAgICAgICAgICAgICMgQ29uZGl0aW9uYWwgZGlzdHJpYnV0aW9uIHAoeiB8IHJlc3QpXG4gICAgICAgICAgICAgICAgbGlrZWxpaG9vZCA9ICh0b3BpY193b3JkWzosIHddICsgZXRhKSAvICh0b3BpY190b3RhbCArIHZvY2FiX3NpemUgKiBldGEpXG4gICAgICAgICAgICAgICAgcHJpb3IgPSBkb2NfdG9waWNbZF0gKyBhbHBoYVxuICAgICAgICAgICAgICAgIHAgPSBsaWtlbGlob29kICogcHJpb3JcbiAgICAgICAgICAgICAgICBwIC89IHAuc3VtKClcbiAgICAgICAgICAgICAgICB6X25ldyA9IG5wLnJhbmRvbS5jaG9pY2UoSywgcD1wKVxuICAgICAgICAgICAgICAgIGFzc2lnbm1lbnRzW2RdW2ldID0gel9uZXdcbiAgICAgICAgICAgICAgICBkb2NfdG9waWNbZCwgel9uZXddICs9IDFcbiAgICAgICAgICAgICAgICB0b3BpY193b3JkW3pfbmV3LCB3XSArPSAxXG4gICAgICAgICAgICAgICAgdG9waWNfdG90YWxbel9uZXddICs9IDFcblxuICAgIHRoZXRhID0gKGRvY190b3BpYyArIGFscGhhKSAvIChkb2NfdG9waWMgKyBhbHBoYSkuc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcbiAgICBwaGkgPSAodG9waWNfd29yZCArIGV0YSkgLyAodG9waWNfd29yZCArIGV0YSkuc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcbiAgICByZXR1cm4gdGhldGEsIHBoaVxuXG5wcmludChcdTAwMjdMREEgR2liYnMgc2FtcGxlciByZWFkeS4gUGFzcyB0b2tlbmlzZWQgaW50ZWdlciBjb3JwdXMuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxEQSBJbmZlcmVuY2Ugd2l0aCBza2xlYXJuIGFuZCBweUxEQXZpcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgZmV0Y2hfMjBuZXdzZ3JvdXBzXG5mcm9tIHNrbGVhcm4uZmVhdHVyZV9leHRyYWN0aW9uLnRleHQgaW1wb3J0IENvdW50VmVjdG9yaXplclxuZnJvbSBza2xlYXJuLmRlY29tcG9zaXRpb24gaW1wb3J0IExhdGVudERpcmljaGxldEFsbG9jYXRpb25cblxuY2F0cyA9IFtcdTAwMjdzY2kuc3BhY2VcdTAwMjcsIFx1MDAyN3JlYy5hdXRvc1x1MDAyNywgXHUwMDI3dGFsay5wb2xpdGljcy5ndW5zXHUwMDI3LCBcdTAwMjdjb21wLmdyYXBoaWNzXHUwMDI3XVxubmV3cyA9IGZldGNoXzIwbmV3c2dyb3VwcyhzdWJzZXQ9XHUwMDI3dHJhaW5cdTAwMjcsIGNhdGVnb3JpZXM9Y2F0cyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgcmVtb3ZlPShcdTAwMjdoZWFkZXJzXHUwMDI3LCBcdTAwMjdmb290ZXJzXHUwMDI3LCBcdTAwMjdxdW90ZXNcdTAwMjcpKVxuXG52ZWMgPSBDb3VudFZlY3Rvcml6ZXIobWF4X2ZlYXR1cmVzPTUwMDAsIHN0b3Bfd29yZHM9XHUwMDI3ZW5nbGlzaFx1MDAyNyxcbiAgICAgICAgICAgICAgICAgICAgICBtaW5fZGY9NSwgbWF4X2RmPTAuOSlcblhfYm93ID0gdmVjLmZpdF90cmFuc2Zvcm0obmV3cy5kYXRhKVxuZmVhdHVyZV9uYW1lcyA9IG5wLmFycmF5KHZlYy5nZXRfZmVhdHVyZV9uYW1lc19vdXQoKSlcblxuSyA9IDhcbmxkYSA9IExhdGVudERpcmljaGxldEFsbG9jYXRpb24obl9jb21wb25lbnRzPUssIG1heF9pdGVyPTIwLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGVhcm5pbmdfbWV0aG9kPVx1MDAyN29ubGluZVx1MDAyNyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJhbmRvbV9zdGF0ZT00Miwgbl9qb2JzPS0xKVxuZG9jX3RvcGljcyA9IGxkYS5maXRfdHJhbnNmb3JtKFhfYm93KVxuXG5mb3IgayBpbiByYW5nZShLKTpcbiAgICB0b3BfaWR4ID0gbnAuYXJnc29ydChsZGEuY29tcG9uZW50c19ba10pWy0xMDpdWzo6LTFdXG4gICAgdG9wX3N0ciA9IFx1MDAyNyB8IFx1MDAyNy5qb2luKGZlYXR1cmVfbmFtZXNbdG9wX2lkeF0pXG4gICAgcHJpbnQoZlx1MDAyN1RvcGljIHtrOjJkfToge3RvcF9zdHJ9XHUwMDI3KVxuXG5wcmludChmXHUwMDI3XFxuUGVycGxleGl0eToge2xkYS5wZXJwbGV4aXR5KFhfYm93KTouMWZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0RvYy10b3BpYyBtYXRyaXggc2hhcGU6IHtkb2NfdG9waWNzLnNoYXBlfVx1MDAyNylcblxudHJ5OlxuICAgIGltcG9ydCBweUxEQXZpcy5za2xlYXJuXG4gICAgcGFuZWwgPSBweUxEQXZpcy5za2xlYXJuLnByZXBhcmUobGRhLCBYX2JvdywgdmVjLCBtZHM9XHUwMDI3dHNuZVx1MDAyNylcbiAgICBweUxEQXZpcy5zYXZlX2h0bWwocGFuZWwsIFx1MDAyN2xkYV92aXMuaHRtbFx1MDAyNylcbiAgICBwcmludChcdTAwMjdJbnRlcmFjdGl2ZSB2aXN1YWxpc2F0aW9uIHNhdmVkIHRvIGxkYV92aXMuaHRtbFx1MDAyNylcbmV4Y2VwdCBJbXBvcnRFcnJvcjpcbiAgICBwcmludChcdTAwMjdwaXAgaW5zdGFsbCBweUxEQXZpcyBmb3IgaW50ZXJhY3RpdmUgdG9waWMgZXhwbG9yZXJcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJIeXBlcnBhcmFtZXRlcnM6IGFscGhhIGFuZCBldGEiLCJjb250ZW50IjoiYWxwaGEgKGRvY3VtZW50IERpcmljaGxldCBwcmlvcik6IHNtYWxsZXIgYWxwaGEgKDAuMDHigJMwLjEpIOKGkiBkb2N1bWVudHMgYXJlIHNwYXJzZSBvdmVyIHRvcGljcywgbW9yZSBmb2N1c2VkLiBMYXJnZXIgYWxwaGEgKDEuMCkg4oaSIGRvY3VtZW50cyBibGVuZCBtYW55IHRvcGljcy4gZXRhICh0b3BpYyBEaXJpY2hsZXQgcHJpb3IpOiBzbWFsbGVyIGV0YSDihpIgdG9waWNzIGFyZSBzcGFyc2Ugb3ZlciB2b2NhYnVsYXJ5IChzaGFycGVyLCBtb3JlIGNvaGVyZW50IHRvcGljcykuIEEgZ29vZCBkZWZhdWx0IGlzIGFscGhhID0gNTAvSyBhbmQgZXRhID0gMC4wMS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOTUYgZm9yIFRvcGljIE1vZGVsaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOb24tbmVnYXRpdmUgTWF0cml4IEZhY3Rvcml6YXRpb24gZGVjb21wb3NlcyB0aGUgVEYtSURGIG1hdHJpeCBWIOKJiCBXSCB3aGVyZSBXIOKIiCDihJ3igorigb/Lo+G0tyAoZG9jdW1lbnQtdG9waWMpIGFuZCBIIOKIiCDihJ3igorhtLfLo+G1myAodG9waWMtd29yZCkuIFRoZSBub24tbmVnYXRpdml0eSBjb25zdHJhaW50IHByb2R1Y2VzIGFkZGl0aXZlLCBwYXJ0cy1iYXNlZCB0b3BpY3MuIE5NRiBpcyBvcHRpbWlzZWQgdmlhIGFsdGVybmF0aW5nIG5vbi1uZWdhdGl2ZSBsZWFzdCBzcXVhcmVzIHVwZGF0ZXMuIFVubGlrZSBMREEsIE5NRiBoYXMgbm8gcHJvYmFiaWxpc3RpYyBpbnRlcnByZXRhdGlvbiBhbmQgbm8gYnVpbHQtaW4gcmVndWxhcmlzYXRpb24g4oCUIGl0IHRlbmRzIHRvIHByb2R1Y2UgdG9waWNzIHRoYXQgYXJlIG1vcmUgc3Ryb25nbHkgZHJpdmVuIGJ5IGZyZXF1ZW50IHRlcm1zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgZmV0Y2hfMjBuZXdzZ3JvdXBzXG5mcm9tIHNrbGVhcm4uZmVhdHVyZV9leHRyYWN0aW9uLnRleHQgaW1wb3J0IFRmaWRmVmVjdG9yaXplciwgQ291bnRWZWN0b3JpemVyXG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgTk1GLCBMYXRlbnREaXJpY2hsZXRBbGxvY2F0aW9uXG5cbmNhdHMgPSBbXHUwMDI3c2NpLnNwYWNlXHUwMDI3LCBcdTAwMjdyZWMuYXV0b3NcdTAwMjcsIFx1MDAyN3RhbGsucG9saXRpY3MuZ3Vuc1x1MDAyN11cbm5ld3MgPSBmZXRjaF8yMG5ld3Nncm91cHMoc3Vic2V0PVx1MDAyN3RyYWluXHUwMDI3LCBjYXRlZ29yaWVzPWNhdHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgIHJlbW92ZT0oXHUwMDI3aGVhZGVyc1x1MDAyNywgXHUwMDI3Zm9vdGVyc1x1MDAyNywgXHUwMDI3cXVvdGVzXHUwMDI3KSlcblxudGZpZGZfdmVjID0gVGZpZGZWZWN0b3JpemVyKG1heF9mZWF0dXJlcz0zMDAwLCBzdG9wX3dvcmRzPVx1MDAyN2VuZ2xpc2hcdTAwMjcsIG1pbl9kZj01KVxuWF90ZmlkZiA9IHRmaWRmX3ZlYy5maXRfdHJhbnNmb3JtKG5ld3MuZGF0YSlcbm5hbWVzX3RmaWRmID0gbnAuYXJyYXkodGZpZGZfdmVjLmdldF9mZWF0dXJlX25hbWVzX291dCgpKVxuXG5jb3VudF92ZWMgPSBDb3VudFZlY3Rvcml6ZXIobWF4X2ZlYXR1cmVzPTMwMDAsIHN0b3Bfd29yZHM9XHUwMDI3ZW5nbGlzaFx1MDAyNywgbWluX2RmPTUpXG5YX2JvdyA9IGNvdW50X3ZlYy5maXRfdHJhbnNmb3JtKG5ld3MuZGF0YSlcbm5hbWVzX2JvdyA9IG5wLmFycmF5KGNvdW50X3ZlYy5nZXRfZmVhdHVyZV9uYW1lc19vdXQoKSlcblxuSyA9IDVcbm5tZiA9IE5NRihuX2NvbXBvbmVudHM9SywgcmFuZG9tX3N0YXRlPTQyLCBtYXhfaXRlcj01MDAsIGFscGhhX1c9MC4wMSlcbldfbm1mID0gbm1mLmZpdF90cmFuc2Zvcm0oWF90ZmlkZilcblxubGRhID0gTGF0ZW50RGlyaWNobGV0QWxsb2NhdGlvbihuX2NvbXBvbmVudHM9SywgcmFuZG9tX3N0YXRlPTQyLCBuX2pvYnM9LTEpXG5XX2xkYSA9IGxkYS5maXRfdHJhbnNmb3JtKFhfYm93KVxuXG5wcmludChcdTAwMjc9PT0gTk1GIFRvcGljcyAoVEYtSURGKSA9PT1cdTAwMjcpXG5mb3IgayBpbiByYW5nZShLKTpcbiAgICB0b3AgPSBcdTAwMjcgfCBcdTAwMjcuam9pbihuYW1lc190ZmlkZltucC5hcmdzb3J0KG5tZi5jb21wb25lbnRzX1trXSlbLTg6XVs6Oi0xXV0pXG4gICAgcHJpbnQoZlx1MDAyNyAge2t9OiB7dG9wfVx1MDAyNylcblxucHJpbnQoXHUwMDI3XFxuPT09IExEQSBUb3BpY3MgKENvdW50cykgPT09XHUwMDI3KVxuZm9yIGsgaW4gcmFuZ2UoSyk6XG4gICAgdG9wID0gXHUwMDI3IHwgXHUwMDI3LmpvaW4obmFtZXNfYm93W25wLmFyZ3NvcnQobGRhLmNvbXBvbmVudHNfW2tdKVstODpdWzo6LTFdXSlcbiAgICBwcmludChmXHUwMDI3ICB7a306IHt0b3B9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJUTSBmb3IgU2hvcnQgVGV4dHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIExEQSBzdHJ1Z2dsZXMgd2l0aCBzaG9ydCB0ZXh0cyAodHdlZXRzLCBwcm9kdWN0IHJldmlld3MpOiBhIDEwLXdvcmQgZG9jdW1lbnQgaGFzIHRvbyBmZXcgd29yZCBjby1vY2N1cnJlbmNlcyB0byBpbmZlciByZWxpYWJsZSB0b3BpYyBwcm9wb3J0aW9ucy4gQml0ZXJtIFRvcGljIE1vZGVsIChCVE0pIG9wZXJhdGVzIGF0IHRoZSBjb3JwdXMgbGV2ZWw6IGl0IG1vZGVscyB0aGUgZGlzdHJpYnV0aW9uIG92ZXIgYml0ZXJtcyAodW5vcmRlcmVkIHdvcmQgcGFpcnMpIGRpcmVjdGx5LiBCeSBhZ2dyZWdhdGluZyBjby1vY2N1cnJlbmNlcyBhY3Jvc3MgdGhlIHdob2xlIGNvcnB1cywgQlRNIG92ZXJjb21lcyB0aGUgZGF0YSBzcGFyc2l0eSBwcm9ibGVtIGluaGVyZW50IHRvIHNob3J0IGRvY3VtZW50cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUb3BpYyBDb2hlcmVuY2UgRXZhbHVhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGVycGxleGl0eSBtZWFzdXJlcyBoZWxkLW91dCBsaWtlbGlob29kIGJ1dCBjb3JyZWxhdGVzIHBvb3JseSB3aXRoIGh1bWFuIGp1ZGdlbWVudCBvZiB0b3BpYyBxdWFsaXR5LiBDb2hlcmVuY2UgbWV0cmljcyBtZWFzdXJlIHRoZSBzZW1hbnRpYyByZWxhdGVkbmVzcyBvZiB0b3Agd29yZHMgaW4gZWFjaCB0b3BpYy4gVGhlIEN2IHNjb3JlIHVzZXMgc2xpZGluZy13aW5kb3cgUE1JIChQb2ludHdpc2UgTXV0dWFsIEluZm9ybWF0aW9uKSBjb21wdXRlZCBvdmVyIHJlZmVyZW5jZSBjb3JwdXMgY28tb2NjdXJyZW5jZXMuIE5QTUkgPSBQTUkod+KCgSx34oKCKS8oLWxvZyBwKHfigoEsd+KCgikpIG5vcm1hbGlzZXMgUE1JIHRvIFstMSwxXS4gQ3Yg4omIIDAuNCBpcyBtZWRpb2NyZTsgQ3YgXHUwMDNlIDAuNTUgaXMgZ29vZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGZldGNoXzIwbmV3c2dyb3Vwc1xuZnJvbSBza2xlYXJuLmZlYXR1cmVfZXh0cmFjdGlvbi50ZXh0IGltcG9ydCBDb3VudFZlY3Rvcml6ZXJcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBMYXRlbnREaXJpY2hsZXRBbGxvY2F0aW9uXG5cbmNhdHMgPSBbXHUwMDI3c2NpLnNwYWNlXHUwMDI3LCBcdTAwMjdyZWMuYXV0b3NcdTAwMjcsIFx1MDAyN2NvbXAuZ3JhcGhpY3NcdTAwMjcsIFx1MDAyN3RhbGsucG9saXRpY3MuZ3Vuc1x1MDAyN11cbm5ld3MgPSBmZXRjaF8yMG5ld3Nncm91cHMoc3Vic2V0PVx1MDAyN3RyYWluXHUwMDI3LCBjYXRlZ29yaWVzPWNhdHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgIHJlbW92ZT0oXHUwMDI3aGVhZGVyc1x1MDAyNywgXHUwMDI3Zm9vdGVyc1x1MDAyNywgXHUwMDI3cXVvdGVzXHUwMDI3KSlcblxudHJ5OlxuICAgIGltcG9ydCBnZW5zaW1cbiAgICBpbXBvcnQgZ2Vuc2ltLmNvcnBvcmEgYXMgY29ycG9yYVxuICAgIGZyb20gZ2Vuc2ltLm1vZGVscyBpbXBvcnQgQ29oZXJlbmNlTW9kZWwsIExkYU1vZGVsXG5cbiAgICAjIFRva2VuaXNlIGFuZCBmaWx0ZXJcbiAgICB0ZXh0cyA9IFtbdy5sb3dlcigpIGZvciB3IGluIGRvYy5zcGxpdCgpIGlmIGxlbih3KSBcdTAwM2UgM11cbiAgICAgICAgICAgICAgZm9yIGRvYyBpbiBuZXdzLmRhdGFdXG4gICAgZGljdGlvbmFyeSA9IGNvcnBvcmEuRGljdGlvbmFyeSh0ZXh0cylcbiAgICBkaWN0aW9uYXJ5LmZpbHRlcl9leHRyZW1lcyhub19iZWxvdz01LCBub19hYm92ZT0wLjgpXG4gICAgY29ycHVzID0gW2RpY3Rpb25hcnkuZG9jMmJvdyhkb2MpIGZvciBkb2MgaW4gdGV4dHNdXG5cbiAgICAjIFRyeSBzZXZlcmFsIEsgdmFsdWVzIGFuZCBwaWNrIGJlc3QgY29oZXJlbmNlXG4gICAgcmVzdWx0cyA9IFtdXG4gICAgZm9yIEsgaW4gWzQsIDYsIDgsIDEwLCAxMl06XG4gICAgICAgIG1vZGVsID0gTGRhTW9kZWwoY29ycHVzPWNvcnB1cywgaWQyd29yZD1kaWN0aW9uYXJ5LFxuICAgICAgICAgICAgICAgICAgICAgICAgICBudW1fdG9waWNzPUssIHJhbmRvbV9zdGF0ZT00MiwgcGFzc2VzPTUpXG4gICAgICAgIGNtID0gQ29oZXJlbmNlTW9kZWwobW9kZWw9bW9kZWwsIHRleHRzPXRleHRzLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkaWN0aW9uYXJ5PWRpY3Rpb25hcnksIGNvaGVyZW5jZT1cdTAwMjdjX3ZcdTAwMjcpXG4gICAgICAgIHNjb3JlID0gY20uZ2V0X2NvaGVyZW5jZSgpXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKChLLCBzY29yZSkpXG4gICAgICAgIHByaW50KGZcdTAwMjdLPXtLfTogQ3YgY29oZXJlbmNlPXtzY29yZTouNGZ9XHUwMDI3KVxuXG4gICAgYmVzdF9LID0gbWF4KHJlc3VsdHMsIGtleT1sYW1iZGEgeDogeFsxXSlbMF1cbiAgICBwcmludChmXHUwMDI3XFxuQmVzdCBLIGJ5IGNvaGVyZW5jZToge2Jlc3RfS31cdTAwMjcpXG5leGNlcHQgSW1wb3J0RXJyb3I6XG4gICAgcHJpbnQoXHUwMDI3cGlwIGluc3RhbGwgZ2Vuc2ltIGZvciBjb2hlcmVuY2UgZXZhbHVhdGlvblx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmVwcm9jZXNzaW5nIFBpcGVsaW5lIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcXVhbGl0eSBvZiB0b3BpYyBtb2RlbHMgaXMgaGlnaGx5IHNlbnNpdGl2ZSB0byBwcmVwcm9jZXNzaW5nLiBQb29yIHByZXByb2Nlc3NpbmcgaXMgdGhlIG1vc3QgY29tbW9uIHJlYXNvbiBmb3IgaW5jb2hlcmVudCB0b3BpY3MuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUb2tlbmlzZTogc3BsaXQgb24gd2hpdGVzcGFjZSBhbmQgcHVuY3R1YXRpb247IGxvd2VyY2FzZSBhbGwgdG9rZW5zIiwiUmVtb3ZlIHN0b3Agd29yZHM6IHVzZSBkb21haW4tc3BlY2lmaWMgbGlzdCwgbm90IGp1c3QgTkxUSyBkZWZhdWx0czsgXHUwMDI3dXNlXHUwMDI3LCBcdTAwMjdhbHNvXHUwMDI3LCBcdTAwMjd3b3VsZFx1MDAyNyBhcmUgY29tbW9uIGN1bHByaXRzIiwiTGVtbWF0aXNlIChub3QganVzdCBzdGVtKTogXHUwMDI3cnVubmluZ1x1MDAyNyDihpIgXHUwMDI3cnVuXHUwMDI3LCBub3QgXHUwMDI3cnVublx1MDAyNyIsIkZpbHRlciBieSBkb2N1bWVudCBmcmVxdWVuY3k6IG1pbl9kZj01IChyZW1vdmUgcmFyZSB0ZXJtcyksIG1heF9kZj0wLjkgKHJlbW92ZSBuZWFyLXVuaXZlcnNhbCB0ZXJtcykiLCJPcHRpb25hbGx5OiBhZGQgYmlncmFtcyAoYmlncmFtX3BocmFzZXIgZnJvbSBnZW5zaW0pIHRvIGNhcHR1cmUgXHUwMDI3bWFjaGluZV9sZWFybmluZ1x1MDAyNywgXHUwMDI3bmV3X3lvcmtcdTAwMjciLCJCdWlsZCBkaWN0aW9uYXJ5OiBtYXAgdG9rZW5zIHRvIGludGVnZXIgSURzIGFuZCBjcmVhdGUgYmFnLW9mLXdvcmRzIGNvcnB1cyJdfSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJMREEiLCJOTUYiLCJCVE0iXSwicm93cyI6W1siUHJvYmFiaWxpc3RpYyIsIlllcyAoZ2VuZXJhdGl2ZSkiLCJObyIsIlllcyJdLFsiU2hvcnQgdGV4dCIsIlBvb3IiLCJNb2RlcmF0ZSIsIkV4Y2VsbGVudCJdLFsiSW5mZXJlbmNlIiwiR2liYnMgb3IgdmFyaWF0aW9uYWwgRU0iLCJBbHRlcm5hdGluZyBOTkxTIiwiR2liYnMgb24gYml0ZXJtcyJdLFsiSW50ZXJwcmV0YWJpbGl0eSIsIkhpZ2giLCJIaWdoIiwiSGlnaCJdLFsiQ29oZXJlbmNlIHF1YWxpdHkiLCJHb29kIiwiR29vZCIsIkdvb2QgKHNob3J0IHRleHQpIl0sWyJJbnB1dCByZXByZXNlbnRhdGlvbiIsIkNvdW50IG1hdHJpeCIsIlRGLUlERiBtYXRyaXgiLCJCaXRlcm0gY29ycHVzIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiT3B0aW1hbCBOdW1iZXIgb2YgVG9waWNzIiwiY29udGVudCI6IlBsb3QgY29oZXJlbmNlIHNjb3JlIChDdikgdnMgSy4gQ2hvb3NlIHRoZSBLIGF0IHRoZSBlbGJvdyBvciB0aGUgZmlyc3QgbG9jYWwgbWF4aW11bS4gQXZvaWQgb3Zlci10cnVzdGluZyBwZXJwbGV4aXR5IOKAlCBsb3dlciBwZXJwbGV4aXR5IGRvZXMgbm90IG1lYW4gbW9yZSBpbnRlcnByZXRhYmxlIHRvcGljcy4gRm9yIHByYWN0aWNhbCB1c2UsIDEw4oCTNTAgdG9waWNzIGNvdmVyIG1vc3QgY29ycG9yYSB3aXRoIDEwa+KAkzEwMGsgZG9jdW1lbnRzLiBEb21haW4gZXhwZXJ0cyBzaG91bGQgdmFsaWRhdGUgdGhlIHRvcCAxMCB3b3JkcyBvZiBlYWNoIHRvcGljLiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxEQSBhbmQgTk1GIHJlbWFpbiB0aGUgbW9zdCBwcmFjdGljYWwgdG9waWMgbW9kZWxpbmcgYXBwcm9hY2hlcyBmb3IgbWlkLXNpemVkIGNvcnBvcmEuIEZvciBzaG9ydCB0ZXh0cywgQlRNIG9yIExEQSB3aXRoIGFnZ3JlZ2F0ZWQgcHNldWRvLWRvY3VtZW50cyBhcmUgYmV0dGVyIGNob2ljZXMuIEFsd2F5cyBldmFsdWF0ZSB3aXRoIGNvaGVyZW5jZSBtZXRyaWNzIGFuZCBodW1hbiBpbnNwZWN0aW9uIOKAlCBwZXJwbGV4aXR5IGFsb25lIGlzIGEgcG9vciBndWlkZS4gTmV1cmFsIHRvcGljIG1vZGVscyAoUHJvZExEQSwgQ1RNKSBvZmZlciBiZXR0ZXIgcmVwcmVzZW50YXRpb25zIHdoZW4gcHJlLXRyYWluZWQgZW1iZWRkaW5ncyBhcmUgYXZhaWxhYmxlLiJ9XQ=="
---
# Topic Modeling — LDA, NMF, and BTM

Topic modeling discovers the latent thematic structure in a corpus of documents without supervision. Given a bag-of-words matrix, it recovers topics (distributions over words) and document-topic mixtures. The two dominant approaches — LDA (probabilistic) and NMF (matrix factorization) — differ in their assumptions but often produce comparable results on clean corpora.

## LDA Generative Model

LDA (Blei et al. 2003) assumes the following generative process: for each document d, draw a topic proportion vector θ_d ~ Dir(α). For each word position, draw a topic zₙ ~ Categorical(θ_d), then draw the word wₙ ~ Categorical(β_z) where β_k is the word distribution for topic k (β_k ~ Dir(η)). The Dirichlet prior α controls document sparsity (small α → documents focus on few topics); η controls topic sparsity (small η → topics focus on few words).

```python
import numpy as np

def lda_gibbs(corpus, vocab_size, K, alpha=0.1, eta=0.01, n_iter=100):
    """Collapsed Gibbs sampling for LDA (pedagogical implementation)."""
    D = len(corpus)
    doc_topic = np.zeros((D, K), dtype=int)
    topic_word = np.zeros((K, vocab_size), dtype=int)
    topic_total = np.zeros(K, dtype=int)

    # Random initialisation
    assignments = []
    for d, doc in enumerate(corpus):
        z_doc = []
        for w in doc:
            z = np.random.randint(K)
            z_doc.append(z)
            doc_topic[d, z] += 1
            topic_word[z, w] += 1
            topic_total[z] += 1
        assignments.append(z_doc)

    # Gibbs iterations
    for _ in range(n_iter):
        for d, doc in enumerate(corpus):
            for i, w in enumerate(doc):
                z = assignments[d][i]
                doc_topic[d, z] -= 1
                topic_word[z, w] -= 1
                topic_total[z] -= 1
                # Conditional distribution p(z | rest)
                likelihood = (topic_word[:, w] + eta) / (topic_total + vocab_size * eta)
                prior = doc_topic[d] + alpha
                p = likelihood * prior
                p /= p.sum()
                z_new = np.random.choice(K, p=p)
                assignments[d][i] = z_new
                doc_topic[d, z_new] += 1
                topic_word[z_new, w] += 1
                topic_total[z_new] += 1

    theta = (doc_topic + alpha) / (doc_topic + alpha).sum(axis=1, keepdims=True)
    phi = (topic_word + eta) / (topic_word + eta).sum(axis=1, keepdims=True)
    return theta, phi

print('LDA Gibbs sampler ready. Pass tokenised integer corpus.')
```

## LDA Inference with sklearn and pyLDAvis

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

cats = ['sci.space', 'rec.autos', 'talk.politics.guns', 'comp.graphics']
news = fetch_20newsgroups(subset='train', categories=cats,
                          remove=('headers', 'footers', 'quotes'))

vec = CountVectorizer(max_features=5000, stop_words='english',
                      min_df=5, max_df=0.9)
X_bow = vec.fit_transform(news.data)
feature_names = np.array(vec.get_feature_names_out())

K = 8
lda = LatentDirichletAllocation(n_components=K, max_iter=20,
                                 learning_method='online',
                                 random_state=42, n_jobs=-1)
doc_topics = lda.fit_transform(X_bow)

for k in range(K):
    top_idx = np.argsort(lda.components_[k])[-10:][::-1]
    top_str = ' | '.join(feature_names[top_idx])
    print(f'Topic {k:2d}: {top_str}')

print(f'\nPerplexity: {lda.perplexity(X_bow):.1f}')
print(f'Doc-topic matrix shape: {doc_topics.shape}')

try:
    import pyLDAvis.sklearn
    panel = pyLDAvis.sklearn.prepare(lda, X_bow, vec, mds='tsne')
    pyLDAvis.save_html(panel, 'lda_vis.html')
    print('Interactive visualisation saved to lda_vis.html')
except ImportError:
    print('pip install pyLDAvis for interactive topic explorer')
```

> **Hyperparameters: alpha and eta**: alpha (document Dirichlet prior): smaller alpha (0.01–0.1) → documents are sparse over topics, more focused. Larger alpha (1.0) → documents blend many topics. eta (topic Dirichlet prior): smaller eta → topics are sparse over vocabulary (sharper, more coherent topics). A good default is alpha = 50/K and eta = 0.01.

## NMF for Topic Modeling

Non-negative Matrix Factorization decomposes the TF-IDF matrix V ≈ WH where W ∈ ℝ₊ⁿˣᴷ (document-topic) and H ∈ ℝ₊ᴷˣᵛ (topic-word). The non-negativity constraint produces additive, parts-based topics. NMF is optimised via alternating non-negative least squares updates. Unlike LDA, NMF has no probabilistic interpretation and no built-in regularisation — it tends to produce topics that are more strongly driven by frequent terms.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

cats = ['sci.space', 'rec.autos', 'talk.politics.guns']
news = fetch_20newsgroups(subset='train', categories=cats,
                          remove=('headers', 'footers', 'quotes'))

tfidf_vec = TfidfVectorizer(max_features=3000, stop_words='english', min_df=5)
X_tfidf = tfidf_vec.fit_transform(news.data)
names_tfidf = np.array(tfidf_vec.get_feature_names_out())

count_vec = CountVectorizer(max_features=3000, stop_words='english', min_df=5)
X_bow = count_vec.fit_transform(news.data)
names_bow = np.array(count_vec.get_feature_names_out())

K = 5
nmf = NMF(n_components=K, random_state=42, max_iter=500, alpha_W=0.01)
W_nmf = nmf.fit_transform(X_tfidf)

lda = LatentDirichletAllocation(n_components=K, random_state=42, n_jobs=-1)
W_lda = lda.fit_transform(X_bow)

print('=== NMF Topics (TF-IDF) ===')
for k in range(K):
    top = ' | '.join(names_tfidf[np.argsort(nmf.components_[k])[-8:][::-1]])
    print(f'  {k}: {top}')

print('\n=== LDA Topics (Counts) ===')
for k in range(K):
    top = ' | '.join(names_bow[np.argsort(lda.components_[k])[-8:][::-1]])
    print(f'  {k}: {top}')
```

## BTM for Short Texts

Standard LDA struggles with short texts (tweets, product reviews): a 10-word document has too few word co-occurrences to infer reliable topic proportions. Biterm Topic Model (BTM) operates at the corpus level: it models the distribution over biterms (unordered word pairs) directly. By aggregating co-occurrences across the whole corpus, BTM overcomes the data sparsity problem inherent to short documents.

## Topic Coherence Evaluation

Perplexity measures held-out likelihood but correlates poorly with human judgement of topic quality. Coherence metrics measure the semantic relatedness of top words in each topic. The Cv score uses sliding-window PMI (Pointwise Mutual Information) computed over reference corpus co-occurrences. NPMI = PMI(w₁,w₂)/(-log p(w₁,w₂)) normalises PMI to [-1,1]. Cv ≈ 0.4 is mediocre; Cv > 0.55 is good.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

cats = ['sci.space', 'rec.autos', 'comp.graphics', 'talk.politics.guns']
news = fetch_20newsgroups(subset='train', categories=cats,
                          remove=('headers', 'footers', 'quotes'))

try:
    import gensim
    import gensim.corpora as corpora
    from gensim.models import CoherenceModel, LdaModel

    # Tokenise and filter
    texts = [[w.lower() for w in doc.split() if len(w) > 3]
              for doc in news.data]
    dictionary = corpora.Dictionary(texts)
    dictionary.filter_extremes(no_below=5, no_above=0.8)
    corpus = [dictionary.doc2bow(doc) for doc in texts]

    # Try several K values and pick best coherence
    results = []
    for K in [4, 6, 8, 10, 12]:
        model = LdaModel(corpus=corpus, id2word=dictionary,
                          num_topics=K, random_state=42, passes=5)
        cm = CoherenceModel(model=model, texts=texts,
                             dictionary=dictionary, coherence='c_v')
        score = cm.get_coherence()
        results.append((K, score))
        print(f'K={K}: Cv coherence={score:.4f}')

    best_K = max(results, key=lambda x: x[1])[0]
    print(f'\nBest K by coherence: {best_K}')
except ImportError:
    print('pip install gensim for coherence evaluation')
```

## Preprocessing Pipeline

The quality of topic models is highly sensitive to preprocessing. Poor preprocessing is the most common reason for incoherent topics.

- Tokenise: split on whitespace and punctuation; lowercase all tokens
- Remove stop words: use domain-specific list, not just NLTK defaults; 'use', 'also', 'would' are common culprits
- Lemmatise (not just stem): 'running' → 'run', not 'runn'
- Filter by document frequency: min_df=5 (remove rare terms), max_df=0.9 (remove near-universal terms)
- Optionally: add bigrams (bigram_phraser from gensim) to capture 'machine_learning', 'new_york'
- Build dictionary: map tokens to integer IDs and create bag-of-words corpus

| Property | LDA | NMF | BTM |
| --- | --- | --- | --- |
| Probabilistic | Yes (generative) | No | Yes |
| Short text | Poor | Moderate | Excellent |
| Inference | Gibbs or variational EM | Alternating NNLS | Gibbs on biterms |
| Interpretability | High | High | High |
| Coherence quality | Good | Good | Good (short text) |
| Input representation | Count matrix | TF-IDF matrix | Biterm corpus |

> **Optimal Number of Topics**: Plot coherence score (Cv) vs K. Choose the K at the elbow or the first local maximum. Avoid over-trusting perplexity — lower perplexity does not mean more interpretable topics. For practical use, 10–50 topics cover most corpora with 10k–100k documents. Domain experts should validate the top 10 words of each topic.

---

LDA and NMF remain the most practical topic modeling approaches for mid-sized corpora. For short texts, BTM or LDA with aggregated pseudo-documents are better choices. Always evaluate with coherence metrics and human inspection — perplexity alone is a poor guide. Neural topic models (ProdLDA, CTM) offer better representations when pre-trained embeddings are available.

