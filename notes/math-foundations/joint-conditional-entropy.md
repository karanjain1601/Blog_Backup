---
title: "Joint Entropy and Conditional Entropy"
slug: "joint-conditional-entropy"
description: "Joint entropy H(X,Y), conditional entropy H(Y|X), the chain rule, subadditivity, and information-theoretic implications for deep learning pipelines."
tags: ["information-theory","math","foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSm9pbnQgYW5kIGNvbmRpdGlvbmFsIGVudHJvcHkgZXh0ZW5kIFNoYW5ub24gZW50cm9weSB0byBtdWx0aXBsZSByYW5kb20gdmFyaWFibGVzLiBUaGV5IGZvcm1hbGl6ZSBob3cgaW5mb3JtYXRpb24gaXMgc2hhcmVkIG9yIHJlbWFpbnMgcHJpdmF0ZSBiZXR3ZWVuIHZhcmlhYmxlcywgYW5kIGdpdmUgcmlzZSB0byB0aGUgY2hhaW4gcnVsZSBvZiBlbnRyb3B5IOKAlCBvbmUgb2YgdGhlIG1vc3QgdXNlZnVsIGlkZW50aXRpZXMgaW4gaW5mb3JtYXRpb24gdGhlb3J5LiBVbmRlcnN0YW5kaW5nIHRoZXNlIHF1YW50aXRpZXMgaXMgcHJlcmVxdWlzaXRlIHRvIG11dHVhbCBpbmZvcm1hdGlvbiwgdGhlIGRhdGEgcHJvY2Vzc2luZyBpbmVxdWFsaXR5LCBhbmQgdGhlIGluZm9ybWF0aW9uIGJvdHRsZW5lY2suIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSm9pbnQgRW50cm9weSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIHR3byBkaXNjcmV0ZSByYW5kb20gdmFyaWFibGVzIFggYW5kIFkgd2l0aCBqb2ludCBQTUYgcCh4LHkpLCBqb2ludCBlbnRyb3B5IGlzOlxuXG5IKFgsWSkgPSAtc3VtX3t4LHl9IHAoeCx5KSBsb2cgcCh4LHkpID0gRVstbG9nIHAoWCxZKV1cblxuSm9pbnQgZW50cm9weSBtZWFzdXJlcyB0aGUgdG90YWwgdW5jZXJ0YWludHkgb2YgdGhlIHBhaXIgKFgsWSkuIEl0IGdlbmVyYWxpc2VzIG5hdHVyYWxseSB0byBuIHZhcmlhYmxlczogSChYMSwuLi4sWG4pID0gLUVbbG9nIHAoWDEsLi4uLFhuKV0uIEpvaW50IGVudHJvcHkgaXMgYWx3YXlzIGF0IGxlYXN0IGFzIGxhcmdlIGFzIGVhY2ggbWFyZ2luYWw6IEgoWCxZKSA+PSBtYXgoSChYKSwgSChZKSkuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uZGl0aW9uYWwgRW50cm9weSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uZGl0aW9uYWwgZW50cm9weSBIKFl8WCkgaXMgdGhlIGV4cGVjdGVkIHJlbWFpbmluZyB1bmNlcnRhaW50eSBhYm91dCBZIGFmdGVyIG9ic2VydmluZyBYOlxuXG5IKFl8WCkgPSBzdW1feCBwKHgpIEgoWXxYPXgpID0gLXN1bV97eCx5fSBwKHgseSkgbG9nIHAoeXx4KVxuXG5FcXVpdmFsZW50bHkgSChZfFgpID0gRV97WH1bSChZfFg9eCldID0gRVstbG9nIHAoWXxYKV0uIENvbmRpdGlvbmFsIGVudHJvcHkgaXMgYWx3YXlzIG5vbi1uZWdhdGl2ZTogSChZfFgpID49IDAsIHdpdGggZXF1YWxpdHkgaWZmIFkgaXMgYSBkZXRlcm1pbmlzdGljIGZ1bmN0aW9uIG9mIFguXG5cbkNvbmRpdGlvbmluZyByZWR1Y2VzIGVudHJvcHk6IEgoWXxYKSA8PSBIKFkpLCB3aXRoIGVxdWFsaXR5IGlmZiBYIGFuZCBZIGFyZSBpbmRlcGVuZGVudC4gT2JzZXJ2aW5nIGEgY29ycmVsYXRlZCB2YXJpYWJsZSBjYW4gb25seSByZWR1Y2UgKG9yIG1haW50YWluKSB1bmNlcnRhaW50eSDigJQgaXQgY2FuIG5ldmVyIGluY3JlYXNlIGl0LiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNoYWluIFJ1bGUgb2YgRW50cm9weSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNoYWluIHJ1bGUgaXMgdGhlIGNlbnRyYWwgaWRlbnRpdHkgY29ubmVjdGluZyBqb2ludCBhbmQgY29uZGl0aW9uYWwgZW50cm9weTpcblxuSChYLFkpID0gSChYKSArIEgoWXxYKSA9IEgoWSkgKyBIKFh8WSlcblxuTXVsdGl2YXJpYXRlIGdlbmVyYWxpc2F0aW9uOlxuSChYMSwuLi4sWG4pID0gSChYMSkgKyBIKFgyfFgxKSArIEgoWDN8WDEsWDIpICsgLi4uICsgSChYbnxYMSwuLi4sWF97bi0xfSlcblxuVGhpcyBpcyBleGFjdGx5IHRoZSBjaGFpbiBydWxlIG9mIHByb2JhYmlsaXR5IGluIGxvZyBmb3JtOiBsb2cgcCh4MSwuLi4seG4pID0gbG9nIHAoeDEpICsgbG9nIHAoeDJ8eDEpICsgLi4uICsgbG9nIHAoeG58eDEsLi4uLHhfe24tMX0pLiBBdXRvcmVncmVzc2l2ZSBsYW5ndWFnZSBtb2RlbHMgYXJlIHRyYWluZWQgdG8gZXN0aW1hdGUgZWFjaCBjb25kaXRpb25hbCBIKFh0fFgxLC4uLixYX3t0LTF9KSDigJQgdGhlIGNoYWluIHJ1bGUgZ3VhcmFudGVlcyB0aGF0IHRoZSBzdW0gb2YgdGhlc2UgY29uZGl0aW9uYWxzIGVxdWFscyB0aGUgdG90YWwgc2VxdWVuY2UgZW50cm9weS4ifSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkF1dG9yZWdyZXNzaXZlIE1vZGVscyBhbmQgdGhlIENoYWluIFJ1bGUiLCJjb250ZW50IjoiR1BULXN0eWxlIGxhbmd1YWdlIG1vZGVscyBtYXhpbWlzZSB0aGUgbG9nLWxpa2VsaWhvb2Q6IHN1bV90IGxvZyBwKHh0IHwgeDEsLi4uLHhfe3QtMX0pLiBUaGlzIGlzIGV4YWN0bHkgdGhlIGNoYWluLXJ1bGUgZGVjb21wb3NpdGlvbiBvZiBIKFgxLC4uLixYVCkuIFRyYWluaW5nIGNyb3NzLWVudHJvcHkgPSBIKHBfdHJ1ZSwgcV9tb2RlbCkgd2hlcmUgdGhlIGNoYWluIHJ1bGUgZmFjdG9ycyBib3RoIHBfdHJ1ZSBhbmQgcV9tb2RlbC4gUGVycGxleGl0eSA9IGV4cChhdmVyYWdlIHRva2VuIGNyb3NzLWVudHJvcHkpIGRpcmVjdGx5IGVzdGltYXRlcyBleHAoSF9yYXRlKSwgdGhlIGJyYW5jaGluZyBmYWN0b3Igb2YgdGhlIHByb2Nlc3MuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3ViYWRkaXRpdml0eSBvZiBFbnRyb3B5In0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIKFgsWSkgPD0gSChYKSArIEgoWSksIHdpdGggZXF1YWxpdHkgaWZmIFggYW5kIFkgYXJlIGluZGVwZW5kZW50LlxuXG5UaGlzIGlzIHRoZSBzdWJhZGRpdGl2aXR5IHByb3BlcnR5LiBJdCBzYXlzIHRoYXQga25vd2luZyB0aGUgam9pbnQgZGlzdHJpYnV0aW9uIHRvZ2V0aGVyIGNhbiBvbmx5IHJlcHJlc2VudCBsZXNzIHVuY2VydGFpbnR5IHRoYW4gdHJlYXRpbmcgdGhlIHZhcmlhYmxlcyBhcyBjb21wbGV0ZWx5IGluZGVwZW5kZW50LiBTdWJhZGRpdGl2aXR5IGlzIHRpZ2h0IHdoZW4gdGhlcmUgaXMgemVybyBzaGFyZWQgaW5mb3JtYXRpb24uIFRoZSBnYXAgSChYKStIKFkpLUgoWCxZKSA9IEkoWDtZKSBpcyB0aGUgbXV0dWFsIGluZm9ybWF0aW9uIOKAlCBleGFjdGx5IHdoYXQgaXMgc2hhcmVkIGJldHdlZW4gWCBhbmQgWS4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBqb2ludF9lbnRyb3B5KHBfeHkpOlxuICAgIFwiXCJcIkpvaW50IGVudHJvcHkgSChYLFkpIGZyb20gMi1EIGpvaW50IGRpc3RyaWJ1dGlvbiBhcnJheS5cIlwiXCJcbiAgICBwID0gcF94eS5mbGF0dGVuKClcbiAgICBtYXNrID0gcCA+IDBcbiAgICByZXR1cm4gZmxvYXQoLW5wLnN1bShwW21hc2tdICogbnAubG9nMihwW21hc2tdKSkpXG5cbmRlZiBjb25kaXRpb25hbF9lbnRyb3B5KHBfeHkpOlxuICAgIFwiXCJcIkgoWXxYKSA9IEgoWCxZKSAtIEgoWCkuXCJcIlwiXG4gICAgcF94ID0gcF94eS5zdW0oYXhpcz0xKVxuICAgIGhfeHkgPSBqb2ludF9lbnRyb3B5KHBfeHkpXG4gICAgaF94ICA9IGVudHJvcHlfYml0cyhwX3gpXG4gICAgcmV0dXJuIGhfeHkgLSBoX3hcblxuZGVmIGVudHJvcHlfYml0cyhwKTpcbiAgICBwID0gbnAuYXNhcnJheShwLCBkdHlwZT1mbG9hdClcbiAgICBtYXNrID0gcCA+IDBcbiAgICByZXR1cm4gZmxvYXQoLW5wLnN1bShwW21hc2tdICogbnAubG9nMihwW21hc2tdKSkpXG5cbiMgRXhhbXBsZTogdHdvIGNvcnJlbGF0ZWQgYmluYXJ5IHZhcmlhYmxlc1xuIyBwKFg9MCxZPTApPTAuNCwgcChYPTAsWT0xKT0wLjEsIHAoWD0xLFk9MCk9MC4xLCBwKFg9MSxZPTEpPTAuNFxucF94eSA9IG5wLmFycmF5KFtbMC40LCAwLjFdLFswLjEsIDAuNF1dKVxucF94ICA9IHBfeHkuc3VtKGF4aXM9MSkgICAjIFswLjUsIDAuNV1cbnBfeSAgPSBwX3h5LnN1bShheGlzPTApICAgIyBbMC41LCAwLjVdXG5cbmhfeHkgPSBqb2ludF9lbnRyb3B5KHBfeHkpICAgICAgICAgICAgIyAxLjcyMiBiaXRzXG5oX3ggID0gZW50cm9weV9iaXRzKHBfeCkgICAgICAgICAgICAgICMgMS4wMDAgYml0XG5oX3kgID0gZW50cm9weV9iaXRzKHBfeSkgICAgICAgICAgICAgICMgMS4wMDAgYml0XG5oX3lfZ2l2ZW5feCA9IGhfeHkgLSBoX3ggICAgICAgICAgICAgICMgMC43MjIgYml0ICA8IGhfeSAoY29uZGl0aW9uaW5nIGhlbHBzKVxubWkgICA9IGhfeCArIGhfeSAtIGhfeHkgICAgICAgICAgICAgICMgMC4yNzggYml0IChzaGFyZWQgaW5mb3JtYXRpb24pXG5cbnByaW50KGYnSChYLFkpICA9IHtoX3h5Oi4zZn0nKSAgICAgICAgIyAxLjcyMlxucHJpbnQoZidIKFl8WCkgID0ge2hfeV9naXZlbl94Oi4zZn0nKSAjIDAuNzIyICA8IEgoWSk9MS4wXG5wcmludChmJ0koWDtZKSAgPSB7bWk6LjNmfScpICAgICAgICAgICMgMC4yNzgifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25kaXRpb25pbmcgUmVkdWNlcyBFbnRyb3B5IOKAlCBQcm9vZiBTa2V0Y2gifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkgoWXxYKSA8PSBIKFkpIGZvbGxvd3MgZnJvbSBKZW5zZW4ncyBpbmVxdWFsaXR5IGFwcGxpZWQgdG8gdGhlIGNvbmNhdml0eSBvZiBlbnRyb3B5LCBvciBkaXJlY3RseSBmcm9tIEkoWDtZKSA+PSAwOlxuXG5JKFg7WSkgPSBIKFkpIC0gSChZfFgpID49IDAgID0+ICBIKFl8WCkgPD0gSChZKVxuXG5JbnR1aXRpdmVseToga25vd2luZyBYIGNhbm5vdCBpbmNyZWFzZSB1bmNlcnRhaW50eSBhYm91dCBZIG9uIGF2ZXJhZ2UuIE5vdGUgdGhhdCBmb3IgYSBzcGVjaWZpYyByZWFsaXNhdGlvbiB4MCBpdCBpcyBwb3NzaWJsZSB0aGF0IEgoWXxYPXgwKSA+IEgoWSkg4oCUIHRoZSBpbmVxdWFsaXR5IGhvbGRzIG9ubHkgaW4gZXhwZWN0YXRpb24gb3ZlciBYLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVudHJvcHkgb2YgRnVuY3Rpb25zIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJZiBaID0gZihYKSBmb3IgYW55IGRldGVybWluaXN0aWMgZnVuY3Rpb24gZiwgdGhlbiBIKFopIDw9IEgoWCkuIEluZm9ybWF0aW9uIGNhbiBvbmx5IGJlIGxvc3Qgb3IgcHJlc2VydmVkLCBuZXZlciBjcmVhdGVkLCBieSBkZXRlcm1pbmlzdGljIHByb2Nlc3NpbmcuIEVxdWFsaXR5IGhvbGRzIGlmZiBmIGlzIGludmVydGlibGUgb24gdGhlIHN1cHBvcnQgb2YgWC5cblxuQ29yb2xsYXJ5OiBhbnkgZmVhdHVyZSBleHRyYWN0aW9uIHN0ZXAgWiA9IHBoaShYKSBzYXRpc2ZpZXMgSChaKSA8PSBIKFgpLiBEZWVwIG5ldHdvcmtzIGFyZSBpbmZvcm1hdGlvbiBjb21wcmVzc29ycyDigJQgZWFjaCBsYXllciBjYW4gb25seSBkZXN0cm95IG9yIHByZXNlcnZlIHRoZSBpbmZvcm1hdGlvbiBwcmVzZW50IGluIGl0cyBpbnB1dC4gVGhpcyBpcyB0aGUgZm91bmRhdGlvbiBvZiB0aGUgaW5mb3JtYXRpb24gYm90dGxlbmVjayB2aWV3IG9mIGRlZXAgbGVhcm5pbmcuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGF0YSBQcm9jZXNzaW5nIEluZXF1YWxpdHkgZm9yIEVudHJvcHkifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IklmIFggLT4gWSAtPiBaIGlzIGEgTWFya292IGNoYWluIChaIGlzIGNvbmRpdGlvbmFsbHkgaW5kZXBlbmRlbnQgb2YgWCBnaXZlbiBZKSwgdGhlbjpcblxuSChYfFopID49IEgoWHxZKVxuXG5Lbm93aW5nIHRoZSBvdXRwdXQgb2YgYSBwaXBlbGluZSAoWikgZ2l2ZXMgbm8gbW9yZSBpbmZvcm1hdGlvbiBhYm91dCB0aGUgc291cmNlIChYKSB0aGFuIGtub3dpbmcgYW4gaW50ZXJtZWRpYXRlIHN0YWdlIChZKS4gQ29tYmluZWQgd2l0aCBIKFl8WCkgPD0gSChZKSwgdGhpcyBlc3RhYmxpc2hlcyBhIGNoYWluIG9mIGVudHJvcHkgaW5lcXVhbGl0aWVzIGFsb25nIGFueSBwcm9jZXNzaW5nIHBpcGVsaW5lLiJ9LAogIHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJRdWFudGl0eSIsIkZvcm11bGEiLCJLZXkgUHJvcGVydHkiXSwicm93cyI6W1siSChYLFkpIiwiRVstbG9nIHAoWCxZKV0iLCJUb3RhbCB1bmNlcnRhaW50eSBvZiBwYWlyIl0sWyJIKFl8WCkiLCJIKFgsWSkgLSBIKFgpIiwiUmVtYWluaW5nIHVuY2VydGFpbnR5IGdpdmVuIFgiXSxbIkNoYWluIHJ1bGUiLCJIKFgsWSk9SChYKStIKFl8WCkiLCJGdW5kYW1lbnRhbCBkZWNvbXBvc2l0aW9uIl0sWyJTdWJhZGRpdGl2aXR5IiwiSChYLFkpIDw9IEgoWCkrSChZKSIsIkVxdWFsaXR5IGlmZiBpbmRlcGVuZGVudCJdLFsiQ29uZGl0aW9uaW5nIiwiSChZfFgpIDw9IEgoWSkiLCJFcXVhbGl0eSBpZmYgaW5kZXBlbmRlbnQiXSxbIkgoZihYKSkgPD0gSChYKSIsIuKAlCIsIkZ1bmN0aW9ucyBkZXN0cm95IGluZm9ybWF0aW9uIl1dfSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkNvbmRpdGlvbmluZyBDYW4gSW5jcmVhc2UgRW50cm9weSBmb3IgU3BlY2lmaWMgVmFsdWVzIiwiY29udGVudCI6IkgoWXxYKSA8PSBIKFkpIGhvbGRzIGluIGV4cGVjdGF0aW9uLiBGb3IgYSBzcGVjaWZpYyBvdXRjb21lIFg9eDAsIEgoWXxYPXgwKSBjYW4gZXhjZWVkIEgoWSkuIEV4YW1wbGU6IGtub3dpbmcgc29tZW9uZSBpcyBpbiBhIHNwZWNpZmljIGNpdHkgbWlnaHQgaW5jcmVhc2UgdW5jZXJ0YWludHkgYWJvdXQgd2hpY2ggbmVpZ2hib3VyaG9vZCB0aGV5IGFyZSBpbiAoaWYgeW91IHByZXZpb3VzbHkgaGFkIHN0cm9uZyBwcmlvciBiZWxpZWZzKS4gT25seSB0aGUgZXhwZWN0YXRpb24gb3ZlciBYIGlzIGd1YXJhbnRlZWQgdG8gYmUgbm9uLWluY3JlYXNpbmcuIn0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkFyY2hpdGVjdCBVc2U6IFdoeSBUcmFuc2Zvcm1lciBMYXllcnMgQ2Fubm90IEluY3JlYXNlIEluZm9ybWF0aW9uIiwiY29udGVudCI6IkVhY2ggdHJhbnNmb3JtZXIgbGF5ZXIgY29tcHV0ZXMgWiA9IGYoWCkgZGV0ZXJtaW5pc3RpY2FsbHksIHNvIEgoWikgPD0gSChYKS4gSG93ZXZlciBhdHRlbnRpb24gKyByZXNpZHVhbCBjb25uZWN0aW9ucyBtYWtlIGYgbmVhcmx5IGludmVydGlibGUgaW4gcHJhY3RpY2UsIG1lYW5pbmcgSChaKSDiiYggSChYKSB0aHJvdWdob3V0LiBPbmx5IHRoZSBmaW5hbCBzb2Z0bWF4IHByb2plY3Rpb24gaXMgYSBnZW51aW5lIGxvc3N5IGNvbXByZXNzaW9uLiBUaGlzIGlzIHdoeSByZXNpZHVhbCBjb25uZWN0aW9ucyBhcmUgc28gaW1wb3J0YW50IOKAlCB0aGV5IGtlZXAgdGhlIGZvcndhcmQgcGFzcyBuZWFybHkgbG9zc2xlc3MsIG1heGltaXNpbmcgaW5mb3JtYXRpb24gYXZhaWxhYmxlIGZvciB0aGUgb3V0cHV0IGxheWVyLiJ9Cl0="
---
# Joint Entropy and Conditional Entropy

Joint and conditional entropy extend Shannon entropy to multiple random variables. They formalise how information is shared or remains private between variables, and give rise to the chain rule of entropy.

## Joint Entropy

$$H(X,Y) = -\sum_{x,y} p(x,y)\log p(x,y) = \mathbb{E}[-\log p(X,Y)]$$

Joint entropy measures the total uncertainty of the pair (X,Y). It generalises to n variables via H(X₁,...,Xₙ) = −E[log p(X₁,...,Xₙ)].

## Conditional Entropy

$$H(Y|X) = \sum_x p(x)\,H(Y|X=x) = -\sum_{x,y} p(x,y)\log p(y|x) = \mathbb{E}[-\log p(Y|X)]$$

Conditional entropy is always non-negative: H(Y|X) ≥ 0, with equality iff Y is a deterministic function of X. **Conditioning reduces entropy:** H(Y|X) ≤ H(Y), with equality iff X ⊥ Y.

## Chain Rule of Entropy

$$H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)$$

Multivariate: $H(X_1,\ldots,X_n) = \sum_{i=1}^n H(X_i | X_1,\ldots,X_{i-1})$

This is the log form of the chain rule of probability. Autoregressive language models estimate each conditional term $H(X_t|X_1,\ldots,X_{t-1})$ — their sum equals the total sequence entropy.

> **INFO: Autoregressive Models and the Chain Rule**
> GPT-style models maximise $\sum_t \log p(x_t|x_1,\ldots,x_{t-1})$ — exactly the chain-rule decomposition of sequence entropy. Perplexity = exp(average token cross-entropy).

## Subadditivity of Entropy

$$H(X,Y) \leq H(X) + H(Y)$$

Equality iff X ⊥ Y. The gap $H(X)+H(Y)-H(X,Y) = I(X;Y)$ is the mutual information — the shared information between variables.

```python
import numpy as np

def entropy_bits(p):
    p = np.asarray(p, dtype=float)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

def joint_entropy(p_xy):
    return entropy_bits(p_xy.flatten())

def conditional_entropy_h_y_given_x(p_xy):
    return joint_entropy(p_xy) - entropy_bits(p_xy.sum(axis=1))

p_xy = np.array([[0.4, 0.1],[0.1, 0.4]])
p_x  = p_xy.sum(axis=1)
p_y  = p_xy.sum(axis=0)

h_xy            = joint_entropy(p_xy)               # 1.722 bits
h_x             = entropy_bits(p_x)                 # 1.000 bit
h_y             = entropy_bits(p_y)                 # 1.000 bit
h_y_given_x     = conditional_entropy_h_y_given_x(p_xy)  # 0.722 < h_y
mi              = h_x + h_y - h_xy                  # 0.278 (shared)

print(f'H(X,Y)  = {h_xy:.3f}')
print(f'H(Y|X)  = {h_y_given_x:.3f}')
print(f'I(X;Y)  = {mi:.3f}')
```

## Conditioning Reduces Entropy — Proof Sketch

$I(X;Y) = H(Y) - H(Y|X) \geq 0 \Rightarrow H(Y|X) \leq H(Y)$.

Note: For a specific realisation $x_0$, $H(Y|X=x_0)$ can exceed $H(Y)$ — the inequality holds only in expectation.

## Entropy of Functions

If $Z = f(X)$ deterministically, then $H(Z) \leq H(X)$. Equality iff $f$ is invertible on the support of X. Every feature-extraction step is an information compressor.

## Data Processing Inequality for Entropy

If $X \to Y \to Z$ is a Markov chain: $H(X|Z) \geq H(X|Y)$. Downstream processing can only degrade, not improve, source-side information.

| Quantity | Formula | Key Property |
|---|---|---|
| H(X,Y) | E[−log p(X,Y)] | Total uncertainty of pair |
| H(Y\|X) | H(X,Y) − H(X) | Remaining uncertainty given X |
| Chain rule | H(X,Y)=H(X)+H(Y\|X) | Fundamental decomposition |
| Subadditivity | H(X,Y) ≤ H(X)+H(Y) | Equality iff independent |
| Conditioning | H(Y\|X) ≤ H(Y) | Equality iff independent |
| Functions | H(f(X)) ≤ H(X) | Functions destroy information |

> **WARNING: Conditioning Can Increase Entropy for Specific Values**
> H(Y|X) ≤ H(Y) holds in expectation. For a specific x₀, H(Y|X=x₀) can exceed H(Y). Only the expectation is guaranteed non-increasing.

> **TIP: Why Transformer Layers Cannot Increase Information**
> Each layer computes Z = f(X) deterministically, so H(Z) ≤ H(X). Residual connections make f nearly invertible, keeping H(Z) ≈ H(X) throughout the network — maximising information for the output layer.