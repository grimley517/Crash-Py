---
layout: page
title: "Lesson 9a: Project — Sieve of Eratosthenes"
permalink: /lessons/09a-sieve-of-eratosthenes/
---

## About this project

This is a **project lesson**.  Unlike the numbered lessons, it does not follow
the *Introduction → Do → Explore* pattern.  Instead it walks you along a single
guided route to a finished piece of software, then leaves you with some
open-ended ideas to explore once it works.

The goal: find **every prime number from 1 to 1,000,000** and save them all to a
plain-text file, one per line.

By the time you reach the end you will have combined several things you already
know — numbers (Lesson 3, *Mathematical Operations*), lists and `for` loops
(Lesson 7, *Lists*), the `range()` function (Lesson 9, *For Loops with Range*),
and text files (Lesson 6, *Text Files*) — into a real, useful program that
produces a genuine data file.

### The learning objective

The real point of this project is not the primes themselves — it is learning to
follow and implement an **algorithm**.  An algorithm is simply a precise,
step-by-step recipe for solving a problem: a fixed sequence of instructions
that, if you follow them exactly, always produces the right answer.  A cooking
recipe is an everyday algorithm; the *Sieve of Eratosthenes* is a mathematical
one.  By the end of this project you will have taken an algorithm described in
plain English and turned it, step by step, into working Python code.

---

## What you will build

A script called `sieve.py` that:

1. Uses the *Sieve of Eratosthenes* **algorithm** (a step-by-step recipe,
   explained below) to find all primes up to a limit.
2. Writes those primes to `primes.txt`, one number per line.
3. Prints a short summary (how many primes it found, and how long it took).

A **prime number** is a whole number greater than 1 that has no divisors other
than 1 and itself: 2, 3, 5, 7, 11, 13, …  There are 78,498 of them below one
million, so this is far too many to find by hand — exactly the kind of job a
computer is good at.

---

## Before you start

You should already be comfortable with:

- Numbers and arithmetic operators — Lesson 3 (*Mathematical Operations*).
- Lists, and reading list items by their index — Lesson 7 (*Lists*).
- `for` loops and the `range()` function — Lesson 9 (*For Loops with Range*).
- Writing to a text file with `with open(...)` — Lesson 6 (*Text Files*).

This project brings all four of those together, so it sits after the lessons on
lists and ranges rather than earlier in the course.

Create a new folder for the project and open it in VS Code:

```bash
mkdir sieve-project
cd sieve-project
code .
```

Create an empty file called `sieve.py` — you will fill it in step by step.

---

## The idea behind the sieve

Eratosthenes was a Greek mathematician who, over 2,000 years ago, described a
beautifully simple way to find primes.  Imagine writing every number from 2 up
to your limit on a big grid:

1. Start at the first number, 2.  It is prime.  Now cross out **every multiple**
   of 2 (4, 6, 8, …) — none of those can be prime.
2. Move to the next number that is *not* crossed out.  That is 3, and it is
   prime.  Cross out every multiple of 3 (6, 9, 12, …).
3. The next un-crossed number is 5 (4 was already crossed out).  Cross out its
   multiples.
4. Keep going.  Every time you land on a number that has not been crossed out,
   it is prime, and you cross out all of its multiples.

When you have finished, every number still standing is a prime.  We will
represent "crossed out" with a list of `True`/`False` flags.

---

## Building it step by step

### Step 1 — Set up the list of flags

We use a **list** of booleans (`True`/`False` values) called `is_prime`, with one
entry for every number from 0 up to `limit`.  We start by *assuming* every
number is prime (`True`), then cross out the ones that are not.

```python
limit = 1_000_000

# is_prime[n] is True if n might still be prime.
# Index 0 and 1 are not prime, so start them as False.
is_prime = [True] * (limit + 1)
is_prime[0] = False
is_prime[1] = False
```

> **Recap: lists and indexes**
>
> A **list** (Lesson 7, *Lists*) is an ordered collection of values.  Each value
> has a position number called its **index**, and Python counts indexes from
> **0**, not 1.  So in the list `["a", "b", "c"]` the value `"a"` is at index 0,
> `"b"` at index 1, and `"c"` at index 2.  You read a value with square
> brackets: `my_list[0]` gives `"a"`.
>
> The clever trick in this project is that we use *the number itself as the
> index*.  `is_prime[7]` tells us whether the number 7 is still prime, and
> `is_prime[7] = False` crosses 7 out.  Storing information at the index that
> matches the number is what makes the sieve so fast.

`[True] * (limit + 1)` builds a list of `limit + 1` copies of `True`.  We use
`limit + 1` rather than `limit` because indexes start at 0: to have a valid
index all the way up to `limit` itself (index `1_000_000`), the list needs
`1_000_001` entries.

Notice `1_000_000` — Python lets you put underscores in numbers to make them
readable.  It means exactly the same as `1000000`.

---

### Step 2 — Cross out the multiples

Now walk through the numbers.  Whenever `is_prime[n]` is still `True`, mark every
multiple of `n` as `False`.

```python
for n in range(2, limit + 1):
    if is_prime[n]:
        # Cross out 2n, 3n, 4n, ... up to the limit.
        for multiple in range(n * n, limit + 1, n):
            is_prime[multiple] = False
```

Two details worth understanding:

- We start crossing out at `n * n`, not `2 * n`.  Any smaller multiple of `n`
  (like `2 * n` or `3 * n`) was already crossed out by a smaller prime, so we
  can safely skip straight to `n * n`.
- `range(n * n, limit + 1, n)` counts up in steps of `n`: `n*n`, `n*n + n`,
  `n*n + 2n`, and so on — exactly the multiples of `n`.

---

### Step 3 — Collect the primes into a list

After the sieve has run, the primes are every index whose flag is still `True`.
Gather them into a new list using a list comprehension (Lesson 7, *Lists*).

```python
primes = [n for n in range(2, limit + 1) if is_prime[n]]

print(f"Found {len(primes)} primes up to {limit}.")
```

A **list comprehension** `[expression for item in sequence if condition]` is a
compact way to build a list.  Read the line above as: "collect `n` for every
`n` from 2 to the limit, but only if `is_prime[n]` is `True`."

---

### Step 4 — Write the primes to a text file

This is where Lesson 6 (*Text Files*) pays off.  Open a file in write mode and
write each prime on its own line, followed by the newline character `\n`.

```python
with open("primes.txt", "w") as f:
    for prime in primes:
        f.write(f"{prime}\n")

print("Primes written to primes.txt")
```

Remember from Lesson 6 (*Text Files*) that `"w"` creates the file (or overwrites
it) and that `\n` starts a new line, so each prime ends up on its own line.

---

### Step 5 — Time how long it takes

One million numbers is enough that the speed of the sieve is worth measuring.
Python's built-in `time` module can tell you how many seconds a block of code
took.

Why bother timing it?  Because a measurement is the only way to know whether a
*change* to your code actually made it faster.  If you later rewrite the
algorithm (see the Explore section), you can compare the new time against this
one and see, objectively, whether you improved it or made it worse.  "It feels
faster" is a guess; a number of seconds is evidence.

```python
import time

start = time.perf_counter()

# ... the sieve, list building, and file writing go here ...

elapsed = time.perf_counter() - start
print(f"Done in {elapsed:.2f} seconds.")
```

`time.perf_counter()` returns a running count of seconds.  Record it before and
after, then subtract to get how long the work took.  `{elapsed:.2f}` formats the
number to two decimal places.

---

### Step 6 — Put it all together

Here is the complete script.  Type it into `sieve.py` (or download the finished
version from the resources below) and run it.

```python
import time


def sieve_of_eratosthenes(limit):
    """Return a list of all prime numbers from 2 up to and including limit."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for n in range(2, limit + 1):
        if is_prime[n]:
            for multiple in range(n * n, limit + 1, n):
                is_prime[multiple] = False

    return [n for n in range(2, limit + 1) if is_prime[n]]


def save_primes(primes, filename):
    """Write each prime to filename, one number per line."""
    with open(filename, "w") as f:
        for prime in primes:
            f.write(f"{prime}\n")


if __name__ == "__main__":
    limit = 1_000_000

    start = time.perf_counter()
    primes = sieve_of_eratosthenes(limit)
    save_primes(primes, "primes.txt")
    elapsed = time.perf_counter() - start

    print(f"Found {len(primes)} primes up to {limit:,}.")
    print(f"Saved to primes.txt in {elapsed:.2f} seconds.")
```

Run it from the terminal:

```bash
python3 sieve.py
```

You should see something like:

```
Found 78498 primes up to 1,000,000.
Saved to primes.txt in 0.35 seconds.
```

Open `primes.txt` in VS Code.  It should begin `2`, `3`, `5`, `7`, `11`, … and
end with `999983` — the largest prime below one million.

> **Download:** [sieve.py]({{ site.baseurl }}/resources/lesson-09a/sieve.py)
> — the complete project script.

---

## Explore

Now that the project works, try extending it.  These are open-ended — there is
no single right answer.

1. Change `limit` to 100 and print the primes to the screen instead of a file.
   Check them against a list of primes you find online.
2. Count how many primes fall in each block of 100,000 (0–100,000,
   100,000–200,000, and so on).  Do primes get rarer as numbers get larger?
3. Write the primes to the file separated by commas on a single line instead of
   one per line.  Which format would be easier for another program to read back?
4. Read `primes.txt` back in (Lesson 6, *Text Files*) and find the largest gap
   between two consecutive primes below one million.
5. Time the sieve for limits of 100,000, 1,000,000, and 10,000,000.  How does the
   time grow as the limit gets bigger?
6. The classic sieve uses a lot of memory for very large limits.  Research the
   *Sieve of Sundaram* or a *segmented sieve* — how do they differ?

---

[← Lesson 9: For Loops with Range]({{ site.baseurl }}/lessons/09-for-loops/)
[Next Lesson: Dictionaries →]({{ site.baseurl }}/lessons/10-dictionaries/)
