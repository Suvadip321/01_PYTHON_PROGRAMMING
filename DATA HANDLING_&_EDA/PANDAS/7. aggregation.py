import pandas as pd 

df = pd.read_csv('IPL2025Batters.csv')

print("whole dataframe:")
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))

print("by column:")
print(df['Runs'].mean())
print(df['Runs'].sum())
print(df['Runs'].min())
print(df['Runs'].max())

