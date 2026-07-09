---
title: "Gaussian Mixture Models (GMMs)"
slug: "gaussian-mixture-models"
description: "Understand GMMs as probabilistic clustering: the mixture density, soft assignments via responsibilities, EM algorithm for parameter estimation, covariance type selection, BIC/AIC model order selection, and anomaly detection using log-likelihood thresholds."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2F1c3NpYW4gTWl4dHVyZSBNb2RlbHMgKEdNTXMpIGFyZSBhIHByaW5jaXBsZWQgcHJvYmFiaWxpc3RpYyBmcmFtZXdvcmsgZm9yIGNsdXN0ZXJpbmcgYW5kIGRlbnNpdHkgZXN0aW1hdGlvbi4gVW5saWtlIGstbWVhbnMsIHdoaWNoIG1ha2VzIGhhcmQgY2x1c3RlciBhc3NpZ25tZW50cywgR01NcyBjb21wdXRlIHNvZnQgcmVzcG9uc2liaWxpdGllcyDigJQgdGhlIHByb2JhYmlsaXR5IHRoYXQgZWFjaCBwb2ludCBiZWxvbmdzIHRvIGVhY2ggY29tcG9uZW50LiBUaGUgbW9kZWwgaXMgZml0IGJ5IG1heGltdW0gbGlrZWxpaG9vZCB1c2luZyB0aGUgRU0gYWxnb3JpdGhtLCBhbmQgdGhlIHJlc3VsdGluZyBtaXh0dXJlIGRlbnNpdHkgY2FuIGJlIHVzZWQgZm9yIGRlbnNpdHkgZXN0aW1hdGlvbiwgYW5vbWFseSBkZXRlY3Rpb24sIGFuZCBnZW5lcmF0aXZlIG1vZGVsaW5nIGluIGFkZGl0aW9uIHRvIGNsdXN0ZXJpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR01NIEZvcm11bGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIEdNTSB3aXRoIGsgY29tcG9uZW50cyBtb2RlbHMgdGhlIGRhdGEgZGVuc2l0eSBhcyBwKHgpID0gzqPigpYgz4DigpYgTih4IHwgzrzigpYsIM6j4oKWKSB3aGVyZSDPgOKCliDiiaUgMCBhcmUgbWl4aW5nIHdlaWdodHMgc3VtbWluZyB0byAxLCDOvOKCliBpcyB0aGUgay10aCBjb21wb25lbnQgbWVhbiwgYW5kIM6j4oKWIGlzIGl0cyBjb3ZhcmlhbmNlIG1hdHJpeC4gVGhlIGxhdGVudCB2YXJpYWJsZSB64bWiIOKIiCB7MSwuLi4sa30gaW5kaWNhdGVzIHdoaWNoIGNvbXBvbmVudCBnZW5lcmF0ZWQgcG9pbnQgeOG1oiwgd2l0aCBQKHrhtaI9aykgPSDPgOKCli4gVGhlIGNvbXBsZXRlLWRhdGEgbGlrZWxpaG9vZCBpcyBwKFgsWnzOuCkgPSDOoOG1oiDOoOKCliBbz4DigpYgTih44bWifM684oKWLM6j4oKWKV1eezEoeuG1oj1rKX0sIHdoaWNoIGlzIHRyYWN0YWJsZS4gVGhlIG9ic2VydmVkLWRhdGEgbGlrZWxpaG9vZCDOo19aIHAoWCxafM64KSByZXF1aXJlcyBzdW1taW5nIG92ZXIgYWxsIGvigb8gYXNzaWdubWVudHMgYW5kIGlzIG1heGltaXplZCBieSBFTS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFTSBBbGdvcml0aG0gZm9yIEdNTXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVNIGFsdGVybmF0ZXMgYmV0d2VlbjogRS1zdGVwIOKAlCBjb21wdXRlIHRoZSByZXNwb25zaWJpbGl0eSBy4bWi4oKWID0gUCh64bWiPWsgfCB44bWiLCDOuCkgPSDPgOKCliBOKHjhtaJ8zrzigpYszqPigpYpIC8gzqPisbwgz4DisbwgTih44bWifM684rG8LM6j4rG8KS4gVGhpcyBpcyB0aGUgcG9zdGVyaW9yIHByb2JhYmlsaXR5IHRoYXQgY29tcG9uZW50IGsgZ2VuZXJhdGVkIHjhtaIuIE0tc3RlcCDigJQgdXBkYXRlIHBhcmFtZXRlcnMgdXNpbmcgc29mdC13ZWlnaHRlZCBzdGF0aXN0aWNzOiBO4oKWID0gzqPhtaIgcuG1ouKCliAoZWZmZWN0aXZlIGNvdW50KSwgz4DigpYgPSBO4oKWL24sIM684oKWID0gzqPhtaIgcuG1ouKCliB44bWiIC8gTuKCliwgzqPigpYgPSDOo+G1oiBy4bWi4oKWICh44bWi4oiSzrzigpYpKHjhtaLiiJLOvOKClinhtYAgLyBO4oKWLiBFYWNoIGl0ZXJhdGlvbiBtb25vdG9uaWNhbGx5IGluY3JlYXNlcyB0aGUgbG9nLWxpa2VsaWhvb2QgbG9nIHAoWHzOuCkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbXVsdGl2YXJpYXRlX25vcm1hbFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2Jsb2JzXG5cbmRlZiBnbW1fZW0oWCwgaywgbWF4X2l0ZXI9MTAwLCB0b2w9MWUtNCwgc2VlZD00Mik6XG4gICAgXCJcIlwiRU0gYWxnb3JpdGhtIGZvciBhIGstY29tcG9uZW50IEdNTS5cIlwiXCJcbiAgICBybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoc2VlZClcbiAgICBuLCBkID0gWC5zaGFwZVxuICAgICMgSW5pdGlhbGl6ZSB3aXRoIHJhbmRvbSBhc3NpZ25tZW50c1xuICAgIHBpID0gbnAub25lcyhrKSAvIGtcbiAgICBtdSA9IFhbcm5nLmNob2ljZShuLCBrLCByZXBsYWNlPUZhbHNlKV1cbiAgICBTaWdtYSA9IFtucC5leWUoZCkgKiBYLnZhcigpIGZvciBfIGluIHJhbmdlKGspXVxuICAgIGxvZ19saWtzID0gW11cbiAgICBmb3IgaXRlcmF0aW9uIGluIHJhbmdlKG1heF9pdGVyKTpcbiAgICAgICAgIyBFLXN0ZXA6IHJlc3BvbnNpYmlsaXRpZXNcbiAgICAgICAgUiA9IG5wLnplcm9zKChuLCBrKSlcbiAgICAgICAgZm9yIGogaW4gcmFuZ2Uoayk6XG4gICAgICAgICAgICBSWzosIGpdID0gcGlbal0gKiBtdWx0aXZhcmlhdGVfbm9ybWFsLnBkZihYLCBtdVtqXSwgU2lnbWFbal0pXG4gICAgICAgIGxsID0gbnAubG9nKFIuc3VtKGF4aXM9MSkgKyAxZS0zMDApLnN1bSgpXG4gICAgICAgIGxvZ19saWtzLmFwcGVuZChsbClcbiAgICAgICAgUiAvPSBSLnN1bShheGlzPTEsIGtlZXBkaW1zPVRydWUpXG4gICAgICAgICMgTS1zdGVwOiB1cGRhdGUgcGFyYW1ldGVyc1xuICAgICAgICBOayA9IFIuc3VtKGF4aXM9MClcbiAgICAgICAgcGkgPSBOayAvIG5cbiAgICAgICAgbXUgPSAoUi5UIEAgWCkgLyBOa1s6LCBOb25lXVxuICAgICAgICBmb3IgaiBpbiByYW5nZShrKTpcbiAgICAgICAgICAgIGRpZmYgPSBYIC0gbXVbal1cbiAgICAgICAgICAgIFNpZ21hW2pdID0gKFJbOiwgaiwgTm9uZV0gKiBkaWZmKS5UIEAgZGlmZiAvIE5rW2pdICsgMWUtNiAqIG5wLmV5ZShkKVxuICAgICAgICBpZiBpdGVyYXRpb24gXHUwMDNlIDAgYW5kIGFicyhsb2dfbGlrc1stMV0gLSBsb2dfbGlrc1stMl0pIFx1MDAzYyB0b2w6XG4gICAgICAgICAgICBwcmludChmXCJDb252ZXJnZWQgYXQgaXRlcmF0aW9uIHtpdGVyYXRpb24gKyAxfVwiKVxuICAgICAgICAgICAgYnJlYWtcbiAgICByZXR1cm4gcGksIG11LCBTaWdtYSwgbnAuYXJyYXkobG9nX2xpa3MpXG5cblgsIHlfdHJ1ZSA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTMwMCwgY2VudGVycz0zLCBjbHVzdGVyX3N0ZD0wLjgsIHJhbmRvbV9zdGF0ZT00MilcbnBpLCBtdSwgU2lnbWEsIGxscyA9IGdtbV9lbShYLCBrPTMpXG5sYWJlbHMgPSBucC5hcmdtYXgobnAuY29sdW1uX3N0YWNrKFtwaVtqXSAqIG11bHRpdmFyaWF0ZV9ub3JtYWwucGRmKFgsIG11W2pdLCBTaWdtYVtqXSlcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmb3IgaiBpbiByYW5nZSgzKV0pLCBheGlzPTEpXG5wcmludChmXCJNaXhpbmcgd2VpZ2h0czoge3BpLnJvdW5kKDMpfVwiKVxucHJpbnQoZlwiRmluYWwgbG9nLWxpa2VsaWhvb2Q6IHtsbHNbLTFdOi4yZn0gKGluY3JlYXNlZCBtb25vdG9uaWNhbGx5OiB7YWxsKG5wLmRpZmYobGxzKSBcdTAwM2U9IC0xZS04KX0pXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ292YXJpYW5jZSBUeXBlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvdmFyaWFuY2Ugc3RydWN0dXJlIG9mIGVhY2ggY29tcG9uZW50IGNvbnRyb2xzIHRoZSBzaGFwZSBvZiBjbHVzdGVycyBpdCBjYW4gbW9kZWwuIFNrbGVhcm5cdTAwMjdzIEdhdXNzaWFuTWl4dHVyZSBzdXBwb3J0cyBmb3VyIHR5cGVzLCB0cmFkaW5nIGZsZXhpYmlsaXR5IGZvciB0aGUgbnVtYmVyIG9mIHBhcmFtZXRlcnM6IGZ1bGwgKGVhY2ggY29tcG9uZW50IGhhcyBpdHMgb3duIGFyYml0cmFyeSBjb3ZhcmlhbmNlLCBtb3N0IGV4cHJlc3NpdmUpLCB0aWVkIChhbGwgY29tcG9uZW50cyBzaGFyZSBvbmUgY292YXJpYW5jZSBtYXRyaXgpLCBkaWFnb25hbCAob25seSB2YXJpYW5jZXMsIG5vIGNvdmFyaWFuY2VzIOKAlCBheGlzLWFsaWduZWQgZWxsaXBzZXMpLCBhbmQgc3BoZXJpY2FsIChvbmUgc2NhbGFyIHZhcmlhbmNlIHBlciBjb21wb25lbnQg4oCUIHNhbWUgYXMgay1tZWFucyBnZW9tZXRyeSkuIFNpbXBsZXIgc3RydWN0dXJlcyBhcmUgZmFzdGVyLCBuZWVkIGxlc3MgZGF0YSwgYW5kIGFyZSBsZXNzIHByb25lIHRvIG92ZXJmaXR0aW5nIGJ1dCBtYXkgdW5kZXJmaXQgY29tcGxleCBkYXRhLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5taXh0dXJlIGltcG9ydCBHYXVzc2lhbk1peHR1cmVcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cblgsIHlfdHJ1ZSA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTQwMCwgY2VudGVycz00LCBjbHVzdGVyX3N0ZD1bMC41LCAxLjAsIDAuMywgMC44XSwgcmFuZG9tX3N0YXRlPTcpXG5YID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG5cbnByaW50KGZcIntcdTAwMjdDb3ZhcmlhbmNlXHUwMDI3OjEyc30ge1x1MDAyN0FJQ1x1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0JJQ1x1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0xvZy1MaWtcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjcjUGFyYW1zXHUwMDI3Olx1MDAzZTh9XCIpXG5mb3IgY292X3R5cGUgaW4gW1x1MDAyN2Z1bGxcdTAwMjcsIFx1MDAyN3RpZWRcdTAwMjcsIFx1MDAyN2RpYWdcdTAwMjcsIFx1MDAyN3NwaGVyaWNhbFx1MDAyN106XG4gICAgZ20gPSBHYXVzc2lhbk1peHR1cmUobl9jb21wb25lbnRzPTQsIGNvdmFyaWFuY2VfdHlwZT1jb3ZfdHlwZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgbl9pbml0PTUsIHJhbmRvbV9zdGF0ZT00MiwgbWF4X2l0ZXI9MjAwKVxuICAgIGdtLmZpdChYKVxuICAgIHByaW50KGZcIntjb3ZfdHlwZToxMnN9IHtnbS5haWMoWCk6XHUwMDNlMTAuMmZ9IHtnbS5iaWMoWCk6XHUwMDNlMTAuMmZ9IFwiXG4gICAgICAgICAgZlwie2dtLnNjb3JlKFgpKmxlbihYKTpcdTAwM2UxMi4yZn0ge2dtLm5fcGFyYW1ldGVyczpcdTAwM2U4ZH1cIilcblxucHJpbnQoXCJcXG5GdWxsOiBtb3N0IGV4cHJlc3NpdmUgYnV0IG1vc3QgcGFyYW1ldGVycyDigJQgcmlzayBvZiBkZWdlbmVyYXRlIGNvdmFyaWFuY2VzLlwiKVxucHJpbnQoXCJTcGhlcmljYWw6IGVxdWl2YWxlbnQgdG8gay1tZWFucyBnZW9tZXRyeSB3aXRoIHNvZnQgYXNzaWdubWVudHMuXCIpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkNvdmFyaWFuY2UgVHlwZSIsIlNoYXBlIiwiUGFyYW1ldGVycyBwZXIgQ29tcG9uZW50IiwiV2hlbiB0byBVc2UiXSwicm93cyI6W1siZnVsbCIsIkFyYml0cmFyeSBlbGxpcHNvaWQiLCJkKGQrMSkvMiIsIkNvbXBsZXggY29ycmVsYXRlZCBjbHVzdGVycywgc3VmZmljaWVudCBkYXRhIl0sWyJ0aWVkIiwiU2FtZSBlbGxpcHNvaWQgZm9yIGFsbCIsImQoZCsxKS8yIHRvdGFsIiwiU2ltaWxhciBjbHVzdGVyIHNoYXBlcywgcmVkdWNlcyBvdmVyZml0dGluZyJdLFsiZGlhZyIsIkF4aXMtYWxpZ25lZCBlbGxpcHNvaWQiLCJkIiwiSW5kZXBlbmRlbnQgZmVhdHVyZXMsIGhpZ2gtZGltZW5zaW9uYWwgZGF0YSJdLFsic3BoZXJpY2FsIiwiU3BoZXJlIChpc290cm9waWMpIiwiMSIsIkstbWVhbnMtbGlrZSBiZWhhdmlvciwgc2ltcGxlc3QgbW9kZWwiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vZGVsIFNlbGVjdGlvbiDigJQgQklDIGFuZCBBSUMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFJQyA9IOKIkjIgbG9nIEwozrjMgikgKyAycCBhbmQgQklDID0g4oiSMiBsb2cgTCjOuMyCKSArIHAgbG9nIG4sIHdoZXJlIHAgaXMgdGhlIG51bWJlciBvZiBmcmVlIHBhcmFtZXRlcnMgYW5kIEwozrjMgikgaXMgdGhlIG1heGltaXplZCBsaWtlbGlob29kLiBCSUMgcGVuYWxpemVzIG1vZGVsIGNvbXBsZXhpdHkgbW9yZSBoZWF2aWx5IChieSBsb2cgbiB2cyAyKSBhbmQgaXMgY29uc2lzdGVudCDigJQgaXQgc2VsZWN0cyB0aGUgdHJ1ZSBudW1iZXIgb2YgY29tcG9uZW50cyBhcyBu4oaS4oieIGlmIHRoZSB0cnVlIG1vZGVsIGlzIGluIHRoZSBjYW5kaWRhdGUgc2V0LiBBSUMgdGVuZHMgdG8gZmF2b3IgbGFyZ2VyIG1vZGVscy4gVGhlIHJlY29tbWVuZGVkIHByb2NlZHVyZSBpcyB0byBmaXQgR01NcyB3aXRoIGs9MSwuLi4sS19tYXgsIHBsb3QgQklDIHZzIGssIGFuZCBjaG9vc2UgdGhlIGsgYXQgdGhlIG1pbmltdW0uIEEgZGVnZW5lcmF0ZSBjb3ZhcmlhbmNlICh2YXJpYW5jZSDihpIgMCBmb3IgYSBjb21wb25lbnQgZml0dGVkIHRvIGEgc2luZ2xlIHBvaW50KSBzaWduYWxzIG92ZXJmaXR0aW5nIOKAlCBhZGQgcmVndWxhcml6YXRpb24gb3IgcmVkdWNlIGsuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLm1peHR1cmUgaW1wb3J0IEdhdXNzaWFuTWl4dHVyZVxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2Jsb2JzXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuWCwgXyA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTUwMCwgY2VudGVycz00LCBjbHVzdGVyX3N0ZD0wLjksIHJhbmRvbV9zdGF0ZT0wKVxuWCA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKVxuXG5rX3JhbmdlID0gcmFuZ2UoMSwgMTApXG5haWNfdmFscywgYmljX3ZhbHMgPSBbXSwgW11cbmZvciBrIGluIGtfcmFuZ2U6XG4gICAgZ20gPSBHYXVzc2lhbk1peHR1cmUobl9jb21wb25lbnRzPWssIGNvdmFyaWFuY2VfdHlwZT1cdTAwMjdmdWxsXHUwMDI3LFxuICAgICAgICAgICAgICAgICAgICAgICAgICByZWdfY292YXI9MWUtNCwgbl9pbml0PTUsIHJhbmRvbV9zdGF0ZT00MilcbiAgICBnbS5maXQoWClcbiAgICBhaWNfdmFscy5hcHBlbmQoZ20uYWljKFgpKVxuICAgIGJpY192YWxzLmFwcGVuZChnbS5iaWMoWCkpXG5cbmJlc3RfYWljID0gbGlzdChrX3JhbmdlKVtucC5hcmdtaW4oYWljX3ZhbHMpXVxuYmVzdF9iaWMgPSBsaXN0KGtfcmFuZ2UpW25wLmFyZ21pbihiaWNfdmFscyldXG5wcmludChmXCJBSUMgc2VsZWN0cyBrPXtiZXN0X2FpY30sICBCSUMgc2VsZWN0cyBrPXtiZXN0X2JpY31cIilcbnByaW50KGZcIlxcbntcdTAwMjdrXHUwMDI3Olx1MDAzZTR9IHtcdTAwMjdBSUNcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdCSUNcdTAwMjc6XHUwMDNlMTJ9XCIpXG5mb3IgaywgYSwgYiBpbiB6aXAoa19yYW5nZSwgYWljX3ZhbHMsIGJpY192YWxzKTpcbiAgICBtYXJrX2EgPSBcIiBcdTAwM2NcdTAwM2NcIiBpZiBrID09IGJlc3RfYWljIGVsc2UgXCJcIlxuICAgIG1hcmtfYiA9IFwiIFx1MDAzY1x1MDAzY1wiIGlmIGsgPT0gYmVzdF9iaWMgZWxzZSBcIlwiXG4gICAgcHJpbnQoZlwie2s6XHUwMDNlNH0ge2E6XHUwMDNlMTIuMmZ9e21hcmtfYTo0c30ge2I6XHUwMDNlMTIuMmZ9e21hcmtfYn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHTU0gZm9yIEFub21hbHkgRGV0ZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHTU1zIHByb3ZpZGUgYSBmdWxsIGRlbnNpdHkgZXN0aW1hdGUgcCh4KSwgbWFraW5nIHRoZW0gbmF0dXJhbCBmb3IgYW5vbWFseSBkZXRlY3Rpb24uIEEgcG9pbnQgeCBpcyBhbm9tYWxvdXMgaWYgbG9nIHAoeCkgZmFsbHMgYmVsb3cgYSB0aHJlc2hvbGQgz4QgY2hvc2VuIHRvIGFjY2VwdCBhIGRlc2lyZWQgZmFsc2UtcG9zaXRpdmUgcmF0ZSBvbiB0aGUgdHJhaW5pbmcgZGF0YS4gVGhpcyBhcHByb2FjaCBpcyBub24tcGFyYW1ldHJpYyBpbiB0aGUgc2Vuc2UgdGhhdCB0aGUgYW5vbWFseSB0aHJlc2hvbGQgYWRhcHRzIHRvIHRoZSBsZWFybmVkIGRhdGEgZGlzdHJpYnV0aW9uLCBoYW5kbGluZyBtdWx0aS1tb2RhbCBkYXRhIGJldHRlciB0aGFuIHNpbmdsZS1HYXVzc2lhbiBtZXRob2RzLiBUaGUgdGhyZXNob2xkIGlzIHR5cGljYWxseSBzZXQgYXQgYSBsb3cgcGVyY2VudGlsZSAoZS5nLiwgMm5kIG9yIDV0aCBwZXJjZW50aWxlKSBvZiB0aGUgdHJhaW5pbmcgbG9nLWxpa2VsaWhvb2RzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5taXh0dXJlIGltcG9ydCBHYXVzc2lhbk1peHR1cmVcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2Jsb2JzXG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0Milcblhfbm9ybWFsLCBfID0gbWFrZV9ibG9icyhuX3NhbXBsZXM9NDAwLCBjZW50ZXJzPTMsIGNsdXN0ZXJfc3RkPTAuNywgcmFuZG9tX3N0YXRlPTApXG5YX2Fub21hbHkgPSBybmcudW5pZm9ybSgtNiwgNiwgc2l6ZT0oMzAsIDIpKVxuWF9ub3JtYWwgPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWF9ub3JtYWwpXG5YX2Fub21hbHkgPSAoWF9hbm9tYWx5IC0gWF9hbm9tYWx5Lm1lYW4oYXhpcz0wKSkgLyBYX2Fub21hbHkuc3RkKGF4aXM9MClcblxuZ20gPSBHYXVzc2lhbk1peHR1cmUobl9jb21wb25lbnRzPTMsIGNvdmFyaWFuY2VfdHlwZT1cdTAwMjdmdWxsXHUwMDI3LCBuX2luaXQ9NSwgcmFuZG9tX3N0YXRlPTQyKVxuZ20uZml0KFhfbm9ybWFsKVxuXG5sb2dfcHJvYnNfdHJhaW4gPSBnbS5zY29yZV9zYW1wbGVzKFhfbm9ybWFsKVxudGhyZXNob2xkID0gbnAucGVyY2VudGlsZShsb2dfcHJvYnNfdHJhaW4sIDIpXG5cbmxvZ19wcm9ic19ub3JtYWwgPSBnbS5zY29yZV9zYW1wbGVzKFhfbm9ybWFsKVxubG9nX3Byb2JzX2Fub21hbHkgPSBnbS5zY29yZV9zYW1wbGVzKFhfYW5vbWFseSlcblxuZnByID0gKGxvZ19wcm9ic19ub3JtYWwgXHUwMDNjIHRocmVzaG9sZCkubWVhbigpXG5kZXRlY3Rpb25fcmF0ZSA9IChsb2dfcHJvYnNfYW5vbWFseSBcdTAwM2MgdGhyZXNob2xkKS5tZWFuKClcblxucHJpbnQoZlwiVGhyZXNob2xkICgybmQgcGVyY2VudGlsZSk6IHt0aHJlc2hvbGQ6LjRmfVwiKVxucHJpbnQoZlwiRmFsc2UgcG9zaXRpdmUgcmF0ZSBvbiB0cmFpbmluZyBkYXRhOiB7ZnByOi4yJX1cIilcbnByaW50KGZcIkFub21hbHkgZGV0ZWN0aW9uIHJhdGU6IHtkZXRlY3Rpb25fcmF0ZTouMiV9XCIpXG5wcmludChmXCJUcmFpbiBsb2ctcHJvYjogbWVhbj17bG9nX3Byb2JzX3RyYWluLm1lYW4oKTouMmZ9LCBtaW49e2xvZ19wcm9ic190cmFpbi5taW4oKTouMmZ9XCIpXG5wcmludChmXCJBbm9tYWx5IGxvZy1wcm9iOiBtZWFuPXtsb2dfcHJvYnNfYW5vbWFseS5tZWFuKCk6LjJmfSwgbWluPXtsb2dfcHJvYnNfYW5vbWFseS5taW4oKTouMmZ9XCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJHTU0gdnMgSy1NZWFucyDigJQgVGhlIEhhcmQgQXNzaWdubWVudCBMaW1pdCIsImNvbnRlbnQiOiJLLW1lYW5zIGlzIGEgc3BlY2lhbCBjYXNlIG9mIEdNTSB3aXRoIHNwaGVyaWNhbCAoaXNvdHJvcGljKSBjb3ZhcmlhbmNlcyBhbmQgaGFyZCBhc3NpZ25tZW50cy4gQXMgdGhlIGNvdmFyaWFuY2Ugc2NhbGUgz4PihpIwLCB0aGUgc29mdCBHTU0gcmVzcG9uc2liaWxpdGllcyBy4bWi4oKWIGNvbnZlcmdlIHRvIG9uZS1ob3QgY2x1c3RlciBhc3NpZ25tZW50cywgcmVjb3ZlcmluZyBleGFjdGx5IHRoZSBrLW1lYW5zIG9iamVjdGl2ZS4gVGhpcyBtZWFucyBHTU0gZ2VuZXJhbGl6ZXMgay1tZWFucyB0byBlbGxpcHRpY2FsIGNsdXN0ZXJzIGFuZCBwcm9iYWJpbGlzdGljIG1lbWJlcnNoaXAg4oCUIGF0IHRoZSBjb3N0IG9mIG1vcmUgcGFyYW1ldGVycyBhbmQgc2xvd2VyIGNvbnZlcmdlbmNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlZ2VuZXJhdGUgQ292YXJpYW5jZXMgYW5kIFJlZ3VsYXJpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIEdNTSBjb3ZhcmlhbmNlIGJlY29tZXMgZGVnZW5lcmF0ZSB3aGVuIGEgY29tcG9uZW50IGNvbGxhcHNlcyB0byBmaXQgb25seSBvbmUgb3IgYSBmZXcgcG9pbnRzOiBpdHMgZGV0ZXJtaW5hbnQgYXBwcm9hY2hlcyB6ZXJvIGFuZCB0aGUgbGlrZWxpaG9vZCBzcGlrZSB0byAr4oieLCBjYXVzaW5nIG51bWVyaWNhbCBpbnN0YWJpbGl0eSBhbmQgZmFsc2UgY29udmVyZ2VuY2UuIFRoaXMgb3Zlci1maXR0aW5nIGhhcHBlbnMgd2hlbiBrIGlzIHRvbyBsYXJnZSByZWxhdGl2ZSB0byBuLCBvciB3aGVuIHR3byBjb21wb25lbnRzIG92ZXJsYXAgc2V2ZXJlbHkuIFRoZSBmaXggaXMgcmVndWxhcml6YXRpb246IGFkZCByZWdfY292YXIgKGRlZmF1bHQgMWUtNikgdG8gdGhlIGRpYWdvbmFsIG9mIGVhY2ggzqPigpYsIGVxdWl2YWxlbnQgdG8gYWRkaW5nIGEgd2VhayBzcGhlcmljYWwgcHJpb3IuIElmIGRlZ2VuZXJhdGUgY292YXJpYW5jZXMgcGVyc2lzdCwgcmVkdWNlIGsgb3Igc3dpdGNoIGZyb20gXHUwMDI3ZnVsbFx1MDAyNyB0byBcdTAwMjd0aWVkXHUwMDI3IG9yIFx1MDAyN2RpYWdcdTAwMjcgY292YXJpYW5jZSB0eXBlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBOb3RlcyBhbmQgUGl0ZmFsbHMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFsd2F5cyBzZXQgcmVnX2NvdmFyIFx1MDAzZSAwIChkZWZhdWx0IDFlLTYgaW4gc2tsZWFybikgdG8gcHJldmVudCBkZWdlbmVyYXRlIGNvdmFyaWFuY2VzIHdoZW4gYSBjb21wb25lbnQgY29sbGFwc2VzIHRvIGEgc2luZ2xlIHBvaW50LiIsIlVzZSBuX2luaXQgXHUwMDNlPSA1IOKAlCBHTU0gRU0gaXMgc2Vuc2l0aXZlIHRvIGluaXRpYWxpemF0aW9uOyBtdWx0aXBsZSByZXN0YXJ0cyB3aXRoIHJhbmRvbSBpbml0aWFsaXphdGlvbiBhcmUgc3RhbmRhcmQuIiwiRnVsbCBjb3ZhcmlhbmNlIHdpdGggc21hbGwgY2x1c3RlcnMgYW5kIGhpZ2ggZCBjYW4gb3ZlcmZpdDsgcHJlZmVyIGRpYWdvbmFsIG9yIHRpZWQgY292YXJpYW5jZSBhcyBhIHN0YXJ0aW5nIHBvaW50LiIsIkJJQyBpcyB0aGUgc3RhbmRhcmQgbW9kZWwgc2VsZWN0aW9uIGNyaXRlcmlvbiBmb3IgR01NczsgcHJlZmVyIGl0IG92ZXIgQUlDIGFzIHNhbXBsZSBzaXplIGdyb3dzLiIsIkdNTSBsb2ctbGlrZWxpaG9vZCBpcyBub3QgZGlyZWN0bHkgY29tcGFyYWJsZSBhY3Jvc3MgZGlmZmVyZW50IG51bWJlcnMgb2YgY29tcG9uZW50cyB3aXRob3V0IHBlbmFsaXphdGlvbiAoQUlDL0JJQykuIiwiRm9yIHN0cmVhbWluZyBkYXRhLCB1c2Ugb25saW5lIEVNIG9yIHRoZSBza2xlYXJuIHBhcnRpYWxfZml0IGludGVyZmFjZSBmb3IgaW5jcmVtZW50YWwgdXBkYXRlcy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Gaussian Mixture Models (GMMs)

Gaussian Mixture Models (GMMs) are a principled probabilistic framework for clustering and density estimation. Unlike k-means, which makes hard cluster assignments, GMMs compute soft responsibilities — the probability that each point belongs to each component. The model is fit by maximum likelihood using the EM algorithm, and the resulting mixture density can be used for density estimation, anomaly detection, and generative modeling in addition to clustering.

## GMM Formulation

A GMM with k components models the data density as p(x) = Σₖ πₖ N(x | μₖ, Σₖ) where πₖ ≥ 0 are mixing weights summing to 1, μₖ is the k-th component mean, and Σₖ is its covariance matrix. The latent variable zᵢ ∈ {1,...,k} indicates which component generated point xᵢ, with P(zᵢ=k) = πₖ. The complete-data likelihood is p(X,Z|θ) = Πᵢ Πₖ [πₖ N(xᵢ|μₖ,Σₖ)]^{1(zᵢ=k)}, which is tractable. The observed-data likelihood Σ_Z p(X,Z|θ) requires summing over all kⁿ assignments and is maximized by EM.

## EM Algorithm for GMMs

EM alternates between: E-step — compute the responsibility rᵢₖ = P(zᵢ=k | xᵢ, θ) = πₖ N(xᵢ|μₖ,Σₖ) / Σⱼ πⱼ N(xᵢ|μⱼ,Σⱼ). This is the posterior probability that component k generated xᵢ. M-step — update parameters using soft-weighted statistics: Nₖ = Σᵢ rᵢₖ (effective count), πₖ = Nₖ/n, μₖ = Σᵢ rᵢₖ xᵢ / Nₖ, Σₖ = Σᵢ rᵢₖ (xᵢ−μₖ)(xᵢ−μₖ)ᵀ / Nₖ. Each iteration monotonically increases the log-likelihood log p(X|θ).

```python
import numpy as np
from scipy.stats import multivariate_normal
from sklearn.datasets import make_blobs

def gmm_em(X, k, max_iter=100, tol=1e-4, seed=42):
    """EM algorithm for a k-component GMM."""
    rng = np.random.default_rng(seed)
    n, d = X.shape
    # Initialize with random assignments
    pi = np.ones(k) / k
    mu = X[rng.choice(n, k, replace=False)]
    Sigma = [np.eye(d) * X.var() for _ in range(k)]
    log_liks = []
    for iteration in range(max_iter):
        # E-step: responsibilities
        R = np.zeros((n, k))
        for j in range(k):
            R[:, j] = pi[j] * multivariate_normal.pdf(X, mu[j], Sigma[j])
        ll = np.log(R.sum(axis=1) + 1e-300).sum()
        log_liks.append(ll)
        R /= R.sum(axis=1, keepdims=True)
        # M-step: update parameters
        Nk = R.sum(axis=0)
        pi = Nk / n
        mu = (R.T @ X) / Nk[:, None]
        for j in range(k):
            diff = X - mu[j]
            Sigma[j] = (R[:, j, None] * diff).T @ diff / Nk[j] + 1e-6 * np.eye(d)
        if iteration > 0 and abs(log_liks[-1] - log_liks[-2]) < tol:
            print(f"Converged at iteration {iteration + 1}")
            break
    return pi, mu, Sigma, np.array(log_liks)

X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=0.8, random_state=42)
pi, mu, Sigma, lls = gmm_em(X, k=3)
labels = np.argmax(np.column_stack([pi[j] * multivariate_normal.pdf(X, mu[j], Sigma[j])
                                     for j in range(3)]), axis=1)
print(f"Mixing weights: {pi.round(3)}")
print(f"Final log-likelihood: {lls[-1]:.2f} (increased monotonically: {all(np.diff(lls) >= -1e-8)})")
```

## Covariance Types

The covariance structure of each component controls the shape of clusters it can model. Sklearn's GaussianMixture supports four types, trading flexibility for the number of parameters: full (each component has its own arbitrary covariance, most expressive), tied (all components share one covariance matrix), diagonal (only variances, no covariances — axis-aligned ellipses), and spherical (one scalar variance per component — same as k-means geometry). Simpler structures are faster, need less data, and are less prone to overfitting but may underfit complex data.

```python
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=[0.5, 1.0, 0.3, 0.8], random_state=7)
X = StandardScaler().fit_transform(X)

print(f"{'Covariance':12s} {'AIC':>10} {'BIC':>10} {'Log-Lik':>12} {'#Params':>8}")
for cov_type in ['full', 'tied', 'diag', 'spherical']:
    gm = GaussianMixture(n_components=4, covariance_type=cov_type,
                          n_init=5, random_state=42, max_iter=200)
    gm.fit(X)
    print(f"{cov_type:12s} {gm.aic(X):>10.2f} {gm.bic(X):>10.2f} "
          f"{gm.score(X)*len(X):>12.2f} {gm.n_parameters:>8d}")

print("\nFull: most expressive but most parameters — risk of degenerate covariances.")
print("Spherical: equivalent to k-means geometry with soft assignments.")
```

| Covariance Type | Shape | Parameters per Component | When to Use |
| --- | --- | --- | --- |
| full | Arbitrary ellipsoid | d(d+1)/2 | Complex correlated clusters, sufficient data |
| tied | Same ellipsoid for all | d(d+1)/2 total | Similar cluster shapes, reduces overfitting |
| diag | Axis-aligned ellipsoid | d | Independent features, high-dimensional data |
| spherical | Sphere (isotropic) | 1 | K-means-like behavior, simplest model |

## Model Selection — BIC and AIC

AIC = −2 log L(θ̂) + 2p and BIC = −2 log L(θ̂) + p log n, where p is the number of free parameters and L(θ̂) is the maximized likelihood. BIC penalizes model complexity more heavily (by log n vs 2) and is consistent — it selects the true number of components as n→∞ if the true model is in the candidate set. AIC tends to favor larger models. The recommended procedure is to fit GMMs with k=1,...,K_max, plot BIC vs k, and choose the k at the minimum. A degenerate covariance (variance → 0 for a component fitted to a single point) signals overfitting — add regularization or reduce k.

```python
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.9, random_state=0)
X = StandardScaler().fit_transform(X)

k_range = range(1, 10)
aic_vals, bic_vals = [], []
for k in k_range:
    gm = GaussianMixture(n_components=k, covariance_type='full',
                          reg_covar=1e-4, n_init=5, random_state=42)
    gm.fit(X)
    aic_vals.append(gm.aic(X))
    bic_vals.append(gm.bic(X))

best_aic = list(k_range)[np.argmin(aic_vals)]
best_bic = list(k_range)[np.argmin(bic_vals)]
print(f"AIC selects k={best_aic},  BIC selects k={best_bic}")
print(f"\n{'k':>4} {'AIC':>12} {'BIC':>12}")
for k, a, b in zip(k_range, aic_vals, bic_vals):
    mark_a = " <<" if k == best_aic else ""
    mark_b = " <<" if k == best_bic else ""
    print(f"{k:>4} {a:>12.2f}{mark_a:4s} {b:>12.2f}{mark_b}")
```

## GMM for Anomaly Detection

GMMs provide a full density estimate p(x), making them natural for anomaly detection. A point x is anomalous if log p(x) falls below a threshold τ chosen to accept a desired false-positive rate on the training data. This approach is non-parametric in the sense that the anomaly threshold adapts to the learned data distribution, handling multi-modal data better than single-Gaussian methods. The threshold is typically set at a low percentile (e.g., 2nd or 5th percentile) of the training log-likelihoods.

```python
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

rng = np.random.default_rng(42)
X_normal, _ = make_blobs(n_samples=400, centers=3, cluster_std=0.7, random_state=0)
X_anomaly = rng.uniform(-6, 6, size=(30, 2))
X_normal = StandardScaler().fit_transform(X_normal)
X_anomaly = (X_anomaly - X_anomaly.mean(axis=0)) / X_anomaly.std(axis=0)

gm = GaussianMixture(n_components=3, covariance_type='full', n_init=5, random_state=42)
gm.fit(X_normal)

log_probs_train = gm.score_samples(X_normal)
threshold = np.percentile(log_probs_train, 2)

log_probs_normal = gm.score_samples(X_normal)
log_probs_anomaly = gm.score_samples(X_anomaly)

fpr = (log_probs_normal < threshold).mean()
detection_rate = (log_probs_anomaly < threshold).mean()

print(f"Threshold (2nd percentile): {threshold:.4f}")
print(f"False positive rate on training data: {fpr:.2%}")
print(f"Anomaly detection rate: {detection_rate:.2%}")
print(f"Train log-prob: mean={log_probs_train.mean():.2f}, min={log_probs_train.min():.2f}")
print(f"Anomaly log-prob: mean={log_probs_anomaly.mean():.2f}, min={log_probs_anomaly.min():.2f}")
```

> **GMM vs K-Means — The Hard Assignment Limit**: K-means is a special case of GMM with spherical (isotropic) covariances and hard assignments. As the covariance scale σ→0, the soft GMM responsibilities rᵢₖ converge to one-hot cluster assignments, recovering exactly the k-means objective. This means GMM generalizes k-means to elliptical clusters and probabilistic membership — at the cost of more parameters and slower convergence.

## Degenerate Covariances and Regularization

A GMM covariance becomes degenerate when a component collapses to fit only one or a few points: its determinant approaches zero and the likelihood spike to +∞, causing numerical instability and false convergence. This over-fitting happens when k is too large relative to n, or when two components overlap severely. The fix is regularization: add reg_covar (default 1e-6) to the diagonal of each Σₖ, equivalent to adding a weak spherical prior. If degenerate covariances persist, reduce k or switch from 'full' to 'tied' or 'diag' covariance type.

## Practical Notes and Pitfalls

- Always set reg_covar > 0 (default 1e-6 in sklearn) to prevent degenerate covariances when a component collapses to a single point.
- Use n_init >= 5 — GMM EM is sensitive to initialization; multiple restarts with random initialization are standard.
- Full covariance with small clusters and high d can overfit; prefer diagonal or tied covariance as a starting point.
- BIC is the standard model selection criterion for GMMs; prefer it over AIC as sample size grows.
- GMM log-likelihood is not directly comparable across different numbers of components without penalization (AIC/BIC).
- For streaming data, use online EM or the sklearn partial_fit interface for incremental updates.

---

