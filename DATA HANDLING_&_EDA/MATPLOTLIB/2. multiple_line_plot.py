import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
        
plt.plot(x, y1, label='Sine', color='blue')
plt.plot(x, y2, label='Cosine', color='green')
plt.title("Line Plot: Sine & Cosine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()