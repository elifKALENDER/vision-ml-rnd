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
- Generated files go in `learning/outputs/` (git-ignored). Notebooks use relative paths and are run from `learning/`.
- `archive/` is frozen (earlier practice and superseded notebook versions).

## Working style
- Chat in Turkish. Technical terms stay in English (mask, kernel, docstring, commit, …).
- The user learns by writing code: explain *why* a fix is needed, leave the meaningful parts to them, never hand out ready-made solutions.
- **Never edit anything under `learning/`**: notebooks and `.py` helpers alike (e.g. `cvtools.py`). These are learning files. When the user hits an error, explain the cause and give a hint; the user makes the fix. Exception only when the user explicitly asks at that moment, and only within the requested scope. Exercises themselves are worked through in a separate Claude chat (learning archive).
- **Language rule:** everything in code (docstrings, comments, error messages, variable/function names), commit messages and this file is English. Only JOURNAL.md and PROGRESS.md entries are Turkish. Exception: string values that define behavior (e.g. `"karanlık"` returned by `diagnose_exposure`) stay as they are unless the user changes them, because tests compare them.
- Notebook diffs are noisy (base64 outputs). Review changes through cell sources.

## End of session
1. Append a dated Turkish entry to the "Oturum günlüğü" section of `JOURNAL.md` (newest first: `### YYYY-MM-DD — topic`, what was done, exercises done without AI, open items, next step).
2. Update the checkboxes and "Nerede kaldım" in `PROGRESS.md`.
3. If the user pasted lesson notes or made mistakes worth keeping, add them to "Hatalar ve dersler" in `JOURNAL.md` under the matching topic. Append, never overwrite. If no notes were pasted, ask.
4. Drills: add 2–4 new drills for the mistakes the user got stuck on most today to the matching pattern file in `drills/` (or a new `dNN_…`). Write stubs (`raise NotImplementedError`) and `assert` tests only, never solutions. Check the tests against a private reference solution in the scratchpad. Then name 2 older drills to repeat tomorrow. `drills/` is not under the `learning/` no-edit rule, but `cards.md` belongs to the user.
