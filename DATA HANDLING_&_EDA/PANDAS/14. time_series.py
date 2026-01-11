import pandas as pd

data = {
    'date': ['2023-01-05', '2023-02-12', '2023-03-18', '2023-01-20', '2023-02-28'],
    'sales': [100, 150, 130, 120, 170]
}
df = pd.DataFrame(data)

print("raw data:")
print(df)

print("convert to datetime:")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
print(df)

print("datetime feature extraction:")
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday
df['is_weekend'] = df['weekday'] >= 5
print(df)

print("sort by time:")
df = df.sort_values('date')
print(df)

print("time-based filtering:")
filtered = df[df['date'] >= '2023-02-01']
print(filtered)

print("time difference feature:")
df['days_since_start'] = (df['date'] - df['date'].min()).dt.days
print(df)
