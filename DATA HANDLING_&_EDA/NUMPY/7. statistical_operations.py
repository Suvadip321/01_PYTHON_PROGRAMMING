import numpy as np 

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"sum: {np.sum(data)}")
print(f"sum along axis 0: {np.sum(data, axis=0)}") # rows collapse moving down the columns
print(f"sum along axis 1: {np.sum(data, axis=1)}") # columns collapse moving across the rows

print(f"mean: {np.mean(data)}")
print(f"median: {np.median(data)}")
print(f"variance: {np.var(data)}")
print(f"standard deviation: {np.std(data)}")

print(f"max: {np.max(data)}")
print(f"min: {np.min(data)}")
print(f"argmax: {np.argmax(data)}")
print(f"argmin: {np.argmin(data)}")
