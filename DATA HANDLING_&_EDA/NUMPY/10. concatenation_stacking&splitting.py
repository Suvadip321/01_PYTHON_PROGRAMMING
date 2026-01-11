import numpy as np 

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

concatenate = np.concatenate([a1, a2])
print(f"concatenated: {concatenate}")

vstack = np.vstack([a1, a2])
print(f"vstack:\n{vstack}")

hstack = np.hstack([a1, a2])
print(f"hstack:\n{hstack}")

arr1 = np.array([
    [1, 2],
    [3, 4]
])
arr2 = np.array([
    [5, 6],
    [7, 8]]
)

concatenate_0 = np.concatenate([arr1, arr2], axis=0)
print(f"concatenate_0:\n{concatenate_0}")
concatenate_1 = np.concatenate([arr1, arr2], axis=1)
print(f"concatenate_1:\n{concatenate_1}")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

split = np.split(arr, 4)
print(f"split: {split}")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

vsplit = np.vsplit(arr, 2)
print(f"vsplit:\n{vsplit}")

hsplit = np.hsplit(arr, 2)
print(f"hsplit:\n{hsplit}")
