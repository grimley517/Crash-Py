# Lesson 11 - CSV Files
# Run this script with:  python3 csv_files.py
#
# Place student_scores.csv in the same folder before running.

import csv
import openpyxl


# --- Reading a CSV ---
print("=== Reading CSV ===")
with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# --- Skipping the header ---
print("\n=== Skipping header ===")
with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Columns:", header)
    for row in reader:
        print(row)

# --- DictReader ---
print("\n=== DictReader ===")
with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} scored {row['Score']}")

# --- Statistics ---
print("\n=== Statistics ===")
scores = []
with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        scores.append(int(row["Score"]))

print(f"Average: {sum(scores) / len(scores):.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest:  {min(scores)}")

# --- Writing a CSV ---
results = [
    ["Name", "Score", "Grade"],
    ["Alice",   85, "A"],
    ["Bob",     72, "C"],
    ["Charlie", 95, "A*"],
]
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)
print("\noutput.csv written.")

# --- Converting CSV to Excel ---
wb = openpyxl.Workbook()
ws = wb.active

with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        ws.append(row)

wb.save("student_scores_from_csv.xlsx")
print("student_scores_from_csv.xlsx created.")

# --- Grade counts ---
print("\n=== Grade counts ===")
grade_counts = {}
with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        g = row["Grade"]
        grade_counts[g] = grade_counts.get(g, 0) + 1

for grade, count in sorted(grade_counts.items()):
    print(f"  {grade}: {count}")
