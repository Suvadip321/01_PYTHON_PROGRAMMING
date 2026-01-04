import numpy as np 
import pandas as pd 

data = {
  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John', 'Dean'],
  'Age': [25, 30, np.nan, 28, 32, np.nan],
  'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin', 'Singapore'],
  'Salary': [50000, 60000, 70000, 55000, np.nan, 50000],
  'Rating': [6, 7, 8, 9, 10, 8]
}
df = pd.DataFrame(data)

print("adding new columns:")
df['Salary_k'] = df['Salary'] / 1000
print(df)

print("apply functions:")
df['Rating'] = df['Rating'].apply(lambda x: x / 2)
print(df)

print("sorting:")
df_sorted = df.sort_values('Rating')
print(df_sorted)
df_sorted = df.sort_values('Rating', ascending=False)
print(df_sorted)