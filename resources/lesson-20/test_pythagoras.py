# Lesson 20 - Unit Testing with pytest
# File: test_pythagoras.py
#
# Run with:  pytest
# Or verbose:  pytest -v

import math
import pytest
from pythagoras import hypotenuse, shorter_side, is_right_triangle, classify_triangle, grade


# ── hypotenuse ────────────────────────────────────────────────────────────────

def test_hypotenuse_3_4_5():
    assert hypotenuse(3, 4) == 5.0

def test_hypotenuse_5_12_13():
    assert hypotenuse(5, 12) == 13.0

def test_hypotenuse_8_15_17():
    assert hypotenuse(8, 15) == 17.0

def test_hypotenuse_floats():
    result = hypotenuse(1, 1)
    assert math.isclose(result, math.sqrt(2))

@pytest.mark.parametrize("a, b, expected", [
    (3,  4,  5.0),
    (5, 12, 13.0),
    (8, 15, 17.0),
    (7, 24, 25.0),
])
def test_hypotenuse_parametrised(a, b, expected):
    assert hypotenuse(a, b) == expected


# ── shorter_side ──────────────────────────────────────────────────────────────

def test_shorter_side_5_3():
    assert shorter_side(5, 3) == 4.0

def test_shorter_side_13_5():
    assert shorter_side(13, 5) == 12.0

def test_shorter_side_invalid_raises():
    with pytest.raises(ValueError):
        shorter_side(3, 5)   # 5 > 3, impossible

def test_shorter_side_equal_raises():
    with pytest.raises(ValueError):
        shorter_side(5, 5)   # equal, hypotenuse must be strictly greater


# ── is_right_triangle ─────────────────────────────────────────────────────────

def test_is_right_triangle_true():
    assert is_right_triangle(3, 4, 5) is True

def test_is_right_triangle_false():
    assert is_right_triangle(3, 4, 6) is False

def test_is_right_triangle_sides_any_order():
    assert is_right_triangle(5, 3, 4) is True


# ── classify_triangle ─────────────────────────────────────────────────────────

def test_classify_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"

def test_classify_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"

def test_classify_scalene():
    assert classify_triangle(3, 4, 5) == "Scalene"


# ── grade ─────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("score, expected_grade", [
    (100, "A*"),
    (90,  "A*"),
    (89,  "A"),
    (80,  "A"),
    (79,  "B"),
    (70,  "B"),
    (69,  "C"),
    (60,  "C"),
    (59,  "D"),
    (50,  "D"),
    (49,  "U"),
    (0,   "U"),
])
def test_grade_boundaries(score, expected_grade):
    assert grade(score) == expected_grade
