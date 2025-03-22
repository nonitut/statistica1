import numpy as np

otc1 = np.array([2, 4, 5, 8, 9, 10, 14, 16])
otc2 = np.array([6, 12, 15, 24, 27, 30, 42, 48])

std_otc1 = np.std(otc1, ddof=1)
std_otc2 = np.std(otc2, ddof=1)

print(f"Стандартное отклонение 1: {std_otc1:.2f}")
print(f"Стандартное отклонение 2: {std_otc2:.2f}")
print(std_otc1 * 3)