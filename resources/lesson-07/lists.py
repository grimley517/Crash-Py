# Lesson 7 - Lists
# Run this script with:  python3 lists.py


# --- Creating lists ---
scores = [85, 92, 78, 65, 90]
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# --- Accessing elements ---
print(scores[0])     # 85
print(scores[-1])    # 90
print(scores[1:3])   # [92, 78]
print(len(scores))   # 5

# --- Modifying a list ---
scores[2] = 80
scores.append(95)
scores.insert(0, 70)
scores.remove(65)
last = scores.pop()
print("scores after modifications:", scores)

# --- Useful operations ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sorted:", sorted(numbers))

# --- for ... in loop ---
for name in names:
    print("Hello,", name)

# --- Iterating over scores ---
class_scores = [85, 92, 78, 65, 90]
total = 0
for score in class_scores:
    total += score
average = total / len(class_scores)
print(f"Average score: {average:.1f}")

# --- Functions using lists ---
def average(numbers):
    return sum(numbers) / len(numbers)

def highest(numbers):
    return max(numbers)

def lowest(numbers):
    return min(numbers)

data = [72, 85, 91, 68, 77, 88, 95, 60]
print(f"Average: {average(data):.1f}")
print(f"Highest: {highest(data)}")
print(f"Lowest:  {lowest(data)}")

# --- Building a list with a loop ---
squares = []
for n in range(1, 11):
    squares.append(n ** 2)
print(squares)

# --- List comprehension ---
squares_comp = [n ** 2 for n in range(1, 11)]
print(squares_comp)

# --- above_average ---
def above_average(scores):
    avg = average(scores)
    return [s for s in scores if s > avg]

print(above_average(data))
