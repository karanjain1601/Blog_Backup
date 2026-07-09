---
title: "N-BEATS — Basis Expansion for Interpretable Forecasting"
slug: "n-beats"
description: "Understand N-BEATS architecture: doubly residual stacking of blocks with backcast and forecast outputs, polynomial trend basis, Fourier seasonality basis, generic learned basis, and N-HiTS extension for longer horizons."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTi1CRUFUUyAoTmV1cmFsIEJhc2lzIEV4cGFuc2lvbiBBbmFseXNpcyBmb3IgSW50ZXJwcmV0YWJsZSBUaW1lIFNlcmllcykgaXMgYSBwdXJlbHkgZGVlcC1sZWFybmluZyBmb3JlY2FzdGluZyBhcmNoaXRlY3R1cmUgdGhhdCByZXF1aXJlcyBubyB0aW1lLXNlcmllcy1zcGVjaWZpYyBpbmR1Y3RpdmUgYmlhcy4gSXQgbGVhcm5zIHRvIGRlY29tcG9zZSBhIHRpbWUgc2VyaWVzIGludG8gaW50ZXJwcmV0YWJsZSBjb21wb25lbnRzIHRocm91Z2ggYSBkb3VibHkgcmVzaWR1YWwgc3RhY2sgb2YgZmVlZC1mb3J3YXJkIGJsb2Nrcy4gRWFjaCBibG9jayBwcm9kdWNlcyBhIGJhY2tjYXN0IChyZWNvbnN0cnVjdGlvbiBvZiBpdHMgaW5wdXQgd2luZG93KSBhbmQgYSBmb3JlY2FzdCAocHJlZGljdGlvbiBvZiBmdXR1cmUgdmFsdWVzKS4gUmVsZWFzZWQgaW4gMjAyMCwgTi1CRUFUUyBhY2hpZXZlZCBzdGF0ZS1vZi10aGUtYXJ0IG9uIE00IGFuZCBNMyBjb21wZXRpdGlvbnMgcmV0cm9zcGVjdGl2ZWx5IGFuZCByZW1haW5zIGEgc3Ryb25nIGJhc2VsaW5lIGZvciB1bml2YXJpYXRlIGZvcmVjYXN0aW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFyY2hpdGVjdHVyZSBPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW4gTi1CRUFUUyBtb2RlbCBpcyBvcmdhbmlzZWQgaW50byBzdGFja3MsIGVhY2ggY29udGFpbmluZyBtdWx0aXBsZSBibG9ja3MuIEVhY2ggYmxvY2sgcmVjZWl2ZXMgdGhlIHJlc2lkdWFsIHNpZ25hbCAob3JpZ2luYWwgaW5wdXQgbWludXMgdGhlIHN1bSBvZiBhbGwgcHJldmlvdXMgYmFja2Nhc3RzKSDigJQgdGhlIGRvdWJseSByZXNpZHVhbCBwcmluY2lwbGUuIFRoZSBibG9jayBwcm9kdWNlcyB0d28gb3V0cHV0czogYSBiYWNrY2FzdCBleHBsYWluaW5nIHBhcnQgb2YgaXRzIGlucHV0LCBhbmQgYSBmb3JlY2FzdCBjb250cmlidXRpbmcgdG8gdGhlIGZpbmFsIHByZWRpY3Rpb24uIEZpbmFsIGZvcmVjYXN0ID0gc3VtIG9mIGFsbCBibG9ja3PigJkgZm9yZWNhc3Qgb3V0cHV0cyBhY3Jvc3MgYWxsIHN0YWNrcy4gVGhpcyBkZXNpZ24gZW5hYmxlcyB2ZXJ5IGRlZXAgbmV0d29ya3Mgd2l0aG91dCB2YW5pc2hpbmcgZ3JhZGllbnRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBOLUJFQVRTIEJsb2NrIOKAlCBCYWNrY2FzdCBhbmQgRm9yZWNhc3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVhY2ggYmxvY2sgY29udGFpbnMgZm91ciBmdWxseS1jb25uZWN0ZWQgbGF5ZXJzIHdpdGggUmVMVSBhY3RpdmF0aW9ucywgZm9sbG93ZWQgYnkgdHdvIGxpbmVhciBoZWFkcyBwcm9kdWNpbmcgYmFzaXMgZXhwYW5zaW9uIGNvZWZmaWNpZW50cyDOuF9iIChiYWNrY2FzdCkgYW5kIM64X2YgKGZvcmVjYXN0KS4gVGhlIGNvZWZmaWNpZW50cyBhcmUgbXVsdGlwbGllZCBieSBmaXhlZCAodHJlbmQvc2Vhc29uYWxpdHkpIG9yIGxlYXJuZWQgKGdlbmVyaWMpIGJhc2lzIHZlY3RvcnMgZ19iIGFuZCBnX2YuIEZvciBnZW5lcmljIE4tQkVBVFMsIGdfYiBhbmQgZ19mIGFyZSBsZWFybmVkIGxpbmVhciBwcm9qZWN0aW9ucy4gRm9yIGludGVycHJldGFibGUgTi1CRUFUUywgZ19iIHVzZXMgYSBwb2x5bm9taWFsIGJhc2lzIGFuZCBnX2YgdXNlcyBhIEZvdXJpZXIgYmFzaXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE5CRUFUU0Jsb2NrKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU2luZ2xlIE4tQkVBVFMgYmxvY2s6IEZDIHN0YWNrIC1cdTAwM2UgYmFzaXMgY29lZmZpY2llbnRzIC1cdTAwM2UgYmFja2Nhc3QgKyBmb3JlY2FzdC5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfc2l6ZSwgdGhldGFfc2l6ZSwgZm9yZWNhc3Rfc2l6ZSwgaGlkZGVuPTI1NiwgbnVtX2xheWVycz00KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGxheWVycywgaW5fZGltID0gW10sIGlucHV0X3NpemVcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2UobnVtX2xheWVycyk6XG4gICAgICAgICAgICBsYXllcnMgKz0gW25uLkxpbmVhcihpbl9kaW0sIGhpZGRlbiksIG5uLlJlTFUoKV1cbiAgICAgICAgICAgIGluX2RpbSA9IGhpZGRlblxuICAgICAgICBzZWxmLmZjX3N0YWNrID0gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuICAgICAgICBzZWxmLnRoZXRhX2IgPSBubi5MaW5lYXIoaGlkZGVuLCB0aGV0YV9zaXplKSAgICMgYmFja2Nhc3QgYmFzaXMgY29lZmZpY2llbnRzXG4gICAgICAgIHNlbGYudGhldGFfZiA9IG5uLkxpbmVhcihoaWRkZW4sIHRoZXRhX3NpemUpICAgIyBmb3JlY2FzdCBiYXNpcyBjb2VmZmljaWVudHNcbiAgICAgICAgc2VsZi5nX2IgPSBubi5MaW5lYXIodGhldGFfc2l6ZSwgaW5wdXRfc2l6ZSwgYmlhcz1GYWxzZSkgICAgIyBnZW5lcmljIGJhY2tjYXN0IGJhc2lzXG4gICAgICAgIHNlbGYuZ19mID0gbm4uTGluZWFyKHRoZXRhX3NpemUsIGZvcmVjYXN0X3NpemUsIGJpYXM9RmFsc2UpICMgZ2VuZXJpYyBmb3JlY2FzdCBiYXNpc1xuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGggPSBzZWxmLmZjX3N0YWNrKHgpXG4gICAgICAgIGJhY2tjYXN0ID0gc2VsZi5nX2Ioc2VsZi50aGV0YV9iKGgpKVxuICAgICAgICBmb3JlY2FzdCA9IHNlbGYuZ19mKHNlbGYudGhldGFfZihoKSlcbiAgICAgICAgcmV0dXJuIGJhY2tjYXN0LCBmb3JlY2FzdFxuXG4jIFZlcmlmeSBzaGFwZXNcbmJsb2NrID0gTkJFQVRTQmxvY2soaW5wdXRfc2l6ZT0zMCwgdGhldGFfc2l6ZT0zMiwgZm9yZWNhc3Rfc2l6ZT0xMClcbnggPSB0b3JjaC5yYW5kbig4LCAzMClcbmJjLCBmYyA9IGJsb2NrKHgpXG5wcmludChmXHUwMDI3QmFja2Nhc3Q6IHtiYy5zaGFwZX0sIEZvcmVjYXN0OiB7ZmMuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1BhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gYmxvY2sucGFyYW1ldGVycygpKTosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEb3VibHkgUmVzaWR1YWwgU3RhY2tpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIGRvdWJseSByZXNpZHVhbCBzdGFja2luZyBlYWNoIGJsb2NrIHJlY2VpdmVzIG9ubHkgdGhlIHVuZXhwbGFpbmVkIHJlc2lkdWFsIChpbnB1dCBtaW51cyBhbGwgcHJldmlvdXMgYmFja2Nhc3RzKSByYXRoZXIgdGhhbiB0aGUgcmF3IGlucHV0LiBTaW11bHRhbmVvdXNseSwgZm9yZWNhc3RzIGZyb20gYWxsIGJsb2NrcyBhY2N1bXVsYXRlIGFkZGl0aXZlbHkuIFRoaXMgaXMgZG91Ymx5IHJlc2lkdWFsOiByZXNpZHVhbCBvbiB0aGUgaW5wdXQgc2lkZSAoc3VidHJhY3RpbmcgYmFja2Nhc3RzKSBhbmQgYWRkaXRpdmUgb24gdGhlIG91dHB1dCBzaWRlIChzdW1taW5nIGZvcmVjYXN0cykuIEl0IGFsbG93cyBlYWNoIGJsb2NrIHRvIHNwZWNpYWxpc2Ugb24gZXhwbGFpbmluZyBhIGRpZmZlcmVudCBwb3J0aW9uIG9mIHRoZSBzaWduYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE5CRUFUU0Jsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX3N6LCBmY19zeiwgaGlkZGVuPTEyOCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmZjID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoaW5fc3osIGhpZGRlbiksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuKSwgbm4uUmVMVSgpKVxuICAgICAgICBzZWxmLmdfYiA9IG5uLkxpbmVhcihoaWRkZW4sIGluX3N6LCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmdfZiA9IG5uLkxpbmVhcihoaWRkZW4sIGZjX3N6LCBiaWFzPUZhbHNlKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBoID0gc2VsZi5mYyh4KVxuICAgICAgICByZXR1cm4gc2VsZi5nX2IoaCksIHNlbGYuZ19mKGgpXG5cbmRlZiBkb3VibHlfcmVzaWR1YWxfc3RhY2soYmxvY2tzLCB4LCBmY19zeik6XG4gICAgXCJcIlwiU3VidHJhY3QgYmFja2Nhc3RzIChyZXNpZHVhbCBpbnB1dCksIGFjY3VtdWxhdGUgZm9yZWNhc3RzLlwiXCJcIlxuICAgIHJlc2lkdWFsID0geC5jbG9uZSgpXG4gICAgZm9yZWNhc3QgPSB0b3JjaC56ZXJvcyh4LnNpemUoMCksIGZjX3N6KVxuICAgIGZvciBibGsgaW4gYmxvY2tzOlxuICAgICAgICBiYywgZmMgPSBibGsocmVzaWR1YWwpXG4gICAgICAgIHJlc2lkdWFsID0gcmVzaWR1YWwgLSBiYyAgICMgb25seSB1bmV4cGxhaW5lZCBzaWduYWwgcGFzc2VzIGZvcndhcmRcbiAgICAgICAgZm9yZWNhc3QgPSBmb3JlY2FzdCArIGZjICAgIyBlYWNoIGJsb2NrIGNvbnRyaWJ1dGVzIHRvIHRvdGFsIGZvcmVjYXN0XG4gICAgcmV0dXJuIHJlc2lkdWFsLCBmb3JlY2FzdFxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuSU4sIEhaID0gMzAsIDEwXG50cmVuZF9ibGtzID0gW05CRUFUU0Jsb2NrKElOLCBIWikgZm9yIF8gaW4gcmFuZ2UoMyldXG5zZWFzX2Jsa3MgID0gW05CRUFUU0Jsb2NrKElOLCBIWikgZm9yIF8gaW4gcmFuZ2UoMyldXG54ID0gdG9yY2gucmFuZG4oNCwgSU4pXG5yMSwgZmMxID0gZG91Ymx5X3Jlc2lkdWFsX3N0YWNrKHRyZW5kX2Jsa3MsIHgsIEhaKVxucjIsIGZjMiA9IGRvdWJseV9yZXNpZHVhbF9zdGFjayhzZWFzX2Jsa3MsIHIxLCBIWilcbnByaW50KGZcdTAwMjdJbnB1dCBub3JtOiAgICAgICAgICAge3gubm9ybSgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3QWZ0ZXIgdHJlbmQgcmVzaWR1YWw6IHtyMS5ub3JtKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdBZnRlciBzZWFzICByZXNpZHVhbDoge3IyLm5vcm0oKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1RvdGFsIGZvcmVjYXN0IHNoYXBlOiB7KGZjMSArIGZjMikuc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkludGVycHJldGFibGUgTi1CRUFUUyDigJQgVHJlbmQgYW5kIFNlYXNvbmFsaXR5IFN0YWNrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW50ZXJwcmV0YWJsZSBOLUJFQVRTIHVzZXMgZml4ZWQgYmFzaXMgZnVuY3Rpb25zOiBwb2x5bm9taWFsIGZvciB0aGUgdHJlbmQgc3RhY2sgYW5kIEZvdXJpZXIgZm9yIHRoZSBzZWFzb25hbGl0eSBzdGFjay4gVGhlIEZDIHN0YWNrIGxlYXJucyBjb2VmZmljaWVudCB2ZWN0b3JzIM64IHdoaWNoIGFyZSBtdWx0aXBsaWVkIGJ5IHRoZXNlIGZpeGVkIG1hdHJpY2VzLiBUaGlzIGZvcmNlcyB0cmVuZCBibG9ja3MgdG8gbW9kZWwgb25seSBwb2x5bm9taWFsIHRyZW5kcyBhbmQgc2Vhc29uYWxpdHkgYmxvY2tzIHRvIG1vZGVsIG9ubHkgcGVyaW9kaWMgcGF0dGVybnMsIGVuYWJsaW5nIGRpcmVjdCBkZWNvbXBvc2l0aW9uIG9mIHRoZSBmaW5hbCBmb3JlY2FzdCBpbnRvIGludGVycHJldGFibGUgY29tcG9uZW50cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHBhbmRhcyBhcyBwZFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIG5ldXJhbGZvcmVjYXN0IGltcG9ydCBOZXVyYWxGb3JlY2FzdFxuZnJvbSBuZXVyYWxmb3JlY2FzdC5tb2RlbHMgaW1wb3J0IE5CRUFUU1xuZnJvbSBuZXVyYWxmb3JlY2FzdC5sb3NzZXMucHl0b3JjaCBpbXBvcnQgTUFFXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuaG9yaXpvbiA9IDEyXG5kYXRlcyA9IHBkLmRhdGVfcmFuZ2UoXHUwMDI3MjAxNS0wMVx1MDAyNywgcGVyaW9kcz05NiwgZnJlcT1cdTAwMjdNRVx1MDAyNylcbmRmID0gcGQuY29uY2F0KFtcbiAgICBwZC5EYXRhRnJhbWUoe1xuICAgICAgICBcdTAwMjd1bmlxdWVfaWRcdTAwMjc6IGZcdTAwMjdzZXJpZXNfe2l9XHUwMDI3LFxuICAgICAgICBcdTAwMjdkc1x1MDAyNzogZGF0ZXMsXG4gICAgICAgIFx1MDAyN3lcdTAwMjc6ICg1MCAqIG5wLnNpbihucC5saW5zcGFjZSgwLCA2Km5wLnBpLCA5NikpXG4gICAgICAgICAgICAgICsgbnAubGluc3BhY2UoMTAwLCAyMDAsIDk2KVxuICAgICAgICAgICAgICArIDUgKiBucC5yYW5kb20ucmFuZG4oOTYpKVxuICAgIH0pIGZvciBpIGluIHJhbmdlKDMpXG5dLCBpZ25vcmVfaW5kZXg9VHJ1ZSlcblxubW9kZWwgPSBOQkVBVFMoXG4gICAgaD1ob3Jpem9uLCBpbnB1dF9zaXplPTIqaG9yaXpvbixcbiAgICBzdGFja190eXBlcz1bXHUwMDI3dHJlbmRcdTAwMjcsIFx1MDAyN3NlYXNvbmFsaXR5XHUwMDI3XSwgICMgaW50ZXJwcmV0YWJsZSBOLUJFQVRTIHZhcmlhbnRcbiAgICBuX2Jsb2Nrcz1bMywgM10sXG4gICAgbWxwX3VuaXRzPVtbMjU2LCAyNTZdLCBbMjU2LCAyNTZdXSxcbiAgICBtYXhfc3RlcHM9MjAwLCBsb3NzPU1BRSgpLFxuKVxubmYgPSBOZXVyYWxGb3JlY2FzdChtb2RlbHM9W21vZGVsXSwgZnJlcT1cdTAwMjdNRVx1MDAyNylcbm5mLmZpdChkZj1kZilcbnByZWRzID0gbmYucHJlZGljdCgpXG5wcmludChwcmVkcy5oZWFkKCkpXG5wcmludChmXHUwMDI3Q29sdW1uczoge2xpc3QocHJlZHMuY29sdW1ucyl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkludGVycHJldGluZyBUcmVuZCBhbmQgU2Vhc29uYWxpdHkgQmxvY2sgT3V0cHV0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRyZW5kIGJhc2lzIGlzIGEgcG9seW5vbWlhbCB1cCB0byBkZWdyZWUgcDogQl90cmVuZCA9IFsxLCB0LCB0wrIsIC4uLiwgdOG1ll0gd2l0aCB0IG5vcm1hbGlzZWQgdG8gWy0xLCAxXS4gVGhlIHNlYXNvbmFsaXR5IGJhc2lzIGlzIGEgRm91cmllciBleHBhbnNpb246IEJfc2VhcyA9IFtzaW4odCksIGNvcyh0KSwgc2luKDJ0KSwgY29zKDJ0KSwgLi4uXSBhdCBtdWx0aXBsZSBoYXJtb25pY3MuIExlYXJuZWQgY29lZmZpY2llbnRzIM64IGZyb20gdGhlIEZDIHN0YWNrIGFjdCBhcyBhbXBsaXR1ZGVzLiBFeHRyYWN0aW5nIM64IMOXIEIgZ2l2ZXMgdGhlIGludGVycHJldGFibGUgdHJlbmQgYW5kIHNlYXNvbmFsIGZvcmVjYXN0IGNvbXBvbmVudHMgc2VwYXJhdGVseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBwb2x5bm9taWFsX2Jhc2lzKGJhY2tjYXN0X2xlbiwgZm9yZWNhc3RfbGVuLCBkZWdyZWU9Myk6XG4gICAgXCJcIlwiTi1CRUFUUyBwb2x5bm9taWFsIHRyZW5kIGJhc2lzOiBbMSwgdCwgdF4yLCAuLi4sIHReZGVncmVlXS5cIlwiXCJcbiAgICB0ID0gbnAubGluc3BhY2UoLTEsIDEsIGJhY2tjYXN0X2xlbiArIGZvcmVjYXN0X2xlbilcbiAgICBiYXNpcyA9IG5wLnN0YWNrKFt0KipkIGZvciBkIGluIHJhbmdlKGRlZ3JlZSArIDEpXSlcbiAgICByZXR1cm4gYmFzaXNbOiwgOmJhY2tjYXN0X2xlbl0sIGJhc2lzWzosIGJhY2tjYXN0X2xlbjpdXG5cbmRlZiBmb3VyaWVyX2Jhc2lzKGJhY2tjYXN0X2xlbiwgZm9yZWNhc3RfbGVuLCBoYXJtb25pY3M9NCk6XG4gICAgXCJcIlwiTi1CRUFUUyBGb3VyaWVyIHNlYXNvbmFsaXR5IGJhc2lzOiBzaW4gKyBjb3MgYXQgbXVsdGlwbGUgZnJlcXVlbmNpZXMuXCJcIlwiXG4gICAgdCA9IG5wLmxpbnNwYWNlKDAsIDIqbnAucGksIGJhY2tjYXN0X2xlbiArIGZvcmVjYXN0X2xlbilcbiAgICBrID0gbnAuYXJhbmdlKDEsIGhhcm1vbmljcyArIDEpXG4gICAgc2luX2IgPSBucC5zaW4obnAub3V0ZXIoaywgdFs6YmFja2Nhc3RfbGVuXSkpXG4gICAgY29zX2IgPSBucC5jb3MobnAub3V0ZXIoaywgdFs6YmFja2Nhc3RfbGVuXSkpXG4gICAgc2luX2YgPSBucC5zaW4obnAub3V0ZXIoaywgdFtiYWNrY2FzdF9sZW46XSkpXG4gICAgY29zX2YgPSBucC5jb3MobnAub3V0ZXIoaywgdFtiYWNrY2FzdF9sZW46XSkpXG4gICAgcmV0dXJuIG5wLnZzdGFjayhbc2luX2IsIGNvc19iXSksIG5wLnZzdGFjayhbc2luX2YsIGNvc19mXSlcblxubnAucmFuZG9tLnNlZWQoMSlcbkJBQ0ssIEZXRCA9IDI0LCAxMlxudHJlbmRfYmMsIHRyZW5kX2ZjID0gcG9seW5vbWlhbF9iYXNpcyhCQUNLLCBGV0QsIGRlZ3JlZT0zKVxuc2Vhc19iYywgIHNlYXNfZmMgID0gZm91cmllcl9iYXNpcyhCQUNLLCBGV0QsIGhhcm1vbmljcz00KVxuXG50aGV0YV90ID0gbnAuYXJyYXkoWzEwMC4sIDIwLiwgLTMuLCAwLjVdKSAgIyBsZWFybmVkIHRyZW5kIGNvZWZmaWNpZW50c1xudGhldGFfcyA9IG5wLnJhbmRvbS5yYW5kbig4KSAgICAgICAgICAgICAgICMgbGVhcm5lZCBzZWFzb25hbGl0eSBjb2VmZmljaWVudHNcbnRyZW5kX2NvbXBvbmVudCA9IHRoZXRhX3QgQCB0cmVuZF9mY1xuc2Vhc19jb21wb25lbnQgID0gdGhldGFfcyBAIHNlYXNfZmNcbnByaW50KGZcdTAwMjdUcmVuZCBiYXNpcyAoZm9yZWNhc3QpOiB7dHJlbmRfZmMuc2hhcGV9ICAtLSBkZWdyZWUtMyBwb2x5bm9taWFsXHUwMDI3KVxucHJpbnQoZlx1MDAyN1NlYXMgIGJhc2lzIChmb3JlY2FzdCk6IHtzZWFzX2ZjLnNoYXBlfSAgLS0gNCBoYXJtb25pY3MgeCBzaW4rY29zXHUwMDI3KVxucHJpbnQoZlx1MDAyN1RyZW5kIGZvcmVjYXN0OiB7dHJlbmRfY29tcG9uZW50LnJvdW5kKDIpfVx1MDAyNylcbnByaW50KGZcdTAwMjdDb21iaW5lZCBmaXJzdCA0OiB7KHRyZW5kX2NvbXBvbmVudCArIHNlYXNfY29tcG9uZW50KVs6NF0ucm91bmQoMyl9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJJbnRlcnByZXRhYmxlIHZzIEdlbmVyaWMgTi1CRUFUUyIsImNvbnRlbnQiOiJVc2UgaW50ZXJwcmV0YWJsZSBOLUJFQVRTICh0cmVuZCArIHNlYXNvbmFsaXR5IHN0YWNrcyB3aXRoIGZpeGVkIGJhc2VzKSB3aGVuIGV4cGxhaW5hYmlsaXR5IG1hdHRlcnMgb3Igd2hlbiBkb21haW4ga25vd2xlZGdlIGNvbmZpcm1zIHBvbHlub21pYWwgdHJlbmQgYW5kIEZvdXJpZXIgc2Vhc29uYWxpdHkuIFVzZSBnZW5lcmljIE4tQkVBVFMgKGFsbC1sZWFybmVkIGJhc2lzKSBmb3IgcmF3IGJlbmNobWFyayBwZXJmb3JtYW5jZSDigJQgaXQgaXMgdHlwaWNhbGx5IDHigJMyJSBtb3JlIGFjY3VyYXRlIG9uIE00IGJ1dCBwcm9kdWNlcyBubyBkZWNvbXBvc2l0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik4tQkVBVFMgdnMgTi1IaVRTIHZzIFRyYW5zZm9ybWVyIEZvcmVjYXN0ZXJzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiQXJjaGl0ZWN0dXJlIiwiSW50ZXJwcmV0YWJsZSIsIkNvdmFyaWF0ZXMiLCJMb25nIEhvcml6b24iLCJNNCBSYW5rIl0sInJvd3MiOltbIk4tQkVBVFMgR2VuZXJpYyIsIkRlZXAgRkMgKyBsZWFybmVkIGJhc2lzIiwiTm8iLCJObyAoTi1CRUFUU3ggbmVlZGVkKSIsIk1vZGVyYXRlIiwiMXN0ICgyMDIwKSJdLFsiTi1CRUFUUyBJbnRlcnByZXRhYmxlIiwiRkMgKyBwb2x5ICsgRm91cmllciBiYXNpcyIsIlllcyIsIk5vIiwiTW9kZXJhdGUiLCIxc3QgKHRpZWQpIl0sWyJOLUhpVFMiLCJIaWVyYXJjaGljYWwgaW50ZXJwb2xhdGlvbiwgbXVsdGktcmF0ZSBwb29saW5nIiwiUGFydGlhbCIsIlllcyIsIlN0cm9uZyIsIlNPVEEgbG9uZy1ob3Jpem9uIl0sWyJURlQiLCJNdWx0aS1oZWFkIGF0dGVudGlvbiArIExTVE0iLCJWaWEgYXR0ZW50aW9uIiwiWWVzIChyaWNoKSIsIkdvb2QiLCIybmTigJMzcmQiXSxbIlBhdGNoVFNUIiwiUGF0Y2gtYmFzZWQgY2hhbm5lbC1pbmRlcGVuZGVudCBUcmFuc2Zvcm1lciIsIk5vIiwiTGltaXRlZCIsIlN0cm9uZyIsIkNvbXBldGl0aXZlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOLUJFQVRTeCBhbmQgTi1IaVRTIEV4dGVuc2lvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik4tQkVBVFN4IGV4dGVuZHMgTi1CRUFUUyB0byBhY2NlcHQgZXh0ZXJuYWwgY292YXJpYXRlcyBieSBjb25jYXRlbmF0aW5nIHRoZW0gdG8gdGhlIGJsb2NrIGlucHV0LiBOLUhpVFMgaW1wcm92ZXMgbG9uZy1ob3Jpem9uIGZvcmVjYXN0aW5nIGJ5IGhpZXJhcmNoaWNhbCBpbnRlcnBvbGF0aW9uOiBlYWNoIHN0YWNrIG9wZXJhdGVzIGF0IGEgZGlmZmVyZW50IHRlbXBvcmFsIHJlc29sdXRpb24gKGRvd25zYW1wbGluZyByYXRpb3MgWzEsIDIsIDRdKSBhbmQgb3V0cHV0cyBhcmUgdXBzYW1wbGVkIGFuZCBzdW1tZWQuIFRoaXMgZHJhbWF0aWNhbGx5IHJlZHVjZXMgdGhlIGVmZmVjdGl2ZSBzZXF1ZW5jZSBsZW5ndGggZm9yIGxvbmcgaG9yaXpvbnMgYW5kIGltcHJvdmVzIGFjY3VyYWN5IG9uIEVUVCBhbmQgRWxlY3RyaWNpdHkgZGF0YXNldHMgdmVyc3VzIHZhbmlsbGEgVHJhbnNmb3JtZXJzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTi1CRUFUUzogcHVyZWx5IHVuaXZhcmlhdGUsIG5vIGNvdmFyaWF0ZXMsIGludGVycHJldGFibGUgb3IgZ2VuZXJpYyBzdGFja3MuIiwiTi1CRUFUU3g6IGFkZHMgZXhvZ2Vub3VzIGlucHV0IHRvIGJsb2NrIEZDIGxheWVyczsgc3VwcG9ydHMgZnV0dXJlLWtub3duIGNvdmFyaWF0ZXMuIiwiTi1IaVRTOiBoaWVyYXJjaGljYWwgbXVsdGktcmF0ZSBzYW1wbGluZywgc3VwZXJpb3Igb24gaG9yaXpvbnMgSCBcdTAwM2UgNDgsIGF2YWlsYWJsZSBpbiBOZXVyYWxGb3JlY2FzdC4iLCJHZW5lcmljIGJhc2lzOiBmdWxseSBsZWFybmVkIGdfYiBhbmQgZ19mIGFsbG93IGFyYml0cmFyeSBkZWNvbXBvc2l0aW9ucyBidXQgbG9zZSBpbnRlcnByZXRhYmlsaXR5LiIsIlBvbHlub21pYWwgZGVncmVlIGFuZCBGb3VyaWVyIGhhcm1vbmljcyBhcmUgaHlwZXJwYXJhbWV0ZXJzICh0eXBpY2FsbHkgZGVncmVlPTMsIGhhcm1vbmljcz1mbG9vcihILzIpKS4iLCJUcmFpbmluZzogQURBTSB3aXRoIGxyfjFlLTMsIGdyYWRpZW50IGNsaXBwaW5nLCBhbmQgTUFFIG9yIE1TRSBsb3NzLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# N-BEATS — Basis Expansion for Interpretable Forecasting

N-BEATS (Neural Basis Expansion Analysis for Interpretable Time Series) is a purely deep-learning forecasting architecture that requires no time-series-specific inductive bias. It learns to decompose a time series into interpretable components through a doubly residual stack of feed-forward blocks. Each block produces a backcast (reconstruction of its input window) and a forecast (prediction of future values). Released in 2020, N-BEATS achieved state-of-the-art on M4 and M3 competitions retrospectively and remains a strong baseline for univariate forecasting.

## Architecture Overview

An N-BEATS model is organised into stacks, each containing multiple blocks. Each block receives the residual signal (original input minus the sum of all previous backcasts) — the doubly residual principle. The block produces two outputs: a backcast explaining part of its input, and a forecast contributing to the final prediction. Final forecast = sum of all blocks’ forecast outputs across all stacks. This design enables very deep networks without vanishing gradients.

## The N-BEATS Block — Backcast and Forecast

Each block contains four fully-connected layers with ReLU activations, followed by two linear heads producing basis expansion coefficients θ_b (backcast) and θ_f (forecast). The coefficients are multiplied by fixed (trend/seasonality) or learned (generic) basis vectors g_b and g_f. For generic N-BEATS, g_b and g_f are learned linear projections. For interpretable N-BEATS, g_b uses a polynomial basis and g_f uses a Fourier basis.

```python
import torch
import torch.nn as nn

class NBEATSBlock(nn.Module):
    """Single N-BEATS block: FC stack -> basis coefficients -> backcast + forecast."""
    def __init__(self, input_size, theta_size, forecast_size, hidden=256, num_layers=4):
        super().__init__()
        layers, in_dim = [], input_size
        for _ in range(num_layers):
            layers += [nn.Linear(in_dim, hidden), nn.ReLU()]
            in_dim = hidden
        self.fc_stack = nn.Sequential(*layers)
        self.theta_b = nn.Linear(hidden, theta_size)   # backcast basis coefficients
        self.theta_f = nn.Linear(hidden, theta_size)   # forecast basis coefficients
        self.g_b = nn.Linear(theta_size, input_size, bias=False)    # generic backcast basis
        self.g_f = nn.Linear(theta_size, forecast_size, bias=False) # generic forecast basis

    def forward(self, x):
        h = self.fc_stack(x)
        backcast = self.g_b(self.theta_b(h))
        forecast = self.g_f(self.theta_f(h))
        return backcast, forecast

# Verify shapes
block = NBEATSBlock(input_size=30, theta_size=32, forecast_size=10)
x = torch.randn(8, 30)
bc, fc = block(x)
print(f'Backcast: {bc.shape}, Forecast: {fc.shape}')
print(f'Params: {sum(p.numel() for p in block.parameters()):,}')
```

## Doubly Residual Stacking

In doubly residual stacking each block receives only the unexplained residual (input minus all previous backcasts) rather than the raw input. Simultaneously, forecasts from all blocks accumulate additively. This is doubly residual: residual on the input side (subtracting backcasts) and additive on the output side (summing forecasts). It allows each block to specialise on explaining a different portion of the signal.

```python
import torch
import torch.nn as nn

class NBEATSBlock(nn.Module):
    def __init__(self, in_sz, fc_sz, hidden=128):
        super().__init__()
        self.fc = nn.Sequential(nn.Linear(in_sz, hidden), nn.ReLU(),
                                nn.Linear(hidden, hidden), nn.ReLU())
        self.g_b = nn.Linear(hidden, in_sz, bias=False)
        self.g_f = nn.Linear(hidden, fc_sz, bias=False)
    def forward(self, x):
        h = self.fc(x)
        return self.g_b(h), self.g_f(h)

def doubly_residual_stack(blocks, x, fc_sz):
    """Subtract backcasts (residual input), accumulate forecasts."""
    residual = x.clone()
    forecast = torch.zeros(x.size(0), fc_sz)
    for blk in blocks:
        bc, fc = blk(residual)
        residual = residual - bc   # only unexplained signal passes forward
        forecast = forecast + fc   # each block contributes to total forecast
    return residual, forecast

torch.manual_seed(0)
IN, HZ = 30, 10
trend_blks = [NBEATSBlock(IN, HZ) for _ in range(3)]
seas_blks  = [NBEATSBlock(IN, HZ) for _ in range(3)]
x = torch.randn(4, IN)
r1, fc1 = doubly_residual_stack(trend_blks, x, HZ)
r2, fc2 = doubly_residual_stack(seas_blks, r1, HZ)
print(f'Input norm:           {x.norm():.4f}')
print(f'After trend residual: {r1.norm():.4f}')
print(f'After seas  residual: {r2.norm():.4f}')
print(f'Total forecast shape: {(fc1 + fc2).shape}')
```

## Interpretable N-BEATS — Trend and Seasonality Stacks

Interpretable N-BEATS uses fixed basis functions: polynomial for the trend stack and Fourier for the seasonality stack. The FC stack learns coefficient vectors θ which are multiplied by these fixed matrices. This forces trend blocks to model only polynomial trends and seasonality blocks to model only periodic patterns, enabling direct decomposition of the final forecast into interpretable components.

```python
import pandas as pd
import numpy as np
from neuralforecast import NeuralForecast
from neuralforecast.models import NBEATS
from neuralforecast.losses.pytorch import MAE

np.random.seed(42)
horizon = 12
dates = pd.date_range('2015-01', periods=96, freq='ME')
df = pd.concat([
    pd.DataFrame({
        'unique_id': f'series_{i}',
        'ds': dates,
        'y': (50 * np.sin(np.linspace(0, 6*np.pi, 96))
              + np.linspace(100, 200, 96)
              + 5 * np.random.randn(96))
    }) for i in range(3)
], ignore_index=True)

model = NBEATS(
    h=horizon, input_size=2*horizon,
    stack_types=['trend', 'seasonality'],  # interpretable N-BEATS variant
    n_blocks=[3, 3],
    mlp_units=[[256, 256], [256, 256]],
    max_steps=200, loss=MAE(),
)
nf = NeuralForecast(models=[model], freq='ME')
nf.fit(df=df)
preds = nf.predict()
print(preds.head())
print(f'Columns: {list(preds.columns)}')
```

## Interpreting Trend and Seasonality Block Outputs

The trend basis is a polynomial up to degree p: B_trend = [1, t, t², ..., tᵖ] with t normalised to [-1, 1]. The seasonality basis is a Fourier expansion: B_seas = [sin(t), cos(t), sin(2t), cos(2t), ...] at multiple harmonics. Learned coefficients θ from the FC stack act as amplitudes. Extracting θ × B gives the interpretable trend and seasonal forecast components separately.

```python
import numpy as np

def polynomial_basis(backcast_len, forecast_len, degree=3):
    """N-BEATS polynomial trend basis: [1, t, t^2, ..., t^degree]."""
    t = np.linspace(-1, 1, backcast_len + forecast_len)
    basis = np.stack([t**d for d in range(degree + 1)])
    return basis[:, :backcast_len], basis[:, backcast_len:]

def fourier_basis(backcast_len, forecast_len, harmonics=4):
    """N-BEATS Fourier seasonality basis: sin + cos at multiple frequencies."""
    t = np.linspace(0, 2*np.pi, backcast_len + forecast_len)
    k = np.arange(1, harmonics + 1)
    sin_b = np.sin(np.outer(k, t[:backcast_len]))
    cos_b = np.cos(np.outer(k, t[:backcast_len]))
    sin_f = np.sin(np.outer(k, t[backcast_len:]))
    cos_f = np.cos(np.outer(k, t[backcast_len:]))
    return np.vstack([sin_b, cos_b]), np.vstack([sin_f, cos_f])

np.random.seed(1)
BACK, FWD = 24, 12
trend_bc, trend_fc = polynomial_basis(BACK, FWD, degree=3)
seas_bc,  seas_fc  = fourier_basis(BACK, FWD, harmonics=4)

theta_t = np.array([100., 20., -3., 0.5])  # learned trend coefficients
theta_s = np.random.randn(8)               # learned seasonality coefficients
trend_component = theta_t @ trend_fc
seas_component  = theta_s @ seas_fc
print(f'Trend basis (forecast): {trend_fc.shape}  -- degree-3 polynomial')
print(f'Seas  basis (forecast): {seas_fc.shape}  -- 4 harmonics x sin+cos')
print(f'Trend forecast: {trend_component.round(2)}')
print(f'Combined first 4: {(trend_component + seas_component)[:4].round(3)}')
```

> **Interpretable vs Generic N-BEATS**: Use interpretable N-BEATS (trend + seasonality stacks with fixed bases) when explainability matters or when domain knowledge confirms polynomial trend and Fourier seasonality. Use generic N-BEATS (all-learned basis) for raw benchmark performance — it is typically 1–2% more accurate on M4 but produces no decomposition.

## N-BEATS vs N-HiTS vs Transformer Forecasters

| Model | Architecture | Interpretable | Covariates | Long Horizon | M4 Rank |
| --- | --- | --- | --- | --- | --- |
| N-BEATS Generic | Deep FC + learned basis | No | No (N-BEATSx needed) | Moderate | 1st (2020) |
| N-BEATS Interpretable | FC + poly + Fourier basis | Yes | No | Moderate | 1st (tied) |
| N-HiTS | Hierarchical interpolation, multi-rate pooling | Partial | Yes | Strong | SOTA long-horizon |
| TFT | Multi-head attention + LSTM | Via attention | Yes (rich) | Good | 2nd–3rd |
| PatchTST | Patch-based channel-independent Transformer | No | Limited | Strong | Competitive |

## N-BEATSx and N-HiTS Extensions

N-BEATSx extends N-BEATS to accept external covariates by concatenating them to the block input. N-HiTS improves long-horizon forecasting by hierarchical interpolation: each stack operates at a different temporal resolution (downsampling ratios [1, 2, 4]) and outputs are upsampled and summed. This dramatically reduces the effective sequence length for long horizons and improves accuracy on ETT and Electricity datasets versus vanilla Transformers.

- N-BEATS: purely univariate, no covariates, interpretable or generic stacks.
- N-BEATSx: adds exogenous input to block FC layers; supports future-known covariates.
- N-HiTS: hierarchical multi-rate sampling, superior on horizons H > 48, available in NeuralForecast.
- Generic basis: fully learned g_b and g_f allow arbitrary decompositions but lose interpretability.
- Polynomial degree and Fourier harmonics are hyperparameters (typically degree=3, harmonics=floor(H/2)).
- Training: ADAM with lr~1e-3, gradient clipping, and MAE or MSE loss.

---

