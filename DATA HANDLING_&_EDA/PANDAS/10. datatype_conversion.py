import pandas as pd 

data = {
  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John', 'Dean'],
  'Age': ["25", "30", "28", "28", "32", "45"],
  'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin', 'Singapore'],
  'Salary': ["50000", "60000", "70000", "55000", "65000", "48000"],
  'Grade': ['A', 'B', 'A', 'C', 'A', 'B']
}
df = pd.DataFrame(data)
print(df)

print("data type conversion:")
df['Age'] = df['Age'].astype(int)
df['Salary'] = pd.to_numeric(df['Salary'])
print(df)

print("string operations:")
df['Name'] = df['Name'].str.strip()
df['Name_lower'] = df['Name'].str.lower()
df['Name_upper'] = df['Name'].str.upper()
print(df)
