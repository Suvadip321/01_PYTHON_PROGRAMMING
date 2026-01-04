import numpy as np 
import matplotlib.pyplot as plt


sizes = [40, 25, 20, 15, 30]
labels = ['A', 'B', 'C', 'D', 'E']

plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()