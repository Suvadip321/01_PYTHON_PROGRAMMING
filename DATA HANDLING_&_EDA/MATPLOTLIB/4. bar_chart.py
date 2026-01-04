import matplotlib.pyplot as plt 

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

plt.bar(categories, values, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('values')
plt.show()

plt.barh(categories, values, color='orange')
plt.title('Horizontal Bar Chart')
plt.show()