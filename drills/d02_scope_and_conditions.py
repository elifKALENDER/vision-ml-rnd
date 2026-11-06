"""
Pattern B: scope and conditions.

Traps seen in cvtools: `|` instead of `or`, a check inside an `if` block that
can never be true there, `0` rejected by a "positive" check.

Rule: before running, say out loud what each test expects for k = 0, 4, -3.
Run:  python drills/d02_scope_and_conditions.py
"""

from _check import raises, run


def describe(n):
    """Returns "negative", "zero", "positive_even" or "positive_odd"."""
    raise NotImplementedError


def is_valid_k(k):
    """True for 0 and positive odd integers, False for negatives and even numbers > 0."""
    raise NotImplementedError


def in_range(x, lo, hi):
    """True if lo <= x <= hi. Use a single chained comparison, no `and`."""
    raise NotImplementedError


def same_side(a, b):
    """True if a and b are both positive or both negative. Zero is neither."""
    raise NotImplementedError


def window(k=0):
    """k=0 -> None (no window); positive odd k -> (k, k).

    Raises ValueError for negative or even k.
    Put the checks so that k=0 is never rejected and no check is dead code.
    """
    raise NotImplementedError


# ------------------------------------------------------------ tests
def test_describe():
    assert describe(-4) == "negative"
    assert describe(0) == "zero"
    assert describe(4) == "positive_even"
    assert describe(7) == "positive_odd"


def test_is_valid_k():
    for ok in (0, 1, 3, 5):
        assert is_valid_k(ok) is True, ok
    for bad in (-1, -3, 2, 4):
        assert is_valid_k(bad) is False, bad


def test_in_range():
    for x in (1, 5, 10):
        assert in_range(x, 1, 10) is True, x
    for x in (0, 11):
        assert in_range(x, 1, 10) is False, x


def test_same_side():
    assert same_side(1, 2) is True
    assert same_side(-1, -2) is True
    assert same_side(1, -2) is False
    assert same_side(0, 1) is False
    assert same_side(0, 0) is False


def test_window():
    assert window() is None
    assert window(0) is None
    assert window(3) == (3, 3)
    raises(ValueError, window, -3)
    raises(ValueError, window, 4)


if __name__ == "__main__":
    run(globals())
