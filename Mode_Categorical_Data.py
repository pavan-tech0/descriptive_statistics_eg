import pandas as pd

survey = pd.Series(["Python", "Java", "Python", "C++",
                    "Python", "Java", "Python", "R",
                    "Java", "Java"])

# Value counts
print(survey.value_counts())
print(f"\nMode (most common language): {survey.mode()[0]}")
print(f"Bimodal modes: {list(survey.mode())}")

