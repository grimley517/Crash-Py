---
layout: page
title: "Lesson 21: Error Handling — try / except"
permalink: /lessons/21-try-except/
---

## Introduction

### What this lesson is about

When a Python program encounters an unexpected condition — a missing file, an
invalid input, a network timeout — it raises an **exception**.  By default this
crashes the program with an error message.  The `try … except` statement lets
you *catch* exceptions and respond to them gracefully instead.

### Why you need this

The next lesson uses the `requests` library to fetch data from the internet.
Network calls can fail for many reasons: no internet connection, a server that
is down, an invalid URL.  Without error handling your program will crash; with
`try … except` you can detect the failure, print a helpful message, and continue
or retry.

Error handling is also essential for reading files, parsing user input, and any
operation that depends on external resources you do not fully control.

> **Official documentation:**
> [docs.python.org — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

---

## Do

### Step 1 — What is an exception?

Run this script and observe the output:

```python
print(10 / 0)
```

Python raises a `ZeroDivisionError` and stops.  The full traceback tells you:
- *What* went wrong (`ZeroDivisionError: division by zero`)
- *Where* it went wrong (the file name and line number)

Every type of error in Python is a specific **exception class**.  Some common
ones:

| Exception | When it occurs |
|---|---|
| `ZeroDivisionError` | Dividing by zero |
| `FileNotFoundError` | Opening a file that does not exist |
| `ValueError` | Wrong type of value (e.g. `int("abc")`) |
| `TypeError` | Wrong type of argument (e.g. `"hello" + 5`) |
| `KeyError` | Accessing a dict key that does not exist |
| `IndexError` | Accessing a list index that is out of range |
| `ConnectionError` | Network connection failed |

---

### Step 2 — Basic `try … except`

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Program continues here.")
```

### How it works:
1. Python executes the `try` block.
2. If an exception matching `except` is raised, execution jumps to the `except`
   block.
3. Execution continues after the whole `try … except` statement.

---

### Step 3 — Catching multiple exceptions

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero.")
        return None
    except TypeError:
        print("Error: arguments must be numbers.")
        return None

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Error: division by zero.
print(safe_divide(10, "x"))  # Error: arguments must be numbers.
```

You can chain as many `except` clauses as you need — Python checks them in order
and runs the first one that matches.

---

### Step 4 — The `else` and `finally` clauses

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That is not a valid number.")
else:
    # Runs only when no exception was raised
    print(f"You entered: {number}")
finally:
    # Always runs, exception or not — use for clean-up
    print("Done.")
```

| Clause | When it runs |
|---|---|
| `except` | Only when the specified exception was raised |
| `else` | Only when *no* exception was raised |
| `finally` | Always — exception or not |

`finally` is useful for releasing resources (closing files, database
connections) when you are not using a `with` statement.

---

### Step 5 — Catching any exception

You can use a bare `except Exception as e` to catch any exception and inspect
the error message:

```python
try:
    result = int("not a number")
except Exception as e:
    print(f"Something went wrong: {e}")
    print(f"Exception type: {type(e).__name__}")
```

> **Caution:** Catching all exceptions with `except Exception` (or, worse,
> `except:`) can hide bugs.  Prefer catching specific exception types whenever
> you know what can go wrong.

---

### Step 6 — File handling with `try … except`

A file operation that may fail deserves error handling.  Here `with` and
`try … except` work together:

```python
filename = "data.txt"

try:
    with open(filename, "r") as f:
        contents = f.read()
    print(contents)
except FileNotFoundError:
    print(f"'{filename}' was not found.  Check the file name and path.")
except PermissionError:
    print(f"You do not have permission to read '{filename}'.")
```

When a `FileNotFoundError` is raised inside the `with` block, the `with`
statement still closes the file (or rather, since the file was never opened,
there is nothing to close), and the `except` clause handles the error cleanly.

---

### Step 7 — Raising your own exceptions

You can raise exceptions yourself to signal error conditions in your own code:

```python
def square_root(n):
    if n < 0:
        raise ValueError(f"Cannot take the square root of a negative number: {n}")
    return n ** 0.5

try:
    print(square_root(25))   # 5.0
    print(square_root(-4))   # raises ValueError
except ValueError as e:
    print(f"Invalid input: {e}")
```

`raise` stops the current function and propagates the exception upward to the
nearest matching `except` clause.

---

## Explore

1. Write a function `safe_open(filename)` that returns the contents of a text
   file, or `None` if the file does not exist.  Use `try … except`.
2. What exception does `[][0]` raise?  What about `{}["missing"]`?  Write a
   small function that catches both and returns a default value.
3. The `finally` clause always runs.  What happens if you put a `return`
   statement inside a `try` block and also inside `finally`?  Try it and
   explain the result.
4. Look up [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
   in the official exception hierarchy.  What is its parent class?  What is the
   root of all Python exceptions?
5. Write a program that asks the user to enter two numbers and prints their
   quotient.  Handle the case where the user types a non-number, and the case
   where they type zero as the denominator.

---

[← Lesson 20]({{ site.baseurl }}/lessons/20-unit-testing/)
[Next Lesson: Jupyter Notebooks →]({{ site.baseurl }}/lessons/22-jupyter/)
