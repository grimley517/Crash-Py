# Crash-Py — Markdown Example
# This file demonstrates common Markdown syntax used in lessons and on GitHub.

# Heading 1
## Heading 2
### Heading 3
#### Heading 4

Normal paragraph text.  Leave a blank line between paragraphs.

**Bold text** and *italic text* and ***bold italic***.

---

## Lists

Unordered:

- Item one
- Item two
  - Nested item
- Item three

Ordered:

1. First step
2. Second step
3. Third step

Task list:

- [x] Install Python
- [x] Install VS Code
- [ ] Complete all lessons

---

## Links and Images

[Visit Python.org](https://www.python.org)

[Lesson 1](../lessons/01-installation.md)

![Alt text for an image](https://via.placeholder.com/200x100)

---

## Code

Inline code: `print("Hello, World!")`

Fenced code block with syntax highlighting:

```python
def hypotenuse(a, b):
    import math
    return math.sqrt(a**2 + b**2)

print(hypotenuse(3, 4))  # 5.0
```

---

## Tables

| Name    | Score | Grade |
|---------|------:|-------|
| Alice   |    87 | A     |
| Bob     |    72 | C     |
| Charlie |    95 | A*    |

> Columns are right-aligned with `--:`, left-aligned with `:--`, and
> centred with `:-:`.

---

## Blockquotes

> "Pure mathematics is, in its way, the poetry of logical ideas."
> — Albert Einstein

---

## Horizontal rule

---

## Jekyll Front Matter (for GitHub Pages)

Pages on this site begin with YAML front matter between `---` delimiters:

```yaml
---
layout: page
title: My Page Title
permalink: /my-page/
---
```

Everything below the second `---` is normal Markdown.
