---
layout: page
title: "Lesson 25: Pandas"
permalink: /lessons/25-pandas/
---

## Introduction

### What this lesson is about

`pandas` is Python's premier data analysis library.  Its central object — the
*DataFrame* — is like a spreadsheet inside Python: rows and columns of data
that you can filter, sort, group, and summarise with concise commands.  This
lesson covers loading data from a CSV file, computing descriptive statistics,
and answering real questions about a dataset.

### Why you need this

Pandas lets you analyse datasets that would be tedious or error-prone to process
manually in Excel.  It forms the backbone of data science in Python and combines
naturally with matplotlib (the next lesson) for visualisation.

---

## Do

### Step 1 — Install pandas

**What:** Install `pandas` (and `openpyxl` for Excel support) using `uv`,
the fast package manager introduced in the previous lesson.

**Why:** `pandas` is a third-party library not bundled with Python.
Installing it once with `uv` adds it to your project's virtual environment.

```bash
uv add pandas openpyxl
```

---

### Step 2 — The dataset

**What:** Load the same student scores CSV you created in the CSV lesson.

**Why:** Using familiar data lets you focus on learning the pandas API rather
than understanding a new dataset.

> **Download:** [student_scores.csv]({{ site.baseurl }}/resources/lesson-05/student_scores.csv)

---

### Step 3 — Loading a CSV into a DataFrame

**What:** Read the CSV into a pandas *DataFrame* — a labelled, two-dimensional
table.

**Why:** Once data is in a DataFrame you can query, filter, and summarise it
with a few lines rather than writing loops by hand.

```python
import pandas as pd

df = pd.read_csv("student_scores.csv")
print(df.head())         # first 5 rows
print(df.shape)          # (rows, columns)
print(df.columns)        # column names
print(df.dtypes)         # data types of each column
```

`df.head()` is the first thing to run after loading any new dataset — it
confirms the data loaded correctly and lets you see the column names.

---

### Step 4 — Descriptive statistics

**What:** Ask pandas to summarise the distribution of scores numerically.

**Why:** A single call to `df.describe()` replaces dozens of manual
calculations.  The spread between `min`, `25%`, `75%`, and `max` tells you
whether marks are bunched or spread out.

```python
print(df.describe())     # count, mean, std, min, 25%, 50%, 75%, max

print(df["Score"].mean())
print(df["Score"].median())
print(df["Score"].std())
print(df["Score"].min())
print(df["Score"].max())
```

Notice whether the mean and median are close — a large gap suggests the
distribution is *skewed* by a few very high or very low scores.

---

### Step 5 — Accessing columns and rows

**What:** Select specific columns and filter rows by a condition.

**Why:** Real datasets have many columns.  Selecting only what you need keeps
output readable; filtering lets you focus on a sub-group (e.g. only the
students who need support).

```python
# A single column (returns a Series)
scores = df["Score"]

# Multiple columns (returns a DataFrame)
subset = df[["Name", "Score"]]

# Filter rows where score >= 80
high_scorers = df[df["Score"] >= 80]
print(high_scorers)
```

---

### Step 6 — Grouping data

**What:** Split the DataFrame by category, then apply a summary function to
each group.

**Why:** "Which topic do students find hardest?" is answered in one line with
`groupby`.  Doing this by hand with loops would take much longer and be harder
to read.

```python
# Average score per topic
topic_avg = df.groupby("Topic")["Score"].mean()
print(topic_avg)

# Count of each grade
grade_counts = df["Grade"].value_counts()
print(grade_counts)
```

---

### Step 7 — Sorting

**What:** Reorder rows by the value of a column.

**Why:** Seeing the top and bottom performers at a glance is useful when
writing feedback or deciding on intervention groups.

```python
# Sort by score descending
sorted_df = df.sort_values("Score", ascending=False)
print(sorted_df.head(10))
```

---

### Step 8 — Adding a new column

**What:** Apply a function to every value in a column and store the results
as a new column.

**Why:** Derived columns — pass/fail, letter grade, z-score — are computed
once and attached to the DataFrame so subsequent analyses can use them.

```python
def assign_pass_fail(score):
    return "Pass" if score >= 50 else "Fail"

df["Result"] = df["Score"].apply(assign_pass_fail)
print(df[["Name", "Score", "Result"]].head())
```

---

### Step 9 — Saving results to a new CSV

**What:** Write the augmented DataFrame back to a CSV file.

**Why:** You can share the processed file with colleagues or load it again
later without re-running the analysis.

```python
df.to_csv("student_scores_with_results.csv", index=False)
print("Saved.")
```

---

### Step 10 — Reading from Excel

**What:** Use `pandas` to load an `.xlsx` file directly.

**Why:** `pd.read_excel()` is much more concise than opening a workbook with
`openpyxl` row-by-row; use it whenever you only need to analyse the data
rather than manipulate the workbook structure.

```python
df_excel = pd.read_excel("student_scores.xlsx")
print(df_excel.head())
```

> **Download:** [pandas_stats.py]({{ site.baseurl }}/resources/lesson-25/pandas_stats.py)

---

## Explore

1. Find the student with the highest score in each topic.  Hint: use
   `groupby` and `idxmax()`.
2. How many students scored below the class average?  Write one line of pandas
   code to answer this.
3. Use `df.pivot_table()` to create a table showing the average score for each
   grade within each topic.
4. The UK Department for Education publishes GCSE results data at
   [explore-education-statistics.service.gov.uk](https://explore-education-statistics.service.gov.uk).
   Download a CSV, load it with pandas, and compute the national average for
   maths.
5. What is the difference between `df.mean()` and `df["Score"].mean()`?

---

[← Lesson 24]({{ site.baseurl }}/lessons/24-requests-retry/)
[Next Lesson: Pandas Graphs →]({{ site.baseurl }}/lessons/26-pandas-graphs/)
