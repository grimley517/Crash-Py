---
layout: page
title: "Lesson 5: Reading Library Documentation"
permalink: /lessons/05-math-library/
---

## Introduction

### What this lesson is about

Python comes with a large [standard library](https://docs.python.org/3/library/)
— hundreds of ready-made modules covering maths, file handling, dates, internet
access, and much more.  This lesson focuses on the
[`math` module](https://docs.python.org/3/library/math.html) as a practical
example of **how to read and navigate official Python documentation**.

### Why you need this

Every library you meet in this course has official documentation.  Learning how
to read docs is more valuable than memorising any particular function:
documentation tells you every function a module provides, what arguments it
takes, what it returns, and what errors it raises — all with examples.

---

## Do

### Step 1 — Where to find documentation

The official Python documentation lives at:

> **<https://docs.python.org/3/>**

The [`math` module reference](https://docs.python.org/3/library/math.html)
lists every function and constant the module provides, organised into sections:
*Number-theoretic functions*, *Trigonometric functions*, *Angular conversion*,
*Hyperbolic functions*, *Special functions*, and *Constants*.

---

### Step 2 — Reading a function entry

Every entry in the docs follows the same pattern.  For example:

```
math.sqrt(x)
```

> Return the square root of *x*.

The docs tell you:
- **Name:** `math.sqrt`
- **Parameter:** `x` — the number whose square root you want
- **Return value:** the square root as a `float`
- **Special behaviour:** raises `ValueError` if `x` is negative

Try it:

```python
import math

print(math.sqrt(25))    # 5.0
print(math.sqrt(2))     # 1.4142135623730951
```

---

### Step 3 — Constants

> **What is a constant?**  A *constant* is a value that never changes while a
> program runs.  Mathematical constants such as π are perfect examples: they
> have a precise, fixed value defined by mathematics.  In Python, `math.pi` is
> not something you set — you simply read it.  By convention, names written in
> ALL_CAPITALS (e.g. `MAX_STUDENTS = 30`) are treated as constants by
> programmers even though Python doesn't technically enforce this; the `math`
> module's constants are a real-world example of this idea.

The `math` module provides two important constants.  From the
[docs](https://docs.python.org/3/library/math.html#constants):

| Constant | Value | Meaning |
|---|---|---|
| `math.pi` | 3.141592… | The ratio of a circle's circumference to its diameter |
| `math.e` | 2.718281… | Euler's number, the base of natural logarithms |
| `math.tau` | 6.283185… | τ = 2π |
| `math.inf` | ∞ | Positive infinity |
| `math.nan` | NaN | "Not a Number" — result of undefined operations |

```python
import math

print(math.pi)     # 3.141592653589793
print(math.e)      # 2.718281828459045
print(math.tau)    # 6.283185307179586
```

---

### Step 4 — Number-theoretic functions

From the [docs](https://docs.python.org/3/library/math.html#number-theoretic-functions):

```python
import math

print(math.floor(3.7))    # 3  — largest integer ≤ x
print(math.ceil(3.2))     # 4  — smallest integer ≥ x
print(math.trunc(3.9))    # 3  — truncate towards zero
print(math.fabs(-5.5))    # 5.5 — absolute value as float
print(math.factorial(6))  # 720 — 6! = 6×5×4×3×2×1
print(math.gcd(12, 8))    # 4  — greatest common divisor
```

> **Note:** `math.floor()` and `math.ceil()` return `int`, while `math.fabs()`
> always returns `float`.  The docs make this distinction explicit.

---

### Step 5 — Trigonometric functions

The [trig functions](https://docs.python.org/3/library/math.html#trigonometric-functions)
all work in **radians**, not degrees.  Use `math.radians()` to convert:

```python
import math

angle_deg = 30
angle_rad = math.radians(angle_deg)   # convert first

print(math.sin(angle_rad))   # 0.49999999999999994  ≈ 0.5
print(math.cos(angle_rad))   # 0.8660254037844387   ≈ √3/2
print(math.tan(angle_rad))   # 0.5773502691896257   ≈ 1/√3
```

And in reverse:

```python
import math

result = math.asin(0.5)              # arcsin in radians
print(math.degrees(result))          # 30.000000000000004 ≈ 30°
```

---

### Step 6 — Logarithms and powers

From the [docs](https://docs.python.org/3/library/math.html#power-and-logarithmic-functions):

```python
import math

print(math.log(math.e))       # 1.0  — natural log (base e)
print(math.log10(1000))       # 3.0  — log base 10
print(math.log2(8))           # 3.0  — log base 2
print(math.log(8, 2))         # 3.0  — log(x, base) — two-argument form
print(math.exp(1))            # 2.718… — e raised to the power 1
print(math.pow(2, 10))        # 1024.0 — same as 2**10, always float
```

> **When to use `math.pow()` vs `**`:** `math.pow()` always returns a `float`
> and is slightly faster for fractional exponents; `**` preserves the type
> of its operands.

> **Many ways to do the same thing** — you may have noticed that `math.pow(2,
> 10)` and `2 ** 10` produce the same result.  This is common in Python:
> there are often several approaches to a problem, each with small trade-offs
> in readability, speed, or the type of the result.  *Efficiency* in
> programming means choosing the approach that is fast enough *and* easy to
> understand — a function that runs in one millisecond but is impossible to
> read is rarely worth it.  For now, prefer the approach that makes the code
> clearest; you can optimise later if speed becomes a real concern.

---

### Step 7 — Using `help()` offline

You can read documentation without a browser directly in the Python REPL or a
script.  Start Python in the terminal and type:

```python
import math
help(math.sqrt)
```

This prints the docstring for `math.sqrt`.  To see the full module:

```python
help(math)
```

Press `q` to quit the pager.

---

## Explore

1. Look up [`math.comb(n, k)`](https://docs.python.org/3/library/math.html#math.comb)
   in the documentation.  What does it compute?  Write a short example using it
   to answer: "In how many ways can I choose 3 students from a class of 30?"
2. The docs list `math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)`.  What do
   `rel_tol` and `abs_tol` mean?  When would you need `abs_tol`?
3. Read the [`math.hypot()`](https://docs.python.org/3/library/math.html#math.hypot)
   entry.  How does it relate to the `hypotenuse()` function you wrote in
   Lesson 3?  Rewrite that function using `math.hypot()`.
4. Explore the [`math.isfinite()`](https://docs.python.org/3/library/math.html#math.isfinite),
   `math.isinf()`, and `math.isnan()` functions.  When might these be useful in
   real data processing?
5. Python also has a [`statistics`](https://docs.python.org/3/library/statistics.html)
   module in the standard library.  Browse its documentation and identify three
   functions you think would be useful when analysing student marks.

---

[← Lesson 4]({{ site.baseurl }}/lessons/04-docstrings/)
[Next Lesson: Strings →]({{ site.baseurl }}/lessons/06-strings/)
