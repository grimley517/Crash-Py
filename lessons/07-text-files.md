---
layout: page
title: "Lesson 7: Text Files"
permalink: /lessons/07-text-files/
---

## Introduction

### What this lesson is about

Programs frequently need to read data from files and write results back to files.
This lesson introduces Python's built-in file operations: opening a file,
reading its contents, writing new content, and the `with` statement that ensures
files are closed safely.

### Why you need this

Most real-world data lives in files: student registers, mark sheets, resources
for lessons.  Being able to read from and write to text files gives your Python
programs a way to persist information between runs and process data in bulk.

---

## Do

### Step 1 — Writing to a file

```python
with open("notes.txt", "w") as f:
    f.write("Line one\n")
    f.write("Line two\n")
    f.write("Line three\n")

print("File written.")
```

- `"w"` means *write* mode — it creates the file if it does not exist, or
  **overwrites** it if it does.
- `\n` is the **newline character** — see the box below for a full explanation.
- The `with` statement is explained in detail in Step 2.

> **The `open()` function** accepts many arguments including the filename, the
> *mode*, and an *encoding*.  Full documentation:
> [docs.python.org — open()](https://docs.python.org/3/library/functions.html#open)

> **`\n` — the newline character**
>
> Text files store everything as a sequence of characters.  To mark the end of
> one line and the beginning of the next, a special invisible character is used:
> `\n` (backslash + n).  It is called the **newline** or **line feed** character.
>
> When Python *writes* `"Hello\nWorld"` to a file, the file contains:
> ```
> Hello
> World
> ```
> When Python *reads* a line from a file, the `\n` at the end of each line is
> included in the string — that is why you often call `.strip()` to remove it.
>
> You will also see `\t` (tab) and `\r\n` (Windows-style line ending) in some
> files.  These are all called **escape sequences**: a backslash followed by a
> letter that represents an invisible or hard-to-type character.

---

### Step 2 — The `with` statement

The `with` keyword sets up a **context manager**.  For files, this means Python
automatically closes the file when execution leaves the indented block — even if
an error occurs inside it.

```python
# Without with — you must remember to call f.close()
f = open("notes.txt", "r")
data = f.read()
f.close()   # easy to forget, or skipped when an error occurs

# With with — file is always closed for you
with open("notes.txt", "r") as f:
    data = f.read()
# f is closed here automatically
```

The `as f` part assigns the open file object to the name `f` so you can read
from or write to it inside the block.  When the block ends (or if an exception
is raised), Python calls `f.close()` behind the scenes.

Context managers work with many other Python objects beyond files — database
connections, network sockets, locks — anywhere you need a resource to be
released reliably.

See the official documentation for more detail:
[docs.python.org — The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

---

### Step 3 — Reading an entire file

```python
with open("notes.txt", "r") as f:
    contents = f.read()

print(contents)
```

`"r"` means *read* mode (the default, so you can omit it).

> **File objects** — the `f` inside the `with` block is a file object.  Its
> full API (`.read()`, `.readline()`, `.readlines()`, `.write()`, `.seek()`, …)
> is documented at:
> [docs.python.org — File Objects](https://docs.python.org/3/glossary.html#term-file-object)

---

### Step 4 — Reading line by line

```python
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the trailing \n
```

This approach is memory-efficient for large files because it reads one line at
a time.

---

### Step 5 — Reading all lines into a list

```python
with open("notes.txt", "r") as f:
    lines = f.readlines()

print(lines)          # ['Line one\n', 'Line two\n', 'Line three\n']
print(len(lines))     # 3
print(lines[0].strip())  # Line one
```

Notice that each string in the list ends with `\n` — the newline character that
marks the end of each line in the file.  Calling `.strip()` removes it.

---

### Step 6 — Appending to a file

```python
with open("notes.txt", "a") as f:   # "a" = append mode
    f.write("Line four\n")
```

`"a"` adds content to the *end* of the file without erasing what is already
there.

---

### Step 7 — A practical example: saving a times table

```python
def save_times_table(n, filename):
    with open(filename, "w") as f:
        for i in range(1, 13):
            line = f"{i} × {n} = {i * n}\n"
            f.write(line)

save_times_table(7, "seven_times_table.txt")
print("Times table saved.")
```

---

### Sample file

> **Download:** [sample.txt]({{ site.baseurl }}/resources/lesson-07/sample.txt)
> — a plain-text file containing a short poem, for practice.

> **Download:** [text_files.py]({{ site.baseurl }}/resources/lesson-07/text_files.py)

---

## Explore

1. Write a program that reads `sample.txt` and counts how many lines are in it.
2. Write a program that reads `sample.txt` and prints only lines that contain
   the word "the" (case-insensitive).
3. Write a function `word_count(filename)` that returns the number of words
   in a text file.  Hint: split each line on spaces.
4. What happens if you open a file in `"w"` mode that already has content?
   Write an experiment to find out.
5. Write a program that takes a list of student names and scores and saves them
   to a file with one entry per line, e.g. `"Alice: 87"`.  Then write a second
   program that reads that file back and prints the name of the highest scorer.

---

[← Lesson 6]({{ site.baseurl }}/lessons/06-strings/)
[Next Lesson: Lists →]({{ site.baseurl }}/lessons/08-lists/)
