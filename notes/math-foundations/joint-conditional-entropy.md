---
title: "Joint Entropy and Conditional Entropy"
slug: "joint-conditional-entropy"
description: "Joint entropy H(X,Y), conditional entropy H(Y|X), the chain rule, subadditivity, and information-theoretic implications for deep learning pipelines."
tags: ["information-theory","math","foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSm9pbnQgYW5kIGNvbmRpdGlvbmFsIGVudHJvcHkgZXh0ZW5kIFNoYW5ub24gZW50cm9weSB0byBwYWlycyBhbmQgc2VxdWVuY2VzIG9mIHJhbmRvbSB2YXJpYWJsZXMsIGZvcm1hbGl6aW5nIGhvdyBpbmZvcm1hdGlvbiBpcyBzaGFyZWQgYmV0d2VlbiB2YXJpYWJsZXMgYW5kIGhvdyBvYnNlcnZpbmcgb25lIHZhcmlhYmxlIGNoYW5nZXMgdW5jZXJ0YWludHkgYWJvdXQgYW5vdGhlci4gVGhleSBnaXZlIHJpc2UgdG8gdGhlIGNoYWluIHJ1bGUgb2YgZW50cm9weSDigJQgdGhlIGFsZ2VicmFpYyBpZGVudGl0eSB1bmRlcmx5aW5nIGF1dG9yZWdyZXNzaXZlIGxhbmd1YWdlIG1vZGVsIHRyYWluaW5nIOKAlCBhbmQgdG8gc3ViYWRkaXRpdml0eSwgd2hpY2ggc2hvd3MgaG93IGNvcnJlbGF0aW9uIGNvbXByZXNzZXMgam9pbnQgdW5jZXJ0YWludHkuIE1hc3RlcmluZyB0aGVzZSBxdWFudGl0aWVzIGlzIHByZXJlcXVpc2l0ZSB0byBtdXR1YWwgaW5mb3JtYXRpb24sIHRoZSBkYXRhIHByb2Nlc3NpbmcgaW5lcXVhbGl0eSwgYW5kIHRoZSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrIHRoZW9yeSBvZiBkZWVwIGxlYXJuaW5nLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvcmUgRGVmaW5pdGlvbjogSm9pbnQgYW5kIENvbmRpdGlvbmFsIEVudHJvcHkifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkpvaW50IGVudHJvcHkgSChYLFkpID0gLXN1bV97eCx5fSBwKHgseSkgbG9nIHAoeCx5KSA9IEVbLWxvZyBwKFgsWSldIG1lYXN1cmVzIHRvdGFsIHVuY2VydGFpbnR5IG9mIHRoZSBwYWlyLiBJdCBzYXRpc2ZpZXMgSChYLFkpID49IG1heChIKFgpLCBIKFkpKSBhbmQgZ2VuZXJhbGl6ZXMgbmF0dXJhbGx5IHRvIG4gdmFyaWFibGVzOiBIKFgxLC4uLixYbikgPSAtRVtsb2cgcChYMSwuLi4sWG4pXS4gQ29uZGl0aW9uYWwgZW50cm9weSBIKFl8WCkgPSBzdW1feCBwKHgpIEgoWXxYPXgpID0gLXN1bV97eCx5fSBwKHgseSkgbG9nIHAoeXx4KSA9IEVbLWxvZyBwKFl8WCldIGlzIHRoZSBleHBlY3RlZCByZW1haW5pbmcgdW5jZXJ0YWludHkgYWJvdXQgWSBhZnRlciBvYnNlcnZpbmcgWC4gQm90aCBhcmUgYWx3YXlzIG5vbi1uZWdhdGl2ZS4gSChZfFgpPTAgaWZmIFkgaXMgYSBkZXRlcm1pbmlzdGljIGZ1bmN0aW9uIG9mIFg7IEgoWXxYKT1IKFkpIGlmZiBYIGFuZCBZIGFyZSBpbmRlcGVuZGVudC4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBlbnRyb3B5X2JpdHMocCk6XG4gICAgcCA9IG5wLmFzYXJyYXkocCwgZHR5cGU9ZmxvYXQpXG4gICAgbWFzayA9IHAgPiAwXG4gICAgcmV0dXJuIGZsb2F0KC1ucC5zdW0ocFttYXNrXSAqIG5wLmxvZzIocFttYXNrXSkpKVxuXG5kZWYgam9pbnRfZW50cm9weShwX3h5KTpcbiAgICAjIEgoWCxZKSBmcm9tIDItRCBqb2ludCBwcm9iYWJpbGl0eSBtYXRyaXhcbiAgICByZXR1cm4gZW50cm9weV9iaXRzKHBfeHkuZmxhdHRlbigpKVxuXG5kZWYgY29uZGl0aW9uYWxfZW50cm9weShwX3h5KTpcbiAgICAjIEgoWXxYKSA9IEgoWCxZKSAtIEgoWClcbiAgICBwX3ggPSBwX3h5LnN1bShheGlzPTEpICAjIG1hcmdpbmFsIG9mIFggKHJvdyBzdW1zKVxuICAgIHJldHVybiBqb2ludF9lbnRyb3B5KHBfeHkpIC0gZW50cm9weV9iaXRzKHBfeClcblxuIyBDb3JyZWxhdGVkIGJpbmFyeSB2YXJpYWJsZXNcbnBfeHkgPSBucC5hcnJheShbWzAuNDAsIDAuMTBdLFxuICAgICAgICAgICAgICAgICAgWzAuMTAsIDAuNDBdXSlcbnBfeCA9IHBfeHkuc3VtKGF4aXM9MSkgICAjIFswLjUsIDAuNV1cbnBfeSA9IHBfeHkuc3VtKGF4aXM9MCkgICAjIFswLjUsIDAuNV1cblxuaF94eSAgICAgICAgPSBqb2ludF9lbnRyb3B5KHBfeHkpICAgICAgICAjIDEuNzIyIGJpdHNcbmhfeCAgICAgICAgID0gZW50cm9weV9iaXRzKHBfeCkgICAgICAgICAgIyAxLjAwMCBiaXRcbmhfeSAgICAgICAgID0gZW50cm9weV9iaXRzKHBfeSkgICAgICAgICAgIyAxLjAwMCBiaXRcbmhfeV9naXZlbl94ID0gY29uZGl0aW9uYWxfZW50cm9weShwX3h5KSAgIyAwLjcyMiBiaXQgPCBoX3lcbm1pICAgICAgICAgID0gaF94ICsgaF95IC0gaF94eSAgICAgICAgICAjIDAuMjc4IGJpdCBzaGFyZWQgaW5mb1xuXG5wcmludChmJ0goWCxZKSA9IHtoX3h5Oi4zZn0gYml0cycpXG5wcmludChmJ0goWXxYKSA9IHtoX3lfZ2l2ZW5feDouM2Z9IGJpdHMgIFs8IEgoWSk9e2hfeTouM2Z9XScpXG5wcmludChmJ0koWDtZKSA9IHttaTouM2Z9IGJpdHMnKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1hdGhlbWF0aWNhbCBQcm9wZXJ0aWVzIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDaGFpbiBydWxlOiBIKFgsWSkgPSBIKFgpICsgSChZfFgpID0gSChZKSArIEgoWHxZKS4gTXVsdGl2YXJpYXRlIGNoYWluIHJ1bGU6IEgoWDEsLi4uLFhuKSA9IEgoWDEpICsgSChYMnxYMSkgKyAuLi4gKyBIKFhufFgxLC4uLixYX3tuLTF9KSA9IHN1bV9pIEgoWGl8WDEsLi4uLFhfe2ktMX0pLiBUaGlzIGlzIHRoZSBsb2cgZm9ybSBvZiB0aGUgcHJvYmFiaWxpdHkgY2hhaW4gcnVsZSBsb2cgcCh4MSwuLi4seG4pID0gc3VtX2kgbG9nIHAoeGl8eDEsLi4uLHhfe2ktMX0pLiBTdWJhZGRpdGl2aXR5OiBIKFgsWSkgPD0gSChYKStIKFkpLCBlcXVhbGl0eSBpZmYgWCBhbmQgWSBhcmUgaW5kZXBlbmRlbnQ7IHRoZSBnYXAgSChYKStIKFkpLUgoWCxZKSBlcXVhbHMgbXV0dWFsIGluZm9ybWF0aW9uIEkoWDtZKS4gQ29uZGl0aW9uaW5nIHJlZHVjZXMgZW50cm9weTogSChZfFgpIDw9IEgoWSksIGVxdWFsaXR5IGlmZiBpbmRlcGVuZGVudC4gRW50cm9weSBvZiBmdW5jdGlvbnM6IEgoZihYKSkgPD0gSChYKSBmb3IgYW55IGRldGVybWluaXN0aWMgZiwgd2l0aCBlcXVhbGl0eSBpZmYgZiBpcyBpbnZlcnRpYmxlIG9uIHRoZSBzdXBwb3J0IG9mIFguIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZW50cm9weV9iaXRzKHApOlxuICAgIHAgPSBucC5hc2FycmF5KHAsIGR0eXBlPWZsb2F0KVxuICAgIG1hc2sgPSBwID4gMFxuICAgIHJldHVybiBmbG9hdCgtbnAuc3VtKHBbbWFza10gKiBucC5sb2cyKHBbbWFza10pKSlcblxuIyBWZXJpZnkgY2hhaW4gcnVsZTogSChYLFkpID09IEgoWCkgKyBIKFl8WClcbnBfeHkgPSBucC5hcnJheShbWzAuMzAsIDAuMjBdLCBbMC4xMCwgMC40MF1dKVxucF94ICA9IHBfeHkuc3VtKGF4aXM9MSlcbnBfeSAgPSBwX3h5LnN1bShheGlzPTApXG5cbmhfeHkgICAgICAgID0gZW50cm9weV9iaXRzKHBfeHkuZmxhdHRlbigpKVxuaF94ICAgICAgICAgPSBlbnRyb3B5X2JpdHMocF94KVxuaF95ICAgICAgICAgPSBlbnRyb3B5X2JpdHMocF95KVxuaF95X2dpdmVuX3ggPSBoX3h5IC0gaF94XG5oX3hfZ2l2ZW5feSA9IGhfeHkgLSBoX3lcblxucHJpbnQoZidIKFgsWSkgICAgICAgICA9IHtoX3h5Oi40Zn0nKVxucHJpbnQoZidIKFgpK0goWXxYKSAgICA9IHtoX3g6LjRmfSArIHtoX3lfZ2l2ZW5feDouNGZ9ID0ge2hfeCtoX3lfZ2l2ZW5feDouNGZ9JykgICMgZXF1YWxzIEgoWCxZKVxucHJpbnQoZidTdWJhZGRpdGl2aXR5IGdhcCBJKFg7WSkgPSB7aF94K2hfeS1oX3h5Oi40Zn0gYml0cycpXG5cbiMgSW5kZXBlbmRlbnQgY2FzZTogZ2FwIHNob3VsZCBiZSB6ZXJvXG5wX3h5X2luZGVwID0gbnAub3V0ZXIocF94LCBwX3kpICAjIHByb2R1Y3QgZGlzdHJpYnV0aW9uXG5oX2luZGVwICAgID0gZW50cm9weV9iaXRzKHBfeHlfaW5kZXAuZmxhdHRlbigpKVxucHJpbnQoZidIKFgsWSkgaW5kZXBlbmRlbnQgPSB7aF9pbmRlcDouNGZ9LCBIKFgpK0goWSkgPSB7aF94K2hfeTouNGZ9JykifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWYXJpYW50cyBhbmQgU3BlY2lhbCBDYXNlcyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGkuaS5kLiBzb3VyY2VzIHRoZSBtdWx0aXZhcmlhdGUgY2hhaW4gcnVsZSBzaW1wbGlmaWVzIHRvIEgoWDEsLi4uLFhuKT1uKkgoWDEpLiBGb3IgTWFya292IGNoYWlucyBIKFh0fFgxLC4uLixYX3t0LTF9KT1IKFh0fFhfe3QtMX0pLCBnaXZpbmcgZW50cm9weSByYXRlIGggPSBIKFgyfFgxKS4gRW50cm9weSBvZiBmdW5jdGlvbnMgSChmKFgpKSA8PSBIKFgpOiBtYW55LXRvLW9uZSBmdW5jdGlvbnMgc3RyaWN0bHkgcmVkdWNlIGVudHJvcHk7IGJpamVjdGlvbnMgcHJlc2VydmUgaXQgZXhhY3RseS4gRGF0YSBQcm9jZXNzaW5nIEluZXF1YWxpdHkgKERQSSkgZm9yIGVudHJvcHk6IGlmIFggLT4gWSAtPiBaIGlzIGEgTWFya292IGNoYWluIHRoZW4gSChYfFopID49IEgoWHxZKSDigJQgZG93bnN0cmVhbSBwcm9jZXNzaW5nIGNhbm5vdCByZWNvdmVyIGluZm9ybWF0aW9uIGxvc3QgYXQgYW4gaW50ZXJtZWRpYXRlIHN0ZXAuIENvbmRpdGlvbmluZyBvbiBhIHNwZWNpZmljIHZhbHVlIHgwIGNhbiByYWlzZSBlbnRyb3B5IEgoWXxYPXgwKSA+IEgoWSk7IHRoZSBpbmVxdWFsaXR5IEgoWXxYKSA8PSBIKFkpIGhvbGRzIG9ubHkgaW4gZXhwZWN0YXRpb24gb3ZlciBYLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1MIGFuZCBBSSBDb25uZWN0aW9ucyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXV0b3JlZ3Jlc3NpdmUgTE0gdHJhaW5pbmcgbWF4aW1pemVzIHN1bV90IGxvZyBwKHh0fHgxLC4uLix4X3t0LTF9KSwgd2hpY2ggYnkgdGhlIGNoYWluIHJ1bGUgZXF1YWxzIGxvZyBwKHgxLC4uLix4VCkg4oCUIHRoZSBmdWxsIHNlcXVlbmNlIGpvaW50IGxvZy1wcm9iYWJpbGl0eSB1bmRlciB0aGUgbW9kZWwuIFBlcnBsZXhpdHkgUFBMID0gZXhwKGF2ZXJhZ2UgdG9rZW4gY3Jvc3MtZW50cm9weSkgZGlyZWN0bHkgZXN0aW1hdGVzIGV4cChIX3JhdGUpLiBUaGUgaW5mb3JtYXRpb24gYm90dGxlbmVjayB0aGVvcnkgdmlld3MgZWFjaCBuZXVyYWwgbGF5ZXIgYXMgY29tcHJlc3NpbmcgWCBpbnRvIFo6IEgoWikgPD0gSChYKSwgYW5kIHRoZSBsZWFybmluZyBnb2FsIGlzIHRvIHJldGFpbiBJKFo7WSkgd2hpbGUgbWluaW1pemluZyBJKFg7WikuIEZlYXR1cmUgZW5naW5lZXJpbmcgd29ya3MgcHJlY2lzZWx5IGJlY2F1c2UgYWRkaW5nIGluZm9ybWF0aXZlIGZlYXR1cmVzIHJlZHVjZXMgSChZfGZlYXR1cmVzKSwgbG93ZXJpbmcgdGhlIEJheWVzLW9wdGltYWwgZXJyb3IuIERlY2lzaW9uIHRyZWUgaW5mb3JtYXRpb24gZ2FpbiBpcyB0aGUgcmVkdWN0aW9uIGluIEgoWXxmZWF0dXJlKSwgc2VsZWN0aW5nIHNwbGl0cyB0aGF0IG1vc3QgcmVkdWNlIGNvbmRpdGlvbmFsIGVudHJvcHkuIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZW50cm9weV9iaXRzKHApOlxuICAgIHAgPSBucC5hc2FycmF5KHAsIGR0eXBlPWZsb2F0KVxuICAgIG1hc2sgPSBwID4gMFxuICAgIHJldHVybiBmbG9hdCgtbnAuc3VtKHBbbWFza10gKiBucC5sb2cyKHBbbWFza10pKSlcblxuZGVmIG11dHVhbF9pbmZvX2Zyb21fam9pbnQocF94eSk6XG4gICAgcF94ICAgPSBwX3h5LnN1bShheGlzPTEpXG4gICAgcF95ICAgPSBwX3h5LnN1bShheGlzPTApXG4gICAgaF94eSAgPSBlbnRyb3B5X2JpdHMocF94eS5mbGF0dGVuKCkpXG4gICAgaF94ICAgPSBlbnRyb3B5X2JpdHMocF94KVxuICAgIGhfeSAgID0gZW50cm9weV9iaXRzKHBfeSlcbiAgICBoX3lfeCA9IGhfeHkgLSBoX3ggICAjIEgoWXxYKVxuICAgIG1pICAgID0gaF95IC0gaF95X3ggICMgSShYO1kpID0gSChZKSAtIEgoWXxYKVxuICAgIHJldHVybiBoX3ksIGhfeV94LCBtaVxuXG4jIENvbmRpdGlvbmluZyByZWR1Y2VzIGVudHJvcHkgbW9yZSB3aGVuIHZhcmlhYmxlcyBhcmUgY29ycmVsYXRlZFxucF9zdHJvbmcgPSBucC5hcnJheShbWzAuNDUsIDAuMDVdLCBbMC4wNSwgMC40NV1dKSAgIyBoaWdoIGNvcnJlbGF0aW9uXG5wX3dlYWsgICA9IG5wLmFycmF5KFtbMC4yNiwgMC4yNF0sIFswLjI0LCAwLjI2XV0pICAjIGxvdyBjb3JyZWxhdGlvblxucF9pbmRlcCAgPSBucC5hcnJheShbWzAuMjUsIDAuMjVdLCBbMC4yNSwgMC4yNV1dKSAgIyBpbmRlcGVuZGVudFxuXG5mb3IgbmFtZSwgcCBpbiBbKCdzdHJvbmcnLCBwX3N0cm9uZyksICgnd2VhaycsIHBfd2VhayksICgnaW5kZXAnLCBwX2luZGVwKV06XG4gICAgaF95LCBoX3lfeCwgbWkgPSBtdXR1YWxfaW5mb19mcm9tX2pvaW50KHApXG4gICAgcHJpbnQoZid7bmFtZTo2c306IEgoWSk9e2hfeTouM2Z9ICBIKFl8WCk9e2hfeV94Oi4zZn0gIEkoWDtZKT17bWk6LjNmfScpIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW1wbGVtZW50YXRpb24gUGl0ZmFsbHMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gY29tcHV0aW5nIGpvaW50IGVudHJvcHkgZnJvbSBlbXBpcmljYWwgY291bnRzLCBub3JtYWxpemUgdGhlIGNvdW50IG1hdHJpeCB0byBwcm9iYWJpbGl0aWVzIGFuZCB2ZXJpZnkgaXQgc3VtcyB0byAxIGJlZm9yZSBwcm9jZWVkaW5nLiBGb3IgY29tcHV0aW5nIEgoWXxYKSA9IHN1bV94IHAoeCkqSChZfFg9eCksIGhhbmRsZSByb3dzIHdoZXJlIHBfeD0wIGJ5IHNraXBwaW5nIHRoZW0g4oCUIGRpdmlkaW5nIGEgcm93IGJ5IHplcm8gcHJvYmFiaWxpdHkgY3JlYXRlcyBOYU4uIEJld2FyZSB0aGF0IEgoWXxYPXgwKSBmb3IgYSBzcGVjaWZpYyB2YWx1ZSBjYW4gZXhjZWVkIEgoWSk6IGNvbmRpdGlvbmluZyBvbiBhIHNwZWNpZmljIG91dGNvbWUgaXMgbm90IHRoZSBzYW1lIGFzIGNvbmRpdGlvbmluZyBvbiB0aGUgdmFyaWFibGUgaW4gZXhwZWN0YXRpb24uIEZvciBzZXF1ZW5jZSBtb2RlbHMsIHRyYWNrIGVhY2ggY29uZGl0aW9uYWwgdGVybSBIKFh0fFhfezx0fSkgc2VwYXJhdGVseSB0byBpZGVudGlmeSB3aGljaCBwb3NpdGlvbnMgYXJlIG1vc3QgdW5jZXJ0YWluLCByYXRoZXIgdGhhbiBhdmVyYWdpbmcgcGVycGxleGl0eSBhY3Jvc3MgYWxsIHBvc2l0aW9ucy4ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgR3VpZGFuY2UifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVzZSBjb25kaXRpb25hbCBlbnRyb3B5IEgoTGFiZWx8RmVhdHVyZXMpIHRvIHF1YW50aWZ5IGhvdyBtdWNoIHJlc2lkdWFsIHVuY2VydGFpbnR5IHRoZSBmZWF0dXJlcyBsZWF2ZSDigJQgbG93ZXIgaXMgYmV0dGVyLiBDb21wdXRlIEkoWDtZKSA9IEgoWSkgLSBIKFl8WCkgdG8gbWVhc3VyZSBmZWF0dXJlIHJlbGV2YW5jZSB3aXRob3V0IGZpdHRpbmcgYSBtb2RlbC4gRm9yIExMTSBkZWJ1Z2dpbmcsIHRyYWNrIHBlci1wb3NpdGlvbiBlbnRyb3B5IEgoWHR8Y29udGV4dCkgdG8gbG9jYXRlIGhpZ2gtdW5jZXJ0YWludHkgcG9zaXRpb25zIGluIHNlcXVlbmNlcyDigJQgdGhlc2UgY29ycmVzcG9uZCB0byBhbWJpZ3VvdXMgdG9rZW5zIHdoZXJlIHRoZSBtb2RlbCBzcHJlYWRzIHByb2JhYmlsaXR5IG1hc3MuIFdoZW4gYW5hbHl6aW5nIGluZm9ybWF0aW9uIGZsb3cgaW4gYSBwaXBlbGluZSBYIC0+IFkgLT4gWiwgbWVhc3VyZSBJKFg7WSkgYW5kIEkoWTtaKSBzZXBhcmF0ZWx5IHRvIGxvY2FsaXplIHdoZXJlIGluZm9ybWF0aW9uIGlzIGxvc3QuIFJlc2lkdWFsIGNvbm5lY3Rpb25zIGluIHRyYW5zZm9ybWVycyBtYWludGFpbiBIKGxheWVyIG91dHB1dCkgfj0gSChsYXllciBpbnB1dCkgYnkga2VlcGluZyBlYWNoIGxheWVyIG5lYXJseSBpbnZlcnRpYmxlLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGVudHJvcHlfYml0cyhwKTpcbiAgICBwID0gbnAuYXNhcnJheShwLCBkdHlwZT1mbG9hdClcbiAgICBtYXNrID0gcCA+IDBcbiAgICByZXR1cm4gZmxvYXQoLW5wLnN1bShwW21hc2tdICogbnAubG9nMihwW21hc2tdKSkpXG5cbmRlZiB0cmFuc2Zvcm1fZW50cm9weV9sb3NzKHByb2JzLCB0cmFuc2Zvcm1fZm4pOlxuICAgICMgQ29tcHV0ZSBIKFgpIGFuZCBIKGYoWCkpIHRvIG1lYXN1cmUgaW5mb3JtYXRpb24gbG9zc1xuICAgIHAgID0gbnAuYXJyYXkocHJvYnMpXG4gICAgeHMgPSBucC5hcmFuZ2UobGVuKHApKVxuICAgIHlzID0gbnAuYXJyYXkoW3RyYW5zZm9ybV9mbih4KSBmb3IgeCBpbiB4c10pXG4gICAgIyBhZ2dyZWdhdGUgcHJvYmFiaWxpdHkgbWFzcyBhdCBlYWNoIG91dHB1dCB2YWx1ZVxuICAgIG91dF92YWxzID0gbnAudW5pcXVlKHlzKVxuICAgIHBfb3V0ID0gbnAuYXJyYXkoW3BbeXMgPT0gdl0uc3VtKCkgZm9yIHYgaW4gb3V0X3ZhbHNdKVxuICAgIHJldHVybiBlbnRyb3B5X2JpdHMocCksIGVudHJvcHlfYml0cyhwX291dClcblxucCA9IFswLjI1LCAwLjI1LCAwLjI1LCAwLjI1XSAgICMgdW5pZm9ybSBvdmVyIHswLDEsMiwzfVxuaF94LCBoX2lkICAgPSB0cmFuc2Zvcm1fZW50cm9weV9sb3NzKHAsIGxhbWJkYSB4OiB4KSAgICAgICAjIGlkZW50aXR5XG5oX3gsIGhfbW9kMiA9IHRyYW5zZm9ybV9lbnRyb3B5X2xvc3MocCwgbGFtYmRhIHg6IHggJSAyKSAgIyBtYW55LXRvLW9uZVxuaF94LCBoX3NxICAgPSB0cmFuc2Zvcm1fZW50cm9weV9sb3NzKHAsIGxhbWJkYSB4OiB4KngpICAgICMgaW5qZWN0aXZlXG5cbnByaW50KGYnSChYKSAgICAgICAgICAgPSB7aF94Oi4zZn0gYml0cycpXG5wcmludChmJ0goaWRlbnRpdHkoWCkpID0ge2hfaWQ6LjNmfSBiaXRzICBbbm8gbG9zcywgYmlqZWN0aW9uXScpXG5wcmludChmJ0goWCBtb2QgMikgICAgID0ge2hfbW9kMjouM2Z9IGJpdHMgIFtpbmZvIGxvc3QsIG1hbnktdG8tb25lXScpXG5wcmludChmJ0goWCBzcXVhcmVkKSAgID0ge2hfc3E6LjNmfSBiaXRzICBbaW5qZWN0aXZlIG9uIHN1cHBvcnQsIG5vIGxvc3NdJykifSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkF1dG9yZWdyZXNzaXZlIE1vZGVscyBhbmQgdGhlIENoYWluIFJ1bGUiLCJjb250ZW50IjoiR1BULXN0eWxlIG1vZGVscyBtYXhpbWl6ZSBzdW1fdCBsb2cgcCh4dCB8IHgxLC4uLix4X3t0LTF9KS4gQnkgdGhlIGNoYWluIHJ1bGUsIHRoaXMgaXMgZXhhY3RseSBsb2cgcCh4MSwuLi4seFQpIOKAlCB0aGUgam9pbnQgbG9nLXByb2JhYmlsaXR5IG9mIHRoZSBzZXF1ZW5jZS4gVHJhaW5pbmcgY3Jvc3MtZW50cm9weSBpcyBIKHBfdHJ1ZSwgcV9tb2RlbCkgd2hlcmUgdGhlIGNoYWluIHJ1bGUgZmFjdG9ycyBib3RoIHBfdHJ1ZSBhbmQgcV9tb2RlbCBpZGVudGljYWxseS4gUGVycGxleGl0eSA9IGV4cChhdmVyYWdlIHRva2VuIENFKSA9IGV4cChIKHAscSkpIGRpcmVjdGx5IGVzdGltYXRlcyB0aGUgZWZmZWN0aXZlIGJyYW5jaGluZyBmYWN0b3IgYXQgZWFjaCBzdGVwLCBpbnRlcnByZXRhYmxlIGFzIGhvdyBtYW55IGVxdWFsbHkgbGlrZWx5IGNob2ljZXMgdGhlIG1vZGVsIGZhY2VzIG9uIGF2ZXJhZ2UuIn0sCiAgeyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlF1YW50aXR5IiwiRm9ybXVsYSIsIktleSBQcm9wZXJ0eSJdLCJyb3dzIjpbWyJIKFgsWSkiLCJFWy1sb2cgcChYLFkpXSIsIlRvdGFsIHVuY2VydGFpbnR5OyBhbHdheXMgPj0gbWF4KEgoWCksSChZKSkiXSxbIkgoWXxYKSIsIkgoWCxZKSAtIEgoWCkiLCJSZW1haW5pbmcgdW5jZXJ0YWludHkgYWJvdXQgWSBnaXZlbiBYIl0sWyJDaGFpbiBydWxlIiwiSChYLFkpID0gSChYKSArIEgoWXxYKSIsIkZ1bmRhbWVudGFsIGRlY29tcG9zaXRpb24gb2Ygam9pbnQgZW50cm9weSJdLFsiU3ViYWRkaXRpdml0eSIsIkgoWCxZKSA8PSBIKFgpK0goWSkiLCJFcXVhbGl0eSBpZmYgWCBhbmQgWSBpbmRlcGVuZGVudCJdLFsiQ29uZGl0aW9uaW5nIiwiSChZfFgpIDw9IEgoWSkiLCJFcXVhbGl0eSBpZmYgWCBhbmQgWSBpbmRlcGVuZGVudCJdLFsiRnVuY3Rpb25zIiwiSChmKFgpKSA8PSBIKFgpIiwiRXF1YWxpdHkgaWZmIGYgaW52ZXJ0aWJsZSBvbiBzdXBwb3J0IG9mIFgiXSxbIkRQSSIsIkgoWHxaKSA+PSBIKFh8WSkgZm9yIFgtPlktPloiLCJQcm9jZXNzaW5nIGNhbm5vdCByZWNvdmVyIGxvc3QgaW5mb3JtYXRpb24iXV19LAogIHsidHlwZSI6ImRpdmlkZXIifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0sCiAgeyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJIKFgsWSkgPSBFWy1sb2cgcChYLFkpXSDigJQgam9pbnQgZW50cm9weSBtZWFzdXJlcyB0b3RhbCB1bmNlcnRhaW50eSBvZiBhIHBhaXI7IGFsd2F5cyBhdCBsZWFzdCBhcyBsYXJnZSBhcyBlYWNoIG1hcmdpbmFsIiwiSChZfFgpID0gSChYLFkpIC0gSChYKSDigJQgY29uZGl0aW9uYWwgZW50cm9weSBpcyByZW1haW5pbmcgdW5jZXJ0YWludHkgYWJvdXQgWSBhZnRlciBvYnNlcnZpbmcgWDsgYWx3YXlzIG5vbi1uZWdhdGl2ZSIsIkNoYWluIHJ1bGUgSChYLFkpPUgoWCkrSChZfFgpIGlzIHRoZSBmb3VuZGF0aW9uIG9mIGF1dG9yZWdyZXNzaXZlIExNIHRyYWluaW5nIGFuZCBzZXF1ZW5jZSBsaWtlbGlob29kIGZhY3Rvcml6YXRpb24iLCJTdWJhZGRpdGl2aXR5IEgoWCxZKSA8PSBIKFgpK0goWSkg4oCUIHRoZSBnYXAgSShYO1kpID0gSChYKStIKFkpLUgoWCxZKSBpcyB0aGUgbXV0dWFsIGluZm9ybWF0aW9uIGJldHdlZW4gdmFyaWFibGVzIiwiQ29uZGl0aW9uaW5nIHJlZHVjZXMgZW50cm9weSBpbiBleHBlY3RhdGlvbjsgZm9yIGEgc3BlY2lmaWMgb3V0Y29tZSB4MCwgSChZfFg9eDApIGNhbiBleGNlZWQgSChZKSIsIkgoZihYKSkgPD0gSChYKSBmb3IgYW55IGRldGVybWluaXN0aWMgZnVuY3Rpb24g4oCUIGluZm9ybWF0aW9uIGNhbiBvbmx5IGJlIGxvc3Qgb3IgcHJlc2VydmVkLCBuZXZlciBjcmVhdGVkLCBieSBwcm9jZXNzaW5nIiwiRGF0YSBwcm9jZXNzaW5nIGluZXF1YWxpdHk6IGZvciBYLT5ZLT5aIE1hcmtvdiBjaGFpbiwgSChYfFopID49IEgoWHxZKSDigJQgbm8gZG93bnN0cmVhbSBzdGFnZSBjYW4gcmVjb3ZlciBsb3N0IGluZm9ybWF0aW9uIl19Cl0K"
---
# Joint Entropy and Conditional Entropy

Joint and conditional entropy extend Shannon entropy to pairs and sequences of random variables, formalizing how information is shared between variables and how observing one variable changes uncertainty about another. They give rise to the chain rule of entropy — the algebraic identity underlying autoregressive language model training — and to subadditivity, which shows how correlation compresses joint uncertainty. Mastering these quantities is prerequisite to mutual information, the data processing inequality, and the information bottleneck theory of deep learning.

## Core Definition: Joint and Conditional Entropy

Joint entropy H(X,Y) = -sum_{x,y} p(x,y) log p(x,y) = E[-log p(X,Y)] measures total uncertainty of the pair. It satisfies H(X,Y) >= max(H(X), H(Y)) and generalizes naturally to n variables: H(X1,...,Xn) = -E[log p(X1,...,Xn)]. Conditional entropy H(Y|X) = sum_x p(x) H(Y|X=x) = -sum_{x,y} p(x,y) log p(y|x) = E[-log p(Y|X)] is the expected remaining uncertainty about Y after observing X. Both are always non-negative. H(Y|X)=0 iff Y is a deterministic function of X; H(Y|X)=H(Y) iff X and Y are independent.

```python
import numpy as np

def entropy_bits(p):
    p = np.asarray(p, dtype=float)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

def joint_entropy(p_xy):
    # H(X,Y) from 2-D joint probability matrix
    return entropy_bits(p_xy.flatten())

def conditional_entropy(p_xy):
    # H(Y|X) = H(X,Y) - H(X)
    p_x = p_xy.sum(axis=1)  # marginal of X (row sums)
    return joint_entropy(p_xy) - entropy_bits(p_x)

# Correlated binary variables
p_xy = np.array([[0.40, 0.10],
                  [0.10, 0.40]])
p_x = p_xy.sum(axis=1)   # [0.5, 0.5]
p_y = p_xy.sum(axis=0)   # [0.5, 0.5]

h_xy        = joint_entropy(p_xy)        # 1.722 bits
h_x         = entropy_bits(p_x)          # 1.000 bit
h_y         = entropy_bits(p_y)          # 1.000 bit
h_y_given_x = conditional_entropy(p_xy)  # 0.722 bit < h_y
mi          = h_x + h_y - h_xy          # 0.278 bit shared info

print(f'H(X,Y) = {h_xy:.3f} bits')
print(f'H(Y|X) = {h_y_given_x:.3f} bits  [< H(Y)={h_y:.3f}]')
print(f'I(X;Y) = {mi:.3f} bits')
```

## Mathematical Properties

Chain rule: H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y). Multivariate chain rule: H(X1,...,Xn) = H(X1) + H(X2|X1) + ... + H(Xn|X1,...,X_{n-1}) = sum_i H(Xi|X1,...,X_{i-1}). This is the log form of the probability chain rule log p(x1,...,xn) = sum_i log p(xi|x1,...,x_{i-1}). Subadditivity: H(X,Y) <= H(X)+H(Y), equality iff X and Y are independent; the gap H(X)+H(Y)-H(X,Y) equals mutual information I(X;Y). Conditioning reduces entropy: H(Y|X) <= H(Y), equality iff independent. Entropy of functions: H(f(X)) <= H(X) for any deterministic f, with equality iff f is invertible on the support of X.

```python
import numpy as np

def entropy_bits(p):
    p = np.asarray(p, dtype=float)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

# Verify chain rule: H(X,Y) == H(X) + H(Y|X)
p_xy = np.array([[0.30, 0.20], [0.10, 0.40]])
p_x  = p_xy.sum(axis=1)
p_y  = p_xy.sum(axis=0)

h_xy        = entropy_bits(p_xy.flatten())
h_x         = entropy_bits(p_x)
h_y         = entropy_bits(p_y)
h_y_given_x = h_xy - h_x
h_x_given_y = h_xy - h_y

print(f'H(X,Y)         = {h_xy:.4f}')
print(f'H(X)+H(Y|X)    = {h_x:.4f} + {h_y_given_x:.4f} = {h_x+h_y_given_x:.4f}')  # equals H(X,Y)
print(f'Subadditivity gap I(X;Y) = {h_x+h_y-h_xy:.4f} bits')

# Independent case: gap should be zero
p_xy_indep = np.outer(p_x, p_y)  # product distribution
h_indep    = entropy_bits(p_xy_indep.flatten())
print(f'H(X,Y) independent = {h_indep:.4f}, H(X)+H(Y) = {h_x+h_y:.4f}')
```

## Variants and Special Cases

For i.i.d. sources the multivariate chain rule simplifies to H(X1,...,Xn)=n*H(X1). For Markov chains H(Xt|X1,...,X_{t-1})=H(Xt|X_{t-1}), giving entropy rate h = H(X2|X1). Entropy of functions H(f(X)) <= H(X): many-to-one functions strictly reduce entropy; bijections preserve it exactly. Data Processing Inequality (DPI) for entropy: if X -> Y -> Z is a Markov chain then H(X|Z) >= H(X|Y) — downstream processing cannot recover information lost at an intermediate step. Conditioning on a specific value x0 can raise entropy H(Y|X=x0) > H(Y); the inequality H(Y|X) <= H(Y) holds only in expectation over X.

## ML and AI Connections

Autoregressive LM training maximizes sum_t log p(xt|x1,...,x_{t-1}), which by the chain rule equals log p(x1,...,xT) — the full sequence joint log-probability under the model. Perplexity PPL = exp(average token cross-entropy) directly estimates exp(H_rate). The information bottleneck theory views each neural layer as compressing X into Z: H(Z) <= H(X), and the learning goal is to retain I(Z;Y) while minimizing I(X;Z). Feature engineering works precisely because adding informative features reduces H(Y|features), lowering the Bayes-optimal error. Decision tree information gain is the reduction in H(Y|feature), selecting splits that most reduce conditional entropy.

```python
import numpy as np

def entropy_bits(p):
    p = np.asarray(p, dtype=float)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

def mutual_info_from_joint(p_xy):
    p_x   = p_xy.sum(axis=1)
    p_y   = p_xy.sum(axis=0)
    h_xy  = entropy_bits(p_xy.flatten())
    h_x   = entropy_bits(p_x)
    h_y   = entropy_bits(p_y)
    h_y_x = h_xy - h_x   # H(Y|X)
    mi    = h_y - h_y_x  # I(X;Y) = H(Y) - H(Y|X)
    return h_y, h_y_x, mi

# Conditioning reduces entropy more when variables are correlated
p_strong = np.array([[0.45, 0.05], [0.05, 0.45]])  # high correlation
p_weak   = np.array([[0.26, 0.24], [0.24, 0.26]])  # low correlation
p_indep  = np.array([[0.25, 0.25], [0.25, 0.25]])  # independent

for name, p in [('strong', p_strong), ('weak', p_weak), ('indep', p_indep)]:
    h_y, h_y_x, mi = mutual_info_from_joint(p)
    print(f'{name:6s}: H(Y)={h_y:.3f}  H(Y|X)={h_y_x:.3f}  I(X;Y)={mi:.3f}')
```

## Implementation Pitfalls

When computing joint entropy from empirical counts, normalize the count matrix to probabilities and verify it sums to 1 before proceeding. For computing H(Y|X) = sum_x p(x)*H(Y|X=x), handle rows where p_x=0 by skipping them — dividing a row by zero probability creates NaN. Beware that H(Y|X=x0) for a specific value can exceed H(Y): conditioning on a specific outcome is not the same as conditioning on the variable in expectation. For sequence models, track each conditional term H(Xt|X_{<t}) separately to identify which positions are most uncertain, rather than averaging perplexity across all positions.

## Practical Guidance

Use conditional entropy H(Label|Features) to quantify how much residual uncertainty the features leave — lower is better. Compute I(X;Y) = H(Y) - H(Y|X) to measure feature relevance without fitting a model. For LLM debugging, track per-position entropy H(Xt|context) to locate high-uncertainty positions in sequences — these correspond to ambiguous tokens where the model spreads probability mass. When analyzing information flow in a pipeline X -> Y -> Z, measure I(X;Y) and I(Y;Z) separately to localize where information is lost. Residual connections in transformers maintain H(layer output) ~= H(layer input) by keeping each layer nearly invertible.

```python
import numpy as np

def entropy_bits(p):
    p = np.asarray(p, dtype=float)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

def transform_entropy_loss(probs, transform_fn):
    # Compute H(X) and H(f(X)) to measure information loss
    p  = np.array(probs)
    xs = np.arange(len(p))
    ys = np.array([transform_fn(x) for x in xs])
    # aggregate probability mass at each output value
    out_vals = np.unique(ys)
    p_out = np.array([p[ys == v].sum() for v in out_vals])
    return entropy_bits(p), entropy_bits(p_out)

p = [0.25, 0.25, 0.25, 0.25]   # uniform over {0,1,2,3}
h_x, h_id   = transform_entropy_loss(p, lambda x: x)       # identity
h_x, h_mod2 = transform_entropy_loss(p, lambda x: x % 2)  # many-to-one
h_x, h_sq   = transform_entropy_loss(p, lambda x: x*x)    # injective

print(f'H(X)           = {h_x:.3f} bits')
print(f'H(identity(X)) = {h_id:.3f} bits  [no loss, bijection]')
print(f'H(X mod 2)     = {h_mod2:.3f} bits  [info lost, many-to-one]')
print(f'H(X squared)   = {h_sq:.3f} bits  [injective on support, no loss]')
```

> **INFO: Autoregressive Models and the Chain Rule**
> GPT-style models maximize sum_t log p(xt | x1,...,x_{t-1}). By the chain rule, this is exactly log p(x1,...,xT) — the joint log-probability of the sequence. Training cross-entropy is H(p_true, q_model) where the chain rule factors both p_true and q_model identically. Perplexity = exp(average token CE) = exp(H(p,q)) directly estimates the effective branching factor at each step.

| Quantity | Formula | Key Property |
|---|---|---|
| H(X,Y) | E[-log p(X,Y)] | Total uncertainty; always >= max(H(X),H(Y)) |
| H(Y\|X) | H(X,Y) - H(X) | Remaining uncertainty about Y given X |
| Chain rule | H(X,Y) = H(X) + H(Y\|X) | Fundamental decomposition of joint entropy |
| Subadditivity | H(X,Y) <= H(X)+H(Y) | Equality iff X and Y independent |
| Conditioning | H(Y\|X) <= H(Y) | Equality iff X and Y independent |
| Functions | H(f(X)) <= H(X) | Equality iff f invertible on support of X |
| DPI | H(X\|Z) >= H(X\|Y) for X->Y->Z | Processing cannot recover lost information |

---

## Key Takeaways

- H(X,Y) = E[-log p(X,Y)] — joint entropy measures total uncertainty of a pair; always at least as large as each marginal
- H(Y|X) = H(X,Y) - H(X) — conditional entropy is remaining uncertainty about Y after observing X; always non-negative
- Chain rule H(X,Y)=H(X)+H(Y|X) is the foundation of autoregressive LM training and sequence likelihood factorization
- Subadditivity H(X,Y) <= H(X)+H(Y) — the gap I(X;Y) = H(X)+H(Y)-H(X,Y) is the mutual information between variables
- Conditioning reduces entropy in expectation; for a specific outcome x0, H(Y|X=x0) can exceed H(Y)
- H(f(X)) <= H(X) for any deterministic function — information can only be lost or preserved, never created, by processing
- Data processing inequality: for X->Y->Z Markov chain, H(X|Z) >= H(X|Y) — no downstream stage can recover lost information