---
layout: page
title: "Lesson 11: CSV Files"
permalink: /lessons/11-csv-files/
---

## Introduction

### What this lesson is about

CSV (*Comma-Separated Values*) is one of the most important and universal data
formats in computing.  A CSV file is plain text: each line represents a row of
a table, and values in each row are separated by commas.  This makes it
readable in any text editor and importable by virtually every application —
Excel, Google Sheets, databases, statistical tools, and Python.

Python's built-in `csv` module (part of the standard library — no installation
needed) provides tools for reading, writing, and processing CSV files reliably.

### Why you need this

CSV is the *lingua franca* of data exchange.  As a teacher you will encounter
CSV files from mark books, assessment exports, registration systems, and open
government datasets.  Because CSV is plain text rather than a binary format,
it is easier to inspect, diff, and automate than an Excel file.  Many of the
large public datasets you will encounter in later lessons are provided in CSV.

---

## Do

### Step 1 — The CSV format

Open a plain text file and type the following — this is what a CSV file looks like:

```
StudentID,Name,Topic,Score
1,Alice,Algebra,85
2,Bob,Geometry,72
3,Charlie,Statistics,91
```

Key rules of the CSV format:
- The **first row** is usually a *header* listing column names.
- Every subsequent row contains one record.
- Values are separated by commas; the number of columns must be consistent.
- If a value contains a comma, it is wrapped in double-quotes: `"Smith, Alice"`.
- The file extension is `.csv` and encoding is usually UTF-8.

> **Download:** [student_scores.csv]({{ site.baseurl }}/resources/lesson-05/student_scores.csv)

---

### Step 2 — Reading a CSV file

```python
import csv

with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Each `row` is a **list** of strings.  The `newline=""` argument prevents
double-spacing on Windows — always include it when opening CSV files.

---

### Step 3 — Skipping the header row

```python
import csv

with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)   # read (and skip) the first row
    print("Columns:", header)

    for row in reader:
        print(row)
```

---

### Step 4 — DictReader (recommended)

`csv.DictReader` maps each row to a dictionary using the header as keys —
much easier to work with than remembering column indices:

```python
import csv

with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], "scored", row["Score"])
```

---

### Step 5 — Computing statistics from CSV

```python
import csv

scores = []

with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        scores.append(int(row["Score"]))

print(f"Average: {sum(scores) / len(scores):.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest:  {min(scores)}")
```

Note: values from a CSV are always strings — convert them with `int()` or
`float()` as needed.

---

### Step 6 — Calculating letter grades from marks

A real-world task for a maths teacher: given a mark out of 100, assign a
letter grade according to a mark scheme.  Write a function to do this, then
apply it to every row in the CSV:

```python
import csv

def letter_grade(score):
    """Return the letter grade for a numeric score out of 100."""
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

results = []

with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        score = int(row["Score"])
        grade = letter_grade(score)
        results.append({
            "Name": row["Name"],
            "Score": score,
            "Calculated Grade": grade,
        })

for r in results:
    print(f"{r['Name']:15} {r['Score']:3}  →  {r['Calculated Grade']}")
```

Try adjusting the thresholds in `letter_grade()` and re-running — this is
exactly the kind of script you would use to apply a new mark scheme to an
entire class instantly.

---

### Step 7 — Writing a CSV file

```python
import csv

results = [
    ["Name", "Score", "Grade"],
    ["Alice", 85, "A"],
    ["Bob",   72, "C"],
    ["Charlie", 95, "A*"],
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

print("output.csv written.")
```

> **Download:** [csv_files.py]({{ site.baseurl }}/resources/lesson-05/csv_files.py)

---

## Explore

1. Extend the statistics script to also print how many students achieved each
   grade.  Use a dictionary to count them.
2. Write a script that reads `student_scores.csv` and writes a new CSV
   containing only the rows where `Score >= 70`.
3. Some CSV files use a semicolon (`;`) as the delimiter instead of a comma.
   How would you tell `csv.reader` to use a different delimiter?  Check the
   [documentation](https://docs.python.org/3/library/csv.html) for the
   `delimiter` parameter.
4. What does the `newline=""` argument do in `open()`?  What goes wrong if you
   leave it out on Windows?
5. The UK government publishes thousands of open datasets in CSV format at
   [data.gov.uk](https://data.gov.uk).  Download a dataset that interests you,
   load it with `csv.DictReader`, and print the column names.

---

[← Lesson 10]({{ site.baseurl }}/lessons/10-dictionaries/)
[Next Lesson: Excel Files →]({{ site.baseurl }}/lessons/12-excel-files/)
