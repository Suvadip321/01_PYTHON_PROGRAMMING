import numpy as np 

arr = np.array([["1", "2", "3"], ["4", "5", "6"]])
print(f"array:\n{arr}")

print(f"dimension: {arr.ndim}")
print(f"shape: {arr.shape}")
print(f"size: {arr.size}")
print(f"data type: {arr.dtype}")

int_arr = arr.astype(int)
print(f"int_arr:\n{int_arr}")
print(int_arr.dtype)
