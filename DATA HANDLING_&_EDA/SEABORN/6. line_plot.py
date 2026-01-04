import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.lineplot(x='size', y='tip', data=tips, ci=None)
plt.show()