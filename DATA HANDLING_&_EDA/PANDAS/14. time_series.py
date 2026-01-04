import pandas as pd 
import numpy as np 

# create date range
dates = pd.date_range('2023-01-01', '2023-12-31', freq='M')
print(dates)
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
print(dates)
data = pd.DataFrame({
  'Date': dates,
  'Sales': np.random.randint(100, 500, size=100),
  'Visitors': np.random.randint(50, 200, size=100)
})
print(data)

# entering dates manually
df = pd.DataFrame({
  'Sales': [22, 15, 41]
})
df['Date'] = pd.to_datetime(['2023-01-01', '2023-06-15', '2023-12-31'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Quarter'] = df['Date'].dt.quarter
print(df)

today = pd.Timestamp.now()
print(today)
