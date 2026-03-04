import numpy as np

scores  = [85, 92, 78, 95, 88]         # Quiz, Mid, Lab, Final, Project
weights = [0.10, 0.25, 0.15, 0.35, 0.15]  # Must sum to 1.0

simple_mean   = np.mean(scores)
weighted_mean = np.average(scores, weights=weights)

print(f"Simple Mean  : {simple_mean:.2f}")
print(f"Weighted Mean: {weighted_mean:.2f}")
print(f"Weights sum  : {sum(weights)}")

# Manual verification
manual_wm = sum(s * w for s, w in zip(scores, weights))
print(f"Manual check : {manual_wm:.2f}")