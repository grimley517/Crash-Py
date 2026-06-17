---
layout: page
title: "Lesson 6: Strings"
permalink: /lessons/06-strings/
---

## Introduction

### What this lesson is about

A *string* is a sequence of characters — basically any text.  This lesson covers
how to create strings, combine them, extract parts of them, and use Python's
rich set of built-in string methods to manipulate text.

### Why you need this

Data rarely arrives in exactly the right format.  Student names have inconsistent
capitalisation, spreadsheet entries have trailing spaces, and values need to be
formatted for display or saved to files.  String manipulation is therefore an
everyday Python skill.

---

## Do

### Step 1 — Creating strings

Strings can use single quotes, double quotes, or triple quotes:

```python
name = "Alice"
subject = 'Mathematics'
note = """This is a
multi-line string."""
```

Use triple quotes for text that spans more than one line.

---

### Step 2 — Concatenation and repetition

```python
first = "Hello"
second = "World"
message = first + ", " + second + "!"
print(message)   # Hello, World!

line = "-" * 30
print(line)      # ------------------------------
```

---

### Step 3 — f-strings (formatted string literals)

f-strings let you embed values directly inside a string — by far the most
readable way to build strings from variables:

```python
name = "Alice"
score = 87
print(f"{name} scored {score}%")           # Alice scored 87%
print(f"{name} scored {score:.1f}%")       # Alice scored 87.0%
print(f"Double her score: {score * 2}")    # Double her score: 174
```

---

### Step 4 — String methods

Python strings come with many built-in methods:

```python
text = "  Hello, World!  "

print(text.strip())          # "Hello, World!"   — remove whitespace
print(text.upper())          # "  HELLO, WORLD!  "
print(text.lower())          # "  hello, world!  "
print(text.replace("World", "Python"))   # "  Hello, Python!  "
print(text.strip().startswith("Hello"))  # True
print(text.strip().endswith("!"))        # True
```

---

### Step 5 — Splitting and joining

```python
csv_line = "Alice,87,A"
parts = csv_line.split(",")
print(parts)           # ['Alice', '87', 'A']
print(parts[0])        # Alice
print(parts[1])        # 87

# Join a list back into a string
rejoined = " | ".join(parts)
print(rejoined)        # Alice | 87 | A
```

---

### Step 6 — Indexing and slicing

Strings are sequences — you can access individual characters or sub-strings:

```python
word = "Mathematics"

print(word[0])      # M   — first character (index 0)
print(word[-1])     # s   — last character
print(word[0:4])    # Math
print(word[4:])     # ematics
print(word[:4])     # Math
print(len(word))    # 11  — number of characters
```

---

### Step 7 — Checking content

```python
sentence = "The quick brown fox"

print("quick" in sentence)        # True
print(sentence.count("o"))        # 2
print(sentence.find("brown"))     # 10  (index where it starts)
```

---

### Step 8 — Converting other types to strings

```python
score = 95
grade = "A*"

# You cannot concatenate a string and an int directly:
# print("Score: " + score)  ← this raises a TypeError

# Convert with str():
print("Score: " + str(score))   # Score: 95

# Or use an f-string:
print(f"Score: {score}, Grade: {grade}")
```

> **Download:** [strings.py]({{ site.baseurl }}/resources/lesson-06/strings.py)

---

## Explore

1. Write a function `title_case(name)` that converts a full name to title case,
   e.g. `"alice smith"` → `"Alice Smith"`.  Python has a `.title()` method —
   can you find it?
2. A student enters their name as `"  BOB JONES  "`.  Write code to clean it up
   to `"Bob Jones"`.
3. Write a function `initials(full_name)` that returns the initials from a full
   name.  `initials("Alice Mary Smith")` should return `"A.M.S."`.
4. How would you check whether a string represents a whole number?  Look up the
   `.isdigit()` method.
5. f-strings support format specifiers: `f"{3.14159:.2f}"` gives `"3.14"`.
   Experiment with formatting numbers as percentages, with leading zeros, or
   aligned to a fixed width.

---

[← Lesson 5]({{ site.baseurl }}/lessons/05-math-library/)
[Next Lesson: Text Files →]({{ site.baseurl }}/lessons/07-text-files/)
