---
title: "GRU — Reset and Update Gates"
slug: "gru-gated-recurrent-unit"
description: "GRU (Cho et al. 2014) simplifies LSTM to two gates and no separate cell state: update gate zt interpolates between old and new hidden state, reset gate rt controls how much past context enters the candidate. Covers parameter count comparison, minGRU parallel variant, reset gate visualization, and when to prefer GRU over LSTM."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR1JVIChHYXRlZCBSZWN1cnJlbnQgVW5pdCwgQ2hvIGV0IGFsLiAyMDE0KSBzaW1wbGlmaWVzIHRoZSBMU1RNIGFyY2hpdGVjdHVyZSBmcm9tIHRocmVlIGdhdGVzIGFuZCBhIHNlcGFyYXRlIGNlbGwgc3RhdGUgdG8gdHdvIGdhdGVzIHdpdGggYSBzaW5nbGUgaGlkZGVuIHN0YXRlLiBEZXNwaXRlIHRoaXMgc2ltcGxpZmljYXRpb24sIEdSVSBvZnRlbiBtYXRjaGVzIExTVE0gcGVyZm9ybWFuY2Ugb24gbWFueSBzZXF1ZW5jZSB0YXNrcyB3aGlsZSB0cmFpbmluZyByb3VnaGx5IDI1JSBmYXN0ZXIgZHVlIHRvIGZld2VyIHBhcmFtZXRlcnMuIFVuZGVyc3RhbmRpbmcgd2hlbiBHUlUgaXMgcHJlZmVyYWJsZSDigJQgYW5kIGhvdyBpdHMgdHdvIGdhdGVzIGNvdmVyIHRoZSBzYW1lIGNvbmNlcHR1YWwgZ3JvdW5kIGFzIExTVE1cdTAwMjdzIHRocmVlIOKAlCBpcyBlc3NlbnRpYWwgZm9yIGNob29zaW5nIHRoZSByaWdodCBhcmNoaXRlY3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR1JVIEFyY2hpdGVjdHVyZSDigJQgVHdvIEdhdGVzLCBObyBDZWxsIFN0YXRlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHUlUgY29tcHV0ZXM6IHVwZGF0ZSBnYXRlIHp0ID0gz4MoV3pbaHQtMSwgeHRdKTsgcmVzZXQgZ2F0ZSBydCA9IM+DKFdyW2h0LTEsIHh0XSk7IGNhbmRpZGF0ZSBozIN0ID0gdGFuaChXaFtydCDiipkgaHQtMSwgeHRdKTsgbmV3IGhpZGRlbiBodCA9IHp0IOKKmSBodC0xICsgKDEtenQpIOKKmSBozIN0LiBUaGUgdXBkYXRlIGdhdGUgenQgcGxheXMgdGhlIGNvbWJpbmVkIHJvbGUgb2YgTFNUTVx1MDAyN3MgZm9yZ2V0IGFuZCBpbnB1dCBnYXRlczogenQg4omIIDEgbWVhbnMga2VlcCB0aGUgb2xkIGhpZGRlbiBzdGF0ZSAoZXF1aXZhbGVudCB0byBmdCDiiYggMSBhbmQgaXQg4omIIDAgaW4gTFNUTSk7IHp0IOKJiCAwIG1lYW5zIGZ1bGx5IHJlcGxhY2Ugd2l0aCB0aGUgY2FuZGlkYXRlLiBUaGUgcmVzZXQgZ2F0ZSBydCBjb250cm9scyBob3cgbXVjaCBvZiB0aGUgcGFzdCBoaWRkZW4gc3RhdGUgZW50ZXJzIHRoZSBjYW5kaWRhdGUgY29tcHV0YXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgc2lnbW9pZCh4KTpcbiAgICByZXR1cm4gMS4wIC8gKDEuMCArIG5wLmV4cCgtbnAuY2xpcCh4LCAtMTAsIDEwKSkpXG5cbmNsYXNzIEdSVUNlbGw6XG4gICAgXCJcIlwiTWluaW1hbCBHUlUgY2VsbDogdXBkYXRlIGdhdGUsIHJlc2V0IGdhdGUsIGNhbmRpZGF0ZSwgaW50ZXJwb2xhdGlvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfc2l6ZSwgaGlkZGVuX3NpemUsIHNlZWQ9MCk6XG4gICAgICAgIHJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyhzZWVkKVxuICAgICAgICBzID0gbnAuc3FydCgxLjAgLyBoaWRkZW5fc2l6ZSlcbiAgICAgICAgZCA9IGlucHV0X3NpemUgKyBoaWRkZW5fc2l6ZVxuICAgICAgICBzZWxmLld6ID0gcm5nLm5vcm1hbCgwLCBzLCAoaGlkZGVuX3NpemUsIGQpKTsgIHNlbGYuYnogPSBucC56ZXJvcyhoaWRkZW5fc2l6ZSlcbiAgICAgICAgc2VsZi5XciA9IHJuZy5ub3JtYWwoMCwgcywgKGhpZGRlbl9zaXplLCBkKSk7ICBzZWxmLmJyID0gbnAuemVyb3MoaGlkZGVuX3NpemUpXG4gICAgICAgIHNlbGYuV2ggPSBybmcubm9ybWFsKDAsIHMsIChoaWRkZW5fc2l6ZSwgZCkpOyAgc2VsZi5iaCA9IG5wLnplcm9zKGhpZGRlbl9zaXplKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgaCk6XG4gICAgICAgIHhoID0gbnAuY29uY2F0ZW5hdGUoW3gsIGhdKVxuICAgICAgICB6ID0gc2lnbW9pZChzZWxmLld6IEAgeGggKyBzZWxmLmJ6KSAgICAgICAgICAgIyB1cGRhdGUgZ2F0ZVxuICAgICAgICByID0gc2lnbW9pZChzZWxmLldyIEAgeGggKyBzZWxmLmJyKSAgICAgICAgICAgICMgcmVzZXQgZ2F0ZVxuICAgICAgICB4cmggPSBucC5jb25jYXRlbmF0ZShbeCwgciAqIGhdKVxuICAgICAgICBoX2NhbmQgPSBucC50YW5oKHNlbGYuV2ggQCB4cmggKyBzZWxmLmJoKSAgICAjIGNhbmRpZGF0ZVxuICAgICAgICBoX25ldyAgPSB6ICogaCArICgxIC0geikgKiBoX2NhbmQgICAgICAgICAgICAgIyBpbnRlcnBvbGF0ZVxuICAgICAgICByZXR1cm4gaF9uZXcsIGRpY3Qoej16LCByPXIpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuZ3J1ID0gR1JVQ2VsbChpbnB1dF9zaXplPTQsIGhpZGRlbl9zaXplPTgpXG5oID0gbnAuemVyb3MoOClcbnByaW50KFx1MDAyN0dSVSBmcm9tIHNjcmF0Y2gg4oCUIGdhdGUgYWN0aXZhdGlvbnMgcGVyIHN0ZXA6XHUwMDI3KVxucHJpbnQoXHUwMDI3ezpcdTAwM2U0fSB7Olx1MDAzZTEwfSB7Olx1MDAzZTEwfSB7Olx1MDAzZTEwfVx1MDAyNy5mb3JtYXQoXHUwMDI3dFx1MDAyNywgXHUwMDI3aF9ub3JtXHUwMDI3LCBcdTAwMjd6X21lYW5cdTAwMjcsIFx1MDAyN3JfbWVhblx1MDAyNykpXG5mb3IgdCBpbiByYW5nZSg1KTpcbiAgICB4ID0gbnAucmFuZG9tLnJhbmRuKDQpXG4gICAgaCwgZyA9IGdydS5mb3J3YXJkKHgsIGgpXG4gICAgcHJpbnQoXHUwMDI3ezpcdTAwM2U0fSB7Olx1MDAzZTEwLjRmfSB7Olx1MDAzZTEwLjRmfSB7Olx1MDAzZTEwLjRmfVx1MDAyNy5mb3JtYXQodCwgbnAubGluYWxnLm5vcm0oaCksIGdbXHUwMDI3elx1MDAyN10ubWVhbigpLCBnW1x1MDAyN3JcdTAwMjddLm1lYW4oKSkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVXBkYXRlIEdhdGUg4oCUIEludGVycG9sYXRpb24gQmV0d2VlbiBPbGQgYW5kIE5ldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHVwZGF0ZSBnYXRlIHp0IOKIiCAoMCwxKeG0tCBhY3RzIGFzIGEgbGVhcm5lZCBpbnRlcnBvbGF0aW9uIGNvZWZmaWNpZW50IGJldHdlZW4gdGhlIHByZXZpb3VzIGhpZGRlbiBzdGF0ZSBodC0xIGFuZCB0aGUgbmV3IGNhbmRpZGF0ZSBozIN0OiBodCA9IHp0IOKKmSBodC0xICsgKDEtenQpIOKKmSBozIN0LiBXaGVuIHp0IOKJiCAxLCB0aGUgaGlkZGVuIHN0YXRlIGlzIHByZXNlcnZlZCB1bmNoYW5nZWQg4oCUIHRoZSB1bml0IHJlbWVtYmVycy4gV2hlbiB6dCDiiYggMCwgdGhlIGhpZGRlbiBzdGF0ZSBpcyBmdWxseSByZXBsYWNlZCBieSB0aGUgY2FuZGlkYXRlIOKAlCB0aGUgdW5pdCB1cGRhdGVzLiBUaGlzIHNpbmdsZSBnYXRlIGhhbmRsZXMgd2hhdCBMU1RNIG5lZWRzIHR3byBnYXRlcyAoZm9yZ2V0ICsgaW5wdXQpIHRvIGFjaGlldmUsIGF0IHRoZSBjb3N0IG9mIGxvc2luZyB0aGUgYWJpbGl0eSB0byBpbmRlcGVuZGVudGx5IGNvbnRyb2wgaG93IG11Y2ggdG8gZm9yZ2V0IHZzIGhvdyBtdWNoIHRvIHdyaXRlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlc2V0IEdhdGUg4oCUIENvbnRyb2xsaW5nIENhbmRpZGF0ZSBDb21wdXRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlc2V0IGdhdGUgcnQg4oiIICgwLDEp4bS0IGNvbnRyb2xzIGhvdyBtdWNoIG9mIHRoZSBwcmV2aW91cyBoaWRkZW4gc3RhdGUgZW50ZXJzIHRoZSBjYW5kaWRhdGU6IGjMg3QgPSB0YW5oKFdoW3J0IOKKmSBodC0xLCB4dF0pLiBXaGVuIHJ0IOKJiCAxLCB0aGUgY2FuZGlkYXRlIHNlZXMgdGhlIGZ1bGwgcGFzdCBjb250ZXh0IOKAlCB0aGUgY2VsbCB1c2VzIGl0cyBoaXN0b3J5LiBXaGVuIHJ0IOKJiCAwLCB0aGUgY2FuZGlkYXRlIGNvbXB1dGF0aW9uIGlnbm9yZXMgaHQtMSDigJQgdGhlIHVuaXQgYmVoYXZlcyBhcyBpZiBpdCBoYXMgbm8gbWVtb3J5IGFuZCBnZW5lcmF0ZXMgYSBjYW5kaWRhdGUgcHVyZWx5IGZyb20gdGhlIGN1cnJlbnQgaW5wdXQuIFRoaXMgYWxsb3dzIEdSVSB0byByZXNldCBpdHMgY29udGV4dCB3aGVuIHRoZSBpbnB1dCBkaXN0cmlidXRpb24gY2hhbmdlcyBhYnJ1cHRseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuaW1wb3J0IHRpbWVcblxuZGVmIGJlbmNobWFya19ybm4oY2VsbF90eXBlPVx1MDAyN2dydVx1MDAyNywgST0xNiwgSD02NCwgVD0zMCwgQz01LCBOPTUxMiwgZXBvY2hzPTIwKTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZCg0MilcbiAgICBybm4gPSAobm4uR1JVIGlmIGNlbGxfdHlwZSA9PSBcdTAwMjdncnVcdTAwMjcgZWxzZSBubi5MU1RNKShJLCBILCBiYXRjaF9maXJzdD1UcnVlKVxuICAgIGZjICA9IG5uLkxpbmVhcihILCBDKVxuICAgIG9wdCA9IG9wdGltLkFkYW0obGlzdChybm4ucGFyYW1ldGVycygpKSArIGxpc3QoZmMucGFyYW1ldGVycygpKSwgbHI9MWUtMylcbiAgICB4ID0gdG9yY2gucmFuZG4oTiwgVCwgSSlcbiAgICB5ID0gdG9yY2gucmFuZGludCgwLCBDLCAoTiwpKVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGZvciBfIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIG91dCwgc3RhdGUgPSBybm4oeClcbiAgICAgICAgaCA9IHN0YXRlWzBdLnNxdWVlemUoMCkgaWYgY2VsbF90eXBlID09IFx1MDAyN2xzdG1cdTAwMjcgZWxzZSBzdGF0ZS5zcXVlZXplKDApXG4gICAgICAgIGxvc3MgPSBubi5Dcm9zc0VudHJvcHlMb3NzKCkoZmMoaCksIHkpXG4gICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgZWxhcHNlZCA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBvdXQsIHN0YXRlID0gcm5uKHgpXG4gICAgICAgIGggPSBzdGF0ZVswXS5zcXVlZXplKDApIGlmIGNlbGxfdHlwZSA9PSBcdTAwMjdsc3RtXHUwMDI3IGVsc2Ugc3RhdGUuc3F1ZWV6ZSgwKVxuICAgICAgICBhY2MgPSAoZmMoaCkuYXJnbWF4KDEpID09IHkpLmZsb2F0KCkubWVhbigpLml0ZW0oKVxuICAgIG5fcGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBsaXN0KHJubi5wYXJhbWV0ZXJzKCkpICsgbGlzdChmYy5wYXJhbWV0ZXJzKCkpKVxuICAgIHJldHVybiBhY2MsIGVsYXBzZWQsIG5fcGFyYW1zXG5cbnByaW50KFx1MDAyN0dSVSB2cyBMU1RNIG9uIHNlcXVlbmNlIGNsYXNzaWZpY2F0aW9uIChzZXFfbGVuPTMwLCA1IGNsYXNzZXMpOlx1MDAyNylcbmZvciBuYW1lIGluIFtcdTAwMjdncnVcdTAwMjcsIFx1MDAyN2xzdG1cdTAwMjddOlxuICAgIGFjYywgdCwgbiA9IGJlbmNobWFya19ybm4obmFtZSlcbiAgICBwcmludChcdTAwMjcgIHt9OiBhY2M9ezouM2Z9ICB0aW1lPXs6LjJmfXMgIHBhcmFtcz17Oix9XHUwMDI3LmZvcm1hdChuYW1lLnVwcGVyKCksIGFjYywgdCwgbikpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGFyYW1ldGVyIENvdW50IGFuZCBDb21wdXRhdGlvbmFsIENvc3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdSVSBoYXMgMyBnYXRlIHdlaWdodCBtYXRyaWNlcyAoV3osIFdyLCBXaCkgZWFjaCBvZiBzaGFwZSBIw5coSCtJKSwgZ2l2aW5nIDPCt0jCtyhIK0kpICsgM0ggcGFyYW1ldGVycy4gTFNUTSBoYXMgNCBnYXRlIG1hdHJpY2VzIChXZiwgV2ksIFdnLCBXbyksIGdpdmluZyA0wrdIwrcoSCtJKSArIDRIIHBhcmFtZXRlcnMuIEZvciBIPTI1NiwgST0xMjgsIEdSVSBoYXMgfjI5NEsgcGFyYW1ldGVycyB2cyBMU1RNIH4zOTJLIOKAlCBhIDI1JSByZWR1Y3Rpb24uIEdSVSBhbHNvIHBlcmZvcm1zIGZld2VyIG1hdHJpeCBtdWx0aXBsaWNhdGlvbnMgcGVyIHN0ZXAgYW5kIGhhcyBubyBjZWxsIHN0YXRlIHRvIG1haW50YWluLCBtYWtpbmcgZWFjaCBmb3J3YXJkIHN0ZXAgcm91Z2hseSAyNSUgZmFzdGVyIGluIHByYWN0aWNlLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIkdhdGVzIiwiQ2VsbCBTdGF0ZSIsIlBhcmFtcyAoSD0yNTYsIEk9MTI4KSIsIlBhcmFsbGVsaXphYmxlIiwiVHlwaWNhbCBQZXJmIl0sInJvd3MiOltbIlZhbmlsbGEgUk5OIiwiMCAoZGlyZWN0IFdoaCkiLCJObyIsIn45OEsiLCJObyAoc2VxdWVudGlhbCkiLCJCYXNlbGluZSDigJQgZmFpbHMgb24gbG9uZyBzZXF1ZW5jZXMiXSxbIkdSVSIsIjIgKHVwZGF0ZSwgcmVzZXQpIiwiTm8iLCJ+Mjk0SyIsIk5vIChzZXF1ZW50aWFsKSIsIk9uIHBhciB3aXRoIExTVE0gb24gc2hvcnQtbWlkIHRhc2tzIl0sWyJMU1RNIiwiMyAoZm9yZ2V0LCBpbnB1dCwgb3V0cHV0KSIsIlllcyAoQ3QpIiwifjM5M0siLCJObyAoc2VxdWVudGlhbCkiLCJCZXN0IG9uIGxvbmcgc2VxdWVuY2VzIHdpdGggZmluZSBjb250cm9sIl0sWyJtaW5HUlUgKDIwMjQpIiwiMSAodXBkYXRlLCBubyByZXNldCkiLCJObyIsIn4xMzFLIiwiWWVzIChwYXJhbGxlbCBzY2FuKSIsIkNvbXBldGl0aXZlIG9uIG1hbnkgdGFza3MsIG11Y2ggZmFzdGVyIHRyYWluaW5nIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJtaW5HUlUg4oCUIFBhcmFsbGVsLVRyYWluYWJsZSBTaW1wbGlmaWVkIEdSVSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoibWluR1JVIChGZW5nIGV0IGFsLiAyMDI0KSByZW1vdmVzIHRoZSByZXNldCBnYXRlIGFuZCB0aGUgdGFuaCBub25saW5lYXJpdHkgZnJvbSB0aGUgY2FuZGlkYXRlLCBhbmQgbWFrZXMgdGhlIGNhbmRpZGF0ZSBkZXBlbmQgb25seSBvbiB0aGUgY3VycmVudCBpbnB1dCB4dCDigJQgbm90IG9uIGh0LTEuIFRoaXMgYnJlYWtzIHRoZSBzZXF1ZW50aWFsIGRlcGVuZGVuY3kgaW4gdGhlIGZvcndhcmQgcGFzcywgZW5hYmxpbmcgZnVsbHkgcGFyYWxsZWwgdHJhaW5pbmcgdmlhIGFuIGFzc29jaWF0aXZlIHNjYW4gKHNpbWlsYXIgdG8gaG93IHByZWZpeC1zdW0gY2FuIGJlIHBhcmFsbGVsaXplZCkuIFRoZSByZXN1bHQgaXMgYSBtb2RlbCB0aGF0IHRyYWlucyBtdWNoIGZhc3RlciB0aGFuIHN0YW5kYXJkIEdSVSBvbiBsb25nIHNlcXVlbmNlcyB3aGlsZSByZW1haW5pbmcgY29tcGV0aXRpdmUgb24gbWFueSBiZW5jaG1hcmtzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBNaW5HUlUobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJtaW5HUlUgKEZlbmcgZXQgYWwuIDIwMjQpOiBubyByZXNldCBnYXRlLCBubyB0YW5oLCBpbnB1dC1vbmx5IGNhbmRpZGF0ZS5cblxuICAgIFJlbW92ZXMgc2VxdWVudGlhbCBkZXBlbmRlbmN5IC1cdTAwM2UgdHJhaW5hYmxlIGluIHBhcmFsbGVsIHZpYSBhc3NvY2lhdGl2ZSBzY2FuLlxuICAgIFNlcXVlbnRpYWwgbG9vcCBzaG93biBoZXJlIGZvciBjbGFyaXR5OyByZWFsIGltcGwgdXNlcyBsb2ctc3BhY2UgcGFyYWxsZWwgc2Nhbi5cbiAgICBcIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfc2l6ZSwgaGlkZGVuX3NpemUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5nYXRlICAgICAgPSBubi5MaW5lYXIoaW5wdXRfc2l6ZSwgaGlkZGVuX3NpemUpICAgIyB1cGRhdGUgZ2F0ZVxuICAgICAgICBzZWxmLmNhbmRpZGF0ZSA9IG5uLkxpbmVhcihpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSkgICAjIGNhbmRpZGF0ZSAobm8gdGFuaCwgbm8gaClcbiAgICAgICAgc2VsZi5oaWRkZW5fc2l6ZSA9IGhpZGRlbl9zaXplXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgXCJcIlwieDogKEIsIFQsIEkpLiBSZXR1cm5zIChCLCBULCBIKSBvdXRwdXQgc2VxdWVuY2UuXCJcIlwiXG4gICAgICAgIHogICAgICA9IHRvcmNoLnNpZ21vaWQoc2VsZi5nYXRlKHgpKSAgICAgICMgKEIsIFQsIEgpIHVwZGF0ZSBnYXRlc1xuICAgICAgICBoX3RpbGQgPSBzZWxmLmNhbmRpZGF0ZSh4KSAgICAgICAgICAgICAgICAjIChCLCBULCBIKSBjYW5kaWRhdGVzXG4gICAgICAgIEIgPSB4LnNpemUoMClcbiAgICAgICAgaCA9IHRvcmNoLnplcm9zKEIsIHNlbGYuaGlkZGVuX3NpemUpXG4gICAgICAgIG91dHB1dHMgPSBbXVxuICAgICAgICBmb3IgdCBpbiByYW5nZSh4LnNpemUoMSkpOlxuICAgICAgICAgICAgaCA9ICgxIC0gels6LCB0XSkgKiBoICsgels6LCB0XSAqIGhfdGlsZFs6LCB0XVxuICAgICAgICAgICAgb3V0cHV0cy5hcHBlbmQoaClcbiAgICAgICAgcmV0dXJuIHRvcmNoLnN0YWNrKG91dHB1dHMsIGRpbT0xKVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubW9kZWwgPSBNaW5HUlUoaW5wdXRfc2l6ZT04LCBoaWRkZW5fc2l6ZT0xNilcbnggPSB0b3JjaC5yYW5kbig0LCAyMCwgOClcbm91dCA9IG1vZGVsKHgpXG5mdWxsX2dydV9wYXJhbXMgPSAzICogKDggKiAxNiArIDE2ICogMTYgKyAxNilcbnByaW50KFx1MDAyN21pbkdSVSBvdXRwdXQ6IHt9XHUwMDI3LmZvcm1hdCh0dXBsZShvdXQuc2hhcGUpKSlcbnByaW50KFx1MDAyN21pbkdSVSBwYXJhbXM6IHs6LH0gIHZzIGZ1bGwgR1JVIHBhcmFtczogezosfVx1MDAyNy5mb3JtYXQoXG4gICAgc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpLCBmdWxsX2dydV9wYXJhbXMpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlc2V0IEdhdGUgVmlzdWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlc2V0IGdhdGUgdGVuZHMgdG8gZmlyZSAoYXBwcm9hY2ggMCkgd2hlbiB0aGUgaW5wdXQgZGlzdHJpYnV0aW9uIGNoYW5nZXMgYWJydXB0bHksIGFsbG93aW5nIHRoZSBjYW5kaWRhdGUgdG8gYmUgY29tcHV0ZWQgZnJvbSBzY3JhdGNoIHdpdGhvdXQgY29udGFtaW5hdGlvbiBmcm9tIHN0YWxlIGhpZGRlbiBzdGF0ZS4gT24gc3RhdGlvbmFyeSBpbnB1dCwgdGhlIHJlc2V0IGdhdGUgc3RheXMgbmVhciAxLCBwcmVzZXJ2aW5nIGNvbnRleHQuIFRoaXMgYmVoYXZpb3IgaXMgbGVhcm5lZCBhdXRvbWF0aWNhbGx5IGZyb20gZGF0YSDigJQgdGhlIG5ldHdvcmsgZGlzY292ZXJzIHRoYXQgcmVzZXR0aW5nIGNvbnRleHQgaGVscHMgcmVjb3ZlciBmcm9tIGRpc3RyaWJ1dGlvbiBzaGlmdHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHZpc3VhbGl6ZV9yZXNldF9nYXRlKHNlcV9sZW49NDAsIGlucHV0X3NpemU9NCwgaGlkZGVuX3NpemU9OCwgc2VlZD0yKTpcbiAgICBcIlwiXCJTaG93IHJlc2V0IGdhdGUgYWN0aXZhdGlvbnMgYWNyb3NzIGEgdHdvLXBoYXNlIHNlcXVlbmNlLlwiXCJcIlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgY2VsbCA9IG5uLkdSVUNlbGwoaW5wdXRfc2l6ZSwgaGlkZGVuX3NpemUpXG4gICAgeCA9IHRvcmNoLmNhdChbXG4gICAgICAgIHRvcmNoLnJhbmRuKHNlcV9sZW4gLy8gMiwgaW5wdXRfc2l6ZSkgKiAwLjIsICAgIyBzbW9vdGggcGhhc2VcbiAgICAgICAgdG9yY2gucmFuZG4oc2VxX2xlbiAvLyAyLCBpbnB1dF9zaXplKSAqIDMuMCAgICAjIGhpZ2gtdmFyaWFuY2UgcGhhc2VcbiAgICBdLCBkaW09MClcbiAgICBoID0gdG9yY2guemVyb3MoMSwgaGlkZGVuX3NpemUpXG4gICAgcmVzZXRfbWVhbnMgPSBbXVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgdCBpbiByYW5nZShzZXFfbGVuKTpcbiAgICAgICAgICAgIHByZSA9ICh4W3Q6dCsxXSBAIGNlbGwud2VpZ2h0X2loLlQgKyBoIEAgY2VsbC53ZWlnaHRfaGguVFxuICAgICAgICAgICAgICAgICAgICsgY2VsbC5iaWFzX2loICsgY2VsbC5iaWFzX2hoKVxuICAgICAgICAgICAgcl9nYXRlID0gdG9yY2guc2lnbW9pZChwcmVbOiwgaGlkZGVuX3NpemU6MipoaWRkZW5fc2l6ZV0pXG4gICAgICAgICAgICByZXNldF9tZWFucy5hcHBlbmQocl9nYXRlLm1lYW4oKS5pdGVtKCkpXG4gICAgICAgICAgICBoID0gY2VsbCh4W3Q6dCsxXSwgaClcbiAgICBybSA9IG5wLmFycmF5KHJlc2V0X21lYW5zKVxuICAgIHByaW50KFx1MDAyN1Jlc2V0IGdhdGUgbWVhbiAoMD1pZ25vcmUgcGFzdCwgMT11c2UgcGFzdCk6XHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgU21vb3RoIHQ9MDAtMTk6IHs6LjNmfVx1MDAyNy5mb3JtYXQocm1bOjIwXS5tZWFuKCkpKVxuICAgIHByaW50KFx1MDAyNyAgTm9pc3kgIHQ9MjAtMzk6IHs6LjNmfVx1MDAyNy5mb3JtYXQocm1bMjA6XS5tZWFuKCkpKVxuICAgIHByaW50KFx1MDAyNyAgVHJhbnNpdGlvbiB0PTIwOiB7Oi4zZn0gIFx1MDAzYy0gcmVzZXRzIG9uIHN1ZGRlbiBpbnB1dCBzcGlrZVx1MDAyNy5mb3JtYXQocm1bMjBdKSlcblxudmlzdWFsaXplX3Jlc2V0X2dhdGUoKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTm8gVW5pdmVyc2FsIFdpbm5lcjogR1JVIHZzIExTVE0iLCJjb250ZW50IjoiRW1waXJpY2FsIGNvbXBhcmlzb25zIChDaHVuZyBldCBhbC4gMjAxNCwgR3JlZmYgZXQgYWwuIDIwMTcpIHNob3cgbmVpdGhlciBHUlUgbm9yIExTVE0gZG9taW5hdGVzIGNvbnNpc3RlbnRseS4gR1JVIHRlbmRzIHRvIHdpbiBvbiBzaG9ydGVyIHNlcXVlbmNlcyBhbmQgc21hbGxlciBkYXRhc2V0cyB3aGVyZSBpdHMgbG93ZXIgcGFyYW1ldGVyIGNvdW50IGFjdHMgYXMgcmVndWxhcml6YXRpb24uIExTVE0gdGVuZHMgdG8gd2luIG9uIHRhc2tzIHJlcXVpcmluZyBmaW5lLWdyYWluZWQgY29udHJvbCBvdmVyIHdoYXQgdG8gZm9yZ2V0IHZzIHdoYXQgdG8gd3JpdGUg4oCUIHN1Y2ggYXMgbGFuZ3VhZ2UgbW9kZWxpbmcgd2l0aCBsb25nLXJhbmdlIGRlcGVuZGVuY2llcy4gV2hlbiBpbiBkb3VidCwgdHJ5IEdSVSBmaXJzdCAoZmFzdGVyIHRvIHRyYWluKSBhbmQgc3dpdGNoIHRvIExTVE0gaWYgcGVyZm9ybWFuY2UgaXMgaW5zdWZmaWNpZW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoZW4gdG8gQ2hvb3NlIEdSVSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR1JVIGlzIHByZWZlcmFibGUgd2hlbiB0cmFpbmluZyBzcGVlZCBtYXR0ZXJzIG1vcmUgdGhhbiBzcXVlZXppbmcgdGhlIGxhc3QgZnJhY3Rpb24gb2YgYWNjdXJhY3kuIEl0cyAyNSUgcGFyYW1ldGVyIHJlZHVjdGlvbiBhbmQgc2ltcGxlciBmb3J3YXJkIHBhc3MgbWFrZSBpdCBhdHRyYWN0aXZlIGZvciBtb2JpbGUgZGVwbG95bWVudCBhbmQgcmFwaWQgaXRlcmF0aW9uLiBPbiB0YXNrcyB3aGVyZSBzZXF1ZW5jZSBsZW5ndGggaXMgbW9kZXJhdGUgKFx1MDAzYyA1MCBzdGVwcykgYW5kIHRoZSBkYXRhc2V0IGlzIHNtYWxsIHRvIG1lZGl1bSwgR1JVXHUwMDI3cyBpbXBsaWNpdCByZWd1bGFyaXphdGlvbiBmcm9tIGZld2VyIHBhcmFtZXRlcnMgb2Z0ZW4gb3V0cGVyZm9ybXMgTFNUTS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNob3J0ZXIgc2VxdWVuY2VzIChcdTAwM2MgNTAgc3RlcHMpOiBHUlUgaXMgY29tcGV0aXRpdmUgd2l0aCBMU1RNIGFuZCB0cmFpbnMgZmFzdGVyLiIsIlNtYWxsIGRhdGFzZXRzOiBmZXdlciBwYXJhbWV0ZXJzIGluIEdSVSByZWR1Y2Ugb3ZlcmZpdHRpbmcgcmlzay4iLCJTcGVlZC1jb25zdHJhaW5lZCBkZXBsb3ltZW50OiBHUlUgaGFzIGxvd2VyIEZMT1BzIHBlciBzdGVwLCBiZXR0ZXIgZm9yIGVkZ2UgaW5mZXJlbmNlLiIsIldoZW4gaW50ZXJwcmV0YWJpbGl0eSBtYXR0ZXJzOiAyIGdhdGVzIGFyZSBlYXNpZXIgdG8gYW5hbHl6ZSB0aGFuIDMgKyBjZWxsIHN0YXRlLiIsIlVzZSBMU1RNIHdoZW46IHNlcXVlbmNlcyBcdTAwM2UgMTAwIHN0ZXBzLCBmaW5lLWdyYWluZWQgZ2F0aW5nIGlzIG5lZWRlZCwgb3IgZW1waXJpY2FsbHkgTFNUTSB3aW5zLiIsIlVzZSBtaW5HUlUgd2hlbjogdmVyeSBsb25nIHNlcXVlbmNlcyBhbmQgdHJhaW5pbmcgdGltZSBpcyB0aGUgYm90dGxlbmVjayDigJQgcGFyYWxsZWwgc2NhbiBlbmFibGVzIGJhdGNoIHRyYWluaW5nLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBHUlUgYXJjaGl0ZWN0dXJlIGRlbW9uc3RyYXRlcyB0aGF0IG11Y2ggb2YgTFNUTVx1MDAyN3MgY2FwYWJpbGl0eSBjb21lcyBmcm9tIHRoZSBnYXRpbmcgbWVjaGFuaXNtIGl0c2VsZiByYXRoZXIgdGhhbiB0aGUgc3BlY2lmaWMgdGhyZWUtZ2F0ZSBwbHVzIGNlbGwtc3RhdGUgZGVzaWduLiBUaGUgZW1waXJpY2FsIGZpbmRpbmcgdGhhdCBHUlUgYW5kIExTVE0gcGVyZm9ybSBzaW1pbGFybHkgb24gbWFueSB0YXNrcyBzdWdnZXN0cyB0aGF0IHRoZSBhZGRpdGl2ZSB1cGRhdGUgc3RydWN0dXJlIOKAlCBub3QgdGhlIHByZWNpc2UgZ2F0ZSBjb3VudCDigJQgaXMgdGhlIGVzc2VudGlhbCBpbmdyZWRpZW50IGZvciBsZWFybmluZyBsb25nLXJhbmdlIGRlcGVuZGVuY2llcy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# GRU — Reset and Update Gates

GRU (Gated Recurrent Unit, Cho et al. 2014) simplifies the LSTM architecture from three gates and a separate cell state to two gates with a single hidden state. Despite this simplification, GRU often matches LSTM performance on many sequence tasks while training roughly 25% faster due to fewer parameters. Understanding when GRU is preferable — and how its two gates cover the same conceptual ground as LSTM's three — is essential for choosing the right architecture.

## GRU Architecture — Two Gates, No Cell State

GRU computes: update gate zt = σ(Wz[ht-1, xt]); reset gate rt = σ(Wr[ht-1, xt]); candidate h̃t = tanh(Wh[rt ⊙ ht-1, xt]); new hidden ht = zt ⊙ ht-1 + (1-zt) ⊙ h̃t. The update gate zt plays the combined role of LSTM's forget and input gates: zt ≈ 1 means keep the old hidden state (equivalent to ft ≈ 1 and it ≈ 0 in LSTM); zt ≈ 0 means fully replace with the candidate. The reset gate rt controls how much of the past hidden state enters the candidate computation.

```python
import numpy as np

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -10, 10)))

class GRUCell:
    """Minimal GRU cell: update gate, reset gate, candidate, interpolation."""
    def __init__(self, input_size, hidden_size, seed=0):
        rng = np.random.default_rng(seed)
        s = np.sqrt(1.0 / hidden_size)
        d = input_size + hidden_size
        self.Wz = rng.normal(0, s, (hidden_size, d));  self.bz = np.zeros(hidden_size)
        self.Wr = rng.normal(0, s, (hidden_size, d));  self.br = np.zeros(hidden_size)
        self.Wh = rng.normal(0, s, (hidden_size, d));  self.bh = np.zeros(hidden_size)

    def forward(self, x, h):
        xh = np.concatenate([x, h])
        z = sigmoid(self.Wz @ xh + self.bz)           # update gate
        r = sigmoid(self.Wr @ xh + self.br)            # reset gate
        xrh = np.concatenate([x, r * h])
        h_cand = np.tanh(self.Wh @ xrh + self.bh)    # candidate
        h_new  = z * h + (1 - z) * h_cand             # interpolate
        return h_new, dict(z=z, r=r)

np.random.seed(42)
gru = GRUCell(input_size=4, hidden_size=8)
h = np.zeros(8)
print('GRU from scratch — gate activations per step:')
print('{:>4} {:>10} {:>10} {:>10}'.format('t', 'h_norm', 'z_mean', 'r_mean'))
for t in range(5):
    x = np.random.randn(4)
    h, g = gru.forward(x, h)
    print('{:>4} {:>10.4f} {:>10.4f} {:>10.4f}'.format(t, np.linalg.norm(h), g['z'].mean(), g['r'].mean()))
```

## Update Gate — Interpolation Between Old and New

The update gate zt ∈ (0,1)ᴴ acts as a learned interpolation coefficient between the previous hidden state ht-1 and the new candidate h̃t: ht = zt ⊙ ht-1 + (1-zt) ⊙ h̃t. When zt ≈ 1, the hidden state is preserved unchanged — the unit remembers. When zt ≈ 0, the hidden state is fully replaced by the candidate — the unit updates. This single gate handles what LSTM needs two gates (forget + input) to achieve, at the cost of losing the ability to independently control how much to forget vs how much to write.

## Reset Gate — Controlling Candidate Computation

The reset gate rt ∈ (0,1)ᴴ controls how much of the previous hidden state enters the candidate: h̃t = tanh(Wh[rt ⊙ ht-1, xt]). When rt ≈ 1, the candidate sees the full past context — the cell uses its history. When rt ≈ 0, the candidate computation ignores ht-1 — the unit behaves as if it has no memory and generates a candidate purely from the current input. This allows GRU to reset its context when the input distribution changes abruptly.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import time

def benchmark_rnn(cell_type='gru', I=16, H=64, T=30, C=5, N=512, epochs=20):
    torch.manual_seed(42)
    rnn = (nn.GRU if cell_type == 'gru' else nn.LSTM)(I, H, batch_first=True)
    fc  = nn.Linear(H, C)
    opt = optim.Adam(list(rnn.parameters()) + list(fc.parameters()), lr=1e-3)
    x = torch.randn(N, T, I)
    y = torch.randint(0, C, (N,))
    t0 = time.perf_counter()
    for _ in range(epochs):
        out, state = rnn(x)
        h = state[0].squeeze(0) if cell_type == 'lstm' else state.squeeze(0)
        loss = nn.CrossEntropyLoss()(fc(h), y)
        opt.zero_grad(); loss.backward(); opt.step()
    elapsed = time.perf_counter() - t0
    with torch.no_grad():
        out, state = rnn(x)
        h = state[0].squeeze(0) if cell_type == 'lstm' else state.squeeze(0)
        acc = (fc(h).argmax(1) == y).float().mean().item()
    n_params = sum(p.numel() for p in list(rnn.parameters()) + list(fc.parameters()))
    return acc, elapsed, n_params

print('GRU vs LSTM on sequence classification (seq_len=30, 5 classes):')
for name in ['gru', 'lstm']:
    acc, t, n = benchmark_rnn(name)
    print('  {}: acc={:.3f}  time={:.2f}s  params={:,}'.format(name.upper(), acc, t, n))
```

## Parameter Count and Computational Cost

GRU has 3 gate weight matrices (Wz, Wr, Wh) each of shape H×(H+I), giving 3·H·(H+I) + 3H parameters. LSTM has 4 gate matrices (Wf, Wi, Wg, Wo), giving 4·H·(H+I) + 4H parameters. For H=256, I=128, GRU has ~294K parameters vs LSTM ~392K — a 25% reduction. GRU also performs fewer matrix multiplications per step and has no cell state to maintain, making each forward step roughly 25% faster in practice.

| Model | Gates | Cell State | Params (H=256, I=128) | Parallelizable | Typical Perf |
| --- | --- | --- | --- | --- | --- |
| Vanilla RNN | 0 (direct Whh) | No | ~98K | No (sequential) | Baseline — fails on long sequences |
| GRU | 2 (update, reset) | No | ~294K | No (sequential) | On par with LSTM on short-mid tasks |
| LSTM | 3 (forget, input, output) | Yes (Ct) | ~393K | No (sequential) | Best on long sequences with fine control |
| minGRU (2024) | 1 (update, no reset) | No | ~131K | Yes (parallel scan) | Competitive on many tasks, much faster training |

## minGRU — Parallel-Trainable Simplified GRU

minGRU (Feng et al. 2024) removes the reset gate and the tanh nonlinearity from the candidate, and makes the candidate depend only on the current input xt — not on ht-1. This breaks the sequential dependency in the forward pass, enabling fully parallel training via an associative scan (similar to how prefix-sum can be parallelized). The result is a model that trains much faster than standard GRU on long sequences while remaining competitive on many benchmarks.

```python
import torch
import torch.nn as nn

class MinGRU(nn.Module):
    """minGRU (Feng et al. 2024): no reset gate, no tanh, input-only candidate.

    Removes sequential dependency -> trainable in parallel via associative scan.
    Sequential loop shown here for clarity; real impl uses log-space parallel scan.
    """
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.gate      = nn.Linear(input_size, hidden_size)   # update gate
        self.candidate = nn.Linear(input_size, hidden_size)   # candidate (no tanh, no h)
        self.hidden_size = hidden_size

    def forward(self, x):
        """x: (B, T, I). Returns (B, T, H) output sequence."""
        z      = torch.sigmoid(self.gate(x))      # (B, T, H) update gates
        h_tild = self.candidate(x)                # (B, T, H) candidates
        B = x.size(0)
        h = torch.zeros(B, self.hidden_size)
        outputs = []
        for t in range(x.size(1)):
            h = (1 - z[:, t]) * h + z[:, t] * h_tild[:, t]
            outputs.append(h)
        return torch.stack(outputs, dim=1)

torch.manual_seed(0)
model = MinGRU(input_size=8, hidden_size=16)
x = torch.randn(4, 20, 8)
out = model(x)
full_gru_params = 3 * (8 * 16 + 16 * 16 + 16)
print('minGRU output: {}'.format(tuple(out.shape)))
print('minGRU params: {:,}  vs full GRU params: {:,}'.format(
    sum(p.numel() for p in model.parameters()), full_gru_params))
```

## Reset Gate Visualization

The reset gate tends to fire (approach 0) when the input distribution changes abruptly, allowing the candidate to be computed from scratch without contamination from stale hidden state. On stationary input, the reset gate stays near 1, preserving context. This behavior is learned automatically from data — the network discovers that resetting context helps recover from distribution shifts.

```python
import torch
import torch.nn as nn
import numpy as np

def visualize_reset_gate(seq_len=40, input_size=4, hidden_size=8, seed=2):
    """Show reset gate activations across a two-phase sequence."""
    torch.manual_seed(seed)
    cell = nn.GRUCell(input_size, hidden_size)
    x = torch.cat([
        torch.randn(seq_len // 2, input_size) * 0.2,   # smooth phase
        torch.randn(seq_len // 2, input_size) * 3.0    # high-variance phase
    ], dim=0)
    h = torch.zeros(1, hidden_size)
    reset_means = []
    with torch.no_grad():
        for t in range(seq_len):
            pre = (x[t:t+1] @ cell.weight_ih.T + h @ cell.weight_hh.T
                   + cell.bias_ih + cell.bias_hh)
            r_gate = torch.sigmoid(pre[:, hidden_size:2*hidden_size])
            reset_means.append(r_gate.mean().item())
            h = cell(x[t:t+1], h)
    rm = np.array(reset_means)
    print('Reset gate mean (0=ignore past, 1=use past):')
    print('  Smooth t=00-19: {:.3f}'.format(rm[:20].mean()))
    print('  Noisy  t=20-39: {:.3f}'.format(rm[20:].mean()))
    print('  Transition t=20: {:.3f}  <- resets on sudden input spike'.format(rm[20]))

visualize_reset_gate()
```

> **No Universal Winner: GRU vs LSTM**: Empirical comparisons (Chung et al. 2014, Greff et al. 2017) show neither GRU nor LSTM dominates consistently. GRU tends to win on shorter sequences and smaller datasets where its lower parameter count acts as regularization. LSTM tends to win on tasks requiring fine-grained control over what to forget vs what to write — such as language modeling with long-range dependencies. When in doubt, try GRU first (faster to train) and switch to LSTM if performance is insufficient.

## When to Choose GRU

GRU is preferable when training speed matters more than squeezing the last fraction of accuracy. Its 25% parameter reduction and simpler forward pass make it attractive for mobile deployment and rapid iteration. On tasks where sequence length is moderate (< 50 steps) and the dataset is small to medium, GRU's implicit regularization from fewer parameters often outperforms LSTM.

- Shorter sequences (< 50 steps): GRU is competitive with LSTM and trains faster.
- Small datasets: fewer parameters in GRU reduce overfitting risk.
- Speed-constrained deployment: GRU has lower FLOPs per step, better for edge inference.
- When interpretability matters: 2 gates are easier to analyze than 3 + cell state.
- Use LSTM when: sequences > 100 steps, fine-grained gating is needed, or empirically LSTM wins.
- Use minGRU when: very long sequences and training time is the bottleneck — parallel scan enables batch training.

The GRU architecture demonstrates that much of LSTM's capability comes from the gating mechanism itself rather than the specific three-gate plus cell-state design. The empirical finding that GRU and LSTM perform similarly on many tasks suggests that the additive update structure — not the precise gate count — is the essential ingredient for learning long-range dependencies.

---

