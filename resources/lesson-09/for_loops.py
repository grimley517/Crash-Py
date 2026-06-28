# Lesson 9 - For Loops with Range
# Run this script with:  python3 for_loops.py


# --- range() basics ---
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()

print("range(0, 20, 2):")
for i in range(0, 20, 2):
    print(i, end=" ")
print()

# --- Counting down ---
print("Countdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Go!")

# --- Times table ---
n = 7
print(f"\nTimes table for {n}:")
for i in range(1, 13):
    print(f"{i:2d} × {n} = {i * n:3d}")

# --- Accumulating ---
total = 0
for i in range(1, 101):
    total += i
print(f"\nSum of 1 to 100: {total}")

# --- Nested loops: multiplication grid ---
print("\n3 × 3 multiplication grid:")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} × {col} = {row * col:2d}", end="   ")
    print()

# --- break ---
for i in range(1, 100):
    if i * i > 50:
        print(f"\nFirst integer whose square exceeds 50: {i}")
        break

# --- continue ---
print("\nNumbers 1–20 that are not multiples of 3:")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# --- Prime numbers ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 50) if is_prime(n)]
print("\nPrimes below 50:", primes)

# --- Factorial ---
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

for k in range(0, 8):
    print(f"{k}! = {factorial(k)}")

# --- Pythagorean triples ---
print("\nPythagorean triples with sides < 50:")
for a in range(1, 50):
    for b in range(a, 50):
        c_sq = a**2 + b**2
        c = int(c_sq**0.5)
        if c * c == c_sq and c < 50:
            print(f"({a}, {b}, {c})")
