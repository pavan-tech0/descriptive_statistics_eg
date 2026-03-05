import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'Age'   : np.random.randint(22, 60, 100),
    'Salary': np.random.normal(60000, 15000, 100).astype(int)
})

print(f"Data:{df}")
print(df.describe().round(2))
print(f"\nIQR Age   : {df.Age.quantile(0.75) - df.Age.quantile(0.25):.1f}")
print(f"IQR Salary: {df.Salary.quantile(0.75) - df.Salary.quantile(0.25):.0f}")