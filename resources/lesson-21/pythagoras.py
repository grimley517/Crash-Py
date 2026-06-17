# Lesson 12 - Unit Testing with pytest
# File: pythagoras.py
#
# Run the tests with:  pytest
# (Make sure test_pythagoras.py is in the same folder.)

import math


def hypotenuse(a, b):
    """Return the length of the hypotenuse given the two shorter sides a and b."""
    return math.sqrt(a**2 + b**2)


def shorter_side(hyp, a):
    """Return the missing shorter side given the hypotenuse and one side.

    Raises ValueError if a >= hyp (geometrically impossible).
    """
    if a >= hyp:
        raise ValueError(f"Side {a} cannot be >= hypotenuse {hyp}")
    return math.sqrt(hyp**2 - a**2)


def is_right_triangle(a, b, c):
    """Return True if a, b, c are the side lengths of a right-angled triangle."""
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)


def classify_triangle(a, b, c):
    """Classify a triangle as Equilateral, Isosceles, or Scalene."""
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


def grade(score):
    """Return a letter grade for a percentage score."""
    if score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "U"
