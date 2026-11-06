"""
Pattern A: validate -> branch -> return.

Skeleton, always the same:
    1. reject bad input first (raise ValueError)
    2. branch; every branch assigns the result, the last `else` raises
    3. one `return` at the end

Rule: write each function from scratch, no peeking at old code. 5 minutes each.
Run:  python drills/d01_validate_branch_return.py
"""

from _check import raises, run


def positive_odd(n):
    """Returns n if it is a positive odd integer, otherwise raises ValueError."""
    raise NotImplementedError


def grade(score, scale="letter"):
    """Grades a score in 0..100.

    scale="letter" -> "A" (>= 90), "B" (>= 75), "C" (otherwise)
    scale="pass"   -> "pass" (>= 50), "fail" (otherwise)
    scale=<number> -> that number is the pass mark: "pass" if score >= scale, else "fail"
    Raises ValueError for a score outside 0..100 or an unknown scale string.
    """
    raise NotImplementedError


def tax(amount, kind="vat"):
    """Returns the tax on amount, rounded to 2 decimals.

    kind="vat" -> 20%, "reduced" -> 8%, "none" -> 0%
    kind=<number between 0 and 1> -> that rate
    Raises ValueError for a negative amount, an unknown kind string, or a rate outside 0..1.
    """
    raise NotImplementedError


def normalize(values, method="minmax"):
    """Scales a list of numbers.

    "minmax" -> (v - min) / (max - min); if all values are equal, all zeros
    "max"    -> v / max
    <number> -> v / that number
    Raises ValueError for an empty list, an unknown method string, or a zero divisor.
    """
    raise NotImplementedError


# ------------------------------------------------------------ tests
def test_positive_odd():
    assert positive_odd(5) == 5
    assert positive_odd(1) == 1
    for bad in (-3, 0, 4):
        raises(ValueError, positive_odd, bad)


def test_grade_letter():
    assert grade(95) == "A"
    assert grade(90) == "A"
    assert grade(80) == "B"
    assert grade(10) == "C"


def test_grade_pass_and_number():
    assert grade(60, "pass") == "pass"
    assert grade(40, "pass") == "fail"
    assert grade(70, 65) == "pass"
    assert grade(60, 65) == "fail"


def test_grade_errors():
    raises(ValueError, grade, 70, "letteer")
    raises(ValueError, grade, 101)
    raises(ValueError, grade, -1)


def test_tax():
    assert tax(100) == 20.0
    assert tax(100, "reduced") == 8.0
    assert tax(100, "none") == 0.0
    assert tax(100, 0.5) == 50.0
    raises(ValueError, tax, 10, "vta")
    raises(ValueError, tax, -1)
    raises(ValueError, tax, 10, 1.5)


def test_normalize():
    assert normalize([2, 4, 6]) == [0.0, 0.5, 1.0]
    assert normalize([5, 5]) == [0.0, 0.0]
    assert normalize([1, 2, 4], "max") == [0.25, 0.5, 1.0]
    assert normalize([2, 4], 2) == [1.0, 2.0]


def test_normalize_errors():
    raises(ValueError, normalize, [])
    raises(ValueError, normalize, [1, 2], "zscore")
    raises(ValueError, normalize, [1, 2], 0)


if __name__ == "__main__":
    run(globals())
