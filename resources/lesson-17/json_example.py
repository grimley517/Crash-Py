# Lesson 17 - JSON
# Run this script with:  python3 json_example.py
#
# Place student_scores.csv in the same folder before running.

import json
import csv


# --- json.dumps(): Python → JSON string ---
student = {
    "name": "Alice",
    "score": 87,
    "grade": "A",
    "topics": ["Algebra", "Geometry"],
    "passed": True
}

json_text = json.dumps(student, indent=2)
print("=== json.dumps() ===")
print(json_text)

# --- json.loads(): JSON string → Python ---
print("\n=== json.loads() ===")
json_str = '{"name": "Bob", "score": 72, "passed": true}'
data = json.loads(json_str)
print(data["name"])
print(type(data))

# --- Writing and reading a JSON file ---
students = [
    {"name": "Alice", "score": 87},
    {"name": "Bob",   "score": 72},
    {"name": "Charlie", "score": 95},
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)
print("\nstudents.json written.")

with open("students.json", "r") as f:
    loaded = json.load(f)

print("\n=== Read back from students.json ===")
for s in loaded:
    print(s["name"], s["score"])

# --- CSV marksheet to JSON ---
print("\n=== Converting CSV marksheet to JSON ===")
marksheet = []

with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        marksheet.append({
            "id":    int(row["StudentID"]),
            "name":  row["Name"],
            "topic": row["Topic"],
            "score": int(row["Score"]),
            "grade": row["Grade"],
        })

with open("marksheet.json", "w") as f:
    json.dump(marksheet, f, indent=2)

print(f"Exported {len(marksheet)} students to marksheet.json")

# --- Group by topic ---
print("\n=== Average score per topic ===")
topic_scores = {}
for entry in marksheet:
    t = entry["topic"]
    if t not in topic_scores:
        topic_scores[t] = []
    topic_scores[t].append(entry["score"])

for topic, scores in sorted(topic_scores.items()):
    avg = sum(scores) / len(scores)
    print(f"  {topic}: {avg:.1f}")
