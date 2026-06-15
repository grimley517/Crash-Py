---
layout: page
title: "Lesson 1: Installation & Hello World"
permalink: /lessons/01-installation/
---

## Introduction

**What this lesson is about**

Before writing any Python code you need the right tools on your computer.
This lesson walks you through installing Python, a code editor (Visual Studio
Code), and a package manager on your machine — **Homebrew** on a Mac or
**Chocolatey** on Windows.  You will then write your first Python program — the
traditional "Hello, World!" — and learn how to run it from a terminal.

**Why you need this**

Every lesson that follows requires Python to be installed and a place to write
code.  Getting comfortable with the terminal is an essential skill: it lets you
run programs, install packages, and automate tasks that would otherwise take many
mouse-clicks.

---

## Do

### Step 1 — Install a package manager

A package manager lets you install and update developer tools from the command
line without manually downloading installers.  Choose the instructions for your
operating system.

#### Mac — Homebrew

[Homebrew](https://brew.sh) is the standard package manager for macOS.

1. Open **Terminal** (search for "Terminal" in Spotlight with `⌘ Space`).
2. Paste the following command and press `Return`:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Follow the on-screen instructions.  You may be asked for your Mac password.
4. Once finished, verify the installation:

```bash
brew --version
```

You should see a version number such as `Homebrew 4.x.x`.

#### Windows — Chocolatey

[Chocolatey](https://chocolatey.org) is a package manager for Windows, similar
to Homebrew on a Mac.  It lets you install and update developer tools from the
command line.

1. Open **PowerShell as Administrator**: search for "PowerShell" in the Start
   menu, right-click it, and choose **Run as administrator**.
2. Paste the following command and press `Enter`:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Follow the on-screen instructions.  Once finished, verify the installation:

```powershell
choco --version
```

You should see a version number such as `Chocolatey v2.x.x`.

---

### Step 2 — Install Python

#### Mac

```bash
brew install python
```

Verify the installation:

```bash
python3 --version
```

You should see `Python 3.x.x`.

#### Windows (Chocolatey)

```powershell
choco install python -y
```

Close and reopen PowerShell, then verify:

```powershell
python --version
```

You should see `Python 3.x.x`.

---

### Step 3 — Install Visual Studio Code

#### Mac

```bash
brew install --cask visual-studio-code
```

Open VS Code from your Applications folder (or type `code .` in Terminal once
the shell integration is set up — VS Code will prompt you to do this the first
time it opens).

#### Windows (Chocolatey)

```powershell
choco install vscode -y
```

Open VS Code from the Start menu.

Install the **Python extension** (Mac and Windows):

1. Click the Extensions icon in the left sidebar (or press `Ctrl Shift X` on
   Windows, `⌘ Shift X` on Mac).
2. Search for **Python** (published by Microsoft).
3. Click **Install**.

---

### Step 4 — Create a project folder

#### Mac

In Terminal:

```bash
mkdir ~/crash-py
cd ~/crash-py
```

#### Windows

In Command Prompt:

```cmd
mkdir %USERPROFILE%\crash-py
cd %USERPROFILE%\crash-py
```

---

### Step 5 — Write Hello World

Open VS Code in your new folder.

**Mac** — in Terminal:

```bash
code .
```

**Windows** — in Command Prompt:

```cmd
code .
```

Create a new file called `hello_world.py` (File → New File, then save as
`hello_world.py`).  Type the following:

```python
print("Hello, World!")
```

Save the file (`⌘ S` on Mac, `Ctrl S` on Windows).

---

### Step 6 — Run the script (Mac)

In Terminal (make sure you are in the `~/crash-py` folder):

```bash
python3 hello_world.py
```

You should see:

```
Hello, World!
```

---

### Step 7 — Run the script (Windows)

> **Note:** If you installed Python using Chocolatey in Step 2 you are already
> set up.  If you prefer a manual install instead, download Python from
> [python.org/downloads](https://www.python.org/downloads/) and tick
> **"Add Python to PATH"** during setup.

1. Open **Command Prompt** (`Windows + R`, type `cmd`, press Enter).
2. Navigate to your project folder:

```cmd
cd %USERPROFILE%\crash-py
```

3. Run the script:

```cmd
python hello_world.py
```

On Windows the command is `python` rather than `python3`.

---

### Step 8 — Extend Hello World

Edit `hello_world.py` to print a few more lines:

```python
print("Hello, World!")
print("I am learning Python.")
print("I am a maths teacher.")
```

Run the script again and watch all three lines appear.

> **Download:** [hello_world.py]({{ site.baseurl }}/resources/lesson-01/hello_world.py)

---

## Explore

1. What happens if you misspell `print` as `Print`?  Try it and read the error
   message carefully — Python's error messages are usually very helpful.
2. Can you print a number instead of text?  Try `print(42)`.
3. What is the difference between `print("Hello")` and `print(Hello)` (without
   quotes)?  Why does one work and the other not?
4. In Terminal, type `python3 --help`.  What information does it give you?
5. The `print` function can take multiple values separated by commas:
   `print("Hello", "World")`.  What does this produce?  How is it different
   from `print("Hello World")`?

---

[← Back to Lessons]({{ site.baseurl }}/lessons/)
[Next Lesson: Functions →]({{ site.baseurl }}/lessons/02-functions/)
