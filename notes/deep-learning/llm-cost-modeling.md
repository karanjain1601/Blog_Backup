---
title: "LLM Inference Cost Modeling"
slug: "llm-cost-modeling"
description: "Quantitative models for estimating GPU compute, memory bandwidth, and dollar costs for LLM inference, covering FLOP counts, memory-bound vs compute-bound regimes, and per-token pricing."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVW5kZXJzdGFuZGluZyB0aGUgY29zdCBvZiBMTE0gaW5mZXJlbmNlIHJlcXVpcmVzIHJlYXNvbmluZyBhY3Jvc3MgdGhyZWUgZGlzdGluY3QgbGF5ZXJzOiBjb21wdXRlIChGTE9QcyksIG1lbW9yeSBzeXN0ZW0gKGJhbmR3aWR0aCBhbmQgY2FwYWNpdHkpLCBhbmQgZG9sbGFycyAoR1BVIGhvdXJzLCBhbW9ydGl6ZWQgaGFyZHdhcmUpLiBBIG1vZGVsIHRoYXQgYXBwZWFycyBjaGVhcCBvbiBGTE9QcyBtYXkgYmUgZXhwZW5zaXZlIGluIHByYWN0aWNlIGJlY2F1c2UgZGVjb2RlIGlzIG1lbW9yeS1iYW5kd2lkdGggYm91bmQsIG5vdCBjb21wdXRlIGJvdW5kIOKAlCBtb3N0IG9mIHRoZSBHUFVcdTAwMjdzIFRGTE9QUyBhcmUgaWRsZSB3aGlsZSB3YWl0aW5nIGZvciB3ZWlnaHRzIHRvIHN0cmVhbSBmcm9tIEhCTS4gQ29udmVyc2VseSwgYSBtb2RlbCB0aGF0IHNlZW1zIGhhcmR3YXJlLWludGVuc2l2ZSBtYXkgYmUgc3VycHJpc2luZ2x5IGNoZWFwIHdoZW4gYmF0Y2hlZCBiZWNhdXNlIGJhbmR3aWR0aCBpcyBhbW9ydGl6ZWQgYWNyb3NzIGJhdGNoIGVsZW1lbnRzLiBUaGlzIG5vdGUgZGV2ZWxvcHMgcXVhbnRpdGF0aXZlIG1vZGVscyBmb3IgZWFjaCBsYXllciwgZGVyaXZlcyB0aGUgcm9vZmxpbmUgY3Jvc3NvdmVyIGJhdGNoIHNpemUgdGhhdCBzZXBhcmF0ZXMgdGhlIG1lbW9yeS1ib3VuZCBhbmQgY29tcHV0ZS1ib3VuZCByZWdpbWVzLCBhbmQgdHJhbnNsYXRlcyBoYXJkd2FyZSB1dGlsaXNhdGlvbiBpbnRvIGRvbGxhcnMgcGVyIG1pbGxpb24gdG9rZW5zIGFjcm9zcyBjbG91ZCBBUEksIGNsb3VkIHNlbGYtaG9zdGVkIEdQVSwgYW5kIG9uLXByZW1pc2UgZGVwbG95bWVudCBvcHRpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMTE0gaW5mZXJlbmNlIGhhcyB0d28gZGlzdGluY3QgcGhhc2VzIHdpdGggZGlmZmVyZW50IGNvc3QgcHJvZmlsZXMuIFByZWZpbGwgKGFsc28gY2FsbGVkIGVuY29kaW5nIG9yIHRoZSBwcm9tcHQgcHJvY2Vzc2luZyBwaGFzZSkgcHJvY2Vzc2VzIGFsbCBpbnB1dCB0b2tlbnMgaW4gcGFyYWxsZWwgdXNpbmcgbWF0cml4IG11bHRpcGxpY2F0aW9ucyB0aGF0IGFyZSBjb21wdXRlLWJvdW5kOiBhcml0aG1ldGljIGludGVuc2l0eSBpcyBoaWdoIGJlY2F1c2UgZWFjaCB3ZWlnaHQgYnl0ZSBpcyByZXVzZWQgYWNyb3NzIGFsbCBpbnB1dCB0b2tlbnMgc2ltdWx0YW5lb3VzbHkuIERlY29kZSBnZW5lcmF0ZXMgb25lIG5ldyB0b2tlbiBwZXIgc3RlcCB1c2luZyBtYXRyaXgtdmVjdG9yIG11bHRpcGxpY2F0aW9uczogZWFjaCB3ZWlnaHQgaXMgcmVhZCBmcm9tIG1lbW9yeSB0byBjb21wdXRlIGEgc2luZ2xlIG91dHB1dCwgbWFraW5nIGRlY29kZSBtZW1vcnktYmFuZHdpZHRoIGJvdW5kLiBUaGUgcmF0aW8gb2YgY29tcHV0ZSBGTE9QcyB0byBtZW1vcnkgYnl0ZXMgdHJhbnNmZXJyZWQgcGVyIG9wZXJhdGlvbiDigJQgdGhlIGFyaXRobWV0aWMgaW50ZW5zaXR5IOKAlCBkZXRlcm1pbmVzIHdoaWNoIHJlZ2ltZSBhcHBsaWVzLiBGb3IgZGVjb2RlIGF0IGJhdGNoIHNpemUgMSwgYXJpdGhtZXRpYyBpbnRlbnNpdHkgaXMgYXBwcm94aW1hdGVseSAxIEZMT1AvYnl0ZSwgZmFyIGJlbG93IHRoZSByaWRnZSBwb2ludCBvZiBtb2Rlcm4gR1BVcyAodHlwaWNhbGx5IDEwMOKAkzMwMCBGTE9Qcy9ieXRlKSwgbWVhbmluZyB0aGUgR1BVIGlzIGFsbW9zdCBhbHdheXMgbWVtb3J5LWJhbmR3aWR0aCBsaW1pdGVkIGR1cmluZyBkZWNvZGUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRkxPUCBDb3VudGluZyBmb3IgVHJhbnNmb3JtZXIgSW5mZXJlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSB0cmFuc2Zvcm1lciB3aXRoIEwgbGF5ZXJzLCBkX21vZGVsIGhpZGRlbiBkaW1lbnNpb24sIGRfZmYgRkZOIGRpbWVuc2lvbiwgbl9oZWFkcyBhdHRlbnRpb24gaGVhZHMsIGFuZCB2b2NhYnVsYXJ5IHNpemUgViwgdGhlIGRvbWluYW50IEZMT1AgY29zdHMgYXJlIHRoZSBsaW5lYXIgcHJvamVjdGlvbnMuIEVhY2ggbGluZWFyIGxheWVyIG9mIHNoYXBlIChkX2luLCBkX291dCkgY29zdHMgMipCKlMqZF9pbipkX291dCBGTE9QcyBmb3IgYmF0Y2ggc2l6ZSBCIGFuZCBzZXF1ZW5jZSBsZW5ndGggUyAoZmFjdG9yIG9mIDIgZm9yIG11bHRpcGx5LWFjY3VtdWxhdGUpLiBBdHRlbnRpb24gc2NvcmVzIGFkZCAyKkIqbl9oZWFkcypTXjIqKGRfbW9kZWwvbl9oZWFkcykgPSAyKkIqU14yKmRfbW9kZWwgRkxPUHMgcGVyIGxheWVyIGR1cmluZyBwcmVmaWxsLiBEdXJpbmcgZGVjb2RlLCBTX3F1ZXJ5PTEgc28gYXR0ZW50aW9uIG92ZXIgdGhlIEtWIGNhY2hlIGNvc3RzIDIqQipTX2t2KmRfbW9kZWwgcGVyIGxheWVyIOKAlCBsaW5lYXIgaW4gY29udGV4dCBsZW5ndGggcmF0aGVyIHRoYW4gcXVhZHJhdGljLiBUaGUgTE0gaGVhZCBwcm9qZWN0aW9uIChkX21vZGVsIOKGkiB2b2NhYl9zaXplKSBjb250cmlidXRlcyAyKkIqUypkX21vZGVsKnZvY2FiX3NpemUgRkxPUHMsIHdoaWNoIGZvciBsYXJnZSB2b2NhYnVsYXJpZXMgKDMyS+KAkzEyOEsgdG9rZW5zKSBpcyBhIG1hdGVyaWFsIGZyYWN0aW9uIG9mIHRvdGFsIGNvc3QuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBtYXRoXG5mcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcbmZyb20gdHlwaW5nIGltcG9ydCBEaWN0XG5cbkBkYXRhY2xhc3NcbmNsYXNzIFRyYW5zZm9ybWVyQ29uZmlnOlxuICAgIG5fbGF5ZXJzOiBpbnRcbiAgICBuX2hlYWRzOiBpbnRcbiAgICBkX21vZGVsOiBpbnRcbiAgICBkX2ZmOiBpbnRcbiAgICB2b2NhYl9zaXplOiBpbnRcbiAgICBzZXFfbGVuOiBpbnRcbiAgICBiYXRjaF9zaXplOiBpbnQgPSAxXG5cbmRlZiBjb3VudF90cmFuc2Zvcm1lcl9mbG9wcyhjZmc6IFRyYW5zZm9ybWVyQ29uZmlnKSAtXHUwMDNlIERpY3Rbc3RyLCBmbG9hdF06XG4gICAgXCJcIlwiQ291bnQgRkxPUHMgZm9yIG9uZSBwcmVmaWxsIHBhc3MgYW5kIG9uZSBkZWNvZGUgc3RlcC4gUmV0dXJucyBURkxPUHMgLyBHRkxPUHMuXCJcIlwiXG4gICAgQiwgUywgTCA9IGNmZy5iYXRjaF9zaXplLCBjZmcuc2VxX2xlbiwgY2ZnLm5fbGF5ZXJzXG4gICAgRCwgRiwgViA9IGNmZy5kX21vZGVsLCBjZmcuZF9mZiwgY2ZnLnZvY2FiX3NpemVcbiAgICBIID0gY2ZnLm5faGVhZHNcbiAgICAjIFByZWZpbGwgYXR0ZW50aW9uIHBlciBsYXllcjogUUtWIHByb2ogKyBhdHRuIHNjb3JlcyArIGF0dG4gdmFsdWVzICsgb3V0IHByb2pcbiAgICBhdHRuX3FrdiAgID0gMyAqIDIgKiBCICogUyAqIEQgKiBEICAgICAgICAgIyAzIHByb2plY3Rpb25zLCBlYWNoIChCLFMsRClAKEQsRClcbiAgICBhdHRuX3Njb3JlID0gMiAqIEIgKiBIICogUyAqIFMgKiAoRCAvLyBIKSAgIyAoQixILFMsZClAKEIsSCxkLFMpID0gUUteVFxuICAgIGF0dG5fdmFsICAgPSAyICogQiAqIEggKiBTICogUyAqIChEIC8vIEgpICAjIChCLEgsUyxTKUAoQixILFMsZCkgPSBBVlxuICAgIGF0dG5fb3V0ICAgPSAyICogQiAqIFMgKiBEICogRCAgICAgICAgICAgICAjIG91dHB1dCBwcm9qZWN0aW9uXG4gICAgZmZuX2xheWVyICA9IDIgKiAyICogQiAqIFMgKiBEICogRiAgICAgICAgICMgdHdvIGxpbmVhciBsYXllcnMgaW4gRkZOXG4gICAgcHJlZmlsbF9mbG9wcyA9IEwgKiAoYXR0bl9xa3YgKyBhdHRuX3Njb3JlICsgYXR0bl92YWwgKyBhdHRuX291dCArIGZmbl9sYXllcilcbiAgICBwcmVmaWxsX2Zsb3BzICs9IDIgKiBCICogUyAqIEQgKiBWICAgICAgICAgIyBMTSBoZWFkXG4gICAgIyBEZWNvZGUgKFNfcXVlcnk9MSwgS1YgY2FjaGUgbGVuZ3RoID0gUyBmb3IgcHJpb3IgY29udGV4dClcbiAgICBkZWNfcWt2ICAgPSAzICogMiAqIEIgKiAxICogRCAqIERcbiAgICBkZWNfc2NvcmUgPSAyICogQiAqIEggKiAxICogUyAqIChEIC8vIEgpICAjIGF0dGVuZCBvdmVyIEtWIGNhY2hlIGxlbmd0aFxuICAgIGRlY192YWwgICA9IDIgKiBCICogSCAqIDEgKiBTICogKEQgLy8gSClcbiAgICBkZWNfb3V0ICAgPSAyICogQiAqIDEgKiBEICogRFxuICAgIGRlY19mZm4gICA9IDIgKiAyICogQiAqIDEgKiBEICogRlxuICAgIGRlY29kZV9mbG9wcyA9IEwgKiAoZGVjX3FrdiArIGRlY19zY29yZSArIGRlY192YWwgKyBkZWNfb3V0ICsgZGVjX2ZmbilcbiAgICBkZWNvZGVfZmxvcHMgKz0gMiAqIEIgKiAxICogRCAqIFZcbiAgICByZXR1cm4ge1wicHJlZmlsbF9URkxPUHNcIjogcHJlZmlsbF9mbG9wcyAvIDFlMTIsXG4gICAgICAgICAgICBcImRlY29kZV9HRkxPUHNfcGVyX3Rva2VuXCI6IGRlY29kZV9mbG9wcyAvIDFlOX1cblxuY2ZnID0gVHJhbnNmb3JtZXJDb25maWcobl9sYXllcnM9MzIsIG5faGVhZHM9MzIsIGRfbW9kZWw9NDA5NixcbiAgICAgICAgICAgICAgICAgICAgICAgICBkX2ZmPTExMDA4LCB2b2NhYl9zaXplPTMyMDAwLCBzZXFfbGVuPTIwNDgpXG5yID0gY291bnRfdHJhbnNmb3JtZXJfZmxvcHMoY2ZnKVxucHJpbnQoZlwiTGxhbWEtN0IgcHJlZmlsbCB7Y2ZnLnNlcV9sZW59IHRva2Vuczoge3JbXHUwMDI3cHJlZmlsbF9URkxPUHNcdTAwMjddOi4yZn0gVEZMT1BzXCIpXG5wcmludChmXCJMbGFtYS03QiBkZWNvZGUgcGVyIHRva2VuOiAgICAgICB7cltcdTAwMjdkZWNvZGVfR0ZMT1BzX3Blcl90b2tlblx1MDAyN106LjJmfSBHRkxPUHNcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcnkgQmFuZHdpZHRoIEJvdHRsZW5lY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkR1cmluZyBhdXRvcmVncmVzc2l2ZSBkZWNvZGUgYXQgYmF0Y2ggc2l6ZSAxLCBldmVyeSBmb3J3YXJkIHBhc3MgbXVzdCByZWFkIGFsbCBtb2RlbCB3ZWlnaHRzIGZyb20gR1BVIEhCTSB0byBjb21wdXRlIGEgc2luZ2xlIG91dHB1dCB0b2tlbi4gRm9yIGEgN0IgcGFyYW1ldGVyIG1vZGVsIGluIGZwMTYsIHRoaXMgaXMgMTQgR0Igb2YgZGF0YSBwZXIgdG9rZW4uIEFuIEExMDAgODBHQiBHUFUgcHJvdmlkZXMgMi4wIFRCL3Mgb2YgSEJNIGJhbmR3aWR0aCwgc28gdGhlIG1pbmltdW0gcG9zc2libGUgZGVjb2RlIGxhdGVuY3kgaXMgMTQgR0IgLyAyMDAwIEdCL3MgPSA3IG1zIHBlciB0b2tlbiwgY29ycmVzcG9uZGluZyB0byBhIG1heGltdW0gb2YgYWJvdXQgMTQzIHRva2Vucy9zZWNvbmQuIFRoaXMgaXMgdGhlIGJhbmR3aWR0aC1ib3VuZCBjZWlsaW5nIOKAlCBhY3R1YWwgdGhyb3VnaHB1dCBpcyBsb3dlciBkdWUgdG8ga2VybmVsIGxhdW5jaCBvdmVyaGVhZCwgYXR0ZW50aW9uIG92ZXIgdGhlIEtWIGNhY2hlLCBhbmQgb3RoZXIgbWVtb3J5IGFjY2Vzc2VzLiBUaGUgS1YgY2FjaGUgYWRkcyAyIChrZXlzICsgdmFsdWVzKSDDlyBuX2xheWVycyDDlyBzZXFfbGVuIMOXIG5faGVhZHMgw5cgaGVhZF9kaW0gw5cgMiBieXRlcyAoZnAxNikgb2YgYWRkaXRpb25hbCBtZW1vcnkgcmVhZCBwZXIgZGVjb2RlIHN0ZXAsIHdoaWNoIGZvciBsb25nIGNvbnRleHQgbGVuZ3RocyBiZWNvbWVzIHNpZ25pZmljYW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcbmZyb20gdHlwaW5nIGltcG9ydCBEaWN0XG5cbiMgUGVhayBIQk0gYmFuZHdpZHRoIGNvbnN0YW50cyAoVEIvcylcbkhXX0JXX1RCczogRGljdFtzdHIsIGZsb2F0XSA9IHtcbiAgICBcIkExMDAtNDBHQlwiOiAgMS41NTUsXG4gICAgXCJBMTAwLTgwR0JcIjogIDIuMDAwLFxuICAgIFwiSDEwMC1TWE1cIjogICAzLjM1MCxcbiAgICBcIkgxMDAtUENJZVwiOiAgMi4wMDAsXG4gICAgXCJSVFgtNDA5MFwiOiAgIDEuMDA4LFxuICAgIFwiUlRYLTMwOTBcIjogICAwLjkzNixcbn1cblxuZGVmIGRlY29kZV9iYW5kd2lkdGhfbW9kZWwoXG4gICAgbl9wYXJhbXM6IGludCxcbiAgICBuX2xheWVyczogaW50LFxuICAgIHNlcV9sZW46IGludCxcbiAgICBuX2hlYWRzOiBpbnQsXG4gICAgaGVhZF9kaW06IGludCxcbiAgICBiYXRjaF9zaXplOiBpbnQgPSAxLFxuICAgIGh3OiBzdHIgPSBcIkExMDAtODBHQlwiLFxuICAgIGR0eXBlX2J5dGVzOiBpbnQgPSAyLCAgICMgZnAxNj0yLCBmcDMyPTQsIGludDg9MVxuKSAtXHUwMDNlIGRpY3Q6XG4gICAgXCJcIlwiRXN0aW1hdGUgYmFuZHdpZHRoLWJvdW5kIGRlY29kZSBsYXRlbmN5IGFuZCBtYXhpbXVtIHRocm91Z2hwdXQuXCJcIlwiXG4gICAgYndfQl9wZXJfcyAgICAgPSBIV19CV19UQnNbaHddICogMWUxMlxuICAgIHdlaWdodF9ieXRlcyAgID0gbl9wYXJhbXMgKiBkdHlwZV9ieXRlc1xuICAgIGt2X2NhY2hlX2J5dGVzID0gMiAqIG5fbGF5ZXJzICogc2VxX2xlbiAqIG5faGVhZHMgKiBoZWFkX2RpbSAqIGR0eXBlX2J5dGVzXG4gICAgdG90YWxfYnl0ZXMgICAgPSAod2VpZ2h0X2J5dGVzICsga3ZfY2FjaGVfYnl0ZXMpICogYmF0Y2hfc2l6ZVxuICAgIG1pbl9sYXRlbmN5X21zID0gKHRvdGFsX2J5dGVzIC8gYndfQl9wZXJfcykgKiAxZTNcbiAgICBtYXhfdGhyb3VnaHB1dCA9IGJhdGNoX3NpemUgLyAobWluX2xhdGVuY3lfbXMgLyAxZTMpXG4gICAgcHJpbnQoZlwiW3tod31dIE1vZGVsOiB7bl9wYXJhbXMvMWU5Oi4xZn1CIHBhcmFtcyB8IFwiXG4gICAgICAgICAgZlwiS1Y6IHtrdl9jYWNoZV9ieXRlcy8xZTk6LjJmfSBHQiB8IGJzPXtiYXRjaF9zaXplfVwiKVxuICAgIHByaW50KGZcIiAgTWluIGRlY29kZSBsYXRlbmN5IChidy1ib3VuZCk6IHttaW5fbGF0ZW5jeV9tczouMWZ9IG1zL3Rva1wiKVxuICAgIHByaW50KGZcIiAgTWF4IHRocm91Z2hwdXQ6ICAgICAgICAgICAgICAgIHttYXhfdGhyb3VnaHB1dDouMGZ9IHRvay9zXCIpXG4gICAgcmV0dXJuIHtcIm1pbl9sYXRlbmN5X21zXCI6IG1pbl9sYXRlbmN5X21zLCBcIm1heF90aHJvdWdocHV0XCI6IG1heF90aHJvdWdocHV0fVxuXG4jIExsYW1hLTdCIGF0IHNlcV9sZW49MjA0OCwgZnAxNlxuZGVjb2RlX2JhbmR3aWR0aF9tb2RlbChcbiAgICBuX3BhcmFtcz03XzAwMF8wMDBfMDAwLCBuX2xheWVycz0zMiwgc2VxX2xlbj0yMDQ4LFxuICAgIG5faGVhZHM9MzIsIGhlYWRfZGltPTEyOCwgYmF0Y2hfc2l6ZT0xLCBodz1cIkExMDAtODBHQlwiXG4pIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXJpdGhtZXRpYyBJbnRlbnNpdHkgYW5kIFJvb2ZsaW5lIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBcml0aG1ldGljIGludGVuc2l0eSAoQUkpIGlzIHRoZSByYXRpbyBvZiBGTE9QcyBwZXJmb3JtZWQgdG8gYnl0ZXMgdHJhbnNmZXJyZWQgZnJvbSBtZW1vcnk6IEFJID0gRkxPUHMgLyBieXRlcy4gRm9yIGEgbGluZWFyIGxheWVyIG9mIHNoYXBlIChkX2luLCBkX291dCkgcHJvY2Vzc2luZyBhIGJhdGNoIG9mIEIgdG9rZW5zOiBGTE9QcyA9IDIqQipkX2luKmRfb3V0LCBieXRlcyA9IChkX2luKmRfb3V0ICsgQipkX2luICsgQipkX291dCkgKiBkdHlwZV9ieXRlcyDiiYggZF9pbipkX291dCAqIGR0eXBlX2J5dGVzIGZvciBzbWFsbCBCLiBUaHVzIEFJIOKJiCAyKkIgLyBkdHlwZV9ieXRlcywgd2hpY2ggZm9yIGZwMTYgKGR0eXBlX2J5dGVzPTIpIGdpdmVzIEFJID0gQiBGTE9Qcy9ieXRlLiBUaGUgcm9vZmxpbmUgbW9kZWwgcHJlZGljdHMgYWNoaWV2YWJsZSB0aHJvdWdocHV0IGFzIG1pbihwZWFrX1RGTE9QUywgQUkgKiBwZWFrX2JhbmR3aWR0aF9UQi9zKS4gVGhlIHJpZGdlIHBvaW50IOKAlCB3aGVyZSBjb21wdXRlIGFuZCBiYW5kd2lkdGggYm91bmRzIGludGVyc2VjdCDigJQgb2NjdXJzIGF0IEFJID0gcGVha19URkxPUFMgLyBwZWFrX2JhbmR3aWR0aF9UQi9zLiBGb3IgYW4gQTEwMCAoMzEyIFRGTE9QUyBiZjE2LCAyIFRCL3MpOiByaWRnZSBwb2ludCA9IDMxMiAvIDIgPSAxNTYgRkxPUHMvYnl0ZSwgbWVhbmluZyBkZWNvZGUgaXMgYmFuZHdpZHRoLWJvdW5kIGZvciBiYXRjaCBzaXplcyBiZWxvdyAxNTYgYW5kIGNvbXB1dGUtYm91bmQgYWJvdmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWJcbm1hdHBsb3RsaWIudXNlKFx1MDAyN0FnZ1x1MDAyNylcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBPcHRpb25hbFxuXG5kZWYgcGxvdF9yb29mbGluZShcbiAgICBwZWFrX2Zsb3BzX1RzOiBmbG9hdCA9IDMxMi4wLCAgICAjIEExMDAgYmYxNjogMzEyIFRGTE9QU1xuICAgIGJ3X1RCX3M6IGZsb2F0ID0gMi4wLCAgICAgICAgICAgICMgQTEwMCA4MEdCIGJhbmR3aWR0aFxuICAgIGJhdGNoX3NpemVzOiBPcHRpb25hbFtMaXN0W2ludF1dID0gTm9uZSxcbiAgICBuX3BhcmFtczogZmxvYXQgPSA3ZTksXG4gICAgc2F2ZV9wYXRoOiBzdHIgPSBcInJvb2ZsaW5lX2xsbS5wbmdcIixcbikgLVx1MDAzZSBOb25lOlxuICAgIFwiXCJcIlBsb3Qgcm9vZmxpbmUgbW9kZWwgZm9yIExMTSBkZWNvZGUgYWNyb3NzIGJhdGNoIHNpemVzLlwiXCJcIlxuICAgIGlmIGJhdGNoX3NpemVzIGlzIE5vbmU6XG4gICAgICAgIGJhdGNoX3NpemVzID0gWzEsIDIsIDQsIDgsIDE2LCAzMiwgNjQsIDEyOCwgMjU2XVxuICAgIGJ5dGVzX3Blcl9wYXJhbSA9IDIgICAgICAgICAgICAgICAgICAgICAgICAjIGZwMTZcbiAgICBmbG9wc19wZXJfdG9rZW4gPSAyICogbl9wYXJhbXMgICAgICAgICAgICAgIyB+MiBGTE9QcyBwZXIgcGFyYW1ldGVyIHBlciB0b2tlblxuICAgIGJ3X2J5dGVzX3Blcl9zICA9IGJ3X1RCX3MgKiAxZTEyXG4gICAgcmlkZ2VfYnMgPSBwZWFrX2Zsb3BzX1RzICogMWUxMiAvIChmbG9wc19wZXJfdG9rZW4gLyAobl9wYXJhbXMgKiBieXRlc19wZXJfcGFyYW0pKVxuICAgIHRwdXQgPSBbXVxuICAgIGZvciBicyBpbiBiYXRjaF9zaXplczpcbiAgICAgICAgYWkgPSAoZmxvcHNfcGVyX3Rva2VuICogYnMpIC8gKG5fcGFyYW1zICogYnl0ZXNfcGVyX3BhcmFtKVxuICAgICAgICBhY2hpZXZhYmxlX2Zsb3BzX3MgPSBtaW4ocGVha19mbG9wc19UcyAqIDFlMTIsIGFpICogYndfYnl0ZXNfcGVyX3MpXG4gICAgICAgIHRwdXQuYXBwZW5kKGFjaGlldmFibGVfZmxvcHNfcyAqIGJzIC8gZmxvcHNfcGVyX3Rva2VuKSAgIyB0b2tlbnMvc1xuICAgIHJpZGdlX3BvaW50X2FpID0gcGVha19mbG9wc19UcyAvIGJ3X1RCX3NcbiAgICBwcmludChmXCJSaWRnZSBwb2ludCBBSToge3JpZGdlX3BvaW50X2FpOi4wZn0gRkxPUHMvYnl0ZVwiKVxuICAgIHByaW50KGZcIkNyb3Nzb3ZlciBiYXRjaCBzaXplIChhcHByb3gpOiB7cmlkZ2VfcG9pbnRfYWk6LjBmfVwiKVxuICAgIGZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oOSwgNSkpXG4gICAgYXguc2VtaWxvZ3goYmF0Y2hfc2l6ZXMsIHRwdXQsIFx1MDAyN2Itb1x1MDAyNywgbGFiZWw9XHUwMDI3RGVjb2RlIHRocm91Z2hwdXQgKHJvb2ZsaW5lKVx1MDAyNylcbiAgICBheC5heHZsaW5lKHJpZGdlX3BvaW50X2FpLCBjb2xvcj1cdTAwMjdyXHUwMDI3LCBsaW5lc3R5bGU9XHUwMDI3LS1cdTAwMjcsIGxhYmVsPWZcdTAwMjdDcm9zc292ZXIgYnM9e3JpZGdlX3BvaW50X2FpOi4wZn1cdTAwMjcpXG4gICAgYXguc2V0X3hsYWJlbChcdTAwMjdCYXRjaCBzaXplXHUwMDI3KTsgYXguc2V0X3lsYWJlbChcdTAwMjdUb2tlbnMgLyBzZWNvbmRcdTAwMjcpXG4gICAgYXguc2V0X3RpdGxlKFx1MDAyN0xMTSBEZWNvZGUgUm9vZmxpbmUg4oCUIEExMDAgODBHQiAoMzEyIFRGTE9QUywgMiBUQi9zKVx1MDAyNylcbiAgICBheC5sZWdlbmQoKTsgYXguZ3JpZChUcnVlLCB3aGljaD1cdTAwMjdib3RoXHUwMDI3KVxuICAgIHBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNhdmVmaWcoc2F2ZV9wYXRoLCBkcGk9MTUwKVxuICAgIHByaW50KGZcIlNhdmVkIHtzYXZlX3BhdGh9XCIpXG5cbnBsb3Rfcm9vZmxpbmUoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvc3QgcGVyIFRva2VuIEZvcm11bGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjb3N0IHBlciB0b2tlbiBmb3Igc2VsZi1ob3N0ZWQgaW5mZXJlbmNlIGlzOiBjb3N0X3Blcl90b2tlbiA9IChHUFVfaG91cmx5X3JhdGUgKyBjYXBleF9wZXJfaG91cikgLyAodG9rZW5zX3Blcl9zZWNvbmQgKiAzNjAwKS4gR1BVIGhvdXJseSByYXRlIGluY2x1ZGVzIGNsb3VkIGluc3RhbmNlIGNvc3Qgb3IsIGZvciBvbi1wcmVtaXNlLCB0aGUgYWxsb2NhdGVkIGVsZWN0cmljaXR5IGFuZCBvcGVyYXRpb25zIGNvc3QgcGVyIEdQVS1ob3VyLiBDYXBleCBwZXIgaG91ciBhbW9ydGlzZXMgdGhlIEdQVSBwdXJjaGFzZSBwcmljZSBvdmVyIGl0cyB1c2VmdWwgbGlmZSAodHlwaWNhbGx5IDLigJMzIHllYXJzIG9mIGNvbnRpbnVvdXMgb3BlcmF0aW9uLCB+MTcsNTAw4oCTMjYsMDAwIGhvdXJzKS4gVG9rZW5zIHBlciBzZWNvbmQgaXMgdGhlIGFjaGlldmVkIGRlY29kZSB0aHJvdWdocHV0IGF0IHRoZSB0YXJnZXQgYmF0Y2ggc2l6ZS4gRm9yIGNsb3VkIEFQSXMsIHByaWNpbmcgaXMgcXVvdGVkIGRpcmVjdGx5IGluIGRvbGxhcnMgcGVyIG1pbGxpb24gaW5wdXQgb3Igb3V0cHV0IHRva2Vucywgc28gdGhlIGZvcm11bGEgc2ltcGxpZmllcyB0byByZWFkaW5nIHRoZSB2ZW5kb3JcdTAwMjdzIHB1Ymxpc2hlZCByYXRlLiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCB0b2tlbnNfcGVyX3NlY29uZCBzY2FsZXMgd2l0aCBiYXRjaCBzaXplICh1bnRpbCB0aGUgY29tcHV0ZS1ib3VuZCByZWdpbWUpLCBzbyBoaWdoZXIgYmF0Y2ggc2l6ZXMgZHJhbWF0aWNhbGx5IHJlZHVjZSBjb3N0IHBlciB0b2tlbiDigJQgYnV0IG9ubHkgaWYgdGhlIHdvcmtsb2FkIGNhbiB0b2xlcmF0ZSB0aGUgcXVldWluZyBsYXRlbmN5LiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJCYXRjaCBTaXplIGFzIENvc3QgTGV2ZXIiLCJjb250ZW50IjoiRm9yIGRlY29kZS1ib3VuZCB3b3JrbG9hZHMsIGJhdGNoIHNpemUgaXMgdGhlIG1haW4gbGV2ZXI6IGRvdWJsaW5nIGJhdGNoIHNpemUgcm91Z2hseSBoYWx2ZXMgY29zdC1wZXItdG9rZW4gdW50aWwgeW91IGhpdCB0aGUgY29tcHV0ZS1ib3VuZCByZWdpbWUg4oCUIHByb2ZpbGUgeW91ciB0YXJnZXQgYmF0Y2ggc2l6ZSBiZWZvcmUgaW52ZXN0aW5nIGluIGhhcmR3YXJlIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gZGF0YWNsYXNzZXMgaW1wb3J0IGRhdGFjbGFzcywgZmllbGRcbmZyb20gdHlwaW5nIGltcG9ydCBEaWN0LCBPcHRpb25hbFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBEZXBsb3ltZW50T3B0aW9uOlxuICAgIG5hbWU6IHN0clxuICAgIGhvdXJseV91c2Q6IGZsb2F0ICAgICAgICAgICAjIGNsb3VkIGluc3RhbmNlIG9yIGVsZWN0cmljaXR5K29wcyBjb3N0IHBlciBHUFUtaG91clxuICAgIHRva2Vuc19wZXJfc2VjOiBmbG9hdCAgICAgICAjIGFjaGlldmVkIGRlY29kZSB0aHJvdWdocHV0XG4gICAgY2FwZXhfdXNkOiBmbG9hdCA9IDAuMCAgICAgICMgaGFyZHdhcmUgcHVyY2hhc2UgcHJpY2UgKDAgZm9yIGNsb3VkKVxuICAgIGxpZmVzcGFuX2hvdXJzOiBmbG9hdCA9IDE3NTIwLjAgICMgMiB5ZWFycyBjb250aW51b3VzXG5cbmRlZiBjb3N0X3Blcl9taWxsaW9uX3Rva2VucyhvcHQ6IERlcGxveW1lbnRPcHRpb24pIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiQ29tcHV0ZSBpbmZyYXN0cnVjdHVyZSBjb3N0IHBlciAxTSBvdXRwdXQgdG9rZW5zIGluY2x1ZGluZyBhbW9ydGl6ZWQgY2FwZXguXCJcIlwiXG4gICAgY2FwZXhfcGVyX2hvdXIgICA9IG9wdC5jYXBleF91c2QgLyBvcHQubGlmZXNwYW5faG91cnNcbiAgICB0b3RhbF9ob3VybHkgICAgID0gb3B0LmhvdXJseV91c2QgKyBjYXBleF9wZXJfaG91clxuICAgIHRva2Vuc19wZXJfaG91ciAgPSBvcHQudG9rZW5zX3Blcl9zZWMgKiAzNjAwXG4gICAgcmV0dXJuICh0b3RhbF9ob3VybHkgLyB0b2tlbnNfcGVyX2hvdXIpICogMV8wMDBfMDAwXG5cbkFQSV9SQVRFU19VU0RfUEVSXzFNID0ge1wiR1BULTRvIEFQSVwiOiAxMC4wMCwgXCJHUFQtMy41IEFQSVwiOiAwLjUwfVxuXG5vcHRpb25zOiBEaWN0W3N0ciwgRGVwbG95bWVudE9wdGlvbl0gPSB7XG4gICAgXCJHUFQtNG8gQVBJXCI6ICAgIERlcGxveW1lbnRPcHRpb24oXCJHUFQtNG8gQVBJXCIsICAgIDAuMCwgICA1MC4wKSxcbiAgICBcIkdQVC0zLjUgQVBJXCI6ICAgRGVwbG95bWVudE9wdGlvbihcIkdQVC0zLjUgQVBJXCIsICAgMC4wLCAgMjAwLjApLFxuICAgIFwiQTEwMCBjbG91ZCAxeFwiOiBEZXBsb3ltZW50T3B0aW9uKFwiQTEwMCAxeCBjbG91ZFwiLCAzLjUwLCAxMjAwLjApLFxuICAgIFwiQTEwMCBjbG91ZCA4eFwiOiBEZXBsb3ltZW50T3B0aW9uKFwiQTEwMCA4eCBjbG91ZFwiLDI0LjAwLCA5NjAwLjApLFxuICAgIFwiSDEwMCBjbG91ZCAxeFwiOiBEZXBsb3ltZW50T3B0aW9uKFwiSDEwMCAxeCBjbG91ZFwiLCA1LjAwLCAyODAwLjApLFxuICAgIFwiT24tcHJlbSBBMTAwXCI6ICBEZXBsb3ltZW50T3B0aW9uKFwiT24tcHJlbSBBMTAwXCIsICAwLjQwLCAxMjAwLjAsIGNhcGV4X3VzZD0xMl8wMDAuMCksXG59XG5cbnByaW50KGZcIntcdTAwMjdPcHRpb25cdTAwMjc6XHUwMDNjMjJ9IHtcdTAwMjdDb3N0LzFNIHRva1x1MDAyNzpcdTAwM2UxMn0gIHtcdTAwMjdUb2svc1x1MDAyNzpcdTAwM2U4fVwiKVxucHJpbnQoXCItXCIgKiA0OClcbmZvciBuYW1lLCBvcHQgaW4gb3B0aW9ucy5pdGVtcygpOlxuICAgIGNvc3QgPSBBUElfUkFURVNfVVNEX1BFUl8xTS5nZXQobmFtZSwgY29zdF9wZXJfbWlsbGlvbl90b2tlbnMob3B0KSlcbiAgICBwcmludChmXCJ7bmFtZTpcdTAwM2MyMn0gICR7Y29zdDpcdTAwM2UxMC4yZn0gIHtvcHQudG9rZW5zX3Blcl9zZWM6XHUwMDNlNy4wZn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDbG91ZCB2cyBPbi1wcmVtaXNlIENvc3QgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2xvdWQgQVBJIHByaWNpbmcgaXMgY29udmVuaWVudCBidXQgZXhwZW5zaXZlIGF0IHNjYWxlOiBHUFQtNG8gYXQgJDEwLzFNIG91dHB1dCB0b2tlbnMgY29zdHMgNTDigJMxMDDDlyBtb3JlIHRoYW4gc2VsZi1ob3N0aW5nIGFuIGVxdWl2YWxlbnQgb3Blbi13ZWlnaHQgbW9kZWwgb24gYSBjbG91ZCBBMTAwIGluc3RhbmNlLiBIb3dldmVyLCBjbG91ZCBBUElzIGVsaW1pbmF0ZSBvcGVyYXRpb25hbCBvdmVyaGVhZCwgcHJvdmlkZSBtYW5hZ2VkIHJlbGlhYmlsaXR5LCBhbmQgcmVxdWlyZSBubyBtaW5pbXVtIGNvbW1pdHRlZCBzcGVuZCDigJQgbWFraW5nIHRoZW0gY29zdC1lZmZlY3RpdmUgZm9yIGxvdy12b2x1bWUgdXNlIGNhc2VzIGJlbG93IHJvdWdobHkgMTAwTSB0b2tlbnMgcGVyIG1vbnRoLiBBYm92ZSB0aGF0IHRocmVzaG9sZCwgc2VsZi1ob3N0aW5nIG9uIGNsb3VkIEdQVXMgKEExMDAgb3IgSDEwMCBpbnN0YW5jZXMpIHR5cGljYWxseSByZWR1Y2VzIGNvc3QgYnkgMTDigJMzMMOXIHBlciB0b2tlbi4gT24tcHJlbWlzZSBkZXBsb3ltZW50IGZ1cnRoZXIgcmVkdWNlcyBjb3N0IGJ5IDLigJMzw5cgdmVyc3VzIGNsb3VkIEdQVSBpbnN0YW5jZXMgYnkgZWxpbWluYXRpbmcgdGhlIGNsb3VkIG1hcmdpbiwgYnV0IHJlcXVpcmVzIGNhcGl0YWwgZXhwZW5kaXR1cmUsIGhhcmR3YXJlIG9wZXJhdGlvbnMgY2FwYWNpdHksIGFuZCBzdWZmaWNpZW50IHZvbHVtZSB0byBrZWVwIEdQVXMgaGlnaGx5IHV0aWxpc2VkICh0YXJnZXQgXHUwMDNlNzAlIEdQVSB1dGlsaXNhdGlvbiB0byBqdXN0aWZ5IG9uLXByZW0gY2FwZXgpLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJEZXBsb3ltZW50IG9wdGlvbiIsIkNvc3QgLyAxTSB0b2tlbnMiLCJMYXRlbmN5IHA1MCIsIk1heCB0aHJvdWdocHV0IiwiU2V0dXAgY29tcGxleGl0eSJdLCJyb3dzIjpbWyJHUFQtNG8gQVBJIiwiJDEwLjAwIiwiODAw4oCTMTUwMCBtcyAoVFRGVCkiLCJVbmxpbWl0ZWQgKG1hbmFnZWQpIiwiTm9uZSDigJQgQVBJIGtleSBvbmx5Il0sWyJHUFQtMy41IEFQSSIsIiQwLjUwIiwiMzAw4oCTNjAwIG1zIChUVEZUKSIsIlVubGltaXRlZCAobWFuYWdlZCkiLCJOb25lIOKAlCBBUEkga2V5IG9ubHkiXSxbIkExMDAgY2xvdWQgMcOXIiwiJDAuODEiLCI1MOKAkzEyMCBtcyIsIjEsMjAwIHRvay9zIChMbGFtYS03QikiLCJNZWRpdW0g4oCUIGluZnJhICsgc2VydmluZyBzdGFjayJdLFsiQTEwMCBjbG91ZCA4w5ciLCIkMC42OSIsIjMw4oCTODAgbXMiLCI5LDYwMCB0b2svcyAoTGxhbWEtN0IpIiwiSGlnaCDigJQgbXVsdGktR1BVIHNlcnZpbmciXSxbIkgxMDAgY2xvdWQgMcOXIiwiJDAuNTAiLCIzMOKAkzcwIG1zIiwiMiw4MDAgdG9rL3MgKExsYW1hLTdCKSIsIk1lZGl1bSDigJQgaW5mcmEgKyBzZXJ2aW5nIHN0YWNrIl0sWyJPbi1wcmVtIEExMDAiLCIkMC4yOCIsIjUw4oCTMTIwIG1zIiwiMSwyMDAgdG9rL3MgKExsYW1hLTdCKSIsIkhpZ2gg4oCUIGhhcmR3YXJlICsgb3BzIHRlYW0iXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9wdGltaXppbmcgZm9yIENvc3QgRWZmaWNpZW5jeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGhpZ2hlc3QtaW1wYWN0IGNvc3QgcmVkdWN0aW9uIGxldmVycywgaW4gcm91Z2ggb3JkZXIgb2YgaW1wYWN0LCBhcmU6ICgxKSBRdWFudGlzYXRpb24g4oCUIG1vdmluZyBmcm9tIGZwMTYgdG8gaW50OCBvciBpbnQ0IGhhbHZlcyBvciBxdWFydGVycyB0aGUgd2VpZ2h0IGJ5dGVzIHJlYWQgcGVyIGRlY29kZSBzdGVwLCBkaXJlY3RseSBzY2FsaW5nIG1lbW9yeS1iYW5kd2lkdGgtYm91bmQgdGhyb3VnaHB1dCBieSAy4oCTNMOXIGF0IG1pbmltYWwgcXVhbGl0eSBsb3NzIGZvciBtb3N0IG1vZGVscy4gKDIpIEJhdGNoIHNpemUg4oCUIGFzIHNob3duIGJ5IHRoZSByb29mbGluZSBtb2RlbCwgaW5jcmVhc2luZyBiYXRjaCBzaXplIGFtb3J0aXNlcyB3ZWlnaHQgcmVhZHMgYWNyb3NzIG1vcmUgb3V0cHV0IHRva2VucyBzaW11bHRhbmVvdXNseS4gKDMpIFNwZWN1bGF0aXZlIGRlY29kaW5nIOKAlCBNZWR1c2Egb3IgZHJhZnQtbW9kZWwgYXBwcm9hY2hlcyBhY2hpZXZlIDLigJMzw5cgdGhyb3VnaHB1dCBpbXByb3ZlbWVudCB3aXRoIG5vIGFkZGl0aW9uYWwgR1BVIG1lbW9yeS4gKDQpIEtWIGNhY2hlIGNvbXByZXNzaW9uIOKAlCByZWR1Y2luZyBLViBjYWNoZSBzaXplIHZpYSBncm91cGVkLXF1ZXJ5IGF0dGVudGlvbiAoR1FBKSwgbXVsdGktcXVlcnkgYXR0ZW50aW9uIChNUUEpLCBvciBxdWFudGlzZWQgS1YgY2FjaGUgZnJlZXMgbWVtb3J5IGZvciBsYXJnZXIgYmF0Y2ggc2l6ZXMuICg1KSBNb2RlbCBzZWxlY3Rpb24g4oCUIGEgc21hbGxlciBtb2RlbCBhdCBoaWdoZXIgYmF0Y2ggc2l6ZSBvZnRlbiBjb3N0cyBsZXNzIHBlciB0b2tlbiB0aGFuIGEgbGFyZ2VyIG1vZGVsIGF0IGxvdyBiYXRjaCBzaXplIHdoaWxlIG1haW50YWluaW5nIGFjY2VwdGFibGUgcXVhbGl0eS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlF1YW50aXNhdGlvbiAoaW50OC9pbnQ0KSBpcyB0aGUgc2luZ2xlIGhpZ2hlc3QtbGV2ZXJhZ2UgY29zdCByZWR1Y3Rpb246IGhhbHZpbmcgd2VpZ2h0IGJ5dGVzIGRvdWJsZXMgYmFuZHdpZHRoLWJvdW5kIHRocm91Z2hwdXQgYXQgbWluaW1hbCBxdWFsaXR5IGNvc3QuIiwiVGhlIHJvb2ZsaW5lIGNyb3Nzb3ZlciBiYXRjaCBzaXplIGZvciBhbiBBMTAwICgzMTIgVEZMT1BTLCAyIFRCL3MpIGlzIGFwcHJveGltYXRlbHkgMTU2IOKAlCBiZWxvdyB0aGlzLCBHUFUgaXMgbWVtb3J5LWJvdW5kOyBhYm92ZSwgY29tcHV0ZS1ib3VuZC4iLCJLViBjYWNoZSBpcyBhIHNpZ25pZmljYW50IG1lbW9yeSBjb25zdW1lcjogYXQgc2VxX2xlbj04SyB3aXRoIExsYW1hLTdCIGluIGZwMTYsIEtWIGNhY2hlIHBlciByZXF1ZXN0IGlzIDIgR0Ig4oCUIGxhcmdlciB0aGFuIG1hbnkgc21hbGxlciBtb2RlbHMgZW50aXJlbHkuIiwiR1FBIChncm91cGVkLXF1ZXJ5IGF0dGVudGlvbikgcmVkdWNlcyBLViBjYWNoZSBieSBuX2hlYWRzL25fa3ZfaGVhZHMgZmFjdG9yOyBMbGFtYS0zIHVzZXMgR1FBIHdpdGggOCBLViBoZWFkcyB2cyAzMiBxdWVyeSBoZWFkcyDigJQgNMOXIEtWIG1lbW9yeSByZWR1Y3Rpb24uIiwiRmxhc2ggQXR0ZW50aW9uIHJlZHVjZXMgbWVtb3J5IHRyYWZmaWMgZm9yIGF0dGVudGlvbiBmcm9tIE8oU14yKSB0byBPKFMpIGJ5dGVzLCBlbGltaW5hdGluZyBwcmVmaWxsIGJvdHRsZW5lY2tzIGZvciBsb25nIGNvbnRleHRzLiIsIkNvc3QgcGVyIHRva2VuIHNjYWxlcyBpbnZlcnNlbHkgd2l0aCBHUFUgdXRpbGlzYXRpb24g4oCUIHRhcmdldCBcdTAwM2U3MCUgdXRpbGlzYXRpb247IGJlbG93IDUwJSBpbmRpY2F0ZXMgb3Zlci1wcm92aXNpb25lZCBvciB1bmRlci1iYXRjaGVkIGRlcGxveW1lbnQuIiwiQ29udGludW91cyBiYXRjaGluZyAoaXRlcmF0aW9uLWxldmVsIHNjaGVkdWxpbmcpIGluY3JlYXNlcyBlZmZlY3RpdmUgR1BVIHV0aWxpc2F0aW9uIGZyb20gMzDigJM0MCUgKHN0YXRpYyBiYXRjaGluZykgdG8gNjDigJM4MCUgaW4gdHlwaWNhbCBjaGF0IHdvcmtsb2Fkcy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTExNIGluZmVyZW5jZSBjb3N0IGlzIGRvbWluYXRlZCBieSB0aGUgbWVtb3J5IGJhbmR3aWR0aCBib3R0bGVuZWNrIGR1cmluZyBhdXRvcmVncmVzc2l2ZSBkZWNvZGUuIEF0IGJhdGNoIHNpemUgMSwgbW9kZXJuIEdQVSBjb21wdXRlIHVuaXRzIGFyZSB1dGlsaXNlZCBhdCBsZXNzIHRoYW4gMSUgb2YgdGhlaXIgcGVhayBGTE9QUyBiZWNhdXNlIHRoZSBib3R0bGVuZWNrIGlzIHN0cmVhbWluZyB3ZWlnaHRzIGZyb20gSEJNLiBUaGUgcHJhY3RpY2FsIGNvbnNlcXVlbmNlIGlzIHRoYXQgb3B0aW1pc2F0aW9ucyB0YXJnZXRpbmcgbWVtb3J5IOKAlCBxdWFudGlzYXRpb24sIEdRQSwgS1YgY2FjaGUgY29tcHJlc3Npb24sIHNwZWN1bGF0aXZlIGRlY29kaW5nIOKAlCBkZWxpdmVyIGxhcmdlciBjb3N0IHJlZHVjdGlvbnMgdGhhbiBvcHRpbWlzYXRpb25zIHRhcmdldGluZyBjb21wdXRlLiBGb3IgY29zdCBtb2RlbGxpbmcsIHRoZSB0aHJlZS1sYXllciBmcmFtZXdvcmsgKEZMT1BzIOKGkiBiYW5kd2lkdGgg4oaSIGRvbGxhcnMpIHByb3ZpZGVzIGEgcHJpbmNpcGxlZCBtZXRob2RvbG9neTogY291bnQgRkxPUHMgdG8gdW5kZXJzdGFuZCBtb2RlbCBjb21wbGV4aXR5LCBhcHBseSB0aGUgcm9vZmxpbmUgdG8gZmluZCB0aGUgb3BlcmF0aW5nIHJlZ2ltZSwgdGhlbiB0cmFuc2xhdGUgdG8gZG9sbGFycyB1c2luZyBvYnNlcnZlZCB0aHJvdWdocHV0IGFuZCBHUFUgcHJpY2luZy4gQWx3YXlzIHByb2ZpbGUgYXQgeW91ciB0YXJnZXQgYmF0Y2ggc2l6ZSDigJQgcm9vZmxpbmUgcHJlZGljdGlvbnMgY2FuIGRpZmZlciBmcm9tIG1lYXN1cmVkIHRocm91Z2hwdXQgYnkgMjDigJM0MCUgZHVlIHRvIGtlcm5lbCBvdmVyaGVhZHMsIG1lbW9yeSBmcmFnbWVudGF0aW9uLCBhbmQgYXR0ZW50aW9uIGNvc3RzIG5vdCBjYXB0dXJlZCBpbiBzaW1wbGlmaWVkIG1vZGVscy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkRlY29kZSBpcyBhbG1vc3QgYWx3YXlzIG1lbW9yeS1iYW5kd2lkdGggYm91bmQgYXQgYmF0Y2ggc2l6ZSAxOiBhcml0aG1ldGljIGludGVuc2l0eSDiiYggMSBGTE9QL2J5dGUgdmVyc3VzIHJpZGdlIHBvaW50cyBvZiAxMDDigJMzMDAgRkxPUC9ieXRlIG9uIG1vZGVybiBHUFVzLiIsIlByZWZpbGwgaXMgY29tcHV0ZS1ib3VuZCBmb3IgbG9uZyBzZXF1ZW5jZXM6IGFyaXRobWV0aWMgaW50ZW5zaXR5IHNjYWxlcyB3aXRoIHNlcXVlbmNlIGxlbmd0aCBTLCByZWFjaGluZyB0aGUgcmlkZ2UgcG9pbnQgYXJvdW5kIFM9MTAw4oCTMzAwIHRva2Vucy4iLCJUaGUgY29zdCBjcm9zc292ZXIgYmV0d2VlbiBjbG91ZCBBUEkgYW5kIHNlbGYtaG9zdGVkIEExMDAgb2NjdXJzIGF0IHJvdWdobHkgNTDigJMxNTBNIG91dHB1dCB0b2tlbnMgcGVyIG1vbnRoIGRlcGVuZGluZyBvbiBtb2RlbCBzaXplLiIsImludDggcXVhbnRpc2F0aW9uIHJlZHVjZXMgY29zdCBieSB+MsOXIHdpdGggbGVzcyB0aGFuIDElIHF1YWxpdHkgZGVncmFkYXRpb24gb24gbW9zdCBiZW5jaG1hcmtzOyBpbnQ0IHJlZHVjZXMgYnkgfjTDlyB3aXRoIDLigJM1JSBkZWdyYWRhdGlvbi4iLCJHUFUgdXRpbGlzYXRpb24gaXMgdGhlIGhpZGRlbiBlZmZpY2llbmN5IG11bHRpcGxpZXI6IGEgNTAlLXV0aWxpc2VkIEExMDAgY29zdHMgMsOXIHBlciB0b2tlbiB2ZXJzdXMgYSBmdWxseSB1dGlsaXNlZCBvbmUuIiwiRm9yIGxhdGVuY3ktc2Vuc2l0aXZlIHdvcmtsb2Fkcywgc3BlY3VsYXRpdmUgZGVjb2RpbmcgKE1lZHVzYSkgaXMgdGhlIG1vc3QgcHJhY3RpY2FsIDLigJMzw5cgc3BlZWR1cCB3aXRoIG5vIGFkZGl0aW9uYWwgaW5mcmFzdHJ1Y3R1cmUuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# LLM Inference Cost Modeling

Understanding the cost of LLM inference requires reasoning across three distinct layers: compute (FLOPs), memory system (bandwidth and capacity), and dollars (GPU hours, amortized hardware). A model that appears cheap on FLOPs may be expensive in practice because decode is memory-bandwidth bound, not compute bound — most of the GPU's TFLOPS are idle while waiting for weights to stream from HBM. Conversely, a model that seems hardware-intensive may be surprisingly cheap when batched because bandwidth is amortized across batch elements. This note develops quantitative models for each layer, derives the roofline crossover batch size that separates the memory-bound and compute-bound regimes, and translates hardware utilisation into dollars per million tokens across cloud API, cloud self-hosted GPU, and on-premise deployment options.

## Overview

LLM inference has two distinct phases with different cost profiles. Prefill (also called encoding or the prompt processing phase) processes all input tokens in parallel using matrix multiplications that are compute-bound: arithmetic intensity is high because each weight byte is reused across all input tokens simultaneously. Decode generates one new token per step using matrix-vector multiplications: each weight is read from memory to compute a single output, making decode memory-bandwidth bound. The ratio of compute FLOPs to memory bytes transferred per operation — the arithmetic intensity — determines which regime applies. For decode at batch size 1, arithmetic intensity is approximately 1 FLOP/byte, far below the ridge point of modern GPUs (typically 100–300 FLOPs/byte), meaning the GPU is almost always memory-bandwidth limited during decode.

## FLOP Counting for Transformer Inference

For a transformer with L layers, d_model hidden dimension, d_ff FFN dimension, n_heads attention heads, and vocabulary size V, the dominant FLOP costs are the linear projections. Each linear layer of shape (d_in, d_out) costs 2*B*S*d_in*d_out FLOPs for batch size B and sequence length S (factor of 2 for multiply-accumulate). Attention scores add 2*B*n_heads*S^2*(d_model/n_heads) = 2*B*S^2*d_model FLOPs per layer during prefill. During decode, S_query=1 so attention over the KV cache costs 2*B*S_kv*d_model per layer — linear in context length rather than quadratic. The LM head projection (d_model → vocab_size) contributes 2*B*S*d_model*vocab_size FLOPs, which for large vocabularies (32K–128K tokens) is a material fraction of total cost.

```python
import math
from dataclasses import dataclass
from typing import Dict

@dataclass
class TransformerConfig:
    n_layers: int
    n_heads: int
    d_model: int
    d_ff: int
    vocab_size: int
    seq_len: int
    batch_size: int = 1

def count_transformer_flops(cfg: TransformerConfig) -> Dict[str, float]:
    """Count FLOPs for one prefill pass and one decode step. Returns TFLOPs / GFLOPs."""
    B, S, L = cfg.batch_size, cfg.seq_len, cfg.n_layers
    D, F, V = cfg.d_model, cfg.d_ff, cfg.vocab_size
    H = cfg.n_heads
    # Prefill attention per layer: QKV proj + attn scores + attn values + out proj
    attn_qkv   = 3 * 2 * B * S * D * D         # 3 projections, each (B,S,D)@(D,D)
    attn_score = 2 * B * H * S * S * (D // H)  # (B,H,S,d)@(B,H,d,S) = QK^T
    attn_val   = 2 * B * H * S * S * (D // H)  # (B,H,S,S)@(B,H,S,d) = AV
    attn_out   = 2 * B * S * D * D             # output projection
    ffn_layer  = 2 * 2 * B * S * D * F         # two linear layers in FFN
    prefill_flops = L * (attn_qkv + attn_score + attn_val + attn_out + ffn_layer)
    prefill_flops += 2 * B * S * D * V         # LM head
    # Decode (S_query=1, KV cache length = S for prior context)
    dec_qkv   = 3 * 2 * B * 1 * D * D
    dec_score = 2 * B * H * 1 * S * (D // H)  # attend over KV cache length
    dec_val   = 2 * B * H * 1 * S * (D // H)
    dec_out   = 2 * B * 1 * D * D
    dec_ffn   = 2 * 2 * B * 1 * D * F
    decode_flops = L * (dec_qkv + dec_score + dec_val + dec_out + dec_ffn)
    decode_flops += 2 * B * 1 * D * V
    return {"prefill_TFLOPs": prefill_flops / 1e12,
            "decode_GFLOPs_per_token": decode_flops / 1e9}

cfg = TransformerConfig(n_layers=32, n_heads=32, d_model=4096,
                         d_ff=11008, vocab_size=32000, seq_len=2048)
r = count_transformer_flops(cfg)
print(f"Llama-7B prefill {cfg.seq_len} tokens: {r['prefill_TFLOPs']:.2f} TFLOPs")
print(f"Llama-7B decode per token:       {r['decode_GFLOPs_per_token']:.2f} GFLOPs")
```

## Memory Bandwidth Bottleneck

During autoregressive decode at batch size 1, every forward pass must read all model weights from GPU HBM to compute a single output token. For a 7B parameter model in fp16, this is 14 GB of data per token. An A100 80GB GPU provides 2.0 TB/s of HBM bandwidth, so the minimum possible decode latency is 14 GB / 2000 GB/s = 7 ms per token, corresponding to a maximum of about 143 tokens/second. This is the bandwidth-bound ceiling — actual throughput is lower due to kernel launch overhead, attention over the KV cache, and other memory accesses. The KV cache adds 2 (keys + values) × n_layers × seq_len × n_heads × head_dim × 2 bytes (fp16) of additional memory read per decode step, which for long context lengths becomes significant.

```python
from dataclasses import dataclass
from typing import Dict

# Peak HBM bandwidth constants (TB/s)
HW_BW_TBs: Dict[str, float] = {
    "A100-40GB":  1.555,
    "A100-80GB":  2.000,
    "H100-SXM":   3.350,
    "H100-PCIe":  2.000,
    "RTX-4090":   1.008,
    "RTX-3090":   0.936,
}

def decode_bandwidth_model(
    n_params: int,
    n_layers: int,
    seq_len: int,
    n_heads: int,
    head_dim: int,
    batch_size: int = 1,
    hw: str = "A100-80GB",
    dtype_bytes: int = 2,   # fp16=2, fp32=4, int8=1
) -> dict:
    """Estimate bandwidth-bound decode latency and maximum throughput."""
    bw_B_per_s     = HW_BW_TBs[hw] * 1e12
    weight_bytes   = n_params * dtype_bytes
    kv_cache_bytes = 2 * n_layers * seq_len * n_heads * head_dim * dtype_bytes
    total_bytes    = (weight_bytes + kv_cache_bytes) * batch_size
    min_latency_ms = (total_bytes / bw_B_per_s) * 1e3
    max_throughput = batch_size / (min_latency_ms / 1e3)
    print(f"[{hw}] Model: {n_params/1e9:.1f}B params | "
          f"KV: {kv_cache_bytes/1e9:.2f} GB | bs={batch_size}")
    print(f"  Min decode latency (bw-bound): {min_latency_ms:.1f} ms/tok")
    print(f"  Max throughput:                {max_throughput:.0f} tok/s")
    return {"min_latency_ms": min_latency_ms, "max_throughput": max_throughput}

# Llama-7B at seq_len=2048, fp16
decode_bandwidth_model(
    n_params=7_000_000_000, n_layers=32, seq_len=2048,
    n_heads=32, head_dim=128, batch_size=1, hw="A100-80GB"
)
```

## Arithmetic Intensity and Roofline

Arithmetic intensity (AI) is the ratio of FLOPs performed to bytes transferred from memory: AI = FLOPs / bytes. For a linear layer of shape (d_in, d_out) processing a batch of B tokens: FLOPs = 2*B*d_in*d_out, bytes = (d_in*d_out + B*d_in + B*d_out) * dtype_bytes ≈ d_in*d_out * dtype_bytes for small B. Thus AI ≈ 2*B / dtype_bytes, which for fp16 (dtype_bytes=2) gives AI = B FLOPs/byte. The roofline model predicts achievable throughput as min(peak_TFLOPS, AI * peak_bandwidth_TB/s). The ridge point — where compute and bandwidth bounds intersect — occurs at AI = peak_TFLOPS / peak_bandwidth_TB/s. For an A100 (312 TFLOPS bf16, 2 TB/s): ridge point = 312 / 2 = 156 FLOPs/byte, meaning decode is bandwidth-bound for batch sizes below 156 and compute-bound above.

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from typing import List, Optional

def plot_roofline(
    peak_flops_Ts: float = 312.0,    # A100 bf16: 312 TFLOPS
    bw_TB_s: float = 2.0,            # A100 80GB bandwidth
    batch_sizes: Optional[List[int]] = None,
    n_params: float = 7e9,
    save_path: str = "roofline_llm.png",
) -> None:
    """Plot roofline model for LLM decode across batch sizes."""
    if batch_sizes is None:
        batch_sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bytes_per_param = 2                        # fp16
    flops_per_token = 2 * n_params             # ~2 FLOPs per parameter per token
    bw_bytes_per_s  = bw_TB_s * 1e12
    ridge_bs = peak_flops_Ts * 1e12 / (flops_per_token / (n_params * bytes_per_param))
    tput = []
    for bs in batch_sizes:
        ai = (flops_per_token * bs) / (n_params * bytes_per_param)
        achievable_flops_s = min(peak_flops_Ts * 1e12, ai * bw_bytes_per_s)
        tput.append(achievable_flops_s * bs / flops_per_token)  # tokens/s
    ridge_point_ai = peak_flops_Ts / bw_TB_s
    print(f"Ridge point AI: {ridge_point_ai:.0f} FLOPs/byte")
    print(f"Crossover batch size (approx): {ridge_point_ai:.0f}")
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.semilogx(batch_sizes, tput, 'b-o', label='Decode throughput (roofline)')
    ax.axvline(ridge_point_ai, color='r', linestyle='--', label=f'Crossover bs={ridge_point_ai:.0f}')
    ax.set_xlabel('Batch size'); ax.set_ylabel('Tokens / second')
    ax.set_title('LLM Decode Roofline — A100 80GB (312 TFLOPS, 2 TB/s)')
    ax.legend(); ax.grid(True, which='both')
    plt.tight_layout(); plt.savefig(save_path, dpi=150)
    print(f"Saved {save_path}")

plot_roofline()
```

## Cost per Token Formula

The cost per token for self-hosted inference is: cost_per_token = (GPU_hourly_rate + capex_per_hour) / (tokens_per_second * 3600). GPU hourly rate includes cloud instance cost or, for on-premise, the allocated electricity and operations cost per GPU-hour. Capex per hour amortises the GPU purchase price over its useful life (typically 2–3 years of continuous operation, ~17,500–26,000 hours). Tokens per second is the achieved decode throughput at the target batch size. For cloud APIs, pricing is quoted directly in dollars per million input or output tokens, so the formula simplifies to reading the vendor's published rate. The key insight is that tokens_per_second scales with batch size (until the compute-bound regime), so higher batch sizes dramatically reduce cost per token — but only if the workload can tolerate the queuing latency.

> **Batch Size as Cost Lever**: For decode-bound workloads, batch size is the main lever: doubling batch size roughly halves cost-per-token until you hit the compute-bound regime — profile your target batch size before investing in hardware

```python
from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class DeploymentOption:
    name: str
    hourly_usd: float           # cloud instance or electricity+ops cost per GPU-hour
    tokens_per_sec: float       # achieved decode throughput
    capex_usd: float = 0.0      # hardware purchase price (0 for cloud)
    lifespan_hours: float = 17520.0  # 2 years continuous

def cost_per_million_tokens(opt: DeploymentOption) -> float:
    """Compute infrastructure cost per 1M output tokens including amortized capex."""
    capex_per_hour   = opt.capex_usd / opt.lifespan_hours
    total_hourly     = opt.hourly_usd + capex_per_hour
    tokens_per_hour  = opt.tokens_per_sec * 3600
    return (total_hourly / tokens_per_hour) * 1_000_000

API_RATES_USD_PER_1M = {"GPT-4o API": 10.00, "GPT-3.5 API": 0.50}

options: Dict[str, DeploymentOption] = {
    "GPT-4o API":    DeploymentOption("GPT-4o API",    0.0,   50.0),
    "GPT-3.5 API":   DeploymentOption("GPT-3.5 API",   0.0,  200.0),
    "A100 cloud 1x": DeploymentOption("A100 1x cloud", 3.50, 1200.0),
    "A100 cloud 8x": DeploymentOption("A100 8x cloud",24.00, 9600.0),
    "H100 cloud 1x": DeploymentOption("H100 1x cloud", 5.00, 2800.0),
    "On-prem A100":  DeploymentOption("On-prem A100",  0.40, 1200.0, capex_usd=12_000.0),
}

print(f"{'Option':<22} {'Cost/1M tok':>12}  {'Tok/s':>8}")
print("-" * 48)
for name, opt in options.items():
    cost = API_RATES_USD_PER_1M.get(name, cost_per_million_tokens(opt))
    print(f"{name:<22}  ${cost:>10.2f}  {opt.tokens_per_sec:>7.0f}")
```

## Cloud vs On-premise Cost Comparison

Cloud API pricing is convenient but expensive at scale: GPT-4o at $10/1M output tokens costs 50–100× more than self-hosting an equivalent open-weight model on a cloud A100 instance. However, cloud APIs eliminate operational overhead, provide managed reliability, and require no minimum committed spend — making them cost-effective for low-volume use cases below roughly 100M tokens per month. Above that threshold, self-hosting on cloud GPUs (A100 or H100 instances) typically reduces cost by 10–30× per token. On-premise deployment further reduces cost by 2–3× versus cloud GPU instances by eliminating the cloud margin, but requires capital expenditure, hardware operations capacity, and sufficient volume to keep GPUs highly utilised (target >70% GPU utilisation to justify on-prem capex).

| Deployment option | Cost / 1M tokens | Latency p50 | Max throughput | Setup complexity |
| --- | --- | --- | --- | --- |
| GPT-4o API | $10.00 | 800–1500 ms (TTFT) | Unlimited (managed) | None — API key only |
| GPT-3.5 API | $0.50 | 300–600 ms (TTFT) | Unlimited (managed) | None — API key only |
| A100 cloud 1× | $0.81 | 50–120 ms | 1,200 tok/s (Llama-7B) | Medium — infra + serving stack |
| A100 cloud 8× | $0.69 | 30–80 ms | 9,600 tok/s (Llama-7B) | High — multi-GPU serving |
| H100 cloud 1× | $0.50 | 30–70 ms | 2,800 tok/s (Llama-7B) | Medium — infra + serving stack |
| On-prem A100 | $0.28 | 50–120 ms | 1,200 tok/s (Llama-7B) | High — hardware + ops team |

## Optimizing for Cost Efficiency

The highest-impact cost reduction levers, in rough order of impact, are: (1) Quantisation — moving from fp16 to int8 or int4 halves or quarters the weight bytes read per decode step, directly scaling memory-bandwidth-bound throughput by 2–4× at minimal quality loss for most models. (2) Batch size — as shown by the roofline model, increasing batch size amortises weight reads across more output tokens simultaneously. (3) Speculative decoding — Medusa or draft-model approaches achieve 2–3× throughput improvement with no additional GPU memory. (4) KV cache compression — reducing KV cache size via grouped-query attention (GQA), multi-query attention (MQA), or quantised KV cache frees memory for larger batch sizes. (5) Model selection — a smaller model at higher batch size often costs less per token than a larger model at low batch size while maintaining acceptable quality.

- Quantisation (int8/int4) is the single highest-leverage cost reduction: halving weight bytes doubles bandwidth-bound throughput at minimal quality cost.
- The roofline crossover batch size for an A100 (312 TFLOPS, 2 TB/s) is approximately 156 — below this, GPU is memory-bound; above, compute-bound.
- KV cache is a significant memory consumer: at seq_len=8K with Llama-7B in fp16, KV cache per request is 2 GB — larger than many smaller models entirely.
- GQA (grouped-query attention) reduces KV cache by n_heads/n_kv_heads factor; Llama-3 uses GQA with 8 KV heads vs 32 query heads — 4× KV memory reduction.
- Flash Attention reduces memory traffic for attention from O(S^2) to O(S) bytes, eliminating prefill bottlenecks for long contexts.
- Cost per token scales inversely with GPU utilisation — target >70% utilisation; below 50% indicates over-provisioned or under-batched deployment.
- Continuous batching (iteration-level scheduling) increases effective GPU utilisation from 30–40% (static batching) to 60–80% in typical chat workloads.

## Key Takeaways

LLM inference cost is dominated by the memory bandwidth bottleneck during autoregressive decode. At batch size 1, modern GPU compute units are utilised at less than 1% of their peak FLOPS because the bottleneck is streaming weights from HBM. The practical consequence is that optimisations targeting memory — quantisation, GQA, KV cache compression, speculative decoding — deliver larger cost reductions than optimisations targeting compute. For cost modelling, the three-layer framework (FLOPs → bandwidth → dollars) provides a principled methodology: count FLOPs to understand model complexity, apply the roofline to find the operating regime, then translate to dollars using observed throughput and GPU pricing. Always profile at your target batch size — roofline predictions can differ from measured throughput by 20–40% due to kernel overheads, memory fragmentation, and attention costs not captured in simplified models.

- Decode is almost always memory-bandwidth bound at batch size 1: arithmetic intensity ≈ 1 FLOP/byte versus ridge points of 100–300 FLOP/byte on modern GPUs.
- Prefill is compute-bound for long sequences: arithmetic intensity scales with sequence length S, reaching the ridge point around S=100–300 tokens.
- The cost crossover between cloud API and self-hosted A100 occurs at roughly 50–150M output tokens per month depending on model size.
- int8 quantisation reduces cost by ~2× with less than 1% quality degradation on most benchmarks; int4 reduces by ~4× with 2–5% degradation.
- GPU utilisation is the hidden efficiency multiplier: a 50%-utilised A100 costs 2× per token versus a fully utilised one.
- For latency-sensitive workloads, speculative decoding (Medusa) is the most practical 2–3× speedup with no additional infrastructure.

---

