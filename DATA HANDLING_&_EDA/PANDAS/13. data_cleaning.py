import numpy as np 
import pandas as pd 

data = {
  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John', 'Dean'],
  'Age': [25, 30, np.nan, 28, 32, np.nan],
  'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin', 'Singapore'],
  'Salary': [50000, 60000, 70000, 55000, np.nan, 50000],
  'Grade': ['A', 'B', 'A', 'C', 'A', 'B']
}

df = pd.DataFrame(data)
print(df)

print("drop any column:")
df = df.drop(columns=['Grade'])
print(df)

print("handling missing values:")
print(df.isna())
print(df.isna().sum())

print(df.dropna(subset=['Age', 'Salary']))
print(df.fillna({'Age': df['Age'].mean(), 'Salary': df['Salary'].median()}))

print("removing duplicates:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df)
