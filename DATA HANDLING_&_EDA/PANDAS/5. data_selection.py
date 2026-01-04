import pandas as pd 

df = pd.read_csv('IPL2025Batters.csv')

print("selection by column/s:")
print(df['Player Name'])
print(df[['Player Name', 'Runs']])

print("selection by row/s:")
print(df.loc[0])
df = pd.read_csv('IPL2025Batters.csv', index_col='Player Name')

print(df.loc['Sai Sudharsan',['Runs', 'SR']])
print(df.loc['Sai Sudharsan':'Virat Kohli',['Runs', 'SR']])

print(df.iloc[0:11])
print(df.iloc[0:11:2])

print(df.iloc[0:11, 0:3])


