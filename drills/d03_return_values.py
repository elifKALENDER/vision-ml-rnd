"""
Pattern C: return values and not modifying the input.

Traps seen: `_, mask = cv2.adaptiveThreshold(...)` (it returns one value, not two),
`x.astype(...)` result thrown away, drawing on the original instead of a copy.

Rule: for each function, write the call site too (unpack it the way a caller would).
Run:  python drills/d03_return_values.py
"""

from _check import raises, run


def min_max(values):
    """Returns the tuple (smallest, largest). Raises ValueError for an empty list."""
    raise NotImplementedError


def only_max(values):
    """Returns only the largest value. Call min_max() and unpack it, throwing the first away."""
    raise NotImplementedError


def split_sign(values):
    """Returns (negatives, non_negatives), both lists in the original order."""
    raise NotImplementedError


def above(values, t):
    """Returns (count, indices) of values strictly greater than t."""
    raise NotImplementedError


def add_one(values):
    """Returns a NEW list with 1 added to each value. The input list must stay unchanged."""
    raise NotImplementedError


# ------------------------------------------------------------ tests
def test_min_max():
    assert min_max([3, 1, 2]) == (1, 3)
    lo, hi = min_max([5])
    assert (lo, hi) == (5, 5)
    raises(ValueError, min_max, [])


def test_only_max():
    assert only_max([3, 9, 2]) == 9


def test_split_sign():
    neg, rest = split_sign([3, -1, 0, -2, 5])
    assert neg == [-1, -2]
    assert rest == [3, 0, 5]


def test_above():
    assert above([1, 5, 3, 7], 3) == (2, [1, 3])
    assert above([1, 2], 5) == (0, [])


def test_add_one():
    original = [1, 2, 3]
    result = add_one(original)
    assert result == [2, 3, 4]
    assert original == [1, 2, 3], "input was modified"
    assert result is not original


if __name__ == "__main__":
    run(globals())
