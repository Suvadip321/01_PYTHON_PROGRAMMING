import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', size='size', style='time')
plt.title('Tips vs Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.legend(title='Legend Title')
plt.show()