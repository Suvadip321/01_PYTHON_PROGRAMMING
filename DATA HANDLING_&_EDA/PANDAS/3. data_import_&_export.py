import pandas as pd 

df1 = pd.read_csv('input.csv')
print(df1)

df2 = pd.DataFrame({
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Score': [89, 98, 76],
  'Grade': ['B', 'A', 'C']
})
df2.to_csv('output.csv', index=False)

