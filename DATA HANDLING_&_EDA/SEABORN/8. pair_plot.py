import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.pairplot(tips, hue='sex')
plt.show()