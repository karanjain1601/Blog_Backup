---
title: "BLIP-2: Q-Former Bridging Vision and Language Models"
slug: "blip2-qformer"
description: ""
tags: ["blip2", "qformer", "bootstrapping", "frozen-llm", "salesforce"]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCTElQLTIgKEJvb3RzdHJhcHBpbmcgTGFuZ3VhZ2UtSW1hZ2UgUHJldHJhaW5pbmcpIGZyb20gU2FsZXNmb3JjZSBSZXNlYXJjaCBpbnRyb2R1Y2VzIHRoZSBRLUZvcm1lciwgYSBsaWdodHdlaWdodCB0cmFuc2Zvcm1lciBtb2R1bGUgdGhhdCBicmlkZ2VzIGEgZnJvemVuIGltYWdlIGVuY29kZXIgYW5kIGEgZnJvemVuIGxhcmdlIGxhbmd1YWdlIG1vZGVsLiBCeSBrZWVwaW5nIGJvdGggcHJlLXRyYWluZWQgY29tcG9uZW50cyBmcm96ZW4sIEJMSVAtMiBhY2hpZXZlcyBzdGF0ZS1vZi10aGUtYXJ0IG11bHRpbW9kYWwgcGVyZm9ybWFuY2Ugd2l0aCBtaW5pbWFsIHRyYWluYWJsZSBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNlbnRyYWwgY2hhbGxlbmdlIEJMSVAtMiBhZGRyZXNzZXMgaXMgdGhlIG1vZGFsaXR5IGdhcDogaW1hZ2UgZW5jb2RlciBhbmQgTExNIGVtYmVkZGluZyBzcGFjZXMgYXJlIGxlYXJuZWQgaW5kZXBlbmRlbnRseSBhbmQgaW5jb21wYXRpYmxlIG91dCBvZiB0aGUgYm94LiBUaGUgUS1Gb3JtZXIgc29sdmVzIHRoaXMgYnkgbGVhcm5pbmcgdG8gdHJhbnNsYXRlIGJldHdlZW4gdGhlbSB1c2luZyBvbmx5IDE4OE0gdHJhaW5hYmxlIHBhcmFtZXRlcnMsIHdoaWxlIHRoZSBiYWNrYm9uZSBlbmNvZGVycyAoYmlsbGlvbnMgb2YgcGFyYW1ldGVycykgcmVtYWluIGZyb3plbi4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJjb250ZW50IjoiUS1Gb3JtZXIgaXMgdGhlIGNvcmUgaW5ub3ZhdGlvbjogMzIgbGVhcm5lZCBxdWVyaWVzIGRpc3RpbGwgdGhlIGVudGlyZSBpbWFnZSBpbnRvIGEgY29tcGFjdCB2aXN1YWwgcmVwcmVzZW50YXRpb24gdGhhdCBhbnkgZnJvemVuIExMTSBjYW4gY29uZGl0aW9uIG9uLiBUaGlzIGRlY291cGxlcyB2aXNpb24gZW5jb2RlciB1cGdyYWRlcyBmcm9tIExMTSB1cGdyYWRlcyDigJQgc3dhcCBlaXRoZXIgaW5kZXBlbmRlbnRseS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJMSVAtMiB1c2VzIEVWQS1DTElQIFZpVC1HLzE0ICgxQiBwYXJhbXMpIGFzIHRoZSB2aXN1YWwgZW5jb2RlciBhbmQgZWl0aGVyIE9QVCBvciBGbGFuVDUgYXMgdGhlIGxhbmd1YWdlIG1vZGVsLiBEZXNwaXRlIHVzaW5nIGZyb3plbiBiYWNrYm9uZXMsIEJMSVAtMiBGbGFuVDUtWFhMIGFjaGlldmVzIDY1LjAlIG9uIFZRQXYyIGFuZCA0NS45JSBvbiBPSy1WUUEsIG91dHBlcmZvcm1pbmcgRmxhbWluZ28gODBCIHdpdGggNTR4IGZld2VyIHRyYWluYWJsZSBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlEtRm9ybWVyIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFEtRm9ybWVyIGlzIGEgQkVSVC1iYXNlZCB0cmFuc2Zvcm1lciB3aXRoIHR3byBhdHRlbnRpb24gcGF0aHdheXM6IHNlbGYtYXR0ZW50aW9uIGJldHdlZW4gbGVhcm5lZCBxdWVyeSB0b2tlbnMsIGFuZCBjcm9zcy1hdHRlbnRpb24gZnJvbSBxdWVyeSB0b2tlbnMgdG8gZnJvemVuIGltYWdlIHBhdGNoIGZlYXR1cmVzLiBUaGUgMzIgcXVlcnkgdG9rZW5zIChlYWNoIDc2OC1kaW1lbnNpb25hbCkgYXJlIHRoZSBvbmx5IGxlYXJuZWQgdmlzdWFsIHJlcHJlc2VudGF0aW9ucyBwYXNzZWQgZG93bnN0cmVhbSB0byB0aGUgTExNLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBRRm9ybWVyTGF5ZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgbl9oZWFkcywgbl9xdWVyaWVzPTMyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucXVlcnlfdG9rZW5zID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKDEsIG5fcXVlcmllcywgZF9tb2RlbCkpXG4gICAgICAgIHNlbGYuc2VsZl9hdHRuID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG5faGVhZHMsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuY3Jvc3NfYXR0biA9IG5uLk11bHRpaGVhZEF0dGVudGlvbihkX21vZGVsLCBuX2hlYWRzLCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLmZmbiA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKGRfbW9kZWwsIDQqZF9tb2RlbCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBubi5HRUxVKCksIG5uLkxpbmVhcig0KmRfbW9kZWwsIGRfbW9kZWwpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgaW1hZ2VfZmVhdHVyZXMpOlxuICAgICAgICBCID0gaW1hZ2VfZmVhdHVyZXMuc2hhcGVbMF1cbiAgICAgICAgcSA9IHNlbGYucXVlcnlfdG9rZW5zLmV4cGFuZChCLCAtMSwgLTEpXG4gICAgICAgIHEsIF8gPSBzZWxmLnNlbGZfYXR0bihxLCBxLCBxKVxuICAgICAgICBxLCBfID0gc2VsZi5jcm9zc19hdHRuKHEsIGltYWdlX2ZlYXR1cmVzLCBpbWFnZV9mZWF0dXJlcylcbiAgICAgICAgcmV0dXJuIHNlbGYuZmZuKHEpICsgcSAgIyByZXNpZHVhbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIDMyIHF1ZXJ5IHRva2VucyBjb21wcmVzcyB0aGUgZW50aXJlIGltYWdlIOKAlCB3aGljaCBtYXkgaGF2ZSAyNTYgb3IgbW9yZSBwYXRjaCB0b2tlbnMgZnJvbSBWaVQtRy8xNCDigJQgaW50byBhIGZpeGVkLXNpemUgcmVwcmVzZW50YXRpb24uIFRoaXMgY29tcHJlc3Npb24gaXMgbGVhcm5lZCByYXRoZXIgdGhhbiBoYW5kLWRlc2lnbmVkOiB0aGUgUS1Gb3JtZXIgdHJhaW5pbmcgb2JqZWN0aXZlcyB0ZWFjaCBpdCB3aGF0IHZpc3VhbCBpbmZvcm1hdGlvbiBpcyByZWxldmFudCBmb3IgbGFuZ3VhZ2UgdW5kZXJzdGFuZGluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdGFnZS0xIFZpc2lvbi1MYW5ndWFnZSBQcmV0cmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhZ2UtMSB0cmFpbnMgdGhlIFEtRm9ybWVyIHdpdGggdGhyZWUgb2JqZWN0aXZlcyBzaW11bHRhbmVvdXNseSwgdXNpbmcgMTI5TSBpbWFnZS10ZXh0IHBhaXJzLiBUaGUgaW1hZ2UgZW5jb2RlciBpcyBmcm96ZW47IG9ubHkgUS1Gb3JtZXIgd2VpZ2h0cyBhcmUgdXBkYXRlZC4gVGhlIHRocmVlIGxvc3NlcyB0b2dldGhlciB0ZWFjaCB0aGUgUS1Gb3JtZXIgdG8gZXh0cmFjdCBpbWFnZSBmZWF0dXJlcyB1c2VmdWwgZm9yIG1hdGNoaW5nLCBkaXNjcmltaW5hdGluZywgYW5kIGdlbmVyYXRpbmcgdGV4dCBkZXNjcmlwdGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiBxZm9ybWVyX3N0YWdlMV9sb3NzZXMocXVlcnlfb3V0cHV0LCB0ZXh0X291dHB1dCwgaW1hZ2VfZW1iZWRzLCB0ZXh0X2lkcywgbW9kZWwpOlxuICAgICMgMS4gSW1hZ2UtVGV4dCBDb250cmFzdGl2ZSAoSVRDKSDigJQgYWxpZ24gW0NMU10gb2YgcXVlcnkgYW5kIHRleHRcbiAgICBxX2ZlYXQgPSBGLm5vcm1hbGl6ZShtb2RlbC5pdGNfcXVlcnlfcHJvaihxdWVyeV9vdXRwdXRbOiwgMF0pLCBkaW09LTEpXG4gICAgdF9mZWF0ID0gRi5ub3JtYWxpemUobW9kZWwuaXRjX3RleHRfcHJvaih0ZXh0X291dHB1dFs6LCAwXSksIGRpbT0tMSlcbiAgICBzaW1fbWF0cml4ID0gcV9mZWF0IEAgdF9mZWF0LlQgLyBtb2RlbC50ZW1wXG4gICAgbGFiZWxzID0gdG9yY2guYXJhbmdlKHNpbV9tYXRyaXguc2l6ZSgwKSwgZGV2aWNlPXNpbV9tYXRyaXguZGV2aWNlKVxuICAgIGl0Y19sb3NzID0gKEYuY3Jvc3NfZW50cm9weShzaW1fbWF0cml4LCBsYWJlbHMpICtcbiAgICAgICAgICAgICAgICBGLmNyb3NzX2VudHJvcHkoc2ltX21hdHJpeC5ULCBsYWJlbHMpKSAvIDJcbiAgICAjIDIuIEltYWdlLVRleHQgTWF0Y2hpbmcgKElUTSkg4oCUIGJpbmFyeSBjbGFzc2lmaWNhdGlvbiBvbiBmdXNlZCBmZWF0dXJlc1xuICAgIGl0bV9sb2dpdHMgPSBtb2RlbC5pdG1faGVhZChxdWVyeV9vdXRwdXQpICAjIChCLCAyKVxuICAgIGl0bV9sb3NzID0gRi5jcm9zc19lbnRyb3B5KGl0bV9sb2dpdHMsIG1vZGVsLml0bV9sYWJlbHMpXG4gICAgIyAzLiBJbWFnZS1Hcm91bmRlZCBUZXh0IEdlbmVyYXRpb24gKElURykg4oCUIGNhdXNhbCBMTSBvbiBxdWVyeSt0ZXh0XG4gICAgaXRnX2xvc3MgPSBtb2RlbC5sbV9oZWFkX2xvc3MocXVlcnlfb3V0cHV0LCB0ZXh0X2lkcylcbiAgICByZXR1cm4gaXRjX2xvc3MgKyBpdG1fbG9zcyArIGl0Z19sb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJVEMgYWxpZ25zIGdsb2JhbCBpbWFnZSBhbmQgdGV4dCByZXByZXNlbnRhdGlvbnMuIElUTSBpcyBhIGJpbmFyeSBjcm9zcy1lbnRyb3B5IGxvc3MgdGhhdCB0ZWFjaGVzIHRoZSBRLUZvcm1lciB0byBkaXN0aW5ndWlzaCBnZW51aW5lIGZyb20gbWlzbWF0Y2hlZCBpbWFnZS10ZXh0IHBhaXJzLiBJVEcgaXMgYXV0b3JlZ3Jlc3NpdmUgdGV4dCBnZW5lcmF0aW9uIGNvbmRpdGlvbmVkIG9uIHF1ZXJ5IHRva2VuIG91dHB1dHMg4oCUIGl0IGZvcmNlcyB0aGUgcXVlcnkgdG9rZW5zIHRvIGNhcHR1cmUgdGV4dC1yZWxldmFudCB2aXN1YWwgaW5mb3JtYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RhZ2UtMiBMYW5ndWFnZSBNb2RlbCBDb25uZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFnZS0yIGNvbm5lY3RzIHRoZSBRLUZvcm1lciBvdXRwdXQgdG8gYSBmcm96ZW4gTExNIHZpYSBhIGxpbmVhciBwcm9qZWN0aW9uLiBUaGUgMzIgcXVlcnkgdG9rZW4gb3V0cHV0cyAoNzY4LWRpbSkgYXJlIHByb2plY3RlZCB0byB0aGUgTExNIGlucHV0IGRpbWVuc2lvbiAoZS5nLiwgMjA0OCBmb3IgT1BULTIuN0IpIGFuZCBwcmVwZW5kZWQgdG8gdGhlIHRleHQgZW1iZWRkaW5nIHNlcXVlbmNlLiBUaGUgTExNIGdlbmVyYXRlcyB0ZXh0IGNvbmRpdGlvbmVkIG9uIHRoaXMgdmlzdWFsIHByZWZpeC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZGVmIGJsaXAyX2dlbmVyYXRlKGltYWdlLCBwcm9tcHRfaWRzLCBtb2RlbCwgbWF4X25ld190b2tlbnM9NTApOlxuICAgICMgRnJvemVuIENMSVAgZW5jb2RlcyBpbWFnZVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBpbWFnZV9mZWF0dXJlcyA9IG1vZGVsLnZpc3VhbF9lbmNvZGVyKGltYWdlKSAgIyAoQiwgMjU3LCAxNDA4KVxuICAgICMgUS1Gb3JtZXIgZXh0cmFjdHMgMzIgcXVlcnkgdG9rZW5zXG4gICAgcXVlcnlfb3V0cHV0ID0gbW9kZWwucWZvcm1lcihpbWFnZV9mZWF0dXJlcykgICAgIyAoQiwgMzIsIDc2OClcbiAgICAjIFByb2plY3QgdG8gTExNIGVtYmVkZGluZyBzcGFjZVxuICAgIHZpc3VhbF9wcmVmaXggPSBtb2RlbC5sYW5ndWFnZV9wcm9qZWN0aW9uKHF1ZXJ5X291dHB1dCkgICMgKEIsIDMyLCBEX2xsbSlcbiAgICAjIEdldCB0ZXh0IGVtYmVkZGluZ3MgYW5kIGNvbmNhdGVuYXRlXG4gICAgdGV4dF9lbWJlZHMgPSBtb2RlbC5sYW5ndWFnZV9tb2RlbC5nZXRfaW5wdXRfZW1iZWRkaW5ncygpKHByb21wdF9pZHMpXG4gICAgaW5wdXRzX2VtYmVkcyA9IHRvcmNoLmNhdChbdmlzdWFsX3ByZWZpeCwgdGV4dF9lbWJlZHNdLCBkaW09MSlcbiAgICAjIEZyb3plbiBMTE0gZ2VuZXJhdGVzXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG91dHB1dHMgPSBtb2RlbC5sYW5ndWFnZV9tb2RlbC5nZW5lcmF0ZShcbiAgICAgICAgICAgIGlucHV0c19lbWJlZHM9aW5wdXRzX2VtYmVkcywgbWF4X25ld190b2tlbnM9bWF4X25ld190b2tlbnMpXG4gICAgcmV0dXJuIG91dHB1dHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBnZW5lcmF0aXZlIExMTXMgKE9QVCksIHRoZSB2aXN1YWwgcHJlZml4IGFjdHMgYXMgYSBzb2Z0IHZpc3VhbCBwcm9tcHQgYW5kIHRoZSBMTE0gZ2VuZXJhdGVzIHRoZSBmdWxsIHJlc3BvbnNlIGF1dG9yZWdyZXNzaXZlbHkuIEZvciBlbmNvZGVyLWRlY29kZXIgTExNcyAoRmxhblQ1KSwgcXVlcnkgdG9rZW5zIGFyZSBwYXNzZWQgdG8gdGhlIGVuY29kZXIsIGFuZCB0aGUgZGVjb2RlciBnZW5lcmF0ZXMgdGhlIGFuc3dlci4gRmxhblQ1LWJhc2VkIHZhcmlhbnRzIGdlbmVyYWxseSBzY29yZSBoaWdoZXIgb24ga25vd2xlZGdlLWludGVuc2l2ZSBWUUEgdGFza3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiWmVyby1TaG90IFZRQSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQkxJUC0yIHN1cHBvcnRzIHplcm8tc2hvdCBWUUEgb3V0IG9mIHRoZSBib3ggdGhyb3VnaCBpdHMgZ2VuZXJhdGl2ZSBpbnRlcmZhY2UuIFRoZSBxdWVzdGlvbiBpcyBmb3JtYXR0ZWQgYXMgYSBwcm9tcHQgYW5kIGNvbmNhdGVuYXRlZCBhZnRlciB0aGUgdmlzdWFsIHByZWZpeCB0b2tlbnMuIFRoZSBmcm96ZW4gTExNIGdlbmVyYXRlcyBhIGZyZWUtZm9ybSBhbnN3ZXIgY29uZGl0aW9uZWQgb24gYm90aCB0aGUgdmlzdWFsIHJlcHJlc2VudGF0aW9uIGFuZCB0aGUgcXVlc3Rpb24gdGV4dCDigJQgbm8gZmluZS10dW5pbmcgcmVxdWlyZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBCbGlwMlByb2Nlc3NvciwgQmxpcDJGb3JDb25kaXRpb25hbEdlbmVyYXRpb25cbmZyb20gUElMIGltcG9ydCBJbWFnZVxuaW1wb3J0IHJlcXVlc3RzXG5pbXBvcnQgdG9yY2hcblxucHJvY2Vzc29yID0gQmxpcDJQcm9jZXNzb3IuZnJvbV9wcmV0cmFpbmVkKFwiU2FsZXNmb3JjZS9ibGlwMi1vcHQtMi43YlwiKVxubW9kZWwgPSBCbGlwMkZvckNvbmRpdGlvbmFsR2VuZXJhdGlvbi5mcm9tX3ByZXRyYWluZWQoXG4gICAgXCJTYWxlc2ZvcmNlL2JsaXAyLW9wdC0yLjdiXCIsIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsIGRldmljZV9tYXA9XCJhdXRvXCIpXG5cbmltYWdlID0gSW1hZ2Uub3BlbihyZXF1ZXN0cy5nZXQoXCJodHRwczovL2V4YW1wbGUuY29tL2ltZy5qcGdcIiwgc3RyZWFtPVRydWUpLnJhdylcbnF1ZXN0aW9uID0gXCJRdWVzdGlvbjogSG93IG1hbnkgcGVvcGxlIGFyZSBpbiB0aGUgaW1hZ2U/IEFuc3dlcjpcIlxuaW5wdXRzID0gcHJvY2Vzc29yKGltYWdlLCBxdWVzdGlvbiwgcmV0dXJuX3RlbnNvcnM9XCJwdFwiKS50byhtb2RlbC5kZXZpY2UsIHRvcmNoLmZsb2F0MTYpXG5nZW5lcmF0ZWQgPSBtb2RlbC5nZW5lcmF0ZSgqKmlucHV0cywgbWF4X25ld190b2tlbnM9MzApXG5wcmludChwcm9jZXNzb3IuZGVjb2RlKGdlbmVyYXRlZFswXSwgc2tpcF9zcGVjaWFsX3Rva2Vucz1UcnVlKSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ilplcm8tc2hvdCBWUUF2MiBhY2N1cmFjeSBmb3IgQkxJUC0yIE9QVC02LjdCIGlzIDYxLjIlLCBjb21wYXJlZCB0byBGbGFtaW5nby04MEIgYXQgNTYuMyUg4oCUIGFjaGlldmVkIHdpdGggYSA1NHggc21hbGxlciBtb2RlbC4gVGhlIGdhcCBjb21lcyBmcm9tIEJMSVAtMlx1MDAyN3Mgc3RhZ2VkIHByZXRyYWluaW5nOiBRLUZvcm1lciBzdGFnZS0xIHByb3ZpZGVzIGEgc3Ryb25nIHZpc3VhbCByZXByZXNlbnRhdGlvbiBiZWZvcmUgdGhlIExMTSBjb25uZWN0aW9uIGlzIGV2ZW4gaW50cm9kdWNlZC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQkxJUC0yIFZhcmlhbnQiLCJMTE0iLCJWaXN1YWwgRW5jb2RlciIsIlZRQXYyICUiLCJPSy1WUUEgJSIsIlBhcmFtcyBUb3RhbCJdLCJyb3dzIjpbWyJCTElQLTIgT1BULTIuN0IiLCJPUFQtMi43QiIsIkVWQS1DTElQIFZpVC1HIiwiNTMuNyIsIjMxLjciLCJ+My40QiJdLFsiQkxJUC0yIE9QVC02LjdCIiwiT1BULTYuN0IiLCJFVkEtQ0xJUCBWaVQtRyIsIjYxLjIiLCIzNi40IiwifjguMkIiXSxbIkJMSVAtMiBGbGFuVDUtWEwiLCJGbGFuVDUtWEwgKDNCKSIsIkVWQS1DTElQIFZpVC1HIiwiNjIuMCIsIjQwLjciLCJ+NC4xQiJdLFsiQkxJUC0yIEZsYW5UNS1YWEwiLCJGbGFuVDUtWFhMICgxMUIpIiwiRVZBLUNMSVAgVmlULUciLCI2NS4wIiwiNDUuOSIsIn4xMi4xQiJdLFsiSW5zdHJ1Y3RCTElQIEZsYW5UNS1YWEwiLCJGbGFuVDUtWFhMICgxMUIpIiwiRVZBLUNMSVAgVmlULUciLCLigJQiLCI1MC43IiwifjEyLjFCIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCTElQLTJcdTAwMjdzIFEtRm9ybWVyIGRlc2lnbiBzb2x2ZXMgYSBmdW5kYW1lbnRhbCBwcm9ibGVtIGluIG11bHRpbW9kYWwgbGVhcm5pbmc6IGhvdyB0byBlZmZpY2llbnRseSBicmlkZ2UgcHJldHJhaW5lZCB1bmltb2RhbCBtb2RlbHMgd2l0aG91dCBjYXRhc3Ryb3BoaWMgZm9yZ2V0dGluZy4gQnkga2VlcGluZyBib3RoIGVuY29kZXJzIGZyb3plbiBhbmQgdHJhaW5pbmcgb25seSB0aGUgMTg4TS1wYXJhbWV0ZXIgYnJpZGdlLCBCTElQLTIgaXMgY29tcHV0ZS1lZmZpY2llbnQgYW5kIG1vZHVsYXIuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdHdvLXN0YWdlIHByZXRyYWluaW5nIGN1cnJpY3VsdW0gaXMgcHJpbmNpcGxlZDogc3RhZ2UtMSBkZXZlbG9wcyByaWNoIHZpc3VhbCByZXByZXNlbnRhdGlvbnMgYWxpZ25lZCB0byBsYW5ndWFnZSwgYW5kIHN0YWdlLTIgdGVhY2hlcyB0aGUgTExNIHRvIHVzZSB0aGVtIGZvciBnZW5lcmF0aW9uLiBUaGlzIHNlcGFyYXRpb24gcHJldmVudHMgdGhlIExMTVx1MDAyN3Mgc3Ryb25nIGxhbmd1YWdlIHByaW9ycyBmcm9tIG92ZXJ3aGVsbWluZyB0aGUgdmlzdWFsIHNpZ25hbCBkdXJpbmcgZWFybHkgdHJhaW5pbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCTElQLTJcdTAwMjdzIGxpbWl0YXRpb25zIGluY2x1ZGUgZml4ZWQgMzItcXVlcnkgY29tcHJlc3Npb24gKG1heSBtaXNzIGZpbmUtZ3JhaW5lZCBkZXRhaWxzKSwgbm8gaW5zdHJ1Y3Rpb24tZm9sbG93aW5nIGNhcGFiaWxpdHkgaW4gdGhlIGJhc2UgbW9kZWwgKGFkZHJlc3NlZCBieSBJbnN0cnVjdEJMSVApLCBhbmQgcmVkdWNlZCBwZXJmb3JtYW5jZSBvbiB0YXNrcyByZXF1aXJpbmcgc3BhdGlhbCByZWFzb25pbmcgb3IgY291bnRpbmcuIFN1YnNlcXVlbnQgd29yayBsaWtlIEluc3RydWN0QkxJUCBhZGRzIGluc3RydWN0aW9uIHR1bmluZyBvbiB0b3Agb2YgdGhlIFEtRm9ybWVyIGZyYW1ld29yay4ifV0="
---
# BLIP-2: Q-Former Bridging Vision and Language Models

## Overview

BLIP-2 (Bootstrapping Language-Image Pretraining) from Salesforce Research introduces the Q-Former, a lightweight transformer module that bridges a frozen image encoder and a frozen large language model. By keeping both pre-trained components frozen, BLIP-2 achieves state-of-the-art multimodal performance with minimal trainable parameters.

The central challenge BLIP-2 addresses is the modality gap: image encoder and LLM embedding spaces are learned independently and incompatible out of the box. The Q-Former solves this by learning to translate between them using only 188M trainable parameters, while the backbone encoders (billions of parameters) remain frozen.

> **info**: Q-Former is the core innovation: 32 learned queries distill the entire image into a compact visual representation that any frozen LLM can condition on. This decouples vision encoder upgrades from LLM upgrades — swap either independently.

BLIP-2 uses EVA-CLIP ViT-G/14 (1B params) as the visual encoder and either OPT or FlanT5 as the language model. Despite using frozen backbones, BLIP-2 FlanT5-XXL achieves 65.0% on VQAv2 and 45.9% on OK-VQA, outperforming Flamingo 80B with 54x fewer trainable parameters.

## Q-Former Architecture

The Q-Former is a BERT-based transformer with two attention pathways: self-attention between learned query tokens, and cross-attention from query tokens to frozen image patch features. The 32 query tokens (each 768-dimensional) are the only learned visual representations passed downstream to the LLM.

```python
import torch
import torch.nn as nn

class QFormerLayer(nn.Module):
    def __init__(self, d_model, n_heads, n_queries=32):
        super().__init__()
        self.query_tokens = nn.Parameter(torch.randn(1, n_queries, d_model))
        self.self_attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.cross_attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.ffn = nn.Sequential(nn.Linear(d_model, 4*d_model),
                                 nn.GELU(), nn.Linear(4*d_model, d_model))

    def forward(self, image_features):
        B = image_features.shape[0]
        q = self.query_tokens.expand(B, -1, -1)
        q, _ = self.self_attn(q, q, q)
        q, _ = self.cross_attn(q, image_features, image_features)
        return self.ffn(q) + q  # residual
```

The 32 query tokens compress the entire image — which may have 256 or more patch tokens from ViT-G/14 — into a fixed-size representation. This compression is learned rather than hand-designed: the Q-Former training objectives teach it what visual information is relevant for language understanding.

## Stage-1 Vision-Language Pretraining

Stage-1 trains the Q-Former with three objectives simultaneously, using 129M image-text pairs. The image encoder is frozen; only Q-Former weights are updated. The three losses together teach the Q-Former to extract image features useful for matching, discriminating, and generating text descriptions.

```python
def qformer_stage1_losses(query_output, text_output, image_embeds, text_ids, model):
    # 1. Image-Text Contrastive (ITC) — align [CLS] of query and text
    q_feat = F.normalize(model.itc_query_proj(query_output[:, 0]), dim=-1)
    t_feat = F.normalize(model.itc_text_proj(text_output[:, 0]), dim=-1)
    sim_matrix = q_feat @ t_feat.T / model.temp
    labels = torch.arange(sim_matrix.size(0), device=sim_matrix.device)
    itc_loss = (F.cross_entropy(sim_matrix, labels) +
                F.cross_entropy(sim_matrix.T, labels)) / 2
    # 2. Image-Text Matching (ITM) — binary classification on fused features
    itm_logits = model.itm_head(query_output)  # (B, 2)
    itm_loss = F.cross_entropy(itm_logits, model.itm_labels)
    # 3. Image-Grounded Text Generation (ITG) — causal LM on query+text
    itg_loss = model.lm_head_loss(query_output, text_ids)
    return itc_loss + itm_loss + itg_loss
```

ITC aligns global image and text representations. ITM is a binary cross-entropy loss that teaches the Q-Former to distinguish genuine from mismatched image-text pairs. ITG is autoregressive text generation conditioned on query token outputs — it forces the query tokens to capture text-relevant visual information.

## Stage-2 Language Model Connection

Stage-2 connects the Q-Former output to a frozen LLM via a linear projection. The 32 query token outputs (768-dim) are projected to the LLM input dimension (e.g., 2048 for OPT-2.7B) and prepended to the text embedding sequence. The LLM generates text conditioned on this visual prefix.

```python
def blip2_generate(image, prompt_ids, model, max_new_tokens=50):
    # Frozen CLIP encodes image
    with torch.no_grad():
        image_features = model.visual_encoder(image)  # (B, 257, 1408)
    # Q-Former extracts 32 query tokens
    query_output = model.qformer(image_features)    # (B, 32, 768)
    # Project to LLM embedding space
    visual_prefix = model.language_projection(query_output)  # (B, 32, D_llm)
    # Get text embeddings and concatenate
    text_embeds = model.language_model.get_input_embeddings()(prompt_ids)
    inputs_embeds = torch.cat([visual_prefix, text_embeds], dim=1)
    # Frozen LLM generates
    with torch.no_grad():
        outputs = model.language_model.generate(
            inputs_embeds=inputs_embeds, max_new_tokens=max_new_tokens)
    return outputs
```

For generative LLMs (OPT), the visual prefix acts as a soft visual prompt and the LLM generates the full response autoregressively. For encoder-decoder LLMs (FlanT5), query tokens are passed to the encoder, and the decoder generates the answer. FlanT5-based variants generally score higher on knowledge-intensive VQA tasks.

## Zero-Shot VQA

BLIP-2 supports zero-shot VQA out of the box through its generative interface. The question is formatted as a prompt and concatenated after the visual prefix tokens. The frozen LLM generates a free-form answer conditioned on both the visual representation and the question text — no fine-tuning required.

```python
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import requests
import torch

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16, device_map="auto")

image = Image.open(requests.get("https://example.com/img.jpg", stream=True).raw)
question = "Question: How many people are in the image? Answer:"
inputs = processor(image, question, return_tensors="pt").to(model.device, torch.float16)
generated = model.generate(**inputs, max_new_tokens=30)
print(processor.decode(generated[0], skip_special_tokens=True))
```

Zero-shot VQAv2 accuracy for BLIP-2 OPT-6.7B is 61.2%, compared to Flamingo-80B at 56.3% — achieved with a 54x smaller model. The gap comes from BLIP-2's staged pretraining: Q-Former stage-1 provides a strong visual representation before the LLM connection is even introduced.

| BLIP-2 Variant | LLM | Visual Encoder | VQAv2 % | OK-VQA % | Params Total |
| --- | --- | --- | --- | --- | --- |
| BLIP-2 OPT-2.7B | OPT-2.7B | EVA-CLIP ViT-G | 53.7 | 31.7 | ~3.4B |
| BLIP-2 OPT-6.7B | OPT-6.7B | EVA-CLIP ViT-G | 61.2 | 36.4 | ~8.2B |
| BLIP-2 FlanT5-XL | FlanT5-XL (3B) | EVA-CLIP ViT-G | 62.0 | 40.7 | ~4.1B |
| BLIP-2 FlanT5-XXL | FlanT5-XXL (11B) | EVA-CLIP ViT-G | 65.0 | 45.9 | ~12.1B |
| InstructBLIP FlanT5-XXL | FlanT5-XXL (11B) | EVA-CLIP ViT-G | — | 50.7 | ~12.1B |

## Key Takeaways

BLIP-2's Q-Former design solves a fundamental problem in multimodal learning: how to efficiently bridge pretrained unimodal models without catastrophic forgetting. By keeping both encoders frozen and training only the 188M-parameter bridge, BLIP-2 is compute-efficient and modular.

The two-stage pretraining curriculum is principled: stage-1 develops rich visual representations aligned to language, and stage-2 teaches the LLM to use them for generation. This separation prevents the LLM's strong language priors from overwhelming the visual signal during early training.

BLIP-2's limitations include fixed 32-query compression (may miss fine-grained details), no instruction-following capability in the base model (addressed by InstructBLIP), and reduced performance on tasks requiring spatial reasoning or counting. Subsequent work like InstructBLIP adds instruction tuning on top of the Q-Former framework.

