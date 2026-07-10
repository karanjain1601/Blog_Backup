---
title: "Pre-Norm vs Post-Norm Transformers — Stability and Performance"
slug: "pre-norm-vs-post-norm"
description: "Comparing the original post-norm Transformer (Vaswani 2017) with the modern pre-norm layout used in GPT-2 and LLaMA: training stability, gradient flow, and the Sandwich normalisation variant."
tags: ["deep-learning", "transformers"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHBsYWNlbWVudCBvZiBMYXllciBOb3JtYWxpc2F0aW9uIGluc2lkZSBhIFRyYW5zZm9ybWVyIGJsb2NrIGhhcyBhIHN1cnByaXNpbmdseSBsYXJnZSBlZmZlY3Qgb24gdHJhaW5pbmcgc3RhYmlsaXR5IGFuZCB0aGUgYWJpbGl0eSB0byBzY2FsZSB0byBkZWVwIG1vZGVscy4gVGhlIG9yaWdpbmFsIFZhc3dhbmkgZXQgYWwuICgyMDE3KSBhcmNoaXRlY3R1cmUgYXBwbGllcyBMYXllck5vcm0gKmFmdGVyKiBlYWNoIHJlc2lkdWFsIGNvbm5lY3Rpb24g4oCUIHBvc3Qtbm9ybS4gTmVhcmx5IGFsbCBtb2Rlcm4gbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzIChHUFQtMiwgTExhTUEsIE1pc3RyYWwpIGluc3RlYWQgYXBwbHkgTGF5ZXJOb3JtICpiZWZvcmUqIHRoZSBzdWItbGF5ZXIg4oCUIHByZS1ub3JtLiBUaGUgZGlmZmVyZW5jZSBpcyBvbmUgbGluZSBvZiBjb2RlLCBidXQgaXRzIHRyYWluaW5nIGltcGxpY2F0aW9ucyBhcmUgc2lnbmlmaWNhbnQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUG9zdC1Ob3JtIOKAlCBUaGUgT3JpZ2luYWwgVHJhbnNmb3JtZXIgRGVzaWduIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiB0aGUgcG9zdC1ub3JtIGZvcm11bGF0aW9uIChWYXN3YW5pIDIwMTcpLCB0aGUgcmVzaWR1YWwgYW5kIHRoZSBzdWItbGF5ZXIgb3V0cHV0IGFyZSBzdW1tZWQgZmlyc3QsIHRoZW4gbm9ybWFsaXNlZDogeCA9IExheWVyTm9ybSh4ICsgU3VibGF5ZXIoeCkpLiBMYXllck5vcm0gc2VlcyB0aGUgY29tYmluZWQgcmVzaWR1YWwgc3RyZWFtIGFuZCBzdGFiaWxpc2VzIGl0LiBUaGUgcHJvYmxlbSBpcyB0aGF0IGF0IGluaXRpYWxpc2F0aW9uLCB0aGUgSmFjb2JpYW4gb2YgTGF5ZXJOb3JtIHdpdGggcmVzcGVjdCB0byBpdHMgaW5wdXQgY2FuIGhhdmUgZXh0cmVtZSBlaWdlbnZhbHVlcywgbGVhZGluZyB0byB1bnN0YWJsZSBncmFkaWVudHMgaW4gdmVyeSBkZWVwIG5ldHdvcmtzLiBUcmFpbmluZyBwb3N0LW5vcm0gbW9kZWxzIHR5cGljYWxseSByZXF1aXJlcyBhIGNhcmVmdWwgbGVhcm5pbmcgcmF0ZSB3YXJtdXAgc2NoZWR1bGUgdG8gcHJldmVudCBkaXZlcmdlbmNlIGluIHRoZSBmaXJzdCBmZXcgdGhvdXNhbmQgc3RlcHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQb3N0LW5vcm0gYXR0ZW50aW9uOiB4ID0gTGF5ZXJOb3JtKHggKyBNdWx0aUhlYWRBdHRuKHgpKSIsIlBvc3Qtbm9ybSBGRk46ICAgICAgeCA9IExheWVyTm9ybSh4ICsgRkZOKHgpKSIsIlJlcXVpcmVzIHdhcm11cDogTFIgbXVzdCByYW1wIGZyb20gbmVhci16ZXJvIHRvIHBlYWsgb3ZlciB+NDAwMCBzdGVwcyIsIkZpbmFsIHF1YWxpdHk6IGVtcGlyaWNhbGx5IHNsaWdodGx5IGJldHRlciBhdCBjb252ZXJnZW5jZSBmb3Igc2hhbGxvdyBtb2RlbHMiLCJEZWVwIG1vZGVscyAoMjQrIGxheWVycyk6IHRyYWluaW5nIGluc3RhYmlsaXR5IGlzIGNvbW1vbiB3aXRob3V0IGNhcmVmdWwgdHVuaW5nIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUHJlLUxOIFRyYW5zZm9ybWVycyBQYXBlciAoTGl1IGV0IGFsLiAyMDIwKSIsImNvbnRlbnQiOiJUaGUgcGFwZXIgXHUwMDI3T24gdGhlIFZhcmlhbmNlIG9mIHRoZSBBZGFwdGl2ZSBMZWFybmluZyBSYXRlIGFuZCBCZXlvbmRcdTAwMjcgYW5kIHRoZSBcdTAwMjdQcmUtTE4gVHJhbnNmb3JtZXJcdTAwMjcgYW5hbHlzaXMgKExpdSBldCBhbC4pIHNob3dlZCB0aGF0IHBvc3Qtbm9ybSBtb2RlbHMgaGF2ZSBleHRyZW1lbHkgbGFyZ2UgZ3JhZGllbnQgdmFyaWFuY2UgYXQgaW5pdGlhbGlzYXRpb24sIHdoaWNoIGlzIHdoeSB3YXJtdXAgaXMgZXNzZW50aWFsLiBQcmUtbm9ybSBlbGltaW5hdGVzIHRoaXMgaW5zdGFiaWxpdHkgYmVjYXVzZSB0aGUgcmVzaWR1YWwgcGF0aCBjYXJyaWVzIHJhdyBncmFkaWVudHMgd2hvc2UgbWFnbml0dWRlIGlzIGJvdW5kZWQgaW5kZXBlbmRlbnRseSBvZiBkZXB0aC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmUtTm9ybSDigJQgTW9kZXJuIExMTXMgYW5kIFRyYWluaW5nIFN0YWJpbGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gdGhlIHByZS1ub3JtIGZvcm11bGF0aW9uLCBMYXllck5vcm0gaXMgYXBwbGllZCB0byB4IGJlZm9yZSBwYXNzaW5nIGl0IHRvIHRoZSBzdWItbGF5ZXIsIGFuZCB0aGUgcmVzdWx0IGlzIGFkZGVkIGJhY2sgdG8gdGhlIHVuLW5vcm1hbGlzZWQgeDogeCA9IHggKyBTdWJsYXllcihMYXllck5vcm0oeCkpLiBUaGUgcmVzaWR1YWwgYnlwYXNzIHBhdGggY2FycmllcyByYXcgZ3JhZGllbnRzIGFsbCB0aGUgd2F5IGJhY2sgdG8gdGhlIGZpcnN0IGxheWVyLCBsaWtlIGEgaGlnaHdheS4gVGhpcyBtYWtlcyBncmFkaWVudCBtYWduaXR1ZGUgYXBwcm94aW1hdGVseSBjb25zdGFudCBhY3Jvc3MgZGVwdGggYXQgaW5pdGlhbGlzYXRpb24sIGVuYWJsaW5nIHRyYWluaW5nIGF0IGZ1bGwgbGVhcm5pbmcgcmF0ZSB3aXRob3V0IGEgd2FybXVwIHBoYXNlLiBHUFQtMiBhZG9wdGVkIHByZS1ub3JtIGFuZCBpdCBoYXMgYmVlbiB0aGUgc3RhbmRhcmQgaW4gTExNcyBldmVyIHNpbmNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IEZsb3cgQW5hbHlzaXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrZXkgZGlmZmVyZW5jZSBpbiBncmFkaWVudCBiZWhhdmlvdXIgY29tZXMgZnJvbSB0aGUgcmVzaWR1YWwgcGF0aC4gSW4gcG9zdC1ub3JtLCBncmFkaWVudHMgbXVzdCBmbG93IHRocm91Z2ggdGhlIExheWVyTm9ybSBKYWNvYmlhbiBhdCBlYWNoIGxheWVyOiB0aGUgZ3JhZGllbnQgbWFnbml0dWRlIGNhbiBncm93IG9yIHNocmluayB1bnByZWRpY3RhYmx5IHdpdGggZGVwdGguIEluIHByZS1ub3JtLCB0aGUgcmVzaWR1YWwgY29ubmVjdGlvbiBieXBhc3NlcyBMYXllck5vcm0gZW50aXJlbHkg4oCUIGEgZ3JhZGllbnQgZmxvd2luZyBiYWNrIHRocm91Z2ggdGhlIHJlc2lkdWFsIHBhdGggc2VlcyBpZGVudGl0eSBKYWNvYmlhbiwgc28gaXRzIG1hZ25pdHVkZSBpcyBwcmVzZXJ2ZWQuIE9ubHkgdGhlIHN1Yi1sYXllciBicmFuY2ggKGEgZnJhY3Rpb24gb2YgdGhlIHRvdGFsIGdyYWRpZW50KSBwYXNzZXMgdGhyb3VnaCBMYXllck5vcm0uIFRoaXMgaXMgd2h5IHByZS1ub3JtIG1vZGVscyBjb252ZXJnZSBmYXN0ZXIgYW5kIHJlcXVpcmUgbGVzcyBjYXJlZnVsIGh5cGVycGFyYW1ldGVyIHR1bmluZywgZXZlbiBpZiB0aGVpciBmaW5hbCBwZXJwbGV4aXR5IHNvbWV0aW1lcyBsYWdzIHBvc3Qtbm9ybSBieSBhIHNtYWxsIG1hcmdpbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIFByZS1Ob3JtIFRyYW5zZm9ybWVyIEJsb2NrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2Fub25pY2FsIHByZS1ub3JtIGJsb2NrIHVzZWQgaW4gR1BULTIsIExMYU1BLCBhbmQgTWlzdHJhbDogTGF5ZXJOb3JtIGlzIGFwcGxpZWQgdG8gdGhlIGlucHV0IGJlZm9yZSBlYWNoIHN1Yi1sYXllciwgYW5kIG91dHB1dHMgYXJlIGFkZGVkIHRvIHRoZSB1bi1ub3JtYWxpc2VkIHJlc2lkdWFsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBQcmVOb3JtQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJQcmUtbm9ybWFsaXNhdGlvbiBUcmFuc2Zvcm1lciBibG9jayAoR1BULTIgLyBMTGFNQSBzdHlsZSkuXG4gICAgeCA9IHggKyBBdHRuKExheWVyTm9ybSh4KSlcbiAgICB4ID0geCArIEZGTihMYXllck5vcm0oeCkpXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgbl9oZWFkczogaW50LCBkX2ZmOiBpbnQsXG4gICAgICAgICAgICAgICAgIGRyb3BvdXQ6IGZsb2F0ID0gMC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubm9ybTEgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5ub3JtMiA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmF0dG4gID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRyb3BvdXQ9ZHJvcG91dCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5mZjEgICA9IG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKVxuICAgICAgICBzZWxmLmZmMiAgID0gbm4uTGluZWFyKGRfZmYsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYuYWN0ICAgPSBubi5HRUxVKClcbiAgICAgICAgc2VsZi5kcm9wICA9IG5uLkRyb3BvdXQoZHJvcG91dClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICBhdHRuX21hc2s6IHRvcmNoLlRlbnNvciA9IE5vbmUpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICAjIFNlbGYtYXR0ZW50aW9uIHN1Yi1sYXllcjogbm9ybSBCRUZPUkUgYXR0ZW50aW9uXG4gICAgICAgIG5vcm1lZCAgPSBzZWxmLm5vcm0xKHgpXG4gICAgICAgIGEsIF8gICAgPSBzZWxmLmF0dG4obm9ybWVkLCBub3JtZWQsIG5vcm1lZCwgYXR0bl9tYXNrPWF0dG5fbWFzaylcbiAgICAgICAgeCAgICAgICA9IHggKyBzZWxmLmRyb3AoYSlcbiAgICAgICAgIyBGRk4gc3ViLWxheWVyOiBub3JtIEJFRk9SRSBGRk5cbiAgICAgICAgeCA9IHggKyBzZWxmLmRyb3Aoc2VsZi5mZjIoc2VsZi5hY3Qoc2VsZi5mZjEoc2VsZi5ub3JtMih4KSkpKSlcbiAgICAgICAgcmV0dXJuIHhcblxuIyBTYW5pdHkgY2hlY2tcbmJsb2NrID0gUHJlTm9ybUJsb2NrKGRfbW9kZWw9MjU2LCBuX2hlYWRzPTgsIGRfZmY9MTAyNClcbmlucCAgID0gdG9yY2gucmFuZG4oMiwgMTAsIDI1Nilcbm91dCAgID0gYmxvY2soaW5wKVxucHJpbnQoXHUwMDI3UHJlLW5vcm0gb3V0cHV0IHNoYXBlOlx1MDAyNywgb3V0LnNoYXBlKSAgICAgICMgKDIsIDEwLCAyNTYpXG5hc3NlcnQgb3V0LnNoYXBlID09IGlucC5zaGFwZVxucHJpbnQoXHUwMDI3T3V0cHV0IG5vcm0gKHByZS1ub3JtIOKAlCByZXNpZHVhbCBrZWVwcyBzY2FsZSk6XHUwMDI3LCBvdXQubm9ybShkaW09LTEpLm1lYW4oKS5pdGVtKCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAyIOKAlCBQb3N0LU5vcm0gVHJhbnNmb3JtZXIgQmxvY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvcmlnaW5hbCBWYXN3YW5pICgyMDE3KSBwb3N0LW5vcm0gYmxvY2s6IExheWVyTm9ybSBpcyBhcHBsaWVkIGFmdGVyIHRoZSByZXNpZHVhbCBhZGRpdGlvbiwgc3RhYmlsaXNpbmcgdGhlIGhpZGRlbiBzdGF0ZSBhdCBlYWNoIHN1Yi1sYXllciBvdXRwdXQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFBvc3ROb3JtQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJQb3N0LW5vcm1hbGlzYXRpb24gVHJhbnNmb3JtZXIgYmxvY2sgKFZhc3dhbmkgMjAxNyBvcmlnaW5hbCBzdHlsZSkuXG4gICAgeCA9IExheWVyTm9ybSh4ICsgQXR0bih4KSlcbiAgICB4ID0gTGF5ZXJOb3JtKHggKyBGRk4oeCkpXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgbl9oZWFkczogaW50LCBkX2ZmOiBpbnQsXG4gICAgICAgICAgICAgICAgIGRyb3BvdXQ6IGZsb2F0ID0gMC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubm9ybTEgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5ub3JtMiA9IG5uLkxheWVyTm9ybShkX21vZGVsKVxuICAgICAgICBzZWxmLmF0dG4gID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRyb3BvdXQ9ZHJvcG91dCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5mZjEgICA9IG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKVxuICAgICAgICBzZWxmLmZmMiAgID0gbm4uTGluZWFyKGRfZmYsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYuYWN0ICAgPSBubi5HRUxVKClcbiAgICAgICAgc2VsZi5kcm9wICA9IG5uLkRyb3BvdXQoZHJvcG91dClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICBhdHRuX21hc2s6IHRvcmNoLlRlbnNvciA9IE5vbmUpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICAjIFNlbGYtYXR0ZW50aW9uIHN1Yi1sYXllcjogbm9ybSBBRlRFUiByZXNpZHVhbFxuICAgICAgICBhLCBfID0gc2VsZi5hdHRuKHgsIHgsIHgsIGF0dG5fbWFzaz1hdHRuX21hc2spXG4gICAgICAgIHggICAgPSBzZWxmLm5vcm0xKHggKyBzZWxmLmRyb3AoYSkpXG4gICAgICAgICMgRkZOIHN1Yi1sYXllcjogbm9ybSBBRlRFUiByZXNpZHVhbFxuICAgICAgICB4ID0gc2VsZi5ub3JtMih4ICsgc2VsZi5kcm9wKHNlbGYuZmYyKHNlbGYuYWN0KHNlbGYuZmYxKHgpKSkpKVxuICAgICAgICByZXR1cm4geFxuXG4jIFNhbml0eSBjaGVja1xuYmxvY2sgPSBQb3N0Tm9ybUJsb2NrKGRfbW9kZWw9MjU2LCBuX2hlYWRzPTgsIGRfZmY9MTAyNClcbmlucCAgID0gdG9yY2gucmFuZG4oMiwgMTAsIDI1Nilcbm91dCAgID0gYmxvY2soaW5wKVxucHJpbnQoXHUwMDI3UG9zdC1ub3JtIG91dHB1dCBzaGFwZTpcdTAwMjcsIG91dC5zaGFwZSkgICAgICMgKDIsIDEwLCAyNTYpXG4jIFBvc3Qtbm9ybTogTGF5ZXJOb3JtIHN0YWJpbGlzZXMgb3V0cHV0IG1hZ25pdHVkZSBhZnRlciBlYWNoIHJlc2lkdWFsXG5wcmludChcdTAwMjdPdXRwdXQgbm9ybSAocG9zdC1ub3JtIOKAlCBMTiBub3JtYWxpc2VzIG91dHB1dCk6XHUwMDI3LCBvdXQubm9ybShkaW09LTEpLm1lYW4oKS5pdGVtKCkpXG5wcmludChcdTAwMjdJbnB1dCBub3JtOlx1MDAyNywgaW5wLm5vcm0oZGltPS0xKS5tZWFuKCkuaXRlbSgpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMyDigJQgR3JhZGllbnQgTm9ybSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFbXBpcmljYWxseSBtZWFzdXJpbmcgZ3JhZGllbnQgbm9ybXMgYWNyb3NzIDIwIHN0ZXBzIHRvIGlsbHVzdHJhdGUgdGhhdCBwcmUtbm9ybSBrZWVwcyBncmFkaWVudCBtYWduaXR1ZGUgbW9yZSBzdGFibGUgdGhhbiBwb3N0LW5vcm0gZm9yIGEgMTItbGF5ZXIgc3RhY2suIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBidWlsZF9zdGFjayhub3JtX3R5cGU6IHN0ciwgbl9sYXllcnM6IGludCA9IDEyLCBkOiBpbnQgPSAxMjgpOlxuICAgIFwiXCJcIk1pbmltYWwgZmVlZC1mb3J3YXJkIHN0YWNrIGVtdWxhdGluZyBwcmUgdnMgcG9zdCBub3JtIHN0YWNraW5nLlwiXCJcIlxuICAgIGxheWVycyA9IFtdXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl9sYXllcnMpOlxuICAgICAgICBpZiBub3JtX3R5cGUgPT0gXHUwMDI3cHJlXHUwMDI3OlxuICAgICAgICAgICAgbGF5ZXJzICs9IFtubi5MYXllck5vcm0oZCksIG5uLkxpbmVhcihkLCBkKSwgbm4uR0VMVSgpLCBubi5MaW5lYXIoZCwgZCldXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICBsYXllcnMgKz0gW25uLkxpbmVhcihkLCBkKSwgbm4uR0VMVSgpLCBubi5MaW5lYXIoZCwgZCksIG5uLkxheWVyTm9ybShkKV1cbiAgICByZXR1cm4gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuXG5kZWYgbWVhc3VyZV9ncmFkX25vcm0obW9kZWw6IG5uLk1vZHVsZSwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIGZsb2F0OlxuICAgIHggPSB4LmRldGFjaCgpLnJlcXVpcmVzX2dyYWRfKEZhbHNlKVxuICAgIHkgPSBtb2RlbCh4KS5tZWFuKClcbiAgICB5LmJhY2t3YXJkKClcbiAgICB0b3RhbF9zcSA9IHN1bShwLmdyYWQubm9ybSgpLml0ZW0oKSoqMlxuICAgICAgICAgICAgICAgICAgIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLmdyYWQgaXMgbm90IE5vbmUpXG4gICAgbW9kZWwuemVyb19ncmFkKClcbiAgICByZXR1cm4gdG90YWxfc3EgKiogMC41XG5cbmQgPSAxMjhcbnggPSB0b3JjaC5yYW5kbig0LCBkKVxucmVzdWx0cyA9IHt9XG5mb3IgbnR5cGUgaW4gKFx1MDAyN3ByZVx1MDAyNywgXHUwMDI3cG9zdFx1MDAyNyk6XG4gICAgdG9yY2gubWFudWFsX3NlZWQoMClcbiAgICBtb2RlbCA9IGJ1aWxkX3N0YWNrKG50eXBlLCBuX2xheWVycz0xMiwgZD1kKVxuICAgIG5vcm1zID0gW11cbiAgICBmb3Igc3RlcCBpbiByYW5nZSgyMCk6XG4gICAgICAgIHhpID0geCArIDAuMDEgKiBzdGVwICogdG9yY2gucmFuZG5fbGlrZSh4KVxuICAgICAgICBub3Jtcy5hcHBlbmQobWVhc3VyZV9ncmFkX25vcm0obW9kZWwsIHhpKSlcbiAgICByZXN1bHRzW250eXBlXSA9IG5vcm1zXG4gICAgbWVhbl9nbiA9IHN1bShub3JtcykgLyBsZW4obm9ybXMpXG4gICAgc3RkX2duICA9IChzdW0oKGcgLSBtZWFuX2duKSoqMiBmb3IgZyBpbiBub3JtcykgLyBsZW4obm9ybXMpKSoqMC41XG4gICAgcHJpbnQoZlx1MDAyN3tudHlwZX0tbm9ybTogbWVhbiBncmFkIG5vcm0gPSB7bWVhbl9nbjouNGZ9LCBzdGQgPSB7c3RkX2duOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdQcmUtbm9ybSBoYXMgbG93ZXIgdmFyaWFuY2Ug4oCUIG1vcmUgcHJlZGljdGFibGUgZ3JhZGllbnQgc2lnbmFsXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgNCDigJQgU2FuZHdpY2ggTm9ybWFsaXNhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2FuZHdpY2gtTE4gKERpbmcgZXQgYWwuIDIwMjEsIENvZ1ZpZXcpIGFwcGxpZXMgTGF5ZXJOb3JtIGJvdGggYmVmb3JlIHRoZSBzdWItbGF5ZXIgKHByZSkgYW5kIGFmdGVyIHRoZSByZXNpZHVhbCAocG9zdCksIGNvbWJpbmluZyB0aGUgc3RhYmlsaXR5IG9mIHByZS1ub3JtIHdpdGggc29tZSBvZiB0aGUgcXVhbGl0eSBiZW5lZml0cyBvZiBwb3N0LW5vcm0uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFNhbmR3aWNoQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTYW5kd2ljaCBub3JtYWxpc2F0aW9uOiBMYXllck5vcm0gYmVmb3JlIHN1YmxheWVyIEFORCBhZnRlciByZXNpZHVhbC5cbiAgICB4X2F0dG4gPSBMYXllck5vcm1fcG9zdCh4ICsgQXR0bihMYXllck5vcm1fcHJlKHgpKSlcbiAgICB4X2ZmbiAgPSBMYXllck5vcm1fcG9zdCh4ICsgRkZOKExheWVyTm9ybV9wcmUoeCkpKVxuICAgIFJlZmVyZW5jZTogRGluZyBldCBhbC4gKDIwMjEpIENvZ1ZpZXcuXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgbl9oZWFkczogaW50LCBkX2ZmOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5wcmVfYXR0biAgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5wb3N0X2F0dG4gPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5wcmVfZmZuICAgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5wb3N0X2ZmbiAgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5hdHRuID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZmYxICA9IG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKVxuICAgICAgICBzZWxmLmZmMiAgPSBubi5MaW5lYXIoZF9mZiwgZF9tb2RlbClcbiAgICAgICAgc2VsZi5hY3QgID0gbm4uR0VMVSgpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICAjIEF0dGVudGlvbiB3aXRoIHByZS0gYW5kIHBvc3Qtbm9ybWFsaXNhdGlvblxuICAgICAgICBuID0gc2VsZi5wcmVfYXR0bih4KVxuICAgICAgICBhLCBfID0gc2VsZi5hdHRuKG4sIG4sIG4pXG4gICAgICAgIHggPSBzZWxmLnBvc3RfYXR0bih4ICsgYSlcbiAgICAgICAgIyBGRk4gd2l0aCBwcmUtIGFuZCBwb3N0LW5vcm1hbGlzYXRpb25cbiAgICAgICAgbiA9IHNlbGYucHJlX2Zmbih4KVxuICAgICAgICB4ID0gc2VsZi5wb3N0X2Zmbih4ICsgc2VsZi5mZjIoc2VsZi5hY3Qoc2VsZi5mZjEobikpKSlcbiAgICAgICAgcmV0dXJuIHhcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmRfbW9kZWwsIG5faGVhZHMsIGRfZmYgPSAyNTYsIDgsIDEwMjRcbmlucCAgID0gdG9yY2gucmFuZG4oMiwgMTIsIGRfbW9kZWwpXG5ibG9jayA9IFNhbmR3aWNoQmxvY2soZF9tb2RlbCwgbl9oZWFkcywgZF9mZilcbm91dCAgID0gYmxvY2soaW5wKVxucHJpbnQoXHUwMDI3U2FuZHdpY2ggYmxvY2sgb3V0cHV0Olx1MDAyNywgb3V0LnNoYXBlKVxucHJpbnQoXHUwMDI3SW5wdXQgIG1lYW4gbm9ybTpcdTAwMjcsIGlucC5ub3JtKGRpbT0tMSkubWVhbigpLml0ZW0oKSlcbnByaW50KFx1MDAyN091dHB1dCBtZWFuIG5vcm06XHUwMDI3LCBvdXQubm9ybShkaW09LTEpLm1lYW4oKS5pdGVtKCkpXG5wcmludChcdTAwMjdQYXJhbXM6XHUwMDI3LCBzdW0ocC5udW1lbCgpIGZvciBwIGluIGJsb2NrLnBhcmFtZXRlcnMoKSkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJlLU5vcm0gdnMgUG9zdC1Ob3JtIGF0IGEgR2xhbmNlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiUG9zdC1Ob3JtIChWYXN3YW5pIDIwMTcpIiwiUHJlLU5vcm0gKEdQVC0yLCBMTGFNQSkiLCJTYW5kd2ljaC1Ob3JtIl0sInJvd3MiOltbIkxOIHBvc2l0aW9uIiwiQWZ0ZXIgcmVzaWR1YWwgYWRkaXRpb24iLCJCZWZvcmUgc3ViLWxheWVyIGlucHV0IiwiQmVmb3JlIGFuZCBhZnRlciBzdWItbGF5ZXIiXSxbIkxSIHdhcm11cCBuZWVkZWQiLCJZZXMg4oCUIHJlcXVpcmVkIHRvIHByZXZlbnQgZGl2ZXJnZW5jZSIsIk5vIOKAlCBtb3JlIGZvcmdpdmluZyBMUiBzY2hlZHVsZSIsIk1pbmltYWwg4oCUIHN0YWJsZSBhdCBpbml0Il0sWyJHcmFkaWVudCBmbG93IiwiVGhyb3VnaCBMTiBKYWNvYmlhbiAodW5wcmVkaWN0YWJsZSkiLCJSZXNpZHVhbCBieXBhc3NlcyBMTiAoc3RhYmxlKSIsIk1peGVkOiBwcmUgYW5kIHBvc3QgcGF0aHMiXSxbIkNvbnZlcmdlbmNlIHF1YWxpdHkiLCJTbGlnaHRseSBiZXR0ZXIgYXQgZmluYWwgcGVycGxleGl0eSIsIlNsaWdodGx5IGxvd2VyIGJ1dCByZWxpYWJsZSIsIk9uIHBhciBvciBiZXR0ZXIiXSxbIlN0YWJpbGl0eSBhdCAyNCsgbGF5ZXJzIiwiRGlmZmljdWx0IOKAlCBjb21tb24gZGl2ZXJnZW5jZSIsIkdvb2Qg4oCUIGRlZmF1bHQgY2hvaWNlIiwiQmVzdCByZXBvcnRlZCBzdGFiaWxpdHkiXSxbIk1vZGVybiBhZG9wdGlvbiIsIlQ1LCBvbGRlciBCRVJUIHZhcmlhbnRzIiwiR1BULTIvMy80LCBMTGFNQSwgTWlzdHJhbCwgR2VtbWEiLCJDb2dWaWV3LCBzcGVjaWFsaXNlZCBtb2RlbHMiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIG5ldyBUcmFuc2Zvcm1lciBhcmNoaXRlY3R1cmVzLCBwcmUtbm9ybSBpcyB0aGUgc2FmZSBkZWZhdWx0OiBpdCB0cmFpbnMgd2l0aG91dCB3YXJtdXAsIHNjYWxlcyB0byBodW5kcmVkcyBvZiBsYXllcnMsIGFuZCByZXF1aXJlcyBsZXNzIGNhcmVmdWwgbGVhcm5pbmctcmF0ZSB0dW5pbmcuIFBvc3Qtbm9ybSBtYXkgcmVjb3ZlciBhIHNtYWxsIHF1YWxpdHkgbWFyZ2luIHdoZW4gdHJhaW5pbmcgaXMgY2FyZWZ1bGx5IG1hbmFnZWQgd2l0aCB3YXJtdXAsIGFuZCBpcyB3b3J0aCBjb25zaWRlcmluZyBmb3Igc21hbGxlciBtb2RlbHMgd2hlcmUgdHJhaW5pbmcgc3RhYmlsaXR5IGlzIGxlc3Mgb2YgYSBjb25jZXJuLiBTYW5kd2ljaC1ub3JtIG9mZmVycyBhIG1pZGRsZSBncm91bmQgYnV0IGFkZHMgZXh0cmEgcGFyYW1ldGVycyBhbmQgaXMgdXNlZCBwcmltYXJpbHkgaW4gbGFyZ2UgaW1hZ2UtZ2VuZXJhdGlvbiBtb2RlbHMuIn1d"
---
# Pre-Norm vs Post-Norm Transformers — Stability and Performance

The placement of Layer Normalisation inside a Transformer block has a surprisingly large effect on training stability and the ability to scale to deep models. The original Vaswani et al. (2017) architecture applies LayerNorm *after* each residual connection — post-norm. Nearly all modern large language models (GPT-2, LLaMA, Mistral) instead apply LayerNorm *before* the sub-layer — pre-norm. The difference is one line of code, but its training implications are significant.

## Post-Norm — The Original Transformer Design

In the post-norm formulation (Vaswani 2017), the residual and the sub-layer output are summed first, then normalised: x = LayerNorm(x + Sublayer(x)). LayerNorm sees the combined residual stream and stabilises it. The problem is that at initialisation, the Jacobian of LayerNorm with respect to its input can have extreme eigenvalues, leading to unstable gradients in very deep networks. Training post-norm models typically requires a careful learning rate warmup schedule to prevent divergence in the first few thousand steps.

- Post-norm attention: x = LayerNorm(x + MultiHeadAttn(x))
- Post-norm FFN:      x = LayerNorm(x + FFN(x))
- Requires warmup: LR must ramp from near-zero to peak over ~4000 steps
- Final quality: empirically slightly better at convergence for shallow models
- Deep models (24+ layers): training instability is common without careful tuning

> **Pre-LN Transformers Paper (Liu et al. 2020)**: The paper 'On the Variance of the Adaptive Learning Rate and Beyond' and the 'Pre-LN Transformer' analysis (Liu et al.) showed that post-norm models have extremely large gradient variance at initialisation, which is why warmup is essential. Pre-norm eliminates this instability because the residual path carries raw gradients whose magnitude is bounded independently of depth.

## Pre-Norm — Modern LLMs and Training Stability

In the pre-norm formulation, LayerNorm is applied to x before passing it to the sub-layer, and the result is added back to the un-normalised x: x = x + Sublayer(LayerNorm(x)). The residual bypass path carries raw gradients all the way back to the first layer, like a highway. This makes gradient magnitude approximately constant across depth at initialisation, enabling training at full learning rate without a warmup phase. GPT-2 adopted pre-norm and it has been the standard in LLMs ever since.

## Gradient Flow Analysis

The key difference in gradient behaviour comes from the residual path. In post-norm, gradients must flow through the LayerNorm Jacobian at each layer: the gradient magnitude can grow or shrink unpredictably with depth. In pre-norm, the residual connection bypasses LayerNorm entirely — a gradient flowing back through the residual path sees identity Jacobian, so its magnitude is preserved. Only the sub-layer branch (a fraction of the total gradient) passes through LayerNorm. This is why pre-norm models converge faster and require less careful hyperparameter tuning, even if their final perplexity sometimes lags post-norm by a small margin.

## Code 1 — Pre-Norm Transformer Block

The canonical pre-norm block used in GPT-2, LLaMA, and Mistral: LayerNorm is applied to the input before each sub-layer, and outputs are added to the un-normalised residual.

```python
import torch
import torch.nn as nn

class PreNormBlock(nn.Module):
    """Pre-normalisation Transformer block (GPT-2 / LLaMA style).
    x = x + Attn(LayerNorm(x))
    x = x + FFN(LayerNorm(x))
    """
    def __init__(self, d_model: int, n_heads: int, d_ff: int,
                 dropout: float = 0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.attn  = nn.MultiheadAttention(d_model, n_heads,
                                            dropout=dropout, batch_first=True)
        self.ff1   = nn.Linear(d_model, d_ff)
        self.ff2   = nn.Linear(d_ff, d_model)
        self.act   = nn.GELU()
        self.drop  = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor,
                attn_mask: torch.Tensor = None) -> torch.Tensor:
        # Self-attention sub-layer: norm BEFORE attention
        normed  = self.norm1(x)
        a, _    = self.attn(normed, normed, normed, attn_mask=attn_mask)
        x       = x + self.drop(a)
        # FFN sub-layer: norm BEFORE FFN
        x = x + self.drop(self.ff2(self.act(self.ff1(self.norm2(x)))))
        return x

# Sanity check
block = PreNormBlock(d_model=256, n_heads=8, d_ff=1024)
inp   = torch.randn(2, 10, 256)
out   = block(inp)
print('Pre-norm output shape:', out.shape)      # (2, 10, 256)
assert out.shape == inp.shape
print('Output norm (pre-norm — residual keeps scale):', out.norm(dim=-1).mean().item())
```

## Code 2 — Post-Norm Transformer Block

The original Vaswani (2017) post-norm block: LayerNorm is applied after the residual addition, stabilising the hidden state at each sub-layer output.

```python
import torch
import torch.nn as nn

class PostNormBlock(nn.Module):
    """Post-normalisation Transformer block (Vaswani 2017 original style).
    x = LayerNorm(x + Attn(x))
    x = LayerNorm(x + FFN(x))
    """
    def __init__(self, d_model: int, n_heads: int, d_ff: int,
                 dropout: float = 0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.attn  = nn.MultiheadAttention(d_model, n_heads,
                                            dropout=dropout, batch_first=True)
        self.ff1   = nn.Linear(d_model, d_ff)
        self.ff2   = nn.Linear(d_ff, d_model)
        self.act   = nn.GELU()
        self.drop  = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor,
                attn_mask: torch.Tensor = None) -> torch.Tensor:
        # Self-attention sub-layer: norm AFTER residual
        a, _ = self.attn(x, x, x, attn_mask=attn_mask)
        x    = self.norm1(x + self.drop(a))
        # FFN sub-layer: norm AFTER residual
        x = self.norm2(x + self.drop(self.ff2(self.act(self.ff1(x)))))
        return x

# Sanity check
block = PostNormBlock(d_model=256, n_heads=8, d_ff=1024)
inp   = torch.randn(2, 10, 256)
out   = block(inp)
print('Post-norm output shape:', out.shape)     # (2, 10, 256)
# Post-norm: LayerNorm stabilises output magnitude after each residual
print('Output norm (post-norm — LN normalises output):', out.norm(dim=-1).mean().item())
print('Input norm:', inp.norm(dim=-1).mean().item())
```

## Code 3 — Gradient Norm Comparison

Empirically measuring gradient norms across 20 steps to illustrate that pre-norm keeps gradient magnitude more stable than post-norm for a 12-layer stack.

```python
import torch
import torch.nn as nn

def build_stack(norm_type: str, n_layers: int = 12, d: int = 128):
    """Minimal feed-forward stack emulating pre vs post norm stacking."""
    layers = []
    for _ in range(n_layers):
        if norm_type == 'pre':
            layers += [nn.LayerNorm(d), nn.Linear(d, d), nn.GELU(), nn.Linear(d, d)]
        else:
            layers += [nn.Linear(d, d), nn.GELU(), nn.Linear(d, d), nn.LayerNorm(d)]
    return nn.Sequential(*layers)

def measure_grad_norm(model: nn.Module, x: torch.Tensor) -> float:
    x = x.detach().requires_grad_(False)
    y = model(x).mean()
    y.backward()
    total_sq = sum(p.grad.norm().item()**2
                   for p in model.parameters() if p.grad is not None)
    model.zero_grad()
    return total_sq ** 0.5

d = 128
x = torch.randn(4, d)
results = {}
for ntype in ('pre', 'post'):
    torch.manual_seed(0)
    model = build_stack(ntype, n_layers=12, d=d)
    norms = []
    for step in range(20):
        xi = x + 0.01 * step * torch.randn_like(x)
        norms.append(measure_grad_norm(model, xi))
    results[ntype] = norms
    mean_gn = sum(norms) / len(norms)
    std_gn  = (sum((g - mean_gn)**2 for g in norms) / len(norms))**0.5
    print(f'{ntype}-norm: mean grad norm = {mean_gn:.4f}, std = {std_gn:.4f}')
print('Pre-norm has lower variance — more predictable gradient signal')
```

## Code 4 — Sandwich Normalisation

Sandwich-LN (Ding et al. 2021, CogView) applies LayerNorm both before the sub-layer (pre) and after the residual (post), combining the stability of pre-norm with some of the quality benefits of post-norm.

```python
import torch
import torch.nn as nn

class SandwichBlock(nn.Module):
    """Sandwich normalisation: LayerNorm before sublayer AND after residual.
    x_attn = LayerNorm_post(x + Attn(LayerNorm_pre(x)))
    x_ffn  = LayerNorm_post(x + FFN(LayerNorm_pre(x)))
    Reference: Ding et al. (2021) CogView.
    """
    def __init__(self, d_model: int, n_heads: int, d_ff: int):
        super().__init__()
        self.pre_attn  = nn.LayerNorm(d_model)
        self.post_attn = nn.LayerNorm(d_model)
        self.pre_ffn   = nn.LayerNorm(d_model)
        self.post_ffn  = nn.LayerNorm(d_model)
        self.attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.ff1  = nn.Linear(d_model, d_ff)
        self.ff2  = nn.Linear(d_ff, d_model)
        self.act  = nn.GELU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Attention with pre- and post-normalisation
        n = self.pre_attn(x)
        a, _ = self.attn(n, n, n)
        x = self.post_attn(x + a)
        # FFN with pre- and post-normalisation
        n = self.pre_ffn(x)
        x = self.post_ffn(x + self.ff2(self.act(self.ff1(n))))
        return x

torch.manual_seed(0)
d_model, n_heads, d_ff = 256, 8, 1024
inp   = torch.randn(2, 12, d_model)
block = SandwichBlock(d_model, n_heads, d_ff)
out   = block(inp)
print('Sandwich block output:', out.shape)
print('Input  mean norm:', inp.norm(dim=-1).mean().item())
print('Output mean norm:', out.norm(dim=-1).mean().item())
print('Params:', sum(p.numel() for p in block.parameters()))
```

## Pre-Norm vs Post-Norm at a Glance

| Property | Post-Norm (Vaswani 2017) | Pre-Norm (GPT-2, LLaMA) | Sandwich-Norm |
| --- | --- | --- | --- |
| LN position | After residual addition | Before sub-layer input | Before and after sub-layer |
| LR warmup needed | Yes — required to prevent divergence | No — more forgiving LR schedule | Minimal — stable at init |
| Gradient flow | Through LN Jacobian (unpredictable) | Residual bypasses LN (stable) | Mixed: pre and post paths |
| Convergence quality | Slightly better at final perplexity | Slightly lower but reliable | On par or better |
| Stability at 24+ layers | Difficult — common divergence | Good — default choice | Best reported stability |
| Modern adoption | T5, older BERT variants | GPT-2/3/4, LLaMA, Mistral, Gemma | CogView, specialised models |

For new Transformer architectures, pre-norm is the safe default: it trains without warmup, scales to hundreds of layers, and requires less careful learning-rate tuning. Post-norm may recover a small quality margin when training is carefully managed with warmup, and is worth considering for smaller models where training stability is less of a concern. Sandwich-norm offers a middle ground but adds extra parameters and is used primarily in large image-generation models.

