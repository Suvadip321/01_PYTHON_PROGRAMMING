import numpy as np 

data = np.array([[1, 2, 3], [4, 5, 6]])
print(data)

np.save('data.npy', data)

loaded_data = np.load('data.npy')
print(loaded_data)
