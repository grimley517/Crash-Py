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
  lessons.  Projects use letter-suffixed numbers (e.g. `10a`, `17a`) and are
  placed after all of the lessons they depend on.

See `AGENTS.md` for the full authoring conventions.

## Lessons

| # | Title |
|---|---|
| 1 | Installation & Hello World |
| 2 | Functions |
| 3 | Mathematical Operations |
| 4 | Docstrings and Code Documentation |
| 6 | Strings |
| 7 | Text Files |
| 8 | Lists |
| 9 | Decisions |
| 10 | For Loops with Range |
| 10a | Project — Sieve of Eratosthenes |
| 11 | Dictionaries |
| 12 | CSV Files |
| 13 | Excel Files |
| 14 | Markdown |
| 15 | Version Control with Git |
| 16 | GitHub — Remote Repositories and Collaboration |
| 17 | GitHub Pages — Publishing Your Classroom Blog |
| 17a | Project — Manual of Me |
| 18 | JSON |
| 19 | Python Packaging with uv |
| 20 | Code Reuse with Modules |
| 21 | Unit Testing |
| 22 | Error Handling — try / except |
| 23 | Jupyter Notebooks |
| 24 | Requests |
| 25 | Robust Requests — Retry Mechanics |
| 26 | Pandas |
| 27 | Pandas Graphs |

## Running locally

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000/Crash-Py` in your browser.
