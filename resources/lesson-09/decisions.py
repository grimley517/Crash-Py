# Lesson 6 - Decisions
# Run this script with:  python3 decisions.py


# --- Basic if ---
score = 75
if score >= 50:
    print("Pass")

# --- if ... else ---
score = 45
if score >= 50:
    print("Pass")
else:
    print("Fail")

# --- Grade function ---
def grade(score):
    if score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "U"

for s in [95, 85, 72, 62, 55, 40]:
    print(f"{s} → {grade(s)}")

# --- Boolean data and operations ---
passed_exam = True
good_attendance = False

print(type(passed_exam))
print(passed_exam and good_attendance)
print(passed_exam or good_attendance)
print(not passed_exam)

# --- Logical operators ---
score = 75
attendance = 80

if score >= 50 and attendance >= 75:
    print("Eligible for certificate")

if score >= 90 or attendance >= 95:
    print("Distinction candidate")
else:
    print("Not a distinction candidate (this time)")

# --- Chaining comparisons ---
mark = 73
if 70 <= mark < 80:
    print(f"{mark} is a Grade B")

# --- Triangle classifier ---
def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print(classify_triangle(5, 5, 5))
print(classify_triangle(5, 5, 8))
print(classify_triangle(3, 4, 5))

# --- Valid triangle check ---
def is_valid_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(is_valid_triangle(3, 4, 5))   # True
print(is_valid_triangle(1, 2, 10))  # False

# --- FizzBuzz ---
def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

for i in range(1, 21):
    print(fizzbuzz(i), end=" ")
print()
