# Crash-Py

**Python for Maths Teachers** — a practical crash course in Python using
Visual Studio Code and Homebrew on macOS.

The lessons are published as a GitHub Pages website powered by Jekyll.

## Teaching approach

The course mixes two kinds of lesson:

- **Standard lessons** follow an *Introduction → Do → Explore* structure: the
  introduction explains what the topic is and why it matters, *Do* gives guided
  step-by-step activities, and *Explore* ends with open-ended questions.
- **Project lessons** deliberately deviate from that pattern.  Instead they walk
  you along a single guided route to a finished, useful result and then finish
  with open-ended exploration.  Each project makes its learning objective (the
  underlying skill it teaches) explicit and pulls together several earlier
  lessons.  Projects use letter-suffixed numbers (e.g. `9a`, `16a`) and are
  placed after all of the lessons they depend on.

See `AGENTS.md` for the full authoring conventions.

## Lessons

| # | Title |
|---|---|
| 1 | Installation & Hello World |
| 2 | Functions |
| 3 | Mathematical Operations |
| 4 | Docstrings and Code Documentation |
| 5 | Strings |
| 6 | Text Files |
| 7 | Lists |
| 8 | Decisions |
| 9 | For Loops with Range |
| 9a | Project — Sieve of Eratosthenes |
| 10 | Dictionaries |
| 11 | CSV Files |
| 12 | Excel Files |
| 13 | Markdown |
| 14 | Version Control with Git |
| 15 | GitHub — Remote Repositories and Collaboration |
| 16 | GitHub Pages — Publishing Your Classroom Blog |
| 16a | Project — Manual of Me |
| 17 | JSON |
| 18 | Python Packaging with uv |
| 19 | Code Reuse with Modules |
| 20 | Unit Testing |
| 21 | Error Handling — try / except |
| 22 | Jupyter Notebooks |
| 23 | Requests |
| 24 | Robust Requests — Retry Mechanics |
| 25 | Pandas |
| 26 | Pandas Graphs |

## Running locally

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000/Crash-Py` in your browser.
