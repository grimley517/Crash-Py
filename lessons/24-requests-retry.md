---
layout: page
title: "Lesson 24: Robust Requests — Retry Mechanics"
permalink: /lessons/24-requests-retry/
---

## Introduction

### What this lesson is about

Network calls can fail for many reasons: the server is temporarily overloaded,
your Wi-Fi drops for a moment, or the API rate-limits your requests.  A
production-quality HTTP client handles these failures gracefully by *retrying*
the request — but only a sensible number of times, and only for errors that
are worth retrying.  This lesson builds a `fetch_with_retry` function using
`try / except`, a *default parameter*, and *recursion*.

### Why you need this

You already know `try / except` from Lesson 21.  Here you will see how to
combine it with a recursive function to build something genuinely useful.
Along the way you will deepen your understanding of: default parameters,
recursive functions, exponential back-off, and which HTTP status codes are
worth retrying.

---

## Do

### Step 1 — The problem: transient failures

A transient failure is one that might succeed if you try again shortly.
Examples:
- `503 Service Unavailable` — the server is temporarily overloaded.
- `429 Too Many Requests` — you are hitting a rate limit; slow down.
- `requests.exceptions.ConnectionError` — temporary network blip.

A *permanent* failure such as `404 Not Found` is never worth retrying — the
resource simply does not exist.

---

### Step 2 — A basic retry loop

Before writing a recursive version, here is the iterative approach for
comparison:

```python
import requests
import time

def fetch_with_retry_loop(url, retries=3, delay=1):
    """Fetch url, retrying up to `retries` times on transient errors."""
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()   # raises HTTPError for 4xx/5xx
            return response
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout) as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                time.sleep(delay)
    raise RuntimeError(f"All {retries} attempts failed for {url}")
```

> **`response.raise_for_status()`** — raises `requests.exceptions.HTTPError`
> if the status code is 4xx or 5xx.  This converts a "silent" bad response
> into a Python exception you can catch.

---

### Step 3 — The recursive version

A *recursive function* is one that calls itself.  Each call is given a
*remaining retries* count; when it reaches zero, the recursion stops.

```python
import requests
import time

def fetch_with_retry(url, retries=3, delay=1):
    """Fetch url, retrying up to `retries` times on transient errors.

    Parameters
    ----------
    url : str
        The URL to fetch.
    retries : int
        Number of attempts remaining.  Counts down on each recursive call.
    delay : int or float
        Seconds to wait before the next attempt.

    Returns
    -------
    requests.Response
        The successful response object.

    Raises
    ------
    RuntimeError
        If all retry attempts are exhausted.
    requests.exceptions.HTTPError
        If the server returns a permanent error (e.g. 404).
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response

    except requests.exceptions.HTTPError as e:
        # Permanent errors: don't retry
        if e.response.status_code in (400, 401, 403, 404):
            raise
        # Transient server errors (5xx): fall through to retry
        print(f"Server error {e.response.status_code}, retrying…")

    except (requests.exceptions.ConnectionError,
            requests.exceptions.Timeout) as e:
        print(f"Network error: {e}, retrying…")

    if retries <= 1:
        raise RuntimeError(f"All retry attempts exhausted for {url}")

    time.sleep(delay)
    return fetch_with_retry(url, retries=retries - 1, delay=delay)
```

---

### Step 4 — How recursion works here

Trace through what happens if the server fails twice then succeeds:

```
fetch_with_retry(url, retries=3)
  → ConnectionError → sleep(1) → fetch_with_retry(url, retries=2)
      → ConnectionError → sleep(1) → fetch_with_retry(url, retries=1)
          → success → return response
      ← return response
  ← return response
```

Each recursive call is a *smaller* version of the same problem — the
`retries` parameter counts down, guaranteeing the recursion terminates.

> **Infinite recursion** — if `retries` never decreased, the function would
> call itself forever and eventually raise `RecursionError`.  Always ensure a
> recursive function has a *base case* (here: `retries <= 1`) that stops it.

---

### Step 5 — Exponential back-off

Doubling the delay on each retry is called *exponential back-off*.  It is
the standard approach used by production HTTP clients and avoids hammering an
already-struggling server:

```python
def fetch_with_retry(url, retries=3, delay=1):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response
    except (requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.HTTPError) as e:
        if retries <= 1:
            raise RuntimeError(f"All retries exhausted for {url}") from e
        print(f"Failed ({e}), waiting {delay}s then retrying…")
        time.sleep(delay)
        return fetch_with_retry(url, retries=retries - 1, delay=delay * 2)
```

With `delay=1` the three attempts wait 0 s, 1 s, 2 s between calls.
With `delay=2` they wait 0 s, 2 s, 4 s — better for protecting a busy server.

---

### Step 6 — Using the function

```python
url = "https://opentdb.com/api.php?amount=5&category=19&type=multiple"

try:
    response = fetch_with_retry(url, retries=3, delay=1)
    data = response.json()
    for q in data["results"]:
        print(q["question"])
except RuntimeError as e:
    print(f"Could not fetch data: {e}")
```

---

## Explore

1. Test the retry function by pointing it at a URL that does not exist
   (`https://httpbin.org/status/503`).  What output do you see?
2. Add a `max_delay` parameter so the back-off never exceeds, say, 30 seconds.
3. What is the difference between `raise` (re-raise) and `raise RuntimeError(…)
   from e`?  What does `from e` do?
4. Research `urllib3.util.retry.Retry` — the retry mechanism built into the
   `requests` library.  How does it compare to the function you wrote?
5. Write a test for `fetch_with_retry` using `pytest` and `unittest.mock` to
   simulate network failures without making real HTTP calls.

---

[← Lesson 23]({{ site.baseurl }}/lessons/23-requests/)
[Next Lesson: Pandas →]({{ site.baseurl }}/lessons/25-pandas/)
