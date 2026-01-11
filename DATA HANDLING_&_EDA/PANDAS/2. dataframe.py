import pandas as pd

print("creating dataframe from dictionary:")
data = {
  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John'],
  'Age': [25, 30, 35, 28, 32],
  'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin'],
  'Salary': [50000, 60000, 70000, 55000, 65000]
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=[1, 2, 3, 4, 5])
print(df)

print("accessing columns:")
print(f"Name column:\n{df['Name']}")
print(f"Name and Age columns:\n{df[['Name', 'Age']]}")

print("loc and iloc:")
print(f"loc:\n{df.loc[1]}")
print(f"iloc:\n{df.iloc[0]}")
