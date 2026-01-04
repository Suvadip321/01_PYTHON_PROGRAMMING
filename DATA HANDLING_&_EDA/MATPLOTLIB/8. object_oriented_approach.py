import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(x, np.sin(x), color='red')
ax[0].set_title('sine wave')

ax[1].plot(x, np.cos(x), color='blue')
ax[1].set_title('cosine wave')

plt.suptitle('sine & cosine wave')
plt.show()

fig, ax = plt.subplots(2, 2, figsize=(10, 6))

ax[0, 0].plot(x, np.sin(x), color='red')
ax[0, 0].set_title('sine')

ax[0, 1].plot(x, np.cos(x), color='blue')
ax[0, 1].set_title('cosine')

ax[1, 0].plot(x, np.tan(x), color='green')
ax[1, 0].set_title('tangent')

ax[1, 1].plot(x, np.exp(x), color='yellow')
ax[1, 1].set_title('exponential')

plt.tight_layout()
plt.show()