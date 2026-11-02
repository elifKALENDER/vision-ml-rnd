# R&D reports

Each report lives in its own folder: `RND-NNN-<topic>/` with `report.md`, `figures/`, `configs/`. Technical notes (TN) are shorter method notes. Negative results are reports too.

| No | Module | Question | Finding | Status |
|---|---|---|---|---|
| RND-001 | 1 | SketchToRender: how does sketch preprocessing (raw / Canny / adaptive threshold) change line fidelity of the render? | — | planned |
| RND-002 | 2 | Dataset audit + leakage-free baseline: how much does a group split change the score? | — | planned |
| RND-003 | 3 | Which classical model is the strongest baseline to set against the Phase B deep models? | — | planned |
| TN-001 | 4 | Math for ML | — | planned |
| TN-002 | 5 | Experiment design and statistics | — | planned |
| RND-004 | 6 | Can an MLP written from scratch beat the classical baseline on small data, and how much do initialization and optimizer choice matter? | — | planned |
| RND-005 | 7 | Does a small CNN trained from scratch on a small architectural image set beat the classical baseline? | — | planned |
| RND-006 | 8 | Transfer learning on small architectural datasets: linear probe, partial or full fine-tuning? | — | planned |
| RND-007 | 9 | Which frozen features work best for few-shot classification of historic building elements: ResNet, DINOv2 or CLIP? | — | planned |
| RND-008 | 10 | How consistent are my own labels, and what does that imply for the highest reachable mAP? | — | planned |
| RND-009 | 11 | Can a detector trained on real + synthetic images reliably count windows on a facade? | — | planned |
| RND-010 | 12 | Facade element segmentation: zero-shot SAM 2 or a trained U-Net? | — | planned |
| RND-011 | 13 | Can pedestrian trajectories from a fixed camera reveal desire paths? | — | planned |
| RND-012 | K1 | What moved the score most in this competition: data, resolution, backbone or ensembling? | — | planned |
| RND-013 | 14 | On repetitive facades, is classical (SIFT + RANSAC) or learned (LightGlue) matching more reliable? | — | planned |
| RND-014 | 15 | How far does MASt3R depth deviate from Blender ground truth on original vs clay-preprocessed inputs? | — | planned |
| RND-015 | 16 | SD 1.5 on an RTX 2060, steps × scheduler: where is the quality (CLIP/FID) vs time trade-off? | — | planned |
| RND-016 | 17 | MassToRender benchmark v1: which ControlNet component carries structure, and which carries material? | — | planned |
| RND-017 | 18 | Deployment cost of my models on an RTX 2060: PyTorch FP32 vs FP16 vs ONNX vs TensorRT | — | planned |
| RND-018 | K2 | What changed since Kaggle 1: how many places did each new method gain? | — | planned |
