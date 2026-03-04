import numpy as np

salaries_no_outlier  = [40000, 42000, 45000, 47000, 50000]
salaries_with_outlier = [40000, 42000, 45000, 47000, 500000]  # CEO salary

for label, salaries in [("without outlier", salaries_no_outlier),("with outlier", salaries_with_outlier)]:
    mean_salary = np.mean(salaries)
    median_salary = np.median(salaries)
    print(f"Mean salary {label}: {mean_salary:>10,.0f} | Median salary {label}: {median_salary:>10,.0f}")