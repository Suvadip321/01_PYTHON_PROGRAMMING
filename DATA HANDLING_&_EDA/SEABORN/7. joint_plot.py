import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
plt.show()