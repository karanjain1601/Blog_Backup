---
title: "Restricted Boltzmann Machines — Visible/Hidden Units and CD Training"
slug: "energy-based-models-rbm"
description: "RBMs are bipartite undirected graphical models with tractable conditional distributions that enable efficient Gibbs sampling and contrastive divergence training, forming the building block for Deep Belief Networks and the historical foundation of modern deep learning."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVzdHJpY3RlZCBCb2x0em1hbm4gTWFjaGluZXMgKFJCTXMpIGFyZSBzaGFsbG93IGdlbmVyYXRpdmUgbW9kZWxzIHRoYXQgcmVwcmVzZW50IGEgam9pbnQgZGlzdHJpYnV0aW9uIG92ZXIgdmlzaWJsZSB2YXJpYWJsZXMgdiAob2JzZXJ2ZWQgZGF0YSkgYW5kIGhpZGRlbiB2YXJpYWJsZXMgaCAobGF0ZW50IGZlYXR1cmVzKSB2aWEgYW4gZW5lcmd5IGZ1bmN0aW9uLiBUaGUgXHUwMDI3cmVzdHJpY3RlZFx1MDAyNyByZWZlcnMgdG8gdGhlIGJpcGFydGl0ZSBzdHJ1Y3R1cmU6IGNvbm5lY3Rpb25zIGV4aXN0IG9ubHkgYmV0d2VlbiB2aXNpYmxlIGFuZCBoaWRkZW4gbGF5ZXJzLCB3aXRoIG5vIGludHJhLWxheWVyIGNvbm5lY3Rpb25zLiBUaGlzIHJlc3RyaWN0aW9uIG1ha2VzIHRoZSBjb25kaXRpb25hbCBkaXN0cmlidXRpb25zIHAoaHx2KSBhbmQgcCh2fGgpIGZ1bGx5IGZhY3RvcmlzZWQgYW5kIGVhc3kgdG8gY29tcHV0ZSDigJQgdGhlIGtleSBwcm9wZXJ0eSB0aGF0IG1ha2VzIEdpYmJzIHNhbXBsaW5nIGVmZmljaWVudCBhbmQgZW5hYmxlcyBDRC1rIHRyYWluaW5nLiBSQk1zIHdlcmUgdGhlIGNyaXRpY2FsIGJ1aWxkaW5nIGJsb2NrIGZvciBEZWVwIEJlbGllZiBOZXR3b3JrcyAoMjAwNikgYW5kIHJlaWduaXRlZCBpbnRlcmVzdCBpbiBkZWVwIGxlYXJuaW5nIGJlZm9yZSBtb2Rlcm4gYmFja3Byb3BhZ2F0aW9uIHRvb2sgb3Zlci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSQk0gU3RydWN0dXJlIGFuZCBFbmVyZ3kgRnVuY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBlbmVyZ3kgb2YgYSBjb25maWd1cmF0aW9uICh2LCBoKSBpczogRSh2LGgpID0gLXbhtYBXaCAtIGLhtYB2IC0gY+G1gGgsIHdoZXJlIFcgaXMgdGhlIHdlaWdodCBtYXRyaXggKHx2fMOXfGh8KSwgYiBpcyB0aGUgdmlzaWJsZSBiaWFzLCBhbmQgYyBpcyB0aGUgaGlkZGVuIGJpYXMuIFRoZSBqb2ludCBkaXN0cmlidXRpb24gaXMgcCh2LGgpIOKInSBleHAoLUUodixoKSkuIFRoZSBwYXJ0aXRpb24gZnVuY3Rpb24gWiA9IM6jX3t2LGh9IGV4cCgtRSh2LGgpKSBpcyBpbnRyYWN0YWJsZSBmb3IgY29udGludW91cyBvciBsYXJnZSBkaXNjcmV0ZSB2IOKAlCBidXQgdGhlIG1hcmdpbmFsIHAodikgPSDOo19oIHAodixoKSBhbmQgdGhlIGNvbmRpdGlvbmFsIHAoaHx2KSBhcmUgdHJhY3RhYmxlIGJlY2F1c2Ugb2YgdGhlIGJpcGFydGl0ZSBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhY3RhYmxlIENvbmRpdGlvbmFsIERpc3RyaWJ1dGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBhYnNlbmNlIG9mIGludHJhLWxheWVyIGNvbm5lY3Rpb25zIG1lYW5zIHRoYXQgZ2l2ZW4gdiwgYWxsIGhpZGRlbiB1bml0cyBoX2ogYXJlIGNvbmRpdGlvbmFsbHkgaW5kZXBlbmRlbnQ6IHAoaHx2KSA9IM6gX2ogcChoX2p8diksIHdoZXJlIHAoaF9qPTF8dikgPSDPgyhX4rG84bWAdiArIGNfaikgZm9yIGJpbmFyeSB1bml0cy4gU2ltaWxhcmx5IHAodl9pPTF8aCkgPSDPgyhXX2nCt2ggKyBiX2kpLiBUaGVzZSBmYWN0b3Jpc2F0aW9ucyBlbmFibGUgYmxvY2sgR2liYnMgc2FtcGxpbmc6IHNhbXBsZSBhbGwgaCBpbiBwYXJhbGxlbCBmcm9tIHAoaHx2KSwgdGhlbiBhbGwgdiBpbiBwYXJhbGxlbCBmcm9tIHAodnxoKSwgYWx0ZXJuYXRpbmcuIE9uZSBmdWxsIGN5Y2xlICh24oaSaOKGknYpIGlzIGEgc2luZ2xlIEdpYmJzIHN0ZXAgYW5kIGlzIHRoZSBiYXNpcyBvZiBDRC0xIHRyYWluaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBSQk0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJCaW5hcnkgUmVzdHJpY3RlZCBCb2x0em1hbm4gTWFjaGluZSB3aXRoIENELWsgdHJhaW5pbmcuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fdmlzaWJsZSwgbl9oaWRkZW4pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5XID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKG5fdmlzaWJsZSwgbl9oaWRkZW4pICogMC4wMSlcbiAgICAgICAgc2VsZi5iID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKG5fdmlzaWJsZSkpICAgIyB2aXNpYmxlIGJpYXNcbiAgICAgICAgc2VsZi5jID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKG5faGlkZGVuKSkgICAgIyBoaWRkZW4gYmlhc1xuXG4gICAgZGVmIHNhbXBsZV9oKHNlbGYsIHYpOlxuICAgICAgICBcIlwiXCJTYW1wbGUgaGlkZGVuIHVuaXRzIGdpdmVuIHZpc2libGU6IHAoaHx2KSA9IHNpZ21vaWQoV15UIHYgKyBjKS5cIlwiXCJcbiAgICAgICAgcF9oID0gdG9yY2guc2lnbW9pZCh2IEAgc2VsZi5XICsgc2VsZi5jKSAgIyAoQiwgbl9oaWRkZW4pXG4gICAgICAgIHJldHVybiB0b3JjaC5iZXJub3VsbGkocF9oKSwgcF9oXG5cbiAgICBkZWYgc2FtcGxlX3Yoc2VsZiwgaCk6XG4gICAgICAgIFwiXCJcIlNhbXBsZSB2aXNpYmxlIHVuaXRzIGdpdmVuIGhpZGRlbjogcCh2fGgpID0gc2lnbW9pZChXIGggKyBiKS5cIlwiXCJcbiAgICAgICAgcF92ID0gdG9yY2guc2lnbW9pZChoIEAgc2VsZi5XLnQoKSArIHNlbGYuYikgICMgKEIsIG5fdmlzaWJsZSlcbiAgICAgICAgcmV0dXJuIHRvcmNoLmJlcm5vdWxsaShwX3YpLCBwX3ZcblxuICAgIGRlZiBmcmVlX2VuZXJneShzZWxmLCB2KTpcbiAgICAgICAgXCJcIlwiRnJlZSBlbmVyZ3kgRih2KSA9IC1iXlQgdiAtIHN1bV9qIGxvZygxICsgZXhwKFdfal5UIHYgKyBjX2opKS5cIlwiXCJcbiAgICAgICAgYnZfdGVybSAgPSB2IEAgc2VsZi5iXG4gICAgICAgIHd4X3BsdXNfYyA9IHYgQCBzZWxmLlcgKyBzZWxmLmNcbiAgICAgICAgaGlkZGVuX3Rlcm0gPSB0b3JjaC5sb2coMSArIHd4X3BsdXNfYy5leHAoKSkuc3VtKGRpbT0xKVxuICAgICAgICByZXR1cm4gLWJ2X3Rlcm0gLSBoaWRkZW5fdGVybVxuXG5yYm0gPSBSQk0obl92aXNpYmxlPTc4NCwgbl9oaWRkZW49MjU2KVxudiA9IHRvcmNoLmJlcm5vdWxsaSh0b3JjaC5yYW5kKDE2LCA3ODQpKVxuaF9zYW1wbGUsIHBfaCA9IHJibS5zYW1wbGVfaCh2KVxudl9yZWNvbiwgcF92ID0gcmJtLnNhbXBsZV92KGhfc2FtcGxlKVxucHJpbnQoZlx1MDAyN1JCTTogdj17di5zaGFwZX0gLVx1MDAzZSBoPXtoX3NhbXBsZS5zaGFwZX0gLVx1MDAzZSB2X3JlY29uPXt2X3JlY29uLnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdGcmVlIGVuZXJneSBtZWFuOiB7cmJtLmZyZWVfZW5lcmd5KHYpLm1lYW4oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNELTEgVHJhaW5pbmcgb24gTU5JU1QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNELTEgKENvbnRyYXN0aXZlIERpdmVyZ2VuY2Ugd2l0aCBrPTEpIGlzIHRoZSBzdGFuZGFyZCB0cmFpbmluZyBhbGdvcml0aG0gZm9yIFJCTXMuIFRoZSBncmFkaWVudCBvZiB0aGUgbmVnYXRpdmUgbG9nLWxpa2VsaWhvb2QgaXMgYXBwcm94aW1hdGVkIGJ5IHRoZSBkaWZmZXJlbmNlIGJldHdlZW4gZGF0YSBzdGF0aXN0aWNzIGFuZCBvbmUtc3RlcCByZWNvbnN0cnVjdGlvbiBzdGF0aXN0aWNzLiBUaGUgdHJhaW5pbmcgbG9vcDogKDEpIGNsYW1wIHZpc2libGUgdW5pdHMgdG8gZGF0YSB4OyAoMikgc2FtcGxlIGhpZGRlbiB1bml0cyBoIH4gcChofHgpOyAoMykgc2FtcGxlIHJlY29uc3RydWN0ZWQgdmlzaWJsZSB1bml0cyB4XHUwMDI3IH4gcCh2fGgpOyAoNCkgZ3JhZGllbnQg4omIIC3iiIdfVyBFKHgsaCkgKyDiiIdfVyBFKHhcdTAwMjcsaFx1MDAyNykgd2hlcmUgaFx1MDAyNyB+IHAoaHx4XHUwMDI3KS4gVGhpcyBjYW4gYmUgY29tcHV0ZWQgd2l0aG91dCBrbm93aW5nIFouIFRoZSByZWNvbnN0cnVjdGlvbiBlcnJvciDigJZ4IC0gcCh2fGgp4oCWwrIgc2VydmVzIGFzIGFuIGluZm9ybWFsIHF1YWxpdHkgbWV0cmljLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgZGF0YXNldHMsIHRyYW5zZm9ybXNcblxuZGVmIHRyYWluX3JibV9jZDEocmJtLCBuX2Vwb2Nocz01LCBiYXRjaF9zaXplPTY0LCBscj0wLjAxKTpcbiAgICBcIlwiXCJUcmFpbiBSQk0gb24gYmluYXJ5IE1OSVNUIHdpdGggQ0QtMSB1c2luZyBmcmVlIGVuZXJneSBncmFkaWVudC5cIlwiXCJcbiAgICB0cmFuc2Zvcm0gPSB0cmFuc2Zvcm1zLkNvbXBvc2UoW3RyYW5zZm9ybXMuVG9UZW5zb3IoKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cmFuc2Zvcm1zLkxhbWJkYShsYW1iZGEgeDogdG9yY2guYmVybm91bGxpKHgudmlldygtMSkpKV0pXG4gICAgdHJ5OlxuICAgICAgICBkYXRhc2V0ID0gZGF0YXNldHMuTU5JU1QoXHUwMDI3Li9kYXRhXHUwMDI3LCB0cmFpbj1UcnVlLCBkb3dubG9hZD1UcnVlLCB0cmFuc2Zvcm09dHJhbnNmb3JtKVxuICAgICAgICBsb2FkZXIgID0gdG9yY2gudXRpbHMuZGF0YS5EYXRhTG9hZGVyKGRhdGFzZXQsIGJhdGNoX3NpemU9YmF0Y2hfc2l6ZSwgc2h1ZmZsZT1UcnVlKVxuICAgIGV4Y2VwdCBFeGNlcHRpb246XG4gICAgICAgIHByaW50KFx1MDAyN01OSVNUIG5vdCBhdmFpbGFibGUg4oCUIHVzaW5nIHN5bnRoZXRpYyBiaW5hcnkgZGF0YVx1MDAyNylcbiAgICAgICAgbG9hZGVyID0gWyh0b3JjaC5iZXJub3VsbGkodG9yY2gucmFuZChiYXRjaF9zaXplLCA3ODQpKSwgTm9uZSkgZm9yIF8gaW4gcmFuZ2UoNTApXVxuICAgIG9wdGltaXplciA9IG9wdGltLlNHRChyYm0ucGFyYW1ldGVycygpLCBscj1sciwgbW9tZW50dW09MC41KVxuICAgIGZvciBlcG9jaCBpbiByYW5nZShuX2Vwb2Nocyk6XG4gICAgICAgIHJlY29uX2VycnMgPSBbXVxuICAgICAgICBmb3IgYmF0Y2hfaWR4LCAodl9kYXRhLCBfKSBpbiBlbnVtZXJhdGUobG9hZGVyKTpcbiAgICAgICAgICAgIHZfZGF0YSA9IHZfZGF0YS52aWV3KC0xLCA3ODQpXG4gICAgICAgICAgICAjIFBvc2l0aXZlIHBoYXNlXG4gICAgICAgICAgICBoX2RhdGEsIF8gPSByYm0uc2FtcGxlX2godl9kYXRhKVxuICAgICAgICAgICAgIyBOZWdhdGl2ZSBwaGFzZSAoQ0QtMSlcbiAgICAgICAgICAgIHZfcmVjb24sIHBfdl9yZWNvbiA9IHJibS5zYW1wbGVfdihoX2RhdGEpXG4gICAgICAgICAgICBoX3JlY29uLCBfID0gcmJtLnNhbXBsZV9oKHZfcmVjb24pXG4gICAgICAgICAgICAjIEZyZWUgZW5lcmd5IGNvbnRyYXN0aXZlIGxvc3NcbiAgICAgICAgICAgIGxvc3MgPSAocmJtLmZyZWVfZW5lcmd5KHZfZGF0YSkgLSByYm0uZnJlZV9lbmVyZ3kodl9yZWNvbikpLm1lYW4oKVxuICAgICAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdGltaXplci5zdGVwKClcbiAgICAgICAgICAgIHJlY29uX2VycnMuYXBwZW5kKCh2X2RhdGEgLSBwX3ZfcmVjb24pLnBvdygyKS5tZWFuKCkuaXRlbSgpKVxuICAgICAgICAgICAgaWYgYmF0Y2hfaWR4IFx1MDAzZT0gNDk6IGJyZWFrXG4gICAgICAgIHByaW50KGZcdTAwMjdFcG9jaCB7ZXBvY2grMX06IHJlY29uIGVycm9yID0ge3N1bShyZWNvbl9lcnJzKS9sZW4ocmVjb25fZXJycyk6LjRmfVx1MDAyNylcblxucmJtID0gUkJNKG5fdmlzaWJsZT03ODQsIG5faGlkZGVuPTI1NilcbnRyYWluX3JibV9jZDEocmJtLCBuX2Vwb2Nocz0zKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZhbnRhc3kgUGFydGljbGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGYW50YXN5IHBhcnRpY2xlcyBhcmUgc2FtcGxlcyBvYnRhaW5lZCBieSBydW5uaW5nIHRoZSBHaWJicyBjaGFpbiBmcm9tIHJhbmRvbSBub2lzZSByYXRoZXIgdGhhbiBmcm9tIGRhdGEuIFRoZXkgc2hvdyB3aGF0IHRoZSBtb2RlbCBoYXMgbGVhcm5lZCB0byBcdTAwMjdpbWFnaW5lXHUwMDI3IGFzIHZhbGlkIGRhdGEuIEVhcmx5IGluIHRyYWluaW5nLCBmYW50YXN5IHBhcnRpY2xlcyBsb29rIGxpa2Ugbm9pc2UuIEFmdGVyIGNvbnZlcmdlbmNlIG9uIE1OSVNULCB0aGV5IHNob3VsZCBsb29rIGxpa2UgZGlnaXQgaW1hZ2VzIOKAlCBibHVycnkgYnV0IHJlY29nbmlzYWJsZS4gSW5zcGVjdGluZyBmYW50YXN5IHBhcnRpY2xlcyBpcyB0aGUgcHJpbWFyeSBxdWFsaXRhdGl2ZSBkaWFnbm9zdGljIGZvciBSQk0gdHJhaW5pbmcuIElmIHRoZXkgcmVzZW1ibGUgZGF0YSwgdGhlIG1vZGVsIGhhcyBjYXB0dXJlZCB0aGUgZGF0YSBkaXN0cmlidXRpb24uIElmIHRoZXkgYXJlIG5vaXN5IG9yIG1vZGUtY29sbGFwc2VkIChhbGwgZGlnaXRzIGxvb2sgc2ltaWxhciksIHRoZSBtb2RlbCBuZWVkcyBtb3JlIGhpZGRlbiB1bml0cyBvciBsb25nZXIgTUNNQyBjaGFpbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBnZW5lcmF0ZV9mYW50YXN5X3BhcnRpY2xlcyhyYm0sIG5fc2FtcGxlcz0xNiwgbl9naWJic19zdGVwcz0xMDAwKTpcbiAgICBcIlwiXCJSdW4gZXh0ZW5kZWQgR2liYnMgc2FtcGxpbmcgZnJvbSByYW5kb20gaW5pdCB0byBnZXQgbW9kZWwgc2FtcGxlcy5cIlwiXCJcbiAgICB2ID0gdG9yY2guYmVybm91bGxpKHRvcmNoLnJhbmQobl9zYW1wbGVzLCByYm0uYi5zaGFwZVswXSkpICAjIHJhbmRvbSBpbml0XG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZvciBzdGVwIGluIHJhbmdlKG5fZ2liYnNfc3RlcHMpOlxuICAgICAgICAgICAgaCwgXyA9IHJibS5zYW1wbGVfaCh2KVxuICAgICAgICAgICAgdiwgcF92ID0gcmJtLnNhbXBsZV92KGgpXG4gICAgICAgICAgICBpZiBzdGVwICUgMjAwID09IDA6XG4gICAgICAgICAgICAgICAgcmVjb25fdmFyID0gcF92LnZhcihkaW09MCkubWVhbigpLml0ZW0oKVxuICAgICAgICAgICAgICAgIHByaW50KGZcdTAwMjcgIEdpYmJzIHN0ZXAge3N0ZXA6NGR9OiBwaXhlbCB2YXJpYW5jZSA9IHtyZWNvbl92YXI6LjRmfVx1MDAyNylcbiAgICByZXR1cm4gdiwgcF92ICAjIGJpbmFyeSBzYW1wbGVzIGFuZCBwcm9iYWJpbGl0aWVzXG5cbmRlZiBjaGVja19mYW50YXN5X2RpZ2l0X2xpa2UocF92LCBuX3Zpc2libGU9Nzg0KTpcbiAgICBcIlwiXCJDaGVjayBpZiBmYW50YXNpZXMgaGF2ZSBkaWdpdC1saWtlIHNwYXJzaXR5IChvbmx5IH4xNS0yMCUgcGl4ZWxzIGFjdGl2ZSkuXCJcIlwiXG4gICAgbWVhbl9hY3RpdmF0aW9uID0gcF92Lm1lYW4oKS5pdGVtKClcbiAgICBwcmludChmXHUwMDI3TWVhbiBwaXhlbCBhY3RpdmF0aW9uOiB7bWVhbl9hY3RpdmF0aW9uOi40Zn0gKGRpZ2l0czogfjAuMTItMC4yMClcdTAwMjcpXG4gICAgcmV0dXJuIDAuMDUgXHUwMDNjIG1lYW5fYWN0aXZhdGlvbiBcdTAwM2MgMC41MFxuXG5yYm1fc21hbGwgPSBSQk0obl92aXNpYmxlPTc4NCwgbl9oaWRkZW49NjQpXG5wcmludChcdTAwMjdHZW5lcmF0aW5nIGZhbnRhc3kgcGFydGljbGVzICh1bnRyYWluZWQgUkJNIOKAlCBleHBlY3Qgbm9pc2UpOlx1MDAyNylcbnZfZmFudGFzeSwgcF9mYW50YXN5ID0gZ2VuZXJhdGVfZmFudGFzeV9wYXJ0aWNsZXMocmJtX3NtYWxsLCBuX3NhbXBsZXM9OCwgbl9naWJic19zdGVwcz02MDApXG5jaGVja19mYW50YXN5X2RpZ2l0X2xpa2UocF9mYW50YXN5KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlZXAgQmVsaWVmIE5ldHdvcmtzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIERlZXAgQmVsaWVmIE5ldHdvcmsgKERCTiwgSGludG9uIGV0IGFsLiAyMDA2KSBpcyBidWlsdCBieSBzdGFja2luZyBSQk1zIGdyZWVkaWx5OiB0cmFpbiB0aGUgZmlyc3QgUkJNIG9uIHJhdyBkYXRhLCB1c2UgaXRzIGhpZGRlbiBhY3RpdmF0aW9ucyBhcyBpbnB1dCB0byB0cmFpbiBhIHNlY29uZCBSQk0sIGFuZCBzbyBvbi4gRWFjaCBsYXllciBsZWFybnMgYSBoaWdoZXItbGV2ZWwgcmVwcmVzZW50YXRpb24uIEFmdGVyIGdyZWVkeSBwcmV0cmFpbmluZywgdGhlIERCTiBpcyB0eXBpY2FsbHkgZmluZS10dW5lZCBkaXNjcmltaW5hdGl2ZWx5IHZpYSBiYWNrcHJvcGFnYXRpb24gd2l0aCB0aGUgUkJNIHdlaWdodHMgYXMgaW5pdGlhbGlzYXRpb24uIFRoaXMgcHJldHJhaW5pbmctdGhlbi1maW5ldHVuaW5nIGFwcHJvYWNoIHdhcyB0aGUgZmlyc3QgcHJhY3RpY2FsIG1ldGhvZCBmb3IgdHJhaW5pbmcgZGVlcCBuZXR3b3JrcyBiZWZvcmUgWGF2aWVyL0hlIGluaXRpYWxpc2F0aW9uIGFuZCBSZUxVIGFjdGl2YXRpb25zIGJlY2FtZSBzdGFuZGFyZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGdyZWVkeV9yYm1fc3RhY2sobGF5ZXJfc2l6ZXMsIGRhdGEsIG5fZXBvY2hzPTMsIGxyPTAuMDEpOlxuICAgIFwiXCJcIlxuICAgIEdyZWVkeSBsYXllci13aXNlIFJCTSBwcmV0cmFpbmluZy5cbiAgICBsYXllcl9zaXplczogZS5nLiBbNzg0LCA1MTIsIDI1NiwgMTI4XVxuICAgIFJldHVybnMgbGlzdCBvZiB0cmFpbmVkIFJCTXMgYW5kIGZpbmFsIGhpZGRlbiByZXByZXNlbnRhdGlvbnMuXG4gICAgXCJcIlwiXG4gICAgcmJtcyA9IFtdXG4gICAgY3VycmVudF9kYXRhID0gZGF0YVxuICAgIGZvciBpIGluIHJhbmdlKGxlbihsYXllcl9zaXplcykgLSAxKTpcbiAgICAgICAgbl92aXMsIG5faGlkID0gbGF5ZXJfc2l6ZXNbaV0sIGxheWVyX3NpemVzW2kgKyAxXVxuICAgICAgICBwcmludChmXHUwMDI3VHJhaW5pbmcgUkJNIGxheWVyIHtpKzF9OiB7bl92aXN9IC1cdTAwM2Uge25faGlkfSBoaWRkZW5cdTAwMjcpXG4gICAgICAgIHJibSA9IFJCTShuX3Zpc2libGU9bl92aXMsIG5faGlkZGVuPW5faGlkKVxuICAgICAgICBvcHQgPSB0b3JjaC5vcHRpbS5TR0QocmJtLnBhcmFtZXRlcnMoKSwgbHI9bHIpXG4gICAgICAgIGZvciBlcG9jaCBpbiByYW5nZShuX2Vwb2Nocyk6XG4gICAgICAgICAgICBoX2RhdGEsIF8gPSByYm0uc2FtcGxlX2goY3VycmVudF9kYXRhKVxuICAgICAgICAgICAgdl9yZWNvbiwgXyA9IHJibS5zYW1wbGVfdihoX2RhdGEpXG4gICAgICAgICAgICBsb3NzID0gKHJibS5mcmVlX2VuZXJneShjdXJyZW50X2RhdGEpIC0gcmJtLmZyZWVfZW5lcmd5KHZfcmVjb24pKS5tZWFuKClcbiAgICAgICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgICAgICMgVXNlIGhpZGRlbiBwcm9iYWJpbGl0aWVzIGFzIGlucHV0IHRvIG5leHQgbGF5ZXJcbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICBfLCBjdXJyZW50X2RhdGEgPSByYm0uc2FtcGxlX2goY3VycmVudF9kYXRhKVxuICAgICAgICByYm1zLmFwcGVuZChyYm0pXG4gICAgICAgIHByaW50KGZcdTAwMjcgIExheWVyIHtpKzF9IGRvbmU6IGhpZGRlbiByZXByIHNoYXBlID0ge2N1cnJlbnRfZGF0YS5zaGFwZX1cdTAwMjcpXG4gICAgcmV0dXJuIHJibXMsIGN1cnJlbnRfZGF0YVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuZGF0YSA9IHRvcmNoLmJlcm5vdWxsaSh0b3JjaC5yYW5kKDIwMCwgNzg0KSlcbnJibV9zdGFjaywgZGVlcF9yZXByID0gZ3JlZWR5X3JibV9zdGFjayhbNzg0LCAyNTYsIDEyOCwgNjRdLCBkYXRhLCBuX2Vwb2Nocz0yKVxucHJpbnQoZlx1MDAyN0RCTiBwcmV0cmFpbmVkOiB7bGVuKHJibV9zdGFjayl9IGxheWVycywgZmluYWwgcmVwcjoge2RlZXBfcmVwci5zaGFwZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVlcCBCb2x0em1hbm4gTWFjaGluZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZXAgQm9sdHptYW5uIE1hY2hpbmVzIChEQk1zLCBTYWxha2h1dGRpbm92IFx1MDAyNiBIaW50b24gMjAwOSkgZGlmZmVyIGZyb20gREJOcyBpbiB0d28gaW1wb3J0YW50IHdheXM6IGFsbCBsYXllcnMgYXJlIHVuZGlyZWN0ZWQgKHVubGlrZSBEQk5cdTAwMjdzIGRpcmVjdGVkIHRvcCBsYXllciksIGFuZCBpbmZlcmVuY2UgaXMgaW50cmFjdGFibGUg4oCUIGFwcHJveGltYXRlIG1lYW4tZmllbGQgaW5mZXJlbmNlIGlzIHJlcXVpcmVkIGV2ZW4gZm9yIGNvbXB1dGluZyBoaWRkZW4gYWN0aXZhdGlvbnMgZ2l2ZW4gdmlzaWJsZSB1bml0cy4gREJNcyBzdXBwb3J0IGEgcmljaGVyIGpvaW50IGRpc3RyaWJ1dGlvbiBidXQgYXJlIGhhcmRlciB0byB0cmFpbiBhbmQgc2xvd2VyIHRvIHNhbXBsZSBmcm9tLiBHcmVlZHkgcHJldHJhaW5pbmcgd2l0aCBtb2RpZmllZCBSQk1zIChkb3VibGluZyB3ZWlnaHRzIGZvciBpbnRlcmlvciBsYXllcnMpIHByb3ZpZGVzIGEgZ29vZCBpbml0aWFsaXNhdGlvbiBiZWZvcmUgbWVhbi1maWVsZCBmaW5lLXR1bmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIaXN0b3JpY2FsIFJvbGUgYW5kIE1vZGVybiBQZXJzcGVjdGl2ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUkJNcyBhbmQgREJOcyB3ZXJlIGNlbnRyYWwgdG8gdGhlIGRlZXAgbGVhcm5pbmcgcmV2aXZhbCBvZiAyMDA2LTIwMTIuIEhpbnRvblx1MDAyN3MgMjAwNiBTY2llbmNlIHBhcGVyIHNob3dpbmcgdGhhdCBncmVlZHkgUkJNIHByZXRyYWluaW5nIGVuYWJsZWQgdHJhaW5pbmcgZGVlcCBuZXR3b3JrcyB3YXMgdGhlIGNhdGFseXN0IGZvciB0aGUgbW9kZXJuIGRlZXAgbGVhcm5pbmcgZXJhLiBCeSAyMDEyLCBSZUxVIGFjdGl2YXRpb25zLCBkcm9wb3V0LCBhbmQgSGUgaW5pdGlhbGlzYXRpb24gbWFkZSBwcmV0cmFpbmluZyB1bm5lY2Vzc2FyeSwgYW5kIFJCTXMgZmFkZWQgZnJvbSBwcmFjdGljYWwgdXNlLiBUb2RheSwgUkJNcyBhcmUgc3R1ZGllZCBhcyBjYW5vbmljYWwgZXhhbXBsZXMgb2YgZW5lcmd5LWJhc2VkIGxlYXJuaW5nLCBhbmQgdGhlaXIgQ0QgdHJhaW5pbmcgYWxnb3JpdGhtIGlzIGRpcmVjdGx5IHJlbGF0ZWQgdG8gdGhlIGNvbnRyYXN0aXZlIGxlYXJuaW5nIGxvc3NlcyB1c2VkIGluIFNpbUNMUiBhbmQgTW9Dby4gVGhlIGNvcmUgaW5zaWdodCDigJQgdGhhdCB0aGUgZGlmZmVyZW5jZSBiZXR3ZWVuIGRhdGEgYW5kIG1vZGVsIHN0YXRpc3RpY3Mgc2hhcGVzIGEgdXNlZnVsIGVuZXJneSBsYW5kc2NhcGUg4oCUIHJlbWFpbnMgZm91bmRhdGlvbmFsLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTW9kZXJuIFVzZSBDYXNlcyBmb3IgUkJNcyIsImNvbnRlbnQiOiJXaGlsZSBSQk1zIGFyZSBubyBsb25nZXIgY29tcGV0aXRpdmUgZm9yIGltYWdlIGdlbmVyYXRpb24gKGRpZmZ1c2lvbiBtb2RlbHMgZG9taW5hdGUpLCB0aGV5IHJlbWFpbiByZWxldmFudCBmb3I6ICgxKSBjb2xsYWJvcmF0aXZlIGZpbHRlcmluZyB3aXRoIGJpbmFyeSByYXRpbmdzIOKAlCB0aGUgTmV0ZmxpeCBQcml6ZSBzaG93ZWQgUkJNcyBlZmZlY3RpdmUgZm9yIHJlY29tbWVuZGF0aW9uOyAoMikgY2F0ZWdvcmljYWwgZGF0YSBtb2RlbGxpbmcgd2hlcmUgR2F1c3NpYW4gYXNzdW1wdGlvbnMgb2YgVkFFcyBhcmUgaW5hcHByb3ByaWF0ZTsgKDMpIHVuZGVyc3RhbmRpbmcgZW5lcmd5LWJhc2VkIGxlYXJuaW5nIGJlZm9yZSB0YWNrbGluZyBtb2Rlcm4gRUJNcyBvciBkaWZmdXNpb24gbW9kZWxzLiBSQk1zIGFyZSBhbHNvIHRoZSBzaW1wbGVzdCBleGFtcGxlIG9mIGEgbW9kZWwgd2hlcmUgTUNNQyBpcyB0aGUgb25seSBpbmZlcmVuY2Ugb3B0aW9uIOKAlCB1bmRlcnN0YW5kaW5nIHRoZWlyIGZhaWx1cmUgbW9kZXMgdGVhY2hlcyBpbnR1aXRpb24gZm9yIGFsbCBFQk0gdHJhaW5pbmcuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiVHJhaW5pbmcgTWV0aG9kIiwiRGVwdGgiLCJJbmZlcmVuY2UiLCJHZW5lcmF0aW9uIFF1YWxpdHkiLCJIaXN0b3JpY2FsIFJvbGUiXSwicm93cyI6W1siUkJNIiwiQ0QtayAoR2liYnMgc2FtcGxpbmcpIiwiMSBoaWRkZW4gbGF5ZXIiLCJFeGFjdCBjb25kaXRpb25hbHMsIEdpYmJzIHNhbXBsaW5nIiwiTW9kZXJhdGUgKGJsdXJyeSBkaWdpdHMpIiwiS2V5IHByZS1kZWVwLWxlYXJuaW5nIGNvbXBvbmVudCAoMjAwNikiXSxbIkRCTiIsIkdyZWVkeSBSQk0gcHJldHJhaW5pbmcgKyBCUCBmaW5lLXR1bmUiLCJNdWx0aXBsZSBkaXJlY3RlZCBsYXllcnMiLCJBbmNlc3RyYWwgc2FtcGxpbmcgKHRvcC1kb3duKSIsIkdvb2QgZm9yIE1OSVNUIGVyYSIsIkZpcnN0IHByYWN0aWNhbCBkZWVwIG5ldCAoMjAwNiBTY2llbmNlIHBhcGVyKSJdLFsiREJNIiwiTWVhbi1maWVsZCArIGdyZWVkeSBSQk0gcHJldHJhaW5pbmciLCJNdWx0aXBsZSB1bmRpcmVjdGVkIGxheWVycyIsIkFwcHJveGltYXRlIG1lYW4tZmllbGQiLCJNb2RlcmF0ZSDigJQgaGFyZCB0byB0cmFpbiIsIlJpY2hlciBqb2ludCBkaXN0cmlidXRpb24sIHJhcmVseSB1c2VkIl0sWyJNb2Rlcm4gRUJNIiwiUGVyc2lzdGVudCBDRCAvIFNHTEQiLCJEZWVwIE1MUCBlbmVyZ3kgbmV0IiwiTGFuZ2V2aW4gTUNNQyAoc2xvdykiLCJDb21wZXRpdGl2ZSBidXQgYmVsb3cgZGlmZnVzaW9uIiwiT09EIGRldGVjdGlvbiwgZGVuc2l0eSBlc3RpbWF0aW9uIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlJCTSBjb25kaXRpb25hbHMgcChofHYpIGFuZCBwKHZ8aCkgYXJlIGZ1bGx5IGZhY3RvcmlzZWQg4oCUIGFsbCB1bml0cyBhcmUgaW5kZXBlbmRlbnQgZ2l2ZW4gdGhlIG90aGVyIGxheWVyLiIsIkNELTEgaXMgc3VmZmljaWVudCBmb3IgUkJNczsgQ0QtayAoa1x1MDAzZTEpIGhlbHBzIGZvciBsYXJnZXIgbW9kZWxzIHdoZXJlIHRoZSBjaGFpbiBuZWVkcyBtb3JlIHN0ZXBzIHRvIG1peC4iLCJGYW50YXN5IHBhcnRpY2xlcyBzaG91bGQgdmlzdWFsbHkgcmVzZW1ibGUgZGF0YSBhZnRlciB0cmFpbmluZyDigJQgdXNlIHRoZW0gYXMgdGhlIHByaW1hcnkgcXVhbGl0YXRpdmUgZGlhZ25vc3RpYy4iLCJEQk4gZ3JlZWR5IHByZXRyYWluaW5nIGltcHJvdmVkIGRlZXAgbmV0d29yayBhY2N1cmFjeSBieSAxLTIlIG9uIE1OSVNUIGluIHRoZSBwcmUtUmVMVSBlcmEuIiwiVGhlIGNvbm5lY3Rpb246IFJCTSBzY29yZSBmdW5jdGlvbiA9IC3iiIdfdiBFKHYpID0gYiArIFfPgyhXXlQgdiArIGMpLCBkaXJlY3RseSBhbmFsb2dvdXMgdG8gZGVub2lzaW5nIHNjb3JlIG1hdGNoaW5nIHRhcmdldHMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Restricted Boltzmann Machines — Visible/Hidden Units and CD Training

Restricted Boltzmann Machines (RBMs) are shallow generative models that represent a joint distribution over visible variables v (observed data) and hidden variables h (latent features) via an energy function. The 'restricted' refers to the bipartite structure: connections exist only between visible and hidden layers, with no intra-layer connections. This restriction makes the conditional distributions p(h|v) and p(v|h) fully factorised and easy to compute — the key property that makes Gibbs sampling efficient and enables CD-k training. RBMs were the critical building block for Deep Belief Networks (2006) and reignited interest in deep learning before modern backpropagation took over.

## RBM Structure and Energy Function

The energy of a configuration (v, h) is: E(v,h) = -vᵀWh - bᵀv - cᵀh, where W is the weight matrix (|v|×|h|), b is the visible bias, and c is the hidden bias. The joint distribution is p(v,h) ∝ exp(-E(v,h)). The partition function Z = Σ_{v,h} exp(-E(v,h)) is intractable for continuous or large discrete v — but the marginal p(v) = Σ_h p(v,h) and the conditional p(h|v) are tractable because of the bipartite structure.

## Tractable Conditional Distributions

The absence of intra-layer connections means that given v, all hidden units h_j are conditionally independent: p(h|v) = Π_j p(h_j|v), where p(h_j=1|v) = σ(Wⱼᵀv + c_j) for binary units. Similarly p(v_i=1|h) = σ(W_i·h + b_i). These factorisations enable block Gibbs sampling: sample all h in parallel from p(h|v), then all v in parallel from p(v|h), alternating. One full cycle (v→h→v) is a single Gibbs step and is the basis of CD-1 training.

```python
import torch
import torch.nn as nn

class RBM(nn.Module):
    """Binary Restricted Boltzmann Machine with CD-k training."""
    def __init__(self, n_visible, n_hidden):
        super().__init__()
        self.W = nn.Parameter(torch.randn(n_visible, n_hidden) * 0.01)
        self.b = nn.Parameter(torch.zeros(n_visible))   # visible bias
        self.c = nn.Parameter(torch.zeros(n_hidden))    # hidden bias

    def sample_h(self, v):
        """Sample hidden units given visible: p(h|v) = sigmoid(W^T v + c)."""
        p_h = torch.sigmoid(v @ self.W + self.c)  # (B, n_hidden)
        return torch.bernoulli(p_h), p_h

    def sample_v(self, h):
        """Sample visible units given hidden: p(v|h) = sigmoid(W h + b)."""
        p_v = torch.sigmoid(h @ self.W.t() + self.b)  # (B, n_visible)
        return torch.bernoulli(p_v), p_v

    def free_energy(self, v):
        """Free energy F(v) = -b^T v - sum_j log(1 + exp(W_j^T v + c_j))."""
        bv_term  = v @ self.b
        wx_plus_c = v @ self.W + self.c
        hidden_term = torch.log(1 + wx_plus_c.exp()).sum(dim=1)
        return -bv_term - hidden_term

rbm = RBM(n_visible=784, n_hidden=256)
v = torch.bernoulli(torch.rand(16, 784))
h_sample, p_h = rbm.sample_h(v)
v_recon, p_v = rbm.sample_v(h_sample)
print(f'RBM: v={v.shape} -> h={h_sample.shape} -> v_recon={v_recon.shape}')
print(f'Free energy mean: {rbm.free_energy(v).mean():.4f}')
```

## CD-1 Training on MNIST

CD-1 (Contrastive Divergence with k=1) is the standard training algorithm for RBMs. The gradient of the negative log-likelihood is approximated by the difference between data statistics and one-step reconstruction statistics. The training loop: (1) clamp visible units to data x; (2) sample hidden units h ~ p(h|x); (3) sample reconstructed visible units x' ~ p(v|h); (4) gradient ≈ -∇_W E(x,h) + ∇_W E(x',h') where h' ~ p(h|x'). This can be computed without knowing Z. The reconstruction error ‖x - p(v|h)‖² serves as an informal quality metric.

```python
import torch
import torch.optim as optim
from torchvision import datasets, transforms

def train_rbm_cd1(rbm, n_epochs=5, batch_size=64, lr=0.01):
    """Train RBM on binary MNIST with CD-1 using free energy gradient."""
    transform = transforms.Compose([transforms.ToTensor(),
                                     transforms.Lambda(lambda x: torch.bernoulli(x.view(-1)))])
    try:
        dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
        loader  = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
    except Exception:
        print('MNIST not available — using synthetic binary data')
        loader = [(torch.bernoulli(torch.rand(batch_size, 784)), None) for _ in range(50)]
    optimizer = optim.SGD(rbm.parameters(), lr=lr, momentum=0.5)
    for epoch in range(n_epochs):
        recon_errs = []
        for batch_idx, (v_data, _) in enumerate(loader):
            v_data = v_data.view(-1, 784)
            # Positive phase
            h_data, _ = rbm.sample_h(v_data)
            # Negative phase (CD-1)
            v_recon, p_v_recon = rbm.sample_v(h_data)
            h_recon, _ = rbm.sample_h(v_recon)
            # Free energy contrastive loss
            loss = (rbm.free_energy(v_data) - rbm.free_energy(v_recon)).mean()
            optimizer.zero_grad(); loss.backward(); optimizer.step()
            recon_errs.append((v_data - p_v_recon).pow(2).mean().item())
            if batch_idx >= 49: break
        print(f'Epoch {epoch+1}: recon error = {sum(recon_errs)/len(recon_errs):.4f}')

rbm = RBM(n_visible=784, n_hidden=256)
train_rbm_cd1(rbm, n_epochs=3)
```

## Fantasy Particles

Fantasy particles are samples obtained by running the Gibbs chain from random noise rather than from data. They show what the model has learned to 'imagine' as valid data. Early in training, fantasy particles look like noise. After convergence on MNIST, they should look like digit images — blurry but recognisable. Inspecting fantasy particles is the primary qualitative diagnostic for RBM training. If they resemble data, the model has captured the data distribution. If they are noisy or mode-collapsed (all digits look similar), the model needs more hidden units or longer MCMC chains.

```python
import torch
import numpy as np

def generate_fantasy_particles(rbm, n_samples=16, n_gibbs_steps=1000):
    """Run extended Gibbs sampling from random init to get model samples."""
    v = torch.bernoulli(torch.rand(n_samples, rbm.b.shape[0]))  # random init
    with torch.no_grad():
        for step in range(n_gibbs_steps):
            h, _ = rbm.sample_h(v)
            v, p_v = rbm.sample_v(h)
            if step % 200 == 0:
                recon_var = p_v.var(dim=0).mean().item()
                print(f'  Gibbs step {step:4d}: pixel variance = {recon_var:.4f}')
    return v, p_v  # binary samples and probabilities

def check_fantasy_digit_like(p_v, n_visible=784):
    """Check if fantasies have digit-like sparsity (only ~15-20% pixels active)."""
    mean_activation = p_v.mean().item()
    print(f'Mean pixel activation: {mean_activation:.4f} (digits: ~0.12-0.20)')
    return 0.05 < mean_activation < 0.50

rbm_small = RBM(n_visible=784, n_hidden=64)
print('Generating fantasy particles (untrained RBM — expect noise):')
v_fantasy, p_fantasy = generate_fantasy_particles(rbm_small, n_samples=8, n_gibbs_steps=600)
check_fantasy_digit_like(p_fantasy)
```

## Deep Belief Networks

A Deep Belief Network (DBN, Hinton et al. 2006) is built by stacking RBMs greedily: train the first RBM on raw data, use its hidden activations as input to train a second RBM, and so on. Each layer learns a higher-level representation. After greedy pretraining, the DBN is typically fine-tuned discriminatively via backpropagation with the RBM weights as initialisation. This pretraining-then-finetuning approach was the first practical method for training deep networks before Xavier/He initialisation and ReLU activations became standard.

```python
import torch
import torch.nn as nn

def greedy_rbm_stack(layer_sizes, data, n_epochs=3, lr=0.01):
    """
    Greedy layer-wise RBM pretraining.
    layer_sizes: e.g. [784, 512, 256, 128]
    Returns list of trained RBMs and final hidden representations.
    """
    rbms = []
    current_data = data
    for i in range(len(layer_sizes) - 1):
        n_vis, n_hid = layer_sizes[i], layer_sizes[i + 1]
        print(f'Training RBM layer {i+1}: {n_vis} -> {n_hid} hidden')
        rbm = RBM(n_visible=n_vis, n_hidden=n_hid)
        opt = torch.optim.SGD(rbm.parameters(), lr=lr)
        for epoch in range(n_epochs):
            h_data, _ = rbm.sample_h(current_data)
            v_recon, _ = rbm.sample_v(h_data)
            loss = (rbm.free_energy(current_data) - rbm.free_energy(v_recon)).mean()
            opt.zero_grad(); loss.backward(); opt.step()
        # Use hidden probabilities as input to next layer
        with torch.no_grad():
            _, current_data = rbm.sample_h(current_data)
        rbms.append(rbm)
        print(f'  Layer {i+1} done: hidden repr shape = {current_data.shape}')
    return rbms, current_data

torch.manual_seed(0)
data = torch.bernoulli(torch.rand(200, 784))
rbm_stack, deep_repr = greedy_rbm_stack([784, 256, 128, 64], data, n_epochs=2)
print(f'DBN pretrained: {len(rbm_stack)} layers, final repr: {deep_repr.shape}')
```

## Deep Boltzmann Machines

Deep Boltzmann Machines (DBMs, Salakhutdinov & Hinton 2009) differ from DBNs in two important ways: all layers are undirected (unlike DBN's directed top layer), and inference is intractable — approximate mean-field inference is required even for computing hidden activations given visible units. DBMs support a richer joint distribution but are harder to train and slower to sample from. Greedy pretraining with modified RBMs (doubling weights for interior layers) provides a good initialisation before mean-field fine-tuning.

## Historical Role and Modern Perspective

RBMs and DBNs were central to the deep learning revival of 2006-2012. Hinton's 2006 Science paper showing that greedy RBM pretraining enabled training deep networks was the catalyst for the modern deep learning era. By 2012, ReLU activations, dropout, and He initialisation made pretraining unnecessary, and RBMs faded from practical use. Today, RBMs are studied as canonical examples of energy-based learning, and their CD training algorithm is directly related to the contrastive learning losses used in SimCLR and MoCo. The core insight — that the difference between data and model statistics shapes a useful energy landscape — remains foundational.

> **Modern Use Cases for RBMs**: While RBMs are no longer competitive for image generation (diffusion models dominate), they remain relevant for: (1) collaborative filtering with binary ratings — the Netflix Prize showed RBMs effective for recommendation; (2) categorical data modelling where Gaussian assumptions of VAEs are inappropriate; (3) understanding energy-based learning before tackling modern EBMs or diffusion models. RBMs are also the simplest example of a model where MCMC is the only inference option — understanding their failure modes teaches intuition for all EBM training.

| Model | Training Method | Depth | Inference | Generation Quality | Historical Role |
| --- | --- | --- | --- | --- | --- |
| RBM | CD-k (Gibbs sampling) | 1 hidden layer | Exact conditionals, Gibbs sampling | Moderate (blurry digits) | Key pre-deep-learning component (2006) |
| DBN | Greedy RBM pretraining + BP fine-tune | Multiple directed layers | Ancestral sampling (top-down) | Good for MNIST era | First practical deep net (2006 Science paper) |
| DBM | Mean-field + greedy RBM pretraining | Multiple undirected layers | Approximate mean-field | Moderate — hard to train | Richer joint distribution, rarely used |
| Modern EBM | Persistent CD / SGLD | Deep MLP energy net | Langevin MCMC (slow) | Competitive but below diffusion | OOD detection, density estimation |

- RBM conditionals p(h|v) and p(v|h) are fully factorised — all units are independent given the other layer.
- CD-1 is sufficient for RBMs; CD-k (k>1) helps for larger models where the chain needs more steps to mix.
- Fantasy particles should visually resemble data after training — use them as the primary qualitative diagnostic.
- DBN greedy pretraining improved deep network accuracy by 1-2% on MNIST in the pre-ReLU era.
- The connection: RBM score function = -∇_v E(v) = b + Wσ(W^T v + c), directly analogous to denoising score matching targets.

---

