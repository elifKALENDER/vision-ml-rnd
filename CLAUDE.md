# CLAUDE.md

Read at the start of every session. Instructions for Claude only; progress and history live in the files listed under "Docs map".

## Project
- Repo: `F:\vision-ml-rnd`, remote `https://github.com/elifKALENDER/vision-ml-rnd.git` (branch `main`).
- Exercise-driven curriculum from classical CV to deep learning, 3D and generative models. Long-term target: **MassToRender** (see README).
- Python: conda env `vision-ml-rnd` (`C:\Users\ekale\.conda\envs\vision-ml-rnd\python.exe`, Python 3.13), defined in `environment.yml`. Jupyter kernel: `vision-ml-rnd`. There is no system `python` command; use this path. Conda: `C:\ProgramData\anaconda3\Scripts\conda.exe`.
- `torch` is not installed yet; it is added in Module 7. Until then m07+ notebooks stop at `import torch`.
- Verification: every notebook is run top to bottom with `learning/` as the working directory.

## Docs map
Each fact lives in exactly one file.

| File | Language | Purpose |
|---|---|---|
| `CLAUDE.md` | English | Rules for Claude (this file) |
| `PROGRESS.md` | Turkish | Checklist of modules/sessions and "Nerede kaldım" |
| `JOURNAL.md` | Turkish | The user's file: mistakes and lessons, dated session log |
| `README.md` | English | Public face of the repo: goal, structure, setup, curriculum |
| `rnd/README.md` | English | Index of R&D reports (RND-NNN) and technical notes (TN-NNN) |
| `rnd/RND-000-template.md` | English | Template for each report |
| `drills/README.md` | English | Short repeatable Python drills (stubs + tests) and the day-end routine |

## Folder rules
- Notebooks live in `learning/`, named by module number (`m01a_…`, `k1_…`, `tracks/p1_…`).
- Inputs go in `learning/images/` and `learning/data/`.
- Generated files go in `learning/outputs/` (git-ignored). Notebooks use relative paths and are run from `learning/`. `learning/cv_outputs/` is an older output folder that `m01a_opencv_core_v2.ipynb` still writes to; keep it, do not delete it, and use `outputs/` for new work.
- `rnd/`: reports and technical notes (see `rnd/README.md`).
- `drills/`: repeatable practice, outside the `learning/` no-edit rule; `cards.md` belongs to the user.
- `src/` (reusable code extracted from notebooks) and `papers/` (paper notes) are empty placeholders (`.gitkeep`) listed in the README. Keep them; fill only when the curriculum reaches that point.
- `archive/` is frozen (earlier practice and superseded notebook versions).
- Ignore tool-generated folders such as `*-pycharm-support-libs/` and `__pycache__/` (git-ignored). Do not delete anything whose purpose is unclear; ask first.

## Working style
- Chat in Turkish. Technical terms stay in English (mask, kernel, docstring, commit, …).
- The user is a beginner and learns by writing code: explain *why* a fix is needed, leave the meaningful parts to them, never hand out ready-made solutions.
- **Never edit existing code or notebooks under `learning/`**: notebooks and `.py` helpers alike (e.g. `cvtools.py`). These are learning files. When the user hits an error, explain the cause and give a hint; the user makes the fix. Exception only when the user explicitly asks at that moment, and only within the requested scope. Adding new input files to `learning/images/` or `learning/data/` at the user's request is fine. Exercises themselves are worked through in a separate Claude chat (learning archive).
- **Review level:** first, does it work and meet the docstring/test contract (explain the cause and the concept)? Second, is it the right tool and is the logic sound? Report only real bugs plus 1–2 concepts per review. Basic robustness (a clear error for the obvious bad input) is welcome; exhaustive hardening, PEP 8/spacing and unused variables are skipped (the IDE handles them) unless asked or an error shows up. A better name is only a small side note.
- **Language rule:** everything in code (docstrings, comments, error messages, variable/function names), commit messages and this file is English. Only JOURNAL.md and PROGRESS.md entries are Turkish. Exception: string values that define behavior (e.g. `"karanlık"` returned by `diagnose_exposure`) stay as they are unless the user changes them, because tests compare them.
- Notebook diffs are noisy (base64 outputs). Review changes through cell sources.
- JOURNAL entries stay short: a few bullets per topic, only lessons likely to recur.

## Git
- Commit at the end of every session (step 5 below) and whenever the user asks mid-session. Never commit otherwise.
- Push only when the user asks.
- Stage files by name (no `git add -A`), check `git status` first, and never commit secrets or git-ignored outputs. Include the user's own `learning/` changes from the session; do not modify them.
- Messages: English, imperative, one line summary (see `git log` for style). Split unrelated changes into separate commits.

## End of session
1. Append a dated Turkish entry to the "Oturum günlüğü" section of `JOURNAL.md` (newest first: `### YYYY-MM-DD — topic`, what was done, exercises done without AI, open items, next step).
2. Update the checkboxes and "Nerede kaldım" in `PROGRESS.md`.
3. If the user pasted lesson notes or made mistakes worth keeping, add them to "Hatalar ve dersler" in `JOURNAL.md` under the matching topic. Append, never overwrite. Important mistakes may be added on Claude's own initiative; if nothing was pasted and nothing stands out, ask.
4. Drills: add 2–4 new drills for the mistakes the user got stuck on most today to the matching pattern file in `drills/` (or a new `dNN_…`). Write stubs (`raise NotImplementedError`) and `assert` tests only, never solutions. Check the tests against a private reference solution in the scratchpad. Then name 2 older drills to repeat tomorrow. Update the pattern table in `drills/README.md` if a file is added.
5. Commit (see "Git").
