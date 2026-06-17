---
layout: page
title: "Lesson 24: Requests"
permalink: /lessons/24-requests/
---

## Introduction

### What this lesson is about

The `requests` library makes it straightforward to call web APIs — services
that respond to HTTP requests with data, usually in JSON format.  This lesson
shows you how to make a GET request, inspect the response, and work with the
JSON data returned.

### Why you need this

Web APIs are how programs communicate with the wider internet: weather services,
government data portals, maths databases.  Being able to retrieve and use live
data programmatically opens up a huge range of possibilities for data-driven
lessons and projects.

---

## Do

### Step 1 — Install the `requests` library

```bash
pip3 install requests
```

---

### Step 2 — Your first GET request

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)   # 200 means success
print(response.text)          # raw JSON text
```

[JSONPlaceholder](https://jsonplaceholder.typicode.com) is a free, public
practice API that returns fictional data — no account or API key needed.

---

### Step 3 — Parsing the JSON response

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()   # automatically parses JSON into a Python dict/list

print(data)
print(data["title"])
print(data["completed"])
```

---

### Step 4 — Fetching a list of items

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()   # returns a list of 200 items

print(f"Fetched {len(todos)} to-do items")

# Count how many are completed
completed = [t for t in todos if t["completed"]]
print(f"Completed: {len(completed)}")
print(f"Remaining: {len(todos) - len(completed)}")
```

---

### Step 5 — Handling errors

```python
import requests

url = "https://jsonplaceholder.typicode.com/todos/99999"  # does not exist
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
elif response.status_code == 404:
    print("Resource not found.")
else:
    print(f"Unexpected status: {response.status_code}")
```

---

### Step 6 — Passing query parameters

```python
import requests

# Get posts by a specific user
params = {"userId": 1}
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)
posts = response.json()

print(f"User 1 has {len(posts)} posts")
for post in posts[:3]:
    print(" -", post["title"])
```

---

### Step 7 — A maths trivia API

The [Open Trivia Database](https://opentdb.com) provides free trivia questions,
including maths questions:

```python
import requests

url = "https://opentdb.com/api.php"
params = {
    "amount": 5,
    "category": 19,   # Mathematics
    "type": "multiple"
}

response = requests.get(url, params=params)
data = response.json()

for q in data["results"]:
    print(q["question"])
    print("Answer:", q["correct_answer"])
    print()
```

> **Download:** [requests_example.py]({{ site.baseurl }}/resources/lesson-24/requests_example.py)

---

## Explore

1. The JSONPlaceholder API also has a `/users` endpoint.  Fetch the list of
   users and print each one's name and email address.
2. What HTTP status code means "not found"?  What does "200 OK" mean?  Research
   the most common HTTP status codes.
3. Use the Open Trivia Database to fetch 10 maths questions and quiz yourself:
   print the question, wait for user input (`input()`), then reveal the answer.
4. The `requests` library can also make POST requests.  Research `requests.post()`
   and find out when you would use it instead of `requests.get()`.
5. What happens if you make a request to an address that does not exist (e.g.
   a made-up domain)?  Handle the `requests.exceptions.ConnectionError` exception.

---

[← Lesson 23]({{ site.baseurl }}/lessons/23-jupyter/)
[Next Lesson: Robust Requests — Retry Mechanics →]({{ site.baseurl }}/lessons/25-requests-retry/)
