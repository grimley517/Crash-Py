---
layout: page
title: "Lesson 12: Excel Files"
permalink: /lessons/12-excel-files/
---

## Introduction

### What this lesson is about

Excel spreadsheets (`.xlsx` files) are common in schools for recording marks,
registers, and data.  This lesson shows you how to read an Excel file into
Python, process the data, and write the results to a new Excel file using the
`openpyxl` library.

### Why you need this

Being able to automate Excel tasks with Python means you can process large
mark books, generate reports, and transform data far more quickly than by hand.
These skills directly support the pandas lessons where you will do
even more powerful analysis.

> **Standard vs third-party libraries** — So far every `import` statement in
> this course has used a *standard library* module: code that ships with
> Python itself (`math`, `csv`, `json`, …).  `openpyxl` is different: it is a
> *third-party library* written by the open-source community and hosted on
> [PyPI](https://pypi.org) (the Python Package Index).  You install it once
> with `pip` and then import it like any other module.  Thousands of
> third-party libraries exist for tasks ranging from web scraping to machine
> learning; knowing how to find and install them is an essential Python skill.
> Always check a library's PyPI page or documentation before using it in
> production — look for active maintenance and a clear licence.

---

## Do

### Step 1 — Install `openpyxl`

Open Terminal and run:

```bash
pip3 install openpyxl
```

---

### Step 2 — The sample dataset

This lesson uses a freely available dataset of fictional student maths scores.
A sample file is provided for download below.

> **Download sample data:** [student_scores.xlsx]({{ site.baseurl }}/resources/lesson-05/student_scores.xlsx)

The spreadsheet has these columns:

| Column | Description |
|---|---|
| `StudentID` | Unique identifier |
| `Name` | Student name |
| `Topic` | Maths topic (Algebra, Geometry, Statistics, …) |
| `Score` | Score out of 100 |
| `Grade` | Letter grade |

---

### Step 3 — Reading an Excel file

Create `excel_files.py`:

```python
import openpyxl

wb = openpyxl.load_workbook("student_scores.xlsx")
ws = wb.active   # select the first sheet

# Print the header row
header = [cell.value for cell in ws[1]]
print(header)

# Print each data row
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
```

---

### Step 4 — Processing the data

```python
import openpyxl

wb = openpyxl.load_workbook("student_scores.xlsx")
ws = wb.active

scores = []
for row in ws.iter_rows(min_row=2, values_only=True):
    student_id, name, topic, score, grade = row
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Class average: {average:.1f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score:  {min(scores)}")
```

---

### Step 5 — Writing an Excel file

```python
import openpyxl

# Create a new workbook
wb_out = openpyxl.Workbook()
ws_out = wb_out.active
ws_out.title = "Summary"

# Write a header
ws_out.append(["Metric", "Value"])

# Write some data
ws_out.append(["Average Score", 76.4])
ws_out.append(["Highest Score", 98])
ws_out.append(["Lowest Score", 42])

wb_out.save("summary.xlsx")
print("summary.xlsx saved.")
```

---

### Step 6 — Copying and transforming data

Read `student_scores.xlsx`, add a "Pass/Fail" column, and save as a new file:

```python
import openpyxl

wb_in = openpyxl.load_workbook("student_scores.xlsx")
ws_in = wb_in.active

wb_out = openpyxl.Workbook()
ws_out = wb_out.active
ws_out.title = "Results"

# Copy header and add new column
header = [cell.value for cell in ws_in[1]]
header.append("Pass/Fail")
ws_out.append(header)

for row in ws_in.iter_rows(min_row=2, values_only=True):
    student_id, name, topic, score, grade = row
    result = "Pass" if score >= 50 else "Fail"
    ws_out.append([student_id, name, topic, score, grade, result])

wb_out.save("results.xlsx")
print("results.xlsx saved.")
```

---

### Step 7 — Basic formatting

```python
from openpyxl.styles import Font, PatternFill

ws_out["A1"].font = Font(bold=True)
ws_out["A1"].fill = PatternFill(fill_type="solid", fgColor="FFFF00")
```

---

### Step 8 — Converting a CSV file to Excel

Having learned CSV in the previous lesson, you can combine both libraries to
convert a CSV file into an Excel workbook:

```python
import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        ws.append(row)

wb.save("student_scores_from_csv.xlsx")
print("Excel file created.")
```

This pattern is useful whenever you receive data in plain CSV format but need
to share it with colleagues who use Excel.

> **Download:** [excel_files.py]({{ site.baseurl }}/resources/lesson-05/excel_files.py)

---

## Explore

1. Modify the script to count how many students achieved each grade (A*, A, B,
   C, D, U) and write the counts to a new sheet called "Grade Distribution".
2. The UK Department for Education publishes open data on exam results at
   [explore-education-statistics.service.gov.uk](https://explore-education-statistics.service.gov.uk).
   Download a dataset, open it in Python, and compute a summary statistic.
3. How would you sort the rows by score before writing them to the output file?
   Hint: read all rows into a list of tuples and use `sorted()`.
4. What happens if a cell contains `None` (an empty cell)?  Write code to
   handle this safely.
5. `openpyxl` can also create charts inside Excel files.  Search the
   [openpyxl documentation](https://openpyxl.readthedocs.io) to find out how.

---

[← Lesson 11]({{ site.baseurl }}/lessons/11-csv-files/)
[Next Lesson: Markdown →]({{ site.baseurl }}/lessons/13-markdown/)
