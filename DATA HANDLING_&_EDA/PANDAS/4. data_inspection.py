import pandas as pd

import pandas as pd 

df = pd.read_csv('IPL2025Batters.csv')
print(df)

print(f"shape:\n{df.shape}")
print(f"dtypes:\n{df.dtypes}")
print(f"info:\n{df.info()}")
print(f"describe:\n{df.describe()}")
print(f"head:\n{df.head()}")
print(f"tail:\n{df.tail()}")
print(f"index:\n{df.index}")
print(f"columns:\n{df.columns}")
