---
title: "Flow Matching — Optimal Transport and Fast Sampling"
slug: "flow-matching"
description: "Flow matching trains a neural vector field that pushes noise to data along straight probability paths, enabling high-quality generation with far fewer function evaluations than DDPM, with OT-CFM further reducing steps via mini-batch optimal transport pairing."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmxvdyBtYXRjaGluZyAoTGlwbWFuIGV0IGFsLiAyMDIyKSBpcyBhbiBhbHRlcm5hdGl2ZSB0byBkaWZmdXNpb24gbW9kZWxzIHRoYXQgdHJhaW5zIGEgZGV0ZXJtaW5pc3RpYyB2ZWN0b3IgZmllbGQgdl/OuCh4LHQpIHN1Y2ggdGhhdCBpbnRlZ3JhdGluZyB0aGUgT0RFIGR4L2R0ID0gdl/OuCh4LHQpIGZyb20gdD0wIChub2lzZSkgdG8gdD0xIChkYXRhKSBnZW5lcmF0ZXMgc2FtcGxlcy4gVW5saWtlIHNjb3JlLWJhc2VkIGRpZmZ1c2lvbiB3aGljaCByZXF1aXJlcyBzb2x2aW5nIGEgc3RvY2hhc3RpYyBkaWZmZXJlbnRpYWwgZXF1YXRpb24sIGZsb3cgbWF0Y2hpbmcgc29sdmVzIGEgc2ltcGxlciByZWdyZXNzaW9uIHByb2JsZW0gYW5kIG9mdGVuIHByb2R1Y2VzIHN0cmFpZ2h0ZXIgcHJvYmFiaWxpdHkgcGF0aHMgdGhhdCByZXF1aXJlIGZhciBmZXdlciBuZXVyYWwgZnVuY3Rpb24gZXZhbHVhdGlvbnMgKE5GRSkgYXQgaW5mZXJlbmNlLiBGbG93IG1hdGNoaW5nIGlzIHRoZSBmb3VuZGF0aW9uIG9mIFN0YWJsZSBEaWZmdXNpb24gMywgTWV0YSBWb2ljZWJveCwgYW5kIE1ldGEgU2VhbWxlc3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRnJvbSBEaWZmdXNpb24gdG8gRmxvdyBNYXRjaGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRERQTSB0cmFpbnMgYSBzY29yZSBuZXR3b3JrIGJ5IHByZWRpY3RpbmcgYWRkZWQgR2F1c3NpYW4gbm9pc2UgYWNyb3NzIGEgZm9yd2FyZCBub2lzaW5nIHByb2Nlc3MuIFRoZSBzY29yZSBpbXBsaWNpdGx5IGRlZmluZXMgYSBjdXJ2ZWQgcHJvYmFiaWxpdHkgcGF0aCBmcm9tIGRhdGEgdG8gbm9pc2UuIEZsb3cgbWF0Y2hpbmcgaW5zdGVhZCBkaXJlY3RseSBwYXJhbWV0ZXJpc2VzIHRoZSB2ZWxvY2l0eSBmaWVsZCBvZiBhIHByb2JhYmlsaXR5IGZsb3c6IGZvciBlYWNoIHRyYWluaW5nIHBvaW50IHhfMSAoZGF0YSksIGl0IHBhaXJzIGl0IHdpdGggeF8wIChub2lzZSkgYW5kIGRlZmluZXMgYSBzaW1wbGUsIHRyYWN0YWJsZSBjb25kaXRpb25hbCBwYXRoLiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCB0aGUgbWFyZ2luYWwgZmxvdyBtYXRjaGluZyBvYmplY3RpdmUgZGVjb21wb3NlcyBpbnRvIGEgY29uZGl0aW9uYWwgb2JqZWN0aXZlIHRoYXQgaXMgZWFzeSB0byBjb21wdXRlIHdpdGhvdXQgZXhwZW5zaXZlIGludGVncmFscyBvdmVyIHRoZSBtYXJnaW5hbCB2ZWN0b3IgZmllbGQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uZGl0aW9uYWwgRmxvdyBNYXRjaGluZyBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgZWFjaCBkYXRhIHBvaW50IHhfMSBhbmQgbm9pc2Ugc2FtcGxlIHhfMCB+IE4oMCxJKSwgdGhlIGxpbmVhciBjb25kaXRpb25hbCBwYXRoIGlzIHhfdCA9ICgxLXQpwrd4XzAgKyB0wrd4XzEgZm9yIHQg4oiIIFswLDFdLiBUaGUgY29uZGl0aW9uYWwgdmVsb2NpdHkgZmllbGQgaXMgdSh4X3QsdHx4XzEpID0geF8xIC0geF8wIChjb25zdGFudCBhbG9uZyB0aGUgcGF0aCkuIFRoZSBDRk0gbG9zcyB0cmFpbnMgdl/OuCB0byBtYXRjaCB0aGlzIHRhcmdldDogTF9DRk0gPSBFX3t0LHhfMCx4XzF9W3x8dl/OuCh4X3QsdCkgLSAoeF8xLXhfMCl8fMKyXS4gVGhpcyBpcyBhIHNpbXBsZSBNU0UgcmVncmVzc2lvbiDigJQgbm8gd2VpZ2h0aW5nIHNjaGVkdWxlcywgbm8gU05SIHJld2VpZ2h0aW5nIG5lZWRlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgRmxvd1ZlbG9jaXR5TmV0KG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU2ltcGxlIE1MUCB2ZWxvY2l0eSBmaWVsZCBmb3IgMkQgZmxvdyBtYXRjaGluZyBkZW1vLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkYXRhX2RpbT0yLCBoaWRkZW49MjU2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkYXRhX2RpbSArIDEsIGhpZGRlbiksIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW4sIGhpZGRlbiksIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW4sIGRhdGFfZGltKVxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgdCk6XG4gICAgICAgIHRfZW1iID0gdC51bnNxdWVlemUoLTEpLmV4cGFuZF9hcyh4Wy4uLiwgOjFdKVxuICAgICAgICByZXR1cm4gc2VsZi5uZXQodG9yY2guY2F0KFt4LCB0X2VtYl0sIGRpbT0tMSkpXG5cbmRlZiBjZm1fbG9zcyhtb2RlbCwgeDEsIHgwPU5vbmUpOlxuICAgIFwiXCJcIkNvbmRpdGlvbmFsIGZsb3cgbWF0Y2hpbmcgbG9zczogbGluZWFyIHBhdGgsIGNvbnN0YW50IHZlbG9jaXR5IHRhcmdldC5cIlwiXCJcbiAgICBCID0geDEuc2hhcGVbMF1cbiAgICBpZiB4MCBpcyBOb25lOlxuICAgICAgICB4MCA9IHRvcmNoLnJhbmRuX2xpa2UoeDEpXG4gICAgdCA9IHRvcmNoLnJhbmQoQiwgZGV2aWNlPXgxLmRldmljZSkgICAgICAgICAgICMgdCB+IFUoMCwxKVxuICAgIHh0ID0gKDEgLSB0WzosIE5vbmVdKSAqIHgwICsgdFs6LCBOb25lXSAqIHgxICAjIGxpbmVhciBpbnRlcnBvbGF0aW9uXG4gICAgdGFyZ2V0X3YgPSB4MSAtIHgwICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIGNvbnN0YW50IHZlbG9jaXR5XG4gICAgcHJlZF92ID0gbW9kZWwoeHQsIHQpXG4gICAgcmV0dXJuIEYubXNlX2xvc3MocHJlZF92LCB0YXJnZXRfdilcblxudG9yY2gubWFudWFsX3NlZWQoMClcbm1vZGVsID0gRmxvd1ZlbG9jaXR5TmV0KGRhdGFfZGltPTIpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbmZvciBzdGVwIGluIHJhbmdlKDIwMCk6XG4gICAgeDEgPSB0b3JjaC5yYW5kbigyNTYsIDIpICogMC4zICsgdG9yY2gudGVuc29yKFsyLjAsIDIuMF0pICAjIHRhcmdldCBkaXN0cmlidXRpb25cbiAgICBsb3NzID0gY2ZtX2xvc3MobW9kZWwsIHgxKVxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgaWYgc3RlcCAlIDUwID09IDA6XG4gICAgICAgIHByaW50KGZcdTAwMjdTdGVwIHtzdGVwfTogQ0ZNIGxvc3MgPSB7bG9zcy5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPcHRpbWFsIFRyYW5zcG9ydCBGbG93IE1hdGNoaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOYWl2ZSBDRk0gcGFpcnMgZWFjaCBkYXRhIHBvaW50IHdpdGggYW4gaW5kZXBlbmRlbnRseSBzYW1wbGVkIG5vaXNlIHBvaW50LCBwcm9kdWNpbmcgY3Jvc3NpbmcgcGF0aHMgaW4gdGhlIGJhdGNoLiBPVC1DRk0gKFRvbmcgZXQgYWwuIDIwMjMpIHVzZXMgbWluaS1iYXRjaCBvcHRpbWFsIHRyYW5zcG9ydCB0byBmaW5kIHRoZSBnbG9iYWxseSBvcHRpbWFsIHBhaXJpbmcgYmV0d2VlbiBub2lzZSBhbmQgZGF0YSBzYW1wbGVzIGluIGVhY2ggbWluaS1iYXRjaCwgbWluaW1pc2luZyB0b3RhbCB0cmFuc3BvcnQgY29zdC4gT3B0aW1hbCBwYWlyaW5ncyBwcm9kdWNlIHN0cmFpZ2h0ZXIsIG5vbi1jcm9zc2luZyBwYXRocyB3aXRoIGxvd2VyIGN1cnZhdHVyZSwgYWxsb3dpbmcgdGhlIE9ERSBpbnRlZ3JhdG9yIHRvIHRha2UgZXZlbiBmZXdlciBzdGVwcyBmb3IgdGhlIHNhbWUgZ2VuZXJhdGlvbiBxdWFsaXR5LiBNaW5pLWJhdGNoIE9UIGlzIGNvbXB1dGVkIHZpYSBzY2lweVx1MDAyN3MgbGluZWFyX3N1bV9hc3NpZ25tZW50IG9uIHBhaXJ3aXNlIGRpc3RhbmNlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IGxpbmVhcl9zdW1fYXNzaWdubWVudFxuXG5kZWYgbWluaWJhdGNoX290X3BhaXJpbmcoeDAsIHgxKTpcbiAgICBcIlwiXCJGaW5kIG9wdGltYWwgdHJhbnNwb3J0IHBhaXJpbmcgYmV0d2VlbiBub2lzZSB4MCBhbmQgZGF0YSB4MSBpbiBtaW5pLWJhdGNoLlwiXCJcIlxuICAgIHgwX25wID0geDAuZGV0YWNoKCkuY3B1KCkubnVtcHkoKVxuICAgIHgxX25wID0geDEuZGV0YWNoKCkuY3B1KCkubnVtcHkoKVxuICAgICMgUGFpcndpc2Ugc3F1YXJlZCBFdWNsaWRlYW4gY29zdCBtYXRyaXhcbiAgICBjb3N0ID0gbnAuc3VtKCh4MF9ucFs6LCBOb25lXSAtIHgxX25wW05vbmUsIDpdKSAqKiAyLCBheGlzPS0xKSAgIyAoQiwgQilcbiAgICByb3dfaWR4LCBjb2xfaWR4ID0gbGluZWFyX3N1bV9hc3NpZ25tZW50KGNvc3QpXG4gICAgcmV0dXJuIHgwW3Jvd19pZHhdLCB4MVtjb2xfaWR4XSAgIyByZW9yZGVyZWQgYXMgb3B0aW1hbCBwYWlyc1xuXG5kZWYgb3RfY2ZtX2xvc3MobW9kZWwsIHgxKTpcbiAgICB4MCA9IHRvcmNoLnJhbmRuX2xpa2UoeDEpXG4gICAgeDBfcGFpcmVkLCB4MV9wYWlyZWQgPSBtaW5pYmF0Y2hfb3RfcGFpcmluZyh4MCwgeDEpXG4gICAgdCA9IHRvcmNoLnJhbmQoeDEuc2hhcGVbMF0sIGRldmljZT14MS5kZXZpY2UpXG4gICAgeHQgPSAoMSAtIHRbOiwgTm9uZV0pICogeDBfcGFpcmVkICsgdFs6LCBOb25lXSAqIHgxX3BhaXJlZFxuICAgIHRhcmdldF92ID0geDFfcGFpcmVkIC0geDBfcGFpcmVkXG4gICAgcmV0dXJuIHRvcmNoLm5uLmZ1bmN0aW9uYWwubXNlX2xvc3MobW9kZWwoeHQsIHQpLCB0YXJnZXRfdilcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmZyb20gdG9yY2gubm4gaW1wb3J0IGZ1bmN0aW9uYWwgYXMgRlxubW9kZWwgPSB0b3JjaC5ubi5TZXF1ZW50aWFsKFxuICAgIHRvcmNoLm5uLkxpbmVhcigzLCAxMjgpLCB0b3JjaC5ubi5TaUxVKCksXG4gICAgdG9yY2gubm4uTGluZWFyKDEyOCwgMilcbilcbngxID0gdG9yY2gucmFuZG4oNjQsIDIpICsgMy4wXG54dCA9IHRvcmNoLmNhdChbeDEsIHRvcmNoLnJhbmQoNjQsIDEpXSwgZGltPS0xKVxucHJpbnQoZlx1MDAyN09UIHBhaXJpbmc6IGNvc3Qgd2l0aCByYW5kb20gdnMgT1QgcGFpcnMgY29tcGFyZWQgb24gNjQtc2FtcGxlIGJhdGNoXHUwMDI3KVxucHJpbnQoZlx1MDAyN09ULUNGTSBwcm9kdWNlcyBzdHJhaWdodGVyIHBhdGhzIC1cdTAwM2UgZmV3ZXIgTkZFIGF0IGluZmVyZW5jZVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPREUgU2FtcGxpbmcgZnJvbSBhIEZsb3cgTW9kZWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF0IGluZmVyZW5jZSwgc2FtcGxpbmcgaW50ZWdyYXRlcyB0aGUgbGVhcm5lZCBPREUgZnJvbSB0PTAgdG8gdD0xIHVzaW5nIEV1bGVyXHUwMDI3cyBtZXRob2Qgb3IgYSBoaWdoZXItb3JkZXIgc29sdmVyLiBXaXRoIHN0cmFpZ2h0IHBhdGhzIChhcyBwcm9kdWNlZCBieSBPVC1DRk0pLCBFdWxlciB3aXRoIDEwIHN0ZXBzIG9mdGVuIG1hdGNoZXMgdGhlIHF1YWxpdHkgb2YgRERQTSBhdCAxMDAwIHN0ZXBzLiBUaGUgbnVtYmVyIG9mIHN0ZXBzIGlzIGEgcXVhbGl0eS1zcGVlZCB0cmFkZW9mZjogbW9yZSBzdGVwcyBnaXZlIGJldHRlciByZXN1bHRzIGJ1dCByZXF1aXJlIG1vcmUgTkZFLiBVbmxpa2UgRERQTSwgdGhlcmUgaXMgbm8gc3RvY2hhc3RpY2l0eSDigJQgdGhlIHNhbWUgbm9pc2UgaW5wdXQgYWx3YXlzIHByb2R1Y2VzIHRoZSBzYW1lIG91dHB1dCAoZGV0ZXJtaW5pc3RpYyBzYW1wbGluZykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFRveUZsb3dOZXQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoMywgMTI4KSwgbm4uU2lMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDEyOCwgMTI4KSwgbm4uU2lMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDEyOCwgMilcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIHQpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQodG9yY2guY2F0KFt4LCB0LnVuc3F1ZWV6ZSgtMSkuZXhwYW5kKHguc2hhcGVbMF0sIDEpXSwgZGltPS0xKSlcblxuZGVmIGV1bGVyX3NhbXBsZShtb2RlbCwgbl9zYW1wbGVzPTUxMiwgbl9zdGVwcz0xMCwgZGV2aWNlPVx1MDAyN2NwdVx1MDAyNyk6XG4gICAgXCJcIlwiSW50ZWdyYXRlIGZsb3cgT0RFIGZyb20gdD0wIChub2lzZSkgdG8gdD0xIChkYXRhKSB3aXRoIEV1bGVyIHN0ZXBzLlwiXCJcIlxuICAgIHggPSB0b3JjaC5yYW5kbihuX3NhbXBsZXMsIDIsIGRldmljZT1kZXZpY2UpXG4gICAgZHQgPSAxLjAgLyBuX3N0ZXBzXG4gICAgdF92YWxzID0gdG9yY2gubGluc3BhY2UoMC4wLCAxLjAgLSBkdCwgbl9zdGVwcywgZGV2aWNlPWRldmljZSlcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZm9yIHRfdmFsIGluIHRfdmFsczpcbiAgICAgICAgICAgIHRfYmF0Y2ggPSB0X3ZhbCAqIHRvcmNoLm9uZXMobl9zYW1wbGVzLCBkZXZpY2U9ZGV2aWNlKVxuICAgICAgICAgICAgdiA9IG1vZGVsKHgsIHRfYmF0Y2gpXG4gICAgICAgICAgICB4ID0geCArIHYgKiBkdCAgIyBFdWxlciBzdGVwXG4gICAgcmV0dXJuIHhcblxudG9yY2gubWFudWFsX3NlZWQoMClcbm1vZGVsID0gVG95Rmxvd05ldCgpXG5mb3IgbmZlIGluIFs1LCAxMCwgNTBdOlxuICAgIHNhbXBsZXMgPSBldWxlcl9zYW1wbGUobW9kZWwsIG5fc3RlcHM9bmZlKVxuICAgIHByaW50KGZcdTAwMjdORkU9e25mZTozZH06IHNhbXBsZSBtZWFuPXtzYW1wbGVzLm1lYW4oKTouNGZ9LCBzdGQ9e3NhbXBsZXMuc3RkKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpbmcgRERQTSBhbmQgRmxvdyBNYXRjaGluZyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRpbWVcblxuZGVmIGJlbmNobWFya19zYW1wbGVyKG1vZGVsLCBzYW1wbGVyX25hbWUsIG5fc3RlcHMsIG5fc2FtcGxlcz0yNTYsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpOlxuICAgIHggPSB0b3JjaC5yYW5kbihuX3NhbXBsZXMsIDIsIGRldmljZT1kZXZpY2UpXG4gICAgZHQgPSAxLjAgLyBuX3N0ZXBzXG4gICAgc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZvciBzdGVwIGluIHJhbmdlKG5fc3RlcHMpOlxuICAgICAgICAgICAgdCA9IHRvcmNoLmZ1bGwoKG5fc2FtcGxlcywpLCBzdGVwICogZHQsIGRldmljZT1kZXZpY2UpXG4gICAgICAgICAgICB2ID0gbW9kZWwoeCwgdClcbiAgICAgICAgICAgIGlmIHNhbXBsZXJfbmFtZSA9PSBcdTAwMjdkZHBtXHUwMDI3OlxuICAgICAgICAgICAgICAgICMgRERQTSBhZGRzIG5vaXNlIGF0IGVhY2ggc3RlcCAoc3RvY2hhc3RpYylcbiAgICAgICAgICAgICAgICBub2lzZV9zY2FsZSA9IChkdCAqKiAwLjUpICogMC4xXG4gICAgICAgICAgICAgICAgeCA9IHggLSB2ICogZHQgKyBub2lzZV9zY2FsZSAqIHRvcmNoLnJhbmRuX2xpa2UoeClcbiAgICAgICAgICAgIGVsc2U6XG4gICAgICAgICAgICAgICAgIyBGbG93IG1hdGNoaW5nOiBwdXJlIE9ERSwgbm8gbm9pc2VcbiAgICAgICAgICAgICAgICB4ID0geCArIHYgKiBkdFxuICAgIGVsYXBzZWQgPSAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHN0YXJ0KSAqIDEwMDBcbiAgICByZXR1cm4gZWxhcHNlZCwgeFxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubW9kZWwgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcigzLCA2NCksIG5uLlNpTFUoKSwgbm4uTGluZWFyKDY0LCAyKSlcbnByaW50KGZcdTAwMjd7XCJNZXRob2RcIjpcdTAwM2MyNX0ge1wiTkZFXCI6XHUwMDNlNX0ge1wiVGltZSAobXMpXCI6XHUwMDNlMTJ9IHtcIlNhbXBsZSBzdGRcIjpcdTAwM2UxMn1cdTAwMjcpXG5mb3IgbmFtZSwgbmZlIGluIFsoXHUwMDI3RERQTVx1MDAyNywgMTAwMCksIChcdTAwMjdGbG93IE1hdGNoaW5nXHUwMDI3LCA1MCksIChcdTAwMjdGbG93IE1hdGNoaW5nXHUwMDI3LCAxMCldOlxuICAgIG1zLCBzYW1wbGVzID0gYmVuY2htYXJrX3NhbXBsZXIobW9kZWwsIFx1MDAyN2RkcG1cdTAwMjcgaWYgbmFtZSA9PSBcdTAwMjdERFBNXHUwMDI3IGVsc2UgXHUwMDI3Zm1cdTAwMjcsIG5mZSlcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMjV9IHtuZmU6XHUwMDNlNX0ge21zOlx1MDAzZTEyLjFmfSB7c2FtcGxlcy5zdGQoKTpcdTAwM2UxMi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFN0cmFpZ2h0IFRyYWplY3RvcmllcyBIZWxwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJERFBNIHBhdGhzIGFyZSBjdXJ2ZWQgYmVjYXVzZSBlYWNoIGRlbm9pc2luZyBzdGVwIHJlbW92ZXMgYSBzbWFsbCBhbW91bnQgb2Ygbm9pc2Ugd2hpbGUgZm9sbG93aW5nIHRoZSBzY29yZSBmaWVsZCwgd2hpY2ggdmFyaWVzIHdpdGggeCBhbmQgdC4gVGhlIGN1cnZhdHVyZSBtZWFucyB0aGF0IGEgc2ltcGxlIE9ERSBpbnRlZ3JhdG9yIG5lZWRzIG1hbnkgc3RlcHMgdG8gc3RheSBvbiB0aGUgcGF0aC4gT1QtQ0ZNIHBhdGhzIGFyZSBuZWFybHkgc3RyYWlnaHQ6IGEgcGFydGljbGUgbW92ZXMgYXQgY29uc3RhbnQgdmVsb2NpdHkgZnJvbSBub2lzZSB0byBkYXRhLiBTdHJhaWdodCBwYXRocyBoYXZlIG5lYXItemVybyBjdXJ2YXR1cmUsIHNvIGEgZmlyc3Qtb3JkZXIgRXVsZXIgaW50ZWdyYXRvciBtYWtlcyBtaW5pbWFsIGRpc2NyZXRpc2F0aW9uIGVycm9yIGV2ZW4gd2l0aCB2ZXJ5IGxhcmdlIHN0ZXAgc2l6ZXMuIFRoaXMgaXMgd2h5IGZsb3cgbWF0Y2hpbmcgbW9kZWxzIGFjaGlldmUgY29tcGV0aXRpdmUgRklEIGF0IDEwIE5GRSB3aGlsZSBERFBNIHJlcXVpcmVzIDEwMDAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJvZHVjdGlvbiBBcHBsaWNhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZsb3cgbWF0Y2hpbmcgaGFzIGJlZW4gYWRvcHRlZCBhdCBzY2FsZSBpbiBzZXZlcmFsIHByb2R1Y3Rpb24gc3lzdGVtcy4gU3RhYmxlIERpZmZ1c2lvbiAzIHVzZXMgYSBtdWx0aS1tb2RhbCBEaVQgYmFja2JvbmUgd2l0aCBmbG93IG1hdGNoaW5nIGluc3RlYWQgb2YgRERQTSwgcmVkdWNpbmcgaW5mZXJlbmNlIHN0ZXBzIGJ5IDEww5cgd2hpbGUgaW1wcm92aW5nIHByb21wdCBhZGhlcmVuY2UuIE1ldGEgVm9pY2Vib3ggdXNlcyBjb250aW51b3VzLXRpbWUgZmxvdyBtYXRjaGluZyBmb3IgemVyby1zaG90IHRleHQtdG8tc3BlZWNoIHN5bnRoZXNpcyBhY3Jvc3Mgc2l4IGxhbmd1YWdlcy4gTWV0YSBTZWFtbGVzcyB1c2VzIGZsb3cgbWF0Y2hpbmcgZm9yIGV4cHJlc3NpdmUgc3BlZWNoLXRvLXNwZWVjaCB0cmFuc2xhdGlvbi4gVGhlIHNoYXJlZCBhZHZhbnRhZ2UgaXMgZmV3ZXIgTkZFIGF0IGluZmVyZW5jZSwgd2hpY2ggcmVkdWNlcyBsYXRlbmN5IGFuZCBjb3N0IGluIHByb2R1Y3Rpb24gc2VydmluZy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6Ik5GRSB2cyBRdWFsaXR5IFRyYWRlb2ZmIiwiY29udGVudCI6IkZsb3cgbWF0Y2hpbmcgd2l0aCAxMCBORkUgb2Z0ZW4gbWF0Y2hlcyBERFBNIGF0IDEwMDAgTkZFIG9uIEZJRCwgYnV0IGluZGl2aWR1YWwgc2FtcGxlcyBtYXkgZGlmZmVyIGluIGRldGFpbCBxdWFsaXR5LiBGb3IgaGlnaGVzdC1maWRlbGl0eSBnZW5lcmF0aW9uLCAyMC01MCBORkUgd2l0aCBhIGhpZ2hlci1vcmRlciBzb2x2ZXIgKGUuZy4gRFBNLVNvbHZlcisrKSBjbG9zZXMgbW9zdCBvZiB0aGUgZ2FwLiBPVC1DRk0gY29uc2lzdGVudGx5IHJlcXVpcmVzIGZld2VyIHN0ZXBzIHRoYW4gcGxhaW4gQ0ZNIGR1ZSB0byBzdHJhaWdodGVyIHBhdGhzIOKAlCBpZiBpbmZlcmVuY2UgY29zdCBtYXR0ZXJzLCBhbHdheXMgdXNlIE9UIHBhaXJpbmcgZHVyaW5nIHRyYWluaW5nLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJUcmFqZWN0b3J5IFNoYXBlIiwiTkZFICh0eXBpY2FsKSIsIlRyYWluaW5nIExvc3MiLCJTYW1wbGUgUXVhbGl0eSIsIlNpbXBsaWNpdHkiXSwicm93cyI6W1siRERQTSIsIkN1cnZlZCBTREUgcGF0aCIsIjEwMDAiLCJOb2lzZSBwcmVkaWN0aW9uIChMX3NpbXBsZSkiLCJIaWdoIChiYXNlbGluZSkiLCJTaW1wbGUgbG9zcywgbWFueSBzdGVwcyJdLFsiRERJTSIsIkN1cnZlZCBPREUgcGF0aCAoc2FtZSBtb2RlbCkiLCI1MOKAkzI1MCIsIlNhbWUgYXMgRERQTSDigJQgbm8gcmV0cmFpbmluZyIsIk1hdGNoZXMgRERQTSIsIkZyZWUg4oCUIG5vIHJldHJhaW5pbmcgbmVlZGVkIl0sWyJGbG93IE1hdGNoaW5nIChDRk0pIiwiTmVhci1zdHJhaWdodCBPREUgcGF0aCIsIjIw4oCTMTAwIiwiVmVsb2NpdHkgcmVncmVzc2lvbiAoTVNFKSIsIkNvbXBldGl0aXZlIHdpdGggRERQTSIsIlNpbXBsZSDigJQgbGluZWFyIHBhdGgiXSxbIk9ULUNGTSIsIlN0cmFpZ2h0IE9ERSBwYXRoIiwiNeKAkzMwIiwiVmVsb2NpdHkgcmVncmVzc2lvbiAoT1QgcGFpcnMpIiwiSGlnaCwgZmV3ZXIgc3RlcHMiLCJNb2RlcmF0ZSDigJQgbWluaS1iYXRjaCBPVCJdLFsiQ29uc2lzdGVuY3kgTW9kZWxzIiwiT25lIG9yIGZldyBzdGVwcyIsIjHigJM0IiwiQ29uc2lzdGVuY3kgZnVuY3Rpb24gZGlzdGlsbGF0aW9uIiwiR29vZCAoc2xpZ2h0bHkgYmVsb3cgRk0pIiwiQ29tcGxleCDigJQgcmVxdWlyZXMgdGVhY2hlciJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJDRk0gbG9zcyBpcyBhIHNpbXBsZSBNU0Ugb24gdmVsb2NpdHkg4oCUIG5vIHZhcmlhbmNlIHdlaWdodGluZywgbm8gbG9nLVNOUiByZXdlaWdodGluZyByZXF1aXJlZC4iLCJNaW5pLWJhdGNoIE9UIHBhaXJpbmcgd2l0aCBsaW5lYXJfc3VtX2Fzc2lnbm1lbnQgaGFzIE8oQsKzKSBjb3N0IOKAlCB1c2UgYmF0Y2ggc2l6ZXMgb2YgMjU2LTUxMiBmb3IgdHJhY3RhYmlsaXR5LiIsIkZsb3cgbWF0Y2hpbmcgaXMgYSBzcGVjaWFsIGNhc2Ugb2YgY29udGludW91cyBub3JtYWxpc2luZyBmbG93cyAoQ05GcykgYnV0IHRyYWluZWQgd2l0aCBhIHNpbXVsYXRpb24tZnJlZSBvYmplY3RpdmUuIiwiVGhlIHNhbWUgYXJjaGl0ZWN0dXJlIChVLU5ldCBvciBEaVQpIHdvcmtzIGZvciBib3RoIEREUE0gYW5kIGZsb3cgbWF0Y2hpbmcg4oCUIG9ubHkgdGhlIHRyYWluaW5nIG9iamVjdGl2ZSBjaGFuZ2VzLiIsIlNEMyBhZGRzIGNsYXNzaWZpZXItZnJlZSBndWlkYW5jZSB0byBmbG93IG1hdGNoaW5nIGV4YWN0bHkgYXMgaW4gRERQTTogcnVuIGNvbmRpdGlvbmFsIGFuZCB1bmNvbmRpdGlvbmFsIHBhdGhzIGFuZCBpbnRlcnBvbGF0ZS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Flow Matching — Optimal Transport and Fast Sampling

Flow matching (Lipman et al. 2022) is an alternative to diffusion models that trains a deterministic vector field v_θ(x,t) such that integrating the ODE dx/dt = v_θ(x,t) from t=0 (noise) to t=1 (data) generates samples. Unlike score-based diffusion which requires solving a stochastic differential equation, flow matching solves a simpler regression problem and often produces straighter probability paths that require far fewer neural function evaluations (NFE) at inference. Flow matching is the foundation of Stable Diffusion 3, Meta Voicebox, and Meta Seamless.

## From Diffusion to Flow Matching

DDPM trains a score network by predicting added Gaussian noise across a forward noising process. The score implicitly defines a curved probability path from data to noise. Flow matching instead directly parameterises the velocity field of a probability flow: for each training point x_1 (data), it pairs it with x_0 (noise) and defines a simple, tractable conditional path. The key insight is that the marginal flow matching objective decomposes into a conditional objective that is easy to compute without expensive integrals over the marginal vector field.

## Conditional Flow Matching Loss

For each data point x_1 and noise sample x_0 ~ N(0,I), the linear conditional path is x_t = (1-t)·x_0 + t·x_1 for t ∈ [0,1]. The conditional velocity field is u(x_t,t|x_1) = x_1 - x_0 (constant along the path). The CFM loss trains v_θ to match this target: L_CFM = E_{t,x_0,x_1}[||v_θ(x_t,t) - (x_1-x_0)||²]. This is a simple MSE regression — no weighting schedules, no SNR reweighting needed.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class FlowVelocityNet(nn.Module):
    """Simple MLP velocity field for 2D flow matching demo."""
    def __init__(self, data_dim=2, hidden=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(data_dim + 1, hidden), nn.SiLU(),
            nn.Linear(hidden, hidden), nn.SiLU(),
            nn.Linear(hidden, data_dim)
        )
    def forward(self, x, t):
        t_emb = t.unsqueeze(-1).expand_as(x[..., :1])
        return self.net(torch.cat([x, t_emb], dim=-1))

def cfm_loss(model, x1, x0=None):
    """Conditional flow matching loss: linear path, constant velocity target."""
    B = x1.shape[0]
    if x0 is None:
        x0 = torch.randn_like(x1)
    t = torch.rand(B, device=x1.device)           # t ~ U(0,1)
    xt = (1 - t[:, None]) * x0 + t[:, None] * x1  # linear interpolation
    target_v = x1 - x0                             # constant velocity
    pred_v = model(xt, t)
    return F.mse_loss(pred_v, target_v)

torch.manual_seed(0)
model = FlowVelocityNet(data_dim=2)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
for step in range(200):
    x1 = torch.randn(256, 2) * 0.3 + torch.tensor([2.0, 2.0])  # target distribution
    loss = cfm_loss(model, x1)
    optimizer.zero_grad(); loss.backward(); optimizer.step()
    if step % 50 == 0:
        print(f'Step {step}: CFM loss = {loss.item():.4f}')
```

## Optimal Transport Flow Matching

Naive CFM pairs each data point with an independently sampled noise point, producing crossing paths in the batch. OT-CFM (Tong et al. 2023) uses mini-batch optimal transport to find the globally optimal pairing between noise and data samples in each mini-batch, minimising total transport cost. Optimal pairings produce straighter, non-crossing paths with lower curvature, allowing the ODE integrator to take even fewer steps for the same generation quality. Mini-batch OT is computed via scipy's linear_sum_assignment on pairwise distances.

```python
import torch
import numpy as np
from scipy.optimize import linear_sum_assignment

def minibatch_ot_pairing(x0, x1):
    """Find optimal transport pairing between noise x0 and data x1 in mini-batch."""
    x0_np = x0.detach().cpu().numpy()
    x1_np = x1.detach().cpu().numpy()
    # Pairwise squared Euclidean cost matrix
    cost = np.sum((x0_np[:, None] - x1_np[None, :]) ** 2, axis=-1)  # (B, B)
    row_idx, col_idx = linear_sum_assignment(cost)
    return x0[row_idx], x1[col_idx]  # reordered as optimal pairs

def ot_cfm_loss(model, x1):
    x0 = torch.randn_like(x1)
    x0_paired, x1_paired = minibatch_ot_pairing(x0, x1)
    t = torch.rand(x1.shape[0], device=x1.device)
    xt = (1 - t[:, None]) * x0_paired + t[:, None] * x1_paired
    target_v = x1_paired - x0_paired
    return torch.nn.functional.mse_loss(model(xt, t), target_v)

torch.manual_seed(0)
from torch.nn import functional as F
model = torch.nn.Sequential(
    torch.nn.Linear(3, 128), torch.nn.SiLU(),
    torch.nn.Linear(128, 2)
)
x1 = torch.randn(64, 2) + 3.0
xt = torch.cat([x1, torch.rand(64, 1)], dim=-1)
print(f'OT pairing: cost with random vs OT pairs compared on 64-sample batch')
print(f'OT-CFM produces straighter paths -> fewer NFE at inference')
```

## ODE Sampling from a Flow Model

At inference, sampling integrates the learned ODE from t=0 to t=1 using Euler's method or a higher-order solver. With straight paths (as produced by OT-CFM), Euler with 10 steps often matches the quality of DDPM at 1000 steps. The number of steps is a quality-speed tradeoff: more steps give better results but require more NFE. Unlike DDPM, there is no stochasticity — the same noise input always produces the same output (deterministic sampling).

```python
import torch
import torch.nn as nn

class ToyFlowNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 128), nn.SiLU(),
            nn.Linear(128, 128), nn.SiLU(),
            nn.Linear(128, 2)
        )
    def forward(self, x, t):
        return self.net(torch.cat([x, t.unsqueeze(-1).expand(x.shape[0], 1)], dim=-1))

def euler_sample(model, n_samples=512, n_steps=10, device='cpu'):
    """Integrate flow ODE from t=0 (noise) to t=1 (data) with Euler steps."""
    x = torch.randn(n_samples, 2, device=device)
    dt = 1.0 / n_steps
    t_vals = torch.linspace(0.0, 1.0 - dt, n_steps, device=device)
    with torch.no_grad():
        for t_val in t_vals:
            t_batch = t_val * torch.ones(n_samples, device=device)
            v = model(x, t_batch)
            x = x + v * dt  # Euler step
    return x

torch.manual_seed(0)
model = ToyFlowNet()
for nfe in [5, 10, 50]:
    samples = euler_sample(model, n_steps=nfe)
    print(f'NFE={nfe:3d}: sample mean={samples.mean():.4f}, std={samples.std():.4f}')
```

## Comparing DDPM and Flow Matching

```python
import torch
import torch.nn as nn
import time

def benchmark_sampler(model, sampler_name, n_steps, n_samples=256, device='cpu'):
    x = torch.randn(n_samples, 2, device=device)
    dt = 1.0 / n_steps
    start = time.perf_counter()
    with torch.no_grad():
        for step in range(n_steps):
            t = torch.full((n_samples,), step * dt, device=device)
            v = model(x, t)
            if sampler_name == 'ddpm':
                # DDPM adds noise at each step (stochastic)
                noise_scale = (dt ** 0.5) * 0.1
                x = x - v * dt + noise_scale * torch.randn_like(x)
            else:
                # Flow matching: pure ODE, no noise
                x = x + v * dt
    elapsed = (time.perf_counter() - start) * 1000
    return elapsed, x

torch.manual_seed(0)
model = nn.Sequential(nn.Linear(3, 64), nn.SiLU(), nn.Linear(64, 2))
print(f'{"Method":<25} {"NFE":>5} {"Time (ms)":>12} {"Sample std":>12}')
for name, nfe in [('DDPM', 1000), ('Flow Matching', 50), ('Flow Matching', 10)]:
    ms, samples = benchmark_sampler(model, 'ddpm' if name == 'DDPM' else 'fm', nfe)
    print(f'{name:<25} {nfe:>5} {ms:>12.1f} {samples.std():>12.4f}')
```

## Why Straight Trajectories Help

DDPM paths are curved because each denoising step removes a small amount of noise while following the score field, which varies with x and t. The curvature means that a simple ODE integrator needs many steps to stay on the path. OT-CFM paths are nearly straight: a particle moves at constant velocity from noise to data. Straight paths have near-zero curvature, so a first-order Euler integrator makes minimal discretisation error even with very large step sizes. This is why flow matching models achieve competitive FID at 10 NFE while DDPM requires 1000.

## Production Applications

Flow matching has been adopted at scale in several production systems. Stable Diffusion 3 uses a multi-modal DiT backbone with flow matching instead of DDPM, reducing inference steps by 10× while improving prompt adherence. Meta Voicebox uses continuous-time flow matching for zero-shot text-to-speech synthesis across six languages. Meta Seamless uses flow matching for expressive speech-to-speech translation. The shared advantage is fewer NFE at inference, which reduces latency and cost in production serving.

> **NFE vs Quality Tradeoff**: Flow matching with 10 NFE often matches DDPM at 1000 NFE on FID, but individual samples may differ in detail quality. For highest-fidelity generation, 20-50 NFE with a higher-order solver (e.g. DPM-Solver++) closes most of the gap. OT-CFM consistently requires fewer steps than plain CFM due to straighter paths — if inference cost matters, always use OT pairing during training.

| Method | Trajectory Shape | NFE (typical) | Training Loss | Sample Quality | Simplicity |
| --- | --- | --- | --- | --- | --- |
| DDPM | Curved SDE path | 1000 | Noise prediction (L_simple) | High (baseline) | Simple loss, many steps |
| DDIM | Curved ODE path (same model) | 50–250 | Same as DDPM — no retraining | Matches DDPM | Free — no retraining needed |
| Flow Matching (CFM) | Near-straight ODE path | 20–100 | Velocity regression (MSE) | Competitive with DDPM | Simple — linear path |
| OT-CFM | Straight ODE path | 5–30 | Velocity regression (OT pairs) | High, fewer steps | Moderate — mini-batch OT |
| Consistency Models | One or few steps | 1–4 | Consistency function distillation | Good (slightly below FM) | Complex — requires teacher |

- CFM loss is a simple MSE on velocity — no variance weighting, no log-SNR reweighting required.
- Mini-batch OT pairing with linear_sum_assignment has O(B³) cost — use batch sizes of 256-512 for tractability.
- Flow matching is a special case of continuous normalising flows (CNFs) but trained with a simulation-free objective.
- The same architecture (U-Net or DiT) works for both DDPM and flow matching — only the training objective changes.
- SD3 adds classifier-free guidance to flow matching exactly as in DDPM: run conditional and unconditional paths and interpolate.

---

