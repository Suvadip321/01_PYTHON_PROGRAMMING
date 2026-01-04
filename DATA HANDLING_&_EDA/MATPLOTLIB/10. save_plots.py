import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.grid(True)
plt.legend()
plt.savefig('sin_cos.png', dpi=300, bbox_inches='tight')
plt.show()