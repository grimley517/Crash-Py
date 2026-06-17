---
layout: page
title: "Lesson 14: Markdown"
permalink: /lessons/14-markdown/
---

## Introduction

### What this lesson is about

Markdown is a lightweight markup language — a simple set of conventions for
adding formatting to plain text.  This lesson covers the Markdown syntax,
explains how this very website is built from Markdown files using Jekyll, and
shows you how to write your own Markdown documents.

### Why you need this

Markdown is used everywhere in the Python world: README files, Jupyter
notebooks, GitHub comments, and documentation sites.  Understanding it helps you
write readable documentation for your own code and share lessons or resources
online.

---

## Do

### Step 1 — Basic Markdown syntax

Open VS Code and create a new file called `example.md`.  Type the following:

```markdown
# Heading 1
## Heading 2
### Heading 3

This is a normal paragraph.  Leave a blank line between paragraphs.

**Bold text** and *italic text*.

---

- Item one
- Item two
- Item three

1. First
2. Second
3. Third
```

In VS Code you can preview Markdown by pressing `⌘ Shift V` (Mac) or
`Ctrl Shift V` (Windows).

---

### Step 2 — Links and images

```markdown
[Visit Python.org](https://www.python.org)

![Python logo](https://www.python.org/static/community_logos/python-logo.png)
```

A link is `[text](url)`.  An image is the same but with a `!` at the start.

---

### Step 3 — Code blocks

Use backticks for inline code: `` `print("Hello")` ``

Use triple backticks for a block:

````markdown
```python
def greet(name):
    print(f"Hello, {name}")
```
````

GitHub and Jekyll automatically apply syntax highlighting.

---

### Step 4 — Tables

```markdown
| Name    | Score | Grade |
|---------|-------|-------|
| Alice   | 87    | A     |
| Bob     | 72    | C     |
| Charlie | 95    | A*    |
```

---

### Step 5 — How this site works

This website is built with **Jekyll**, a static site generator that turns
Markdown files into HTML.  GitHub Pages runs Jekyll automatically when you push
to a repository.

The structure of a Jekyll page:

```markdown
---
layout: page
title: My Page Title
---

## Content starts here

Write normal Markdown below the front matter.
```

The block between the `---` lines is called **front matter** — it tells Jekyll
which layout to use and sets the page title.

---

### Step 6 — Run Jekyll locally (optional)

If you want to preview the site before pushing:

```bash
# Install Ruby and Bundler (via Homebrew)
brew install ruby
gem install bundler

# In your project folder
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000` in your browser.

---

### Step 7 — Markdown in Python (bonus)

The `markdown` Python library converts Markdown text to HTML:

```bash
pip3 install markdown
```

```python
import markdown

text = "# Hello\n\nThis is **Markdown**."
html = markdown.markdown(text)
print(html)
```

> **Download:** [markdown_example.md]({{ site.baseurl }}/resources/lesson-14/markdown_example.md)

---

## Explore

1. Write a Markdown file summarising what you have learned in Lessons 1–9.
   Include headings, bullet points, a table, and at least one code block.
2. What is the difference between a `#` heading and a `##` heading in terms of
   the HTML they produce?  Use VS Code's preview to inspect the output.
3. How would you add a *task list* in Markdown?  Research the syntax for
   checkboxes.
4. Jekyll uses *Liquid* templating alongside Markdown.  Look at the source of
   this page on GitHub and find the `{{ site.baseurl }}` expressions — what do
   they do?
5. Create a simple Jekyll site locally with two pages linked together.

---

[← Lesson 13]({{ site.baseurl }}/lessons/13-excel-files/)
[Next Lesson: Git →]({{ site.baseurl }}/lessons/15-git/)
