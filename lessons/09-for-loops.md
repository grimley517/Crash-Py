---
layout: page
title: "Lesson 9: For Loops with Range"
permalink: /lessons/09-for-loops/
---

## Introduction

### What this lesson is about

You met `for … in` with lists in Lesson 7.  This lesson introduces `range()`,
which generates a sequence of numbers on demand, making it possible to loop a
known number of times without creating a list manually.  You will also look at
nested loops — loops inside loops — and the `break` and `continue` keywords.

### Why you need this

Many mathematical and classroom tasks repeat a fixed number of times: produce a
times table for numbers 1–12, check every integer from 1 to 100, build a grid
of multiplication results.  `range()` combined with a `for` loop is the
standard Python tool for this.

---

## Do

### Step 1 — `range()` basics

```python
for i in range(5):
    print(i)
# 0  1  2  3  4
```

`range(n)` produces the integers `0, 1, 2, …, n-1` (note: **not** `n`).

```python
for i in range(1, 6):
    print(i)
# 1  2  3  4  5
```

`range(start, stop)` starts at `start` and stops *before* `stop`.

```python
for i in range(0, 20, 2):
    print(i, end=" ")
# 0 2 4 6 8 10 12 14 16 18
```

`range(start, stop, step)` counts in steps.

---

### Step 2 — Counting down

```python
for i in range(10, 0, -1):
    print(i, end=" ")
# 10 9 8 7 6 5 4 3 2 1
print("Go!")
```

---

### Step 3 — Times table

```python
n = 7
for i in range(1, 13):
    print(f"{i:2d} × {n} = {i * n:3d}")
```

The `:2d` and `:3d` format specifiers right-align numbers in a fixed-width
column, giving a neat layout.

---

### Step 4 — Accumulating a result

```python
total = 0
for i in range(1, 101):   # sum of 1 to 100
    total += i             # shorthand for total = total + i

print(total)  # 5050
```

---

### Step 5 — Nested loops

A loop *inside* another loop:

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} × {col} = {row * col:2d}", end="   ")
    print()   # newline after each row
```

Output:

```
1 × 1 =  1   1 × 2 =  2   1 × 3 =  3
2 × 1 =  2   2 × 2 =  4   2 × 3 =  6
3 × 1 =  3   3 × 2 =  6   3 × 3 =  9
```

---

### Step 6 — `break` and `continue`

```python
# break — exit the loop early
for i in range(1, 100):
    if i * i > 50:
        print(f"First integer whose square exceeds 50 is {i}")
        break

# continue — skip the rest of this iteration
for i in range(1, 21):
    if i % 3 == 0:
        continue   # skip multiples of 3
    print(i, end=" ")
```

---

### Step 7 — Practical example: prime numbers

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for n in range(2, 50):
    if is_prime(n):
        primes.append(n)

print(primes)
```

> **Download:** [for_loops.py]({{ site.baseurl }}/resources/lesson-05/for_loops.py)

---

## Explore

1. Use a `for` loop to compute the factorial of a number
   (e.g. `5! = 5 × 4 × 3 × 2 × 1 = 120`).
2. Print a multiplication table for all integers from 1 to 12 (a 12 × 12 grid).
3. Write code to find all *Pythagorean triples* `(a, b, c)` where `a`, `b`, and
   `c` are all less than 50 and `a² + b² = c²`.
4. What does `list(range(10))` produce?  When might you want to convert a
   `range` to a `list`?
5. The `enumerate()` function gives you both the index *and* the value while
   iterating over a list:
   `for i, name in enumerate(["Alice", "Bob", "Charlie"]): print(i, name)`.
   Rewrite the times-table exercise to use `enumerate`.

---

[← Lesson 8]({{ site.baseurl }}/lessons/08-decisions/)
[Next: Project — Sieve of Eratosthenes →]({{ site.baseurl }}/lessons/09a-sieve-of-eratosthenes/)
