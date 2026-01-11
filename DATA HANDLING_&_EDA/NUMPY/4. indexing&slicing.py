import numpy as np 

arr1d = np.array([10, 20, 30, 40, 50])

print("single element access:")
print(arr1d[0])
print(arr1d[-1])

print("slicing: [start:stop:step]")
print(arr1d[1:4])
print(arr1d[0:5])
print(arr1d[0:])
print(arr1d[:])
print(arr1d[0:5:2])
print(arr1d[::2])
print(arr1d[::-1])

arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
])

print("multidimensional indexing:")
print(arr2d[0, 0])
print(arr2d[1, 1])
print(arr2d[2, 2])
print(arr2d[0])
print(arr2d[1])
print(arr2d[2])

print("subarray slicing:")
print(arr2d[1, :])
print(arr2d[:, 1])
print(arr2d[0:3, 0:3])
print(arr2d[0:2, 0:2])
print(arr2d[0:2, 1:3])
print(arr2d[1:3, 0:2])
print(arr2d[1:3, 1:3])

print("fancy indexing:")
indices = np.array([0, 2, 4])
print(arr1d[indices])
