---
title: "Downstream Evaluation — Linear Probe, Fine-Tuning, and k-NN"
slug: "downstream-evaluation-ssl"
description: "A systematic guide to evaluating self-supervised representations via linear probing, full fine-tuning, k-NN retrieval, semi-supervised protocols, and transfer learning benchmarks, with standardised code for fair comparison across SSL methods."
tags: ["deep-learning", "self-supervised-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXZhbHVhdGluZyBzZWxmLXN1cGVydmlzZWQgbGVhcm5pbmcgaXMgYXMgaW1wb3J0YW50IGFzIHRoZSB0cmFpbmluZyBvYmplY3RpdmUgaXRzZWxmLiBBIHJlcHJlc2VudGF0aW9uIHRoYXQgcGVyZm9ybXMgd2VsbCB1bmRlciBvbmUgZXZhbHVhdGlvbiBwcm90b2NvbCBtYXkgZmFpbCBhbm90aGVyIOKAlCByZXZlYWxpbmcgZGlmZmVyZW50IGFzcGVjdHMgb2Ygd2hhdCB0aGUgZW5jb2RlciBoYXMgbGVhcm5lZC4gVGhlIGZpZWxkIGhhcyBjb252ZXJnZWQgb24gZm91ciBzdGFuZGFyZCBwcm90b2NvbHM6IGxpbmVhciBwcm9iaW5nIChmcm96ZW4gZW5jb2RlciwgbGluZWFyIGNsYXNzaWZpZXIpLCBmdWxsIGZpbmUtdHVuaW5nICh1bmZyZWV6ZSBlbmNvZGVyKSwgay1OTiBldmFsdWF0aW9uIChubyB0cmFpbmluZyBhdCBhbGwpLCBhbmQgc2VtaS1zdXBlcnZpc2VkIGxlYXJuaW5nIChsaW1pdGVkIGxhYmVscykuIEVhY2ggbWVhc3VyZXMgc29tZXRoaW5nIGRpZmZlcmVudDogbGluZWFyIHByb2JlIG1lYXN1cmVzIHJlcHJlc2VudGF0aW9uIHF1YWxpdHk7IGZpbmUtdHVuaW5nIG1lYXN1cmVzIGxlYXJuaW5nIGNhcGFjaXR5OyBrLU5OIG1lYXN1cmVzIGZlYXR1cmUgZ2VvbWV0cnk7IHNlbWktc3VwZXJ2aXNlZCBtZWFzdXJlcyBsYWJlbCBlZmZpY2llbmN5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbmVhciBQcm9iZSDigJQgTWVhc3VyaW5nIFJlcHJlc2VudGF0aW9uIFF1YWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxpbmVhciBldmFsdWF0aW9uIGlzIHRoZSBnb2xkIHN0YW5kYXJkIGZvciBtZWFzdXJpbmcgdGhlIHF1YWxpdHkgb2Ygc2VsZi1zdXBlcnZpc2VkIHJlcHJlc2VudGF0aW9ucy4gVGhlIGVuY29kZXIgaXMgZnJvemVuIGNvbXBsZXRlbHkgKG5vIGdyYWRpZW50IHRocm91Z2ggaXRzIHBhcmFtZXRlcnMpLiBBIHNpbmdsZSBsaW5lYXIgbGF5ZXIgaXMgdHJhaW5lZCBvbiB0b3Agb2YgdGhlIGZyb3plbiBmZWF0dXJlcyB1c2luZyB0aGUgbGFiZWxsZWQgdHJhaW5pbmcgc2V0LiBUaGUgcmVzdWx0aW5nIHRvcC0xIGFjY3VyYWN5IG9uIHRoZSB2YWxpZGF0aW9uIHNldCBtZWFzdXJlcyBob3cgbGluZWFybHkgc2VwYXJhYmxlIHRoZSBmZWF0dXJlcyBhcmUg4oCUIGEgaGlnaCBzY29yZSBpbmRpY2F0ZXMgdGhlIGVuY29kZXIgaGFzIG9yZ2FuaXNlZCBzZW1hbnRpYyBjYXRlZ29yaWVzIGludG8gZGlzdGluY3QsIGxpbmVhcmx5IHNlcGFyYWJsZSByZWdpb25zIG9mIHRoZSBmZWF0dXJlIHNwYWNlIHdpdGhvdXQgYW55IGxhYmVsIHN1cGVydmlzaW9uLiBUaGlzIGlzIHRoZSBtb3N0IGNvbnN0cmFpbmVkIHByb3RvY29sLCBtYWtpbmcgaXQgdGhlIGZhaXJlc3QgbWVhc3VyZSBvZiB3aGF0IFNTTCBhY3R1YWxseSBsZWFybmVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgTG9naXN0aWNSZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YUxvYWRlclxuXG5cbmRlZiBleHRyYWN0X2ZlYXR1cmVzKGJhY2tib25lLCBkYXRhbG9hZGVyLCBkZXZpY2U9XHUwMDI3Y3VkYVx1MDAyNyk6XG4gICAgXCJcIlwiRXh0cmFjdCBmcm96ZW4gZmVhdHVyZXMgZnJvbSBTU0wgYmFja2JvbmUuIFJldHVybnMgKGZlYXR1cmVzLCBsYWJlbHMpIG51bXB5IGFycmF5cy5cIlwiXCJcbiAgICBiYWNrYm9uZS5ldmFsKCkudG8oZGV2aWNlKVxuICAgIGZvciBwIGluIGJhY2tib25lLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgcC5yZXF1aXJlc19ncmFkXyhGYWxzZSlcblxuICAgIGZlYXRzX2xpc3QsIGxhYmVsX2xpc3QgPSBbXSwgW11cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZm9yIGltZ3MsIGxhYmVscyBpbiBkYXRhbG9hZGVyOlxuICAgICAgICAgICAgaW1ncyA9IGltZ3MudG8oZGV2aWNlKVxuICAgICAgICAgICAgZmVhdHMgPSBiYWNrYm9uZShpbWdzKSAgICAgICAgICAgICAgICAgIyAoQiwgRCkg4oCUIHVzZSBDTFMgdG9rZW4gb3IgZ2xvYmFsIGF2ZyBwb29sXG4gICAgICAgICAgICBpZiBmZWF0cy5kaW0oKSBcdTAwM2UgMjpcbiAgICAgICAgICAgICAgICBmZWF0cyA9IGZlYXRzLmZsYXR0ZW4oMSkgICAgICAgICAgICMgZmxhdHRlbiBzcGF0aWFsIGRpbXMgaWYgbmVlZGVkXG4gICAgICAgICAgICBmZWF0c19saXN0LmFwcGVuZChmZWF0cy5jcHUoKS5udW1weSgpKVxuICAgICAgICAgICAgbGFiZWxfbGlzdC5hcHBlbmQobGFiZWxzLm51bXB5KCkpXG4gICAgcmV0dXJuIG5wLnZzdGFjayhmZWF0c19saXN0KSwgbnAuY29uY2F0ZW5hdGUobGFiZWxfbGlzdClcblxuXG5kZWYgbGluZWFyX3Byb2JlX3NrbGVhcm4oYmFja2JvbmUsIHRyYWluX2xvYWRlciwgdmFsX2xvYWRlciwgZGV2aWNlPVx1MDAyN2N1ZGFcdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgICAgICAgbWF4X2l0ZXI9MTAwMCwgQz0wLjMxNik6XG4gICAgXCJcIlwiRnJvemVuIGJhY2tib25lICsgc2tsZWFybiBMb2dpc3RpY1JlZ3Jlc3Npb24gbGluZWFyIHByb2JlLlwiXCJcIlxuICAgIHByaW50KFx1MDAyN0V4dHJhY3RpbmcgdHJhaW4gZmVhdHVyZXMuLi5cdTAwMjcpXG4gICAgWF90cmFpbiwgeV90cmFpbiA9IGV4dHJhY3RfZmVhdHVyZXMoYmFja2JvbmUsIHRyYWluX2xvYWRlciwgZGV2aWNlKVxuICAgIHByaW50KFx1MDAyN0V4dHJhY3RpbmcgdmFsIGZlYXR1cmVzLi4uXHUwMDI3KVxuICAgIFhfdmFsLCAgIHlfdmFsICAgPSBleHRyYWN0X2ZlYXR1cmVzKGJhY2tib25lLCB2YWxfbG9hZGVyLCBkZXZpY2UpXG5cbiAgICAjIEwyLW5vcm1hbGlzZSBmZWF0dXJlcyAoaW1wb3J0YW50IGZvciBjb3NpbmUtYmFzZWQgU1NMIHJlcHJlc2VudGF0aW9ucylcbiAgICBzY2FsZXIgID0gU3RhbmRhcmRTY2FsZXIod2l0aF9zdGQ9RmFsc2UpXG4gICAgWF90cmFpbiA9IHNjYWxlci5maXRfdHJhbnNmb3JtKFhfdHJhaW4pXG4gICAgWF92YWwgICA9IHNjYWxlci50cmFuc2Zvcm0oWF92YWwpXG4gICAgbm9ybXMgICA9IG5wLmxpbmFsZy5ub3JtKFhfdHJhaW4sIGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcbiAgICBYX3RyYWluIC89IG5wLmNsaXAobm9ybXMsIDFlLTgsIE5vbmUpXG4gICAgbm9ybXMgICA9IG5wLmxpbmFsZy5ub3JtKFhfdmFsLCBheGlzPTEsIGtlZXBkaW1zPVRydWUpXG4gICAgWF92YWwgICAvPSBucC5jbGlwKG5vcm1zLCAxZS04LCBOb25lKVxuXG4gICAgY2xmID0gTG9naXN0aWNSZWdyZXNzaW9uKG1heF9pdGVyPW1heF9pdGVyLCBDPUMsIHNvbHZlcj1cdTAwMjdsYmZnc1x1MDAyNyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbXVsdGlfY2xhc3M9XHUwMDI3bXVsdGlub21pYWxcdTAwMjcsIG5fam9icz0tMSlcbiAgICBjbGYuZml0KFhfdHJhaW4sIHlfdHJhaW4pXG4gICAgYWNjID0gY2xmLnNjb3JlKFhfdmFsLCB5X3ZhbClcbiAgICBwcmludChmXHUwMDI3TGluZWFyIHByb2JlIGFjY3VyYWN5OiB7YWNjKjEwMDouMmZ9JVx1MDAyNylcbiAgICByZXR1cm4gYWNjXG5cblxucHJpbnQoXHUwMDI3TGluZWFyIHByb2JlOiBmcmVlemUgYmFja2JvbmUsIHRyYWluIHNrbGVhcm4gTG9nUmVnIG9uIGV4dHJhY3RlZCBmZWF0dXJlcy5cdTAwMjcpXG5wcmludChcdTAwMjdUaXA6IEwyLW5vcm1hbGlzZSBmZWF0dXJlcyBiZWZvcmUgTG9nUmVnIGZvciBjb250cmFzdGl2ZSBTU0wgbWV0aG9kcy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmluZS1UdW5pbmcg4oCUIENlaWxpbmcgUGVyZm9ybWFuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZpbmUtdHVuaW5nIHVuZnJlZXplcyB0aGUgZW50aXJlIGVuY29kZXIgYW5kIHRyYWlucyBhbGwgcGFyYW1ldGVycyBqb2ludGx5IHdpdGggdGhlIGxpbmVhciBoZWFkLiBUaGlzIGFsd2F5cyBhY2hpZXZlcyBoaWdoZXIgYWNjdXJhY3kgdGhhbiBsaW5lYXIgcHJvYmUgYmVjYXVzZSB0aGUgZW5jb2RlciBjYW4gYWRhcHQgaXRzIHJlcHJlc2VudGF0aW9ucyB0byB0aGUgZG93bnN0cmVhbSB0YXNrLiBUaGUgZ2FwIGJldHdlZW4gbGluZWFyIHByb2JlIGFuZCBmaW5lLXR1bmUgYWNjdXJhY3kgaW5kaWNhdGVzIGhvdyBcdTAwMjd0YXNrLXJlYWR5XHUwMDI3IHRoZSByZXByZXNlbnRhdGlvbiBpczogYSBzbWFsbCBnYXAgbWVhbnMgdGhlIGZyb3plbiBmZWF0dXJlcyBhcmUgbmVhcmx5IG9wdGltYWwgKERJTk92MiBjbG9zZXMgdGhpcyBnYXAgc3Vic3RhbnRpYWxseSk7IGEgbGFyZ2UgZ2FwIG1lYW5zIHRoZSByZXByZXNlbnRhdGlvbiBuZWVkcyB0YXNrLXNwZWNpZmljIHJlc3RydWN0dXJpbmcgKE1BRSBmZWF0dXJlcywgd2hpY2ggYXJlIGRlc2lnbmVkIGZvciByZWNvbnN0cnVjdGlvbiwgc2hvdyBsYXJnZSBsaW5lYXItdG8tZmluZXR1bmUgZ2FwcykuIEZpbmUtdHVuaW5nIHVzZXMgYSBsb3dlciBsZWFybmluZyByYXRlIGZvciBiYWNrYm9uZSBsYXllcnMgdGhhbiBmb3IgdGhlIG5ld2x5IGFkZGVkIGhlYWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFMb2FkZXJcblxuXG5kZWYgZmluZXR1bmVfc3NsX21vZGVsKGJhY2tib25lLCB0cmFpbl9sb2FkZXIsIHZhbF9sb2FkZXIsXG4gICAgICAgICAgICAgICAgICAgICAgIG51bV9jbGFzc2VzOiBpbnQgPSAxMDAwLCBmZWF0X2RpbTogaW50ID0gNzY4LFxuICAgICAgICAgICAgICAgICAgICAgICBiYWNrYm9uZV9scjogZmxvYXQgPSAxZS01LCBoZWFkX2xyOiBmbG9hdCA9IDFlLTMsXG4gICAgICAgICAgICAgICAgICAgICAgIGVwb2NoczogaW50ID0gMzAsIGRldmljZTogc3RyID0gXHUwMDI3Y3VkYVx1MDAyNyk6XG4gICAgXCJcIlwiRmluZS10dW5lIFNTTCBiYWNrYm9uZTogbG93ZXIgTFIgZm9yIGJhY2tib25lLCBoaWdoZXIgZm9yIG5ldyBoZWFkLlwiXCJcIlxuICAgIGhlYWQgPSBubi5MaW5lYXIoZmVhdF9kaW0sIG51bV9jbGFzc2VzKS50byhkZXZpY2UpXG4gICAgYmFja2JvbmUgPSBiYWNrYm9uZS50byhkZXZpY2UpXG5cbiAgICAjIFNlcGFyYXRlIHBhcmFtZXRlciBncm91cHMgd2l0aCBkaWZmZXJlbnQgTFJzXG4gICAgb3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbVcoW1xuICAgICAgICB7XHUwMDI3cGFyYW1zXHUwMDI3OiBiYWNrYm9uZS5wYXJhbWV0ZXJzKCksIFx1MDAyN2xyXHUwMDI3OiBiYWNrYm9uZV9sciwgXHUwMDI3d2VpZ2h0X2RlY2F5XHUwMDI3OiAwLjA1fSxcbiAgICAgICAge1x1MDAyN3BhcmFtc1x1MDAyNzogaGVhZC5wYXJhbWV0ZXJzKCksICAgICBcdTAwMjdsclx1MDAyNzogaGVhZF9sciwgICAgIFx1MDAyN3dlaWdodF9kZWNheVx1MDAyNzogMC4wfSxcbiAgICBdKVxuICAgIHNjaGVkdWxlciA9IHRvcmNoLm9wdGltLmxyX3NjaGVkdWxlci5Db3NpbmVBbm5lYWxpbmdMUihvcHRpbWl6ZXIsIGVwb2NocylcbiAgICBjcml0ZXJpb24gPSBubi5Dcm9zc0VudHJvcHlMb3NzKGxhYmVsX3Ntb290aGluZz0wLjEpXG5cbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgYmFja2JvbmUudHJhaW4oKTsgaGVhZC50cmFpbigpXG4gICAgICAgIGZvciBpbWdzLCBsYWJlbHMgaW4gdHJhaW5fbG9hZGVyOlxuICAgICAgICAgICAgaW1ncywgbGFiZWxzID0gaW1ncy50byhkZXZpY2UpLCBsYWJlbHMudG8oZGV2aWNlKVxuICAgICAgICAgICAgZmVhdHMgID0gYmFja2JvbmUoaW1ncykuZmxhdHRlbigxKSAgICMgKEIsIGZlYXRfZGltKVxuICAgICAgICAgICAgbG9naXRzID0gaGVhZChmZWF0cylcbiAgICAgICAgICAgIGxvc3MgICA9IGNyaXRlcmlvbihsb2dpdHMsIGxhYmVscylcbiAgICAgICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgICAgICAgICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgICAgICAgICBubi51dGlscy5jbGlwX2dyYWRfbm9ybV8oYmFja2JvbmUucGFyYW1ldGVycygpLCBtYXhfbm9ybT0xLjApXG4gICAgICAgICAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgIHNjaGVkdWxlci5zdGVwKClcbiAgICAgICAgaWYgKGVwb2NoICsgMSkgJSAxMCA9PSAwOlxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyNyAgRXBvY2gge2Vwb2NoKzF9L3tlcG9jaHN9IGRvbmUuXHUwMDI3KVxuXG4gICAgIyBWYWxpZGF0aW9uXG4gICAgYmFja2JvbmUuZXZhbCgpOyBoZWFkLmV2YWwoKVxuICAgIGNvcnJlY3QgPSB0b3RhbCA9IDBcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZm9yIGltZ3MsIGxhYmVscyBpbiB2YWxfbG9hZGVyOlxuICAgICAgICAgICAgaW1ncywgbGFiZWxzID0gaW1ncy50byhkZXZpY2UpLCBsYWJlbHMudG8oZGV2aWNlKVxuICAgICAgICAgICAgcHJlZHMgPSBoZWFkKGJhY2tib25lKGltZ3MpLmZsYXR0ZW4oMSkpLmFyZ21heCgxKVxuICAgICAgICAgICAgY29ycmVjdCArPSAocHJlZHMgPT0gbGFiZWxzKS5zdW0oKS5pdGVtKClcbiAgICAgICAgICAgIHRvdGFsICAgKz0gbGFiZWxzLnNpemUoMClcbiAgICBhY2MgPSBjb3JyZWN0IC8gdG90YWxcbiAgICBwcmludChmXHUwMDI3RmluZS10dW5lIGFjY3VyYWN5OiB7YWNjKjEwMDouMmZ9JVx1MDAyNylcbiAgICByZXR1cm4gYWNjXG5cblxucHJpbnQoXHUwMDI3RmluZS10dW5lOiBsb3dlciBMUiBmb3IgU1NMIGJhY2tib25lLCBzdGFuZGFyZCBMUiBmb3IgdGFzayBoZWFkLlx1MDAyNylcbnByaW50KFx1MDAyN0xheWVyLXdpc2UgTFIgZGVjYXkgaXMgYWxzbyBjb21tb246IExSICo9IDAuNjVebGF5ZXJfZGVwdGhfZnJvbV9oZWFkLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJrLU5OIEV2YWx1YXRpb24g4oCUIE5vIFRyYWluaW5nIFJlcXVpcmVkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJrLU5lYXJlc3QgTmVpZ2hib3VyIGV2YWx1YXRpb24gcmVxdWlyZXMgbm8gdHJhaW5pbmcgYWZ0ZXIgU1NMIHByZXRyYWluaW5nLiBBbGwgdHJhaW5pbmcgc2V0IGltYWdlcyBhcmUgZW5jb2RlZCwgYW5kIHRoZWlyIGZlYXR1cmVzIGFyZSBzdG9yZWQgaW4gYW4gaW5kZXguIEEgdGVzdCBpbWFnZSBpcyBjbGFzc2lmaWVkIGJ5IGZpbmRpbmcgaXRzIGsgbmVhcmVzdCBuZWlnaGJvdXJzIGluIGZlYXR1cmUgc3BhY2UgKGJ5IGNvc2luZSBzaW1pbGFyaXR5KSBhbmQgdGFraW5nIGEgbWFqb3JpdHkgdm90ZS4gay1OTiBhY2N1cmFjeSBpcyB0aGUgZmFzdGVzdCB3YXkgdG8gYXNzZXNzIHdoZXRoZXIgU1NMIGZlYXR1cmVzIGFyZSBzZW1hbnRpY2FsbHkgbWVhbmluZ2Z1bDogaWYgc2VtYW50aWNhbGx5IHNpbWlsYXIgaW1hZ2VzIGNsdXN0ZXIgdG9nZXRoZXIgaW4gdGhlIGZlYXR1cmUgc3BhY2UsIGstTk4gd2lsbCBwZXJmb3JtIHdlbGwuIERJTk8gZmVhdHVyZXMgZmFtb3VzbHkgcHJvZHVjZSBrLU5OIGFjY3VyYWN5IG9mIDc4JSBvbiBJbWFnZU5ldCB3aXRoIGs9MjAg4oCUIGNsb3NlIHRvIHN1cGVydmlzZWQgUmVzTmV0LTUwIOKAlCB1c2luZyBubyBsYWJlbGxlZCB0cmFpbmluZyBhdCBhbGwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbnRyeTpcbiAgICBpbXBvcnQgZmFpc3NcbiAgICBIQVNfRkFJU1MgPSBUcnVlXG5leGNlcHQgSW1wb3J0RXJyb3I6XG4gICAgSEFTX0ZBSVNTID0gRmFsc2VcbiAgICBwcmludChcdTAwMjdmYWlzcyBub3QgYXZhaWxhYmxlIOKAlCBmYWxsaW5nIGJhY2sgdG8gYnJ1dGUtZm9yY2UgY29zaW5lIGstTk4uXHUwMDI3KVxuXG5cbmRlZiBrbm5fZXZhbHVhdGUoYmFja2JvbmUsIHRyYWluX2xvYWRlciwgdmFsX2xvYWRlcixcbiAgICAgICAgICAgICAgICAgazogaW50ID0gMjAsIGRldmljZTogc3RyID0gXHUwMDI3Y3VkYVx1MDAyNyk6XG4gICAgXCJcIlwiay1OTiBldmFsdWF0aW9uIHVzaW5nIGZhaXNzIEluZGV4RmxhdElQIChjb3NpbmUgc2ltaWxhcml0eSB2aWEgTDIgbm9ybSkuXCJcIlwiXG4gICAgIyBFeHRyYWN0IGFuZCBMMi1ub3JtYWxpc2UgZmVhdHVyZXNcbiAgICBkZWYgZ2V0X2ZlYXRzKGxvYWRlcik6XG4gICAgICAgIGJhY2tib25lLmV2YWwoKVxuICAgICAgICBhbGxfZiwgYWxsX2wgPSBbXSwgW11cbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICBmb3IgaW1ncywgbGFiZWxzIGluIGxvYWRlcjpcbiAgICAgICAgICAgICAgICBmID0gYmFja2JvbmUoaW1ncy50byhkZXZpY2UpKVxuICAgICAgICAgICAgICAgIGYgPSBGLm5vcm1hbGl6ZShmLmZsYXR0ZW4oMSksIGRpbT0xKSAgICMgdW5pdCBub3JtIGZvciBjb3NpbmVcbiAgICAgICAgICAgICAgICBhbGxfZi5hcHBlbmQoZi5jcHUoKS5udW1weSgpKVxuICAgICAgICAgICAgICAgIGFsbF9sLmFwcGVuZChsYWJlbHMubnVtcHkoKSlcbiAgICAgICAgcmV0dXJuIG5wLnZzdGFjayhhbGxfZikuYXN0eXBlKFx1MDAyN2Zsb2F0MzJcdTAwMjcpLCBucC5jb25jYXRlbmF0ZShhbGxfbClcblxuICAgIHRyYWluX2ZlYXRzLCB0cmFpbl9sYWJlbHMgPSBnZXRfZmVhdHModHJhaW5fbG9hZGVyKVxuICAgIHZhbF9mZWF0cywgICB2YWxfbGFiZWxzICAgPSBnZXRfZmVhdHModmFsX2xvYWRlcilcbiAgICBEID0gdHJhaW5fZmVhdHMuc2hhcGVbMV1cblxuICAgIGlmIEhBU19GQUlTUzpcbiAgICAgICAgaW5kZXggPSBmYWlzcy5JbmRleEZsYXRJUChEKSAgICAgICAgICMgaW5uZXIgcHJvZHVjdCA9IGNvc2luZSBmb3IgTDItbm9ybWVkIHZlY3RvcnNcbiAgICAgICAgaW5kZXguYWRkKHRyYWluX2ZlYXRzKVxuICAgICAgICBfLCBJID0gaW5kZXguc2VhcmNoKHZhbF9mZWF0cywgaykgICAgIyAoTl92YWwsIGspIOKAlCBpbmRpY2VzIG9mIGsgbmVhcmVzdCBuZWlnaGJvdXJzXG4gICAgZWxzZTpcbiAgICAgICAgIyBCcnV0ZS1mb3JjZTogKE5fdmFsLCBOX3RyYWluKSBjb3NpbmUgc2ltaWxhcml0eSBtYXRyaXhcbiAgICAgICAgc2ltcyA9IHZhbF9mZWF0cyBAIHRyYWluX2ZlYXRzLlQgICAgICMgKE5fdmFsLCBOX3RyYWluKVxuICAgICAgICBJICAgID0gbnAuYXJnc29ydCgtc2ltcywgYXhpcz0xKVs6LCA6a10gICAjIHRvcC1rIGluZGljZXNcblxuICAgICMgTWFqb3JpdHkgdm90ZVxuICAgIGtubl9sYWJlbHMgPSB0cmFpbl9sYWJlbHNbSV0gICAgICAgICAgICAgIyAoTl92YWwsIGspXG4gICAgcHJlZHMgPSBucC5hcHBseV9hbG9uZ19heGlzKFxuICAgICAgICBsYW1iZGEgcm93OiBucC5iaW5jb3VudChyb3csIG1pbmxlbmd0aD1pbnQodHJhaW5fbGFiZWxzLm1heCgpKSsxKS5hcmdtYXgoKSxcbiAgICAgICAgYXhpcz0xLCBhcnI9a25uX2xhYmVsc1xuICAgIClcbiAgICBhY2MgPSAocHJlZHMgPT0gdmFsX2xhYmVscykubWVhbigpXG4gICAgcHJpbnQoZlx1MDAyN2stTk4gKGs9e2t9KSBhY2N1cmFjeToge2FjYyoxMDA6LjJmfSVcdTAwMjcpXG4gICAgcmV0dXJuIGFjY1xuXG5cbnByaW50KFx1MDAyN2stTk4gZXZhbDogZXh0cmFjdCBmZWF0dXJlcywgTDItbm9ybWFsaXNlLCBmYWlzcyBJbmRleEZsYXRJUCwgbWFqb3JpdHkgdm90ZS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VtaS1TdXBlcnZpc2VkIFByb3RvY29sIOKAlCAxJSBhbmQgMTAlIExhYmVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2VtaS1zdXBlcnZpc2VkIGV2YWx1YXRpb24gdGVzdHMgbGFiZWwgZWZmaWNpZW5jeTogaG93IHdlbGwgZG9lcyB0aGUgU1NMIG1vZGVsIHBlcmZvcm0gd2hlbiBvbmx5IDElIG9yIDEwJSBvZiBJbWFnZU5ldCBsYWJlbHMgYXJlIGF2YWlsYWJsZT8gVGhlIHByb3RvY29sIGlzIHN0YW5kYXJkaXNlZDogKDEpIHNlbGVjdCBhIGJhbGFuY2VkIHN1YnNldCDigJQgZXF1YWwgbnVtYmVyIG9mIGV4YW1wbGVzIHBlciBjbGFzczsgKDIpIGZyZWV6ZSB0aGUgU1NMIGJhY2tib25lOyAoMykgZmluZS10dW5lIG9ubHkgdGhlIGxpbmVhciBoZWFkIChvciBhIGxpZ2h0IE1MUCBoZWFkKSBvbiB0aGUgbGFiZWxsZWQgc3Vic2V0OyAoNCkgZXZhbHVhdGUgb24gdGhlIGZ1bGwgdmFsaWRhdGlvbiBzZXQuIFRoaXMgcHJvdG9jb2wgaXNvbGF0ZXMgdGhlIGNvbnRyaWJ1dGlvbiBvZiB0aGUgU1NMIGZlYXR1cmVzIGZyb20gc3VwZXJ2aXNlZCBkYXRhIHF1YW50aXR5LiBTaW1DTFIgdjIgc2hvd2VkIDc0JSB0b3AtMSB3aXRoIG9ubHkgMSUgbGFiZWxzIHZpYSBkaXN0aWxsYXRpb247IERJTk92MiBleGNlZWRzIDgwJSB3aXRoIDEwJSBsYWJlbHMgdXNpbmcganVzdCBhIGxpbmVhciBsYXllci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgU3Vic2V0LCBEYXRhTG9hZGVyXG5mcm9tIHRvcmNodmlzaW9uLmRhdGFzZXRzIGltcG9ydCBJbWFnZUZvbGRlclxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVmYXVsdGRpY3RcblxuXG5kZWYgc2VsZWN0X2JhbGFuY2VkX3N1YnNldChkYXRhc2V0OiBJbWFnZUZvbGRlciwgZnJhY3Rpb246IGZsb2F0ID0gMC4wMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHNlZWQ6IGludCA9IDQyKSAtXHUwMDNlIFN1YnNldDpcbiAgICBcIlwiXCJTZWxlY3QgYSBjbGFzcy1iYWxhbmNlZCBmcmFjdGlvbiBvZiBhIGRhdGFzZXQuXG4gICAgUmV0dXJucyBhIFN1YnNldCB3aXRoIGZyYWN0aW9uKmxlbihkYXRhc2V0KSBzYW1wbGVzLCBlcXVhbGx5IGRpc3RyaWJ1dGVkLlxuICAgIFwiXCJcIlxuICAgIHJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyhzZWVkKVxuICAgIGNsYXNzX3RvX2luZGljZXMgPSBkZWZhdWx0ZGljdChsaXN0KVxuICAgIGZvciBpZHgsIChfLCBsYWJlbCkgaW4gZW51bWVyYXRlKGRhdGFzZXQuc2FtcGxlcyk6XG4gICAgICAgIGNsYXNzX3RvX2luZGljZXNbbGFiZWxdLmFwcGVuZChpZHgpXG5cbiAgICBzZWxlY3RlZCA9IFtdXG4gICAgZm9yIGxhYmVsLCBpbmRpY2VzIGluIGNsYXNzX3RvX2luZGljZXMuaXRlbXMoKTpcbiAgICAgICAgbl9zZWxlY3QgPSBtYXgoMSwgaW50KGxlbihpbmRpY2VzKSAqIGZyYWN0aW9uKSlcbiAgICAgICAgY2hvc2VuICAgPSBybmcuY2hvaWNlKGluZGljZXMsIHNpemU9bl9zZWxlY3QsIHJlcGxhY2U9RmFsc2UpXG4gICAgICAgIHNlbGVjdGVkLmV4dGVuZChjaG9zZW4udG9saXN0KCkpXG5cbiAgICBybmcuc2h1ZmZsZShzZWxlY3RlZClcbiAgICBwcmludChmXHUwMDI3U2VsZWN0ZWQge2xlbihzZWxlY3RlZCl9IHNhbXBsZXMgKHtmcmFjdGlvbioxMDA6LjFmfSUpIFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjdmcm9tIHtsZW4oZGF0YXNldC5jbGFzc2VzKX0gY2xhc3Nlcy5cdTAwMjcpXG4gICAgcmV0dXJuIFN1YnNldChkYXRhc2V0LCBzZWxlY3RlZClcblxuXG5kZWYgc2VtaXN1cF9ldmFsKGJhY2tib25lLCBmdWxsX2RhdGFzZXQ6IEltYWdlRm9sZGVyLCB2YWxfbG9hZGVyOiBEYXRhTG9hZGVyLFxuICAgICAgICAgICAgICAgICBmcmFjdGlvbjogZmxvYXQgPSAwLjAxLCBmZWF0X2RpbTogaW50ID0gNzY4LFxuICAgICAgICAgICAgICAgICBudW1fY2xhc3NlczogaW50ID0gMTAwMCwgZXBvY2hzOiBpbnQgPSAzMCwgZGV2aWNlOiBzdHIgPSBcdTAwMjdjdWRhXHUwMDI3KTpcbiAgICBcIlwiXCJTZW1pLXN1cGVydmlzZWQgZXZhbHVhdGlvbjogZnJlZXplIGJhY2tib25lLCB0cmFpbiBsaW5lYXIgaGVhZCBvbiBmcmFjdGlvbiUgbGFiZWxzLlwiXCJcIlxuICAgIHN1YnNldCAgPSBzZWxlY3RfYmFsYW5jZWRfc3Vic2V0KGZ1bGxfZGF0YXNldCwgZnJhY3Rpb24pXG4gICAgc3ViX2xvYWRlciA9IERhdGFMb2FkZXIoc3Vic2V0LCBiYXRjaF9zaXplPTI1Niwgc2h1ZmZsZT1UcnVlLCBudW1fd29ya2Vycz00KVxuXG4gICAgYmFja2JvbmUuZXZhbCgpLnRvKGRldmljZSlcbiAgICBmb3IgcCBpbiBiYWNrYm9uZS5wYXJhbWV0ZXJzKCk6XG4gICAgICAgIHAucmVxdWlyZXNfZ3JhZF8oRmFsc2UpXG5cbiAgICBoZWFkID0gdG9yY2gubm4uTGluZWFyKGZlYXRfZGltLCBudW1fY2xhc3NlcykudG8oZGV2aWNlKVxuICAgIG9wdCAgPSB0b3JjaC5vcHRpbS5BZGFtVyhoZWFkLnBhcmFtZXRlcnMoKSwgbHI9MWUtMywgd2VpZ2h0X2RlY2F5PTAuMClcbiAgICBjcml0ID0gdG9yY2gubm4uQ3Jvc3NFbnRyb3B5TG9zcygpXG5cbiAgICBmb3IgXyBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICBoZWFkLnRyYWluKClcbiAgICAgICAgZm9yIGltZ3MsIGxhYmVscyBpbiBzdWJfbG9hZGVyOlxuICAgICAgICAgICAgaW1ncywgbGFiZWxzID0gaW1ncy50byhkZXZpY2UpLCBsYWJlbHMudG8oZGV2aWNlKVxuICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICAgICAgZmVhdHMgPSBiYWNrYm9uZShpbWdzKS5mbGF0dGVuKDEpXG4gICAgICAgICAgICBsb3NzID0gY3JpdChoZWFkKGZlYXRzKSwgbGFiZWxzKVxuICAgICAgICAgICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcblxuICAgIGhlYWQuZXZhbCgpXG4gICAgY29ycmVjdCA9IHRvdGFsID0gMFxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgaW1ncywgbGFiZWxzIGluIHZhbF9sb2FkZXI6XG4gICAgICAgICAgICBpbWdzLCBsYWJlbHMgPSBpbWdzLnRvKGRldmljZSksIGxhYmVscy50byhkZXZpY2UpXG4gICAgICAgICAgICBjb3JyZWN0ICs9IChoZWFkKGJhY2tib25lKGltZ3MpLmZsYXR0ZW4oMSkpLmFyZ21heCgxKSA9PSBsYWJlbHMpLnN1bSgpLml0ZW0oKVxuICAgICAgICAgICAgdG90YWwgICArPSBsYWJlbHMuc2l6ZSgwKVxuICAgIHByaW50KGZcdTAwMjdTZW1pLXN1cCB7ZnJhY3Rpb24qMTAwOi4wZn0lIGFjY3VyYWN5OiB7Y29ycmVjdC90b3RhbCoxMDA6LjJmfSVcdTAwMjcpXG4gICAgcmV0dXJuIGNvcnJlY3QgLyB0b3RhbFxuXG5cbnByaW50KFx1MDAyN1NlbWktc3VwZXJ2aXNlZDogYmFsYW5jZWQgc3Vic2V0IHNlbGVjdGlvbiAtXHUwMDNlIGZyZWV6ZSBiYWNrYm9uZSAtXHUwMDNlIHRyYWluIGxpbmVhciBoZWFkLlx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlN0YW5kYXJkaXNlIEV2YWx1YXRpb24gSHlwZXJwYXJhbWV0ZXJzIGZvciBGYWlyIENvbXBhcmlzb24iLCJjb250ZW50IjoiU1NMIHBhcGVycyBvZnRlbiByZXBvcnQgZmF2b3JhYmxlIGV2YWx1YXRpb24gbnVtYmVycyBieSB0dW5pbmcgZXZhbHVhdGlvbi1zcGVjaWZpYyBoeXBlcnBhcmFtZXRlcnMgKGxlYXJuaW5nIHJhdGUsIGVwb2NocywgYXVnbWVudGF0aW9uIGR1cmluZyBldmFsdWF0aW9uKS4gRmFpciBjb21wYXJpc29uIHJlcXVpcmVzOiAoMSkgc2FtZSBudW1iZXIgb2YgbGluZWFyIHByb2JlIGVwb2NocyAoMTAwIHN0YW5kYXJkKTsgKDIpIHNhbWUgb3B0aW1pemVyIChMQkZHUyBvciBTR0QrbW9tZW50dW0pOyAoMykgc2FtZSBhdWdtZW50YXRpb24gZHVyaW5nIGZlYXR1cmUgZXh0cmFjdGlvbiAocmVzaXplICsgY2VudGVyIGNyb3AsIG5vIHJhbmRvbSBhdWdtZW50YXRpb24pOyAoNCkgc2FtZSBmcmFjdGlvbiBhbmQgc2VlZCBmb3Igc2VtaS1zdXBlcnZpc2VkIHNwbGl0cy4gVGhlIERJTk92MiBwYXBlciBwcm92aWRlcyBhIHN0YW5kYXJkaXNlZCBldmFsdWF0aW9uIGNvZGViYXNlIOKAlCB1c2UgaXQgYXMgdGhlIHJlZmVyZW5jZSBpbXBsZW1lbnRhdGlvbiB3aGVuIGNvbXBhcmluZyBTU0wgbWV0aG9kcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFuc2ZlciBMZWFybmluZyBhbmQgRG9tYWluIFNoaWZ0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZXlvbmQgSW1hZ2VOZXQsIFNTTCByZXByZXNlbnRhdGlvbnMgc2hvdWxkIGdlbmVyYWxpc2UgdG8gb3RoZXIgZG9tYWlucy4gU3RhbmRhcmQgdHJhbnNmZXIgYmVuY2htYXJrcyBpbmNsdWRlOiBDSUZBUi0xMDAgKDMyw5czMiBvYmplY3QgcmVjb2duaXRpb24pLCBGbG93ZXJzLTEwMiAoZmluZS1ncmFpbmVkIGZsb3dlcnMpLCBGb29kLTEwMSAoZmluZS1ncmFpbmVkIGZvb2QgY2F0ZWdvcmllcyksIGFuZCBDVUItMjAwIChiaXJkIHNwZWNpZXMg4oCUIHJlcXVpcmVzIGZpbmUtZ3JhaW5lZCBkaXNjcmltaW5hdGlvbikuIFRoZSB0cmFuc2ZlciBldmFsdWF0aW9uIHByb3RvY29sIGlzIHRoZSBzYW1lIGFzIGxpbmVhciBwcm9iZTogZnJlZXplIGJhY2tib25lLCB0cmFpbiBsaW5lYXIgaGVhZCwgbWVhc3VyZSB0b3AtMS4gU3Ryb25nIFNTTCBtZXRob2RzIChESU5PdjIsIERJTk8pIGNvbnNpc3RlbnRseSBvdXRwZXJmb3JtIHN1cGVydmlzZWQgSW1hZ2VOZXQgcHJldHJhaW5pbmcgb24gZmluZS1ncmFpbmVkIGJlbmNobWFya3MgYmVjYXVzZSB0aGVpciBmZWF0dXJlcyBhcmUgbW9yZSBkaXZlcnNlIGFuZCBsZXNzIGJpYXNlZCB0b3dhcmQgSW1hZ2VOZXQtc3BlY2lmaWMgY2F0ZWdvcmllcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNJRkFSLTEwMCB0cmFuc2ZlcjogRElOT3YyLVZpVC1MIH45NCUgbGluZWFyIHByb2JlIChSZXNOZXQtNTAgc3VwZXJ2aXNlZDogfjg3JSkuIiwiRmxvd2Vycy0xMDI6IFNTTCBtZXRob2RzIG9mdGVuIG1hdGNoIG9yIGV4Y2VlZCBzdXBlcnZpc2VkLCBhcyBJbWFnZU5ldCBoYXMgZmV3IGZsb3dlciBjbGFzc2VzLiIsIkNVQi0yMDA6IGZpbmUtZ3JhaW5lZCBkaXNjcmltaW5hdGlvbiBmYXZvcnMgcmljaCBwYXRjaC1sZXZlbCBmZWF0dXJlcyAoRElOT3YyLCBpQk9UKS4iLCJNZWRpY2FsIGltYWdpbmc6IFNTTCBwcmV0cmFpbmVkIG9uIG5hdHVyYWwgaW1hZ2VzIHRyYW5zZmVycyB3ZWxsIHdpdGggb25seSAxMDAtNTAwIGxhYmVsbGVkIGV4YW1wbGVzLiIsIlNhdGVsbGl0ZSBpbWFnZXJ5OiBkb21haW4gZ2FwIGlzIGxhcmdlIOKAlCBjb25zaWRlciBkb21haW4tc3BlY2lmaWMgU1NMIHByZXRyYWluaW5nIGZyb20gc2NyYXRjaC4iLCJrLU5OIHRyYW5zZmVyOiBoaWdoIGstTk4gYWNjdXJhY3kgb24gdHJhbnNmZXIgZGF0YXNldHMgPSBmZWF0dXJlIGRpdmVyc2l0eSwgbm90IGp1c3QgSW1hZ2VOZXQgb3ZlcmZpdHRpbmcuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV2YWx1YXRpb24gUHJvdG9jb2wgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm90b2NvbCIsIkxhYmVscyBOZWVkZWQiLCJDb21wdXRlIiwiV2hhdCBJdCBNZWFzdXJlcyIsIlN0YW5kYXJkIERhdGFzZXQiXSwicm93cyI6W1siTGluZWFyIHByb2JlIiwiRnVsbCB0cmFpbiBzZXQiLCJMb3cgKGZyb3plbiBmZWF0dXJlcyArIGxpbmVhcikiLCJGcm96ZW4gcmVwcmVzZW50YXRpb24gcXVhbGl0eSIsIkltYWdlTmV0IHRvcC0xIl0sWyJGaW5lLXR1bmluZyIsIkZ1bGwgdHJhaW4gc2V0IiwiSGlnaCAoZnVsbCBiYWNrcHJvcCkiLCJUYXNrIGNlaWxpbmcgLyBhZGFwdGFiaWxpdHkiLCJJbWFnZU5ldCB0b3AtMSJdLFsiay1OTiAoaz0yMCkiLCJGdWxsIHRyYWluIHNldCAobm8gdHJhaW5pbmcpIiwiVmVyeSBsb3cgKGluZGV4IGxvb2t1cCkiLCJGZWF0dXJlIGdlb21ldHJ5IC8gY2x1c3RlcmluZyIsIkltYWdlTmV0IHRvcC0xIl0sWyJTZW1pLXN1cGVydmlzZWQgKDElKSIsIjElIG9mIHRyYWluIHNldCAofjEzSyBmb3IgSW1hZ2VOZXQpIiwiTG93IChsaW5lYXIgaGVhZCBvbmx5KSIsIkxhYmVsIGVmZmljaWVuY3kiLCJJbWFnZU5ldCB0b3AtMSJdLFsiU2VtaS1zdXBlcnZpc2VkICgxMCUpIiwiMTAlIG9mIHRyYWluIHNldCAofjEyOEspIiwiTG93IiwiTGFiZWwgZWZmaWNpZW5jeSBhdCBzY2FsZSIsIkltYWdlTmV0IHRvcC0xIl0sWyJUcmFuc2ZlciAobGluZWFyKSIsIlRhcmdldCBkb21haW4gZnVsbCBzZXQiLCJMb3cgKGZyb3plbiBmZWF0dXJlcykiLCJHZW5lcmFsaXphdGlvbiB0byBuZXcgZG9tYWlucyIsIkNJRkFSLTEwMCAvIEZsb3dlcnMgLyBDVUIiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlbGF0aW9uc2hpcCBiZXR3ZWVuIHRoZXNlIHByb3RvY29scyB0ZWxscyBhIHN0b3J5IGFib3V0IGEgcmVwcmVzZW50YXRpb24uIExhcmdlIGxpbmVhci10by1maW5ldHVuZSBnYXA6IHJlcHJlc2VudGF0aW9uIG5lZWRzIHRhc2stc3BlY2lmaWMgcmVzdHJ1Y3R1cmluZyAoTUFFLCBwaXhlbCByZWNvbnN0cnVjdGlvbiBtZXRob2RzKS4gU21hbGwgZ2FwOiByZXByZXNlbnRhdGlvbiBpcyBhbHJlYWR5IHdlbGwtb3JnYW5pc2VkIGZvciB0aGUgZG93bnN0cmVhbSB0YXNrIChESU5PdjIsIERJTk8pLiBIaWdoIGstTk4gYnV0IGxvd2VyIGxpbmVhciBwcm9iZTogZmVhdHVyZXMgZm9ybSBjbHVzdGVycyBidXQgYXJlIG5vdCBsaW5lYXJseSBzZXBhcmFibGUgKHNvbWUgY29udHJhc3RpdmUgbWV0aG9kcykuIExvdyBrLU5OIGJ1dCBnb29kIGxpbmVhciBwcm9iZSBhZnRlciB0cmFpbmluZzogZmVhdHVyZXMgYXJlIGxpbmVhcmx5IHNlcGFyYWJsZSBidXQgbm90IG5hdHVyYWxseSBjbHVzdGVyZWQg4oCUIHRoZSBsaW5lYXIgbGF5ZXIgbGVhcm5zIGEgbm9uLXRyaXZpYWwgbWFwcGluZy4gVHJhY2tpbmcgYWxsIGZvdXIgbWV0cmljcyBwcm92aWRlcyBhIGNvbXBsZXRlIHBpY3R1cmUgb2YgU1NMIHJlcHJlc2VudGF0aW9uIHF1YWxpdHkuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJCZXN0IHByYWN0aWNlOiBhbHdheXMgcmVwb3J0IGxpbmVhciBwcm9iZSBBTkQgZmluZS10dW5lIOKAlCByZXBvcnRpbmcgb25seSBmaW5lLXR1bmUgaGlkZXMgcmVwcmVzZW50YXRpb24gcXVhbGl0eS4iLCJrLU5OIGlzIGZyZWUgdG8gY29tcHV0ZSBvbmNlIGZlYXR1cmVzIGFyZSBleHRyYWN0ZWQg4oCUIGluY2x1ZGUgaXQgYXMgYSBzYW5pdHkgY2hlY2sgaW4gZXZlcnkgZXhwZXJpbWVudC4iLCJVc2UgdGhlIHNhbWUgZmVhdHVyZSBleHRyYWN0aW9uIHRyYW5zZm9ybTogMjU2cHggcmVzaXplLCAyMjRweCBjZW50ZXIgY3JvcCwgSW1hZ2VOZXQgbm9ybWFsaXNhdGlvbi4iLCJSZXBvcnQgc3RhbmRhcmQgZGV2aWF0aW9uIG92ZXIgMyBzZWVkcyBmb3Igc2VtaS1zdXBlcnZpc2VkIGV2YWx1YXRpb25zIOKAlCBoaWdoIHZhcmlhbmNlIGlzIGNvbW1vbi4iLCJESU5PdjIgZXZhbHVhdGlvbiBjb2RlYmFzZTogZ2l0aHViLmNvbS9mYWNlYm9va3Jlc2VhcmNoL2Rpbm92Mi90cmVlL21haW4vZGlub3YyL2V2YWwg4oCUIHVzZSBhcyByZWZlcmVuY2UuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNob29zaW5nIHRoZSBSaWdodCBFdmFsdWF0aW9uIFByb3RvY29sIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcmlnaHQgZXZhbHVhdGlvbiBwcm90b2NvbCBkZXBlbmRzIG9uIHRoZSBkZXBsb3ltZW50IHNjZW5hcmlvLiBJZiB0aGUgZW5jb2RlciB3aWxsIGJlIGZyb3plbiBpbiBwcm9kdWN0aW9uIChlbWJlZGRpbmcgc2VydmljZSwgc2VhcmNoIGluZGV4KSwgbGluZWFyIHByb2JlIGFjY3VyYWN5IGlzIHRoZSBtb3N0IHJlbGV2YW50IG1ldHJpYyDigJQgb3B0aW1pc2UgZm9yIGl0LiBJZiB0aGUgZW5jb2RlciB3aWxsIGJlIGZpbmUtdHVuZWQgcGVyLXRhc2sgKHRoZSBjb21tb24gY2FzZSksIGxpbmVhciBwcm9iZSBhY2N1cmFjeSBpcyBhIHByb3h5IGJ1dCBmaW5lLXR1bmUgYWNjdXJhY3kgaXMgdGhlIHRydWUgdGFyZ2V0LiBrLU5OIGFjY3VyYWN5IGlzIHRoZSBmYXN0ZXN0IGRpYWdub3N0aWM6IGl0IHJldmVhbHMgd2hldGhlciBmZWF0dXJlcyBhcmUgZ2VvbWV0cmljYWxseSBtZWFuaW5nZnVsIHdpdGhvdXQgYW55IHRyYWluaW5nLiBGb3IgcmVzb3VyY2UtY29uc3RyYWluZWQgZW52aXJvbm1lbnRzIHdpdGggZmV3IGxhYmVscywgc2VtaS1zdXBlcnZpc2VkIDElIGFjY3VyYWN5IHJldmVhbHMgdGhlIG1vc3QgaW1wb3J0YW50IHByb3BlcnR5IOKAlCBob3cgbXVjaCBhIG1vZGVsIHJlZHVjZXMgbGFiZWxsaW5nIGNvc3QuIFJlcG9ydCBhbGwgZm91ciBmb3IgcHVibGlzaGFibGUgd29yazsgc3RhcnQgd2l0aCBrLU5OIGZvciBxdWljayBpdGVyYXRpb24uIn1d"
---
# Downstream Evaluation — Linear Probe, Fine-Tuning, and k-NN

Evaluating self-supervised learning is as important as the training objective itself. A representation that performs well under one evaluation protocol may fail another — revealing different aspects of what the encoder has learned. The field has converged on four standard protocols: linear probing (frozen encoder, linear classifier), full fine-tuning (unfreeze encoder), k-NN evaluation (no training at all), and semi-supervised learning (limited labels). Each measures something different: linear probe measures representation quality; fine-tuning measures learning capacity; k-NN measures feature geometry; semi-supervised measures label efficiency.

## Linear Probe — Measuring Representation Quality

Linear evaluation is the gold standard for measuring the quality of self-supervised representations. The encoder is frozen completely (no gradient through its parameters). A single linear layer is trained on top of the frozen features using the labelled training set. The resulting top-1 accuracy on the validation set measures how linearly separable the features are — a high score indicates the encoder has organised semantic categories into distinct, linearly separable regions of the feature space without any label supervision. This is the most constrained protocol, making it the fairest measure of what SSL actually learned.

```python
import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader


def extract_features(backbone, dataloader, device='cuda'):
    """Extract frozen features from SSL backbone. Returns (features, labels) numpy arrays."""
    backbone.eval().to(device)
    for p in backbone.parameters():
        p.requires_grad_(False)

    feats_list, label_list = [], []
    with torch.no_grad():
        for imgs, labels in dataloader:
            imgs = imgs.to(device)
            feats = backbone(imgs)                 # (B, D) — use CLS token or global avg pool
            if feats.dim() > 2:
                feats = feats.flatten(1)           # flatten spatial dims if needed
            feats_list.append(feats.cpu().numpy())
            label_list.append(labels.numpy())
    return np.vstack(feats_list), np.concatenate(label_list)


def linear_probe_sklearn(backbone, train_loader, val_loader, device='cuda',
                         max_iter=1000, C=0.316):
    """Frozen backbone + sklearn LogisticRegression linear probe."""
    print('Extracting train features...')
    X_train, y_train = extract_features(backbone, train_loader, device)
    print('Extracting val features...')
    X_val,   y_val   = extract_features(backbone, val_loader, device)

    # L2-normalise features (important for cosine-based SSL representations)
    scaler  = StandardScaler(with_std=False)
    X_train = scaler.fit_transform(X_train)
    X_val   = scaler.transform(X_val)
    norms   = np.linalg.norm(X_train, axis=1, keepdims=True)
    X_train /= np.clip(norms, 1e-8, None)
    norms   = np.linalg.norm(X_val, axis=1, keepdims=True)
    X_val   /= np.clip(norms, 1e-8, None)

    clf = LogisticRegression(max_iter=max_iter, C=C, solver='lbfgs',
                             multi_class='multinomial', n_jobs=-1)
    clf.fit(X_train, y_train)
    acc = clf.score(X_val, y_val)
    print(f'Linear probe accuracy: {acc*100:.2f}%')
    return acc


print('Linear probe: freeze backbone, train sklearn LogReg on extracted features.')
print('Tip: L2-normalise features before LogReg for contrastive SSL methods.')
```

## Fine-Tuning — Ceiling Performance

Fine-tuning unfreezes the entire encoder and trains all parameters jointly with the linear head. This always achieves higher accuracy than linear probe because the encoder can adapt its representations to the downstream task. The gap between linear probe and fine-tune accuracy indicates how 'task-ready' the representation is: a small gap means the frozen features are nearly optimal (DINOv2 closes this gap substantially); a large gap means the representation needs task-specific restructuring (MAE features, which are designed for reconstruction, show large linear-to-finetune gaps). Fine-tuning uses a lower learning rate for backbone layers than for the newly added head.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader


def finetune_ssl_model(backbone, train_loader, val_loader,
                       num_classes: int = 1000, feat_dim: int = 768,
                       backbone_lr: float = 1e-5, head_lr: float = 1e-3,
                       epochs: int = 30, device: str = 'cuda'):
    """Fine-tune SSL backbone: lower LR for backbone, higher for new head."""
    head = nn.Linear(feat_dim, num_classes).to(device)
    backbone = backbone.to(device)

    # Separate parameter groups with different LRs
    optimizer = torch.optim.AdamW([
        {'params': backbone.parameters(), 'lr': backbone_lr, 'weight_decay': 0.05},
        {'params': head.parameters(),     'lr': head_lr,     'weight_decay': 0.0},
    ])
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, epochs)
    criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

    for epoch in range(epochs):
        backbone.train(); head.train()
        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            feats  = backbone(imgs).flatten(1)   # (B, feat_dim)
            logits = head(feats)
            loss   = criterion(logits, labels)
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(backbone.parameters(), max_norm=1.0)
            optimizer.step()
        scheduler.step()
        if (epoch + 1) % 10 == 0:
            print(f'  Epoch {epoch+1}/{epochs} done.')

    # Validation
    backbone.eval(); head.eval()
    correct = total = 0
    with torch.no_grad():
        for imgs, labels in val_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            preds = head(backbone(imgs).flatten(1)).argmax(1)
            correct += (preds == labels).sum().item()
            total   += labels.size(0)
    acc = correct / total
    print(f'Fine-tune accuracy: {acc*100:.2f}%')
    return acc


print('Fine-tune: lower LR for SSL backbone, standard LR for task head.')
print('Layer-wise LR decay is also common: LR *= 0.65^layer_depth_from_head.')
```

## k-NN Evaluation — No Training Required

k-Nearest Neighbour evaluation requires no training after SSL pretraining. All training set images are encoded, and their features are stored in an index. A test image is classified by finding its k nearest neighbours in feature space (by cosine similarity) and taking a majority vote. k-NN accuracy is the fastest way to assess whether SSL features are semantically meaningful: if semantically similar images cluster together in the feature space, k-NN will perform well. DINO features famously produce k-NN accuracy of 78% on ImageNet with k=20 — close to supervised ResNet-50 — using no labelled training at all.

```python
import numpy as np
import torch
import torch.nn.functional as F

try:
    import faiss
    HAS_FAISS = True
except ImportError:
    HAS_FAISS = False
    print('faiss not available — falling back to brute-force cosine k-NN.')


def knn_evaluate(backbone, train_loader, val_loader,
                 k: int = 20, device: str = 'cuda'):
    """k-NN evaluation using faiss IndexFlatIP (cosine similarity via L2 norm)."""
    # Extract and L2-normalise features
    def get_feats(loader):
        backbone.eval()
        all_f, all_l = [], []
        with torch.no_grad():
            for imgs, labels in loader:
                f = backbone(imgs.to(device))
                f = F.normalize(f.flatten(1), dim=1)   # unit norm for cosine
                all_f.append(f.cpu().numpy())
                all_l.append(labels.numpy())
        return np.vstack(all_f).astype('float32'), np.concatenate(all_l)

    train_feats, train_labels = get_feats(train_loader)
    val_feats,   val_labels   = get_feats(val_loader)
    D = train_feats.shape[1]

    if HAS_FAISS:
        index = faiss.IndexFlatIP(D)         # inner product = cosine for L2-normed vectors
        index.add(train_feats)
        _, I = index.search(val_feats, k)    # (N_val, k) — indices of k nearest neighbours
    else:
        # Brute-force: (N_val, N_train) cosine similarity matrix
        sims = val_feats @ train_feats.T     # (N_val, N_train)
        I    = np.argsort(-sims, axis=1)[:, :k]   # top-k indices

    # Majority vote
    knn_labels = train_labels[I]             # (N_val, k)
    preds = np.apply_along_axis(
        lambda row: np.bincount(row, minlength=int(train_labels.max())+1).argmax(),
        axis=1, arr=knn_labels
    )
    acc = (preds == val_labels).mean()
    print(f'k-NN (k={k}) accuracy: {acc*100:.2f}%')
    return acc


print('k-NN eval: extract features, L2-normalise, faiss IndexFlatIP, majority vote.')
```

## Semi-Supervised Protocol — 1% and 10% Labels

Semi-supervised evaluation tests label efficiency: how well does the SSL model perform when only 1% or 10% of ImageNet labels are available? The protocol is standardised: (1) select a balanced subset — equal number of examples per class; (2) freeze the SSL backbone; (3) fine-tune only the linear head (or a light MLP head) on the labelled subset; (4) evaluate on the full validation set. This protocol isolates the contribution of the SSL features from supervised data quantity. SimCLR v2 showed 74% top-1 with only 1% labels via distillation; DINOv2 exceeds 80% with 10% labels using just a linear layer.

```python
import torch
import numpy as np
from torch.utils.data import Subset, DataLoader
from torchvision.datasets import ImageFolder
from collections import defaultdict


def select_balanced_subset(dataset: ImageFolder, fraction: float = 0.01,
                           seed: int = 42) -> Subset:
    """Select a class-balanced fraction of a dataset.
    Returns a Subset with fraction*len(dataset) samples, equally distributed.
    """
    rng = np.random.default_rng(seed)
    class_to_indices = defaultdict(list)
    for idx, (_, label) in enumerate(dataset.samples):
        class_to_indices[label].append(idx)

    selected = []
    for label, indices in class_to_indices.items():
        n_select = max(1, int(len(indices) * fraction))
        chosen   = rng.choice(indices, size=n_select, replace=False)
        selected.extend(chosen.tolist())

    rng.shuffle(selected)
    print(f'Selected {len(selected)} samples ({fraction*100:.1f}%) '
          f'from {len(dataset.classes)} classes.')
    return Subset(dataset, selected)


def semisup_eval(backbone, full_dataset: ImageFolder, val_loader: DataLoader,
                 fraction: float = 0.01, feat_dim: int = 768,
                 num_classes: int = 1000, epochs: int = 30, device: str = 'cuda'):
    """Semi-supervised evaluation: freeze backbone, train linear head on fraction% labels."""
    subset  = select_balanced_subset(full_dataset, fraction)
    sub_loader = DataLoader(subset, batch_size=256, shuffle=True, num_workers=4)

    backbone.eval().to(device)
    for p in backbone.parameters():
        p.requires_grad_(False)

    head = torch.nn.Linear(feat_dim, num_classes).to(device)
    opt  = torch.optim.AdamW(head.parameters(), lr=1e-3, weight_decay=0.0)
    crit = torch.nn.CrossEntropyLoss()

    for _ in range(epochs):
        head.train()
        for imgs, labels in sub_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            with torch.no_grad():
                feats = backbone(imgs).flatten(1)
            loss = crit(head(feats), labels)
            opt.zero_grad(); loss.backward(); opt.step()

    head.eval()
    correct = total = 0
    with torch.no_grad():
        for imgs, labels in val_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            correct += (head(backbone(imgs).flatten(1)).argmax(1) == labels).sum().item()
            total   += labels.size(0)
    print(f'Semi-sup {fraction*100:.0f}% accuracy: {correct/total*100:.2f}%')
    return correct / total


print('Semi-supervised: balanced subset selection -> freeze backbone -> train linear head.')
```

> **Standardise Evaluation Hyperparameters for Fair Comparison**: SSL papers often report favorable evaluation numbers by tuning evaluation-specific hyperparameters (learning rate, epochs, augmentation during evaluation). Fair comparison requires: (1) same number of linear probe epochs (100 standard); (2) same optimizer (LBFGS or SGD+momentum); (3) same augmentation during feature extraction (resize + center crop, no random augmentation); (4) same fraction and seed for semi-supervised splits. The DINOv2 paper provides a standardised evaluation codebase — use it as the reference implementation when comparing SSL methods.

## Transfer Learning and Domain Shift

Beyond ImageNet, SSL representations should generalise to other domains. Standard transfer benchmarks include: CIFAR-100 (32×32 object recognition), Flowers-102 (fine-grained flowers), Food-101 (fine-grained food categories), and CUB-200 (bird species — requires fine-grained discrimination). The transfer evaluation protocol is the same as linear probe: freeze backbone, train linear head, measure top-1. Strong SSL methods (DINOv2, DINO) consistently outperform supervised ImageNet pretraining on fine-grained benchmarks because their features are more diverse and less biased toward ImageNet-specific categories.

- CIFAR-100 transfer: DINOv2-ViT-L ~94% linear probe (ResNet-50 supervised: ~87%).
- Flowers-102: SSL methods often match or exceed supervised, as ImageNet has few flower classes.
- CUB-200: fine-grained discrimination favors rich patch-level features (DINOv2, iBOT).
- Medical imaging: SSL pretrained on natural images transfers well with only 100-500 labelled examples.
- Satellite imagery: domain gap is large — consider domain-specific SSL pretraining from scratch.
- k-NN transfer: high k-NN accuracy on transfer datasets = feature diversity, not just ImageNet overfitting.

## Evaluation Protocol Comparison

| Protocol | Labels Needed | Compute | What It Measures | Standard Dataset |
| --- | --- | --- | --- | --- |
| Linear probe | Full train set | Low (frozen features + linear) | Frozen representation quality | ImageNet top-1 |
| Fine-tuning | Full train set | High (full backprop) | Task ceiling / adaptability | ImageNet top-1 |
| k-NN (k=20) | Full train set (no training) | Very low (index lookup) | Feature geometry / clustering | ImageNet top-1 |
| Semi-supervised (1%) | 1% of train set (~13K for ImageNet) | Low (linear head only) | Label efficiency | ImageNet top-1 |
| Semi-supervised (10%) | 10% of train set (~128K) | Low | Label efficiency at scale | ImageNet top-1 |
| Transfer (linear) | Target domain full set | Low (frozen features) | Generalization to new domains | CIFAR-100 / Flowers / CUB |

The relationship between these protocols tells a story about a representation. Large linear-to-finetune gap: representation needs task-specific restructuring (MAE, pixel reconstruction methods). Small gap: representation is already well-organised for the downstream task (DINOv2, DINO). High k-NN but lower linear probe: features form clusters but are not linearly separable (some contrastive methods). Low k-NN but good linear probe after training: features are linearly separable but not naturally clustered — the linear layer learns a non-trivial mapping. Tracking all four metrics provides a complete picture of SSL representation quality.

- Best practice: always report linear probe AND fine-tune — reporting only fine-tune hides representation quality.
- k-NN is free to compute once features are extracted — include it as a sanity check in every experiment.
- Use the same feature extraction transform: 256px resize, 224px center crop, ImageNet normalisation.
- Report standard deviation over 3 seeds for semi-supervised evaluations — high variance is common.
- DINOv2 evaluation codebase: github.com/facebookresearch/dinov2/tree/main/dinov2/eval — use as reference.

## Choosing the Right Evaluation Protocol

The right evaluation protocol depends on the deployment scenario. If the encoder will be frozen in production (embedding service, search index), linear probe accuracy is the most relevant metric — optimise for it. If the encoder will be fine-tuned per-task (the common case), linear probe accuracy is a proxy but fine-tune accuracy is the true target. k-NN accuracy is the fastest diagnostic: it reveals whether features are geometrically meaningful without any training. For resource-constrained environments with few labels, semi-supervised 1% accuracy reveals the most important property — how much a model reduces labelling cost. Report all four for publishable work; start with k-NN for quick iteration.

