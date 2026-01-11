import pandas as pd 

data = {
  'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
  'Employee': ['A', 'B', 'C', 'D', 'E', 'F'],
  'Age': [25, 30, 28, 35, 32, 29],
  'Salary': [50000, 60000, 55000, 45000, 65000, 70000]
}
df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].mean()
print(result)

result = df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'count', 'std', 'median'])
print(result)

result = df.groupby('Department')[['Salary', 'Age']].agg({
    'Salary': ['mean', 'max'],
    'Age': ['min', 'max']
})
print(result)

result = df.groupby(['Department', 'Employee'])['Salary'].sum()
print(result)
