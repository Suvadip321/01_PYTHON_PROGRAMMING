import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"dot product: {np.dot(a, b)}")

matrix1 = np.array([[1, 2],
                    [3, 4]])
matrix2 = np.array([[5, 6],
                    [7, 8]])

print(f"matrix multiplication:\n{matrix1 @ matrix2}")

matrix = np.array( [[1, 2],
                    [3, 4]] )

print(f"transpose:\n{np.transpose(matrix)}")
print(f"determinant:\n{np.linalg.det(matrix)}")
print(f"inverse:\n{np.linalg.inv(matrix)}")
print(f"eigen values: {np.linalg.eigvals(matrix)}")
