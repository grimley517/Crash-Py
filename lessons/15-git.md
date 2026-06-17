---
layout: page
title: "Lesson 15: Version Control with Git"
permalink: /lessons/15-git/
---

## Introduction

### What this lesson is about

*Git* is the world's most widely used version control system.  It tracks every
change you make to a project over time, lets you experiment safely, and enables
multiple people to collaborate on the same codebase.  This lesson covers
installing Git, configuring it, and the core workflow: initialise a repository,
stage changes, commit them, and review history.

### Why you need this

Even working alone, Git protects you: you can always roll back to a version
that worked.  For the next two lessons you will use Git to publish your lessons
and classroom blog on GitHub Pages — a free hosting service for static sites
that runs on the same Markdown and Jekyll you learned in Lesson 14.

---

## Do

### Step 1 — Install Git

### Mac:

```bash
git --version
```

If Git is not installed, macOS will prompt you to install the Xcode Command
Line Tools.  Follow the prompt.  Alternatively, with Homebrew:

```bash
brew install git
```

### Windows:

```bash
choco install git -y
```

Restart your terminal after installation.

Verify:

```bash
git --version
# git version 2.x.x
```

---

### Step 2 — Configure Git

Tell Git your name and email — these appear in every commit you make:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Set VS Code as the default editor (used when Git opens an editor for commit
messages):

```bash
git config --global core.editor "code --wait"
```

---

### Step 3 — Initialise a repository

Navigate to your project folder and create a Git repository:

```bash
cd ~/projects/crash-py
git init
```

Git creates a hidden `.git` folder that stores all history.  Never delete it.

---

### Step 4 — The three-area model

Git has three areas:

| Area | Description |
|---|---|
| **Working directory** | Files on disk as you edit them |
| **Staging area (index)** | Files you have marked ready to commit with `git add` |
| **Repository** | Permanent snapshots (commits) stored in `.git` |

The cycle is: edit → `git add` → `git commit`.

---

### Step 5 — Your first commit

Create a file, stage it, and commit:

```bash
echo "# Crash-Py classroom blog" > README.md
git add README.md
git commit -m "Initial commit: add README"
```

`-m` provides the commit message inline.  A good message explains *why* the
change was made, not just *what* changed.

---

### Step 6 — Checking status and history

```bash
git status        # what has changed since the last commit?
git log           # full commit history
git log --oneline # compact one-line summary
```

---

### Step 7 — Staging and committing more changes

```bash
# Make a change
echo "Welcome to my classroom blog." >> README.md

# See what changed
git diff README.md

# Stage and commit
git add README.md
git commit -m "Add welcome message to README"
```

---

### Step 8 — The `.gitignore` file

Tell Git to ignore generated files you don't want to track:

```
# .gitignore
__pycache__/
*.pyc
_site/
.jekyll-cache/
```

```bash
git add .gitignore
git commit -m "Add .gitignore"
```

---

## Explore

1. Make three separate commits to your README, then use `git log --oneline`
   to see the history.  What does the hexadecimal code next to each commit
   mean?
2. Use `git show <commit-hash>` to see the exact changes in a previous commit.
3. Research `git diff HEAD~1` — what does `HEAD~1` mean?
4. What is the difference between `git add .` and `git add <filename>`?  When
   might `git add .` be dangerous?
5. Run `git log --oneline --graph` in a repository with multiple branches.
   What does the graph represent?

---

[← Lesson 14]({{ site.baseurl }}/lessons/14-markdown/)
[Next Lesson: GitHub →]({{ site.baseurl }}/lessons/16-github/)
