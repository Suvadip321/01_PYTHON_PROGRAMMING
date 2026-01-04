import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.scatterplot(x='total_bill', y='tip', hue='sex', data=tips)
plt.show()