import numpy as np

arr = np.arange(12)
print(f"arr: {arr}")

reshape = arr.reshape(4, 3) # Use -1 for auto reshape (arr.reshape(4, -1) / arr.reshape(-1, 4))    
print(f"reshaped:\n{reshape}")

flatten = reshape.flatten()
print(f"flatten:\n{flatten}")

transpose = reshape.T
print(f"transpose:\n{transpose}")
