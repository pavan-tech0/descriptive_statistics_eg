import numpy as np
from scipy import stats

np.random.seed(0)
normal_data = np.random.normal(0, 1, 1000)
right_skewed = np.random.exponential(2, 1000)  # always positive → right skew

for name, data in [("Normal", normal_data), ("Right-Skewed", right_skewed)]:
    skew = stats.skew(data)
    kurt = stats.kurtosis(data)  # excess kurtosis
    print(f"\n{name}:")
    print(f"  Skewness         : {skew:.3f}")
    print(f"  Excess Kurtosis  : {kurt:.3f}")
    print(f"  Shape            : {'Symmetric' if abs(skew)<0.5 else 'Skewed'}")

import matplotlib.pyplot as plt
import seaborn as sns

# Create the figure
plt.figure(figsize=(12, 5))

# Plot 1: Normal Distribution
plt.subplot(1, 2, 1)
sns.histplot(normal_data, kde=True, color='skyblue', stat="density")
plt.title(f'Normal Distribution\nSkew: {stats.skew(normal_data):.2f} | Kurt: {stats.kurtosis(normal_data):.2f}')
plt.axvline(np.mean(normal_data), color='red', linestyle='--', label='Mean')

# Plot 2: Right-Skewed Distribution
plt.subplot(1, 2, 2)
sns.histplot(right_skewed, kde=True, color='salmon', stat="density")
plt.title(f'Right-Skewed (Exponential)\nSkew: {stats.skew(right_skewed):.2f} | Kurt: {stats.kurtosis(right_skewed):.2f}')
plt.axvline(np.mean(right_skewed), color='red', linestyle='--', label='Mean')

plt.tight_layout()
plt.show()