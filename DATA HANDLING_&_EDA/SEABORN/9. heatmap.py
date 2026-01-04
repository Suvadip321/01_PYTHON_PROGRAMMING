import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

corr = tips.corr(numeric_only=True)
print(corr)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()