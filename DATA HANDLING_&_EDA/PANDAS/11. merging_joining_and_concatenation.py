import pandas as pd 

employees = pd.DataFrame({
  'id': [1, 2, 3, 4, 5],
  'name': ['john', 'anna', 'peter', 'linda', 'bob'],
  'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})
salaries = pd.DataFrame({
  'id': [1, 2, 3, 6, 7],
  'salary': [60000, 80000, 65000, 70000, 90000],
  'bonus': [5000, 10000, 7000, 8000, 12000]
})

print("merging:")
df_merged1 = pd.merge(employees, salaries, on='id', how='inner')
print(df_merged1)

df_merged2 = pd.merge(employees, salaries, on='id', how='outer')
print(df_merged2)

df_merged3 = pd.merge(employees, salaries, on='id', how='left')
print(df_merged3)

df_merged4 = pd.merge(employees, salaries, on='id', how='right')
print(df_merged4)

employees = pd.DataFrame({
  'id': [1, 2, 3, 4, 5],
  'name': ['john', 'anna', 'peter', 'linda', 'bob'],
  'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})
salaries = pd.DataFrame({
  'salary': [60000, 80000, 65000, 70000, 90000],
  'bonus': [5000, 10000, 7000, 8000, 12000]
})

print("concatenation:")
df_concat = pd.concat([employees, salaries], axis=1)
print(df_concat)

print("joining:")
df1 = pd.DataFrame({
  'name': ['alice', 'bob', 'charlie']
}, index=[1, 2, 3])

df2 = pd.DataFrame({
  'score': [85, 90, 75]
}, index=[2, 3, 4])

joined = df1.join(df2)
print(joined)