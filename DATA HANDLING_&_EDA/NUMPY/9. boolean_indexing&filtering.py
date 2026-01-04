import numpy as np 

data = np.array([1, 5, 3, 8, 2, 7, 4, 6])

print(f"data > 4: {data > 4}")
print(f"data[data > 4]: {data[data > 4]}")
print(f"data[(data > 3) & (data < 7)]: {data[(data > 3) & (data < 7)]}")
print(f"where(data > 5): {np.where(data > 5, data, 0)}")
print(f"index where(data > 5): {np.where(data > 5)[0]}")
print(f"any(data > 10): {any(data > 10)}")
print(f"all(data) > 0: {all(data > 0)}")

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = matrix <= 5
print(f"matrix[mask]: {matrix[mask]}")