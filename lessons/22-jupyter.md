---
layout: page
title: "Lesson 22: Jupyter Notebooks"
permalink: /lessons/22-jupyter/
---

## Introduction

### What this lesson is about

A *Jupyter notebook* is an interactive document that combines live Python code,
formatted text (Markdown), equations, and output (including plots) in a single
file.  You run code one cell at a time and see the result immediately below it.
This lesson covers installing Jupyter, writing and running notebooks, and
understanding when to use them.

### Why you need this

The next two lessons use `requests` and `pandas` / `matplotlib` — libraries
that produce a lot of output and benefit enormously from interactive
exploration.  In a notebook you can tweak a chart, re-run the cell, and see
the updated plot instantly, without re-running a whole script.  Jupyter is the
de-facto standard environment for data analysis, data science, and teaching in
Python.

---

## Do

### Step 1 — Install Jupyter

Using `uv` in your project:

```bash
uv add jupyter
```

---

### Step 2 — Start the notebook server

```bash
uv run jupyter notebook
```

Your browser opens automatically at `http://localhost:8888`.  If it doesn't,
copy the URL printed in the terminal.

---

### Step 3 — Create your first notebook

1. In the browser, click **New → Python 3 (ipykernel)**.
2. A new tab opens with an empty notebook.
3. Click on the first cell and type:

```python
print("Hello from Jupyter!")
```

4. Press **Shift + Enter** to run the cell.  The output appears directly below.

---

### Step 4 — Cell types

Notebooks have two main cell types:

| Type | Purpose | How to set |
|---|---|---|
| **Code** | Python code to execute | Default |
| **Markdown** | Formatted text, headings, equations | Change dropdown from "Code" to "Markdown" |

Change a cell to Markdown, type `## My Analysis`, and press **Shift + Enter**
to render it as a heading.

---

### Step 5 — Mixing code and explanation

A typical analysis notebook looks like:

```markdown
## Loading the data
```

```python
import pandas as pd
df = pd.read_csv("student_scores.csv")
df.head()
```

```markdown
The dataset has 30 rows and 5 columns.  Next we compute summary statistics.
```

```python
df.describe()
```

This makes your reasoning visible alongside your code — ideal for teaching.

---

### Step 6 — Saving and sharing notebooks

Notebooks are saved as `.ipynb` files (JSON internally).  To save: **Ctrl + S**
(or **Cmd + S** on Mac).

You can share a `.ipynb` file and the recipient can re-run it.  GitHub also
renders `.ipynb` files directly in the browser — useful for sharing analyses
without requiring the reader to run anything.

---

### Step 7 — VS Code notebooks

VS Code has built-in Jupyter notebook support.  Open any `.ipynb` file in VS
Code to get the same interactive experience with the VS Code editor features
(autocomplete, variable explorer, etc.).

Install the **Jupyter** extension from the VS Code Extensions panel, then open
or create a `.ipynb` file.

---

### Step 8 — When to use a notebook vs a script

| Use a notebook | Use a script (`.py`) |
|---|---|
| Exploratory analysis, data visualisation | Production code, CLI tools |
| Teaching demonstrations | Code that will be imported as a module |
| One-off reports | Automated pipelines / scheduled tasks |
| Sharing results with narrative | Code that needs version control carefully |

---

## Explore

1. Create a notebook that loads `student_scores.csv` and displays the first
   10 rows.  Add a Markdown cell above explaining what the dataset contains.
2. Research **Jupyter Lab** — how does it differ from classic Jupyter Notebook?
3. What happens if you run cells out of order?  Try defining a variable in
   cell 3 and using it in cell 1.  What does this tell you about notebook
   state?
4. Export your notebook as a PDF: **File → Download as → PDF**.  What do you
   need installed for this to work?
5. Install the `nbconvert` tool and convert a notebook to HTML from the
   terminal: `uv run jupyter nbconvert --to html my_notebook.ipynb`.

---

[← Lesson 21]({{ site.baseurl }}/lessons/21-try-except/)
[Next Lesson: Requests →]({{ site.baseurl }}/lessons/23-requests/)
