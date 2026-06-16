# Lesson 2 - Functions
# Run this script with:  python3 functions.py


# --- Variables and data types ---
name = "Alice"        # str
age = 16              # int
height = 1.72         # float
is_enrolled = True    # bool

print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(height))       # <class 'float'>
print(type(is_enrolled))  # <class 'bool'>

# Reassigning a variable
score = 85
print(score)   # 85
score = 90
print(score)   # 90


# --- Defining a simple function ---
def greet():
    print("Hello from inside a function!")


greet()


# --- Arguments ---
def greet_person(name):
    print("Hello,", name)


greet_person("Alice")
greet_person("Bob")


# --- Multiple arguments ---
def add(a, b):
    print(a + b)


add(3, 5)
add(10, 2)


# --- Return values ---
def multiply(a, b):
    return a * b


result = multiply(6, 7)
print("6 × 7 =", result)


# --- is_even ---
def is_even(n):
    return n % 2 == 0


print(is_even(4))   # True
print(is_even(7))   # False


# --- pass keyword ---
def calculate_area():
    pass   # placeholder — write the body later


def calculate_perimeter():
    pass


# --- Named (keyword) arguments ---
def describe_triangle(base, height):
    area = 0.5 * base * height
    print(f"Base: {base}, Height: {height}, Area: {area}")


describe_triangle(6, 4)
describe_triangle(height=4, base=6)  # same result, different order


# --- Rectangle helpers ---
def rectangle_area(width, height):
    return width * height


def rectangle_perimeter(width, height):
    return 2 * (width + height)


w, h = 5, 3
print("Area:", rectangle_area(w, h))
print("Perimeter:", rectangle_perimeter(w, h))
