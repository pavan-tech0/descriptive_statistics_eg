import numpy as np
from scipy import stats
import random

income = np.array([random.randint(25000, 100000) for _ in range(40)])  # one high earner

mean   = np.mean(income)
median = np.median(income)
std    = np.std(income, ddof=1)

pearson_skew = 3 * (mean - median) / std
scipy_skew   = stats.skew(income)

print(f"Mean         : {mean:,.0f}")
print(f"Median       : {median:,.0f}")
print(f"Pearson Skew : {pearson_skew:.3f}")
print(f"SciPy Skew   : {scipy_skew:.3f}")
print(f"Interpretation: {'Right (positive) skew' if pearson_skew > 0 else 'Left (negative) skew'}")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,5))
sns.histplot(income,kde=True, color = 'lightgreen', stat = "density")
plt.title(f'Income Distribution \n Pearson Skew: {pearson_skew:.2f} | Scipy Skew: {scipy_skew:.2f}')
plt.axvline(mean, color='red', linestyle='--', label='Mean')
plt.axvline(median, color='blue', linestyle='--', label='Median')
plt.tight_layout()
plt.show()
