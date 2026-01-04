import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.histplot(tips['total_bill'], bins=30, kde='True')
plt.title('Distribution of Total Bill')
plt.show()