# `state_of_art/` — Source Index

This folder contains the primary sources cited in the research article
(`../LLM_behavior_evaluation_survey.md` / `../LLM_behavior_evaluation_survey_ES.md`).

- **39 arXiv PDFs** were downloaded on 2026-07-08 (filenames: `<arXivID>_<shortname>.pdf`).
- Tools/frameworks and governance documents that are **not** on arXiv are listed at the
  bottom with their official URLs (product pages, GitHub repos, standards bodies).

All arXiv IDs below were surfaced and cross-checked in web search results. A small number
of speculative future-dated IDs surfaced during research were **excluded** because they
could not be verified.

---

## A. Bias benchmarks & datasets (downloaded PDFs)

| File (arXiv ID) | Title (short) | Year | Notes |
|---|---|---|---|
| 2110.08193 | BBQ: Bias Benchmark for QA (Parrish et al.) | 2022 | 9 US social axes + intersectional; ambiguous vs disambiguated contexts |
| 2101.11718 | BOLD: Bias in Open-ended Language Generation (Dhamala et al.) | 2021 | 23.7k prompts, 5 domains; automated toxicity/sentiment/regard |
| 2205.09209 | HolisticBias (Smith et al.) | 2022 | 600 descriptors × 13 axes → 450k+ prompts; participatory design |
| 2004.09456 | StereoSet (Nadeem et al.) | 2020 | LM score vs stereotype score; widely critiqued for validity |
| 2010.00133 | CrowS-Pairs (Nangia et al.) | 2020 | 1,508 minimal pairs, 9 bias types; masked-LM pseudo-log-likelihood |
| 2403.00742 | Dialect prejudice predicts AI decisions (Hofmann et al., *Nature* 2024) | 2024 | Matched-guise probing of covert AAE bias |
| 2212.08011 | Multi-VALUE: cross-dialectal English (Ziems et al.) | 2023 | 50 dialects / 189 features; dialect stress tests |
| 2403.14633 | Born With a Silver Spoon? Socioeconomic bias (Singh et al.) | 2024 | SilverSpoon dataset, 3k scenarios |
| 2405.18662 | Intrinsic Socioeconomic Biases in LLMs (Arzaghi et al., AIES) | 2024 | 1M-sentence dataset; intersectional amplification |
| 2309.00770 | Bias and Fairness in LLMs: A Survey (Gallegos et al., *Computational Linguistics*) | 2024 | Standard reference taxonomy; Fair-LLM-Benchmark repo |

## B. Red-teaming, jailbreaks & harmful-behavior benchmarks (downloaded PDFs)

| File (arXiv ID) | Title (short) | Year | Notes |
|---|---|---|---|
| 2402.04249 | HarmBench (Mazeika et al., ICML) | 2024 | Standardized automated red-teaming; ASR; R2D2 defense |
| 2404.01318 | JailbreakBench (Chao et al., NeurIPS D&B) | 2024 | JBB-Behaviors, live leaderboard, artifact repo |
| 2406.14598 | SORRY-Bench (ICLR 2025) | 2024 | 45-topic taxonomy, 450 unsafe instructions, fine-tuned judges |
| 2402.10260 | StrongREJECT (Souly et al., NeurIPS) | 2024 | 346 forbidden prompts; autograder; "empty jailbreaks" critique |
| 2307.15043 | GCG: Universal & Transferable Adversarial Attacks (Zou et al.) | 2023 | Introduced AdvBench; gradient suffixes |
| 2310.08419 | PAIR: jailbreak in 20 queries (Chao et al.) | 2023 | Attacker-LLM iterative refinement |
| 2312.02119 | TAP: Tree of Attacks (Mehrotra et al., NeurIPS) | 2023 | Tree-of-thoughts branching; >80% ASR GPT-4 |
| 2402.16822 | Rainbow Teaming (Samvelyan et al., NeurIPS) | 2024 | Quality-diversity adversarial prompt search |
| 2408.15221 | Multi-turn human jailbreaks / MHJ (Scale AI) | 2024 | >70% ASR vs defenses reporting single-digit single-turn ASR |
| 2404.01833 | Crescendo multi-turn jailbreak (Russinovich et al., Microsoft) | 2024 | Gradual escalation; Crescendomation automation |
| 2404.02151 | Simple Adaptive Attacks (Andriushchenko et al., ICLR 2025) | 2024 | ~100% ASR; ASR sensitivity to budget/judge/target string |

## C. Methodology, metrics & meta-evaluation (downloaded PDFs)

| File (arXiv ID) | Title (short) | Year | Notes |
|---|---|---|---|
| 2202.03286 | Red Teaming LMs with LMs (Perez et al., DeepMind) | 2022 | Foundational automated red-teaming |
| 2209.07858 | Red Teaming to Reduce Harms (Ganguli et al., Anthropic) | 2022 | ~39k human attacks; scaling behavior |
| 2403.13793 | Evaluating Frontier Models for Dangerous Capabilities (DeepMind) | 2024 | Persuasion/cyber/self-proliferation/CBRN batteries |
| 2404.14068 | Holistic Safety & Responsibility Evaluations (DeepMind) | 2024 | End-to-end eval practice |
| 2402.19464 | Curiosity-driven Red-teaming | 2024 | Diversity of automated attacks |
| 2503.04856 | M2S: Multi-turn to Single-turn | 2025 | Compresses multi-turn escalation |
| 2504.03174 | Multilingual Multi-turn Automated Red Teaming | 2025 | Cross-lingual guardrail failure |
| 2504.20879 | The Leaderboard Illusion | 2025 | Chatbot Arena / LMArena critique |
| 2501.17858 | Improving Arena Ranking by Vote Rigging | 2025 | Preference-metric manipulability |
| 2407.21792 | Safetywashing (Ren et al., CAIS) | 2024 | Safety benchmarks correlate with capability |
| 2406.04244 | Benchmark Data Contamination: A Survey | 2024 | Contamination taxonomy & detection |
| 2511.04703 | Measuring what Matters: Construct Validity (Bean et al., NeurIPS 2025) | 2025 | Review of 445 benchmarks |
| 2502.06559 | Can We Trust AI Benchmarks? Interdisciplinary Review | 2025 | Measurement-theory critique |
| 2411.16594 | LLM-as-a-judge survey (Li et al.) | 2024 | Position/verbosity/self-preference bias |
| 2307.03109 | A Survey on Evaluation of LLMs (Chang et al.) | 2023 | Canonical what/where/how survey |
| 2407.04069 | Systematic Survey & Critical Review on Evaluating LLMs | 2024 | Limitations-focused |
| 2412.08653 | What AI evaluations can and cannot do | 2024 | Evals as lower bounds |
| 2603.06594 | A Coin Flip for Safety: LLM Judges Fail to Measure Robustness | 2026 | LLM judges near-chance on ASR |

---

## D. Tools & frameworks (not on arXiv — official URLs)

**Open source**
- NVIDIA **garak** — https://github.com/NVIDIA/garak · https://garak.ai/ (Apache-2.0)
- Microsoft **PyRIT** — https://github.com/microsoft/PyRIT · https://microsoft.github.io/PyRIT/ (MIT)
- **promptfoo** — https://github.com/promptfoo/promptfoo · https://www.promptfoo.dev/docs/red-team/ (MIT)
- **Giskard** — https://github.com/Giskard-AI/giskard-oss · https://www.giskard.ai/ (Apache-2.0)
- **DeepEval** (Confident AI) — https://github.com/confident-ai/deepeval · https://deepeval.com/ (Apache-2.0)
- Stanford **HELM** — https://github.com/stanford-crfm/helm · https://crfm.stanford.edu/helm/
- **OpenAI Evals** — https://github.com/openai/evals (MIT)
- UK AISI **Inspect** — https://github.com/UKGovernmentBEIS/inspect_ai · https://inspect.aisi.org.uk/ · evals: https://github.com/UKGovernmentBEIS/inspect_evals
- **HuggingFace Evaluate** — https://github.com/huggingface/evaluate · https://huggingface.co/blog/evaluating-llm-bias
- Meta **Purple Llama / Llama Guard** — https://github.com/meta-llama/PurpleLlama

**Commercial / SaaS**
- **Lakera Red / Guard** (Check Point) — https://www.lakera.ai/lakera-red · https://docs.lakera.ai/
- **Robust Intelligence** (Cisco AI Defense) — https://www.cisco.com/site/us/en/products/security/ai-defense/
- Google Jigsaw **Perspective API** — https://perspectiveapi.com/ *(scheduled sunset 2026-12-31)*

## E. Governance / standards references (not on arXiv)
- NIST **ARIA** program — https://www.nist.gov/news-events/news/2024/05/nist-launches-aria-new-program-advance-sociotechnical-testing-and
- NIST **AI 800-1** (Managing Misuse Risk for Dual-Use Foundation Models, draft) — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd2.pdf
- US AI Safety Institute research agreements (2024) — https://www.nist.gov/news-events/news/2024/08/us-ai-safety-institute-signs-agreements-regarding-ai-safety-research
- Anthropic **Many-shot jailbreaking** (no confirmed arXiv ID; cite these) — https://www.anthropic.com/research/many-shot-jailbreaking · NeurIPS 2024 proceedings: https://proceedings.neurips.cc/paper_files/paper/2024/file/ea456e232efb72d261715e33ce25f208-Paper-Conference.pdf
