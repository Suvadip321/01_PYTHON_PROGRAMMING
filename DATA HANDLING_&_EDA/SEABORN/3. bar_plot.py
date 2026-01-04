import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.barplot(x='day', y='total_bill', data=tips, estimator=sum, ci=None)
plt.show()