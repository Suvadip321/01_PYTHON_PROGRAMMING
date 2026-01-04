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

print("creating dataframe from lists:")
columns = ['Name', 'Age', 'City', 'Salary']
rows = [
  ['Alice', 25, 'New York', 50000],
  ['Bob', 30, 'London', 60000 ],
  ['Charlie', 35, 'Tokyo', 70000],
  ['David', 28, 'Paris', 55000],
  ['John', 32, 'Berlin', 65000]
]
df = pd.DataFrame(rows)
print(df)

df = pd.DataFrame(rows, columns=columns)
print(df) 

df = pd.DataFrame(rows, columns=columns, index=[1, 2, 3, 4 ,5])
print(df) 

print("loc and iloc:")
print(f"loc:\n{df.loc[1]}")
print(f"iloc:\n{df.iloc[1]}")

print("add a new column:")
df['Profession'] = ['Software Developer', 'Data Scientist', 'ML Engineer', 'Cybersecurity Analyst', 'Database Administrator']
print(df)

print("add new rows:")
new_df = pd.DataFrame({
  'Name': ['Dean', 'Charles'],
  'Age': [29, 33],
  'City': ['London', 'New York'],
  'Salary': [57000, 62000],
  'Profession': ['Software Engineer', 'Data Analyst']
}, index=[6, 7])

df = pd.concat([df, new_df])
print(df)