import pandas as pd

df = pd.read_csv('IPL2025Batters.csv', index_col='Player Name')

# 1. Select one row by label
one_player = df.loc['Virat Kohli']

# 2. Select specific rows and columns by label
player_stats = df.loc[['Virat Kohli', 'Rohit Sharma'], ['Runs', 'SR']]

# 3. Label-based slicing (inclusive)
range_slice = df.loc['Sai Sudharsan':'Virat Kohli', ['Runs', 'SR']]

# 4. Select all rows, selected columns
runs_and_sr = df.loc[:, ['Runs', 'SR']]

# 5. Boolean filtering (MOST COMMON)
high_scorers = df.loc[df['Runs'] > 400, ['Runs', 'SR']]

# 6. Boolean filtering with multiple conditions
elite = df.loc[(df['Runs'] > 400) & (df['SR'] > 140)]

# 7. Select first N rows (positional)
first_10 = df.iloc[:10]

# 8. Select last N rows
last_5 = df.iloc[-5:]

# 9. Positional slicing (rows + columns)
positional_slice = df.iloc[0:10, 0:3]

# 10. Scalar access (row + column)
virat_runs = df.loc['Virat Kohli', 'Runs']
