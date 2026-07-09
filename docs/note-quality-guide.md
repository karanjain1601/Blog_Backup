# Note Quality Guide

This document captures the methodology used by the highest-quality notes in the curriculum (the Linear Algebra batch), so future note generation matches that standard.

---

## Quality Benchmark

The Linear Algebra notes set the bar. Their profile:

| Metric | Target (Linear Algebra) | Short notes (to fix) |
|---|---|---|
| File size | 18–25 KB | 11–15 KB |
| Total blocks | 20–24 | 15–17 |
| Code blocks | **3–4** | 0–1 |
| Code chars total | 1800–2900 | 0–700 |
| Tables | 1 | 0–1 |
| Callouts | 1–2 | 1 |
| H2 sections | 6–8 | 5–6 |

The single biggest differentiator: **multiple substantial code blocks** (3–4 per note, each with real working Python/NumPy/PyTorch code, imports included, 15–40 lines).

---

## Block Structure Template

Every note should follow this structure. Each numbered item = one block.

```
1.  text       — Introduction (300–500 chars): "what it is, why it matters for ML/AI"
2.  heading-2  — Core Definition
3.  text       — Mathematical definition, notation, intuition (400–600 chars)
4.  code       — Working Python/NumPy example demonstrating the concept (15–30 lines)
5.  heading-2  — Mathematical Properties / Derivation
6.  text       — Key theorem, proof sketch, or derivation (400–600 chars)
7.  code       — Second working example showing the math (15–25 lines)
8.  heading-2  — Variants / Flavors / Algorithm Steps
9.  text       — Explain 2–4 variants or the step-by-step algorithm (400–600 chars)
10. heading-2  — ML / AI Connections
11. text       — Where and why this is used in real ML systems (400–600 chars)
12. code       — Third code example: ML/PyTorch application (15–30 lines)
13. heading-2  — Implementation Considerations
14. text       — Numerical stability, hyperparameter sensitivity, pitfalls (300–500 chars)
15. heading-2  — Practical Guidance
16. text       — When to use, how to tune, what to monitor (300–500 chars)
17. code       — Fourth code example: production-style usage or debugging (10–20 lines)
18. callout    — Warning or Info: the #1 pitfall or the key insight to remember
19. table      — Summary table: variants, hyperparameters, or tradeoff comparison
20. divider
21. heading-2  — Key Takeaways
22. list       — 5–7 bullet takeaways
```

Minimum: 20 blocks. Aim for 22.

---

## Code Block Guidelines

- **Always include imports** (`import numpy as np`, `import torch`, etc.)
- **Show real computation**, not pseudo-code
- **Use appropriate libraries**: NumPy for math, scikit-learn for classical ML, PyTorch for deep learning concepts
- **Comment key lines** explaining what's happening
- **Each block should be independent** — a reader should be able to copy and run it
- **Length**: 15–40 lines per block
- **Four code blocks per note** targeting:
  1. Basic concept demonstration
  2. Mathematical property or algorithm step
  3. ML/PyTorch application
  4. Practical usage / diagnostics / debugging

### Example of a good code block

```python
import numpy as np
from numpy.linalg import svd

# Rank-2 matrix: column space is 2D even though matrix is 4x4
A = np.array([[1, 2, 3, 4],
              [2, 4, 6, 8],   # = 2 * row 0
              [1, 0, 1, 0],
              [2, 0, 2, 0]])  # = 2 * row 2

# SVD reveals the rank via number of significant singular values
U, s, Vt = svd(A)
print("Singular values:", np.round(s, 4))   # [7.07, 2.83, 0.00, 0.00]
print("Numerical rank:", np.sum(s > 1e-10)) # 2

# Null space: vectors that A maps to zero
from scipy.linalg import null_space
ns = null_space(A)
print("Null space dimension:", ns.shape[1])  # 2 (rank-nullity: 4 = 2 + 2)
```

### Example of a poor code block (too short, no imports)

```python
s = np.linalg.svd(A, compute_uv=False)
rank = (s > 1e-10).sum()
```

---

## Text Block Guidelines

- **Per-block target**: 350–600 chars
- Cover: definition, notation, intuition, edge cases, ML relevance
- Use **bold** for key terms on first mention
- Use inline math notation freely: θ = (XᵀX)⁻¹Xᵀy, σ(z) = 1/(1+e⁻ᶻ), etc.
- Do NOT just restate the heading — add substance

---

## Table Guidelines

At minimum, one table per note. Good candidates:
- Comparison of variants (e.g., L1 vs L2 vs ElasticNet)
- Hyperparameter reference (name, typical range, effect)
- Algorithm steps (step #, action, complexity)
- Tradeoffs (method, pros, cons)

---

## Callout Guidelines

Use `variant: "warning"` for the #1 pitfall/mistake.
Use `variant: "info"` for a key insight or counterintuitive fact.
Use `variant: "tip"` for a practical heuristic.

---

## Regeneration Priority

Notes below 15 KB with ≤1 code block should be regenerated with this methodology.

The short batches (from the Calculus & Optimization, Information Theory, and Numerical Methods agents):

**Calculus & Optimization** (all ≤14.9 KB): derivatives-partial-directional, gradient-jacobian-hessian, chain-rule-backpropagation, automatic-differentiation, gradient-descent, sgd-stochastic-approximation, momentum-optimization, nesterov-momentum, adam-optimizer, adamw-weight-decay, lion-optimizer, learning-rate-schedules, convex-nonconvex-landscapes, sharp-flat-minima-generalization, lagrangian-kkt-conditions, second-order-methods, gradient-clipping

**Information Theory** (≤15 KB): shannon-entropy, joint-conditional-entropy, cross-entropy-mle, kl-divergence, jensen-shannon-divergence, mutual-information, entropy-rate, perplexity-llm, noisychannel-shannons-theorem, data-processing-inequality

**Numerical Methods** (≤14.5 KB): machine-epsilon, overflow-underflow-logsumexp, numerically-stable-softmax

**Probability & Statistics** (≤14 KB): monte-carlo-methods, expectation-variance-covariance, probability-axioms-bayes, maximum-likelihood-estimation, map-estimation-regularization, importance-sampling, exponential-family
