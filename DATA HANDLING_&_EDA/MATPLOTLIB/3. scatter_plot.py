import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', marker='o', alpha=0.7)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()