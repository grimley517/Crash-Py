# Lesson 25 - Pandas Statistics
# Run this script with:  python3 pandas_stats.py
#
# Install dependencies first:
#   pip3 install pandas openpyxl
#
# Place student_scores.csv in the same folder.

import pandas as pd


def main():
    # --- Load the dataset ---
    df = pd.read_csv("student_scores.csv")

    print("=== First 5 rows ===")
    print(df.head())
    print(f"\nShape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nData types:\n{df.dtypes}")

    # --- Descriptive statistics ---
    print("\n=== Descriptive Statistics ===")
    print(df.describe())

    print(f"\nMean score:   {df['Score'].mean():.1f}")
    print(f"Median score: {df['Score'].median():.1f}")
    print(f"Std dev:      {df['Score'].std():.1f}")
    print(f"Min score:    {df['Score'].min()}")
    print(f"Max score:    {df['Score'].max()}")

    # --- Filtering ---
    print("\n=== Students who scored >= 80 ===")
    high_scorers = df[df["Score"] >= 80]
    print(high_scorers[["Name", "Topic", "Score", "Grade"]])

    # --- Grouping ---
    print("\n=== Average score per topic ===")
    topic_avg = df.groupby("Topic")["Score"].mean()
    print(topic_avg.round(1))

    print("\n=== Grade counts ===")
    print(df["Grade"].value_counts())

    # --- Top scorer per topic ---
    print("\n=== Top scorer per topic ===")
    idx = df.groupby("Topic")["Score"].idxmax()
    print(df.loc[idx, ["Topic", "Name", "Score"]])

    # --- Sorting ---
    print("\n=== Top 5 students by score ===")
    print(df.sort_values("Score", ascending=False).head(5)[["Name", "Topic", "Score", "Grade"]])

    # --- Adding a column ---
    df["Result"] = df["Score"].apply(lambda s: "Pass" if s >= 50 else "Fail")
    print("\n=== Pass / Fail counts ===")
    print(df["Result"].value_counts())

    # --- How many scored below average? ---
    avg = df["Score"].mean()
    below_avg = (df["Score"] < avg).sum()
    print(f"\nStudents below average ({avg:.1f}): {below_avg}")

    # --- Save to CSV ---
    df.to_csv("student_scores_with_results.csv", index=False)
    print("\nSaved student_scores_with_results.csv")

    # --- Read from Excel (requires openpyxl) ---
    # Uncomment the lines below if you have student_scores.xlsx from Lesson 12
    # df_excel = pd.read_excel("student_scores.xlsx")
    # print(df_excel.head())


if __name__ == "__main__":
    main()
