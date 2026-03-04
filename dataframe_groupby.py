import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Department': ['HR','IT','IT','HR','IT','HR','Finance','Finance'],
    'Salary'    : [50000,90000,85000,52000,95000,48000,70000,75000]
})

summary = df.groupby('Department')['Salary'].agg(
    Mean='mean', Median='median', Mode=lambda x: x.mode()[0]
).round(2)

print(df)

print(summary)

