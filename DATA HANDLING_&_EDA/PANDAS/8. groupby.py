import pandas as pd 

data = {
  'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
  'Employee': ['A', 'B', 'C', 'D', 'E', 'F'],
  'Salary': [50000, 60000, 55000, 45000, 65000, 70000]
}
df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].mean()
print(result)

result = df.groupby('Department')['Salary'].sum()
print(result)

result = df.groupby('Department')['Salary'].max()
print(result)

result = df.groupby('Department')['Salary'].min()
print(result)

result = df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'count', 'std', 'median'])
print(result)