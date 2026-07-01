---
layout: page
title: "Lesson 15: GitHub — Remote Repositories and Collaboration"
permalink: /lessons/15-github/
---

## Introduction

### What this lesson is about

*GitHub* is a cloud hosting service for Git repositories.  It adds a web
interface, pull requests, issues, and (crucially) free hosting for static
sites via *GitHub Pages*.  This lesson covers creating a GitHub account,
connecting your local Git repository to a remote, and pushing and pulling
changes.

### Why you need this

A local Git repository is great, but storing your code on GitHub means it is
backed up, shareable, and ready to publish as a website.  In the next lesson
you will use GitHub Pages to turn your Markdown files into a live classroom
blog with zero configuration.

---

## Do

### Step 1 — Create a GitHub account

Go to [github.com](https://github.com) and sign up for a free account.  Choose
a username you are happy to share — it will appear in your site's URL.

---

### Step 2 — Create a new repository on GitHub

1. Click the **+** icon → **New repository**.
2. Name it `classroom-blog`.
3. Leave it **Public** (required for free GitHub Pages hosting).
4. Do **not** tick "Add a README" — you already have one locally.
5. Click **Create repository**.

GitHub shows you setup instructions.  Copy the HTTPS URL, e.g.
`https://github.com/yourusername/classroom-blog.git`.

---

### Step 3 — Connect your local repo to GitHub

In your project folder:

```bash
git remote add origin https://github.com/yourusername/classroom-blog.git
git branch -M main
git push -u origin main
```

- `remote add origin` names the GitHub URL "origin" (the conventional name).
- `-M main` renames your branch to `main` (GitHub's default).
- `-u origin main` sets the default so future `git push` commands need no arguments.

---

### Step 4 — The push/pull workflow

After each set of changes:

```bash
git add .
git commit -m "Describe what you changed"
git push
```

To download changes made elsewhere (e.g. by a collaborator, or edits via the
GitHub web interface):

```bash
git pull
```

---

### Step 5 — Viewing your repository on GitHub

After pushing, refresh the GitHub page.  You will see:
- Your files listed with the last commit message next to each.
- The `README.md` rendered as a formatted page.
- The **Commits** tab showing your full history.

---

### Step 6 — Editing files on GitHub

You can edit any file directly in the browser:
1. Click the file name.
2. Click the pencil icon (Edit).
3. Make your change, scroll down, and click **Commit changes**.

Then pull the change locally with `git pull`.

---

### Step 7 — SSH keys (optional but recommended)

Every push using HTTPS asks for your password.  An *SSH key pair* authenticates
you automatically:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

Copy the public key (`~/.ssh/id_ed25519.pub`) to GitHub: **Settings → SSH and
GPG keys → New SSH key**.  Then change your remote URL:

```bash
git remote set-url origin git@github.com:yourusername/classroom-blog.git
```

---

## Explore

1. Make a change on GitHub using the browser editor, then `git pull` locally.
   Use `git log --oneline` to confirm the change appears.
2. What is the difference between `git fetch` and `git pull`?
3. Create a second repository called `test-repo`, clone it locally with
   `git clone <url>`, make a change, and push it back.
4. What is a *branch*?  Use `git checkout -b my-feature` to create one,
   make a commit, and then merge it back with `git merge`.
5. Research what a *pull request* is and why teams use them instead of
   pushing directly to `main`.

---

[← Lesson 14]({{ site.baseurl }}/lessons/14-git/)
[Next Lesson: GitHub Pages — Publishing Your Classroom Blog →]({{ site.baseurl }}/lessons/16-github-pages/)
