import numpy as np

arr = np.arange(12)
print(f"arr: {arr}")

reshape = arr.reshape(3, 4)
print(f"reshaped:\n{reshape}")

flatten = reshape.flatten()
print(f"flatten:\n{flatten}")

transpose = reshape.T
print(f"transpose:\n{transpose}")

