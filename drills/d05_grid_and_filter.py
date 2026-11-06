"""
Pattern E: grid indexing, filtering and sorting (the `show` and `find_boxes` shapes).

Rule: no numpy, no cv2. Plain lists and tuples only.
Run:  python drills/d05_grid_and_filter.py
"""

from _check import raises, run


def grid_pos(i, ncols):
    """Returns (row, col) of item i in a grid with ncols columns. Hint: divmod."""
    raise NotImplementedError


def grid_shape(n, ncols):
    """Returns (nrows, ncols) needed to hold n items.

    Raises ValueError if n < 1 or ncols < 1. No math.ceil needed if you think in integers.
    """
    raise NotImplementedError


def tile_rows(items, ncols):
    """Splits items into rows of ncols; the last row is padded with None."""
    raise NotImplementedError


def check_titles(titles, n):
    """Returns titles as a list of length n.

    titles=None -> [None] * n
    len(titles) != n -> ValueError
    """
    raise NotImplementedError


def keep_large(boxes, min_area):
    """boxes are (x, y, w, h, area) tuples.

    Returns a NEW list without boxes whose area is below min_area, sorted by area,
    largest first. The input list must stay unchanged.
    """
    raise NotImplementedError


# ------------------------------------------------------------ tests
def test_grid_pos():
    assert grid_pos(0, 3) == (0, 0)
    assert grid_pos(4, 3) == (1, 1)
    assert grid_pos(7, 3) == (2, 1)


def test_grid_shape():
    assert grid_shape(7, 3) == (3, 3)
    assert grid_shape(6, 3) == (2, 3)
    assert grid_shape(1, 4) == (1, 4)
    raises(ValueError, grid_shape, 0, 3)
    raises(ValueError, grid_shape, 5, 0)


def test_tile_rows():
    assert tile_rows([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5, None]]
    assert tile_rows([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert tile_rows([1, 2], 5) == [[1, 2, None, None, None]]


def test_check_titles():
    assert check_titles(None, 3) == [None, None, None]
    assert check_titles(["a", "b"], 2) == ["a", "b"]
    raises(ValueError, check_titles, ["a"], 2)


def test_keep_large():
    boxes = [(0, 0, 1, 1, 50), (5, 5, 3, 3, 900), (9, 9, 2, 2, 300), (1, 1, 1, 1, 100)]
    before = list(boxes)
    result = keep_large(boxes, 100)
    assert [b[4] for b in result] == [900, 300, 100], result
    assert boxes == before, "input was modified"
    assert keep_large([], 10) == []


if __name__ == "__main__":
    run(globals())
