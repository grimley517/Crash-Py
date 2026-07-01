# AGENTS

## Markdown Style

- Use progressive heading levels (`###`) for subsection headers in markdown files.
- Do not use standalone bold lines as headers.

## Lesson Pedagogy

The course uses two kinds of lesson.  Match the appropriate format when adding or
editing lessons in `lessons/`.

### Standard lessons

- Follow the *Introduction → Do → Explore* structure.
- `## Introduction` sets out *what* the lesson covers and *why* it matters
  (typically with `### What this lesson is about` and `### Why you need this`).
- `## Do` gives guided, step-by-step practical activities (`### Step 1`, etc.).
- `## Explore` ends the lesson with open-ended questions and experiments.

### Project lessons

- Project lessons **deliberately deviate** from the *Introduction → Do → Explore*
  pattern.  Instead they walk the learner along a single guided route to a
  finished result, then finish with open-ended exploration.
- State this deviation up front in an `## About this project` section.
- Suggested flow: `## About this project` → `## What you will build` →
  `## Before you start` → `## Building it step by step` (with `### Step N`
  headings) → `## Explore`.
- Make the learning objective explicit — name the concept or skill the project is
  really teaching (for example, "implementing an algorithm"), not just the
  artefact produced.
- Title project lessons `Lesson Na: Project — <Name>` and refer to them as
  projects in the lesson tables.

### Shared conventions for all lessons

- Insert new lessons and projects using **letter-suffixed numbers** (for example
  `9a`, `16a`) so the lesson slots in after its prerequisite without renumbering
  existing lessons or breaking permalinks.  Reserve the plain number for the
  established sequence.
- Place a lesson **after every lesson it depends on**.  Project lessons in
  particular must come after all of their prerequisite lessons.
- Reference other lessons by number **and topic**, for example
  "Lesson 6 (*Text Files*)", so the dependency is clear.
- Every lesson ends with previous/next navigation links, and links to the
  neighbouring lessons must be updated when a lesson is inserted or moved.
- Downloadable resources for a lesson live in `resources/lesson-NN/` and are
  linked with `{{ site.baseurl }}/resources/lesson-NN/<file>`.  Resource files
  must **not** contain Jekyll front matter, otherwise Jekyll renders them as site
  pages instead of serving them as downloads — show front-matter templates inline
  in a code block instead.

## Keeping Docs In Sync

When lessons are added, removed, renamed, reordered, or change pedagogy, keep the
following in step (dedicated maintainer agents exist for each):

- The lesson tables in `index.md` and `lessons/index.md`
  (see `.github/agents/course-index-maintainer.agent.md`).
- The lesson table and teaching-approach section in `README.md`
  (see `.github/agents/readme-maintainer.agent.md`).
- The pedagogy conventions in this `AGENTS.md`
  (see `.github/agents/agents-md-maintainer.agent.md`).
