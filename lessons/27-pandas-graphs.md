---
layout: page
title: "Lesson 27: Pandas Graphs"
permalink: /lessons/27-pandas-graphs/
---

## Introduction

### What this lesson is about

Numbers alone rarely tell a complete story.  This lesson combines `pandas` with
`matplotlib` — Python's most widely used plotting library — to produce bar
charts, histograms, scatter plots, and box plots from data held in a DataFrame.

### Why you need this

Visualisation is a core skill for a maths teacher: spotting trends in class
results, comparing groups, presenting data to students or parents.  Python
graphs are reproducible — run the same script on new data and the charts update
automatically.

---

## Do

### Step 1 — Install matplotlib

```bash
pip3 install matplotlib
```

---

### Step 2 — The dataset

This lesson uses the student scores dataset.

> **Download:** [student_scores.csv]({{ site.baseurl }}/resources/lesson-12/student_scores.csv)

---

### Step 3 — A basic bar chart: average score by topic

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_scores.csv")

topic_avg = df.groupby("Topic")["Score"].mean()

topic_avg.plot(kind="bar", color="steelblue", edgecolor="black")
plt.title("Average Score by Topic")
plt.xlabel("Topic")
plt.ylabel("Average Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("avg_by_topic.png", dpi=150)
plt.show()
```

`plt.tight_layout()` prevents labels being cut off.
`plt.savefig()` saves the chart to a PNG file.

---

### Step 4 — Histogram: score distribution

```python
df["Score"].plot(
    kind="hist",
    bins=10,
    edgecolor="black",
    color="coral"
)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("score_distribution.png", dpi=150)
plt.show()
```

---

### Step 5 — Scatter plot: student ID vs score

```python
plt.figure(figsize=(8, 5))
plt.scatter(df["StudentID"], df["Score"], alpha=0.6, color="green")
plt.axhline(y=df["Score"].mean(), color="red", linestyle="--",
            label=f"Mean: {df['Score'].mean():.1f}")
plt.title("Score by Student ID")
plt.xlabel("Student ID")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("scatter.png", dpi=150)
plt.show()
```

`plt.axhline()` draws a horizontal reference line.

---

### Step 6 — Box plot: score spread per topic

```python
df.boxplot(column="Score", by="Topic", figsize=(10, 6))
plt.title("Score Spread by Topic")
plt.suptitle("")   # suppress the default title added by boxplot
plt.xlabel("Topic")
plt.ylabel("Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("boxplot.png", dpi=150)
plt.show()
```

---

### Step 7 — Pie chart: grade distribution

```python
grade_counts = df["Grade"].value_counts()

grade_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colors=["gold", "lightblue", "lightgreen", "salmon", "violet", "grey"]
)
plt.title("Grade Distribution")
plt.ylabel("")   # hide the default 'Grade' label
plt.tight_layout()
plt.savefig("grades_pie.png", dpi=150)
plt.show()
```

---

### Step 8 — Customising plots

```python
plt.style.use("ggplot")   # change the overall style
```

Other available styles: `"seaborn-v0_8"`, `"bmh"`, `"dark_background"`.
List all styles with `print(plt.style.available)`.

---

### Step 9 — Multiple subplots

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

df["Score"].plot(kind="hist", bins=10, ax=axes[0], color="steelblue",
                 edgecolor="black", title="Score Distribution")
df.groupby("Topic")["Score"].mean().plot(kind="bar", ax=axes[1],
    color="coral", edgecolor="black", title="Average by Topic")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("combined.png", dpi=150)
plt.show()
```

> **Download:** [pandas_graphs.py]({{ site.baseurl }}/resources/lesson-27/pandas_graphs.py)

---

## Explore

1. Modify the bar chart to show the *standard deviation* rather than the mean
   for each topic.  What does a high standard deviation tell you about that
   topic's results?
2. Add error bars to the bar chart using the standard deviation.  Research the
   `yerr` parameter of `.plot(kind="bar")`.
3. Create a line chart showing how average scores change as student IDs
   increase.  What might a downward trend suggest?
4. The matplotlib documentation at [matplotlib.org](https://matplotlib.org) has
   a gallery of example plots.  Reproduce one that interests you using the
   student scores data.
5. Save all your charts to a single PDF file.  Research `matplotlib.backends.backend_pdf.PdfPages`.

---

[← Lesson 26]({{ site.baseurl }}/lessons/26-pandas/)
[Back to All Lessons]({{ site.baseurl }}/lessons/)
