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
print("concatenating along columns:")
df_concat_cols = pd.concat([employees, salaries], axis=1)
print(df_concat_cols )

print("concatenating along rows:")
df1 = pd.DataFrame({
  'A': ['A0', 'A1', 'A2'],
  'B': ['B0', 'B1', 'B2']
})
df2 = pd.DataFrame({ 
  'A': ['A3', 'A4', 'A5'],
  'B': ['B3', 'B4', 'B5']
})
df3 = pd.DataFrame({
  'A': ['A6', 'A7', 'A8'],
  'B': ['B6', 'B7', 'B8']
})

df_concat_rows = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(df_concat_rows)
