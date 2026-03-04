import numpy as np
from scipy import stats
import random

data = [random.randint(1,150) for _ in range(60)]
print("data = ", data)


mean_manual = sum(data)/len(data)
mean_np = np.mean(data)

print(f"mean manual = ", mean_manual)
print(f"mean numpy = ",mean_np)

median_manual = sorted(data)[len(data)//2]
median_np = np.median(data)

print(f"median manual = ", median_manual)
print(f"median numpy = ",median_np)

mode_manual = max(set(data), key=data.count)
mode_scipy = stats.mode(data, keepdims=True)
print(f"mode manual = ", mode_manual)
print(f"mode scipy = ", mode_scipy.mode[0], "count = ", mode_scipy.count[0],)
