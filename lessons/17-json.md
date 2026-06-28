---
layout: page
title: "Lesson 17: JSON"
permalink: /lessons/17-json/
---

## Introduction

### What this lesson is about

JSON (*JavaScript Object Notation*) is the most widely used format for
exchanging data between programs and over the internet.  This lesson explains
the JSON format, how it maps directly to Python lists and dictionaries, and how
to convert between JSON text and Python objects using the built-in `json` module.
You will also build a practical example that converts a mark sheet from a CSV
file into a structured JSON file.

### Why you need this

JSON is everywhere: web APIs (covered in the Requests lesson), configuration files, data exports.
Once you understand JSON you will find it easy to work with any modern data
source or web service.

---

## Do

### Step 1 — What JSON looks like

JSON uses the same notation as Python dictionaries and lists, with a few
differences:

```json
{
  "name": "Alice",
  "score": 87,
  "grade": "A",
  "topics": ["Algebra", "Geometry"],
  "passed": true
}
```

| JSON | Python |
|---|---|
| `object { }` | `dict { }` |
| `array [ ]` | `list [ ]` |
| `string " "` | `str` |
| `number` | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

---

### Step 2 — `json.dumps()` — Python → JSON string

```python
import json

student = {
    "name": "Alice",
    "score": 87,
    "grade": "A",
    "topics": ["Algebra", "Geometry"],
    "passed": True
}

json_text = json.dumps(student, indent=2)
print(json_text)
```

`indent=2` makes the output nicely formatted (pretty-printed).

---

### Step 3 — `json.loads()` — JSON string → Python

```python
import json

json_text = '{"name": "Bob", "score": 72, "passed": true}'
data = json.loads(json_text)

print(data["name"])    # Bob
print(type(data))      # <class 'dict'>
```

---

### Step 4 — Reading and writing JSON files

```python
import json

# Write to a file
students = [
    {"name": "Alice", "score": 87},
    {"name": "Bob",   "score": 72},
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

# Read from a file
with open("students.json", "r") as f:
    loaded = json.load(f)

for student in loaded:
    print(student["name"], student["score"])
```

---

### Step 5 — CSV marksheet to JSON

Convert the student scores CSV from Lesson 11 into a structured JSON file:

```python
import csv
import json

students = []

with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({
            "id":    int(row["StudentID"]),
            "name":  row["Name"],
            "topic": row["Topic"],
            "score": int(row["Score"]),
            "grade": row["Grade"],
        })

with open("marksheet.json", "w") as f:
    json.dump(students, f, indent=2)

print(f"Exported {len(students)} students to marksheet.json")
```

---

### Step 6 — Inspecting JSON in VS Code

Open `marksheet.json` in VS Code.  Press `⌘ Shift P` and search for
**"Format Document"** — VS Code will pretty-print the JSON and highlight the
structure.

> **Download:** [json_example.py]({{ site.baseurl }}/resources/lesson-17/json_example.py)
> **Download:** [marksheet.json]({{ site.baseurl }}/resources/lesson-17/marksheet.json)

---

## Explore

1. Modify the marksheet script to group students by topic.  The output JSON
   should look like:
   ```json
   {
     "Algebra": [{"name": "Alice", "score": 85}, ...],
     "Geometry": [...]
   }
   ```
2. What happens if you try to `json.dumps()` a Python object that JSON does not
   support, such as a `datetime` object?  Research the `default` parameter of
   `json.dumps`.
3. Write a script that reads `marksheet.json` and prints the average score for
   each topic.
4. JSON does not support comments.  Why do you think this was a design choice?
   Are there any JSON variants that support comments?
5. Compare the size of `student_scores.csv` and `marksheet.json` for the same
   data.  Which is smaller?  Why?

---

[← Lesson 16]({{ site.baseurl }}/lessons/16-github-pages/)
[Next Lesson: Python Packaging with uv →]({{ site.baseurl }}/lessons/18-uv/)
