# Lesson 5 - Strings
# Run this script with:  python3 strings.py


# --- Creating strings ---
name = "Alice"
subject = 'Mathematics'
note = """This is a
multi-line string."""
print(note)

# --- Concatenation and repetition ---
first = "Hello"
second = "World"
message = first + ", " + second + "!"
print(message)

line = "-" * 30
print(line)

# --- f-strings ---
score = 87
print(f"{name} scored {score}%")
print(f"{name} scored {score:.1f}%")
print(f"Double her score: {score * 2}")

# --- String methods ---
text = "  Hello, World!  "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("World", "Python"))
print(text.strip().startswith("Hello"))
print(text.strip().endswith("!"))

# --- Splitting and joining ---
csv_line = "Alice,87,A"
parts = csv_line.split(",")
print(parts)
rejoined = " | ".join(parts)
print(rejoined)

# --- Indexing and slicing ---
word = "Mathematics"
print(word[0])      # M
print(word[-1])     # s
print(word[0:4])    # Math
print(word[4:])     # ematics
print(len(word))    # 11

# --- Checking content ---
sentence = "The quick brown fox"
print("quick" in sentence)
print(sentence.count("o"))
print(sentence.find("brown"))

# --- Converting to string ---
grade = "A*"
print("Score: " + str(score))
print(f"Score: {score}, Grade: {grade}")

# --- Title case helper ---
def title_case(full_name):
    return full_name.strip().title()

print(title_case("  alice smith  "))   # Alice Smith

# --- Initials ---
def initials(full_name):
    parts = full_name.strip().split()
    return ".".join(p[0].upper() for p in parts) + "."

print(initials("Alice Mary Smith"))   # A.M.S.
