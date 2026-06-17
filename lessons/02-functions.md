---
layout: page
title: "Lesson 2: Functions"
permalink: /lessons/02-functions/
---

## Introduction

### What this lesson is about

Before we can write useful programs we need two building blocks: *variables*
(named storage for values) and *functions* (named, reusable blocks of code).
This lesson introduces both.  It covers how to assign values to variables,
Python's four core data types, the `def` keyword, how to pass information into
a function using *arguments*, how to get information back out using a *return
value*, and the `pass` keyword that acts as a placeholder.

### Why you need this

Variables let you label and reuse values; functions let you name and reuse
instructions.  Together they are the foundation of every Python program you will
ever write, and every subsequent lesson builds on them.

---

## Do

### Step 1 — Variables and data types

A [**variable**](https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords) is a named label that stores a value.  You create a variable and give it a value using the *assignment operator* `=`:

```python
name = "Alice"        
age = 16              
height = 1.72         
is_enrolled = True    
```

NB: Running this will produce no output. This is an example only

The above code shows 4 variables being set. The name is on the left; the value is on the right.  After this line executes, Python remembers the value whenever you use that name.

#### References:

These links contain a lot of data, just know these are here to refer to later.

- [boolean data](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)
    - A boolean data has 2 values , `True` or `False`
- [string data](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
    - String data is any sequence of characters, think any text.  
    - Be aware that numbers are often text.
        - An example if this is a phone number, this is useful as it maintains the leading 0, and we don't usually have any need to perform any operations on phone numbers
- [numeric](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)


### Variable Naming Rules

- Names may contain letters, digits, and underscores, but must **not** start with a digit.
- Names are case-sensitive: `score` and `Score` are two different variables.
- By convention, use lowercase words separated by underscores:
    - `student_score`
    - `class_average`
- *System variables*: that you may see later have double underscores. You can use these in your scripts, but avoid creating them as your own variables.
    - eg `__name__`

### Core data types

Python automatically detects the type of a variable from the value you assign.
The four types you will use most often are:

| Type | Example values | Notes |
|---|---|---|
| `int` | `42`, `-7`, `0` | Whole number, no decimal point |
| `float` | `3.14`, `-0.5`, `1.0` | Number with a decimal point |
| `str` | `"Alice"`, `'hello'` | Text, enclosed in quotes |
| `bool` | `True`, `False` | Logical true/false value (capital first letter) |

```python
name = "Alice"        # str
age = 16              # int
height = 1.72         # float
is_enrolled = True    # bool

print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(height))       # <class 'float'>
print(type(is_enrolled))  # <class 'bool'>
```

You can reassign a variable at any time — the new value replaces the old one:

```python
score = 85
print(score)   # 85
score = 90
print(score)   # 90
```

---

### Step 2 — Defining a simple function

Create a new file called `functions.py` in your `~/crash-py` folder.

```python
def greet():
    print("Hello from inside a function!")
```

This defines a function called `greet` but does **not** run it yet.  To run it,
you must *call* it:

```python
def greet():
    print("Hello from inside a function!")

greet()
```

Run the script:

```bash
python3 functions.py
```

---

### Step 3 — Arguments

Arguments let you pass values *into* a function so it can use them.

```python
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")
```

You can define multiple arguments separated by commas:

```python
def add(a, b):
    print(a + b)

add(3, 5)   # prints 8
add(10, 2)  # prints 12
```

---

### Step 4 — Return values

Instead of printing inside the function you can *return* a value so the caller
can use it.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print("The answer is", result)
```

The `return` statement sends a value back to whatever called the function.
Execution of the function stops at `return`.

```python
def is_even(n):
    return n % 2 == 0   # returns True or False

print(is_even(4))   # True
print(is_even(7))   # False
```

---

### Step 5 — The `pass` keyword

Sometimes you want to define a function as a *placeholder* — you know you will
need it, but you have not written the body yet.  Python requires at least one
statement inside a function body, so you use `pass`:

```python
def calculate_area():
    pass   # TODO: write this later

def calculate_perimeter():
    pass
```

`pass` does nothing; it is simply a valid, empty statement that satisfies
Python's syntax rules.

---

### Step 6 — Named (keyword) arguments

You can call a function using argument *names* instead of relying on position.
This makes code much more readable:

```python
def describe_triangle(base, height):
    area = 0.5 * base * height
    print("Base:", base, "Height:", height, "Area:", area)

# positional — order matters
describe_triangle(6, 4)

# keyword — order does not matter
describe_triangle(height=4, base=6)
```

---

### Step 7 — Putting it together

```python
def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

w = 5
h = 3
print("Area:", rectangle_area(w, h))
print("Perimeter:", rectangle_perimeter(w, h))
```

> **Download:** [functions.py]({{ site.baseurl }}/resources/lesson-02/functions.py)

---

## Explore

1. Write a function called `square` that takes a number and returns its square.
   Test it with `print(square(7))` — you should get `49`.
2. What happens if you call a function *before* it is defined in the file?
   Try it and read the error.
3. Write a function with a *default* argument value, for example
   `def greet(name="World"):`.  What happens when you call `greet()` with no
   argument?
4. Can a function call another function?  Write `double(x)` that returns
   `2 * x`, and then a function `quadruple(x)` that calls `double` twice.
5. What does a function return if it has no `return` statement?  Try
   `result = greet("Alice")` then `print(result)`.

---

[← Lesson 1]({{ site.baseurl }}/lessons/01-installation/)
[Next Lesson: Mathematics →]({{ site.baseurl }}/lessons/03-mathematics/)
