# drills

Short, repeatable Python drills for the basics (branching, scope, return values,
dtype, indexing). Not part of the curriculum, not graded. Outside `learning/`.

## How a drill works
1. Open a pattern file (`d01_…` to `d05_…`). Each function is an empty stub with a docstring.
2. Write the body from scratch. No peeking at `cvtools.py` or old drills.
3. Run `python drills/dNN_….py` (conda env `vision-ml-rnd`). Each test prints `TODO`, `PASS`, `FAIL` or `ERROR`.
4. On `FAIL`/`ERROR`, explain the cause to yourself in one sentence before fixing.
5. Next day: reset the stub (`raise NotImplementedError`) and write it again without looking.

## Patterns
| File | Pattern | Seen in |
|---|---|---|
| `d01_validate_branch_return.py` | validate → branch → return | `smooth`, `binarize`, `diagnose_exposure` |
| `d02_scope_and_conditions.py` | scope, `or`/`and`/`|`, dead checks, the `0` case | `smooth`, `edge_map`, `binarize` |
| `d03_return_values.py` | tuple vs single return, not modifying the input | `threshold`/`adaptiveThreshold`, `draw_boxes` |
| `d04_dtype_overflow.py` | uint8 wrap, int16, clip, copies | `excess_green` |
| `d05_grid_and_filter.py` | grid indexing, filter + sort | `show`, `find_boxes` (P8) |

## Day-end routine
At the end of each session Claude:
1. Reads the day's mistakes (`JOURNAL.md` → "Hatalar ve dersler" and the session entry).
2. Adds 2–4 new drills for the mistakes you got stuck on most, into the matching pattern file (or a new `dNN_…` if none fits). Stubs and tests only, never solutions.
3. Picks 2 older drills to repeat tomorrow and lists them in the chat.

## Tool cards
`cards.md` is yours: one card per OpenCV/NumPy function, written from memory.
