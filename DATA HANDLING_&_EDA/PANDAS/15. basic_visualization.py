import pandas as pd 
import matplotlib.pyplot as plt 

data = {
  'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
  'Sales': [250, 300, 400, 350, 500, 600],
  'Profit': [100, 120, 180, 160, 220, 300]
}
df = pd.DataFrame(data)

# line plot
df.plot(x='Month', y='Sales', kind='line', marker='o', title='Monthly Sales')
plt.show()

# bar plot
df.plot(x='Month', y='Sales', kind='bar', title='Sales by Month')
plt.show()

# multiple columns in one plot
df.plot(x='Month', y=['Sales', 'Profit'], kind='line', marker='o', title='Sales vs Profit')
plt.show()

# histogram
df['Sales'].plot(kind='hist', bins=5, title='Sales Distribution')
plt.show()

# scatter plot
df.plot(x='Sales', y='Profit', kind='scatter', title='Sales vs Profit')
plt.show()
