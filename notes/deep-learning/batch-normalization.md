---
title: "Batch Normalization — Running Stats, Train vs Eval, and Gradients"
slug: "batch-normalization"
description: "Implement batch norm from scratch with train and eval modes, derive its gradient analytically, demonstrate the critical importance of model.eval(), examine batch size effects, and compare BN to layer norm, instance norm, and group norm."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmF0Y2ggTm9ybWFsaXNhdGlvbiAoQk4pIG5vcm1hbGlzZXMgdGhlIHByZS1hY3RpdmF0aW9ucyBvZiBlYWNoIGxheWVyIHRvIGhhdmUgemVybyBtZWFuIGFuZCB1bml0IHZhcmlhbmNlIHdpdGhpbiBhIG1pbmktYmF0Y2gsIHRoZW4gcmUtc2NhbGVzIHdpdGggbGVhcm5hYmxlIHBhcmFtZXRlcnMgzrMgYW5kIM6yLiBJdCBkcmFtYXRpY2FsbHkgYWNjZWxlcmF0ZXMgdHJhaW5pbmcgYnkgYWxsb3dpbmcgaGlnaGVyIGxlYXJuaW5nIHJhdGVzLCByZWR1Y2VzIHNlbnNpdGl2aXR5IHRvIGluaXRpYWxpc2F0aW9uLCBhbmQgcHJvdmlkZXMgbWlsZCByZWd1bGFyaXNhdGlvbiB0aHJvdWdoIHRoZSBub2lzZSBpbiBiYXRjaCBzdGF0aXN0aWNzLiBVbmRlcnN0YW5kaW5nIHRoZSBkaWZmZXJlbmNlIGJldHdlZW4gdHJhaW4gbW9kZSAoYmF0Y2ggc3RhdHMpIGFuZCBldmFsIG1vZGUgKHJ1bm5pbmcgc3RhdHMpIGlzIGNyaXRpY2FsIOKAlCBjb25mdXNpbmcgdGhlbSBpcyBvbmUgb2YgdGhlIG1vc3QgY29tbW9uIGJ1Z3MgaW4gZGVlcCBsZWFybmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCYXRjaCBOb3JtIEZvcndhcmQgUGFzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgbWluaS1iYXRjaCBvZiBtIGFjdGl2YXRpb25zIHgg4oiIIOKEnV57bSDDlyBkfTogzrxfQiA9ICgxL20pzqN44bWiIOKIiCDihJ1eZCwgz4PCsl9CID0gKDEvbSnOoyh44bWiLc68X0IpwrIg4oiIIOKEnV5kLCB4zILhtaIgPSAoeOG1oi3OvF9CKS/iiJooz4PCsl9CK861KSwgeeG1oiA9IM6z4oqZeMyC4bWiICsgzrIuIM61IGlzIGEgc21hbGwgY29uc3RhbnQgKHR5cGljYWxseSAxZS01KSBmb3IgbnVtZXJpY2FsIHN0YWJpbGl0eS4gzrMg4oiIIOKEnV5kIGFuZCDOsiDiiIgg4oSdXmQgYXJlIGxlYXJuYWJsZTogzrMgc3RhcnRzIGF0IDEsIM6yIGF0IDAuIFRoaXMgYWxsb3dzIHRoZSBuZXR3b3JrIHRvIHVuZG8gbm9ybWFsaXNhdGlvbiBpZiBpdCBoZWxwcyDigJQgQk4gaXMgc3RyaWN0bHkgbW9yZSBleHByZXNzaXZlIHRoYW4gbm90IGhhdmluZyBpdCwgc2luY2UgzrM9c3RkLCDOsj1tZWFuIHJlY292ZXJzIHRoZSBvcmlnaW5hbCBkaXN0cmlidXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUnVubmluZyBTdGF0aXN0aWNzIGFuZCBUcmFpbiB2cyBFdmFsIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdCB0cmFpbmluZyB0aW1lLCBCTiB1c2VzIHBlci1iYXRjaCBzdGF0aXN0aWNzIM68X0IgYW5kIM+DwrJfQi4gQXQgaW5mZXJlbmNlIHRpbWUsIHVzaW5nIGJhdGNoIHN0YXRzIGlzIHByb2JsZW1hdGljOiAoMSkgdGhlIGJhdGNoIG1heSBoYXZlIGEgc2luZ2xlIHNhbXBsZSAobT0xLCDPg8KyPTApOyAoMikgYmF0Y2ggc3RhdGlzdGljcyBpbnRyb2R1Y2UgcmFuZG9tbmVzcyBpbnRvIGRldGVybWluaXN0aWMgaW5mZXJlbmNlLiBTb2x1dGlvbjogbWFpbnRhaW4gZXhwb25lbnRpYWwgbW92aW5nIGF2ZXJhZ2VzIGR1cmluZyB0cmFpbmluZzogzrxfcnVubmluZyDihpAgKDEtbW9tZW50dW0pwrfOvF9ydW5uaW5nICsgbW9tZW50dW3Ct868X0IsIGFuZCBzaW1pbGFybHkgZm9yIM+DwrJfcnVubmluZy4gQXQgZXZhbCB0aW1lLCB1c2UgzrxfcnVubmluZyBhbmQgz4PCsl9ydW5uaW5nIGluc3RlYWQgb2YgYmF0Y2ggc3RhdHMuIFB5VG9yY2hcdTAwMjdzIG1vZGVsLnRyYWluKCkgYW5kIG1vZGVsLmV2YWwoKSBzd2l0Y2ggdGhpcyBiZWhhdmlvdXIg4oCUIGZvcmdldHRpbmcgbW9kZWwuZXZhbCgpIGJlZm9yZSBpbmZlcmVuY2UgaXMgYSBjb21tb24gYW5kIHNpbGVudCBidWcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5jbGFzcyBCYXRjaE5vcm0xZDpcbiAgICBcIlwiXCJCYXRjaCBOb3JtYWxpemF0aW9uIGZvciAyRCBpbnB1dCAobSwgZCkgd2l0aCB0cmFpbi9ldmFsIG1vZGVzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkLCBlcHM9MWUtNSwgbW9tZW50dW09MC4xKTpcbiAgICAgICAgc2VsZi5nYW1tYSA9IG5wLm9uZXMoZClcbiAgICAgICAgc2VsZi5iZXRhICA9IG5wLnplcm9zKGQpXG4gICAgICAgIHNlbGYuZXBzICAgPSBlcHNcbiAgICAgICAgc2VsZi5tb21lbnR1bSA9IG1vbWVudHVtXG4gICAgICAgIHNlbGYucnVubmluZ19tZWFuID0gbnAuemVyb3MoZClcbiAgICAgICAgc2VsZi5ydW5uaW5nX3ZhciAgPSBucC5vbmVzKGQpXG4gICAgICAgIHNlbGYudHJhaW5pbmcgPSBUcnVlXG4gICAgICAgIHNlbGYuX2NhY2hlID0gTm9uZVxuXG4gICAgZGVmIF9fY2FsbF9fKHNlbGYsIHgpOlxuICAgICAgICBpZiBzZWxmLnRyYWluaW5nOlxuICAgICAgICAgICAgbXUgID0geC5tZWFuKGF4aXM9MCkgICAgICAgICAgICAgICAgICAgICAgIyAoZCwpXG4gICAgICAgICAgICB2YXIgPSB4LnZhcihheGlzPTApICAgICAgICAgICAgICAgICAgICAgICAgIyAoZCwpXG4gICAgICAgICAgICB4X2hhdCA9ICh4IC0gbXUpIC8gbnAuc3FydCh2YXIgKyBzZWxmLmVwcylcbiAgICAgICAgICAgICMgVXBkYXRlIHJ1bm5pbmcgc3RhdGlzdGljc1xuICAgICAgICAgICAgc2VsZi5ydW5uaW5nX21lYW4gPSAoKDEgLSBzZWxmLm1vbWVudHVtKSAqIHNlbGYucnVubmluZ19tZWFuXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICArIHNlbGYubW9tZW50dW0gKiBtdSlcbiAgICAgICAgICAgIHNlbGYucnVubmluZ192YXIgID0gKCgxIC0gc2VsZi5tb21lbnR1bSkgKiBzZWxmLnJ1bm5pbmdfdmFyXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICArIHNlbGYubW9tZW50dW0gKiB2YXIpXG4gICAgICAgICAgICBzZWxmLl9jYWNoZSA9ICh4LCB4X2hhdCwgbXUsIHZhcilcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgICMgVXNlIHJ1bm5pbmcgc3RhdHMg4oCUIGRldGVybWluaXN0aWMgaW5mZXJlbmNlXG4gICAgICAgICAgICB4X2hhdCA9ICh4IC0gc2VsZi5ydW5uaW5nX21lYW4pIC8gbnAuc3FydChzZWxmLnJ1bm5pbmdfdmFyICsgc2VsZi5lcHMpXG4gICAgICAgIHJldHVybiBzZWxmLmdhbW1hICogeF9oYXQgKyBzZWxmLmJldGFcblxuICAgIGRlZiB0cmFpbihzZWxmKTogc2VsZi50cmFpbmluZyA9IFRydWVcbiAgICBkZWYgZXZhbChzZWxmKTogIHNlbGYudHJhaW5pbmcgPSBGYWxzZVxuXG5ucC5yYW5kb20uc2VlZCgwKVxuYm4gPSBCYXRjaE5vcm0xZCg4KVxuWF90cmFpbiA9IG5wLnJhbmRvbS5yYW5kbig2NCwgOCkgKiAzICsgNSAgIyBtZWFu4omINSwgc3Rk4omIM1xuXG4jIFNpbXVsYXRlIGEgZmV3IHRyYWluaW5nIHN0ZXBzXG5mb3IgaSBpbiByYW5nZSgyMCk6XG4gICAgYmF0Y2ggPSBYX3RyYWluW25wLnJhbmRvbS5jaG9pY2UoNjQsIDE2LCByZXBsYWNlPUZhbHNlKV1cbiAgICBvdXQgPSBibihiYXRjaClcblxucHJpbnQoZlx1MDAyN0FmdGVyIDIwIHRyYWluIHN0ZXBzOlx1MDAyNylcbnByaW50KGZcdTAwMjcgIHJ1bm5pbmdfbWVhbjoge2JuLnJ1bm5pbmdfbWVhbls6NF0ucm91bmQoMyl9XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgcnVubmluZ192YXI6ICB7Ym4ucnVubmluZ192YXJbOjRdLnJvdW5kKDMpfVx1MDAyNylcblxuIyBUcmFpbiBtb2RlIG9uIGEgc2luZ2xlIHNhbXBsZVxuYm4uZXZhbCgpXG5vdXRfZXZhbCA9IGJuKFhfdHJhaW5bWzBdXSlcbnByaW50KGZcdTAwMjdFdmFsIG1vZGUgb3V0cHV0IChkZXRlcm1pbmlzdGljKToge291dF9ldmFsWzAsIDo0XS5yb3VuZCg0KX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3JpdGljYWw6IG1vZGVsLmV2YWwoKSBNYXR0ZXJzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxudG9yY2gubWFudWFsX3NlZWQoMClcbm1vZGVsID0gbm4uU2VxdWVudGlhbChcbiAgICBubi5MaW5lYXIoMTYsIDY0KSxcbiAgICBubi5CYXRjaE5vcm0xZCg2NCksXG4gICAgbm4uUmVMVSgpLFxuICAgIG5uLkxpbmVhcig2NCwgNClcbilcblxuIyBTaW11bGF0ZSB0cmFpbmluZzogdXBkYXRlIHJ1bm5pbmcgc3RhdHNcbm1vZGVsLnRyYWluKClcbmZvciBfIGluIHJhbmdlKDEwMCk6XG4gICAgeGIgPSB0b3JjaC5yYW5kbigzMiwgMTYpICogNSArIDMgICMgbm9uLXN0YW5kYXJkIGRpc3RyaWJ1dGlvblxuICAgIF8gPSBtb2RlbCh4YilcblxuIyBUZXN0IHBvaW50XG54X3Rlc3QgPSB0b3JjaC5yYW5kbigxLCAxNikgKiA1ICsgM1xuXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAjIFdST05HOiBtb2RlbCBzdGlsbCBpbiB0cmFpbiBtb2RlXG4gICAgbW9kZWwudHJhaW4oKVxuICAgIG91dF90cmFpbiA9IG1vZGVsKHhfdGVzdCkubnVtcHkoKVxuXG4gICAgIyBDT1JSRUNUOiBzd2l0Y2ggdG8gZXZhbCBtb2RlXG4gICAgbW9kZWwuZXZhbCgpXG4gICAgb3V0X2V2YWwgPSBtb2RlbCh4X3Rlc3QpLm51bXB5KClcblxucHJpbnQoXHUwMDI3T3V0cHV0IHdpdGggbW9kZWwudHJhaW4oKSAoYmF0Y2ggc3RhdHMsIHN0b2NoYXN0aWMpOlx1MDAyNylcbnByaW50KFx1MDAyNyBcdTAwMjcsIG91dF90cmFpbi5yb3VuZCg0KSlcbnByaW50KFx1MDAyN091dHB1dCB3aXRoIG1vZGVsLmV2YWwoKSAocnVubmluZyBzdGF0cywgZGV0ZXJtaW5pc3RpYyk6XHUwMDI3KVxucHJpbnQoXHUwMDI3IFx1MDAyNywgb3V0X2V2YWwucm91bmQoNCkpXG5wcmludChcdTAwMjdNYXggZGlmZmVyZW5jZTpcdTAwMjcsIG5wLmFicyhvdXRfdHJhaW4gLSBvdXRfZXZhbCkubWF4KCkucm91bmQoNCkpXG5wcmludChcdTAwMjdcXG5SdW5uaW5nIG1lYW4gb2YgQk4gbGF5ZXI6XHUwMDI3LCBtb2RlbFsxXS5ydW5uaW5nX21lYW5bOjRdLm51bXB5KCkucm91bmQoMykpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJBbHdheXMgQ2FsbCBtb2RlbC5ldmFsKCkgQmVmb3JlIEluZmVyZW5jZSIsImNvbnRlbnQiOiJGb3JnZXR0aW5nIG1vZGVsLmV2YWwoKSBjYXVzZXMgQmF0Y2hOb3JtIHRvIHVzZSB0aGUgY3VycmVudCBtaW5pLWJhdGNoIHN0YXRpc3RpY3MgaW5zdGVhZCBvZiB0aGUgbGVhcm5lZCBydW5uaW5nIHN0YXRpc3RpY3MuIFdpdGggbT0xIGF0IGluZmVyZW5jZSwgdmFyaWFuY2UgaXMgMCBhbmQgb3V0cHV0cyBjYW4gYmUgTmFOIG9yIHdpbGRseSBvZmYuIERyb3BvdXQgYWxzbyByZW1haW5zIGFjdGl2ZSBpbiB0cmFpbiBtb2RlLiBBbHdheXMgY2FsbCBtb2RlbC5ldmFsKCkgYmVmb3JlIGFueSBpbmZlcmVuY2UsIGV2YWx1YXRpb24gbG9vcCwgb3IgZXhwb3J0IOKAlCBhbmQgbW9kZWwudHJhaW4oKSBiZWZvcmUgcmVzdW1pbmcgdHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmF0Y2ggTm9ybSBHcmFkaWVudCBEZXJpdmF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGJuX2JhY2t3YXJkX2FuYWx5dGljYWwoZG91dCwgY2FjaGUpOlxuICAgIFwiXCJcIkFuYWx5dGljYWwgYmFja3dhcmQgcGFzcyBmb3IgYmF0Y2ggbm9ybS5cIlwiXCJcbiAgICB4LCB4X2hhdCwgbXUsIHZhciwgZ2FtbWEsIGVwcyA9IGNhY2hlXG4gICAgbSwgZCA9IHguc2hhcGVcbiAgICAjIEdyYWRpZW50cyBvZiBsZWFybmFibGUgcGFyYW1zXG4gICAgZGdhbW1hID0gKGRvdXQgKiB4X2hhdCkuc3VtKGF4aXM9MCkgICAjIChkLClcbiAgICBkYmV0YSAgPSBkb3V0LnN1bShheGlzPTApICAgICAgICAgICAgICAjIChkLClcbiAgICAjIEdyYWRpZW50IHdydCB4X2hhdFxuICAgIGR4X2hhdCA9IGRvdXQgKiBnYW1tYSAgICAgICAgICAgICAgICAgICMgKG0sIGQpXG4gICAgIyBHcmFkaWVudCB3cnQgdmFyaWFuY2VcbiAgICBzdGRfaW52ID0gMS4wIC8gbnAuc3FydCh2YXIgKyBlcHMpXG4gICAgZHZhciA9IChkeF9oYXQgKiAoeCAtIG11KSAqIC0wLjUgKiBzdGRfaW52KiozKS5zdW0oYXhpcz0wKVxuICAgICMgR3JhZGllbnQgd3J0IG1lYW5cbiAgICBkbXUgPSAoZHhfaGF0ICogKC1zdGRfaW52KSkuc3VtKGF4aXM9MCkgKyBkdmFyICogKC0yLjAgLyBtKSAqICh4IC0gbXUpLnN1bShheGlzPTApXG4gICAgIyBHcmFkaWVudCB3cnQgeFxuICAgIGR4ID0gKGR4X2hhdCAqIHN0ZF9pbnZcbiAgICAgICAgICArIGR2YXIgKiAyLjAgKiAoeCAtIG11KSAvIG1cbiAgICAgICAgICArIGRtdSAvIG0pXG4gICAgcmV0dXJuIGR4LCBkZ2FtbWEsIGRiZXRhXG5cbm5wLnJhbmRvbS5zZWVkKDEpXG5tLCBkID0gMzIsIDhcblhfbnAgPSBucC5yYW5kb20ucmFuZG4obSwgZCkgKiAyICsgMVxuZ2FtbWFfbnAgPSBucC5yYW5kb20ucmFuZChkKSArIDAuNVxuYmV0YV9ucCAgPSBucC5yYW5kb20ucmFuZG4oZClcbmVwcyA9IDFlLTVcblxubXUgID0gWF9ucC5tZWFuKDApOyB2YXIgPSBYX25wLnZhcigwKVxueF9oYXQgPSAoWF9ucCAtIG11KSAvIG5wLnNxcnQodmFyICsgZXBzKVxub3V0ICAgPSBnYW1tYV9ucCAqIHhfaGF0ICsgYmV0YV9ucFxuZG91dCAgPSBucC5yYW5kb20ucmFuZG4obSwgZClcbmNhY2hlID0gKFhfbnAsIHhfaGF0LCBtdSwgdmFyLCBnYW1tYV9ucCwgZXBzKVxuXG5keF9hbmFseXRpY2FsLCBkZ2FtbWFfYSwgZGJldGFfYSA9IGJuX2JhY2t3YXJkX2FuYWx5dGljYWwoZG91dCwgY2FjaGUpXG5cbiMgQ29tcGFyZSB3aXRoIFB5VG9yY2ggYXV0b2dyYWRcblhfdCA9IHRvcmNoLnRlbnNvcihYX25wLCBkdHlwZT10b3JjaC5mbG9hdDY0LCByZXF1aXJlc19ncmFkPVRydWUpXG5nX3QgPSB0b3JjaC50ZW5zb3IoZ2FtbWFfbnAsIGR0eXBlPXRvcmNoLmZsb2F0NjQsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbmJfdCA9IHRvcmNoLnRlbnNvcihiZXRhX25wLCAgZHR5cGU9dG9yY2guZmxvYXQ2NCwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxubXVfdCA9IFhfdC5tZWFuKDApOyB2YXJfdCA9IFhfdC52YXIoMCwgdW5iaWFzZWQ9RmFsc2UpXG54X2hhdF90ID0gKFhfdCAtIG11X3QpIC8gKHZhcl90ICsgZXBzKS5zcXJ0KClcbm91dF90ID0gZ190ICogeF9oYXRfdCArIGJfdFxub3V0X3QuYmFja3dhcmQodG9yY2gudGVuc29yKGRvdXQsIGR0eXBlPXRvcmNoLmZsb2F0NjQpKVxuXG5wcmludChmXHUwMDI3ZHggICAgIG1heCBkaWZmOiB7bnAuYWJzKGR4X2FuYWx5dGljYWwgLSBYX3QuZ3JhZC5udW1weSgpKS5tYXgoKTouMmV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN2RnYW1tYSBtYXggZGlmZjoge25wLmFicyhkZ2FtbWFfYSAtIGdfdC5ncmFkLm51bXB5KCkpLm1heCgpOi4yZX1cdTAwMjcpXG5wcmludChmXHUwMDI3ZGJldGEgIG1heCBkaWZmOiB7bnAuYWJzKGRiZXRhX2EgIC0gYl90LmdyYWQubnVtcHkoKSkubWF4KCk6LjJlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCYXRjaCBTaXplIEVmZmVjdHMgb24gQk4gUXVhbGl0eSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5cbmRlZiBibl9ub2lzZV9ieV9iYXRjaF9zaXplKGJhdGNoX3NpemUsIG5fZXhwZXJpbWVudHM9MjAwLCBkPTY0KTpcbiAgICBcIlwiXCJNZWFzdXJlIHZhcmlhbmNlIG9mIEJOIG5vcm1hbGlzZWQgYWN0aXZhdGlvbnMgYWNyb3NzIGJhdGNoZXMuXCJcIlwiXG4gICAgYm4gPSBubi5CYXRjaE5vcm0xZChkKVxuICAgIGJuLnRyYWluKClcbiAgICBub3JtcyA9IFtdXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl9leHBlcmltZW50cyk6XG4gICAgICAgIHggPSB0b3JjaC5yYW5kbihiYXRjaF9zaXplLCBkKSAqIDMgKyAyXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgb3V0ID0gYm4oeClcbiAgICAgICAgbm9ybXMuYXBwZW5kKG91dC5zdGQoZGltPTApLm1lYW4oKS5pdGVtKCkpXG4gICAgcmV0dXJuIGZsb2F0KG5wLm1lYW4obm9ybXMpKSwgZmxvYXQobnAuc3RkKG5vcm1zKSlcblxucHJpbnQoZlx1MDAyN3tcIkJhdGNoIFNpemVcIjpcdTAwM2UxMn0gIHtcIk1lYW4gc3RkXCI6XHUwMDNlMTB9ICB7XCJTdGQgb2Ygc3RkXCI6XHUwMDNlMTJ9ICB7XCJCTiBSZWxpYWJsZVwiOlx1MDAzZTEyfVx1MDAyNylcbmZvciBicyBpbiBbMiwgNCwgOCwgMTYsIDMyLCA2NCwgMTI4LCAyNTZdOlxuICAgIG1lYW5fcywgc3RkX3MgPSBibl9ub2lzZV9ieV9iYXRjaF9zaXplKGJzKVxuICAgIHJlbGlhYmxlID0gc3RkX3MgXHUwMDNjIDAuMDVcbiAgICBwcmludChmXHUwMDI3e2JzOlx1MDAzZTEyfSAge21lYW5fczpcdTAwM2UxMC40Zn0gIHtzdGRfczpcdTAwM2UxMi40Zn0gIHtzdHIocmVsaWFibGUpOlx1MDAzZTEyfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOb3JtYWxpc2F0aW9uIE1ldGhvZCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIk5vcm1hbGlzZXMgT3ZlciIsIkJhdGNoIERlcGVuZGVudD8iLCJXb3JrcyBmb3IgbT0xPyIsIkJlc3QgRm9yIl0sInJvd3MiOltbIkJhdGNoIE5vcm0iLCJCYXRjaCBkaW1lbnNpb24gKHBlciBmZWF0dXJlKSIsIlllcyDigJQgdXNlcyBiYXRjaCDOvCzPgyIsIk5vIOKAlCDPgz0wLCBOYU4iLCJDTk5zIHdpdGggbGFyZ2UgYmF0Y2hlczsgc3VwZXJ2aXNlZCBpbWFnZSBtb2RlbHMiXSxbIkxheWVyIE5vcm0iLCJGZWF0dXJlIGRpbWVuc2lvbiAocGVyIHNhbXBsZSkiLCJObyDigJQgcGVyLXNhbXBsZSBzdGF0cyIsIlllcyIsIlRyYW5zZm9ybWVycywgTkxQLCB2YXJpYWJsZS1sZW5ndGggc2VxdWVuY2VzIl0sWyJJbnN0YW5jZSBOb3JtIiwiU3BhdGlhbCBkaW1zIHBlciBzYW1wbGUgcGVyIGNoYW5uZWwiLCJObyIsIlllcyIsIlN0eWxlIHRyYW5zZmVyLCBpbWFnZSBnZW5lcmF0aW9uIChzaW5nbGUtc2FtcGxlIHN0eWxlKSJdLFsiR3JvdXAgTm9ybSIsIkdyb3VwcyBvZiBjaGFubmVscyBwZXIgc2FtcGxlIiwiTm8iLCJZZXMiLCJPYmplY3QgZGV0ZWN0aW9uLCBzbWFsbC1iYXRjaCByZWdpbWVzIChiYXRjaCBzaXplIDLigJM0KSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGxhY2VtZW50OiBQcmUtQWN0aXZhdGlvbiB2cyBQb3N0LUFjdGl2YXRpb24gQk4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvcmlnaW5hbCBCTiBwYXBlciAoSW9mZmUgXHUwMDI2IFN6ZWdlZHkgMjAxNSkgcGxhY2VzIEJOIGFmdGVyIHRoZSBsaW5lYXIgbGF5ZXIgYW5kIGJlZm9yZSB0aGUgYWN0aXZhdGlvbjogTGluZWFyIOKGkiBCTiDihpIgUmVMVS4gSGUgZXQgYWwuICgyMDE2KSBwcm9wb3NlZCBwcmUtYWN0aXZhdGlvbiBvcmRlcmluZyBmb3IgUmVzTmV0czogQk4g4oaSIFJlTFUg4oaSIENvbnYsIHdoaWNoIGtlZXBzIHRoZSByZXNpZHVhbCBwYXRoIGNsZWFuIChpZGVudGl0eSBzaG9ydGN1dCBhZGRzIHVuLW5vcm1hbGlzZWQgdmFsdWVzKSBhbmQgZW1waXJpY2FsbHkgaW1wcm92ZXMgdHJhaW5pbmcgb2YgdmVyeSBkZWVwIG5ldHdvcmtzLiBGb3IgVHJhbnNmb3JtZXJzLCBMYXllciBOb3JtIGlzIHBsYWNlZCBiZWZvcmUgdGhlIHN1Yi1sYXllciAoUHJlLUxOKSByYXRoZXIgdGhhbiBhZnRlciAoUG9zdC1MTiBhcyBpbiB0aGUgb3JpZ2luYWwgcGFwZXIpIOKAlCBQcmUtTE4gaW1wcm92ZXMgZ3JhZGllbnQgZmxvdyBhbmQgdHJhaW5pbmcgc3RhYmlsaXR5IGF0IGxhcmdlIHNjYWxlLiBUaGUgcHJhY3RpY2FsIHRha2Vhd2F5OiB3aGVuIGluIGRvdWJ0LCB1c2UgUG9zdC1hY3RpdmF0aW9uIEJOIGZvciBDTk5zIGFuZCBQcmUtTE4gZm9yIFRyYW5zZm9ybWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCZW5lZml0cyBvZiBCYXRjaCBOb3JtYWxpc2F0aW9uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJIaWdoZXIgbGVhcm5pbmcgcmF0ZXM6IEJOIHNtb290aHMgdGhlIGxvc3MgbGFuZHNjYXBlLCBhbGxvd2luZyA14oCTMTDDlyBsYXJnZXIgTFIgd2l0aG91dCBkaXZlcmdpbmcuIiwiUmVkdWNlZCBzZW5zaXRpdml0eSB0byBpbml0aWFsaXNhdGlvbjogcG9vciBpbml0IGlzIHBhcnRpYWxseSBjb3JyZWN0ZWQgYnkgbm9ybWFsaXNhdGlvbiBlYWNoIGZvcndhcmQgcGFzcy4iLCJNaWxkIHJlZ3VsYXJpc2F0aW9uOiBiYXRjaCBzdGF0aXN0aWNzIGludHJvZHVjZSBub2lzZSAoZWFjaCBiYXRjaCBoYXMgZGlmZmVyZW50IM68LM+DKSDigJQgYWN0cyBsaWtlIGRyb3BvdXQuIiwiRmFzdGVyIGNvbnZlcmdlbmNlOiBub3JtYWxpc2VkIGFjdGl2YXRpb25zIHByZXZlbnQgc2F0dXJhdGlvbiBvZiB0YW5oL3NpZ21vaWQ7IHNwZWVkcyB1cCBncmFkaWVudCBmbG93LiIsIkdyYWRpZW50IGNvbmRpdGlvbmluZzogQk4gbWFrZXMgdGhlIGVmZmVjdGl2ZSBIZXNzaWFuIGJldHRlciBjb25kaXRpb25lZCDigJQgbW9yZSB1bmlmb3JtIGN1cnZhdHVyZS4iLCJSZXBsYWNlcyBzb21lIG5lZWQgZm9yIGNhcmVmdWwgaW5pdDogSGUgaW5pdCArIEJOIHRvZ2V0aGVyIGFyZSBuZWFybHkgZm9vbHByb29mIGZvciBDTk4gdHJhaW5pbmcuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbW1vbiBCYXRjaCBOb3JtIE1pc3Rha2VzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJGb3JnZXR0aW5nIG1vZGVsLmV2YWwoKSDigJQgQk4gdXNlcyBiYXRjaCBzdGF0cyBhdCBpbmZlcmVuY2U7IHByZWRpY3Rpb25zIGFyZSBub2lzeSBhbmQgd3JvbmcuIiwiQmF0Y2ggc2l6ZSA9IDEgYXQgdHJhaW4gdGltZSDigJQgdmFyaWFuY2UgaXMgMDsgb3V0cHV0IGlzIE5hTiBvciBhbGwtZ2FtbWEuIFVzZSBncm91cCBub3JtIGluc3RlYWQuIiwiRnJlZXppbmcgQk4gbGF5ZXJzIGJ1dCBub3Qgc2V0dGluZyB0aGVtIHRvIGV2YWwg4oCUIHJ1bm5pbmcgc3RhdHMgZGl2ZXJnZSBmcm9tIGFjdHVhbCBkYXRhIGRpc3RyaWJ1dGlvbi4iLCJEb3VibGUgbm9ybWFsaXNpbmcg4oCUIGFwcGx5aW5nIGJvdGggQk4gYW5kIExheWVyIE5vcm0gaW4gdGhlIHNhbWUgYmxvY2sgcmFyZWx5IGhlbHBzIGFuZCBjYW4gaHVydC4iLCJGb3JnZXR0aW5nIHRvIGNhbGwgbW9kZWwudHJhaW4oKSBhZnRlciBldmFsdWF0aW9uIOKAlCBCTiBzdGF5cyBpbiBldmFsIG1vZGUgYW5kIGlnbm9yZXMgYmF0Y2ggc3RhdHMuIiwiVXNpbmcgQk4gd2l0aCB2ZXJ5IHNtYWxsIGJhdGNoZXMgKFx1MDAzYyA4KSDigJQgc3RhdGlzdGljcyBhcmUgbm9pc3k7IHN3aXRjaCB0byBHcm91cCBOb3JtIHdpdGggRz0zMi4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Batch Normalization — Running Stats, Train vs Eval, and Gradients

Batch Normalisation (BN) normalises the pre-activations of each layer to have zero mean and unit variance within a mini-batch, then re-scales with learnable parameters γ and β. It dramatically accelerates training by allowing higher learning rates, reduces sensitivity to initialisation, and provides mild regularisation through the noise in batch statistics. Understanding the difference between train mode (batch stats) and eval mode (running stats) is critical — confusing them is one of the most common bugs in deep learning.

## Batch Norm Forward Pass

For a mini-batch of m activations x ∈ ℝ^{m × d}: μ_B = (1/m)Σxᵢ ∈ ℝ^d, σ²_B = (1/m)Σ(xᵢ-μ_B)² ∈ ℝ^d, x̂ᵢ = (xᵢ-μ_B)/√(σ²_B+ε), yᵢ = γ⊙x̂ᵢ + β. ε is a small constant (typically 1e-5) for numerical stability. γ ∈ ℝ^d and β ∈ ℝ^d are learnable: γ starts at 1, β at 0. This allows the network to undo normalisation if it helps — BN is strictly more expressive than not having it, since γ=std, β=mean recovers the original distribution.

## Running Statistics and Train vs Eval

At training time, BN uses per-batch statistics μ_B and σ²_B. At inference time, using batch stats is problematic: (1) the batch may have a single sample (m=1, σ²=0); (2) batch statistics introduce randomness into deterministic inference. Solution: maintain exponential moving averages during training: μ_running ← (1-momentum)·μ_running + momentum·μ_B, and similarly for σ²_running. At eval time, use μ_running and σ²_running instead of batch stats. PyTorch's model.train() and model.eval() switch this behaviour — forgetting model.eval() before inference is a common and silent bug.

```python
import numpy as np

class BatchNorm1d:
    """Batch Normalization for 2D input (m, d) with train/eval modes."""
    def __init__(self, d, eps=1e-5, momentum=0.1):
        self.gamma = np.ones(d)
        self.beta  = np.zeros(d)
        self.eps   = eps
        self.momentum = momentum
        self.running_mean = np.zeros(d)
        self.running_var  = np.ones(d)
        self.training = True
        self._cache = None

    def __call__(self, x):
        if self.training:
            mu  = x.mean(axis=0)                      # (d,)
            var = x.var(axis=0)                        # (d,)
            x_hat = (x - mu) / np.sqrt(var + self.eps)
            # Update running statistics
            self.running_mean = ((1 - self.momentum) * self.running_mean
                                 + self.momentum * mu)
            self.running_var  = ((1 - self.momentum) * self.running_var
                                 + self.momentum * var)
            self._cache = (x, x_hat, mu, var)
        else:
            # Use running stats — deterministic inference
            x_hat = (x - self.running_mean) / np.sqrt(self.running_var + self.eps)
        return self.gamma * x_hat + self.beta

    def train(self): self.training = True
    def eval(self):  self.training = False

np.random.seed(0)
bn = BatchNorm1d(8)
X_train = np.random.randn(64, 8) * 3 + 5  # mean≈5, std≈3

# Simulate a few training steps
for i in range(20):
    batch = X_train[np.random.choice(64, 16, replace=False)]
    out = bn(batch)

print(f'After 20 train steps:')
print(f'  running_mean: {bn.running_mean[:4].round(3)}')
print(f'  running_var:  {bn.running_var[:4].round(3)}')

# Train mode on a single sample
bn.eval()
out_eval = bn(X_train[[0]])
print(f'Eval mode output (deterministic): {out_eval[0, :4].round(4)}')
```

## Critical: model.eval() Matters

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(0)
model = nn.Sequential(
    nn.Linear(16, 64),
    nn.BatchNorm1d(64),
    nn.ReLU(),
    nn.Linear(64, 4)
)

# Simulate training: update running stats
model.train()
for _ in range(100):
    xb = torch.randn(32, 16) * 5 + 3  # non-standard distribution
    _ = model(xb)

# Test point
x_test = torch.randn(1, 16) * 5 + 3

with torch.no_grad():
    # WRONG: model still in train mode
    model.train()
    out_train = model(x_test).numpy()

    # CORRECT: switch to eval mode
    model.eval()
    out_eval = model(x_test).numpy()

print('Output with model.train() (batch stats, stochastic):')
print(' ', out_train.round(4))
print('Output with model.eval() (running stats, deterministic):')
print(' ', out_eval.round(4))
print('Max difference:', np.abs(out_train - out_eval).max().round(4))
print('\nRunning mean of BN layer:', model[1].running_mean[:4].numpy().round(3))
```

> **Always Call model.eval() Before Inference**: Forgetting model.eval() causes BatchNorm to use the current mini-batch statistics instead of the learned running statistics. With m=1 at inference, variance is 0 and outputs can be NaN or wildly off. Dropout also remains active in train mode. Always call model.eval() before any inference, evaluation loop, or export — and model.train() before resuming training.

## Batch Norm Gradient Derivation

```python
import numpy as np
import torch
import torch.nn as nn

def bn_backward_analytical(dout, cache):
    """Analytical backward pass for batch norm."""
    x, x_hat, mu, var, gamma, eps = cache
    m, d = x.shape
    # Gradients of learnable params
    dgamma = (dout * x_hat).sum(axis=0)   # (d,)
    dbeta  = dout.sum(axis=0)              # (d,)
    # Gradient wrt x_hat
    dx_hat = dout * gamma                  # (m, d)
    # Gradient wrt variance
    std_inv = 1.0 / np.sqrt(var + eps)
    dvar = (dx_hat * (x - mu) * -0.5 * std_inv**3).sum(axis=0)
    # Gradient wrt mean
    dmu = (dx_hat * (-std_inv)).sum(axis=0) + dvar * (-2.0 / m) * (x - mu).sum(axis=0)
    # Gradient wrt x
    dx = (dx_hat * std_inv
          + dvar * 2.0 * (x - mu) / m
          + dmu / m)
    return dx, dgamma, dbeta

np.random.seed(1)
m, d = 32, 8
X_np = np.random.randn(m, d) * 2 + 1
gamma_np = np.random.rand(d) + 0.5
beta_np  = np.random.randn(d)
eps = 1e-5

mu  = X_np.mean(0); var = X_np.var(0)
x_hat = (X_np - mu) / np.sqrt(var + eps)
out   = gamma_np * x_hat + beta_np
dout  = np.random.randn(m, d)
cache = (X_np, x_hat, mu, var, gamma_np, eps)

dx_analytical, dgamma_a, dbeta_a = bn_backward_analytical(dout, cache)

# Compare with PyTorch autograd
X_t = torch.tensor(X_np, dtype=torch.float64, requires_grad=True)
g_t = torch.tensor(gamma_np, dtype=torch.float64, requires_grad=True)
b_t = torch.tensor(beta_np,  dtype=torch.float64, requires_grad=True)
mu_t = X_t.mean(0); var_t = X_t.var(0, unbiased=False)
x_hat_t = (X_t - mu_t) / (var_t + eps).sqrt()
out_t = g_t * x_hat_t + b_t
out_t.backward(torch.tensor(dout, dtype=torch.float64))

print(f'dx     max diff: {np.abs(dx_analytical - X_t.grad.numpy()).max():.2e}')
print(f'dgamma max diff: {np.abs(dgamma_a - g_t.grad.numpy()).max():.2e}')
print(f'dbeta  max diff: {np.abs(dbeta_a  - b_t.grad.numpy()).max():.2e}')
```

## Batch Size Effects on BN Quality

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(0)

def bn_noise_by_batch_size(batch_size, n_experiments=200, d=64):
    """Measure variance of BN normalised activations across batches."""
    bn = nn.BatchNorm1d(d)
    bn.train()
    norms = []
    for _ in range(n_experiments):
        x = torch.randn(batch_size, d) * 3 + 2
        with torch.no_grad():
            out = bn(x)
        norms.append(out.std(dim=0).mean().item())
    return float(np.mean(norms)), float(np.std(norms))

print(f'{"Batch Size":>12}  {"Mean std":>10}  {"Std of std":>12}  {"BN Reliable":>12}')
for bs in [2, 4, 8, 16, 32, 64, 128, 256]:
    mean_s, std_s = bn_noise_by_batch_size(bs)
    reliable = std_s < 0.05
    print(f'{bs:>12}  {mean_s:>10.4f}  {std_s:>12.4f}  {str(reliable):>12}')
```

## Normalisation Method Comparison

| Method | Normalises Over | Batch Dependent? | Works for m=1? | Best For |
| --- | --- | --- | --- | --- |
| Batch Norm | Batch dimension (per feature) | Yes — uses batch μ,σ | No — σ=0, NaN | CNNs with large batches; supervised image models |
| Layer Norm | Feature dimension (per sample) | No — per-sample stats | Yes | Transformers, NLP, variable-length sequences |
| Instance Norm | Spatial dims per sample per channel | No | Yes | Style transfer, image generation (single-sample style) |
| Group Norm | Groups of channels per sample | No | Yes | Object detection, small-batch regimes (batch size 2–4) |

## Placement: Pre-Activation vs Post-Activation BN

The original BN paper (Ioffe & Szegedy 2015) places BN after the linear layer and before the activation: Linear → BN → ReLU. He et al. (2016) proposed pre-activation ordering for ResNets: BN → ReLU → Conv, which keeps the residual path clean (identity shortcut adds un-normalised values) and empirically improves training of very deep networks. For Transformers, Layer Norm is placed before the sub-layer (Pre-LN) rather than after (Post-LN as in the original paper) — Pre-LN improves gradient flow and training stability at large scale. The practical takeaway: when in doubt, use Post-activation BN for CNNs and Pre-LN for Transformers.

## Benefits of Batch Normalisation

- Higher learning rates: BN smooths the loss landscape, allowing 5–10× larger LR without diverging.
- Reduced sensitivity to initialisation: poor init is partially corrected by normalisation each forward pass.
- Mild regularisation: batch statistics introduce noise (each batch has different μ,σ) — acts like dropout.
- Faster convergence: normalised activations prevent saturation of tanh/sigmoid; speeds up gradient flow.
- Gradient conditioning: BN makes the effective Hessian better conditioned — more uniform curvature.
- Replaces some need for careful init: He init + BN together are nearly foolproof for CNN training.

## Common Batch Norm Mistakes

- Forgetting model.eval() — BN uses batch stats at inference; predictions are noisy and wrong.
- Batch size = 1 at train time — variance is 0; output is NaN or all-gamma. Use group norm instead.
- Freezing BN layers but not setting them to eval — running stats diverge from actual data distribution.
- Double normalising — applying both BN and Layer Norm in the same block rarely helps and can hurt.
- Forgetting to call model.train() after evaluation — BN stays in eval mode and ignores batch stats.
- Using BN with very small batches (< 8) — statistics are noisy; switch to Group Norm with G=32.

---

