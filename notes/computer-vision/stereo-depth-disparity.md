---
title: "Stereo Depth Estimation: Disparity Maps and SGM"
slug: "stereo-depth-disparity"
description: ""
tags: [""]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGVyZW8gZGVwdGggZXN0aW1hdGlvbiByZWNvdmVycyBwZXItcGl4ZWwgZGVwdGggZnJvbSBhIHBhaXIgb2YgY2FsaWJyYXRlZCBjYW1lcmFzIHNlcGFyYXRlZCBieSBhIGtub3duIGJhc2VsaW5lLiBCeSBsb2NhdGluZyBjb3JyZXNwb25kaW5nIHBpeGVscyBiZXR3ZWVuIGxlZnQgYW5kIHJpZ2h0IGltYWdlcyBhbmQgbWVhc3VyaW5nIGhvcml6b250YWwgZGlzcGFyaXR5LCBkZXB0aCBpcyBjb21wdXRlZCB2aWEgdGhlIHN0ZXJlbyB0cmlhbmd1bGF0aW9uIGZvcm11bGEuIEl0IGlzIHdpZGVseSB1c2VkIGluIGF1dG9ub21vdXMgZHJpdmluZywgcm9ib3RpY3MsIGFuZCBBUi9WUiBhcHBsaWNhdGlvbnMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFzc2ljYWwgc3RlcmVvIG1ldGhvZHMgbGlrZSBTZW1pLUdsb2JhbCBNYXRjaGluZyAoU0dNKSBidWlsZCBleHBsaWNpdCBjb3N0IHZvbHVtZXMgYW5kIHJlZ3VsYXJpemUgdGhlbSB3aXRoIGR5bmFtaWMgcHJvZ3JhbW1pbmcuIERlZXAgbGVhcm5pbmcgYXBwcm9hY2hlcyDigJQgZnJvbSBQU01OZXQgdG8gUkFGVC1TdGVyZW8g4oCUIGxlYXJuIGNvc3Qgdm9sdW1lIGNvbnN0cnVjdGlvbiBhbmQgZGlzcGFyaXR5IHJlZ3Jlc3Npb24gZW5kLXRvLWVuZCwgYWNoaWV2aW5nIHN1Yi1waXhlbCBhY2N1cmFjeSBvbiBiZW5jaG1hcmtzIGxpa2UgS0lUVEkgMjAxNSBhbmQgU2NlbmVGbG93LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0ZXJlbyBDYW1lcmEgR2VvbWV0cnkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcmVjdGlmaWVkIHN0ZXJlbyBwYWlyIGhhcyBib3RoIGltYWdlIHBsYW5lcyBjb3BsYW5hciB3aXRoIHRoZSBiYXNlbGluZSB2ZWN0b3IuIEFmdGVyIHJlY3RpZmljYXRpb24sIGVwaXBvbGFyIGxpbmVzIGJlY29tZSBob3Jpem9udGFsIHNjYW5saW5lcywgcmVkdWNpbmcgdGhlIDJEIGNvcnJlc3BvbmRlbmNlIHNlYXJjaCB0byBhIDFEIHByb2JsZW0gYWxvbmcgZWFjaCByb3cuIFJlY3RpZmljYXRpb24gcmVxdWlyZXMgaW50cmluc2ljIG1hdHJpY2VzIGFuZCB0aGUgcmVsYXRpdmUgcm90YXRpb24gUiBhbmQgdHJhbnNsYXRpb24gVCBvYnRhaW5lZCBmcm9tIHN0ZXJlbyBjYWxpYnJhdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBmdW5kYW1lbnRhbCBtYXRyaXggRiBlbmNvZGVzIHRoZSBlcGlwb2xhciBjb25zdHJhaW50IHhcdTAwMjdGeCA9IDAgZm9yIGNvcnJlc3BvbmRpbmcgcGl4ZWxzIHggYW5kIHhcdTAwMjcuIEFmdGVyIHJlY3RpZmljYXRpb24gRiBzaW1wbGlmaWVzIHRvIGEgaG9yaXpvbnRhbCBzaGlmdCBvcGVyYXRvci4gVGhlIGVzc2VudGlhbCBtYXRyaXggRSA9IFt0XV94IFIgcmVsYXRlcyBjYWxpYnJhdGVkIG5vcm1hbGl6ZWQgY29vcmRpbmF0ZXMsIHdoaWxlIEYgYXBwbGllcyB0byBwaXhlbCBjb29yZGluYXRlcyB2aWEgRiA9IEsyXnstVH0gRSBLMV57LTF9LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpc3Bhcml0eSBhbmQgRGVwdGggUmVsYXRpb25zaGlwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaXNwYXJpdHkgZCBpcyB0aGUgaG9yaXpvbnRhbCBwaXhlbCBzaGlmdCBiZXR3ZWVuIGEgbWF0Y2hlZCBwb2ludCBpbiB0aGUgbGVmdCBpbWFnZSBhbmQgaXRzIGNvdW50ZXJwYXJ0IGluIHRoZSByaWdodCBpbWFnZS4gRm9yIGEgcmVjdGlmaWVkIHBhaXIsIGQgPSB4X2xlZnQgLSB4X3JpZ2h0IFx1MDAzZT0gMCBmb3IgcG9pbnRzIGluIGZyb250IG9mIHRoZSBjYW1lcmFzLiBEZXB0aCBaIGlzIGludmVyc2VseSBwcm9wb3J0aW9uYWwgdG8gZGlzcGFyaXR5OiBaID0gZipiL2QsIHdoZXJlIGYgaXMgZm9jYWwgbGVuZ3RoIGluIHBpeGVscyBhbmQgYiBpcyB0aGUgYmFzZWxpbmUgaW4gbWV0ZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImYgPSBmb2NhbF9sZW5ndGggICAgIyBlLmcuLCA3MjEgcHggKEtJVFRJKVxuYiA9IGJhc2VsaW5lICAgICAgICAjIGUuZy4sIDAuNTQgbSAgKEtJVFRJKVxuIyBDb21wdXRlIGRlcHRoOyBndWFyZCBhZ2FpbnN0IGRpdmlzaW9uIGJ5IHplcm9cbmRlcHRoID0gbnAud2hlcmUoZGlzcGFyaXR5IFx1MDAzZSAwLCBmICogYiAvIGRpc3Bhcml0eSwgMC4wKVxuIyBFeGFtcGxlOiBmPTcyMSwgYj0wLjU0LCBkPTUwIHB4XG4jIGRlcHRoID0gNzIxICogMC41NCAvIDUwID0gNy43OSBtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZXB0aCB1bmNlcnRhaW50eSBncm93cyBxdWFkcmF0aWNhbGx5IHdpdGggZGlzdGFuY2U6IHNpZ21hX1ogPSAoWl4yIC8gKGYqYikpICogc2lnbWFfZC4gRm9yIEtJVFRJIChmPTcyMSwgYj0wLjU0IG0pIGEgaGFsZi1waXhlbCBkaXNwYXJpdHkgZXJyb3IgYXQgMTAgbSBnaXZlcyB+MTMgY20gZGVwdGggdW5jZXJ0YWludHksIHdoaWxlIGF0IDUwIG0gdGhlIHNhbWUgZXJyb3IgeWllbGRzIH4zLjIgbSB1bmNlcnRhaW50eS4gVGhpcyBpcyB3aHkgc3RlcmVvIGlzIHR5cGljYWxseSByZWxpYWJsZSBvbmx5IHVwIHRvIHJvdWdobHkgNTAtMTAwIG0gcmFuZ2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VtaS1HbG9iYWwgTWF0Y2hpbmcgKFNHTSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNHTSBidWlsZHMgYSAzRCBjb3N0IHZvbHVtZSBDKHAsIGQpIG1lYXN1cmluZyB0aGUgbWF0Y2hpbmcgY29zdCBhdCBwaXhlbCBwIGZvciBkaXNwYXJpdHkgZCwgdXNpbmcgQ2Vuc3VzIHRyYW5zZm9ybSBvciBtdXR1YWwgaW5mb3JtYXRpb24uIEl0IHRoZW4gcnVucyBkeW5hbWljIHByb2dyYW1taW5nIGFsb25nIDQgb3IgOCBkaXJlY3Rpb25hbCBwYXRocyBhbmQgYWdncmVnYXRlcyBwYXRoIGNvc3RzIHRvIHJlZ3VsYXJpemUgdGhlIGRpc3Bhcml0eSBtYXAsIHBlbmFsaXppbmcgbGFyZ2UgZGlzcGFyaXR5IGNoYW5nZXMgYXQgbm9uLWVkZ2UgcGl4ZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImNvc3QgPSB0b3JjaC56ZXJvcyhCLCBtYXhfZGlzcCwgSCwgVylcbmZvciBkIGluIHJhbmdlKG1heF9kaXNwKTpcbiAgICBzaGlmdGVkX3JpZ2h0ID0gdG9yY2gucm9sbChyaWdodF9mZWF0LCBkLCBkaW1zPS0xKVxuICAgIGNvc3RbOiwgZCwgOiwgOl0gPSAobGVmdF9mZWF0IC0gc2hpZnRlZF9yaWdodCkuYWJzKCkubWVhbigxKVxuIyBjb3N0IHNoYXBlOiAoQiwgRCwgSCwgVylcbiMgV2lubmVyLVRha2UtQWxsOiBkaXNwYXJpdHkgPSBhcmdtaW4gb3ZlciBEIGRpbWVuc2lvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoidGV4dCIsImNvbnRlbnQiOiIjIFNHTSBwYXRoIGNvc3QgYWdncmVnYXRpb24gKG9uZSBkaXJlY3Rpb24gcik6XG4jIExfcihwLGQpID0gQyhwLGQpICsgbWluKFxuIyAgICAgTF9yKHAtciwgZCksXG4jICAgICBMX3IocC1yLCBkLTEpICsgUDEsXG4jICAgICBMX3IocC1yLCBkKzEpICsgUDEsXG4jICAgICBtaW5fayhMX3IocC1yLCBrKSkgKyBQMlxuIyApIC0gbWluX2soTF9yKHAtciwgaykpXG4jIFAxIHBlbmFsaXplcyArLTEgZGlzcGFyaXR5IGNoYW5nZTsgUDIgcGVuYWxpemVzIGxhcmdlciBqdW1wcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUDEgYW5kIFAyIGFyZSB0aGUgY3JpdGljYWwgU0dNIGh5cGVycGFyYW1ldGVycy4gUDEgcGVuYWxpemVzIHNtYWxsIGRpc3Bhcml0eSBjaGFuZ2VzICgrLTEpIHRvIGVuY291cmFnZSBzbW9vdGggc3VyZmFjZXMuIFAyIHBlbmFsaXplcyBsYXJnZXIganVtcHMgd2l0aCBhbiBpbWFnZS1hZGFwdGl2ZSB2YWx1ZSBQMiA9IFAyX2luaXQgLyB8ZGVsdGFfSShwKXwsIHdoZXJlIGRlbHRhX0kgaXMgdGhlIGxvY2FsIGludGVuc2l0eSBncmFkaWVudC4gVGhpcyBhZGFwdGl2ZSBwZW5hbHR5IHByZXNlcnZlcyBzaGFycCBkZXB0aCBkaXNjb250aW51aXRpZXMgYXQgb2JqZWN0IGJvdW5kYXJpZXMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwiY29udGVudCI6IlN0ZXJlbyBkZXB0aCBmYWlscyBhdCB0ZXh0dXJlbGVzcyByZWdpb25zIChza3ksIHdoaXRlIHdhbGxzKSBiZWNhdXNlIHRoZSBjb3N0IHZvbHVtZSBoYXMgbm8gZGlzY3JpbWluYXRpdmUgc2lnbmFsIHRvIG1hdGNoLiBBZGQgcmVndWxhcml6YXRpb24gKFNHTVx1MDAyN3MgUDIgcGVuYWx0eSkgb3IgdXNlIGRlcHRoIGNvbXBsZXRpb24gd2l0aCBzcGFyc2UgTGlEQVIgdG8gZmlsbCB0aGVzZSByZWdpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlZXAgU3RlcmVvIE5ldHdvcmtzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQU01OZXQgaW50cm9kdWNlZCBTcGF0aWFsIFB5cmFtaWQgUG9vbGluZyBhbmQgM0QgY29udm9sdXRpb25zIG92ZXIgdGhlIGNvc3Qgdm9sdW1lLCBjYXB0dXJpbmcgZ2xvYmFsIGNvbnRleHQgZm9yIGltcHJvdmVkIGFjY3VyYWN5LiBHQU5ldCByZXBsYWNlZCAzRCBjb252b2x1dGlvbnMgd2l0aCBndWlkZWQgYWdncmVnYXRpb24gbGF5ZXJzIHRoYXQgbWltaWMgU0dNIGRpcmVjdGlvbmFsIHBhdGhzIGJ1dCBhcmUgbGVhcm5lZCBlbmQtdG8tZW5kLCByZWR1Y2luZyBpbmZlcmVuY2UgdGltZSB3aGlsZSBhY2hpZXZpbmcgYmV0dGVyIHJlc3VsdHMgb24gS0lUVEkgYW5kIFNjZW5lRmxvdyBiZW5jaG1hcmtzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImZlYXRfbGVmdCwgZmVhdF9yaWdodCA9IGZlYXR1cmVfZW5jb2RlcihsZWZ0LCByaWdodClcbmNvcnJfZm4gPSBDb3JyQmxvY2soZmVhdF9sZWZ0LCBmZWF0X3JpZ2h0LCBudW1fbGV2ZWxzPTQpXG5kaXNwYXJpdHkgPSB0b3JjaC56ZXJvcyhCLCAxLCBILCBXKVxuZm9yIF8gaW4gcmFuZ2Uobl9pdGVycyk6XG4gICAgY29yciA9IGNvcnJfZm4oZGlzcGFyaXR5KSAgICAgICAgICAgIyAoQiwgbGV2ZWxzKnJhZGl1cywgSCwgVylcbiAgICBkZWx0YV9kID0gdXBkYXRlX2Jsb2NrKGNvcnIsIGNvbnRleHQsIGRpc3Bhcml0eSlcbiAgICBkaXNwYXJpdHkgPSBkaXNwYXJpdHkgKyBkZWx0YV9kICAgICAjIGl0ZXJhdGl2ZSBHUlUgcmVmaW5lbWVudCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUkFGVC1TdGVyZW8gYWNoaWV2ZXMgY29tcGV0aXRpdmUgYWNjdXJhY3kgdGhyb3VnaCBpdGVyYXRpdmUgR1JVLWJhc2VkIHVwZGF0ZXMgdGhhdCBwcm9ncmVzc2l2ZWx5IHJlZmluZSBjb2Fyc2UgZGlzcGFyaXR5IGVzdGltYXRlcywgYW5hbG9nb3VzIHRvIG9wdGljYWwgZmxvdy4gSG93ZXZlciwgaXQgaXMgbGVzcyByb2J1c3Qgd2hlbiB0aGUgc3RlcmVvIHBhaXIgdmlvbGF0ZXMgdGhlIHJlY3RpZmljYXRpb24gYXNzdW1wdGlvbiBvciB3aGVuIGxhcmdlIHRleHR1cmVsZXNzIHJlZ2lvbnMgYW5kIHNpZ25pZmljYW50IG9jY2x1c2lvbnMgYXJlIHByZXNlbnQgaW4gdGhlIHNjZW5lLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJUeXBlIiwiS0lUVEkgRDEgJSIsIlNjZW5lRmxvdyBFUEUiLCJTcGVlZCAobXMpIiwiTWF4IERpc3AiXSwicm93cyI6W1siU0dNIiwiQ2xhc3NpY2FsIiwiNC41JSIsIk4vQSIsIn4xNTAiLCIyNTYiXSxbIlBTTU5ldCIsIkNOTiAzRCIsIjIuMzIlIiwiMS4wOSBweCIsIn40MTAiLCIxOTIiXSxbIkdBTmV0IiwiQ05OIGd1aWRlZCIsIjEuNjMlIiwiMC44NCBweCIsIn4zNjAiLCIxOTIiXSxbIlJBRlQtU3RlcmVvIiwiSXRlcmF0aXZlIiwiMS41OCUiLCIwLjczIHB4IiwifjM4MCIsIjI1NiJdLFsiQ1JFU3RlcmVvIiwiSXRlcmF0aXZlIiwiMS40NSUiLCIwLjY5IHB4IiwifjQxMCIsIjI1NiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RlcmVvIGRlcHRoIHByb3ZpZGVzIGRlbnNlLCBhYnNvbHV0ZSBkZXB0aCBmcm9tIHBhc3NpdmUgY2FtZXJhcyB3aXRob3V0IGEgZGVkaWNhdGVkIGRlcHRoIHNlbnNvci4gVGhlIGZvcm11bGEgWiA9IGYqYi9kIG1lYW5zIGRlcHRoIHJlc29sdXRpb24gaXMgZ292ZXJuZWQgYnkgYmFzZWxpbmUgbGVuZ3RoLCBmb2NhbCBsZW5ndGgsIGFuZCBtaW5pbXVtIG1lYXN1cmFibGUgZGlzcGFyaXR5LiBMb25nZXIgYmFzZWxpbmVzIGltcHJvdmUgZmFyLXJhbmdlIGFjY3VyYWN5IGJ1dCBpbmNyZWFzZSB0aGUgbmVhci1jYW1lcmEgb2NjbHVzaW9uIHpvbmUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTR00gcmVtYWlucyBhIHN0cm9uZyBjbGFzc2ljYWwgYmFzZWxpbmUgYmVjYXVzZSBpdCBpcyBkZXRlcm1pbmlzdGljLCBpbnRlcnByZXRhYmxlLCBhbmQgZWZmaWNpZW50IG9uIHNwZWNpYWxpemVkIGhhcmR3YXJlIHN1Y2ggYXMgRlBHQXMgYW5kIEFTSUNzLiBEZWVwIGxlYXJuaW5nIHN0ZXJlbyBtZXRob2RzIGdlbmVyYWxpemUgYmV0dGVyIGFjcm9zcyBzY2VuZXMgYW5kIGxpZ2h0aW5nIGJ1dCByZXF1aXJlIEdQVSBpbmZlcmVuY2UgYW5kIHJlcHJlc2VudGF0aXZlIHRyYWluaW5nIGRhdGEgdG8gYXZvaWQgbGFyZ2UgYWNjdXJhY3kgZHJvcHMgaW4gbmV3IGRvbWFpbnMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZXB0aCBjb21wbGV0aW9uIGNvbWJpbmVzIHNwYXJzZS1idXQtYWNjdXJhdGUgTGlEQVIgZGVwdGggd2l0aCBkZW5zZS1idXQtbm9pc3kgc3RlcmVvIG9yIG1vbm9jdWxhciBlc3RpbWF0ZXMgdG8gcHJvZHVjZSBkZW5zZSwgYWNjdXJhdGUgZGVwdGggbWFwcy4gVGhpcyBoeWJyaWQgc3RyYXRlZ3kgaXMgY29tbW9uIGluIHByb2R1Y3Rpb24gYXV0b25vbW91cyBkcml2aW5nIHN0YWNrcyB3aGVyZSBib3RoIHNlbnNvciB0eXBlcyBhcmUgYXZhaWxhYmxlIGFuZCB0aGVpciBjb21wbGVtZW50YXJ5IHN0cmVuZ3RocyBjYW4gYmUgZXhwbG9pdGVkIGpvaW50bHkuIn1d"
---
# Stereo Depth Estimation: Disparity Maps and SGM

## Overview

Stereo depth estimation recovers per-pixel depth from a pair of calibrated cameras separated by a known baseline. By locating corresponding pixels between left and right images and measuring horizontal disparity, depth is computed via the stereo triangulation formula. It is widely used in autonomous driving, robotics, and AR/VR applications.

Classical stereo methods like Semi-Global Matching (SGM) build explicit cost volumes and regularize them with dynamic programming. Deep learning approaches — from PSMNet to RAFT-Stereo — learn cost volume construction and disparity regression end-to-end, achieving sub-pixel accuracy on benchmarks like KITTI 2015 and SceneFlow.

## Stereo Camera Geometry

A rectified stereo pair has both image planes coplanar with the baseline vector. After rectification, epipolar lines become horizontal scanlines, reducing the 2D correspondence search to a 1D problem along each row. Rectification requires intrinsic matrices and the relative rotation R and translation T obtained from stereo calibration.

The fundamental matrix F encodes the epipolar constraint x'Fx = 0 for corresponding pixels x and x'. After rectification F simplifies to a horizontal shift operator. The essential matrix E = [t]_x R relates calibrated normalized coordinates, while F applies to pixel coordinates via F = K2^{-T} E K1^{-1}.

## Disparity and Depth Relationship

Disparity d is the horizontal pixel shift between a matched point in the left image and its counterpart in the right image. For a rectified pair, d = x_left - x_right >= 0 for points in front of the cameras. Depth Z is inversely proportional to disparity: Z = f*b/d, where f is focal length in pixels and b is the baseline in meters.

```
f = focal_length    # e.g., 721 px (KITTI)
b = baseline        # e.g., 0.54 m  (KITTI)
# Compute depth; guard against division by zero
depth = np.where(disparity > 0, f * b / disparity, 0.0)
# Example: f=721, b=0.54, d=50 px
# depth = 721 * 0.54 / 50 = 7.79 m
```

Depth uncertainty grows quadratically with distance: sigma_Z = (Z^2 / (f*b)) * sigma_d. For KITTI (f=721, b=0.54 m) a half-pixel disparity error at 10 m gives ~13 cm depth uncertainty, while at 50 m the same error yields ~3.2 m uncertainty. This is why stereo is typically reliable only up to roughly 50-100 m range.

## Semi-Global Matching (SGM)

SGM builds a 3D cost volume C(p, d) measuring the matching cost at pixel p for disparity d, using Census transform or mutual information. It then runs dynamic programming along 4 or 8 directional paths and aggregates path costs to regularize the disparity map, penalizing large disparity changes at non-edge pixels.

```
cost = torch.zeros(B, max_disp, H, W)
for d in range(max_disp):
    shifted_right = torch.roll(right_feat, d, dims=-1)
    cost[:, d, :, :] = (left_feat - shifted_right).abs().mean(1)
# cost shape: (B, D, H, W)
# Winner-Take-All: disparity = argmin over D dimension
```

```
# SGM path cost aggregation (one direction r):
# L_r(p,d) = C(p,d) + min(
#     L_r(p-r, d),
#     L_r(p-r, d-1) + P1,
#     L_r(p-r, d+1) + P1,
#     min_k(L_r(p-r, k)) + P2
# ) - min_k(L_r(p-r, k))
# P1 penalizes +-1 disparity change; P2 penalizes larger jumps
```

P1 and P2 are the critical SGM hyperparameters. P1 penalizes small disparity changes (+-1) to encourage smooth surfaces. P2 penalizes larger jumps with an image-adaptive value P2 = P2_init / |delta_I(p)|, where delta_I is the local intensity gradient. This adaptive penalty preserves sharp depth discontinuities at object boundaries.

> **warning**: Stereo depth fails at textureless regions (sky, white walls) because the cost volume has no discriminative signal to match. Add regularization (SGM's P2 penalty) or use depth completion with sparse LiDAR to fill these regions.

## Deep Stereo Networks

PSMNet introduced Spatial Pyramid Pooling and 3D convolutions over the cost volume, capturing global context for improved accuracy. GANet replaced 3D convolutions with guided aggregation layers that mimic SGM directional paths but are learned end-to-end, reducing inference time while achieving better results on KITTI and SceneFlow benchmarks.

```
feat_left, feat_right = feature_encoder(left, right)
corr_fn = CorrBlock(feat_left, feat_right, num_levels=4)
disparity = torch.zeros(B, 1, H, W)
for _ in range(n_iters):
    corr = corr_fn(disparity)           # (B, levels*radius, H, W)
    delta_d = update_block(corr, context, disparity)
    disparity = disparity + delta_d     # iterative GRU refinement
```

RAFT-Stereo achieves competitive accuracy through iterative GRU-based updates that progressively refine coarse disparity estimates, analogous to optical flow. However, it is less robust when the stereo pair violates the rectification assumption or when large textureless regions and significant occlusions are present in the scene.

| Method | Type | KITTI D1 % | SceneFlow EPE | Speed (ms) | Max Disp |
| --- | --- | --- | --- | --- | --- |
| SGM | Classical | 4.5% | N/A | ~150 | 256 |
| PSMNet | CNN 3D | 2.32% | 1.09 px | ~410 | 192 |
| GANet | CNN guided | 1.63% | 0.84 px | ~360 | 192 |
| RAFT-Stereo | Iterative | 1.58% | 0.73 px | ~380 | 256 |
| CREStereo | Iterative | 1.45% | 0.69 px | ~410 | 256 |

## Key Takeaways

Stereo depth provides dense, absolute depth from passive cameras without a dedicated depth sensor. The formula Z = f*b/d means depth resolution is governed by baseline length, focal length, and minimum measurable disparity. Longer baselines improve far-range accuracy but increase the near-camera occlusion zone.

SGM remains a strong classical baseline because it is deterministic, interpretable, and efficient on specialized hardware such as FPGAs and ASICs. Deep learning stereo methods generalize better across scenes and lighting but require GPU inference and representative training data to avoid large accuracy drops in new domains.

Depth completion combines sparse-but-accurate LiDAR depth with dense-but-noisy stereo or monocular estimates to produce dense, accurate depth maps. This hybrid strategy is common in production autonomous driving stacks where both sensor types are available and their complementary strengths can be exploited jointly.

