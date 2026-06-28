# Lesson 6 - Text Files
# Run this script with:  python3 text_files.py


# --- Writing a file ---
with open("notes.txt", "w") as f:
    f.write("Line one\n")
    f.write("Line two\n")
    f.write("Line three\n")

print("notes.txt written.")

# --- Reading the whole file ---
with open("notes.txt", "r") as f:
    contents = f.read()
print(contents)

# --- Reading line by line ---
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# --- readlines() ---
with open("notes.txt", "r") as f:
    lines = f.readlines()
print(f"Number of lines: {len(lines)}")

# --- Appending ---
with open("notes.txt", "a") as f:
    f.write("Line four\n")

# --- Times table to file ---
def save_times_table(n, filename):
    with open(filename, "w") as f:
        for i in range(1, 13):
            line = f"{i:2d} × {n} = {i * n:3d}\n"
            f.write(line)

save_times_table(7, "seven_times_table.txt")
print("Times table saved to seven_times_table.txt")

# --- Handling a missing file ---
try:
    with open("missing_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("The file does not exist.")

# --- Read sample.txt ---
try:
    with open("sample.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("sample.txt not found — download it from the lesson resources.")
