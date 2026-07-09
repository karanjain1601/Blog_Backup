# Complete AI/ML Topic List — Architect Level
> Every topic you need to cover, organized by domain and depth. Use this as your master checklist.

---

## PHASE 1 — Mathematical Foundations

### Linear Algebra
- [ ] Vectors, matrices, tensors — shapes, broadcasting, memory layout
- [ ] Matrix multiplication as linear transformation — geometric view
- [ ] Eigenvalues and eigenvectors — PCA, stability, Markov chains
- [ ] Singular Value Decomposition (SVD) — low-rank approximation, pseudoinverse
- [ ] Norms — L0, L1, L2, L-inf, Frobenius — regularization connections
- [ ] Dot product and cosine similarity — embeddings and retrieval
- [ ] Orthogonality, projections, Gram-Schmidt process
- [ ] Positive semi-definite matrices — kernels, covariance matrices
- [ ] Tensor operations — higher-order extensions, tensor decompositions (CP, Tucker)
- [ ] Matrix calculus — derivatives of matrix expressions
- [ ] Kronecker product, Hadamard product
- [ ] Rank, nullspace, column space, row space

### Calculus & Optimization
- [ ] Derivatives, partial derivatives, directional derivatives
- [ ] Gradient, Jacobian, Hessian — definitions and computation
- [ ] Chain rule — derive backprop for every layer type by hand
- [ ] Forward-mode vs reverse-mode automatic differentiation
- [ ] Gradient descent — convergence conditions, step size, convexity
- [ ] SGD — stochastic approximation, minibatch variance
- [ ] Momentum — exponential moving average of gradients
- [ ] Nesterov momentum — lookahead correction
- [ ] Adam — adaptive learning rates, bias correction derivation
- [ ] AdamW — decoupled weight decay, why it differs from L2
- [ ] Lion optimizer — sign-based updates, memory efficiency
- [ ] Learning rate schedules — warmup, cosine annealing, cyclical, polynomial
- [ ] Convex vs non-convex loss landscapes — local minima, saddle points
- [ ] Sharp vs flat minima — generalization implications
- [ ] Lagrangian optimization — constrained problems, KKT conditions
- [ ] Second-order methods — Newton's method, L-BFGS, why rarely used in DL
- [ ] Gradient clipping — norm clipping vs value clipping

### Probability & Statistics
- [ ] Probability axioms, sigma-algebras, measure theory basics
- [ ] Conditional probability, Bayes theorem, total probability
- [ ] Common distributions — Gaussian, Bernoulli, Categorical, Dirichlet, Beta, Gamma, Poisson, Laplace
- [ ] Exponential family — natural parameters, sufficient statistics
- [ ] MLE — maximum likelihood estimation, derivation, properties
- [ ] MAP estimation — posterior mode, connection to regularization
- [ ] Expectation, variance, covariance, correlation
- [ ] Central Limit Theorem — convergence in distribution, implications for SGD
- [ ] Law of Large Numbers — weak and strong versions
- [ ] Hypothesis testing — p-values, Type I/II errors, power
- [ ] Confidence intervals — frequentist interpretation
- [ ] Bayesian inference — priors, posteriors, likelihood, evidence
- [ ] Conjugate priors — Beta-Binomial, Dirichlet-Categorical, Gaussian-Gaussian
- [ ] Variational inference — ELBO, mean-field approximation
- [ ] Monte Carlo methods — law of large numbers for integration
- [ ] Importance sampling — correcting distributional mismatch
- [ ] MCMC — Metropolis-Hastings, Gibbs sampling, mixing time
- [ ] Markov chains — steady-state distribution, ergodicity
- [ ] Bootstrap — resampling for uncertainty estimation

### Information Theory
- [ ] Shannon entropy — definition, units (bits vs nats), properties
- [ ] Joint entropy, conditional entropy, chain rule
- [ ] Cross-entropy — connection to MLE, use as loss function
- [ ] KL divergence — asymmetry, non-negativity proof, forward vs reverse
- [ ] Jensen-Shannon divergence — symmetric, bounded, connection to GANs
- [ ] Mutual information — feature selection, contrastive objectives
- [ ] Entropy rate — information in stochastic processes
- [ ] Minimum description length — Kolmogorov complexity, regularization view
- [ ] Perplexity — LLM evaluation metric, connection to entropy
- [ ] Noisy channel model — Shannon's coding theorem
- [ ] Data processing inequality — why compression can't add information
- [ ] Rate-distortion theory — lossy compression, VAE connection

### Numerical Methods & Stability
- [ ] IEEE 754 floating point — fp16, bf16, fp32, fp64 precision limits
- [ ] Machine epsilon — smallest representable difference from 1
- [ ] Overflow and underflow — log-sum-exp trick, safe implementations
- [ ] Catastrophic cancellation — when subtraction destroys precision
- [ ] Condition number — ill-conditioned vs well-conditioned systems
- [ ] Numerically stable softmax — subtract max before exponentiating
- [ ] Stable log-softmax and logsumexp implementations
- [ ] Numerical differentiation — finite differences, step size selection
- [ ] Iterative solvers — conjugate gradient, Lanczos algorithm
- [ ] Stiff ODEs — numerical integration challenges

---

## PHASE 2 — Classical Machine Learning

### Supervised Learning
- [ ] Linear regression — OLS derivation, normal equations, QR decomposition
- [ ] Bias-variance tradeoff — decomposition, underfitting vs overfitting
- [ ] Logistic regression — sigmoid derivation, MLE interpretation, coefficients
- [ ] Regularization — L1 (Lasso, sparsity), L2 (Ridge, weight decay), ElasticNet
- [ ] Regularization paths — coordinate descent, LARS algorithm
- [ ] SVMs — margin maximization, Lagrangian dual, support vectors
- [ ] Kernel trick — Mercer's theorem, implicit infinite feature maps
- [ ] Soft-margin SVM — C parameter, slack variables
- [ ] Decision trees — information gain, Gini impurity, pruning
- [ ] Bias-variance in trees — depth, leaf size, min split
- [ ] Random forests — bagging, feature subsampling, OOB error
- [ ] Feature importance — Gini importance, permutation importance, SHAP
- [ ] Gradient boosting — additive model, stage-wise fitting
- [ ] XGBoost — second-order Taylor expansion, regularized objective
- [ ] LightGBM — leaf-wise growth, histogram-based splitting
- [ ] CatBoost — ordered boosting, categorical feature handling
- [ ] k-Nearest Neighbors — curse of dimensionality, ANN (HNSW, Faiss, ScaNN)
- [ ] Naive Bayes — generative classifier, feature independence assumption
- [ ] Linear Discriminant Analysis — class-conditional Gaussians
- [ ] Bayesian linear regression — posterior over weights, predictive distribution
- [ ] Quantile regression — conditional quantile estimation, pinball loss

### Unsupervised Learning
- [ ] K-means clustering — Lloyd's algorithm, k-means++ initialization
- [ ] K-means convergence proof — monotone decrease, local optima
- [ ] Gaussian Mixture Models — EM algorithm derivation step by step
- [ ] EM algorithm — E-step, M-step, convergence to local maximum
- [ ] DBSCAN — epsilon, min_samples, core/border/noise points
- [ ] HDBSCAN — hierarchical density-based, cluster persistence
- [ ] Hierarchical clustering — single, complete, average, Ward linkage
- [ ] Spectral clustering — graph Laplacian, eigenvectors, normalized cut
- [ ] PCA — derivation from SVD, explained variance, reconstruction
- [ ] Kernel PCA — nonlinear dimensionality reduction
- [ ] t-SNE — perplexity, gradient computation, crowding problem, pitfalls
- [ ] UMAP — topological data analysis, fuzzy simplicial sets
- [ ] Autoencoders — undercomplete, denoising, sparse, contractive
- [ ] ICA — non-Gaussianity, FastICA, cocktail party problem
- [ ] Topic modeling — LDA, NMF, BTM for short texts
- [ ] Subspace methods — robust PCA, sparse PCA

### Kernel Methods & Gaussian Processes
- [ ] Reproducing Kernel Hilbert Spaces (RKHS) — feature map, inner product
- [ ] Common kernels — RBF/Gaussian, polynomial, Matérn, periodic
- [ ] Kernel composition rules — sum, product, transformation
- [ ] Kernel PCA, kernel regression, kernel SVM
- [ ] Gaussian Process definition — mean function, covariance function
- [ ] GP prior — sampling from a GP, visualizing function distributions
- [ ] GP posterior — conditioning on observations, predictive distribution
- [ ] GP hyperparameter learning — type-II MLE, marginal likelihood
- [ ] Noisy GP regression — observation noise, signal vs noise separation
- [ ] GP classification — Laplace approximation, expectation propagation
- [ ] Sparse GPs — Nyström approximation, inducing points (FITC, VFE)
- [ ] Deep kernel learning — neural network + GP
- [ ] Bayesian Optimization — surrogate model, acquisition functions
- [ ] Acquisition functions — EI (Expected Improvement), UCB, Thompson sampling, PI
- [ ] Multi-fidelity BO — cheap approximations of expensive objectives

### Anomaly Detection & Density Estimation
- [ ] Statistical methods — Z-score, modified Z-score, IQR, Grubbs test
- [ ] Mahalanobis distance — multivariate anomaly detection
- [ ] Isolation Forest — path length, random partitioning, contamination
- [ ] Local Outlier Factor (LOF) — local density comparison
- [ ] One-Class SVM — hypersphere in feature space, nu parameter
- [ ] SVDD — Support Vector Data Description
- [ ] Autoencoder reconstruction error — threshold selection, calibration
- [ ] Variational autoencoder anomaly score — ELBO-based detection
- [ ] Kernel Density Estimation (KDE) — bandwidth selection, Silverman's rule
- [ ] Normalizing flows for density — exact likelihood, high-dimensional challenges
- [ ] Energy-based models — Boltzmann distribution, MCMC sampling
- [ ] OOD detection — energy score, Mahalanobis distance, MaxSoftmax
- [ ] Deep SVDD — deep one-class classification
- [ ] Time-series anomaly detection — ARIMA residuals, LSTM reconstruction

### Time-Series ML
- [ ] Stationarity — strict vs weak, unit root tests (ADF, KPSS)
- [ ] Trend, seasonality, residual — additive vs multiplicative decomposition
- [ ] STL decomposition — seasonal-trend decomposition via LOESS
- [ ] ACF and PACF — autocorrelation function, partial ACF, model identification
- [ ] ARIMA — AR, I, MA components, Box-Jenkins methodology
- [ ] SARIMA — seasonal ARIMA, period selection
- [ ] State Space Models — Kalman filter, local level model
- [ ] Exponential smoothing — Holt-Winters, ETS models
- [ ] Feature engineering — lag features, rolling statistics, Fourier features
- [ ] Walk-forward validation — preventing data leakage through time
- [ ] Temporal train/val/test split — no random shuffling
- [ ] Multi-step forecasting — direct vs recursive vs MIMO strategies
- [ ] Temporal Convolutional Networks (TCN) — dilated causal convolutions
- [ ] Transformer-based forecasting — Informer, Autoformer, PatchTST
- [ ] N-BEATS — basis expansion for interpretable forecasting
- [ ] Time-series Foundation Models — TimesFM, Chronos, Moirai
- [ ] Probabilistic forecasting — quantile regression, conformal prediction
- [ ] Anomaly detection in streams — CUSUM, ADWIN, online methods
- [ ] Change point detection — PELT, BOCPD
- [ ] Evaluation — MAE, MAPE, SMAPE, CRPS, WQL, calibration

### Tabular Deep Learning
- [ ] Why tree models dominate tabular data — inductive bias analysis
- [ ] TabNet — attention-based feature selection for tabular data
- [ ] FT-Transformer — feature tokenization for tabular
- [ ] SAINT — self-attention and intersample attention
- [ ] TabPFN — in-context learning for small tabular datasets
- [ ] Entity embeddings — learning representations for categorical variables
- [ ] When deep learning beats gradient boosting on tabular — conditions

### Tools & Frameworks
- [ ] PyTorch — autograd, tensors, nn.Module, DataLoader, custom layers
- [ ] PyTorch internals — strides, contiguous memory, dispatch system
- [ ] torch.compile — dynamo tracing, inductor code generation
- [ ] Mixed precision — fp16/bf16, GradScaler, torch.autocast
- [ ] Scikit-learn — Pipeline, ColumnTransformer, cross_val_score
- [ ] JAX — functional transformations, jit, grad, vmap, pmap
- [ ] NumPy — broadcasting rules, vectorization, advanced indexing

---

## PHASE 3 — Deep Learning Core

### Neural Network Fundamentals
- [ ] Forward pass — linear layers, activations, loss computation
- [ ] Backward pass — derive gradients for every common layer by hand
- [ ] Activation functions — ReLU, Leaky ReLU, GELU, SiLU/Swish, Mish, sigmoid, tanh
- [ ] Dead ReLU problem — causes, mitigation (Leaky ReLU, PReLU)
- [ ] Weight initialization — Xavier/Glorot, Kaiming/He — mathematical derivation
- [ ] Batch norm — running stats, train vs eval mode, learnable gamma/beta
- [ ] Layer norm — sequence model standard, pre-norm vs post-norm placement
- [ ] RMSNorm — simplified layer norm, used in LLaMA, Gemma, Mistral
- [ ] Group norm, instance norm — when to use for small batches
- [ ] Dropout — inverted dropout, variational dropout, structured dropout
- [ ] Label smoothing — soft targets, calibration improvement
- [ ] Focal loss — hard example mining, class imbalance in detection
- [ ] Contrastive losses — triplet, NT-Xent, InfoNCE
- [ ] Vanishing gradients — mathematical cause, gradient norm monitoring
- [ ] Exploding gradients — gradient clipping (norm and value)
- [ ] Residual / skip connections — gradient highway, depth efficiency
- [ ] Universal approximation theorem — statements and limitations
- [ ] Deep vs shallow — expressivity vs optimization tradeoffs
- [ ] Lottery ticket hypothesis — sparse subnetworks that train well

### CNNs
- [ ] Convolution operation — cross-correlation, padding, stride, dilation
- [ ] 1D, 2D, 3D convolutions — applications for each
- [ ] Grouped and depthwise convolutions — MobileNet efficiency
- [ ] Transposed convolution — upsampling, checkerboard artifacts
- [ ] Receptive field — theoretical vs effective, how depth and dilation grow it
- [ ] Max pooling, average pooling, global pooling, adaptive pooling
- [ ] Spatial pyramid pooling — multi-scale feature aggregation
- [ ] AlexNet, VGG — early deep CNN architectures, lessons learned
- [ ] GoogLeNet / Inception — parallel branches, auxiliary classifiers
- [ ] ResNet — residual connections, bottleneck blocks, pre-activation variant
- [ ] DenseNet — dense connections, feature reuse, memory efficiency
- [ ] EfficientNet — compound scaling, NAS-designed architecture
- [ ] ConvNeXt — modernized CNN matching ViT performance
- [ ] Deformable convolutions — learned geometric offsets
- [ ] Transfer learning — feature extraction vs fine-tuning strategies
- [ ] Data augmentation — flips, crops, color jitter, CutMix, MixUp, RandAugment

### RNNs & Sequence Models
- [ ] Recurrent computation — hidden state, weight sharing across time
- [ ] Backpropagation through time (BPTT) — unrolling, gradient computation
- [ ] Truncated BPTT — practical approximation for long sequences
- [ ] Vanishing gradient in RNNs — why it happens, mathematical derivation
- [ ] LSTM — forget gate, input gate, output gate, cell state
- [ ] LSTM gradient flow — how gates solve vanishing gradient
- [ ] GRU — reset and update gates, when to prefer over LSTM
- [ ] Bidirectional RNNs — forward and backward pass concatenation
- [ ] Multi-layer RNNs — depth in sequence models
- [ ] Seq2Seq — encoder, decoder, attention bridging
- [ ] Bahdanau attention — additive attention, alignment model
- [ ] Luong attention — multiplicative attention, dot-product variant
- [ ] S4 — structured state space model, HiPPO initialization
- [ ] Mamba — selective state space, input-dependent SSM, hardware efficiency
- [ ] RetNet — retention mechanism, parallel and recurrent modes

### The Transformer
- [ ] Scaled dot-product attention — QKV projections, softmax, sqrt(d) scaling
- [ ] Multi-head attention — parallel heads, concatenation, output projection
- [ ] Why multiple heads — different attention patterns, subspace specialization
- [ ] Self-attention vs cross-attention — encoder-decoder difference
- [ ] Positional encoding — sinusoidal derivation, why it works
- [ ] Learned positional embeddings — BERT approach, pros and cons
- [ ] Relative positional encodings — Shaw, T5 bias, relative attention
- [ ] RoPE — rotary positional embeddings, rotation matrices in complex space
- [ ] ALiBi — attention with linear biases, length extrapolation
- [ ] NoPE — no positional encoding (some long-context models)
- [ ] Causal masking — autoregressive training, upper-triangular mask
- [ ] Padding mask — handling variable-length sequences in batches
- [ ] Pre-norm vs post-norm — stability, gradient flow differences
- [ ] Feed-forward sublayer — two linear layers, 4x expansion, role
- [ ] SwiGLU — gated linear unit activation in FFN, LLaMA FFN variant
- [ ] Encoder-only (BERT) — masked language modeling, bidirectional context
- [ ] Decoder-only (GPT) — causal language modeling, autoregressive generation
- [ ] Encoder-decoder (T5, BART) — when to use, cross-attention
- [ ] Transformer scaling — depth, width, heads — empirical behavior
- [ ] Flash Attention 1/2/3 — IO-aware, tiling, no O(n^2) materialization
- [ ] Multi-Query Attention (MQA) — shared K/V heads, memory reduction
- [ ] Grouped Query Attention (GQA) — trade-off between MHA and MQA
- [ ] Multi-head Latent Attention (MLA) — DeepSeek KV compression
- [ ] Sparse attention — Longformer sliding window + global, BigBird
- [ ] Linear attention — kernel feature maps, O(n) complexity, limitations
- [ ] Ring attention — distributed attention across devices, extreme context

### Generative Models
- [ ] Autoregressive models — PixelCNN, WaveNet, language models
- [ ] VAE — ELBO derivation from Jensen, reparameterization trick
- [ ] Beta-VAE — disentanglement, rate-distortion perspective
- [ ] VQ-VAE — discrete codebook, commitment loss, straight-through estimator
- [ ] VQ-VAE-2 — hierarchical discrete latents, top-down prior
- [ ] GANs — minimax game, Nash equilibrium, Jensen-Shannon divergence connection
- [ ] DCGAN — deep convolutional GAN best practices
- [ ] Wasserstein GAN — Earth Mover distance, Lipschitz constraint
- [ ] WGAN-GP — gradient penalty for Lipschitz, improved training
- [ ] StyleGAN 1/2/3 — style-based generator, mapping network, progressive growing
- [ ] Conditional GAN — label conditioning, cGAN
- [ ] Pix2Pix — image-to-image translation with paired data
- [ ] CycleGAN — unpaired translation, cycle consistency loss
- [ ] GAN evaluation — FID, IS, Precision and Recall metrics
- [ ] Normalizing flows — change of variables, Jacobian determinant
- [ ] RealNVP — coupling layers, affine transformations
- [ ] Glow — 1x1 invertible convolutions, multiscale architecture
- [ ] MAF/IAF — masked autoregressive flows, trade-offs between them
- [ ] Neural ODEs — continuous normalizing flows, adjoint method
- [ ] DDPM — forward process, reverse process, denoising objective
- [ ] DDPM loss derivation — simplified to predict noise, full derivation
- [ ] Score matching — Stein score function, denoising score matching
- [ ] DDIM — deterministic sampling, ODE interpretation, step skipping
- [ ] Classifier guidance — external classifier gradient, quality vs diversity
- [ ] Classifier-free guidance — joint conditional/unconditional training, CFG scale
- [ ] Latent diffusion — VAE encoder/decoder, diffuse in latent space
- [ ] Stable Diffusion architecture — UNet, CLIP text encoder, VAE
- [ ] Flow matching — optimal transport paths, simpler training than DDPM
- [ ] Consistency models — single-step generation via distillation
- [ ] DiT — Diffusion Transformers, replacing UNet with ViT, scaling
- [ ] Energy-based models — Boltzmann distribution, contrastive divergence

### Self-Supervised & Representation Learning
- [ ] SimCLR — contrastive, augmentation-based, NT-Xent loss
- [ ] MoCo — momentum encoder, memory queue for negatives
- [ ] BYOL — no negatives, online and target network, stop-gradient
- [ ] SimSiam — simplified BYOL, predictor MLP prevents collapse
- [ ] Barlow Twins — redundancy reduction, cross-correlation matrix
- [ ] VICReg — variance, invariance, covariance regularization
- [ ] MAE — masked autoencoder, high mask ratio, ViT encoder
- [ ] BEiT — discrete visual tokens as targets for masked prediction
- [ ] DINO — self-distillation with no labels, emerging segmentation features
- [ ] DINOv2 — curated data, distillation, strong universal features
- [ ] JEPA — predict representations not pixels, LeCun's proposed direction
- [ ] Uniformity and alignment — two axes of good representations
- [ ] Downstream evaluation — linear probe, k-NN probe, fine-tuning

### Knowledge Distillation & Compression
- [ ] Hinton distillation — soft targets, temperature parameter, dark knowledge
- [ ] Feature map distillation — intermediate layer matching losses
- [ ] Attention transfer — matching attention maps between teacher and student
- [ ] Born-again networks — same-size distillation for ensemble benefits
- [ ] Data-free distillation — synthesizing data from teacher for student training
- [ ] Unstructured pruning — magnitude-based, gradient-based
- [ ] Lottery ticket hypothesis — winning tickets, iterative magnitude pruning
- [ ] Structured pruning — head pruning, layer dropping, channel pruning
- [ ] Movement pruning — fine-tuning then pruning, L0 regularization
- [ ] N:M structured sparsity — 2:4 sparsity for Ampere GPU acceleration
- [ ] Neural Architecture Search (NAS) — RL-based, gradient-based (DARTS)
- [ ] Once-for-all network — train once, deploy many architectures
- [ ] DistilBERT, TinyBERT — practical LLM distillation recipes

---

## PHASE 4 — Large Language Models

### Tokenization
- [ ] Byte-Pair Encoding (BPE) — merge algorithm, vocabulary building
- [ ] SentencePiece — unigram language model tokenizer, byte fallback
- [ ] WordPiece — BERT tokenizer, likelihood-based subword selection
- [ ] Tiktoken — byte-level BPE, GPT-3/4 tokenizer
- [ ] Vocabulary size tradeoffs — fertility, embedding table size, coverage
- [ ] Byte-level tokenization — no UNK token, handles any Unicode
- [ ] Multilingual tokenization — token fertility across scripts
- [ ] Code tokenization — whitespace, indentation, special symbols
- [ ] Special tokens — BOS, EOS, PAD, SEP, MASK, instruction format tokens
- [ ] Tokenizer-free models — byte-level or character-level approaches

### Pre-Training
- [ ] Causal language modeling — next-token prediction, shifted targets
- [ ] Masked language modeling — BERT-style, 15% masking, [MASK] token
- [ ] Prefix language modeling — T5 span corruption, mixture of objectives
- [ ] Common Crawl processing — filtering, deduplication, quality scoring
- [ ] Deduplication — MinHash LSH, exact dedup, near-dedup
- [ ] Data mixing ratios — domain weights, curriculum ablations
- [ ] Scaling laws (Kaplan 2020) — power law, compute-optimal prediction
- [ ] Chinchilla scaling laws — token:parameter ratio, 20x tokens per param
- [ ] Beyond Chinchilla — inference-aware training, LLaMA compute efficiency
- [ ] RoPE positional encoding — rotary embeddings, complex number view
- [ ] SwiGLU activation — gated MLP in Transformers
- [ ] GQA — grouped query attention, KV cache reduction
- [ ] RMSNorm — simplified normalization, no mean subtraction
- [ ] Training dynamics — warmup, loss spikes, gradient norm monitoring
- [ ] Data contamination — benchmark leakage, decontamination
- [ ] Pretraining on code — code understanding, math reasoning benefits
- [ ] Multi-epoch training — data repetition effects, scaling
- [ ] Sequence packing — concatenating short sequences, attention masking

### Post-Training
- [ ] Supervised Fine-Tuning (SFT) — instruction format, conversation templates
- [ ] Data quality for SFT — filtering, diversity, instruction complexity
- [ ] Reward modeling — Bradley-Terry model, pairwise preference data
- [ ] PPO for RLHF — policy, value network, reference model, KL penalty
- [ ] RLHF instability — reward hacking, KL coefficient tuning
- [ ] DPO — Direct Preference Optimization, implicit reward, no RL loop
- [ ] IPO — Identity Preference Optimization, overcomes DPO pitfalls
- [ ] ORPO — odds ratio preference optimization, no reference model
- [ ] SimPO — simple preference optimization, length-normalized rewards
- [ ] KTO — Kahneman-Tversky Optimization, unpaired preferences
- [ ] Constitutional AI — principles-based self-critique, revision
- [ ] RLAIF — AI labeler replacing human annotators
- [ ] Scalable oversight — debate, amplification, recursive reward modeling
- [ ] Rejection sampling fine-tuning — generate N completions, keep best
- [ ] Iterative DPO — online preference learning, self-generated pairs
- [ ] Chat templates — system/user/assistant format, tokenizer integration

### Parameter-Efficient Fine-Tuning
- [ ] LoRA — low-rank AB decomposition, rank selection, target modules
- [ ] QLoRA — 4-bit NF4 quantization + LoRA, double quantization
- [ ] DoRA — weight-decomposed LoRA, magnitude + direction
- [ ] LoRA+ — different learning rates for A and B matrices
- [ ] VeRA — vector-based random matrix adaptation
- [ ] Prefix tuning — prepend virtual tokens to each layer's KV
- [ ] Prompt tuning — soft prompts only at input, scale-dependent
- [ ] Adapter layers — bottleneck FFN modules between Transformer layers
- [ ] IA3 — learned rescaling of K, V, FFN activations
- [ ] Adapter merging — TIES merging, DARE, model soup
- [ ] Task arithmetic — adding and negating fine-tuned weight deltas
- [ ] When to use each — data size, task type, inference constraints

### Quantization
- [ ] Post-Training Quantization (PTQ) — INT8, INT4, FP8
- [ ] GPTQ — one-shot weight quantization using Hessian information
- [ ] AWQ — activation-aware weight quantization, salient weight protection
- [ ] GGUF — llama.cpp format, k-quant variants for CPU inference
- [ ] Quantization-Aware Training (QAT) — fake quantization in forward pass
- [ ] Calibration data — representative samples for PTQ accuracy
- [ ] Mixed-precision quantization — sensitivity analysis, keeping fragile layers fp16
- [ ] KV cache quantization — reducing memory of cached keys and values
- [ ] Perplexity as quantization quality metric

### Inference Optimization
- [ ] KV cache — computation reuse, memory footprint per token per layer
- [ ] Paged attention — virtual memory for KV cache, vLLM implementation
- [ ] Continuous batching — dynamic request scheduling, no padding waste
- [ ] Speculative decoding — draft model, parallel verification, rejection sampling
- [ ] Prompt caching — prefix matching across requests, hash-based lookup
- [ ] Flash Attention — IO-aware, tiling over SRAM, backward pass
- [ ] Tensor parallelism for inference — Megatron column/row splitting
- [ ] Pipeline parallelism for inference — layer-wise distribution
- [ ] Disaggregated prefill/decode — separate GPUs for each phase
- [ ] Batched speculative decoding — speculative decoding at batch level
- [ ] Medusa — multiple speculative heads on same model
- [ ] Cost modeling — tokens/sec, GPU utilization, cost per million tokens

### Long Context
- [ ] RoPE linear scaling — interpolating positions beyond training length
- [ ] NTK-aware RoPE scaling — base frequency adjustment
- [ ] YaRN — yet another RoPE extension, dynamic scaling + attention temperature
- [ ] Positional interpolation (PI) — LongRoPE, fine-tuning at longer lengths
- [ ] ALiBi — attention linear biases, zero-shot length generalization
- [ ] Attention sinks — first token accumulation, StreamingLLM observation
- [ ] StreamingLLM — attention sink retention + sliding window for infinite context
- [ ] LongLoRA — efficient long-context fine-tuning with sparse attention
- [ ] Retrieval vs long context — latency and cost comparison at scale

### Architecture Variants
- [ ] MoE — Mixture of Experts, sparse routing, top-k selection
- [ ] MoE load balancing — auxiliary loss, jitter noise, expert capacity
- [ ] Fine-grained MoE — many tiny experts, DeepSeek-V3 approach
- [ ] Shared experts — always-active plus sparse experts
- [ ] Mamba in LLMs — hybrid Mamba+Attention, Jamba, Zamba
- [ ] RWKV — receptance weighted key value, linear attention recurrence
- [ ] State Space Language Models — Hyena, H3, Griffin

### Prompting & Structured Output
- [ ] Zero-shot, one-shot, few-shot — when and why each helps
- [ ] Chain-of-Thought — scratchpad reasoning, why it helps accuracy
- [ ] Zero-shot CoT — "let's think step by step" effect
- [ ] Least-to-most prompting — decompose then solve subproblems
- [ ] Self-consistency — sample multiple CoT paths, majority vote
- [ ] Tree of Thoughts — branching reasoning, evaluate and backtrack
- [ ] System prompt design — persona, constraints, output format
- [ ] Structured output — JSON mode, constrained decoding (Outlines, guidance)
- [ ] Grammar-based decoding — CFG-guided token sampling
- [ ] Prompt injection — direct and indirect attack vectors
- [ ] Prompt caching design — prefix engineering for cost reduction
- [ ] Prompt versioning and A/B testing — treat prompts as code

### RAG & Retrieval
- [ ] Dense retrieval — bi-encoder, contrastive training, FAISS indexing
- [ ] BM25 — TF-IDF, term saturation, field weighting
- [ ] Hybrid search — dense + sparse, Reciprocal Rank Fusion (RRF)
- [ ] Chunking strategies — fixed, recursive, semantic, late chunking
- [ ] Reranking — cross-encoder, ColBERT, Cohere Rerank
- [ ] HyDE — Hypothetical Document Embeddings, generate then retrieve
- [ ] FLARE — forward-looking active retrieval, retrieve when uncertain
- [ ] GraphRAG — knowledge graph extraction + community summaries
- [ ] Multi-hop reasoning — iterative retrieval for complex questions
- [ ] RAG evaluation — RAGAS: context precision, faithfulness, answer relevance
- [ ] Vector databases — Qdrant, Weaviate, Pinecone, pgvector — internals

### Test-Time Compute
- [ ] Inference-time scaling — compute vs accuracy tradeoffs
- [ ] Extended chain-of-thought — thinking tokens, o1/o3 style
- [ ] Process Reward Models (PRM) — step-level reward, verification
- [ ] Outcome Reward Models (ORM) — final answer reward
- [ ] MCTS for LLMs — Monte Carlo Tree Search over reasoning steps
- [ ] Best-of-N sampling — generate multiple, score with reward model
- [ ] DeepSeek-R1 — pure RL to learn reasoning, no supervised CoT
- [ ] Thinking budget — controlling compute allocation at inference
- [ ] Reward model as verifier — math and code verification

### LLM Security
- [ ] Prompt injection — system prompt leakage, instruction hijacking
- [ ] Indirect injection — malicious content in retrieved documents
- [ ] Jailbreaking — many-shot, roleplay, suffix attacks, DAN variants
- [ ] GCG — greedy coordinate gradient, white-box adversarial suffix
- [ ] Data poisoning — backdoor triggers in pretraining data
- [ ] Model extraction — replicating capabilities via API queries
- [ ] Membership inference — detecting training data presence
- [ ] Watermarking — green/red token lists, KGW scheme, cryptographic
- [ ] Output filtering — classifier-based, rule-based content moderation
- [ ] System-level defenses — sandboxing, privilege separation

---

## PHASE 5 — Computer Vision

### Vision Transformers & Backbones
- [ ] ViT — patch tokenization, CLS token, sinusoidal 2D positional encoding
- [ ] ViT pretraining — supervised ImageNet, MAE self-supervised, DINO
- [ ] DeiT — data-efficient ViT, distillation token
- [ ] Swin Transformer — shifted windows, hierarchical features, local attention
- [ ] PVT — pyramid vision Transformer, spatial reduction attention
- [ ] ConvNeXt — CNN modernized to match ViT, depthwise conv, LN
- [ ] MaxViT — multi-axis attention, global + local
- [ ] DINOv2 — curated pretraining, strong universal visual features
- [ ] EVA — exploring limits of masked visual pretraining
- [ ] Scaling ViTs — ViT-L/H/G/22B, scaling laws for vision

### Object Detection
- [ ] Anchor-based two-stage — Faster R-CNN, FPN, RoI align
- [ ] Anchor-based one-stage — SSD, RetinaNet, focal loss
- [ ] Anchor-free one-stage — FCOS, CenterNet, ATSS
- [ ] DETR — bipartite matching, Hungarian algorithm, set prediction
- [ ] Deformable DETR — multi-scale deformable attention, faster convergence
- [ ] Co-DETR — collaborative training, multiple auxiliary heads
- [ ] YOLO family — YOLOv1 through YOLOv11, speed-accuracy evolution
- [ ] DINO (detection) — improved DETR with contrastive denoising
- [ ] RT-DETR — real-time detection Transformer, efficient encoder

### Segmentation
- [ ] Semantic segmentation — FCN, DeepLab variants, dilated convolutions
- [ ] DeepLab v3+ — ASPP, encoder-decoder, separable convolutions
- [ ] Instance segmentation — Mask R-CNN, SOLO, QueryInst
- [ ] Panoptic segmentation — Panoptic FPN, Panoptic SegFormer
- [ ] SAM — Segment Anything, prompt-based, promptable segmentation
- [ ] SAM 2 — video object segmentation extension
- [ ] Open-vocabulary segmentation — CLIP-based, FC-CLIP, CAT-Seg
- [ ] Referring expression segmentation — language-guided segmentation

### Self-Supervised Vision
- [ ] MoCo v1/v2/v3 — momentum encoder, queue, ViT compatible
- [ ] SimCLR v1/v2 — projection head, large batches
- [ ] BYOL — exponential moving average teacher, no negatives
- [ ] SwAV — online clustering, prototype assignment
- [ ] MAE — high-ratio masking, asymmetric encoder-decoder
- [ ] BEiT, BEiT v2 — discrete tokens as prediction targets
- [ ] DINO, DINOv2 — self-distillation, patch-level features
- [ ] CLIP — contrastive image-text, zero-shot transfer

### Video Understanding
- [ ] Optical flow — Lucas-Kanade, Horn-Schunck, FlowNet, RAFT
- [ ] 3D CNN — C3D, I3D — inflating 2D operations into space-time
- [ ] Slow-Fast networks — dual-pathway: slow spatial + fast temporal
- [ ] Two-stream networks — RGB + optical flow fusion
- [ ] Video Swin Transformer — 3D shifted windows
- [ ] TimeSformer — divided space-time attention
- [ ] VideoMAE — masked autoencoder for video
- [ ] Action recognition — Kinetics-400/600, Something-Something
- [ ] Temporal action localization — boundary detection, ActionFormer
- [ ] Video object segmentation — STCN, XMem, cutie
- [ ] Video generation — Sora, CogVideoX, Open-Sora, video diffusion

### 3D Vision
- [ ] Monocular depth estimation — MiDaS, DepthAnything, ZoeDepth
- [ ] Stereo depth — SGM, RAFT-Stereo, neural cost volumes
- [ ] Point cloud processing — PointNet, PointNet++, DGCNN
- [ ] 3D object detection — VoxelNet, PointPillars, CenterPoint (LiDAR)
- [ ] Voxel representations — 3D CNNs on voxels
- [ ] Implicit neural representations — occupancy networks, SDF networks
- [ ] NeRF — volume rendering integral, positional encoding, hierarchical sampling
- [ ] NeRF extensions — Instant-NGP, Mip-NeRF, NeRF-W for in-the-wild
- [ ] 3D Gaussian Splatting — explicit, differentiable rasterization, editing
- [ ] Dynamic 3DGS — deformation fields, 4D Gaussians
- [ ] 3D generation — Zero-1-to-3, DreamFusion, SyncDreamer, One-2-3-45
- [ ] Multi-view stereo — classical MVS, MVSNet, learning-based
- [ ] Human body estimation — SMPL, HMR, 3D pose estimation

### Generative Vision
- [ ] Text-to-image — Stable Diffusion (v1, v2, XL, v3), DALL-E 3, Flux.1
- [ ] Image editing — SDEdit, Prompt2Prompt, InstructPix2Pix
- [ ] Inpainting — masked diffusion, LaMa, Paint-by-Example
- [ ] Super-resolution — ESRGAN, Real-ESRGAN, diffusion SR
- [ ] ControlNet — spatial conditioning (edges, depth, skeleton, segmentation)
- [ ] T2I-Adapter — lightweight conditioning adapters
- [ ] IP-Adapter — image prompt via decoupled cross-attention
- [ ] DreamBooth — few-shot concept personalization
- [ ] LoRA for image generation — style and content fine-tuning
- [ ] Image generation evaluation — FID, IS, CLIP score, HPSv2, human ELO

### Medical & Scientific Imaging
- [ ] Radiology — chest X-ray, CT, MRI modality differences
- [ ] Histopathology — WSI gigapixel images, patch extraction, MIL
- [ ] nnU-Net — self-configuring medical segmentation pipeline
- [ ] MedSAM — SAM adapted for medical image segmentation
- [ ] Pathology foundation models — PLIP, CONCH, UNI, Prov-GigaPath
- [ ] Radiology VLMs — CheXagent, LLaVA-Med, report generation
- [ ] Microscopy — cell segmentation, CellPose, StarDist
- [ ] Retinal imaging — fundus, OCT, diabetic retinopathy screening
- [ ] Domain shift in medical — staining variation, scanner differences
- [ ] Label-efficient medical AI — active learning, semi-supervised

---

## PHASE 6 — NLP (Deep)

### Linguistic Foundations
- [ ] Morphology — inflection, derivation, stemming, lemmatization
- [ ] Syntax — constituency parse trees, dependency graphs, head-dependent
- [ ] Semantics — lexical semantics, compositional semantics, logic forms
- [ ] Discourse — coherence, cohesion, reference chains
- [ ] Pragmatics — implicature, presupposition, speech acts
- [ ] Named Entity Recognition — BIO/BIOES tagging, nested, fine-grained
- [ ] Part-of-Speech tagging — Penn Treebank tags, universal POS
- [ ] Dependency parsing — graph-based, transition-based (arc-eager)
- [ ] Coreference resolution — mention detection, antecedent scoring
- [ ] Semantic Role Labeling — PropBank arguments, FrameNet frames
- [ ] Relation extraction — distant supervision, DocRE
- [ ] Event extraction — triggers, arguments, schemas

### Core NLP Tasks
- [ ] Text classification — fine-tuning BERT, prompting LLMs, data augmentation
- [ ] Sentiment analysis — aspect-level, fine-grained, opinion mining
- [ ] Question answering — extractive (SQuAD), abstractive, open-domain
- [ ] Machine reading comprehension — evidence retrieval + answer extraction
- [ ] Natural language inference (NLI) — entailment, contradiction, neutral
- [ ] Semantic textual similarity — sentence embeddings, bi-encoder training
- [ ] Text summarization — extractive, abstractive, faithfulness constraints
- [ ] Machine translation — encoder-decoder, beam search, back-translation
- [ ] Dialogue systems — task-oriented, open-domain, state tracking
- [ ] Commonsense reasoning — Winogrande, HellaSwag, CommonsenseQA
- [ ] Math reasoning — GSM8K, MATH, chain-of-thought, tool-augmented

### Text Representation
- [ ] Word2Vec — CBOW, skip-gram, negative sampling
- [ ] GloVe — global co-occurrence statistics, factorization
- [ ] FastText — subword n-grams, OOV handling
- [ ] ELMo — contextual embeddings, biLM, character CNN
- [ ] BERT — MLM + NSP pretraining, WordPiece, [CLS] classification
- [ ] RoBERTa — BERT improvements: no NSP, dynamic masking, more data
- [ ] DeBERTa — disentangled attention, enhanced mask decoder
- [ ] Sentence-BERT — siamese network, cosine similarity fine-tuning
- [ ] E5, BGE, GTE — modern embedding models for retrieval
- [ ] Matryoshka Representation Learning — nested subvector embeddings

### Multilingual NLP
- [ ] mBERT — multilingual BERT, cross-lingual transfer without fine-tuning
- [ ] XLM — cross-lingual LM, translation language modeling
- [ ] XLM-R — RoBERTa scale multilingual, 100 languages
- [ ] mT5 — multilingual T5, span corruption, all languages
- [ ] BLOOM, mGPT — multilingual autoregressive LLMs
- [ ] Zero-shot cross-lingual transfer — language-agnostic representations
- [ ] Few-shot multilingual — translate-then-fine-tune, cross-lingual prompting
- [ ] Low-resource NLP — data augmentation, back-translation, cross-lingual transfer
- [ ] Machine translation quality estimation — without reference translation

### Information Retrieval
- [ ] Boolean retrieval — inverted index, posting lists
- [ ] TF-IDF — term frequency, inverse document frequency, variations
- [ ] BM25 — probabilistic retrieval, term saturation, field length norm
- [ ] Dense retrieval — DPR, bi-encoder architecture, contrastive training
- [ ] ColBERT — late interaction, per-token matching efficiency
- [ ] SPLADE — sparse learned representation, BERT-based sparse retrieval
- [ ] Hybrid search — dense + sparse, RRF fusion, learned fusion
- [ ] Re-ranking — cross-encoder, pairwise scoring, listwise ranking
- [ ] Neural IR evaluation — BEIR benchmark, nDCG, MRR, Recall@K
- [ ] Query understanding — query expansion, reformulation
- [ ] Knowledge graphs — entity linking, graph completion, embedding

---

## PHASE 7 — Speech & Audio

### Audio Signal Processing
- [ ] Digital audio — sampling rate, Nyquist theorem, bit depth
- [ ] Fourier transform — DFT, FFT, time-frequency uncertainty
- [ ] Short-Time Fourier Transform (STFT) — window, hop length, spectrogram
- [ ] Mel scale — perceptual frequency warping
- [ ] Mel spectrogram — filterbank, log compression
- [ ] MFCC — cepstral analysis, delta/delta-delta features
- [ ] Pitch estimation — autocorrelation, YIN, PYIN, CREPE neural
- [ ] Voice activity detection (VAD) — energy, spectral, neural
- [ ] Noise robustness — spectral subtraction, Wiener filter, learned
- [ ] Neural audio codecs — EnCodec (RVQ-VAE), DAC, SoundStream

### Automatic Speech Recognition
- [ ] CTC — blank token, prefix beam search, CTC loss derivation
- [ ] RNN-T — transducer, streaming capable, blank prediction
- [ ] Attention-based encoder-decoder — LAS (Listen-Attend-Spell)
- [ ] Wav2Vec 2.0 — contrastive pretraining, quantized speech units
- [ ] HuBERT — offline k-means targets, masked prediction
- [ ] Whisper — web-scale weak supervision, multilingual, multitask
- [ ] Conformer — convolutional augmented Transformer for ASR
- [ ] Language model fusion — shallow fusion, deep fusion, cold fusion
- [ ] CTC beam search with LM — prefix beam search with n-gram LM
- [ ] End-to-end vs modular ASR — tradeoffs in production
- [ ] Streaming ASR — chunk-based, look-ahead, CIF mechanism
- [ ] ASR evaluation — WER, CER, word-level error breakdown
- [ ] Domain adaptation for ASR — acoustic and language model adaptation

### Text-to-Speech
- [ ] Text normalization — numbers, dates, abbreviations, heteronyms
- [ ] G2P — grapheme-to-phoneme, pronunciation dictionary, neural G2P
- [ ] Tacotron 2 — attention-based mel synthesis, WaveNet vocoder
- [ ] FastSpeech 1/2 — non-autoregressive, duration predictor, variance adaptor
- [ ] VITS — end-to-end TTS combining VAE, flow, GAN
- [ ] Voicebox — flow matching, fill-in-the-middle, any-context TTS
- [ ] VALL-E — codec language model, few-shot voice cloning
- [ ] SoundStorm — parallel decoding for efficient audio generation
- [ ] Natural Speech 2/3 — diffusion-based TTS, in-context learning
- [ ] Vocoders — WaveNet, WaveGlow, HiFi-GAN, BigVGAN
- [ ] Voice cloning — speaker embedding, few-shot adaptation
- [ ] Emotion and prosody control — style tokens, GST, reference audio
- [ ] TTS evaluation — MOS, UTMOS neural MOS predictor, PESQ

### Speaker & Audio Understanding
- [ ] Speaker verification — d-vector, x-vector, ECAPA-TDNN, RawNet
- [ ] Speaker identification — closed-set vs open-set recognition
- [ ] Speaker diarization — EEND-EDA, clustering-based, pyannote.audio
- [ ] Overlapping speech — separation, diarization with overlap
- [ ] Audio event detection — SED, AudioSet, PANNs, BEATs
- [ ] Environmental sound classification — ESC-50, UrbanSound8K
- [ ] Music information retrieval — genre, key, tempo, chord, beat
- [ ] Music source separation — Open-Unmix, Demucs, HTDemucs
- [ ] Music generation — MusicGen, AudioCraft, MusicLM
- [ ] Voice conversion — any-to-any VC, kNN-VC, DiffVC
- [ ] Speech enhancement — denoising, dereverberation, beamforming
- [ ] Audio question answering — AudioQA, SALMONN

---

## PHASE 8 — Multimodal AI

### Vision-Language Models
- [ ] CLIP — contrastive pretraining, image-text pairs, zero-shot transfer
- [ ] ALIGN — noisy image-text pairs at billion scale
- [ ] BLIP — bootstrapping language-image pretraining, CapFilt
- [ ] BLIP-2 — frozen image encoder + LLM, Q-Former bridge
- [ ] Flamingo — interleaved image-text, cross-attention into frozen LLM
- [ ] LLaVA 1/1.5/NeXT — linear projection, visual instruction tuning
- [ ] InstructBLIP — task-specific instruction fine-tuning
- [ ] MiniGPT-4 — BLIP-2 + Vicuna, efficient alignment
- [ ] InternVL — scaling vision encoder with LLM co-training
- [ ] Qwen-VL — native resolution, multi-task visual understanding
- [ ] Phi-3 Vision — small but capable VLM, CLIP + Phi-3
- [ ] GPT-4V / Claude Vision / Gemini Vision — capability benchmarking
- [ ] Open-vocabulary detection — GDINO, OWL-ViT, OWLv2
- [ ] Referring image segmentation — language-guided masks
- [ ] Visual grounding — region-level understanding, REC

### Video-Language Models
- [ ] VideoCLIP — video-text contrastive learning
- [ ] CLIP4Clip — adapting CLIP for video retrieval
- [ ] VideoLLaMA — video understanding with LLM
- [ ] Video-LLaVA — unified visual representation for video
- [ ] InternVideo — video foundation model, multi-task
- [ ] Video question answering — ActivityNet-QA, MSVD-QA
- [ ] Temporal grounding — video moment retrieval, NLQ
- [ ] Video captioning — dense captioning, event localization

### Audio-Language & Omni Models
- [ ] SALMONN — speech audio language music open neural network
- [ ] Qwen-Audio — audio understanding with LLM
- [ ] LTU — listen, think, understand audio LLM
- [ ] Pengi — audio language model with task prefix
- [ ] GPT-4o speech mode — end-to-end speech LLM
- [ ] Moshi — real-time speech-to-speech LLM
- [ ] AnyGPT — any-to-any LLM with multimodal tokenization
- [ ] Unified-IO — unified input-output across modalities

### Document AI
- [ ] Document layout analysis — LayoutParser, Detectron2 for documents
- [ ] LayoutLM 1/2/3 — layout-aware pretraining with 2D positions
- [ ] Donut — OCR-free document understanding, seq2seq vision
- [ ] Nougat — academic PDF parsing, LaTeX output
- [ ] PaddleOCR — end-to-end OCR, multilingual, detection + recognition
- [ ] TrOCR — Transformer OCR, image encoder + text decoder
- [ ] Table detection and structure recognition — TATR, TableFormer
- [ ] Key-value extraction from forms — LayoutLM for form parsing
- [ ] Document VQA — DocVQA, InfoVQA, ChartQA benchmarks

---

## PHASE 9 — Reinforcement Learning

### Foundations
- [ ] Markov Decision Processes — states, actions, rewards, transition model
- [ ] Discount factor — geometric sum, infinite horizon problems
- [ ] Value function V(s) — Bellman expectation equation
- [ ] Action-value function Q(s,a) — Bellman optimality equation
- [ ] Policy — deterministic vs stochastic, parameterized policies
- [ ] Model-free vs model-based — when to learn a model
- [ ] On-policy vs off-policy — SARSA vs Q-learning distinction
- [ ] Exploration vs exploitation — epsilon-greedy, UCB, Thompson sampling
- [ ] Tabular methods — dynamic programming, policy iteration, value iteration
- [ ] Monte Carlo methods — first-visit, every-visit MC control
- [ ] Temporal difference — TD(0), TD(λ), eligibility traces
- [ ] Q-learning — off-policy TD, convergence conditions
- [ ] SARSA — on-policy TD, semi-gradient

### Deep RL
- [ ] DQN — deep Q-network, experience replay, target network
- [ ] Double DQN — overestimation fix, separate action selection
- [ ] Dueling DQN — advantage and value stream decomposition
- [ ] Prioritized experience replay — TD-error-based sampling
- [ ] Rainbow — combining all DQN improvements
- [ ] REINFORCE — Monte Carlo policy gradient, high variance
- [ ] Variance reduction — baselines, control variates, advantage
- [ ] Actor-Critic — simultaneous policy and value learning
- [ ] A2C / A3C — synchronous and asynchronous advantage actor-critic
- [ ] PPO — clipped surrogate objective, stable policy updates
- [ ] TRPO — trust region, KL constraint, natural gradient
- [ ] SAC — soft actor-critic, maximum entropy RL, automatic temperature
- [ ] TD3 — twin delayed DDPG, clipped critic, delayed policy updates
- [ ] DDPG — deterministic policy gradient, continuous action spaces
- [ ] Distributional RL — C51, QR-DQN, IQN — modeling return distribution
- [ ] HER — hindsight experience replay, sparse reward problems
- [ ] Intrinsic motivation — ICM, RND — curiosity-driven exploration
- [ ] Hierarchical RL — options framework, feudal networks, HIRO
- [ ] Model-based RL — Dyna, world models, planning with learned model
- [ ] Offline RL — learning from fixed datasets, CQL, IQL, TD3+BC
- [ ] Multi-agent RL — QMIX, MADDPG, MAPPO, CTDE framework
- [ ] AlphaGo — MCTS + policy/value network + self-play
- [ ] AlphaZero — no human data, generalized game playing
- [ ] MuZero — model-based without known game rules
- [ ] Reward shaping — potential-based, curiosity, HER reward relabeling
- [ ] Sim-to-real — domain randomization, system identification, adaptation

### RL for LLMs
- [ ] PPO for RLHF — reward model, reference policy, KL penalty
- [ ] DPO as RL — implicit reward model, Bradley-Terry connection
- [ ] Reward hacking in RLHF — overoptimization, proxy reward divergence
- [ ] RLHF stability — KL coefficient, clipping, reward normalization
- [ ] Process reward models — step-level feedback, math verification
- [ ] DeepSeek-R1 — pure RL to learn chain-of-thought reasoning
- [ ] GRPO — group relative policy optimization, no critic

---

## PHASE 10 — Agentic AI

### Reasoning Patterns
- [ ] Chain-of-Thought (CoT) — scratchpad reasoning, accuracy improvement
- [ ] Zero-shot CoT — emergent with scale, "think step by step"
- [ ] Least-to-most prompting — decompose then solve sequentially
- [ ] Self-consistency — multiple CoT samples, majority vote answer
- [ ] ReAct — interleaved reasoning and acting, trace format
- [ ] Reflexion — verbal self-reflection, episodic memory for improvement
- [ ] Plan-and-Execute — upfront planning then stepwise execution
- [ ] Tree of Thoughts — branching exploration, evaluation, backtracking
- [ ] LATS — Language Agent Tree Search, MCTS for agents
- [ ] Self-RAG — retrieve when needed, self-critique retrieved content
- [ ] Critique and revision — generate then verify and improve
- [ ] Meta-cognitive monitoring — knowing when you're wrong

### Tools & Function Calling
- [ ] Function calling API — JSON schema, tool choice, parallel calls
- [ ] Tool design principles — clear names, typed parameters, LLM-friendly docs
- [ ] Code interpreters — Python execution, matplotlib, data analysis
- [ ] Web search tools — query formulation, result parsing, attribution
- [ ] Browser automation — navigation, form filling, structured extraction
- [ ] Database tools — SQL generation, schema understanding
- [ ] API integration — authentication, pagination, error handling
- [ ] MCP (Model Context Protocol) — server/client architecture, discovery
- [ ] Tool error handling — retry strategies, fallback, error communication
- [ ] Tool sandboxing — resource limits, side effect management, permissions
- [ ] Tool output parsing — structured extraction from tool results

### Memory Systems
- [ ] In-context memory — conversation history, summarization strategies
- [ ] Context window management — what to keep, compress, or drop
- [ ] External episodic memory — storing and retrieving past interactions
- [ ] Semantic memory — knowledge bases, vector stores for long-term facts
- [ ] Procedural memory — caching successful workflows, learned skills
- [ ] Memory consolidation — importance scoring, compression, forgetting
- [ ] MemGPT — virtual context management, paging in/out of context
- [ ] Long-term user personalization — preferences, history across sessions
- [ ] Shared team memory — multi-agent shared knowledge stores

### Multi-Agent Systems
- [ ] Orchestrator-worker pattern — centralized task delegation
- [ ] Decentralized coordination — peer-to-peer communication
- [ ] Debate and critique — agents challenging each other's reasoning
- [ ] Specialization — role-based expert agents, domain sub-agents
- [ ] Shared world state — synchronized state across agents
- [ ] Communication protocols — message passing, structured formats
- [ ] LangGraph — state machine workflows, conditional branching
- [ ] AutoGen — conversational multi-agent, two-agent and group chat
- [ ] CrewAI — role and goal-based crews, task delegation
- [ ] Consensus and voting — when agents disagree on decisions
- [ ] Async agent execution — parallel subagent runs, join points

### Computer Use & Agentic Applications
- [ ] Screen understanding — screenshots as VLM input, UI element detection
- [ ] Action spaces — click, type, scroll, hotkeys, drag
- [ ] DOM parsing — HTML-based navigation vs visual-based
- [ ] WebArena benchmark — realistic web navigation tasks
- [ ] SWE-agent — software engineering agent, ACT interface
- [ ] SWE-bench — real GitHub issues as benchmark for coding agents
- [ ] OpenDevin — open-source software development agent
- [ ] Computer use API — Anthropic's computer use, screenshot + action loop
- [ ] GUI agent safety — preventing irreversible actions, sandboxed browsers
- [ ] Code agents — repository understanding, multi-file edits, testing
- [ ] Data analysis agents — CSV analysis, visualization, statistical testing

### Agent Evaluation
- [ ] Task success rate — clear binary definition vs fuzzy completion
- [ ] Trajectory evaluation — efficiency, unnecessary steps, backtracking
- [ ] Tool use correctness — right tool, right arguments, right interpretation
- [ ] GAIA benchmark — general AI assistant tasks, real-world grounding
- [ ] AgentBench — diverse agent environments
- [ ] WebArena, WorkArena — web and workplace task benchmarks
- [ ] AssistGUI — GUI-based task completion evaluation
- [ ] Human-in-the-loop design — when to pause and confirm
- [ ] Failure mode taxonomy — wrong tool / argument / stop / plan
- [ ] Automated regression testing — nightly evaluation harness

---

## PHASE 11 — AI Safety & Interpretability

### AI Safety Foundations
- [ ] Reward hacking — Goodhart's Law, specification gaming examples
- [ ] Goal misgeneralization — different behavior out of training distribution
- [ ] Inner alignment — mesa-optimizer learning wrong objective
- [ ] Outer alignment — reward function doesn't capture true intent
- [ ] Corrigibility — maintaining ability to be corrected and shut down
- [ ] Scalable oversight — supervising AI systems smarter than humans
- [ ] Debate — using AI arguments to help humans judge AI
- [ ] Amplification — recursive task decomposition with human oversight
- [ ] Iterated distillation and amplification (IDA)
- [ ] Deceptive alignment — appearing aligned during training, diverging after
- [ ] Power-seeking behavior — instrumental convergence thesis
- [ ] Responsible scaling policies — capability thresholds, safety commitments
- [ ] Red-teaming — systematic adversarial probing, diverse attack axes
- [ ] Constitutional AI — principle-based self-critique and revision
- [ ] RLAIF — AI feedback for scalable supervision

### Mechanistic Interpretability
- [ ] Circuits hypothesis — neural networks implement interpretable algorithms
- [ ] Probing classifiers — what's linearly decodable from representations
- [ ] Attention pattern analysis — what heads attend to, head ablations
- [ ] Logit lens — predicting tokens from intermediate layer residuals
- [ ] Activation patching — causal interventions, path patching
- [ ] Causal scrubbing — verifying circuit hypotheses rigorously
- [ ] Superposition — representing more features than neurons, geometry
- [ ] Sparse autoencoders (SAEs) — decomposing superposed features
- [ ] Feature visualization — maximally activating inputs, feature directions
- [ ] Universality — same circuits appearing across different models
- [ ] Indirect object identification (IOI) — studied circuit in GPT-2
- [ ] Induction heads — in-context learning mechanism discovered in Transformers
- [ ] TransformerLens — mechanistic interpretability tooling, hooks
- [ ] Neuron2graph — understanding individual neurons
- [ ] Dictionary learning — finding monosemantic features

### Hallucination & Reliability
- [ ] Hallucination taxonomy — factual errors, attribution errors, reasoning errors
- [ ] Sycophancy — agreeing with incorrect premises, instruction following failures
- [ ] Hallucination causes — memorization vs generalization, exposure bias
- [ ] Factual consistency evaluation — FactScore, QAFactEval, FActKB
- [ ] Self-consistency as hallucination detector — variance across samples
- [ ] Chain-of-Verification — generate then verify specific facts
- [ ] Retrieval grounding — RAG as hallucination mitigation
- [ ] Calibration — ECE, reliability diagrams, temperature scaling
- [ ] Conformal prediction — distribution-free coverage guarantees
- [ ] Uncertainty quantification — Bayesian, ensemble, MC Dropout

### Fairness, Bias & Ethics
- [ ] Sources of bias — historical, representation, measurement, aggregation
- [ ] Fairness criteria — demographic parity, equalized odds, calibration
- [ ] Impossibility theorem — fairness criteria are mutually incompatible
- [ ] Bias in word embeddings — gender bias in Word2Vec, debiasing
- [ ] Bias in LLMs — stereotypes, toxicity, dialect discrimination
- [ ] Bias benchmarks — WinoBias, BBQ, BOLD, StereoSet
- [ ] Toxicity — PerspectiveAPI, Jigsaw datasets, hate speech detection
- [ ] Privacy — membership inference, differential privacy, federated learning
- [ ] Differential privacy — (ε,δ)-DP, Gaussian mechanism, DP-SGD
- [ ] Federated learning — local training, aggregation, communication efficiency
- [ ] Model cards — documenting model purpose, limitations, and risks
- [ ] Datasheets for datasets — data provenance, collection, intended use
- [ ] EU AI Act — risk categories, compliance requirements
- [ ] Responsible AI practices — accountability, auditability, explainability

---

## PHASE 12 — Graph, Geometric & Scientific AI

### Graph Neural Networks
- [ ] Graph representations — adjacency matrix, edge list, node/edge features
- [ ] Message passing framework — aggregate, update, readout
- [ ] GCN — spectral graph convolution, Chebyshev approximation
- [ ] GraphSAGE — inductive learning, neighborhood sampling
- [ ] GAT — graph attention networks, multi-head attention on edges
- [ ] GIN — graph isomorphism network, 1-WL expressivity limit
- [ ] Graph Transformers — global attention over all nodes
- [ ] Heterogeneous graphs — multiple node/edge types, RGCN, HAN
- [ ] Link prediction — embedding dot product, knowledge graph completion
- [ ] Node classification — semi-supervised, label propagation
- [ ] Graph classification — pooling methods, DiffPool, hierarchical
- [ ] Molecular property prediction — MPNN, DimeNet, SchNet, PaiNN
- [ ] AlphaFold 2 — Evoformer, invariant point attention, structure module
- [ ] AlphaFold 3 — diffusion-based structure prediction for all biomolecules
- [ ] Protein language models — ESM-2, ESM-3, ProtTrans

### Geometric Deep Learning
- [ ] Group theory — symmetry groups, representations, equivariance
- [ ] Equivariant networks — G-CNNs, steerable CNNs, E(n)-equivariant
- [ ] SE(3)/E(3)-equivariant networks — 3D molecules, proteins, materials
- [ ] Geometric message passing — EGNN, DimeNet angle features, NequIP
- [ ] Invariant vs equivariant representations — when each is needed
- [ ] Clifford/geometric algebra for ML

### World Models
- [ ] World model definition — latent dynamics model for planning
- [ ] RSSM — Recurrent State Space Model, stochastic and deterministic
- [ ] DreamerV1/V2/V3 — imagination-based actor-critic, universal agent
- [ ] TD-MPC2 — temporal difference model predictive control
- [ ] IRIS — Transformer world model for RL
- [ ] GAIA-1 — generative world model for autonomous driving
- [ ] UniSim — neural closed-loop sensor simulator
- [ ] Genie — generative interactive environment from video
- [ ] LLMs as world models — planning through text, limitations

### AI for Science
- [ ] AlphaFold 2 — MSA encoding, triangle attention, recycling
- [ ] RoseTTAFold — protein structure, diffusion extension
- [ ] Molecular generation — diffusion for molecules, equivariant models
- [ ] Drug discovery — ADMET prediction, virtual screening, hit expansion
- [ ] Property prediction — graph-level regression, uncertainty estimation
- [ ] Reaction prediction — forward synthesis, retrosynthesis
- [ ] Materials discovery — crystal structure prediction, property screening
- [ ] Climate models — GraphCast, Pangu-Weather, FourCastNet
- [ ] Physics-Informed Neural Networks (PINNs) — PDE constraints
- [ ] Neural Operators — FNO, DeepONet — learning solution operators
- [ ] Genomics — DNA language models, DNABERT, Nucleotide Transformer
- [ ] Single-cell RNA — scGPT, Geneformer — cell type prediction

---

## PHASE 13 — Emerging Directions

### Synthetic Data
- [ ] LLM-generated instruction data — Alpaca, WizardLM, Orca pipelines
- [ ] Self-play and self-improvement — iterative self-training
- [ ] Rejection sampling fine-tuning — generate many, keep best by reward
- [ ] Model collapse — training on AI outputs degrades quality over generations
- [ ] Data augmentation — back-translation, paraphrase, task-specific
- [ ] Simulation-based data — rendering engines for CV training
- [ ] Synthetic tabular data — conditional GANs, TabDDPM
- [ ] Knowledge distillation as synthetic data — teacher logits as soft labels

### Continual & Lifelong Learning
- [ ] Catastrophic forgetting — stability-plasticity dilemma
- [ ] Elastic Weight Consolidation (EWC) — Fisher information regularization
- [ ] Progressive Neural Networks — lateral connections, no forgetting
- [ ] Replay methods — experience replay, generative replay
- [ ] PackNet — hard parameter isolation via pruning
- [ ] Online learning — streaming data, concept drift adaptation
- [ ] Meta-learning — MAML, Prototypical Networks, few-shot generalization
- [ ] In-context learning as continual learning — no weight updates

### Efficient AI
- [ ] Mixture of Depths — adaptive compute, skipping some layers
- [ ] Early exit — stop at intermediate layer if confident enough
- [ ] Conditional computation — routing by input complexity
- [ ] Token merging (ToMe) — reducing ViT tokens via bipartite matching
- [ ] Dynamic neural networks — input-adaptive computation
- [ ] Hardware-aware NAS — optimizing for specific device constraints
- [ ] Model parallelism strategies — optimal tensor and pipeline splits

### Neurosymbolic AI
- [ ] Neural-symbolic integration — combining neural and symbolic reasoning
- [ ] Program synthesis — code generation, inductive programming
- [ ] Neuro-symbolic concept learner — visual concept grounding
- [ ] Logic tensor networks — fuzzy logic with neural networks
- [ ] LLMs for formal reasoning — theorem proving, Lean, Isabelle
- [ ] Tool-augmented LLMs — calculator, symbolic math (Wolfram Alpha)

---

## PHASE 14 — Systems, MLOps & Infrastructure

### Hardware & Compute
- [ ] GPU memory hierarchy — HBM, L2 cache, SRAM, bandwidth vs capacity
- [ ] CUDA programming model — threads, blocks, warps, occupancy
- [ ] Memory access patterns — coalescing, bank conflicts, shared memory
- [ ] Compute vs memory bound — arithmetic intensity, roofline model
- [ ] NVIDIA GPU generations — V100, A100, H100, H200, B100 specs
- [ ] Tensor Core operations — fp16/bf16 matrix multiply, sparsity
- [ ] TPU architecture — systolic arrays, XLA compilation
- [ ] Interconnects — NVLink bandwidth, InfiniBand for multi-node
- [ ] NCCL — collective operations (all-reduce, all-gather, broadcast)
- [ ] Custom CUDA kernels — writing fused operations, profiling with Nsight

### Distributed Training
- [ ] Data parallelism — DDP, gradient all-reduce, gradient accumulation
- [ ] Model parallelism — tensor parallelism, Megatron column/row split
- [ ] Pipeline parallelism — micro-batching, 1F1B schedule, bubble overhead
- [ ] Sequence parallelism — for long contexts, Ulysses approach
- [ ] ZeRO Stage 1/2/3 — optimizer/gradient/parameter sharding
- [ ] FSDP — PyTorch Fully Sharded Data Parallel, CPU offload
- [ ] 3D parallelism — combining data + tensor + pipeline parallelism
- [ ] Communication overlap — async all-reduce while computing forward
- [ ] Gradient checkpointing — trading compute for memory
- [ ] Mixed precision training — fp16/bf16, GradScaler, loss scaling
- [ ] Checkpoint saving and resuming — fault tolerance at scale
- [ ] Optimizer state management — Adam state on CPU, offloading

### ML System Design
- [ ] Problem framing — when ML is and is not the right tool
- [ ] Data flywheel — collecting labels from product interactions
- [ ] Training-serving skew — causes, detection, prevention
- [ ] Feature stores — Feast, Tecton — consistent training and serving features
- [ ] Online vs batch inference — latency, cost, freshness tradeoffs
- [ ] Model versioning — naming, lineage, rollback strategy
- [ ] A/B testing for ML — statistical power, minimum detectable effect
- [ ] Shadow deployment — run new model alongside old, compare outputs
- [ ] Canary deployment — gradual traffic shift with monitoring
- [ ] SLA for ML — p50/p95/p99 latency, availability, throughput
- [ ] Cost optimization — model selection, caching, spot instances
- [ ] Multi-model routing — selecting model by cost-quality tradeoff per request
- [ ] Case studies — recommendation, search, ads, fraud, content moderation

### MLOps Tools
- [ ] Weights & Biases — runs, sweeps, artifacts, tables, reports
- [ ] MLflow — tracking, model registry, serving, projects
- [ ] DVC — data and model versioning, pipelines as code
- [ ] Hydra — config composition and overrides for experiments
- [ ] Optuna — hyperparameter optimization, pruning, distributed search
- [ ] Ray Tune — distributed hyperparameter search, integration with frameworks
- [ ] BentoML — model serving, custom runners, distributed serving
- [ ] Seldon Core — Kubernetes-native model serving
- [ ] KServe — serverless model inference on Kubernetes
- [ ] Docker and containerization — reproducible environments
- [ ] Kubernetes basics — pods, deployments, services, autoscaling

### Data Engineering
- [ ] Data pipelines — batch (Spark, Beam) vs streaming (Kafka, Flink)
- [ ] Apache Spark — distributed data processing, MLlib
- [ ] Data validation — Great Expectations, Pandera, schema enforcement
- [ ] Deduplication — MinHash, SimHash, exact and approximate dedup
- [ ] Data labeling — Label Studio, Scale AI, annotation guidelines
- [ ] Inter-annotator agreement — Cohen's kappa, Krippendorff's alpha
- [ ] Programmatic labeling — Snorkel, label functions, majority vote
- [ ] Imbalanced datasets — SMOTE, class weights, threshold optimization
- [ ] Data flywheel design — implicit labels from user behavior
- [ ] Data governance — lineage, provenance, access control
- [ ] Privacy-preserving ML — federated learning, differential privacy, SMPC

### Model Monitoring
- [ ] Covariate shift — input distribution changes, detection methods
- [ ] Label shift — output distribution changes, class prior drift
- [ ] Concept drift — input-output relationship changes over time
- [ ] Drift detection — KS test, PSI, MMD, learned classifiers
- [ ] LLM observability — LangSmith, Langfuse, Phoenix, Braintrust
- [ ] Logging strategy — what to log, sampling rate, cost management
- [ ] Alerting — threshold-based, anomaly detection on metrics
- [ ] Human evaluation loops — periodic sampling and quality review
- [ ] Model cards — performance across subgroups, known limitations

### Evaluation
- [ ] Language benchmarks — MMLU, BIG-Bench, AGIEval, GPQA, MATH
- [ ] Coding benchmarks — HumanEval, MBPP, SWE-bench, LiveCodeBench
- [ ] Reasoning benchmarks — GSM8K, MATH, ARC, HellaSwag, WinoGrande
- [ ] LLM-as-judge — methodology, biases, verbosity and position bias
- [ ] MT-Bench — multi-turn instruction following evaluation
- [ ] AlpacaEval — win rate against reference model
- [ ] Chatbot Arena — crowd-sourced ELO ranking
- [ ] Custom domain evaluation — task-specific test set construction
- [ ] Data contamination — detecting and handling benchmark leakage
- [ ] Eval harness — EleutherAI LM Eval, consistent multi-task evaluation

### CI/CD for ML
- [ ] Model testing — unit tests for preprocessing and postprocessing
- [ ] Behavioral testing — CheckList methodology, property-based tests
- [ ] Automated evaluation on PR — regression detection before merge
- [ ] Prompt regression tests — catching prompt quality regressions
- [ ] Model registry — versioning, tagging stages (staging, production)
- [ ] LLMOps — cost tracking, token usage, latency per endpoint
- [ ] Deployment automation — GitHub Actions, ArgoCD for ML pipelines

---

## PHASE 15 — Architect-Level Mastery

### Reading & Research
- [ ] 3-pass paper reading — title/abstract/intro → methods → full read
- [ ] Connected Papers — visual citation graph exploration
- [ ] Semantic Scholar — citation-based paper discovery, author tracking
- [ ] arXiv — cs.LG, cs.CL, cs.CV, cs.AI daily feeds
- [ ] HuggingFace Papers, The Batch, Import AI — curated weekly digests
- [ ] Reproducing papers — 1 implementation per month minimum
- [ ] Writing paper summaries — distilling to core contribution in 200 words
- [ ] Target — 3 papers read per week, 1 implemented per month

### System Design Practice
- [ ] Design a recommendation system — features, retrieval, ranking, reranking
- [ ] Design a search engine — indexing, query understanding, retrieval, ranking
- [ ] Design a content moderation system — classifiers, human review, appeals
- [ ] Design an LLM serving platform — routing, caching, batching, monitoring
- [ ] Design a RAG pipeline — chunking, embedding, retrieval, reranking, generation
- [ ] Design a multi-agent system — orchestration, tools, memory, evaluation
- [ ] Design an ASR/TTS pipeline — streaming, adaptation, quality monitoring
- [ ] Estimate compute and cost for training runs — FLOPs, time, hardware
- [ ] ML system design interviews — 45-minute structured walkthrough

### Building & Shipping
- [ ] End-to-end project — combines LLM + retrieval + agents + eval
- [ ] Experiment tracking from day one — W&B or MLflow on every run
- [ ] Evaluation harness before building — define success metric first
- [ ] Monitoring in production — drift detection, cost tracking, quality sampling
- [ ] Technical writing — architecture decision records (ADRs)
- [ ] Blog posts — one per major topic mastered
- [ ] Open-source contributions — documentation, bug fixes, features
- [ ] HuggingFace model/dataset uploads — sharing work publicly
- [ ] Technical presentations — explaining systems to non-ML engineers

### Teaching & Communicating
- [ ] Feynman technique — explain simply, identify gaps, iterate
- [ ] Writing for different audiences — executive summary vs deep dive
- [ ] Mock design interviews — 45-minute system design with feedback
- [ ] Paper presentations — distilling a paper in 20 minutes
- [ ] Blogging — one post per completed topic
- [ ] Speaking — conference talks, internal tech talks
- [ ] Mentoring — teaching someone more junior cements your own understanding

---

## Key Papers to Read (Essential List)

### Foundations
- [ ] Attention Is All You Need — Vaswani et al. (2017)
- [ ] BERT — Devlin et al. (2018)
- [ ] GPT-3 — Brown et al. (2020)
- [ ] Chinchilla — Hoffmann et al. (2022)
- [ ] LLaMA 1/2/3 — Touvron et al. (2023/2024)

### Training & Alignment
- [ ] InstructGPT — Ouyang et al. (2022)
- [ ] DPO — Rafailov et al. (2023)
- [ ] Constitutional AI — Bai et al. (2022)
- [ ] LoRA — Hu et al. (2021)
- [ ] QLoRA — Dettmers et al. (2023)

### Vision
- [ ] ResNet — He et al. (2015)
- [ ] ViT — Dosovitskiy et al. (2020)
- [ ] CLIP — Radford et al. (2021)
- [ ] MAE — He et al. (2021)
- [ ] SAM — Kirillov et al. (2023)

### Generative
- [ ] DDPM — Ho et al. (2020)
- [ ] Stable Diffusion / LDM — Rombach et al. (2022)
- [ ] Flow Matching — Lipman et al. (2022)
- [ ] DiT — Peebles & Xie (2022)
- [ ] StyleGAN2 — Karras et al. (2020)

### Speech
- [ ] Wav2Vec 2.0 — Baevski et al. (2020)
- [ ] Whisper — Radford et al. (2022)
- [ ] VITS — Kim et al. (2021)
- [ ] VALL-E — Wang et al. (2023)
- [ ] EnCodec — Défossez et al. (2022)

### Systems & Efficiency
- [ ] FlashAttention — Dao et al. (2022)
- [ ] ZeRO — Rajbhandari et al. (2020)
- [ ] vLLM / PagedAttention — Kwon et al. (2023)
- [ ] Mixtral of Experts — Jiang et al. (2024)
- [ ] DeepSeek-V3 — DeepSeek Team (2024)

### Agents & Reasoning
- [ ] ReAct — Yao et al. (2022)
- [ ] Reflexion — Shinn et al. (2023)
- [ ] Tree of Thoughts — Yao et al. (2023)
- [ ] SWE-bench — Jimenez et al. (2023)
- [ ] DeepSeek-R1 — DeepSeek Team (2025)

### Safety & Interpretability
- [ ] Risks from Learned Optimization — Hubinger et al. (2019)
- [ ] Toy Models of Superposition — Elhage et al. (2022)
- [ ] Scaling Monosemanticity — Templeton et al. (2024)
- [ ] A Mathematical Framework for Transformer Circuits — Elhage et al. (2021)

### AI for Science
- [ ] AlphaFold 2 — Jumper et al. (2021)
- [ ] GraphCast — Lam et al. (2023)
- [ ] AlphaGo/AlphaZero — Silver et al. (2016/2017)

---

## Key Books
- [ ] Deep Learning — Goodfellow, Bengio, Courville (free online)
- [ ] Pattern Recognition and Machine Learning — Bishop
- [ ] Elements of Statistical Learning — Hastie, Tibshirani, Friedman (free PDF)
- [ ] Reinforcement Learning — Sutton & Barto (free online)
- [ ] Gaussian Processes for Machine Learning — Rasmussen & Williams (free PDF)
- [ ] Speech and Language Processing — Jurafsky & Martin (free online)
- [ ] Designing Machine Learning Systems — Chip Huyen
- [ ] AI Engineering — Chip Huyen (2024)
- [ ] Information Theory, Inference, and Learning Algorithms — MacKay (free PDF)
- [ ] Mathematics for Machine Learning — Deisenroth, Faisal, Ong (free PDF)

---

> **How to use this list**: Work through it phase by phase. For each topic, come back to this conversation and ask Claude to teach it — with math, code, paper walkdowns, or quizzes, depending on what you need. Check off topics as you genuinely understand them (i.e., you could explain them to someone else).
