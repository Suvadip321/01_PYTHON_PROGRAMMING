import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John', 'Dean'],
    'Age': [25, 30, 28, 28, 32, 45],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'New York', 'Berlin'],
    'Salary': [50000, 60000, 70000, 55000, 65000, 50000],
    'Rating': [6, 7, 8, 9, 10, 8]
}
df = pd.DataFrame(data)

print("modifying column:")
df['Rating'] = df['Rating'] / 2
print(df)

print("adding new columns:")
df['Salary_k'] = df['Salary'] / 1000
print(df)

print("groupby transform:")
df['avg_salary'] = df.groupby('City')['Salary'].transform('mean')
print(df)

print("sorting:")
df_sorted = df.sort_values(['Rating', 'Salary'], ascending=[True, False])
print(df_sorted)
