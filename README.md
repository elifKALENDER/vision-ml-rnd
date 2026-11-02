# vision-ml-rnd

A structured, exercise-driven path from Python and classical computer vision to deep learning, 3D geometry and generative models, documented as reproducible R&D reports.

The long-term target is **MassToRender** (RND-016): turning architectural massing models and sketches into controlled renders. Every module builds a skill that project needs.

## Structure

```
learning/        Module notebooks, named by module number
  m00_numpy_core.ipynb          Module 0
  m01a_… m01b_… m01c_…          Module 1 (classical CV, three parts)
  m02_… … m18_…                 Modules 2–18
  m15b_rendering_pbr.ipynb      Module 15b
  k1_kaggle.ipynb, k2_kaggle    Kaggle checkpoints
  extras.ipynb                  Supplementary sessions (EK-A–D)
  tracks/                       Parallel tracks P1–P5
  images/, data/                Inputs used by the notebooks
  outputs/                      Generated files (git-ignored)
rnd/             R&D reports (RND-NNN) and technical notes (TN-NNN)
papers/          Paper notes
src/             Reusable code extracted from the notebooks
archive/         Earlier Python / pandas / OpenCV practice (frozen)
PROGRESS.md      Session plan and progress log
CLAUDE.md        Working notes and session log for AI-assisted sessions
environment.yml  Conda environment (vision-ml-rnd)
```

## Setup

```
conda env create -f environment.yml
conda activate vision-ml-rnd
python -m ipykernel install --user --name vision-ml-rnd --display-name "Python (vision-ml-rnd)"
```

Run notebooks from the `learning/` directory; they use paths relative to it (`images/`, `data/`, `outputs/`).

## Curriculum

| Phase | Modules |
|---|---|
| Foundations | 0 Python + NumPy · 1 Classical CV · 2 Data + ML baseline · 3 Classical ML · 4 Math for ML · 5 Experiment design |
| Deep learning | 6 NN from scratch · 7 PyTorch training · 8 CNN + transfer · 9 Transformers, SSL, multimodal |
| Vision tasks | 10 Dataset engineering · 11 Detection · 12 Segmentation · 13 Video + tracking · **K1** |
| Geometry & rendering | 14 Projective geometry · 15 Multi-view 3D · 15b Radiometry & PBR |
| Generative & deployment | 16 Diffusion · 17 Controlled generation · 18 Deployment · **K2** |

Each module ends with an R&D report answering one concrete question. See [`rnd/README.md`](rnd/README.md) and [`PROGRESS.md`](PROGRESS.md).

## Learning method

Problem → understand input/output → write a first solution → test → debug → refactor → repeat from a blank file.

AI assistance is used as a learning and debugging aid, not as a replacement for understanding the solution. `PROGRESS.md` records which exercises were done without AI.

## Sources

Early exercises (see `archive/`) build on concepts studied in MIUUL training materials, reworked into independent practice problems.

## License

MIT
