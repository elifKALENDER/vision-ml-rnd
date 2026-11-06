"""
Pattern D: dtype, overflow, copies (NumPy).

Traps seen: uint8 wraps (200*2 -> 144), uint16 cannot hold negatives, clip does not
change dtype, astype returns a copy.

Rule: predict each result on paper first (value AND dtype), then run.
Run:  python drills/d04_dtype_overflow.py
"""

import numpy as np

from _check import run


def safe_double(a):
    """uint8 array -> array of twice the values as int16, without wrap-around."""
    raise NotImplementedError


def signed_diff(a, b):
    """Two uint8 arrays -> a - b as int16 (negative results must stay negative)."""
    raise NotImplementedError


def clip_u8(a):
    """Integer array -> values clipped to 0..255, returned as uint8."""
    raise NotImplementedError


def brighten(img, delta):
    """uint8 image + delta (may be negative), saturating at 0 and 255. Returns uint8.

    The input image must stay unchanged.
    """
    raise NotImplementedError


def to_unit_float(a):
    """uint8 array -> float32 array scaled to 0..1. The input must stay unchanged."""
    raise NotImplementedError


# ------------------------------------------------------------ tests
def test_safe_double():
    r = safe_double(np.array([200, 100], np.uint8))
    assert r.dtype == np.int16, r.dtype
    assert np.array_equal(r, [400, 200]), r


def test_signed_diff():
    r = signed_diff(np.array([10, 200], np.uint8), np.array([20, 100], np.uint8))
    assert r.dtype == np.int16, r.dtype
    assert np.array_equal(r, [-10, 100]), r


def test_clip_u8():
    r = clip_u8(np.array([-5, 100, 300]))
    assert r.dtype == np.uint8, r.dtype
    assert np.array_equal(r, [0, 100, 255]), r


def test_brighten():
    img = np.array([[250, 10]], np.uint8)
    assert np.array_equal(brighten(img, 10), [[255, 20]])
    assert np.array_equal(brighten(img, -20), [[230, 0]])
    assert brighten(img, 5).dtype == np.uint8
    assert np.array_equal(img, [[250, 10]]), "input was modified"


def test_to_unit_float():
    a = np.array([0, 255], np.uint8)
    r = to_unit_float(a)
    assert r.dtype == np.float32, r.dtype
    assert np.allclose(r, [0.0, 1.0]), r
    assert a.dtype == np.uint8


if __name__ == "__main__":
    run(globals())
