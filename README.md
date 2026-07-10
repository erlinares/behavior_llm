# Evaluating the Behavior of Large Language Models

A research essay surveying the 2024–2026 state of the art in evaluating **LLM behavior** — as
distinct from LLM capability — across two axes: **social bias** (dialectal, gender, racial,
socioeconomic, intersectional) and **harmful behavior / red-teaming** (jailbreaks,
manipulation, multi-turn escalation). The essay reviews the principal benchmarks and
methodologies, summarizes recent findings and the research gaps their own authors admit to,
compares the commercial and open-source tooling landscape, and closes with a concrete
methodological proposal and a set of open research questions. It takes a deliberately critical
stance: a recurring theme is that the instruments used to certify LLM safety are themselves
poorly validated.

This is a research-writing project, not a software codebase — there is no build system, no
tests, and no application code to run.

## Contents

| File | Description |
|---|---|
| [`LLM_behavior_evaluation_survey.md`](LLM_behavior_evaluation_survey.md) | The essay, in English (canonical version). |
| [`LLM_behavior_evaluation_survey_ES.md`](LLM_behavior_evaluation_survey_ES.md) | Spanish translation, kept in sync with the English version. |
| [`LLM_behavior_evaluation_survey.pdf`](LLM_behavior_evaluation_survey.pdf) / [`_ES.pdf`](LLM_behavior_evaluation_survey_ES.pdf) | Rendered arXiv-style PDFs of the two versions above. |
| [`state_of_art/`](state_of_art/) | Archive of the ~40 primary sources (arXiv PDFs) cited in the essay, indexed in [`state_of_art/SOURCES.md`](state_of_art/SOURCES.md). |

## Essay structure

1. Context and problem — why evaluating behavior differs from evaluating capability
2. State of the art in research (2024–2026) — bias benchmarks, red-teaming benchmarks, recent
   findings, and admitted research gaps
3. Methodologies — human vs. automated red-teaming, single- vs. multi-turn, static vs.
   dynamic evaluation, metrics and their limitations
4. Tools available on the market — open-source and commercial frameworks compared
5. Proposal — a concrete, resource-aware methodological design for original research
6. Open questions for an original research project

## Sources

Every claim in the essay is traceable to a primary source archived in
[`state_of_art/`](state_of_art/state_of_art), indexed by arXiv ID in
[`SOURCES.md`](state_of_art/SOURCES.md) and grouped into: bias benchmarks, red-teaming/jailbreak
benchmarks, methodology/meta-evaluation papers, tools/frameworks not on arXiv, and
governance/standards references. Sources are cited inline in the essay by arXiv ID (e.g.
`2402.04249`).

## License

No license specified.
