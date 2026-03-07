import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns 

np.random.seed(1)
n = 2000

distributions = {
    "Normal (Mesokurtic)" : np.random.normal(0, 1, n),
    "t(3) Leptokurtic"    : np.random.standard_t(3, n),   # heavy tails
    "Uniform Platykurtic" : np.random.uniform(-3, 3, n),   # light tails
}

print(f"{'Distribution':<25} {'Excess Kurt':>12} {'Type'}")
print("-" * 55)
for name, data in distributions.items():
    ek = stats.kurtosis(data)
    kind = "Mesokurtic" if abs(ek) < 0.5 else ("Leptokurtic" if ek > 0 else "Platykurtic")
    print(f"{name:<25} {ek:>12.3f}   {kind}")
    plt.figure(figsize=(12,5))
    sns.histplot(data, kde=True, color='lightblue', stat="density")
    plt.title(f'{name} \n Excess Kurtosis: {ek:.2f} | Type: {kind}')
    plt.axvline(np.mean(data), color='red', linestyle='--', label= 'mean')
    plt.axvline(np.median(data), color='blue', linestyle='--', label= 'median')
    plt.legend()
    plt.tight_layout()
    plt.show()

