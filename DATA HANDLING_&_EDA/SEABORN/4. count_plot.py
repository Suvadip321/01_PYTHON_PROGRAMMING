import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.countplot(x='smoker', hue='sex', data=tips)
plt.show()