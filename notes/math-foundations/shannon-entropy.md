---
title: "Shannon Entropy"
slug: "shannon-entropy"
description: "Entropy definition, units, bounds, and its role as the information-theoretic foundation of compression and ML loss functions."
tags: ["information-theory","math","foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2hhbm5vbiBlbnRyb3B5IGlzIHRoZSBmb3VuZGF0aW9uYWwgbWVhc3VyZSBvZiB1bmNlcnRhaW50eSBpbiBpbmZvcm1hdGlvbiB0aGVvcnksIGludHJvZHVjZWQgYnkgQ2xhdWRlIFNoYW5ub24gaW4gMTk0OC4gSXQgcXVhbnRpZmllcyB0aGUgYXZlcmFnZSBudW1iZXIgb2YgYml0cyByZXF1aXJlZCB0byBlbmNvZGUgb3V0Y29tZXMgb2YgYSByYW5kb20gdmFyaWFibGUgYW5kIHNldHMgdGhlIHRoZW9yZXRpY2FsIGZsb29yIGZvciBsb3NzbGVzcyBjb21wcmVzc2lvbi4gRm9yIE1MIGFyY2hpdGVjdHMgZXZlcnkgY3Jvc3MtZW50cm9weSBsb3NzLCBwZXJwbGV4aXR5IG1ldHJpYywgYW5kIG11dHVhbCBpbmZvcm1hdGlvbiBjYWxjdWxhdGlvbiB0cmFjZXMgZGlyZWN0bHkgYmFjayB0byB0aGlzIHNpbmdsZSBmb3JtdWxhLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlZmluaXRpb24ifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIGRpc2NyZXRlIHJhbmRvbSB2YXJpYWJsZSBYIHdpdGggUE1GIHAoeCkgb3ZlciBhbHBoYWJldCBYLCBlbnRyb3B5IGlzOlxuXG5IKFgpID0gLXN1bV97eCBpbiBYfSBwKHgpIGxvZyBwKHgpID0gRVstbG9nIHAoWCldXG5cblRoZSB0ZXJtIC1sb2cgcCh4KSBpcyB0aGUgc2VsZi1pbmZvcm1hdGlvbiBvZiBldmVudCB4LiBSYXJlIGV2ZW50cyAoc21hbGwgcCkgY2FycnkgbGFyZ2Ugc2VsZi1pbmZvcm1hdGlvbjsgY2VydGFpbiBldmVudHMgY2FycnkgemVyby4gRW50cm9weSBpcyB0aGVyZWZvcmUgdGhlIGV4cGVjdGVkIHN1cnByaXNlIG9mIHRoZSBkaXN0cmlidXRpb24uIFRoZSBjb252ZW50aW9uIDAgKiBsb2cgMCA9IDAgaGFuZGxlcyB6ZXJvLXByb2JhYmlsaXR5IGV2ZW50cyAoanVzdGlmaWVkIGJ5IGNvbnRpbnVpdHkpLiJ9LAogIHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiVW5pdHMiLCJjb250ZW50IjoiQmFzZS0yIGxvZyAtPiBiaXRzLiBOYXR1cmFsIGxvZyAtPiBuYXRzLiBCYXNlLTEwIC0+IGhhcnRsZXlzLiBDb252ZXJzaW9uOiAxIG5hdCA9IGxvZzIoZSkgfj0gMS40NDI3IGJpdHMuIFB5VG9yY2ggYW5kIFRlbnNvckZsb3cgY3Jvc3NfZW50cm9weSB1c2UgbmF0dXJhbCBsb2cgaW50ZXJuYWxseSwgc28gcmF3IGxvc3MgdmFsdWVzIGFyZSBpbiBuYXRzLiBQZXJwbGV4aXR5ID0gZXhwKG5hdHMpID0gMl4oYml0cykuIEFsd2F5cyBjaGVjayB0aGUgbG9nIGJhc2Ugd2hlbiBjb21wYXJpbmcgbnVtYmVycyBhY3Jvc3MgcGFwZXJzLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJvdW5kcyBhbmQgU3BlY2lhbCBDYXNlcyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm9uLW5lZ2F0aXZpdHk6IEgoWCkgPj0gMCBhbHdheXMuIEVxdWFsaXR5IGlmZiBYIGlzIGRldGVybWluaXN0aWMgKHAoeDApPTEgZm9yIHNvbWUgeDApLlxuXG5NYXhpbXVtIGVudHJvcHk6IEgoWCkgPD0gbG9nfFh8LCBhY2hpZXZlZCB1bmlxdWVseSBieSB0aGUgdW5pZm9ybSBkaXN0cmlidXRpb24gb3ZlciBhbGwgb3V0Y29tZXMuIEZvciBhIGstY2xhc3MgY2xhc3NpZmllciB0aGUgb3V0cHV0IGVudHJvcHkgaXMgYXQgbW9zdCBsb2cyKGspIGJpdHMuXG5cbkJpbmFyeSBlbnRyb3B5IGZ1bmN0aW9uOiBGb3IgWCB+IEJlcm5vdWxsaShwKSwgSF9iKHApID0gLXAgbG9nIHAgLSAoMS1wKSBsb2coMS1wKS4gVGhpcyBjb25jYXZlLCBzeW1tZXRyaWMgZnVuY3Rpb24gcGVha3MgYXQgSF9iKDAuNSkgPSAxIGJpdCBhbmQgdmFuaXNoZXMgYXQgcCBpbiB7MCwxfS4gSXQgYXBwZWFycyBpbiB0aGUgYmluYXJ5IHN5bW1ldHJpYyBjaGFubmVsIGNhcGFjaXR5IGZvcm11bGEgQyA9IDEgLSBIX2IocCkuIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZW50cm9weV9iaXRzKHByb2JzKTpcbiAgICBcIlwiXCJTaGFubm9uIGVudHJvcHkgaW4gYml0cy4gSGFuZGxlcyAwKmxvZygwKT0wIGJ5IGNvbnZlbnRpb24uXCJcIlwiXG4gICAgcCA9IG5wLmFzYXJyYXkocHJvYnMsIGR0eXBlPW5wLmZsb2F0NjQpXG4gICAgbWFzayA9IHAgPiAwXG4gICAgcmV0dXJuIGZsb2F0KC1ucC5zdW0ocFttYXNrXSAqIG5wLmxvZzIocFttYXNrXSkpKVxuXG5kZWYgYmluYXJ5X2VudHJvcHkocCk6XG4gICAgXCJcIlwiSF9iKHApIGluIGJpdHMuXCJcIlwiXG4gICAgcCA9IG5wLmNsaXAocCwgMWUtMTUsIDEgLSAxZS0xNSlcbiAgICByZXR1cm4gZmxvYXQoLShwICogbnAubG9nMihwKSArICgxIC0gcCkgKiBucC5sb2cyKDEgLSBwKSkpXG5cbnByaW50KGVudHJvcHlfYml0cyhbMC4yNV0qNCkpICAgICAgICAgIyAyLjAgIG1heCBmb3IgNCBvdXRjb21lc1xucHJpbnQoZW50cm9weV9iaXRzKFsxLjAsMC4wLDAuMF0pKSAgICAjIDAuMCAgZGV0ZXJtaW5pc3RpY1xucHJpbnQoYmluYXJ5X2VudHJvcHkoMC41KSkgICAgICAgICAgICAjIDEuMCAgbWF4IGJpbmFyeVxucHJpbnQoYmluYXJ5X2VudHJvcHkoMC45KSkgICAgICAgICAgICAjIDAuNDY5XG5cbiMgTW9kZWwgY29uZmlkZW5jZSB2aWEgZW50cm9weVxuZGVmIHNvZnRtYXhfZW50cm9weShsb2dpdHMpOlxuICAgIGxvZ2l0cyA9IG5wLmFycmF5KGxvZ2l0cywgZHR5cGU9ZmxvYXQpXG4gICAgbG9naXRzIC09IGxvZ2l0cy5tYXgoKVxuICAgIHByb2JzID0gbnAuZXhwKGxvZ2l0cykgLyBucC5leHAobG9naXRzKS5zdW0oKVxuICAgIHJldHVybiBlbnRyb3B5X2JpdHMocHJvYnMpXG5cbnByaW50KHNvZnRtYXhfZW50cm9weShbMTAuMCwwLjAsMC4wXSkpICAgIyB+MC4wMDUgIGNvbmZpZGVudFxucHJpbnQoc29mdG1heF9lbnRyb3B5KFswLjEsMC4wLC0wLjFdKSkgICAjIH4xLjU4NSAgdW5jZXJ0YWluIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXhpb21zIFRoYXQgVW5pcXVlbHkgQ2hhcmFjdGVyaXplIEVudHJvcHkifSwKICB7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNvbnRpbnVpdHk6IEggaXMgY29udGludW91cyBpbiBhbGwgcGkg4oCUIHNtYWxsIHByb2JhYmlsaXR5IGNoYW5nZXMgZ2l2ZSBzbWFsbCBlbnRyb3B5IGNoYW5nZXMiLCJTeW1tZXRyeTogSCBpcyBpbnZhcmlhbnQgdW5kZXIgcGVybXV0YXRpb24gb2Ygb3V0Y29tZXMg4oCUIG9ubHkgcHJvYmFiaWxpdGllcyBtYXR0ZXIiLCJNYXhpbWFsaXR5OiBVbmlmb3JtIGRpc3RyaWJ1dGlvbiBtYXhpbWl6ZXMgSCBmb3IgYW55IGZpeGVkIGFscGhhYmV0IHNpemUiLCJFeHBhbnNpYmlsaXR5OiBBZGRpbmcgYW4gaW1wb3NzaWJsZSBldmVudCBsZWF2ZXMgSCB1bmNoYW5nZWQ6IEgocDEsLi4uLHBuLDApPUgocDEsLi4uLHBuKSIsIkFkZGl0aXZpdHkgKGNoYWluIHJ1bGUpOiBIKFgsWSkgPSBIKFgpICsgSChZfFgpIl19LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpZmZlcmVudGlhbCBFbnRyb3B5IGZvciBDb250aW51b3VzIERpc3RyaWJ1dGlvbnMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBjb250aW51b3VzIFggd2l0aCBkZW5zaXR5IGYoeCksIGRpZmZlcmVudGlhbCBlbnRyb3B5IGlzIGgoWCkgPSAtaW50ZWdyYWwgZih4KSBsb2cgZih4KSBkeC5cblxuS2V5IGRpc3RpbmN0aW9ucyBmcm9tIGRpc2NyZXRlIGVudHJvcHk6XG4xLiBoKFgpIGNhbiBiZSBuZWdhdGl2ZTogaChVbmlmb3JtWzAsIGVwc10pID0gbG9nKGVwcykgLT4gLWluZiBhcyBlcHMtPjAuXG4yLiBOb3QgcmVwYXJhbWV0cml6YXRpb24taW52YXJpYW50OiBoKGFYKSA9IGgoWCkgKyBsb2d8YXwuXG4zLiBPbmx5IGRpZmZlcmVuY2VzIChlLmcuIG11dHVhbCBpbmZvcm1hdGlvbikgY2FycnkgYWJzb2x1dGUgbWVhbmluZy5cblxuR2F1c3NpYW4gbWF4aW1pemVzIGggZm9yIGZpeGVkIHZhcmlhbmNlOiBoKE4obXUsIHNpZ21hXjIpKSA9IDAuNSAqIGxvZygyKnBpKmUqc2lnbWFeMikuIFRoaXMgaXMgd2h5IEdhdXNzaWFuIHByaW9ycyBhcHBlYXIgc28gb2Z0ZW4g4oCUIHRoZXkgYXJlIHRoZSBtYXhpbXVtLWVudHJvcHkgZGlzdHJpYnV0aW9ucyBnaXZlbiBhIG1lYW4gYW5kIHZhcmlhbmNlIGNvbnN0cmFpbnQuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRW50cm9weSBSYXRlIGZvciBTZXF1ZW5jZXMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIHN0YXRpb25hcnkgc3RvY2hhc3RpYyBwcm9jZXNzIFgxLCBYMiwgLi4uLCB0aGUgZW50cm9weSByYXRlIGlzOlxuXG5oID0gbGltX3tuLT5pbmZ9IEgoWDEsLi4uLFhuKSAvIG5cblxuRm9yIGkuaS5kLiBzb3VyY2VzIGggPSBIKFgxKS4gRm9yIGEgc3RhdGlvbmFyeSBNYXJrb3YgY2hhaW4gd2l0aCB0cmFuc2l0aW9uIG1hdHJpeCBQIGFuZCBzdGF0aW9uYXJ5IGRpc3RyaWJ1dGlvbiBwaTogaCA9IC1zdW1fe2ksan0gcGlfaSAqIFBfe2lqfSAqIGxvZyBQX3tpan0uXG5cbkVtcGlyaWNhbCBlbnRyb3B5IHJhdGUgb2YgRW5nbGlzaCB0ZXh0IGlzIH4xLjAtMS41IGJpdHMvY2hhcmFjdGVyLCBmYXIgYmVsb3cgdGhlIHRoZW9yZXRpY2FsIG1heGltdW0gbG9nMigyNykgfj0gNC43NSBiaXRzL2NoYXJhY3RlciwgcmVmbGVjdGluZyB0aGUgcmljaCBzdGF0aXN0aWNhbCBzdHJ1Y3R1cmUgb2YgbGFuZ3VhZ2UuIEFuIExMTSdzIHBlcnBsZXhpdHkgUFBMID0gZXhwKGNyb3NzLWVudHJvcHkpIGVzdGltYXRlcyAyXmgg4oCUIGxvd2VyIFBQTCBtZWFucyBsb3dlciBlc3RpbWF0ZWQgZW50cm9weSByYXRlIG1lYW5zIGJldHRlciBtb2RlbGluZyBvZiBzdHJ1Y3R1cmUuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2hhbm5vbidzIFNvdXJjZSBDb2RpbmcgVGhlb3JlbSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlb3JlbTogRm9yIGFueSB1bmlxdWVseSBkZWNvZGFibGUgY29kZSBmb3IgWCwgdGhlIGV4cGVjdGVkIGNvZGUgbGVuZ3RoIEwgc2F0aXNmaWVzIEwgPj0gSChYKS4gTW9yZW92ZXIsIHByZWZpeC1mcmVlIGNvZGVzIGV4aXN0IHdpdGggTCA8IEgoWCkrMS5cblxuVGhpcyBlc3RhYmxpc2hlcyBlbnRyb3B5IGFzIHRoZSBoYXJkIGxvd2VyIGJvdW5kIG9uIGxvc3NsZXNzIGNvbXByZXNzaW9uLiBDcm9zcy1lbnRyb3B5IGxvc3MgSChwX3RydWUsIHFfbW9kZWwpID0gSChwX3RydWUpICsgS0wocF90cnVlIHx8IHFfbW9kZWwpIGRlY29tcG9zZXMgaW50byBhbiBpcnJlZHVjaWJsZSBmbG9vciBIKHBfdHJ1ZSkg4oCUIHNldCBieSB0aGUgZGF0YSdzIGluaGVyZW50IHJhbmRvbW5lc3Mg4oCUIHBsdXMgdGhlIEtMIHRlcm0gdGhhdCB0cmFpbmluZyByZWR1Y2VzLiBVbmRlcnN0YW5kaW5nIHRoaXMgc3BsaXQgZXhwbGFpbnM6IHdoeSBub2lzeSBsYWJlbHMgc2V0IGEgbm9uLXplcm8gbG9zcyBmbG9vciwgd2h5IGxhYmVsIHNtb290aGluZyBpbXByb3ZlcyBjYWxpYnJhdGlvbiwgYW5kIHdoeSBwZXJmZWN0IHRyYWluaW5nIGxvc3MgaXMgaW1wb3NzaWJsZSBvbiBzdG9jaGFzdGljIGRhdGEuIn0sCiAgeyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRpc3RyaWJ1dGlvbiIsIkggKGJpdHMpIiwiTm90ZXMiXSwicm93cyI6W1siVW5pZm9ybSgyKSIsIjEuMDAiLCJGYWlyIGNvaW4iXSxbIkJlcm5vdWxsaSgwLjkpIiwiMC40NyIsIkltYmFsYW5jZWQgYmluYXJ5Il0sWyJVbmlmb3JtKDI1NikiLCI4LjAwIiwiVW5pZm9ybSBieXRlIl0sWyJVbmlmb3JtKDUwIDAwMCB2b2NhYikiLCJ+MTUuNiIsIkxMTSB0b2tlbiB1cHBlciBib3VuZCJdLFsiRW5nbGlzaCBjaGFyYWN0ZXJzIiwifjEuMC0xLjUiLCJFbXBpcmljYWwgKFNoYW5ub24gMTk1MSkiXSxbIkRldGVybWluaXN0aWMgb3V0cHV0IiwiMC4wMCIsIlBlcmZlY3QgY2VydGFpbnR5Il1dfSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQXJjaGl0ZWN0IEluc2lnaHQ6IEVudHJvcHkgRmxvb3IgaW4gVHJhaW5pbmciLCJjb250ZW50IjoiSChwX3RydWUsIHFfbW9kZWwpID0gSChwX3RydWUpICsgS0wocF90cnVlIHx8IHFfbW9kZWwpLiBUaGUgSChwX3RydWUpIHRlcm0gaXMgeW91ciBpcnJlZHVjaWJsZSBsb3NzIGZsb29yIOKAlCBubyBtb2RlbCBzaXplIG9yIHRyYWluaW5nIGR1cmF0aW9uIGNhbiBicmVhY2ggaXQuIElmIHRyYWluaW5nIGxvc3MgcGxhdGVhdXMgd2VsbCBhYm92ZSB0aGlzIGZsb29yLCB5b3UgYXJlIHVuZGVyZml0dGluZy4gSWYgdHJhaW5pbmcgbG9zcyBpcyBuZWFyIHRoZSBmbG9vciBidXQgdmFsaWRhdGlvbiBsb3NzIGlzIG11Y2ggaGlnaGVyLCB5b3UgYXJlIG92ZXJmaXR0aW5nLiBGb3Igbm9pc3ktbGFiZWwgZGF0YXNldHMsIHRoZSBmbG9vciBjYW4gYmUgc3Vic3RhbnRpYWwg4oCUIHRyYWNrIEtMKHBfdHJ1ZXx8cV9tb2RlbCkgc2VwYXJhdGVseSB0byBtZWFzdXJlIGFjdHVhbCBsZWFybmluZyBwcm9ncmVzcy4ifQpd"
---
# Shannon Entropy

Shannon entropy is the foundational measure of uncertainty in information theory, introduced by Claude Shannon in 1948. It quantifies the average number of bits required to encode outcomes of a random variable and sets the theoretical floor for lossless compression. For ML architects every cross-entropy loss, perplexity metric, and mutual information calculation traces directly back to this single formula.

## Definition

For a discrete random variable X with PMF p(x) over alphabet X, entropy is:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x) \log p(x) = \mathbb{E}[-\log p(X)]$$

The term $-\log p(x)$ is the **self-information** of event x. Rare events carry large self-information; certain events carry zero. Entropy is the expected surprise of the distribution. Convention: $0 \cdot \log 0 = 0$.

> **INFO: Units**
> Base-2 log → bits. Natural log → nats. Conversion: 1 nat ≈ 1.4427 bits. PyTorch cross_entropy uses natural log. Perplexity = exp(nats). Always check log base when comparing across papers.

## Bounds and Special Cases

- **Non-negativity:** $H(X) \geq 0$, equality iff deterministic.
- **Maximum:** $H(X) \leq \log|\mathcal{X}|$, achieved by uniform distribution.
- **Binary entropy:** $H_b(p) = -p\log p - (1-p)\log(1-p)$, peaks at 1 bit when $p=0.5$.

```python
import numpy as np

def entropy_bits(probs):
    """Shannon entropy in bits. Handles 0*log(0)=0 by convention."""
    p = np.asarray(probs, dtype=np.float64)
    mask = p > 0
    return float(-np.sum(p[mask] * np.log2(p[mask])))

def binary_entropy(p):
    """H_b(p) in bits."""
    p = np.clip(p, 1e-15, 1 - 1e-15)
    return float(-(p * np.log2(p) + (1 - p) * np.log2(1 - p)))

print(entropy_bits([0.25]*4))         # 2.0  max for 4 outcomes
print(entropy_bits([1.0,0.0,0.0]))    # 0.0  deterministic
print(binary_entropy(0.5))            # 1.0  max binary
print(binary_entropy(0.9))            # 0.469

# Model confidence via entropy
def softmax_entropy(logits):
    logits = np.array(logits, dtype=float)
    logits -= logits.max()
    probs = np.exp(logits) / np.exp(logits).sum()
    return entropy_bits(probs)

print(softmax_entropy([10.0,0.0,0.0]))   # ~0.005  confident
print(softmax_entropy([0.1,0.0,-0.1]))   # ~1.585  uncertain
```

## Axioms That Uniquely Characterize Entropy

- **Continuity:** H is continuous in all pᵢ
- **Symmetry:** H is invariant under permutation of outcomes
- **Maximality:** Uniform distribution maximizes H for fixed alphabet size
- **Expansibility:** H(p₁,...,pₙ,0) = H(p₁,...,pₙ)
- **Additivity (chain rule):** H(X,Y) = H(X) + H(Y|X)

## Differential Entropy for Continuous Distributions

For continuous X with density f(x): $h(X) = -\int f(x)\log f(x)\,dx$

Key distinctions: (1) $h(X)$ **can be negative**; (2) not reparametrization-invariant: $h(aX)=h(X)+\log|a|$; (3) only differences carry absolute meaning. Gaussian maximizes $h$ for fixed variance: $h(\mathcal{N}(\mu,\sigma^2)) = \tfrac{1}{2}\log(2\pi e\sigma^2)$.

## Entropy Rate for Sequences

$$h = \lim_{n\to\infty} \frac{H(X_1,\ldots,X_n)}{n}$$

Empirical rate for English text: ~1.0–1.5 bits/character (vs. theoretical max ~4.75). LLM perplexity PPL = exp(H(p,q)) estimates $2^h$.

## Shannon's Source Coding Theorem

For any uniquely decodable code, expected code length $L \geq H(X)$. Prefix-free codes exist with $L < H(X)+1$. The cross-entropy loss decomposition $H(p,q) = H(p) + \text{KL}(p\|q)$ reveals that training only reduces the KL term — the entropy floor $H(p)$ is irreducible.

| Distribution | H (bits) | Notes |
|---|---|---|
| Uniform(2) | 1.00 | Fair coin |
| Bernoulli(0.9) | 0.47 | Imbalanced binary |
| Uniform(256) | 8.00 | Uniform byte |
| Uniform(50 000 vocab) | ~15.6 | LLM token upper bound |
| English characters | ~1.0–1.5 | Empirical (Shannon 1951) |
| Deterministic output | 0.00 | Perfect certainty |

> **TIP: Architect Insight: Entropy Floor in Training**
> $H(p,q) = H(p) + \text{KL}(p\|q)$. The $H(p)$ term is your irreducible loss floor. Training only reduces KL. For noisy-label datasets track KL separately to measure actual learning progress.