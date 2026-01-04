import numpy as np 

print("scalar with array:")
arr = np.array([1, 2, 3, 4])
result = arr + 10
print(result)

print("1d array with 2d array:")
arr1d = np.array([10, 20, 30])
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
result = arr1d + arr2d
print(result)

print("different broadcasting example:")
row_vector = np.array([ [1],
                        [2],
                        [3]])
column_vector = np.array([10, 20])
result = row_vector + column_vector
print(result)