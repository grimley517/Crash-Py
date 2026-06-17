# Lesson 13 - Requests
# Run this script with:  python3 requests_example.py
#
# Install the library first:
#   pip3 install requests

import requests


def fetch_single_todo():
    """Fetch one item from JSONPlaceholder."""
    print("=== Single Todo ===")
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Status:", response.status_code)
    data = response.json()
    print(data)
    print("Title:", data["title"])
    print("Completed:", data["completed"])


def fetch_todo_summary():
    """Fetch all 200 todos and summarise them."""
    print("\n=== Todo Summary ===")
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = response.json()
    completed = [t for t in todos if t["completed"]]
    print(f"Total:     {len(todos)}")
    print(f"Completed: {len(completed)}")
    print(f"Remaining: {len(todos) - len(completed)}")


def fetch_posts_by_user(user_id=1):
    """Fetch posts by a specific user using query parameters."""
    print(f"\n=== Posts by User {user_id} ===")
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": user_id}
    )
    posts = response.json()
    print(f"User {user_id} has {len(posts)} post(s)")
    for post in posts[:3]:
        print(f"  - {post['title'][:60]}")


def fetch_maths_trivia():
    """Fetch maths trivia questions from the Open Trivia Database."""
    print("\n=== Maths Trivia ===")
    url = "https://opentdb.com/api.php"
    params = {"amount": 5, "category": 19, "type": "multiple"}
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for q in data.get("results", []):
                print(f"Q: {q['question']}")
                print(f"A: {q['correct_answer']}\n")
        else:
            print(f"Unexpected status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the trivia API.")


def handle_not_found():
    """Demonstrate handling a 404 response."""
    print("\n=== Handle 404 ===")
    response = requests.get("https://jsonplaceholder.typicode.com/todos/99999")
    if response.status_code == 200:
        print(response.json())
    elif response.status_code == 404:
        print("Resource not found.")
    else:
        print(f"Unexpected status: {response.status_code}")


if __name__ == "__main__":
    fetch_single_todo()
    fetch_todo_summary()
    fetch_posts_by_user(user_id=1)
    handle_not_found()
    fetch_maths_trivia()
