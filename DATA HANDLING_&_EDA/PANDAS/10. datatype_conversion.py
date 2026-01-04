import numpy as np 
import pandas as pd 

data = {
  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John', 'Dean'],
  'Age': [25, 30, 35, 28, 32, 27],
  'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin', 'Singapore'],
  'Salary': [50000, 60000, 70000, 55000, 57000, 50000],
  'Grade': ['A', 'B', 'A', 'C', 'A', 'B']
}
df = pd.DataFrame(data)
print(df)

print("data type conversion:")
df['Salary'] = df['Salary'].astype(float)
df['City'] = df['City'].astype('category')
print(df) 

print("string operations:")
df['Name_lower'] = df['Name'].str.lower()
df['Name_upper'] = df['Name'].str.upper()
df['City'] = df['City'].str.replace('New York', 'NYC')
print(df)

