import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1) # 2 rows, 2 columns, 1st plot
plt.plot(x, np.sin(x), label='sin(x)', color='red')
plt.title('sine')
plt.legend()

plt.subplot(2, 2, 2) # 2nd plot
plt.plot(x, np.cos(x), label='cos(x)', color='blue')
plt.title('cosine')
plt.legend()

plt.subplot(2, 2, 3) # 3rd plot
plt.plot(x, np.tan(x), label='tan(x)', color='green')
plt.title('tangent')
plt.legend()

plt.subplot(2, 2, 4) # 4th plot
plt.plot(x, np.exp(x), label='exp(x)', color='yellow')
plt.title('exponential')
plt.legend()

plt.suptitle('Multiple Plots')
plt.tight_layout() # adjusts spacing to avoid overlap
plt.show()
