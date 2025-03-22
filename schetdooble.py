import numpy as np

data = np.array([1, 5, 2, 7, 1, 9, 3, 8, 5, 9])

std_dev = np.std(data, ddof=1) 
print(f"Стандартное отклонение data: {std_dev:.2f}")

per1 = np.array([1, 3, 5, 6 ,6 , 7 , 9 , 11 ])
per2 = np.array([5, 7, 9, 10, 10, 11, 13, 15])

std_per1 = np.std(per1, ddof=1)
std_per2 = np.std(per2, ddof=1)

print(f"Стандартное отклонение per1: {std_per1:.2f}")
print(f"Стандартное отклонение per2: {std_per2:.2f}")
