---
layout: page
title: "Lesson 16a: Project — Manual of Me"
permalink: /lessons/16a-manual-of-me/
---

## About this project

This is a **project lesson**.  Unlike the numbered lessons, it does not follow
the *Introduction → Do → Explore* pattern.  Instead it walks you along a single
guided route to a finished result, then leaves you with ideas to explore once it
is published.

The goal: write a **"Manual of Me"** — a short, friendly guide that tells new
colleagues how to work well with you — and publish it as a website using
**Markdown** (Lesson 13) and **GitHub Pages** (Lesson 16).

A Manual of Me (sometimes called a *user guide to me* or *README for a person*)
is a genuinely useful document.  A new teaching assistant, a trainee, or a
colleague joining your department can read it and immediately understand how you
prefer to communicate, when you are available, and what matters to you.  It is
also the perfect low-stakes way to practise everything you learned about
Markdown and GitHub Pages.

---

## What you will build

A small GitHub Pages site containing:

1. A home page introducing who you are and what the guide is for.
2. A structured "Manual of Me" written in Markdown, covering how you work, how
   you communicate, and how colleagues can get the best from working with you.
3. A live, shareable URL like
   `https://yourusername.github.io/manual-of-me/`.

---

## Before you start

You should already have completed:

- Lesson 13 — Markdown (headings, lists, tables, links).
- Lesson 14 — Git (init, add, commit).
- Lesson 15 — GitHub (creating a repository, pushing).
- Lesson 16 — GitHub Pages (enabling Pages, `_config.yml`, front matter).

If you can already publish the classroom blog from Lesson 16, you have
everything you need for this project.

---

## Building it step by step

### Step 1 — Create the repository

On GitHub, create a new **public** repository called `manual-of-me`.  Tick
*"Add a README file"* so the repository is not empty, then clone it to your
computer:

```bash
git clone https://github.com/yourusername/manual-of-me.git
cd manual-of-me
code .
```

Replace `yourusername` with your own GitHub username.

---

### Step 2 — Add the Jekyll config

GitHub Pages uses Jekyll to turn your Markdown into a website.  Create a file
called `_config.yml`:

```yaml
title: Manual of Me
description: How to work well with me
theme: minima
baseurl: /manual-of-me
url: https://yourusername.github.io
```

The `baseurl` must match your repository name, and `url` uses your GitHub
username — exactly as you did for the classroom blog in Lesson 16.

---

### Step 3 — Write the home page

Create `index.md`.  The front matter (the block between the `---` lines) tells
Jekyll to use the site's home layout.

```markdown
---
layout: home
title: Manual of Me
---

Welcome!  This short guide explains how I like to work so that we can
collaborate well from day one.  Read the [full manual](manual) whenever you
have five minutes.
```

The `[full manual](manual)` link points to the page you will create in the next
step.

---

### Step 4 — Write the manual

This is the heart of the project.  Create a file called `manual.md` and use
everything you learned about Markdown in Lesson 13 — headings, lists, and a
table — to structure a clear, honest guide.

Use the template below as a starting point, then replace the example text with
your own answers.  The `###` sub-headings keep the page tidy and easy to scan.

```markdown
---
layout: page
title: The Manual
permalink: /manual/
---

## How to work with me

### My role

I teach maths and I am learning to use Python to build classroom tools.  This
guide is for anyone working alongside me — trainees, teaching assistants, and
colleagues.

### How I communicate

- I prefer a quick chat in person for anything urgent.
- For non-urgent things, email is best — I check it twice a day.
- I am at my most focused first thing in the morning.

### When I am available

| Day       | Best times to reach me |
|-----------|------------------------|
| Monday    | Before 9am, after 3pm  |
| Wednesday | Lunchtime              |
| Friday    | Any time               |

### What helps me do my best work

- Clear, specific requests with a deadline.
- A heads-up before a meeting so I can prepare.
- Honest feedback — I would rather know early.

### Things that are good to know

- I get straight to the point; it is never meant to be abrupt.
- If I go quiet, I am concentrating, not ignoring you.
```

Save the file and preview it in VS Code with `Ctrl Shift V` (or `⌘ Shift V` on a
Mac) to check that the headings and table look right.

---

### Step 5 — Commit and push

Save your files, then commit and push them to GitHub:

```bash
git add _config.yml index.md manual.md
git commit -m "Add Manual of Me site"
git push
```

---

### Step 6 — Turn on GitHub Pages

Just like the classroom blog in Lesson 16:

1. On GitHub, open your `manual-of-me` repository.
2. Go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Select branch `main` and folder `/ (root)`, then click **Save**.

Wait 1–2 minutes, then visit `https://yourusername.github.io/manual-of-me/`.
Your home page should appear, with a working link through to the manual.

---

### Step 7 — Preview locally (optional)

If you installed Ruby and Bundler back in Lesson 16, you can preview the site
before pushing.  Create a `Gemfile`:

```ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
```

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000/manual-of-me/` to see your site.  It rebuilds each
time you save a file.

---

## Explore

Your manual is live — now make it your own.  These ideas are open-ended.

1. Add an **About** page (`about.md`) with a short paragraph about why you became
   a teacher.  Link to it from the home page.
2. Add a section on how you like to *receive* feedback versus how you like to
   *give* it.  What is the difference?
3. Ask a colleague to read your manual and tell you one thing that surprised
   them.  Update the manual based on what they say.
4. Change the `theme:` in `_config.yml` to another GitHub Pages theme such as
   `jekyll-theme-cayman`.  Push and compare the look.  You can browse the full
   list of built-in themes at
   [pages.github.com/themes](https://pages.github.com/themes/), and the complete
   set of supported themes is documented at
   [GitHub Docs — Supported themes](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#supported-themes).
5. Share the link with a colleague and invite them to write their own Manual of
   Me.  How could a whole department benefit from having one each?
6. Could students write a "Manual of Me" too, to help you understand how they
   learn best?  Sketch out what sections theirs might include.

---

[← Lesson 16: GitHub Pages]({{ site.baseurl }}/lessons/16-github-pages/)
[Next Lesson: JSON →]({{ site.baseurl }}/lessons/17-json/)
