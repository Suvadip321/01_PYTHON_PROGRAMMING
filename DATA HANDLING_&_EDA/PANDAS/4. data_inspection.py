import pandas as pd 

df = pd.read_csv('IPL2025Batters.csv')
print(df)

print(f"shape:\n{df.shape}")
print(f"dtypes:\n{df.dtypes}")
print(f"columns:\n{df.columns}")
print(f"head:\n{df.head()}")
print(f"tail:\n{df.tail()}")
print(f"info:\n{df.info()}")
print(f"describe:\n{df.describe()}")
print(f"unique values in 'Team' column:\n{df['Team'].unique()}")
print(f"value counts in 'Team' column:\n{df['Team'].value_counts()}")
