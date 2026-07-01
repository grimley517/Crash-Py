# Lesson 10 - Dictionaries
# Run this script with:  python3 dictionaries.py


# --- Creating a dictionary ---
student = {
    "name": "Alice",
    "score": 87,
    "grade": "A"
}
print(student)

# --- Accessing values ---
print(student["name"])
print(student.get("age", "unknown"))   # default if key missing

# --- Adding and updating ---
student["age"] = 16
student["score"] = 90
print(student)

# --- Removing ---
del student["age"]
print(student)

# --- Checking for a key ---
if "name" in student:
    print("Name:", student["name"])

# --- Iterating ---
print("\nKeys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# --- Class register ---
class_register = {
    "Alice":   87,
    "Bob":     72,
    "Charlie": 95,
    "Diana":   68,
}

for name, score in class_register.items():
    print(f"{name}: {score}")

top_student = max(class_register, key=class_register.get)
print(f"Top student: {top_student} ({class_register[top_student]})")

# --- Nested dictionaries ---
students = {
    "Alice": {"score": 87, "grade": "A"},
    "Bob":   {"score": 72, "grade": "C"},
}
for name, details in students.items():
    print(f"{name}: score={details['score']}, grade={details['grade']}")

# --- letter_count ---
def letter_count(text):
    counts = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return counts

print(letter_count("Mathematics"))

# --- dict() construction ---
d = dict(a=1, b=2, c=3)
print(d)
