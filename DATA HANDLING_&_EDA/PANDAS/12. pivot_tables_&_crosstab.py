import numpy as np 
import pandas as pd 

data = {
  'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
  'Employee': ['A', 'B', 'C', 'D', 'E', 'F'],
  'Salary': [50000, 60000, 55000, 45000, 65000, 70000],
  'Experience': [2, 3, 4, 5, 3, 2]
}
df = pd.DataFrame(data)

pivot1 = pd.pivot_table(df, values=['Salary', 'Experience'], index=['Department'], columns=['Employee'])
print(pivot1)

pivot2 = pd.pivot_table(df, values='Salary', index='Experience', columns='Department', aggfunc='mean')
print(pivot2)

crosstab = pd.crosstab(df['Salary'], df['Experience'])
print(crosstab)
