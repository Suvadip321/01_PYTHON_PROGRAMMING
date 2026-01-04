import numpy as np 

print("basic arithmetic:")
a1 = np.array([1, 2, 3, 4])
a2 = np.array([10, 20, 30, 40])
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)

print(a1 + 1)
print(a2 * 2)

print("mathematical functions:")
arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))
print(np.log(arr))
print(np.exp(arr))

angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))
print(np.cos(angles))

decimals = np.array([1.234, 5.678, 9.999])
print(np.round(decimals, 2))