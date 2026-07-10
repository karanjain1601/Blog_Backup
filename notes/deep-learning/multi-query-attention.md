---
title: "Multi-Query Attention (MQA) — Single KV Head for Fast Inference"
slug: "multi-query-attention"
description: "MQA shares a single key-value head across all query heads, shrinking KV cache by h×, reducing memory bandwidth pressure, and enabling faster autoregressive decoding at minimal quality cost."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgbXVsdGktaGVhZCBhdHRlbnRpb24gKE1IQSkgdXNlcyBoIGluZGVwZW5kZW50IHF1ZXJ5LCBrZXksIGFuZCB2YWx1ZSBwcm9qZWN0aW9ucyDigJQgb25lIHBlciBoZWFkLiBEdXJpbmcgYXV0b3JlZ3Jlc3NpdmUgaW5mZXJlbmNlIHRoZSBLViBjYWNoZSBncm93cyBsaW5lYXJseSB3aXRoIHNlcXVlbmNlIGxlbmd0aCBhbmQgbXVzdCBiZSByZWFkIGZyb20gR1BVIG1lbW9yeSBhdCBldmVyeSBnZW5lcmF0aW9uIHN0ZXAsIG1ha2luZyBtZW1vcnkgYmFuZHdpZHRoIHRoZSBwcmltYXJ5IGJvdHRsZW5lY2suIE11bHRpLVF1ZXJ5IEF0dGVudGlvbiAoTVFBLCBTaGF6ZWVyIDIwMTkpIHNoYXJlcyBhIHNpbmdsZSBrZXkgYW5kIHZhbHVlIGhlYWQgYWNyb3NzIGFsbCBoIHF1ZXJ5IGhlYWRzLiBUaGlzIHJlZHVjZXMgdGhlIEtWIGNhY2hlIHNpemUgYnkgaMOXIHdpdGhvdXQgY2hhbmdpbmcgdGhlIG51bWJlciBvZiBxdWVyeSBoZWFkcyBvciB0aGUgYXR0ZW50aW9uIGNvbXB1dGF0aW9uIHN0cnVjdHVyZSwgeWllbGRpbmcgc2lnbmlmaWNhbnRseSBmYXN0ZXIgZGVjb2RlIHRocm91Z2hwdXQgd2l0aCBvbmx5IGEgc21hbGwgcXVhbGl0eSBkZWdyYWRhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdGFuZGFyZCBNdWx0aS1IZWFkIEF0dGVudGlvbiBSZWNhcCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gTUhBIHdpdGggaCBoZWFkcywgZWFjaCBvZiBkaW1lbnNpb24gZF9oZWFkID0gZF9tb2RlbC9oLCB0aGVyZSBhcmUgdGhyZWUgcHJvamVjdGlvbiBtYXRyaWNlcyBwZXIgaGVhZDogV19RXmksIFdfS15pLCBXX1ZeaSDiiIgg4oSdXntkX21vZGVsw5dkX2hlYWR9LiBUb3RhbCBLViBwcm9qZWN0aW9uIHBhcmFtZXRlcnM6IDIgw5cgaCDDlyBkX21vZGVsIMOXIGRfaGVhZCA9IDIgw5cgZF9tb2RlbMKyLiBEdXJpbmcgaW5mZXJlbmNlLCB0aGUgS1YgY2FjaGUgZm9yIGEgc2luZ2xlIGxheWVyIHN0b3JlcyBoIMOXIFQgw5cgZF9oZWFkIGtleXMgYW5kIGggw5cgVCDDlyBkX2hlYWQgdmFsdWVzLCB0b3RhbGxpbmcgMiDDlyBoIMOXIFQgw5cgZF9oZWFkIGVsZW1lbnRzID0gMiDDlyBUIMOXIGRfbW9kZWwgZWxlbWVudHMgcGVyIGxheWVyLiBBY3Jvc3MgTCBsYXllcnMgdGhpcyBpcyAyIMOXIEwgw5cgVCDDlyBkX21vZGVsIHBhcmFtZXRlcnMg4oCUIGZvciBMTGFNQS0yLTcwQiAoTD04MCwgZD04MTkyLCBUPTQwOTYpIHRoaXMgaXMgfjQwIEdCIGluIGZsb2F0MTYuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIE11bHRpUXVlcnlBdHRlbnRpb24obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJcbiAgICBNUUE6IGggcXVlcnkgaGVhZHMgYnV0IGEgc2luZ2xlIHNoYXJlZCBLIGFuZCBWIGhlYWQuXG4gICAgS1YgY2FjaGUgaXMgaCB0aW1lcyBzbWFsbGVyIHRoYW4gTUhBLlxuICAgIFwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsPTUxMiwgbl9oZWFkcz04KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubl9oZWFkcyA9IG5faGVhZHNcbiAgICAgICAgc2VsZi5kX2hlYWQgPSBkX21vZGVsIC8vIG5faGVhZHNcbiAgICAgICAgIyBTZXBhcmF0ZSBRIHByb2plY3Rpb24gcGVyIGhlYWRcbiAgICAgICAgc2VsZi5xX3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSkgICAgICAgIyBoICogZF9oZWFkXG4gICAgICAgICMgU2luZ2xlIHNoYXJlZCBLIGFuZCBWIHByb2plY3Rpb24gKG9ubHkgMSBoZWFkKVxuICAgICAgICBzZWxmLmtfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBzZWxmLmRfaGVhZCwgYmlhcz1GYWxzZSkgICAjIDEgaGVhZFxuICAgICAgICBzZWxmLnZfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBzZWxmLmRfaGVhZCwgYmlhcz1GYWxzZSkgICAjIDEgaGVhZFxuICAgICAgICBzZWxmLm91dF9wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBtYXNrPU5vbmUpOlxuICAgICAgICBCLCBULCBDID0geC5zaGFwZVxuICAgICAgICAjIFE6IChCLCBoLCBULCBkX2hlYWQpXG4gICAgICAgIFEgPSBzZWxmLnFfcHJvaih4KS52aWV3KEIsIFQsIHNlbGYubl9oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICAjIEssIFY6IChCLCAxLCBULCBkX2hlYWQpIC0tIHNpbmdsZSBoZWFkLCBicm9hZGNhc3QgYWNyb3NzIGFsbCBxdWVyeSBoZWFkc1xuICAgICAgICBLID0gc2VsZi5rX3Byb2ooeCkudmlldyhCLCBULCAxLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIFYgPSBzZWxmLnZfcHJvaih4KS52aWV3KEIsIFQsIDEsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgYXR0ID0gKFEgQCBLLnRyYW5zcG9zZSgtMiwgLTEpKSAqIHNlbGYuZF9oZWFkICoqIC0wLjUgICMgSyBicm9hZGNhc3RzIHRvIGhcbiAgICAgICAgaWYgbWFzayBpcyBub3QgTm9uZTpcbiAgICAgICAgICAgIGF0dCA9IGF0dC5tYXNrZWRfZmlsbChtYXNrID09IDAsIGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpKVxuICAgICAgICBvdXQgPSBGLnNvZnRtYXgoYXR0LCBkaW09LTEpIEAgViAgIyBWIGJyb2FkY2FzdHMgdG8gaFxuICAgICAgICByZXR1cm4gc2VsZi5vdXRfcHJvaihvdXQudHJhbnNwb3NlKDEsIDIpLmNvbnRpZ3VvdXMoKS52aWV3KEIsIFQsIEMpKVxuXG5tcWEgPSBNdWx0aVF1ZXJ5QXR0ZW50aW9uKGRfbW9kZWw9NTEyLCBuX2hlYWRzPTgpXG54ID0gdG9yY2gucmFuZG4oMiwgMzIsIDUxMilcbnByaW50KGZcdTAwMjdPdXRwdXQ6IHttcWEoeCkuc2hhcGV9XHUwMDI3KSAgIyAoMiwgMzIsIDUxMilcbnByaW50KGZcdTAwMjdNUUEgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtcWEucGFyYW1ldGVycygpKTosfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLViBDYWNoZSBTaXplIGFuZCBJbmZlcmVuY2UgVGhyb3VnaHB1dCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGluZmVyZW5jZSBzcGVlZHVwIGZyb20gTVFBIGNvbWVzIGZyb20gcmVkdWNlZCBtZW1vcnkgYmFuZHdpZHRoIGNvbnN1bXB0aW9uLiBEdXJpbmcgZGVjb2RlLCBmb3IgZWFjaCBuZXcgdG9rZW4gdGhlIEdQVSBtdXN0IGxvYWQgdGhlIGVudGlyZSBLViBjYWNoZSBmcm9tIEhCTS4gTUhBIGxvYWRzIDIgw5cgaCDDlyBUIMOXIGRfaGVhZCB2YWx1ZXMgcGVyIGxheWVyOyBNUUEgbG9hZHMgb25seSAyIMOXIFQgw5cgZF9oZWFkIHZhbHVlcyDigJQgYW4gaMOXIHJlZHVjdGlvbi4gRm9yIGg9OCB0aGlzIGlzIGFuIDjDlyByZWR1Y3Rpb24gaW4gS1YgY2FjaGUgcmVhZHMuIE9uIG1lbW9yeS1iYW5kd2lkdGgtbGltaXRlZCBoYXJkd2FyZSAoYWxsIG1vZGVybiBpbmZlcmVuY2Ugc2NlbmFyaW9zKSwgdGhpcyB0cmFuc2xhdGVzIGRpcmVjdGx5IHRvIHByb3BvcnRpb25hbGx5IGhpZ2hlciB0aHJvdWdocHV0LiBUaGUgY29tcHV0ZSBjb3N0IChtYXRtdWwgRkxPUHMpIGNoYW5nZXMgbWluaW1hbGx5IGJlY2F1c2UgYXR0ZW50aW9uIGlzIGNvbXB1dGVkIHdpdGggdGhlIHNhbWUgUSBidXQgdGhlIEsvViBicm9hZGNhc3QgaXMgZnJlZS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiTWVtb3J5IEJhbmR3aWR0aCBJcyB0aGUgSW5mZXJlbmNlIEJvdHRsZW5lY2siLCJjb250ZW50IjoiRHVyaW5nIHRva2VuLWJ5LXRva2VuIGRlY29kZSwgdGhlIEdQVSBnZW5lcmF0ZXMgb25lIHRva2VuIHBlciBmb3J3YXJkIHBhc3MuIEVhY2ggcGFzcyByZWFkcyBtb2RlbCB3ZWlnaHRzIChmcm96ZW4sIGNhbiBiZSBwcmVmZXRjaGVkKSBhbmQgdGhlIGVudGlyZSBLViBjYWNoZSAoZ3Jvd3Mgd2l0aCBzZXF1ZW5jZSBsZW5ndGgpLiBBMTAwIDgwR0IgaGFzIDIgVEIvcyBIQk0gYmFuZHdpZHRoLiBGb3IgYSA3MEIgbW9kZWwgd2l0aCA0MCBHQiBLViBjYWNoZSBhdCBUPTQwOTYsIGxvYWRpbmcgdGhlIGNhY2hlIGFsb25lIHRha2VzIH4yMCBtcyBwZXIgdG9rZW4g4oCUIHlpZWxkaW5nIG9ubHkgfjUwIHRva2Vucy9zZWNvbmQgZXZlbiBhdCB6ZXJvIEZMT1AgY29zdC4gTVFBIGRpcmVjdGx5IGF0dGFja3MgdGhpcyBib3R0bGVuZWNrLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IHRpbWVcblxuY2xhc3MgTUhBRGVjb2RlKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw9NTEyLCBuX2hlYWRzPTgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uX2hlYWRzLCBzZWxmLmRfaGVhZCA9IG5faGVhZHMsIGRfbW9kZWwgLy8gbl9oZWFkc1xuICAgICAgICBzZWxmLnFrdiA9IG5uLkxpbmVhcihkX21vZGVsLCAzICogZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYua19jYWNoZSA9IHNlbGYudl9jYWNoZSA9IE5vbmVcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBCLCBULCBDID0geC5zaGFwZVxuICAgICAgICBxLCBrLCB2ID0gc2VsZi5xa3YoeCkuc3BsaXQoQywgZGltPS0xKVxuICAgICAgICBzcGxpdCA9IGxhbWJkYSB0LCBoOiB0LnZpZXcoQiwgVCwgaCwgQyAvLyBoKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgcSwgaywgdiA9IHNwbGl0KHEsIHNlbGYubl9oZWFkcyksIHNwbGl0KGssIHNlbGYubl9oZWFkcyksIHNwbGl0KHYsIHNlbGYubl9oZWFkcylcbiAgICAgICAgc2VsZi5rX2NhY2hlID0gdG9yY2guY2F0KFtzZWxmLmtfY2FjaGUsIGtdLCBkaW09MikgaWYgc2VsZi5rX2NhY2hlIGlzIG5vdCBOb25lIGVsc2Uga1xuICAgICAgICBzZWxmLnZfY2FjaGUgPSB0b3JjaC5jYXQoW3NlbGYudl9jYWNoZSwgdl0sIGRpbT0yKSBpZiBzZWxmLnZfY2FjaGUgaXMgbm90IE5vbmUgZWxzZSB2XG4gICAgICAgIGF0dCA9IEYuc29mdG1heCgocSBAIHNlbGYua19jYWNoZS50cmFuc3Bvc2UoLTIsIC0xKSkgKiBzZWxmLmRfaGVhZCAqKiAtMC41LCBkaW09LTEpXG4gICAgICAgIHJldHVybiBzZWxmLnByb2ooKGF0dCBAIHNlbGYudl9jYWNoZSkudHJhbnNwb3NlKDEsIDIpLmNvbnRpZ3VvdXMoKS52aWV3KEIsIFQsIEMpKVxuXG5jbGFzcyBNUUFEZWNvZGUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbD01MTIsIG5faGVhZHM9OCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5faGVhZHMsIHNlbGYuZF9oZWFkID0gbl9oZWFkcywgZF9tb2RlbCAvLyBuX2hlYWRzXG4gICAgICAgIHNlbGYucV9wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYua19wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwgLy8gbl9oZWFkcywgYmlhcz1GYWxzZSkgICMgc2luZ2xlIGhlYWRcbiAgICAgICAgc2VsZi52X3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCAvLyBuX2hlYWRzLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnByb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5rX2NhY2hlID0gc2VsZi52X2NhY2hlID0gTm9uZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIEIsIFQsIEMgPSB4LnNoYXBlXG4gICAgICAgIHEgPSBzZWxmLnFfcHJvaih4KS52aWV3KEIsIFQsIHNlbGYubl9oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICBrID0gc2VsZi5rX3Byb2ooeCkudmlldyhCLCBULCAxLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIHYgPSBzZWxmLnZfcHJvaih4KS52aWV3KEIsIFQsIDEsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgc2VsZi5rX2NhY2hlID0gdG9yY2guY2F0KFtzZWxmLmtfY2FjaGUsIGtdLCBkaW09MikgaWYgc2VsZi5rX2NhY2hlIGlzIG5vdCBOb25lIGVsc2Uga1xuICAgICAgICBzZWxmLnZfY2FjaGUgPSB0b3JjaC5jYXQoW3NlbGYudl9jYWNoZSwgdl0sIGRpbT0yKSBpZiBzZWxmLnZfY2FjaGUgaXMgbm90IE5vbmUgZWxzZSB2XG4gICAgICAgIGF0dCA9IEYuc29mdG1heCgocSBAIHNlbGYua19jYWNoZS50cmFuc3Bvc2UoLTIsIC0xKSkgKiBzZWxmLmRfaGVhZCAqKiAtMC41LCBkaW09LTEpXG4gICAgICAgIHJldHVybiBzZWxmLnByb2ooKGF0dCBAIHNlbGYudl9jYWNoZSkudHJhbnNwb3NlKDEsIDIpLmNvbnRpZ3VvdXMoKS52aWV3KEIsIFQsIEMpKVxuXG5kX21vZGVsLCBuX2hlYWRzLCBUX3Byb21wdCA9IDUxMiwgOCwgMjU2XG5taGFfbSwgbXFhX20gPSBNSEFEZWNvZGUoZF9tb2RlbCwgbl9oZWFkcyksIE1RQURlY29kZShkX21vZGVsLCBuX2hlYWRzKVxucHJvbXB0ID0gdG9yY2gucmFuZG4oMSwgVF9wcm9tcHQsIGRfbW9kZWwpXG5taGFfbShwcm9tcHQpOyBtcWFfbShwcm9tcHQpICAjIGZpbGwgY2FjaGVcbm1oYV9rdl9tYiA9IHN1bShjLm51bWVsKCkgKiAyIC8gMWU2IGZvciBjIGluIFttaGFfbS5rX2NhY2hlLCBtaGFfbS52X2NhY2hlXSlcbm1xYV9rdl9tYiA9IHN1bShjLm51bWVsKCkgKiAyIC8gMWU2IGZvciBjIGluIFttcWFfbS5rX2NhY2hlLCBtcWFfbS52X2NhY2hlXSlcbnByaW50KGZcdTAwMjdNSEEgS1YgY2FjaGU6IHttaGFfa3ZfbWI6LjJmfSBNQlx1MDAyNylcbnByaW50KGZcdTAwMjdNUUEgS1YgY2FjaGU6IHttcWFfa3ZfbWI6LjJmfSBNQiAgKHttaGFfa3ZfbWIvbXFhX2t2X21iOi4xZn14IHNtYWxsZXIpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikdyb3VwZWQgUXVlcnkgQXR0ZW50aW9uIChHUUEpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHcm91cGVkIFF1ZXJ5IEF0dGVudGlvbiAoQWluc2xpZSBldCBhbC4gMjAyMykgaW50ZXJwb2xhdGVzIGJldHdlZW4gTUhBIChnPWggZ3JvdXBzKSBhbmQgTVFBIChnPTEgZ3JvdXApLiBXaXRoIGcgZ3JvdXBzLCBnIHNldHMgb2YgSyxWIHByb2plY3Rpb25zIGFyZSBzaGFyZWQgYWNyb3NzIGgvZyBxdWVyeSBoZWFkcyBlYWNoLiBHUUEgYWNoaWV2ZXMgcXVhbGl0eSBjbG9zZSB0byBNSEEgd2hpbGUgcmVkdWNpbmcgS1YgY2FjaGUgYnkgaC9nw5cg4oCUIGEgdHVuYWJsZSBxdWFsaXR5L21lbW9yeSB0cmFkZS1vZmYuIExMYU1BLTItNzBCIHVzZXMgR1FBIHdpdGggZz04IGdyb3VwcyBhbmQgaD02NCBoZWFkcyAoOCBLL1YgaGVhZHMgdG90YWwsIDggcXVlcnkgaGVhZHMgcGVyIEsvViBoZWFkKS4gTWlzdHJhbC03QiB1c2VzIEdRQSB3aXRoIGc9OCBncm91cHMsIG5faGVhZHM9MzIsIG5fa3ZfaGVhZHM9OC4gR1FBIGNhbiBhbHNvIGJlIG9idGFpbmVkIGJ5IG1lYW4tcG9vbGluZyBNSEEgY2hlY2twb2ludCBLL1YgaGVhZHMgZm9yIHBvc3QtaG9jIGNvbnZlcnNpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEdyb3VwZWRRdWVyeUF0dGVudGlvbihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlxuICAgIEdRQTogbl9oZWFkcyBxdWVyeSBoZWFkcyBncm91cGVkIGludG8gbl9rdl9oZWFkcyBLViBncm91cHMuXG4gICAgbl9rdl9oZWFkcz1uX2hlYWRzID1cdTAwM2UgTUhBOyBuX2t2X2hlYWRzPTEgPVx1MDAzZSBNUUEuXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw9NTEyLCBuX2hlYWRzPTgsIG5fa3ZfaGVhZHM9Mik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBhc3NlcnQgbl9oZWFkcyAlIG5fa3ZfaGVhZHMgPT0gMFxuICAgICAgICBzZWxmLm5faGVhZHMgPSBuX2hlYWRzXG4gICAgICAgIHNlbGYubl9rdl9oZWFkcyA9IG5fa3ZfaGVhZHNcbiAgICAgICAgc2VsZi5uX3JlcCA9IG5faGVhZHMgLy8gbl9rdl9oZWFkcyAgIyBxdWVyeSBoZWFkcyBwZXIgS1YgZ3JvdXBcbiAgICAgICAgc2VsZi5kX2hlYWQgPSBkX21vZGVsIC8vIG5faGVhZHNcbiAgICAgICAgc2VsZi5xX3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5rX3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgbl9rdl9oZWFkcyAqIHNlbGYuZF9oZWFkLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnZfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBuX2t2X2hlYWRzICogc2VsZi5kX2hlYWQsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYub3V0X3Byb2ogPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBCLCBULCBDID0geC5zaGFwZVxuICAgICAgICBRID0gc2VsZi5xX3Byb2ooeCkudmlldyhCLCBULCBzZWxmLm5faGVhZHMsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgSyA9IHNlbGYua19wcm9qKHgpLnZpZXcoQiwgVCwgc2VsZi5uX2t2X2hlYWRzLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIFYgPSBzZWxmLnZfcHJvaih4KS52aWV3KEIsIFQsIHNlbGYubl9rdl9oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICAjIFJlcGVhdCBLLFYgZm9yIGVhY2ggZ3JvdXAgKGludGVybGVhdmVkKVxuICAgICAgICBLID0gSy5yZXBlYXRfaW50ZXJsZWF2ZShzZWxmLm5fcmVwLCBkaW09MSkgICMgKEIsIG5faGVhZHMsIFQsIGRfaGVhZClcbiAgICAgICAgViA9IFYucmVwZWF0X2ludGVybGVhdmUoc2VsZi5uX3JlcCwgZGltPTEpXG4gICAgICAgIGF0dCA9IEYuc29mdG1heCgoUSBAIEsudHJhbnNwb3NlKC0yLCAtMSkpICogc2VsZi5kX2hlYWQgKiogLTAuNSwgZGltPS0xKVxuICAgICAgICByZXR1cm4gc2VsZi5vdXRfcHJvaigoYXR0IEAgVikudHJhbnNwb3NlKDEsIDIpLmNvbnRpZ3VvdXMoKS52aWV3KEIsIFQsIEMpKVxuXG54ID0gdG9yY2gucmFuZG4oMiwgMzIsIDUxMilcbmZvciBuX2t2IGluIFs4LCA0LCAyLCAxXTpcbiAgICBtID0gR3JvdXBlZFF1ZXJ5QXR0ZW50aW9uKDUxMiwgbl9oZWFkcz04LCBuX2t2X2hlYWRzPW5fa3YpXG4gICAgbGFiZWwgPSBcdTAwMjdNSEFcdTAwMjcgaWYgbl9rdj09OCBlbHNlIChcdTAwMjdNUUFcdTAwMjcgaWYgbl9rdj09MSBlbHNlIFx1MDAyN0dRQVx1MDAyNylcbiAgICBrdl9wYXJhbXMgPSBzdW0ocC5udW1lbCgpIGZvciBuLHAgaW4gbS5uYW1lZF9wYXJhbWV0ZXJzKCkgaWYgXHUwMDI3X3Byb2pcdTAwMjcgaW4gbiBhbmQgblswXSBpbiBcdTAwMjdrdlx1MDAyNylcbiAgICBwcmludChmXHUwMDI3bl9rdj17bl9rdn0gKHtsYWJlbH0pOiBLViBwYXJhbXM9e2t2X3BhcmFtczosfSwgb3V0PXttKHgpLnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXJhbWV0ZXIgQ291bnQgQ29tcGFyaXNvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgY291bnRfYXR0ZW50aW9uX3BhcmFtcyhkX21vZGVsLCBuX2hlYWRzLCBuX2t2X2hlYWRzLCBpbmNsdWRlX291dHB1dD1UcnVlKTpcbiAgICBcIlwiXCJDb3VudCBwYXJhbWV0ZXJzIGZvciBRLCBLLCBWLCBhbmQgb3V0cHV0IHByb2plY3Rpb25zLlwiXCJcIlxuICAgIGRfaGVhZCA9IGRfbW9kZWwgLy8gbl9oZWFkc1xuICAgIHFfcGFyYW1zID0gbl9oZWFkcyAqIGRfbW9kZWwgKiBkX2hlYWQgICAgICMgUTogb25lIHBlciBoZWFkXG4gICAga19wYXJhbXMgPSBuX2t2X2hlYWRzICogZF9tb2RlbCAqIGRfaGVhZCAgIyBLOiBvbmUgcGVyIEtWIGdyb3VwXG4gICAgdl9wYXJhbXMgPSBuX2t2X2hlYWRzICogZF9tb2RlbCAqIGRfaGVhZCAgIyBWOiBvbmUgcGVyIEtWIGdyb3VwXG4gICAgb19wYXJhbXMgPSBkX21vZGVsICogZF9tb2RlbCBpZiBpbmNsdWRlX291dHB1dCBlbHNlIDBcbiAgICB0b3RhbCA9IHFfcGFyYW1zICsga19wYXJhbXMgKyB2X3BhcmFtcyArIG9fcGFyYW1zXG4gICAga3ZfY2FjaGVfcGVyX3RvayA9IDIgKiBuX2t2X2hlYWRzICogZF9oZWFkICAjIEsgKyBWIGVsZW1lbnRzIHBlciB0b2tlblxuICAgIHJldHVybiB0b3RhbCwga3ZfY2FjaGVfcGVyX3Rva1xuXG5jb25maWdzID0gW1xuICAgIChcdTAwMjdNSEEgIGg9MzIga3Y9MzJcdTAwMjcsICA0MDk2LCAzMiwgMzIpLFxuICAgIChcdTAwMjdHUUEgIGg9MzIga3Y9OFx1MDAyNywgICA0MDk2LCAzMiwgIDgpLFxuICAgIChcdTAwMjdHUUEgIGg9MzIga3Y9NFx1MDAyNywgICA0MDk2LCAzMiwgIDQpLFxuICAgIChcdTAwMjdNUUEgIGg9MzIga3Y9MVx1MDAyNywgICA0MDk2LCAzMiwgIDEpLFxuICAgIChcdTAwMjdNSEEgIGg9NjQga3Y9NjRcdTAwMjcsICA4MTkyLCA2NCwgNjQpLFxuICAgIChcdTAwMjdHUUEgIGg9NjQga3Y9OFx1MDAyNywgICA4MTkyLCA2NCwgIDgpLFxuICAgIChcdTAwMjdNUUEgIGg9NjQga3Y9MVx1MDAyNywgICA4MTkyLCA2NCwgIDEpLFxuXVxuXG5wcmludChmXHUwMDI3e1x1MDAyN0NvbmZpZ1x1MDAyNzpcdTAwM2MyMn0ge1x1MDAyN1BhcmFtc1x1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0tWL3Rva1x1MDAyNzpcdTAwM2U4fSB7XHUwMDI3S1YgUmVkdWN0aW9uXHUwMDI3Olx1MDAzZTE0fVx1MDAyNylcbmJhc2Vfa3YgPSB7NDA5NjogTm9uZSwgODE5MjogTm9uZX1cbmZvciBuYW1lLCBkLCBoLCBrdiBpbiBjb25maWdzOlxuICAgIHRvdGFsLCBrdl9wZXJfdG9rID0gY291bnRfYXR0ZW50aW9uX3BhcmFtcyhkLCBoLCBrdilcbiAgICBtaGFfa3YgPSAyICogKGQgLy8gaCkgKiBoICAjIE1IQSBiYXNlbGluZVxuICAgIHJlZHVjdGlvbiA9IG1oYV9rdiAvIGt2X3Blcl90b2tcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMjJ9IHt0b3RhbDpcdTAwM2UxMCx9IHtrdl9wZXJfdG9rOlx1MDAzZTh9IHtyZWR1Y3Rpb246XHUwMDNlMTQuMWZ9eFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaGVyZSBNUUEgYW5kIEdRQSBBcmUgVXNlZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTVFBIGFuZCBHUUEgaGF2ZSBiZWVuIHdpZGVseSBhZG9wdGVkIGFzIHRoZSBkZWZhdWx0IGluIHByb2R1Y3Rpb24gTExNcy4gVGhlIHF1YWxpdHkgY29zdCBvZiBNUUEgKHZzIE1IQSkgaXMgbWVhc3VyZWQgdG8gYmUgbGVzcyB0aGFuIDUlIGRlZ3JhZGF0aW9uIG9uIG1vc3QgYmVuY2htYXJrcywgd2hpbGUgdGhyb3VnaHB1dCBnYWlucyBhdCBsb25nIHNlcXVlbmNlIGxlbmd0aHMgYXJlIHN1YnN0YW50aWFsLiBHUUEgd2l0aCBuX2t2X2hlYWRzPTggaGFzIGJlY29tZSB0aGUgZG9taW5hbnQgY2hvaWNlIGZvciBsYXJnZSBtb2RlbHMsIG9mZmVyaW5nIG1vc3Qgb2YgTVFBXHUwMDI3cyBlZmZpY2llbmN5IHdoaWxlIHJlY292ZXJpbmcgcXVhbGl0eSBjbG9zZXIgdG8gTUhBLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUGFMTSAoNTQwQiwgMjAyMik6IE1RQSDigJQgb25lIG9mIHRoZSBmaXJzdCBsYXJnZS1zY2FsZSBkZXBsb3ltZW50cy4iLCJGYWxjb24tN0IgYW5kIEZhbGNvbi00MEI6IE1RQSBieSBkZWZhdWx0LiIsIk1pc3RyYWwtN0IgKDIwMjMpOiBHUUEgd2l0aCBuX2t2X2hlYWRzPTgsIG5faGVhZHM9MzIuIiwiTExhTUEtMi03MEI6IEdRQSB3aXRoIG5fa3ZfaGVhZHM9OCwgbl9oZWFkcz02NC4iLCJMTGFNQS0zIGZhbWlseTogR1FBIGFjcm9zcyBhbGwgc2l6ZXMgKDhCLCA3MEIsIDQwNUIpLiIsIlN0YXJDb2RlciAoMTVCKTogTVFBIGZvciBmYXN0IGNvZGUgZ2VuZXJhdGlvbiBpbmZlcmVuY2UuIiwiR2VtbWEtMiBhbmQgUGhpLTM6IEdRQSBhcyBzdGFuZGFyZC4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbjogTUhBIHZzIE1RQSB2cyBHUUEifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXR0cmlidXRlIiwiTUhBIiwiTVFBIiwiR1FBIChnIGdyb3VwcykiXSwicm93cyI6W1siSy9WIGhlYWRzIiwiaCAob25lIHBlciBxdWVyeSBoZWFkKSIsIjEgKHNoYXJlZCBhY3Jvc3MgYWxsKSIsImcgKGcgXHUwMDNjIGgsIHNoYXJlZCB3aXRoaW4gZ3JvdXApIl0sWyJLViBjYWNoZSBzaXplIiwiMiDDlyBoIMOXIFQgw5cgZF9oZWFkIiwiMiDDlyBUIMOXIGRfaGVhZCIsIjIgw5cgZyDDlyBUIMOXIGRfaGVhZCJdLFsiS1YgY2FjaGUgcmVkdWN0aW9uIiwiMcOXIChiYXNlbGluZSkiLCJow5cgc21hbGxlciIsImgvZ8OXIHNtYWxsZXIiXSxbIkluZmVyZW5jZSB0aHJvdWdocHV0IiwiQmFzZWxpbmUiLCJVcCB0byBow5cgZmFzdGVyIChiYW5kd2lkdGggYm91bmQpIiwiQmV0d2VlbiBNSEEgYW5kIE1RQSJdLFsiUXVhbGl0eSB2cyBNSEEiLCJCZXN0IHF1YWxpdHkiLCJ+MS01JSBkcm9wIG9uIGJlbmNobWFya3MiLCJOZWdsaWdpYmxlIGRyb3AgYXQgZz04Il0sWyJQYXJhbWV0ZXIgY291bnQiLCJGdWxsIChRLEssViBlYWNoIGTCsikiLCJROiBkwrIsIEsrVjogMsOXZMOXZF9oZWFkIiwiUTogZMKyLCBLK1Y6IDJnw5dkw5dkX2hlYWQiXSxbIkNvbnZlcnQgZnJvbSBNSEEiLCJOL0EiLCJNdXN0IHJldHJhaW4iLCJDYW4gYXBwcm94aW1hdGUgYnkgcG9vbGluZyBoZWFkcyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhaW5pbmcgQ29uc2lkZXJhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1RQSBhbmQgR1FBIG11c3QgdHlwaWNhbGx5IGJlIHRyYWluZWQgZnJvbSBzY3JhdGNoIOKAlCBjb252ZXJ0aW5nIGEgcHJldHJhaW5lZCBNSEEgbW9kZWwgdG8gTVFBIGJ5IG5haXZlbHkgc2hhcmluZyBLL1Ygd2VpZ2h0cyBkZWdyYWRlcyBxdWFsaXR5IHNpZ25pZmljYW50bHkuIE9uZSBleGNlcHRpb246IEFpbnNsaWUgZXQgYWwuICgyMDIzKSBzaG93ZWQgdGhhdCBHUUEgY2FuIGJlIGluaXRpYWxpemVkIGZyb20gTUhBIGJ5IG1lYW4tcG9vbGluZyB0aGUgSy9WIGhlYWRzIHdpdGhpbiBlYWNoIGdyb3VwIGFuZCB0aGVuIGZpbmUtdHVuaW5nIGZvciBhIHNtYWxsIGZyYWN0aW9uIG9mIHByZXRyYWluaW5nIGNvbXB1dGUgKH41JSkgdG8gcmVjb3ZlciBtb3N0IG9mIHRoZSBxdWFsaXR5IGdhcC4gVGhpcyB1cHRyYWluZWQgR1FBIGlzIG5vdyB1c2VkIGluIExMYU1BLTItNzBCLCB3aGljaCB3YXMgaW5pdGlhbGl6ZWQgZnJvbSBNSEEgYW5kIHRoZW4gY29udmVydGVkLiBUaGUgZmluZS10dW5pbmcgY29zdCBpcyBhcHByb3hpbWF0ZWx5IDUlIG9mIHRoZSBvcmlnaW5hbCBwcmV0cmFpbmluZyBjb21wdXRlLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiBjaG9vc2luZyBiZXR3ZWVuIE1IQSwgTVFBLCBhbmQgR1FBIGZvciBhIG5ldyBtb2RlbDogZm9yIG1vZGVscyB1bmRlciA3QiBwYXJhbWV0ZXJzIHdoZXJlIEtWIGNhY2hlIHByZXNzdXJlIGlzIGxvdywgTUhBIGlzIHNhZmUgYW5kIG1heGltaXplcyBxdWFsaXR5LiBGb3IgN0LigJM3MEIgbW9kZWxzIGRlcGxveWVkIGF0IHNjYWxlIHdpdGggbG9uZyBjb250ZXh0LCBHUUEgd2l0aCBnPTggaXMgdGhlIGN1cnJlbnQgYmVzdCBwcmFjdGljZSDigJQgaXQgY3V0cyBLViBjYWNoZSBiYW5kd2lkdGggYnkgOMOXIHdpdGggbmVnbGlnaWJsZSBxdWFsaXR5IGxvc3MuIFB1cmUgTVFBIChnPTEpIGlzIGFwcHJvcHJpYXRlIGZvciBleHRyZW1lbHkgYmFuZHdpZHRoLWNvbnN0cmFpbmVkIGluZmVyZW5jZSAoZS5nLiwgZWRnZSBkZXZpY2VzLCBiYXRjaCBzaXplIDEpIHdoZXJlIGV2ZW4gR1FBXHUwMDI3cyBzbWFsbCBjYWNoZSBpcyB0b28gbGFyZ2UuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Multi-Query Attention (MQA) — Single KV Head for Fast Inference

Standard multi-head attention (MHA) uses h independent query, key, and value projections — one per head. During autoregressive inference the KV cache grows linearly with sequence length and must be read from GPU memory at every generation step, making memory bandwidth the primary bottleneck. Multi-Query Attention (MQA, Shazeer 2019) shares a single key and value head across all h query heads. This reduces the KV cache size by h× without changing the number of query heads or the attention computation structure, yielding significantly faster decode throughput with only a small quality degradation.

## Standard Multi-Head Attention Recap

In MHA with h heads, each of dimension d_head = d_model/h, there are three projection matrices per head: W_Q^i, W_K^i, W_V^i ∈ ℝ^{d_model×d_head}. Total KV projection parameters: 2 × h × d_model × d_head = 2 × d_model². During inference, the KV cache for a single layer stores h × T × d_head keys and h × T × d_head values, totalling 2 × h × T × d_head elements = 2 × T × d_model elements per layer. Across L layers this is 2 × L × T × d_model parameters — for LLaMA-2-70B (L=80, d=8192, T=4096) this is ~40 GB in float16.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiQueryAttention(nn.Module):
    """
    MQA: h query heads but a single shared K and V head.
    KV cache is h times smaller than MHA.
    """
    def __init__(self, d_model=512, n_heads=8):
        super().__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        # Separate Q projection per head
        self.q_proj = nn.Linear(d_model, d_model, bias=False)       # h * d_head
        # Single shared K and V projection (only 1 head)
        self.k_proj = nn.Linear(d_model, self.d_head, bias=False)   # 1 head
        self.v_proj = nn.Linear(d_model, self.d_head, bias=False)   # 1 head
        self.out_proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x, mask=None):
        B, T, C = x.shape
        # Q: (B, h, T, d_head)
        Q = self.q_proj(x).view(B, T, self.n_heads, self.d_head).transpose(1, 2)
        # K, V: (B, 1, T, d_head) -- single head, broadcast across all query heads
        K = self.k_proj(x).view(B, T, 1, self.d_head).transpose(1, 2)
        V = self.v_proj(x).view(B, T, 1, self.d_head).transpose(1, 2)
        att = (Q @ K.transpose(-2, -1)) * self.d_head ** -0.5  # K broadcasts to h
        if mask is not None:
            att = att.masked_fill(mask == 0, float('-inf'))
        out = F.softmax(att, dim=-1) @ V  # V broadcasts to h
        return self.out_proj(out.transpose(1, 2).contiguous().view(B, T, C))

mqa = MultiQueryAttention(d_model=512, n_heads=8)
x = torch.randn(2, 32, 512)
print(f'Output: {mqa(x).shape}')  # (2, 32, 512)
print(f'MQA params: {sum(p.numel() for p in mqa.parameters()):,}')
```

## KV Cache Size and Inference Throughput

The inference speedup from MQA comes from reduced memory bandwidth consumption. During decode, for each new token the GPU must load the entire KV cache from HBM. MHA loads 2 × h × T × d_head values per layer; MQA loads only 2 × T × d_head values — an h× reduction. For h=8 this is an 8× reduction in KV cache reads. On memory-bandwidth-limited hardware (all modern inference scenarios), this translates directly to proportionally higher throughput. The compute cost (matmul FLOPs) changes minimally because attention is computed with the same Q but the K/V broadcast is free.

> **Memory Bandwidth Is the Inference Bottleneck**: During token-by-token decode, the GPU generates one token per forward pass. Each pass reads model weights (frozen, can be prefetched) and the entire KV cache (grows with sequence length). A100 80GB has 2 TB/s HBM bandwidth. For a 70B model with 40 GB KV cache at T=4096, loading the cache alone takes ~20 ms per token — yielding only ~50 tokens/second even at zero FLOP cost. MQA directly attacks this bottleneck.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import time

class MHADecode(nn.Module):
    def __init__(self, d_model=512, n_heads=8):
        super().__init__()
        self.n_heads, self.d_head = n_heads, d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.k_cache = self.v_cache = None

    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=-1)
        split = lambda t, h: t.view(B, T, h, C // h).transpose(1, 2)
        q, k, v = split(q, self.n_heads), split(k, self.n_heads), split(v, self.n_heads)
        self.k_cache = torch.cat([self.k_cache, k], dim=2) if self.k_cache is not None else k
        self.v_cache = torch.cat([self.v_cache, v], dim=2) if self.v_cache is not None else v
        att = F.softmax((q @ self.k_cache.transpose(-2, -1)) * self.d_head ** -0.5, dim=-1)
        return self.proj((att @ self.v_cache).transpose(1, 2).contiguous().view(B, T, C))

class MQADecode(nn.Module):
    def __init__(self, d_model=512, n_heads=8):
        super().__init__()
        self.n_heads, self.d_head = n_heads, d_model // n_heads
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model // n_heads, bias=False)  # single head
        self.v_proj = nn.Linear(d_model, d_model // n_heads, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.k_cache = self.v_cache = None

    def forward(self, x):
        B, T, C = x.shape
        q = self.q_proj(x).view(B, T, self.n_heads, self.d_head).transpose(1, 2)
        k = self.k_proj(x).view(B, T, 1, self.d_head).transpose(1, 2)
        v = self.v_proj(x).view(B, T, 1, self.d_head).transpose(1, 2)
        self.k_cache = torch.cat([self.k_cache, k], dim=2) if self.k_cache is not None else k
        self.v_cache = torch.cat([self.v_cache, v], dim=2) if self.v_cache is not None else v
        att = F.softmax((q @ self.k_cache.transpose(-2, -1)) * self.d_head ** -0.5, dim=-1)
        return self.proj((att @ self.v_cache).transpose(1, 2).contiguous().view(B, T, C))

d_model, n_heads, T_prompt = 512, 8, 256
mha_m, mqa_m = MHADecode(d_model, n_heads), MQADecode(d_model, n_heads)
prompt = torch.randn(1, T_prompt, d_model)
mha_m(prompt); mqa_m(prompt)  # fill cache
mha_kv_mb = sum(c.numel() * 2 / 1e6 for c in [mha_m.k_cache, mha_m.v_cache])
mqa_kv_mb = sum(c.numel() * 2 / 1e6 for c in [mqa_m.k_cache, mqa_m.v_cache])
print(f'MHA KV cache: {mha_kv_mb:.2f} MB')
print(f'MQA KV cache: {mqa_kv_mb:.2f} MB  ({mha_kv_mb/mqa_kv_mb:.1f}x smaller)')
```

## Grouped Query Attention (GQA)

Grouped Query Attention (Ainslie et al. 2023) interpolates between MHA (g=h groups) and MQA (g=1 group). With g groups, g sets of K,V projections are shared across h/g query heads each. GQA achieves quality close to MHA while reducing KV cache by h/g× — a tunable quality/memory trade-off. LLaMA-2-70B uses GQA with g=8 groups and h=64 heads (8 K/V heads total, 8 query heads per K/V head). Mistral-7B uses GQA with g=8 groups, n_heads=32, n_kv_heads=8. GQA can also be obtained by mean-pooling MHA checkpoint K/V heads for post-hoc conversion.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GroupedQueryAttention(nn.Module):
    """
    GQA: n_heads query heads grouped into n_kv_heads KV groups.
    n_kv_heads=n_heads => MHA; n_kv_heads=1 => MQA.
    """
    def __init__(self, d_model=512, n_heads=8, n_kv_heads=2):
        super().__init__()
        assert n_heads % n_kv_heads == 0
        self.n_heads = n_heads
        self.n_kv_heads = n_kv_heads
        self.n_rep = n_heads // n_kv_heads  # query heads per KV group
        self.d_head = d_model // n_heads
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, n_kv_heads * self.d_head, bias=False)
        self.v_proj = nn.Linear(d_model, n_kv_heads * self.d_head, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x):
        B, T, C = x.shape
        Q = self.q_proj(x).view(B, T, self.n_heads, self.d_head).transpose(1, 2)
        K = self.k_proj(x).view(B, T, self.n_kv_heads, self.d_head).transpose(1, 2)
        V = self.v_proj(x).view(B, T, self.n_kv_heads, self.d_head).transpose(1, 2)
        # Repeat K,V for each group (interleaved)
        K = K.repeat_interleave(self.n_rep, dim=1)  # (B, n_heads, T, d_head)
        V = V.repeat_interleave(self.n_rep, dim=1)
        att = F.softmax((Q @ K.transpose(-2, -1)) * self.d_head ** -0.5, dim=-1)
        return self.out_proj((att @ V).transpose(1, 2).contiguous().view(B, T, C))

x = torch.randn(2, 32, 512)
for n_kv in [8, 4, 2, 1]:
    m = GroupedQueryAttention(512, n_heads=8, n_kv_heads=n_kv)
    label = 'MHA' if n_kv==8 else ('MQA' if n_kv==1 else 'GQA')
    kv_params = sum(p.numel() for n,p in m.named_parameters() if '_proj' in n and n[0] in 'kv')
    print(f'n_kv={n_kv} ({label}): KV params={kv_params:,}, out={m(x).shape}')
```

## Parameter Count Comparison

```python
import torch
import torch.nn as nn

def count_attention_params(d_model, n_heads, n_kv_heads, include_output=True):
    """Count parameters for Q, K, V, and output projections."""
    d_head = d_model // n_heads
    q_params = n_heads * d_model * d_head     # Q: one per head
    k_params = n_kv_heads * d_model * d_head  # K: one per KV group
    v_params = n_kv_heads * d_model * d_head  # V: one per KV group
    o_params = d_model * d_model if include_output else 0
    total = q_params + k_params + v_params + o_params
    kv_cache_per_tok = 2 * n_kv_heads * d_head  # K + V elements per token
    return total, kv_cache_per_tok

configs = [
    ('MHA  h=32 kv=32',  4096, 32, 32),
    ('GQA  h=32 kv=8',   4096, 32,  8),
    ('GQA  h=32 kv=4',   4096, 32,  4),
    ('MQA  h=32 kv=1',   4096, 32,  1),
    ('MHA  h=64 kv=64',  8192, 64, 64),
    ('GQA  h=64 kv=8',   8192, 64,  8),
    ('MQA  h=64 kv=1',   8192, 64,  1),
]

print(f'{'Config':<22} {'Params':>10} {'KV/tok':>8} {'KV Reduction':>14}')
base_kv = {4096: None, 8192: None}
for name, d, h, kv in configs:
    total, kv_per_tok = count_attention_params(d, h, kv)
    mha_kv = 2 * (d // h) * h  # MHA baseline
    reduction = mha_kv / kv_per_tok
    print(f'{name:<22} {total:>10,} {kv_per_tok:>8} {reduction:>14.1f}x')
```

## Where MQA and GQA Are Used

MQA and GQA have been widely adopted as the default in production LLMs. The quality cost of MQA (vs MHA) is measured to be less than 5% degradation on most benchmarks, while throughput gains at long sequence lengths are substantial. GQA with n_kv_heads=8 has become the dominant choice for large models, offering most of MQA's efficiency while recovering quality closer to MHA.

- PaLM (540B, 2022): MQA — one of the first large-scale deployments.
- Falcon-7B and Falcon-40B: MQA by default.
- Mistral-7B (2023): GQA with n_kv_heads=8, n_heads=32.
- LLaMA-2-70B: GQA with n_kv_heads=8, n_heads=64.
- LLaMA-3 family: GQA across all sizes (8B, 70B, 405B).
- StarCoder (15B): MQA for fast code generation inference.
- Gemma-2 and Phi-3: GQA as standard.

## Comparison: MHA vs MQA vs GQA

| Attribute | MHA | MQA | GQA (g groups) |
| --- | --- | --- | --- |
| K/V heads | h (one per query head) | 1 (shared across all) | g (g < h, shared within group) |
| KV cache size | 2 × h × T × d_head | 2 × T × d_head | 2 × g × T × d_head |
| KV cache reduction | 1× (baseline) | h× smaller | h/g× smaller |
| Inference throughput | Baseline | Up to h× faster (bandwidth bound) | Between MHA and MQA |
| Quality vs MHA | Best quality | ~1-5% drop on benchmarks | Negligible drop at g=8 |
| Parameter count | Full (Q,K,V each d²) | Q: d², K+V: 2×d×d_head | Q: d², K+V: 2g×d×d_head |
| Convert from MHA | N/A | Must retrain | Can approximate by pooling heads |

## Training Considerations

MQA and GQA must typically be trained from scratch — converting a pretrained MHA model to MQA by naively sharing K/V weights degrades quality significantly. One exception: Ainslie et al. (2023) showed that GQA can be initialized from MHA by mean-pooling the K/V heads within each group and then fine-tuning for a small fraction of pretraining compute (~5%) to recover most of the quality gap. This uptrained GQA is now used in LLaMA-2-70B, which was initialized from MHA and then converted. The fine-tuning cost is approximately 5% of the original pretraining compute.

When choosing between MHA, MQA, and GQA for a new model: for models under 7B parameters where KV cache pressure is low, MHA is safe and maximizes quality. For 7B–70B models deployed at scale with long context, GQA with g=8 is the current best practice — it cuts KV cache bandwidth by 8× with negligible quality loss. Pure MQA (g=1) is appropriate for extremely bandwidth-constrained inference (e.g., edge devices, batch size 1) where even GQA's small cache is too large.

---

