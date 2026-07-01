---
layout: page
title: "Lesson 20: Unit Testing"
permalink: /lessons/20-unit-testing/
---

## Introduction

### What this lesson is about

A *unit test* is a small, automated check that verifies one specific piece of
your code produces the correct output for a given input.  This lesson introduces
`pytest` — the most popular Python testing framework — and shows you how to
write, organise, and run tests for the functions you have built in earlier
lessons.

### Why you need this

As programs grow, it becomes impossible to manually check every function every
time you make a change.  Automated tests catch mistakes immediately and give you
confidence to refactor code.  This is especially important when writing code
that will be relied upon — such as a grade calculator or a data-processing script.

---

## Do

### Step 1 — Install pytest

```bash
pip3 install pytest
```

---

### Step 2 — A function to test

Create a file `pythagoras.py`:

```python
import math

def hypotenuse(a, b):
    """Return the length of the hypotenuse given the two shorter sides."""
    return math.sqrt(a**2 + b**2)

def shorter_side(hyp, a):
    """Return the missing shorter side given the hypotenuse and one side."""
    return math.sqrt(hyp**2 - a**2)

def is_right_triangle(a, b, c):
    """Return True if a, b, c are the sides of a right-angled triangle."""
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
```

---

### Step 3 — Writing your first tests

Create a file `test_pythagoras.py` (pytest finds files named `test_*.py`):

```python
import math
import pytest
from pythagoras import hypotenuse, shorter_side, is_right_triangle
```

> **Importing from your own modules** — `from pythagoras import …` tells
> Python to look for a file called `pythagoras.py` in the *same directory* as
> `test_pythagoras.py`.  This is an **absolute import**: you name the module
> exactly as its file is named (without `.py`).
>
> Python also supports **relative imports** (e.g. `from . import pythagoras`)
> used inside packages (folders with an `__init__.py` file), where the `.`
> means "the current package".  For simple scripts kept in a single folder,
> absolute imports are clearer and are what you should use here.
>
> If you get a `ModuleNotFoundError`, check that both files are in the same
> folder and that you are running `pytest` (or `python`) from that folder.


def test_hypotenuse_3_4_5():
    assert hypotenuse(3, 4) == 5.0

def test_hypotenuse_5_12_13():
    assert hypotenuse(5, 12) == 13.0

def test_shorter_side_5_3():
    assert shorter_side(5, 3) == 4.0

def test_is_right_triangle_true():
    assert is_right_triangle(3, 4, 5) is True

def test_is_right_triangle_false():
    assert is_right_triangle(3, 4, 6) is False

def test_hypotenuse_floats():
    result = hypotenuse(1, 1)
    assert math.isclose(result, math.sqrt(2))
```

---

### Step 4 — Running the tests

In Terminal, from the folder containing both files:

```bash
pytest
```

You should see output like:

```
============================= test session starts ==============================
collected 6 items

test_pythagoras.py ......                                               [100%]

============================== 6 passed in 0.12s ===============================
```

Each `.` represents a passing test.

---

### Step 5 — A failing test

Change `test_hypotenuse_3_4_5` to expect the wrong answer:

```python
def test_hypotenuse_3_4_5():
    assert hypotenuse(3, 4) == 6.0   # wrong!
```

Run `pytest` again.  Notice how pytest shows you exactly what went wrong:

```
FAILED test_pythagoras.py::test_hypotenuse_3_4_5
AssertionError: assert 5.0 == 6.0
```

Fix it back before moving on.

---

### Step 6 — Testing for exceptions

```python
import pytest

def test_shorter_side_invalid():
    """The short side cannot be longer than the hypotenuse."""
    with pytest.raises(ValueError):
        shorter_side(3, 5)   # 5 > 3, impossible
```

To make this test pass, update `shorter_side` to raise `ValueError` when the
maths is impossible:

```python
def shorter_side(hyp, a):
    if a >= hyp:
        raise ValueError(f"Side {a} cannot be >= hypotenuse {hyp}")
    return math.sqrt(hyp**2 - a**2)
```

---

### Step 7 — Parametrised tests

Instead of repeating similar tests, use `pytest.mark.parametrize`:

```python
@pytest.mark.parametrize("a, b, expected", [
    (3,  4,  5.0),
    (5, 12, 13.0),
    (8, 15, 17.0),
])
def test_hypotenuse_parametrised(a, b, expected):
    assert hypotenuse(a, b) == expected
```

> **Download:** [pythagoras.py]({{ site.baseurl }}/resources/lesson-19/pythagoras.py)
> **Download:** [test_pythagoras.py]({{ site.baseurl }}/resources/lesson-19/test_pythagoras.py)

---

## Explore

1. Write a test for the `grade()` function from Lesson 8.  Make sure you test
   all the boundary values (e.g. exactly 90, 89, 80, 79, …).
2. What happens when two tests have the same name?  Try it and see.
3. Run `pytest -v` (verbose mode) to see the full name of each test as it runs.
4. Write a test that checks `classify_triangle("equilateral", 5, 5, 5)` —
   what do you need to be careful about when testing string return values?
5. Research `pytest` fixtures (`@pytest.fixture`).  How would you use a fixture
   to share a list of sample scores between multiple tests?

---

[← Lesson 19]({{ site.baseurl }}/lessons/19-code-reuse/)
[Next Lesson: Error Handling — try / except →]({{ site.baseurl }}/lessons/21-try-except/)
