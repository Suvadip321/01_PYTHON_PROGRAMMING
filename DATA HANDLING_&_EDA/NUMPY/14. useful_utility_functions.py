import numpy as np 

arr = np.array([3, 1, 2, 5, 4, 3])
copied_arr = np.copy(arr)

print(f"copied array: {copied_arr}")
print(f"sorted order: {np.sort(arr)}")
print(f"indices of sorted order: {np.argsort(arr)}")
print(f"unique elements: {np.unique(arr)}")
