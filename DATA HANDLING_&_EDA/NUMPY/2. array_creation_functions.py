import numpy as np 

zeros = np.zeros((2, 3))
print(f"zeros:\n{zeros}")

ones = np.ones((3, 2))
print(f"ones:\n{ones}")

full = np.full((2, 2), 7)
print(f"full:\n{full}")

eye = np.eye(3)
print(f"eye:\n{eye}")

arange = np.arange(0, 10, 2)
print(f"arange:\n{arange}")

linspace = np.linspace(0, 1, 5)
print(f"linspace:\n{linspace}")
