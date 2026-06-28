---
layout: page
title: "Lesson 3: Mathematical Operations"
permalink: /lessons/03-mathematics/
---

## Introduction

### What this lesson is about

Python is an excellent calculator.  This lesson covers how Python represents
numbers, the arithmetic operators it supports, and how to build useful maths
functions — specifically Pythagoras' theorem functions that will feel immediately
relevant to a maths teacher.

### Why you need this

Understanding Python's number types and operators is the foundation of any
quantitative work — statistics, data analysis, graph plotting — all of which
appear in later lessons.  Writing Pythagoras functions is also a natural first
exercise in combining maths knowledge with the functions you learned in Lesson 2.

---

## Do

Start a new file `mathematics.py` in your project folder

### Step 1 — Number types

Python has two main numeric types:

| Type | Example | Notes |
|---|---|---|
| `int` | `5`, `-3`, `0` | Whole numbers, no decimal point |
| `float` | `3.14`, `-0.5` | Numbers with a decimal point |

```python
a = 10       # int
b = 3.5      # float
print(type(a))   # <class 'int'>
print(type(b))   # <class 'float'>
```

Python also understands complex numbers, read the [documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) for more details.

---

### Step 2 — Arithmetic operators

```python
print(5 + 3)    # Addition       → 8
print(10 - 4)   # Subtraction    → 6
print(3 * 7)    # Multiplication → 21
print(15 / 4)   # Division       → 3.75  (always returns float)
print(15 // 4)  # Floor division → 3     (drops the decimal)
print(15 % 4)   # Modulo         → 3     (remainder)
print(2 ** 8)   # Exponentiation → 256
```

> **Key point:** `/` always gives a `float`.  `//` gives an `int` (rounded
> *down*).

---

### Step 3 — The `math` module

> **What is a library?**  A *library* (also called a *module*) is a collection
> of pre-written code that you can use in your own programs.  Python comes with
> a large *standard library* of modules covering maths, file handling, dates,
> internet access, and much more — all free to use without installing anything
> extra.  You tell Python to load a module with the `import` keyword.  We will
> explore how to read library documentation in depth in the next lesson.

Python's built-in `math` module provides many useful functions:

```python
import math               # Import statements generally go at the very top of the code 

print(math.sqrt(16))      # 4.0  — square root
print(math.pi)            # 3.141592...
print(math.floor(3.9))    # 3  — round down
print(math.ceil(3.1))     # 4  — round up
print(math.fabs(-7))      # 7.0 — absolute value
```

The math library is a built in library. Further details are available from the [math library documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

The lowest common multiple of 6 and 9 is 3. use the library to write a print statement to print this out.

---

### Step 4 — Pythagoras: find the hypotenuse

Pythagoras' theorem states that for a right-angled triangle:

> **c² = a² + b²**

So the hypotenuse `c` is `√(a² + b²)`.

```python
import math

def hypotenuse(a, b):
    """Return the length of the hypotenuse given the two shorter sides."""
    pass # replace this with code to find a hypotenuse.

print(hypotenuse(3, 4))    # 5.0
print(hypotenuse(5, 12))   # 13.0
```

Complete the function to make it work. Hint: math is already imported in your file you don't need to import it again.

---

### Step 5 — Pythagoras: find a shorter side

If you know the hypotenuse `c` and one shorter side `a`, the other short side is:

> **b = √(c² − a²)**

```python
def shorter_side(hyp, a):
    """Return the missing shorter side given the hypotenuse and one side."""
    pass   # replace this with code to find a shorter side.

print(shorter_side(5, 3))    # 4.0
print(shorter_side(13, 5))   # 12.0
```

Correct the fnction to make it work


---

### Step 6 — Order of operations

Python follows standard BODMAS / BIDMAS rules.  Use parentheses to be explicit:

```python
print(2 + 3 * 4)    # 14  (multiplication first)
print((2 + 3) * 4)  # 20  (brackets first)
```

---

### Step 7 — Numeric type gotchas

Python's number types have some important quirks you should know before using
them for serious maths work.

### Float precision

Floats are stored in binary, which cannot represent some decimal fractions
exactly.  This leads to surprising results:

```python
print(0.1 + 0.2)       # 0.30000000000000004  (not exactly 0.3!)
print(0.1 + 0.2 == 0.3)  # False
```

To compare floats, use `math.isclose()` instead of `==`:

```python
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True
```

### Division always returns a float

```python
print(10 / 2)    # 5.0 — not 5
print(type(10 / 2))   # <class 'float'>
```

If you need a whole-number result, use `//` (floor division):

```python
print(10 // 3)   # 3  (rounds down)
print(-7 // 2)   # -4 (rounds towards negative infinity!)
```

### Mixed arithmetic promotes to float

```python
print(type(3 + 2))      # <class 'int'>   — int + int → int
print(type(3 + 2.0))    # <class 'float'> — int + float → float
```

### Integers have unlimited precision

Unlike many languages, Python integers can be arbitrarily large with no
overflow:

```python
print(2 ** 100)   # 1267650600228229401496703205376 — exact!
```

### Converting between types

Use `int()` and `float()` to convert explicitly:

```python
x = int(3.9)    # 3  — truncates (does NOT round)
y = float(7)    # 7.0
z = int("42")   # 42 — works on numeric strings too
```

> **Download:** [pythagoras.py]({{ site.baseurl }}/resources/lesson-03/pythagoras.py)

---

## Explore

1. Write a function `circle_area(radius)` that returns the area of a circle.
   Use `math.pi`.
2. What is `7 % 3`?  What does the modulo operator tell you in practical terms
   — A leap year is divisible by 4 except for century years, which are not leap years. Write a function to check if a year is a leap year.
3. Rewrite the hypotenuse function to return the answer correct to 2 decimal places (hint: look in the documentation for the math module)
4. What happens when you try `math.sqrt(-1)`?
   - Python has a `cmath` (complex
   math) module — can you find out how to compute complex square roots?

---

[← Lesson 2]({{ site.baseurl }}/lessons/02-functions/)
[Next Lesson: Docstrings →]({{ site.baseurl }}/lessons/04-docstrings/)
