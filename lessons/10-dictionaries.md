---
layout: page
title: "Lesson 10: Dictionaries"
permalink: /lessons/10-dictionaries/
---

## Introduction

### What this lesson is about

A *dictionary* stores data as *key–value pairs*.  Instead of finding an item
by its position (as with a list), you look it up by name.  This lesson covers
creating dictionaries, reading and updating values, iterating over them, and
common patterns for using them.

### Why you need this

Dictionaries are the natural structure for records — a student's details, a
set of settings, JSON data from the internet.  They appear throughout the
remaining lessons, so a solid grasp of them now pays dividends later.

---

## Do

### Step 1 — Creating a dictionary

```python
student = {
    "name": "Alice",
    "score": 87,
    "grade": "A"
}
```

Keys are usually strings (though they can be any *immutable* type).
Values can be anything.

> **Mutable vs immutable** — An *immutable* object cannot be changed after it
> is created.  Numbers (`int`, `float`), strings, and tuples are immutable:
> once you have `x = 5`, the number `5` itself cannot be altered (you can
> point `x` at a different number, but `5` stays `5`).  A *mutable* object
> *can* be changed after creation — lists and dictionaries are mutable.  This
> distinction matters for dictionary keys because Python needs to compute a
> fixed *hash* for each key to look it up quickly; a mutable object (like a
> list) could change after being inserted, which would break the lookup.
> That is why `{"a": 1}` is valid but `{["a"]: 1}` raises a `TypeError`.

---

### Step 2 — Accessing values

```python
print(student["name"])    # Alice
print(student["score"])   # 87
```

If the key does not exist, Python raises a `KeyError`.  Use `.get()` to
provide a default instead:

```python
print(student.get("age", "unknown"))   # unknown
```

---

### Step 3 — Adding and updating values

```python
student["age"] = 16             # add a new key
student["score"] = 90           # update an existing key
print(student)
```

---

### Step 4 — Removing a key

```python
del student["age"]
removed = student.pop("grade")  # removes and returns the value
print(removed)
```

---

### Step 5 — Checking for a key

```python
if "name" in student:
    print("Name is:", student["name"])
```

---

### Step 6 — Iterating over a dictionary

```python
student = {"name": "Alice", "score": 87, "grade": "A"}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Keys and values together
for key, value in student.items():
    print(f"{key}: {value}")
```

---

### Step 7 — A dictionary of students

```python
class_register = {
    "Alice": 87,
    "Bob":   72,
    "Charlie": 95,
    "Diana": 68,
}

for name, score in class_register.items():
    print(f"{name}: {score}")

# Highest scorer
top_student = max(class_register, key=class_register.get)
print(f"Top student: {top_student} with {class_register[top_student]}")
```

---

### Step 8 — Nested dictionaries

```python
students = {
    "Alice": {"score": 87, "grade": "A"},
    "Bob":   {"score": 72, "grade": "C"},
}

for name, details in students.items():
    print(f"{name}: score={details['score']}, grade={details['grade']}")
```

---

### Step 9 — Using `dict()` and other useful methods

```python
d = dict(a=1, b=2, c=3)   # alternative construction
print(d.keys())            # dict_keys(['a', 'b', 'c'])
print(d.values())          # dict_values([1, 2, 3])
print(len(d))              # 3

d2 = {"d": 4, "e": 5}
d.update(d2)               # merge d2 into d
print(d)
```

> **Download:** [dictionaries.py]({{ site.baseurl }}/resources/lesson-05/dictionaries.py)

---

## Explore

1. Write a function `letter_count(text)` that returns a dictionary where each
   key is a letter and each value is how many times it appears in `text`.
2. Given a list of student scores, write code to build a dictionary mapping
   each score to its grade using the `grade()` function from Lesson 8.
3. What is the difference between `student["missing_key"]` and
   `student.get("missing_key", 0)`?  When is each appropriate?
4. Dictionaries maintain *insertion order* in Python 3.7+.  Write an experiment
   to verify this.
5. Write a function `invert(d)` that swaps keys and values in a dictionary.
   What problem might occur if two keys have the same value?

---

[← Project: Sieve of Eratosthenes]({{ site.baseurl }}/lessons/09a-sieve-of-eratosthenes/)
[Next Lesson: CSV Files →]({{ site.baseurl }}/lessons/11-csv-files/)
