# RND-NNN — <one-sentence question>

Project: <SketchToRender | MassToRender | ImageToRender | Desire Paths | learning> · Module: <n> · Date: <YYYY-MM-DD> · Status: <draft | final>

## Question
One sentence. What would change your decision if you knew the answer?

## Baseline
What is the simplest thing you compare against? Include its number.

## Hypothesis
"If I change X, metric Y will go up/down because Z."

## Setup
Data (source, size, split method), model / pipeline, metric and why this metric. Seeds.

## Experiments
One variable per run.

| Run | Changed | Value | Metric (mean ± std) | Note |
|---|---|---|---|---|
| 0 | — (baseline) |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |

## Results
The number, one figure, and one sentence on what it means.

## Failure cases
A grid of failures + one line per failure type.

## Limitations
What this does not show. Small data, one building type, one seed, etc.

## Next experiment
The single next thing to test, and why.

## Reproduce
```bash
python src/<script>.py --config rnd/RND-NNN-<topic>/configs/<file>.yaml
```
Commit: `<hash>`
