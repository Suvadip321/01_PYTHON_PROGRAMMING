import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))         
plt.plot(x, y)
plt.title("Line Plot: Sine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()