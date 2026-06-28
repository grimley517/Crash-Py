---
layout: page
title: "Lesson 16: GitHub Pages — Publishing Your Classroom Blog"
permalink: /lessons/16-github-pages/
---

## Introduction

### What this lesson is about

*GitHub Pages* is a free static site hosting service built into GitHub.  Any
public repository can serve a website built from Markdown files and a Jekyll
theme — no server, no cost, no configuration beyond a single settings toggle.
This lesson guides you through creating a classroom blog: a simple Jekyll site
where you (or your students) can publish posts about what they are learning.

### Why you need this

A classroom blog is a genuine project you can use immediately.  It practises
the Markdown you learned in Lesson 13, the Git and GitHub skills from Lessons
14–15, and gives you a permanent, public URL to share with students and parents.

---

## Do

### Step 1 — Enable GitHub Pages for your repository

1. Open your `classroom-blog` repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Select branch `main` and folder `/ (root)`.
5. Click **Save**.

GitHub will show a message: *"Your site is ready to be published at
`https://yourusername.github.io/classroom-blog/`"*.  It takes 1–2 minutes to
go live.

---

### Step 2 — Add a Jekyll config file

In your local repo, create `_config.yml`:

```yaml
title: My Classroom Blog
description: Reflections on teaching maths with Python
theme: minima
baseurl: /classroom-blog
url: https://yourusername.github.io
```

Commit and push:

```bash
git add _config.yml
git commit -m "Add Jekyll config"
git push
```

---

### Step 3 — Your home page

Create `index.md`:

```markdown
---
layout: home
---

Welcome to the classroom blog!  Here you will find weekly write-ups of what
we have been learning in our Python for Maths lessons.
```

---

### Step 4 — Write your first blog post

Jekyll looks for posts in a `_posts/` folder.  Post filenames must follow the
format `YYYY-MM-DD-title.md`:

```bash
mkdir _posts
```

Create `_posts/2026-01-15-hello-world.md`:

```markdown
---
layout: post
title: "Hello World — Week 1"
date: 2026-01-15
---

This week we installed Python and ran our first script.  The most important
thing we learned is that computers do exactly what you tell them — not what
you mean!

```python
print("Hello, class!")
```

Next week: functions and Pythagoras.
```

---

### Step 5 — Preview locally with Jekyll

If you have Ruby and Bundler installed, you can preview the site locally:

Create `Gemfile`:

```ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
```

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000/classroom-blog/` in your browser.  The site rebuilds
automatically when you save a file.

---

### Step 6 — Publish and iterate

```bash
git add _posts/
git commit -m "Add first blog post"
git push
```

Wait 1–2 minutes, then reload `https://yourusername.github.io/classroom-blog/`
to see your post live.

---

### Step 7 — Add an About page

Create `about.md`:

```markdown
---
layout: page
title: About
permalink: /about/
---

This blog documents our Python for Maths lessons.  Posts are written by the
class teacher and students at [Your School Name].
```

```bash
git add about.md
git commit -m "Add About page"
git push
```

---

## Explore

1. Add a second post documenting what you learned in a later lesson.  Use a
   code block, a list, and a heading.
2. Change the `theme:` in `_config.yml` to `jekyll-theme-cayman` (or any
   other GitHub Pages supported theme).  Push and see the result.
3. What is the difference between a Jekyll `post` and a Jekyll `page`?  When
   would you use each?
4. Research how to add a custom domain name to a GitHub Pages site.  What DNS
   records would you need to set?
5. Students could write posts themselves using the GitHub web editor (no local
   Git needed).  How could you use pull requests to let students submit their
   posts for your review before they go live?

---

[← Lesson 15]({{ site.baseurl }}/lessons/15-github/)
[Next Lesson: JSON →]({{ site.baseurl }}/lessons/17-json/)
