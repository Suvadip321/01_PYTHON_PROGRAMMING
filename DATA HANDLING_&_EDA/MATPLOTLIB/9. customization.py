import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y1, y2 = np.sin(x), np.cos(x)

plt.style.use('seaborn-v0_8-whitegrid') # good default style

plt.figure(figsize=(8, 5), dpi=100) # figure size & resolution

# basic plot with customizations
plt.plot(x, y1, label='sine', color='red', linewidth=1, linestyle='--', marker='o', markersize=4, alpha=0.75)
plt.plot(x, y2, label='cosine', color='blue', linewidth=1, linestyle='--', marker='*', markersize=4, alpha=0.75)

# titles and labels
plt.title('Customized Line Plot', fontsize=16, fontweight='bold')
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)

# limits and ticks
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, 11, 1), fontsize=10)
plt.yticks(np.arange(-1.5, 1.6, 0.25), fontsize=10)

# grid
plt.grid(True, which='major',linestyle='--', alpha=0.5)

# legend 
plt.legend(loc='upper right', fontsize=10, frameon=True, shadow=True)

# annotations 
plt.annotate('peak', xy=(1.57, 1), xytext=(3, 1.2), arrowprops=dict(facecolor='black', arrowstyle='->', lw=1))

plt.show()