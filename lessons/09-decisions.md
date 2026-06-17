---
layout: page
title: "Lesson 9: Decisions"
permalink: /lessons/09-decisions/
---

## Introduction

### What this lesson is about

Programs need to make decisions — taking different actions depending on
conditions.  This lesson covers Python's `if`, `elif`, and `else` statements,
comparison operators, logical operators, and how to combine them to build
programs that respond intelligently to data.

### Why you need this

Almost every useful program makes decisions.  Assigning a grade from a score,
flagging results that need attention, choosing which calculation to perform —
all of these require conditional logic.  `if` statements are one of the most
fundamental constructs in any programming language.

---

## Do

### Step 1 — A basic `if` statement

```python
score = 75

if score >= 50:
    print("Pass")
```

The indented block runs *only if* the condition is `True`.

---

### Step 2 — `if … else`

```python
score = 45

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

`else` provides the alternative when the condition is `False`.

---

### Step 3 — `if … elif … else`

```python
def grade(score):
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

print(grade(95))   # A*
print(grade(72))   # B
print(grade(40))   # U
```

Python checks conditions from top to bottom and uses the *first* one that is
`True`.

---

### Step 4 — Boolean data (`bool`)

Python has a dedicated boolean type, `bool`, with exactly two values:
`True` and `False`.

```python
is_weekday = True
has_homework = False

print(type(is_weekday))  # <class 'bool'>
print(is_weekday)        # True
print(has_homework)      # False
```

Many decisions in code are based on boolean variables that were computed
earlier in your program.

---

### Step 5 — Comparison operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

```python
print(5 == 5)   # True
print(5 != 3)   # True
print(10 > 20)  # False
```

> **Common mistake:** `=` assigns a value; `==` *compares* two values.

---

### Step 6 — Logical operators

```python
score = 75
attendance = 80

# Both conditions must be True
if score >= 50 and attendance >= 75:
    print("Eligible for certificate")

# At least one condition must be True
if score >= 90 or attendance >= 95:
    print("Distinction candidate")

# Negate a condition
if not score >= 50:
    print("Needs resit")
```

---

### Step 7 — Boolean operations with `and`, `or`, `not`

```python
passed_exam = True
good_attendance = False

print(passed_exam and good_attendance)  # False
print(passed_exam or good_attendance)   # True
print(not passed_exam)                  # False
```

These operators combine or invert booleans and are used constantly in `if`
statements.

---

### Step 8 — Chaining comparisons

Python allows you to chain comparisons naturally:

```python
mark = 73

if 70 <= mark < 80:
    print("Grade B")
```

---

### Step 9 — Practical example: classifying triangles

```python
def classify_triangle(a, b, c):
    """Classify a triangle by its side lengths."""
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print(classify_triangle(5, 5, 5))   # Equilateral
print(classify_triangle(5, 5, 8))   # Isosceles
print(classify_triangle(3, 4, 5))   # Scalene
```

> **Download:** [decisions.py]({{ site.baseurl }}/resources/lesson-09/decisions.py)

---

## Explore

1. Extend the `grade()` function to also print a short comment alongside the
   grade, e.g. "A* — Outstanding".
2. Write a function `is_valid_triangle(a, b, c)` that returns `True` if the
   three lengths can form a triangle.  (Hint: the sum of any two sides must be
   greater than the third side.)
3. What is the difference between `is` and `==` in Python?  When does using
   `is` give unexpected results?
4. Write a function `fizzbuzz(n)` that returns `"Fizz"` if `n` is divisible
   by 3, `"Buzz"` if divisible by 5, `"FizzBuzz"` if divisible by both, and
   the number itself otherwise.
5. Can you write a `grade()` function using a *dictionary* instead of
   `if … elif`?  (Hint: this is tricky — come back to it after Lesson 8.)

---

[← Lesson 7]({{ site.baseurl }}/lessons/08-lists/)
[Next Lesson: For Loops →]({{ site.baseurl }}/lessons/10-for-loops/)
