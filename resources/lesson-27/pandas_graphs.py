# Lesson 15 - Pandas Graphs with matplotlib
# Run this script with:  python3 pandas_graphs.py
#
# Install dependencies first:
#   pip3 install pandas matplotlib openpyxl
#
# Place student_scores.csv in the same folder.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("student_scores.csv")

    # Use a clean style
    plt.style.use("ggplot")

    # ── 1. Bar chart: average score by topic ──────────────────────────────────
    topic_avg = df.groupby("Topic")["Score"].mean()

    topic_avg.plot(kind="bar", color="steelblue", edgecolor="black")
    plt.title("Average Score by Topic")
    plt.xlabel("Topic")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("avg_by_topic.png", dpi=150)
    plt.show()
    print("Saved avg_by_topic.png")

    # ── 2. Histogram: score distribution ──────────────────────────────────────
    df["Score"].plot(kind="hist", bins=10, edgecolor="black", color="coral")
    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("score_distribution.png", dpi=150)
    plt.show()
    print("Saved score_distribution.png")

    # ── 3. Scatter plot: student ID vs score ──────────────────────────────────
    plt.figure(figsize=(8, 5))
    plt.scatter(df["StudentID"], df["Score"], alpha=0.6, color="green")
    mean_score = df["Score"].mean()
    plt.axhline(y=mean_score, color="red", linestyle="--",
                label=f"Mean: {mean_score:.1f}")
    plt.title("Score by Student ID")
    plt.xlabel("Student ID")
    plt.ylabel("Score")
    plt.legend()
    plt.tight_layout()
    plt.savefig("scatter.png", dpi=150)
    plt.show()
    print("Saved scatter.png")

    # ── 4. Box plot: score spread per topic ───────────────────────────────────
    df.boxplot(column="Score", by="Topic", figsize=(10, 6))
    plt.title("Score Spread by Topic")
    plt.suptitle("")
    plt.xlabel("Topic")
    plt.ylabel("Score")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("boxplot.png", dpi=150)
    plt.show()
    print("Saved boxplot.png")

    # ── 5. Pie chart: grade distribution ──────────────────────────────────────
    grade_counts = df["Grade"].value_counts()
    colours = ["gold", "lightblue", "lightgreen", "salmon", "violet", "grey"]

    grade_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        colors=colours[:len(grade_counts)]
    )
    plt.title("Grade Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("grades_pie.png", dpi=150)
    plt.show()
    print("Saved grades_pie.png")

    # ── 6. Combined subplots ───────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    df["Score"].plot(
        kind="hist", bins=10, ax=axes[0],
        color="steelblue", edgecolor="black",
        title="Score Distribution"
    )
    axes[0].set_xlabel("Score")
    axes[0].set_ylabel("Number of Students")

    df.groupby("Topic")["Score"].mean().plot(
        kind="bar", ax=axes[1],
        color="coral", edgecolor="black",
        title="Average by Topic"
    )
    axes[1].set_xlabel("Topic")
    axes[1].set_ylabel("Average Score")
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("combined.png", dpi=150)
    plt.show()
    print("Saved combined.png")


if __name__ == "__main__":
    main()
